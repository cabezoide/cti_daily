---
tlp: "TLP:CLEAR"
pap: "PAP:WHITE"
id: "CTI-2026-059"
version: "1.0"
tipo: "Perfil de operación de extorsión"
foco_regional: "Estados Unidos 56 % · Brasil 2 · España 2 · sin relevancia chilena"
niveles: ["Estratégico", "Operacional"]
autor: "Célula CTI"
actor: "Booba Project"
fecha: "2026-11-19"
caduca: "2026-12-19"
distribucion: "ADVERTENCIA DE CONTENIDO: el catálogo de este actor incluye entradas cuyo título es el nombre de un documento de identidad de una persona física concreta. Este informe documenta el patrón y NO reproduce ninguno de esos títulos, ni nombres de víctima, ni nombres de persona. Es la regla de CTI-2026-049 aplicada a un actor que la hace necesaria. Difusión libre conservando la atribución y las salvedades de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-059

## Casi la mitad de sus víctimas son hospitales y administraciones públicas, y publica documentos de identidad de personas concretas

### Actor nuevo verificado, activo el día de emisión, con la concentración sectorial más alta del lote y el catálogo que más se edita después de publicado

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-059` |
| Versión | 1.0 |
| Tipo | Perfil de operación de extorsión |
| Clasificación | `TLP:CLEAR` · `PAP:WHITE` |
| Fecha de emisión | 2026-11-19 |
| Caducidad | 2026-12-19 |
| Niveles | Estratégico · Operacional |
| Actor | Booba Project |
| Entradas en la ventana | 129 · **100 % con captura** |
| Concentración sectorial | **Sanidad 39 + Administración 23 = 48 %** |
| Clasificación de novedad | **Nuevo contemporáneo verificado** (retraso mediano 0,0 d) |
| Infraestructura | 4 sitios · **2 activos** · funcionalmente separados |
| Autor | Célula CTI |

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** **Concentra el 48 % de su catálogo en sanidad y administración pública, la proporción sectorial más alta de los seis actores del lote.** Treinta y nueve entradas de sanidad y veintitrés de administración y sector público, de 129. Le siguen servicios profesionales con catorce y educación con once — de modo que **servicios esenciales y públicos suman el 56 %** si se incluye educación. Valoramos **casi con certeza** *(≥99 %)* el recuento, sobre un catálogo con 74 % de cobertura de sector. **Confianza: alta.** *Consecuencia:* es el actor del lote cuya victimología implica **daño a terceros que no son la víctima** —pacientes, administrados, estudiantes—, y eso cambia qué significa una filtración suya (`E-2`).

**KJ-2.** **Y el catálogo incluye entradas cuyo título es el nombre de un documento de identidad de una persona física concreta.** Entre las 129 hay cuatro entradas cuyo título es un nombre de fichero, y de ellas varias corresponden a documentos personales: tarjetas de identificación, licencias y expedientes nominales. Valoramos **casi con certeza** *(≥99 %)* la observación. **Confianza: alta.** *Consecuencia, y es una decisión de este informe:* **no se reproduce ninguno de esos títulos**, por la regla establecida en `CTI-2026-049`. Y la consecuencia para una organización de los sectores de `KJ-1` es más grave que la habitual: **lo expuesto no es información corporativa, es la identidad de personas individuales** (`E-3`).

**KJ-3.** **Es un actor nuevo de verdad, y está verificado por el método de `CTI-2026-054`: retraso mediano de cero días entre la fecha que declara y la fecha en que fue descubierto.** De los sesenta y ocho grupos que parecían estrenarse en el semestre, sólo catorce superan esa prueba, y éste es uno de ellos — con primera entrada el 6 de julio de 2026 y **actividad el mismo día de emisión de este informe**. Valoramos **casi con certeza** *(≥99 %)* que su aparición es contemporánea y no una incorporación retroactiva de cobertura. **Confianza: alta.** *Consecuencia:* a diferencia de veintitrés de los sesenta y ocho candidatos, **aquí el expediente mide realmente el arranque de una operación** (`O-1`).

**KJ-4.** **Es el actor del lote que más edita sus entradas después de publicarlas: cuarenta y cinco de 129 (35 %) llevan marca de revisión.** En el conjunto del semestre la proporción media es del 16,3 %. Valoramos **casi con certeza** *(≥99 %)* el recuento. **Confianza: alta** para la medición, **baja** para la interpretación, porque no sabemos si el campo registra cambios sustantivos o también cambios triviales de la página —brecha `G-4` de `CTI-2026-054`—. *Consecuencia:* si las revisiones son sustantivas, **una entrada de este actor no es un estado final**, y una organización que compruebe su situación una vez puede encontrarla distinta días después (`O-4`).

**KJ-5.** **Su infraestructura está separada por función y el actor la etiqueta él mismo: sitio de filtración, sala de negociación y dos almacenes.** Los títulos declarados son «Booba Project», «Booba Chat» y «Booba Storage» por duplicado. Dos de los cuatro están activos al 19 de noviembre, incluido el almacén secundario; el de negociación figura con estado de incidencia. Valoramos **casi con certeza** *(≥99 %)* los recuentos. **Confianza: alta.** *Consecuencia:* la separación funcional responde afirmativamente al criterio más discriminante del triaje de `CTI-2026-042` —**hay portal, luego hay operación y no herramienta**—, y el almacén separado explica cómo sostiene volúmenes declarados de 50 a 70 GB por caso (`O-3`).

**KJ-6.** **No tiene relevancia chilena y tiene muy poca regional: tres entradas latinoamericanas de 129 (2,3 %), ninguna chilena.** Su catálogo es estadounidense en el 56 % —72 de 129— con sólo catorce países representados, la segunda dispersión más estrecha del lote. Valoramos **probable** *(55–80 %)* que la ausencia chilena sea real, con 74 % de cobertura de país. **Confianza: moderada.** *Consecuencia:* **para una organización chilena este actor es de vigilancia y no de prioridad**, y la prioridad sigue siendo Qilin por `CTI-2026-015` (`E-4`).

**KJ-7.** **El perfil declarado afirma que el acceso procede de credenciales robadas por programas de sustracción de información y que no hay programa de afiliados, y la segunda parte es consistente con lo medido.** La ficha del proveedor describe volcado de credenciales mediante infostealer, movimiento lateral, recolección masiva, exfiltración y cifrado, con un promedio declarado de 50 a 70 GB por caso y anuncios por Telegram. Nada está corroborado. Valoramos **probable** *(55–80 %)* la ausencia de programa de afiliados, por coherencia con la cadencia medida; **posible** *(40–60 %)* el vector de credenciales sustraídas. **Confianza: baja para el perfil.** *Consecuencia:* el único control que el expediente justifica es genérico y ya conocido —rotación de credenciales expuestas en filtraciones públicas—, y es el mismo al que llegó `CTI-2026-051` por otra vía (`O-5`).

---

## 2. Resumen ejecutivo

Booba Project apareció el 6 de julio de 2026, publicó **129 entradas** hasta el mismo día de emisión de este informe, y es uno de los **catorce actores del semestre que son nuevos de verdad** — una distinción que importa, porque de los sesenta y ocho que lo parecían, veintitrés eran sitios que ya existían y que el rastreador empezó a mirar en septiembre. La prueba es la del método de `CTI-2026-054`: el retraso mediano entre la fecha que el propio sitio declara y la fecha en que fue descubierto es de **cero días**, lo que significa que apareció mientras la fuente ya vigilaba.

Lo que lo distingue de los otros cinco actores del lote es a quién ataca. **Treinta y nueve de sus 129 víctimas son organizaciones sanitarias y veintitrés son administraciones públicas: el 48 % del catálogo.** Añadiendo educación, los servicios esenciales y públicos llegan al 56 %. Ninguno de los otros cinco se acerca: `krybit` no pasa del 13 % en ningún sector, `safepay` del 18 %, `Storm` del 16 %.

Esa concentración cambia lo que significa una filtración suya. Cuando el afectado es un hospital o un ayuntamiento, **los datos expuestos no son de la organización: son de las personas a las que atiende**. Y el catálogo lo confirma de la forma más directa posible: entre sus 129 entradas hay varias cuyo título es el nombre de un documento de identidad de una persona física concreta — tarjetas de identificación, licencias, expedientes nominales.

**Este informe no reproduce ninguno de esos títulos.** Es la regla que `CTI-2026-049` estableció cuando un actor convirtió al dueño de la empresa, como persona física, en la palanca de extorsión: documentar el patrón, no los datos. Aquí es más necesaria todavía, porque las personas afectadas no son ni la víctima corporativa ni decidieron nada.

Dos rasgos operativos completan el perfil. El primero es que **edita sus entradas después de publicarlas más que ningún otro actor del lote**: cuarenta y cinco de 129 llevan marca de revisión, frente a una media del 16,3 % en el semestre. Si esas revisiones son sustantivas —y no se sabe—, una entrada suya no es un estado final, y comprobar la propia situación una vez no basta.

El segundo es que **su infraestructura está separada por función y él mismo la etiqueta**: un sitio de filtración, una sala de negociación llamada «Booba Chat» y dos almacenes llamados «Booba Storage». Dos de los cuatro están activos. Esa separación es lo que responde afirmativamente al criterio más discriminante del triaje de la cartera —si hay portal de contacto, hay operación y no herramienta— y explica cómo sostiene los volúmenes de 50 a 70 GB por caso que su perfil declara.

No tiene relevancia chilena: tres entradas latinoamericanas de 129, ninguna chilena, y un catálogo estadounidense en el 56 %. Para una organización chilena es vigilancia, no prioridad.

---

## 3. Alcance y limitaciones

### 3.1 Base de la medición

Las 129 entradas y los 4 sitios proceden de la API de cti.fyi consultada el 19 de noviembre de 2026. Reproducible con `Anexo F`.

### 3.2 Límites

- **El sector y el país son enriquecimiento derivado.** Cobertura del 74 % en ambos. `KJ-1` y `KJ-6` heredan ese límite, y `KJ-1` es el juicio principal del informe.
- **No se sabe qué registra el campo de revisión.** Es la brecha `G-4` de `CTI-2026-054` y limita `KJ-4` a la medición, sin interpretación.
- **No se leyó el sitio de filtración.** Sin acceso a Tor en este entorno.
- **Ninguna víctima ha confirmado nada.**
- **El perfil del actor no está corroborado**, incluido el promedio declarado de 50 a 70 GB.
- **No se cuantificó el número exacto de entradas con datos de persona física**, por la razón de `§3.3`: hacerlo con precisión habría exigido examinar y clasificar títulos que contienen esos datos. Se documenta el patrón y su existencia, no su recuento fino.

### 3.3 Higiene, que en este expediente es la decisión principal

**No se reproduce:** ningún nombre de organización víctima, ningún dominio, ningún nombre de persona física, y **ningún título de entrada que sea el nombre de un documento personal**.

La regla procede de `CTI-2026-049`, donde la cartera se encontró con un actor cuya palanca de extorsión era el titular de la empresa como persona física —con identificación fiscal, domicilio y teléfono particular— y decidió documentar el mecanismo sin reproducir ni un dato, ni censurado.

**Aquí la razón es más fuerte.** En aquel caso el afectado era el dueño de la organización atacada. En éste, con el 48 % del catálogo en sanidad y administración pública, los afectados son **pacientes y administrados**: personas que no son la víctima corporativa, que no tomaron ninguna decisión sobre la seguridad de sus datos, y que no pueden hacer nada al respecto. Reproducir aquí el nombre de una tarjeta de identificación individual añadiría una exposición permanente en un documento de difusión libre, sobre alguien que ya está expuesto por decisión de un adversario.

Y conviene nombrar la tensión, porque existe: **no publicar el dato reduce la verificabilidad de este informe.** Un lector no puede comprobar `KJ-2` por sí mismo con lo que aquí se publica. Se acepta ese coste. El procedimiento del `Anexo F` permite a cualquiera con acceso a la fuente reproducir la observación sin que este documento sea el vehículo de la exposición.

### 3.4 Veredicto por nivel

| Nivel | Veredicto | Motivo |
|---|---|---|
| Estratégico | **Utilizable** | Victimología con 74 % de cobertura y concentración inequívoca |
| Operacional | **Utilizable** | Cadencia, infraestructura y revisiones medidas |
| Táctico | **No evaluable** | Sin TTP observados |
| Técnico | **No se emite** | Sin indicadores de ejecución; el perfil no basta (`O-5`) |

---

# NIVEL ESTRATÉGICO

## E-1. Cifras

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `129` | Entradas en la ventana | Noveno del semestre |
| `39` | **Entradas de sanidad (30 %)** | Primer sector |
| `23` | **Administración y sector público (18 %)** | Segundo sector |
| `48 %` | **Sanidad + administración** | **La concentración sectorial más alta del lote** |
| `56 %` | Añadiendo educación | Servicios esenciales y públicos |
| `72 / 129` | Entradas estadounidenses (56 %) | Sólo **14 países** |
| `3` | Entradas latinoamericanas (2,3 %) | **0 chilenas** |
| `129 / 129` | Entradas con captura | 100 % |
| `45 / 129` | **Entradas revisadas (35 %)** | **Media del semestre: 16,3 %** |
| `0,0 d` | Retraso mediano declarado→visto | **Nuevo contemporáneo verificado** |
| `4 / 2` | Sitios registrados / activos | **Separados por función** |

## E-2. La concentración sectorial, y por qué importa más que un número

| Sector | Entradas | Proporción |
|---|---|---|
| **Sanidad** | **39** | 30,2 % |
| **Administración y sector público** | **23** | 17,8 % |
| Servicios profesionales | 14 | 10,9 % |
| Educación | 11 | 8,5 % |
| Tecnología | 7 | 5,4 % |
| Otros | 35 | 27,1 % |

Comparado con el resto del lote:

| Actor | Sector principal | Proporción del principal |
|---|---|---|
| **Booba Project** | **Sanidad** | **30,2 %**, y 48 % con el segundo |
| safepay | Tecnología | 17,9 % |
| Storm | Manufactura | 16,3 % |
| dragonforce | Manufactura | 16,7 % |
| krybit | Tecnología | 12,3 % |

**Ningún otro actor del lote concentra así.** Y la combinación de los dos primeros sectores —sanidad y administración pública— no es una categoría cualquiera: son los dos ámbitos donde la organización atacada **custodia datos de personas que no eligieron confiárselos**.

Un paciente no decide el nivel de seguridad de su hospital. Un ciudadano no decide el de su ayuntamiento. En ambos casos la relación es obligada o cuasi obligada, y en ambos los datos custodiados son de las categorías de mayor sensibilidad: historial clínico, situación administrativa, datos de menores en el caso de educación.

### E-2.1 Y la hipótesis que la concentración sugiere

Un actor que concentra el 48 % en dos sectores, o selecciona, o explota algo común a ellos.

La selección deliberada tiene una lógica conocida: sanidad y administración pública tienen **menor tolerancia a la interrupción** —un hospital no puede detenerse— y **mayor exposición reputacional y regulatoria**, lo que históricamente se asocia con mayor propensión al pago. El perfil del proveedor no afirma selección, pero la victimología es compatible.

La alternativa es que el vector sea común: un producto de gestión clínica, un proveedor de servicios compartido, o un conjunto de credenciales procedente de un sector concreto. **No se puede distinguir con estos datos** y es la pregunta de más valor del expediente (`G-2`).

## E-3. Los documentos personales en el catálogo

Entre las 129 entradas hay cuatro cuyo título es un nombre de fichero y no una organización. Varias de ellas corresponden a **documentos de identificación de personas físicas concretas**: tarjetas de identificación, licencias, expedientes nominales en formato de documento portátil.

**Qué significa esto, y qué no.**

**Significa** que el sitio de filtración de este actor publica, al menos en ocasiones, el inventario de ficheros individuales y no sólo el nombre de la organización. Es el mismo comportamiento que `CTI-2026-056` documentó en otro actor del lote, donde el 99 % de las entradas eran nombres de fichero; aquí es el 3 %, de modo que **es excepción y no norma** — pero la excepción incluye documentos nominales.

**No significa** que el actor se dirija a particulares. Las personas cuyos documentos aparecen son, con casi total seguridad, **pacientes, administrados o empleados de las organizaciones víctimas** de `KJ-1`, cuyos expedientes estaban en los sistemas comprometidos.

Y tiene una consecuencia práctica para una organización de esos sectores que se encuentre en este catálogo: **la notificación a afectados no es un trámite diferible**. Si el sitio publica nombres de fichero y alguno es un documento nominal, la exposición de esa persona concreta ya es pública y comprobable por cualquiera, no una posibilidad futura.

> **Y una nota sobre por qué este informe no da más detalle.** La precisión que un analista desearía aquí —cuántas entradas, de qué tipo exacto, de qué organizaciones— exigiría examinar y catalogar datos de identidad de personas concretas, y publicar el resultado los expondría otra vez. El procedimiento del `Anexo F` permite reproducir la observación a quien tenga acceso a la fuente. **Este documento no va a ser el vehículo.** Es la misma decisión de `CTI-2026-049` y con la misma incomodidad: se pierde verificabilidad y se gana no participar en la exposición.

## E-4. Relevancia regional: baja

Tres entradas latinoamericanas de 129 (2,3 %): dos brasileñas y una más. Dos españolas. **Ninguna chilena.** Catorce países en total, con Estados Unidos en el 56 %.

Para la cartera: **vigilancia, no prioridad.** `CTI-2026-015` midió que Qilin concentra veinte de las treinta víctimas chilenas del top diez de extorsión, y ninguno de los seis actores de este lote lo desplaza. Este es, junto con `Storm` y `BrainCipher`, uno de los tres sin punto de contacto chileno.

**Con una salvedad que vale para los tres sectores de `KJ-1`:** una organización sanitaria o pública latinoamericana que use un proveedor de servicios compartido con víctimas estadounidenses de este actor está expuesta por esa vía y no por su geografía. Es el eje que la cartera tiene abierto sobre compromiso de proveedor, y es la razón por la que `G-2` importa.

## E-5. Decisiones que este informe pide

1. **Para una organización sanitaria, pública o educativa: comprobar el propio dominio.** El 88 % de las entradas lleva dominio y el 100 % captura, así que la comprobación cuesta minutos.
2. **Si aparece en el catálogo: comprobar si hay entradas con nombres de fichero asociadas**, porque de ello depende si la exposición de personas concretas ya es pública. Es la diferencia entre notificar como precaución y notificar como hecho consumado.
3. **Volver a comprobar.** Con el 35 % de las entradas revisadas después de publicadas, una comprobación única no es concluyente (`KJ-4`).
4. **No reasignar prioridad chilena.** `KJ-6` es explícito.
5. **Perseguir el factor común de `G-2`**, porque decide si la exposición de una organización depende de su sector o de un producto concreto.

---

# NIVEL OPERACIONAL

## O-1. Identificación, con la novedad verificada

| Campo | Valor | Procedencia |
|---|---|---|
| Nombre | Booba Project | Títulos de sus propios sitios |
| Primera entrada observada | **2026-07-06** | Medición propia |
| Última entrada observada | **2026-11-19** | Medición propia, **el día de emisión** |
| Aparición declarada | Finales de junio de 2026 | **Perfil de proveedor**, coherente con lo medido |
| Clasificación de novedad | **Nuevo contemporáneo verificado** | Retraso mediano **0,0 d** (`KJ-3`) |
| Modelo declarado | Doble extorsión, **sin programa de afiliados** | **Perfil de proveedor**, coherente con la cadencia |
| Acceso declarado | Credenciales de programas de sustracción de información | **Perfil de proveedor, no corroborado** |
| Volumen declarado | 50 a 70 GB por caso | **Perfil de proveedor** |
| Canal adicional declarado | Anuncios por Telegram | **Perfil de proveedor**, no verificado |
| Sitios | 4 registrados · **2 activos** · separados por función | Medición propia |

**Sobre la verificación de novedad, que es lo que distingue este expediente.** `CTI-2026-054` `§E-1` estableció que de sesenta y ocho grupos que parecían estrenarse en el semestre, sólo catorce lo hacían de verdad: los demás eran sitios preexistentes que el rastreador incorporó, detectables porque sus entradas declaran fechas de publicación muy anteriores a su descubrimiento. Este actor tiene **retraso mediano de cero días**, y su fecha de aparición declarada por el proveedor —finales de junio— coincide con la primera entrada observada, el 6 de julio.

Las dos cosas juntas significan que **este expediente mide el arranque real de una operación**, y no el día en que alguien empezó a mirar. Es una afirmación que la mayoría de los perfiles de actor nuevo no pueden hacer.

## O-2. El catálogo

| Medición | Valor | Lectura |
|---|---|---|
| Con captura | **129 / 129 (100 %)** | Comprobable visualmente |
| Con dominio | 113 / 129 (88 %) | Comprobable por la víctima |
| Con país | 96 / 129 (74 %) | Base de `KJ-6` |
| Con sector | 96 / 129 (74 %) | Base de `KJ-1` |
| Con fecha declarada | 80 / 129 (62 %) | — |
| **Con revisión posterior** | **45 / 129 (35 %)** | `KJ-4` |
| Con historial de título | 1 / 129 | Un solo desenmascaramiento registrado |
| **Con título que es nombre de fichero** | **4 / 129 (3 %)** | `KJ-2`, `E-3` |

En la escala de prueba de ocho niveles de `CTI-2026-048` `Anexo D`, este catálogo combina nivel 3 —captura, el que más engaña— con nivel 4 —organización identificable y verificable por dominio— en casi todo el conjunto, y alcanza nivel 6 en las cuatro entradas con nombre de fichero, porque **un inventario de ficheros es prueba de acceso que una captura no es**.

## O-3. La infraestructura separada por función

| Dirección | Título declarado | Estado |
|---|---|---|
| `7t3zi3e7ki6iseun77ofqtr6wmbpgnpc2ada6gstcxp54lw6q2zb7jad.onion` | **Booba Project** | **Activo** |
| `culappkcuogv2omb37253e236mvmsfzvl4yw3p3incyzeoixhc6ocxqd.onion` | **Booba Storage** | **Activo** |
| `eazk7las3xsvsyxgww3jgzammqjevso2ydnmlopdhl3u2muyrmmilrqd.onion` | **Booba Chat** | Con incidencia |
| `d77tnb4bkmj3e366msrzllnwsi2t5e54e4yqh7zm7y5hlfwugnwzswad.onion` | Booba Storage | Inactivo desde 2026-10-14 |

**Cuatro servicios, tres funciones, y el actor las etiqueta él mismo.** Sitio de filtración, sala de negociación, y almacenamiento por duplicado — con el almacén original caído en octubre y uno nuevo activo.

Esto tiene tres lecturas operativas:

**Primera, y es la que decide la clasificación.** El criterio más discriminante del triaje de `CTI-2026-042` `Anexo D` es *cómo contacta la víctima*: si hay portal, hay operación; si sólo hay correo, puede ser una herramienta usada por cualquiera. Aquí hay un servicio dedicado y etiquetado como sala de conversación. **Es operación.**

**Segunda: el almacén separado explica el volumen.** Un perfil que declara 50 a 70 GB por caso y 129 casos implica del orden de varios terabytes. Servir eso desde el mismo servicio que el sitio de filtración lo haría inutilizable; separarlo es la decisión de ingeniería esperable, y el hecho de que el primer almacén cayera y apareciera otro sugiere que **el almacenamiento es su restricción operativa**, no la publicación.

**Tercera: la distribución de entradas por sitio no coincide con la función declarada.** El sitio de filtración sirvió 73 entradas, el almacén activo 45 y el almacén caído 11. Que un almacén sirva entradas de catálogo indica que **el límite entre publicar y almacenar es más borroso de lo que los títulos sugieren**, o que el raspador sigue enlaces entre ellos. No se interpreta más allá.

## O-4. Las revisiones: el más editado del lote

Cuarenta y cinco de 129 entradas (35 %) llevan marca de revisión, frente al 16,3 % de media en el semestre. En el conjunto del semestre sólo `nightspire` (66 %), `Orova` (77 %), `metaencryptor` (100 %), `m3rx` (86 %), `anubis` (79 %), `Dark Project` (76 %), `spacebears` (78 %) y `titan` (86 %) superan esa proporción, y varios de ellos son sospechosos de artefacto precisamente por ser demasiado altos.

**Qué no se puede concluir.** `CTI-2026-054` dejó abierta la brecha `G-4`: no se sabe si el campo de revisión registra cambios sustantivos o también cambios triviales de la página servida. Con un 100 % en `metaencryptor` la sospecha de artefacto es seria. **Por eso `KJ-4` lleva confianza alta para la medición y baja para la interpretación.**

**Qué sí se puede hacer con ello.** Si las revisiones son sustantivas, la consecuencia práctica es directa y barata: **comprobar una vez no basta**. Una organización que busque su dominio en este catálogo y no lo encuentre, o lo encuentre con un contenido determinado, debería repetir la comprobación, porque un tercio de las entradas cambia después de publicarse. El coste de repetir es el mismo que el de la primera vez: minutos.

Y hay un dato contiguo que apoya la lectura sustantiva: `CTI-2026-054` `§E-3` documentó que las revisiones de título de otros actores son desenmascaramientos de víctima —`AuditTeam` reveló cuatro nombres en veintisiete segundos— o adiciones de cardinalidad —`Vortex` convirtió `700+ GB` en `20,90 GB`—. Este actor tiene **un solo cambio de título registrado**, de modo que sus cuarenta y cinco revisiones no son desenmascaramientos: son cambios en otra parte de la entrada.

## O-5. Lo que el perfil declara, y el único control que justifica

| Elemento declarado | Qué permite |
|---|---|
| Credenciales de programas de sustracción de información como acceso | **El único con valor preventivo**: rotación de credenciales de la organización aparecidas en filtraciones públicas |
| Sin programa de afiliados | **Consistente con lo medido** (`O-6` `H-3`), pero no genera acción |
| 50 a 70 GB por caso | Coherente con el almacén separado de `O-3`. **Alerta genérica por volumen de salida** |
| Movimiento lateral y recolección masiva | Genérico, sin indicadores |
| Anuncios por Telegram | **No verificado.** Si existiera el canal, sería una fuente de colección (`I-5`) |

**Un solo control, y no es nuevo.** La rotación preventiva de credenciales de la organización que aparezcan en filtraciones públicas es exactamente la recomendación a la que llegó `CTI-2026-051` `§X-2.3` por otra vía, y con la misma salvedad: **el proveedor no afirma que ése fuera el vector en ningún caso concreto**, de modo que la medida se justifica por sí misma y no por este actor.

**No se emite nivel técnico** en este expediente. No hay hash, ni extensión declarada, ni nombre de nota, ni dirección de contacto: nada que un sistema de detección pueda consumir. Emitir una sección técnica con el contenido de esta tabla daría a una ficha de proveedor sin referencias la apariencia de inteligencia técnica, y es la decisión que `CTI-2026-048` estableció para la serie.

## O-6. Hipótesis y pre-mortem

**H-1.** *La concentración en sanidad y administración es selección deliberada por propensión al pago.* **Posible** *(40–60 %)*. Apoyo: es la lógica conocida del sector. En contra: no hay ni un indicio directo.

**H-2.** *La concentración refleja un vector común —producto, proveedor o lote de credenciales— del sector.* **Posible** *(40–60 %)*. **Las dos hipótesis son las dos caras de `G-2`** y tienen consecuencias defensivas distintas: la primera no se puede mitigar, la segunda sí.

**H-3.** *No hay programa de afiliados.* **Probable** *(55–80 %)*. Apoyo: diecinueve días de actividad con mediana de seis y un solo pico de 36 — irregular, pero mucho menos que `krybit` o `Storm`. Es el mismo razonamiento de consistencia que `CTI-2026-058` `§O-4.1`.

**H-4.** *Las cuarenta y cinco revisiones son sustantivas.* **Posible** *(40–60 %)*. Sin resolver por `G-4` de `CTI-2026-054`.

**H-5.** *Las personas cuyos documentos aparecen son pacientes, administrados o empleados de las organizaciones víctimas, no objetivos propios.* **Muy probable** *(80–95 %)*. Apoyo: la victimología de `KJ-1` y el hecho de que los nombres de fichero aparecen junto a entradas de organización.

### Pre-mortem

*Si este informe se equivoca, será en `KJ-1`.* La concentración del 48 % se apoya en un campo de sector que es inferencia de un enriquecedor automático con cobertura del 74 %. `CTI-2026-056` `§E-2` documentó que ese mismo enriquecedor **inventa víctimas cuando no tiene datos**, y asigna sector con confianza alta a títulos que son nombres de fichero. Aquí la mayoría de los títulos son organizaciones, lo que hace la inferencia mucho más fiable, pero **no se verificó ni una de las 39 entradas sanitarias contra la organización**. Es `I-1`, y es el requisito más importante del expediente.

*El segundo modo de fallo es `KJ-4`.* Si el campo de revisión es un artefacto del raspador, el 35 % no dice nada del actor y la recomendación de volver a comprobar pierde su fundamento — aunque sigue siendo barata y prudente por otros motivos.

---

## 14. Brechas de inteligencia y requisitos de colección

**G-1. Ninguna de las 39 entradas sanitarias está verificada contra la organización**, y el sector es enriquecimiento derivado.
→ **I-1.** Verificar diez de las 39 por dominio y por existencia de la organización en el sector declarado. **Disparador:** inmediato; sostiene `KJ-1`, el juicio principal.

**G-2. No sabemos si la concentración es selección o vector común.** Decide si la exposición de una organización sanitaria depende de su sector —no mitigable— o de un producto concreto —mitigable—.
→ **I-2.** Comprobar si las 62 entradas de sanidad y administración comparten producto de gestión, proveedor de servicios o geografía fina. **Es la pregunta de más valor del expediente.**

**G-3. No sabemos cuántas entradas con datos de persona física hay ni de qué organizaciones**, y no se investigó por la razón de `§3.3`.
→ **I-3.** Si una organización de este catálogo lo solicita, la comprobación sobre su propio caso es inmediata y no requiere catalogar datos ajenos. **Es la única vía que este informe considera aceptable.**

**G-4. No sabemos si el campo de revisión registra cambios sustantivos.** Heredada de `CTI-2026-054` `G-4`.
→ **I-4.** Comparar contenido antes y después en una muestra de diez entradas revisadas.

**G-5. El canal de Telegram declarado no está verificado.** Si existe, es una fuente de colección directa sobre el actor.
→ **I-5.** Buscar el canal. **Disparador:** antes de la próxima revisión del expediente.

**G-6. No hay ni un indicador técnico.** Es la razón por la que no se emite nivel técnico.
→ **I-6.** Informe de incidente de una víctima, o muestra en repositorio público.

---

# ANEXOS

## Anexo A — Indicadores

### A.1 — Infraestructura

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| domain | `7t3zi3e7ki6iseun77ofqtr6wmbpgnpc2ada6gstcxp54lw6q2zb7jad.onion` | **Sitio de filtración, activo.** Sirvió 73 de las 129 entradas | Alta | 90 días | Vigilancia |
| domain | `culappkcuogv2omb37253e236mvmsfzvl4yw3p3incyzeoixhc6ocxqd.onion` | **«Booba Storage», activo.** Sirvió 45 entradas | Alta | 90 días | Vigilancia |
| domain | `eazk7las3xsvsyxgww3jgzammqjevso2ydnmlopdhl3u2muyrmmilrqd.onion` | **«Booba Chat»: la sala de negociación.** Con incidencia al 2026-11-19 | Alta | 90 días | Vigilancia |
| domain | `d77tnb4bkmj3e366msrzllnwsi2t5e54e4yqh7zm7y5hlfwugnwzswad.onion` | «Booba Storage» original. **Inactivo desde 2026-10-14**, sustituido | Alta como registro | 90 días | Análisis |
| pattern | **Infraestructura separada y etiquetada en filtración, negociación y almacén** | **Responde afirmativamente al criterio 1 del triaje** de `CTI-2026-042`: hay portal, luego **operación y no herramienta** (`O-3`) | Alta | 90 días | Clasificación |
| artefacto | **Sustitución del almacén en octubre con el resto de la infraestructura intacta** | **El almacenamiento es su restricción operativa**, no la publicación (`O-3`) | Moderada | 90 días | Análisis |

### A.2 — Patrones del catálogo

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| pattern | **Entrada cuyo título es el nombre de un documento de identidad de una persona física** | `KJ-2`, `E-3`. **4 de 129 entradas son nombres de fichero y varias son documentos nominales.** Los títulos **no se reproducen** (`§3.3`) | **Alta como observación** | 90 días | **Notificación a afectados como hecho, no como precaución** |
| pattern | **35 % de las entradas revisadas después de publicadas** | `KJ-4`. Frente al 16,3 % del semestre. **Comprobar una vez no basta** | Alta para la medición, **baja para la interpretación** | 90 días | **Repetir la comprobación** |
| pattern | **Un solo cambio de título en 129 entradas** | A diferencia de `AuditTeam` o `Vortex`, **este actor no desenmascara progresivamente** (`O-4`) | Alta | 90 días | Análisis |
| pattern | **Entrada con captura y dominio pero sin muestra de ficheros** | Niveles 3 y 4 de la escala de `CTI-2026-048`. **La captura engaña; el dominio permite comprobar** | Alta | 90 días | Comprobación por la víctima |
| pattern | **Credencial de la organización aparecida en filtración pública previa** | Vector declarado, **no corroborado**. El único control preventivo del expediente, y es genérico (`O-5`) | **Baja como atribución**, moderada como control | Sin caducidad | **Rotación preventiva** |
| pattern | **Salida de datos del orden de 50 a 70 GB** | Volumen declarado por el proveedor, coherente con el almacén separado | Moderada como control | Sin caducidad | Alerta genérica |

### A.3 — Victimología y decisiones de higiene

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| cartera | **39 sanidad + 23 administración = 48 % de 129** | **La concentración sectorial más alta del lote** (`KJ-1`) | Alta como recuento, **moderada como atribución** | 90 días | **Comprobación si opera en esos sectores** |
| cartera | **56 % con educación incluida** | Servicios esenciales y públicos | Alta como recuento | 90 días | Medición |
| cartera | **72 de 129 estadounidenses (56 %) · 14 países** | La segunda dispersión más estrecha del lote | Alta como recuento | 90 días | Medición |
| cartera | **3 entradas latinoamericanas (2,3 %) · 0 chilenas · 2 españolas** | `KJ-6`. **Vigilancia, no prioridad** | Moderada | 90 días | **No reasignar prioridad chilena** |
| cartera | **Nuevo contemporáneo verificado: retraso mediano 0,0 días** | Uno de los **14 de 68** que superan la prueba de `CTI-2026-054` (`KJ-3`) | Alta | Histórico | Clasificación |
| cartera | **Activo el día de emisión, 2026-11-19** | 19 días de actividad en 136 | Alta | **Reevaluar en 30 días** | Vigilancia |
| cartera | **No se reproduce ningún nombre de víctima, dominio, persona ni título de documento personal** | Regla de `CTI-2026-049`, **reforzada aquí porque los afectados no son la víctima corporativa** (`§3.3`) | — | — | **No ingerir** |

## Anexo B — Fuentes y valoración

| # | Fuente | Grado | Qué aportó | Salvedad |
|---|---|---|---|---|
| 1 | API de cti.fyi, entradas y ficha de grupo, 2026-11-19 | **Medición propia** sobre datos de proveedor | Las 129 entradas, los 4 sitios, la victimología, las revisiones | Evaluada en `CTI-2026-054`. **Sector y país son enriquecimiento derivado** con 74 % de cobertura |
| 2 | Ficha de perfil del grupo, misma fuente | **Proveedor, con indicio de redacción sintética** | El vector declarado, el volumen de 50-70 GB, la ausencia de afiliados, el canal de Telegram | **No corroborada en ningún punto** |
| 3 | `CTI-2026-054` §E-1 y §E-3 | Propio | **El método que verifica la novedad de `KJ-3`**, y el contexto de las revisiones de título de `O-4` | Emitido el mismo día |
| 4 | `CTI-2026-049` | Propio | **La regla de higiene de `§3.3`**, que es la decisión principal de este expediente | — |
| 5 | `CTI-2026-048` Anexo D · `CTI-2026-042` Anexo D | Propio | La escala de prueba de `O-2` y el triaje de `O-3` | — |
| 6 | `CTI-2026-051` §X-2.3 · `CTI-2026-015` | Propio | El control de credenciales de `O-5` y el contexto chileno de `E-4` | — |

## Anexo C — Léxico de probabilidad y confianza

ICD 203. **Casi con certeza** ≥99 % · **muy probable** 80–95 % · **probable** 55–80 % · **posible** 40–60 % · **improbable** 20–45 % · **muy improbable** 5–20 %. La **confianza** califica la base de prueba. Aquí: alta para los recuentos y para la verificación de novedad; **moderada para la atribución sectorial**, que es el juicio principal y descansa en enriquecimiento derivado; **baja para la interpretación de las revisiones** y para todo elemento del perfil del proveedor.

## Anexo D — Qué hacer cuando el catálogo de un actor incluye datos de personas físicas

Procedimiento para el analista, y es una ampliación del `Anexo D` de `CTI-2026-049` al caso en que los afectados **no son la víctima corporativa**.

**Paso 1 — Distinguir de quién son los datos.** No es lo mismo el titular de la empresa atacada —el caso de `CTI-2026-049`— que un paciente, un administrado o un empleado. En el primer caso la persona tiene relación con la decisión de seguridad; en el segundo, ninguna. **El segundo caso exige más cautela, no menos**, aunque el dato sea aparentemente menos sensible.

**Paso 2 — Documentar el patrón y no el dato.** Que el actor publica documentos nominales es el hallazgo; **cuáles son, no lo es**. Un informe de difusión libre que reproduzca un nombre de documento de identidad añade una exposición permanente sobre alguien ya expuesto.

**Paso 3 — No cuantificar con precisión si cuantificar exige catalogar.** Es una renuncia real: «varias de cuatro entradas» es menos informativo que un recuento exacto por tipo de documento. Pero el recuento exacto exige leer y clasificar datos de identidad ajenos, y publicarlo los reexpone. **Se renuncia a la precisión y se dice que se renuncia.**

**Paso 4 — Dar a la víctima la vía de comprobación, no el resultado.** El `Anexo F` permite a cualquiera con acceso a la fuente reproducir la observación sobre **su propio caso**. Eso conserva la utilidad operativa sin que el informe sea el vehículo de la exposición.

**Paso 5 — Y decir qué cambia para la notificación**, que es la única consecuencia que de verdad importa a los afectados. Si el sitio publica nombres de ficheros nominales, **la exposición de esa persona ya es pública y comprobable por cualquiera**: la notificación deja de ser una precaución ante un riesgo y pasa a ser la comunicación de un hecho consumado. El plazo y el tono de la notificación cambian en consecuencia.

> **El paso que distingue este método del de `CTI-2026-049` es el primero.** Allí la pregunta era si reproducir datos del dueño de la empresa; aquí es si reproducir datos de terceros que no tenían ninguna relación con la decisión. **La respuesta es más clara y la tentación es mayor**, porque un nombre en una tarjeta de identificación parece menos sensible que una declaración fiscal — y no lo es, porque su dueño no eligió nada.

## Anexo E — Marcos de referencia empleados

ICD 203. Escala de Almirantazgo con los grados propios de la cartera. TLP 2.0 y PAP. Triaje de actor nuevo de `CTI-2026-042` `Anexo D`, con el criterio de contacto como discriminante. Escala de prueba de ocho niveles de `CTI-2026-048` `Anexo D`. Método de verificación de novedad de `CTI-2026-054` `Anexo D`, correctivo 1. Reglas de higiene de datos personales de `CTI-2026-049` `Anexo D`, ampliadas en el `Anexo D` de este informe. **No se emite mapa ATT&CK ni nivel técnico**, por la razón de `O-5`.

## Anexo F — Paquete legible por máquina

| Medición | Procedimiento |
|---|---|
| Entradas | `GET /api/v1/posts?group=Booba%20Project&since=2026-05-19&limit=500` |
| Infraestructura | `GET /api/v1/groups/Booba%20Project` → `locations[]` con `title` y `site_status` |
| Concentración sectorial | Agrupar `enriched_metadata.industry_sector` → Sanidad 39, Administración 23, de 96 con sector |
| Revisiones | Contar registros con campo `updated` no vacío → 45 |
| Verificación de novedad | Mediana de `discovered − published` sobre las 80 con ambas fechas → **0,0 días** |
| Entradas con nombre de fichero | Expresión regular de extensión sobre `post_title`, como en `CTI-2026-056` `Anexo F` → 4 |

**Advertencia sobre la última fila.** El procedimiento devuelve títulos que contienen datos de identidad de personas concretas. **Quien lo ejecute hereda la decisión de `§3.3`**: documentar el patrón y no difundir los títulos. Si se ejecuta sobre el propio dominio para comprobar la exposición de la propia organización, no hay problema de esta clase.

## Anexo G — Control de cambios

| Versión | Fecha | Qué cambió | Qué juicio se movió |
|---|---|---|---|
| 1.0 | 2026-11-19 | Emisión inicial. Incluye la concentración sectorial más alta del lote (`KJ-1`), **la presencia de documentos de identidad de personas físicas en el catálogo y la decisión de no reproducirlos** (`KJ-2`, `§3.3`, `Anexo D`), la verificación de novedad por el método de `CTI-2026-054` (`KJ-3`), la proporción de revisiones más alta del lote (`KJ-4`) y la infraestructura separada por función (`KJ-5`). **No se emite nivel técnico**, y se explica por qué | — |

## Anexo H — Realimentación del consumidor

Este informe se corrige si se recibe: verificación de cualquiera de las 39 entradas sanitarias contra la organización, que elevaría `KJ-1` a confianza alta (`I-1`); un factor común entre las 62 entradas de sanidad y administración, que resolvería `G-2` y convertiría una concentración no mitigable en un vector mitigable; la comparación antes y después de entradas revisadas, que resolvería `KJ-4` (`I-4`); el canal de Telegram declarado, que abriría una vía de colección directa (`I-5`); o una víctima chilena, que invalidaría `KJ-6`.

El requisito más importante es **`I-1`**, porque `KJ-1` es el juicio principal, es el que una organización sanitaria usará para decidir, y descansa sobre un campo que un enriquecedor automático rellena por inferencia y que ya se ha demostrado capaz de inventar víctimas en otro expediente de este mismo lote.
