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
import datetime as _dt
import ipaddress
import json
import os
import re
import subprocess
import sys

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

def extraer_ioc(inf):
    """Extrae indicadores de las tablas marcadas con `cti:ioc`.

    Deliberadamente NO rastrea la prosa. Las tablas del Anexo A son la lista
    curada, con contexto, confianza y acción permitida; la prosa contiene
    indicadores citados, variantes erróneas señaladas como tales y ejemplos.
    Agregar la prosa produciría ruido que nadie podría auditar después.
    """
    halladas = {k: set() for k in FICHEROS_IOC}
    en_tabla = False
    for linea in inf["texto"].split("\n"):
        if "<!-- cti:ioc" in linea:
            en_tabla = True
            continue
        if en_tabla and linea.startswith("#"):
            en_tabla = False            # se acabó el anexo
            continue
        if not en_tabla or not linea.lstrip().startswith("|"):
            continue
        celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
        if len(celdas) < 2:
            continue
        tipo = celdas[0].lower().strip("* `")
        destino = TIPO_A_FICHERO.get(tipo)
        if not destino:
            continue
        # una celda puede llevar varios valores separados por · o coma
        crudos = re.findall(r"`([^`]+)`", celdas[1]) or [celdas[1]]
        for crudo in crudos:
            for parte in re.split(r"[·,;]| y ", crudo):
                valor = desenmascarar(parte)
                if not valor or valor.startswith("("):
                    continue
                if destino == "ipv4":
                    try:
                        ip = ipaddress.IPv4Address(valor)
                    except ValueError:
                        continue
                    halladas["ipv4"].add(str(ip))
                elif destino == "ipv6":
                    try:
                        ip = ipaddress.IPv6Address(valor)
                    except ValueError:
                        continue
                    halladas["ipv6"].add(str(ip))
                else:
                    if "://" in valor:
                        halladas["url"].add(valor)
                    elif RE_DOMINIO.match(valor):
                        halladas["url"].add(valor.lower())
    return halladas


def construir_ioc(lista):
    agregados = {k: set() for k in FICHEROS_IOC}
    procedencia = {k: {} for k in FICHEROS_IOC}
    for inf in lista:
        if not inf["publicable"]:
            continue
        for clase, valores in extraer_ioc(inf).items():
            agregados[clase] |= valores
            for v in valores:
                procedencia[clase].setdefault(v, []).append(inf["id"])
    ordenado = {}
    for clase, valores in agregados.items():
        if clase == "ipv4":
            ordenado[clase] = sorted(valores, key=lambda x: int(ipaddress.IPv4Address(x)))
        elif clase == "ipv6":
            ordenado[clase] = sorted(valores, key=lambda x: int(ipaddress.IPv6Address(x)))
        else:
            ordenado[clase] = sorted(valores)
    return ordenado, procedencia


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
    """Regenera el HTML de los informes cuyo .md sea más reciente."""
    hechos = []
    for inf in lista:
        html = os.path.join(RAIZ, inf["html"])
        hay_que = forzar or not os.path.exists(html) or \
            os.path.getmtime(inf["ruta"]) > os.path.getmtime(html)
        if not hay_que:
            continue
        hechos.append(inf["md"])
        if simular:
            continue
        subprocess.run(
            [sys.executable, os.path.join(RAIZ, "render", "cti_render.py"), inf["ruta"]],
            check=True, cwd=RAIZ, stdout=subprocess.DEVNULL,
        )
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


def tabla_ioc(ioc, procedencia):
    filas = [
        "| Fichero | Indicadores | Tipos incluidos | Informes que aportan |",
        "|---|---|---|---|",
    ]
    desc = {
        "ipv4": "`ipv4`, `ip`",
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
    return "\n".join(filas)


def bloque_indice(lista, ioc, procedencia, hoy):
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
        tabla_ioc(ioc, procedencia),
        "",
        "### Estado del ciclo",
        "",
        "| Métrica | Valor |",
        "|---|---|",
        "| Informes publicados | %d |" % len(publicables),
        "| Indicadores agregados | %d |" % total_ioc,
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

    ioc, procedencia = construir_ioc(lista)
    for clase, fichero in FICHEROS_IOC.items():
        cuerpo = "".join(v + "\n" for v in ioc[clase])
        if escribir_si_cambia(os.path.join(RAIZ, fichero), cuerpo, opt.check):
            cambios.append("%s (%d indicadores)" % (fichero, len(ioc[clase])))

    ruta_readme = os.path.join(RAIZ, "README.md")
    if os.path.exists(ruta_readme):
        readme = open(ruta_readme, encoding="utf-8").read()
        nuevo = bloque_indice(lista, ioc, procedencia, hoy)
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
