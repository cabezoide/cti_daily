---
tlp: "TLP:CLEAR"
pap: "PAP:WHITE"
id: "CTI-2026-056"
version: "1.0"
tipo: "Perfil de operación de extorsión"
foco_regional: "Sin relevancia regional medible"
niveles: ["Estratégico", "Operacional"]
autor: "Célula CTI"
actor: "BrainCipher"
fecha: "2026-11-19"
caduca: "2026-12-19"
distribucion: "ADVERTENCIA PRINCIPAL: el recuento de 432 entradas que sitúa a este actor como el segundo del semestre no son 432 víctimas. El 99 % son nombres de fichero, y el enriquecimiento automático de la fuente ha inventado víctimas a partir de ellos. No se reproduce ningún nombre de víctima ni ningún nombre de fichero que identifique a una persona física. Difusión libre conservando la atribución y las salvedades de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-056

## El segundo actor del semestre por volumen no tiene 432 víctimas: tiene 429 nombres de fichero

### Y el enriquecimiento automático convirtió seis de esos ficheros en víctimas que no existen, una de ellas Amazon

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-056` |
| Versión | 1.0 |
| Tipo | Perfil de operación de extorsión |
| Clasificación | `TLP:CLEAR` · `PAP:WHITE` |
| Fecha de emisión | 2026-11-19 |
| Caducidad | 2026-12-19 |
| Niveles | Estratégico · Operacional |
| Actor | BrainCipher · Brain Cipher |
| Entradas en la ventana | 432, de las que **3 son víctimas identificables** |
| Infraestructura | **54 sitios registrados · 6 activos** |
| Relevancia regional | **Ninguna medible** · 0 LATAM · 0 Chile |
| Autor | Célula CTI |

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** **Las 432 entradas que convierten a este actor en el segundo del semestre son, en el 99 % de los casos, nombres de fichero y no víctimas.** De 432 entradas, **429 llevan por título un nombre de archivo**: series como `aws.part07.rar` a `aws.part18.rar`, cadenas como `SQL` o rutas como `1.outlooks/`. Valoramos **casi con certeza** *(≥99 %)* la medición. **Confianza: alta**, y ahora **corroborada por una fuente independiente**: un segundo agregador consultado el mismo día atribuye a este actor **entre 64 y 110 víctimas en todo su historial** (`E-1.2`). *Consecuencia:* **el recuento de víctimas de este actor en el semestre es indeterminado y con casi total seguridad de dos cifras**, y cualquier comparación de volumen que incluya el 432 está contaminada (`E-1`).

**KJ-2.** **El enriquecimiento automático de la fuente no detectó el problema: inventó víctimas a partir de los nombres de fichero, y una de ellas es Amazon.** A entradas tituladas `aws.partNN.rar` les asignó el dominio **`aws.amazon.com`**, país Estados Unidos y sector Tecnología, con puntuación de confianza **0,95**. El mismo mecanismo produjo otros cinco dominios inexistentes como víctimas: `officefiles.com` (8 entradas), `studiodata.com` (5), `eworldme.com` (5), `windiam.com` (4) y `managers-share.com` (3). Valoramos **casi con certeza** *(≥99 %)* que son falsos positivos. **Confianza: alta.** *Consecuencia, y es la más grave:* una consulta de víctimas de este actor por país y sector **devuelve a Amazon Web Services como organización comprometida**, y no hay nada en la respuesta que lo señale (`E-2`).

**KJ-3.** **Lo que sí se puede afirmar del actor es que publica el contenido, no sólo el nombre de la víctima, y eso es una diferencia de modelo.** La estructura de las entradas —series de volúmenes de archivo numerados consecutivamente, nombres de tablas, rutas de buzones— indica que el sitio expone el **inventario de lo exfiltrado** fichero a fichero. Valoramos **muy probable** *(80–95 %)* esta lectura. **Confianza: moderada**, porque se infiere de los títulos y no de la lectura del sitio. *Consecuencia:* para una víctima de este actor, **el perjuicio no se negocia sobre una amenaza sino sobre un índice publicado** (`O-2`).

**KJ-4.** **Su infraestructura es la más extensa de los seis actores de este lote y está casi toda muerta: cincuenta y cuatro sitios registrados, seis activos.** Las fechas de última exploración se agrupan en tandas —el 22 de agosto, el 24 de octubre, el 5 de noviembre, el 19 de noviembre—, lo que indica rotación por bloques y no caída progresiva. Ninguno de los cincuenta y cuatro lleva prefijo legible. Valoramos **casi con certeza** *(≥99 %)* los recuentos. **Confianza: alta.** *Consecuencia:* un bloqueo por dirección no sirve contra este actor; **la rotación por bloques es su contramedida y hay cuarenta y ocho direcciones conocidas inactivas que pueden volver** (`O-3`).

**KJ-5.** **No tiene relevancia regional medible, y la ausencia está mal medida en origen.** Los campos de país sólo están poblados en **34 de 432 entradas (8 %)** y los seis países que aparecen son Estados Unidos, Reino Unido, Canadá, Italia, Países Bajos y Alemania. **Cero entradas latinoamericanas, cero chilenas.** Valoramos **probable** *(55–80 %)* que la ausencia regional sea real y no un hueco de datos, apoyándonos en que el perfil declarado del actor sitúa su origen operativo en el sudeste asiático. **Confianza: baja**, y es el juicio más débil del informe: con el 92 % de las entradas sin país, **la ausencia no es demostrable** (`E-3`).

**KJ-6.** **El perfil que la fuente publica sobre este actor es extenso, afirmativo y no verificado, y conviene tratarlo como lo que es.** Declara derivación del constructor filtrado de LockBit 3.0, módulos de evasión con cifrado dinámico de nombres de API, terminación de Windows Defender, variante para Linux, uso de corredores de acceso inicial, adjuntos de suplantación dirigida y explotación de **CVE-2023-28252** en el controlador CLFS de Windows. Ninguna de esas afirmaciones lleva referencia, y el registro textual indica redacción automática. Valoramos **posible** *(40–60 %)* que el conjunto sea sustancialmente correcto —es coherente con lo publicado sobre este actor desde 2024— y **no lo damos por cierto en ningún punto**. **Confianza: baja.** *Consecuencia:* **el único elemento accionable del perfil es la CVE**, y se traslada al nivel técnico como hipótesis de caza, no como hecho (`X-1`).

**KJ-7.** **El juicio de conjunto: este expediente no es un perfil de actor, es el registro de un artefacto de medición con el poco actor que se deja ver detrás.** Valoramos **muy probable** *(80–95 %)* que un recuento correcto situara a este actor fuera de los diez primeros del semestre. **Confianza: moderada.** *Consecuencia:* se emite para que la cifra de 432 **no se vuelva a citar**, y para dejar fijado el método de detección del `Anexo D`, que cuesta un minuto (`E-4`).

---

## 2. Resumen ejecutivo

En el recuento de entradas publicadas en los seis meses que van del 19 de mayo al 19 de noviembre de 2026, BrainCipher aparece **segundo**, con 432, sólo por detrás de Qilin. Es un dato llamativo: la cartera no tenía expediente de este actor y un segundo puesto justificaba abrirlo.

**El dato es falso, y el motivo es de granularidad.** Al mirar los títulos de las 432 entradas, 429 no son organizaciones: son nombres de fichero. Hay series completas de volúmenes de archivo —`aws.part07.rar`, `aws.part08.rar`, y así hasta el dieciocho—, cadenas sueltas como `SQL`, rutas de carpeta como `1.outlooks/`. El rastreador está indexando **cada fichero que el sitio de filtración publica como si fuera una víctima independiente**, y el resultado es que un único volcado de datos de una sola organización genera decenas de entradas.

La distribución diaria lo confirma: las 432 entradas se reparten en **ocho días**, con 142 el 5 de septiembre y 133 el 18 de septiembre. No son 432 ataques: son unos pocos volcados de ficheros, contados fichero a fichero.

La segunda parte del hallazgo es peor que la primera. El enriquecimiento automático de la fuente —el proceso que asigna nombre canónico, país, sector y dominio a cada entrada— **no detectó el problema y rellenó los huecos**. A las entradas tituladas `aws.partNN.rar` les asignó el dominio `aws.amazon.com`, el país Estados Unidos y el sector Tecnología, con una puntuación de confianza de 0,95. El mismo mecanismo produjo otros cinco dominios como presuntas víctimas: `officefiles.com`, `studiodata.com`, `eworldme.com`, `windiam.com` y `managers-share.com`. **Ninguna de esas seis es una víctima; son nombres de fichero interpretados como organizaciones.**

Lo que queda del actor, una vez descontado el artefacto, es poco pero no nulo. La estructura misma de las entradas dice algo sobre su modelo: **publica el inventario de lo exfiltrado, fichero a fichero**, en lugar de publicar sólo el nombre de la organización con una amenaza. Para una víctima eso cambia la negociación, porque lo que está expuesto no es una afirmación sino un índice.

Y su infraestructura es la más extensa de los seis actores de este lote: **cincuenta y cuatro direcciones de servicio oculto registradas, de las que seis están activas**. Las fechas de última exploración se agrupan en cuatro tandas, lo que indica rotación por bloques. Ninguna de las cincuenta y cuatro lleva prefijo legible, decisión opuesta a la de krybit (`CTI-2026-057`) y probablemente deliberada.

No tiene relevancia regional medible. Pero conviene decir con claridad que eso está mal medido en origen: **sólo el 8 % de sus entradas tiene país**, de modo que la ausencia de víctimas latinoamericanas no es demostrable, sólo no observada.

---

## 3. Alcance y limitaciones

### 3.1 Qué se midió y cómo

Las 432 entradas proceden de la consulta de entradas con descubrimiento posterior al 19 de mayo de 2026, paginada, en la API de cti.fyi el 19 de noviembre. La clasificación de un título como nombre de fichero se hizo con un criterio explícito y conservador: extensión de archivo conocida, patrón de volumen numerado, o terminación en barra. El criterio está en `Anexo F` y es reproducible.

### 3.2 Lo que este informe no puede decir

- **No sabemos cuántas víctimas tiene este actor en el semestre.** Las tres entradas que no son nombres de fichero son el suelo, no la cifra. El techo sería el número de volcados distintos, y para contarlo haría falta leer el sitio.
- **No se leyó el sitio de filtración.** No hay acceso a la red oscura en este entorno. Todo procede de los metadatos del rastreador.
- **No se verificó ninguna reclamación contra la víctima.**
- **El perfil del actor no se corroboró en ningún punto.** Véase `KJ-6` y `Anexo B`.

### 3.3 Higiene

No se reproduce ningún nombre de víctima. **Y no se reproduce ningún nombre de fichero que identifique a una persona física**: en el conjunto del semestre hay seis entradas de ese tipo repartidas entre cinco actores, y la regla de `CTI-2026-049` se aplica igual aquí. Los nombres de fichero que sí se citan —`aws.part07.rar`, `SQL`, `1.outlooks/`— son genéricos y necesarios para documentar el artefacto.

### 3.4 Veredicto por nivel

| Nivel | Veredicto | Motivo |
|---|---|---|
| Estratégico | **Utilizable como advertencia** | El artefacto está medido; el actor no |
| Operacional | **Parcial** | Infraestructura sí; victimología no |
| Táctico | **No evaluable** | Sin TTP observados |
| Técnico | **Hipótesis únicamente** | La CVE del perfil, sin corroborar |

---

# NIVEL ESTRATÉGICO

## E-1. Cuatrocientas treinta y dos entradas, ocho días

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `432` | Entradas en la ventana | **Segundo puesto del semestre** |
| `429` | **De ellas, nombres de fichero** | **99 %** (`KJ-1`) |
| `3` | Entradas que podrían ser víctimas | El suelo, no la cifra |
| `8` | **Días con actividad en 184** | 142 y 133 en dos de ellos |
| `0` | Entradas con fecha de publicación | **De 432. Único en el lote** |
| `34` | Entradas con país (8 %) | `KJ-5` |
| `6` | **Dominios inventados por el enriquecedor** | Entre ellos `aws.amazon.com` |
| `54` | Sitios registrados · **6 activos** | La infraestructura más extensa del lote |

La distribución diaria es la primera señal de que algo no cuadra:

| Fecha | Entradas |
|---|---|
| 2026-09-04 | 20 |
| **2026-09-05** | **142** |
| 2026-09-11 | 13 |
| 2026-09-15 | 31 |
| **2026-09-18** | **133** |
| 2026-09-22 | 20 |
| 2026-10-19 | 26 |
| 2026-11-15 | 47 |

Ninguna operación de extorsión publica ciento cuarenta y dos víctimas en un día y nada durante los seis días siguientes. Lo que se publicó el 5 de septiembre fue **un volcado**, y el rastreador lo contó fichero a fichero.

### E-1.1 La prueba, en los propios títulos

Las primeras veinte entradas del 4 de septiembre incluyen la serie `aws.part07.rar` a `aws.part18.rar` —doce entradas consecutivas que son los volúmenes de un único archivo partido—, más `SQL` y `1.outlooks/`. **Doce entradas, un archivo.**

Aplicado el criterio de `Anexo F` a las 432: **429 son nombres de fichero (99,3 %)**.

El mismo artefacto afecta a otros actores de la fuente, aunque con mucha menor intensidad: `Panzer` (17 de 35, 49 %), `incransom` (8 de 248, 3 %), `Booba Project` (4 de 129, 3 %) y `hellcat` (2 de 2). En el semestre completo son **460 entradas de 5.144 (8,9 %)**. En este actor está concentrado casi todo el efecto.

### E-1.2 La corroboración independiente

Un segundo agregador —CTIWatch, evaluado en `CTI-2026-054` `§O-8`— mantiene
ficha de este actor y le atribuye, **en el mismo día de consulta**, una cifra de
víctimas de **dos órdenes de magnitud por debajo** de las 432 entradas:

| Fuente | Cifra | Qué cuenta |
|---|---|---|
| cti.fyi, entradas del semestre | **432** | **Ficheros publicados** (`KJ-1`) |
| CTIWatch, cabecera de ficha | 110 | Víctimas, todo el historial |
| CTIWatch, prosa de la misma ficha | **64** | Víctimas, todo el historial |

Las dos cifras de CTIWatch **se contradicen entre sí** —defecto sistemático de
esa fuente, presente en seis de seis fichas comprobadas— y por eso no se adopta
ninguna como recuento. **Lo que sí establecen es el orden de magnitud**, y es
decenas en todo el historial del actor frente a cuatrocientas treinta y dos en
seis meses.

Esto convierte `KJ-1` de una inferencia sobre títulos en una conclusión
apoyada por dos fuentes que no comparten método: una cuenta ficheros y lo
documenta en los títulos, y la otra cuenta organizaciones y da decenas.


## E-2. Las víctimas que el enriquecedor inventó

El proceso de enriquecimiento de la fuente recibe un título y devuelve nombre canónico, dominio, país, sector, un resumen en prosa y una puntuación de confianza. Cuando el título es una organización, funciona. **Cuando el título es un nombre de fichero, no se abstiene: infiere.**

| Dominio asignado como víctima | Entradas | Procedencia real del dato |
|---|---|---|
| `officefiles.com` | 8 | Nombres de fichero |
| `studiodata.com` | 5 | Nombres de fichero |
| `eworldme.com` | 5 | Nombres de fichero |
| `windiam.com` | 4 | Nombres de fichero |
| **`aws.amazon.com`** | **4** | **Las entradas `aws.partNN.rar`** |
| `managers-share.com` | 3 | Nombres de fichero |
| `studiodata.it` | 1 | Nombre de fichero |
| `studioadviser.com` | 1 | Nombre de fichero |

**El caso de Amazon es el que mejor ilustra el mecanismo.** El enriquecedor leyó `aws.part12.rar`, reconoció la cadena «aws», y concluyó que la víctima era Amazon Web Services: dominio `aws.amazon.com`, país Estados Unidos, sector Tecnología, confianza **0,95**. La cadena «aws» en el nombre de un fichero comprimido indica, como mucho, que el contenido procede de una cuenta de AWS **de la víctima real** — y ni eso es seguro.

Esto conecta con una medición de `CTI-2026-054` `§O-5`: la puntuación de confianza de esta fuente vale 0,95 en el 77,9 % de los registros, y correlaciona con **cuántos campos están poblados**, no con si son correctos. Aquí se ve por qué eso importa: **estos registros tienen los tres campos duros poblados y los tres son falsos**, de modo que la puntuación alta es consecuencia del error, no un control contra él.

> **La lección transferible, y es incómoda:** un enriquecedor automático que nunca se abstiene convierte la ausencia de datos en datos falsos, y el campo de confianza **premia** ese comportamiento porque mide completitud y no veracidad.

## E-3. Relevancia regional: ninguna observada, y mal medida

| Medición | Valor |
|---|---|
| Entradas con país | **34 de 432 (8 %)** |
| Países distintos | 6 |
| Reparto | US 24 · GB 5 · CA 2 · IT 1 · NL 1 · DE 1 |
| **Latinoamérica** | **0** |
| **Chile** | **0** |

Treinta y cuatro entradas con país de cuatrocientas treinta y dos. Y de esas treinta y cuatro, parte son los falsos positivos de `E-2`.

**Este informe no afirma que el actor no tenga víctimas latinoamericanas.** Afirma que no se observa ninguna, con el 92 % del catálogo sin país y con el catálogo mismo contaminado. Es la diferencia entre ausencia de evidencia y evidencia de ausencia, y aquí sólo hay la primera.

El único apoyo lateral es que el perfil declarado por la fuente sitúa los primeros ataques del actor en un organismo público de Indonesia, lo que encaja con un foco asiático. **Es un apoyo débil, de una fuente no corroborada**, y por eso `KJ-5` lleva confianza baja.

## E-4. Decisiones que este informe pide

1. **Retirar la cifra de 432 de cualquier comparación de volumen** del semestre, y rehacer el recuento de los diez primeros con el filtro de `Anexo D`.
2. **No ingerir los seis dominios de `E-2` como indicadores ni como víctimas.** Si alguno ya entró en una lista por esta vía, retirarlo. `aws.amazon.com` en una lista de organizaciones comprometidas es un falso positivo con consecuencias.
3. **Mantener el expediente abierto con prioridad baja.** El actor es real y su infraestructura es extensa; lo que no es real es su volumen aparente.
4. **Aplicar el filtro de `Anexo D` al recolector diario de la cartera** antes de la próxima ejecución, para que el artefacto no entre por la vía automática.

---

# NIVEL OPERACIONAL

## O-1. Identificación

| Campo | Valor | Procedencia |
|---|---|---|
| Nombre | BrainCipher · Brain Cipher | Títulos de sus propios sitios |
| Primera aparición declarada | Mediados de junio de 2024 | **Perfil de proveedor, no corroborado** |
| Primera entrada en la ventana | 2026-09-04 | Medición propia |
| Última entrada | 2026-11-15 | Medición propia |
| Linaje declarado | Derivado del constructor filtrado de LockBit 3.0 | **Perfil de proveedor, no corroborado** |
| Modelo declarado | Doble extorsión, exfiltración previa al cifrado | **Perfil de proveedor** |
| Sitios | 54 registrados · 6 activos | Medición propia |

## O-2. Qué se deja ver del modelo

La única observación propia y sustantiva sobre el comportamiento de este actor es **la forma de sus entradas**, y dice algo que vale la pena.

Un sitio de filtración típico publica una ficha por organización: nombre, descripción, tamaño de los datos, plazo, capturas. Este sitio publica, además, **el inventario de ficheros**. Las series de volúmenes numerados consecutivamente, las cadenas que son nombres de tabla —`SQL`—, las rutas que son carpetas de buzón —`1.outlooks/`— son la estructura de un listado de contenido.

Consecuencia para una víctima: **lo que está publicado no es una afirmación sobre lo robado, es un índice de lo robado**. Eso cambia tres cosas. La reclamación es verificable por la propia víctima en minutos, comparando nombres de fichero con su propio sistema de archivos. La presión no depende de la credibilidad del actor. Y el alcance de la exfiltración se puede acotar desde fuera, lo que normalmente es imposible.

Y consecuencia para el analista: **un sitio que publica inventario produce mucho más ruido de recuento que uno que publica fichas**, que es exactamente el artefacto de `E-1`.

## O-3. Infraestructura

Cincuenta y cuatro direcciones de servicio oculto registradas. **Seis activas** al 19 de noviembre de 2026:

| Dirección | Última exploración |
|---|---|
| `6ft2dfh26wm3w44orpjcgviutvfp25ez2iyh5ego5egvfmifrws7vvqd.onion` | 2026-11-18 |
| `dkeqrg3fxrijolpgpbsmk6eacare4bg5awrracxdiestki2onyz5bnyd.onion` | 2026-11-19 |
| `emdnfl2fv32jhssxcbxlo6dzg2at4d7qbw2md6inz63qzdfgyln5cwyd.onion` | 2026-11-19 |
| `lhsxojxowgtwdqlryl72d2v5cpgqv3sll4d47yyqdisersigvfbl5uid.onion` | 2026-11-19 |
| `mejouwrwja4iou7myj34rqi7cixyhn7vsa42e2n2dhxzc5mmkiaki3yd.onion` | 2026-11-18 |
| `rpoeu7zimfpwxbwmjmjyprqaprtvkj3ykfczhbc4x3voydopffn337id.onion` | 2026-10-26 |

### O-3.1 La rotación es por bloques

Las fechas de última exploración de los cuarenta y ocho sitios inactivos se agrupan: **ocho el 22 de agosto, catorce el 24 de octubre, cinco el 5 de noviembre**, y el resto el 19 de noviembre. Eso no es desgaste progresivo: es **sustitución por tandas**.

Los ocho más antiguos conservan título descriptivo —«BrainCipher Dataleak», «Brain Cipher Client Area», «BrainCipher Storage», y uno literalmente «Not Found»— mientras que los cuarenta y seis posteriores no tienen título. La lectura más económica es que los primeros corresponden a una generación anterior de la operación, con portal de negociación y almacenamiento separados, y los posteriores a una infraestructura de rotación rápida sin estructura declarada.

**Y hay un detalle que importa a quien bloquee por dirección:** el sitio titulado «BrainCipher Dataleak» —el principal de la generación antigua— aparece como disponible con estado inactivo y fecha de exploración de hoy. Es uno de los casos del defecto de contradicción de campos documentado en `CTI-2026-054` `§O-7.1`, que afecta al 31 % de los sitios de este lote. **No se puede afirmar desde estos datos si ese sitio responde o no.**

### O-3.2 El contraste con krybit

Ninguna de las cincuenta y cuatro direcciones lleva prefijo legible. En el mismo lote, `krybit` tiene cuatro sitios activos y los cuatro empiezan por `krybit` o `krybie` (`CTI-2026-057`). Son dos decisiones opuestas sobre lo mismo:

- **Prefijo legible**: cuesta cómputo, facilita que la víctima encuentre el sitio correcto y evita suplantaciones, **y hace al actor cazable por patrón**.
- **Dirección aleatoria con rotación por bloques**: no es cazable por patrón, no sirve para reconocimiento de marca, **y obliga al actor a publicar la dirección por otro canal cada vez que rota**.

Con cincuenta y cuatro direcciones y seis activas, este actor ha elegido la segunda y paga su coste.

## O-4. Clasificación

Aplicando el triaje de `CTI-2026-042` `Anexo D`, el actor cumple **cuatro criterios de siete**: tiene sitio de filtración con contenido publicado, tiene infraestructura propia y extensa, tiene continuidad temporal desde 2024 según el perfil del proveedor, y tiene portal de cliente separado en su generación antigua —lo que responde al criterio más discriminante del método, cómo contacta la víctima: **portal, luego operación y no herramienta**—. Falla en análisis primario verificable, en muestra disponible y en víctima confirmada por tercero.

**Clase: marca con operación**, con el volumen sin determinar.

## O-5. Hipótesis y pre-mortem

**H-1.** *Las 429 entradas-fichero corresponden a menos de veinte organizaciones.* **Probable** *(55–80 %)*. Apoyo: ocho días de actividad, dos con más de 130 entradas, y series de volúmenes consecutivos. En contra: no se puede contar sin leer el sitio.

**H-2.** *El artefacto es del rastreador y no del sitio.* **Muy probable** *(80–95 %)*. Apoyo: otros cuatro actores del semestre presentan el mismo patrón en menor grado, lo que apunta a un criterio de extracción y no a un comportamiento de este actor.

**H-3.** *Las seis supuestas víctimas de `E-2` son todas falsas.* **Muy probable** *(80–95 %)*. El caso de Amazon es demostrable; los otros cinco son dominios genéricos sin presencia verificable.

**H-4.** *El actor sigue operativo.* **Probable** *(55–80 %)*. Seis sitios activos y una entrada el 15 de noviembre.

### Pre-mortem

*Si este informe se equivoca, será en `KJ-5`.* Con el 92 % de las entradas sin país, la afirmación de que no hay víctimas latinoamericanas se apoya en casi nada. **Una sola víctima chilena o mexicana en el catálogo real invalidaría el juicio**, y no tenemos forma de descartarla. Está calificado con confianza baja y recogido en `G-2`.

*El segundo modo de fallo es `H-2`.* Si el inventario de ficheros lo publica el sitio con una ficha por fichero —es decir, si el actor realmente presenta cada archivo como una entrada—, entonces el rastreador estaría representando fielmente el sitio y el artefacto sería de interpretación nuestra, no de extracción. La comprobación exige leer el sitio (`I-1`).

---

# NIVEL TÉCNICO

## X-1. Lo único accionable, y es una hipótesis

El perfil del proveedor atribuye a este actor la explotación de **CVE-2023-28252**, una elevación de privilegios en el controlador CLFS de Windows. No está corroborado y no se emite como hecho.

Se traslada como **hipótesis de caza** por tres razones: es una vulnerabilidad con parche disponible desde abril de 2023, es de elevación local —lo que la sitúa después del acceso inicial y antes del cifrado, el momento donde la detección tiene más valor—, y es barata de comprobar en un inventario de parches.

**Acción permitida:** verificar el estado del parche. **Acción no permitida:** atribuir a este actor una explotación observada de esa CVE sobre la base de este informe.

El resto del perfil declarado —cifrado dinámico de nombres de API, bloqueos antidepuración, terminación de Windows Defender, variante para Linux, uso de corredores de acceso inicial, adjuntos de suplantación dirigida— **no genera ninguna acción** porque no lleva ni un indicador asociado ni una referencia.

---

## 14. Brechas de inteligencia y requisitos de colección

**G-1. No sabemos cuántas víctimas tiene este actor en el semestre.** Es la brecha principal y la que impide que este expediente sea un perfil.
→ **I-1.** Lectura del sitio de filtración activo, agrupando ficheros por organización. Requiere acceso a la red oscura. **Disparador:** cualquier tanda nueva de más de veinte entradas.

**G-2. La ausencia de víctimas latinoamericanas no es demostrable** con el 8 % de cobertura de país.
→ **I-2.** Contrastar el catálogo con el otro rastreador de la cartera, que puebla el país con más frecuencia. **Disparador:** inmediato; sostiene `KJ-5`.

**G-3. El perfil del actor no está corroborado en ningún punto**, incluida la CVE de `X-1`.
→ **I-3.** Buscar análisis primario de proveedor con muestra y referencias. **Disparador:** antes de emitir cualquier juicio técnico.

**G-4. No sabemos si el artefacto de granularidad es del rastreador o del sitio.** Es `H-2`, y decide de quién es el error.
→ **I-4.** Comparar una entrada-fichero con la ficha correspondiente en el sitio.

**G-5. Cuarenta y ocho direcciones inactivas podrían reactivarse.** La rotación por bloques lo hace plausible.
→ **I-5.** Vigilancia periódica del estado de las cincuenta y cuatro. **Disparador:** reactivación de cualquiera de las de la generación antigua.

---

# ANEXOS

## Anexo A — Indicadores

### A.1 — Infraestructura activa

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| domain | `6ft2dfh26wm3w44orpjcgviutvfp25ez2iyh5ego5egvfmifrws7vvqd.onion` | Activo. **El sitio que sirvió las 142 entradas del 05-09** | Alta | 90 días | Vigilancia |
| domain | `dkeqrg3fxrijolpgpbsmk6eacare4bg5awrracxdiestki2onyz5bnyd.onion` | Activo al 2026-11-19 | Alta | 90 días | Vigilancia |
| domain | `emdnfl2fv32jhssxcbxlo6dzg2at4d7qbw2md6inz63qzdfgyln5cwyd.onion` | Activo. **Campos de estado contradictorios** (`O-3.1`) | Moderada | 90 días | Vigilancia |
| domain | `lhsxojxowgtwdqlryl72d2v5cpgqv3sll4d47yyqdisersigvfbl5uid.onion` | Activo. Campos contradictorios | Moderada | 90 días | Vigilancia |
| domain | `mejouwrwja4iou7myj34rqi7cixyhn7vsa42e2n2dhxzc5mmkiaki3yd.onion` | Activo | Alta | 90 días | Vigilancia |
| domain | `rpoeu7zimfpwxbwmjmjyprqaprtvkj3ykfczhbc4x3voydopffn337id.onion` | Activo, **última exploración 26-10**: el más dudoso de los seis | Baja | 30 días | Vigilancia |
| domain | `nxetaioe4eelwhdwagi3ikv6ee6tttwvnqikalgkrslz7bwvuwqzdeqd.onion` | Sirvió 62 entradas. **Inactivo**, puede volver (`G-5`) | Alta como registro | 90 días | Vigilancia |
| domain | `ltxnzpfvmr3c3rcbw5x4q2ejy6fmbp7kc35oql3gooyydg7belfmnyad.onion` | Sirvió 47 entradas. Inactivo | Alta como registro | 90 días | Vigilancia |
| domain | `vkvsgl7lhipjirmz6j5ubp3w3bwvxgcdbpi3fsbqngfynetqtw4w5hyd.onion` | **«BrainCipher Dataleak»**, generación antigua. Estado indeterminable | Baja | 90 días | Vigilancia |
| domain | `mybmtbgd7aprdnw2ekxht5qap5daam2wch25coqerrq2zdioanob34ad.onion` | **«Brain Cipher Client Area»**: el portal de negociación. Inactivo desde 08-2026 | Alta como registro | Histórico | Análisis |
| artefacto | **54 direcciones registradas · 6 activas · rotación en 4 tandas** | `O-3.1`. **El bloqueo por dirección no sirve** | Alta | 90 días | Análisis |
| pattern | **Ausencia de prefijo legible en las 54 direcciones** | Decisión opuesta a krybit. **No cazable por patrón** | Alta como observación | Sin caducidad | Análisis |

### A.2 — Falsos positivos a retirar

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| artefacto | **`aws.amazon.com` NO es víctima de este actor** | El enriquecedor lo infirió de `aws.partNN.rar` con confianza 0,95 (`E-2`) | **Alta** | Sin caducidad | **Retirar si entró en alguna lista** |
| artefacto | **`officefiles.com`, `studiodata.com`, `eworldme.com`, `windiam.com`, `managers-share.com`, `studioadviser.com` NO son víctimas** | Los otros cinco dominios inferidos de nombres de fichero | Alta | Sin caducidad | **No ingerir** |
| artefacto | **La cifra de 432 entradas no es un recuento de víctimas** | 429 son nombres de fichero (`KJ-1`). **Un segundo agregador da 64–110 víctimas en todo el historial** (`E-1.2`) | Alta | Sin caducidad | **No citar en comparaciones de volumen** |
| pattern | **Título de entrada con forma `nombre.partNN.rar` o extensión de archivo** | **El detector del artefacto** (`Anexo D`), un minuto de coste | Alta como método | Sin caducidad | **Filtrar antes de contar** |
| artefacto | **0 de 432 entradas con fecha de publicación** | Único del lote, y consecuencia de `KJ-1`: un fichero no tiene fecha de publicación | Alta | Sin caducidad | **Señal secundaria del artefacto** |

### A.3 — Victimología, con su salvedad

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| cartera | **432 entradas · 429 ficheros · 3 posibles víctimas · 8 días** | La anatomía del artefacto | Alta como recuento | 90 días | Medición |
| cartera | **34 de 432 con país (8 %)** · 6 países · **0 LATAM · 0 Chile** | `KJ-5`. **La ausencia no es demostrable** | **Baja** | 90 días | **No concluir ausencia** |
| cartera | **73 de 432 con captura (17 %) · 43 con dominio (10 %)** | El perfil probatorio más pobre del lote, y por la misma causa | Alta como recuento | 90 días | Medición |
| cartera | **Portal de cliente separado del sitio de filtración** en la generación antigua | Criterio 1 del triaje de `CTI-2026-042`: **portal ⇒ operación, no herramienta** | Moderada | Histórico | Clasificación |
| cve | **CVE-2023-28252** (CLFS, elevación local) | **Hipótesis de caza, no hecho.** Del perfil no corroborado (`X-1`) | **Baja** | Hasta corroboración | **Verificar parche. No atribuir** |

## Anexo B — Fuentes y valoración

| # | Fuente | Grado | Qué aportó | Salvedad |
|---|---|---|---|---|
| 1 | API de cti.fyi, entradas y ficha de grupo, 2026-11-19 | **Medición propia** sobre datos de proveedor | Las 432 entradas, los 54 sitios, los recuentos | Evaluada en `CTI-2026-054`. **El artefacto de este informe es un séptimo defecto de esa fuente** |
| 2 | Ficha de perfil del grupo, misma fuente | **Proveedor, con indicio de redacción sintética** | El linaje LockBit 3.0, la CVE de `X-1`, el origen indonesio | **No corroborada en ningún punto.** Registro textual y caracteres de espacio fino indican generación automática |
| 3 | `CTI-2026-054` §O-5 y §O-7.1 | Propio | El comportamiento de la puntuación de confianza y la contradicción de campos de estado | — |
| 4 | `CTI-2026-042` Anexo D | Propio | El triaje de `O-4` | — |
| 5 | `CTI-2026-049` | Propio | La regla de higiene sobre nombres de fichero con datos de persona física (`§3.3`) | — |
| 6 | **CTIWatch**, ficha pública del actor, consultada el 2026-11-19 | Proveedor, **con prosa generada automáticamente declarada por la propia fuente** | **La corroboración independiente del orden de magnitud** de `E-1.2`: 64–110 víctimas frente a 432 entradas | **Sus dos cifras se contradicen entre sí.** No se adopta ninguna como recuento, sólo el orden de magnitud. Evaluada en `CTI-2026-054` `§O-8`. Su `robots.txt` prohíbe el uso de la API: se consultó la página pública |

## Anexo C — Léxico de probabilidad y confianza

ICD 203. **Casi con certeza** ≥99 % · **muy probable** 80–95 % · **probable** 55–80 % · **posible** 40–60 % · **improbable** 20–45 % · **muy improbable** 5–20 %. La **confianza** califica la base de prueba. En este informe las mediciones del artefacto llevan confianza alta; **`KJ-5` lleva confianza baja y es el juicio más frágil**; `KJ-6` lleva confianza baja por tratarse de un perfil de proveedor sin referencias.

## Anexo D — Cómo detectar que un recuento de víctimas está contando ficheros

Un minuto de coste, y resuelve el caso.

**Paso 1 — Mirar los títulos, no el total.** Diez títulos al azar bastan. Si alguno tiene extensión de archivo, o termina en barra, o es una cadena como `SQL`, sospechar.

**Paso 2 — Buscar series numeradas.** `nombre.part01.rar`, `.part02`, `.part03`. **Es la firma inequívoca**: ninguna organización se llama así, y una serie de doce volúmenes es un archivo, no doce víctimas.

**Paso 3 — Comparar entradas con días de actividad.** Cuatrocientas treinta y dos entradas en ocho días no es actividad: es volcado. Un actor real reparte.

**Paso 4 — Comprobar la cobertura de la fecha de publicación.** Un fichero no tiene fecha de publicación. **Cero de 432 es una señal potentísima**, y es gratis de mirar.

**Paso 5 — Desconfiar del enriquecimiento, sobre todo cuando está completo.** Si el enriquecedor ha asignado dominio, país y sector a un título que es un nombre de fichero, **los tres son inventados**, y la puntuación de confianza será alta precisamente por eso (`E-2`).

> **El paso más barato es el cuarto y el más concluyente el segundo.** Y la conclusión general va más allá de esta fuente: **un recuento de víctimas es un recuento de fichas, y una ficha no siempre es una víctima.** La cartera ya había tropezado con lo contrario —un actor que publica varias fichas de la misma víctima, en `CTI-2026-050`—; éste es el caso simétrico y mucho más grave, porque multiplica por cien en lugar de por dos.

## Anexo E — Marcos de referencia empleados

ICD 203. Escala de Almirantazgo con los grados propios de la cartera. TLP 2.0 y PAP. Triaje de actor nuevo de `CTI-2026-042` `Anexo D`. Escala de prueba de ocho niveles de `CTI-2026-048` `Anexo D`, aplicada al perfil de proveedor de `KJ-6`. CVE y CVSS para `X-1`. **No se emite mapa ATT&CK**: no hay ni una técnica observada, y el perfil del proveedor no es base suficiente, por la misma razón que en `CTI-2026-048`.

## Anexo F — Paquete legible por máquina

| Medición | Procedimiento |
|---|---|
| Entradas | `GET /api/v1/posts?group=BrainCipher&since=2026-05-19&limit=500` |
| Infraestructura | `GET /api/v1/groups/BrainCipher` → `locations[]` |
| Criterio de nombre de fichero | Expresión regular sobre el título: extensión en `{rar,zip,7z,pdf,png,jpg,txt,sql,csv,xls,doc,tar,gz,bak,eml,msg,pst,vmdk,iso}`, o patrón `\.part\d+\.(rar\|zip\|7z)$`, o `\.z\d{2}$`, o terminación en `/` |
| Resultado | **429 de 432** |
| Falsos positivos | Agrupar `enriched_metadata.domain` sobre las entradas que cumplen el criterio |

## Anexo G — Control de cambios

| Versión | Fecha | Qué cambió | Qué juicio se movió |
|---|---|---|---|
| 1.0 | 2026-11-19 | Emisión inicial. **El expediente se abrió para perfilar al segundo actor del semestre y acabó documentando por qué no lo es.** Incluye la corroboración independiente de `E-1.2`, incorporada el mismo día desde una cuarta fuente | — |

## Anexo H — Realimentación del consumidor

Este informe se corrige si se recibe: un recuento de víctimas reales del semestre, que convertiría este expediente en un perfil (`I-1`); evidencia de que el sitio publica una ficha por fichero, lo que trasladaría el artefacto del rastreador al actor (`I-4`); una víctima latinoamericana en su catálogo, que invalidaría `KJ-5`; o un análisis primario con muestra, que permitiría emitir nivel técnico (`I-3`).

El disparador más urgente es **`I-2`**, porque `KJ-5` es el juicio más débil del informe y el que una organización de la región usaría para despriorizar este actor.
