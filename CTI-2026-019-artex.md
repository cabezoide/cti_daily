---
tlp: "TLP:CLEAR"
pap: "PAP:WHITE"
id: "CTI-2026-019"
version: "1.0"
tipo: "Evaluación estratégica"
foco_regional: "Global · Latinoamérica · Chile"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "ARTEX · framework ofensivo agéntico"
fecha: "2026-11-16"
caduca: "2027-02-16"
autor: "Célula CTI"
distribucion: "Elaborado íntegramente con fuentes abiertas, incluido el FLASH FBI-20261113-001 (TLP:CLEAR) y los informes públicos de Microsoft, CrowdStrike, Google Threat Intelligence Group, Wiz, Zscaler, Censys y CERT-EU. Difusión libre conservando la atribución de las fuentes y las salvedades metodológicas de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-019
## ARTEX: intrusiones con acceso privilegiado en menos de tres horas, el plazo que la Ley 21.663 da sólo para la alerta
### Un framework agéntico publicado en julio de 2026 y retirado en octubre, hoy en manos de al menos cuatro clústeres

> **Regla de oro del producto:** todo párrafo debe responder a un requisito de
> inteligencia (PIR) y habilitar una decisión. Si un párrafo no cambia lo que
> alguien va a hacer, va al anexo o se borra.

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-019` |
| Versión / fecha | `1.0` — 2026-11-16 |
| Tipo de producto | Evaluación estratégica + perfil de capacidad adversaria (no es un perfil de actor: el sujeto es una herramienta compartida) |
| Niveles cubiertos | Estratégico · Operacional · Táctico · Técnico |
| Foco regional | Global, con lectura específica para Latinoamérica y Chile |
| Marcado de difusión | `TLP:CLEAR` · `PAP:WHITE` |
| Clasificación interna | Uso interno — no sensible |
| Requisitos atendidos | `PIR-01` (actores con intención y capacidad contra nuestro sector), `PIR-03` (nuevas capacidades adversarias que degradan nuestros controles), `PIR-05` (riesgo de terceros y cadena de suministro), `PIR-07` (superficie expuesta a Internet), `PIR-09` (indicadores tempranos de campaña) |
| Solicitante / consumidor primario | CISO · Jefatura de SOC · Ingeniería de Detección · Arquitectura Cloud e Identidad · Comité de Riesgo Operacional · Oficial de cumplimiento Ley 21.663 |
| Ventana de observación | 2026-07-26 (publicación de ARTEX) → 2026-11-16 (cierre de redacción) |
| Base de colección | 14 fuentes externas. Fuente primaria: FLASH FBI-20261113-001 (TLP:CLEAR), texto completo, incluidas sus tablas de IOC y su mapeo ATT&CK. Informes de proveedor de primera mano: Microsoft (21-oct y 6-nov), CrowdStrike (29-oct), Google Threat Intelligence Group/Mandiant (30-oct), Wiz (22-oct), Zscaler ThreatLabz (14-oct), Censys (5-nov), CERT-EU (5-nov), Check Point (5-nov), Akamai (23-oct). Documentación y contenido de detección de un fork público del framework. **Sin telemetría propia incorporada** |
| Autor (analista) | Célula CTI |
| Revisión por pares | Pendiente |
| Aprobación | Pendiente |
| Caducidad / revisión | 2027-02-16, o antes si: se publica un caso con víctima chilena nombrada; aparece un clúster que use ARTEX con cadencia humana y baja huella; o un framework sucesor (AntiFox, HexStrike, PentAGI) desplaza a ARTEX en los informes de respuesta a incidentes |
| Productos relacionados | `CTI-2026-014` (TheGentlemen), `CTI-2026-015` (Qilin), `CTI-2026-016` (LockBit 5.0), `CTI-2026-017` (FamousSparrow), `CTI-2026-018` (abuso de TLD). **Transversal a los cinco:** no describe un adversario nuevo, describe el acelerador que los adversarios conocidos ya están incorporando |
| Paquete legible por máquina | Pendiente de generar (véase §14) |

<!-- cti:note type="warn" -->

> **Limitación estructural de este producto.** Se ha elaborado con la fuente primaria
> gubernamental y con informes de proveedor de primera mano, pero **sin telemetría de la
> organización**. En consecuencia **§O-4 (nuestra exposición) está sin rellenar**: no
> sabemos cuántas aplicaciones periféricas propias están expuestas a Internet, cuántas
> aplicaciones multiinquilino de terceros tienen consentimiento vigente en nuestro tenant,
> ni si alguna credencial de larga vida nuestra figura en un volcado o respaldo histórico.
> Hasta que se rellene, las detecciones de §X-3 son plantillas y las decisiones de §E-4
> son hipótesis de política, no decisiones evaluadas.

<!-- cti:note type="warn" -->

> ⚠ **Sobre la novedad.** Ninguna técnica descrita en este informe es nueva. Kerberoasting,
> DCSync, inyección SQL, SSRF, SAML sin firmar y claves no rotadas llevan años en nuestros
> catálogos. Lo que cambia es el **tiempo de ciclo** con que se encadenan y el **número de
> objetivos simultáneos** que un operador puede sostener. Leer este informe buscando una
> técnica desconocida es leerlo mal.

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** ARTEX comprime el tiempo de intrusión por debajo de nuestro ciclo de decisión humano. El FBI documenta intrusiones que pasan de objetivo inicial a acceso privilegiado **en menos de tres horas**, y Google/Mandiant observó secuencias de ejecución en ráfagas de 2 a 25 segundos, con un caso de 27 eventos en 23 segundos. Valoramos **casi con certeza** *(95–99 %)*. **Confianza: alta.** *Base:* FLASH FBI-20261113-001 citando telemetría de Microsoft, corroborado de forma independiente por mediciones de GTIG/Mandiant y CrowdStrike.

**KJ-2.** El factor limitante de nuestra exposición no es la destreza del adversario, sino el **inventario de nuestra superficie periférica**: portales de socios y proveedores, backends móviles, aplicaciones de empleados, sistemas de apoyo comercial, servicios heredados e integraciones creadas por unidades de negocio al margen de TI. El FBI señala explícitamente que ARTEX destaca en esos activos «que reciben menos atención de seguridad que las aplicaciones emblemáticas». Valoramos **muy probable** *(80–95 %)*. **Confianza: moderada.** *Base:* FLASH FBI y Akamai (23-oct) coinciden en el criterio de selección; la aplicación a nuestro caso concreto es inferencia, no observación.

**KJ-3.** ARTEX cambia sigilo por velocidad, y por eso **es detectable**: genera cientos de eventos de registro por error y reintento, se autoidentifica en nombres de cuenta, ficheros, roles y agentes de usuario, y produce picos de volumen imposibles de confundir con actividad humana. La detección efectiva es **conductual y por velocidad**; el bloqueo por IOC fracasará. Valoramos **muy probable** *(80–95 %)*. **Confianza: alta.** *Base:* GTIG («intercambia sigilo por velocidad»), CrowdStrike (marcadores `artx`, `art18-`, `C:\ProgramData\artx5v\`), Microsoft (2.900 fallos de autenticación por minuto en el pico).

**KJ-4.** Latinoamérica ya está dentro del alcance, no en el horizonte. CrowdStrike documenta que VAPOR PANDA dirigió ARTEX contra **cancillerías latinoamericanas**, con dos ministerios de exteriores de la región efectivamente atacados y un tercero **probablemente comprometido**, entre el 17 y el 28 de octubre de 2026. Ningún país se nombra. Valoramos **probable** *(55–80 %)* que la región siga figurando en campañas de los próximos seis meses. **Confianza: moderada.** *Base:* fuente única de primera mano (CrowdStrike OverWatch), no corroborada por otro proveedor.

**KJ-5.** La retirada del repositorio original el 8 de octubre de 2026 **no redujo la disponibilidad** de la capacidad. El framework persiste en forks comunitarios —uno de ellos con más de 3.000 bifurcaciones y consola traducida al español—, copias archivadas, variantes renombradas (ScopeWeaver) y una versión comercial (ARTEX PRO). Entre 1.300 y 2.557 consolas siguen expuestas a Internet según el medidor. Valoramos **casi con certeza** *(95–99 %)*. **Confianza: alta.** *Base:* FLASH FBI, Censys (5-nov), Check Point (5-nov), GTIG, repositorio público verificado por nosotros.

**KJ-6.** El patrón trasciende a ARTEX. GTIG documenta abuso de HexStrike, CAIRN y PentAGI en respuesta a incidentes, experimentación con AgentZero, y en noviembre apareció AntiFox vinculado al acceso a secretos de producción en AWS. Construir detección **contra ARTEX** en lugar de **contra la conducta agéntica** nos deja ciegos ante el siguiente framework, que llegará en semanas, no en años. Valoramos **muy probable** *(80–95 %)*. **Confianza: moderada.** *Base:* GTIG (30-oct), CERT-EU (5-nov), reportes de prensa técnica de noviembre sobre AntiFox.

**KJ-7.** El vector de mayor impacto no es la explotación directa, sino el **abuso de relaciones de confianza ya establecidas**. Con las credenciales de una sola aplicación multiinquilino comprometida —ConnectWise Cloud Backup—, un clúster intentó autenticarse contra **más de 2.250 tenants** de Microsoft 365 aguas abajo, sin requerir inicio de sesión interactivo. Valoramos **probable** *(55–80 %)* que un compromiso de ese tipo, no una intrusión directa, sea la vía por la que esta capacidad nos alcance. **Confianza: alta.** *Base:* Microsoft (21-oct), confirmado por el FLASH del FBI.

**Qué cambiaría estos juicios:** la publicación de un caso de intrusión con ARTEX operado a cadencia humana, con pausas de horas entre fases y volumen de registro indistinguible del tráfico normal, rompería KJ-3 y con él toda la estrategia de detección de §T-4 y §X-3. El análisis de laboratorio de Simbian —2 hallazgos en modo autónomo frente a 17 guiado por un plan experto— apunta en la dirección contraria y conviene vigilarlo: un operador competente que use ARTEX con disciplina de sigilo sería un adversario distinto y peor del que describe este informe.

---

## 2. Resumen ejecutivo

ARTEX no es un grupo criminal ni un programa malicioso. Es una plataforma de pruebas de penetración autónoma, publicada en GitHub en julio de 2026 como software libre, que traduce objetivos escritos en lenguaje natural a comandos ejecutados por agentes de inteligencia artificial. Su autor la retiró el 8 de octubre tras los primeros informes de abuso; a esas alturas ya era irrelevante. Desde finales de agosto, al menos cuatro agrupaciones distintas —dos vinculadas al Estado chino, una banda financiera con base en Camboya y un actor individual de habla china— la han usado contra organizaciones de servicios financieros, gobierno, tecnología, defensa, semiconductores, energía, salud, manufactura, telecomunicaciones y servicios jurídicos.

Lo que nos importa no es la herramienta: es su efecto en el reloj. Un operador que trabajaba a mano sostenía unos 40 comandos por hora; con ARTEX se han observado más de 1.500. El FBI documenta intrusiones que llegaron a acceso privilegiado en menos de tres horas desde el primer contacto. En Chile, tres horas es exactamente el plazo que la Ley 21.663 concede para enviar la alerta temprana a la ANCI: el adversario puede haber terminado su trabajo antes de que venza nuestro primer deber legal de informar. Ninguna cadena de escalamiento que dependa de un analista localizando a un jefe, que localiza a un gerente, que autoriza una contención, cabe dentro de esa ventana.

La buena noticia es que esta velocidad es ruidosa. ARTEX se equivoca, reintenta, duplica peticiones entre subagentes y deja su propio nombre en cuentas, ficheros, roles de nube y cabeceras HTTP. Es detectable —pero por conducta y por tasa, no por indicadores. La decisión que este informe pide a Dirección no es comprar nada: es autorizar por anticipado la contención automática para un conjunto acotado de detecciones de alta fidelidad, y financiar el inventario completo de lo que tenemos expuesto a Internet, incluido lo que las unidades de negocio publicaron sin pasar por TI.

<!-- cti:cards -->

| Rasgo | Qué significa | Etiqueta |
|---|---|---|
| Opera a velocidad de máquina, no de persona | Nuestro procedimiento de escalamiento humano queda fuera de plazo por diseño, no por descuido. La única respuesta con tiempo útil es automática | `01 · velocidad` |
| Ataca la periferia, no la fachada | El activo que nos compromete no es el que auditamos cada año, es el portal de proveedores que una filial publicó en 2019 y nadie inventarió | `02 · superficie` |
| Baja la barrera de entrada, no el techo | Un actor con poca pericia técnica sostiene ahora campañas simultáneas que antes exigían un equipo. El número de adversarios capaces crece sin que crezca su sofisticación | `03 · escala` |
| Entra por la confianza que ya concedimos | Una aplicación multiinquilino comprometida aguas arriba abre 2.250 tenants aguas abajo sin un solo inicio de sesión interactivo | `04 · terceros` |
| Es sobrevivible a la retirada de su repositorio | Forks, espejos, variantes renombradas y una versión comercial. La capacidad ya no depende de su autor | `05 · persistencia` |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `3 h` | Tiempo de objetivo inicial a acceso privilegiado en varias intrusiones | Igual al plazo legal chileno para la alerta temprana a la ANCI |
| `1500` | Comandos por hora observados en actividad interactiva con ARTEX | Un operador humano sostenía hasta 40 |
| `2250` | Tenants de Microsoft 365 contra los que se intentó autenticar con las credenciales de una sola aplicación de proveedor | Vector de cadena de suministro, sin inicio de sesión interactivo |
| `67000` | Personas cuya información personal se exfiltró de instituciones financieras surcoreanas | Nombres, teléfonos, renta anual y límites de crédito |
| `200` | Organizaciones distintas atacadas por un solo clúster en 11 días | 14 países; cancillerías latinoamericanas entre ellas |
| `110000` | Objetos de Active Directory enumerados en una sola ráfaga desde un controlador de dominio | Incluida la recuperación del grupo Domain Admins |
| `1465` | Consolas ARTEX expuestas a Internet el 4 de noviembre de 2026 | El FBI estima el total «significativamente mayor» |

<!-- cti:note type="good" -->

> ✅ **Decisiones que se solicitan a Dirección.** (a) Autorizar contención automática sin escalado humano para las cinco detecciones marcadas CRÍTICO en §X-3, con criterio de reversión documentado — 15 días. (b) Encargar el inventario completo de activos expuestos a Internet con propietario nominal por activo, incluida la TI de sombra de unidades de negocio — 30 días, responsable único designado. (c) Aprobar la rotación de credenciales de larga vida de nube, aplicaciones y claves de firma de tokens, incluidas las contenidas en respaldos y exportaciones de directorio históricos — 45 días. (d) Fijar la postura de notificación bajo Ley 21.663 para un incidente que concluye antes del plazo de alerta temprana: alerta pre-redactada y autoridad delegada para enviarla — 30 días.

---

## 3. Alcance, requisitos y limitaciones

**3.1 Requisitos de inteligencia atendidos**

| Req. | Enunciado | ¿Respondido? | Dónde |
|---|---|---|---|
| PIR-01 | ¿Qué actores tienen intención y capacidad contra nuestro sector? | Sí | §O-1, §O-2, §E-2 |
| PIR-03 | ¿Qué capacidades adversarias nuevas degradan la eficacia de nuestros controles actuales? | Sí | §E-1, §T-1, §T-3 |
| PIR-05 | ¿Qué riesgo nos llega por terceros y cadena de suministro? | Sí | §O-3, §E-4 (decisión d) |
| PIR-07 | ¿Qué tenemos expuesto a Internet y quién responde por ello? | **No** — requiere inventario propio | §O-4 (sin evaluar), §14 |
| PIR-09 | ¿Qué indicadores tempranos permitirían anticipar una campaña contra nosotros? | Parcial | §O-7, §T-4 |

**3.2 Fuera de alcance.** Este informe no evalúa: el riesgo de que nuestros propios agentes de IA internos sean manipulados por inyección de instrucciones (es un problema distinto, con otro modelo de amenaza); la seguridad de los proveedores de modelos de lenguaje; el uso legítimo de ARTEX y frameworks equivalentes por nuestros equipos de red team, que requiere una política propia; y la atribución nominal de los clústeres descritos, que dejamos en manos de los servicios que tienen base para hacerla.

**3.3 Limitaciones de la colección.** (i) **Sin telemetría propia.** Todo lo que este informe dice sobre nosotros es inferencia a partir de patrones ajenos. (ii) **Sesgo de visibilidad del proveedor.** Lo que sabemos de ARTEX lo sabemos porque Microsoft, CrowdStrike, Google y Wiz tienen sensores donde lo encontraron: nube hiperescalar, identidad empresarial y endpoints Windows con EDR. La actividad contra entornos sin esa instrumentación —aplicaciones heredadas en centros de datos propios, OT, pymes proveedoras— es sistemáticamente invisible en este conjunto de fuentes, y es precisamente la superficie que el FBI describe como preferida. **El sesgo apunta a subestimar el problema.** (iii) **Recuentos en disputa.** Las cifras de consolas expuestas difieren entre medidores por un factor de dos (véase §E-2) y los recuentos de compromiso de VAPOR PANDA no son conciliables entre fuentes (9 confirmados frente a ~70 % de más de 200 objetivos). Se consignan ambos. (iv) **Discrepancias sin resolver en los datos de origen:** Microsoft publica `178.16.54[.]129` en su tabla de indicadores y `178.15.54.129` en su consulta de Sentinel; su texto menciona cuatro identificadores de aplicación afectados y solo tres son visibles en el artículo. (v) **El texto del FLASH se obtuvo por extracción automática del PDF.** El contenido de las celdas de su tabla de TTP perdió los verbos iniciales en la extracción; donde era necesario se reconstruyó el procedimiento a partir de las fuentes que el propio FLASH cita, y se indica cuando es así. (vi) **Los plazos de la Ley 21.663** se tomaron de guías de cumplimiento comerciales, no del texto oficial del Decreto 295; deben verificarse con el oficial antes de usarse como base de una decisión de cumplimiento.

**3.4 Metodología.** Disciplinas: OSINT gubernamental (FLASH del FBI, fuente primaria), OSINT comercial de proveedor (nueve informes de primera mano), medición propia de un repositorio público de código y de su material de detección. Técnicas analíticas estructuradas aplicadas: análisis de hipótesis competidoras (§O-6), comprobación de supuestos clave, pre-mortem. Marcos: MITRE ATT&CK v18, Pirámide del Dolor, Cadena de Intrusión, ICD 203 para el lenguaje estimativo, código Admiralty para la valoración de fuentes (Anexo B).

---

# NIVEL ESTRATÉGICO
### Para: Consejo · CISO · Riesgo · Legal · Cumplimiento Ley 21.663 · Horizonte: 6–24 meses

## E-1. Qué representa ARTEX en el panorama

Durante treinta años la ventaja estructural de la defensa fue el tiempo: el atacante necesitaba horas o días para encadenar reconocimiento, explotación, escalamiento y exfiltración, y ese intervalo era el espacio donde vivían nuestro SOC, nuestro proceso de escalamiento y nuestra respuesta a incidentes. ARTEX no inventa técnicas nuevas: elimina ese intervalo.

El cambio tiene tres consecuencias estructurales, y ninguna se resuelve comprando producto.

**La primera es económica.** El coste marginal de atacar una organización adicional tiende a cero. Un clúster atacó más de 200 organizaciones distintas en 14 países durante una ventana de once días, persiguiendo varias rutas de ataque en paralelo y conmutando de enfoque cuando una fallaba. Antes, la selección de objetivos era un acto de racionamiento: el adversario elegía porque no podía con todos. Ahora puede con todos, y la pregunta «¿por qué nos atacarían a nosotros?» deja de ser una pregunta: ya no hace falta una razón para estar en la lista, basta estar accesible.

**La segunda es de umbral.** El FBI es explícito: el framework «permite a actores con pericia técnica mínima ejecutar operaciones complejas y multiobjetivo simultáneamente». La población de adversarios capaces de una intrusión con movimiento lateral, escalamiento de dominio y exfiltración estructurada crece sin que crezca su sofisticación individual. Esto no significa que el techo suba —el análisis de laboratorio independiente sugiere que ARTEX sin dirección experta rinde mal—, significa que el suelo sube mucho. El riesgo se desplaza de «pocos adversarios muy buenos» a «muchos adversarios suficientemente buenos», y nuestros controles están calibrados para lo primero.

**La tercera es temporal, y es la que importa.** Varias intrusiones alcanzaron acceso privilegiado en menos de tres horas desde el objetivo inicial. Las secuencias de ejecución duran entre 2 y 25 segundos. Un caso registró 27 eventos en 23 segundos de ráfaga activa. Otro escribió y borró un blob de prueba en 330–400 milisegundos para medir permisos, y recorrió once tipos de recurso de Azure con validaciones en seco en ocho segundos. Nuestro procedimiento de respuesta no es lento por mala gestión: es que fue diseñado contra un adversario que ya no existe.

<!-- cti:cards -->

| Cambio estructural | Por qué nos afecta | Etiqueta |
|---|---|---|
| El coste marginal de un objetivo adicional tiende a cero | Dejamos de estar protegidos por irrelevancia. La selección por valor se sustituye por barrido por accesibilidad | `01 · economía` |
| La pericia deja de ser cuello de botella | Más adversarios con capacidad de intrusión completa, sin más sofisticación. Nuestros controles están calibrados contra el adversario sofisticado, no contra el numeroso | `02 · umbral` |
| El tiempo de ciclo baja por debajo del tiempo de decisión | Cualquier control que requiera un humano en la ruta crítica queda fuera de plazo. La contención debe estar pre-autorizada o no existe | `03 · reloj` |
| La confianza concedida es el nuevo perímetro | Un proveedor con una aplicación multiinquilino comprometida nos alcanza sin tocar nuestro perímetro ni autenticar un usuario | `04 · confianza` |
| La herramienta sobrevive a su autor | Retirar el repositorio no retiró la capacidad. No hay palanca de proveedor, de parche ni de orden judicial que la revierta | `05 · irreversible` |

<!-- cti:note type="info" -->

> **Nota de encuadre para el Consejo.** Conviene resistir dos lecturas erróneas y simétricas.
> La primera es el pánico: ARTEX no es una inteligencia artificial que ataca por sí sola;
> hay un operador humano dirigiendo, en los casos documentados en chino y en horario de
> China continental, que interviene en los puntos de decisión. La segunda es el desdén:
> el hecho de que use técnicas conocidas no reduce su efecto, igual que una ametralladora
> no es menos relevante por disparar las mismas balas que un fusil. La afirmación defendible
> es la intermedia: **capacidad conocida, ejecutada a una velocidad y escala nuevas, por
> adversarios que antes no alcanzaban a ejecutarla.**

## E-2. Victimología y distribución

<!-- cti:bars title="Consolas ARTEX expuestas a Internet, según quién mide" color="#e0a33e" -->

| Medidor | Consolas |
|---|---|
| Check Point (5-nov, alojaron o alojan) | 2557 |
| BadByte (nov) | 1645 |
| FBI FLASH (principios de nov) | 1600 |
| Check Point (5-nov, activas) | 1608 |
| Censys (4-nov) | 1465 |
| Hunt.io (nov) | 1300 |

<!-- cti:note type="warn" -->

> ⚠ **Leer esta tabla con cuidado.** Las seis cifras miden cosas distintas con métodos
> distintos en fechas distintas, y la diferencia entre el extremo alto y el bajo es de
> casi el doble. Censys advierte además que «parte de los equipos expuestos probablemente
> los operan evaluadores autorizados»: una consola expuesta no es prueba de actividad
> criminal. La conclusión robusta no es el número, es el orden de magnitud —miles— y su
> implicación: **el acceso a esta capacidad no es escaso.** Úsese el rango, nunca un dato
> suelto, y jamás como denominador de un cálculo de riesgo.

<!-- cti:bars title="Dónde están las consolas expuestas (Censys, 4-nov-2026)" -->

| País | Consolas |
|---|---|
| Estados Unidos | 726 |
| Hong Kong | 387 |
| China | 177 |
| Resto del mundo | 175 |

<!-- cti:bars title="Comandos por hora en actividad interactiva sobre el objetivo" color="#c0392b,#2d7d6f" -->

| Modo de operación | Comandos/hora |
|---|---|
| Con ARTEX (observado por CrowdStrike) | 1500 |
| Operador humano a mano (máximo típico) | 40 |

**Sectores atacados.** El FLASH del FBI enumera diez verticales: servicios financieros, gobierno, tecnología, defensa, semiconductores, energía, salud, manufactura, telecomunicaciones y servicios jurídicos. Es una lista tan amplia que resulta poco informativa como criterio de selección, y eso es precisamente el hallazgo: **la distribución sectorial de ARTEX se parece a la distribución de la superficie expuesta, no a la distribución del valor.** Los casos con detalle lo confirman por otra vía: Wiz documenta concentración en proveedores de TI y software —es decir, en quien tiene acceso a los demás—, y Microsoft sitúa a Storm-3358 contra instituciones financieras del sudeste asiático más un conjunto menor de entidades financieras grandes a escala global.

**Geografía de las víctimas, hasta donde se publica.** Corea del Sur (instituciones financieras, campaña financiera); Estados Unidos (19 organizaciones en farmacéutica, semiconductores, defensa, nuclear y financiero); un país europeo con su cancillería, presidencia, jefatura de gobierno y entidades de defensa, justicia, finanzas e inteligencia; un ministerio del interior de Oriente Medio; proveedores de telecomunicaciones en Estados Unidos, Bélgica y Filipinas; cancillerías en Centroamérica y Asia con ficheros ya preparados para extracción; e **instituciones de la Unión Europea**, donde CERT-EU valora como **altamente probable** que la actividad observada contra ellas involucrara el framework.

<!-- cti:note type="warn" -->

> ⚠ **Lectura regional — el dato que nos concierne.** CrowdStrike documenta que el clúster
> VAPOR PANDA dirigió esta capacidad contra **cancillerías latinoamericanas**: dos
> ministerios de relaciones exteriores de países de la región fueron atacados y un tercero
> fue **probablemente comprometido**, entre el 17 y el 28 de octubre de 2026. No se nombra
> ningún país. No hay ninguna fuente pública que sitúe a Chile dentro o fuera de ese
> conjunto, y a la fecha de cierre **no existe alerta de la ANCI ni del CSIRT Nacional sobre
> ARTEX** (comprobación propia por fuentes abiertas, 16-nov-2026). Esa ausencia de alerta
> no es evidencia de ausencia de actividad: es una brecha de colección, y está consignada
> como `G-2` en §14.

## E-3. Tendencia y pronóstico

<!-- cti:chart title="Productos públicos relevantes sobre abuso de ARTEX, por semana" cap="Mide el ciclo de divulgación, no el volumen de actividad. La curva de actividad precede a esta en semanas: el primer abuso se observó a finales de agosto y el primer informe se publicó el 7 de octubre." -->

| Periodo | Informes |
|---|---|
| 29sep | 0 |
| 6oct | 1 |
| 13oct | 3 |
| 20oct | 3 |
| 27oct | 2 |
| 3nov | 4 |
| 10nov | 3 |

De la publicación del framework al FLASH del FBI pasaron **110 días**. De la primera observación de abuso a la alerta federal, unas once semanas. Para un ecosistema de amenazas que suele tardar meses o años en consolidar una capacidad, el ciclo de adopción ha sido excepcionalmente corto, y conviene no leer la curva de divulgación como la curva del problema: cuando el FBI publica, la capacidad ya está distribuida.

La métrica independiente que mejor describe la tendencia subyacente la aporta CrowdStrike: unas 45 intrusiones con adversarios agénticos en septiembre y 126 en octubre, un crecimiento de casi el triple en un mes. Es una sola fuente y una sola serie de dos puntos; no sostiene una extrapolación, pero sí descarta la hipótesis de que esto sea un incidente aislado.

<!-- cti:cards -->

| Escenario | Desarrollo | Etiqueta |
|---|---|---|
| Normalización como utillaje estándar | ARTEX y sus sucesores se incorporan al utillaje ordinario de actores de todo el espectro, igual que ocurrió con Cobalt Strike y Mimikatz. Los informes dejan de titular con el framework y pasan a mencionarlo de pasada. La defensa se reorganiza en torno a detección por velocidad y contención automática | `Probable · 55–80 %` |
| Industrialización con sigilo | Un operador competente incorpora disciplina de sigilo: cadencia humana simulada, limitación de tasa deliberada, agentes de usuario creíbles y supresión de los marcadores autoidentificativos. Perdemos la ventaja de KJ-3 y la detección vuelve a depender de telemetría fina de identidad y nube | `Posibilidad real · 45–55 %` |
| Integración con extorsión a escala | Un grupo de ransomware como servicio integra un framework agéntico en su cadena de afiliados, convirtiendo la selección de víctimas en un barrido continuo. El tiempo de permanencia mediano de la extorsión cae de días a horas y la negociación empieza antes de que se detecte la intrusión | `Poco probable · 20–45 %` |
| Contención por el lado de los modelos | Los proveedores de modelos detectan y cortan de forma efectiva el uso agéntico ofensivo, y el ecosistema se repliega hacia modelos locales de menor capacidad. La velocidad baja y el problema se degrada a su versión de 2025 | `Remoto · 5–15 %` |

<!-- cti:note type="info" -->

> **Por qué el último escenario es remoto.** La capacidad ya se ejecuta mayoritariamente
> sobre modelos de origen chino —el FBI señala la familia DeepSeek Flash como dominante,
> «por su equilibrio de capacidades, coste relativamente bajo y ausencia de barreras
> observables cuando se enmarca como prueba de penetración»— y existe un mercado de
> revendedores de API y pasarelas autoalojadas (`CLIProxyAPI`, `New API`) cuya función es
> precisamente desacoplar al operador del proveedor. La palanca de gobernanza del modelo
> existe, pero no cubre la ruta que estos actores ya usan.

## E-4. Decisiones que este informe pide al nivel estratégico

<!-- cti:table highlight="Chile|ANCI|21.663|regional" -->

| # | Decisión | Fundamento | Plazo |
|---|---|---|---|
| E-a | Autorizar **contención automática sin escalado humano** para las cinco detecciones marcadas CRÍTICO en §X-3, con criterio de reversión y registro de auditoría documentados. Designar quién responde por un falso positivo con impacto operativo | KJ-1: tres horas hasta acceso privilegiado hace que cualquier control con humano en la ruta crítica llegue tarde por diseño | 15 días |
| E-b | Encargar el **inventario completo de activos expuestos a Internet**, con propietario nominal por activo, incluyendo portales de socios y proveedores, backends móviles, aplicaciones de empleados, sistemas de apoyo comercial, servicios heredados, integraciones de terceros y publicaciones de unidades de negocio al margen de TI. Responsable único, no comité | KJ-2: el criterio de selección del adversario es la accesibilidad, no el valor. No podemos defender lo que no sabemos que tenemos | 30 días |
| E-c | Aprobar la **rotación de credenciales de larga vida**: claves de cuenta de almacenamiento, tokens SAS, secretos de principal de servicio, credenciales de publicación, y claves de firma de tokens y de preautenticación — **incluidas las contenidas en respaldos y exportaciones de directorio históricos** | CrowdStrike documenta una intrusión que usó una exportación de directorio de 2022 y una clave de cliente VPN filtrada en 2024 para forjar un token de administrador. Una clave que no se rotó nunca caduca para el adversario | 45 días |
| E-d | Revisar **todas las aplicaciones multiinquilino de terceros** con consentimiento vigente o pasado en nuestro tenant, buscando por identificador de aplicación y no por nombre visible, y aplicar mínimo privilegio a sus permisos y concesiones. Para clientes de ConnectWise Cloud Backup: revisar actividad desde al menos el 1 de octubre de 2026 | KJ-7: 2.250 tenants alcanzables desde una sola aplicación comprometida, sin inicio de sesión interactivo | 30 días |
| E-e | Fijar la **postura de notificación bajo Ley 21.663** para un incidente que puede concluir antes de que venza el plazo de alerta temprana: alerta temprana pre-redactada con campos mínimos, autoridad delegada y nominal para enviarla sin esperar validación completa, y criterio explícito de qué se informa cuando aún no se sabe el alcance | El plazo de alerta temprana (3 h) coincide con el tiempo de intrusión completa observado. Esperar a tener certeza garantiza incumplir; informar sin alcance confirmado es la opción conforme | 30 días |
| E-f | Definir **política de egreso para endpoints de API de modelos de lenguaje** desde segmentos de servidor y de infraestructura: lista de permitidos explícita, denegación por defecto, y alerta sobre tráfico a pasarelas y revendedores no aprobados | Un servidor de aplicaciones que habla con una API de modelos es, salvo excepción justificada, un agente ofensivo operando desde dentro | 45 días |
| E-g | Encargar al área de red team la **política de uso interno de frameworks agénticos**: aislamiento, prohibición de credenciales de producción, alcance forzado en configuración y no en instrucciones, y revisión de forks antes de ejecutarlos | Un investigador perdió el control de un agente que escapó de su entorno de pruebas y alcanzó una aplicación interna de un tercero. Nuestro propio red team es un vector | 60 días |
| E-h | Evaluar la adopción de **controles de engaño** (señuelos, cuentas trampa, tarpits) en la superficie expuesta, con contención automática asociada | Microsoft informa que en sus pruebas el engaño «redujo el tráfico de ataque que alcanzaba activos reales». Un agente que optimiza por progreso aparente es particularmente susceptible a un señuelo que le dé progreso falso | 90 días |

---

# NIVEL OPERACIONAL
### Para: Jefatura de SOC · Respuesta a Incidentes · Threat Hunting · Arquitectura de Identidad · Horizonte: semanas–meses

## O-1. Identificación: la herramienta y los clústeres que la usan

Esta sección existe para prevenir el error analítico más probable con este material: tratar «ARTEX» como si fuera un actor. No lo es. Es utillaje compartido, y fusionar bajo un solo nombre a los grupos que lo usan produciría un adversario quimérico que no existe en ninguna parte.

**La herramienta y sus variantes**

| Designación | Origen | Grado de equivalencia |
|---|---|---|
| `ARTEX` | Autodenominación del proyecto original (`Autumn-27`, GitHub, 26-jul-2026, AGPL-3.0) | Referencia |
| `ARTEX PRO` | Versión comercial de terceros | Derivado comercial — capacidades no verificadas públicamente |
| `ScopeWeaver` | Fork renombrado, «variación localizada» según GTIG | Derivado — equivalente funcional presumido, no verificado |
| `artex-global` | Fork comunitario público, consola en inglés/coreano/chino/**español**/japonés | Derivado — autodeclarado «solo para uso autorizado, defensivo y de detección»; publica su propio material de detección |
| `artex-ko` | Nombre anterior del mismo fork en su registro de contenedores | Equivalente al anterior |

**Los clústeres que la operan**

| Designación | Origen | Grado de equivalencia |
|---|---|---|
| `Storm-0940` | Microsoft | Clúster alineado con el Estado chino, activo desde 2021. Responsable asignado del compromiso de ConnectWise |
| `UNC7228` | Google Threat Intelligence Group | **Solapamiento declarado** con Storm-0940 por GTIG |
| `VAPOR PANDA` | CrowdStrike | Clúster de nexo chino. **Declarado explícitamente separado** de Storm-0940 por CrowdStrike |
| `Storm-3358` | Microsoft | Clúster con base en Camboya, con motivación financiera, contra el sector financiero del sudeste asiático |
| Actor sin nombre (campaña surcoreana) | Zscaler / CrowdStrike | Actor de habla china con motivación financiera, valorado por Zscaler con **confianza moderada**. CrowdStrike lo considera «probablemente un individuo con base en China» más que un grupo estatal confirmado |

<!-- cti:note type="warn" -->

> ⚠ **Nota de tradecraft — el riesgo de fusión indebida es alto en este caso.** Wiz afirma
> que su actividad observada **solapa** con Storm-0940; CrowdStrike afirma que VAPOR PANDA
> es **separado** de Storm-0940. Ambas afirmaciones pueden ser ciertas simultáneamente y no
> hay base pública para unificarlas. Lo único que comparten los cinco clústeres es la
> herramienta: **ningún proveedor publica solapamiento de infraestructura, de víctimas ni
> de TTP más allá de ARTEX.** Si en nuestra telemetría aparece un indicador de esta lista,
> la conclusión legítima es «actividad compatible con el uso de ARTEX», nunca «somos
> objetivo de un actor estatal chino».

## O-2. Atribución: qué se puede y qué no se puede sostener

| Eje de atribución | Valoración | Confianza |
|---|---|---|
| Clúster técnico | Al menos cinco agrupaciones distinguibles usan la misma herramienta; se distinguen entre sí por infraestructura, víctimas, motivación y huso horario de operación | Alta |
| Grupo organizado | Dos clústeres presentan disciplina de grupo (Storm-0940 activo desde 2021, Storm-3358 con utillaje propio post-explotación); uno se valora como individuo | Moderada |
| Nexo estatal | Storm-0940 y VAPOR PANDA: alineamiento con el Estado chino valorado por Microsoft y CrowdStrike respectivamente. Storm-3358: criminal, sin nexo estatal planteado | Moderada |
| Identidad nominal | Ninguna. El FBI **no nombra ningún patrocinador estatal** en el FLASH | Baja |
| Autoría de la herramienta | `Autumn-27`, desarrollador público que declaró finalidad de prueba autorizada y retiró el repositorio tras los informes de abuso. **No es un actor de amenaza** y no debe tratarse como tal | Alta |

*Razonamiento a favor del nexo chino en los dos clústeres estatales:* CrowdStrike recuperó las instrucciones del operador escritas en chino, marcadas con el prefijo `【人类指令】` («instrucción humana») y con marcas de tiempo en horario estándar de China; una de ellas ordenaba a los agentes «buscar máquinas Windows del dominio sin 猎鹰 [el sensor de CrowdStrike], juzgando por `tasklist` y listados de carpetas». El objetivo —cancillerías, defensa, semiconductores, nuclear, telecomunicaciones— es coherente con una misión de recopilación estatal y no con una monetización.

*Contraargumento que debe consignarse:* la herramienta es pública y gratuita, los modelos usados son de acceso comercial, y el idioma de las instrucciones acredita al operador, no a su patrocinador. Un actor criminal de habla china produciría artefactos indistinguibles. Para nuestros fines operativos la distinción es además poco relevante: **la respuesta técnica a una intrusión con ARTEX es la misma sea quien sea quien lo opere.** Donde sí cambia es en la decisión de notificación y en la respuesta institucional, y ahí la atribución debe dejarse a quien tiene base para hacerla.

## O-3. Qué hace escalar a esta capacidad

Tres cosas, y conviene entenderlas porque cada una tiene un contraataque distinto.

**La arquitectura de agentes.** ARTEX es un *arnés*, no un modelo: está escrito en Go, lleva una consola Next.js incorporada, y distribuye el ciclo de ataque entre seis subagentes especializados. En el fork público verificable los roles son: `goals` descompone el objetivo y extrae el alcance; `planner` es el único productor de intenciones y las despacha a una cola; `worker` —tres en paralelo por tarea en la configuración por defecto— reclama una intención, ejecuta herramientas vía shell y HTTP, escribe el resultado y termina; `mainagent` atiende el diálogo con el humano; `retester` revalida hallazgos. La memoria son dos grafos: uno de activos, global y compartido entre tareas; otro de exploración, por tarea, con nodos de objetivo, intención, hecho, hallazgo e indicio. El bucle es dirigido por eventos: un cambio en el grafo despierta al planificador, que despacha, los trabajadores escriben, y eso vuelve a despertar al planificador. Termina cuando un objetivo queda probado o cuando un despertar no despacha nada. **El contraataque es el engaño:** un bucle que optimiza por progreso aparente en un grafo es manipulable con progreso falso.

**El desacoplamiento del modelo.** ARTEX no incluye modelo propio. Se conecta a proveedores externos —el FBI enumera Anthropic Claude, OpenAI GPT, DeepSeek, GLM, Grok y Kimi— y en las instancias controladas por atacantes predominan los modelos de origen chino, con la familia DeepSeek Flash dominante. El actor de la campaña surcoreana configuró DeepSeek v4.1-flash como respaldo principal y GLM-5.3 y Grok 4.6 como razonamiento suplementario. VAPOR PANDA operó sobre DeepSeek más un segundo modelo comercial que CrowdStrike no pudo identificar, y sus agentes de planificación consumieron del orden de **1.400 millones de tokens de entrada en una sola intrusión**. Existe además un mercado de reventa de API y de pasarelas autoalojadas (`CLIProxyAPI`, `New API`) y un dominio revendedor identificado (`xcai[.]pro`). **El contraataque es el egreso:** el tráfico hacia un proveedor de modelos desde un segmento de servidores es una señal de altísima fidelidad, y las pasarelas autoalojadas son el modo de evadirla.

**La ausencia de alcance forzado.** El framework trae una lista de bloqueo por defecto que excluye entidades gubernamentales y universidades, pero —como Zscaler verificó en el código fuente— **no cubre instituciones financieras**. El alcance es una instrucción, no una restricción: se declara en lenguaje natural y el agente lo interpreta. Esto explica tanto el abuso como el accidente: un agente de un investigador escapó de su entorno de pruebas y alcanzó una aplicación interna de un tercero. **El contraataque, para nuestro propio uso interno, es forzar el alcance en configuración y en red, nunca en el prompt** (decisión E-g).

## O-4. Nuestra exposición

<!-- cti:note type="gap" -->

> ⬛ **Sección sin evaluar — requiere telemetría e inventario internos.** Un informe con esta
> sección vacía es inteligencia genérica, no inteligencia propia. Las preguntas de abajo son
> el trabajo mínimo para convertirla en lo segundo, y cada una tiene un responsable asignado.

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| X-1 | ¿Cuántas aplicaciones propias están publicadas a Internet, y cuántas de ellas no figuran en el inventario oficial de TI? ¿Quién responde nominalmente por cada una? | Descubrimiento externo + inventario + revisión con unidades de negocio | TI / Arquitectura |
| X-2 | ¿Alguna de nuestras aplicaciones de página única (SPA) incluye credenciales, claves o endpoints internos en sus paquetes JavaScript o en sus mapas de origen (`*.js.map`, `/assets/config.json`, `/env.js`)? | Revisión de artefactos de compilación publicados | Desarrollo / AppSec |
| X-3 | ¿Qué aplicaciones multiinquilino de terceros tienen consentimiento vigente o pasado en nuestro tenant, con qué permisos, y cuál es el identificador de aplicación y el Object ID local de cada principal de servicio? | Microsoft Entra — buscar por identificador de aplicación, no por nombre | Identidad |
| X-4 | ¿Tenemos interfaces de administración de nube, publicación de aplicaciones (Kudu/SCM), hipervisores o plataformas de respaldo accesibles desde Internet? | Inventario de nube + descubrimiento externo | Infraestructura / Nube |
| X-5 | ¿Existen credenciales de larga vida sin rotar: claves de cuenta de almacenamiento, tokens SAS, secretos de principal de servicio, claves de firma de tokens, claves de preautenticación? ¿Y en respaldos y exportaciones de directorio de años anteriores? | Inventario de secretos + revisión de respaldos históricos | Identidad / Nube |
| X-6 | ¿Validamos la firma de las aserciones SAML en todos los puntos de federación? ¿Exigimos IMDSv2 en todas las instancias? | Revisión de configuración de federación y de nube | Identidad / Nube |
| X-7 | ¿Qué cobertura real de EDR tenemos en servidores, y específicamente en los que consideramos «no alcanzables desde Internet»? La enumeración de cobertura de sensor es una TTP observada | Consola de EDR contra inventario de activos | SOC / Endpoint |
| X-8 | ¿Registramos y conservamos los eventos necesarios para las hipótesis de §T-4: plano de control de nube, plano de datos de almacenamiento, inicios de sesión de principal de servicio, auditoría de Entra, actividad de Microsoft Graph, registros web con agente de usuario? ¿Con qué retención? | Revisión de fuentes del SIEM | Ingeniería de Detección |
| X-9 | ¿Hay alguna instancia de ARTEX o framework agéntico equivalente ejecutándose en nuestros rangos, puesta por un equipo propio o por un proveedor? Buscar puertos `8787` y `8788` | Barrido interno + descubrimiento externo | SOC / Red team |
| X-10 | ¿Nuestros portales de socios y de empleados aplican límite de tasa, autorización del lado del servidor por registro y limitación de campos en la respuesta? | Revisión de AppSec sobre endpoints de consulta | AppSec |

## O-5. Cronología

<!-- cti:timeline -->

| Fecha | Hecho | Traza |
|---|---|---|
| `2026-07-26` | **Publicación de ARTEX en GitHub** por el usuario `Autumn-27`, bajo licencia AGPL-3.0, como framework de pruebas de penetración autorizadas | Global |
| `2026-08` (finales) | **Primer abuso observado.** GTIG sitúa aquí el inicio de la adopción «por un rango diverso de actores a lo largo de todo el espectro de motivaciones» | Global |
| `2026-09` | Storm-0940 comienza a usar ARTEX, según telemetría de Microsoft | Global |
| `2026-09` (finales) | Primera observación de la campaña contra instituciones financieras surcoreanas (Zscaler) | Global |
| `2026-10-07` | CrowdStrike publica el primer informe de abuso: actor desconocido contra el sector financiero surcoreano | Global |
| `2026-10-08` | **El autor retira el repositorio** y lo pasa a código cerrado tras los informes de abuso. Sin efecto en la disponibilidad | Global |
| `2026-10-10` → `10-14` | Pulverización de contraseñas entre tenants desde `144.172.64[.]99`: 327 cuentas en 8 organizaciones, más de 151.000 autenticaciones fallidas, pico de 2.900 por minuto el 11-oct, ~98 % de la actividad terminó en bloqueo de cuenta. Sin autenticación exitosa en esta fase | Global |
| `2026-10-14` | Zscaler publica la campaña surcoreana: PII de ~67.000 personas exfiltrada; fase de monetización apoyada en sesiones de Claude Code para buscar canales de venta | Global |
| `2026-10-15` | **Divulgación pública del compromiso de ConnectWise** (Huntress). Desde esta fecha, uso de credenciales de aplicación robadas desde el mismo rango de IP | Global |
| `2026-10-16` | Aviso inicial de ConnectWise, con una IP coincidente exactamente con la de la pulverización previa | Global |
| `2026-10-17` | **Inicio de la campaña de VAPOR PANDA: cancillerías latinoamericanas entre los objetivos.** Más de 200 organizaciones en 14 países durante los 11 días siguientes | LATAM |
| `2026-10-21` | Microsoft publica el compromiso de cadena de suministro de Storm-0940: intentos de inicio de sesión contra más de 2.250 tenants, más de 200 inicios de sesión en menos de 4 minutos con 4 credenciales de aplicación | Global |
| `2026-10-22` | Wiz publica la expansión de Storm-0940 contra proveedores de TI y software y proveedores de identidad | Global |
| `2026-10-23` | Akamai publica el análisis de superficies de ataque desatendidas, que el FBI citará como base de su sección de mitigaciones | Global |
| `2026-10-28` | Fin de la ventana de 11 días de VAPOR PANDA. **Dos cancillerías latinoamericanas atacadas, una tercera probablemente comprometida** | LATAM |
| `2026-10-29` | CrowdStrike publica VAPOR PANDA: 9 organizaciones con post-explotación confirmada, 12 más con pulverización o barrido, 1.400 millones de tokens de entrada en una intrusión | Global |
| `2026-10-30` | GTIG/Mandiant publica «ARTEX and Friends»: arquitectura de seis subagentes, 491 URL rotatorias de `webhook.site`, 110.000+ objetos de AD enumerados, y la presencia de HexStrike, CAIRN y PentAGI en respuesta a incidentes | Global |
| `2026-11-04` | Censys mide 1.465 consolas ARTEX expuestas; 155 de ellas (10,6 %) alojan además otra amenaza detectada | Global |
| `2026-11-05` | **CERT-EU valora como altamente probable** que la actividad observada contra instituciones de la UE involucrara el framework. Check Point publica 2.557 sistemas que alojaron ARTEX, 10 de ellos con su base de datos completa expuesta | Global |
| `2026-11-06` | Microsoft publica la expansión al sector financiero: Storm-3358, con base en Camboya, usa ARTEX con RAT de código abierto (WISP, vshell, AdaptixC2) | Global |
| `2026-11-13` | **FLASH FBI-20261113-001 (TLP:CLEAR).** Diez sectores afectados, más de 1.600 consolas expuestas, tablas de IOC y mapeo ATT&CK. Primera fuente gubernamental | Global |
| `2026-11-16` | Cierre de este informe. **Sin alerta de la ANCI ni del CSIRT Nacional sobre ARTEX** (comprobación propia por fuentes abiertas) | Chile |

## O-6. Hipótesis alternativas consideradas

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| H1 — ARTEX es un acelerador real que comprime el ciclo de intrusión por debajo del ciclo de decisión defensivo | Consistente con las mediciones independientes de tres proveedores y con la fuente gubernamental: <3 h a acceso privilegiado, ráfagas de 2–25 s, >1.500 comandos/hora. Ninguna fuente la contradice | `Retenida` |
| H2 — Es sobre todo exageración de proveedores con interés comercial en dramatizar la IA ofensiva | Inconsistencia decisiva: la fuente primaria es un FLASH del FBI sin producto que vender, y las cifras duras —67.000 personas, 2.250 tenants, 151.000 autenticaciones fallidas— son recuentos verificables, no adjetivos. **Pero el núcleo de verdad debe conservarse:** los titulares sobre «IA autónoma atacando» no se sostienen (hay operador humano en los puntos de decisión) y las cifras de consolas expuestas se han usado con laxitud | `Poco probable · 20–35 %` |
| H3 — El riesgo real no es la velocidad sino la escala: lo nuevo es el número de objetivos simultáneos, no el tiempo por objetivo | Parcialmente consistente y **complementaria de H1, no alternativa**. Se retiene como matiz: la escala explica por qué estamos en la lista; la velocidad explica por qué no llegamos a tiempo. Ambas tienen contraataques distintos (inventario frente a automatización) | `Retenida como matiz` |
| H4 — ARTEX sin dirección experta rinde mal, y por tanto el adversario relevante sigue siendo el operador competente | Apoyada por análisis de laboratorio independiente (2 hallazgos en modo autónomo frente a 17 con plan experto) y por la propia observación de GTIG de subagentes que se sobrescriben entre sí y errores repetidos. **Se retiene como advertencia:** implica que el peor escenario es ARTEX en manos buenas, no ARTEX solo | `Retenida como advertencia` |
| H5 — Los clústeres que usan ARTEX son en realidad uno solo, o están coordinados | Sin evidencia. Ningún proveedor publica solapamiento de infraestructura, víctimas o TTP más allá de la herramienta compartida, y CrowdStrike declara explícitamente la separación. Se consigna para que no se reabra en cada reunión | `Descartada` |
| H6 — El retiro del repositorio y la presión sobre proveedores de modelos degradarán la capacidad en los próximos meses | Inconsistente con lo observado: el retiro no afectó la disponibilidad (forks, espejos, versión comercial) y la ejecución ya se apoya mayoritariamente en modelos fuera del alcance de esa presión, con un mercado de reventa que la elude | `Poco probable · 20–35 %` |

**Supuesto clave.** Que la velocidad observada es intrínseca al modo de operación agéntico y no una elección del operador. **Si es falso** —si los operadores pueden ralentizar deliberadamente sin perder la ventaja de escala— entonces toda la estrategia de detección por velocidad de §T-4 y §X-3 pierde fidelidad, y la defensa debe reconstruirse sobre telemetría fina de identidad y de plano de control de nube, que es más costosa y que hoy no tenemos completa.

**Pre-mortem.** Es mayo de 2027 y este informe resultó equivocado. Los tres finales más probables: **(1)** nos concentramos en las detecciones de velocidad, el adversario introdujo limitación de tasa deliberada y pasó por debajo de todos los umbrales que fijamos; **(2)** el inventario de activos expuestos se encargó, se hizo y nadie mantuvo el proceso, de modo que seis meses después la superficie real volvió a divergir del inventario y nos comprometieron por un activo publicado en marzo; **(3)** acertamos en todo lo técnico y nos comprometieron por un proveedor pequeño sin EDR, sin registros y sin obligación contractual de notificarnos, con el que nunca ejercimos la revisión de terceros que esta sección pedía.

## O-7. Indicadores y señales de alerta

| # | Indicador observable | Qué señalaría | Disciplina | Responsable |
|---|---|---|---|---|
| I-1 | Aparición de un caso público con víctima nombrada en Chile o con sector chileno identificable | El paso de riesgo regional a riesgo propio; activa revisión de este informe antes de su caducidad | OSINT | Célula CTI |
| I-2 | Publicación de alerta de la ANCI o del CSIRT Nacional sobre frameworks agénticos | Cambio del marco de notificación y posible instrucción técnica sectorial aplicable | OSINT gubernamental | Célula CTI / Cumplimiento |
| I-3 | Informe que documente ARTEX operado con cadencia humana y baja huella de registro | Rompe KJ-3; obliga a rediseñar §T-4 y §X-3 | OSINT comercial | Célula CTI / Ingeniería de Detección |
| I-4 | Integración de un framework agéntico en un programa de ransomware como servicio | Materializa el tercer escenario de §E-3; cambia el perfil de impacto de recopilación a extorsión | OSINT + foros criminales | Célula CTI |
| I-5 | Sucesor que desplace a ARTEX en los informes de respuesta a incidentes (AntiFox, HexStrike, PentAGI u otro) | Confirma KJ-6 y valida la decisión de detectar conducta en lugar de herramienta | OSINT comercial | Célula CTI |
| I-6 | Aparición de credenciales o secretos propios en volcados públicos, repositorios o exportaciones de directorio antiguas | Precondición directa del vector de token forjado documentado por CrowdStrike | OSINT / vigilancia de filtraciones | Célula CTI / Identidad |
| I-7 | Consola ARTEX expuesta en nuestros rangos o en los de un proveedor conocido | Instalación propia no gobernada, o proveedor comprometido u operando contra nosotros | Descubrimiento externo | SOC |
| I-8 | Aviso de un proveedor de software multiinquilino sobre compromiso de sus credenciales de aplicación | Replica el patrón ConnectWise; activa la revisión de E-d en modo urgente | Gestión de terceros | Riesgo de Terceros / Identidad |

---

# NIVEL TÁCTICO
### Para: Analistas de SOC · Ingeniería de Detección · Threat Hunting · Horizonte: días–semanas

## T-1. Cadena de intrusión

<!-- cti:stages title="Tres etapas, una sola ráfaga continua" dwell="next" -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 01 · Periferia | Entrada por el activo que nadie inventarió | Portales de socios y proveedores · backends móviles · apps de empleados · servicios heredados · credenciales de administrador embebidas en paquetes JavaScript de SPA · API sin autenticación · SSRF · XXE · inyección SQL y de comandos · IDOR · subida anónima de ficheros · aserciones SAML sin firmar · JWT con `alg:none` · abuso de recuperación de cuenta · configuraciones VPN robadas · confianza entre cuentas de nube desde un tenant socio · federación B2B de un proveedor más débil |
| Etapa 02 · Identidad y nube | Mapeo de permisos y escalamiento a velocidad de máquina | Comprobación subsegundo de permisos efectivos de tokens SAS, principales de servicio, credenciales Kudu y claves de cuenta de almacenamiento · escritura y borrado de blob de prueba en 330–400 ms · barrido de validación en seco de ARM sobre 11 tipos de recurso en 8 s · `DryRun` en IAM de AWS · enumeración de usuarios, buzones y aplicaciones vía Microsoft Graph · forja de token de administrador con claves no rotadas · Kerberoasting · DCSync del `krbtgt` · delegación restringida basada en recursos · lectura de contraseñas LAPS · plantillas de AD CS · enumeración de cobertura de EDR para localizar hosts sin sensor |
| Etapa 03 · Impacto | Persistir, recolectar, sacar | Webshells `.jsp`/`.aspx`, incluida la plantada vía envenenamiento de `general_log` de MySQL · abuso de API administrativas de Kudu · RAT de código abierto (WISP, vshell, AdaptixC2) descargados con `curl` y `netcat` · puerta trasera BLOODALCHEMY por carga lateral de DLL sobre binario legítimo renombrado a `svchost.exe` · creación de cuentas con `is_admin=true` y nombres que contienen `ArtexProbe` · adición de secretos a aplicaciones OAuth existentes · claves SSH e IP elásticas nuevas · volcado de bases de datos · lectura masiva de blobs · lectura de buzones en servidor de correo comprometido · volúmenes de 100 GB para preparar extracción · salida por 491 URL rotatorias de `webhook.site` · túneles con Chisel y SoftEther · Tor, proxies SOCKS y relés comprometidos |

**Permanencia:** de objetivo inicial a acceso privilegiado **en menos de 3 horas** en varias intrusiones; ráfagas de ejecución de 2 a 25 segundos, con un caso de 27 eventos en 23 segundos; sesiones completas de 24 a 30 horas con ráfagas de 20 a 60 minutos.

<!-- cti:note type="info" -->

> **Dónde se rompe la cadena más barato.** Las tres etapas no tienen el mismo coste de
> interrupción. La **etapa 01 se corta con inventario y con mínimo privilegio en la
> publicación**, que es trabajo de arquitectura y no de SOC. La **etapa 02 se corta con
> rotación de credenciales de larga vida y validación de firma SAML**: es la intervención
> con mejor relación coste-efecto de todo este informe, porque invalida de golpe el vector
> de token forjado. La **etapa 03 solo se corta con detección y contención automática**, y
> es la más cara. Invertir de atrás hacia adelante es el error habitual.

## T-2. Mapa MITRE ATT&CK

<!-- cti:matrix -->

| Táctica | ID | Técnica | Procedimiento observado |
|---|---|---|---|
| Desarrollo de recursos | T1588.007 | Obtain Capabilities: Artificial Intelligence | Adopción de ARTEX, framework agéntico público, más suscripción a modelos de lenguaje comerciales (DeepSeek, GLM, Grok) y reventa de API (`xcai[.]pro`, `CLIProxyAPI`, `New API`) |
| Reconocimiento | T1595 | Active Scanning | Más de 500 peticiones web probando nombres y extensiones de fichero, discriminando por código de respuesta `200` o `403`; barrido con nuclei, httpx, katana, ffuf; línea base con una ruta inexistente antes de la ráfaga de fuzzing |
| Reconocimiento | T1595.002 | Active Scanning: Vulnerability Scanning | Escaneo activo de vulnerabilidades sobre aplicaciones periféricas con herramientas estándar orquestadas por los agentes |
| Descubrimiento | T1580 | Cloud Infrastructure Discovery | Mapeo automático de permisos efectivos de credenciales de Azure con comprobaciones subsegundo; barrido de validación en seco de despliegues ARM sobre 11 tipos de recurso |
| Descubrimiento | T1526 | Cloud Service Discovery | Enumeración de servicios de nube accesibles con la credencial obtenida; inventario de recursos previo a la lectura de secretos |
| Descubrimiento | T1087.004 | Account Discovery: Cloud Account | Enumeración de usuarios, buzones y aplicaciones vía Microsoft Graph con autenticación solo de aplicación; validación de nombres de usuario sin preautenticación |
| Descubrimiento | T1069.003 | Permission Groups Discovery: Cloud Groups | Descubrimiento de grupos y roles de nube asociados a la identidad comprometida |
| Acceso inicial | T1190 | Exploit Public-Facing Application | Inyección SQL y de comandos, XXE, SSRF, IDOR, bypass de autenticación y subida anónima de ficheros contra aplicaciones periféricas; más de 60 variaciones de rutas SSO probadas en dos minutos |
| Acceso inicial | T1078 | Valid Accounts | Pulverización de contraseñas contra Okta y Entra ID; 327 cuentas en 8 organizaciones con más de 151.000 fallos y pico de 2.900 por minuto |
| Acceso inicial | T1133 | External Remote Services | Uso de configuraciones VPN robadas y de claves de cliente VPN recuperadas de correo filtrado para alcanzar la red interna |
| Acceso inicial | T1195 | Supply Chain Compromise | Compromiso de ConnectWise Cloud Backup y uso de sus credenciales de aplicación contra más de 2.250 tenants aguas abajo; modificación de infraestructura de distribución de aplicaciones iOS vía credenciales de nube expuestas |
| Acceso inicial | T1199 | Trusted Relationship | Abuso de confianza entre cuentas de nube desde un tenant socio externo y pivote por federación B2B desde un proveedor más débil |
| Acceso a credenciales | T1606.002 | Forge Web Credentials: SAML Tokens | Aserciones SAML sin firmar aceptadas por el punto de federación; forja de token de administrador a partir de claves de preautenticación no rotadas contenidas en una exportación de directorio de 2022 |
| Acceso a credenciales | T1552.001 | Unsecured Credentials: Credentials in Files | Contraseñas de administrador embebidas en paquetes JavaScript de aplicaciones de página única; secretos en variables de entorno, IaC y scripts de despliegue |
| Acceso a credenciales | T1552.005 | Unsecured Credentials: Cloud Instance Metadata API | Consulta al servicio de metadatos de instancia vía XXE para obtener un rol con permiso de ejecución de comandos sobre miles de instancias |
| Acceso a credenciales | T1552.006 | Unsecured Credentials: Group Policy Preferences | Búsqueda de credenciales en preferencias de directiva de grupo durante el reconocimiento interno |
| Acceso a credenciales | T1558.003 | Steal or Forge Kerberos Tickets: Kerberoasting | Ejecución de scripts de Kerberoasting para cosechar tiques de servicio |
| Acceso a credenciales | T1555 | Credentials from Password Stores | Acceso a bóveda de credenciales interna (PasswordState) y lectura de contraseñas LAPS |
| Acceso a credenciales | T1555.006 | Credentials from Password Stores: Cloud Secrets Management Stores | Lectura de secretos a escala en múltiples Azure Key Vault, con operación de desenvoltura de clave observada |
| Acceso a credenciales | T1110.003 | Brute Force: Password Spraying | Pulverización con cadencia mediana de ~1 segundo en ráfagas de 20 a 60 minutos, con agente de usuario distinto por ráfaga |
| Persistencia | T1505.003 | Server Software Component: Web Shell | Webshells `.jsp` y `.php`, una de ellas plantada mediante `SET GLOBAL general_log_file` + `SET GLOBAL general_log = 1` en MySQL; ficheros `cl1217.jsp`, `f1219a.jsp`, `z1219.jsp`; webshells R57 y WSO identificadas |
| Persistencia | T1078.004 | Valid Accounts: Cloud Accounts | Creación de cuentas administrativas en nube y uso de credenciales de aplicación de proveedor sin inicio de sesión interactivo |
| Persistencia | T1098.001 | Account Manipulation: Additional Cloud Credentials | Adición de secretos a principales de servicio y a aplicaciones OAuth existentes para asegurar reingreso |
| Persistencia | T1098.003 | Account Manipulation: Additional Cloud Roles | Autoasignación del rol de Administrador Global por parte de una aplicación; asignación de rol Owner |
| Persistencia | T1136 | Create Account | Creación de cuentas con el indicador `is_admin=true` en minutos tras descubrir una bandera administrativa escribible; nombres que contienen `ArtexProbe` |
| Ejecución | T1059 | Command and Scripting Interpreter | Ejecución de comandos arbitrarios vía API administrativas de Kudu; `curl` y `netcat` para descargar RAT |
| Ejecución | T1059.001 | Command and Scripting Interpreter: PowerShell | Scripts de enumeración iterativa de PowerShell contra controladores de dominio; scripts generados dinámicamente y descargados con `curl` nativo |
| Ejecución | T1651 | Cloud Administration Command | Uso de un rol de nube con permiso para emitir comandos administrativos sobre miles de instancias |
| Escalamiento de privilegios | T1134.001 | Access Token Manipulation: Token Impersonation/Theft | Suplantación de token administrativo para leer buzones en el entorno objetivo |
| Escalamiento de privilegios | T1484.002 | Domain or Tenant Policy Modification: Trust Modification | Abuso de delegación restringida basada en recursos (RBCD) para alcanzar privilegio de dominio |
| Evasión de defensas | T1574.001 | Hijack Execution Flow: DLL | BLOODALCHEMY: binario legítimo GameHook renombrado a `svchost.exe` carga lateralmente `graphics-hook-filter64.dll`, que descifra `graphics-hook_config.bin` |
| Evasión de defensas | T1036.005 | Masquerading: Match Legitimate Resource Name or Location | Renombrado del binario portador como `svchost.exe`; nombres de fichero y rutas que imitan recursos legítimos de captura de vídeo |
| Evasión de defensas | T1562.001 | Impair Defenses: Disable or Modify Tools | No se observó desactivación de EDR; en su lugar, **selección de hosts sin sensor** tras inventariar la cobertura (véase T1518.001) |
| Descubrimiento | T1518.001 | Software Discovery: Security Software Discovery | Instrucción explícita del operador: localizar máquinas Windows del dominio sin el sensor de EDR, juzgando por `tasklist` y listados de carpetas |
| Descubrimiento | T1087.002 | Account Discovery: Domain Account | Enumeración de más de 110.000 objetos de Active Directory desde un controlador de dominio, con recuperación del grupo Domain Admins; listado de cuentas de servicio administradas por grupo |
| Movimiento lateral | T1550.003 | Use Alternate Authentication Material: Pass the Ticket | Intentos de Pass-the-Ticket contra controladores de dominio |
| Movimiento lateral | T1550.002 | Use Alternate Authentication Material: Pass the Hash | Intentos de Pass-the-Hash **bloqueados por la protección de endpoint** donde el sensor estaba presente y operativo |
| Movimiento lateral | T1021.006 | Remote Services: Windows Remote Management | Movimiento por WinRM hacia controladores de dominio |
| Movimiento lateral | T1557.001 | Adversary in the Middle: LLMNR/NBT-NS Poisoning and SMB Relay | Relé Kerberos y envenenamiento para reutilizar material de autenticación |
| Recolección | T1530 | Data from Cloud Storage | Lectura masiva de blobs tras confirmar permisos de lectura con la prueba de escritura y borrado |
| Recolección | T1005 | Data from Local System | Interrogación de bases de datos SQL de respaldo y extracción de ~400 KB de resultados en ~20 consultas |
| Recolección | T1114.002 | Email Collection: Remote Email Collection | Lectura de buzones en servidor de correo comprometido, con token administrativo forjado |
| Recolección | T1074.001 | Data Staged: Local Data Staging | Preparación local de datos antes de la extracción |
| Recolección | T1074.002 | Data Staged: Remote Data Staging | Creación de volúmenes de 100 GB y scripts de arranque personalizados en instancias EC2 para cosechar y preparar datos |
| Mando y control | T1071.001 | Application Layer Protocol: Web Protocols | Devolución de resultados de comando sobre HTTP a 491 URL rotatorias de `webhook.site`; comunicación de BLOODALCHEMY con dominios C2 propios |
| Mando y control | T1090 | Proxy | Enrutamiento a través de proxies residenciales y de servicios de proxy |
| Mando y control | T1090.003 | Proxy: Multi-hop Proxy | Cadenas con Tor, proxies SOCKS y relés comprometidos |
| Mando y control | T1572 | Protocol Tunneling | Túneles con Chisel y SoftEther |
| Impacto | T1485 | Data Destruction | No observado como objetivo. **Relevante por omisión:** las campañas documentadas son de recopilación y robo, no destructivas; un cambio aquí sería un cambio de perfil de amenaza |

<!-- cti:note type="warn" -->

> ⚠ **Dos notas de precisión sobre esta tabla.** La primera: el FLASH del FBI publica
> `T11558.003`, que no existe; es evidentemente `T1558.003` (Kerberoasting) y así se
> consigna. La segunda: las técnicas marcadas como «no observado» (`T1562.001`, `T1485`)
> se incluyen deliberadamente porque **su ausencia es un hallazgo**. Este adversario no
> apaga el EDR: busca dónde no está. Una detección construida sobre la expectativa de
> manipulación del sensor no se disparará nunca.

## T-3. Dónde atacamos en la Pirámide del Dolor

<!-- cti:pyramid -->

| Nivel | Qué contiene en este informe y qué vale | Valor |
|---|---|---|
| Hashes | Tres hashes de BLOODALCHEMY en el Anexo A. Son el único artefacto binario estable del informe, y solo cubren a un clúster. Sirven para retrohunt y para bloqueo; no sirven para detectar el uso de ARTEX, que no deja binario propio en el objetivo | Base · valor trivial |
| IP · Dominios | 25 direcciones y 4 dominios en el Anexo A. El propio FBI advierte que son «infraestructura observada históricamente» y que las IP de nube se reasignan. Una de ellas (`144.172.64[.]99`) apareció primero en pulverización y luego en uso de credenciales robadas: valiosa como pivote de investigación, pobre como regla de bloqueo | Valor bajo |
| Artefactos | **Aquí hay más de lo habitual, y es el regalo de este adversario.** Nombres de cuenta con `ArtexProbe`, ficheros `artex-probe-*`, roles de nube con prefijo `artx-`, comentarios administrativos `art18-`, directorio `C:\ProgramData\artx5v\`, agentes de usuario `artex-enrich/1.0`, `norma/0.4` y `artex-selfupdate`, puertos `8787`/`8788`, fichero `traffic/_ca/mitmproxy-ca-cert.pem`, tablas `exploration_nodes` y `agent_prompts`. Duraderos entre versiones **mientras el operador no se moleste en cambiarlos**, y hasta ahora no se ha molestado | Valor medio |
| Herramientas | Nmap, curl, wget, netcat, sqlmap, nuclei, httpx, subfinder, katana, ffuf, dalfox, bbot, Impacket, jadx, Chromium headless vía Playwright. Todas legítimas y todas presentes en cualquier red con un equipo de pruebas. Detectar por contexto —qué host, qué hora, qué secuencia, qué volumen—, nunca por presencia | Valor alto |
| TTP | **El comportamiento agéntico es el único nivel que no se puede eludir sin perder la ventaja:** ráfagas comprimidas, cientos de fallos con variaciones incrementales, peticiones duplicadas por subagentes que se pisan, pruebas de permisos subsegundo, y egreso hacia una API de modelos desde un servidor. Aquí debe concentrarse todo el esfuerzo de ingeniería de detección | Cima · valor máximo |

## T-4. Hipótesis de caza prioritarias

<!-- cti:accordion critical="^(H-1|H-2|H-3|H-4)\b" regional="^(H-13|H-14)\b" -->

**H-1 — Velocidad en el plano de control de nube.** Una sola identidad —usuario, principal de servicio o rol— ejecuta un número de operaciones distintas del plano de control de nube en una ventana que ningún humano puede sostener. Fuente: registros de actividad de ARM, CloudTrail, `CloudAuditEvents`. Ventana: 60 segundos, agrupando por identidad; umbral inicial sugerido 30 operaciones distintas, a calibrar contra una semana de línea base propia. Esta es la hipótesis madre del informe: cubre a cualquier framework agéntico y no depende de ningún indicador. Fidelidad esperada alta tras calibración; falsos positivos conocidos: pipelines de IaC (Terraform, ARM, CloudFormation), herramientas de etiquetado masivo y de gestión de configuración, que deben exceptuarse **por identidad nominal y no por patrón**.

**H-2 — Prueba de permisos de almacenamiento: escribir y borrar en menos de medio segundo.** Secuencia de escritura de blob seguida de su borrado por la misma identidad con una separación inferior a 500 ms, especialmente si se repite en varios contenedores. Fuente: registros del plano de datos de almacenamiento (`CloudStorageAggregatedEvents`, diagnósticos de Azure Storage, acceso a objetos de S3). Observado con precisión: 330–400 ms. Ninguna aplicación legítima comprueba sus propios permisos así. Fidelidad esperada muy alta; requiere que el registro del plano de datos esté habilitado, lo que no es el valor por defecto y es la brecha `G-3` de §14.

**H-3 — Barrido de validación en seco.** Validaciones de despliegue ARM (`deployments/validate`) sobre múltiples tipos de recurso en segundos, o llamadas a API de AWS con el indicador `DryRun` encadenadas con `PassRole` y consultas al servicio de metadatos. Observado: 11 tipos de recurso en 8 segundos. Fuente: plano de control de nube. Fidelidad alta; falsos positivos: herramientas de validación de plantillas en CI, exceptuables por identidad.

**H-4 — Egreso a API de modelos de lenguaje desde segmentos que no deberían hablar con ellas.** Conexiones salientes a `api.anthropic.com`, `api.deepseek.com`, `open.bigmodel.cn`, `api.x.ai` u otros proveedores desde subredes de servidores, de infraestructura o de gestión. Ampliar a pasarelas y revendedores autoalojados: `CLIProxyAPI`, `New API`, y el dominio `xcai[.]pro`. Añadir la variante económica: anomalías de consumo de tokens o de facturación en nuestras propias suscripciones de modelos. Fuente: registros de proxy, DNS, firewall de salida. Fidelidad muy alta en segmentos donde el uso de modelos no está justificado; **esta hipótesis es la que mejor sobrevive al cambio de framework**, porque ningún agente funciona sin hablar con un modelo.

**H-5 — Inicio de sesión de principal de servicio desde infraestructura nueva.** Autenticación de un principal de servicio desde un ASN, proveedor de alojamiento o geografía no vistos antes para esa identidad, seguida de enumeración de directorio vía Microsoft Graph con autenticación solo de aplicación. Fuente: `EntraIdSpnSignInEvents`, `GraphAPIAuditEvents`, registros de auditoría de Entra. Revisar **por separado los inicios exitosos y los fallidos**, y no limitar la revisión a las IP publicadas. Fidelidad alta; es el patrón exacto del compromiso de ConnectWise.

**H-6 — Aplicación que se concede privilegio a sí misma.** Adición de credenciales o secretos a un principal de servicio o a una aplicación OAuth existente; asignación de rol privilegiado a una aplicación; autoasignación del rol de Administrador Global mediante una operación de adición de miembro a rol; nuevos propietarios de aplicación. Fuente: auditoría de Microsoft Entra. Fidelidad muy alta: estas operaciones son raras y deberían tener un cambio aprobado detrás. Toda ocurrencia sin cambio aprobado es incidente, no alerta.

**H-7 — Webshell en ruta inesperada y envenenamiento de registro de base de datos.** Ficheros `*.jsp`, `*.aspx` o `*.php` escritos en directorios servidos por la web que no provienen de un despliegue conocido. Complementarlo con el vector indirecto: cambios en `general_log_file` y activación de `general_log` en MySQL, que es cómo se plantó una de las webshells observadas, y que además deja el registro de la base de datos como fichero servible. Fuente: auditoría de integridad de ficheros, registros de la base de datos, registros del servidor web. Fidelidad alta; falsos positivos: despliegues legítimos, resolubles exigiendo correlación con el proceso y la cuenta que escribió el fichero.

**H-8 — Marcadores autoidentificativos del framework.** Buscar en línea de comandos, nombres de fichero, nombres de cuenta, nombres de rol y comentarios: `artx`, `artex`, `ArtexProbe`, `artex-probe-`, roles con prefijo `artx-`, comentarios `art18-`, y el directorio `C:\ProgramData\artx5v\`. Fuente: telemetría de endpoint, auditoría de directorio, registros de nube. Fidelidad extremadamente alta y coste de implementación casi nulo. **Advertencia explícita:** son triviales de cambiar y su ausencia no prueba nada. Son una red de seguridad barata, no una estrategia.

**H-9 — Agentes de usuario del framework y de su SDK.** `artex-enrich/1.0` (sonda de enriquecimiento, concurrencia 4, una petición GET por activo, sin redirecciones ni keep-alive), `norma/0.4` (herramienta de obtención web del SDK subyacente, **compartida con otras herramientas basadas en el mismo SDK**), `artex-selfupdate` (llamada de autoactualización, visible solo en el egreso del host operador) y `ReconProbe/1.0`. Fuente: registros web, WAF, proxy. Fidelidad alta para el primero, media para el segundo por compartición. El framework **no fuerza un agente de usuario sobre el tráfico de las herramientas**, de modo que la mayoría del tráfico llevará el agente por defecto de nmap, sqlmap, ffuf, curl o Python.

**H-10 — Secuencia de lectura de la aplicación antes del ataque.** Patrón de alta fidelidad porque describe el razonamiento del agente, no su utillaje: petición de mapas de origen (`*.js.map`), de ficheros de configuración (`/assets/config.json`, `/env.js`) o de especificación de API (`/swagger/?format=openapi`), seguida en minutos por peticiones a rutas internas que **solo se mencionan en esos ficheros**. Añadir la línea base que el agente establece antes de fuzzear: una petición a una ruta deliberadamente inexistente para aprender cómo responde el servidor al 404. Fuente: registros del servidor web. Fidelidad muy alta; prácticamente no tiene equivalente legítimo.

**H-11 — Abuso de autenticación en secuencia agéntica.** Encadenamiento, por el mismo origen o la misma sesión, de: validación de nombre de usuario sin preautenticación, petición de token de restablecimiento (`/forgot_password`, `POST /api/v1/Users/GeneratePasswordResetToken`, respuesta `204`), callback OAuth con código manifiestamente inválido (`code=AAAA`), y JWT con `{"alg":"none"}` enviado a la ruta de SSO. Fuente: registros de aplicación y de proveedor de identidad. Fidelidad muy alta: **un JWT con `alg:none` es siempre un ataque**, nunca un error de cliente.

**H-12 — Pulverización con firma de cadencia agéntica.** Fallos de autenticación con separación mediana de ~1 segundo, en ráfagas de 20 a 60 minutos, con cambio de agente de usuario entre ráfagas, y con una proporción de bloqueos de cuenta que domina la actividad (~98 % en el caso medido). Añadir el indicador volumétrico: más de 100.000 fallos en un día, pico de 2.900 por minuto. Fuente: registros de inicio de sesión del proveedor de identidad. Fidelidad alta; **el bloqueo masivo de cuentas es en sí mismo un incidente de disponibilidad** aunque ninguna autenticación tenga éxito, y debe tratarse como tal.

**H-13 — Enumeración en nuestros portales de socios y de empleados.** Consultas secuenciales y número de registros por sesión anormalmente alto contra endpoints de consulta de clientes, especialmente en portales fuera del núcleo de negocio. Este es el patrón exacto por el que se exfiltró la información de 67.000 personas en Corea del Sur, y es la hipótesis con mayor probabilidad de aplicarnos directamente. Fuente: registros de aplicación con identificador de sesión y recuento de registros devueltos. Fidelidad alta si el registro incluye el recuento de registros por respuesta, lo que habitualmente no ocurre: brecha `G-4` de §14.

**H-14 — Consola del framework en nuestros propios rangos.** Puertos `8787` (consola y API) y `8788` (proxy de grabación MITM) escuchando en activos propios o de proveedores; imagen o contenedor Docker con `artex` en el nombre; base de datos PostgreSQL con las tablas `exploration_nodes`, `assets`, `companies`, `activity`, `agent_prompts`; fichero `traffic/_ca/mitmproxy-ca-cert.pem`; ruta `/setup` servida; marcador de auditoría `【ARTEX 平台管控·非目标防御】`. Fuente: barrido interno, inventario de contenedores, osquery. Fidelidad extremadamente alta. **Dos hallazgos posibles y ambos importan:** una instalación de nuestro propio red team sin gobierno, o una instalación del adversario dentro de nuestra red.

**H-15 — Salida hacia servicios de recolección fuera de banda.** Tráfico desde servidores hacia `webhook.site` y servicios equivalentes de OAST, túneles y compartición de ficheros. Observado: 491 URL rotatorias del mismo servicio en una sola operación. Fuente: proxy, DNS, firewall de salida. Fidelidad muy alta desde segmentos de servidor; un servidor de producción no tiene ninguna razón legítima para hablar con un capturador de peticiones.

**H-16 — Reconocimiento de cobertura de EDR.** Secuencias de `tasklist`, enumeración de servicios y listados de directorios de instalación de productos de seguridad, ejecutadas iterativamente a través de varios hosts por la misma cuenta. Fuente: telemetría de endpoint. Fidelidad media-alta; es la precondición directa del movimiento lateral hacia los hosts sin sensor, de modo que **detectarla aquí es la última oportunidad antes de perder visibilidad**.

## T-5. Brechas de visibilidad que hay que cerrar primero

| Brecha | Por qué importa aquí |
|---|---|
| Registro del plano de datos de almacenamiento deshabilitado (valor por defecto en Azure y AWS) | Deja ciegas `H-2` y `H-15`, y con ellas la detección más específica y más barata de todo el informe |
| Inicios de sesión de principal de servicio no monitorizados, o monitorizados solo en caso de éxito | Deja ciega `H-5`, que es el patrón del compromiso de cadena de suministro de mayor impacto conocido |
| Auditoría de Microsoft Entra no ingerida en el SIEM, o con retención inferior a 90 días | Deja ciega `H-6` y hace imposible la revisión retrospectiva desde el 1 de octubre de 2026 que exige la decisión E-d |
| Registros de aplicación sin recuento de registros devueltos ni identificador de sesión | Deja ciega `H-13`, la hipótesis con mayor probabilidad de aplicarnos |
| Sin registro de agente de usuario en el servidor web o en el WAF | Degrada `H-9` y `H-10`; el agente de usuario es gratuito de registrar y se descarta por costumbre |
| Sin control ni registro de egreso en segmentos de servidor | Deja ciegas `H-4` y `H-15`, las dos hipótesis que sobreviven al cambio de framework |
| Cobertura de EDR incompleta en servidores considerados internos | Convierte `H-16` en una alerta sin consecuencia: sabremos que buscan el hueco, pero el hueco seguirá ahí |
| Sin correlación por velocidad en el SIEM (reglas de umbral por identidad y ventana corta) | Deja ciega `H-1`, la hipótesis madre. Es un problema de reglas, no de datos: los eventos ya están |

---

# NIVEL TÉCNICO
### Para: Ingeniería de detección · Automatización · TIP/SIEM · Vida útil: días–semanas

## X-1. Arsenal y capacidad

| Propiedad | Valor |
|---|---|
| Lenguaje y forma de despliegue | Go, con consola Next.js incorporada. Despliegue por Docker Compose o binario compilado (`CGO_ENABLED=0 go build -tags embedui -o artex ./cmd/artex`). Supervisor `start.sh` que reinicia el proceso |
| Arquitectura de agentes | Seis subagentes: `goals` (descomposición de objetivo y extracción de alcance), `planner` (único productor de intenciones), `worker` (3 en paralelo por tarea por defecto; ejecuta vía shell y HTTP), `mainagent` (diálogo con el operador), `retester` (revalidación de hallazgos) |
| Memoria | Dos grafos en PostgreSQL. Grafo de activos global (`root_domain`, `subdomain`, `ip`, `service`, `app`, `endpoint`, agrupados por compañía) y grafo de exploración por tarea (`goal`, `intent`, `fact`, `finding`, `hint`; aristas `spawns`, `derived_from`, `yields`, `proves`). Anclas en `exploration_anchors` unen ambos |
| Modelos soportados | Sin modelo propio. Proveedores: Anthropic Claude, OpenAI GPT, DeepSeek, GLM (Zhipu), Grok, Kimi, Ollama local, y cualquier servicio compatible con la API de OpenAI. Predominio observado: familia DeepSeek Flash |
| Utillaje incorporado | nmap, nuclei, httpx, subfinder, katana, ffuf, dalfox, sqlmap, bbot, curl, wget, netcat, ripgrep, npm, Impacket, jadx, Playwright con Chromium headless. Soporte de servidores MCP y de «skills» (manuales en Markdown: `api-recon`, `api-security`, `codeaudit`, `edr-bypass-re`, `patch-diff`, `php2shell`, `playwright-cli`, `scopesentry`, entre otras) |
| Puertos por defecto | `8787` consola web y API · `8788` proxy de grabación MITM · `5173` frontend en modo desarrollo · `5432` PostgreSQL · `11434` Ollama si se usa como backend local |
| Credenciales iniciales | Sin credenciales por defecto. Primer arranque por token de configuración emitido en el registro del contenedor, ruta `/setup`, cuenta administrativa `ARTEX`. Variables de instalación desatendida: `ARTEX_SETUP_TOKEN`, `ARTEX_ADMIN_PASSWORD` |
| Capacidad C2 | GTIG lo califica de «plataforma de mando y control ofensiva», pero no se ha documentado protocolo ni baliza propios: el C2 observado usa `curl` nativo contra URL rotatorias de `webhook.site`, más RAT de terceros (WISP, vshell, AdaptixC2) y túneles Chisel/SoftEther |
| Trazabilidad propia | Proxy MITM con CA propia que graba todo el tráfico de los trabajadores; capa de guarda que retiene llamadas de herramienta para aprobación, con reglas regex en base de datos; registro de auditoría con marcador fijo en cada llamada bloqueada |
| Criptografía | No aplica: no hay cifrador ni carga propia. El material criptográfico relevante es el que **roba y forja** (claves `krbtgt`, claves de firma de tokens, claves de preautenticación, tokens SAS) |
| Limitación operativa observada | Sin limitación de tasa hacia el objetivo: la cadencia depende de la herramienta que el modelo invoca. Subagentes que se sobrescriben mutuamente al perseguir el mismo objetivo, generando peticiones duplicadas y errores repetidos |

<!-- cti:note type="info" -->

> **Por qué este cuadro es más útil que una lista de hashes.** ARTEX no deja binario propio
> en la víctima: el artefacto está en la **máquina del operador**, no en la nuestra. Las
> únicas excepciones son los RAT y la puerta trasera de terceros de la etapa 03, y los
> ficheros con nombres autoidentificativos que el framework crea por descuido. Toda
> detección construida sobre «el ejecutable de ARTEX» es un esfuerzo mal dirigido.

## X-2. Artefactos persistentes entre versiones

<!-- cti:cards -->

| Categoría | Artefactos | Etiqueta |
|---|---|---|
| Nombres autoidentificativos en la víctima | `ArtexProbe` en nombres de cuenta · ficheros `artex-probe-*` con numeración incremental de cinco dígitos · roles de nube con prefijo `artx-` · comentarios administrativos `art18-` · directorio `C:\ProgramData\artx5v\` · cadenas `artx` o `artex` en línea de comandos | `autoidentificación` |
| Agentes de usuario | `artex-enrich/1.0` · `norma/0.4` (compartido con otras herramientas del mismo SDK) · `artex-selfupdate` · `ReconProbe/1.0` · además de los agentes por defecto de las herramientas: `curl/7.88.1`, `Python-urllib/3.12`, `python-requests/2.31.0`, `python-requests/2.34.2`, `aws-cli/1.46.1`, y ~15 cadenas de Chrome suplantadas | `red` |
| Webshells observadas | `cl1217.jsp` · `f1219a.jsp` · `z1219.jsp` · webshells R57 y WSO en PHP · plantadas también vía `SET GLOBAL general_log_file` + `SET GLOBAL general_log = 1` | `persistencia web` |
| Puerta trasera de terceros (BLOODALCHEMY) | Binario legítimo GameHook renombrado a `svchost.exe` · `graphics-hook-filter64.dll` (cargador) · `graphics-hook_config.bin` (carga cifrada) · ruta de proyecto interna `D:\ProjectX\Merman_New\` | `endpoint` |
| RAT de código abierto | WISP · vshell · AdaptixC2, descargados con `curl` y `netcat` | `endpoint` |
| Host del operador (si lo encontramos en nuestra red) | Puertos `8787` y `8788` escuchando · contenedor o imagen con `artex` en el nombre · `traffic/_ca/mitmproxy-ca-cert.pem` · `traffic/_index/index.sqlite` · directorio `traffic/_blobs/` · tablas PostgreSQL `exploration_nodes`, `assets`, `companies`, `activity`, `agent_prompts`, `task_scope`, `exploration_anchors` · variables `HTTP_PROXY` y de confianza de CA inyectadas en subprocesos de los trabajadores · marcador de auditoría `【ARTEX 平台管控·非目标防御】` | `instalación propia` |
| Artefactos de nube | Cuentas creadas con `is_admin=true` · claves SSH nuevas · IP elásticas asignadas · instancias `t3.micro` persistentes · volúmenes de 100 GB para preparación de datos · secretos añadidos a aplicaciones OAuth existentes | `nube` |

## X-3. Lógica de detección prioritaria

<!-- cti:detections -->

**D-1 · CRÍTICO — Velocidad imposible en el plano de control de nube**

```
cloud_control_plane_event
| summarize distinct_operations = dcount(operation_name),
            events = count()
          by identity_id, bin(timestamp, 1m)
| where distinct_operations >= 30
| exclude identity_id IN (<lista nominal de identidades de automatización aprobadas>)
```

→ Contención automática: deshabilitar la identidad y revocar sus tokens de sesión, sin escalado humano. Notificar en paralelo. El criterio de reversión debe estar documentado antes de activar la regla, y la lista de exclusión debe ser **nominal y versionada**, nunca un patrón.

**D-2 · CRÍTICO — Prueba de permisos por escritura y borrado de blob**

```
storage_data_plane_event
| where operation IN ("PutBlob", "DeleteBlob", "PutObject", "DeleteObject")
| summarize ops = make_list(operation), ts = make_list(timestamp)
          by identity_id, container, bin(timestamp, 5s)
| where ops contains write AND ops contains delete
      AND delta_ms(ts) < 500
```

→ Contención automática: revocar la credencial empleada (token SAS, clave de cuenta o secreto de principal de servicio) y aislar su uso. Ninguna aplicación legítima comprueba sus permisos escribiendo y borrando en menos de medio segundo.

**D-3 · CRÍTICO — Aplicación que se concede privilegio a sí misma**

```
EntraAuditLogs
| where OperationName IN ("Add member to role",
                          "Add app role assignment to service principal",
                          "Add service principal credentials",
                          "Add owner to application",
                          "Consent to application")
| where InitiatedBy_type == "Application"
      OR TargetResource_type == "ServicePrincipal"
| where PrivilegedRole == true OR ConsentScope has_any ("Directory.ReadWrite.All",
                                                         "Mail.ReadWrite",
                                                         "Application.ReadWrite.All")
```

→ Contención automática: suspender la concesión y bloquear el principal de servicio. Toda ocurrencia sin un cambio aprobado asociado se trata como incidente confirmado, no como alerta a triar.

**D-4 · CRÍTICO — JWT sin firma o aserción SAML sin validar en el punto de federación**

```
(http_request.body CONTAINS "eyJhbGciOiJub25lIn0"
 OR jwt.header.alg IN ("none", "None", "NONE"))
AND http_request.path MATCHES "(?i)/(sso|saml|oauth|auth|login)"
```

→ Contención automática: rechazar y bloquear el origen; alerta de severidad máxima. Un JWT con `alg:none` no tiene explicación benigna. Verificar en la misma acción que el punto de federación **valida la firma**: si la petición no fue rechazada por la aplicación, el hallazgo es una vulnerabilidad, no solo un ataque.

**D-5 · CRÍTICO — Egreso a API de modelos de lenguaje desde segmento de servidores**

```
network_connection
| where src_subnet IN (<segmentos de servidor, infraestructura y gestión>)
| where dst_domain has_any ("api.anthropic.com", "api.deepseek.com",
                            "open.bigmodel.cn", "api.x.ai",
                            "api.openai.com", "xcai.pro")
      OR dst_process has_any ("CLIProxyAPI", "new-api")
```

→ Contención automática: bloquear la conexión y aislar el host de origen para triaje. Es la detección con mejor relación entre fidelidad y longevidad de todo el informe: **sobrevive al cambio de framework**, porque ningún agente opera sin hablar con un modelo. Exige lista de permitidos previa para los sistemas con uso de IA justificado.

**D-6 · ALTO — Inicio de sesión de principal de servicio desde infraestructura nueva**

```
EntraIdSpnSignInEvents
| join kind=leftanti (
    EntraIdSpnSignInEvents
    | where Timestamp between (ago(90d) .. ago(1d))
    | distinct ServicePrincipalId, AutonomousSystemNumber
  ) on ServicePrincipalId, AutonomousSystemNumber
| where ResultType == 0 OR ResultType != 0
```

→ Investigación prioritaria en menos de 30 minutos; revisar actividad posterior en Microsoft Graph. Revisar **exitosos y fallidos por separado** y no limitar la revisión a las IP del Anexo A.

**D-7 · ALTO — Lectura de la aplicación seguida de rutas internas no publicadas**

```
web_request
| where path MATCHES "(?i)\.(js\.map)$|/assets/config\.json|/env\.js|/swagger/\?format=openapi"
| join kind=inner (
    web_request
    | where path IN (<rutas internas no enlazadas, derivadas del inventario de API>)
  ) on client_ip
| where time_delta < 10m
```

→ Bloqueo del origen y revisión de AppSec sobre el artefacto filtrado. Si el mapa de origen o el fichero de configuración está publicado, la corrección es retirarlo, no solo bloquear la IP.

**D-8 · ALTO — Webshell escrita en ruta servida**

```
file_create
| where path MATCHES "(?i)\.(jsp|jspx|aspx|asmx|php|phtml)$"
| where path IN (<directorios servidos por el servidor web>)
| where actor_process NOT IN (<procesos de despliegue aprobados>)
```

→ Aislamiento del host y preservación del fichero antes de su eliminación. Complementar con alerta sobre cambios de `general_log_file` y activación de `general_log` en motores MySQL.

**D-9 · ALTO — Marcadores autoidentificativos del framework**

```
process.command_line CONTAINS_ANY ("artx", "artex")
OR file.path CONTAINS_ANY ("C:\\ProgramData\\artx5v\\", "artex-probe-")
OR account.name CONTAINS_ANY ("ArtexProbe", "artx")
OR cloud.role.name STARTSWITH "artx-"
OR http.user_agent IN ("artex-enrich/1.0", "artex-selfupdate", "ReconProbe/1.0")
```

→ Investigación inmediata. Coste de implementación casi nulo y fidelidad altísima. **No cuenta como estrategia:** un operador que cambie una cadena de texto la elude por completo.

**D-10 · MEDIO — Pulverización con cadencia agéntica y tormenta de bloqueos**

```
signin_logs
| where ResultType IN (50126, 50053, 50055)
| summarize failures = count(),
            accounts = dcount(UserPrincipalName),
            user_agents = dcount(UserAgent),
            lockouts = countif(ResultType == 50053)
          by SourceIp, bin(Timestamp, 20m)
| where accounts >= 20 AND failures >= 200
      AND lockouts * 1.0 / failures > 0.5
```

→ Bloqueo del origen y revisión de la política de bloqueo de cuentas. **Tratar la tormenta de bloqueos como incidente de disponibilidad por sí misma**, aunque ninguna autenticación tenga éxito.

**D-11 · MEDIO — Salida hacia servicio de recolección fuera de banda desde servidor**

```
network_connection
| where src_subnet IN (<segmentos de servidor>)
| where dst_domain has_any ("webhook.site", "requestbin", "interact.sh",
                            "oast.fun", "pipedream.net", "burpcollaborator.net")
```

→ Bloqueo y triaje del host. Añadir los dominios equivalentes que aparezcan en el catálogo propio de OAST.

**D-12 · MEDIO — Consola del framework escuchando en activo propio**

```
listening_port IN (8787, 8788)
OR docker_image MATCHES "(?i)artex"
OR file.path ENDSWITH "traffic/_ca/mitmproxy-ca-cert.pem"
OR postgres_table IN ("exploration_nodes", "agent_prompts", "exploration_anchors")
```

→ Verificación inmediata de propiedad: si no hay un red team propio que la reclame por escrito, se trata como compromiso. Si lo hay, se traslada a la política de la decisión E-g.

<!-- cti:note type="warn" -->

> ⚠ **Regla de operación — esta es la parte que hay que decidir, no implementar.**
> Las detecciones D-1 a D-5 deben ejecutar **contención automática sin escalado humano**.
> No es una preferencia de ingeniería: con un tiempo a acceso privilegiado inferior a tres
> horas y ráfagas de ejecución de segundos, una cadena de escalamiento que pase por un
> analista, un turno y una autorización llega después del impacto. El coste de esa decisión
> es real y debe asumirse explícitamente: un falso positivo en D-1 deshabilita una identidad
> de automatización y puede detener un pipeline. Por eso la lista de exclusión es nominal y
> versionada, el criterio de reversión se documenta antes de activar la regla, y **se
> designa por nombre a quien responde por el impacto operativo de un falso positivo**.
> Activar estas reglas sin esa designación previa garantiza que se desactiven en el primer
> incidente, que es el peor de los resultados posibles.

<!-- cti:note type="gap" -->

> ⬛ **Estado de este material.** Las doce consultas son **plantillas en pseudocódigo, no
> reglas probadas.** Los nombres de tabla y campo se han escrito en la nomenclatura de
> Microsoft Defender XDR y Sentinel donde existe equivalente público, pero deben traducirse
> al esquema real de nuestro SIEM, y **todos los umbrales son valores iniciales a calibrar
> contra al menos una semana de línea base propia**. Publicarlas como reglas activas sin ese
> paso producirá una avalancha de falsos positivos y el descrédito de todo el informe.

## X-4. Consultas de caza

Microsoft publica consultas de caza avanzada propias para la actividad de Storm-0940 y Storm-3358; donde existan, deben usarse esas antes que estas, porque están escritas contra el esquema real. Las siguientes cubren las hipótesis que Microsoft no publica.

```kql
// H-1 · Velocidad en el plano de control de nube — ventana de 60 s por identidad
// Calibrar el umbral contra 7 días de línea base antes de activar.
CloudAuditEvents
| where Timestamp > ago(24h)
| extend Identity = coalesce(AccountObjectId, AccountUpn, tostring(RawEventData.identity))
| summarize Operaciones = dcount(OperationName),
            Eventos = count(),
            Muestra = make_set(OperationName, 12)
        by Identity, bin(Timestamp, 1m)
| where Operaciones >= 30
| order by Operaciones desc
```

```kql
// H-2 · Escritura y borrado de blob en menos de 500 ms por la misma identidad
CloudStorageAggregatedEvents
| where Timestamp > ago(7d)
| where ActivityType in ("PutBlob", "DeleteBlob")
| sort by AccountObjectId asc, Timestamp asc
| extend AnteriorTipo = prev(ActivityType), AnteriorTs = prev(Timestamp),
         AnteriorId = prev(AccountObjectId)
| where AccountObjectId == AnteriorId
      and AnteriorTipo == "PutBlob" and ActivityType == "DeleteBlob"
      and datetime_diff('millisecond', Timestamp, AnteriorTs) < 500
| project Timestamp, AccountObjectId, AccountTenantId, ResourceId, LatenciaMs = datetime_diff('millisecond', Timestamp, AnteriorTs)
```

```kql
// H-5 · Principal de servicio autenticando desde ASN nunca visto para esa identidad
let LineaBase = EntraIdSpnSignInEvents
    | where Timestamp between (ago(90d) .. ago(1d))
    | distinct ServicePrincipalId, AutonomousSystemNumber;
EntraIdSpnSignInEvents
| where Timestamp > ago(1d)
| join kind=leftanti LineaBase on ServicePrincipalId, AutonomousSystemNumber
| summarize Intentos = count(), Exitosos = countif(ErrorCode == 0),
            IPs = make_set(IPAddress, 20), ASN = any(AutonomousSystemNumber)
        by ServicePrincipalId, ServicePrincipalName, bin(Timestamp, 1h)
| order by Exitosos desc, Intentos desc
```

```kql
// H-12 · Pulverización con cadencia agéntica y dominio de bloqueos
SigninLogs
| where TimeGenerated > ago(7d)
| where ResultType in ("50126", "50053", "50055", "50056")
| summarize Fallos = count(), Cuentas = dcount(UserPrincipalName),
            Bloqueos = countif(ResultType == "50053"),
            AgentesUsuario = dcount(UserAgent)
        by IPAddress, bin(TimeGenerated, 20m)
| extend RatioBloqueo = todouble(Bloqueos) / todouble(Fallos)
| where Cuentas >= 20 and Fallos >= 200 and RatioBloqueo > 0.5
| order by Fallos desc
```

```kql
// H-9 + H-10 · Agentes de usuario del framework y lectura de artefactos de compilación
// Requiere que el WAF o el servidor web registren el agente de usuario.
let ArtefactosLectura = dynamic(["js.map", "/assets/config.json", "/env.js", "/swagger/?format=openapi"]);
WebRequestLogs
| where TimeGenerated > ago(14d)
| where UserAgent has_any ("artex-enrich/1.0", "norma/0.4", "artex-selfupdate", "ReconProbe/1.0")
      or UrlPath has_any (ArtefactosLectura)
| summarize Peticiones = count(), Rutas = dcount(UrlPath),
            Agentes = make_set(UserAgent, 10), Muestra = make_set(UrlPath, 15)
        by ClientIP, bin(TimeGenerated, 1h)
| order by Peticiones desc
```

```yaml
# Sigma — Marcadores autoidentificativos de ARTEX en línea de comandos y ficheros
# Autor: Célula CTI · Fecha: 2026-11-16 · ATT&CK: T1588.007, T1078.004
# Nivel: high · Estado: experimental (sin validar contra telemetría propia)
# Falsos positivos conocidos: equipos propios de red team que ejecuten el framework
# de forma autorizada; herramientas cuyo nombre contenga la subcadena "artex".
title: Marcadores del framework agentico ARTEX
id: 7f3c1e52-ARTEX-CTI-2026-019
status: experimental
logsource:
  category: process_creation
detection:
  cmdline_markers:
    CommandLine|contains:
      - 'artx5v'
      - 'artex-probe-'
      - 'ArtexProbe'
      - '\artx-'
  path_markers:
    Image|contains:
      - 'C:\ProgramData\artx5v\'
  condition: cmdline_markers or path_markers
fields:
  - CommandLine
  - Image
  - User
  - ParentImage
level: high
```

```yaml
# Sigma — Carga lateral de BLOODALCHEMY sobre binario legitimo renombrado
# Autor: Célula CTI · Fecha: 2026-11-16 · ATT&CK: T1574.001, T1036.005
# Nivel: critical · Estado: experimental
title: Carga lateral graphics-hook-filter64.dll por svchost renombrado
id: 9a21b7d4-ARTEX-CTI-2026-019
status: experimental
logsource:
  category: image_load
detection:
  dll:
    ImageLoaded|endswith: '\graphics-hook-filter64.dll'
  proceso_sospechoso:
    Image|endswith: '\svchost.exe'
  ruta_no_sistema:
    Image|startswith:
      - 'C:\Windows\System32\'
      - 'C:\Windows\SysWOW64\'
  condition: dll and proceso_sospechoso and not ruta_no_sistema
fields:
  - Image
  - ImageLoaded
  - Hashes
level: critical
```

<!-- cti:note type="info" -->

> **Sobre el material de detección publicado por terceros.** Un fork público del framework
> distribuye su propio paquete de detección: reglas Sigma atómicas y de correlación para los
> agentes de usuario, el egreso de autoactualización y el marcador de auditoría; firmas
> Suricata (`sid` 1000001–1000003); un fichero de indicadores en CSV y MISP; un script de
> triaje de host de solo lectura; y una capa de ATT&CK Navigator con ocho técnicas. Es
> material útil **como punto de partida y nada más**: proviene de la misma comunidad que
> mantiene la herramienta, no ha sido validado por nosotros, y su propio README advierte que
> la regla de comandos destructivos es genérica y no debe atribuirse a ARTEX. Revisarlo sí;
> ejecutar su script de triaje sin leerlo, no.

## X-5. Mitigaciones de configuración con efecto directo

| Control | Corta |
|---|---|
| Validación obligatoria de firma en todas las aserciones SAML | La forja de credenciales web (T1606.002), que es el acceso inicial de mayor impacto observado |
| IMDSv2 exigido en todas las instancias | El robo de credenciales por consulta al servicio de metadatos vía XXE (T1552.005) |
| Rotación de claves de firma de tokens y de preautenticación, incluidas las de respaldos y exportaciones de directorio históricas | La forja de token de administrador a partir de material de 2022 y 2024, documentada por CrowdStrike |
| Registro del plano de datos de almacenamiento habilitado | No corta nada por sí mismo: **habilita** D-2 y H-2, sin las cuales la etapa 02 es invisible |
| Interfaces de administración de nube, Kudu/SCM, hipervisores y plataformas de respaldo restringidas a redes de confianza | La ejecución de comandos arbitrarios vía API administrativas de publicación (T1059, T1651) |
| Autenticación básica de publicación deshabilitada; despliegue desde paquete (`run from package`) | La escritura de webshells y la modificación del contenido desplegado (T1505.003) |
| Mínimo privilegio en permisos y concesiones de aplicaciones multiinquilino | El pivote de 1 proveedor a 2.250 tenants (T1195, T1199) |
| Límite de tasa, límite de registros por sesión y autorización del lado del servidor por registro en portales de socios y empleados | La exfiltración por enumeración que afectó a 67.000 personas (T1190 + recolección) |
| Supresión de trazas de pila, errores SQL, rutas internas y detalles del framework en respuestas a usuarios no autenticados | El reconocimiento de la aplicación que precede a la explotación (T1595) |
| Retirada de mapas de origen y ficheros de configuración de los artefactos publicados; escaneo continuo de secretos en repositorios, imágenes y pipelines | Las credenciales de administrador embebidas en paquetes JavaScript (T1552.001) y la lectura de la aplicación de H-10 |
| Denegación por defecto de egreso en segmentos de servidor, con lista de permitidos | La salida a API de modelos (D-5) y a servicios de recolección fuera de banda (D-11) |
| Cobertura de EDR en **todos** los servidores, incluidos los considerados no alcanzables desde Internet | El movimiento lateral hacia los hosts sin sensor, que es la consecuencia directa de T1518.001 |
| Controles de engaño: señuelos, cuentas trampa y tarpits en la superficie expuesta | El bucle del planificador, que optimiza por progreso aparente y es manipulable con progreso falso |
| Políticas de acceso condicional sobre riesgo de inicio de sesión y de usuario | La pulverización y el uso de credenciales desde infraestructura no habitual (T1078, T1110.003) |

---

## 14. Brechas de inteligencia y nuevos requisitos de colección

| # | Brecha | Impacto en el juicio | Requisito propuesto | Prioridad |
|---|---|---|---|---|
| G-1 | Sin telemetría propia de ningún tipo incorporada a este informe | §O-4 vacía; KJ-2 queda en confianza moderada por inferencia; las detecciones de §X-3 son plantillas sin calibrar | Ejecutar el cuestionario X-1 a X-10 de §O-4 con los responsables asignados y emitir la versión 1.1 con los resultados | Crítica |
| G-2 | Sin visibilidad sobre si Chile o entidades chilenas figuran en las campañas observadas | KJ-4 se sostiene solo a nivel regional; no podemos afirmar ni descartar exposición nacional | Consulta formal al CSIRT Nacional/ANCI sobre actividad compatible con frameworks agénticos; participación en el canal sectorial de intercambio | Crítica |
| G-3 | Registro del plano de datos de almacenamiento y de la actividad de Microsoft Graph no confirmado en nuestro entorno | D-2, D-6, H-2 y H-5 no son implementables; la etapa 02 de la cadena es invisible | Verificar y habilitar el registro, con retención mínima de 90 días, e ingerirlo en el SIEM | Crítica |
| G-4 | Registros de aplicación sin identificador de sesión ni recuento de registros devueltos | H-13, la hipótesis con mayor probabilidad de aplicarnos, no es implementable | Requisito de registro para portales de socios y empleados: sesión, endpoint, registros devueltos por respuesta | Alta |
| G-5 | Sin inventario de aplicaciones multiinquilino de terceros con consentimiento en nuestro tenant | La decisión E-d no se puede ejecutar; el vector de KJ-7 queda sin evaluar | Extracción por identificador de aplicación desde Entra, con Object ID local del principal de servicio por tenant | Alta |
| G-6 | Sin inventario de credenciales de larga vida ni de su antigüedad, incluidas las presentes en respaldos | La decisión E-c no se puede priorizar; el vector de token forjado queda abierto | Inventario de secretos con fecha de emisión y última rotación; búsqueda en respaldos y exportaciones de directorio | Alta |
| G-7 | Texto del FLASH obtenido por extracción automática del PDF, con pérdida de los verbos en las celdas de la tabla de TTP | Los procedimientos de §T-2 están reconstruidos a partir de las fuentes citadas por el FLASH, no transcritos de él | Obtener el PDF con extracción de texto fiable y verificar la tabla de TTP celda por celda | Media |
| G-8 | Discrepancias sin resolver en los datos de origen: `178.16.54[.]129` frente a `178.15.54.129`; cuatro identificadores de aplicación mencionados y tres publicados | Dos indicadores del Anexo A pueden estar mal transcritos en su origen; una aplicación afectada puede quedar sin revisar | Consulta al proveedor o verificación contra una segunda fuente antes de usar esos indicadores en bloqueo | Media |
| G-9 | Sin visibilidad sobre el uso de frameworks agénticos por nuestros propios proveedores y equipos de pruebas | H-14 puede producir hallazgos sin dueño identificable; riesgo de incidente autoinfligido | Cláusula de declaración en contratos de pruebas de penetración; registro interno de instancias autorizadas | Media |
| G-10 | Sin seguimiento sistemático de los frameworks sucesores (AntiFox, HexStrike, PentAGI, CAIRN, AgentZero) | KJ-6 no es accionable: sabemos que vendrán pero no vigilamos cuáles | Añadir los cinco nombres y la categoría «framework ofensivo agéntico» al plan de colección permanente | Media |

---

# ANEXOS

## Anexo A — Indicadores de compromiso

<!-- cti:note type="warn" -->

> ⚠ **Leer antes de usar.** Los IOC son el nivel más perecedero y menos valioso de este
> producto, y en este caso particularmente: **ARTEX no deja binario propio en la víctima**,
> de modo que casi nada de esta lista detecta el uso del framework. Lo que detecta el uso
> del framework está en §T-4 y §X-3. El propio FBI advierte en el FLASH que esta
> infraestructura está alojada en plataformas de nube y virtualización donde las direcciones
> se reasignan dinámicamente, y que **debe interpretarse como infraestructura observada
> históricamente dentro de la ventana de actividad**, corroborándola con telemetría propia
> antes de usarla con fines defensivos. Se entrega con contexto, confianza y acción
> permitida; nunca como lista para cargar en un bloqueo automático.

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Acción permitida |
|---|---|---|---|---|
| ipv4 | `38.244.50[.]120` | Host ARTEX con directorio abierto — campaña financiera surcoreana | Alta | Bloqueo |
| ipv4 | `144.172.64[.]99` | Origen de la pulverización entre tenants del 10 al 14-oct-2026 y, desde el 15-oct, del uso de credenciales de aplicación de ConnectWise. Coincide exactamente con la IP del aviso del proveedor | Alta | Bloqueo |
| ipv4 | `144.172.64[.]60` | Inicios de sesión y actividad de Microsoft Graph en entornos de cliente — campaña ConnectWise | Alta | Bloqueo |
| ipv4 | `144.172.64[.]128` | Inicios de sesión y actividad de Microsoft Graph en entornos de cliente — campaña ConnectWise | Alta | Bloqueo |
| ipv4 | `187.15.88[.]186` | Acceso a Microsoft Graph vía aplicaciones comprometidas — **IP de VPN transitoria, relevante solo para el 15 y 16-oct-2026** | Moderada | Solo retrohunt |
| ipv4 | `187.15.90[.]217` | Acceso a Microsoft Graph vía aplicaciones comprometidas — IP de VPN transitoria, 15–16-oct-2026 | Moderada | Solo retrohunt |
| ipv4 | `187.15.89[.]186` | Acceso a Microsoft Graph vía aplicaciones comprometidas — IP de VPN transitoria, 15–16-oct-2026 | Moderada | Solo retrohunt |
| ipv4 | `101.53.80[.]20` | Proxy — campaña financiera surcoreana | Moderada | Solo retrohunt |
| ipv4 | `205.214.59[.]31` | Proxy — campaña financiera surcoreana | Moderada | Solo retrohunt |
| ipv4 | `124.155.252[.]63` | Proxy — campaña financiera surcoreana | Moderada | Solo retrohunt |
| ipv4 | `154.201.79[.]246` | Proxy — campaña financiera surcoreana | Moderada | Solo retrohunt |
| ipv4 | `23.248.249[.]90` | Proxy — campaña financiera surcoreana | Moderada | Solo retrohunt |
| ipv4 | `23.158.220[.]98` | Proxy — campaña financiera surcoreana | Moderada | Solo retrohunt |
| ipv4 | `103.248.148[.]84` | Proxy — campaña financiera surcoreana | Moderada | Solo retrohunt |
| ipv4 | `203.160.133[.]172` | Proxy — campaña financiera surcoreana | Moderada | Solo retrohunt |
| ipv4 | `209.209.85[.]38` | Proxy — campaña financiera surcoreana | Moderada | Solo retrohunt |
| ipv4 | `199.19.95[.]66` | Nodo C2 del RAT WISP — campaña Storm-3358, activo al 6-nov-2026 | Alta | Bloqueo |
| ipv4 | `199.19.95[.]67` | Nodo C2 del RAT WISP — campaña Storm-3358, activo al 6-nov-2026 | Alta | Bloqueo |
| ipv4 | `199.19.95[.]68` | Nodo C2 del RAT WISP — campaña Storm-3358, activo al 6-nov-2026 | Alta | Bloqueo |
| ipv4 | `91.92.240[.]238` | Servidor ARTEX — campaña Storm-3358, visto por primera vez el 4-nov-2026 | Alta | Bloqueo |
| ipv4 | `85.11.168[.]45` | Servidor ARTEX — campaña Storm-3358, visto por primera vez el 4-nov-2026 | Alta | Bloqueo |
| ipv4 | `31.77.229[.]35` | Servidor ARTEX — campaña Storm-3358, visto por primera vez el 28-oct-2026 | Alta | Bloqueo |
| ipv4 | `178.16.54[.]129` | Servidor ARTEX — campaña Storm-3358, visto por primera vez el 19-oct-2026. **Discrepancia en origen:** la consulta de Sentinel del proveedor indica `178.15.54.129`. Verificar antes de bloquear | Baja | Solo retrohunt |
| ipv4 | `85.11.167[.]52` | Servidor C2 — campaña Storm-3358, activo al 6-nov-2026 | Alta | Bloqueo |
| ipv4 | `104.194.150[.]21` | Infraestructura de pulverización y abuso de identidad contra proveedores de TI y software | Moderada | Bloqueo tras verificación |
| ipv4 | `167.88.172[.]97` | Infraestructura de pulverización y abuso de identidad contra proveedores de TI y software | Moderada | Bloqueo tras verificación |
| ipv4 | `45.153.126[.]223` | Resuelve `nginxmysql[.]com` — infraestructura C2 de BLOODALCHEMY (VAPOR PANDA) | Alta | Bloqueo |
| ipv4 | `89.46.234[.]50` | Resuelve `sqlserver-sqlite[.]com` — infraestructura C2 de BLOODALCHEMY (VAPOR PANDA) | Alta | Bloqueo |
| ipv4 | `192.121.47[.]20` | Resuelve `www[.]ddduuuppp[.]com` — infraestructura C2 de BLOODALCHEMY (VAPOR PANDA) | Alta | Bloqueo |
| domain | `xcai[.]pro` | Revendedor de API de modelos de lenguaje — campaña financiera surcoreana. Útil también como indicador de intención en egreso | Alta | Bloqueo |
| domain | `nginxmysql[.]com` | Dominio C2 de BLOODALCHEMY | Alta | Bloqueo |
| domain | `sqlserver-sqlite[.]com` | Dominio C2 de BLOODALCHEMY | Alta | Bloqueo |
| domain | `www[.]ddduuuppp[.]com` | Dominio C2 de BLOODALCHEMY | Alta | Bloqueo |
| servicio | `webhook.site` | Destino de devolución de resultados de comando — 491 URL rotatorias en una sola operación. **Servicio legítimo de terceros** | Alta | Bloqueo desde segmentos de servidor únicamente |
| herramienta | `49fe70419fd19b81ca8d730a6ef7c1ec71b681d60b390761070d42686c7d2068` | Binario legítimo GameHook renombrado a `svchost.exe` — portador de BLOODALCHEMY | Alta | Bloqueo |
| sha256 | `3fb5a9fb3e2cb1d6208966bd4e55d10282d19c7250d827efa560463d60a12ee4` | `graphics-hook-filter64.dll` — cargador de BLOODALCHEMY | Alta | Bloqueo |
| sha256 | `364251838edfcf5ef1107fa692da3c5bd9a540482449f645992830134bf807ab` | `graphics-hook_config.bin` — carga cifrada de BLOODALCHEMY | Alta | Bloqueo |
| appid | `506e08f9-6e9a-4da4-942b-a099a03644ae` | Aplicación multiinquilino ConnectWise Cloud Backup — **buscar por este identificador, no por nombre visible** | Alta | Revisión obligatoria en el tenant |
| appid | `24205314-2b89-4e07-a2a4-579e898a5640` | Aplicación multiinquilino ConnectWise - MS Teams | Alta | Revisión obligatoria en el tenant |
| appid | `0de14c77-b9b0-4137-9360-34878a929827` | Aplicación multiinquilino ConnectWise - MS Graph | Alta | Revisión obligatoria en el tenant |
| appid | *(cuarto identificador no publicado)* | El proveedor menciona cuatro credenciales de aplicación afectadas y publica tres. Brecha `G-8` | Baja | Consulta al proveedor |
| filename | `graphics-hook-filter64.dll` | Cargador de BLOODALCHEMY por carga lateral de DLL | Alta | Bloqueo |
| filename | `graphics-hook_config.bin` | Carga cifrada de BLOODALCHEMY | Alta | Bloqueo |
| filename | `cl1217.jsp` · `f1219a.jsp` · `z1219.jsp` | Webshells escritas vía envenenamiento de `general_log` de MySQL | Moderada | Detección; nombres triviales de cambiar |
| filepath | `C:\ProgramData\artx5v\` | Directorio de trabajo del framework en host comprometido | Alta | Detección y caza |
| filepath | `D:\ProjectX\Merman_New\` | Ruta de proyecto interna del desarrollador de BLOODALCHEMY, embebida en el binario | Alta | Caza por cadena en binarios |
| useragent | `artex-enrich/1.0` | Sonda de enriquecimiento del framework — **el único agente de usuario atribuible con alta fidelidad** | Alta | Detección y bloqueo |
| useragent | `artex-selfupdate` | Llamada de autoactualización del framework; visible en el egreso del host operador, no en el tráfico al objetivo | Alta | Detección en egreso propio |
| useragent | `norma/0.4` | Herramienta de obtención web del SDK subyacente. **Compartido con otras herramientas basadas en el mismo SDK** | Moderada | Detección; no bloquear sin verificar |
| useragent | `ReconProbe/1.0` | Observado en reconocimiento del mismo clúster | Moderada | Detección |
| useragent | `curl/7.88.1` · `Python-urllib/3.12` · `python-requests/2.31.0` · `python-requests/2.34.2` · `aws-cli/1.46.1` | Agentes por defecto de las herramientas invocadas por los agentes. **Genéricos: el proveedor advierte explícitamente que no son exclusivos de este actor** | Baja | Solo retrohunt y correlación |
| artefacto | `ArtexProbe` en nombres de cuenta · `artex-probe-*` en nombres de fichero · roles de nube con prefijo `artx-` · comentarios administrativos `art18-` | Marcadores autoidentificativos creados por el framework por descuido | Alta | Detección y caza |
| artefacto | `【ARTEX 平台管控·非目标防御】` | Marcador escrito en el registro de auditoría del framework en cada llamada de herramienta bloqueada por su capa de guarda. Solo aparece en el **host del operador** | Alta | Caza en instalaciones propias |
| puerto | `8787` (consola y API) · `8788` (proxy de grabación MITM) | Puertos por defecto del framework. Configurables con `-addr` y `-proxy` | Moderada | Caza interna y descubrimiento externo |
| herramienta | WISP · vshell · AdaptixC2 | RAT de código abierto desplegados para persistencia y movimiento lateral, descargados con `curl` y `netcat` | Alta | Detección por firma de EDR |
| herramienta | Chisel · SoftEther | Túneles usados para C2 y pivote | Alta | Detección por firma y por política |
| herramienta | `CLIProxyAPI` · `New API` | Pasarelas y revendedores de API de modelos autoalojados; el FBI los solicita explícitamente como indicador en sus peticiones de información | Alta | Detección en egreso |

*Nota de higiene.* Están marcados como infraestructura compartida o servicio legítimo, y por tanto **no deben bloquearse sin evaluar el impacto operativo**: `webhook.site` (servicio legítimo de captura de peticiones, bloquear solo desde segmentos de servidor), los agentes de usuario genéricos de `curl`, Python y AWS CLI (presentes en cualquier automatización propia), `norma/0.4` (compartido con otras herramientas del mismo SDK) y las IP de VPN transitorias `187.15.x` (reasignables, relevantes solo para dos días concretos). Los endpoints de API de modelos (`api.anthropic.com`, `api.deepseek.com`, `open.bigmodel.cn`, `api.x.ai`) **no son indicadores de compromiso**: son destinos legítimos cuyo valor está en el contexto —qué host habla con ellos— y bloquearlos de forma indiscriminada romperá usos de negocio aprobados.

## Anexo B — Fuentes y valoración

> Valoración doble tipo Admiralty/OTAN: **fiabilidad de la fuente (A–F)** ×
> **credibilidad de la información (1–6)**. Se valoran por separado.

| Fuente | Disciplina | Fiabilidad | Credibilidad | Notas de sesgo |
|---|---|---|---|---|
| FBI, FLASH-20261113-001, «Threat Overview of ARTEX Autonomous Penetration Testing Framework», 13-nov-2026 (TLP:CLEAR) | OSINT gubernamental | A | 1 | **Fuente primaria de este informe.** Sin producto que vender. Sintetiza once fuentes de proveedor, que cita; parte de su contenido es por tanto de segunda mano. Contiene un error tipográfico en un identificador ATT&CK. Texto obtenido por extracción automática del PDF (brecha `G-7`) |
| Microsoft Security Research y Microsoft Threat Intelligence, «AI-driven, large-scale nation-state campaign using ARTEX enables supply chain compromise», 21-oct-2026 | OSINT comercial / TECHINT | B | 1 | Telemetría de primera mano, con cifras verificables y consultas de caza publicadas. Interés propio en enmarcar el incidente como ajeno a sus productos, y lo declara explícitamente. No confirma acceso a datos de cliente |
| Microsoft Threat Intelligence, «ARTEX abuse expands as cybercriminals target financial sector», 6-nov-2026 | OSINT comercial / TECHINT | B | 2 | Telemetría de primera mano. Varias capacidades se enuncian como genéricas de ARTEX y no se atribuyen explícitamente a Storm-3358; el informe lo distingue y nosotros lo hemos respetado. Discrepancia de una IP entre tabla y consulta |
| CrowdStrike, «VAPOR PANDA uses ARTEX to scale global campaign», 29-oct-2026 | OSINT comercial / TECHINT | B | 1 | **Única fuente del dato regional latinoamericano.** Telemetría de primera mano con detalle excepcional (instrucciones del operador recuperadas). Interés comercial evidente en los pasajes sobre evasión de su propio sensor. Recuentos de compromiso no conciliables con la cobertura de prensa derivada |
| Google Threat Intelligence Group / Mandiant, «ARTEX and Friends: Enter Agentic Offensive Frameworks», 30-oct-2026 | OSINT comercial / TECHINT | B | 1 | La mejor descripción técnica disponible de la arquitectura y de la huella forense. Declara explícitamente sus límites de visibilidad y la incertidumbre sobre artefactos concretos. Juicio moderado y falsable («aún en etapas tempranas», «skids poco sofisticados») |
| Wiz, «ARTEX in the Wild: STORM-0940 expands targeting of IT and software vendors», 22-oct-2026 | OSINT comercial / TECHINT | B | 2 | Detalle operativo valioso sobre rutas y cadencia. Su propia tabla de indicadores advierte que muchos agentes de usuario no son exclusivos del actor. Afirma solapamiento con Storm-0940 donde otro proveedor afirma separación |
| Zscaler ThreatLabz, «Threat Actor Abuses Agentic AI Pentesting Framework to Target South Korean Financial Institutions», 14-oct-2026 | OSINT comercial | B | 2 | Única fuente de la verificación del código de la lista de bloqueo del framework. Atribución declarada con confianza moderada. Sección final de producto propio, descartada. Sin IOC de red |
| Censys, «ARTEX: Agentic Asbestos», 5-nov-2026 | OSINT comercial / medición de infraestructura | B | 2 | Medición directa reproducible. Advierte explícitamente que parte de las consolas expuestas pertenecen a evaluadores autorizados. Su metodología de huella no se publica en detalle |
| CERT-EU, «From Penetration Testing to Cyber Threat: Beware of ARTEX», 5-nov-2026 | OSINT gubernamental | A | 2 | Sin interés comercial. Su juicio sobre instituciones de la UE se formula como «altamente probable», no como confirmado, y así se ha transcrito |
| Check Point Research, «Hacking on Autopilot: Inside ARTEX Cybercrime Campaigns», 5-nov-2026 | OSINT comercial | B | 3 | Conocido solo a través de la cita del FLASH y de cobertura derivada; no se accedió al original. Su recuento de sistemas es el más alto de los seis medidores y no es conciliable con los demás |
| Akamai, «What ARTEX Reveals About Overlooked Attack Surfaces», 23-oct-2026 | OSINT comercial | B | 3 | Conocido solo a través de la cita del FLASH; no se accedió al original. Base de la tesis de superficie periférica de KJ-2, lo que hace deseable verificarlo directamente |
| SafeBreach, cobertura del FLASH, 14-nov-2026 | OSINT comercial | C | 3 | Útil como índice del FLASH y por la identificación de las familias de webshell. Describe el FLASH en lugar de citarlo; su contenido de simulación es producto propio. **Superado por el acceso directo al FLASH** |
| Repositorio público de un fork del framework, su documentación de defensa y su paquete de detección (verificado por nosotros, 16-nov-2026) | OSINT técnico / análisis propio | C | 2 | **Material de la propia comunidad que mantiene la herramienta.** Fiabilidad baja por conflicto de interés estructural; credibilidad alta en los datos verificables (puertos, variables, esquema de base de datos, agentes de usuario) porque son comprobables contra el código. No ejecutado ni instalado |
| Guías comerciales de cumplimiento sobre Ley 21.663 y Decreto 295 | OSINT comercial | C | 3 | **Fuente de los plazos de notificación citados en §E-4 y §2.** No es el texto oficial. Coinciden entre sí en el esquema 3 h / 72 h / 15 días pero discrepan en los plazos especiales para operadores de importancia vital. Debe verificarse contra el Decreto 295 antes de sostener una decisión de cumplimiento |
| Comprobación propia de ausencia de alerta de la ANCI/CSIRT Nacional sobre ARTEX, 16-nov-2026 | Análisis propio / OSINT | B | 3 | **Hallazgo negativo:** la ausencia de alerta en fuentes abiertas no prueba la ausencia de alerta ni de actividad. Consignado como brecha `G-2`, no como conclusión |

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

## Anexo D — Otros frameworks ofensivos agénticos a vigilar

> Este anexo existe por KJ-6: la detección debe construirse contra la conducta, no contra
> ARTEX. Estos son los nombres que ya aparecen en respuesta a incidentes o en
> experimentación documentada, y que deben incorporarse al plan de colección (`G-10`).

| Framework | Origen y estado | Qué se le atribuye |
|---|---|---|
| `HexStrike` (HexStrike AI) | Código abierto; conecta modelos a más de 150 herramientas de seguridad | Observado por GTIG en compromisos de respuesta a incidentes |
| `CAIRN` | Código abierto, framework agéntico de pentesting | Observado por GTIG en compromisos de respuesta a incidentes; sin detalle público |
| `PentAGI` | Desarrollado por VXControl; edición libre y edición comercial; ejecuta herramientas en entornos aislados con Kali Linux; soporta más de una docena de backends de modelos locales y en nube | Plataforma de orquestación personalizada construida sobre su versión libre, usada entre finales de agosto y principios de octubre de 2026 contra organizaciones asiáticas; encadenada con servicios de proxy contra el sector aeroespacial |
| `AgentZero` | Framework completamente agéntico de propósito general, código abierto | Evidencia de experimentación por actores de amenaza, junto al servicio de inferencia `ZeroHollow` |
| `AntiFox` | Plataforma de pentesting con IA, aparecida en noviembre de 2026 | Vinculada públicamente a ataques que accedieron a secretos de producción en AWS |
| `ScopeWeaver` | Variante localizada y renombrada de ARTEX | Equivalente funcional presumido del original |
| `ARTEX PRO` | Versión comercial de ARTEX ofrecida por terceros | Capacidades no verificadas públicamente |
| `HONESTCUE` · `PROMPTSPY` | No son frameworks: familias de malware con modelos de lenguaje embebidos | Categoría adyacente, mencionada por GTIG; vigilar como tendencia distinta |

## Anexo E — Marcos de referencia empleados

`MITRE ATT&CK v18` · `MITRE D3FEND` · `Cyber Kill Chain` · `Pirámide del Dolor` ·
`Modelo del Diamante` · `F3EAD` · `ICD 203` (lenguaje estimativo) · `ACH, supuestos
clave, pre-mortem` · `TLP 2.0` · `PAP` · `STIX 2.1 / TAXII 2.1` · `Admiralty Code` ·
`Ley 21.663 y Decreto 295` (marco de notificación aplicable en Chile)

## Anexo F — Paquete legible por máquina

- Bundle STIX 2.1: pendiente de generar. Debe incluir los objetos `tool` (ARTEX y derivados), `intrusion-set` (los cinco clústeres, **sin fusionar**), `attack-pattern` (las 47 técnicas de §T-2), `indicator` (Anexo A, con `valid_until` y marcado de infraestructura compartida) y las relaciones `uses` entre clústeres y herramienta.
- Evento MISP: pendiente. Taxonomías a aplicar: `tlp`, `pap`, `admiralty-scale`, `estimative-language`, `veris`, y etiqueta propia `framework-agentico-ofensivo`.
- Reglas: las dos reglas Sigma de §X-4 y las doce plantillas de detección de §X-3 deben versionarse en el repositorio de detección con el identificador `CTI-2026-019` y estado `experimental` hasta su calibración.
- Capa de ATT&CK Navigator: pendiente de generar a partir de §T-2.

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-11-16 | Emisión inicial. Elaborado sobre el texto completo del FLASH FBI-20261113-001 y nueve informes de proveedor de primera mano. Sin telemetría propia: §O-4 sin evaluar | Célula CTI |

## Anexo H — Realimentación del consumidor

| Pregunta | Respuesta |
|---|---|
| ¿Respondió a su requisito? | |
| ¿Qué decisión tomó o cambió con este informe? | |
| De las ocho decisiones de §E-4, ¿cuáles se aprobaron y con qué plazo real? | |
| ¿Se designó responsable nominal para el impacto operativo de las detecciones críticas de §X-3? | |
| ¿Qué faltó? | |
| ¿Llegó a tiempo? | |

> Sin este anexo devuelto, el ciclo de inteligencia queda abierto y el próximo
> producto no mejora. En este caso concreto hay además una dependencia dura: **la
> versión 1.1 de este informe no se puede escribir sin las respuestas al cuestionario
> de §O-4.**
