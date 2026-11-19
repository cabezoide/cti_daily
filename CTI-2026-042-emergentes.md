---
tlp: "TLP:CLEAR"
pap: "PAP:AMBER"
id: "CTI-2026-042"
version: "1.0"
tipo: "Perfil de ecosistema"
foco_regional: "Chile · Latinoamérica"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "Devman · Funky Mantis · Dire Wolf · Sauron"
fecha: "2026-11-19"
caduca: "2027-02-19"
autor: "Célula CTI"
distribucion: "Elaborado íntegramente con fuentes abiertas TLP:CLEAR. Se leyó en original el análisis de prensa especializada que recoge extensamente el informe de PRODAFT sobre el portal de afiliados de Devman, con sus cinco roles, su política de objetivos, su modelo de gobernanza y los parámetros de su cifrador; y la cobertura chilena del caso de la Clínica Dávila. El informe original de PRODAFT, el análisis de Trustwave SpiderLabs sobre Dire Wolf del 2025-06-24 y el aviso del centro nacional de ciberseguridad de Singapur **no fueron accesibles directamente** y se usan a través de cobertura que los cita, con la limitación declarada en B-2, B-4 y G-1. Difusión libre, conservando la atribución de las fuentes y las salvedades metodológicas de §3. Se mantiene PAP:AMBER. **Advertencia de contenido: este informe describe la exposición pública de historiales clínicos de personas identificables; ningún dato personal se reproduce, y la decisión se consigna en A.7.**"
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-042

## Los tres actores que el requisito agrupó como «emergentes» no son comparables entre sí

### Lo que el requisito afirmaba sobre Chile se corrobora y con nombre: la Clínica Dávila de Santiago

> **Regla de oro del producto:** todo párrafo debe responder a un requisito de
> inteligencia (PIR) y habilitar una decisión. Si un párrafo no cambia lo que
> alguien va a hacer, va al anexo o se borra.

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-042` |
| Versión / fecha | `1.0` — 2026-11-19 (emisión inicial) |
| Tipo de producto | **Informe de ecosistema** de tres actores que el requisito agrupó y que este informe separa, más **estudio de caso nacional** sobre el incidente de la Clínica Dávila, más **método de triaje para un grupo de extorsión recién nombrado**, más evaluación de una **reclamación de capacidad destructiva contra sistemas de control industrial** |
| Niveles cubiertos | Estratégico · Operacional · Táctico · Técnico |
| Foco regional | **Una afirmación corroborada con víctima nombrada y otra sin evidencia.** (1) **Chile**: Devman atacó la **Clínica Dávila** de Santiago hacia el **2025-12-18**, con más de **250 GB** reclamados de registros de pacientes, **entrada reportada por la red privada virtual con usuario y contraseña idénticos**, y publicación parcial del material a fin de año al no cobrar. (2) **Colombia y Perú**: **ninguna fuente documenta actividad de ninguno de los tres grupos**, ni con cifrado ni sin él. (3) Y el mecanismo que importa: el programa de afiliados de Devman **ofrecía accesos por país**, lo que hace de la victimología regional una función del inventario de accesos del programa |
| Marcado de difusión | `TLP:CLEAR` · `PAP:AMBER` |
| Clasificación interna | Sin clasificar. Material íntegramente de publicación abierta |
| Requisitos atendidos | `PIR-01`, `PIR-02`, `PIR-03`, `PIR-06`, `PIR-09`, `PIR-10`, `RFI-2026-11-H` |
| Solicitante / consumidor primario | Jefatura de SOC, Respuesta a Incidentes e Ingeniería de Detección. **Y tres destinatarios que este expediente obliga a añadir**: **quien administre el acceso remoto**, porque es el vector del caso chileno y porque la recomendación más concreta del expediente es sobre cuentas de servicio y de respaldo en la red privada virtual; **quien sea responsable de tecnología de operación o de control industrial**, por `E-3`; y **Dirección**, porque la pregunta de `O-4.3` no la puede responder Seguridad |
| Ventana de observación | **2024-10 → 2026-11-19.** Octubre de 2024, primera observación de Sauron; mayo de 2025, aparición de Dire Wolf; abril de 2025, aparición de Devman; diciembre de 2025, el caso chileno; julio de 2026, el análisis del portal |
| Base de colección | Diez fuentes externas, **dos leídas en original** —el análisis extenso del portal de afiliados y la cobertura chilena del caso—, **y tres fuentes primarias no accesibles** que se usan por cita (`G-1`). Sin telemetría propia |
| Autor (analista) | Célula CTI |
| Revisión por pares | Pendiente |
| Aprobación | Pendiente |
| Caducidad / revisión | 2027-02-19 (92 días). **Revisión anticipada obligatoria si:** se documenta el uso real de un cifrador para SCADA por este o cualquier actor de extorsión (sería un cambio de categoría, y es `I-1`); Devman reaparece con marca propia o se identifica la marca en la que está trabajando como afiliado; aparece una víctima colombiana o peruana de cualquiera de los tres; se publica un análisis primario de Sauron que establezca que es una operación con sitio de filtración; o la Clínica Dávila o la autoridad chilena publican un alcance verificado |
| Productos relacionados | **`CTI-2026-041` (Anubis) — es el informe gemelo y hay que leerlos juntos.** Los dos documentan un ataque chileno **por la red privada virtual** con cinco semanas de diferencia —salud el 18 de diciembre de 2025, energía en enero de 2026—, los dos con víctima que minimiza y atacante que publica, y el `Anexo D` de aquél es el instrumento para leer las cifras de éste · **`CTI-2026-040` (BlackSuit → Chaos)**: su `Anexo D` evalúa desarticulaciones, y aquí se aplica a un caso distinto —**una marca que se apaga sin que la toque nadie** · **`CTI-2026-036` (Volt Typhoon)** y la familia de tecnología de operación: `E-3` evalúa qué significaría que un actor **criminal** reclamara capacidad de daño físico, y por qué eso sería un cruce de categoría · `CTI-2026-024` (Rhysida): el precedente de una operación con actores de acceso asociados, que aquí aparece **integrada en el propio programa** · `CTI-2026-014`, `015`, `016`, `035`: el resto de la familia de extorsión |
| Paquete legible por máquina | Las tablas `cti:ioc` del Anexo A alimentan `ioc_index.csv`. **Y este informe tiene una peculiaridad de ingesta que conviene entender:** aporta **muy pocos valores y mucha estructura**, porque tres de sus fuentes primarias no fueron accesibles (`G-1`) y porque lo que el expediente tiene de valioso son **el modelo de gobernanza del programa, los parámetros del cifrador y el método de triaje**. Las entradas de `A.5` llevan tipo `cartera` y **cada una indica quién lo dice**, aplicando el `Anexo D` de `CTI-2026-041`. **Y ningún dato personal de los pacientes expuestos se reproduce** (`A.7`) |

> ⚠ **Cinco limitaciones, y la primera condiciona la estructura del informe.**
> (1) **Tres de las fuentes primarias no fueron accesibles**: el informe
> original de PRODAFT sobre el portal, el análisis de Trustwave SpiderLabs
> sobre Dire Wolf y el aviso del centro nacional de Singapur. Se usan a
> través de cobertura que los cita extensamente y con atribución nominal, y
> **los indicadores de Dire Wolf no se transcriben** por la regla de
> `CTI-2026-032`. (2) **De Sauron no hay ningún análisis primario**, y ese
> vacío es un hallazgo y no sólo una carencia: `O-1.3` lo desarrolla. (3)
> **La reclamación del cifrador para SCADA es una afirmación del adversario
> en una entrevista**, sin verificación, y `E-3` la trata con el marco de
> `CTI-2026-041`. (4) **En el caso chileno, el volumen y la vía de entrada
> los dicen el atacante y la prensa**; la institución **no ha confirmado
> formalmente** que fuera extorsión ni que afectara a datos de pacientes. (5)
> **Los recuentos de víctimas provienen de rastreadores de sitios de
> filtración**, que cuentan **reclamaciones** y no brechas verificadas.

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** **La primera conclusión del informe es que los tres actores no son comparables, y agruparlos como «emergentes» oculta precisamente lo que hay que saber de cada uno.** La diferencia no es de tamaño sino de **naturaleza y de solidez probatoria**:

| | **Devman** | **Dire Wolf** | **Sauron** |
|---|---|---|---|
| Qué es | **RaaS industrializado** con portal de afiliados, roles, nómina y gobernanza | **Equipo reducido y cerrado**, sin programa amplio de afiliados | **Una familia de cifrador** con contacto por correo. **No hay evidencia de que sea un «grupo»** |
| Sitio de filtración | Sí, **184 víctimas reclamadas** | Sí, **100 víctimas en 32 países** a agosto de 2026 | **Ninguno confirmado** |
| Análisis primario | **Sí**, extenso, de una empresa suiza | **Sí**, de un equipo de investigación | **Ninguno localizado** |
| Aviso de un Estado | Boletín del centro nacional israelí | **Alerta crítica del centro nacional de Singapur** | **Ninguno** |
| Víctima regional | **Sí: Clínica Dávila, Santiago** | No documentada | No documentada |
| Estado | **Silencio desde el 2026-02-04** | **Activo y acelerando** | Desconocido |

Valoramos **casi con certeza** *(≥99 %)* que los tres estén en niveles distintos de madurez operativa y de evidencia disponible. **Confianza: alta.** *Base:* `B-1` a `B-6`. **Y la consecuencia práctica es de asignación de esfuerzo:** un informe que trate a los tres igual induce a repartir atención por igual, y **el único de los tres que está activo, acelerando y con alerta de un Estado es Dire Wolf**, mientras el único con víctima regional nombrada es Devman, que está callado.

**KJ-2.** **La afirmación del requisito sobre Chile se corrobora, y con nombre de institución.** Devman atacó la **Clínica Dávila**, en Santiago, hacia el **18 de diciembre de 2025**, reclamando **más de 250 GB** de registros sensibles de pacientes. Al no obtener el pago, **publicó parte del material robado** hacia el 31 de diciembre en un foro de la web oscura en ruso. El vector reportado es **la red privada virtual, con usuario y contraseña idénticos**. La institución reconoció «un incidente de un tercero» y **no ha confirmado formalmente** que se tratara de extorsión ni que afectara a datos de pacientes. Valoramos **casi con certeza** *(≥99 %)* que la publicación en el sitio del grupo y la posterior filtración ocurrieran, y **probable** *(55–80 %)* que el volumen y la vía de entrada sean los reportados. **Confianza: alta para los hechos públicos; moderada para las cifras**, que son del atacante y de la prensa. *Base:* `B-3`.

**KJ-3.** **Y la segunda afirmación del requisito no tiene ninguna evidencia: no hay actividad documentada de ninguno de los tres grupos en Colombia ni en Perú, ni con cifrado ni sin él.** Se buscó expresamente en español y en inglés. Valoramos **muy probable** *(80–95 %)* que la afirmación sea una extrapolación. **Confianza: moderada.** *Base:* ausencia en diez fuentes. **Y conviene enunciar con precisión qué significa ese «no»**, porque es el tipo de negativo que esta cartera ya ha visto fallar dos veces en este mismo lote: significa que **no se publicó**, y en extorsión eso tiene una causa estructural concreta — **un sitio de filtración sólo publica a quien no paga**, de modo que la victimología publicada mide la negativa a pagar y no el ataque. Una víctima colombiana o peruana que pagó **no aparecería en ninguna fuente de este informe**.

**KJ-4.** **El hallazgo que explica la victimología regional no es la geografía ni el sector: es que el propio programa reparte el acceso.** Según el análisis del portal de afiliados, los administradores **ofrecían «redes» específicas por país**, preguntaban al afiliado **si usaría acceso propio o suministrado por el programa**, e imponían **ventanas de ejecución de dos a tres días**. Valoramos **casi con certeza** *(≥99 %)* que el programa funcionara así. **Confianza: moderada-alta**, por la vía (`G-1`). **Y las tres consecuencias son las que importan:** primera, **la victimología regional de un programa así es función de qué accesos tiene el programa**, no de las preferencias de sus afiliados — lo que convierte al mercado de corredores de acceso en el determinante real de quién es atacado en cada país; segunda, **el tiempo de permanencia es corto por diseño**: dos o tres días desde el acceso hasta el cifrado, lo que deja una ventana de detección mucho más estrecha que la de los adversarios de espionaje de esta cartera; y tercera, **esto integra en un solo producto lo que `CTI-2026-024` documentó como dos capas separadas** —el actor de acceso y el de cifrado—, y la integración es la novedad.

**KJ-5.** **Devman reclamó haber desarrollado un cifrador especializado para sistemas de control industrial diseñado para causar daño físico, y la reclamación hay que tratarla con el máximo cuidado.** En una entrevista publicada en octubre de 2025, el actor afirmó haber trabajado con Conti y haber desarrollado un «cifrador especializado para SCADA» dirigido a una compañía de gas no identificada, diseñado para infligir «daño físico progresivo más allá del cifrado»: el programa empujaría los sistemas de control «más allá de sus parámetros de operación, procesadores, memoria y límites térmicos, forzando los sistemas a acelerar y funcionar calientes hasta que el hardware falle». Valoramos **aproximadamente igual de probable** *(40–60 %)* que exista algún desarrollo en esa dirección, y **poco probable** *(20–45 %)* que la capacidad funcione como se describe y se haya empleado. **Confianza: baja. Es una afirmación del adversario en una entrevista, sin ninguna verificación.** *Base:* `B-2`. **Lo que sí está documentado y no es una reclamación** es su **política de objetivos**: anima **expresamente a atacar infraestructura crítica** e **instruye a los afiliados a solicitar un cifrador aparte para sistemas SCADA**. Es decir: **la política corrobora que el producto se ofrece; no corrobora que haga lo que el actor dice que hace.** `E-3` desarrolla por qué la distinción es toda la diferencia.

**KJ-6.** **La política de objetivos del programa es un documento revelador, y su ética es estrecha y publicitable mientras su permisividad es amplia y peligrosa.** Permite atacar fuera de los países de la Comunidad de Estados Independientes y de Serbia; excluye consulados y empresas vinculadas a esos países; **levantó una restricción previa sobre Arabia Saudí**; **anima expresamente a atacar infraestructura crítica**; e instruye a pedir cifrador aparte para SCADA. Y **prohíbe** dos cosas: atacar negocios de salud **relacionados con la infancia**, y la filtración intencionada de datos personales de **menores de dieciocho años**. Valoramos **casi con certeza** *(≥99 %)* que la política diga eso. **Confianza: moderada-alta**, por la vía. **Y la lectura que este informe sostiene:** las dos prohibiciones son **estrechas, concretas y fáciles de publicitar**; la autorización de infraestructura crítica es **amplia y de consecuencias físicas**. El caso chileno marca exactamente el límite de la regla: **la Clínica Dávila es un hospital, y la prohibición cubre la salud *infantil*, no la salud.** Una política así no es un código de conducta: es **gestión de reputación de marca entre afiliados**, y conviene leerla como tal.

**KJ-7.** **La marca se apagó sin que la desarticulara nadie, y la persona sigue.** Devman reclamó **184 víctimas** y **no ha publicado ninguna desde el 4 de febrero de 2026**; su volumen había caído de 82 en el último trimestre de 2025 a 25 en el primero de 2026, con veinticuatro de esas veinticinco en enero. Antes, en **junio de 2025**, un desconocido que se identificaba como `GangExposed` **publicó las identidades de los operadores**, lo que llevó a varios afiliados a abandonar; y el propio Devman alegó que ese mismo desconocido intentó extorsionarle por entre 0,3 y 1 bitcóin. PRODAFT declara que **no hay evidencia sólida** de por qué cerró la operación, y valora **con confianza moderada** que la persona tras el alias **sigue activa, ya no dirigiendo un programa sino trabajando como afiliado de otros grupos**. Valoramos **probable** *(55–80 %)* que así sea. **Confianza: moderada, heredada.** *Base:* `B-2`. **Y la lección es la de `CTI-2026-040` con otra forma:** allí una desarticulación judicial no detuvo a los operadores porque el sucesor ya estaba montado; aquí **no hubo desarticulación en absoluto** —hubo un desenmascaramiento y, después, silencio— y el resultado es el mismo: **la marca es el activo desechable, y la persona es el que no lo es.**

**KJ-8.** **Dire Wolf es el único de los tres que está activo, acelerando y con una alerta de Estado — y es el único sin víctima regional documentada.** Observado por primera vez en **mayo de 2025**, es un binario en Go empaquetado con UPX, con **doble extorsión, un mes de plazo para pagar y cifradores construidos a medida para cada objetivo**, cuyas notas de rescate llevan **un identificador de sala y credenciales de acceso específicos de cada víctima** — lo que su analista lee como señal de operación dirigida. Pasó de **once países** en junio de 2025 a **cien víctimas en treinta y dos países** a agosto de 2026, con **cuarenta y tres víctimas nuevas en un solo mes**. El centro nacional de ciberseguridad de **Singapur** emitió una alerta crítica. Y un informe de 2026 declara **dos negativos relevantes**: opera con **un equipo nuclear reducido y no con un programa amplio de afiliados**, y **no se encontró solapamiento de infraestructura** con cuatro operaciones conocidas. Valoramos **casi con certeza** *(≥99 %)* que esté activo y creciendo. **Confianza: moderada-alta**, por la vía (`G-1`). **Y la combinación de rasgos es lo interesante:** un equipo cerrado que crece rápido **sin afiliados** es un perfil poco común, y su consecuencia defensiva es la opuesta a la de Devman: **sin programa de afiliados no hay accesos repartidos por país, y por tanto su selección sí refleja sus propias preferencias.**

**KJ-9.** **De Sauron no hay evidencia de que sea un grupo, y el vacío es el hallazgo.** Lo que hay es **una familia de cifrador** observada por primera vez el 1 de octubre de 2024, que añade la extensión `.Sauron` junto a un identificador de víctima y **un correo electrónico del atacante**, con nota `#HowToRecover.txt` y contacto por un proveedor de correo cifrado; la nota amenaza con filtrar o vender los datos. **No se localizó ningún sitio de filtración, ningún análisis primario, ningún aviso de autoridad, ni ninguna víctima nombrada** — y una herramienta pública de identificación de familias **no pudo identificarla**, de modo que no hay descifrador conocido. Valoramos **probable** *(55–80 %)* que no sea una operación con marca y sitio de filtración comparable a las otras dos, y **aproximadamente igual de probable** *(40–60 %)* que sea una operación pequeña, un afiliado independiente o un cifrador reutilizado por varios. **Confianza: baja, y el límite es de nuestra colección tanto como del objeto.** *Base:* ausencia en diez fuentes. **Y por qué esto importa más de lo que parece:** el **contacto por correo electrónico en lugar de por portal** es el rasgo que lo separa de los otros dos. Un grupo con sitio de filtración y portal de negociación es una **marca**; un cifrador que deja una dirección de correo es **una herramienta**, y puede estar en manos de cualquiera. **El método de triaje del `Anexo D` existe para no tratar lo segundo como lo primero.**

**KJ-10.** **Y el patrón regional que une este informe con el anterior: dos incidentes chilenos de alto perfil en cinco semanas, los dos por el acceso remoto.** La Clínica Dávila el 18 de diciembre de 2025, con red privada virtual **con usuario y contraseña idénticos** según lo reportado; y el caso de `CTI-2026-041` en enero de 2026, con **la red privada virtual corporativa** según el propio atacante. Dos sectores distintos —salud y energía—, dos grupos distintos, **el mismo punto de entrada**. Valoramos **probable** *(55–80 %)* que el acceso remoto sea el vector predominante de la extorsión en la región, con la salvedad de que **dos casos no son una muestra** y de que en los dos la vía la reporta el atacante o la prensa. **Confianza: moderada.** *Base:* `B-3` y el expediente de `CTI-2026-041`. **Y la recomendación que se sigue es, por una vez, muy concreta, y la da la propia fuente primaria de este informe:** prohibir que las **cuentas de servicio y de respaldo** inicien sesión interactiva por la red privada virtual salvo requisito documentado; exigir **segundo factor resistente a suplantación** para acceso remoto y administración privilegiada; y **rotar las credenciales expuestas a concentradores de red privada virtual, integraciones de directorio, guiones y herramientas de respaldo**, empezando por las que conceden administración local o de dominio.

---

## 2. Resumen ejecutivo

El requisito pedía un informe de ecosistema sobre tres actores de extorsión emergentes —Devman, Dire Wolf y Sauron— y afirmaba dos cosas sobre la región: una exfiltración de Devman en la salud privada de Santiago, y extorsión sin cifrado en Colombia y Perú. **La primera se corrobora con nombre de institución. La segunda no tiene ninguna evidencia. Y la verificación produjo una conclusión previa a las dos: los tres actores no son comparables, y agruparlos oculta lo que hay que saber de cada uno.**

**Devman** es una operación industrializada. Apareció en abril de 2025 como afiliado de cuatro programas mayores antes de montar el suyo, su cifrador es un derivado reconocible de otra familia conocida, y mantiene un **portal web para sus afiliados** con generación de cargas, finanzas, chat con la víctima, soporte, expedientes de víctima, equipos y pagos. Su tercera versión, de enero de 2026, añadió expedientes estructurados, estados del ciclo de vida, creación de equipos, control de invitaciones, opciones de compilación por víctima, seguimiento de plazos y campos de ingresos. Hay **cinco roles identificados** —administrador, coordinador de accesos, dos operadores superiores y un afiliado—, un modelo de gobernanza en el que **el afiliado entra al chat corporativo tras producir su primera víctima**, se le asigna un **tutor experimentado** y **puede ser expulsado si pasa un mes sin una víctima nueva**, y un reparto de 80 a 20 con los fondos yendo a dos monederos distintos.

**Y el detalle que explica la victimología regional mejor que cualquier mapa**: los administradores **ofrecían «redes» por país**, preguntaban al afiliado si usaría acceso propio o suministrado por el programa, e imponían **ventanas de ejecución de dos a tres días**. Si el programa distribuye accesos por país, entonces quién es atacado en Chile, en Colombia o en Perú **depende de qué accesos tiene el programa**, no de las preferencias de sus afiliados. Eso convierte al mercado de corredores de acceso en el determinante real de la exposición regional, e integra en un solo producto lo que esta cartera había documentado como dos capas separadas.

El caso chileno. Devman atacó la **Clínica Dávila**, en Santiago, hacia el **18 de diciembre de 2025**, reclamando **más de 250 GB** de registros sensibles de pacientes, y publicó parte del material a fin de año al no obtener el pago. **El vector reportado es la red privada virtual, con usuario y contraseña idénticos.** La institución reconoció un «incidente de un tercero» y no ha confirmado formalmente que fuera extorsión ni que afectara a datos de pacientes. **Y ése es el segundo caso chileno de este lote que entra por el acceso remoto**: cinco semanas después, el expediente de `CTI-2026-041` documenta otro, en el sector energético, también por la red privada virtual. Dos sectores, dos grupos, el mismo punto de entrada.

**Y hay una reclamación que excede el requisito y que hay que tratar con el máximo cuidado.** En una entrevista de octubre de 2025, Devman afirmó haber trabajado con una operación de extorsión histórica y haber desarrollado un **«cifrador especializado para SCADA»** dirigido a una compañía de gas, diseñado para infligir **daño físico progresivo más allá del cifrado**: empujar los sistemas de control más allá de sus parámetros de operación, de procesador, de memoria y térmicos, «forzándolos a acelerar y funcionar calientes hasta que el hardware falle». **Es una afirmación del adversario en una entrevista, sin verificación alguna**, y el marco de `CTI-2026-041` dice exactamente cómo leerla: es la clase de afirmación con el máximo incentivo para exagerar. **Lo que sí está documentado, y no es una reclamación, es su política de objetivos: anima expresamente a atacar infraestructura crítica e instruye a los afiliados a pedir un cifrador aparte para sistemas SCADA.** La política corrobora que el producto se ofrece; no corrobora que haga lo que el actor dice.

Esa misma política es un documento revelador por otra razón. Prohíbe dos cosas —atacar negocios de salud **relacionados con la infancia** y filtrar intencionadamente datos de menores— y autoriza una mucho mayor: atacar infraestructura crítica. Las prohibiciones son estrechas, concretas y fáciles de publicitar; la autorización es amplia y de consecuencias físicas. **Y el caso chileno marca el límite exacto de la regla: la Clínica Dávila es un hospital, y la prohibición cubre la salud infantil, no la salud.** No es un código de conducta: es gestión de reputación de marca entre afiliados.

**Devman lleva sin publicar una víctima desde el 4 de febrero de 2026**, tras 184 reclamadas, y nadie la desarticuló. Lo que hubo fue un **desenmascaramiento público de sus operadores en junio de 2025** por parte de un desconocido, que llevó a algunos afiliados a marcharse y que —según el propio Devman— intentó después extorsionarle. La empresa que analizó el portal declara que no hay evidencia sólida de por qué cerró, y valora con confianza moderada que **la persona tras el alias sigue activa, ya no dirigiendo un programa sino trabajando como afiliado de otros grupos**. Es la lección de `CTI-2026-040` con otra forma: allí una acción policial no detuvo nada porque el sucesor ya estaba montado; aquí no hubo acción policial, y el resultado es el mismo. **La marca es el activo desechable; la persona, no.**

**Dire Wolf** es otra cosa. Observado por primera vez en mayo de 2025, binario en Go, doble extorsión, **un mes de plazo**, y **cifradores construidos a medida para cada objetivo**, con notas de rescate que llevan identificador de sala y credenciales propias de cada víctima. Pasó de once países a **cien víctimas en treinta y dos países**, con cuarenta y tres víctimas nuevas en un solo mes, y el centro nacional de ciberseguridad de Singapur emitió una alerta crítica. Opera con **un equipo nuclear reducido y sin programa amplio de afiliados**, y no se encontró solapamiento de infraestructura con cuatro operaciones conocidas. **Es el único de los tres que está activo y acelerando, y el único sin víctima regional documentada** — y las dos cosas están relacionadas: sin programa de afiliados no hay accesos repartidos por país, de modo que su selección sí refleja sus propias preferencias.

**De Sauron no hay evidencia de que sea un grupo.** Lo que hay es una familia de cifrador vista por primera vez en octubre de 2024, con extensión `.Sauron`, nota `#HowToRecover.txt` y **contacto por correo electrónico** en lugar de por portal de negociación. No se localizó sitio de filtración, ni análisis primario, ni aviso de autoridad, ni víctima nombrada, y una herramienta pública de identificación de familias no pudo reconocerla. **El contacto por correo es el rasgo que lo separa de los otros dos**: un grupo con sitio de filtración y portal es una marca; un cifrador que deja una dirección de correo es una herramienta, y puede estar en manos de cualquiera.

De ahí el `Anexo D`, que es la aportación generalizable del informe: **un método de triaje para decidir, ante un nombre nuevo, si uno tiene delante una marca, una herramienta o una reclamación sin respaldo.** Hace falta porque el ecosistema lo exige: según un recuento de tercero, **casi todo el crecimiento de las publicaciones en sitios de filtración del tercer trimestre de 2026 vino de grupos recién observados**, y esas listas mezclan ataques nuevos, cambios de marca, datos reciclados y reclamaciones sin respaldo. **Tratar cada nombre nuevo como un actor equivalente es cómo se infla un panorama de amenazas.**

<!-- cti:cards -->

| Título | Texto | Etiqueta |
|---|---|---|
| Los tres no son comparables | Uno es un **RaaS industrializado** con portal, roles y nómina; otro un **equipo cerrado** sin afiliados; del tercero **no hay evidencia de que sea un grupo**. Agruparlos oculta lo que hay que saber de cada uno | Conclusión previa |
| Santiago: corroborado | **Clínica Dávila**, 18 de diciembre de 2025, Devman, **más de 250 GB** reclamados de registros de pacientes, publicados a fin de año. **Entrada por la red privada virtual con usuario y contraseña idénticos** | Corroborado |
| Colombia y Perú: nada | **Ninguna fuente documenta actividad de los tres grupos** en ninguno de los dos países. Y el «no» tiene causa estructural: **un sitio de filtración sólo publica a quien no paga** | Sin evidencia |
| El programa reparte el acceso | Los administradores ofrecían **«redes» por país** y preguntaban si el afiliado usaría acceso propio o del programa, con **ventanas de dos a tres días**. La victimología regional es función del **inventario de accesos del programa** | Hallazgo |
| La reclamación de SCADA | Devman afirmó un cifrador que empuja los sistemas de control «hasta que el hardware falle». **Es una afirmación del adversario en una entrevista.** Lo documentado es su política: **anima a atacar infraestructura crítica y manda pedir cifrador aparte para SCADA** | Cautela |
| La ética estrecha | Prohíbe atacar salud **infantil** y filtrar datos de menores; **autoriza infraestructura crítica**. La Clínica Dávila es un hospital: **la regla cubre la salud infantil, no la salud** | Lectura |
| La marca muere, la persona no | 184 víctimas, **ninguna desde el 4 de febrero de 2026**, y **nadie la desarticuló**: hubo un desenmascaramiento en junio de 2025. Y se valora que la persona **sigue, ahora como afiliado de otros** | Hallazgo |
| Dos casos, un vector | Clínica Dávila en diciembre y el caso de `CTI-2026-041` en enero, **los dos por el acceso remoto**. Dos sectores, dos grupos, el mismo punto de entrada | Patrón regional |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| 250 GB | Volumen reclamado **por el atacante** en el caso de la Clínica Dávila | La institución reconoció un «incidente de un tercero» y **no ha confirmado** que afectara a datos de pacientes |
| 2025-12-18 | Fecha reportada del ataque a la clínica de Santiago | Y la publicación del material, hacia el **31 de diciembre** |
| 184 → 0 | Víctimas reclamadas por Devman, y las publicadas desde el **2026-02-04** | El volumen cayó de 82 en el cuarto trimestre de 2025 a 25 en el primero de 2026, **24 de ellas en enero** |
| 5 | Roles identificados en la operación de Devman | Administrador, coordinador de accesos, dos operadores superiores y un afiliado |
| 2–3 días | Ventana de ejecución que el programa **impone** al afiliado | **El tiempo de permanencia es corto por diseño**, mucho más que el de los actores de espionaje de esta cartera |
| 80 / 20 | Reparto del rescate, con los fondos a **dos monederos** | Uno del afiliado, uno del programa |
| 1 mes | Plazo tras el cual un afiliado **puede ser expulsado** si no produce una víctima nueva | Y entra al chat corporativo sólo **tras producir la primera**, con un **tutor** asignado |
| 100 en 32 | Víctimas de Dire Wolf y países, a agosto de 2026 | Desde **once países** en junio de 2025. **43 víctimas nuevas en un solo mes** |
| 0 | Análisis primarios, sitios de filtración y avisos de autoridad localizados para **Sauron** | Y una herramienta pública de identificación de familias **no pudo reconocerla** |
| 3 MiB / 1 MiB cada 51 | Umbral de cifrado completo y patrón de cifrado parcial del cifrador de Devman | Con **ChaCha20-Poly1305**. Por encima del umbral, **un trozo de 1 MiB cada 51 MiB** |
| 3 | Fuentes primarias de este informe **no accesibles** | Es `G-1`, y por eso **los indicadores de Dire Wolf no se transcriben** |

---

## 3. Alcance, requisitos y limitaciones

**3.1 Requisitos de inteligencia atendidos**

| Req. | Enunciado | ¿Respondido? | Dónde |
|---|---|---|---|
| PIR-01 | ¿Qué actores tienen intención y capacidad contra nuestra región? | **Sí: uno con víctima chilena nombrada, y dos sin evidencia regional** | `KJ-2`, `KJ-3`, `KJ-8`, `KJ-9` |
| PIR-02 | ¿Qué afirmaciones del requisito resisten la verificación? | **Sí: una corroborada, una sin evidencia, y una conclusión previa que el requisito no contemplaba** | `3.5`, `KJ-1` |
| PIR-03 | ¿Qué técnicas invalidan nuestros controles? | **Sí, y la principal es de tempo**: ventanas de ejecución de dos a tres días impuestas por el programa | `KJ-4`, `E-2` |
| PIR-06 | ¿Qué efecto tiene la industrialización del modelo de afiliados? | **Sí, y es el hallazgo del informe**: el programa reparte el acceso por país | `KJ-4`, `E-2` |
| PIR-09 | ¿Cómo se valora la información que publica un adversario sobre sí mismo? | **Sí, aplicando el marco de `CTI-2026-041` a una reclamación de capacidad destructiva** | `KJ-5`, `E-3` |
| PIR-10 | ¿Cómo se decide si un grupo recién nombrado merece un expediente? | **Sí, y es la aportación generalizable** | `Anexo D` |
| RFI-2026-11-H | El requisito pedía agrupar tres actores emergentes y evaluar dos afirmaciones regionales | **Sí, y la agrupación misma resultó ser el problema** | `3.5`, `KJ-1` |
| PIR-04 | ¿Nos afecta hoy? | **No sin telemetría propia** | `O-4` |

**3.2 Fuera de alcance.** No se evalúan: las cuatro operaciones mayores de las que Devman fue afiliado, que son actores propios y tienen más actividad que los tres de este informe; la familia de la que deriva su cifrador, que merece su propio expediente; la **controversia sobre la conducta de un investigador de una empresa de seguridad** que aparece en la misma cobertura y que es materia de ética profesional y no de inteligencia de amenazas; la identidad de los operadores desenmascarados en junio de 2025, que esta cartera no reproduce; el episodio de extorsión entre el desconocido y el grupo; la decisión de pagar; y los datos personales de los pacientes expuestos, que **no se reproducen** (`A.7`).

**3.3 Limitaciones de la colección.** Seis, y la primera determina la forma del informe.

1. **Tres fuentes primarias no fueron accesibles**: el informe original de la empresa suiza sobre el portal de afiliados, el análisis del equipo de investigación sobre Dire Wolf, y el aviso del centro nacional de Singapur. Se usan a través de cobertura que los cita extensamente y con atribución nominal. **Consecuencia directa: los indicadores de Dire Wolf no se transcriben en el Anexo A**, por la regla que `CTI-2026-032` adoptó ante un anexo ilegible —un carácter mal leído produce un indicador que no detecta nada—. Es `G-1`.
2. **De Sauron no hay ningún análisis primario**, y conviene distinguir las dos posibles causas: que el objeto sea menor, o que nuestra colección no llegue. `O-1.3` argumenta la primera y declara la segunda como límite.
3. **La reclamación del cifrador para SCADA es una afirmación del adversario en una entrevista**, sin verificación. `E-3` la trata con el marco de `CTI-2026-041`, y el juicio correspondiente lleva confianza **baja**.
4. **En el caso chileno, el volumen y la vía de entrada los dicen el atacante y la prensa.** La institución **no ha confirmado formalmente** que fuera extorsión ni que afectara a datos de pacientes. No hay informe independiente.
5. **Los recuentos de víctimas provienen de rastreadores de sitios de filtración**, que cuentan **reclamaciones del adversario** y no brechas verificadas. Una fuente de este informe lo dice expresamente, y otra advierte de que las listas mezclan ataques nuevos, cambios de marca, datos reciclados y reclamaciones sin respaldo.
6. **No hay telemetría propia.**

**3.4 Metodología.** ICD 203 para el léxico de probabilidad y confianza (Anexo C). Código Admiralty doble para las fuentes (Anexo B). MITRE ATT&CK v18 en `T-2`. Pirámide del Dolor en `T-3`. ACH y pre-mortem en `O-6`. **Grado de establecimiento** de `CTI-2026-039`, con el grado **«declaración del adversario»** que `CTI-2026-041` añadió, aplicado en `A.5`. **Y la técnica que este informe tuvo que improvisar: un método de triaje para decidir qué es un grupo recién nombrado** (`Anexo D`), que surgió de no poder comparar los tres actores que el requisito agrupaba.

**3.5 Lo que el requisito afirmaba, y lo que las fuentes sostienen**

El requisito pedía un informe de ecosistema sobre Devman, Dire Wolf y Sauron, y afirmaba una exfiltración de Devman en la salud privada de Santiago y extorsión sin cifrado en Colombia y Perú.

<!-- cti:table highlight="NO corroborado|Sin evidencia|Impreciso|Incompleto|No se pudo|y la agrupación es el problema" -->

| # | Enunciado atómico | Veredicto | Qué dicen las fuentes |
|---|---|---|---|
| 1 | «Devman, Dire Wolf y Sauron son tres actores de extorsión emergentes comparables» | **NO corroborado, y la agrupación es el problema** | Son tres objetos de naturaleza distinta: un **RaaS industrializado** con portal de afiliados, roles y nómina; un **equipo cerrado sin programa de afiliados**; y **una familia de cifrador con contacto por correo electrónico de la que no hay evidencia de que sea un grupo**. `KJ-1` y `O-1` desarrollan la separación, y el `Anexo D` da el método |
| 2 | «Hubo una **exfiltración de Devman en la salud privada de Santiago**» | **Corroborado, y con nombre de institución** | `B-3`: **Clínica Dávila**, ataque reportado hacia el **2025-12-18**, **más de 250 GB** reclamados de registros sensibles de pacientes, y **publicación parcial del material** hacia el 31 de diciembre al no obtener el pago. **Entrada reportada por la red privada virtual, con usuario y contraseña idénticos** |
| 2 *bis* | *(matiz que la fuente obliga a añadir)* | **La institución no lo ha confirmado formalmente** | `B-3`: la clínica reconoció «un incidente de un tercero» y **no ha reportado formalmente** que se tratara de extorsión ni que afectara a datos de pacientes. **Las dos cosas pueden ser ciertas a la vez**: véase el `Anexo D` de `CTI-2026-041` |
| 3 | «Hubo **extorsión sin cifrado en Colombia y Perú**» | **Sin evidencia en ninguna de las diez fuentes** | Se buscó expresamente en español y en inglés. **Ninguna fuente documenta actividad de ninguno de los tres grupos en Colombia ni en Perú**, con cifrado o sin él. Y conviene añadir la causa estructural del «no»: **un sitio de filtración sólo publica a quien no paga**, de modo que una víctima que pagó no aparecería (`KJ-3`) |
| 4 | Implícito: «los tres merecen la misma atención» | **NO corroborado** | De los tres, **el único activo, acelerando y con alerta crítica de un Estado es Dire Wolf**; el único con víctima regional nombrada es **Devman, que está callado desde febrero de 2026**; y del tercero no hay evidencia de que exista como operación. **Repartir la atención por igual es la decisión que el informe desaconseja** |
| 5 | *(no estaba en el requisito, y explica la victimología regional)* | **Corroborado, y es el hallazgo** | `B-2`: los administradores del programa de Devman **ofrecían «redes» por país**, preguntaban al afiliado **si usaría acceso propio o suministrado por el programa**, e imponían **ventanas de dos a tres días**. **La victimología regional de un programa así es función del inventario de accesos del programa** (`KJ-4`) |
| 6 | *(no estaba en el requisito, y es lo más grave)* | **Es una reclamación del adversario, no un hallazgo** | `B-2`: en una entrevista de octubre de 2025, Devman afirmó haber desarrollado un **«cifrador especializado para SCADA»** diseñado para empujar los sistemas de control «más allá de sus parámetros de operación, procesadores, memoria y límites térmicos... hasta que el hardware falle». **Sin verificación alguna.** Lo que sí está documentado es que su **política de objetivos anima a atacar infraestructura crítica e instruye a pedir cifrador aparte para SCADA** (`KJ-5`, `E-3`) |

> ⚠ **Por qué el punto 1 es la conclusión más útil de este informe, y no una
> objeción formal al requisito.** Un informe de ecosistema tiene sentido
> cuando sus actores comparten algo que explica a los tres: un linaje, un
> mercado, un modelo. Los tres troyanos bancarios de `CTI-2026-021`
> comparten región y método; los tres modelos operativos de `CTI-2026-032`
> comparten patrocinador. **Aquí lo único que comparten es la fecha
> aproximada en que alguien les puso nombre**, y eso no explica nada.
>
> El coste de la agrupación no es estético: es de **asignación de esfuerzo**.
> Un lector que reciba a los tres en el mismo documento, con el mismo
> formato, concluirá razonablemente que merecen atención comparable. **Y la
> atención correcta es muy desigual**: Dire Wolf está activo, acelerando y
> con una alerta crítica de un Estado; Devman tiene la única víctima regional
> nombrada **y está callado**; y Sauron puede no ser un actor en absoluto.
> **Un informe de ecosistema que no distingue niveles de evidencia no
> informa: infla.** De ahí el `Anexo D`.

---

# NIVEL ESTRATÉGICO
### Para: Consejo · CISO · Riesgo · Legal · Tecnología de Operación · Horizonte: 6–24 meses

## E-1. La industrialización, vista desde el organigrama del adversario

El análisis del portal de afiliados de Devman permite algo que esta cartera rara vez tiene: **ver cómo se gestiona una operación de extorsión desde dentro**. Y lo que se ve no es un grupo de delincuentes: es **una empresa pequeña con problemas de empresa pequeña**.

| Función empresarial | Cómo la resuelve el programa |
|---|---|
| **Producto** | Generación de cargas desde el portal, con opciones de compilación **por víctima**, para Windows, ESXi o Linux |
| **Ventas y entrada de clientes** | Reclutamiento en foros, y **«redes» por país** ofrecidas al afiliado |
| **Incorporación de personal** | El afiliado **entra al chat corporativo tras producir su primera víctima** |
| **Formación** | Se le asigna **un tutor experimentado** |
| **Gestión del desempeño** | **Puede ser expulsado si pasa un mes sin una víctima nueva** |
| **Control de la marca** | La formación de equipos y la revelación de la afiliación **requieren aprobación del tutor** |
| **Escalado de conflictos** | La dirección **se reserva el derecho de tomar el control de una conversación** si el afiliado se comporta mal o incumple un compromiso |
| **Nómina** | Reparto 80-20, con los fondos a **dos monederos distintos** |
| **Atención al cliente** | Chat con la víctima y mesa de ayuda, en el propio portal |
| **Administración** | Expedientes de víctima, estados del ciclo de vida, seguimiento de plazos, campos de ingresos |
| **Política corporativa** | Documento de objetivos permitidos y prohibidos |

**Las tres filas que más dicen, y ninguna es técnica.**

**La primera es la gestión del desempeño.** Un afiliado que pasa un mes sin producir una víctima **puede ser expulsado**. Eso no es una medida de seguridad operativa: es **gestión de productividad**, y tiene una consecuencia defensiva directa — **el programa impone un ritmo**, y un afiliado bajo presión de cuota es un afiliado que corre riesgos. Junto con las ventanas de ejecución de dos a tres días, describe un adversario cuyo **tempo lo fija su empleador y no la víctima**.

**La segunda es el control de la marca.** Que la formación de equipos y la revelación de la afiliación requieran aprobación del tutor, y que la dirección pueda arrebatarle una negociación a un afiliado que se porta mal, describe una organización que **sabe que su activo principal es la reputación** —la credibilidad de que cumple si le pagan— y que la defiende de sus propios empleados.

**Y la tercera es la que convierte esto en el hallazgo del informe: las «redes» por país.** El programa no sólo vende malware: **distribuye accesos**, y los distribuye por país. `E-2` saca las consecuencias.

> **Y una observación de método sobre este apartado.** Todo lo anterior
> proviene del análisis de un portal, no de una confesión ni de una filtración
> de documentos internos. **Es una de las formas de inteligencia más fiables
> que existen sobre un adversario de este tipo**, porque un portal de
> afiliados **tiene que funcionar**: sus campos, sus estados y sus reglas no
> son declaraciones, son **mecanismos que el adversario necesita que
> operen**. A diferencia de las cifras de un sitio de filtración, que son
> publicidad (`CTI-2026-041`, `Anexo D`), **la estructura de un portal de
> gestión es infraestructura**, y la infraestructura no miente sobre su propia
> función.

## E-2. El programa reparte el acceso, y eso cambia la pregunta de exposición regional

Éste es el juicio con más consecuencias del informe, y es el que menos se parece a lo que un informe de extorsión suele decir.

**El dato.** Según el análisis del portal, los administradores:

1. **Ofrecían «redes» específicas por país.**
2. **Preguntaban al afiliado si usaría acceso propio o suministrado por el programa.**
3. **Imponían ventanas de ejecución de dos a tres días.**

**Y el servicio, en palabras del propio análisis, «integraba la intermediación o distribución de accesos con el despliegue de *ransomware*».**

**Lo que eso significa para la pregunta «¿estamos expuestos?».** La formulación habitual supone que un adversario **elige** a sus víctimas por sector, por país o por tamaño, y por tanto que la exposición de una organización depende de **cuán atractiva es**. En un programa que distribuye accesos por país, la cadena causal es otra:

| Modelo habitual | Modelo de este programa |
|---|---|
| El adversario **elige** a quién atacar | El programa **ofrece lo que tiene** |
| La exposición depende de **cuán atractiva es la víctima** | La exposición depende de **qué accesos existen en el mercado para su país** |
| El determinante es el **sector y el tamaño** | El determinante es **quién ha comprometido qué, antes** |
| Reducir la exposición = ser menos atractivo | **Reducir la exposición = que no exista un acceso vendible a nuestra red** |

**La fila de abajo es la decisión.** Si la vía por la que una organización latinoamericana acaba en el sitio de filtración de un programa así es que **alguien vendió un acceso a su red en un mercado**, entonces el control que importa no es el que detecta al cifrador: es el que **impide que exista un acceso vendible**. Y los accesos vendibles tienen, casi siempre, la misma forma: **credenciales válidas de acceso remoto**.

**Lo cual encaja exactamente con lo que este informe y el anterior documentan de la región.** Dos incidentes chilenos de alto perfil en cinco semanas, en dos sectores distintos y de dos grupos distintos, **los dos por el acceso remoto** — y en el caso de la clínica, con la circunstancia reportada de **usuario y contraseña idénticos**.

**La recomendación que se sigue es, por una vez, muy concreta, y la da la propia fuente primaria del informe.** Tres medidas:

1. **Prohibir que las cuentas de servicio y de respaldo inicien sesión interactiva por la red privada virtual**, salvo requisito operativo documentado. Es la recomendación literal, y es la que menos se aplica: las cuentas de servicio son el punto ciego clásico porque nadie las vive como usuarios.
2. **Exigir segundo factor resistente a suplantación** para el acceso remoto y la administración privilegiada.
3. **Rotar las credenciales expuestas a concentradores de red privada virtual, integraciones de directorio, guiones y herramientas de respaldo**, **dando prioridad a los secretos que conceden administración local o de dominio**.

**Y la consecuencia de tempo, que es la segunda cara del mismo hallazgo.** Si el programa impone **dos o tres días** desde el acceso hasta la ejecución, entonces el tiempo de permanencia de este adversario es **un orden de magnitud menor** que el de los actores de espionaje de esta cartera —`CTI-2026-036` documenta hasta cinco años—. Eso tiene dos lecturas, y las dos importan:

- **Mala**: la ventana de detección es muy estrecha. Una caza trimestral no sirve de nada contra un adversario que entra y cifra en setenta y dos horas.
- **Buena, y es la que suele perderse**: **un adversario con prisa hace ruido**. No puede permitirse la paciencia que hace invisible a un actor de espionaje, y por tanto **las detecciones de comportamiento ruidoso —enumeración masiva, movimiento lateral rápido, borrado de copias— tienen aquí un rendimiento que no tienen contra otros adversarios**.

## E-3. La reclamación del cifrador para SCADA, y por qué hay que tratarla con cuidado y no ignorarla

Devman afirmó, en una entrevista publicada en octubre de 2025, haber desarrollado un **«cifrador especializado para SCADA»** dirigido a una compañía de gas no identificada, diseñado para infligir **daño físico progresivo más allá del cifrado**. En sus palabras, el programa empujaría los sistemas de control «más allá de sus parámetros de operación, procesadores, memoria y límites térmicos, forzando los sistemas a acelerar y funcionar calientes hasta que el hardware falle».

**Primero, qué clase de afirmación es.** Aplicando el marco del `Anexo D` de `CTI-2026-041`:

| Criterio | Esta afirmación |
|---|---|
| ¿Quién lo dice? | **El adversario**, en una entrevista que concedió |
| ¿Qué incentivo tiene? | **El máximo para exagerar.** Es una afirmación de prestigio, no operativa |
| ¿Es verificable por un tercero? | **No.** No nombra la compañía, no hay incidente público asociado, no hay muestra |
| ¿Le resta mérito? | **No. Al contrario** |
| ¿Es contable o refutable por una víctima? | **No** |
| **Credibilidad resultante** | **Baja** |

**Y el mismo marco dice cuál es la parte creíble del conjunto, que no es la reclamación.** Lo que **sí** está documentado —por el análisis del portal, no por el actor— es que su **política de objetivos**:

- **anima expresamente a atacar infraestructura crítica**, e
- **instruye a los afiliados a solicitar un cifrador aparte para sistemas SCADA**.

**Esa segunda línea es el dato.** Una política de programa es un **mecanismo** —existe para que los afiliados sepan qué pedir— y por tanto **corrobora que el producto se ofrece**. No corrobora que haga lo que el actor dice que hace. **La distinción es toda la diferencia entre un juicio sostenible y una alarma.**

| Afirmación | Base | Valoración |
|---|---|---|
| El programa **ofrece** un cifrador específico para entornos SCADA | **Política documentada del portal** | **Probable** *(55–80 %)* |
| El programa **anima** a atacar infraestructura crítica | **Política documentada del portal** | **Casi con certeza** *(≥99 %)* |
| Ese cifrador **existe y funciona** | Reclamación del actor | **Aproximadamente igual de probable** *(40–60 %)* |
| Causa **daño físico al hardware** como se describe | Reclamación del actor | **Poco probable** *(20–45 %)* |
| **Se ha empleado** contra una víctima real | Reclamación del actor, sin incidente público asociado | **Poco probable** *(20–45 %)* |

**Y por qué, aun con esa valoración, esto no se puede ignorar: sería un cruce de categoría.** Esta cartera documenta capacidad de daño a procesos físicos en dos informes, y los dos son de **actores estatales**: `CTI-2026-029`, cuyo propósito es la destrucción, y `CTI-2026-036`, cuyo propósito es el preposicionamiento para una perturbación futura. **Un actor criminal con capacidad de daño físico sería una categoría nueva**, y lo sería por una razón que no es técnica:

| | Actor estatal con capacidad destructiva | **Actor criminal con capacidad destructiva** |
|---|---|---|
| Cuándo la usa | Cuando una decisión política lo ordena | **Cuando mejora su posición negociadora** |
| Frecuencia esperable | Rara, y ligada a un conflicto | **Potencialmente rutinaria** |
| Contra quién | Objetivos de valor estratégico | **Quien tenga el acceso disponible** (`E-2`) |
| Qué la contiene | Disuasión, coste político, escalada | **Nada equivalente** |
| Predecibilidad | Alta: su propósito es conocido | **Baja: depende del cálculo de un afiliado** |

**La última fila es la razón de que este apartado exista.** Un actor estatal usa capacidad destructiva cuando lo decide un Estado; un afiliado de un programa de extorsión la usaría **cuando le pareciera que aumenta la probabilidad de cobrar**, y esa decisión la toma una persona con una cuota mensual.

**Las dos decisiones que esto pide, y son proporcionadas a una valoración baja:**

1. **No reaccionar como si la capacidad estuviera demostrada.** No hay incidente, no hay muestra, no hay verificación. Reasignar presupuesto de tecnología de operación por esta reclamación sería desproporcionado, y además sería **actuar sobre publicidad del adversario**, que es exactamente lo que `CTI-2026-041` advierte.
2. **Y sí tratar la política de objetivos como lo que es: un dato.** Que un programa de extorsión **anime a atacar infraestructura crítica** e **instruya a pedir cifrador para SCADA** es información sobre su apetito, y es documentada. La pregunta que se sigue para una organización con tecnología de operación no es «¿nos van a quemar los equipos?» sino la de siempre, y es contestable: **¿qué separa nuestra red de oficina de nuestra red de operación, y lo hemos comprobado?** Es `O-4.1`, punto 8.
3. **Y el disparador, que es lo que convierte esto en vigilancia en lugar de en alarma**: `I-1` es el primer **uso documentado** de un cifrador para sistemas de control por un actor criminal. Si ocurre, es un cambio de categoría para toda esta cartera y no sólo para este informe.

## E-4. La marca muere, la persona no: el tercer caso del patrón

`CTI-2026-040` estableció un patrón con tres casos: **el reemplazo de una operación precede a la intervención que la termina**. Este expediente añade un cuarto caso con una variante importante — **aquí no hubo intervención en absoluto.**

| Caso | Qué terminó la operación | Qué pasó con las personas |
|---|---|---|
| `CTI-2026-036` · red de bots | **Orden judicial**, enero de 2024 | La red sustituta ya operaba desde noviembre de 2023 |
| `CTI-2026-040` · extorsión | **Operación policial internacional**, julio de 2025, **sin detenciones** | El grupo sucesor ya operaba desde febrero de 2025 |
| `CTI-2026-037` · secuestro de DNS | **Operación judicial internacional**, abril de 2026 | El linaje de desarrollo había sobrevivido a una desarticulación anterior en 2024 |
| **Este informe** · extorsión | **Nada. Un desenmascaramiento público en junio de 2025, y silencio desde febrero de 2026** | Se valora que **la persona sigue activa como afiliado de otros programas** |

**Lo que el cuarto caso añade es el contrafactual que faltaba.** Los tres primeros podían leerse así: «las acciones policiales no terminan las operaciones porque el sucesor ya está montado». Este caso muestra que **una operación puede apagarse sin que nadie la toque** —por desgaste, por pérdida de afiliados tras un desenmascaramiento, por cálculo de riesgo del operador— **y que el resultado para el defensor es idéntico**: la capacidad y las personas siguen, bajo otra marca o dentro de otra.

**Y de ahí se sigue la conclusión que esta cartera puede ahora sostener con cuatro casos de cuatro familias de adversario distintas:**

> **El nombre de un grupo de extorsión es el activo más desechable de su
> operación, y por tanto el peor eje sobre el que organizar una defensa.** Lo
> que persiste son las personas, su conocimiento, sus accesos y su código.
> Una defensa construida sobre «detectar a X» caduca cuando X cambia de
> nombre, que es siempre; una construida sobre **el mecanismo** —el acceso
> remoto vendible, el borrado de copias, el ritmo de dos días— no caduca.

**La decisión práctica:** que la ingeniería de detección de esta organización se organice **por mecanismo y no por marca**, y que los expedientes de actor sirvan para entender el mecanismo y no para alimentar listas por nombre. Es una decisión de encuadre y cuesta cero, y es la lección acumulada de cuatro informes.

## E-5. Decisiones que este informe pide al nivel estratégico

1. **Prohibir que las cuentas de servicio y de respaldo inicien sesión interactiva por la red privada virtual**, salvo requisito documentado; exigir segundo factor resistente a suplantación en acceso remoto y administración privilegiada; y **rotar los secretos expuestos a concentradores de red privada virtual, integraciones de directorio, guiones y herramientas de respaldo**, empezando por los que conceden administración. `E-2`. **Es la recomendación literal de la fuente primaria y la que más directamente responde a los dos casos chilenos.** *Coste: trabajo de identidad y de redes; y una conversación con quien administra las copias.*
2. **Asumir un tiempo de permanencia de dos a tres días para esta clase de adversario**, y revisar si el programa de caza está dimensionado para eso. Una caza trimestral no detecta nada que entre y cifre en setenta y dos horas. *Coste: una revisión de la frecuencia y del alcance de la caza.*
3. **No reasignar esfuerzo de tecnología de operación por la reclamación del cifrador para SCADA**, y **sí** responder la pregunta de `E-3`, punto 2: qué separa la red de oficina de la red de operación, y si se ha comprobado. *Coste: un ejercicio de verificación de segmentación.*
4. **Organizar la ingeniería de detección por mecanismo y no por marca.** `E-4`. Es la lección acumulada de cuatro informes de esta cartera y cuesta cero. *Coste: una decisión de encuadre.*
5. **Repartir la atención entre los tres actores de forma desigual y explícita**: Dire Wolf por actividad, Devman por precedente regional y por lo que su portal enseña, Sauron por nada hasta que haya evidencia. `KJ-1`. *Coste: cero, y es lo contrario de lo que el formato de un informe de ecosistema sugiere.*
6. **Adoptar el método de triaje del `Anexo D` para los nombres nuevos.** Según una de las fuentes, **casi todo el crecimiento de publicaciones en sitios de filtración del tercer trimestre de 2026 vino de grupos recién observados**, y esas listas mezclan ataques nuevos, cambios de marca, datos reciclados y reclamaciones sin respaldo. Sin un filtro, el panorama de amenazas se infla solo. *Coste: media jornada por nombre nuevo, y ahorra expedientes enteros.*
7. **Y una decisión de comunicación que el caso chileno hace evidente**: si la organización es un prestador de salud, tener preparado **cómo se comunica a los pacientes** la exposición de su historial clínico. En este caso, la institución reconoció «un incidente de un tercero» y el adversario publicó los registros. *Coste: cero ahora; incalculable después.*
8. **No adquirir nada por este informe.** *Coste: cero en licencias.*

---

# NIVEL OPERACIONAL
### Para: Jefatura de SOC · Respuesta a Incidentes · Threat Hunting · Acceso Remoto · Horizonte: semanas–meses

## O-1. Identificación: los tres actores, separados

### O-1.1 — Devman · `Funky Mantis`

| Designación | Quién la usa | Nota |
|---|---|---|
| **Devman** · **DevMan** | Uso general, y el propio actor | La marca pública, con **presencia notoria en línea**: el boletín de un centro nacional señala que publica actualizaciones y declaraciones **en inglés y a veces en ruso**, y que «se jacta» de sus logros hasta el punto de **publicar relatos de cómo obtuvo el acceso y ejecutó el ataque** |
| **`Funky Mantis`** | **PRODAFT** | **Designación de la operación administrada centralmente.** No es un alias de la marca: es el nombre que el analista da al conjunto que incluye el portal, los roles y la gobernanza |
| `LARVA-367` · `LARVA-546` · `LARVA-547` · `LARVA-548` · `LARVA-550` | PRODAFT | **Los cinco roles identificados**: administrador y coordinador central; coordinador de accesos como punto de contacto alternativo para acceso a red; dos operadores superiores; y un afiliado acreditado por una instalación |
| *(linaje)* **DragonForce** | Vectra AI | **No es un alias: es el origen del código.** «El ADN del cifrador es inconfundiblemente DragonForce» |
| *(historial)* Qilin · DragonForce · Apos · RansomHub | Varios | **Los cuatro programas de los que fue afiliado** antes de montar el suyo, en abril de 2025 |
| *(reclamado)* Conti | **El propio actor**, en una entrevista | **Afirmación del adversario.** Dijo haber trabajado con esa operación. No verificada |

### O-1.2 — Dire Wolf

| Designación | Quién la usa | Nota |
|---|---|---|
| **Dire Wolf** · **DireWolf** | Uso general | Observado por primera vez en **mayo de 2025** |
| *(sin alias de proveedor)* | — | **No se localizó ninguna designación alternativa**, lo que es coherente con un actor reciente y con un equipo cerrado |
| *(negativos declarados)* | Un informe de 2026 | **No se encontró solapamiento de infraestructura con Akira, Fog, Qilin ni SafePay**, y opera con **un equipo nuclear reducido y no con un programa amplio de afiliados**. **Dos negativos declarados valen más que una lista de alias** |

### O-1.3 — Sauron, y por qué este informe sostiene que no es comparable

**Lo que hay:**

| Elemento | Dato |
|---|---|
| Primera observación | **1 de octubre de 2024** |
| Extensión | **`.Sauron`**, junto a un identificador único de víctima **y un correo electrónico del atacante** |
| Nota de rescate | **`#HowToRecover.txt`** |
| Amenaza | La nota informa de que los ficheros fueron cifrados **y exfiltrados**, y amenaza con filtrar o vender los datos |
| Contacto | **Correo electrónico**, con una dirección en un proveedor de correo cifrado |
| Identificación de familia | Una herramienta pública de identificación **no pudo reconocerla**, de modo que **no hay descifrador confirmado** |

**Lo que no hay, y es la lista que importa:** ningún sitio de filtración localizado, ningún análisis primario, ningún aviso de autoridad, ninguna víctima nombrada, ningún recuento, ninguna designación de proveedor, ningún dato de victimología por país o por sector.

**Y el rasgo que lo separa de los otros dos no es el tamaño: es el canal de contacto.**

| | **Marca** (Devman, Dire Wolf) | **Herramienta** (lo que Sauron parece) |
|---|---|---|
| Cómo contacta la víctima | **Portal de negociación**, URL propia por víctima | **Una dirección de correo** |
| Cómo se presiona | **Sitio de filtración público** | Amenaza en la nota |
| Qué se protege | **La reputación de la marca** | Nada: no hay marca que proteger |
| Quién puede usarlo | El programa y sus afiliados | **Cualquiera que tenga el binario** |
| Qué significa el nombre | **Una operación** | **Una familia de código**, que puede estar en varias manos |

**La consecuencia práctica, y es la razón de que `O-1.3` exista:** un expediente de actor sobre Sauron sería, con la evidencia disponible, **un expediente sobre un nombre**. Lo que una organización puede hacer con él es muy poco: no hay infraestructura que bloquear, no hay victimología que comparar con la propia, no hay programa de afiliados cuyo apetito evaluar. **Lo único accionable son la extensión y el nombre de la nota**, que están en `A.4` y que sirven para una cosa: **identificar la familia si aparece**. Es útil y es poco, y conviene decir que es poco.

> **Y el límite de esta valoración, declarado.** La ausencia de análisis
> primario puede deberse a que el objeto sea menor **o a que nuestra
> colección no llegue**, y las dos causas son indistinguibles desde aquí.
> Este informe sostiene la primera porque el perfil completo —contacto por
> correo, sin sitio de filtración, familia no identificable, sin víctima
> nombrada en dos años— es el perfil típico de una operación pequeña o de un
> cifrador reutilizado, y no el de una marca. **Pero es un juicio de
> confianza baja, y `I-4` existe para el día en que alguien publique un
> análisis que lo refute.**

## O-2. Estructura y atribución

### O-2.1 — Grado de establecimiento, por actor

| Afirmación | Base | Grado |
|---|---|---|
| **Devman** opera un portal de afiliados con cinco roles, gobernanza y política de objetivos | PRODAFT, por cita extensa en `B-2` | **Proveedor, no leído en original** (`G-1`) |
| Su cifrador deriva de DragonForce | Vectra AI, citado | **Proveedor** |
| Fue afiliado de cuatro programas antes de montar el suyo | Varios análisis, citados | **Proveedor, consistente** |
| Los administradores ofrecían **«redes» por país** y ventanas de dos a tres días | PRODAFT, por cita | **Proveedor, y es el hallazgo de `KJ-4`** |
| **184 víctimas reclamadas, ninguna desde el 2026-02-04** | Rastreador de sitios de filtración, citado | **Recuento de reclamaciones**, no de brechas verificadas |
| La persona tras el alias **sigue activa como afiliado de otros** | PRODAFT, **confianza moderada declarada** | **Proveedor, confianza moderada** |
| **Clínica Dávila**, Santiago, hacia el 2025-12-18, >250 GB reclamados, entrada por red privada virtual | Prensa chilena, recogiendo al atacante | **Declaración del adversario y prensa** |
| La institución reconoció «un incidente de un tercero» **y no ha confirmado** extorsión ni afectación de datos de pacientes | Cobertura, recogiendo a la institución | **Declaración de la víctima, por omisión** |
| **Reclamación del cifrador para SCADA** y del trabajo con Conti | **El propio actor, en una entrevista** | **Declaración del adversario, sin verificar** (`E-3`) |
| Su **política de objetivos** anima a atacar infraestructura crítica y manda pedir cifrador para SCADA | PRODAFT, por cita | **Proveedor — y es un mecanismo, no una declaración** |
| **Dire Wolf**: Go, UPX, cifrador a medida por víctima, un mes de plazo, identificador de sala y credenciales por víctima | Trustwave SpiderLabs, por cita | **Proveedor, no leído en original** (`G-1`) |
| **100 víctimas en 32 países** a agosto de 2026; **43 nuevas en un mes**; equipo cerrado; sin solapamiento con cuatro operaciones | Informes de 2026, citados | **Proveedor, no leído en original** |
| **Alerta crítica del centro nacional de Singapur** | Cobertura | **Oficial por referencia** |
| **Sauron**: extensión, nota, contacto por correo, familia no identificable | Fichas de proveedor y foro de soporte | **Proveedor de bajo nivel de detalle** |
| Sauron tiene sitio de filtración, víctimas nombradas o análisis primario | **Nada** | **Sin evidencia** |
| Actividad de cualquiera de los tres en **Colombia o Perú** | **Nada** | **Sin evidencia** |

### O-2.2 — Lo que significa que el código de Devman derive de otra familia

El cifrador de Devman es, según uno de los análisis, «inconfundiblemente DragonForce» en su ADN. Y conviene extraer de ahí lo correcto y no más:

| Lectura | ¿Sostenible? |
|---|---|
| «Devman **es** DragonForce» | **No.** Fue **afiliado** de ese programa, entre otros tres, y después montó el suyo con código derivado |
| «Las detecciones de DragonForce sirven contra Devman» | **Probablemente sí, en buena medida**, y es la consecuencia práctica más útil |
| «Comparten infraestructura» | **Sin evidencia** |
| «Comparten operadores» | **Sin evidencia**, más allá de que Devman fue afiliado |
| «Un afiliado que se lleva el código al montar su propio programa es un patrón» | **Sí, y es la lectura más informativa**: describe cómo se propaga la capacidad en este ecosistema |

**La última fila es la que vale para el futuro.** El recorrido documentado de Devman —**afiliado de cuatro programas → programa propio con código derivado de uno de ellos → vuelta a ser afiliado de otros**— describe un ecosistema en el que **la capacidad circula con las personas**, y en el que la pertenencia a una marca es un estado temporal. Es la misma conclusión de `E-4` vista desde el lado del código, y refuerza la decisión 4 de `E-5`: **detectar por mecanismo y no por marca**.

### O-2.3 — Los cuatro informes de extorsión de este lote y del anterior, comparados

| | `CTI-2026-040` BlackSuit → Chaos | `CTI-2026-041` Anubis | **Devman** | **Dire Wolf** |
|---|---|---|---|---|
| Modelo | RaaS tras operación cerrada | RaaS, **tres programas** | **RaaS industrializado con portal** | **Equipo cerrado, sin afiliados** |
| Estado | Sucesor activo | **Activo** | **Callado desde 2026-02** | **Activo y acelerando** |
| Vector distintivo | **Llamada telefónica** | Correo; y **VPN** en el caso chileno | **VPN** en el caso chileno; y **acceso suministrado por el programa** | No documentado con precisión |
| Capacidad destructiva | No | **Modo de borrado** (sin uso documentado) | **Reclamada para SCADA** (sin verificar) | Mencionado borrado de ficheros |
| Exclusiones declaradas | **BRICS, CEI, hospitales, gobierno** | **Ninguna** | **CEI y Serbia; salud infantil y menores** — **pero anima a infraestructura crítica** | No documentadas |
| Víctima regional | Ninguna | **Chile (energía)** | **Chile (salud)** | Ninguna |
| Tiempo de permanencia | No documentado | **~1 semana** de exfiltración | **2–3 días impuestos** | **1 mes de plazo de pago** |
| Qué enseña | Evaluar una desarticulación | Leer al extorsionador | **Ver el organigrama del adversario** | **Que un equipo cerrado puede crecer rápido** |

> **Dos filas merecen una lectura cruzada.** La de **víctima regional**: de
> los cuatro, **dos tienen víctima chilena nombrada, en sectores distintos, en
> cinco semanas, y los dos entraron por el acceso remoto**. Y la de
> **exclusiones**: de los cuatro, **sólo uno declara excluir hospitales** —y
> es el que no tiene víctima regional—; los dos con víctima chilena **no
> excluyen la salud**, y uno de ellos excluye expresamente sólo **la salud
> infantil**. La asimetría es incómoda y es un dato.

## O-3. Modelo de operación

### O-3.A — El portal, y lo que cada campo revela

| Función del portal | Qué revela sobre la operación |
|---|---|
| **Generación de cargas**, con opciones **por víctima**, para **Windows, ESXi o Linux** | Cifrador multiplataforma, y **configuración por objetivo**: no es una carga única |
| **Expedientes de víctima** y **estados del ciclo de vida** | Hay un proceso definido, con fases, y alguien lo supervisa |
| **Seguimiento de plazos** | El tempo es un parámetro gestionado, no una consecuencia |
| **Chat con la víctima** y **mesa de ayuda** | La negociación es una función del producto, no del afiliado |
| **Campos de ingresos** y **pagos a dos monederos** | Contabilidad separada entre afiliado y programa |
| **Creación de equipos** y **control de invitaciones** | Los afiliados pueden formar subequipos, **con aprobación** |
| **Acceso operativo compartido** | Varias personas sobre la misma víctima |
| **«Redes» por país** ofrecidas por los administradores | **El programa distribuye accesos** (`KJ-4`, `E-2`) |

### O-3.B — El cifrador, y los dos parámetros que deciden la recuperación

| Propiedad | Detalle | Consecuencia |
|---|---|---|
| **Plataformas** | Windows, **ESXi** y Linux | **El hipervisor está en el alcance.** Un plan que lo trate como refugio no es válido |
| **Algoritmo** | **ChaCha20-Poly1305** | Cifrado autenticado moderno; **no hay esperanza de fallo criptográfico** |
| **Umbral de cifrado completo** | Ficheros de **hasta 3 MiB inclusive**: cifrado **completo** | **Los ficheros pequeños se pierden enteros.** Documentos de oficina, hojas de cálculo, correos exportados: todo cae aquí |
| **Cifrado parcial** | Por encima de 3 MiB: **un trozo de 1 MiB cada 51 MiB** | Es ~2 % del fichero. **Suficiente para corromperlo y rapidísimo**: una base de datos de 100 GB se inutiliza tocando ~2 GB |
| **Funciones documentadas** | Comprobación de privilegios, **deterioro de controles de seguridad**, terminación de procesos y servicios, **inhibición de la recuperación**, **borrado de registros de eventos**, descubrimiento local y de recursos compartidos, **movimiento lateral**, cifrado multihilo, creación de nota y **autoborrado opcional** | **El movimiento lateral está en el propio cifrador**, como en `CTI-2026-040`: la contención es una carrera |

> **La fila del cifrado parcial es la que hay que llevar a quien gestione las
> copias.** Tocar un dos por ciento de un fichero grande lo inutiliza igual
> que cifrarlo entero, y cuesta cincuenta veces menos tiempo. **Eso significa
> que el tiempo entre el inicio del cifrado y la pérdida total de un
> almacenamiento grande es mucho menor de lo que la intuición sugiere**, y que
> la ventana para cortar está en minutos, no en horas.

### O-3.C — Dire Wolf, y los tres rasgos que lo distinguen

| Rasgo | Detalle | Qué significa |
|---|---|---|
| **Cifrador a medida por objetivo** | **Construido específicamente para cada víctima** | Es lo contrario de un programa de afiliados con constructor: implica **trabajo artesanal por víctima** y acota el volumen posible... salvo que creció a 43 víctimas en un mes, lo que **tensiona la afirmación** |
| **Identificador de sala y credenciales por víctima**, embebidos en la nota | Cada nota lleva lo necesario para entrar al portal de esa víctima concreta | Su analista lo lee como **señal de operación dirigida**. Y es un artefacto de identificación excelente |
| **Un mes de plazo** | Frente a los dos o tres días de ejecución de Devman | **Plazos de negociación largos** sugieren un equipo que no está bajo presión de cuota — coherente con un equipo cerrado |
| **Sin solapamiento de infraestructura** con cuatro operaciones conocidas | Negativo declarado | **Un negativo declarado es más valioso que una lista de alias**: significa que alguien buscó la conexión y no la encontró |
| **Equipo nuclear reducido, sin programa amplio de afiliados** | Negativo declarado | **Su victimología refleja sus propias preferencias**, no un inventario de accesos ajeno (`KJ-8`) |

> **Y la tensión que conviene dejar a la vista, porque el informe no la
> resuelve:** «cifradores construidos a medida para cada objetivo» y «cuarenta
> y tres víctimas nuevas en un mes» **no encajan bien**. O la personalización
> es menos profunda de lo que el término sugiere —una plantilla con
> parámetros, más que un desarrollo—, o el equipo es mayor de lo que «equipo
> nuclear reducido» sugiere, o los recuentos del sitio de filtración incluyen
> reclamaciones sin ataque. **Las tres explicaciones son plausibles y las tres
> provienen de fuentes que no pudimos leer en original** (`G-1`). Se consigna
> sin resolver, que es lo honesto.

## O-4. Nuestra exposición

### O-4.1 — El cuestionario, por orden de lo que decide

| # | Pregunta | A quién se pregunta | Por qué decide |
|---|---|---|---|
| 1 | ¿Pueden las **cuentas de servicio y de respaldo** iniciar sesión interactiva por la red privada virtual? | Identidad + Redes | **La recomendación literal de la fuente primaria**, y la que responde a los dos casos chilenos. Las cuentas de servicio son el punto ciego clásico porque nadie las vive como usuarios |
| 2 | ¿Hay **segundo factor resistente a suplantación** en el acceso remoto y en la administración privilegiada? | Identidad | `E-2` |
| 3 | ¿Cuándo se **rotaron por última vez** los secretos expuestos a concentradores de red privada virtual, integraciones de directorio, guiones y herramientas de respaldo? | Redes + Infraestructura | Es la tercera pieza de la recomendación, y la que **casi nunca se hace** |
| 4 | ¿Existe en nuestra red **alguna credencial de acceso remoto que alguien podría vender**? | Identidad | Es la pregunta de `E-2` en su forma más directa: **si el programa compra accesos, la defensa es que no exista uno vendible** |
| 5 | ¿Está nuestro programa de caza dimensionado para un **tiempo de permanencia de dos a tres días**? | SOC | Una caza trimestral no detecta lo que entra y cifra en setenta y dos horas |
| 6 | ¿Cubre el plan de recuperación **ESXi y Linux**, no sólo Windows? | Infraestructura | El cifrador se construye para las tres plataformas |
| 7 | ¿Cuánto tardaríamos en **cortar** un cifrado en curso sobre un almacenamiento grande? | SOC + Infraestructura | Con cifrado parcial de ~2 %, **la ventana está en minutos** (`O-3.B`) |
| 8 | **¿Qué separa nuestra red de oficina de nuestra red de operación, y lo hemos comprobado?** | Tecnología de Operación | `E-3`. Es la pregunta proporcionada a la reclamación de SCADA: **no reaccionar a la reclamación, y sí responder esto** |
| 9 | Si somos prestador de salud, ¿hay un procedimiento para **comunicar a los pacientes** la exposición de su historial? | Comunicación + Legal | El caso chileno lo hace evidente, y es la parte peor preparada |
| 10 | ¿Alguien **lee los relatos que este actor publica** sobre cómo entró en sus víctimas? | CTI | El boletín de un centro nacional señala que **publica relatos de cómo obtuvo el acceso**. Es inteligencia gratuita y específica |

### O-4.2 — Qué se puede medir hoy

1. **Preguntar si las cuentas de servicio y de respaldo pueden entrar por la red privada virtual.** Una consulta a Identidad, y es la medida más directa del informe.
2. **Medir la frecuencia real de la caza** y compararla con setenta y dos horas.
3. **Comprobar si el plan de copias cubre el hipervisor.**
4. **Y leer los relatos del propio actor**, que según una fuente oficial publica cómo entró. Es la única fuente de inteligencia de este informe que es gratuita, específica y que nadie recoge por sistema.

### O-4.3 — La pregunta que Seguridad no puede responder

Si la organización es un prestador de salud, hay una pregunta que este expediente plantea y que no es técnica: **¿qué se le dice a un paciente cuyo historial clínico está publicado en una web oscura?**

En el caso chileno, el adversario publicó parte de más de 250 GB de registros que dice haber tomado, y la institución reconoció «un incidente de un tercero» **sin confirmar formalmente** que afectara a datos de pacientes. **Las dos cosas pueden ser ciertas a la vez** —el marco de `CTI-2026-041` explica cómo— y la consecuencia para los pacientes es la misma en cualquier caso.

**Lo que esta célula puede ofrecer es el límite:** este informe puede decir cómo entró el adversario, qué se llevó según él, y qué configuración lo habría impedido. **No puede decir qué se le debe a un paciente**, porque eso es una cuestión jurídica, regulatoria y ética, y depende del marco de cada país. **La decisión 7 de `E-5` está dirigida a Legal y a Comunicación, y no a Seguridad, por esa razón.**

## O-5. Cronología

| Fecha | Hecho | Fuente | Grado |
|---|---|---|---|
| **2024-10-01** | Primera observación de la familia **Sauron** | `B-6` | Proveedor de bajo detalle |
| **2025-04** | **Devman aparece**, como afiliado de **Qilin, DragonForce, Apos y RansomHub** | `B-2` | Proveedor |
| **2025-05** | **Primera observación de Dire Wolf** | `B-4` | Proveedor, por cita |
| **2025-06** | **Un desconocido que se identifica como `GangExposed` publica las identidades de los operadores de Devman.** Varios afiliados abandonan; y Devman alega que intentó extorsionarle por entre 0,3 y 1 bitcóin | `B-2` | Proveedor, con una parte en declaración del adversario |
| **2025-06-24** | Se publica el análisis de **Dire Wolf**: Go, UPX, **once países**, manufactura y tecnología | `B-4` | Proveedor, por cita (`G-1`) |
| **2025-10** | Un análisis establece que el **ADN del cifrador de Devman es «inconfundiblemente DragonForce»** | `B-2` | Proveedor |
| **2025-10** | **Entrevista con Devman**: dice haber trabajado con **Conti** y haber desarrollado un **«cifrador especializado para SCADA»** para una compañía de gas | `B-2` | **Declaración del adversario** |
| **2025-12-18** | **Ataque reportado a la Clínica Dávila**, Santiago. **Entrada por la red privada virtual con usuario y contraseña idénticos**, según lo reportado | `B-3` | **Prensa, recogiendo al atacante** |
| **2025-12-31** | **Devman publica parte de los registros de pacientes** en un foro de la web oscura en ruso, al no obtener el pago | `B-3` | Prensa |
| **2025-Q4** | Devman reclama **82 víctimas** en el trimestre | `B-5` | Recuento de reclamaciones |
| **2026-01** | **Versión 3 del portal de afiliados**: expedientes estructurados, estados del ciclo de vida, equipos, control de invitaciones, compilación por víctima, plazos, campos de ingresos y acceso compartido | `B-2` | Proveedor |
| **2026-01** | Devman reclama **24 víctimas en el mes** | `B-5` | Recuento |
| **2026-02-04** | **Última víctima publicada por Devman.** Silencio desde entonces | `B-5` | Recuento |
| **2026-08-19** | **Dire Wolf: 100 víctimas en 32 países**, y **43 nuevas en un solo mes** | `B-4` | Proveedor, por cita |
| **2026-Q3** | Un recuento declara que **casi todo el crecimiento de publicaciones en sitios de filtración vino de grupos recién observados**, y advierte de que las listas mezclan ataques nuevos, cambios de marca, datos reciclados y reclamaciones sin respaldo | `B-5` | Proveedor |
| **2026-07-25** | Se publica el análisis del **portal de afiliados**, con los cinco roles, la gobernanza y la política de objetivos. Y la valoración de que **la persona sigue activa como afiliado de otros** | `B-2` | Proveedor, por cita (`G-1`) |
| **2026-11-19** | Emisión de este informe | — | — |

> **La observación que esta cronología hace visible.** El análisis más
> completo de la operación de Devman —el del portal— se publicó en **julio de
> 2026**, **cinco meses después de que la operación dejara de publicar
> víctimas**. Es decir: **el mejor material sobre una operación de extorsión
> llegó cuando la operación ya estaba apagada.** Eso no es un defecto del
> analista: es la forma normal de este mercado, y tiene una consecuencia de
> expectativas que conviene asumir — **la inteligencia detallada sobre un
> actor de extorsión suele llegar tarde para ese actor, y a tiempo para el
> siguiente**, porque lo que enseña no es la marca sino el mecanismo (`E-4`).

## O-6. Hipótesis alternativas consideradas

| Hipótesis | Evidencia a favor | Evidencia en contra | Valoración |
|---|---|---|---|
| **H-A.** La operación de Devman cesó, y la persona trabaja ahora como afiliado de otros programas | Lo valora así su analista **con confianza moderada**, a partir de información de origen humano y de análisis de conducta; el silencio desde febrero de 2026 es consistente; y el recorrido previo —afiliado, programa propio, vuelta a afiliado— es un patrón del ecosistema | Es confianza **moderada** declarada; y «no hay evidencia sólida» de por qué cerró, en palabras de la misma fuente | **Probable** *(55–80 %)* — **hipótesis preferida, heredada sin elevarla** |
| **H-B.** La operación está en pausa y volverá con la misma marca | La versión 3 del portal se lanzó **en enero de 2026**, un mes antes del silencio: **nadie invierte en una plataforma que va a abandonar** | Siete meses sin publicar víctimas es mucho para una pausa; y el desenmascaramiento de junio de 2025 da motivo para abandonar la marca | **Poco probable** *(20–45 %)*, **y la fila a favor es la que más incomoda a `H-A`** |
| **H-C.** La reclamación del cifrador para SCADA es sustancialmente cierta | La política de objetivos, documentada, **instruye a pedir cifrador aparte para SCADA**, lo que corrobora que el producto se ofrece; y el actor tiene historial de publicar relatos técnicos de sus ataques | Es una afirmación en una entrevista, **sin muestra, sin incidente público y sin compañía nombrada**; y el mecanismo descrito —forzar el hardware hasta el fallo térmico— es mucho más difícil de lograr genéricamente de lo que la frase sugiere | **Poco probable** *(20–45 %)* para el mecanismo; **probable** *(55–80 %)* para que **se ofrezca algo** con ese nombre |
| **H-D.** Hay víctimas de los tres grupos en Colombia y Perú que no se han publicado | **Un sitio de filtración sólo publica a quien no paga**, de modo que la victimología publicada mide la negativa a pagar; y el programa de Devman **ofrecía accesos por país**, lo que no excluye a ninguno | Ninguna fuente lo documenta, y los recuentos por país de los rastreadores no los sitúan | **Aproximadamente igual de probable** *(40–60 %)*, y es el límite estructural de toda victimología de extorsión |
| **H-E.** Sauron es una operación comparable a las otras dos y nuestra colección no llega | Es posible: la ausencia de análisis primario puede ser un hueco de colección | El perfil completo —contacto por **correo electrónico**, sin sitio de filtración, familia **no identificable**, sin víctima nombrada en **dos años**— es el de una herramienta o una operación pequeña, no el de una marca | **Poco probable** *(20–45 %)*, **y es un juicio de confianza baja** |
| **H-F.** Dire Wolf tiene más operadores de los que su perfil declara | **43 víctimas en un mes** no encaja bien con «cifradores a medida para cada objetivo» y «equipo nuclear reducido» | Los tres datos vienen de fuentes que **no pudimos leer en original**; y «a medida» puede significar una plantilla con parámetros | **Aproximadamente igual de probable** *(40–60 %)*, y **se consigna sin resolver** (`O-3.C`) |

**Pre-mortem.** Si en seis meses este informe resulta haber sido un error, ¿cuál será la causa más probable?

1. **Que la reclamación del cifrador para SCADA se haya citado como capacidad establecida.** Es el riesgo principal y el más dañino, porque una alarma de daño físico mueve presupuesto. El informe lo valora como *poco probable* y con confianza *baja*, y lo repite en `KJ-5`, `E-3` y `A.5`.
2. **Que la agrupación se haya mantenido pese a `KJ-1`**, y que los tres actores hayan recibido atención comparable. Es el error que el propio requisito induce.
3. **Que las cifras de víctimas se hayan citado como brechas verificadas.** Son recuentos de **reclamaciones** en sitios de filtración, y una de las fuentes advierte expresamente de que mezclan ataques nuevos, cambios de marca, datos reciclados y reclamaciones sin respaldo.
4. **Que la ausencia de evidencia en Colombia y Perú se haya leído como ausencia de riesgo**, ignorando que un sitio de filtración sólo publica a quien no paga.
5. **Que no se haya hecho la pregunta 1 de `O-4.1`** —cuentas de servicio y de respaldo en la red privada virtual—, que es la recomendación literal de la fuente primaria y la que responde a los dos casos chilenos.
6. **Que Devman reaparezca con la misma marca** y `H-A` resulte equivocada. La fila a favor de `H-B` —que la versión 3 del portal se lanzó un mes antes del silencio— es el argumento más incómodo del informe contra su propia hipótesis preferida, y se deja a la vista.

## O-7. Indicadores y señales de alerta

| Señal | Qué significaría | Acción inmediata |
|---|---|---|
| **Inicio de sesión interactivo por la red privada virtual de una cuenta de servicio o de respaldo** | **La señal que los dos casos chilenos sugieren**, y la que la fuente primaria pide prohibir | Incidente; y revisar la política de `X-5.1` |
| Autenticación correcta en el acceso remoto **con usuario y contraseña iguales** | Es la circunstancia reportada del caso de la clínica | Rotación inmediata y revisión de política de contraseñas en el concentrador |
| Enumeración masiva de recursos compartidos **seguida de movimiento lateral en horas** | **Tempo de dos a tres días**: la fase intermedia de la cadena | Incidente. **La ventana es de horas, no de días** |
| **Borrado de registros de eventos** en varios equipos | Función documentada del cifrador | Incidente |
| **Deterioro de controles de seguridad** en varios equipos | Función documentada del cifrador | Incidente, y véase `CTI-2026-041`, `X-3.2`: **alertar también sobre los intentos bloqueados** |
| Nota de rescate con **identificador de sala y credenciales de acceso embebidas** | **Dire Wolf.** Es su artefacto más específico | Incidente |
| Extensión **`.Sauron`** y nota **`#HowToRecover.txt`** | La familia de `O-1.3`. **No hay descifrador conocido** | Incidente; y preservar muestras, porque la familia **no es identificable** por las herramientas públicas |
| Ficheros grandes **corrompidos en ~2 % de su contenido**, en trozos regulares | **Cifrado parcial del cifrador de Devman**: 1 MiB cada 51 MiB | Medir el alcance por este patrón, no por la extensión |
| Cifrado sobre **ESXi** o **Linux** | Las tres plataformas están en el alcance | Incidente; y revisar si el plan de copias las cubre |
| Un **relato publicado por el actor** sobre cómo entró en una víctima del sector | Inteligencia gratuita y específica, que un boletín oficial señala que publica | Leerlo, y comprobar si la vía descrita existe en la propia red |
| **Devman reaparece con marca propia**, o se identifica la marca en la que opera como afiliado | `H-A` y `H-B` se reevalúan | **Revisión anticipada obligatoria** |
| **Uso documentado de un cifrador para sistemas de control** por un actor criminal | **Cambio de categoría para toda esta cartera** | **Revisión anticipada obligatoria** (`I-1`) |

---

# NIVEL TÁCTICO
### Para: Analistas de SOC · Ingeniería de Detección · Threat Hunting · Horizonte: días–semanas

## T-1. Cadenas de intrusión

**Devman** *(con la ventana de tempo que el programa impone)*

`Acceso inicial: credencial de acceso remoto —propia del afiliado O SUMINISTRADA POR EL PROGRAMA, que ofrece «redes» por país—` → **`ventana de ejecución impuesta: 2 a 3 días`** → `Comprobación de privilegios` → `Deterioro de los controles de seguridad; terminación de procesos y servicios` → `Descubrimiento local y de recursos compartidos de red` → `Movimiento lateral, ejecutado por el propio cifrador` → `Inhibición de la recuperación; borrado de registros de eventos` → `Cifrado multihilo con ChaCha20-Poly1305 — completo hasta 3 MiB, y por encima un trozo de 1 MiB cada 51 MiB` → `Creación de la nota; autoborrado opcional` → `Negociación en el portal del programa, con chat y mesa de ayuda` → `Publicación en el sitio de fugas si no se paga`

**Dire Wolf**

`Acceso inicial no documentado con precisión` → `Despliegue de un cifrador CONSTRUIDO A MEDIDA PARA ESA VÍCTIMA, en Go y empaquetado con UPX` → `Doble extorsión` → `Nota con identificador de sala y credenciales de acceso ESPECÍFICOS DE LA VÍCTIMA` → `Plazo de UN MES` → `Publicación si no se paga`

**Sauron** *(lo poco que hay)*

`Acceso inicial desconocido` → `Cifrado con extensión .Sauron más identificador de víctima y correo del atacante` → `Nota #HowToRecover.txt con amenaza de filtración o venta` → `Negociación POR CORREO ELECTRÓNICO`

> ⚠ **La fase que invierte el supuesto habitual está en la primera cadena, y
> es la segunda flecha.** La ventana de dos a tres días **no la impone la
> víctima ni la elige el atacante: la impone su empleador**. Eso significa
> que el tiempo de permanencia de este adversario **es un parámetro de
> gestión**, y tiene dos consecuencias opuestas: la ventana de detección es
> muy estrecha, y **un adversario con prisa hace ruido**. Las detecciones de
> comportamiento ruidoso —enumeración masiva, movimiento lateral rápido,
> borrado de registros— rinden aquí lo que no rinden contra un actor de
> espionaje.

## T-2. Mapa MITRE ATT&CK

Marco: **ATT&CK v18**. **(DM)** Devman; **(DW)** Dire Wolf; **(SA)** Sauron; **(AT)** declaración del adversario; **▲** prioridad de detección.

| Táctica | ID | Técnica | Cómo se manifiesta |
|---|---|---|---|
| Desarrollo de recursos | `T1650` ▲ | **Adquisición de acceso** | **El propio programa ofrece «redes» por país y pregunta al afiliado si usará acceso propio o suministrado.** El servicio «integraba la intermediación o distribución de accesos con el despliegue de *ransomware*» **(DM)** — es `KJ-4` |
| | `T1588.001` | Obtención de capacidades: malware | El cifrador se genera desde el portal, con opciones por víctima **(DM)** |
| | `T1587.001` | Desarrollo de malware | **Cifrador a medida para cada objetivo** **(DW)**; y el derivado de DragonForce **(DM)** |
| Acceso inicial | `T1133` ▲ | **Servicios remotos externos** | **Red privada virtual en el caso chileno, con usuario y contraseña idénticos** según lo reportado **(DM)** |
| | `T1078` | Cuentas válidas | Consecuencia del acceso comprado **(DM)** |
| Ejecución | `T1059` | Intérprete de órdenes | **(DM)** |
| Evasión | `T1562.001` ▲ | **Deterioro de los controles de seguridad** | Función documentada del cifrador **(DM)**. Véase `CTI-2026-041`, `X-3.2`: **alertar también sobre los intentos bloqueados** |
| | `T1489` | Detención de servicio | Terminación de procesos y servicios **(DM)** |
| | `T1070.001` ▲ | **Borrado de registros de eventos** | Función documentada del cifrador **(DM)** |
| | `T1027.002` | Empaquetado | **UPX** **(DW)** |
| | `T1070.004` | Borrado de ficheros | **Autoborrado opcional del propio cifrador** **(DM)** |
| Descubrimiento | `T1083`, `T1135` ▲ | Ficheros y directorios; **recursos compartidos de red** | **Lo hace el propio cifrador** **(DM)** |
| Movimiento lateral | `T1021` ▲ | **Servicios remotos** | **También lo hace el propio cifrador**, igual que en `CTI-2026-040`: la contención es una carrera **(DM)** |
| Impacto | `T1486` ▲ | **Datos cifrados para impacto** | **ChaCha20-Poly1305**; completo hasta **3 MiB**, y por encima **1 MiB cada 51 MiB** **(DM)**. Extensión `.Sauron` **(SA)** |
| | `T1490` | Inhibir la recuperación del sistema | Función documentada **(DM)** |
| | `T1657` | Robo financiero | Doble extorsión; portal de negociación **(DM, DW)**; **contacto por correo** **(SA)** |
| | `T1485` | Destrucción de datos | Mencionado borrado de ficheros **(DW)** |
| | **`T0828` / `T0831`** *(ATT&CK para ICS)* | **Pérdida de productividad e ingresos; manipulación del control** | **RECLAMADO, NO VERIFICADO.** Cifrador para SCADA diseñado para empujar los sistemas «hasta que el hardware falle» **(AT)**. Se consigna **con la marca de reclamación** y se desarrolla en `E-3` |

**Las ▲, y por qué.** `T1650` es el hallazgo del informe: **es la primera vez que esta cartera marca la adquisición de acceso como prioridad de detección**, y lo hace porque el programa la industrializa — y la contramedida no es una detección sino `X-5.1`. `T1133` es el vector de los dos casos chilenos. `T1562.001`, `T1070.001`, `T1135` y `T1021` son las cuatro funciones que **el propio cifrador** ejecuta, lo que comprime la cadena y las convierte en la última oportunidad real. Y `T1486` está marcada por el **patrón de cifrado parcial**, que decide cómo se mide el alcance.

> **Y una nota sobre la última fila, que es inusual en esta cartera.** Es la
> primera vez que un informe de este repositorio consigna una técnica del
> marco de sistemas de control industrial **a partir de una reclamación del
> adversario y no de una observación**. Se hace porque el dato existe y
> ocultarlo sería peor, y se marca con `(AT)` y con la advertencia expresa
> para que nadie lo trate como observado. **Si alguien extrae esta tabla sin
> la leyenda, habrá convertido una reclamación en un hecho**, y es el riesgo 1
> del pre-mortem.

## T-3. Dónde atacamos en la Pirámide del Dolor

| Nivel | Valor aquí | Por qué |
|---|---|---|
| **Hashes** | **No disponibles para Dire Wolf; escasos para los otros** | Tres de las fuentes primarias no fueron accesibles (`G-1`), y **los indicadores de Dire Wolf no se transcriben** por la regla de `CTI-2026-032`. Además, un cifrador **construido a medida por víctima** tiene un hash distinto por víctima: el nivel es estructuralmente inútil contra `(DW)` |
| **Direcciones IP y dominios** | **Cercano a nulo** | Negociación en portales por víctima y en servicios ocultos; y en el caso de `(SA)`, **por correo electrónico** |
| **Artefactos de red** | **Bajo-medio** | Lo más específico es el **inicio de sesión de una cuenta de servicio por la red privada virtual**, que es más un artefacto de identidad que de red |
| **Artefactos de anfitrión** | **Medio-alto** | Extensión `.Sauron` y nota `#HowToRecover.txt`; **nota con identificador de sala y credenciales embebidas** `(DW)`; el **patrón de cifrado parcial de 1 MiB cada 51 MiB** `(DM)`, que es una firma de contenido y no de fichero |
| **Herramientas** | **Bajo** | Ninguna de las tres fuentes documenta un conjunto de herramientas auxiliares detallado, en buena parte porque **el cifrador hace por sí mismo el descubrimiento, el movimiento lateral y la evasión** |
| **TTP** | **El máximo, y aquí es casi lo único** | **(1)** El **acceso remoto como vector**, que ni el programa ni sus afiliados pueden abandonar porque es lo que compran. **(2)** El **tempo de dos a tres días**, que el programa impone. **(3)** Las **cuatro funciones embebidas en el cifrador** —evasión, borrado de registros, descubrimiento y movimiento lateral—, que no puede quitar sin perder eficacia |

> **La consecuencia de inversión es la más acusada de este lote, y conviene
> decirla sin adornos: este expediente no da indicadores, da mecanismos.** Un
> consumidor que mida el valor de un informe por filas ingeribles concluirá
> que no aporta nada. Lo que aporta son **la pregunta 1 de `O-4.1`**, que
> responde al vector de los dos casos chilenos, y el **método del `Anexo D`**,
> que evita escribir expedientes sobre nombres. Las dos cosas valen más que
> una lista de hashes de un cifrador que se recompila por víctima.

## T-4. Hipótesis de caza prioritarias

| Id | Hipótesis | Dónde se busca | Qué confirma | Coste |
|---|---|---|---|---|
| **H-1** | Alguna **cuenta de servicio o de respaldo** ha iniciado sesión interactiva por la red privada virtual en los últimos doce meses | Registros de autenticación del concentrador, cruzados con el inventario de cuentas de servicio | **La señal que los dos casos chilenos sugieren**, y la que la fuente primaria pide prohibir | **Bajo, y es la primera** |
| **H-2** | Hay **credenciales de acceso remoto con usuario y contraseña iguales**, o con contraseñas triviales, en el concentrador o en el directorio | Auditoría de credenciales | Es la circunstancia **reportada** del caso de la clínica | **Bajo** |
| **H-3** | Algún secreto expuesto a concentradores de red privada virtual, integraciones de directorio, guiones o herramientas de respaldo **no se ha rotado en más de un año** | Inventario de secretos | Tercera pieza de la recomendación de la fuente, y la que **casi nunca se hace** | **Medio** |
| **H-4** | Hubo **enumeración masiva de recursos compartidos seguida de movimiento lateral en menos de 24 horas** | Registros de acceso a recursos compartidos y de autenticación | **La fase intermedia de la cadena, dentro de la ventana de dos a tres días** | **Medio** |
| **H-5** | Se borraron **registros de eventos** en más de un equipo en una ventana corta | Registro del propio registro de eventos | Función documentada del cifrador, y es ruidosa | **Bajo** |
| **H-6** | Hay ficheros grandes **corrompidos en trozos regulares de 1 MiB separados por 51 MiB** | Análisis de ficheros en un incidente | **Firma de contenido del cifrado parcial.** Permite medir el alcance real sin depender de la extensión | **Bajo en un incidente; no aplicable antes** |
| **H-7** | Existe la extensión **`.Sauron`** o una nota **`#HowToRecover.txt`** en algún almacenamiento | Barrido de ficheros | La familia de `O-1.3`. **Preservar muestras**: la familia no es identificable por las herramientas públicas | **Trivial** |
| **H-8** | Hay cifrado o intento de cifrado en **ESXi** o en **Linux**, no sólo en Windows | Registros del hipervisor y de los anfitriones Linux | Las tres plataformas están en el alcance, **y el hipervisor suele estar peor instrumentado** | **Medio** |
| **H-9** | Nuestra **red de operación** es alcanzable desde la red de oficina con credenciales de oficina | Ejercicio de verificación de segmentación | **La pregunta proporcionada a la reclamación de SCADA** (`E-3`). No busca al adversario: comprueba un supuesto propio | **Medio, y es de arquitectura** |

> **Una nota sobre `H-9`, que es la única hipótesis de este informe que no
> busca al adversario.** Comprobar si la red de operación es alcanzable desde
> la de oficina **no depende de que la reclamación del cifrador para SCADA sea
> cierta**. Si es falsa, la comprobación sigue valiendo contra todos los
> demás; si es cierta, es lo único que importaba. **Es la forma correcta de
> responder a una reclamación de confianza baja: con una medida cuyo valor no
> dependa de que la reclamación sea verdadera.**

## T-5. Brechas de visibilidad que hay que cerrar primero

| Brecha | Qué nos impide ver | Coste | Prioridad |
|---|---|---|---|
| **No se sabe si las cuentas de servicio y de respaldo pueden entrar por la red privada virtual** | **El vector de los dos casos chilenos** | **Trivial preguntarlo; bajo cerrarlo** | **1** |
| No hay inventario de **cuándo se rotó cada secreto** expuesto a acceso remoto, directorio, guiones y respaldo | Lo que un corredor de acceso podría estar vendiendo ya | Medio | **2** |
| El **programa de caza no está dimensionado** para dos o tres días de permanencia | Todo lo que entra y cifra en setenta y dos horas | Medio: es frecuencia y alcance | **3** |
| El **hipervisor está peor instrumentado** que los servidores | Un tercio del alcance del cifrador | Medio | **4** |
| No se **alerta sobre intentos bloqueados** de deteriorar los controles de seguridad | La fase de evasión, que el propio cifrador ejecuta. **Es la misma brecha que `CTI-2026-041`, y se cierra una vez para los dos** | Bajo | **5** |
| **No se ha comprobado la segmentación entre red de oficina y red de operación** | `H-9`, y es un supuesto propio no verificado | Medio | **6** |

---

# NIVEL TÉCNICO
### Para: Ingeniería de detección · Automatización · TIP/SIEM · Acceso Remoto · Vida útil: meses

## X-1. Arsenal y capacidad

| Nombre | Qué es | Nota que importa |
|---|---|---|
| **Cifrador de Devman** | Generado desde el portal, para **Windows, ESXi o Linux**, con opciones **por víctima** | **ChaCha20-Poly1305.** Completo hasta **3 MiB**; por encima, **1 MiB cada 51 MiB**. Y hace por sí mismo: comprobación de privilegios, **deterioro de controles de seguridad**, terminación de procesos y servicios, **inhibición de la recuperación**, **borrado de registros de eventos**, descubrimiento local y de recursos compartidos, **movimiento lateral**, cifrado multihilo, nota y **autoborrado opcional** |
| **Portal de afiliados** (v3, enero de 2026) | Plataforma web de gestión | Generación de cargas, finanzas, chat con la víctima, soporte, expedientes de víctima, equipos, pagos; **estados del ciclo de vida, control de invitaciones, seguimiento de plazos, campos de ingresos y acceso operativo compartido** |
| **«Redes» por país** | **Servicio de acceso del propio programa** | **El hallazgo del informe.** El servicio integra la distribución de accesos con el despliegue del cifrador, y pregunta al afiliado si usará acceso propio o del programa |
| **Cifrador de Dire Wolf** | Binario en **Go**, empaquetado con **UPX** | **Construido a medida para cada objetivo.** Nota con **identificador de sala y credenciales de acceso específicos de la víctima** |
| **Cifrador de Sauron** | Familia no identificable por las herramientas públicas | Extensión **`.Sauron`** más identificador de víctima **y correo del atacante**; nota **`#HowToRecover.txt`**; **sin descifrador conocido** |
| *(reclamado)* **Cifrador para SCADA** | — | **RECLAMACIÓN DEL ADVERSARIO, SIN VERIFICAR.** Véase `E-3`. Lo documentado es que **la política del programa instruye a pedirlo** |

### X-1.1 — Lo que no hay, y lo que el cifrador hace por sí mismo

**Lo que no hay, y limita este informe:** **no hay conjunto de herramientas auxiliares documentado** para ninguno de los tres. No hay `Mimikatz`, ni `Impacket`, ni herramientas de exfiltración nombradas, ni infraestructura de mando. Y hay dos razones distintas: una es **nuestra** —tres fuentes primarias inaccesibles (`G-1`)— y la otra es **del objeto**, y es la interesante.

**Lo que el cifrador hace por sí mismo, y es la razón:**

| Función | Lo habitual | Aquí |
|---|---|---|
| Evasión de la defensa | Herramientas aparte, desplegadas antes | **Dentro del cifrador** |
| Borrado de registros | `wevtutil` o un lote | **Dentro del cifrador** |
| Descubrimiento de recursos compartidos | `net view`, `SharpShares` | **Dentro del cifrador** |
| Movimiento lateral | `PsExec`, `wmic`, RDP | **Dentro del cifrador** |
| Inhibición de recuperación | `vssadmin` | **Dentro del cifrador** |
| Borrado de rastros | Lote de limpieza | **Autoborrado del propio cifrador** |

**Y la consecuencia es la que importa para la detección:** un cifrador que integra las seis funciones **comprime la cadena de ataque en un solo proceso y en una sola ventana de minutos**. Eso elimina las detecciones intermedias clásicas —ver `PsExec` antes de ver el cifrado, ver `vssadmin` antes de ver el cifrado— porque **ya no hay un antes**. Lo que queda son dos cosas: **lo que ocurre antes de ejecutar el cifrador** —el acceso remoto, el descubrimiento previo, el movimiento del operador— y **el bloqueo del propio cifrador**.

**Esa es la justificación técnica de que las dos recomendaciones de este informe sean `X-5.1` —cerrar el acceso vendible— y la regla de intentos bloqueados de `CTI-2026-041`.** No es una elección de estilo: es que **no hay mucho en medio donde mirar**.

## X-2. Artefactos de anfitrión persistentes

| Artefacto | Dónde | Confianza |
|---|---|---|
| Ficheros grandes con **trozos de 1 MiB corrompidos cada 51 MiB** | Sistema de ficheros | **Alta, y es la firma para medir el alcance real** sin depender de la extensión |
| Ficheros de hasta 3 MiB **íntegramente cifrados** | Sistema de ficheros | Alta |
| **Registros de eventos borrados** en varios equipos en ventana corta | Registro de eventos | Alta |
| Extensión **`.Sauron`** más identificador de víctima y correo del atacante; nota **`#HowToRecover.txt`** | Sistema de ficheros | **Alta, y es casi lo único accionable de ese actor** |
| Nota de rescate con **identificador de sala y credenciales de acceso embebidas** | Sistema de ficheros | **Alta, y es el artefacto más específico de Dire Wolf** |
| **Inicio de sesión interactivo de una cuenta de servicio o de respaldo** en el concentrador de acceso remoto | Registros de identidad | **Alta como anomalía.** Es más un artefacto de identidad que de anfitrión, y es el que más vale |

## X-3. Lógica de detección prioritaria

### X-3.1 — `D-1` · Cuenta de servicio o de respaldo por el acceso remoto · **la detección de este informe**

```
INVENTARIO previo (y es todo el trabajo):
   lista de cuentas de SERVICIO y de RESPALDO, y de cuentas sin persona
   detras — las que existen para que un proceso funcione

EVENTO: autenticacion CORRECTA en el concentrador de acceso remoto
        (red privada virtual, escritorio remoto publicado, pasarela)
Y       la cuenta esta en esa lista
ENTONCES alertar SIEMPRE

Razon: la recomendacion literal de la fuente primaria es PROHIBIR que
esas cuentas inicien sesion interactiva por la red privada virtual
salvo requisito operativo documentado. Mientras la prohibicion no
este desplegada, la deteccion es el sustituto.

Y la version PREVENTIVA es mucho mejor, y es X-5.1: denegar por
politica, con excepciones documentadas y revisables.
```

**Por qué es la primera.** Porque es la señal que los dos casos chilenos de este lote sugieren —los dos por acceso remoto, uno de ellos con la circunstancia reportada de usuario y contraseña idénticos—, porque las cuentas de servicio son el punto ciego clásico, y porque **un acceso de cuenta de servicio es exactamente la clase de credencial que se vende en un mercado**, que es el mecanismo de `KJ-4`.

### X-3.2 — `D-2` · El cifrador en ejecución, por sus funciones embebidas

```
CUALQUIERA de estas, en un mismo equipo y en una ventana de 30 min:
 - deterioro o terminacion de servicios de seguridad
 - borrado de registros de eventos
 - enumeracion masiva de recursos compartidos de red
 - inhibicion de la recuperacion
 - y, sobre todo, DOS O MAS de las anteriores
ENTONCES INCIDENTE CON PRIORIDAD MAXIMA

Razon tecnica: este cifrador integra las seis funciones en un solo
proceso (X-1.1), de modo que NO HAY UN "ANTES" donde mirar. Las
detecciones intermedias clasicas no aplican, y la coincidencia de dos
o mas de estas senales en media hora es el propio cifrador
ejecutandose.

Y conviene unirla a la regla de CTI-2026-041, X-3.2: alertar tambien
sobre los INTENTOS BLOQUEADOS, no solo sobre los exitosos. Se cierra
una vez para los dos informes.
```

### X-3.3 — `D-3` · Medir el alcance por el patrón de cifrado parcial

```
EN UN INCIDENTE, para medir el alcance real:

 - ficheros de hasta 3 MiB: cifrados POR COMPLETO
 - ficheros mayores: corrompidos en TROZOS DE 1 MiB CADA 51 MiB

Consecuencia practica, y es la que hay que llevar a quien gestione las
copias: un fichero grande "parcialmente cifrado" NO es parcialmente
recuperable. Tocar ~2 % de un fichero en trozos regulares lo inutiliza
igual que cifrarlo entero, y cuesta cincuenta veces menos tiempo.

Por eso la ventana para CORTAR un cifrado sobre un almacenamiento
grande esta en MINUTOS y no en horas: el adversario no necesita
procesar el volumen, solo tocarlo.
```

### X-3.4 — `D-4` · Artefactos de identificación de familia

```
Dire Wolf:
 - nota de rescate que contiene un IDENTIFICADOR DE SALA y
   CREDENCIALES DE ACCESO especificos de la victima
   -> artefacto muy especifico, y senal de operacion dirigida

Sauron:
 - extension .Sauron mas identificador de victima mas CORREO del
   atacante
 - nota #HowToRecover.txt
 -> PRESERVAR MUESTRAS: la familia NO es identificable por las
    herramientas publicas, y no hay descifrador conocido. Una muestra
    bien conservada vale mas aqui que en cualquier otro caso de este
    lote.

Devman:
 - extension y nota no documentadas con precision en las fuentes
   accesibles (G-1)
 - lo identificable es el PATRON DE CIFRADO PARCIAL de D-3
```

## X-4. Consultas de caza

```kql
// =====================================================================
// H-1 y D-1 · LA CONSULTA DE ESTE INFORME: cuentas de servicio y de
// respaldo autenticandose en el acceso remoto.
//
// Es la recomendacion literal de la fuente primaria y la que responde
// al vector de los dos casos chilenos de este lote.
// =====================================================================

// Paso 0: el inventario. Es TODO el trabajo de esta consulta.
let cuentas_sin_persona = dynamic([
    // cuentas de servicio, de respaldo, de integracion, de aplicacion
    // — las que existen para que un proceso funcione, no una persona.
    "svc_backup", "svc_sql", "svc_veeam", "svc_monitor",
    "backupadmin", "sa_integration", "svc_ldap"
]);
SigninLogs
| where TimeGenerated > ago(365d)
| where ResultType == 0                            // solo EXITOS
| where AppDisplayName has_any ("VPN", "Gateway", "Remote",
                               "AnyConnect", "GlobalProtect",
                               "Pulse", "NetScaler", "Citrix")
     or ClientAppUsed has "VPN"
| extend cuenta = tolower(split(UserPrincipalName, "@")[0])
| where cuenta in~ (cuentas_sin_persona)
       or cuenta startswith "svc" or cuenta startswith "sa_"
       or cuenta has "backup" or cuenta has "service"
| project TimeGenerated, UserPrincipalName, AppDisplayName,
          IPAddress, Location, DeviceDetail, ResultType
| order by TimeGenerated desc

// Y la pregunta que ningun guion responde: para cada acierto,
// ¿existe un REQUISITO OPERATIVO DOCUMENTADO para que esa cuenta
// entre por la red privada virtual? Si no existe, hay que cerrarlo.
```

```kql
// =====================================================================
// H-4 y D-2 · La fase intermedia dentro de la ventana de 2-3 dias:
// enumeracion masiva de recursos compartidos seguida de movimiento
// lateral en menos de 24 horas.
//
// Contra un adversario cuyo tempo lo impone su empleador, la correlacion
// TEMPORAL ESTRECHA es lo que distingue el ataque del ruido.
// =====================================================================

let ventana_lateral = 24h;
let enumeracion = DeviceNetworkEvents
| where Timestamp > ago(90d)
| where RemotePort == 445
| summarize destinos = dcount(RemoteIP), intentos = count()
        by DeviceName, AccountName = InitiatingProcessAccountName,
           hora = bin(Timestamp, 1h)
| where destinos >= 20                   // enumeracion, no uso normal
| project DeviceName, AccountName, hora_enum = hora, destinos;
let lateral = DeviceLogonEvents
| where Timestamp > ago(90d)
| where LogonType in ("Network", "RemoteInteractive")
| summarize equipos = dcount(DeviceName) by AccountName,
            hora = bin(Timestamp, 1h)
| where equipos >= 5
| project AccountName, hora_lat = hora, equipos;
enumeracion
| join kind=inner (lateral) on AccountName
| where hora_lat between (hora_enum .. hora_enum + ventana_lateral)
| project AccountName, hora_enum, destinos, hora_lat, equipos,
          DeviceName
| order by hora_enum desc
```

```bash
# =====================================================================
# H-6 y D-3 · Medir el alcance real por el patron de cifrado parcial.
#
# Un fichero grande "parcialmente cifrado" NO es parcialmente
# recuperable: tocar ~2 % en trozos regulares lo inutiliza igual que
# cifrarlo entero. Esta comprobacion sirve para dimensionar el dano en
# un incidente, no para detectarlo.
# =====================================================================

# Busca trozos de alta entropia de 1 MiB separados por ~51 MiB.
# Uso: ./patron.py <fichero>
cat > patron.py <<'EOF'
import sys, math

TROZO   = 1024 * 1024          # 1 MiB cifrado
PASO    = 51 * 1024 * 1024     # cada 51 MiB
UMBRAL  = 7.8                  # bits/byte; >7.8 ~ cifrado o comprimido

def entropia(b: bytes) -> float:
    if not b:
        return 0.0
    frec = [0] * 256
    for x in b:
        frec[x] += 1
    n = len(b)
    return -sum((c/n) * math.log2(c/n) for c in frec if c)

def analizar(ruta: str) -> None:
    with open(ruta, "rb") as f:
        f.seek(0, 2); tamano = f.tell()
        if tamano <= 3 * 1024 * 1024:
            f.seek(0)
            e = entropia(f.read(min(tamano, 65536)))
            print(f"{ruta}: <=3 MiB, entropia {e:.2f} "
                  f"-> {'CIFRADO COMPLETO probable' if e > UMBRAL else 'sin indicios'}")
            return
        altos = bajos = 0
        off = 0
        while off < tamano:
            f.seek(off)
            e = entropia(f.read(min(65536, tamano - off)))
            if e > UMBRAL: altos += 1
            else:          bajos += 1
            off += PASO
        print(f"{ruta}: {tamano/1048576:.0f} MiB, "
              f"{altos} muestras de alta entropia / {bajos} de baja "
              f"-> {'PATRON DE CIFRADO PARCIAL' if altos and bajos else 'no concluyente'}")

for r in sys.argv[1:]:
    try:
        analizar(r)
    except OSError as e:
        print(f"{r}: {e}")
EOF

# AVISO: un resultado de alta entropia tambien lo dan los ficheros ya
# comprimidos o cifrados legitimamente (zip, jpg, pdf, bases cifradas).
# La senal es la ALTERNANCIA REGULAR de trozos altos y bajos, no la
# entropia alta por si sola.
```

## X-5. Mitigaciones de configuración con efecto directo

Cuatro. **Ninguna exige comprar un producto de seguridad**, y las tres primeras son la recomendación literal de la fuente primaria.

### X-5.1 — Cerrar el acceso vendible · **la medida de mayor efecto del informe**

Tres piezas, y las tres vienen de la fuente:

1. **Prohibir que las cuentas de servicio y de respaldo inicien sesión interactiva por la red privada virtual**, salvo requisito operativo documentado. **Es la primera porque es la más concreta y la menos aplicada**: nadie trata a una cuenta de servicio como un usuario, y por eso nadie le mira el acceso remoto.
2. **Exigir segundo factor resistente a suplantación** para el acceso remoto y la administración privilegiada.
3. **Rotar los secretos expuestos a concentradores de red privada virtual, integraciones de directorio, guiones y herramientas de respaldo**, **dando prioridad a los que conceden administración local o de dominio**.

**Por qué es la medida de mayor efecto, y es un razonamiento de mecanismo y no de indicador.** Si el programa **compra accesos** y los **distribuye por país** (`KJ-4`), entonces la exposición de una organización no depende de cuán atractiva sea: depende de **que exista un acceso vendible a su red**. Y los accesos vendibles tienen casi siempre la misma forma: credenciales válidas de acceso remoto, con preferencia por las que nadie vigila.

### X-5.2 — Dimensionar la caza para dos o tres días

El programa **impone al afiliado una ventana de ejecución de dos a tres días**. Eso convierte cualquier ciclo de caza más lento en inútil contra este adversario, y tiene una contrapartida favorable que conviene aprovechar: **un adversario con prisa hace ruido**.

**Las dos consecuencias de configuración:**

1. **Las detecciones de comportamiento ruidoso** —enumeración masiva de recursos compartidos, movimiento lateral rápido, borrado de registros— **rinden aquí lo que no rinden contra un actor de espionaje**, y merecen umbrales más sensibles.
2. **Y la correlación temporal estrecha es el discriminante**: enumeración seguida de movimiento lateral **en menos de veinticuatro horas** es la consulta de `X-4`, y es específica precisamente porque el tempo es un parámetro de gestión del adversario y no una casualidad.

### X-5.3 — Copias que cubran el hipervisor, y fuera del alcance del cifrador

El cifrador se construye para **Windows, ESXi y Linux**. Tres requisitos:

1. **Copias no alcanzables desde un recurso compartido de red**, porque el cifrador enumera los recursos compartidos por sí mismo.
2. **Copias inmutables o fuera de línea**, porque la inhibición de la recuperación es una función embebida.
3. **Y copias del hipervisor**, no sólo de las máquinas que corren en él. Un plan que trate la plataforma de virtualización como refugio no es válido.

**Y la advertencia de tempo que `D-3` justifica:** con cifrado parcial de ~2 % en trozos regulares, **la ventana para cortar un cifrado sobre un almacenamiento grande está en minutos**. El adversario no necesita procesar el volumen; sólo tocarlo.

### X-5.4 — Comprobar la segmentación entre red de oficina y red de operación

Es la medida proporcionada a la reclamación del cifrador para SCADA (`E-3`), **y su valor no depende de que la reclamación sea cierta**. La pregunta es concreta y contestable: **¿qué separa la red de oficina de la red de operación, y se ha comprobado alguna vez con un ejercicio y no con un diagrama?**

> ⚠ **Y las dos cosas que este informe NO recomienda.** **Primera: reasignar
> esfuerzo de tecnología de operación por la reclamación del cifrador para
> SCADA.** No hay muestra, no hay incidente, no hay compañía nombrada. El
> juicio es *poco probable* con confianza *baja*, y actuar sobre él sería
> actuar sobre publicidad del adversario. **Segunda: construir detecciones
> sobre los nombres de los tres grupos.** `E-4` lo desarrolla con cuatro
> casos de esta cartera: **el nombre de un grupo de extorsión es el activo
> más desechable de su operación**, y uno de los tres de este informe lleva
> siete meses sin publicar una víctima mientras se valora que su operador
> sigue trabajando bajo otra marca.

---

## 14. Brechas de inteligencia y nuevos requisitos de colección

| Id | Brecha | Por qué importa | Cómo se cierra | Coste |
|---|---|---|---|---|
| `G-1` | **Tres fuentes primarias no accesibles**: el informe del portal de afiliados, el análisis de Dire Wolf y el aviso del centro nacional de Singapur | **Es la brecha principal.** Por ella **no se transcriben los indicadores de Dire Wolf**, y todo el material del portal llega por cita | Solicitud a los autores; y resolver el acceso a publicaciones de proveedor, que es la misma tarea que `G-1` de `CTI-2026-039` | **Bajo, y es la prioridad 1** |
| `G-2` | **De Sauron no hay ningún análisis primario** | Decide si es una operación o una herramienta (`O-1.3`) | Búsqueda en rastreadores de sitios de filtración por nombre de grupo; y en repositorios de muestras | Bajo |
| `G-3` | **No hay informe independiente del caso de la Clínica Dávila** | El volumen y la vía de entrada los dicen el atacante y la prensa; la institución no ha confirmado el alcance | Informe de la institución o de la autoridad chilena, si se publica | Medio, y fuera de nuestro control |
| `G-4` | **No sabemos si el cifrador para SCADA existe** | `KJ-5` y `E-3`. Su confirmación sería **un cambio de categoría para esta cartera** | Vigilancia. `I-1` es el disparador | **Fuera de nuestro alcance** |
| `G-5` | No sabemos bajo qué marca opera ahora la persona tras el alias Devman | Decide si las detecciones de este expediente siguen siendo pertinentes **y bajo qué nombre** | Vigilancia de foros y de linajes de código | Medio |
| `G-6` | **No sabemos si nuestras cuentas de servicio y de respaldo pueden entrar por la red privada virtual** | **Es la medida de mayor efecto del informe** | **Una consulta a Identidad** | **Trivial, y es la prioridad 1 de acción** |
| `G-7` | No sabemos cuándo se rotaron los secretos expuestos a acceso remoto, directorio, guiones y respaldo | Lo que un corredor de acceso podría estar vendiendo ya | Inventario de secretos | Medio |
| `G-8` | No se ha comprobado la segmentación entre red de oficina y red de operación | `H-9`, y es un supuesto propio no verificado | Ejercicio de verificación | Medio |
| `G-9` | No hay victimología por país publicada para ninguno de los tres | `KJ-3` y `H-D` de `O-6` | Recuento propio sobre sitios de filtración, con la salvedad de que **cuentan reclamaciones** | Medio |
| `G-10` | No leemos los relatos que Devman publica sobre cómo entró en sus víctimas | Un boletín oficial señala que los publica. **Es inteligencia gratuita, específica y nadie la recoge por sistema** | Encargarlo | **Trivial, y de las más rentables** |

**Disparadores de reevaluación.** `I-1`: **primer uso documentado de un cifrador contra sistemas de control industrial por un actor criminal** — sería un cambio de categoría para toda esta cartera y no sólo para este informe. `I-2`: **Devman reaparece con marca propia**, o se identifica la marca en la que opera como afiliado. `I-3`: aparición de una víctima **colombiana o peruana** de cualquiera de los tres. `I-4`: publicación de un análisis primario de **Sauron** que establezca que es una operación con sitio de filtración, lo que refutaría `KJ-9`. `I-5`: publicación del alcance verificado del caso chileno. `I-6`: **Dire Wolf abre un programa de afiliados**, lo que cambiaría su victimología de preferencias propias a inventario de accesos ajeno. `I-7`: aparición de un cuarto caso del patrón de `E-4` —una marca que se apaga y una persona que continúa—, que lo convertiría en una serie.

---

# ANEXOS

## Anexo A — Indicadores de compromiso

> ⚠ **`PAP:AMBER` — y este anexo empieza reconociendo lo que no tiene.**
> **Aporta muy pocos valores y mucha estructura**, por dos razones: tres de
> sus fuentes primarias no fueron accesibles (`G-1`), de modo que **los
> indicadores de Dire Wolf no se transcriben** por la regla que
> `CTI-2026-032` adoptó ante un anexo ilegible; y porque **un cifrador
> construido a medida para cada víctima no tiene un hash que compartir**.
>
> **Lo que el anexo sí tiene, y es lo que hay que desplegar:** el patrón de
> identidad de `A.1` —una cuenta de servicio autenticándose en el acceso
> remoto—, que responde al vector de los dos casos chilenos de este lote; la
> firma de contenido de `A.2`, que permite **medir el alcance real** de un
> cifrado sin depender de la extensión; y los artefactos de identificación de
> familia de `A.4`.
>
> **Tres advertencias más.** (1) **`A.5` lleva una columna de quién lo dice**,
> aplicando el `Anexo D` de `CTI-2026-041`: la reclamación del cifrador para
> SCADA está ahí **marcada como reclamación**, y extraerla sin esa marca es
> el riesgo 1 del pre-mortem. (2) **`A.3` consigna una ausencia verificada** —
> Colombia y Perú— para que figure con su razón y nadie repita la búsqueda.
> (3) **Ningún dato personal de los pacientes expuestos se reproduce**, y la
> decisión se explica en `A.7`.

### A.1 — El patrón que decide, y es de identidad · **leer primero**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| pattern | **Autenticación correcta de una cuenta de servicio, de respaldo o sin persona detrás, en un concentrador de acceso remoto** —red privada virtual, escritorio remoto publicado, pasarela— | **El indicador de mayor valor del informe, y no es técnico: es de identidad.** Responde al vector de los **dos casos chilenos de este lote** —salud en diciembre de 2025 y energía en enero de 2026, los dos por acceso remoto— y, más importante, **es exactamente la clase de credencial que se vende en un mercado de accesos**, que es el mecanismo de `KJ-4`: el programa de Devman **ofrecía «redes» por país** y preguntaba al afiliado si usaría acceso propio o suministrado. La recomendación **literal** de la fuente primaria es **prohibirlo** salvo requisito operativo documentado | **Alta** | **Sin caducidad.** Es estructural al modelo de negocio del adversario | **PREVENCIÓN antes que detección** (`X-5.1`): denegar por política con excepciones documentadas. Mientras no esté desplegada, **detección** (`D-1`) |
| pattern | Credencial de acceso remoto **con usuario y contraseña idénticos**, o trivialmente derivable | **Es la circunstancia reportada del caso de la Clínica Dávila**: según lo publicado, Devman entró por una red privada virtual que usaba usuario y contraseña iguales. **Lo reporta la prensa recogiendo al atacante**, no un informe independiente | Media *(vía indirecta)* | Sin caducidad | **Auditoría de credenciales** (`H-2`), no detección |
| pattern | **Secreto expuesto a un concentrador de red privada virtual, a una integración de directorio, a un guion o a una herramienta de respaldo, sin rotar en más de un año** —con prioridad a los que conceden administración local o de dominio— | Tercera pieza de la recomendación literal de la fuente, **y la que casi nunca se hace**. No es un indicador de compromiso: es **un inventario de lo que un corredor de acceso podría estar vendiendo ya** | Media-alta | Sin caducidad | **Inventario y rotación** (`H-3`, `X-5.1`) |
| pattern | **Enumeración masiva de recursos compartidos de red seguida de movimiento lateral en menos de 24 horas** | **La fase intermedia de la cadena, dentro de la ventana de dos a tres días que el programa impone al afiliado.** La correlación temporal estrecha es el discriminante: contra un adversario cuyo tempo lo fija su empleador, **la prisa es la firma** | Media-alta | Sin caducidad | **Caza** (`D-2`, `H-4`) |

### A.2 — La firma de contenido del cifrado, y sirve para medir el daño

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| pattern | **Ficheros de hasta 3 MiB inclusive, cifrados por completo; y ficheros mayores corrompidos en trozos de 1 MiB cada 51 MiB** | **La firma de contenido del cifrador de Devman, y la única forma fiable de medir el alcance real de un incidente** sin depender de la extensión del fichero —que se puede renombrar— ni de la nota. **Y la consecuencia que hay que llevar a quien gestione las copias: un fichero grande «parcialmente cifrado» NO es parcialmente recuperable.** Tocar un dos por ciento en trozos regulares lo inutiliza igual que cifrarlo entero, y cuesta cincuenta veces menos tiempo: por eso **la ventana para cortar un cifrado sobre un almacenamiento grande está en minutos y no en horas** | **Alta** | Sin caducidad mientras no cambie el cifrador | **Medición de alcance en respuesta a incidentes** (`D-3`, `H-6`). **La señal es la alternancia regular de trozos de alta y baja entropía, no la entropía alta por sí sola** |
| pattern | **ChaCha20-Poly1305** | Algoritmo del cifrador. Cifrado autenticado moderno: **no hay esperanza de recuperación por fallo criptográfico**. La única vía es la copia de seguridad | Alta | Sin caducidad | **Evaluación de recuperabilidad.** Es el dato que Dirección necesita el primer día |
| pattern | Cifrado o intento de cifrado en **ESXi** o en **Linux** | El cifrador se genera para las **tres** plataformas desde el portal. **Y el hipervisor suele estar peor instrumentado que los servidores** | Alta | Sin caducidad | **Detección**, y revisión del alcance del plan de copias (`H-8`, `X-5.3`) |

### A.3 — Victimología, con sus grados · **incluida una ausencia verificada**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| cartera | **Clínica Dávila, Santiago de Chile. Ataque reportado hacia el 2025-12-18; publicación parcial de los datos hacia el 2025-12-31** | **La única víctima regional nombrada de los tres actores**, y el segundo caso chileno de este lote por acceso remoto. **Hecho observable**: la publicación en el sitio del grupo y la posterior filtración en un foro | **Alta para los hechos públicos** | No caduca | **Citable como hecho** |
| cartera | **Más de 250 GB de registros sensibles de pacientes** | **Afirmación del atacante.** Es la métrica con más incentivo para inflar. **Parcialmente verificable** sólo si publicó listados | **Media; afirmación del adversario** | No caduca | **Citable SÓLO con atribución al atacante** |
| cartera | **Entrada por la red privada virtual, con usuario y contraseña idénticos** | **Reportado por la prensa recogiendo al atacante.** Cae en la categoría más creíble de un relato adversario —no gana nada mintiendo sobre el producto por el que entró— **pero sí gana presentando la entrada como técnica en lugar de como un descuido**; y aquí describe precisamente un descuido, lo que la hace **más** creíble | **Media-alta; afirmación del adversario vía prensa** | No caduca | **Citable con atribución.** Es la base de `X-5.1` |
| cartera | **La institución reconoció «un incidente de un tercero» y no ha confirmado formalmente que fuera extorsión ni que afectara a datos de pacientes** | **Declaración de la víctima, por omisión.** **Las dos cosas pueden ser ciertas a la vez**: el marco del `Anexo D` de `CTI-2026-041` explica por qué un comunicado que no menciona algo no lo niega | **Alta como declaración** | No caduca | **Citable como declaración de la víctima, no como alcance verificado** |
| cartera | **184 víctimas reclamadas por Devman; ninguna publicada desde el 2026-02-04**. Caída de **82** en el cuarto trimestre de 2025 a **25** en el primero de 2026, **24 de ellas en enero** | **Recuento de reclamaciones en un sitio de filtración, no de brechas verificadas.** Casi 50 en Estados Unidos; sectores de tecnología, salud, servicios financieros, servicios profesionales y gobierno | Media | — | **Citable como reclamaciones** |
| cartera | **Dire Wolf: 100 víctimas en 32 países a 2026-08-19, con 43 nuevas en un solo mes.** Desde **11 países** en junio de 2025 | Recuento de reclamaciones. **Y la tensión con «cifradores a medida por víctima» y «equipo nuclear reducido» se consigna sin resolver** (`O-3.C`) | Media | — | **Citable como reclamaciones** |
| cartera | **AUSENCIA VERIFICADA: no hay actividad documentada de ninguno de los tres grupos en Colombia ni en Perú** | Se buscó expresamente en español y en inglés, en diez fuentes. **Se consigna la ausencia para que figure con su razón y nadie repita la búsqueda.** Y con la causa estructural del «no»: **un sitio de filtración sólo publica a quien no paga**, de modo que la victimología publicada mide la negativa a pagar y no el ataque | **Ausencia verificada en diez fuentes** | — | **Contexto.** `KJ-3` explica qué significa y qué no |
| cartera | **Sauron: ninguna víctima nombrada, ningún recuento, ningún sitio de filtración localizado, en dos años desde su primera observación** | Es la base de `KJ-9` y de `O-1.3` | **Ausencia verificada** | — | **Contexto** |

### A.4 — Artefactos de identificación de familia

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| filename | Extensión **`.Sauron`**, añadida junto a **un identificador único de víctima y un correo electrónico del atacante**; nota **`#HowToRecover.txt`** | **Casi lo único accionable de ese actor** (`O-1.3`). La nota informa de que los ficheros fueron cifrados **y exfiltrados**, y amenaza con filtrar o vender. **Y el dato crítico para la respuesta: una herramienta pública de identificación de familias NO pudo reconocerla, de modo que no hay descifrador confirmado** | Alta | Sin caducidad | **Identificación de familia.** **PRESERVAR MUESTRAS**: aquí valen más que en cualquier otro caso de este lote, precisamente porque la familia no es identificable |
| pattern | Nota de rescate que contiene **un identificador de sala y credenciales de acceso específicos de la víctima** | **El artefacto más específico de Dire Wolf**, y su analista lo lee como señal de operación dirigida: cada nota lleva embebido lo necesario para entrar al portal de esa víctima concreta | Alta | Sin caducidad como patrón | **Identificación de familia** |
| pattern | Binario en **Go** empaquetado con **UPX**, **construido a medida para el objetivo** | Dire Wolf. **Y la consecuencia es que no hay hash compartible**: cada víctima recibe un binario distinto, de modo que el nivel de los hashes es estructuralmente inútil contra este actor | Alta | Sin caducidad | **Contexto para el análisis** |
| pattern | **Plazo de un mes** para pagar | Dire Wolf. **Contrasta con la ventana de ejecución de dos a tres días de Devman**, y sugiere un equipo que no está bajo presión de cuota — coherente con un equipo cerrado sin programa de afiliados | Media-alta | Sin caducidad | **Contexto de perfilado** |
| artefacto | *(Devman)* Extensión y nota **no documentadas con precisión en las fuentes accesibles** | Es `G-1`. **Lo identificable de este cifrador es el patrón de cifrado parcial de `A.2`**, que es una firma de contenido y no de nombre | — | — | **Se consigna la carencia** |

### A.5 — Lo que el adversario dice de sí mismo · **con la columna de quién lo dice**

> **Esta tabla aplica el `Anexo D` de `CTI-2026-041`, y su propósito es que
> nadie extraiga una reclamación del adversario como si fuera un hallazgo.**
> La fila del cifrador para SCADA es la razón principal de que exista.

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| artefacto | **«Cifrador especializado para SCADA»**, dirigido a una compañía de gas no identificada, diseñado para empujar los sistemas de control «más allá de sus parámetros de operación, procesadores, memoria y límites térmicos, forzándolos a acelerar y funcionar calientes hasta que el hardware falle» | **RECLAMACIÓN DEL ADVERSARIO EN UNA ENTREVISTA. SIN NINGUNA VERIFICACIÓN.** No nombra la compañía, no hay incidente público asociado, no hay muestra. **Máximo incentivo para exagerar**: es una afirmación de prestigio, no operativa. Valorado en `KJ-5` como **poco probable** para el mecanismo, con confianza **baja** | **Baja** | — | **NO TRATAR COMO CAPACIDAD ESTABLECIDA.** La respuesta proporcionada es `X-5.4`, cuyo valor **no depende** de que esto sea cierto |
| artefacto | **La política de objetivos del programa anima expresamente a atacar infraestructura crítica e instruye a los afiliados a solicitar un cifrador aparte para sistemas SCADA** | **ESTO SÍ ESTÁ DOCUMENTADO, y es de otra naturaleza: es un mecanismo del portal, no una declaración.** Una política existe para que los afiliados sepan qué pedir, y por tanto **corrobora que el producto se ofrece**. **No corrobora que haga lo que el actor dice.** La distinción es toda la diferencia entre un juicio sostenible y una alarma | **Media-alta** | — | **Contexto de apetito del adversario.** Base de `E-3` |
| artefacto | **Política de objetivos, resto**: permite atacar fuera de los países de la Comunidad de Estados Independientes y de **Serbia**; excluye **consulados y empresas vinculadas** a esos países; **levantó una restricción previa sobre Arabia Saudí**; y **prohíbe** atacar negocios de salud **relacionados con la infancia** y la filtración intencionada de datos de **menores de dieciocho años** | **Las dos prohibiciones son estrechas, concretas y publicitables; la autorización de infraestructura crítica es amplia y de consecuencias físicas.** Y **el caso chileno marca el límite exacto de la regla: la Clínica Dávila es un hospital, y la prohibición cubre la salud infantil, no la salud.** No es un código de conducta: es **gestión de reputación de marca entre afiliados** (`KJ-6`) | Media-alta | **Volátil**: una política de marca se cambia en un mensaje | **Contexto de victimología** |
| artefacto | **Trabajo previo con una operación de extorsión histórica** | **Reclamación del adversario** en la misma entrevista. No verificada | **Baja** | — | **Contexto.** No usar para vincular operaciones |
| artefacto | **Relatos publicados por el actor sobre cómo obtuvo el acceso y ejecutó sus ataques** | Un boletín de un centro nacional de ciberseguridad señala que el actor tiene presencia notoria en línea, publica en **inglés y a veces en ruso**, y «se jacta» de sus logros **hasta el punto de publicar relatos de cómo entró**. **Es inteligencia gratuita, específica y que nadie recoge por sistema** | Media-alta | — | **Requisito de colección** (`G-10`), y de los más rentables |
| artefacto | **Desenmascaramiento público de los operadores en junio de 2025** por un desconocido autodenominado `GangExposed`, con abandono de varios afiliados; y alegación del propio Devman de que ese desconocido intentó extorsionarle por entre 0,3 y 1 bitcóin | **Contexto de por qué la marca pudo apagarse sin intervención policial** (`E-4`, `KJ-7`). La primera parte está recogida por el analista; **la segunda es alegación del adversario**. **Este informe no reproduce ninguna identidad** | Media para el hecho; **baja para la alegación** | — | **Contexto.** No se reproducen identidades |

### A.6 — Estructura de la operación · **material de perfilado, no indicadores**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| artefacto | **«Redes» por país ofrecidas por los administradores**, con la pregunta al afiliado de si usará acceso propio o suministrado, y **ventanas de ejecución impuestas de dos a tres días** | **El hallazgo del informe.** El servicio «integraba la intermediación o distribución de accesos con el despliegue de *ransomware*». **Convierte la victimología regional en función del inventario de accesos del programa** y fija un tiempo de permanencia corto por diseño (`KJ-4`, `E-2`) | **Media-alta** *(vía indirecta)* | — | **Base de `X-5.1` y de `X-5.2`** |
| artefacto | **Cinco roles**: administrador y coordinador central; coordinador de accesos como punto de contacto alternativo para acceso a red; dos operadores superiores; y un afiliado acreditado por una instalación | Material de perfilado. **La existencia de un rol dedicado al acceso a red corrobora la integración de `KJ-4`** | Media-alta | — | **Contexto** |
| artefacto | **Gobernanza**: el afiliado entra al chat corporativo **tras producir su primera víctima**; se le asigna un **tutor experimentado**; **puede ser expulsado si pasa un mes sin una víctima nueva**; la formación de equipos y la revelación de la afiliación **requieren aprobación del tutor**; y la dirección **puede tomar el control de una negociación** si el afiliado se porta mal | **Describe una organización que gestiona productividad y protege su marca de sus propios empleados** (`E-1`). Y tiene consecuencia defensiva: **el programa impone un ritmo, y un afiliado con cuota es un afiliado que corre riesgos** | Media-alta | — | **Contexto de perfilado** |
| artefacto | **Reparto 80-20, con los fondos a dos monederos distintos**; **versión 3 del portal en enero de 2026** con expedientes estructurados, estados del ciclo de vida, equipos, control de invitaciones, compilación por víctima, seguimiento de plazos, campos de ingresos y acceso compartido | **La fecha de la versión 3 es el argumento más incómodo contra la hipótesis preferida de este informe**: nadie invierte en una plataforma un mes antes de abandonarla. Se deja a la vista en `H-B` de `O-6` | Media-alta | — | **Contexto** |
| artefacto | **Linaje**: afiliado de **Qilin, DragonForce, Apos y RansomHub** → programa propio con código **derivado de DragonForce** → valoración de que **ha vuelto a ser afiliado de otros** | **Describe cómo circula la capacidad en este ecosistema: con las personas.** Refuerza la decisión de detectar por mecanismo y no por marca (`E-4`, `O-2.2`) | Media-alta | — | **Contexto.** **Y consecuencia práctica: las detecciones de DragonForce probablemente sirven en buena medida** |
| artefacto | **Dire Wolf**: equipo nuclear reducido **sin programa amplio de afiliados**, y **sin solapamiento de infraestructura con Akira, Fog, Qilin ni SafePay** | **Dos negativos declarados, que valen más que una lista de alias**: alguien buscó la conexión y no la encontró. Y el primero tiene consecuencia analítica: **sin afiliados, su victimología refleja sus propias preferencias** y no un inventario de accesos ajeno (`KJ-8`) | Media-alta *(vía indirecta)* | — | **Contexto** |

### A.7 — Decisiones de higiene de este informe

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| cartera | **No se reproduce ningún dato personal de los pacientes expuestos en el caso chileno** | El adversario publicó parte de lo que dice ser más de 250 GB de **registros sensibles de pacientes**. **Son personas identificables que no han hecho nada, y un historial clínico es la categoría de dato personal cuya exposición menos se puede revertir.** Este informe cita **el volumen que el atacante reclama y la categoría de material**, porque es lo que un consumidor necesita para dimensionar el daño, **y nada más**. Misma regla que `CTI-2026-041` aplicó a los expedientes de personal, `CTI-2026-038` al archivo de una víctima en un directorio abierto y `CTI-2026-036` a las direcciones de terceros comprometidos | **Decisión propia** | — | **Se consigna para que la omisión figure con su razón** |
| cartera | **No se reproducen las identidades de los operadores desenmascarados en junio de 2025** | Fueron publicadas por un tercero desconocido cuya motivación incluye, según la alegación del propio adversario, un intento de extorsión. **Esta cartera no reproduce identidades personales obtenidas por esa vía**, con independencia de a quién pertenezcan: no aporta nada accionable y la procedencia no es verificable | **Decisión propia** | — | **Se consigna** |
| cartera | **Los indicadores de Dire Wolf no se transcriben** | Su análisis primario no fue accesible (`G-1`), y se aplica la regla de `CTI-2026-032`: **un carácter mal leído produce un indicador que no detecta nada, y eso es peor que su ausencia porque consume confianza.** Si `G-1` se cierra, este informe necesita una versión 1.1 | **Decisión propia** | — | **Se consigna** |

## Anexo B — Fuentes y valoración

> Valoración doble tipo Admiralty/OTAN, más el **grado de establecimiento** de `CTI-2026-039` y el grado **«declaración del adversario»** que `CTI-2026-041` añadió.

| Fuente | Disciplina | Fiab. | Cred. | Grado | Notas de sesgo |
|---|---|---|---|---|---|
| **`B-1` — Informe de PRODAFT sobre el portal de afiliados de Devman, rastreado como `Funky Mantis`** *(**no accesible**; usado a través de `B-2`)* | OSINT comercial · investigación sobre infraestructura del adversario | **B** | **3** *(por la vía)* | Proveedor | **La fuente del hallazgo central del informe**, y la que no pudimos leer. De ella salen los cinco roles, el modelo de gobernanza, la política de objetivos, las «redes» por país, las ventanas de dos a tres días, los parámetros del cifrador y la valoración —**declarada como de confianza moderada**— de que el operador sigue activo como afiliado de otros. **La credibilidad se degrada a 3 no por la fuente, que sería 2, sino porque no la leímos**: es `G-1` |
| **`B-2` — Cobertura especializada que recoge extensamente `B-1`**, con atribución nominal y cita directa — **leída en original** | OSINT · prensa especializada, **como vehículo de una fuente primaria** | **C** | **3** | Proveedor, por cita | **Su valor no está en su análisis sino en que transporta `B-1` con detalle y atribución.** Recoge además la observación de Vectra AI sobre el linaje del código, el boletín del centro nacional israelí sobre la conducta pública del actor, el episodio del desenmascaramiento, y **la entrevista en la que el actor hace la reclamación del cifrador para SCADA**. Sesgo del vehículo: medio especializado cuyo valor depende de la exclusividad, y la misma pieza incluye **una controversia sobre la conducta de un investigador** que este informe deja expresamente fuera de alcance |
| **`B-3` — Cobertura chilena del caso de la Clínica Dávila** — **leída en original** | OSINT · prensa regional, **como vehículo de dos declaraciones** | **C** | **3** | **Víctima y adversario** | Fuente del único caso regional nombrado. Transporta **la declaración de la institución** —«un incidente de un tercero», sin confirmar extorsión ni afectación de pacientes— y **las afirmaciones del atacante**: el volumen, la vía de entrada por red privada virtual con usuario y contraseña idénticos, y la publicación parcial al no cobrar. **La fiabilidad del vehículo importa para saber si transcribió bien; la credibilidad de cada declaración hay que valorarla por separado**, y por eso `A.3` y `A.5` llevan columna de quién lo dice |
| **`B-4` — Análisis de Trustwave SpiderLabs sobre Dire Wolf (2025-06-24) y el aviso del centro nacional de ciberseguridad de Singapur** *(**no accesibles**; usados a través de cobertura)* | OSINT comercial y GOVINT, por referencia | **B** | **3** *(por la vía)* | Proveedor y oficial, por referencia | Fuente de todo el material de Dire Wolf: Go, UPX, cifrador a medida por víctima, identificador de sala y credenciales en la nota, plazo de un mes, once países en 2025 y cien en treinta y dos países en 2026, equipo cerrado y ausencia de solapamiento con cuatro operaciones. **Es `G-1`, y por eso sus indicadores no se transcriben** |
| **`B-5` — Recuentos y análisis de panorama de terceros** (rastreadores de sitios de filtración, informes trimestrales) | OSINT · compilación | **C** | **4** | **Recuento de reclamaciones** | Fuente de todas las cifras de víctimas de este informe, **y conviene insistir en lo que son: reclamaciones en sitios de filtración, no brechas verificadas**. Una de estas fuentes lo advierte expresamente, y otra añade el dato que justifica el `Anexo D`: **casi todo el crecimiento de publicaciones del tercer trimestre de 2026 vino de grupos recién observados**, y esas listas mezclan ataques nuevos, cambios de marca, datos reciclados y reclamaciones sin respaldo |
| **`B-6` — Fichas de proveedor y foro de soporte sobre la familia Sauron** | OSINT · compilación de bajo nivel de detalle | **C** | **4** | Proveedor de bajo detalle | **Todo lo que hay sobre Sauron**, y es poco: primera observación, extensión, nota, contacto por correo, y el dato de que una herramienta pública **no pudo identificar la familia**. **La pobreza de esta fila es el hallazgo de `KJ-9`**, no sólo su limitación |

> **Una observación sobre la estructura de fuentes de este informe, y es la
> más desfavorable de este lote.** **Tres de las fuentes primarias no fueron
> accesibles**, y entre ellas está la que sostiene el hallazgo central. Todo
> lo que este informe afirma sobre el portal de afiliados —los roles, la
> gobernanza, las «redes» por país, los parámetros del cifrador— llega por
> **una sola vía**, y aunque esa vía cite con atribución nominal y detalle,
> **no es lo mismo que haber leído el original**.
>
> **Y la consecuencia práctica, que conviene asumir en lugar de disimular:**
> si `B-1` resultara mal transcrita en algún punto, los juicios `KJ-4` y
> `KJ-6` —que son los dos más originales del informe— se verían afectados.
> Es `G-1`, es la prioridad 1 de colección, y es **la misma tarea que `G-1`
> de `CTI-2026-039`**: resolver cómo esta célula lee las publicaciones de
> proveedor que no se sirven de forma legible. **Dos informes de seis en este
> lote tienen su brecha principal en el mismo problema, y eso ya no es una
> casualidad: es una carencia de capacidad.**

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

> **Y la aplicación que este informe necesita, sobre la reclamación de `KJ-5`:
> hay que desdoblar una afirmación en las dos que contiene.** «Existe un
> cifrador para SCADA» y «ese cifrador causa daño físico al hardware» son
> **dos juicios con dos probabilidades**, y el informe los lleva separados en
> `E-3`: *probable* que el programa **ofrezca** algo con ese nombre, porque
> su política documentada instruye a pedirlo; *poco probable* que **haga lo
> que el actor dice**, porque eso sólo lo afirma el actor.
>
> **La regla que se sigue, y es la generalización de la que `CTI-2026-041`
> estableció para la capacidad destructiva:** cuando una reclamación del
> adversario mezcla **existencia** y **efecto**, hay que separarlas, porque
> casi siempre la existencia está corroborada por un mecanismo —una política,
> un campo de un formulario, una opción de un constructor— y el efecto sólo
> por su palabra. **Colapsarlas produce la frase «este grupo puede quemar
> equipos industriales», que no es sostenible, a partir de dos afirmaciones
> de las cuales una sí lo es.**

## Anexo D — Cómo triar un grupo de extorsión recién nombrado

**El problema.** Aparece un nombre nuevo en un sitio de filtración, en un informe o en un requisito. Hay que decidir, antes de invertir en él, **qué clase de objeto es**: una marca con operación detrás, una herramienta en manos de cualquiera, un cambio de nombre de algo conocido, o una reclamación sin respaldo.

**Por qué hace falta ahora y no antes.** Según uno de los recuentos de este informe, **casi todo el crecimiento de publicaciones en sitios de filtración del tercer trimestre de 2026 vino de grupos recién observados**, y las listas **mezclan ataques nuevos, cambios de marca, datos reciclados y reclamaciones sin respaldo**. Otro recuento cifra en cuarenta y tres los grupos nuevos de un solo trimestre. **Sin un filtro, el panorama de amenazas se infla solo**, y cada nombre consume atención que no devuelve nada.

Y este expediente es la demostración: el requisito agrupó tres nombres como «emergentes» y **los tres están en niveles distintos de existencia**.

**Los siete criterios, en orden de poder discriminante.**

| # | Criterio | Qué indica | En este expediente |
|---|---|---|---|
| **1** | **¿Cómo contacta la víctima con el adversario?** | **El criterio más discriminante, y el más barato de comprobar.** Un **portal de negociación por víctima** exige infraestructura, mantenimiento y personal: es una **operación**. Una **dirección de correo electrónico** no exige nada: es una **herramienta**, y puede estar en manos de cualquiera | Portal: **Devman, Dire Wolf**. Correo: **Sauron** |
| **2** | **¿Hay sitio de filtración con víctimas nombradas y comprobables?** | Un sitio de filtración es una inversión en reputación de marca. Su ausencia, tras dos años, es informativa | Sí: **Devman (184), Dire Wolf (100)**. **No localizado: Sauron** |
| **3** | **¿Existe un análisis primario con muestra desmontada?** | Distingue un objeto que alguien ha estudiado de un nombre que alguien ha visto | Sí: **Devman, Dire Wolf**. **Ninguno: Sauron** |
| **4** | **¿Lo ha nombrado alguna autoridad nacional?** | Un aviso de un Estado implica víctimas que notificaron y un umbral de daño | **Dire Wolf** (alerta crítica de un centro nacional); **Devman** (boletín de otro); **Sauron**: ninguno |
| **5** | **¿Las herramientas públicas identifican la familia?** | Si no la identifican, o el objeto es muy nuevo, o es marginal, o es una variante de algo mal catalogado. **Y en cualquiera de los tres casos no hay descifrador** | Sí para los dos primeros; **No para Sauron** |
| **6** | **¿Hay linaje de código o de personal con algo conocido?** | Un linaje convierte un nombre nuevo en un capítulo de un expediente que ya existe — **y hace que las detecciones del predecesor sirvan** | **Devman**: derivado de DragonForce, y afiliado previo de cuatro programas. **Dire Wolf**: negativo declarado, sin solapamiento con cuatro operaciones. **Sauron**: desconocido |
| **7** | **¿Hay víctimas verificables por un tercero?** | Es el criterio que distingue una reclamación de un ataque. No hace falta que la víctima lo confirme: basta que exista evidencia que un tercero pueda comprobar | **Devman**: sí, con institución nombrada y comunicado. **Dire Wolf**: recuentos, sin caso nombrado en nuestras fuentes. **Sauron**: ninguna |

**La clasificación que resulta, y es lo que el método produce:**

| Clase | Qué significa | Qué merece |
|---|---|---|
| **Marca con operación** | Portal, sitio de filtración, análisis primario, y preferiblemente aviso de autoridad | **Expediente propio**, con detección, victimología y seguimiento |
| **Herramienta** | Cifrador identificable con contacto por correo, sin portal ni sitio de filtración | **Una ficha**: extensión, nota, y la instrucción de preservar muestras. **No un expediente** |
| **Capítulo de otro expediente** | Linaje claro de código o de personal con algo conocido | **Una sección en el expediente del predecesor**, no un documento nuevo |
| **Reclamación sin respaldo** | Nombre y lista de víctimas, sin muestras, sin análisis, sin víctima verificable | **Una línea en una lista de vigilancia**, y nada más |

**Aplicado a este expediente:** **Devman** es una marca con operación —y además un capítulo del expediente de DragonForce, lo que es información útil por sí misma—; **Dire Wolf** es una marca con operación; y **Sauron** es, con la evidencia disponible, **una herramienta**, lo que significa que merecía una ficha y no una tercera parte de este informe. **El requisito pedía tratar a los tres igual, y hacerlo habría sido el error.**

**Las tres reglas de uso del método.**

1. **La ausencia de evidencia no es evidencia de ausencia, pero la ausencia de *infraestructura* sí es informativa.** No tener análisis primario puede ser un hueco de colección. **No tener portal de negociación ni sitio de filtración, dos años después de la primera observación, es un hecho sobre el objeto**, porque esas cosas son visibles por diseño: existen para que las víctimas las encuentren.
2. **Un cambio de marca cuenta como el mismo objeto, y hay que buscarlo activamente.** `CTI-2026-040` y este informe documentan cuatro casos en los que la marca se apaga y la capacidad sigue. **Antes de abrir un expediente nuevo, el criterio 6 ahorra el expediente entero.**
3. **Y el criterio 1 se comprueba en minutos y resuelve la mayoría de los casos.** Mirar cómo se le pide a la víctima que contacte —portal propio o dirección de correo— es la comprobación de mejor relación coste-beneficio de toda esta disciplina, y casi nadie la hace primero.

**Lo que hay que declarar sobre este marco.** Tres cosas:

- **Clasifica el objeto, no mide la amenaza.** Una «herramienta» en manos de un operador competente puede hacer más daño a una organización concreta que una «marca con operación» que nunca la toque. **El método decide dónde invertir atención analítica, no quién es peligroso.**
- **Los criterios 3, 4 y 5 dependen de nuestra colección**, y por tanto el método puede clasificar como «herramienta» algo que es una marca cuyos análisis no hemos encontrado. Los criterios **1, 2, 6 y 7** son más robustos porque dependen del objeto y no de nosotros. **Si hay conflicto, pesan más esos cuatro.**
- **Y el método tiene un sesgo que conviene conocer: favorece lo visible.** Una operación deliberadamente discreta —sin sitio de filtración, que extorsiona en privado y cobra— sería clasificada como «herramienta» o como «reclamación sin respaldo», y sería un error. **La contramedida es el criterio 7**: una víctima verificable por un tercero pesa más que la ausencia de escaparate.

**Dónde más se aplica en esta cartera.** En los seis informes de extorsión, y especialmente al recibir un requisito que agrupa nombres. **Y hay un parentesco directo que conviene nombrar:** el criterio 1 de este método es, en el fondo, la misma observación que el `Anexo D` de `CTI-2026-041` —que **la necesidad de ser creído obliga al adversario a publicar cosas comprobables**— aplicada un paso antes: **un portal de negociación es la inversión mínima en credibilidad que una operación de extorsión tiene que hacer, y por eso su presencia o su ausencia dice qué clase de cosa se tiene delante.**

## Anexo E — Marcos de referencia empleados

- **ICD 203** (*Analytic Standards*), para el léxico de probabilidad y la separación de los ejes (Anexo C), **con la regla de desdoblar una reclamación que mezcla existencia y efecto** que ese anexo desarrolla.
- **Código Admiralty/OTAN**, doble valoración (Anexo B), **con la distinción entre la fiabilidad del vehículo y la credibilidad del contenido transportado**, que `CTI-2026-041` introdujo y que aquí se aplica a tres fuentes.
- **Grado de establecimiento** —oficial, proveedor, propio— de `CTI-2026-039`, **más el grado «declaración del adversario»** de `CTI-2026-041`.
- **MITRE ATT&CK v18** y **ATT&CK para sistemas de control industrial** (`T-2`), con la novedad —y la advertencia— de consignar dos técnicas del segundo marco **a partir de una reclamación del adversario y no de una observación**.
- **Pirámide del Dolor** (Bianco), en `T-3`, con la observación de que **un cifrador construido a medida por víctima hace estructuralmente inútil el nivel de los hashes**.
- **Análisis de Hipótesis Competidoras (ACH)** y **pre-mortem**, en `O-6`, con el argumento más incómodo contra la hipótesis preferida dejado a la vista (`H-B`).
- **Lectura de los relatos del adversario**, con el marco del `Anexo D` de `CTI-2026-041`, aplicado en `A.5` y en `E-3`.
- **Triaje de un grupo de extorsión recién nombrado**, propio de este informe (`Anexo D`), con sus siete criterios ordenados por poder discriminante y su clasificación en cuatro clases.

## Anexo F — Paquete legible por máquina

Las tablas `cti:ioc` de este anexo alimentan `ioc_index.csv`. **Cinco advertencias de ingesta, y la primera es sobre lo que este informe no aporta:**

1. **Este informe aporta muy pocos valores ingeribles, y por dos razones distintas.** Una es nuestra: tres fuentes primarias no accesibles (`G-1`), por lo que **los indicadores de Dire Wolf no se transcriben**. La otra es del objeto: **un cifrador construido a medida para cada víctima no tiene un hash que compartir**. Un consumidor que mida el valor por filas ingeribles concluirá que no aporta nada; **lo que aporta son el patrón de identidad de `A.1`, la firma de contenido de `A.2` y el método del `Anexo D`**.
2. **Las entradas de `A.5` llevan tipo `artefacto` y una columna explícita de quién lo dice.** La reclamación del **cifrador para SCADA** está marcada como reclamación del adversario, con confianza **baja**. **Extraerla sin esa marca convierte una afirmación de prestigio de un delincuente en una capacidad establecida**, y es el riesgo 1 del pre-mortem.
3. **`A.3` consigna una ausencia verificada** —ninguna actividad documentada en Colombia ni en Perú— con tipo `cartera`, para que figure con su razón. **Y con la causa estructural del «no»**: un sitio de filtración sólo publica a quien no paga.
4. **Las cifras de víctimas son recuentos de reclamaciones**, no de brechas verificadas, y una de las fuentes lo advierte expresamente.
5. **Y ningún dato personal de los pacientes expuestos ni ninguna identidad de operador se reproduce** (`A.7`).

Ninguna de las fuentes accesibles publica paquete STIX. **Si `G-1` se cierra**, este informe necesita una versión 1.1 con los indicadores de Dire Wolf y los parámetros del cifrador de Devman verificados contra el original, y sería una mejora sustancial.

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-11-19 | Emisión inicial. Incluye: la **conclusión previa de que los tres actores no son comparables** y de que la agrupación del requisito era el problema (`KJ-1`, `O-1`, `Anexo D`); la **corroboración con nombre de institución** del caso de la Clínica Dávila y la **ausencia verificada** de evidencia en Colombia y Perú (`KJ-2`, `KJ-3`); el hallazgo de que **el propio programa reparte el acceso por país** e impone ventanas de dos a tres días, lo que convierte la victimología regional en función del inventario de accesos del programa (`KJ-4`, `E-2`); el tratamiento de la **reclamación del cifrador para SCADA**, desdoblada en existencia y efecto, con la lectura de que **la política documentada corrobora que el producto se ofrece pero no que haga lo que el actor dice** (`KJ-5`, `E-3`); la lectura de la **política de objetivos** como gestión de reputación de marca, con el caso chileno marcando el límite exacto de su regla sobre la salud (`KJ-6`); el **cuarto caso del patrón** de `CTI-2026-040`, esta vez **sin intervención alguna** —la marca se apaga, la persona sigue— (`KJ-7`, `E-4`); la separación de **Dire Wolf** como el único activo y acelerando (`KJ-8`); el juicio de que **Sauron probablemente no es un grupo** (`KJ-9`, `O-1.3`); el **patrón regional de dos casos chilenos en cinco semanas, los dos por el acceso remoto** (`KJ-10`); y el método de triaje del `Anexo D` con sus siete criterios | Célula CTI |

> **Nota sobre dos peculiaridades de esta emisión.** La primera: es el único
> informe de este lote cuya **primera conclusión es que el requisito estaba
> mal planteado**, no que una de sus afirmaciones fuera falsa. La agrupación
> de tres objetos incomparables no es un error de dato: es un error de
> encuadre, y corregirlo era más útil que responder la pregunta tal como
> venía. La segunda: **la brecha principal de este informe es la misma que la
> de `CTI-2026-039`** —fuentes de proveedor que no se pueden leer—, y que dos
> de los seis informes del lote compartan su carencia principal **deja de ser
> una casualidad del expediente y pasa a ser una carencia de capacidad de
> esta célula**. Está en `G-1` de los dos.

## Anexo H — Realimentación del consumidor

Este informe reencuadra el requisito, sostiene un hallazgo sobre el reparto de accesos que descansa en una sola vía, y trata con cautela una reclamación de daño físico. Las tres cosas se pueden atacar.

1. **¿Pueden nuestras cuentas de servicio y de respaldo iniciar sesión interactiva por la red privada virtual?** Es `G-6`, se responde con una consulta a Identidad, es **la recomendación literal de la fuente primaria**, y responde al vector de los **dos casos chilenos de este lote**. Si la respuesta es que sí y no hay requisito documentado, **ése es el hallazgo del informe en esa organización**.
2. **¿Puede alguien leer los tres análisis primarios inaccesibles?** Es `G-1`, es la prioridad 1, **y es la misma tarea que `G-1` de `CTI-2026-039`**. Dos de los seis informes de este lote tienen su brecha principal en el mismo problema: cómo lee esta célula las publicaciones de proveedor que no se sirven de forma legible. **Resolverlo vale más que cualquiera de los dos informes.**
3. **¿Se extrajo la reclamación del cifrador para SCADA sin su marca?** Es el riesgo 1 del pre-mortem. «El programa ofrece algo que llama cifrador para SCADA» es *probable*; «este grupo puede quemar equipos industriales» **no es sostenible**, y la diferencia está en `E-3` y en `A.5`.
4. **¿Hay contraejemplos del método del `Anexo D`?** Lo más útil que alguien puede aportar es **una operación discreta y sin sitio de filtración que resultara ser grande**, porque ése es el sesgo declarado del método: favorece lo visible. El criterio 7 es la contramedida y no se ha probado.
5. **¿Se mantuvo la agrupación de los tres actores pese a `KJ-1`?** Si los tres han recibido atención comparable, el informe habrá fallado en su primera conclusión. **La atención correcta es desigual y explícita** (decisión 5 de `E-5`).
6. **¿Alguien lee los relatos que el actor publica sobre cómo entró en sus víctimas?** Es `G-10`. Un boletín oficial señala que los publica, y es inteligencia gratuita, específica y que nadie recoge por sistema. **Es la petición más barata de este informe.**
7. **¿Se ha comprobado la segmentación entre red de oficina y red de operación?** Es `H-9` y `X-5.4`, **y su valor no depende de que la reclamación de SCADA sea cierta**. Es la forma correcta de responder a una reclamación de confianza baja: con una medida que vale igual si es falsa.
8. **¿Está el programa de caza dimensionado para dos o tres días?** Es la decisión 2 de `E-5`. Una caza trimestral no detecta nada que entre y cifre en setenta y dos horas.
9. **Si somos prestador de salud: ¿hay un procedimiento para comunicar a los pacientes la exposición de su historial?** Es `O-4.3` y la decisión 7 de `E-5`, y está dirigida a Legal y a Comunicación, **no a Seguridad**. Esta célula puede decir cómo entró el adversario y qué lo habría impedido; **no puede decir qué se le debe a un paciente.**
10. **Y una pregunta sobre esta colección, que cierra el lote de noviembre de 2026:** de las seis afirmaciones regionales que los requisitos de este lote traían, **dos se dieron por improbables en las notas de cartera y las dos se corroboraron** —la de `CTI-2026-037` y la de `CTI-2026-041`—, y **una se corrobora aquí con nombre de institución**. Conviene preguntarse cuántas notas de cartera anticipan un veredicto y cuántas se han comprobado. **Una expectativa sobre el resultado de una búsqueda no es un sustituto de la búsqueda**, y este lote lo ha demostrado tres veces.

*Fin del informe `CTI-2026-042` v1.0.*
