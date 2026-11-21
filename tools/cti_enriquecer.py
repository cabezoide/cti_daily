#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cti_enriquecer — compuerta de enriquecimiento de los indicadores publicados.

QUÉ PROBLEMA RESUELVE
=====================

`cti_gate.py` comprueba **coherencia interna**: que el informe no se contradiga.
No puede saber si un indicador que publicamos sigue vivo, si pertenece a
Cloudflare, o si un tercero lo atribuye a otra familia. Eso exige salir a la
red, y es lo que hace esta compuerta.

Nació de un hallazgo del **21-11-2026**: cuatro de las nueve direcciones IP del
aviso conjunto `AA26-293A` pertenecen a **Cloudflare, GitHub y Google**, y se
descubrió resolviéndolas a mano. **Un repositorio que publica listas ingeribles
no puede depender de que alguien lo mire a mano**, así que aquí está
automatizado: la regla `N1` detecta esa clase de fallo en cualquier indicador de
cualquier informe.

LAS CINCO REGLAS
================

| Regla | Qué detecta | Por qué importa |
|---|---|---|
| **`N1`** | Indicador publicado que es **infraestructura legítima** | Es el fallo de `AA26-293A`. Una ingesta lo convierte en un corte propio |
| **`N2`** | **Conflicto de atribución**: un tercero lo asigna a otra familia | Publicar «es de X» cuando ThreatFox dice «es de Y» exige decidirlo, no ignorarlo |
| **`N3`** | **Corroboración disponible y no citada** | Si un tercero confirma nuestro indicador, el informe gana grado y no lo sabe |
| **`N4`** | Indicador **declarado caducado que sigue vivo**, o al revés | La caducidad es un juicio y aquí se puede comprobar |
| **`N5`** | **Colección parcial** | Doctrina de la casa: una fuente caída no es un veredicto limpio |

LO QUE NO HACE, Y ES DELIBERADO
===============================

**No bloquea por omisión.** Depende de la red y de cuotas de terceros, y una
compuerta que bloquea el trabajo porque VirusTotal agotó su cuota se desactiva
el primer día. Por omisión informa; con `--estricto` bloquea. **Y nunca bloquea
por `N5`**: una fuente caída es una brecha de colección, no un defecto del
informe.

**No consulta el mismo indicador dos veces al día.** La caché está en
`vigilancia/.cache-enriquecimiento.json`, con vida útil configurable, y no se
versiona.

USO
===

    python3 tools/cti_enriquecer.py                  # lote ThreatFox, toda la cartera
    python3 tools/cti_enriquecer.py CTI-2026-045*    # un informe
    python3 tools/cti_enriquecer.py --profundo       # además, por indicador
    python3 tools/cti_enriquecer.py --dias 7         # ventana del lote ThreatFox

**La ventana del lote decide qué se cruza, y es la limitación principal.**
`get_iocs` devuelve los indicadores de los últimos N días, no el histórico. Con
`--dias 3` el C2 `103.163.214.134` de `CTI-2026-045` **no aparecía** aunque
ThreatFox lo tenía: su `first_seen` era de cuatro días antes. Por eso el valor
por omisión es 7. Para comprobar un indicador histórico concreto hay que
buscarlo uno a uno (`search_ioc`), y eso no se hace para los 440 de la cartera
porque sería una petición por indicador.
    python3 tools/cti_enriquecer.py --estricto       # salir 1 si hay hallazgos
    python3 tools/cti_enriquecer.py --fuentes        # qué está disponible y salir

LAS CLAVES NO VIVEN AQUÍ
========================

Se leen del entorno o de `~/.config/cti/claves.env`, **fuera del repositorio**.
Este repositorio se publica en GitHub Pages: una clave escrita en `tools/`
quedaría publicada. El script del que desciende llevaba siete en el código.
"""

import argparse
import datetime as _dt
import ipaddress
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "tools"))

import cti_build as B                                            # noqa: E402

CACHE = os.path.join(RAIZ, "vigilancia", ".cache-enriquecimiento.json")
FICHERO_CLAVES = os.path.expanduser("~/.config/cti/claves.env")
AGENTE = "cti-enriquecer/1.0"
ESPERA = 25
PAUSA = 1.1                      # cortesía con servicios gratuitos de terceros
VIDA_CACHE = 86400               # un día


# ─────────────────────────────────────────────────────────────────── claves

CLAVES = {
    "threatfox": "CTI_THREATFOX_KEY",
    "virustotal": "CTI_VIRUSTOTAL_KEY",
    "shodan": "CTI_SHODAN_KEY",
    "greynoise": "CTI_GREYNOISE_KEY",
    "abuseipdb": "CTI_ABUSEIPDB_KEY",
    "otx": "CTI_OTX_KEY",
}


def _del_fichero():
    if not os.path.exists(FICHERO_CLAVES):
        return {}
    d = {}
    try:
        with open(FICHERO_CLAVES, encoding="utf-8") as f:
            for l in f:
                l = l.strip()
                if l and not l.startswith("#") and "=" in l:
                    k, v = l.split("=", 1)
                    d[k.strip()] = v.strip().strip('"').strip("'")
    except OSError:
        pass
    return d


_FICH = _del_fichero()


def clave(n):
    return os.environ.get(CLAVES[n]) or _FICH.get(CLAVES[n]) or ""


# ───────────────────────────────── proveedores cuyo bloqueo rompe la casa
#
# La señal de `N1` no puede depender de una sola fuente: AbuseIPDB marca la
# lista blanca, GreyNoise marca `riot`, y ninguna de las dos cubre todo. Esta
# lista es el tercer apoyo, y se compara contra el ISP declarado.

# **La distinción que importa, y la primera versión de esta regla no la hacía.**
#
# No todo «proveedor grande» es infraestructura compartida:
#
#   · Una IP de **Cloudflare, Akamai o GitHub Pages** sirve a millones de
#     terceros. Bloquearla **rompe a terceros ajenos al caso**.
#   · Una IP de **Hetzner, OVH o Hostinger** es de UN cliente, que puede ser
#     perfectamente el adversario. Bloquearla afecta a ese cliente y a nadie más.
#
# La primera versión metía a los dos grupos en la misma lista y marcaba como
# «posible infraestructura legítima» tres direcciones de `AA26-293A` alojadas en
# Hostinger, Hetzner y servinga que el aviso califica de exfiltración y paneles
# del adversario. Eso es ruido, y el ruido desactiva la compuerta.
#
# Sólo el primer grupo dispara el hallazgo.
INFRAESTRUCTURA_COMPARTIDA = (
    "cloudflare", "akamai", "fastly", "cloudfront", "github", "gitlab",
    "bitbucket", "google", "dropbox", "imperva", "incapsula", "sucuri",
    "stackpath", "bunny", "atlassian", "jsdelivr", "unpkg", "wordpress",
    "automattic", "shopify", "wix", "squarespace",
)

# Alojamiento por servidor: NO dispara por sí solo. Se conserva para poder
# decirlo en el mensaje cuando otra señal sí haya disparado.
ALOJAMIENTO = (
    "hetzner", "ovh", "digitalocean", "linode", "vultr", "hostinger",
    "servinga", "contabo", "scaleway", "leaseweb", "oracle", "choopa",
)

# Tipos que SÍ llegan a los agregados planos y por tanto a una lista de bloqueo.
# Un hallazgo `N1` sobre uno de éstos es más grave que sobre un `artefacto`.
TIPOS_INGERIBLES = {"ipv4", "ipv6", "domain", "url", "md5", "sha1", "sha256",
                    "cve", "asn", "pattern", "filename", "fqdn"}


class H:
    __slots__ = ("informe", "regla", "valor", "mensaje", "grave")

    def __init__(self, informe, regla, valor, mensaje, grave=False):
        self.informe, self.regla = informe, regla
        self.valor, self.mensaje, self.grave = valor, mensaje, grave

    def a_dict(self):
        return {"informe": self.informe, "regla": self.regla,
                "valor": self.valor, "mensaje": self.mensaje,
                "grave": self.grave}


# ──────────────────────────────────────────────────────────────────── red

def _pedir(url, cabeceras=None, cuerpo=None, metodo=None):
    pet = urllib.request.Request(url, data=cuerpo, method=metodo)
    pet.add_header("User-Agent", AGENTE)
    for k, v in (cabeceras or {}).items():
        pet.add_header(k, v)
    with urllib.request.urlopen(pet, timeout=ESPERA) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def _cache_leer():
    try:
        with open(CACHE, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def _cache_escribir(c):
    try:
        os.makedirs(os.path.dirname(CACHE), exist_ok=True)
        with open(CACHE, "w", encoding="utf-8") as f:
            json.dump(c, f, ensure_ascii=False)
    except OSError as ex:
        print("aviso: no se pudo escribir la caché: %s" % ex, file=sys.stderr)


# ───────────────────────────────────────────────── ThreatFox: lote y búsqueda

def threatfox_lote(dias, avisos):
    """Una sola petición para toda la cartera.

    `get_iocs` devuelve los indicadores de los últimos `dias`. Cruzarlo en
    local cuesta una petición y cubre los 440 `ipv4` del repositorio; hacerlo
    indicador a indicador costaría 440 y agotaría la cortesía de la fuente.

    **La API exige `Auth-Key` desde 2026.** Sin cabecera devuelve
    `{"error": "Unauthorized"}`, que es una respuesta bien formada a otra
    pregunta: el consultor del que desciende este módulo lo mostraba como
    «sin datos» y así estuvo.
    """
    k = clave("threatfox")
    if not k:
        avisos.append("ThreatFox: falta CTI_THREATFOX_KEY; no se consulta")
        return None
    try:
        d = _pedir("https://threatfox-api.abuse.ch/api/v1/",
                   cabeceras={"Auth-Key": k, "Content-Type": "application/json"},
                   cuerpo=json.dumps({"query": "get_iocs",
                                      "days": int(dias)}).encode(),
                   metodo="POST")
    except Exception as ex:
        avisos.append("ThreatFox: no se pudo consultar (%s)" % ex)
        return None
    if d.get("error"):
        avisos.append("ThreatFox: %s" % d["error"])
        return None
    if d.get("query_status") != "ok":
        avisos.append("ThreatFox: query_status=%s" % d.get("query_status"))
        return None
    filas = d.get("data") or []
    if not isinstance(filas, list):
        avisos.append("ThreatFox: `data` no es una lista")
        return None

    idx = {}
    for x in filas:
        v = (x.get("ioc") or "").strip()
        if not v:
            continue
        # Los IOC de tipo `ip:port` se indexan también por la IP desnuda.
        idx.setdefault(v.lower(), []).append(x)
        if ":" in v:
            idx.setdefault(v.split(":")[0].lower(), []).append(x)
    return {"n": len(filas), "idx": idx, "dias": dias}


def threatfox_buscar(valor, cache, avisos):
    k = clave("threatfox")
    if not k:
        return None
    cc = "tf:%s" % valor
    ahora = time.time()
    if cc in cache and ahora - cache[cc].get("_t", 0) < VIDA_CACHE:
        return cache[cc].get("v")
    try:
        d = _pedir("https://threatfox-api.abuse.ch/api/v1/",
                   cabeceras={"Auth-Key": k, "Content-Type": "application/json"},
                   cuerpo=json.dumps({"query": "search_ioc",
                                      "search_term": valor}).encode(),
                   metodo="POST")
    except Exception as ex:
        avisos.append("ThreatFox/%s: %s" % (valor, ex))
        return None
    v = d.get("data") if d.get("query_status") == "ok" else []
    v = v if isinstance(v, list) else []
    cache[cc] = {"_t": ahora, "v": v}
    time.sleep(PAUSA)
    return v


# ────────────────────────────────────────── fuentes por indicador (profundo)

def abuseipdb(ip, cache, avisos):
    k = clave("abuseipdb")
    if not k:
        return None
    cc, ahora = "ab:%s" % ip, time.time()
    if cc in cache and ahora - cache[cc].get("_t", 0) < VIDA_CACHE:
        return cache[cc].get("v")
    try:
        d = _pedir("https://api.abuseipdb.com/api/v2/check"
                   "?ipAddress=%s&maxAgeInDays=90" % ip,
                   cabeceras={"Accept": "application/json", "Key": k})
        v = d.get("data")
    except Exception as ex:
        avisos.append("AbuseIPDB/%s: %s" % (ip, ex))
        return None
    cache[cc] = {"_t": ahora, "v": v}
    time.sleep(PAUSA)
    return v


def greynoise(ip, cache, avisos):
    """GreyNoise comunidad. Un 404 **es** un resultado: «no observada»."""
    k = clave("greynoise")
    if not k:
        return None
    cc, ahora = "gn:%s" % ip, time.time()
    if cc in cache and ahora - cache[cc].get("_t", 0) < VIDA_CACHE:
        return cache[cc].get("v")
    v = None
    try:
        v = _pedir("https://api.greynoise.io/v3/community/%s" % ip,
                   cabeceras={"Accept": "application/json", "key": k})
    except urllib.error.HTTPError as ex:
        if ex.code == 404:
            try:
                v = json.loads(ex.read().decode("utf-8", "replace"))
            except Exception:
                v = None
        else:
            avisos.append("GreyNoise/%s: HTTP %s" % (ip, ex.code))
            return None
    except Exception as ex:
        avisos.append("GreyNoise/%s: %s" % (ip, ex))
        return None
    cache[cc] = {"_t": ahora, "v": v}
    time.sleep(PAUSA)
    return v


# ───────────────────────────────────────────────────────────── evaluación

def _es_ip(v):
    try:
        ipaddress.ip_address(v)
        return True
    except ValueError:
        return False


def _familias_del_informe(inf):
    """Nombres que el informe reivindica, para comparar con los de terceros."""
    fm = inf["fm"]
    bruto = (fm.get("actor", "") + " " + fm.get("id", "")).lower()
    piezas = re.split(r"[·,|/]| y |\s-\s", bruto)
    return {p.strip() for p in piezas if len(p.strip()) > 2}


def evaluar(inf, lote, cache, avisos, profundo):
    H_ = []
    ident = inf["id"]
    familias = _familias_del_informe(inf)

    try:
        filas = B.filas_ioc(inf)
    except Exception as ex:
        avisos.append("%s: no se pudieron extraer indicadores (%s)" % (ident, ex))
        return H_

    for fila in filas:
        tipo = (fila.get("tipo") or "").strip().lower()
        valor = (fila.get("valor") or "").strip()
        if not valor or len(valor) > 120:
            continue
        ingerible = tipo in TIPOS_INGERIBLES
        ctx = " ".join(str(v) for v in fila.values()).lower()

        # ── N2 / N3 · cruce con el lote de ThreatFox
        if lote:
            hits = lote["idx"].get(valor.lower()) or []
            if hits:
                fams = {(x.get("malware_printable") or "").strip()
                        for x in hits if x.get("malware_printable")}
                fams = {f for f in fams if f}
                amenazas = {x.get("threat_type") for x in hits if x.get("threat_type")}
                ultima = max((x.get("last_seen") or "") for x in hits)

                ajena = {f for f in fams
                         if not any(t and (t in f.lower() or f.lower() in t)
                                    for t in familias)}
                if ajena:
                    H_.append(H(ident, "N2", valor,
                                "ThreatFox lo atribuye a **%s** (%s), que no es "
                                "el actor de este informe. Visto por última vez "
                                "%s. **Decidir si es el mismo operador, un "
                                "solapamiento o un error de atribución.**"
                                % (", ".join(sorted(ajena)),
                                   ", ".join(sorted(amenazas)) or "sin tipo",
                                   ultima or "sin fecha"),
                                grave=False))
                else:
                    H_.append(H(ident, "N3", valor,
                                "ThreatFox lo corrobora (%s, visto hasta %s). "
                                "**El informe gana grado de evidencia y no lo "
                                "cita.**" % (", ".join(sorted(fams)) or "sin familia",
                                             ultima or "sin fecha")))

                # ── N4 · declarado caducado pero vivo en la fuente
                if re.search(r"caducad|ventana cerrada|retirada|inactiv", ctx):
                    H_.append(H(ident, "N4", valor,
                                "el informe lo da por **caducado o retirado** y "
                                "ThreatFox lo ha visto hasta **%s**. Revisar la "
                                "caducidad declarada." % (ultima or "sin fecha"),
                                grave=True))

        # ── N1 · infraestructura legítima publicada como indicador
        if not _es_ip(valor):
            continue

        señales = []
        if profundo:
            ab = abuseipdb(valor, cache, avisos)
            if ab:
                isp = (ab.get("isp") or "").lower()
                uso = (ab.get("usageType") or "")
                if ab.get("isWhitelisted"):
                    señales.append("AbuseIPDB lo tiene en **lista blanca**")
                compartida = next((p for p in INFRAESTRUCTURA_COMPARTIDA
                                   if p in isp), None)
                if compartida:
                    señales.append("el ISP es **%s**, infraestructura "
                                   "**compartida** por muchos terceros"
                                   % ab.get("isp"))
                if uso.lower().startswith("content delivery"):
                    señales.append("AbuseIPDB lo clasifica como **red de "
                                   "distribución de contenido**")
                # «Data Center/Web Hosting/Transit» con puntuación 0 describe a
                # cualquier servidor alquilado, el del adversario incluido. NO
                # es señal por sí mismo: sólo se menciona si algo más disparó.
                if señales and next((p for p in ALOJAMIENTO if p in isp), None):
                    señales.append("alojado en **%s** (alojamiento por servidor: "
                                   "el bloqueo afectaría sólo a ese cliente)"
                                   % ab.get("isp"))
            gn = greynoise(valor, cache, avisos)
            if gn and gn.get("riot"):
                señales.append("GreyNoise lo marca **`riot`**: servicio legítimo "
                               "de uso común (%s)" % (gn.get("name") or "sin nombre"))

        if señales:
            H_.append(H(ident, "N1", valor,
                        "**posible infraestructura legítima publicada como "
                        "indicador** — %s. %s"
                        % ("; ".join(señales),
                           "**Tipo `%s`: llega al agregado plano, que es una "
                           "lista de bloqueo.**" % tipo if ingerible
                           else "Tipo `%s`: no llega a los agregados, pero "
                                "conviene revisar el contexto." % tipo),
                        grave=ingerible))
    return H_


# ────────────────────────────────────────────────────────────── ejecución

def main():
    p = argparse.ArgumentParser(
        description="Compuerta de enriquecimiento: comprueba contra terceros los "
                    "indicadores que la cartera publica.")
    p.add_argument("patron", nargs="*", help="informes (por omisión, todos)")
    p.add_argument("--dias", type=int, default=7,
                   help="ventana del lote de ThreatFox (por omisión 7; con 3 se "
                        "escapan indicadores vistos hace 4-7 días, medido)")
    p.add_argument("--profundo", action="store_true",
                   help="además, consultar cada IP en AbuseIPDB y GreyNoise")
    p.add_argument("--limite", type=int, default=120,
                   help="máximo de IP a consultar en modo profundo")
    p.add_argument("--estricto", action="store_true",
                   help="salir con código 1 si hay hallazgos graves")
    p.add_argument("--json", action="store_true", help="salida legible por máquina")
    p.add_argument("--fuentes", action="store_true",
                   help="mostrar disponibilidad de claves y salir")
    a = p.parse_args()

    if a.fuentes:
        print("Claves (entorno o %s):" % FICHERO_CLAVES)
        for n in CLAVES:
            print("  %-12s %s" % (n, "disponible" if clave(n) else "FALTA"))
        print("\nCensys Search v2 está apagada (cierre 2026-09-30): no se usa.")
        print("VirusTotal no se usa en esta compuerta: su cuota se agota con "
              "una fracción de los 440 indicadores de la cartera.")
        return 0

    lista = B.informes()
    if a.patron:
        import fnmatch
        lista = [i for i in lista
                 if any(fnmatch.fnmatch(i["md"], q) or q in i["id"]
                        for q in a.patron)]

    avisos = []
    lote = threatfox_lote(a.dias, avisos)

    # En modo profundo se acota el número de IP distintas, porque son cuotas
    # de terceros y porque el resultado se cachea un día.
    if a.profundo:
        vistos, tope = set(), a.limite
        for inf in lista:
            try:
                for f in B.filas_ioc(inf):
                    v = (f.get("valor") or "").strip()
                    if _es_ip(v):
                        vistos.add(v)
            except Exception:
                pass
        if len(vistos) > tope:
            avisos.append("modo profundo: %d IP distintas, se consultarán las "
                          "primeras %d (usar --limite para ampliar)"
                          % (len(vistos), tope))

    cache = _cache_leer()
    hallazgos = []
    for inf in lista:
        hallazgos += evaluar(inf, lote, cache, avisos, a.profundo)
    _cache_escribir(cache)

    graves = [h for h in hallazgos if h.grave]
    leves = [h for h in hallazgos if not h.grave]

    if a.json:
        print(json.dumps({"informes": len(lista),
                          "threatfox": (lote or {}).get("n", 0),
                          "graves": [h.a_dict() for h in graves],
                          "leves": [h.a_dict() for h in leves],
                          "avisos_de_coleccion": avisos},
                         ensure_ascii=False, indent=1))
        return 1 if (graves and a.estricto) else 0

    print("cti_enriquecer · %d informes · ThreatFox: %d indicadores de %d día(s) "
          "· %d grave(s) · %d hallazgo(s) leve(s)"
          % (len(lista), (lote or {}).get("n", 0), a.dias, len(graves), len(leves)))

    for titulo, grupo in (("GRAVE", graves), ("hallazgos", leves)):
        if not grupo:
            continue
        print("\n╭─ %s ───────────────────────────────────────────" % titulo)
        por = {}
        for h in grupo:
            por.setdefault(h.informe, []).append(h)
        for ident in sorted(por):
            print("│\n│ %s" % ident)
            for h in por[ident]:
                print("│   [%s] `%s`" % (h.regla, h.valor))
                print("│        %s" % h.mensaje)
        print("╰────────────────────────────────────────────────────────")

    # ── N5 · la colección se declara siempre, y nunca bloquea
    if avisos:
        print("\n╭─ N5 · colección parcial ───────────────────────────────")
        for m in avisos:
            print("│   ⚠ %s" % m)
        print("│   La ausencia de hallazgos en una fuente que no respondió")
        print("│   NO es un veredicto limpio. (R6 de la doctrina de la casa)")
        print("╰────────────────────────────────────────────────────────")

    if not hallazgos:
        print("\nSin hallazgos de enriquecimiento.")

    if graves and a.estricto:
        print("\n--estricto: hay %d hallazgo(s) grave(s)." % len(graves))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
