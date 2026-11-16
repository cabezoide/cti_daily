#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cti_render.py — Renderizador de informes CTI
============================================

Convierte un informe escrito en Markdown (según `plantilla-informe-cti.md`)
en un HTML autocontenido con el sistema de diseño de CTI-2026-014.

    python3 render/cti_render.py informe.md
    python3 render/cti_render.py informe.md -o salida.html
    python3 render/cti_render.py informe.md --theme otro-informe.html

Principios
----------
1. El .md sigue siendo un .md: se lee igual de bien en cualquier visor.
   Todo lo que activa un componente rico es un comentario HTML invisible
   (`<!-- cti:algo -->`) o una convención de escritura que ya usarías.
2. Degradación elegante: si una directiva no encaja con el bloque que la
   sigue, ese bloque se renderiza como tabla o párrafo normal. Nunca falla.
3. El tema (CSS) no se duplica: se extrae del HTML de referencia, que es el
   informe ya aprobado. Cambiar el diseño allí cambia el diseño de todos.

Sin dependencias: solo biblioteca estándar de Python 3.8+.
"""

import argparse
import html as _html
import os
import re
import sys
import unicodedata

VERSION = "1.0"

# --------------------------------------------------------------------------
# Utilidades
# --------------------------------------------------------------------------

def slug(text, taken=None):
    t = unicodedata.normalize("NFKD", text)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = t.lower()
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    t = t or "seccion"
    if taken is not None:
        base, n = t, 2
        while t in taken:
            t = "%s-%d" % (base, n)
            n += 1
        taken.add(t)
    return t


ALLOWED_TAGS = re.compile(
    r"&lt;(/?)(br|b|strong|em|i|u|sup|sub|code|span|small|abbr)"
    r'((?:\s+[a-zA-Z-]+="[^"]*")*)\s*(/?)&gt;'
)


def inline(t):
    """Markdown en línea -> HTML. Permite un puñado de etiquetas crudas."""
    if t is None:
        return ""
    t = _html.escape(t, quote=False)
    t = ALLOWED_TAGS.sub(lambda m: "<%s%s%s%s>" % (m.group(1), m.group(2), m.group(3), m.group(4)), t)
    # código en línea (protege su contenido del resto de reglas)
    holds = []

    def _hold(m):
        holds.append(m.group(1))
        return "\x00%d\x00" % (len(holds) - 1)

    t = re.sub(r"`([^`]+)`", _hold, t)
    t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', t)
    # negrita no codiciosa: admite cursiva anidada («**válidas de *infostealers***»)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t, flags=re.S)
    t = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", t)
    t = re.sub(r"(?<![\w_])_([^_\n]+)_(?![\w_])", r"<em>\1</em>", t)
    t = re.sub(r"~~([^~]+)~~", r"<s>\1</s>", t)
    for i, c in enumerate(holds):
        t = t.replace("\x00%d\x00" % i, "<code>%s</code>" % c)
    return t


def plain(t):
    """Texto sin marcas, para atributos y búsquedas."""
    t = re.sub(r"`|\*\*|\*|~~", "", t or "")
    # el guion bajo solo es cursiva entre límites de palabra: borrarlo a ciegas
    # destruye nombres como G_hlm7jj_windows_amd64.exe
    t = re.sub(r"(?<![\w\\])_([^_]+)_(?![\w])", r"\1", t)
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)
    t = re.sub(r"<[^>]+>", "", t)
    return t.strip()


def attr(t):
    return _html.escape(plain(t), quote=True)


def split_sentences(text):
    """Parte en oraciones SIN cortar dentro de un tramo en negrita.

    Cortar por `(?<=[.:])\\s+` a secas deja `**` sin cerrar cuando el juicio
    escribe la afirmación entera en negrita, y el HTML sale con asteriscos
    sueltos y etiquetas cruzadas.
    """
    out, buf, bold, i = [], "", False, 0
    while i < len(text):
        if text[i:i + 2] == "**":
            bold = not bold
            buf += "**"
            i += 2
            continue
        ch = text[i]
        buf += ch
        # los dos puntos solo cierran oración si lo que sigue arranca en mayúscula;
        # si no, son una aposición («…es el borde de red: appliances sin parchear»)
        if ch == ":" and not bold:
            nxt = text[i + 1:].lstrip()
            if nxt and not nxt[0].isupper():
                i += 1
                continue
        if ch in ".:" and not bold and (i + 1 >= len(text) or text[i + 1].isspace()):
            if buf.strip():
                out.append(buf.strip())
            buf = ""
        i += 1
    if buf.strip():
        out.append(buf.strip())
    return out


def num(t):
    """Primer número de una celda, o None."""
    m = re.search(r"-?\d[\d.  ]*(?:,\d+)?", (t or "").replace(" ", " "))
    if not m:
        return None
    s = m.group(0).replace(" ", "").replace(" ", "")
    # 1.570 -> 1570 ; 4,5 -> 4.5
    if "," in s:
        s = s.replace(".", "").replace(",", ".")
    else:
        if re.match(r"^-?\d{1,3}(\.\d{3})+$", s):
            s = s.replace(".", "")
    try:
        return float(s)
    except ValueError:
        return None


# --------------------------------------------------------------------------
# Frontmatter (subconjunto de YAML)
# --------------------------------------------------------------------------

def read_frontmatter(text):
    meta = {}
    if not text.startswith("---"):
        return meta, text
    end = re.search(r"^---\s*$", text[3:], re.M)
    if not end:
        return meta, text
    raw = text[3:3 + end.start()]
    rest = text[3 + end.end():]
    for line in raw.splitlines():
        line = line.rstrip()
        if not line.strip() or line.strip().startswith("#"):
            continue
        m = re.match(r"^([A-Za-z0-9_\-]+)\s*:\s*(.*)$", line)
        if not m:
            continue
        k, v = m.group(1).strip(), m.group(2).strip()
        if v.startswith("[") and v.endswith("]"):
            items = [x.strip().strip("\"'").strip() for x in v[1:-1].split(",")]
            v = [x for x in items if x]
        elif len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
            v = v[1:-1]
        meta[k] = v
    return meta, rest.lstrip("\n")


# --------------------------------------------------------------------------
# Tokenizador de bloques
# --------------------------------------------------------------------------

DIRECTIVE = re.compile(r"^<!--\s*cti:([a-zA-Z][\w-]*)\s*(.*?)\s*-->\s*$")
ARGS = re.compile(r'([a-zA-Z][\w-]*)\s*=\s*"([^"]*)"')


def tokenize(text):
    lines = text.replace("\r\n", "\n").split("\n")
    blocks, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i]
        s = line.strip()

        if not s:
            i += 1
            continue

        m = DIRECTIVE.match(s)
        if m:
            blocks.append(("dir", m.group(1).lower(), dict(ARGS.findall(m.group(2) or ""))))
            i += 1
            continue

        if s.startswith("<!--"):                       # comentario normal: se ignora
            while i < n and "-->" not in lines[i]:
                i += 1
            i += 1
            continue

        if re.match(r"^(-{3,}|\*{3,}|_{3,})$", s):
            blocks.append(("hr",))
            i += 1
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", s)
        if m:
            blocks.append(("h", len(m.group(1)), m.group(2).strip()))
            i += 1
            continue

        if s.startswith("```") or s.startswith("~~~"):
            fence = s[:3]
            lang = s[3:].strip()
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith(fence):
                buf.append(lines[i])
                i += 1
            i += 1
            blocks.append(("code", lang, buf))
            continue

        if s.startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            blocks.append(("quote", buf))
            continue

        if s.startswith("|") and i + 1 < n and re.match(r"^\s*\|?[\s:|-]+\|[\s:|-]*$", lines[i + 1]):
            head = split_row(lines[i])
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            blocks.append(("table", head, rows))
            continue

        m = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$", line)
        if m:
            ordered = not m.group(2) in ("-", "*", "+")
            items = []                       # cada item: [texto, [subbloques]]
            while i < n:
                mm = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$", lines[i])
                if mm:
                    items.append([mm.group(3).strip(), []])
                    i += 1
                    continue
                s2 = lines[i].strip()
                # bloque de código indentado DENTRO de un punto de la lista:
                # se conserva como bloque, no se aplasta en el texto del <li>
                if items and s2.startswith(("```", "~~~")):
                    fence, lang = s2[:3], s2[3:].strip()
                    i += 1
                    buf = []
                    while i < n and not lines[i].strip().startswith(fence):
                        buf.append(lines[i])
                        i += 1
                    i += 1
                    items[-1][1].append(("code", lang, dedent(buf)))
                    continue
                if s2 and lines[i].startswith(("  ", "\t")) and items:
                    items[-1][0] += " " + s2
                    i += 1
                    continue
                break
            blocks.append(("list", ordered, items))
            continue

        buf = []
        while i < n and lines[i].strip() and not is_break(lines[i]):
            buf.append(lines[i].strip())
            i += 1
        if buf:
            blocks.append(("p", " ".join(buf)))
        else:
            i += 1
    return blocks


MES = r"(ene|feb|mar|abr|may|jun|jul|ago|sep|oct|nov|dic)"


def short_label(label):
    """Etiqueta de eje X legible: las largas se solapan entre sí.

    «Últimos meses de 2025» → «2025» · «Septiembre 2026» → «Sep·26»
    """
    if len(label) <= 13:
        return label
    year = re.search(r"\d{2}(\d{2})\b", label)
    mes = re.search(MES, label, re.I)
    if mes:
        return mes.group(1).capitalize() + ("·" + year.group(1) if year else "")
    if year:
        return year.group(0)
    return label[:12] + "…"


def dedent(lines):
    """Quita la sangría común de un bloque de código anidado en una lista."""
    widths = [len(l) - len(l.lstrip()) for l in lines if l.strip()]
    cut = min(widths) if widths else 0
    return [l[cut:] if len(l) >= cut else l.lstrip() for l in lines]


def is_break(line):
    s = line.strip()
    return (
        s.startswith("#") or s.startswith(">") or s.startswith("|")
        or s.startswith("```") or s.startswith("~~~") or s.startswith("<!--")
        or re.match(r"^(-{3,}|\*{3,}|_{3,})$", s)
        or re.match(r"^(\s*)([-*+]|\d+[.)])\s+", line)
    )


def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in re.split(r"(?<!\\)\|", line)]


# --------------------------------------------------------------------------
# Vocabulario analítico
# --------------------------------------------------------------------------

PROB = [
    ("casi con certeza no", 3), ("casi con certeza", 97), ("muy probable", 88),
    ("poco probable", 32), ("muy poco probable", 12), ("posibilidad real", 50),
    ("probable", 68), ("remoto", 5), ("confirmado", 100),
]

CONF_CLASS = {"alta": "kj-hi", "moderada": "kj-md", "media": "kj-md", "baja": "kj-lo"}

PILL_COLS = {
    "confianza", "prioridad", "plazo", "severidad", "fiabilidad", "credibilidad",
    "nivel", "estado", "uso", "acción", "accion", "acción permitida", "grado de equivalencia",
    "esfuerzo", "audiencia", "disciplina", "responsable", "valor",
}

PILL_MAP = [
    (r"^(crítica|critica|crítico|critico|alta|alto|máximo|maximo)$", "p-amber"),
    (r"^(moderada|moderado|media|medio)$", "p-sky"),
    (r"^(baja|bajo|mínimo|minimo|trivial)$", "p-grey"),
    (r"^(sí|si|equivalente|referencia|confirmado|bloqueo)$", "p-mint"),
    (r"^(no|descartada|ambiguo|caducado)$", "p-grey"),
    (r"^\d+\s*(h|d|días|dias|horas|meses)$", "p-amber"),
    (r"^a-?\d$|^a$", "p-mint"),
    (r"^b-?\d$|^b$", "p-sky"),
    (r"^c-?\d$|^c$", "p-amber"),
    (r"^d-?\d$|^[def]$", "p-grey"),
]

LEVELS = [
    (re.compile(r"estrat", re.I), "e", "var(--deep)", "Estratégico"),
    (re.compile(r"operac", re.I), "o", "var(--sky)", "Operacional"),
    (re.compile(r"t[áa]ctic", re.I), "t", "var(--mint)", "Táctico"),
    (re.compile(r"t[ée]cnic", re.I), "x", "var(--amber)", "Técnico"),
    (re.compile(r"anexo", re.I), "an", "var(--ink-3)", "Anexos"),
]

PREFIX_COLOR = {"E": "var(--deep)", "O": "var(--sky)", "T": "var(--mint)", "X": "var(--amber)"}


def prob_from(text):
    """-> (valor 0-100, término textual, rango legible). Cualquiera puede ser None."""
    low = plain(text).lower()
    term = None
    for t, _v in sorted(PROB, key=lambda x: -len(x[0])):
        if t in low:
            term = t
            break
    m = re.search(r"\(?\s*(\d{1,3})\s*[–\-]\s*(\d{1,3})\s*%", low)
    if m:
        a, b = float(m.group(1)), float(m.group(2))
        return (a + b) / 2.0, term, "%d–%d %%" % (a, b)
    if term:
        val = dict(PROB)[term]
        return float(val), term, ("%d %%" % val if val < 100 else "hecho")
    return None, None, None


# en una columna de confianza/fiabilidad, «Alta» es una virtud (verde);
# en una de prioridad/severidad/plazo, es una alarma (ámbar)
POSITIVE_COLS = {"confianza", "fiabilidad", "credibilidad", "cobertura"}


def pill_for(value, column=""):
    v = plain(value).lower().strip().rstrip(".")
    col = plain(column).lower().strip()
    if col in POSITIVE_COLS:
        if re.match(r"^(alta|alto)$", v):
            return "p-mint"
        if re.match(r"^(moderada|moderado|media|medio)$", v):
            return "p-sky"
        if re.match(r"^(baja|bajo)$", v):
            return "p-grey"
    for rx, cls in PILL_MAP:
        if re.match(rx, v):
            return cls
    return None


# --------------------------------------------------------------------------
# Renderizador
# --------------------------------------------------------------------------

class Renderer:
    def __init__(self, meta, opts):
        self.meta = meta
        self.opts = opts
        self.out = []
        self.toc = []
        self.group = None
        self.level = None          # letra del nivel actual
        self.level_color = "var(--sky)"
        self.ids = set()
        self.open_section = False
        self.pending = None        # (nombre, args) de la última directiva
        self.counters = {"tl": 0, "matrix": 0, "ioc": 0, "pyr": 0}

    # ---------- helpers ----------
    def w(self, s):
        self.out.append(s)

    def take(self):
        d, self.pending = self.pending, None
        return d or (None, {})

    def group_push(self, title, cls):
        self.group = {"title": title, "cls": cls, "items": []}
        self.toc.append(self.group)

    def toc_add(self, sid, label):
        if self.group is None:
            self.group_push("Apertura", "g-top")
        self.group["items"].append((sid, label))

    def close_section(self):
        if self.open_section:
            self.w("</section>")
            self.open_section = False

    # ---------- bucle principal ----------
    def run(self, blocks):
        self.hero(blocks)
        i = self.hero_end
        while i < len(blocks):
            b = blocks[i]
            kind = b[0]

            if kind == "dir":
                self.pending = (b[1], b[2])
                i += 1
                continue

            if kind == "h":
                i = self.heading(blocks, i)
                continue

            if kind == "hr":
                i += 1
                continue

            name, args = self.take()
            if kind == "table":
                i = self.table_block(blocks, i, name, args)
                continue
            if kind == "quote":
                self.quote(b[1], args)
                i += 1
                continue
            if kind == "code":
                self.code(b[1], b[2], args)
                i += 1
                continue
            if kind == "list":
                self.w(self.list_html(b[1], b[2]))
                i += 1
                continue
            if kind == "p":
                if name == "kj" or (not name and re.match(r"^\*\*KJ-", b[1])):
                    i = self.kj_group(blocks, i)
                    continue
                if name == "accordion":
                    i = self.accordion(blocks, i, args)
                    continue
                if name == "detections":
                    i = self.detections(blocks, i)
                    continue
                self.w('<p class="rv">%s</p>' % inline(b[1]))
                i += 1
                continue
            i += 1

        self.close_section()
        return "".join(self.out)

    # ---------- portada ----------
    def hero(self, blocks):
        title = sub = sub2 = None
        i = 0
        if blocks and blocks[0][0] == "h" and blocks[0][1] == 1:
            title = blocks[0][2]
            i = 1
            while i < len(blocks) and blocks[i][0] == "h" and blocks[i][1] in (2, 3):
                if blocks[i][1] == 2 and sub is None:
                    sub = blocks[i][2]
                elif sub2 is None:
                    sub2 = blocks[i][2]
                else:
                    break
                i += 1
        self.hero_end = i
        m = self.meta
        # el titular es el actor si el frontmatter lo declara: el h1 de un informe
        # CTI suele ser el rótulo del producto («INFORME DE CIBERINTELIGENCIA — …»),
        # que no dice nada en una portada
        title = m.get("actor") or title or "Informe de ciberinteligencia"

        # el título del hero se parte por el primer separador fuerte
        parts = re.split(r"\s+[–—]\s+|\s*\(|\s*:\s*", title, maxsplit=1)
        head = parts[0].strip()
        tail = (parts[1].rstrip(")").strip() if len(parts) > 1 else "")

        pills = []
        if m.get("tipo"):
            pills.append('<span class="pill p-amber">%s</span>' % inline(m["tipo"]))
        if m.get("foco_regional"):
            pills.append('<span class="pill p-mint">%s</span>' % inline(m["foco_regional"]))
        ver = " · ".join(x for x in [m.get("version") and "v" + str(m["version"]), m.get("fecha")] if x)
        if ver:
            pills.append('<span class="pill p-sky">%s</span>' % inline(ver))

        self.group_push("Apertura", "g-top")
        self.toc_add("portada", "Portada y control")
        self.w('<section id="portada" class="hero"><div class="wrap"><div class="hero-grid"><div>')
        self.w('<div class="eyebrow">%s</div>' % "".join(pills))
        self.w("<h1>%s%s</h1>" % (
            inline(head),
            ('<br><span class="hl">%s</span>' % inline(tail)) if tail else ""))
        if sub:
            self.w('<p class="sub">%s</p>' % inline(sub))
        if sub2:
            self.w('<p class="sub2">%s</p>' % inline(sub2))
        self.w("</div>")
        self.w(HERO_3D)
        self.w("</div>")
        self.w(self.meta_grid())
        self.w("</div></section>")

    def meta_grid(self):
        m, cells = self.meta, []
        order = [
            ("id", "Identificador", True), ("ventana", "Ventana de observación", True),
            ("colección", "Base de colección", False), ("coleccion", "Base de colección", False),
            ("telemetria", "Telemetría propia", False),
            ("caduca", "Caducidad / revisión", True), ("niveles", "Niveles cubiertos", False),
            ("autor", "Autor (analista)", False), ("revision", "Revisión por pares", False),
            ("aprobacion", "Aprobación", False), ("solicitante", "Consumidor primario", False),
            ("pir", "Requisitos atendidos", True), ("relacionados", "Productos relacionados", False),
            ("paquete", "Paquete legible por máquina", False),
        ]
        seen = set()
        for key, label, mono in order:
            if key in seen or key not in m or not m[key]:
                continue
            seen.add(key)
            v = m[key]
            if isinstance(v, list):
                v = " · ".join(v)
            cells.append('<div><dt>%s</dt><dd%s>%s</dd></div>' % (
                _html.escape(label), ' class="m"' if mono else "", inline(str(v))))
        tlp = m.get("tlp", "")
        pap = m.get("pap", "")
        if tlp or pap:
            cells.append('<div><dt>Marcado de difusión</dt><dd class="m" style="color:var(--amber)">%s</dd></div>'
                         % inline(" · ".join(x for x in [tlp, pap] if x)))
        if not cells:
            return ""
        return '<dl class="meta-grid rv">%s</dl>' % "".join(cells)

    # ---------- encabezados ----------
    def heading(self, blocks, i):
        _, lvl, text = blocks[i]
        name, args = self.take()

        if lvl == 1:
            self.close_section()
            key, color, label = None, "var(--ink-3)", text
            for rx, k, c, lab in LEVELS:
                if rx.search(text):
                    key, color, label = k, c, lab
                    break
            self.level, self.level_color = key, color
            if key in ("e", "o", "t", "x"):
                self.counters["lvl"] = self.counters.get("lvl", 0) + 1
                kicker = args.get("kicker") or ("Nivel %02d" % self.counters["lvl"])
            else:
                kicker = args.get("kicker", "")
            meta_line = ""
            j = i + 1
            if j < len(blocks) and blocks[j][0] == "h" and blocks[j][1] == 3:
                meta_line = self.level_meta(blocks[j][2])
                j += 1
            cls = "lv-%s" % key if key in ("e", "o", "t", "x") else ""
            style = "" if cls else ' style="--lv:%s;--lv-soft:rgba(130,148,184,.12)"' % color
            self.w('<div class="level %s rv" id="nivel-%s"%s>' % (cls, key or slug(text, self.ids), style))
            if kicker:
                self.w('<div class="kicker">%s</div>' % inline(kicker))
            self.w("<h2>%s</h2>" % inline(label if key else text))
            if meta_line:
                self.w(meta_line)
            self.w("</div>")
            self.group_push(label if key else text, "g-%s" % (key or "top"))
            return j

        if lvl == 2:
            self.close_section()
            sid = args.get("id") or slug(text, self.ids)
            # admite «E-4.», «E-2.1», «O-6.1», «14.», «A», «D–G»
            num_m = re.match(r"^\s*([A-Z]{1,3}(?:-[\w.]+)?|\d+(?:\.\d+)*)[.·]?\s+(.+)$", text)
            badge, title = (num_m.group(1), num_m.group(2)) if num_m else ("", text)
            badge = badge.rstrip(".")
            color = PREFIX_COLOR.get(badge[:1].upper(), self.level_color) if badge else self.level_color
            lead = ""
            j = i + 1
            if j < len(blocks) and blocks[j][0] == "p" and args.get("lead") != "no" \
               and len(plain(blocks[j][1])) < 260 and self.opts.leads:
                lead = blocks[j][1]
                j += 1
            self.w('<section id="%s" class="wrap">' % sid)
            self.open_section = True
            self.w('<div class="sec-head rv">')
            if badge:
                self.w('<span class="sec-num" style="color:%s">%s</span>' % (color, inline(badge)))
            self.w("<div><h2>%s</h2>%s</div></div>" % (
                inline(title), ("<p>%s</p>" % inline(lead)) if lead else ""))
            self.toc_add(sid, plain(text))
            return j

        tag = "h3" if lvl == 3 else "h4"
        self.w('<%s class="rv">%s</%s>' % (tag, inline(text), tag))
        return i + 1

    def level_meta(self, text):
        bits = [b.strip() for b in re.split(r"\s+·\s+|\s+\|\s+", text) if b.strip()]
        out = []
        for b in bits:
            mm = re.match(r"^(?:\*\*)?([^:*]+?)(?:\*\*)?\s*:\s*(.*)$", b)
            if mm:
                out.append("<span><b>%s:</b> %s</span>" % (inline(mm.group(1)), inline(mm.group(2))))
            else:
                out.append("<span>%s</span>" % inline(b))
        return '<div class="meta">%s</div>' % "".join(out)

    # ---------- bloques ----------
    def quote(self, lines, args=None):
        args = args or {}
        text = "\n".join(lines).strip()
        kind = args.get("type")
        if not kind:
            head = plain(text)[:6]
            if "⚠" in head or "⛔" in head:
                kind = "warn"
            elif "✅" in head or "✔" in head:
                kind = "good"
            elif "⬛" in head or "◼" in head:
                kind = "gap"
            else:
                kind = "info"
        sub = tokenize(text)
        title = args.get("title", "")
        body = []
        for k, blk in enumerate(sub):
            if blk[0] == "p":
                # admite un emoji delante del título: «⚠ **Verificar con Legal** …»
                m = re.match(r"^([^\w\s*]{0,3}\s*)\*\*(.+?)\.?\*\*\s*(.*)$", blk[1])
                if k == 0 and not title and m and len(plain(m.group(2))) < 90:
                    title = (m.group(1) or "").strip() + (" " if m.group(1).strip() else "") + m.group(2)
                    if m.group(3).strip():
                        body.append("<p>%s</p>" % inline(m.group(3)))
                    continue
                body.append("<p>%s</p>" % inline(blk[1]))
            elif blk[0] == "list":
                body.append(self.list_html(blk[1], blk[2], plainer=True))
            elif blk[0] == "table":
                body.append(self.table_html(blk[1], blk[2], {}))
            elif blk[0] == "code":
                body.append(self.code_html(blk[1], blk[2], {}))
        if not title and not body:
            return
        self.w('<div class="note %s rv">%s%s</div>' % (
            kind,
            ('<div class="t">%s</div>' % inline(title)) if title else "",
            "".join(body) or ""))

    def list_html(self, ordered, items, plainer=False):
        tag = "ol" if ordered else "ul"
        out = []
        for it in items:
            text, subs = (it[0], it[1]) if isinstance(it, (list, tuple)) else (it, [])
            extra = "".join(self.code_html(b[1], b[2], {}) for b in subs if b[0] == "code")
            out.append("<li>%s%s</li>" % (inline(text), extra))
        cls = "" if plainer else ' class="rv"'
        return "<%s%s>%s</%s>" % (tag, cls, "".join(out), tag)

    def code(self, lang, lines, args):
        self.w(self.code_html(lang, lines, args))

    def code_html(self, lang, lines, args):
        body = _html.escape("\n".join(lines))
        body = self.highlight(body, lang)
        label = args.get("title") or (lang.upper() if lang else "código")
        return ('<div class="codewrap rv"><div class="codehead"><span>%s</span>'
                '<button class="copy">copiar</button></div><pre><code>%s</code></pre></div>'
                % (_html.escape(label), body))

    def highlight(self, body, lang):
        """Resalta el bloque de código en UNA sola pasada.

        Antes se aplicaba una `re.sub` por cada clase de token, en cascada: la
        regla de cadenas acababa casando el `class="tok-k"` que la regla de
        palabras clave acababa de insertar, y producía marcado roto del tipo
        `<span class=<span class="tok-s">"tok-k"</span>>where</span>`, que el
        navegador muestra como texto literal. Con una sola pasada ninguna regla
        puede volver a resaltar el marcado que otra emitió.
        """
        l = (lang or "").lower()
        if l in ("kql", "sql", "spl"):
            pat = re.compile(
                r'(?P<s>&quot;[^&]*?&quot;|"[^"]*")'
                r'|\b(?P<k>where|project|summarize|extend|join|let|order by|by'
                r'|has_any|has|in~|in|and|or|not)\b', re.I)
        elif l in ("powershell", "ps1", "bash", "sh", "cmd", "bat"):
            pat = re.compile(
                r'(?P<c>^[ \t]*(?:#|::|REM).*$)'
                r"|(?P<s>'[^']*')"
                r'|(?P<ws>^[ \t]*)(?P<k>[A-Za-z][\w\-]*)', re.M)
        elif l in ("yaml", "yml", "sigma"):
            pat = re.compile(
                r'(?P<c>^[ \t]*#.*$)'
                r'|(?P<ws2>^[ \t]*)(?P<n>[\w\-.]+)(?=:)', re.M)
        else:
            return body

        def repl(m):
            d = m.groupdict()
            for g in ("c", "s", "k", "n"):
                if d.get(g):
                    sangria = d.get("ws") or d.get("ws2") or ""
                    return '%s<span class="tok-%s">%s</span>' % (sangria, g, d[g])
            return m.group(0)

        return pat.sub(repl, body)

    # ---------- tablas y componentes de tabla ----------
    def table_block(self, blocks, i, name, args):
        head, rows = blocks[i][1], blocks[i][2]
        builders = {
            "stats": self.stats, "bars": self.bars, "chart": self.chart,
            "timeline": self.timeline, "matrix": self.matrix, "ioc": self.ioc,
            "cards": self.cards, "pyramid": self.pyramid, "stages": self.stages,
            "meta": self.meta_table,
        }
        # dwell="next": la franja inferior de la cadena sale del párrafo que
        # sigue a la tabla, para que el dato siga visible al leer el .md en plano
        eaten = 0
        if name == "stages" and args.get("dwell") == "next":
            j = i + 1
            if j < len(blocks) and blocks[j][0] == "p":
                args = dict(args)
                args["dwell"] = blocks[j][1]
                eaten = 1

        fn = builders.get(name or "")
        if fn:
            try:
                out = fn(head, rows, args)
                if out:
                    self.w(out)
                    return i + 1 + eaten
            except Exception as e:                      # degradación elegante
                sys.stderr.write("  aviso: cti:%s no pudo construirse (%s); se usa tabla\n" % (name, e))
        self.w(self.table_html(head, rows, args))
        return i + 1

    def table_html(self, head, rows, args):
        hl = args.get("highlight")
        rx = re.compile(hl, re.I) if hl else None
        pill_idx = {k for k, h in enumerate(head) if plain(h).lower() in PILL_COLS}
        th = "".join("<th>%s</th>" % inline(h) for h in head)
        body = []
        for r in rows:
            cells = []
            for k, c in enumerate(r):
                v = c
                if k in pill_idx:
                    cls = pill_for(c, head[k] if k < len(head) else "")
                    if cls:
                        v = '<span class="pill %s">%s</span>' % (cls, inline(plain(c)))
                    else:
                        v = inline(c)
                else:
                    v = inline(c)
                cells.append("<td>%s</td>" % v)
            style = ""
            if rx and rx.search(" ".join(plain(x) for x in r)):
                style = ' style="background:rgba(247,164,0,.05)"'
            body.append("<tr%s>%s</tr>" % (style, "".join(cells)))
        return ('<div class="tw rv"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
                % (th, "".join(body)))

    def meta_table(self, head, rows, args):
        cells = []
        for r in rows:
            if len(r) < 2 or not plain(r[1]):
                continue
            mono = bool(re.match(r"^`", r[1])) or bool(re.match(r"^[\w.\-/ :→]+$", plain(r[1])))
            cells.append('<div><dt>%s</dt><dd%s>%s</dd></div>' % (
                inline(plain(r[0])), ' class="m"' if mono else "", inline(r[1])))
        if not cells:
            return None
        return '<dl class="meta-grid rv" style="margin-top:0">%s</dl>' % "".join(cells)

    def stats(self, head, rows, args):
        colors = ["var(--amber)", "var(--sky)", "var(--mint)", "var(--deep)"]
        out = []
        for k, r in enumerate(rows):
            if len(r) < 2:
                continue
            raw = plain(r[0])
            v = num(raw)
            suffix = re.sub(r"[\d.,  ]", "", raw)
            col = args.get("color") or colors[k % len(colors)]
            if v is not None and v == int(v):
                figure = '<div class="n" data-count="%d">0%s</div>' % (
                    int(v), ('<small>%s</small>' % _html.escape(suffix)) if suffix else "")
            else:
                figure = '<div class="n">%s</div>' % inline(raw)
            note = ('<div class="s">%s</div>' % inline(r[2])) if len(r) > 2 and plain(r[2]) else ""
            out.append('<div class="stat" style="--c:%s">%s<div class="l">%s</div>%s</div>'
                       % (col, figure, inline(r[1]), note))
        if not out:
            return None
        cls = "g4" if len(out) >= 4 else "g3"
        return '<div class="grid %s rv">%s</div>' % (cls, "".join(out))

    def bars(self, head, rows, args):
        vals = [(r[0], num(r[1]) or 0, r[1]) for r in rows if len(r) > 1]
        if not vals:
            return None
        mx = max(v for _, v, _ in vals) or 1
        colors = args.get("color", "").split(",") if args.get("color") else []
        out = []
        for k, (label, v, raw) in enumerate(vals):
            col = colors[k % len(colors)].strip() if colors else (
                "var(--amber)" if v == mx else "var(--sky)")
            out.append('<div class="bar" style="--bc:%s"><span class="bn">%s</span>'
                       '<span class="bt"><i data-w="%d"></i></span><span class="bv">%s</span></div>'
                       % (col, inline(label), round(v / mx * 100), inline(plain(raw))))
        title = args.get("title")
        inner = '<div class="bars" data-bars>%s</div>' % "".join(out)
        if title:
            return '<div class="card rv"><h4 style="margin-top:0">%s</h4>%s</div>' % (inline(title), inner)
        return '<div class="card rv">%s</div>' % inner

    def chart(self, head, rows, args):
        pts = [(plain(r[0]), num(r[1]), plain(r[1])) for r in rows if len(r) > 1]
        pts = [p for p in pts if p[1] is not None]
        if len(pts) < 2:
            return None
        W, H = 720.0, 250.0
        x0, x1, y0, y1 = 50.0, 690.0, 24.0, 200.0
        mx = max(p[1] for p in pts) or 1.0
        step = (x1 - x0) / (len(pts) - 1)
        xy = [(x0 + k * step, y1 - (p[1] / mx) * (y1 - y0)) for k, p in enumerate(pts)]
        line = " L".join("%.1f,%.1f" % p for p in xy)
        area = "M%s L%.1f,%.1f L%.1f,%.1f Z" % (line, xy[-1][0], y1, x0, y1)
        grid = "".join('<line x1="%.0f" y1="%.1f" x2="%.0f" y2="%.1f"/>'
                       % (x0, y1 - k * (y1 - y0) / 4.0, x1 + 10, y1 - k * (y1 - y0) / 4.0) for k in range(5))
        ylab = "".join('<text x="42" y="%.1f">%s</text>'
                       % (y1 - k * (y1 - y0) / 4.0 + 4, int(round(mx * k / 4.0))) for k in range(5))
        dots, vals, xlab = [], [], []
        for k, ((label, v, raw), (px, py)) in enumerate(zip(pts, xy)):
            last = k == len(pts) - 1
            col = "#f7a400" if last else ("#4db99c" if k > len(pts) / 2 else "#5a7ebe")
            dots.append('<circle class="pt" cx="%.1f" cy="%.1f" r="%s" fill="%s"><title>%s: %s</title></circle>'
                        % (px, py, "6.5" if last else "5", col, _html.escape(label), _html.escape(raw)))
            vals.append('<text x="%.1f" y="%.1f"%s>%s</text>'
                        % (px, py - 11, ' fill="#f7a400"' if last else "", _html.escape(raw)))
            xlab.append('<text x="%.1f" y="222">%s</text>' % (px, _html.escape(short_label(label))))
        title = args.get("title", "")
        cap = args.get("cap", "")
        return ('<div class="chart rv">%s%s'
                '<svg viewBox="0 0 %d %d" role="img" aria-label="%s">'
                '<defs><linearGradient id="gArea" x1="0" y1="0" x2="0" y2="1">'
                '<stop offset="0%%" stop-color="#f7a400" stop-opacity=".34"/>'
                '<stop offset="100%%" stop-color="#f7a400" stop-opacity="0"/></linearGradient>'
                '<linearGradient id="gLine" x1="0" y1="1" x2="1" y2="0"><stop offset="0%%" stop-color="#375d9d"/>'
                '<stop offset="45%%" stop-color="#4db99c"/><stop offset="100%%" stop-color="#f7a400"/></linearGradient></defs>'
                '<g stroke="rgba(90,126,190,.16)" stroke-width="1">%s</g>'
                '<g class="gtxt" text-anchor="end">%s</g>'
                '<path d="%s" fill="url(#gArea)"/><path class="ln" stroke="url(#gLine)" d="M%s"/>'
                '<g>%s</g><g class="gval" text-anchor="middle">%s</g>'
                '<g class="gtxt" text-anchor="middle">%s</g></svg></div>'
                % (('<h4>%s</h4>' % inline(title)) if title else "",
                   ('<p class="cap">%s</p>' % inline(cap)) if cap else "",
                   int(W), int(H), attr(title or "Serie temporal"),
                   grid, ylab, area, line, "".join(dots), "".join(vals), "".join(xlab)))

    def timeline(self, head, rows, args):
        self.counters["tl"] += 1
        tid = "timeline" if self.counters["tl"] == 1 else "timeline%d" % self.counters["tl"]
        tracks, evs = {}, []
        for r in rows:
            if len(r) < 2:
                continue
            date_, text = r[0], r[1]
            track = plain(r[2]).lower() if len(r) > 2 and plain(r[2]) else ""
            keys = []
            cls = []
            if track:
                key = re.sub(r"[^a-z0-9]+", "", track)[:12] or "x"
                keys.append(key)
                tracks[key] = plain(r[2])
                if re.search(r"chile|latam|regional", track):
                    cls.append("cl")
                else:
                    cls.append("gl")
            big = "**" in date_ or "**" in text
            if big:
                keys.append("big")
                cls.append("big")
            evs.append('<div class="ev %s" data-k="%s"><div class="d">%s</div><div class="x">%s</div></div>'
                       % (" ".join(cls), " ".join(keys), inline(plain(date_)), inline(text)))
        has_big = any('big' in e.split('data-k="')[1].split('"')[0] for e in evs if 'data-k="' in e)
        chips = ""
        if tracks or has_big:
            btns = ['<button class="chip on" data-tl="all">Todo</button>']
            for k, label in tracks.items():
                btns.append('<button class="chip" data-tl="%s">%s</button>' % (k, _html.escape(label)))
            if has_big:
                btns.append('<button class="chip" data-tl="big">Hitos</button>')
            chips = '<div class="tlfilter rv" data-for="%s">%s</div>' % (tid, "".join(btns))
        return '%s<div class="tl rv" id="%s">%s</div>' % (chips, tid, "".join(evs))

    def matrix(self, head, rows, args):
        cols = {}
        order = []
        idx = {plain(h).lower(): k for k, h in enumerate(head)}
        c_tac = idx.get("táctica", idx.get("tactica", 0))
        c_id = idx.get("id", 1)
        c_tec = idx.get("técnica", idx.get("tecnica", 2))
        c_pro = idx.get("procedimiento observado", idx.get("procedimiento", 3))
        for r in rows:
            if len(r) <= max(c_tac, c_id, c_tec):
                continue
            tac = plain(r[c_tac])
            if tac not in cols:
                cols[tac] = []
                order.append(tac)
            cols[tac].append((plain(r[c_id]), plain(r[c_tec]), r[c_pro] if c_pro < len(r) else ""))
        if not order:
            return None
        out = []
        for tac in order:
            items = cols[tac]
            body = []
            for tid, tname, proc in items:
                blob = attr(" ".join([tac, tid, tname, plain(proc)]).lower())
                body.append('<div class="tq" data-s="%s"><div class="tid">%s</div>'
                            '<div class="tn">%s</div><div class="tp">%s</div></div>'
                            % (blob, _html.escape(tid), _html.escape(tname), inline(proc)))
            out.append('<div class="mcol" data-col><h5>%s <i>%d</i></h5>%s</div>'
                       % (_html.escape(tac), len(items), "".join(body)))
        return (SEARCH_BAR % ("attckSearch", args.get("placeholder", "Buscar: técnica, ID, herramienta…"), "attckCount")
                + '<div class="matrix" id="matrix">%s</div>' % "".join(out))

    def ioc(self, head, rows, args):
        out = []
        for r in rows:
            if len(r) < 2:
                continue
            ty, val = plain(r[0]), plain(r[1])
            if len(r) > 3:                      # …| contexto | … | acción
                ctx = " · ".join(plain(c) for c in r[2:-1] if plain(c))
                action = plain(r[-1])
            elif len(r) == 3:                   # …| contexto
                ctx, action = plain(r[2]), ""
            else:
                ctx, action = "", ""
            if re.search(r"no bloquear|no usar|caducad", action, re.I):
                cls = "p-amber"                      # advertencia, no acción rutinaria
            elif re.search(r"retrohunt|monitor|solo ", action, re.I):
                cls = "p-grey"
            else:
                cls = pill_for(action) or "p-mint"
            pill = ('<span class="pill %s">%s</span>' % (cls, _html.escape(action))) if action else "<span></span>"
            out.append('<div class="ioc-row" data-s="%s"><span class="ty">%s</span>'
                       '<span class="vv">%s%s</span>%s</div>'
                       % (attr(" ".join([ty, val, ctx, action]).lower()), _html.escape(ty),
                          _html.escape(val), ('<em>%s</em>' % inline(ctx)) if ctx else "", pill))
        if not out:
            return None
        bar = ""
        if args.get("search", "yes") != "no":
            bar = SEARCH_BAR % ("iocSearch", args.get("placeholder", "Filtrar indicadores…"), "iocCount")
        return bar + '<div class="card rv" style="padding:0">%s</div>' % "".join(out)

    def cards(self, head, rows, args):
        colors = ["var(--amber)", "var(--sky)", "var(--mint)", "var(--deep)"]
        pills = ["p-amber", "p-sky", "p-mint", "p-deep"]
        out = []
        for k, r in enumerate(rows):
            if len(r) < 2:
                continue
            tag = plain(r[2]) if len(r) > 2 else ""
            out.append('<div class="card tight" style="border-top:2px solid %s">%s'
                       '<h4 style="margin:0 0 6px">%s</h4><p style="font-size:13.8px;margin:0">%s</p></div>'
                       % (colors[k % 4],
                          ('<div class="pill %s" style="margin-bottom:9px">%s</div>' % (pills[k % 4], _html.escape(tag))) if tag else "",
                          inline(r[0]), inline(r[1])))
        if not out:
            return None
        return '<div class="grid %s rv">%s</div>' % ("g3" if len(out) % 3 == 0 else "g2", "".join(out))

    def stages(self, head, rows, args):
        klass = ["s-edge", "s-dom", "s-imp"]
        out = []
        for k, r in enumerate(rows):
            if len(r) < 2:
                continue
            items = re.split(r"\s*·\s*|\s*;\s*", r[2]) if len(r) > 2 else []
            lis = "".join("<li>%s</li>" % inline(x) for x in items if plain(x))
            out.append('<div class="stage %s"><div class="st">%s</div><h5>%s</h5>%s</div>'
                       % (klass[k % 3], inline(plain(r[0])), inline(r[1]),
                          ("<ul>%s</ul>" % lis) if lis else ""))
        if not out:
            return None
        foot = ""
        if args.get("dwell"):
            foot = '<div class="dwell"><span>⏱</span><span>%s</span></div>' % inline(args["dwell"])
        return ('<div class="kill rv"><div class="kill-head"><h4 style="margin:0">%s</h4>'
                '<span class="count">pulsa una etapa para fijarla</span></div>'
                '<div class="kill-stage">%s</div>%s</div>'
                % (inline(args.get("title", "Cadena de intrusión")), "".join(out), foot))

    def pyramid(self, head, rows, args):
        data = []
        for r in rows:
            if len(r) < 2:
                continue
            data.append((plain(r[0]), r[1], r[2] if len(r) > 2 else ""))
        if len(data) < 3:
            return None
        palette = ["#375d9d", "#5a7ebe", "#4db99c", "#a2ae4e", "#f7a400"]
        n = len(data)
        slabs = []
        for k, (name, col2, col3) in enumerate(data):
            # con tres columnas, la última es el porqué (lo que se lee en el panel)
            # y la segunda, la referencia a dónde está en el informe
            body, ref = (col3, col2) if col3 else (col2, "")
            kicker = ("Base · el nivel más barato de eludir" if k == 0 else
                      "Cima · máximo valor defensivo" if k == n - 1 else
                      "Nivel %d de %d" % (k + 1, n))
            col = palette[int(round(k * (len(palette) - 1) / float(n - 1)))]
            w = 296 - k * (200 // max(1, n - 1))
            slabs.append('<div class="slab" data-i="%d" style="--w:%dpx;--d:%dpx;--z:%dpx;--col:%s" '
                         'data-lv="%s" data-t="%s" data-b="%s" data-s="%s">'
                         '<span>%s</span></div>'
                         % (k, w, w, k * 30, col,
                            attr(kicker), attr(name),
                            _html.escape(inline(body), quote=True),
                            _html.escape(inline("En este informe: " + ref), quote=True) if ref else "",
                            _html.escape(name)))
        return ('<div class="pyr-wrap rv"><div class="pyr" id="pyr"><div class="pyr-in" id="pyrIn">%s</div></div>'
                '<div class="pyr-info card" id="pyrInfo" style="--pc:%s">'
                '<div class="lv" id="pyrLv"></div><h4 id="pyrTitle"></h4><p id="pyrBody"></p>'
                '<div class="pv" id="pyrSrc"></div></div></div>'
                % ("".join(slabs), palette[-1]))

    # ---------- componentes de párrafo ----------
    def kj_group(self, blocks, i):
        cards = []                                   # cada elemento: [html_sin_cierre]
        while i < len(blocks):
            b = blocks[i]
            if b[0] == "p" and re.match(r"^\*\*(KJ|JC)[-\s]?\d+", b[1]):
                cards.append([self.kj_card(b[1])])
                i += 1
                continue
            # párrafo de continuación del último juicio; uno que empiece en negrita
            # («**Qué cambiaría estos juicios:**…») cierra el grupo en vez de absorberse
            if b[0] == "p" and cards and not b[1].lstrip().startswith("**"):
                cards[-1].append("<p>%s</p>" % inline(b[1]))
                i += 1
                continue
            break
        if not cards:
            return i
        html_cards = "".join("".join(parts) + "</div>" for parts in cards)
        self.w('<div class="grid g2">%s</div>' % html_cards)
        return i

    def kj_card(self, text):
        m = re.match(r"^\*\*(?P<id>[^*]+?)\.?\*\*\s*(?P<rest>.*)$", text, re.S)
        kid = plain(m.group("id")) if m else "KJ"
        rest = m.group("rest") if m else text

        base = ""
        mb = re.search(r"\*Base:\*\s*(.*)$", rest, re.S)
        if mb:
            base = mb.group(1).strip()
            rest = rest[:mb.start()].strip()

        conf = ""
        mc = re.search(r"\*\*Confianza:\s*([^.*]+)\.?\*\*", rest)
        if mc:
            conf = plain(mc.group(1)).lower().strip()
            rest = (rest[:mc.start()] + rest[mc.end():]).strip()

        p, term, rango = prob_from(rest)
        cls = CONF_CLASS.get(conf, "kj-md" if p is None else ("kj-hi" if p >= 80 else "kj-md"))

        # el titular es la primera oración; se unen las demasiado cortas
        # (abreviaturas tipo «EE. UU.» parten la frase donde no toca)
        sentences = split_sentences(rest.strip())
        title, rest_idx = (sentences[0], 1) if sentences else (rest, 1)
        while len(plain(title)) < 45 and rest_idx < len(sentences):
            title += " " + sentences[rest_idx]
            rest_idx += 1
        body = " ".join(sentences[rest_idx:]) if rest_idx < len(sentences) else ""

        gauge = ""
        if p is not None:
            gauge = ('<div class="gauge" data-p="%d"><div class="lab"><span>%s</span><b>%s</b></div>'
                     '<div class="track"><i></i></div></div>'
                     % (round(p),
                        inline((term or "Probabilidad estimada").capitalize()),
                        inline(rango or "%d %%" % round(p))))
        foot = ""
        if conf or base:
            if base:
                base = base[0].upper() + base[1:]      # «*Base:* concordancia…» → «Concordancia…»
            foot = '<p class="base">%s%s</p>' % (
                ("<b>Confianza: %s.</b> " % _html.escape(conf)) if conf else "",
                inline(base))
        # se devuelve SIN el </div> de cierre: lo pone kj_group tras añadir extras
        return ('<div class="kj %s rv"><div class="id">%s</div><h4>%s</h4>%s%s%s'
                % (cls, _html.escape(kid), inline(plain(title).rstrip(".: ")),
                   ("<p>%s</p>" % inline(body)) if body else "", gauge, foot))

    def accordion(self, blocks, i, args):
        items = []
        crit = re.compile(args.get("critical", r"^(H-[1-4]|H-8)\b"))
        reg = re.compile(args.get("regional", r"^(H-1[0-9])\b"))
        while i < len(blocks):
            b = blocks[i]
            if b[0] != "p":
                if b[0] in ("list", "code", "table") and items:
                    extra = (self.list_html(b[1], b[2], plainer=True) if b[0] == "list"
                             else self.code_html(b[1], b[2], {}) if b[0] == "code"
                             else self.table_html(b[1], b[2], {}))
                    items[-1][2].append(extra)
                    i += 1
                    continue
                break
            # el separador exige espacios a ambos lados: sin eso, «**H-1 — …**»
            # se parte por el guion de «H-1» y la chapa queda en «H»
            m = re.match(r"^\*\*([^*]+?)\s+[—–-]\s+(.+?)\*\*\s*(.*)$", b[1], re.S)
            if m:
                items.append([plain(m.group(1)), plain(m.group(2)).rstrip("."),
                              ["<p>%s</p>" % inline(m.group(3))] if m.group(3).strip() else []])
                i += 1
                continue
            if items:
                items[-1][2].append("<p>%s</p>" % inline(b[1]))
                i += 1
                continue
            break
        if not items:
            return i
        out = []
        for hid, title, body in items:
            cls = "h-crit" if crit.match(hid) else ("h-reg" if reg.match(hid) else "")
            out.append('<div class="acc %s"><button><span class="hid">%s</span>'
                       '<span class="ht">%s</span>%s</button>'
                       '<div class="body">%s</div></div>'
                       % (cls, _html.escape(hid), inline(title), CHEVRON, "".join(body)))
        self.w('<div class="rv">%s</div>' % "".join(out))
        return i

    def detections(self, blocks, i):
        out = []
        cur = None
        while i < len(blocks):
            b = blocks[i]
            if b[0] == "p":
                m = re.match(r"^\*\*([A-Z]+-\d+)\s*[·|]?\s*"
                             r"(?:([A-ZÁÉÍÓÚ]{3,})\s*[—–-]\s*)?"
                             r"(?:[—–-]\s*)?(.*?)\*\*\s*(.*)$", b[1], re.S)
                if m:
                    if cur:
                        out.append(self.det_html(cur))
                    cur = {"id": m.group(1), "sev": (m.group(2) or "ALTO").upper(),
                           "name": plain(m.group(3)), "code": "", "act": m.group(4).strip(), "lang": ""}
                    i += 1
                    continue
                if cur and b[1].strip().startswith(("→", "->")):
                    cur["act"] = re.sub(r"^(→|->)\s*", "", b[1].strip())
                    i += 1
                    continue
                break
            if b[0] == "code" and cur:
                cur["code"] = self.highlight(_html.escape("\n".join(b[2])), b[1])
                cur["lang"] = b[1]
                i += 1
                continue
            if b[0] == "dir":
                break
            break
        if cur:
            out.append(self.det_html(cur))
        if not out:
            return i
        self.w("".join(out))
        return i

    def det_html(self, d):
        sev = d["sev"]
        cls = "d-crit" if sev.startswith("CRÍT") or sev.startswith("CRIT") else (
            "d-high" if sev.startswith("ALT") else "d-med")
        pill = "p-amber" if cls == "d-crit" else ("p-sky" if cls == "d-high" else "p-grey")
        return ('<div class="det %s rv"><div class="dh"><span class="did">%s</span>'
                '<span class="dn">%s</span><span class="pill %s">%s</span></div>'
                '%s%s</div>'
                % (cls, _html.escape(d["id"]), inline(d["name"]), pill, _html.escape(sev),
                   ("<pre><code>%s</code></pre>" % d["code"]) if d["code"] else "",
                   ('<div class="act">%s</div>' % inline(d["act"])) if d["act"] else ""))


# --------------------------------------------------------------------------
# Fragmentos fijos
# --------------------------------------------------------------------------

CHEVRON = ('<svg class="ar" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
           'stroke-width="2.4" stroke-linecap="round"><path d="M6 9l6 6 6-6"/></svg>')

SEARCH_BAR = ('<div class="attck-bar rv"><label class="search">'
              '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
              'stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.6-3.6"/></svg>'
              '<input id="%s" type="search" placeholder="%s" autocomplete="off"></label>'
              '<span class="count" id="%s"></span></div>')

HERO_3D = """<div class="hero-3d" id="hero3d">
  <div class="scene" id="scene">
    <div class="plane p1" id="plane1"></div>
    <div class="plane p2" id="plane2"></div>
    <div class="plane p3" id="plane3"></div>
  </div>
  <div class="hint">arrastra para girar &#8635;</div>
  <div class="legend">
    <span><i style="background:var(--amber)"></i>host comprometido</span>
    <span><i style="background:var(--sky)"></i>alcanzable</span>
    <span><i style="background:rgba(90,126,190,.42)"></i>no alcanzado</span>
  </div>
</div>"""


def build_toc(toc):
    out = []
    for g in toc:
        if not g["items"]:
            continue
        links = "".join('<a href="#%s">%s</a>' % (sid, _html.escape(label)) for sid, label in g["items"])
        out.append('<div class="%s"><h6>%s</h6>%s</div>' % (g["cls"], _html.escape(g["title"]), links))
    return "".join(out)


def build_header(meta):
    tlp = meta.get("tlp", "")
    pap = meta.get("pap", "")
    return ('<header class="topbar"><div class="topbar-in">'
            '<button class="navtoggle" id="navToggle" aria-label="Abrir índice">&#9776; Índice</button>'
            '<div class="brand"><span class="dot"></span><span>%s<small>%s</small></span></div>'
            '<div class="spacer"></div>%s%s</div>'
            '<div class="progress"><i id="prog"></i></div></header>'
            % (_html.escape(str(meta.get("id", "Informe CTI"))),
               _html.escape(str(meta.get("actor", meta.get("tipo", "")))),
               ('<span class="tlp">%s</span>' % _html.escape(tlp)) if tlp else "",
               ('<span class="pap">%s</span>' % _html.escape(pap)) if pap else ""))


def build_footer(meta):
    bits = [x for x in [meta.get("id"), meta.get("version") and "v" + str(meta["version"]), meta.get("fecha")] if x]
    caduca = ("caduca %s" % meta["caduca"]) if meta.get("caduca") else ""
    nota = meta.get("distribucion") or (
        "Distribución conforme al marcado de difusión. Los indicadores del Anexo A caducan; "
        "los TTP de los niveles táctico y técnico, no.")
    return ('<footer class="wrap"><div class="fg"><div><strong style="color:var(--ink-2)">%s</strong>%s</div>'
            '<div style="display:flex;gap:8px;align-items:center">%s%s</div></div>'
            '<p style="margin:14px 0 0;font-size:12.6px;max-width:74ch">%s</p></footer>'
            % (_html.escape(" · ".join(bits)), (" · " + _html.escape(caduca)) if caduca else "",
               ('<span class="tlp">%s</span>' % _html.escape(meta.get("tlp", ""))) if meta.get("tlp") else "",
               ('<span class="pap">%s</span>' % _html.escape(meta.get("pap", ""))) if meta.get("pap") else "",
               inline(nota)))


FAB = ('<div class="fab" id="toTop" title="Volver arriba" role="button" tabindex="0">'
       '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" '
       'stroke-linecap="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg></div>')


# --------------------------------------------------------------------------
# Tema
# --------------------------------------------------------------------------

def load_theme(path, here):
    """Devuelve el CSS. Acepta un .css o un .html del que se extrae el <style>."""
    candidates = []
    if path:
        candidates.append(path)
    candidates += [
        os.path.join(here, "cti_theme.css"),
        os.path.join(here, "..", "CTI-2026-014-thegentlemen.html"),
    ]
    for c in candidates:
        if not c or not os.path.isfile(c):
            continue
        raw = open(c, encoding="utf-8").read()
        if c.lower().endswith(".css"):
            return raw
        m = re.search(r"<style>(.*?)</style>", raw, re.S)
        if m:
            return m.group(1).strip()
    raise SystemExit("error: no encuentro el tema. Usa --theme con un .css o con un informe .html ya generado.")


# --------------------------------------------------------------------------
# JavaScript del documento (data-driven)
# --------------------------------------------------------------------------

APP_JS = r"""
(function(){
  "use strict";
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var $  = function(s,c){return (c||document).querySelector(s);};
  var $$ = function(s,c){return Array.prototype.slice.call((c||document).querySelectorAll(s));};

  var io = new IntersectionObserver(function(es){
    es.forEach(function(e){
      if(!e.isIntersecting) return;
      e.target.classList.add("in"); animateIn(e.target); io.unobserve(e.target);
    });
  },{rootMargin:"0px 0px -8% 0px",threshold:.08});
  $$(".rv").forEach(function(el){io.observe(el);});

  function animateIn(root){
    $$(".gauge",root).concat(root.classList&&root.classList.contains("gauge")?[root]:[]).forEach(function(g){
      var p = Math.max(0,Math.min(100, parseFloat(g.getAttribute("data-p"))||0));
      var bar = $(".track i",g); if(bar) setTimeout(function(){bar.style.width = p+"%";},60);
    });
    $$("[data-bars] i[data-w]",root).forEach(function(i,k){
      setTimeout(function(){ i.style.width = i.getAttribute("data-w")+"%"; }, 40+k*55);
    });
    $$("[data-count]",root).forEach(countUp);
  }

  function countUp(el){
    if(el.dataset.done) return; el.dataset.done="1";
    var target = parseFloat(el.getAttribute("data-count"))||0;
    var suf = el.querySelector("small"); var sufHTML = suf ? suf.outerHTML : "";
    if(reduce){ el.innerHTML = target.toLocaleString("es-CL")+sufHTML; return; }
    var dur = 1100, t0 = performance.now();
    (function step(t){
      var k = Math.min(1,(t-t0)/dur), e = 1-Math.pow(1-k,3);
      el.innerHTML = Math.round(target*e).toLocaleString("es-CL")+sufHTML;
      if(k<1) requestAnimationFrame(step);
    })(t0);
  }

  var prog = $("#prog"), fab = $("#toTop");
  function onScroll(){
    var h = document.documentElement.scrollHeight - window.innerHeight;
    if(prog) prog.style.width = (h>0 ? (window.scrollY/h)*100 : 0).toFixed(2)+"%";
    if(fab) fab.classList.toggle("show", window.scrollY > 700);
  }
  window.addEventListener("scroll", onScroll, {passive:true}); onScroll();
  if(fab){
    var up=function(){ window.scrollTo({top:0,behavior: reduce?"auto":"smooth"}); };
    fab.addEventListener("click", up);
    fab.addEventListener("keydown", function(e){ if(e.key==="Enter"||e.key===" "){e.preventDefault();up();} });
  }

  var links = $$("nav.toc a"), map = {};
  links.forEach(function(a){
    var s = document.getElementById(a.getAttribute("href").slice(1));
    if(s) map[s.id] = a;
  });
  var spy = new IntersectionObserver(function(es){
    es.forEach(function(e){
      if(!e.isIntersecting || !map[e.target.id]) return;
      links.forEach(function(l){l.classList.remove("on");});
      map[e.target.id].classList.add("on");
    });
  },{rootMargin:"-88px 0px -72% 0px",threshold:0});
  Object.keys(map).forEach(function(k){ spy.observe(document.getElementById(k)); });

  var toc = $("#toc"), toggle = $("#navToggle"), scrim = null;
  function closeNav(){ if(toc) toc.classList.remove("open"); if(scrim){scrim.remove(); scrim=null;} }
  if(toggle) toggle.addEventListener("click", function(){
    if(toc.classList.contains("open")) return closeNav();
    toc.classList.add("open");
    scrim = document.createElement("div"); scrim.className="scrim";
    scrim.addEventListener("click", closeNav); document.body.appendChild(scrim);
  });
  links.forEach(function(a){ a.addEventListener("click", function(){ if(window.innerWidth<=1080) closeNav(); }); });

  /* escena 3D de portada */
  (function(){
    var scene = $("#scene"), host = $("#hero3d"); if(!scene||!host) return;
    var planes = [$("#plane1"),$("#plane2"),$("#plane3")], G=5, nodes=[];
    planes.forEach(function(pl,pi){
      for(var r=0;r<G;r++) for(var c=0;c<G;c++){
        if(pi===0 && (r+c)%2===1) continue;
        if(pi===2 && (r%2===1||c%2===1)) continue;
        var n=document.createElement("i"); n.className="node host";
        n.style.left=(12+c*19)+"%"; n.style.top=(12+r*19)+"%";
        pl.appendChild(n); nodes.push({el:n,p:pi,r:r,c:c,on:false});
      }
    });
    function neighbours(n){
      return nodes.filter(function(m){
        if(m.on) return false;
        var dp=Math.abs(m.p-n.p), dr=Math.abs(m.r-n.r), dc=Math.abs(m.c-n.c);
        if(dp===0) return dr+dc<=2 && dr+dc>0;
        if(dp===1) return dr<=2 && dc<=2;
        return false;
      });
    }
    var queue=[];
    function seed(){
      nodes.forEach(function(n){n.on=false;n.el.className="node host";});
      queue=[];
      var start=nodes.filter(function(n){return n.p===0;});
      var s=start[Math.floor(Math.random()*start.length)];
      s.on=true; s.el.className="node seed"; queue.push(s); step();
    }
    function step(){
      if(reduce) return;
      setTimeout(function(){
        if(!queue.length){ setTimeout(seed,1600); return; }
        var batch=queue.splice(0,2), next=[];
        batch.forEach(function(n){
          neighbours(n).slice(0,3).forEach(function(m){
            if(m.on) return; m.on=true; m.el.className="node hit"; next.push(m);
          });
        });
        queue=queue.concat(next); step();
      },220);
    }
    if(!reduce) seed(); else nodes.forEach(function(n,i){ if(i%3===0) n.el.className="node hit"; });
    drag(host, scene, 58, -34, 24, 80);
  })();

  /* pirámide 3D, alimentada por data-* */
  (function(){
    var pyr=$("#pyr"), inner=$("#pyrIn"); if(!pyr||!inner) return;
    var slabs=$$(".slab",inner), infoEl=$("#pyrInfo");
    function darken(hex,f){
      var n=parseInt(hex.slice(1),16);
      return "rgb("+Math.round(((n>>16)&255)*f)+","+Math.round(((n>>8)&255)*f)+","+Math.round((n&255)*f)+")";
    }
    slabs.forEach(function(s){
      var col=s.style.getPropertyValue("--col").trim();
      s.style.width=s.style.getPropertyValue("--w").trim();
      s.style.height=s.style.getPropertyValue("--d").trim();
      s.style.background="linear-gradient(135deg,"+col+","+darken(col,.78)+")";
      s.style.transform="translate(-50%,-50%) translateZ("+s.style.getPropertyValue("--z").trim()+")";
      var side=darken(col,.5), sh=[];
      for(var i=1;i<=13;i++) sh.push("0 "+i+"px 0 "+side);
      sh.push("0 22px 34px -12px rgba(0,0,0,.75)");
      s.style.boxShadow=sh.join(",");
    });
    function select(i){
      slabs.forEach(function(s){ s.classList.toggle("act", +s.getAttribute("data-i")===i); });
      var s=slabs.filter(function(x){return +x.getAttribute("data-i")===i;})[0]; if(!s) return;
      infoEl.style.setProperty("--pc", s.style.getPropertyValue("--col").trim());
      $("#pyrLv").textContent = s.getAttribute("data-lv")||"";
      $("#pyrTitle").textContent = s.getAttribute("data-t")||"";
      $("#pyrBody").innerHTML = s.getAttribute("data-b")||"";
      var src=$("#pyrSrc"); if(src) src.innerHTML = s.getAttribute("data-s")||"";
    }
    slabs.forEach(function(s){
      s.addEventListener("click", function(){ select(+s.getAttribute("data-i")); });
    });
    if(slabs.length) select(slabs.length-1);
    drag(pyr, inner, 64, 0, 20, 84);
  })();

  /* rotación por arrastre, compartida */
  function drag(host, target, rx0, rz0, minX, maxX){
    var rx=rx0, rz=rz0, on=false, sx=0, sy=0;
    function apply(){ target.style.transform="rotateX("+rx+"deg) rotateZ("+rz+"deg)"; }
    function pt(e){ var t=e.touches&&e.touches[0]; return {x:t?t.clientX:e.clientX, y:t?t.clientY:e.clientY}; }
    function down(e){ on=true; var p=pt(e); sx=p.x; sy=p.y; target.style.transition="none"; }
    function move(e){
      if(!on) return; var p=pt(e);
      rz += (p.x-sx)*0.44; rx = Math.max(minX, Math.min(maxX, rx-(p.y-sy)*0.3));
      sx=p.x; sy=p.y; apply();
      if(e.type==="touchmove" && e.cancelable) e.preventDefault();
    }
    function up(){ on=false; target.style.transition=""; }
    host.addEventListener("mousedown",down);
    host.addEventListener("touchstart",down,{passive:true});
    window.addEventListener("mousemove",move);
    window.addEventListener("touchmove",move,{passive:false});
    window.addEventListener("mouseup",up);
    window.addEventListener("touchend",up);
    apply();
  }

  /* cronologías con filtros */
  $$(".tlfilter").forEach(function(bar){
    var tl = document.getElementById(bar.getAttribute("data-for")); if(!tl) return;
    var evs = $$(".ev", tl);
    $$("[data-tl]", bar).forEach(function(btn){
      btn.addEventListener("click", function(){
        var k = btn.getAttribute("data-tl");
        $$("[data-tl]", bar).forEach(function(b){ b.classList.remove("on","a"); });
        btn.classList.add("on");
        if(k!=="all" && k!=="gl") btn.classList.add("a");
        evs.forEach(function(ev){
          var keys=(ev.getAttribute("data-k")||"").split(" ");
          ev.hidden = !(k==="all" || keys.indexOf(k)>=0);
        });
      });
    });
  });

  /* buscadores */
  function wire(inputId, counterId, itemSel, groupSel, noun){
    var input=$("#"+inputId); if(!input) return;
    var items=$$(itemSel), groups=groupSel?$$(groupSel):[], counter=$("#"+counterId);
    function run(){
      var q=input.value.trim().toLowerCase(), shown=0;
      items.forEach(function(t){
        var hay=((t.getAttribute("data-s")||"")+" "+t.textContent).toLowerCase();
        var ok = !q || hay.indexOf(q)>=0; t.hidden=!ok; if(ok) shown++;
      });
      groups.forEach(function(g){ g.hidden = $$(itemSel,g).every(function(t){return t.hidden;}); });
      if(counter) counter.textContent = shown+" de "+items.length+" "+noun;
    }
    input.addEventListener("input", run); run();
  }
  wire("attckSearch","attckCount",".tq","[data-col]","técnicas");
  wire("iocSearch","iocCount",".ioc-row",null,"indicadores");

  $$(".ioc-row .vv").forEach(function(v){
    v.style.cursor="copy"; v.title="Pulsa para copiar";
    v.addEventListener("click", function(){
      var txt = v.childNodes[0] ? v.childNodes[0].textContent.trim() : v.textContent.trim();
      copy(txt, function(ok){
        var old=v.style.color; v.style.color= ok?"#4db99c":"#f7a400";
        setTimeout(function(){ v.style.color=old; },700);
      });
    });
  });

  $$(".acc > button").forEach(function(b){
    b.addEventListener("click", function(){ b.parentElement.classList.toggle("open"); });
  });

  $$(".stage").forEach(function(s){
    s.addEventListener("click", function(){
      var on=s.classList.contains("fixed");
      $$(".stage").forEach(function(o){ o.classList.remove("fixed"); });
      if(!on) s.classList.add("fixed");
    });
  });

  function copy(text, cb){
    if(navigator.clipboard && navigator.clipboard.writeText){
      navigator.clipboard.writeText(text).then(function(){cb(true);},function(){cb(false);}); return;
    }
    try{
      var ta=document.createElement("textarea"); ta.value=text;
      ta.setAttribute("readonly",""); ta.style.position="fixed"; ta.style.opacity="0";
      document.body.appendChild(ta); ta.select(); document.execCommand("copy"); ta.remove(); cb(true);
    }catch(e){ cb(false); }
  }
  $$(".copy").forEach(function(btn){
    btn.addEventListener("click", function(){
      var wrap=btn.closest(".codewrap"), pre=wrap?wrap.querySelector("pre"):null; if(!pre) return;
      copy(pre.innerText, function(ok){
        btn.textContent = ok?"copiado ✓":"error"; btn.classList.toggle("ok",ok);
        setTimeout(function(){ btn.textContent="copiar"; btn.classList.remove("ok"); },1500);
      });
    });
  });

  document.addEventListener("keydown", function(e){
    if(e.key==="/" && !/^(INPUT|TEXTAREA)$/.test(document.activeElement.tagName)){
      var vis=$$(".search input").filter(function(i){
        var r=i.getBoundingClientRect(); return r.top>0 && r.top<window.innerHeight;
      });
      if(vis.length){ e.preventDefault(); vis[0].focus(); }
    }
    if(e.key==="Escape") closeNav();
  });
})();
"""


# --------------------------------------------------------------------------
# Ensamblado
# --------------------------------------------------------------------------

# elementos de bloque que empiezan en su propia línea: sin esto el HTML sale
# como una sola línea de 200 KB, ilegible de inspeccionar e inútil en un diff
BLOCK_START = re.compile(
    r'(?<!^)(<section\b|</section>|<div class="(?:level|wrap|tw|card|note|grid|kj|det|acc|chart|'
    r'codewrap|stat|mcol|tq|ev |ioc-row|src |bar |stage |pyr|kill|tlfilter|attck-bar|matrix|bars|tl )'
    r'|<h3\b|<h4\b|<p class="rv"|<dl class="meta-grid|<tr>|<tr\s|<pre>|<footer\b|<nav\b|<main>|</main>)')


def prettify(html_text):
    return BLOCK_START.sub(r"\n\1", html_text)


def render(md_text, css, opts):
    meta, body = read_frontmatter(md_text)
    blocks = tokenize(body)
    r = Renderer(meta, opts)
    main = prettify(r.run(blocks))
    title = opts.title or ("%s · %s" % (meta.get("id", "Informe CTI"), meta.get("actor", ""))).strip(" ·")
    lang = meta.get("idioma", "es")
    return (
        "<!doctype html>\n<html lang=\"%s\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
        "<title>%s</title>\n<style>\n%s\n</style>\n</head>\n<body>\n"
        "%s\n<div class=\"shell\">\n<nav class=\"toc\" id=\"toc\">%s</nav>\n<main>\n%s\n%s\n%s\n</main>\n</div>\n"
        "<script>%s</script>\n</body>\n</html>\n"
        % (_html.escape(lang), _html.escape(title), css,
           build_header(meta), build_toc(r.toc), main, build_footer(meta), FAB, APP_JS)
    )


def main():
    ap = argparse.ArgumentParser(
        description="Convierte un informe CTI en Markdown al HTML del sistema de diseño.")
    ap.add_argument("entrada", help="informe .md")
    ap.add_argument("-o", "--salida", help="archivo .html de salida (por defecto, el mismo nombre)")
    ap.add_argument("--theme", help=".css del tema, o un .html del que extraerlo")
    ap.add_argument("--title", help="título de la pestaña (por defecto, id + actor)")
    ap.add_argument("--no-leads", dest="leads", action="store_false",
                    help="no promover el primer párrafo de cada sección a subtítulo")
    ap.add_argument("--version", action="version", version="cti_render %s" % VERSION)
    ap.set_defaults(leads=True)
    opts = ap.parse_args()

    here = os.path.dirname(os.path.abspath(__file__))
    if not os.path.isfile(opts.entrada):
        raise SystemExit("error: no existe %s" % opts.entrada)
    md = open(opts.entrada, encoding="utf-8").read()
    css = load_theme(opts.theme, here)
    out = opts.salida or os.path.splitext(opts.entrada)[0] + ".html"
    html_text = render(md, css, opts)
    open(out, "w", encoding="utf-8").write(html_text)
    sys.stderr.write("✓ %s → %s  (%.0f KB)\n" % (opts.entrada, out, len(html_text) / 1024.0))


if __name__ == "__main__":
    main()
