#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Paso de construcción determinista del repositorio `cti_daily`.

Hace cuatro cosas y ninguna de ellas requiere red:

  1. Regenera el HTML de todo informe cuyo `.md` sea más reciente (el `.md` manda).
  2. Regenera el índice del README entre las marcas AUTO-ÍNDICE.
  3. Regenera los agregados `ioc_ipv4.txt`, `ioc_ipv6.txt` e `ioc_url.txt`.
  4. Informa del estado de vigencia de cada informe: eso es lo que decide, cada
     día, sobre qué hay que volver a investigar.

Lo que este script NO hace —y no puede hacer— es averiguar si hay información
nueva sobre un actor. Eso exige un analista o un agente con acceso a fuentes.
El script prepara la decisión; no la toma.

Uso:
    python3 tools/cti_build.py              # construye y escribe
    python3 tools/cti_build.py --check      # no escribe; sale 1 si algo cambiaría (CI)
    python3 tools/cti_build.py --force      # regenera todos los HTML aunque no toque el .md
    python3 tools/cti_build.py --json       # estado de vigencia en JSON, para automatizar

Sin dependencias: sólo la biblioteca estándar de Python 3.8+.
"""

import argparse
import csv
import datetime as _dt
import filecmp
import io
import ipaddress
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ───────────────────────────────────────────────────────────────────────────
# Política de publicación.
#
# Sólo los informes cuyo marcado TLP esté en este conjunto entran en el índice
# público y en los agregados de IOC. El repositorio es público: un informe
# TLP:AMBER o superior que se añada mañana quedará fuera por diseño, sin
# depender de que alguien se acuerde. Si algún día el repositorio pasa a
# privado, amplíese este conjunto de forma explícita y documentada.
# ───────────────────────────────────────────────────────────────────────────
TLP_PUBLICABLE = {"TLP:CLEAR", "TLP:WHITE"}

MARCA_INI = "<!-- AUTO-ÍNDICE: no editar a mano. Lo regenera tools/cti_build.py -->"
MARCA_FIN = "<!-- FIN AUTO-ÍNDICE -->"

FICHEROS_IOC = {
    "ipv4": "ioc_ipv4.txt",
    "ipv6": "ioc_ipv6.txt",
    "url": "ioc_url.txt",
}

# El índice con contexto. Los `ioc_*.txt` son listas planas para ingesta
# automática; este CSV es la misma información con lo que esas listas pierden:
# de qué informe sale cada indicador, con qué confianza, qué acción permite y
# por qué está ahí. Incluye TODOS los tipos de indicador, no sólo los tres que
# tienen fichero agregado propio: hashes, nombres de fichero, agentes de
# usuario, identificadores de aplicación, ASN, CVE y cuanto declare el Anexo A.
FICHERO_INDICE = "ioc_index.csv"

COLUMNAS_INDICE = [
    "informe", "fecha_informe", "tlp", "pap", "tipo", "valor", "puerto",
    "confianza", "caducidad", "accion_permitida", "agregado", "contexto",
]

# Tipos de la primera columna del Anexo A que alimentan cada fichero.
TIPO_A_FICHERO = {
    "ipv4": "ipv4",
    "ip": "ipv4",
    "ipv6": "ipv6",
    "domain": "url",
    "dominio": "url",
    "url": "url",
    "fqdn": "url",
    "hostname": "url",
}

RE_DOMINIO = re.compile(
    r"^(?=.{1,253}$)(?!-)[a-z0-9-]{1,63}(?<!-)(\.(?!-)[a-z0-9-]{1,63}(?<!-))+$", re.I
)


# ───────────────────────────────────────────────────── utilidades de lectura

def desenmascarar(v):
    """Revierte el ofuscado defensivo habitual: 1.2.3[.]4 → 1.2.3.4"""
    v = v.strip().strip("`").strip()
    v = v.replace("[.]", ".").replace("(.)", ".").replace("{.}", ".")
    v = v.replace("[:]", ":").replace("[@]", "@")
    v = re.sub(r"^h(?:xx|XX)p(s?)://", r"http\1://", v)
    v = re.sub(r"^\[|\]$", "", v)
    return v.strip()


def frontmatter(texto):
    """Subconjunto de YAML suficiente para la cabecera de estos informes."""
    if not texto.startswith("---"):
        return {}
    fin = texto.find("\n---", 3)
    if fin < 0:
        return {}
    datos = {}
    for linea in texto[3:fin].split("\n"):
        m = re.match(r'^([a-z_]+):\s*(.*)$', linea.strip())
        if not m:
            continue
        clave, valor = m.group(1), m.group(2).strip()
        if valor.startswith('"') and valor.endswith('"') and len(valor) > 1:
            valor = valor[1:-1]
        datos[clave] = valor
    return datos


def informes():
    """Devuelve los informes ordenados por identificador."""
    salida = []
    for nombre in sorted(os.listdir(RAIZ)):
        if not re.match(r"^CTI-\d{4}-\d{3}.*\.md$", nombre):
            continue
        ruta = os.path.join(RAIZ, nombre)
        texto = open(ruta, encoding="utf-8").read()
        fm = frontmatter(texto)
        salida.append({
            "md": nombre,
            "html": nombre[:-3] + ".html",
            "ruta": ruta,
            "texto": texto,
            "fm": fm,
            "id": fm.get("id", nombre[:12]),
            "tlp": fm.get("tlp", "").upper(),
            "publicable": fm.get("tlp", "").upper() in TLP_PUBLICABLE,
        })
    return salida


# ─────────────────────────────────────────────────────────── extracción IOC

def _normalizar_cabecera(c):
    return re.sub(r"[*`]", "", c).strip().lower()


def _limpiar_prosa(c):
    """Deja una celda de tabla legible en un CSV: sin énfasis ni comillas."""
    c = re.sub(r"\*\*|\*|`", "", c)
    c = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", c)   # enlaces → sólo el texto
    return re.sub(r"\s+", " ", c).strip()


ALIAS_COLUMNA = {
    "tipo": ("tipo", "type"),
    "valor": ("valor", "value", "indicador"),
    "contexto": ("contexto", "context", "descripción", "descripcion"),
    "confianza": ("confianza", "confidence"),
    "caducidad": ("caducidad", "validez", "vigencia"),
    "accion": ("acción permitida", "accion permitida", "uso",
               "acción", "accion", "acción recomendada"),
}

NORMALIZA_TIPO = {
    "sha-256": "sha256", "sha-1": "sha1", "sha-512": "sha512",
    "md-5": "md5", "ip": "ipv4", "dominio": "domain",
    "user-agent": "useragent", "agente de usuario": "useragent",
    "nombre de fichero": "filename", "ruta": "filepath",
}


def filas_ioc(inf):
    """Genera una fila por indicador a partir de las tablas marcadas `cti:ioc`.

    Un único parser alimenta tanto los agregados `ioc_*.txt` como el índice
    `ioc_index.csv`: así no puede ocurrir que un fichero contenga un indicador
    que el otro no.

    Tres cosas que este parser hace y conviene no deshacer:

    - **Mapea las columnas por nombre, no por posición.** Las tablas no son
      uniformes entre informes: CTI-2026-014 tiene una con columna `Caducidad`
      y otra sin `Confianza`. Por posición se leería la confianza de una
      columna que contiene otra cosa.
    - **Sigue dentro del anexo al cruzar un `###`.** El Anexo A de 014 está
      dividido en A.1 a A.4, y detenerse en el primer subtítulo dejaba fuera
      la infraestructura de red de A.3. Sólo termina en el siguiente `## `.
    - **Toma como valores los segmentos entre tildes invertidas, y no los
      parte más.** Una celda puede llevar varios indicadores, cada uno
      entrecomillado; partir además por `·` destrozaría valores que contienen
      ese carácter, como el marcador de auditoría de ARTEX.

    Deliberadamente NO rastrea la prosa: las tablas del Anexo A son la lista
    curada, con contexto, confianza y acción permitida, mientras que la prosa
    contiene indicadores citados, ejemplos y variantes señaladas como erróneas
    —como la errata de transcripción que CTI-2026-019 documenta en una IP de
    Microsoft—. Agregarla produciría ruido que nadie podría auditar después.
    """
    fm = inf["fm"]
    dentro, mapa = False, None
    for linea in inf["texto"].split("\n"):
        if "<!-- cti:ioc" in linea:
            dentro, mapa = True, None
            continue
        if not dentro:
            continue
        if linea.startswith("## "):          # fin del anexo
            dentro, mapa = False, None
            continue
        s = linea.strip()
        if not s.startswith("|"):
            continue
        celdas = [c.strip() for c in s.strip("|").split("|")]
        normal = [_normalizar_cabecera(c) for c in celdas]
        if normal and set("".join(normal)) <= set("-: "):
            continue                         # fila separadora
        if "tipo" in normal and ("valor" in normal or "indicador" in normal):
            mapa = {}
            for idx, nombre in enumerate(normal):
                for campo, alias in ALIAS_COLUMNA.items():
                    if nombre in alias and campo not in mapa:
                        mapa[campo] = idx
            continue
        if not mapa or "valor" not in mapa:
            continue

        def celda(campo):
            i = mapa.get(campo)
            return celdas[i] if i is not None and i < len(celdas) else ""

        tipo = _normalizar_cabecera(celda("tipo"))
        tipo = NORMALIZA_TIPO.get(tipo, tipo)
        bruto = celda("valor")
        valores = re.findall(r"`([^`]+)`", bruto)
        if not valores and bruto:
            valores = [bruto]
        for v in valores:
            valor = desenmascarar(v)
            if not valor or valor.startswith("(") or valor in ("—", "-"):
                continue
            puerto = ""
            # tipos del estilo `ipv4:puerto`, con el valor 1.2.3.4:5678
            if tipo.startswith(("ipv4", "ip")) and ":" in valor:
                posible, _, resto = valor.partition(":")
                if resto.isdigit():
                    try:
                        ipaddress.IPv4Address(posible)
                        valor, puerto = posible, resto
                    except ValueError:
                        pass
            yield {
                "informe": inf["id"],
                "fecha_informe": fm.get("fecha", ""),
                "tlp": inf["tlp"],
                "pap": fm.get("pap", ""),
                "tipo": tipo,
                "valor": valor,
                "puerto": puerto,
                "confianza": _limpiar_prosa(celda("confianza")),
                "caducidad": _limpiar_prosa(celda("caducidad")),
                "accion_permitida": _limpiar_prosa(celda("accion")),
                "contexto": _limpiar_prosa(celda("contexto")),
            }


def clasificar(fila):
    """Devuelve el agregado `ioc_*.txt` que corresponde a la fila, o None."""
    destino = TIPO_A_FICHERO.get(fila["tipo"])
    if not destino and fila["tipo"].startswith("ipv4"):
        destino = "ipv4"                     # cubre `ipv4:puerto`
    if not destino:
        return None
    v = fila["valor"]
    if destino == "ipv4":
        try:
            ipaddress.IPv4Address(v)
        except ValueError:
            return None
        return "ipv4"
    if destino == "ipv6":
        try:
            ipaddress.IPv6Address(v)
        except ValueError:
            return None
        return "ipv6"
    if "://" in v or RE_DOMINIO.match(v):
        return "url"
    return None


def construir_ioc(lista):
    """Devuelve (agregados ordenados, procedencia, filas del índice CSV)."""
    agregados = {k: set() for k in FICHEROS_IOC}
    procedencia = {k: {} for k in FICHEROS_IOC}
    indice = []
    for inf in lista:
        if not inf["publicable"]:
            continue
        for fila in filas_ioc(inf):
            clase = clasificar(fila)
            fila["agregado"] = FICHEROS_IOC[clase] if clase else ""
            indice.append(fila)
            if not clase:
                continue
            v = fila["valor"] if clase != "url" else (
                fila["valor"] if "://" in fila["valor"] else fila["valor"].lower())
            agregados[clase].add(v)
            procedencia[clase].setdefault(v, [])
            if inf["id"] not in procedencia[clase][v]:
                procedencia[clase][v].append(inf["id"])
    ordenado = {}
    for clase, valores in agregados.items():
        if clase == "ipv4":
            ordenado[clase] = sorted(valores, key=lambda x: int(ipaddress.IPv4Address(x)))
        elif clase == "ipv6":
            ordenado[clase] = sorted(valores, key=lambda x: int(ipaddress.IPv6Address(x)))
        else:
            ordenado[clase] = sorted(valores)
    indice.sort(key=lambda f: (f["informe"], f["tipo"], f["valor"]))
    return ordenado, procedencia, indice


# ──────────────────────────────────────────────────────────────── vigencia

def vigencia(fm, hoy):
    """Estado de caducidad: lo que decide si hoy hay que reinvestigar."""
    caduca = fm.get("caduca", "")
    try:
        f = _dt.date.fromisoformat(caduca)
    except ValueError:
        return "sin fecha", None
    dias = (f - hoy).days
    if dias < 0:
        return "caducado", dias
    if dias <= 14:
        return "por caducar", dias
    return "vigente", dias


ETIQUETA = {
    "vigente": "vigente",
    "por caducar": "**por caducar**",
    "caducado": "**CADUCADO**",
    "sin fecha": "sin fecha",
}


# ───────────────────────────────────────────────────────────────── renderizado

def renderizar(lista, forzar=False, simular=False):
    """Regenera el HTML que no coincida con lo que produce su `.md`.

    La comparación es **por contenido, no por fecha de modificación**. git no
    preserva los mtime: en un clon nuevo o en un runner de CI todos los
    ficheros reciben la hora del checkout en un orden arbitrario, así que
    comparar mtimes da un resultado aleatorio —y de hecho hizo fallar la
    primera ejecución del flujo de verificación, que declaró obsoleto un
    informe intacto—. El renderizador es determinista: produce el mismo byte
    para la misma entrada. La pregunta correcta, por tanto, es si el HTML
    publicado es el que produce el `.md` de hoy.
    """
    hechos = []
    tmp = tempfile.mkdtemp(prefix="cti-build-")
    try:
        for inf in lista:
            destino = os.path.join(RAIZ, inf["html"])
            candidato = os.path.join(tmp, inf["html"])
            proc = subprocess.run(
                [sys.executable, os.path.join(RAIZ, "render", "cti_render.py"),
                 inf["ruta"], "-o", candidato],
                check=True, cwd=RAIZ,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
            )
            # El renderizador anuncia cada éxito por stderr: eso es ruido aquí.
            # Sus avisos de directiva mal puesta, en cambio, hay que verlos.
            for linea in (proc.stderr or "").splitlines():
                if re.search(r"aviso|error|warning", linea, re.I):
                    print("  %s: %s" % (inf["md"], linea.strip()), file=sys.stderr)
            igual = os.path.exists(destino) and \
                filecmp.cmp(candidato, destino, shallow=False)
            if igual and not forzar:
                continue
            hechos.append(inf["md"])
            if not simular:
                shutil.copyfile(candidato, destino)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return hechos


# ───────────────────────────────────────────────────────────────────── índice

def tabla_indice(lista, hoy):
    filas = [
        "| Informe | Tema | Tipo | Fecha | Ver. | TLP | Vigencia | Formatos |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for inf in lista:
        fm = inf["fm"]
        estado, dias = vigencia(fm, hoy)
        if estado == "caducado":
            vig = "%s · hace %d d" % (ETIQUETA[estado], abs(dias))
        elif dias is not None:
            vig = "%s · %d d" % (ETIQUETA[estado], dias)
        else:
            vig = ETIQUETA[estado]
        if not inf["publicable"]:
            filas.append(
                "| `%s` | *no publicado — %s* | — | %s | — | `%s` | — | — |"
                % (inf["id"], inf["tlp"] or "sin marcado", fm.get("fecha", ""), inf["tlp"])
            )
            continue
        filas.append(
            "| `%s` | %s | %s | %s | %s | `%s` | %s | [md](%s) · [html](%s) |"
            % (
                inf["id"],
                fm.get("actor", "—"),
                fm.get("tipo", "—"),
                fm.get("fecha", "—"),
                fm.get("version", "—"),
                inf["tlp"] or "—",
                vig,
                inf["md"],
                inf["html"],
            )
        )
    return "\n".join(filas)


def tabla_ioc(ioc, procedencia, indice):
    filas = [
        "| Fichero | Indicadores | Tipos incluidos | Informes que aportan |",
        "|---|---|---|---|",
    ]
    desc = {
        "ipv4": "`ipv4`, `ip`, `ipv4:puerto`",
        "ipv6": "`ipv6`",
        "url": "`domain`, `url`, `fqdn`, `hostname`",
    }
    for clase, fichero in FICHEROS_IOC.items():
        fuentes = sorted({i for v in ioc[clase] for i in procedencia[clase][v]})
        filas.append(
            "| [`%s`](%s) | %d | %s | %s |"
            % (fichero, fichero, len(ioc[clase]), desc[clase],
               ", ".join("`%s`" % f for f in fuentes) if fuentes else "—")
        )
    tipos = sorted({f["tipo"] for f in indice})
    fuentes = sorted({f["informe"] for f in indice})
    filas.append(
        "| [`%s`](%s) | %d | todos: %s | %s |"
        % (FICHERO_INDICE, FICHERO_INDICE, len(indice),
           ", ".join("`%s`" % t for t in tipos) if tipos else "—",
           ", ".join("`%s`" % f for f in fuentes) if fuentes else "—")
    )
    return "\n".join(filas)


def bloque_indice(lista, ioc, procedencia, indice, hoy):
    publicables = [i for i in lista if i["publicable"]]
    total_ioc = sum(len(v) for v in ioc.values())
    caducados = [i for i in publicables if vigencia(i["fm"], hoy)[0] == "caducado"]
    por_caducar = [i for i in publicables if vigencia(i["fm"], hoy)[0] == "por caducar"]

    partes = [
        MARCA_INI,
        "",
        "### Informes",
        "",
        tabla_indice(lista, hoy),
        "",
        "### Agregados de indicadores",
        "",
        tabla_ioc(ioc, procedencia, indice),
        "",
        "### Estado del ciclo",
        "",
        "| Métrica | Valor |",
        "|---|---|",
        "| Informes publicados | %d |" % len(publicables),
        "| Indicadores en listas planas | %d |" % total_ioc,
        "| Indicadores en el índice con contexto | %d |" % len(indice),
        "| Caducados (exigen revisión) | %d%s |" % (
            len(caducados),
            " — " + ", ".join("`%s`" % i["id"] for i in caducados) if caducados else "",
        ),
        "| Por caducar en 14 días | %d%s |" % (
            len(por_caducar),
            " — " + ", ".join("`%s`" % i["id"] for i in por_caducar) if por_caducar else "",
        ),
        "| Última construcción | %s |" % hoy.isoformat(),
        "",
        MARCA_FIN,
    ]
    return "\n".join(partes)


# ─────────────────────────────────────────────────────────────────── escritura

def escribir_si_cambia(ruta, contenido, simular):
    anterior = None
    if os.path.exists(ruta):
        anterior = open(ruta, encoding="utf-8").read()
    if anterior == contenido:
        return False
    if not simular:
        with open(ruta, "w", encoding="utf-8") as fh:
            fh.write(contenido)
    return True


def main():
    ap = argparse.ArgumentParser(description="Construcción del repositorio cti_daily")
    ap.add_argument("--check", action="store_true",
                    help="no escribe nada; sale con 1 si algo cambiaría")
    ap.add_argument("--force", action="store_true",
                    help="regenera todos los HTML aunque el .md no sea más reciente")
    ap.add_argument("--json", action="store_true",
                    help="volca el estado de vigencia en JSON y termina")
    opt = ap.parse_args()

    hoy = _dt.date.today()
    lista = informes()
    if not lista:
        sys.exit("error: no encuentro ningún informe CTI-*.md en %s" % RAIZ)

    if opt.json:
        print(json.dumps({
            "fecha": hoy.isoformat(),
            "informes": [
                {
                    "id": i["id"],
                    "md": i["md"],
                    "actor": i["fm"].get("actor", ""),
                    "fecha": i["fm"].get("fecha", ""),
                    "caduca": i["fm"].get("caduca", ""),
                    "version": i["fm"].get("version", ""),
                    "tlp": i["tlp"],
                    "publicable": i["publicable"],
                    "estado": vigencia(i["fm"], hoy)[0],
                    "dias": vigencia(i["fm"], hoy)[1],
                }
                for i in lista
            ],
        }, ensure_ascii=False, indent=2))
        return 0

    cambios = []

    rehechos = renderizar(lista, forzar=opt.force, simular=opt.check)
    if rehechos:
        cambios.append("HTML regenerado: " + ", ".join(rehechos))

    ioc, procedencia, indice = construir_ioc(lista)
    for clase, fichero in FICHEROS_IOC.items():
        cuerpo = "".join(v + "\n" for v in ioc[clase])
        if escribir_si_cambia(os.path.join(RAIZ, fichero), cuerpo, opt.check):
            cambios.append("%s (%d indicadores)" % (fichero, len(ioc[clase])))

    buf = io.StringIO()
    escritor = csv.DictWriter(buf, fieldnames=COLUMNAS_INDICE,
                              lineterminator="\n", extrasaction="ignore")
    escritor.writeheader()
    for fila in indice:
        escritor.writerow(fila)
    if escribir_si_cambia(os.path.join(RAIZ, FICHERO_INDICE), buf.getvalue(), opt.check):
        cambios.append("%s (%d indicadores con contexto)" % (FICHERO_INDICE, len(indice)))

    ruta_readme = os.path.join(RAIZ, "README.md")
    if os.path.exists(ruta_readme):
        readme = open(ruta_readme, encoding="utf-8").read()
        nuevo = bloque_indice(lista, ioc, procedencia, indice, hoy)
        if MARCA_INI in readme and MARCA_FIN in readme:
            ini = readme.index(MARCA_INI)
            fin = readme.index(MARCA_FIN) + len(MARCA_FIN)
            readme2 = readme[:ini] + nuevo + readme[fin:]
            if escribir_si_cambia(ruta_readme, readme2, opt.check):
                cambios.append("README.md (índice)")
        else:
            print("aviso: no encuentro las marcas AUTO-ÍNDICE en README.md; "
                  "el índice no se ha tocado", file=sys.stderr)
    else:
        print("aviso: no hay README.md", file=sys.stderr)

    # informe de vigencia, siempre a stdout: es el insumo de la decisión diaria
    print("── estado de vigencia · %s ──" % hoy.isoformat())
    for i in lista:
        estado, dias = vigencia(i["fm"], hoy)
        marca = {"caducado": "✗", "por caducar": "!", "vigente": "·", "sin fecha": "?"}[estado]
        print("  %s %-14s %-11s %s" % (
            marca, i["id"], estado,
            ("hace %d d" % abs(dias)) if dias is not None and dias < 0
            else ("%d d" % dias) if dias is not None else ""))

    if opt.check:
        if cambios:
            print("\n--check: hay %d artefacto(s) derivado(s) sin regenerar:" % len(cambios),
                  file=sys.stderr)
            for c in cambios:
                print("  - " + c, file=sys.stderr)
            print("\nEjecuta: python3 tools/cti_build.py", file=sys.stderr)
            return 1
        print("\n--check: todo al día.")
        return 0

    if cambios:
        print("\nactualizado:")
        for c in cambios:
            print("  ✓ " + c)
    else:
        print("\nsin cambios: todo estaba al día.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
