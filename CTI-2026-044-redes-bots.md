---
tlp: "TLP:CLEAR"
pap: "PAP:WHITE"
id: "CTI-2026-044"
version: "1.3"
tipo: "Perfil de ecosistema"
foco_regional: "Brasil · Chile · Latinoamérica"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "Redes de bots de DDoS y de proxy residencial · 33 familias"
fecha: "2026-11-19"
caduca: "2027-01-19"
autor: "Célula CTI"
distribucion: "Elaborado con fuentes abiertas y con medición propia sobre una interfaz pública de consulta de telemetría. No contiene telemetría de la organización emisora ni datos de terceros. Difusión libre, conservando la atribución de las fuentes y las salvedades metodológicas de §3. Se mantiene PAP:WHITE para el feed BGP descrito en X-1 y X-2, que es de consumo público y cuyo propósito es precisamente el bloqueo; pero los prefijos OBJETIVO del Anexo A.4 llevan tipo artefacto y NO deben bloquearse bajo ninguna circunstancia: son víctimas, no infraestructura adversaria. A partir de la versión 1.3 el informe contiene además, en A.9, tres direcciones cuya acción permitida es SÓLO VIGILANCIA y expresamente NO bloqueo: una sola fuente las declara mando y control y cuatro fuentes independientes no tienen nada contra ellas (O-3.7). Quien ingiera A.9 como lista de bloqueo estará bloqueando por la palabra de un solo tercero.
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-044
## Redes de bots activas: 33 familias, y el 85 % de la infraestructura pertenece a las siete que nunca lanzan un ataque
### Medición propia sobre telemetría en vivo, y un feed BGP defensivo operado desde Chile que ya tiene 176 pares

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-044` |
| Versión | **1.3 — 2026-11-22** *(emisión inicial 1.0 — 2026-11-19)* |
| Clasificación | `TLP:CLEAR` · `PAP:WHITE` *(con una excepción expresa: ver `A.4`)* |
| Tipo | Evaluación estratégica de ecosistema + medición propia + evaluación de fuente + método de colección |
| Objeto | **No es un perfil de actor.** Es el ecosistema de 33 familias de redes de bots en seguimiento activo, la estructura económica que las separa en dos negocios distintos, y la fuente que permite medirlas |
| Foco regional | **Brasil** como objetivo dominante (80,2 % del flujo medido) · **Chile** como origen de la capacidad defensiva y como alojamiento residual de infraestructura adversaria |
| Horizonte | Estratégico 6–18 meses · táctico días |
| Caducidad | **2027-01-19 (60 días, la más corta de la cartera).** Deliberado: este informe descansa en una medición de un sistema vivo, y sus proporciones envejecen en semanas. `G-2` explica por qué |
| Origen de los datos | **Medición propia** sobre la interfaz pública de consulta de `botnet.cl` (573 direcciones de mando y control, 2.500 eventos de ataque en una ventana de 97 minutos, 33 familias consultadas una a una, contadores acumulados verificados), **más seis fuentes externas independientes** para corroboración |
| Paquete legible por máquina | Las tablas `cti:ioc` del Anexo A alimentan `ioc_index.csv`. **Advertencia de higiene central de este informe, y es la inversa de la de `CTI-2026-040`:** las direcciones de mando y control de `A.2` y `A.3` llevan tipo `ipv4` y **sí** entran en los agregados planos, porque son infraestructura adversaria confirmada por la fuente; pero **los prefijos y los ASN objetivo de `A.4` llevan tipo `artefacto` y `asn` precisamente para que no entren**, porque son **redes víctima de operadores brasileños legítimos**. Una ingesta ingenua de esta fuente bloquearía a los atacados |
| Autor | Célula CTI |

<!-- cti:note type="warn" -->

> ⚠ **Lea esto antes de usar cualquier dato de este informe.** Este expediente
> mide un **sistema vivo** a través de la interfaz de consulta de un tercero.
> Eso le da una virtud que la cartera no tenía —datos primarios propios, no
> relato de proveedor— y tres defectos que no se pueden eliminar:
>
> 1. **Todo lo que medimos lo medimos a través de los ojos de otro.** No
>    tenemos sensores. Si `botnet.cl` no ve una familia, para este informe esa
>    familia no existe. Las 33 familias son **las 33 que esa fuente sigue**, no
>    las que hay.
> 2. **Las proporciones son de una ventana corta.** El flujo en vivo que
>    sostiene `KJ-1` y `KJ-5` son **97 minutos del 19 de noviembre de 2026**.
>    Una ventana de 97 minutos no es una medida del año. Se declara en cada
>    cifra y se trata en `G-2`.
> 3. **Y una de las conclusiones más llamativas puede ser un artefacto de
>    clasificación y no un hecho del mundo.** `KJ-9` —cero solapamiento de
>    infraestructura entre 33 familias— tiene dos lecturas incompatibles y
>    **este informe no puede decidir entre ellas**. Está escrito como pregunta,
>    no como hallazgo.

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** **Los objetivos están en la región y la infraestructura que los ataca no.** En una ventana en vivo de 97 minutos del 19-11-2026 (2.500 eventos únicos, medición propia), **el 80,2 % de los ataques observados tuvo por objetivo redes brasileñas** —2.006 de 2.500— y el resto se repartió entre Estados Unidos (9,4 %), China (6,9 %) y Qatar (1,8 %). Pero de las **573 direcciones de mando y control** que la fuente publicaba en el mismo momento, **sólo 12 están en Latinoamérica: el 2,1 %** —once en Brasil y una en Chile—, frente al 56,4 % en Estados Unidos, el 13,6 % en Singapur y el 9,4 % en Países Bajos. Valoramos **casi con certeza** *(≥99 %)* que esta asimetría sea real y no un artefacto de la fuente, porque es consistente en los dos conjuntos de datos, medidos por vías distintas. **Confianza: alta para la asimetría; moderada para las proporciones exactas**, que dependen de la ventana — **aunque en la versión 1.1 una segunda ventana independiente las sostuvo**: 572 eventos entre las 15:11 y las 15:31 dieron **Brasil al 76,9 %**, a 3,3 puntos de la primera medición (§O-3.5). *Consecuencia práctica:* **bloquear por geografía no sirve de nada aquí**, y el nodo infectado que genera el tráfico no está donde está el C2 ni donde está la víctima.

**KJ-2.** **El hallazgo central, y no lo esperábamos: el 85 % de la infraestructura de mando y control pertenece a las siete familias que no lanzan un solo ataque.** De las 572 direcciones atribuidas a una familia, **487 son de `CXFJ` (215), `Aigogo` (134), `LinkFog` (46), `SZJL` (46), `Hotota` (24), `Aisuru-Proxy` (13) y `Titan` (9)** — todas ellas **módulos de proxy residencial**, casi todos para Android, y **ninguna con un solo evento de ataque registrado**. Las familias ruidosas apenas tienen infraestructura: `Cereal2`, con 395.887 eventos acumulados, tiene **cero** direcciones vivas; `Liso`, la más activa de todas, tiene **diecisiete**. Valoramos **muy probable** *(80–95 %)* que esto refleje una diferencia estructural de modelo de negocio y no un sesgo de la colección. **Confianza: alta, y reforzada por una comprobación posterior que no esperábamos poder hacer:** los dos negocios **no comparten ni un bloque de direcciones**. De los 206 bloques `/24` que aloja esta infraestructura, **144 alojan familias de proxy, 62 alojan familias de DDoS y ninguno aloja las dos clases**; y a nivel de sistema autónomo, de los 57 ASN implicados **sólo 4 son usados por ambas**. **Dos huellas de alojamiento físicamente disjuntas son difíciles de explicar como un artefacto de etiquetado** (§O-3.4). **Recomputado el 22-11-2026, el reparto no sólo se mantiene: se acentúa** *(añadido en la versión 1.3)*. Sobre las 625 direcciones de hoy, **556 —el 89,0 %— pertenecen a las siete familias de proxy** frente al 85 % del 19-11, y el crecimiento viene casi entero de la migración de `SZJL` (`KJ-11`, `O-3.6`). **Y la separación se verificó además por una vía que no pasa por el clasificador de la fuente** (`KJ-12`, `O-3.7`), que es lo que rebaja `H-2`. *La lectura que importa:* **el recuento de mando y control no mide agresividad, mide modelo de negocio.** Un proxy residencial vende disponibilidad y necesita infraestructura estable y numerosa; una red de bots de DDoS necesita un punto de control desechable. **Quien priorice por número de direcciones priorizará exactamente al revés de lo que cree.**

**KJ-3.** **Tres familias de treinta y tres concentran el 90 % de toda la actividad registrada.** Los contadores acumulados —que verificamos que son recuentos reales de eventos y no identificadores con huecos (§O-3.2)— dan `Liso` 444.692, `Cereal2` 395.887 y `Potassium` 304.258: **1.144.837 eventos de un total aproximado de 1.269.333**, el 90,2 %. Las treinta familias restantes se reparten el 9,8 %, y **dieciséis de ellas no superan los 200 eventos en toda su historia registrada**. Valoramos **casi con certeza** *(≥99 %)* la concentración. **Confianza: alta.** *Consecuencia:* un programa de defensa que trate las 33 familias con igual atención gastará el 90 % de su esfuerzo en el 10 % del problema. **Es el mismo error de encuadre que `CTI-2026-042` encontró en un requisito de extorsión**, y aquí aparece en una lista de proveedor.

**KJ-4.** **El objetivo no es «Brasil»: son los proveedores de fibra pequeños y regionales de Brasil, y eso está corroborado por una fuente independiente nueve meses antes de nuestra medición.** En nuestra ventana, los veinte ASN más golpeados incluyen diecisiete operadores brasileños regionales —`Halver LTDA` (`AS274564`) con 550 eventos, `EGR NET`, `Speednet`, `GD NET`, `INETVIP`, `PARAOPEBANET`, `Fullnet`, `GOX`, `BHNET`, `YAS`, `Livenet`, `UNIVERSO FIBER`— y **ningún operador nacional brasileño**. A10 Networks midió lo mismo en febrero de 2026: **17.527 ataques en una semana en Brasil con cerca del 99 % concentrado en cinco ISP regionales de fibra**, dejando intactos a los grandes. Valoramos **muy probable** *(80–95 %)* que el patrón sea estable y de nueve meses de duración como mínimo. **Confianza: alta** — dos mediciones independientes, con métodos distintos, coinciden. *Por qué pasa:* `E-2.1` sostiene que es una elección de **eficiencia**, no de ideología.

**KJ-5.** **La forma del ataque derrota a la mitigación que funciona en escala humana: la mediana de duración es de cinco segundos.** De los 2.500 eventos medidos, **1.979 duraron 5 segundos** y 505 duraron 60; y el 23,2 % de los segundos observados contienen **dos o más ataques simultáneos**, con un máximo de **once eventos en un mismo segundo contra seis prefijos distintos del mismo operador**. A10 describió el mismo patrón en marzo de 2026 sobre 498.163 ataques —ráfagas cortas y repetidas contra múltiples subredes— y lo atribuyó a un servicio de alquiler o a un módulo que ejecuta un bucle configurado. Valoramos **muy probable** *(80–95 %)* que la ráfaga corta sea el modo normal de operación y no una excepción. **Confianza: alta, y reforzada en la versión 1.1**: la ventana independiente dio los pulsos de cinco segundos en el **82,4 %** de los eventos de `Liso`, frente al 79,2 % de la primera (§O-3.5). *Consecuencia operativa, y es la más importante del informe para un operador:* **un procedimiento que exige que una persona vea una alerta, confirme y active el desvío nunca llegará a tiempo.** Cinco segundos es menos que el tiempo de carga de un panel.

**KJ-6.** **Existe un activo defensivo regional, gratuito, ya desplegado y operado desde Chile, y nuestra medición actualiza la cifra que su operador publica.** `botnet.cl` ofrece un **feed BGP de blackhole** que anuncia una ruta `/32` por cada dirección de mando y control, con la comunidad `65535:666` (RFC 7999) y comunidades informativas de familia, antigüedad y fuente; con dos puntos de presencia —Chile y São Paulo—, sesión eBGP multisalto de sólo conexión, y plantillas de configuración publicadas para MikroTik, Juniper, Huawei y Cisco. En una charla de **NANOG 98** atribuida a Rodrigo Peña, de Bitred Group SpA, se afirmaba **«más de 100 ISP suscritos en dos meses»**; la interfaz pública declaraba el 19-11-2026 **176 pares establecidos distintos** en siete países, **71,6 % brasileños, 12,5 % chilenos y 11,4 % argentinos**. Valoramos **casi con certeza** *(≥99 %)* que el servicio exista y funcione como se describe, y **probable** *(55–80 %)* que la cifra de 176 sea de pares reales y no de intentos. **Confianza: alta para la existencia; moderada para la cifra.** *Y la observación incómoda:* **Brasil es a la vez el más atacado y el más defendido**; Chile, con 22 pares, está defendido muy por encima de su exposición medida.

**KJ-7.** **La infraestructura adversaria está concentrada en muy pocos proveedores de alojamiento, y eso la hace atacable por una vía que no es técnica.** De las 573 direcciones, **147 —el 25,7 %— están en un solo sistema autónomo**: `AS62610`, Zenlayer. Los cinco primeros concentran **322, el 56,2 %**: Zenlayer (147), GoCodeIT (58), Alibaba US Technology (45), Tube-Hosting (42) y CDS Global Cloud (30). Y hay **58 ASN distintos en total**, lo que significa que la mitad de todo el problema cabe en cinco interlocutores. Valoramos **casi con certeza** *(≥99 %)* la concentración medida. **Confianza: alta.** *Consecuencia:* la palanca de mayor rendimiento no es un bloqueo, es **una notificación de abuso bien documentada a cinco proveedores**; y, para quien tenga capacidad de política, la misma concentración que `CTI-2026-018` encontró en el abuso de dominios. **Remedición del 22-11-2026, y la estructura se mantiene pero los nombres cambian** *(añadido en la versión 1.3)*: sobre 625 direcciones, los cinco primeros son ahora Zenlayer (163), **`AS150436` Byteplus Pte. Ltd. (92), que el 19-11 no aparecía en el conjunto**, GoCodeIT (63), Tube-Hosting (43) y **DigitalOcean (32), que entra desde el eje de DDoS y no desde el de proxy** — **393 direcciones, el 62,9 %**, casi siete puntos más concentrado que el 56,2 % inicial. **Alibaba US Technology cae de 45 a 29** y sale de los cinco primeros. **La concentración no se ha disuelto: se ha reordenado en tres días**, y `O-3.6` explica por qué, que es lo que hace a este juicio menos tranquilizador de lo que parece.

**KJ-8.** **`Cereal2` enmudeció el 30 de octubre de 2026 tras 395.887 eventos y se quedó sin infraestructura, y el contexto sugiere que fue intervención y no abandono.** Su último evento registrado es del **2026-10-30 a las 11:02 UTC**; hoy tiene **cero direcciones de mando y control** vivas en el feed. En el mismo período, Cloudflare asocia una **acción policial de principios de 2026 contra cuatro grandes redes de bots de internet de las cosas —Aisuru, KimWolf, JackSkid y Mossad—** a una caída de los ataques por encima de 1 Tbps de 805 en el segundo trimestre a 251 en el tercero. Y nuestra propia medición es consistente: **`Aisuru-DDoS` tiene sólo 792 eventos acumulados**, una cifra ridícula para la red de bots a la que se atribuye el récord mundial de 31,4 Tbps. Valoramos **aproximadamente igual de probable** *(40–60 %)* que el silencio de `Cereal2` sea consecuencia directa de una acción externa, frente a una migración de marca. **Confianza: baja** — es una correlación temporal y nada más, y se consigna así expresamente. *Y la advertencia de la cartera:* `CTI-2026-040` y `CTI-2026-042` documentan cuatro casos en que **la marca se apaga y la capacidad sigue**. **El silencio de una familia no es su final; es el momento de buscar a la sucesora.**

**KJ-9.** **Ninguna de las 572 direcciones es compartida por dos familias, pero doce bloques `/24` sí lo son — y esa diferencia de granularidad es el hallazgo.** A nivel de dirección, el solapamiento es **cero**, lo que es llamativo porque **la propia documentación de la fuente prevé el caso** —«una dirección asociada a varias familias lleva todas las comunidades de familia que correspondan»— y no ocurre nunca; eso deja abiertas dos lecturas, **(a)** compartimentación real o **(b)** un clasificador que asigna una sola familia por dirección, y **la ambigüedad a ese nivel sigue sin resolverse** (`G-1`). **Pero al subir a granularidad de bloque, la medida sí dice algo:** de 206 bloques `/24`, **doce (5,8 %) alojan más de una familia**, y el reparto no es aleatorio: **once de los doce están en un mismo sistema autónomo, `AS62610`**, y los doce enfrentan siempre familias **del mismo negocio**. Dos emparejamientos destacan: **`Hotota` y `LinkFog` comparten seis bloques distintos** —el vínculo más fuerte entre dos familias que este informe puede ofrecer—, y **`Aisuru-DDoS` y `Eclipse` comparten uno** (`141.98.10.0/24`). Valoramos **probable** *(55–80 %)* que la coincidencia repetida de `Hotota` y `LinkFog` en seis bloques indique **un operador o un proveedor de alojamiento común**, y **poco probable** *(20–45 %)* que sea casualidad de un proveedor grande. **Confianza: moderada.** *Y la consecuencia de método:* **el solapamiento a nivel de `/32` no existe, pero el de `/24` sí y es medible — de modo que la unidad de análisis correcta en esta fuente es el bloque, no la dirección.*** **Y una corrección de la versión 1.3 que afecta a la mitad de este juicio:** `Eclipse` **ya no tiene ninguna dirección viva** en la fuente, y `141.98.10.0/24` aloja hoy **cinco direcciones que son todas de `Aisuru-DDoS`**. El **único solapamiento entre dos familias de DDoS deja de ser observable**, de modo que la conjetura de §O-3.4 sobre `Eclipse` como herramienta o prueba del mismo entorno **pierde su base observacional**: se conserva por trazabilidad, se degrada a conjetura histórica y pasa a `G-12`. **El vínculo `Hotota`↔`LinkFog` en seis bloques, que es la parte fuerte de este juicio, no está afectado.**

**KJ-10.** **Y el hallazgo metodológico, que es el que se transfiere a otros expedientes: la interfaz de esta fuente tiene un comportamiento por omisión que produce una conclusión falsa, y lo tuvimos delante.** La consulta de eventos **sin parámetros** devuelve, en silencio y sin aviso, **sólo los de `Cereal2`** —una familia muda desde el 30 de octubre— con su histórico congelado. Nuestra primera recolección fueron 1.400 eventos que parecían el flujo general y eran todos de esa familia: habríamos concluido que **`Cereal2` es el 100 % de la actividad** y que **su objetivo principal es un proveedor de alojamiento estadounidense**, dos afirmaciones falsas. El error se detectó porque la portada mostraba a `Liso` atacando en ese mismo minuto y los datos decían otra cosa. Valoramos **casi con certeza** *(≥99 %)* el comportamiento, verificado con cuatro consultas de control (§O-2.2). **Confianza: alta** —es reproducible a voluntad contra la interfaz, y se reprodujo— *(declaración añadida en la versión 1.3: las versiones 1.0 a 1.2 omitían la confianza de este juicio)*. *La lección, que es la de `O-2.2` de `CTI-2026-037` aplicada a una fuente automatizada:* **cuando los datos forman una historia limpia, hay que preguntarse qué pregunta se ha hecho realmente**, y el `Anexo D` da los cinco controles que lo comprueban en diez minutos.

**KJ-11.** **`SZJL` no perdió infraestructura cuando su proveedor principal se vació: la trasladó entera a otro proveedor en un solo día, y eso mide lo que vale la palanca de `E-5.6`.** Entre el 19 y el 22 de noviembre de 2026, `AS45102` —Alibaba (US) Technology— **cayó de 45 a 29 direcciones**, y su bloque `43.117.72.0/24`, que `A.2` publica como el pivote de caza de mayor densidad del expediente, **cayó de 43 a 20: un 53 %**. La lectura cómoda era una notificación de abuso eficaz. **No lo es:** el 21-11-2026 aparecieron de golpe **92 direcciones en `AS150436`, Byteplus Pte. Ltd. (Singapur), todas con la misma fecha de primera observación**, repartidas en cuatro bloques y concentradas en dos —`101.47.51.0/24` con 69 y `101.47.50.0/24` con 21—, y **las 92 pertenecen a `SZJL`**. La familia pasó de 46 a 115 direcciones: **no se replegó, se multiplicó por 2,5 mientras abandonaba el proveedor anterior.** Valoramos **muy probable** *(80–95 %)* que se trate de una migración deliberada de alojamiento y no de dos hechos independientes, porque las 92 direcciones comparten familia, fecha de alta y dos bloques contiguos. **Confianza: alta** para la medición —es reproducible contra la fuente—, **moderada** para la causa, que no está documentada por nadie. *Consecuencia, y es incómoda para `E-5.6`:* **el tiempo de reconstitución de este operador es de un día y el coste de cambiar de proveedor es, para él, casi nulo.** Una notificación de abuso que tarda semanas en tramitarse compite contra un adversario que rehace su huella en veinticuatro horas. **La notificación sigue valiendo, pero su rendimiento hay que medirlo en direcciones retiradas y no en bloques vaciados**, porque un bloque vaciado puede significar que el operador se ha ido a otro sitio más grande. **Esto cumple el disparador `I-6` con el resultado contrario al que `I-6` esperaba.**

**KJ-12.** **La separación entre los dos negocios se sostiene por una segunda vía independiente que no pasa por el clasificador de la fuente: la huella de servicio observada desde fuera.** `KJ-2` apoyaba la separación en que los dos negocios no comparten ni un bloque `/24`, y `H-2` planteaba que todo podía ser un sesgo del clasificador de binarios de la fuente. **El 22-11-2026 se comprobó por una vía que no depende ni del clasificador ni del bloque:** se consultó la huella de puertos y de banderas de servicio de **27 direcciones en Shodan** —tres por familia, seis familias de proxy y tres de DDoS—. El resultado separa las dos clases limpiamente: **ninguna de las nueve direcciones de las tres familias de DDoS** (`Liso`, `Potassium`, `SixSayven`) **lleva la etiqueta `proxy` ni expone un reto de autenticación de proxy**, y todas presentan el perfil de un servidor corriente (22, 80, 443) o de un dispositivo doméstico (23, 554, 4567); mientras que **once de las dieciocho direcciones de familias de proxy sí llevan la etiqueta `proxy`**, y tres familias exponen además el patrón que las identifica: **un abanico de puertos consecutivos, cada uno respondiendo `407 Proxy Authentication Required` con un reino de autenticación propio** — `CXFJ` en 12337–12406 con reino `Proxy`, `Aigogo` en 10000–10xxx con reino `proxy`, `Titan` en 8888–51001 con reino `Restricted`. Valoramos **probable** *(55–80 %)* que la huella de servicio sea un discriminante utilizable de las dos clases, con la salvedad de que **27 direcciones de 625 son una muestra pequeña y elegida por conveniencia** (`G-12`). **Confianza: moderada.** *Lo que esto hace con `H-2`:* una etiqueta de Shodan y un reino de autenticación HTTP **no los produce el clasificador de binarios de `botnet.cl`**, de modo que la coincidencia entre dos medidas independientes **baja `H-2` de «posibilidad real» a «poco probable»**, y lo hace sin necesidad del correo al operador que `G-1` pedía. *Y la consecuencia de método, que es la que se transfiere:* **cuando una fuente única clasifica, la verificación no tiene que ser una segunda fuente de inteligencia: puede ser una medición directa de la infraestructura que la fuente nombra.**

---

## 2. Resumen ejecutivo

Hay un ecosistema de **33 familias de redes de bots** en seguimiento activo, y la primera cosa que hay que entender es que **no son 33 cosas del mismo tipo**. Se parten en dos negocios con economías opuestas.

El negocio **ruidoso** es la denegación de servicio. Son 26 familias, concentran el 90 % de su actividad en tres de ellas, atacan en ráfagas de cinco segundos y **apuntan abrumadoramente a proveedores de fibra pequeños de Brasil**. Su infraestructura de control es **mínima y desechable**: la familia más activa del conjunto mantiene diecisiete direcciones, y la segunda más activa de la historia del feed no mantiene ninguna.

El negocio **silencioso** es el proxy residencial. Son siete familias, casi todas módulos para Android, **no lanzan un solo ataque**, y entre ellas tienen **el 85 % de toda la infraestructura de mando y control del ecosistema**. Su alojamiento está concentrado en nubes grandes y reputadas —65 % Estados Unidos, 15 % Singapur— porque lo que venden es **disponibilidad**, y un proxy que no responde no se cobra. Un día antes de la emisión de este informe, HUMAN Security publicó que los módulos de proxy de la operación BADBOX 3.0 inscriben dispositivos comprometidos en **once redes de proxy residencial distintas** sin que el dueño lo sepa: nuestra medición es la vista de esa misma economía desde la capa de red.

La consecuencia de juntar las dos mitades es contraintuitiva y es el hallazgo del informe: **el número de direcciones de mando y control de una familia no dice nada sobre lo peligrosa que es.** Dice a qué se dedica.

Para la región, el cuadro tiene una **asimetría dura**: los objetivos están aquí y la infraestructura no. Ocho de cada diez ataques observados van contra redes brasileñas; dos de cada cien direcciones de control están en Latinoamérica. Y los atacados no son los operadores nacionales, sino los regionales de fibra —diecisiete nombres propios en nuestra lista de veinte—, lo que una medición independiente de A10 Networks ya había encontrado nueve meses antes con cerca del 99 % de los ataques de una semana concentrados en cinco de ellos. La razón más probable no es ideológica sino de **eficiencia**: un operador regional tiene objetivos valiosos para quien vende ataques por encargo, poca capacidad de absorción, y a menudo ningún acuerdo previo de desvío con su tránsito.

Frente a eso hay algo que la cartera no suele poder decir: **existe una capacidad defensiva regional, es gratuita, está desplegada y se opera desde Chile.** `botnet.cl` publica un feed BGP de agujero negro con las direcciones de mando y control, con comunidades que permiten filtrar por familia y por antigüedad, dos puntos de presencia y plantillas listas para cuatro fabricantes de enrutadores. Su operador afirmaba más de cien ISP suscritos en dos meses; nuestra medición del 19 de noviembre contó **176 pares establecidos**, con Brasil al 71,6 % y Chile al 12,5 %. Es decir: **el país más atacado es también el que más se ha suscrito**, y la defensa está siguiendo a la amenaza con un retardo medible.

Este informe aporta, además de la medición, dos cosas de método. La primera es una advertencia de higiene que invierte la de `CTI-2026-040`: aquí las direcciones de control **sí** son indicadores legítimos y entran en los agregados, pero **los prefijos objetivo no deben entrar jamás**, porque son redes de operadores brasileños legítimos que están siendo atacados. Una ingesta ingenua de esta fuente **bloquearía a las víctimas**. La segunda es el `Anexo D`: cinco controles para usar un canal de telemetría continua como fuente de inteligencia, escritos porque **la interfaz de esta fuente nos devolvió, en silencio, una respuesta a una pregunta que no habíamos hecho**, y estuvimos a punto de publicarla.

---

## 3. Alcance y limitaciones

### 3.1 Qué cubre este informe

El ecosistema de las 33 familias que `botnet.cl` sigue, su partición en dos modelos de negocio, la estructura geográfica de objetivos e infraestructura, la forma táctica del ataque, la evaluación de la fuente, y el consumo del feed BGP que ofrece. Cubre además, en el `Anexo D`, el método de colección que el expediente obligó a desarrollar.

### 3.2 Qué NO cubre, y conviene decirlo antes de que alguien lo busque

| Fuera de alcance | Por qué |
|---|---|
| **Un perfil completo de cada una de las 33 familias** | Sería el error que `CTI-2026-042` documentó: tratar como comparables objetos que no lo son. `O-1` las **clasifica**; `KJ-3` explica por qué 30 de ellas no merecen un expediente. **`Liso` sí lo merece, y lo tiene aparte en `CTI-2026-045`** |
| **Análisis de las muestras de malware** | No tenemos muestras. Todo lo que este informe dice sobre capacidades de cada familia procede de la matriz publicada por la fuente, que **declara haberla obtenido de ingeniería inversa de binarios** («catorce manejadores de inundación», «diecinueve métodos», «las opciones numéricas suministradas resuelven a 10»). Es una afirmación de la fuente que **no verificamos** |
| **La atribución de las familias a personas u organizaciones** | La fuente no la ofrece y no la construimos. La única atribución de este informe es la de **la fuente misma** (`O-2`) |
| **El récord de 31,4 Tbps de Aisuru** | Está documentado por terceros y se cita como contexto en `KJ-8`, pero **no lo medimos** y las fuentes discrepan incluso en el mes |
| **La operación BADBOX** | Se cita como corroboración externa del eje de proxy residencial (`E-3`). Es un expediente propio que esta cartera no tiene y que `G-5` pide |
| **La identidad de los nodos infectados** | El feed publica **mando y control**, no víctimas infectadas. No sabemos qué dispositivos componen estas redes salvo por lo que la matriz de familias indica (Android, MIPS, ARM) |

### 3.3 Limitaciones de la colección

<!-- cti:note type="warn" -->

> ⚠ **Seis limitaciones, y las dos primeras afectan a casi todas las cifras.**
>
> 1. **Fuente única para los datos primarios.** Las 573 direcciones, los 2.500
>    eventos, los contadores y la matriz de capacidades vienen **todos** de
>    `botnet.cl`. La corroboración externa existe y es buena (`B-3` a `B-6`),
>    pero corrobora **el fenómeno**, no nuestras cifras. Si la fuente clasifica
>    mal, clasificamos mal.
> 2. **Ventana de 97 minutos.** El flujo en vivo que sostiene las proporciones
>    de `KJ-1`, `KJ-4` y `KJ-5` es de un único tramo del 19-11-2026, entre las
>    13:33 y las 15:11 UTC. **No es una medida del día, ni del mes.** Un
>    muestreo longitudinal quedó lanzado al cierre de este informe y su
>    resultado es material para la versión 1.1 (`G-2`).
> 3. **Las columnas de país y de método por familia de `O-1` proceden de los
>    últimos 100 eventos de cada familia**, no de su historia. Para `Liso` o
>    `Potassium` eso son minutos; para `Ouroboros`, con cuatro eventos en toda
>    su vida registrada, es toda su historia. **Las dos cosas están en la misma
>    tabla y no son comparables**: la columna lleva aviso.
> 4. **No vemos el volumen del ataque, sólo su existencia.** La fuente publica
>    objetivo, método y duración; **no publica bits por segundo ni paquetes por
>    segundo**. Por tanto este informe **no puede decir nada sobre la magnitud**
>    de ningún ataque, y cualquier lectura de «intensidad» a partir del número
>    de eventos sería un error (`I-3` del pre-mortem).
> 5. **La matriz de capacidades es de la fuente y no la verificamos.** Que
>    `Manta` descargue y ejecute un minero, o que `KATARU` se propague por ADB,
>    son **afirmaciones de un tercero** sobre binarios que no hemos visto.
> 6. **Y una limitación de nuestra propia honestidad: casi publicamos una
>    conclusión falsa.** Está documentada en `O-2.2` en lugar de borrada,
>    porque es el aporte más reutilizable del expediente.

### 3.4 Qué aporta sobre lo que ya había

| Aporte | Dónde |
|---|---|
| **La partición del ecosistema en dos negocios con economías opuestas**, medida: 85 % de la infraestructura en manos de las familias que no atacan | `KJ-2`, `E-3` |
| **La asimetría objetivo/infraestructura cuantificada**: 80,2 % de ataques contra Brasil frente a 2,1 % de infraestructura en la región | `KJ-1`, `E-2` |
| **La concentración de actividad medida con contadores verificados**: 90,2 % en tres familias de 33 | `KJ-3`, `O-1` |
| **Verificación propia de una afirmación pública del operador de la fuente**: «más de 100 ISP» → 176 pares establecidos medidos | `KJ-6`, `O-2.1` |
| **La concentración del alojamiento adversario**: 25,7 % en un ASN, 56,2 % en cinco | `KJ-7`, `A.3` |
| **La separación física del alojamiento entre los dos negocios**: 0 de 206 bloques `/24` compartidos, 4 de 57 ASN | `KJ-2`, `O-3.4` |
| **Doce bloques `/24` compartidos entre familias**, con `Hotota` y `LinkFog` coincidiendo en seis | `KJ-9`, `O-3.4` |
| **El comportamiento por omisión de la interfaz que produce una conclusión falsa**, con los controles que lo detectan | `KJ-10`, `O-2.2`, `Anexo D` |
| **La advertencia de higiene inversa**: en esta fuente los objetivos son víctimas y no deben entrar en los agregados | `A.4`, `X-4` |
| **Un método de cinco controles para usar telemetría continua como fuente de inteligencia** | `Anexo D` |

### 3.5 Veredicto sobre lo que se pedía comprobar

<!-- cti:table highlight="CORROBORADO|NO SOSTENIDO|SIN RESOLVER|propio" -->

| # | Elemento | Veredicto | Base |
|---|---|---|---|
| 1 | Existen redes de bots activas con telemetría pública consultable | **CORROBORADO** | 33 familias, 573 direcciones y un flujo en vivo medido el 19-11-2026 |
| 2 | La región es objetivo de esta actividad | **CORROBORADO, y más de lo esperado** | 80,2 % de los ataques de la ventana contra Brasil. Pero **contra operadores regionales, no nacionales** (`KJ-4`) |
| 3 | La región aloja infraestructura de estas redes | **NO SOSTENIDO como fenómeno relevante** | 12 de 573 direcciones, el 2,1 %. Existe —once en Brasil, **una en Chile**— pero es residual (`A.3`) |
| 4 | El número de direcciones de control indica la peligrosidad de una familia | **NO SOSTENIDO, y es el hallazgo del informe** | Indica el **modelo de negocio**. Las siete familias con más infraestructura no atacan nunca (`KJ-2`) |
| 5 | Las 33 familias son objetos comparables que merecen atención similar | **NO SOSTENIDO** | 90,2 % de la actividad en tres; dieciséis no llegan a 200 eventos históricos (`KJ-3`, `O-1`) |
| 6 | Hay una capacidad defensiva regional aprovechable | **CORROBORADO** | Feed BGP con 176 pares, dos puntos de presencia y plantillas para cuatro fabricantes (`KJ-6`, `X-1`, `X-2`) |
| 7 | La mitigación manual es viable frente a esta amenaza | **NO SOSTENIDO** | Mediana de cinco segundos por ataque; 23,2 % de los segundos con ataques simultáneos (`KJ-5`) |
| 8 | Las familias comparten infraestructura entre sí | **DEPENDE DE LA GRANULARIDAD — hallazgo propio** | **Cero** a nivel de dirección (ambigüedad sin resolver, `G-1`); **doce bloques `/24` de 206 sí**, con `Hotota` y `LinkFog` en seis (`KJ-9`, `O-3.4`) |
| 11 | Los dos modelos de negocio son operaciones separadas o líneas de un mismo operador | **SEPARADAS, con confianza alta — hallazgo propio** | **Ni un bloque `/24` de 206 aloja las dos clases**, y sólo 4 ASN de 57 (`O-3.4`) |
| 9 | `Cereal2` sigue activa | **NO SOSTENIDO** | Muda desde el 30-10-2026 y sin infraestructura viva. La causa, **sin establecer** (`KJ-8`) |
| 10 | La afirmación pública del operador sobre la adopción del feed | **CORROBORADO Y ACTUALIZADO (verificación propia)** | «Más de 100 ISP en dos meses» → **176 pares establecidos** medidos el 19-11-2026 (`O-2.1`) |

---

# NIVEL ESTRATÉGICO
### Para: Consejo, CISO, Riesgo, Arquitectura de red · Horizonte: 6–18 meses

## E-1. Qué es este ecosistema, y por qué no es «el problema del DDoS»

<!-- cti:cards -->

| Rasgo del ecosistema | Qué significa para nosotros | Etiqueta |
|---|---|---|
| **Son dos negocios, no uno.** 26 familias venden interrupción; 7 venden ancho de banda residencial ajeno | Exigen dos defensas distintas y dos interlocutores distintos. La primera es un problema de capacidad de red; **la segunda es un problema de confianza en el origen del tráfico que llega a nuestros servicios** | `01 · dos negocios` |
| **La infraestructura de control está donde se puede pagar con tarjeta**, no donde está la víctima: 56 % Estados Unidos, 14 % Singapur, 9 % Países Bajos | El bloqueo geográfico no sirve. El pivote útil es **el proveedor de alojamiento**, y ahí la concentración es extrema (`KJ-7`) | `02 · geografía irrelevante` |
| **El ataque dura cinco segundos y se repite** | Toda la doctrina de «detectar, confirmar, desviar» está mal dimensionada. Lo que funciona es **automático y preacordado**, no humano y reactivo | `03 · escala temporal` |
| **El objetivo preferido es el proveedor regional pequeño** | Si somos uno, somos el objetivo preferente y no un daño colateral. Si dependemos de uno, **nuestra disponibilidad depende de la capacidad de absorción de un tercero que probablemente no tiene desvío preacordado** | `04 · victimología` |
| **Las marcas se apagan y la capacidad persiste** | `Cereal2` pasó de 395.887 eventos a cero infraestructura en tres semanas. Organizar la defensa por nombre de familia es construir sobre el activo más desechable del adversario | `05 · volatilidad de marca` |
| **Y la mitad del problema cabe en cinco interlocutores comerciales** | Es la única palanca de este informe que no es técnica, y probablemente la de mayor rendimiento por unidad de esfuerzo | `06 · palanca` |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `573` | Direcciones de mando y control publicadas el 19-11-2026 | En 58 ASN y 24 países |
| `487` | Las que pertenecen a familias que **nunca atacan** | El 85,1 % del total. **Es el hallazgo del informe** |
| `80,2 %` | Ataques de la ventana con objetivo en Brasil | 2.006 de 2.500 eventos |
| `2,1 %` | Direcciones de control alojadas en Latinoamérica | 12 de 573: once en Brasil, una en Chile |
| `90,2 %` | Actividad acumulada concentrada en tres familias | `Liso`, `Cereal2` y `Potassium`, de 33 |
| `25,7 %` | Direcciones de control en un solo sistema autónomo | `AS62610`. Los cinco primeros, el 56,2 % |
| `5 s` | Duración mediana de un ataque | 1.979 de 2.500 eventos. **Menos que cargar un panel** |
| `176` | Pares BGP establecidos del feed defensivo | 71,6 % Brasil · 12,5 % Chile · 11,4 % Argentina |
| `0` | Direcciones compartidas por dos familias, de 572 | **Y no sabemos si es del mundo o del clasificador** (`KJ-9`) |

**Lo que esto cambia respecto del encuadre habitual.** La conversación sobre redes de bots suele girar sobre **el récord de tráfico**: 31,4 Tbps, un titular, una cifra que crece cada trimestre. Esa conversación es irrelevante para casi todas las organizaciones, porque nadie que no sea un operador de tránsito va a absorber ni una décima parte de eso: **o hay desvío preacordado o no hay defensa, y el número exacto no cambia la decisión.**

La conversación que sí importa es la que este informe mide, y tiene dos mitades. La primera es que **la amenaza real para un proveedor regional no es el récord mundial sino la ráfaga de cinco segundos repetida mil veces al día**, que no sale en ningún titular porque no rompe ningún récord y sí degrada el servicio de forma continua. La segunda es que **la mayor parte de esta infraestructura no está haciendo DDoS en absoluto**: está vendiendo el ancho de banda residencial de dispositivos comprometidos, y eso llega a nuestras organizaciones **por la puerta de entrada, no por la de salida** — como tráfico de aspecto doméstico y reputación limpia contra nuestros portales de acceso.

## E-2. La asimetría: los objetivos están aquí y la infraestructura no

<!-- cti:chart title="Dónde están los objetivos (ventana de 97 min, 2.500 eventos)" cap="Medición propia del 19-11-2026, 13:33–15:11 UTC. Es una ventana corta: las proporciones envejecen, la asimetría no." -->

| País del objetivo | Eventos |
|---|---|
| `Brasil` | 2006 |
| `EE. UU.` | 235 |
| `China` | 172 |
| `Qatar` | 45 |
| `Hong Kong` | 17 |
| `Alemania` | 10 |

<!-- cti:chart title="Dónde está la infraestructura de control (573 direcciones)" cap="Mismo momento, otro conjunto de datos. Latinoamérica suma 12 direcciones: el 2,1 %." -->

| País del C2 | Direcciones |
|---|---|
| `EE. UU.` | 323 |
| `Singapur` | 78 |
| `Países Bajos` | 54 |
| `Alemania` | 32 |
| `Hong Kong` | 12 |
| `Brasil` | 11 |
| `Reino Unido` | 11 |

**Las dos gráficas son el mismo ecosistema en el mismo minuto, y no se parecen en nada.** Esa es la asimetría, y tiene tres consecuencias que conviene no confundir entre sí:

1. **Para la víctima**, significa que **el bloqueo por país es inútil y además peligroso**: el tráfico de ataque llega de dispositivos infectados repartidos por todo el mundo, y bloquear los países donde está el control no detiene ni un paquete del ataque, porque el control no es el que inunda.
2. **Para el defensor de red**, significa que **el punto de intervención es el canal de control y no el de ataque**. Un agujero negro sobre 573 direcciones `/32` no absorbe el ataque, pero **impide que el nodo infectado reciba la orden**, y eso sí escala. Es exactamente lo que hace el feed de `X-1`.
3. **Para quien hace política o notificación de abuso**, significa que **los interlocutores están en otra jurisdicción**, mayoritariamente Estados Unidos y Singapur, y que una vía nacional o regional de notificación no alcanza al 98 % del problema.

### E-2.1 Foco regional: por qué los proveedores regionales de fibra y no los nacionales

El dato más robusto de este informe no es nuestro: es la **coincidencia** de nuestra medición con la de A10 Networks nueve meses antes. Ellos, en una semana de febrero de 2026, contaron **17.527 ataques en Brasil con cerca del 99 % concentrado en cinco ISP regionales de fibra**, y constataron que los grandes operadores nacionales quedaron prácticamente intactos. Nosotros, en 97 minutos de noviembre, encontramos **diecisiete operadores regionales brasileños entre los veinte ASN más golpeados y ningún nacional**.

Dos mediciones, dos métodos, nueve meses de separación, el mismo resultado. **Eso convierte el patrón en un hecho estructural y no en una anécdota de una ventana.**

**Las cuatro explicaciones posibles, y cuál sostiene este informe:**

| Explicación | Argumento | Estado |
|---|---|---|
| **Eficiencia del atacante** | Un operador regional tiene **objetivos valiosos** —servidores de juego, clientes empresariales, su propia red de acceso—, **poca capacidad de absorción** y, muy a menudo, **ningún desvío preacordado con su tránsito**. Un ataque pequeño produce un efecto grande | **Retenida como principal.** *Probable (55–80 %)* |
| **Disponibilidad de objetivos** | Brasil tiene miles de sistemas autónomos de acceso, muchos más que cualquier otro país de la región: hay simplemente más objetivos de ese perfil | **Retenida como concurrente.** Explica el país, no el tamaño |
| **Alquiler por encargo contra servicios de juego** | La presencia de prefijos `/32` individuales y de puertos altos no estándar entre los objetivos (§`T-1`) es compatible con ataques contratados contra servidores de juego alojados en esas redes | **Retenida como parcial.** `CTI-2026-045` la desarrolla con los datos de `Liso` |
| **Represalia o competencia entre proveedores** | Existe un precedente documentado y grave: Krebs informó en abril de 2026 de un actor brasileño con acceso de raíz a la infraestructura de **una empresa de mitigación de DDoS**, que construyó una red de bots rastreando enrutadores inseguros; el director de la empresa atribuyó la actividad a un competidor | **Retenida como hipótesis que no podemos evaluar.** No hay confirmación independiente de la atribución a un competidor, y **nuestra medición no distingue motivación** |

> **Y una conexión con el expediente de `CTI-2026-037` que conviene anotar
> aunque los actores no tengan nada que ver.** El caso de Krebs implica
> **vulnerabilidades de enrutadores TP-Link** como vía de reclutamiento de
> nodos, y `CTI-2026-037` documentó a un servicio de inteligencia estatal
> secuestrando el DNS de enrutadores **de la misma marca y clase**. No hay
> vínculo entre los actores y no se insinúa ninguno. **Lo que hay es un
> hallazgo sobre el inventario: la misma clase de dispositivo, instalada por
> millones en hogares y pequeñas oficinas de la región, sirve a la vez de nodo
> de red de bots criminal y de punto de interceptación estatal.** Quien
> defienda ese parque no tiene dos problemas: tiene un problema con dos
> clientes.

### E-2.2 Chile: defendido por encima de su exposición, y con una dirección de control propia

| Dato chileno | Valor | Lectura |
|---|---|---|
| Ataques con objetivo en Chile en la ventana medida | **0 de 2.500** | **No concluir que Chile no es atacado.** Una ventana de 97 minutos no detecta un fenómeno de baja frecuencia. Es `G-3` |
| Direcciones de mando y control alojadas en Chile | **1 de 573** | `64.176.16.182`, en un proveedor de nube internacional con presencia local. Pertenece a `Liso` y se detalla en `CTI-2026-045` |
| Pares BGP chilenos del feed defensivo | **22 de 176 (12,5 %)** | **Segundo país del mundo en adopción**, muy por encima de su exposición medida |
| Punto de presencia del feed | **Chile** (`rbl1.botnet.cl`) | La capacidad se opera desde aquí |

**La lectura honesta de este cuadro es que Chile aparece en este expediente sobre todo como origen de capacidad defensiva, no como víctima.** Y eso puede ser cierto o puede ser un artefacto de nuestra ventana: la diferencia importa, porque **si es un artefacto, estamos declarando una ausencia que no hemos medido**. Es la razón de que el muestreo longitudinal de `G-2` sea la primera prioridad después de `G-1`, y de que la caducidad de este informe sean 60 días y no 90.

## E-3. El negocio silencioso: por qué el 85 % de la infraestructura no ataca a nadie

<!-- cti:bars title="Reparto de la infraestructura de mando y control por modelo de negocio (572 direcciones atribuidas)" -->

| Modelo | Direcciones |
|---|---|
| Proxy residencial puro (7 familias, 0 ataques) | 487 |
| DDoS y mixtas (26 familias) | 85 |

**El dato y su interpretación, por separado.** El dato es que siete familias —`CXFJ` 215, `Aigogo` 134, `LinkFog` 46, `SZJL` 46, `Hotota` 24, `Aisuru-Proxy` 13, `Titan` 9— suman **487 direcciones y cero eventos de ataque**, mientras las veintiséis restantes suman **85 direcciones y 1,27 millones de eventos**.

La interpretación es que **se trata de dos industrias con requisitos de infraestructura opuestos:**

| Dimensión | Proxy residencial | DDoS |
|---|---|---|
| **Qué vende** | Acceso continuado a direcciones residenciales de aspecto legítimo | Interrupción puntual |
| **Qué exige la infraestructura** | **Disponibilidad y capilaridad.** Cada nodo tiene que poder recibir y devolver tráfico de forma fiable y permanente | **Un punto de mando desechable.** Dar la orden y desaparecer |
| **Dónde se aloja** | Nubes grandes y reputadas: **65 % Estados Unidos, 15 % Singapur, 9 % Países Bajos** | **Más disperso y menos reputado**: Alemania al 27 %, con presencia de proveedores pequeños, Vietnam, Rusia, Rumanía |
| **Coste de perder una dirección** | **Alto**: interrumpe un servicio que se está cobrando | **Bajo**: se levanta otra |
| **Plataforma del nodo** | **Android**, mayoritariamente: decodificadores, televisores, tabletas baratas | IoT clásico (MIPS, ARM) y Android |
| **Visibilidad para la víctima** | **Ninguna.** El dueño del dispositivo no nota nada | Total, por definición |

**La corroboración externa es de un día antes de este informe y es muy buena.** HUMAN Security publicó el **18 de noviembre de 2026** su análisis de BADBOX 3.0: decodificadores Android de bajo coste que llegaron a generar del orden de **40.000 millones de solicitudes publicitarias diarias**, con **módulos de proxy que inscriben el dispositivo en once redes de proxy residencial distintas** sin consentimiento del dueño, y con vínculo del catálogo de software a un fabricante de electrónica mediante un lanzador instalado de fábrica.

**«Once redes de proxy residencial distintas» es, desde la capa de red, exactamente lo que medimos:** siete marcas de módulo de proxy, cada una con su propia infraestructura de control, **sin una sola dirección en común**, alimentándose plausiblemente del mismo parque de dispositivos. La cifra no coincide —ellos ven once redes de proxy, nosotros siete familias de módulo— y **no debe forzarse a coincidir**: son dos recuentos de cosas distintas, el suyo de redes comerciales de reventa y el nuestro de familias de código. Pero la **forma** del hallazgo es la misma.

> **Y la consecuencia defensiva, que es la que se suele pasar por alto.** El
> proxy residencial **no nos ataca: nos visita.** Llega a nuestros portales de
> acceso, a nuestros formularios de inicio de sesión y a nuestras pasarelas de
> pago como **tráfico doméstico de un operador legítimo del país que al
> adversario le convenga**, con reputación limpia y sin ninguno de los rasgos
> que delatan a un centro de datos. Es lo que hace fracasar las defensas
> basadas en reputación de dirección y en geografía, y es el mismo mecanismo
> que `CTI-2026-037` describió para `CovertNetwork-1658` en el contexto de un
> actor estatal. **La diferencia es el precio: aquí se alquila.**

## E-4. Tendencia y pronóstico a seis meses

<!-- cti:cards -->

| Escenario a 6 meses | Desarrollo esperado | Etiqueta |
|---|---|---|
| **Continuidad con rotación de marca** | Una o dos de las tres familias dominantes enmudece —como `Cereal2`— y otra ocupa su lugar sin que el volumen agregado baje. El parque de nodos no cambia de manos: cambia de panel | `Probable · 55–80 %` |
| **Crecimiento del eje de proxy a costa del de DDoS** | La proporción de infraestructura dedicada a proxy residencial sigue subiendo, porque es el negocio con ingreso recurrente y sin titular. El documentado giro de Aisuru de DDoS a proxy es el precedente | `Probable · 55–80 %` |
| **Desplazamiento del objetivo a otros países de la región** | El patrón brasileño se replica en Argentina, Colombia o Chile, donde también hay muchos operadores regionales de fibra con poca capacidad de absorción | `Posibilidad real · 40–60 %` |
| **Contracción real por acción policial** | Una intervención como la de principios de 2026 reduce el agregado de forma sostenida. **Precedente favorable** —805 → 251 ataques sobre 1 Tbps entre trimestres— **y precedente desfavorable**: el sucesor suele estar ya operando (`CTI-2026-040`) | `Poco probable · 20–45 %` |
| **Que esta fuente deje de estar disponible** | Es un servicio de una empresa pequeña, sin respaldo institucional declarado. **Si cierra, este informe pierde su base de datos entera** y la región pierde el feed. Es un riesgo de concentración de fuente, y está en `G-4` | `Posibilidad real · 40–60 %` |

## E-5. Decisiones que este informe pide al nivel estratégico

| # | Decisión | A quién | Coste | Por qué ahora |
|---|---|---|---|---|
| **1** | **Suscribir el feed BGP de agujero negro**, o evaluarlo formalmente y documentar la decisión de no hacerlo | Arquitectura de red · Operaciones | **Bajo**: dos sesiones eBGP y una política de importación. Plantillas publicadas para cuatro fabricantes (`X-2`) | Es la única medida de este informe que **reduce riesgo sin comprar nada**. Y 176 pares ya lo hicieron |
| **2** | **Negociar desvío ante DDoS con el tránsito ANTES de necesitarlo**, con activación automática | Arquitectura de red · Compras | Medio | **Cinco segundos de mediana** (`KJ-5`). Es la recomendación literal de A10 para este fenómeno, y la nuestra |
| **3** | **Si somos proveedor de acceso regional: asumir que somos objetivo preferente y no daño colateral** | Dirección · Riesgo | Cero decidirlo | Diecisiete operadores regionales entre los veinte más golpeados, y el 99 % de A10 en cinco de ellos |
| **4** | **Tratar el tráfico de proxy residencial como un riesgo de autenticación, no de red** | CISO · Identidad | Medio | `E-3`. Es tráfico doméstico con reputación limpia: **las defensas por dirección y por país no lo ven** |
| **5** | **No organizar la defensa por nombre de familia** | CTI · SOC | Cero | `Cereal2`: 395.887 eventos a cero infraestructura en tres semanas |
| **6** | **Dirigir notificación de abuso documentada a los cinco proveedores de alojamiento concentradores**, **y medir el resultado en direcciones vivas de la familia y no en bloques vaciados** | Legal · CTI | Bajo | El **62,6 %** de la infraestructura en cinco interlocutores (`KJ-7`). **Y la salvedad medida en la versión 1.3**: `SZJL` rehízo su huella, ampliada, en un proveedor nuevo **en un día** (`KJ-11`, `O-3.6`). La palanca sigue siendo la de mayor rendimiento; **lo que no sirve es la métrica ingenua**. El interlocutor nuevo, `AS150436` Byteplus, tiene equipo de abuso registrado en APNIC |
| **7** | **Revisar el parque de enrutadores y decodificadores de la organización y de sus trabajadores remotos** | TI · Seguridad | Medio | El nodo de estas redes es un dispositivo doméstico. **Y el mismo parque es objetivo estatal** (`E-2.1`) |
| **8** | **Asignar la atención de forma desigual y explícita entre las 33 familias** | CTI | Cero | 90,2 % de la actividad en tres. Repartir por igual es gastar el 90 % del esfuerzo en el 10 % del problema |

---

# NIVEL OPERACIONAL
### Para: Jefatura de SOC, Ingeniería de red, Threat Hunting, CTI · Horizonte: semanas

## O-1. Las 33 familias, clasificadas por lo que son y no por el orden en que la fuente las lista

<!-- cti:note type="warn" -->

> ⚠ **Cómo leer esta tabla, porque mezcla dos escalas que no son
> comparables.** La columna **«eventos acumulados»** es el contador histórico
> de la fuente y es homogénea: verificamos en §O-3.2 que dentro de una familia
> la secuencia es contigua, de modo que **es un recuento real de eventos**. En
> cambio las columnas **«objetivo principal»** y **«% región»** se calculan
> sobre **los últimos 100 eventos de cada familia**: para `Liso` eso son cuatro
> minutos de hoy, y para `Ouroboros` es su vida entera, porque tiene cuatro
> eventos en total. **Para las familias de menos de 100 eventos acumulados las
> dos últimas columnas describen toda su historia; para las grandes describen
> un instante.** No se deben comparar entre sí.

<!-- cti:table highlight="DOMINANTE|PROXY|MUDA|Brasil" -->

| Familia | Clase | Eventos acum. | C2 | Último evento | Objetivo principal (últimos 100) | % región |
|---|---|---|---|---|---|---|
| **`Liso`** | **DDoS — DOMINANTE** | **444.692** | 17 | **19-11 15:09** | **Brasil 86** | **86 %** |
| **`Cereal2`** | **DDoS — MUDA desde 30-10** | **395.887** | **0** | **30-10 11:02** | EE. UU. 71 · Brasil 25 | 25 % |
| **`Potassium`** | **DDoS — DOMINANTE** | **304.258** | 24 | 19-11 10:52 | EE. UU. 20 · P. Bajos 19 · Qatar 11 | 4 % |
| `SixSayven` | DDoS + proxy + RCE | 98.667 | 1 | 19-11 15:09 | **China 97** | 0 % |
| `BNETv2` | Puerta trasera Android | 9.947 | 2 | 19-11 14:57 | Alemania 19 · Qatar 17 · EE. UU. 17 | 1 % |
| `Kittenbotv18` | DDoS Android — muda desde 18-10 | 7.778 | **0** | 18-10 19:40 | **Irak 79** · Azerbaiyán 14 | 0 % |
| **`KATARU`** | DDoS Android + propagación ADB | 4.904 | 1 | 11-11 02:08 | **Brasil 100** | **100 %** |
| `Aisuru-DDoS` | DDoS + proxy + RCE | **792** | **31** | 19-11 15:04 | Hong Kong 44 · Alemania 28 · China 20 | 0 % |
| `Sarbot` | DDoS + proxy + RCE | 633 | 1 | 18-11 22:24 | Alemania 43 · EE. UU. 21 | 0 % |
| `SERVICER` | DDoS Android (19 métodos) | 497 | 1 | 18-11 21:40 | Qatar 38 · EE. UU. 34 | 1 % |
| `HelloBot` | DDoS + RCE | 300 | 1 | 19-11 13:31 | China 57 · Hong Kong 19 | 0 % |
| `MINIv3` | DDoS Android G11 + MIPS | 172 | 1 | 19-11 05:42 | EE. UU. 70 | 0 % |
| `Yerco` | DDoS (UDP/TCP/GRE) | 157 | 1 | 17-11 11:48 | EE. UU. 75 · R. Unido 19 | 1 % |
| `Tadashi` | DDoS + proxy + RCE | 108 | **0** | 07-10 17:55 | China 16 · Hungría 16 | 0 % |
| `KittyCattos` | DDoS MIPS (15 métodos) | 100 | **0** | 05-10 17:19 | EE. UU. 53 · Alemania 25 | 0 % |
| `Kyorij` | DDoS (UDP/TCP/GRE) | 90 | 1 | 16-11 12:12 | Vietnam 41 · India 18 | 0 % |
| `Wuming0` | DDoS ARM (10 manejadores) | 28 | **0** | 07-10 14:01 | China 24 | 0 % |
| `FF1` | DDoS Android (HTTP/2 sobre TLS) | 23 | **0** | 11-10 15:51 | Qatar 21 | 0 % |
| `Supercrone` | DDoS + proxy + RCE | 22 | 1 | 19-11 13:54 | China 9 · EE. UU. 5 | 0 % |
| `Manta` | DDoS + **minero** | 21 | **0** | 05-11 17:31 | Corea 8 · EE. UU. 6 | 0 % |
| `EZF3` | DDoS + RCE (guion horario) | 20 | **0** | 11-10 00:42 | EE. UU. 10 | 0 % |
| `Eclipse` | DDoS + RCE (orden UPDATE) | 18 | 1 | 16-11 18:48 | **Brasil 7** · China 4 | **39 %** |
| `XOR10` | DDoS + proxy + RCE | 12 | 1 | 10-11 09:27 | Alemania 7 | 0 % |
| `Ecstasy` | DDoS (defectos documentados) | 5 | **0** | 14-11 10:11 | Australia 2 | 0 % |
| `Ouroboros` | DDoS + RCE | 4 | **0** | 15-10 23:53 | EE. UU. 2 | 0 % |
| `SexyBot-linked` | DDoS ARM (14 manejadores) | **0** | **0** | — | — | — |
| **`CXFJ`** | **PROXY Android puro** | **0** | **215** | — | — | — |
| **`Aigogo`** | **PROXY Android puro (DTLS)** | **0** | **134** | — | — | — |
| **`LinkFog`** | **PROXY TCP** *(binario sin identificar)* | **0** | **46** | — | — | — |
| **`SZJL`** | **PROXY Android puro** | **0** | **46** | — | — | — |
| **`Hotota`** | **PROXY Android modular + RCE** | **0** | **24** | — | — | — |
| **`Aisuru-Proxy`** | **PROXY dedicado** | **0** | **13** | — | — | — |
| **`Titan`** | **PROXY Android puro (WebSocket)** | **0** | **9** | — | — | — |

### O-1.1 La clasificación en cuatro clases, que es lo que esta tabla sirve para producir

Aplicando el criterio de `CTI-2026-042` —clasificar antes de invertir— las 33 familias se reparten así:

| Clase | Cuántas | Cuáles | Qué merece |
|---|---|---|---|
| **Dominante activa** | **2** | `Liso`, `Potassium` | **Expediente propio.** `Liso` lo tiene: `CTI-2026-045`. **`Potassium` es la brecha `G-7`** |
| **Activa secundaria** | **7** | `SixSayven`, `BNETv2`, `Aisuru-DDoS`, `Sarbot`, `SERVICER`, `HelloBot`, `Supercrone` | **Seguimiento con umbral**: alerta si su contador crece por encima de su línea base |
| **Infraestructura de proxy** | **7** | `CXFJ`, `Aigogo`, `LinkFog`, `SZJL`, `Hotota`, `Aisuru-Proxy`, `Titan` | **Expediente conjunto, no siete.** Es un ecosistema, no siete actores (`E-3`), y es **`G-5`** |
| **Muda o residual** | **17** | `Cereal2`, `Kittenbotv18`, `KATARU`, `Tadashi`, `KittyCattos`, `Wuming0`, `FF1`, `Manta`, `EZF3`, `Ouroboros`, `Ecstasy`, `XOR10`, `Eclipse`, `Kyorij`, `Yerco`, `MINIv3`, `SexyBot-linked` | **Una línea en una lista de vigilancia.** Con **dos excepciones nombradas abajo** |

**Las dos excepciones, porque la regla ciega se equivocaría con ellas:**

- **`Cereal2` no es residual: es una familia grande que acaba de callarse.** Con 395.887 eventos acumulados y cero infraestructura viva, es el objeto más interesante de la lista de mudas, y lo que merece no es vigilancia pasiva sino **la búsqueda activa de su sucesora**, que es el método del `Anexo D` de `CTI-2026-040`.
- **`KATARU` es residual en volumen y máxima en relevancia regional**: 4.904 eventos, y **el 100 % de sus últimos 100 eventos tuvo objetivo en Brasil**. Es, además, la única familia de la lista cuya matriz de capacidades declara **propagación por ADB** —el puente de depuración de Android—, lo que la hace la candidata más plausible a crecer en un parque de decodificadores regional. **Merece seguimiento por encima de su volumen.**

## O-2. La fuente: qué es `botnet.cl`, quién la opera y cómo hay que valorarla

**Lo que es, descrito con sus propias funciones observadas:** un servicio que publica (a) un **flujo de observaciones de ataque en vivo** con objetivo, método, duración y prefijo afectado; (b) una **lista de direcciones de mando y control** con ASN, país y fechas de primera y última observación; (c) una **matriz de capacidades por familia** —DDoS, proxy residencial, ejecución remota de código— con descripciones que sólo pueden proceder de análisis de binarios; y (d) un **feed BGP de agujero negro** para consumir todo lo anterior como rutas.

**Quién la opera.** La agenda de **NANOG 98** recoge una charla titulada «Botnet.cl — Live Botnet Monitoring and BGP Feed» atribuida a **Rodrigo Peña, de Bitred Group SpA**, en la que se describe el uso de aprendizaje automático para descubrir redes de bots emergentes, seguir su actividad e identificar su infraestructura de control, y se afirma **«más de 100 ISP suscritos a nuestro feed BGP de agujero negro en dos meses»**.

**Y una salvedad que hay que poner por delante:** esa atribución procede de **un listado de ponentes de una conferencia, no del propio sitio**. No localizamos en `botnet.cl` una página de identificación de la entidad operadora, ni datos de contacto corporativo. **Es la única atribución que tenemos y se consigna con ese grado.** Para una fuente de la que depende un informe entero, es poco, y está en `G-4`.

### O-2.1 Verificación propia de la afirmación pública del operador

**Esta es la única parte de este informe en que verificamos a la fuente en lugar de usarla**, y el resultado es favorable:

| Afirmación | Dónde | Nuestra medición (19-11-2026) | Veredicto |
|---|---|---|---|
| «Más de 100 ISP suscritos en dos meses» | Agenda de NANOG 98 | **176 pares BGP establecidos distintos** en 7 países, con 2 nodos activos | **Corroborada y superada.** La interfaz declara el detalle por país: BR 126, CL 22, AR 20, US 4, MX 1, PY 1, VE 1 |
| Dos puntos de presencia | Página del feed | `rbl1.botnet.cl` → `38.7.199.217` (Chile) · `rbl2.botnet.cl` → `45.171.231.57` (São Paulo) | **Corroborada** por resolución directa |
| Uso de aprendizaje automático para descubrir familias | Agenda de NANOG 98 | **No verificable.** Es una afirmación sobre su método interno | **Sin evaluar** |
| Análisis de binarios por familia | Implícito en la matriz | **No verificable, pero el detalle es coherente con ello**: «catorce manejadores de inundación», «diecinueve métodos», «las opciones numéricas resuelven a 10», «defectos de la carga nativa documentados» | **Plausible, no verificada** |

> **Dos observaciones sobre la calidad de la fuente, y las dos son
> favorables, que es inusual en esta cartera.**
>
> La primera: **declara sus propias limitaciones por familia.** La matriz usa
> «**No** = no identificado en los binarios revisados» y «**Desconocido** =
> evidencia insuficiente» como valores distintos, y anota cosas como
> «binario del cliente aún no identificado» en `LinkFog` o «defectos de la
> carga nativa y limitaciones de HTTP permanecen documentados» en `Ecstasy`.
> **Una fuente que distingue «no lo hace» de «no lo sé» está haciendo el
> trabajo que esta cartera exige de sí misma.**
>
> La segunda: **la etiqueta de antigüedad del feed es una concesión contra su
> propio interés.** Publica una comunidad para «visto hace menos de 24 horas»
> y otra para «visto hace más de siete días», y **declara expresamente que
> entre 24 horas y siete días no se adjunta ninguna etiqueta**. Eso permite al
> suscriptor **descartar las entradas más viejas de su propio feed**, es decir,
> reducir su utilidad aparente. Una fuente que facilita que la filtres a la
> baja está más interesada en acertar que en parecer grande.

### O-2.2 El error que este informe estuvo a punto de publicar

**Lo que ocurrió, en orden.** La interfaz de consulta de eventos admite un parámetro de familia. Al recolectar, no lo usamos: pedimos la ruta sin parámetros y paginamos catorce veces, obteniendo **1.400 eventos** con su cursor de continuación, su contador de secuencia y su marca de agua. Todo tenía el aspecto del flujo general.

**El análisis de esos 1.400 eventos daba una historia limpia y coherente:** una sola familia, `Cereal2`, con el **81,9 % de sus objetivos en Estados Unidos** y un solo proveedor de alojamiento —`PEG TECH INC`, `AS398823`— recibiendo **1.136 de los 1.400 eventos**; duración mediana de 60 segundos; puerto 80 en el 85 % de los casos. De ahí salían dos conclusiones: que **`Cereal2` era la familia dominante del ecosistema** y que **el objetivo principal de esta actividad era un proveedor de alojamiento estadounidense**.

**Las dos son falsas.** La consulta sin parámetros devuelve, **en silencio y sin ningún aviso en la respuesta**, únicamente los eventos de `Cereal2` — una familia **muda desde el 30 de octubre** — con su histórico congelado. El flujo real de ese momento era otro: `Liso` con el 92,4 % de los eventos y **Brasil con el 80,2 % de los objetivos**.

**Cómo se detectó, y es lo menos tranquilizador del episodio:** no por una comprobación metódica, sino porque **la portada del sitio mostraba a `Liso` atacando a operadores brasileños en el mismo minuto en que nuestros datos decían que sólo había `Cereal2` atacando a un proveedor estadounidense**. Fue una contradicción visible, por casualidad, entre dos vistas del mismo servicio.

**La verificación posterior, con cuatro consultas de control:**

| Consulta | Eventos | Familias | Marca de agua | Ventana |
|---|---|---|---|---|
| sin parámetros | 100 | **`cereal2` 100** | 395.887 | 30-10, 10:39 → 11:02 |
| `family=all` | 100 | `liso` 96 · `sixsayven` 4 | **1.269.333** | **19-11, 15:05 → 15:09** |
| `family=liso` | 100 | `liso` 100 | 444.670 | 19-11, 15:05 → 15:09 |
| `family=all&limit=5` | 5 | `liso` 5 | 1.269.333 | 19-11, 15:09 |

**Las marcas de agua lo cierran:** 395.887 sin parámetros frente a 1.269.333 con `family=all`. La consulta por omisión estaba devolviendo **el 31 % del flujo**, y además el tramo congelado de una familia inactiva.

> **La lección, y es la razón de que este error esté escrito en lugar de
> borrado.** `O-2.2` de `CTI-2026-037` estableció que **cuando los hechos
> verificados forman una explicación elegante, ése es el momento de mayor
> riesgo de la colección**. Ese caso era un adversario y una fuente humana.
> **Este es el mismo fallo con una interfaz automatizada, y es peor en un
> sentido concreto: aquí no hubo ninguna señal de que faltara algo.** La
> respuesta era bien formada, paginaba, traía contadores crecientes y un
> cursor que funcionaba. **Un parámetro ausente no produce un error; produce
> una respuesta a otra pregunta.**
>
> Y hay un agravante que conviene asumir: **los datos falsos eran más
> interesantes.** «Una familia dominante atacando a un proveedor
> estadounidense» es una historia más limpia que «veintiséis familias de
> actividad desigual atacando a diecisiete operadores regionales
> brasileños». **La hipótesis cómoda venía incorporada en el valor por
> omisión de la interfaz**, y eso es exactamente la trampa que el `Anexo D`
> intenta cerrar.

## O-3. La medición: método y resultados

### O-3.1 Qué se recogió

| Conjunto | Volumen | Método | Para qué sirve |
|---|---|---|---|
| **Direcciones de mando y control** | **573** | Consulta del agregado completo | `KJ-1`, `KJ-7`, `A.2`, `A.3` |
| **C2 por familia** | 33 consultas, **572 atribuidas** | Una consulta por familia | `KJ-2`, `KJ-9`, `O-1` |
| **Flujo de eventos mezclado** | **2.500 únicos**, 97 min | 25 páginas con `family=all` y cursor | `KJ-1`, `KJ-4`, `KJ-5` |
| **Eventos por familia** | 33 × hasta 100 | Una consulta por familia | `O-1`, contadores acumulados |
| **Contigüidad de secuencia** | 800 eventos de `Liso` | 8 páginas de una sola familia | **Validación de `KJ-3`** (§O-3.2) |
| **Pares BGP** | 176, 7 países | Consulta del agregado de la tabla de clasificación | `KJ-6`, `O-5` |
| **Matriz de capacidades** | 33 familias × 3 ejes | Lectura de la página del feed | `O-1`, `E-3` |

**Y una decisión de conducta de la colección que conviene declarar:** todas las consultas se hicieron contra la **interfaz pública de consulta** del servicio, con cadencia baja, identificándonos con un agente de usuario genérico de cliente de investigación, **sin credenciales, sin eludir ningún control y sin acceder a nada que el sitio no sirva a cualquier visitante**. El muestreo longitudinal lanzado al cierre hace **una petición cada 90 segundos**. No se estableció sesión BGP con el feed.

### O-3.2 La validación que hace utilizable el `KJ-3`, y el error de diseño que tuvo antes

Los contadores acumulados son la base de la afirmación de que tres familias concentran el 90,2 % de la actividad. Antes de usarlos había que saber **si son recuentos de eventos o identificadores con huecos**.

**La primera prueba estuvo mal diseñada.** Tomamos los 2.500 eventos del flujo mezclado y comprobamos la contigüidad de su número de secuencia: salió un rango de 444.700 para 2.500 eventos, es decir **442.200 huecos**, y la conclusión aparente era que el contador no sirve.

**Era un error nuestro, no de los datos.** En el flujo mezclado **cada evento lleva la secuencia de su propia familia**, de modo que mezclar familias es mezclar espacios de numeración distintos: los huecos son inevitables y la prueba no mide nada.

**La prueba correcta, dentro de una sola familia:** 800 eventos consecutivos de `Liso`, secuencias de 443.929 a 444.728, **rango de exactamente 800 para 800 eventos: cero huecos**. Por tanto, dentro de una familia la secuencia es contigua y **el contador es un recuento real de eventos acumulados**. `KJ-3` se sostiene.

### O-3.3 Lo que midió el flujo en vivo

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `2.500` | Eventos únicos de la ventana | 97 minutos, 13:33–15:11 UTC del 19-11-2026 |
| `25,6` | Eventos por minuto, media | Cadencia sostenida, no un pico |
| `5` | Familias distintas observadas atacando | De 33 en seguimiento. `Liso` 92,4 %, `SixSayven` 5,9 % |
| `69` | ASN objetivo distintos | De los cuales 17 brasileños entre los 20 más golpeados |
| `258` | Prefijos objetivo distintos | El ataque se reparte por subredes del mismo operador |
| `550` | Eventos contra un solo operador | `Halver LTDA`, `AS274564`, Brasil |
| `23,2 %` | Segundos con dos o más ataques simultáneos | 580 de 985 segundos con actividad |
| `11` | Máximo de ataques en un mismo segundo | Contra **seis prefijos distintos del mismo operador** |

### O-3.5 Verificación en una segunda ventana independiente *(añadido en la versión 1.1)*

El control 5 del `Anexo D` —**medir dos ventanas separadas antes de afirmar una proporción**— era el único que la versión 1.0 **no pudo ejecutar antes de emitir**. El muestreo longitudinal lanzado al cierre lo permitió horas después, y **el resultado es favorable**:

| Medida | Ventana 1 *(13:33–15:11, 2.500 ev.)* | **Ventana 2** *(15:11–15:31, 572 ev.)* | **Ventana 3** *(15:31–15:45, 357 ev.)* |
|---|---|---|---|
| **Objetivos en Brasil (global)** | **80,2 %** | **76,9 %** | **73,1 %** |
| `Liso` sobre el total de eventos | 92,4 % | 92,1 % | **88,0 %** |
| **Objetivos de `Liso` en Brasil** | 86,9 % | 83,5 % | **83,1 %** |
| Pulsos de 5 s en `Liso` | 79,2 % | 82,4 % | **82,5 %** |
| Operador más atacado | `Halver LTDA` | `Halver LTDA` | **`Halver LTDA`** |
| Familias observadas atacando | 5 | 4 | 4 |

**Y las tres ventanas juntas enseñan algo que dos no enseñaban, que es la razón de haber añadido la tercera.** La proporción **global** de objetivos brasileños **desciende de forma monótona**: 80,2 → 76,9 → 73,1. Pero la proporción de objetivos brasileños **de `Liso`** se queda prácticamente clavada: 86,9 → 83,5 → 83,1. **Lo que se mueve no es la selección de objetivos de ninguna familia: es la mezcla de familias.** `Liso` baja del 92,4 % al 88,0 % del flujo, y el hueco lo ocupan `SixSayven` —que apunta a China— y `BNETv2`, de modo que **el agregado se desplaza sin que nadie cambie de conducta.**

> **La consecuencia de método, y es importante para cualquiera que use esta
> fuente: el agregado de este ecosistema es una media ponderada por una mezcla
> inestable, y por tanto es la cifra menos informativa que se puede extraer.**
> «El 80 % de los ataques van contra Brasil» es verdadero para una ventana y
> engañoso como caracterización, porque cambia cuando una familia sube o baja
> su ritmo. **La magnitud estable es la de cada familia por separado.** Es la
> misma lección que `KJ-3` daba desde otro ángulo —tres familias concentran el
> 90 %— y aquí se convierte en una instrucción: **medir por familia, no en
> agregado.**

**Qué sostiene esto y qué no.** Sostiene que **las proporciones por familia no eran un accidente de la ventana**: las de `Liso` se mueven menos de 3,8 puntos en tres mediciones y el operador más atacado es el mismo en las tres. **No sostiene** que sean la medida del mes: **las dos ventanas son del mismo día y de la misma tarde**, separadas por minutos, no por días. Un fenómeno con ciclo diario o semanal seguiría invisible.

**Y una observación sobre la honestidad del control:** el tramo 15:11–15:31 es **estrictamente posterior** a la primera ventana y no comparte un solo evento con ella, lo que se verificó por identificador. Si se hubiera usado el acumulado completo de la serie —que solapa con la ventana 1— la coincidencia habría sido artificialmente buena. **La comprobación vale porque se hizo sobre el tramo disjunto, y eso había que decidirlo antes de mirar el resultado.**

La instantánea de infraestructura también se repitió: **573 direcciones a las 15:08 y 574 a las 15:24**. Estabilidad en quince minutos, lo que es coherente con una mediana de vida de 5,2 días.

### O-3.4 La estructura del alojamiento: dos huellas disjuntas y doce bloques compartidos

Esta sección se construyó al final del expediente, cruzando las 33 consultas por familia con los bloques `/24` de cada dirección, y **produjo el resultado más estructural del informe**.

**Primer resultado: los dos negocios no se tocan.**

| Medida | Proxy residencial | DDoS y mixtas | Compartido |
|---|---|---|---|
| Direcciones | 487 | 85 | **0** |
| Bloques `/24` | **144** | **62** | **0** |
| Sistemas autónomos | 35 | 26 | **4 de 57** |

**Ni un bloque de 206 aloja a la vez una familia de proxy y una de DDoS.** Eso es un hecho sobre dónde se compra el alojamiento, y es la razón por la que `H-2` baja de «posibilidad real» a «poco probable»: **un sesgo de clasificación de binarios no puede producir una separación geográfica del alojamiento**, porque el clasificador no mira el bloque.

**Y la huella de cada negocio tiene carácter distinto**, lo que encaja con la economía de `E-3`:

| Negocio | ASN dominantes | Perfil |
|---|---|---|
| **Proxy** | Zenlayer (169) · GoCodeIT (60) · Alibaba US Technology (52) · Tube-Hosting (42) · CDS Global Cloud (30) | **Volumen y capilaridad**: proveedores grandes, bloques enteros, decenas de direcciones contiguas |
| **DDoS** | DigitalOcean (30) · Blatant Technologies (11) · UAB Host Baltic (6) · Lanit Technology (6) · RouterHosting (5) · The Constant Company (3) | **Unidades sueltas y desechables**: servidores virtuales de proveedores pequeños, pocas direcciones por ASN |

**Segundo resultado: los doce bloques compartidos, y el vínculo que sugieren.**

| Bloque | Dir. | Familias | ASN |
|---|---|---|---|
| `66.92.19.0/24` | 32 | **`CXFJ` · `Hotota` · `LinkFog`** | `AS62610` Zenlayer |
| `66.92.17.0/24` | 22 | **`CXFJ` · `Hotota` · `LinkFog`** | `AS62610` Zenlayer |
| `141.98.10.0/24` | 6 | **`Aisuru-DDoS` · `Eclipse`** | `AS209605` UAB Host Baltic |
| `199.190.45.0/24` | 6 | `Hotota` · `LinkFog` | `AS62610` Zenlayer |
| `128.14.146.0/24` | 5 | `CXFJ` · `LinkFog` | `AS62610` Zenlayer |
| `107.151.198.0/24` | 4 | `CXFJ` · `Titan` | `AS62610` Zenlayer |
| `98.96.225.0/24` | 4 | `Hotota` · `LinkFog` | `AS62610` Zenlayer |
| `98.96.240.0/24` | 4 | `Hotota` · `LinkFog` | `AS62610` Zenlayer |
| `107.151.209.0/24` | 3 | `Hotota` · `LinkFog` | `AS62610` Zenlayer |
| `128.14.145.0/24` | 3 | `Hotota` · `LinkFog` | `AS62610` Zenlayer |
| `69.165.76.0/24` | 3 | `Hotota` · `LinkFog` | `AS62610` Zenlayer |
| `66.93.173.0/24` | 2 | `CXFJ` · `Hotota` | `AS62610` Zenlayer |

**Lo que sostiene y lo que no.** `Hotota` y `LinkFog` coinciden en **seis bloques distintos**, y `CXFJ` con una u otra en cuatro más. Eso **no demuestra que sean el mismo operador**: once de los doce bloques están en el mismo proveedor, y un proveedor grande con asignación por bloques puede colocar a clientes distintos en direcciones vecinas. **Pero seis coincidencias no son una.**

**La prueba discriminante que lo resolvería, y que no podemos hacer:** si las direcciones de `Hotota` y `LinkFog` dentro de un mismo `/24` fueran **contiguas o alternas** —es decir, asignadas en el mismo lote— el vínculo sería fuerte; si están dispersas por el bloque, es coincidencia de proveedor. **Requiere la lista completa ordenada por dirección, que tenemos, y una decisión sobre qué cuenta como contiguo, que no está establecida.** Queda como `G-11`.

**Y el caso de `141.98.10.0/24` merece nota aparte**, porque es el único solapamiento entre dos familias de **DDoS** y porque enfrenta a la familia a la que se atribuye el récord mundial con una familia residual de 18 eventos. Si `Aisuru-DDoS` y `Eclipse` comparten alojamiento, la lectura más económica es que **`Eclipse` sea una herramienta o una prueba del mismo entorno**, y no una operación independiente. Es *poco probable* *(20–45 %)* con **confianza baja**, es una sola coincidencia, y se consigna para que alguien con muestras lo compruebe.

### O-3.6 La migración de `SZJL`: el bloque que se vació y el proveedor que apareció *(añadido en la versión 1.3)*

**Cómo se encontró, porque importa para el método.** El parte de vigilancia del
22-11-2026 señaló tres direcciones nuevas y nada más. La migración **no apareció
en ningún parte diario**, y la razón es un límite del instrumento que conviene
escribir: **el parte compara el día con el día anterior, y un concentrador que
entra completo en una sola jornada aparece una vez como noventa y dos candidatos
sueltos y nunca más.** Se encontró porque se remidieron los agregados
publicados en `A.2` y `A.3` contra la fuente, que es una comprobación distinta
de un delta diario.

**Lo que midió la remedición del 22-11-2026**, contra las cifras que el informe
publicó el 19-11:

| Sistema autónomo | 19-11 | 22-11 | Delta |
|---|---|---|---|
| `AS62610` Zenlayer | 147 | **163** | **+16** |
| **`AS150436` Byteplus Pte. Ltd.** | **—** | **92** | **nuevo** |
| `AS835` GoCodeIT | 58 | 63 | +5 |
| `AS49581` Tube-Hosting | 42 | 43 | +1 |
| `AS63199` CDS Global Cloud | 30 | 30 | 0 |
| `AS14061` DigitalOcean | 30 | 32 | +2 |
| **`AS45102` Alibaba (US) Technology** | **45** | **29** | **−16** |
| `AS403005` Blatant Technologies | 11 | 5 | −6 |

Y a nivel de bloque, los dos movimientos que se corresponden:

| Bloque | 19-11 | 22-11 | Familia |
|---|---|---|---|
| `43.117.72.0/24` *(`AS45102`)* | **43** | **20** | `SZJL` |
| **`101.47.51.0/24`** *(`AS150436`)* | **—** | **69** | **`SZJL`** |
| **`101.47.50.0/24`** *(`AS150436`)* | **—** | **21** | **`SZJL`** |

**Las 92 direcciones de Byteplus declaran todas la misma fecha de primera
observación —`2026-11-21`— y las 92 pertenecen a `SZJL`.** La familia pasa de 46
direcciones a 115. **No es un repliegue: es un traslado con ampliación.**

**La verificación de registro, en fuente primaria.** `AS150436` es
`BYTEPLUS-AS-AP`, Byteplus Pte. Ltd., Singapur, y el prefijo
`101.47.0.0 – 101.47.63.255` está asignado como `ALLOCATED NON-PORTABLE` a
`BYTEPLUS-SG`. **Tiene equipo de respuesta a incidentes registrado**
—`IRT-BYTEPLUS-SG`— con dirección de abuso publicada en el propio registro. Eso
importa para `E-5.6`: **el interlocutor nuevo es nominal y está en el RDAP**, no
hay que buscarlo.

> **La lectura que cambia una recomendación.** `E-5.6` propone la notificación
> de abuso documentada a los cinco proveedores concentradores como la palanca de
> mayor rendimiento, y **sigue siendo cierto**. Lo que esta medición añade es el
> **denominador que faltaba**: el operador de `SZJL` reconstituyó su huella, más
> grande, en otro proveedor **en un día**. De modo que la métrica de éxito de
> una campaña de notificación **no puede ser «el bloque se vació»**, porque un
> bloque vaciado es compatible con una migración exitosa del adversario. **La
> métrica tiene que ser el recuento total de direcciones vivas de la familia**,
> y esa cifra, para `SZJL`, **subió un 150 % la misma semana en que su bloque
> principal perdió la mitad.**

### O-3.7 Verificación del clasificador por huella de servicio, y las tres direcciones que no encajan *(añadido en la versión 1.3)*

**El problema que resuelve.** `G-1` pregunta si el solapamiento cero de `KJ-9`
es del ecosistema o del clasificador, y propone como remedio *un correo al
operador de la fuente*. Hay una vía más barata y que no depende de que nadie
conteste: **medir la infraestructura que la fuente nombra, desde fuera, y ver si
la separación que ella declara aparece también en el servicio expuesto.**

**Método.** 27 direcciones —tres por familia, elegidas por orden de dirección
dentro de cada lista—, consultadas en Shodan el 22-11-2026, registrando
etiquetas, puertos y retos de autenticación de proxy.

| Familia | Clase declarada | Con etiqueta `proxy` | Huella de servicio |
|---|---|---|---|
| `CXFJ` | proxy | **3 de 3** | 22, 111 + **abanico 12337–12406**, reino `Proxy` |
| `Aigogo` | proxy | **3 de 3** | 22, 1080/8081 + **abanico 10000–10xxx**, reino `proxy` |
| `SZJL` | proxy | **3 de 3** | 22 + abanico amplio de puertos bajos |
| `Titan` | proxy | 2 de 3 | 22, **8888, 8889, 9100, 51001**, reino `Restricted` |
| `LinkFog` | proxy | 0 de 3 | 1080, 8080, 9000, 9101 — **puertos de proxy sin etiqueta** |
| `Hotota` | proxy | sin datos | **las tres sin puertos observados** |
| **`Liso`** | **DDoS** | **0 de 3** | 22, 80, 443 — certificado autofirmado |
| **`Potassium`** | **DDoS** | **0 de 3** | 22, 80, 443 — etiqueta `cloud` |
| **`SixSayven`** | **DDoS** | **0 de 3** | 23, 80, 554, 4567 — **perfil de dispositivo doméstico** |

**El resultado es asimétrico y por eso es útil.** Las nueve direcciones de las
tres familias de DDoS **no presentan ni una sola señal de proxy**; las de las
familias de proxy la presentan en once de dieciocho, y los siete casos sin
señal son **ausencias de dato** —`Hotota` sin puertos observados, `LinkFog` con
puertos de proxy pero sin etiqueta— **y no contraejemplos**. Es decir: la huella
**no produce ningún falso cruce**, que es la propiedad que hacía falta.

**Lo que esto le hace a `H-2`.** La etiqueta de un escáner de Internet y un
reino de autenticación HTTP son productos de la infraestructura observada, **no
del clasificador de binarios de `botnet.cl`**. Dos medidas que no comparten
mecanismo coinciden, y eso es lo que **baja `H-2` de «posibilidad real» a «poco
probable»**. `G-1` sigue abierta en su forma estricta —seguimos sin saber si una
dirección puede llevar dos familias—, pero **la duda sobre si las dos clases son
reales queda sustancialmente reducida sin depender de la fuente.**

### O-3.7.1 Las tres direcciones nuevas, y por qué NO se publican para bloqueo

Las tres direcciones que el parte del 22-11 señaló —`121.91.237.218`,
`121.91.238.159`, `121.91.242.135`— **comparten exactamente el patrón de las
familias de proxy** y, a la vez, **no son atribuibles a ninguna**:

- **Huella propia y consistente en las tres.** Puertos **22, 111 y 9009**, más un
  abanico en **18000–18021**. Cada puerto del abanico responde
  `407 Proxy Authentication Required` con la cabecera **`x-proxy-agent: atlas`**
  y reino `atlas`; el **9009** responde con un reino distinto, `gateway`, y
  cabeceras propias `X-Proxy-Code` y `X-Proxy-Message`. **La huella es idéntica
  en las tres direcciones**, lo que las agrupa; y **no coincide con ninguno de
  los tres reinos conocidos** (`Proxy`, `proxy`, `Restricted`), lo que las separa
  de las familias catalogadas.
- **La fuente las atribuye a `Aisuru-Proxy`, y llegar a eso costó un error
  propio que conviene dejar escrito.** La primera consulta por familia las
  declaró huérfanas: se interrogaron las 33 familias una a una y ninguna las
  contenía. **El fallo era nuestro y no de la fuente.** La interfaz exige el
  identificador de familia **en minúsculas y con guion**, y nuestra
  normalización convertía el guion en subrayado, de modo que `aisuru-ddos`,
  `aisuru-proxy` y `sexybot-linked` devolvían «familia desconocida» —un `404`
  bien formado— mientras las otras treinta respondían con normalidad.
  **Treinta aciertos hicieron verosímiles tres fallos.** Con el identificador
  correcto, `aisuru-proxy` devuelve **trece direcciones y las tres están entre
  ellas**, y el reparto por clase **sí es recomputable**: 556 de 625
  direcciones —el 89,0 %— pertenecen a las siete familias de proxy. *La lección
  es la del `Anexo D` vuelta del revés:* allí el peligro era una respuesta
  válida a una pregunta que no habíamos hecho; **aquí fue un error silencioso
  en nuestro propio formateo de la pregunta, y produjo una brecha inexistente
  que estuvo escrita en el borrador de esta versión.** Un `404` de una interfaz
  ajena merece la misma desconfianza que un `200`.
- **Ninguna corroboración externa.** ThreatFox: sin resultado. AbuseIPDB:
  **0 informes y puntuación 0**. GreyNoise: no las conoce. OTX: **0 pulsos**.
  Búsqueda abierta del agente `atlas` con el patrón de puertos: **sin
  corroboración** — la brecha se declara en lugar de rellenarse.
- **El registro, verificado documentalmente, y aquí se refutó una hipótesis.** El
  prefijo `121.91.224.0/19` **parece espacio de APNIC y no lo es**: el RDAP de
  APNIC devuelve un objeto `STUB` con país `ZZ` y sin titular, lo que invita a
  pensar en espacio huérfano o secuestrado. **No lo es.** El fichero de
  transferencias de APNIC registra el bloque como **transferido de Iseek
  Communications Pty Ltd (AU) a ARIN el 2020-12-22, destinatario `RL-859`**, y
  `RL-859` es **la misma entidad que ARIN da como registrante de `AS398465`,
  Rackdog, LLC**. El prefijo lo anuncia ese mismo ASN, **visto por 322 de 322
  pares de la colección de rutas**. Es decir: **espacio legítimamente
  transferido y anunciado por su titular. La hipótesis de secuestro queda
  refutada**, y conviene dejarla escrita porque era la lectura más natural de lo
  que devuelve el RDAP.

> **Y la decisión de higiene, que es la razón de que estas tres direcciones no
> entren todavía en los agregados planos.** Son **mando y control según una sola
> fuente**; esa fuente **sí las atribuye a `Aisuru-Proxy`** y su huella de
> servicio concuerda, pero **cuatro servicios independientes no tienen nada
> contra ellas** y **llevan menos de veinticuatro horas observadas**. La regla de
> `cti_enriquecer` aplicada aquí es la misma que en el resto de la cartera: **una
> coincidencia que remite a la fuente que ya citas no es una segunda fuente**, y
> aquí no hay ni coincidencia. **Publicarlas hoy para bloqueo sería elevar la
> confianza de una fuente única por el acto de citarla.** Van en `A.9` con tipo
> `artefacto`, confianza **moderada para la clase y baja para la atribución**, y
> acción permitida **vigilancia y caza retrospectiva, expresamente NO bloqueo**
> —con la regla de salida escrita: **si persisten a los catorce días pasan a
> `ipv4`**, porque entonces la objeción ya no será la evidencia sino la inercia.

### O-3.7.2 Un hallazgo sobre el enriquecimiento que se transfiere a toda la cartera

Al resolver el ASN de estas tres direcciones, **cinco fuentes dieron tres
respuestas distintas**:

| Fuente | Qué dijo | ¿Correcto? |
|---|---|---|
| `botnet.cl` | `AS398465` Rackdog, LLC · US | **sí** |
| Shodan | `AS398465` Rackdog, LLC | **sí** |
| RDAP de APNIC | objeto `STUB`, país `ZZ`, **sin titular** | inútil, no incorrecto |
| **AbuseIPDB** | **«CABLE & FIBERLINK», `cablefiberlink.com`** | **no** |
| **OTX** | **`AS701` Verizon** | **no** |

**Lo que lo resolvió no fue el RDAP, fue el fichero de transferencias
inter-RIR.** Y la causa del desorden es estructural: **cuando un prefijo cambia
de registro regional, el RIR de origen deja un objeto de relleno y los servicios
que cachean geolocalización o titularidad se quedan desactualizados durante
años.** La consecuencia práctica para esta cartera: **el campo «proveedor» de un
indicador no es verificable por consenso de servicios de enriquecimiento**, y
para cualquier dirección cuyo prefijo parezca de un RIR distinto del ASN que la
anuncia, **la comprobación barata es el fichero de transferencias del RIR de
origen**. Se consigna aquí y no sólo en el utillaje porque **dos de los cinco
servicios que esta cartera usa a diario se equivocaron en el mismo dato**.

## O-4. Nuestra exposición

| Si la organización es… | Exposición | Medida de mayor rendimiento |
|---|---|---|
| **Proveedor de acceso regional** | **Máxima, y como objetivo preferente** | Desvío preacordado y automático (`E-5.2`) + el feed BGP (`X-2`) |
| **Cliente de un proveedor regional** | **Alta e indirecta.** Nuestra disponibilidad depende de la capacidad de absorción de un tercero | Preguntar al proveedor si tiene desvío preacordado. **Es una pregunta contractual, no técnica** |
| **Operador de servicios expuestos a Internet** | Media | Los objetivos `/32` de la ventana indican ataques contra anfitriones concretos, no sólo contra redes |
| **Cualquiera con portales de acceso en Internet** | **Alta por la vía del proxy residencial, y probablemente no medida** | `E-3`: es un riesgo de autenticación. Segundo factor resistente a suplantación, no reputación de dirección |
| **Operadora de parque de dispositivos domésticos** *(trabajo remoto)* | Media | Los nodos de estas redes son enrutadores y decodificadores domésticos (`E-5.7`) |

## O-5. El feed BGP como activo defensivo, y sus límites

**Lo que hace:** anuncia **una ruta IPv4 `/32` por cada dirección de mando y control** listada, con el camino de sistemas autónomos formado por `AS64512` seguido del ASN de origen que el servicio registra. **No importa rutas del suscriptor**: es sólo de exportación. La acción de descarte la activa **únicamente** la comunidad `65535:666`; todas las comunidades `64512:*` son informativas.

**Lo que no hace, y hay que decirlo con claridad porque es la confusión más probable:**

| Expectativa | Realidad |
|---|---|
| «Me protege del DDoS» | **No.** Un agujero negro sobre el C2 **no absorbe un ataque entrante**. Lo que hace es impedir que **nuestros** nodos infectados reciban órdenes, y que nuestros usuarios alcancen esa infraestructura |
| «Sustituye al desvío de tránsito» | **No.** Son medidas de capas distintas y hacen falta las dos (`E-5.1` y `E-5.2`) |
| «Las rutas son seguras de descartar sin más» | **Con matiz.** Son `/32` de direcciones que la fuente clasifica como C2. El riesgo de falso positivo es bajo pero **no nulo**, y hay 12 direcciones en Latinoamérica y varias en nubes grandes. `X-2.3` da la política de importación conservadora |
| «Cubre el eje de proxy residencial» | **Sólo su control.** Descartar el C2 de un módulo de proxy no impide que tráfico de proxy residencial **llegue** a nuestros servicios desde nodos de terceros |

**Las comunidades, que son la parte más útil del diseño:**

| Comunidad | Significado | Uso recomendado |
|---|---|---|
| `65535:666` | **BLACKHOLE** (RFC 7999) | **La única que activa el descarte.** Requerida |
| `64512:1001` | Infraestructura de mando y control | Observabilidad |
| `64512:2001` | Fuente de inteligencia: `botnet.cl` | Trazabilidad del origen del dato |
| `64512:3001` | Visto hace **menos de 24 horas** | **Política selectiva: descartar sólo lo fresco** |
| `64512:3003` | Visto hace **más de siete días** | **Candidato a no descartar**, o a descartar con revisión |
| `64512:4001`…`4033` | **Identificador de familia** | Permite política por familia y medición propia |

> **Y el uso más interesante de las comunidades no es defensivo, es
> analítico.** Un suscriptor que reciba el feed completo con sus comunidades
> obtiene, sin pedir nada a nadie, **su propia serie temporal de la
> infraestructura de cada una de las 33 familias**: cuántas direcciones,
> cuándo aparecen, cuánto duran y en qué ASN. **Eso es exactamente la base de
> datos de este informe, y con una sesión BGP se tiene de forma continua en
> lugar de por instantáneas.** Es la recomendación de colección `G-2.1`.

## O-6. Cronología

<!-- cti:timeline -->

| Fecha | Acontecimiento |
|---|---|
| 2016 | Filtración del código de Mirai: base de casi todo lo que hay en este informe |
| 2025 (2S) | Aisuru se consolida como la mayor amenaza de DDoS del año según varios recuentos |
| 2025-11/12 | **Récord mundial atribuido a Aisuru/Kimwolf: 31,4 Tbps.** *Las fuentes discrepan en el mes* |
| 2026-01 | Google obtiene orden judicial para retirar dominios asociados a un proveedor de proxy residencial |
| 2026-01 | Krebs informa de que los operadores de Kimwolf tenían acceso al panel de control de BADBOX 2.0 |
| **2026 (1T)** | **Acción policial contra cuatro grandes redes de bots de IoT** — Aisuru, KimWolf, JackSkid, Mossad |
| 2026-02 | A10 mide **17.527 ataques en Brasil en una semana, ~99 % contra cinco ISP regionales de fibra** |
| 2026-03 | A10 analiza 498.163 ataques y describe el patrón de **ráfagas cortas repetidas en múltiples subredes** |
| 2026-04 | Krebs: actor brasileño con acceso de raíz a la infraestructura de una empresa de mitigación de DDoS |
| 2026-06 | Kaspersky descubre malware en unidades de cabecera de automóvil con fin de fraude publicitario y **red de proxy** |
| 2026 (3T) | Caída de los ataques sobre 1 Tbps de 805 a 251 respecto del trimestre anterior |
| 2026-09-22 | **Primera observación más antigua** entre las 573 direcciones del feed |
| 2026-10-05 → 10-18 | Enmudecen `KittyCattos`, `Wuming0`, `Tadashi`, `EZF3`, `FF1`, `Ouroboros`, `Kittenbotv18` |
| **2026-10-30 11:02** | **Último evento de `Cereal2`**, tras 395.887 acumulados. Hoy sin infraestructura |
| 2026-11-13 | **Aparecen 200 direcciones nuevas en el feed en un solo día** (`G-6`: adversario o colección) |
| **2026-11-18** | **HUMAN Security publica BADBOX 3.0**: módulos de proxy que inscriben dispositivos en **once** redes de proxy residencial |
| 2026-11-18 | **Aparecen otras 168 direcciones nuevas.** Dos días concentran 368 de las 573 |
| **2026-11-19** | **Medición propia**: 573 C2, 2.500 eventos, 176 pares BGP, 33 familias. Emisión de este informe |

## O-7. Hipótesis alternativas y pre-mortem

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| **H-1 — La asimetría objetivo/infraestructura es real** | **Retenida como principal.** Dos conjuntos de datos independientes dentro de la fuente, y corroboración externa del lado del objetivo por A10 | `Casi con certeza · ≥99 %` |
| **H-2 — El 85 % de proxy es un artefacto del clasificador** | **Rebajada en esta versión, y por un argumento que no teníamos al formularla.** Si la fuente etiquetara como «proxy» toda dirección cuyo binario no vio atacar, el reparto diría más de su método que del mundo. **Pero las dos clases de negocio no comparten ni un bloque `/24` de 206, y sólo 4 ASN de 57**: un error de etiquetado no produce huellas de alojamiento disjuntas, porque el etiquetado no sabe en qué bloque está la dirección. **Sigue retenida como limitación, con probabilidad menor** (§O-3.4) | `Poco probable · 20–45 %` |
| **H-3 — La concentración en Brasil es sesgo de observación de una fuente regional** | **Parcialmente retenida, y es el argumento más fuerte contra `KJ-4`.** Un servicio con 126 de 176 pares brasileños **podría ver mejor lo que pasa en Brasil**. **Mitigación:** A10 midió lo mismo sin ser una fuente regional. Pero no se puede descartar que la *proporción* esté inflada | `Posibilidad real · 40–60 %` |
| **H-4 — `Cereal2` fue desarticulada** | **Sin confianza.** Correlación temporal con una acción policial contra otras redes. **No hay ninguna fuente que lo afirme** y se consigna sólo para que nadie lo reabra como hecho | `Aprox. igual de probable · 40–60 %` |
| **H-5 — El cero solapamiento indica compartimentación real** | **Sin resolver, y es `G-1`.** Dos lecturas incompatibles, ninguna conclusión del informe apoyada en ella | `Aprox. igual de probable · 40–60 %` |
| **H-6 — Los picos del 13 y 18 de noviembre son actividad del adversario** | **Retenida con alternativa igual de fuerte.** 368 de 573 direcciones aparecen en dos días. Puede ser expansión de infraestructura **o** incorporación de familias nuevas al seguimiento de la fuente. **Es la pregunta de `G-6`, y es la misma de siempre: ¿la forma está en los datos o en la colección?** | `Aprox. igual de probable · 40–60 %` |

**Pre-mortem — si en seis meses este informe resulta equivocado, será por una de estas razones:**

1. **Porque alguien tomó las proporciones de una ventana de 97 minutos como la medida del fenómeno.** Es el riesgo 1 y el más probable, porque las cifras son concretas y se citan bien. **El 80,2 % es de hora y media de un jueves.**
2. **Porque la fuente clasifica de un modo que no entendimos**, y el hallazgo del 85 % de proxy era una propiedad de su etiquetado (`H-2`).
3. **Porque alguien ingirió los prefijos objetivo como indicadores y bloqueó redes de operadores brasileños legítimos.** Es el riesgo con consecuencia más grave y está contenido en `A.4` y `X-4`.
4. **Porque la fuente dejó de existir** y el informe se quedó sin base de datos renovable (`G-4`).
5. **Porque se leyó «número de eventos» como «intensidad del ataque».** La fuente **no publica volumen de tráfico**: un evento es una observación, no una magnitud.
6. **Porque se concluyó que Chile no está afectado** a partir de cero eventos en una ventana en la que tampoco había por qué verlos (`G-3`).

## O-8. Indicadores y señales de alerta temprana

| Señal | Qué indicaría | Dónde se ve |
|---|---|---|
| El contador acumulado de una familia secundaria crece un orden de magnitud en una semana | Promoción de familia residual a activa | Consulta por familia |
| Aparece una familia nueva en la matriz con infraestructura numerosa desde el primer día | **Posible sucesora de `Cereal2`**, o cambio de marca | Matriz + lista de C2 |
| Una dirección aparece con **dos comunidades de familia** | **Resolvería `KJ-9` en el sentido (a)** y sería una señal fuerte de vínculo entre operaciones | Comunidades del feed |
| Prefijos objetivo chilenos o argentinos en el flujo en vivo | **Desplazamiento regional del objetivo** (`E-4`) | Flujo con `family=all` |
| Caída brusca del número de pares BGP | Problema del servicio, o pérdida de confianza de los suscriptores | Tabla de clasificación |
| Un ASN concentrador pierde de golpe muchas direcciones | Efecto de una notificación de abuso: **mediría la palanca de `E-5.6`** | Lista de C2 por ASN |

---

# NIVEL TÁCTICO
### Para: Analistas de SOC, Ingeniería de detección, Operaciones de red · Horizonte: días

## T-1. Anatomía del ataque de pulso, que es la forma dominante y la que rompe la doctrina

<!-- cti:stages title="Lo que se observa en un pulso, y las dos únicas oportunidades de intervención" dwell="next" -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 01 · Reclutamiento | El nodo se infecta | Enrutador doméstico o decodificador Android · credencial por omisión o vulnerabilidad conocida · **propagación por ADB** en el caso de `KATARU` · el dueño no nota nada |
| Etapa 02 · Mando | El nodo recibe la orden | Conexión al C2 — **573 direcciones, 58 ASN, mediana de vida 5,2 días** · **Única oportunidad de intervención en red: el agujero negro del feed** (`X-2`) |
| Etapa 03 · Pulso | La ráfaga | **Mediana 5 segundos** · UDP en el 85 % · **hasta 11 objetivos simultáneos del mismo operador** · reparto por múltiples prefijos de la misma red |
| Etapa 04 · Repetición | El bucle | **25,6 eventos/min sostenidos** en la ventana medida · el mismo operador recibe cientos de pulsos en una hora · **el efecto es acumulativo, no puntual** |

**Por qué el pulso es un problema distinto del DDoS grande, en tres puntos:**

1. **No dispara los umbrales pensados para picos sostenidos.** Cinco segundos de tráfico elevado, repetidos, pueden quedar por debajo de una media de cinco minutos y no activar nada, mientras degradan el servicio de forma continua.
2. **Agota la mitigación en lugar de superarla.** Un sistema de desvío que tarda decenas de segundos en converger **nunca llega a tiempo**, y si converge, el ataque ya terminó y el desvío se retira justo antes del siguiente pulso. **El adversario no necesita ganar: necesita que el defensor oscile.**
3. **Y reparte el daño entre prefijos para diluir la señal.** El ejemplo medido es nítido: **once eventos en el mismo segundo contra seis prefijos distintos de `Halver LTDA`**. Visto por prefijo, cada uno recibe poco; visto por operador, es un ataque.

> **La consecuencia de doctrina, y es la recomendación más concreta de este
> informe para un operador de red:** la detección tiene que estar
> **agregada por operador o por bloque, no por prefijo**, y la mitigación
> tiene que ser **preacordada y automática**, porque **no existe un
> procedimiento humano que opere en cinco segundos**. Es también la
> recomendación de A10 para este mismo fenómeno: acordar el desvío con el
> tránsito **antes** del ataque, no durante.

## T-2. Mapa MITRE ATT&CK

<!-- cti:matrix -->

| Táctica | ID | Técnica | Procedimiento observado |
|---|---|---|---|
| Desarrollo de recursos | T1583.003 | Acquire Infrastructure: Virtual Private Server | 625 direcciones de C2, con **62,9 % en cinco proveedores**. **Y el procedimiento medido en la versión 1.3:** `SZJL` **traslada 92 direcciones a un proveedor nuevo en un día** mientras vacía la mitad del anterior (`O-3.6`) |
| Desarrollo de recursos | T1584.005 | Compromise Infrastructure: Botnet | El propio objeto del informe: parque de enrutadores y dispositivos Android comprometidos |
| Desarrollo de recursos | T1583.005 | Acquire Infrastructure: Botnet | **El eje de alquiler**: las «redes» de proxy residencial que se venden por suscripción (`E-3`) |
| Acceso inicial *(al nodo)* | T1078.001 | Valid Accounts: Default Accounts | Vía clásica de reclutamiento en IoT. **Declarada por la fuente, no observada por nosotros** |
| Ejecución | T1059.004 | Command and Scripting Interpreter: Unix Shell | Declarado para `Potassium`, `EZF3`, `Ouroboros`, `Tadashi`, `KATARU`, `HelloBot`, `Sarbot`, `Supercrone` |
| Movimiento lateral | **T1021** | Remote Services | **`KATARU`: propagación por ADB**, el puente de depuración de Android. **Corregido en la versión 1.3:** las versiones 1.0–1.2 citaban `T1021.001`, que es *Remote Desktop Protocol* y no corresponde a ADB |
| Mando y control | T1071.001 | Application Layer Protocol: Web Protocols | `Titan` usa **túnel de control por WebSocket**; `FF1` inunda con HTTP/2 sobre TLS |
| Mando y control | T1095 | Non-Application Layer Protocol | **`Aigogo` usa DTLS**; varias familias usan GRE como portador de UDP |
| Mando y control | T1572 | Protocol Tunneling | `CXFJ` y `SZJL`: relé de TCP y UDP por canales de retrollamada |
| Mando y control | T1090.002 | Proxy: External Proxy | **El eje entero de proxy residencial: 556 de 625 direcciones, el 89,0 %** —recomputado el 22-11 familia a familia—. Huella observada desde fuera: **abanico de puertos consecutivos, cada uno con reto `407` y reino propio** — `Proxy`, `proxy`, `Restricted` y, sin familia conocida, `atlas` (`O-3.7`) |
| Mando y control | T1105 | Ingress Tool Transfer | `Eclipse`: orden `UPDATE` que descarga y ejecuta una URL suministrada. `EZF3`: guion horario |
| Impacto | **T1498.001** | **Network Denial of Service: Direct Network Flood** | **La técnica central**: UDP, TCP y GRE contra prefijos de operadores |
| Impacto | T1499.002 | Endpoint DoS: Service Exhaustion Flood | `Liso` «TCP session holding»; `Cereal2` «session-pool flood» |
| Impacto | T1496 | Resource Hijacking | **`Manta`: descarga y ejecución de un minero** — declarado por la fuente |

**Dos observaciones sobre este mapa.** La primera: **la mitad de las técnicas son de desarrollo de recursos y de mando y control, no de impacto.** Eso es coherente con `KJ-2` y es lo que diferencia este ecosistema de un actor de intrusión: casi todo su esfuerzo está en **tener** la red, no en usarla. La segunda: **las técnicas de acceso inicial al nodo se consignan como declaradas por la fuente y no observadas por nosotros**, porque no tenemos ninguna muestra ni ningún dispositivo comprometido a la vista.

## T-3. Dónde atacamos en la Pirámide del Dolor

<!-- cti:pyramid -->

| Nivel | Indicador | Valor en este expediente |
|---|---|---|
| Trivial | Valores de hash | **Nulo.** No tenemos muestras, y la fuente no publica hashes |
| Fácil | Direcciones IP | **Alto y operacionalizable, excepcionalmente, pero menos de lo que decía la versión 1.0.** El 19-11 eran 573 direcciones con mediana de vida de **5,2 días** y **el 91 % vistas en las últimas 24 h**. **Remedido el 22-11: de 625 direcciones sólo el 78,2 % se vio ese día** —116 llevaban un día sin verse y 20 llevaban dos—, es decir **un 21,8 % que el feed publica sin haber reobservado**. Caducan rápido y **el feed las renueva solo**, pero **renovar no es reverificar**: el valor sigue estando en la suscripción y no en la lista, con la salvedad de `X-2.3` |
| Simple | Nombres de dominio | **Nulo.** La fuente publica direcciones, no dominios |
| Molesto | Artefactos de red / anfitrión | **Alto.** El perfil de pulso —UDP a puerto **65535**, duración de 5 s, múltiples prefijos del mismo operador en el mismo segundo— es un artefacto de red **estable y propio de la familia** |
| Irritante | Herramientas | **Medio.** La matriz de capacidades por familia es, en la práctica, un catálogo de herramientas. **No verificado por nosotros** |
| Difícil | TTP | **El nivel que de verdad importa aquí:** el **modelo de negocio de pulso repetido contra operadores regionales**, y el de **alquiler de ancho de banda residencial**. Ninguno de los dos cambia porque bloqueemos direcciones |

> **La observación que este expediente añade a la pirámide, y contradice su
> lectura habitual:** normalmente se desaconseja operar en el nivel de las
> direcciones IP porque caducan. **Aquí no, y por una razón estructural: la
> caducidad la gestiona la fuente.** Una lista de 573 direcciones descargada
> hoy es basura en dos semanas; **una sesión BGP con el mismo origen es un
> control permanente** cuyo contenido se renueva sin intervención. **Lo que
> cambia el valor del indicador no es el indicador, es el mecanismo de
> entrega.**

## T-4. Hipótesis de caza

<!-- cti:accordion critical="^(H-1|H-2)\b" regional="^(H-5|H-6)\b" -->

| # | Hipótesis | Cómo se comprueba | Qué significa un positivo |
|---|---|---|---|
| **H-1** | **Algún anfitrión de nuestra red habla con una de las 573 direcciones de mando y control** | Cruzar la lista de C2 contra registros de flujo de 30 días. **Es la caza de mayor rendimiento del informe y se hace en una tarde** | **Tenemos un nodo de red de bots dentro.** No es un incidente de DDoS: es un dispositivo comprometido que obedece a un tercero |
| **H-2** | **Algún dispositivo de nuestra red resuelve o conecta a las direcciones del eje de proxy residencial** (las 487) | Mismo cruce, restringido a las familias de proxy | **Peor que H-1 en un sentido**: nuestro ancho de banda y nuestra dirección se están vendiendo, y nuestra reputación de IP es la que se gasta |
| **H-3** | **Recibimos tráfico de autenticación desde proxy residencial** | Buscar en los portales de acceso: direcciones residenciales de operadores con los que no tenemos relación, agente de usuario coherente, baja tasa de éxito y alta dispersión de direcciones por cuenta | Las defensas por reputación y geografía no nos protegen (`E-3`) |
| **H-4** | **Nuestros prefijos aparecen como objetivo en el flujo en vivo de la fuente** | Consulta del flujo con filtro de nuestro ASN. **Comprobación directa y gratuita** | Nos están atacando ahora y quizá no lo habíamos visto, porque el pulso no dispara umbrales |
| **H-5** | **Hay pulsos cortos repetidos contra nuestros prefijos que no disparan nuestros umbrales** | Agregar por **operador y por bloque**, no por prefijo, con ventanas de 10 s | `T-1`: el ataque que no vemos porque lo medimos mal |
| **H-6** | **Tenemos enrutadores o decodificadores domésticos en el perímetro del trabajo remoto con administración expuesta** | Inventario + barrido de los rangos de acceso remoto | Es el parque del que se nutren estas redes, **y el mismo que `CTI-2026-037` describió como objetivo estatal** |
| **H-7** | **Algún proveedor nuestro de tránsito o de alojamiento figura entre los cinco ASN concentradores** | Cruzar `A.3` con el inventario de proveedores | Tenemos una vía de notificación de abuso **con relación contractual**, que es la más eficaz que existe |
| **H-8** | **Hay sesión BGP con el feed y la política de importación es correcta** | Revisar que sólo se acepta `65535:666` y se rechaza el resto (`X-2.3`) | Un feed mal importado puede **aceptar rutas que no debía** |

## T-5. Brechas de visibilidad que hay que cerrar primero

| # | Brecha | Por qué duele aquí | Cómo se cierra |
|---|---|---|---|
| **V-1** | **Sin registros de flujo retenidos 30 días** | Sin ellos no se puede ejecutar `H-1` ni `H-2`, que son las dos cazas de mayor rendimiento | Retención de NetFlow/IPFIX en el borde |
| **V-2** | **Detección de DDoS agregada por prefijo y no por operador** | `T-1`: el pulso reparte el daño para quedar por debajo de los umbrales | Reagregar y bajar la ventana a 10 s |
| **V-3** | **Sin visibilidad del tráfico saliente de la red de invitados y de IoT** | El nodo de red de bots suele estar ahí, y suele ser el segmento con menos registro | Registro de flujo también en esos segmentos |
| **V-4** | **Sin medición de reputación de origen en los portales de acceso** | `H-3`: el proxy residencial entra por la puerta y con buena reputación | Métrica de dispersión de direcciones por cuenta y de ASN de origen |
| **V-5** | **Desvío de tránsito sin acuerdo previo y con activación manual** | `KJ-5`: cinco segundos. Es inútil por diseño | Contractual, no técnico (`E-5.2`) |

---

# NIVEL TÉCNICO
### Para: Ingeniería de red, automatización, TIP/SIEM · Vida útil: días–semanas

## X-1. El feed: parámetros de sesión

| Parámetro | Valor |
|---|---|
| Punto de presencia Chile | `rbl1.botnet.cl` → `38.7.199.217` *(publica A y AAAA)* |
| Punto de presencia São Paulo | `rbl2.botnet.cl` → `45.171.231.57` *(infraestructura cedida por un tercero según la propia página)* |
| Sistema autónomo remoto | **`AS64512`** — ASN privado |
| Tipo de sesión | **eBGP multisalto** |
| Dirección | **Sólo conexión: la inicia el suscriptor.** El feed **no importa** rutas del suscriptor |
| Familia de direcciones | **IPv4** en el servicio actual; ambos nombres publican A y AAAA |
| Contenido | **Una ruta `/32` por dirección de C2**, con camino `AS64512` + ASN de origen registrado |
| Recomendación del operador | **Establecer sesión con los dos extremos** para redundancia de camino |

## X-2. Consumo del feed

### X-2.1 Política de importación — el principio que no hay que romper

La página del feed es explícita en algo que conviene repetir: **sólo `65535:666` activa el descarte; todas las comunidades `64512:*` son informativas.** De ahí la política correcta, en dos reglas y en este orden:

```
1) si las comunidades BGP incluyen 65535:666  ->  marcar como agujero negro y ACEPTAR
2) en cualquier otro caso                     ->  RECHAZAR
```

La segunda regla es la importante y es la que se olvida: **una sesión de feed de terceros debe rechazar por omisión todo lo que no se esté esperando.** Sin ella, un error del origen —o un compromiso del origen— puede inyectar rutas en nuestra tabla.

### X-2.2 Plantilla de MikroTik RouterOS v7, que es la del fabricante más extendido en la región

```
# 1 · Política de entrada: marcar el agujero negro y rechazar el resto
/routing/filter/rule
add chain=BOTNET-CL-BGP-IN \
    rule="if (bgp-communities includes 65535:666) { set blackhole yes; accept; }"
add chain=BOTNET-CL-BGP-IN rule="reject;"
```

El sitio publica además la creación de las dos conexiones eBGP multisalto de sólo conexión con la política anterior adjunta, y plantillas equivalentes para **Juniper Junos OS, Huawei VRP y Cisco IOS / IOS XE**. **Se recomienda tomarlas del propio sitio** en lugar de transcribirlas aquí, por la razón de higiene de `CTI-2026-032`: una configuración mal copiada no falla de forma visible, y un carácter de más en una política de importación de BGP tiene consecuencias peores que un indicador inútil.

### X-2.3 Política conservadora para una primera adopción

Para quien no quiera descartar 573 rutas el primer día, las comunidades permiten una adopción por fases **sin perder la mayor parte del beneficio**:

| Fase | Política | Cobertura | Riesgo |
|---|---|---|---|
| **1 · Observar** | Aceptar e instalar **sin** marcar agujero negro; medir cuántos de nuestros flujos tocan esas rutas | 100 % de visibilidad, 0 % de bloqueo | **Nulo.** Y responde `H-1` sin esperar a tener registros de flujo históricos |
| **2 · Descartar lo fresco** | Descartar sólo lo que lleve `64512:3001` *(visto hace menos de 24 h)* | La infraestructura activa | Mínimo |
| **3 · Descartar todo menos lo viejo** | Descartar todo salvo `64512:3003` *(más de 7 días sin verse)* | Casi total | Bajo |
| **4 · Completo** | Descartar todo lo que lleve `65535:666` | Total | Bajo, con revisión de falsos positivos. **Y una salvedad medida en la versión 1.3:** descarta también lo que la fuente ya no reobserva —el 21,8 % del feed el 22-11— |

> **La fase 1 es la recomendación de este informe para empezar hoy**, porque
> **convierte el feed en un sensor antes de convertirlo en un control**, y
> porque un operador que mide primero puede justificar el bloqueo después con
> datos propios en lugar de con la palabra de un tercero.

> **Y una consecuencia que la versión 1.0 no podía ver, porque hacía falta un
> segundo punto en el tiempo** *(añadida en la versión 1.3)*. La proporción de
> direcciones vistas en las últimas 24 horas **cayó del 91 % al 78,2 % entre el
> 19 y el 22 de noviembre**: el 21,8 % restante son rutas que el feed sigue
> anunciando sin haberlas reobservado. **No hay que leerlo como que el adversario
> se apagó** —de ocho direcciones muestreadas con última observación del 20 o del
> 21, **las ocho seguían con servicio activo en un escáner independiente el
> 22**—, sino como **pérdida de cobertura del sensor**. De ahí la revisión de la
> recomendación: **las comunidades de antigüedad `64512:300x` dejan de ser una
> comodidad de adopción y pasan a ser un control de calidad.** Quien opere en
> fase 4 debería **marcar, medir y revisar** lo que llega con `64512:3003`
> —visto hace más de siete días— en lugar de descartarlo sin más, porque en ese
> tramo se acumula justamente lo que la fuente ha dejado de mirar.

## X-3. Detección del pulso

### X-3.1 La agregación correcta

```
# Pseudocódigo. La clave es la ventana corta y la agregación por BLOQUE, no por IP.
ventana = 10 segundos
para cada (bloque_destino /24 o superior) en flujos_entrantes:
    paquetes = suma(paquetes en ventana)
    si paquetes > umbral_bloque(bloque) y duracion_rafaga < 15 s:
        registrar PULSO(bloque, ventana, protocolo, puerto)

# Y la señal que de verdad distingue este patrón de un pico cualquiera:
si cuenta_distinta(bloques_destino con PULSO en el mismo segundo) >= 3:
    alertar "ATAQUE DE PULSO DISTRIBUIDO POR SUBREDES"
```

**La segunda condición es la que importa** y es la que el expediente permite escribir: el adversario reparte el pulso entre **varios prefijos del mismo operador en el mismo segundo** —hasta once en nuestra medición—, de modo que **la simultaneidad entre bloques es una señal más limpia que el volumen en cualquiera de ellos.**

### X-3.2 Artefactos de red del perfil dominante

| Artefacto | Valor observado | Nota |
|---|---|---|
| Protocolo | **UDP en el 85,3 %** (2.133 de 2.500), TCP en el 14,7 % | |
| Puerto de destino | **`65535` en el 79,6 %** de los eventos con puerto declarado | **Puerto no asociado a ningún servicio legítimo.** Es la señal más barata del expediente |
| Duración | **5 s en el 79,2 %**; 60 s en el 20,2 % | Bimodal: pulso y ráfaga corta |
| Simultaneidad | 23,2 % de los segundos con ≥2 eventos | Máximo 11 |
| GRE | Presente como portador de UDP en varias familias | Un descarte de GRE no solicitado en el borde es barato |

## X-4. Higiene: la advertencia inversa de `CTI-2026-040`

> ⚠ **Esta es la advertencia operativa más importante del informe.**
>
> Esta fuente publica **dos clases de direcciones que no se deben confundir
> nunca**, y la confusión no es hipotética: están en el mismo servicio, con
> interfaces parecidas, y una de las dos es una lista de víctimas.
>
> | Clase | Qué es | Tipo en `ioc_index.csv` | Acción |
> |---|---|---|---|
> | **Direcciones de mando y control** (573) | Infraestructura adversaria clasificada por la fuente | **`ipv4`** — **sí** entra en los agregados planos | Bloqueo, con la política de `X-2.3` |
> | **Prefijos y ASN objetivo** (258 prefijos, 69 ASN) | **Redes de operadores brasileños legítimos que están siendo atacadas** | **`artefacto`** y **`asn`** — **no** entran en los agregados | **NUNCA bloquear.** Se consignan para medir victimología |
>
> **Una ingesta automática que tome «las direcciones de botnet.cl» sin
> distinguir las dos vistas bloqueará a `Halver LTDA`, `EGR NET`, `Speednet`,
> `INETVIP` y otros trece operadores brasileños**, es decir, a los atacados. Y
> el fallo sería silencioso: el bloqueo funcionaría perfectamente, y el
> síntoma aparecería días después como pérdida de conectividad con clientes o
> proveedores en Brasil.
>
> **`CTI-2026-040` tuvo que advertir de lo contrario** —seis direcciones de
> banda ancha latinoamericana dentro de un aviso oficial de indicadores, que
> no debían bloquearse—. **Aquí el riesgo está en el otro sentido y es
> mayor**, porque la vista de objetivos es la más llamativa del servicio y la
> que un recolector automático encontrará primero.

## X-5. Mitigaciones de configuración con efecto directo

| # | Medida | Dónde | Efecto | Coste |
|---|---|---|---|---|
| **X-5.1** | **Desvío ante DDoS preacordado con el tránsito, con activación automática** | Contrato + borde | **El único control que opera en la escala de `KJ-5`** | Medio |
| **X-5.2** | **Sesión BGP con el feed, fase 1 (observar)** | Borde | Convierte el feed en sensor; responde `H-1` sin histórico | **Bajo** |
| **X-5.3** | **Agregación de detección por bloque con ventana de 10 s** | Detección | Hace visible el pulso (`X-3.1`) | Bajo |
| **X-5.4** | **Descarte de GRE no solicitado en el borde** | Borde | Elimina un portador usado por varias familias | Bajo |
| **X-5.5** | **Bloqueo de salida a UDP/65535 desde segmentos de usuario e IoT** | Borde | **No defiende de recibir el ataque: impide participar en él** si tenemos nodos infectados | Bajo |
| **X-5.6** | **Segundo factor resistente a suplantación en todo portal de acceso** | Identidad | **La única defensa real contra el eje de proxy residencial** (`E-3`, `H-3`) | Medio |
| **X-5.7** | **Segmentar y registrar la red de invitados y de IoT** | Red | Es donde vive el nodo y donde menos se mira (`V-3`) | Medio |
| **X-5.8** | **Inventario y endurecimiento del parque de enrutadores domésticos del trabajo remoto** | TI | Corta el reclutamiento en la etapa 01 | Medio |

---

## 14. Brechas de inteligencia y requisitos de colección

| # | Brecha | Impacto | Cómo se cierra | Prioridad |
|---|---|---|---|---|
| **G-1** | **No sabemos si el cero solapamiento de `KJ-9` es del ecosistema o del clasificador** | **Deja sin resolver el único hallazgo estructural que podría medir vínculos entre operaciones** | **Un correo al operador de la fuente.** Es la pregunta más barata y más rentable del expediente | **1** |
| **G-2** | **Todas las proporciones del flujo salen de dos ventanas de la MISMA TARDE** | Riesgo 1 del pre-mortem. **Parcialmente cerrada en la versión 1.1**: la segunda ventana sostuvo las proporciones dentro de 3,5 puntos (`O-3.5`). **Lo que sigue abierto es la variación por hora del día y por día de la semana** | Continuar el muestreo durante días, no horas. **Y con una sesión BGP en fase 1 se obtiene gratis para la infraestructura** (`G-2.1`) | **1** |
| **G-2.1** | No tenemos serie temporal de la infraestructura | Impide medir la vida real de las direcciones y el efecto de las notificaciones de abuso. **Parcialmente cerrada en la versión 1.3**: la remedición del 22-11 contra las cifras del 19-11 dio el primer punto de serie y **produjo `KJ-11`** — tres días bastaron para detectar una migración completa de proveedor (`O-3.6`). **Lo que sigue abierto es la serie continua**, que un delta de tres días no sustituye | **Sesión BGP en fase 1**: da la serie de forma continua y gratuita (`O-5`). **Y, mientras no la haya, remedir los agregados de `A.2` y `A.3` y no sólo leer el delta diario** | 2 |
| **G-3** | **Cero eventos contra Chile en la ventana, y no sabemos si es una ausencia o un artefacto** | Podríamos estar declarando una ausencia no medida (`E-2.2`) | El mismo muestreo de `G-2`, con filtro por ASN propios | 2 |
| **G-4** | **La fuente no publica identificación de su entidad operadora ni contacto** | **Riesgo de concentración**: si cierra, este informe pierde su base de datos | Contacto directo; y evaluar una segunda fuente de telemetría | 2 |
| **G-5** | **No tenemos expediente del ecosistema de proxy residencial** | Es el 85 % de la infraestructura y el eje que más nos afecta como organización | Expediente propio partiendo de BADBOX 3.0 y de las siete familias de `O-1` | **1** |
| **G-6** | **368 de 573 direcciones aparecen en dos días (13 y 18 de noviembre) y no sabemos por qué** | Puede ser expansión del adversario o incorporación de familias al seguimiento | Preguntar a la fuente; o detectarlo en la serie de `G-2.1` | 2 |
| **G-7** | **`Potassium` tiene 304.258 eventos y ningún expediente** | Es la tercera familia del ecosistema y la segunda activa | Expediente propio | 2 |
| **G-8** | **No verificamos la matriz de capacidades** | Afirmaciones como el minero de `Manta` o el ADB de `KATARU` son de la fuente | Muestras, o un análisis de proveedor independiente | 3 |
| **G-9** | **No sabemos el volumen de tráfico de ningún ataque** | Impide cualquier juicio de magnitud | La fuente no lo publica. Requiere telemetría de operador | 3 |
| **G-12** | **`Eclipse` se ha quedado sin ninguna dirección viva, y con ella desaparece el único solapamiento entre dos familias de DDoS que `KJ-9` ofrecía** | **Toca a `KJ-9` y a `A.2`**: el bloque `141.98.10.0/24` aloja hoy **cinco direcciones y las cinco son de `Aisuru-DDoS`**; la coincidencia con `Eclipse` **deja de ser observable**, de modo que la conjetura de §O-3.4 sobre `Eclipse` como herramienta o prueba del mismo entorno **ya no se puede comprobar ni refutar con esta fuente**. El vínculo `Hotota`↔`LinkFog` en seis bloques no está afectado | **Serie temporal** (`G-2.1`): sólo un histórico de la infraestructura dice si `Eclipse` se apagó, se renombró o nunca tuvo infraestructura propia. **Y, mientras no la haya, no citar el solapamiento DDoS como observación vigente** | 2 |
| **G-11** | **No sabemos si las direcciones de `Hotota` y `LinkFog` dentro de un mismo `/24` están asignadas en lote** | Decidiría si el vínculo de seis bloques es un operador común o una coincidencia de proveedor (`O-3.4`) | Análisis de contigüidad sobre la lista que ya tenemos, con un criterio de «mismo lote» establecido antes de mirar | 2 |
| **G-10** | **Sin telemetría propia** | Limitación estructural de toda la cartera | Registros de flujo retenidos (`V-1`) | 2 |

**Disparadores de reevaluación.** `I-1`: una dirección con dos comunidades de familia —resolvería `G-1`—. `I-2`: aparición de prefijos chilenos o argentinos en el flujo —`E-4`—. `I-3`: una familia nueva con infraestructura numerosa desde el primer día —posible sucesora de `Cereal2`—. `I-4`: caída brusca de los pares BGP o indisponibilidad del servicio —`G-4`—. `I-5`: que el muestreo longitudinal desmienta la proporción brasileña —`G-2`—. `I-6`: que un ASN concentrador pierda de golpe muchas direcciones —mediría la palanca de `E-5.6`—. **CUMPLIDO el 22-11-2026, y con el resultado contrario al previsto: `AS45102` perdió 16 direcciones y `SZJL` las reconstituyó —ampliadas— en `AS150436` en un día** (`KJ-11`, `O-3.6`). **El disparador se reformula:** lo que hay que vigilar no es que un ASN se vacíe, sino **que el recuento total de direcciones de la familia baje**, porque sólo eso distingue remediación de migración. `I-7`: **aparición de la huella `x-proxy-agent: atlas` en una dirección atribuida a una familia distinta de `Aisuru-Proxy`**, que indicaría software de proxy compartido entre operaciones —o en una cuarta dirección del mismo conjunto, que mediría su crecimiento—. `I-8`: **que `Eclipse` recupere infraestructura viva**, que reabriría el único solapamiento entre dos familias de DDoS y resolvería `G-12`. `I-9`: **que el recuento total de `SZJL` baje de 115**, que sería la primera señal de remediación real y no de migración, y la única métrica que `I-6` reformulado acepta.

---

# ANEXOS

## Anexo A — Indicadores, con su valoración y su acción permitida

> **Lea `A.4` antes de ingerir nada de este anexo.** Contiene la única lista de
> este informe que **no debe bloquearse jamás**, y es la que un recolector
> automático encontrará primero.

### A.1 — El patrón de red del pulso · **el indicador más duradero del expediente**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| pattern | **UDP con destino al puerto `65535`** | **La señal más barata de todo el informe.** Presente en el 79,6 % de los eventos con puerto declarado. El `65535` **no corresponde a ningún servicio legítimo**: es el último puerto del espacio y aquí funciona como valor por omisión del constructor del ataque. Un solo filtro lo ve | **Alta como señal de familia** | **Sin caducidad mientras el constructor no cambie su valor por omisión** | **Detección y, en salida desde segmentos de usuario e IoT, bloqueo** (`X-5.5`) |
| pattern | **Ráfagas de ~5 segundos repetidas, contra el mismo destino o el mismo operador** | El modo normal de operación: **1.979 de 2.500 eventos duraron 5 s**. **Y es el patrón que los umbrales de media móvil de cinco minutos no ven**: hay que medir en ventanas de 10 s | **Alta** | Sin caducidad como método | **Detección con reagregación** (`X-3.1`). No alerta por sí sola |
| pattern | **Dos o más prefijos del MISMO operador atacados en el mismo segundo** | **La señal discriminante del expediente, y la que menos organizaciones tienen.** 23,2 % de los segundos con actividad; **máximo de once eventos simultáneos contra seis prefijos de un mismo operador**. Visto por prefijo es poco; visto por operador es un ataque | **Alta** | Sin caducidad | **Alerta** (`X-3.1`). Requiere agregar por bloque u operador, no por prefijo |
| pattern | **GRE no solicitado encapsulando UDP** | Declarado por la fuente en `Liso`, `Yerco`, `SixSayven`, `MINIv3`, `Kyorij` y `Supercrone`. Un descarte en el borde es barato y sin efecto colateral si no se usa GRE legítimamente | Media | Sin caducidad | **Bloqueo en el borde** (`X-5.4`) |
| pattern | **Objetivos `/32` individuales mezclados con prefijos de operador** | El 13,1 % de los objetivos de `Liso` son `/32`: **anfitriones concretos, no redes**. Compatible con ataque por encargo contra servidores de juego alojados en esas redes (`E-2.1`) | Media | Sin caducidad | **Contexto de investigación**, no detección |

### A.2 — Bloques concentradores de infraestructura · **el pivote de caza correcto**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| artefacto | **`43.117.72.0/24`** | **43 direcciones de `SZJL`** en un solo bloque, en `AS45102`. El bloque entero es infraestructura de una familia de proxy | Alta | **Volátil: revisar en 14 días** | **Caza y vigilancia.** Ver nota de higiene de `A.8` sobre por qué no va como `ipv4` |
| artefacto | **`207.174.105.0/24`** | 32 direcciones de `Aigogo`, `AS835` | Alta | Volátil | Caza y vigilancia |
| artefacto | **`66.92.19.0/24`** | **32 direcciones y TRES familias: `CXFJ`, `Hotota`, `LinkFog`**, `AS62610`. Uno de los doce bloques compartidos (`O-3.4`) | Alta | Volátil | **Caza prioritaria**: es el bloque de mayor densidad y de mayor valor analítico |
| artefacto | **`74.119.149.0/24`** | 26 direcciones de `Aigogo`, `AS835` | Alta | Volátil | Caza y vigilancia |
| artefacto | **`185.91.127.0/24`** | 24 direcciones de `Aigogo`, `AS49581` | Alta | Volátil | Caza y vigilancia |
| artefacto | **`66.92.17.0/24`** | **22 direcciones y tres familias**: `CXFJ`, `Hotota`, `LinkFog`, `AS62610` | Alta | Volátil | Caza prioritaria |
| artefacto | **`141.98.10.0/24`** | **6 direcciones, `Aisuru-DDoS` y `Eclipse`**, `AS209605`. **El único solapamiento entre dos familias de DDoS** (`O-3.4`) | Alta como observación; **baja** como vínculo | Volátil | **Caza y requisito de colección** (`G-11`) |
| artefacto | **`199.190.45.0/24` · `98.96.225.0/24` · `98.96.240.0/24` · `107.151.209.0/24` · `128.14.145.0/24` · `69.165.76.0/24`** | **Los seis bloques donde coinciden `Hotota` y `LinkFog`** — el vínculo más fuerte entre dos familias que este informe ofrece. Todos en `AS62610` | Alta como observación; **moderada** como vínculo | Volátil | **Caza y `G-11`** |

### A.3 — Sistemas autónomos concentradores · **la palanca no técnica**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| asn | **`AS62610`** — Zenlayer Inc | **147 de 573 direcciones: el 25,7 % de toda la infraestructura del ecosistema en un solo sistema autónomo.** Y **once de los doce bloques compartidos** están aquí. Perfil: proxy residencial, bloques enteros | **Alta** | Estructural | **Notificación de abuso documentada** (`E-5.6`). **No bloquear el ASN**: es un proveedor legítimo con clientes legítimos |
| asn | **`AS835`** — GoCodeIT Inc | 58 direcciones. Perfil: proxy (`Aigogo`) | Alta | Estructural | Notificación de abuso |
| asn | **`AS45102`** — Alibaba (US) Technology | 45 direcciones. Perfil: proxy (`SZJL`) | Alta | Estructural | Notificación de abuso |
| asn | **`AS49581`** — Tube-Hosting | 42 direcciones. Perfil: proxy (`Aigogo`) | Alta | Estructural | Notificación de abuso |
| asn | **`AS63199`** — CDS Global Cloud | 30 direcciones. Perfil: proxy | Alta | Estructural | Notificación de abuso |
| asn | **`AS14061`** — DigitalOcean | **30 direcciones, y es el primero del eje de DDoS**, no del de proxy. Repartido en al menos cuatro países | Alta | Estructural | Notificación de abuso. **Proveedor con proceso de abuso maduro: es el más probable de responder** |
| asn | **`AS209605`** — UAB Host Baltic · **`AS131366`** — Lanit Technology · **`AS403005`** — Blatant Technologies | 6, 6 y 11 direcciones. **Perfil de DDoS**: proveedores pequeños, unidades sueltas | Alta | Volátil | Notificación de abuso, con expectativa baja |

> **Los cinco primeros concentran 322 direcciones, el 56,2 %.** Es la cifra que
> convierte una lista de 573 indicadores en **cinco conversaciones**, y es la
> misma estructura de concentración que `CTI-2026-018` encontró en el abuso de
> dominios: **el problema tiene nombres propios y es, en principio, remediable
> por política de proveedor.**

### A.4 — Prefijos y ASN OBJETIVO · ⚠ **NO BLOQUEAR BAJO NINGUNA CIRCUNSTANCIA**

<!-- cti:note type="warn" -->

> ⚠ **Estos son los atacados.** Son redes de **operadores de fibra brasileños
> legítimos**, y se consignan aquí **únicamente para medir victimología y para
> que quien tenga relación comercial con ellos sepa que están bajo ataque**.
> Van con tipo `artefacto` y `asn` **para que no entren en los agregados
> planos**. Bloquearlas produciría pérdida de conectividad con clientes y
> proveedores en Brasil, y el fallo sería silencioso durante días.

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| asn | **`AS274564`** — Halver LTDA (BR) | **La red más atacada de la ventana: 550 de 2.500 eventos.** Y el caso del ataque simultáneo a seis de sus prefijos en un mismo segundo | Alta | 60 días | **SÓLO victimología.** **NUNCA bloqueo** |
| asn | **`AS263415`** — EGR NET · **`AS52532`** — Speednet · **`AS264886`** — GD NET · **`AS263994`** — Fullnet · **`AS263623`** — GOX · **`AS53072`** — INETVIP · **`AS52947`** — PARAOPEBANET · **`AS266498`** — UNIVERSO FIBER · **`AS267357`** — Livenet · **`AS271252`** — BHNET · **`AS270641`** — YAS · **`AS273350`** — Gns Telecom · **`AS264862`** — TRIANGULO NET · **`AS270336`** — Careassunet · **`AS268568`** — IMPLANTAR · **`AS267158`** — MG NET · **`AS266641`** — Lavrasnet (todos BR) | **Diecisiete operadores regionales brasileños entre los más golpeados, y ningún operador nacional.** Es la base de `KJ-4`, corroborada independientemente por A10 nueve meses antes | Alta | 60 días | **SÓLO victimología.** **NUNCA bloqueo** |
| asn | **`AS201106`** — Spartan Host Ltd (US) | 231 eventos: **el único objetivo no brasileño relevante de `Liso`**, con prefijos `/32` individuales. Perfil de alojamiento de servidores de juego | Alta | 60 días | SÓLO victimología |
| cartera | **258 prefijos objetivo distintos**, no transcritos aquí | **Decisión de higiene deliberada.** Transcribir 258 prefijos de víctimas en un documento de indicadores **maximiza el riesgo de ingesta errónea** sin aportar nada: quien necesite la lista puede consultarla en la fuente con su propio ASN como filtro (`H-4`) | — | — | **No ingerir.** Consultar en origen |

### A.5 — Las doce direcciones de mando y control alojadas en Latinoamérica

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| ipv4 | **`64.176.16.182`** | **La única dirección de C2 alojada en Chile de las 573.** Pertenece a `Liso` —la familia dominante— en `AS20473`, un proveedor de nube internacional con presencia local. Vista el 18-11 y **ya sin actividad el 19-11 a las 08:55**: vida inferior a un día. `CTI-2026-045` la detalla | **Alta** | **Caducada como indicador activo; se conserva como hecho regional** | **Caza retrospectiva** en registros de flujo. Bloqueo sin valor: ya no responde |
| ipv4 | `23.251.55.81` · `23.251.55.155` · `23.251.56.95` · `23.251.56.138` · `23.251.56.223` · `23.251.57.18` · `23.251.57.149` · `23.251.57.223` | **Ocho direcciones en `AS62610` geolocalizadas en Brasil**, aparecidas todas el **13-11** —el día del pico de 200 direcciones— y activas al cierre | Alta | **Volátil: 14 días** | Bloqueo por el feed; caza en registros de flujo |
| ipv4 | `128.1.239.194` · `129.227.121.2` | Dos direcciones en `AS21859`, Zenlayer, geolocalizadas en Brasil. La primera es de las más antiguas del conjunto: **primera observación el 03-11** | Alta | Volátil | Bloqueo por el feed; caza |
| ipv4 | `79.127.208.195` | `AS60068`, geolocalizada en Brasil. Aparecida el 18-11 | Alta | Volátil | Bloqueo por el feed; caza |

> **Y la lectura de esta tabla, que es la que importa: doce direcciones de 573
> es el 2,1 %, y nueve de las doce son del mismo proveedor.** La presencia de
> infraestructura adversaria en la región **existe pero es marginal y
> concentrada**, y la única chilena duró menos de un día. **Quien esperaba
> encontrar aquí una historia regional de alojamiento no la va a encontrar: la
> historia regional de este informe está en los objetivos, no en el C2.**

### A.6 — Comunidades BGP del feed · **para política y para medición**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| artefacto | **`65535:666`** | **BLACKHOLE (RFC 7999). La única comunidad que activa el descarte.** Todo lo demás es informativo | Alta | Estructural | **Requerida en la política de importación** (`X-2.1`) |
| artefacto | `64512:1001` · `64512:2001` | Infraestructura de C2 · fuente `botnet.cl` | Alta | Estructural | Observabilidad y trazabilidad del origen del dato |
| artefacto | **`64512:3001`** · **`64512:3003`** | **Visto hace menos de 24 h** · **visto hace más de 7 días.** Entre 24 h y 7 días, **ninguna etiqueta** | Alta | Estructural | **Adopción por fases** (`X-2.3`): la herramienta que permite empezar sin descartar todo |
| artefacto | `64512:4001`…`64512:4033` | **Identificador de familia**, 33 valores | Alta | Estructural | **Política por familia y serie temporal propia** (`G-2.1`) |

### A.7 — Capacidades declaradas por familia · **con quién lo dice**

<!-- cti:note type="warn" -->

> ⚠ **Toda esta sección es afirmación de la fuente, no observación nuestra.**
> No tenemos muestras. Se consigna porque es útil y porque la fuente distingue
> «no identificado en los binarios revisados» de «evidencia insuficiente»,
> pero **ninguna de estas capacidades está verificada por esta célula** (`G-8`).

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| artefacto | **`KATARU`: propagación por ADB** | **La capacidad de mayor relevancia regional declarada**, porque el puente de depuración de Android abierto en un decodificador permite propagación en red local sin credenciales. Y `KATARU` tiene **el 100 % de sus últimos 100 objetivos en Brasil** | **Declarado por la fuente.** Confianza moderada | Sin caducidad | **Contexto para `E-5.7`**: justifica el inventario del parque doméstico |
| artefacto | **`Manta`: descarga y ejecución de un minero** | Única familia con minería declarada en las 33. Mezcla de monetización —DDoS y criptominería— sobre el mismo parque | Declarado. Confianza moderada | Sin caducidad | Contexto |
| artefacto | **`Eclipse`: orden `UPDATE` que descarga y ejecuta una URL suministrada** · **`EZF3`: guion horario de descarga y ejecución** | **Capacidad de ejecución arbitraria sobre el nodo**: convierten una red de bots de DDoS en una plataforma de distribución de cualquier otra cosa | Declarado. Confianza moderada | Sin caducidad | Contexto. **Eleva el riesgo del nodo comprometido más allá del DDoS** |
| artefacto | **`Aigogo`: retrollamadas sobre DTLS** · **`Titan`: túnel de control por WebSocket** · **`CXFJ`/`SZJL`: relé por canales de retrollamada TCP** | **Tres transportes de control distintos para el mismo negocio de proxy.** Es lo que hace que una firma de red por familia no generalice | Declarado. Confianza moderada | Sin caducidad | Contexto de detección |
| artefacto | **`LinkFog`: «binario del cliente aún no identificado»** | **Se consigna precisamente porque es una admisión de ignorancia de la fuente**, y porque `LinkFog` tiene 46 direcciones y comparte seis bloques con `Hotota` (`O-3.4`). **Una familia con infraestructura medible y sin muestra conocida** | **La propia fuente declara el hueco** | — | **Requisito de colección** |
| artefacto | **`Ecstasy`: «defectos de la carga nativa y limitaciones de HTTP documentados»** · **`Kyorij`: «las opciones numéricas suministradas resuelven a 10»** | **Dos anotaciones que valen como señal de calidad de la fuente**: describen **fallos del malware**, que es información que nadie inventa y que sólo se obtiene desmontando el binario | Declarado | — | **Contexto para `O-2`**: sostiene la valoración de la fuente |

### A.8 — Decisiones de higiene de este informe

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| cartera | **Los 258 prefijos objetivo y los 69 ASN objetivo no se transcriben como indicadores, y los 17 ASN brasileños van marcados `NUNCA bloqueo`** | **La decisión de higiene central del informe** (`X-4`). Son víctimas. Una ingesta ingenua bloquearía a los atacados, y el síntoma tardaría días en aparecer | — | — | Ver `A.4` |
| cartera | **Los bloques `/24` de `A.2` van con tipo `artefacto` y no `ipv4`** | **Razón técnica, no de criterio:** los agregados planos esperan direcciones individuales, y un valor con máscara dentro de `ioc_ipv4.txt` **produciría una entrada que no coincide con nada**. Es la regla de `CTI-2026-032`: un indicador mal formado es peor que su ausencia porque consume confianza. Los bloques son **pivotes de caza**, no valores de bloqueo | — | — | Caza |
| cartera | **No se transcriben las 573 direcciones** | **Sería el error de diseño del informe.** Tienen **mediana de vida de 5,2 días**: una lista aquí es basura en dos semanas. **El valor está en la suscripción al feed, no en la lista** (`T-3`). Se transcriben sólo las doce latinoamericanas, por su interés regional, y marcadas como volátiles | — | — | **Suscribir el feed** (`X-2`) |
| cartera | **No se transcriben las plantillas de configuración de los cuatro fabricantes** | Se da la de MikroTik por ser el fabricante más extendido en la región, y se **remite al sitio para las demás**, por la misma regla de `CTI-2026-032`: **una política de importación de BGP mal copiada falla de forma silenciosa y peor que un indicador** (`X-2.2`) | — | — | Tomar del origen |

### A.9 — Infraestructura de `SZJL` tras la migración, y las tres direcciones de huella `atlas` · ⚠ **estas últimas NO para bloqueo** *(añadido en la versión 1.3)*

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| artefacto | **`101.47.51.0/24`** | **69 direcciones de `SZJL` en `AS150436` Byteplus**, todas con primera observación el **21-11-2026**. Sustituye a `43.117.72.0/24` como bloque de mayor densidad del expediente (`O-3.6`) | **Alta** | **Volátil: revisar en 14 días** | **Caza prioritaria.** Pivote; **no bloquear el bloque**: va como `artefacto` por la razón de `A.8` |
| artefacto | **`101.47.50.0/24`** | 21 direcciones de `SZJL`, mismo ASN y misma fecha de alta | Alta | Volátil | Caza y vigilancia |
| asn | **`AS150436`** — Byteplus Pte. Ltd. (SG) | **92 direcciones aparecidas en un día: el segundo concentrador del ecosistema** y el interlocutor nuevo de `E-5.6`. `IRT-BYTEPLUS-SG` registrado en APNIC con dirección de abuso publicada | **Alta** | Estructural | **Notificación de abuso documentada.** **No bloquear el ASN**: proveedor legítimo con clientes legítimos |
| artefacto | **`43.117.72.0/24`** | **Corrección de `A.2`:** de 43 direcciones a **20**. El pivote sigue siendo válido pero **ya no es el principal**, y su vaciado **no indica remediación** (`O-3.6`) | Alta | Volátil | Caza; **y leer `O-3.6` antes de contarlo como éxito** |
| artefacto | **`x-proxy-agent: atlas`** + **reino `atlas`** en abanico `18000–18021`, con pasarela en **`9009`** y reino `gateway` | **Huella de servicio, y es el indicador más duradero de este añadido**: idéntica en las tres direcciones y distinta de los tres reinos conocidos (`Proxy`, `proxy`, `Restricted`). **Sin corroboración externa de ningún proveedor** | **Moderada** como agrupador; **baja** como atribución | **Estructural mientras el operador no cambie de software** | **Caza**: buscar el patrón en registros de proxy y en escaneos propios. **Pivote de descubrimiento, no valor de bloqueo** |
| artefacto | `121.91.237.218` · `121.91.238.159` · `121.91.242.135` | `AS398465` Rackdog, LLC, prefijo `121.91.224.0/19` **transferido de APNIC a ARIN en 2020** (`O-3.7.1`). La fuente las atribuye a **`Aisuru-Proxy`** —trece direcciones—, y su huella de servicio es de proxy, pero **ninguna corroboración externa las respalda**: ThreatFox, AbuseIPDB, GreyNoise y OTX no tienen nada contra ellas | **Moderada** para la clase *(familia asignada + huella coincidente)*; **baja** para la atribución del conjunto `atlas` | **Volátil: 14 días** | ⚠ **VIGILANCIA Y CAZA RETROSPECTIVA. NO BLOQUEAR TODAVÍA.** Llevan **menos de veinticuatro horas** observadas por la fuente y una sola fuente no sostiene un bloqueo. **Si persisten en la revisión de los 14 días, pasan a `ipv4` como el resto de la infraestructura de proxy de `A.2` y `A.3`** |

> **Por qué estas tres direcciones van como `artefacto` aunque sean direcciones
> individuales y bien formadas, que es la excepción a `A.8` y conviene explicarla.**
> El primer borrador de esta fila las puso como `ipv4` razonando que el tipo
> describe la forma del dato y la acción permitida describe lo que la evidencia
> autoriza. **La compuerta de higiene lo rechazó, y tenía razón por un motivo
> puramente operativo:** el tipo `ipv4` las envía a `ioc_ipv4.txt`, y **ese
> agregado plano no lleva la columna de acción permitida**. Una fila que dice «no
> bloquear» en una columna que el consumidor final no recibe **no dice nada**:
> dice «bloquear». De modo que la regla de `CTI-2026-032` se aplica también al
> revés de como se formuló — **no sólo un indicador mal formado es peor que su
> ausencia; un indicador bien formado cuya salvedad no viaja con él también lo
> es**. El tipo `artefacto` las mantiene fuera del agregado y dentro del
> expediente, que es exactamente donde la evidencia de hoy las sitúa.

## Anexo B — Fuentes y valoración

> Valoración doble Admiralty/OTAN, con el **grado de establecimiento** de
> `CTI-2026-039`. Este informe añade un grado que la cartera no tenía:
> **«medición propia»**, para los datos que esta célula obtuvo directamente.

| Fuente | Disciplina | Fiab. | Cred. | Grado | Notas de sesgo |
|---|---|---|---|---|---|
| **`B-1` — Interfaz pública de consulta de `botnet.cl`**: agregado de 573 direcciones de C2, flujo de eventos con `family=all`, 33 consultas por familia, tabla de pares BGP, matriz de capacidades y página del feed — **leída y medida directamente** | OSINT técnico · **telemetría de tercero, medida por nosotros** | **B** | **2** | **Medición propia sobre fuente de tercero** | **La base de datos entera de este informe.** Virtud: son datos primarios, no relato. Sesgos: **(1)** es fuente única; **(2)** su cobertura define nuestro universo —33 familias son las que esa fuente sigue—; **(3)** **126 de sus 176 pares son brasileños, lo que podría darle mejor visibilidad de Brasil** y es el argumento de `H-3`; **(4)** no publica volumen de tráfico, de modo que nada de intensidad es evaluable |
| **`B-2` — Agenda de NANOG 98**, charla «Botnet.cl — Live Botnet Monitoring and BGP Feed» atribuida a Rodrigo Peña, Bitred Group SpA | OSINT · **listado de ponentes de una conferencia técnica** | **C** | **3** | **Atribución de tercero, no confirmada por el sitio** | **La única identificación del operador que localizamos**, y hay que tomarla con su grado: **un listado de ponentes no es una página de identidad corporativa**. De aquí sale la afirmación de «más de 100 ISP en dos meses», que **verificamos y actualizamos a 176 pares** (`O-2.1`), y la de uso de aprendizaje automático, que **no es verificable**. Sesgo obvio: es material de presentación, y nadie presenta sus fracasos en NANOG. Es `G-4` |
| **`B-3` — Análisis de A10 Networks sobre DDoS en Brasil** (febrero y marzo de 2026) | OSINT comercial · **medición independiente de proveedor** | **B** | **2** | Proveedor | **La corroboración más valiosa del informe, y la más independiente**: 17.527 ataques en una semana con ~99 % contra cinco ISP regionales de fibra, y 498.163 ataques analizados en marzo con el patrón de **ráfagas cortas repetidas en múltiples subredes**. **Dos mediciones, dos métodos, nueve meses de separación, el mismo resultado.** Sesgo: es un proveedor de mitigación de DDoS describiendo un problema que su producto resuelve, y su recomendación —desvío preacordado— es también su negocio. **Que el sesgo sea evidente no hace falso el dato**, y la coincidencia con nuestra medición no se explica por el sesgo |
| **`B-4` — Investigación de HUMAN Security sobre BADBOX 3.0** (2026-11-18) | OSINT comercial · investigación de plataforma | **B** | **2** | Proveedor | **Publicada un día antes de este informe**, y es la corroboración del eje de proxy residencial por una vía completamente distinta —la del dispositivo y el fraude publicitario, no la de la red—: **módulos que inscriben dispositivos en once redes de proxy residencial sin consentimiento**, ~40.000 millones de solicitudes publicitarias diarias en el pico, y vínculo del catálogo a un fabricante mediante lanzador de fábrica. **Las cifras no coinciden con las nuestras y no deben forzarse**: once redes comerciales no son siete familias de código |
| **`B-5` — Cobertura de KrebsOnSecurity** (enero y abril de 2026) | OSINT · periodismo de investigación especializado | **B** | **2** | Periodístico con fuentes propias | Dos aportes distintos: el vínculo entre los operadores de Kimwolf y el panel de control de BADBOX 2.0, y **el caso del actor brasileño con acceso de raíz a la infraestructura de una empresa de mitigación de DDoS**, con vulnerabilidades de enrutadores TP-Link como vía de reclutamiento. **La atribución a un competidor es declaración del director de la empresa afectada y no tiene confirmación independiente**: se consigna como hipótesis que no podemos evaluar (`E-2.1`) |
| **`B-6` — Recuentos de Cloudflare y cobertura del récord de Aisuru** | OSINT · compilación de proveedor y prensa | **C** | **3** | Proveedor, por la vía de la prensa | Fuente del contexto de `KJ-8`: el récord de 31,4 Tbps, la clase TurboMirai, **la acción policial del primer trimestre de 2026 contra Aisuru, KimWolf, JackSkid y Mossad**, y la caída de 805 a 251 ataques sobre 1 Tbps entre trimestres. **Las fuentes discrepan incluso en el mes del récord** —noviembre o diciembre de 2025—, y la cifra trimestral llega por un artículo secundario. **Se usa sólo como contexto y ningún juicio se apoya en ella** |

> **Una observación sobre la estructura de fuentes de este informe, y es
> favorable en comparación con el lote anterior.** `CTI-2026-039` y
> `CTI-2026-042` tuvieron su brecha principal en fuentes de proveedor
> inaccesibles. **Aquí no hay ninguna fuente inaccesible: la fuente primaria
> se consultó directamente y se midió.** La brecha de este informe es de otra
> naturaleza y en cierto modo peor: **no es que no pudiéramos leer la fuente,
> es que sólo hay una**, y su cobertura define nuestro universo. La defensa
> contra eso no es leer más, es **tener un sensor propio** (`G-10`) o una
> segunda fuente de telemetría (`G-4`).

## Anexo C — Léxico de probabilidad y confianza

<!-- cti:bars title="Probabilidad estimativa — cuán probable es que el hecho sea cierto" -->

| Etiqueta | Valor |
|---|---|
| Casi con certeza (≥99 %) | 99 |
| Muy probable (80–95 %) | 88 |
| Probable (55–80 %) | 68 |
| Aproximadamente igual de probable (40–60 %) | 50 |
| Poco probable (20–45 %) | 32 |
| Muy poco probable (5–20 %) | 12 |
| Remoto (≤5 %) | 4 |

**Confianza** (en la *base* del juicio, no en su probabilidad): **alta** —fuentes múltiples, corroboradas, con método expuesto—; **moderada** —fuente única de calidad, o inferencia propia sobre datos verificables—; **baja** —dato ausente, o inferencia sobre indicios indirectos—.

> **La distinción que este informe necesita y que no estaba en la cartera, y
> conviene añadirla al léxico: hay que separar la confianza en el DATO de la
> confianza en la PROPORCIÓN.**
>
> No son lo mismo y en este expediente divergen mucho. «Hay 573 direcciones de
> mando y control, de las cuales 12 en Latinoamérica» es un **dato**: lo
> medimos, es reproducible y la confianza es **alta**. «El 80,2 % de los
> ataques van contra Brasil» es una **proporción de una muestra**: el dato
> subyacente es igual de sólido, pero la afirmación que la gente va a extraer
> —«ocho de cada diez ataques de este ecosistema van a Brasil»— **generaliza
> desde 97 minutos**, y la confianza en esa generalización es **moderada**.
>
> **La regla que se sigue en todo el informe:** cada vez que aparece un
> porcentaje del flujo en vivo, aparece también la ventana. Y donde una
> proporción sostiene un juicio, el juicio lleva **confianza alta para el
> hecho y moderada para la proporción**, como en `KJ-1`. **Colapsar las dos
> produce la frase «medimos que el 80 % del DDoS de la región va a Brasil»,
> que no es lo que medimos.**

## Anexo D — Cómo usar un canal de telemetría continua como fuente de inteligencia

**El problema.** Una fuente que publica un **flujo vivo** —una interfaz de consulta, un canal de eventos, un feed— se comporta de un modo distinto a un informe de proveedor, y las defensas que la cartera tiene desarrolladas no aplican. Un informe se lee entero y sus límites están escritos; **un flujo responde exactamente a lo que se le pregunta, y no dice lo que no se le preguntó.** Un parámetro ausente no produce un error: produce una respuesta bien formada a otra pregunta.

**Por qué hace falta.** Porque este informe estuvo a punto de publicar dos conclusiones falsas a partir de 1.400 eventos perfectamente válidos (`O-2.2`), y porque **no hubo ninguna señal de que faltara algo**: la respuesta paginaba, los contadores crecían y el cursor funcionaba.

**Los seis controles, en orden de coste creciente. Los tres primeros cuestan diez minutos juntos, y el sexto se añadió en la versión 1.3 porque la advertencia 1 de este anexo decía que faltaba.**

| # | Control | Qué detecta | Coste |
|---|---|---|---|
| **1** | **Comparar la consulta con la vista para humanos, en el mismo minuto** | **El control que salvó este informe, y el más barato de todos.** Si el sitio tiene una portada o un panel, **mirarlo mientras se recolecta**: si lo que se ve no se parece a lo que llega, hay un filtro implícito. Aquí la portada mostraba una familia atacando y los datos traían otra | **Minutos** |
| **2** | **Pedir deliberadamente lo que creemos que ya tenemos** | Los valores por omisión invisibles. Si existe un parámetro de ámbito, **pedir explícitamente «todo»** y comparar: `family=all` devolvía otra familia, otra ventana y una marca de agua **cuatro veces mayor** que la consulta sin parámetros | **Minutos** |
| **3** | **Comparar los contadores de la propia fuente entre consultas** | Que estamos viendo una fracción. **Un contador global que es cuatro veces el de nuestra consulta nos dice que tenemos el 25 % de los datos**, y lo dice sin que haya que entender nada del dominio | **Minutos** |
| **4** | **Validar la semántica de todo contador antes de usarlo, y validarla dentro del grupo correcto** | Que un «identificador» no es un «recuento». Aquí los contadores **sí** eran recuentos, pero la primera prueba lo negó porque **mezclamos espacios de numeración de familias distintas** (§O-3.2). **Un resultado negativo en una prueba de contigüidad obliga a revisar el diseño de la prueba antes que el dato** | Una hora |
| **5** | **Antes de afirmar una proporción, medir dos ventanas separadas** | Que la forma esté en la ventana y no en el mundo. Una ventana única no distingue un patrón estable de un episodio. **La versión 1.0 no pudo ejecutarlo antes de emitir; la 1.1 sí, y las proporciones se sostuvieron dentro de 3,5 puntos** (§O-3.5). **Con la salvedad de que las dos ventanas son de la misma tarde**: el control queda ejecutado contra la variación de minutos, no contra la de días | Horas o días |
| **6** | **Medir desde fuera la infraestructura que la fuente nombra, y comprobar si su clasificación aparece en el servicio expuesto** *(añadido en la versión 1.3)* | **Lo que los cinco anteriores no pueden: un error de clasificación, no de filtrado.** Si la fuente separa su catálogo en clases, esas clases deben dejar rastro en algo que la fuente no produce —puertos abiertos, banderas de un escáner de Internet, reinos de autenticación, banners de servicio—. Aquí 27 direcciones en Shodan dieron **cero cruces entre las dos clases declaradas** y **tres reinos de autenticación distintos por familia**, lo que bajó `H-2` sin depender de la fuente (§O-3.7). **Y tiene un segundo rendimiento que no se buscaba:** comparar la última observación de la fuente con la de un escáner independiente **mide la cobertura del sensor**, y así se detectó que la frescura del feed había caído del 91 % al 78,2 % en tres días | Una hora |

**Y la pregunta transversal, que es la que de verdad transfiere a cualquier expediente:**

> **¿Esta forma está en los datos o está en mi colección?**

Se aplica a todo, y en este informe se aplicó cuatro veces con cuatro resultados distintos, lo que es la mejor demostración de que la pregunta discrimina:

| Observación | ¿Datos o colección? | Resolución |
|---|---|---|
| «`Cereal2` es el 100 % de la actividad» | **Colección.** Un valor por omisión | **Falsa.** Corregida (`O-2.2`) |
| «368 de 573 direcciones aparecen en dos días» | **No resuelto.** Puede ser expansión del adversario o incorporación de familias al seguimiento | **Declarada como pregunta** (`G-6`, `H-6`) |
| «Cero ataques contra Chile» | **Probablemente colección**: 97 minutos no detectan un fenómeno de baja frecuencia. **La segunda ventana tampoco vio ninguno**, lo que no resuelve nada: dos ventanas de la misma tarde no son dos observaciones independientes de un fenómeno de baja frecuencia | **Declarada como ausencia no medida** (`G-3`) |
| «El 80,2 % de los ataques van contra Brasil» | **Ni una cosa ni la otra: es una media ponderada por una mezcla inestable.** Tres ventanas dan 80,2 → 76,9 → 73,1 % **sin que ninguna familia cambie de conducta** | **Reemplazada por la medida por familia** (`O-3.5`) |
| «El 85 % de la infraestructura es de familias que no atacan» | **Datos.** Y se pudo demostrar: **las dos clases no comparten ni un bloque `/24` de 206**, y un sesgo de etiquetado no produce huellas de alojamiento disjuntas | **Sostenida, y `H-2` rebajada** (`O-3.4`) |

**La última fila es el patrón que conviene imitar.** La duda sobre el 85 % no se resolvió discutiendo el método de la fuente —que no conocemos— sino **buscando una propiedad de los datos que fuera independiente del clasificador**. El etiquetado de familia no sabe en qué bloque de direcciones está alojada una dirección; por tanto, **si el etiquetado estuviera equivocado, los bloques estarían mezclados.** No lo están.

> **La generalización, y es lo que este anexo aporta a la cartera:** cuando se
> sospecha que un hallazgo es un artefacto de la clasificación de un tercero,
> **la salida no es auditar su clasificador, es encontrar en los mismos datos
> una variable que su clasificador no mira.** Si el hallazgo sobrevive en esa
> variable, es del mundo.

**Las tres advertencias de uso de este marco.**

1. **Los controles 1 a 5 detectan filtros implícitos, no datos erróneos.** Si la fuente clasifica mal, no lo verán — **y ésa es exactamente la laguna que el control 6 cubre**: no corrobora con una segunda fuente de inteligencia, que heredaría el mismo juicio, sino **midiendo la infraestructura directamente**. La versión 1.0 escribió esta advertencia sin tener remedio para ella; la 1.3 lo tiene, y resultó ser más barato de lo que esta nota suponía.
2. **El control 5 es el que casi nadie hace y el que más vale.** Este informe no pudo completarlo antes de emitir: **lo honesto fue acortar la caducidad y declararlo**, no esperar — y ejecutarlo después, que es lo que hizo la versión 1.1. **Y cuando se ejecute, hay que decidir qué tramo cuenta como independiente ANTES de ver el resultado**, porque usar el acumulado que solapa con la primera ventana produce una coincidencia que no significa nada.
3. **Un `404` de una interfaz ajena merece la misma desconfianza que un `200`** *(añadido en la versión 1.3)*. Al recomputar el reparto por clase, nuestra normalización del identificador de familia convertía un guion en subrayado y tres de las treinta y tres familias devolvían «familia desconocida». **Treinta aciertos hicieron verosímiles tres fallos**, y el borrador de esta versión llegó a declarar una brecha —38 direcciones huérfanas— **que no existía** (§O-3.7.1). El control es trivial y no estaba escrito: **cuando una consulta paramétrica falla para un subconjunto, sospechar del formato de la pregunta antes que del catálogo del tercero**, y comprobar que la suma de las partes da el total del agregado.
4. **Y un flujo vivo crea una tentación nueva: la de confundir recolectar con medir.** Es fácil acumular cien mil eventos y creer que se tiene una medición, cuando lo que se tiene es cien mil eventos de la misma hora. **El volumen de la muestra no sustituye a su dispersión en el tiempo.**

## Anexo E — Marcos de referencia empleados

- **ICD 203** (*Analytic Standards*), con la adición de `Anexo C`: **separar la confianza en el dato de la confianza en la proporción**, porque en una medición de ventana corta divergen.
- **Código Admiralty/OTAN**, con el grado nuevo **«medición propia»** para los datos que esta célula obtuvo directamente de la interfaz de la fuente, distinto de «proveedor».
- **Grado de establecimiento** de `CTI-2026-039` —judicial / oficial / proveedor / propio—, aquí con la observación de que **una atribución de un listado de ponentes de conferencia no es una identificación corporativa**.
- **MITRE ATT&CK v18** (`T-2`), con la observación de que **la mitad de las técnicas de este ecosistema son de desarrollo de recursos y de mando y control, no de impacto**.
- **Pirámide del Dolor** (Bianco), en `T-3`, con la **excepción que este expediente obliga a hacer**: el nivel de las direcciones IP, normalmente desaconsejado por su caducidad, **es operacionalizable aquí porque la caducidad la gestiona la fuente mediante una sesión BGP**. Lo que cambia el valor del indicador es el mecanismo de entrega.
- **Análisis de Hipótesis Competidoras (ACH)** y **pre-mortem**, en `O-7`, con `H-2` y `H-3` —las dos hipótesis contrarias a los juicios principales— retenidas y argumentadas, y `H-2` **rebajada por un hallazgo posterior y no por preferencia**.
- **RFC 7999** (comunidad BLACKHOLE) y **RFC 1997** (comunidades BGP), en `X-1` y `X-2`.
- **Uso de telemetría continua como fuente de inteligencia**, propio de este informe (`Anexo D`): cinco controles y la pregunta transversal de si la forma está en los datos o en la colección.

## Anexo F — Paquete legible por máquina

Las tablas `cti:ioc` de este anexo alimentan `ioc_index.csv`. **Seis advertencias de ingesta, y la primera es de seguridad y no de calidad:**

1. **⚠ Los prefijos y ASN de `A.4` son VÍCTIMAS y llevan tipo `artefacto` y `asn` para que no entren en los agregados planos.** Diecisiete de ellos son operadores de fibra brasileños legítimos. **Una ingesta que los bloquee producirá pérdida de conectividad con Brasil y el síntoma tardará días en aparecer.** Es la advertencia inversa de `CTI-2026-040` y la más grave de este informe (`X-4`).
2. **Las 573 direcciones de mando y control NO se transcriben**, y es deliberado: tienen **mediana de vida de 5,2 días**. Se transcriben sólo las doce latinoamericanas. **El valor de esta fuente está en la suscripción al feed BGP, no en una lista estática** (`T-3`, `X-2`).
3. **Los bloques `/24` de `A.2` llevan tipo `artefacto`** por razón técnica: un valor con máscara dentro de `ioc_ipv4.txt` produciría una entrada que no coincide con nada, y la regla de `CTI-2026-032` dice que eso es peor que su ausencia. **Son pivotes de caza.**
4. **Las capacidades de `A.7` son afirmaciones de la fuente**, no observaciones nuestras, y así están marcadas. Extraer «`Manta` instala un minero» o «`KATARU` se propaga por ADB» como hecho establecido sería un error (`G-8`).
5. **Toda proporción del flujo en vivo lleva su ventana.** Sin la ventana, el `80,2 %` se convierte en una afirmación que no hicimos (`Anexo C`).
6. **Y los contadores acumulados son recuentos de eventos, verificados**, pero **un evento no es una magnitud**: la fuente no publica volumen de tráfico, de modo que ninguna lectura de intensidad es sostenible (`G-9`).

Ninguna fuente de este informe publica paquete STIX. **Pero este expediente tiene, excepcionalmente, un camino de automatización mejor que un paquete:** una sesión BGP en fase de observación (`X-2.3`) entrega el conjunto completo de forma continua, con comunidades de familia y de antigüedad, **sin fichero intermedio y sin que nadie tenga que mantener una lista**. Es la recomendación `G-2.1` y hace innecesario el paquete.

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| **1.3** | **2026-11-22** | **Remedición de los agregados publicados en `A.2` y `A.3` contra la fuente, tres días después de la emisión, y dos hallazgos que un delta diario no da.** **El primero (`KJ-11`, `O-3.6`): `SZJL` migró de proveedor.** `AS45102` cayó de 45 a 29 direcciones y su bloque `43.117.72.0/24` de 43 a 20 —un 53 %—, mientras el 21-11 aparecían **92 direcciones de `SZJL` en `AS150436` Byteplus, todas con la misma fecha de alta**, en dos bloques contiguos. La familia pasó de 46 a 115 direcciones: **se trasladó y se amplió**. Esto deja el disparador **`I-6` CUMPLIDO el 22-11-2026, con el resultado contrario al que esperaba**, y obliga a reformularlo: un bloque vaciado es compatible con una migración exitosa del adversario, de modo que **la métrica de la palanca de `E-5.6` pasa a ser el recuento total de direcciones vivas de la familia y no el vaciado de un bloque**. `KJ-7` se **modifica** con las cifras nuevas —los cinco primeros concentran ahora el 62,9 % frente al 56,2 %, y `DigitalOcean` entra entre ellos desde el eje de DDoS— y `A.9` publica el bloque nuevo, el ASN nuevo y la corrección de `43.117.72.0/24`. **El segundo (`KJ-12`, `O-3.7`): la separación de los dos negocios se verificó por una vía que no pasa por el clasificador de la fuente.** 27 direcciones consultadas en Shodan: **ninguna de las nueve de las tres familias de DDoS presenta señal de proxy**, y once de las dieciocho de familias de proxy sí, con **abanicos de puertos consecutivos y reinos de autenticación propios** por familia. Dos medidas sin mecanismo común coinciden, y eso **baja `H-2` de «posibilidad real» a «poco probable»** sin necesitar el correo al operador que `G-1` pedía. **Y tres añadidos de higiene.** Las **tres direcciones nuevas del parte** van a `A.9` con **acción permitida de sólo vigilancia, expresamente no bloqueo, y regla de salida a catorce días**: la fuente las atribuye a `Aisuru-Proxy` y su huella de servicio concuerda, pero es **una sola fuente**, ThreatFox, AbuseIPDB, GreyNoise y OTX no tienen nada contra ellas y **llevan menos de veinticuatro horas observadas**; su huella `x-proxy-agent: atlas` se publica como **pivote de caza** porque es lo más duradero que aportan, y se deja escrito que **la hipótesis de prefijo secuestrado se refutó** con el fichero de transferencias de APNIC (`O-3.7.1`). **Se corrige además un error de colección propio que el borrador de esta misma versión llegó a publicar como brecha:** la consulta por familia normalizaba el identificador con subrayado en lugar de guion, de modo que `aisuru-ddos`, `aisuru-proxy` y `sexybot-linked` devolvían «familia desconocida» y 38 direcciones parecían huérfanas. **No lo son: las 625 tienen familia**, el reparto por clase **sí es recomputable** —556 de 625, el 89,0 %, son de las siete familias de proxy, frente al 85 % del 19-11 (`KJ-2`)— y la lección va al `Anexo D` como advertencia nueva: **un `404` de una interfaz ajena merece la misma desconfianza que un `200`**. **`G-12` se reescribe** y pasa a recoger la brecha que sí existe: **`Eclipse` se ha quedado sin ninguna dirección viva**, `141.98.10.0/24` aloja hoy cinco direcciones todas de `Aisuru-DDoS`, y con ello **el único solapamiento entre dos familias de DDoS deja de ser observable**, lo que degrada a conjetura histórica esa mitad de `KJ-9` sin afectar al vínculo `Hotota`↔`LinkFog`. **Y una tercera medición, sobre el sensor y no sobre el adversario:** la proporción de direcciones vistas en las últimas 24 h **cayó del 91 % al 78,2 %** en tres días, y ocho de ocho direcciones muestreadas que la fuente llevaba uno o dos días sin ver **seguían activas en un escáner independiente**; de modo que la caída es **pérdida de cobertura del sensor y no repliegue del adversario**, y las comunidades de antigüedad `64512:300x` pasan de comodidad de adopción a **control de calidad obligatorio** en la fase 4 (`T-3`, `X-2.3`). El `Anexo D` gana el **control 6** —medir desde fuera la infraestructura que la fuente nombra—, que es el remedio que su propia advertencia 1 declaraba inexistente. Y se corrige un **error de identificador ATT&CK que arrastraban las versiones 1.0 a 1.2**: la propagación por ADB de `KATARU` citaba `T1021.001`, que es *Remote Desktop Protocol*; el correcto es **`T1021`**, *Remote Services*. **No se extiende la caducidad**, que sigue en 2027-01-19: esta versión remide infraestructura y verifica una clasificación, **no revalida las proporciones del flujo**, que siguen descansando en las tres ventanas de la misma tarde del 19-11 (`G-2`) | Célula CTI |
| 1.2 | 2026-11-19 | **Tercera ventana** (15:31–15:45, 357 eventos) añadida a §O-3.5, y con ella un hallazgo que dos ventanas no daban: **la proporción global de objetivos brasileños desciende de forma monótona (80,2 → 76,9 → 73,1 %) mientras la de `Liso` se mantiene (86,9 → 83,5 → 83,1 %)**. Lo que cambia es **la mezcla de familias**, no la conducta de ninguna. De ahí la instrucción de método añadida: **medir por familia y no en agregado**, porque el agregado de este ecosistema es una media ponderada por una mezcla inestable | Célula CTI |
| 1.1 | 2026-11-19 | **Ejecución del control 5 del `Anexo D`**, que la versión 1.0 declaró como no realizado. Una **segunda ventana estrictamente disjunta** de 572 eventos (15:11–15:31 UTC) sostiene las proporciones: Brasil 76,9 % frente a 80,2 %, pulsos de cinco segundos 82,4 % frente a 79,2 %, y el mismo operador en cabeza. **Se refuerza la confianza de `KJ-1` y `KJ-5`, se cierra parcialmente `G-2`** —queda abierta la variación por hora y por día— y se añade §O-3.5 con la salvedad de que **las dos ventanas son de la misma tarde**. Instantánea de infraestructura repetida: 573 → 574 direcciones en quince minutos. **Sin cambios en los demás juicios ni en los indicadores** | Célula CTI |
| 1.0 | 2026-11-19 | Emisión inicial. Incluye: la **asimetría medida entre objetivos regionales e infraestructura extrarregional** —80,2 % de ataques contra Brasil frente a 2,1 % de C2 en la región— (`KJ-1`, `E-2`); el **hallazgo central de que el 85 % de la infraestructura pertenece a las siete familias que nunca atacan**, con la demostración posterior de que **las dos clases de negocio no comparten ni un bloque `/24` de 206** (`KJ-2`, `E-3`, `O-3.4`); la **concentración del 90,2 % de la actividad en tres familias de 33**, con los contadores validados (`KJ-3`, `O-3.2`); la **victimología de operadores regionales brasileños**, corroborada independientemente por A10 nueve meses antes (`KJ-4`, `E-2.1`); el **perfil de pulso de cinco segundos** y su consecuencia de doctrina (`KJ-5`, `T-1`); la **evaluación del feed BGP como activo defensivo regional** con verificación propia de la cifra pública de su operador —«más de 100 ISP» → **176 pares medidos**— (`KJ-6`, `O-2.1`, `X-1`); la **concentración del alojamiento adversario** en cinco proveedores (`KJ-7`, `A.3`); el **silencio de `Cereal2`** y su contexto sin establecer (`KJ-8`); el **análisis de granularidad del solapamiento** con los doce bloques compartidos y el vínculo `Hotota`↔`LinkFog` en seis de ellos (`KJ-9`, `O-3.4`); el **error de colección documentado en lugar de borrado** (`KJ-10`, `O-2.2`); la **advertencia de higiene inversa** sobre los prefijos víctima (`X-4`, `A.4`); y el método de cinco controles del `Anexo D` | Célula CTI |

> **Tres notas sobre esta emisión.**
>
> La primera: **es el primer informe de la cartera cuyos datos primarios son
> propios.** Todos los anteriores son lectura y reconciliación de fuentes de
> terceros; aquí se midió. Eso cambia la naturaleza de las brechas: ya no es
> «no pudimos leer la fuente» sino **«sólo hay una fuente y su cobertura define
> nuestro universo»**.
>
> La segunda: **la caducidad son 60 días y no los 90 habituales**, porque las
> proporciones de una medición de 97 minutos envejecen más rápido que un juicio
> sobre un actor. **No es prudencia retórica: el muestreo longitudinal de
> `G-2` puede desmentir una cifra de este informe**, y si lo hace habrá una
> versión 1.1.
>
> La tercera: **el error de `O-2.2` es el tercer caso del mismo patrón en dos
> lotes.** `CTI-2026-037` casi concluyó que un requisito era falso porque los
> hechos verificados formaban una explicación elegante; aquí casi concluimos
> algo falso porque **el valor por omisión de una interfaz devolvió una
> historia más limpia que la realidad**. La forma del error es la misma: **la
> hipótesis cómoda llegó primero.** Lo nuevo es que esta vez venía incorporada
> en una herramienta, y eso es más difícil de detectar que un sesgo propio.

## Anexo H — Realimentación del consumidor

Este informe mide un sistema vivo con una fuente única, sostiene un hallazgo estructural sobre el reparto de la infraestructura, y recomienda adoptar una capacidad defensiva de un tercero pequeño. Las tres cosas se pueden atacar, y conviene que se ataquen.

1. **¿Se cruzaron las 573 direcciones contra los registros de flujo?** Es `H-1`, se hace en una tarde, **y es la única pregunta de este informe que puede convertir un documento en un incidente**. Un positivo significa que hay un nodo de red de bots dentro de la organización. Si no hay registros de flujo retenidos, **ésa es la conclusión del informe en esa organización** (`V-1`).
2. **¿Se suscribió el feed BGP, aunque sólo sea en fase de observación?** Es `E-5.1` y `X-2.3`. **La fase 1 no bloquea nada, no tiene riesgo y convierte el feed en un sensor.** 176 pares ya lo hicieron, 22 de ellos chilenos. Si se decidió no hacerlo, **la decisión documentada también sirve**: lo que no sirve es no haberla tomado.
3. **¿Alguien preguntó a la fuente si una dirección puede llevar dos comunidades de familia?** Es `G-1`, es un correo, y **resolvería la ambigüedad del hallazgo más estructural del informe**. Es la petición más barata del expediente.
4. **¿Se tomaron las proporciones del flujo como la medida del fenómeno?** Es el riesgo 1 del pre-mortem. **El 80,2 % es de hora y media de un jueves de noviembre.** Si alguien ha citado esa cifra sin la ventana, el informe ha fallado en su advertencia más repetida.
5. **¿Se bloqueó algún prefijo de `A.4`?** Es la pregunta de seguridad de este informe. **Son víctimas.** Si la respuesta es que sí, hay que revertirlo hoy y revisar el proceso de ingesta, porque el fallo no es de este informe: es del proceso que no distingue dos vistas de una misma fuente.
6. **¿Se midió la detección de pulso agregando por operador en ventanas de diez segundos?** Es `X-3.1` y `H-5`. Una organización puede estar recibiendo cientos de pulsos al día y **no tener ni una alerta**, porque los está midiendo con la granularidad equivocada.
7. **¿Hay desvío preacordado con el tránsito, con activación automática?** Es `E-5.2`. **Con cinco segundos de mediana, un procedimiento manual es decorativo.** Y es la recomendación de A10 además de la nuestra, que es la clase de coincidencia que conviene aprovechar en una conversación con Compras.
8. **Si somos proveedor de acceso regional: ¿se ha asumido que somos objetivo preferente?** `KJ-4` y el 99 % de A10 en cinco operadores. **No es daño colateral de ataques dirigidos a otros.**
9. **¿Se está tratando el proxy residencial como riesgo de autenticación y no de red?** Es `E-3` y `H-3`, es el 85 % de la infraestructura de este ecosistema, y es el eje que **más probablemente afecta a una organización que no es operador**. Llega por la puerta de entrada, con reputación limpia.
10. **Y una pregunta sobre nuestro propio método, que es la que más vale de las diez:** el `Anexo D` propone cinco controles contra los filtros implícitos de una fuente viva. **¿Alguien ha encontrado un sexto, o ha visto fallar uno de los cinco?** El control 5 —medir dos ventanas separadas— era el único que la versión 1.0 **no pudo completar antes de emitir**; la 1.1 lo ejecutó y las proporciones se sostuvieron (`O-3.5`). **Pero las dos ventanas son de la misma tarde**, de modo que el control está probado contra la variación de minutos y no contra la de días. **Si alguien muestrea una semana y la proporción brasileña no se sostiene, ese resultado vale más que este informe.**

*Fin del informe `CTI-2026-044` v1.0.*
