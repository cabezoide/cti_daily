#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cti_attack — el catálogo MITRE ATT&CK, destilado y en caché.

POR QUÉ EXISTE
==============

El **21-11-2026** el usuario pidió *«alineamiento de todos los informes a MITRE
ATT&CK de TTPs […] y dejalo en un gate para mantenerlo en el tiempo»*. Una
compuerta que sólo comprobara la FORMA del identificador —`Tnnnn`— dejaría
pasar `T1234` inventado, o `T1086` (PowerShell), que MITRE **retiró** en 2020 y
que sigue copiándose de informes viejos. Para decir «esta técnica existe y se
llama así» hace falta el catálogo.

**De dónde sale.** El paquete STIX oficial de `mitre-attack/attack-stix-data`.
Son ~45 MB, así que no se guarda entero: se **destila** a lo único que la
compuerta necesita —identificador, nombre, tácticas, y si está obsoleta o
sustituida— y eso cabe en unos 100 KB.

**La caché es deliberada y larga.** ATT&CK publica versiones, no cambios
diarios: consultarlo en cada commit sería descortés e inútil. Vida por omisión
de 30 días, y `--refrescar` para forzarlo.

**No bloquea cuando no hay red.** Misma doctrina que `cti_enriquecer`: una
compuerta que detiene el trabajo porque GitHub no responde se desactiva el
primer día. Sin catálogo, las reglas que dependen de él se declaran **no
comprobadas** en voz alta, y las de forma siguen funcionando.

USO
===

    python3 tools/cti_attack.py              # estado de la caché
    python3 tools/cti_attack.py --refrescar  # volver a descargar
    python3 tools/cti_attack.py T1588.007    # consultar una técnica
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.request

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(RAIZ, "vigilancia", ".cache-attack.json")
VIDA = 30 * 24 * 3600

# Las TRES matrices. Enterprise no basta: `CTI-2026-018` cita `T1660`
# (Phishing), que existe pero en **Mobile**, y una compuerta que sólo mirase
# Enterprise lo declararía inventado. ICS entra por los informes de OT.
FUENTES = {
    "enterprise": "https://raw.githubusercontent.com/mitre-attack/"
                  "attack-stix-data/master/enterprise-attack/enterprise-attack.json",
    "mobile":     "https://raw.githubusercontent.com/mitre-attack/"
                  "attack-stix-data/master/mobile-attack/mobile-attack.json",
    "ics":        "https://raw.githubusercontent.com/mitre-attack/"
                  "attack-stix-data/master/ics-attack/ics-attack.json",
}

RE_TEC = re.compile(r"^T\d{4}(\.\d{3})?$")

# El nombre que esta cartera usa en castellano para cada táctica. **La lista
# de tácticas NO se codifica aquí**: se extrae del propio STIX, porque ATT&CK
# las cambia —la v20 añadió `stealth`, que no existía cuando se escribieron
# los primeros informes de esta cartera— y una tabla a mano envejece sin que
# nadie se entere. Esto es sólo la traducción; lo que no esté traducido se
# muestra con su nombre inglés.
TACTICAS = {
    "reconnaissance":         "Reconocimiento",
    "resource-development":   "Desarrollo de recursos",
    "initial-access":         "Acceso inicial",
    "execution":              "Ejecución",
    "persistence":            "Persistencia",
    "privilege-escalation":   "Escalada de privilegios",
    "defense-evasion":        "Evasión de defensas",
    "credential-access":      "Acceso a credenciales",
    "discovery":              "Descubrimiento",
    "lateral-movement":       "Movimiento lateral",
    "collection":             "Recolección",
    "command-and-control":    "Mando y control",
    "exfiltration":           "Exfiltración",
    "impact":                 "Impacto",
    "stealth":                "Sigilo",
    "defense-impairment":     "Degradación de defensas",
    "defense-evasion":        "Evasión de defensas",
    "network-effects":        "Efectos de red",
    "remote-service-effects": "Efectos sobre servicios remotos",
    "impair-process-control": "Degradación del control de proceso",
    "inhibit-response-function": "Inhibición de la función de respuesta",
    "evasion":                "Evasión",
}
# El mismo mapa al revés, tolerante: sin tildes ni mayúsculas.
def _norm(x):
    s = (x or "").strip().lower()
    for a, b in (("á","a"),("é","e"),("í","i"),("ó","o"),("ú","u")):
        s = s.replace(a, b)
    return s

ES_A_CLAVE = {_norm(v): k for k, v in TACTICAS.items()}


def forma_valida(ident):
    return bool(RE_TEC.match((ident or "").strip()))


# ─────────────────────────────────────────────────────── descarga y destilado

def _destilar(bruto, matriz="enterprise", tecnicas=None, tacticas=None):
    """Del STIX completo a lo que la compuerta necesita."""
    tecnicas = {} if tecnicas is None else tecnicas
    tacticas = {} if tacticas is None else tacticas
    revocaciones = {}
    por_stix = {}

    for o in bruto.get("objects", []):
        if o.get("type") == "x-mitre-tactic":
            sn = o.get("x_mitre_shortname")
            if sn:
                tacticas[sn] = o.get("name") or sn
        t = o.get("type")
        if t == "attack-pattern":
            ident = None
            for ref in o.get("external_references", []):
                if ref.get("source_name") == "mitre-attack":
                    ident = ref.get("external_id")
                    break
            if not ident:
                continue
            por_stix[o.get("id")] = ident
            if ident in tecnicas and matriz != "enterprise":
                continue          # Enterprise manda si una está en dos matrices
            tecnicas[ident] = {
                "matriz": matriz,
                "nombre": o.get("name") or "",
                "tacticas": [f.get("phase_name") for f
                             in (o.get("kill_chain_phases") or [])
                             if f.get("kill_chain_name") == "mitre-attack"],
                "obsoleta": bool(o.get("x_mitre_deprecated")),
                "revocada": bool(o.get("revoked")),
                "sub": "." in ident,
            }
        elif t == "relationship" and o.get("relationship_type") == "revoked-by":
            revocaciones[o.get("source_ref")] = o.get("target_ref")

    # «revocada por» traducido a identificadores legibles
    for origen, destino in revocaciones.items():
        a, b = por_stix.get(origen), por_stix.get(destino)
        if a in tecnicas and b:
            tecnicas[a]["sustituida_por"] = b

    version = ""
    for o in bruto.get("objects", []):
        if o.get("type") == "x-mitre-collection":
            version = (o.get("x_mitre_version") or "")
            break
    return version


def descargar(avisos=None):
    tecnicas, tacticas, version = {}, {}, ""
    for matriz, url in FUENTES.items():
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": "cti-daily-gate"})
            with urllib.request.urlopen(req, timeout=180) as r:
                bruto = json.load(r)
        except Exception as ex:
            if avisos is not None:
                avisos.append("ATT&CK: no se pudo descargar la matriz %s (%s)"
                              % (matriz, ex))
            if matriz == "enterprise":
                return None       # sin Enterprise no hay catálogo que valga
            continue
        v = _destilar(bruto, matriz, tecnicas, tacticas)
        if matriz == "enterprise":
            version = v
    d = {"version": version, "n": len(tecnicas), "tecnicas": tecnicas,
         "tacticas": tacticas, "_t": time.time()}
    try:
        os.makedirs(os.path.dirname(CACHE), exist_ok=True)
        json.dump(d, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False)
    except Exception:
        pass
    return d


def catalogo(avisos=None, refrescar=False):
    """El catálogo destilado, de la caché o de la red. `None` si no hay."""
    if not refrescar and os.path.exists(CACHE):
        try:
            d = json.load(open(CACHE, encoding="utf-8"))
            if time.time() - d.get("_t", 0) < VIDA:
                return d
        except Exception:
            pass
    d = descargar(avisos)
    if d is None and os.path.exists(CACHE):
        # Caducada pero utilizable: mejor un catálogo viejo que ninguno, y se
        # dice en voz alta.
        try:
            d = json.load(open(CACHE, encoding="utf-8"))
            if avisos is not None:
                avisos.append("ATT&CK: se usa la caché caducada (%d técnicas)"
                              % d.get("n", 0))
        except Exception:
            return None
    return d


def main():
    ap = argparse.ArgumentParser(description="El catálogo MITRE ATT&CK en caché.")
    ap.add_argument("tecnica", nargs="?", help="identificador a consultar")
    ap.add_argument("--refrescar", action="store_true")
    a = ap.parse_args()

    avisos = []
    c = catalogo(avisos, refrescar=a.refrescar)
    for x in avisos:
        print(x, file=sys.stderr)
    if not c:
        print("sin catálogo: no hay caché y no se pudo descargar",
              file=sys.stderr)
        return 1

    edad = (time.time() - c.get("_t", 0)) / 86400.0
    print("ATT&CK Enterprise v%s · %d técnicas · caché de hace %.1f día(s)"
          % (c.get("version") or "?", c.get("n", 0), edad))
    if a.tecnica:
        t = c["tecnicas"].get(a.tecnica.strip().upper())
        if not t:
            print("  %s NO existe en el catálogo" % a.tecnica)
            return 1
        print("  %s · %s" % (a.tecnica, t["nombre"]))
        print("     tácticas: %s" % ", ".join(
            TACTICAS.get(x, x) for x in t["tacticas"]))
        if t.get("obsoleta"):  print("     ⚠ OBSOLETA")
        if t.get("revocada"):  print("     ⚠ REVOCADA -> %s"
                                     % t.get("sustituida_por", "?"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
