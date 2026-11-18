---
tlp: "TLP:CLEAR"
pap: "PAP:AMBER"
id: "CTI-2026-031"
version: "1.0"
tipo: "Perfil de actor estatal mercenario + evaluación de un canal de mando y control que no se puede dar de baja"
foco_regional: "Latinoamérica hispanohablante. **Confirmado: una organización de comunicaciones en Venezuela (junio de 2026).** Chile, Colombia, Ecuador, Brasil, El Salvador y Uruguay aparecen con **confianza moderada** y sin intrusión confirmada: la distinción es el eje de este informe"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "Dark Caracal · G0070 (MITRE ATT&CK) · nexo con la Dirección General de Seguridad General (GDGS) del Líbano · familias Bandook, CrossRAT, Pallas, Poco RAT, AsioGate y (2026) GoCaracal"
fecha: "2026-11-17"
caduca: "2027-02-17"
autor: "Célula CTI"
distribucion: "Elaborado íntegramente con fuentes abiertas TLP:CLEAR, con el informe de Arctic Wolf Labs del 26 de agosto de 2026 leído en original como fuente principal, incluido su anexo técnico. Una fuente consultada y deliberadamente NO reproducida: véase el Anexo B.1. Difusión libre, conservando la atribución de las fuentes y las salvedades metodológicas de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-031

## Un servicio de inteligencia estatal libanés lleva cinco años operando contra el mundo hispanohablante, y en junio de 2026 puso su canal de respaldo de mando y control en la cadena de bloques de Ethereum

### Es la primera pieza de infraestructura adversaria de esta cartera que **nadie puede dar de baja** — y la primera que **el adversario tampoco puede borrar**. Esas dos frases tienen la misma causa, y sólo la segunda está a nuestro favor

#### Lo confirmado es **una** intrusión: una organización de comunicaciones de Venezuela, junio de 2026. Chile, Colombia y Ecuador aparecen con **confianza moderada** y sin víctima confirmada. El requisito que originó este informe los daba por confirmados y añadía «entidades gubernamentales» que ninguna fuente de 2026 sostiene

> **Regla de oro del producto:** todo párrafo debe responder a un requisito de
> inteligencia (PIR) y habilitar una decisión. Si un párrafo no cambia lo que
> alguien va a hacer, va al anexo o se borra.

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-031` |
| Versión / fecha | `1.0` — 2026-11-17 (emisión inicial) |
| Tipo de producto | Perfil de actor estatal con comportamiento de mercenario, más **evaluación de una técnica de resiliencia de mando y control que invalida parcialmente el modelo de retirada de infraestructura**, más **corrección de cuatro afirmaciones del requisito que originó el informe** |
| Niveles cubiertos | Estratégico · Operacional · Táctico · Técnico |
| Foco regional | **Latinoamérica hispanohablante, con una gradación que hay que respetar.** (a) **Confirmado con investigación de respuesta a incidentes:** una organización de comunicaciones en Venezuela, junio de 2026. (b) **Confianza moderada, sin víctima nombrada:** artefactos e infraestructura asociados a Brasil, Ecuador, Chile, Colombia, El Salvador y Uruguay. (c) **Histórico, febrero de 2026:** Venezuela principalmente, con componentes de la cadena reutilizados contra Chile y Brasil |
| Marcado de difusión | `TLP:CLEAR` · `PAP:AMBER` |
| Clasificación interna | Sin clasificar. Todo el material proviene de publicaciones abiertas, salvo una fuente consultada y no reproducida por su propio marcado (Anexo B.1) |
| Requisitos atendidos | `PIR-01` (actores con intención y capacidad contra nuestro sector y nuestra geografía), `PIR-03` (técnicas de mando y control resistentes a la retirada de infraestructura), `PIR-07` (abuso de servicios legítimos y de cadenas de bloques públicas), `RFI-2026-11-A` (el requisito que pidió este lote) |
| Solicitante / consumidor primario | Jefatura de SOC y Dirección. La sección `E-4` lleva una decisión que es de Dirección y no de SOC, porque implica a Legal |
| Ventana de observación | 2012-01-01 → 2026-11-17. **Ventana densa: 2026-01-01 → 2026-07-31**, que es el periodo de desarrollo del marco GoCaracal documentado sobre 249 muestras |
| Base de colección | Cinco fuentes externas, una de ellas primaria y leída en original con su anexo técnico completo. **Sin telemetría propia** |
| Autor (analista) | Célula CTI |
| Revisión por pares | Pendiente |
| Aprobación | Pendiente |
| Caducidad / revisión | 2027-02-17 (92 días). **Revisión anticipada obligatoria si se cumple cualquiera de los disparadores de `O-7`**, y uno de ellos es consultable a diario sin permiso de nadie: una escritura nueva en el contrato |
| Productos relacionados | `CTI-2026-020` (Blind Eagle: el otro actor que opera con señuelos en español contra la región andina, con el que **no debe confundirse**) · `CTI-2026-022` (Red Akodon) · `CTI-2026-023` (Machete) · `CTI-2026-018` (abuso de TLD: los dominios de entrega de este actor viven en `.cloud`, `.icu`, `.online` y `.me`) · `CTI-2026-019` (ARTEX) |
| Paquete legible por máquina | Las tablas `cti:ioc` del Anexo A alimentan `ioc_index.csv` en la construcción. **La fuente preferente para ingesta sigue siendo el anexo del informe de Arctic Wolf**, que advierte que sus indicadores son *referential* y que la lista completa está sólo con sus clientes |

> ⚠ **Limitación estructural, y hay que decirla antes que nada.** Este informe
> **no incorpora telemetría propia**. La sección `O-4` («nuestra exposición»)
> queda sin evaluar y se entrega como cuestionario, no como hallazgo. Todo lo
> que sigue describe lo que el actor hace **en otros**, y la única pregunta que
> este documento no puede responder es la única que importa de verdad: si está
> dentro. Dicho esto, hay una excepción insólita y es el motivo de que este
> informe exista: **una parte de la infraestructura de este adversario es
> consultable por cualquiera, hoy, sin telemetría, sin permiso y sin pagar**.
> Véase `E-1` y `T-4`/`H-1`.

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** Dark Caracal mantiene en 2026 una operación de espionaje sostenida contra organizaciones e individuos hispanohablantes de Latinoamérica, con un marco de malware nuevo escrito en Go. Arctic Wolf Labs investigó en junio de 2026 una intrusión dirigida contra una organización de comunicaciones en Venezuela y la vincula a Dark Caracal; el análisis posterior de 249 muestras relacionadas reconstruye el desarrollo del marco entre enero y julio de 2026. Valoramos **muy probable** *(80–95 %)* que el conjunto de 249 muestras corresponda a un único marco desarrollado de forma planificada por un mismo equipo. **Confianza: alta.** *Base:* fuente primaria B-2 leída en original, con metodología declarada (estructuras de paquete compartidas, módulos reutilizables, flujos de ejecución comunes y cadenas de versión interna `v1.0.1`–`v1.0.6`).

**KJ-2.** El canal de respaldo de mando y control en Ethereum **no se puede retirar, y por la misma razón no se puede ocultar**. El build extendido de GoCaracal lee una dirección de C2 de reemplazo desde el almacenamiento de un contrato inteligente, mediante una llamada `eth_getStorageAt` a un extremo JSON-RPC público. Eso elimina la retirada de infraestructura como medida de contención de ese canal —no hay servidor que incautar ni dominio que suspender—, pero **convierte la configuración del adversario en un registro público, permanente, histórico y consultable por el defensor antes de que el implante la use**. Valoramos **casi con certeza** *(≥99 %)* que el valor almacenado en ese contrato sea legible por cualquiera en cualquier momento: es una propiedad de la cadena, no una valoración sobre el actor. **Confianza: alta.** *Base:* diseño documentado del contrato `BulletproofC2` en la fuente primaria, más la naturaleza pública de Ethereum.

**KJ-3.** Bloquear el C2 principal sin leer antes el contrato **activa el mecanismo de respaldo y nos deja ciegos**. La fuente primaria describe el disparador con precisión: tras **fallos repetidos** contra el C2 principal, el implante consulta el contrato, y si el valor devuelto resuelve a una dirección válida, actualiza su configuración en memoria y reintenta. Es decir: la medida defensiva evidente es exactamente el estímulo que el mecanismo espera. Valoramos **probable** *(55–80 %)* que un bloqueo de las 24 direcciones publicadas, aplicado sin vigilancia del contrato, produzca pérdida de visibilidad sobre un implante que sigue activo. **Confianza: moderada.** *Base:* la lógica del implante está documentada; el resultado depende de si el operador mantiene el valor del contrato al día, lo que no está establecido.

**KJ-4.** La exposición de Chile, Colombia y Ecuador **está afirmada con confianza moderada y sin una sola víctima nombrada**, y el requisito que pidió este informe la daba por confirmada. Arctic Wolf identifica artefactos e infraestructura asociados a Brasil, Ecuador, Chile, Colombia, El Salvador y Uruguay, y valora esa actividad regional adicional **con confianza moderada mientras sigue investigando su alcance**. Valoramos **probable** *(55–80 %)* que exista al menos una víctima real no publicada en uno de esos seis países. **Confianza: baja.** *Base:* inferencia a partir de infraestructura de entrega y de más de cien ficheros SVG relacionados, sin ninguna intrusión confirmada fuera de Venezuela. El dato se usa para priorizar caza, **no** para afirmar compromiso.

**KJ-5.** La afirmación de que en 2026 este actor atacó **«entidades gubernamentales»** en la región andina **no está corroborada por ninguna fuente pública de 2026**. Históricamente sí: el informe de 2018 documenta gobiernos, militares, instituciones financieras y activistas entre los objetivos. Pero el expediente de 2026 nombra **un** sector —comunicaciones— y **un** país —Venezuela—, con señuelos financieros y fiscales en español como único indicio de la selección. Valoramos **posibilidad real** *(45–55 %)* de que haya objetivos gubernamentales regionales en 2026 no publicados. **Confianza: baja.** *Base:* precedente histórico sólido más ausencia total de evidencia contemporánea. Es brecha de colección `G-1`, no hallazgo.

**KJ-6.** La cadena de linaje «Poco RAT → AsioGate → GoCaracal» **no está establecida, y la fuente primaria la niega explícitamente en su tramo final**. Arctic Wolf afirma que **no ha identificado evidencia de que GoCaracal sea un sucesor directo de AsioGate a nivel de código**, y que lo que comparten es un papel funcional dentro de ecosistemas de entrega e infraestructura solapados. La idea de que AsioGate sucede a Poco RAT procede de un agregador, no de Kaspersky. Valoramos **poco probable** *(20–45 %)* que exista una relación de sucesión de código entre estas tres familias. **Confianza: moderada.** *Base:* negación explícita de la fuente que hizo el análisis de código. Esta cartera tiene tres informes que existen porque alguien compuso un solapamiento con una equivalencia (`CTI-2026-017`, `CTI-2026-022`, `CTI-2026-030`): no se añade un cuarto por comodidad narrativa.

**KJ-7.** Veintitrés de las veinticuatro direcciones de C2 de GoCaracal están en redes operadas por **Aeza Group**, proveedor designado por la OFAC del Tesoro de EE. UU. el 1 de julio de 2025. Las de Bandook están en **AlexHost**, que la misma fuente describe como proveedor previamente asociado a Dark Caracal. Valoramos **casi con certeza** *(≥99 %)* que la concentración de alojamiento sea una preferencia deliberada y estable del actor, y **muy probable** *(80–95 %)* que el bloqueo por prefijo de esas redes sea defendible en una red corporativa. **Confianza: alta** para la concentración —es un recuento, no un juicio—, **moderada** para la recomendación de bloqueo, que depende del inventario propio. *Base:* anexo de la fuente primaria más el comunicado de designación del Tesoro.

**Qué cambiaría estos juicios.** Cuatro falsadores concretos y observables, en orden de facilidad: **(a)** una escritura nueva en el almacenamiento de `0x03D6…99d8`, o un contrato nuevo desplegado desde la cartera `0x7D32…052F`, consultable hoy y gratis —rompería la hipótesis de que la campaña está en pausa y daría el C2 siguiente antes de que se use—; **(b)** la publicación por cualquier proveedor de una intrusión **confirmada** en Chile, Colombia, Ecuador o Perú, que convertiría `KJ-4` de inferencia en hecho; **(c)** una muestra de GoCaracal cuyo `CONTRACT` apunte a una cadena distinta de Ethereum, o a un mecanismo de resolución distinto del almacenamiento de contrato, que ampliaría la superficie de detección de `D-1`; **(d)** evidencia de código que vincule GoCaracal con AsioGate o con Poco RAT, que invalidaría `KJ-6` y obligaría a reescribir `O-1`.

---

## 2. Resumen ejecutivo

Hay un servicio de inteligencia estatal que lleva al menos catorce años haciendo espionaje y que desde 2021 ha girado su atención hacia el mundo hispanohablante. No es chino, ni ruso, ni norcoreano, ni iraní: es libanés. En enero de 2018, la Electronic Frontier Foundation y Lookout publicaron un informe conjunto que rastreó la infraestructura de prueba del actor hasta un edificio de la Dirección General de Seguridad General del Líbano en Beirut. El propio informe fue prudente con la última milla de esa atribución —los investigadores dijeron que no podían descartar que fuera obra de un empleado por su cuenta— y el Líbano lo negó. Pero el actor existe, tiene nombre en MITRE ATT&CK (`G0070`) y sigue operando.

**Lo que nos importa es que sus objetivos hablan español y están en esta región.** Desde 2021 la selección se desplazó a Latinoamérica; en 2024 y 2025 se documentó una familia llamada Poco RAT contra empresas de habla hispana, con Venezuela, Chile, Colombia, Ecuador y la República Dominicana entre los países citados; en febrero de 2026 Kaspersky describió una campaña con señuelos financieros en español, adjuntos SVG armados, acortadores de URL y un cargador en Delphi; y en junio de 2026 Arctic Wolf Labs investigó una intrusión real contra una organización de comunicaciones en Venezuela.

**Lo nuevo de 2026 no es el malware: es el canal de respaldo.** El marco nuevo, GoCaracal, escrito en Go y con dos perfiles de compilación, lleva una capacidad opcional que cambia la aritmética de la contención. Si el servidor de mando y control principal deja de responder varias veces, el implante no se rinde: hace una llamada `eth_getStorageAt` a un extremo JSON-RPC público de Ethereum, lee un valor del almacenamiento de un contrato inteligente, y si ese valor resuelve a una dirección válida, se reconfigura en memoria y reintenta. El contrato se llama `BulletproofC2`, está escrito en Solidity, guarda un único valor mutable y sólo admite actualizaciones del monedero que lo desplegó.

**Esto rompe algo y regala algo, y conviene no quedarse con la primera mitad.** Lo que rompe: la retirada de infraestructura. No hay servidor que incautar ni registrador al que escribir; el valor vive replicado en miles de nodos y se puede leer por varias rutas distintas, de modo que ninguna incautación lo elimina. Lo que regala: ese mismo valor es público. Cualquiera puede leer hoy, gratis y sin autorización de nadie, la dirección de C2 que el adversario ha dejado preparada para la próxima vez — **antes de que ningún implante la use**. Y puede leer además el historial completo: cada cambio, con su fecha, y los despliegues de prueba que el mismo monedero hizo primero en la red Sepolia antes de pasar a la red principal, incluidos valores con direcciones privadas RFC 1918 que delatan una fase de desarrollo. Es el único componente de infraestructura adversaria de esta cartera que **el propio adversario no puede borrar**.

**La decisión concreta que este informe pide es de secuencia, y es contraintuitiva.** El reflejo —bloquear las veinticuatro direcciones publicadas— es exactamente el estímulo que activa el mecanismo de respaldo: la fuente primaria dice que el disparador son los fallos repetidos contra el C2 principal. Bloquear primero y mirar después significa empujar al implante hacia un canal que no estamos vigilando. El orden correcto es: leer el contrato, instrumentar su vigilancia, **y después** bloquear, con la lectura del contrato convertida en una fuente de inteligencia permanente.

<!-- cti:cards -->

| Rasgo | Qué significa | Etiqueta |
|---|---|---|
| Canal de respaldo en una cadena de bloques pública | La retirada de infraestructura deja de ser una medida de contención para ese canal. No hay servidor que incautar. Pero el valor es legible por nosotros **antes** de que se use: se invierte quién tiene la ventaja de información | `01 · resiliencia de C2` |
| Dos perfiles de compilación de un mismo marco | El operador ajusta la capacidad a la necesidad: un implante pequeño entra y entrega, uno extendido se queda y recolecta. La detección entrenada sobre el grande no ve el pequeño | `02 · modularidad` |
| Alojamiento concentrado en un proveedor sancionado | 23 de 24 direcciones en redes de Aeza Group, designado por la OFAC en julio de 2025. El bloqueo por prefijo es defendible, y hay una pregunta de cumplimiento normativo que no es del SOC | `03 · infraestructura` |
| Identificadores de comando de Bandook aleatorizados | Las firmas y los métodos de análisis construidos sobre los identificadores secuenciales `@0001`–`@0136` han quedado sin valor. El esfuerzo de detección tiene que subir de nivel | `04 · antianálisis` |
| Señuelos financieros y fiscales en español, y mensajes de operador en español | La selección es lingüística y sectorial, no nacional. Ser una empresa hispanohablante con un departamento de contabilidad es el criterio | `05 · selección` |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `249` | Muestras relacionadas analizadas por la fuente primaria | Reconstruyen el desarrollo del marco entre enero y julio de 2026 en cuatro fases |
| `1` | Intrusiones **confirmadas** con investigación de respuesta a incidentes | Una organización de comunicaciones en Venezuela, junio de 2026. Todo lo demás es inferencia |
| `6` | Países con artefactos e infraestructura asociados, **con confianza moderada** | Brasil, Ecuador, Chile, Colombia, El Salvador y Uruguay. Sin víctima nombrada en ninguno |
| `23 de 24` | Direcciones de C2 de GoCaracal en redes de un proveedor sancionado | Aeza Group, designado por la OFAC el 1 de julio de 2025 |
| `34` | Manejadores de comando del build extendido | Frente a un despachador numérico compacto en el build ligero. Mismo marco, dos tamaños |
| `≈82` | Manejadores de comando de la variante de Bandook de junio de 2026 | **Menos** que en variantes anteriores, con los identificadores aleatorizados: build a medida, no capacidad reducida |
| `14 años` | Antigüedad mínima de la operación | Campañas documentadas desde enero de 2012 |

> ✅ **Decisiones que se solicitan, con plazo.**
> **(a) Hoy, antes de bloquear nada:** leer el valor almacenado en los cuatro contratos del Anexo A.2 y registrarlo con fecha. Cuesta una llamada HTTP y no requiere autorización de nadie (`E-a`).
> **(b) 7 días:** instrumentar la vigilancia diaria de esos contratos y de la cartera que los despliega, y sólo entonces aplicar el bloqueo de red del Anexo A.3 (`E-b`).
> **(c) 14 días:** desplegar `D-1`, la detección de tráfico `eth_getStorageAt` y de resolución de extremos JSON-RPC públicos desde puestos sin justificación de desarrollo. Es la detección de mayor valor de este informe y **no depende de ningún indicador perecedero** (`E-c`).
> **(d) 30 días:** decisión de Dirección con Legal sobre el bloqueo por prefijo de las redes de un proveedor designado por la OFAC, y sobre si la designación obliga a algo más que a bloquear (`E-d`).
> **(e) 30 días:** comprobar en el parque la existencia de cualquier fichero `NTUSER.MAN` y del patrón de ruta de `X-2`. Son artefactos duraderos y de falso positivo casi nulo (`E-e`).

---

## 3. Alcance, requisitos y limitaciones

**3.1 Requisitos de inteligencia atendidos**

| Req. | Enunciado | ¿Respondido? | Dónde |
|---|---|---|---|
| PIR-01 | ¿Qué actores tienen intención y capacidad demostradas contra organizaciones hispanohablantes de nuestra región? | Sí, con la gradación de confianza de `KJ-4` intacta | `E-1`, `E-2`, `O-1` |
| PIR-03 | ¿Qué técnicas de mando y control vuelven inútil la retirada de infraestructura, y qué hacemos en su lugar? | **Sí, y es el núcleo del informe** | `E-1`, `T-1`, `X-3`, `H-1` |
| PIR-07 | ¿Qué servicios legítimos y qué infraestructuras públicas se están abusando como canal de configuración? | Sí: extremos JSON-RPC públicos de Ethereum, acortadores de URL, 7-Zip, SVG | `T-2`, `X-3` |
| RFI-2026-11-A | El requisito que pidió este lote afirmaba cuatro cosas sobre este actor. ¿Se sostienen? | **Sí para dos, no para dos.** Véase `O-6` y la tabla de `3.5` | `KJ-5`, `KJ-6`, `O-6`, `3.5` |
| PIR-04 | ¿Nos afecta? | **No.** Requiere telemetría propia | `O-4`, sin evaluar |

**3.2 Fuera de alcance.** No se evalúan: la actividad histórica del actor contra objetivos de Oriente Medio ni contra activistas y periodistas, salvo lo necesario para establecer su naturaleza; la plataforma Android (`Pallas` y las versiones troyanizadas de aplicaciones de mensajería), porque el expediente de 2026 es íntegramente Windows y no hay evidencia pública de componente móvil en esta campaña; la atribución estatal en su última milla, que la fuente de 2018 dejó deliberadamente abierta y que este informe no puede cerrar; y el análisis del código de AsioGate, por el motivo del Anexo B.1.

**3.3 Limitaciones de la colección.** Cinco, y la tercera es la que más duele.

1. **Sin telemetría propia.** `O-4` es un cuestionario. No sabemos si estamos afectados.
2. **Una sola intrusión confirmada.** Todo juicio sobre el alcance regional descansa en infraestructura de entrega y en más de cien ficheros SVG relacionados, no en víctimas. La fuente primaria es explícita en que valora esa parte con confianza moderada **y sigue investigando**.
3. **Una fuente relevante consultada y no reproducida.** El informe de Kaspersky de febrero de 2026 sobre la campaña AsioGate existe y es público en la red, pero lleva en portada una restricción de distribución explícita. Este repositorio publica `TLP:CLEAR`. La decisión y su fundamento están en el **Anexo B.1**; la consecuencia práctica es que **todo lo que este informe dice de esa campaña procede de la cita que hace de ella la fuente primaria y de la cobertura secundaria**, no del documento.
4. **El anexo de indicadores de la fuente primaria se declara parcial.** Dice literalmente que los indicadores publicados son *referential* y que la lista completa se entregó a sus clientes. Lo que tenemos es una muestra representativa, no el conjunto.
5. **Una fuente técnica de 2025 inaccesible.** El análisis de Positive Technologies sobre la evolución de las herramientas de Dark Caracal y la campaña de Poco RAT no se pudo leer en original por un fallo permanente de certificado TLS en su servidor. Lo que este informe dice de Poco RAT procede de cobertura secundaria y está marcado como tal en el Anexo B, con la fiabilidad degradada que corresponde.

**3.4 Metodología.** ICD 203 para el lenguaje estimativo, con probabilidad y confianza declaradas por separado. Código Admiralty doble para las fuentes (Anexo B). MITRE ATT&CK v18 para los procedimientos. Pirámide del Dolor para priorizar el esfuerzo de detección, con una conclusión poco habitual en `T-3`. Análisis de hipótesis competidoras y pre-mortem en `O-6`. **Y una técnica estructurada que este informe aplica de forma explícita: la verificación de cada afirmación del requisito contra la fuente primaria, consignando los resultados negativos.** Es el apartado siguiente.

**3.5 Lo que el requisito afirmaba, y lo que las fuentes sostienen.** Este informe nació de un requisito que describía al actor con cinco afirmaciones. Verificarlas una a una no es pedantería: dos de ellas, si se hubieran dado por buenas, habrían producido un informe que afirma más de lo que nadie ha publicado.

<!-- cti:table highlight="NO corroborado|Parcial" -->

| # | Afirmación del requisito | Veredicto | Qué dicen las fuentes |
|---|---|---|---|
| 1 | «Fuerte giro operativo hacia países hispanohablantes de Sudamérica entre 2025 y 2026» | **Corroborado** | El giro está documentado desde 2021 por la propia fuente primaria, y las campañas de 2024-2026 lo confirman. Si algo falla en la afirmación es la fecha de inicio: es anterior |
| 2 | «En 2026 introdujo el framework modular en Go GoCaracal, que utiliza contratos en la blockchain de Ethereum como mecanismo de respaldo para resolver su infraestructura C2» | **Corroborado, y con precisión** | Es exactamente lo que describe Arctic Wolf Labs el 26 de agosto de 2026. Incluido el detalle del mecanismo: `eth_getStorageAt` sobre el almacenamiento de un contrato, como respaldo y no como canal principal |
| 3 | «Mediante campañas de phishing con archivos `.SVG` armados y señuelos en la nube» | **Parcial** | El SVG armado está corroborado. **Los «señuelos en la nube» corresponden a las campañas de Poco RAT de 2024-2025** (enlaces de Google Drive y Dropbox a un archivo `.rev`), no a la cadena de 2026, que usa un acortador, un redirector intermedio, un dominio temático de documentos y un archivo 7-Zip. Mezclarlas produce una cadena de intrusión que nunca existió |
| 4 | «Contra entidades gubernamentales y de comunicaciones en la región andina» | **Parcial: comunicaciones sí, gubernamentales NO** | Comunicaciones sí: es el sector de la única víctima confirmada. **«Entidades gubernamentales» no aparece en ninguna fuente de 2026.** Y Venezuela no es «región andina» en el sentido en que el requisito usa el término —Colombia, Perú, Ecuador, Chile—, donde no hay víctima confirmada. Es `KJ-5` y la brecha `G-1` |
| 5 | «Distribuir Bandook y Poco RAT» en la región andina en 2025-2026 | **Parcial** | Bandook sí, en la intrusión de junio de 2026 en Venezuela. Poco RAT pertenece al ciclo 2024-2025 y su vínculo con 2026 no está establecido; la relación de sucesión entre las familias la **niega** la fuente primaria (`KJ-6`) |

> ⚠ **Por qué esta tabla va en §3 y no en un anexo.** Porque el error que
> corrige no es menor y es del tipo que esta cartera ya ha documentado tres
> veces: componer afirmaciones de campañas distintas, separadas por dos años,
> hasta construir una cadena de intrusión coherente que **ninguna fuente
> describe**. Un informe que empezara por «Dark Caracal ataca gobiernos andinos
> con SVG y señuelos en la nube» sería legible, útil en apariencia y falso en
> tres de sus cinco componentes. La disciplina no consiste en no equivocarse:
> consiste en que el documento diga en qué se apoya cada frase.

---

# NIVEL ESTRATÉGICO
### Para: Consejo · CISO · Riesgo · Legal · Horizonte: 6–24 meses

## E-1. Qué representa este actor, y qué representa su contrato

Dark Caracal importa por dos razones distintas, y conviene separarlas porque llevan a decisiones distintas.

**La primera es quién es.** Es un actor con nexo estatal declarado por una investigación conjunta de una organización de derechos digitales y un proveedor de seguridad móvil, operando desde un país que no tiene ninguna disputa geopolítica con Latinoamérica. Eso lo sitúa en una categoría incómoda: el espionaje estatal que esta cartera documenta suele tener un motivo legible —Gamaredon y Ucrania, Salt Typhoon y las telecomunicaciones occidentales, APT36 y la India—. Aquí el motivo no es legible desde la geopolítica. Un servicio de seguridad interior que opera masivamente contra empresas hispanohablantes de otro continente está haciendo algo que se explica mejor por **capacidad disponible y clientela** que por interés nacional. El informe de 2018 ya apuntaba en esa dirección al documentar que la infraestructura de Dark Caracal se solapaba con **Operation Manul**, una campaña contra disidentes kazajos: la misma infraestructura sirviendo a dos intereses nacionales distintos es el patrón de un proveedor, no de un servicio.

**La segunda es qué ha hecho con su canal de mando y control**, y es lo que convierte este informe en algo más que un perfil de actor regional.

<!-- cti:cards -->

| Cambio estructural | Por qué nos afecta | Etiqueta |
|---|---|---|
| El canal de configuración de respaldo vive en una cadena de bloques pública | **La retirada de infraestructura deja de funcionar para ese canal.** No hay abuso que denunciar, registrador al que escribir ni proveedor al que notificar. El valor está replicado en miles de nodos y es accesible por varios extremos RPC independientes | `01 · el fin de un modelo` |
| Y por la misma razón, es público | **La ventaja de información se invierte.** Podemos leer hoy la dirección que el adversario ha dejado preparada, con su historial de cambios y sus pruebas previas en una red de test. Ninguna otra pieza de infraestructura adversaria de esta cartera ofrece esto | `02 · el regalo` |
| El historial on-chain es permanente e inmutable | **El adversario tampoco puede borrarlo.** Los despliegues en Sepolia con direcciones RFC 1918 son su cuaderno de laboratorio, publicado para siempre. La financiación del monedero deja una traza que lleva a una entidad regulada | `03 · atribución` |
| El mecanismo se activa cuando defendemos | El disparador son los **fallos repetidos** contra el C2 principal. Nuestra medida evidente es su estímulo de diseño | `04 · secuencia` |
| Un proveedor de alojamiento sancionado, un año después de la sanción | Que 23 de 24 direcciones sigan en redes de Aeza Group en 2026, designado en julio de 2025, dice algo sobre la eficacia de la designación como medida de disrupción — y abre una pregunta de cumplimiento que no es técnica | `05 · sanciones` |

**Y una nota de calibración, porque la novedad invita a exagerarla.** Esto **no** es «mando y control sobre la cadena de bloques». La fuente primaria se cuida de decirlo: el mecanismo no pone el canal de C2 completo en Ethereum, sino que usa la cadena como **canal de configuración o buzón muerto resistente**. La diferencia es operativa y no retórica: el tráfico de órdenes y de datos sigue yendo a una dirección IP convencional, que sigue siendo bloqueable, atribuible y observable. Lo que no se puede retirar es el mecanismo que entrega **la dirección siguiente**. Quien lea esto como «ya no se puede bloquear nada» habrá sacado la conclusión opuesta a la correcta.

## E-2. Victimología

Aquí hay que ser cuidadoso con las cifras, porque **no hay cifras de víctimas**. Lo que hay es una víctima confirmada y una lista de países con infraestructura asociada. Presentar lo segundo como lo primero es el error que `KJ-4` existe para evitar.

<!-- cti:bars title="Qué nivel de evidencia sostiene cada país (escala: 3 = intrusión confirmada con IR · 2 = componentes de cadena reutilizados según fuente citada · 1 = artefactos e infraestructura asociados, confianza moderada)" -->

| País | Nivel de evidencia |
|---|---|
| Venezuela | `3` |
| Chile | `2` |
| Brasil | `2` |
| Ecuador | `1` |
| Colombia | `1` |
| El Salvador | `1` |
| Uruguay | `1` |

> **Lectura clave, y es incómoda.** Esa escala no mide actividad del
> adversario: mide **nuestra capacidad de verla**. Que Venezuela puntúe tres y
> Ecuador uno no significa que el actor opere tres veces más en Venezuela;
> significa que en Venezuela hubo una organización que contrató una
> investigación de respuesta a incidentes y un proveedor que publicó el
> resultado. La distribución de un mapa de víctimas construido sobre informes
> de proveedores es, en primer lugar, un mapa de quién compra respuesta a
> incidentes y de quién permite que se publique. `CTI-2026-025` dedica una
> sección a este sesgo con el nombre que le corresponde; se hereda aquí entera.

**Sobre sectores, lo que se puede decir es poco y conviene decirlo poco.** El sector de la víctima confirmada es **comunicaciones**. El criterio de selección que se deduce de los señuelos es **lingüístico y funcional, no sectorial**: correos con temática financiera y fiscal —facturas, cotizaciones— suplantando a empresas venezolanas de varios sectores. Eso significa que el destinatario buscado es quien abre facturas: contabilidad, administración, tesorería, compras. En términos de exposición propia, la pregunta no es «¿somos del sector que atacan?» sino «¿tenemos un buzón donde entran facturas de proveedores en español?». La respuesta es sí en todas las organizaciones de la región.

De la fase anterior del actor hay referencias a minería, manufactura y hostelería como sectores golpeados por Poco RAT desde 2022, pero proceden de cobertura secundaria y las fuentes no concuerdan entre sí: unas enfatizan minería y hostelería, otras tecnología y organizaciones financieras. No se usan para priorizar nada.

## E-3. Tendencia y pronóstico

La única serie temporal fiable que existe sobre este actor en 2026 no mide víctimas: mide **desarrollo de software**. Y resulta ser más informativa que un recuento de víctimas, porque un calendario de desarrollo revela intención y recursos.

<!-- cti:chart title="Fases de desarrollo del marco GoCaracal, por capacidad acumulada (escala ordinal de madurez, reconstruida sobre 249 muestras)" cap="No es un recuento de víctimas ni de muestras por mes: es la progresión de capacidad que la fuente primaria reconstruye en cuatro fases. Indicador de intención y de recursos, no de actividad." -->

| Periodo | Madurez |
|---|---|
| `Ene·26` | `1` |
| `Feb·26` | `2` |
| `Mar·26` | `2` |
| `Abr·26` | `2` |
| `May·26` | `3` |
| `Jun·26` | `4` |
| `Jul·26` | `4` |

Las cuatro fases que la fuente primaria describe son, literalmente: **fundación** en enero —comunicaciones básicas, perfilado de anfitrión, tareas cifradas y ejecución de código—; **modularización** de febrero a abril, cuando el desarrollador reorganiza el marco en componentes reutilizables de red, núcleo y ejecución, y añade soporte de C2 activo, descubrimiento de antivirus y consola interactiva; **expansión de capacidad** de mayo a junio, cuando aparece el build extendido con la funcionalidad posterior al compromiso; y **resiliencia operativa** de junio a julio, cuando aparece el respaldo en Ethereum.

Hay un detalle en ese calendario que merece atención y que la fuente primaria no subraya: **el contrato `BulletproofC2` se desplegó el 20 de mayo de 2026**, es decir, antes de la fase que la cronología de desarrollo sitúa en junio-julio, y la regla YARA se creó el 13 de julio. Eso no es una contradicción: encaja con que la capacidad se desarrollara y probara —primero en Sepolia— antes de incorporarse a los builds configurados. Pero sí dice algo: el mecanismo no fue una improvisación ante una retirada de infraestructura. **Fue planificado con semanas de antelación.**

<!-- cti:cards -->

| Escenario | Desarrollo | Etiqueta |
|---|---|---|
| **Más probable** | El marco sigue en desarrollo y el actor mantiene en paralelo Bandook y GoCaracal durante los próximos dos a cuatro trimestres, con el respaldo on-chain pasando de opcional a estándar en los builds extendidos. La campaña de entrega sigue siendo SVG con señuelos financieros en español, y el repertorio de dominios temáticos de documentos se renueva cada pocos meses | `Probable · 55–80 %` |
| **Alternativa creíble** | GoCaracal sustituye a Bandook en los próximos doce meses. La fuente primaria apunta en esta dirección —el marco nuevo cubre ya la mayoría de las capacidades históricas de Bandook— pero dice explícitamente que la evidencia actual muestra las dos familias operando en paralelo y **no** indica sustitución | `Posibilidad real · 45–55 %` |
| **La que hay que vigilar** | La técnica de respaldo on-chain se difunde. No tiene nada de específico de este actor, el contrato es trivial de escribir, y un buzón muerto en una cadena pública resuelve un problema que tienen todos los operadores de malware. Si se difunde, deja de ser una peculiaridad de Dark Caracal y pasa a ser una clase de tráfico que hay que saber detectar — y `D-1` pasa de detección de un actor a control de arquitectura | `Probable · 55–80 %` |
| **Baja probabilidad, alto impacto** | Aparece una variante que usa la cadena como canal de C2 completo, no sólo de configuración, con las órdenes codificadas en transacciones o en campos de datos. Eso sí eliminaría el punto de bloqueo convencional y obligaría a replantear la contención de red | `Poco probable · 20–45 %` |
| **Descartado, y se consigna** | Que la capacidad on-chain fuera código muerto o una prueba de concepto no usada. La fuente primaria lo falsa directamente: el historial de transacciones muestra que el valor configurado se cambió a una dirección IP pública | `Descartada` |

## E-4. Decisiones que este informe pide al nivel estratégico

<!-- cti:table highlight="OFAC|Legal|hoy" -->

| # | Decisión | Fundamento | Plazo |
|---|---|---|---|
| E-a | **Leer y registrar hoy** el valor almacenado en los cuatro contratos del Anexo A.2, con sello de fecha, antes de aplicar cualquier bloqueo | `KJ-2`, `KJ-3`. Es una llamada HTTP a un extremo público. Si se bloquea primero y se lee después, se ha empujado al implante a un canal no vigilado | **Hoy** |
| E-b | Instrumentar la vigilancia diaria de esos contratos y de la cartera `0x7D32…052F`, y **sólo entonces** aplicar el bloqueo de red del Anexo A.3 | `KJ-3`. El orden importa más que las medidas | 7 días |
| E-c | Desplegar `D-1`: detección de `eth_getStorageAt` y de resolución de extremos JSON-RPC públicos de Ethereum desde segmentos sin justificación de desarrollo | `KJ-2`. **Es la única detección de este informe que no caduca**, porque ataca el mecanismo y no el indicador | 14 días |
| E-d | **Decisión de Dirección con Legal**, no del SOC: posición de la organización frente a un proveedor de alojamiento designado por la OFAC con el que 23 de 24 direcciones de este actor se relacionan. Dos preguntas: ¿bloqueamos sus prefijos completos?, y ¿la designación nos obliga a algo más que a bloquear si detectamos tráfico propio hacia esas redes? | `KJ-7`. La segunda pregunta no es técnica y el SOC no puede responderla | 30 días |
| E-e | Barrido de parque en busca de `NTUSER.MAN` y del patrón de ruta `%AppData%\<12 hex>\<8 hex>.exe` | `X-2`. Artefactos duraderos, de falso positivo casi nulo, que sobreviven a la recompilación | 30 días |
| E-f | Dar por **no establecida** la cadena de linaje Poco RAT → AsioGate → GoCaracal en toda comunicación interna y externa, y dar por **no corroborada** la afirmación de objetivos gubernamentales regionales en 2026 | `KJ-5`, `KJ-6`, `§3.5`. Una decisión de higiene analítica: es más barato no afirmarlo que retractarlo | Inmediato |
| E-g | Añadir a la vigilancia de proveedores el requisito de notificación de intrusión con detalle de familia de malware para los proveedores de comunicaciones y los de servicios contables tercerizados en la región | `E-2`. El sector de la única víctima confirmada es comunicaciones, y el destinatario buscado es quien procesa facturas | 60 días |

---

# NIVEL OPERACIONAL
### Para: Jefatura de SOC · Respuesta a Incidentes · Threat Hunting · Horizonte: semanas–meses

## O-1. Identificación, alias y familias de malware

Dos tablas, porque aquí se mezclan dos cosas que no son lo mismo: **los nombres del actor** y **los nombres de su malware**. La confusión entre ambas es el origen del error que `§3.5` corrige.

**O-1.1 — Designaciones del actor**

| Designación | Origen | Grado de equivalencia |
|---|---|---|
| `Dark Caracal` | EFF y Lookout, enero de 2018 | **Referencia.** Es el nombre con el que se publicó el expediente fundacional |
| `G0070` | MITRE ATT&CK | **Equivalente.** Identificador de grupo |
| `GDGS` / Dirección General de Seguridad General del Líbano | Nexo estatal valorado por EFF y Lookout, recogido por Arctic Wolf y HivePro en 2026 | **No es un alias: es una atribución de patrocinio**, y su última milla quedó deliberadamente abierta por quien la hizo. Véase `O-2` |
| `Operation Manul` | EFF, 2016 | **Campaña distinta con infraestructura solapada**, contra disidentes kazajos. **No es un alias de Dark Caracal.** El solapamiento es el dato interesante, no la equivalencia |

**O-1.2 — Familias de malware atribuidas, y qué relación tienen entre sí**

| Familia | Lenguaje | Periodo documentado | Relación establecida con las demás |
|---|---|---|---|
| `Bandook` | Nativo, con sistema de plugins | 2007 en adelante como herramienta de mercado; en operaciones de Dark Caracal desde los años del expediente de 2018, y **activa en junio de 2026** | Herramienta histórica del actor. **Sigue en uso en paralelo a GoCaracal** |
| `CrossRAT` | Java, multiplataforma | 2017-2018 | Documentada en el expediente fundacional. Sin actividad reciente publicada |
| `Pallas` | Android | 2017-2018 | Familia móvil, distribuida en versiones troyanizadas de aplicaciones de mensajería. **Fuera del alcance de este informe**: el expediente de 2026 es íntegramente Windows |
| `Poco RAT` | Delphi (el implante) | 2024-2025 | Atribuida a Dark Caracal por Positive Technologies en marzo de 2025 **por solapamiento de oficio con Bandook**, no por identidad de código. El nombre viene de las bibliotecas POCO de C++ que emplea |
| `AsioGate` | C++ | Febrero de 2026 | Descrita por Kaspersky en la campaña de SVG. **Su relación de sucesión con Poco RAT procede de un agregador, no de Kaspersky** |
| `GoCaracal` | Go | Enero-julio de 2026 | **La fuente que hizo el análisis de código afirma que no hay evidencia de que suceda a AsioGate a nivel de código.** Papel funcional solapado, ecosistema de entrega e infraestructura compartidos |

> ⚠ **Nota de *tradecraft*, y es la razón de que haya dos tablas.** El impulso
> natural al leer seis familias en una línea temporal es dibujar una flecha
> entre ellas: Bandook → Poco RAT → AsioGate → GoCaracal, cuatro generaciones
> de una misma herramienta. **Esa flecha no existe en ninguna fuente, y la
> única que analizó el código la niega.** Lo que hay es un actor que opera
> varias familias a la vez, algunas compradas, algunas propias, algunas
> heredadas, y que en junio de 2026 se vio desplegando **dos de ellas en la
> misma intrusión**. Un árbol genealógico es una afirmación sobre desarrollo de
> software; un ecosistema solapado es una afirmación sobre operaciones. Sólo la
> segunda está sostenida.

## O-2. Estructura y atribución

| Eje de atribución | Valoración | Confianza |
|---|---|---|
| Clúster técnico | **Establecido.** 249 muestras con estructuras de paquete, módulos y flujos de ejecución compartidos conforman un marco único | Alta |
| Grupo organizado | **Establecido.** Catorce años de operaciones multiplataforma, calendario de desarrollo planificado en cuatro fases, pruebas en red de test antes de producción, separación deliberada de infraestructura por familia de malware | Alta |
| Nexo estatal | **Valorado, no probado, y quien lo valoró lo dijo.** EFF y Lookout rastrearon dispositivos de prueba del actor hasta un edificio de la GDGS en Beirut, y declararon que no podían descartar que fuera obra de un empleado al margen de la institución. El Líbano lo negó | Moderada |
| Identidad nominal | **Ninguna.** No hay personas identificadas, ni acusación, ni sanción contra este actor | Baja |
| Esta intrusión concreta | **Confianza media**, con esas palabras, por la convergencia de: uso de Bandook, características recurrentes del cargador en Delphi, señuelos financieros en español, SVG maliciosos, acortadores, infraestructura temática de documentos, preferencias de proveedor y selección consistente con el foco histórico | Moderada |

*Razonamiento de la fuente primaria, en sus términos:* el despliegue de GoCaracal junto al utillaje tradicional de Bandook y su infraestructura **«sugiere fuertemente»** que las operaciones son del mismo actor. Y añade un descargo que esta cartera valora y reproduce: la atribución refleja la valoración del laboratorio en el periodo del informe, puede evolucionar con evidencia nueva, y las referencias a identidad, nexo e intención del actor son **juicios analíticos, no afirmaciones de hecho jurídico**.

*Contraargumento que hay que mantener vivo:* el patrón de un actor cuya infraestructura sirvió a dos intereses nacionales distintos —Líbano y Kazajistán, según el expediente de 2016-2018— es compatible con un proveedor de servicios ofensivos más que con un servicio de inteligencia operando en su propio nombre. Si eso fuera así, la pregunta «¿por qué el Líbano espía empresas chilenas?» estaría mal planteada, y la correcta sería «¿quién paga por espiar empresas chilenas?». Ninguna fuente pública de 2026 permite decidirlo. Es la brecha `G-3`.

## O-3. Modelo de operación: tres capas de infraestructura, deliberadamente separadas

Lo que distingue a este actor operacionalmente no es ninguna de sus herramientas: es cómo organiza su infraestructura. Hay tres capas, y están separadas a propósito.

**Capa de entrega.** Siete dominios relacionados, con convenciones de nombre, relaciones de alojamiento y patrones de registro compartidos, todos de temática documental y en español: `getpdfdigital[.]cloud`, `getpdf[.]digital`, `visualizarpdf[.]online`, `contabilidad[.]icu`, `soportedigital[.]cloud`, `documentodigital[.]cloud`, `gestionadocs[.]me`. Dos de ellos ya estaban vinculados a actividad previa de Dark Caracal. Uno se registró en julio de 2026 y se observó entregando GoCaracal, lo que indica que la capa **se mantiene y se amplía activamente**. Nótese la elección de TLD —`.cloud`, `.digital`, `.online`, `.icu`, `.me`—, que es precisamente el patrón que `CTI-2026-018` documenta.

**Capa de C2 por familia, y aquí está la decisión de diseño.** De las 24 direcciones de C2 extraídas de muestras de GoCaracal, **23 están en redes operadas por Aeza Group**. Las de Bandook, en cambio, están en **AlexHost**. La fuente primaria lee esa separación como un intento de limitar el efecto de una disrupción de infraestructura que afecte a una familia, y añade con honestidad que también podría reflejar simplemente prácticas distintas de adquisición o gestión. Ambas lecturas tienen la misma consecuencia defensiva: **una retirada que acierte con Bandook no toca GoCaracal, y al revés**.

**Capa de resiliencia, que es nueva.** Por encima de las dos anteriores, el contrato. Su función es precisamente sobrevivir a la pérdida de la segunda capa.

> **Lo que este diseño nos dice del adversario.** Compartimentar la
> infraestructura por familia de malware es una decisión que sólo toma quien ha
> perdido infraestructura antes, o quien ha visto perderla. Y añadir un canal
> de resolución que no se puede retirar es la respuesta a una amenaza concreta:
> la incautación. **Este actor está diseñando contra nuestras medidas de
> disrupción, no contra nuestras medidas de detección.** Eso es informativo
> sobre dónde ha sentido presión.

## O-4. Nuestra exposición

> ⬛ **Sección sin evaluar — requiere telemetría interna.** No hay telemetría
> propia en este informe. Lo que sigue es el cuestionario que la convierte en
> hallazgo, ordenado por facilidad de respuesta. Las tres primeras preguntas se
> responden hoy y sin herramientas nuevas.

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| X-1 | ¿Existe en el parque **algún** fichero `NTUSER.MAN`? En un entorno sin perfiles obligatorios, la respuesta esperada es cero | EDR · barrido de sistema de ficheros | TI/Puesto |
| X-2 | ¿Hay ejecutables en rutas que casen con `AppData\Roaming\[0-9a-f]{12}\[0-9a-f]{8}\.exe`? | EDR · telemetría de creación de proceso y de fichero | SOC |
| X-3 | ¿Ha salido tráfico hacia alguno de los siete dominios de entrega o las 29 direcciones del Anexo A.3, en los últimos 12 meses? **Retrohunt, no bloqueo** | Proxy · DNS · NetFlow | SOC |
| X-4 | ¿Se resuelve o se alcanza algún extremo JSON-RPC público de Ethereum desde puestos de usuario? ¿Desde cuáles y con qué justificación? | DNS · proxy · TLS SNI | SOC · Arquitectura |
| X-5 | ¿Permitimos la entrada de adjuntos `.svg` por correo? ¿Se inspecciona su contenido, o se trata como imagen? | Pasarela de correo | Seguridad de correo |
| X-6 | ¿Permitimos la entrada de archivos 7-Zip, y la ejecución de binarios extraídos de ellos en `%AppData%`? | Pasarela · AppLocker/WDAC | TI/Puesto |
| X-7 | ¿Tenemos política sobre acortadores de URL en correo entrante? ¿Se expanden y se evalúa el destino final, incluidos los redirectores intermedios? | Pasarela de correo | Seguridad de correo |
| X-8 | ¿Qué departamentos reciben facturas y cotizaciones de proveedores en español desde direcciones externas, y qué privilegios tienen esos puestos? | Inventario · RR. HH. · Compras | Riesgo |
| X-9 | ¿Bloquea nuestro perímetro los prefijos de los sistemas autónomos de Aeza Group? ¿Hay tráfico legítimo propio hacia ellos que lo impida? | NetFlow · BGP | Redes |
| X-10 | Para los proveedores de comunicaciones y de contabilidad tercerizada: ¿tenemos cláusula de notificación de intrusión con detalle de familia de malware? | Contratos | Legal · Compras |

## O-5. Cronología

<!-- cti:timeline -->

| Fecha | Hecho | Traza |
|---|---|---|
| `2012-01` | Primeras campañas de Dark Caracal documentadas. Inicio de la ventana de actividad que la fuente de 2018 reconstruye | Global |
| `2016` | EFF publica **Operation Manul**, contra disidentes kazajos. Su infraestructura se solapará con la de Dark Caracal | Global |
| `2018-01-18` | **EFF y Lookout publican «Dark Caracal: Cyber-Espionage at a Global Scale».** Rastrean dispositivos de prueba hasta un edificio de la GDGS en Beirut; cientos de gigabytes exfiltrados, más de 21 países, miles de víctimas. El Líbano lo niega | Global |
| `2021` | **La fuente primaria sitúa aquí el giro:** foco operativo creciente sobre países hispanohablantes, particularmente en Latinoamérica | **LATAM** |
| `2022-03` | EFF documenta una campaña nueva de Dark Caracal, con cientos de infecciones en más de una docena de países | Global |
| `2024-07` | Primera cobertura pública de **Poco RAT** contra víctimas hispanohablantes | **LATAM** |
| `2025-03` | Positive Technologies atribuye **Poco RAT a Dark Caracal**. Objetivos: empresas de habla hispana, con Venezuela, Chile, Colombia, Ecuador y República Dominicana entre los países citados. Entrega por enlaces de nube a un archivo `.rev` | **LATAM** |
| `2025-07-01` | **La OFAC designa a Aeza Group** y filiales como proveedor de alojamiento a prueba de balas, en coordinación con la NCA británica | Global |
| `2026-01` | **Fase 1 de GoCaracal.** Comunicaciones básicas, perfilado de anfitrión, tareas cifradas y ejecución de código | — |
| `2026-02` | **Kaspersky publica la campaña de AsioGate**: señuelos financieros en español, adjuntos SVG, acortadores y cargador en Delphi. Venezuela principalmente, con **componentes reutilizados contra Chile y Brasil** | **LATAM** |
| `2026-02 → 04` | Fase 2: modularización del marco en componentes reutilizables, C2 activo, descubrimiento de antivirus, consola interactiva | — |
| `2026-05-20` | **Se despliega el contrato `BulletproofC2`** en Ethereum. Semanas antes de que la capacidad aparezca en builds configurados: fue planificado | Global |
| `2026-05 → 06` | Fase 3: aparece el build extendido con la funcionalidad posterior al compromiso | — |
| `2026-06` | **Arctic Wolf Labs investiga una intrusión dirigida contra una organización de comunicaciones en Venezuela.** Se despliegan el GoCaracal ligero, un cargador en Delphi con Bandook, y el GoCaracal extendido | **LATAM** |
| `2026-06 → 07` | Fase 4: **resiliencia operativa**. El respaldo en Ethereum aparece en los builds extendidos configurados | — |
| `2026-07` | Se registra un dominio nuevo de la capa de entrega, observado entregando GoCaracal. La capa se amplía | **LATAM** |
| `2026-07-13` | Fecha de creación de la regla YARA publicada | — |
| `2026-08-26` | **Arctic Wolf Labs publica «Dark Caracal Reloaded».** 249 muestras, dos perfiles de compilación, el respaldo on-chain y el anexo de indicadores | Global |
| `2026-11-17` | Emisión de este informe. **Ninguna fuente pública ha documentado todavía una intrusión confirmada de esta campaña en Chile, Colombia, Perú o Ecuador** | **Chile / LATAM** |

## O-6. Hipótesis alternativas consideradas

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| **H1 — GoCaracal es de Dark Caracal** | Consistente con el despliegue conjunto con Bandook en la misma intrusión, el cargador en Delphi recurrente, la preferencia de proveedor, los señuelos en español y la selección regional. La fuente primaria lo valora con confianza media y lo llama «fuertemente sugerido» | `Retenida · probable 55–80 %` |
| **H2 — Es un suministrador que vende a Dark Caracal y a otros** | Consistente con el solapamiento histórico de infraestructura entre Dark Caracal y Operation Manul, que ya mostró infraestructura común sirviendo a dos intereses nacionales distintos. **No se puede descartar con lo publicado.** Si fuera cierta, la atribución al Líbano seguiría siendo correcta sobre *un* cliente y errónea sobre *el* actor | `Retenida · posibilidad real 45–55 %` |
| **H3 — El respaldo on-chain es código de prueba sin uso real** | **Falsada.** El historial de transacciones muestra que el valor configurado se cambió a una dirección IP pública. La propia fuente lo señala como evidencia de que el mecanismo no era código inactivo | `Descartada` |
| **H4 — GoCaracal sustituye a Bandook** | Inconsistencia directa: en la misma intrusión se despliegan los dos. La fuente primaria dice que el marco nuevo **complementa** y «podría reducir» la dependencia futura, y que la evidencia actual **no** indica sustitución | `Poco probable · 20–45 %, por ahora` |
| **H5 — Hay víctimas confirmadas en Chile, Colombia o Ecuador que no se han publicado** | Sin evidencia pública. Consistente con el sesgo de `E-2`: la ausencia de informes de respuesta a incidentes publicados en esos países no es ausencia de intrusiones. **Se retiene como hipótesis de caza, no como juicio** | `Retenida para caza` |
| **H6 — El actor atacó entidades gubernamentales andinas en 2026** | **Sin evidencia de 2026 en absoluto.** Procede del requisito, no de una fuente. Se consigna para que no se reabra como si fuera un hallazgo | `Descartada como hallazgo · brecha G-1` |
| **H7 — La técnica on-chain la copiarán otros actores** | No es una hipótesis sobre este actor sino sobre la clase. El contrato es trivial de escribir, el mecanismo resuelve un problema universal de los operadores de malware, y el coste es de céntimos. **Se retiene y es el motivo de que `D-1` se priorice sobre cualquier indicador** | `Retenida · probable 55–80 %` |

**Supuesto clave.** Que el valor almacenado en el contrato es, cuando está puesto, **infraestructura real del actor y no un señuelo**. Si el actor empezara a escribir valores falsos deliberadamente —sabiendo que los defensores los leen—, la vigilancia del contrato pasaría de fuente de inteligencia a fuente de ruido, y las direcciones leídas de ahí dejarían de ser bloqueables sin verificación. **Qué se rompe si es falso:** `E-a`, `E-b` y buena parte del valor de `H-1`. La mitigación es no bloquear nunca una dirección leída del contrato sin corroborarla, y tratarla como señal de caza. Está escrito así en la columna de acción permitida del Anexo A.2.

**Pre-mortem.** Es mayo de 2027 y este informe resultó equivocado. Los tres motivos más probables, en orden:

1. **Nos quedamos con la mitad brillante.** El informe dedicó su mejor prosa al contrato de Ethereum y el lector concluyó que lo importante era eso, cuando la vía de entrada real seguía siendo un adjunto SVG en un correo con una factura falsa. El canal de respaldo es analíticamente interesante; **el vector es aburrido y es el que hay que cerrar**. Si alguien despliega `D-1` y no toca la política de adjuntos de `X-5`, este informe habrá hecho daño.
2. **La gradación de `KJ-4` se perdió en la segunda reunión.** Alguien citó «Chile, Colombia y Ecuador» de este informe sin la palabra «moderada» ni la frase «sin víctima confirmada», y el dato circuló como hecho. Es exactamente lo que `CTI-2026-030` documenta que pasó con otro actor.
3. **La campaña cambió de familia y seguimos cazando GoCaracal.** El actor opera varias familias en paralelo y ha demostrado que desarrolla una nueva en seis meses. Las detecciones basadas en cadenas de Go de `X-3`/`D-3` tienen fecha de caducidad corta; las de `D-1`, `D-2` y `D-5` no.

## O-7. Indicadores y señales de alerta

| # | Indicador observable | Qué señalaría | Disciplina | Responsable |
|---|---|---|---|---|
| I-1 | **Escritura nueva en el almacenamiento de cualquiera de los cuatro contratos del Anexo A.2** | Campaña activa y **C2 siguiente conocido antes de su uso**. Es el indicador de mayor valor y el más barato de este informe | OSINT · on-chain | Célula CTI |
| I-2 | Despliegue de un contrato nuevo desde la cartera `0x7D32…052F` | Infraestructura de respaldo nueva en preparación. Revisión anticipada del informe | OSINT · on-chain | Célula CTI |
| I-3 | Actividad nueva de esa cartera en **Sepolia** | Fase de desarrollo o validación: suele preceder a la red principal. **Alerta temprana con semanas de margen** | OSINT · on-chain | Célula CTI |
| I-4 | Registro de dominios nuevos con el patrón `<verbo/sustantivo documental en español>.<cloud\|digital\|online\|icu\|me>` | Ampliación de la capa de entrega | OSINT · vigilancia de registro | Célula CTI |
| I-5 | Publicación por cualquier proveedor de una intrusión **confirmada** en Chile, Colombia, Perú o Ecuador | Convierte `KJ-4` de inferencia en hecho. Revisión inmediata | OSINT | Célula CTI |
| I-6 | Aparición de muestras de GoCaracal con `CONTRACT` en una cadena distinta de Ethereum | Ampliación de la superficie de `D-1` a otros extremos RPC | OSINT · TECHINT | Célula CTI |
| I-7 | Un segundo actor usando resolución de C2 por almacenamiento de contrato | `H7` confirmada. `D-1` pasa de detección de actor a control de arquitectura | OSINT | Célula CTI |
| I-8 | Retirada o sanción de Aeza Group que surta efecto en el enrutamiento | Fuerza migración de infraestructura y, muy probablemente, el primer uso masivo del respaldo | OSINT | Célula CTI |

---

# NIVEL TÁCTICO
### Para: Analistas de SOC · Ingeniería de Detección · Threat Hunting · Horizonte: días–semanas

## T-1. Cadena de intrusión

<!-- cti:stages title="De un adjunto de imagen a un marco modular con respaldo en una cadena de bloques" dwell="next" -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 01 · Entrega | Un SVG que es un navegador, no una imagen | correo con factura o cotización en español · adjunto `.svg` · URL acortada en `base64` dentro del fichero · redirector intermedio · dominio temático de documentos · archivo 7-Zip |
| Etapa 02 · Pie en la puerta | El implante pequeño entra, perfila y entrega | `tf-oficina004a9.exe` · GoCaracal ligero en Go · protocolo de paquetes propio con `AES-GCM` · perfilado de usuario, anfitrión, SO, *uptime*, ventana activa y **productos de seguridad** · descarga y ejecución · *shellcode* e inyección |
| Etapa 03 · Instalación y permanencia | El cargador en Delphi trae dos cosas a la vez | cargador en Delphi · **Bandook actualizado** con identificadores de comando aleatorizados · **GoCaracal extendido** `v1.0.1`–`v1.0.6` con 34 manejadores · manipulación de *hives* del registro · `NTUSER.MAN` oculto asociado a un flujo de clave `Run` |
| Etapa 04 · Recolección y resiliencia | Lo que se llevan, y cómo sobreviven a que les cortemos | *cookies* y bases de datos de credenciales de **Chrome, Brave y Firefox** · registro de teclas · escritorio remoto por **WebRTC** · VNC oculto · **clonado del perfil de Chrome a una sesión de navegador oculta** · proxy `SOCKS5` en banda · **respaldo de C2 por `eth_getStorageAt` sobre contrato de Ethereum** |

**Permanencia:** no publicada. La fuente primaria no da tiempos de permanencia ni mediana de detección. Lo que sí publica es la ventana de desarrollo —enero a julio de 2026— y la fecha de la intrusión investigada, junio de 2026. **La ausencia de este dato es la brecha `G-4`** y conviene no rellenarla con el valor de otro actor: un marco con proxy `SOCKS5`, escritorio remoto y recolección de navegador está construido para quedarse meses, no horas, pero eso es una inferencia de diseño y no una medición.

**Dos observaciones sobre esta cadena que cambian dónde se pone el esfuerzo.**

**La primera: el SVG no es un adjunto de imagen, es un documento ejecutable.** Un fichero SVG es XML, y el estándar admite contenido embebido —incluido *script*— que el navegador ejecuta al abrirlo. Eso es lo que convierte a un formato que todas las pasarelas tratan como imagen inofensiva en un vehículo de *smuggling*: la URL va dentro, codificada en `base64`, y el fichero que atraviesa la pasarela no contiene ninguna URL que inspeccionar. La fuente primaria no recuperó el SVG original de esta intrusión, pero sí uno análogo de la misma infraestructura y el mismo periodo, y **más de cien ficheros SVG relacionados comunicando con el mismo sitio de alojamiento malicioso**. Un adjunto por víctima potencial: ese centenar largo es el único número de volumen que tenemos sobre la campaña de entrega, y la fuente no da más precisión.

**La segunda: hay dos saltos de confianza seguidos, y el segundo es el que se puede cortar sin falsos positivos.** El primero —el usuario abre el adjunto— es un problema de concienciación y de política de pasarela. El segundo —un binario extraído de un archivo 7-Zip descargado desde un dominio registrado hace semanas se ejecuta desde `%AppData%`— es un problema de control de ejecución, y se cierra con una regla de lista blanca que no necesita saber nada de este actor. `X-5` lo detalla.

## T-2. Mapa MITRE ATT&CK

La fuente primaria no publica identificadores de técnica. La tabla siguiente combina la lista que sí publica HivePro con el mapeo propio de los procedimientos descritos por Arctic Wolf; **la última columna dice de dónde sale cada fila**, porque un mapeo propio y uno de proveedor no tienen la misma autoridad.

<!-- cti:matrix -->

| Táctica | ID | Técnica | Procedimiento observado |
|---|---|---|---|
| Desarrollo de recursos | T1583.001 | Acquire Infrastructure: Domains | Siete dominios temáticos de documentos en español, con convenciones de nombre y patrones de registro compartidos; uno registrado en julio de 2026 *(HivePro)* |
| Desarrollo de recursos | T1583.003 | Acquire Infrastructure: Virtual Private Server | 23 de 24 direcciones de C2 de GoCaracal en redes de Aeza Group; las de Bandook en AlexHost *(HivePro)* |
| Desarrollo de recursos | T1583.006 | Acquire Infrastructure: Web Services | **Despliegue de cuatro contratos `BulletproofC2` en Ethereum**, primero en Sepolia y después en la red principal, desde una sola cartera *(mapeo propio)* |
| Desarrollo de recursos | T1608.001 | Stage Capabilities: Upload Malware | `getpdfdigital[.]cloud` entrega el archivo 7-Zip con el implante *(HivePro)* |
| Acceso inicial | T1566.001 | Phishing: Spearphishing Attachment | Correo con temática financiera y fiscal en español, suplantando empresas venezolanas de varios sectores, con adjunto `.svg` *(HivePro)* |
| Ejecución | T1204.002 | User Execution: Malicious File | El destinatario abre el SVG; el contenido embebido dirige el navegador a la URL acortada *(HivePro)* |
| Defensa | T1027.006 | Obfuscated Files or Information: HTML Smuggling | **URL acortada codificada en `base64` dentro del fichero SVG.** La pasarela no ve ninguna URL que inspeccionar *(mapeo propio; HivePro lo agrupa como T1027)* |
| Ejecución | T1059.003 | Command and Scripting Interpreter: Windows Command Shell | Consola interactiva en ambos perfiles de compilación *(HivePro)* |
| Ejecución | T1106 | Native API | `main.loadAPIs` en el build ligero: resolución dinámica de API nativas *(mapeo propio, desde la regla YARA)* |
| Persistencia | T1547.001 | Registry Run Keys / Startup Folder | Flujo de clave `Run` asociado al artefacto `NTUSER.MAN` *(HivePro)* |
| Persistencia | T1112 | Modify Registry | Manipulación de *hives* del registro como comportamiento de persistencia del build extendido *(HivePro)* |
| Defensa | T1564.001 | Hide Artifacts: Hidden Files and Directories | **Creación de un `NTUSER.MAN` oculto** *(HivePro)* |
| Defensa | T1070.004 | Indicator Removal: File Deletion | Borrado y renombrado de ficheros entre las funciones de ciclo de vida del build extendido *(HivePro)* |
| Defensa | T1036.005 | Masquerading: Match Legitimate Name or Location | `tf-oficina004a9.exe`, `VRJDL_21812.exe`, `7676230602QQ.exe`: nombres de apariencia administrativa o de identificador de trámite *(HivePro)* |
| Defensa | T1055 | Process Injection | Inyección de código en otro proceso; `main.InjectShellcode` y `main.injectShellcodeWoW64` *(HivePro)* |
| Defensa | T1140 | Deobfuscate/Decode Files or Information | Decodificación del `base64` del SVG y del *payload* de Bandook cifrado *(HivePro)* |
| Defensa | T1497 | Virtualization/Sandbox Evasion | `main.smartSleep`: temporización adaptativa *(mapeo propio, desde la regla YARA)* |
| Descubrimiento | T1518.001 | Software Discovery: Security Software Discovery | `main.detectAntivirus` y `main.AntivirusProduct`: recolección de productos de seguridad en el perfilado inicial *(HivePro)* |
| Descubrimiento | T1082 | System Information Discovery | Usuario, nombre de anfitrión, SO, *uptime*; `getRawOSVersion` *(HivePro)* |
| Descubrimiento | T1057 | Process Discovery | Enumeración de procesos en el build extendido *(HivePro)* |
| Descubrimiento | T1083 | File and Directory Discovery | Listado de directorios, descubrimiento de unidades y **búsqueda recursiva de ficheros** *(HivePro)* |
| Descubrimiento | T1010 | Application Window Discovery | Ventana activa; `main.lastInputInfo` *(HivePro)* |
| Credenciales | T1555.003 | Credentials from Password Stores: Credentials from Web Browsers | Bases de datos de credenciales de Chrome, Brave y Firefox (Bandook); bases de datos de *login* del navegador (GoCaracal extendido) *(HivePro)* |
| Credenciales | T1539 | Steal Web Session Cookie | Recolección de *cookies* de navegador *(HivePro)* |
| Credenciales | T1056.001 | Input Capture: Keylogging | Registro de teclas en el build extendido *(HivePro)* |
| Recolección | T1185 | Browser Session Hijacking | **Clonado del perfil local de Chrome a una sesión de navegador oculta e independiente.** La sesión autenticada de la víctima, operada por el adversario, sin credenciales *(mapeo propio)* |
| Recolección | T1005 | Data from Local System | Descarga de ficheros y búsqueda dirigida *(HivePro)* |
| Mando y control | T1105 | Ingress Tool Transfer | Descarga de contenido desde URL; el ligero entrega el cargador en Delphi *(HivePro)* |
| Mando y control | T1573.001 | Encrypted Channel: Symmetric Cryptography | **Protocolo de paquetes propio protegido con `AES-GCM`**; `readSecurePacket` y `SendSecurePacket` *(HivePro)* |
| Mando y control | T1071.001 | Application Layer Protocol: Web Protocols | Agente de usuario `Mozilla/5.0 (Windows NT 10.0; Win64; x64)`, sin cadena de navegador completa *(HivePro)* |
| Mando y control | T1102.001 | Web Service: Dead Drop Resolver | **`eth_getStorageAt` contra un extremo JSON-RPC público de Ethereum para leer la dirección de C2 de reemplazo del almacenamiento del contrato `BulletproofC2`.** El buzón muerto que no se puede retirar; `RPCFallback` en la regla YARA *(HivePro lo lista; el procedimiento es de Arctic Wolf)* |
| Mando y control | T1090.001 | Proxy: Internal Proxy | **Proxy `SOCKS5` en banda**: el anfitrión comprometido como punto de tránsito del tráfico del operador *(HivePro)* |
| Mando y control | T1219.002 | Remote Access Tools: Remote Desktop Software | Escritorio remoto basado en **WebRTC** y comportamiento de VNC oculto *(HivePro)* |
| Exfiltración | T1041 | Exfiltration Over C2 Channel | Por el mismo canal cifrado. **No se identificó canal de exfiltración separado** *(HivePro)* |

> ⚠ **Una técnica de esta tabla merece lectura aparte, y no es la de Ethereum.**
> `T1185`, el clonado del perfil de Chrome a una sesión oculta, **elude la
> autenticación multifactor sin atacarla**. No roba una contraseña ni
> intercepta un segundo factor: copia una sesión ya autenticada y la opera en
> paralelo, de modo que para el servicio de destino el acceso es el del usuario
> legítimo, desde su propio equipo, con su propio navegador. En una
> organización que haya puesto su defensa de identidad en el MFA y su
> detección en los inicios de sesión anómalos, **este procedimiento no genera
> ni un solo evento**. La contramedida no es de puesto: es de lado del
> servicio —vinculación de sesión al dispositivo, detección de uso concurrente
> de la misma *cookie*, y acortamiento de la vida de la sesión en las
> aplicaciones sensibles—.

## T-3. Dónde atacamos en la Pirámide del Dolor

<!-- cti:pyramid -->

| Nivel | Qué contiene en este informe y qué vale | Valor |
|---|---|---|
| Hashes | **Cinco SHA-256, y la propia fuente los declara *referential*.** Son binarios en Go: cambian con cada compilación, y el expediente documenta 249 muestras de siete meses. Valor preventivo nulo. **Sólo retrohunt.** Y una advertencia de higiene que esta cartera hace cada vez: uno de los hashes circula truncado a 63 caracteres en cobertura secundaria; el valor correcto está en el Anexo A.1 | Base · valor trivial |
| IP · Dominios | 29 direcciones y 7 dominios. Aquí hay una **inversión respecto a lo habitual**: estos indicadores no sólo caducan rápido, sino que **bloquearlos activa el mecanismo de respaldo**. Siguen siendo necesarios, pero su uso tiene un orden obligatorio (`E-a`, `E-b`). El nivel útil no es la dirección individual, es **el prefijo y el sistema autónomo** | Valor bajo · **y con secuencia obligatoria** |
| Artefactos | **El nivel más rentable de este informe.** `NTUSER.MAN` en un entorno sin perfiles obligatorios es un hallazgo con falso positivo próximo a cero. El patrón de ruta `AppData\<12 hex>\<8 hex>.exe` sobrevive a la recompilación. Las cadenas de versión `v1.0.1`–`v1.0.6` y los nombres de función de Go persisten entre *builds* del mismo marco | Valor medio · **empezar aquí** |
| Herramientas | 7-Zip, SVG, acortadores de URL, WebRTC, `SOCKS5` y **extremos JSON-RPC públicos de Ethereum**: todas legítimas, todas con uso corporativo real. Se detectan por contexto —quién, desde dónde, con qué justificación—, nunca por presencia | Valor alto |
| TTP | **La cima, y en este informe tiene un nombre concreto: resolución de C2 por buzón muerto en una cadena de bloques pública.** Es independiente del contrato, del actor y de la familia de malware. `D-1` la detecta en 2026 y la seguirá detectando cuando el tercer actor que la copie no se parezca en nada a éste. Y la segunda TTP de la cima no es técnica: **el adjunto SVG como vehículo de *smuggling* de carga** | Cima · valor máximo |

> **Por qué, excepcionalmente, el consejo de este informe es empezar por el
> tercer nivel y no por la cima.** La doctrina de la Pirámide del Dolor dice
> concentrar el esfuerzo arriba, y esta cartera la sigue. Pero aquí hay un
> atajo que no suele existir: dos artefactos de host —`NTUSER.MAN` y el patrón
> de ruta hexadecimal— se comprueban en un barrido de parque de una tarde, no
> necesitan ingeniería de detección, no tienen falsos positivos apreciables y
> responden la única pregunta que `O-4` no puede responder: **si estamos
> dentro del expediente**. Hacer eso primero no es renunciar a la cima: es
> ordenar las dos cosas por lo que tardan en dar respuesta.

## T-4. Hipótesis de caza prioritarias

<!-- cti:accordion critical="^(H-1|H-2|H-3)\b" regional="^H-1[0-2]\b" -->

**H-1 — El contrato tiene un valor escrito ahora mismo, y lo podemos leer antes que el implante.** No es una hipótesis de caza en el sentido habitual: no se busca en nuestros registros, se consulta la infraestructura del adversario. Una petición JSON-RPC a cualquier extremo público de Ethereum contra los cuatro contratos del Anexo A.2, leyendo el espacio de almacenamiento, devuelve el valor que los implantes leerán si pierden su C2 principal. Se ejecuta en segundos, cuesta cero y **se puede automatizar en un cron diario**. Fidelidad: no aplica —es colección, no detección—. El producto es una dirección IP que **no se bloquea**: se busca retrospectivamente en NetFlow y en proxy, se compara con el valor del día anterior y se registra el cambio con fecha. Un cambio de valor es `I-1` y dispara revisión del informe. Precaución obligatoria: véase el supuesto clave de `O-6` sobre la posibilidad de valores señuelo.

**H-2 — Alguien en nuestra red habla con un extremo JSON-RPC de Ethereum, y no es de desarrollo.** La hipótesis de detección central de este informe. Buscar, en registros de DNS, de proxy y de SNI de TLS, resolución o conexión hacia extremos RPC públicos —`cloudflare-eth.com`, `mainnet.infura.io`, `eth-mainnet.g.alchemy.com`, `rpc.ankr.com`, `eth.llamarpc.com`, `ethereum-rpc.publicnode.com`, `eth.drpc.org`, `1rpc.io`— desde cualquier segmento de puesto de usuario. En una organización que no desarrolla sobre cadenas de bloques, el resultado esperado es cero, y cada acierto es investigable en minutos. Donde haya inspección del cuerpo de la petición, el discriminador fino es el método `eth_getStorageAt`: un desarrollador consulta saldos y transacciones; **leer el almacenamiento crudo de un contrato que no es suyo es un patrón estrecho**. Fidelidad: alta en entornos sin desarrollo Web3, media donde lo haya. Falsos positivos conocidos: extensiones de navegador de monedero —MetaMask y similares—, que son por sí mismas un hallazgo de política; herramientas de analítica financiera; y algún instalador que consulta precios de criptoactivos. Ventana recomendada: 180 días hacia atrás, y permanente hacia delante.

**H-3 — Existe un `NTUSER.MAN` en algún perfil de usuario.** Un `NTUSER.MAN` es la variante de perfil obligatorio del fichero de *hive* de usuario: cuando está presente, Windows lo usa con preferencia sobre `NTUSER.DAT` y el perfil se vuelve de sólo lectura. En una organización que no despliega perfiles obligatorios —la inmensa mayoría— **no debería existir ni uno**. El actor crea uno, oculto, asociado a un flujo de clave `Run`. Buscar en todo el parque cualquier fichero con ese nombre, y en particular con atributo de oculto, bajo `C:\Users\*\`. Fidelidad: muy alta. Falsos positivos: sólo en entornos con perfiles obligatorios heredados, que se enumeran una vez y se listan como excepción conocida. **Es la comprobación con mejor relación entre coste y conclusión de todo el informe.**

**H-4 — Un ejecutable con nombre hexadecimal corre desde un directorio con nombre hexadecimal en `AppData`.** Las dos rutas publicadas son `%AppData%\Roaming\d30547514515\91ed375e.exe` y `%AppData%\Roaming\e1d58f51c58a\5c0416e4.exe`. El patrón generalizable, y no las rutas literales, es lo que hay que cazar: un directorio de **doce** caracteres hexadecimales que contiene un ejecutable de **ocho** caracteres hexadecimales, en el árbol de datos de aplicación móviles del usuario. Expresión regular: `\\AppData\\Roaming\\[0-9a-f]{12}\\[0-9a-f]{8}\.exe`. **Nota de transcripción importante:** las fuentes escriben la ruta como `%AppData%\Roaming\…`, lo que es redundante —la variable `%AppData%` ya apunta a `…\AppData\Roaming`— de modo que **una detección que busque literalmente la cadena `%AppData%\Roaming\` nunca casará con nada**. Hay que cazar la ruta expandida. Fidelidad: alta. Falsos positivos: algunos instaladores y actualizadores usan directorios de nombre GUID, que no casan con este patrón por longitud y por alfabeto.

**H-5 — Entró un adjunto SVG por correo en los últimos doce meses.** Pregunta de retrohunt sobre la pasarela, previa a cualquier cambio de política. Enumerar todos los adjuntos `.svg` recibidos, su remitente, su destinatario y su tamaño. Un SVG legítimo en correo corporativo es raro —un logotipo, un diagrama de un proveedor de diseño— y la lista completa de un año cabe en una pantalla en casi cualquier organización. Para los que haya, inspeccionar el XML en busca de contenido embebido: etiquetas `<script>`, atributos de evento, elementos `<foreignObject>`, y cualquier cadena larga en `base64`. Fidelidad: alta como ejercicio de inventario; el objetivo real es decidir `X-5` con datos propios en lugar de a ciegas.

**H-6 — Un binario extraído de un archivo 7-Zip descargado por el navegador se ejecutó desde el perfil del usuario.** La cadena completa en un solo evento compuesto: proceso hijo del navegador o del gestor de archivos, imagen situada bajo `C:\Users\`, archivo de origen con extensión `.7z` y marca de zona de Internet. Fidelidad: media-alta; es un patrón de *malware* genérico y por eso mismo rentable más allá de este actor. Falsos positivos: herramientas portables legítimas descargadas por usuarios con privilegio local, que es a su vez un hallazgo de política.

**H-7 — Un puesto de usuario está actuando como proxy `SOCKS5`.** El build extendido lleva un proxy en banda, lo que significa tráfico entrando al puesto desde el C2 y saliendo hacia destinos internos o externos, con el puesto como pivote. Buscar en NetFlow puestos con conexiones de larga duración hacia una dirección externa **y** un abanico de destinos internos atípico para su perfil; en particular, un puesto de contabilidad conectando con rangos de servidores que nunca usa. Fidelidad: media. Es la hipótesis que más depende de tener línea base por rol, y la que detecta movimiento lateral antes de que haya credenciales nuevas en juego.

**H-8 — Hay una segunda sesión de Chrome ejecutándose con un perfil clonado.** Buscar procesos `chrome.exe` con `--user-data-dir` apuntando a una ruta que no sea el perfil estándar del usuario, especialmente bajo `%AppData%`, `%LocalAppData%\Temp` o un directorio de nombre aleatorio; y procesos de navegador sin ventana visible asociada. Complementariamente, del lado de las aplicaciones: uso concurrente de la misma *cookie* de sesión desde el mismo origen aparente. Fidelidad: alta en el puesto, y es la única vía de detectar `T1185` antes del daño. Falsos positivos: automatización legítima de pruebas, perfiles de navegador múltiples creados por el usuario.

**H-9 — Hubo resolución DNS hacia alguno de los siete dominios de entrega.** Retrohunt simple, 12 meses, con el listado del Anexo A.3. Y la variante que sobrevive a la rotación: buscar resoluciones hacia dominios de registro reciente —menos de 90 días— cuyo nombre combine un término documental o contable en español con los TLD `.cloud`, `.digital`, `.online`, `.icu` o `.me`. Fidelidad: alta para los literales, media para el patrón. Falsos positivos del patrón: proveedores legítimos de gestión documental de la región, que se enumeran una vez y se listan.

**H-10 — Tenemos tráfico, cualquier tráfico, hacia los prefijos de Aeza Group.** Caza de alcance regional y de valor doble. Las direcciones del Anexo A.3 se agrupan en unos pocos prefijos —entre ellos `193.233.244.0/22`, `77.110.104.0/22` y `82.117.87.0/24`, anunciados por los sistemas autónomos `AS216246` y `AS210644`—. La pregunta no es sólo si hay tráfico hacia las 24 direcciones publicadas, sino **si hay tráfico hacia esas redes en general**, porque un proveedor designado por la OFAC alberga a muchos más actores que éste. Verificar las asignaciones contra datos BGP o RIPE antes de actuar: las fuentes de terceros discrepan entre sí y algunos rangos aparecen bajo los dos sistemas autónomos. Fidelidad: media-alta como ejercicio de reducción de superficie. **Un acierto aquí probablemente no sea Dark Caracal, y de todos modos interesa.**

**H-11 — Un remitente externo nos escribió en español con una factura de una empresa venezolana.** Caza de alcance regional sobre los señuelos, no sobre el malware. Buscar correos entrantes con asunto o adjunto que combine términos de factura, cotización, comprobante, retención o liquidación, con remitente que suplante a una empresa de la región y sin relación comercial previa en el sistema de compras. Fidelidad: baja por sí sola —es el patrón de todo el fraude por correo de la región—, pero alta en combinación con `H-5`: **un correo así, con un adjunto SVG, es este actor o uno que le copia**.

**H-12 — Nuestro proveedor de comunicaciones o de contabilidad tercerizada tuvo un incidente que no nos contó.** No se caza en nuestros registros. Se pregunta. El sector de la única víctima confirmada es comunicaciones, y el destinatario buscado es quien procesa facturas: un proveedor de contabilidad tercerizada comprometido es, para este actor, acceso a todas sus carteras de clientes con un solo implante. Revisar qué proveedores de esa categoría tenemos en la región, y qué dice el contrato sobre notificación. Es `E-g` y `X-10`.

## T-5. Brechas de visibilidad que hay que cerrar primero

| Brecha | Por qué importa aquí |
|---|---|
| Sin registro de DNS de puesto, o sin retención de 180 días | Deja ciegas `H-2`, `H-9` y la mitad de `H-10`. Es la brecha con peor relación entre lo que cuesta cerrarla y lo que inhabilita |
| Sin inspección del cuerpo de las peticiones HTTP salientes | Sin ella, `H-2` se queda en el nombre del extremo y no puede discriminar por el método `eth_getStorageAt`. Se puede vivir con esto: el nombre del extremo ya es un discriminador fuerte |
| Sin telemetría de creación de ficheros en perfiles de usuario | Deja ciegas `H-3` y `H-4`, que son las dos hipótesis de mejor fidelidad del informe |
| Sin registro de línea de comandos completa de los procesos | Deja ciega `H-8`: el discriminador es el argumento `--user-data-dir`, no el nombre de la imagen |
| Sin línea base de tráfico por rol de puesto | Deja ciega `H-7`. Un proxy `SOCKS5` en un puesto sólo es anómalo si se sabe qué es normal en ese puesto |
| Sin registro de adjuntos de la pasarela de correo con tipo y nombre | Deja ciegas `H-5` y `H-11`, y con ellas la posibilidad de decidir la política de SVG con datos propios |
| **Sin vigilancia on-chain** | No es una brecha de telemetría: es una capacidad que no tenemos porque hasta ahora no hacía falta. Deja ciegas `H-1`, `I-1`, `I-2` e `I-3`. **Cerrarla cuesta un script y un cron**, y es la recomendación `E-b` |

---

# NIVEL TÉCNICO
### Para: Ingeniería de detección · Automatización · TIP/SIEM · Vida útil: días–semanas

## X-1. Arsenal y capacidad

| Propiedad | Valor |
|---|---|
| GoCaracal — lenguaje | **Go**, compilado para Windows. Dos perfiles derivados de una arquitectura común: ligero y extendido |
| GoCaracal — cifrado de C2 | Protocolo de paquetes **propio** protegido con **`AES-GCM`**. Funciones `readSecurePacket` y `SendSecurePacket` |
| GoCaracal ligero — despacho | **Identificadores numéricos de paquete** mapeados a un conjunto compacto de rutinas. La fuente primaria remite la referencia completa de códigos a un anexo técnico acompañante |
| GoCaracal extendido — despacho | **Cadenas de comando legibles**, con **34 manejadores** expuestos. Cadenas de versión interna **`v1.0.1` a `v1.0.6`** |
| GoCaracal extendido — idioma | **Mensajes de estado orientados al operador en español**; nombres de paquete y de función en inglés. Dato de atribución blanda: el operador es hispanohablante, el desarrollador escribe código en inglés |
| GoCaracal — respaldo de C2 | **Opcional.** Configuración con `HOST`, `PORT` y, cuando está presente, `CONTRACT`. Resolución por `eth_getStorageAt` contra extremo JSON-RPC público. Función `RPCFallback` |
| Bandook (junio de 2026) — cambios | **Identificadores de comando aleatorizados**, sustituyendo los secuenciales `@0001`–`@0136` de variantes anteriores. **Nombres de exportación de plugins ofuscados** con identificadores genéricos. **≈82 manejadores** de comando |
| Bandook — recolección | Credenciales de navegador: **Chrome, Brave y Firefox** |
| Cargador | **Delphi.** Contiene a la vez Bandook y el GoCaracal extendido. Característica recurrente del actor y uno de los pilares de la atribución |
| Entrega | Adjunto **SVG** con URL acortada en `base64` → redirector intermedio → dominio temático de documentos → archivo **7-Zip** → ejecutable |
| Capacidades de interacción remota | **WebRTC** para escritorio remoto, comportamiento de **VNC oculto**, **clonado de perfil de Chrome** a sesión oculta |
| Capacidades de red | **Proxy `SOCKS5` en banda** |
| Exfiltración | **Por el mismo canal cifrado de C2.** No se identificó canal separado |
| Antianálisis | Descubrimiento de antivirus (`main.detectAntivirus`), temporización adaptativa (`main.smartSleep`), resolución dinámica de API (`main.loadAPIs`), aleatorización de identificadores en Bandook |
| Plataformas | **Windows** en todo el expediente de 2026. Histórico: Android (`Pallas`), multiplataforma (`CrossRAT` en Java) |

## X-2. Artefactos de host persistentes entre builds

<!-- cti:cards -->

| Categoría | Artefactos | Etiqueta |
|---|---|---|
| **Fichero de perfil obligatorio** | `NTUSER.MAN`, oculto, en el perfil de usuario, asociado a un flujo de clave `Run` | `el de mejor fidelidad` |
| **Patrón de ruta de ejecución** | `C:\Users\<usuario>\AppData\Roaming\[0-9a-f]{12}\[0-9a-f]{8}.exe` — directorio de 12 hex, ejecutable de 8 hex. Observados: `d30547514515\91ed375e.exe` y `e1d58f51c58a\5c0416e4.exe` | `persistencia · ejecución` |
| **Nombres de fichero de entrega** | `TF-OFICINA004A9.exe` · `VRJDL_21812.exe` · `7676230602QQ.exe`. Apariencia de identificador de trámite administrativo | `caducan rápido` |
| **Cadenas de función de Go** | `main.cleanupShell` · `main.handleConnection` · `main.detectAntivirus` · `main.saveFile` · `main.openUrl` · `main.smartSleep` · `main.runModule` · `main.InjectShellcode` · `main.injectShellcodeWoW64` · `main.handlePipeClient` · `main.loadAPIs` · `main.AntivirusProduct` · `main.lastInputInfo` | `sobreviven a la recompilación del mismo marco` |
| **Cadenas de protocolo** | `readSecurePacket` · `SendSecurePacket` · `RPCFallback` · `insensate` | `las tres primeras son el protocolo; la cuarta es una rareza útil` |
| **Cadenas de versión** | `v1.0.1` a `v1.0.6` en el build extendido | `trazan el mantenimiento` |
| **Configuración** | Claves `HOST`, `PORT` y `CONTRACT` en la configuración del build extendido | `la tercera es el indicador de que hay respaldo` |

> **Por qué `insensate` merece una línea propia.** Entre las dieciocho cadenas
> de la regla YARA publicada, diecisiete son nombres de función o de rutina
> plausibles. Una no: `insensate`. Una palabra inglesa de uso literario, que no
> es un nombre de API ni un término técnico, incrustada en un implante en Go.
> Es el tipo de cadena que elige una persona, no un compilador, y por eso es un
> excelente ancla de búsqueda: **las cadenas arbitrarias son más estables entre
> versiones que los nombres descriptivos**, porque nadie las refactoriza. Si
> sólo se puede desplegar una búsqueda de cadena en todo el parque, que sea
> ésta, en combinación con otra del conjunto.

## X-3. Lógica de detección prioritaria

<!-- cti:detections -->

**D-1 · CRÍTICO — Resolución de C2 por buzón muerto en una cadena de bloques pública**

```
(dns.question.name IN ("cloudflare-eth.com","mainnet.infura.io",
                       "eth-mainnet.g.alchemy.com","rpc.ankr.com",
                       "eth.llamarpc.com","ethereum-rpc.publicnode.com",
                       "eth.drpc.org","1rpc.io","eth.merkle.io",
                       "rpc.flashbots.net","eth.public-rpc.com")
 OR tls.sni IN (<misma lista>)
 OR (http.request.body CONTAINS "eth_getStorageAt"))
AND source.segment NOT IN (<segmentos con desarrollo Web3 justificado>)
AND process.name NOT IN (<lista blanca nominal de herramientas de desarrollo>)
```

→ **Investigación inmediata del puesto, con aislamiento si el proceso de origen no es un navegador con sesión de usuario interactiva.** Ésta es la detección de mayor valor y mayor vida útil de todo el informe: no depende de ningún hash, dominio ni dirección, y seguirá sirviendo cuando este actor haya cambiado de marco tres veces. **No automatizar la contención** sin revisar primero el resultado de `X-4`/`H-2`: en una organización con desarrollo sobre cadenas de bloques, la lista blanca hay que construirla antes de armar la regla, o la primera alerta será un desarrollador.

**D-2 · CRÍTICO — Aparición de un fichero `NTUSER.MAN`**

```
file.name == "NTUSER.MAN"
AND file.path MATCHES "C:\\Users\\[^\\]+\\"
AND event.action IN ("creation","rename","modification")
```

→ **Aislamiento del puesto y análisis.** En un entorno sin perfiles obligatorios desplegados, el falso positivo es próximo a cero y **esta detección sí admite contención automática**. Comprobar antes, una sola vez, si existen perfiles obligatorios heredados en el dominio; si existen, enumerarlos como excepción nominal y mantener la regla armada para todo lo demás.

**D-3 · ALTO — Ejecución desde directorio de nombre hexadecimal en el perfil del usuario**

```
process.executable MATCHES
  "(?i)\\\\Users\\\\[^\\\\]+\\\\AppData\\\\Roaming\\\\[0-9a-f]{12}\\\\[0-9a-f]{8}\\.exe"
```

→ **Alerta de severidad alta y recogida del binario.** Sobrevive a la recompilación porque el patrón lo genera el instalador, no el compilador. Recordar la nota de `H-4`: hay que casar la ruta **expandida**, no la cadena literal `%AppData%`.

**D-4 · ALTO — Cadena completa de entrega: SVG, archivo comprimido y ejecución**

```
(email.attachment.extension == "svg"
 AND email.attachment.content MATCHES "(?i)(<script|foreignObject|on(load|click)=|base64,)")
OR
(process.parent.name IN ("7zFM.exe","7zG.exe","explorer.exe","chrome.exe","msedge.exe")
 AND process.executable MATCHES "(?i)\\\\Users\\\\[^\\\\]+\\\\(AppData|Downloads)\\\\"
 AND file.origin.zone == "Internet"
 AND file.source.extension == "7z")
```

→ **Bloqueo en pasarela para la primera rama; alerta y recogida para la segunda.** La primera rama es prevención y debe actuar antes de la entrega; la segunda es detección y llega tarde pero a tiempo. Un SVG con `<script>` o `foreignObject` en correo entrante no tiene uso legítimo defendible en una organización que no sea un estudio de diseño.

**D-5 · ALTO — Segunda sesión de navegador con perfil desviado**

```
process.name IN ("chrome.exe","brave.exe","msedge.exe")
AND process.command_line CONTAINS "--user-data-dir"
AND NOT process.command_line MATCHES
      "(?i)--user-data-dir=.{0,4}C:\\\\Users\\\\[^\\\\]+\\\\AppData\\\\Local\\\\(Google|BraveSoftware|Microsoft)\\\\"
```

→ **Alerta alta e investigación de sesión.** Es la única detección de puesto que ataca `T1185` antes del daño. Complementar en el lado de las aplicaciones con detección de uso concurrente de la misma *cookie* de sesión, que es donde el procedimiento se ve de verdad.

**D-6 · MEDIO — Perfilado de productos de seguridad seguido de descarga**

```
EID 4688 OR EDR process_create
WHERE (
  (process.command_line CONTAINS_ANY ("SELECT * FROM AntiVirusProduct",
                                      "root\\SecurityCenter2"))
  OR wmi.namespace == "root\\SecurityCenter2"
)
AND NOT process.name IN (<herramientas de inventario y de EDR propias>)
FOLLOWED BY (SAME host WITHIN 10m) network.direction == "outbound"
            AND network.bytes_received > 100000
```

→ **Alerta media y correlación.** El build ligero consulta productos de seguridad en su perfilado inicial. Por sí sola la consulta la hacen muchos instaladores legítimos; la secuencia *consulta de antivirus → descarga de cien kilobytes o más desde una dirección sin reputación* es estrecha.

**D-7 · MEDIO — Puesto de usuario operando como proxy**

```
network.flow WHERE source.ip IN <rango_puestos>
AND flow.duration > 3600
AND destination.ip NOT IN <destinos_habituales_del_rol>
AND flow.bytes_in > 0 AND flow.bytes_out > 0
GROUP BY source.ip
HAVING count(distinct destination.ip) > <umbral_del_rol>
   AND count(distinct external.ip WITH duration > 3600) >= 1
```

→ **Alerta media; investigación del puesto, no del destino.** Requiere línea base por rol; sin ella, la regla genera ruido. Es la brecha de `T-5` que hay que cerrar para que esta detección valga algo.

**D-8 · MEDIO — Tráfico hacia prefijos de un proveedor designado**

```
network.destination.as_number IN (216246, 210644)
OR network.destination.ip IN_SUBNET ("193.233.244.0/22","77.110.104.0/22",
                                     "82.117.87.0/24","185.96.80.0/24")
```

→ **Alerta media y escalado a `E-d`.** Verificar las asignaciones contra datos BGP o RIPE antes de armar la regla: las fuentes de terceros discrepan y varios rangos aparecen bajo los dos sistemas autónomos. **No es una detección de este actor**: es una reducción de superficie que probablemente encuentre otra cosa, y eso también sirve.

> ⚠ **Regla de operación, y aquí la secuencia es la regla.** De las ocho
> detecciones anteriores, **sólo `D-2` debe ejecutar contención automática sin
> escalado humano**: su falso positivo es próximo a cero y su hallazgo implica
> persistencia instalada. `D-1` no debe automatizarse hasta que la lista blanca
> de `H-2` esté construida. Y el bloqueo de red del Anexo A.3 **no debe
> aplicarse antes de que `H-1` esté instrumentada**: la fuente primaria
> documenta que el mecanismo de respaldo se activa tras fallos repetidos contra
> el C2 principal, de modo que bloquear sin vigilar la cadena es provocar
> exactamente el evento que no podremos observar. **Leer, instrumentar,
> bloquear. En ese orden.**

## X-4. Consultas de caza

```kql
// H-1 y H-2 · Extremos JSON-RPC públicos de Ethereum desde puestos de usuario.
// La consulta central de este informe. Vida util larga: no contiene ningun IOC.
let rpc = dynamic(["cloudflare-eth.com","mainnet.infura.io","eth-mainnet.g.alchemy.com",
                   "rpc.ankr.com","eth.llamarpc.com","ethereum-rpc.publicnode.com",
                   "eth.drpc.org","1rpc.io","eth.merkle.io","rpc.flashbots.net",
                   "eth.public-rpc.com"]);
DeviceNetworkEvents
| where Timestamp > ago(180d)
| where RemoteUrl has_any (rpc) or tostring(AdditionalFields.sni) has_any (rpc)
| summarize Intentos = count(), Primero = min(Timestamp), Ultimo = max(Timestamp),
            Procesos = make_set(InitiatingProcessFileName, 10),
            Destinos = make_set(RemoteUrl, 10)
         by DeviceName, InitiatingProcessAccountName
| order by Intentos desc
```

```kql
// H-3 · Cualquier NTUSER.MAN en el parque. En un entorno sin perfiles
// obligatorios el resultado esperado es una tabla vacia.
DeviceFileEvents
| where Timestamp > ago(365d)
| where FileName =~ "NTUSER.MAN"
| where FolderPath startswith @"C:\Users\"
| project Timestamp, DeviceName, FolderPath, ActionType,
          InitiatingProcessFileName, InitiatingProcessCommandLine,
          InitiatingProcessAccountName
| order by Timestamp desc
```

```kql
// H-4 · Patron de ruta hexadecimal en el perfil del usuario.
// Nota: se casa la ruta EXPANDIDA, no la cadena literal %AppData%.
DeviceProcessEvents
| where Timestamp > ago(180d)
| where FolderPath matches regex @"(?i)\\Users\\[^\\]+\\AppData\\Roaming\\[0-9a-f]{12}\\[0-9a-f]{8}\.exe"
| project Timestamp, DeviceName, AccountName, FolderPath, ProcessCommandLine,
          InitiatingProcessFileName, SHA256
| order by Timestamp desc
```

```kql
// H-8 · Segunda sesion de navegador con perfil desviado (T1185).
DeviceProcessEvents
| where Timestamp > ago(90d)
| where FileName in~ ("chrome.exe","brave.exe","msedge.exe")
| where ProcessCommandLine contains "--user-data-dir"
| where not(ProcessCommandLine matches regex
      @"(?i)--user-data-dir=.{0,4}C:\\Users\\[^\\]+\\AppData\\Local\\(Google|BraveSoftware|Microsoft)\\")
| project Timestamp, DeviceName, AccountName, ProcessCommandLine,
          InitiatingProcessFileName, InitiatingProcessCommandLine
| order by Timestamp desc
```

```kql
// H-6 · Binario ejecutado tras extraccion de un archivo descargado.
DeviceProcessEvents
| where Timestamp > ago(180d)
| where InitiatingProcessFileName in~ ("7zFM.exe","7zG.exe","7z.exe","explorer.exe",
                                       "chrome.exe","msedge.exe","firefox.exe")
| where FolderPath matches regex @"(?i)\\Users\\[^\\]+\\(AppData|Downloads|Desktop)\\"
| where FileName endswith ".exe"
| join kind=leftouter (
    DeviceFileEvents
    | where Timestamp > ago(180d)
    | where FileName endswith ".7z" or FileName endswith ".zip"
    | project ArchiveTime = Timestamp, DeviceName, Archive = FileName
  ) on DeviceName
| where ArchiveTime between (Timestamp - 10m .. Timestamp)
| project Timestamp, DeviceName, AccountName, FolderPath, Archive, SHA256
```

```bash
#!/bin/sh
# H-1 · Lectura del valor de respaldo almacenado en los contratos BulletproofC2.
# Esto NO consulta nuestros registros: consulta la infraestructura del adversario.
# Cuesta cero, se puede poner en un cron diario, y devuelve la direccion de C2
# que los implantes usaran si pierden la principal, ANTES de que la usen.
#
# AVISO OBLIGATORIO: la direccion que devuelva NO SE BLOQUEA sin corroborar.
# Vease el supuesto clave de O-6: un valor senuelo deliberado es posible.
# Uso previsto: retrohunt en NetFlow y proxy, y registro del cambio con fecha.

RPC="https://cloudflare-eth.com"
CONTRATOS="0x03D605f13A74Bfb6149078122FcF62BD6d8799d8
0x04aB453494381E60171BE04Ea6BE6E7C44EafAfd
0xD7635f31620772882a6712472a6278c53247Bc44
0xf165F26300BF65DFaC78BC9557326bDbB3C6d33C"

for C in $CONTRATOS; do
  for RANURA in 0x0 0x1 0x2; do
    VAL=$(curl -s --max-time 15 -X POST "$RPC" \
      -H 'Content-Type: application/json' \
      --data "{\"jsonrpc\":\"2.0\",\"id\":1,\"method\":\"eth_getStorageAt\",\"params\":[\"$C\",\"$RANURA\",\"latest\"]}")
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) $C ranura=$RANURA $VAL"
  done
done

# Las ranuras 0x0 a 0x2 cubren las primeras variables de estado del contrato.
# La fuente primaria no publica el indice de la ranura que guarda el valor de C2,
# de modo que se leen las primeras y se compara con la ejecucion anterior:
# lo que interesa es EL CAMBIO, no el valor absoluto.
# Un cambio respecto al dia anterior es el indicador I-1 y dispara revision.
```

```yaml
# Sigma — Consulta de almacenamiento de contrato de Ethereum desde un puesto
title: Resolucion de C2 por buzon muerto en cadena de bloques publica
id: 8f3c1e52-7b9a-4d61-9c2e-1a4f6d80b3e7
status: experimental
description: >
  Detecta la resolucion o el acceso a extremos JSON-RPC publicos de Ethereum
  desde segmentos sin desarrollo Web3 justificado. Procedimiento documentado en
  GoCaracal (Dark Caracal, 2026) como mecanismo de respaldo de C2, y aplicable a
  cualquier actor que adopte la misma tecnica.
author: Celula CTI
date: 2026-11-17
references:
  - https://arcticwolf.com/resources/blog/dark-caracal-reloaded-new-malware-same-hunting-grounds/
tags:
  - attack.command_and_control
  - attack.t1102.001
  - attack.t1568
logsource:
  category: dns_query
detection:
  seleccion:
    QueryName:
      - 'cloudflare-eth.com'
      - 'mainnet.infura.io'
      - 'eth-mainnet.g.alchemy.com'
      - 'rpc.ankr.com'
      - 'eth.llamarpc.com'
      - 'ethereum-rpc.publicnode.com'
      - 'eth.drpc.org'
      - '1rpc.io'
      - 'eth.merkle.io'
      - 'rpc.flashbots.net'
      - 'eth.public-rpc.com'
  filtro_desarrollo:
    Image|contains:
      - '\node.exe'
      - '\python.exe'
      - '\go.exe'
      - '\cast.exe'
      - '\hardhat'
  condition: seleccion and not filtro_desarrollo
falsepositives:
  - Extensiones de monedero de navegador (MetaMask y similares): son por si
    mismas un hallazgo de politica, no un falso positivo inocuo
  - Desarrollo legitimo sobre cadenas de bloques: enumerar los puestos y
    excluirlos nominalmente, no por proceso
  - Herramientas de analitica financiera y algun instalador que consulta precios
level: high
```

```yaml
# Sigma — Creacion de un fichero de perfil obligatorio NTUSER.MAN
title: Creacion de NTUSER.MAN en un perfil de usuario
id: 2d7a94b1-c4e8-4f03-8b56-9e1d2c7a04f5
status: stable
description: >
  NTUSER.MAN convierte el perfil de usuario en obligatorio y de solo lectura, y
  Windows lo prefiere sobre NTUSER.DAT. En un entorno que no despliega perfiles
  obligatorios no deberia existir ninguno. GoCaracal extendido crea uno oculto
  asociado a un flujo de clave Run.
author: Celula CTI
date: 2026-11-17
references:
  - https://arcticwolf.com/resources/blog/dark-caracal-reloaded-new-malware-same-hunting-grounds/
tags:
  - attack.persistence
  - attack.t1547.001
  - attack.defense_evasion
  - attack.t1564.001
logsource:
  category: file_event
  product: windows
detection:
  seleccion:
    TargetFilename|endswith: '\NTUSER.MAN'
    TargetFilename|startswith: 'C:\Users\'
  condition: seleccion
falsepositives:
  - Entornos con perfiles obligatorios heredados: enumerarlos una vez y
    listarlos como excepcion nominal
level: critical
```

```yaml
# Sigma — Cadenas del marco GoCaracal en un binario en ejecucion
title: Cadenas caracteristicas del marco GoCaracal
id: 5b1e7c08-3a46-4d92-bf17-6c8309ea25d4
status: experimental
description: >
  Complemento de la regla YARA publicada por Arctic Wolf, para motores que
  evaluan cadenas en memoria o en el binario en el momento de la ejecucion.
  Vida util corta por diseno: las cadenas de funcion de Go cambian cuando el
  desarrollador refactoriza. La cadena 'insensate' es la mas estable porque es
  arbitraria y nadie la refactoriza.
author: Celula CTI
date: 2026-11-17
tags:
  - attack.execution
  - attack.t1106
  - attack.defense_evasion
logsource:
  category: process_creation
  product: windows
detection:
  cadenas:
    - 'main.detectAntivirus'
    - 'main.injectShellcodeWoW64'
    - 'readSecurePacket'
    - 'SendSecurePacket'
    - 'RPCFallback'
    - 'insensate'
  condition: cadenas
falsepositives:
  - Minimos. Son cadenas internas de un marco concreto
level: high
```

## X-5. Mitigaciones de configuración con efecto directo

| Control | Corta |
|---|---|
| **Bloqueo o cuarentena de adjuntos `.svg` en la pasarela de correo**, o reescritura a imagen rasterizada | **La etapa 01 completa.** Es la mitigación de mayor efecto y la única que actúa antes de que el usuario decida. Decidirla con los datos de `H-5`, no a ciegas |
| Expansión de acortadores de URL en correo entrante, con evaluación del destino **final** tras los redirectores | La etapa 01 en su segundo tramo. Un acortador sin expandir hace invisible el dominio de entrega a cualquier reputación |
| **Control de ejecución (WDAC o AppLocker) que impida ejecutar binarios desde `%AppData%` y `%LocalAppData%\Temp`** | **La etapa 02 completa, y también la 03.** Las dos rutas publicadas están ahí, y no hay motivo legítimo para que un ejecutable nuevo corra desde el árbol de datos móviles del usuario en un parque gestionado |
| Bloqueo de la ejecución de binarios extraídos de archivos con marca de zona de Internet | La segunda mitad de `H-6`. Rompe la cadena *archivo comprimido → ejecutable* sin saber nada de este actor |
| **Bloqueo por egreso de extremos JSON-RPC públicos de cadenas de bloques**, por lista de denegación en el proxy, para todos los segmentos sin justificación de desarrollo | **El mecanismo de respaldo.** No se puede retirar el contrato, pero sí impedir que nuestro puesto lo consulte. Es la contramedida que corresponde a `KJ-2`: si el buzón es inalcanzable, es irrelevante que sea indestructible |
| Prohibición de extensiones de monedero de criptoactivos en navegadores corporativos | Elimina de golpe el principal falso positivo de `D-1` y cierra un riesgo propio |
| Bloqueo de los prefijos de `AS216246` y `AS210644`, previa verificación BGP y decisión `E-d` | La capa de C2 de GoCaracal, por mayoría. Y de paso, los demás inquilinos de un proveedor designado |
| **Vinculación de sesión al dispositivo y detección de uso concurrente de *cookie* en las aplicaciones sensibles** | **`T1185`**, el clonado de perfil de Chrome. Es el único control de esta tabla que no está en el puesto, y el único que ataca un procedimiento que no genera eventos de autenticación |
| Acortamiento de la vida de sesión en aplicaciones con datos financieros | Reduce la ventana de utilidad de las *cookies* robadas por Bandook y por el build extendido |
| Perfiles obligatorios documentados y enumerados | No es una mitigación: es la condición para que `D-2` pueda armarse con contención automática |

---

## 14. Brechas de inteligencia y nuevos requisitos de colección

| # | Brecha | Impacto en el juicio | Requisito propuesto | Prioridad |
|---|---|---|---|---|
| G-1 | **Ninguna intrusión confirmada fuera de Venezuela.** Y en particular, ninguna evidencia de 2026 de objetivos gubernamentales regionales | `KJ-4` queda en confianza baja y `KJ-5` en posibilidad real. Toda la priorización regional es inferencia desde infraestructura | Solicitar a los CSIRT nacionales de Chile, Colombia, Perú y Ecuador si tienen notificaciones compatibles con esta cadena. Vigilar publicaciones de proveedores regionales | **Crítica** |
| G-2 | **El anexo de indicadores de la fuente primaria se declara parcial** (*referential*; la lista completa está con sus clientes) | El Anexo A es una muestra, no el conjunto. Un retrohunt negativo **no** es prueba de ausencia | Valorar acceso a la fuente completa. Mientras no exista, declarar explícitamente el alcance limitado en todo informe de caza negativo | Alta |
| G-3 | **No se puede decidir entre actor estatal y suministrador** (`H2` de `O-6`) | Cambia la naturaleza de la amenaza: un servicio opera contra objetivos de su interés nacional; un suministrador, contra los de quien pague. La predicción de selección futura depende de esto | Vigilar solapamientos de infraestructura de este actor con campañas cuyo beneficiario nacional sea distinto, como ocurrió con Operation Manul | Media |
| G-4 | **Sin tiempos de permanencia publicados** | `T-1` no lleva franja de permanencia y no se puede calibrar la ventana de retrohunt con fundamento. Se eligió 180 días por convención, no por dato | Pedir el dato a la fuente primaria si publica anexo técnico ampliado; mientras, usar la ventana por convención y decirlo | Media |
| G-5 | **No se publica el índice de la ranura de almacenamiento** que guarda el valor de C2 en el contrato | El guion de `H-1` tiene que leer varias ranuras y comparar cambios, en lugar de leer la correcta. Funciona, pero es menos limpio | Resolver por análisis propio del *bytecode* del contrato, que es público; o pedirlo a la fuente | Baja |
| G-6 | **No hay telemetría propia.** `O-4` sin evaluar | La única pregunta que importa —si estamos dentro— no tiene respuesta en este documento | Ejecutar `H-3` y `H-4`, que son las dos comprobaciones que convierten `O-4` en hallazgo en una tarde | **Crítica** |
| G-7 | **No se sabe si el actor sabe que leemos el contrato** | El supuesto clave de `O-6`. Si empieza a escribir valores señuelo, `H-1` se degrada de colección a ruido | Registrar con fecha cada valor leído y correlacionarlo después con infraestructura confirmada por terceros. La divergencia sería la señal | Media |

---

# ANEXOS

## Anexo A — Indicadores de compromiso

> ⚠ **Leer antes de usar. Cuatro advertencias, y dos son específicas de este
> informe.**
>
> **Primera, de alcance, y la hace la propia fuente.** El anexo de Arctic Wolf
> declara literalmente que sus indicadores son *referential* y que **la lista
> completa se entregó a sus clientes**. Lo que sigue es, por tanto, una muestra
> representativa. **Un retrohunt negativo contra esta lista no es prueba de
> ausencia**, y así debe constar en cualquier informe de caza que la use. Es la
> brecha `G-2`.
>
> **Segunda, de secuencia, y es la que de verdad importa aquí.** El Anexo A.3
> **no debe aplicarse como bloqueo antes de que la vigilancia del Anexo A.2
> esté instrumentada**. La fuente primaria documenta que el mecanismo de
> respaldo se activa tras fallos repetidos contra el C2 principal: bloquear sin
> vigilar la cadena es provocar precisamente el evento que no podremos
> observar. **Leer, instrumentar, bloquear.**
>
> **Tercera, de naturaleza, sobre el Anexo A.2.** Los indicadores on-chain
> **no son bloqueables y no deben tratarse como IOC convencionales**. No son
> infraestructura a la que nuestro tráfico vaya: son objetos públicos a
> consultar. Su acción permitida es *vigilancia*, y la dirección IP que
> devuelvan **no se bloquea sin corroborar**, por el supuesto clave de `O-6`.
>
> **Cuarta, de higiene, sobre el Anexo A.5.** Contiene servicios legítimos de
> terceros. Están declarados con tipo `servicio` precisamente para que **no
> entren en los agregados planos** `ioc_ipv4.txt` ni `ioc_url.txt` de este
> repositorio: cargar un extremo JSON-RPC público en una lista de bloqueo sin
> el contexto de `X-5` es exactamente el error que la portada advierte.

### A.1 — Ficheros

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| sha256 | `1e499c815146124c4a6d2b48c99068b980ad74e1a2cfd16013f8d75a9425a0ca` | **GoCaracal, variante ligera.** Publicado como `TF-OFICINA004A9.exe`. Primera de las dos muestras del mismo nombre | Alta | Vida útil de la muestra; binario en Go recompilable | **Solo retrohunt** |
| sha256 | `77f7ad29f4a8037ee5f38d3d87fb91cfd97cb8f7fa7883edf3fce506df5200c0` | **GoCaracal, variante ligera.** Segunda muestra publicada como `TF-OFICINA004A9.exe` | Alta | Vida útil de la muestra | **Solo retrohunt** |
| sha256 | `8c03d072df2e1bf14b0c00a8ab99834138c8b69f301849bf09cb44394e916015` | **GoCaracal, variante extendida.** `VRJDL_21812.exe`. Es el perfil que lleva los 34 manejadores y el respaldo on-chain | Alta | Vida útil de la muestra | **Solo retrohunt** |
| sha256 | `0a6da70548f14834acb8960689a589b48ff422f8385ae445a281aab77045fe22` | **Cargador en Delphi.** `7676230602QQ.exe`. Contiene a la vez Bandook y el GoCaracal extendido | Alta | Vida útil de la muestra | **Solo retrohunt** |
| sha256 | `a2cdf2fe741de4b13ad2298b387a6c32da4a94da180ae75bf8547386aee7376b` | **La carga (*payload*) de Bandook, descifrada.** No se observa en disco en esa forma: sirve para análisis y para correlación con repositorios de muestras, no para detección en el endpoint | Alta | Sin caducidad como referencia de análisis | **Solo retrohunt y análisis** |
| sha256 | `c9da1b08a39491dfdbede6ff4c1a2d383f57cb29e2d3532aee08d6e0a5c1dda6` | **Muestra de referencia de la regla YARA oficial.** Valor tomado del campo `hash` de la regla publicada. **Advertencia de transcripción: esta cadena circula en cobertura secundaria truncada a 63 caracteres; la de aquí tiene los 64 y es la correcta** | Alta | Sin caducidad como referencia | **Solo retrohunt** |
| filename | `TF-OFICINA004A9.exe` | Nombre del implante ligero entregado en el archivo 7-Zip. Apariencia de identificador de trámite administrativo | Alta | Caduca con la campaña | Caza (`H-6`) |
| filename | `VRJDL_21812.exe` | Nombre del build extendido | Alta | Caduca con la campaña | Caza |
| filename | `7676230602QQ.exe` | Nombre del cargador en Delphi | Alta | Caduca con la campaña | Caza |
| filename | `NTUSER.MAN` | **No es un nombre de fichero de malware: es un nombre legítimo de Windows usado como persistencia.** Fichero de *hive* de perfil obligatorio, creado oculto y asociado a un flujo de clave `Run`. **En un entorno sin perfiles obligatorios, su existencia es el hallazgo** | Alta | **Sin caducidad** | **Detección** (`D-2`) |

### A.2 — Indicadores on-chain · **vigilancia, no bloqueo**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| contrato | `0x03D605f13A74Bfb6149078122FcF62BD6d8799d8` | **Contrato `BulletproofC2` configurado como respaldo**, desplegado el 20 de mayo de 2026. Guarda un único valor mutable de C2, actualizable sólo por el monedero propietario. **Es el objeto a consultar a diario** (`H-1`, `I-1`) | Alta | **Sin caducidad: un contrato desplegado no se puede retirar** | **Vigilancia diaria. NO bloqueable** |
| contrato | `0x04aB453494381E60171BE04Ea6BE6E7C44EafAfd` | Despliegue idéntico de `BulletproofC2` desde la misma cartera. Primero en la red de pruebas Sepolia, después en la red principal | Alta | Sin caducidad | **Vigilancia diaria. NO bloqueable** |
| contrato | `0xD7635f31620772882a6712472a6278c53247Bc44` | Idem | Alta | Sin caducidad | **Vigilancia diaria. NO bloqueable** |
| contrato | `0xf165F26300BF65DFaC78BC9557326bDbB3C6d33C` | Idem | Alta | Sin caducidad | **Vigilancia diaria. NO bloqueable** |
| cartera | `0x7D321FE277f8c25aaC14aF1BA3Fc34953242052F` | **Monedero de despliegue y gestión de los contratos de respaldo.** Según la fuente, financiado a través de infraestructura asociada a Binance. **Su valor no es defensivo sino de alerta temprana: un despliegue nuevo desde esta cartera precede a una infraestructura nueva** (`I-2`), y su actividad en Sepolia precede a la red principal (`I-3`). La relación con una entidad regulada es además una vía que no es técnica: es de `E-d` y de Legal | Alta | **Sin caducidad** | **Vigilancia. NO bloqueable** |
| pattern | `eth_getStorageAt` | **Método JSON-RPC usado para leer el valor del contrato.** El discriminador fino de `D-1` donde haya inspección del cuerpo de la petición. No es un indicador del actor: es el indicador de la **técnica** | Alta | **Sin caducidad** | **Detección** (`D-1`) |
| artefacto | `CONTRACT` | **Clave de configuración del build extendido**, junto a `HOST` y `PORT`. Su presencia en una muestra indica que ese *build* lleva respaldo on-chain, y su valor da el contrato a vigilar | Alta | Sin caducidad | Análisis de muestras |
| artefacto | `BulletproofC2` | Nombre del contrato en Solidity. Útil para buscar despliegues análogos de otros actores que reutilicen el código (`I-7`, `H7`) | Alta | **Sin caducidad** | Caza en registros públicos de contratos |

### A.3 — Red · **aplicar después de A.2, no antes**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| domain | `getpdfdigital[.]cloud` | **Sitio de entrega** del archivo 7-Zip con el implante ligero. El eslabón confirmado de la cadena de junio de 2026 | Alta | 2027-02-17, revisable | **Bloqueo** |
| domain | `getpdf[.]digital` | Infraestructura de entrega del mismo clúster | Alta | 2027-02-17 | **Bloqueo** |
| domain | `visualizarpdf[.]online` | Infraestructura de entrega | Alta | 2027-02-17 | **Bloqueo** |
| domain | `contabilidad[.]icu` | Infraestructura de entrega. **El nombre dice a quién va dirigido** | Alta | 2027-02-17 | **Bloqueo** |
| domain | `soportedigital[.]cloud` | Infraestructura de entrega | Alta | 2027-02-17 | **Bloqueo** |
| domain | `documentodigital[.]cloud` | Infraestructura de entrega | Alta | 2027-02-17 | **Bloqueo** |
| domain | `gestionadocs[.]me` | **Entrega y además panel de C2.** El único de los siete con doble función | Alta | 2027-02-17 | **Bloqueo** |
| ipv4 | `109.120.187.217` | C2 de GoCaracal. Red de Aeza Group | Alta | 2027-02-17 | **Bloqueo** (tras `E-a`) |
| ipv4 | `109.172.95.121` | C2 de GoCaracal. Aeza | Alta | 2027-02-17 | **Bloqueo** (tras `E-a`) |
| ipv4 | `138.124.112.213` | C2 de GoCaracal. Aeza | Alta | 2027-02-17 | **Bloqueo** (tras `E-a`) |
| ipv4 | `138.124.14.130` | C2 de GoCaracal. Aeza | Alta | 2027-02-17 | **Bloqueo** (tras `E-a`) |
| ipv4 | `176.124.220.153` | C2 de GoCaracal. Aeza | Alta | 2027-02-17 | **Bloqueo** (tras `E-a`) |
| ipv4 | `185.125.101.181` | C2 de GoCaracal. Aeza | Alta | 2027-02-17 | **Bloqueo** (tras `E-a`) |
| ipv4 | `185.96.80.110` | C2 de GoCaracal. Aeza | Alta | 2027-02-17 | **Bloqueo** (tras `E-a`) |
| ipv4 | `185.96.80.54` | C2 de GoCaracal. Aeza. **Mismo /24 que la anterior** | Alta | 2027-02-17 | **Bloqueo** (tras `E-a`) |
| ipv4 | `193.233.245.52` | C2 de GoCaracal. Aeza | Alta | 2027-02-17 | **Bloqueo** (tras `E-a`) |
| ipv4 | `193.233.245.45` | C2 de GoCaracal. Aeza. **Mismo /24** | Alta | 2027-02-17 | **Bloqueo** (tras `E-a`) |
| ipv4 | `193.233.245.0` | C2 de GoCaracal. Aeza. **Mismo /24, y es la dirección de red del bloque: tres direcciones del mismo /24 justifican bloquear el prefijo y no las direcciones** | Alta | 2027-02-17 | **Bloqueo del prefijo** (`D-8`) |
| ipv4 | `62.60.237.22` | C2 de GoCaracal. Aeza | Alta | 2027-02-17 | **Bloqueo** (tras `E-a`) |
| ipv4 | `77.110.104.98` | C2 de GoCaracal. Aeza | Alta | 2027-02-17 | **Bloqueo** (tras `E-a`) |
| ipv4 | `77.110.105.244` | C2 de GoCaracal. Aeza | Alta | 2027-02-17 | **Bloqueo** (tras `E-a`) |
| ipv4 | `77.110.105.56` | C2 de GoCaracal. Aeza | Alta | 2027-02-17 | **Bloqueo** (tras `E-a`) |
| ipv4 | `77.110.105.59` | C2 de GoCaracal. Aeza | Alta | 2027-02-17 | **Bloqueo** (tras `E-a`) |
| ipv4 | `77.110.98.66` | C2 de GoCaracal. Aeza | Alta | 2027-02-17 | **Bloqueo** (tras `E-a`) |
| ipv4 | `80.71.224.30` | C2 de GoCaracal. Aeza | Alta | 2027-02-17 | **Bloqueo** (tras `E-a`) |
| ipv4 | `82.117.87.138` | C2 de GoCaracal. Aeza. **Aparece dos veces en la lista publicada** | Alta | 2027-02-17 | **Bloqueo** (tras `E-a`) |
| ipv4 | `82.117.87.192` | C2 de GoCaracal. Aeza. Mismo /24 que la anterior | Alta | 2027-02-17 | **Bloqueo** (tras `E-a`) |
| ipv4 | `85.192.30.211` | C2 de GoCaracal. Aeza | Alta | 2027-02-17 | **Bloqueo** (tras `E-a`) |
| ipv4 | `79.137.192.38` | C2 de GoCaracal. Aeza. **Aparece dos veces en la lista publicada** | Alta | 2027-02-17 | **Bloqueo** (tras `E-a`) |
| ipv4 | `46.226.162.68` | C2 de GoCaracal. Aeza | Alta | 2027-02-17 | **Bloqueo** (tras `E-a`) |
| ipv4 | `45.152.198.108` | C2 de GoCaracal. **La fuente dice que 23 de las 24 direcciones están en redes de Aeza Group y NO dice cuál es la excepción.** Las etiquetas «Aeza» de las filas anteriores son, por tanto, inferencia nuestra a partir del agrupamiento en prefijos, no un dato publicado dirección por dirección | Alta | 2027-02-17 | **Bloqueo** (tras `E-a`) |
| ipv4 | `91.208.197.80` | **C2 de Bandook.** Red de AlexHost, proveedor previamente asociado al actor. Capa de infraestructura **distinta** de la de GoCaracal: una retirada que acierte con una no toca la otra | Alta | 2027-02-17 | **Bloqueo** |
| ipv4 | `91.208.184.45` | C2 de Bandook. AlexHost | Alta | 2027-02-17 | **Bloqueo** |
| ipv4 | `91.208.206.88` | C2 de Bandook. AlexHost | Alta | 2027-02-17 | **Bloqueo** |
| ipv4 | `91.208.184.130` | C2 de Bandook. AlexHost. **Mismo /24 que `91.208.184.45`** | Alta | 2027-02-17 | **Bloqueo** |
| ipv4 | `176.123.1.174` | C2 de Bandook. AlexHost | Alta | 2027-02-17 | **Bloqueo** |
| asn | `AS216246` | **Aeza Group LLC.** Sistema autónomo que anuncia la mayoría de los prefijos de C2 de GoCaracal, entre ellos `77.110.105.0/24` y el bloque que contiene `193.233.245.x`. Designado por la OFAC el 1 de julio de 2025 | Media — **verificar contra BGP o RIPE antes de actuar: las fuentes de terceros discrepan y algunos rangos aparecen bajo los dos sistemas autónomos** | Sin caducidad mientras se mantenga el anuncio | **Bloqueo por prefijo, decisión `E-d`** |
| asn | `AS210644` | **AEZA GROUP LLC.** Segundo sistema autónomo del mismo proveedor | Media — misma salvedad | Sin caducidad | **Bloqueo por prefijo, decisión `E-d`** |
| pattern | `193.233.244.0/22` · `77.110.104.0/22` · `82.117.87.0/24` · `185.96.80.0/24` | **Prefijos donde se agrupan las direcciones publicadas**, derivados por nosotros de la lista: **la fuente publica direcciones y la cifra agregada de 23 sobre 24, no la asignación individual.** El nivel útil de este anexo no es la dirección individual: tres direcciones del mismo /24 dicen que el actor compra bloques, no direcciones | Media — verificar asignación vigente | Sin caducidad mientras se mantenga el anuncio | **Bloqueo por prefijo** (`D-8`, `H-10`) |
| useragent | `Mozilla/5.0 (Windows NT 10.0; Win64; x64)` | **Agente de usuario del implante.** Cadena truncada: carece de la parte de motor y de navegador que lleva cualquier agente real. **Ese truncamiento es el indicador**, no la cadena completa, que de por sí es genérica | Media | 2027-02-17 | Caza con contraste |

### A.4 — Artefactos de host y patrones · **el nivel que no caduca**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| filepath | `C:\Users\<usuario>\AppData\Roaming\[0-9a-f]{12}\[0-9a-f]{8}.exe` | **Patrón de ruta de ejecución**, generalizado desde las dos rutas publicadas. **Advertencia: las fuentes lo escriben como `%AppData%\Roaming\…`, que es redundante; una detección sobre esa cadena literal nunca casa. Hay que casar la ruta expandida** | Alta | **Sin caducidad** | **Detección** (`D-3`, `H-4`) |
| filepath | `%AppData%\Roaming\d30547514515\91ed375e.exe` | Ruta literal publicada, tal cual. Se conserva por fidelidad a la fuente, **no para construir detección con ella** | Alta | Caduca con la muestra | Solo retrohunt |
| filepath | `%AppData%\Roaming\e1d58f51c58a\5c0416e4.exe` | Segunda ruta literal publicada | Alta | Caduca con la muestra | Solo retrohunt |
| pattern | `main.cleanupShell` · `main.handleConnection` · `main.detectAntivirus` · `main.saveFile` · `main.openUrl` · `main.smartSleep` · `main.runModule` · `main.InjectShellcode` · `main.injectShellcodeWoW64` · `main.handlePipeClient` · `main.loadAPIs` · `main.AntivirusProduct` · `main.lastInputInfo` | **Nombres de función de Go del build ligero**, de la regla YARA oficial. Persisten entre compilaciones del mismo marco; mueren cuando el desarrollador refactoriza | Alta | Vida útil de la versión del marco | **Detección** (regla YARA oficial) |
| pattern | `readSecurePacket` · `SendSecurePacket` · `RPCFallback` | **Cadenas del protocolo y del mecanismo de respaldo.** `RPCFallback` es la que delata la capacidad on-chain en una muestra | Alta | Vida útil de la versión | **Detección** |
| pattern | `insensate` | **Cadena arbitraria del binario.** Palabra inglesa de uso literario, sin función técnica, en un implante en Go. **Las cadenas arbitrarias son más estables entre versiones que los nombres descriptivos, porque nadie las refactoriza.** El mejor ancla de búsqueda del informe | Alta | **Previsiblemente larga** | **Detección** (`X-3`) |
| pattern | `v1.0.1` … `v1.0.6` | Cadenas de versión interna del build extendido. Trazan el mantenimiento del marco entre mayo y julio de 2026 | Alta | Se amplía con versiones nuevas | Análisis de muestras |
| artefacto | `@0001` … `@0136` | **Identificadores de comando secuenciales de variantes ANTERIORES de Bandook. Ya no sirven: la variante de junio de 2026 los sustituyó por cadenas aleatorias.** Se consignan precisamente para que una regla heredada que los use se dé de baja | Alta | **Caducado por diseño del adversario** | **Retirar las reglas que dependan de esto** |
| herramienta | `targeted_DarkCaracal_GoCaracal_Lightweight_RAT` | **Nombre de la regla YARA oficial** publicada por Arctic Wolf, marcada `TLP:CLEAR`, con identificador `6e5e3b86-5ea6-499b-b418-cacd57254978` y fecha de creación 2026-07-13. Condición: 5 de 18 cadenas. **Usar la regla mantenida, no las cadenas sueltas** | Alta | Mantenida por el autor | **Desplegar la regla oficial** |

### A.5 — Servicios legítimos abusados · **no bloquear sin leer `X-5`**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| servicio | `cloudflare-eth.com` · `mainnet.infura.io` · `eth-mainnet.g.alchemy.com` · `rpc.ankr.com` · `eth.llamarpc.com` · `ethereum-rpc.publicnode.com` · `eth.drpc.org` · `1rpc.io` | **Extremos JSON-RPC públicos de Ethereum.** Servicios legítimos de terceros, de uso masivo y enteramente lícito. **El implante no necesita ninguno en concreto: cualquiera sirve, y por eso la lista es orientativa y no exhaustiva.** El indicador no es el extremo, es **que un puesto de usuario lo consulte** | Alta como vía de abuso; la lista es orientativa | Sin caducidad | **No bloquear a ciegas.** Bloqueo por egreso **sólo** en segmentos sin desarrollo justificado, previa lista blanca (`X-5`, `D-1`) |
| servicio | `Ethereum` — red principal y red de pruebas **Sepolia** | Infraestructura pública. La actividad del actor en Sepolia precede a la red principal y constituye **alerta temprana** (`I-3`) | Alta | Sin caducidad | **Vigilancia** |
| servicio | Acortadores de URL | Eslabón intermedio de la cadena de entrega. La fuente no nombra el servicio concreto | Alta | Sin caducidad | **Expansión y evaluación del destino final** (`X-5`) |
| servicio | `7-Zip` · formato `.7z` | Contenedor del implante entregado. Herramienta legítima | Alta | Sin caducidad | **No bloquear la herramienta**; controlar la ejecución de lo extraído (`X-5`) |
| servicio | `WebRTC` | Base del escritorio remoto del build extendido. Tecnología legítima y ubicua | Alta | Sin caducidad | Detección por contexto |
| servicio | `SOCKS5` | Proxy en banda del build extendido | Alta | Sin caducidad | Detección por contexto (`D-7`) |
| servicio | Formato `SVG` en adjuntos de correo | **Vehículo de la etapa 01.** Formato legítimo y estándar, que es XML y admite contenido ejecutable embebido | Alta | **Sin caducidad** | **Bloqueo, cuarentena o rasterización en pasarela** (`X-5`) |
| servicio | `Binance` | La fuente indica que el monedero de despliegue se financió a través de infraestructura asociada a esta entidad. **No es un indicador de compromiso: es una vía de atribución que pasa por una entidad regulada, y por tanto por Legal, no por el SOC** | Media | Sin caducidad | **Ninguna acción técnica.** Insumo de `E-d` |

## Anexo B — Fuentes y valoración

> Valoración doble tipo Admiralty/OTAN: **fiabilidad de la fuente (A–F)** ×
> **credibilidad de la información (1–6)**. Se valoran por separado.

| Fuente | Disciplina | Fiabilidad | Credibilidad | Notas de sesgo |
|---|---|---|---|---|
| **Arctic Wolf Labs, «Dark Caracal Reloaded: New Malware, Same Hunting Grounds», 26-08-2026** — leída en original, incluido su anexo técnico | OSINT comercial · TECHINT de primera mano | **B** | **2** | **Fuente primaria de este informe.** Investigación de respuesta a incidentes propia más análisis de 249 muestras. Declara su confianza como media y publica un descargo explícito de que la atribución es juicio analítico y no hecho jurídico, lo que es una señal de calidad. Sesgo: interés comercial en nombrar un marco nuevo; anexo de indicadores **declaradamente parcial** |
| **HivePro, aviso TA2026250, 27-08-2026** — leído en original | OSINT comercial · derivada | **C** | **3** | Deriva íntegramente de la anterior y añade el mapeo ATT&CK que la primaria no publica, lo que la hace útil. **Introduce al menos un error de transcripción verificado**: un SHA-256 truncado a 63 caracteres. Se usa sólo para el mapeo ATT&CK y para corroborar, nunca como fuente única |
| **EFF y Lookout, «Dark Caracal: Cyber-Espionage at a Global Scale», 18-01-2018** — no leída en original en esta revisión; citada a través de cobertura secundaria y de la propia fuente primaria | OSINT · investigación conjunta | **B** | **2** | Expediente fundacional del actor. **Su prudencia es parte de su valor**: los autores declararon no poder descartar la actuación de un empleado al margen de la institución. El Líbano la negó. Las cifras de volumen exfiltrado difieren entre coberturas secundarias —una de ellas da 48 GB sólo para las campañas de Android—, de modo que este informe usa únicamente el orden de magnitud que las fuentes comparten («cientos de gigabytes») y ninguna cifra exacta |
| **Comunicado de designación de la OFAC sobre Aeza Group, 01-07-2025** | Fuente gubernamental | **A** | **1** | Documento oficial. Se usa sólo para el hecho de la designación y su fecha |
| **Cobertura secundaria sobre Poco RAT (2024-2025)** | OSINT comercial · derivada y agregada | **D** | **4** | **Fuentes en desacuerdo entre sí** sobre fecha de descubrimiento, sectores y porcentajes de vector de entrega. Se usan **únicamente** para establecer la existencia y el periodo de la familia, y para los países citados. **Ninguna cifra ni porcentaje de esta categoría se usa en los juicios clave** |
| **Datos de asignación de sistemas autónomos y prefijos de terceros** | OSINT técnico | **C** | **4** | Las fuentes consultadas **discrepan entre sí** sobre qué prefijos pertenecen a cada sistema autónomo de Aeza. Por eso la confianza del Anexo A.3 en esas filas es media y por eso la acción exige verificación previa contra BGP o RIPE |
| **Positive Technologies, «The evolution of Dark Caracal tools»** | OSINT comercial · TECHINT | **B** | **2** *(no aplicada)* | **Inaccesible.** Fallo permanente de certificado TLS en el servidor del proveedor. Es la fuente técnica primaria sobre Poco RAT y su ausencia es la limitación `3.3.5`. **No se cita ningún dato suyo que no venga confirmado por otra fuente** |

### Anexo B.1 — Una fuente consultada y deliberadamente no reproducida

Durante la colección se localizó el informe de **Kaspersky sobre la campaña de AsioGate**, publicado en febrero de 2026, accesible sin autenticación en un servidor del propio proveedor. Es la fuente primaria de la campaña que antecede inmediatamente a la que describe este informe, y contiene material técnico que habría enriquecido `T-1`, `X-1` y el Anexo A.

**No se ha utilizado, y conviene explicar por qué con precisión.** El documento lleva en su primera página una restricción de distribución explícita: declara ser un documento restringido y pide no distribuirlo fuera de la base de clientes de inteligencia APT del proveedor. Que un fichero sea alcanzable por una URL pública no modifica el marcado que su autor le puso; la accesibilidad técnica y la autorización de difusión son cosas distintas, y confundirlas es precisamente el error que esta disciplina pide no cometer.

Este repositorio publica **`TLP:CLEAR`**, es decir, material redistribuible sin restricción. Incorporar a un producto `TLP:CLEAR` el contenido de un documento marcado para una base de clientes cerrada equivaldría a desclasificarlo por cuenta propia y a trasladar a cualquier lector una restricción que no podría cumplir. La política de publicación de este repositorio está implementada en el propio constructor para los informes propios (`TLP_PUBLICABLE` en `tools/cti_build.py`); aplicarla a las fuentes es la otra mitad de la misma disciplina, y ésa no la puede automatizar ningún script.

**Consecuencia práctica, declarada para que el lector calibre:** todo lo que este informe afirma sobre la campaña de febrero de 2026 —señuelos financieros en español, adjuntos SVG, acortadores de URL, cargador en Delphi, el nombre y el lenguaje del *backdoor* AsioGate, el foco en Venezuela y la reutilización de componentes contra Chile y Brasil— procede de **la cita que de ella hace la fuente primaria de Arctic Wolf** y de cobertura secundaria pública, no del documento. Es menos de lo que podría decirse. Es todo lo que se puede decir sin romper el marcado de un tercero.

Para quien tenga acceso legítimo a esa base de clientes, el documento existe, es relevante y vale la pena leerlo: resolvería parte de la brecha `G-2`.

## Anexo C — Léxico de probabilidad y confianza

<!-- cti:bars title="Probabilidad estimativa — cuán probable es que el hecho sea cierto" -->

| Término | Techo del rango |
|---|---|
| Remoto | 5 |
| Muy poco probable | 20 |
| Poco probable | 45 |
| Posibilidad real | 55 |
| Probable | 80 |
| Muy probable | 95 |
| Casi con certeza | 99 |

| Nivel de confianza | Criterio |
|---|---|
| Alta | Múltiples fuentes de calidad, corroboradas, sin brechas relevantes |
| Moderada | Fuentes creíbles pero corroboración parcial o brechas conocidas |
| Baja | Fuente única, no corroborada, fuerte dependencia de supuestos |

> Usar siempre el término **y** el porcentaje. No usar «podría» ni «es posible»
> como juicio: son afirmaciones no falsables.

## Anexo D — Cómo se defiende uno de un canal de mando y control que no se puede retirar

Este anexo no es sobre Dark Caracal. Es el método que queda cuando la medida habitual —localizar la infraestructura, denunciarla, incautarla— deja de estar disponible, y se escribe aparte porque va a hacer falta otra vez: el contrato cuesta céntimos, el código es trivial y `H7` valora como probable que la técnica se difunda.

**Primero, calibrar qué se ha perdido exactamente.** No se ha perdido el bloqueo: se ha perdido la *retirada*. El tráfico de órdenes y de datos sigue yendo a una dirección IP convencional, bloqueable y observable. Lo que no se puede retirar es el mecanismo que entrega la dirección siguiente. Esa distinción decide todo lo demás: si se confunden, se concluye que no hay nada que hacer, y hay bastante.

**Segundo, invertir la pregunta.** Un buzón muerto en una infraestructura pública es, por definición, legible por todos. El adversario ha ganado indestructibilidad y ha pagado con transparencia, y el precio es asimétrico a nuestro favor: él necesita que el buzón esté disponible para sus implantes, y no puede restringir quién lo lee. Nosotros no tenemos ninguna necesidad equivalente. **La lectura del buzón es inteligencia anticipada**, no reactiva: entrega la infraestructura futura antes de su uso.

**Tercero, cinco preguntas antes de tocar nada**, en este orden:

1. **¿Cuál es el valor almacenado ahora?** Léase y regístrese con fecha. Es gratis y es la línea base de todo lo que venga después.
2. **¿Cuál es el historial?** Una cadena pública guarda cada cambio con su fecha. El historial dice si el mecanismo está vivo, cada cuánto se actualiza y desde cuándo. Un contrato desplegado hace seis meses y nunca actualizado dice algo muy distinto de uno escrito ayer.
3. **¿Hay huellas de desarrollo?** Los despliegues en redes de pruebas y los valores con direcciones privadas son el cuaderno de laboratorio del adversario, publicado para siempre. Ahí está la alerta temprana.
4. **¿Qué entidad financió el origen?** Una cartera se financia desde algún sitio, y si ese sitio es una entidad regulada hay una vía que no es técnica. Esa pregunta no es del SOC.
5. **¿Puedo impedir que mis equipos lean el buzón?** Casi siempre sí. No se puede destruir el buzón, pero sí cortar el camino hasta él: el implante necesita alcanzar un extremo público desde dentro de nuestra red, y ese extremo se bloquea por egreso como cualquier otro destino. **Un buzón indestructible pero inalcanzable es un buzón inútil.**

**Cuarto, el orden de las medidas, que es lo contrario del reflejo.** Leer, instrumentar la vigilancia, y sólo entonces bloquear. Bloquear primero es activar el mecanismo de respaldo en el momento exacto en que no lo estamos mirando.

**Quinto, y es la trampa.** En cuanto el adversario advierte que el buzón público se vigila, puede escribir valores falsos. El buzón sigue siendo legible, pero deja de ser fiable, y una dirección leída de ahí y bloqueada a ciegas puede ser un destino legítimo elegido para hacernos daño. Por eso, en todo este informe, la acción permitida de un valor leído del contrato es **caza y corroboración, nunca bloqueo directo**. La transparencia que el adversario nos regaló no viene con garantía de veracidad: viene con garantía de publicidad, que no es lo mismo.

> **Y la conclusión que se le pide al lector que no saque.** Que un actor haya
> puesto su respaldo en una cadena de bloques no dice nada sobre las cadenas de
> bloques, ni justifica ninguna posición sobre ellas. Lo que dice es algo más
> útil y más estrecho: **cualquier infraestructura pública, permanente y
> escribible por su propietario sirve de buzón muerto**, y ya ha servido antes
> —repositorios de código, servicios de notas, perfiles de redes sociales,
> entradas DNS TXT—. La novedad no es el abuso: es que esta vez el buzón no se
> puede cerrar. Lo que hay que saber detectar es la **clase** de tráfico, y por
> eso `D-1` está escrita contra el mecanismo y no contra el contrato.

## Anexo E — Marcos de referencia empleados

`MITRE ATT&CK v18` · `Modelo del Diamante` · `Cyber Kill Chain` · `Pirámide del Dolor` · `F3EAD` · `ICD 203` · `ACH, supuestos clave y pre-mortem` · `TLP 2.0` · `PAP` · `Admiralty Code` · `Sigma` · `YARA`

## Anexo F — Paquete legible por máquina

- Las tablas `cti:ioc` de los Anexos A.1 a A.5 alimentan `ioc_index.csv` en cada construcción, con informe de origen, confianza, caducidad, acción permitida y contexto.
- **Fuente preferente para ingesta automática:** el anexo del informe de Arctic Wolf Labs, que su autor mantiene y que declara su propio alcance parcial.
- **Regla YARA oficial:** `targeted_DarkCaracal_GoCaracal_Lightweight_RAT`, identificador `6e5e3b86-5ea6-499b-b418-cacd57254978`, versión 1.0, creada el 2026-07-13, marcada `TLP:CLEAR` por su autor y por tanto reproducible. Transcrita íntegra en `X-3` del original.
- **Reglas propias:** tres reglas Sigma en `X-4`, de autoría propia, sin repositorio externo. La de `NTUSER.MAN` y la de `eth_getStorageAt` son las que conviene desplegar primero.
- **Guion de vigilancia on-chain:** en `X-4`, sólo `curl` y `sh`. Sin dependencias y sin claves de API.

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-11-17 | Emisión inicial. Fuente primaria leída en original con su anexo técnico. Se corrigen cuatro afirmaciones del requisito de origen en `§3.5`, se consigna en el Anexo B.1 una fuente relevante deliberadamente no reproducida por su marcado de distribución, y se verifica un error de transcripción de hash que circula en cobertura secundaria | Célula CTI |

## Anexo H — Realimentación del consumidor

| Pregunta | Respuesta |
|---|---|
| ¿Respondió a su requisito? | |
| ¿Qué decisión tomó o cambió con este informe? | |
| ¿Se ejecutó `E-a` —la lectura de los contratos— antes de aplicar cualquier bloqueo? | |
| ¿Qué devolvió `H-3`, el barrido de `NTUSER.MAN`? | |
| ¿Faltó algo que esté en la fuente primaria y no aquí? | |
| ¿Llegó a tiempo? | |

> Sin este anexo devuelto, el ciclo de inteligencia queda abierto y el próximo
> producto no mejora. **Y hay una pregunta de esta tabla que vale más que las
> demás:** la de `H-3`. Es la única que convierte este documento de inteligencia
> genérica en inteligencia propia, y se responde en una tarde.
