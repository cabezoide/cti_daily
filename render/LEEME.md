# El par `.md` ↔ `.html`

El informe se escribe **una sola vez**, en Markdown. El HTML se genera desde él.
Nadie mantiene dos versiones del mismo documento.

```bash
python3 render/cti_render.py CTI-2026-014-thegentlemen.md
# → CTI-2026-014-thegentlemen.html

python3 render/cti_render.py informe.md -o /ruta/salida.html
```

Sin dependencias: solo Python 3.8+ de serie. La salida es **un único archivo
autocontenido** (CSS y JS incrustados), apto para adjuntar en un correo o
guardar en un repositorio con marcado TLP sin llamar a ningún servidor externo.

## El pacto

1. **El `.md` manda.** Es la fuente. Se versiona, se revisa por pares, se
   difunde en texto plano si hace falta.
2. **El `.md` sigue siendo un `.md`.** Todo lo que activa un componente visual
   es un comentario HTML (`<!-- cti:algo -->`), invisible en GitHub, Obsidian,
   VS Code o `pandoc`.
3. **Degradación elegante.** Si una directiva no encaja con el bloque que la
   sigue, ese bloque sale como tabla o párrafo normal y se avisa por `stderr`.
   El informe nunca se rompe por una directiva mal puesta.
4. **El diseño no se duplica.** El tema se extrae del HTML de referencia
   (`CTI-2026-014-thegentlemen.html`). Retocar el `<style>` de ese archivo
   cambia el aspecto de todos los informes futuros. También puedes pasar
   `--theme mi-tema.css`.

## Lo que el renderizador hace solo, sin que le digas nada

| En el Markdown | En el HTML |
|---|---|
| Frontmatter (`id`, `tlp`, `pap`, `actor`, `caduca`…) | Barra superior, portada, rejilla de metadatos y pie |
| `# TÍTULO` + `##` + `###` al principio | Portada con escena 3D de propagación en malla |
| `# NIVEL ESTRATÉGICO` (u Operacional / Táctico / Técnico / Anexos) | Divisor a todo ancho con el color del nivel, y grupo propio en el índice |
| `### Para: … · Horizonte: …` bajo un `# NIVEL` | Línea de destinatarios del nivel |
| `## E-4. Título` | Sección con chapa `E-4` coloreada según el prefijo (E/O/T/X) |
| Primer párrafo corto de una sección | Subtítulo de la sección (desactívalo con `--no-leads`) |
| `> texto` | Nota lateral. El emoji inicial elige el tono: `⚠` ámbar · `✅` verde · `⬛` gris · sin emoji, azul |
| `> **Título.** cuerpo` | Nota con su título en versalitas |
| Tabla con columna *Confianza*, *Prioridad*, *Plazo*, *Fiabilidad*, *Severidad*… | Esos valores salen como píldoras de color |
| ```` ```kql ````, ```` ```powershell ````, ```` ```yaml ```` | Bloque con resaltado y botón *copiar* |
| Todo el documento | Índice lateral con scrollspy, barra de progreso, atajo `/` para buscar, estilos de impresión |

## Directivas

Se escriben en su propia línea, **justo antes** del bloque que transforman.

| Directiva | Espera | Produce |
|---|---|---|
| `<!-- cti:meta -->` | Tabla `Campo \| Valor` | Rejilla de metadatos de la cabecera de control |
| `<!-- cti:kj -->` | Párrafos que empiezan por `**KJ-n.**` | Tarjetas de juicio con medidor de probabilidad y pie de confianza/base |
| `<!-- cti:stats -->` | Tabla `Cifra \| Qué mide \| Contexto` | Tarjetas de cifra con contador animado |
| `<!-- cti:bars -->` | Tabla `Etiqueta \| Valor` | Barras horizontales proporcionales |
| `<!-- cti:chart -->` | Tabla `Periodo \| Valor` | Gráfico de línea SVG con área y puntos |
| `<!-- cti:cards -->` | Tabla `Título \| Texto \| Etiqueta` | Tarjetas en rejilla |
| `<!-- cti:timeline -->` | Tabla `Fecha \| Hecho \| Traza` | Cronología con filtros por traza |
| `<!-- cti:stages -->` | Tabla `Etapa \| Título \| Elementos` | Cadena de intrusión en tres etapas |
| `<!-- cti:matrix -->` | Tabla `Táctica \| ID \| Técnica \| Procedimiento` | Matriz ATT&CK agrupada y buscable |
| `<!-- cti:pyramid -->` | Tabla `Nivel \| Descripción \| Valor` | Pirámide del Dolor en 3D, rotable y clicable |
| `<!-- cti:accordion -->` | Párrafos `**H-n — Título.** cuerpo` | Acordeón de hipótesis de caza |
| `<!-- cti:detections -->` | `**D-n · CRÍTICO — Nombre**` + bloque de código + `→ acción` | Tarjetas de detección por severidad |
| `<!-- cti:ioc -->` | Tabla `Tipo \| Valor \| Contexto \| … \| Acción` | Lista de indicadores buscable, con copia al pulsar |
| `<!-- cti:table -->` | Tabla | Tabla normal, con opciones |

### Argumentos

Se escriben como `clave="valor"` dentro de la directiva:

| Argumento | En | Para qué |
|---|---|---|
| `title="…"` | `bars`, `chart`, `stages` | Encabezado del componente |
| `cap="…"` | `chart` | Nota bajo el título (fuente, salvedad metodológica) |
| `dwell="…"` | `stages` | Franja inferior de la cadena: tiempos de permanencia |
| `dwell="next"` | `stages` | Toma esa franja del párrafo que sigue a la tabla y lo consume — así el dato sigue visible al leer el `.md` en plano, sin salir dos veces en el HTML |
| `highlight="regex"` | `table` | Resalta en ámbar las filas que casen (útil para el eje regional) |
| `color="…"` | `stats`, `bars` | Color fijo, o lista separada por comas |
| `critical="regex"` `regional="regex"` | `accordion` | Qué hipótesis se marcan como críticas y cuáles como regionales |
| `type="warn\|good\|gap\|info"` | `<!-- cti:note type="warn" -->` antes de un `>` | Fuerza el tono de la nota cuando la cita no lleva emoji |
| `id="…"` | antes de un `##` | Fija el ancla de la sección (por defecto se deriva del título) |

### Convenciones de escritura que el renderizador entiende

- **Juicios clave.** `**KJ-1.** Afirmación… Valoramos **muy probable** *(80–95 %)*. **Confianza: alta.** *Base:* …`
  El medidor toma el porcentaje si está, y si no, el término del Anexo C. La
  primera frase se convierte en el titular de la tarjeta; `*Base:*` va al pie.
- **Hitos de cronología.** Pon en `**negrita**` la fecha o el hecho y el evento
  se marca como hito, con filtro propio.
- **Trazas de cronología.** La tercera columna es el filtro. Si contiene
  «Chile», «LATAM» o «regional», el evento se colorea en ámbar.
- **Etiquetas de gráfico.** La primera columna de `cti:chart` es el eje X: usa
  etiquetas cortas («Ene», «Feb·26»). Por encima de 13 caracteres se recortan
  para que no se solapen, y el recorte no siempre elige bien.
- **Medidor de los juicios.** Sale del rango `(80–95 %)` o del término del
  Anexo C. Un porcentaje suelto en mitad del texto no cuenta como probabilidad
  estimativa — si quieres medidor, escribe el término o el rango.
- **Detecciones.** El formato `**D-4 · CRÍTICO — Argumentos del cifrador**`
  fija identificador, severidad y nombre. La línea que empieza por `→` es la
  acción de respuesta.

## Migrar un informe ya escrito

Un `.md` sin ninguna directiva se renderiza entero y correcto: encabezados,
tablas, listas, citas y código. Las directivas se añaden después, una a una,
donde aporten. Es un camino incremental, no una reescritura.

Para convertir `CTI-2026-014` en el HTML hecho a mano bastan ~12 directivas:
`meta` en §0, `kj` en §1, `cards` y `stats` en §2, `bars` en E-2, `chart` en
E-3, `timeline` en O-6, `stages` en T-1, `matrix` en T-2, `pyramid` en T-3,
`accordion` en T-4, `detections` en X-5 e `ioc` en el Anexo A.

## Comprobar el resultado

```bash
python3 -c "
from html.parser import HTMLParser
import sys
class P(HTMLParser):
    def __init__(s): super().__init__(); s.st=[]; s.err=0
    def handle_starttag(s,t,a):
        if t not in {'br','img','input','meta','link','hr','col','source'}: s.st.append(t)
    def handle_endtag(s,t):
        if s.st and s.st[-1]==t: s.st.pop()
        elif t in s.st:
            while s.st and s.st.pop()!=t: s.err+=1
p=P(); p.feed(open(sys.argv[1],encoding='utf-8').read())
print('etiquetas sin cerrar:', len(p.st), '| desajustes:', p.err)
" informe.html
```

## Si algo no sale como esperabas

- El renderizador avisa por `stderr`: `aviso: cti:matrix no pudo construirse (…)`.
  Casi siempre es que la tabla no tiene las columnas que esa directiva espera.
- Las columnas se localizan **por nombre** en `matrix` (Táctica, ID, Técnica,
  Procedimiento) y **por posición** en el resto.
- Una directiva sin bloque detrás, o seguida de un encabezado, simplemente se
  descarta.
