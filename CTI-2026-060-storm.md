---
tlp: "TLP:CLEAR"
pap: "PAP:WHITE"
id: "CTI-2026-060"
version: "1.0"
tipo: "Perfil de operación de extorsión"
foco_regional: "Estados Unidos 50 % · sin relevancia latinoamericana"
niveles: ["Estratégico", "Operacional"]
autor: "Célula CTI"
actor: "Storm"
fecha: "2026-11-19"
caduca: "2026-12-19"
distribucion: "El actor cuyo propio perfil de proveedor declara que infla el recuento de víctimas, y cuyo catálogo lo confirma: un grupo bancario estadounidense aparece tres veces, como matriz y dos filiales. No se reproduce ningún nombre de víctima; el procedimiento del Anexo F permite reproducir el hallazgo. Difusión libre conservando la atribución y las salvedades de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-060

## Setenta y tres de sus ochenta y seis víctimas aparecieron el primer día, con fechas de un mes antes

### Y un grupo bancario figura tres veces —matriz y dos filiales— en el catálogo de un actor cuyo propio perfil de proveedor declara que infla recuentos

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-060` |
| Versión | 1.0 |
| Tipo | Perfil de operación de extorsión |
| Clasificación | `TLP:CLEAR` · `PAP:WHITE` |
| Fecha de emisión | 2026-11-19 |
| Caducidad | 2026-12-19 |
| Niveles | Estratégico · Operacional |
| Actor | Storm |
| Entradas en la ventana | 86 · **73 el primer día (85 %)** |
| Clasificación de novedad | **Dudoso** — retraso mediano 27,8 d |
| Inflación medida | **3 entradas = 1 grupo bancario** |
| Infraestructura | **1 sitio, activo** |
| Autor | Célula CTI |

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** **Setenta y tres de sus ochenta y seis entradas aparecieron el 30 de septiembre de 2026, su primer día, y declaran fechas de publicación de casi un mes antes.** El retraso mediano entre la fecha que el propio sitio declara y la fecha en que fue descubierto es de **27,8 días**. Valoramos **casi con certeza** *(≥99 %)* las mediciones. **Confianza: alta.** *Consecuencia:* el sitio de filtración es nuevo pero **el catálogo no lo es**; este actor no arrancó el 30 de septiembre, ese fue el día en que abrió escaparate con material acumulado. Por el método de `CTI-2026-054` queda clasificado como **dudoso**: no es un sitio preexistente incorporado por el rastreador, pero tampoco una operación que empezara entonces (`E-1`).

**KJ-2.** **Y el hallazgo propio del expediente: un grupo bancario estadounidense figura tres veces en el catálogo —como matriz y como dos filiales— con dos dominios distintos.** Las tres entradas tienen títulos diferentes y el enriquecedor las resolvió como tres organizaciones separadas. Valoramos **muy probable** *(80–95 %)* que correspondan a un único compromiso. **Confianza: alta para la observación, moderada para la unicidad del compromiso**, porque un grupo bancario puede tener sistemas segregados por filial. *Consecuencia:* **el recuento de 86 es un techo, no una medida**, y basta un caso como éste para que cualquier comparación de volumen con otros actores pierda precisión (`E-2`).

**KJ-3.** **Lo notable es que el propio perfil del proveedor lo anticipa: declara que el actor emplea «tácticas de inflación de víctimas».** Es la primera vez en esta cartera que una ficha de proveedor no corroborada **predice un comportamiento que después se confirma en los datos propios**. Valoramos **casi con certeza** *(≥99 %)* que la afirmación figura en la ficha, y **probable** *(55–80 %)* que la inflación medida en `KJ-2` sea una instancia de lo que describe. **Confianza: moderada.** *Consecuencia:* eleva marginalmente la credibilidad del resto de ese perfil —no a «cierto», sino de «sin apoyo» a «con un acierto comprobado»—, y es la única vez en los seis expedientes del lote en que algo así ocurre (`O-5`).

**KJ-4.** **Toda su infraestructura es un único sitio, y está activo.** Una sola dirección de servicio oculto, titulada «Storm Blog», que sirvió las 86 entradas y responde al 19 de noviembre de 2026. Es la infraestructura más simple de los seis actores del lote: `BrainCipher` tiene cincuenta y cuatro direcciones y `dragonforce` veinte. Valoramos **casi con certeza** *(≥99 %)* la observación. **Confianza: alta.** *Consecuencia:* **no hay portal de negociación observable**, lo que deja sin responder el criterio más discriminante del triaje de `CTI-2026-042` —cómo contacta la víctima— y limita la clasificación (`O-3`).

**KJ-5.** **Después del volcado inicial casi se detuvo: trece entradas en los cuarenta y tres días siguientes, y nada desde el 12 de noviembre.** El reparto posterior al primer día es de tres, una, una, una, dos, tres y dos entradas en siete días dispersos. Valoramos **casi con certeza** *(≥99 %)* la medición. **Confianza: alta.** *Consecuencia:* el patrón —volcado grande y goteo mínimo— es compatible con una operación cuyo catálogo era **el trabajo acumulado antes de abrir el sitio** y cuya capacidad de generar víctimas nuevas es muy inferior a lo que su cifra total sugiere (`O-4`).

**KJ-6.** **No tiene relevancia regional: cero entradas latinoamericanas de 86, y sólo siete países.** Estados Unidos concentra 43 (50 %), con Alemania, Canadá, Reino Unido, Australia, India y Rumanía completando el resto. Valoramos **probable** *(55–80 %)* que la ausencia sea real, con 66 % de cobertura de país. **Confianza: moderada.** *Consecuencia:* **para la cartera es vigilancia de línea base y nada más** (`E-3`).

**KJ-7.** **El perfil declara una antigüedad de 2021 que ningún dato propio apoya, y es la contradicción central del expediente.** Si el actor opera desde 2021, un catálogo visible de 86 entradas que empieza en septiembre de 2026 es incompatible con cinco años de actividad — a menos que el sitio de filtración sea una reapertura, lo que el perfil no afirma. Valoramos **improbable** *(20–45 %)* que la antigüedad declarada se refiera a la misma operación que publica en este sitio. **Confianza: baja.** *Consecuencia:* **o el nombre designa dos cosas distintas, o la ficha mezcla expedientes** — y la cartera ya ha visto las dos cosas en este mismo lote (`O-5.1`).

---

## 2. Resumen ejecutivo

Storm publicó **86 entradas** y setenta y tres de ellas, el **85 %**, aparecieron el 30 de septiembre de 2026, su primer día de existencia observable. Las fechas que esas entradas declaran son de casi un mes antes: el retraso mediano entre la fecha del sitio y la del descubrimiento es de **27,8 días**.

Eso coloca al actor en una categoría intermedia que el método de `CTI-2026-054` identifica y la mayoría de los recuentos no: **el sitio de filtración es nuevo, pero el catálogo no lo es**. No es un sitio preexistente que el rastreador empezara a mirar —esos tienen retrasos de cientos de días—, pero tampoco una operación que empezara el 30 de septiembre. Es un actor que **abrió escaparate con material acumulado**.

El hallazgo propio del expediente es otro, y es el que más dice. **Un grupo bancario estadounidense figura tres veces en el catálogo**: una entrada para la matriz y dos para sendas filiales, con dos dominios distintos. El enriquecedor de la fuente las resolvió como tres organizaciones separadas, y el actor las publicó como tres víctimas. Con casi total seguridad corresponden a un único compromiso.

Lo llamativo es que el perfil que el proveedor publica sobre este actor **lo anticipa**: declara expresamente que emplea «tácticas de inflación de víctimas». Es la primera vez en los cuarenta informes de esta cartera que una ficha de proveedor no corroborada predice un comportamiento que luego se confirma en los datos propios. No convierte el resto de esa ficha en cierto, pero la mueve de «sin ningún apoyo» a «con un acierto comprobable», y eso merece consignarse.

Después del volcado inicial, el actor casi se detuvo: **trece entradas en los cuarenta y tres días siguientes**, repartidas en siete días dispersos, y nada desde el 12 de noviembre. El patrón —un volcado grande seguido de goteo— es el de una operación cuyo catálogo era el trabajo previo y cuya capacidad de generar víctimas nuevas es muy inferior a lo que su cifra total sugiere.

Su infraestructura es la más simple del lote: **un único sitio**, titulado «Storm Blog», activo. Frente a las cincuenta y cuatro direcciones de `BrainCipher` o las veinte de `dragonforce`. Y eso tiene una consecuencia para la clasificación: **no hay portal de negociación observable**, de modo que el criterio más discriminante del triaje de la cartera —cómo contacta la víctima— queda sin responder.

No tiene relevancia regional alguna: cero entradas latinoamericanas, siete países, la mitad del catálogo en Estados Unidos.

Y queda una contradicción sin resolver. El perfil declara que el actor opera **desde 2021**, lo que no encaja con un catálogo visible que empieza en septiembre de 2026. O el nombre designa dos cosas distintas, o la ficha mezcla expedientes — y la cartera ha encontrado ambos errores en este mismo lote.

---

## 3. Alcance y limitaciones

### 3.1 Base de la medición

Las 86 entradas y el sitio único proceden de la API de cti.fyi consultada el 19 de noviembre de 2026. La detección de la inflación de `KJ-2` se hizo por comparación de similitud textual entre los 86 títulos y verificación de los dominios asociados. Reproducible con `Anexo F`.

### 3.2 Límites

- **El país y el sector son enriquecimiento derivado**, con 66 % de cobertura de país — la segunda más baja del lote tras `BrainCipher`.
- **Sólo el 45 % de las entradas lleva dominio** (39 de 86), la proporción más baja del lote entre los actores con catálogo legible. Eso limita la verificabilidad por la víctima y es lo que hace que `KJ-2` requiriera comparación textual en lugar de comparación de dominios.
- **No se leyó el sitio de filtración.** Sin acceso a Tor en este entorno.
- **Ninguna víctima ha confirmado nada.**
- **El perfil del actor no está corroborado**, con la excepción parcial de `KJ-3`.
- **Una segunda fuente da 89 víctimas** sin más detalle utilizable (CTIWatch), cifra compatible con las 86 medidas pero procedente de una ficha cuyos defectos están documentados en `CTI-2026-054` `§O-8.2`.

### 3.3 Higiene

No se reproduce ningún nombre de víctima, incluidos los tres del grupo bancario de `KJ-2`. Es una renuncia con coste: el hallazgo sería más convincente con los nombres a la vista. Se describe la estructura —matriz y dos filiales, dos dominios— y el `Anexo F` da el procedimiento para que cualquiera con acceso a la fuente lo reproduzca. La regla es la de `CTI-2026-048`: no amplificar reclamaciones nominales que ninguna víctima ha confirmado.

### 3.4 Veredicto por nivel

| Nivel | Veredicto | Motivo |
|---|---|---|
| Estratégico | **Utilizable con la salvedad del recuento** | `KJ-2` hace de 86 un techo |
| Operacional | **Parcial** | Cadencia sí; canal de contacto no observado |
| Táctico | **No evaluable** | Sin TTP observados |
| Técnico | **No se emite** | Sin indicadores de ejecución |

---

# NIVEL ESTRATÉGICO

## E-1. El volcado del primer día

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `86` | Entradas en la ventana | **Techo, no medida** (`KJ-2`) |
| `73` | **Entradas el 2026-09-30, su primer día** | **85 % del catálogo** |
| `27,8 d` | **Retraso mediano declarado→visto** | Clasificación: **dudoso** |
| `13` | Entradas en los 43 días siguientes | Repartidas en 7 días |
| `0` | Entradas desde el 2026-11-12 | 7 días de silencio al cierre |
| `86 / 86` | Entradas con fecha declarada | **100 %, único del lote con krybit** |
| `39 / 86` | Entradas con dominio (45 %) | **La más baja del lote con catálogo legible** |
| `43 / 86` | Entradas estadounidenses (50 %) | **Sólo 7 países** |
| `0` | Entradas latinoamericanas | `KJ-6` |
| `3` | **Entradas que son un solo grupo bancario** | `KJ-2` |
| `1` | Sitio de infraestructura, **activo** | La más simple del lote |

| Fecha | Entradas |
|---|---|
| **2026-09-30** | **73** |
| 2026-10-02 | 3 |
| 2026-10-04 · 10-06 · 10-07 | 1 cada uno |
| 2026-10-12 | 2 |
| 2026-10-19 | 3 |
| 2026-11-12 | 2 |

### E-1.1 Por qué «dudoso» y no «nuevo»

El método del correctivo 1 de `CTI-2026-054` `Anexo D` clasifica a un grupo que se estrena en la ventana según el retraso mediano entre la fecha que sus entradas declaran y la fecha en que fueron descubiertas:

| Retraso mediano | Clase | Lectura |
|---|---|---|
| ≤ 3 días | Nuevo contemporáneo | Apareció mientras la fuente ya vigilaba |
| 3 a 30 días | **Dudoso** | **Este actor: 27,8 días** |
| > 30 días | Preexistente incorporado | La fuente empezó a mirar un sitio que ya existía |

Veintisiete días no son ni una cosa ni la otra, y la lectura correcta es específica: **el sitio es nuevo y el contenido tiene un mes**. Un rastreador que descubre un sitio recién publicado ve entradas de horas; uno que incorpora un sitio antiguo ve entradas de meses o años. Aquí las entradas tienen semanas, lo que encaja con **un actor que trabajó durante septiembre y publicó todo a la vez el día 30**.

Y el 100 % de cobertura de fecha declarada —86 de 86, compartido en el lote sólo con la práctica de `krybit`— es lo que hace esta medición posible. Sin ese campo, el 85 % de entradas en un día se habría leído como actividad frenética en lugar de como volcado.

## E-2. La inflación del recuento

Entre los 86 títulos, tres corresponden a **un mismo grupo bancario estadounidense**: uno nombra al grupo, otro a un banco con la denominación «and Trust», y el tercero a un banco con la denominación «Community». Los dos últimos llevan dominios distintos; el primero no lleva dominio.

**Qué apoya que sean un solo compromiso:**

- Los tres nombres comparten los dos primeros términos de la razón social.
- Los dos dominios corresponden al mismo grupo bancario, con marcas distintas para líneas de negocio diferentes.
- Las tres entradas aparecieron **el mismo día**, el 30 de septiembre, dentro del volcado inicial.
- El enriquecedor de la fuente las resolvió como tres organizaciones separadas y asignó sector financiero a las tres.

**Qué podría refutarlo:** un grupo bancario puede tener sistemas segregados por filial, con lo que tres compromisos distintos son posibles. Por eso `KJ-2` lleva confianza moderada para la unicidad y alta sólo para la observación.

### E-2.1 Y por qué un solo caso ya cambia la cifra

Tres entradas de ochenta y seis son el 3,5 %. Parece poco. Pero el hallazgo no es «el recuento está inflado un 3,5 %»: es que **el recuento es un techo cuya distancia al suelo no se puede medir desde fuera**.

La búsqueda por similitud textual encontró otros pares sospechosos que **no se pudieron resolver**: dos entradas de construcción con razones sociales distintas, dos «grupos de compañías» con nombres diferentes, dos entidades bancarias más sin dominio. Ninguno es concluyente, y precisamente por eso el 86 no es una medida.

Esto conecta con dos hallazgos previos de la cartera y los completa:

- `CTI-2026-050` documentó un actor con **35 entradas y sólo 26 descripciones distintas**, con al menos cuatro víctimas listadas dos veces bajo dos nombres.
- `CTI-2026-056`, en este mismo lote, documentó el caso extremo opuesto: **429 de 432 entradas eran nombres de fichero**, de modo que decenas de entradas correspondían a una sola víctima.

**Los tres juntos dicen lo mismo con intensidades distintas: una entrada de sitio de filtración no es una víctima.** Y esa es la lección transferible de los tres expedientes.

## E-3. Relevancia regional: ninguna

| País | Entradas |
|---|---|
| Estados Unidos | 43 |
| Alemania | 4 |
| Canadá | 3 |
| Reino Unido | 3 |
| Australia | 2 |
| India · Rumanía | 1 cada uno |
| Sin país | 29 |

Siete países, cero entradas latinoamericanas, cero chilenas. Con un 34 % del catálogo sin país, la ausencia no es demostrable con la fuerza con que lo sería en `krybit` —donde la cobertura es del 83 %—, pero el catálogo visible es inequívocamente norteamericano y europeo.

Sectores: Manufactura 14, Sanidad 13, **Servicios financieros 12**, Construcción 8, Tecnología 7. Ninguno por encima del 16 %, de modo que tampoco hay concentración sectorial — con la salvedad de que doce entradas financieras incluyen las tres de `KJ-2`, lo que reduce ese sector a diez organizaciones como máximo.

**Para la cartera: vigilancia de línea base.** No desplaza ninguna prioridad, y en particular no afecta a Chile, donde `CTI-2026-015` sitúa a Qilin con veinte de las treinta víctimas medidas.

## E-4. Decisiones que este informe pide

1. **No usar la cifra de 86 en comparaciones de volumen sin la salvedad de `KJ-2`.** Es un techo.
2. **Aplicar la comprobación de similitud del `Anexo D` a los demás catálogos de la cartera.** Cuesta minutos y ya ha encontrado algo en tres actores distintos.
3. **Reevaluar en catorce días.** Siete días de silencio tras un goteo de trece entradas no permiten concluir cese, pero el patrón merece vigilancia (`I-1`).
4. **Resolver la contradicción de antigüedad de `KJ-7`** antes de aceptar cualquier parte del perfil de este actor.

---

# NIVEL OPERACIONAL

## O-1. Identificación

| Campo | Valor | Procedencia |
|---|---|---|
| Nombre | Storm | Título de su propio sitio, «Storm Blog» |
| Primera entrada observada | **2026-09-30** | Medición propia |
| Última entrada observada | **2026-11-12** | Medición propia |
| Clasificación de novedad | **Dudoso**, retraso mediano 27,8 d | Método de `CTI-2026-054` |
| Antigüedad declarada | **2021** | **Perfil de proveedor — contradictoria** (`KJ-7`) |
| Modelo declarado | RaaS con red de afiliados | **Perfil de proveedor** |
| Táctica declarada | **«Inflación de víctimas»** | **Perfil de proveedor — confirmada** (`KJ-3`) |
| Sitios | **1, activo** | Medición propia |

**Advertencia sobre el nombre.** «Storm» es también el prefijo que un fabricante de sistemas operativos emplea en su nomenclatura de actores no atribuidos —del tipo `Storm-NNNN`—, y el agregador CTIWatch lista una entidad `Storm-3358` distinta de ésta. **No deben confundirse.** Este expediente se refiere exclusivamente al actor cuyo sitio se titula «Storm Blog» y cuyas 86 entradas se midieron. Es la clase de colisión de nombres que `CTI-2026-054` `§O-8.3` documentó y que el correctivo 8 de su `Anexo D` exige comprobar.

## O-2. El catálogo

| Medición | Valor | Lectura |
|---|---|---|
| Con fecha declarada | **86 / 86 (100 %)** | **Lo que hace posible `KJ-1`** |
| Con captura | 86 / 86 (100 %) | Nivel 3 de la escala de prueba |
| **Con dominio** | **39 / 86 (45 %)** | **La más baja del lote con catálogo legible** |
| Con país | 57 / 86 (66 %) | Base débil para `KJ-6` |
| Con sector | 57 / 86 (66 %) | — |
| Con revisión posterior | 9 / 86 (10 %) | Por debajo de la media del semestre |
| Con historial de título | 0 | No desenmascara progresivamente |

**La cobertura de dominio del 45 % es el límite práctico de este expediente**, y conviene decir por qué importa. Un catálogo cuyos títulos son dominios —como `krybit` al 96 % o `safepay` al 99 %— permite dos cosas: que la víctima se reconozca en minutos, y que el analista detecte duplicados comparando dominios. Aquí los títulos son razones sociales, de modo que **ambas cosas se vuelven difusas**: una organización puede no reconocer su propia razón social abreviada, y la detección de duplicados exigió comparación textual con un umbral arbitrario.

**Eso significa que `KJ-2` es el resultado del método más débil del expediente**, y que probablemente haya más duplicados que no se detectaron. Es coherente con que sea un techo.

## O-3. La infraestructura más simple del lote

Una sola dirección:

```
yqhecvqtdvq6p7duqcgw2qca77spbgakxcoibtx6zpvfshltsbbbhfqd.onion
```

Titulada «Storm Blog», activa al 19 de noviembre de 2026, y origen de las 86 entradas.

| Actor del lote | Direcciones registradas | Activas |
|---|---|---|
| BrainCipher | **54** | 6 |
| dragonforce | 20 | **0** |
| apt73 (retirado del lote) | 11 | 2 |
| krybit | 6 | 4 |
| safepay | 5 | **0** |
| Booba Project | 4 | 2 |
| **Storm** | **1** | **1** |

Dos lecturas, y la segunda es la que afecta a la clasificación.

**Primera: la simplicidad no es debilidad.** Un solo sitio activo y sin rotación es una operación que no ha perdido infraestructura ni ha necesitado cambiarla. `safepay` y `dragonforce` tienen cinco y veinte direcciones registradas **y ninguna activa**; este actor tiene una y funciona.

**Segunda, y es la limitación: no hay portal de negociación observable.** `Booba Project` etiqueta su sala de conversación y su almacén; `BrainCipher` tuvo un «Client Area». Aquí sólo hay blog. El criterio más discriminante del triaje de `CTI-2026-042` `Anexo D` es *cómo contacta la víctima* —portal significa operación, correo electrónico puede significar herramienta usada por cualquiera—, y **este expediente no puede responderlo**. Es `G-3`.

## O-4. Después del volcado: trece entradas

Trece entradas en los cuarenta y tres días posteriores al 30 de septiembre, repartidas en siete días, con un máximo de tres. Y nada desde el 12 de noviembre.

**La lectura más económica** es que el catálogo del primer día era el trabajo acumulado antes de abrir el sitio, y que la capacidad de generar víctimas nuevas del actor está en el orden de **una cada tres días**, no de setenta y tres en un día. Si eso es correcto, su cifra total engaña por partida doble: por la inflación de `KJ-2` y por el volcado de `KJ-1`.

**Siete días de silencio no permiten concluir cese**, y menos en un actor cuyo intervalo típico tras el volcado es de seis días. Aplicando el paso 2 del `Anexo D` de `CTI-2026-058` —medir el silencio en unidades de la cadencia propia—, siete días es poco más de un intervalo. No es una señal.

## O-5. El perfil, y el acierto que hay que reconocerle

| Elemento declarado | Estado |
|---|---|
| **«Tácticas de inflación de víctimas»** | **CONFIRMADO en los datos propios** (`KJ-2`) |
| Antigüedad desde 2021 | **CONTRADICE** el catálogo observado (`O-5.1`) |
| RaaS con red de afiliados | Sin apoyo. **Contradicho débilmente** por el goteo de `O-4`: una red de afiliados produce flujo, no un volcado y silencio |
| «Muertes de espejo» para complicar la atribución | Sin apoyo. **Contradicho** por tener un solo sitio |
| Explotación de exposiciones recientes o de día cero | Sin apoyo, sin ninguna CVE citada |
| Cronómetros de filtración de alta presión | Sin apoyo; no se observó plazo en ninguna entrada |
| Pivotes a la nube y puertas traseras en la nube | Sin apoyo, sin indicadores |
| Umbrales de pago variables por sector | Sin apoyo; no se observó ninguna cifra |

**Uno confirmado de ocho, y es el que importa.** La ficha declaró que el actor infla recuentos, y los datos propios encontraron un grupo bancario contado tres veces. Es la primera vez en los cuarenta informes de esta cartera que una ficha de proveedor sin referencias **predice un comportamiento que la medición independiente confirma**.

**Qué hace y qué no hace eso.** No convierte las otras siete afirmaciones en ciertas: tres de ellas están débilmente contradichas por los propios datos. Lo que hace es mover la ficha de «sin ningún apoyo» a «con un acierto comprobable», lo que en la escala de prueba de `CTI-2026-048` `Anexo D` es un cambio real aunque pequeño. **Y obliga a una corrección de postura general:** la cartera ha tratado estas fichas como no corroboradas y debe seguir haciéndolo, pero «no corroborado» no es lo mismo que «falso», y este caso lo demuestra.

### O-5.1 La contradicción de antigüedad

La ficha afirma que el actor «surgió por primera vez en el submundo en 2021». El catálogo observable empieza el 30 de septiembre de 2026 con 86 entradas cuyas fechas declaradas no van más allá de agosto de 2026.

Cinco años de operación no caben en 86 entradas. Las tres explicaciones:

1. **El nombre designa dos cosas distintas** y la ficha mezcla un actor de 2021 con el sitio de 2026. Es exactamente el error que `CTI-2026-054` `§O-8.3` documentó en otra fuente con el nombre `soul`, y el que el correctivo 8 obliga a comprobar.
2. **El sitio es una reapertura** de una operación anterior cuyo catálogo previo se perdió o se abandonó. La ficha no lo afirma.
3. **La antigüedad declarada es errónea**, lo que en una ficha con indicio de redacción automática es perfectamente posible.

**No se puede decidir**, y por eso `KJ-7` lleva confianza baja. Pero la consecuencia práctica es clara: **ninguna parte de ese perfil debe usarse sin resolver primero si habla de este actor** (`I-4`).

## O-6. Clasificación

Triaje de `CTI-2026-042` `Anexo D`: cumple **tres criterios de siete**. Tiene sitio de filtración con víctimas nombradas, tiene infraestructura propia activa, y tiene continuidad temporal de mes y medio. Falla en análisis primario con muestra, en víctima confirmada por tercero, en linaje verificable, y **en canal de contacto observable** — que es el criterio decisivo y queda sin responder.

**Clase: marca con operación, con recuento inflado y canal de contacto sin determinar.**

## O-7. Hipótesis y pre-mortem

**H-1.** *Las tres entradas bancarias son un solo compromiso.* **Muy probable** *(80–95 %)*. Apoyo: nombres compartidos, dominios del mismo grupo, mismo día de publicación.

**H-2.** *Hay más duplicados sin detectar.* **Probable** *(55–80 %)*. Apoyo: la cobertura de dominio del 45 % hace la detección difusa, y la búsqueda textual dejó varios pares sin resolver.

**H-3.** *El catálogo del primer día era trabajo acumulado antes de abrir el sitio.* **Muy probable** *(80–95 %)*. Apoyo: retraso mediano de 27,8 días con 100 % de cobertura de fecha.

**H-4.** *No hay red de afiliados, pese a lo declarado.* **Posible** *(40–60 %)*. Apoyo: un volcado y goteo es lo contrario del flujo irregular que produce una red de afiliados — el mismo razonamiento de consistencia que `CTI-2026-058` `§O-4.1` y `CTI-2026-059` `§O-6`.

**H-5.** *La ficha mezcla dos actores con el mismo nombre.* **Posible** *(40–60 %)*. Es `KJ-7`.

### Pre-mortem

*Si este informe se equivoca, será en `KJ-2`.* La detección de la inflación se hizo por similitud textual de razones sociales, que es el método más débil del expediente, y la unicidad del compromiso es una inferencia: un grupo bancario con filiales puede tener sistemas segregados y sufrir tres incidentes. **Si las tres entradas son tres compromisos reales, el hallazgo propio del informe desaparece** — aunque `KJ-3` se mantendría, porque la declaración del proveedor seguiría ahí sin confirmar. Es `I-2`.

*El segundo modo de fallo es `KJ-6`.* Con el 34 % del catálogo sin país, la ausencia de víctimas latinoamericanas está peor apoyada que en otros expedientes del lote. Veintinueve entradas sin país podrían incluir alguna.

---

## 14. Brechas de inteligencia y requisitos de colección

**G-1. No sabemos si el actor sigue operando.** Siete días de silencio no son concluyentes con su cadencia.
→ **I-1.** Reevaluar a catorce días, aplicando el paso 2 del `Anexo D` de `CTI-2026-058`: medir el silencio en unidades de su propia cadencia. **Disparador: 3 de diciembre de 2026.**

**G-2. Las tres entradas bancarias no están verificadas como un solo compromiso.** Es el hallazgo propio del informe.
→ **I-2.** Comprobar la titularidad de los dos dominios y si el grupo notificó uno o varios incidentes. **Disparador:** inmediato; sostiene `KJ-2`.

**G-3. No se ha observado el canal de contacto con la víctima**, que es el criterio decisivo del triaje.
→ **I-3.** Lectura del sitio de filtración. Requiere acceso a Tor. **Disparador:** antes de elevar la clasificación.

**G-4. La contradicción de antigüedad de `KJ-7` está sin resolver**, e invalida el uso de todo el perfil.
→ **I-4.** Buscar si existe un actor distinto con este nombre activo desde 2021, y comprobar si la ficha mezcla expedientes. **Disparador:** antes de citar cualquier elemento del perfil.

**G-5. No sabemos cuántos duplicados más hay** (`H-2`), y la cobertura de dominio del 45 % lo impide.
→ **I-5.** Contrastar los 86 títulos contra el otro rastreador de la cartera, que puebla el dominio con más frecuencia.

**G-6. No hay ni un indicador técnico**, razón por la que no se emite nivel técnico.
→ **I-6.** Informe de incidente de una víctima, o muestra en repositorio público.

---

# ANEXOS

## Anexo A — Indicadores

### A.1 — Infraestructura

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| domain | `yqhecvqtdvq6p7duqcgw2qca77spbgakxcoibtx6zpvfshltsbbbhfqd.onion` | **Único sitio del actor, «Storm Blog», activo al 2026-11-19.** Sirvió las 86 entradas | Alta | 90 días | Vigilancia |
| artefacto | **1 sola dirección, sin rotación, activa** | **La infraestructura más simple del lote** frente a las 54 de BrainCipher (`O-3`) | Alta | 90 días | Análisis |
| artefacto | **Sin portal de negociación observable** | Deja sin responder el criterio decisivo del triaje de `CTI-2026-042` (`G-3`) | Alta como ausencia | 90 días | **No elevar la clasificación hasta resolverlo** |
| artefacto | **Dirección sin prefijo legible** | A diferencia de krybit y safepay: **no cazable por patrón** | Alta | Sin caducidad | Análisis |

### A.2 — Patrones del catálogo

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| pattern | **Tres entradas correspondientes a un solo grupo empresarial: matriz y dos filiales con dominios distintos** | **El hallazgo propio** (`KJ-2`). Detectado por similitud textual; los nombres **no se reproducen** (`§3.3`) | Alta para la observación, **moderada para la unicidad** | 90 días | **Tratar el recuento como techo** |
| pattern | **85 % del catálogo publicado el primer día con retraso mediano de 27,8 días** | `KJ-1`. **Sitio nuevo, catálogo de un mes.** Clasificación «dudoso» | Alta | Histórico | Clasificación |
| pattern | **100 % de cobertura de fecha declarada** | **Es lo que hace posible distinguir volcado de actividad.** Único del lote con krybit | Alta | 90 días | **Exigirlo antes de leer una curva de actividad** |
| pattern | **Catálogo con razones sociales y sólo 45 % de dominios** | **Dificulta la detección de duplicados y el reconocimiento por la víctima** (`O-2`) | Alta | 90 días | Análisis |
| pattern | **Volcado grande seguido de goteo de una entrada cada tres días** | `O-4`. **La capacidad real es muy inferior a la cifra total** | Moderada | 90 días | **Dimensionar la amenaza por el goteo, no por el total** |
| artefacto | **El perfil del proveedor declara «inflación de víctimas» y los datos lo confirman** | `KJ-3`. **Primera vez en la cartera que una ficha no corroborada acierta de forma comprobable** | Moderada | Sin caducidad | **Matizar la postura sobre fichas de proveedor** |
| artefacto | **El perfil declara antigüedad de 2021, incompatible con el catálogo** | `KJ-7`, `O-5.1`. **O el nombre designa dos cosas, o la ficha mezcla expedientes** | Baja | Hasta resolver `I-4` | **No citar el perfil** |
| artefacto | **Colisión de nombre con la nomenclatura `Storm-NNNN` de un fabricante** | `O-1`. Otro agregador lista un `Storm-3358` distinto | Alta | Sin caducidad | **Comprobar identidad antes de corroborar** |

### A.3 — Victimología

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| cartera | **86 entradas, de las que 3 son una organización** | **Techo, no medida** (`E-2.1`) | Alta como recuento de entradas | 90 días | Medición con salvedad |
| cartera | **43 estadounidenses (50 %) · 7 países · 29 sin país** | La dispersión más estrecha del lote | Alta como recuento | 90 días | Medición |
| cartera | **0 entradas latinoamericanas · 0 chilenas** | `KJ-6`. **Con 34 % sin país: ausencia no demostrable** | **Moderada** | 90 días | **No concluir ausencia** |
| cartera | **12 entradas financieras, reducibles a 10 organizaciones** | El sector afectado por `KJ-2` | Moderada | 90 días | Análisis |
| cartera | **Sin concentración sectorial**: máximo 16 % | Manufactura 14, Sanidad 13, Financiero 12 | Alta como recuento | 90 días | Medición |
| cartera | **7 días sin publicar al cierre** | **Poco más de un intervalo típico: no es señal** (`O-4`) | Alta | **Reevaluar el 2026-12-03** | Vigilancia |

## Anexo B — Fuentes y valoración

| # | Fuente | Grado | Qué aportó | Salvedad |
|---|---|---|---|---|
| 1 | API de cti.fyi, entradas y ficha de grupo, 2026-11-19 | **Medición propia** sobre datos de proveedor | Las 86 entradas, el sitio único, la cadencia, la detección de `KJ-2` | Evaluada en `CTI-2026-054`. **Cobertura de dominio del 45 %**, lo que limita `KJ-2` |
| 2 | Ficha de perfil del grupo, misma fuente | **Proveedor, con indicio de redacción sintética.** Elevada parcialmente por `KJ-3` | La declaración de inflación de víctimas —**confirmada**— y la antigüedad de 2021 —**contradictoria**— | **Una de ocho afirmaciones confirmada, tres débilmente contradichas.** Véase `O-5` |
| 3 | CTIWatch, ficha pública, 2026-11-19 | Proveedor, prosa generada automáticamente | 89 víctimas, cifra compatible con las 86 medidas. **Lista además un `Storm-3358` distinto** (`O-1`) | Defectos en `CTI-2026-054` `§O-8.2` |
| 4 | `CTI-2026-054` Anexo D | Propio | El correctivo 1 que clasifica `KJ-1`, y el correctivo 8 que obliga la advertencia de `O-1` | Emitido el mismo día |
| 5 | `CTI-2026-050` · `CTI-2026-056` | Propio | Los otros dos casos de «una entrada no es una víctima» que `E-2.1` reúne | — |
| 6 | `CTI-2026-058` Anexo D · `CTI-2026-048` Anexo D · `CTI-2026-042` Anexo D | Propio | El método del silencio de `O-4`, la escala de prueba y el triaje de `O-6` | — |

## Anexo C — Léxico de probabilidad y confianza

ICD 203. **Casi con certeza** ≥99 % · **muy probable** 80–95 % · **probable** 55–80 % · **posible** 40–60 % · **improbable** 20–45 % · **muy improbable** 5–20 %. La **confianza** califica la base de prueba. Aquí: alta para los recuentos y la cadencia; **moderada para `KJ-2`** en cuanto a la unicidad del compromiso; **moderada para `KJ-6`** por la cobertura de país del 66 %; **baja para `KJ-7`** y para todo el perfil salvo el elemento confirmado.

## Anexo D — Cómo detectar que un catálogo cuenta la misma víctima varias veces

Procedimiento, diez minutos. Es el caso simétrico del `Anexo D` de `CTI-2026-056` —que detectaba catálogos contando **ficheros**— y aquí se trata de catálogos contando **filiales, marcas o divisiones**.

**Paso 1 — Si hay dominios, comparar dominios.** Es la vía limpia y la que no exige criterio: dos entradas con el mismo dominio son la misma organización. Sólo funciona si la cobertura de dominio es alta; aquí era del 45 % y por eso hubo que ir al paso 2.

**Paso 2 — Comparar razones sociales por similitud textual.** Un umbral en torno al 0,6 de similitud de secuencias devuelve candidatos manejables. **Produce falsos positivos** —dos empresas de construcción con apellidos distintos salen emparejadas— y hay que resolverlos a mano.

**Paso 3 — Buscar los términos compartidos iniciales, no la similitud global.** Es el refinamiento que encontró el caso de este informe: tres entradas que comparten **los dos primeros términos** de la razón social y difieren en el resto son candidatas a matriz y filiales, aunque su similitud global sea baja. Un grupo empresarial nombra así a sus marcas.

**Paso 4 — Comprobar la fecha.** Varias entradas de la misma organización **publicadas el mismo día** apuntan a un compromiso contado varias veces. Publicadas con meses de diferencia, pueden ser compromisos distintos — o republicación, que es el caso de `CTI-2026-055`.

**Paso 5 — Resolver la titularidad de los dominios.** Es lo único que convierte la sospecha en hallazgo, y es la parte que este informe dejó en `I-2` por no poder completarla.

> **El paso más productivo es el tercero y casi nadie lo hace**, porque la intuición lleva a buscar nombres parecidos y los nombres de un grupo empresarial **no se parecen: comparten prefijo**. «Banco X Group», «Banco X and Trust» y «Banco X Community» tienen similitud global baja entre sí y comparten los dos primeros términos.
>
> Y la conclusión que une este anexo con el de `CTI-2026-056`: **el recuento de entradas de un sitio de filtración es un techo en los dos sentidos** — infla cuando cuenta ficheros o filiales por separado, y nunca deshincha. Toda comparación de volumen entre actores que no haya pasado por estos dos filtros compara cosas distintas.

## Anexo E — Marcos de referencia empleados

ICD 203. Escala de Almirantazgo con los grados propios de la cartera. TLP 2.0 y PAP. Triaje de actor nuevo de `CTI-2026-042` `Anexo D`, con el criterio de contacto como discriminante — aquí **sin responder**. Correctivos 1 y 8 de `CTI-2026-054` `Anexo D`. Escala de prueba de ocho niveles de `CTI-2026-048` `Anexo D`. Método del silencio de `CTI-2026-058` `Anexo D`, paso 2. **No se emite mapa ATT&CK ni nivel técnico**: no hay ni una técnica observada, y el perfil está bajo la contradicción de `KJ-7`.

## Anexo F — Paquete legible por máquina

| Medición | Procedimiento |
|---|---|
| Entradas | `GET /api/v1/posts?group=Storm&since=2026-05-19&limit=500` |
| Infraestructura | `GET /api/v1/groups/Storm` → `locations[]` |
| Volcado inicial | Agrupar `discovered[:10]` → 73 el 2026-09-30 de 86 |
| Retraso | Mediana de `discovered − published` sobre las 86 → **27,8 días** |
| **Detección de duplicados** | Similitud de secuencias entre pares de `post_title` con umbral 0,62, **más comparación de los dos primeros términos de cada razón social** (paso 3 del `Anexo D`) |
| Verificación | Titularidad de los dominios de las entradas emparejadas |

## Anexo G — Control de cambios

| Versión | Fecha | Qué cambió | Qué juicio se movió |
|---|---|---|---|
| 1.0 | 2026-11-19 | Emisión inicial. Incluye el volcado del primer día con retraso de 27,8 días y la clasificación «dudoso» (`KJ-1`), **la inflación del recuento con un grupo bancario contado tres veces** (`KJ-2`), **la primera vez en la cartera que una ficha de proveedor no corroborada acierta de forma comprobable** (`KJ-3`), la infraestructura más simple del lote (`KJ-4`), y la contradicción de antigüedad sin resolver (`KJ-7`) | — |

## Anexo H — Realimentación del consumidor

Este informe se corrige si se recibe: confirmación de que las tres entradas bancarias son un solo compromiso, que elevaría `KJ-2` a confianza alta, o de que son tres, que lo retiraría (`I-2`); la lectura del sitio de filtración, que resolvería el canal de contacto y permitiría elevar la clasificación (`I-3`); evidencia sobre la antigüedad declarada, que resolvería `KJ-7` (`I-4`); una víctima latinoamericana, que invalidaría `KJ-6`; o una entrada nueva posterior al 12 de noviembre, que cerraría `G-1`.

El requisito más importante es **`I-2`**, porque `KJ-2` es el hallazgo propio del expediente, descansa en el método más débil que aquí se empleó, y es el que sostiene la recomendación general de `E-4`: que el recuento de entradas de cualquier sitio de filtración se trate como un techo.
