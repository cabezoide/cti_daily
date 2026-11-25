#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vigilancia diaria del repositorio `cti_daily`: qué ha cambiado desde ayer.

`cti_build.py` construye y dice qué informe caduca. Este script hace lo otro:
**sale a las fuentes, compara con la línea base de ayer y escribe un parte con
los deltas**. No decide nada —no toca ningún informe, no propone redacción— y
eso es deliberado: la decisión de si un delta merece una versión nueva exige
juicio, y el juicio lo pone el analista o el agente que lea el parte.

Qué hace, en orden:

  1. **Inventario local.** Lee el frontmatter de los 40 informes, extrae los
     alias de cada actor y los disparadores de reevaluación que cada uno declara.
  2. **Fuentes en vivo.** Consulta las dos que esta cartera tiene verificadas:
     `ransomware.live` (extorsión) y `botnet.cl` (redes de bots y C2).
  3. **Correlación.** Empareja cada informe con el actor o la familia que le
     corresponde en esas fuentes, por alias plegado.
  4. **Deltas.** Compara contra `vigilancia/estado.json`: víctimas nuevas,
     países nuevos, víctimas REGIONALES nuevas, sitios de filtración que
     aparecen o caen, cambios de inventario de herramientas y TTP, direcciones
     de mando y control nuevas, familias nuevas, y actores que han enmudecido.
  5. **Candidatos a IOC.** Extrae los indicadores nuevos y **descuenta los que
     ya están en `ioc_index.csv`**, que es lo que convierte una lista en una
     propuesta.
  6. **Parte.** Escribe `vigilancia/parte-<fecha>.md` para leer y
     `vigilancia/parte-<fecha>.json` para automatizar, y actualiza la línea base.

Seis reglas de higiene que van CODIFICADAS aquí y no en la cabeza de nadie,
porque cada una se aprendió equivocándose (los informes que lo documentan van
citados):

  R1. **Las dos fechas.** Un registro de víctima tiene fecha de publicación y
      fecha de ataque declarada por el adversario, y las dos cuentas divergen
      hasta ×8,3. El parte da SIEMPRE las dos. (`CTI-2026-046` §O-3.1)
  R2. **Parámetros explícitos.** La consulta de ataques de `botnet.cl` sin
      `family=all` devuelve en silencio una sola familia con su histórico
      congelado. Aquí se pasa siempre. (`CTI-2026-044` §O-2.2)
  R3. **Los objetivos son víctimas.** Los prefijos y ASN atacados NO son
      indicadores y no se proponen nunca como tales, ni se escriben en una
      lista que alguien pueda cargar en un bloqueo. (`CTI-2026-044` §X-4)
  R4. **Sin nombres de víctima ni descripciones en el estado ni en el parte.**
      El estado guarda HASHES, no nombres: son reclamaciones sin confirmar, y
      las descripciones de algunos actores contienen datos personales de
      terceros. (`CTI-2026-049` Anexo D)
  R5. **Nada se da por nuevo sin comprobarlo contra el índice.** Un indicador
      ya publicado no es un hallazgo. (`CTI-2026-032`)
  R7. **El fichero anual no es el universo.** El conjunto `victims/<año>` de
      `ransomware.live` es un **subconjunto estricto** del histórico por grupo
      `groupvictims/<grupo>`: medido el 24-11-2026, 110 entradas frente a 116
      con `discovered` de 2026 para `shinyhunters`, y la misma carencia en
      nueve de dieciocho grupos muestreados. Una entrada que la fuente añade
      al histórico y no al anual **nunca** aparecería como nueva en un parte.
      Por eso los grupos que tienen informe en la cartera se completan con su
      histórico —sólo ellos, por cortesía con la fuente—. Es `G-8` de
      `CTI-2026-064`.

  R6. **El front-end y la API pueden no coincidir.** Si un grupo existe en el
      catálogo pero no tiene víctimas en el fichero anual, se marca como
      discrepancia y no como ausencia. (`CTI-2026-053` §KJ-2)

Uso:
    python3 tools/cti_vigilancia.py                  # recoge, compara, escribe el parte
    python3 tools/cti_vigilancia.py --inicializar    # crea la línea base sin reportar deltas
    python3 tools/cti_vigilancia.py --sin-red        # sólo lo local: vigencia y disparadores
    python3 tools/cti_vigilancia.py --json           # el parte por salida estándar, para encadenar
    python3 tools/cti_vigilancia.py --silencio 21    # umbral de días para declarar a un actor mudo

Sin dependencias: sólo la biblioteca estándar de Python 3.8+.
Código de salida: 0 siempre que la ejecución termine, también sin hallazgos.
Un parte vacío es un resultado, no un fallo.
"""

import argparse
import datetime as _dt
import hashlib
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cti_build as cb  # noqa: E402  — reutiliza frontmatter, informes() y el índice de IOC

RAIZ = cb.RAIZ
DIR_VIG = os.path.join(RAIZ, "vigilancia")
ESTADO = os.path.join(DIR_VIG, "estado.json")

AGENTE = "cti-vigilancia/1.0"

# ── Caché de respuestas, y no es una optimización: es una CONDICIÓN DE USO.
#
# Los términos de `ransomware.live` —§4, Fair Usage— dicen que sus datos se
# cachean treinta minutos y que **consultar con más frecuencia «may be
# considered a breach»**. Esta herramienta no cacheaba nada: dos ejecuciones
# seguidas eran dos descargas completas del catálogo del año, y nada impedía
# lanzarla cinco veces en una tarde mientras se depura.
#
# Treinta minutos es su número, no uno elegido por nosotros. `--sin-cache`
# fuerza la descarga cuando hace falta de verdad, y queda dicho en la salida.
VIDA_CACHE = 30 * 60
RUTA_CACHE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                          "vigilancia", ".cache-fuentes.json")
_CACHE = {"d": None, "sucia": False}


def _cache():
    if _CACHE["d"] is None:
        try:
            _CACHE["d"] = json.load(open(RUTA_CACHE, encoding="utf-8"))
        except Exception:
            _CACHE["d"] = {}
    return _CACHE["d"]


def _guardar_cache():
    if not _CACHE["sucia"]:
        return
    try:
        os.makedirs(os.path.dirname(RUTA_CACHE), exist_ok=True)
        json.dump(_CACHE["d"], open(RUTA_CACHE, "w", encoding="utf-8"),
                  ensure_ascii=False)
    except Exception:
        pass
TIEMPO_ESPERA = 45
PAUSA_ENTRE_FUENTES = 2      # segundos; cortesía con servicios gratuitos de terceros
PAUSA_REINTENTO = 4
PAUSA_429 = 20

# Países que esta cartera cuenta como regionales. Se mantiene explícito y no
# como «todo lo que no es EE. UU.» porque el foco del repositorio es concreto.
LATAM = {
    "AR": "Argentina", "BO": "Bolivia", "BR": "Brasil", "BZ": "Belice",
    "CL": "Chile", "CO": "Colombia", "CR": "Costa Rica", "CU": "Cuba",
    "DO": "R. Dominicana", "EC": "Ecuador", "GT": "Guatemala", "HN": "Honduras",
    "MX": "México", "NI": "Nicaragua", "PA": "Panamá", "PE": "Perú",
    "PR": "Puerto Rico", "PY": "Paraguay", "SV": "El Salvador",
    "UY": "Uruguay", "VE": "Venezuela",
}
# Los que el repositorio prioriza. Un hallazgo aquí sube de nivel en el parte.
PRIORITARIOS = {"CL", "BR", "AR", "MX", "CO", "PE"}

FUENTES = {
    "rwlive_victimas": "https://api.ransomware.live/v2/victims/%(anio)d",
    "rwlive_grupos": "https://api.ransomware.live/v2/groups",
    # R2: `family=all` explícito, siempre.
    "botnetcl_c2": "https://botnet.cl/api/v1/c2",
    "botnetcl_ataques": "https://botnet.cl/api/v1/attacks?family=all&limit=100",
    "botnetcl_bgp": "https://botnet.cl/api/v1/bgp/leaderboard",
}

# R7 · el histórico por grupo. Va FUERA de `FUENTES` a propósito: `recoger()`
# formatea esa tabla entera con `%(anio)s` y una plantilla con otra clave la
# rompe —ocurrió al escribirlo—. Se consulta aparte y sólo para los grupos
# correlacionados con un informe.
FUENTE_HISTORICO = "https://api.ransomware.live/v2/groupvictims/%(grupo)s"


# ───────────────────────────────────────────────────────────── utilidades

def aviso(*args, **kw):
    """Progreso y avisos van a `stderr`.

    `stdout` queda reservado para el JSON de `--json`: mezclarlos rompería
    cualquier encadenamiento, y de hecho lo rompió al probarlo.
    """
    kw.setdefault("file", sys.stderr)
    print(*args, **kw)


def plegar(s):
    """Minúsculas sin diacríticos ni separadores, para emparejar alias.

    «The Gentlemen», «thegentlemen» y «TheGentlemen» tienen que casar, porque
    las tres grafías aparecen en las fuentes y en los informes.
    """
    s = unicodedata.normalize("NFD", s or "")
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]", "", s.lower())


def clave(*partes):
    """Hash corto y estable de una víctima.

    R4: la línea base NO guarda nombres de víctima. Guarda esto.
    """
    crudo = "\x1f".join(str(p or "") for p in partes)
    return hashlib.sha256(crudo.encode("utf-8")).hexdigest()[:16]


def traer(url, etiqueta, reintentos=2, usar_cache=True):
    """Descarga y decodifica JSON. Devuelve (datos, error).

    Reintenta con espera creciente ante fallos transitorios, y **respeta el
    `Retry-After` de un 429**. Las fuentes de esta cartera son servicios
    gratuitos de terceros: insistir sin pausa es la forma más rápida de que
    dejen de responder, y de hecho ocurrió al probar este script.
    """
    c = _cache()
    guardado = c.get(url)
    if usar_cache and guardado and time.time() - guardado.get("t", 0) < VIDA_CACHE:
        edad = int((time.time() - guardado["t"]) / 60)
        aviso("  %s: de la caché (%d min; se refresca a los %d)"
              % (etiqueta, edad, VIDA_CACHE // 60))
        return guardado.get("d"), None

    pet = urllib.request.Request(url, headers={
        "User-Agent": AGENTE,
        "Accept": "application/json",
    })
    ultimo = None
    for intento in range(reintentos + 1):
        try:
            with urllib.request.urlopen(pet, timeout=TIEMPO_ESPERA) as r:
                crudo = r.read()
            try:
                d = json.loads(crudo.decode("utf-8", "replace"))
                c[url] = {"t": time.time(), "d": d}
                _CACHE["sucia"] = True
                return d, None
            except ValueError as ex:
                return None, "%s: respuesta no es JSON (%d B): %s" % (
                    etiqueta, len(crudo), ex)
        except urllib.error.HTTPError as ex:
            ultimo = "%s: HTTP %s %s" % (etiqueta, ex.code, ex.reason)
            if ex.code == 429:
                espera = 0
                try:
                    espera = int(ex.headers.get("Retry-After") or 0)
                except (TypeError, ValueError):
                    espera = 0
                espera = min(max(espera, PAUSA_429 * (intento + 1)), 180)
                ultimo += " — limitado por tasa; esperando %ds" % espera
                if intento < reintentos:
                    time.sleep(espera)
                    continue
            if 400 <= ex.code < 500 and ex.code != 429:
                return None, ultimo          # un 404 no mejora reintentando
        except (urllib.error.URLError, OSError) as ex:
            ultimo = "%s: %s" % (etiqueta, ex)
        if intento < reintentos:
            time.sleep(PAUSA_REINTENTO * (intento + 1))
    return None, ultimo


def dia(s):
    """Primeros diez caracteres de una marca ISO, o cadena vacía."""
    return (s or "")[:10]


# ───────────────────────────────────────────────── inventario de informes

ALIAS_RUIDO = {
    "raas", "linaje", "discutido", "designacion", "de", "y", "marca", "hermana",
    "ransom", "group", "grupo", "framework", "ofensivo", "agentico", "familias",
    "ecosistema", "abuso", "dominios", "primer", "nivel", "troyanos", "bancarios",
    "brasilenos", "campanas", "cargador", "redes", "bots", "ddos", "proxy",
    "residencial", "operation", "sin", "atribuir", "familia", "red", "denegacion",
    "servicio", "mas", "activa", "las", "en", "seguimiento",
}


def alias_de(fm):
    """Extrae los alias emparejables del campo `actor` del frontmatter.

    El campo es una lista separada por `·` con algún paréntesis ocasional. Se
    descartan los fragmentos que son prosa y no nombres —la lista `ALIAS_RUIDO`—
    porque un alias como «de» casaría con cualquier cosa.
    """
    crudo = fm.get("actor", "") or ""
    trozos = re.split(r"[·,]", crudo)
    salida = []
    for t in trozos:
        t = re.sub(r"\((.*?)\)", r" \1 ", t)
        t = re.sub(r"[*`]", "", t).strip(" —-")
        for pieza in re.split(r"\s+/\s+|\s+·\s+", t):
            p = plegar(pieza)
            if len(p) >= 3 and p not in ALIAS_RUIDO:
                salida.append((pieza.strip(), p))
    vistos, unicos = set(), []
    for orig, pl in salida:
        if pl not in vistos:
            vistos.add(pl)
            unicos.append((orig, pl))
    return unicos


def disparadores_de(texto):
    """Devuelve los disparadores de reevaluación `I-n` que el informe declara.

    No se interpretan: se transcriben para que el parte los tenga delante. Un
    disparador que nadie recuerda no dispara nada.
    """
    m = re.search(r"\*\*Disparadores de reevaluaci[oó]n\.?\*\*(.{0,2600}?)(?:\n\n|\n---)",
                  texto, re.S)
    if not m:
        return []
    cuerpo = re.sub(r"\s+", " ", m.group(1))
    trozos = re.findall(r"`?(I-\d+[a-z]?)`?\s*:?\s*(.*?)(?=`?I-\d+[a-z]?`?\s*:|$)", cuerpo)
    return [{"id": i, "texto": t.strip(" .·—-")[:320]} for i, t in trozos if t.strip()]


def inventario(hoy):
    """Inventario local: un registro por informe publicable."""
    salida = []
    for inf in cb.informes():
        fm = inf["fm"]
        estado, dias = cb.vigencia(fm, hoy)
        salida.append({
            "id": inf["id"],
            "md": inf["md"],
            "actor": fm.get("actor", ""),
            "tipo": fm.get("tipo", ""),
            "version": fm.get("version", ""),
            "actualizado": inf["actualizado"],
            "vigencia": estado,
            "dias": dias,
            "alias": alias_de(fm),
            "disparadores": disparadores_de(inf["texto"]),
            "publicable": inf["publicable"],
        })
    return salida


def indicadores_publicados():
    """Conjunto plegado de todo valor que ya está en `ioc_index.csv`.

    R5: es lo que permite decir «nuevo» con fundamento.
    """
    ruta = os.path.join(RAIZ, cb.FICHERO_INDICE)
    if not os.path.exists(ruta):
        return set()
    import csv
    vistos = set()
    with open(ruta, newline="", encoding="utf-8") as fh:
        for fila in csv.DictReader(fh):
            v = (fila.get("valor") or fila.get("indicador") or "").strip()
            if v:
                vistos.add(plegar(v))
    return vistos


# ─────────────────────────────────────────────────────────── recolección

def recoger(anio, errores, usar_cache=True):
    """Consulta las fuentes en vivo.

    Devuelve `(datos, ok)`, donde `ok` dice **por fuente** si respondió. Esa
    distinción es la que impide confundir «no hay cambios» con «no hubo
    colección», y la que protege la línea base (ver `main`).
    """
    datos, ok = {}, {}
    pedidas = 0
    for nombre, patron in FUENTES.items():
        if pedidas:
            time.sleep(PAUSA_ENTRE_FUENTES)
        url = patron % {"anio": anio} if "%(" in patron else patron
        d, err = traer(url, nombre, usar_cache=usar_cache)
        if err:
            errores.append(err)
        datos[nombre] = d
        ok[nombre] = err is None and d is not None
        pedidas += 1
    _guardar_cache()
    return datos, ok


def correlacionar(inv, grupos_rwlive, familias_botnet):
    """Empareja cada informe con el actor de cada fuente, por alias plegado.

    Devuelve dos mapas: id de informe → nombre en la fuente. Un informe puede
    no casar con nada, y eso es normal: la mitad de la cartera son actores
    estatales que no publican en sitios de filtración.
    """
    por_rw, por_bn = {}, {}
    idx_rw = {plegar(g): g for g in grupos_rwlive}
    idx_bn = {plegar(f): f for f in familias_botnet}
    for r in inv:
        for orig, pl in r["alias"]:
            if pl in idx_rw and r["id"] not in por_rw:
                por_rw[r["id"]] = idx_rw[pl]
            if pl in idx_bn and r["id"] not in por_bn:
                por_bn[r["id"]] = idx_bn[pl]
    return por_rw, por_bn


def resumir_victimas(registros):
    """Comprime la lista de víctimas de un actor a lo que el estado necesita.

    R4: claves hash, no nombres. R1: las dos fechas, por separado.
    """
    claves, paises, sectores = set(), {}, {}
    por_publicacion, por_ataque = {}, {}
    for v in registros:
        claves.add(clave(v.get("group"), v.get("victim"), dia(v.get("discovered"))))
        c = (v.get("country") or "??").upper()
        paises[c] = paises.get(c, 0) + 1
        a = v.get("activity") or "—"
        sectores[a] = sectores.get(a, 0) + 1
        dp, da = dia(v.get("discovered")), dia(v.get("attackdate"))
        if dp:
            por_publicacion[dp] = por_publicacion.get(dp, 0) + 1
        if da:
            por_ataque[da] = por_ataque.get(da, 0) + 1
    return {
        "total": len(registros),
        "claves": sorted(claves),
        "paises": paises,
        "sectores": sectores,
        "por_publicacion": por_publicacion,
        "por_ataque": por_ataque,
    }


def completar_con_historico(por_grupo, nombres, anio, errores, usar_cache=True):
    """Completa `por_grupo` con lo que el fichero anual no trae (R7).

    El conjunto anual de `ransomware.live` es un subconjunto estricto del
    histórico por grupo —`G-8` de `CTI-2026-064`—, y la consecuencia no es
    cosmética: **una entrada que sólo está en el histórico no aparece como
    nueva en ningún parte, nunca**, porque el delta diario compara contra un
    universo que no la contiene.

    Se consulta sólo para los grupos que casan con un informe de la cartera,
    con pausa entre peticiones: son del orden de veinte, no de doscientos.
    """
    resultado = []
    for i, nombre in enumerate([n for n in nombres if n]):
        if i:
            time.sleep(PAUSA_ENTRE_FUENTES)
        url = FUENTE_HISTORICO % {"grupo": urllib.parse.quote(nombre, safe="")}
        d, err = traer(url, "histórico de «%s»" % nombre, usar_cache=usar_cache)
        if err:
            errores.append(err)
            continue
        if not isinstance(d, list):
            errores.append("histórico de «%s»: la respuesta no es una lista" % nombre)
            continue
        ya = {clave(v.get("group"), v.get("victim"), dia(v.get("discovered")))
              for v in (por_grupo.get(nombre) or [])}
        nuevas = []
        for v in d:
            if str(v.get("discovered") or "")[:4] != str(anio):
                continue
            v.setdefault("group", nombre)
            if clave(v.get("group"), v.get("victim"), dia(v.get("discovered"))) in ya:
                continue
            # Marca de procedencia. Sin ella, las entradas recuperadas se
            # cuentan como «víctimas nuevas de hoy» y el parte publica un
            # salto que no ocurrió: la primera ejecución con R7 recuperó 90
            # entradas y el recuento del día pasó de 1 a 91. Son relleno de
            # catálogo con fecha de ataque de 2025, no actividad de la jornada.
            v["_procedencia"] = "historico"
            nuevas.append(v)
        if nuevas:
            por_grupo.setdefault(nombre, []).extend(nuevas)
            resultado.append({"grupo": nombre, "anadidas": len(nuevas),
                              "historico": len(d)})
            aviso("  histórico de «%s»: %d entrada(s) del año en curso que el "
                  "fichero anual no traía" % (nombre, len(nuevas)))
    return resultado


# ────────────────────────────────────────────────────────────────── deltas

def delta_actor(idi, nombre, nuevo, viejo, registros_nuevos):
    """Compara el estado de un actor con el de la línea base.

    Devuelve un dict de hallazgos, o None si no hay ninguno. Las víctimas
    nuevas se identifican por clave hash; de ellas sólo se extrae país,
    sector y las dos fechas (R1, R4).
    """
    viejo = viejo or {}
    previas = set(viejo.get("claves", []))
    actuales = set(nuevo["claves"])
    nuevas = actuales - previas
    primera_vez = not previas

    h = {
        "informe": idi, "fuente_nombre": nombre, "primera_vez": primera_vez,
        "total_antes": viejo.get("total", 0), "total_ahora": nuevo["total"],
        "victimas_nuevas": len(nuevas),
        "paises_nuevos": sorted(set(nuevo["paises"]) - set(viejo.get("paises", {}))),
        "detalle_nuevas": [], "regionales_nuevas": [],
    }

    if nuevas:
        for v in registros_nuevos:
            k = clave(v.get("group"), v.get("victim"), dia(v.get("discovered")))
            if k not in nuevas:
                continue
            pais = (v.get("country") or "??").upper()
            reg = {
                "pais": pais,
                "sector": v.get("activity") or "—",
                "publicada": dia(v.get("discovered")),
                "ataque_declarado": dia(v.get("attackdate")),
                "tiene_dominio": bool(v.get("domain")),
                "tiene_prensa": bool(v.get("press")),
                "recuperada": v.get("_procedencia") == "historico",
                # R4: ni nombre ni descripción.
            }
            h["detalle_nuevas"].append(reg)
            if pais in LATAM:
                reg2 = dict(reg)
                reg2["pais_nombre"] = LATAM[pais]
                reg2["prioritario"] = pais in PRIORITARIOS
                h["regionales_nuevas"].append(reg2)

    # R1: el reparto de las dos fechas sobre lo nuevo, que es lo que permite
    # distinguir una tanda de un ritmo.
    h["recuperadas"] = sum(1 for r in h["detalle_nuevas"] if r.get("recuperada"))
    h["nuevas_de_hoy"] = h["victimas_nuevas"] - h["recuperadas"]

    if h["detalle_nuevas"]:
        pub = {}
        for r in h["detalle_nuevas"]:
            if r["publicada"]:
                pub[r["publicada"]] = pub.get(r["publicada"], 0) + 1
        h["tanda"] = max(pub.values()) if pub else 0
        h["dias_de_publicacion"] = len(pub)
        h["con_fecha_de_ataque_distinta"] = sum(
            1 for r in h["detalle_nuevas"]
            if r["ataque_declarado"] and r["ataque_declarado"] != r["publicada"])

    hay = (nuevas or h["paises_nuevos"] or primera_vez)
    return h if hay else None


def delta_catalogo(idi, nombre, g_nuevo, g_viejo):
    """Compara la ficha de catálogo de un grupo: sitios, herramientas, TTP."""
    g_viejo = g_viejo or {}
    def sitios(g):
        return {l.get("fqdn") or l.get("slug") or "?":
                bool(l.get("available")) for l in (g.get("locations") or [])}
    sn, sv = sitios(g_nuevo), sitios(g_viejo)
    def herramientas(g):
        out = set()
        for bloque in (g.get("tools") or []):
            if isinstance(bloque, dict):
                for cat, lista in bloque.items():
                    for h in (lista or []):
                        out.add("%s/%s" % (cat, h))
        return out
    hn, hv = herramientas(g_nuevo), herramientas(g_viejo)
    def tecnicas(g):
        n = 0
        for t in (g.get("ttps") or []):
            n += len(t.get("techniques") or [])
        return n
    tn, tv = tecnicas(g_nuevo), tecnicas(g_viejo)

    h = {
        "informe": idi, "fuente_nombre": nombre,
        "sitios_nuevos": sorted(set(sn) - set(sv)),
        "sitios_caidos": sorted(k for k in sn if k in sv and sv[k] and not sn[k]),
        "sitios_revividos": sorted(k for k in sn if k in sv and not sv[k] and sn[k]),
        "herramientas_nuevas": sorted(hn - hv),
        "herramientas_retiradas": sorted(hv - hn),
        "tecnicas_antes": tv, "tecnicas_ahora": tn,
        "descripcion_nueva": bool((g_nuevo.get("description") or "").strip()
                                  and not (g_viejo.get("description") or "").strip()),
    }
    hay = any([h["sitios_nuevos"], h["sitios_caidos"], h["sitios_revividos"],
               h["herramientas_nuevas"], h["herramientas_retiradas"],
               tn != tv, h["descripcion_nueva"]])
    return h if hay else None


def delta_c2(c2_nuevo, c2_viejo, ya_publicados):
    """Direcciones de mando y control nuevas, descontando las ya publicadas.

    R5: sólo es «nuevo» lo que no está en `ioc_index.csv`.
    R3: aquí sólo entran direcciones de C2. Los prefijos objetivo no se
    recogen ni se proponen: son víctimas.
    """
    previas = set(c2_viejo or [])
    entradas = {e["ip"]: e for e in (c2_nuevo or []) if e.get("ip")}
    nuevas = sorted(set(entradas) - previas)
    desaparecidas = sorted(previas - set(entradas))
    candidatos = []
    for ip in nuevas:
        e = entradas[ip]
        candidatos.append({
            "valor": ip,
            "tipo": "ipv4",
            "asn": e.get("asn"),
            "asn_nombre": e.get("asn_name"),
            "pais": (e.get("country_code") or "??").upper(),
            "primera_vez": dia(e.get("first_seen")),
            "ya_en_el_indice": plegar(ip) in ya_publicados,
        })
    return {
        "total_ahora": len(entradas),
        "total_antes": len(previas),
        "nuevas": candidatos,
        "desaparecidas": desaparecidas,
        "candidatos_a_ioc": [c for c in candidatos if not c["ya_en_el_indice"]],
        "regionales": [c for c in candidatos if c["pais"] in LATAM],
    }


# ─────────────────────────────────────────────────────────────── el parte

def _lineas_urgente(p):
    """Lo que exige mirar hoy. Si esta sección sale vacía, el día está tranquilo."""
    L = []
    reg = [(h, r) for h in p["actores"] for r in h.get("regionales_nuevas", [])]
    prio = [(h, r) for h, r in reg if r.get("prioritario")]
    if prio:
        L.append("### ⚠ Víctimas nuevas en países prioritarios\n")
        L.append("| Informe | Actor en la fuente | País | Sector | Publicada | Ataque declarado | ¿Dominio? | Procedencia |")
        L.append("|---|---|---|---|---|---|---|---|")
        for h, r in prio:
            L.append("| `%s` | %s | **%s** | %s | %s | %s | %s | %s |" % (
                h["informe"], h["fuente_nombre"], r["pais_nombre"], r["sector"],
                r["publicada"] or "—", r["ataque_declarado"] or "—",
                "sí" if r["tiene_dominio"] else "**no**",
                "**histórico** (R7)" if r.get("recuperada") else "anual"))
        L.append("")
        L.append("> **Qué hacer con esto.** Son **reclamaciones de sitio de "
                 "filtración, no brechas verificadas**. Antes de escribirlas en "
                 "un informe hay que comprobar si la organización lo ha "
                 "confirmado, y si la entrada trae dominio —si no lo trae, no "
                 "es verificable por un tercero—.\n")
    otras = [(h, r) for h, r in reg if not r.get("prioritario")]
    if otras:
        L.append("### Víctimas nuevas en el resto de la región\n")
        for h, r in otras:
            L.append("- `%s` (%s): **%s**, %s, publicada %s" % (
                h["informe"], h["fuente_nombre"], r["pais_nombre"], r["sector"],
                r["publicada"] or "—"))
        L.append("")
    cand = p["c2"].get("candidatos_a_ioc") or []
    if cand:
        L.append("### ⚠ Candidatos a indicador que NO están en el índice\n")
        L.append("| Valor | Tipo | ASN | Proveedor | País | Primera observación |")
        L.append("|---|---|---|---|---|---|")
        for c in cand[:60]:
            L.append("| `%s` | %s | AS%s | %s | %s | %s |" % (
                c["valor"], c["tipo"], c["asn"], (c["asn_nombre"] or "?")[:34],
                c["pais"], c["primera_vez"] or "—"))
        if len(cand) > 60:
            L.append("")
            L.append("*(y %d más; están completos en el JSON)*" % (len(cand) - 60))
        L.append("")
        L.append("> **Antes de ingerir.** Son direcciones de **mando y "
                 "control** de la fuente, no objetivos. Cada una necesita su "
                 "tipo, su confianza, su caducidad y su acción permitida "
                 "escritas por quien la analice: el índice no acepta una "
                 "dirección sin contexto, y con razón.\n")
    ch = p.get("completado_historico") or []
    if ch:
        L.append("### Entradas recuperadas del histórico por grupo (R7)\n")
        L.append("> El fichero anual de la fuente es un **subconjunto "
                 "estricto** de su histórico por grupo (`G-8` de "
                 "`CTI-2026-064`). Estas entradas **no habrían aparecido "
                 "nunca** en un parte sin consultar el histórico, y ya van "
                 "incluidas en los deltas de arriba.\n")
        L.append("| Grupo | Entradas del año recuperadas | Histórico total |")
        L.append("|---|---|---|")
        for x in sorted(ch, key=lambda y: -y["anadidas"]):
            L.append("| `%s` | **%d** | %d |" % (x["grupo"], x["anadidas"], x["historico"]))
        L.append("")

    cad = [r for r in p["inventario"] if r["vigencia"] == "caducado"]
    if cad:
        L.append("### ⚠ Informes caducados\n")
        for r in cad:
            L.append("- `%s` — %s · caducado hace **%d días** · v%s" % (
                r["id"], r["actor"][:56], abs(r["dias"] or 0), r["version"]))
        L.append("")
    return L


def escribir_parte(p, ruta_md):
    """Escribe el parte legible. El orden es el de la urgencia, no el del dato."""
    f = p["fecha"]
    L = ["# Parte de vigilancia — %s" % f, ""]
    L.append("> Generado por `tools/cti_vigilancia.py`. **Este parte no decide "
             "nada**: recoge deltas y los pone delante. Si un delta merece una "
             "versión nueva de un informe lo decide quien lo lea.")
    L.append("")

    if p.get("parcial"):
        caidas = [k for k, v in (p.get("fuentes") or {}).items() if not v]
        L.append("> ## ⚠ COLECCIÓN PARCIAL")
        L.append("> ")
        L.append("> **No respondieron: %s.** Todo lo que este parte diga sobre "
                 "esas fuentes es «no se pudo mirar», **no «no hay cambios»**. "
                 "La línea base de las secciones afectadas se ha conservado sin "
                 "tocar, de modo que el delta de mañana seguirá siendo correcto."
                 % ", ".join("`%s`" % c for c in caidas))
        L.append("")
    if p.get("base_no_actualizada"):
        L.append("> ## ⚠ LÍNEA BASE NO ACTUALIZADA")
        L.append("> ")
        L.append("> El estado nuevo era **más pequeño** que el anterior sin "
                 "motivo declarado, así que **no se ha escrito**: se conserva el "
                 "de la ejecución previa. Un estado que encoge sin explicación "
                 "produce cientos de falsos positivos al día siguiente. Si el "
                 "encogimiento es legítimo, reinicialice con `--inicializar`.")
        L.append("")

    tot_reg = sum(len(h.get("regionales_nuevas", [])) for h in p["actores"])
    tot_vic = sum(h.get("victimas_nuevas", 0) for h in p["actores"])
    L.append("## Resumen de la jornada")
    L.append("")
    L.append("| Métrica | Valor |")
    L.append("|---|---|")
    L.append("| Informes en cartera | %d |" % len(p["inventario"]))
    if p.get("fuentes"):
        L.append("| Fuentes que respondieron | %d de %d |" % (
            sum(1 for v in p["fuentes"].values() if v), len(p["fuentes"])))
    L.append("| Informes correlacionados con una fuente viva | %d |" % p["correlacionados"])
    tot_rec = sum(h.get("recuperadas", 0) for h in p["actores"])
    L.append("| **Víctimas nuevas observadas** | **%d** |" % tot_vic)
    if tot_rec:
        L.append("| de ellas, **recuperadas del histórico** (R7; **no son "
                 "actividad de hoy**) | **%d** |" % tot_rec)
        L.append("| **Víctimas nuevas de la jornada** | **%d** |" % (tot_vic - tot_rec))
    L.append("| **Víctimas nuevas en la región** | **%d** |" % tot_reg)
    L.append("| **Candidatos a indicador nuevos** | **%d** |" % len(p["c2"].get("candidatos_a_ioc") or []))
    L.append("| Direcciones de C2 en la fuente | %d (antes %d) |" % (
        p["c2"].get("total_ahora", 0), p["c2"].get("total_antes", 0)))
    L.append("| Cambios de catálogo (sitios, herramientas, TTP) | %d |" % len(p["catalogo"]))
    ch = p.get("completado_historico") or []
    if ch:
        L.append("| **Entradas que el fichero anual no traía** (R7) | **%d en %d grupo(s)** |"
                 % (sum(x["anadidas"] for x in ch), len(ch)))
    L.append("| Actores nuevos sin informe | %d |" % len(p["actores_sin_informe"]))
    L.append("| Informes caducados | %d |" % sum(
        1 for r in p["inventario"] if r["vigencia"] == "caducado"))
    L.append("| Informes que caducan en 14 días | %d |" % sum(
        1 for r in p["inventario"]
        if r["vigencia"] == "vigente" and (r["dias"] or 999) <= 14))
    L.append("")

    urg = _lineas_urgente(p)
    if urg:
        L.append("## Lo que exige mirar hoy")
        L.append("")
        L += urg
    else:
        L.append("## Lo que exige mirar hoy")
        L.append("")
        L.append("**Nada.** Ni víctimas regionales nuevas, ni candidatos a "
                 "indicador fuera del índice, ni informes caducados. "
                 "**Un parte vacío es un resultado**, y conviene registrarlo "
                 "igual: la ausencia de cambio también es inteligencia.")
        L.append("")

    if p["actores"]:
        L.append("## Deltas por informe")
        L.append("")
        for h in sorted(p["actores"], key=lambda x: -x.get("victimas_nuevas", 0)):
            L.append("### `%s` ↔ %s" % (h["informe"], h["fuente_nombre"]))
            L.append("")
            if h["primera_vez"]:
                L.append("**Primera observación de este actor en la línea "
                         "base.** No hay delta: lo que sigue es su estado "
                         "actual, y mañana sí habrá comparación.")
                L.append("")
            L.append("| Medida | Valor |")
            L.append("|---|---|")
            L.append("| Víctimas acumuladas | %d (antes %d) |" % (
                h["total_ahora"], h["total_antes"]))
            L.append("| **Víctimas nuevas** | **%d** |" % h["victimas_nuevas"])
            if h.get("regionales_nuevas"):
                L.append("| **De ellas, regionales** | **%d** |" % len(h["regionales_nuevas"]))
            if h.get("tanda"):
                L.append("| Mayor tanda en un día | %d |" % h["tanda"])
                L.append("| Días distintos de publicación | %d |" % h.get("dias_de_publicacion", 0))
                L.append("| Con fecha de ataque **distinta** de la de publicación | %d de %d |" % (
                    h.get("con_fecha_de_ataque_distinta", 0), h["victimas_nuevas"]))
            if h["paises_nuevos"]:
                L.append("| Países nuevos alcanzados | %s |" % ", ".join(h["paises_nuevos"]))
            L.append("")
            if h.get("tanda", 0) >= 10:
                L.append("> **Atención a la tanda.** %d entradas en un solo día. "
                         "Recuerde la regla R1: contado por fecha de "
                         "publicación este actor parecerá mucho más activo que "
                         "contado por fecha de ataque declarada, y las dos "
                         "cuentas son correctas. **No cite una sin decir cuál "
                         "es.**\n" % h["tanda"])

    if p["catalogo"]:
        L.append("## Cambios de catálogo")
        L.append("")
        for c in p["catalogo"]:
            L.append("### `%s` ↔ %s" % (c["informe"], c["fuente_nombre"]))
            L.append("")
            if c["sitios_nuevos"]:
                L.append("- **Sitios de filtración nuevos:** %s" % ", ".join(
                    "`%s`" % s for s in c["sitios_nuevos"]))
            if c["sitios_caidos"]:
                L.append("- **Sitios que han caído:** %s" % ", ".join(
                    "`%s`" % s for s in c["sitios_caidos"]))
            if c["sitios_revividos"]:
                L.append("- **Sitios que han vuelto:** %s" % ", ".join(
                    "`%s`" % s for s in c["sitios_revividos"]))
            if c["herramientas_nuevas"]:
                L.append("- **Herramientas nuevas en su inventario:** %s" % ", ".join(
                    "`%s`" % h for h in c["herramientas_nuevas"]))
                L.append("  - *Recuerde: casi todas las herramientas de estos "
                         "inventarios son legítimas. Van al Anexo A con tipo "
                         "`herramienta` y **no entran en los agregados "
                         "planos**.*")
            if c["herramientas_retiradas"]:
                L.append("- Herramientas que ya no figuran: %s" % ", ".join(
                    "`%s`" % h for h in c["herramientas_retiradas"]))
            if c["tecnicas_ahora"] != c["tecnicas_antes"]:
                L.append("- **Técnicas documentadas:** %d → **%d**" % (
                    c["tecnicas_antes"], c["tecnicas_ahora"]))
            if c["descripcion_nueva"]:
                L.append("- **La fuente ha publicado una descripción** donde "
                         "antes no había: material nuevo que leer.")
            L.append("")

    if p["actores_sin_informe"]:
        L.append("## Actores de las fuentes que no tienen informe")
        L.append("")
        L.append("> **No todos merecen uno.** Antes de abrir expediente, el "
                 "triaje del `Anexo D` de `CTI-2026-042` resuelve la mayoría "
                 "en minutos, y el criterio más barato es **cómo contacta la "
                 "víctima**: portal es operación, correo es herramienta.")
        L.append("")
        L.append("| Nombre en la fuente | Alta | Sitios | Técnicas | ¿Descripción? |")
        L.append("|---|---|---|---|---|")
        for a in p["actores_sin_informe"][:40]:
            L.append("| %s | %s | %d | %d | %s |" % (
                a["nombre"], a.get("alta") or "—", a.get("sitios", 0),
                a.get("tecnicas", 0), "sí" if a.get("descripcion") else "**no**"))
        if len(p["actores_sin_informe"]) > 40:
            L.append("")
            L.append("*(y %d más en el JSON)*" % (len(p["actores_sin_informe"]) - 40))
        L.append("")

    prox = [r for r in p["inventario"]
            if r["vigencia"] in ("vigente", "por caducar") and (r["dias"] or 999) <= 14]
    if prox:
        L.append("## Informes que caducan en catorce días o menos")
        L.append("")
        for r in sorted(prox, key=lambda x: x["dias"] or 0):
            L.append("- `%s` — %s · **%d días** · v%s" % (
                r["id"], r["actor"][:56], r["dias"] or 0, r["version"]))
        L.append("")

    disp = [r for r in p["inventario"] if r["disparadores"]]
    if disp:
        L.append("## Disparadores de reevaluación declarados")
        L.append("")
        L.append("> Los informes los escribieron para que alguien los "
                 "comprobara. Esta sección los pone delante; **comprobarlos es "
                 "trabajo de análisis y no de script**.")
        L.append("")
        for r in disp:
            L.append("<details><summary><code>%s</code> — %s (%d disparadores)</summary>\n" % (
                r["id"], r["actor"][:54], len(r["disparadores"])))
            for d in r["disparadores"]:
                L.append("- **`%s`** · %s" % (d["id"], d["texto"]))
            L.append("\n</details>\n")

    if p["errores"] or p["discrepancias"]:
        L.append("## Problemas de colección de esta ejecución")
        L.append("")
        for e in p["errores"]:
            L.append("- ⚠ **Fuente no disponible:** %s" % e)
        for d in p["discrepancias"]:
            L.append("- ⚠ **Discrepancia dentro de una fuente:** %s" % d)
        L.append("")
        L.append("> **Una fuente caída no es un día sin hallazgos: es un día "
                 "sin colección.** No se debe interpretar la ausencia de "
                 "deltas como ausencia de cambios si esta sección no está "
                 "vacía. (R6)")
        L.append("")

    L.append("---")
    L.append("")
    L.append("*Línea base actualizada en `vigilancia/estado.json`. Datos "
             "completos en `vigilancia/parte-%s.json`.*" % f)
    with open(ruta_md, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")


# ─────────────────────────────────────────────────────────────────── main

def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Vigilancia diaria: qué ha cambiado en las fuentes desde la última ejecución.")
    ap.add_argument("--inicializar", action="store_true",
                    help="crea la línea base sin reportar deltas (primera ejecución)")
    ap.add_argument("--sin-cache", action="store_true",
                    help="ignora la caché de 30 min y vuelve a descargar. "
                         "Los términos de ransomware.live consideran posible "
                         "incumplimiento consultar más a menudo: usar sólo "
                         "cuando haga falta de verdad")
    ap.add_argument("--sin-red", action="store_true",
                    help="sólo inventario local: vigencia y disparadores")
    ap.add_argument("--json", action="store_true",
                    help="volcar el parte por salida estándar")
    ap.add_argument("--silencio", type=int, default=21, metavar="DÍAS",
                    help="días sin víctimas nuevas para declarar a un actor mudo (por omisión 21)")
    ap.add_argument("--anio", type=int, default=None,
                    help="año del fichero de víctimas a consultar (por omisión, el actual)")
    a = ap.parse_args(argv)

    hoy = _dt.date.today()
    anio = a.anio or hoy.year
    os.makedirs(DIR_VIG, exist_ok=True)

    errores, discrepancias = [], []
    inv = inventario(hoy)

    parte = {
        "fecha": hoy.isoformat(),
        "generado": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        "anio_consultado": anio,
        "inventario": inv,
        "correlacionados": 0,
        "actores": [], "catalogo": [], "actores_sin_informe": [],
        "c2": {}, "errores": errores, "discrepancias": discrepancias,
        "mudos": [],
    }

    if a.sin_red:
        parte["c2"] = {"total_ahora": 0, "total_antes": 0, "candidatos_a_ioc": []}
        ruta_md = os.path.join(DIR_VIG, "parte-%s.md" % hoy.isoformat())
        escribir_parte(parte, ruta_md)
        aviso("sin red: parte local escrito en %s" % os.path.relpath(ruta_md, RAIZ))
        if a.json:
            json.dump(parte, sys.stdout, ensure_ascii=False, indent=1)
        return 0

    # ── línea base
    base = {}
    if os.path.exists(ESTADO) and not a.inicializar:
        try:
            base = json.load(open(ESTADO, encoding="utf-8"))
        except ValueError as ex:
            errores.append("línea base ilegible, se recrea: %s" % ex)
            base = {}
    primera = not base

    # ── recolección
    datos, fuente_ok = recoger(anio, errores, usar_cache=not a.sin_cache)
    parte["fuentes"] = fuente_ok
    parte["parcial"] = not all(fuente_ok.values())
    victimas = datos.get("rwlive_victimas") or []
    grupos = datos.get("rwlive_grupos") or []
    c2 = datos.get("botnetcl_c2") or {}
    entradas_c2 = (c2.get("entries") if isinstance(c2, dict) else None) or []
    ataques = datos.get("botnetcl_ataques") or {}
    eventos = (ataques.get("events") if isinstance(ataques, dict) else None) or []
    bgp = datos.get("botnetcl_bgp") or {}

    # ── índices de las fuentes
    por_grupo = {}
    for v in victimas:
        por_grupo.setdefault((v.get("group") or "").strip(), []).append(v)
    fichas = {}
    for g in grupos:
        n = (g.get("name") or "").strip()
        if n:
            fichas[n] = g
    # Las familias de redes de bots salen de los eventos de ataque: es la única
    # vista de esa fuente que las enumera con nombre.
    familias = sorted({(e.get("family") or "").strip() for e in eventos if e.get("family")})

    # R6: un grupo en el catálogo sin víctimas en el fichero anual es una
    # discrepancia dentro de la fuente, no una ausencia del mundo. Sólo se
    # señala para los de alta reciente, porque en los antiguos la ausencia de
    # víctimas en el año en curso es simplemente inactividad.
    nombres_victimas = {plegar(k) for k in por_grupo}
    for n, g in fichas.items():
        alta = g.get("added_date") or ""
        if plegar(n) not in nombres_victimas and alta and alta >= (
                hoy - _dt.timedelta(days=45)).isoformat():
            discrepancias.append(
                "«%s» figura en el catálogo (alta %s) y no tiene víctimas en el "
                "fichero anual: puede ser retraso de ingesta y no ausencia (R6)" % (n, alta))

    # ── correlación informe ↔ fuente
    por_rw, por_bn = correlacionar(inv, list(por_grupo) + list(fichas), familias)
    parte["correlacionados"] = len({**por_rw, **por_bn})

    # R7 · el fichero anual pierde entradas que el histórico por grupo sí
    # tiene. Se completa para los grupos con informe, antes de calcular
    # cualquier delta: si se hiciera después, lo añadido no se compararía.
    parte["completado_historico"] = completar_con_historico(
        por_grupo, sorted(set(por_rw.values())), anio, errores,
        usar_cache=not a.sin_cache)

    base_act = base.get("actores", {})
    base_cat = base.get("catalogo", {})
    nuevo_act, nuevo_cat = {}, {}

    for r in inv:
        idi = r["id"]
        nombre = por_rw.get(idi)
        if not nombre:
            continue
        regs = por_grupo.get(nombre) or []
        resumen = resumir_victimas(regs)
        nuevo_act[idi] = resumen
        if not a.inicializar and not primera:
            h = delta_actor(idi, nombre, resumen, base_act.get(idi), regs)
            if h:
                parte["actores"].append(h)
        # mudos: último día con víctima nueva
        dias_pub = sorted(resumen["por_publicacion"])
        if dias_pub:
            ultimo = dias_pub[-1]
            try:
                d = (hoy - _dt.date.fromisoformat(ultimo)).days
            except ValueError:
                d = None
            if d is not None and d >= a.silencio:
                parte["mudos"].append({"informe": idi, "fuente_nombre": nombre,
                                       "ultima_publicacion": ultimo, "dias": d})
        ficha = fichas.get(nombre)
        if ficha:
            nuevo_cat[idi] = ficha
            if not a.inicializar and not primera:
                c = delta_catalogo(idi, nombre, ficha, base_cat.get(idi))
                if c:
                    parte["catalogo"].append(c)

    # ── actores de las fuentes sin informe
    cubiertos = {plegar(n) for n in list(por_rw.values()) + list(por_bn.values())}
    for n, g in sorted(fichas.items()):
        if plegar(n) in cubiertos:
            continue
        regs = por_grupo.get(n) or []
        if not regs:
            continue
        parte["actores_sin_informe"].append({
            "nombre": n, "alta": g.get("added_date"),
            "victimas": len(regs),
            "sitios": len(g.get("locations") or []),
            "tecnicas": sum(len(t.get("techniques") or []) for t in (g.get("ttps") or [])),
            "descripcion": bool((g.get("description") or "").strip()),
        })
    parte["actores_sin_informe"].sort(key=lambda x: -x["victimas"])

    # ── C2 e indicadores
    ya = indicadores_publicados()
    parte["c2"] = delta_c2(entradas_c2, base.get("c2"), ya)
    if a.inicializar or primera:
        # En la primera ejecución no hay delta: todo es «nuevo» y sería ruido.
        parte["c2"]["nuevas"] = []
        parte["c2"]["candidatos_a_ioc"] = []
        parte["c2"]["regionales"] = []
        parte["c2"]["desaparecidas"] = []

    parte["bgp"] = bgp if isinstance(bgp, dict) else {}

    # ── escritura
    ruta_md = os.path.join(DIR_VIG, "parte-%s.md" % hoy.isoformat())
    ruta_js = os.path.join(DIR_VIG, "parte-%s.json" % hoy.isoformat())
    escribir_parte(parte, ruta_md)
    with open(ruta_js, "w", encoding="utf-8") as fh:
        json.dump(parte, fh, ensure_ascii=False, indent=1)

    # ── línea base: NUNCA se degrada por un fallo de fuente
    #
    # Éste es el punto más delicado del script y se aprendió rompiéndolo: en la
    # primera prueba, un 429 de la fuente de extorsión hizo que se escribiera un
    # estado con cero actores, borrando la base acumulada. La consecuencia no es
    # perder un día: es que **el día siguiente reporta todo como nuevo**, cientos
    # de falsos positivos, y el parte deja de ser creíble.
    #
    # Regla: cada sección del estado sólo se sustituye si la fuente que la
    # alimenta respondió. Si no, se arrastra la anterior tal cual.
    rw_ok = fuente_ok.get("rwlive_victimas") and fuente_ok.get("rwlive_grupos")
    bn_ok = fuente_ok.get("botnetcl_c2")

    nuevo_estado = {
        "fecha": hoy.isoformat(),
        "anio": anio,
        "actores": nuevo_act if rw_ok else base.get("actores", {}),
        "catalogo": nuevo_cat if rw_ok else base.get("catalogo", {}),
        "c2": (sorted({e["ip"] for e in entradas_c2 if e.get("ip")})
               if bn_ok else base.get("c2", [])),
        "bgp": parte["bgp"] if fuente_ok.get("botnetcl_bgp") else base.get("bgp", {}),
        "arrastrado_de": {
            k: base.get("fecha") for k, v in
            {"actores": rw_ok, "catalogo": rw_ok, "c2": bn_ok,
             "bgp": fuente_ok.get("botnetcl_bgp")}.items() if not v
        },
    }

    # Cinturón y tirantes: si la base nueva tuviera menos actores o menos
    # direcciones que la anterior sin que se haya pedido reinicializar, no se
    # escribe y se avisa. Un estado que encoge sin motivo es un error.
    encoge = []
    if not a.inicializar:
        if len(nuevo_estado["actores"]) < len(base.get("actores", {})):
            encoge.append("actores: %d → %d" % (
                len(base.get("actores", {})), len(nuevo_estado["actores"])))
        if len(nuevo_estado["c2"]) < len(base.get("c2", [])) * 0.5:
            encoge.append("C2: %d → %d (caída de más de la mitad)" % (
                len(base.get("c2", [])), len(nuevo_estado["c2"])))
    if encoge:
        discrepancias.append(
            "LÍNEA BASE NO ACTUALIZADA para evitar perder estado — %s. "
            "Se conserva la de %s. Si el encogimiento es legítimo, "
            "reinicialice con --inicializar" % ("; ".join(encoge), base.get("fecha", "?")))
        parte["base_no_actualizada"] = True
    else:
        with open(ESTADO, "w", encoding="utf-8") as fh:
            json.dump(nuevo_estado, fh, ensure_ascii=False, indent=1)

    # ── resumen por consola
    tot_reg = sum(len(h.get("regionales_nuevas", [])) for h in parte["actores"])
    tot_vic = sum(h.get("victimas_nuevas", 0) for h in parte["actores"])
    cand = len(parte["c2"].get("candidatos_a_ioc") or [])
    if a.inicializar or primera:
        aviso("línea base creada: %d actores correlacionados, %d direcciones de C2."
              % (len(nuevo_act), len(nuevo_estado["c2"])))
        aviso("La próxima ejecución ya reportará deltas.")
    elif parte["parcial"]:
        caidas = [k for k, v in fuente_ok.items() if not v]
        aviso("COLECCIÓN PARCIAL: no respondieron %s." % ", ".join(caidas))
        aviso("Lo que sigue NO es «no hay cambios»: es «no se pudo mirar».")
        aviso("  medido donde sí hubo colección → víctimas nuevas: %d · "
              "regionales: %d · candidatos a indicador: %d" % (tot_vic, tot_reg, cand))
    else:
        aviso("víctimas nuevas: %d · regionales: %d · candidatos a indicador: %d · "
              "cambios de catálogo: %d" % (tot_vic, tot_reg, cand, len(parte["catalogo"])))
    if parte.get("base_no_actualizada"):
        aviso("⚠ línea base NO actualizada para no perder estado — ver el parte.")
    if errores:
        aviso("⚠ %d fuente(s) con problemas — ver el parte." % len(errores))
    aviso("parte: %s" % os.path.relpath(ruta_md, RAIZ))
    if a.json:
        json.dump(parte, sys.stdout, ensure_ascii=False, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
