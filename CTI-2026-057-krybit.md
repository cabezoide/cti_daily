---
tlp: "TLP:CLEAR"
pap: "PAP:WHITE"
id: "CTI-2026-057"
version: "1.0"
tipo: "Perfil de operación de extorsión"
foco_regional: "México · España · República Dominicana · Latinoamérica 14,9 %"
niveles: ["Estratégico", "Operacional", "Técnico"]
autor: "Célula CTI"
actor: "krybit · Krybit"
fecha: "2026-11-19"
caduca: "2026-12-19"
distribucion: "El actor con mayor proporción latinoamericana de los seis del lote y el único cuyas direcciones de infraestructura son cazables por patrón. No se reproduce ningún nombre de víctima: el catálogo de este actor está compuesto casi íntegramente por dominios de organización, y publicarlos equivaldría a amplificar la reclamación. Difusión libre conservando la atribución y las salvedades de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-057

## Ciento cincuenta y cuatro víctimas en cuarenta y seis países, y una de cada siete en Latinoamérica

### El actor del lote con el catálogo más verificable y el único que eligió direcciones de infraestructura legibles, lo que lo hace cazable por patrón

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-057` |
| Versión | 1.0 |
| Tipo | Perfil de operación de extorsión |
| Clasificación | `TLP:CLEAR` · `PAP:WHITE` |
| Fecha de emisión | 2026-11-19 |
| Caducidad | 2026-12-19 |
| Niveles | Estratégico · Operacional · Técnico |
| Actor | krybit · Krybit |
| Entradas en la ventana | 154 · **96 % con dominio · 100 % con captura** |
| Dispersión | **46 países** · 14,9 % Latinoamérica · **0 Chile** |
| Infraestructura | 6 sitios · **4 activos, los 4 con prefijo legible** |
| Autor | Célula CTI |

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** **Es el actor de este lote con mayor relevancia latinoamericana: veintitrés de sus ciento cincuenta y cuatro entradas (14,9 %) son de la región, siete veces la proporción del siguiente.** El reparto incluye **México con ocho**, República Dominicana, y el resto distribuido. Para comparar: `safepay` tiene el 6,7 %, `Booba Project` el 2,3 %, y `BrainCipher`, `Storm` y `dragonforce` cero o casi. Valoramos **casi con certeza** *(≥99 %)* el recuento sobre los campos de país de la fuente. **Confianza: moderada**, porque el país es un dato enriquecido y no observado, aunque aquí con cobertura del 83 %. *Consecuencia:* **de los seis actores de este lote, éste es el que una organización latinoamericana debe vigilar** (`E-2`).

**KJ-2.** **Y sin embargo no tiene ni una víctima chilena, lo que es informativo en sí.** Cero de 154, con 46 países representados y México, España, República Dominicana, Brasil y otros países de la región presentes. Valoramos **probable** *(55–80 %)* que la ausencia sea real y no un hueco de datos, dado el 83 % de cobertura de país. **Confianza: moderada.** *Consecuencia:* la prioridad chilena sigue siendo Qilin, que concentra veinte de las treinta víctimas chilenas medidas en `CTI-2026-015`; **este actor es prioridad regional pero no nacional** (`E-2.1`).

**KJ-3.** **Tiene el catálogo más verificable de los seis: el 96 % de sus entradas lleva dominio de la organización y el 100 % lleva captura de pantalla.** Ciento cuarenta y ocho de 154 con dominio, 154 de 154 con captura, 128 con país. Valoramos **casi con certeza** *(≥99 %)* los recuentos. **Confianza: alta.** *Consecuencia:* a diferencia de `CTI-2026-048`, donde el actor mejor situado en el ranking era el de prueba más débil, **aquí la reclamación es comprobable por la víctima en minutos**: el título de la entrada es su propio dominio (`O-2`).

**KJ-4.** **Su dispersión geográfica es extrema y eso dice algo sobre cómo obtiene el acceso: cuarenta y seis países para ciento cincuenta y cuatro víctimas, con India como primero y sólo catorce entradas.** Ninguna geografía supera el 9 % del catálogo. Valoramos **probable** *(55–80 %)* que el patrón sea incompatible con selección deliberada de objetivo y compatible con explotación oportunista de un conjunto de accesos obtenidos por barrido o comprados a granel. **Confianza: moderada.** *Consecuencia:* no hay un sector ni una región que defienda; **lo que hay es una superficie expuesta que este actor encuentra antes que su dueño** (`E-3`).

**KJ-5.** **Las cuatro direcciones activas de su infraestructura empiezan por `krybit` o `krybie`, y eso lo convierte en el único actor cazable por patrón del lote.** Un prefijo legible en una dirección de servicio oculto versión 3 **no se puede elegir: hay que calcularlo**, generando claves hasta que la dirección empiece por la cadena deseada. Es coste de cómputo deliberado. Valoramos **casi con certeza** *(≥99 %)* la observación. **Confianza: alta.** *Consecuencia, y es la aportación operativa del informe:* **la infraestructura futura de este actor se puede buscar por prefijo antes de que publique víctimas en ella** (`X-1`).

**KJ-6.** **Publica en tandas separadas por semanas, no de forma continua: catorce días de actividad en ciento setenta y cinco.** La mayor tanda son 45 entradas el 25 de julio; le siguen 32 el 6 de septiembre y 19 el 17 de agosto. El retraso mediano entre la fecha que declara y la de descubrimiento es de **11,1 días**. Valoramos **muy probable** *(80–95 %)* que el patrón refleje publicación por lotes de accesos acumulados. **Confianza: alta para la medición.** *Consecuencia:* **el intervalo entre el compromiso y la publicación es de semanas**, lo que da margen real a una organización que detecte la exfiltración (`O-3`).

**KJ-7.** **Y su perfil declarado incluye un dato que, si fuera cierto, sería el más valioso del expediente: que un competidor le reventó el panel interno.** La ficha del proveedor afirma que el operador rival `0APT` accedió a su infraestructura de gestión y la expuso a investigadores. No está corroborado y no se emite como hecho. Valoramos **posible** *(40–60 %)* que ocurriera. **Confianza: baja.** *Consecuencia:* si se confirmara, existiría material interno del actor en circulación, lo que **cambiaría por completo lo que se puede saber de él** y es la tarea de colección prioritaria (`G-1`).

---

## 2. Resumen ejecutivo

De los seis actores que la cartera incorpora en este lote, krybit es el que más importa a una organización latinoamericana y el que menos importa a una chilena.

Publicó **154 entradas** entre el 28 de mayo y el 19 de noviembre de 2026, repartidas en **cuarenta y seis países**. Veintitrés de esas entradas (**14,9 %**) corresponden a organizaciones latinoamericanas, con México a la cabeza con ocho. Es siete veces la proporción regional del siguiente actor del lote. Y a la vez **no tiene ni una víctima chilena**, con el 83 % de su catálogo etiquetado por país: la ausencia es significativa, no un hueco.

Su catálogo es el más verificable del lote, y por un motivo sencillo: **el título de casi todas sus entradas es el dominio de la organización**. Ciento cuarenta y ocho de 154 llevan dominio, las 154 llevan captura de pantalla. Eso contrasta de forma deliberada con el actor mejor situado del ranking que `CTI-2026-048` examinó, donde 59 de 259 entradas eran anónimas y ninguna tenía referencia de prensa. Aquí la reclamación se puede comprobar en minutos y el que la comprueba es el propio dueño del dominio.

La dispersión geográfica es el rasgo que más dice sobre su método. Cuarenta y seis países para ciento cincuenta y cuatro víctimas significa que **ninguna geografía llega al 9 % del catálogo**: India catorce, Estados Unidos diez, México ocho, Francia siete. No hay patrón de selección. Lo que hay es compatible con explotar un conjunto de accesos obtenidos a granel —por barrido de un servicio expuesto, o comprados— y publicarlos en lotes.

Y publica en lotes, literalmente: **catorce días de actividad en ciento setenta y cinco**, con una tanda de cuarenta y cinco entradas el 25 de julio. El retraso mediano entre la fecha que el propio sitio declara y la fecha en que el rastreador la ve es de **once días**, lo que sitúa el intervalo entre el compromiso y la publicación en el orden de semanas. Para una organización comprometida, eso es margen.

La aportación operativa del expediente, sin embargo, está en su infraestructura. Las cuatro direcciones activas de su sitio de filtración **empiezan por `krybit` o `krybie`**. Un prefijo legible en una dirección de servicio oculto no se elige: se calcula, generando claves hasta acertar. Es coste de cómputo invertido deliberadamente en que la dirección sea reconocible. Y tiene una consecuencia que el actor probablemente no valoró: **su infraestructura futura se puede buscar por prefijo**, lo que permite localizarla antes de que publique nada en ella. Ninguno de los otros cinco actores del lote es cazable así; `BrainCipher`, con cincuenta y cuatro direcciones, eligió explícitamente lo contrario.

Del perfil que la fuente publica sobre este actor —RaaS derivado de Babuk, reparto 80/20 con afiliados, cifrador multiplataforma para Windows, Linux, VMware ESXi y almacenamiento en red, extensión `.KRYBIT`, nota `RECOVER-README`— nada está corroborado, y así se marca. Contiene un dato que sería el más valioso del expediente si se confirmara: que un operador rival accedió a su panel de gestión y lo expuso. Esa es la tarea de colección prioritaria.

---

## 3. Alcance y limitaciones

### 3.1 Base de la medición

Las 154 entradas proceden de la consulta paginada de entradas con descubrimiento posterior al 19 de mayo de 2026 en la API de cti.fyi, el 19 de noviembre. La ficha de infraestructura procede del mismo origen. Ambas son reproducibles con `Anexo F`.

### 3.2 Límites

- **Los campos de país y sector son enriquecimiento derivado, no observación.** Cobertura del 83 % para país. `KJ-1` y `KJ-2` heredan ese límite y están calificados en consecuencia.
- **No se leyó el sitio de filtración.** Sin acceso a la red oscura en este entorno.
- **Ninguna víctima ha confirmado nada.**
- **El perfil del actor no está corroborado en ningún punto.** Véase `KJ-7` y `Anexo B`.
- **Una segunda fuente consultada el mismo día da cifras incompatibles y no se usa.** CTIWatch atribuye a este actor 183 víctimas en su cabecera y 78 en la prosa de la misma página, lo clasifica como motivado por espionaje —siendo un RaaS con reparto de ingresos— y declara su última actividad en abril de 2026, cuando hay entradas del 19 de noviembre. Los defectos están documentados en `CTI-2026-054` `§O-8.2`.

### 3.3 Higiene

**No se reproduce ningún nombre ni dominio de víctima.** Es una decisión con coste: el catálogo de este actor está formado casi íntegramente por dominios, lo que haría muy fácil ilustrar el informe con ejemplos. Publicarlos amplificaría la reclamación de un adversario sobre organizaciones que no han confirmado nada. Es la regla de la serie desde `CTI-2026-048`.

### 3.4 Veredicto por nivel

| Nivel | Veredicto | Motivo |
|---|---|---|
| Estratégico | **Utilizable** | Victimología con cobertura del 83 % |
| Operacional | **Utilizable** | Cadencia e infraestructura medidas |
| Táctico | **No evaluable** | Sin TTP observados; el perfil no basta |
| Técnico | **Parcial** | Infraestructura y patrón de caza sí; artefactos de ejecución no |

---

# NIVEL ESTRATÉGICO

## E-1. Cifras

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `154` | Entradas en la ventana | Sexto puesto del semestre |
| `46` | **Países distintos** | **Ninguno supera el 9 %** |
| `23` | **Entradas latinoamericanas (14,9 %)** | **Siete veces el siguiente del lote** |
| `0` | **Víctimas chilenas** | Con 83 % de cobertura de país (`KJ-2`) |
| `148 / 154` | Entradas con dominio (96 %) | **El catálogo más verificable del lote** |
| `154 / 154` | Entradas con captura | 100 % |
| `14` | **Días con actividad en 175** | Publica en tandas (`KJ-6`) |
| `45` | Mayor tanda, el 2026-07-25 | 29 % del catálogo en un día |
| `11,1 d` | Retraso mediano declarado→visto | **Semanas de margen** |
| `4 / 6` | Sitios activos, **todos con prefijo legible** | `KJ-5` |

## E-2. Relevancia regional: la más alta del lote

| Actor del lote | Entradas | Latinoamérica | Proporción |
|---|---|---|---|
| **krybit** | 154 | **23** | **14,9 %** |
| safepay | 134 | 9 | 6,7 % |
| dragonforce | 144 | 3 | 2,1 % |
| Booba Project | 129 | 3 | 2,3 % |
| Storm | 86 | 0 | 0 % |
| BrainCipher | 432 | 0 | 0 % (mal medido) |

Veintitrés entradas latinoamericanas con **México a la cabeza (ocho)**, y presencia de República Dominicana, Brasil y otros países de la región. España, que no es Latinoamérica pero sí hispanohablante y relevante para esta cartera, aparece con cinco.

**Lo que hace accionable este dato es que va unido a `KJ-3`.** Una organización mexicana que quiera saber si está en este catálogo no necesita interpretar nada: el título de la entrada es un dominio, y basta buscar el propio. Eso no es trivial —en el catálogo de `CTI-2026-048` sólo 22 de 259 entradas tenían dominio— y convierte la comprobación en una tarea de minutos.

### E-2.1 Y la ausencia chilena, que también informa

Cero de 154, con 46 países representados, con México, España, República Dominicana y Brasil presentes, y con el 83 % del catálogo etiquetado. **La ausencia no es un hueco de datos: es un dato.**

Para la cartera eso significa que la prioridad chilena no cambia. `CTI-2026-015` estableció que Qilin concentra **veinte de las treinta víctimas chilenas** medidas en el top diez de extorsión, y ninguno de los seis actores de este lote la desplaza. **Este actor es prioridad regional y no nacional**, y conviene decirlo con esas palabras para que una organización chilena no gaste esfuerzo donde no hay riesgo medido.

## E-3. Cuarenta y seis países: lo que la dispersión dice del método

| País | Entradas | Proporción |
|---|---|---|
| India | 14 | 9,1 % |
| Estados Unidos | 10 | 6,5 % |
| **México** | **8** | **5,2 %** |
| Francia | 7 | 4,5 % |
| Reino Unido | 6 | 3,9 % |
| Singapur · Tailandia | 5 cada uno | 3,2 % |
| **España** | **5** | 3,2 % |
| Otros 38 países | 94 | 61 % |

Ninguna geografía llega al 10 %. Y los sectores siguen el mismo patrón: Tecnología 19, Otros 18, Manufactura 16, Sanidad 14, Servicios profesionales 13 — ninguno por encima del 13 %.

**Un actor que selecciona objetivos produce concentración.** `safepay` concentra el 29 % de su catálogo en Alemania (`CTI-2026-058`); `Booba Project` concentra el 48 % en sanidad y administración pública (`CTI-2026-059`). Este actor no concentra nada, y eso es informativo: **lo que determina a sus víctimas no es una decisión sobre ellas**.

Las dos explicaciones compatibles con el patrón son el barrido de un servicio expuesto en Internet —que encuentra lo que haya, sin preferencia— y la compra de accesos a granel a un corredor que tampoco seleccionó. **No se pueden distinguir con estos datos**, y la distinción importa: en el primer caso existe una vulnerabilidad concreta que buscar, en el segundo no.

## E-4. Decisiones que este informe pide

1. **Para una organización latinoamericana, y en particular mexicana: comprobar el propio dominio en este catálogo.** Coste: minutos. Es la acción de mejor relación entre coste y valor de todo el lote, y es posible gracias a `KJ-3`.
2. **Añadir el patrón de prefijo de `X-1` a la vigilancia de infraestructura.** Permite localizar sitios nuevos de este actor antes de que publiquen víctimas.
3. **No reasignar prioridad chilena.** `KJ-2` es explícito y Qilin sigue siendo el actor relevante en Chile.
4. **Perseguir el dato de `KJ-7`.** Si el panel interno de este actor fue expuesto, existe material primario y el expediente cambiaría de naturaleza.

---

# NIVEL OPERACIONAL

## O-1. Identificación

| Campo | Valor | Procedencia |
|---|---|---|
| Nombre | krybit · Krybit | Prefijo de sus propias direcciones |
| Primera entrada observada | 2026-05-28 | Medición propia |
| Última entrada observada | 2026-11-19 | Medición propia, **el día de emisión** |
| Aparición declarada | Finales de marzo de 2026 | **Perfil de proveedor, no corroborado** |
| Linaje declarado | Derivado de Babuk | **Perfil de proveedor** |
| Modelo declarado | RaaS, reparto 80/20 con afiliados | **Perfil de proveedor** |
| Plataformas declaradas | Windows, Linux, VMware ESXi, almacenamiento en red | **Perfil de proveedor** |
| Extensión declarada | `.KRYBIT` | **Perfil de proveedor** |
| Nota declarada | `RECOVER-README` | **Perfil de proveedor** |
| Sitios | 6 registrados · **4 activos** | Medición propia |

**La columna de procedencia es el contenido principal de esta tabla.** Siete de las diez filas proceden de una ficha de proveedor sin referencias y con indicio de redacción automática. Se consignan porque son comprobables si aparece una muestra, y porque la extensión y el nombre de la nota son exactamente lo que una organización puede buscar en su propio sistema de archivos. **Pero no se afirman.**

## O-2. El catálogo, y por qué es el más verificable

| Medición | krybit | Comparación en la cartera |
|---|---|---|
| Entradas con dominio | **148 / 154 (96 %)** | n0n: 22 / 259 (8,5 %) |
| Entradas con captura | **154 / 154 (100 %)** | PixelLeaks: 0 / 34 |
| Entradas con país | 128 / 154 (83 %) | BrainCipher: 34 / 432 (8 %) |
| Entradas con sector | 128 / 154 (83 %) | — |
| Entradas con fecha declarada | 122 / 154 (79 %) | settra: 116 / 116 (100 %) |

Aplicando la **escala de prueba de ocho niveles** de `CTI-2026-048` `Anexo D`, este catálogo se sitúa de forma consistente en los niveles medios: tiene nombre identificable y verificable por el afectado (dominio), tiene captura de pantalla —nivel 3, el que según aquel informe **engaña más**—, y carece de muestra de ficheros y de referencia de prensa.

**La combinación de dominio y captura es lo que lo hace útil.** Una captura sin nombre no se puede comprobar; un nombre sin captura no demuestra acceso. Las dos juntas permiten a la víctima decidir en minutos si la reclamación la señala a ella, aunque no si es cierta.

## O-3. Cadencia: catorce días en ciento setenta y cinco

| Fecha | Entradas |
|---|---|
| 2026-05-28 | 13 |
| 2026-05-30 | 1 |
| **2026-07-25** | **45** |
| 2026-08-17 | 19 |
| **2026-09-06** | **32** |
| 2026-09-12 | 12 |
| 2026-09-13 | 1 |
| 2026-10-23 | 13 |
| 2026-10-27 | 6 |
| 2026-11-09 | 6 |
| 2026-11-10 · 11-15 · 11-18 | 1 cada uno |
| 2026-11-19 | 3 |

El patrón es de **tandas con huecos de semanas**: entre el 30 de mayo y el 25 de julio no publica nada, y entre el 13 de septiembre y el 23 de octubre tampoco.

Y el retraso entre la fecha que el propio sitio declara y la fecha de descubrimiento tiene mediana de **11,1 días**. Las dos cosas juntas sostienen `KJ-6`: el actor **acumula accesos y los publica por lotes**, con un intervalo del orden de semanas entre el compromiso y la aparición pública.

> **Para una organización comprometida eso es margen, y es el dato operativo más útil del expediente.** Entre la exfiltración y la publicación hay semanas. Una detección de exfiltración masiva en ese intervalo no llega tarde: llega **antes** de que la reclamación sea pública, que es el único momento en que algunas decisiones siguen siendo posibles.

La actividad del último mes es notablemente más fina —una a seis entradas por día— y continúa el día de emisión. Eso puede indicar cambio de modo o simplemente que la tanda siguiente no ha llegado. **No se interpreta.**

## O-4. Clasificación

Triaje de `CTI-2026-042` `Anexo D`: cumple **cinco criterios de siete**. Tiene sitio de filtración con víctimas nombradas y verificables, tiene infraestructura propia con cuatro sitios activos, tiene continuidad temporal de casi seis meses medidos, tiene linaje declarado —aunque no corroborado— y tiene un modelo de negocio declarado con reparto de afiliados. Falla en análisis primario con muestra y en víctima confirmada por tercero.

**Clase: marca con operación.** Es la clasificación más alta de los seis actores del lote.

## O-5. Hipótesis y pre-mortem

**H-1.** *El acceso se obtiene por barrido de un servicio expuesto, no por selección.* **Probable** *(55–80 %)*. Apoyo: 46 países, ningún sector por encima del 13 %, publicación por lotes. En contra: no hay ni un vector observado.

**H-2.** *La ausencia de víctimas chilenas es real.* **Probable** *(55–80 %)*. Apoyo: 83 % de cobertura de país y presencia de otros países de la región. En contra: 26 entradas sin país podrían incluir alguna.

**H-3.** *El reparto 80/20 con afiliados es cierto.* **Posible** *(40–60 %)*. Sin corroborar. Si lo fuera, la dispersión de `E-3` tendría una segunda explicación: **varios afiliados actuando en paralelo, cada uno sobre su propio conjunto de accesos.** Esta hipótesis es compatible con `H-1` y no la excluye.

**H-4.** *El panel interno fue expuesto por un competidor.* **Posible** *(40–60 %)*. Es `KJ-7`.

### Pre-mortem

*Si este informe se equivoca, será en `KJ-1`.* La proporción latinoamericana del 14,9 % se apoya en un campo de país que es inferencia de un enriquecedor automático, no observación. `CTI-2026-054` `§O-5` midió que ese enriquecedor **nunca se abstiene**, y `CTI-2026-056` `§E-2` documentó que inventa víctimas cuando no tiene datos. Aquí la cobertura es alta (83 %) y los títulos son dominios —lo que hace la inferencia de país mucho más fiable, porque un dominio de nivel superior nacional la determina—, pero **no se verificó ninguna de las veintitrés entradas regionales contra la organización**. Es `I-2`.

*El segundo modo de fallo es `KJ-5`.* Si el actor cambia de práctica y genera direcciones aleatorias, el patrón de caza de `X-1` deja de servir **sin aviso**, y una vigilancia que dependa de él daría falsa tranquilidad. Se consigna en la caducidad del indicador.

---

# NIVEL TÉCNICO

## X-1. El prefijo legible como indicador de caza

Las cuatro direcciones activas:

```
krybitxdpxohsmjooeb3gbgpmdddreh6mnflzac6bnezz74b7yje67yd.onion
krybitx3fh5krdnhegyp2ob3lhizsaiadturtio3ginf7it5gsdgu2yd.onion
krybitqsdzwmhnitvwuhvsntfgf2wrhxveyxroxpc44c6gkft2cqldyd.onion
krybieodq754vlwufrsuxaswxb5zpxyibaawmed2jaduoz2e5m56hmid.onion
```

Tres empiezan por `krybit` y una por `krybie`.

### X-1.1 Por qué esto es un indicador y no una curiosidad

Una dirección de servicio oculto versión 3 es la codificación de una clave pública Ed25519. **No se puede elegir el texto**: se generan pares de claves hasta que la codificación empiece por la cadena deseada. El coste crece exponencialmente con la longitud del prefijo, y seis caracteres significativos es un objetivo que requiere trabajo deliberado pero perfectamente alcanzable con herramientas públicas.

De ahí se siguen tres cosas:

1. **El actor invirtió cómputo en ser reconocible.** Eso tiene sentido en un negocio donde la víctima debe encontrar el sitio correcto y donde la suplantación por terceros —un sitio falso que recoja los pagos— es un riesgo real.
2. **La cuarta dirección, con `krybie`, probablemente es un error o un compromiso de coste.** Cambiar la sexta letra reduce mucho el trabajo de generación. Es una señal menor de que la generación se hizo con prisa.
3. **Y lo que el actor paga por ello: es cazable.** Cualquier dirección nueva que empiece por `krybit` o `krybie` es candidata a infraestructura suya **antes de que publique una sola víctima**.

### X-1.2 El contraste, que confirma que es una decisión

`BrainCipher` tiene **cincuenta y cuatro direcciones registradas y ninguna con prefijo legible** (`CTI-2026-056` `§O-3.2`). `dragonforce` tiene veinte, de las que tres sí llevan prefijo `dragonfor`/`dragongo` y diecisiete no (`CTI-2026-061`). Son decisiones distintas sobre el mismo problema, y el hecho de que coexistan demuestra que **no es una propiedad de la tecnología sino una elección del operador**.

## X-2. Lo que el perfil declara y no se puede usar como detección

| Elemento declarado | Por qué no genera detección |
|---|---|
| Extensión `.KRYBIT` | **Sí es comprobable por la víctima** en su propio sistema de ficheros. **No es detección**: aparece después del cifrado |
| Nota `RECOVER-README` | Igual: comprobable, no preventivo |
| Cifrador para Windows, Linux, VMware ESXi y NAS | Sin muestra, sin hash, sin firma. **No hay nada que detectar** |
| Exfiltración de 10 a 250 GB antes del cifrado | **Es lo único con valor preventivo**, y es genérico: una salida de datos de ese volumen es anómala para casi cualquier organización, con independencia del actor |

**El único control que este expediente justifica recomendar es el último, y no es específico de este actor.** Una alerta por volumen de salida en el rango de decenas a centenares de gigabytes, correlacionada con horario y destino, es la contramedida que el perfil declarado sugiere — y la que además encaja con `O-3`: si el intervalo entre exfiltración y publicación es de semanas, **la detección en ese punto llega a tiempo**.

---

## 14. Brechas de inteligencia y requisitos de colección

**G-1. El supuesto compromiso del panel interno por un rival no está corroborado.** Es la brecha de mayor valor potencial: material primario del actor.
→ **I-1.** Buscar publicaciones de investigadores que citen datos internos de este actor o del rival nombrado. **Disparador:** cualquier análisis que mencione el panel.

**G-2. Ninguna de las veintitrés entradas latinoamericanas está verificada contra la organización**, y el país es enriquecimiento derivado.
→ **I-2.** Verificar los dominios de las ocho entradas mexicanas: existencia, titularidad y, si es posible, confirmación. **Disparador:** inmediato; sostiene `KJ-1`, el juicio principal.

**G-3. No hay ni un vector de acceso observado**, lo que impide distinguir entre barrido y compra a granel (`H-1` frente a `H-3`).
→ **I-3.** Informe de incidente de cualquier víctima, o coincidencia de un producto expuesto en varias.

**G-4. No hay muestra ni hash**, de modo que el nivel táctico queda vacío.
→ **I-4.** Buscar muestra en repositorios públicos por la extensión declarada. **Disparador:** antes de emitir nivel táctico.

**G-5. No sabemos si el prefijo legible seguirá usándose.** De ello depende `X-1`.
→ **I-5.** Vigilancia del patrón, y reevaluación si aparece un sitio suyo sin prefijo.

**G-6. Las cifras de una segunda fuente son incompatibles** (183 / 78) y no se pudo reconciliar.
→ **I-6.** Contrastar entrada por entrada contra el otro rastreador de la cartera.

---

# ANEXOS

## Anexo A — Indicadores

### A.1 — Infraestructura

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| domain | `krybitqsdzwmhnitvwuhvsntfgf2wrhxveyxroxpc44c6gkft2cqldyd.onion` | **Activo.** Sirvió 90 de las 154 entradas | Alta | 90 días | Vigilancia |
| domain | `krybitx3fh5krdnhegyp2ob3lhizsaiadturtio3ginf7it5gsdgu2yd.onion` | Activo. Sirvió 27 entradas | Alta | 90 días | Vigilancia |
| domain | `krybitxdpxohsmjooeb3gbgpmdddreh6mnflzac6bnezz74b7yje67yd.onion` | Activo. Sirvió 24 entradas | Alta | 90 días | Vigilancia |
| domain | `krybieodq754vlwufrsuxaswxb5zpxyibaawmed2jaduoz2e5m56hmid.onion` | Activo. Sirvió 13 entradas. **Prefijo `krybie`, no `krybit`** | Alta | 90 días | Vigilancia |
| pattern | **Dirección de servicio oculto v3 con prefijo `krybit` o `krybie`** | **El indicador de caza del informe** (`X-1`). Un prefijo legible exige cómputo deliberado y hace al actor localizable **antes** de que publique víctimas | **Alta como método** | **Hasta que aparezca un sitio suyo sin prefijo** (`I-5`) | **Búsqueda proactiva de infraestructura** |

### A.2 — Comprobables por la víctima

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| pattern | **Extensión de fichero `.KRYBIT`** | Declarada por el proveedor, **no corroborada**. Comprobable en el propio sistema de ficheros. **Posterior al cifrado: no es detección** | **Baja** (declaración de proveedor) | Hasta corroboración | **Comprobación por la víctima** |
| filename | `RECOVER-README` | Nota de rescate declarada. Misma salvedad | **Baja** | Hasta corroboración | Comprobación por la víctima |
| pattern | **Entrada de sitio de filtración cuyo título es el dominio de la organización** | 148 de 154 (96 %). **El patrón que hace este catálogo comprobable en minutos** (`KJ-3`) | Alta | 90 días | **Comprobación por la víctima** |
| pattern | **Salida de datos de 10 a 250 GB previa al cifrado** | Declarada por el proveedor. **El único control con valor preventivo del expediente**, y es genérico (`X-2`) | Moderada como control | Sin caducidad | **Alerta, con independencia de este actor** |

### A.3 — Victimología

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| cartera | **154 entradas · 96 % con dominio · 100 % con captura · 83 % con país** | **El perfil probatorio más fuerte del lote** (`O-2`) | Alta como recuento | 90 días | Medición |
| cartera | **23 entradas latinoamericanas (14,9 %), México 8** | **El dato regional más accionable del lote** (`KJ-1`) | **Moderada**: país derivado | 90 días | **Comprobación si opera en la región** |
| cartera | **0 víctimas chilenas de 154** | Con 83 % de cobertura. **La ausencia es dato** (`KJ-2`) | Moderada | 90 días | **No reasignar prioridad chilena** |
| cartera | **46 países, ninguno por encima del 9,1 %** | Dispersión incompatible con selección de objetivo (`E-3`) | Alta como recuento | 90 días | Análisis |
| cartera | **14 días de actividad en 175 · mayor tanda 45 entradas** | Publicación por lotes (`O-3`) | Alta | 90 días | Análisis |
| cartera | **Retraso mediano declarado→visto de 11,1 días** | **Semanas de margen entre compromiso y publicación** | Alta | 90 días | **Dimensionar la ventana de detección** |
| artefacto | **Una segunda fuente da 183 y 78 víctimas en la misma página** | `§3.2`. **No se usa ninguna de las dos** | Alta como observación | — | — |

## Anexo B — Fuentes y valoración

| # | Fuente | Grado | Qué aportó | Salvedad |
|---|---|---|---|---|
| 1 | API de cti.fyi, entradas y ficha de grupo, 2026-11-19 | **Medición propia** sobre datos de proveedor | Las 154 entradas, los 6 sitios, toda la victimología y la cadencia | Evaluada en `CTI-2026-054`, con ocho defectos. Los campos de país y sector son **enriquecimiento derivado** |
| 2 | Ficha de perfil del grupo, misma fuente | **Proveedor, con indicio de redacción sintética** | El linaje Babuk, el reparto 80/20, las plataformas, la extensión, la nota, y el supuesto compromiso del panel de `KJ-7` | **No corroborada en ningún punto.** Siete de las diez filas de `O-1` proceden de aquí y así se marcan |
| 3 | CTIWatch, ficha pública del actor, 2026-11-19 | Proveedor, **prosa generada automáticamente** | **Nada utilizable.** Se consigna como contraste negativo en `§3.2` | **183 frente a 78 víctimas en la misma página**, motivación clasificada como espionaje, última actividad en abril con entradas en noviembre |
| 4 | `CTI-2026-015` | Propio | La comparación chilena de `KJ-2`: 20 de 30 víctimas chilenas son de Qilin | — |
| 5 | `CTI-2026-048` Anexo D | Propio | La escala de prueba de ocho niveles aplicada en `O-2` | — |
| 6 | `CTI-2026-042` Anexo D | Propio | El triaje de `O-4` | — |

## Anexo C — Léxico de probabilidad y confianza

ICD 203. **Casi con certeza** ≥99 % · **muy probable** 80–95 % · **probable** 55–80 % · **posible** 40–60 % · **improbable** 20–45 % · **muy improbable** 5–20 %. La **confianza** califica la base de prueba con independencia de la probabilidad. En este informe los recuentos llevan confianza alta; **todo juicio que dependa del campo de país lleva confianza moderada** por ser enriquecimiento derivado; los elementos del perfil del proveedor llevan confianza baja.

## Anexo D — Cuándo un prefijo legible es un indicador aprovechable

Procedimiento para decidir si la infraestructura de un actor es cazable por patrón. Coste: cinco minutos.

**Paso 1 — Listar las direcciones conocidas y mirar los primeros caracteres.** Si dos o más comparten un prefijo de cuatro o más caracteres que además es pronunciable o relacionado con el nombre del actor, hay candidato.

**Paso 2 — Descartar la coincidencia.** Una dirección v3 tiene 56 caracteres de un alfabeto de 32. Que dos direcciones compartan seis caracteres iniciales por azar es, en la práctica, imposible. **Un prefijo compartido no es casualidad: es generación dirigida.**

**Paso 3 — Medir la longitud útil del prefijo.** Cuanto más largo, más específico el patrón y menos falsos positivos — pero también más fácil de abandonar por el actor. **Entre cinco y siete caracteres es el intervalo aprovechable.** Aquí seis, con una variante de cinco.

**Paso 4 — Comprobar si el actor lo usa en toda su infraestructura o sólo en la cara pública.** Si el portal de negociación o el almacenamiento no llevan prefijo, el patrón sólo encuentra el sitio de filtración. **Es la limitación más frecuente**, y aquí los cuatro activos lo llevan.

**Paso 5 — Fijar la condición de caducidad explícita.** Un patrón de prefijo deja de funcionar **sin aviso** en cuanto el actor cambia de práctica, y una vigilancia que dependa de él dará falsa tranquilidad. La caducidad no es una fecha: es **la aparición del primer sitio sin prefijo**.

> **El paso que más se olvida es el quinto, y es el que distingue un indicador de una trampa.** Los otros cuatro dicen si el patrón funciona hoy; el quinto dice cómo sabrás que ha dejado de funcionar. Sin él, la ausencia de resultados se lee como ausencia de actividad — que es el mismo error que la trampa del valor por omisión de `CTI-2026-044` `§O-2.2`, cometido con otra herramienta.

## Anexo E — Marcos de referencia empleados

ICD 203. Escala de Almirantazgo con los grados propios de la cartera. TLP 2.0 y PAP. Triaje de actor nuevo de `CTI-2026-042` `Anexo D`. Escala de prueba de ocho niveles de `CTI-2026-048` `Anexo D`. Especificación de servicios ocultos versión 3 de Tor para `X-1`. **No se emite mapa ATT&CK**: no hay ni una técnica observada, y la ficha del proveedor no es base suficiente, por el mismo criterio de `CTI-2026-048`.

## Anexo F — Paquete legible por máquina

| Medición | Procedimiento |
|---|---|
| Entradas | `GET /api/v1/posts?group=krybit&since=2026-05-19&limit=500` |
| Infraestructura | `GET /api/v1/groups/krybit` → `locations[]` |
| Victimología | Agrupar `enriched_metadata.country_iso` y `.industry_sector` |
| Latinoamérica | Suma sobre el conjunto de 23 códigos ISO de la región |
| Cadencia | Agrupar `discovered[:10]` |
| Retraso | Mediana de `discovered − published` sobre las 122 entradas con ambas fechas |

## Anexo G — Control de cambios

| Versión | Fecha | Qué cambió | Qué juicio se movió |
|---|---|---|---|
| 1.0 | 2026-11-19 | Emisión inicial. Incluye la proporción latinoamericana más alta del lote (`KJ-1`), la ausencia chilena como dato (`KJ-2`), el patrón de caza por prefijo (`KJ-5`, `X-1`) y el método del `Anexo D` | — |

## Anexo H — Realimentación del consumidor

Este informe se corrige si se recibe: verificación de cualquiera de las ocho entradas mexicanas contra la organización, que elevaría `KJ-1` a confianza alta (`I-2`); una víctima chilena en su catálogo, que invalidaría `KJ-2`; una muestra con la extensión declarada, que permitiría emitir niveles táctico y técnico (`I-4`); material procedente del supuesto compromiso del panel interno, que cambiaría la naturaleza del expediente (`I-1`); o un sitio suyo sin prefijo legible, que caducaría el indicador de `X-1` (`I-5`).

El disparador más urgente es **`I-2`**, porque `KJ-1` es el juicio principal, es el que una organización de la región usará para decidir, y descansa sobre un campo que es inferencia automática.
