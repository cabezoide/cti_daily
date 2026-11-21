#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cti_render — comprueba las páginas en un navegador de verdad.

POR QUÉ EXISTE
==============

El **21-11-2026** se corrigieron cinco fallos del repositorio. Tres los encontró
una compuerta. **Dos los encontró el usuario mirando la página**, y las dos
compuertas existentes los dejaron pasar enteros porque ninguna abre un
navegador:

1. **La píldora que invadía la tarjeta vecina.** El tipo de `CTI-2026-062` era
   más largo que los demás, `.pill` tenía `white-space:nowrap`, y la etiqueta se
   salía por la derecha montándose sobre la tarjeta de al lado. El HTML era
   válido y el texto correcto: sólo se veía mal.
2. **El buscador y las píldoras no filtraban nada.** El JavaScript marcaba las
   tarjetas con `hidden` y el contador decía «1 informe de 49»… y las 49 seguían
   en pantalla, porque `.card{display:flex}` gana por precedencia al
   `[hidden]{display:none}` de la hoja del navegador y **no había regla propia**.
   Es el fallo más instructivo de los dos: **el estado interno era correcto y la
   página mentía**, así que cualquier comprobación que mirase el DOM en lugar de
   la geometría lo habría dado por bueno.

De ahí las dos reglas que gobiernan este módulo:

- **Se mide la geometría, no el atributo.** `getClientRects()`, no `.hidden`.
- **Se comprueba a varios anchos**, porque el desbordamiento depende del ancho.

CÓMO SE USA
===========

    python3 tools/cti_render.py              # comprueba y sale 0/1
    python3 tools/cti_render.py --json       # salida legible por máquina
    python3 tools/cti_render.py --anchos 1400,900,380

`tools/cti_build.py` lo llama al terminar. **Si no hay Playwright instalado, no
falla: avisa y sigue.** Un repositorio que no se puede construir en una máquina
sin navegador sería peor que el fallo que esto previene.

    pip install playwright && playwright install chromium
"""

import argparse
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ANCHOS = (1400, 1180, 900, 600, 380)
MARGEN = 1.0          # píxeles de tolerancia: el redondeo subpíxel no es un fallo


class Fallo:
    __slots__ = ("pagina", "regla", "mensaje", "ancho")

    def __init__(self, pagina, regla, mensaje, ancho=None):
        self.pagina, self.regla, self.mensaje, self.ancho = pagina, regla, mensaje, ancho

    def a_dict(self):
        return {"pagina": self.pagina, "regla": self.regla,
                "mensaje": self.mensaje, "ancho": self.ancho}


def disponible():
    try:
        import playwright.sync_api                                   # noqa: F401
        return True
    except Exception:
        return False


# ───────────────────────────────────────────────────────── comprobaciones

# R1 · ningún elemento se sale de su tarjeta. El fallo de la píldora.
JS_DESBORDES = """() => {
  const fuera = [];
  document.querySelectorAll('.card').forEach(c => {
    const cr = c.getBoundingClientRect();
    c.querySelectorAll('*').forEach(el => {
      const r = el.getBoundingClientRect();
      if (r.width === 0 && r.height === 0) return;
      const dcha = r.right - cr.right, izq = cr.left - r.left;
      if (dcha > 1 || izq > 1)
        fuera.push({texto: (el.textContent || '').trim().slice(0, 44),
                    clase: el.className && el.className.toString().slice(0, 34),
                    dcha: +dcha.toFixed(1), izq: +izq.toFixed(1)});
    });
  });
  return fuera;
}"""

# R2 · la página no debe desplazarse en horizontal a ningún ancho.
JS_SCROLL = """() => ({
  scroll: document.documentElement.scrollWidth,
  ancho: document.documentElement.clientWidth
})"""

# R4 · `hidden` tiene que ocultar DE VERDAD. Se mide la geometría.
JS_HIDDEN = """() => {
  const d = document.createElement('div');
  d.className = 'card'; d.hidden = true; d.textContent = 'x';
  document.body.appendChild(d);
  const visible = d.getClientRects().length > 0;
  d.remove();
  return visible;
}"""

JS_VISIBLES = """() => [...document.querySelectorAll('#rejilla .card')]
                       .filter(c => c.getClientRects().length > 0).length"""


def _contar(pg):
    return pg.evaluate(JS_VISIBLES)


def comprobar_indice(b, anchos):
    """El índice: desbordes, scroll, y que el filtro filtre de verdad."""
    fallos = []
    ruta = "file://" + os.path.join(RAIZ, "index.html")

    for ancho in anchos:
        pg = b.new_page(viewport={"width": ancho, "height": 1000})
        errores = []
        pg.on("pageerror", lambda e: errores.append(str(e)))
        pg.goto(ruta)
        pg.wait_for_timeout(700)

        for f in pg.evaluate(JS_DESBORDES):
            fallos.append(Fallo("index.html", "R1",
                                "«%s» (clase `%s`) se sale de su tarjeta: %+.1f px "
                                "por la derecha, %+.1f por la izquierda. **Se "
                                "monta sobre la tarjeta vecina.**"
                                % (f["texto"], f["clase"], f["dcha"], f["izq"]),
                                ancho))

        s = pg.evaluate(JS_SCROLL)
        if s["scroll"] - s["ancho"] > MARGEN:
            fallos.append(Fallo("index.html", "R2",
                                "la página se desplaza en horizontal: %d px de "
                                "contenido en %d de ventana"
                                % (s["scroll"], s["ancho"]), ancho))

        for e in errores:
            fallos.append(Fallo("index.html", "R3",
                                "error de JavaScript: %s" % e[:150], ancho))
        pg.close()

    # ── R4 y R5 · el filtro, al ancho de escritorio
    pg = b.new_page(viewport={"width": 1280, "height": 1000})
    pg.goto(ruta)
    pg.wait_for_timeout(800)

    if pg.evaluate(JS_HIDDEN):
        fallos.append(Fallo("index.html", "R4",
                            "**el atributo `hidden` NO oculta**: una tarjeta con "
                            "`hidden` sigue ocupando sitio. Falta "
                            "`[hidden]{display:none !important}`; sin ella el "
                            "filtro marca las tarjetas y no se ve nada."))

    total = _contar(pg)
    if total == 0:
        fallos.append(Fallo("index.html", "R5", "no hay ninguna tarjeta visible"))
    else:
        # buscar algo que exista
        pg.fill("#q", "apt28")
        pg.wait_for_timeout(450)
        pocos = _contar(pg)
        if pocos >= total:
            fallos.append(Fallo("index.html", "R5",
                                "**el buscador no filtra**: con «apt28» siguen "
                                "visibles %d de %d tarjetas" % (pocos, total)))
        if pocos == 0:
            fallos.append(Fallo("index.html", "R5",
                                "el buscador oculta TODO con «apt28», que debería "
                                "tener al menos un resultado"))

        # buscar algo que no exista
        pg.fill("#q", "zzzzqqq")
        pg.wait_for_timeout(450)
        if _contar(pg) != 0:
            fallos.append(Fallo("index.html", "R5",
                                "una búsqueda sin resultados deja tarjetas visibles"))

        # limpiar restaura
        pg.fill("#q", "")
        pg.wait_for_timeout(400)
        if _contar(pg) != total:
            fallos.append(Fallo("index.html", "R5",
                                "limpiar el buscador no restaura: %d de %d"
                                % (_contar(pg), total)))

        # las píldoras de categoría
        n = pg.evaluate("document.querySelectorAll('#chips .chip').length")
        if n == 0:
            fallos.append(Fallo("index.html", "R6",
                                "no se generó ninguna píldora de categoría"))
        else:
            pg.click("#chips .chip:nth-child(1)")
            pg.wait_for_timeout(450)
            con = _contar(pg)
            if con >= total:
                fallos.append(Fallo("index.html", "R6",
                                    "**las píldoras no filtran**: con una activa "
                                    "siguen visibles %d de %d" % (con, total)))
            pg.click("#chips .chip:nth-child(1)")
            pg.wait_for_timeout(450)
            if _contar(pg) != total:
                fallos.append(Fallo("index.html", "R6",
                                    "desactivar la píldora no restaura las tarjetas"))
    pg.close()
    return fallos


def comprobar_grafo(b):
    """El grafo 3D: que cargue y dibuje, sin errores de consola."""
    fallos = []
    ruta_f = os.path.join(RAIZ, "red-actores-3d.html")
    if not os.path.exists(ruta_f):
        return fallos
    pg = b.new_page(viewport={"width": 1280, "height": 900})
    errores = []
    pg.on("pageerror", lambda e: errores.append(str(e)))
    pg.goto("file://" + ruta_f)
    pg.wait_for_timeout(5000)

    if not pg.evaluate("!!document.querySelector('canvas')"):
        fallos.append(Fallo("red-actores-3d.html", "R7",
                            "no se creó ningún lienzo: el grafo no se dibuja"))
    else:
        vacio = pg.evaluate("""() => {
          const c = document.querySelector('canvas');
          return c.width === 0 || c.height === 0;
        }""")
        if vacio:
            fallos.append(Fallo("red-actores-3d.html", "R7",
                                "el lienzo tiene tamaño cero"))
    for e in errores:
        fallos.append(Fallo("red-actores-3d.html", "R3",
                            "error de JavaScript: %s" % e[:150]))
    pg.close()
    return fallos


def ejecutar(anchos=ANCHOS):
    from playwright.sync_api import sync_playwright
    fallos = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        try:
            fallos += comprobar_indice(b, anchos)
            fallos += comprobar_grafo(b)
        finally:
            b.close()
    return fallos


def informar(fallos, silencioso=False):
    if not fallos:
        if not silencioso:
            print("cti_render · todo se ve bien.")
        return 0
    print("cti_render · %d fallo(s) de representación" % len(fallos),
          file=sys.stderr)
    print("╭─ SE VE MAL ────────────────────────────────────────────",
          file=sys.stderr)
    for f in fallos:
        donde = " · %dpx" % f.ancho if f.ancho else ""
        print("│ [%s] %s%s" % (f.regla, f.pagina, donde), file=sys.stderr)
        print("│      %s" % f.mensaje, file=sys.stderr)
    print("╰────────────────────────────────────────────────────────",
          file=sys.stderr)
    return 1


def main():
    ap = argparse.ArgumentParser(
        description="Comprueba en un navegador real que las páginas se ven bien: "
                    "desbordes, scroll horizontal, errores de JavaScript y que "
                    "el filtro del índice filtre de verdad.")
    ap.add_argument("--json", action="store_true", help="salida legible por máquina")
    ap.add_argument("--anchos", help="anchos en píxeles separados por comas")
    a = ap.parse_args()

    if not disponible():
        print("cti_render: Playwright no está instalado; no se comprueba el "
              "render.\n  pip install playwright && playwright install chromium",
              file=sys.stderr)
        return 0

    anchos = ANCHOS
    if a.anchos:
        try:
            anchos = tuple(int(x) for x in a.anchos.split(","))
        except ValueError:
            sys.exit("error: --anchos espera números separados por comas")

    fallos = ejecutar(anchos)
    if a.json:
        print(json.dumps({"fallos": [f.a_dict() for f in fallos]},
                         ensure_ascii=False, indent=1))
        return 1 if fallos else 0
    return informar(fallos)


if __name__ == "__main__":
    sys.exit(main())
