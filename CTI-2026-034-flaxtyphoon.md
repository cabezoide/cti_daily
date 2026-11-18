---
tlp: "TLP:CLEAR"
pap: "PAP:AMBER"
id: "CTI-2026-034"
version: "1.0"
tipo: "Perfil de actor estatal por contrato + evaluación de un modelo de negocio con ánimo de lucro + identificación de un eje de exposición regional que atraviesa tres informes de esta cartera"
foco_regional: "**Paraguay es el único caso sudamericano confirmado**, anunciado por su propio Gobierno en noviembre de 2024 y ampliado en julio de 2026. Y el motivo lo dijo su presidente: es el único país de Sudamérica que reconoce a Taiwán. La afirmación de actividad en 2026 contra infraestructura portuaria, telecomunicaciones y energía en Perú y Chile **no la sostiene ninguna fuente pública**"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "Flax Typhoon · Ethereal Panda · RedJuliett · Storm-0919 · habilitados por el Integrity Technology Group (Yongxin Zhicheng), designado por la OFAC, el Reino Unido y la Unión Europea"
fecha: "2026-11-17"
caduca: "2027-02-17"
autor: "Célula CTI"
distribucion: "Elaborado íntegramente con fuentes abiertas TLP:CLEAR, con el aviso conjunto AA26-281A de diez organizaciones de siete países —entre ellas el Centro Nacional de Inteligencia de España— leído en original, incluidos sus anexos. Difusión libre, conservando la atribución de las fuentes y las salvedades metodológicas de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-034

## Una empresa con ánimo de lucro, mil trescientos guiones de escaneo y una vulnerabilidad de **2014**: el actor estatal menos sofisticado de esta cartera, y exactamente por eso el que tiene más probabilidades de alcanzarnos

### Las ocho vulnerabilidades que el aviso conjunto confirma como **explotadas con éxito** van de 2014 a 2023, todas con parche publicado hace años. No hay ni un día cero. Lo que hay es **escala industrial**: escaneo masivo, pulverización de contraseñas contra el correo, y una VPN legítima para quedarse

#### Y el único caso sudamericano confirmado es **Paraguay**, cuyo presidente dijo públicamente por qué: es el único país de Sudamérica que reconoce a Taiwán. **La exposición regional de este actor no sigue a los puertos ni a los calendarios electorales: sigue a la cuestión taiwanesa** — y su persistencia más duradera conocida vivió un año entero dentro de un servidor de información geográfica

> **Regla de oro del producto:** todo párrafo debe responder a un requisito de
> inteligencia (PIR) y habilitar una decisión. Si un párrafo no cambia lo que
> alguien va a hacer, va al anexo o se borra.

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-034` |
| Versión / fecha | `1.0` — 2026-11-17 (emisión inicial) |
| Tipo de producto | Perfil de **actor estatal operado por una empresa con ánimo de lucro** —el modelo de *hacking* por contrato, documentado con sanciones y con un aviso conjunto—, más evaluación del eje de selección regional, más **identificación de un patrón que atraviesa tres informes de esta cartera**: el geoespacial |
| Niveles cubiertos | Estratégico · Operacional · Táctico · Técnico |
| Foco regional | **Paraguay, confirmado y por partida doble** (noviembre de 2024 y julio de 2026), anunciado por el propio Gobierno paraguayo. **Y una corrección**: la actividad contra Perú y Chile que afirmaba el requisito no está sostenida por ninguna fuente pública localizada |
| Marcado de difusión | `TLP:CLEAR` · `PAP:AMBER` |
| Clasificación interna | Sin clasificar. Fuente principal gubernamental y pública |
| Requisitos atendidos | `PIR-01`, `PIR-09` (superficie expuesta y gestión de parches), `PIR-10` (ecosistema de contratistas ofensivos y efecto de las sanciones), `PIR-11` (plataformas sectoriales fuera del inventario de TI), `RFI-2026-11-A` |
| Solicitante / consumidor primario | Dirección, Jefatura de SOC y **el área responsable de los sistemas de información geográfica**, que en la mayoría de las organizaciones de la región no depende de TI y es destinatario directo de `E-c` |
| Ventana de observación | 2017-01-01 → 2026-11-17. **Ventanas densas:** enero de 2021 en adelante (acceso inicial según el aviso), noviembre de 2024 (caso paraguayo), mediados de 2024 a septiembre de 2025 (compromiso de ArcGIS), octubre de 2026 (aviso conjunto e incautación) |
| Base de colección | Nueve fuentes externas, **una primaria gubernamental multinacional leída en original con sus dos anexos**. Sin telemetría propia |
| Autor (analista) | Célula CTI |
| Revisión por pares | Pendiente |
| Aprobación | Pendiente |
| Caducidad / revisión | 2027-02-17 (92 días). **Revisión anticipada si se publica un caso confirmado en otro país de la región**, y en particular en cualquiera de los que reconocen a Taiwán |
| Productos relacionados | `CTI-2026-030` (Salt Typhoon: el otro actor chino de infraestructura de red de esta cartera, **y el contraste entre ambos es instructivo**) · `CTI-2026-033` (StrikeShark: **comparte FScan, y comparte el eje geoespacial**) · `CTI-2026-023` (Machete: el tercer informe del eje geoespacial) · `CTI-2026-017` y `CTI-2026-027` (FamousSparrow, Mustang Panda) · `CTI-2026-018` (abuso de TLD: la infraestructura de este actor usa servicios de DNS dinámico) |
| Paquete legible por máquina | **El aviso publica su propio paquete STIX 2.1, en XML y en JSON, y es la fuente preferente para ingesta.** El Anexo A de este informe es una selección razonada para lectura humana, subordinada al original, por el mismo criterio que `CTI-2026-030` |

> ⚠ **Limitación estructural, y una advertencia sobre la naturaleza del sujeto.**
> **Sin telemetría propia:** `O-4` es un cuestionario. Y hay una ambigüedad
> deliberada en la fuente que hay que trasladar íntegra: el aviso conjunto **no
> habla de «Flax Typhoon»**, habla de «los actores de amenaza habilitados por
> el Integrity Technology Group», y precisa que esos actores usan tácticas,
> técnicas y procedimientos **consistentes con** la actividad conocida
> públicamente como Flax Typhoon, Ethereal Panda y Red Juliett, **entre otras**
> — añadiendo que esos actores **también pueden realizar actividad no asociada
> a la empresa**. Esa formulación no es prudencia retórica: es la descripción de
> un ecosistema de suministro, y está en `O-1` y en `O-2`.

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** Este expediente no describe un grupo: describe **un proveedor**. El aviso conjunto AA26-281A, publicado el 8 de octubre de 2026 por diez organizaciones de siete países, atribuye la actividad a actores **habilitados por el Integrity Technology Group**, una empresa china con ánimo de lucro y vínculos con su Gobierno, que según el Tesoro de EE. UU. proporcionó infraestructura a Flax Typhoon entre el verano de 2022 y el otoño de 2023 y controló la red de bots *Raptor Train* desde mediados de 2021. Valoramos **casi con certeza** *(≥99 %)* que el modelo operativo sea de contratación y no de unidad orgánica. **Confianza: alta.** *Base:* aviso conjunto gubernamental multinacional A-1, más designaciones de sanciones de tres jurisdicciones.

**KJ-2.** **No hay un solo día cero en todo el expediente.** Las ocho vulnerabilidades que el aviso confirma como explotadas con éxito van de `CVE-2014-6278` —un fallo de GNU Bash de 2014— a `CVE-2023-22894`, y cinco de ellas se incorporaron al catálogo de vulnerabilidades explotadas conocidas de CISA con motivo de este aviso. El acceso inicial se obtiene con utilidades de línea de comandos construidas sobre código de explotación en Python y Go, ataques de *cross-site scripting* y pulverización de contraseñas contra servidores de correo. Valoramos **casi con certeza** *(≥99 %)* que la capacidad de explotación de este actor sea de nivel ordinario. **Confianza: alta.** *Base:* el anexo B del aviso, que lista producto, versión y tipo de vulnerabilidad de cada una.

**KJ-3.** Y eso lo hace **más** peligroso para nosotros, no menos. Un actor que depende de días cero ataca a quien le interesa; **un actor que escanea Internet con mil trescientos guiones y explota fallos de hace diez años alcanza a quien se descuida**, y eso incluye a cualquier organización de la región con un servicio expuesto sin parchear. La propia composición de su utillaje —nueve herramientas públicas de escaneo, puertos 21, 22, 53, 80, 443 y 1080— describe una operación de volumen. Valoramos **probable** *(55–80 %)* que existan víctimas latinoamericanas no identificadas públicamente. **Confianza: moderada.** *Base:* el modelo de selección por barrido, más la confirmación de que el aviso sólo cubre lo observado en investigaciones del FBI.

**KJ-4.** El único caso sudamericano confirmado es **Paraguay**, y el criterio de selección lo declaró públicamente su propio presidente: **la posición del país en defensa de Taiwán**. En noviembre de 2024, el Ministerio de Tecnologías de la Información y Comunicación paraguayo y la Embajada de EE. UU. anunciaron, tras una revisión conjunta con participación del Comando Sur estadounidense, la identificación de Flax Typhoon dentro de sistemas del Estado; en julio de 2026 una declaración conjunta nueva señaló la presencia de **varios** actores vinculados al Gobierno chino en sistemas estatales paraguayos. Valoramos **probable** *(55–80 %)* que el reconocimiento diplomático de Taiwán sea el criterio dominante de selección de este actor en el hemisferio. **Confianza: moderada.** *Base:* un caso confirmado y una declaración política de parte interesada; es una muestra de uno, y así se trata.

**KJ-5.** **La afirmación de que en 2026 este actor opera contra infraestructura portuaria, telecomunicaciones, energía y el ciclo electoral en Perú y Chile no está sostenida por ninguna fuente pública que hayamos localizado**, y el aviso conjunto señala expresamente como geografías afectadas el sudeste asiático, África y Norteamérica. Valoramos **poco probable** *(20–45 %)* que exista un caso confirmado y no publicado de esa clase. **Confianza: moderada.** *Base:* ausencia de evidencia en colección dirigida, en inglés y en español; y la observación de que el mecanismo de selección que sí está documentado —la cuestión taiwanesa— apunta en dirección contraria, porque tanto Perú como Chile mantienen relaciones con Pekín.

**KJ-6.** **La persistencia más duradera documentada de este actor vivió un año dentro de un servidor de información geográfica, y no hubo ninguna vulnerabilidad.** ReliaQuest documentó en octubre de 2025 un compromiso que, con **confianza moderada**, atribuye a este actor: entrada con credenciales válidas de un administrador de portal en un servidor ArcGIS expuesto, conversión de una extensión de objeto de servidor en Java en una interfaz web de administración remota, protegida con una clave fija para que nadie más pudiera usarla, **y preservada automáticamente en las copias de seguridad**, de modo que sobrevivió a restauraciones completas. Valoramos **muy probable** *(80–95 %)* que esa técnica sea reutilizable contra despliegues equivalentes en la región. **Confianza: moderada-alta.** *Base:* fuente única de proveedor con confianza moderada declarada, pero mecanismo completamente descrito y no dependiente de ningún fallo de software.

**KJ-7.** Hay un **eje geoespacial** que ya atraviesa tres informes de esta cartera, y merece tratarse como hallazgo propio: `CTI-2026-023` documenta un actor que roba cartografía y datos de sistemas de información geográfica militares andinos; `CTI-2026-033` documenta que la víctima colombiana de otro clúster se comprometió por un **GeoServer** sin parchear; y este informe documenta un año de persistencia en un **ArcGIS**. Valoramos **probable** *(55–80 %)* que las plataformas geoespaciales constituyan una superficie de ataque sistemáticamente desatendida en la región, por una razón organizativa y no técnica: **las administra el área de cartografía, catastro, minería o ambiente, no el área de sistemas**, y por eso quedan fuera del inventario de aplicaciones y del ciclo de parcheo. **Confianza: moderada.** *Base:* tres casos independientes y un mecanismo organizativo plausible; no es una medición.

**Qué cambiaría estos juicios.** **(a)** Un caso confirmado en Perú, Chile, Colombia o Ecuador, que invalidaría `KJ-5` y, si no guarda relación con Taiwán, también `KJ-4`. **(b)** Evidencia de uso de un día cero por este actor, que cambiaría `KJ-2` y con él toda la estrategia de `E-4`, que descansa en el parcheo. **(c)** La publicación de que la incautación de dominios de octubre de 2026 no degradó la operación —el propio aviso advierte que la empresa conserva capacidad de reconstruir su infraestructura—, que confirmaría que las sanciones y las incautaciones no son contención. **(d)** Un cuarto caso del eje geoespacial, que convertiría `KJ-7` de patrón en requisito de inventario sectorial.

---

## 2. Resumen ejecutivo

Conviene empezar por lo que este actor **no** es, porque la palabra «Typhoon» en el nombre arrastra una expectativa que el expediente no cumple.

No es un equipo de élite. No usa días cero. Las ocho vulnerabilidades que el aviso conjunto de octubre de 2026 confirma como explotadas con éxito son un fallo de GNU Bash de **2014**, uno de un servidor FTP de 2015, uno del servidor DNS más usado del mundo de 2015, uno de Apache Struts de 2016, uno de un concentrador VPN de 2019, uno de GitLab y uno de un servidor de documentos de 2021, y uno de un gestor de contenidos de 2023. Todas tienen parche publicado hace años. Cinco de las ocho se incorporaron al catálogo oficial de vulnerabilidades explotadas conocidas **con motivo de este aviso**, es decir: hasta octubre de 2026 no constaba oficialmente que alguien las estuviera usando.

**Lo que sí es, es una empresa.** El aviso no habla de un grupo: habla de «los actores de amenaza habilitados por el Integrity Technology Group», una compañía china con ánimo de lucro y vínculos con su Gobierno que, según el Tesoro estadounidense, suministró infraestructura a Flax Typhoon y controló desde mediados de 2021 una red de bots de centenares de miles de dispositivos domésticos. Esa compañía está sancionada por Estados Unidos desde enero de 2025, por el Reino Unido desde ese mismo año y por la Unión Europea desde marzo de 2026. Y su producto tiene aspecto de producto: **MicroScan**, una aplicación web en Python con más de mil trescientos guiones de pruebas de intrusión, **con panel de cuenta y lista de vulnerabilidades detectadas**. El aviso reproduce una captura de ese panel. Es software de escaneo con interfaz de cliente.

**El modelo de negocio está a la vista en los detalles técnicos**, y es la parte más reveladora del expediente. El actor roba correo masivamente, lo comprime, lo cifra, lo sube, y **mantiene una aplicación web propia que da acceso a terceros al contenido robado**, con argumentos en la URL para consultar las cuentas de interés. En algunos casos restringió el acceso a lo exfiltrado a direcciones IP **de Xiamen, en China**. Eso no es espionaje con un consumidor: es un almacén con clientes.

**Y hay una conclusión contraintuitiva que es el eje de este informe:** la falta de sofisticación de este actor lo hace **más** probable para nosotros, no menos. Un adversario que necesita un día cero elige a sus víctimas; uno que escanea Internet con mil trescientos guiones y explota fallos de hace una década **encuentra** a sus víctimas, y el criterio de encuentro es estar expuesto y sin parchear. Eso sitúa a cualquier organización de la región dentro del universo alcanzable, con independencia de su interés estratégico.

**Sobre la región, hay un caso confirmado y no es ninguno de los que el requisito afirmaba.** Es **Paraguay**: en noviembre de 2024 su Ministerio de Tecnologías de la Información y Comunicación, junto con la Embajada de Estados Unidos y tras una revisión conjunta con participación del Comando Sur, anunció la identificación de Flax Typhoon dentro de sistemas del Estado paraguayo; el ministro habló de «infiltración» y de que hacía suponer «un monitoreo de actividades», y el ministerio no aclaró qué sistemas estaban comprometidos. En julio de 2026 una declaración conjunta posterior señaló la presencia de varios actores vinculados al Gobierno chino en sistemas estatales. **Y el presidente paraguayo atribuyó públicamente el espionaje a la posición de su país en defensa de Taiwán.**

Esa atribución política, viniendo de parte interesada, hay que tomarla con la cautela que corresponde — pero tiene una propiedad valiosa: **es una hipótesis de selección falsable y con consecuencias de priorización**. Si el criterio es la cuestión taiwanesa, Paraguay es un objetivo permanente y Perú o Chile lo son mucho menos, lo que contradice directamente lo que el requisito afirmaba. Y si el criterio es ése, el indicador de alerta temprana para cualquier país de la región no es técnico: es diplomático.

**Por último, el hallazgo que no estaba en el requisito y que probablemente sea lo más útil de este documento.** La persistencia más duradera que se ha documentado de este actor no fue un *rootkit* ni un implante: fue **una extensión de un servidor de información geográfica**. Entró con credenciales válidas de administrador en un ArcGIS expuesto a Internet, convirtió una extensión legítima en una consola de administración remota, le puso una clave fija para que ningún otro pudiera usarla, y se quedó **más de un año** — sobreviviendo a restauraciones completas del sistema, porque la plataforma incluye sus extensiones en las copias de seguridad. No hubo vulnerabilidad: hubo una credencial y un diseño.

Y eso completa un patrón que esta cartera ya tiene a medias. `CTI-2026-023` describe un actor que roba cartografía militar andina. `CTI-2026-033` describe una víctima colombiana comprometida por un GeoServer sin parchear. Este informe añade un año de persistencia en un ArcGIS. **Tres informes, tres actores sin relación entre sí, un mismo tipo de plataforma** — y una explicación organizativa simple: en casi toda la administración y la gran empresa de la región, los sistemas de información geográfica los administra el área de cartografía, de catastro, de minería o de ambiente, **no el área de sistemas**, y por eso no están en el inventario de aplicaciones ni en el ciclo de parcheo de nadie.

<!-- cti:cards -->

| Rasgo | Qué significa | Etiqueta |
|---|---|---|
| Un contratista con ánimo de lucro, no una unidad | **La disuasión que funciona con un Estado no funciona con un proveedor.** Y las sanciones, aplicadas por tres jurisdicciones desde 2025, no lo han detenido: el aviso es de 2026 | `01 · modelo de negocio` |
| Cero días cero, y una vulnerabilidad de 2014 | La capacidad de explotación es ordinaria. **Toda la defensa cabe en el ciclo de parcheo**, y eso es una noticia extraordinariamente buena si se actúa | `02 · nivel técnico` |
| Escala industrial: 1.300 guiones y panel de cliente | **Encuentra víctimas, no las elige.** Estar expuesto y sin parchear es el criterio completo de selección | `03 · volumen` |
| Vende o comparte lo robado | Aplicación web propia para dar acceso de terceros al correo robado, y restricción de acceso a direcciones de Xiamen. **Hay un cliente al otro lado** | `04 · el almacén` |
| Una VPN legítima como persistencia | SoftEther, renombrada a nombres de procesos de Windows y configurada para reconectar al arrancar. **El EDR no la marca porque no es malware** | `05 · persistencia` |
| Un año dentro de un servidor de mapas | Sin vulnerabilidad: credencial válida, extensión legítima convertida en consola, clave fija y supervivencia a las copias de seguridad | `06 · el eje geoespacial` |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `8` | Vulnerabilidades confirmadas como **explotadas con éxito** | **Cinco se añadieron al catálogo oficial de explotadas conocidas con este aviso.** Ninguna es un día cero |
| `2014` | Año de la más antigua de ellas | `CVE-2014-6278`, GNU Bash. **Doce años con parche disponible** |
| `>1.300` | Guiones de prueba de intrusión en la aplicación MicroScan | Usada por estos actores **desde al menos 2017**. Con panel de cuenta y lista de vulnerabilidades detectadas |
| `10` | Organizaciones firmantes del aviso conjunto | De **siete países**. Una de ellas es el **Centro Nacional de Inteligencia de España**: el único firmante hispanohablante, y **ninguno latinoamericano** |
| `7` | Dominios incautados por el FBI el 8 de octubre de 2026 | Soportaban dos herramientas: **MicroScan** y **FishHub** |
| `1` | Casos sudamericanos confirmados | **Paraguay**, anunciado por su propio Gobierno en noviembre de 2024 y ampliado en julio de 2026 |
| `>1 año` | Duración de la persistencia en el servidor ArcGIS | Desde mediados de 2024 hasta septiembre de 2025, **sin vulnerabilidad y sobreviviendo a restauraciones completas** |
| `3` | Informes de esta cartera con eje geoespacial | `CTI-2026-023`, `CTI-2026-033` y este. **Tres actores sin relación entre sí** |

> ✅ **Decisiones que se solicitan, con plazo.**
> **(a) 7 días:** contrastar las ocho vulnerabilidades del Anexo A.1 contra el inventario expuesto. Son ocho, tienen parche y cinco acaban de entrar en el catálogo oficial de explotadas (`E-a`).
> **(b) 14 días:** buscar SoftEther en el parque, y cualquier cliente de VPN de terceros que reconecte al arrancar. **No es malware y por eso el EDR no lo marca** (`E-b`).
> **(c) 14 días, y es la decisión propia de este informe:** inventariar **toda plataforma geoespacial** —ArcGIS, GeoServer, nodos de infraestructura de datos espaciales, visores catastrales—, identificar quién la administra y revisar sus extensiones y sus cuentas de administrador. **Es la decisión que `CTI-2026-033` ya pedía y que este informe convierte en patrón** (`E-c`).
> **(d) 30 días:** exigir autenticación multifactor en **todas** las interfaces de correo que el aviso enumera, no sólo en la web (`E-d`).
> **(e) 30 días:** revisar si las copias de seguridad de las plataformas sectoriales preservan complementos y extensiones, porque ahí la restauración **reinstala al adversario** (`E-e`).
> **(f) 45 días:** ingerir el paquete STIX del aviso, que es extenso y la fuente preferente, en lugar de transcribir indicadores a mano (`E-f`).

---

## 3. Alcance, requisitos y limitaciones

**3.1 Requisitos de inteligencia atendidos**

| Req. | Enunciado | ¿Respondido? | Dónde |
|---|---|---|---|
| PIR-01 | ¿Qué actores tienen intención y capacidad contra nuestra región? | **Sí, y con un criterio de selección identificado y falsable** | `KJ-4`, `E-2`, `O-3` |
| PIR-09 | ¿Qué superficie expuesta nos convierte en alcanzables? | **Sí, con ocho vulnerabilidades concretas** | `A.1`, `E-a` |
| PIR-10 | ¿Cómo opera el ecosistema de contratistas ofensivos, y sirven las sanciones? | **Sí, y la respuesta sobre las sanciones es incómoda** | `KJ-1`, `E-1`, `O-3.A` |
| PIR-11 | ¿Qué plataformas sectoriales quedan fuera del inventario de TI y son alcanzables? | **Sí, y es el hallazgo propio del informe** | `KJ-6`, `KJ-7`, `E-c`, `Anexo D` |
| RFI-2026-11-A | El requisito afirmaba actividad en Perú y Chile contra puertos, telecomunicaciones, energía y el ciclo electoral. ¿Se sostiene? | **No.** Véase `3.5` | `KJ-5`, `3.5` |
| PIR-04 | ¿Nos afecta? | **No.** Requiere telemetría propia | `O-4`, sin evaluar |

**3.2 Fuera de alcance.** No se evalúan: la red de bots *Raptor Train* en su detalle técnico, desarticulada en septiembre de 2024 y cubierta por fuentes de entonces que no son el objeto de este informe; la política de sanciones y su eficacia general, más allá de la observación de `E-1`; la actividad de este actor contra Taiwán, que es su foco principal y está bien documentada, salvo lo necesario para establecer el criterio de selección; la relación de este actor con los otros clústeres chinos de esta cartera, para la que no hay evidencia pública de solapamiento; y la atribución estatal en su última milla, que está establecida por designaciones de tres jurisdicciones y por un aviso conjunto de siete países.

**3.3 Limitaciones de la colección.** Seis.

1. **Sin telemetría propia.** `O-4` es un cuestionario.
2. **El aviso cubre lo observado en investigaciones del FBI**, y lo declara: la información proviene de evidencia técnica recuperada en múltiples investigaciones relativas a la empresa. No es un censo de la actividad del actor.
3. **El aviso no habla de Latinoamérica.** Enumera sectores de infraestructura crítica estadounidense y, como geografías adicionales, el sudeste asiático, África y Norteamérica. **La ausencia de la región en un documento de siete países es un dato, y de los más relevantes del informe**, pero es ausencia de evidencia y no evidencia de ausencia.
4. **El caso paraguayo se conoce por comunicación oficial, no por informe técnico.** No hay indicadores, ni cadena de intrusión, ni sectores concretos: el propio ministerio no aclaró qué sistemas estaban comprometidos. Y la atribución del motivo —Taiwán— la hizo el presidente del país afectado, que es parte interesada.
5. **El caso de ArcGIS es de fuente única y con confianza moderada declarada.** El proveedor que lo publicó se declara seguro de que el actor es un APT chino y con **confianza moderada** de que sea este actor concreto. Se usa así.
6. **No hay detalle público sobre FishHub.** La segunda herramienta cuyos dominios se incautaron en octubre de 2026 no aparece descrita en el aviso conjunto que hemos leído; su nombre procede de la cobertura de la incautación. Es la brecha `G-5`.

**3.4 Metodología.** ICD 203. Código Admiralty doble (Anexo B). **MITRE ATT&CK v19**, que es la versión que usa el aviso y que este informe hereda. Pirámide del Dolor. ACH y pre-mortem en `O-6`. **Y una técnica estructurada propia: la búsqueda deliberada de patrones entre informes de la cartera**, que produjo `KJ-7` y cuyo método está en el Anexo D.

**3.5 Lo que el requisito afirmaba, y lo que las fuentes sostienen**

<!-- cti:table highlight="NO corroborado|Corregido|Parcial" -->

| # | Afirmación del requisito | Veredicto | Qué dicen las fuentes |
|---|---|---|---|
| 1 | «Flax Typhoon (Ethereal Panda / RedJuliett)… para Perú y Chile en 2026 es fundamental» | **NO corroborado** | Ninguna fuente pública localizada documenta actividad de este actor en Perú o Chile. El único caso sudamericano confirmado es **Paraguay** |
| 2 | «Especialmente en torno a infraestructura portuaria como Chancay, telecomunicaciones, energía y el ciclo electoral peruano de 2026» | **NO corroborado** | Ninguna fuente pública localizada vincula a este actor con el puerto de Chancay, con el sector eléctrico peruano ni con el ciclo electoral de 2026. **Son afirmaciones concretas y verificables, y no se verifican** |
| 3 | «Su modelo de comprometer dispositivos de borde, cámaras IP y routers SOHO para construir botnets de retransmisión ORB» | **Corroborado para el pasado, con matiz importante** | La red de bots existió y fue desarticulada en **septiembre de 2024**; las fuentes discrepan sobre su tamaño, entre más de 200.000 y más de 260.000 dispositivos. **Pero el aviso de 2026 no describe ese modelo como el vector principal**: describe escaneo, *cross-site scripting*, pulverización de contraseñas y SoftEther. El modelo de red de bots es parte del expediente, **no es el método vigente documentado** |
| 4 | «Tiene alta presencia en redes de telecomunicaciones y gobiernos sudamericanos» | **NO corroborado para telecomunicaciones; corroborado para UN gobierno** | Gobiernos sudamericanos: **Paraguay, confirmado**. Telecomunicaciones sudamericanas: sin evidencia. **Y conviene separar este actor de `CTI-2026-030`**, que sí es el actor de las telecomunicaciones y no es éste |
| 5 | «Complementa tu informe de Salt Typhoon» | **Corroborado como juicio de cartera, y el contraste es útil** | Son complementarios precisamente porque son opuestos: uno vive en los routers de los operadores con oficio artesanal; **éste escanea Internet en masa y explota fallos de hace diez años**. Confundirlos produce la defensa equivocada en los dos casos |

> ⚠ **Por qué la corrección del punto 3 importa más de lo que parece.** La
> diferencia entre «construye redes de retransmisión con dispositivos de borde»
> y «escanea, pulveriza contraseñas e instala una VPN legítima» no es de matiz:
> **son dos programas de defensa distintos**. El primero lleva a mirar los
> routers domésticos y las cámaras de los proveedores; el segundo, a parchear
> ocho cosas, a exigir doble factor en diez interfaces de correo y a buscar
> SoftEther. El primero es, además, casi inaccionable para una organización
> normal —no controlamos los routers de los clientes de nuestro operador—; el
> segundo cabe entero en un plan de treinta días. **La red de bots es cierta y
> es historia; el método vigente documentado es otro.**

---

# NIVEL ESTRATÉGICO
### Para: Consejo · CISO · Riesgo · Legal · Horizonte: 6–24 meses

## E-1. Qué representa un actor estatal que es una empresa

Esta cartera tiene varios actores estatales y un solo suministrador nombrado hasta ahora. Aquí el suministrador **es** el expediente, y eso cambia tres cosas que normalmente se dan por supuestas.

**La primera: la motivación es doble y no coincide.** Un servicio de inteligencia ataca lo que le interesa a su Estado. Una empresa que vende acceso ataca **lo que puede vender**, que incluye lo que le interesa al Estado pero no se limita a ello. Esa diferencia explica por sí sola la forma del expediente: mil trescientos guiones de escaneo, nueve herramientas públicas, puertos genéricos, y una aplicación web para dar a terceros acceso al correo robado. Nada de eso tiene sentido como operación de inteligencia dirigida; todo lo tiene como **inventario de mercancía**. Y el aviso recoge la consecuencia con precisión: los actores habilitados por la empresa **también pueden realizar actividad no asociada a la empresa**. Es decir, el proveedor y sus clientes no son lo mismo, y la actividad de unos contamina la atribución de los otros.

**La segunda: la disuasión no aplica igual.** Las medidas que se diseñan contra un Estado —atribución pública, sanciones, presión diplomática— se dirigen a un actor que tiene costes reputacionales y objetivos políticos. Una empresa sancionada tiene un problema de negocio, no de legitimidad. Y el expediente permite medir el efecto: la empresa fue designada por la OFAC en **enero de 2025**, por el Reino Unido ese mismo año y por la Unión Europea en **marzo de 2026**; su red de bots fue desarticulada en septiembre de 2024; y en **octubre de 2026** siete países tuvieron que publicar un aviso conjunto sobre su actividad en curso e incautar siete dominios. **La cadena de medidas no ha producido cese.** El propio aviso, según la cobertura, advierte que la empresa conserva capacidad de reconstruir su infraestructura.

**La tercera: la atribución se vuelve estructuralmente más difícil, y el aviso lo dice en una nota que conviene leer.** Señala que las empresas de ciberseguridad tienen métodos distintos de rastrear y atribuir actores, y que **esos métodos pueden no tener una correspondencia uno a uno con la metodología y el entendimiento del Gobierno de EE. UU.** para toda la actividad relacionada con estas agrupaciones. Traducido: cuando varios actores comparten un proveedor de herramientas e infraestructura, los clústeres que los proveedores de seguridad dibujan por solapamiento de infraestructura **pueden estar dibujando al proveedor y no al operador**. Es el mismo problema que `CTI-2026-030` documenta desde otro ángulo.

<!-- cti:cards -->

| Cambio estructural | Por qué nos afecta | Etiqueta |
|---|---|---|
| El acceso es una mercancía con catálogo | Mil trescientos guiones, panel de cuenta, aplicación web para clientes. **Lo que nos convierte en objetivo no es nuestro interés estratégico: es nuestro inventario sin parchear** | `01 · mercado` |
| Tres jurisdicciones de sanciones, y sigue operando | **La sanción no es contención.** Es útil para otras cosas —cumplimiento, atribución, coste de infraestructura— pero no debe contabilizarse como mitigación en ninguna matriz de riesgo | `02 · límites de la política` |
| El solapamiento de infraestructura puede ser del proveedor | **Dos actores que comparten servidores pueden no tener nada que ver entre sí**: pueden tener el mismo contratista. El aviso lo advierte explícitamente | `03 · atribución` |
| Correo robado en un almacén accesible a terceros | La exfiltración no termina en el adversario. **Nuestro correo robado puede tener varios consumidores sucesivos**, con consecuencias de notificación y de riesgo que duran años | `04 · el dato robado circula` |
| La capacidad técnica es ordinaria | **Toda la defensa cabe en el parcheo, el doble factor y el inventario.** Es, de todos los informes de esta cartera, el que pide las medidas más convencionales | `05 · la buena noticia` |
| Ningún firmante latinoamericano en el aviso | Siete países, diez organizaciones, **ninguna de la región**, y el único firmante hispanohablante es español. **Eso es una brecha de capacidad regional, no una ausencia de amenaza** | `06 · quién avisa` |

## E-2. Victimología, y el criterio de selección

<!-- cti:bars title="Sectores que el aviso conjunto nombra como afectados (presencia declarada, no recuento de víctimas)" -->

| Sector | Presencia declarada |
|---|---|
| Servicios e instalaciones gubernamentales | `1` |
| Manufactura crítica | `1` |
| Salud y salud pública | `1` |
| Tecnologías de la información | `1` |
| Fuerzas del orden | `1` |
| Educación | `1` |
| Organizaciones religiosas | `1` |

> ⚠ **Ese gráfico es deliberadamente plano, y la planitud es el mensaje.** El
> aviso enumera siete categorías de víctima sin jerarquía ni cifras, y añade
> organizaciones en el sudeste asiático, África y Norteamérica. **No hay perfil
> sectorial.** La presencia de organizaciones religiosas y educativas junto a
> manufactura crítica y fuerzas del orden no describe una prioridad de
> inteligencia: describe **lo que cabe en una red de barrido**. Un actor que
> selecciona por vulnerabilidad expuesta produce exactamente esta distribución.

**Y sin embargo hay un criterio de selección, al menos en el hemisferio, y es político.** El caso paraguayo es el único sudamericano confirmado, y su presidente lo atribuyó públicamente a la posición de su país en defensa de Taiwán. Paraguay es, en efecto, **el único país de Sudamérica que mantiene relaciones diplomáticas con Taipéi y no con Pekín**, y eso convierte una coincidencia en una hipótesis con mecanismo.

**La consecuencia práctica de esa hipótesis es de priorización y conviene enunciarla con cuidado**, porque es cómoda y las conclusiones cómodas merecen desconfianza. Si el criterio dominante es la cuestión taiwanesa, entonces: Paraguay es un objetivo permanente; los países de la región que reconocen a Taipéi —en el hemisferio, además de Paraguay, varios Estados centroamericanos y caribeños— están en la misma categoría; y Perú, Chile, Colombia y Ecuador, que mantienen relaciones con Pekín, son mucho menos probables **como objetivos dirigidos**. Pero eso no los saca del universo de `KJ-3`: siguen siendo perfectamente alcanzables como víctimas **encontradas** por barrido, y en ese caso el motivo no sería geopolítico sino que el correo de una organización cualquiera también se vende.

**Dicho de otro modo, y es la lectura que este informe recomienda:** el eje taiwanés predice **quién recibirá atención dirigida**; el estado del parcheo predice **quién será alcanzado de todos modos**. La primera pregunta no la controlamos. La segunda, sí.

## E-3. Tendencia y pronóstico

<!-- cti:chart title="Cronología de medidas públicas contra el proveedor, y continuidad de la actividad" cap="El eje mide número acumulado de medidas públicas relevantes —desarticulación, designaciones, aviso conjunto, incautación—. La actividad no cesa en ningún punto de la serie: es el argumento de E-1." -->

| Periodo | Medidas acumuladas |
|---|---|
| `Sep·24` | `1` |
| `Ene·25` | `2` |
| `2025` | `3` |
| `Mar·26` | `4` |
| `Oct·26` | `6` |

Las seis medidas de la serie son: la desarticulación de la red de bots en septiembre de 2024; la designación de la OFAC en enero de 2025; la designación británica de 2025; la incorporación a la lista de la Unión Europea en marzo de 2026; y, en octubre de 2026, el aviso conjunto de siete países y la incautación de siete dominios. **Entre la primera y la última hay dos años, y la última existe porque la actividad continúa.**

<!-- cti:cards -->

| Escenario | Desarrollo | Etiqueta |
|---|---|---|
| **Más probable** | La empresa reconstruye infraestructura y continúa, con el mismo modelo: escaneo masivo, vulnerabilidades públicas, pulverización de contraseñas y VPN legítima para persistir. La lista de vulnerabilidades explotadas se amplía con lo que se publique, con meses de retraso | `Probable · 55–80 %` |
| **Alternativa creíble** | La presión acumulada desplaza el negocio a otros proveedores del mismo ecosistema, con nombres nuevos y los mismos métodos. **Para la defensa sería indistinguible**, y es la razón de que `E-4` no mencione al proveedor en ninguna de sus medidas | `Posibilidad real · 45–55 %` |
| **La que importa para la región** | Un caso confirmado en un país de la región que **no** reconozca a Taiwán, lo que falsaría `KJ-4` y obligaría a rehacer el criterio de selección. Sería el desarrollo más informativo posible | `Poco probable · 20–45 %` |
| **La que importa para el inventario** | Un cuarto caso del eje geoespacial, en cualquier actor. **Convertiría `KJ-7` en requisito de inventario sectorial** y probablemente justificaría un producto propio sobre esa superficie | `Posibilidad real · 45–55 %` |
| **Descartado, y se consigna** | Que este actor sea un adversario de capacidad excepcional al que no se pueda cerrar la puerta. **El anexo B del aviso lo falsa: ocho vulnerabilidades, la más nueva de 2023, todas con parche.** Se consigna porque el nombre del actor invita a lo contrario | `Descartada` |

## E-4. Decisiones que este informe pide al nivel estratégico

<!-- cti:table highlight="geoespacial|SoftEther|7 días" -->

| # | Decisión | Fundamento | Plazo |
|---|---|---|---|
| E-a | **Contrastar las ocho vulnerabilidades del Anexo A.1 contra el inventario expuesto** y cerrar las vivas. Son ocho, no trece ni cien | `KJ-2`. **Cinco acaban de entrar en el catálogo oficial de vulnerabilidades explotadas conocidas**, lo que les da prioridad formal además de técnica | 7 días |
| E-b | **Buscar SoftEther en todo el parque**, y en general cualquier cliente de VPN de terceros configurado para reconectar al arrancar | `KJ-1`. **No es malware y el EDR no lo marca.** Es la persistencia preferente de este actor y la más fácil de pasar por alto | 14 días |
| E-c | **Inventariar toda plataforma geoespacial**, identificar quién la administra, revisar sus extensiones y complementos, y auditar sus cuentas de administrador y su exposición a Internet | `KJ-6`, `KJ-7`. **Es la decisión propia de este informe**, y la pedía ya `CTI-2026-033` desde otro expediente. La pregunta de quién la administra es tan importante como la de qué versión tiene | 14 días |
| E-d | **Exigir autenticación multifactor en todas las interfaces de correo** que el aviso enumera —no sólo en la interfaz web— y comprobar que no queda ninguna accesible con sólo contraseña | `KJ-2`. La herramienta de pulverización que usa el actor ataca **diez interfaces distintas** del mismo servidor, y basta con que una siga abierta | 30 días |
| E-e | Revisar si las copias de seguridad de las plataformas sectoriales **preservan complementos y extensiones** | `KJ-6`. En el caso de ArcGIS, **la restauración completa reinstalaba la puerta trasera**. Es una propiedad del diseño de la plataforma, no un fallo | 30 días |
| E-f | **Ingerir el paquete STIX del aviso**, en lugar de transcribir indicadores a mano | `E-1`. El anexo de indicadores del aviso es muy extenso y está mantenido por sus firmantes. Transcribirlo a mano garantiza errores | 45 días |
| E-g | **Decisión de Dirección:** posición sobre el riesgo de que el correo corporativo exfiltrado circule entre terceros durante años, y sus consecuencias de notificación, de secreto profesional y de relación con clientes | `E-1`. El actor mantiene una aplicación web que da acceso de terceros al correo robado. **Eso convierte una brecha de confidencialidad en un riesgo con cola larga** | 60 días |
| E-h | **No contabilizar las sanciones ni las incautaciones como mitigación** en ninguna matriz de riesgo que mencione a este actor | `E-1`, `E-3`. Dos años de medidas y la actividad continúa. Es higiene de evaluación de riesgo | Inmediato |

---

# NIVEL OPERACIONAL
### Para: Jefatura de SOC · Respuesta a Incidentes · Threat Hunting · Horizonte: semanas–meses

## O-1. Identificación y alias

| Designación | Origen | Qué designa | Grado de equivalencia |
|---|---|---|---|
| `Integrity Technology Group` · `Yongxin Zhicheng` | Designaciones de la OFAC, el Reino Unido y la Unión Europea; aviso conjunto | **La empresa.** Compañía china con ánimo de lucro y vínculos con su Gobierno, que adquiere o construye herramientas, adquiere y aloja infraestructura, y compromete redes | **Es el sujeto del aviso conjunto.** No es un alias de actor: es un proveedor |
| `Flax Typhoon` | Microsoft | Clúster de actividad | **El aviso dice que los actores habilitados por la empresa usan TTP «consistentes con» esta actividad, «entre otras».** No dice que sean lo mismo |
| `Ethereal Panda` | CrowdStrike | Clúster de actividad | **Misma formulación.** Consistente con, no equivalente a |
| `Red Juliett` / `RedJuliett` | Recorded Future | Clúster de actividad, con foco documentado en Taiwán | **Misma formulación** |
| `Storm-0919` | Microsoft | Designación de clúster en desarrollo | Referencia |
| `Raptor Train` | Lumen Black Lotus Labs | **La red de bots**, no el actor. Desarticulada en septiembre de 2024; el Tesoro afirma que la empresa la controlaba desde mediados de 2021 usando direcciones de China Unicom en Pekín | **Es infraestructura, no un grupo** |
| `MicroScan` · `FishHub` | Aviso conjunto e incautación de octubre de 2026 | **Herramientas.** Siete dominios incautados el 8 de octubre de 2026 las soportaban | **Son productos, no actores** |

> ⚠ **Nota de *tradecraft*, y es el motivo de que esta tabla tenga la columna
> que tiene.** El aviso conjunto se cuida de no decir «Flax Typhoon» como
> sujeto. Dice «los actores de amenaza habilitados por el Integrity Technology
> Group», y añade dos salvedades que esta cartera recoge íntegras: que esos
> actores **también pueden realizar actividad no asociada a la empresa**, y que
> los métodos de rastreo y atribución de las empresas de seguridad **pueden no
> tener correspondencia uno a uno** con los del Gobierno estadounidense.
>
> Eso significa que «Flax Typhoon» puede estar nombrando, según quién lo use,
> tres cosas distintas: un operador, el conjunto de clientes de un proveedor, o
> la infraestructura del proveedor. **Y cuando un alias puede nombrar al
> proveedor, el solapamiento de infraestructura deja de ser evidencia de que
> dos actividades son del mismo actor** — que es, exactamente, el error que
> `CTI-2026-030` documenta en otro expediente. Es la misma lección por una vía
> nueva: aquí el alias no se infló, **se compartió**.

## O-2. Estructura y atribución

| Eje de atribución | Valoración | Confianza |
|---|---|---|
| Existencia y papel de la empresa | **Establecido por vía oficial en tres jurisdicciones.** Designada por la OFAC el 3 de enero de 2025, por el Reino Unido en 2025 y por la Unión Europea en marzo de 2026 | **Alta** |
| Vínculo de la empresa con el Gobierno chino | **Establecido por el aviso conjunto**, que la describe como empresa con ánimo de lucro con vínculos con el Gobierno chino | **Alta** |
| Que la actividad del aviso sea «Flax Typhoon» | **Consistencia de TTP, no identidad.** El propio aviso lo formula así y advierte de las dos salvedades de `O-1` | Moderada |
| Suministro de infraestructura a Flax Typhoon | **Establecido por el Tesoro:** entre el verano de 2022 y el otoño de 2023 | Alta |
| Control de la red de bots | **Establecido por el Tesoro:** desde mediados de 2021, usando direcciones de China Unicom en Pekín | Alta |
| Que el caso paraguayo sea de este actor | **Afirmado por el Gobierno paraguayo y la Embajada de EE. UU.** tras una revisión conjunta con participación del Comando Sur | Moderada-alta |
| Que el motivo del caso paraguayo sea Taiwán | **Afirmado por el presidente de Paraguay.** Declaración política de parte interesada, con mecanismo plausible y sin corroboración técnica | Moderada |
| Que el compromiso de ArcGIS sea de este actor | **Confianza moderada declarada por el proveedor** que lo publicó, que se declara seguro de que es un APT chino y moderadamente seguro de que es éste | Moderada |
| Identidad nominal | **Ninguna.** Según la cobertura, la acción de octubre de 2026 **no incluyó acusaciones penales contra personas nombradas** | Baja |

*Razonamiento:* hay un detalle técnico que vale más que varios párrafos de atribución y que el aviso menciona de pasada: en algunos casos, **el actor restringió el acceso a los datos exfiltrados a direcciones IP de Xiamen, China**. Eso no es una huella de código ni un solapamiento de infraestructura: es una lista de control de acceso que alguien configuró para que sólo sus colegas pudieran leer el botín, y que señala la ubicación de esos colegas.

*Contraargumento que hay que mantener vivo:* precisamente porque el modelo es de suministro, cualquier atribución apoyada en infraestructura compartida es sospechosa. Si dos campañas usan servidores de la misma empresa, lo que comparten es el proveedor. **La atribución en este expediente debe apoyarse en comportamiento operativo y no en infraestructura**, y eso es una inversión del orden habitual.

## O-3. Modelo de operación

### O-3.A — El producto, y lo que revela

Hay dos piezas en el expediente que no son malware y que describen el negocio mejor que ninguna cadena de intrusión.

**MicroScan.** Una aplicación web en Python, en uso por estos actores **desde al menos 2017**, que contiene más de **mil trescientos guiones de pruebas de intrusión** escritos para escanear sitios web buscando vulnerabilidades concretas, con servicios objetivo que incluyen OpenSSL, Oracle WebLogic, Rejetto, WordPress, Juniper ScreenOS, Jenkins y Apache Struts. Y —el detalle que lo convierte en producto— **tiene panel de cuenta con la lista de vulnerabilidades detectadas**; el aviso reproduce una captura. Un panel de cuenta implica cuentas, y las cuentas implican usuarios distintos del desarrollador.

**La aplicación web de consulta del correo robado.** El aviso dice que los actores **mantienen una aplicación web propia que proporciona acceso de terceros al contenido de correo robado**, y que sus usuarios pueden pasar argumentos concretos en la URL para ver el correo de cuentas específicas. Esto es la cara de cliente del negocio: no un canal de exfiltración, sino **un servicio de consulta sobre lo ya exfiltrado**.

> **Lo que estas dos piezas significan para una víctima, y es una consecuencia
> que conviene llevar a Dirección.** Si el correo robado vive en una aplicación
> de consulta con acceso de terceros, entonces **el daño no termina con la
> expulsión del adversario**. La información sigue disponible, para
> destinatarios que la víctima no conoce, durante un plazo indefinido. Para una
> organización con secreto profesional, con información de clientes o con
> negociaciones en curso, eso cambia la evaluación del incidente: no es una
> brecha con fecha de cierre. Es `E-g`.

### O-3.B — La cadena, en una frase por fase

**Reconocimiento.** Nueve herramientas públicas de escaneo —BBScan, dirsearch, Fscan, ksubdomain, masscan, NMAP, OneForAll, ShuiZe y wpscan—, más MicroScan. Concentración en los puertos 21, 22, 53, 80, 443 y 1080; con dirsearch, enumeración de páginas PHP y ASP. El aviso hace una observación interpretativa valiosa: **el uso de herramientas abiertas típicamente alojadas en GitHub sugiere que los actores tienden a buscar objetivos más vulnerables**.

**Acceso inicial.** Desde al menos mediados de enero de 2021, principalmente mediante utilidades de línea de comandos construidas sobre código de explotación escrito en Python y en Go. Y una vía distinta y poco habitual: **JavaScript y HTML para ataques de *cross-site scripting* contra terceros**, usando aplicaciones de terceros vulnerables para modificar el contenido de una página y atacar a otras víctimas. El FBI recuperó una de esas cargas: ejecutada en un sitio vulnerable, **añade campos de usuario y contraseña a la página** para cosechar credenciales; después de que la víctima introduzca cualquier cosa, genera un enlace de descarga de un fichero comprimido protegido con contraseña, cuyo contenido sale de bytes codificados dentro de la propia carga y contiene un ejecutable. Ese ejecutable arranca un proceso con **el nombre de un servicio legítimo de Windows**, establece comunicaciones cifradas sobre HTTP con un dominio atribuido a la empresa, y contiene funciones para consultar datos de buzones de correo.

**Credenciales.** EBurst, una herramienta abierta en Python, para pulverización y adivinación de contraseñas contra cuentas de correo, **a través de diez interfaces distintas del mismo servidor**: panel de control, servicios web, libreta de direcciones sin conexión, acceso web, llamada a procedimiento remoto, interfaz de programación, interfaz de mensajería, PowerShell, autodescubrimiento y sincronización activa. El aviso añade una instrucción explícita a los defensores: **incluir esas interfaces al defenderse**. Es la base de `E-d`.

**Persistencia.** Clientes de **SoftEther**, una VPN legítima, instalados en los equipos de la víctima para ofuscar el mando y control. Se descargan con PowerShell o binarios del propio sistema en Windows, y con `curl` o `wget` en Linux y Unix; se configuran para **reconectar automáticamente al arrancar**; y se renombran a `conhost.exe` o `dllhost.exe` para parecer ejecutables comunes de Windows. El aviso señala el motivo con franqueza: **el software de detección de endpoint es menos probable que lo marque, porque SoftEther es una VPN legítima**.

**Recolección y exfiltración.** Descarga de bases de datos y extracción manual de correo, con nombres de fichero discretos para minimizar la detección del volcado —imágenes, hojas de estilo, guiones—. Un bot en PHP que habla con la interfaz de servicios web de Exchange, sube el correo a un servidor remoto, ofusca los directorios que crea y **cambia el nombre de su proceso hijo**. Una herramienta que ejecuta la técnica de replicación de controlador de dominio para copiar credenciales, pertenencias a grupos y relaciones de confianza. Y una utilidad de línea de comandos para acceder de forma continuada a buzones en la nube mediante ficheros de configuración con identificador de cliente, de inquilino y secreto — es decir, **con credenciales de aplicación, que no disparan alertas de inicio de sesión**.

### O-3.C — El caso del servidor de información geográfica

Merece sección aparte porque es el único componente del expediente que **no encaja en el modelo industrial** y porque es el hallazgo más transferible a la región.

Según el proveedor que lo publicó en octubre de 2025, la intrusión empezó con **una cuenta de administrador de portal comprometida** en un servidor ArcGIS expuesto a Internet, vinculado a otro servidor interno. **No hubo ninguna vulnerabilidad**: hubo credenciales válidas. Con ellas, el actor modificó una **extensión de objeto de servidor en Java** —un mecanismo legítimo y documentado de la plataforma para ampliar su funcionalidad— convirtiéndola en una consola de administración remota funcional. Le añadió **una clave fija**, de modo que ni otros atacantes ni los propios administradores curiosos pudieran usarla. Y aquí está la parte que convierte el caso en una lección de arquitectura: **porque la plataforma incluye rutinariamente todas sus extensiones en las copias de seguridad, la puerta trasera se preservaba automáticamente incluso después de restauraciones completas del sistema**. El acceso duró más de un año.

> ⚠ **Las tres propiedades de este caso, y ninguna es específica de ArcGIS.**
> **(1) El punto de entrada fue una credencial**, no un fallo: ningún programa
> de parcheo lo habría evitado. **(2) La persistencia fue una funcionalidad
> legítima de la plataforma**, de modo que ningún antivirus tenía nada que
> marcar. **(3) La copia de seguridad era parte del mecanismo de persistencia**,
> lo que invierte la medida de recuperación más básica que existe: restaurar
> **reinstalaba** al adversario.
>
> Cualquier plataforma empresarial extensible con el mismo diseño —y son
> muchas: gestores de contenidos, plataformas de integración, servidores de
> aplicaciones, sistemas de gestión documental— admite el mismo patrón. **La
> pregunta que hay que llevarse de aquí no es «¿tenemos ArcGIS?», es «¿qué
> plataformas nuestras admiten extensiones, quién puede instalarlas, y las
> incluye la copia de seguridad?»**. Es `E-c` y `E-e`.

## O-4. Nuestra exposición

> ⬛ **Sección sin evaluar — requiere telemetría e inventario interno.** Y una
> nota: las preguntas están agrupadas por quién tiene la respuesta, porque en
> este expediente **tres de los cuatro grupos no son del SOC**.

**Superficie expuesta — responde TI y Vulnerabilidades**

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| A-1 | ¿Cuáles de las **ocho** vulnerabilidades del Anexo A.1 están vivas en servicios expuestos? | Escaneo externo · inventario | Vulnerabilidades |
| A-2 | ¿Qué tenemos escuchando en los puertos 21, 22, 53, 80, 443 y 1080 desde Internet, y hace falta que esté ahí? | Escaneo externo | Redes · TI |
| A-3 | ¿Tenemos aplicaciones web con vulnerabilidades de *cross-site scripting* sin corregir, especialmente en páginas de acceso? | Análisis de aplicaciones | Desarrollo |

**Plataformas sectoriales — responde el área dueña, no TI. Es `E-c`**

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| B-1 | **¿Qué plataformas geoespaciales tenemos —ArcGIS, GeoServer, nodos de datos espaciales, visores catastrales—, en qué versión y quién las administra?** | Inventario · entrevista | TI · área geoespacial |
| B-2 | ¿Alguna está expuesta a Internet? ¿Está vinculada a un servidor interno? | Escaneo externo · arquitectura | TI · área geoespacial |
| B-3 | **¿Qué extensiones y complementos tiene instalados cada una, y quién los instaló?** | Consola de la plataforma | área geoespacial |
| B-4 | ¿Cuántas cuentas de administrador de portal existen, con qué contraseñas y con qué segundo factor? | Consola de la plataforma | área geoespacial |
| B-5 | **¿Incluyen las copias de seguridad de esas plataformas sus extensiones?** Si sí, restaurar puede reinstalar lo que se quería eliminar | Procedimiento de respaldo | TI · área geoespacial |
| B-6 | ¿Qué otras plataformas nuestras admiten extensiones de terceros con el mismo modelo? | Inventario de aplicaciones | Arquitectura |

**Correo e identidad — responde Sistemas y Seguridad**

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| C-1 | ¿Está exigido el segundo factor en **las diez interfaces** de correo del Anexo A.4, o sólo en la web? | Configuración | Sistemas |
| C-2 | ¿Detectamos pulverización de contraseñas en interfaces distintas de la web, como la sincronización activa o el autodescubrimiento? | Registros de autenticación | SOC |
| C-3 | ¿Qué aplicaciones registradas tienen permisos de lectura de buzón, con qué secreto y desde cuándo? **El actor usa credenciales de aplicación, que no generan eventos de inicio de sesión** | Consola de identidad | Sistemas · SOC |
| C-4 | ¿Hay alertas de replicación de controlador de dominio desde equipos que no son controladores? | Registros de directorio | SOC |

**Persistencia — responde SOC y TI/Puesto**

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| P-1 | **¿Existe SoftEther en algún equipo del parque?** ¿Y cualquier otro cliente de VPN de terceros? | Inventario de software · EDR | TI/Puesto |
| P-2 | ¿Hay procesos llamados `conhost.exe` o `dllhost.exe` **fuera de `C:\Windows\System32`**? | EDR | SOC |
| P-3 | ¿Hay conexiones salientes persistentes hacia servicios de DNS dinámico desde servidores? | NetFlow · DNS | SOC |

## O-5. Cronología

<!-- cti:timeline -->

| Fecha | Hecho | Traza |
|---|---|---|
| `2014-09` | Se publica `CVE-2014-6278` (GNU Bash). **Doce años después sigue en la lista de explotadas con éxito de este actor** | Global |
| `2017` | **Primer uso documentado de MicroScan** por estos actores. La aplicación de escaneo con más de 1.300 guiones | Global |
| `2021-01` | Comienzo de la ventana de acceso inicial que el aviso documenta: utilidades de línea de comandos sobre código de explotación en Python y Go | Global |
| `2021` (mediados) | **La empresa controla la red de bots** desde esta fecha, según el Tesoro, usando direcciones de China Unicom en Pekín | Global |
| `2022` (verano) → `2023` (otoño) | **Periodo en que la empresa suministró infraestructura a Flax Typhoon**, según la designación del Tesoro | Global |
| `2024` (mediados) | **Inicio del compromiso del servidor ArcGIS** que duraría más de un año | Global |
| `2024-09` | **Desarticulación de la red de bots.** Entre 200.000 y 260.000 dispositivos según la fuente | Global |
| `2024-11-26` | **PARAGUAY.** El Ministerio de Tecnologías de la Información y Comunicación y la Embajada de EE. UU. anuncian la identificación de Flax Typhoon en sistemas del Estado, tras una revisión conjunta con participación del Comando Sur. El ministro habla de «infiltración» y de «monitoreo de actividades»; **no se aclara qué sistemas** | **LATAM** |
| `2024-11` | **El presidente de Paraguay atribuye el espionaje a la posición de su país en defensa de Taiwán** | **LATAM** |
| `2025-01-03` | **La OFAC designa al Integrity Technology Group** | Global |
| `2025` | El Reino Unido sanciona a la empresa | Global |
| `2025-09` | Fin del compromiso del servidor ArcGIS: **más de un año de persistencia**, sobreviviendo a restauraciones completas | Global |
| `2025-10` | **Se publica el caso de ArcGIS**, atribuido a este actor con confianza moderada | Global |
| `2026-03` | **La Unión Europea añade a la empresa a su lista de sanciones** | Global |
| `2026-07` | **PARAGUAY, segunda vez.** Una declaración conjunta señala la presencia de **varios** actores vinculados al Gobierno chino en sistemas informáticos del Estado paraguayo | **LATAM** |
| `2026-10-08` | **Aviso conjunto AA26-281A**, de diez organizaciones de siete países —incluido el CNI de España—, e **incautación de siete dominios** que soportaban MicroScan y FishHub. **Cinco vulnerabilidades se añaden al catálogo oficial de explotadas conocidas** | Global |
| `2026-11-17` | Emisión de este informe. **Sin ningún caso confirmado en Perú, Chile, Colombia o Ecuador** | **Chile / LATAM** |

## O-6. Hipótesis alternativas consideradas

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| **H1 — El modelo es de contratación: una empresa vende acceso y herramientas** | Establecido por tres designaciones oficiales y por el propio aviso. **Y confirmado por el producto**: panel de cuenta en la herramienta de escaneo, aplicación web de consulta del correo robado | `Establecida · ≥99 %` |
| **H2 — «Flax Typhoon» nombra al proveedor y no al operador, al menos en parte** | **Consistente con la formulación deliberadamente cuidadosa del aviso** y con sus dos salvedades. Si es cierta, el solapamiento de infraestructura deja de ser evidencia de identidad de actor | `Retenida · posibilidad real 45–55 %` |
| **H3 — El criterio de selección en el hemisferio es la cuestión taiwanesa** | Consistente con el único caso confirmado y con la declaración de su presidente. **Muestra de uno**, y la atribución del motivo es de parte interesada. Falsable: un caso en un país que reconozca a Pekín la rompería | `Retenida · probable 55–80 %, confianza moderada` |
| **H4 — La región es alcanzable por barrido, con independencia de su interés estratégico** | Consistente con todo el modelo: 1.300 guiones, herramientas públicas, puertos genéricos, vulnerabilidades de hasta doce años. **No compite con H3: la complementa**, y de hecho es la que más probablemente nos afecta | `Retenida · probable 55–80 %` |
| **H5 — Hay actividad en Perú y Chile no publicada** | Sin evidencia. **Y con un argumento en contra** que no es sólo la ausencia: el mecanismo de selección documentado apunta a países que reconocen a Taipéi, y ninguno de esos dos lo hace. Se retiene sólo como caza (`I-2`) | `Poco probable · 20–45 %` |
| **H6 — La red de bots es el método vigente** | **Inconsistente con el aviso de 2026**, que describe escaneo, *cross-site scripting*, pulverización de contraseñas y VPN legítima, y no una red de retransmisión. La red existió y fue desarticulada en 2024. Se consigna porque el requisito la daba por vigente | `Descartada como método vigente` |
| **H7 — Las plataformas geoespaciales son una superficie desatendida en la región** | Consistente con tres casos independientes en tres informes de esta cartera y con un mecanismo organizativo plausible —las administra el área sectorial y no TI—. **No es una medición y así se declara** | `Retenida · probable 55–80 %, confianza moderada` |
| **H8 — Las sanciones han degradado la capacidad del proveedor** | **Inconsistente con la cronología**: seis medidas públicas en dos años y un aviso conjunto de siete países en octubre de 2026 porque la actividad continúa. Según la cobertura, el propio aviso advierte que conserva capacidad de reconstruir infraestructura | `Descartada` |

**Supuesto clave.** Que la capacidad de explotación de este actor seguirá siendo ordinaria — es decir, que seguirá sin usar días cero. **Toda la estrategia de `E-4` descansa en eso**, porque es lo que permite que el parcheo, el doble factor y el inventario sean una defensa suficiente y no un paliativo. **Qué se rompe si es falso:** si apareciera un día cero en manos de este actor, la defensa volvería a depender de detección y de respuesta, es decir del terreno caro. El falsador es `(b)` de `§1` y el disparador es `I-3`.

**Pre-mortem.** Es mayo de 2027 y este informe resultó equivocado. Los tres motivos más probables:

1. **`E-c` no se hizo porque el servidor de mapas no es de nadie.** Es la decisión propia del informe, la más original, y la que atraviesa una frontera organizativa: pedir a un área de cartografía o de catastro que audite las extensiones de su plataforma y las cuentas de administrador de su portal es una petición que no tiene cauce en la mayoría de las organizaciones. **Si se queda sin hacer, este informe habrá identificado un patrón y no habrá cerrado nada.**
2. **Se leyó «no sofisticado» como «no importante».** `KJ-3` dice exactamente lo contrario y el pre-mortem lo repite: un actor de capacidad ordinaria y alcance industrial es **más** probable que uno de élite. El riesgo de este informe es que su propio argumento central —no hay días cero— se use para archivarlo.
3. **Se tomó `H3` como garantía.** «No reconocemos a Taiwán, luego no nos buscan» es una inferencia correcta sobre el objetivo dirigido y **completamente irrelevante** frente al barrido de `H4`. Si alguien sale del informe tranquilo por el eje taiwanés, habrá leído la mitad.

## O-7. Indicadores y señales de alerta

| # | Indicador observable | Qué señalaría | Disciplina | Responsable |
|---|---|---|---|---|
| I-1 | **Un caso confirmado en un país de la región que no reconozca a Taiwán** | Falsa `H3` y obliga a rehacer el criterio de selección. **El desarrollo más informativo posible** | OSINT · CSIRT | Célula CTI |
| I-2 | Publicación de actividad de este actor en Perú, Chile, Colombia o Ecuador | Invalida `KJ-5`. Revisión del informe | OSINT · CSIRT | Célula CTI |
| I-3 | **Evidencia de uso de un día cero por este actor** | Rompe el supuesto clave y toda la estrategia de `E-4` | OSINT · avisos de fabricante | Célula CTI |
| I-4 | Ampliación de la lista de vulnerabilidades explotadas con éxito | Mantenimiento del Anexo A.1 | OSINT · catálogo oficial de explotadas | Vulnerabilidades |
| I-5 | **Un cuarto caso del eje geoespacial, en cualquier actor** | Convierte `KJ-7` en requisito de inventario sectorial y probablemente justifica un producto propio | OSINT | Célula CTI |
| I-6 | Evidencia de que la incautación de octubre de 2026 no degradó la operación | Confirma `H8` y refuerza `E-h`: la sanción no es mitigación | OSINT | Célula CTI |
| I-7 | Publicación de detalle técnico sobre **FishHub** | Cierra la brecha `G-5`: hoy sólo conocemos su nombre | OSINT | Célula CTI |
| I-8 | Un tercer anuncio paraguayo, o uno de otro país de la región que reconozca a Taipéi | Consolidaría `H3` de hipótesis a patrón | OSINT | Célula CTI |
| I-9 | Aparición de este patrón de persistencia —extensión legítima más clave fija más supervivencia en copias— en otra plataforma empresarial extensible | Generalizaría `O-3.C` y ampliaría `E-c` más allá de lo geoespacial | OSINT | Célula CTI |

---

# NIVEL TÁCTICO
### Para: Analistas de SOC · Ingeniería de Detección · Threat Hunting · Horizonte: días–semanas

## T-1. Cadena de intrusión

<!-- cti:stages title="Tres etapas, y ninguna necesita un día cero" dwell="next" -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 01 · Encontrar y entrar | Escanear Internet y empujar la puerta que lleva años abierta | **9 herramientas públicas** (BBScan, dirsearch, Fscan, ksubdomain, masscan, NMAP, OneForAll, ShuiZe, wpscan) · **MicroScan**, >1.300 guiones, con panel de cliente · puertos **21, 22, 53, 80, 443, 1080** · **8 CVE de 2014 a 2023** · *cross-site scripting* con cosecha de credenciales en la propia página · **EBurst** pulverizando contraseñas contra **10 interfaces** de correo |
| Etapa 02 · Quedarse | Una VPN legítima con nombre de proceso de Windows | **SoftEther** descargado con PowerShell o `curl`/`wget` · renombrado a `conhost.exe` o `dllhost.exe` · **configurado para reconectar al arrancar** · dominios de DNS dinámico · **el EDR no lo marca porque no es malware** · alternativa: **extensión legítima de una plataforma convertida en consola, con clave fija y preservada en las copias de seguridad** |
| Etapa 03 · Vaciar el correo | Automatizado, con nombres de fichero aburridos | bot en PHP contra la interfaz de servicios web de Exchange · **proceso hijo renombrado** · compresión y cifrado RC4 o AES-128-CBC · utilidad de línea de comandos con **credenciales de aplicación**, que no generan eventos de inicio de sesión · replicación de controlador de dominio · nombres de preparación: `001.gif`, `Include.png`, `Css.js`, `M2k.js` |

**Permanencia:** el aviso no publica mediana. **Pero el expediente contiene el único dato de permanencia verdaderamente alarmante de esta cartera**, y no viene del aviso sino del caso de `O-3.C`: **más de un año**, desde mediados de 2024 hasta septiembre de 2025, en un servidor de información geográfica, sobreviviendo a restauraciones completas del sistema. Ése es el número que hay que llevar a Dirección, no una mediana.

**Y una observación sobre la forma de esta cadena.** Las tres etapas se construyen **íntegramente con software que no es del adversario**: herramientas públicas de escaneo, exploits públicos, una VPN comercial legítima, la interfaz de servicios web del propio servidor de correo, credenciales de aplicación legítimas y una extensión documentada de una plataforma comercial. Lo único propio son MicroScan, el bot en PHP y un par de utilidades de línea de comandos. **Para una organización, eso significa que casi nada de esta cadena activará una alerta de malware**, porque casi nada de esta cadena es malware. La detección tiene que ser de **configuración y de contexto**: una VPN que no debería estar, un segundo factor que falta en una interfaz, una extensión que nadie recuerda haber instalado.

## T-2. Mapa MITRE ATT&CK

El aviso publica su propio mapeo sobre **ATT&CK v19**. La tabla siguiente lo recoge con los identificadores que el propio aviso cita en el texto, y marca como *(mapeo propio)* las filas que no proceden de él.

<!-- cti:matrix -->

| Táctica | ID | Técnica | Procedimiento observado |
|---|---|---|---|
| Reconocimiento | T1595.002 | Active Scanning: Vulnerability Scanning | **Nueve herramientas públicas de escaneo** más MicroScan, con >1.300 guiones de prueba desde al menos 2017. Concentración en los puertos 21, 22, 53, 80, 443 y 1080 |
| Desarrollo de recursos | T1588.002 | Obtain Capabilities: Tool | Herramientas abiertas de GitHub. El aviso observa que su uso **sugiere que los actores tienden a buscar objetivos más vulnerables** *(mapeo propio del juicio)* |
| Desarrollo de recursos | T1588.005 | Obtain Capabilities: Exploits | **Código de explotación público** sobre el que se construyen utilidades de línea de comandos en Python y Go *(mapeo propio)* |
| Acceso inicial | T1189 | Drive-by Compromise | **Ataques de tipo *cross-site scripting* contra terceros**, que usan aplicaciones de terceros vulnerables para modificar el contenido de una página y alcanzar a otras víctimas |
| Acceso inicial | T1190 | Exploit Public-Facing Application | Las ocho vulnerabilidades del Anexo A.1 *(mapeo propio)* |
| Acceso inicial | T1133 | External Remote Services | **Instalación de clientes de VPN en los equipos de la víctima** para ofuscar el mando y control, impidiendo además que la víctima atribuya la actividad |
| Acceso inicial | T1078 | Valid Accounts | **Cuenta de administrador de portal comprometida** en el caso del servidor ArcGIS. Sin vulnerabilidad *(fuente distinta del aviso)* |
| Ejecución | T1059.001 | PowerShell | Descarga de los instaladores de SoftEther en sistemas Windows |
| Ejecución | T1059.004 | Unix Shell | Ejecución de la utilidad de exfiltración de correo desde la línea de comandos o desde un guion de intérprete |
| Ejecución | T1059.006 | Python | Utilidades de línea de comandos construidas sobre código de explotación |
| Ejecución | T1059.007 | JavaScript | Cargas de *cross-site scripting* |
| Persistencia | T1505.004 | Server Software Component: IIS Components | **Análogo conceptual** del caso ArcGIS: extensión legítima del servidor convertida en consola de administración remota. **La técnica exacta no tiene identificador propio para esa plataforma** *(mapeo propio)* |
| Credenciales | T1110.001 | Brute Force: Password Guessing | EBurst contra cada dirección de correo suministrada |
| Credenciales | T1110.003 | Brute Force: Password Spraying | EBurst a través de **diez interfaces** del servidor de correo |
| Credenciales | T1003.006 | OS Credential Dumping: DCSync | **Replicación de controlador de dominio** mediante llamada a procedimiento remoto y servicio de replicación de directorio, para copiar credenciales, pertenencias a grupos y relaciones de confianza |
| Defensa | T1036.003 | Masquerading: Rename Legitimate Utilities | **Doble uso.** Los instaladores de SoftEther se renombran a `conhost.exe` o `dllhost.exe`; y el ejecutable de la carga de *cross-site scripting* **arranca un proceso con el nombre de un servicio legítimo de Windows** |
| Defensa | T1562 | Impair Defenses | **No por ataque, sino por elección de herramienta:** el aviso señala que el software de detección de endpoint es menos probable que marque SoftEther **porque es una VPN legítima** *(mapeo propio del razonamiento)* |
| Recolección | T1114.002 | Email Collection: Remote Email Collection | Bot en PHP contra la interfaz de servicios web de Exchange, que permite acceder a correo, calendarios y contactos |
| Recolección | T1074.001 | Data Staged: Local Data Staging | El guion busca un directorio con permiso de escritura recorriendo una lista concreta, saltando los directorios del sistema |
| Recolección | T1560.003 | Archive Collected Data: Archive via Custom Method | Compresión del correo antes de la exfiltración y cifrado con **RC4 o AES-128-CBC**, con clave y vector de inicialización fijos en el guion |
| Exfiltración | T1020 | Automated Exfiltration | El guion sube el correo a un servidor remoto de forma automatizada |
| Mando y control | T1071.001 | Application Layer Protocol: Web Protocols | Comunicaciones cifradas sobre HTTP con el dominio atribuido a la empresa |
| Mando y control | T1090 | Proxy | SoftEther como capa de ofuscación del mando y control *(mapeo propio)* |

> **Dos filas de esta tabla no son técnicas de ataque y son las más útiles.**
> `T1133` y `T1036.003`: **el adversario instala una VPN comercial legítima y
> le pone el nombre de un proceso de Windows.** No hay explotación, no hay
> malware, no hay nada que un motor de firmas pueda marcar. La detección de esa
> combinación es, literalmente, **inventario de software más una regla sobre
> nombres de proceso fuera de su directorio**, y es `D-1` y `D-2`. Son las dos
> detecciones más baratas y más eficaces del informe.

## T-3. Dónde atacamos en la Pirámide del Dolor

<!-- cti:pyramid -->

| Nivel | Qué contiene en este informe y qué vale | Valor |
|---|---|---|
| Hashes | **Casi nada, y es coherente con el actor.** Esta cadena se construye con software legítimo y herramientas públicas: no hay una familia de malware cuyos hashes perseguir. El aviso publica indicadores en su paquete STIX, pero el valor de esta capa aquí es estructuralmente bajo | Base · valor trivial |
| IP · Dominios | **Mucho volumen y poca densidad.** El anexo del aviso es extenso, con cientos de subdominios de unos pocos dominios base y servicios de DNS dinámico. **Dos observaciones valiosas:** algunos subdominios **llevan el nombre de la organización objetivo**, de modo que la propia lista de indicadores filtra a quién atacaron; y el uso de DNS dinámico significa que el bloqueo por dominio base puede afectar a terceros legítimos | Valor bajo · **pero el patrón de nombres sí informa** |
| Artefactos | **El nivel decisivo de este expediente, y no son artefactos de malware: son de configuración.** La presencia de SoftEther, un `conhost.exe` fuera de `System32`, un cliente de VPN que reconecta al arrancar, una extensión de plataforma que nadie instaló, una aplicación registrada con permisos de buzón y un secreto antiguo. **Ninguno es malicioso por naturaleza: todos son anómalos por contexto** | Valor medio · **empezar aquí** |
| Herramientas | SoftEther, PowerShell, `curl`, `wget`, nueve escáneres públicos, EBurst, la interfaz de servicios web del propio Exchange, credenciales de aplicación legítimas, extensiones documentadas de una plataforma comercial. **Todo legítimo. Todo detectable sólo por contexto** | Valor alto |
| TTP | **Tres, y la tercera es la aportación del informe.** (1) **Explotación de vulnerabilidades públicas antiguas en servicios expuestos**, que se derrota con inventario y parcheo. (2) **VPN legítima como persistencia**, que se derrota con inventario de software. (3) **Extensión legítima de una plataforma extensible convertida en consola, con clave fija y preservada por las copias de seguridad** — que no se derrota con ninguna de las anteriores y que es `E-c` y `E-e` | Cima · valor máximo |

> **La conclusión de esta pirámide es la más ortodoxa de toda la cartera, y
> conviene decirlo porque suele ser lo contrario.** Aquí la doctrina funciona
> tal cual: la base no vale casi nada, el tercer nivel es rentable, y la cima
> es donde está todo. Y hay un motivo estructural: **un adversario que no
> escribe malware no deja indicadores de malware**. Su rastro es enteramente
> de configuración y de comportamiento, de modo que la pirámide se vacía por
> abajo sola. Es, en cierto modo, el adversario que la doctrina tenía en mente.

## T-4. Hipótesis de caza prioritarias

<!-- cti:accordion critical="^(H-1|H-2|H-3)\b" regional="^H-1[0-2]\b" -->

**H-1 — Hay SoftEther, o cualquier otra VPN de terceros, en el parque.** La caza de mejor relación entre coste y conclusión del informe, y no requiere telemetría de seguridad: **basta el inventario de software**. Buscar instalaciones de SoftEther —cliente, servidor o puente—, y en general cualquier cliente de VPN de terceros que no sea el corporativo: servicios registrados, entradas de arranque, adaptadores de red virtuales, y conexiones salientes persistentes. Discriminador adicional: **configurado para reconectar automáticamente al arrancar**, que es lo que el aviso documenta. En un parque gestionado, cada acierto es investigable en minutos y la mayoría serán hallazgos de política aunque no sean este actor. Fidelidad: **muy alta**. Falsos positivos: usuarios con VPN personal, equipos de laboratorio; se enumeran.

**H-2 — Hay un `conhost.exe` o un `dllhost.exe` fuera de `C:\Windows\System32`.** La otra mitad de la anterior, y es una regla de una línea. El actor renombra los instaladores de SoftEther a esos dos nombres precisamente porque son procesos ubicuos y nadie los mira. **Un `conhost.exe` fuera de `System32` no tiene uso legítimo.** Extender la caza a procesos con nombres de binario del sistema ejecutándose desde rutas de perfil, de datos de aplicación o de temporales. Fidelidad: muy alta. Falsos positivos: prácticamente ninguno. **Es la comprobación más desproporcionadamente rentable de este informe.**

**H-3 — Hay una extensión en una plataforma sectorial que nadie recuerda haber instalado.** La caza propia de este informe, y la única que detecta `O-3.C`. No se hace en el SIEM: se hace en la consola de la plataforma, y la hace el área que la administra. Para cada plataforma geoespacial, de gestión documental, de integración o de contenidos: **enumerar todas las extensiones, complementos y componentes de servidor instalados; contrastar con la lista de lo que el área instaló deliberadamente; y revisar la fecha de instalación**. Señales de alarma: una extensión sin documentación interna; una cuyo nombre imite a una legítima; **una que requiera una clave o un parámetro para responder**, que es exactamente el mecanismo de la clave fija del caso documentado. Fidelidad: muy alta si se hace; **imposible si no la hace el área dueña**. Es `E-c` y la brecha organizativa de `T-5`.

**H-4 — Alguien pulverizó contraseñas contra una interfaz de correo que no es la web.** La herramienta que usa el actor ataca diez interfaces distintas del mismo servidor, y la mayoría de las organizaciones vigila los intentos fallidos sólo en la interfaz web. Cazar fallos de autenticación agrupados por interfaz —panel de control, servicios web, libreta de direcciones sin conexión, llamada a procedimiento remoto, interfaz de mensajería, PowerShell, autodescubrimiento y sincronización activa—, buscando el patrón característico: **muchas cuentas distintas con pocos intentos cada una**, que es lo contrario de la fuerza bruta clásica y lo que elude los bloqueos por cuenta. Fidelidad: alta. **Y el hallazgo más probable de esta caza no es un ataque: es descubrir que hay interfaces sin segundo factor**, que es `E-d`.

**H-5 — Hay una aplicación registrada con permisos de lectura de buzón que nadie reconoce.** El actor usa una utilidad de línea de comandos con ficheros de configuración que contienen identificador de cliente, identificador de inquilino y secreto. **Eso es acceso con credenciales de aplicación, que no genera eventos de inicio de sesión de usuario y no se ve en los informes de acceso.** Cazar en la consola de identidad: todas las aplicaciones registradas con permisos de lectura de correo, su propietario, la fecha de creación de su secreto y su uso reciente. Fidelidad: alta como auditoría. Falsos positivos: integraciones legítimas olvidadas, que son a su vez el hallazgo.

**H-6 — Se replicó el directorio desde un equipo que no es controlador de dominio.** Caza clásica y aquí documentada expresamente. Buscar solicitudes de replicación de directorio desde direcciones o cuentas que no correspondan a controladores de dominio. Fidelidad: muy alta. **Si esta caza acierta, el incidente ya no es un equipo: es el dominio**, y la respuesta es de otro orden.

**H-7 — Hay ficheros con nombre de imagen o de hoja de estilo que no son lo que dicen.** El actor prepara la exfiltración con nombres deliberadamente aburridos: `001.gif`, `Include.png`, `Css.js`, `M2k.js`, `M2k_list.js`, `M2k_ui_adm.js`, `All_scanner_vXX.pl.gz`. Cazar: ficheros con esas extensiones cuyo contenido real no corresponda al tipo declarado, especialmente en directorios de servidores web y en rutas con permiso de escritura; y en particular **cualquier fichero `.gif` o `.png` de tamaño desproporcionado**. Fidelidad: media-alta. Falsos positivos: pocos, y la comprobación de tipo real es automatizable.

**H-8 — Hay rastros del bot de correo en PHP en algún servidor.** Caza específica y con indicadores muy concretos. Buscar en servidores con PHP los directorios y ficheros que el guion crea: un directorio `storage/fm` con un fichero `.run` dentro, un `.run` en la raíz de ejecución, y ficheros `clientid` y `cp`. Buscar también `/var/tmp/.sess.zip`. Y, en el tráfico, peticiones a rutas de servicios web de Exchange con una cabecera de identificador de cliente no estándar. Fidelidad: muy alta por lo específico. **Y una nota de respuesta:** el guion parece ser autónomo y no instalado, de modo que su ausencia en el inventario de software no prueba nada.

**H-9 — Hubo *cross-site scripting* en una de nuestras páginas de acceso.** El vector más inusual del expediente y el que casi nadie caza. La carga que el FBI recuperó **añade campos de usuario y contraseña a una página legítima vulnerable** y después ofrece una descarga. Cazar: vulnerabilidades de *cross-site scripting* sin corregir en aplicaciones propias, con prioridad absoluta en las que tengan formularios de acceso; y en los registros del servidor web, parámetros con contenido de etiquetas de guion o con cadenas codificadas largas. Fidelidad: media. **El valor real de esta caza es preventivo: no busca al adversario, busca la puerta.**

**H-10 — Las ocho vulnerabilidades, contra nuestro perímetro.** Variante de alcance regional de `E-a`, y la más importante del informe. Son **ocho**, no trece ni cien: GNU Bash, ProFTPD, ISC BIND, Apache Struts, Pulse Connect Secure, GitLab, ONLYOFFICE DocumentServer y Strapi. Cruzarlas con el inventario expuesto y con un escaneo externo propio. **Nota de prioridad regional:** varias de ellas corresponden a software de uso muy extendido en la administración pública y en la educación superior de la región —un servidor DNS, un gestor de código, un servidor de documentos de oficina, un gestor de contenidos—, es decir, exactamente el tipo de servicio que se despliega una vez y se olvida. Fidelidad: no aplica; es inventario.

**H-11 — Las plataformas geoespaciales, en toda la región y en nuestra casa.** Caza de alcance regional, y la aportación propia de este informe. Para cada plataforma geoespacial: versión, exposición a Internet, vinculación con servidores internos, extensiones instaladas, cuentas de administrador de portal con y sin segundo factor, **y si la copia de seguridad incluye las extensiones**. Y la pregunta organizativa que precede a todas: **quién la administra**. Fidelidad: no aplica. **Contexto regional, y es el motivo de que esta caza exista:** `CTI-2026-023` documenta un actor que roba cartografía militar andina, `CTI-2026-033` una víctima colombiana comprometida por un GeoServer, y este informe un año de persistencia en un ArcGIS. **Tres actores sin relación, una misma clase de plataforma, y una misma causa organizativa.**

**H-12 — ¿Estamos en la lista de subdominios del aviso?** Caza de alcance regional con un truco de lectura. Algunos subdominios del anexo del aviso **contienen el nombre de la organización objetivo** como etiqueta. Eso convierte la lista de indicadores en una lista parcial de víctimas: cazar en ella **nuestro propio nombre, el de nuestras marcas, el de nuestros proveedores y el de nuestros clientes**, como subcadena. Fidelidad: no aplica; es una consulta de texto sobre el paquete STIX. **Coste: cinco minutos. Valor potencial: muy alto.** Es, probablemente, la comprobación más fácil de todo este informe y la que menos gente hará.

## T-5. Brechas de visibilidad que hay que cerrar primero

| Brecha | Por qué importa aquí |
|---|---|
| **Sin inventario de las plataformas sectoriales, y sin acceso de Seguridad a sus consolas** | Deja ciega `H-3` y `H-11`, que son las cazas propias del informe. **No es una brecha técnica: es organizativa**, y es la que el pre-mortem señala como más probable de no cerrarse |
| Sin inventario de software fiable | Deja ciega `H-1`. Y es la brecha más fácil de cerrar del expediente: **SoftEther aparece en cualquier inventario que exista** |
| Sin registro de autenticación desagregado por interfaz de correo | Deja ciega `H-4`. Si los fallos de autenticación se agregan sin distinguir la interfaz, la pulverización contra la sincronización activa es invisible |
| Sin auditoría de aplicaciones registradas y de sus secretos | Deja ciega `H-5`. **El acceso con credenciales de aplicación no aparece en los informes de inicio de sesión**, que es precisamente su atractivo |
| Sin escaneo externo propio y recurrente | Deja `E-a` y `H-10` dependiendo de que el inventario esté bien. **La vista del adversario es externa; la nuestra debería serlo también** |
| Sin comprobación de tipo real de fichero en servidores web | Deja ciega `H-7` |
| Sin registro de solicitudes de replicación de directorio | Deja ciega `H-6`, que es la que distingue un equipo comprometido de un dominio comprometido |
| **Sin verificar si las copias de seguridad preservan extensiones** | No es una brecha de visibilidad sino de procedimiento, y es la peor de todas: **si no se sabe, la restauración puede reinstalar al adversario** y nadie lo detectará porque la restauración es la medida de recuperación |

---

# NIVEL TÉCNICO
### Para: Ingeniería de detección · Automatización · TIP/SIEM · Vida útil: meses

## X-1. Arsenal y capacidad

| Propiedad | Valor |
|---|---|
| Escaneo | **BBScan · dirsearch · Fscan · ksubdomain · masscan · NMAP · OneForAll · ShuiZe · wpscan**, todas públicas. Puertos 21, 22, 53, 80, 443, 1080. Con dirsearch, enumeración de páginas PHP y ASP |
| Herramienta propia de escaneo | **MicroScan**: aplicación web en Python, >1.300 guiones de prueba, en uso desde al menos 2017, **con panel de cuenta y lista de vulnerabilidades detectadas**. Objetivos: OpenSSL, Oracle WebLogic, Rejetto, WordPress, Juniper ScreenOS, Jenkins, Apache Struts |
| Explotación | Utilidades de línea de comandos construidas sobre **código de explotación público** en Python y Go. **Ocho CVE confirmadas como explotadas con éxito, de 2014 a 2023. Ningún día cero** |
| Vía alternativa de acceso | **JavaScript y HTML para *cross-site scripting*, una vía poco habitual.** La carga recuperada añade campos de usuario y contraseña a una página legítima, y después ofrece la descarga de un comprimido protegido con contraseña cuyo contenido sale de bytes codificados **dentro de la propia carga** |
| Carga de la vía de *cross-site scripting* | `live700_v1.exe`, que arranca un proceso llamado **`DiagTrack.exe`** —nombre de software legítimo de Windows—, establece comunicaciones cifradas sobre HTTP con `dns.studiocloud[.]xyz`, y **contiene funciones para consultar datos de buzones de correo** |
| Credenciales | **EBurst**, herramienta abierta en Python, contra **diez interfaces** del servidor de correo: panel de control, servicios web, libreta de direcciones sin conexión, acceso web, llamada a procedimiento remoto, interfaz de programación, interfaz de mensajería, PowerShell, autodescubrimiento y sincronización activa |
| Persistencia preferente | **SoftEther**, VPN legítima. Descarga con PowerShell o binarios del sistema en Windows, con `curl` o `wget` en Linux y Unix. **Reconexión automática al arrancar.** Renombrada a `conhost.exe` o `dllhost.exe` |
| Persistencia excepcional | **Extensión de objeto de servidor en Java de una plataforma geoespacial, convertida en consola de administración remota**, con clave fija y **preservada automáticamente en las copias de seguridad** |
| Bot de correo | Guion en PHP (`Curlc4.txt`) contra la interfaz de servicios web de Exchange. **Renombra su proceso hijo a `crypto`.** Busca directorio con permiso de escritura recorriendo `/`, `/home`, `/var/www`, `/usr`, `/var/tmp`, **saltando** `/bin`, `/boot`, `/dev`, `/etc`, `/run`, `/proc`, `/sys`, `/var` y `/tmp`. Comprime y cifra con **RC4 o AES-128-CBC**, con clave y vector de inicialización **fijos en el guion** |
| Exfiltración de nube | Utilidad de línea de comandos con ficheros de configuración JSON —identificador de cliente, de inquilino y secreto— en un directorio `config`, y volcado en un subdirectorio `dump`. **Acceso con credenciales de aplicación: no genera eventos de inicio de sesión de usuario** |
| Credenciales de dominio | Herramienta que ejecuta **replicación de controlador de dominio** mediante llamada a procedimiento remoto y servicio de replicación, usando una lista de unos diecinueve identificadores de objeto de atributos del directorio |
| Servicio al cliente | **Aplicación web propia que da acceso de terceros al correo robado**, con argumentos en la URL para consultar cuentas concretas. En algunos casos, **acceso restringido a direcciones IP de Xiamen, China** |
| Infraestructura | Dominios base con **cientos de subdominios**, algunos de los cuales **contienen el nombre de la organización objetivo**. Servicios de **DNS dinámico**. Red de bots de entre 200.000 y 260.000 dispositivos, desarticulada en septiembre de 2024 |

### X-1.1 — Lo que no hay, y es la clave de la detección

No hay: familia de malware propia con implante persistente; cifrado o destrucción; día cero; técnica de evasión de controles de endpoint; canal de mando y control propio más allá de HTTP cifrado y la VPN legítima; ni *rootkit*.

**Este adversario no tiene malware que detectar.** Tiene una lista de la compra de software ajeno, legítimo o público, usado con mala intención. **La consecuencia operativa es que un programa de seguridad basado en detección de amenazas no lo ve, y un programa basado en gestión de configuración e inventario lo ve entero.** De ahí que `X-5` sea, en este informe, más importante que `X-3`.

## X-2. Artefactos de host persistentes

<!-- cti:cards -->

| Categoría | Artefactos | Etiqueta |
|---|---|---|
| **VPN legítima como persistencia** | Instalación de **SoftEther** (cliente, servidor o puente) · servicio registrado · adaptador de red virtual · **configuración de reconexión automática al arrancar** | `el artefacto más valioso` |
| **Binarios del sistema fuera de su sitio** | `conhost.exe` o `dllhost.exe` **fuera de `C:\Windows\System32`** · proceso `DiagTrack.exe` que no sea el servicio legítimo | `regla de una línea` |
| **Rastros del bot de correo** | `storage/fm` · `storage/fm/.run` · `.run` en la raíz de ejecución · `clientid` · `cp` · `/var/tmp/.sess.zip` · proceso hijo renombrado a `crypto` | `muy específicos` |
| **Cadenas fijas del bot** | `jh4jnryw76ikmh` (contraseña) · `rhnr5m54pk65wertc` (clave) · vector de inicialización `1111111111111111` · cabecera `X-Id:` | `clave fija: no rota` |
| **Preparación de exfiltración** | `001.gif` · `Include.png` · `Css.js` · `M2k.js` · `M2k_list.js` · `M2k_ui_adm.js` · `All_scanner_vXX.pl.gz` | `nombres aburridos a propósito` |
| **Identidad** | Aplicación registrada con permisos de lectura de buzón, con secreto antiguo y sin propietario reconocible · directorios `config` y `dump` de la utilidad de exfiltración | `no genera eventos de inicio de sesión` |
| **Plataformas extensibles** | **Extensión, complemento o componente de servidor no documentado**, que responde sólo con una clave o parámetro concreto, y **presente en las copias de seguridad** | `la aportación del informe` |

## X-3. Lógica de detección prioritaria

<!-- cti:detections -->

**D-1 · CRÍTICO — VPN de terceros instalada o reconectando al arrancar**

```
(software.inventory.name MATCHES "(?i)softether"
 OR service.name MATCHES "(?i)(softether|vpnclient|vpnbridge|vpnserver)"
 OR file.name MATCHES "(?i)(vpnclient|vpnbridge|vpnserver|vpncmd)\\.exe"
 OR network.adapter.description MATCHES "(?i)(softether|vpn.*virtual)")
AND NOT host.name IN <laboratorios y excepciones nominales>
```

→ **Alerta crítica e investigación del equipo.** No es una detección de malware: es una detección de inventario, y por eso funciona contra un adversario que no usa malware. **El aviso dice expresamente que el software de detección de endpoint es menos probable que marque SoftEther porque es una VPN legítima**, lo que significa que esta regla hay que escribirla a mano: no vendrá en el catálogo del fabricante.

**D-2 · CRÍTICO — Binario con nombre del sistema fuera de su directorio**

```
process.name IN ("conhost.exe","dllhost.exe","DiagTrack.exe","svchost.exe",
                 "taskhostw.exe","rundll32.exe","lsass.exe","spoolsv.exe")
AND process.executable NOT MATCHES "(?i)^C:\\\\Windows\\\\(System32|SysWOW64|WinSxS)\\\\"
```

→ **Contención automática.** Falso positivo prácticamente nulo y cobertura muy superior al expediente: **un `conhost.exe` fuera de `System32` no tiene uso legítimo**, con independencia de quién lo haya puesto ahí. Es la regla más corta y más rentable del informe.

**D-3 · CRÍTICO — Pulverización de contraseñas en interfaces de correo distintas de la web**

```
auth.failure
WHERE service == "exchange" OR service == "o365"
GROUP BY source.ip, auth.protocol, window(15m)
HAVING count(distinct user.name) >= 10 AND max(attempts_per_user) <= 3
AND auth.protocol IN ("ECP","EWS","OAB","RPC","MAPI","PowerShell",
                      "Autodiscover","ActiveSync","API")
```

→ **Alerta crítica y bloqueo de la dirección de origen.** El patrón es **muchas cuentas con pocos intentos cada una**, que es lo contrario de la fuerza bruta y lo que elude los bloqueos por cuenta. **La condición sobre el protocolo es la aportación:** la mayoría de las organizaciones vigila sólo la interfaz web, y la herramienta del actor ataca diez. Si esta regla no se puede escribir porque el registro no distingue la interfaz, eso es la brecha de `T-5`.

**D-4 · ALTO — Acceso a buzones con credenciales de aplicación no reconocidas**

```
mailbox.access
WHERE auth.type == "application"
  AND application.id NOT IN <inventario aprobado de aplicaciones>
  AND (mailbox.count > 5 OR data.volume > <umbral>)
```

→ **Alerta alta e investigación con Sistemas.** Es la detección del canal que **no genera eventos de inicio de sesión de usuario**, y por tanto la única forma de ver la utilidad de exfiltración de nube del actor. **Requiere que exista un inventario aprobado de aplicaciones registradas**, que es `H-5`.

**D-5 · CRÍTICO — Replicación de directorio desde un equipo que no es controlador**

```
directory.replication_request
WHERE source.host NOT IN <controladores de dominio>
   OR user.name NOT IN <cuentas de replicación aprobadas>
```

→ **Contención automática.** Marca el punto en que el incidente deja de ser un equipo y pasa a ser el dominio.

**D-6 · ALTO — Rastros del bot de correo en PHP**

```
(file.path MATCHES "(?i)/storage/fm(/\\.run)?$"
 OR file.name IN (".run","clientid","cp")
 OR file.path == "/var/tmp/.sess.zip"
 OR process.name == "crypto" AND process.parent.name MATCHES "(?i)(php|httpd|nginx)")
OR (http.request.header.name == "X-Id" AND http.request.uri CONTAINS "/ews")
OR file.content CONTAINS_ANY ("jh4jnryw76ikmh","rhnr5m54pk65wertc")
```

→ **Alerta alta y análisis del servidor.** Las dos cadenas fijas del final son el indicador más fuerte del expediente: **son una contraseña y una clave escritas a mano en el guion, y no rotan**. La condición de la cabecera no estándar sobre la ruta de servicios web es la variante de red.

**D-7 · ALTO — Fichero con extensión de imagen o de guion que no lo es**

```
file.created
WHERE file.extension IN ("gif","png","jpg","js","css")
  AND file.magic_type NOT MATCHING file.extension
  AND file.path MATCHES "(?i)(/var/www|/inetpub|/wwwroot|/html|/public)"
```

→ **Alerta alta.** Cubre los nombres de preparación del aviso y, más en general, el patrón de ocultar datos preparados para exfiltración bajo extensiones inocuas. **Y detecta también interfaces web de administración remota**, que es un beneficio colateral.

**D-8 · CRÍTICO — Extensión nueva en una plataforma extensible**

```
// Esta deteccion normalmente NO existe, y es el punto del informe.
platform.extension_installed
WHERE platform IN ("ArcGIS","GeoServer","<plataforma documental>",
                   "<plataforma de integracion>","<gestor de contenidos>")
  AND extension.id NOT IN <inventario aprobado de extensiones>
```

→ **Alerta crítica e investigación con el área dueña de la plataforma.** La inmensa mayoría de las organizaciones **no tiene esta telemetría ni el inventario que la regla necesita**, y construirlos es `E-c`. Mientras no exista, la alternativa es la auditoría periódica manual de `H-3`, que es peor pero es algo. **Y la condición de recuperación que acompaña a esta detección:** si se encuentra una extensión maliciosa, **restaurar desde copia de seguridad no la elimina** — eso es `E-e`.

> ⚠ **Regla de operación.** Tres detecciones admiten contención automática:
> `D-2` por fidelidad, `D-5` por lo que está en juego, y `D-1` **en servidores**
> pero no en puestos de usuario, donde una VPN personal es un problema de
> política y no un incidente. Y la observación que recorre toda la sección:
> **ninguna de estas ocho reglas detecta malware, porque este adversario no
> tiene malware.** Siete de las ocho son reglas sobre configuración, inventario
> e identidad. Si el programa de seguridad de la organización está construido
> enteramente alrededor del producto de endpoint, **este expediente lo
> atravesará sin tocarlo**.

## X-4. Consultas de caza

```kql
// H-1 y D-1 · SoftEther y cualquier VPN de terceros en el parque.
// No requiere telemetria de seguridad: basta el inventario.
union
( DeviceTvmSoftwareInventory
  | where SoftwareName has_any ("SoftEther","VPN Client","VPN Bridge","VPN Server")
  | project DeviceName, Senal = strcat("inventario: ", SoftwareName), SoftwareVersion
),
( DeviceProcessEvents
  | where Timestamp > ago(365d)
  | where FileName in~ ("vpnclient.exe","vpnbridge.exe","vpnserver.exe","vpncmd.exe")
     or ProcessCommandLine has "softether"
  | project DeviceName, Senal = strcat("proceso: ", FileName), ProcessCommandLine
),
( DeviceFileEvents
  | where Timestamp > ago(365d)
  | where FileName has_any ("vpnclient","vpnbridge","vpnserver","vpncmd")
  | project DeviceName, Senal = strcat("fichero: ", FileName), FolderPath
)
| summarize Senales = make_set(Senal, 10) by DeviceName
```

```kql
// H-2 y D-2 · Binario con nombre del sistema fuera de su directorio.
// La regla mas corta y mas rentable del informe.
DeviceProcessEvents
| where Timestamp > ago(365d)
| where FileName in~ ("conhost.exe","dllhost.exe","DiagTrack.exe","svchost.exe",
                      "taskhostw.exe","spoolsv.exe","lsass.exe")
| where not(FolderPath matches regex @"(?i)^C:\\Windows\\(System32|SysWOW64|WinSxS)\\")
| project Timestamp, DeviceName, AccountName, FileName, FolderPath,
          ProcessCommandLine, SHA256, InitiatingProcessFileName
| order by Timestamp desc
```

```kql
// H-4 y D-3 · Pulverizacion de contrasenas por interfaz de correo.
// El patron es MUCHAS cuentas con POCOS intentos: lo contrario de la fuerza bruta.
let ventana = 15m;
IdentityLogonEvents
| where Timestamp > ago(90d)
| where ActionType == "LogonFailed"
| extend Interfaz = tostring(AdditionalFields.Protocol)
| summarize Cuentas = dcount(AccountUpn), Intentos = count(),
            PorCuenta = count() * 1.0 / dcount(AccountUpn),
            Interfaces = make_set(Interfaz, 10)
         by IPAddress, bin(Timestamp, ventana)
| where Cuentas >= 10 and PorCuenta <= 3.0
| order by Cuentas desc
// Revisar la columna Interfaces: si aparece algo distinto de la interfaz web,
// es probable que esa interfaz no tenga segundo factor exigido (E-d).
```

```kql
// H-5 y D-4 · Aplicaciones registradas con permisos de buzon.
// El actor usa credenciales de aplicacion, que NO generan eventos de inicio
// de sesion de usuario. Esta consulta es una auditoria, no una deteccion.
CloudAppEvents
| where Timestamp > ago(180d)
| where ActionType has_any ("MailItemsAccessed","Create","Send","MailboxLogin")
| where isnotempty(tostring(RawEventData.AppId))
| summarize Buzones = dcount(tostring(RawEventData.MailboxOwnerUPN)),
            Accesos = count(), Primero = min(Timestamp), Ultimo = max(Timestamp)
         by AppId = tostring(RawEventData.AppId), ApplicationName = tostring(RawEventData.AppDisplayName)
| order by Buzones desc
// Contrastar con el inventario aprobado de aplicaciones. Una aplicacion que
// toca muchos buzones y que nadie reconoce es el hallazgo.
```

```bash
#!/bin/sh
# H-8 y D-6 · Rastros del bot de correo en PHP, en servidores Linux/Unix.
# Las dos cadenas fijas son una contrasena y una clave escritas a mano en el
# guion por su autor: no rotan, y son el indicador mas fuerte del expediente.

echo "== ficheros y directorios caracteristicos =="
find / -xdev \( -path /proc -o -path /sys -o -path /dev \) -prune -o \
     \( -path '*/storage/fm' -o -name '.run' -o -name 'clientid' -o -name 'cp' \) \
     -print 2>/dev/null | head -50

echo "== fichero de sesion =="
ls -la /var/tmp/.sess.zip 2>/dev/null

echo "== cadenas fijas del guion (contrasena y clave) =="
grep -rIl --exclude-dir=/proc --exclude-dir=/sys \
     -e 'jh4jnryw76ikmh' -e 'rhnr5m54pk65wertc' \
     /var/www /home /usr /var/tmp 2>/dev/null | head -20

echo "== guiones PHP que hablan con servicios web de Exchange =="
grep -rIl --include='*.php' -e 'CURLOPT_HTTPHEADER' -e '/ews' \
     /var/www 2>/dev/null | head -20

# AVISO: un acierto en las cadenas fijas es concluyente. Un acierto en la
# ultima comprobacion no lo es: hay integraciones legitimas con Exchange.
```

```bash
#!/bin/sh
# H-11 y E-c · Inventario de plataformas geoespaciales expuestas.
# La aportacion propia de este informe. No es una consulta de seguridad:
# es un inventario, y lo decisivo es la ultima pregunta, que no es tecnica.

RANGOS="<prefijos propios anunciados>"

echo "== puertos tipicos de plataformas geoespaciales =="
# ArcGIS Server: 6080/6443 (y 80/443 tras proxy) · ArcGIS Portal: 7080/7443
# GeoServer: habitualmente 8080/tomcat · MapServer/QGIS Server: via CGI en 80/443
nmap -Pn -p 80,443,6080,6443,7080,7443,8080,8443 --open $RANGOS 2>/dev/null \
  | grep -E "Nmap scan report|open"

echo
echo "== rutas delatoras en los servicios web encontrados =="
for H in <hosts encontrados>; do
  for R in /arcgis/rest/services /arcgis/admin /portal/home \
           /geoserver/web /geoserver/rest /server/rest/services; do
    C=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "https://$H$R")
    [ "$C" = "200" ] || [ "$C" = "401" ] || [ "$C" = "403" ] && echo "$H$R -> $C"
  done
done

# Y LAS TRES PREGUNTAS QUE NO SE RESPONDEN CON UN ESCANER:
#   1. Quien administra cada una de estas plataformas? (casi nunca es TI)
#   2. Que extensiones tiene instaladas, y quien las instalo?
#   3. Incluye su copia de seguridad las extensiones? Si si, restaurar
#      reinstala al adversario.
```

```yaml
# Sigma — VPN de terceros como mecanismo de persistencia
title: Instalacion o ejecucion de SoftEther u otra VPN de terceros
id: 5d2a8c71-4f63-49b0-a7e8-1b96c3047ea2
status: stable
description: >
  Persistencia preferente de los actores habilitados por el Integrity
  Technology Group. El propio aviso conjunto senala que el software de
  deteccion de endpoint es menos probable que lo marque porque SoftEther es una
  VPN legitima: esta regla hay que escribirla a mano.
author: Celula CTI
date: 2026-11-17
references:
  - https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-281a
tags:
  - attack.persistence
  - attack.t1133
  - attack.command_and_control
  - attack.t1090
logsource:
  category: process_creation
  product: windows
detection:
  binarios:
    Image|endswith:
      - '\vpnclient.exe'
      - '\vpnbridge.exe'
      - '\vpnserver.exe'
      - '\vpncmd.exe'
  cadena:
    CommandLine|contains:
      - 'softether'
      - 'SoftEther'
  descarga:
    CommandLine|contains|all:
      - 'softether'
    Image|endswith:
      - '\powershell.exe'
      - '\curl.exe'
      - '\wget.exe'
  condition: binarios or cadena or descarga
falsepositives:
  - Equipos de laboratorio y usuarios con VPN personal: enumerar nominalmente.
    En servidores no deberia haber ninguno
level: critical
```

```yaml
# Sigma — Binario con nombre del sistema fuera de su directorio
title: conhost, dllhost u otro binario del sistema fuera de System32
id: 8c47e2b5-1a90-4d36-bf52-9e37d0a61c84
status: stable
description: >
  El actor renombra los instaladores de SoftEther a conhost.exe o dllhost.exe
  para parecer ejecutables comunes de Windows. La regla cubre mucho mas que
  este expediente: un conhost.exe fuera de System32 no tiene uso legitimo.
author: Celula CTI
date: 2026-11-17
tags:
  - attack.defense_evasion
  - attack.t1036.003
logsource:
  category: process_creation
  product: windows
detection:
  nombres:
    Image|endswith:
      - '\conhost.exe'
      - '\dllhost.exe'
      - '\DiagTrack.exe'
      - '\svchost.exe'
      - '\taskhostw.exe'
      - '\spoolsv.exe'
  ubicacion_legitima:
    Image|startswith:
      - 'C:\Windows\System32\'
      - 'C:\Windows\SysWOW64\'
      - 'C:\Windows\WinSxS\'
  condition: nombres and not ubicacion_legitima
falsepositives:
  - Practicamente ninguno
level: critical
```

## X-5. Mitigaciones de configuración con efecto directo

**Esta sección es, en este informe, más importante que la de detección**, y conviene decirlo: contra un adversario sin malware, la configuración gana a la detección.

| Control | Corta |
|---|---|
| **Parchear las ocho vulnerabilidades del Anexo A.1** | **La etapa 01 completa por la vía principal.** Son ocho, tienen parche desde hace años y cinco acaban de entrar en el catálogo oficial de explotadas conocidas |
| **Autenticación multifactor exigida en las diez interfaces de correo**, no sólo en la web | **La etapa 01 por la vía de credenciales, y la etapa 03 entera.** Basta con que una interfaz siga aceptando sólo contraseña para que la pulverización funcione |
| **Lista blanca de aplicaciones registradas con permisos de buzón**, con revisión de secretos y caducidad obligatoria | La exfiltración de nube, que **no genera eventos de inicio de sesión**. Sin esta medida, `D-4` no se puede escribir |
| **Control de ejecución y de instalación de software que impida clientes de VPN de terceros**, especialmente en servidores | **La etapa 02 por su vía principal.** Y es la medida que compensa que el EDR no marque SoftEther |
| **Inventario y control de cambios de extensiones en toda plataforma extensible**, con aprobación nominal | **La etapa 02 por su vía excepcional**, que es la del caso de un año de permanencia. **Es `E-c` y la aportación propia del informe** |
| **Verificar y, si procede, cambiar el procedimiento de copia de seguridad de las plataformas sectoriales** para que la restauración no reinstale extensiones no aprobadas | El mecanismo que convirtió una restauración completa en una reinstalación del adversario. **Es `E-e`, y es una medida de continuidad además de seguridad** |
| Segundo factor obligatorio en las cuentas de administrador de portal de las plataformas sectoriales | El punto de entrada del caso de `O-3.C`: **una credencial válida, no una vulnerabilidad** |
| Retirar de Internet las consolas de administración de las plataformas publicadas, manteniendo público sólo el nodo de consulta | Generaliza la medida geoespacial: muchos de estos servicios **deben** publicar datos, pero ninguno necesita publicar su consola |
| Corrección de vulnerabilidades de *cross-site scripting*, con prioridad en páginas con formulario de acceso | La vía inusual de la etapa 01, y protege además a terceros: el actor usa sitios vulnerables **para atacar a otras víctimas** |
| Cierre de los puertos 21, 22, 53 y 1080 en el perímetro donde no sean necesarios | Reduce la superficie que el escaneo del actor busca. **Cuatro de los seis puertos que escanea raramente necesitan estar abiertos a Internet** |
| Bloqueo de servicios de DNS dinámico desde servidores | El canal de mando y control de la etapa 02. **Con la salvedad de `A.3`:** el bloqueo por dominio base de un servicio de DNS dinámico puede afectar a terceros legítimos |

---

## 14. Brechas de inteligencia y nuevos requisitos de colección

| # | Brecha | Impacto en el juicio | Requisito propuesto | Prioridad |
|---|---|---|---|---|
| G-1 | **El aviso no menciona Latinoamérica**, y el único caso regional se conoce por comunicación oficial sin detalle técnico | `KJ-3` y `KJ-5` descansan en inferencia. **No hay indicadores de la actividad regional, ni cadena de intrusión, ni sectores**: el propio ministerio paraguayo no aclaró qué sistemas estaban comprometidos | Consulta a los CSIRT nacionales de la región, y en particular al paraguayo, sobre indicadores y sectores de los casos de 2024 y 2026 | **Crítica** |
| G-2 | **El criterio de selección taiwanés es una muestra de uno**, con atribución de motivo hecha por parte interesada | `KJ-4` y `H3` quedan en confianza moderada. Si el criterio es otro, toda la priorización regional de `E-2` cambia | Vigilar `I-1` e `I-8`. **Y buscar activamente casos en los otros Estados del hemisferio que reconocen a Taipéi**, que es donde la hipótesis se confirma o se rompe | Alta |
| G-3 | **El caso de la plataforma geoespacial es de fuente única con confianza moderada declarada** | `KJ-6` descansa en un proveedor que se declara moderadamente seguro de la atribución. **El mecanismo, en cambio, está completamente descrito y no depende de la atribución** | Buscar corroboración. **Y entretanto, actuar sobre el mecanismo y no sobre el actor**: `E-c` es correcta aunque la atribución sea errónea | Media |
| G-4 | **El eje geoespacial de `KJ-7` es un patrón de tres casos, no una medición** | Es la aportación propia del informe y la más frágil: tres casos independientes pueden ser coincidencia, y la explicación organizativa es plausible pero no está medida | **Medirlo en casa primero** (`E-c`): si en nuestra propia organización las plataformas geoespaciales no están en el inventario ni en el ciclo de parcheo, el mecanismo queda confirmado al menos para nosotros | Alta |
| G-5 | **No hay detalle público sobre FishHub** | Se conoce el nombre y que sus dominios se incautaron. Nada más: ni función, ni indicadores, ni relación con MicroScan | `I-7`. Vigilar publicaciones posteriores de los firmantes | Media |
| G-6 | **No se sabe si la incautación de octubre de 2026 degradó la operación** | `H8` y `E-h` descansan en el historial, no en una medición del efecto de la última medida | `I-6`. Vigilar si hay reaparición de la infraestructura o un aviso de seguimiento | Media |
| G-7 | **Sin telemetría propia, y sin acceso de Seguridad a las consolas de las plataformas sectoriales** | `O-4` sin evaluar, y **el grupo B del cuestionario —el geoespacial— no lo puede responder Seguridad**: lo tiene que responder el área dueña | `E-c`, que antes que una medida técnica es **una conversación con tres áreas que hoy no hablan con Seguridad** | **Crítica** |
| G-8 | **No se ha comprobado si nuestro nombre aparece en los subdominios del anexo del aviso** | `H-12` está sin ejecutar, y es una consulta de texto de cinco minutos sobre un fichero público | Ejecutar `H-12` hoy, buscando el nombre propio, de las marcas, de los proveedores y de los clientes | Alta |

---

# ANEXOS

## Anexo A — Indicadores de compromiso

> ⚠ **Leer antes de usar. Cuatro advertencias.**
>
> **Primera, de procedencia, y es la que manda.** El aviso conjunto publica su
> propio **paquete STIX 2.1, en XML y en JSON**, con un anexo de indicadores
> muy extenso. **Esa es la fuente preferente para ingesta automática**: está
> mantenida por sus diez firmantes y puede actualizarse. Lo que sigue es una
> **selección razonada con fecha**, para lectura humana y para el índice con
> contexto de este repositorio, y está subordinada al original. Es la decisión
> `E-f`, y es el mismo criterio que `CTI-2026-030` aplicó con su aviso.
>
> **Segunda, de prioridad.** Como en `CTI-2026-033`, **el nivel más valioso de
> este anexo no son los indicadores de red: es el Anexo A.1**, ocho
> vulnerabilidades con parche. Cierra la etapa 01 completa.
>
> **Tercera, sobre el DNS dinámico.** Varios de los dominios de la
> infraestructura son subdominios de **servicios de DNS dinámico**
> compartidos. **Bloquear el dominio base afectaría a terceros legítimos**, y
> eso está marcado fila por fila. Es exactamente el riesgo que la portada de
> este repositorio advierte sobre cargar un `ioc_*.txt` sin filtrar.
>
> **Cuarta, y es una oportunidad poco habitual.** Algunos subdominios del anexo
> del aviso **contienen el nombre de la organización objetivo** como etiqueta.
> La lista de indicadores es, por tanto, **una lista parcial de víctimas**, y
> buscar en ella el nombre propio, de las marcas, de los proveedores y de los
> clientes cuesta cinco minutos. Es `H-12` y la brecha `G-8`.

### A.1 — Vulnerabilidades explotadas con éxito · **la sección que hay que atender primero**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| cve | `CVE-2014-6278` | **GNU Bash, versiones hasta 4.3 bash43-026.** Inyección de comandos del sistema operativo, ejecución remota de código. **La más antigua del expediente: doce años con parche disponible.** Si está viva en algún servicio expuesto, el hallazgo es el proceso de parcheo, no el actor | Alta | Sin caducidad: la decisión es de parcheo | **Parchear y verificar** |
| cve | `CVE-2015-3306` | **ProFTPD 1.3.5.** Control de acceso indebido, lectura no autorizada. **Añadida al catálogo oficial de vulnerabilidades explotadas conocidas con motivo de este aviso** | Alta | Sin caducidad | **Parchear y verificar** |
| cve | `CVE-2015-5477` | **ISC BIND 9.x**, anteriores a 9.9.7-P2 y 9.10.x anteriores a 9.10.2-P3. Denegación de servicio. **Añadida al catálogo oficial con este aviso.** Es el servidor DNS más desplegado del mundo y uno de los servicios que se instala una vez y se olvida | Alta | Sin caducidad | **Parchear y verificar** |
| cve | `CVE-2016-3081` | **Apache Struts** 2.3.19–2.3.20.2, 2.3.21–2.3.24.1 y 2.3.25–2.3.28. Inyección de comandos, ejecución remota. **Añadida al catálogo oficial con este aviso** | Alta | Sin caducidad | **Parchear y verificar** |
| cve | `CVE-2019-11510` | **Pulse Connect Secure** 8.2 anteriores a 8.2R12.1, 8.3 anteriores a 8.3R7.1 y 9.0 anteriores a 9.0R3.4. Recorrido de ruta, lectura no autorizada. **Concentrador de VPN: si está vivo, hay credenciales comprometidas** | Alta | Sin caducidad | **Parchear, y rotar credenciales si estuvo expuesto** |
| cve | `CVE-2021-22205` | **GitLab**, todas las versiones desde 11.9. Inyección de código, ejecución remota. **Gestor de código fuente: el impacto incluye el código y los secretos de integración continua** | Alta | Sin caducidad | **Parchear, y rotar secretos de integración continua** |
| cve | `CVE-2021-3199` | **ONLYOFFICE DocumentServer** 5.1.5 a 5.6.2. Recorrido de ruta, escritura no autorizada. **Añadida al catálogo oficial con este aviso.** Servidor de documentos de oficina con despliegue significativo en administración pública y educación de la región | Alta | Sin caducidad | **Parchear y verificar** |
| cve | `CVE-2023-22894` | **Strapi**, hasta 4.5.5. Almacenamiento de información sensible en claro, divulgación de información. **Añadida al catálogo oficial con este aviso.** La más reciente del expediente | Alta | Sin caducidad | **Parchear y verificar** |
| artefacto | **Ninguna es un día cero. La más reciente es de 2023** | **No es un indicador: es el juicio que ordena toda la defensa de este informe.** Un adversario cuya lista de explotación con éxito termina en 2023 se detiene con gestión de parches. Es `KJ-2`, y el supuesto clave de `O-6` | Alta | Sin caducidad | **Criterio de priorización** |
| artefacto | Objetivos de los guiones de MicroScan: **OpenSSL · Oracle WebLogic · Rejetto · WordPress · Juniper ScreenOS · Jenkins · Apache Struts** | **No son vulnerabilidades confirmadas como explotadas: son los servicios que la herramienta de escaneo busca.** Útil para priorizar el inventario más allá de las ocho CVE confirmadas | Alta | Sin caducidad | **Inventario y vigilancia** |
| puerto | `21` · `22` · `53` · `80` · `443` · `1080` | **Los seis puertos en que el actor concentra su escaneo.** Cuatro de los seis raramente necesitan estar abiertos a Internet: cerrarlos es reducción de superficie directa | Alta | Sin caducidad | **Revisión de exposición** (`X-5`) |

### A.2 — Persistencia y artefactos de host

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| herramienta | `SoftEther` — cliente, servidor y puente | **Persistencia preferente del actor, y NO ES MALWARE.** VPN legítima, instalada en los equipos de la víctima para ofuscar el mando y control, configurada para **reconectar automáticamente al arrancar**. El propio aviso señala que el software de detección de endpoint es menos probable que la marque **precisamente por ser legítima** | Alta | **Sin caducidad** | **Detección por inventario** (`D-1`). **No bloquear el producto en general**: controlar su instalación |
| filename | `conhost.exe` · `dllhost.exe` **fuera de `C:\Windows\System32`** | **Nombres a los que el actor renombra los instaladores de SoftEther.** El indicador no es el nombre, que es legítimo: **es el nombre fuera de su directorio**, que no tiene uso legítimo | Alta | **Sin caducidad** | **Detección con contención automática** (`D-2`) |
| filename | `DiagTrack.exe` | **Nombre de software legítimo de Windows** que adopta el proceso lanzado por `live700_v1.exe`. Misma lógica que el anterior | Alta | **Sin caducidad** | **Detección** (`D-2`) |
| filename | `live700_v1.exe` | Ejecutable contenido en el comprimido protegido con contraseña que entrega la carga de *cross-site scripting*. **Contiene funciones para consultar datos de buzones de correo** | Alta | Caduca con la campaña | **Solo retrohunt** |
| artefacto | Extensión de objeto de servidor en Java de una plataforma geoespacial, **convertida en consola de administración remota, con clave fija y preservada en las copias de seguridad** | **El artefacto de persistencia más duradero del expediente: más de un año.** No hay fichero malicioso que buscar: hay una extensión legítima modificada. **Y la copia de seguridad es parte del mecanismo** | Media *(fuente única, confianza moderada declarada)* | **Sin caducidad** | **Auditoría de extensiones** (`D-8`, `H-3`, `E-c`, `E-e`) |
| path | `storage/fm` · `storage/fm/.run` · `.run` · `clientid` · `cp` · `/var/tmp/.sess.zip` | **Directorios y ficheros que crea el bot de correo en PHP.** Muy específicos | Alta | **Sin caducidad** | **Detección** (`D-6`, `H-8`) |
| clave | `jh4jnryw76ikmh` | **Contraseña fija escrita a mano en el guion del bot de correo.** No rota. Indicador concluyente | Alta | **Sin caducidad mientras no se reescriba el guion** | **Detección** (`D-6`) |
| clave | `rhnr5m54pk65wertc` | **Clave de cifrado fija del mismo guion.** Mismo valor que la anterior | Alta | **Sin caducidad** | **Detección** (`D-6`) |
| pattern | Vector de inicialización `1111111111111111` · cifrado `rc4` o `aes-128-cbc` · cabecera HTTP `X-Id:` sobre rutas `/ews` | Parámetros fijos y cabecera no estándar del bot. **La cabecera es la variante de red del indicador** | Alta | **Sin caducidad** | **Detección** (`D-6`) |
| artefacto | Proceso hijo renombrado a `crypto` | El guion cambia el nombre de su proceso hijo. **Un proceso llamado `crypto` hijo de PHP o de un servidor web no tiene uso legítimo** | Alta | **Sin caducidad** | **Detección** (`D-6`) |
| filename | `001.gif` · `Include.png` · `Css.js` · `M2k.js` · `M2k_list.js` · `M2k_ui_adm.js` · `All_scanner_vXX.pl.gz` | **Nombres de preparación de la exfiltración**, elegidos deliberadamente aburridos para minimizar la detección del volcado de correo. **El indicador generalizable es el tipo real distinto de la extensión** | Alta | Caducan con la campaña; **el patrón no** | **Detección** (`D-7`, `H-7`) |
| path | `config/` con JSON de `client_id`, `tenant_id` y `secret` · `dump/` | Directorios de la utilidad de exfiltración de correo en la nube. **Acceso con credenciales de aplicación: no genera eventos de inicio de sesión de usuario** | Alta | Sin caducidad | **Auditoría de identidad** (`D-4`, `H-5`) |

### A.3 — Red · **leer la advertencia del DNS dinámico**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| domain | `dns.studiocloud[.]xyz` | **Dominio de mando y control atribuido por el FBI a la empresa.** Destino de las comunicaciones cifradas sobre HTTP del ejecutable entregado por la carga de *cross-site scripting* | Alta | 2027-10-08 (12 meses desde el aviso) | **Bloqueo** |
| domain | `natcloudservice[.]com` · `upl.natcloudservice[.]com` | **Dominio de mando y control del bot de correo en PHP**, con rutas `/ews`. El guion original se descargaba del segundo | Alta | 2027-10-08 | **Bloqueo** |
| ipv4 | `149.28.132.137` | Dirección desde la que se descargaba el guion del bot de correo | Alta | 2027-10-08 | **Bloqueo** |
| domain | `98aiblog[.]com` · `hmbcloud[.]com` · `hmbcloud[.]net` · `hmbiplc-01[.]com` · `sexytube0[.]com` · `twimg.co[.]uk` | **Dominios y subdominios de víctima que alojaron las conexiones de SoftEther.** Atención a la naturaleza: el aviso los describe como dominios **de víctimas** que alojaron los concentradores, de modo que **pueden corresponder a infraestructura comprometida de terceros y no a infraestructura propia del actor**. El último suplanta visualmente un dominio conocido | Alta | 2027-10-08 | **Bloqueo, con verificación previa**: puede tratarse de un tercero comprometido |
| domain | `iepl.node[.]cm` · `javacheck.ooguy[.]com` · `javaupdate.giize[.]com` · `2637596418.softether[.]net` | Mismo papel que los anteriores. **Los tres últimos son subdominios de servicios compartidos** —DNS dinámico y el propio servicio de relé de la VPN— | Alta para el subdominio; **el dominio base es un servicio legítimo** | 2027-10-08 | **Bloqueo SÓLO del subdominio completo. NO bloquear el dominio base**: afectaría a terceros legítimos |
| pattern | Subdominios con la estructura `<número>.<etiqueta>.<dominio base>` y, en particular, **etiquetas que contienen el nombre de una organización objetivo** | **La lista de indicadores del aviso es, en parte, una lista de víctimas.** Buscar en el paquete STIX el nombre propio, de las marcas, de los proveedores y de los clientes | Alta | Sin caducidad como método | **Consulta de texto** (`H-12`) |
| pattern | Subdominios con etiquetas numéricas largas separadas por puntos, en dominios de rastreo | Infraestructura de sondeo y escaneo asociada. **Centenares de entradas en el anexo del aviso**: ingerir el paquete STIX, no transcribir | Media | 2027-10-08 | **Ingesta del paquete STIX** (`E-f`) |
| artefacto | **7 dominios incautados el 8 de octubre de 2026** | Soportaban **MicroScan** y **FishHub**. Se consigna el hecho; los dominios concretos están en la documentación de la incautación. **Y el aviso advierte que la empresa conserva capacidad de reconstruir su infraestructura** | Alta | Sin caducidad como hecho | Contexto; **no contabilizar como mitigación** (`E-h`) |
| asn | Direcciones de **China Unicom, provincia de Pekín** | Red desde la que, según el Tesoro, la empresa controlaba la red de bots desde mediados de 2021 | Alta | Sin caducidad | **No bloquear por ASN**: es un operador nacional con tráfico legítimo masivo. Contexto de atribución |
| artefacto | Restricción de acceso a los datos exfiltrados **a direcciones IP de Xiamen, China** | **No es un indicador de compromiso: es el dato de atribución más concreto del expediente.** Una lista de control de acceso que alguien configuró para que sólo sus colegas leyeran el botín | Alta | Sin caducidad | **Contexto de atribución** |

### A.4 — Herramientas, interfaces y servicios · **no son maliciosos**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| herramienta | `BBScan` · `dirsearch` · `Fscan` · `ksubdomain` · `masscan` · `NMAP` · `OneForAll` · `ShuiZe` · `wpscan` | **Nueve escáneres públicos.** Su presencia **no atribuye**: son herramientas estándar de pruebas de intrusión. **Y una observación de cartera: `Fscan` aparece también en `CTI-2026-033`, usado por un clúster sin ninguna relación con éste.** Es la ilustración más limpia de por qué la herramienta no atribuye | Alta | Sin caducidad | **Detección por contexto. NO usar como base de atribución** |
| herramienta | `MicroScan` | **Herramienta propia:** aplicación web en Python, >1.300 guiones, **con panel de cuenta**. En uso desde al menos 2017. Sus dominios se incautaron en octubre de 2026 | Alta | Sin caducidad como referencia | Contexto |
| herramienta | `FishHub` | **Segunda herramienta cuyos dominios se incautaron.** Sólo se conoce el nombre: ni función, ni indicadores. Es la brecha `G-5` | Baja — sólo el nombre | — | **Vigilancia** (`I-7`) |
| herramienta | `EBurst` | **Herramienta abierta en Python** de pulverización y adivinación de contraseñas contra cuentas de correo. Pública en GitHub | Alta | Sin caducidad | **Detección por contexto** (`D-3`) |
| servicio | `ECP` · `EWS` · `OAB` · `OWA` · `RPC` · `API` · `MAPI` · `PowerShell` · `Autodiscover` · `Microsoft-Server-ActiveSync` | **Las diez interfaces del servidor de correo que la herramienta ataca.** El aviso instruye expresamente a los defensores a **incluirlas al defenderse**. No son indicadores: **son la lista de comprobación de `E-d`** | Alta | **Sin caducidad** | **Exigir segundo factor en todas** (`E-d`, `X-5`) |
| servicio | `PowerShell` · `curl` · `wget` | Medios de descarga de los instaladores de la VPN. Herramientas del propio sistema | Alta | Sin caducidad | Detección por contexto |
| servicio | Servicios de **DNS dinámico** | Infraestructura compartida legítima usada para alojar subdominios del actor. **Declarados con tipo `servicio` para que no entren en los agregados planos de este repositorio** | Alta | Sin caducidad | **No bloquear el servicio.** Bloquear subdominios completos (`A.3`) |
| servicio | Plataformas extensibles: **ArcGIS** y, por analogía, cualquier plataforma empresarial que admita extensiones de terceros | **No es un indicador: es la superficie.** La persistencia más duradera del expediente usó un mecanismo legítimo y documentado de una plataforma comercial | Alta como superficie | Sin caducidad | **Inventario y control de cambios** (`E-c`) |

## Anexo B — Fuentes y valoración

> Valoración doble tipo Admiralty/OTAN: **fiabilidad de la fuente (A–F)** ×
> **credibilidad de la información (1–6)**. Se valoran por separado.

| Fuente | Disciplina | Fiabilidad | Credibilidad | Notas de sesgo |
|---|---|---|---|---|
| **Aviso conjunto AA26-281A, 08-10-2026** — FBI, CISA, NSA, NCSC británico, Dirección de Señales australiana, Centro Canadiense de Ciberseguridad, Agencia Nacional de Policía y Oficina Nacional de Ciberseguridad de Japón, NCSC neozelandés y **Centro Nacional de Inteligencia de España**. Leído en original con sus dos anexos | Fuente gubernamental multinacional · TECHINT de investigaciones del FBI | **A** | **1** | **Fuente principal.** Diez organizaciones de siete países; la información proviene de evidencia técnica recuperada en múltiples investigaciones del FBI. **Declara su propio alcance** —lo observado en esas investigaciones— y publica dos salvedades de atribución que este informe hereda (`O-1`). Publica paquete STIX. **Sesgo a tener en cuenta:** el aviso enumera sectores de infraestructura crítica estadounidense; su geografía refleja la jurisdicción de sus firmantes, y **ninguno es latinoamericano** |
| **Designación de la OFAC del Tesoro de EE. UU. contra Integrity Technology Group, 03-01-2025** | Fuente gubernamental | **A** | **1** | Documento oficial. Fuente de las fechas del suministro de infraestructura y del control de la red de bots |
| **Anuncio conjunto del Ministerio de Tecnologías de la Información y Comunicación de Paraguay y la Embajada de EE. UU., 26-11-2024**, y declaración conjunta de julio de 2026 | Fuente gubernamental · comunicación oficial | **B** | **2** | **La única fuente del caso regional.** Comunicación oficial de dos gobiernos tras una revisión conjunta con participación del Comando Sur estadounidense. **Pero no es un informe técnico:** sin indicadores, sin cadena de intrusión, y **el propio ministerio no aclaró qué sistemas estaban comprometidos** |
| **Declaración del presidente de Paraguay atribuyendo el espionaje a la posición de su país sobre Taiwán** | Declaración política | **C** | **4** | **Parte interesada.** Se usa como **hipótesis con mecanismo**, explícitamente falsable (`H3`, `I-1`), no como hecho establecido. Su valor es que ordena la priorización regional y que se puede comprobar |
| **ReliaQuest, compromiso de un servidor ArcGIS, octubre de 2025** | OSINT comercial · TECHINT | **B** | **3** | **Fuente única del caso de `O-3.C`.** Se declara segura de que el actor es un APT chino y con **confianza moderada** de que sea éste. El **mecanismo**, en cambio, está descrito por completo y no depende de la atribución: por eso `E-c` es correcta aunque la atribución falle |
| **Lumen Black Lotus Labs y cobertura de la desarticulación de la red de bots, septiembre de 2024** | OSINT comercial y gubernamental | **B** | **2** | Fuente del expediente de la red de bots. **Las cifras de tamaño difieren entre fuentes** —más de 200.000 y más de 260.000 dispositivos—, y así se citan |
| **Cobertura periodística especializada de la incautación de octubre de 2026** | OSINT · prensa especializada | **C** | **3** | Fuente del nombre **FishHub**, del número de dominios incautados y de la advertencia de que la empresa conserva capacidad de reconstruir infraestructura. **Las fuentes discrepaban sobre el número de países firmantes** —seis o siete—; la lectura del original resuelve la discrepancia: **diez organizaciones de siete países** |
| **Cobertura hispanohablante del caso paraguayo (agencias y prensa regional)** | OSINT · prensa | **C** | **3** | Fuente de las declaraciones del ministro y del presidente, y del detalle de que el ministerio no aclaró qué sistemas estaban comprometidos. Varias fuentes independientes coinciden en lo sustancial |

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

## Anexo D — Las plataformas que no son de nadie

Este anexo no es sobre Flax Typhoon. Es el hallazgo que la escritura de este informe produjo al cruzarlo con dos informes anteriores de la cartera, y se escribe aparte porque es un requisito de inventario y no un perfil de actor.

**El patrón, con sus tres casos.** `CTI-2026-023` documenta un actor de espionaje regional cuyo objetivo declarado incluye **cartografía y datos de sistemas de información geográfica militares** andinos. `CTI-2026-033` documenta que la única víctima colombiana de un clúster global se comprometió a través de **un GeoServer vulnerable sin parchear**. Y este informe documenta **más de un año de persistencia dentro de un ArcGIS**, mediante una extensión legítima convertida en consola y preservada por las copias de seguridad. **Tres actores sin ninguna relación entre sí, en tres informes escritos de forma independiente, y una misma clase de plataforma.**

**La explicación no es técnica, es organizativa, y conviene enunciarla sin eufemismos.** En la mayoría de las administraciones públicas y de las grandes empresas de la región, los sistemas de información geográfica los administra el área que los usa: cartografía, catastro, ordenamiento territorial, minería, ambiente, obras públicas, agricultura. Esa área los compró, los instaló, los mantiene y los conoce. **Lo que no hace es estar en el inventario de aplicaciones del departamento de sistemas, ni en su ciclo de parcheo, ni en su catálogo de activos expuestos, ni en el alcance de sus auditorías.** No por negligencia: porque nunca se decidió que lo estuviera, y porque la plataforma funciona.

**Y las plataformas geoespaciales no son el único caso: son el ejemplo legible.** La misma estructura organizativa produce el mismo hueco en: plataformas de gestión documental compradas por Archivo o por Jurídico; sistemas de información de laboratorio en salud; plataformas de supervisión industrial compradas por Operaciones; sistemas de gestión académica compradas por Secretaría General; plataformas de integración compradas por un proyecto concreto hace ocho años. **El criterio común es sencillo: toda plataforma empresarial comprada por un área funcional y administrada por ella.**

**Las cinco preguntas que cierran el hueco**, y ninguna es difícil:

1. **¿Qué plataformas tenemos que no estén en el inventario de aplicaciones?** La forma rápida de averiguarlo no es preguntar a sistemas: es **cruzar el inventario con las facturas de software** del área de compras. Lo que aparece en una lista y no en la otra es el hueco.
2. **¿Quién administra cada una?** Si la respuesta es un nombre que no está en el organigrama de TI, la plataforma está en el hueco.
3. **¿Está expuesta a Internet, y está vinculada a algo interno?** La combinación —nodo público vinculado a servidor interno— es exactamente la del caso de `O-3.C`.
4. **¿Admite extensiones de terceros, quién puede instalarlas y qué tiene instalado?** Es la pregunta que convierte una plataforma en un mecanismo de persistencia, y la que nadie hace.
5. **¿Incluye su copia de seguridad las extensiones?** Si la respuesta es sí, **la restauración reinstala al adversario**, y la medida de recuperación más básica que existe se vuelve en contra. Esta pregunta es también de continuidad de negocio, lo que ayuda a que tenga interlocutor.

> **Y la razón de que esto sea difícil, dicha en voz alta.** Las cinco preguntas
> son triviales técnicamente y costosas políticamente: obligan a que Seguridad
> pida acceso a la consola de una plataforma que otra área considera suya, y a
> que se cuestione una instalación que lleva años funcionando bien. **El
> pre-mortem de este informe predice que `E-c` será la medida que no se haga**,
> y no por falta de razones técnicas. La forma de que se haga es no plantearla
> como una auditoría de seguridad sino como lo que también es: **un inventario
> de activos y una comprobación de que las copias de seguridad sirven para
> restaurar**. Las dos cosas interesan al área dueña por motivos propios.

## Anexo E — Marcos de referencia empleados

`MITRE ATT&CK v19` —la versión que usa el aviso y que este informe hereda— · `Modelo del Diamante` · `Cyber Kill Chain` · `Pirámide del Dolor` · `F3EAD` · `ICD 203` · `ACH, supuestos clave y pre-mortem` · `TLP 2.0` · `PAP` · `Admiralty Code` · `Sigma` · `STIX 2.1` · `Catálogo de vulnerabilidades explotadas conocidas de CISA`

## Anexo F — Paquete legible por máquina

- **Fuente preferente para ingesta: el paquete STIX 2.1 del aviso AA26-281A**, en XML y en JSON, mantenido por sus diez firmantes. **Es la decisión `E-f`**, y el motivo es el mismo que en `CTI-2026-030`: una copia transcrita a mano de un anexo extenso garantiza errores y no se actualiza.
- Las tablas `cti:ioc` de los Anexos A.1 a A.4 alimentan `ioc_index.csv` en cada construcción, como **selección razonada con fecha** y subordinada al original.
- **Tres filas llevan advertencia explícita de no bloquear o de bloquear con cuidado:** los subdominios de servicios de DNS dinámico, cuyo dominio base afectaría a terceros legítimos; los dominios de víctima que alojaron los concentradores de VPN, que pueden ser infraestructura comprometida de un tercero; y el sistema autónomo del operador nacional chino, que tiene tráfico legítimo masivo.
- **Reglas propias:** dos reglas Sigma en `X-4`, ambas sobre configuración y no sobre malware, y las dos sin ningún indicador perecedero.
- **Guiones propios:** dos en `sh`. El segundo —el inventario de plataformas geoespaciales expuestas— no es una herramienta de seguridad: **es un inventario**, y sus tres preguntas finales no las responde ningún escáner.

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-11-17 | Emisión inicial. Se corrigen tres afirmaciones del requisito de origen en `§3.5` —la actividad en Perú y Chile, el puerto de Chancay y el ciclo electoral peruano, y la vigencia del modelo de red de bots—, se establece **Paraguay** como único caso sudamericano confirmado y la cuestión taiwanesa como criterio de selección hipotético y falsable, se resuelve la discrepancia de la cobertura secundaria sobre el número de países firmantes del aviso (**siete países, diez organizaciones**), y se identifica en el Anexo D un **eje geoespacial que atraviesa tres informes de esta cartera** | Célula CTI |

## Anexo H — Realimentación del consumidor

| Pregunta | Respuesta |
|---|---|
| ¿Respondió a su requisito? | |
| ¿Qué decisión tomó o cambió con este informe? | |
| **¿Cuántas de las ocho vulnerabilidades del Anexo A.1 estaban vivas (`E-a`)?** | |
| **¿Apareció SoftEther, o cualquier VPN de terceros, en el parque (`E-b`, `H-1`)?** | |
| **¿Se hizo el inventario de plataformas geoespaciales? ¿Quién las administraba (`E-c`)?** | |
| ¿Incluían sus copias de seguridad las extensiones (`E-e`)? | |
| ¿Había interfaces de correo aceptando sólo contraseña (`E-d`)? | |
| ¿Apareció algún nombre propio en los subdominios del anexo del aviso (`H-12`)? | |
| ¿Llegó a tiempo? | |

> Sin este anexo devuelto, el ciclo de inteligencia queda abierto y el próximo
> producto no mejora. **La pregunta que más importa de esta tabla es la
> tercera**, y no por el adversario: porque su respuesta —quién administra las
> plataformas sectoriales— determina si el hueco del Anexo D existe también en
> nuestra casa. Es la única pregunta de todo el informe cuya respuesta no
> depende de ningún actor.
