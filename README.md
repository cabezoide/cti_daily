# cti_daily

Informes de ciberinteligencia de producción propia, escritos en Markdown y publicados también como HTML autocontenido. El repositorio se revisa **a diario**: cada informe vivo se vuelve a investigar cuando aparece información nueva, y los agregados de indicadores se reconstruyen desde los informes en cada construcción.

**Publicado en https://cabezoide.github.io/cti_daily** — los informes se leen mejor ahí: el HTML lleva su índice lateral, búsqueda, cronologías filtrables y la matriz ATT&CK navegable.

No es un archivo histórico ni un volcado de *feeds*. Cada documento está escrito para que alguien decida algo: si un párrafo no cambia lo que alguien va a hacer, va al anexo o se borra.

---

## Índice

<!-- AUTO-ÍNDICE: no editar a mano. Lo regenera tools/cti_build.py -->

### Informes

| Informe | Tema | Tipo | Fecha | Ver. | TLP | Vigencia | Formatos |
|---|---|---|---|---|---|---|---|
| `CTI-2026-014` | TheGentlemen (Storm-2697) | Perfil de actor + informe de campaña | 2026-09-15 | 1.2 | `TLP:CLEAR` | vigente · 28 d | [md](CTI-2026-014-thegentlemen.md) · [html](CTI-2026-014-thegentlemen.html) |
| `CTI-2026-015` | Qilin (Agenda · Storm-1934) | Perfil de actor + informe de campaña | 2026-09-16 | 1.1 | `TLP:CLEAR` | vigente · 29 d | [md](CTI-2026-015-qilin.md) · [html](CTI-2026-015-qilin.html) |
| `CTI-2026-016` | LockBit 5.0 (ChuongDong) | Perfil de actor + informe de campaña | 2026-09-16 | 1.1 | `TLP:CLEAR` | vigente · 29 d | [md](CTI-2026-016-lockbit5.md) · [html](CTI-2026-016-lockbit5.html) |
| `CTI-2026-017` | FamousSparrow (SparroWocky) · solapamiento con el ecosistema Sparrow de CopperDragon y con el clúster DarkWire (Check Point) | Perfil de actor + informe de campaña | 2026-09-21 | 1.2 | `TLP:CLEAR` | vigente · 92 d | [md](CTI-2026-017-famoussparrow.md) · [html](CTI-2026-017-famoussparrow.html) |
| `CTI-2026-018` | Abuso de dominios de primer nivel (ecosistema de registro DNS) | Evaluación estratégica | 2026-11-15 | 1.0 | `TLP:CLEAR` | vigente · 90 d | [md](CTI-2026-018-abuso-tld.md) · [html](CTI-2026-018-abuso-tld.html) |
| `CTI-2026-019` | ARTEX (framework ofensivo agéntico) y los clústeres que lo operan | Evaluación estratégica + perfil de capacidad adversaria | 2026-11-16 | 1.0 | `TLP:CLEAR` | vigente · 91 d | [md](CTI-2026-019-artex.md) · [html](CTI-2026-019-artex.html) |
| `CTI-2026-020` | Blind Eagle (APT-C-36 · TAG-144 · AguilaCiega · APT-Q-98) | Perfil de actor + informe de campaña | 2026-11-16 | 1.0 | `TLP:CLEAR` | vigente · 91 d | [md](CTI-2026-020-blindeagle.md) · [html](CTI-2026-020-blindeagle.html) |
| `CTI-2026-021` | Ecosistema de troyanos bancarios brasileños (Mekotio · Mispadu · Grandoreiro · Astaroth · Coyote · VENON) | Perfil de ecosistema de malware + evaluación regional | 2026-11-16 | 1.0 | `TLP:CLEAR` | vigente · 91 d | [md](CTI-2026-021-troyanos-br.md) · [html](CTI-2026-021-troyanos-br.html) |
| `CTI-2026-022` | Red Akodon (SCILabs) · solapamiento con TAG-144 / Blind Eagle / APT-C-36 / AguilaCiega / APT-Q-98 · campañas «Shadow Vector» (Acronis) | Perfil de actor en disputa + evaluación de transferibilidad del método | 2026-11-16 | 1.0 | `TLP:CLEAR` | vigente · 91 d | [md](CTI-2026-022-redakodon.md) · [html](CTI-2026-022-redakodon.html) |
| `CTI-2026-023` | Machete · El Machete · APT-C-43 · Grupo G0095 (MITRE ATT&CK) | Perfil de actor de espionaje + evaluación de vigencia y requisito de colección | 2026-11-16 | 1.0 | `TLP:CLEAR` | vigente · 180 d | [md](CTI-2026-023-machete.md) · [html](CTI-2026-023-machete.html) |
| `CTI-2026-024` | Rhysida (RaaS) · afiliados y actores de acceso asociados: Vanilla Tempest · solapamientos con Vice Society / DEV-0832 e Interlock | Perfil de operación de extorsión + estudio de caso nacional | 2026-11-16 | 1.0 | `TLP:CLEAR` | vigente · 91 d | [md](CTI-2026-024-rhysida.md) · [html](CTI-2026-024-rhysida.html) |
| `CTI-2026-025` | Gamaredon (Armageddon · Primitive Bear · ACTINIUM · Shuckworm · Aqua Blizzard · IRON TILDEN · DEV-0157 · NastyShrew · G0047) | Perfil de actor + evaluación de pertinencia regional | 2026-11-17 | 1.0 | `TLP:CLEAR` | vigente · 60 d | [md](CTI-2026-025-gamaredon.md) · [html](CTI-2026-025-gamaredon.html) |
| `CTI-2026-026` | APT36 · Transparent Tribe · Mythic Leopard · COPPER FIELDSTONE · ProjectM · G0134 | Perfil de actor + evaluación de calidad de la evidencia + transferencia de método a Linux | 2026-11-17 | 1.0 | `TLP:CLEAR` | vigente · 92 d | [md](CTI-2026-026-apt36.md) · [html](CTI-2026-026-apt36.html) |
| `CTI-2026-027` | Mustang Panda · Earth Preta · TA416 · RedDelta · BRONZE PRESIDENT · Stately Taurus · Twill Typhoon · HoneyMyte · TEMP.Hex · TANTALUM · G0129 · (vinculado) UNC6384 | Perfil de actor + evaluación de capacidad y de resiliencia a la acción policial | 2026-11-17 | 1.0 | `TLP:CLEAR` | vigente · 92 d | [md](CTI-2026-027-mustangpanda.md) · [html](CTI-2026-027-mustangpanda.html) |
| `CTI-2026-028` | UNC3886 · Grupo G1048 (MITRE ATT&CK) · campaña C0056 «RedPenguin» | Perfil de actor + evaluación de capacidad adversaria + estudio de caso nacional (Singapur) | 2026-11-17 | 1.0 | `TLP:CLEAR` | vigente · 92 d | [md](CTI-2026-028-unc3886.md) · [html](CTI-2026-028-unc3886.html) |
| `CTI-2026-029` | Sandworm · APT44 · Seashell Blizzard · IRIDIUM · Voodoo Bear · TeleBots · BlackEnergy Group · ELECTRUM · FROZENBARENTS · UAC-0002 · G0034 · (subgrupo) BadPilot | Perfil de actor destructivo + evaluación de recuperabilidad | 2026-11-17 | 1.0 | `TLP:CLEAR` | vigente · 92 d | [md](CTI-2026-029-sandworm.md) · [html](CTI-2026-029-sandworm.html) |
| `CTI-2026-030` | Salt Typhoon · OPERATOR PANDA · RedMike · UNC5807 · GhostEmperor (designaciones que recoge el aviso conjunto AA25-239A) | Perfil de actor + estado de una disputa de alias no resuelta + evaluación de exposición en infraestructura de red | 2026-11-17 | 1.0.3 | `TLP:CLEAR` | vigente · 92 d | [md](CTI-2026-030-salttyphoon.md) · [html](CTI-2026-030-salttyphoon.html) |

### Agregados de indicadores

| Fichero | Indicadores | Tipos incluidos | Informes que aportan |
|---|---|---|---|
| [`ioc_ipv4.txt`](ioc_ipv4.txt) | 302 | `ipv4`, `ip`, `ipv4:puerto` | `CTI-2026-014`, `CTI-2026-015`, `CTI-2026-017`, `CTI-2026-019`, `CTI-2026-020`, `CTI-2026-021`, `CTI-2026-022`, `CTI-2026-023`, `CTI-2026-025`, `CTI-2026-026`, `CTI-2026-028`, `CTI-2026-030` |
| [`ioc_ipv6.txt`](ioc_ipv6.txt) | 2 | `ipv6` | `CTI-2026-030` |
| [`ioc_url.txt`](ioc_url.txt) | 242 | `domain`, `url`, `fqdn`, `hostname` | `CTI-2026-017`, `CTI-2026-018`, `CTI-2026-019`, `CTI-2026-020`, `CTI-2026-021`, `CTI-2026-022`, `CTI-2026-023`, `CTI-2026-024`, `CTI-2026-025`, `CTI-2026-026` |
| [`ioc_hash.txt`](ioc_hash.txt) | 343 | `md5`, `sha1`, `sha256`, `sha512`, `imphash` | `CTI-2026-014`, `CTI-2026-015`, `CTI-2026-016`, `CTI-2026-017`, `CTI-2026-019`, `CTI-2026-020`, `CTI-2026-021`, `CTI-2026-022`, `CTI-2026-023`, `CTI-2026-024`, `CTI-2026-025`, `CTI-2026-026`, `CTI-2026-030` |
| [`ioc_index.csv`](ioc_index.csv) | 1646 | todos: `appid`, `artefacto`, `asn`, `asunto`, `clave`, `cve`, `domain`, `email`, `filename`, `filepath`, `fqdn`, `herramienta`, `ipv4`, `ipv4:puerto`, `ipv6`, `md5`, `mutex`, `path`, `pattern`, `puerto`, `servicio`, `sha1`, `sha256`, `url`, `useragent` | `CTI-2026-014`, `CTI-2026-015`, `CTI-2026-016`, `CTI-2026-017`, `CTI-2026-018`, `CTI-2026-019`, `CTI-2026-020`, `CTI-2026-021`, `CTI-2026-022`, `CTI-2026-023`, `CTI-2026-024`, `CTI-2026-025`, `CTI-2026-026`, `CTI-2026-027`, `CTI-2026-028`, `CTI-2026-029`, `CTI-2026-030` |

### Estado del ciclo

| Métrica | Valor |
|---|---|
| Informes publicados | 17 |
| Indicadores en listas planas | 889 |
| Indicadores en el índice con contexto | 1646 |
| Caducados (exigen revisión) | 0 |
| Por caducar en 14 días | 0 |
| Informe más reciente | 2026-11-17 |
| Nodos del mapa de relaciones | 132, con 156 relaciones — [`red-actores-3d.html`](red-actores-3d.html) |

<!-- FIN AUTO-ÍNDICE -->

---

## Mapa de relaciones

**[`red-actores-3d.html`](red-actores-3d.html)** — mapa tridimensional navegable de las
relaciones entre los actores y las herramientas de esta cartera: actores estatales,
clústeres, suministradores, herramientas propias, herramientas públicas, servicios
legítimos abusados y vulnerabilidades. Se gira con el ratón, se filtra por tipo y cada
nodo abre una ficha con su descripción y un enlace al informe de origen. El recuento vivo
está en el índice de más arriba.

Es HTML autocontenido, **sin dependencias externas ni red**: la disposición se calcula en
el navegador con un algoritmo de fuerzas en tres dimensiones y semilla fija, de modo que el
mapa sale idéntico en cada carga.

**No se edita a mano.** La fuente es [`red-actores.json`](red-actores.json) —nodos,
relaciones y la descripción de cada ficha— y `tools/cti_build.py` lo regenera en cada
construcción junto con la portada y los agregados. La construcción comprueba además que
cada nodo apunte a un informe que existe, y **avisa de los informes que todavía no están
en el grafo**: las relaciones son juicios del analista y no se extraen solas de la prosa,
así que lo que el constructor puede hacer es no dejar que el hueco pase inadvertido.

> **Lo que el mapa distingue, y es su razón de ser.** Las relaciones no son todas iguales,
> y tratarlas como si lo fueran es la fuente de error más frecuente de esta disciplina. El
> mapa dibuja con **trazo continuo** lo que está establecido —*usa*, *suministra a*,
> *explota*, *entrega acceso a*— y con **trazo discontinuo** lo que no: *solapamiento
> parcial*, *vinculado a*, *identidad en disputa* y *NO es el mismo que*. Tres informes de
> esta cartera existen porque alguien compuso un solapamiento parcial con una equivalencia:
> `CTI-2026-017`, `CTI-2026-022` y `CTI-2026-030`.

---

## Marcado y condiciones de uso

Todo lo publicado aquí está marcado **`TLP:CLEAR`**: puede redistribuirse sin restricción, conservando la atribución de las fuentes y las salvedades metodológicas de cada informe. La mayoría conserva **`PAP:AMBER`**, y eso sí impone una condición: los indicadores llevan una **acción permitida individual** en el Anexo A de su informe, y no todos admiten bloqueo.

> **Lea esto antes de cargar un `ioc_*.txt` en un bloqueo.**
> Los cuatro ficheros de texto son listas planas, sin contexto por diseño, y eso
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
>
> Sobre `ioc_hash.txt` en particular: agrupa md5, sha1 y sha256 en un solo fichero,
> ordenados por algoritmo según su longitud, porque es lo que esperan la mayoría de
> las plataformas de ingesta. Conviene recordar que un hash solo detecta la muestra
> exacta: contra los actores cuyo empaquetador se automuta en cada ejecución —y este
> repositorio documenta al menos uno— su valor preventivo es nulo y sirven únicamente
> para búsqueda retrospectiva. La columna `accion_permitida` del CSV lo dice fichero
> por fichero.

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
ioc_hash.txt
ioc_index.csv              los mismos indicadores con contexto, confianza y acción permitida
index.html                 portada de GitHub Pages, generada; editarla a mano no sirve
.nojekyll                  desactiva Jekyll: las páginas se sirven tal cual, sin procesar
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

## Publicación

El repositorio se sirve con GitHub Pages desde la rama `main`, directorio raíz, en
**https://cabezoide.github.io/cti_daily**. No hay paso de compilación: los informes ya son
HTML autocontenido —sin CDN, sin fuentes remotas, sin una sola petición a terceros— y se
publican tal cual.

Dos detalles que conviene no deshacer:

- **`.nojekyll`** desactiva el procesado de Jekyll. Sin él, GitHub intentaría convertir los
  `.md` a HTML con su plantilla por omisión, y quedarían dos versiones del mismo informe
  compitiendo: una renderizada por nosotros con el sistema de diseño y otra por Jekyll sin
  él. Con el fichero presente, los `.md` se sirven como fuente y los `.html` como lo que son.
- **`index.html` la genera el constructor**, no se escribe a mano, por la misma razón que el
  índice de este README: un listado mantenido a mano miente en cuanto se añade un informe.

Los agregados de indicadores quedan accesibles como URL estables, utilizables directamente
desde un proceso de ingesta:

```bash
curl -s https://cabezoide.github.io/cti_daily/ioc_index.csv
curl -s https://cabezoide.github.io/cti_daily/ioc_ipv4.txt
curl -s https://cabezoide.github.io/cti_daily/ioc_hash.txt
```

GitHub Pages sirve con una caché de unos diez minutos, de modo que un cambio tarda ese orden
de tiempo en verse.

### Indexación por buscadores

Publicar en Pages hace el contenido indexable, lo que es coherente con `TLP:CLEAR` para los
informes —se quiere que se encuentren— pero no para los agregados de indicadores, que fuera
de contexto se convierten en listas de bloqueo sin las salvedades que los acompañan.

Hay un [`robots.txt`](robots.txt) con las reglas que corresponden, y conviene saber que
**mientras el sitio viva en una subcarpeta no surte efecto**: esto es una *project page*
servida en `cabezoide.github.io/cti_daily/`, y los rastreadores solo leen el `robots.txt`
de la raíz del host, `cabezoide.github.io/robots.txt`. Esa raíz la sirve un repositorio
distinto, `cabezoide.github.io`, que hoy no existe.

Para que las reglas se apliquen de verdad hay dos caminos:

1. **Crear el repositorio `cabezoide.github.io`** con un `robots.txt` que contenga estas
   mismas directivas. Tiene un efecto colateral que conviene decidir a conciencia: ese
   repositorio publica además el sitio raíz de la cuenta.
2. **Poner un dominio propio** en los ajustes de Pages del repositorio. El sitio pasaría a
   servirse en la raíz de ese dominio y el `robots.txt` de este repositorio empezaría a
   leerse —quitando entonces el prefijo `/cti_daily/` de las rutas—.

Y en ningún caso es un control de acceso: `robots.txt` es una convención voluntaria que
solo evita la aparición en resultados de búsqueda. Quien quiera descargar estos ficheros
podrá, y debe poder: son `TLP:CLEAR`. La mitigación que no depende de la buena voluntad de
nadie es que el contexto viaje con el dato, y para eso está `ioc_index.csv`.

## Método

Los informes se organizan por **niveles de consumo** —estratégico, operacional, táctico y técnico— y aplican, de forma explícita y auditable:

- lenguaje estimativo según **ICD 203**: probabilidad y confianza se declaran por separado y nunca se mezclan;
- valoración de fuentes con el **código Admiralty**, fiabilidad de la fuente y credibilidad de la información por separado;
- **MITRE ATT&CK** para los procedimientos, **Pirámide del Dolor** para priorizar el esfuerzo de detección;
- análisis de hipótesis competidoras, supuestos clave y *pre-mortem*, con las hipótesis descartadas consignadas para que no se reabran;
- declaración explícita de las **limitaciones de la colección** y de las brechas de inteligencia, incluido cuando una sección queda sin evaluar por falta de telemetría propia.

Esa última costumbre es deliberada: un informe que no dice lo que no sabe es un informe que no se puede usar para decidir.
