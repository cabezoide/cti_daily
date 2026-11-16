---
tlp: "TLP:CLEAR"
pap: "PAP:AMBER"
id: "CTI-2026-020"
version: "1.0"
tipo: "Perfil de actor + informe de campaña"
foco_regional: "Latinoamérica · Chile"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "Blind Eagle (APT-C-36 · TAG-144 · AguilaCiega · APT-Q-98)"
fecha: "2026-11-16"
caduca: "2027-02-16"
autor: "Célula CTI"
distribucion: "Elaborado íntegramente con fuentes abiertas TLP:CLEAR. No incorpora el contenido de la alerta TLP:AMBER del ColCERT citada en §O-5 y el Anexo B, cuyo marcado se respeta: se consigna su existencia, no su contenido. Difusión libre, conservando la atribución de las fuentes y las salvedades metodológicas de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-020
## Blind Eagle: ocho años atacando Latinoamérica con malware de catálogo, scripts de Visual Basic y DNS dinámico gratuito — y funcionando, porque su ventaja no es técnica sino burocrática
### Suplanta el acto administrativo que ningún funcionario público latinoamericano puede ignorar: la citación judicial. Chile figura como objetivo en cuatro fuentes independientes y en ningún caso documentado

> **Regla de oro del producto:** todo párrafo debe responder a un requisito de
> inteligencia (PIR) y habilitar una decisión. Si un párrafo no cambia lo que
> alguien va a hacer, va al anexo o se borra.

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-020` |
| Versión / fecha | `1.0` — 2026-11-16 |
| Tipo de producto | Perfil de actor + informe de campaña |
| Niveles cubiertos | Estratégico · Operacional · Táctico · Técnico |
| Foco regional | Latinoamérica, con lectura específica para Chile |
| Marcado de difusión | `TLP:CLEAR` · `PAP:AMBER` |
| Clasificación interna | Público — apto para difusión abierta |
| Requisitos atendidos | `PIR-01` (actores con intención y capacidad contra nuestro sector), `PIR-02` (superficie de phishing y suplantación institucional), `PIR-04` (amenazas con foco regional hispanohablante), `PIR-08` (abuso de servicios legítimos como infraestructura) |
| Solicitante / consumidor primario | CISO · Jefatura de SOC · Ingeniería de Detección · Seguridad del Correo · Asuntos Corporativos |
| Ventana de observación | 2018 (primera actividad atribuida) → 2026-11-16, con detalle técnico desde 2024-08 |
| Base de colección | 10 fuentes. De primera mano: MITRE ATT&CK G0099 v2.0 (31-jul-2026), Check Point Research (10-mar-2025), Kaspersky GReAT (19-ago-2024), LevelBlue/Trustwave SpiderLabs (27-jun-2025 y 17-jul-2026), Zscaler ThreatLabz (16-dic-2025), Darktrace (25-jun-2025). De segunda mano: Recorded Future Insikt (26-ago-2025, no accesible en original), prensa técnica sobre la campaña de oct-nov 2026. **Citada pero no incorporada:** alerta ColCERT `AL-20260925-119`, marcada TLP:AMBER. **Sin telemetría propia incorporada** |
| Autor (analista) | Célula CTI |
| Revisión por pares | Pendiente |
| Aprobación | Pendiente |
| Caducidad / revisión | 2027-02-16, o antes si se documenta una víctima chilena nombrada, si aparece señuelo localizado a instituciones chilenas, o si un proveedor publica el análisis técnico de la campaña de oct-nov 2026 |
| Productos relacionados | `CTI-2026-014` (TheGentlemen), `CTI-2026-015` (Qilin), `CTI-2026-016` (LockBit 5.0), `CTI-2026-017` (FamousSparrow), `CTI-2026-018` (abuso de TLD), `CTI-2026-019` (ARTEX). **Contrapunto deliberado de `CTI-2026-019`:** donde ARTEX representa la amenaza por velocidad, este actor representa la amenaza por fluidez cultural. Ninguno de los dos se detiene con el control que detiene al otro |
| Paquete legible por máquina | Pendiente de generar (véase §14) |

<!-- cti:note type="warn" -->

> **Limitación estructural de este producto.** Se ha elaborado con seis informes de
> proveedor de primera mano y la ficha de MITRE, pero **sin telemetría de la
> organización**. En consecuencia **§O-4 (nuestra exposición) está sin rellenar**: no
> sabemos si alguno de nuestros buzones institucionales ha sido usado como remitente,
> si nuestros controles de correo tratan el correo intra-tenant con el mismo rigor que
> el externo, ni si nuestra flota permite la cadena `wscript → PowerShell → utilidad
> .NET` que este actor lleva ocho años usando sin cambios.

<!-- cti:note type="gap" -->

> ⬛ **Decisión de manejo de fuente que conviene conocer antes de leer.** El 25 de
> septiembre de 2026 el ColCERT de Colombia emitió la alerta `AL-20260925-119` sobre una
> campaña de este actor contra entidades públicas colombianas, atribuida por ese equipo
> con alto nivel de confianza. **Ese documento está marcado TLP:AMBER en sus once
> páginas**, y este informe es TLP:CLEAR de difusión pública. En consecuencia se consigna
> su **existencia y su referencia bibliográfica** —que son públicas— pero **no se
> reproduce ninguno de sus contenidos**: ni sus indicadores, ni el nombre del implante que
> analiza, ni su infraestructura, ni su alcance geográfico declarado. Quien necesite ese
> material debe obtenerlo del ColCERT por el canal correspondiente. La consecuencia
> analítica está consignada como brecha `G-1` en §14: **el análisis técnico más reciente y
> más específico que existe sobre este actor no está incorporado a este producto.**

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** La ventaja competitiva de Blind Eagle no es técnica, es institucional: suplanta con precisión el acto administrativo que un funcionario o un empleado latinoamericano no puede permitirse ignorar. Citación judicial, notificación de fiscalía, admisión de demanda laboral, requerimiento tributario. Ocho años de operación con malware de catálogo y scripts de Visual Basic lo confirman: **la eficacia no viene del implante, viene del pretexto.** Valoramos **muy probable** *(80–95 %)*. **Confianza: alta.** *Base:* los seis informes de primera mano coinciden en el señuelo judicial como constante desde 2019; Check Point reproduce siete nombres de fichero `.url` con terminología procesal colombiana exacta.

**KJ-2.** El vector que derrota nuestros controles de correo no es el adjunto, es el **remitente**. En las dos campañas mejor documentadas de 2025 y 2026 el correo salió de una cuenta institucional legítima comprometida de la propia organización objetivo, dirigida a un buzón compartido del área de TI. Zscaler constata que remitente y destinatario tenían DMARC, DKIM y SPF correctamente configurados y sin fallos: el mensaje no cruzó el perímetro, nació dentro. Valoramos **muy probable** *(80–95 %)*. **Confianza: alta.** *Base:* Zscaler (dic-2025) y MITRE `T1534` y `T1586.002`, corroborado por Insikt vía fuente secundaria.

**KJ-3.** La cadena de ejecución es la misma desde 2019 y por eso es detectable: `script de Visual Basic → PowerShell oculto → vaciado de proceso sobre una utilidad .NET del propio Windows`. Los nombres rotan —`RegSvcs.exe`, `MSBuild.exe`, `InstallUtil.exe`, `jsc.exe`, `AppLaunch.exe`, `csc.exe`— pero el patrón no. **Es un conjunto cerrado de binarios que no tienen ninguna razón legítima para abrir conexiones de red en una flota administrada.** Valoramos **casi con certeza** *(95–99 %)*. **Confianza: alta.** *Base:* Kaspersky (2024), Check Point (2025), Zscaler (2025) y SpiderLabs (2026) describen la misma cadena con cuatro conjuntos de muestras distintos.

**KJ-4.** Chile está en el conjunto de objetivos declarados y en ningún caso público documentado. Kaspersky lo nombra como objetivo secundario junto a Ecuador y Panamá; MITRE lo cubre bajo «otros países latinoamericanos»; la prensa técnica sobre la campaña de oct-nov 2026 lo sitúa entre los tres países principales junto a Colombia y México. **Ninguna fuente publica una víctima chilena nombrada ni un señuelo localizado a instituciones chilenas.** Valoramos **posibilidad real** *(45–55 %)* de que exista actividad contra Chile no documentada públicamente. **Confianza: baja.** *Base:* cuatro fuentes que listan el país, ninguna que documente un caso; ausencia de alerta pública del CSIRT Nacional.

**KJ-5.** El actor se está integrando en el ecosistema criminal brasileño, no solo en el colombiano. Cuatro fuentes independientes a lo largo de dos años apuntan en la misma dirección: artefactos con cadenas en portugués (2024), alojamiento de imágenes brasileño (2024), panel de botnet con interfaz en portugués de Brasil (2025), el cargador Caminho con identificadores en portugués y origen hipotético en ese ecosistema (2025), y la atribución de la campaña de 2026 a un clúster brasileño. Valoramos **probable** *(55–80 %)*. **Confianza: moderada.** *Base:* convergencia de cuatro fuentes de primera mano más una secundaria; ninguna lo afirma de forma concluyente y Kaspersky lo plantea explícitamente como hipótesis de colaboración o subcontratación.

**KJ-6.** El grupo compra capacidad en lugar de desarrollarla, y eso acelera su evolución sin aumentar su pericia. Paga un servicio de criptado por suscripción anunciado en Telegram, un empaquetador como servicio (`HeartCrypt`), un cargador como servicio (`Caminho`), alojamiento a prueba de balas (Proton66) y usa DNS dinámico gratuito. **Su arsenal mejora al ritmo del mercado criminal, no al de sus propios programadores.** Valoramos **muy probable** *(80–95 %)*. **Confianza: alta.** *Base:* SpiderLabs identifica el solapamiento con `Vbs-Crypter`; MITRE registra `HeartCrypt` y `PureCrypter` bajo `T1588.001`; Zscaler documenta `Caminho`.

**KJ-7.** Los indicadores atómicos de este actor son inútiles y sus artefactos de nombre son excepcionalmente duraderos. SpiderLabs es explícito: los hashes «caducan en el momento en que una muestra se ejecuta una vez», porque el dropper se automuta y regenera su clave XOR y sus identificadores en cada ejecución. En cambio la tarea programada `Photo Studio`, la carpeta `PhotoStudioVBS`, el prefijo `zv`, el decodificador `Wales()`, el exportado `VAI` o los marcadores `BaseStart-`/`-BaseEnd` llevan meses sin cambiar. Valoramos **muy probable** *(80–95 %)*. **Confianza: alta.** *Base:* SpiderLabs (jul-2026) y Zscaler (dic-2025).

**Qué cambiaría estos juicios:** la aparición de un señuelo específicamente localizado a instituciones chilenas —Poder Judicial, Ministerio Público, Servicio de Impuestos Internos, Dirección del Trabajo— con terminología procesal chilena correcta elevaría KJ-4 de «posibilidad real» a «probable» y convertiría este informe en un producto de alerta y no de perfil. Es el indicador `I-1` de §O-7, y es el que hay que vigilar.

---

## 2. Resumen ejecutivo

Blind Eagle es un actor hispanohablante que ataca Latinoamérica desde 2018, con foco abrumador en Colombia y presencia declarada en Ecuador, Chile, Panamá y España. No es sofisticado y no lo necesita: usa troyanos de acceso remoto que cualquiera puede descargar gratis, scripts de Visual Basic, servicios de DNS dinámico sin coste y plataformas legítimas —GitHub, Bitbucket, Discord, Internet Archive— como almacén de sus cargas. MITRE lo registra como G0099 y lo describe como sospechoso de origen sudamericano, con operaciones de espionaje y de lucro simultáneas.

Su eficacia viene de otro sitio. Este actor entiende la burocracia latinoamericana mejor que nuestros filtros de correo. Suplanta la Fiscalía, la administración de impuestos, los juzgados laborales y los ministerios con una precisión terminológica que un modelo entrenado en inglés no detecta como anómala, y lo hace sobre el único asunto que un empleado no puede archivar sin leer: una citación judicial con número de proceso. En diciembre de 2025, Zscaler documentó el caso completo contra una agencia del Ministerio de Comercio colombiano: el correo salió de un buzón compartido de la propia entidad, con DMARC, DKIM y SPF en regla, porque nunca cruzó un perímetro.

Para nosotros el problema tiene tres caras. La primera es que el control que nos protegería no es técnico sino de proceso: cómo verifica un empleado una notificación judicial que llega por correo. La segunda es que la cadena de ejecución del actor —script de Visual Basic, PowerShell oculto, vaciado de proceso sobre una utilidad .NET de Windows— es idéntica desde 2019 y nuestra flota debería estar detectándola ya; si no lo hace, el problema no es este actor. La tercera es que Chile aparece listado como objetivo en cuatro fuentes y en ningún caso documentado, lo que no es una buena noticia sino una brecha de visibilidad.

<!-- cti:cards -->

| Rasgo | Qué significa | Etiqueta |
|---|---|---|
| Fluidez burocrática, no destreza técnica | El señuelo es culturalmente nativo y nuestros filtros, entrenados en otro idioma y otra administración, lo leen como correo legítimo | `01 · pretexto` |
| Entra desde dentro del tenant | Remitente institucional comprometido, correo intra-tenant, DMARC y SPF intactos. El perímetro no participa | `02 · remitente` |
| Cadena de ejecución inmutable desde 2019 | Si no la detectamos hoy, llevamos siete años sin detectarla. Es la deuda de detección más barata de pagar de este informe | `03 · cadena` |
| Compra capacidad en lugar de crearla | Evoluciona al ritmo del mercado criminal: criptador por suscripción, empaquetador y cargador como servicio, alojamiento a prueba de balas | `04 · mercado` |
| Indicadores inútiles, artefactos duraderos | Los hashes caducan al primer arranque por automutación; los nombres de tarea y carpeta llevan meses intactos. Invertir al revés es el error habitual | `05 · detección` |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `87` | Porcentaje de víctimas localizadas en Colombia | Campañas de espionaje de may-jun 2024 medidas por Kaspersky |
| `9000` | Infecciones aproximadas en una semana de campañas de dic-2024 | Más de 1.600 en una sola de ellas |
| `8075` | Registros válidos de datos personales que el actor filtró por error desde su propio repositorio | Incluían 1.634 direcciones de correo, cinco de ellas de dominios `.gov.co` |
| `6` | Días que tardó en adoptar la técnica del fichero `.url` tras el parche de Microsoft | Parche el 12-nov-2024, primera muestra el 18-nov-2024 |
| `3300` | Correos maliciosos contabilizados entre finales de octubre y principios de noviembre de 2026 | Cifra de fuente única, sin corroboración independiente |
| `38` | Técnicas de MITRE ATT&CK atribuidas al grupo en su ficha G0099 | Nueve familias de herramientas asociadas |

<!-- cti:note type="good" -->

> ✅ **Decisiones que se solicitan a Dirección.** (a) Someter la cadena `wscript/cscript → PowerShell → utilidad .NET` a prueba de detección y cerrar la brecha si existe — 30 días. (b) Equiparar el tratamiento de seguridad del correo intra-tenant al del correo externo, incluidos los buzones compartidos y funcionales — 45 días. (c) Establecer y comunicar un procedimiento de verificación de notificaciones judiciales y tributarias por canal independiente, con la lista de dominios oficiales chilenos legítimos — 60 días, con Asuntos Corporativos. (d) Bloquear por defecto el egreso a dominios de DNS dinámico gratuito desde estaciones de trabajo — 45 días.

---

## 3. Alcance, requisitos y limitaciones

**3.1 Requisitos de inteligencia atendidos**

| Req. | Enunciado | ¿Respondido? | Dónde |
|---|---|---|---|
| PIR-01 | ¿Qué actores tienen intención y capacidad contra nuestro sector y nuestra región? | Sí | §O-1, §O-2, §E-2 |
| PIR-02 | ¿Qué superficie de phishing y suplantación institucional nos afecta? | Sí | §E-1, §T-1, §T-4 |
| PIR-04 | ¿Qué amenazas operan específicamente en español contra Latinoamérica? | Sí | §E-1, §E-2, §O-3 |
| PIR-08 | ¿Qué servicios legítimos se están usando como infraestructura adversaria? | Sí | §X-2, §X-5, Anexo A |
| — | ¿Hemos sido objetivo de este actor? | **No** — requiere telemetría propia | §O-4, §14 |

**3.2 Fuera de alcance.** No se evalúa: la actividad del actor contra el sector bancario minorista colombiano y ecuatoriano, que está bien documentada y no nos aplica directamente; la atribución nominal de los operadores; y el ecosistema brasileño de crimeware por sí mismo, que merece producto propio si se confirma KJ-5.

**3.3 Limitaciones de la colección.** (i) **Sin telemetría propia.** (ii) **La fuente más reciente y específica no está incorporada por decisión de manejo**, no por falta de acceso: la alerta del ColCERT es TLP:AMBER y este producto es público (brecha `G-1`). (iii) **La campaña en curso de oct-nov 2026 descansa en fuentes secundarias.** El informe original de Trustwave y el recuento de 3.300 correos atribuido a Zenox se conocen a través de prensa técnica; no se accedió a ninguno de los dos originales, y la cifra no tiene corroboración independiente. Se consigna con valoración C/3 y así debe tratarse. (iv) **El informe de Recorded Future Insikt sobre los cinco clústeres no pudo leerse en original**: el PDF está publicado pero su codificación tipográfica impidió la extracción de texto, de modo que lo que se dice de él proviene de resúmenes de terceros. (v) **Sesgo de visibilidad hacia Colombia.** Los proveedores que investigan este actor tienen clientes y sensores en Colombia; la ausencia de casos chilenos documentados puede reflejar ausencia de sensores y no ausencia de actividad. Es la razón por la que KJ-4 se formula como «posibilidad real» y no como «poco probable». (vi) **Discrepancias sin resolver en los datos de origen**, consignadas donde aparecen: Check Point publica «1.600 afectados» y «1.600 infectados» para la misma campaña y da 8.000 y 8.400 registros filtrados en dos lugares distintos; Darktrace publica dos versiones del mismo agente de usuario WebDAV; Zscaler describe el estatus comercial de Caminho como «probablemente» de mercado clandestino en el cuerpo y como servicio en su tabla ATT&CK.

**3.4 Metodología.** Disciplinas: OSINT comercial de proveedor (seis informes de primera mano), OSINT de marco de referencia (MITRE ATT&CK G0099 v2.0), OSINT gubernamental (existencia de la alerta del ColCERT, sin su contenido). Técnicas analíticas estructuradas: análisis de hipótesis competidoras (§O-6), comprobación de supuestos clave, pre-mortem. Marcos: MITRE ATT&CK v18, Pirámide del Dolor, Cadena de Intrusión, ICD 203, código Admiralty.

---

# NIVEL ESTRATÉGICO
### Para: Consejo · CISO · Riesgo · Asuntos Corporativos · Horizonte: 6–24 meses

## E-1. Qué representa este actor en el panorama

Blind Eagle es el contraejemplo útil frente a la creencia de que el riesgo se ordena por sofisticación. Lleva ocho años operando con herramientas que un aficionado puede descargar gratis, y sigue comprometiendo ministerios.

Durante esos ocho años la industria ha invertido en detectar capacidad técnica: implantes nuevos, exploits de día cero, evasión de memoria. Este actor no aporta ninguna de las tres cosas. Aporta algo que ninguna de nuestras herramientas mide: **sabe cómo funciona el Estado en América Latina.** Sabe que una notificación de admisión de demanda laboral con número de proceso se abre siempre. Sabe que el buzón compartido del área de TI es el que recibe los avisos administrativos y el que menos sospecha. Sabe que un correo que no cruza el perímetro no es inspeccionado con el mismo rigor.

Hay un detalle que resume el carácter del grupo mejor que cualquier análisis de capacidad. En febrero de 2025, Check Point encontró que el propio actor había subido por error a su repositorio público de GitHub el fichero HTML con los datos personales cosechados de sus víctimas: 8.075 registros válidos, 1.634 direcciones de correo, entre ellas cinco de dominios gubernamentales colombianos. Estuvo publicado hora y media antes de que lo borraran. **Este es un adversario que compromete entidades públicas y que a la vez filtra su propio botín por descuido operacional.** Ambas cosas son ciertas al mismo tiempo, y la segunda no reduce la primera.

La consecuencia estratégica es incómoda: el control que nos defiende de este actor no está en el catálogo de seguridad. Está en el proceso administrativo por el que un empleado verifica una notificación judicial, en la política de buzones funcionales y en una línea base de ejecución de scripts que debería existir desde hace años.

<!-- cti:cards -->

| Cambio estructural | Por qué nos afecta | Etiqueta |
|---|---|---|
| El pretexto se localiza mejor que nuestras defensas | Filtros, modelos y formación entrenados en inglés y en otra administración leen el señuelo como correo rutinario | `01 · idioma` |
| El perímetro deja de participar | Remitente institucional comprometido y correo intra-tenant: DMARC, DKIM y SPF en regla y ningún control activado | `02 · confianza` |
| La capacidad se alquila | Criptador por suscripción, empaquetador y cargador como servicio, alojamiento a prueba de balas. Mejora sin aprender | `03 · mercado` |
| La infraestructura es legítima | GitHub, Bitbucket, Discord, Internet Archive, paste sites y DNS dinámico gratuito. No hay dominio malicioso que bloquear | `04 · abuso` |
| El objetivo regional se amplía despacio y en silencio | Chile listado por cuatro fuentes y documentado por ninguna. La ausencia de casos no es ausencia de actividad | `05 · alcance` |

## E-2. Victimología y distribución

<!-- cti:bars title="Distribución de víctimas por país (Kaspersky, campañas de espionaje may–jun 2024)" color="#e0a33e,#5a7ebe" -->

| País | Porcentaje de víctimas |
|---|---|
| Colombia | 87 |
| Resto de la región | 13 |

<!-- cti:note type="warn" -->

> ⚠ **Leer este reparto con cuidado.** El 87 % corresponde **solo** a las campañas de
> espionaje de mayo y junio de 2024 medidas por la telemetría de Kaspersky, no a toda la
> actividad histórica del grupo. El 13 % restante no está desglosado por país en ninguna
> fuente pública. Usar este dato como «Chile representa un porcentaje despreciable» sería
> una sobrelectura: lo que dice el dato es que **la visibilidad de los proveedores está
> concentrada donde están sus clientes.**

<!-- cti:bars title="Volúmenes documentados, por fuente y campaña" -->

| Medida | Valor |
|---|---|
| Infecciones en una semana de campañas (dic-2024, Check Point) | 9000 |
| Correos maliciosos en dos semanas (oct-nov 2026, fuente única) | 3300 |
| Registros de datos personales filtrados por el propio actor | 8075 |
| Infecciones en la campaña `PARAISO` (dic-2024) | 1600 |
| Direcciones de correo en el volcado filtrado | 1634 |
| Equipos infectados en un panel de control observado (2025) | 264 |

**Sectores.** Las fuentes convergen en cuatro: **administración pública** —ministerios, entidades judiciales, organismos de control—, **servicios financieros** —banca minorista colombiana y ecuatoriana, y el sector asegurador—, **energía y petróleo y gas**, y **educación y salud**. MITRE añade manufactura profesional. El patrón relevante no es el sector sino el perfil del destinatario: personas que reciben notificaciones oficiales como parte de su trabajo.

**Geografía.** Colombia es el foco indiscutido en todas las fuentes. Ecuador aparece en casi todas, con ataques específicos a portales bancarios. Panamá y España figuran en los perfiles históricos. Argentina aparece de forma inesperada: el panel de botnet que SpiderLabs observó en 2025 mostraba 264 equipos infectados «principalmente en Argentina», un dato que ninguna otra fuente recoge y que no encaja con el resto de la victimología.

<!-- cti:note type="warn" -->

> ⚠ **Lectura regional — qué se puede y qué no se puede afirmar sobre Chile.** Chile
> aparece nombrado como país objetivo en Kaspersky (objetivo secundario, junto a Ecuador y
> Panamá), en los perfiles históricos del actor, y en la cobertura de la campaña de
> octubre-noviembre de 2026, que lo sitúa entre los tres países principales junto a
> Colombia y México atribuyéndolo a investigación de Trustwave. **Lo que no existe es un
> solo caso con víctima chilena nombrada, un señuelo que suplante a una institución
> chilena, ni una alerta pública del CSIRT Nacional sobre este actor** (comprobación propia
> por fuentes abiertas, 16-nov-2026). La lectura honesta es que Chile está en la lista de
> objetivos del adversario y fuera de la lista de casos documentados, y que esas dos cosas
> juntas describen una brecha de colección nuestra —`G-2` en §14— y no una buena noticia.

## E-3. Tendencia y pronóstico

<!-- cti:chart title="Informes de primera mano publicados por semestre" cap="Mide la atención de la industria, no la actividad del actor, que es continua desde 2018. El vacío del primer semestre de 2026 no indica pausa: la campaña de ese periodo se documentó en julio." -->

| Periodo | Informes |
|---|---|
| 2024-S1 | 0 |
| 2024-S2 | 1 |
| 2025-S1 | 3 |
| 2025-S2 | 2 |
| 2026-S1 | 0 |
| 2026-S2 | 3 |

La trayectoria técnica del grupo a lo largo de dos años muestra un patrón claro: **no mejora inventando, mejora comprando.** En 2024 usaba troyanos de catálogo con empaquetado propio rudimentario. En noviembre de 2024 incorporó la técnica del fichero `.url` seis días después del parche de Microsoft que la hizo pública. En 2025 añadió un empaquetador como servicio, alojamiento a prueba de balas y un criptador por suscripción comprado en Telegram. En diciembre de 2025 adoptó un cargador como servicio de origen probablemente brasileño. En julio de 2026 su cadena ya incluía automutación del dropper, suplantación del proceso padre, inyección por notificación de estado del núcleo y evasión del cifrado vinculado a aplicación de Chrome. Cada incorporación viene del mercado, no del taller.

<!-- cti:cards -->

| Escenario | Desarrollo | Etiqueta |
|---|---|---|
| Continuidad con mejora comprada | Sigue el patrón de los últimos dos años: señuelo judicial constante, arsenal renovado con lo que ofrezca el mercado criminal. La detección conductual de §X-3 mantiene su validez porque la cadena de ejecución no cambia | `Probable · 55–80 %` |
| Localización a nuevos países hispanohablantes | Adapta la terminología procesal a Chile, Perú o México con la misma precisión que logró en Colombia. Es barato para el actor —solo requiere un hablante que conozca la administración local— y degradaría de golpe la formación de nuestros usuarios | `Posibilidad real · 45–55 %` |
| Convergencia con el crimeware brasileño | Si KJ-5 se confirma, el arsenal migra hacia las familias de banca brasileñas y las TTP se alejan del perfil que describe este informe. Nuestras detecciones, calibradas sobre lo colombiano, pierden cobertura | `Poco probable · 20–45 %` |
| Salto a extorsión con cifrado | El acceso ya lo tienen; monetizarlo con cifrado es un cambio de modelo de negocio, no de capacidad. Ninguna fuente lo ha observado y el perfil del grupo es de robo y espionaje, no de interrupción | `Remoto · 5–15 %` |

## E-4. Decisiones que este informe pide al nivel estratégico

<!-- cti:table highlight="Chile|chilen|CSIRT|21.663|judicial" -->

| # | Decisión | Fundamento | Plazo |
|---|---|---|---|
| E-a | Someter a **prueba de detección la cadena `wscript/cscript → PowerShell → utilidad .NET`** y cerrar la brecha si existe. Es un ejercicio de un día para el equipo de detección | KJ-3: la cadena es idéntica desde 2019. Si no la detectamos, la deuda no es de este informe, es de siete años | 30 días |
| E-b | **Equiparar el tratamiento del correo intra-tenant al del correo externo**, incluidos los buzones compartidos y funcionales: inspección de adjuntos, reescritura de enlaces y detonación en entorno aislado | KJ-2: el vector documentado es un remitente institucional legítimo comprometido. El perímetro no participa y DMARC, DKIM y SPF se cumplen | 45 días |
| E-c | Establecer y comunicar un **procedimiento de verificación de notificaciones judiciales, tributarias y laborales** por canal independiente, con la lista de dominios oficiales chilenos legítimos. Responsable conjunto de Seguridad y Asuntos Corporativos | KJ-1: el control eficaz es de proceso, no técnico. Un empleado que sabe cómo verificar una citación no necesita detectar un adjunto | 60 días |
| E-d | **Bloquear por defecto el egreso a dominios de DNS dinámico gratuito** desde estaciones de trabajo, con excepciones nominales y justificadas | El actor ha usado `duckdns.org`, `noip.com`, `con-ip.com`, `ip-ddns.com`, `ddns-ip.net` e `ydns.eu` durante ocho años. Casi ningún uso de negocio depende de ellos | 45 días |
| E-e | Decidir la **política de ejecución de intérpretes de script** en estaciones de trabajo: restricción de `wscript.exe` y `cscript.exe` por directiva, o al menos registro obligatorio de su actividad | Corta el primer eslabón de la cadena para la totalidad de las campañas documentadas de este actor desde 2019 | 90 días |
| E-f | **Consultar al CSIRT Nacional** sobre actividad compatible con este actor contra entidades chilenas, y solicitar al ColCERT el acceso a su alerta `AL-20260925-119` por el canal entre equipos de respuesta | KJ-4 y brecha `G-1`: el análisis más específico que existe no está en nuestras manos, y la ausencia de casos chilenos puede ser falta de sensores | 30 días |
| E-g | Incorporar al programa de formación un **módulo específico de señuelo judicial y tributario en español**, con ejemplos reales y con la instrucción explícita de que un buzón funcional nunca verifica por el mismo canal | El pretexto es el centro de gravedad del actor y es el único vector que ninguna herramienta cubre por completo | 90 días |

---

# NIVEL OPERACIONAL
### Para: Jefatura de SOC · Respuesta a Incidentes · Threat Hunting · Seguridad del Correo · Horizonte: semanas–meses

## O-1. Identificación y alias

| Designación | Origen | Grado de equivalencia |
|---|---|---|
| `APT-C-36` | Qihoo 360 (2019), primera designación publicada | Referencia en MITRE ATT&CK (`G0099`) |
| `Blind Eagle` | Industria, designación de uso más extendido | Equivalente |
| `TAG-144` | Recorded Future / Insikt Group | Equivalente, con la salvedad de que Insikt subdivide la actividad en cinco clústeres |
| `AguilaCiega` | Industria (traducción al español del anterior) | Equivalente |
| `APT-Q-98` | Qi An Xin | Equivalente |
| `Red Akodon` | Industria | **Solapamiento parcial.** Insikt vincula ambas actividades; no se afirma identidad |
| `Hive0131` | IBM X-Force | **Agrupación distinta.** Comparte el uso del cargador Caminho, no la identidad. No fusionar |

<!-- cti:note type="warn" -->

> ⚠ **Nota de tradecraft.** Los cinco primeros alias son equivalentes y así los trata MITRE.
> Los dos últimos no: `Red Akodon` es un solapamiento declarado por una sola fuente, y
> `Hive0131` es otra agrupación que simplemente **compra el mismo cargador** en el mismo
> mercado. Tratar a Hive0131 como Blind Eagle por compartir `Caminho` sería el mismo error
> que tratar como un solo actor a todos los que usan Cobalt Strike. Además, Insikt distingue
> **cinco clústeres** dentro de TAG-144 con TTP solapadas pero distintas: cuando una fuente
> dice «Blind Eagle» puede estar describiendo a cualquiera de ellos, y los detalles técnicos
> de uno no son necesariamente válidos para otro.

## O-2. Estructura y atribución

| Eje de atribución | Valoración | Confianza |
|---|---|---|
| Clúster técnico | Actividad coherente y sostenida desde 2018, con cadena de ejecución estable y señuelo constante. Insikt la subdivide en cinco clústeres con solapamiento de herramientas | Alta |
| Grupo organizado | Operación con infraestructura propia, panel de control de botnet, gestión de campañas con nombres de código y continuidad de ocho años. No es actividad oportunista | Alta |
| Origen geográfico | **Sospechoso sudamericano** (MITRE). El indicio técnico más citado es el desfase horario `-0500` en los metadatos de los commits del repositorio usado para distribuir las cargas | Moderada |
| Motivación | Doble y simultánea: espionaje contra entidades públicas y robo de credenciales financieras. Kaspersky lo describe como «versatilidad para alternar» entre ambas | Alta |
| Nexo estatal | **No planteado por ninguna fuente.** Ni MITRE, ni Kaspersky, ni Check Point, ni Zscaler sugieren patrocinio estatal | Alta (en la negativa) |
| Identidad nominal | Ninguna | Baja |
| Vínculo con el ecosistema brasileño | Convergencia de indicios en cuatro fuentes a lo largo de dos años. Véase KJ-5 | Moderada |

*Razonamiento sobre el origen:* el desfase `-0500` corresponde a la hora de Colombia, Ecuador y Perú. Check Point lo matiza en el cuerpo de su informe —«podría indicar»— y lo afirma con más firmeza en su resumen ejecutivo, una inconsistencia que conviene conocer. El dominio del español procesal colombiano, la selección de objetivos y la suplantación de instituciones colombianas concretas apuntan en la misma dirección.

*Contraargumento que debe consignarse:* el desfase horario de un commit lo fija el cliente de git y se puede poner a mano. El idioma acredita al redactor del señuelo, no al operador de la infraestructura. Y la presencia creciente de portugués, de alojamiento brasileño y de un panel en portugués de Brasil admite dos lecturas: colaboración con terceros —la hipótesis que plantea Kaspersky— o un grupo cuya composición ha cambiado. Para nuestros fines defensivos la distinción es secundaria; para la atribución es decisiva, y no hay base pública para resolverla.

## O-3. Modelo de operación

**Lo que no hace.** No desarrolla implantes. En ocho años no se le atribuye una sola familia de malware propia: usa `njRAT`, `AsyncRAT`, `LimeRAT`, `BitRAT`, `Remcos`, `DcRat`, `QuasarRAT` y una variante modificada de `Imminent Monitor`. Lo único que personaliza son añadidos funcionales sobre código ajeno —el caso mejor documentado es la conversión de Quasar en troyano bancario, conocido como `BlotchyQuasar`, añadiéndole vigilancia de títulos de ventana del navegador y activación del registrador de pulsaciones cuando el usuario abre el portal de una de diez entidades financieras colombianas.

**Lo que compra.** Aquí está la clave de su evolución. Un servicio de criptado por suscripción anunciado en Telegram (`Vbs-Crypter`, de «Crypters and Tools») que explica la calidad del ofuscado de sus scripts. Un empaquetador como servicio, `HeartCrypt`. Un cargador como servicio, `Caminho`, probablemente originado en el ecosistema criminal brasileño. Alojamiento a prueba de balas en Proton66. Y todo lo gratuito que puede: DNS dinámico, repositorios públicos, Discord, Internet Archive, sitios de pegado de texto.

**Lo que aporta.** Tres cosas, y son las que lo hacen peligroso. Primera, el pretexto: terminología procesal correcta, números de proceso verosímiles, instituciones reales. Segunda, el acceso: cuentas institucionales comprometidas que usa como remitente, lo que convierte el correo en tráfico interno. Tercera, la persistencia operativa: ocho años sin interrupciones conocidas, con rotación constante de infraestructura barata.

**Lo que esto implica para la defensa.** Un adversario que compra capacidad evoluciona a saltos y sin previo aviso, porque su arsenal depende de lo que salga al mercado y no de lo que sepa programar. Pero también significa que **su cadena de entrega y ejecución es conservadora**: lo que compra son capas de ofuscación y de carga, no formas nuevas de ejecutar. De ahí que la cadena de KJ-3 lleve siete años intacta, y de ahí que la detección conductual envejezca bien frente a este actor en particular.

## O-4. Nuestra exposición

<!-- cti:note type="gap" -->

> ⬛ **Sección sin evaluar — requiere telemetría e inventario internos.** Las preguntas de
> abajo son el trabajo mínimo para convertir este perfil en inteligencia propia. Tres de
> ellas (X-1, X-2, X-5) se pueden responder en una tarde y son las que más cambian la
> postura.

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| X-1 | ¿Se da en nuestra flota la secuencia `wscript.exe` o `cscript.exe` creando `powershell.exe`? ¿Con qué frecuencia y desde qué rutas? Establecer la línea base antes de alertar | EDR · telemetría de creación de procesos | Ingeniería de Detección |
| X-2 | ¿Abren conexiones de red `RegSvcs.exe`, `MSBuild.exe`, `InstallUtil.exe`, `jsc.exe`, `AppLaunch.exe` o `csc.exe` en alguna estación de trabajo? Cualquier resultado positivo merece investigación inmediata | EDR · telemetría de red por proceso | SOC |
| X-3 | ¿Nuestros controles de correo inspeccionan adjuntos y reescriben enlaces en el correo **intra-tenant**, o solo en el que cruza el perímetro? ¿Incluyen los buzones compartidos y funcionales? | Configuración de la plataforma de correo | Seguridad del Correo |
| X-4 | ¿Cuántos buzones compartidos o funcionales existen, quién los lee, y tienen autenticación multifactor y acceso condicional equivalentes a los nominales? | Inventario de identidad | Identidad |
| X-5 | ¿Permitimos el egreso a `*.duckdns.org`, `*.ip-ddns.com`, `*.ddns-ip.net`, `*.con-ip.com`, `*.ydns.eu` y `*.noip.com` desde estaciones de trabajo? | Proxy · DNS · cortafuegos | Redes |
| X-6 | ¿Se permite la descarga directa de ejecutables y scripts desde `raw.githubusercontent.com`, `bitbucket.org/*/downloads`, `cdn.discordapp.com`, `archive.org`, `paste.ee` y `textbin.net` por procesos que no son navegadores? | Proxy · EDR | Redes / SOC |
| X-7 | ¿Está `AutoIt3.exe` presente en la flota? ¿Con qué justificación y desde qué rutas se ejecuta? | Inventario de software · EDR | TI / SOC |
| X-8 | ¿Permitimos adjuntos `.svg`, `.xhtml`, `.url`, `.js`, `.vbs`, `.bat` y archivos comprimidos protegidos con contraseña? ¿Y formatos antiguos como `LHA` y `UUE`? | Política de correo | Seguridad del Correo |
| X-9 | ¿Existe un procedimiento documentado y conocido por los empleados para verificar una notificación judicial o tributaria recibida por correo? | Asuntos Corporativos · Legal | Asuntos Corporativos |
| X-10 | ¿Tenemos registro y retención de la actividad de `wscript`, `cscript`, `powershell` y creación de tareas programadas, con al menos 90 días? | Revisión de fuentes del SIEM | Ingeniería de Detección |

## O-5. Cronología

<!-- cti:timeline -->

| Fecha | Hecho | Traza |
|---|---|---|
| `2018` | **Primera actividad atribuida al grupo.** MITRE fija aquí el inicio de las operaciones de espionaje y de lucro | Global |
| `2019` | Qihoo 360 publica la primera designación, `APT-C-36`, sobre campañas contra entidades colombianas | Global |
| `2024-05` | Campaña de espionaje en Colombia con artefactos cuyas cadenas y nombres de variable están **enteramente en portugués**, y alojamiento de imágenes brasileño. Kaspersky lo plantea como posible colaboración con terceros | Global |
| `2024-06` | Campaña suplantando instituciones judiciales colombianas con citación o demanda; `HijackLoader` por carga lateral de DLL sobre binarios firmados por ASUS e IObit, inyectando `AsyncRAT` | Global |
| `2024-08-19` | Kaspersky publica el primer análisis de conjunto: 87 % de las víctimas en Colombia, objetivos secundarios en **Ecuador, Chile y Panamá**, y la variante de Quasar convertida en troyano bancario contra diez entidades colombianas | LATAM |
| `2024-11-12` | Microsoft parchea `CVE-2024-43451`, que permitía filtrar el hash NTLMv2 mediante interacción mínima con un fichero `.url` | Global |
| `2024-11-18` | **Seis días después del parche**, primera muestra de Blind Eagle con un fichero `.url` que imita la técnica **sin explotarla**: no filtra el hash, pero avisa al atacante de que la víctima interactuó con el fichero | Global |
| `2024-12-10` → `12-19` | Campañas `marte`, `saturno`, `PARAISO` y `PARAISO2`. Cargas en Bitbucket, `Remcos` con nombre de botnet `redtube`, C2 en DNS dinámico. **Más de 1.600 infecciones en una sola campaña y unas 9.000 en la semana** | Global |
| `2025-01-21` → `01-22` | Campañas `socialismo` y `miami`, con enlaces a Google Drive posiblemente desde cuentas comprometidas | Global |
| `2025-02-25` | **El actor sube por error a su propio repositorio público el fichero con los datos personales cosechados**: 8.075 registros válidos y 1.634 correos, cinco de dominios `.gov.co`. Lo borra hora y media después | Global |
| `2025-02` (finales) | Darktrace observa el primer caso en red de cliente: cinco horas de actividad en una organización **colombiana**, con descarga por WebDAV, C2 en DNS dinámico y unos 60 MiB exfiltrados | LATAM |
| `2025-03-10` | Check Point publica el análisis técnico de la técnica `.url`, las campañas de diciembre y la filtración del propio actor | Global |
| `2025-06-27` | SpiderLabs vincula **con alta confianza** la infraestructura de entrega por Visual Basic del grupo al alojamiento a prueba de balas **Proton66**, y documenta kits de phishing que clonan cuatro bancos colombianos | Global |
| `2025-08-26` | Insikt Group publica el seguimiento de **cinco clústeres** distintos dentro de TAG-144, activos entre may-2024 y jul-2025, y un vínculo con `Red Akodon` | Global |
| `2025-12-16` | **Zscaler documenta la cadena completa contra una agencia del Ministerio de Comercio de Colombia**: correo desde un buzón compartido de la propia entidad, adjunto `.svg`, portal judicial falso, cargador `Caminho` oculto por esteganografía en una imagen alojada en Internet Archive, y `DCRAT` final | Global |
| `2026-07-17` | SpiderLabs publica la evolución del utillaje: dropper con **automutación**, suplantación del proceso padre, inyección por notificación de estado del núcleo, evasión del cifrado vinculado a aplicación de Chrome y persistencia mediante la tarea `Photo Studio` | Global |
| `2026-07-31` | MITRE actualiza la ficha `G0099` a la versión 2.0: 38 técnicas y nueve familias de herramientas atribuidas | Global |
| `2026-09-25` | **El ColCERT emite la alerta `AL-20260925-119`** sobre una campaña contra entidades públicas colombianas, atribuida con alto nivel de confianza. Documento marcado TLP:AMBER: su contenido no se incorpora a este informe | LATAM |
| `2026-10` → `11` | **Campaña en curso con señuelo de notificación judicial en español y portugués**, atribuida a un clúster brasileño del grupo. Unos 3.300 correos contabilizados; **Colombia, Chile y México** entre los países afectados, con objetivos en administración pública, despachos jurídicos e instituciones financieras. Fuentes secundarias, sin corroboración independiente | Chile |
| `2026-11-16` | Cierre de este informe. **Sin caso con víctima chilena nombrada, sin señuelo localizado a instituciones chilenas y sin alerta pública del CSIRT Nacional** sobre este actor | Chile |

## O-6. Hipótesis alternativas consideradas

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| H1 — Actor regional con doble motivación, espionaje y lucro, que compensa su baja sofisticación técnica con fluidez institucional | Consistente con las seis fuentes de primera mano y con la ficha de MITRE. Explica la longevidad, la elección de herramientas gratuitas y la precisión del señuelo. Ninguna fuente la contradice | `Retenida` |
| H2 — Operación con patrocinio o tolerancia estatal | **Sin evidencia.** Ninguna de las seis fuentes lo plantea, y el perfil contradice la hipótesis: un actor con respaldo estatal no filtra su propio botín por descuido ni depende de criptadores comprados en Telegram. Se consigna para que no se reabra | `Descartada` |
| H3 — No es un grupo sino varios que comparten herramientas y mercado | Parcialmente consistente y **complementaria de H1**. Insikt distingue cinco clústeres; MITRE los trata como un solo actor; Hive0131 comparte cargador sin ser el mismo grupo. Se retiene como matiz operativo: los detalles técnicos de una campaña no son trasladables sin más a otra | `Retenida como matiz` |
| H4 — El centro de gravedad se está desplazando al ecosistema criminal brasileño | Apoyada por cuatro indicios independientes en dos años (KJ-5). Ninguna fuente la afirma de forma concluyente. Importa porque, si se confirma, las TTP convergerán con la banca brasileña y nuestras detecciones calibradas sobre lo colombiano perderán cobertura | `Posibilidad real · 45–55 %` |
| H5 — La ausencia de casos chilenos documentados indica que Chile no es un objetivo real | **Inconsistente con la evidencia disponible.** Cuatro fuentes listan el país; la victimología publicada refleja dónde tienen sensores los proveedores, y Chile no es un mercado principal para ninguno de los seis. La ausencia de casos es compatible tanto con ausencia de actividad como con ausencia de visibilidad, y no distingue entre ambas | `Poco probable · 20–45 %` |
| H6 — El grupo evolucionará hacia extorsión con cifrado | Sin indicios. Ocho años de robo y espionaje sin un solo incidente destructivo documentado. El acceso que obtienen sería suficiente, de modo que la ausencia es una elección de modelo de negocio y no una limitación de capacidad | `Remoto · 5–15 %` |

**Supuesto clave.** Que la cadena de ejecución `script → PowerShell → vaciado de proceso sobre utilidad .NET` seguirá siendo el patrón dominante. **Si es falso** —si el actor adopta cargadores que ejecuten sin tocar ninguno de esos binarios, por ejemplo mediante ensamblados cargados por reflexión en un proceso arbitrario, algo que `Caminho` ya hace parcialmente— entonces las detecciones D-1 y D-2 de §X-3 pierden la mayor parte de su valor y la defensa se desplaza al correo y al proceso, es decir a E-b y E-c.

**Pre-mortem.** Es mayo de 2027 y este informe resultó equivocado. Los tres finales más probables: **(1)** nos concentramos en la cadena de ejecución, el actor adoptó un cargador que no usa utilidades .NET y entró igual; **(2)** acertamos en todo lo técnico y el compromiso llegó por un buzón funcional de una filial que nadie había inventariado, con un correo interno que ningún control inspeccionó; **(3)** Chile nunca fue objetivo real, dedicamos esfuerzo de detección a un actor que no nos apuntaba, y el coste de oportunidad lo pagó otra amenaza que sí lo hacía — por eso KJ-4 se formula con confianza baja y por eso la decisión E-f es consultar antes que desplegar.

## O-7. Indicadores y señales de alerta

| # | Indicador observable | Qué señalaría | Disciplina | Responsable |
|---|---|---|---|---|
| I-1 | **Señuelo con terminología procesal chilena correcta**: Poder Judicial, Ministerio Público, causa RIT o RUC, notificación por estado diario, SII, Dirección del Trabajo, Tesorería General | Localización del pretexto a Chile. Elevaría KJ-4 a «probable» y convertiría este perfil en alerta | OSINT · informes de usuarios | Célula CTI |
| I-2 | Caso público con víctima chilena nombrada, o alerta del CSIRT Nacional sobre este actor | Cierre de la brecha `G-2`; activa revisión anticipada de este informe | OSINT gubernamental | Célula CTI |
| I-3 | Correo con señuelo judicial procedente de un dominio institucional chileno legítimo (`.gob.cl`, `.gov.cl`, `.cl` de institución pública) | Compromiso de una cuenta institucional en el país, el vector de KJ-2 aplicado localmente | Telemetría de correo · intercambio sectorial | Seguridad del Correo |
| I-4 | Aparición de credenciales de nuestros buzones funcionales o compartidos en volcados públicos | Precondición directa del vector de remitente comprometido | Vigilancia de filtraciones | Identidad |
| I-5 | Publicación del análisis técnico de la campaña de oct-nov 2026 por un proveedor de primera mano | Permite sustituir las fuentes secundarias de §3.3 y confirmar o descartar la cifra de 3.300 correos y el alcance a Chile | OSINT comercial | Célula CTI |
| I-6 | Adopción por el grupo de un cargador que ejecute sin usar utilidades .NET de Windows | Rompe el supuesto clave de §O-6 y obliga a rehacer §X-3 | OSINT comercial | Ingeniería de Detección |
| I-7 | Convergencia observable con familias de banca brasileñas | Confirma H4 y KJ-5; obliga a ampliar la cobertura de detección más allá del perfil colombiano | OSINT comercial | Célula CTI |
| I-8 | Uso de este actor, o de su infraestructura, como acceso inicial revendido a un grupo de extorsión | Materializa H6 y cambia el perfil de impacto de robo a interrupción | OSINT · foros criminales | Célula CTI |

---

# NIVEL TÁCTICO
### Para: Analistas de SOC · Ingeniería de Detección · Threat Hunting · Horizonte: días–semanas

## T-1. Cadena de intrusión

<!-- cti:stages title="Tres etapas, y la primera es la que importa" dwell="next" -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 01 · Pretexto | El acto administrativo que no se puede ignorar | Correo con señuelo judicial, de fiscalía, tributario o laboral · **remitente institucional legítimo comprometido**, a menudo intra-tenant hacia un buzón funcional de TI · adjunto `.svg` que abre un HTML embebido en base64 · portal judicial falso que descarga un `.js` · o fichero `.url` que imita `CVE-2024-43451` · o adjunto `PDF`/`DOCX` con macro · o enlace acortado con filtrado por geolocalización que redirige al sitio real si el visitante no está en el país objetivo · archivos `ZIP`, `RAR` con contraseña, `LHA` o `UUE` |
| Etapa 02 · Ejecución | Script, PowerShell oculto y una utilidad de Windows vaciada | Cadena de dos o tres fragmentos de JavaScript o Visual Basic en memoria, sin escritura en disco · WMI `Win32_Process.Create()` con `ShowWindow=0` para lanzar PowerShell sin ventana · descarga de la carga desde GitHub, Bitbucket, Discord, Internet Archive, `paste.ee` o `textbin.net` · esteganografía: carga en base64 dentro de un PNG, delimitada por `BaseStart-` y `-BaseEnd` · carga del ensamblado .NET por reflexión · **vaciado de proceso sobre `RegSvcs.exe`, `MSBuild.exe`, `InstallUtil.exe`, `jsc.exe`, `AppLaunch.exe` o `csc.exe`** · suplantación del proceso padre a `explorer.exe` · abuso de `AutoIt3.exe` legítimo con script remoto |
| Etapa 03 · Objetivo | Control remoto, credenciales y permanencia barata | Troyano de catálogo: `AsyncRAT`, `DCRAT`, `Remcos`, `njRAT`, `LimeRAT`, `BitRAT`, `QuasarRAT` modificado · registro de pulsaciones activado al detectar el portal de un banco en el título de la ventana · robo de credenciales y cookies de navegadores Chromium, con evasión del cifrado vinculado a aplicación · volcado del Administrador de credenciales, Outlook, Thunderbird y claves Wi-Fi · escritorio remoto oculto · persistencia por clave `Run`, carpeta de Inicio y tarea programada `Photo Studio` · exclusión de Defender para todo `C:\` · C2 sobre DNS dinámico gratuito en puertos no estándar |

**Permanencia:** no hay cifra pública de permanencia mediana. El único caso con duración publicada es el de Darktrace: **unas cinco horas** desde la primera descarga hasta la exfiltración de unos 60 MiB, en una red sin respuesta autónoma activada.

<!-- cti:note type="info" -->

> **Dónde se rompe la cadena más barato.** La **etapa 01 se corta con proceso y con
> política de correo**: verificación de notificaciones por canal independiente (E-c),
> inspección del correo intra-tenant (E-b) y bloqueo de los tipos de adjunto que ningún
> flujo de negocio necesita. La **etapa 02 se corta con una línea base de ejecución de
> scripts** y con la regla de que seis binarios .NET del sistema no abren conexiones de
> red: es la intervención con mejor relación coste-efecto de este informe, y además
> envejece bien porque el actor no ha cambiado ese eslabón en siete años. La **etapa 03
> solo se corta con EDR y con contención**, y a esas alturas ya hay credenciales fuera.

## T-2. Mapa MITRE ATT&CK

<!-- cti:matrix -->

| Táctica | ID | Técnica | Procedimiento observado |
|---|---|---|---|
| Desarrollo de recursos | T1583.001 | Acquire Infrastructure: Domains | Dominios propios para alojar cargas |
| Desarrollo de recursos | T1583.003 | Acquire Infrastructure: Virtual Private Server | Servidores virtuales en la infraestructura operativa; Insikt describe además direcciones en rangos de proveedores colombianos |
| Desarrollo de recursos | T1583.006 | Acquire Infrastructure: Web Services | Alojamiento de imágenes, Pastebin, Discord, GitHub, Google Drive, Bitbucket, Dropbox, Internet Archive, `paste.ee`, `textbin.net`, `gofile.io` |
| Desarrollo de recursos | T1584.005 | Compromise Infrastructure: Botnet | Panel de gestión de botnet con interfaz en portugués de Brasil; 264 equipos infectados en el panel observado |
| Desarrollo de recursos | T1586.002 | Compromise Accounts: Email Accounts | **Uso sistemático de cuentas de correo institucionales comprometidas como remitente**, incluidas cuentas de entidades públicas |
| Desarrollo de recursos | T1586.003 | Compromise Accounts: Cloud Accounts | Cuentas de Google Drive comprometidas, una de ellas de un organismo público colombiano |
| Desarrollo de recursos | T1587.001 | Develop Capabilities: Malware | Personalización de `njRAT`, `AsyncRAT`, `LimeRAT` y `BitRAT`; conversión de Quasar en troyano bancario (`BlotchyQuasar`) |
| Desarrollo de recursos | T1588.001 | Obtain Capabilities: Malware | `HeartCrypt` (empaquetador como servicio), `PureCrypter`, `Caminho` (cargador como servicio), `Remcos` y demás troyanos de código abierto |
| Desarrollo de recursos | T1588.002 | Obtain Capabilities: Tool | Utillaje conocido en comunidades criminales, incluida una variante modificada de `Imminent Monitor` y el criptador por suscripción `Vbs-Crypter` |
| Reconocimiento | T1593 | Search Open Websites/Domains | Recopilación de información sobre Bancolombia, BBVA, Banco Caja Social y Davivienda para construir las páginas de phishing |
| Desarrollo de recursos | T1683.001 | Generate Content: Written Content | Redacción de correos que imitan notificaciones y documentos oficiales con terminología procesal correcta |
| Desarrollo de recursos | T1683.002 | Generate Content: Audio-Visual Content | Páginas que replican portales de banca en línea y el portal de la rama judicial colombiana, con HTML, CSS e imágenes clonadas |
| Desarrollo de recursos | T1608.001 | Stage Capabilities: Upload Malware | Cargas alojadas en repositorios y sitios propios y en servicios legítimos de terceros |
| Acceso inicial | T1566.001 | Phishing: Spearphishing Attachment | Adjuntos `PDF`, `DOCX`, `.svg`, `.url` y archivos `RAR` protegidos con contraseña para eludir la pasarela de correo |
| Acceso inicial | T1566.002 | Phishing: Spearphishing Link | Enlaces que aparentan llevar a notificaciones oficiales urgentes, a veces mediante acortadores (`cort[.]as`, `acortaurl[.]com`, `gtly[.]to`) |
| Movimiento lateral | T1534 | Internal Spearphishing | **Correo enviado desde una cuenta comprometida de la propia organización a un buzón compartido vigilado por el área de TI** |
| Ejecución | T1204.001 | User Execution: Malicious Link | El usuario pulsa el enlace de la notificación falsa |
| Ejecución | T1204.002 | User Execution: Malicious File | El usuario abre el adjunto, habilita macros, o abre el fichero en Google Drive que dispara la petición WebDAV |
| Ejecución | T1059.001 | Command and Scripting Interpreter: PowerShell | PowerShell en cadenas sin fichero que descargan y cargan la siguiente etapa |
| Ejecución | T1059.005 | Command and Scripting Interpreter: Visual Basic | Visual Basic Script como vector inicial, incluido en documento de Word con ejecución al abrir. SpiderLabs observa scripts de 6.000 a 20.000 líneas |
| Ejecución | T1059.007 | Command and Scripting Interpreter: JavaScript | Cadena sin fichero de tres fragmentos de JavaScript que ejecutan las etapas siguientes |
| Ejecución | T1047 | Windows Management Instrumentation | `Win32_Process.Create()` para lanzar PowerShell |
| Ejecución | T1053.005 | Scheduled Task/Job: Scheduled Task | Tarea `Photo Studio` apuntando a `%LOCALAPPDATA%\PhotoStudioVBS\PhotoStudio.vbs`; `schtasks /sc minute /mo 1` hacia un `.vbs` en `%TEMP%`; tareas disfrazadas como de Google |
| Persistencia | T1547.001 | Boot or Logon Autostart Execution: Registry Run Keys | Clave `Run` cuando se ejecuta sin privilegios, y carpeta de Inicio |
| Evasión | T1564.003 | Hide Artifacts: Hidden Window | `ShowWindow` a cero en `Win32_ProcessStartup` para ocultar PowerShell |
| Evasión | T1574.001 | Hijack Execution Flow: DLL | Carga lateral de DLL para ejecutar `HijackLoader`, sobre binarios firmados por ASUS e IObit |
| Evasión | T1036.004 | Masquerading: Masquerade Task or Service | Tareas programadas disfrazadas de tareas de Google; tarea `Photo Studio` |
| Evasión | T1036.005 | Masquerading: Match Legitimate Resource Name or Location | Ejecutables con nombre de ficheros legítimos; `AutoIt3.exe` renombrado a `.pif` |
| Evasión | T1027 | Obfuscated Files or Information | `ConfuserEx`, `NET-Reactor`, `CryptoObfuscator`; adjuntos cifrados con contraseña; compresión en `ZIP`, `LHA` y `UUE` |
| Evasión | T1027.003 | Obfuscated Files or Information: Steganography | Carga en base64 dentro de un PNG alojado en Internet Archive, delimitada por `BaseStart-` y `-BaseEnd`; código en la sección de recursos de ejecutables |
| Evasión | T1027.013 | Obfuscated Files or Information: Encrypted/Encoded File | XOR con clave que se regenera en cada ejecución, AES-256-ECB, base64 invertido |
| Evasión | T1027.016 | Obfuscated Files or Information: Junk Code Insertion | Inserción de caracteres y código basura para ofuscar los scripts |
| Evasión | T1055.012 | Process Injection: Process Hollowing | **Vaciado de proceso sobre `RegSvcs.exe`, `MSBuild.exe`, `InstallUtil.exe`, `jsc.exe`, `AppLaunch.exe` y `csc.exe`** |
| Evasión | T1134.004 | Access Token Manipulation: Parent PID Spoofing | Suplantación del proceso padre a `explorer.exe` mediante `PROC_THREAD_ATTRIBUTE_PARENT_PROCESS` |
| Evasión | T1562.001 | Impair Defenses: Disable or Modify Tools | Exclusión de Defender para todo el volumen `C:\`; desactivación de Defender; técnica de evasión de AMSI para 32 y 64 bits |
| Evasión | T1548.002 | Abuse Elevation Control Mechanism: Bypass UAC | Cinco mecanismos observados: `fodhelper`, `cmstp`, `eventvwr`, `computerdefaults` y XML del Programador de tareas |
| Evasión | T1480 | Execution Guardrails | Filtrado por geolocalización en la entrega: si la conexión no procede del país objetivo, el ataque se cancela y la víctima se redirige al sitio legítimo suplantado |
| Evasión | T1497.001 | Virtualization/Sandbox Evasion: System Checks | Inspección de descripciones de memoria del caché de WMI para detectar entorno de análisis |
| Acceso a credenciales | T1555.003 | Credentials from Password Stores: Credentials from Web Browsers | Robo de credenciales y cookies en más de 20 perfiles de navegadores Chromium, con evasión del cifrado vinculado a aplicación |
| Acceso a credenciales | T1555.004 | Credentials from Password Stores: Windows Credential Manager | Volcado del Administrador de credenciales de Windows |
| Acceso a credenciales | T1056.001 | Input Capture: Keylogging | Registro de pulsaciones activado al coincidir el título de la ventana del navegador con el de una de diez entidades financieras colombianas |
| Descubrimiento | T1083 | File and Directory Discovery | Reconocimiento del sistema de ficheros previo a la recolección |
| Mando y control | T1105 | Ingress Tool Transfer | Descarga de la carga desde dominio especificado tras abrir el documento |
| Mando y control | T1568 | Dynamic Resolution | DNS dinámico: `DuckDNS`, `noip[.]com`, `con-ip[.]com`, `ip-ddns[.]com`, `ddns-ip[.]net`, `ydns[.]eu` |
| Mando y control | T1568.002 | Dynamic Resolution: Domain Generation Algorithms | Dominios dinámicos y generación algorítmica atribuidos a la campaña de 2026 por fuente secundaria |
| Mando y control | T1571 | Non-Standard Port | Puertos observados: 4050, 1512, 30201, 30204, 4782, 6001 |
| Mando y control | T1095 | Non-Application Layer Protocol | C2 por sockets del troyano final |
| Acceso remoto | T1133 | External Remote Services | Uso de VPN en la infraestructura operativa; escritorio remoto oculto en la víctima |
| Exfiltración | T1041 | Exfiltration Over C2 Channel | Exfiltración por el canal de mando y control; unos 60 MiB en el caso observado por Darktrace |
| Exfiltración | T1567.002 | Exfiltration Over Web Service: Exfiltration to Cloud Storage | Salida hacia servicios en la nube |

<!-- cti:note type="warn" -->

> ⚠ **Dos notas sobre esta tabla.** La primera: las técnicas provienen de la ficha `G0099`
> v2.0 de MITRE más los procedimientos concretos que publican Check Point, Kaspersky,
> Zscaler, SpiderLabs y Darktrace; donde una técnica aparece en el mapeo de un proveedor
> pero su procedimiento no está descrito, se ha omitido en lugar de rellenarla por
> conjetura. La segunda: Darktrace publica también identificadores del dominio ICS
> (`T0862`, `T0865`, `T0817`, `T0843`, `T0869`, `T0849`) junto a los de empresa. **No se han
> incorporado**: no hay ningún indicio en las fuentes de que este actor haya tocado un
> entorno industrial, y arrastrar ese mapeo produciría una expectativa falsa de riesgo OT.

## T-3. Dónde atacamos en la Pirámide del Dolor

<!-- cti:pyramid -->

| Nivel | Qué contiene en este informe y qué vale | Valor |
|---|---|---|
| Hashes | Veintitantos en el Anexo A. **Valor prácticamente nulo contra este actor:** SpiderLabs es explícito en que caducan en el momento en que una muestra se ejecuta una vez, porque el dropper regenera su clave de cifrado y sus identificadores en cada arranque. Sirven para retrohunt y para nada más | Base · valor trivial |
| IP · Dominios | Más de treinta en el Anexo A, casi todos en servicios de DNS dinámico gratuito que rotan en días. El bloqueo por dominio individual es trabajo perdido; **el bloqueo por sufijo de DNS dinámico, en cambio, sí tiene efecto** y es la decisión E-d | Valor bajo |
| Artefactos | **Aquí está el valor inesperado de este actor.** Tarea `Photo Studio`, carpeta `PhotoStudioVBS`, prefijo `zv` en identificadores, decodificador `Wales()`, exportado `VAI` en `ClassLibrary1.Home`, marcadores `BaseStart-`/`-BaseEnd`, mutex `mono1234`, clave AES `aPZ0ze9qOhazFFqspYVRZ8BW14nGuRUe`, ruta de compilación `JC-46`, nombres de campaña. Llevan meses sin cambiar | Valor medio |
| Herramientas | `AutoIt3.exe` legítimo, `wscript`, `cscript`, PowerShell, WMI y seis utilidades .NET del propio Windows. Todas legítimas y presentes en cualquier flota: **detectar por contexto y por relación padre-hijo, nunca por presencia** | Valor alto |
| TTP | La cadena `script → PowerShell oculto → vaciado de proceso sobre utilidad .NET`, el correo intra-tenant desde remitente institucional comprometido, y el pretexto judicial. **Siete años sin cambiar.** Aquí debe concentrarse todo el esfuerzo, y aquí es donde este actor es más vulnerable que la media | Cima · valor máximo |

## T-4. Hipótesis de caza prioritarias

<!-- cti:accordion critical="^(H-1|H-2|H-3)\b" regional="^(H-12|H-13|H-14)\b" -->

**H-1 — Intérprete de script creando PowerShell.** `wscript.exe` o `cscript.exe` como proceso padre de `powershell.exe`, `pwsh.exe` o `cmd.exe`. Fuente: telemetría de creación de procesos del EDR. Ventana: 30 días hacia atrás para establecer la línea base antes de alertar. **Es la hipótesis madre de este informe:** cubre todas las campañas documentadas del actor desde 2019 y no depende de ningún indicador. Fidelidad esperada muy alta en una flota administrada; falsos positivos conocidos: scripts de inicio de sesión corporativos y herramientas de inventario antiguas, exceptuables por ruta y por firma. Si esta consulta devuelve volumen alto, el hallazgo es que tenemos un problema de línea base, no que el actor esté dentro.

**H-2 — Utilidad .NET de Windows con actividad de red.** Conexiones salientes originadas por `RegSvcs.exe`, `MSBuild.exe`, `InstallUtil.exe`, `jsc.exe`, `AppLaunch.exe` o `csc.exe` en estaciones de trabajo. Fuente: telemetría de red por proceso del EDR. **Ninguno de esos seis binarios tiene razón legítima para hablar con Internet desde el puesto de un usuario.** En un servidor de compilación sí, y por eso la regla se acota a estaciones. Fidelidad esperada extremadamente alta; es la consulta que más probablemente produzca un hallazgo real si el actor está dentro.

**H-3 — Vaciado de proceso sobre esas mismas utilidades.** Creación de uno de los seis binarios en estado suspendido, seguida de escritura en su memoria y reanudación, o discrepancia entre la imagen en disco y la imagen en memoria. Fuente: eventos de inyección del EDR. Complementar con la variante de 2026: creación de proceso con padre declarado `explorer.exe` desde un árbol que no lo tiene, es decir suplantación de PID padre. Fidelidad muy alta; cobertura dependiente de las capacidades del EDR, lo que la convierte también en prueba de nuestra instrumentación.

**H-4 — Exclusión de Defender para un volumen completo.** Añadido de una exclusión de ruta que cubra `C:\` o la raíz de cualquier volumen, o desactivación de la protección en tiempo real. Fuente: eventos de Defender, auditoría de directiva, registro. **Ningún administrador legítimo excluye un volumen entero.** Fidelidad extremadamente alta y coste nulo de implementación; toda ocurrencia es incidente, no alerta.

**H-5 — Persistencia por tarea programada con nombre de aplicación inocua.** Tarea `Photo Studio` con acción `wscript.exe`; cualquier tarea que apunte a un `.vbs`, `.js` o `.bat` en `%TEMP%`, `%APPDATA%` o `%LOCALAPPDATA%`; tareas con intervalo de un minuto; carpeta `%LOCALAPPDATA%\PhotoStudioVBS`. Fuente: inventario de tareas programadas, eventos 4698 y 106. Fidelidad alta; los artefactos son triviales de cambiar pero llevan meses intactos.

**H-6 — Descarga de ejecutable o script por un proceso que no es un navegador.** Peticiones a `raw.githubusercontent.com`, `bitbucket.org/*/downloads/*`, `cdn.discordapp.com/attachments/*`, `archive.org/download/*`, `paste.ee`, `textbin.net`, `gofile.io` o `drive.usercontent.google.com` originadas por `powershell.exe`, `wscript.exe`, `cscript.exe`, `mshta.exe` o `certutil.exe`. Fuente: proxy correlacionado con proceso, o telemetría de red del EDR. Fidelidad alta. **Advertencia explícita: no bloquear esos dominios sin más** —son servicios legítimos de uso cotidiano—; la señal está en el proceso que los solicita.

**H-7 — Egreso a DNS dinámico gratuito.** Resolución o conexión a `*.duckdns.org`, `*.noip.com`, `*.con-ip.com`, `*.ip-ddns.com`, `*.ddns-ip.net`, `*.ydns.eu`, `*.longmusic.com` y los sufijos equivalentes del catálogo propio. Fuente: registros de DNS y de proxy. Fidelidad alta desde estaciones de trabajo; conviene acompañarla de la decisión E-d, porque detectar sin bloquear aquí aporta poco.

**H-8 — `AutoIt3.exe` con script remoto.** Ejecución del intérprete legítimo de AutoIt desde una ruta escribible por el usuario, con un argumento que no termina en `.au3`, o renombrado con extensión `.pif`. Fuente: creación de procesos. Fidelidad muy alta: es una técnica de 2026 del actor y tiene muy poco uso legítimo en una flota corporativa.

**H-9 — PowerShell con ventana oculta lanzado por WMI.** Creación de `powershell.exe` cuyo proceso padre es `WmiPrvSE.exe`, especialmente con `-WindowStyle Hidden`, `-EncodedCommand` o cadenas en base64 largas en la línea de comandos. Fuente: creación de procesos con línea de comandos registrada. Fidelidad alta; requiere que el registro de línea de comandos esté habilitado, lo que es la brecha más común de §T-5.

**H-10 — Acceso no-navegador a datos de perfiles de Chromium.** Procesos distintos del navegador leyendo `Login Data`, `Cookies`, `Local State` o clonando carpetas de perfil; uso del servicio de descifrado vinculado a aplicación por un proceso no autorizado. Fuente: auditoría de acceso a ficheros del EDR. Fidelidad alta; cubre la capacidad de robo de credenciales de 2026 del actor.

**H-11 — Adjunto `.svg`, `.url`, `.xhtml`, `.js` o `.vbs` en correo entrante.** Enumerar su volumen en los últimos 90 días y el destinatario. Complementar con la señal de WebDAV: agente de usuario `Microsoft-WebDAV-MiniRedir/*` saliendo hacia una IP externa por el puerto 80, que delata un fichero `.url` abierto. Fuente: registros de la pasarela de correo y del proxy. Fidelidad alta; **ninguno de esos cinco tipos de adjunto tiene uso legítimo entrante en la práctica totalidad de las organizaciones.**

**H-12 — Correo intra-tenant con señuelo de notificación oficial.** Mensajes originados en buzones internos, dirigidos a buzones compartidos o funcionales, cuyo asunto contenga terminología judicial, tributaria o laboral. Fuente: registros de la plataforma de correo, no de la pasarela perimetral —esa no los ve—. **Es la hipótesis que corresponde al vector de KJ-2 y la que más probablemente esté sin cobertura hoy.** Fidelidad moderada; requiere lista de términos y calibración con Asuntos Corporativos.

**H-13 — Señuelo localizado a instituciones chilenas.** Buscar en el correo entrante y en los informes de usuarios: `Poder Judicial`, `Oficina Judicial Virtual`, `notificación por estado diario`, `causa RIT`, `causa RUC`, `Ministerio Público`, `Fiscalía`, `SII`, `Servicio de Impuestos Internos`, `Tesorería General de la República`, `Dirección del Trabajo`, `demanda laboral`, `tutela`. Fuente: pasarela de correo, informes de usuarios. **Hoy ninguna fuente documenta este señuelo; encontrarlo sería el hallazgo más relevante que este informe puede producir**, y es el indicador `I-1` de §O-7. Fidelidad alta por especificidad, con falsos positivos legítimos en áreas legal y de personas, que deben exceptuarse por destinatario y no por término.

**H-14 — Remitente institucional chileno comprometido.** Correo con señuelo oficial procedente de dominios `.gob.cl`, `.gov.cl` o de instituciones públicas chilenas, hacia nuestros buzones. Fuente: pasarela de correo e intercambio sectorial. Fidelidad alta; el hallazgo tiene además valor para la comunidad y debería compartirse con el CSIRT Nacional.

## T-5. Brechas de visibilidad que hay que cerrar primero

| Brecha | Por qué importa aquí |
|---|---|
| Registro de línea de comandos de creación de procesos deshabilitado | Deja ciegas `H-1`, `H-8` y `H-9`, es decir las tres hipótesis que cubren la etapa 02 completa. Es un ajuste de directiva, no una compra |
| Sin telemetría de red por proceso | Deja ciega `H-2`, la hipótesis con mayor probabilidad de producir un hallazgo real |
| Correo intra-tenant no registrado ni inspeccionado | Deja ciega `H-12` y con ella el vector de acceso documentado de las dos campañas más recientes |
| Sin inventario de buzones compartidos y funcionales | No podemos acotar el destinatario del ataque ni aplicarle controles diferenciados |
| Eventos de tareas programadas no ingeridos (4698, 106) | Deja ciega `H-5`, que es la detección de persistencia más barata del informe |
| Proxy sin atribución de proceso | Degrada `H-6` a una lista de dominios legítimos, inservible para alertar |
| Sin registro de consultas DNS en estaciones de trabajo | Deja ciega `H-7` y elimina la posibilidad de retrohunt sobre los indicadores del Anexo A |
| Auditoría de acceso a ficheros de perfil de navegador no habilitada | Deja ciega `H-10` |

---

# NIVEL TÉCNICO
### Para: Ingeniería de detección · Automatización · TIP/SIEM · Vida útil: semanas–meses

## X-1. Arsenal y capacidad

| Propiedad | Valor |
|---|---|
| Troyanos de acceso remoto | `AsyncRAT` (incluida la compilación interna `JC-46`), `DCRAT`, `Remcos`, `njRAT`, `LimeRAT`, `BitRAT`, `QuasarRAT` modificado como troyano bancario (`BlotchyQuasar`), `Imminent Monitor` modificado |
| Cargadores y descargadores | `Caminho` —también llamado `VMDetectLoader`—, `PureCrypter`, `HijackLoader`, y el inyector propio `Paralell.dll` del proyecto `JC-46` |
| Empaquetadores y ofuscadores | `HeartCrypt` (empaquetador como servicio), `Vbs-Crypter` (criptador por suscripción vendido en Telegram), `ConfuserEx`, `NET-Reactor`, `CryptoObfuscator` |
| Lenguajes de la cadena | Visual Basic Script, JavaScript, PowerShell, C# compilado en memoria con `Add-Type`, AutoIt |
| Criptografía de la cadena | XOR con clave de un byte regenerada en cada ejecución (`0xE0`, `0x8F`, `0xA5`, `0x88`/`0x1E` alternados observados), AES-256-ECB, AES-256-CBC con clave e IV incrustados, base64 invertido, alfabeto base28 propio, tabla XOR rodante de 99 entradas |
| Técnicas de inyección | Vaciado de proceso (`T1055.012`) sobre `RegSvcs.exe`, `MSBuild.exe`, `InstallUtil.exe`, `jsc.exe`, `AppLaunch.exe`, `csc.exe`; inyección por notificación de estado del núcleo mediante `NtUpdateWnfStateData`; suplantación de PID padre a `explorer.exe` |
| Evasión | Exclusión de Defender para `C:\`, desactivación de Defender, evasión de AMSI para 32 y 64 bits, cinco mecanismos de elusión de UAC, comprobaciones antidepuración y antientorno virtual, ventana oculta por WMI, automutación del dropper en cada ejecución |
| Robo de credenciales | Navegadores Chromium en más de 20 perfiles con evasión del cifrado vinculado a aplicación v20, Administrador de credenciales de Windows, Outlook, Thunderbird, claves Wi-Fi, registro de pulsaciones condicionado al título de la ventana |
| Control remoto | Escritorio remoto oculto (HVNC), escritorio remoto con sesión oculta, captura de pantalla, cámara web mediante componente descargado, audio, portapapeles |
| Persistencia | Clave `Run`, carpeta de Inicio, tarea programada `Photo Studio`, tareas disfrazadas de Google, `schtasks` con intervalo de un minuto |
| Infraestructura de C2 | DNS dinámico gratuito (`DuckDNS`, `noip`, `con-ip`, `ip-ddns`, `ddns-ip`, `ydns.eu`), alojamiento a prueba de balas en Proton66, servidores con directorio abierto, VPN comerciales baratas, proveedores en rangos colombianos. Puertos no estándar: 1512, 4050, 4782, 6001, 30201, 30204 |
| Almacén de cargas | GitHub (incluido `raw.githubusercontent.com`), Bitbucket, Discord CDN, Internet Archive, Google Drive, Dropbox, `paste.ee`, `textbin.net`, `gofile.io`, Pastebin, sitios de alojamiento de imágenes |
| Lo que **no** tiene | Implante propio, exploits de día cero, capacidad destructiva documentada, cifrador de extorsión, actividad en entornos industriales |

<!-- cti:note type="info" -->

> **Lo que este cuadro dice de la defensa.** Un arsenal íntegramente comprado o descargado
> significa que **no hay nada estable que firmar**. Lo estable está en la columna de
> técnicas de inyección y en la de persistencia, y eso es precisamente lo que detecta §X-3.
> El resto del cuadro sirve para reconocer al actor cuando ya se está dentro del incidente,
> no para impedirlo.

## X-2. Artefactos persistentes entre versiones

<!-- cti:cards -->

| Categoría | Artefactos | Etiqueta |
|---|---|---|
| Persistencia por tarea | Tarea `Photo Studio` · carpeta `%LOCALAPPDATA%\PhotoStudioVBS` · fichero `PhotoStudio.vbs` · etiqueta `PhotoStudioVBS` · acción `wscript.exe` con tipo de inicio `InteractiveToken` y nivel `LeastPrivilege` | `persistencia` |
| Cadenas del cargador | Exportado `VAI` en `ClassLibrary1.Home` · marcadores `BaseStart-` y `-BaseEnd` · parámetros en portugués `caminhovbs`, `namevbs`, `persitencia`, `nomedoarquivo`, `extençao`, `startuptask`, `vmName` | `Caminho` |
| Cadenas del inyector | `Paralell.dll` · ruta de compilación `C:\Users\UserPC\source\repos\JC-46\JC-46\Paralell\Paralell\bin\Debug\CryptoObfuscator_Output\Paralell.pdb` · clases `CoutureFlow`, `StyleInjection`, `RunwayWalk` | `JC-46` |
| Cadenas del dropper | Prefijo `zv` en identificadores regenerados · decodificador `Wales()` · comentario `#XLOADER` · `ExecuteGlobal` | `dropper` |
| Claves y mutex | Mutex `mono1234` (también contraseña de derivación AES) · sal AES `{1,2,23,234,37,48,134,63,248,4}` · clave AES de DCRAT `aPZ0ze9qOhazFFqspYVRZ8BW14nGuRUe` · versión de malware `0.3.9` · cadenas de configuración `SponsorshipTimeout`, `NextActivator` | `criptografía` |
| Nombres de campaña | `socialismo` · `miami` · `PARAISO` · `PARAISO2` · `marte` · `saturno` · nombre de botnet de Remcos `redtube` | `campañas` |
| Red | Agente de usuario `Microsoft-WebDAV-MiniRedir/10.0.19044` y `/10.0.19045` · puerto 80 para la descarga por WebDAV | `WebDAV` |
| Ficheros de la cadena 2026 | `envifa.vbs` · `sostener.vbs` · `sostener2.vbs` · `31agosto.vbs` · `31diciembre.vbs` · `andre.vbs` · `hold.bat` · `hold.vbs` · `hold.js` · `System3.vbs` · `System5.vbs` · `kiSBJ4DDvg.pif` · `XjvdJar2Kf.pif` | `2026` |

## X-3. Lógica de detección prioritaria

<!-- cti:detections -->

**D-1 · CRÍTICO — Intérprete de script creando un intérprete de comandos**

```
parent_process.name IN ("wscript.exe", "cscript.exe")
AND process.name IN ("powershell.exe", "pwsh.exe", "cmd.exe", "mshta.exe")
AND NOT parent_process.path IN (<rutas de scripts corporativos aprobados>)
```

→ Contención automática en estaciones de trabajo: aislar el equipo y suspender la sesión del usuario. **Calibrar primero con 30 días de línea base**: si el volumen es alto, el hallazgo es una deuda de higiene y debe resolverse antes de activar la regla.

**D-2 · CRÍTICO — Utilidad .NET del sistema con conexión de red saliente**

```
process.name IN ("RegSvcs.exe", "MSBuild.exe", "InstallUtil.exe",
                 "jsc.exe", "AppLaunch.exe", "csc.exe")
AND network.direction == "outbound"
AND host.role == "workstation"
```

→ Contención automática: aislar el equipo. Ninguno de esos seis binarios tiene razón legítima para abrir conexiones desde el puesto de un usuario. **Excluir explícitamente servidores de compilación e integración continua por nombre de host, nunca por patrón.**

**D-3 · CRÍTICO — Vaciado de proceso o suplantación de proceso padre**

```
(process.injection.type == "process_hollowing"
 AND process.target.name IN ("RegSvcs.exe","MSBuild.exe","InstallUtil.exe",
                             "jsc.exe","AppLaunch.exe","csc.exe"))
OR (process.parent.reported == "explorer.exe"
    AND process.parent.actual != "explorer.exe")
```

→ Contención automática y preservación de memoria para análisis. La segunda condición requiere que el EDR distinga el padre declarado del real; si no lo hace, es un hallazgo de instrumentación que debe escalarse.

**D-4 · CRÍTICO — Exclusión de Defender sobre un volumen completo**

```
event.code IN (5007, 5004)
AND exclusion.path MATCHES "^[A-Za-z]:\\\\?$"
```

→ Contención automática: revertir la exclusión, aislar el equipo y abrir incidente. Ningún administrador legítimo excluye la raíz de un volumen. Toda ocurrencia es incidente confirmado, no alerta a triar.

**D-5 · ALTO — Persistencia con tarea de nombre inocuo hacia un script**

```
task.action.executable IN ("wscript.exe", "cscript.exe", "powershell.exe")
AND task.action.arguments MATCHES "\.(vbs|js|bat|ps1)$"
AND task.action.arguments MATCHES "(?i)(TEMP|APPDATA|LOCALAPPDATA|ProgramData)"
```

→ Aislar y eliminar la persistencia tras preservar el fichero. Añadir alerta nominal sobre la tarea `Photo Studio` y la carpeta `%LOCALAPPDATA%\PhotoStudioVBS`, y sobre cualquier tarea con intervalo de un minuto.

**D-6 · ALTO — PowerShell oculto lanzado por WMI**

```
parent_process.name == "WmiPrvSE.exe"
AND process.name IN ("powershell.exe", "pwsh.exe")
AND (cmdline CONTAINS_ANY ("-WindowStyle Hidden", "-w hidden", "-EncodedCommand", "-enc")
     OR cmdline MATCHES "[A-Za-z0-9+/]{200,}={0,2}")
```

→ Investigación prioritaria en menos de 30 minutos. Exige registro de línea de comandos habilitado, que es la brecha más frecuente de §T-5.

**D-7 · ALTO — `AutoIt3.exe` con script remoto o renombrado**

```
(process.original_file_name == "AutoIt3.exe" AND process.name != "AutoIt3.exe")
OR (process.name == "AutoIt3.exe"
    AND process.executable MATCHES "(?i)(Users|TEMP|APPDATA|ProgramData)"
    AND NOT cmdline MATCHES "\.au3\b")
```

→ Aislar y preservar. Detecta el intérprete legítimo renombrado a `.pif` y la ejecución con script remoto, ambas técnicas de 2026 del actor.

**D-8 · ALTO — Descarga de carga por proceso que no es navegador**

```
process.name IN ("powershell.exe","wscript.exe","cscript.exe",
                 "mshta.exe","certutil.exe","curl.exe")
AND url.domain IN ("raw.githubusercontent.com","bitbucket.org",
                   "cdn.discordapp.com","archive.org","paste.ee",
                   "textbin.net","gofile.io","drive.usercontent.google.com")
```

→ Bloquear la conexión y triar el equipo. **No bloquear estos dominios de forma general:** son servicios legítimos de uso cotidiano y la señal está en el proceso que los solicita, no en el destino.

**D-9 · MEDIO — Egreso a DNS dinámico gratuito desde estación de trabajo**

```
host.role == "workstation"
AND dns.question.name MATCHES "(?i)\.(duckdns\.org|noip\.com|con-ip\.com|ip-ddns\.com|ddns-ip\.net|ydns\.eu|longmusic\.com)$"
```

→ Bloqueo por política (decisión E-d) y alerta. Detectar sin bloquear aporta poco aquí: el valor está en cerrar el canal.

**D-10 · MEDIO — Señal de fichero `.url` abierto**

```
http.user_agent MATCHES "^Microsoft-WebDAV-MiniRedir/"
AND destination.ip NOT IN (<rangos internos y de socios aprobados>)
AND destination.port IN (80, 443)
```

→ Investigar el equipo y buscar el fichero `.url` de origen en el correo. Es la huella de la técnica de noviembre de 2024, que el actor siguió usando después del parche.

**D-11 · MEDIO — Acceso no autorizado a datos de perfil de navegador**

```
file.path MATCHES "(?i)\\\\(User Data|Profile [0-9]+)\\\\(Login Data|Cookies|Local State)$"
AND process.name NOT IN ("chrome.exe","msedge.exe","brave.exe","firefox.exe", <navegadores aprobados>)
```

→ Aislar el equipo y forzar rotación de credenciales del usuario. Cubre la capacidad de robo con evasión del cifrado vinculado a aplicación observada en 2026.

**D-12 · MEDIO — Adjunto de tipo sin uso legítimo entrante**

```
email.direction == "inbound"
AND email.attachment.extension IN ("url","svg","xhtml","js","vbs","vbe","bat","cmd","lha","uue")
```

→ Cuarentena. Ampliar a los archivos comprimidos protegidos con contraseña, que el actor usa para eludir el análisis de la pasarela. Medir primero el volumen de 90 días para conocer el impacto antes de activar el bloqueo.

<!-- cti:note type="warn" -->

> ⚠ **Regla de operación.** Las detecciones D-1 a D-4 deben ejecutar **contención
> automática**, con una salvedad importante respecto al informe anterior de esta serie:
> aquí la urgencia no viene de la velocidad del adversario —no hay cifras públicas que
> sugieran una cadena de minutos— sino de **lo que ocurre después del primer éxito**, que
> es robo de credenciales de navegador y de correo. Una vez salen las credenciales, el
> incidente deja de ser de endpoint y pasa a ser de identidad, y eso cuesta un orden de
> magnitud más. El criterio de reversión y el responsable nominal del impacto operativo de
> un falso positivo deben estar designados antes de activar las reglas.

<!-- cti:note type="gap" -->

> ⬛ **Estado de este material.** Las doce reglas son **plantillas en pseudocódigo, no
> reglas probadas**, y los nombres de campo deben traducirse al esquema real de nuestro
> SIEM y de nuestro EDR. D-1 exige calibración obligatoria con línea base previa: activarla
> en frío generará ruido suficiente para que el equipo la desactive, que es el peor
> resultado posible.

## X-4. Consultas de caza

```kql
// H-1 · Intérprete de script creando intérprete de comandos
// Ejecutar primero sobre 30 días para establecer la línea base.
DeviceProcessEvents
| where Timestamp > ago(30d)
| where InitiatingProcessFileName in~ ("wscript.exe", "cscript.exe")
| where FileName in~ ("powershell.exe", "pwsh.exe", "cmd.exe", "mshta.exe")
| project Timestamp, DeviceName, AccountName,
          InitiatingProcessFolderPath, InitiatingProcessCommandLine,
          FileName, ProcessCommandLine
| order by Timestamp desc
```

```kql
// H-2 · Utilidad .NET del sistema abriendo conexiones de red
let utilidades = dynamic(["regsvcs.exe","msbuild.exe","installutil.exe",
                          "jsc.exe","applaunch.exe","csc.exe"]);
DeviceNetworkEvents
| where Timestamp > ago(30d)
| where InitiatingProcessFileName has_any (utilidades)
| summarize Conexiones = count(),
            Destinos = make_set(RemoteUrl, 15),
            IPs = make_set(RemoteIP, 15)
        by DeviceName, InitiatingProcessFileName,
           InitiatingProcessParentFileName, bin(Timestamp, 1h)
| order by Conexiones desc
```

```kql
// H-5 · Persistencia: tareas que ejecutan scripts desde rutas de usuario
DeviceRegistryEvents
| where Timestamp > ago(30d)
| where RegistryKey has @"\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache"
| where RegistryValueData has_any ("wscript", "cscript", "powershell")
      and RegistryValueData has_any ("TEMP", "AppData", "ProgramData", "PhotoStudio")
| project Timestamp, DeviceName, RegistryKey, RegistryValueName, RegistryValueData
```

```kql
// H-6 · Descarga de carga por proceso que no es navegador
let almacenes = dynamic(["raw.githubusercontent.com","bitbucket.org",
                         "cdn.discordapp.com","archive.org","paste.ee",
                         "textbin.net","gofile.io","drive.usercontent.google.com"]);
let sospechosos = dynamic(["powershell.exe","wscript.exe","cscript.exe",
                           "mshta.exe","certutil.exe","curl.exe"]);
DeviceNetworkEvents
| where Timestamp > ago(30d)
| where RemoteUrl has_any (almacenes)
| where InitiatingProcessFileName has_any (sospechosos)
| project Timestamp, DeviceName, AccountName, InitiatingProcessFileName,
          InitiatingProcessCommandLine, RemoteUrl
| order by Timestamp desc
```

```kql
// H-11 + H-13 · Correo: adjuntos sin uso legítimo y señuelo judicial localizado
let extensiones = dynamic(["url","svg","xhtml","js","vbs","vbe","bat","cmd","lha","uue"]);
let terminos_cl = dynamic(["poder judicial","oficina judicial virtual","estado diario",
                           "causa rit","causa ruc","ministerio publico","fiscalia",
                           "impuestos internos","tesoreria general","direccion del trabajo",
                           "demanda laboral","notificacion judicial","tutela"]);
EmailAttachmentInfo
| where Timestamp > ago(90d)
| where FileType in~ (extensiones)
| join kind=inner (
    EmailEvents
    | where EmailDirection == "Inbound"
    | project NetworkMessageId, Subject, SenderFromDomain, RecipientEmailAddress
  ) on NetworkMessageId
| extend SenuelLocalizado = Subject has_any (terminos_cl)
| project Timestamp, SenderFromDomain, RecipientEmailAddress, Subject,
          FileName, FileType, SenuelLocalizado
| order by SenuelLocalizado desc, Timestamp desc
```

```kql
// H-12 · Correo intra-tenant con señuelo oficial hacia buzones funcionales
// La pasarela perimetral no ve este tráfico: hay que consultarlo en la plataforma.
let terminos = dynamic(["judicial","juzgado","fiscalia","demanda","notificacion",
                        "citacion","audiencia","tutela","requerimiento","impuestos"]);
EmailEvents
| where Timestamp > ago(90d)
| where EmailDirection == "Intra-org"
| where Subject has_any (terminos)
| project Timestamp, SenderFromAddress, RecipientEmailAddress, Subject,
          AttachmentCount, UrlCount
| order by Timestamp desc
```

```yaml
# Sigma — Intérprete de script creando intérprete de comandos (Blind Eagle, cadena estable desde 2019)
# Autor: Célula CTI · Fecha: 2026-11-16 · ATT&CK: T1059.005, T1059.001, T1059.007
# Nivel: high · Estado: experimental (requiere línea base previa de 30 días)
# Falsos positivos conocidos: scripts de inicio de sesión corporativos,
# herramientas de inventario antiguas, instaladores empaquetados.
title: Script host lanzando interprete de comandos
id: 4c7e1a93-BE36-CTI-2026-020
status: experimental
logsource:
  category: process_creation
  product: windows
detection:
  padre:
    ParentImage|endswith:
      - '\wscript.exe'
      - '\cscript.exe'
  hijo:
    Image|endswith:
      - '\powershell.exe'
      - '\pwsh.exe'
      - '\cmd.exe'
      - '\mshta.exe'
  condition: padre and hijo
fields:
  - ParentImage
  - ParentCommandLine
  - Image
  - CommandLine
  - User
level: high
```

```yaml
# Sigma — Utilidad .NET del sistema como objetivo de vaciado de proceso
# Autor: Célula CTI · Fecha: 2026-11-16 · ATT&CK: T1055.012
# Nivel: critical · Estado: experimental
# Falsos positivos: servidores de compilacion e integracion continua,
# que deben exceptuarse por nombre de host y no por patron.
title: Utilidad .NET de Windows creada en estado suspendido desde script
id: 8f2b4d61-BE36-CTI-2026-020
status: experimental
logsource:
  category: process_creation
  product: windows
detection:
  objetivo:
    Image|endswith:
      - '\RegSvcs.exe'
      - '\MSBuild.exe'
      - '\InstallUtil.exe'
      - '\jsc.exe'
      - '\AppLaunch.exe'
      - '\csc.exe'
  padre_sospechoso:
    ParentImage|endswith:
      - '\wscript.exe'
      - '\cscript.exe'
      - '\powershell.exe'
      - '\pwsh.exe'
      - '\AutoIt3.exe'
  condition: objetivo and padre_sospechoso
fields:
  - ParentImage
  - ParentCommandLine
  - Image
  - CommandLine
level: critical
```

## X-5. Mitigaciones de configuración con efecto directo

| Control | Corta |
|---|---|
| Restricción de `wscript.exe` y `cscript.exe` por directiva en estaciones de trabajo | El primer eslabón de **todas** las campañas documentadas del actor desde 2019 (`T1059.005`) |
| Bloqueo de adjuntos `.url`, `.svg`, `.xhtml`, `.js`, `.vbs`, `.bat`, `.lha`, `.uue` y de archivos comprimidos con contraseña | La etapa 01 completa en su variante de adjunto (`T1566.001`) |
| Inspección de adjuntos y reescritura de enlaces en el correo **intra-tenant**, incluidos buzones compartidos | El vector de remitente institucional comprometido (`T1534`, `T1586.002`), que hoy no pasa por ningún control |
| Autenticación multifactor y acceso condicional en buzones compartidos y funcionales | La precondición del vector anterior: el compromiso de la cuenta que luego sirve de remitente |
| Denegación por defecto del egreso a sufijos de DNS dinámico gratuito desde estaciones | El canal de mando y control que el actor ha usado durante ocho años (`T1568`) |
| Protección contra manipulación de Defender activada y gestionada centralmente | La exclusión de volumen completo y la desactivación del antivirus (`T1562.001`) |
| Reglas de reducción de superficie de ataque que bloqueen la creación de procesos hijo por parte de scripts y de Office | La transición de la etapa 01 a la etapa 02 |
| Registro de línea de comandos y de creación de procesos habilitado con 90 días de retención | No corta nada: **habilita** D-1, D-6, D-7 y las hipótesis `H-1`, `H-8`, `H-9` |
| Eliminación de `AutoIt3.exe` de la flota, o control por lista de permitidos de aplicaciones | La cadena de 2026 basada en el intérprete legítimo con script remoto |
| Lista de permitidos de aplicaciones para intérpretes y utilidades .NET del sistema | La etapa 02 completa, incluida la variante que aún no conocemos |
| Procedimiento de verificación de notificaciones oficiales por canal independiente | La etapa 01 en su raíz, y es el único control que resiste la localización del señuelo a Chile |

---

## 14. Brechas de inteligencia y nuevos requisitos de colección

| # | Brecha | Impacto en el juicio | Requisito propuesto | Prioridad |
|---|---|---|---|---|
| G-1 | La alerta `AL-20260925-119` del ColCERT es TLP:AMBER y no se ha incorporado | El análisis más reciente y específico del actor queda fuera del producto. Puede contener indicadores vivos que no tenemos | Solicitar acceso al ColCERT por el canal entre equipos de respuesta, y si se obtiene, emitir anexo de circulación restringida separado de este informe | Crítica |
| G-2 | Sin visibilidad sobre actividad de este actor contra Chile | KJ-4 queda en confianza baja; no podemos afirmar ni descartar exposición nacional | Consulta al CSIRT Nacional; participación en el canal sectorial de intercambio; vigilancia activa del indicador `I-1` | Crítica |
| G-3 | Sin telemetría propia de ningún tipo | §O-4 vacía; las doce reglas de §X-3 sin calibrar | Ejecutar el cuestionario X-1 a X-10 de §O-4 y emitir la versión 1.1 | Crítica |
| G-4 | La campaña en curso de oct-nov 2026 solo se conoce por fuentes secundarias | El alcance a Chile, la cifra de 3.300 correos y la familia del implante final no están verificados | Vigilar la publicación del informe original de Trustwave; si no aparece en 60 días, rebajar esas afirmaciones a «no confirmado» en la versión siguiente | Alta |
| G-5 | El informe de Insikt sobre los cinco clústeres no se pudo leer en original | La estructura interna del actor se describe de oído; no sabemos qué TTP corresponde a qué clúster | Obtener el PDF con extracción de texto fiable o acceso al portal del proveedor | Alta |
| G-6 | Sin inventario de buzones compartidos y funcionales ni de sus controles | La decisión E-b no se puede ejecutar ni medir | Extracción desde la plataforma de identidad con responsable y controles por buzón | Alta |
| G-7 | Sin línea base de ejecución de scripts en la flota | D-1 no se puede activar sin generar ruido; `H-1` no es interpretable | Campaña de 30 días de recolección y caracterización | Alta |
| G-8 | Sin lista oficial y mantenida de dominios legítimos de instituciones chilenas que notifican por correo | La decisión E-c no se puede comunicar con precisión y `H-13` produce falsos positivos evitables | Elaboración conjunta con Asuntos Corporativos y Legal | Media |
| G-9 | Discrepancias en los datos de origen sin resolver (§3.3) | Dos cifras de infecciones, dos de registros filtrados y dos versiones del agente de usuario WebDAV | Consulta a los proveedores o verificación contra una segunda fuente antes de citar esas cifras fuera de este informe | Media |
| G-10 | Sin seguimiento del ecosistema brasileño de crimeware, del que el actor parece estar comprando capacidad | KJ-5 y H4 no son accionables: sabemos que la convergencia ocurre pero no vigilamos su catálogo | Añadir `Caminho`, `VMDetectLoader`, `Vbs-Crypter` y «Crypters and Tools» al plan de colección permanente | Media |

---

# ANEXOS

## Anexo A — Indicadores de compromiso

<!-- cti:note type="warn" -->

> ⚠ **Leer antes de usar, y aquí con más motivo que de costumbre.** Contra este actor los
> indicadores atómicos son **excepcionalmente perecederos**: SpiderLabs constata que los
> hashes «caducan en el momento en que una muestra se ejecuta una vez», porque el dropper
> regenera su clave de cifrado y sus identificadores en cada arranque. Los dominios viven
> en servicios de DNS dinámico gratuito y rotan en días. **Esta lista sirve para búsqueda
> retrospectiva y para reconocer al actor dentro de un incidente; no sirve como estrategia
> de prevención.** Lo que sí funciona está en §T-4 y §X-3. Además, buena parte de la
> infraestructura son servicios legítimos de terceros —GitHub, Discord, Internet Archive,
> Bitbucket, acortadores— que **no deben bloquearse**: la señal está en el proceso que los
> solicita, no en el destino.

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Acción permitida |
|---|---|---|---|---|
| ipv4 | `62.60.226[.]64` | Servidor de etapa 2, descarga por WebDAV tras pulsar el fichero `.url` (Check Point, dic-2024/feb-2025) | Alta | Bloqueo y retrohunt |
| ipv4 | `62.60.226[.]112` | Mismo rango, servidor de descarga observado en red de cliente (Darktrace, feb-2025) | Alta | Bloqueo y retrohunt |
| ipv4 | `177.255.85[.]101` | Resuelve C2 de `.NET RAT` y de Remcos; el proveedor indica uso reiterado para múltiples C2 de Remcos | Alta | Bloqueo y retrohunt |
| ipv4 | `181.131.217.244` | Resuelve `newstaticfreepoint24.ddns-ip[.]net` y `17dic.ydns[.]eu` | Alta | Bloqueo y retrohunt |
| ipv4 | `45.135.232[.]38` | Infraestructura de entrega por Visual Basic en Proton66; bloque asociado a ese proveedor a prueba de balas (SpiderLabs, jun-2025) | Alta | Bloqueo |
| ipv4 | `46.246.84[.]5` | Servidor con directorio abierto, droppers `envifa.vbs` y `sostener2.vbs`; históricamente resolvió C2 de AsyncRAT desde mar-2023 (SpiderLabs, jul-2026) | Alta | Bloqueo y retrohunt |
| ipv4 | `181.235.8[.]24` | Servidor con directorio abierto, droppers `31agosto.vbs`, `31diciembre.vbs`, `andre.vbs`, `sostener.vbs` | Alta | Bloqueo y retrohunt |
| ipv4 | `178.16.52[.]80` | Servidor con directorio abierto, dropper de tres lenguajes `hold.bat`/`hold.vbs`/`hold.js` | Alta | Bloqueo y retrohunt |
| ipv4 | `64.89.160[.]17` | Servidor con directorio abierto, `System3.vbs` y `System5.vbs`, cadena con AutoIt | Alta | Bloqueo y retrohunt |
| ipv4 | `45.74.34[.]32` · `45.133.180[.]138` · `45.133.180[.]154` · `45.153.34[.]67` · `46.246.6[.]9` · `74.124.24[.]240` · `83.147.37[.]31` · `103.20.102[.]130` · `103.20.102[.]151` · `103.186.108[.]212` · `103.236.70[.]158` · `104.194.154[.]39` · `146.70.49[.]42` · `146.70.215[.]50` · `178.16.54[.]45` · `179.13.4[.]196` · `179.13.11[.]235` · `181.131.217[.]135` · `181.206.158[.]190` · `181.235.3[.]119` · `185.18.222[.]5` · `191.91.178[.]101` · `191.93.118[.]254` · `203.104.42[.]92` | Equipos que comparten el emisor del certificado de DCRAT. **El propio proveedor advierte que solo un subconjunto es probablemente de este actor** (Zscaler, dic-2025) | Baja | Solo retrohunt |
| domain | `republicadominica2025[.]ip-ddns[.]com` | C2 del descargador .NET, campaña `socialismo` (ene-2025) | Alta | Bloqueo |
| domain | `elyeso.ip-ddns[.]com` | C2 de Remcos, puerto 30204 | Alta | Bloqueo |
| domain | `21ene.ip-ddns[.]com` | C2 de Remcos (feb-2025); confirmado también en red de cliente con unos 60 MiB exfiltrados (Darktrace) | Alta | Bloqueo |
| domain | `newstaticfreepoint24.ddns-ip[.]net` | C2 de las campañas `marte`, `saturno`, `PARAISO` y `PARAISO2` (dic-2024) | Alta | Bloqueo |
| domain | `17dic.ydns[.]eu` | C2 secundario de la campaña `PARAISO2` | Alta | Bloqueo |
| domain | `amuntgroupfree.ip-ddns[.]com` | C2 de Remcos | Alta | Bloqueo |
| domain | `donato.con-ip[.]com` | C2 de Remcos | Alta | Bloqueo |
| domain | `comina998.ddns-ip[.]net` | C2 de Remcos | Alta | Bloqueo |
| domain | `diciembrenotasenclub[.]longmusic[.]com` | C2 observado en puerto 1512, no estándar (Darktrace, feb-2025) | Alta | Bloqueo |
| domain | `rema200426[.]duckdns[.]org` | C2 de la compilación `JC-46` de AsyncRAT; el patrón de registro en DuckDNS sugiere uso desde abr-2020 (SpiderLabs, jul-2026) | Alta | Bloqueo |
| domain | `startmenuexperiencehost[.]ydns[.]eu` | C2 de DCRAT; resuelve a direcciones suecas en el AS 42708 (Zscaler, dic-2025) | Alta | Bloqueo |
| domain | `servicioseguroenlineabb[.]com` | Dominio de phishing que suplanta banca colombiana (mar-2024) | Alta | Bloqueo |
| domain | `cort[.]as` · `acortaurl[.]com` · `gtly[.]to` | Acortadores con filtrado por geolocalización usados en la entrega. **Servicios legítimos de terceros** | Media | Solo retrohunt y correlación |
| url | `hxxp://62.60.226[.]64/file/4025_3980.exe` | Etapa 2 referenciada desde el fichero `.url` | Alta | Bloqueo |
| url | `hxxp://62.60.226[.]112/file/3601_2042.exe` | Etapa 2 observada en red de cliente | Alta | Bloqueo |
| url | `hxxps://raw.githubusercontent[.]com/Oscarito20222/file/refs/heads/main/redtube.exe` | Remcos alojado en GitHub (feb-2025) | Alta | Detección; no bloquear el dominio |
| url | `hxxps://raw.githubusercontent[.]com/cabeto850128/comicsam` | Repositorio de etapa intermedia (jul-2026) | Alta | Detección; no bloquear el dominio |
| url | `hxxps://bitbucket[.]org/facturacioncol/fact/downloads/FileHosting.exe` | Carga de la campaña `marte` | Alta | Detección; no bloquear el dominio |
| url | `hxxps://bitbucket[.]org/trabajo12023/proyecto/downloads/ROSAS.exe` | Carga de la campaña `PARAISO` | Alta | Detección; no bloquear el dominio |
| url | `hxxps://archive[.]org/download/optimized_msi_20250821/optimized_MSI.png` | PNG con el cargador `Caminho` oculto por esteganografía entre los marcadores `BaseStart-` y `-BaseEnd` | Alta | Detección; no bloquear el dominio |
| url | `hxxps://paste[.]ee/r/jNJfecjT/0` | Etapa intermedia en servicio de pegado de texto (jun-2025) | Media | Detección |
| url | `hxxps://textbin[.]net/raw/xsi2eulwpw` | Etapa intermedia en servicio de pegado de texto (jun-2025) | Media | Detección |
| sha1 | `1d1e007a9d8939bee7a0333522cc4f7480d448cc` | Fichero `.url` de etapa 1 con señuelo judicial | Alta | Bloqueo y retrohunt |
| sha1 | `133bc4304057317b0b93f5ff44f20d153b985b50` | Fichero `.url` de etapa 1 | Alta | Bloqueo y retrohunt |
| sha1 | `1fcc44d3b20381acce66f5634743917e8f22dae7` | Fichero `.url` de etapa 1 | Alta | Bloqueo y retrohunt |
| sha1 | `a0338654304b6f824bdc39bbb482a0e114f8a3a1` | Fichero `.url` de etapa 1 | Alta | Bloqueo y retrohunt |
| sha1 | `07647f0eddf46d19e0864624b22236b2cdf561a1` | Etapa 2 empaquetada con `HeartCrypt` | Alta | Bloqueo y retrohunt |
| sha1 | `08daf84d9c2e9c51f64e076e7611601c29f68e90` | Etapa 2 empaquetada con `HeartCrypt` | Alta | Bloqueo y retrohunt |
| sha1 | `83c851f265f6d7dc9436890009822f0c2d4ba50a` | Etapa 2 empaquetada con `HeartCrypt` | Alta | Bloqueo y retrohunt |
| sha1 | `33ddaedc98991435f740f7a5a8a931a8cadd5391` | Etapa 2 empaquetada con `HeartCrypt` | Alta | Bloqueo y retrohunt |
| sha1 | `758c73ab9706ae6977f9b4601c20b3667836d3ef` | `redtube.exe` — Remcos de etapa 3, nombre de botnet `redtube` | Alta | Bloqueo y retrohunt |
| sha1 | `3bd90557615ef95e4244bdbaa8e0e7fd949cdd3a` | `fuck.exe` alojado en el repositorio del actor | Alta | Bloqueo y retrohunt |
| sha1 | `ba95ea1dcc744566a9552d9665feff035925a5c5` | `roma.exe` alojado en el repositorio del actor | Alta | Bloqueo y retrohunt |
| sha1 | `3d3248ad14dce8b6fcf416d56d8de52b07b549e7` | `normales.exe` alojado en el repositorio del actor | Alta | Bloqueo y retrohunt |
| sha1 | `abf71fd332b760da29aa211f4aaa1661860a98c6` | `sena.exe` alojado en el repositorio del actor | Alta | Bloqueo y retrohunt |
| sha1 | `44182ce5a8fadef41064d7c0266e8f99015262b0` | `TobaccoAnnouncement.exe` alojado en el repositorio del actor | Alta | Bloqueo y retrohunt |
| sha1 | `4e3cb251fb98a47c2f5dec5f3722723990c17a49` | `2112-2.7z`, archivo de 2022 en el repositorio del actor | Media | Retrohunt |
| sha1 | `e0837aebd649dba01bc4d594ef21a8086edaaeeb` | `Ver Datos del Formulario.html` — **el fichero con los datos personales que el propio actor filtró por error** | Alta | Retrohunt; no es código malicioso |
| sha256 | `a4fbd707f4ce7ca68e6137cef1c56b6f408e5f0a0f148434d996bb98c3a21fff` | `Paralell.dll` — inyector .NET del proyecto `JC-46`, protegido con `CryptoObfuscator` | Alta | Bloqueo y retrohunt |
| sha256 | `a73cb9d5d46e19f3daa4a14cfe5d8fa4319a3d62452039e4972e6a316bbb26f4` | `Client1.exe` — compilación `JC-46` de AsyncRAT | Alta | Bloqueo y retrohunt |
| sha256 | `8f3dc1649150961e2bac40d8dabe5be160306bcaaa69ebe040d8d6e634987829` | Adjunto `.svg` con HTML en base64 embebido, campaña contra agencia del Ministerio de Comercio de Colombia | Alta | Bloqueo y retrohunt |
| sha256 | `03548c9fad49820c52ff497f90232f68e044958027f330c2c51c80f545944fc1` | Portal judicial falso que descarga el `.js` | Alta | Bloqueo y retrohunt |
| sha256 | `d0fe6555bc72a7a45a836ea137850e6e687998eb1c4465b8ad1fb6119ff882ab` | Fichero JavaScript de etapa 1, con nombre de señuelo judicial largo | Alta | Bloqueo y retrohunt |
| sha256 | `08a5d0d8ec398acc707bb26cb3d8ee2187f8c33a3cbdee641262cfc3aed1e91d` | `optimized_MSI.png` — PNG portador del cargador por esteganografía | Alta | Bloqueo y retrohunt |
| sha256 | `c208d8d0493c60f14172acb4549dcb394d2b92d30bcae4880e66df3c3a7100e4` | Instancia del cargador `Caminho` | Alta | Bloqueo y retrohunt |
| sha256 | `d139bfe642f3080b461677f55768fac1ae1344e529a57732cc740b23e104bff0` | `AGT27.txt` — DCRAT en base64 invertido servido desde Discord CDN | Alta | Bloqueo y retrohunt |
| sha256 | `e7666af17732e9a3954f6308bc52866b937ac67099faa212518d5592baca5d44` | Instancia de DCRAT inyectada en `MSBuild.exe` | Alta | Bloqueo y retrohunt |
| md5 | `18eb0a413b80a548d2b615e11fc580cd` | Muestra de las campañas de espionaje de may-jun 2024 (Kaspersky) | Media | Retrohunt |
| md5 | `53231da42b6f19d2a6b59700f822be6a` | Muestra de las campañas de espionaje de may-jun 2024 (Kaspersky) | Media | Retrohunt |
| md5 | `69d218a3cd86a194d8fbc22c487096bc` | Muestra de las campañas de espionaje de may-jun 2024 (Kaspersky) | Media | Retrohunt |
| md5 | `7b72f2775b7bf33c9778533480d34e04` | Muestra de las campañas de espionaje de may-jun 2024 (Kaspersky) | Media | Retrohunt |
| useragent | `Microsoft-WebDAV-MiniRedir/10.0.19044` | Petición WebDAV disparada por el fichero `.url`. **Agente legítimo de Windows**: la señal es el destino externo por puerto 80, no la cadena | Media | Detección por contexto |
| useragent | `Microsoft-WebDAV-MiniRedir/10.0.19045` | Igual que el anterior, versión observada por Darktrace. La discrepancia entre ambas está consignada en §3.3 | Media | Detección por contexto |
| filename | `PhotoStudio.vbs` | Script de persistencia de la tarea `Photo Studio` (jul-2026) | Alta | Detección y caza |
| filename | `envifa.vbs` · `sostener.vbs` · `sostener2.vbs` · `31agosto.vbs` · `31diciembre.vbs` · `andre.vbs` · `hold.bat` · `hold.vbs` · `hold.js` · `System3.vbs` · `System5.vbs` | Droppers de Visual Basic alojados en los cuatro servidores con directorio abierto de 2026 | Alta | Detección y caza |
| filename | `kiSBJ4DDvg.pif` · `XjvdJar2Kf.pif` | `AutoIt3.exe` legítimo renombrado, sin script compilado incrustado | Alta | Detección y caza |
| filename | `AGT27.txt` · `optimized_MSI.png` | Portadores de carga de la cadena de dic-2025 | Media | Detección |
| filepath | `%LOCALAPPDATA%\PhotoStudioVBS\` | Carpeta de persistencia, compartida por tres cadenas distintas del actor | Alta | Detección y caza |
| filepath | `C:\Users\UserPC\source\repos\JC-46\JC-46\Paralell\Paralell\bin\Debug\CryptoObfuscator_Output\Paralell.pdb` | Ruta de compilación incrustada en el inyector; identifica el proyecto interno `JC-46` | Alta | Caza por cadena en binarios |
| mutex | `mono1234` | Mutex del descargador .NET, usado también como contraseña de derivación de la clave AES | Alta | Detección y caza |
| artefacto | Tarea programada `Photo Studio` · etiqueta `PhotoStudioVBS` · exportado `VAI` en `ClassLibrary1.Home` · marcadores `BaseStart-` y `-BaseEnd` · decodificador `Wales()` · prefijo `zv` en identificadores · clases `CoutureFlow`, `StyleInjection`, `RunwayWalk` · clave AES `aPZ0ze9qOhazFFqspYVRZ8BW14nGuRUe` · cadenas `SponsorshipTimeout` y `NextActivator` | **Los artefactos de mayor vida útil de este informe.** Véase §T-3 | Alta | Detección y caza |
| artefacto | Nombres de campaña `socialismo` · `miami` · `PARAISO` · `PARAISO2` · `marte` · `saturno` · nombre de botnet `redtube` | Identificadores de campaña en la configuración de los implantes | Alta | Caza en configuración de muestras |
| puerto | `4050` · `1512` · `4782` · `6001` · `30201` · `30204` | Puertos no estándar observados en C2. **Detectar por combinación con dominio de DNS dinámico**, no por puerto suelto | Media | Detección por contexto |

*Nota de higiene.* Están marcados como servicio legítimo y **no deben bloquearse por dominio**: `raw.githubusercontent.com`, `bitbucket.org`, `cdn.discordapp.com`, `archive.org`, `paste.ee`, `textbin.net`, `gofile.io`, `drive.usercontent.google.com`, los tres acortadores y los dos agentes de usuario de WebDAV, que son componentes propios de Windows. Las 24 direcciones del clúster de certificado se entregan con confianza baja por indicación expresa del proveedor, que advierte que solo un subconjunto corresponde a este actor. Y la totalidad de los hashes debe tratarse como material de retrohunt: contra un dropper que se automuta en cada ejecución, su valor preventivo es nulo.

## Anexo B — Fuentes y valoración

> Valoración doble tipo Admiralty/OTAN: **fiabilidad de la fuente (A–F)** ×
> **credibilidad de la información (1–6)**. Se valoran por separado.

| Fuente | Disciplina | Fiabilidad | Credibilidad | Notas de sesgo |
|---|---|---|---|---|
| MITRE ATT&CK, ficha `G0099`, versión 2.0, 31-jul-2026 | Marco de referencia / OSINT | A | 1 | Sin interés comercial. Es una síntesis de fuentes de terceros, que cita; su valor está en la normalización, no en la observación primaria. Una de sus entradas (`T1683.002`) tiene una descripción que no encaja con el nombre de la subtécnica |
| Check Point Research, «Blind Eagle: …And Justice for All», 10-mar-2025 | OSINT comercial / TECHINT | B | 1 | **La fuente técnica más detallada disponible.** Observación de primera mano con reproducción de configuraciones, nombres de campaña y metadatos de repositorio. Inconsistencias internas consignadas en §3.3: dos cifras de infectados y dos de registros filtrados. Matiza en el cuerpo lo que afirma con más firmeza en el resumen |
| Kaspersky GReAT, «BlindEagle flying high in Latin America», 19-ago-2024 | OSINT comercial / TECHINT | B | 1 | Única fuente con reparto cuantificado de víctimas por país, y la que nombra a Chile como objetivo. Acota el 87 % a dos meses concretos, lo que es buena práctica. Publica solo cuatro hashes y ningún indicador de red. Es de 2024: su descripción del arsenal está superada |
| LevelBlue / Trustwave SpiderLabs, «Still Circling: Blind Eagle's Toolkit Keeps Evolving», 17-jul-2026 | OSINT comercial / TECHINT | B | 1 | **La fuente más reciente de primera mano.** Análisis profundo del utillaje actual con indicadores de red y de host. Declara sus límites con honestidad poco común, incluido que una rutina de persistencia no se observó ejecutarse. No nombra a Chile |
| LevelBlue / Trustwave SpiderLabs, «Tracing Blind Eagle to Proton66», 27-jun-2025 | OSINT comercial / TECHINT | B | 2 | Vínculo con el alojamiento a prueba de balas declarado con alta confianza. Su tabla de indicadores se publica **como imagen**, de modo que no se pudo transcribir: los indicadores de esa fuente que figuran en el Anexo A proceden solo de su texto corrido |
| Zscaler ThreatLabz, «BlindEagle Targets Colombian Government Agency with Caminho and DCRAT», 16-dic-2025 | OSINT comercial / TECHINT | B | 1 | Cadena de ataque completa de extremo a extremo, con el conjunto de indicadores más limpio del informe. Atribución declarada con **confianza media**, no alta. Advierte expresamente que solo un subconjunto de las 24 direcciones es de este actor. Inconsistencia sobre el estatus comercial de `Caminho` consignada en §3.3 |
| Darktrace, «Patch and Persist», 25-jun-2025 | OSINT comercial / TECHINT | B | 2 | Única fuente con un caso observado en red de cliente y con duración publicada. Atribución declarada con **confianza media**. Dos defectos consignados: publica dos versiones del mismo agente de usuario, y su tabla ATT&CK mezcla identificadores del dominio industrial sin justificación, que este informe ha descartado |
| Recorded Future / Insikt Group, «TAG-144's Persistent Grip on South American Organizations», 26-ago-2025 | OSINT comercial | B | 3 | **No se pudo leer en original.** El PDF está publicado pero su codificación tipográfica impidió la extracción de texto. Todo lo que este informe dice de él proviene de resúmenes de terceros, de ahí la credibilidad 3. Es la única fuente sobre la estructura en cinco clústeres, lo que convierte su inaccesibilidad en la brecha `G-5` |
| Prensa técnica sobre la campaña de oct-nov 2026, atribuida a investigación de Trustwave y a un recuento de Zenox | OSINT comercial derivado | C | 3 | **Fuente secundaria sin acceso a los originales.** Es la única que sitúa a Chile entre los países principales y la única que aporta la cifra de 3.300 correos. Ninguna de las dos afirmaciones tiene corroboración independiente. Tratar como no confirmado y vigilar la publicación del informe original (`G-4`) |
| ColCERT, alerta `AL-20260925-119`, 25-sep-2026 | OSINT gubernamental | A | — | **Marcada TLP:AMBER. Citada por su existencia, no por su contenido.** Su credibilidad no se valora porque no se ha incorporado ningún dato suyo. Véase la nota de §0 y la brecha `G-1` |
| Comprobación propia de ausencia de caso chileno documentado y de alerta del CSIRT Nacional, 16-nov-2026 | Análisis propio / OSINT | B | 3 | **Hallazgo negativo:** la ausencia en fuentes abiertas no prueba la ausencia de actividad. Consignado como brecha `G-2`, no como conclusión. Es la base de que KJ-4 se formule con confianza baja |

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

## Anexo D — Herramientas atribuidas al grupo en MITRE ATT&CK

| ID | Herramienta | Naturaleza |
|---|---|---|
| `S1087` | AsyncRAT | Troyano de código abierto, versión personalizada |
| `S9016` | Caminho | Cargador como servicio, también conocido como `VMDetectLoader` |
| `S9017` | DCRAT | Troyano de código abierto en C#, variante de la familia de AsyncRAT |
| `S9018` | HeartCrypt | Empaquetador como servicio, usado en cadenas de Remcos |
| `S0434` | Imminent Monitor | Troyano comercial, variante modificada |
| `S0385` | njRAT | Troyano de código abierto, versión personalizada |
| `S9019` | PureCrypter | Cargador y criptador |
| `S0262` | QuasarRAT | Troyano de código abierto, personalizado como troyano bancario (`BlotchyQuasar`) |
| `S0332` | Remcos | Troyano comercial de acceso remoto |

> Las nueve son herramientas de terceros. **El grupo no tiene una sola familia propia
> atribuida en ocho años**, y esa es la observación central de §O-3.

## Anexo E — Marcos de referencia empleados

`MITRE ATT&CK v18` (ficha `G0099` v2.0) · `MITRE D3FEND` · `Cyber Kill Chain` ·
`Pirámide del Dolor` · `Modelo del Diamante` · `F3EAD` · `ICD 203` (lenguaje
estimativo) · `ACH, supuestos clave, pre-mortem` · `TLP 2.0` · `PAP` ·
`STIX 2.1 / TAXII 2.1` · `Admiralty Code`

## Anexo F — Paquete legible por máquina

- Bundle STIX 2.1: pendiente de generar. Debe incluir `intrusion-set` (uno solo, con los cinco alias equivalentes como `aliases`, y **sin** fusionar `Hive0131`), `malware` y `tool` (las nueve entradas del Anexo D), `attack-pattern` (las técnicas de §T-2), `indicator` (Anexo A, con `valid_until` y marcado explícito de servicio legítimo) y relaciones `uses`.
- Evento MISP: pendiente. Taxonomías a aplicar: `tlp`, `pap`, `admiralty-scale`, `estimative-language`, y etiqueta propia `actor-regional-hispanohablante`.
- Reglas: las dos reglas Sigma de §X-4 y las doce plantillas de detección de §X-3, versionadas con el identificador `CTI-2026-020` y estado `experimental` hasta su calibración.
- Capa de ATT&CK Navigator: pendiente, a partir de §T-2, **sin** las técnicas del dominio industrial descartadas.

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-11-16 | Emisión inicial. Elaborado sobre seis informes de proveedor de primera mano y la ficha `G0099` v2.0 de MITRE. La alerta TLP:AMBER del ColCERT se cita por su existencia y no se incorpora. Sin telemetría propia: §O-4 sin evaluar | Célula CTI |

## Anexo H — Realimentación del consumidor

| Pregunta | Respuesta |
|---|---|
| ¿Respondió a su requisito? | |
| ¿Qué decisión tomó o cambió con este informe? | |
| ¿Se ejecutó la prueba de detección de la decisión E-a? ¿Con qué resultado? | |
| ¿Se obtuvo acceso a la alerta del ColCERT (E-f)? | |
| ¿Apareció algún señuelo localizado a instituciones chilenas (`I-1`)? | |
| ¿Qué faltó? | |
| ¿Llegó a tiempo? | |

> Sin este anexo devuelto, el ciclo de inteligencia queda abierto y el próximo
> producto no mejora. En este caso hay además dos dependencias duras: la versión 1.1
> no se puede escribir sin las respuestas al cuestionario de §O-4, y la pregunta sobre
> el indicador `I-1` es la que decide si este producto sigue siendo un perfil o pasa a
> ser una alerta.
