---
tlp: "TLP:CLEAR"
pap: "PAP:AMBER"
id: "CTI-2026-024"
version: "1.0"
tipo: "Perfil de operación de extorsión + estudio de caso nacional"
foco_regional: "Chile (víctima documentada: Ejército de Chile) · Latinoamérica"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "Rhysida (RaaS) · afiliados y actores de acceso asociados: Vanilla Tempest · solapamientos con Vice Society / DEV-0832 e Interlock"
fecha: "2026-11-16"
caduca: "2027-02-16"
autor: "Célula CTI"
distribucion: "Elaborado íntegramente con fuentes abiertas TLP:CLEAR, incluidos un aviso conjunto del FBI, CISA y MS-ISAC y el informe de una firma chilena. Difusión libre, conservando la atribución de las fuentes y las salvedades metodológicas de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-024

## El grupo que publicó 360 000 documentos del Ejército de Chile sigue operando tres años después, y en el caso chileno hay un rasgo que ninguna otra amenaza de esta cartera tiene: una detención dentro de la organización víctima

### En febrero de 2024 su cifrado fue roto y hubo descifrador gratuito. Ya no cuenta: lo que ese episodio enseña es que un fallo criptográfico del adversario es una lotería y no un plan de recuperación

> **Regla de oro del producto:** todo párrafo debe responder a un requisito de
> inteligencia (PIR) y habilitar una decisión. Si un párrafo no cambia lo que
> alguien va a hacer, va al anexo o se borra.

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-024` |
| Versión / fecha | `1.0` — 2026-11-16 |
| Tipo de producto | Perfil de operación de extorsión más **estudio de caso nacional**. El caso del Ejército de Chile se desarrolla como tal porque es la única víctima chilena documentada de este actor y porque su gestión pública aporta lecciones que no son técnicas |
| Niveles cubiertos | Estratégico · Operacional · Táctico · Técnico |
| Foco regional | **Chile como víctima documentada** (Ejército de Chile, mayo-junio de 2023), con el conjunto de 317 víctimas publicadas como contexto |
| Marcado de difusión | `TLP:CLEAR` · `PAP:AMBER` |
| Clasificación interna | Público — apto para difusión abierta |
| Requisitos atendidos | `PIR-03` (grupos de extorsión con capacidad de impacto operacional), `PIR-04` (amenazas con foco o presencia regional), `PIR-06` (robo y publicación de información sensible), `PIR-11` (riesgo de persona interna en incidentes de extorsión) |
| Solicitante / consumidor primario | CISO · Jefatura de SOC · Respuesta a Incidentes · Continuidad de Negocio · Riesgo · Asuntos Corporativos · Recursos Humanos |
| Ventana de observación | 17 de mayo de 2023 (primera observación pública) → 2026-11-16, con detalle del caso chileno entre el 27 de mayo y el 9 de junio de 2023 |
| Base de colección | 8 fuentes. **Gubernamental:** aviso conjunto `AA23-319A` del FBI, CISA y MS-ISAC (15-nov-2023, revisado el 30-abr-2025). **Proveedor nacional:** CronUp (29-may-2023, con tres actualizaciones). **Proveedor internacional de primera mano:** IBM X-Force (12-jun-2026). **Académica:** Universidad Kookmin y KISA (feb-2024), método de descifrado. **Agregador:** ransomware.live, consultado el 16-nov-2026. **Prensa especializada:** Help Net Security (1-sep-2026) para el caso de Berlín, BleepingComputer y medios chilenos para el caso del Ejército. **Sin telemetría propia incorporada** |
| Autor (analista) | Célula CTI |
| Revisión por pares | Pendiente |
| Aprobación | Pendiente |
| Caducidad / revisión | 2027-02-16, o antes si aparece una víctima chilena nueva, si se publica el resultado judicial del caso del cabo del Ejército, o si se documenta una variante del cifrador con fallo criptográfico aprovechable |
| Productos relacionados | `CTI-2026-014` a `CTI-2026-016` (actores de extorsión: **comparten el modelo de doble extorsión y el problema de la recuperación**), `CTI-2026-019` (ARTEX — comparte la referencia a los plazos de la Ley 21.663), `CTI-2026-023` (Machete — **el informe hermano de este lote: el mismo conjunto de objetivos militares y diplomáticos, con otro fin y otro método**) |
| Paquete legible por máquina | Pendiente de generar (véase §14) |

<!-- cti:note type="warn" -->

> ⚠ **Limitación estructural de este producto.** La habitual: **no hay telemetría de la
> organización** y §O-4 queda sin rellenar. Y una específica de este informe que conviene
> leer antes que nada: **el caso chileno está documentado por prensa y por una firma
> privada, no por una investigación pública.** No hay informe oficial del Ejército, del
> CSIRT Nacional ni de la fiscalía sobre cómo se produjo la intrusión, qué se exfiltró ni
> qué contenían los documentos publicados. **Las cifras de volumen provienen del propio
> atacante**, y la implicación de una persona interna está en fase de investigación
> judicial, sin sentencia conocida. Todo lo que este informe dice del caso lleva esas
> marcas.

<!-- cti:note type="good" -->

> ✅ **Lo que distingue a este producto de los otros tres informes de extorsión de la
> cartera.** No repite el catálogo de buenas prácticas de ransomware: lo da por leído en
> `CTI-2026-014` a `CTI-2026-016`. Aporta tres cosas nuevas. **Primera:** el único caso
> chileno documentado de la serie con cronología día a día, y lo que su gestión pública
> enseña (§E-5). **Segunda:** la lección del descifrador de 2024, que es un argumento
> directo contra planificar la recuperación sobre la esperanza (§O-3). **Tercera:** la
> dimensión de persona interna, que ninguno de los otros tres informes trata y que aquí
> hay que tratar porque en el caso chileno hubo una detención (§E-5, §O-6, decisión `E-f`).

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** Rhysida sigue operando, tres años y medio después de su aparición y tras haber sido objeto de un aviso conjunto del FBI, de CISA y del MS-ISAC. El agregador público de sitios de filtración contabilizaba el 16 de noviembre de 2026 **317 víctimas publicadas en 42 países**, con la primera el 5 de junio de 2023 y la más reciente el 9 de noviembre de 2026, siete días antes del cierre de este informe. IBM X-Force, en junio de 2026, lo describe operando como ransomware como servicio «desde al menos mayo de 2023» y cifra en unas ochenta las víctimas reclamadas durante 2025. Valoramos **casi con certeza** *(95–99 %)*. **Confianza: alta.** *Base:* agregador público consultado directamente más informe de proveedor de primera mano.

**KJ-2.** La única víctima chilena documentada es el Ejército de Chile, y el caso es el más instructivo de toda esta cartera por lo que ocurrió después del cifrado. El incidente se detectó el fin de semana del 27 de mayo de 2023, la institución lo confirmó públicamente el 29, y el 9 de junio Rhysida publicó los datos y los puso en subasta en su sitio de la red Tor. Un investigador de una firma chilena cifró en unos **360 000 documentos** lo publicado, que el grupo presentó como cerca del 30 % de lo robado. Valoramos **casi con certeza** *(95–99 %)* los hechos y la cronología; **la cifra de volumen proviene del atacante** y se cita como tal. **Confianza: alta** en la cronología, **baja** en el volumen. *Base:* CronUp, firma chilena con seguimiento en tiempo real, y prensa especializada.

**KJ-3.** En el caso chileno hubo una detención dentro de la institución víctima, y eso obliga a tratar una dimensión que los demás informes de extorsión de esta cartera no tratan. El 5 de junio de 2023, la Policía de Investigaciones detuvo a un cabo segundo del Ejército por su presunta participación, con incautación de dispositivos, y un tribunal decretó prisión preventiva por infracción a la ley de delitos informáticos. **No conocemos el resultado judicial ni el papel exacto que se le atribuyó**, y conviene no construir sobre eso más de lo que soporta. Lo que sí soporta es una pregunta de diseño: **nuestro procedimiento de respuesta ante extorsión supone que todos los que lo ejecutan están del lado de la organización.** Valoramos **casi con certeza** *(95–99 %)* que la detención ocurrió; **no valoramos** su significado. **Confianza: alta** en el hecho, **baja** en la interpretación. *Base:* CronUp citando prensa nacional, más cobertura internacional.

**KJ-4.** El acceso inicial de este grupo es, según el aviso gubernamental, el más prosaico posible: credenciales válidas contra servicios remotos y VPN sin autenticación multifactor. El aviso conjunto `AA23-319A` lo atribuye expresamente a «la falta de autenticación multifactor habilitada por defecto», y en su revisión de abril de 2025 añade el cargador `Gootloader` como vía alternativa. **No hay un solo día cero atribuido a este grupo en el aviso.** Valoramos **muy probable** *(80–95 %)*. **Confianza: alta.** *Base:* aviso conjunto del FBI, CISA y MS-ISAC, con investigaciones hasta diciembre de 2024.

**KJ-5.** El cifrado de Rhysida fue roto públicamente en febrero de 2024 y hoy no se debe contar con ello. Investigadores de la Universidad Kookmin y de la agencia coreana KISA encontraron que el generador de números pseudoaleatorios —basado en ChaCha20 de la biblioteca LibTomCrypt y sembrado con la hora de ejecución— permitía reconstruir su estado interno, predecir las claves y también el orden en que el programa cifraba los ficheros; publicaron un descifrador gratuito. **Funciona solo con el cifrador de Windows, no con el de VMware ESXi ni con el basado en PowerShell**, y su publicación hacía previsible que el autor corrigiera el fallo. Valoramos **muy probable** *(80–95 %)* que el fallo esté corregido en las versiones actuales. **Confianza: moderada.** *Base:* trabajo académico con artículo publicado y herramienta distribuida por una agencia nacional; la valoración sobre la corrección es inferencia nuestra.

**KJ-6.** La marca «Rhysida» no identifica al adversario que tendríamos delante: identifica el cifrador. El aviso gubernamental la describe como ransomware como servicio, con herramientas e infraestructura alquiladas y el rescate repartido entre el grupo y sus afiliados, y señala similitudes con Vice Society (`DEV-0832`). IBM X-Force documenta en 2026 que el actor que Microsoft sigue como **Vanilla Tempest** despliega Rhysida tras una cadena propia de cargadores —`Endico`, `Broomstick` (también llamado `Oyster` o `CleanUpLoader`) y `Supper`, con el criptador `Tomb`— y recoge que Cisco Talos valora **con confianza baja** que Interlock «probablemente» surgió de operadores o desarrolladores de Rhysida. Valoramos **muy probable** *(80–95 %)* que el conjunto de técnicas de acceso varíe por afiliado. **Confianza: moderada.** *Base:* aviso gubernamental más IBM X-Force; las relaciones entre grupos las declara su fuente con confianza baja y así se citan.

**KJ-7.** El caso de Berlín, en agosto de 2026, muestra lo que cuesta no pagar, y es un dato útil para una decisión que normalmente se discute sin datos. Rhysida reclamó 5,79 TB y 1,44 millones de ficheros del gobierno del estado de Berlín, pidió 30 bitcoines —unos dos millones de euros—, la administración se negó públicamente y **al vencer el plazo los datos quedaron descargables para cualquiera**. Las autoridades confirmaron el robo pero no las cifras del atacante. Valoramos **casi con certeza** *(95–99 %)* que la negativa a pagar conlleva publicación íntegra en este grupo. **Confianza: alta.** *Base:* prensa especializada citando a las autoridades del estado y a prensa alemana de referencia.

**Qué cambiaría estos juicios:** una víctima chilena nueva de este grupo, o un informe que documente una variante del cifrador con un fallo criptográfico aprovechable. Lo primero convertiría este informe en una alerta; lo segundo cambiaría la respuesta operativa ante un incidente en curso. Son los indicadores `I-1` e `I-4` de §O-7.

---

## 2. Resumen ejecutivo

Rhysida apareció en mayo de 2023 y lo primero que hizo en la región fue atacar al Ejército de Chile. El incidente se detectó el fin de semana del 27 de mayo, la institución lo confirmó el lunes 29 con instrucciones de no encender equipos ni conectarse a la red privada virtual, y el 9 de junio el grupo publicó los datos en su sitio de la red Tor y los puso en subasta. Un investigador chileno contabilizó unos 360 000 documentos, que el grupo presentó como el 30 % de lo robado. Cuatro días antes, la Policía de Investigaciones había detenido a un cabo segundo de la institución por su presunta participación, y un tribunal decretó prisión preventiva.

Tres años y medio después, el grupo sigue funcionando. El agregador público de sitios de filtración contaba 317 víctimas en 42 países el día de cierre de este informe, con la última publicada siete días antes. Y en agosto de 2026 llevó a cabo su operación más visible: el gobierno del estado de Berlín, 5,79 TB reclamados, 30 bitcoines de rescate, negativa pública a pagar y publicación íntegra al vencer el plazo.

Lo que hace a este grupo merecedor de informe propio no es su sofisticación, que es media. Es que su expediente contiene tres lecciones que no están en los otros informes de extorsión de esta cartera.

La primera es sobre la **entrada**: el aviso conjunto del FBI, de CISA y del MS-ISAC dice que entra con credenciales válidas contra VPN sin autenticación multifactor. No hay día cero. Es la misma puerta de siempre, y sigue abierta.

La segunda es sobre la **recuperación**: en febrero de 2024 investigadores coreanos rompieron su cifrado aprovechando un fallo en el generador de números aleatorios y publicaron un descifrador gratuito. Funcionó. Pero funcionó solo con el cifrador de Windows, y su publicación hacía previsible que el autor lo corrigiera. **La lección no es que el ransomware se pueda descifrar: es que confiar en que el adversario cometa un error criptográfico es una lotería, y que la copia de seguridad fuera de línea sigue siendo el único plan.**

La tercera es sobre **quién ejecuta la respuesta**. En el caso chileno hubo una detención dentro de la institución víctima. No sabemos qué papel se le atribuyó ni cómo terminó el caso, y no conviene especular. Pero sí conviene mirar nuestro propio procedimiento de respuesta ante extorsión y preguntarse si supone, en todos sus pasos, que todos los que lo ejecutan están del lado de la organización. El nuestro lo supone.

Lo que pedimos a Dirección son tres cosas concretas: autenticación multifactor resistente a suplantación en todo acceso remoto sin excepciones, una prueba real de restauración desde copia fuera de línea con medición del tiempo, y una revisión del procedimiento de extorsión que contemple la posibilidad de una persona interna implicada.

<!-- cti:cards -->

| Rasgo | Qué significa | Etiqueta |
|---|---|---|
| Entra con credenciales válidas | VPN sin segundo factor. Sin día cero, sin exploit. La puerta más vieja sigue siendo la más usada | `01 · entrada` |
| Doble extorsión con subasta | Cifra y publica. En el caso chileno además subastó. No pagar significa publicación íntegra | `02 · presión` |
| Su cifrado fue roto una vez | Febrero de 2024, fallo del generador aleatorio. Probablemente corregido. No es un plan de recuperación | `03 · lotería` |
| Es un servicio, no un equipo | Herramientas alquiladas y rescate repartido. El afiliado que nos toque define la cadena de acceso | `04 · servicio` |
| El caso chileno tuvo una detención interna | Un cabo del Ejército detenido en junio de 2023. Obliga a revisar quién ejecuta la respuesta | `05 · interno` |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `360 000` | Documentos del Ejército de Chile publicados, según el recuento de un investigador chileno | El grupo lo presentó como cerca del 30 % de lo robado. **Cifra de origen adversario** |
| `317` | Víctimas publicadas en el sitio de filtración, al 16-nov-2026 | En 42 países. Primera: 5-jun-2023. Última: 9-nov-2026 |
| `13` | Días entre la detección del incidente chileno (27-may-2023) y la subasta de los datos (9-jun-2023) | La confirmación pública llegó el día 2 |
| `80` | Víctimas reclamadas durante 2025, según IBM X-Force | La mayoría en Estados Unidos. Cifra equivalente a la de Interlock el mismo año |
| `37,6` | Días de media entre el ataque y la reclamación pública, según el agregador | Es la ventana en la que una víctima puede actuar antes de la exposición |
| `5,79` | Terabytes reclamados en el caso del gobierno de Berlín, agosto de 2026 | 1,44 millones de ficheros. Las autoridades confirmaron el robo, no las cifras |
| `30` | Bitcoines exigidos a Berlín, unos dos millones de euros | Negativa pública a pagar; publicación íntegra al vencer el plazo |
| `1` | Descifradores gratuitos publicados para este ransomware | Febrero de 2024, Universidad Kookmin y KISA. **Solo para el cifrador de Windows** |

<!-- cti:note type="good" -->

> ✅ **Decisiones que se solicitan a Dirección.** (a) **Autenticación multifactor resistente a suplantación en todo acceso remoto** —VPN, escritorio remoto, correo web, portales de administración— sin excepciones por antigüedad del sistema; donde el sistema no la soporte, aislarlo o retirarlo — 45 días. Es la contramedida directa a `KJ-4`. (b) **Prueba real de restauración desde copia fuera de línea**, con medición del tiempo hasta servicio y verificación de que la copia es inmutable y está segmentada — 60 días. (c) **Revisión del procedimiento de respuesta ante extorsión para contemplar la implicación de una persona interna**: quién queda fuera de la lista de distribución, cómo se preserva la evidencia, cuándo entra Recursos Humanos y cuándo la autoridad — 60 días, con Legal y Recursos Humanos. (d) **Decisión escrita y previa sobre el pago**, tomada en frío y aprobada por el Consejo, con el caso de Berlín como referencia de lo que implica no pagar — 90 días. (e) **Prohibir que la recuperación dependa de un posible descifrador**: que quede por escrito en el plan de continuidad que ningún plazo de recuperación se calcula sobre esa hipótesis — 30 días, coste nulo. (f) **Restablecimiento doble de la clave `KRBTGT` y reposición de contraseñas de dominio** incorporados al manual de respuesta, como recomienda el aviso gubernamental cuando se sospecha compromiso de `NTDS.dit` — 45 días.

---

## 3. Alcance, requisitos y limitaciones

**3.1 Requisitos de inteligencia atendidos**

| Req. | Enunciado | ¿Respondido? | Dónde |
|---|---|---|---|
| PIR-03 | ¿Qué grupos de extorsión con capacidad de impacto operacional están activos y nos pueden alcanzar? | Sí | §E-1, §E-3, §O-1 |
| PIR-04 | ¿Qué amenazas tienen víctimas documentadas en Chile o en la región? | Sí — es el núcleo del producto | §E-2, §E-5 |
| PIR-06 | ¿Qué consecuencias tiene la publicación de información sensible robada? | Sí, con dos casos desarrollados | §E-5, §O-3 |
| PIR-11 | ¿Contempla nuestro procedimiento de extorsión el riesgo de persona interna? | **Sí, y la respuesta es que no lo contempla** | §E-5, §O-6, `E-c` |
| — | ¿Es recuperable un cifrado de Rhysida hoy? | **Probablemente no** — el fallo de 2024 está presumiblemente corregido | `KJ-5`, §O-3 |
| — | ¿Estamos ya comprometidos o expuestos? | **No** — requiere telemetría e inventario | §O-4, §14 |

**3.2 Fuera de alcance.** No se evalúa: el catálogo general de buenas prácticas frente a ransomware, que está desarrollado en `CTI-2026-014` a `CTI-2026-016` y no se repite; el perfil completo de Vice Society y de Interlock, que son actores con producto propio pendiente; la economía del pago de rescates y su regulación, que es materia legal y financiera; la cadena de cargadores de los actores de acceso inicial (`Gootloader`, `Broomstick`, `Supper`, `Endico`), que merece producto propio y aquí solo se sitúa; y la respuesta técnica a un incidente en curso, que es materia del manual de respuesta y no de un informe de inteligencia.

**3.3 Limitaciones de la colección.** (i) **Sin telemetría propia**: §O-4 sin rellenar. (ii) **El caso chileno no tiene fuente oficial.** No existe informe público del Ejército, del CSIRT Nacional ni de la fiscalía sobre el vector de entrada, el alcance de la exfiltración o el contenido de lo publicado. La reconstrucción de §E-5 se apoya en una firma privada chilena que siguió el caso en tiempo real y en prensa, y **el vector de entrada del caso chileno es desconocido**. (iii) **Las cifras de volumen del caso chileno y del caso de Berlín provienen del adversario** o de recuentos sobre lo que el adversario publicó. Se citan con esa marca cada vez. (iv) **La implicación de la persona detenida en el caso chileno está en fase judicial**, sin sentencia conocida a la fecha de cierre; este informe no afirma ni insinúa su responsabilidad, y la trata exclusivamente como un hecho procesal con consecuencias para el diseño de nuestros procedimientos. (v) **El aviso gubernamental `AA23-319A` retiró en su revisión de abril de 2025 los indicadores de la versión de 2023**, que permanecen solo en el PDF archivado y en los paquetes STIX; los indicadores del Anexo A provienen de la versión vigente y de las demás fuentes, de modo que **no son el conjunto completo publicado históricamente**. (vi) **Hay una inconsistencia en el propio aviso** sobre el esquema de cifrado: describe «una clave RSA de 4096 bits con un algoritmo ChaCha20» y a continuación «una clave de 256 bits, un contador de 32 bits y un *nonce* de 96 bits»; las dos descripciones conviven y la primera es imprecisa. (vii) **Los datos del agregador público son del día de consulta** (16-nov-2026) y cambian; además su recuento refleja **lo que el grupo publica**, no los incidentes reales, de modo que subestima el total e incluye reclamaciones no verificadas. (viii) **Dos de las fuentes periodísticas sobre el caso de Berlín son de calidad desigual**; aquí solo se usa la que cita a las autoridades del estado y a prensa alemana de referencia, y las cifras del atacante van marcadas. (ix) **La única mención de Chile en las fuentes internacionales es el caso del Ejército**: el agregador no lista ninguna víctima chilena en su tabla de países, lo que sugiere que no ha habido otra publicada o que no fue atribuida al país.

**3.4 Metodología.** Disciplinas: OSINT gubernamental (un aviso conjunto de tres organismos, con dos versiones comparadas), OSINT comercial nacional (una firma chilena con seguimiento en tiempo real), OSINT comercial internacional de primera mano, OSINT académico (un método de descifrado con artículo y herramienta), OSINT de agregador (sitio de filtración, consultado directamente) y prensa especializada para los dos casos de estudio. Técnicas analíticas estructuradas: análisis de hipótesis competidoras (§O-6), comprobación de supuestos clave, pre-mortem, y estudio de caso comparado —Ejército de Chile y Berlín— para extraer la lección sobre el pago. Marcos: MITRE ATT&CK v18 (el aviso usa v17 y se indica dónde difiere), Pirámide del Dolor, Cadena de Intrusión, ICD 203, código Admiralty.

---

# NIVEL ESTRATÉGICO
### Para: Consejo · CISO · Riesgo · Continuidad · Asuntos Corporativos · Recursos Humanos · Horizonte: 6–24 meses

## E-1. Qué representa este actor en el panorama

Rhysida no es sofisticado y eso es, precisamente, lo que lo hace relevante. El aviso conjunto del FBI, de CISA y del MS-ISAC describe un grupo que **entra con credenciales válidas** contra servicios remotos y redes privadas virtuales, atribuyéndolo expresamente a la ausencia de autenticación multifactor habilitada por defecto; que se mueve con **escritorio remoto, PsExec y PuTTY**; que vuelca credenciales con `secretsdump` y `ntdsutil`; que borra registros con `wevtutil`; y que despliega el cifrador copiando un fichero llamado `conhost.exe` a `C:\Windows\Temp` en cada equipo con tres ficheros `.bat` numerados. No hay un solo día cero en el expediente. No hay un implante propio notable. **Hay credenciales robadas y herramientas de administración.**

El segundo rasgo es el modelo de negocio, y determina contra quién estaríamos defendiéndonos. El aviso lo describe como ransomware como servicio: herramientas e infraestructura alquiladas, rescate repartido entre el grupo y sus afiliados. Eso significa que **la marca identifica el cifrador, no al adversario**. IBM X-Force lo documenta con precisión en junio de 2026: el actor que Microsoft sigue como Vanilla Tempest llega con una cadena propia de cargadores —instaladores troyanizados, el descargador `Endico`, la puerta trasera `Broomstick`, también conocida como `Oyster` o `CleanUpLoader`, y el implante `Supper`, todo envuelto con el criptador `Tomb`— y al final del camino despliega Rhysida. Microsoft interrumpió esa campaña en septiembre de 2025. Es decir: la cadena de acceso que nos tocaría depende de quién haya alquilado el cifrador esa semana.

El tercer rasgo es la **selección de víctimas, que no es selección**. El aviso dice que son «objetivos de oportunidad». Los sectores que nombra son educación, salud, manufactura, tecnologías de la información y gobierno, y la distribución del agregador público lo confirma: educación el 19 %, salud el 16 %, servicios profesionales el 15 %, manufactura y gobierno y defensa el 11 % cada uno. **No hay una tesis sectorial que nos exima.** Lo que determina si nos toca es si tenemos un acceso remoto sin segundo factor, no a qué nos dedicamos.

Y el cuarto es el que da título a este informe: **la presión se ejerce publicando, y este grupo publica.** Doble extorsión en todos los casos; subasta en el caso chileno; publicación íntegra y descargable por cualquiera cuando Berlín se negó a pagar. La nota de rescate es un PDF llamado `CriticalBreachDetected`, con un código único por empresa y un portal en la red Tor. Y el grupo se presenta, según la descripción de CronUp, como «un equipo de ciberseguridad» que le hace un favor a la víctima señalándole sus problemas de seguridad.

<!-- cti:cards -->

| Cambio estructural | Por qué nos afecta | Etiqueta |
|---|---|---|
| La entrada es credencial, no vulnerabilidad | Nuestra inversión en parcheo no cubre esto. La cubre el segundo factor, y la cubre entera | `01 · entrada` |
| La marca no es el adversario | Es un servicio. La cadena de acceso cambia con el afiliado, y por tanto los indicadores de acceso caducan antes que el cifrador | `02 · servicio` |
| No hay sector seguro | «Objetivos de oportunidad». Educación, salud, manufactura, gobierno: la distribución es plana. No hay argumento sectorial que nos exima | `03 · oportunidad` |
| No pagar significa publicación íntegra | Berlín lo demostró en agosto de 2026. La decisión sobre el pago hay que tomarla en frío y antes | `04 · publicación` |
| El cifrado fue roto una vez, y no volverá a serlo | Febrero de 2024. Útil como lección, inútil como plan: ningún plazo de recuperación puede apoyarse en ello | `05 · recuperación` |

## E-2. Victimología y distribución

<!-- cti:bars title="Rhysida: víctimas publicadas por sector, al 16 de noviembre de 2026 (317 en total)" color="#5a7ebe,#c0392b,#e0a33e,#4db99c" -->

| Sector | Víctimas |
|---|---|
| Educación | 60 |
| Salud | 51 |
| Servicios profesionales | 47 |
| Manufactura | 34 |
| Gobierno y defensa | 34 |
| Tecnología | 20 |
| Comercio | 15 |
| Resto | 56 |

<!-- cti:bars title="Rhysida: víctimas publicadas por país, al 16 de noviembre de 2026" color="#4a6fa5" -->

| País | Víctimas |
|---|---|
| Estados Unidos | 135 |
| Canadá | 20 |
| Alemania | 13 |
| Reino Unido | 10 |
| Australia | 8 |
| Italia | 8 |
| Suiza | 7 |
| Brasil | 6 |
| Malasia | 4 |
| México | 3 |

<!-- cti:note type="warn" -->

> ⚠ **Qué miden estas dos tablas y qué no.** Miden **lo que el grupo publica en su sitio de
> filtración**, no los incidentes que provoca. Quedan fuera las víctimas que pagaron antes
> de la publicación —que por definición no aparecen— y las que negociaron sin figurar; y
> entran reclamaciones que nadie ha verificado. El propio agregador señala que el grupo
> tarda **37,6 días de media entre el ataque y la reclamación pública**, de modo que el
> recuento siempre va por detrás. Como medida de actividad relativa sirve; como medida de
> daño, no. Y una advertencia sobre la tabla de países: **Chile no figura en ella**, y aun
> así la víctima chilena de 2023 existió y es la más documentada de todo este expediente.
> Las ausencias en los agregadores no son ausencias de hechos.

**Lo regional, con lo que hay.** En los 42 países del agregador, Brasil aparece con 6 víctimas y México con 3, lo que sitúa a Latinoamérica en el margen de la operación. En la parte del listado que pudimos leer directamente figuran tres víctimas regionales recientes: una manufacturera mexicana (30-oct-2026), **el Tribunal de Justicia del Estado de Minas Gerais, en Brasil (7-nov-2026)** y una editorial jurídica latinoamericana (23-sep-2026). Y el caso chileno, que no está en la tabla de países pero es el de mayor relevancia para nosotros, es de 2023.

**Lo que esto nos dice.** Que Chile no es un foco de este grupo, y que un solo caso basta para que la amenaza sea real: ese caso fue el Ejército. Para una organización chilena, el perfil de riesgo no se deriva del sector sino de la superficie: **acceso remoto sin segundo factor, credenciales reutilizadas y copias de seguridad en línea.**

## E-3. Tendencia y pronóstico

<!-- cti:chart title="Hitos públicos de la operación Rhysida, por año" cap="Cuenta hitos documentados (aparición, avisos, descifrador, casos de referencia, informes de proveedor), no volumen de víctimas. El recuento de víctimas del agregador, 317 al 16-nov-2026, se presenta en §E-2." -->

| Periodo | Hitos |
|---|---|
| 2023 | 4 |
| 2024 | 2 |
| 2025 | 2 |
| 2026 | 3 |

La trayectoria de esta operación tiene cuatro movimientos y ninguno es un salto técnico.

El primero es **la supervivencia a la atención**. Un aviso conjunto del FBI, de CISA y del MS-ISAC en noviembre de 2023 no detuvo al grupo; tampoco lo detuvo que su cifrado se rompiera públicamente en febrero de 2024. Tres años y medio después sigue publicando víctimas. Para la gestión de riesgo, el dato relevante es que **la exposición pública de un grupo de extorsión no es una contramedida**.

El segundo es **la profesionalización de la entrada**. El aviso de 2023 describía credenciales válidas; su revisión de abril de 2025 añadió `Gootloader`, y en 2026 IBM X-Force documenta cadenas completas de instaladores troyanizados firmados con certificados fraudulentos, con descargadores y puertas traseras intermedias. El cifrador es el mismo; **lo que ha mejorado es el negocio del acceso, que está en otras manos**.

El tercero es **el movimiento hacia el gobierno y el sector público**. Gobierno y defensa es ya el 11 % del total publicado, y los dos casos de referencia de este informe son un ejército y la administración de un estado federado. Es coherente con el modelo de oportunidad y con una observación incómoda: **las administraciones tienen muchos accesos remotos antiguos y poca autenticación multifactor**.

El cuarto es un dato que conviene no sobreinterpretar: el agregador muestra una **tendencia mensual del −68 %** y seis víctimas en el mes en curso, frente a una media histórica mayor. Puede indicar declive, o rotación de afiliados hacia otras marcas —lo que la relación con Interlock que apunta Cisco Talos haría esperar—, o simplemente retraso en la publicación. **Con un solo mes de datos no se puede distinguir**, y presentarlo como declive sería un error.

<!-- cti:cards -->

| Escenario | Desarrollo | Etiqueta |
|---|---|---|
| Continuidad con rotación de afiliados | La marca sigue publicando víctimas con volumen irregular, y las cadenas de acceso cambian con los actores que alquilan el cifrador. Las detecciones de §X-3 que son de post-explotación mantienen su validez; las de acceso inicial caducan antes | `Probable · 55–80 %` |
| Migración de afiliados a otras marcas, con el cifrador en declive | El dato del −68 % se confirma y la actividad se desplaza a Interlock o a otra operación, con los mismos operadores detrás. **Para nosotros no cambia nada defensivamente**, y cambia todo en la gestión de indicadores | `Posibilidad real · 45–55 %` |
| Nueva víctima chilena, probablemente del sector público o de educación | Coherente con el perfil de oportunidad y con la distribución sectorial. Es el escenario que convertiría este informe en alerta | `Posibilidad real · 45–55 %` |
| Aparición de un fallo criptográfico nuevo y aprovechable | Ocurrió una vez. Que vuelva a ocurrir y que además se publique antes de que el autor lo corrija es poco probable, y **planificar sobre ello sería imprudente** | `Poco probable · 20–45 %` |

## E-4. Decisiones que este informe pide al nivel estratégico

<!-- cti:table highlight="Chile|chilen|multifactor|copia|interna|KRBTGT" -->

| # | Decisión | Fundamento | Plazo |
|---|---|---|---|
| E-a | **Autenticación multifactor resistente a suplantación en todo acceso remoto**, sin excepciones por antigüedad del sistema: VPN, escritorio remoto, correo web y portales de administración. Donde el sistema no la soporte, aislarlo o retirarlo con fecha | KJ-4: el aviso conjunto atribuye el acceso inicial a credenciales válidas contra servicios remotos **y lo imputa expresamente a la falta de segundo factor habilitado por defecto**. Es la contramedida de mayor cobertura del informe | 45 días |
| E-b | **Prueba real de restauración desde copia fuera de línea**, con medición del tiempo hasta servicio, y verificación de que la copia es inmutable, cifrada y está en un emplazamiento segmentado | KJ-5 y §O-3: el descifrador de 2024 probablemente ya no sirve. La copia fuera de línea es el único plan de recuperación que no depende del adversario | 60 días |
| E-c | **Revisión del procedimiento de respuesta ante extorsión para contemplar la implicación de una persona interna**: criterios para restringir la lista de distribución, preservación de evidencia con cadena de custodia, cuándo entra Recursos Humanos y cuándo la autoridad | KJ-3: en el caso chileno hubo una detención dentro de la institución víctima. **Nuestro procedimiento actual supone en todos sus pasos que todos los que lo ejecutan están del lado de la organización** | 60 días |
| E-d | **Decisión escrita y previa sobre el pago**, tomada en frío, aprobada por el Consejo y revisada por Legal, con el caso de Berlín como referencia documentada de lo que implica la negativa | KJ-7: Berlín se negó y los datos quedaron descargables para cualquiera. Esa decisión no se puede tomar bien el día del incidente, con la operación parada y el reloj corriendo | 90 días |
| E-e | **Dejar por escrito en el plan de continuidad que ningún plazo de recuperación se calcula sobre la existencia de un descifrador** | KJ-5: el episodio de 2024 generó la expectativa equivocada. Coste de la decisión: cero. Coste de no tomarla: un plan de continuidad con una hipótesis de lotería dentro | 30 días |
| E-f | **Incorporar al manual de respuesta el restablecimiento doble de la clave `KRBTGT` y la reposición de contraseñas de dominio** ante sospecha de compromiso de `NTDS.dit`, con el procedimiento probado y no solo documentado | El aviso conjunto lo recomienda expresamente, y este grupo volca `NTDS.dit` con `ntdsutil` y `secretsdump` como parte habitual de su cadena | 45 días |
| E-g | **Inventario y reducción de herramientas de administración remota y de transferencia** instaladas en el parque: AnyDesk, PsExec, PuTTY, clientes de almacenamiento en la nube, con lista de permitidos por equipo y por función | El aviso nombra todas esas herramientas como parte del repertorio del grupo, **y advierte expresamente que su uso no debe atribuirse a actividad maliciosa sin más evidencia**: por eso el control es de inventario y no de bloqueo ciego | 90 días |
| E-h | **Encargar a Asuntos Corporativos un plan de comunicación de crisis para el escenario de publicación**, con el caso chileno y el de Berlín como referencias de gestión pública | §E-5: la institución chilena comunicó al segundo día con instrucciones operativas claras, y eso es una decisión acertada que conviene poder repetir. Lo que no se puede improvisar es la respuesta a la publicación | 90 días |

## E-5. Estudio de caso: el Ejército de Chile, mayo y junio de 2023

> Este apartado existe porque es el único caso chileno documentado de esta cartera con
> cronología día a día, y porque lo que enseña no es técnico. **Lo que sigue se apoya en
> una firma privada chilena que siguió el caso en tiempo real y en prensa nacional e
> internacional. No hay informe oficial.** El vector de entrada es desconocido.

**Lo que ocurrió, con las fechas.** El fin de semana del 27 de mayo de 2023 se produjo un ataque que afectó a diversos sistemas de la red interna del Ejército de Chile; los sitios web institucionales estuvieron intermitentes esos días. El lunes 29 la institución lo confirmó públicamente y emitió instrucciones concretas: **no encender equipos, no conectarse a la red privada virtual, no conectar dispositivos de almacenamiento externo.** La red afectada se aisló y se informó al CSIRT del Estado Mayor Conjunto y al Ministerio de Defensa Nacional; el CSIRT de Gobierno confirmó en paralelo que se trataba de ransomware. El 3 de junio Rhysida empezó a publicar sus primeras víctimas en su sitio de la red Tor, sin que el Ejército figurara todavía. El 5 de junio la Policía de Investigaciones detuvo a un cabo segundo de la institución por su presunta participación, con incautación de dispositivos, y un tribunal decretó prisión preventiva por infracción a la ley de delitos informáticos. El 9 de junio el grupo publicó al Ejército en su sitio y puso los datos en subasta. Un investigador de la firma chilena cifró en unos **360 000 documentos** lo publicado; el grupo lo presentó como cerca del 30 % de lo robado.

**Las tres cosas que se hicieron bien, y conviene decirlo.** Primero, **la detección y el aislamiento fueron rápidos**: del fin de semana al lunes. Segundo, **la comunicación pública fue temprana y operativa**: al segundo día, con instrucciones que un usuario puede ejecutar —no encender, no conectar la VPN, no usar almacenamiento externo—, que es exactamente lo que hay que comunicar y no una declaración de intenciones. Tercero, **se notificó a las instancias correspondientes**, tanto al CSIRT sectorial como al ministerio.

**Las cuatro cosas que no sabemos, y que importan más que las anteriores.** Cómo entraron. Qué se exfiltró exactamente. Qué contenían los documentos publicados —hay afirmaciones de medios sobre material de inteligencia, datos personales de personal y detalles de despliegues, procedentes de una sola fuente y no corroboradas—. Y cómo terminó el caso judicial. **Que todo eso siga siendo desconocido tres años y medio después es, en sí mismo, el hallazgo más importante del caso**, porque significa que el sistema nacional no produjo una lección pública y transferible de su incidente de ciberseguridad más grave en una institución de defensa.

**La dimensión que ningún otro informe de esta cartera trata.** Hubo una detención dentro de la organización víctima. No sabemos qué papel se le atribuyó a esa persona ni cómo terminó el proceso, y este informe no lo insinúa. Pero el hecho procesal basta para plantear la pregunta de diseño: **nuestro manual de respuesta ante extorsión, como casi todos, supone que todos los que participan en la respuesta están del lado de la organización.** La lista de distribución del incidente, el canal de coordinación, el acceso a la evidencia, la decisión sobre el pago: todo está diseñado sobre esa premisa. Un procedimiento maduro debe poder funcionar sin ella, y el nuestro hoy no puede. Esa es la decisión `E-c`.

<!-- cti:note type="warn" -->

> ⚠ **Cómo citar este caso sin hacer daño.** Tres reglas. **Primera:** la cifra de 360 000
> documentos y el «30 % de lo robado» **son del atacante** o de recuentos sobre lo que el
> atacante publicó; no son una medición institucional. **Segunda:** la persona detenida
> está amparada por la presunción de inocencia y no consta sentencia; en cualquier uso
> interno de este caso —formación incluida— debe aparecer como hecho procesal sin
> atribución de responsabilidad. **Tercera:** el contenido de los documentos filtrados no
> está verificado; las afirmaciones sobre material de inteligencia o despliegues provienen
> de un solo medio y no se han corroborado. Usar este caso para asustar a la organización
> con detalles no verificados estropearía lo único que vale de él, que es la cronología.

**Y la comparación que vale la pena hacer.** Berlín, agosto de 2026, el otro extremo del mismo problema: exfiltración entre el 7 y el 12 de agosto, departamentos no desconectados de la red del estado **hasta el 14**, reclamación de 5,79 TB y 1,44 millones de ficheros, rescate de 30 bitcoines, **negativa pública a pagar** —«el estado de Berlín está siendo extorsionado», dijo el alcalde gobernante— y publicación íntegra al vencer el plazo, con los datos descargables por cualquiera. Las autoridades confirmaron el robo y el hallazgo de filtraciones adicionales en un departamento concreto, pero no las cifras del atacante. Las dos lecciones del contraste: **el tiempo hasta el aislamiento es la variable que más margen da** —dos días en Chile, siete en Berlín—, y **la negativa a pagar tiene un coste conocido y publicado**, que es exactamente el dato que hace falta para tomar la decisión `E-d` en frío.

---

# NIVEL OPERACIONAL
### Para: Jefatura de SOC · Respuesta a Incidentes · Threat Hunting · Continuidad · Horizonte: semanas–meses

## O-1. Identificación: una marca, varios operadores

| Nombre | Qué es | Relación declarada |
|---|---|---|
| `Rhysida` | **El cifrador y la operación de extorsión como servicio.** Activa desde al menos mayo de 2023; primera observación pública el 17 de mayo de 2023 | — |
| `Rhysida-0.1` | Cadena que el propio binario usa para identificarse, recogida por el aviso conjunto como desarrollo de capacidades propias (`T1587`) | Artefacto |
| `Vice Society` · `DEV-0832` | Operación de extorsión anterior | El aviso conjunto señala **similitudes** y remite a su propio aviso `AA22-249A`. Sophos publicó un análisis sobre «el cambio de un conglomerado de amenaza de Vice Society a Rhysida» |
| `Interlock` | Operación de extorsión posterior | Cisco Talos valora **con confianza baja** que «probablemente es un grupo nuevo diversificado surgido de operadores o desarrolladores de Rhysida» (recogido por IBM X-Force, jun-2026) |
| `Vanilla Tempest` | **Afiliado o actor de acceso**, nomenclatura de Microsoft | IBM X-Force documenta que usa `Endico`, `Tomb`, `Broomstick` y `Supper` y que **despliega Rhysida**, además de INC. Microsoft interrumpió una de sus campañas en septiembre de 2025 |
| `Broomstick` · `Oyster` · `CleanUpLoader` | **Tres nombres de la misma puerta trasera** usada en la cadena previa al despliegue | Herramienta, no actor |
| `Gootloader` | Cargador de acceso inicial | Añadido por el aviso conjunto en su revisión de abril de 2025 como vía de acceso usada «en ocasiones» |

<!-- cti:note type="warn" -->

> ⚠ **Nota de tradecraft — tres errores concretos que evitar.** El primero: **«Rhysida» no
> nombra a un equipo de atacantes.** Nombra un cifrador alquilado. Ante un incidente, la
> pregunta útil no es «qué hace Rhysida» sino «qué afiliado nos tocó», porque la cadena de
> acceso y las herramientas intermedias cambian con él y los indicadores de acceso inicial
> caducan antes que los del cifrado. El segundo: **las relaciones entre Rhysida, Vice
> Society e Interlock están declaradas con confianza baja por sus propias fuentes**;
> presentarlas como linaje establecido es sobrepasar lo que dicen. El tercero: **`Broomstick`,
> `Oyster` y `CleanUpLoader` son el mismo artefacto con tres nombres**, y contarlos como
> tres amenazas distintas infla el inventario, que es el mismo problema que `CTI-2026-022`
> describe con los nombres de actor.

## O-2. Atribución: qué se puede sostener

| Eje de atribución | Valoración | Confianza |
|---|---|---|
| Modelo de negocio | Ransomware como servicio, con herramientas e infraestructura alquiladas y rescate repartido con los afiliados | Alta |
| Motivación | Económica, por doble extorsión: cifrado más amenaza de publicación. Pago exclusivamente en bitcoines | Alta |
| Selección de víctimas | **Objetivos de oportunidad**, según el aviso conjunto. La distribución sectorial del agregador lo respalda: ningún sector supera el 19 % | Alta |
| Nexo estatal | **No planteado por ninguna fuente** | Alta (en la negativa) |
| Origen geográfico | **No determinado por ninguna fuente.** Ni el aviso conjunto ni IBM X-Force lo sitúan | Alta (en la negativa) |
| Relación con Vice Society | Similitudes señaladas por el aviso conjunto, citando a Microsoft, y un análisis de Sophos sobre el tránsito de un conglomerado de un grupo al otro | Moderada |
| Relación con Interlock | «Probablemente surgido de operadores o desarrolladores de Rhysida», **con confianza baja declarada** por Cisco Talos | Baja |
| Composición del conjunto de afiliados | Desconocida. IBM X-Force valora **con confianza media a alta** que las familias de malware que describe «son probablemente exclusivas de un número comparativamente pequeño de usuarios o afiliados» | Baja |

*Razonamiento sobre el modelo:* el dato que importa operativamente no es quién está detrás, sino que **el cifrador y el acceso son negocios distintos**. Eso explica por qué el aviso gubernamental describe una cadena de post-explotación muy consistente —`PsExec`, `secretsdump`, `wevtutil`, los tres `.bat` numerados— y en cambio describe el acceso inicial con dos vías distintas y una añadida dos años después. La parte consistente es la del dueño del cifrador; la variable es la de su clientela.

*Contraargumento sobre las relaciones entre grupos:* la tentación de dibujar un linaje Vice Society → Rhysida → Interlock es fuerte y las fuentes no lo sostienen con firmeza: una habla de «similitudes» y otra declara confianza baja. Para nuestras decisiones es indiferente —las contramedidas son las mismas—, y para la gestión de indicadores no lo es: fusionar los tres conjuntos importaría indicadores de un grupo a los casos de otro.

## O-3. Cómo opera la extorsión, y por qué eso determina qué control sirve

**El cifrado.** El aviso conjunto describe un ejecutable de 64 bits compilado con MinGW y GCC que **se inyecta en procesos en ejecución** (`T1055.002`), cifra y añade la extensión `.rhysida`. Su descripción del esquema es internamente inconsistente —«una clave RSA de 4096 bits con un algoritmo ChaCha20», y después «una clave de 256 bits, un contador de 32 bits y un *nonce* de 96 bits»—, y aquí se consigna tal cual con la advertencia de §3.3. Tras cifrar, **PowerShell borra el binario desde una ventana oculta**, y el propio ejecutable se elimina. Admite los argumentos `-d` para elegir directorio y `-sr` para borrar ficheros.

**La nota y el portal.** La nota es un **PDF llamado `CriticalBreachDetected`**, con un código único por empresa que dirige a un portal en la red Tor. CronUp describe ese portal: la víctima introduce el identificador de la nota y obtiene una página de pago, con un formulario adicional de autenticación y datos de contacto, e instrucciones para comprar y usar bitcoines. El texto de la nota viaja **como cadena en claro dentro del binario**, lo que el aviso señala como base para detección por cadenas.

**El episodio del descifrador, y la lección que deja.** En febrero de 2024, investigadores de la Universidad Kookmin y de la agencia coreana KISA publicaron un método de descifrado. El fallo estaba en el generador de números pseudoaleatorios criptográficamente seguro: basado en ChaCha20 de la biblioteca LibTomCrypt y **sembrado con la hora a la que se ejecutaba el programa**, permitía reconstruir su estado interno, derivar las claves y además predecir el orden en que se cifraban los ficheros. La herramienta se distribuyó gratis desde la agencia, con un artículo académico. **Tres salvedades que convierten este episodio en una advertencia y no en una buena noticia:** funciona solo con el cifrador de Windows, no con el de VMware ESXi ni con el basado en PowerShell; había sido usada en privado desde meses antes de publicarse, lo que sugiere que publicarla fue una decisión difícil; y su publicación hacía previsible que el autor corrigiera el fallo, que es lo que normalmente ocurre.

**Lo que esto implica para la defensa, y es la conclusión central del nivel operacional.** Si el cifrado llega a ejecutarse, la recuperación depende **exclusivamente** de nuestras copias de seguridad. No de un descifrador, no de la negociación, no de la esperanza de que el adversario repita un error de 2023. Y si la copia está en línea, accesible desde el dominio y con las mismas credenciales, no es una copia: es otro objetivo. Es la decisión `E-b`, y es la única de este informe que sigue funcionando cuando todas las demás han fallado.

**La publicación.** Doble extorsión en todos los casos (`T1657`), subasta en el caso chileno, y publicación íntegra y descargable cuando la víctima se niega, como en Berlín. **El robo ocurre antes del cifrado**, de modo que ningún control de recuperación mitiga esta mitad del daño: la mitiga el control de exfiltración y, antes, el de acceso.

## O-4. Nuestra exposición

<!-- cti:note type="gap" -->

> ⬛ **Sección sin evaluar — requiere telemetría, inventario y una prueba real.** De las
> doce preguntas, **X-1, X-2 y X-3 se responden en una tarde** y son las que deciden si
> somos objetivo fácil. **X-4 no se responde con un documento: se responde restaurando.**

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| X-1 | ¿Qué accesos remotos tenemos expuestos —VPN, escritorio remoto, portales de administración, correo web— y **cuáles no exigen segundo factor**? | Inventario de exposición externa · configuración de identidad | Identidad / Redes |
| X-2 | ¿Hay cuentas con acceso remoto cuyas credenciales aparezcan en filtraciones o en registros de ladrones de información? | Vigilancia de credenciales filtradas | Identidad |
| X-3 | ¿Existen cuentas de servicio o de proveedor con acceso remoto permanente, sin segundo factor y sin caducidad? | Revisión de identidades | Identidad |
| X-4 | **¿Cuánto tarda de verdad una restauración desde copia fuera de línea hasta tener servicio?** ¿Está probado este año? | Prueba real de restauración | Continuidad / TI |
| X-5 | ¿Nuestras copias son inmutables, cifradas y están en un emplazamiento segmentado con credenciales propias? | Revisión de la arquitectura de respaldo | Continuidad / TI |
| X-6 | ¿Qué herramientas de administración remota y de transferencia están instaladas en el parque, y cuáles sin ticket de cambio? | Inventario de software · control de cambios | TI |
| X-7 | ¿Detectamos el borrado de registros de eventos con `wevtutil` y la desactivación del registro? | EDR · SIEM | Ingeniería de Detección |
| X-8 | ¿Detectamos el volcado de `NTDS.dit` con `ntdsutil` o `secretsdump`, y tenemos probado el restablecimiento doble de `KRBTGT`? | EDR · manual de respuesta | Ingeniería de Detección / Identidad |
| X-9 | ¿Hay en el parque directorios `C:\in` o `C:\out`, o ficheros `S_0.bat`, `S_1.bat`, `S_2.bat`, `1.ps1`, o un `conhost.exe` fuera de `System32`? | Retrohunt en EDR | SOC |
| X-10 | ¿Está restringido PowerShell a usuarios autorizados, con registro de bloques de script y **180 días de retención**, y vigilamos su desactivación? | Directiva · SIEM | Ingeniería de Detección |
| X-11 | **¿Contempla nuestro procedimiento de extorsión la implicación de una persona interna?** ¿Quién decide restringir la lista de distribución? | Revisión documental | CISO / Legal / RR. HH. |
| X-12 | **¿Existe una decisión escrita y previa sobre el pago, aprobada por el Consejo?** | Revisión documental | CISO / Consejo |

## O-5. Cronología

<!-- cti:timeline -->

| Fecha | Hecho | Traza |
|---|---|---|
| `2023-05-17` | **Primera observación pública de la campaña Rhysida**, por MalwareHunterTeam | Global |
| `2023-05-27` | **Ataque a la red interna del Ejército de Chile**, detectado ese fin de semana. Los sitios institucionales quedan intermitentes | Chile |
| `2023-05-29` | **El Ejército confirma públicamente el incidente** e instruye no encender equipos, no conectarse a la VPN y no conectar almacenamiento externo. Se aísla la red y se informa al CSIRT del Estado Mayor Conjunto y al Ministerio de Defensa. El CSIRT de Gobierno confirma que es ransomware | Chile |
| `2023-06-03` | Rhysida comienza a publicar sus primeras víctimas en su sitio de la red Tor. El Ejército aún no figura | Global |
| `2023-06-05` | **La Policía de Investigaciones detiene a un cabo segundo del Ejército** por su presunta participación, con incautación de dispositivos. Un tribunal decreta prisión preventiva por infracción a la ley de delitos informáticos. *Sin sentencia conocida a la fecha de cierre* | Chile |
| `2023-06-05` | Primera víctima registrada por el agregador público, que a partir de aquí lleva la cuenta | Global |
| `2023-06-09` | **Rhysida publica al Ejército de Chile en su sitio y pone los datos en subasta.** Un investigador chileno cifra en unos 360 000 los documentos publicados; el grupo los presenta como cerca del 30 % de lo robado | Chile |
| `2023-11-15` | **El FBI, CISA y el MS-ISAC publican el aviso conjunto `AA23-319A`**: acceso con credenciales válidas contra VPN sin segundo factor, `PsExec`, `secretsdump`, `ntdsutil`, `wevtutil`, los tres `.bat` numerados, la nota `CriticalBreachDetected` y las similitudes con Vice Society | Global |
| `2024-02` | **Investigadores de la Universidad Kookmin y de KISA publican un método de descifrado** y una herramienta gratuita, aprovechando que el generador pseudoaleatorio se sembraba con la hora de ejecución. Solo para el cifrador de Windows | Global |
| `2024-12` | Fecha más reciente de las investigaciones incorporadas a la revisión del aviso conjunto | Global |
| `2025-04-30` | **Revisión del aviso conjunto**: añade `Gootloader` como vía de acceso, `AZCopy` y el explorador de almacenamiento de Azure como herramientas, y **retira los indicadores de la versión de 2023** | Global |
| `2025-09` | **Microsoft interrumpe una campaña de Vanilla Tempest** basada en instaladores troyanizados que desplegaba `Endico` y `Broomstick` cifrados con `Tomb` y terminaba en Rhysida | Global |
| `2026-08-07` → `08-12` | **Ventana de exfiltración en el gobierno del estado de Berlín**, según los investigadores forenses | Alemania |
| `2026-08-14` | Los departamentos afectados no se desconectan de la red del estado hasta esta fecha: **siete días después del inicio de la exfiltración** | Alemania |
| `2026-08-31` | **Berlín confirma el robo de datos y rechaza públicamente pagar.** Rescate exigido: 30 bitcoines, unos dos millones de euros. Reclamación del grupo: 5,79 TB y 1,44 millones de ficheros | Alemania |
| `2026-09-23` | El agregador registra como víctima a una editorial jurídica latinoamericana | Latinoamérica |
| `2026-10-30` | El agregador registra como víctima a una manufacturera mexicana | México |
| `2026-11-07` | El agregador registra como víctima al **Tribunal de Justicia del Estado de Minas Gerais**, Brasil | Brasil |
| `2026-11-09` | Última víctima publicada antes del cierre de este informe: una empresa tailandesa | Global |
| `2026-11-16` | Cierre de este informe. **317 víctimas publicadas en 42 países; Chile no figura en la tabla de países del agregador y aun así tiene la víctima mejor documentada del expediente** | Chile |

## O-6. Hipótesis alternativas consideradas

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| H1 — Operación de extorsión como servicio, con selección de víctimas por oportunidad y acceso inicial variable según el afiliado | Consistente con las ocho fuentes. Explica la consistencia de la cadena de post-explotación frente a la variabilidad del acceso, y explica que un aviso gubernamental no la haya detenido | `Retenida` |
| H2 — El grupo está en declive y sus afiliados migran a otras marcas | Apoyada por la tendencia mensual del −68 % del agregador y por el vínculo que Cisco Talos apunta con Interlock. **Inconsistencia:** un solo mes de datos no distingue declive de retraso en la publicación, y el grupo publicó víctimas hace siete días | `Posibilidad real · 45–55 %` |
| H3 — El caso chileno fue un ataque dirigido a la institución y no un objetivo de oportunidad | Posible por el valor del objetivo, pero **sin evidencia:** no se conoce el vector de entrada y el aviso gubernamental describe la operación como oportunista. La detención de una persona interna admite las dos lecturas y no decide ninguna | `Retenida sin resolver` |
| H4 — Volverá a aparecer un fallo criptográfico aprovechable | Ocurrió una vez y se publicó. Que vuelva a ocurrir, que se publique y que el autor no lo haya corregido antes es una concurrencia improbable. **Se consigna para cerrarla:** planificar sobre esto es planificar sobre una lotería | `Poco probable · 20–45 %` |
| H5 — Nuestras copias de seguridad resistirían un incidente de este grupo | **No evaluada, y es el supuesto más peligroso del informe.** El grupo vuelca credenciales de dominio con `ntdsutil` y se mueve con `PsExec`: una copia accesible con credenciales de dominio no es una copia. Se resuelve con la prueba de `X-4`, no con un documento | `No evaluada` |
| H6 — La implicación de una persona interna en el caso chileno es excepcional y no generalizable | Probablemente cierta en términos de frecuencia, **y operativamente irrelevante:** un procedimiento que solo funciona si nadie dentro está implicado es un procedimiento con una condición no verificable. Se retiene como matiz, no como motivo para no hacer `E-c` | `Retenida como matiz` |
| H7 — Rhysida, Vice Society e Interlock son la misma operación bajo nombres sucesivos | **Apoyada débilmente y por sus propias fuentes con confianza baja.** No se adopta. Fusionar los conjuntos importaría indicadores de un grupo a los casos de otro, que es un error con coste operativo | `Retenida sin resolver` |

**Supuesto clave.** Que el acceso inicial seguirá siendo credencial válida sobre servicio remoto expuesto. **Si es falso** —si los afiliados se desplazan a la explotación de un dispositivo de borde, como IBM X-Force documenta ya para Interlock con una vulnerabilidad de cortafuegos en 2026— entonces la decisión `E-a` sigue siendo necesaria pero deja de ser suficiente, y el peso se traslada al parcheo de perímetro y a la detección de post-explotación de §X-3.

**Pre-mortem.** Es mayo de 2027 y este informe resultó equivocado. Los tres finales más probables: **(1)** desplegamos segundo factor en la VPN principal, quedó una excepción por un sistema antiguo «que no lo soporta», y por ahí entraron —la decisión `E-a` decía «sin excepciones» y la excepción se concedió en una reunión—; **(2)** la restauración funcionó técnicamente y tardó once días, porque nadie había medido `X-4` y el plan suponía dos; **(3)** gestionamos bien el incidente técnico y perdimos el control del relato, porque la publicación llegó antes que nuestro plan de comunicación —la decisión `E-h`, que era de Asuntos Corporativos—.

## O-7. Indicadores y señales de alerta

| # | Indicador observable | Qué señalaría | Disciplina | Responsable |
|---|---|---|---|---|
| I-1 | **Víctima chilena nueva publicada en el sitio de filtración** | Convierte este informe en alerta y obliga a revisión anticipada; permite además ofrecer apoyo sectorial | OSINT · agregadores | Célula CTI |
| I-2 | Aparición de credenciales nuestras, o de un proveedor con acceso remoto a nuestra red, en filtraciones o registros de ladrones | Es el vector de acceso inicial de `KJ-4`, visto con antelación | Vigilancia de credenciales | Identidad |
| I-3 | Autenticación remota exitosa desde geografía o proveedor de red anómalo sobre una cuenta sin segundo factor | El acceso inicial en curso. Es la alerta que más margen da | Identidad · VPN | SOC |
| I-4 | **Publicación de un fallo criptográfico aprovechable en una variante nueva del cifrador** | Cambiaría la respuesta operativa ante un incidente en curso, y solo entonces | OSINT académico · comercial | Célula CTI |
| I-5 | Víctima nueva en Latinoamérica, especialmente en sector público o judicial | El Tribunal de Minas Gerais es de hace nueve días: indica interés regional creciente por el sector | OSINT · agregadores | Célula CTI |
| I-6 | Campaña de instaladores troyanizados firmados con certificado fraudulento dirigida a nuestro sector | Es la cadena de acceso de Vanilla Tempest, el afiliado mejor documentado | OSINT comercial | Célula CTI |
| I-7 | Aparición de nuestra organización, o de un proveedor crítico, en el sitio de filtración de este o de otro grupo | Materializa el escenario. **Vigilarlo también para los proveedores**, porque su incidente es nuestro incidente de datos | OSINT · agregadores | Célula CTI / Compras |
| I-8 | Resultado judicial del caso del cabo del Ejército de Chile | Es la única vía por la que el caso chileno puede producir una lección pública verificada | OSINT · prensa judicial | Célula CTI |

---

# NIVEL TÁCTICO
### Para: Analistas de SOC · Ingeniería de Detección · Threat Hunting · Horizonte: días–semanas

## T-1. Cadena de intrusión

<!-- cti:stages title="Cuatro etapas, y la primera no usa ninguna vulnerabilidad" dwell="next" -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 01 · Acceso | La credencial que ya tenían | **Credenciales válidas contra servicios remotos externos y VPN** (`T1078`), atribuido por el aviso conjunto a la falta de autenticación multifactor habilitada por defecto · alternativa añadida en abril de 2025: el cargador **`Gootloader`** · en la cadena del afiliado Vanilla Tempest que documenta IBM X-Force: **instaladores troyanizados firmados con certificados fraudulentos**, descargador `Endico`, puerta trasera `Broomstick` (alias `Oyster`, `CleanUpLoader`) e implante `Supper`, todo envuelto con el criptador `Tomb` · **ninguna vulnerabilidad atribuida a este grupo en el aviso** |
| Etapa 02 · Reconocimiento | Comandos nativos, nada que detectar por firma | `net user <usuario> /domain` · `net group "domain computers" /domain` · `net group "domain admins" /domain` · `net localgroup administrators` · `ipconfig` · `whoami` · `nltest` · ejecutados desde `cmd.exe` y PowerShell · `PowerView` para reconocimiento de dominio y recolección de credenciales · el aviso señala como anomalía la generación del fichero `ntuser.dat` en el primer inicio de sesión de la cuenta comprometida |
| Etapa 03 · Movimiento y credenciales | Herramientas de administración, usadas como tales | **`PsExec` «intensamente aprovechado»** para ejecución remota y movimiento lateral · escritorio remoto (`mstsc.exe`) · **`PuTTY` por SSH**, con rastro en el historial de la consola de PowerShell · `PortStarter`, puerta trasera en Go que **modifica el cortafuegos y abre puertos** hacia el mando y control · volcado de credenciales con `secretsdump` y **volcado de `NTDS.dit` con `ntdsutil`** · **`AnyDesk`** para acceso remoto y persistencia · **`wevtutil` para borrar los registros de sistema, aplicación y seguridad** · `AZCopy` y el explorador de almacenamiento de Azure, añadidos en 2025, para mover datos a almacenamiento en la nube · directorios de preparación **`C:\in`** (ficheros con nombre de equipo, probablemente de un escáner) y **`C:\out`** (herramientas y scripts) |
| Etapa 04 · Cifrado y extorsión | Tres `.bat` numerados y un PDF | **`S_0.bat`** coloca **`1.ps1`**, que contiene la lista de extensiones a cifrar o excluir · **`S_1.bat`** copia el cifrador, llamado **`conhost.exe`**, a `C:\Windows\Temp` en cada equipo de la lista · **`S_2.bat`** lo ejecuta en todo el entorno · el cifrador es un PE de 64 bits compilado con MinGW y GCC, **se inyecta en procesos en ejecución** (`T1055.002`), se identifica internamente como `Rhysida-0.1`, admite `-d` y `-sr`, y añade la extensión **`.rhysida`** · modificación del registro con comandos sin ofuscar desde `cmd.exe` · tras cifrar, **PowerShell borra el binario desde una ventana oculta** y el propio ejecutable se autoelimina · nota de rescate en PDF **`CriticalBreachDetected`**, con código único por empresa y portal en la red Tor; **el texto de la nota viaja como cadena en claro dentro del binario** · intento de cambiar el fondo de escritorio por una imagen dejada en `C:\Users\Public\bg.jpg` · **el robo de datos ocurre antes del cifrado**: doble extorsión (`T1657`), con subasta en el caso chileno |

**Permanencia:** el agregador cifra en **37,6 días la media entre el ataque y la reclamación pública**, que es la mejor aproximación pública a la ventana entre el compromiso y la exposición. En el caso de Berlín, la exfiltración ocupó cinco días (7 al 12 de agosto) y la desconexión llegó el 14. En el caso chileno no hay dato público sobre el tiempo de permanencia previo.

<!-- cti:note type="info" -->

> **Dónde se rompe la cadena más barato.** La **etapa 01 se rompe con un control de
> identidad y se rompe entera**: autenticación multifactor resistente a suplantación en
> todo acceso remoto. Es la decisión `E-a` y es la de mayor cobertura del informe. La
> **etapa 02 es casi indetectable por firma** —son comandos nativos— y se detecta por
> **secuencia**: cuatro o cinco de esos comandos desde la misma sesión en pocos minutos es
> la señal, no cada comando por separado (regla `D-2`). La **etapa 03 tiene dos señales de
> altísima fidelidad**: el borrado de registros con `wevtutil` y el volcado de `NTDS.dit`.
> Si cualquiera de las dos dispara, el incidente ya está avanzado y la respuesta es de
> contención, no de investigación. Y la **etapa 04 es demasiado tarde**: cuando `S_1.bat`
> está copiando `conhost.exe` a `C:\Windows\Temp`, lo único que decide el resultado son
> las copias de seguridad.

## T-2. Mapa MITRE ATT&CK

<!-- cti:matrix -->

| Táctica | ID | Técnica | Procedimiento observado |
|---|---|---|---|
| Desarrollo de recursos | T1587 | Develop Capabilities | Herramientas propias identificadas internamente como `Rhysida-0.1` |
| Acceso inicial | T1078 | Valid Accounts | **Credenciales válidas sobre VPN y servicios remotos externos**, atribuido a la ausencia de autenticación multifactor por defecto |
| Acceso inicial | TA0001 | *(sin identificador de técnica)* | `Gootloader` como vía de acceso, añadida en la revisión de abril de 2025 |
| Ejecución | T1059.001 | Command and Scripting Interpreter: PowerShell | `ipconfig`, `nltest`, comandos `net` y scripts; `powershell_ise.exe` lanzado antes de ejecutar `1.ps1` desde `%AppData%\Local\Temp` |
| Ejecución | T1059.003 | Command and Scripting Interpreter: Windows Command Shell | `S_0.bat`, `S_1.bat` y `S_2.bat`; comandos de registro sin ofuscar |
| Ejecución | T1059.009 | Command and Scripting Interpreter: Cloud API | `AZCopy`, añadido en 2025 |
| Escalada de privilegios | T1055.002 | Process Injection: Portable Executable Injection | El cifrador se inyecta en procesos en ejecución |
| Evasión | T1070.001 | Indicator Removal: Clear Windows Event Logs | **`wevtutil` borra los registros de sistema, aplicación y seguridad** |
| Evasión | T1070.004 | Indicator Removal: File Deletion | PowerShell borra el cifrador tras la ejecución; el binario se autoelimina |
| Evasión | T1564.003 | Hide Artifacts: Hidden Window | PowerShell ejecutado desde ventana oculta |
| Acceso a credenciales | T1003.003 | OS Credential Dumping: NTDS | **`secretsdump` y volcado de `NTDS.dit` con `ntdsutil`** |
| Acceso a credenciales | T1112 | Modify Registry | Comandos de registro ejecutados sin ofuscación desde `cmd.exe` |
| Descubrimiento | T1016 | System Network Configuration Discovery | `ipconfig` |
| Descubrimiento | T1018 | Remote System Discovery | `net group "domain computers" /domain` |
| Descubrimiento | T1033 | System Owner/User Discovery | `whoami` y comandos `net` desde PowerShell |
| Descubrimiento | T1069.001 | Permission Groups Discovery: Local Groups | `net localgroup administrators` |
| Descubrimiento | T1069.002 | Permission Groups Discovery: Domain Groups | `net group "domain admins" /domain` |
| Descubrimiento | T1087.002 | Account Discovery: Domain Account | `net user <usuario> /domain` |
| Descubrimiento | T1482 | Domain Trust Discovery | `nltest` |
| Movimiento lateral | T1021.001 | Remote Services: Remote Desktop Protocol | Escritorio remoto con `mstsc.exe` |
| Movimiento lateral | T1021.004 | Remote Services: SSH | **`PuTTY`**, con rastro en el historial de la consola de PowerShell |
| Movimiento lateral | *(sin ID en el aviso)* | *(PsExec)* | **`PsExec` «intensamente aprovechado».** El aviso lo describe sin asignarle identificador de técnica |
| Colección | T1219 | Remote Access Software | **`AnyDesk`** para acceso remoto, persistencia y transferencia de ficheros |
| Colección | T1530 | Data from Cloud Storage | `AZCopy` y explorador de almacenamiento de Azure, añadidos en 2025 |
| Mando y control | T1219 | Remote Access Software | `AnyDesk` como canal |
| Mando y control | *(sin ID en el aviso)* | *(PortStarter)* | Puerta trasera en Go que **modifica la configuración del cortafuegos y abre puertos** hacia servidores de mando y control |
| Impacto | T1486 | Data Encrypted for Impact | Cifrado con la extensión `.rhysida`; descripción del esquema internamente inconsistente en el aviso (§3.3) |
| Impacto | T1657 | Financial Theft | **Doble extorsión**, con subasta en el caso chileno y publicación íntegra en el de Berlín |

<!-- cti:note type="warn" -->

> ⚠ **Procedencia del mapeo y dos ausencias llamativas.** Esta tabla reproduce las tablas
> 9 a 19 del aviso conjunto, que declara usar ATT&CK Enterprise v17. **El aviso no incluye
> táctica de persistencia ni de exfiltración**, lo que es notable en una operación de doble
> extorsión: el robo de datos está recogido solo como `T1657` y mediante las herramientas
> de nube, no como técnica de exfiltración. Tampoco asigna identificador a `PsExec` ni a
> `PortStarter`, dos piezas centrales de la cadena. **Ninguna de esas lagunas se ha
> rellenado aquí con mapeo propio**: se consignan como lo que son, huecos de la fuente, y
> su efecto práctico es que una medición de cobertura basada solo en esta tabla
> infravaloraría nuestras necesidades de detección en persistencia y exfiltración.

## T-3. Dónde atacamos en la Pirámide del Dolor

<!-- cti:pyramid -->

| Nivel | Qué contiene en este informe y qué vale | Valor |
|---|---|---|
| Hashes | Una treintena del aviso vigente —la mayoría de la suite `PsTools`, que es **software legítimo de Microsoft**— más los tres del caso chileno. **Valor muy bajo:** el aviso retiró los indicadores de 2023 y los que quedan son en su mayoría de herramientas legítimas que no deben bloquearse. Útiles para retrohunt y para confirmar | Base · valor trivial |
| IP · Dominios | Casi nada: el aviso vigente publica **un solo dominio** y dos URL de almacenamiento en la nube, y **ninguna dirección IP**. Dos cuentas de correo en `onionmail.org` y el formato con que las construyen. Es un recordatorio de que en una operación como servicio la infraestructura es del afiliado y rota con él | Valor bajo |
| Artefactos | **Lo más valioso del expediente, y es abundante.** Extensión `.rhysida` · nota `CriticalBreachDetected` en PDF, con su texto como cadena en claro en el binario · cifrador llamado **`conhost.exe` fuera de `System32`** · scripts `S_0.bat`, `S_1.bat`, `S_2.bat`, `1.ps1` · directorios `C:\in` y `C:\out` · `C:\out\PSTools.zip\` · imagen `C:\Users\Public\bg.jpg` · cadena interna `Rhysida-0.1` · argumentos `-d` y `-sr` | Valor medio |
| Herramientas | `PsExec`, `PuTTY`, `AnyDesk`, `mstsc`, `wevtutil`, `ntdsutil`, `secretsdump`, `PowerView`, `AZCopy`, explorador de almacenamiento de Azure, `powershell_ise`. **Todas legítimas**, y el aviso advierte expresamente que su uso **no debe atribuirse a actividad maliciosa sin más evidencia**. Se detectan por contexto, por equipo y por ausencia de ticket | Valor alto |
| TTP | Autenticación remota exitosa sobre cuenta sin segundo factor · secuencia de reconocimiento de dominio en minutos desde una sesión · borrado de registros de eventos · volcado de `NTDS.dit` · copia de un ejecutable a `C:\Windows\Temp` en muchos equipos a la vez · despliegue masivo con `PsExec` fuera de ventana de cambio. **Seis comportamientos que no dependen del afiliado ni de la marca del cifrador** | Cima · valor máximo |

## T-4. Hipótesis de caza prioritarias

<!-- cti:accordion critical="^(H-1|H-2|H-3|H-4)\b" regional="^(H-13|H-14)\b" -->

**H-1 — Autenticación remota exitosa sobre una cuenta sin segundo factor.** Inicios de sesión correctos en VPN, escritorio remoto, correo web o portales de administración por cuentas que no tienen autenticación multifactor exigida, especialmente desde direcciones, proveedores de red o geografías no habituales para esa cuenta. Fuente: registros del proveedor de identidad, concentrador de VPN. **Es la hipótesis madre de este informe:** el aviso conjunto sitúa aquí el acceso inicial y atribuye la causa a la ausencia de segundo factor. Fidelidad altísima si antes se ha hecho el inventario de `X-1`; sin ese inventario la hipótesis no se puede escribir, porque no sabríamos qué cuentas están sin proteger.

**H-2 — Secuencia de reconocimiento de dominio en una ventana corta.** La aparición, desde la misma sesión o el mismo equipo y en menos de treinta minutos, de **cuatro o más** de los siguientes: `net user /domain`, `net group "domain admins" /domain`, `net group "domain computers" /domain`, `net localgroup administrators`, `nltest`, `whoami`, `ipconfig`. Fuente: creación de procesos con línea de comandos. **Cada comando por separado es ruido administrativo; la secuencia en minutos no lo es.** Fidelidad alta con el umbral calibrado; falsos positivos conocidos: scripts de inventario y herramientas de auditoría, exceptuables por cuenta y por equipo.

**H-3 — Borrado de registros de eventos.** Ejecución de `wevtutil` con los verbos de limpieza (`cl`, `clear-log`), o el evento `1102` de borrado del registro de seguridad, o `Clear-EventLog` en PowerShell. Fuente: registro de seguridad, creación de procesos. **Si esto dispara, no es caza: es respuesta a incidentes.** Fidelidad extremadamente alta; prácticamente no tiene uso legítimo fuera de un mantenimiento planificado, y uno planificado deja ticket.

**H-4 — Volcado de la base de datos del directorio.** Uso de `ntdsutil` con `ifm` o `create full`, acceso a `NTDS.dit` por un proceso que no es el servicio de directorio, creación de instantáneas de volumen seguida de copia de ficheros del directorio, o firmas de `secretsdump`. Fuente: EDR en controladores de dominio, auditoría de acceso a objetos. **Es el paso que convierte un equipo comprometido en un dominio comprometido**, y es el que activa la necesidad del restablecimiento doble de `KRBTGT`. Fidelidad extremadamente alta.

**H-5 — Ejecutable llamado `conhost.exe` fuera de `System32`.** Creación o ejecución de un fichero con ese nombre en cualquier ruta que no sea `C:\Windows\System32`, y en particular en `C:\Windows\Temp`. Fuente: creación de procesos, creación de ficheros. **`conhost.exe` es un binario legítimo de Windows y el grupo le puso ese nombre a su cifrador precisamente por eso:** la señal no es el nombre, es la ruta. Fidelidad extremadamente alta y coste de implementación nulo.

**H-6 — Los tres scripts numerados y el script de extensiones.** Presencia o ejecución de ficheros llamados `S_0.bat`, `S_1.bat`, `S_2.bat` o `1.ps1`, en particular si `1.ps1` está en `%AppData%\Local\Temp` o si hay un `powershell_ise.exe` que lo lanza. Fuente: creación de ficheros, creación de procesos. **Son nombres publicados en un aviso gubernamental hace tres años y por tanto triviales de cambiar**; se incluyen porque su coste es una lista estática y su fidelidad, mientras duren, es total.

**H-7 — Directorios de preparación en la raíz del sistema.** Creación de directorios `C:\in` o `C:\out`, o de un `PSTools.zip` dentro de ellos. Fuente: creación de ficheros. **Un directorio de dos letras en la raíz de `C:` no es algo que cree el sistema ni un usuario normal.** Fidelidad muy alta, coste nulo.

**H-8 — Despliegue masivo con `PsExec` fuera de ventana de cambio.** Ejecución de `PsExec` o creación del servicio `PSEXESVC` en un número anómalo de equipos en una ventana corta, sin ticket de cambio asociado. Fuente: creación de servicios, creación de procesos, control de cambios. **El aviso describe `PsExec` como «intensamente aprovechado», y es también una herramienta legítima**: el criterio discriminante es administrativo —número de destinos, hora y ausencia de ticket—, no técnico. Fidelidad alta con el criterio bien definido.

**H-9 — Herramienta de administración remota instalada sin cambio aprobado.** Presencia o instalación de `AnyDesk` y equivalentes, cruzada con el registro de cambios y con el inventario autorizado. Fuente: inventario de software, creación de servicios. Es la misma hipótesis que `H-3` de `CTI-2026-021` y **conviene unificarlas en una sola regla de plataforma**: dos informes distintos de esta cartera llegan al mismo control por caminos distintos.

**H-10 — Cliente de almacenamiento en la nube moviendo volumen anómalo.** Ejecución de `AZCopy` o del explorador de almacenamiento de Azure, o subidas de volumen inusual a `blob.core.windows.net` y servicios equivalentes, desde servidores o equipos que no los usan habitualmente. Fuente: proxy con atribución de proceso, creación de procesos. **Es el canal de exfiltración añadido en la revisión de 2025 del aviso**, y es la mitad del daño que ninguna copia de seguridad mitiga. Fidelidad media-alta; requiere conocer qué equipos usan legítimamente esas herramientas.

**H-11 — Modificación de la configuración del cortafuegos del equipo con apertura de puertos.** Cambios en las reglas del cortafuegos local que abran puertos de escucha o permitan salida nueva, por un proceso que no es una herramienta de gestión aprobada. Fuente: eventos de cortafuegos, creación de procesos. **Es el comportamiento documentado de `PortStarter`**, la puerta trasera en Go de este grupo. Fidelidad alta.

**H-12 — Extensión y nota de rescate.** Creación de ficheros con extensión `.rhysida`, de ficheros PDF llamados `CriticalBreachDetected`, o de una imagen en `C:\Users\Public\bg.jpg`. Fuente: creación de ficheros. **Esta hipótesis no previene nada: detecta el cifrado en curso.** Se incluye porque la diferencia entre detectarlo en el primer equipo y detectarlo cuando pare la operación son horas de alcance, y porque su coste es nulo.

**H-13 — Nuestra organización o un proveedor crítico en un sitio de filtración.** Vigilancia de los sitios de filtración de este y de otros grupos buscando nuestro nombre y el de los proveedores con acceso a nuestros datos o a nuestra red. Fuente: agregadores, vigilancia de marca. **El agregador cifra en 37,6 días la media entre ataque y publicación**: si aparecemos ahí, llevamos más de un mes comprometidos y nos acabamos de enterar por el adversario. Para un proveedor, es nuestra única forma de saberlo.

**H-14 — Cuentas de proveedor con acceso remoto permanente y sin segundo factor.** Inventario y revisión de las identidades de terceros con acceso a nuestra red: contratistas, mantenimiento, soporte de fabricante. Fuente: revisión de identidades, registros de acceso. **No es caza en el host: es la variante de `H-1` que nadie mira**, porque esas cuentas suelen quedar fuera del alcance de las campañas de despliegue de segundo factor por ser «de un tercero».

## T-5. Brechas de visibilidad que hay que cerrar primero

| Brecha | Por qué importa aquí |
|---|---|
| **Sin inventario de accesos remotos y de qué cuentas carecen de segundo factor** | Deja `H-1` sin poder escribirse. No es brecha de telemetría sino de inventario, y es la que más determina nuestra exposición real |
| Registro de línea de comandos en creación de procesos deshabilitado | Deja ciegas `H-2`, `H-5`, `H-6` y `H-8`, es decir las etapas 02 y 04 completas |
| Sin EDR ni auditoría reforzada en controladores de dominio | Deja ciega `H-4`, el paso que convierte un equipo comprometido en un dominio comprometido |
| Registro de seguridad sin reenvío a servidor central endurecido | Permite que `wevtutil` borre la evidencia **y la detección a la vez**: `H-3` depende de que el registro ya no esté solo en el equipo |
| Retención de registros inferior a 180 días | El aviso recomienda 180 días para los registros de PowerShell. Con menos, un compromiso de 37 días de media se investiga a ciegas |
| **Copias de seguridad sin prueba real de restauración** | No es brecha de detección: es la brecha que decide el resultado. La resuelve `X-4`, y solo restaurando |
| Inventario de software sin cruce con control de cambios | Deja ciegas `H-8` y `H-9`, cuyo criterio de detección es administrativo |
| Proxy sin atribución de proceso | Degrada `H-10` a una lista de servicios de nube legítimos, inservible para alertar |
| Sin vigilancia de sitios de filtración para proveedores | Deja ciega `H-13` en su mitad más probable: que el incidente lo sufra un tercero y los datos sean nuestros |
| **Procedimiento de extorsión sin hipótesis de persona interna** | No es brecha de visibilidad sino de diseño, y es la lección del caso chileno. La resuelve `E-c` |

---

# NIVEL TÉCNICO
### Para: Ingeniería de detección · Automatización · TIP/SIEM · Vida útil: semanas–meses

## X-1. Arsenal y capacidad de la operación

| Propiedad | Valor |
|---|---|
| Cifrador | PE de 64 bits compilado con **MinGW y GCC**; se identifica internamente como `Rhysida-0.1`; **se inyecta en procesos en ejecución** (`T1055.002`); argumentos `-d` (directorio) y `-sr` (borrado de ficheros); extensión `.rhysida` |
| Esquema de cifrado | El aviso describe «una clave RSA de 4096 bits con un algoritmo ChaCha20» y a continuación «una clave de 256 bits, un contador de 32 bits y un *nonce* de 96 bits con una matriz de cuatro por cuatro de palabras de 32 bits». **Las dos descripciones conviven en la misma fuente y la primera es imprecisa** (§3.3) |
| Fallo criptográfico histórico | Generador pseudoaleatorio basado en **ChaCha20 de LibTomCrypt sembrado con la hora de ejecución**, lo que permitió reconstruir su estado, derivar las claves y predecir el orden de cifrado (Universidad Kookmin y KISA, feb-2024). **Solo afectaba al cifrador de Windows**, no al de VMware ESXi ni al basado en PowerShell. Presumiblemente corregido |
| Despliegue | Tres scripts por lotes numerados: `S_0.bat` (coloca `1.ps1` con la lista de extensiones), `S_1.bat` (copia `conhost.exe` a `C:\Windows\Temp` en cada equipo), `S_2.bat` (lo ejecuta en todo el entorno) |
| Nota de rescate | PDF llamado **`CriticalBreachDetected`**, con código único por empresa y portal en la red Tor; **el texto viaja como cadena en claro dentro del binario**, lo que el aviso propone como base de detección. El aviso sugiere además que el formato PDF podría indicar que solo se atacan sistemas capaces de mostrarlos |
| Portal de extorsión | La víctima introduce el identificador de la nota y obtiene página de pago, un formulario adicional de autenticación y datos de contacto, e instrucciones para comprar y usar bitcoines. **Pago solo en bitcoines**; en el caso chileno, además, subasta |
| Autodestrucción | Tras cifrar, **PowerShell borra el binario desde una ventana oculta** (`T1070.004`, `T1564.003`); el ejecutable también se autoelimina |
| Fondo de escritorio | Intento de sustituirlo por una imagen dejada en `C:\Users\Public\bg.jpg`; CronUp observó en las muestras tempranas que **esa función no funcionaba bien** |
| Madurez de las primeras muestras | CronUp describe las muestras de mayo de 2023 como **en fase temprana de desarrollo**, sin funciones habituales como el borrado de copias de volumen |
| Acceso inicial | Credenciales válidas sobre VPN y servicios remotos; `Gootloader` (añadido en 2025); en la cadena del afiliado Vanilla Tempest, instaladores troyanizados con certificados fraudulentos, `Endico`, `Broomstick`/`Oyster`/`CleanUpLoader` y `Supper`, con el criptador `Tomb` |
| Puerta trasera propia | **`PortStarter`**, escrita en Go, que modifica la configuración del cortafuegos y abre puertos hacia los servidores de mando y control |
| Herramientas de terceros y nativas | `cmd.exe`, `PowerShell`, `powershell_ise.exe`, `PsExec` y la suite `PsTools`, `mstsc.exe`, `PuTTY`, `secretsdump`, `ntdsutil.exe`, `PowerView`, `AnyDesk`, `wevtutil.exe`, `AZCopy`, explorador de almacenamiento de Azure. **El aviso advierte expresamente que el uso de estas herramientas legítimas no debe atribuirse a actividad maliciosa sin más evidencia** |
| Infraestructura publicada | **Un solo dominio** y dos URL de almacenamiento en la nube en el aviso vigente; **ninguna dirección IP**; dos cuentas de correo en `onionmail.org` y el formato `[Nombre][Apellido]@onionmail[.]org` con que se construyen las demás |
| Modelo | Ransomware como servicio: herramientas e infraestructura alquiladas, rescate repartido entre el grupo y sus afiliados |
| Lo que **no** tiene | Días cero atribuidos, explotación de vulnerabilidad en el aviso, implante de espionaje, capacidad destructiva más allá del cifrado, canal de mando y control propio documentado más allá de `PortStarter` y `AnyDesk` |

<!-- cti:note type="info" -->

> **Lo que este cuadro dice de la defensa.** Hay una desproporción que conviene nombrar:
> **toda la capacidad distintiva de esta operación está en el cifrador, y el cifrador es
> lo último que ocurre.** Lo que pasa antes —credenciales robadas, `net group`, `PsExec`,
> `wevtutil`, `ntdsutil`— no requiere capacidad alguna y es indistinguible, pieza por
> pieza, de la administración legítima de un dominio Windows. Eso significa que **la
> detección tiene que ser de secuencia y de contexto, no de herramienta**, y que la única
> contramedida que actúa antes de todo lo demás es el segundo factor en el acceso remoto.

## X-2. Artefactos persistentes entre versiones

<!-- cti:cards -->

| Categoría | Artefactos | Etiqueta |
|---|---|---|
| Cifrado | Extensión `.rhysida` · cadena interna `Rhysida-0.1` · argumentos `-d` y `-sr` · PE de 64 bits de MinGW/GCC con inyección en proceso | `impacto` |
| Despliegue | `S_0.bat` · `S_1.bat` · `S_2.bat` · `1.ps1` (lista de extensiones) · **`conhost.exe` en `C:\Windows\Temp`** · `powershell_ise.exe` lanzando `1.ps1` desde `%AppData%\Local\Temp` | `host` |
| Preparación | Directorios **`C:\in`** (ficheros con nombre de equipo, probablemente de un escáner) y **`C:\out`** (herramientas y scripts) · `C:\out\PSTools.zip\` | `host` |
| Extorsión | Nota PDF **`CriticalBreachDetected`** con código único por empresa · texto de la nota **como cadena en claro en el binario** · portal en la red Tor con formulario de autenticación · pago solo en bitcoines · subasta (caso chileno) | `extorsión` |
| Presentación | Imagen `C:\Users\Public\bg.jpg` para sustituir el fondo de escritorio, con la función defectuosa en las muestras tempranas | `host` |
| Correo del grupo | `rhysidaeverywhere@onionmail[.]org` · `rhysidaofficial@onionmail[.]org` · formato `[Nombre][Apellido]@onionmail[.]org` | `red` |
| Exfiltración a la nube | `AZCopy` · `StorageExplorer-windows-x64.exe` · URL de `blob.core.windows[.]net` | `red` |
| Anomalía de registro | Generación de `ntuser.dat` en el primer inicio de sesión de la cuenta comprometida, señalada por el aviso en el análisis de la tabla maestra de ficheros | `forense` |
| Muestra del caso chileno | `fury_ctm1042.bin` — muestra de referencia que CronUp publicó advirtiendo **expresamente que no es la usada contra el Ejército de Chile** | `Chile` |

## X-3. Lógica de detección prioritaria

<!-- cti:detections -->

**D-1 · CRÍTICO — Autenticación remota exitosa sobre cuenta sin segundo factor**

```
event.category == "authentication"
AND event.outcome == "success"
AND service.type IN ("vpn","rdp-gateway","owa","admin-portal")
AND user.id IN (<cuentas sin MFA exigida — inventario X-1>)
AND (source.geo.country_iso_code NOT IN (<países habituales>)
     OR source.as.organization NOT IN (<proveedores habituales de esa cuenta>))
```

→ Alerta de prioridad crítica con bloqueo de sesión y reposición de credencial. **Es el acceso inicial de este grupo y la regla más importante del informe.** Depende por completo del inventario `X-1`: sin saber qué cuentas carecen de segundo factor, la regla no se puede escribir.

**D-2 · CRÍTICO — Secuencia de reconocimiento de dominio en ventana corta**

```
process.command_line MATCHES "(?i)\b(net(1)? (user|group|localgroup)|nltest|whoami|ipconfig)\b"
| AGGREGATE count(distinct comando) AS variedad BY host.id, user.id, window(30m)
| WHERE variedad >= 4
AND NOT user.id IN (<cuentas de inventario y auditoría aprobadas>)
```

→ Alerta de prioridad crítica con aislamiento preventivo del equipo. **La señal es la secuencia, no el comando:** cada uno por separado es administración legítima. Calibrar el umbral con dos semanas de datos propios antes de poner nada en contención.

**D-3 · CRÍTICO — Borrado de registros de eventos**

```
(process.name == "wevtutil.exe" AND process.command_line MATCHES "(?i)\b(cl|clear-log)\b")
OR event.code == 1102
OR process.command_line MATCHES "(?i)Clear-EventLog"
OR (process.command_line MATCHES "(?i)wmic.*nteventlog.*cleareventlog")
```

→ **Contención automática e incidente.** Si esto dispara, el adversario ya está intentando borrar su rastro: la respuesta es de contención, no de triaje. No tiene uso legítimo fuera de un mantenimiento con ticket.

**D-4 · CRÍTICO — Volcado de la base de datos del directorio**

```
(process.name == "ntdsutil.exe" AND process.command_line MATCHES "(?i)(ifm|create full)")
OR (file.name == "ntds.dit" AND NOT process.name IN ("lsass.exe","ntfrs.exe","vssvc.exe"))
OR (process.command_line MATCHES "(?i)(secretsdump|-just-dc|vssadmin create shadow)"
    AND host.role == "domain-controller")
```

→ Contención automática, incidente y **activación del procedimiento de restablecimiento doble de `KRBTGT`**. Es el paso que convierte un equipo comprometido en un dominio comprometido.

**D-5 · CRÍTICO — Ejecutable `conhost.exe` fuera de `System32`**

```
(process.name == "conhost.exe" OR file.name == "conhost.exe")
AND NOT path MATCHES "(?i)^C:\\\\Windows\\\\(System32|SysWOW64|WinSxS)\\\\"
```

→ Contención automática y preservación del fichero. **`conhost.exe` legítimo vive en `System32`.** El grupo le puso ese nombre a su cifrador precisamente para que el nombre no llamara la atención; la ruta sí lo hace.

**D-6 · ALTO — Scripts de despliegue conocidos**

```
file.name IN ("S_0.bat","S_1.bat","S_2.bat","1.ps1")
OR (process.name == "powershell_ise.exe"
    AND process.command_line MATCHES "(?i)\\\\AppData\\\\Local\\\\Temp\\\\.*1\.ps1")
OR file.path MATCHES "(?i)^C:\\\\(in|out)\\\\"
```

→ Contención automática. **Nombres publicados en un aviso gubernamental hace tres años y por tanto triviales de cambiar**; se mantienen porque el coste es una lista estática y el valor, mientras duren, es total. Incluye los directorios de preparación.

**D-7 · ALTO — Despliegue masivo con `PsExec` fuera de ventana de cambio**

```
(service.name == "PSEXESVC" OR process.name MATCHES "(?i)^psexec(64)?\.exe$"
 OR file.name == "psexesvc.exe")
| AGGREGATE count(distinct host.id) AS destinos BY user.id, window(1h)
| WHERE destinos >= 5
AND NOT change_ticket.active == true
```

→ Alerta de prioridad crítica. **`PsExec` es legítimo**, y el aviso advierte contra atribuirlo sin evidencia: el criterio aquí es el número de destinos, la hora y la ausencia de ticket, no la herramienta.

**D-8 · ALTO — Herramienta de administración remota instalada sin cambio aprobado**

```
(service.name MATCHES "(?i)(anydesk|teamviewer|screenconnect|connectwise|atera|splashtop|pdq)"
 OR file.name MATCHES "(?i)anydesk.*\.exe")
AND NOT host.id IN (<equipos con ticket de cambio vigente>)
```

→ Contención: desinstalar, aislar y abrir incidente. **Unificar con `D-3` de `CTI-2026-021`**: dos amenazas distintas de esta cartera llegan al mismo control, y mantener dos reglas duplicadas es deuda operativa.

**D-9 · ALTO — Modificación del cortafuegos local con apertura de puerto**

```
(process.command_line MATCHES "(?i)netsh.*(advfirewall|firewall).*(add|set).*(allow|openport)"
 OR event.code IN (2004, 2005, 2006))
AND NOT process.parent.name IN (<herramientas de gestión aprobadas>)
```

→ Alerta de prioridad alta. Es el comportamiento documentado de `PortStarter`, la puerta trasera propia del grupo.

**D-10 · MEDIO — Exfiltración a almacenamiento en la nube**

```
(process.name MATCHES "(?i)^(azcopy|StorageExplorer-windows-x64)\.exe$"
 OR destination.domain MATCHES "(?i)\\.blob\\.core\\.windows\\.net$")
AND network.bytes_out > 1073741824
AND NOT host.id IN (<equipos con uso legítimo autorizado>)
```

→ Alerta de prioridad alta. **Es la mitad del daño que ninguna copia de seguridad mitiga.** El umbral de un gigabyte es orientativo y debe ajustarse al perfil de cada equipo.

**D-11 · MEDIO — Nota de rescate, extensión y fondo de escritorio**

```
file.extension == "rhysida"
OR file.name MATCHES "(?i)^CriticalBreachDetected(\.pdf)?$"
OR file.path MATCHES "(?i)^C:\\\\Users\\\\Public\\\\bg\.jpg$"
OR file.content CONTAINS "CriticalBreachDetected"
```

→ Contención automática de todo el segmento. **Esta regla no previene: detecta el cifrado en curso.** La diferencia entre dispararla en el primer equipo y descubrirlo cuando pare la operación son horas de alcance.

**D-12 · MEDIO — Infraestructura y correo del grupo**

```
dns.question.name MATCHES "(?i)776c5589\\.schedule\\.newhomessection\\.com"
OR email.address MATCHES "(?i)^rhysida[a-z]*@onionmail\\.org$"
OR email.body MATCHES "(?i)@onionmail\\.org"
```

→ Alerta de prioridad media. **El dominio de correo es el indicador más duradero de la lista** porque es parte del procedimiento de contacto del grupo, no de su infraestructura técnica, que rota con el afiliado.

<!-- cti:note type="warn" -->

> ⚠ **Las doce reglas están sin calibrar en nuestro entorno, y dos exigen trabajo previo
> que no es de ingeniería.** `D-1` **no se puede escribir** sin el inventario de cuentas sin
> segundo factor (`X-1`), y `D-7` y `D-8` **no se pueden usar** sin un cruce fiable con el
> control de cambios: su criterio discriminante es la ausencia de ticket, de modo que sin
> datos de cambios la regla marca administración legítima. Publicarlas en modo alerta dos
> semanas y medir antes de poner nada en contención.

<!-- cti:note type="gap" -->

> ⬛ **Lo que no se puede detectar con lo que hay publicado.** El aviso vigente **retiró los
> indicadores de 2023** y los que conserva son en su mayoría hashes de herramientas
> legítimas de Microsoft. **No hay direcciones IP, no hay direcciones de la red Tor, no hay
> reglas YARA ni Sigma, no hay claves de registro ni carteras de bitcoines** en la fuente
> gubernamental. Es decir: para este actor no existe una lista de bloqueo útil, y quien
> espere comprarla se llevará un conjunto de hashes de `PsExec`. **Toda la defensa está en
> las seis TTP de la cima de §T-3 y en el segundo factor.**

## X-4. Consultas de caza

```kql
// H-2 · Secuencia de reconocimiento de dominio en una ventana de 30 minutos
let comandos = DeviceProcessEvents
    | where Timestamp > ago(90d)
    | where ProcessCommandLine matches regex @"(?i)\b(net1?\s+(user|group|localgroup)|nltest|whoami|ipconfig)\b"
    | extend Comando = case(
          ProcessCommandLine matches regex @"(?i)net1?\s+user", "net user",
          ProcessCommandLine matches regex @"(?i)net1?\s+group", "net group",
          ProcessCommandLine matches regex @"(?i)net1?\s+localgroup", "net localgroup",
          ProcessCommandLine matches regex @"(?i)nltest", "nltest",
          ProcessCommandLine matches regex @"(?i)whoami", "whoami",
          "ipconfig");
comandos
| summarize Variedad = dcount(Comando), Comandos = make_set(Comando),
            Lineas = make_set(ProcessCommandLine, 10), Eventos = count()
        by DeviceName, AccountName, bin(Timestamp, 30m)
| where Variedad >= 4
| order by Variedad desc, Eventos desc
```

```kql
// H-3 + H-4 · Borrado de registros y volcado del directorio: las dos señales de alarma
let borrado = DeviceProcessEvents
    | where Timestamp > ago(180d)
    | where (FileName =~ "wevtutil.exe" and ProcessCommandLine matches regex @"(?i)\b(cl|clear-log)\b")
          or ProcessCommandLine matches regex @"(?i)Clear-EventLog"
          or ProcessCommandLine matches regex @"(?i)wmic.*nteventlog.*cleareventlog"
    | project Timestamp, DeviceName, AccountName, ProcessCommandLine, Señal = "borrado de registros";
let directorio = DeviceProcessEvents
    | where Timestamp > ago(180d)
    | where (FileName =~ "ntdsutil.exe" and ProcessCommandLine matches regex @"(?i)(ifm|create full)")
          or ProcessCommandLine matches regex @"(?i)(secretsdump|-just-dc)"
          or (ProcessCommandLine matches regex @"(?i)vssadmin.*create.*shadow" and DeviceName has "dc")
    | project Timestamp, DeviceName, AccountName, ProcessCommandLine, Señal = "volcado de directorio";
union borrado, directorio
| order by Timestamp desc
```

```kql
// H-5 + H-6 + H-7 · Artefactos de despliegue del cifrador
let cifrador = union
    (DeviceProcessEvents
     | where Timestamp > ago(180d)
     | where FileName =~ "conhost.exe"
     | where not(FolderPath matches regex @"(?i)^C:\\Windows\\(System32|SysWOW64|WinSxS)\\")
     | project Timestamp, DeviceName, Ruta = FolderPath, Señal = "conhost fuera de System32"),
    (DeviceFileEvents
     | where Timestamp > ago(180d)
     | where FileName in~ ("S_0.bat","S_1.bat","S_2.bat","1.ps1")
     | project Timestamp, DeviceName, Ruta = FolderPath, Señal = "script de despliegue"),
    (DeviceFileEvents
     | where Timestamp > ago(180d)
     | where FolderPath matches regex @"(?i)^C:\\(in|out)\\"
     | project Timestamp, DeviceName, Ruta = FolderPath, Señal = "directorio de preparación"),
    (DeviceFileEvents
     | where Timestamp > ago(180d)
     | where FileName endswith ".rhysida" or FileName matches regex @"(?i)^CriticalBreachDetected"
     | project Timestamp, DeviceName, Ruta = FolderPath, Señal = "cifrado en curso");
cifrador
| summarize Señales = make_set(Señal), Eventos = count(), Rutas = make_set(Ruta, 10)
        by DeviceName, bin(Timestamp, 1h)
| order by Eventos desc
```

```kql
// H-8 · PsExec desplegado sobre muchos equipos en una hora
DeviceProcessEvents
| where Timestamp > ago(180d)
| where FileName matches regex @"(?i)^psexec(64)?\.exe$"
      or ProcessCommandLine matches regex @"(?i)\\\\[^\\]+\\(admin|c)\$"
      or FileName =~ "psexesvc.exe"
| summarize Destinos = dcount(DeviceName), Equipos = make_set(DeviceName, 25), Eventos = count()
        by AccountName, bin(Timestamp, 1h)
| where Destinos >= 5
| order by Destinos desc
```

```kql
// H-10 · Exfiltración a almacenamiento en la nube por volumen
DeviceNetworkEvents
| where Timestamp > ago(180d)
| where RemoteUrl matches regex @"(?i)\.blob\.core\.windows\.net$"
      or InitiatingProcessFileName in~ ("azcopy.exe","StorageExplorer-windows-x64.exe")
| summarize Bytes = sum(todouble(coalesce(column_ifexists("BytesSent", 0), 0))),
            Conexiones = count(), Procesos = make_set(InitiatingProcessFileName, 5)
        by DeviceName, bin(Timestamp, 1h)
| order by Bytes desc, Conexiones desc
```

```kql
// H-1 · Autenticación remota exitosa desde origen anómalo (requiere el inventario X-1)
let sinMFA = dynamic([]);   // rellenar con el inventario de cuentas sin segundo factor
SigninLogs
| where TimeGenerated > ago(90d)
| where ResultType == 0
| where AppDisplayName has_any ("VPN", "Remote Desktop", "Outlook Web", "Azure Portal")
| extend SinMFA = iff(array_length(sinMFA) == 0, true, UserPrincipalName in (sinMFA))
| where SinMFA
| summarize Entradas = count(), Paises = make_set(Location, 10), ASN = make_set(tostring(parse_json(tostring(DeviceDetail)).operatingSystem), 5)
        by UserPrincipalName, bin(TimeGenerated, 1d)
| where array_length(Paises) > 1
| order by Entradas desc
```

```yaml
# Sigma — Borrado de registros de eventos de Windows
# Autor: Célula CTI · Fecha: 2026-11-16 · ATT&CK: T1070.001
# Nivel: critical · Estado: estable
# Sin uso legítimo fuera de mantenimiento con ticket aprobado.
title: Borrado de registros de eventos de Windows
id: 2026-024-wevtutil-clear
status: stable
description: >
  Uso de wevtutil, wmic o PowerShell para borrar los registros de eventos. Rhysida
  borra los registros de sistema, aplicación y seguridad como parte de su cadena,
  según el aviso conjunto AA23-319A del FBI, CISA y MS-ISAC.
logsource:
  category: process_creation
  product: windows
detection:
  wevtutil:
    Image|endswith: '\wevtutil.exe'
    CommandLine|contains:
      - ' cl '
      - ' clear-log '
  powershell:
    CommandLine|contains: 'Clear-EventLog'
  wmic:
    Image|endswith: '\wmic.exe'
    CommandLine|contains: 'cleareventlog'
  condition: wevtutil or powershell or wmic
falsepositives:
  - Mantenimiento planificado con ticket de cambio aprobado
level: critical
tags:
  - attack.defense_evasion
  - attack.t1070.001
```

```yaml
# Sigma — Cifrador desplegado como conhost.exe fuera de System32
# Autor: Célula CTI · Fecha: 2026-11-16 · ATT&CK: T1036.005, T1486
# Nivel: critical · Estado: experimental
# El conhost.exe legítimo vive en System32. La señal es la ruta, no el nombre.
title: conhost.exe ejecutándose fuera de System32
id: 2026-024-conhost-fuera-system32
status: experimental
description: >
  El cifrador de Rhysida se despliega con el nombre conhost.exe y se copia a
  C:\Windows\Temp en cada equipo mediante S_1.bat, según el aviso conjunto AA23-319A.
  Cualquier conhost.exe fuera de los directorios del sistema es sospechoso.
logsource:
  category: process_creation
  product: windows
detection:
  nombre:
    Image|endswith: '\conhost.exe'
  legitimo:
    Image|startswith:
      - 'C:\Windows\System32\'
      - 'C:\Windows\SysWOW64\'
      - 'C:\Windows\WinSxS\'
  condition: nombre and not legitimo
falsepositives:
  - Copias de conhost.exe en imágenes de despliegue o en carpetas de instalación
level: critical
tags:
  - attack.defense_evasion
  - attack.t1036.005
  - attack.impact
  - attack.t1486
```

## X-5. Mitigaciones de configuración con efecto directo

| Control | Corta |
|---|---|
| **Autenticación multifactor resistente a suplantación en todo acceso remoto**, sin excepciones por antigüedad del sistema | **La etapa 01 completa** (`T1078`). Es la contramedida de mayor cobertura del informe y la que el aviso conjunto sitúa en primer lugar |
| Restricción del escritorio remoto a cuentas conocidas, con segundo factor para cuentas privilegiadas y cierre de puertos sin uso | El movimiento lateral por escritorio remoto (`T1021.001`) |
| Restricción de PowerShell a usuarios autorizados, última versión, retirada de las anteriores, **registro de bloques de script con 180 días de retención** | Habilita `D-2`, `D-3` y `D-6`, y es lo que el propio aviso recomienda con ese plazo |
| Auditoría de línea de comandos y seguimiento de procesos activados en todo el parque | Habilita siete de las doce reglas de §X-3 |
| **Reenvío de registros a un servidor central endurecido** | **Que `wevtutil` borre la evidencia y la detección a la vez.** Sin esto, `D-3` detecta su propia ceguera |
| Lista de permitidos de aplicaciones y control de herramientas de acceso remoto, con inventario cruzado contra el control de cambios | `AnyDesk` como persistencia (`T1219`) y el abuso de `PsExec`. **El aviso advierte que no se atribuya sin evidencia**: el control es de inventario, no de bloqueo ciego |
| Segmentación de red y supervisión de tráfico lateral anómalo, con EDR | La etapa 03 y la propagación del despliegue del cifrador |
| **Copias de seguridad fuera de línea, cifradas, inmutables, con credenciales propias y en emplazamiento segmentado, con prueba real de restauración** | **La pérdida.** Es el único control de esta tabla que sigue funcionando cuando todos los demás han fallado, y el único que no depende de lo que haga el adversario |
| Restablecimiento doble de la clave `KRBTGT` y reposición de contraseñas de dominio ante sospecha de compromiso de `NTDS.dit`, con el procedimiento probado | Que el volcado del directorio (`T1003.003`) convierta un incidente contenido en un dominio perdido |
| Auditoría de cuentas administrativas, mínimo privilegio y acceso administrativo justo a tiempo | La escalada y el movimiento con credenciales volcadas |
| Parcheo priorizado de lo expuesto a Internet según catálogo de vulnerabilidades explotadas conocidas | No es la vía de este grupo **y sí la de afiliados que se desplazan a dispositivos de borde**, como ya se documenta para Interlock en 2026 |
| Prohibición escrita de calcular plazos de recuperación sobre la existencia de un descifrador | No corta nada: **evita que el plan de continuidad contenga una hipótesis de lotería.** Coste cero, decisión `E-e` |
| Procedimiento de respuesta ante extorsión con hipótesis de persona interna | No corta la intrusión: **evita que la respuesta se ejecute delante de quien no debe.** Es la lección del caso chileno |

---

## 14. Brechas de inteligencia y nuevos requisitos de colección

| # | Brecha | Impacto en el juicio | Requisito propuesto | Prioridad |
|---|---|---|---|---|
| G-1 | Sin telemetría propia ni inventario de accesos remotos | §O-4 vacía; **`D-1`, la regla más importante del informe, no se puede escribir**; no sabemos cuántas cuentas nuestras carecen de segundo factor | Ejecutar el cuestionario X-1 a X-12 de §O-4, empezando por X-1, X-2 y X-3 | Crítica |
| G-2 | **Sin prueba real de restauración desde copia fuera de línea** | `H5` de §O-6 es el supuesto más peligroso del informe y está sin evaluar. Todo el plan de recuperación descansa en una afirmación no comprobada | Prueba de restauración con medición del tiempo hasta servicio (decisión `E-b`) | Crítica |
| G-3 | **El caso chileno no tiene fuente oficial:** vector de entrada desconocido, alcance no publicado, contenido de lo filtrado no verificado, resultado judicial desconocido | El estudio de caso de §E-5 se apoya en una firma privada y en prensa. Las cifras son del atacante. **No existe lección pública verificada del incidente de ciberseguridad más grave en una institución de defensa chilena** | Consulta al CSIRT Nacional y, por vía institucional, al Ejército, sobre la existencia de un informe público o compartible; seguimiento del caso judicial (indicador `I-8`) | Alta |
| G-4 | El aviso gubernamental vigente **retiró los indicadores de 2023** | El Anexo A no es el conjunto completo publicado históricamente, y los indicadores retirados pueden seguir siendo útiles para retrohunt | Recuperar el PDF archivado de noviembre de 2023 y sus paquetes STIX, y la lista de indicadores que Sophos publicó en su repositorio | Media |
| G-5 | Inconsistencia interna del aviso sobre el esquema de cifrado | Impide afirmar con precisión cómo cifra, lo que importa si alguna vez hay que evaluar una posible recuperación criptográfica | Lectura del artículo académico de la Universidad Kookmin, que describe el esquema con precisión, y comparación con el aviso | Media |
| G-6 | **No sabemos si el fallo del generador aleatorio está corregido** | `KJ-5` es una inferencia nuestra. Si no estuviera corregido, cambiaría la respuesta ante un incidente en curso | Vigilancia del indicador `I-4`; consulta a KISA sobre la vigencia de su herramienta | Alta |
| G-7 | Sin visibilidad sobre qué afiliado opera contra nuestra región | Las cadenas de acceso inicial varían con el afiliado, y las nuestras son las que hay que detectar. Hoy detectamos las de Vanilla Tempest porque es la única documentada | Seguimiento de los actores de acceso asociados (`Gootloader`, `Broomstick`, `Supper`, `Endico`, `Tomb`) en el plan de colección permanente | Media |
| G-8 | **Sin vigilancia de sitios de filtración para nuestros proveedores** | `H-13` queda a medias: el escenario más probable es que el incidente lo sufra un tercero y los datos sean nuestros | Ampliar la vigilancia de marca a la lista de proveedores con acceso a datos o a red (con Compras) | Alta |
| G-9 | El dato del −68 % mensual del agregador no es interpretable con un solo mes | `H2` de §O-6 queda sin resolver, y con ella la pregunta de si este grupo está en declive o rotando de marca | Seguimiento mensual del recuento y de la relación con Interlock durante dos trimestres antes de concluir nada | Media |
| G-10 | Sin canal establecido con el CSIRT Nacional para incidentes de este tipo | Es la tercera vez en esta serie que la brecha aparece. En `CTI-2026-021` la inteligencia más pertinente era la del CERT nacional, y aquí lo sería el informe del caso del Ejército | Suscripción formal e interlocución establecida (decisión pendiente desde `CTI-2026-021`) | Alta |

---

# ANEXOS

## Anexo A — Indicadores de compromiso

<!-- cti:note type="warn" -->

> ⚠ **Leer antes de usar, y aquí la advertencia es inusual: buena parte de esta lista es
> software legítimo de Microsoft.** El aviso conjunto vigente publica como indicadores los
> hashes de **toda la suite `PsTools`** —`PsExec`, `PsInfo`, `PsList`, `PsKill` y el
> resto—, que son herramientas firmadas por Microsoft y de uso administrativo normal.
> **Bloquearlas por hash rompería la administración del parque.** Están marcadas abajo una
> por una. Tres advertencias más: el aviso **retiró los indicadores de su versión de 2023**,
> de modo que esta lista no es el conjunto histórico completo (brecha `G-4`); **no hay
> direcciones IP, ni direcciones de la red Tor, ni carteras de bitcoines** en la fuente
> gubernamental; y la muestra del caso chileno que publicó CronUp lleva su propia
> advertencia, **expresa en la fuente, de que no es la usada contra el Ejército de Chile**.

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Acción permitida |
|---|---|---|---|---|
| sha256 | `6633fa85bb234a75927b23417313e51a4c155e12f71da3959e168851a600b010` | `conhost.exe` — **el cifrador de Rhysida** (aviso `AA23-319A`) | Alta | Bloqueo y retrohunt |
| sha256 | `1c4978cd5d750a2985da9b58db137fc74d28422f1e087fd77642faa7efe7b597` | `S_0.bat` — script que coloca `1.ps1` (aviso `AA23-319A`) | Alta | Bloqueo y retrohunt |
| sha256 | `918784e25bd24192ce4e999538be96898558660659e3c624a5f27857784cd7e1` | `S_2.bat` — script que ejecuta el cifrador en todo el entorno (aviso `AA23-319A`) | Alta | Bloqueo y retrohunt |
| sha256 | `4e34b9442f825a16d7f6557193426ae7a18899ed46d3b896f6e4357367276183` | `1.ps1` — contiene la lista de extensiones a cifrar o excluir (aviso `AA23-319A`) | Alta | Bloqueo y retrohunt |
| sha256 | `c4d5a0c3ea69b2f3af0784df143d2b6d38e7b833def9e84ae9a54b2d25a91f5a` | **`Gootloader`** — vía de acceso inicial añadida en la revisión de abril de 2025 | Alta | Bloqueo y retrohunt |
| sha256 | `d0397d33239229e955eb37842ad84defbe70398bfd953c1b9657967540415aa3` | `main.dll` (aviso `AA23-319A`) | Alta | Bloqueo y retrohunt |
| sha256 | `0c829b3dccd425f090288cb9decc1bd11107e8be2323430aa2ee38e1ee01f716` | Fichero `Merchandise Planning` (aviso `AA23-319A`) | Media | Retrohunt |
| sha256 | `8329bcbadc7f81539a4969ca13f0be5b8eb7652b912324a1926fc9bfb6ec005a` | `Eula.txt` (aviso `AA23-319A`) | Media | Retrohunt |
| sha256 | `48f559e00c472d9ffe3965ab92c6d298f8fb3a3f0d6d203cd2069bfca4bf3a57` | `Sock5.sh` — script de proxy (aviso `AA23-319A`) | Alta | Bloqueo y retrohunt |
| sha256 | `a864282fea5a536510ae86c77ce46f7827687783628e4f2ceb5bf2c41b8cd3c6` | `fury_ctm1042.bin` — muestra de referencia de mayo de 2023 publicada por CronUp. **La fuente advierte expresamente que NO es la muestra usada contra el Ejército de Chile** | Alta | Bloqueo y retrohunt |
| sha1 | `69b3d913a3967153d1e91ba1a31ebed839b297ed` | Misma muestra de referencia de CronUp, en SHA-1 | Alta | Bloqueo y retrohunt |
| md5 | `0c8e88877383ccd23a755f429006b437` | Misma muestra de referencia de CronUp, en MD5 | Alta | Bloqueo y retrohunt |
| sha256 | `edfae1a69522f87b12c6dac3225d930e4848832e3c551ee1e7d31736bf4525ef` | `PsExec64.exe` — **herramienta legítima de Microsoft** listada por el aviso. **NO BLOQUEAR por hash** | Alta | Solo detección; verificar contexto |
| sha256 | `078163d5c16f64caa5a14784323fd51451b8c831c73396b967b4e35e6879937b` | `PsExec.exe` — **herramienta legítima**, mismo caso | Alta | Solo detección; verificar contexto |
| sha256 | `a9ca77dfe03ce15004157727bb43ba66f00ceb215362c9b3d199f000edaa8d61` | `PSTools.zip` — **suite legítima completa**, observada en `C:\out\` | Alta | Solo detección; verificar contexto |
| sha256 | `201d8e77ccc2575d910d47042a986480b1da28cf0033e7ee726ad9d45ccf4daa` | `PsGetsid64.exe` — **herramienta legítima**, mismo caso | Alta | Solo detección; verificar contexto |
| sha256 | `de73b73eeb156f877de61f4a6975d06759292ed69f31aaf06c9811f3311e03e7` | `PsInfo64.exe` — **herramienta legítima**, mismo caso | Alta | Solo detección; verificar contexto |
| sha256 | `fdadb6e15c52c41a31e3c22659dd490d5b616e017d1b1aa6070008ce09ed27ea` | `PsLoggedon64.exe` — **herramienta legítima**, mismo caso | Alta | Solo detección; verificar contexto |
| sha256 | `554f523914cdbaed8b17527170502199c185bd69a41c81102c50dbb0e5e5a78d` | `PsService64.exe` — **herramienta legítima**, mismo caso | Alta | Solo detección; verificar contexto |
| sha256 | `7ba47558c99e18c2c6449be804b5e765c48d3a70ceaa04c1e0fae67ff1d7178d` | `pskill64.exe` — **herramienta legítima**, mismo caso | Alta | Solo detección; verificar contexto |
| sha256 | `d3247f03dcd7b9335344ebba76a0b92370f32f1cb0e480c734da52db2bd8df60` | `pslist64.exe` — **herramienta legítima**, mismo caso | Alta | Solo detección; verificar contexto |
| sha256 | `5e55b4caf47a248a10abd009617684e969dbe5c448d087ee8178262aaab68636` | `psloglist64.exe` — **herramienta legítima**, mismo caso | Alta | Solo detección; verificar contexto |
| sha256 | `8d950068f46a04e77ad6637c680cccf5d703a1828fbd6bdca513268af4f2170f` | `pspasswd64.exe` — **herramienta legítima**, mismo caso | Alta | Solo detección; verificar contexto |
| sha256 | `d1f718d219930e57794bdadf9dda61406294b0759038cef282f7544b44b92285` | `psping64.exe` — **herramienta legítima**, mismo caso | Alta | Solo detección; verificar contexto |
| sha256 | `4226738489c2a67852d51dbf96574f33e44e509bc265b950d495da79bb457400` | `psshutdown64.exe` — **herramienta legítima**, mismo caso | Alta | Solo detección; verificar contexto |
| sha256 | `4bf8fbb7db583e1aacbf36c5f740d012c8321f221066cc68107031bd8b6bc1ee` | `pssuspend64.exe` — **herramienta legítima**, mismo caso | Alta | Solo detección; verificar contexto |
| sha256 | `be922312978a53c92a49fefd2c9f9cc098767b36f0e4d2e829d24725df65bc21` | `psfile64.exe` — **herramienta legítima**, mismo caso | Alta | Solo detección; verificar contexto |
| sha1 | `e66fd750c8bec06fca11b6e2919a3d66bc6c0fc1` | `StorageExplorer-windows-x64.exe` — **herramienta legítima de Microsoft** usada para mover datos a la nube, añadida en 2025. **NO BLOQUEAR por hash** | Alta | Solo detección; verificar contexto |
| sha1 | `b26cfde4ca74d5d5377889bba5b60b5fc72dda75` | `Advanced IP Scanner` — **herramienta legítima** de escaneo de red, listada por el aviso | Alta | Solo detección; verificar contexto |
| sha1 | `3477a173e2c1005a81d042802ab0f22cc12a4d55` | `Advanced Port Scanner` — **herramienta legítima**, mismo caso | Alta | Solo detección; verificar contexto |
| sha1 | `39950150074e5b22d0ef0c30ab4c72287e003908` | `advanced_ip_scanner.exe` — **herramienta legítima**, mismo caso | Alta | Solo detección; verificar contexto |
| sha1 | `1f76997e8a902c1cd3b1e6c68f17f694c61c5445` | `conhost.exe` — variante del cifrador (aviso `AA23-319A`) | Alta | Bloqueo y retrohunt |
| sha1 | `e5d4a2e704ee880273aa4e8114fe9927b0019ff8` | `c:\s$\conhost.exe` — cifrador en ruta de recurso compartido administrativo | Alta | Bloqueo y retrohunt |
| sha1 | `a506fd44ee7a6d16fe8929201bc7887b966d6d14` | `1.exe` (aviso `AA23-319A`) | Alta | Bloqueo y retrohunt |
| sha1 | `ae90d0819ab92e6a1bf7bfab1fa9057221bc0b3a` | `main.dll` (aviso `AA23-319A`) | Alta | Bloqueo y retrohunt |
| domain | `776c5589[.]schedule[.]newhomessection[.]com` | **El único dominio publicado en el aviso vigente.** En una operación como servicio la infraestructura es del afiliado y rota con él | Media | Bloqueo con validación |
| url | `hxxps://oij89jiiuguygh[.]blob[.]core[.]windows[.]net/` | Almacenamiento en la nube usado para mover datos. **Dominio base legítimo de Microsoft: bloquear el subdominio, nunca `blob.core.windows.net`** | Alta | Bloqueo de subdominio |
| url | `hxxps://e57thgdfge[.]blob[.]core[.]windows[.]net/` | Almacenamiento en la nube usado para mover datos, mismo caso | Alta | Bloqueo de subdominio |
| email | `rhysidaeverywhere@onionmail[.]org` | Cuenta de contacto del grupo (aviso `AA23-319A`) | Alta | Detección |
| email | `rhysidaofficial@onionmail[.]org` | Cuenta de contacto del grupo (aviso `AA23-319A`) | Alta | Detección |
| email | `[Nombre][Apellido]@onionmail[.]org` | **Formato con que el grupo construye sus cuentas de contacto.** El patrón vale más que las dos direcciones concretas | Alta | Detección |
| ruta | `C:\in` · `C:\out` · `C:\out\PSTools.zip\` | Directorios de preparación del adversario (aviso `AA23-319A`) | Alta | Detección |
| ruta | `C:\Windows\Temp\conhost.exe` | Destino al que `S_1.bat` copia el cifrador en cada equipo | Alta | Detección |
| ruta | `%AppData%\Local\Temp\1.ps1` | Ubicación del script con la lista de extensiones, lanzado por `powershell_ise.exe` | Alta | Detección |
| ruta | `C:\Users\Public\bg.jpg` | Imagen para sustituir el fondo de escritorio (CronUp, may-2023) | Alta | Detección |
| mutex | `CriticalBreachDetected` | **Nombre de la nota de rescate en PDF**, y cadena en claro dentro del binario: sirve como firma de contenido | Alta | Detección |
| mutex | `.rhysida` | Extensión añadida a los ficheros cifrados | Alta | Detección |
| mutex | `Rhysida-0.1` | Cadena con que el binario se identifica internamente (`T1587`) | Alta | Detección |

## Anexo B — Fuentes y valoración

> Valoración doble tipo Admiralty/OTAN: **fiabilidad de la fuente (A–F)** ×
> **credibilidad de la información (1–6)**. Se valoran por separado.

| Fuente | Disciplina | Fiabilidad | Credibilidad | Notas de sesgo |
|---|---|---|---|---|
| FBI · CISA · MS-ISAC — aviso conjunto `AA23-319A`, «#StopRansomware: Rhysida Ransomware» (15-nov-2023, revisado el 30-abr-2025) | OSINT gubernamental | A | 1 | **La fuente de referencia del informe:** cadena completa, tablas ATT&CK, indicadores, mitigaciones, con investigaciones hasta diciembre de 2024 y agradecimiento a Sophos. **Cuatro salvedades:** su revisión **retiró los indicadores de 2023**; describe el esquema de cifrado de forma internamente inconsistente; **no incluye táctica de persistencia ni de exfiltración** en un grupo de doble extorsión; y publica como indicadores los hashes de toda la suite `PsTools`, que es software legítimo, sin distinguirlos de lo malicioso más que en una advertencia general |
| CronUp — «Ejército de Chile es atacado por la nueva banda de ransomware Rhysida» (29-may-2023, con actualizaciones el 3, 5 y 9 de junio) | OSINT comercial nacional | B | 2 | **La única fuente del caso chileno con seguimiento en tiempo real, y por tanto insustituible.** Aporta la cronología día a día, el comportamiento del portal de extorsión, el nombre de la nota, la imagen de fondo y el estado temprano de desarrollo de las muestras. **Es ejemplarmente clara en una cosa que muchos informes no hacen: advierte que la muestra que publica NO es la del Ejército.** No publica fecha de autoría, no firma con nombre, no da vector de entrada ni volumen, y sus actualizaciones sobre la detención citan prensa |
| IBM X-Force — «Interlock and Rhysida within the ransomware ecosystem», Golo Mühr (12-jun-2026) | OSINT comercial / TECHINT | B | 2 | **La fuente más reciente y la que sitúa el ecosistema de afiliados:** `Vanilla Tempest`, `Broomstick`/`Oyster`/`CleanUpLoader`, `Supper`, `Endico`, el criptador `Tomb`, la interrupción de Microsoft de septiembre de 2025 y la cifra de unas ochenta víctimas en 2025. Declara sus confianzas con precisión y **recoge la de Cisco Talos sobre Interlock como «baja»**, que es como se cita aquí. No describe el cifrado de Rhysida ni su victimología regional |
| Universidad Kookmin y KISA — método de descifrado y herramienta (feb-2024), con artículo académico | Académica / gubernamental | B | 1 | **Trabajo con artículo publicado y herramienta distribuida por una agencia nacional.** Documenta el fallo del generador pseudoaleatorio y sus tres límites —solo cifrador de Windows, no ESXi ni PowerShell—. Citado aquí a través de coberturas de prensa especializada y del resumen del artículo; **el artículo completo no se leyó** (brecha `G-5`) |
| ransomware.live — página del grupo, consultada el 16-nov-2026 | OSINT · agregador | C | 3 | **La única fuente de la distribución global:** 317 víctimas, 42 países, desglose por sector y por país, media de 37,6 días entre ataque y reclamación. **Mide lo que el grupo publica, no los incidentes:** excluye a quien pagó antes e incluye reclamaciones no verificadas. Sus cifras cambian cada día, y las de este informe son del día de consulta. El listado completo de víctimas solo se pudo leer en parte |
| Help Net Security — «Berlin refuses to be blackmailed after network breach», Sinisa Markovic (1-sep-2026) | OSINT · prensa especializada | B | 2 | **La fuente del caso de Berlín, y la mejor de las disponibles sobre él:** cita a las autoridades del estado por su cargo y a prensa alemana de referencia para la cifra del rescate. **Distingue con claridad lo confirmado por las autoridades de lo reclamado por el atacante**, que es exactamente lo que hace falta en un caso así. No da indicadores ni vector de entrada |
| BleepingComputer y prensa chilena — cobertura del caso del Ejército (may–jun 2023) | OSINT · prensa especializada y general | C | 3 | Fuente de la cifra de **360 000 documentos** —atribuida al recuento de un investigador chileno— y de los detalles de la detención. **Cifras de origen adversario y hechos procesales sin resolución conocida.** Una fuente en español publicó afirmaciones sobre el contenido de lo filtrado —material de inteligencia, despliegues— **que no se han podido corroborar y que este informe no adopta** |
| MITRE ATT&CK — marco de referencia | Marco | A | 1 | El aviso declara usar Enterprise v17; este informe nombra las técnicas con v18 y señala en §T-2 los huecos de la fuente en lugar de rellenarlos con mapeo propio |

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

## Anexo D — Qué preguntar antes del incidente, y a quién

> Este anexo es una lista de comprobación previa, no una guía de respuesta. Existe porque
> las seis decisiones de §E-4 se toman mal el día del incidente y bien seis meses antes.
> Cada fila tiene un dueño que no es el SOC.

| Pregunta | Quién la responde | Por qué, en este expediente |
|---|---|---|
| ¿Qué accesos remotos tenemos sin segundo factor, y cuándo dejan de tenerlo? | Identidad y Redes | `KJ-4`: es el acceso inicial documentado por el aviso conjunto |
| ¿Cuánto tarda de verdad una restauración hasta tener servicio? | Continuidad y TI | `KJ-5`: si el cifrado corre, es lo único que queda. Y no se sabe sin probarlo |
| ¿Nuestras copias son alcanzables con credenciales de dominio? | Continuidad y TI | El grupo vuelca `NTDS.dit`. Una copia alcanzable con esas credenciales no es una copia |
| ¿Pagamos o no pagamos, y quién lo decide? | Consejo, con Legal | `KJ-7`: Berlín se negó y los datos se publicaron íntegros. La decisión se toma en frío o no se toma |
| ¿Quién queda **fuera** de la lista de distribución del incidente, y con qué criterio? | CISO, Legal y RR. HH. | `KJ-3`: en el caso chileno hubo una detención dentro de la institución víctima |
| ¿Cómo preservamos la evidencia con cadena de custodia desde la primera hora? | CISO y Legal | Si hay implicación interna, la evidencia es material judicial desde el minuto uno |
| ¿Qué decimos públicamente, cuándo y con qué instrucciones operativas? | Asuntos Corporativos | El Ejército comunicó al segundo día con instrucciones ejecutables. Eso se prepara antes |
| ¿Qué proveedores tienen nuestros datos o acceso a nuestra red, y los vigilamos en los sitios de filtración? | Compras y Célula CTI | `H-13`: el escenario más probable es que el incidente lo sufra un tercero |
| ¿A quién notificamos, en qué plazo y con qué contenido? | Legal y Cumplimiento | Los plazos de notificación de la normativa chilena vigente —alerta temprana, informe y detalle— deben estar en el manual, con la referencia normativa verificada por Legal y no por seguridad |
| ¿Está por escrito que no contamos con un descifrador? | Continuidad | `KJ-5` y decisión `E-e`. Coste cero, y evita una hipótesis de lotería dentro del plan |

## Anexo E — Marcos de referencia empleados

`MITRE ATT&CK v18` (el aviso conjunto declara v17) · `MITRE D3FEND` · `Cyber Kill Chain` ·
`Pirámide del Dolor` · `Modelo del Diamante` · `F3EAD` · `ICD 203` (lenguaje estimativo) ·
`ACH, supuestos clave, pre-mortem` · `TLP 2.0` · `PAP` · `STIX 2.1 / TAXII 2.1` ·
`Admiralty Code` · `CISA Cross-Sector Cybersecurity Performance Goals` (referenciados por el aviso)

## Anexo F — Paquete legible por máquina

- Bundle STIX 2.1: pendiente de generar. Debe modelar **un `intrusion-set` para la operación y objetos separados para los afiliados y actores de acceso** (`Vanilla Tempest` y los cargadores `Gootloader`, `Endico`, `Broomstick`, `Supper`), con relaciones `uses` y no `related-to`: la distinción entre el dueño del cifrador y su clientela es la que hace útil el modelo, y fundirlos repetiría el error que §O-1 advierte.
- **Las relaciones con `Vice Society` e `Interlock` deben llevar la confianza que declara su fuente** —«similitudes» en un caso, confianza baja en el otro—, no una relación afirmativa.
- **Todos los `indicator` correspondientes a herramientas legítimas deben llevar marcado explícito «solo detección»**: la suite `PsTools` completa, `StorageExplorer`, `Advanced IP Scanner` y `Advanced Port Scanner`. Es el segundo producto de esta serie, tras `CTI-2026-021`, donde mezclar las listas provocaría una interrupción, y aquí el riesgo es mayor porque lo que se bloquearía es la herramienta con la que se administra el parque.
- El aviso conjunto publica **paquetes STIX propios en XML y JSON para las dos versiones** (noviembre de 2023 y abril de 2025): ingerir **ambos**, porque la versión nueva retiró indicadores que la antigua conserva (brecha `G-4`).
- Evento MISP: pendiente. Taxonomías: `tlp`, `pap`, `admiralty-scale`, `estimative-language`, más etiquetas propias `extorsion:doble`, `raas`, `victima:chile` y `caso:ejercito-2023`.
- Reglas: las dos reglas Sigma de §X-4 y las doce plantillas de §X-3, versionadas con el identificador `CTI-2026-024`. **La regla del borrado de registros se marca `stable`**; las demás, `experimental`. `D-1` queda bloqueada hasta que exista el inventario de `X-1`, y debe registrarse así en el sistema de reglas en lugar de publicarse sin su lista.
- **Lista de bloqueo y lista de detección separadas, con revisión obligatoria de un segundo analista antes de publicar la de bloqueo.** En este expediente, un error de clasificación bloquea `PsExec`.

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-11-16 | Emisión inicial. Elaborado sobre un aviso conjunto del FBI, CISA y MS-ISAC en sus dos versiones comparadas, el seguimiento en tiempo real de una firma chilena, un informe de proveedor de junio de 2026, el trabajo académico del descifrador de 2024 y la consulta directa de un agregador de sitios de filtración. **El caso del Ejército de Chile se desarrolla como estudio de caso (§E-5)** por ser la única víctima chilena documentada de la serie, con la advertencia expresa de que no tiene fuente oficial, que las cifras de volumen son del atacante y que la implicación de la persona detenida está en fase judicial sin sentencia conocida. **Se incorpora una dimensión que los otros informes de extorsión de la cartera no tratan —el riesgo de persona interna en la respuesta— por lo ocurrido en ese caso** (`KJ-3`, decisión `E-c`). El episodio del descifrador de 2024 se presenta como argumento **contra** apoyar la recuperación en la esperanza (`KJ-5`, decisión `E-e`). Sin telemetría propia: §O-4 sin evaluar | Célula CTI |

## Anexo H — Realimentación del consumidor

| Pregunta | Respuesta |
|---|---|
| ¿Respondió a su requisito? | |
| ¿Qué decisión tomó o cambió con este informe? | |
| ¿Se completó el inventario de accesos remotos sin segundo factor (X-1)? ¿Cuántos había? | |
| ¿Se desplegó el segundo factor sin excepciones (E-a)? ¿Cuántas excepciones se concedieron? | |
| ¿Se hizo la prueba real de restauración (E-b)? ¿Cuánto tardó hasta tener servicio? | |
| ¿Se revisó el procedimiento de extorsión con hipótesis de persona interna (E-c)? | |
| ¿Existe ya una decisión escrita sobre el pago, aprobada por el Consejo (E-d)? | |
| ¿Se probó el restablecimiento doble de `KRBTGT` (E-f)? | |
