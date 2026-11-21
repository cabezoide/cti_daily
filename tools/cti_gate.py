#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cti_gate — compuerta obligatoria de la cartera de informes.

QUÉ PROBLEMA RESUELVE
=====================

`cti_build.py` construye. Esta compuerta **impide publicar**. Son cosas
distintas y conviene que vivan en ficheros distintos: un constructor que
además juzga acaba cediendo, porque quien lo ejecuta quiere que termine.

Las tres compuertas salen de fallos que esta cartera **ya cometió**, no de
una lista de buenas prácticas:

**G1 · CONSISTENCIA.** `CTI-2026-058` v1.0 afirmó «la última entrada es del
7 de noviembre» y «lleva doce días sin publicar» con fecha de cierre el 19:
del 7 al 19 hay doce días, así que la aritmética cerraba. Pero el dato de
partida era falso y **nada en el texto podía detectarlo**. Lo que sí se puede
detectar por máquina es la familia de fallos vecina: una versión que no
aparece en su propio control de cambios, una referencia a una sección que no
existe, un `KJ-n` citado y nunca definido, una fecha futura, una cifra que el
propio informe se contradice.

**G2 · VERACIDAD.** Un informe caducado miente por omisión, y uno que
declara un disparador cumplido sin mover el juicio miente por acción. Esta
compuerta no verifica el mundo —no puede—: verifica que **lo que el informe
dice de sí mismo** sea cierto.

**G3 · ATRIBUCIÓN DE FUENTES.** El fallo más caro de esta cartera es
presentar como hecho lo que es afirmación de un tercero, y elevar la
confianza de una fuente al citarla. La compuerta exige que toda afirmación
marcada como juicio lleve probabilidad **y** confianza del léxico ICD 203, y
que los indicadores lleven acción permitida.

**G4 · HIGIENE DE INDICADORES.** Las cinco reglas R1–R5 ya escritas: una
víctima no es un indicador, un bloque con máscara no es una dirección, una
herramienta legítima no entra en un agregado plano.

CÓMO SE USA
===========

    python3 tools/cti_gate.py                 # toda la cartera
    python3 tools/cti_gate.py CTI-2026-058*   # sólo unos informes
    python3 tools/cti_gate.py --avisos        # los avisos no bloquean
    python3 tools/cti_gate.py --json          # para encadenar

**Código de salida 1 si alguna compuerta BLOQUEA.** Eso es el punto: está
enganchada en `.githooks/pre-commit` antes de construir, y un commit con un
bloqueo no sale. Para saltarla hace falta decirlo en voz alta:

    CTI_GATE_OMITIR=1 git commit …

y el hook lo escribe en la salida, porque una omisión silenciosa de una
compuerta no es una compuerta.
"""

import argparse
import datetime as _dt
import ipaddress
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "tools"))

import cti_build as B                                            # noqa: E402


# ───────────────────────────────────────────────────────── léxico y constantes

# ICD 203. Si una probabilidad no está aquí, no es del léxico y no vale.
PROBABILIDAD = [
    "casi con certeza", "casi con certeza no",
    "muy probable", "muy improbable",
    "probable", "improbable",
    "posible",
    # La cartera usa «posibilidad real» para el tramo 45–55 % —así lo declara el
    # `Anexo C` de los informes— y omitirla señalaba como «juicio sin
    # probabilidad» a juicios que la llevaban, entre ellos `KJ-5` de
    # `CTI-2026-026` y `KJ-7` de `CTI-2026-035`.
    "posibilidad real", "aproximadamente igual de probable",
    "igual de probable",
]
CONFIANZA = ["alta", "moderada", "baja"]

# R4: tipos que NUNCA deben acabar en un agregado plano de bloqueo.
TIPOS_NO_BLOQUEABLES = {"herramienta", "artefacto", "asn", "cartera",
                        "pattern", "patron", "filename", "tecnica", "cve"}

# R1 · marcas de que el valor es un OBJETIVO y no infraestructura del adversario.
#
# La primera versión de esta lista incluía «víctima» y «atacad», y daba falsos
# positivos inmediatos: `CTI-2026-015` tiene una dirección *del atacante* cuyo
# contexto dice «campaña contra víctima chilena», y `CTI-2026-045` una de mando
# y control descrita en una tabla donde esas palabras aparecen. La palabra
# «víctima» en el contexto no dice de quién es la dirección. Sólo valen las
# marcas que lo dicen del valor mismo.
MARCAS_VICTIMA = ("nunca bloqueo", "prefijo atacado", "red atacada",
                  "objetivo del ataque", "prefijo objetivo", "red objetivo",
                  "asn atacado", "organización atacada")

# …y estas lo contradicen: si están, el valor es del adversario.
MARCAS_ADVERSARIO = ("mando y control", "command and control", "c2",
                     "del atacante", "del adversario", "infraestructura del actor",
                     "panel", "exfiltración", "descarga")

# El grupo numérico NO debe terminar en punto: `[\d.]+` es codicioso y capturaba
# «E-1.» del encabezado «## E-1. Cifras», que nunca coincide con la referencia
# `E-1` del cuerpo. Producía un aviso C5 por cada sección correctamente citada.
RE_SECCION = re.compile(r"^#{2,3}\s+(?:`?([A-Z]{1,2}-\d+(?:\.\d+)*|\d+)`?\.?|Anexo\s+([A-Z]))",
                        re.M)
RE_REF_SECCION = re.compile(r"`((?:KJ|E|O|X|G|H|I|A)-[\dA-Za-z.]+)`")
# El marcado real de la cartera varía: `**KJ-8.**` y `**KJ-8 (nuevo en v1.2).**`
# son ambos definiciones. Una regex estricta daba KJ-8..KJ-11 de `CTI-2026-017`
# por indefinidos cuando sí lo estaban, que es la clase de falso positivo que
# hace que una compuerta se omita siempre.
RE_DEF_KJ = re.compile(r"^\*\*(KJ-\d+)\b[^*]*\*\*", re.M)
RE_FILA_VERSION = re.compile(r"^\|\s*\*{0,2}([\d.]+)\*{0,2}\s*\|\s*\*{0,2}(\d{4}-\d{2}-\d{2})",
                             re.M)
RE_FECHA = re.compile(r"\b(20\d{2}-\d{2}-\d{2})\b")
RE_MASCARA = re.compile(r"/\d{1,3}$")


class Hallazgo:
    __slots__ = ("informe", "compuerta", "regla", "bloquea", "mensaje", "donde")

    def __init__(self, informe, compuerta, regla, bloquea, mensaje, donde=""):
        self.informe = informe
        self.compuerta = compuerta
        self.regla = regla
        self.bloquea = bloquea
        self.mensaje = mensaje
        self.donde = donde

    def a_dict(self):
        return {"informe": self.informe, "compuerta": self.compuerta,
                "regla": self.regla, "bloquea": self.bloquea,
                "mensaje": self.mensaje, "donde": self.donde}


# ─────────────────────────────────────────────────────── G1 · CONSISTENCIA

def g1_consistencia(inf, hoy):
    """Lo que el informe dice de su propia estructura tiene que cuadrar."""
    H = []
    t, fm, ident = inf["texto"], inf["fm"], inf["id"]
    ap = lambda r, b, m, d="": H.append(Hallazgo(ident, "consistencia", r, b, m, d))

    # ── C1 · la versión del frontmatter existe en el control de cambios
    version = fm.get("version", "")
    versiones = {m.group(1) for m in RE_FILA_VERSION.finditer(t)}
    if version and versiones and version not in versiones:
        ap("C1", True,
           "`version: %s` no aparece en el control de cambios, que lista %s. "
           "Una versión sin fila es una versión sin explicación."
           % (version, ", ".join(sorted(versiones))))

    # ── C2 · la fila más reciente del control de cambios no puede ser futura
    for v, f in RE_FILA_VERSION.findall(t):
        try:
            if _dt.date.fromisoformat(f) > hoy:
                ap("C2", True, "el control de cambios fecha la versión %s el %s, "
                               "que es futuro." % (v, f))
        except ValueError:
            ap("C2", False, "fecha ilegible en el control de cambios: %r" % f)

    # ── C3 · todo KJ-n citado está definido
    definidos = {m.group(1) for m in RE_DEF_KJ.finditer(t)}
    citados = {r for r in RE_REF_SECCION.findall(t) if r.startswith("KJ-")}
    huerfanos = citados - definidos
    if huerfanos:
        ap("C3", True, "cita juicios que no define: %s. "
                       "Una referencia a un juicio inexistente es una afirmación sin dueño."
           % ", ".join(sorted(huerfanos, key=lambda z: int(z.split("-")[1]))))

    # ── C4 · los KJ están numerados sin huecos
    if definidos:
        nums = sorted(int(k.split("-")[1]) for k in definidos)
        faltan = [n for n in range(1, nums[-1] + 1) if n not in nums]
        if faltan:
            ap("C4", False, "la numeración de juicios tiene huecos: falta %s."
               % ", ".join("KJ-%d" % n for n in faltan))

    # ── C5 · las secciones citadas existen
    presentes = set()
    for m in RE_SECCION.finditer(t):
        if m.group(1):
            presentes.add(m.group(1))
        if m.group(2):
            presentes.add("Anexo " + m.group(2))
    refs = {r for r in RE_REF_SECCION.findall(t) if not r.startswith("KJ-")}
    # G-n, H-n, I-n son listas internas (brechas, hipótesis, disparadores): no
    # son encabezados, así que sólo se comprueban los prefijos estructurales.
    faltantes = {r for r in refs
                 if r.split("-")[0] in ("E", "O", "X") and r not in presentes}
    if faltantes:
        ap("C5", False, "cita secciones que no son encabezados de este informe: %s. "
                        "Puede ser referencia a otro informe sin indicarlo."
           % ", ".join(sorted(faltantes)))

    # ── C6 · fechas futuras en el cuerpo, salvo las declaradas como futuras
    for f in set(RE_FECHA.findall(t)):
        try:
            d = _dt.date.fromisoformat(f)
        except ValueError:
            continue
        if d <= hoy:
            continue
        ctx = "\n".join(l for l in t.split("\n") if f in l).lower()
        if any(p in ctx for p in ("caduca", "reevaluar", "reevaluación", "decisión",
                                  "fecha de decisión", "hasta", "vence", "plazo",
                                  "i-1", "revisar")):
            continue
        ap("C6", False, "la fecha %s es futura y su contexto no la declara como "
                        "plazo ni como reevaluación." % f)

    # ── C9 · el control de cambios va de lo más reciente a lo más antiguo
    #    La convención de la casa dice «la primera fila de la tabla». En
    #    `CTI-2026-053` quedaron 1.0, 1.2, 1.1: quien lo lea de arriba abajo
    #    cree que la última palabra es la 1.1.
    filas = RE_FILA_VERSION.findall(t)
    if len(filas) > 1:
        def clave(v):
            try:
                return [int(x) for x in v[0].split(".")]
            except ValueError:
                return [0]
        ordenadas = sorted(filas, key=clave, reverse=True)
        if [f[0] for f in filas] != [f[0] for f in ordenadas]:
            ap("C9", False, "el control de cambios no está en orden descendente "
                            "(%s). La convención pone la versión más reciente "
                            "primero." % " · ".join(f[0] for f in filas))

    # ── C7 · frontmatter completo
    for clave in ("id", "version", "tlp", "fecha", "caduca", "actor", "distribucion"):
        if not fm.get(clave):
            ap("C7", True, "el frontmatter no declara `%s`." % clave)

    # ── C8 · el identificador del frontmatter coincide con el nombre del fichero
    esperado = inf["md"][:12]
    if fm.get("id") and fm["id"] != esperado:
        ap("C8", True, "`id: %s` no coincide con el nombre del fichero (%s)."
           % (fm["id"], esperado))

    return H


# ───────────────────────────────────────────────────────── G2 · VERACIDAD

def g2_veracidad(inf, hoy):
    """El informe no puede mentir sobre su propio estado."""
    H = []
    t, fm, ident = inf["texto"], inf["fm"], inf["id"]
    ap = lambda r, b, m, d="": H.append(Hallazgo(ident, "veracidad", r, b, m, d))

    # ── V1 · caducado
    estado, dias = B.vigencia(fm, hoy)
    if estado == "caducado":
        ap("V1", True, "CADUCADO hace %d días (`caduca: %s`). Un informe caducado "
                       "miente por omisión: o se revalida y se extiende, o se "
                       "declara histórico." % (abs(dias), fm.get("caduca")))
    elif estado == "sin fecha":
        ap("V1", True, "no declara fecha de caducidad legible.")
    elif estado == "por caducar":
        ap("V1", False, "caduca en %d días." % dias)

    # ── V2 · `caduca` no puede ser anterior a `fecha`
    try:
        if _dt.date.fromisoformat(fm.get("caduca", "")) <= \
           _dt.date.fromisoformat(fm.get("fecha", "")):
            ap("V2", True, "`caduca` (%s) no es posterior a `fecha` (%s)."
               % (fm.get("caduca"), fm.get("fecha")))
    except ValueError:
        pass

    # ── V3 · un disparador marcado CUMPLIDO exige que el control de cambios lo diga
    cumplidos = re.findall(r"\*\*CUMPLIDO[^*]*\*\*", t)
    if cumplidos:
        # Exigir la palabra «cumplido» en el control de cambios era demasiado
        # literal: `CTI-2026-053` registró el movimiento en dos versiones
        # nuevas sin usar esa palabra, y eso no es un disparador decorativo.
        # Lo que delata al decorativo es que NADA se movió: un solo asiento.
        filas_cc = RE_FILA_VERSION.findall(t)
        inicial = fm.get("version", "1.0") in ("1.0", "1")
        if len(filas_cc) < 2 and not inicial:
            ap("V3", True, "declara %d disparador(es) CUMPLIDO y su control de "
                           "cambios tiene un solo asiento: nada se movió. Un "
                           "disparador que se cumple y no mueve nada es un "
                           "disparador decorativo." % len(cumplidos))
        elif len(filas_cc) < 2 and inicial:
            # Una emisión inicial puede nacer con sus propios disparadores ya
            # comprobados —`CTI-2026-062` cumplió el suyo durante la redacción—
            # y entonces no hay versión anterior cuyo juicio mover. Bloquearlo
            # exigiría inventar un asiento 0.9 para satisfacer a la compuerta.
            ap("V3", False, "declara disparador(es) CUMPLIDO en la emisión inicial. "
                            "Correcto si se comprobaron al redactar; revisar que el "
                            "asiento 1.0 lo mencione.")
        elif not re.search(r"cumplid|CUMPLID", t[t.find("Control de cambios"):]):
            ap("V3", False, "declara disparador(es) CUMPLIDO; el control de cambios "
                            "registra movimiento pero no los nombra.")

    # ── V4 · la versión > 1.0 obliga a más de una fila de control de cambios
    filas = RE_FILA_VERSION.findall(t)
    if fm.get("version", "1.0") not in ("1.0", "1") and len(filas) < 2:
        ap("V4", True, "declara versión %s con %d fila(s) de control de cambios."
           % (fm.get("version"), len(filas)))

    # ── V5 · si el informe dice que extiende la caducidad, tiene que justificarlo
    if re.search(r"caduca.{0,40}extend|extend.{0,40}caduca", t, re.I):
        if not re.search(r"revalid", t, re.I):
            ap("V5", False, "menciona extender la caducidad sin usar la palabra "
                            "«revalidar». Añadir victimología no es revalidar.")

    return H


# ──────────────────────────────────────────────── G3 · ATRIBUCIÓN DE FUENTES

def _bloques_kj(t):
    """Los bloques de juicio, **acotados**.

    Partir sólo por el inicio del siguiente `KJ` dejaba que el último juicio se
    comiera el resto del documento —anexos incluidos—, y entonces A4 saltaba
    en el juicio de número más alto de casi todos los informes porque en algún
    anexo aparecían «no corroborado» y «confianza: alta» sin relación entre sí.
    Un bloque termina donde empieza el siguiente juicio, o en el primer
    encabezado o separador posterior.
    """
    salida = []
    for m in RE_DEF_KJ.finditer(t):
        resto = t[m.start():]
        fin = len(resto)
        sig = RE_DEF_KJ.search(resto, m.end() - m.start())
        if sig:
            fin = min(fin, sig.start())
        corte = re.search(r"\n(?:---|\s*##\s)", resto)
        if corte:
            fin = min(fin, corte.start())
        salida.append((m.group(1), resto[:fin]))
    return salida


def g3_atribucion(inf):
    """Quién dice cada cosa, y con cuánta confianza puede decirla."""
    H = []
    t, ident = inf["texto"], inf["id"]
    ap = lambda r, b, m, d="": H.append(Hallazgo(ident, "atribución", r, b, m, d))

    # ── A1 · todo KJ lleva probabilidad y confianza del léxico
    bloques = _bloques_kj(t)
    for kj, bl in bloques:
        bajo = bl.lower()
        if not any(p in bajo for p in PROBABILIDAD):
            ap("A1", True, "%s no usa ninguna probabilidad del léxico ICD 203. "
                           "Un juicio sin probabilidad no es un juicio: es una opinión."
               % kj, kj)
        if "confianza" not in bajo:
            ap("A1", True, "%s no declara confianza." % kj, kj)
        elif not any(re.search(r"confianza[:\s\*]*(?:[a-zñáéíóú ]*\b)?" + c, bajo)
                     for c in CONFIANZA):
            ap("A1", False, "%s declara confianza con un término fuera de "
                            "{alta, moderada, baja}." % kj, kj)

    # ── A2 · el informe tiene que declarar sus fuentes
    if not re.search(r"Anexo B|Fuentes y valoración|## .*Fuentes", t):
        ap("A2", True, "no tiene anexo de fuentes. Sin él no se puede saber de "
                       "quién es cada afirmación.")

    # ── A3 · afirmación de tercero presentada sin marcar
    #    Busca el patrón peligroso: una cifra rotunda en un juicio cuya única
    #    base es un proveedor, sin que el juicio lo diga.
    for kj, bl in bloques:
        bajo = bl.lower()
        tiene_base = re.search(r"\*base:\*|\*base\*|base:|medición propia|"
                               r"declarad|según|afirma|perfil del proveedor|"
                               r"la ficha|el aviso|corrobora|observ|midió|medim", bajo)
        if not tiene_base:
            ap("A3", False, "%s no declara su base. Todo juicio debería decir de "
                            "dónde sale, aunque sea medición propia." % kj, kj)

    # ── A4 · no elevar la confianza por encima de la fuente
    #    Un juicio con confianza alta cuya base es una sola ficha de proveedor y
    #    que además dice «no corroborado» es una contradicción.
    for kj, bl in bloques:
        bajo = bl.lower()
        if re.search(r"no (?:está |se )?corrobor|sin corrobor|no verificad", bajo) \
           and re.search(r"confianza[:\s\*]*alta(?![a-z])", bajo) \
           and "alta para el dato" not in bajo \
           and "alta como" not in bajo \
           and "alta para la observación" not in bajo:
            # Aviso y no bloqueo, deliberadamente. En `CTI-2026-050` `KJ-2`
            # la confianza alta es sobre medición propia y «no verificadas»
            # califica a las reclamaciones *del adversario*: dos cosas que
            # coinciden en el párrafo sin relación lógica. Distinguirlo exige
            # leer la frase, no casarla con una expresión regular, y una
            # compuerta sólo debe bloquear lo que determina con certeza.
            ap("A4", False, "%s declara confianza alta y en el mismo juicio "
                            "aparece que algo no está corroborado. Revisar que la "
                            "confianza no se apoye en lo no corroborado: si la "
                            "fuente no corrobora, hay que decir alta *en qué*."
               % kj, kj)

    return H


# ─────────────────────────────────────────────── G4 · HIGIENE DE INDICADORES

def g4_higiene(inf):
    """R1–R5. Un indicador mal formado es peor que su ausencia."""
    H = []
    ident = inf["id"]
    ap = lambda r, b, m, d="": H.append(Hallazgo(ident, "higiene", r, b, m, d))

    try:
        filas = B.filas_ioc(inf)
    except Exception as ex:                                  # pragma: no cover
        ap("R0", False, "no se pudieron extraer las filas de indicadores: %s" % ex)
        return H

    for fila in filas:
        tipo = (fila.get("tipo") or "").strip().lower()
        valor = (fila.get("valor") or "").strip()
        ctx = " ".join(str(fila.get(k, "")) for k in fila).lower()
        corto = valor[:60]

        # ── R5 · un bloque con máscara no es una dirección
        if tipo.startswith("ipv4") and RE_MASCARA.search(valor):
            ap("R5", True, "`%s` va con tipo `%s` pero lleva máscara: el agregado "
                           "plano espera direcciones individuales. Debe ser "
                           "`artefacto`." % (corto, tipo), corto)

        # ── R1 · una víctima no es un indicador
        if tipo.startswith("ipv4") and any(k in ctx for k in MARCAS_VICTIMA) \
           and not any(k in ctx for k in MARCAS_ADVERSARIO):
            ap("R1", True, "`%s` va con tipo `%s` y su contexto lo describe como "
                           "objetivo o lleva «NUNCA bloqueo». Una ingesta ingenua "
                           "bloquearía al atacado, y el fallo sería silencioso."
               % (corto, tipo), corto)

        # ── R1b · un ASN no es una dirección
        #    El agregado plano lo descarta al validar, así que el fallo no llega
        #    a `ioc_ipv4.txt`; pero la fila queda mal tipada y el consumidor que
        #    lea la tabla —no el agregado— recibe un ASN donde espera una IP.
        if valor.upper().startswith("AS") and valor[2:3].isdigit() \
           and tipo.startswith("ipv4"):
            ap("R1b", True, "`%s` lleva tipo `ipv4` y es un **ASN**. Debe ser "
                            "`asn`, o `artefacto` si va con «NUNCA bloqueo»."
               % corto, corto)

        # ── R4 · una herramienta legítima no va a un agregado plano
        destino = B.clasificar(fila)
        if destino and tipo in TIPOS_NO_BLOQUEABLES:
            ap("R4", True, "`%s` tiene tipo `%s` y aun así cae en el agregado "
                           "`ioc_%s.txt`. Bloquearlo rompe la organización, no al "
                           "adversario." % (corto, tipo, destino), corto)

        # ── R7 · la acción permitida y el tipo no pueden contradecirse
        #
        #    El fallo que motivó esta regla se cometió al redactar `CTI-2026-062`:
        #    tres filas decían «NO bloquear» en la columna de acción permitida y
        #    llevaban tipo `domain`, que las enviaba al agregado plano —una lista
        #    de bloqueo— de todos modos. La tabla se contradecía a sí misma y sólo
        #    se detectó con un `grep` posterior a la construcción. Ahora lo
        #    detecta la compuerta, que es donde debía estar.
        accion = " ".join(str(v) for k, v in fila.items()
                          if "acci" in str(k).lower()).lower()
        niega = any(k in accion for k in (
            "nunca bloqueo", "no bloqueo", "no bloquear", "nunca se bloquea",
            "no implementar", "no como contramedida", "jamás bloqueo"))
        # Una negación puede referirse a un objeto DISTINTO del indicador:
        # `CTI-2026-043` dice «No bloquear MeshCentral como producto» en filas
        # cuyo valor es el MD5 de una muestra concreta, y un hash no bloquea un
        # producto. Esa clase de fila baja a aviso: decidirlo exige leer qué se
        # niega, y la compuerta sólo bloquea lo que determina con certeza.
        # Y si la acción AUTORIZA expresamente el bloqueo de algo —`CTI-2026-035`
        # dice «Bloqueo SÓLO de la URL completa. NO bloquear el dominio base»—
        # la fila no se contradice: autoriza lo que publica y niega otra cosa.
        autoriza = re.search(r"bloque(?:o|ar)\s+(?:s[oó]lo|[uú]nicamente|exclusivamente|"
                             r"de la url|con revisi[oó]n|por el feed)", accion) is not None
        objeto_distinto = autoriza or re.search(
            r"no bloquear\s+(?!este|esta|el indicador|la direcci|el valor|el hash)"
            r"[\w.\-]{3,}", accion) is not None
        if destino and niega and objeto_distinto:
            ap("R7", False, "`%s` dice «no bloquear» nombrando algo que puede no "
                            "ser el indicador mismo, y su tipo `%s` lo envía a "
                            "`ioc_%s.txt`. **Revisar a mano** si lo que no debe "
                            "bloquearse es este valor o un producto."
               % (corto, tipo, destino), corto)
        elif destino and niega:
            ap("R7", True, "`%s` declara en su acción permitida que NO debe "
                           "bloquearse, y su tipo `%s` la envía al agregado "
                           "`ioc_%s.txt`, que es una lista de bloqueo. **La fila "
                           "se contradice a sí misma.** Usar `artefacto`."
               % (corto, tipo, destino), corto)

        # ── R2 · ni datos personales ni nombres de víctima sin confirmar
        if re.search(r"\b(?:rut|r\.u\.t|cuit|cpf|dni|nif)\b[:\s]*[\d.\-]{6,}", ctx):
            ap("R2", True, "una fila parece contener un identificador fiscal de "
                           "persona física. No se reproducen ni censurados.", corto)

        # ── toda fila de indicador necesita acción permitida
        if not (fila.get("accion") or fila.get("accion_permitida") or
                fila.get("acción permitida") or
                any("acci" in str(k).lower() for k in fila)):
            ap("R6", False, "`%s` no declara acción permitida." % corto, corto)

    # ── R3 · toda cifra de ventana corta lleva su base de conteo
    if re.search(r"\b(?:últim|ultim)[oa]s?\s+(?:\d+\s+)?(?:días|dias|semanas|horas)\b",
                 inf["texto"], re.I):
        if not re.search(r"base de conteo|fecha de publicación|fecha de ataque|"
                         r"por publicación|declarad[ao]", inf["texto"], re.I):
            ap("R3", False, "usa una cifra de ventana corta sin declarar la base de "
                            "conteo. Publicación y ataque declarado divergen hasta "
                            "×8,3.")

    return H


# ─────────────────────────────────────── compuerta transversal del repositorio

def g5_agregados():
    """Los agregados planos, comprobados empíricamente y no por confianza."""
    H = []
    ap = lambda r, b, m: H.append(Hallazgo("(cartera)", "higiene", r, b, m))

    ruta = os.path.join(RAIZ, "ioc_ipv4.txt")
    if os.path.exists(ruta):
        for n, linea in enumerate(open(ruta, encoding="utf-8"), 1):
            v = linea.strip()
            if not v or v.startswith("#"):
                continue
            if RE_MASCARA.search(v) or v.upper().startswith("AS"):
                ap("R5", True, "`ioc_ipv4.txt:%d` contiene `%s`, que no es una "
                               "dirección individual." % (n, v))
                continue
            try:
                ipaddress.IPv4Address(v)
            except ValueError:
                ap("R5", True, "`ioc_ipv4.txt:%d` contiene `%s`, que no es IPv4 "
                               "válida." % (n, v))
    return H


# ────────────────────────────────────────────────────────────────── ejecución

def _modificados():
    """Los informes que el commit toca, según git.

    **Por qué es el alcance por omisión.** Auditar la cartera entera en cada
    commit produce 49 bloqueos heredados de convenciones que no existían cuando
    se escribieron los informes antiguos, y una compuerta que bloquea siempre
    se omite siempre. Juzgando sólo lo que se toca, la deuda no crece y se
    paga al pasar por cada fichero. `--todo` audita el conjunto.
    """
    import subprocess
    try:
        r = subprocess.run(["git", "diff", "--cached", "--name-only",
                            "--diff-filter=ACM"],
                           cwd=RAIZ, capture_output=True, text=True, timeout=30)
        n = [l.strip() for l in r.stdout.split("\n") if l.strip()]
        if not n:
            r = subprocess.run(["git", "diff", "--name-only", "--diff-filter=ACM"],
                               cwd=RAIZ, capture_output=True, text=True, timeout=30)
            n = [l.strip() for l in r.stdout.split("\n") if l.strip()]
        return {os.path.basename(x) for x in n
                if re.match(r"^CTI-\d{4}-\d{3}.*\.md$", os.path.basename(x))}
    except Exception:
        # `None` significa «no se pudo determinar», que NO es lo mismo que
        # «ninguno». Sin esta distinción, un fallo de git auditaba la cartera
        # entera y un commit que no toca informes también: pasó en uso real al
        # commitear sólo `.gitignore` y `tools/`, y la compuerta lo bloqueó con
        # los 36 bloqueos heredados de informes que ese commit no tocaba.
        return None


def ejecutar(patrones=None, hoy=None, todo=False):
    hoy = hoy or _dt.date.today()
    lista = B.informes()
    if patrones:
        import fnmatch
        lista = [i for i in lista
                 if any(fnmatch.fnmatch(i["md"], p) or p in i["id"] for p in patrones)]
    elif not todo:
        mod = _modificados()
        if mod is not None:
            # Conjunto vacío = el commit no toca ningún informe = nada que
            # juzgar. Auditar la cartera entera en ese caso bloquearía un
            # cambio de utillaje por deuda ajena al cambio.
            lista = [i for i in lista if i["md"] in mod]
    H = []
    for inf in lista:
        H += g1_consistencia(inf, hoy)
        H += g2_veracidad(inf, hoy)
        H += g3_atribucion(inf)
        H += g4_higiene(inf)
    H += g5_agregados()
    return lista, H


def main():
    ap = argparse.ArgumentParser(
        description="Compuerta obligatoria: consistencia, veracidad, atribución "
                    "de fuentes e higiene de indicadores.")
    ap.add_argument("patron", nargs="*", help="informes a comprobar (por omisión, todos)")
    ap.add_argument("--todo", action="store_true",
                    help="auditar la cartera completa, no sólo lo modificado")
    ap.add_argument("--avisos", action="store_true",
                    help="mostrar también los avisos que no bloquean")
    ap.add_argument("--json", action="store_true", help="salida legible por máquina")
    ap.add_argument("--hoy", help="fecha de referencia (ISO), para pruebas")
    a = ap.parse_args()

    hoy = _dt.date.fromisoformat(a.hoy) if a.hoy else _dt.date.today()
    lista, H = ejecutar(a.patron or None, hoy, a.todo)

    bloqueos = [h for h in H if h.bloquea]
    avisos = [h for h in H if not h.bloquea]

    if a.json:
        print(json.dumps({"informes": len(lista),
                          "bloqueos": [h.a_dict() for h in bloqueos],
                          "avisos": [h.a_dict() for h in avisos]},
                         ensure_ascii=False, indent=1))
        return 1 if bloqueos else 0

    if a.todo or a.patron:
        alcance = "cartera completa"
    elif not lista:
        alcance = "ningún informe modificado: nada que juzgar"
    else:
        alcance = "sólo lo modificado"
    print("cti_gate · %d informes (%s) · %d bloqueo(s) · %d aviso(s)"
          % (len(lista), alcance, len(bloqueos), len(avisos)))

    if bloqueos:
        print("\n╭─ BLOQUEA ──────────────────────────────────────────────────")
        por_inf = {}
        for h in bloqueos:
            por_inf.setdefault(h.informe, []).append(h)
        for ident in sorted(por_inf):
            print("│\n│ %s" % ident)
            for h in por_inf[ident]:
                print("│   [%s/%s] %s" % (h.compuerta, h.regla, h.mensaje))
        print("╰────────────────────────────────────────────────────────────")

    if avisos and a.avisos:
        print("\n╭─ avisos (no bloquean) ─────────────────────────────────────")
        por_inf = {}
        for h in avisos:
            por_inf.setdefault(h.informe, []).append(h)
        for ident in sorted(por_inf):
            print("│\n│ %s" % ident)
            for h in por_inf[ident]:
                print("│   [%s/%s] %s" % (h.compuerta, h.regla, h.mensaje))
        print("╰────────────────────────────────────────────────────────────")
    elif avisos:
        print("\n%d aviso(s) ocultos; `--avisos` los muestra." % len(avisos))

    if bloqueos:
        print("\nLa compuerta NO deja pasar esto. Para omitirla a sabiendas:")
        print("  CTI_GATE_OMITIR=1 git commit …")
        return 1

    print("\nTodo pasa.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
