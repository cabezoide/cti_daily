---
tlp: "TLP:CLEAR"
pap: "PAP:AMBER"
id: "CTI-2026-022"
version: "1.0"
tipo: "Perfil de actor"
foco_regional: "Colombia · Chile · Latinoamérica"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "Red Akodon · campañas «Shadow Vector»"
fecha: "2026-11-16"
caduca: "2027-02-16"
autor: "Célula CTI"
distribucion: "Elaborado íntegramente con fuentes abiertas TLP:CLEAR. Difusión libre, conservando la atribución de las fuentes y las salvedades metodológicas de §3. El informe primario de SCILabs que da nombre al actor no pudo leerse (véase §3.3 y brecha G-1)."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-022

## El actor cuyo nombre está en disputa: tres proveedores, tres nombres y una sola campaña

### Lo que hace funcionar esta amenaza no es el troyano: es el buzón legítimo de una entidad pública comprometido

> **Regla de oro del producto:** todo párrafo debe responder a un requisito de
> inteligencia (PIR) y habilitar una decisión. Si un párrafo no cambia lo que
> alguien va a hacer, va al anexo o se borra.

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-022` |
| Versión / fecha | `1.0` — 2026-11-16 |
| Tipo de producto | Perfil de actor **en disputa de atribución** más evaluación de transferibilidad del método. **No es un perfil cerrado:** el sujeto es un conjunto de actividad que un proveedor sigue como actor propio y otro vincula a un actor mayor sin resolver la relación |
| Niveles cubiertos | Estratégico · Operacional · Táctico · Técnico |
| Foco regional | **Colombia como objetivo documentado.** Chile entra por transferibilidad del método, no por victimología observada |
| Marcado de difusión | `TLP:CLEAR` · `PAP:AMBER` |
| Clasificación interna | Público — apto para difusión abierta |
| Requisitos atendidos | `PIR-02` (superficie de phishing y suplantación institucional), `PIR-04` (amenazas con foco regional hispanohablante), `PIR-07` (abuso de servicios legítimos de Internet como infraestructura), `PIR-09` (acceso inicial por correo de remitente legítimo comprometido) |
| Solicitante / consumidor primario | CISO · Jefatura de SOC · Seguridad del Correo · Ingeniería de Detección · Identidad |
| Ventana de observación | 2018 (primera actividad atribuida a TAG-144) → 2026-11-16, con detalle de campaña entre abril de 2024 y julio de 2025 |
| Base de colección | 7 fuentes. **Proveedor de primera mano:** Recorded Future / Insikt Group (26-ago-2025, corte de análisis 21-jul-2025), Acronis TRU (18-jun-2025). **Marco:** MITRE ATT&CK. **Citada por existencia, no leída:** SCILabs (27-may-2024), el informe que crea el nombre «Red Akodon» — el sitio rechaza la lectura automatizada. **Secundarias para la cronología:** ¡Mucho Hacker! (31-oct-2024) y Securelist, ambas citadas a través de los dos informes primarios. **Sin telemetría propia incorporada** |
| Autor (analista) | Célula CTI |
| Revisión por pares | Pendiente |
| Aprobación | Pendiente |
| Caducidad / revisión | 2027-02-16, o antes si un proveedor resuelve públicamente la relación entre Red Akodon y TAG-144, si aparece una campaña con señuelo judicial o tributario **chileno**, o si se documenta el uso de un buzón `.gob.cl` legítimo comprometido como remitente |
| Productos relacionados | `CTI-2026-018` (abuso de TLD — comparte el problema del dominio de suplantación), `CTI-2026-020` (**Blind Eagle / APT-C-36 — es el informe del que este es la continuación directa y con el que comparte el conjunto de actividad en disputa**), `CTI-2026-021` (troyanos brasileños — comparte el abuso de servicios legítimos y el proveedor brasileño de criptadores) |
| Paquete legible por máquina | Pendiente de generar (véase §14) |

<!-- cti:note type="warn" -->

> ⚠ **Limitación estructural de este producto, y es doble.** La primera: **no hay
> telemetría de la organización**, de modo que §O-4 vuelve a quedar sin rellenar. La
> segunda es específica de este informe y más incómoda: **el informe que crea el nombre
> «Red Akodon» no pudo leerse**. El sitio de SCILabs responde a la petición automatizada
> con una redirección a un sistema antirrobot. Todo lo que este producto afirma sobre el
> contenido de ese informe proviene de **lo que Recorded Future cita de él**, y está
> marcado como tal cada vez que aparece. No se ha rellenado nada de memoria.

<!-- cti:note type="good" -->

> ✅ **Lo que sí se puede hacer hoy, sin esperar a que nadie resuelva la atribución.** Las
> doce reglas de §X-3 y las catorce hipótesis de §T-4 **no dependen de cómo se llame el
> actor**. Cubren el adjunto `SVG`, el buzón institucional comprometido, la cadena de
> servicios legítimos y los cuatro troyanos de uso comercial. Si mañana los proveedores
> deciden que Red Akodon es Blind Eagle, no cambia una sola línea de este informe salvo
> el título.

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** El acceso inicial de esta amenaza es un correo que sale de verdad de una entidad pública, y eso invalida de raíz la capa de controles en la que más hemos invertido. Recorded Future documenta **once cuentas de correo institucionales colombianas** usadas para enviar los señuelos, entre ellas direcciones de la Rama Judicial (`@cendoj.ramajudicial.gov.co`), de una alcaldía (`alcaldia@simacota-santander.gov.co`), de una gobernación (`nomina@magdalena.gov.co`) y de una secretaría de educación. Insikt valora que el uso de cuentas gubernamentales comprometidas es «parte habitual del repertorio» del actor. **SPF, DKIM y DMARC validan correctamente esos correos porque son auténticos.** Valoramos **casi con certeza** *(95–99 %)*. **Confianza: alta.** *Base:* Recorded Future, análisis de primera mano con las direcciones enumeradas.

**KJ-2.** El vehículo del señuelo es un fichero `SVG`, y la técnica es tan reciente que MITRE la incorporó al marco en 2025. El `SVG` se abre en el navegador, presenta una citación judicial maquetada y lleva el enlace a la siguiente etapa; no es una imagen, es un documento con capacidad de ejecución. Acronis publica **141 muestras `SVG`** de una sola campaña, y Recorded Future documenta la misma técnica con el adjunto `Notificacion_electronica_sentencia_preliminar_Departamento_Juridico_sxyebfiv.svg`. La técnica es `T1027.017`. Valoramos **casi con certeza** *(95–99 %)*. **Confianza: alta.** *Base:* dos proveedores de primera mano, con muestras.

**KJ-3.** El pretexto es el mismo que el de Mekotio en Chile, trasladado al poder judicial: el trámite que no se puede ignorar. Las campañas suplantan a la **Fiscalía General de la Nación**, a juzgados civiles y penales nominados con su número y circuito —`Juzgado 06 Civil del Circuito de Bogotá`, `Juzgado 003 Penal Municipal de Chiquinquirá`—, y usan asuntos como «Cobro por intereses moratorios – Radicado 11001-28-05-03004». **El nivel de detalle institucional no es imitable sin conocer el país.** Valoramos **muy probable** *(80–95 %)*. **Confianza: alta.** *Base:* Recorded Future y Acronis, con asuntos y nombres de juzgado transcritos.

**KJ-4.** El arsenal es íntegramente de mercado y buena parte está pirateado, lo que nos quita la posibilidad de detectar por familia. Los implantes son `AsyncRAT`, `REMCOS`, `QuasarRAT` —en la variante `BlotchyQuasar`—, `XWorm`, `DcRAT` y `LimeRAT`: todos comerciales o de código abierto, distribuidos por canales de Telegram, con criptadores por suscripción y, en al menos un caso, con la marca del grupo que los crackeó incrustada en la configuración (`CRACKED BY hxxps://t[.]me/xworm_v2`). Valoramos **casi con certeza** *(95–99 %)*. **Confianza: alta.** *Base:* convergencia de los dos informes primarios, con configuraciones extraídas.

**KJ-5.** La atribución está en disputa y nadie la ha resuelto, pero eso no es una brecha de inteligencia: es el hecho. SCILabs nombró «Red Akodon» en mayo de 2024 y, según Insikt, **eligió seguirlo como actor distinto a pesar de reconocer que se parecía mucho a Blind Eagle**. Recorded Future dice haber encontrado «más evidencia que vincula» TAG-144 con Red Akodon, pero **no declara su propia decisión de fusión ni asigna nivel de confianza**, y Acronis publica el mismo tipo de actividad bajo el nombre «Shadow Vector» **sin hacer ninguna afirmación de atribución**. Valoramos **probable** *(55–80 %)* que los tres conjuntos describan actividad del mismo ecosistema de operadores, y **poco probable** *(20–45 %)* que sean un único equipo con un único mando. **Confianza: baja.** *Base:* tres proveedores con tres delimitaciones distintas y ninguna resolución pública; la valoración es nuestra.

**KJ-6.** La escalada de privilegios de la cadena más reciente llega por controlador vulnerable firmado, no por exploit del sistema. En la variante de `REMCOS` que describe Acronis, el implante deja en `%Temp%` dos controladores legítimos y vulnerables —uno de WiseCleaner (`CVE-2023-1486`) y uno de Zemana (`CVE-2022-42045`)—, los arranca como servicio de núcleo y llama a `DeviceIoControl` con el código `0x80002010` para **registrar su propio `svchost.exe` como proceso «autenticado»**. Es «trae tu propio controlador vulnerable» ejecutado desde una citación judicial falsa. Valoramos **muy probable** *(80–95 %)*. **Confianza: moderada.** *Base:* Acronis, fuente única con análisis de primera mano; la asignación de los CVE proviene de los pies de figura.

**KJ-7.** Chile no aparece como víctima en ninguna de las dos fuentes primarias, y el método es trasladable en una tarde de trabajo del adversario. Lo único colombiano de esta amenaza son los nombres de las instituciones: el `SVG`, el troyano de mercado, el DNS dinámico, el alojamiento en Bitbucket o Paste.ee y el buzón público comprometido funcionan igual con «Oficina Judicial Virtual», «Poder Judicial», «SII» o «Tesorería General». Valoramos **posibilidad real** *(45–55 %)* de que aparezca una campaña con señuelo judicial o tributario chileno en los próximos doce meses. **Confianza: baja.** *Base:* es una inferencia nuestra sobre la facilidad del cambio, apoyada en el precedente del ecosistema brasileño descrito en `CTI-2026-021`, no en evidencia de esta amenaza.

**Qué cambiaría estos juicios:** la aparición de un adjunto `SVG` con un señuelo del Poder Judicial de Chile, o de un correo con remitente `@pjud.cl` o `@sii.cl` legítimo usado para distribuir uno de los cuatro troyanos. Eso convertiría KJ-7 de proyección en hecho y este informe en una alerta. Es el indicador `I-1` de §O-7.

---

## 2. Resumen ejecutivo

Hay un conjunto de campañas contra Colombia que tres proveedores describen con tres nombres distintos y que ninguno de los tres ha conseguido —o querido— unificar. SCILabs lo llamó **Red Akodon** en mayo de 2024 y decidió seguirlo como actor nuevo aunque se parecía mucho a Blind Eagle. Recorded Future lo trata como actividad vinculada a **TAG-144**, que es su nombre para Blind Eagle, pero no cierra la relación. Acronis publica el mismo patrón técnico como **Shadow Vector** y no atribuye a nadie.

La tentación es tratar esto como un problema de taxonomía. No lo es. Es un problema de compra: cuando el informe que fundamenta un indicador lleva un nombre y el proveedor de inteligencia que lo revende lleva otro, los indicadores entran dos veces en el SIEM, las reglas se duplican y nadie sabe si la campaña que tiene delante es nueva o es la de hace un año con otro nombre.

Y debajo de la disputa de nombres hay un mecanismo que sí está perfectamente documentado y que es el que debería ocuparnos. El correo que inicia la intrusión **sale de una cuenta auténtica de una entidad pública**: once direcciones institucionales colombianas enumeradas, varias de la Rama Judicial, una de una alcaldía, una de una gobernación. Lleva un adjunto `SVG` que el navegador abre como una citación judicial maquetada, con el número de radicado y el nombre del juzgado. Detrás vienen una cadena de servicios legítimos —Discord, Bitbucket, Paste.ee, archive.org, Google Drive— y un troyano comercial comprado o pirateado.

Nada de eso es específicamente colombiano salvo el nombre de las instituciones. En Chile, el equivalente exacto del señuelo existe, es igual de obligatorio de atender y tiene la misma estética administrativa: la Oficina Judicial Virtual, una notificación del Poder Judicial, una del Servicio de Impuestos Internos. Lo que falta para que esta amenaza sea chilena es que a alguien le compense traducirla, y traducirla cuesta una tarde.

Lo que pedimos a Dirección no es presupuesto: es asumir que la autenticación de remitente —SPF, DKIM, DMARC, lo que llevamos años desplegando— **no cubre este caso**, y decidir en consecuencia sobre dos cosas concretas: qué hacemos con los adjuntos `SVG` entrantes, y qué procedimiento tiene un empleado para verificar una notificación judicial sin hacer clic.

<!-- cti:cards -->

| Rasgo | Qué significa | Etiqueta |
|---|---|---|
| El remitente es auténtico | Once cuentas públicas comprometidas. La autenticación de correo valida el mensaje porque el mensaje es verdadero | `01 · remitente` |
| El adjunto es un `SVG` | Se abre en el navegador, no en un visor de imágenes. MITRE añadió la técnica en 2025 | `02 · formato` |
| El pretexto es el juzgado | Radicado, circuito, nombre del juzgado. Detalle institucional que no se improvisa | `03 · pretexto` |
| El arsenal es de tienda | Seis troyanos comerciales o pirateados, criptador por suscripción, DNS dinámico gratuito | `04 · mercado` |
| El nombre está en disputa | Tres proveedores, tres nombres, ninguna resolución. Afecta a la compra y a la gestión de indicadores | `05 · taxonomía` |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `11` | Cuentas de correo institucionales colombianas usadas como remitente en los señuelos | Rama Judicial, alcaldía, gobernación, secretaría de educación, hospital |
| `141` | Muestras `SVG` publicadas por Acronis de una sola campaña | Más 4 paquetes y 20 cargas: 165 hashes en total |
| `5` | Conjuntos de infraestructura («clusters») que Recorded Future delimita dentro de TAG-144 | Sin nombre propio: Cluster 1 a Cluster 5 |
| `28` | Víctimas enumeradas por Recorded Future con fechas y C2, en dos de los cinco conjuntos | 20 de ellas de gobierno; el resto salud, educación, transporte, comercio, petróleo |
| `6` | Familias de troyano de acceso remoto observadas | AsyncRAT, REMCOS, QuasarRAT/BlotchyQuasar, XWorm, DcRAT, LimeRAT |
| `170` | Descargas de un repositorio público de Bitbucket con el señuelo judicial, **en las horas siguientes a su publicación** | 28-may-2025, repositorio `notificaciones-judiciales2025-2005` |
| `2` | Controladores legítimos y vulnerables usados para escalar privilegios | WiseCleaner (`CVE-2023-1486`) y Zemana (`CVE-2022-42045`) |
| `0` | Víctimas chilenas documentadas por las fuentes primarias | Chile aparece solo como «ubicación de actividad» en una cita de segunda mano |

<!-- cti:note type="good" -->

> ✅ **Decisiones que se solicitan a Dirección.** (a) Fijar la postura sobre **adjuntos `SVG` entrantes**: bloqueo, o reescritura a imagen plana, o cuarentena con detonación — 30 días. (b) Publicar un **procedimiento de verificación de notificaciones judiciales y tributarias** por canal independiente, con la lista de dominios oficiales legítimos — 45 días, con Asuntos Corporativos y Fiscalía interna. (c) Aceptar formalmente que **la autenticación de remitente no cubre el remitente legítimo comprometido**, y reorientar la inversión de correo hacia el análisis de adjunto y de destino del enlace — decisión de criterio, 30 días. (d) Resolver la **política de servicios legítimos de Internet** —Discord CDN, Bitbucket, Paste.ee, archive.org— en equipos corporativos: bloqueo, o registro con atribución de proceso — 60 días. (e) Encargar a la célula CTI una **nota de equivalencias institucionales Chile–Colombia** para formación y para detección, que es el Anexo D de este informe y ya está hecha — 15 días para distribuirla.

---

## 3. Alcance, requisitos y limitaciones

**3.1 Requisitos de inteligencia atendidos**

| Req. | Enunciado | ¿Respondido? | Dónde |
|---|---|---|---|
| PIR-02 | ¿Qué superficie de suplantación institucional nos puede afectar? | Sí, por transferencia | §E-1, §T-1, Anexo D |
| PIR-04 | ¿Qué amenazas operan contra la región hispanohablante y con qué método? | Sí | §E-2, §O-5 |
| PIR-07 | ¿Qué servicios legítimos se están usando como infraestructura de entrega? | Sí | §X-1, §X-2, Anexo A |
| PIR-09 | ¿Qué hacemos cuando el remitente del phishing es auténtico? | Sí — y la respuesta incomoda | §E-1, §E-4, §X-5 |
| — | ¿Hay víctimas chilenas de este actor? | **No** — ninguna fuente lo documenta | §E-2, §14 |
| — | ¿Estamos ya comprometidos o suplantados? | **No** — requiere telemetría | §O-4, §14 |

**3.2 Fuera de alcance.** No se evalúa: el perfil completo de Blind Eagle / APT-C-36, que es el producto `CTI-2026-020` y no se repite aquí; el análisis interno de cada una de las seis familias de troyano comercial, que ocuparía un producto por familia y está bien cubierto por sus respectivos informes públicos; la actividad de TAG-144 contra Ecuador y Panamá, que se menciona para situar la victimología pero no se desarrolla; y la respuesta a un compromiso consumado, que es materia de respuesta a incidentes.

**3.3 Limitaciones de la colección.** (i) **Sin telemetría propia**, de modo que §O-4 está sin rellenar. (ii) **El informe que da nombre al actor no pudo leerse.** El sitio de SCILabs responde a la petición automatizada con una redirección a un sistema antirrobot de terceros. No se intentó eludirlo. En consecuencia, todo lo que aquí se afirma del contenido de ese informe —los señuelos de la Fiscalía y del Juzgado 06 Civil de Bogotá, los cuatro troyanos, las dos cuentas comprometidas, los cuatro usuarios de GitHub, la persistencia por acceso directo en el menú de inicio— **proviene de lo que Recorded Future cita de él y está marcado así en cada aparición**. Es la brecha `G-1` y es la más barata de cerrar de todo el informe: basta con que una persona abra la página en un navegador. (iii) **La relación entre los tres conjuntos de actividad no está resuelta por ninguna fuente**, y este informe no la resuelve tampoco: la consigna como el hecho que es (`KJ-5`, `H5` de §O-6). (iv) **Recorded Future no publica fecha en el cuerpo de su informe**; la fecha del 26 de agosto de 2025 proviene del nombre del fichero PDF que el propio sitio enlaza, y el corte de análisis declarado es el 21 de julio de 2025. (v) **Hay una contradicción interna en el informe de Recorded Future** que conviene conocer antes de citarlo: el cuerpo dice que el Cluster 1 ataca «exclusivamente» al gobierno colombiano, y su propio apéndice de víctimas incluye seis víctimas de salud, educación, comercio y transporte en ese mismo conjunto. (vi) **Acronis no atribuye y no publica tabla ATT&CK**; el mapeo de §T-2 que no proviene de las dos técnicas que esa fuente sí enlaza (`T1027.017` y `T1055.012`) es nuestro y está marcado. (vii) **Ninguna fuente publica puertos de mando y control** salvo el 7788 de una configuración de AsyncRAT; las reglas de §X-3 no pueden apoyarse en puerto. (viii) **Las cuentas de correo institucionales comprometidas pertenecen a terceros inocentes**: están en el Anexo A porque son el indicador más valioso del informe, marcadas como «no bloquear el dominio», y su uso debe ceñirse a detección.

**3.4 Metodología.** Disciplinas: OSINT comercial de proveedor (dos informes de primera mano con muestras y apéndices), OSINT de marco (MITRE ATT&CK), análisis de transferibilidad (construcción de la tabla de equivalencias institucionales del Anexo D). Técnicas analíticas estructuradas: análisis de hipótesis competidoras sobre la atribución (§O-6), comprobación de supuestos clave, pre-mortem. Marcos: MITRE ATT&CK v18, Pirámide del Dolor, Cadena de Intrusión, ICD 203, código Admiralty.

---

# NIVEL ESTRATÉGICO
### Para: Consejo · CISO · Riesgo · Asuntos Corporativos · Identidad · Horizonte: 6–24 meses

## E-1. Qué representa esta amenaza en el panorama

Llevamos una década construyendo la defensa del correo sobre una premisa: que se puede distinguir al remitente legítimo del impostor. SPF comprueba que el servidor que envía esté autorizado por el dominio. DKIM firma el mensaje. DMARC dice qué hacer cuando algo no cuadra. Tres protocolos, años de despliegue, y una enorme cantidad de capital político gastado en conseguir que los equipos de infraestructura los apliquen.

Esta amenaza no los rompe. Los cumple.

El correo que inicia la intrusión sale de una cuenta auténtica de un juzgado, de una alcaldía o de una gobernación. Recorded Future enumera once direcciones institucionales colombianas, y de una de ellas —la de un juzgado penal municipal de Chiquinquirá— llega a confirmar que es legítima y que **pertenece a la secretaría de un juzgado civil de ese mismo circuito**, cuya dirección apareció además en registros de un ladrón de credenciales. Es decir: el adversario no falsificó un remitente, le robó la contraseña a un funcionario y escribió desde su buzón. SPF pasa. DKIM pasa. DMARC alinea. El mensaje es auténtico y el contenido es malicioso, y esas dos cosas no son incompatibles.

A eso se suma un segundo rasgo que nos quita la otra mitad de la defensa. El adjunto no es un ejecutable ni un documento de ofimática con macro: es un `SVG`. Para la mayoría de las pasarelas y para casi todos los usuarios, un `SVG` es una imagen. Técnicamente es un documento de marcado que el navegador interpreta, y que puede llevar texto maquetado, enlaces y lógica. El adversario lo usa para presentar una citación judicial convincente —con número de radicado, nombre del juzgado y la contraseña del archivo comprimido que vendrá después— sin que ningún motor de análisis vea un binario. MITRE incorporó la técnica al marco en 2025 como `T1027.017`; es decir, es tan reciente que buena parte de los productos de correo desplegados no la contemplaba cuando se compró.

Y el tercer rasgo es el que hace inútil la detección por familia: **todo el arsenal es de tienda**. Seis familias de troyano de acceso remoto, todas comerciales o de código abierto, varias explícitamente pirateadas —una de ellas lleva incrustada en la configuración la marca del grupo que la crackeó y un enlace a su canal de Telegram—, con criptadores contratados por suscripción y mando y control sobre DNS dinámico gratuito. No hay desarrollo propio que rastrear. Hay un presupuesto de pocos cientos de dólares al mes y un mercado que lo surte.

<!-- cti:cards -->

| Cambio estructural | Por qué nos afecta | Etiqueta |
|---|---|---|
| El remitente auténtico comprometido | Invalida la capa de autenticación de correo en la que más hemos invertido. No es un fallo de configuración: es que la premisa no aplica | `01 · premisa` |
| El adjunto que no parece ejecutable | Un `SVG` pasa por imagen. La técnica es de 2025 y muchos productos desplegados no la contemplaban | `02 · formato` |
| La cadena sobre servicios legítimos | Discord, Bitbucket, Paste.ee, archive.org, Google Drive. Bloquear el dominio castiga al negocio; no bloquearlo deja la vía abierta | `03 · servicios` |
| El arsenal alquilado | Seis troyanos de mercado. No hay herramienta propia que seguir, y la detección por familia pierde sentido | `04 · mercado` |
| El nombre en disputa | Tres proveedores con tres nombres. Los indicadores entran duplicados y las campañas se cuentan dos veces | `05 · taxonomía` |

## E-2. Victimología y distribución

<!-- cti:bars title="Víctimas enumeradas por Recorded Future, por sector (Cluster 1 y Cluster 2, 28 víctimas)" color="#5a7ebe,#e0a33e,#4db99c,#c0392b" -->

| Sector | Víctimas |
|---|---|
| Gobierno (local, municipal, federal) | 20 |
| Educación | 4 |
| Transporte | 2 |
| Salud, comercio, petróleo | 3 |

<!-- cti:note type="warn" -->

> ⚠ **Esta tabla tiene una inconsistencia que viene de la fuente y hay que declararla.**
> El informe de Recorded Future afirma en el cuerpo que el Cluster 1 ataca
> «exclusivamente» al gobierno colombiano, y su propio apéndice de víctimas lista en ese
> mismo conjunto seis víctimas de educación, salud, comercio y transporte. Las dos cosas
> no pueden ser ciertas. Se consigna porque quien cite «exclusivamente gobierno» estará
> citando una afirmación que el apéndice de la misma fuente contradice, y porque la
> diferencia importa: si el objetivo es solo el Estado, una empresa privada chilena está
> fuera del tiro; si el objetivo incluye a quien se relaciona con el Estado, no lo está.
> Insikt añade, y esto sí es coherente, que varias víctimas no gubernamentales
> «mantienen algún grado de afiliación con el Estado».

**La geografía, con lo que cada fuente aporta.** Colombia es el objetivo primario en las tres fuentes, y el detalle institucional —juzgados nominados por circuito, la Fiscalía General de la Nación, el Consejo Superior de la Judicatura que llegó a publicar un aviso público sobre el abuso de su nombre— no deja lugar a duda. Recorded Future documenta además intrusiones en **Ecuador** y menciona víctimas ocasionales hispanohablantes en Estados Unidos. Chile aparece **una sola vez en las dos fuentes primarias**, en la sección de antecedentes de Recorded Future, dentro de una frase que cita a Securelist: las operaciones «se centran principalmente en Colombia, con actividad adicional en Ecuador, Chile y Panamá». No hay un hallazgo de Recorded Future sobre víctimas ni infraestructura chilena. Acronis no menciona Chile en ningún lugar.

<!-- cti:note type="warn" -->

> ⚠ **Lectura regional — y aquí hay que ser estrictos con nuestra propia tentación.** La
> frase «actividad adicional en Chile» es exactamente el tipo de dato que, mal usado,
> convierte un informe en alarmismo. Es una mención de segunda mano, sin víctima, sin
> fecha, sin sector y sin indicador, dentro de la sección de antecedentes de un informe
> cuyo objeto es Colombia. **Es el mismo hallazgo que ya consignamos en `CTI-2026-020`
> sobre Blind Eagle: Chile listado y no documentado.** Lo honesto es decir que la
> exposición chilena a esta amenaza **no está observada, está inferida**, y que la
> inferencia se apoya en la transferibilidad del método (§T-1 y Anexo D), no en
> evidencia de victimología. Si algún día hay un `SVG` con el escudo del Poder Judicial,
> este párrafo se reescribe. Hoy no lo hay.

<!-- cti:bars title="Cuentas de correo institucionales colombianas usadas como remitente, por tipo de entidad" color="#c0392b" -->

| Tipo de entidad | Cuentas |
|---|---|
| Rama Judicial (`cendoj.ramajudicial.gov.co`) | 7 |
| Gobernación y alcaldía | 2 |
| Secretaría de educación | 1 |
| Hospital público | 1 |

## E-3. Tendencia y pronóstico

<!-- cti:chart title="Hitos públicos del conjunto de actividad, por año" cap="Mide publicación de proveedor, no volumen de campaña. 2026 figura en cero a la fecha de cierre: no hay informe nuevo sobre este conjunto en lo que va de año, lo que no significa que la actividad haya cesado." -->

| Periodo | Informes públicos |
|---|---|
| 2023 | 0 |
| 2024 | 2 |
| 2025 | 2 |
| 2026 | 0 |

La trayectoria técnica de este conjunto en los dos últimos años tiene tres movimientos, y los tres apuntan en la misma dirección: menos binario propio, más servicio ajeno.

El primero es **el formato del señuelo**. De adjunto comprimido y doble extensión —`RELACIÓN DE SALDOS - CUENTA DE COBRO.pdf.exe`, que Recorded Future documenta en 2024— al `SVG` que se abre en el navegador, que es el patrón dominante en 2025 en las dos fuentes primarias. El cambio no busca más capacidad: busca no parecerse a un adjunto peligroso.

El segundo es **la cadena de alojamiento**. Las etapas intermedias ya no viven en servidores del adversario sino en servicios que ninguna organización puede bloquear sin coste: la red de distribución de contenidos de Discord, repositorios públicos de Bitbucket, Paste.ee, GitHub Gist, Google Drive, Dropbox y —el más llamativo— **archive.org, usado como depósito de cargas en base64 escondidas dentro de los píxeles de un JPEG**. Acronis y Recorded Future describen por separado la misma técnica de esteganografía, con marcadores distintos (`INICIO>>` y `<<FIM>>` en un caso, una cabecera de 54 bytes en el otro).

El tercero es **la ejecución sin fichero**. El cargador final se trae en memoria con `[Reflection.Assembly]::Load()` y se invoca llamando a un método llamado `VAI`. Las dos fuentes primarias coinciden en el nombre del método, lo que es uno de los pocos lazos técnicos duros entre los dos conjuntos de actividad, y una de las razones por las que `H1` de §O-6 se retiene.

Hay un cuarto movimiento, más incómodo de interpretar: **las cadenas tienen cadenas en portugués**. Acronis encuentra en el cargador mensajes de error como «Extensão não suportada» y «Recurso 'UAC.dll' não encontrado!», y nombres de parámetro como `caminhovbs` y `persitencia`; Recorded Future encuentra comentarios en portugués —«Junta os comandos»— en los ficheros de texto alojados en un servicio gratuito. Ninguna fuente concluye nada firme. Acronis sugiere «reutilización de código, recursos de desarrollo compartidos o incluso colaboración entre actores de distintas regiones», y apunta al ecosistema brasileño de criptadores que `CTI-2026-021` describe desde el otro lado. **Es el mismo mercado, visto desde el cliente.**

<!-- cti:cards -->

| Escenario | Desarrollo | Etiqueta |
|---|---|---|
| Continuidad contra Colombia con rotación de formato y de institución suplantada | El conjunto sigue atacando al Estado colombiano, cambia el formato del adjunto cuando los productos de correo lo alcanzan, y renueva el arsenal comprando. Las detecciones de §X-3 mantienen su validez porque son de comportamiento y de canal | `Probable · 55–80 %` |
| Traducción del método a otro país de la región, Chile incluido | El mismo kit con nombres de institución chilenos. Coste marginal para el adversario: redactar el señuelo. Es el cambio de mayor impacto para nosotros y el más barato para él | `Posibilidad real · 45–55 %` |
| Resolución pública de la atribución | Un proveedor con telemetría suficiente fusiona o separa formalmente Red Akodon y TAG-144. Simplifica la compra de inteligencia; no cambia una sola detección | `Posibilidad real · 45–55 %` |
| Salto de objetivo del fraude y el espionaje al acceso como mercancía | Los accesos obtenidos con estos troyanos se venden a terceros, incluidos grupos de extorsión. El mercado existe, pero ninguna fuente documenta el puente en este conjunto | `Poco probable · 20–45 %` |

## E-4. Decisiones que este informe pide al nivel estratégico

<!-- cti:table highlight="Chile|chilen|SVG|judicial|DMARC|remitente" -->

| # | Decisión | Fundamento | Plazo |
|---|---|---|---|
| E-a | **Fijar la postura sobre adjuntos `SVG` entrantes**: bloqueo, reescritura a imagen plana, o cuarentena con detonación. Excepciones nominales y documentadas para las áreas que los usan de verdad (diseño, marketing, ingeniería) | KJ-2: el `SVG` es el vehículo del señuelo en las dos fuentes primarias, con 141 muestras publicadas de una sola campaña. La técnica es de 2025 y nuestros productos pueden no contemplarla | 30 días |
| E-b | Publicar y comunicar un **procedimiento de verificación de notificaciones judiciales y tributarias** por canal independiente, con la lista de dominios y portales oficiales legítimos chilenos | KJ-3: el pretexto es el trámite obligatorio. No se puede pedir a un empleado que ignore una notificación de un juzgado; sí se le puede dar una forma de comprobarla | 45 días |
| E-c | **Aceptar formalmente que la autenticación de remitente no cubre el remitente legítimo comprometido**, y reorientar el criterio de inversión en seguridad del correo del «quién envía» al «qué trae y adónde lleva» | KJ-1: once cuentas públicas auténticas usadas como remitente. SPF, DKIM y DMARC validan correctamente esos mensajes. Es una decisión de criterio, no de producto | 30 días |
| E-d | Resolver la **política de servicios legítimos de Internet** en equipos corporativos —Discord CDN, Bitbucket, Paste.ee, archive.org, Gist— con registro y atribución de proceso donde no haya bloqueo | KJ-4 y §E-3: toda la cadena intermedia vive en servicios que no se pueden bloquear sin coste. Sin atribución de proceso no se puede distinguir el uso legítimo del abuso | 60 días |
| E-e | Distribuir la **tabla de equivalencias institucionales Chile–Colombia** del Anexo D a formación y a ingeniería de detección, y construir sobre ella la regla `D-11` | KJ-7: lo único colombiano de esta amenaza son los nombres. La tabla ya está hecha y su coste de distribución es cero | 15 días |
| E-f | Encargar a Identidad una **revisión de la exposición de nuestras propias cuentas de correo** a robo de credenciales por ladrón de información, con reposición obligatoria ante aparición en registros filtrados | KJ-1: Recorded Future encontró una de las cuentas comprometidas en registros de un ladrón de credenciales. El mecanismo que nos convierte en el remitente auténtico de la próxima campaña es ese | 45 días |
| E-g | Decidir si contratamos **una sola fuente de inteligencia comercial para este conjunto o dos**, y a quién creemos cuando discrepan en el nombre | KJ-5: tres proveedores, tres nombres, ninguna resolución. El coste de no decidir es duplicar indicadores y contar dos veces la misma campaña | 60 días |
| E-h | Incluir en el plan de colección permanente la **vigilancia del indicador `I-1`**: aparición de señuelo judicial o tributario chileno con adjunto `SVG` | Es el único indicador que convertiría este informe de preventivo en operativo. Vigilarlo no cuesta nada; no vigilarlo cuesta el aviso | 30 días |

---

# NIVEL OPERACIONAL
### Para: Jefatura de SOC · Respuesta a Incidentes · Threat Hunting · Seguridad del Correo · Horizonte: semanas–meses

## O-1. Identificación: un conjunto, tres nombres, cinco agrupaciones

Lo primero es fijar el vocabulario, porque sin eso no se puede leer ningún informe de esta amenaza sin confundirse.

| Nombre | Quién lo usa | Qué delimita | Relación declarada por su autor |
|---|---|---|---|
| `Red Akodon` | SCILabs (27-may-2024) | Campañas contra entidades públicas colombianas con REMCOS, QuasarRAT, AsyncRAT y XWorm desde abril de 2024 | **Actor distinto**, decidido así a pesar de reconocer gran parecido con Blind Eagle *(según la cita de Recorded Future; el informe original no pudo leerse)* |
| `TAG-144` | Recorded Future / Insikt (26-ago-2025) | Actor activo desde al menos 2018, con cinco agrupaciones de infraestructura (`Cluster 1` a `Cluster 5`) | «Más evidencia que vincula» TAG-144 con Red Akodon. **No declara fusión ni asigna confianza** |
| `Blind Eagle` · `APT-C-36` · `AguilaCiega` · `APT-Q-98` | Varios proveedores | El mismo actor que Recorded Future llama TAG-144 | Alias reconocidos entre sí |
| `Shadow Vector` | Acronis TRU (18-jun-2025) | Campañas contra usuarios colombianos con señuelo judicial en `SVG`, AsyncRAT y REMCOS, y escalada por controlador vulnerable | **Ninguna atribución.** Cita el informe de Red Akodon solo en la bibliografía |

Y dentro de TAG-144, las cinco agrupaciones que Recorded Future delimita por infraestructura, familia de malware, ventana de actividad y sector de la víctima. No tienen nombre propio, lo que es una decisión deliberada de su autor y conviene respetar al citarlas:

| Agrupación | Rasgo distintivo | Familias | Nomenclatura de dominio |
|---|---|---|---|
| `Cluster 1` | Víctimas de gobierno colombiano; VPN comercial como C2 | AsyncRAT `1.0.7`, DcRAT, REMCOS | `envio[0-9\-]{2,5}.duckdns.org` — Insikt lo describe como «probablemente generado por un DGA» |
| `Cluster 2` | Alojamiento en proxy y VPS; cadena por GitHub Gist | AsyncRAT con criptador `Roda`, XWorm | Palabras en español y la serie `deadpoolstart` más un año de cuatro cifras |
| `Cluster 3` | Infraestructura en ISP colombianos | REMCOS, AsyncRAT | Nombre y apellido en español más dígitos |
| `Cluster 4` | Phishing bancario (Davivienda, Bancolombia, BBVA) | AsyncRAT, XWorm, REMCOS | Abreviaturas cortas |
| `Cluster 5` | Infraestructura en VPS europeos, la más amplia en direcciones | AsyncRAT, REMCOS, XWorm, LimeRAT | Palabras en español con mes o año |

<!-- cti:note type="warn" -->

> ⚠ **Nota de tradecraft — tres errores concretos que evitar.** El primero: **no citar
> «Red Akodon» y «TAG-144» como si fueran dos amenazas distintas en el mismo párrafo.**
> Puede que lo sean y puede que no; mientras no esté resuelto, se citan como lo que son,
> dos nombres con una relación declarada en una dirección y no en la otra. El segundo:
> **no dar nombre propio a las cinco agrupaciones de Recorded Future.** Su autor
> deliberadamente no se lo puso, y bautizarlas nosotros añade un sexto nombre al problema
> que este informe denuncia. El tercero: **compartir un troyano no es ser el mismo
> actor.** AsyncRAT y REMCOS los usan decenas de grupos sin relación alguna; lo que une a
> estas agrupaciones no es el troyano, es el patrón de infraestructura y el señuelo.

## O-2. Atribución: qué se puede sostener

| Eje de atribución | Valoración | Confianza |
|---|---|---|
| Origen geográfico del operador | Hispanohablante con conocimiento institucional colombiano de primera mano. La nomenclatura de dominios usa nombres y apellidos en español; los señuelos nombran juzgados por número y circuito | Alta |
| Motivación | Mixta y no resuelta. Hay robo de credenciales bancarias (`Cluster 4`, phishing a tres bancos colombianos) y hay recolección de información contra entidades públicas. Ninguna fuente declara espionaje estatal | Moderada |
| Nexo estatal | **No planteado por ninguna de las dos fuentes primarias** | Alta (en la negativa) |
| Operadores | Sin identificar. Cuatro usuarios de GitHub asociados *(según la cita de Recorded Future del informe de SCILabs)*, una cuenta de Pastebin vinculada a uno de ellos, y un alias `TheMrHacker` en los repositorios de Bitbucket que Acronis describe como «posible pista sobre la identidad del operador» | Baja |
| Relación Red Akodon ↔ TAG-144 | **Sin resolver.** Un proveedor los separa, otro los vincula sin cerrarlo, un tercero no se pronuncia | Baja |
| Relación con el ecosistema brasileño | Reutilización de herramientas y posible colaboración, apoyada en cadenas y comentarios en portugués en los cargadores de ambas fuentes primarias. Ninguna fuente va más allá de «sugiere» | Baja |
| Capacidad de desarrollo propio | **Mínima o nula.** Todo el arsenal es comercial, de código abierto o pirateado. Lo propio es el señuelo y la cadena de entrega | Alta |

*Razonamiento sobre el conocimiento institucional:* un correo que cita un radicado con el formato correcto —`11001-28-05-03004`—, nombra un juzgado existente por su número y su circuito, y llega desde el buzón auténtico de ese tipo de entidad, lo redacta alguien que ha visto una notificación judicial colombiana de verdad. Es la misma observación que el informe `CTI-2026-020` hace sobre Blind Eagle y que `CTI-2026-021` hace sobre las campañas del SII: **la ventaja competitiva de estos actores es la fluidez administrativa, no la capacidad técnica.**

*Contraargumento:* la fluidez se puede comprar o alquilar igual que el troyano. Que el señuelo esté bien redactado no prueba que quien lo redactó sea quien opera el implante. Esa es precisamente la economía de capas que hace tan difícil la atribución en esta región, y la razón por la que `H5` de §O-6 se retiene sin resolver.

## O-3. Qué se busca, y por qué eso cambia a quién corresponde el control

Esta amenaza tiene dos objetivos observados que conviven y que no exigen el mismo control.

**El primero es la credencial bancaria.** El `Cluster 4` de Recorded Future es phishing dirigido a clientes de Davivienda, Bancolombia y BBVA, y hasta marzo de 2024 hubo un directorio abierto con carpetas por banco. Acronis describe el robo de credenciales de banca como objetivo declarado de su campaña, y las configuraciones de AsyncRAT que publica incluyen comandos para extraer contraseñas de navegador, carteras de criptomonedas (`Wallets`, `Exodus_Chrome`, `Ledger_Live`) y testigos de Discord. Ese riesgo se corta en el flujo de pagos y en la política de gestor de contraseñas del navegador, no en la pasarela de correo.

**El segundo es el acceso persistente a una entidad pública.** Las 28 víctimas que Recorded Future enumera con fecha y C2 son en su mayoría organismos de gobierno colombiano a distintos niveles, y la permanencia observada va de un día a más de un mes —el caso más largo, una víctima de salud, con el mismo C2 desde el 30 de abril hasta el 9 de junio de 2025—. Un troyano de acceso remoto en un organismo público durante cuarenta días no es fraude: es recolección. Qué se recolectó, ninguna fuente lo dice.

**Y hay un tercer mecanismo, que es el que hace de esto un ciclo y no una campaña.** El acceso a un buzón institucional se convierte en el remitente de la siguiente oleada. Es un bucle que se alimenta: cada víctima pública comprometida es, además de víctima, infraestructura de entrega para la siguiente. Eso explica por qué el objetivo es el Estado aunque la monetización parezca bancaria, y explica por qué una organización privada que **recibe** correo del Estado está expuesta aunque no sea objetivo.

**Lo que esto implica para nosotros.** Nuestra exposición no es ser el objetivo: es ser el destinatario. Recibimos notificaciones judiciales, tributarias y municipales reales, y no tenemos forma de distinguir la auténtica de la auténtica-comprometida. Esa es la decisión `E-b`, y es de proceso, no de tecnología.

## O-4. Nuestra exposición

<!-- cti:note type="gap" -->

> ⬛ **Sección sin evaluar — requiere telemetría e inventario internos.** De las once
> preguntas, **X-1, X-2 y X-6 se responden en una tarde** y son las que más cambian la
> postura. Ninguna requiere compra. Es el tercer informe consecutivo en que esta sección
> queda vacía; a estas alturas, la brecha no es de inteligencia, es de encargo.

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| X-1 | ¿Cuántos adjuntos `SVG` entraron por correo en los últimos 90 días, de qué remitentes y a quién? | Pasarela de correo · registro de adjuntos | Seguridad del Correo |
| X-2 | ¿Qué hace hoy nuestra pasarela con un `SVG`: lo entrega, lo analiza, lo reescribe o lo bloquea? | Revisión de configuración | Seguridad del Correo |
| X-3 | ¿Permitimos la descarga desde la red de distribución de Discord, Bitbucket, Paste.ee, Gist y archive.org? ¿Con atribución de proceso? | Proxy · registros de navegación | Redes / SOC |
| X-4 | ¿Detectamos la carga de un ensamblado .NET en memoria desde PowerShell (`Reflection.Assembly::Load`)? | EDR · registro de bloques de script de PowerShell | Ingeniería de Detección |
| X-5 | ¿Tenemos activada la lista de bloqueo de controladores vulnerables de Microsoft, y detectamos la carga de un controlador no firmado por nosotros? | Directiva de integridad de código · EDR | TI / Ingeniería de Detección |
| X-6 | ¿Hay en nuestro parque alguno de los seis troyanos de mercado de §X-1, o tráfico a DNS dinámico (`duckdns.org`, `con-ip.com`, `kozow.com`, `ddns.net`)? | EDR · DNS · proxy | SOC |
| X-7 | ¿Cuántas de nuestras direcciones de correo aparecen en registros de ladrones de credenciales, y qué hacemos cuando aparecen? | Vigilancia de credenciales filtradas | Identidad |
| X-8 | ¿Está deshabilitado por directiva el gestor de contraseñas del navegador para credenciales corporativas? | Directiva de navegador | Identidad |
| X-9 | ¿Existe un procedimiento publicado para verificar una notificación del Poder Judicial o del SII, y cuánta gente lo conoce? | Revisión documental · encuesta | Asuntos Corporativos |
| X-10 | ¿Detectamos la creación de tareas programadas con nombre aleatorio de ocho caracteres, y la escritura invertida de rutas de registro? | EDR · auditoría de registro | Ingeniería de Detección |
| X-11 | ¿Tenemos registro de creación de procesos con línea de comandos y 90 días de retención, imprescindible para §X-3? | Revisión de fuentes del SIEM | Ingeniería de Detección |

## O-5. Cronología

<!-- cti:timeline -->

| Fecha | Hecho | Traza |
|---|---|---|
| `2018` | Primera actividad atribuida a TAG-144 / Blind Eagle, según los antecedentes de Recorded Future | Colombia |
| `2024-03-14` | Último día en que se observa un directorio abierto con carpetas de phishing por banco: Davivienda, Banco Colombia, Banco Caja Social (`Cluster 4`) | Colombia |
| `2024-04` | **Comienza la actividad que SCILabs llamará «Red Akodon»**, según la cita de Recorded Future: suplantación de entidades públicas colombianas con REMCOS, QuasarRAT, AsyncRAT y XWorm | Colombia |
| `2024-05-27` | **SCILabs publica el perfil que crea el nombre «Red Akodon»** y decide seguirlo como actor distinto a pesar del parecido con Blind Eagle. *Informe no leído: el sitio rechaza la lectura automatizada (brecha `G-1`)* | Colombia |
| `2024-08-23` | Se observa una cuenta de Pastebin vinculada a uno de los usuarios de GitHub asociados al actor; los enlaces servían cargas de AsyncRAT alojadas en Bitbucket | Global |
| `2024-10` | Ventana de actividad del `Cluster 2`: nueve víctimas enumeradas entre el 1 y el 31 de octubre, de gobierno, transporte, educación, comercio y petróleo | Colombia |
| `2024-10-31` | ¡Mucho Hacker! documenta el uso de correos de un hospital y de la Rama Judicial colombianos para enviar ficheros `SVG` maliciosos *(citado a través de las dos fuentes primarias)* | Colombia |
| `2025-05-28` | **Un repositorio público de Bitbucket llamado `notificaciones-judiciales2025-2005` acumula más de 170 descargas en las horas siguientes a su publicación.** Alias del publicador: `TheMrHacker` y el genérico `Envio` | Colombia |
| `2025-06-06` | Fecha de la regla YARA que Acronis publica para los `SVG` de la campaña (`crimeware_shadow_vector_svg`, marcada `TLP:CLEAR`) | Global |
| `2025-06-18` | **Acronis TRU publica «Shadow Vector»**: 165 muestras, la cadena completa con `SVG`, carga lateral de DLL, dos controladores vulnerables para escalar privilegios y cargador .NET en memoria. Sin atribución | Colombia |
| `2025-07-01` | Correo de phishing desde `alcaldia@simacota-santander.gov.co`, remitente «probablemente comprometido», con asunto «Cobro por intereses moratorios – Radicado 11001-28-05-03004» y adjunto `SVG` | Colombia |
| `2025-07-21` | Fecha de corte del análisis declarada por Recorded Future | — |
| `2025-08-26` | **Recorded Future / Insikt publica «TAG-144's Persistent Grip on South American Organizations»**: cinco agrupaciones, 28 víctimas enumeradas, once cuentas institucionales comprometidas, y la afirmación de haber encontrado «más evidencia que vincula» TAG-144 con Red Akodon | Colombia · Ecuador |
| `2026-11-16` | Cierre de este informe. **Sin informe público nuevo sobre este conjunto en 2026**, sin resolución de la atribución y sin víctima chilena documentada por ninguna fuente | Chile |

## O-6. Hipótesis alternativas consideradas

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| H1 — Los tres nombres describen actividad de un mismo ecosistema de operadores hispanohablantes con acceso al mismo mercado de herramientas y al mismo conocimiento institucional colombiano | Consistente con las dos fuentes primarias: mismo señuelo judicial, mismo método del `SVG`, mismo nombre de método `VAI` en el cargador, mismos servicios de alojamiento, mismas familias. Explica la convergencia sin exigir un mando único | `Retenida` |
| H2 — Red Akodon es un subconjunto de TAG-144 y debería fusionarse | Apoyada por la afirmación de Insikt de «más evidencia que vincula», y por el enlace concreto de un XWorm crackeado. **Pero Insikt no cierra la fusión y SCILabs la rechazó explícitamente teniendo el dato delante.** No se adopta por respeto a la delimitación de sus autores | `Posibilidad real · 45–55 %` |
| H3 — Son actores distintos que comparten proveedor de herramientas y de criptador | Igual de compatible con la evidencia que H2, y más compatible con el hecho de que el arsenal sea íntegramente comercial: compartir AsyncRAT no vincula a nadie. **Inconsistencia:** no explica la coincidencia del nombre de método `VAI` ni la del patrón de esteganografía | `Posibilidad real · 45–55 %` |
| H4 — El conjunto se traducirá a otro país de la región, Chile incluido, en los próximos doce meses | Sin evidencia directa. Apoyada por el coste marginal del cambio —redactar el señuelo— y por el precedente del ecosistema brasileño, que localiza por país desde 2019. Es el juicio más consecuente para nosotros y el más débilmente sostenido | `Posibilidad real · 45–55 %` |
| H5 — Quien redacta el señuelo y quien opera el implante son la misma persona | **Sin evidencia a favor y con un contraargumento económico fuerte:** en esta región existe un mercado de capas, y la fluidez institucional se contrata igual que el criptador. Se consigna sin resolver porque determina si el actor es «colombiano» o solo «con acceso a Colombia» | `Retenida sin resolver` |
| H6 — El objetivo final es el acceso corporativo para revenderlo a grupos de extorsión | **Sin evidencia.** Ninguna fuente documenta el puente. Se consigna para que no se reabra sin dato nuevo, y porque el indicador `I-7` lo vigila | `Descartada por ahora` |

**Supuesto clave.** Que el canal de entrega seguirá siendo el correo electrónico con adjunto o enlace, sobre Windows de escritorio. **Si es falso** —si el señuelo judicial se traslada a WhatsApp, como ya hizo el ecosistema brasileño que describe `CTI-2026-021`, o a aplicación móvil— entonces la decisión `E-a` sobre los `SVG` pierde la mitad de su valor y la defensa se desplaza a un canal donde no tenemos ni pasarela ni cabeceras ni autoridad.

**Pre-mortem.** Es mayo de 2027 y este informe resultó equivocado. Los tres finales más probables: **(1)** bloqueamos los `SVG` y el compromiso llegó por un `PDF` con enlace desde el buzón auténtico de un organismo público, porque el formato era lo accesorio y el remitente legítimo era lo esencial —y la decisión `E-c`, que era de criterio, se quedó en el acta—; **(2)** acertamos en el correo y la pérdida vino por un empleado al que le robaron la credencial corporativa guardada en el navegador personal, es decir por `E-f`, que dependía de Identidad y no de seguridad del correo; **(3)** dedicamos el esfuerzo a Colombia y el golpe vino traducido a otro país de la región donde tenemos filial y no hicimos ni la formación ni la tabla de equivalencias.

## O-7. Indicadores y señales de alerta

| # | Indicador observable | Qué señalaría | Disciplina | Responsable |
|---|---|---|---|---|
| I-1 | **Señuelo judicial o tributario chileno con adjunto `SVG`**, o remitente `.gob.cl` / `.cl` institucional legítimo distribuyendo uno de los seis troyanos | Convierte KJ-7 de proyección en hecho; obliga a revisión anticipada y a ejecutar `E-a` y `E-b` sin esperar plazo | OSINT · pasarela de correo | Célula CTI / SOC |
| I-2 | Resolución pública de la atribución por un proveedor con telemetría | Cierra KJ-5; permite consolidar listas de indicadores y dejar de contar dos veces | OSINT comercial | Célula CTI |
| I-3 | Aparición de una de **nuestras** direcciones de correo en registros de ladrón de credenciales | Es el mecanismo exacto por el que una organización se convierte en el remitente auténtico de la campaña siguiente | Vigilancia de credenciales | Identidad |
| I-4 | Dominio de DNS dinámico nuevo que siga alguno de los cuatro patrones de nomenclatura de §O-1 | Infraestructura nueva del mismo conjunto; permite bloqueo anticipado antes de la campaña | OSINT · DNS pasivo | Célula CTI |
| I-5 | Uso de un servicio legítimo de alojamiento **nuevo** en la cadena (no Discord, Bitbucket, Paste.ee, Gist, archive.org) | El actor rota de servicio cuando uno se le cierra; detectarlo pronto conserva la validez de `D-6` | OSINT comercial | Célula CTI |
| I-6 | Campaña del mismo conjunto con señuelo de **nuestra** marca en contexto de factura, notificación o cobro | Materializa la cara reputacional; activa denuncia y comunicación a clientes | Vigilancia de marca | Asuntos Corporativos |
| I-7 | Venta de acceso corporativo latinoamericano en foros, atribuida a infección por uno de estos troyanos | Materializaría el puente al ransomware que hoy no está documentado (`H6`) | OSINT · foros criminales | Célula CTI |
| I-8 | Aparición del método del `SVG` combinado con el gusano de WhatsApp de `CTI-2026-021` | Rompería el supuesto clave de §O-6 y trasladaría la defensa fuera de nuestro perímetro | OSINT comercial | Célula CTI |

---

# NIVEL TÁCTICO
### Para: Analistas de SOC · Ingeniería de Detección · Threat Hunting · Horizonte: días–semanas

## T-1. Cadena de intrusión

<!-- cti:stages title="Cuatro etapas, y las tres primeras se apoyan en algo auténtico" dwell="next" -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 01 · Remitente | El correo que es verdadero | Mensaje desde una **cuenta institucional legítima comprometida** —Rama Judicial, alcaldía, gobernación, secretaría de educación, hospital— con asunto de cobro o de notificación judicial, con radicado de formato correcto · SPF, DKIM y DMARC validan · adjunto `SVG` o enlace · en la variante antigua, adjunto comprimido con doble extensión (`RELACIÓN DE SALDOS - CUENTA DE COBRO.pdf.exe`) |
| Etapa 02 · Señuelo | La citación que se abre en el navegador | El `SVG` se renderiza como un resumen de proceso judicial maquetado, con nombre de juzgado, radicado y **la contraseña del archivo comprimido que vendrá después** · enlace a la etapa siguiente alojada en un servicio legítimo: red de distribución de Discord, repositorio público de Bitbucket, Paste.ee, GitHub Gist, Google Drive, Dropbox · 141 muestras `SVG` publicadas de una sola campaña · ficheros `JS` o `VBS` con nombres como `_001-Notificacion_electronica_demanda_judicial_Departamento_Juridico.js` |
| Etapa 03 · Cargador | Servicios legítimos, memoria y ningún binario propio | Tres variantes documentadas. **(a) Carga lateral de DLL:** `ZIP` protegido con contraseña con un ejecutable señuelo (`vcredist.exe`), una DLL legítima (`libbrotlicommon.dll`, `CiscoSparkLauncher.dll`) y una maliciosa (`mscorlib.dll` falsa, `VERSION.dll`), con vaciado de proceso sobre `AddInProcess32.exe`. **(b) Controlador vulnerable:** deja en `%Temp%` dos `.sys` legítimos y vulnerables, los arranca como servicio y llama a `DeviceIoControl` con `0x80002010` para autenticar su propio `svchost.exe`. **(c) Sin fichero:** `JS` → PowerShell oculto (`-nop -w hidden`) → descarga de un `JPEG` de **archive.org** con la carga en base64 escondida tras el marcador de fin de imagen o entre `INICIO>>` y `<<FIM>>` → `[Reflection.Assembly]::Load()` y llamada al método `VAI` |
| Etapa 04 · Implante | Un troyano de tienda y una persistencia barata | `AsyncRAT`, `REMCOS`, `QuasarRAT` / `BlotchyQuasar`, `XWorm`, `DcRAT` o `LimeRAT` · mando y control sobre **DNS dinámico gratuito** (`duckdns.org`, `con-ip.com`, `kozow.com`, `ddns.net`) o VPS y VPN comercial · persistencia por tarea programada con nombre aleatorio (`Yt4Bvc2G`), por clave `Run` escrita **con la ruta invertida** para ocultarla, o por acceso directo en el menú de inicio *(esto último según la cita del informe de SCILabs)* · robo de contraseñas de navegador, carteras de criptomonedas, testigos de Discord · terminación de más de noventa procesos de productos de seguridad · anti-máquina virtual por fabricante, depurador y tamaño de disco |

**Permanencia:** de un día a más de cuarenta. Recorded Future enumera 28 víctimas con fechas de primera y última observación: la más corta, un solo día; la más larga, una organización de salud con el mismo C2 desde el 30 de abril hasta el 9 de junio de 2025. No hay cifra media publicada.

<!-- cti:note type="info" -->

> **Dónde se rompe la cadena más barato.** La **etapa 01 no se rompe con autenticación de
> remitente** y hay que dejar de esperar que lo haga: se rompe con proceso —un
> procedimiento de verificación— y con análisis de adjunto. La **etapa 02 se rompe con una
> decisión de política sobre un tipo de fichero**, que es la intervención de mejor
> relación coste-efecto de todo el informe: un `SVG` entrante tiene usos legítimos
> contables con los dedos de una mano en una organización no creativa. La **etapa 03 se
> rompe con dos controles de plataforma** —lista de bloqueo de controladores vulnerables y
> registro de bloques de script de PowerShell—, ninguno de los cuales cuesta licencia. La
> **etapa 04 ya es respuesta a incidentes**: si el troyano corre, las credenciales salen.

## T-2. Mapa MITRE ATT&CK

<!-- cti:matrix -->

| Táctica | ID | Técnica | Procedimiento observado |
|---|---|---|---|
| Desarrollo de recursos | T1583.001 | Acquire Infrastructure: Domains | Más de doscientos dominios de DNS dinámico con cuatro patrones de nomenclatura distintos |
| Desarrollo de recursos | T1583.003 | Acquire Infrastructure: Virtual Private Server | VPS en AS198953, AS40021, AS42708, AS20473 |
| Desarrollo de recursos | T1583.004 | Acquire Infrastructure: Server | Servidores proxy en AS36352 |
| Desarrollo de recursos | T1583.008 | Acquire Infrastructure: Malvertising | Consignada por Recorded Future en su propio mapeo |
| Desarrollo de recursos | T1584.004 | Compromise Infrastructure: Server | Infraestructura en ISP colombianos; indicios de un enrutador MikroTik comprometido como proxy, **no confirmado por la fuente** |
| Desarrollo de recursos | T1586.002 | Compromise Accounts: Email Accounts | **Once cuentas de correo institucionales colombianas legítimas usadas como remitente** |
| Desarrollo de recursos | T1588.002 | Obtain Capabilities: Tool | Seis familias de troyano comercial o de código abierto, varias pirateadas; criptadores `Roda`, `HeartCrypt`, `PureCrypter` |
| Acceso inicial | T1566.001 | Phishing: Spearphishing Attachment | Adjunto `SVG` con la citación judicial; en la variante antigua, comprimido con doble extensión |
| Acceso inicial | T1566.002 | Phishing: Spearphishing Link | Enlace a `ZIP` protegido con contraseña alojado en servicio legítimo |
| Ejecución | T1204.001 | User Execution: Malicious Link | La víctima abre el enlace del `SVG` |
| Ejecución | T1204.002 | User Execution: Malicious File | La víctima ejecuta el contenido del comprimido |
| Ejecución | T1059.001 | Command and Scripting Interpreter: PowerShell | PowerShell con `-nop -w hidden` e `Invoke-Expression` sobre contenido descargado |
| Ejecución | T1059.005 | Command and Scripting Interpreter: Visual Basic | Droppers `VBS` alojados en Bitbucket |
| Ejecución | T1059.007 | Command and Scripting Interpreter: JavaScript | Dropper `JS` servido desde la red de distribución de Discord y Paste.ee |
| Persistencia | T1053.005 | Scheduled Task/Job: Scheduled Task | `schtasks /create /tn "Yt4Bvc2G" /tr ... /sc onlogon /rl highest /f` |
| Persistencia | T1547.001 | Boot or Logon Autostart: Registry Run Keys | Clave `Run` con la ruta **escrita invertida** en el código para ocultarla |
| Persistencia | T1547.009 | Boot or Logon Autostart: Shortcut Modification | Acceso directo en el menú de inicio *(según la cita del informe de SCILabs)* |
| Escalada de privilegios | T1068 | Exploitation for Privilege Escalation | Dos controladores legítimos vulnerables: WiseCleaner (`CVE-2023-1486`) y Zemana (`CVE-2022-42045`) |
| Escalada de privilegios | T1543.003 | Create or Modify System Process: Windows Service | Los dos controladores se registran y arrancan como servicio de núcleo |
| Escalada de privilegios | T1548.002 | Abuse Elevation Control Mechanism: Bypass UAC | Elusión por `cmstp.exe` en el cargador .NET, activable por configuración |
| Evasión | T1027.017 | Obfuscated Files or Information: SVG Smuggling | **Técnica central del informe.** Adjunto `SVG` que el navegador interpreta; añadida al marco en 2025 |
| Evasión | T1027.009 | Obfuscated Files or Information: Embedded Payloads | Carga en base64 tras el marcador de fin de un `JPEG`, o en los píxeles de la imagen |
| Evasión | T1027.013 | Obfuscated Files or Information: Encrypted/Encoded File | `ZIP` protegido con contraseña, con la contraseña en el `SVG` o en el cuerpo del correo |
| Evasión | T1140 | Deobfuscate/Decode Files or Information | Base64, XOR con dos claves de 16 bytes, Unicode y ofuscación con emoticonos en los scripts |
| Evasión | T1574.002 | Hijack Execution Flow: DLL Side-Loading | `libbrotlicommon.dll` y `CiscoSparkLauncher.dll` legítimas cargando `mscorlib.dll` y `VERSION.dll` maliciosas |
| Evasión | T1055.012 | Process Injection: Process Hollowing | `AddInProcess32.exe` creado suspendido y vaciado. **Técnica enlazada por Acronis** |
| Evasión | T1620 | Reflective Code Loading | `[Reflection.Assembly]::Load()` y llamada al método `VAI`, sin escritura en disco |
| Evasión | T1562.001 | Impair Defenses: Disable or Modify Tools | Lista de terminación con más de noventa procesos de productos de seguridad |
| Evasión | T1497 | Virtualization/Sandbox Evasion | Fabricante con `VIRTUAL`, `vmware`, `VirtualBox`; `CheckRemoteDebuggerPresent`; `SbieDll.dll`; disco menor de 61 GB; comprobación de Windows XP |
| Evasión | T1112 | Modify Registry | Consignada por Recorded Future en su propio mapeo |
| Evasión | T1036.007 | Masquerading: Double File Extension | `RELACIÓN DE SALDOS - CUENTA DE COBRO.pdf.exe` |
| Acceso a credenciales | T1555.003 | Credentials from Password Stores: Web Browsers | Comandos `WebBrowserPass`, `passload`, `Chrome`, `Fox` en la configuración de AsyncRAT |
| Acceso a credenciales | T1056.001 | Input Capture: Keylogging | `klget` y tamaño máximo de registro de pulsaciones en la configuración de REMCOS |
| Descubrimiento | T1082 | System Information Discovery | Consignada por Recorded Future en su propio mapeo |
| Descubrimiento | T1012 | Query Registry | Consignada por Recorded Future en su propio mapeo |
| Colección | T1113 | Screen Capture | Comando `getscreen`; intervalo de captura configurable en REMCOS |
| Colección | T1115 | Clipboard Data | Capacidad estándar de las seis familias |
| Mando y control | T1071.001 | Application Layer Protocol: Web Protocols | HTTP y HTTPS contra DNS dinámico y VPS |
| Mando y control | T1102 | Web Service | **Discord CDN, Bitbucket, GitHub Gist, Paste.ee, Pastebin, archive.org, Google Drive, Dropbox, Tagbox, alojamiento gratuito** |
| Mando y control | T1105 | Ingress Tool Transfer | Descarga de la carga final en tiempo de ejecución |
| Mando y control | T1573.001 | Encrypted Channel: Symmetric Cryptography | Configuración de AsyncRAT cifrada con AES y clave en base64 incrustada; RC4 en la configuración de REMCOS |
| Mando y control | T1573.002 | Encrypted Channel: Asymmetric Cryptography | Consignada por Recorded Future en su propio mapeo |
| Mando y control | T1219 | Remote Access Software | Comando `anydesk` en la configuración de AsyncRAT |
| Exfiltración | T1041 | Exfiltration Over C2 Channel | Credenciales, capturas y registro de pulsaciones por el canal del troyano |

<!-- cti:note type="warn" -->

> ⚠ **Procedencia del mapeo, porque aquí hay que ser estricto.** Recorded Future publica
> su propia tabla, corta: `T1071.001`, `T1573.002`, `T1573.001`, `T1105`, `T1112`,
> `T1082`, `T1012`, `T1059.001`, `T1566.002`, `T1583.001`, `T1583.003`, `T1583.004`,
> `T1583.008` y `T1584.004`. Acronis **no publica tabla** y enlaza solo dos técnicas en el
> cuerpo: `T1027.017` y `T1055.012`. **Todo lo demás de esta tabla es traducción nuestra
> de procedimientos descritos en prosa**, y debe tratarse como tal: es útil para
> construir detección y para medir cobertura, y no debe citarse como si lo hubiera
> publicado el proveedor.

## T-3. Dónde atacamos en la Pirámide del Dolor

<!-- cti:pyramid -->

| Nivel | Qué contiene en este informe y qué vale | Valor |
|---|---|---|
| Hashes | 165 de Acronis, más una docena de Recorded Future, de los que aquí se recoge una selección. **Valor casi nulo para prevenir:** 141 son `SVG` «posiblemente generados en lote», según el comentario de la propia regla YARA de Acronis, de modo que cada campaña nueva produce ciento cuarenta hashes nuevos. Sirven para retrohunt y para confirmar un caso | Base · valor trivial |
| IP · Dominios | Más de doscientos dominios de DNS dinámico gratuito y un centenar de direcciones. **Rotan a voluntad y el coste de un dominio nuevo es cero.** Buena parte de las direcciones son de VPN comercial compartida y de ISP colombianos: bloquearlas castiga a terceros. Lo que sí vale es **el patrón de nomenclatura** y el proveedor de DNS dinámico, no el dominio concreto | Valor bajo |
| Artefactos | **Lo más duradero que ha publicado este conjunto.** Mutex `AsyncMutex_6SI8OkPnk`; la marca `CRACKED BY hxxps://t[.]me/xworm_v2` en la configuración; el nombre de método `VAI`; la tarea `Yt4Bvc2G`; la clave `Run` escrita invertida; los marcadores `INICIO>>` y `<<FIM>>`; la cabecera de 54 bytes del `JPEG`; el código `0x80002010`; los nombres de DLL `libbrotlicommon.dll`, `CiscoSparkLauncher.dll`, `VERSION.dll`, `mscorlib.dll` falsa; los nombres de fichero en español con «Notificacion_electronica» | Valor medio |
| Herramientas | Seis troyanos de mercado, dos controladores legítimos vulnerables, `cmstp.exe`, `AddInProcess32.exe`, `schtasks`, PowerShell, y ocho servicios legítimos de Internet. **Todas legítimas o de venta libre.** Se detectan por contexto, por ruta y por relación padre-hijo, nunca por nombre | Valor alto |
| TTP | Adjunto `SVG` entrante; remitente institucional auténtico con contenido de cobro o notificación; `ZIP` con contraseña publicada en el señuelo; descarga de imagen desde archive.org por un proceso que no es navegador; ensamblado .NET cargado en memoria desde PowerShell; controlador no aprobado cargado desde `%Temp%`. **Seis comportamientos que cubren las tres variantes y la cuarta que venga, con cualquier nombre que le pongan** | Cima · valor máximo |

## T-4. Hipótesis de caza prioritarias

<!-- cti:accordion critical="^(H-1|H-2|H-3|H-4)\b" regional="^(H-11|H-12)\b" -->

**H-1 — Adjunto `SVG` entrante, y qué pasó después.** Correos con adjunto `.svg` recibidos en los últimos 90 días, cruzados con la actividad del destinatario en los diez minutos siguientes: navegación a servicio de alojamiento, descarga de comprimido, creación de proceso. Fuente: pasarela de correo con registro de adjuntos, proxy, EDR. **Es la hipótesis madre de este informe:** el `SVG` es el vehículo en las dos fuentes primarias, con 141 muestras de una sola campaña. Fidelidad esperada muy alta en una organización no creativa, donde el volumen base de `SVG` entrantes es casi nulo. Falsos positivos conocidos: firmas gráficas, material de marketing, documentación de ingeniería; exceptuables por remitente y por área.

**H-2 — Correo de remitente institucional con contenido de cobro o notificación judicial y adjunto o enlace.** Mensajes cuyo remitente pertenezca a un dominio de gobierno o de administración de justicia —`.gov.co`, `.gob.cl`, `.gob.*`, `pjud.cl`, `sii.cl`, `tgr.cl`— y cuyo asunto contenga términos de radicado, demanda, cobro, notificación, citación o requerimiento, **combinados con adjunto o con enlace a servicio de alojamiento**. Fuente: pasarela de correo. **Esta hipótesis es deliberadamente incómoda porque marca correo auténtico**, y es el precio de KJ-1: el remitente es verdadero. No se debe convertir en bloqueo; se debe convertir en etiqueta visible para el usuario y en cola de revisión. Fidelidad baja, valor alto.

**H-3 — Ensamblado .NET cargado en memoria desde PowerShell.** Bloques de script que contengan `Reflection.Assembly`, `[System.Reflection.Assembly]::Load`, `FromBase64String` o la invocación de un método llamado `VAI`, y procesos de PowerShell lanzados con `-nop`, `-w hidden`, `-enc` o `-e`. Fuente: registro de bloques de script de PowerShell (`4104`), creación de procesos. **Es el punto común de las tres variantes de cargador y el único paso que ninguna de ellas puede evitar.** Fidelidad alta; requiere exceptuar herramientas internas de administración por firma y por ruta, nunca por patrón.

**H-4 — Controlador no aprobado cargado desde una ruta escribible por el usuario.** Carga de un `.sys` desde `%Temp%`, `%AppData%` o el perfil del usuario, o creación de un servicio de núcleo apuntando a esas rutas, con nombre de fichero aleatorio. Añadir específicamente los dos controladores conocidos de WiseCleaner y Zemana. Fuente: eventos de carga de controlador del EDR, creación de servicios, directiva de integridad de código. **Es la escalada de privilegios de la variante más capaz, y es también la que más daño permite: un controlador en el núcleo apaga lo que quiera.** Fidelidad extremadamente alta: en una estación de trabajo gestionada esto no tiene equivalente legítimo.

**H-5 — Descarga de imagen desde archive.org o Paste.ee por un proceso que no es navegador.** Peticiones a `archive.org`, `paste.ee`, `pastebin.com`, `gist.githubusercontent.com`, `cdn.discordapp.com` o `bitbucket.org` originadas por `powershell.exe`, `wscript.exe`, `cscript.exe`, `mshta.exe` o un proceso sin firma. Fuente: proxy con atribución de proceso. **La señal no está en el destino —son servicios legítimos— sino en quién los pide.** Fidelidad alta donde haya atribución de proceso; sin ella, la hipótesis degenera en una lista de servicios populares e inservible.

**H-6 — Imagen con carga incrustada tras el marcador de fin.** Ficheros `JPEG` o `PNG` descargados cuyo tamaño exceda notablemente el de la imagen declarada, o que contengan tras el marcador de fin de imagen una secuencia base64 larga, o los marcadores `INICIO>>` y `<<FIM>>`. Fuente: inspección de contenido en el proxy, análisis de ficheros del EDR. **Es la técnica de esteganografía que las dos fuentes primarias describen por separado**, con marcadores distintos, lo que sugiere variantes del mismo kit. Fidelidad media-alta; coste de implementación dependiente del producto.

**H-7 — Carga lateral de DLL desde un directorio de usuario.** Procesos que carguen `libbrotlicommon.dll`, `CiscoSparkLauncher.dll`, `VERSION.dll` o un fichero llamado `mscorlib.dll` desde `%Temp%`, `%AppData%` o una carpeta de descargas, especialmente si el proceso padre descomprimió un archivo poco antes. Añadir la señal de `AddInProcess32.exe` creado suspendido. Fuente: eventos de carga de imagen del EDR, creación de procesos. **`mscorlib.dll` fuera del directorio de .NET no es una biblioteca de .NET:** es la señal más específica y más barata de toda la variante (a). Fidelidad muy alta.

**H-8 — Tarea programada con nombre aleatorio creada al iniciar sesión con privilegio máximo.** Creación de tareas mediante `schtasks /create` con `/sc onlogon` y `/rl highest`, cuyo nombre sea una cadena alfanumérica corta sin significado, apuntando a un ejecutable en `%AppData%\Roaming` o en una ruta de usuario. Fuente: creación de procesos con línea de comandos, registro de tareas programadas. **El ejemplo publicado, `Yt4Bvc2G`, no es el indicador: el indicador es el patrón «nombre sin sentido, al iniciar sesión, privilegio máximo, ruta de usuario».** Fidelidad muy alta.

**H-9 — Clave de ejecución automática escrita con la ruta invertida.** Presencia en el código de un proceso en ejecución, o en su cadena de comandos, de la cadena `\\nuR\\noisreVtenrretnuC\\swodniW\\tfosorciM\\erawtfoS` o cualquier inversión reconocible de una ruta de registro conocida. Fuente: cadenas en memoria del EDR, análisis de muestra. **Es una técnica de evasión de análisis estático trivial y por eso mismo un artefacto excelente:** nada legítimo escribe una ruta de registro al revés. Fidelidad extremadamente alta, cobertura dependiente de la telemetría de memoria.

**H-10 — Tráfico a proveedores de DNS dinámico con los patrones de nomenclatura conocidos.** Resoluciones y conexiones a `duckdns.org`, `con-ip.com`, `kozow.com`, `ddns.net`, `ip-ddns.com`, `writesthisblog.com`, `lovestoblog.com`, y en particular a nombres que casen `envio[0-9\-]{2,5}`, `deadpoolstart\d{4}`, nombre y apellido español seguido de dígitos, o palabra en español con mes o año. Fuente: DNS, cortafuegos, proxy. **El dominio concreto no vale nada; el patrón vale bastante**, y el proveedor de DNS dinámico en una estación de trabajo corporativa casi nunca tiene justificación. Fidelidad media-alta.

**H-11 — Nombres de fichero en español con la fórmula administrativa de la notificación.** Ficheros creados o descargados cuyo nombre contenga `Notificacion_electronica`, `demanda_judicial`, `Departamento_Juridico`, `sentencia_preliminar`, `DEMANDA LABORAL`, `notificaciones-judiciales`, `CUENTA DE COBRO`, `RELACIÓN DE SALDOS`, o sus equivalentes chilenos del Anexo D. Fuente: creación de ficheros, registro de descargas del proxy. **Es la hipótesis que convierte este informe en algo aplicable a Chile:** la fórmula administrativa cambia de país, la estructura no. Fidelidad alta; coste de implementación nulo.

**H-12 — `ZIP` protegido con contraseña cuya contraseña viene en el propio mensaje.** Comprimidos cifrados recibidos o descargados, correlacionados con la aparición de una cadena corta alfanumérica en el cuerpo del correo o en un adjunto `SVG`. Fuente: pasarela de correo, análisis de adjuntos. **El comprimido con contraseña publicada en el señuelo existe para una sola cosa: que el motor de análisis no pueda abrirlo y el usuario sí.** Fidelidad alta; conviene tratarlo como categoría de política, no como detección puntual.

**H-13 — Terminación masiva de procesos de productos de seguridad.** Un proceso que intente terminar o detener varios servicios de productos de seguridad en una ventana corta, con la lista de más de noventa nombres que publica Acronis. Fuente: EDR con protección contra manipulación, eventos de terminación de proceso. **Si esta hipótesis dispara, ya es respuesta a incidentes y no caza.** Fidelidad extremadamente alta; exige que la protección contra manipulación esté activa y gestionada centralmente, lo que es la mitigación de §X-5.

**H-14 — Nuestras direcciones de correo en registros de ladrón de credenciales.** Aparición de direcciones corporativas, y en especial de buzones funcionales y de áreas que tratan con el Estado, en registros de ladrones de información. Fuente: vigilancia de credenciales filtradas. **No es una hipótesis de caza en el host, es la hipótesis que evita que seamos el remitente auténtico de la campaña siguiente.** Recorded Future encontró así una de las cuentas judiciales comprometidas. Fidelidad alta, propiedad de Identidad y no del SOC.

## T-5. Brechas de visibilidad que hay que cerrar primero

| Brecha | Por qué importa aquí |
|---|---|
| Pasarela de correo sin registro de tipo de adjunto ni retención de 90 días | Deja ciegas `H-1`, `H-2` y `H-12`, es decir la etapa 01 y la etapa 02 completas. Es la brecha más determinante del informe |
| Registro de bloques de script de PowerShell deshabilitado | Deja ciega `H-3`, el único paso común a las tres variantes de cargador. Es un ajuste de directiva, sin coste |
| Proxy sin atribución de proceso | Degrada `H-5` y `H-10` a listas de servicios legítimos y de proveedores de DNS gratuito, inservibles para alertar |
| Sin telemetría de carga de controladores ni lista de bloqueo de controladores vulnerables | Deja ciega `H-4`, la escalada de privilegios de la variante más capaz, y permite que un controlador vulnerable firmado apague el EDR |
| Registro de línea de comandos en creación de procesos deshabilitado | Deja ciegas `H-8` y buena parte de `H-3` y `H-7` |
| Sin inspección de contenido de imágenes descargadas | Deja ciega `H-6` y con ella el canal de entrega de la carga final en la variante sin fichero |
| Sin vigilancia de credenciales filtradas con procedimiento de reposición | Deja ciega `H-14` y mantiene abierto el mecanismo exacto de KJ-1 |
| Protección contra manipulación del EDR sin gestión central | Deja ciega `H-13` y permite que la lista de terminación de noventa procesos funcione |
| Sin tabla de equivalencias institucionales en formación y en detección | Deja `H-11` sin términos chilenos, es decir con la hipótesis escrita y sin aplicar. El Anexo D cierra esta brecha hoy |

---

# NIVEL TÉCNICO
### Para: Ingeniería de detección · Automatización · TIP/SIEM · Vida útil: semanas–meses

## X-1. Arsenal y capacidad del conjunto

| Propiedad | Valor |
|---|---|
| Familias de implante | `AsyncRAT` (incluida la versión `1.0.7` y variantes crackeadas), `REMCOS`, `QuasarRAT` en la variante `BlotchyQuasar`, `XWorm`, `DcRAT`, `LimeRAT`. Los antecedentes de Recorded Future añaden `njRAT` y `BitRAT` al repertorio histórico del actor mayor |
| Desarrollo propio | **Ninguno documentado.** Lo propio es el señuelo, la cadena de entrega y la infraestructura |
| Criptadores | `Roda` (observado sobre muestras de AsyncRAT); los antecedentes citan `HeartCrypt`, `PureCrypter`, `pjoao1578` y `CryptersAndTools`, este último **brasileño**, que es el mismo mercado que describe `CTI-2026-021` |
| Cargadores | Tres variantes: carga lateral de DLL con vaciado de proceso; controlador vulnerable para escalada; cargador .NET en memoria compatible con lo que Acronis describe como «Katz Loader» |
| Ejecutores legítimos | `powershell.exe`, `wscript.exe`, `mshta.exe`, `cmstp.exe` (elusión de UAC), `AddInProcess32.exe` (objetivo de vaciado), `schtasks.exe`, `msiexec` no observado en este conjunto |
| Bibliotecas legítimas abusadas | `libbrotlicommon.dll`, `CiscoSparkLauncher.dll`, y una `mscorlib.dll` falsa con **nueve bytes insertados antes de la cabecera PE** para romper el análisis automático |
| Controladores vulnerables | WiseCleaner (`VFZE6ksYnpPfSnEWUNg.sys`, `CVE-2023-1486`) y Zemana (`cuDX73ob9SxeAS0IdV.sys`, `CVE-2022-42045`), arrancados como servicio de núcleo; `DeviceIoControl` con código `0x80002010` para autenticar el proceso propio |
| Servicios legítimos de Internet usados como infraestructura | Red de distribución de **Discord**, **Bitbucket**, **GitHub Gist**, **Paste.ee**, **Pastebin**, **archive.org**, **Google Drive**, **Dropbox**, **Tagbox**, alojamiento gratuito `lovestoblog.com` (InfinityFree), acortadores `cort.as`, `acortaurl.com`, `gtly.to`, y canales de **Telegram** para la distribución de herramientas crackeadas |
| Resolución del C2 | DNS dinámico gratuito con cuatro patrones de nomenclatura; VPS europeos y norteamericanos; **servidores de VPN comercial** (TorGuard, AS9009) usados como punto de mando, lo que mezcla el tráfico del actor con el de clientes legítimos del servicio |
| Criptografía | AES con clave en base64 incrustada en la configuración de AsyncRAT (clave observada `zZ5OP9zoIeGTxRmoYxR6XEu0yUxV6wAE`); RC4 con el tamaño de clave en el primer byte del recurso en REMCOS; XOR con dos claves de 16 bytes en el cargador; base64 sobre Unicode y emoticonos en los scripts |
| Puertos observados | `7788` en una configuración de AsyncRAT. **Ninguna fuente publica más puertos**, de modo que no se puede detectar por puerto |
| Evasión de análisis | Fabricante del sistema con `VIRTUAL`, `vmware` o `VirtualBox`; `CheckRemoteDebuggerPresent`; manejador de `SbieDll.dll` (Sandboxie); disco menor de 61 000 000 000 bytes; comprobación de Windows XP; `Environment.FailFast()` al detectar; ofuscación de flujo de control con saltos y comparaciones inútiles |
| Evasión de defensas | Lista de terminación con más de noventa procesos de productos de seguridad (ESET, Avast, AVG, McAfee, AhnLab, ALYac, 360, Qihoo, `MsMpEng`, `NisSrv`, `smartscreen`, `MpDefenderCoreService`…); modificación del fichero `hosts` mediante los comandos `ResetHosts` y `Block` |
| Robo de información | Contraseñas de navegador (`WebBrowserPass`, `passload`), carteras de criptomonedas y extensiones (`Meta_Chrome`, `Exodus_Chrome`, `Ledger_Live`), testigos de Discord, registro de pulsaciones, capturas de pantalla con intervalo configurable, audio |
| Geocerca | Los antecedentes de Recorded Future describen geocercas que **bloquean el acceso desde fuera de Colombia o Ecuador y redirigen al visitante a sitios web oficiales del gobierno**, citando a otros proveedores |
| Lo que **no** tiene | Cifrador de extorsión, capacidad destructiva, explotación de días cero, desarrollo propio de implante, movimiento lateral clásico documentado, actividad en entornos industriales |

<!-- cti:note type="info" -->

> **Lo que este cuadro dice de la defensa.** Hay una asimetría que conviene nombrar: el
> adversario no tiene **ninguna** capacidad que nosotros podamos atacar en su origen. No
> hay taller que desmantelar, no hay implante propio que firmar, no hay día cero que
> parchear. Todo lo que usa se compra, se alquila o es gratis. En consecuencia, **toda la
> defensa útil está en nuestro lado del cable**: en la política de adjuntos, en la
> atribución de proceso en el proxy, en el registro de PowerShell y en la lista de
> bloqueo de controladores. Es una mala noticia para quien esperaba comprar la solución y
> una buena para quien pueda cambiar cuatro ajustes de configuración esta semana.

## X-2. Artefactos persistentes entre versiones

<!-- cti:cards -->

| Categoría | Artefactos | Etiqueta |
|---|---|---|
| Configuración de AsyncRAT | Clave AES `zZ5OP9zoIeGTxRmoYxR6XEu0yUxV6wAE` · mutex `AsyncMutex_6SI8OkPnk` · puerto `7788` · marca de versión `\| CRACKED BY https://t[.]me/xworm_v2` | `configuración` |
| Mutex de otras familias | `tempcookieess` · `tempcokies` · `tempcookiee` · `WinCookies` · `Cookies` · `CookiesGoogleChrome` (AsyncRAT del `Cluster 2`) · `1e97ead369` (LimeRAT del `Cluster 5`) | `host` |
| Cargador .NET | Método de entrada `VAI` · parámetros observados `MSBuild`, `C:\Users\Public\Downloads`, `js`, `duparted`, `creels`, `backticks`, `2` · cadenas en portugués `Extensão não suportada`, `Recurso 'UAC.dll' não encontrado!`, `Erro ao executar a DLL em memória` · parámetros `caminhovbs`, `persitencia`, `extenção`, `nomedoarquivo` | `código` |
| Esteganografía | Marcadores `INICIO>>` y `<<FIM>>` · cabecera de 54 bytes que comienza `0x42 0x4D 0x72 0x6E 0x37` · carga base64 tras el marcador de fin de un `JPEG` · ruta `archive[.]org/replace_202505/REPLACE[.]txt` | `red` |
| Carga lateral y vaciado | `libbrotlicommon.dll` (`BrotliEncoderCreateInstance`) · `CiscoSparkLauncher.dll` (`GetFileVersionInfoSizeW`) · `VERSION.dll` maliciosa · `mscorlib.dll` con **nueve bytes antes de la cabecera PE** · `AddInProcess32.exe` como objetivo de vaciado | `host` |
| Controladores y escalada | `%Temp%\VFZE6ksYnpPfSnEWUNg.sys` · `%Temp%\cuDX73ob9SxeAS0IdV.sys` · `%Temp%\svchost.exe` · código de control `0x80002010` · asignación de 5 982 208 bytes, sección `.rdata` de 5 989 888, salto de los primeros 7 680 | `núcleo` |
| Persistencia | Tarea `Yt4Bvc2G` creada con `/sc onlogon /rl highest /f` · clave `Run` escrita invertida: `\\nuR\\noisreVtenrretnuC\\swodniW\\tfosorciM\\erawtfoS` · ruta observada `C:\Users\DEV\AppData\Roaming\` | `persistencia` |
| Nombres de fichero del señuelo | `Notificacion_electronica_sentencia_preliminar_Departamento_Juridico_sxyebfiv.svg` · `Notificacion_electronica_sentencia_preliminar_Departamento_De-Justicia_01.js` · `_001-Notificacion_electronica_demanda_judicial_Departamento_Juridico.js` · `DEMANDA LABORAL JUDICIAL 2313154.exe` · `RELACIÓN DE SALDOS - CUENTA DE COBRO.pdf.exe` · `vcredist.exe` · repositorio `notificaciones-judiciales2025-2005` | `señuelo` |
| Identidades del operador | Alias de publicación `TheMrHacker` y `Envio` en Bitbucket · cuenta de GitHub `SmikeY666` · usuarios de GitHub `jairpicc`, `santiagonasar`, `colombo08125`, `mastermr02456` *(estos cuatro, según la cita del informe de SCILabs)* | `atribución` |
| Patrones de nomenclatura de C2 | `envio[0-9\-]{2,5}\.duckdns\.org` · `deadpoolstart20\d{2}` sobre `duckdns.org` y `con-ip.com` · nombre y apellido español más dígitos · palabra en español con mes o año | `red` |

## X-3. Lógica de detección prioritaria

<!-- cti:detections -->

**D-1 · CRÍTICO — Adjunto `SVG` entrante**

```
email.direction == "inbound"
AND email.attachment.file_extension == "svg"
AND NOT email.recipient IN (<buzones de diseño, marketing e ingeniería exceptuados>)
```

→ Cuarentena con detonación, o reescritura a imagen plana. Es el vehículo del señuelo en las dos fuentes primarias, con 141 muestras publicadas de una sola campaña. **La excepción se gestiona por buzón y por remitente, nunca desactivando la regla.**

**D-2 · CRÍTICO — Ensamblado .NET cargado en memoria desde PowerShell**

```
event.code == 4104
AND script_block.text MATCHES "(?i)(Reflection\.Assembly\]?::Load|FromBase64String\s*\(|\.GetMethod\(\s*[\"']VAI)"
AND NOT user IN (<cuentas de administración de plataforma aprobadas>)
```

→ Contención automática en estaciones de trabajo. Es el único paso común a las tres variantes de cargador. Exceptuar por identidad de la cuenta, nunca por patrón de ruta.

**D-3 · CRÍTICO — Controlador cargado desde ruta escribible por el usuario**

```
(event.action == "driver-loaded" AND file.path MATCHES "(?i)\\\\(Users|Temp|AppData|ProgramData)\\\\")
OR (service.type == "kernel" AND service.image_path MATCHES "(?i)\\\\(Users|Temp|AppData)\\\\")
OR file.name IN ("VFZE6ksYnpPfSnEWUNg.sys","cuDX73ob9SxeAS0IdV.sys")
```

→ Contención automática y aislamiento. Un controlador en el núcleo cargado desde `%Temp%` es, en una estación gestionada, un incidente por definición. **Requiere la lista de bloqueo de controladores vulnerables de Microsoft activada, que es la mitigación de §X-5.**

**D-4 · CRÍTICO — `mscorlib.dll` cargada desde fuera del directorio de .NET**

```
event.action == "image-loaded"
AND file.name == "mscorlib.dll"
AND NOT file.directory MATCHES "(?i)\\\\(Windows\\\\Microsoft\.NET|assembly|WinSxS)\\\\"
```

→ Contención automática. `mscorlib.dll` fuera del árbol de .NET no es una biblioteca de .NET. Es la señal más específica y más barata de la variante de carga lateral, y prácticamente no tiene falso positivo.

**D-5 · ALTO — Carga lateral de DLL con vaciado sobre `AddInProcess32.exe`**

```
(event.action == "image-loaded"
 AND file.name IN ("libbrotlicommon.dll","CiscoSparkLauncher.dll","VERSION.dll")
 AND file.directory MATCHES "(?i)\\\\(Users|Temp|AppData|Downloads)\\\\")
OR (process.name == "AddInProcess32.exe" AND process.thread.state == "suspended")
```

→ Alerta de prioridad alta con recolección de la carpeta de ejecución. Exceptuar instalaciones legítimas de los productos que incluyen esas DLL **por ruta de instalación aprobada y firma**.

**D-6 · ALTO — Servicio legítimo de Internet solicitado por un proceso que no es navegador**

```
network.protocol IN ("http","https")
AND destination.domain MATCHES "(?i)(cdn\.discordapp\.com|bitbucket\.org|gist\.githubusercontent\.com|paste\.ee|pastebin\.com|archive\.org|lovestoblog\.com)"
AND process.name IN ("powershell.exe","wscript.exe","cscript.exe","mshta.exe","curl.exe","certutil.exe")
```

→ Alerta de prioridad alta. El destino es legítimo; el solicitante no debería serlo. **Sin atribución de proceso en el proxy esta regla no se puede implementar**, y eso es la brecha de §T-5.

**D-7 · ALTO — Tarea programada con nombre aleatorio al iniciar sesión con privilegio máximo**

```
process.name == "schtasks.exe"
AND process.command_line MATCHES "(?i)/create"
AND process.command_line MATCHES "(?i)/sc\s+onlogon"
AND process.command_line MATCHES "(?i)/rl\s+highest"
AND process.command_line MATCHES "(?i)/tn\s+\"?[A-Za-z0-9]{6,10}\"?\s"
AND process.command_line MATCHES "(?i)\\\\(AppData|Users|Temp|ProgramData)\\\\"
```

→ Alerta de prioridad alta. El nombre `Yt4Bvc2G` es el ejemplo publicado, no el indicador: el indicador es el patrón completo.

**D-8 · ALTO — Ruta de registro escrita de forma invertida**

```
process.command_line CONTAINS "nuR\\noisreVtenrretnuC"
OR file.content CONTAINS "erawtfoS\\tfosorciM\\swodniW"
OR registry.value MATCHES "(?i)nuR\\\\noisreV"
```

→ Alerta de prioridad alta y recolección de muestra. Nada legítimo escribe una ruta de registro al revés. Cobertura dependiente de la telemetría de cadenas en memoria.

**D-9 · MEDIO — Tráfico a DNS dinámico con patrón de nomenclatura conocido**

```
dns.question.name MATCHES "(?i)^(envio[0-9\\-]{2,5}|deadpoolstart20[0-9]{2})\\.(duckdns\\.org|con-ip\\.com|ddns\\.net)$"
OR (dns.question.name MATCHES "(?i)\\.(duckdns\\.org|con-ip\\.com|kozow\\.com|ip-ddns\\.com)$"
    AND source.type == "workstation")
```

→ Alerta de prioridad media; bloqueo del proveedor de DNS dinámico en estaciones de trabajo si la política lo permite. **El dominio concreto caduca; el patrón y el proveedor duran.**

**D-10 · MEDIO — Terminación masiva de procesos de seguridad**

```
event.action IN ("process-terminated","service-stopped")
AND target.process.name MATCHES "(?i)(MsMpEng|NisSrv|MpCmdRun|MpDefenderCoreService|smartscreen|ekrn|egui|aswEngSrv|AvastSvc|AVGSvc|mfemms|McShield|V3SVC|AYAgent|QHSafeMain|ZhuDongFangYu|360Tray)"
AND NOT source.process.name IN (<herramientas de gestión aprobadas>)
AND count(distinct target.process.name) >= 3 WITHIN 5m
```

→ Contención automática. Si esto dispara, la etapa 04 ya está corriendo. Exige protección contra manipulación activa y gestionada centralmente.

**D-11 · MEDIO — Señuelo de notificación institucional, con términos chilenos**

```
email.direction == "inbound"
AND (email.subject MATCHES "(?i)(notificaci(o|ó)n electr(o|ó)nica|demanda (laboral|judicial)|radicado|c(e|é)dula de notificaci(o|ó)n|oficina judicial virtual|requerimiento (de pago|judicial)|cobro por intereses|boleta|liquidaci(o|ó)n de impuesto)"
     OR email.attachment.name MATCHES "(?i)(notificacion_electronica|demanda_judicial|departamento_juridico|sentencia_preliminar|notificaciones-judiciales|cuenta de cobro)")
AND (email.attachment.file_extension IN ("svg","zip","rar","js","vbs","hta","url","exe")
     OR email.has_url == true)
```

→ Etiqueta visible para el usuario y cola de revisión, **no bloqueo**: buena parte de estos correos serán notificaciones auténticas. Los términos chilenos provienen del Anexo D.

**D-12 · MEDIO — Comprimido cifrado con la contraseña en el propio mensaje**

```
email.direction == "inbound"
AND email.attachment.is_encrypted_archive == true
AND (email.body MATCHES "(?i)(contrase(n|ñ)a|clave|password)\\s*[:=]\\s*[A-Za-z0-9]{4,16}"
     OR email.attachment.name MATCHES "(?i)\\.svg$")
```

→ Cuarentena. El comprimido con contraseña publicada en el señuelo existe exactamente para que el motor de análisis no pueda abrirlo. Es una decisión de política antes que una detección.

<!-- cti:note type="warn" -->

> ⚠ **Las doce reglas están sin calibrar en nuestro entorno.** Ninguna se ha ejecutado
> contra nuestra telemetría porque no tenemos acceso a ella (§O-4). Los umbrales de `D-10`,
> las excepciones de `D-1` y `D-5` y la lista de cuentas de `D-2` **deben fijarse con datos
> propios antes de poner nada en bloqueo**. Publicarlas en modo alerta durante dos semanas
> y medir es el camino; ponerlas en contención el primer día es una interrupción
> garantizada.

<!-- cti:note type="gap" -->

> ⬛ **Lo que no se puede detectar con lo que hay publicado.** El correo de remitente
> auténtico comprometido (`KJ-1`) **no tiene detección técnica fiable**: el mensaje es
> legítimo en todos sus campos verificables. `D-11` lo etiqueta, no lo detecta. La única
> contramedida real es el procedimiento de verificación de la decisión `E-b`, y es de
> proceso. Conviene decirlo en voz alta antes de que alguien compre un producto esperando
> que lo resuelva.

## X-4. Consultas de caza

```kql
// H-1 · Adjuntos SVG entrantes y qué ocurrió en los diez minutos siguientes
let svg = EmailAttachmentInfo
    | where Timestamp > ago(90d)
    | where FileType =~ "svg" or FileName endswith ".svg"
    | join kind=inner (
        EmailEvents
        | where Timestamp > ago(90d) and EmailDirection == "Inbound"
        | project NetworkMessageId, Timestamp, SenderFromAddress, SenderFromDomain,
                  RecipientEmailAddress, Subject, DeliveryAction
      ) on NetworkMessageId
    | project Timestamp, SenderFromAddress, SenderFromDomain, RecipientEmailAddress,
              Subject, FileName, SHA256, DeliveryAction;
svg
| join kind=leftouter (
    DeviceProcessEvents
    | where Timestamp > ago(90d)
    | project ProcTime = Timestamp, DeviceName, AccountUpn, ProcessCommandLine,
              FileName_proc = FileName, InitiatingProcessFileName
  ) on $left.RecipientEmailAddress == $right.AccountUpn
| where ProcTime between (Timestamp .. (Timestamp + 10m))
| project Timestamp, SenderFromDomain, RecipientEmailAddress, Subject, FileName,
          ProcTime, DeviceName, FileName_proc, ProcessCommandLine
| order by Timestamp desc
```

```kql
// H-3 · Ensamblado .NET cargado en memoria desde PowerShell, y el método VAI
DeviceEvents
| where Timestamp > ago(90d)
| where ActionType == "PowerShellCommand"
| extend Bloque = tostring(parse_json(AdditionalFields).Command)
| where Bloque matches regex @"(?i)(Reflection\.Assembly\]?::Load|FromBase64String\s*\(|GetMethod\(\s*[""']VAI)"
| project Timestamp, DeviceName, AccountName, InitiatingProcessFileName,
          InitiatingProcessCommandLine, Bloque = substring(Bloque, 0, 600)
| order by Timestamp desc
```

```kql
// H-4 + H-7 · Controlador desde ruta de usuario, y DLL de carga lateral conocidas
let controladores = DeviceImageLoadEvents
    | where Timestamp > ago(90d)
    | where FileName endswith ".sys"
    | where FolderPath matches regex @"(?i)\\(Users|Temp|AppData|ProgramData)\\"
    | project Timestamp, DeviceName, FolderPath, FileName, Señal = "controlador en ruta de usuario";
let laterales = DeviceImageLoadEvents
    | where Timestamp > ago(90d)
    | where FileName in~ ("libbrotlicommon.dll","CiscoSparkLauncher.dll","VERSION.dll","mscorlib.dll")
    | where FolderPath matches regex @"(?i)\\(Users|Temp|AppData|Downloads)\\"
    | project Timestamp, DeviceName, FolderPath, FileName, Señal = "carga lateral";
let vaciado = DeviceProcessEvents
    | where Timestamp > ago(90d)
    | where FileName =~ "AddInProcess32.exe"
    | project Timestamp, DeviceName, FolderPath, FileName, Señal = "AddInProcess32";
union controladores, laterales, vaciado
| summarize Señales = make_set(Señal), Eventos = count(), Ficheros = make_set(FileName, 20)
        by DeviceName, bin(Timestamp, 1h)
| order by array_length(Señales) desc, Eventos desc
```

```kql
// H-5 · Servicio legítimo de Internet solicitado por un proceso que no es navegador
let servicios = dynamic(["cdn.discordapp.com","bitbucket.org","gist.githubusercontent.com",
                         "paste.ee","pastebin.com","archive.org","web.archive.org",
                         "lovestoblog.com","tagbox.io"]);
let sospechosos = dynamic(["powershell.exe","pwsh.exe","wscript.exe","cscript.exe",
                           "mshta.exe","curl.exe","certutil.exe","bitsadmin.exe","regsvr32.exe"]);
DeviceNetworkEvents
| where Timestamp > ago(90d)
| where RemoteUrl has_any (servicios) or RemoteUrl matches regex @"(?i)(paste\.ee|archive\.org)"
| where InitiatingProcessFileName in~ (sospechosos)
| project Timestamp, DeviceName, AccountName, InitiatingProcessFileName,
          InitiatingProcessCommandLine, RemoteUrl, RemoteIP
| order by Timestamp desc
```

```kql
// H-8 + H-9 · Persistencia: tarea de nombre aleatorio, y ruta de registro invertida
let tareas = DeviceProcessEvents
    | where Timestamp > ago(90d)
    | where FileName =~ "schtasks.exe"
    | where ProcessCommandLine matches regex @"(?i)/create"
          and ProcessCommandLine matches regex @"(?i)/sc\s+onlogon"
          and ProcessCommandLine matches regex @"(?i)/rl\s+highest"
    | where ProcessCommandLine matches regex @"(?i)\\(AppData|Users|Temp|ProgramData)\\"
    | project Timestamp, DeviceName, AccountName, ProcessCommandLine, Señal = "tarea onlogon";
let invertida = DeviceProcessEvents
    | where Timestamp > ago(90d)
    | where ProcessCommandLine contains "nuR\\noisreVtenrretnuC"
          or ProcessCommandLine contains "erawtfoS\\tfosorciM"
    | project Timestamp, DeviceName, AccountName, ProcessCommandLine, Señal = "ruta invertida";
union tareas, invertida
| order by Timestamp desc
```

```kql
// H-10 · DNS dinámico con los patrones de nomenclatura del conjunto
DeviceNetworkEvents
| where Timestamp > ago(90d)
| where RemoteUrl matches regex @"(?i)\.(duckdns\.org|con-ip\.com|kozow\.com|ddns\.net|ip-ddns\.com|writesthisblog\.com)$"
| extend Patron = case(
      RemoteUrl matches regex @"(?i)^envio[0-9\-]{2,5}\.", "serie envio",
      RemoteUrl matches regex @"(?i)^deadpoolstart20[0-9]{2}\.", "serie deadpoolstart",
      RemoteUrl matches regex @"(?i)^[a-z]+[a-z]+[0-9]{4,8}\.", "nombre + dígitos",
      "otro")
| summarize Conexiones = count(), Equipos = dcount(DeviceName),
            Procesos = make_set(InitiatingProcessFileName, 10)
        by RemoteUrl, Patron
| order by Conexiones desc
```

```yaml
# Sigma — Adjunto SVG entrante con asunto de notificación judicial o tributaria
# Autor: Célula CTI · Fecha: 2026-11-16 · ATT&CK: T1566.001, T1027.017
# Nivel: high · Estado: experimental
# Falsos positivos conocidos: notificaciones auténticas de organismos públicos y
# material gráfico legítimo. Esta regla etiqueta y encola; NO debe bloquear.
title: Adjunto SVG con señuelo de notificación institucional
id: 2026-022-svg-notificacion
status: experimental
description: >
  Detecta correo entrante con adjunto SVG y asunto o nombre de adjunto con la fórmula
  administrativa de una notificación judicial o tributaria. Basada en las campañas que
  Acronis TRU publicó el 2025-06-18 y Recorded Future el 2025-08-26.
logsource:
  category: mail
  product: gateway
detection:
  adjunto_svg:
    attachment|endswith: '.svg'
  entrante:
    direction: 'inbound'
  formula:
    - subject|contains:
        - 'notificacion electronica'
        - 'notificación electrónica'
        - 'demanda judicial'
        - 'demanda laboral'
        - 'radicado'
        - 'cedula de notificacion'
        - 'oficina judicial virtual'
        - 'requerimiento de pago'
        - 'cobro por intereses'
    - attachment|contains:
        - 'Notificacion_electronica'
        - 'demanda_judicial'
        - 'Departamento_Juridico'
        - 'sentencia_preliminar'
  condition: entrante and adjunto_svg and formula
falsepositives:
  - Notificaciones auténticas de organismos públicos
  - Firmas gráficas y material de marketing en SVG
level: high
tags:
  - attack.initial_access
  - attack.t1566.001
  - attack.defense_evasion
  - attack.t1027.017
```

```yaml
# Sigma — Controlador cargado desde ruta escribible por el usuario
# Autor: Célula CTI · Fecha: 2026-11-16 · ATT&CK: T1068, T1543.003
# Nivel: critical · Estado: experimental
# Basada en los dos controladores vulnerables que Acronis TRU documentó el 2025-06-18.
title: Controlador de núcleo cargado desde ruta de usuario
id: 2026-022-driver-ruta-usuario
status: experimental
description: >
  Un controlador cargado desde %Temp%, %AppData% o el perfil del usuario, o un servicio
  de núcleo apuntando a esas rutas. En una estación gestionada no tiene equivalente
  legítimo. Cubre los controladores vulnerables de WiseCleaner (CVE-2023-1486) y de
  Zemana (CVE-2022-42045) usados para escalar privilegios.
logsource:
  category: driver_load
  product: windows
detection:
  ruta_usuario:
    ImageLoaded|contains:
      - '\Users\'
      - '\Temp\'
      - '\AppData\'
      - '\ProgramData\'
  extension:
    ImageLoaded|endswith: '.sys'
  conocidos:
    ImageLoaded|endswith:
      - 'VFZE6ksYnpPfSnEWUNg.sys'
      - 'cuDX73ob9SxeAS0IdV.sys'
  condition: (ruta_usuario and extension) or conocidos
falsepositives:
  - Instaladores de controladores que extraen a Temp antes de registrar; exceptuar por
    firma digital y por ventana de cambio aprobada
level: critical
tags:
  - attack.privilege_escalation
  - attack.t1068
  - attack.t1543.003
```

## X-5. Mitigaciones de configuración con efecto directo

| Control | Corta |
|---|---|
| Bloqueo, reescritura a imagen plana o cuarentena con detonación de adjuntos `SVG` entrantes | **La etapa 02 completa** en su variante dominante de 2025 (`T1027.017`). Es el control de mejor relación coste-efecto del informe |
| Bloqueo de adjuntos `.js`, `.vbs`, `.hta`, `.url`, `.scr` y comprimidos con contraseña | El resto de la etapa 02 y la transición a la etapa 03 |
| Lista de bloqueo de controladores vulnerables de Microsoft activada y mantenida | **La escalada de privilegios de la variante más capaz** (`T1068`), incluidos los dos controladores publicados |
| Registro de bloques de script de PowerShell, con 90 días de retención | No corta nada: **habilita** `D-2`, que es la detección del único paso común a las tres variantes de cargador |
| Modo de lenguaje restringido de PowerShell, o directiva de ejecución firmada, en estaciones de trabajo | La variante sin fichero completa (`T1620`), que es la más reciente y la que no deja artefacto en disco |
| Proxy con atribución de proceso y registro de descargas | No corta nada: **habilita** `D-6` y `D-9`, sin las cuales los servicios legítimos quedan indistinguibles |
| Reglas de reducción de superficie de ataque que bloqueen la creación de procesos hijo por scripts y la ejecución de contenido descargado | La transición de la etapa 02 a la etapa 03 |
| Gestor de contraseñas del navegador deshabilitado por directiva para credenciales corporativas | El objetivo principal del implante (`T1555.003`), aunque la etapa 04 tenga éxito |
| Protección contra manipulación del EDR activada y gestionada centralmente | La lista de terminación de más de noventa procesos de seguridad (`T1562.001`) |
| Bloqueo de proveedores de DNS dinámico gratuito en estaciones de trabajo | El canal de mando y control de cuatro de los cinco conjuntos de infraestructura |
| Autenticación multifactor resistente a suplantación en el correo corporativo, y reposición obligatoria ante aparición en registros filtrados | **Que seamos nosotros el remitente auténtico de la campaña siguiente.** Es el único control que ataca el mecanismo de `KJ-1` en su origen |
| Procedimiento publicado de verificación de notificaciones judiciales y tributarias | **La etapa 01**, que no tiene contramedida técnica. Es proceso, no producto, y por eso se decide en `E-b` y no en el SOC |

---

## 14. Brechas de inteligencia y nuevos requisitos de colección

| # | Brecha | Impacto en el juicio | Requisito propuesto | Prioridad |
|---|---|---|---|---|
| G-1 | **El informe primario de SCILabs no pudo leerse** | Todo lo que este producto dice del contenido de ese informe es cita de segunda mano, incluidas las dos cuentas comprometidas atribuidas a Red Akodon, los cuatro usuarios de GitHub y la persistencia por acceso directo | Que una persona abra `blog.scilabs.mx` en un navegador y guarde el artículo. **Coste: cinco minutos.** Hasta entonces, no citar nada de SCILabs sin la advertencia | Crítica |
| G-2 | Sin telemetría propia | §O-4 vacía; las doce reglas de §X-3 sin calibrar; no sabemos si ya nos alcanzó ni cuántos `SVG` entran por semana | Ejecutar el cuestionario X-1 a X-11 de §O-4, empezando por X-1, X-2 y X-6 | Crítica |
| G-3 | La relación entre los tres conjuntos de actividad no está resuelta por ninguna fuente | `KJ-5` queda con confianza baja; la gestión de indicadores y la compra de inteligencia siguen duplicadas | Preguntar formalmente a los proveedores que tengamos contratados por su posición sobre la equivalencia Red Akodon ↔ TAG-144 ↔ Shadow Vector, y registrar la respuesta | Alta |
| G-4 | **Ninguna fuente documenta víctimas chilenas** | `KJ-7` es una inferencia nuestra sobre transferibilidad, no un hallazgo. Es el juicio más consecuente del informe y el más débil | Consulta al CSIRT Nacional sobre campañas con señuelo judicial o del SII con adjunto `SVG`; vigilancia específica del indicador `I-1` | Alta |
| G-5 | No hay puertos de mando y control publicados salvo uno | Las reglas de red de §X-3 no pueden apoyarse en puerto y dependen enteramente de dominio y de patrón | Extraer configuraciones de muestras públicas de las seis familias asociadas a estos dominios y construir la tabla de puertos | Media |
| G-6 | La contradicción interna de Recorded Future sobre el sector del `Cluster 1` | Determina si una empresa privada sin relación con el Estado está o no en el tiro, y por tanto cuánta urgencia tiene este informe para nosotros | Pedir aclaración al proveedor; mientras no haya respuesta, asumir el supuesto amplio | Media |
| G-7 | Las cadenas en portugués de los cargadores no están explicadas por ninguna fuente | Si hay colaboración real con el ecosistema brasileño, los dos informes —este y `CTI-2026-021`— describen un mismo mercado y deberían leerse juntos | Añadir al plan de colección permanente el seguimiento de criptadores brasileños y su clientela hispanohablante | Media |
| G-8 | Sin vigilancia de suplantación de nuestra propia marca en contexto de notificación o cobro | La cara reputacional queda sin evaluar, y es la que no controla seguridad informática | Encargo a Asuntos Corporativos con procedimiento de denuncia, reutilizando lo hecho en `CTI-2026-018` | Media |
| G-9 | Sin inventario del volumen base de `SVG` entrantes | No se puede dimensionar el coste de la decisión `E-a` ni fijar sus excepciones | Consulta de 90 días en la pasarela de correo: pregunta X-1 de §O-4 | Alta |
| G-10 | Los apéndices de Recorded Future no están ingeridos en nuestras herramientas | Más de doscientos dominios y un centenar de direcciones publicadas que no están en ninguna lista nuestra | Ingesta del apéndice completo como lista de **detección**, no de bloqueo, por el problema de la VPN compartida y los ISP colombianos | Alta |

---

# ANEXOS

## Anexo A — Indicadores de compromiso

<!-- cti:note type="warn" -->

> ⚠ **Leer antes de usar, y aquí las advertencias son tres y ninguna es formularia.**
> **Primera:** buena parte de las direcciones de los conjuntos 1 y 5 son **servidores de
> VPN comercial** (TorGuard, AS9009) y de **ISP colombianos domésticos**. Bloquearlas
> corta a clientes legítimos de esos servicios y a redes residenciales enteras. Trátense
> como detección, nunca como bloqueo. **Segunda:** las cuentas de correo institucionales
> que aparecen abajo son **buzones auténticos de entidades públicas colombianas,
> pertenecientes a terceros inocentes**, y una de ellas está confirmada como legítima por
> la propia fuente. Están aquí porque son el indicador más valioso del informe; **bloquear
> el dominio `cendoj.ramajudicial.gov.co` cortaría notificaciones judiciales reales**.
> **Tercera:** los 141 hashes de `SVG` que publica Acronis son, según el comentario de su
> propia regla YARA, «posiblemente generados en lote»: su valor es de retrohunt y de
> confirmación, no de prevención. Aquí se recoge una selección representativa; la lista
> completa está en la fuente.

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Acción permitida |
|---|---|---|---|---|
| sha256 | `04878a5889e3368c2cf093d42006ba18a87c5054f1464900094e6864f4919899` | `Notificacion_electronica_sentencia_preliminar_Departamento_Juridico_sxyebfiv.svg` — adjunto del correo del 1-jul-2025 desde la alcaldía de Simacota (Recorded Future) | Alta | Bloqueo y retrohunt |
| sha256 | `1226a8d066328a8b6f353c9d98f1dc8128bd84f3909ae1cc6811dc1adff33c81` | `Notificacion_electronica_sentencia_preliminar_Departamento_De-Justicia_01.js` — segunda etapa servida desde la red de distribución de Discord | Alta | Bloqueo y retrohunt |
| sha256 | `591744244c7ca9cea69cde263187efde3f65a157f8e5eb885ccc1f9e078b5572` | Cuerpo de la respuesta de Paste.ee ejecutado como JavaScript por la etapa anterior | Alta | Bloqueo y retrohunt |
| sha256 | `64e971f0fed4da9d71cd742db56f73b6f7da8fec3b8aebd17306e8e0d4f1d29d` · `4d292a785ec35530bac5f4674a97c0dffa2a2396bd8b0cc6f8b478ba13d73611` · `d713793b0b6dd1fe7c2432a28069745bc4bf97c098f1217de0731c7ed7c1d70a` | Muestras `SVG` de la campaña Shadow Vector (Acronis, jun-2025) | Alta | Retrohunt; bloqueo de escaso valor |
| sha256 | `1920d23a395aa729cc7658b8471939ef871108a94e93456793d1322dcbe9750b` · `fab0b6945c1ee0057349254760469b7d5a502819517b31049efc51a71b25c46d` · `52d2b4ac1a84449c72226e1deed8d33ebbe8fd00d4853e026adef679d7fa273d` | Muestras `SVG` de la misma campaña | Alta | Retrohunt |
| sha256 | `f9b6c8f6f6a2f69286b298dd6375ebc25a07eb2012e226af1dfafd861b9edb3e` · `e50f96eb8fd7ca90df3db47368b413ffb875d5cd3685b9d601bb884ebe980ef9` · `ea81ab0c9daee3a3e5a34e1a94a5a7f1ea1ed664ee6df4596671c30f56d06f30` | Muestras `SVG` de la misma campaña | Alta | Retrohunt |
| sha256 | `2ad823885a7406219944bd07a438b53495ab7440b857857f7d2b48001d43c841` · `15818f97142d49cbc9662d51bb0155a7a8dc650bf1daf26e07a5fff4ff15d93f` · `589dc2e8e4528ee6c18ac1c7cf5964a352d3cb245a8b32c7f81c12cf51f5f926` | Muestras `SVG` de la misma campaña | Alta | Retrohunt |
| sha256 | `ddd31270f6150d004bd857785096d0ebd6ba68a5657ca64decce494dc26fb824` · `fa1bd87281ed0d2ffbed269160008cd9fa758a5a3e1702c5871cffe2b8837bb5` · `49abf67639aca4a12e4205b407b82d281cbc4e47d9f0dae799a6900b3c48aa13` | Muestras `SVG` de la misma campaña | Alta | Retrohunt |
| sha256 | `dd5fab6baa5967e6b1d023f6d98dcbe0d7a03cedafc7bddbab6d9b5bc07f6a2d` · `651f8771e83fe70a57215adb225de065c9cfd3485bd041768cb5923b29449b18` · `d1f7e55aee74a868f8defd411231d0fbd7a9f2050a5a32660a8845e5e890efb9` | Muestras `SVG` de la misma campaña | Alta | Retrohunt |
| sha256 | `bf596502f05062d156f40322bdbe9033b28df967ce694832a78482b47dcdd967` | Paquete comprimido de la campaña Shadow Vector | Alta | Bloqueo y retrohunt |
| sha256 | `53cad386b6af155952380eb8050eebef368836bcb035dffe2ca8a58ae22c055c` | Paquete comprimido de la campaña Shadow Vector | Alta | Bloqueo y retrohunt |
| sha256 | `5576f8e746f206f9a682b9bbb4a623c72b60892c96979fbe2ffab3b32d6aea7e` | Paquete comprimido de la campaña Shadow Vector | Alta | Bloqueo y retrohunt |
| sha256 | `bb20c46a817a7c0cdffb513ec4d14bd2026ea70b8f1a0ec07bb699cd0d70a29a` | Paquete comprimido de la campaña Shadow Vector | Alta | Bloqueo y retrohunt |
| sha256 | `0e5a768a611a4d0ed7cb984b2ee790ad419c6ce0be68c341a2d4f64c531d8122` | Carga final de Shadow Vector (AsyncRAT o REMCOS según variante) | Alta | Bloqueo y retrohunt |
| sha256 | `b04ea3c83515c3daf2de76c18e72cb87c0772746ec7369acce8212891d0d8997` | Carga final de Shadow Vector | Alta | Bloqueo y retrohunt |
| sha256 | `ad1d1b6fea71c28a555341f8591c59272b0509df9b2c75519a813066c3053ff6` | Carga final de Shadow Vector | Alta | Bloqueo y retrohunt |
| sha256 | `9e6aa602427a41bcf12c5ffa022941a6eb1d51be71e36ecebd714e6c9e9ab51e` | Carga final de Shadow Vector | Alta | Bloqueo y retrohunt |
| sha256 | `3150ef6e48e403c8667aea84bfa1585878df68c0cea1925edcc2a745759b119e` | Carga final de Shadow Vector | Alta | Bloqueo y retrohunt |
| sha256 | `17ac16f1cd25ea3b31b2a89b193d51c7b1959d48cb72364eb05081d806178f1d` | Carga final de Shadow Vector | Alta | Bloqueo y retrohunt |
| sha256 | `1b3c1501b3fbcd0a4fbcb1f8bbc21a34f89232aa1e794dc2821cc92eee4ce44c` | Carga final de Shadow Vector | Alta | Bloqueo y retrohunt |
| sha256 | `721df71a5491d481044c149d24e19ca6dbce34baf6ad98fe4f4cc66af0d1826b` | Carga final de Shadow Vector | Alta | Bloqueo y retrohunt |
| sha256 | `f847d48b3007ab27c5b3207d41cb36a7f5b15f2192d1bbb7cec58f371fdce685` | Carga final de Shadow Vector | Alta | Bloqueo y retrohunt |
| sha256 | `c5399f7e0adefb814ae8b921273f96c612e20fc66dd9d3048749a2ee9e39850e` | Carga final de Shadow Vector | Alta | Bloqueo y retrohunt |
| sha256 | `2bbc6b9dd5e6d0327250b32305be20c89b19b56d33a096522ee33f22d8c82ff1` | Carga final de Shadow Vector | Alta | Bloqueo y retrohunt |
| sha256 | `30aa90270ca9f04c554b2a6e17d22b49e5e3f6fb526e133fd35364b08784925d` | Carga final de Shadow Vector | Alta | Bloqueo y retrohunt |
| sha256 | `906c7cf78cff18b7d43c4137937a75b3be41eaf654e835afb473168b7ed24f2d` | Carga final de Shadow Vector | Alta | Bloqueo y retrohunt |
| sha256 | `5201e12cfdbeb48488599eefc84e9bafd9feabf208da15b3c25c56243de1eba7` | Carga final de Shadow Vector | Alta | Bloqueo y retrohunt |
| sha256 | `e407403a0ab5fcd89fa7bafb82de1d6261b9260398122d105cd1a97f4258ac1f` | Carga final de Shadow Vector | Alta | Bloqueo y retrohunt |
| sha256 | `92706a73c54332b33f845adb4ed8f0e2fbbb6cba0cae53a0e695257621ba269e` | Carga final de Shadow Vector | Alta | Bloqueo y retrohunt |
| sha256 | `1af14cc00b1044636f6623f5f26343dfef3003f1c2a0181c995a573eae832c7a` | Carga final de Shadow Vector | Alta | Bloqueo y retrohunt |
| sha256 | `0b188c53a446ce7b8acbc58d4e0b02ba4b87ece9c9b9bb14bf10e8d9c34d26cd` | Carga final de Shadow Vector | Alta | Bloqueo y retrohunt |
| sha256 | `0c4eb3c0537182c4cd5281f08559534b2eb44ae20b91867c115b9fc404c1b425` | Carga final de Shadow Vector | Alta | Bloqueo y retrohunt |
| sha256 | `11cdb65e5b007e249a51a7410da0653ec6c6b28f68b33e1de88ac3989dd745d6` | Carga final de Shadow Vector | Alta | Bloqueo y retrohunt |
| domain | `asynk02[.]duckdns[.]org` | C2 de AsyncRAT, puerto `7788`, campaña Shadow Vector | Alta | Bloqueo |
| domain | `cococovid202420242024[.]duckdns[.]org` | C2 de AsyncRAT del `Cluster 2`, entregado por GitHub Gist | Alta | Bloqueo |
| domain | `deadpoolstart2064[.]duckdns[.]org` · `deadpoolstart2025[.]duckdns[.]org` · `deadpoolstart2026[.]con-ip[.]com` | C2 de XWorm del `Cluster 2`. **La serie `deadpoolstart` llega hasta el año 2065: el patrón vale más que el dominio** | Alta | Bloqueo |
| domain | `envio01[.]ddns[.]net` · `envio07[.]duckdns[.]org` · `envio1010[.]duckdns[.]org` · `envio2020[.]duckdns[.]org` | C2 del `Cluster 1`, serie `envio` que Insikt describe como probablemente generada por un algoritmo | Alta | Bloqueo |
| domain | `envio14-05[.]duckdns[.]org` · `envio16-05[.]duckdns[.]org` · `envio19-05[.]duckdns[.]org` · `envio21-05[.]duckdns[.]org` | C2 del `Cluster 1`, variante con día y mes en el nombre | Alta | Bloqueo |
| domain | `newremco[.]duckdns[.]org` · `rem25rem[.]duckdns[.]org` · `remc21[.]duckdns[.]org` | C2 de REMCOS del `Cluster 1` | Alta | Bloqueo |
| domain | `qua25q[.]duckdns[.]org` · `qua25qua[.]duckdns[.]org` | C2 de QuasarRAT del `Cluster 1` | Alta | Bloqueo |
| domain | `respaldito01[.]duckdns[.]org` · `respaldomax3[.]duckdns[.]org` · `respaldomx1[.]duckdns[.]org` | C2 de respaldo del `Cluster 1` | Alta | Bloqueo |
| domain | `pesosdepesoslibras[.]duckdns[.]org` · `camarasdeseguridad202420242024[.]duckdns[.]org` · `dominioseternosgraciasadios20230230230[.]duckdns[.]org` | C2 del `Cluster 2`, patrón de palabras en español | Alta | Bloqueo |
| domain | `sebastiancorrea905040[.]duckdns[.]org` · `carlosmendoza504070[.]duckdns[.]org` · `armandovillareal504010[.]duckdns[.]org` | C2 del `Cluster 3`, patrón de nombre y apellido español más dígitos | Alta | Bloqueo |
| domain | `asynpro[.]duckdns[.]org` · `dcfast[.]duckdns[.]org` · `sostenermio2025[.]duckdns[.]org` · `testedark[.]writesthisblog[.]com` | C2 del `Cluster 4` | Alta | Bloqueo |
| domain | `ansy10jun[.]duckdns[.]org` · `asegurar2octubre[.]duckdns[.]org` · `gotemburgoxm[.]duckdns[.]org` · `romanovas[.]duckdns[.]org` | C2 del `Cluster 5`; `gotemburgoxm` sirve REMCOS y XWorm, `romanovas` sirve LimeRAT | Alta | Bloqueo |
| url | `hxxps://archive[.]org/replace_202505/REPLACE[.]txt` | Depósito de la carga en base64 en la campaña Shadow Vector. **Servicio legítimo: bloquear la ruta, no el dominio** | Alta | Detección; bloqueo de ruta |
| url | `hxxps://t[.]me/xworm_v2` | Canal de Telegram que distribuye la versión crackeada de XWorm, con más de 300 miembros. **Es inteligencia de proveedor, no infraestructura de ataque** | Media | Solo detección |
| ipv4 | `146.70.137.90` | C2 de DcRAT, AsyncRAT y REMCOS del `Cluster 1`; **servidor de VPN comercial TorGuard (AS9009)** | Alta | Solo detección; no bloquear |
| ipv4 | `146.70.51.42` · `146.70.83.218` · `146.70.57.58` · `146.70.50.42` | C2 del `Cluster 1`; **todas servidores de VPN comercial compartida** | Alta | Solo detección; no bloquear |
| ipv4 | `45.133.180.26` · `45.133.180.154` · `93.115.35.146` · `193.56.253.66` | C2 del `Cluster 1`; VPN comercial | Alta | Solo detección; no bloquear |
| ipv4 | `181.235.4.255` · `181.235.10.163` · `181.235.15.197` | C2 del `Cluster 1` en ISP colombiano (AS3816). **Probables equipos de terceros comprometidos** | Media | Solo detección |
| ipv4 | `186.169.48.180` · `186.169.50.123` · `186.169.80.199` · `186.169.82.147` | C2 del `Cluster 1` en ISP colombiano | Media | Solo detección |
| ipv4 | `64.188.9.172` · `64.188.9.173` · `64.188.9.175` · `64.188.9.177` | Servidores proxy del `Cluster 2` (AS36352); resuelven la serie `deadpoolstart` | Alta | Bloqueo con validación |
| ipv4 | `45.77.72.102` | VPS del `Cluster 2` (AS20473), AsyncRAT | Alta | Bloqueo |
| ipv4 | `172.93.160.188` · `191.88.249.175` · `179.14.8.131` · `177.255.84.173` · `181.131.217.63` | C2 del `Cluster 2`, mezcla de VPS e ISP colombianos | Media | Detección; bloqueo con validación |
| ipv4 | `181.131.216.206` · `181.131.218.182` · `181.131.219.42` | C2 de REMCOS y AsyncRAT del `Cluster 3` (AS13489, ISP colombiano) | Media | Solo detección |
| ipv4 | `45.135.232.38` · `89.117.23.25` · `178.73.218.8` · `46.246.82.9` | C2 del `Cluster 4` en VPS europeos | Alta | Bloqueo |
| ipv4 | `181.235.3.0` · `191.93.113.151` | C2 del `Cluster 4` en ISP colombianos | Media | Solo detección |
| ipv4 | `46.246.4.3` · `46.246.6.4` · `46.246.14.2` · `46.246.80.3` · `46.246.84.5` · `46.246.86.4` | C2 del `Cluster 5` (AS42708); el conjunto más amplio, con medio centenar de direcciones en el mismo espacio | Alta | Bloqueo con validación |
| ipv4 | `178.73.192.3` · `178.73.218.2` · `188.126.90.2` · `45.133.180.162` | C2 del `Cluster 5` | Alta | Bloqueo con validación |
| email | `nomina@magdalena[.]gov[.]co` | **Cuenta institucional legítima comprometida**, atribuida a Red Akodon *(según la cita del informe de SCILabs)*. **NO bloquear el dominio** | Alta | Solo detección; verificar contexto |
| email | `npereza@cendoj[.]ramajudicial[.]gov[.]co` | **Cuenta de la Rama Judicial legítima comprometida**, atribuida a Red Akodon *(ídem)*. **NO bloquear el dominio** | Alta | Solo detección; verificar contexto |
| email | `alcaldia@simacota-santander[.]gov[.]co` | Remitente «probablemente comprometido» del correo del 1-jul-2025 con el adjunto `SVG` | Alta | Solo detección; verificar contexto |
| email | `j03mpmixartado@cendoj[.]ramajudicial[.]gov[.]co` | **Cuenta confirmada como legítima por Recorded Future**, perteneciente a la secretaría de un juzgado civil; apareció en registros de un ladrón de credenciales | Alta | Solo detección; **jamás bloquear** |
| email | `ftorreshe@cendoj[.]ramajudicial[.]gov[.]co` · `j01pmpalchiquinquira@cendoj[.]ramajudicial[.]gov[.]co` · `j02cctochiquinquira@cendoj[.]ramajudicial[.]gov[.]co` | Cuentas institucionales de la Rama Judicial asociadas a los envíos | Alta | Solo detección; verificar contexto |
| email | `jcmpalchoconta@cendoj[.]ramajudicial[.]gov[.]co` · `raccionestutj02cctochiquinquira@cendoj[.]ramajudicial[.]gov[.]co` · `repchiquinquiraboy@cendoj[.]ramajudicial[.]gov[.]co` | Cuentas institucionales de la Rama Judicial asociadas a los envíos | Alta | Solo detección; verificar contexto |
| email | `silay.salamanca699@educacionbogota[.]edu[.]co` | Cuenta de la secretaría de educación de Bogotá asociada a los envíos | Alta | Solo detección; verificar contexto |
| email | `abogados@hujmb[.]gov[.]co` | Cuenta de un hospital público usada para enviar `SVG` maliciosos *(citado a través de ¡Mucho Hacker!, oct-2024)* | Media | Solo detección; verificar contexto |
| mutex | `AsyncMutex_6SI8OkPnk` | Mutex de la variante crackeada de XWorm y de AsyncRAT; aparece en **las dos fuentes primarias**, lo que lo convierte en el lazo técnico más duro entre ambos conjuntos | Alta | Detección |
| mutex | `tempcookieess` · `tempcokies` · `tempcookiee` · `WinCookies` · `CookiesGoogleChrome` · `1e97ead369` | Mutex de AsyncRAT del `Cluster 2` y de LimeRAT del `Cluster 5` | Alta | Detección |
| ruta | `%Temp%\VFZE6ksYnpPfSnEWUNg.sys` · `%Temp%\cuDX73ob9SxeAS0IdV.sys` · `%Temp%\svchost.exe` | Controladores vulnerables y carga de REMCOS de la campaña Shadow Vector | Alta | Detección |
| ruta | `C:\Users\DEV\AppData\Roaming\DEMANDA LABORAL JUDICIAL 2313154.exe` | Objetivo de la tarea programada `Yt4Bvc2G`; la cadena `\DEV\` es del entorno del atacante | Alta | Detección |
| clave | `zZ5OP9zoIeGTxRmoYxR6XEu0yUxV6wAE` | Clave AES de la configuración de AsyncRAT en la campaña Shadow Vector | Alta | Detección |

## Anexo B — Fuentes y valoración

> Valoración doble tipo Admiralty/OTAN: **fiabilidad de la fuente (A–F)** ×
> **credibilidad de la información (1–6)**. Se valoran por separado.

| Fuente | Disciplina | Fiabilidad | Credibilidad | Notas de sesgo |
|---|---|---|---|---|
| Recorded Future / Insikt Group — «TAG-144's Persistent Grip on South American Organizations» (26-ago-2025, corte 21-jul-2025) | OSINT comercial / TECHINT | B | 2 | **La fuente más extensa del informe:** cinco agrupaciones delimitadas por infraestructura, 28 víctimas enumeradas con fecha y C2, once cuentas institucionales, apéndices completos de dominios y direcciones. **Tres salvedades:** no publica fecha en el cuerpo del documento; **no declara su propia decisión sobre la relación con Red Akodon** ni asigna confianza numérica; y **se contradice** entre el cuerpo («exclusivamente gobierno») y su apéndice de víctimas. Sesgo de producto: las mitigaciones que propone son en buena parte sus propios servicios |
| Acronis TRU — «Shadow Vector targets Colombian users via privilege escalation and court-themed SVG decoys» (18-jun-2025) | OSINT comercial / TECHINT | B | 2 | **El mejor análisis técnico de la cadena:** tres variantes de cargador descritas paso a paso, 165 hashes, regla YARA marcada `TLP:CLEAR`, configuración de AsyncRAT extraída. **No atribuye a nadie** y cita el informe de Red Akodon solo en la bibliografía, lo que es metodológicamente limpio y a la vez deja el nombre sin resolver. **No publica tabla ATT&CK** (solo dos técnicas enlazadas) ni valores de la configuración de REMCOS |
| SCILabs — «Red Akodon, a new threat actor distributing RAT to Colombia» (27-may-2024) | OSINT comercial | F | 6 | **No evaluable: el informe no pudo leerse.** El sitio responde a la petición automatizada con una redirección a un sistema antirrobot de terceros, que no se intentó eludir. **Es la fuente que da nombre al actor y la única que sostiene su condición de actor distinto**, y todo lo que este producto le atribuye proviene de las citas de Recorded Future. Brecha `G-1`. La valoración F/6 no juzga la calidad del trabajo de SCILabs: dice que no hemos podido verla |
| ¡Mucho Hacker! — correos de hospital y de la Rama Judicial usados para enviar `SVG` (31-oct-2024) | OSINT · medio especializado | C | 3 | **Citada a través de las dos fuentes primarias, no leída directamente.** Aporta el dato del hospital público como remitente y la anterioridad del método del `SVG` en Colombia. Medio pequeño, sin trayectoria verificable por nosotros |
| Securelist (Kaspersky) — mención de Chile como ubicación de actividad | OSINT comercial | B | 4 | **Citada a través de Recorded Future, no leída directamente para este informe.** Es la única mención de Chile en toda la base de colección, está en una sección de antecedentes, y no trae víctima, fecha, sector ni indicador. **No debe citarse como evidencia de exposición chilena**, y así se consigna en §E-2 |
| MITRE ATT&CK v18 — técnicas `T1027.017` y catálogo general | Marco de referencia | A | 1 | Usado para nombrar técnicas y para construir §T-2. La incorporación de `T1027.017` en 2025 es el dato que fecha la novedad del método del `SVG`. Sin aporte de contenido propio |
| Comprobación propia de ausencia de informe nuevo sobre este conjunto en 2026, 16-nov-2026 | Análisis propio / OSINT | B | 3 | **Hallazgo negativo:** la ausencia de publicación no prueba la ausencia de actividad. Consignado como contexto en §E-3, no como juicio |

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

## Anexo D — Equivalencias institucionales Colombia → Chile, para formación y para detección

> Este anexo existe para dos usos concretos: alimentar la regla `D-11` y la hipótesis
> `H-11`, y servir de guion al módulo de formación de la decisión `E-b`. **No es una lista
> de amenazas: es la lista de los trámites chilenos que un empleado no puede ignorar**, que
> es exactamente la razón por la que el señuelo funcionaría. La columna de la izquierda
> está documentada; la de la derecha es nuestra traducción y no está observada en ninguna
> campaña.

| Señuelo documentado en Colombia | Fuente | Equivalente chileno a vigilar | Términos para `D-11` |
|---|---|---|---|
| Notificación de proceso de la **Fiscalía General de la Nación** | SCILabs *(vía Recorded Future)* | Notificación de la **Fiscalía** o del **Ministerio Público** | `fiscalía`, `ministerio público`, `causa RUC`, `citación a declarar` |
| Citación del **Juzgado 06 Civil del Circuito de Bogotá** y de juzgados penales municipales nominados | SCILabs *(vía Recorded Future)*, Recorded Future | Notificación de **tribunal civil o de garantía**, con rol y materia | `juzgado civil`, `juzgado de garantía`, `rol`, `causa`, `notificación de demanda` |
| Correo desde buzón auténtico de la **Rama Judicial** (`cendoj.ramajudicial.gov.co`) | Recorded Future | Correo desde buzón del **Poder Judicial** (`pjud.cl`) o de la **Oficina Judicial Virtual** | `oficina judicial virtual`, `pjud`, `estado diario` |
| «Cobro por intereses moratorios – Radicado …» | Recorded Future | **Requerimiento de pago** o **liquidación de intereses** de la Tesorería General de la República | `tesorería general`, `requerimiento de pago`, `intereses moratorios`, `giro` |
| **Demanda laboral** con citación a audiencia | Acronis | Demanda ante **Juzgado de Letras del Trabajo**, o notificación de la **Dirección del Trabajo** | `demanda laboral`, `dirección del trabajo`, `comparendo`, `audiencia preparatoria` |
| Notificación de **alcaldía** o **gobernación** desde buzón auténtico | Recorded Future | Notificación de **municipalidad** o de **delegación presidencial regional** | `municipalidad`, `patente municipal`, `dirección de obras`, `multa` |
| Correo de **secretaría de educación** | Recorded Future | Correo de **Ministerio de Educación**, **Superintendencia de Educación** o **JUNAEB** | `mineduc`, `superintendencia de educación` |
| Correo de **hospital público** | ¡Mucho Hacker! *(vía fuentes primarias)* | Correo de **servicio de salud**, **FONASA** o **Superintendencia de Salud** | `fonasa`, `servicio de salud`, `licencia médica` |
| Phishing bancario a **Davivienda, Bancolombia, BBVA** | Recorded Future | Phishing a la banca chilena. **No se enumeran aquí: la lista de los 24 bancos está en `CTI-2026-021`, Anexo D** | — |
| — *(sin equivalente documentado en Colombia)* | — | **Servicio de Impuestos Internos**: el señuelo chileno de mayor rendimiento histórico, documentado en cinco alertas del CSIRT Nacional | `sii`, `impuestos internos`, `boleta electrónica`, `factura impaga`, `rectificatoria` |

## Anexo E — Marcos de referencia empleados

`MITRE ATT&CK v18` · `MITRE D3FEND` · `Cyber Kill Chain` · `Pirámide del Dolor` ·
`Modelo del Diamante` · `F3EAD` · `ICD 203` (lenguaje estimativo) · `ACH, supuestos
clave, pre-mortem` · `TLP 2.0` · `PAP` · `STIX 2.1 / TAXII 2.1` · `Admiralty Code`

## Anexo F — Paquete legible por máquina

- Bundle STIX 2.1: pendiente de generar. Debe modelar **tres objetos `intrusion-set` distintos y relacionados por `related-to`, no uno solo**: `Red Akodon`, `TAG-144` y `Shadow Vector`, cada uno con la delimitación de su autor, y la relación marcada con la confianza que su fuente declara —que en dos de los tres casos es ninguna—. Fundir los tres en un objeto sería tomar partido en una disputa que las fuentes no han resuelto, y perder la información de que está abierta.
- Las once cuentas de correo institucionales deben modelarse como `email-addr` con marcado explícito de **cuenta legítima comprometida** y acción permitida «solo detección», y las direcciones de VPN comercial e ISP con la misma salvedad. Es la primera vez en esta serie que una lista de indicadores puede cortar el acceso a la justicia de un tercero si se aplica mal.
- Evento MISP: pendiente. Taxonomías: `tlp`, `pap`, `admiralty-scale`, `estimative-language`, más etiquetas propias `señuelo:judicial`, `remitente:legítimo-comprometido` y `objetivo:colombia`.
- Reglas: las dos reglas Sigma de §X-4 y las doce plantillas de §X-3, versionadas con el identificador `CTI-2026-022` y estado `experimental`. **Incorporar además la regla YARA `crimeware_shadow_vector_svg` de Acronis**, que está publicada con marcado `TLP:CLEAR` y no se reproduce aquí por ser material de terceros; advertencia obligada al adoptarla: su condición se basa en palabras españolas de ámbito judicial y puede casar con `SVG` legítimos en español.
- Lista de bloqueo y lista de detección **separadas**, como en `CTI-2026-021` y por una razón aún más fuerte: aquí la lista de detección contiene buzones de juzgados reales.

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-11-16 | Emisión inicial. Elaborado sobre dos informes de proveedor de primera mano. **El informe que da nombre al actor no pudo leerse** y queda consignado como brecha `G-1` y como valoración F/6 en el Anexo B; todo lo que se le atribuye está marcado como cita de segunda mano. **La disputa de atribución no se resuelve: se consigna como hallazgo** (`KJ-5`, `H2`, `H3`). Chile entra por transferibilidad del método y no por victimología observada, lo que queda dicho en `KJ-7`, en §E-2 y en la brecha `G-4`. Sin telemetría propia: §O-4 sin evaluar | Célula CTI |

## Anexo H — Realimentación del consumidor

| Pregunta | Respuesta |
|---|---|
| ¿Respondió a su requisito? | |
| ¿Qué decisión tomó o cambió con este informe? | |
| ¿Se tomó la decisión sobre adjuntos `SVG` (E-a)? ¿Con qué resultado y con cuántas excepciones? | |
| ¿Cuántos `SVG` entraron en los últimos 90 días (X-1)? | |
| ¿Se publicó el procedimiento de verificación de notificaciones (E-b)? | |
| ¿Se leyó por fin el informe de SCILabs (G-1)? ¿Cambió algo de este producto? | |
| ¿Se ingirieron los apéndices de Recorded Future como lista de detección (G-10)? | |
