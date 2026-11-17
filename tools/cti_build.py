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
    "hash": "ioc_hash.txt",
}

# El índice con contexto. Los `ioc_*.txt` son listas planas para ingesta
# automática; este CSV es la misma información con lo que esas listas pierden:
# de qué informe sale cada indicador, con qué confianza, qué acción permite y
# por qué está ahí. Incluye TODOS los tipos de indicador, no sólo los tres que
# tienen fichero agregado propio: hashes, nombres de fichero, agentes de
# usuario, identificadores de aplicación, ASN, CVE y cuanto declare el Anexo A.
FICHERO_INDICE = "ioc_index.csv"

# El mapa de relaciones. Se genera igual que la portada y por la misma razón:
# un diagrama con los datos incrustados a mano queda obsoleto en silencio en
# cuanto se publica un informe nuevo, y nadie se entera. Aquí la fuente de
# verdad es `red-actores.json`; la plantilla sólo pone el motor alrededor, y la
# construcción comprueba que cada nodo apunte a un informe que existe y avisa
# de los informes que todavía no están en el grafo.
RED_DATOS = "red-actores.json"
RED_PLANTILLA = os.path.join("render", "red_actores_plantilla.html")
RED_SALIDA = "red-actores-3d.html"

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
    "sha256": "hash",
    "sha1": "hash",
    "sha512": "hash",
    "md5": "hash",
    "imphash": "hash",
}

# Longitud en caracteres hexadecimales de cada algoritmo admitido. Un valor que
# no case exactamente con una de estas longitudes no es un hash y se descarta:
# en las tablas del Anexo A conviven hashes con nombres de fichero y con notas.
LONGITUD_HASH = {32: "md5", 40: "sha1", 64: "sha256", 128: "sha512"}
RE_HEX = re.compile(r"^[0-9a-fA-F]+$")

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
    if destino == "hash":
        if RE_HEX.match(v) and len(v) in LONGITUD_HASH:
            return "hash"
        return None
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
            if clase == "hash":
                v = fila["valor"].lower()
            elif clase == "url" and "://" not in fila["valor"]:
                v = fila["valor"].lower()
            else:
                v = fila["valor"]
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
        elif clase == "hash":
            # agrupados por algoritmo: md5, sha1, sha256, sha512
            ordenado[clase] = sorted(valores, key=lambda x: (len(x), x))
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
        "hash": "`md5`, `sha1`, `sha256`, `sha512`, `imphash`",
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


PORTADA = "index.html"

CSS_PORTADA = """
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --amber:#f7a400;--mint:#4db99c;--deep:#375d9d;--sky:#5a7ebe;
  --amber-soft:rgba(247,164,0,.14);--mint-soft:rgba(77,185,156,.14);
  --bg:#080c18;--surface:#0f1830;--surface-2:#131e3a;
  --line:rgba(90,126,190,.22);--line-strong:rgba(90,126,190,.42);
  --ink:#e9eefb;--ink-2:#b9c6e2;--ink-3:#8294b8;
  --mono:ui-monospace,"SF Mono","JetBrains Mono",Menlo,Consolas,monospace;
  --sans:"Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;
  --r:14px;--r-s:9px;
}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--ink);font-family:var(--sans);
  line-height:1.62;-webkit-font-smoothing:antialiased;
  background-image:radial-gradient(1200px 600px at 20% -10%,rgba(55,93,157,.20),transparent 60%),
                   radial-gradient(900px 500px at 95% 5%,rgba(247,164,0,.07),transparent 55%);
  background-repeat:no-repeat}
.tlp-bar{background:#fff;color:#000;font-family:var(--mono);font-size:11.5px;
  letter-spacing:.14em;text-align:center;padding:5px 10px;font-weight:700}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px 72px}
header.hero{padding:62px 0 34px;border-bottom:1px solid var(--line)}
.eyebrow{font-family:var(--mono);font-size:12px;letter-spacing:.2em;
  text-transform:uppercase;color:var(--amber);margin-bottom:16px}
h1{font-size:clamp(30px,5.2vw,50px);line-height:1.08;letter-spacing:-.022em;font-weight:680}
.lede{color:var(--ink-2);font-size:17.5px;max-width:68ch;margin-top:18px}
h2{font-size:21px;letter-spacing:-.01em;margin:52px 0 6px;font-weight:620}
h2 .num{font-family:var(--mono);font-size:12px;color:var(--sky);
  letter-spacing:.14em;display:block;margin-bottom:7px;font-weight:500}
.sub{color:var(--ink-3);font-size:14.5px;margin-bottom:22px;max-width:70ch}
.grid{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(318px,1fr))}
.card{background:linear-gradient(180deg,var(--surface),var(--surface-2));
  border:1px solid var(--line);border-radius:var(--r);padding:20px 21px;
  display:flex;flex-direction:column;gap:11px;
  transition:border-color .18s ease,transform .18s ease}
.card:hover{border-color:var(--line-strong);transform:translateY(-2px)}
.card .id{font-family:var(--mono);font-size:11.5px;letter-spacing:.1em;color:var(--sky)}
.card h3{font-size:17px;line-height:1.3;letter-spacing:-.008em;font-weight:600}
.card h3 a{color:var(--ink);text-decoration:none}
.card h3 a:hover{color:var(--amber)}
.card .meta{color:var(--ink-3);font-size:13px;flex:1}
.pills{display:flex;flex-wrap:wrap;gap:6px}
.pill{font-family:var(--mono);font-size:10.5px;letter-spacing:.07em;padding:3px 8px;
  border-radius:99px;border:1px solid var(--line-strong);color:var(--ink-2);white-space:nowrap}
.pill.ok{background:var(--mint-soft);border-color:rgba(77,185,156,.5);color:#9fe0cb}
.pill.warn{background:var(--amber-soft);border-color:rgba(247,164,0,.5);color:#ffd27a}
.pill.bad{background:rgba(214,77,77,.16);border-color:rgba(214,77,77,.5);color:#ffb3b3}
.links{display:flex;gap:9px;border-top:1px solid var(--line);padding-top:12px}
.links a{font-family:var(--mono);font-size:12px;text-decoration:none;color:var(--ink-2);
  border:1px solid var(--line-strong);border-radius:var(--r-s);padding:5px 11px;transition:.16s}
.links a.primary{background:var(--amber);border-color:var(--amber);color:#1a1200;font-weight:600}
.links a:hover{border-color:var(--amber);color:var(--amber)}
.links a.primary:hover{color:#1a1200;filter:brightness(1.08)}
table{width:100%;border-collapse:collapse;font-size:14px;
  border:1px solid var(--line);border-radius:var(--r);overflow:hidden}
th,td{text-align:left;padding:11px 14px;border-bottom:1px solid var(--line);vertical-align:top}
th{background:rgba(55,93,157,.16);font-size:11.5px;font-family:var(--mono);
  letter-spacing:.1em;text-transform:uppercase;color:var(--ink-2);font-weight:600}
tr:last-child td{border-bottom:none}
td code,.mono{font-family:var(--mono);font-size:12.5px;color:var(--amber)}
td a{color:var(--sky)}
.note{border-left:3px solid var(--amber);background:var(--amber-soft);
  border-radius:0 var(--r-s) var(--r-s) 0;padding:16px 19px;margin:22px 0;
  font-size:14.5px;color:var(--ink-2)}
.note strong{color:var(--ink)}
.stats{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(168px,1fr))}
.stat{background:var(--surface);border:1px solid var(--line);
  border-radius:var(--r-s);padding:16px 17px}
.stat .n{font-family:var(--mono);font-size:27px;color:var(--amber);letter-spacing:-.02em}
.stat .l{color:var(--ink-3);font-size:12.5px;margin-top:3px;line-height:1.45}
footer{margin-top:58px;padding-top:22px;border-top:1px solid var(--line);
  color:var(--ink-3);font-size:13px}
footer a{color:var(--sky)}
@media(max-width:620px){header.hero{padding:38px 0 26px}.wrap{padding:0 16px 52px}
  table{font-size:13px}th,td{padding:9px 10px}}
"""


def pagina_portada(lista, ioc, indice, hoy, red_n=None):
    """Genera la portada de GitHub Pages.

    Se escribe aquí, y no a mano, por la misma razón que el índice del README:
    un listado mantenido a mano miente en cuanto se añade un informe. Reutiliza
    la paleta de `render/cti_theme.css` para que la portada no parezca ajena a
    los informes que indexa, y es autocontenida —sin CDN ni fuentes remotas—,
    igual que ellos.
    """
    import html as _h
    e = _h.escape
    publicables = [i for i in lista if i["publicable"]]
    reciente = max((i["fm"].get("fecha", "") for i in publicables), default="")

    tarjetas = []
    for inf in sorted(publicables, key=lambda x: x["id"], reverse=True):
        fm = inf["fm"]
        estado, dias = vigencia(fm, hoy)
        clase = {"vigente": "ok", "por caducar": "warn",
                 "caducado": "bad", "sin fecha": ""}[estado]
        if estado == "caducado":
            txt_vig = "caducado hace %d d" % abs(dias)
        elif dias is not None:
            txt_vig = "vigente · %d d" % dias
        else:
            txt_vig = "sin fecha"
        tarjetas.append(
            '<article class="card">\n'
            '  <div class="id">%s · %s</div>\n'
            '  <h3><a href="%s">%s</a></h3>\n'
            '  <div class="meta">%s</div>\n'
            '  <div class="pills"><span class="pill">v%s</span>'
            '<span class="pill">%s</span>'
            '<span class="pill %s">%s</span></div>\n'
            '  <div class="links"><a class="primary" href="%s">Leer el informe</a>'
            '<a href="%s">fuente .md</a></div>\n'
            '</article>' % (
                e(inf["id"]), e(fm.get("fecha", "")),
                e(inf["html"]), e(fm.get("actor", inf["id"])),
                e(fm.get("tipo", "")),
                e(fm.get("version", "?")), e(inf["tlp"] or "—"),
                clase, e(txt_vig),
                e(inf["html"]), e(inf["md"]),
            )
        )

    filas_ioc_tabla = []
    desc = {
        "ipv4": "Direcciones IPv4, una por línea, ya desenmascaradas",
        "ipv6": "Direcciones IPv6 (hoy ningún informe declara ninguna)",
        "url": "Dominios y URL, una por línea",
        "hash": "Hashes de fichero, agrupados por algoritmo según su longitud",
    }
    for clase, fichero in FICHEROS_IOC.items():
        filas_ioc_tabla.append(
            "<tr><td><a href=\"%s\"><code>%s</code></a></td><td class=\"mono\">%d</td>"
            "<td>%s</td></tr>" % (fichero, fichero, len(ioc[clase]), e(desc[clase]))
        )
    filas_ioc_tabla.append(
        "<tr><td><a href=\"%s\"><code>%s</code></a></td><td class=\"mono\">%d</td>"
        "<td>Todos los tipos, con informe de origen, confianza, caducidad, "
        "acción permitida y contexto. <strong>Es el que hay que ingerir.</strong></td></tr>"
        % (FICHERO_INDICE, FICHERO_INDICE, len(indice))
    )

    # El mapa sólo se anuncia si existe: la portada no debe enlazar un fichero
    # que la construcción no ha generado.
    bloque_red = ""
    if red_n:
        bloque_red = (
            '<h2><span class="num">02 · relaciones</span>Mapa de actores y herramientas</h2>\n'
            '<p class="sub">Las relaciones entre los actores y las herramientas de esta cartera, '
            'en un grafo tridimensional navegable. Se gira con el ratón, se filtra por tipo y cada '
            'nodo abre su ficha con enlace al informe de origen. Se regenera en cada construcción '
            'desde <code>%s</code>.</p>\n'
            '<div class="grid">\n'
            '<article class="card">\n'
            '  <div class="id">%d nodos · %d relaciones</div>\n'
            '  <h3><a href="%s">Red de actores y herramientas</a></h3>\n'
            '  <div class="meta">Actores estatales, clústeres, suministradores, herramientas propias '
            'y públicas, servicios legítimos abusados y vulnerabilidades.</div>\n'
            '  <div class="pills"><span class="pill">HTML autocontenido</span>'
            '<span class="pill">sin dependencias</span>'
            '<span class="pill ok">siempre al día</span></div>\n'
            '  <div class="links"><a class="primary" href="%s">Abrir el mapa</a>'
            '<a href="%s">datos .json</a></div>\n'
            '</article>\n'
            '</div>\n'
            '<div class="note">\n'
            '<strong>Lo que el mapa distingue, y es su razón de ser.</strong> No todas las relaciones '
            'valen lo mismo, y tratarlas como si lo fueran es la fuente de error más frecuente de '
            'esta disciplina. El trazo continuo marca lo establecido —<em>usa</em>, '
            '<em>suministra a</em>, <em>explota</em>, <em>entrega acceso a</em>—; el discontinuo, lo '
            'que no lo está: <em>solapamiento parcial</em>, <em>vinculado a</em>, <em>identidad en '
            'disputa</em> y <em>no es el mismo que</em>. Tres informes de esta cartera existen porque '
            'alguien compuso un solapamiento parcial con una equivalencia.\n'
            '</div>\n\n'
        ) % (e(RED_DATOS), red_n[0], red_n[1], e(RED_SALIDA), e(RED_SALIDA), e(RED_DATOS))

    retro = sum(1 for f in indice
                if f["agregado"] and "retrohunt" in f["accion_permitida"].lower()
                and "bloqueo" not in f["accion_permitida"].lower())
    caducados = sum(1 for i in publicables if vigencia(i["fm"], hoy)[0] == "caducado")

    return """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>cti_daily — informes de ciberinteligencia</title>
<meta name="description" content="Informes de ciberinteligencia de producción propia, en Markdown y HTML autocontenido. Marcado TLP:CLEAR.">
<style>%(css)s</style>
</head>
<body>
<div class="tlp-bar">TLP:CLEAR &nbsp;·&nbsp; DIFUSIÓN SIN RESTRICCIÓN, CONSERVANDO LA ATRIBUCIÓN DE LAS FUENTES</div>
<div class="wrap">

<header class="hero">
  <div class="eyebrow">Célula CTI · ciclo diario</div>
  <h1>Informes de ciberinteligencia</h1>
  <p class="lede">Producción propia, escrita en Markdown y publicada como HTML autocontenido.
  Cada informe está escrito para que alguien decida algo: si un párrafo no cambia lo que
  alguien va a hacer, va al anexo o se borra. El repositorio se revisa a diario y los
  agregados de indicadores se reconstruyen desde los informes en cada construcción.</p>
</header>

<h2><span class="num">01 · catálogo</span>Informes publicados</h2>
<p class="sub">%(n)d informes. El botón abre el informe renderizado; la fuente en Markdown
es el documento canónico y se versiona.</p>
<div class="grid">
%(tarjetas)s
</div>

%(bloque_red)s<h2><span class="num">%(num_ioc)s · indicadores</span>Agregados de IOC</h2>
<p class="sub">Reconstruidos en cada construcción desde las tablas del Anexo A de cada
informe. Enlaces directos, utilizables con <code>curl</code> desde cualquier proceso de ingesta.</p>
<table>
<thead><tr><th>Fichero</th><th>Núm.</th><th>Qué contiene</th></tr></thead>
<tbody>
%(filas_ioc)s
</tbody>
</table>

<div class="note">
<strong>Antes de cargar un <code>.txt</code> en un bloqueo.</strong> Las listas planas pierden
la confianza, la caducidad y la acción permitida de cada indicador: %(retro)d de los que
contienen están marcados <em>solo retrohunt</em>, y hay indicadores marcados
<em>no bloquear — herramienta legítima</em>. Cargarlas sin filtrar provocará cortes de
servicio propios. Para eso está <code>ioc_index.csv</code> y su columna
<code>accion_permitida</code>, escrita por quien analizó cada indicador.
</div>

<h2><span class="num">%(num_estado)s · estado</span>Estado del ciclo</h2>
<div class="stats">
  <div class="stat"><div class="n">%(n)d</div><div class="l">informes publicados</div></div>
  <div class="stat"><div class="n">%(n_ioc)d</div><div class="l">indicadores con contexto</div></div>
  <div class="stat"><div class="n">%(caducados)d</div><div class="l">caducados, exigen revisión</div></div>
  <div class="stat"><div class="n">%(reciente)s</div><div class="l">informe más reciente</div></div>
</div>

<footer>
  Todo el material está marcado <code>TLP:CLEAR</code>; la mayoría conserva
  <code>PAP:AMBER</code>, que condiciona el uso activo de los indicadores.
  Fuente, plantilla y utillaje en
  <a href="https://github.com/cabezoide/cti_daily">github.com/cabezoide/cti_daily</a>.
  Esta portada y los agregados los regenera <code>tools/cti_build.py</code>;
  editarlos a mano no sirve de nada.
</footer>

</div>
</body>
</html>
""" % {
        "css": CSS_PORTADA.strip(),
        "n": len(publicables),
        "n_ioc": len(indice),
        "tarjetas": "\n".join(tarjetas),
        "filas_ioc": "\n".join(filas_ioc_tabla),
        "bloque_red": bloque_red,
        "num_ioc": "03" if red_n else "02",
        "num_estado": "04" if red_n else "03",
        "retro": retro,
        "caducados": caducados,
        "reciente": e(reciente or "—"),
    }


def construir_red(lista):
    """Genera el mapa de relaciones desde `red-actores.json` y la plantilla.

    Devuelve (html, avisos). El html es None si falta algún insumo: el mapa es
    opcional y su ausencia no debe romper la construcción del resto.

    Las dos comprobaciones que justifican que esto viva en el constructor:

    - **Referencias rotas.** Cada nodo declara en `r` el informe del que sale.
      Si apunta a un informe que no existe, el enlace de su ficha llevaría a
      ninguna parte y nadie lo notaría hasta pulsarlo.
    - **Informes ausentes del grafo.** Al publicar un informe nuevo, el mapa no
      lo incorpora solo —las relaciones son juicios del analista, no algo
      extraíble de la prosa—, así que lo que hace la construcción es avisar.
      Es deliberado que avise y no falle: un informe sin nodo es una tarea
      pendiente, no un error de integridad.
    """
    avisos = []
    ruta_datos = os.path.join(RAIZ, RED_DATOS)
    ruta_plant = os.path.join(RAIZ, RED_PLANTILLA)
    if not (os.path.exists(ruta_datos) and os.path.exists(ruta_plant)):
        return None, avisos

    with open(ruta_datos, encoding="utf-8") as fh:
        datos = json.load(fh)
    nodos = datos.get("nodos", [])
    aristas = datos.get("aristas", [])

    ids = {n["id"] for n in nodos}
    for a, b, _r in aristas:
        if a not in ids or b not in ids:
            avisos.append("red: arista hacia un nodo inexistente: %s → %s" % (a, b))

    publicables = {i["id"]: i for i in lista if i["publicable"]}
    archivos = {i["id"]: i["html"] for i in publicables.values()}

    citados = set()
    for n in nodos:
        ref = (n.get("r") or "").strip()
        if re.fullmatch(r"CTI-\d{4}-\d{3}", ref):
            citados.add(ref)
            if ref not in archivos:
                avisos.append("red: el nodo %r cita %s, que no existe o no es publicable"
                              % (n.get("l", n["id"]), ref))
    for ident in sorted(set(publicables) - citados):
        avisos.append("red: %s no aparece en ningún nodo de %s" % (ident, RED_DATOS))

    plantilla = open(ruta_plant, encoding="utf-8").read()
    html = (plantilla
            .replace("/*__DATOS__*/",
                     "const DATOS = " + json.dumps(
                         {"nodos": nodos, "aristas": aristas},
                         ensure_ascii=False, separators=(",", ":")) + ";")
            .replace("/*__ARCHIVOS__*/",
                     "const ARCHIVOS = " + json.dumps(
                         archivos, ensure_ascii=False, indent=2) + ";")
            .replace("__N_NODOS__", str(len(nodos)))
            .replace("__N_ARISTAS__", str(len(aristas))))
    return html, avisos


def bloque_indice(lista, ioc, procedencia, indice, hoy, red_n=None):
    publicables = [i for i in lista if i["publicable"]]
    total_ioc = sum(len(v) for v in ioc.values())
    caducados = [i for i in publicables if vigencia(i["fm"], hoy)[0] == "caducado"]
    reciente = max((i["fm"].get("fecha", "") for i in publicables), default="")
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
        "| Informe más reciente | %s |" % (reciente or "—"),
    ]
    if red_n:
        partes += [
            "| Nodos del mapa de relaciones | %d, con %d relaciones — "
            "[`%s`](%s) |" % (red_n[0], red_n[1], RED_SALIDA, RED_SALIDA),
        ]
    partes += [
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

    red_html, red_avisos = construir_red(lista)
    red_n = None
    if red_html is not None:
        with open(os.path.join(RAIZ, RED_DATOS), encoding="utf-8") as fh:
            _d = json.load(fh)
        red_n = (len(_d.get("nodos", [])), len(_d.get("aristas", [])))
        if escribir_si_cambia(os.path.join(RAIZ, RED_SALIDA), red_html, opt.check):
            cambios.append("%s (%d nodos, %d relaciones)" % (RED_SALIDA, red_n[0], red_n[1]))
    for aviso in red_avisos:
        print("aviso: " + aviso, file=sys.stderr)

    portada = pagina_portada(lista, ioc, indice, hoy, red_n)
    if escribir_si_cambia(os.path.join(RAIZ, PORTADA), portada, opt.check):
        cambios.append("%s (portada de GitHub Pages)" % PORTADA)

    ruta_readme = os.path.join(RAIZ, "README.md")
    if os.path.exists(ruta_readme):
        readme = open(ruta_readme, encoding="utf-8").read()
        nuevo = bloque_indice(lista, ioc, procedencia, indice, hoy, red_n)
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
