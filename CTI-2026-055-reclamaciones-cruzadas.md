---
tlp: "TLP:CLEAR"
pap: "PAP:WHITE"
id: "CTI-2026-055"
version: "1.1"
tipo: "Método analítico"
foco_regional: "Global · España y Chile como casos"
niveles: ["Estratégico", "Operacional"]
autor: "Célula CTI"
actor: "Multiactor · 237 grupos en reclamaciones cruzadas"
fecha: "2026-11-19"
caduca: "2027-02-19"
distribucion: "Método para separar los cuatro fenómenos que se esconden detrás de 'dos grupos reclamaron la misma víctima'. Aplicado a 1.895 agrupaciones de un rastreador de terceros y a tres preguntas que la cartera tenía abiertas. No se reproduce ningún nombre de víctima que no esté ya publicado por el propio actor. Difusión libre conservando la atribución y las salvedades de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-055

## Dos grupos reclamando la misma víctima significa cinco cosas distintas, y cuatro de ellas no son multi-extorsión

### Método de tres ejes, y lo que responde: Lynx no heredó el expediente de INC, y SoulGroup republicó el de insomnia noventa y cuatro días después

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-055` |
| Versión | 1.0 |
| Tipo | Método analítico |
| Clasificación | `TLP:CLEAR` · `PAP:WHITE` |
| Fecha de emisión | 2026-11-19 |
| Caducidad | 2027-02-19 |
| Niveles | Estratégico · Operacional |
| Objeto | 1.895 agrupaciones de víctima con dos o más grupos reclamantes |
| Grupos implicados | 237 |
| Ventana de validación | 2026-05-19 a 2026-11-19 |
| Dependencia | `CTI-2026-054` §O-2 para los defectos de la fuente |
| Autor | Célula CTI |

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** **«Dos grupos reclamaron la misma víctima» agrupa cuatro fenómenos que exigen respuestas opuestas, y el agregado de 1.895 casos los suma como si fueran uno.** Son el alias de expediente —el mismo sitio indexado dos veces—, el rebranding sucesivo —un actor que hereda el catálogo de otro—, la reventa o republicación parcial, y la colisión genuina de dos operaciones sobre una misma víctima. Valoramos **casi con certeza** *(≥99 %)* que los cuatro están presentes en el conjunto. **Confianza: alta.** *Consecuencia:* la cifra agregada **no es interpretable**, y la mayor parte de lo que contiene no es multi-extorsión (`E-1`).

**KJ-2.** **Los tres ejes que los separan son el solapamiento de catálogo, la separación temporal y la unanimidad de la dirección, y con ellos la clasificación es inequívoca.** Un alias de expediente comparte el 90 % o más del catálogo con separación mediana **de cero días** y dirección repartida al azar: `hive`/`hiveleak` comparten 193 de 194 víctimas con separación de 0,0 días en los percentiles 10 y 90. Un rebranding comparte catálogo igual de alto pero con separación **consistente y dirección unánime**: `eldorado` precede a `blacklock` en 179 días en el **100 %** de los 47 casos. Una reventa comparte sólo una fracción: `lockbit3` precede a `dispossessor` en 338 días pero comparten el **39 %**. Valoramos **casi con certeza** *(≥99 %)* la capacidad discriminante de los tres ejes sobre este conjunto. **Confianza: alta.** *Consecuencia:* once pares de alias quedan identificados, cuatro de ellos **con nombres sin ningún parecido léxico** (`O-2`).

**KJ-3.** **Aplicado a la pregunta que `CTI-2026-047` dejó abierta, el método la responde con una prueba más fuerte que la que entonces tuvimos: Lynx no es el rebranding de INC Ransom, y la razón es que no comparten ni una víctima.** De las 72 víctimas contestadas en que participa uno de los dos, **las comunes son cero**. Un rebranding hereda el catálogo —`eldorado`/`blacklock` comparten el 96 %, `hive`/`hiveleak` el 99 %—; estos dos comparten el 0 %, y ambos publican dentro del semestre. Valoramos **muy probable** *(80–95 %)* que la hipótesis del rebranding sea falsa. **Confianza: alta**, y es una **segunda prueba independiente**: en `CTI-2026-047` el argumento fue la simultaneidad de publicación, y éste es el de los catálogos disjuntos (`E-2`).

**KJ-4.** **Y responde otra que `CTI-2026-053` dejó explícitamente abierta: SoulGroup no es una operación nueva, es el catálogo de insomnia republicado noventa y cuatro días después.** Dieciséis de las veintisiete entradas de SoulGroup (**59 %**) corresponden a víctimas ya publicadas por `insomnia` entre agosto y septiembre de 2026. La dirección es unánime —**16 casos de 16** con SoulGroup posterior— y la separación es consistente: mediana de **94 días**, con el 100 % de los casos entre 57 y 94. Valoramos **muy probable** *(80–95 %)* que SoulGroup sea marca sucesora o republicadora de insomnia y **no** una operación con capacidad propia. **Confianza: alta para el solapamiento, moderada para la interpretación.** *Consecuencia:* explica lo que aquel informe no pudo explicar —veinticinco entradas en un solo ciclo de observación— y **cambia el juicio central de `CTI-2026-053`** (`E-3`).

**KJ-5.** **La multi-extorsión genuina y simultánea es rarísima: ninguna colisión por debajo de una hora en todo el semestre, y una sola por debajo de veinticuatro.** De las 44 agrupaciones con dos grupos distintos reclamando dentro de la ventana, el 68 % tiene separaciones superiores a treinta días. El único caso por debajo de un día es una empresa italiana de servicios profesionales reclamada por `cmdorganization` y `imnotavillain` con **0,3 días** de separación. Valoramos **casi con certeza** *(≥99 %)* la escasez. **Confianza: alta.** *Consecuencia:* el escenario que los equipos temen —dos operaciones extorsionando a la vez— es el menos frecuente de los cuatro, y **lo que de verdad ocurre es la reaparición meses después** (`E-4`).

**KJ-6.** **El par más relevante para esta cartera no es ni alias ni rebranding: Qilin y TheGentlemen comparten nueve víctimas con dirección aleatoria y dispersión de ±170 días, que es la firma del acceso compartido.** Comparten el 7 % del catálogo contestado, la separación mediana es de **−0,6 días** pero con percentil 10 en −172 y percentil 90 en +158, y la dirección se reparte **56 % / 44 %**. Valoramos **probable** *(55–80 %)* que el patrón se explique por corredor de acceso común o afiliados operando en ambas marcas, y **muy improbable** *(5–20 %)* que sea alias o sucesión. **Confianza: moderada**, con nueve casos. *Consecuencia:* los dos actores de mayor relevancia regional de la cartera **tocan el mismo conjunto de víctimas sin ser el mismo actor**, y eso es un requisito de colección, no una conclusión (`O-4`, `G-2`).

**KJ-7.** **Para una organización, la consecuencia práctica invierte la intuición: ser reclamada por un segundo grupo es, casi siempre, el mismo robo reapareciendo, no un robo nuevo.** De los cuatro fenómenos, tres implican que **no hubo segundo acceso**: el alias es un artefacto del observador, el rebranding es el mismo operador con otro nombre, y la reventa es un tercero que compró o recicló datos ya exfiltrados. Valoramos **muy probable** *(80–95 %)* que ante una segunda reclamación la hipótesis inicial correcta sea la reaparición. **Confianza: moderada.** *Consecuencia:* la respuesta primera no es activar la gestión de un incidente nuevo sino **comparar la muestra publicada con la del primero** (`O-5`, `Anexo D`).

**KJ-8.** **Añadido en v1.1: hay una quinta clase, y la descubrió un expediente de actor del mismo lote.** `CTI-2026-061` documenta un actor cuyo modelo declarado permite a los afiliados **publicar bajo sus propias marcas**, y verifica que uno de esos afiliados coaparece con la marca matriz sobre una misma víctima. Eso no es alias de expediente —son dos marcas reales y deliberadas—, ni rebranding —coexisten—, ni reventa —hay un acceso y dos publicadores—, ni colisión —no son independientes—. Valoramos **probable** *(55–80 %)* que la clase exista como fenómeno distinto. **Confianza: moderada**, con una sola coaparición verificada. *Consecuencia incómoda:* **su firma es casi indistinguible de la del acceso de origen común** de `O-4`, y lo único que las separa es una declaración de modelo procedente de una ficha de proveedor no corroborada. Si no se pueden distinguir sin ella, **las dos clases deben fundirse** (`O-7`, `G-6`).


---

## 2. Resumen ejecutivo

La fuente evaluada en `CTI-2026-054` ofrece una capacidad que ninguna otra de la cartera tiene: localizar víctimas reclamadas por más de un grupo de extorsión, con la promesa de identificar corredores de acceso compartidos, afiliados operando en varias marcas a la vez y reventa de datos. Devuelve **1.895 agrupaciones** y destaca **706 colisiones en menos de veinticuatro horas**.

Este informe sostiene que la cifra agregada no es interpretable, y no porque la fuente mienta, sino porque **la pregunta está mal planteada**. «Dos grupos reclamaron la misma víctima» describe cuatro situaciones que exigen respuestas distintas y que, mezcladas, se anulan.

La primera es la más abundante y la menos interesante: **el mismo sitio de filtración está indexado dos veces** bajo nombres distintos. `hive` y `hiveleak` aparecen juntos en 193 víctimas; `killsec` y `killsecurity` en 141. No hay dos grupos: hay un expediente duplicado. La segunda es el **rebranding sucesivo**, donde un actor se renombra y arrastra su catálogo: `eldorado` se convierte en `blacklock`. La tercera es la **reventa o republicación**, donde un tercero publica parte de lo que otro ya había publicado: `dispossessor` lleva años haciéndolo con material de `lockbit3`. Y la cuarta, la única que corresponde a la promesa del endpoint, es la **colisión genuina**: dos operaciones independientes extorsionando a la misma organización.

El método que aquí se propone las separa con tres mediciones. **Cuánto catálogo comparten** —el índice de Jaccard sobre el conjunto de víctimas—, **cuánto tiempo las separa**, y **si la dirección es unánime**. Las tres juntas bastan: el alias comparte casi todo con separación cero y dirección aleatoria; el rebranding comparte casi todo con separación consistente y dirección unánime; la reventa comparte una fracción; y la colisión genuina comparte poco y ocurre en horas.

Aplicado al conjunto, el método identifica **once pares de alias**, cuatro de ellos con nombres que no se parecen en nada —el más notable es `j` y `l group`, que comparten **catorce víctimas de catorce**—. Y deja la cifra de multi-extorsión genuina del semestre en **un caso**: una empresa italiana reclamada por dos actores con 0,3 días de diferencia.

El valor del método, sin embargo, está en que responde tres preguntas que la cartera tenía abiertas. A la primera, planteada en `CTI-2026-047`, responde que **Lynx no es el rebranding de INC Ransom**, porque de las setenta y dos víctimas contestadas en que participa alguno de los dos no comparten ninguna, y un rebranding hereda el catálogo. A la segunda, planteada en `CTI-2026-053` y dejada expresamente sin resolver, responde que **SoulGroup republicó el catálogo de insomnia con noventa y cuatro días de retraso**, en dieciséis de sus veintisiete entradas, con dirección unánime. Y sobre la tercera —la relación entre Qilin y TheGentlemen, los dos actores de mayor relevancia regional de la cartera— responde que **comparten nueve víctimas sin ser el mismo actor**, con un patrón compatible con acceso de origen común.

La consecuencia práctica para una organización invierte la intuición. Si un segundo grupo publica su nombre, lo más probable **no** es que la hayan vuelto a atacar: es que el mismo robo esté reapareciendo con otra etiqueta. La primera acción no es abrir un incidente nuevo, sino comparar lo publicado con lo publicado la vez anterior.

---

## 3. Alcance y limitaciones

### 3.1 Base de datos y su procedencia

Las 1.895 agrupaciones proceden de cuatro consultas paginadas al endpoint de reclamaciones cruzadas de cti.fyi el 19 de noviembre de 2026. Cada agrupación trae la víctima, los grupos, el recuento de reclamaciones y, por cada reclamación, el grupo, el título, las dos fechas, la dirección y el estado.

### 3.2 El defecto de la fuente que este informe no usa

El campo de separación horaria que la propia fuente calcula **discrepa de su definición en el 41 % de los casos** y es el origen de la cifra de 706 colisiones. Está documentado en `CTI-2026-054` `§O-2`. **Este informe no lo emplea en ningún punto**: todas las separaciones temporales que aquí aparecen están recalculadas tomando la primera reclamación de cada grupo distinto.

### 3.3 Qué no se puede concluir

- **El método clasifica relaciones entre expedientes, no identidades.** Decir que dos nombres son alias del mismo sitio es una afirmación sobre el catálogo observable. **No** establece quién lo opera.
- **La distinción entre rebranding y republicación no es firme.** Ambos producen catálogo compartido con dirección unánime. Lo que los separa es si el actor anterior sigue publicando, y eso exige observación posterior. En el caso de SoulGroup, `insomnia` **sigue activo** en el semestre, lo que inclina hacia republicación; pero no lo decide.
- **El solapamiento se calcula sobre víctimas contestadas, no sobre catálogos completos.** Un par de actores que comparta víctimas que la fuente no haya agrupado no aparece. El método detecta, no descarta.
- **Ninguna víctima ha confirmado nada.** Todo procede de reclamaciones de adversario.

### 3.4 Higiene

Se nombran organizaciones sólo cuando el propio actor las publicó con nombre completo y lo mantiene. Las entradas con nombre enmascarado, y el caso documentado en `CTI-2026-054` `§E-3` de un nombre revelado y vuelto a ocultar, **no se reproducen**.

### 3.5 Veredicto por nivel

| Nivel | Veredicto | Motivo |
|---|---|---|
| Estratégico | **Utilizable** | Los cuatro fenómenos y su proporción relativa están medidos |
| Operacional | **Utilizable** | El método de `Anexo D` es reproducible con los datos del `Anexo F` |
| Táctico | **No aplica** | El método no produce TTP |
| Técnico | **No aplica** | No produce indicadores de ejecución |

---

# NIVEL ESTRATÉGICO

## E-1. Los cuatro fenómenos, y cuánto pesa cada uno

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `1.895` | Agrupaciones que la fuente declara | Toda su historia, desde 2022 |
| `237` | Grupos distintos implicados | De 425 del catálogo |
| `1.759` | Agrupaciones con exactamente dos grupos | **93 % del total** |
| `44` | **Con dos grupos distintos dentro del semestre** | `KJ-5` |
| `0` | **Por debajo de una hora de separación** | En el semestre |
| `1` | Por debajo de veinticuatro horas | 0,3 días |
| `68 %` | De las 44, con más de treinta días de separación | **El fenómeno dominante es la reaparición** |
| `11` | Pares de alias identificados | Cuatro sin parecido léxico |

El conjunto completo tiene una estructura muy sesgada: el 93 % de las agrupaciones tiene exactamente dos grupos, y los participantes más frecuentes son precisamente los pares de alias.

| Grupo | Víctimas contestadas | Su par |
|---|---|---|
| `lockbit3` | 283 | — |
| `dispossessor` | 263 | — |
| `hiveleak` | 194 | **`hive` (193)** |
| `hive` | 193 | **`hiveleak` (194)** |
| `clop` | 164 | — |
| `killsec` | 143 | **`killsecurity` (141)** |
| `killsecurity` | 141 | **`killsec` (143)** |
| `qilin` | 112 | — |
| `raworld` | 95 | **`ragroup` (95)** |
| `ragroup` | 95 | **`raworld` (95)** |
| `apt73` | 85 | **`bashe` (83)** |
| `bashe` | 83 | **`apt73` (85)** |

**La simetría de los recuentos es la primera señal, y se ve a simple vista.** Cuando dos expedientes son el mismo sitio, cada víctima del uno es víctima del otro, y los totales quedan casi idénticos: 193 y 194, 143 y 141, 95 y 95, 85 y 83. Es el indicio más barato de todo el método.

## E-2. La pregunta de INC y Lynx, respondida con una prueba nueva

`CTI-2026-047` abordó una afirmación muy repetida en la literatura de proveedor: que **Lynx es el rebranding de INC Ransom**. Aquel informe la calificó de falsa con un argumento temporal —ambas marcas publican simultáneamente a lo largo de 2026, y un rebranding implica sucesión, no coexistencia— y propuso tratarlas como **marcas hermanas**.

El método de este informe aporta una segunda prueba, independiente de la primera y más difícil de explicar de otro modo.

| Medición | `incransom` / `lynx` | Un rebranding real: `eldorado` / `blacklock` | Un alias real: `hive` / `hiveleak` |
|---|---|---|---|
| Víctimas contestadas de A | 44 | 48 | 193 |
| Víctimas contestadas de B | 28 | 48 | 194 |
| **Víctimas comunes** | **0** | **47** | **193** |
| Solapamiento (Jaccard) | **0 %** | **96 %** | **99 %** |
| Dirección unánime | — | **100 %** | No (10 %) |

**De las setenta y dos víctimas contestadas en que participa uno de los dos, ninguna aparece en los dos catálogos.** Un actor que se renombra arrastra su expediente: eso es lo que significa heredar una marca. Aquí no hay herencia de ninguna clase.

Y la coexistencia que `CTI-2026-047` observó se confirma en la ventana de este informe: `incransom` publica **248 entradas** entre el 19 de mayo y el 17 de noviembre, y `lynx` publica **7** entre el 11 de junio y el 29 de agosto. Ambos activos, catálogos disjuntos.

> **Lo que no se puede concluir.** Que no haya rebranding no significa que no haya relación. Dos marcas pueden compartir operadores, código o afiliados y mantener catálogos separados deliberadamente. El método descarta la sucesión, **no el parentesco**.

## E-3. SoulGroup, y la pregunta que `CTI-2026-053` dejó abierta a propósito

`CTI-2026-053` se emitió el mismo día en que SoulGroup fue observado por primera vez. Documentó veintiséis entradas publicadas en un intervalo muy corto, cero fuentes independientes, un criterio de triaje cumplido de siete, y se clasificó como **reclamación sin respaldo, pendiente de evidencia**. Su juicio `KJ-1` planteaba dos posibilidades sin poder elegir: víctimas acumuladas antes de abrir escaparate, o sitio sembrado.

**Era ninguna de las dos.**

| Medición | Resultado |
|---|---|
| Entradas de SoulGroup en el semestre | 27 |
| De ellas, víctimas ya publicadas por `insomnia` | **16 (59 %)** |
| Casos en que SoulGroup es posterior | **16 de 16 (100 %)** |
| Separación mediana | **94,0 días** |
| Separación mínima / máxima | 57 / 94 días |
| `insomnia` activo en el semestre | **Sí, 23 entradas** |

Las dieciséis víctimas comunes son organizaciones estadounidenses de sanidad, servicios jurídicos y administración local, más una española y una alemana, publicadas por `insomnia` entre el 9 de agosto y el 15 de septiembre de 2026 y reaparecidas en SoulGroup **el 11 de noviembre**.

Esto explica lo que aquel informe no pudo explicar: **veinticinco de las veintisiete entradas aparecen con la misma marca de observación** —un único ciclo de sondeo— porque el catálogo no se construyó, **se copió**. Y permite precisar una medición propia de entonces: la ventana de «trece minutos» que `CTI-2026-053` midió era el intervalo entre dos sondeos del rastreador, no la duración real de la publicación. Es la misma lección de `CTI-2026-045` `§O-5.2` —las marcas de tiempo son horas de observación—, aplicada ahora contra nuestra propia medición.

### E-3.1 Republicación o sucesión, y por qué importa la diferencia

El método no distingue por sí solo entre un actor que hereda una marca y uno que republica el material de otro. Lo que inclina la balanza es que **`insomnia` sigue publicando**: 23 entradas en el semestre, la última el 14 de noviembre, tres días después de la aparición de SoulGroup. Si fuera sucesión, el predecesor habría callado.

Valoramos **probable** *(55–80 %)* que se trate de republicación —SoulGroup usando material ajeno, comprado o reciclado— y **posible** *(40–60 %)* que haya relación operativa entre ambos. **La diferencia importa a la víctima:** si es republicación, no hubo segundo acceso y los datos son los de agosto; si hay relación operativa, el acceso original pudo no haberse cerrado.

## E-4. Lo que de verdad ocurre, y lo que se teme que ocurra

| Fenómeno | Qué implica para la víctima | Frecuencia en el semestre |
|---|---|---|
| **Alias de expediente** | **Nada.** Artefacto del observador | Dominante en el histórico |
| **Rebranding sucesivo** | El mismo operador con otro nombre. **No hubo segundo acceso** | 4 pares identificados |
| **Reventa / republicación** | Un tercero publica datos ya exfiltrados. **No hubo segundo acceso** | **68 % de las 44** |
| **Colisión genuina** | Dos operaciones distintas. **Pudo haber dos accesos** | **1 caso de 44** |

El escenario que los equipos de respuesta temen —dos grupos extorsionando a la vez— es el más raro de los cuatro. Lo que de verdad pasa, en más de dos tercios de los casos recientes, es que **el material reaparece meses después**.

Eso cambia la prioridad. Un programa que vigile su propio nombre en sitios de filtración debería estar preparado no para la colisión simultánea, sino para **la reaparición a los tres meses**, que es el caso modal y para el que la respuesta es distinta: no contención, sino verificación de que lo publicado es el mismo conjunto de datos.

---

# NIVEL OPERACIONAL

## O-1. Los tres ejes

**Eje 1 — Solapamiento de catálogo.** Índice de Jaccard sobre el conjunto de víctimas contestadas de cada grupo: víctimas comunes dividido por víctimas de la unión. Mide si los dos expedientes describen el mismo conjunto de hechos.

**Eje 2 — Separación temporal.** Para cada víctima común, la diferencia entre la primera reclamación de cada grupo. Se reportan mediana, percentil 10 y percentil 90: **la dispersión importa tanto como el centro**.

**Eje 3 — Unanimidad de la dirección.** Proporción de casos en que el mismo grupo reclama primero. Es el eje que `CTI-2026-045` `Anexo D` enseñó a buscar: **el parámetro que no se alinea**. Un alias no tiene dirección; una sucesión la tiene al 100 %.

### O-1.1 La tabla de decisión

| Eje 1 (Jaccard) | Eje 2 (separación) | Eje 3 (dirección) | Clase |
|---|---|---|---|
| ≥ 90 % | **≈ 0 días**, p10 y p90 estrechos en torno a 0 | 30–70 % | **Alias de expediente** |
| ≥ 85 % | Consistente, p10 y p90 del mismo signo | **≥ 95 %** | **Rebranding o republicación** |
| 20–50 % | Grande | ≥ 95 % | **Reventa parcial** |
| < 20 % | **< 24 horas** | — | **Colisión genuina** |
| < 20 % | Grande, p10 y p90 de signo opuesto | ~50 % | **Acceso de origen común** (`O-4`) |
| **< 20 %** | **Pequeña, días** | **~50 %**, + **declaración de modelo de afiliados** | **Dos marcas de una operación** (`O-7`, añadido en v1.1) |

## O-2. Los once pares de alias

| A | B | n(A) | n(B) | Comunes | Jaccard | Separación mediana | A primero |
|---|---|---|---|---|---|---|---|
| `ragroup` | `raworld` | 95 | 95 | 95 | **100 %** | 0,0 d | 47 % |
| `j` | `l group` | 14 | 14 | 14 | **100 %** | 452,0 d | 0 % |
| `hive` | `hiveleak` | 193 | 194 | 193 | 99 % | **0,0 d** | 10 % |
| `killsec` | `killsecurity` | 143 | 141 | 141 | 99 % | −0,0 d | 65 % |
| `ransomed` | `ransomedvc` | 52 | 53 | 52 | 98 % | −0,4 d | 58 % |
| `apt73` | `bashe` | 85 | 83 | 83 | 98 % | 20,1 d | 19 % |
| `blacklock` | `eldorado` | 48 | 48 | 47 | 96 % | **−178,7 d** | **100 %** |
| `dunghill` | `dunghill_leak` | 13 | 14 | 13 | 93 % | −0,0 d | 54 % |
| `unsafe` | `unsafeleak` | 11 | 10 | 10 | 91 % | 4,8 d | 10 % |
| `medusalocker` | `ransomblog_noname` | 51 | 46 | 46 | 90 % | 0,0 d | 35 % |
| `insomnia` | `soul` | 17 | 17 | 16 | 89 % | **94,0 d** | **0 %** |

**Leída con los tres ejes, la tabla se parte en dos mitades.** Los que tienen separación en torno a cero y dirección repartida —`ragroup`/`raworld`, `hive`/`hiveleak`, `killsec`/`killsecurity`, `ransomed`/`ransomedvc`, `dunghill`/`dunghill_leak`, `medusalocker`/`ransomblog_noname`— son **expedientes duplicados**: el mismo sitio visto dos veces. Los que tienen dirección unánime y separación consistente —`blacklock`/`eldorado` a 179 días, `j`/`l group` a 452, `insomnia`/`soul` a 94, y `nova`/`ralord` a 13— son **sucesión o republicación**.

### O-2.1 Los cuatro que el parecido de nombres no detecta

Un filtro léxico —uno de los nombres contenido en el otro— encuentra `hive`/`hiveleak`, `killsec`/`killsecurity`, `ransomed`/`ransomedvc`, `dunghill`/`dunghill_leak` y `unsafe`/`unsafeleak`. **No encuentra estos:**

- **`j` y `l group`**: catorce víctimas de catorce. Sin una letra en común.
- **`blacklock` y `eldorado`**: 96 % del catálogo, con `eldorado` precediendo siempre.
- **`medusalocker` y `ransomblog_noname`**: 90 %, separación cero.
- **`nova` y `ralord`**: 88 %, `ralord` precediendo en el 100 % de los casos por 13 días.

**La lección es que el nombre no es un buen detector de identidad y el catálogo sí.** Es la misma conclusión a la que llegó `CTI-2026-047` por otra vía al rechazar la hipótesis del rebranding de Lynx: lo que decide es el expediente, no la etiqueta.

## O-3. Las 44 agrupaciones del semestre

Dieciséis de las cuarenta y cuatro son el par `insomnia`/`soul` de `E-3`. Las otras veintiocho implican a veintiséis pares distintos, casi todos con una única víctima en común, lo que impide clasificarlas con los tres ejes: **con n=1 no hay dispersión ni dirección que medir**.

Las que sí admiten lectura:

| Víctima | País / Sector | Grupos | Separación | Lectura |
|---|---|---|---|---|
| Contact Srl | IT / Servicios profesionales | `cmdorganization`, `imnotavillain` | **0,3 d** | **Única candidata a colisión genuina** |
| Interim HealthCare | — / Sanidad | `anubis`, `genesis` | 4,3 d | Candidata, separación corta |
| The Excalibur Group | — / Servicios profesionales | `dark project`, `qilin` | 4,9 d | Candidata |
| StrucSure Home Warranty | US / Servicios profesionales | `incransom`, `play` | 8,4 d | Dudosa |
| eTeam | US / Servicios profesionales | `byod`, `endzone` | 9,6 d | Dudosa |
| MPA Pharma | US / Sanidad | `metaencryptor`, `rhysida` | 11,9 d | Dudosa |
| La Sevillanita | **ES / Sanidad** | `global secret group`, `krybit` | 105,0 d | Reaparición |
| Dolrad | — | `bavacai`, `medusalocker` | 125,0 d | Reaparición |

Hay además una entrada cuyo nombre de víctima es literalmente **`WARNING`**, reclamada por `endzone` e `imnotavillain`. No es una organización: es un mensaje publicado en un sitio de filtración que el agrupador trató como víctima. **Artefacto, y se consigna como tal.**

## O-4. Qilin y TheGentlemen: la quinta clase

Los dos actores de mayor relevancia regional de la cartera —`CTI-2026-015` y `CTI-2026-014`— comparten nueve víctimas contestadas. El patrón no encaja en ninguna de las cuatro clases anteriores.

| Eje | Valor | Qué descarta |
|---|---|---|
| Jaccard | **7 %** | Descarta alias y rebranding, que exigen ≥85 % |
| Separación mediana | −0,6 días | — |
| Percentil 10 / 90 | **−172,2 / +158,1 días** | **Descarta colisión simultánea** |
| Dirección | **56 % / 44 %** | **Descarta sucesión**, que exige unanimidad |

Lo característico es la combinación de **dispersión enorme con dirección aleatoria**. No es que uno siga al otro: unas veces va primero Qilin y otras TheGentlemen, con meses de diferencia en ambos sentidos. Eso es incompatible con que uno herede del otro, y también con que se encuentren por casualidad nueve veces.

La explicación más económica es que **ambos obtienen acceso de la misma fuente** —un corredor de acceso inicial, o afiliados que trabajan para las dos marcas— y lo exploten en momentos distintos. Es exactamente lo que el endpoint promete detectar, y es el único caso del conjunto donde la promesa se cumple.

**Esto no es una conclusión, es un requisito de colección.** Nueve casos son pocos, y la hipótesis alternativa —que ambos ataquen de forma independiente a un mismo segmento de víctimas— no está descartada. Va a `G-2`.

Un patrón de la misma forma aparece, con muestras aún menores, en `qilin`/`lynx` (4 comunes, 75 % de dirección) y en los tres pares de `krybit` con `incransom`, `global secret group` y `netrunner`, cada uno con una sola víctima común.

## O-7. La quinta clase: dos marcas de una misma operación por diseño

**Añadido en v1.1.** La emisión de `CTI-2026-061` el mismo día que este informe
obligó a ampliar la tabla de `O-1.1`.

Aquel expediente documenta un actor cuyo perfil declara un **mercado de marca
blanca**: los afiliados despliegan la carga de la plataforma y **publican las
víctimas bajo sus propios nombres comerciales**. El perfil nombra dos afiliados,
y se verificó que uno de ellos existe como expediente separado con 111 entradas
propias **y coaparece con la marca matriz en una víctima contestada**.

Esa coaparición no encaja en ninguna de las cuatro clases:

| Clase de `O-1.1` | Por qué no encaja |
|---|---|
| Alias de expediente | **No**: son dos marcas reales y deliberadas del adversario, no un error de indexación del rastreador |
| Rebranding o republicación | **No**: coexisten en el tiempo, y el solapamiento de catálogo es mínimo en lugar del 85 % que la clase exige |
| Reventa parcial | **No**: no hay transferencia de datos entre dos actores; hay **un acceso y dos publicadores** |
| Colisión genuina | **No**: no son operaciones independientes |

**La quinta clase, y su firma:**

| Eje | Valor esperado |
|---|---|
| 1. Solapamiento de catálogo | **Muy bajo**: cada afiliado publica lo suyo, y sólo coinciden cuando ambos publican el mismo caso |
| 2. Separación temporal | **Pequeña**, del orden de días |
| 3. Dirección | **Sin unanimidad** |
| **4. Requisito añadido** | **Existencia de una declaración de modelo** que vincule las marcas |

### O-7.1 El problema, y es serio

**Los tres primeros ejes de esta clase son los mismos que los del acceso de
origen común** de `O-4`, el patrón que atribuimos al par Qilin/TheGentlemen:
solapamiento bajo, separación variable, dirección repartida. Las dos
situaciones producen la misma huella.

Lo único que las distingue es el cuarto requisito — y ese requisito **no es una
medición**: es una afirmación de una ficha de proveedor sin referencias y con
indicio de redacción automática, de la clase que `CTI-2026-054` `§O-8.2`
demostró capaz de contradecirse consigo misma en seis de seis casos.

Hay tres salidas posibles y conviene decir cuál se toma:

1. **Mantener las dos clases y aceptar que la asignación depende de una fuente
   débil.** Es lo que hace este informe, marcando `KJ-8` con confianza
   moderada.
2. **Fundirlas en una sola clase** —«víctimas compartidas sin sucesión ni
   duplicación»— y renunciar a distinguir el mecanismo. Es más honesto y menos
   útil.
3. **Buscar un cuarto eje que las separe sin depender de declaraciones.** La
   candidata es la **coincidencia de formato de entrada**: dos marcas que usan
   la misma plantilla de publicación, los mismos campos y el mismo estilo de
   título son más probablemente la misma plataforma que dos operaciones que
   compran al mismo corredor. **No se ha probado**, y es `I-6`.

**Se adopta la primera salida provisionalmente, con `I-6` abierto.** Fundir las
clases ahora perdería una distinción que tiene consecuencias defensivas
distintas: si son dos marcas de una plataforma, la víctima sufrió **un** acceso;
si comparten corredor, pudo sufrir **dos**.

### O-7.2 Y una consecuencia sobre el conjunto de 44

Si la quinta clase es real y frecuente, parte de las veintiocho agrupaciones de
`O-3` que quedaron sin clasificar por tener una sola víctima común podrían ser
instancias suyas. Los pares de `krybit` con `netrunner`, de `genesis` con `n0n`,
de `byod` con `endzone` o de `endzone` con `imnotavillain` —todos con una sola
coincidencia y marcas pequeñas— tienen exactamente la forma que `O-7` predice.

**No se reclasifican**, porque con n=1 no hay dispersión ni dirección que medir y
porque no hay declaración de modelo para ninguno. Pero se consigna como la
hipótesis más probable para esa cola, y refuerza `KJ-5`: **cuanto más de las 44
se explique por mecanismos estructurales, menos queda para la multi-extorsión
genuina.**

## O-5. Qué hacer si un segundo grupo publica su nombre

Procedimiento para la organización afectada, en orden de coste creciente. El primer paso resuelve la mayoría de los casos.

1. **Comparar la muestra publicada con la anterior.** Si los ficheros, las rutas, los nombres de usuario y las marcas de tiempo coinciden, es el mismo robo reapareciendo y **no hubo segundo acceso**. Coste: minutos, y sólo requiere lo que ya se conserva del primer incidente.
2. **Comprobar si el primer grupo sigue publicando.** Si calló cuando apareció el segundo, es sucesión de marca. Si sigue activo, es republicación por un tercero.
3. **Fechar la separación.** Por debajo de veinticuatro horas, es el caso raro y hay que tratarlo como dos accesos posibles. Por encima de treinta días, es reaparición en el 68 % de los casos recientes.
4. **Sólo si 1 a 3 no resuelven, abrir incidente nuevo.** Y entonces la pregunta es si el acceso original se cerró de verdad.

## O-6. Hipótesis y pre-mortem

**H-1.** *El agregado de 1.895 está dominado por alias de expediente.* **Probable** *(55–80 %)*. Apoyo: los seis participantes más frecuentes forman tres pares de alias. En contra: no se midió el conjunto completo por pares, sólo los cuarenta más frecuentes.

**H-2.** *SoulGroup republica material de insomnia sin acceso propio.* **Probable** *(55–80 %)*. Apoyo: dirección unánime, separación consistente, insomnia sigue activo. En contra: once de sus veintisiete entradas no aparecen en insomnia y podrían ser propias.

**H-3.** *Qilin y TheGentlemen comparten origen de acceso.* **Probable** *(55–80 %)*, con nueve casos.

**H-4.** *La escasez de colisiones simultáneas es real y no un artefacto de la fuente.* **Posible** *(40–60 %)*. **Es la hipótesis más débil de este informe.** Si la fuente agrupa por nombre canónico de víctima, dos grupos que nombren a la misma organización de forma distinta no se agruparían, y las colisiones simultáneas estarían infracontadas. No se pudo comprobar.

### Pre-mortem

*Si este informe está equivocado, ¿cómo lo sabremos?* **Por `H-4`.** Si el agrupador falla al unificar nombres de víctima, el conjunto de 44 está sesgado hacia los casos fáciles —organizaciones con nombre estable y dominio— y la conclusión de `KJ-5` caería. La comprobación está en `I-1`.

*El segundo modo de fallo es la clase de `O-4`.* Nueve víctimas comunes entre dos actores con 112 y 19 víctimas contestadas podría ser coincidencia si ambos atacan el mismo segmento. No lo hemos descartado, y `KJ-6` está calificado en consecuencia.

---

## 14. Brechas de inteligencia y requisitos de colección

**G-1. No sabemos cómo agrupa la fuente los nombres de víctima.** Es el sostén de `H-4` y la mayor amenaza a `KJ-5`.
→ **I-1.** Buscar en el conjunto dos reclamaciones de la misma organización bajo nombres distintos que **no** estén agrupadas. **Disparador:** inmediato; condiciona `KJ-5`.

**G-2. Nueve víctimas comunes entre Qilin y TheGentlemen no bastan para afirmar acceso compartido.**
→ **I-2.** Comparar los vectores declarados de las nueve y comprobar si hay un proveedor, un producto expuesto o un intervalo de compromiso común. **Disparador:** décima víctima común.

**G-3. No sabemos si las once entradas de SoulGroup que no están en insomnia son propias o de otro origen.**
→ **I-3.** Someterlas al mismo contraste frente a los demás actores del semestre. **Disparador:** antes de cerrar `CTI-2026-053` v1.1.

**G-4. El método no se ha validado contra un caso de rebranding documentado por una fuente judicial u oficial.** Todos los pares de `O-2` se clasificaron con los datos del propio rastreador.
→ **I-4.** Aplicarlo a un rebranding establecido en una acusación formal y comprobar que la clasificación coincide. **Es la validación externa que falta.**

**G-5. Sólo se midieron los cuarenta pares más frecuentes.** Puede haber alias en la cola larga.
→ **I-5.** Calcular los tres ejes para todos los pares con al menos tres víctimas comunes.

**G-6. Añadida en v1.1. La quinta clase de `O-7` no se distingue del acceso de origen común sin recurrir a una declaración de modelo no corroborada.** Es el problema de `O-7.1`.
→ **I-6.** Probar el **cuarto eje candidato**: coincidencia de plantilla de publicación, campos y estilo de título entre las dos marcas. **Si funciona, las clases quedan separadas por medición y no por declaración; si no, deben fundirse.** Disparador: inmediato, porque de él depende si `KJ-8` sobrevive.

---

# ANEXOS

## Anexo A — Indicadores

### A.1 — Pares de expediente a unificar antes de contar

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| pattern | **`hive` ≡ `hiveleak`** | 193 de 194 víctimas comunes, separación 0,0 d. **Mismo sitio, dos expedientes** | Alta | Sin caducidad | **Unificar antes de cualquier recuento** |
| pattern | **`killsec` ≡ `killsecurity`** | 141 comunes, separación −0,0 d | Alta | Sin caducidad | Unificar |
| pattern | **`ragroup` ≡ `raworld`** | 95 de 95, Jaccard 100 % | Alta | Sin caducidad | Unificar |
| pattern | **`apt73` ≡ `bashe`** | 83 comunes. **La propia ficha del proveedor lo declara** (`CTI-2026-054` `O-3`) | Alta | Sin caducidad | Unificar |
| pattern | **`ransomed` ≡ `ransomedvc`** | 52 de 53 | Alta | Sin caducidad | Unificar |
| pattern | **`medusalocker` ≡ `ransomblog_noname`** | 46 comunes, separación 0,0 d. **Sin parecido léxico** | Alta | Sin caducidad | Unificar |
| pattern | **`j` ≡ `l group`** | 14 de 14. **Sin una letra en común** | Alta | Sin caducidad | Unificar |
| pattern | **`dunghill` ≡ `dunghill_leak`** | 13 de 14 | Alta | Sin caducidad | Unificar |
| pattern | **`unsafe` ≡ `unsafeleak`** | 10 de 11 | Alta | Sin caducidad | Unificar |
| pattern | **`eldorado` → `blacklock`** | 47 de 48, **dirección 100 %**, 179 días. **Sucesión, no alias** | Alta | Sin caducidad | **Tratar como un actor en el tiempo** |
| pattern | **`ralord` → `nova`** | 14 comunes, dirección 100 %, 13 días | Alta | Sin caducidad | Tratar como sucesión |
| pattern | **`insomnia` → `soul`** | 16 de 27 entradas de soul, dirección 100 %, **94 días** (`E-3`) | Alta para el solapamiento | **Reevaluar en 30 días** | **Actualizar `CTI-2026-053`** |

### A.2 — Patrones de detección del método

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| pattern | **Dos expedientes con recuentos de víctimas contestadas casi idénticos** | 193/194, 143/141, 95/95, 85/83. **El indicio más barato de alias** (`E-1`) | **Alta como método** | Sin caducidad | **Primera comprobación** |
| pattern | **Jaccard ≥ 90 % con separación mediana ≈ 0 y dirección 30–70 %** | Firma del expediente duplicado | Alta como método | Sin caducidad | Unificar |
| pattern | **Jaccard ≥ 85 % con dirección ≥ 95 % y separación consistente** | Firma de sucesión o republicación | Alta como método | Sin caducidad | Tratar como un actor |
| pattern | **Jaccard 20–50 % con dirección unánime** | Firma de reventa parcial: `lockbit3`→`dispossessor`, 39 % | Alta como método | Sin caducidad | Análisis |
| pattern | **Jaccard < 20 % con dirección ~50 % y dispersión de meses en ambos signos** | **Firma de acceso de origen común.** El caso Qilin/TheGentlemen (`O-4`) | **Moderada**, n=9 | Reevaluar con n≥10 | **Requisito de colección** |
| pattern | **Separación entre reclamaciones < 24 h con Jaccard bajo** | La única colisión genuina del semestre | Alta como criterio | Sin caducidad | **Tratar como dos accesos posibles** |
| artefacto | **Agrupación cuyo nombre de víctima es un mensaje, p. ej. `WARNING`** | El agrupador trata texto del sitio como organización (`O-3`) | Alta | Sin caducidad | Descartar |
| pattern | **Jaccard < 20 % con separación de días, sin dirección, y una de las marcas declarando afiliados con nombre propio** | **La quinta clase** (`O-7`, v1.1). **Una operación, dos marcas: la víctima sufrió un acceso, no dos** | **Moderada**, n=1 | Hasta resolver `I-6` | **Clasificación provisional** |

### A.3 — Victimología de las 44

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| cartera | **44 agrupaciones en el semestre · 0 bajo 1 h · 1 bajo 24 h · 68 % sobre 30 días** | La anatomía de `KJ-5` | Alta como recuento | 90 días | Medición |
| cartera | **16 de las 44 son un solo par**, `insomnia`/`soul` | **El 36 % del conjunto reciente es un único fenómeno** | Alta | 90 días | Análisis |
| cartera | **1 víctima española**, sanidad, reclamada por `global secret group` y `krybit` a 105 días | **El único caso de relevancia hispanohablante** del conjunto | Moderada | 90 días | **Comprobación si opera en el sector** |
| cartera | **Ninguna víctima chilena** entre las 44 | Contrasta con la concentración de Qilin de `CTI-2026-015` | Alta como ausencia | 90 días | — |
| cartera | **Sanidad y servicios jurídicos dominan las víctimas comunes** | 7 de 16 del par insomnia/soul son sanidad | Moderada | 90 días | Análisis |

## Anexo B — Fuentes y valoración

| # | Fuente | Grado | Qué aportó | Salvedad |
|---|---|---|---|---|
| 1 | Endpoint de reclamaciones cruzadas de cti.fyi, 2026-11-19, cuatro páginas | **Medición propia** sobre datos de proveedor | Las 1.895 agrupaciones | **Su campo de separación horaria no se usa**: está mal en el 41 % (`CTI-2026-054` `O-2`) |
| 2 | Endpoint de entradas, ventana de 184 días | Medición propia sobre datos de proveedor | La actividad de cada grupo en el semestre, para `E-2` y `E-3` | Enriquecimiento derivado |
| 3 | `CTI-2026-047` | Propio | La hipótesis de marcas hermanas que `E-2` corrobora por segunda vía | — |
| 4 | `CTI-2026-053` | Propio | La pregunta abierta que `E-3` responde | Su `KJ-1` queda superado |
| 5 | `CTI-2026-045` `Anexo D` | Propio | El eje de la dirección: buscar el parámetro que no se alinea | — |
| 6 | `CTI-2026-014` y `CTI-2026-015` | Propio | Los dos actores de `O-4` | — |

## Anexo C — Léxico de probabilidad y confianza

ICD 203. **Casi con certeza** ≥99 % · **muy probable** 80–95 % · **probable** 55–80 % · **posible** 40–60 % · **improbable** 20–45 % · **muy improbable** 5–20 %. La **confianza** califica la base de prueba con independencia de la probabilidad. En este informe, las mediciones de solapamiento y dirección tienen confianza alta por ser reproducibles; las interpretaciones de `O-4` y `E-3.1` tienen confianza moderada por tamaño de muestra.

## Anexo D — Cómo clasificar una reclamación cruzada en veinte minutos

**Paso 1 — Comparar los recuentos totales (dos minutos).** Contar en cuántas víctimas contestadas participa cada uno de los dos grupos. **Si los dos números son casi iguales, sospechar alias de inmediato.** Es el paso más barato y resuelve los casos más abundantes.

**Paso 2 — Calcular el solapamiento (cinco minutos).** Víctimas comunes dividido por víctimas de la unión. Por encima del 85 % no son dos actores independientes: son el mismo expediente duplicado o una sucesión. Por debajo del 20 %, son distintos.

**Paso 3 — Medir la separación y su dispersión (cinco minutos).** Mediana, percentil 10 y percentil 90. **La dispersión importa tanto como la mediana:** una mediana de cero con percentiles de ±170 días no significa simultaneidad, significa dirección aleatoria.

**Paso 4 — Mirar la dirección (tres minutos).** Proporción de casos en que el mismo grupo va primero. Unanimidad significa sucesión. Reparto significa alias, o acceso compartido si el solapamiento es bajo.

**Paso 5 — Comprobar si el primer grupo sigue activo (cinco minutos).** Es lo único que separa sucesión de republicación, y la fuente lo da directamente.

> **El paso más discriminante es el cuarto**, y es el que casi nadie hace. El solapamiento dice si dos catálogos describen los mismos hechos; **la dirección dice si uno viene del otro**. Sin el cuarto eje, `insomnia`/`soul` es indistinguible de `hive`/`hiveleak`: ambos tienen solapamiento alto. Con él, uno es una sucesión de noventa y cuatro días y el otro un duplicado de cero.
>
> Y el paso que hay que hacer **antes** de los cinco: comprobar que el campo de separación que la fuente ofrezca calculado no esté mal. En este caso lo estaba, en el 41 % de los registros.

**Paso 6 — Añadido en v1.1: antes de concluir «colisión» o «acceso compartido» por un solapamiento bajo, comprobar si alguna de las dos marcas declara un programa de afiliados que publiquen con nombre propio.** Si lo declara, el caso es la quinta clase de `O-7` —una operación, dos marcas— y **la víctima sufrió un acceso, no dos**. La señal más barata está en el perfil del propio proveedor: las expresiones «marca blanca», «marca local» o «afiliados con su propia marca». Es el paso que separa un error de diagnóstico con consecuencias para la respuesta.

## Anexo E — Marcos de referencia empleados

ICD 203 para el lenguaje estimativo. Escala de Almirantazgo con los grados propios de la cartera. TLP 2.0 y PAP. Índice de Jaccard para el eje 1. El método de separación de campañas de `CTI-2026-045` `Anexo D`, del que este informe es la aplicación al caso simétrico: allí se trataba de decidir si una familia eran dos campañas, y aquí si dos expedientes son un actor. **El principio es el mismo —buscar el parámetro que no se alinea— y en este informe ese parámetro es la dirección.** Los cinco criterios para evaluar una afirmación de rebranding de `CTI-2026-047` `Anexo D`, que este método cuantifica: el solapamiento de catálogo es la medida de su criterio de herencia.

## Anexo F — Paquete legible por máquina

| Medición | Procedimiento |
|---|---|
| Conjunto base | `GET /api/v1/cross-claims?limit=500&offset=N`, N ∈ {0, 500, 1000, 1500} |
| Eje 1 | Jaccard sobre `victim_key` por grupo, en minúsculas |
| Eje 2 | Para cada víctima común, `min(discovered)` de B menos `min(discovered)` de A |
| Eje 3 | Proporción de diferencias negativas |
| Actividad en ventana | `GET /api/v1/posts?since=2026-05-19&limit=500&offset=N&sort=discovered` |
| Verificación del par insomnia/soul | Filtrar agrupaciones cuyos `groups` contengan ambos; 16 resultados |

**Advertencia de reproducción.** El campo `delta_hours` de la fuente **no** se usó. Quien reproduzca estas cifras con él obtendrá resultados distintos y equivocados.

## Anexo G — Control de cambios

| Versión | Fecha | Qué cambió | Qué juicio se movió |
|---|---|---|---|
| 1.0 | 2026-11-19 | Emisión inicial. El método de tres ejes, los once pares de alias, y las respuestas a las preguntas abiertas de `CTI-2026-047` y `CTI-2026-053` | — |
| 1.1 | 2026-11-19 | **Amplía el método de cuatro clases a cinco**, por el hallazgo de `CTI-2026-061`: un actor cuyo modelo de marca blanca permite a los afiliados publicar bajo nombre propio, verificado por una coaparición entre la matriz y un afiliado declarado. Incorpora `KJ-8`, `§O-7`, la quinta fila de la tabla de decisión, el **paso 6** del `Anexo D` y la brecha `G-6`. **Consigna el problema abierto de `O-7.1`:** la firma de la quinta clase es casi idéntica a la del acceso de origen común, y las separa una declaración de proveedor no corroborada; se propone un cuarto eje —coincidencia de plantilla de publicación— como salida por medición. **Ningún juicio de v1.0 se retira** | `KJ-5` se refuerza: más de las 44 se explica por mecanismos estructurales |

## Anexo H — Realimentación del consumidor

Este informe se corrige si se recibe: un caso de dos reclamaciones de la misma organización bajo nombres distintos que la fuente **no** haya agrupado, lo que confirmaría `H-4` y debilitaría `KJ-5`; la validación del método contra un rebranding establecido por fuente judicial, que cerraría `G-4`; una décima víctima común entre Qilin y TheGentlemen, que permitiría elevar `KJ-6`; o la confirmación de que las once entradas restantes de SoulGroup tienen otro origen, que cerraría `G-3`.

El disparador más inmediato es **`I-1`**, porque de él depende el juicio `KJ-5`, que es el más contraintuitivo de este informe y el que más probablemente se citará.
