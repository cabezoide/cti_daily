# cti_daily

Informes de ciberinteligencia de producción propia, escritos en Markdown y publicados también como HTML autocontenido. El repositorio se revisa **a diario**: cada informe vivo se vuelve a investigar cuando aparece información nueva, y los agregados de indicadores se reconstruyen desde los informes en cada construcción.

No es un archivo histórico ni un volcado de *feeds*. Cada documento está escrito para que alguien decida algo: si un párrafo no cambia lo que alguien va a hacer, va al anexo o se borra.

---

## Índice

<!-- AUTO-ÍNDICE: no editar a mano. Lo regenera tools/cti_build.py -->

### Informes

| Informe | Tema | Tipo | Fecha | Ver. | TLP | Vigencia | Formatos |
|---|---|---|---|---|---|---|---|
| `CTI-2026-014` | TheGentlemen (Storm-2697) | Perfil de actor + informe de campaña | 2026-09-15 | 1.2 | `TLP:CLEAR` | vigente · 29 d | [md](CTI-2026-014-thegentlemen.md) · [html](CTI-2026-014-thegentlemen.html) |
| `CTI-2026-015` | Qilin (Agenda · Storm-1934) | Perfil de actor + informe de campaña | 2026-09-16 | 1.1 | `TLP:CLEAR` | vigente · 30 d | [md](CTI-2026-015-qilin.md) · [html](CTI-2026-015-qilin.html) |
| `CTI-2026-016` | LockBit 5.0 (ChuongDong) | Perfil de actor + informe de campaña | 2026-09-16 | 1.1 | `TLP:CLEAR` | vigente · 30 d | [md](CTI-2026-016-lockbit5.md) · [html](CTI-2026-016-lockbit5.html) |
| `CTI-2026-017` | FamousSparrow (SparroWocky) | Perfil de actor + informe de campaña | 2026-09-21 | 1.1 | `TLP:CLEAR` | vigente · 35 d | [md](CTI-2026-017-famoussparrow.md) · [html](CTI-2026-017-famoussparrow.html) |
| `CTI-2026-018` | Abuso de dominios de primer nivel (ecosistema de registro DNS) | Evaluación estratégica | 2026-11-15 | 1.0 | `TLP:CLEAR` | vigente · 91 d | [md](CTI-2026-018-abuso-tld.md) · [html](CTI-2026-018-abuso-tld.html) |
| `CTI-2026-019` | ARTEX (framework ofensivo agéntico) y los clústeres que lo operan | Evaluación estratégica + perfil de capacidad adversaria | 2026-11-16 | 1.0 | `TLP:CLEAR` | vigente · 92 d | [md](CTI-2026-019-artex.md) · [html](CTI-2026-019-artex.html) |

### Agregados de indicadores

| Fichero | Indicadores | Tipos incluidos | Informes que aportan |
|---|---|---|---|
| [`ioc_ipv4.txt`](ioc_ipv4.txt) | 56 | `ipv4`, `ip`, `ipv4:puerto` | `CTI-2026-014`, `CTI-2026-015`, `CTI-2026-017`, `CTI-2026-019` |
| [`ioc_ipv6.txt`](ioc_ipv6.txt) | 0 | `ipv6` | — |
| [`ioc_url.txt`](ioc_url.txt) | 28 | `domain`, `url`, `fqdn`, `hostname` | `CTI-2026-017`, `CTI-2026-018`, `CTI-2026-019` |
| [`ioc_index.csv`](ioc_index.csv) | 193 | todos: `appid`, `artefacto`, `asn`, `cve`, `domain`, `filename`, `filepath`, `herramienta`, `ipv4`, `ipv4:puerto`, `md5`, `mutex`, `path`, `pattern`, `puerto`, `sha1`, `sha256`, `url`, `useragent` | `CTI-2026-014`, `CTI-2026-015`, `CTI-2026-016`, `CTI-2026-017`, `CTI-2026-018`, `CTI-2026-019` |

### Estado del ciclo

| Métrica | Valor |
|---|---|
| Informes publicados | 6 |
| Indicadores en listas planas | 84 |
| Indicadores en el índice con contexto | 193 |
| Caducados (exigen revisión) | 0 |
| Por caducar en 14 días | 0 |
| Última construcción | 2026-11-16 |

<!-- FIN AUTO-ÍNDICE -->

---

## Marcado y condiciones de uso

Todo lo publicado aquí está marcado **`TLP:CLEAR`**: puede redistribuirse sin restricción, conservando la atribución de las fuentes y las salvedades metodológicas de cada informe. La mayoría conserva **`PAP:AMBER`**, y eso sí impone una condición: los indicadores llevan una **acción permitida individual** en el Anexo A de su informe, y no todos admiten bloqueo.

> **Lea esto antes de cargar un `ioc_*.txt` en un bloqueo.**
> Los tres ficheros de texto son listas planas, sin contexto por diseño, y eso
> significa que **pierden la confianza, la caducidad y la acción permitida** de
> cada indicador. En ellos conviven direcciones de mando y control que deben
> bloquearse con infraestructura compartida, servicios legítimos de terceros y
> direcciones de nube reasignables que sólo sirven para búsqueda retrospectiva.
> Cargarlos sin filtrar provocará cortes de servicio propios.
>
> Para eso está [`ioc_index.csv`](ioc_index.csv): los mismos indicadores **más
> todos los demás tipos** —hashes, nombres de fichero, agentes de usuario,
> identificadores de aplicación, ASN, CVE, mutex—, cada uno con su informe de
> origen, su fecha, su marcado TLP y PAP, su confianza, su caducidad cuando el
> informe la declara, la acción que el analista autorizó y el contexto que
> explica por qué está en la lista. Es el fichero que debe ingerir una
> plataforma de inteligencia; los `.txt` son para cuando ya se ha decidido qué
> hacer con cada cosa.
>
> Una columna merece atención especial: `accion_permitida`. Dice `Bloqueo`,
> `Solo retrohunt`, `No bloquear — herramienta legítima` y otras variantes
> escritas por quien analizó el indicador. Filtrar por ella antes de actuar es
> la diferencia entre usar esto bien y provocar una interrupción.

Los informes marcados `TLP:AMBER` o superior **no se publican en este repositorio** y aparecen en el índice como *no publicados*. La exclusión está implementada en el propio constructor (`TLP_PUBLICABLE` en `tools/cti_build.py`), de modo que un informe restringido que se añada mañana queda fuera —y fuera de los agregados de IOC— sin depender de que alguien se acuerde.

---

## El ciclo diario

El ciclo tiene dos mitades y conviene no confundirlas, porque sólo una se puede automatizar del todo.

**La mitad determinista** la hace `tools/cti_build.py`. No toca la red:

```bash
python3 tools/cti_build.py            # construye y escribe
python3 tools/cti_build.py --check    # no escribe; sale 1 si algo está sin regenerar
python3 tools/cti_build.py --force    # regenera todos los HTML
python3 tools/cti_build.py --json     # estado de vigencia en JSON
```

1. Regenera el HTML de todo informe cuyo `.md` sea más reciente.
2. Regenera el índice de este README entre las marcas `AUTO-ÍNDICE`.
3. Regenera `ioc_ipv4.txt`, `ioc_ipv6.txt` e `ioc_url.txt` desde las tablas `cti:ioc` de los informes publicables.
4. Imprime el **estado de vigencia** de cada informe, comparando su campo `caduca` con la fecha de hoy.

Ese cuarto punto es el que mueve el ciclo: un informe caducado o a menos de catorce días de caducar es un informe que hay que volver a investigar hoy.

**La mitad que exige criterio** es la investigación. Ningún script puede decidir si hay información nueva sobre un actor, si una fuente nueva corrobora o contradice un juicio, o si un indicador sigue vivo. Eso lo hace un analista —o un agente con acceso a fuentes— leyendo el informe, revisando sus fuentes y, si hay algo nuevo:

- actualiza el `.md`, que es la fuente única;
- sube la versión en el *frontmatter* y en la cabecera de control;
- añade la fila correspondiente al Anexo de control de cambios, diciendo **qué juicio cambió**, no sólo que hubo cambios;
- y vuelve a ejecutar el constructor.

Un informe que se reemite sin que ningún juicio haya cambiado no necesita versión nueva: necesita que se revise su fecha de caducidad.

---

## Cómo se escribe un informe

El `.md` es la fuente. El HTML se genera; nadie mantiene dos versiones del mismo documento.

```bash
cp plantilla-informe-cti-v2.md CTI-2026-020-nuevo.md
# ...escribir...
python3 render/cti_render.py CTI-2026-020-nuevo.md
python3 tools/cti_build.py
```

Todo lo que activa un componente visual es un comentario HTML (`<!-- cti:algo -->`), invisible al leer el Markdown en cualquier visor. Si se borra una directiva, ese bloque sale como tabla o párrafo normal: el informe nunca se rompe por una directiva mal puesta. La referencia completa está en [`render/LEEME.md`](render/LEEME.md).

El tema visual vive en [`render/cti_theme.css`](render/cti_theme.css) y se aplica a todos los informes. Retocarlo cambia el aspecto de todos a la siguiente construcción.

---

## Estructura

```
CTI-2026-0NN-*.md          informes — la fuente
CTI-2026-0NN-*.html        informes renderizados, autocontenidos (sin red, sin CDN)
ioc_ipv4.txt               listas planas de indicadores, para ingesta automática
ioc_ipv6.txt
ioc_url.txt
ioc_index.csv              los mismos indicadores con contexto, confianza y acción permitida
plantilla-informe-cti-v2.md   plantilla vigente
plantilla-informe-cti.md      plantilla v1, conservada por referencia
render/cti_render.py       Markdown → HTML, sólo biblioteca estándar
render/cti_theme.css       sistema de diseño
render/LEEME.md            referencia de directivas
tools/cti_build.py         construcción, índice, agregados y vigencia
.githooks/pre-commit       mantiene los artefactos derivados al día en cada commit
```

Para que el *hook* funcione en un clon nuevo, una sola vez:

```bash
git config core.hooksPath .githooks
```

---

## Método

Los informes se organizan por **niveles de consumo** —estratégico, operacional, táctico y técnico— y aplican, de forma explícita y auditable:

- lenguaje estimativo según **ICD 203**: probabilidad y confianza se declaran por separado y nunca se mezclan;
- valoración de fuentes con el **código Admiralty**, fiabilidad de la fuente y credibilidad de la información por separado;
- **MITRE ATT&CK** para los procedimientos, **Pirámide del Dolor** para priorizar el esfuerzo de detección;
- análisis de hipótesis competidoras, supuestos clave y *pre-mortem*, con las hipótesis descartadas consignadas para que no se reabran;
- declaración explícita de las **limitaciones de la colección** y de las brechas de inteligencia, incluido cuando una sección queda sin evaluar por falta de telemetría propia.

Esa última costumbre es deliberada: un informe que no dice lo que no sabe es un informe que no se puede usar para decidir.
