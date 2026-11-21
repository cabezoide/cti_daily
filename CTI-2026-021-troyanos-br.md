---
tlp: "TLP:CLEAR"
pap: "PAP:AMBER"
id: "CTI-2026-021"
version: "1.0"
tipo: "Perfil de ecosistema"
foco_regional: "Chile · Latinoamérica"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "Troyanos bancarios brasileños · Mekotio · Mispadu · Grandoreiro · Astaroth · Coyote · VENON"
fecha: "2026-11-16"
caduca: "2027-02-16"
autor: "Célula CTI"
distribucion: "Elaborado íntegramente con fuentes abiertas TLP:CLEAR, incluidas cinco alertas del CSIRT Nacional de Chile. Difusión libre, conservando la atribución de las fuentes y las salvedades metodológicas de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-021
## La única amenaza de esta cartera donde Chile es objetivo primario, y la que menos atención recibe
### El CSIRT Nacional ha alertado de Mekotio al menos cinco veces desde 2023

> **Regla de oro del producto:** todo párrafo debe responder a un requisito de
> inteligencia (PIR) y habilitar una decisión. Si un párrafo no cambia lo que
> alguien va a hacer, va al anexo o se borra.

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-021` |
| Versión / fecha | `1.0` — 2026-11-16 |
| Tipo de producto | Perfil de ecosistema de malware + evaluación regional. **No es un perfil de actor:** el sujeto son seis familias con operadores distintos que comparten mercado, técnicas y proveedores |
| Niveles cubiertos | Estratégico · Operacional · Táctico · Técnico |
| Foco regional | **Chile como objetivo primario**, con el ecosistema regional como contexto |
| Marcado de difusión | `TLP:CLEAR` · `PAP:AMBER` |
| Clasificación interna | Público — apto para difusión abierta |
| Requisitos atendidos | `PIR-02` (superficie de phishing y suplantación institucional), `PIR-04` (amenazas con foco regional hispanohablante), `PIR-06` (fraude y robo de credenciales con impacto financiero), `PIR-08` (abuso de servicios y software legítimos como infraestructura) |
| Solicitante / consumidor primario | CISO · Jefatura de SOC · Seguridad del Correo · Ingeniería de Detección · Asuntos Corporativos · Prevención de Fraude |
| Ventana de observación | 2015 (primeras muestras de Mekotio) → 2026-11-16, con detalle técnico desde 2019 |
| Base de colección | 12 fuentes. **Gubernamental chilena:** cinco alertas del CSIRT Nacional (`2CMV23-00417-01`, `CMV24-00455`, `CMV24-00463`, `CMV24-00483`, `CMV25-00499`), cuatro de ellas marcadas `TLP:CLEAR` en el portal. **Proveedor de primera mano:** ESET LA (2019 y 2020), CronUp (2025), CrowdStrike (29-jul-2026), ZenoX (10-mar-2026), Palo Alto Unit 42 (2-feb-2024), Cofense (11-feb-2026), Recorded Future Insikt (LAC, ~ene-2026). **Sin telemetría propia incorporada** |
| Autor (analista) | Célula CTI |
| Revisión por pares | Pendiente |
| Aprobación | Pendiente |
| Caducidad / revisión | 2027-02-16, o antes si el CSIRT Nacional emite una alerta nueva de esta familia, si el filtro de numeración `+55` del gusano de WhatsApp se amplía a otros prefijos, o si se confirma la hipótesis de reescritura asistida por IA de `VENON` |
| Productos relacionados | `CTI-2026-014` a `CTI-2026-017` (actores de extorsión y espionaje), `CTI-2026-018` (abuso de TLD — comparte los dominios de suplantación postal chilena), `CTI-2026-019` (ARTEX — comparte el hilo de la IA en el desarrollo ofensivo), `CTI-2026-020` (Blind Eagle — **comparte la tesis central:** la fluidez institucional como ventaja competitiva, y el ecosistema brasileño como proveedor) |
| Paquete legible por máquina | Pendiente de generar (véase §14) |

<!-- cti:note type="warn" -->

> **Limitación estructural de este producto.** Hay por primera vez en esta serie
> indicadores con víctima nacional y alertas del CERT chileno, pero **sigue sin haber
> telemetría de la organización**. En consecuencia **§O-4 (nuestra exposición) está sin
> rellenar**: no sabemos cuántos de nuestros equipos ejecutan el intérprete de AutoIt desde
> rutas de usuario, cuántos permiten instalar un MSI llegado por correo, ni si alguien ha
> instalado una herramienta de administración remota sin ticket de cambio. Las tres cosas
> son el núcleo de esta amenaza y las tres se responden en una tarde.

<!-- cti:note type="good" -->

> ✅ **Lo que distingue a este informe de los seis anteriores.** Es el primero donde el
> **CSIRT Nacional de Chile** ha emitido alertas públicas nombrando la familia —al menos
> cinco desde junio de 2023—, donde las instituciones suplantadas son **chilenas y
> concretas** (Servicio de Impuestos Internos, Compañía General de Electricidad, Tesorería
> General de la República, Ministerio de Energía), y donde el Anexo A contiene indicadores
> con **contexto chileno verificable**, no inferido de victimología ajena. Donde los
> informes `CTI-2026-014` a `CTI-2026-020` tuvieron que razonar por analogía regional, aquí
> hay evidencia nacional directa.

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** Chile es objetivo primario de este ecosistema, no colateral. ESET describe a Mekotio como la familia de troyanos bancarios que más afecta a Chile, con muestras construidas específicamente contra los portales de banca electrónica de **los 24 bancos de mayor presencia en el país**, y en 2019 Chile concentró el **48 % de las detecciones mundiales** de esa familia. El CSIRT Nacional ha alertado de ella al menos cinco veces desde 2023. Valoramos **casi con certeza** *(95–99 %)*. **Confianza: alta.** *Base:* ESET LA (análisis técnico de primera mano, 2019 y 2020) corroborado por cinco alertas del CERT nacional y por una firma chilena (CronUp, 2025).

**KJ-2.** El señuelo no es el banco: es la institución chilena con la que toda empresa trata obligatoriamente. Las campañas documentadas suplantan al Servicio de Impuestos Internos —boletas electrónicas, facturas impagas—, a la Tesorería General de la República —devolución de impuestos—, a la Compañía General de Electricidad —retraso en el pago— y al Ministerio de Energía —alerta de apagón—. **El pretexto se adapta al acontecimiento nacional del momento:** la campaña del Ministerio de Energía se lanzó aprovechando el corte de luz masivo de febrero de 2025. Valoramos **muy probable** *(80–95 %)*. **Confianza: alta.** *Base:* cuatro alertas del CSIRT Nacional con la marca suplantada nombrada, más el análisis de CronUp.

**KJ-3.** El canal de propagación cambió en el último año y es donde no tenemos ningún control. Desde el cuarto trimestre de 2025, Astaroth incorpora un módulo que **clona el perfil del navegador de la víctima, levanta un navegador sin interfaz y se adhiere a su sesión de WhatsApp Web ya autenticada** para enviar el malware a sus contactos: saludo, adjunto y mensaje, tres mensajes por contacto. Hoy filtra solo números que empiezan por `+55`. **Ese filtro es una línea de código.** Valoramos **probable** *(55–80 %)* que el filtrado se amplíe a otros prefijos en los próximos doce meses. **Confianza: moderada.** *Base:* CrowdStrike (29-jul-2026), análisis de primera mano del módulo; la proyección sobre el filtro es nuestra.

**KJ-4.** La entrega se apoya en software legítimo y firmado, de modo que los controles de reputación y de firma no se activan. Las campañas usan el **intérprete oficial de AutoIt** para ejecutar el implante, instaladores **MSI**, la herramienta de administración remota **PDQ Connect** —firmada digitalmente y con cero detecciones en VirusTotal cuando se usó—, bibliotecas legítimas de automatización de WhatsApp (`WPPConnect/WA-JS`) descargadas de GitHub, controladores oficiales de Selenium y binarios firmados de NVIDIA para carga lateral de DLL. Valoramos **muy probable** *(80–95 %)*. **Confianza: alta.** *Base:* ESET, CronUp, CrowdStrike y ZenoX documentan cada caso por separado.

**KJ-5.** La detección que funciona es genérica al ecosistema, no específica de cada familia. Son seis familias con operadores distintos, pero comparten un conjunto corto de comportamientos: intérprete de script o de AutoIt ejecutándose desde ruta de usuario, MSI llegado por correo, instalación de herramienta de administración remota sin cambio aprobado, vaciado de proceso sobre utilidades del sistema y ventana falsa superpuesta al navegador. **Perseguir familia por familia es perseguir nombres; perseguir esos cinco comportamientos cubre a las seis y a la séptima que llegue.** Valoramos **muy probable** *(80–95 %)*. **Confianza: alta.** *Base:* convergencia de los seis informes técnicos de primera mano.

**KJ-6.** El ecosistema acaba de producir su primera familia escrita en Rust, y su analista plantea que podría ser una reescritura asistida por inteligencia artificial de una familia preexistente. `VENON`, identificada en febrero de 2026, no contiene una línea de Delphi: es Rust nativo de extremo a extremo, con Argon2id y XChaCha20 para su configuración y WebSocket sobre TLS 1.3 para su mando y control. ZenoX plantea como **hipótesis, sin asignarle nivel de confianza**, que sea «una refactorización mediante *vibecoding* asistido por IA de un troyano bancario ya establecido en la región, posiblemente Grandoreiro». Valoramos **posibilidad real** *(45–55 %)* de que la hipótesis se confirme en algún caso del ecosistema durante 2027. **Confianza: baja.** *Base:* fuente única, hipótesis declarada como tal por su autor, sin corroboración.

**KJ-7.** Nuestra exposición es doble y las dos mitades tienen dueños distintos. Como **organización**, el riesgo es el equipo corporativo comprometido por un correo del SII falso, que luego roba credenciales de navegador y propaga por WhatsApp a la agenda del empleado. Como **marca**, el riesgo es que nos suplanten igual que a la CGE: la alerta `CMV24-00455` describe exactamente eso contra una empresa de servicios chilena. Valoramos **muy probable** *(80–95 %)* que ambas caras sean materiales. **Confianza: moderada.** *Base:* el patrón está documentado contra terceros; su aplicación a nosotros es inferencia.

**Qué cambiaría estos juicios:** que el módulo de WhatsApp de Astaroth —o de cualquiera de sus clones— aparezca filtrando prefijos `+56`. Eso convertiría KJ-3 de proyección en hecho y este informe en una alerta. Es el indicador `I-1` de §O-7 y es el único de la lista que justificaría una revisión anticipada del producto.

---

## 2. Resumen ejecutivo

Brasil produce malware bancario desde hace una década y lo exporta a toda Iberoamérica. No son grupos de espionaje ni de extorsión: son familias de código —Mekotio, Mispadu, Grandoreiro, Astaroth, Coyote y ahora VENON— operadas por bandas distintas que comparten proveedores, técnicas y mercado. ESET contabilizó que once de las treinta familias de malware más detectadas de la región son brasileñas, y que Brasil concentra el 61 % de las detecciones regionales de troyanos bancarios.

De todas ellas, la que nos concierne directamente es Mekotio. ESET la describe como la familia que más afecta a Chile y documenta que sus muestras chilenas están construidas contra los portales de los 24 bancos con mayor presencia en el país. El Servicio de Impuestos Internos, la Tesorería General de la República y la Compañía General de Electricidad han sido suplantados en campañas que el CSIRT Nacional alertó públicamente, con indicadores incluidos, entre 2023 y 2025. En febrero de 2025, tras el apagón masivo, una campaña se hizo pasar por el Ministerio de Energía con una «Alerta de Posible Apagón Eléctrico» y entregó el implante instalando primero una herramienta legítima de administración remota, firmada y sin detecciones.

Ese último detalle resume el problema. Esta amenaza no llega como un fichero malicioso que un antivirus reconozca: llega como un MSI, un intérprete oficial de AutoIt, un agente de administración remota comercial o una biblioteca legítima de automatización descargada de GitHub. Y desde finales de 2025 llega también por un canal que prácticamente ningún control corporativo toca: el módulo nuevo de Astaroth se adhiere a la sesión de WhatsApp Web ya abierta de la víctima y escribe a sus contactos en su nombre. Hoy solo a números brasileños. El filtro que lo limita a Brasil es una línea de código.

Lo que pedimos a Dirección no es presupuesto, es decisión sobre tres cosas que ya están en nuestras manos: si un empleado puede ejecutar un MSI llegado por correo, si puede instalarse una herramienta de administración remota sin pasar por control de cambios, y si existe un procedimiento conocido para verificar una notificación del SII.

<!-- cti:cards -->

| Rasgo | Qué significa | Etiqueta |
|---|---|---|
| Chile es objetivo primario, no colateral | Es la única amenaza de esta cartera con alertas del CERT nacional y con muestras construidas contra los bancos del país | `01 · nacional` |
| El señuelo es el Estado, no el banco | SII, Tesorería General, CGE, Ministerio de Energía. Trámites que ninguna empresa puede ignorar ni archivar | `02 · pretexto` |
| Se entrega con software legítimo y firmado | MSI, AutoIt oficial, PDQ Connect firmado, bibliotecas de GitHub. La firma y la reputación no se activan | `03 · legítimo` |
| El canal nuevo es WhatsApp y nadie lo mira | Se adhiere a la sesión ya autenticada de la víctima y escribe a su agenda. Hoy filtrado a Brasil | `04 · canal` |
| Seis familias, cinco comportamientos | Perseguir nombres es perder; detectar los cinco comportamientos compartidos cubre también a la familia que aún no existe | `05 · detección` |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `24` | Bancos chilenos cuyos portales de banca electrónica ataca la variante chilena de Mekotio | ESET, análisis de la variante `CY` |
| `48` | Porcentaje de las detecciones mundiales de Mekotio registradas en Chile en el mes previo al informe de ESET de 2019 | Brasil quedó segundo con el 44 % |
| `5` | Alertas públicas del CSIRT Nacional de Chile que nombran esta familia entre 2023 y 2025 | SII (dos veces), CGE, Tesorería General, factura impaga genérica |
| `106` | Descargas e instalaciones potenciales contabilizadas en la campaña del Ministerio de Energía | Panel de monitoreo del propio atacante, feb-2025 |
| `3` | Mensajes que el módulo de WhatsApp envía a cada contacto de la víctima | Saludo, adjunto comprimido y texto de cierre |
| `55` | Prefijo telefónico al que está limitado hoy el gusano de WhatsApp | El filtro es una línea de código |
| `11` | Familias brasileñas entre las 30 más detectadas de la región | Brasil concentra el 61 % de las detecciones regionales de troyanos bancarios |

<!-- cti:note type="good" -->

> ✅ **Decisiones que se solicitan a Dirección.** (a) Bloquear la ejecución de ficheros `.msi` llegados por correo y la ejecución del intérprete de AutoIt desde rutas escribibles por el usuario — 30 días. (b) Prohibir la instalación de herramientas de administración remota sin ticket de cambio aprobado, y detectar las que ya estén instaladas sin él — 45 días. (c) Publicar un procedimiento de verificación de notificaciones del SII, la Tesorería General y empresas de servicios, por canal independiente — 60 días, con Asuntos Corporativos. (d) Decidir la postura sobre WhatsApp Web en equipos corporativos: bloqueo, o detección de navegador sin interfaz y de clonado de perfil — 60 días. (e) Suscribirse formalmente al canal de alertas del CSIRT Nacional e integrar sus indicadores en el SIEM, que hoy no se ingieren — 30 días.

---

## 3. Alcance, requisitos y limitaciones

**3.1 Requisitos de inteligencia atendidos**

| Req. | Enunciado | ¿Respondido? | Dónde |
|---|---|---|---|
| PIR-02 | ¿Qué superficie de suplantación institucional nos afecta en Chile? | Sí | §E-1, §E-2, §T-1 |
| PIR-04 | ¿Qué amenazas operan específicamente contra Chile y la región? | Sí | §E-2, §O-5 |
| PIR-06 | ¿Qué amenazas de fraude y robo de credenciales con impacto financiero nos alcanzan? | Sí | §O-3, §X-1 |
| PIR-08 | ¿Qué software y servicios legítimos se están usando como vehículo? | Sí | §X-2, §X-5, Anexo A |
| — | ¿Estamos ya comprometidos o suplantados? | **No** — requiere telemetría y vigilancia de marca | §O-4, §14 |

**3.2 Fuera de alcance.** No se evalúa: el fraude bancario minorista contra clientes brasileños, que es el grueso de la actividad del ecosistema y no nos aplica; el detalle interno de cada una de las seis familias, que ocuparía un producto por familia; el ecosistema brasileño de *stealers* genéricos y de malware NFC, que es adyacente y merece producto propio; y la respuesta a un fraude consumado, que es materia de Prevención de Fraude y no de este informe.

**3.3 Limitaciones de la colección.** (i) **Sin telemetría propia.** (ii) **Sesgo de encargo, y conviene dejarlo escrito.** Este producto se encargó bajo la premisa de que Mispadu era la familia de mayor relevancia chilena. La colección no lo sostiene: Unit 42 la describe centrada en México, Cofense cifra en febrero de 2026 que el 81 % de sus correos van en español y mayoritariamente a México, con Colombia y Argentina, y **ninguna de las tres fuentes técnicas de Mispadu menciona Chile**. La familia con relevancia chilena documentada es Mekotio, y el foco del informe se reorientó en consecuencia. Se consigna porque una premisa de partida equivocada es una limitación de la colección como cualquier otra, y porque el lector debe saber que el título del encargo y la conclusión no coinciden. (iii) **Las cifras chilenas más contundentes son de 2019 y 2020.** El 48 % de detecciones mundiales y los 24 bancos provienen de análisis de ESET de hace seis y siete años; la familia sigue activa y el CERT chileno sigue alertando, pero **no existe una medición reciente de la cuota chilena** y no debe presentarse el dato antiguo como actual. (iv) **La campaña del Ministerio de Energía descansa en una fuente única**, CronUp, y la cifra de 106 descargas proviene del panel del propio atacante, no de telemetría defensiva. (v) **Las alertas del CSIRT Nacional no traen recomendaciones ni análisis de persistencia**, y sus indicadores incluyen ficheros de software legítimo —el agente de PDQ Connect, `WixSharp.dll`— listados sin explicar el abuso: deben verificarse antes de bloquear. (vi) **No se leyeron los PDF adjuntos a las alertas del CSIRT**, de modo que el marcado interno de esos documentos no está verificado; el portal muestra `TLP:CLEAR` en cuatro de las cinco. (vii) **Discrepancias en los datos de origen**, consignadas donde aparecen: ZenoX da 33 objetivos bancarios en el cuerpo y «36+» en su tabla comparativa; Unit 42 nombra dos ficheros distintos para la misma etapa; Recorded Future publica 128 y 130 víctimas de ransomware en Brasil en el mismo documento.

**3.4 Metodología.** Disciplinas: OSINT gubernamental nacional (cinco alertas del CSIRT de Chile), OSINT comercial de proveedor (siete informes de primera mano), OSINT de marco regional (Recorded Future). Técnicas analíticas estructuradas: análisis de hipótesis competidoras (§O-6), comprobación de supuestos clave, pre-mortem. Marcos: MITRE ATT&CK v18, Pirámide del Dolor, Cadena de Intrusión, ICD 203, código Admiralty.

---

# NIVEL ESTRATÉGICO
### Para: Consejo · CISO · Riesgo · Asuntos Corporativos · Prevención de Fraude · Horizonte: 6–24 meses

## E-1. Qué representa este ecosistema en el panorama

Hay una razón por la que esta amenaza lleva una década funcionando y recibe una fracción de la atención que recibe el ransomware: no parece un problema de empresa. Parece fraude bancario de consumidor.

El diseño original lo justificaba. Estas familias nacieron para robarle las credenciales de banca en línea a una persona, mostrándole una ventana falsa cuando abría el portal de su banco. Pero las capacidades que fueron acumulando por el camino —robo de contraseñas guardadas en el navegador, volcado del gestor de credenciales, registro de pulsaciones, captura de pantalla, escritorio remoto oculto, sustitución del portapapeles— **no distinguen entre la cuenta bancaria personal del empleado y las credenciales corporativas que ese mismo navegador tiene guardadas.** El vector es doméstico; el botín, no necesariamente.

A eso se suma algo que cambia la naturaleza del riesgo. Desde finales de 2025 el ecosistema propaga por WhatsApp, y no mediante un enlace que el usuario reenvía: el módulo nuevo de Astaroth clona el perfil del navegador de la víctima, levanta un navegador sin interfaz en un puerto local aleatorio, borra las marcas de automatización para que no aparezca el aviso de «Chrome está siendo controlado», carga una biblioteca legítima de automatización descargada de GitHub y **se adhiere a la sesión de WhatsApp Web que la víctima ya tiene abierta y autenticada.** Luego recorre su agenda y escribe en su nombre. Tres mensajes por contacto. Un mensaje de un contacto conocido, en WhatsApp, en el idioma correcto, con un adjunto, es el vehículo de phishing con mejor tasa de apertura que existe, y no pasa por ninguna pasarela de correo.

El tercer rasgo estructural es el que hace inútil buena parte de nuestro arsenal: **esta amenaza se entrega con software legítimo.** El implante lo ejecuta el intérprete oficial de AutoIt. La entrega la hace un instalador MSI. En la campaña chilena de febrero de 2025 el implante llegó porque la víctima instaló PDQ Connect, una herramienta comercial de administración remota, firmada digitalmente y con cero detecciones en VirusTotal en ese momento; el atacante usó después ese agente legítimo para instalar lo demás. No hay firma que revocar ni reputación que consultar.

<!-- cti:cards -->

| Cambio estructural | Por qué nos afecta | Etiqueta |
|---|---|---|
| El vector es doméstico, el botín puede ser corporativo | El mismo navegador guarda la banca personal del empleado y las credenciales de trabajo. La frontera la pone nuestra política, no el malware | `01 · frontera` |
| La propagación usa la identidad de la víctima | Un WhatsApp de un contacto conocido con adjunto. No hay pasarela, no hay cabecera que analizar, no hay DMARC que aplicar | `02 · confianza` |
| El vehículo es software firmado | MSI, AutoIt oficial, herramienta de administración remota comercial, bibliotecas de GitHub. Firma y reputación no se activan | `03 · legítimo` |
| El pretexto es el trámite obligatorio | SII, Tesorería, empresa eléctrica. No se puede formar a la gente para que ignore una notificación tributaria | `04 · trámite` |
| El ecosistema se renueva comprando y, quizá, generando | Cargadores como servicio, criptadores por suscripción, y una primera familia en Rust que su analista sospecha reescrita con ayuda de IA | `05 · renovación` |

## E-2. Victimología y distribución

<!-- cti:bars title="Mekotio: detecciones mundiales por país, mes previo al informe de ESET (ago-2019)" color="#e0a33e,#5a7ebe,#4db99c" -->

| País | Porcentaje |
|---|---|
| Chile | 48 |
| Brasil | 44 |
| Resto | 8 |

<!-- cti:note type="warn" -->

> ⚠ **Este dato tiene siete años y hay que decirlo cada vez que se use.** Es la medición
> más contundente que existe sobre la exposición chilena a esta familia, y es de agosto de
> 2019. La familia sigue activa —el CERT chileno alertó en 2023, 2024 y 2025— pero **no
> existe una medición reciente de la cuota chilena**, y la distribución regional cambió:
> en 2023 ESET situó a Argentina al 52 %, México al 17 %, Perú al 12 %, Chile al 10 % y
> Brasil al 3 %. Las dos cifras son ciertas en su momento y describen cosas distintas.
> Presentar el 48 % como actual sería deshonesto; descartar la exposición chilena por el
> 10 % de 2023 también, porque esa serie mide detecciones de producto y no campañas.

<!-- cti:bars title="Instituciones chilenas suplantadas en campañas alertadas por el CSIRT Nacional" color="#c0392b" -->

| Institución | Alertas públicas |
|---|---|
| Servicio de Impuestos Internos | 2 |
| Compañía General de Electricidad | 1 |
| Tesorería General de la República | 1 |
| Factura impaga genérica | 1 |

**Los objetivos del ecosistema, por familia.** La división del trabajo es nítida y conviene conocerla porque determina quién nos puede alcanzar. **Mekotio** es la familia con foco chileno: 24 bancos del país, más 27 instituciones brasileñas, y campañas documentadas también en Argentina, México, Perú, España y Portugal; su kit de distribución de 2025 listaba diez países, Chile entre ellos. **Mispadu** es México y Brasil, con expansión reciente a España, Italia y Portugal y a casas de cambio de criptomonedas; está operada por un único grupo al que se atribuyen unos 55 millones de dólares acumulados. **Grandoreiro** es el más global: Brasil, México y España, con más de 1.700 entidades objetivo según la tabla comparativa de ZenoX, y es el único que ha sufrido una operación policial seria. **Astaroth** y **Coyote** son hoy exclusivamente brasileños. **VENON**, la familia nueva, también: 33 objetivos entre bancos brasileños, fintech, la Receita Federal y nueve casas de cambio y seis monederos de criptomonedas.

<!-- cti:note type="warn" -->

> ⚠ **Lectura regional — y aquí, por una vez, no es una brecha.** En los seis informes
> anteriores de esta serie la sección regional terminaba diciendo que Chile aparecía
> listado y no documentado. **Aquí la evidencia nacional es directa:** cinco alertas del
> CSIRT Nacional entre 2023 y 2025 que nombran la familia y publican indicadores; marcas
> chilenas concretas suplantadas; una campaña que explotó un acontecimiento nacional —el
> apagón de febrero de 2025— a los pocos días; geolocalización de la descarga restringida a
> direcciones IP chilenas ya en 2019; y muestras compiladas contra los portales de los
> bancos del país. Lo que falta no es evidencia de la amenaza: es **nuestra** telemetría
> para saber si nos alcanzó.

## E-3. Tendencia y pronóstico

<!-- cti:chart title="Alertas del CSIRT Nacional de Chile que nombran esta familia, por año" cap="Mide la actividad que el CERT nacional consideró digna de alerta pública, no el volumen real de campañas. 2026 figura en cero a la fecha de cierre; la alerta de abril de 2026 sobre el SII no atribuye familia." -->

| Periodo | Alertas |
|---|---|
| 2022 | 0 |
| 2023 | 2 |
| 2024 | 3 |
| 2025 | 1 |
| 2026 | 0 |

La trayectoria técnica del ecosistema en los últimos dos años tiene tres movimientos, y ninguno es un salto de sofisticación clásico.

El primero es **el canal**: de correo electrónico a WhatsApp. Recorded Future constata un aumento de troyanos bancarios dirigidos a la plataforma durante 2025, y a finales de ese año aparecen al menos tres implementaciones del mismo concepto —Vareg, Water Saci y el módulo de Astaroth— con nombres de función compartidos, lo que CrowdStrike valora con confianza moderada como un mismo desarrollador o un acuerdo de intercambio de código.

El segundo es **el vehículo**: de adjunto malicioso a software legítimo. La campaña chilena de 2025 no entregó malware, entregó un agente comercial de administración remota firmado.

El tercero es **el lenguaje**: la aparición de `VENON` en febrero de 2026, la primera familia del ecosistema escrita íntegramente en Rust, con criptografía moderna y mando y control por WebSocket cifrado. Su analista plantea —como hipótesis explícita, sin asignarle confianza— que podría ser una reescritura asistida por inteligencia artificial de una familia preexistente. Si eso se confirmara en algún caso, el coste de rehacer una de estas familias desde cero caería, y con él la vida útil de toda detección basada en artefactos de implementación.

<!-- cti:cards -->

| Escenario | Desarrollo | Etiqueta |
|---|---|---|
| Continuidad con rotación de canal y de marca suplantada | El ecosistema sigue alternando correo y WhatsApp, y adapta la institución suplantada al calendario tributario y a los acontecimientos nacionales. Las detecciones conductuales de §X-3 mantienen su validez | `Probable · 55–80 %` |
| Ampliación del gusano de WhatsApp más allá de Brasil | El filtro `+55` se amplía o se elimina y la propagación alcanza agendas chilenas. Es el cambio de mayor impacto y el más barato para el adversario | `Posibilidad real · 45–55 %` |
| Reescritura asistida por IA como práctica establecida | La hipótesis de `VENON` se confirma y se repite. Los artefactos de implementación dejan de ser útiles como indicador y la detección se repliega al comportamiento y al canal | `Poco probable · 20–45 %` |
| Convergencia con extorsión | Alguna de estas bandas vende el acceso corporativo obtenido a un grupo de ransomware en lugar de monetizar el fraude. Recorded Future describe el mercado de accesos, pero no documenta este puente | `Poco probable · 20–45 %` |

## E-4. Decisiones que este informe pide al nivel estratégico

<!-- cti:table highlight="Chile|chilen|SII|CSIRT|Tesorería|WhatsApp" -->

| # | Decisión | Fundamento | Plazo |
|---|---|---|---|
| E-a | **Bloquear la ejecución de `.msi` llegados por correo** y la ejecución del intérprete de AutoIt desde rutas escribibles por el usuario. Excepciones nominales y documentadas | KJ-4: el MSI es el vehículo de entrega en cuatro de las cinco campañas alertadas por el CSIRT, y AutoIt es el ejecutor del implante desde 2019 | 30 días |
| E-b | **Prohibir la instalación de herramientas de administración remota sin ticket de cambio aprobado**, y buscar las ya instaladas sin él. Incluir PDQ Connect, y no solo él, en la búsqueda | La campaña del Ministerio de Energía de feb-2025 entregó el implante instalando un agente comercial firmado y sin detecciones. El control es de proceso, no de firma | 45 días |
| E-c | Publicar y comunicar un **procedimiento de verificación de notificaciones del SII, de la Tesorería General y de empresas de servicios**, por canal independiente, con la lista de dominios oficiales legítimos | KJ-2: el pretexto es el trámite obligatorio. No se puede pedir a un empleado que ignore una notificación tributaria; sí se le puede dar una forma de comprobarla | 60 días |
| E-d | Fijar la **postura sobre WhatsApp Web en equipos corporativos**: bloqueo, o detección de navegador sin interfaz, clonado de perfil y descarga de controladores de Selenium | KJ-3: el módulo nuevo se adhiere a la sesión ya autenticada. Ningún control de correo participa, y hoy no mitigamos nada en este canal | 60 días |
| E-e | **Suscribirse formalmente al canal de alertas del CSIRT Nacional e ingerir sus indicadores en el SIEM.** Hoy no se ingieren, y este informe existe en parte porque nadie los estaba leyendo | Cinco alertas públicas con indicadores chilenos entre 2023 y 2025 que no estaban en nuestras listas. Es inteligencia gratuita, nacional y específica | 30 días |
| E-f | Encargar a Asuntos Corporativos la **vigilancia de suplantación de nuestra propia marca** en campañas de factura o notificación falsa, con procedimiento de denuncia al CSIRT | KJ-7: la alerta `CMV24-00455` describe exactamente este patrón contra una empresa chilena de servicios. La mitad de nuestra exposición es reputacional | 60 días |
| E-g | Incluir en formación un **módulo sobre notificación tributaria y de servicios falsa**, y uno específico sobre **adjuntos recibidos por WhatsApp de contactos conocidos** | El segundo es contraintuitivo y por eso necesario: la instrucción habitual es desconfiar de desconocidos, y aquí el remitente es un contacto real cuya sesión está secuestrada | 90 días |
| E-h | Evaluar con Prevención de Fraude el **impacto de un robo de credenciales de banca corporativa** por esta vía, y los controles compensatorios en el flujo de pagos | El objetivo final del ecosistema es el fraude. El control que corta la pérdida está en el proceso de pago, no en el endpoint | 90 días |

---

# NIVEL OPERACIONAL
### Para: Jefatura de SOC · Respuesta a Incidentes · Threat Hunting · Seguridad del Correo · Horizonte: semanas–meses

## O-1. Identificación: seis familias, no un actor

Este informe cubre un **ecosistema**, y la distinción no es académica: confundir familia con actor llevaría a atribuir a un mismo grupo campañas que operan bandas distintas, con infraestructura distinta y objetivos distintos, y que solo comparten mercado y proveedores.

| Familia | Alias | Lenguaje | Periodo activo | Foco geográfico | Relación con las demás |
|---|---|---|---|---|---|
| `Mekotio` | Casbaneiro, Metamorfo | Delphi | 2015–2026 | **Chile** (foco principal), Brasil, Argentina, México, Perú, España, Portugal | Familia distinta; comparte técnicas y mercado |
| `Mispadu` | URSA | Delphi | 2019–2026 | México y Brasil, con expansión a España, Italia y Portugal | Operada por **un único grupo**: `TA2725`, `Malteiro` (SCILabs), `Manipulated Caiman` (Perception Point) |
| `Grandoreiro` | — | Delphi | 2017–2026 | Brasil, México, España. 45 países según ZenoX | El único con operación policial internacional (ene-2024) |
| `Astaroth` | Guildma | Delphi (núcleo), AutoIt (cargador) | 2015–2026 | **Exclusivamente Brasil** hoy | Comparte código de *spambot* con `Vareg` |
| `Coyote` | — | .NET + Nim | 2024–2026 | Brasil | Distribuido por el cargador `SORVEPOTEL`, igual que `Maverick` |
| `VENON` | — | **Rust nativo** | 2024–2026 | Brasil | Atribución de **baja confianza**; posible reescritura de otra familia |
| `Vareg` | WATER SACI, Eternidade | PowerShell → Python | 2025 (cesó en 4T) | Brasil | Su cese coincide con la aparición del *spambot* de Astaroth |

<!-- cti:note type="warn" -->

> ⚠ **Nota de tradecraft — dos errores concretos que evitar.** El primero: `Mekotio`,
> `Casbaneiro` y `Metamorfo` se usan como sinónimos en la literatura, pero distintos
> proveedores trazan la línea en sitios distintos; al leer un informe hay que comprobar
> qué conjunto de muestras llama así cada uno. El segundo: **compartir un cargador no es
> ser el mismo actor.** `Coyote` y `Maverick` se distribuyen por la misma infraestructura
> de `SORVEPOTEL`; `Mispadu` y `Grandoreiro` los ha usado el mismo grupo; `Astaroth` y
> `Vareg` comparten nombres de función. Nada de eso los une más allá del proveedor, igual
> que compartir mensajería no une a dos empresas.

## O-2. Atribución: qué se puede sostener

| Eje de atribución | Valoración | Confianza |
|---|---|---|
| Origen del ecosistema | Brasil. Once de las treinta familias más detectadas de la región son brasileñas y el país concentra el 61 % de las detecciones regionales de troyanos bancarios | Alta |
| Motivación | Fraude financiero. No hay un solo caso documentado de espionaje ni de extorsión con cifrado en ninguna de las seis familias | Alta |
| Operadores | Bandas distintas por familia. Solo en `Mispadu` hay un operador único identificado y seguido por tres proveedores con tres nombres | Moderada |
| Modelo de negocio | Mixto: operación propia más compra de servicios (cargador, criptador, alojamiento). `Grandoreiro` es el único descrito como «MaaS parcial» | Moderada |
| Nexo estatal | **No planteado por ninguna fuente** | Alta (en la negativa) |
| Idioma de operación | Portugués para el ecosistema; español para las campañas dirigidas a Hispanoamérica. El *spambot* de Astaroth compone sus saludos en portugués | Alta |
| Atribución de `VENON` | **Baja por declaración expresa de su analista:** «la atribución de VENON a un operador o grupo conocido presentó baja confianza a lo largo del análisis» | Baja |

*Razonamiento sobre el origen brasileño:* el ecosistema comparte lenguaje de programación histórico (Delphi), bibliotecas de cifrado (`DelphiEncryptionCompendium`), nombres de función y de variable en portugués, infraestructura de alojamiento y un mercado de servicios común. En `VENON`, una versión temprana expuso rutas de compilación con el nombre de usuario del desarrollador.

*Contraargumento:* el origen del código no determina el origen del operador de una campaña concreta. Una campaña contra Chile con señuelo del SII y terminología chilena correcta la redacta alguien que conoce Chile, no necesariamente el autor del implante. Es la misma economía de capas que `CTI-2026-020` describe en Blind Eagle, vista desde el lado del proveedor.

## O-3. Cómo se monetiza, y por qué eso nos importa

El objetivo es el fraude, y la cadena de monetización determina qué controles cortan la pérdida.

**La captura.** Tres mecanismos, por orden de antigüedad. El primero y más característico es la **ventana falsa**: el implante vigila los títulos de ventana y los dominios que visita el navegador, y cuando reconoce el portal de un banco objetivo superpone una ventana de inicio de sesión que imita a la entidad. El segundo es el **robo de lo ya guardado**: contraseñas almacenadas en navegadores Chromium y Opera, para lo que las familias llevan `SQLite3.dll` y, en las versiones recientes, evasión del cifrado vinculado a aplicación; más el gestor de credenciales de Windows, Outlook y Thunderbird. El tercero es el **registro de pulsaciones y la captura de pantalla**, con escritorio remoto oculto en las variantes más capaces.

**El desvío directo.** Dos técnicas que no requieren credenciales. La **sustitución del portapapeles**: cuando la víctima copia una dirección de monedero de criptomonedas, el implante la cambia por la del atacante. ESET analizó una de esas direcciones en 2020 y contabilizó seis transacciones por 0,2678 BTC, unos 2.500 dólares de entonces. Y en Brasil, la **interceptación del QR de Pix y la sustitución del boleto**, que `VENON` declara en su tabla de capacidades.

**El atajo chileno.** La variante de Mekotio dirigida a Chile está construida contra los portales de los 24 bancos de mayor presencia en el país, y ataca tanto cuentas personales como **cuentas de empresa**. Esa última palabra es la que convierte un problema de fraude de consumidor en un problema nuestro.

**Lo que esto implica para la defensa.** Si la captura ocurre en el navegador del empleado, el control que evita la pérdida no está en el endpoint: está en el **flujo de pagos**. Doble autorización, límites por transacción, verificación fuera de banda de cambios de destinatario. Es la decisión E-h, y es la única de este informe que sigue funcionando incluso si el compromiso del equipo tiene éxito.

## O-4. Nuestra exposición

<!-- cti:note type="gap" -->

> ⬛ **Sección sin evaluar — requiere telemetría e inventario internos.** De las once
> preguntas, **X-1, X-2 y X-4 se responden en una tarde** y son las que más cambian la
> postura. Ninguna requiere compra.

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| X-1 | ¿Se ejecuta el intérprete de AutoIt (`AutoIt3.exe` o renombrado) en algún equipo, desde qué ruta y con qué argumento? | EDR · creación de procesos | SOC |
| X-2 | ¿Puede un empleado ejecutar un `.msi` descargado del correo? ¿Ha ocurrido en los últimos 90 días? | EDR · política de software | TI / SOC |
| X-3 | ¿Hay herramientas de administración remota instaladas sin ticket de cambio? Buscar PDQ Connect y equivalentes | Inventario de software · control de cambios | TI |
| X-4 | ¿Se ingieren las alertas del CSIRT Nacional en el SIEM? ¿Están cargados los indicadores de las cinco alertas de esta familia? | Revisión del SIEM y de la plataforma de inteligencia | Ingeniería de Detección |
| X-5 | ¿Cuántos equipos corporativos tienen sesión de WhatsApp Web abierta? ¿Está permitido? | Proxy · política | Seguridad / TI |
| X-6 | ¿Detectamos la creación de carpetas de perfil de navegador clonado en `C:\Users\Public\Temp\` y la ejecución de navegador sin interfaz? | EDR | Ingeniería de Detección |
| X-7 | ¿Permitimos la descarga de controladores de Selenium (`chromedriver`, `msedgedriver`) y de bibliotecas de GitHub por procesos que no son navegadores? | Proxy · EDR | Redes / SOC |
| X-8 | ¿Guardan nuestros empleados credenciales corporativas en el navegador? ¿Está deshabilitado el gestor de contraseñas del navegador por directiva? | Directiva de navegador | Identidad |
| X-9 | ¿Qué cuentas de banca corporativa existen, con qué equipos se operan y qué controles de doble autorización tienen? | Tesorería · Finanzas | Prevención de Fraude |
| X-10 | ¿Existe vigilancia de suplantación de nuestra marca en campañas de factura o notificación falsa? | Vigilancia de marca | Asuntos Corporativos |
| X-11 | ¿Tenemos registro de creación de procesos con línea de comandos y 90 días de retención, imprescindible para §X-3? | Revisión de fuentes del SIEM | Ingeniería de Detección |

## O-5. Cronología

<!-- cti:timeline -->

| Fecha | Hecho | Traza |
|---|---|---|
| `2015` | Primeras muestras atribuidas a `Mekotio` y a `Astaroth` | Global |
| `2017` | Primeras muestras de `Grandoreiro` | Global |
| `2019-08-16` | **ESET documenta una campaña dirigida a Chile**: correo con falso informe de deuda de una compañía de servicios telefónicos chilena, y **enlace de descarga que solo funciona desde direcciones IP chilenas**. Chile concentra el 48 % de las detecciones mundiales del mes; Brasil, el 44 % | Chile |
| `2019` | Primeras muestras de `Mispadu` | Global |
| `2020-07-14` | ESET publica el análisis de la variante `CY` de Mekotio, **dirigida a usuarios de Chile**: ataca los portales de los **24 bancos de mayor presencia en el país** y 27 instituciones brasileñas, roba contraseñas de Chrome y Opera y sustituye direcciones de Bitcoin en el portapapeles | Chile |
| `2022-08` | Comienzan las campañas de Mispadu que acumularán más de 90.000 credenciales robadas según la medición de un proveedor | Global |
| `2023-06-08` | **Primera alerta del CSIRT Nacional de Chile sobre Mekotio** (`2CMV23-00417-01`): suplanta al **Servicio de Impuestos Internos** con una falsa factura no pagada, entregando `.zip` y `.msi`. La alerta nombra como objetivos Brasil, Chile, México, España, Perú y Portugal | Chile |
| `2024-01` | **Operación policial internacional contra `Grandoreiro`**: la Policía Federal de Brasil ejecuta cinco detenciones y trece órdenes de registro en cinco estados, con coordinación de INTERPOL y aporte técnico de varios proveedores. Más de 3,5 millones de euros robados; una entidad bancaria estima que los intentos fallidos habrían superado los 110 millones | Global |
| `2024-02-02` | Unit 42 publica una variante de Mispadu que abusa de la elusión de SmartScreen `CVE-2023-36025` mediante un `.url` que apunta a una ruta de red; constata que las muestras **se compilaron antes de la publicación del CVE** | Global |
| `2024-04-08` | Alerta del CSIRT Nacional (`CMV24-00455`): Mekotio suplanta a la **Compañía General de Electricidad** con un falso retraso en el pago de una factura. La alerta indica que **la campaña está preparada para Chile** | Chile |
| `2024-05-22` | Alerta del CSIRT Nacional (`CMV24-00463`): Mekotio suplanta de nuevo al **SII**, esta vez con un falso problema en la emisión de boletas electrónicas | Chile |
| `2024-08-22` | Alerta del CSIRT Nacional (`CMV24-00483`): Mekotio suplanta a la **Tesorería General de la República** con una supuesta devolución de impuestos pendiente | Chile |
| `2025-01-16` | Alerta del CSIRT Nacional (`CMV25-00499`): campaña de factura impaga genérica que entrega Mekotio **usando el agente de PDQ Connect**; la alerta lista como indicadores ficheros del propio software legítimo | Chile |
| `2025-02-27` | **CronUp documenta la campaña del Ministerio de Energía**: señuelo «Alerta de Posible Apagón Eléctrico» aprovechando el corte de luz masivo en Chile, entregando PDQ Connect firmado y sin detecciones. El panel del atacante muestra **al menos 106 descargas potenciales**. El kit lista diez países objetivo, Chile entre ellos | Chile |
| `2025-10` → `11` | `Vareg` distribuye troyanos bancarios a usuarios brasileños vía WhatsApp; su desarrollador reescribe el componente de PowerShell a Python y, según CrowdStrike, «probablemente usó IA» | Global |
| `2025-4T` | **El cese de `Vareg` coincide con la aparición del módulo de *spambot* de `Astaroth`**, que comparte nombres de función y lógica de filtrado. CrowdStrike valora con confianza moderada un mismo desarrollador o un acuerdo de intercambio de código | Global |
| `2026-01` | ZenoX encuentra una versión temprana en DLL de `VENON` durante actividad de caza | Global |
| `2026-02` | **ZenoX identifica `VENON`**, primera familia del ecosistema escrita íntegramente en Rust, y plantea la hipótesis de que sea una reescritura asistida por IA de una familia preexistente | Global |
| `2026-02-11` | Cofense publica la línea base de Mispadu: desde 2025 **todas** las campañas observadas arrancan con un fichero `HTA`, y el 81 % de los correos van en español, mayoritariamente a México | Global |
| `2026-04` | El CSIRT Nacional alerta de un sitio fraudulento que suplanta al SII, **sin atribución de familia** | Chile |
| `2026-07-29` | **CrowdStrike publica el análisis del *spambot* de Astaroth**: clonado del perfil del navegador, navegador sin interfaz en puerto aleatorio, adhesión a la sesión de WhatsApp Web autenticada y envío de tres mensajes por contacto, filtrado a números `+55` | Global |
| `2026-11-16` | Cierre de este informe. **Sin alerta del CSIRT Nacional sobre esta familia en 2026** y sin medición reciente de la cuota chilena | Chile |

## O-6. Hipótesis alternativas consideradas

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| H1 — Ecosistema de familias independientes con proveedores y mercado comunes, orientado al fraude financiero | Consistente con las doce fuentes. Explica la convergencia técnica sin exigir un actor único, y explica que los saltos de capacidad lleguen de golpe y no por evolución | `Retenida` |
| H2 — Es fraude de consumidor y no un riesgo corporativo | **Inconsistencia decisiva:** la variante chilena ataca explícitamente cuentas de empresa, y las capacidades de robo no distinguen entre credenciales personales y corporativas guardadas en el mismo navegador. **El núcleo de verdad que hay que conservar:** el impacto más probable sigue siendo fraude sobre un empleado, no compromiso del dominio, y eso cambia a quién corresponde el control | `Poco probable · 20–45 %` |
| H3 — La exposición chilena es histórica y hoy marginal | Parcialmente apoyada: las cifras fuertes son de 2019-2020 y la serie de 2023 sitúa a Chile en el 10 % regional. **Pero** el CERT nacional alertó en 2023, 2024 y 2025, y la campaña de feb-2025 fue chilena y oportunista. Se retiene como advertencia contra el alarmismo, no como conclusión | `Retenida como matiz` |
| H4 — El gusano de WhatsApp se ampliará más allá de Brasil | Sin evidencia directa; apoyada por el coste marginal nulo del cambio y por el precedente de todas estas familias, que localizan señuelos por país desde 2019. Es el juicio más consecuente de este informe y el más débilmente sostenido | `Posibilidad real · 45–55 %` |
| H5 — `VENON` es una familia nueva de un actor nuevo | Posible y no descartable: su propio analista declara baja confianza en cualquier atribución. La hipótesis alternativa —reescritura de Grandoreiro— tampoco está sostenida. **Se consigna el desacuerdo, no se resuelve** | `Retenida sin resolver` |
| H6 — Hay un actor único coordinando el ecosistema | **Sin evidencia.** Infraestructura, objetivos, lenguajes y operadores difieren; lo único compartido son proveedores y mercado. Se consigna para que no se reabra | `Descartada` |

**Supuesto clave.** Que el canal de entrega seguirá siendo correo electrónico y WhatsApp sobre Windows de escritorio. **Si es falso** —si el ecosistema se desplaza a móvil, como ya apuntan las familias adyacentes de NFC y los troyanos bancarios de Android de la región— entonces todas las detecciones de §X-3, que son de endpoint Windows, quedan fuera de juego, y la defensa se traslada a la aplicación bancaria y al dispositivo personal, donde no tenemos ni visibilidad ni autoridad.

**Pre-mortem.** Es mayo de 2027 y este informe resultó equivocado. Los tres finales más probables: **(1)** cerramos MSI y AutoIt, y el compromiso llegó por WhatsApp a un equipo con sesión abierta, canal sobre el que no tomamos la decisión E-d; **(2)** acertamos en el endpoint y la pérdida se produjo igualmente porque el flujo de pagos no tenía doble autorización —la decisión E-h, la única que corta la pérdida, es también la que menos depende de seguridad—; **(3)** dedicamos el esfuerzo a Chile y el golpe vino por una filial en otro país del kit de distribución, donde ni formamos ni medimos.

## O-7. Indicadores y señales de alerta

| # | Indicador observable | Qué señalaría | Disciplina | Responsable |
|---|---|---|---|---|
| I-1 | **Módulo de propagación por WhatsApp filtrando prefijos `+56`** u otros distintos de `+55` | Convierte KJ-3 de proyección en hecho; obliga a revisión anticipada del informe y a ejecutar E-d sin esperar plazo | OSINT comercial | Célula CTI |
| I-2 | Alerta nueva del CSIRT Nacional nombrando esta familia | Campaña chilena activa; cargar indicadores el mismo día | OSINT gubernamental | SOC / Célula CTI |
| I-3 | Señuelo que suplante a **nuestra** marca en una campaña de factura o notificación | Materializa la mitad reputacional de KJ-7; activa denuncia al CSIRT y comunicación a clientes | Vigilancia de marca | Asuntos Corporativos |
| I-4 | Campaña que explote un acontecimiento nacional chileno reciente —corte de servicio, catástrofe, proceso electoral, plazo tributario— | Patrón confirmado en feb-2025. Precede en días al pico de la campaña | OSINT · prensa | Célula CTI |
| I-5 | Confirmación pública de desarrollo de malware asistido por IA en el ecosistema | Confirma KJ-6; reduce la vida útil de toda detección por artefacto de implementación | OSINT comercial | Célula CTI / Ingeniería de Detección |
| I-6 | Aparición de estas familias sobre plataforma móvil con la misma victimología | Rompe el supuesto clave de §O-6 y traslada la defensa fuera de nuestro perímetro de control | OSINT comercial | Célula CTI |
| I-7 | Venta de acceso corporativo chileno en foros, atribuida a infección por troyano bancario | Materializaría el puente al ransomware que hoy no está documentado | OSINT · foros criminales | Célula CTI |
| I-8 | Nuevo cargador como servicio brasileño distribuyendo más de una de estas familias | Precede históricamente a saltos de capacidad simultáneos en varias familias | OSINT comercial | Célula CTI |

---

# NIVEL TÁCTICO
### Para: Analistas de SOC · Ingeniería de Detección · Threat Hunting · Horizonte: días–semanas

## T-1. Cadena de intrusión

<!-- cti:stages title="Tres etapas, y el software de las tres es legítimo" dwell="next" -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 01 · Trámite | El aviso oficial que hay que atender | Correo suplantando al **SII** (factura impaga, problema con boletas electrónicas), a la **Tesorería General** (devolución de impuestos pendiente), a la **CGE** (retraso en el pago), al **Ministerio de Energía** (alerta de apagón) o una factura impaga genérica · enlace con redirección en cadena por varios dominios comprometidos · descarga automática de `.zip` que contiene un `.msi` · o fichero `HTA` como primera etapa, hoy el 100 % de las campañas de Mispadu · o `.url` apuntando a ruta de red para eludir SmartScreen · o, desde finales de 2025, **mensaje de WhatsApp de un contacto conocido con adjunto comprimido** |
| Etapa 02 · Ejecución | Intérpretes oficiales haciendo el trabajo | El `.msi` descarga un `.zip` a `C:\programdata\<aleatorio>\` con cuatro ficheros: **el intérprete oficial de AutoIt**, un script `.au3` que carga la DLL, la DLL del implante en Delphi y `SQLite3.dll` para leer las bases de contraseñas · o cadena `HTA → dropper JavaScript → VBS` · o PowerShell oculto mediante WMI con `ShowWindow=0` · o instalación de **PDQ Connect**, agente comercial firmado, usado después para instalar el implante remotamente · evasión: anti-VM por procesos (`VBoxService.exe`), `IsDebuggerPresent`, comportamiento según idioma del sistema, ocultación en el Administrador de tareas, desactivación del registro de eventos, autodestrucción · persistencia por clave de ejecución automática o acceso directo en la carpeta de Inicio, **ambos apuntando al intérprete de AutoIt** |
| Etapa 03 · Fraude | Credenciales, y el dinero por la vía corta | Vigilancia de títulos de ventana y dominios del navegador · **ventana de inicio de sesión falsa** al detectar uno de los 24 bancos chilenos, personales o de empresa · robo de contraseñas guardadas en Chromium y Opera con `SQLite3.dll`, evasión del cifrado vinculado a aplicación en variantes recientes · gestor de credenciales de Windows, Outlook, Thunderbird, claves Wi-Fi · registro de pulsaciones, captura de pantalla, escritorio remoto oculto · **sustitución de direcciones de criptomonedas en el portapapeles** · interceptación de QR de Pix y sustitución de *boleto* en las familias brasileñas · C2 con dirección obtenida de un documento público que el atacante actualiza, en puertos no estándar · **propagación por la sesión de WhatsApp Web de la víctima** |

**Permanencia:** no hay cifra pública. El modelo no requiere permanencia prolongada: la captura de credenciales y la sustitución de portapapeles producen resultado desde el primer uso del navegador. La campaña del Ministerio de Energía contabilizó 106 instalaciones potenciales en pocos días.

<!-- cti:note type="info" -->

> **Dónde se rompe la cadena más barato.** La **etapa 01 se corta con política de correo y
> con proceso**: bloquear `.msi`, `.hta` y `.url` entrantes, y dar a la gente una forma de
> verificar una notificación del SII. La **etapa 02 se corta con dos reglas de ejecución**
> —ni MSI de correo, ni AutoIt desde rutas de usuario— y es, con diferencia, la
> intervención de mejor relación coste-efecto de este informe: son dos líneas de política
> que invalidan la cadena documentada desde 2019. La **etapa 03 no se corta en el endpoint**:
> si el implante corre, las credenciales salen. Lo que evita la pérdida a esas alturas está
> en el flujo de pagos, y por eso la decisión E-h no es de seguridad informática.

## T-2. Mapa MITRE ATT&CK

<!-- cti:matrix -->

| Táctica | ID | Técnica | Procedimiento observado |
|---|---|---|---|
| Desarrollo de recursos | T1583.001 | Acquire Infrastructure: Domains | Dominios de descarga, redirección y contención publicados en las alertas del CSIRT chileno |
| Desarrollo de recursos | T1584 | Compromise Infrastructure | Sitios legítimos comprometidos usados como contenedores de malware y como destino de exfiltración |
| Desarrollo de recursos | T1588.001 | Obtain Capabilities: Malware | Cargadores como servicio (`SORVEPOTEL`, `Caminho`) y criptadores por suscripción |
| Desarrollo de recursos | T1588.002 | Obtain Capabilities: Tool | Intérprete oficial de AutoIt, `SQLite3.dll`, PDQ Connect, controladores de Selenium, biblioteca `WPPConnect/WA-JS` |
| Acceso inicial | T1566.001 | Phishing: Spearphishing Attachment | Adjuntos `.zip` con `.msi`, ficheros `HTA`, `.url` apuntando a ruta de red |
| Acceso inicial | T1566.002 | Phishing: Spearphishing Link | Enlace a falso formulario o factura, con redirección en cadena. Es la técnica que el CSIRT chileno cita en las cinco alertas |
| Acceso inicial | T1189 | Drive-by Compromise | Descarga automática del `.zip` al visitar la página de redirección |
| Movimiento lateral | T1534 | Internal Spearphishing | **Propagación por la sesión de WhatsApp Web autenticada de la víctima** a los contactos de su agenda |
| Ejecución | T1204.001 | User Execution: Malicious Link | El usuario pulsa el enlace de la notificación falsa |
| Ejecución | T1204.002 | User Execution: Malicious File | El usuario ejecuta el `.msi` o hace doble clic en el `.js` descargado por el portal falso |
| Ejecución | T1059.001 | Command and Scripting Interpreter: PowerShell | Descarga del controlador de Selenium; evasión de protecciones del sistema (citado en `CMV25-00499`) |
| Ejecución | T1059.003 | Command and Scripting Interpreter: Windows Command Shell | Fichero `.cmd` de la campaña de la Tesorería General |
| Ejecución | T1059.005 | Command and Scripting Interpreter: Visual Basic | Etapa `VBS` en la cadena de Mispadu; script de secuestro de accesos directos en `VENON` |
| Ejecución | T1059.007 | Command and Scripting Interpreter: JavaScript | Dropper JavaScript intermedio; scripts inyectados en el navegador para automatizar WhatsApp |
| Ejecución | T1047 | Windows Management Instrumentation | Obtención de información del sistema (`CMV25-00499`); lanzamiento de PowerShell con ventana oculta |
| Ejecución | T1569.002 | System Services: Service Execution | Ejecución por servicio citada en `CMV25-00499` |
| Ejecución | T1218.011 | System Binary Proxy Execution: Rundll32 | `rundll32` como ejecutor, citado en `CMV25-00499` y en la cadena WebDAV de Mispadu |
| Persistencia | T1547.001 | Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder | Clave de ejecución automática o acceso directo en Inicio, **ambos apuntando al intérprete de AutoIt** |
| Persistencia | T1053.005 | Scheduled Task/Job: Scheduled Task | Tarea `NVIDIA Notification Service` en `VENON` |
| Persistencia | T1543.003 | Create or Modify System Process: Windows Service | Servicio que no permite detención ni eliminación, descrito por ESET en 2019 |
| Evasión | T1036.003 | Masquerading: Rename System Utilities | Renombrado de utilidades legítimas, citado en `CMV25-00499`; `AutoIt3.exe` renombrado |
| Evasión | T1036.005 | Masquerading: Match Legitimate Resource Name or Location | Ficheros con nombre de biblioteca de sistema (`shfolder.dll`, `ssleay32.dll`, `libeay32.dll`) |
| Evasión | T1574.001 | Hijack Execution Flow: DLL | Carga lateral de DLL; en `VENON`, `libcef.dll` malicioso cargado por un binario firmado de NVIDIA |
| Evasión | T1497 | Virtualization/Sandbox Evasion | Vigilancia de procesos de máquina virtual, `IsDebuggerPresent`, comprobaciones anti-caja de arena |
| Evasión | T1562.002 | Impair Defenses: Disable Windows Event Logging | Citado en la alerta de la Tesorería General |
| Evasión | T1562.001 | Impair Defenses: Disable or Modify Tools | Exclusión de Defender para la carpeta de trabajo; evasión de AMSI y de ETW en `VENON` |
| Evasión | T1518.001 | Software Discovery: Security Software Discovery | Búsqueda de productos de seguridad instalados |
| Evasión | T1564.003 | Hide Artifacts: Hidden Window | Navegador sin interfaz; PowerShell con `ShowWindow=0`; ocultación en el Administrador de tareas |
| Evasión | T1490 | Inhibit System Recovery | Citado en la alerta `CMV25-00499` |
| Evasión | T1027.013 | Obfuscated Files or Information: Encrypted/Encoded File | Configuración cifrada con AES-CTS y HMAC-SHA256 en el *spambot*; Argon2id y XChaCha20 en `VENON` |
| Acceso a credenciales | T1555.003 | Credentials from Password Stores: Credentials from Web Browsers | Robo de contraseñas guardadas en Chromium y Opera mediante `SQLite3.dll`; evasión del cifrado vinculado a aplicación |
| Acceso a credenciales | T1555.004 | Credentials from Password Stores: Windows Credential Manager | Volcado del gestor de credenciales |
| Acceso a credenciales | T1056.001 | Input Capture: Keylogging | Registro de pulsaciones, activado al detectar el portal de un banco objetivo |
| Acceso a credenciales | T1056.002 | Input Capture: GUI Input Capture | **Ventana de inicio de sesión falsa superpuesta** que imita el portal del banco. Es la técnica característica de la familia |
| Acceso a credenciales | T1552.001 | Unsecured Credentials: Credentials In Files | Credenciales en ficheros, citado en la primera alerta del CSIRT chileno |
| Descubrimiento | T1012 | Query Registry | Citado en las cinco alertas del CSIRT chileno |
| Descubrimiento | T1082 | System Information Discovery | Recolección de información del sistema mediante comandos SQL o WMI |
| Descubrimiento | T1033 | System Owner/User Discovery | Citado en `CMV25-00499` |
| Descubrimiento | T1007 | System Service Discovery | Citado en `CMV25-00499` |
| Descubrimiento | T1120 | Peripheral Device Discovery | Citado en `CMV24-00463` |
| Recolección | T1113 | Screen Capture | Captura de pantalla en las variantes con control remoto |
| Recolección | T1115 | Clipboard Data | Lectura del portapapeles, previa a su sustitución |
| Recolección | T1005 | Data from Local System | Recolección de datos locales, citado en la primera alerta del CSIRT chileno |
| Mando y control | T1071.001 | Application Layer Protocol: Web Protocols | Exfiltración por HTTP a sitios comprometidos; `VENON` usa WebSocket sobre TLS 1.3 |
| Mando y control | T1102 | Web Service | **Dirección del C2 obtenida de un documento público que el atacante actualiza periódicamente**; `VENON` la toma de un depósito en la nube |
| Mando y control | T1571 | Non-Standard Port | Puertos observados en las alertas chilenas: 9091, 57496, 7957 |
| Mando y control | T1105 | Ingress Tool Transfer | Descarga de etapas sucesivas y de componentes adicionales |
| Impacto | T1565.002 | Data Manipulation: Transmitted Data Manipulation | **Sustitución de direcciones de criptomonedas en el portapapeles**; interceptación de QR de Pix y sustitución de *boleto* |
| Exfiltración | T1041 | Exfiltration Over C2 Channel | Envío de credenciales y de información del sistema por el canal de control |

<!-- cti:note type="warn" -->

> ⚠ **Nota de precisión sobre esta tabla.** Las técnicas provienen de tres orígenes que
> conviene no mezclar: las que el **CSIRT Nacional** lista en sus cinco alertas, que están
> citadas como tal; las que **ESET** publica en su tabla ATT&CK de 2020, con numeración
> antigua que se ha traducido a la actual —`T1192` y `T1194` corresponden hoy a `T1566.002`
> y `T1566.001`, y `T1503` a `T1555.003`—; y las que se deducen de los procedimientos
> descritos por CrowdStrike, ZenoX y Unit 42, que **no publican mapeo ATT&CK**. Donde un
> procedimiento no estaba descrito, la técnica se ha omitido en lugar de rellenarla por
> conjetura.

## T-3. Dónde atacamos en la Pirámide del Dolor

<!-- cti:pyramid -->

| Nivel | Qué contiene en este informe y qué vale | Valor |
|---|---|---|
| Hashes | Más de veinte en el Anexo A, la mayoría de las alertas del CSIRT chileno. **Valor real pero limitado:** ESET advierte desde 2020 que los *hashes* de esta familia son de vida corta. Útiles para retrohunt sobre los 90 días previos y para confirmar un caso, no para prevenir | Base · valor trivial |
| IP · Dominios | Más de treinta, también de las alertas chilenas. Rotan rápido y buena parte son **sitios legítimos comprometidos**, de modo que bloquear el dominio castiga a un tercero inocente. El C2 se obtiene además de un documento público que el atacante cambia a voluntad | Valor bajo |
| Artefactos | **Lo más duradero de esta amenaza, y ESET lo publicó en 2020.** Ficheros de marca en el perfil del usuario (`Bizarro.txt`, `V.txt`, `Ok.txt`, `Etc`, `<intérprete>.jkl`, `<intérprete>.exe.jpg`), carpeta `C:\Users\Public\Temp\ChromeAuto_<id><fecha>`, clave HMAC `TenHaVunf!@#2026`, palabra mágica de configuración `EF01`, nombres de función `BaixarWAJS`, `ProcessarEnvio`, `ProcessarContatos`, `WebDriverUpdater`, formato de comando C2 `<\|comando\|>` | Valor medio |
| Herramientas | Intérprete oficial de AutoIt, `SQLite3.dll`, `msiexec`, PowerShell, WMI, `rundll32`, PDQ Connect, controladores de Selenium, `WPPConnect/WA-JS`. **Todas legítimas, varias firmadas.** Detectar por contexto, por ruta y por relación padre-hijo | Valor alto |
| TTP | Intérprete de AutoIt ejecutándose desde ruta de usuario; MSI llegado por correo; administración remota instalada sin cambio aprobado; navegador sin interfaz con perfil clonado; ventana superpuesta sobre el navegador. **Cinco comportamientos que cubren seis familias y la séptima que venga** | Cima · valor máximo |

## T-4. Hipótesis de caza prioritarias

<!-- cti:accordion critical="^(H-1|H-2|H-3|H-4)\b" regional="^(H-12|H-13)\b" -->

**H-1 — Intérprete de AutoIt ejecutándose desde ruta escribible por el usuario.** `AutoIt3.exe`, o cualquier binario cuyo nombre original sea ése, ejecutándose desde `C:\ProgramData\`, `%TEMP%`, `%APPDATA%`, `%LOCALAPPDATA%` o el perfil del usuario, con un argumento `.au3` o sin argumento reconocible. Fuente: creación de procesos del EDR. **Es la hipótesis madre de este informe:** cubre la cadena documentada de Mekotio desde 2019 y la de Astaroth hoy. Fidelidad esperada muy alta: AutoIt tiene usos legítimos de automatización, pero no desde esas rutas y no lanzado por `msiexec`. Falsos positivos conocidos: instaladores empaquetados con AutoIt, exceptuables por firma y ruta.

**H-2 — `msiexec` ejecutando un MSI descargado del correo o de Internet.** Creación de `msiexec.exe` con un argumento que apunte a `%TEMP%`, a la carpeta de descargas o a `C:\ProgramData\`, especialmente si su proceso padre es un navegador, un cliente de correo o un intérprete de script. Fuente: creación de procesos con línea de comandos. **El MSI es el vehículo en cuatro de las cinco campañas que alertó el CSIRT chileno.** Fidelidad alta; requiere exceptuar el despliegue legítimo de software por identidad de la herramienta de distribución, nunca por patrón de ruta.

**H-3 — Herramienta de administración remota instalada sin cambio aprobado.** Presencia o instalación de PDQ Connect y equivalentes —agentes de administración y soporte remoto— cruzada contra el registro de cambios. Fuente: inventario de software, creación de servicios, eventos de instalación de MSI. **Es la técnica de la campaña chilena de febrero de 2025, y el software es legítimo y firmado:** ninguna herramienta de seguridad la va a marcar. Fidelidad extremadamente alta porque el criterio es administrativo y no técnico: lo que delata es la ausencia de ticket.

**H-4 — Navegador sin interfaz con perfil clonado.** Creación de carpetas que casen `C:\Users\Public\Temp\ChromeAuto_*`; ejecución de Chrome, Edge o Chromium con `--headless` y `--excludeSwitches` desde un perfil que no es el del usuario; escucha de un puerto local en el rango 31175–39999; descarga de `chromedriver` o `msedgedriver` por PowerShell. Fuente: creación de procesos, creación de ficheros, puertos en escucha. **Es la firma del gusano de WhatsApp.** Fidelidad muy alta; prácticamente no tiene equivalente legítimo en una estación de trabajo corporativa.

**H-5 — Descarga de la biblioteca de automatización de WhatsApp.** Peticiones a `github.com/wppconnect-team` o a los CDN que sirven `WA-JS`, originadas por un proceso que no es un navegador en uso interactivo. Fuente: proxy con atribución de proceso. Fidelidad alta; la biblioteca es legítima y de uso comercial, de modo que la señal está en quién la pide y desde dónde.

**H-6 — Ficheros de marca de Mekotio en el perfil del usuario.** Presencia de `Bizarro.txt`, `V.txt`, `Ok.txt`, `Etc`, `<nombre>.jkl` o `<nombre>.exe.jpg` en la raíz del perfil de usuario. Fuente: inventario de ficheros, auditoría de integridad. ESET advierte que **la mayoría no coexisten, de modo que encontrar uno ya es motivo de sospecha**. Fidelidad extremadamente alta y coste de implementación casi nulo; advertencia obligada: son triviales de cambiar y llevan seis años publicados.

**H-7 — Persistencia apuntando a un intérprete de script.** Claves de ejecución automática o accesos directos en la carpeta de Inicio cuyo destino sea `AutoIt3.exe`, `wscript.exe`, `cscript.exe`, `mshta.exe` o un ejecutable en `C:\ProgramData\<aleatorio>\`. Fuente: inventario de arranque automático, eventos de registro. Fidelidad alta; es el mecanismo que ESET documenta en 2020 y que sigue vigente.

**H-8 — Ventana superpuesta sobre el navegador en sitios de banca.** Creación de ventana de nivel superior sin decoración, a pantalla completa o posicionada sobre la ventana del navegador, mientras el navegador tiene cargado un dominio de banca. Fuente: telemetría de interfaz del EDR, si existe. **Es la técnica característica de la familia y la más difícil de detectar con herramientas estándar;** se incluye porque, donde el EDR la soporte, es el indicio más específico que existe. Fidelidad alta, cobertura baja.

**H-9 — Sustitución de portapapeles con patrón de dirección de criptomonedas.** Proceso que no es un gestor de portapapeles escribiendo en él un valor que case con el formato de una dirección de Bitcoin o Ethereum, poco después de una lectura. Fuente: telemetría de portapapeles del EDR. Fidelidad alta donde esté disponible; cobertura dependiente del producto.

**H-10 — Lectura de las bases de contraseñas del navegador por un proceso ajeno.** Acceso a `Login Data`, `Cookies` o `Local State` de perfiles de Chromium, o copia de esos ficheros a `%TEMP%`, por un proceso que no es el navegador. Añadir la señal específica de esta familia: **presencia de `SQLite3.dll` junto a un ejecutable en una carpeta de usuario**. Fuente: auditoría de acceso a ficheros. Fidelidad alta.

**H-11 — C2 en puerto no estándar y dirección tomada de un documento público.** Conexiones salientes a puertos como 9091, 7957 o 57496 desde estaciones de trabajo; y, como señal complementaria, acceso a documentos públicos de servicios de ofimática en la nube por procesos que no son navegadores, que es cómo estas familias resuelven su C2. Fuente: cortafuegos, proxy, EDR. Fidelidad media; el segundo indicio es inusual y vale la pena por su especificidad.

**H-12 — Correo que suplanta a institución chilena con adjunto o enlace de descarga.** Mensajes cuyo remitente o cuerpo invoque `SII`, `Servicio de Impuestos Internos`, `boleta electrónica`, `factura impaga`, `Tesorería General`, `devolución de impuestos`, `CGE`, `Compañía General de Electricidad`, `corte de suministro`, `Ministerio de Energía`, combinados con adjunto `.zip`, `.msi`, `.hta`, `.url` o enlace a dominio recién registrado. **Cargar además los indicadores de las cinco alertas del CSIRT**, que están en el Anexo A y que hoy no están en nuestras listas. Fuente: pasarela de correo. Fidelidad alta; es la hipótesis que corresponde directamente a la evidencia nacional.

**H-13 — Dominio que suplante nuestra propia marca en contexto de facturación.** Registro de dominios que combinen nuestro nombre con términos de facturación, pago, boleta o notificación. Fuente: vigilancia de registro de dominios, que `CTI-2026-018` ya describe. Fidelidad alta; cubre la mitad reputacional de KJ-7 y conecta con el trabajo del informe de abuso de TLD.

**H-14 — Adjunto comprimido recibido por WhatsApp en equipo corporativo.** Ficheros `.zip` escritos por el proceso de WhatsApp Web o por el navegador desde `web.whatsapp.com`, especialmente con nombre que siga el patrón `m_<número>_NUMERO_`. Fuente: creación de ficheros, proxy. Fidelidad media-alta; depende de que WhatsApp Web esté permitido, y si no lo está, la propia detección sobra.

## T-5. Brechas de visibilidad que hay que cerrar primero

| Brecha | Por qué importa aquí |
|---|---|
| Registro de línea de comandos en creación de procesos deshabilitado | Deja ciegas `H-1`, `H-2`, `H-4` y `H-7`, es decir las cuatro hipótesis que cubren la etapa 02 completa. Es un ajuste de directiva |
| Indicadores del CSIRT Nacional no ingeridos en el SIEM | Deja sin usar la única inteligencia específicamente chilena y gratuita que existe sobre esta amenaza, y es la brecha más fácil de cerrar de todo el informe |
| Inventario de software sin cruce con el registro de cambios | Deja ciega `H-3`, cuyo criterio de detección es administrativo y no técnico |
| Sin telemetría de interfaz gráfica en el EDR | Deja ciega `H-8`, la detección más específica de la técnica característica de la familia |
| Sin telemetría de portapapeles | Deja ciega `H-9` y con ella el vector de robo que no necesita credenciales |
| Proxy sin atribución de proceso | Degrada `H-5` y `H-11` a listas de servicios legítimos, inservibles para alertar |
| Correo sin registro de tipo de adjunto ni retención de 90 días | Deja ciega `H-12`, la hipótesis alineada con la evidencia nacional |
| Sin inventario de equipos con sesión de WhatsApp Web | No podemos dimensionar la exposición al canal de KJ-3 ni priorizar la decisión E-d |

---

# NIVEL TÉCNICO
### Para: Ingeniería de detección · Automatización · TIP/SIEM · Vida útil: semanas–meses

## X-1. Arsenal y capacidad del ecosistema

| Propiedad | Valor |
|---|---|
| Lenguajes de implante | Delphi en `Mekotio`, `Mispadu`, `Grandoreiro` y el núcleo de `Astaroth`; .NET más Nim en `Coyote`; **Rust nativo en `VENON`**; PowerShell y después Python en `Vareg` |
| Biblioteca de cifrado compartida | `DelphiEncryptionCompendium`, de código abierto, usada por el núcleo de Astaroth y por su *spambot*. Es uno de los lazos técnicos del ecosistema |
| Ejecutores legítimos | Intérprete oficial de AutoIt, `msiexec`, `rundll32`, PowerShell, WMI, `wscript`; `CasPol.exe` como objetivo de carga lateral en `VENON` |
| Bibliotecas legítimas incorporadas | `SQLite3.dll` para leer las bases de contraseñas; `WPPConnect/WA-JS` para automatizar WhatsApp; controladores de Selenium; `WixSharp.dll`; `libcef.dll` como vehículo de carga lateral |
| Software comercial abusado | **PDQ Connect**, agente de administración remota firmado digitalmente y con cero detecciones en el momento de la campaña chilena |
| Criptografía de la cadena | AES-CBC con robo de cifrado (CTS) y HMAC-SHA256 con clave `TenHaVunf!@#2026` en el *spambot*; **Argon2id (m=19456 KiB, t=2, p=1) más XChaCha20-Poly1305** en la configuración de `VENON`; XOR con clave por bloque; base64 invertido |
| Resolución del C2 | **Dirección obtenida de un documento público** que el atacante actualiza (Mekotio, 2020); depósito en la nube pública (`VENON`); dominios de DNS dinámico en las familias más antiguas |
| Transporte del C2 | HTTP en claro en las familias antiguas, con formato de comando `<\|comando\|>`; **WebSocket sobre TLS 1.3 con ChaCha20-Poly1305** en `VENON`, lo que impide la inspección pasiva sin la clave de sesión |
| Puertos no estándar observados | 9091, 7957, 57496, y en `VENON` el rango local 31175–39999 para el controlador del navegador |
| Evasión de análisis | Anti-máquina virtual por nombre de proceso, `IsDebuggerPresent`, ocultación del hilo frente al depurador, comportamiento según idioma del sistema, ocultación en el Administrador de tareas, autodestrucción, búsqueda de productos de seguridad, desactivación del registro de eventos |
| Evasión avanzada (solo `VENON`) | Elusión de AMSI y de ETW, sobrescritura de la sección de código de `ntdll` con una copia limpia leída de disco, llamadas al sistema indirectas, lista de control de acceso sobre su propio proceso, y `SetWindowDisplayAffinity` para que las capturas de pantalla de sus ventanas salgan en negro |
| Robo de credenciales | Navegadores Chromium y Opera, gestor de credenciales de Windows, Outlook, Thunderbird, claves Wi-Fi; en variantes recientes, evasión del cifrado vinculado a aplicación de Chrome |
| Desvío de fondos | Sustitución de direcciones de criptomonedas en el portapapeles; interceptación de QR de Pix y sustitución de *boleto* (`VENON`) |
| Objetivos declarados | **24 bancos chilenos** y 27 brasileños en Mekotio; más de 1.700 entidades en Grandoreiro; 33 objetivos en `VENON` entre banca, fintech, la Receita Federal, nueve casas de cambio y seis monederos de criptomonedas |
| Lo que **no** tiene | Cifrador de extorsión, capacidad destructiva documentada, explotación de días cero, actividad en entornos industriales, movimiento lateral clásico en red |

<!-- cti:note type="info" -->

> **Lo que este cuadro dice de la defensa.** Hay dos niveles tecnológicos conviviendo. Las
> cuatro familias clásicas son **ruidosas y detectables**: Delphi, AutoIt, HTTP en claro,
> ficheros de marca en el perfil del usuario. `VENON` es otra cosa: Rust, criptografía
> moderna, elusión de AMSI y ETW, llamadas indirectas al sistema y C2 que no se puede
> inspeccionar pasivamente. **Si la hipótesis de la reescritura asistida por IA se
> confirmara, el segundo nivel dejaría de ser la excepción**, y las detecciones de §X-3 que
> dependen de artefactos de implementación —`H-6`, `H-7`— perderían valor antes que las que
> dependen del canal y del comportamiento.

## X-2. Artefactos persistentes entre versiones

<!-- cti:cards -->

| Categoría | Artefactos | Etiqueta |
|---|---|---|
| Ficheros de marca de Mekotio | `Bizarro.txt` · `V.txt` · `Ok.txt` · `Etc` · `<intérprete>.jkl` · `<intérprete>.exe.jpg`, todos en la raíz del perfil del usuario. ESET advierte que **la mayoría no coexisten**, de modo que encontrar uno ya es sospechoso | `host` |
| Cadena de ejecución de Mekotio | Carpeta `C:\programdata\<nombre aleatorio>\` con cuatro ficheros: intérprete de AutoIt, script `.au3`, DLL del implante y `SQLite3.dll` | `host` |
| Gusano de WhatsApp | Carpeta `C:\Users\Public\Temp\ChromeAuto_<BROWSER_ID><FECHA>` · puerto local en 31175–39999 · elementos comprobados en la página: `new-chat-outline`, `settings-refreshed`, `chat` · patrón de nombre de adjunto `m_<número>_NUMERO_` | `WhatsApp` |
| Configuración del *spambot* | Palabra mágica `EF01` · clave HMAC `TenHaVunf!@#2026` · claves de configuración `ENA`, `FCX`, `LT`, `HL`, `PFX`, `DEL`, `ArrMSG`, `ArrMF`, `ArrURL` | `configuración` |
| Nombres de función del *spambot* | `BaixarWAJS` · `ProcessarEnvio` · `ProcessarContatos` · `LoadConfigs` · `WebDriverUpdater` · `Cleanup` · `enviarParaContato` · `mensagemSaudacao` | `código` |
| Artefactos de `VENON` | Exportado `VAI` ausente; tarea `NVIDIA Notification Service` · carpeta `C:\ProgramData\USOShared\NuPLihaOH\` · implante `®mjtgr.exe` (con prefijo U+00AE) · `libcef.dll` malicioso · contraseña de derivación `L0@D_S3CR3T_K3Y_X9F2_PR0D_2024!` y sal `LOAD_SALT_2024!!` | `VENON` |
| Formato de C2 clásico | Mensajes con el formato `<\|comando\|>`; ejemplos observados: `<\|vhxboj\|>`, `<\|WGSGTNU\|>`, `<\|tksN\|>`, `<\|VOTM\|>`, `<\|LSTU\|>` | `red` |
| Ficheros con nombre de biblioteca | `shfolder.dll` · `ssleay32.dll` · `libeay32.dll` · `5nkdggch.dll`, usados para aparentar componentes legítimos | `enmascaramiento` |
| Nombres de fichero de las campañas chilenas | `nopagadafacSiimarzo.zip/.msi` · `Siifactmarzo.zip` · `nopagadafacturaSii.zip` · `factnuevamarzocgeboletaeletricidad.zip/.msi` · `DevolucionImpuestopiendenteTGR_16081.zip` · `FacturaContabilSolutionsDiciembre.msi` · `Informe-21-2024.zip` · `Informe-Detallado.msi` | `Chile` |

## X-3. Lógica de detección prioritaria

<!-- cti:detections -->

**D-1 · CRÍTICO — Intérprete de AutoIt desde ruta escribible por el usuario**

```
(process.original_file_name == "AutoIt3.exe" OR process.name MATCHES "(?i)autoit")
AND process.executable MATCHES "(?i)\\\\(Users|ProgramData|Temp|AppData)\\\\"
AND NOT process.code_signature.subject IN (<instaladores aprobados que empaquetan AutoIt>)
```

→ Contención automática: aislar el equipo y preservar la carpeta de ejecución. Es el ejecutor del implante en la cadena documentada desde 2019 y sigue vigente en 2026.

**D-2 · CRÍTICO — `msiexec` instalando un MSI llegado de Internet o del correo**

```
process.name == "msiexec.exe"
AND process.command_line MATCHES "(?i)\\\\(Downloads|Temp|AppData|ProgramData)\\\\.*\.msi"
AND parent_process.name IN ("chrome.exe","msedge.exe","firefox.exe","outlook.exe",
                            "wscript.exe","cscript.exe","powershell.exe","explorer.exe")
```

→ Contención automática en estaciones de trabajo. El MSI es el vehículo en cuatro de las cinco campañas alertadas por el CSIRT Nacional. Exceptuar la herramienta corporativa de distribución de software **por identidad, no por ruta**.

**D-3 · CRÍTICO — Agente de administración remota instalado sin cambio aprobado**

```
(service.name MATCHES "(?i)(pdq|connectwise|anydesk|teamviewer|screenconnect|atera|splashtop)"
 OR file.name MATCHES "(?i)pdq-connect-agent|pdq-connect-updater")
AND NOT host.id IN (<equipos con ticket de cambio vigente>)
```

→ Contención automática: desinstalar, aislar y abrir incidente. La campaña chilena de feb-2025 entregó el implante por esta vía con software **firmado y sin detecciones**. El criterio es administrativo: lo que delata es la ausencia de ticket.

**D-4 · CRÍTICO — Navegador sin interfaz con perfil clonado (gusano de WhatsApp)**

```
file.directory MATCHES "(?i)C:\\\\Users\\\\Public\\\\Temp\\\\ChromeAuto_"
OR (process.name IN ("chrome.exe","msedge.exe","chromedriver.exe","msedgedriver.exe")
    AND process.command_line CONTAINS_ANY ("--headless", "excludeSwitches", "enable-automation")
    AND process.command_line MATCHES "(?i)user-data-dir=.*(Public|Temp)")
```

→ Contención automática: aislar el equipo, cerrar las sesiones de WhatsApp Web del usuario y avisar a sus contactos corporativos. **Si esta regla se dispara, el equipo ya está escribiendo a la agenda de la víctima.**

**D-5 · ALTO — Persistencia apuntando a un intérprete de script**

```
(registry.path MATCHES "(?i)\\\\CurrentVersion\\\\Run"
 OR file.path MATCHES "(?i)\\\\Start Menu\\\\Programs\\\\Startup\\\\")
AND registry.value MATCHES "(?i)(AutoIt3|wscript|cscript|mshta|\.au3|\.vbs|\.js)$"
```

→ Aislar y eliminar la persistencia tras preservar el fichero. Es el mecanismo que ESET documentó en 2020 y que las alertas chilenas siguen reflejando.

**D-6 · ALTO — Ficheros de marca de Mekotio en el perfil del usuario**

```
file.path MATCHES "(?i)C:\\\\Users\\\\[^\\\\]+\\\\(Bizarro\.txt|V\.txt|Ok\.txt|Etc)$"
OR file.name MATCHES "(?i)\.(jkl|exe\.jpg)$"
```

→ Investigación inmediata. Coste de implementación nulo y fidelidad altísima. **Advertencia: publicados en 2020 y triviales de cambiar.** Red de seguridad barata, no estrategia.

**D-7 · ALTO — `SQLite3.dll` acompañando a un ejecutable en carpeta de usuario**

```
file.name == "SQLite3.dll"
AND file.directory MATCHES "(?i)\\\\(Users|ProgramData|Temp|AppData)\\\\"
AND NOT file.directory IN (<rutas de aplicaciones aprobadas>)
```

→ Investigar el contenido completo de la carpeta. Es el componente que estas familias llevan para leer las bases de contraseñas del navegador, y su presencia en una carpeta de usuario junto a un ejecutable es la firma de la cadena de cuatro ficheros.

**D-8 · ALTO — Descarga del controlador de Selenium o de la biblioteca de WhatsApp**

```
(process.name == "powershell.exe" AND process.command_line MATCHES "(?i)(chromedriver|msedgedriver|googlechromelabs|msedgedriver\.azureedge)")
OR (url.full MATCHES "(?i)github\.com/wppconnect-team" AND process.name NOT IN (<navegadores en uso interactivo>))
```

→ Bloquear y triar el equipo. Ambos componentes son legítimos; la señal está en el proceso que los solicita.

**D-9 · MEDIO — Acceso no autorizado a las bases de contraseñas del navegador**

```
file.path MATCHES "(?i)\\\\(User Data|Profile [0-9]+)\\\\(Login Data|Cookies|Local State)$"
AND process.name NOT IN (<navegadores aprobados>)
```

→ Aislar y forzar rotación de credenciales del usuario, incluidas las corporativas que tuviera guardadas.

**D-10 · MEDIO — Sustitución de portapapeles con formato de dirección de criptomonedas**

```
clipboard.write.value MATCHES "^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,62}$|^0x[a-fA-F0-9]{40}$"
AND process.name NOT IN (<gestores de portapapeles y navegadores aprobados>)
AND time_since(clipboard.read) < 2s
```

→ Alerta de severidad alta y aviso inmediato al usuario. Cubre el vector de desvío que no necesita robar ninguna credencial.

**D-11 · MEDIO — C2 en puerto no estándar desde estación de trabajo**

```
host.role == "workstation"
AND destination.port IN (9091, 7957, 57496)
AND NOT destination.ip IN (<rangos internos y de proveedores aprobados>)
```

→ Bloquear y triar. Son los puertos de las alertas chilenas; conviene ampliar la regla a «puerto alto no estándar hacia destino externo con proceso no reconocido», que envejece mejor que una lista.

**D-12 · MEDIO — Correo que suplanta a institución chilena con adjunto ejecutable**

```
email.direction == "inbound"
AND (email.subject CONTAINS_ANY ("SII","Impuestos Internos","boleta electrónica",
                                  "factura impaga","Tesorería General","devolución de impuestos",
                                  "CGE","Compañía General de Electricidad","Ministerio de Energía")
     OR email.body CONTAINS_ANY (<mismos términos>))
AND email.attachment.extension IN ("msi","zip","hta","url","js","vbs","cmd")
```

→ Cuarentena y notificación al usuario con el procedimiento de verificación de la decisión E-c. Cargar además los indicadores del Anexo A, que provienen de las cinco alertas del CSIRT Nacional.

<!-- cti:note type="warn" -->

> ⚠ **Regla de operación.** D-1 a D-4 deben ejecutar **contención automática**, y aquí el
> motivo es distinto al de los informes anteriores de esta serie: no es la velocidad del
> adversario, es que **el producto del compromiso es credencial y dinero**, y ambos salen en
> la primera sesión de navegación. En D-4 la contención tiene además un componente que no
> es técnico: hay que avisar a los contactos de la víctima, porque el equipo ya les ha
> escrito en su nombre. Ese paso debe estar en el procedimiento antes de activar la regla.

<!-- cti:note type="gap" -->

> ⬛ **Estado de este material.** Las doce reglas son **plantillas en pseudocódigo**, con
> nombres de campo que deben traducirse al esquema real de nuestro SIEM y de nuestro EDR.
> D-10 depende de telemetría de portapapeles y D-4 de telemetría de ficheros y de línea de
> comandos: si no las tenemos, la regla no es implementable y el hallazgo es la brecha, no
> la detección.

## X-4. Consultas de caza

```kql
// H-1 · Intérprete de AutoIt desde ruta escribible por el usuario
DeviceProcessEvents
| where Timestamp > ago(90d)
| where ProcessVersionInfoOriginalFileName =~ "AutoIt3.exe"
      or FileName matches regex @"(?i)autoit"
| where FolderPath matches regex @"(?i)\\(Users|ProgramData|Temp|AppData)\\"
| project Timestamp, DeviceName, AccountName, FolderPath, ProcessCommandLine,
          InitiatingProcessFileName, InitiatingProcessCommandLine
| order by Timestamp desc
```

```kql
// H-2 · msiexec instalando un MSI traído de Internet o del correo
DeviceProcessEvents
| where Timestamp > ago(90d)
| where FileName =~ "msiexec.exe"
| where ProcessCommandLine matches regex @"(?i)\\(Downloads|Temp|AppData|ProgramData)\\.*\.msi"
| where InitiatingProcessFileName in~ ("chrome.exe","msedge.exe","firefox.exe","outlook.exe",
                                       "wscript.exe","cscript.exe","powershell.exe","explorer.exe")
| project Timestamp, DeviceName, AccountName, InitiatingProcessFileName, ProcessCommandLine
| order by Timestamp desc
```

```kql
// H-4 · Gusano de WhatsApp: perfil de navegador clonado y navegador sin interfaz
let carpetas = DeviceFileEvents
    | where Timestamp > ago(90d)
    | where FolderPath matches regex @"(?i)C:\\Users\\Public\\Temp\\ChromeAuto_"
    | project Timestamp, DeviceName, FolderPath, Señal = "perfil clonado";
let navegador = DeviceProcessEvents
    | where Timestamp > ago(90d)
    | where ProcessCommandLine has_any ("--headless", "excludeSwitches", "enable-automation")
    | where ProcessCommandLine matches regex @"(?i)user-data-dir=.*(Public|Temp)"
    | project Timestamp, DeviceName, FolderPath = ProcessCommandLine, Señal = "navegador oculto";
union carpetas, navegador
| summarize Señales = make_set(Señal), Eventos = count() by DeviceName, bin(Timestamp, 1h)
| where array_length(Señales) > 0
| order by Eventos desc
```

```kql
// H-6 + H-7 · Ficheros de marca de Mekotio y persistencia hacia intérprete
let marcas = dynamic(["Bizarro.txt","V.txt","Ok.txt","Etc"]);
DeviceFileEvents
| where Timestamp > ago(90d)
| where (FileName in~ (marcas) and FolderPath matches regex @"(?i)C:\\Users\\[^\\]+\\[^\\]+$")
      or FileName matches regex @"(?i)\.(jkl|exe\.jpg)$"
| project Timestamp, DeviceName, FolderPath, FileName, InitiatingProcessFileName
| order by Timestamp desc
```

```kql
// H-12 · Correo que suplanta a institución chilena con adjunto ejecutable
let terminos = dynamic(["sii","impuestos internos","boleta electronica","boleta electrónica",
                        "factura impaga","factura pendiente","tesoreria general","tesorería general",
                        "devolucion de impuestos","devolución de impuestos","cge",
                        "compañia general de electricidad","ministerio de energia","apagon","apagón"]);
let extensiones = dynamic(["msi","zip","hta","url","js","vbs","cmd"]);
EmailEvents
| where Timestamp > ago(90d) and EmailDirection == "Inbound"
| where Subject has_any (terminos)
| join kind=leftouter (
    EmailAttachmentInfo
    | where Timestamp > ago(90d)
    | project NetworkMessageId, FileName, FileType
  ) on NetworkMessageId
| where FileType in~ (extensiones) or isempty(FileType)
| project Timestamp, SenderFromAddress, SenderFromDomain, RecipientEmailAddress,
          Subject, FileName, FileType, DeliveryAction
| order by Timestamp desc
```

```yaml
# Sigma — Intérprete de AutoIt ejecutado desde ruta escribible por el usuario
# Autor: Célula CTI · Fecha: 2026-11-16 · ATT&CK: T1588.002, T1059
# Nivel: high · Estado: experimental
# Falsos positivos conocidos: instaladores comerciales empaquetados con AutoIt
# (exceptuar por firma digital y por ruta de instalación aprobada).
title: Interprete AutoIt desde ruta de usuario
id: 2d9f6c41-BRBK-CTI-2026-021
status: experimental
logsource:
  category: process_creation
  product: windows
detection:
  autoit:
    - OriginalFileName: 'AutoIt3.exe'
    - Image|endswith:
        - '\AutoIt3.exe'
        - '\autoit3.exe'
  ruta_usuario:
    Image|contains:
      - '\Users\'
      - '\ProgramData\'
      - '\AppData\'
      - '\Temp\'
  condition: autoit and ruta_usuario
fields:
  - Image
  - CommandLine
  - ParentImage
  - ParentCommandLine
  - User
level: high
```

```yaml
# Sigma — Perfil de navegador clonado en Public\Temp (gusano de WhatsApp de Astaroth)
# Autor: Célula CTI · Fecha: 2026-11-16 · ATT&CK: T1534, T1564.003
# Nivel: critical · Estado: experimental
# Basada en el patron de carpeta publicado por CrowdStrike el 2026-07-29.
title: Perfil de navegador clonado para automatizar WhatsApp Web
id: 7a3e85b2-BRBK-CTI-2026-021
status: experimental
logsource:
  category: file_event
  product: windows
detection:
  carpeta:
    TargetFilename|contains: '\Users\Public\Temp\ChromeAuto_'
  condition: carpeta
fields:
  - TargetFilename
  - Image
  - User
level: critical
```

## X-5. Mitigaciones de configuración con efecto directo

| Control | Corta |
|---|---|
| Bloqueo de ejecución de `.msi` no originado por la herramienta corporativa de distribución | El vehículo de entrega de cuatro de las cinco campañas alertadas por el CSIRT Nacional |
| Lista de permitidos de aplicaciones que excluya el intérprete de AutoIt desde rutas de usuario | El ejecutor del implante en la cadena documentada desde 2019 (`T1588.002`) |
| Bloqueo de adjuntos `.msi`, `.hta`, `.url`, `.js`, `.vbs`, `.cmd` y comprimidos con contraseña | La etapa 01 completa en su variante de adjunto (`T1566.001`) |
| Prohibición de instalar herramientas de administración remota sin cambio aprobado, con detección de las ya presentes | La vía de entrega de la campaña chilena de feb-2025, que usa software firmado y sin detecciones |
| Gestor de contraseñas del navegador deshabilitado por directiva para credenciales corporativas | El segundo mecanismo de captura, que no requiere ninguna ventana falsa (`T1555.003`) |
| Reglas de reducción de superficie de ataque que bloqueen la creación de procesos hijo por scripts y por Office | La transición de la etapa 01 a la etapa 02 |
| Bloqueo de WhatsApp Web en equipos corporativos, o detección de navegador sin interfaz y de clonado de perfil | El canal de propagación de KJ-3, sobre el que hoy no hay ningún control |
| Protección contra manipulación de Defender activada y gestionada centralmente | Las exclusiones de carpeta y la desactivación del antivirus (`T1562.001`) |
| Registro de línea de comandos y de creación de procesos con 90 días de retención | No corta nada: **habilita** D-1, D-2, D-4, D-5 y las hipótesis `H-1`, `H-2`, `H-4`, `H-7` |
| Ingesta de las alertas del CSIRT Nacional en el SIEM y en la plataforma de inteligencia | No corta nada: incorpora la única inteligencia específicamente chilena que existe sobre esta amenaza |
| Doble autorización y verificación fuera de banda en el flujo de pagos | **La pérdida**, incluso si el compromiso del equipo tiene éxito. Es el único control de esta tabla que no depende de seguridad informática |

---

## 14. Brechas de inteligencia y nuevos requisitos de colección

| # | Brecha | Impacto en el juicio | Requisito propuesto | Prioridad |
|---|---|---|---|---|
| G-1 | Sin telemetría propia | §O-4 vacía; las doce reglas de §X-3 sin calibrar; no sabemos si ya nos alcanzó | Ejecutar el cuestionario X-1 a X-11 de §O-4, empezando por X-1, X-2 y X-4, que se responden en una tarde | Crítica |
| G-2 | Los indicadores del CSIRT Nacional no están en nuestro SIEM | Inteligencia nacional, gratuita y específica, sin usar. Es la brecha más barata de cerrar del informe | Suscripción formal al canal de alertas e ingesta automatizada de sus indicadores (decisión E-e) | Crítica |
| G-3 | Sin medición reciente de la cuota chilena de esta familia | KJ-1 se apoya en datos de 2019 y 2020 y debe advertirlo cada vez que se cite | Consulta al CSIRT Nacional sobre volumen de reportes asociados a la familia en 2025-2026; participación en el canal sectorial | Alta |
| G-4 | Sin visibilidad sobre el canal de WhatsApp | KJ-3, el juicio más consecuente, descansa en una proyección nuestra sobre un filtro de código | Vigilancia específica del indicador `I-1`; inventario de equipos con WhatsApp Web (X-5) | Alta |
| G-5 | La hipótesis de reescritura asistida por IA de `VENON` proviene de una fuente única y sin nivel de confianza asignado | KJ-6 no es accionable; si se confirma, cambia la vida útil de media docena de nuestras detecciones | Vigilar corroboración independiente; añadir `VENON` al plan de colección permanente | Media |
| G-6 | No se leyeron los PDF adjuntos a las alertas del CSIRT | El marcado interno de esos documentos no está verificado, y pueden contener detalle técnico que el portal resume | Descargar y revisar los cinco PDF; si alguno lleva marcado restrictivo, retirar de este informe lo que provenga de él | Media |
| G-7 | Las cifras de volumen de la campaña chilena provienen del panel del atacante | El dato de 106 instalaciones no es telemetría defensiva y no debe citarse como tal | Buscar corroboración en fuentes nacionales; preguntar al CSIRT si recibió reportes asociados | Media |
| G-8 | Sin vigilancia de suplantación de nuestra propia marca | La mitad reputacional de KJ-7 queda sin evaluar, y es la mitad que no controla seguridad | Encargo a Asuntos Corporativos con procedimiento de denuncia (decisión E-f) | Media |
| G-9 | Sin seguimiento del mercado brasileño de cargadores y criptadores como servicio | Los saltos de capacidad de este ecosistema llegan del mercado, no del taller; no vigilarlo es no ver venir el siguiente | Añadir `SORVEPOTEL`, `Caminho`, `Vareg` y los criptadores por suscripción al plan de colección | Media |
| G-10 | Sin evaluación del flujo de pagos frente a este escenario | La decisión E-h, que es la única que corta la pérdida, no se puede priorizar sin saber qué controles existen | Revisión conjunta con Prevención de Fraude y Tesorería | Alta |

---

# ANEXOS

## Anexo A — Indicadores de compromiso

<!-- cti:note type="warn" -->

> ⚠ **Leer antes de usar.** La mayor parte de esta lista proviene de las cinco alertas del
> **CSIRT Nacional de Chile**, lo que la hace la más pertinente de esta serie y también la
> que exige más cuidado por tres motivos. Primero, **buena parte de los dominios son sitios
> legítimos comprometidos** usados como contenedor o redirección: bloquearlos castiga a un
> tercero inocente y conviene tratarlos como detección, no como bloqueo. Segundo, las
> alertas del CSIRT **listan ficheros de software legítimo** —el agente de PDQ Connect,
> `WixSharp.dll`— sin explicar el abuso; están marcados abajo y **no deben bloquearse**.
> Tercero, ESET advierte desde 2020 que los *hashes* de esta familia son de vida corta: su
> valor es de retrohunt. Lo que previene está en §T-4 y §X-3.

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Acción permitida |
|---|---|---|---|---|
| sha256 | `203d8a6e596cad036eae854e7484509a11ee35547ca5e1f2b2249ae825ec714f` | `nopagadafacSiimarzo.zip` — campaña que suplanta al SII (CSIRT `2CMV23-00417-01`) | Alta | Bloqueo y retrohunt |
| sha256 | `3d5f0dbce1204d0db72b9574800bef878015fdbbe7b24dc5b553caed5da4dc5a` | MSI de la campaña del SII, **el mismo hash servido con tres nombres distintos** (CSIRT `2CMV23-00417-01`) | Alta | Bloqueo y retrohunt |
| sha256 | `6d2f67ddd2438baa14e2565e02e015296db31daf3d03410e7c783e89c785e614` | `Siifactmarzo.zip` — campaña del SII (CSIRT `2CMV23-00417-01`) | Alta | Bloqueo y retrohunt |
| sha256 | `f178861e00b0a2ba7d50c103ac41ac6eb89e7c6232bd25bd1fa8752a8871e445` | `nopagadafacturaSii.zip` — campaña del SII (CSIRT `2CMV23-00417-01`) | Alta | Bloqueo y retrohunt |
| sha256 | `e87329c39e9647d1f4bd64400a2988f9c83b3547845c998ae6bfbcb361d6240c` | `Informe-21-2024.zip` — campaña del SII por boletas electrónicas (CSIRT `CMV24-00463`) | Alta | Bloqueo y retrohunt |
| sha256 | `d12f56009bcdf27276235380343948f1f909cf17c1490c5c91ec2c2a8cffc699` | `Informe-Detallado.msi` — misma campaña (CSIRT `CMV24-00463`) | Alta | Bloqueo y retrohunt |
| sha256 | `7e643c188a1ee3b0251b7dfcab000b7c48fd840eff35189e8a45901852e3910a` | `ssleay32.dll` — **aparece en dos campañas chilenas distintas**, SII y CGE: es el componente reutilizado (CSIRT `CMV24-00463` y `CMV24-00455`) | Alta | Bloqueo y retrohunt |
| sha256 | `e28e34fbdaff077669586dcdb4e10f0ba2ca6c9973ed4d372a5c3ec3b8ad20e7` | `libeay32.dll` — también en ambas campañas (CSIRT `CMV24-00463` y `CMV24-00455`) | Alta | Bloqueo y retrohunt |
| sha256 | `19ef6dcc8257fc55032aa97eb5613a8dc35cfd41bf4804d239ee349d03b7129c` | `factnuevamarzocgeboletaeletricidad.zip` — campaña que suplanta a la CGE (CSIRT `CMV24-00455`) | Alta | Bloqueo y retrohunt |
| sha256 | `5cc97524d9ab2d29019d545b06f8ef8fcf5b9fb8ee257d7352a619f8950f5449` | `factnuevamarzocgeboletaeletricidad.msi` — misma campaña (CSIRT `CMV24-00455`) | Alta | Bloqueo y retrohunt |
| sha256 | `dc626f8f3b32c1e751d02c3e881bdfdc701a8db9dcb11a424b68f69fd7c4ce5c` | `DevolucionImpuestopiendenteTGR_16081.zip` — campaña de la Tesorería General (CSIRT `CMV24-00483`) | Alta | Bloqueo y retrohunt |
| sha256 | `1e74435045984691a9d8bce58101b8e3509c1031142b8aedd8f81d1c67eedbd2` | `DevolucionImpuestopiendenteTGR_b1Gz5R2UBS.cmd` — misma campaña (CSIRT `CMV24-00483`) | Alta | Bloqueo y retrohunt |
| sha256 | `28225c5622637cdaed8342e14560e8de7b53dd6ba145d973643fc4b5bdd67b75` | Fichero sin nombre asignado en la alerta de la Tesorería General (CSIRT `CMV24-00483`) | Media | Retrohunt |
| sha256 | `3f9ee99d2336918d7a3df73df04115d14aebf029dacffcebedefadd88ec8c49b` | `FacturaContabilSolutionsDiciembre.msi` — campaña de factura impaga genérica (CSIRT `CMV25-00499`) | Alta | Bloqueo y retrohunt |
| sha256 | `dd2c7a676fa3497a3761e17aab18cbcf301e6e389f63469d61c0eeb849917db6` | `5nkdggch.dll` — misma campaña (CSIRT `CMV25-00499`) | Alta | Bloqueo y retrohunt |
| herramienta | `307215945683763731f3bdd61ada911367be4d25e02c8a158d6c314c16865d47` | `pdq-connect-agent.exe` — **software legítimo de administración remota**, listado por el CSIRT como indicador de la campaña. **NO BLOQUEAR por hash** | Alta | Solo detección; verificar contexto |
| herramienta | `8daa7bc4f2e938960186dfd65ee38cc8917361c90dc9cfef5f2ce83306691988` | `pdq-connect-updater.exe` — **software legítimo**, mismo caso | Alta | Solo detección; verificar contexto |
| herramienta | `101665452ebc6e400550380510e8db10a9ce2af1e458f928ca4b0188daeceb9d` | `PDQConnectUpdater-0.3.0.msi` — **software legítimo**, mismo caso | Alta | Solo detección; verificar contexto |
| sha256 | `caa9da1c55e33446eaeb783957e990847369423c7dd652f07a5c93bf1d786a66` | `WixSharp.dll` — **biblioteca legítima de construcción de instaladores**, mismo caso | Alta | Solo detección; verificar contexto |
| sha1 | `8b683c897ecc6fa6881d29f6c41c7c159d65fa62` | `OZIW6737LTREEE.exe` — campaña dirigida a Chile de ago-2019 (ESET) | Media | Retrohunt |
| sha256 | `4236f4d3626e61dc37d83cbd26597ee2ce1adcbfdb36bf101435d0d3e134b4ea` | `shfolder.dll` — misma campaña de 2019; **el informe lo publica bajo encabezado SHA1 pero su longitud corresponde a SHA-256** | Media | Retrohunt |
| sha256 | `c7c62303ee1a37fd7a6e2db9c590ba75c647bc4d22d7dca50cfa8879222ac9e1` | *Spambot* de Astaroth cifrado (CrowdStrike, jul-2026) | Alta | Bloqueo y retrohunt |
| sha256 | `d89105c4d567a95f674ed6eac538e32e288b658a4222a3d52e284a77782af4d5` | *Spambot* de Astaroth descifrado, PE Delphi de 32 bits compilado el 2026-02-13 | Alta | Bloqueo y retrohunt |
| sha256 | `ec43a17685e3a555c2eb5f0a2802e9e45d5a2a5d49a0803155acbd74d9ecdbd7` | Configuración cifrada del *spambot* | Alta | Bloqueo y retrohunt |
| sha256 | `6168d63fad22a4e5e45547ca6116ef68bb5173e17e25fd1714f7cc1e4f7b41e1` | Componente en Python de `Vareg`, cuyo desarrollador «probablemente usó IA» según CrowdStrike | Alta | Bloqueo y retrohunt |
| sha256 | `a1aa786e02fb9a37a71e0f76b052ab284ba877f2aaa2fb28f05d60487389976a` | Componente en PowerShell de `Vareg`, versión anterior a la reescritura | Alta | Bloqueo y retrohunt |
| sha256 | `c482286a7fdfb64d308c197a4deabcd773b8b62d9e74d1d08fcfd02568d75d72` | `libcef.dll` empaquetado de `VENON` (ZenoX, mar-2026) | Alta | Bloqueo y retrohunt |
| sha256 | `75d1a2560cf93c6a028aa3573febddaf713014d64b0e8904488111772e4cff49` | `libcef.dll` desempaquetado de `VENON` | Alta | Bloqueo y retrohunt |
| sha256 | `fd5d9effc1ef77a49b0720d2691bc144f513609760c22fa62bc1e8b84dedf879` | `Itau_swap_install.vbs` — script de secuestro de accesos directos de `VENON` | Alta | Bloqueo y retrohunt |
| sha256 | `8e1d354dccc3c689899dc4e75fdbdd0ab076ac457de7fb83645fb735a46ad4ea` | Variante de Mispadu que abusa de `CVE-2023-36025` (Unit 42, feb-2024) | Alta | Bloqueo y retrohunt |
| sha256 | `bc25f7836c273763827e1680856ec6d53bd73bbc4a03e9f743eddfc53cf68789` | Variante de Mispadu del mismo conglomerado (Unit 42) | Alta | Bloqueo y retrohunt |
| sha256 | `fb3995289bac897e881141e281c18c606a772a53356cc81caf38e5c6296641d4` | Variante de Mispadu del mismo conglomerado (Unit 42) | Alta | Bloqueo y retrohunt |
| sha256 | `46d20fa82c936c5784f86106838697ab79a1f6dc243ae6721b42f0da467eaf52` | Variante de Mispadu del mismo conglomerado (Unit 42) | Alta | Bloqueo y retrohunt |
| sha256 | `03bdae4d40d3eb2db3c12d27b76ee170c4813f616fec5257cf25a068c46ba15f` | Variante de Mispadu del mismo conglomerado (Unit 42) | Alta | Bloqueo y retrohunt |
| herramienta | `0adb9b817f1df7807576c2d7068dd931` | **Intérprete legítimo de AutoIt** usado en casi todas las campañas de Mispadu desde jun-2024 (Cofense). **NO BLOQUEAR por hash** | Alta | Solo detección; verificar ruta y padre |
| domain | `gscjgn[.]org` | Descarga del fichero, campaña del SII (CSIRT `2CMV23-00417-01`) | Alta | Bloqueo |
| domain | `cmg-technology[.]ro` | Contenedor de malware, campaña del SII. **Probable sitio legítimo comprometido** | Media | Detección; bloqueo con validación |
| domain | `anchoriaatrade[.]com` | Redirección, campaña de la CGE (CSIRT `CMV24-00455`) | Alta | Bloqueo |
| domain | `digitalmukesh[.]info` | Descarga del fichero, campaña de la CGE | Alta | Bloqueo |
| domain | `arconmat[.]org` | Falso formulario, campaña de la Tesorería General (CSIRT `CMV24-00483`) | Alta | Bloqueo |
| domain | `artin-services[.]com` | Descarga del fichero, campaña de la Tesorería General | Alta | Bloqueo |
| domain | `ebccarpentrydublin[.]com` | Redirección, campaña de la Tesorería General. **Probable sitio legítimo comprometido** | Media | Detección; bloqueo con validación |
| domain | `enviroecobusiness[.]ro` | Comprobación, campaña de la Tesorería General. **Probable sitio legítimo comprometido** | Media | Detección; bloqueo con validación |
| domain | `pexinxaria[.]com[.]br` | Sitio falso del SII, campaña `CMV24-00463` | Alta | Bloqueo |
| domain | `portalriosul[.]com[.]br` | Redirección, campaña `CMV24-00463` | Alta | Bloqueo |
| domain | `sii-mail[.]cl` | **Dominio que suplanta al SII**, usado como remitente (`Informe-N40351073@sii-mail[.]cl`) | Alta | Bloqueo |
| domain | `meridianeyecare[.]com` · `inovia[.]com[.]ao` · `greatcreekcanines[.]com` · `gptplan[.]ro` | Infraestructura de la campaña del Ministerio de Energía (CronUp, feb-2025). **Probables sitios legítimos comprometidos** | Media | Detección; bloqueo con validación |
| domain | `molejo[.]online` | C2 de la campaña del Ministerio de Energía, puerto 7957 | Alta | Bloqueo |
| domain | `stretar7[.]contabilfacil[.]sbs` · `graconxonjal[.]empresaeficiente[.]sbs` · `plansonval[.]impostosrapido[.]top` | C2 del instalador de Astaroth (CrowdStrike, jul-2026) | Alta | Bloqueo |
| domain | `varegjopeaks[.]com` | C2 del componente Python de `Vareg` | Alta | Bloqueo |
| domain | `docsmoonstudioclayworks[.]online` | C2 del componente PowerShell de `Vareg` | Alta | Bloqueo |
| domain | `brasilmotorsvs14[.]com` | C2 principal de `VENON` | Alta | Bloqueo |
| domain | `lazybearpottery[.]net` | C2 alternativo de `VENON` | Alta | Bloqueo |
| domain | `digitalmoineyp[.]com` · `portalhondihs[.]com` | Distribución de `VENON` | Alta | Bloqueo |
| domain | `pluginsafeguard[.]help` | Configuración de reserva de `VENON`; **no figura en su tabla de indicadores, solo en el cuerpo del informe** | Media | Detección |
| domain | `plinqok[.]com` · `trilivok[.]com` · `xalticainvest[.]com` · `moscovatech[.]com` | C2 de la variante de Mispadu de `CVE-2023-36025` (Unit 42) | Alta | Bloqueo |
| ipv4 | `103.235.105[.]113` | Página de descarga, campaña del SII de 2023 | Media | Solo retrohunt |
| ipv4 | `188.240.2[.]189` | Página contenedora, campaña del SII de 2023 | Media | Solo retrohunt |
| ipv4 | `50.116.72.199` · `158.69.109.191` · `162.214.157.170` | Infraestructura de correo, campaña del SII de 2023 | Media | Solo retrohunt |
| ipv4 | `23.239.3[.]218` | **C2 de la campaña de la CGE, puerto 9091** (CSIRT `CMV24-00455`) | Alta | Bloqueo |
| ipv4 | `209.59.174[.]255` | Infraestructura SMTP, campaña de la CGE | Media | Solo retrohunt |
| ipv4 | `148.66.147[.]215` | Infraestructura SMTP, campaña del SII de 2024 | Media | Solo retrohunt |
| ipv4 | `185.43.207[.]177` | Infraestructura SMTP, campaña de la Tesorería General | Media | Solo retrohunt |
| ipv4 | `45.79.86[.]87` | Infraestructura SMTP, campaña de factura impaga, puerto 57496 | Media | Solo retrohunt |
| ipv4 | `95.164.22[.]60` | C2 de la campaña del Ministerio de Energía, puerto 7957 | Alta | Bloqueo |
| ipv4 | `24.199.98[.]128` | Servidor WebDAV de la variante de Mispadu de `CVE-2023-36025`, puerto 80 | Alta | Bloqueo |
| ipv4 | `104.21.7[.]106` · `188.114.96[.]3` | Resuelven los C2 de `VENON`; **ambas son de un proveedor de CDN compartido** | Baja | Solo retrohunt |
| ipv4 | `206.0.29[.]58` · `51.222.75[.]250` · `51.222.75[.]248` · `192.99.226[.]117` · `212.69.5[.]84` · `34.227.229[.]85` | Panel de control de `VENON` | Media | Bloqueo tras verificación |
| ipv4 | `140.82.18[.]85` | C2 observado en la configuración de Mispadu (Cofense, feb-2026) | Media | Bloqueo tras verificación |
| url | `hxxps://52zd[.]com/profile/analytic/Informe-21-2024.zip` | Contenedor del malware, campaña del SII de 2024 | Alta | Bloqueo |
| url | `hxxps://s3.sa-east-1.amazonaws[.]com/8151218-25.2025.7.12.5178/modmarco2026-2.zip` | Carga de `VENON` en almacenamiento en la nube. **Servicio legítimo** | Alta | **Bloqueo de la URL completa; NO del dominio base**, que es un servicio legítimo de uso masivo. Detección y búsqueda retrospectiva|
| url | `hxxps://storage.googleapis[.]com/mydns2026/startabril2026` | Depósito de configuración de `VENON`. **Servicio legítimo** | Alta | **Bloqueo de la URL completa; NO del dominio base**, que es un servicio legítimo de uso masivo. Detección y búsqueda retrospectiva|
| url | `hxxp://trilivok[.]com/4g3031ar0/cb6y1dh/it.php` | Extremo de exfiltración de Mispadu; el sufijo `it.php` se repite entre campañas | Alta | Bloqueo |
| useragent | `Microsoft-WebDAV-MiniRedir` | Petición WebDAV disparada por el `.url` de Mispadu. **Componente legítimo de Windows**: la señal es el destino externo | Media | Detección por contexto |
| filepath | `C:\Users\Public\Temp\ChromeAuto_` | **Carpeta de perfil de navegador clonado del gusano de WhatsApp.** El artefacto más específico de la amenaza de 2026 | Alta | Detección y caza |
| filepath | `C:\ProgramData\USOShared\NuPLihaOH\` | Carpeta de preparación de `VENON` | Alta | Detección y caza |
| filename | `Bizarro.txt` · `V.txt` · `Ok.txt` · `Etc` | Ficheros de marca de Mekotio en la raíz del perfil del usuario. **La mayoría no coexisten: encontrar uno ya es sospechoso** | Alta | Detección y caza |
| filename | `nopagadafacSiimarzo.msi` · `Siifactmarzo.zip` · `nopagadafacturaSii.zip` · `Informe-21-2024.zip` · `Informe-Detallado.msi` · `factnuevamarzocgeboletaeletricidad.zip` · `DevolucionImpuestopiendenteTGR_16081.zip` · `FacturaContabilSolutionsDiciembre.msi` | Nombres de fichero de las cinco campañas chilenas. **Son los más útiles para búsqueda retrospectiva en el correo** | Alta | Detección y caza |
| filename | `®mjtgr.exe` · `libcef.dll` · `qYogBt.zip` · `NVIDIANotification.exe` | Ficheros de la cadena de `VENON`; el primero lleva el carácter U+00AE como prefijo | Alta | Detección y caza |
| artefacto | Clave HMAC `TenHaVunf!@#2026` · palabra mágica de configuración `EF01` · claves `ENA`, `FCX`, `LT`, `HL`, `PFX`, `DEL`, `ArrMSG`, `ArrMF`, `ArrURL` | Configuración del *spambot* de WhatsApp de Astaroth | Alta | Caza en memoria y en disco |
| artefacto | `BaixarWAJS` · `ProcessarEnvio` · `ProcessarContatos` · `LoadConfigs` · `WebDriverUpdater` · `Cleanup` · `enviarParaContato` · `mensagemSaudacao` | Nombres de función compartidos entre el *spambot* de Astaroth y `Vareg` | Alta | Caza por cadena en binarios |
| artefacto | Contraseña `L0@D_S3CR3T_K3Y_X9F2_PR0D_2024!` y sal `LOAD_SALT_2024!!` · tarea programada `NVIDIA Notification Service` | Material criptográfico y persistencia de `VENON` | Alta | Caza |
| artefacto | Formato de comando C2 `<\|comando\|>` · elementos de página `new-chat-outline`, `settings-refreshed`, `chat` · patrón de adjunto `m_<número>_NUMERO_` | Artefactos de protocolo de Mekotio y del gusano de WhatsApp | Alta | Detección en red y en host |
| puerto | `9091` · `7957` · `57496` | Puertos de C2 de las campañas chilenas. **Detectar por combinación con proceso no reconocido**, no por puerto suelto | Media | Detección por contexto |
| asunto | `Notificacion de Factura Pendiente` · `Restitución de Valores de Impuestos. 08/21/2024 06:15:11 pm` | Asuntos exactos de dos campañas chilenas (CSIRT `CMV25-00499` y `CMV24-00483`) | Alta | Búsqueda retrospectiva en el correo |

*Nota de higiene.* Están marcados como software o servicio legítimo y **no deben bloquearse por hash ni por dominio**: el agente y el actualizador de PDQ Connect, `PDQConnectUpdater-0.3.0.msi`, `WixSharp.dll`, el intérprete de AutoIt, el agente de usuario de WebDAV, y los servicios de almacenamiento en la nube (`amazonaws.com`, `storage.googleapis.com`, `github.com`). Están marcados como probable sitio legítimo comprometido, y merecen validación antes del bloqueo, los dominios `cmg-technology[.]ro`, `ebccarpentrydublin[.]com`, `enviroecobusiness[.]ro`, `meridianeyecare[.]com`, `inovia[.]com[.]ao`, `greatcreekcanines[.]com` y `gptplan[.]ro`. Las dos direcciones que resuelven los C2 de `VENON` pertenecen a un proveedor de CDN compartido y se entregan con confianza baja.

## Anexo B — Fuentes y valoración

> Valoración doble tipo Admiralty/OTAN: **fiabilidad de la fuente (A–F)** ×
> **credibilidad de la información (1–6)**. Se valoran por separado.

| Fuente | Disciplina | Fiabilidad | Credibilidad | Notas de sesgo |
|---|---|---|---|---|
| CSIRT Nacional de Chile — cinco alertas (`2CMV23-00417-01`, `CMV24-00455`, `CMV24-00463`, `CMV24-00483`, `CMV25-00499`) | OSINT gubernamental nacional | A | 1 | **La fuente más pertinente de este informe y la única nacional.** Cuatro de las cinco marcadas `TLP:CLEAR` en el portal; la de 2023 no muestra campo TLP. Publican indicadores con contexto pero **sin recomendaciones, sin análisis de persistencia y sin distinguir el software legítimo del malicioso** en sus listas. No se leyeron los PDF adjuntos (brecha `G-6`) |
| ESET LA — «Mekotio: troyano bancario dirigido principalmente a Chile» (14-jul-2020) | OSINT comercial / TECHINT | B | 1 | **El análisis técnico de referencia sobre la variante chilena.** Primera mano, con tabla ATT&CK y descripción de los artefactos más duraderos del informe. Tiene seis años: su descripción del arsenal está superada, sus artefactos de host siguen vigentes. No publica hashes, por decisión explícita |
| ESET LA — «Campaña activa dirigida a Chile» (16-ago-2019) | OSINT comercial / TECHINT | B | 2 | Fuente del dato del 48 % de detecciones mundiales en Chile y de la geolocalización de la descarga a direcciones chilenas. Siete años de antigüedad. Publica un indicador bajo encabezado erróneo (SHA1 para un valor de 64 caracteres) |
| CrowdStrike — «Inside Astaroth's New Spambot Component» (29-jul-2026) | OSINT comercial / TECHINT | B | 1 | **La fuente más reciente y la del hallazgo de mayor consecuencia.** Análisis de primera mano del módulo de WhatsApp, con regla YARA y consulta de caza publicadas. Declara sus confianzas con precisión poco común: alta para el desarrollador, moderada para el código compartido, baja para la fusión con `Vareg` |
| ZenoX — «VENON: The First Brazilian Banker RAT in Rust» (10-mar-2026) | OSINT comercial / TECHINT | B | 2 | Análisis técnico profundo con metodología declarada. **Declara expresamente baja confianza en cualquier atribución** y presenta la hipótesis de la reescritura asistida por IA sin asignarle nivel de confianza. Dos inconsistencias internas consignadas en §3.3. Proveedor pequeño, menos trayectoria verificable que los demás |
| Palo Alto Unit 42 — «Exploring the Latest Mispadu Stealer Variant» (2-feb-2024) | OSINT comercial / TECHINT | B | 1 | Primera mano, con regla YARA y consultas de caza. Reconoce que las muestras **se compilaron antes de la publicación del CVE**, lo que matiza su propio titular. Nombra dos ficheros distintos para la misma etapa |
| Cofense — «Mispadu Phishing Malware Baseline» (11-feb-2026) | OSINT comercial | B | 2 | Línea base cuantificada de cadenas de entrega con porcentajes. **Es la fuente que desmiente la premisa del encargo:** 81 % de correos en español, mayoritariamente a México, sin mención de Chile. Pocos indicadores |
| CronUp — campaña del Ministerio de Energía (feb-2025) | OSINT comercial nacional | B | 3 | **Fuente chilena, lo que es valioso y escaso.** Documenta la campaña más oportunista del informe. Fuente única, sin corroboración, y su cifra de 106 instalaciones proviene del panel del atacante. Sin hashes |
| Recorded Future / Insikt — panorama de cibercrimen en Latinoamérica y el Caribe (~ene-2026) | OSINT comercial | B | 2 | Contexto regional cuantificado. Útil para situar el ecosistema; **casi sin indicadores y sin mapeo ATT&CK**. Su mención de Chile es marginal. Una inconsistencia interna en las cifras de Brasil |
| Feedzai — análisis de Mispadu (oct-2024) | OSINT comercial | C | 3 | **Solo se leyó la página de presentación;** el informe completo está tras un formulario y su PDF no fue legible. Lo poco citado proviene del resumen público. No menciona Chile |
| MITRE ATT&CK — traducción de la numeración antigua de la tabla de ESET | Marco de referencia | A | 1 | Usado solo para traducir identificadores obsoletos (`T1192`, `T1194`, `T1503`) a la numeración actual. Sin aporte de contenido |
| Comprobación propia de ausencia de alerta chilena de esta familia en 2026, 16-nov-2026 | Análisis propio / OSINT | B | 3 | **Hallazgo negativo:** la ausencia en el portal no prueba la ausencia de campañas. La alerta de abril de 2026 sobre el SII existe pero no atribuye familia. Consignado como brecha `G-3` |

**Escalas**
- **A** completamente fiable · **B** normalmente fiable · **C** bastante fiable · **D** normalmente no fiable · **E** no fiable · **F** no evaluable.
- **1** confirmada por otras fuentes · **2** probablemente cierta · **3** posiblemente cierta · **4** dudosa · **5** improbable · **6** no evaluable.

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

## Anexo D — Instituciones chilenas suplantadas, para formación y para detección

> Esta tabla existe para dos usos concretos: alimentar la regla `D-12` y el módulo de
> formación de la decisión E-g. No es una lista de amenazas, es la lista de los trámites
> que un empleado chileno no puede ignorar, que es exactamente por lo que funcionan.

| Institución o marca | Pretexto documentado | Fuente | Fecha |
|---|---|---|---|
| Servicio de Impuestos Internos (SII) | Falsa factura no pagada, con adjunto `.zip` y `.msi` | CSIRT `2CMV23-00417-01` | 2023-06-08 |
| Compañía General de Electricidad (CGE) | Falso retraso en el pago de una factura, con enlace de descarga | CSIRT `CMV24-00455` | 2024-04-08 |
| Servicio de Impuestos Internos (SII) | Falso problema en la emisión de boletas electrónicas | CSIRT `CMV24-00463` | 2024-05-22 |
| Tesorería General de la República | Supuesta devolución de impuestos pendiente, con falso formulario | CSIRT `CMV24-00483` | 2024-08-22 |
| Sin marca concreta — factura impaga genérica | Supuesta deuda impaga, asunto «Notificacion de Factura Pendiente» | CSIRT `CMV25-00499` | 2025-01-16 |
| Ministerio de Energía | «Alerta de Posible Apagón Eléctrico», aprovechando el corte masivo | CronUp | 2025-02-27 |
| Compañía de servicios telefónicos chilena (no nombrada) | Falso informe de deuda, con descarga restringida a IP chilenas | ESET LA | 2019-08-16 |

## Anexo E — Marcos de referencia empleados

`MITRE ATT&CK v18` · `MITRE D3FEND` · `Cyber Kill Chain` · `Pirámide del Dolor` ·
`Modelo del Diamante` · `F3EAD` · `ICD 203` (lenguaje estimativo) · `ACH, supuestos
clave, pre-mortem` · `TLP 2.0` · `PAP` · `STIX 2.1 / TAXII 2.1` · `Admiralty Code`

## Anexo F — Paquete legible por máquina

- Bundle STIX 2.1: pendiente de generar. Debe modelar **seis objetos `malware` distintos y no un `intrusion-set` único**, con relaciones `related-to` entre ellos justificadas por proveedor compartido y no por identidad de operador; `indicator` del Anexo A con `valid_until` y marcado explícito de software legítimo; y `attack-pattern` con las técnicas de §T-2, distinguiendo las que publica el CSIRT de las que se deducen.
- Evento MISP: pendiente. Taxonomías: `tlp`, `pap`, `admiralty-scale`, `estimative-language`, más etiqueta propia `troyano-bancario-latam` y `objetivo:chile`.
- Reglas: las dos reglas Sigma de §X-4 y las doce plantillas de §X-3, versionadas con el identificador `CTI-2026-021` y estado `experimental`. **Incorporar además la regla YARA de CrowdStrike para el *spambot* y la de Unit 42 para Mispadu**, que están publicadas y no se reproducen aquí por ser material de terceros.
- Lista de bloqueo y lista de detección **separadas**: este informe es el primero de la serie donde una parte de los indicadores corresponde a software legítimo y mezclarlos en un solo fichero provocaría una interrupción.

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-11-16 | Emisión inicial. Elaborado sobre cinco alertas del CSIRT Nacional de Chile y siete informes de proveedor de primera mano. **El encargo partía de la premisa de que Mispadu era la familia de mayor relevancia chilena; la colección mostró que es Mekotio y el foco se reorientó**, lo que queda consignado en §3.3. Sin telemetría propia: §O-4 sin evaluar | Célula CTI |

## Anexo H — Realimentación del consumidor

| Pregunta | Respuesta |
|---|---|
| ¿Respondió a su requisito? | |
| ¿Qué decisión tomó o cambió con este informe? | |
| ¿Se respondieron X-1, X-2 y X-4 de §O-4? ¿Con qué resultado? | |
| ¿Se ingirieron los indicadores del CSIRT Nacional en el SIEM (decisión E-e)? | |
| ¿Se tomó la decisión sobre WhatsApp Web (E-d)? | |
| ¿Se evaluó el flujo de pagos con Prevención de Fraude (E-h)? | |
| ¿Qué faltó? | |
| ¿Llegó a tiempo? | |

> Sin este anexo devuelto, el ciclo de inteligencia queda abierto y el próximo producto no
> mejora. En este caso la dependencia más dura no es la telemetría: es **la decisión E-e**.
> Mientras los indicadores del CERT nacional no entren en nuestras herramientas, este
> informe seguirá siendo lectura y no defensa.
