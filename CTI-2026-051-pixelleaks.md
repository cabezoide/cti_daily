---
tlp: "TLP:CLEAR"
pap: "PAP:WHITE"
id: "CTI-2026-051"
version: "1.0"
tipo: "Perfil de operación de extorsión"
foco_regional: "Global · México · Latinoamérica"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "PixelLeaks · Pixelleaks"
fecha: "2026-11-19"
caduca: "2027-01-19"
autor: "Célula CTI"
distribucion: "Elaborado con fuentes abiertas y con medición propia sobre la interfaz pública de consulta de un rastreador de sitios de filtración. No se reproduce ningún nombre de víctima: sus reclamaciones no están confirmadas por ninguna de ellas. Difusión libre, conservando la atribución y las salvedades de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-051

## PixelLeaks no publica ni una captura de pantalla en sus 34 entradas, y escribe como un regulador en lugar de como un extorsionador

### Hallazgo propio: cero prueba visual y la especificidad descriptiva más alta del lote — recuentos de registros tabla por tabla · y la mayor proporción de víctimas latinoamericanas de los actores nuevos

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-051` |
| Versión | 1.0 — 2026-11-19 |
| Clasificación | `TLP:CLEAR` · **`PAP:WHITE`** — sin indicadores accionables |
| Objeto | **`PixelLeaks`**, segundo puesto del ranking de siete días que motiva esta serie. **Dieciséis días de existencia observada** |
| Foco regional | **3 víctimas mexicanas de 34 (8,8 %): la mayor proporción latinoamericana de los seis actores nuevos del lote.** Una de ellas con plazo declarado al 22 de noviembre de 2026 |
| Lo que lo distingue en este lote | **Cero capturas de pantalla en 34 entradas** —único en el lote— **y a la vez la especificidad descriptiva más alta**: recuentos de registros tabla por tabla, con cifras de seis y siete dígitos |
| Y su rasgo más propio | **El registro con que escribe**: «esta divulgación se refiere a un conjunto verificado de registros de…». **Imita una notificación de brecha, no una nota de rescate** |
| Horizonte | Estratégico 3–6 meses |
| Origen de los datos | **Medición propia** sobre 34 registros, más cuatro fuentes externas |
| Caducidad | **2027-01-19 (60 días)** |
| Autor | Célula CTI |

<!-- cti:note type="warn" -->

> ⚠ **Cuatro advertencias.**
>
> 1. **Dieciséis días de existencia observada**, desde el 3 de noviembre de
>    2026. Nada de lo que sigue es un patrón establecido.
> 2. **Ninguna de sus víctimas ha confirmado nada**, y el rastreador marca al
>    actor como emergente con advertencia expresa de tratar sus reclamaciones
>    con cautela.
> 3. **Los recuentos no concuerdan**: nosotros medimos 34 entradas, un
>    proveedor cuenta 23 víctimas nombradas, y el rastreador declara 27 en el
>    mes. También discrepan en la fecha de su primera víctima: 3 u 9 de
>    noviembre.
> 4. **Hay una reclamación activa contra una organización mexicana con plazo
>    declarado al 22 de noviembre de 2026.** Este informe **no la nombra**
>    —regla de `CTI-2026-048` `E-4`— pero el dato de que existe es relevante
>    para quien opere en ese país (`E-4.1`).

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** **Es el único actor del lote que no ofrece ninguna prueba visual: cero capturas de pantalla en sus 34 entradas.** Para contraste, en el mismo conjunto de datos y el mismo día: `n0n` tiene 259 de 259, `Vortex` 35 de 35 y `settra` 113 de 116. Valoramos **casi con certeza** *(≥99 %)* el dato. **Confianza: alta.** *Consecuencia:* **su catálogo descansa enteramente en la palabra escrita**, y eso es inusual en un ecosistema donde la imagen de un árbol de ficheros es la moneda de credibilidad corriente.

**KJ-2.** **Y compensa esa ausencia con la especificidad descriptiva más alta del lote: describe el material por tablas y con recuentos exactos.** Una de sus entradas detalla, para una plataforma de pagos de un país africano, **818.849 transacciones de monedero de cliente, 7.630.625 detalles de transacción, 428.587 registros de libro de comisiones y 343.229 registros de saldo de servicio**. Otra describe **copias de seguridad completas de las veintiuna bases de datos de clientes** de una plataforma de gestión de licencias. Valoramos **muy probable** *(80–95 %)* que ese nivel de detalle —estructura de tablas y cardinalidades— **sea difícil de inventar sin haber tenido acceso al esquema**. **Confianza: moderada-alta.** *En la escala de `CTI-2026-048` `Anexo D` opera en el nivel 5 —inventario descriptivo— sin pasar por el 3, que es exactamente el revés de `Vortex`.*

**KJ-3.** **El hallazgo propio de este informe es el registro con que escribe, y no es un detalle de estilo: define a quién va dirigido.** Sus entradas empiezan con fórmulas del tipo «esta divulgación se refiere a un conjunto **verificado** de registros de…» y describen el material como «programado para publicación». **No hay amenaza, no hay insulto, no hay precio, no hay plazo en la prosa.** Es el registro de un aviso regulatorio o de una notificación de brecha. Valoramos **probable** *(55–80 %)* que la audiencia buscada **no sea el departamento de TI de la víctima sino sus clientes, sus reguladores y la prensa**, porque ése es el único público para el que ese tono funciona mejor que una amenaza. **Confianza: moderada** — es interpretación nuestra sobre material público, y **ninguna fuente externa lo describe** (`Anexo D`).

**KJ-4.** **No es un programa de afiliados ni una operación de ransomware: no tiene malware, ni manifiesto, ni reglas, ni aviso de reclutamiento.** Una fuente lo señala expresamente, y el rastreador no le registra ninguna herramienta ni ninguna TTP. Valoramos **muy probable** *(80–95 %)* que se trate de **extorsión por datos sin cifrado**, operada por un equipo reducido o una persona. **Confianza: moderada-alta.** *Consecuencia:* como en `CTI-2026-048` y `050`, **la copia de seguridad no defiende de nada** y la medida que vale es el control de egreso y la identidad.

**KJ-5.** **Y su dato regional es el más relevante de los actores nuevos: tres víctimas mexicanas de 34, el 8,8 %, con una reclamación activa y plazo al 22 de noviembre de 2026.** Es la proporción latinoamericana más alta de los seis actores nuevos del lote —por delante de `settra` (4,3 %), `n0n` (4,2 %) y de `Vortex` y `curious worm` (0 %)— aunque en términos absolutos sean tres casos. Valoramos **moderada** la confianza, con la salvedad de que **diez de sus 34 entradas no tienen país asignado**, de modo que la proporción real podría ser distinta. *Consecuencia:* **para una organización mexicana este actor no es ruido del ranking: hay una reclamación con fecha** (`E-4.1`).

**KJ-6.** **Publica todo con la fecha del día: el 100 % de sus entradas tiene la fecha de ataque igual a la de publicación.** De 34 registros, **los 34**. Sólo `curious worm` comparte esta propiedad en el lote, y es su opuesto exacto `settra`, con el 0 %. Valoramos **casi con certeza** *(≥99 %)* el dato. **Confianza: alta.** *Lectura, y hay que dar las dos:* o el actor **no declara cuándo ocurrió el acceso** —lo que priva a la víctima del único dato que le permitiría comprobarlo—, o **el rastreador le asigna la fecha de publicación por omisión** al no encontrar otra. **Para el lector el efecto es el mismo: no hay ventana temporal que comprobar** (`G-2`).

**KJ-7.** **Los recuentos no concuerdan entre fuentes, y la discrepancia es del 48 %.** Nosotros medimos **34 entradas**; un proveedor cuenta **23 víctimas nombradas**; el rastreador declara **27 en el mes**. Y discrepan también en la fecha de la primera víctima: **3 de noviembre** según el rastreador, **9 de noviembre** según el proveedor. Valoramos **casi con certeza** *(≥99 %)* que las tres cifras sean correctas para su método y su momento. **Confianza: alta.** *Y la lectura más probable de la diferencia entre 34 y 23 es precisamente `KJ-1` y la ausencia de dominio en 21 de las 34 entradas:* **un recuento de «víctimas nombradas» excluye lo que no se puede nombrar.**

**KJ-8.** **Hay un indicio de vector, débil pero es el único que existe para este actor: dos de veintitrés víctimas tenían credenciales de empleado filtradas en los doce meses anteriores a su publicación.** Es el 8,7 %, según un proveedor que además **declara expresamente que no sabe si esas credenciales fueron la vía de acceso**. Valoramos **poco probable** *(20–45 %)* que esa correlación establezca el vector, y **probable** *(55–80 %)* que el credencial robado sea **una** de sus vías, por ser la más común en esta clase de operación. **Confianza: baja.** *Se consigna porque es el único indicio de acceso del expediente, y con su grado.*

---

## 2. Resumen ejecutivo

`PixelLeaks` apareció el 3 de noviembre de 2026 y dieciséis días después ocupa el segundo puesto del ranking que motiva esta serie. Tiene dos rasgos que no comparte con ningún otro actor del lote, y los dos apuntan en la misma dirección.

El primero: **no ofrece ninguna prueba visual.** En sus 34 entradas no hay **una sola captura de pantalla**, cuando `n0n` tiene 259 de 259, `Vortex` 35 de 35 y `settra` 113 de 116. En un ecosistema donde la imagen de un árbol de ficheros es la moneda corriente de la credibilidad, éste no la usa.

El segundo: **compensa con palabras, y con un nivel de detalle que es el más alto del lote.** Describe el material por tablas y con cardinalidades exactas: para una plataforma de pagos de un país africano, 818.849 transacciones de monedero, 7.630.625 detalles de transacción, 428.587 registros de libro de comisiones; para una plataforma de gestión de licencias, las copias completas de sus veintiuna bases de datos de clientes. **Describir una estructura de tablas con sus cardinalidades es difícil de inventar sin haber visto el esquema**, y eso lo sitúa alto en la escala de prueba por una vía distinta de la habitual.

Y hay un tercer rasgo, que es el hallazgo propio de este informe y que no aparece en ninguna fuente externa: **el registro con que escribe.** Sus entradas empiezan con fórmulas como «esta divulgación se refiere a un conjunto verificado de registros de…» y describen el material como «programado para publicación». **No hay amenaza, no hay insulto, no hay precio y no hay plazo en la prosa.** Es el tono de un aviso regulatorio. La lectura más económica es que **su audiencia no es el departamento de TI de la víctima, sino sus clientes, sus reguladores y la prensa** — porque es el único público para el que ese tono funciona mejor que una amenaza. Es interpretación nuestra y se marca como tal.

No es un programa de afiliados ni una operación de ransomware: **no tiene malware, ni manifiesto, ni reglas, ni reclutamiento**, y el rastreador no le registra ninguna herramienta. Es extorsión por datos, probablemente de un equipo muy pequeño.

Para esta región hay un dato que lo separa del resto de los nuevos: **tres víctimas mexicanas de 34 —el 8,8 %, la proporción latinoamericana más alta de los seis actores nuevos— y una de ellas con plazo declarado al 22 de noviembre de 2026.** En términos absolutos son tres casos; en términos de relevancia para una organización mexicana, es una reclamación con fecha.

---

## 3. Alcance y limitaciones

### 3.1 Qué cubre

El objeto `PixelLeaks` en sus dieciséis días de existencia observada: la anatomía de su catálogo, la ausencia de prueba visual y la especificidad descriptiva que la sustituye, el registro retórico de sus publicaciones y a quién apunta, su victimología y su exposición regional.

### 3.2 Qué NO cubre

| Fuera de alcance | Por qué |
|---|---|
| **Una cadena de intrusión** | Ninguna TTP, ninguna herramienta, ninguna muestra. Es `G-1` |
| **La veracidad de las reclamaciones** | Ninguna víctima ha confirmado; el rastreador advierte de cautela |
| **Los nombres de las víctimas, incluida la mexicana con plazo activo** | **No se reproducen** (`CTI-2026-048` `E-4`). El dato de que existe la reclamación sí se da |
| **El vector de acceso** | Sólo hay un indicio débil y declarado como tal (`KJ-8`) |
| **Indicadores** | No hay ninguno. `PAP:WHITE` |

### 3.3 Limitaciones de la colección

<!-- cti:note type="warn" -->

> ⚠ **Seis limitaciones.**
>
> 1. **Dieciséis días de observación y 34 entradas.** Ninguna proporción es un
>    patrón.
> 2. **Diez de las 34 entradas no tienen país**, lo que afecta directamente a
>    `KJ-5`, que es el juicio regional.
> 3. **Veintiuna de 34 no tienen dominio**, de modo que la mayoría de su
>    catálogo no es comprobable por un tercero.
> 4. **El hallazgo del registro retórico es interpretación nuestra** y ninguna
>    fuente externa lo describe (`Anexo D`).
> 5. **Los recuentos discrepan un 48 %** entre fuentes, y también la fecha de
>    su primera víctima (`KJ-7`).
> 6. **Y el 100 % de sus entradas publica con fecha del día**, de modo que **no
>    hay ninguna ventana temporal que una víctima pueda comprobar** (`KJ-6`).

### 3.4 Qué aporta

| Aporte | Dónde |
|---|---|
| **La ausencia total de prueba visual medida**: 0 de 34 | `KJ-1` |
| **La especificidad descriptiva por tablas y cardinalidades** como forma alternativa de prueba | `KJ-2`, `O-2` |
| **El registro retórico como indicador de audiencia** — hallazgo propio | `KJ-3`, `Anexo D` |
| **El 100 % de entradas con fecha del día** y su consecuencia para la víctima | `KJ-6` |
| **La exposición regional más alta de los actores nuevos**, con una reclamación activa fechada | `KJ-5`, `E-4` |
| **Un método para leer el registro retórico de un catálogo de extorsión** | `Anexo D` |

### 3.5 Veredicto

<!-- cti:table highlight="CORROBORADO|NO SOSTENIDO|propio" -->

| # | Elemento | Veredicto | Base |
|---|---|---|---|
| 1 | Es una operación de ransomware | **NO SOSTENIDO** | **Sin malware, sin manifiesto, sin reglas, sin reclutamiento** (`KJ-4`) |
| 2 | Ofrece prueba de sus reclamaciones | **NO SOSTENIDO en lo visual, PARCIALMENTE en lo descriptivo** | **0 capturas de 34**; pero recuentos por tabla difíciles de inventar (`KJ-1`, `KJ-2`) |
| 3 | Sus reclamaciones son comprobables por la víctima | **NO SOSTENIDO** | **100 % con fecha del día: no hay ventana temporal** (`KJ-6`) |
| 4 | Sus entradas son verificables por terceros | **NO SOSTENIDO** | **13 de 34 con dominio** |
| 5 | Es un actor irrelevante para la región | **NO SOSTENIDO** | **3 víctimas mexicanas (8,8 %), la mayor proporción de los nuevos, con una reclamación fechada** (`KJ-5`) |
| 6 | Su tono es el de un extorsionador | **NO SOSTENIDO — y es el hallazgo** | **Es el de un aviso regulatorio** (`KJ-3`) |
| 7 | Los recuentos públicos sobre él son consistentes | **NO SOSTENIDO** | 34 · 23 · 27, y dos fechas distintas de inicio (`KJ-7`) |
| 8 | Se conoce su vector de acceso | **NO SOSTENIDO** | Un indicio del 8,7 %, con el propio proveedor declarando que no sabe si fue la vía (`KJ-8`) |

---

# NIVEL ESTRATÉGICO
### Para: CISO, Legal, Comunicación, Riesgo · Horizonte: 3–6 meses

## E-1. Qué clase de objeto es

<!-- cti:cards -->

| Rasgo | Qué significa | Etiqueta |
|---|---|---|
| **Cero capturas de pantalla en 34 entradas** | Único en el lote. **Su credibilidad descansa en el texto** | `01 · sin prueba visual` |
| **Recuentos de registros tabla por tabla** | Difícil de inventar sin ver el esquema. **Prueba de nivel 5 sin pasar por el 3** | `02 · detalle estructural` |
| **Escribe como un regulador** | **Su audiencia son clientes, reguladores y prensa**, no el TI de la víctima | `03 · audiencia externa` |
| **Sin malware, sin reglas, sin reclutamiento** | No es un programa de afiliados. Equipo muy pequeño | `04 · operación mínima` |
| **100 % de entradas con fecha del día** | La víctima no tiene ventana temporal que comprobar | `05 · sin ventana` |
| **Mayor proporción regional de los nuevos** | 3 de 34 mexicanas, con una reclamación fechada | `06 · relevancia regional` |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `34` | Entradas medidas | Desde el 2026-11-03 |
| `0 / 34` | **Entradas con captura de pantalla** | **Único en el lote.** `n0n` 259/259, `Vortex` 35/35, `settra` 113/116 |
| `13 / 34` | Entradas con dominio | El 38 % |
| `100 %` | Entradas con fecha de ataque igual a la de publicación | Sólo `curious worm` comparte. `settra`: 0 % |
| `0` | Entradas con tamaño de datos o cifra de rescate en campo estructurado | Las magnitudes van en la prosa |
| `0` | Entradas con referencia de prensa | Ninguna recogida por un tercero |
| `3` | **Víctimas mexicanas** | **8,8 %: la mayor proporción latinoamericana de los seis actores nuevos** |
| `10 / 34` | Entradas sin país asignado | Afecta a `KJ-5` |
| `23` | Entradas publicadas en un solo día (2026-11-15) | **El 68 % de su catálogo en una jornada** |
| `34 · 23 · 27` | Recuentos de tres fuentes distintas | **Discrepancia del 48 %** |
| `7.630.625` | Detalles de transacción declarados en una sola entrada | El nivel de cardinalidad que caracteriza su prosa |

## E-2. El registro retórico, y por qué es un dato operativo

**Tres rasgos de su prosa, medidos sobre el catálogo:**

| Rasgo | Lo que hace | Lo que NO hace |
|---|---|---|
| **Fórmula de apertura** | «Esta divulgación se refiere a un conjunto **verificado** de registros de…» | No dice «hemos hackeado» |
| **Descripción del material** | Inventario por tablas, con cardinalidades y nombres de sistema | No ofrece capturas ni muestras |
| **Referencia al tiempo** | «Material **programado para publicación**» | **No amenaza, no insulta, no pone precio y no fija plazo en la prosa** |

**La lectura.** Un extorsionador escribe para su víctima: el tono es amenazante porque quiere una transferencia. **Este actor escribe para un lector externo**: el tono es administrativo porque quiere que la publicación parezca un hecho inevitable y documentado, no una negociación.

**Y eso tiene tres consecuencias prácticas:**

1. **El daño llega por fuera.** Si el material se publica con ese envoltorio, **el que lo lee primero no es el TI de la víctima: es un cliente, un periodista o un regulador**, y lo lee como un informe y no como un chantaje.
2. **La respuesta de comunicación tiene que anticiparse.** Contra una nota de rescate, la organización puede guardar silencio. **Contra una «divulgación» redactada como un aviso, el silencio parece confirmación.**
3. **Y la decisión se traslada otra vez a Legal y a Comunicación**, igual que en `CTI-2026-049` por otra vía. **Dos de los seis actores nuevos de este lote tienen su palanca fuera del alcance de Seguridad.**

> **La salvedad, que hay que poner junto a la lectura: esto es interpretación
> nuestra de un rasgo de estilo.** Ninguna fuente externa lo describe, y la
> alternativa es trivial —que el actor use una plantilla generada
> automáticamente y el tono sea un subproducto— y **no se puede descartar**. Lo
> que sí es un hecho medido es el rasgo; la intención es inferencia (`Anexo C`).

## E-3. La prueba que ofrece, y la que no

| Nivel de prueba *(escala de `CTI-2026-048` `Anexo D`)* | `PixelLeaks` | Comparación en el lote |
|---|---|---|
| **0 · Anuncio anónimo** | Algunas entradas describen «una organización del sector…» sin nombre | `n0n`: 59 de 259 |
| **2 · Dominio** | **13 de 34 (38 %)** | `settra`: 116 de 116 · `n0n`: 22 de 259 |
| **3 · Captura de pantalla** | **0 de 34 (0 %)** | **Único con cero.** Todos los demás por encima del 97 % |
| **4 · Magnitud declarada** | **Sí, y con cardinalidades de siete dígitos** | `Vortex`: 8 de 35 |
| **5 · Inventario descriptivo** | **Sí, por tablas y sistemas. El más detallado del lote** | `Vortex` en 9 de 35 |
| **6 · Muestra publicada** | No | Ninguno del lote |
| **7 · Confirmación de tercero** | **0 de 34** | `settra`: 4 · `n0n`: 0 |

**El perfil es singular: salta el nivel 3 y llega al 5.** Es el revés exacto de `Vortex`, que ofrece el 3 en el 100 % de sus entradas y el 2 sólo en el 20 %.

> **Y conviene decir qué significa eso para un analista, porque es
> contraintuitivo: el nivel 5 vale más que el 3.** Una captura de pantalla se
> fabrica, se recicla y no se puede fechar. **Un inventario de tablas con
> cardinalidades exactas requiere haber visto el esquema**, y un error en él es
> comprobable por la víctima en minutos. **Este actor ofrece menos prueba
> aparente y más prueba real que varios de los que publican imágenes.**

## E-4. Decisiones que este informe pide

| # | Decisión | A quién | Coste | Por qué |
|---|---|---|---|---|
| **1** | **Si operamos en México: comprobar si aparecemos listados, y hacerlo esta semana** | CISO · CTI | **Bajo** | `KJ-5`: tres víctimas mexicanas y **una reclamación con plazo al 22 de noviembre de 2026** |
| **2** | **Si aparecemos: comprobar las cardinalidades declaradas contra las tablas reales** | Datos · TI | Bajo | **La comprobación más discriminante de este informe.** Un error de cardinalidad refuta la reclamación; una coincidencia la hace muy difícil de explicar (`T-1`) |
| **3** | **Preparar una respuesta de comunicación para una «divulgación» redactada como aviso** | **Comunicación · Legal** | Medio | `E-2`: contra ese envoltorio **el silencio parece confirmación** |
| **4** | **Control de egreso por destino y volumen** | Red | Medio | Vale aquí, en `048`, `049` y `050`: **es la medida común de los actores sin cifrado** |
| **5** | **Rotación y vigilancia de credenciales de empleado filtradas** | Identidad | Medio | `KJ-8`: único indicio de vector, y es barato de cerrar con independencia |
| **6** | **No priorizarlo por su segundo puesto en el ranking** | CTI | Cero | Dieciséis días, 34 entradas, 68 % publicado en un solo día |

---

# NIVEL OPERACIONAL
### Para: SOC, CTI, Comunicación · Horizonte: semanas

## O-1. Identificación

| Campo | Valor |
|---|---|
| Nombre | **`PixelLeaks`** · también **`Pixelleaks`** |
| Alias | Ninguno conocido |
| En el rastreador desde | **2026-11-03** *(un proveedor sitúa su primera víctima el 9 de noviembre)* |
| Sitios de filtración | **Uno, activo** |
| TTP registradas | **Ninguna** |
| Herramientas registradas | **Ninguna** |
| Malware conocido | **Ninguno.** Una fuente lo señala expresamente |
| Manifiesto, reglas o reclutamiento | **Ninguno**, según fuente |
| Cifrado | **Sin mención** |
| Aviso gubernamental | Ninguno |

## O-2. La anatomía de su catálogo

| Campo | Presente en | Lectura |
|---|---|---|
| **Captura de pantalla** | **0 de 34** | **Único en el lote** (`KJ-1`) |
| Dominio | 13 de 34 (38 %) | Mejor que `n0n` (8,5 %), peor que `settra` (100 %) |
| País | 24 de 34 | Diez sin país |
| **Descripción con inventario por tablas** | La mayoría | **Su forma característica** (`KJ-2`) |
| **Fecha de ataque distinta de la publicación** | **0 de 34** | `KJ-6` |
| Tamaño de datos en campo estructurado | 0 de 34 | Las magnitudes van en la prosa |
| Cifra de rescate | 0 de 34 | |
| Referencia de prensa | **0 de 34** | Ninguna confirmación de tercero |

**Tres ejemplos de su prosa, parafraseados y sin identificar a nadie:** una plataforma estadounidense de gestión de licencias para cadenas de restauración, con «copias de seguridad completas de las veintiuna bases de datos de clientes»; una plataforma de pagos de consumo de un país africano, con el desglose de cuatro tablas y sus cardinalidades —desde 343.229 hasta 7.630.625 filas—; y «una organización del sector de servicios de seguridad privada», sin nombre, con un conjunto de registros comerciales y financieros.

> **La tercera es la que revela el método: cuando no nombra, describe el sector
> con una precisión casi burocrática.** No dice «una empresa»: dice el sector y
> el subsector. **Eso es suficiente para que la víctima se reconozca y
> insuficiente para que un tercero la identifique**, lo que es exactamente el
> punto óptimo para una presión sin exposición pública todavía.

## O-3. La actividad medida

| Ventana | Por **fecha de ataque** | Por **publicación** | Nota |
|---|---|---|---|
| Total | 34 | 34 | Dieciséis días |
| Últimos 7 días | **31** | **31** | **Idénticas**: consecuencia directa del 100 % de `KJ-6` |
| Ranking del sitio *(16:20 UTC del 19-11)* | — | — | **31** |
| Pico en un día | — | **23 el 2026-11-15** | **El 68 % del catálogo en una jornada** |

**Geografía** *(sobre los 24 con país)*: Estados Unidos 7, **México 3**, India 3, Vietnam 2, China 2. **Sectores**: Tecnología 8, Servicios financieros 5, Sanidad 5, Servicios profesionales 3.

> **El pico del día 15 —23 entradas, el 68 % del catálogo— es el dato que
> obliga a leer con cautela su segundo puesto en el ranking.** Como en
> `CTI-2026-050`, **el catálogo llegó mayoritariamente de una vez**, y un
> ranking de siete días no distingue entre una operación que publica a ritmo y
> una que vacía un fondo acumulado.

## O-4. Nuestra exposición

| Si la organización… | Exposición | Medida |
|---|---|---|
| **Es mexicana** | **La más alta de la región para los actores nuevos del lote.** Tres víctimas, una con plazo activo | `E-4.1` **esta semana** |
| **Es chilena** | **Ninguna medida.** Cero víctimas | Vigilancia pasiva |
| **Es de tecnología, servicios financieros o sanidad** | Baja-media. Sus tres sectores principales | Control de egreso |
| **Opera una plataforma con bases de datos de clientes** | **Media-alta en términos de daño** | Su material preferido son copias completas de bases de datos de clientes |
| **Aparece listada** | **Comprobar cardinalidades** (`T-1`) | `E-4.2` |

## O-5. Hipótesis alternativas y pre-mortem

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| **H-1 — El registro retórico busca a clientes, reguladores y prensa** | **Retenida como principal**, con la salvedad de que es interpretación nuestra | `Probable · 55–80 %` |
| **H-2 — El tono es un subproducto de una plantilla automática** | **Retenida como alternativa trivial y no descartable.** Si las descripciones se generan con un modelo de lenguaje, el registro administrativo sale de serie **sin ninguna intención** | `Posibilidad real · 40–60 %` |
| **H-3 — El detalle por tablas implica acceso real al esquema** | **Retenida.** Las cardinalidades de siete dígitos son difíciles de inventar de forma consistente | `Probable · 55–80 %` |
| **H-4 — La ausencia de capturas es una decisión de opsec** | **Retenida.** Una captura puede revelar nombres de usuario, rutas y marcas de tiempo del propio operador. **No publicarlas protege al actor** | `Posibilidad real · 40–60 %` |
| **H-5 — Las credenciales filtradas fueron el vector** | **Poco probable como establecido.** 2 de 23, y el propio proveedor dice que no lo sabe | `Poco probable · 20–45 %` |
| **H-6 — Es una marca nueva de un actor conocido** | **Sin evidencia.** Ninguna fuente lo sugiere | `Aprox. igual de probable · 40–60 %` |

**Pre-mortem — si este informe se equivoca, será porque:**

1. **`H-2` es cierta** y el hallazgo del registro retórico describe una plantilla y no una estrategia. **Es el riesgo 1**, y no cambiaría las medidas de `E-4` pero sí el encuadre.
2. **Se leyó «cero capturas» como «menos creíble»**, cuando su nivel de prueba descriptivo es el más alto del lote (`E-3`).
3. **Una organización mexicana no comprobó si estaba listada** porque el actor parecía menor.
4. **Se esperó una nota de rescate** y llegó una «divulgación» que la prensa trató como informe.
5. **Se tomó la ausencia de víctimas chilenas como garantía** con diez entradas sin país.
6. **Se priorizó por el segundo puesto** de un ranking con el 68 % del catálogo publicado en un día.

---

# NIVEL TÁCTICO Y TÉCNICO
### Para: SOC, Datos · Horizonte: días

<!-- cti:note type="warn" -->

> ⚠ **Sin TTP, sin herramientas, sin muestras y sin indicadores.** Como en los
> tres informes anteriores de la serie, **no se incluye mapa ATT&CK**: sería una
> lista vacía.
>
> **Lo que sigue es la comprobación específica que su forma de publicar
> permite, y es inusualmente buena.**

## T-1. La comprobación de cardinalidad

Si una organización aparece listada con una descripción del tipo «N transacciones, M detalles, K registros de libro», **esa descripción es comprobable en minutos y es el mejor regalo que un extorsionador puede hacer a su víctima**:

| # | Comprobación | Cómo | Qué establece |
|---|---|---|---|
| **1** | **¿Existen esas tablas con esos nombres o esa función?** | Esquema de la base de datos | Un nombre de tabla inventado **refuta la reclamación de inmediato** |
| **2** | **¿Coinciden las cardinalidades, con el margen del crecimiento desde la fecha supuesta?** | `SELECT count(*)` | **La comprobación decisiva.** Una coincidencia aproximada en **cuatro** cardinalidades distintas es casi imposible de inventar |
| **3** | **¿El número declarado es menor que el actual?** | Comparación | **Si es menor, acota la fecha del acceso**, que es el dato que el actor no da (`KJ-6`). **Es la única forma de recuperar la ventana temporal** |
| **4** | **¿Hay consultas de volcado masivo en los registros de la base de datos en esa ventana?** | Auditoría de la base de datos | La evidencia directa |
| **5** | **¿Existe esa auditoría y se retiene?** | — | Si no, los pasos 3 y 4 no se pueden responder |

> **El paso 3 es el hallazgo práctico de este informe y conviene subrayarlo.**
> Este actor **no declara cuándo accedió** —el 100 % de sus entradas publica
> con fecha del día—, lo que priva a la víctima de la ventana que necesitaría
> para investigar. **Pero las cardinalidades que sí declara llevan la fecha
> dentro**: si una tabla que crece de forma conocida tenía 818.849 filas y hoy
> tiene más, **la diferencia dice cuándo se tomó la copia.** El actor dio por
> descuido el dato que ocultó por diseño.

## T-2. Mitigaciones

| # | Medida | Dónde | Efecto | Coste |
|---|---|---|---|---|
| **X-2.1** | **Auditoría de consultas de volcado masivo en bases de datos de clientes, con retención** | Datos | Habilita los pasos 3 y 4 de `T-1` | Medio |
| **X-2.2** | **Control de egreso por destino y por volumen** | Red | La medida común a los cuatro actores sin cifrado de esta serie | Medio |
| **X-2.3** | **Vigilancia y rotación de credenciales de empleado expuestas en filtraciones públicas** | Identidad | Cierra el único indicio de vector (`KJ-8`) | Bajo |
| **X-2.4** | **Segundo factor resistente a suplantación en accesos a sistemas de datos** | Identidad | Limita el valor de una credencial robada | Medio |
| **X-2.5** | **Plan de comunicación para una «divulgación» con formato de aviso** | Comunicación · Legal | `E-2`: evita que el silencio parezca confirmación | Medio |

---

## 14. Brechas de inteligencia y requisitos de colección

| # | Brecha | Impacto | Cómo se cierra | Prioridad |
|---|---|---|---|---|
| **G-1** | **Ninguna TTP, herramienta, muestra ni indicador** | Sin detección específica posible. `PAP:WHITE` | Informe de respuesta a incidentes de una víctima | **1** |
| **G-2** | **El 100 % de entradas con fecha del día: no sabemos si el actor no la declara o el rastreador la asigna por omisión** | Afecta a `KJ-6`, y determina si la víctima puede recuperar la ventana | **Comparar una entrada del rastreador con el sitio original.** Esta célula no tiene acceso a la red oscura | **1** |
| **G-3** | **No sabemos si el registro retórico es estrategia o plantilla automática** | Es `H-2`, el riesgo 1 del pre-mortem | Comparar la prosa de entradas separadas en el tiempo; o un análisis externo del actor | 2 |
| **G-4** | **Diez de 34 entradas sin país** | Afecta a `KJ-5`, el juicio regional | Segunda fuente de rastreo | 2 |
| **G-5** | **No se ha comprobado ninguna cardinalidad declarada** | `T-1` paso 2 **sólo lo puede hacer una víctima**, y sería la validación más fuerte posible del actor | **Que una víctima lo compruebe y lo publique.** Es la petición más valiosa del informe | **1** |
| **G-6** | **Discrepancia del 48 % entre recuentos** | `KJ-7` | Criterios de recuento de cada fuente | 3 |

**Disparadores de reevaluación.** `I-1`: **que una víctima confirme o refute una cardinalidad declarada** —resolvería `G-5` y `H-3` de golpe—. `I-2`: publicación efectiva del material de la reclamación mexicana tras el 22 de noviembre. `I-3`: aparición de la primera captura de pantalla, que indicaría cambio de política. `I-4`: aparición de una entrada con fecha de ataque distinta de la de publicación, que refutaría `KJ-6`. `I-5`: aparición de malware o de reglas de afiliación, que cambiaría su clase. `I-6`: primera víctima chilena.

---

# ANEXOS

## Anexo A — Indicadores

### A.1 — ⚠ Sin indicadores de compromiso

<!-- cti:note type="warn" -->

> ⚠ **No hay ninguno.** Ni direcciones, ni dominios, ni hashes, ni ficheros, ni
> herramientas. **`PAP:WHITE`**. Y **no se reproduce ningún nombre de víctima**,
> incluida la mexicana con plazo activo: la regla de `CTI-2026-048` `E-4` se
> aplica, y el dato de que la reclamación existe se da sin nombrarla.

### A.2 — Patrones de reconocimiento y comprobación

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| pattern | **Entrada de sitio de filtración con inventario de tablas y cardinalidades exactas** | **El patrón característico de este actor** y, más importante, **la clase de reclamación que una víctima puede comprobar en minutos** (`T-1`) | Alta | Mientras mantenga el formato | **Comprobación por la víctima.** No es indicador de compromiso |
| pattern | **Entrada con fórmula «esta divulgación se refiere a un conjunto verificado de registros de…»** | El registro retórico de `KJ-3`. **Reconocimiento del actor** | Alta como observación | Igual | Reconocimiento |
| pattern | **Catálogo sin ninguna captura de pantalla** | 0 de 34, único en el lote. **Posible decisión de opsec del actor** (`H-4`): una captura revela rutas, usuarios y marcas de tiempo del operador | Alta | Igual | Graduación de la prueba |
| pattern | **Consulta de volcado masivo sobre tablas de clientes** | **El único indicador de detección que el perfil de este actor permite inferir** (`X-2.1`) | Media como inferencia | Sin caducidad | **Alerta**, con independencia de este actor |
| pattern | **Credencial de empleado de la organización aparecida en una filtración pública en los 12 meses previos** | Único indicio de vector, al 8,7 % y con el proveedor declarando que no sabe si fue la vía | **Baja** | Continua | **Rotación preventiva** (`X-2.3`) |

### A.3 — Victimología y decisiones de higiene

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| cartera | **34 entradas · 0 con captura · 13 con dominio · 0 con prensa · 100 % con fecha del día** | La anatomía de `O-2`. **El perfil de prueba más singular del lote** | Alta como recuento | 60 días | Medición |
| cartera | **3 víctimas mexicanas (8,8 %), una con plazo declarado al 2026-11-22. Ninguna chilena** | **El dato regional más accionable de los seis actores nuevos** (`KJ-5`), con diez entradas sin país como salvedad | Moderada | **22-11-2026 para el plazo** | **Comprobación inmediata si se opera en México** |
| cartera | **23 de 34 entradas publicadas el 2026-11-15** | El 68 % del catálogo en un día (`O-3`) | Alta | Histórico | Análisis |
| cartera | **Recuentos de tres fuentes: 34 · 23 · 27** | `KJ-7`. **No se reconcilian** | Alta | — | — |
| cartera | **No se reproduce ningún nombre de víctima** | Ninguna ha confirmado. Regla de la serie | — | — | No ingerir |

## Anexo B — Fuentes y valoración

| Fuente | Disciplina | Fiab. | Cred. | Grado | Notas |
|---|---|---|---|---|---|
| **`B-1` — Medición propia** sobre 34 registros: campos presentes y ausentes, lectura directa de las descripciones, perfil diario | OSINT técnico · **medición propia** | **B** | **2** | **Medición propia** | **Fuente de `KJ-1`, `KJ-2`, `KJ-3`, `KJ-5` y `KJ-6`.** Su virtud: mide ausencias —cero capturas, cero prensa, cero fechas distintas— y lee la prosa del adversario directamente. **Su límite: no verificamos contra el sitio original** (`G-2`) |
| **`B-2` — Rastreador y perfiles de proveedor** (WatchGuard, Breachsense, CyberXtron, DeXpose) | OSINT comercial · compilación | **C** | **3** | Proveedor | Fuente de **las 23 víctimas nombradas**, de la **ausencia de malware, manifiesto, reglas y reclutamiento**, de los **temporizadores de cuenta atrás**, de los nombres de tres víctimas —que **no reproducimos**— y del **indicio del 8,7 % de credenciales filtradas**, con la salvedad declarada por el propio proveedor de que **no sabe si fueron el vector** |
| **`B-3` — Fichas de víctima de terceros** (HookPhish y similares) | OSINT · compilación | **C** | **4** | Compilación | Fuente del **plazo declarado al 22 de noviembre** para la reclamación mexicana y de las fechas de listado. **Advierten de que las reclamaciones no están verificadas** |
| **`B-4` — Datos comparativos del mismo rastreador para los otros actores del lote** | OSINT técnico · medición propia | **B** | **2** | Medición propia | Lo que hace utilizable la tabla de `E-3` |

> **Una observación sobre esta estructura: es la más pobre de la serie en
> fuentes externas y la más rica en material del propio adversario.** No hay
> análisis técnico de nadie, pero **la prosa del actor es inusualmente
> informativa** porque describe su material con precisión estructural. **El
> adversario es, en este expediente, la mejor fuente disponible sobre sí
> mismo**, y eso obliga a la cautela del `Anexo D`: lo que dice de su material
> puede ser comprobable, pero lo dice él.

## Anexo C — Léxico de probabilidad y confianza

<!-- cti:bars title="Probabilidad estimativa" -->

| Etiqueta | Valor |
|---|---|
| Casi con certeza (≥99 %) | 99 |
| Muy probable (80–95 %) | 88 |
| Probable (55–80 %) | 68 |
| Aproximadamente igual de probable (40–60 %) | 50 |
| Poco probable (20–45 %) | 32 |
| Muy poco probable (5–20 %) | 12 |
| Remoto (≤5 %) | 4 |

**Confianza**: **alta** —fuentes múltiples corroboradas, método expuesto—; **moderada** —fuente única de calidad, o inferencia propia sobre datos verificables—; **baja** —dato ausente o inferencia indirecta—.

> **La distinción que este informe necesita: separar la confianza en un rasgo
> de estilo de la confianza en lo que ese estilo busca.**
>
> «Sus entradas usan un registro administrativo y no amenazante» es una
> observación directa y reproducible: confianza **alta**. «Ese registro busca a
> clientes, reguladores y prensa» es una **atribución de propósito a una
> elección retórica**, y tiene una alternativa trivial —que la prosa la genere
> una plantilla automática y el tono sea un subproducto— que no se puede
> descartar: confianza **moderada**, probabilidad *probable*.
>
> **La regla, y es la hermana de la de `CTI-2026-049`:** un rasgo observado en
> el material del adversario se afirma con la confianza de la observación; **su
> propósito, nunca.** Y en la era de los textos generados automáticamente, la
> inferencia de intención a partir del estilo **ha perdido fuerza y conviene
> decirlo**: lo que antes revelaba a un autor hoy puede revelar sólo una
> herramienta.

## Anexo D — Cómo leer el registro retórico de un catálogo de extorsión

**El problema.** Los catálogos de los sitios de filtración se leen por su contenido —a quién nombran, qué datos reclaman— y casi nunca por su **forma**. Y la forma lleva información: **el tono en que un extorsionador escribe indica para quién escribe**, y eso determina por dónde va a llegar el daño.

**Los cuatro registros que esta cartera ha observado, con su audiencia y su consecuencia:**

| Registro | Rasgos | Audiencia implícita | Qué cambia en la respuesta |
|---|---|---|---|
| **Amenazante clásico** | Insultos, plazos, precio explícito, mayúsculas | **El TI y la dirección de la víctima** | Respuesta técnica y de negociación. **El silencio público es viable** |
| **Administrativo** *(este actor)* | «Divulgación», «conjunto verificado», «programado para publicación». Sin amenaza ni precio | **Clientes, reguladores, prensa** | **Respuesta de comunicación obligatoria**: el silencio parece confirmación |
| **Personal** *(`CTI-2026-049`)* | Inventario de datos personales del propietario | **Una persona física concreta** | **Respuesta de apoyo legal personal**, y la decisión sale de Seguridad |
| **Técnico-presuntuoso** *(`CTI-2026-042`)* | Reclamaciones de capacidad, entrevistas, alardes | **Afiliados y competidores del propio mercado** | **Las afirmaciones son publicidad de reclutamiento**: se valoran como tales |

**Cómo se usa, en tres pasos:**

1. **Leer tres entradas completas antes de leer el recuento.** El recuento se obtiene en un segundo y no dice nada; la forma exige cinco minutos y dice para quién escribe.
2. **Clasificar el registro y derivar la audiencia.** De la audiencia sale **qué función de la organización tiene que estar preparada**, que es la decisión más cara de tomar durante un incidente.
3. **Y buscar la discordancia.** Un actor con registro administrativo y plazos agresivos en los metadatos está hablando a dos públicos a la vez: **la discordancia entre la prosa y la mecánica es informativa** y suele indicar una plantilla por encima de una estrategia.

**Las dos advertencias, y la segunda es nueva:**

1. **El registro se imita y se cambia.** Un actor puede adoptar un tono administrativo sin que eso cambie nada de su operación. **La inferencia es sobre la intención comunicativa, no sobre la capacidad.**
2. **Y la inferencia de intención a partir del estilo ha perdido fuerza, porque los textos se generan.** Si las descripciones de un catálogo las produce un modelo de lenguaje a partir de unos campos, **el registro es un ajuste por omisión y no una elección**. Esta cartera ya observó descripciones marcadas explícitamente como generadas automáticamente en otro rastreador. **El paso 3 —buscar la discordancia— es la contramedida**: una plantilla produce tono uniforme; una estrategia produce tono coherente con la mecánica.

## Anexo E — Marcos de referencia empleados

- **ICD 203**, con la adición del `Anexo C`: **un rasgo de estilo se afirma con la confianza de la observación; su propósito, nunca** — y con la advertencia de que la inferencia de intención a partir del estilo ha perdido fuerza desde que los textos se generan automáticamente.
- **Código Admiralty/OTAN**, con el grado **medición propia**, y con la observación de que aquí **el adversario es la mejor fuente disponible sobre sí mismo**.
- **MITRE ATT&CK: deliberadamente sin mapa.** Sin TTP ni procedimientos observados.
- **Graduación de la prueba de una entrada de sitio de filtración**, `Anexo D` de `CTI-2026-048`: este actor **salta el nivel 3 y llega al 5**, el revés exacto de `CTI-2026-050`, y la tabla de `E-3` es la aplicación.
- **Lectura del registro retórico de un catálogo**, propio de este informe (`Anexo D`): cuatro registros, tres pasos, y la búsqueda de discordancia como contramedida frente a la prosa generada.

## Anexo F — Paquete legible por máquina

Las tablas `cti:ioc` alimentan `ioc_index.csv`. **Cinco advertencias:**

1. **No hay indicadores de compromiso.** `PAP:WHITE`. El único patrón de detección —consulta de volcado masivo— es **inferencia nuestra** y vale con independencia de este actor.
2. **No se reproduce ningún nombre de víctima**, incluida la mexicana con plazo activo. El dato de que la reclamación existe y su fecha límite sí se dan.
3. **El recuento de 34 no concuerda con el de las otras fuentes** (23 y 27), y la diferencia se explica plausiblemente por las 21 entradas sin dominio.
4. **Las cardinalidades que el actor declara no se transcriben como datos de ninguna víctima**, sino como ejemplos de su formato. **Una organización que las vea referidas a ella debe comprobarlas con `T-1`, y el paso 3 puede devolverle la fecha del acceso.**
5. **El plazo del 22 de noviembre de 2026 es el único dato con caducidad dura de este informe**, y después de esa fecha el expediente necesita revisión (`I-2`).

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-11-19 | Emisión inicial, sexta de la serie `046`–`053`. Incluye: la **ausencia total de prueba visual medida** —cero capturas en 34 entradas, único en el lote— (`KJ-1`); la **especificidad descriptiva por tablas y cardinalidades** como forma alternativa y superior de prueba, con el perfil que **salta el nivel 3 y llega al 5** (`KJ-2`, `E-3`); el **hallazgo propio del registro retórico administrativo** y la inferencia de que su audiencia son clientes, reguladores y prensa, con la alternativa de la plantilla automática retenida como seria (`KJ-3`, `E-2`, `H-2`); la constatación de que **no es un programa de afiliados** —sin malware, manifiesto, reglas ni reclutamiento— (`KJ-4`); el **dato regional más accionable de los actores nuevos**: tres víctimas mexicanas y una reclamación con plazo al 22 de noviembre (`KJ-5`); el **100 % de entradas con fecha del día** y su consecuencia de privar a la víctima de ventana temporal (`KJ-6`); la **discrepancia del 48 % entre recuentos** (`KJ-7`); la **comprobación de cardinalidad** de `T-1`, cuyo paso 3 permite a la víctima **recuperar la fecha del acceso que el actor oculta**; y el método del `Anexo D` para leer el registro retórico de un catálogo | Célula CTI |

> **Nota sobre esta emisión.** Es el informe de la serie con **menos fuentes
> externas y más material del propio adversario**, y de ahí salen sus dos
> aportaciones: una es que **el nivel de prueba descriptivo vale más que el
> visual** —un inventario de tablas es comprobable, una captura no—, y la otra
> es que **el actor que oculta la fecha del acceso la entrega sin darse cuenta
> en las cardinalidades que publica** (`T-1` paso 3).

## Anexo H — Realimentación del consumidor

1. **Si operamos en México: ¿se comprobó esta semana si aparecemos listados?** Es la decisión 1 de `E-4`. **Hay tres víctimas mexicanas y una reclamación con plazo al 22 de noviembre de 2026**, y es el dato más accionable de los seis actores nuevos de esta serie.
2. **Si aparecemos: ¿se compararon las cardinalidades declaradas con las tablas reales?** Es `T-1` paso 2 y la comprobación más discriminante del informe. **Una coincidencia aproximada en cuatro cardinalidades distintas es casi imposible de inventar.**
3. **¿Y se usó el paso 3?** Si la cifra declarada es menor que la actual, **la diferencia dice cuándo se tomó la copia** — y es la ventana temporal que el actor no da.
4. **¿Existe auditoría de consultas de volcado masivo sobre las bases de datos de clientes, y se retiene?** Es `X-2.1`. Sin ella, los pasos 3 y 4 de `T-1` no se pueden responder.
5. **¿Hay un plan de comunicación para una «divulgación» redactada como aviso regulatorio?** Es `E-2` y `X-2.5`. Contra ese envoltorio **el silencio parece confirmación**, y es la segunda vez en esta serie que la palanca de un actor cae fuera de Seguridad.
6. **¿Se rotaron las credenciales de empleado aparecidas en filtraciones públicas?** Es `X-2.3`: único indicio de vector, débil, y barato de cerrar de todos modos.
7. **¿Puede alguien comparar una entrada del rastreador con el sitio original?** Es `G-2`: resolvería si el 100 % de fechas del día es una propiedad del actor o del rastreador.
8. **¿Alguna víctima ha comprobado y publicado si una cardinalidad declarada era correcta?** Es `G-5` y **la petición más valiosa del informe**: validaría o destruiría `H-3`, que es el juicio sobre si este actor tuvo acceso real.
9. **Y la pregunta de método:** el `Anexo D` sostiene que la inferencia de intención a partir del estilo **ha perdido fuerza porque los textos se generan automáticamente**, y propone buscar la discordancia entre la prosa y la mecánica como contramedida. **¿Alguien ha encontrado un catálogo con tono uniforme y mecánica coherente, es decir, un caso en que la contramedida no discrimine?** Eso acotaría cuándo el método sirve.

*Fin del informe `CTI-2026-051` v1.0.*
