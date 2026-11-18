---
tlp: "TLP:CLEAR"
pap: "PAP:AMBER"
id: "CTI-2026-032"
version: "1.0"
tipo: "Perfil de bloque de actores + separación de tres modelos operativos que comparten nombre + evaluación de exposición regional"
foco_regional: "Chile y región andina. **El único golpe confirmado a un banco del Cono Sur sigue siendo el Banco de Chile en mayo de 2018.** La afirmación de actividad en 2026 contra banca chilena, cooperativas reguladas por la SEPS en Ecuador y fintechs regionales **no está corroborada por ninguna fuente pública**, y este informe explica qué sí lo está"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "APT38 (G0082) · BlueNoroff · TraderTraitor · Sapphire Sleet · Contagious Interview / DeceptiveDevelopment · todos bajo el paraguas Lazarus Group (G0032) y el Buró General de Reconocimiento de la RPDC"
fecha: "2026-11-17"
caduca: "2027-02-17"
autor: "Célula CTI"
distribucion: "Elaborado íntegramente con fuentes abiertas TLP:CLEAR. Fuente principal: el informe de Arctic Wolf Labs del 12 de noviembre de 2026 y su documento completo, marcado «Classification: Public» por su autor, leídos en original. Difusión libre, conservando la atribución de las fuentes y las salvedades metodológicas de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-032

## El bloque financiero de Corea del Norte **no es un actor**, y defenderse de «Lazarus» es casi siempre defenderse de la cosa equivocada

### Tres modelos operativos incompatibles comparten paraguas: el que sacó diez millones de dólares del **Banco de Chile** en 2018 destruyendo nueve mil puestos de trabajo como señuelo, el que en 2026 industrializó la ingeniería social con vídeo sintético contra **677 directivos de 58 países**, y el que coloca trabajadores remotos dentro de la nómina. **Las tres defensas no se parecen en nada**

#### Y la afirmación de que en 2026 operan contra banca comercial chilena, cooperativas reguladas por la SEPS en Ecuador y fintechs andinas **no la sostiene ninguna fuente pública que hayamos podido localizar, en inglés ni en español**. Lo que sí está documentado es peor en un sentido y mejor en otro, y eso cambia qué hay que hacer

> **Regla de oro del producto:** todo párrafo debe responder a un requisito de
> inteligencia (PIR) y habilitar una decisión. Si un párrafo no cambia lo que
> alguien va a hacer, va al anexo o se borra.

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-032` |
| Versión / fecha | `1.0` — 2026-11-17 (emisión inicial) |
| Tipo de producto | Perfil de **bloque** de actores —no de un actor—, más **separación explícita de tres modelos operativos que la prensa y buena parte de la industria tratan como uno**, más evaluación de exposición regional, más corrección de una afirmación del requisito que originó el informe |
| Niveles cubiertos | Estratégico · Operacional · Táctico · Técnico |
| Foco regional | **Chile y región andina, con una conclusión incómoda:** el expediente regional confirmado es de 2018 y el expediente de 2026 no es regional. La exposición propia de 2026 **no está donde el requisito la situaba** |
| Marcado de difusión | `TLP:CLEAR` · `PAP:AMBER` |
| Clasificación interna | Sin clasificar. Todo el material proviene de publicaciones abiertas. La fuente principal está marcada «Classification: Public» por su propio autor |
| Requisitos atendidos | `PIR-01` (actores con intención y capacidad contra nuestro sector), `PIR-02` (amenazas al sistema financiero y de pagos), `PIR-05` (amenaza interna y cadena de contratación), `PIR-08` (ingeniería social asistida por generación sintética), `RFI-2026-11-A` |
| Solicitante / consumidor primario | Dirección, Riesgo Operacional y Jefatura de SOC. **Dos de las decisiones de `E-4` son de Recursos Humanos**, y ésa es una de las conclusiones del informe |
| Ventana de observación | 2014-01-01 → 2026-11-17. **Ventanas densas:** mayo-junio de 2018 (expediente regional) y abril-noviembre de 2026 (campaña vigente) |
| Base de colección | Nueve fuentes externas; dos primarias leídas en original, una de ellas el documento técnico completo en PDF. **Sin telemetría propia** |
| Autor (analista) | Célula CTI |
| Revisión por pares | Pendiente |
| Aprobación | Pendiente |
| Caducidad / revisión | 2027-02-17 (92 días). Revisión anticipada si se cumple cualquier disparador de `O-7`, y en particular el `I-1`: la publicación de **cualquier** intrusión confirmada en una entidad financiera de Chile, Perú, Colombia o Ecuador |
| Productos relacionados | `CTI-2026-031` (Dark Caracal: misma fuente primaria, mecanismo de C2 distinto) · `CTI-2026-021` (troyanos bancarios brasileños: la amenaza que **sí** golpea banca de la región a diario, y con la que conviene no competir por recursos) · `CTI-2026-019` (ARTEX) · `CTI-2026-029` (Sandworm: el otro actor de esta cartera que usa destrucción como instrumento, con finalidad distinta) |
| Paquete legible por máquina | **Importante:** las tablas `cti:ioc` del Anexo A de este informe son deliberadamente cortas. La fuente primaria publica su lista completa de indicadores y sus reglas YARA en un anexo que **no es extraíble como texto** (va en imágenes). La fuente preferente para ingesta es ese documento, no este anexo. Véase el Anexo B.1 |

> ⚠ **Limitación estructural, doble.** Primero, la habitual: **sin telemetría
> propia**, de modo que `O-4` es un cuestionario. Segundo, y específica de este
> informe: **el anexo de indicadores de la fuente primaria no se puede
> transcribir** porque su autor lo maquetó como imagen. Se declara abiertamente
> porque cambia cómo hay que usar este documento: el Anexo A de aquí **no
> sustituye** al de la fuente, y un retrohunt contra lo que hay aquí no es un
> retrohunt contra la campaña.

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** «Lazarus» no es un actor operativo: es un paraguas que agrupa al menos tres modelos de negocio distintos, y **tratarlos como uno produce decisiones de defensa equivocadas**. El modelo de APT38 —intrusión larga en una entidad financiera, manipulación de la mensajería de pagos y destrucción masiva como señuelo de salida— y el modelo de BlueNoroff en 2026 —ingeniería social dirigida a personas concretas con autoridad sobre activos digitales— no comparten vector, ni objetivo, ni indicadores, ni contramedida. Valoramos **casi con certeza** *(≥99 %)* que un programa de defensa construido sobre los indicadores de uno sea ineficaz contra el otro. **Confianza: alta.** *Base:* los expedientes públicos de ambos modelos, leídos en paralelo, no comparten un solo elemento técnico común.

**KJ-2.** El modelo vigente de BlueNoroff está industrializado y **su mecanismo de compromiso no ha cambiado**. En noviembre de 2026 la fuente primaria documenta 677 personas identificadas en la biblioteca de material del actor, repartidas en 58 países, de las cuales **el 84 % son fundadores y altos directivos**; 98 dominios de alta confianza, 73 de ellos no reportados antes; y una cadena de producción de vídeo sintético que combina varios servicios comerciales de generación. Pero el paso del que todo depende sigue siendo el mismo: **una página de aspecto confiable pide a la persona que ejecute algo en su equipo**. Valoramos **muy probable** *(80–95 %)* que ese paso siga siendo el invariante durante los próximos doce meses. **Confianza: alta.** *Base:* la propia fuente lo afirma tras seis meses de seguimiento con acceso a la infraestructura del actor, y es su hallazgo central: cambió casi todas las señales visibles y casi nada del mecanismo.

**KJ-3.** **No hemos localizado ninguna fuente pública que documente actividad de este bloque en 2026 contra banca comercial chilena, cooperativas reguladas por la SEPS en Ecuador o fintechs andinas.** La búsqueda se hizo en inglés y en español, incluyendo terminología de los supervisores locales. Valoramos **poco probable** *(20–45 %)* que exista un incidente de esa clase, confirmado y no publicado, en los últimos doce meses. **Confianza: moderada.** *Base:* ausencia de evidencia en una colección deliberadamente dirigida a encontrarla, que es más que ausencia de búsqueda pero menos que evidencia de ausencia. Es `G-1`, y es el motivo de que `I-1` sea el disparador de revisión más importante del informe.

**KJ-4.** El precedente regional confirmado es uno y es de 2018: **el Banco de Chile**. A finales de mayo de 2018 se destruyeron del orden de 9.000 puestos de trabajo y 500 servidores, y **cuatro transacciones SWIFT fraudulentas** salieron antes de que se detectara el robo, por unos 10 millones de dólares transferidos a una cuenta en Hong Kong. Valoramos **casi con certeza** *(≥99 %)* que los hechos sean esos. **Confianza: alta** para los hechos. Para la atribución, en cambio, **confianza moderada**: la vinculación a APT38 es la valoración de FireEye, otras fuentes la sostienen con menos convicción, y el borrador usado compartía guion de instalador NSIS con código de Buhtrap **filtrado públicamente en febrero de 2018**, lo que debilita precisamente el tipo de evidencia —identidad de código— en que se apoya.

**KJ-5.** La parte del modelo de 2018 para la que nadie está preparado no es el robo: **es la destrucción usada para ocultarlo**. Un plan de respuesta a incidentes típico contempla el fraude o contempla el cifrado destructivo, y los trata como escenarios alternativos. Aquí la destrucción masiva **es la cobertura de la salida del dinero**, con el efecto operativo de que la organización dedica sus primeras cuarenta y ocho horas a restaurar puestos de trabajo mientras la transferencia se consuma y se hace irreversible. Valoramos **probable** *(55–80 %)* que la mayoría de las entidades financieras de la región no tenga en su plan el escenario «destrucción simultánea a fraude de pagos» como un único evento. **Confianza: moderada.** *Base:* inferencia a partir de la estructura habitual de los planes, no de una muestra propia.

**KJ-6.** El dinero del programa ya no está en la mensajería bancaria: **está en los criptoactivos**, y eso desplaza nuestra exposición de la sala de pagos a las personas. TRM Labs estimó unos 577 millones de dólares robados por actores vinculados a la RPDC hasta abril de 2026; Chainalysis calculó al menos 2.020 millones en 2025. En abril de 2026 se atribuyó preliminarmente a la unidad TraderTraitor el vaciado de unos 292 millones de dólares en `rsETH` del puente de KelpDAO —unos 116.500 `rsETH`—, con unos 71 millones congelados después. Valoramos **muy probable** *(80–95 %)* que el eje principal de generación de ingresos del bloque siga siendo el ecosistema de activos digitales en los próximos doce meses. **Confianza: alta** para la tendencia, **baja** para cualquier cifra concreta: proceden de estimaciones de analítica de cadena que no son auditables desde fuera y que difieren entre proveedores.

**KJ-7.** Hay un tercer modelo que no es intrusión y que la mayoría de los programas de seguridad no cubre porque **no es competencia del SOC: la colocación de trabajadores remotos dentro de la nómina**. El 1 de octubre de 2026 un jurado federal en Ohio acusó a catorce personas por un esquema plurianual de empleo remoto en beneficio de la RPDC que afectó a más de setenta empresas y generó alrededor de tres millones de dólares; entre el 21 y el 25 de septiembre de 2026 se desarticularon más de cuarenta «granjas de portátiles» en Texas. Valoramos **muy probable** *(80–95 %)* que este modelo sea aplicable a cualquier organización de la región que contrate desarrollo remoto. **Confianza: alta.** *Base:* acusación formal de una fiscalía federal, corroborada por varios medios con las mismas cifras; se trata de imputaciones, no de condenas.

**Qué cambiaría estos juicios.** **(a)** Cualquier intrusión confirmada y publicada en una entidad financiera de Chile, Perú, Colombia o Ecuador atribuida a este bloque convertiría `KJ-3` en obsoleto y obligaría a reemitir el informe en 48 horas. **(b)** Una muestra de BlueNoroff que logre ejecución **sin** intervención manual del usuario —un día cero de navegador, por ejemplo— rompería `KJ-2` y, con él, la detección `D-1`, que es la de mayor valor del informe. **(c)** Un golpe nuevo de tipo 2018 contra mensajería de pagos en cualquier país revalidaría el modelo de APT38 como vigente y cambiaría la prioridad de `E-4`. **(d)** La identificación de facilitadores de granjas de portátiles en Latinoamérica, hoy no documentada, ampliaría `KJ-7` del plano de la contratación al de la infraestructura regional.

---

## 2. Resumen ejecutivo

Hay una cosa que conviene entender antes de cualquier dato, porque de ella depende que el resto sirva: **«Lazarus» es una etiqueta de origen, no una descripción de comportamiento**. Designa la actividad cibernética ofensiva de un Estado, atribuida públicamente al Buró General de Reconocimiento de la RPDC, dentro de la cual conviven equipos con misiones, métodos y víctimas que no tienen nada en común. Confundirlos tiene una consecuencia práctica inmediata: un banco que lea un informe sobre la campaña de 2026 e ingiera sus indicadores habrá cargado en sus controles la infraestructura de una operación de ingeniería social contra directivos de empresas de criptoactivos, que no tocará nunca su sala de pagos.

**Este informe separa tres modelos y dice qué defensa corresponde a cada uno.**

**El primero es el de APT38**, y es el que tiene precedente en Chile. En mayo de 2018 el Banco de Chile sufrió la destrucción de unos nueve mil puestos de trabajo y quinientos servidores. Durante el caos, cuatro transferencias SWIFT fraudulentas salieron hacia una cuenta en Hong Kong por unos diez millones de dólares. La destrucción no era el ataque: era el señuelo. Esa es la innovación operativa que importa, porque invierte la lógica de la respuesta: la organización gasta sus primeras horas —las únicas en que una transferencia internacional puede retrocederse— restaurando ordenadores.

**El segundo es el de BlueNoroff y TraderTraitor**, y es el vigente. No ataca instituciones: ataca personas con autoridad sobre dinero. La fuente principal de este informe lleva seis meses con acceso a la biblioteca de material del propio actor, y lo que documenta es una fábrica: 677 personas preparadas como objetivo en 58 países, el 84 % de ellas fundadores o altos directivos; material de señuelo capturado no sólo de fotografías de perfil, sino de **entrevistas en YouTube y charlas de congresos grabadas en pantalla**, lo que permite reproducir la cara y la voz de alguien sin necesidad de comprometerlo; y vídeo sintético que ya no se distingue de una grabación real por inspección visual, de modo que los analistas tuvieron que determinar qué era falso **por evidencia de procedencia, no por aspecto**.

Y, con todo eso, el hallazgo central de esa fuente es casi un alivio: **el actor cambió en seis meses casi todas las señales que una víctima puede ver, y casi nada de cómo funciona la intrusión**. Sigue habiendo un momento en que una página de aspecto impecable pide a la persona que ejecute algo en su equipo. Ese momento es el punto de corte, y no caduca.

**El tercero no es una intrusión y por eso suele quedar sin dueño: es la contratación.** Trabajadores remotos de la RPDC, con identidades ajenas y facilitadores locales que mantienen encendidos los portátiles corporativos en sus casas para que el acceso parezca doméstico. En octubre de 2026 una fiscalía federal estadounidense acusó a catorce personas por un esquema que afectó a más de setenta empresas. Para una organización que contrata desarrollo remoto en la región, esto no es un problema de SOC: es un problema de Recursos Humanos con consecuencias de seguridad.

**Y lo que no hemos encontrado, que es la mitad del valor de este informe.** El requisito que lo originó afirmaba que en 2026 este bloque mantiene operaciones activas contra banca comercial chilena, cooperativas financieras reguladas por la SEPS en Ecuador y fintechs y casas de cambio regionales. **Hemos buscado eso expresamente, en inglés y en español, y no lo hemos encontrado en ninguna fuente pública.** Lo que la colección devuelve sobre la región es: un precedente de 2018 en Chile, una mención histórica de Perú entre los países más atacados en un perfil de proveedor de hace casi cuatro años, y nada de 2026. Decirlo importa porque la alternativa —escribir el informe como si la afirmación fuera cierta— habría orientado un presupuesto hacia la defensa de un escenario sin evidencia, en un año en que la amenaza que sí vacía cuentas en la región todos los días es otra y está en `CTI-2026-021`.

<!-- cti:cards -->

| Rasgo | Qué significa | Etiqueta |
|---|---|---|
| Tres modelos operativos bajo un nombre | **El error más caro de este expediente no es técnico, es de clasificación.** Los indicadores de uno no sirven contra otro, y el presupuesto se asigna por nombre de actor, no por modelo | `01 · taxonomía` |
| Destrucción como señuelo de un fraude de pagos | Invierte la respuesta a incidentes: las horas en que la transferencia es reversible se gastan restaurando puestos. **El plan tiene que contemplarlo como un solo evento** | `02 · el modelo de 2018` |
| El objetivo es la persona, no la institución | 84 % de los objetivos identificados son fundadores y altos directivos. Los controles perimetrales no aplican a quien tiene autoridad para saltárselos | `03 · el modelo de 2026` |
| Vídeo sintético indistinguible por inspección visual | La formación de «fíjese en las manos y en el parpadeo» **ha caducado**. La verificación tiene que ser de canal, no de apariencia | `04 · generación sintética` |
| El mecanismo de compromiso es estable y manual | **La buena noticia del informe.** Hay un paso que no ha cambiado en seis meses de evolución, y es detectable por comportamiento | `05 · el punto de corte` |
| La nómina como vector | No hay intrusión que detectar: hay un contrato laboral. Compete a RR. HH. y a Compras antes que al SOC | `06 · contratación` |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `677` | Personas identificadas como objetivo preparado en la biblioteca del actor, noviembre de 2026 | Frente a unas 400 en abril, de las que la fuente verificó 100 de forma independiente. **No son compromisos confirmados: es material preparado** |
| `58` | Países en los que están esas personas | Frente a 20 en abril. La ampliación geográfica es el cambio de escala más claro |
| `84 %` | Proporción de fundadores y altos directivos entre los objetivos identificados | El criterio de selección es la **autoridad sobre fondos y claves de firma**, no el sector ni el país |
| `98` | Dominios de alta confianza documentados en noviembre de 2026 | **73 de ellos no se habían reportado antes.** La infraestructura se renueva más rápido que su publicación |
| `349` | Vídeos de la biblioteca del actor analizados como «probablemente modificados» | A 6 de noviembre de 2026. Determinación por **procedencia**, no por apariencia |
| `4` | Transferencias SWIFT fraudulentas que salieron del Banco de Chile en 2018 | Antes de que se detectara el robo. Unos **10 millones de dólares** a Hong Kong |
| `≈9.000` | Puestos de trabajo destruidos en ese incidente | Más unos 500 servidores. **No era el ataque: era la cobertura** |
| `14` | Personas acusadas en Ohio el 1 de octubre de 2026 por el esquema de empleo remoto | Más de 70 empresas afectadas, unos 3 millones de dólares. Imputaciones, no condenas |
| `0` | Intrusiones de este bloque confirmadas públicamente en 2026 en entidades financieras de Chile, Perú, Colombia o Ecuador | **Es el dato que el requisito daba por distinto** |

> ✅ **Decisiones que se solicitan, con plazo.**
> **(a) Inmediato, y es de higiene analítica:** prohibir el uso de «Lazarus» como designación operativa en documentos internos. Cada medida se asocia a **un modelo**, no al paraguas (`E-a`).
> **(b) 14 días:** desplegar `D-1`, la detección del paso invariante —ejecución manual inducida desde el navegador—. Es la de mayor valor y no depende de ningún indicador perecedero (`E-b`).
> **(c) 30 días:** revisar el plan de respuesta de la entidad para el escenario **único** «destrucción masiva simultánea a fraude de pagos», con el requisito explícito de que el equipo de pagos no quede subordinado al de restauración (`E-c`).
> **(d) 30 días, y es de RR. HH.:** controles de verificación de identidad en contratación remota de perfiles técnicos, y revisión del parque de portátiles entregados a personal remoto (`E-d`).
> **(e) 45 días:** formación específica de nivel directivo sobre inducción a ejecutar, **retirando** de la formación existente el material que enseña a identificar vídeo falso por su aspecto (`E-e`).
> **(f) 60 días:** decidir si procede **no** ingerir los indicadores de la campaña Web3 en los controles de la red de pagos, y documentar la decisión (`E-f`).

---

## 3. Alcance, requisitos y limitaciones

**3.1 Requisitos de inteligencia atendidos**

| Req. | Enunciado | ¿Respondido? | Dónde |
|---|---|---|---|
| PIR-01 | ¿Qué actores tienen intención y capacidad contra nuestro sector y geografía? | Sí, **y la respuesta regional es la contraria a la esperada** | `KJ-3`, `E-2`, `O-5` |
| PIR-02 | ¿Qué amenazas pesan sobre el sistema de pagos y la mensajería financiera? | Sí, con un precedente nacional y una evaluación de vigencia del modelo | `KJ-4`, `KJ-5`, `E-1`, `T-1.A` |
| PIR-05 | ¿Qué amenaza representa la cadena de contratación? | Sí, y es el apartado que no es del SOC | `KJ-7`, `O-3.C`, `E-d` |
| PIR-08 | ¿Cómo cambia la ingeniería social con generación sintética de audio y vídeo? | Sí, con una consecuencia directa sobre la formación vigente | `E-1`, `T-1.B`, `E-e` |
| RFI-2026-11-A | El requisito afirmaba actividad en 2026 contra banca chilena, cooperativas de la SEPS y fintechs regionales. ¿Se sostiene? | **No se ha podido corroborar.** Véase `3.5` | `KJ-3`, `3.5`, `G-1` |
| PIR-04 | ¿Nos afecta? | **No.** Requiere telemetría propia | `O-4`, sin evaluar |

**3.2 Fuera de alcance.** No se evalúan: la actividad de espionaje político y militar del mismo origen estatal —Kimsuky, Andariel y los conglomerados de ciberespionaje de la RPDC—, salvo lo necesario para delimitar el paraguas; el programa de armas al que se destinan los fondos, que es materia de otros productos; las operaciones contra defensa y aeroespacial; la atribución al Estado en su última milla, que está establecida por acusaciones federales y por designaciones y este informe no necesita reabrir; y el análisis de la cadena de blanqueo de criptoactivos, que exige analítica de cadena que no tenemos.

**3.3 Limitaciones de la colección.** Seis, y la segunda y la cuarta condicionan el uso del documento.

1. **Sin telemetría propia.** `O-4` es un cuestionario.
2. **El anexo de indicadores de la fuente primaria no es extraíble.** Su autor lo maquetó como imagen dentro del PDF. Se intentó la extracción y no fue posible; véase el Anexo B.1. Consecuencia: el Anexo A de este informe **no contiene los 98 dominios** y no sustituye a la fuente.
3. **Las cifras de robo de criptoactivos no son auditables.** Proceden de estimaciones de analítica de cadena de proveedores comerciales, que difieren entre sí. Se usan como **orden de magnitud y tendencia**, nunca como dato.
4. **Las cifras de objetivos no son cifras de víctimas.** La propia fuente lo advierte de forma expresa: los 677 describen **a quién preparó material el actor**, no compromisos confirmados. Este informe lo repite cada vez que usa el número.
5. **La atribución del incidente de 2018 es de un proveedor** y tiene un debilitamiento conocido: el código del borrador compartía elementos con material filtrado públicamente meses antes.
6. **El informe de abril de 2026 de la fuente primaria no se pudo leer en original** —su dirección devolvió un error—, de modo que su contenido se cita a través del informe de noviembre, que lo resume.

**3.4 Metodología.** ICD 203, con probabilidad y confianza separadas. Código Admiralty doble (Anexo B). MITRE ATT&CK v18. Pirámide del Dolor. ACH, supuestos clave y pre-mortem en `O-6`. **Y una técnica estructurada que estructura el informe entero: la descomposición de un alias agregado en modelos operativos**, con la regla de que ninguna medida se recomienda contra «el actor» sino contra un modelo. El Anexo D la generaliza.

**3.5 Lo que el requisito afirmaba, y lo que las fuentes sostienen**

<!-- cti:table highlight="NO corroborado|Parcial" -->

| # | Afirmación del requisito | Veredicto | Qué dicen las fuentes |
|---|---|---|---|
| 1 | «Aunque es un actor global, sigue siendo una brecha crítica en tu catálogo para Chile, Ecuador y Colombia» | **Corroborado como brecha de catálogo** | Es cierto que faltaba. Este informe la cierra. Que fuera una brecha del catálogo no implica que haya actividad regional: son dos cosas distintas y el requisito las une |
| 2 | «En 2026 mantiene operaciones activas contra la banca comercial» en esos países | **NO corroborado** | Ninguna fuente pública localizada documenta un incidente de 2026 en banca comercial de Chile, Ecuador, Colombia o Perú atribuido a este bloque. El precedente bancario regional es de **mayo de 2018** |
| 3 | «Cooperativas financieras, como las reguladas por la SEPS en Ecuador» | **NO corroborado** | Búsqueda específica en español incluyendo la terminología del supervisor: **sin resultados**. No hay fuente pública que vincule a este bloque con cooperativas ecuatorianas. La afirmación es concreta y verificable, y no se verifica |
| 4 | «Fintechs y exchanges cripto regionales» | **NO corroborado para la región; corroborado para la clase de víctima** | Que el bloque ataca plataformas de criptoactivos y a sus directivos está sobradamente documentado en 2026, con objetivos en 58 países. **Que haya víctimas regionales, no.** La distinción no es retórica: cambia si el control va en el perímetro de una entidad andina o en la formación de sus directivos |
| 5 | «Combinando ataques a infraestructura financiera/SWIFT con campañas de ingeniería social en LinkedIn (perfiles profesionales falsos y pruebas técnicas maliciosas para desarrolladores)» | **Corroborado, pero son modelos distintos y no se combinan** | Los dos fenómenos existen. **Pero no son el mismo equipo ni la misma operación**, y presentarlos como una combinación es exactamente el error que `KJ-1` describe. La prueba técnica maliciosa para desarrolladores es el modelo de *Contagious Interview*; SWIFT es el de APT38. Un banco que se prepare para «la combinación» se preparará para algo que no existe |

> ⚠ **Por qué esta tabla no es un reproche.** El requisito describía bien el
> fenómeno global y mal su localización, y ésa es la confusión más frecuente
> con los actores de este origen: son **globales de verdad**, de modo que
> cualquier afirmación sobre ellos suena plausible en cualquier país. La
> pregunta útil no es «¿operan contra la banca?» —sí, y han operado en Chile—
> sino **«¿hay evidencia de que hayan operado aquí este año, y con qué
> modelo?»**. La respuesta es no, y eso no reduce la exposición: la traslada,
> de la sala de pagos a tres directivos con cartera de criptoactivos y a un
> proceso de contratación de desarrolladores remotos.

---

# NIVEL ESTRATÉGICO
### Para: Consejo · CISO · Riesgo · Legal · RR. HH. · Horizonte: 6–24 meses

## E-1. Qué representa este bloque, y por qué su nombre es parte del problema

Un Estado que no puede financiarse por los canales normales de la economía internacional ha convertido su aparato de inteligencia en un centro de beneficio. Eso no es una metáfora: es la descripción funcional de lo que distingue a este bloque de cualquier otro actor estatal de esta cartera. Gamaredon roba documentos; Salt Typhoon se instala en los routers de los operadores; Sandworm destruye. **Éste ingresa.** Y una organización que ingresa tiene propiedades que una que espía no tiene: escala con el beneficio, reinvierte en capacidad, diversifica cuando un mercado se cierra, y mide el éxito en una unidad que se puede contar.

De ahí la estructura en modelos. Un centro de beneficio con varias líneas de negocio **no tiene un modo de operar, tiene una cartera**, y las líneas se abren y se cierran según el rendimiento. Eso explica la secuencia histórica mejor que cualquier teoría sobre capacidades técnicas: la mensajería bancaria daba decenas de millones por operación pero exigía meses de intrusión y dejaba un rastro interbancario trazable; los criptoactivos dan cientos de millones, se mueven sin corresponsales y el blanqueo es un problema propio y no del banco de nadie; y la colocación de trabajadores remotos da poco por unidad pero es casi indetectable y escala con la economía del teletrabajo.

<!-- cti:cards -->

| Cambio estructural | Por qué nos afecta | Etiqueta |
|---|---|---|
| El beneficio como criterio de selección de línea de negocio | **La predicción no se hace sobre capacidades, se hace sobre rendimientos.** Si el ecosistema de criptoactivos endurece la custodia, el bloque vuelve a la banca o a otro sitio. No hay fidelidad a un método | `01 · economía` |
| El objetivo es quien tiene autoridad, no quien tiene acceso | 84 % de los objetivos identificados son fundadores y altos directivos. **Los controles que un directivo puede saltarse no son controles para él** | `02 · selección` |
| La verificación por apariencia ha caducado | Los analistas de la fuente primaria tuvieron que clasificar los vídeos por procedencia, no por aspecto, porque ya no se distinguen visualmente. **Toda la formación que enseña a detectar lo falso mirando está obsoleta** | `03 · formación` |
| El material de señuelo ya no exige comprometer a nadie | Se captura de entrevistas públicas y charlas de congresos grabadas en pantalla. **La exposición pública de un directivo es ahora materia prima del ataque al siguiente** | `04 · reconocimiento` |
| La generación sintética es multiplicador, no cambio de mecanismo | La propia fuente lo dice: la campaña sigue dependiendo de investigación del objetivo, infraestructura a medida y **ejecución manual del usuario**. La IA amplía el volumen; no elimina el punto de corte | `05 · calibración` |
| El vector puede ser un contrato de trabajo | No hay intrusión. **Hay una nómina**, y la detección corresponde a quien valida identidades, no a quien vigila la red | `06 · nómina` |

**Y una nota sobre el nombre, que es la recomendación `E-a`.** Mientras el término «Lazarus» se use como designación operativa en documentos internos, las medidas se asignarán al nombre y no al modelo, y el resultado observable es predecible: listas de bloqueo con infraestructura de campañas que no nos tocan, formación genérica sobre «hackers norcoreanos», y ningún control nuevo en la sala de pagos ni en el proceso de contratación. **El coste de la precisión taxonómica aquí es cero y el beneficio es que cada medida tiene dueño.**

## E-2. Victimología, con la gradación intacta

Hay que presentar dos conjuntos de datos que no se pueden sumar, y la tentación de sumarlos es exactamente lo que `KJ-1` advierte.

<!-- cti:bars title="Objetivos identificados en la biblioteca del actor, por perfil (noviembre de 2026) — material PREPARADO, no compromisos confirmados" -->

| Perfil | Proporción (%) |
|---|---|
| Fundadores y alta dirección | `84` |
| Resto de perfiles | `16` |

<!-- cti:bars title="Evolución del alcance de la campaña BlueNoroff entre abril y noviembre de 2026" -->

| Medida | Valor |
|---|---|
| Objetivos identificados (nov.) | `677` |
| Objetivos identificados (abr.) | `400` |
| Países (nov.) | `58` |
| Países (abr.) | `20` |
| Dominios de alta confianza (nov.) | `98` |
| De ellos, no reportados antes | `73` |

> ⚠ **Lo que estas barras no dicen, y hay que decirlo cada vez.** La fuente es
> explícita: **estas cuentas describen contra quién preparó material el actor,
> no compromisos confirmados**. Son una medida de *intención dirigida*, que es
> informativa y poco habitual —procede de acceso a la infraestructura del
> propio actor, no de víctimas que denunciaron—, pero no es una medida de
> impacto. Un informe que cite «677 víctimas» habrá convertido una buena fuente
> en un dato falso.

**Sobre la región, el conjunto es casi vacío y eso es el hallazgo.** El expediente regional confirmado de este bloque, en todos sus modelos, cabe en tres líneas: el Banco de Chile en mayo de 2018; una mención de Perú entre los países más atacados por el modelo financiero en un perfil de proveedor de hace casi cuatro años, que se cita aquí con esa antigüedad declarada y sin usarla para priorizar nada; y la ausencia completa de evidencia pública de 2026. Lo que de verdad desplaza la exposición regional no es un país: **es un perfil de persona** —quien controle criptoactivos, claves de firma o relaciones de confianza con inversores— y ese perfil existe en Santiago, en Bogotá y en Lima igual que en Singapur.

## E-3. Tendencia y pronóstico

<!-- cti:chart title="Ampliación del alcance geográfico de la campaña vigente, en países con objetivos identificados" cap="Dos puntos de medición de la misma fuente, abril y noviembre de 2026. Dos puntos no son una serie: se presentan como lo que son, un salto medido, no una curva." -->

| Periodo | Países |
|---|---|
| `Abr·26` | `20` |
| `Nov·26` | `58` |
| `¿Feb·27?` | `0` |

> **Sobre el tercer punto del gráfico.** Está a cero a propósito. No hay dato y
> no se va a extrapolar uno: dos mediciones separadas por siete meses no
> autorizan una proyección, y el repositorio prefiere un hueco visible a una
> línea inventada. Lo que sí se puede decir en prosa es el sentido del cambio,
> y está en los escenarios de abajo.

<!-- cti:cards -->

| Escenario | Desarrollo | Etiqueta |
|---|---|---|
| **Más probable** | El modelo de 2026 continúa y se amplía: más temas de señuelo alineados con los flujos de trabajo reales de la inversión y la gestión de activos digitales, más países, más calidad de vídeo sintético, **y el mismo paso final de ejecución manual**. La defensa que funciona en febrero de 2027 es la misma que funciona hoy | `Probable · 55–80 %` |
| **Alternativa creíble** | Aparece una variante que elimina el paso manual —explotación de navegador, o abuso de una funcionalidad legítima que ejecute sin confirmación—. Sería el cambio más grave posible para nuestra posición defensiva, porque invalida `D-1` | `Poco probable · 20–45 %` |
| **La que hay que vigilar en la región** | El endurecimiento de la custodia institucional de criptoactivos en los mercados centrales desplaza el esfuerzo hacia mercados con supervisión más joven. **Ése es el escenario en que Latinoamérica pasa de periferia a objetivo**, y su indicador de alerta temprana es regulatorio antes que técnico | `Posibilidad real · 45–55 %` |
| **Retorno del modelo de 2018** | Un golpe nuevo contra mensajería de pagos, con destrucción como señuelo. El modelo no está desmantelado: está desplazado por rendimiento. Si los criptoactivos se encarecen como objetivo, vuelve | `Poco probable · 20–45 %` |
| **Descartado, y se consigna** | Que la generación sintética haya cambiado el mecanismo de intrusión. La fuente primaria lo falsa explícitamente: la IA es multiplicador de producción y la campaña sigue dependiendo de ejecución manual del objetivo | `Descartada` |

## E-4. Decisiones que este informe pide al nivel estratégico

<!-- cti:table highlight="RR. HH.|Legal|Inmediato" -->

| # | Decisión | Fundamento | Plazo |
|---|---|---|---|
| E-a | **Prohibir «Lazarus» como designación operativa** en documentos internos de riesgo y de seguridad. Cada medida se asocia a un modelo: `APT38/pagos`, `BlueNoroff-TraderTraitor/personas y activos digitales`, `Contagious Interview/contratación` | `KJ-1`. Coste cero, y es la condición para que todo lo demás tenga dueño | **Inmediato** |
| E-b | Desplegar `D-1`: detección del paso invariante, ejecución inducida desde el navegador —diálogo *Ejecutar*, intérprete lanzado por el navegador, `osascript` en macOS— | `KJ-2`. **La única detección del informe que no depende de indicadores perecederos** | 14 días |
| E-c | Revisar el plan de respuesta para el escenario **único** «destrucción masiva simultánea a fraude de pagos». Requisito explícito: el equipo de pagos no se subordina al de restauración, y la decisión de retroceso de transferencias no espera a que el parque esté operativo | `KJ-5`, y el precedente de `KJ-4`. **Es la decisión con más valor por euro de este informe para una entidad financiera** | 30 días |
| E-d | **Decisión de RR. HH. con Seguridad:** controles de verificación de identidad en contratación remota de perfiles técnicos, y revisión del parque de portátiles corporativos entregados a personal remoto y de su geolocalización efectiva | `KJ-7`. No es una medida de SOC y por eso se queda sin hacer | 30 días |
| E-e | Formación de nivel directivo sobre inducción a ejecutar, **y retirada del material que enseña a detectar vídeo sintético por su aspecto** | `E-1`. Mantener esa formación es peor que no tenerla: entrena una confianza injustificada | 45 días |
| E-f | **Decidir y documentar que los indicadores de la campaña Web3 NO se ingieren en los controles de la red de pagos**, salvo justificación caso por caso | `KJ-1`. Evita el ruido que desacredita el programa de inteligencia ante el equipo de pagos | 60 días |
| E-g | Procedimiento de verificación fuera de banda para toda solicitud inesperada dirigida a personas con autoridad sobre fondos, claves de firma o relaciones con inversores, con canal conocido previamente acordado | Recomendación explícita de la fuente primaria, y la que ella misma destaca como conclusión | 60 días |
| E-h | **Decisión de Legal y Riesgo:** posición sobre custodia y segregación de criptoactivos corporativos, si los hay, y sobre quién puede firmar una transacción sin control de doble persona | `KJ-6`. Si la respuesta es «una sola persona», ese nombre está en la misma lista de objetivos que los 677 | 90 días |

---

# NIVEL OPERACIONAL
### Para: Jefatura de SOC · Respuesta a Incidentes · Threat Hunting · Riesgo Operacional · RR. HH. · Horizonte: semanas–meses

## O-1. Identificación: el mapa de alias, que es el núcleo del informe

Esta sección es larga a propósito. Es la única parte del documento que, si se lee mal, invalida el resto.

**O-1.1 — El paraguas y lo que hay debajo**

| Designación | Origen | Qué designa realmente | Grado de equivalencia |
|---|---|---|---|
| `Lazarus Group` · `G0032` | Nombre de consenso de la industria; `HIDDEN COBRA` en avisos del Gobierno de EE. UU.; `Diamond Sleet` y antes `ZINC` en Microsoft | **Paraguas de origen.** La actividad cibernética ofensiva atribuida al Buró General de Reconocimiento de la RPDC | **No es equivalente a nada: es un conjunto.** Usarlo como sujeto de una frase operativa es el error de `KJ-1` |
| `APT38` · `G0082` | Mandiant / FireEye, 2018 | **El modelo financiero institucional:** intrusión larga en entidades financieras, manipulación de mensajería de pagos interbancaria, destrucción como señuelo. **Es el del Banco de Chile** | **Subconjunto con misión propia.** No es sinónimo de Lazarus |
| `BlueNoroff` | Kaspersky | **El modelo financiero contra personas y activos digitales.** La fuente primaria lo describe como subgrupo con motivación financiera del Lazarus Group, atribuido públicamente al Buró General de Reconocimiento, **activo desde al menos 2014** | **Solapa con APT38 en la literatura y no es su sinónimo.** En 2026 su comportamiento documentado es el de `T-1.B`, no el de `T-1.A` |
| `TraderTraitor` | Avisos conjuntos del Gobierno de EE. UU. | **El modelo de criptoactivos y cadena de suministro de software de blockchain.** Es la unidad a la que se atribuyó preliminarmente el vaciado del puente de KelpDAO en abril de 2026 | **Designación de campaña y de conjunto de TTP**, de uso gubernamental. Solapamiento parcial con BlueNoroff |
| `Sapphire Sleet` | Microsoft | Ingeniería social contra el sector de criptoactivos | **Solapamiento parcial con BlueNoroff.** No tratar como equivalente sin verificar en el informe concreto |
| `Contagious Interview` · `DeceptiveDevelopment` · `Famous Chollima` | Varios proveedores | **El modelo de la contratación:** proceso de selección falso, prueba técnica maliciosa, y colocación de trabajadores remotos | **Modelo distinto, vector distinto, dueño distinto.** Es `O-3.C` |
| `Andariel` · `Onyx Sleet` | Varios proveedores | Espionaje y, en algunos periodos, extorsión, con foco en Corea del Sur | **Fuera del alcance de este informe** |

**O-1.2 — La prueba de que la distinción no es académica**

| Dimensión | Modelo APT38 (Banco de Chile, 2018) | Modelo BlueNoroff / TraderTraitor (2026) |
|---|---|---|
| Víctima | Una **institución** financiera | Una **persona** con autoridad sobre activos |
| Vector de entrada | Intrusión en la red corporativa, meses de permanencia | Contacto profesional de apariencia legítima y **ejecución manual inducida** |
| Objetivo técnico | Los sistemas que originan y validan mensajería de pagos | Credenciales, sesiones, claves de firma y contactos del individuo |
| Monetización | Transferencia interbancaria a una cuenta controlada | Transferencia de activos digitales desde carteras o plataformas |
| Salida | **Destrucción masiva como señuelo** | Reutilización del acceso para alcanzar al siguiente objetivo |
| Dónde se detecta | Red interna, cambios en el entorno de pagos, creación de cuentas | **El puesto del directivo, en el momento de la ejecución manual** |
| Quién defiende | Riesgo operacional, equipo de pagos, SOC | Formación directiva, control de ejecución en el puesto, verificación fuera de banda |
| **Indicadores comunes entre ambos modelos** | **Ninguno** | **Ninguno** |

> ⚠ **Nota de *tradecraft*.** La última fila de esa tabla es el informe entero.
> Dos conjuntos de actividad que comparten atribución estatal y **no comparten
> un solo indicador** no pueden defenderse con el mismo programa. La fusión de
> alias es, según la propia plantilla de esta cartera, una de las principales
> fuentes de error analítico; aquí el error no sería confundir dos actores
> distintos, sino **tratar como uno a lo que la propia industria describe como
> un conjunto de equipos con misiones separadas**.

## O-2. Estructura y atribución

| Eje de atribución | Valoración | Confianza |
|---|---|---|
| Nexo estatal del paraguas | **Establecido, y con base jurídica, no sólo técnica.** Acusaciones federales estadounidenses contra operadores nombrados y designaciones de sanciones. Atribución pública al Buró General de Reconocimiento | **Alta** |
| Clúster técnico de la campaña de 2026 | **Establecido.** La fuente primaria tuvo acceso a la biblioteca de material del propio actor durante seis meses, y vincula la infraestructura nueva con la de abril por convenciones de nombre, comandos de entrega y hábitos de certificado | Alta |
| Que la campaña de 2026 sea de BlueNoroff | Valorado por la fuente primaria, que lo describe como subgrupo con motivación financiera del Lazarus Group | Moderada-alta |
| Atribución del Banco de Chile (2018) a APT38 | **Valoración de proveedor.** FireEye lo incluye entre los ataques contra SWIFT que atribuye a APT38. Otras fuentes atribuyen al ecosistema Lazarus más amplio, con menos convicción. **Debilitamiento conocido:** el borrador compartía guion de instalador NSIS con código de Buhtrap filtrado públicamente en febrero de 2018, de modo que la identidad de código —el eje de la atribución— es menos concluyente de lo que parece | **Moderada** |
| Atribución del incidente de KelpDAO (abril de 2026) a TraderTraitor | **Preliminar, y así se publicó.** Atribución preliminar comunicada por la plataforma afectada | Baja |
| Identidad nominal | **Parcialmente establecida** por vía judicial para varios operadores y facilitadores, incluidas las catorce personas acusadas en octubre de 2026. Son imputaciones | Moderada |

*Razonamiento:* un bloque cuya atribución estatal está sostenida por acusaciones judiciales y designaciones es un caso raro en esta cartera, donde la mayoría de los nexos estatales son valoraciones de proveedor. **Eso hace más llamativo que la atribución de incidentes concretos sea mucho más débil que la atribución del conjunto.** Es una asimetría que conviene tener presente: se sabe con solidez quién está detrás del programa y con fragilidad quién hizo cada cosa.

*Contraargumento que hay que mantener vivo:* el uso de código filtrado públicamente —el caso de Buhtrap en 2018— y la existencia de un mercado de herramientas significan que la identidad de código es un eje débil para este bloque en particular. Una atribución que descanse sólo en ella debe leerse con la confianza que corresponde.

## O-3. Los tres modelos de operación, uno por uno

### O-3.A — El modelo institucional de pagos (APT38)

Es el que tiene precedente nacional y el que la mayoría de las entidades financieras de la región cree que está defendiendo cuando habla de este actor. Su estructura es: intrusión en la red corporativa por los medios habituales; permanencia prolongada y silenciosa mientras se aprende el entorno de pagos, que es específico de cada entidad y no se puede automatizar; manipulación de la originación o la validación de la mensajería para emitir transferencias que parecen legítimas; y una salida que es la innovación real del modelo.

**La salida merece su propio párrafo.** En el Banco de Chile, la destrucción de unos nueve mil puestos de trabajo y quinientos servidores no fue un sabotaje ni una extorsión: fue **un dispositivo de retardo**. Mientras cuatro transferencias por unos diez millones de dólares viajaban hacia una cuenta en Hong Kong, la organización entera estaba ocupada en lo único que podía ver. Esa asimetría es deliberada y explota una propiedad estructural de la respuesta a incidentes: **lo visible desplaza lo importante**, y una transferencia internacional sólo es reversible durante un tiempo corto.

### O-3.B — El modelo de personas y activos digitales (BlueNoroff / TraderTraitor)

Es el vigente, y la fuente primaria lo describe con una precisión poco habitual porque lo observó desde dentro de la infraestructura del actor. Su ciclo, en los términos de la fuente, es una fábrica con dos extremos.

**Aguas arriba, el reconocimiento se ha ensanchado y se ha vuelto más deliberado.** El material de señuelo ya no se limita a fotografías de perfil y a grabaciones de cámara web de víctimas anteriores: se captura de **entrevistas en YouTube y charlas de congresos, grabadas en pantalla por el propio actor**. Eso permite reproducir la apariencia y la voz de una persona concreta —un fundador, un consejero delegado— y fabricar material de reunión falsa **sin necesidad de comprometerla**. La consecuencia es contraintuitiva y conviene decirla sin rodeos: la visibilidad pública de un directivo se ha convertido en materia prima para atacar a los de su círculo.

**Aguas abajo, el bucle de reciclaje se ha acelerado.** Cada objetivo comprometido aporta dos cosas: material de vídeo real para poblar las reuniones falsas siguientes, y contactos para alcanzar a su círculo profesional. La producción pasó de un editor con un portátil y una herramienta de edición convencional a una cadena de servicios comerciales de generación, y el resultado es que **los vídeos ya no se distinguen de una grabación auténtica por inspección visual**. Los analistas de la fuente lo declararon así y adoptaron, por eso, una regla metodológica que esta cartera adopta también: **la determinación de falsedad se hace por procedencia, no por apariencia**.

**Y en el medio, el paso que no ha cambiado.** Todos los señuelos, por variados que sean —documento compartido que no se puede descifrar, verificación de identidad, actualización del visor de PDF, reproductor de medios, acceso a monedero físico, auditoría de seguridad—, siguen el mismo patrón: se establece confianza profesional, **se fabrica un problema técnico**, y se persuade a la persona de ejecutar una «solución» que trae la etapa siguiente. La fuente lo resume en una frase que vale como política: trátese toda petición de ejecutar un comando, un guion, un atajo o un flujo de trabajo como una señal de alarma, por pulida que parezca la interacción, y confírmese por un canal distinto conocido de antemano.

### O-3.C — El modelo de la contratación (Contagious Interview y trabajadores remotos)

Tiene dos caras y conviene no confundirlas.

**La cara ofensiva** es el proceso de selección falso: se contacta a un desarrollador con una oferta creíble y se le pide ejecutar una prueba técnica —un repositorio, un paquete, un proyecto— que contiene el implante. La víctima es el desarrollador y, a través de él, su empleador.

**La cara de infiltración** es la inversa y es la que casi nadie cubre: **el operador es el candidato**. Trabajadores remotos que obtienen empleo con identidades ajenas, y facilitadores locales que reciben en su domicilio los portátiles que entrega la empresa y los mantienen encendidos para que el acceso remoto parezca doméstico. El expediente judicial de octubre de 2026 describe el mecanismo con detalle: catorce personas acusadas, más de setenta empresas afectadas, alrededor de tres millones de dólares generados, y más de cuarenta «granjas de portátiles» desarticuladas en Texas entre el 21 y el 25 de septiembre de 2026. La acusación describe además el uso de identidades de más de veinticinco ciudadanos por parte de un solo facilitador.

> **Lo que este tercer modelo significa para una organización de la región.** No
> hay nada que detectar en la red, porque el acceso es legítimo: lo concede un
> contrato. Las señales están en el proceso de contratación —currículos que
> comparten huella, entrevistas donde la cámara falla siempre, direcciones de
> entrega que no coinciden con la residencia declarada, software de control
> remoto instalado el primer día— y en la geolocalización efectiva del
> dispositivo corporativo frente a la declarada. **Nada de eso lo mira el SOC
> hoy, y ninguna de esas comprobaciones es difícil.** Es `E-d`.

## O-4. Nuestra exposición

> ⬛ **Sección sin evaluar — requiere telemetría interna y datos de RR. HH.**
> El cuestionario está separado por modelo, porque las respuestas las tienen
> áreas distintas y mezclarlas es cómo se queda sin hacer.

**Modelo de pagos (`O-3.A`) — responde Riesgo Operacional y el equipo de pagos**

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| A-1 | ¿Qué puestos y servidores pueden originar o validar mensajería de pagos interbancaria, y están segmentados de la red corporativa general? | Inventario · arquitectura | Pagos · Redes |
| A-2 | ¿Existe control de doble persona efectivo —no sólo nominal— para transferencias por encima de un umbral, y puede un administrador de sistemas eludirlo? | Procedimientos | Riesgo Operacional |
| A-3 | **¿Nuestro plan de respuesta contempla destrucción masiva y fraude de pagos como un ÚNICO evento?** Si son dos escenarios separados, ¿quién decide cuál se atiende primero? | Plan de RI | Riesgo · CISO |
| A-4 | ¿Cuánto tarda hoy la organización en poder solicitar el retroceso de una transferencia internacional, **con el parque de puestos caído**? | Ejercicio | Pagos · Tesorería |
| A-5 | ¿Tenemos registro inmutable y fuera de banda de la mensajería emitida, que sobreviva a la destrucción de los puestos? | Arquitectura | Pagos · TI |
| A-6 | ¿Están protegidos el sector de arranque y el acceso crudo a disco en los servidores críticos? | Configuración · EDR | TI/Puesto |

**Modelo de personas y activos digitales (`O-3.B`) — responde Seguridad y Dirección**

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| B-1 | ¿Quién en la organización tiene autoridad para mover fondos o firmar transacciones **por sí solo**? La lista de nombres es la lista de objetivos | Procedimientos | Riesgo · Dirección |
| B-2 | ¿Tenemos criptoactivos corporativos? ¿En custodia propia o de tercero? ¿Quién tiene las claves? | Tesorería | Riesgo · Legal |
| B-3 | ¿Está bloqueado el diálogo *Ejecutar* de Windows por política para los puestos de dirección? ¿Y la ejecución de intérpretes lanzados desde el navegador? | GPO · EDR | TI/Puesto |
| B-4 | En macOS, ¿hay control sobre `osascript` y sobre la ejecución de comandos pegados en el terminal por puestos de dirección? | MDM · EDR | TI/Puesto |
| B-5 | ¿Existe un canal fuera de banda **acordado de antemano** para verificar solicitudes inesperadas, y los directivos saben cuál es sin tener que buscarlo? | Procedimientos | Seguridad · Dirección |
| B-6 | ¿Qué directivos tienen entrevistas, charlas de congreso o grabaciones públicas en vídeo? Esa lista es el inventario de materia prima disponible para suplantarlos | OSINT propio | Comunicación · Seguridad |
| B-7 | ¿Nuestra formación actual enseña a detectar vídeo falso **por su aspecto**? Si sí, hay que retirarla | Catálogo de formación | RR. HH. · Seguridad |

**Modelo de contratación (`O-3.C`) — responde RR. HH.**

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| C-1 | ¿Cuántos perfiles técnicos remotos hemos contratado en 24 meses, y cómo se verificó su identidad? | RR. HH. | RR. HH. |
| C-2 | ¿Coincide la dirección de entrega del portátil corporativo con la residencia declarada, en todos los casos? | Logística · RR. HH. | RR. HH. · TI |
| C-3 | ¿Dónde está, de verdad, cada portátil corporativo de personal remoto? ¿Coincide la geolocalización efectiva con la declarada? | MDM · telemetría de red | TI |
| C-4 | ¿Hay software de control remoto de terceros instalado en portátiles de personal remoto, y cuándo se instaló respecto a la fecha de alta? | Inventario de software | TI/Puesto |
| C-5 | ¿Se accede a nuestros sistemas desde proxies residenciales o VPN comerciales por cuentas de empleado? | Registros de acceso | SOC |
| C-6 | ¿Hemos pedido alguna vez a un candidato técnico ejecutar código ajeno en su equipo como parte de una prueba, **o lo hemos aceptado de un candidato**? | Proceso de selección | RR. HH. · Ingeniería |

## O-5. Cronología

<!-- cti:timeline -->

| Fecha | Hecho | Traza |
|---|---|---|
| `2014` | **Inicio de la actividad de BlueNoroff** según la fuente primaria: «activo desde al menos 2014», centrado en la generación de ingresos | Global |
| `2016-02` | Golpe contra la mensajería de pagos de un banco central asiático: el caso que estableció el modelo de `O-3.A` ante la industria | Global |
| `2018-02` | **Se filtra públicamente el código de Buhtrap.** Tres meses antes del incidente chileno, y el detalle que debilita su atribución por identidad de código | Global |
| `2018-05` | **Banco de Chile.** Destrucción de ≈9.000 puestos y 500 servidores; **cuatro transferencias SWIFT fraudulentas** por unos 10 millones de dólares a una cuenta en Hong Kong. El borrador era una variante de la familia HERMES y actuó como señuelo | **Chile** |
| `2018-10` | FireEye publica el expediente de **APT38** e incluye el incidente chileno entre los ataques contra SWIFT que le atribuye | Global |
| `2022` | Primeros avisos conjuntos gubernamentales sobre **TraderTraitor** y el sector de cadenas de bloques | Global |
| `2025` | **Año récord de robo de criptoactivos:** Chainalysis calcula al menos 2.020 millones de dólares robados por actores vinculados a la RPDC | Global |
| `2026-03-01` | Una plataforma de tarjetas regalo y criptoactivos atribuye a este bloque una brecha cuyo punto de entrada fue **el portátil comprometido de un empleado** | Global |
| `2026-04` | **Arctic Wolf publica el primer informe de la campaña:** reuniones falsas de Zoom y Teams, mensajes de tipo *ClickFix*, participantes generados con IA. 400+ objetivos identificados, 100 verificados, 20 países | Global |
| `2026-04` | **KelpDAO.** Vaciado de unos 292 millones de dólares en `rsETH` —unos 116.500 `rsETH`— del puente basado en LayerZero. Atribución **preliminar** a TraderTraitor; unos 71 millones congelados después | Global |
| `2026-04` | TRM Labs estima unos 577 millones de dólares robados por actores vinculados a la RPDC en lo que va de año | Global |
| `2026-09-21 → 25` | **Operación «Lonestar Roundup»:** se desarticulan más de cuarenta «granjas de portátiles» en Texas | Global |
| `2026-10-01` | **Acusación federal en Ohio:** catorce personas imputadas por el esquema de empleo remoto. Más de 70 empresas afectadas, ≈3 millones de dólares | Global |
| `2026-11-06` | Fecha de corte del análisis forense de 349 vídeos de la biblioteca del actor marcados como probablemente modificados | Global |
| `2026-11-12` | **Arctic Wolf publica «Still in the Meeting: BlueNoroff Six Months On».** 677 objetivos en 58 países, 84 % alta dirección, 98 dominios —73 nuevos—, y el hallazgo central: **cambió las señales, no el mecanismo** | Global |
| `2026-11-17` | Emisión de este informe. **Sin ninguna intrusión de este bloque confirmada públicamente en 2026 en entidades financieras de Chile, Perú, Colombia o Ecuador** | **Chile / LATAM** |

## O-6. Hipótesis alternativas consideradas

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| **H1 — Los tres modelos son equipos distintos con misiones separadas** | Consistente con la literatura de la industria, con la asignación de designaciones distintas por parte de proveedores y gobiernos, y con la ausencia total de indicadores comunes entre los expedientes de 2018 y 2026 | `Retenida · probable 55–80 %` |
| **H2 — Hay un único centro que asigna recursos entre modelos** | Consistente con el comportamiento de cartera descrito en `E-1` y con la atribución común a un mismo organismo estatal. **No es incompatible con H1**, y su diferencia práctica importa: si es cierta, un endurecimiento en un modelo desplaza esfuerzo hacia otro, en lugar de reducirlo | `Retenida · posibilidad real 45–55 %` |
| **H3 — Hay víctimas regionales de 2026 no publicadas** | Sin evidencia. Consistente con el sesgo de publicación: en la región hay menos informes de respuesta a incidentes publicados que en los mercados centrales, y una entidad financiera latinoamericana tiene incentivos regulatorios y reputacionales fuertes para no publicar. **Se retiene como hipótesis de caza, y es la que `I-1` vigila** | `Retenida para caza` |
| **H4 — La actividad de 2026 contra cooperativas ecuatorianas existe** | **Sin evidencia.** Se buscó específicamente, en español, con la terminología del supervisor. Se consigna como descartada **como hallazgo** para que no se reabra como si lo fuera | `Descartada como hallazgo · G-1` |
| **H5 — La generación sintética cambió el mecanismo de intrusión** | **Falsada por la fuente primaria**, que afirma que la IA es multiplicador de producción y que la campaña sigue dependiendo de investigación del objetivo, infraestructura a medida y ejecución manual | `Descartada` |
| **H6 — El modelo de 2018 está desmantelado** | Inconsistente con `E-1`: lo que decide la línea de negocio es el rendimiento, no la capacidad. No hay evidencia de que la capacidad se haya perdido, sólo de que no se está usando | `Poco probable · 20–45 %` |
| **H7 — La atribución del Banco de Chile a APT38 es incorrecta** | **Se retiene explícitamente.** El código del borrador compartía elementos con material filtrado tres meses antes, y la atribución es de un proveedor con confianza declarada variable. Que se retenga **no cambia ninguna decisión** de este informe: las medidas de `O-3.A` son correctas con independencia de quién lo hizo | `Retenida · poco probable 20–45 %` |

**Supuesto clave.** Que el paso de ejecución manual sigue siendo necesario. Todo `D-1`, toda `E-b` y buena parte de `E-e` dependen de ello. **Qué se rompe si es falso:** si apareciera una variante con ejecución sin interacción —un día cero de navegador—, la defensa volvería a depender de parcheo y de indicadores perecederos, es decir, del terreno donde este adversario tiene ventaja. Es el falsador `(b)` de `§1` y el disparador `I-2`.

**Pre-mortem.** Es mayo de 2027 y este informe resultó equivocado. Los tres motivos más probables:

1. **Se leyó `KJ-3` como «no nos afecta».** Que no haya evidencia de operaciones regionales contra bancos no significa que no haya exposición: significa que la exposición está en tres personas y en un proceso de contratación, no en el perímetro. Si alguien cierra el informe concluyendo que esto es un problema de otros países, habrá leído la frase correcta y sacado la conclusión opuesta.
2. **Se montó la defensa sobre los 98 dominios.** Son 98 hoy; 73 de ellos eran nuevos respecto al informe de hace siete meses. La infraestructura se renueva más rápido de lo que se publica, y el Anexo A de este informe **ni siquiera los contiene**. Quien base el programa en indicadores de red estará permanentemente siete meses por detrás.
3. **`E-d` no se hizo porque no tenía dueño.** Es la decisión más barata del informe y la única que no pertenece a Seguridad. Las medidas que requieren que dos áreas se pongan de acuerdo son las que se quedan sin hacer, y ésta requiere que RR. HH. acepte un control que hoy no tiene.

## O-7. Indicadores y señales de alerta

| # | Indicador observable | Qué señalaría | Disciplina | Responsable |
|---|---|---|---|---|
| I-1 | **Publicación de cualquier intrusión confirmada en una entidad financiera de Chile, Perú, Colombia o Ecuador atribuida a este bloque** | `KJ-3` obsoleto. **Reemisión del informe en 48 horas** y reasignación de prioridades de `E-4` | OSINT · CSIRT nacionales | Célula CTI |
| I-2 | Muestra de este bloque que logre ejecución **sin interacción manual** del usuario | Rompe el supuesto clave. `D-1` deja de ser suficiente | OSINT · TECHINT | Célula CTI |
| I-3 | Un golpe nuevo contra mensajería de pagos interbancaria, en cualquier país, con destrucción simultánea | El modelo de `O-3.A` vuelve a estar activo. Eleva `E-c` a prioridad máxima | OSINT | Célula CTI |
| I-4 | Identificación de facilitadores o «granjas de portátiles» en Latinoamérica | Amplía `KJ-7` de la contratación a la infraestructura regional | OSINT · judicial | Célula CTI |
| I-5 | Endurecimiento regulatorio de la custodia de criptoactivos en mercados centrales | Precede al desplazamiento hacia mercados de supervisión más joven. **Alerta temprana regulatoria, no técnica** | OSINT regulatorio | Riesgo · Célula CTI |
| I-6 | Aparición de señuelos de esta campaña **en español** | Cambio de selección lingüística. Hoy el material documentado no es hispanohablante | OSINT | Célula CTI |
| I-7 | Un directivo propio reporta una reunión con problemas técnicos y una solicitud de ejecutar algo | **No es un indicador de inteligencia: es un incidente.** Figura aquí porque la vía de reporte tiene que existir antes de que haga falta | Interna | Seguridad |
| I-8 | Publicación por la fuente primaria de un tercer informe de seguimiento | Renovación de los 98 dominios y posible cambio de temas de señuelo. Revisión del Anexo A | OSINT | Célula CTI |

---

# NIVEL TÁCTICO
### Para: Analistas de SOC · Ingeniería de Detección · Threat Hunting · Horizonte: días–semanas

## T-1. Las dos cadenas de intrusión, que no se parecen

Esta sección lleva dos cadenas porque hay dos modelos. Compararlas es el ejercicio más útil del informe: **ninguna etapa de una se corresponde con ninguna etapa de la otra**.

### T-1.A — Cadena del modelo institucional de pagos (APT38 · patrón del Banco de Chile, 2018)

<!-- cti:stages title="Tres etapas, y la tercera es un señuelo" dwell="next" -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 01 · Entrada y permanencia | Acceso corporativo ordinario, paciencia extraordinaria | phishing o explotación de servicio expuesto · credenciales · movimiento lateral · **meses de aprendizaje del entorno de pagos**, que es específico de cada entidad y no se automatiza |
| Etapa 02 · Pagos | Manipular la emisión, no robar el dinero del cajero | acceso a los sistemas que originan y validan la mensajería · emisión de **cuatro transferencias** que parecen legítimas · destino en una jurisdicción de recuperación difícil |
| Etapa 03 · Señuelo y salida | Destruir lo visible para proteger lo importante | borrador de la familia **HERMES** · ≈**9.000 puestos** y **500 servidores** inutilizados · la organización atiende la restauración mientras la transferencia se hace irreversible |

**Permanencia:** el expediente público no da la mediana, pero la estructura del modelo exige meses: aprender el entorno de pagos de una entidad concreta no es un paso automatizable. **Y el dato de permanencia que de verdad importa en este modelo no es el del atacante, es el nuestro:** el tiempo que la organización tarda, **con el parque de puestos destruido**, en poder solicitar el retroceso de una transferencia internacional. Ese número no lo tiene casi nadie medido, y es la pregunta `A-4` de `O-4`.

### T-1.B — Cadena del modelo de personas y activos digitales (BlueNoroff · campaña vigente, 2026)

<!-- cti:stages title="Tres etapas, y la segunda la ejecuta la víctima" dwell="next" -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 01 · Confianza | Un contacto profesional que encaja con lo que el objetivo hace a diario | reconocimiento sobre entrevistas en **YouTube** y charlas de congresos grabadas en pantalla · **vídeo sintético** de participantes · contactos heredados de víctimas anteriores · señuelos alineados con captación de inversión, inversión en activos digitales, auditoría y verificación de identidad |
| Etapa 02 · Fabricación del problema y **ejecución manual** | El punto de corte, y no ha cambiado en seis meses | reunión que «falla» · documento protegido que «no se puede descifrar» · «actualización» del visor de PDF de Chrome · reproductor de medios falso · verificación de identidad · **la persona ejecuta un comando, un guion o un atajo que le han dado** |
| Etapa 03 · Cosecha y reciclaje | Lo que se llevan alimenta el siguiente ataque | credenciales · sesiones autenticadas · **claves de firma** · contactos del círculo profesional · **vídeo real de la propia víctima** para poblar las reuniones falsas siguientes |

**Permanencia:** no publicada, y es poco relevante en este modelo. Lo que importa aquí no es cuánto tiempo está el adversario dentro, sino **cuánto tarda en consumarse una transferencia de activos digitales**, que puede ser minutos, y es irreversible por diseño. **El tiempo de respuesta útil en este modelo es anterior al compromiso**: está en la etapa 01, en la verificación fuera de banda de `E-g`.

> ⚠ **Lo que `NovaStream` enseña, y es lo que convierte esta campaña en una
> fábrica.** La fuente primaria documenta un señuelo concreto —un reproductor
> de medios fabricado— y lo rastrea **desde antes de existir**: apareció en la
> biblioteca de material del actor como ilustración generada con IA, guías para
> el operador y guiones de prueba, **antes de entrar en servicio**. Es decir:
> hay una fase de producción observable que precede a la fase operativa. Para
> quien tenga acceso a esa clase de visibilidad, eso es alerta temprana real;
> para el resto, que somos casi todos, la lección es más modesta y más útil:
> **la marca, el aspecto y el nombre del señuelo son lo que el adversario
> fabrica a voluntad y renueva sin coste**. Construir la defensa sobre eso es
> construirla sobre lo único que él controla por completo.

## T-2. Mapa MITRE ATT&CK

La fuente primaria publica su mapeo en un anexo no extraíble. La tabla siguiente es **mapeo propio** de los procedimientos descritos en la prosa de las fuentes, y se declara como tal fila por fila. Va separada por modelo, por el mismo motivo que todo el informe.

<!-- cti:matrix -->

| Táctica | ID | Técnica | Procedimiento observado |
|---|---|---|---|
| Reconocimiento | T1593.001 | Search Open Websites/Domains: Social Media | **Modelo B.** Captura de material de señuelo desde perfiles profesionales y redes sociales *(mapeo propio)* |
| Reconocimiento | T1593 | Search Open Websites/Domains | **Modelo B.** **Grabación en pantalla de entrevistas en YouTube y charlas de congresos** para reproducir apariencia y voz de una persona concreta sin comprometerla *(mapeo propio; procedimiento literal de la fuente)* |
| Reconocimiento | T1589.002 | Gather Victim Identity Information: Email Addresses | **Modelo B.** Contactos heredados de objetivos comprometidos previamente, que alimentan el bucle de reciclaje *(mapeo propio)* |
| Desarrollo de recursos | T1585.001 | Establish Accounts: Social Media Accounts | **Modelo B y C.** Identidades profesionales fabricadas para el contacto inicial y para los procesos de selección falsos *(mapeo propio)* |
| Desarrollo de recursos | T1583.001 | Acquire Infrastructure: Domains | **Modelo B.** **98 dominios de alta confianza, 73 no reportados antes**, con convenciones de nombre, comandos de entrega y hábitos de certificado que los vinculan a la actividad de abril *(fuente primaria)* |
| Desarrollo de recursos | T1588.007 | Obtain Capabilities: Artificial Intelligence | **Modelo B.** Combinación de varios servicios comerciales de generación para ilustración, avatares y **vídeo sintético de participantes**, con un flujo de edición maduro *(fuente primaria)* |
| Desarrollo de recursos | T1608.001 | Stage Capabilities: Upload Malware | **Modelo B.** Sitios de «actualización» falsos que sirven la etapa siguiente *(fuente primaria)* |
| Acceso inicial | T1566.003 | Phishing: Spearphishing via Service | **Modelo B.** Contacto por plataformas profesionales y de reuniones, no por correo corporativo *(mapeo propio)* |
| Acceso inicial | T1566.001 | Phishing: Spearphishing Attachment | **Modelo A.** Vector de entrada histórico a la red corporativa *(mapeo propio)* |
| Acceso inicial | T1190 | Exploit Public-Facing Application | **Modelo A.** Alternativa de entrada a la red corporativa *(mapeo propio)* |
| Acceso inicial | T1199 | Trusted Relationship | **Modelo C.** **El acceso lo concede un contrato de trabajo.** No hay explotación *(mapeo propio)* |
| Ejecución | T1204.004 | User Execution: Malicious Copy and Paste | **Modelo B. La técnica central de la campaña vigente.** El patrón *ClickFix*: una página de aspecto confiable instruye a la persona para que pegue y ejecute un comando. **Es el paso que no ha cambiado en seis meses** *(fuente primaria)* |
| Ejecución | T1059.001 | Command and Scripting Interpreter: PowerShell | **Modelo B.** Patrones de ejecución de PowerShell **sin fichero**, según la detección que la fuente declara tener en producción *(fuente primaria)* |
| Ejecución | T1059.002 | Command and Scripting Interpreter: AppleScript | **Modelo B.** El señuelo del visor de PDF de Chrome **inicia una descarga por AppleScript** en el flujo recuperado de macOS. Patrón `osascript` declarado por la fuente *(fuente primaria)* |
| Ejecución | T1059.004 | Command and Scripting Interpreter: Unix Shell | **Modelo B.** Patrón de `curl` encadenado a un intérprete, declarado por la fuente *(fuente primaria)* |
| Ejecución | T1072 | Software Deployment Tools | **Modelo C.** Herramientas de control remoto instaladas sobre un equipo corporativo con acceso legítimo *(mapeo propio)* |
| Persistencia | T1543 | Create or Modify System Process | **Modelo B.** Técnicas de persistencia documentadas en el informe de abril *(fuente primaria, por referencia)* |
| Defensa | T1055 | Process Injection | **Modelo B.** Declarado por la fuente entre las técnicas con detección en producción *(fuente primaria)* |
| Defensa | T1036 | Masquerading | **Modelo B.** Marcas y nombres legítimos suplantados: Chrome, visores de PDF, plataformas de reunión, reproductores de medios *(fuente primaria)* |
| Defensa | T1656 | Impersonation | **Modelo B.** **Vídeo sintético de personas reales e identificables** en reuniones. La fuente adopta la definición de *deepfake* de la GAO estadounidense y clasifica por procedencia, no por apariencia *(fuente primaria)* |
| Credenciales | T1555.003 | Credentials from Password Stores: Credentials from Web Browsers | **Modelo B.** Objetivo declarado: credenciales y accesos del individuo *(mapeo propio)* |
| Credenciales | T1539 | Steal Web Session Cookie | **Modelo B.** Sesiones autenticadas, que eluden el segundo factor sin atacarlo *(mapeo propio)* |
| Descubrimiento | T1087 | Account Discovery | **Modelo A.** Reconocimiento interno durante la permanencia prolongada *(mapeo propio)* |
| Recolección | T1125 | Video Capture | **Modelo B.** El informe de abril documenta **grabación de la cámara web de los objetivos** mientras intentaban arreglar la reunión falsa, y ese material alimentó reuniones posteriores *(fuente primaria, por referencia)* |
| Recolección | T1114 | Email Collection | **Modelo B.** Cuentas comprometidas «saqueadas en busca de contactos», en los términos de la fuente *(fuente primaria)* |
| Mando y control | T1071.001 | Application Layer Protocol: Web Protocols | Ambos modelos *(mapeo propio)* |
| Mando y control | T1105 | Ingress Tool Transfer | **Modelo B.** El comando ejecutado por la víctima recupera la etapa siguiente *(fuente primaria)* |
| Impacto | T1565.001 | Data Manipulation: Stored Data Manipulation | **Modelo A.** Manipulación de la originación y validación de mensajería de pagos *(mapeo propio)* |
| Impacto | T1561.002 | Disk Wipe: Disk Structure Wipe | **Modelo A.** **≈9.000 puestos y 500 servidores inutilizados como señuelo**, no como objetivo *(mapeo propio sobre el expediente de 2018)* |
| Impacto | T1657 | Financial Theft | **Ambos modelos, y es el propósito.** Cuatro transferencias por ≈10 M USD en 2018; cientos de millones en activos digitales en 2025-2026 *(mapeo propio)* |

> **Una observación sobre `T1204.004`.** Que la técnica central de la campaña
> más industrializada de este bloque sea **«el usuario copia y pega un
> comando»** dice algo que conviene no perder entre los deepfakes y los
> servicios de generación: después de invertir en una cadena de producción de
> vídeo sintético, en 98 dominios y en reconocimiento sobre 677 personas, el
> adversario sigue necesitando que alguien **pegue una línea en una consola**.
> Toda la sofisticación está al servicio de que ese gesto parezca razonable.
> Por eso la contramedida no es tecnológica en su núcleo: es que ese gesto se
> vuelva socialmente impensable en la organización. Y por eso `E-e` está en el
> nivel estratégico y no aquí.

## T-3. Dónde atacamos en la Pirámide del Dolor

<!-- cti:pyramid -->

| Nivel | Qué contiene en este informe y qué vale | Valor |
|---|---|---|
| Hashes | **Prácticamente nada, y es deliberado.** El anexo de la fuente no es extraíble y este informe no publica hashes de la campaña vigente. Quien los necesite debe ir a la fuente. Su valor sería de todos modos sólo retrohunt | Base · valor trivial |
| IP · Dominios | **98 dominios existen y no están aquí.** Y el dato que importa sobre ellos no es la lista: es que **73 de 98 eran nuevos respecto al informe de siete meses antes**. Un programa basado en esta capa va estructuralmente por detrás. Para el modelo A, además, no hay infraestructura publicada reciente en absoluto | Valor bajo · **estructuralmente insuficiente** |
| Artefactos | **El rastro del gesto.** La clave de registro que guarda el historial del diálogo *Ejecutar* de Windows es el artefacto más valioso de este informe: conserva, en texto, lo que la víctima pegó. Sobrevive al reinicio y no depende de la familia de malware. En macOS, el equivalente es el historial del intérprete y la invocación de `osascript` | Valor medio · **empezar aquí en un caso real** |
| Herramientas | PowerShell, `curl`, `osascript`, el navegador, las plataformas de reunión, los servicios comerciales de generación de vídeo y las herramientas de control remoto: **todas legítimas**. En el modelo C, la «herramienta» es un contrato de trabajo | Valor alto |
| TTP | **Dos, y son el informe.** (1) **Inducción a ejecutar:** establecer confianza, fabricar un problema técnico, pedir que se ejecute la solución. No ha cambiado en seis meses de evolución intensa y es independiente de marca, dominio y plataforma. (2) **Destrucción como señuelo de un fraude de pagos**, que no es un indicador sino una hipótesis de plan de respuesta | Cima · valor máximo |

> **Y una conclusión sobre esta pirámide que no es la habitual.** En casi todos
> los informes de esta cartera, los niveles bajos aportan algo —retrohunt,
> contexto, corroboración—. Aquí la base está casi vacía, y no por descuido:
> **la campaña vigente se defiende entera desde la cima**, y el modelo
> histórico se defiende desde un plan de respuesta que no es detección en
> absoluto. Es, de todos los informes de esta cartera, el que menos depende de
> indicadores y el que más depende de decisiones. Si alguien pide «los IOC de
> Lazarus» para cerrar este expediente, la respuesta correcta es que ese
> expediente no se cierra con IOC.

## T-4. Hipótesis de caza prioritarias

<!-- cti:accordion critical="^(H-1|H-2|H-3)\b" regional="^H-1[0-2]\b" -->

**H-1 — Alguien ha pegado un comando en el diálogo *Ejecutar* de Windows.** La hipótesis de caza central para el modelo B, y la de mejor relación entre coste y conclusión de todo el informe. El patrón de inducción a ejecutar en Windows pasa casi siempre por que la víctima pulse la combinación de tecla de Windows y `R` y pegue una línea. Windows guarda ese historial en texto, por usuario, en `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU`. Cazar: volcar esa clave en todo el parque —o al menos en todos los puestos de dirección— y revisar manualmente las entradas. En un parque normal contiene `cmd`, `mstsc`, `\\servidor\recurso` y poco más. Cualquier entrada con `powershell`, `curl`, `mshta`, `-enc`, `iex`, `IEX`, `FromBase64String`, `conhost` o una URL es un hallazgo. Fidelidad: **muy alta**; la clave es texto que escribió el usuario, no telemetría inferida. Falsos positivos: administradores de sistemas, que se enumeran una vez. Ventana: lo que dure el perfil del usuario, que suele ser años. **Es la pregunta que convierte `O-4`/`B-3` en un hallazgo en una tarde.**

**H-2 — El navegador lanzó un intérprete.** La forma de detección, no sólo de caza, del mismo gesto. Buscar creaciones de proceso donde el padre sea un navegador —`chrome.exe`, `msedge.exe`, `firefox.exe`, `brave.exe`— o `explorer.exe`, y el hijo sea `powershell.exe`, `pwsh.exe`, `cmd.exe`, `mshta.exe`, `wscript.exe`, `cscript.exe`, `curl.exe` o `bitsadmin.exe`. En macOS, el equivalente: el navegador o `Terminal` lanzando `osascript`, `curl` o `/bin/sh -c`. Fidelidad: alta. Falsos positivos: algunos instaladores y portales corporativos que abren un script; se enumeran. **Nota importante:** la fuente primaria declara tener detección en producción precisamente para los patrones de PowerShell, de `curl` encadenado a intérprete y de `osascript`, lo que corrobora que éste es el punto de corte correcto.

**H-3 — Un puesto escribió en el disco en crudo, o tocó la configuración de arranque.** Hipótesis del modelo A, y la única que da margen de reacción en ese escenario. La destrucción masiva de `T-1.A` requiere, antes del impacto, acceso de escritura a estructuras de disco. Cazar: apertura de manejadores a `\\.\PhysicalDrive*` o `\\.\Harddisk*` con permiso de escritura por procesos que no sean el conjunto corto y conocido que lo necesita; ejecución de `bcdedit`, `bootcfg`, `vssadmin delete shadows`, `wbadmin delete`, `wmic shadowcopy delete`; y despliegue simultáneo de un ejecutable nuevo a muchos equipos por GPO, PsExec o el agente de gestión. Fidelidad: alta para el acceso crudo a disco, media para el despliegue masivo, que tiene uso legítimo. **El valor de esta hipótesis no es su fidelidad: es que es lo único que puede sonar antes de perder nueve mil puestos.** Falsos positivos: herramientas de copia de seguridad, de clonado y de cifrado de disco; se enumeran nominalmente y la lista es corta.

**H-4 — Hay una segunda sesión de navegador, o una sesión autenticada en uso desde dos sitios.** El objetivo declarado del modelo B incluye sesiones autenticadas, que eluden el segundo factor sin atacarlo. Del lado del puesto: procesos de navegador con un directorio de perfil no estándar, o sin ventana visible. Del lado de las aplicaciones: uso concurrente de la misma *cookie* de sesión, o una sesión que cambia de dirección de origen sin reautenticar. Fidelidad: alta en el lado de las aplicaciones, que es donde este procedimiento se ve de verdad. **Para los nombres de la lista `B-1`, esta caza debería ser permanente y no un ejercicio.**

**H-5 — Un directivo recibió un contacto profesional nuevo seguido de una invitación a reunión y de un problema técnico.** No se caza en registros: se pregunta, y hay que preguntarlo antes de que haga falta. La secuencia de `T-1.B`/etapa 01 es socialmente invisible porque es exactamente lo que ocurre en la captación de inversión legítima. Establecer, con los nombres de `B-1` y `B-6`, una conversación trimestral de quince minutos: contactos nuevos, reuniones con participantes no conocidos previamente, y cualquier momento en que alguien les haya pedido ejecutar algo. Fidelidad: no aplica; es colección humana. **Es la única «caza» de este informe que detecta la etapa 01, y por tanto la única que llega antes del compromiso.**

**H-6 — Se instaló software de control remoto en un portátil corporativo poco después de su entrega.** Hipótesis del modelo C. Cruzar la fecha de alta de cada empleado remoto con la fecha de instalación de cualquier herramienta de control remoto de terceros en su equipo. Una instalación en los primeros días es el patrón del facilitador: el portátil se queda en un domicilio y el acceso llega por encima. Fidelidad: alta como señal de política, media como señal de este actor. Falsos positivos: equipos de soporte que instalan su propia herramienta; se distingue por quién la instaló.

**H-7 — La geolocalización efectiva de un portátil corporativo no coincide con la declarada.** Continuación de la anterior. Comparar la geolocalización por dirección de origen y por telemetría del dispositivo con la residencia declarada en RR. HH., para todo el personal remoto. Y buscar accesos a través de proxies residenciales o VPN comerciales con cuentas de empleado. Fidelidad: media-alta. Falsos positivos: viajes, mudanzas no comunicadas y uso legítimo de VPN; **cada uno exige una conversación, que es precisamente el control**.

**H-8 — Un desarrollador ejecutó código de un repositorio o paquete externo como parte de un proceso de selección.** Hipótesis del modelo C en su cara ofensiva. Cazar: `node.exe`, `python.exe`, `npm`, `pip`, `yarn` ejecutándose con directorio de trabajo bajo `Downloads`, `Desktop` o un repositorio clonado recientemente, en el equipo de alguien de perfil técnico, especialmente fuera del horario habitual. Y, de forma complementaria, preguntar en Ingeniería si alguien está en un proceso de selección. Fidelidad: media; requiere contexto. **Si la organización no prohíbe explícitamente ejecutar pruebas técnicas de terceros en el equipo corporativo, esta caza encontrará cosas y ninguna será de este actor — y aun así habrá valido la pena.**

**H-9 — Hay cambios no autorizados en el entorno que origina mensajería de pagos.** Hipótesis del modelo A, y la más específica del sector. Para los puestos y servidores de `A-1`: cualquier ejecutable nuevo, cualquier cuenta creada o modificada, cualquier inicio de sesión interactivo fuera de la lista aprobada, cualquier cambio en configuración o plantillas de mensajería. Fidelidad: **muy alta, porque ese entorno debería ser inmutable**. Falsos positivos: ventanas de cambio planificadas, que se conocen. Si esta caza tiene ruido, el hallazgo es el ruido.

**H-10 — Búsqueda retrospectiva de los indicadores de la fuente, y de su ausencia.** Caza de alcance regional con una advertencia. Los 98 dominios están en el anexo no extraíble de la fuente primaria; quien tenga acceso al documento puede ejecutar el retrohunt. **Y hay que registrar explícitamente el resultado negativo con su limitación:** un retrohunt contra 98 dominios de los que 73 eran nuevos hace siete meses no descarta compromiso, descarta compromiso **por esa infraestructura**. Fidelidad: alta para el acierto, **nula como prueba de ausencia**.

**H-11 — ¿Alguien de la organización aparece en la lista de los 677?** Caza de alcance regional que sólo se puede hacer preguntando. La lista no es pública y describe a quién preparó material el actor. Si la organización es cliente de la fuente primaria, la pregunta es directa y vale la pena hacerla. Si no lo es, la aproximación es `B-6`: inventariar qué directivos tienen vídeo público suficiente para ser suplantados, que es el criterio de materia prima del actor. Fidelidad: no aplica. **El valor está en que la respuesta, sea cual sea, cambia la prioridad de `E-e`.**

**H-12 — ¿Hay señuelos de esta campaña en español?** Caza de alcance regional y, a día de hoy, la pregunta abierta más relevante para nosotros. Todo el material documentado de la campaña vigente es en inglés y dirigido a los ecosistemas de inversión en activos digitales de los mercados centrales. Vigilar la aparición de señuelos en español —o de dominios con temática de inversión en español registrados con las convenciones del clúster— es `I-6`, y sería la primera señal de que la región pasa de periferia a objetivo. Fidelidad: no aplica; es vigilancia.

## T-5. Brechas de visibilidad que hay que cerrar primero

| Brecha | Por qué importa aquí |
|---|---|
| Sin recolección de la clave de registro del diálogo *Ejecutar* | Deja ciega `H-1`, que es la caza de mejor fidelidad y menor coste del informe. **Es un valor de registro, no una fuente de telemetría nueva** |
| Sin registro de línea de comandos completa | Deja ciega `H-2` y la mitad de `H-8`: el discriminador está en los argumentos, no en el nombre del proceso |
| Sin telemetría de macOS | **La brecha más probable y la más grave en este expediente.** El flujo recuperado por la fuente para el señuelo del visor de PDF es de macOS, y los puestos de dirección de la región son desproporcionadamente macOS. Un EDR que sólo cubre Windows no ve esta campaña |
| Sin detección de acceso crudo a disco | Deja ciega `H-3`, y con ella la única alerta posible antes del impacto del modelo A |
| Sin segmentación ni registro diferenciado del entorno de pagos | Deja ciega `H-9`. Si los puestos de pagos están en la misma red y el mismo nivel de registro que el resto, no hay nada que distinguir |
| Sin datos de RR. HH. accesibles a Seguridad | Deja ciegas `H-6` y `H-7`. No es una brecha técnica: es una brecha de permisos y de acuerdo entre áreas |
| Sin detección de uso concurrente de sesión en las aplicaciones | Deja ciega la mitad útil de `H-4`. Es del lado del servicio, no del puesto |
| Sin canal de reporte directivo | Deja ciega `H-5`. Un directivo no abre un ticket: llama a alguien, y tiene que haber alguien a quien llamar |

---

# NIVEL TÉCNICO
### Para: Ingeniería de detección · Automatización · TIP/SIEM · Vida útil: meses, inusualmente

## X-1. Arsenal y capacidad

Separado por modelo, y con una advertencia: el detalle técnico del modelo B está en el anexo no extraíble de la fuente, de modo que esta tabla recoge lo que su prosa describe, no su anexo.

| Propiedad | Modelo A (pagos, 2018) | Modelo B (personas y activos digitales, 2026) |
|---|---|---|
| Vector | Intrusión de red convencional | **Contacto profesional + ejecución manual inducida** |
| Plataformas | Windows corporativo y servidores | **Windows, macOS y Linux**, con flujos específicos por plataforma |
| Ejecución | Herramientas de intrusión y de movimiento lateral | **PowerShell sin fichero**, `curl` encadenado a intérprete, **AppleScript (`osascript`)** |
| Componente destructivo | **Borrador de la familia HERMES**, con guion de instalador NSIS compartido con código de **Buhtrap filtrado en febrero de 2018** | Ninguno documentado |
| Objetivo técnico | Sistemas de originación y validación de mensajería de pagos | Credenciales, **sesiones autenticadas**, claves de firma, contactos |
| Infraestructura | No publicada recientemente | **98 dominios de alta confianza, 73 nuevos.** Clúster coordinado de servidores, vinculado al de abril por convenciones de nombre, comandos de entrega y **hábitos de certificado** |
| Producción de señuelos | No aplica | **Cadena de servicios comerciales de generación**: ilustración, avatares y vídeo sintético. Guías para el operador y guiones de prueba **anteriores a la puesta en servicio** |
| Antianálisis / evasión | Destrucción de la evidencia por destrucción del sistema | **Diálogo falso de «actualización completada»** tras la ejecución, para que la víctima no sospeche. Inyección de proceso, declarada por la fuente |
| Idioma del material | — | **Inglés.** No hay material en español documentado: es `I-6` |
| Selección | La institución | **La persona:** 84 % fundadores y alta dirección |

> **Un detalle de `X-1` que merece subrayado operativo: el diálogo de «éxito
> falso».** Tras la ejecución, la página muestra un cuadro de diálogo con la
> marca de Chrome diciendo que la actualización se ha completado — y la fuente
> señala que reproduce el mismo mecanismo de falso éxito que ya se observó en
> las intrusiones por reunión falsa. Eso tiene una consecuencia directa sobre
> la respuesta: **la víctima no tiene ningún motivo para reportar nada**. Su
> experiencia es que el problema se arregló. Toda la esperanza de detección
> temprana en el modelo B está, por tanto, en la telemetría del puesto y no en
> el usuario, y eso vuelve a `H-1`, `H-2` y la brecha de macOS de `T-5`.

## X-2. Artefactos de host persistentes

<!-- cti:cards -->

| Categoría | Artefactos | Etiqueta |
|---|---|---|
| **Historial del diálogo *Ejecutar* de Windows** | `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU` — **conserva en texto lo que la víctima pegó**, por usuario, y sobrevive al reinicio | `el artefacto más valioso del informe` |
| **Relación padre-hijo anómala** | Navegador o `explorer.exe` → `powershell.exe`, `pwsh.exe`, `cmd.exe`, `mshta.exe`, `curl.exe`, `bitsadmin.exe`, `wscript.exe` | `el gesto, en telemetría` |
| **macOS** | Invocación de `osascript` desde navegador o terminal; `/bin/sh -c` con `curl` encadenado; historial del intérprete (`.zsh_history`, `.bash_history`) | `la brecha más probable` |
| **Argumentos característicos de PowerShell** | `-w hidden` · `-enc` · `-EncodedCommand` · `FromBase64String` · `iex` / `IEX` · `Invoke-Expression` · `irm` · `Invoke-RestMethod` · `DownloadString` | `caducan poco: son la gramática del método` |
| **Precursores de destrucción (modelo A)** | Manejadores de escritura a `\\.\PhysicalDrive*` · `bcdedit` · `bootcfg` · `vssadmin delete shadows` · `wbadmin delete` · `wmic shadowcopy delete` | `la única alerta previa al impacto` |
| **Modelo C** | Herramienta de control remoto instalada en los primeros días de alta · acceso desde proxy residencial o VPN comercial · discrepancia de geolocalización · currículos con huella compartida | `no son artefactos de malware` |
| **Lo que NO hay aquí** | **Hashes y dominios de la campaña vigente.** Están en la fuente, en un anexo no extraíble | `ir a la fuente` |

## X-3. Lógica de detección prioritaria

<!-- cti:detections -->

**D-1 · CRÍTICO — Ejecución manual inducida desde el navegador (el patrón *ClickFix*)**

```
// Windows — rama 1: relacion padre-hijo
(process.parent.name IN ("chrome.exe","msedge.exe","firefox.exe","brave.exe",
                         "explorer.exe","Teams.exe","Zoom.exe")
 AND process.name IN ("powershell.exe","pwsh.exe","cmd.exe","mshta.exe",
                      "wscript.exe","cscript.exe","curl.exe","bitsadmin.exe",
                      "certutil.exe","regsvr32.exe"))
// Windows — rama 2: la gramatica del metodo, con independencia del padre
OR (process.name IN ("powershell.exe","pwsh.exe")
    AND process.command_line CONTAINS_ANY ("-w hidden","-windowstyle hidden",
          "-enc","-EncodedCommand","FromBase64String","iex ","IEX(",
          "Invoke-Expression","irm ","Invoke-RestMethod","DownloadString",
          "DownloadFile","| iex","|iex"))
// macOS
OR (process.name == "osascript"
    AND process.parent.name IN ("Google Chrome","Safari","firefox","Terminal",
                                "zoom.us","Microsoft Teams"))
OR (process.command_line MATCHES "curl .*\\| ?(ba)?sh"
    OR process.command_line MATCHES "curl .*\\| ?osascript")
```

→ **Aislamiento del puesto y contacto telefónico con el usuario, no por correo ni por chat.** Es la detección de mayor valor y mayor vida útil del informe: ataca el único paso que seis meses de evolución del adversario no cambiaron. **Contención automática recomendada para la rama 1 en puestos de dirección**, previa lista blanca de los portales corporativos que legítimamente lanzan un script. La rama 2 genera más ruido en entornos con administración por PowerShell y conviene arrancarla en modo alerta.

**D-2 · CRÍTICO — Entrada sospechosa en el historial del diálogo *Ejecutar* de Windows**

```
registry.path MATCHES
  "HKU\\\\.*\\\\Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Explorer\\\\RunMRU"
AND registry.value CONTAINS_ANY ("powershell","pwsh","cmd /c","mshta","curl",
      "bitsadmin","certutil","iex","IEX","-enc","FromBase64String","http://",
      "https://","\\\\\\\\")
```

→ **Alerta crítica e investigación.** La víctima de este patrón pega la línea en ese diálogo, y Windows la guarda en texto. **Es evidencia, no inferencia.** Falso positivo acotado a administradores de sistemas, que se enumeran nominalmente. Donde el EDR no vigile el registro en tiempo real, esta misma consulta sirve como barrido periódico — y es `H-1`.

**D-3 · ALTO — Descarga y ejecución desde un sitio de «actualización» de navegador**

```
(dns.question.name MATCHES "(?i)(chrome|edge|firefox|adobe|acrobat|zoom|teams).*(update|updater|install|viewer|player|fix|verify)"
 AND NOT dns.question.name IN <dominios legitimos de los fabricantes>)
OR (process.parent.name IN ("chrome.exe","msedge.exe","Google Chrome","Safari")
    AND file.created.extension IN ("exe","msi","dmg","pkg","scpt","sh","ps1")
    AND file.origin.zone == "Internet"
    FOLLOWED BY (SAME file) process.start WITHIN 10m)
```

→ **Bloqueo en el proxy para la primera rama; alerta alta y recogida para la segunda.** El señuelo del visor de PDF de Chrome y el del reproductor de medios caen aquí. **La lista blanca de dominios legítimos de actualización hay que construirla antes de armar la regla**, y conviene que la mantenga Arquitectura y no el SOC.

**D-4 · CRÍTICO — Preparación de destrucción de estructuras de disco (modelo A)**

```
(file.handle.target MATCHES "\\\\\\\\\\.\\\\(PhysicalDrive|Harddisk)[0-9]+"
 AND file.handle.access CONTAINS "WRITE"
 AND NOT process.name IN <lista blanca nominal: copia, clonado, cifrado de disco>)
OR process.command_line CONTAINS_ANY ("vssadmin delete shadows",
      "wbadmin delete","wmic shadowcopy delete","bcdedit /set","bootcfg /raw",
      "fsutil usn deletejournal")
```

→ **Contención automática, sin escalado humano, y el fundamento es el expediente de 2018.** De todas las detecciones de este informe, ésta es la que protege el activo de mayor valor —nueve mil puestos y la capacidad de operar— y la que tiene menos tiempo de reacción. La lista blanca es corta y conocida. **Si esta regla no se puede armar con contención automática por política interna, eso es en sí mismo un hallazgo para `E-c`.**

**D-5 · ALTO — Cambio en el entorno de originación de mensajería de pagos**

```
host.name IN <conjunto de puestos y servidores de pagos de A-1>
AND (
  (event.action == "process_create" AND process.hash NOT IN <linea base aprobada>)
  OR event.code IN (4720, 4722, 4728, 4732, 4756)   // cuentas y grupos
  OR (event.code == 4624 AND logon.type IN (2,10)
      AND user.name NOT IN <lista aprobada de operadores>)
  OR (event.action == "file_modify" AND file.path IN <plantillas y configuracion de mensajeria>)
)
```

→ **Alerta crítica y verificación telefónica con el equipo de pagos.** La premisa es que ese entorno **debe ser inmutable** entre ventanas de cambio. Si la regla hace ruido, el ruido es el hallazgo y la conversación corresponde a Riesgo Operacional. Es `H-9`.

**D-6 · ALTO — Sesión autenticada en uso concurrente**

```
// del lado de la aplicacion, no del puesto
session.id APPEARS WITH distinct(source.ip) > 1 WITHIN 15m
AND source.ip.geo.country COUNT distinct > 1
AND user.name IN <lista B-1: autoridad sobre fondos o claves de firma>
```

→ **Invalidación inmediata de la sesión y reautenticación fuera de banda.** Es la única detección que ataca el robo de sesión, que es lo que elude el segundo factor sin atacarlo. **Para los nombres de `B-1` debería estar permanentemente activa y con umbral bajo**, aunque genere alguna molestia: es la lista de personas cuyo acceso vale cientos de millones.

**D-7 · MEDIO — Control remoto instalado en un equipo de personal remoto recién incorporado**

```
process.name IN ("AnyDesk.exe","TeamViewer.exe","rustdesk.exe","ScreenConnect*",
                 "remotepc*","chrome_remote_desktop*","splashtop*","Atera*")
AND host.owner.hire_date WITHIN 30d
AND NOT process.installed_by IN <equipo de soporte propio>
```

→ **Alerta media a RR. HH. y a Seguridad conjuntamente.** No es una detección de malware: es un control de la hipótesis de `O-3.C`. Requiere que el dato de fecha de alta esté accesible, que es la brecha de `T-5`.

**D-8 · MEDIO — Ejecución de código de un repositorio externo por perfil técnico**

```
process.name IN ("node.exe","python.exe","npm.cmd","yarn.cmd","pip.exe","node","python3")
AND process.working_directory MATCHES "(?i)\\\\(Downloads|Desktop|Temp)\\\\"
AND user.department IN ("Ingenieria","Desarrollo","Datos")
AND NOT process.working_directory IN <repositorios corporativos aprobados>
```

→ **Alerta media y conversación con la persona.** Cubre la cara ofensiva del modelo C. Generará falsos positivos legítimos, y cada uno de ellos es una oportunidad de establecer la política que `C-6` pregunta si existe.

> ⚠ **Regla de operación.** Dos detecciones de este informe deben ejecutar
> **contención automática sin escalado humano**, y por razones opuestas: `D-4`
> porque el tiempo de reacción es de minutos y el daño es irreversible, y `D-1`
> rama 1 **en puestos de dirección** porque el usuario afectado no va a
> reportar nada —el diálogo de éxito falso de `X-1` se encarga de eso—. Las
> demás son de alerta. Y una prohibición expresa: **no ingerir los indicadores
> de red de la campaña Web3 en los controles del entorno de pagos**. Son
> universos disjuntos, el ruido resultante desacredita el programa de
> inteligencia ante el equipo que más lo necesita, y es la decisión `E-f`.

## X-4. Consultas de caza

```kql
// H-2 y D-1 · El gesto, en telemetria de creacion de proceso.
// La consulta central del informe. Vida util larga: no contiene ningun IOC.
let navegadores = dynamic(["chrome.exe","msedge.exe","firefox.exe","brave.exe",
                           "explorer.exe","Teams.exe","Zoom.exe","Outlook.exe"]);
let interpretes = dynamic(["powershell.exe","pwsh.exe","cmd.exe","mshta.exe",
                           "wscript.exe","cscript.exe","curl.exe","bitsadmin.exe",
                           "certutil.exe","regsvr32.exe"]);
DeviceProcessEvents
| where Timestamp > ago(180d)
| where InitiatingProcessFileName in~ (navegadores)
| where FileName in~ (interpretes)
| project Timestamp, DeviceName, AccountName, FileName, ProcessCommandLine,
          InitiatingProcessFileName, InitiatingProcessCommandLine
| order by Timestamp desc
```

```kql
// H-1 y D-2 · Historial del dialogo Ejecutar. Evidencia en texto de lo que
// la victima pego. Es la caza de mejor fidelidad y menor coste del informe.
DeviceRegistryEvents
| where Timestamp > ago(365d)
| where RegistryKey has @"\Explorer\RunMRU"
| where RegistryValueData has_any ("powershell","pwsh","cmd /c","mshta","curl",
        "bitsadmin","certutil","iex","IEX","-enc","FromBase64String","http")
| project Timestamp, DeviceName, RegistryValueName, RegistryValueData,
          InitiatingProcessAccountName
| order by Timestamp desc
```

```kql
// H-2 (macOS) · La brecha mas probable de este expediente.
// El flujo recuperado por la fuente para el senuelo del visor de PDF es macOS.
DeviceProcessEvents
| where Timestamp > ago(180d)
| where DeviceType == "Mac" or InitiatingProcessFileName in~ ("Google Chrome","Safari","zoom.us")
| where FileName in~ ("osascript","curl","sh","bash","zsh")
| where ProcessCommandLine has_any ("curl","osascript","| sh","|sh","| bash","|bash",
                                    "do shell script")
| project Timestamp, DeviceName, AccountName, FileName, ProcessCommandLine,
          InitiatingProcessFileName
| order by Timestamp desc
```

```kql
// H-3 y D-4 · Precursores de destruccion de estructuras de disco (modelo A).
// Lo unico que puede sonar antes de perder nueve mil puestos.
union
( DeviceProcessEvents
  | where Timestamp > ago(365d)
  | where ProcessCommandLine has_any ("vssadmin delete shadows","wbadmin delete",
          "shadowcopy delete","bcdedit /set","bootcfg /raw","usn deletejournal")
  | project Timestamp, DeviceName, AccountName, Senal = "comando", ProcessCommandLine
),
( DeviceFileEvents
  | where Timestamp > ago(365d)
  | where FolderPath has_any (@"\\.\PhysicalDrive", @"\\.\Harddisk")
  | where not(InitiatingProcessFileName in~ ("veeam.exe","acronis.exe","BitLockerWizard.exe"))
  | project Timestamp, DeviceName, AccountName = InitiatingProcessAccountName,
            Senal = "disco crudo", ProcessCommandLine = InitiatingProcessCommandLine
)
| order by Timestamp desc
```

```kql
// H-9 y D-5 · Inmutabilidad del entorno de pagos.
// Si esta consulta devuelve ruido, el ruido ES el hallazgo.
let pagos = dynamic(["<host-pagos-01>","<host-pagos-02>","<srv-mensajeria-01>"]);
DeviceProcessEvents
| where Timestamp > ago(90d)
| where DeviceName in~ (pagos)
| summarize Ejecuciones = count(), Primero = min(Timestamp), Ultimo = max(Timestamp)
         by DeviceName, FileName, SHA256, AccountName
| order by Primero desc
// Revisar manualmente: cualquier SHA256 que no este en la linea base aprobada.
```

```sql
-- H-7 · Discrepancia entre geolocalizacion efectiva y residencia declarada
-- del personal remoto. No es una consulta de seguridad: es un cruce con RR. HH.,
-- y por eso es la que no se hace.
SELECT e.empleado_id, e.pais_declarado, a.pais_observado,
       COUNT(*) AS accesos, MIN(a.fecha) AS desde, MAX(a.fecha) AS hasta
FROM accesos a
JOIN empleados e ON e.empleado_id = a.empleado_id
WHERE e.modalidad = 'remoto'
  AND e.perfil IN ('desarrollo','datos','infraestructura')
  AND a.pais_observado <> e.pais_declarado
  AND a.fecha > CURRENT_DATE - INTERVAL '365' DAY
GROUP BY e.empleado_id, e.pais_declarado, a.pais_observado
HAVING COUNT(*) > 5
ORDER BY accesos DESC;
```

```yaml
# Sigma — Interprete lanzado por el navegador (patron de inducción a ejecutar)
title: Navegador o explorador lanza un interprete de comandos
id: 4c8e1b73-2fa6-4e59-91d0-7b3c5a2e6d41
status: stable
description: >
  Detecta el paso invariante del modelo de ingenieria social de BlueNoroff en
  2026: una pagina de aspecto confiable induce a la persona a ejecutar un
  comando. Seis meses de evolucion del actor cambiaron las senales visibles y
  no este mecanismo. Aplicable a cualquier actor que use el patron ClickFix.
author: Celula CTI
date: 2026-11-17
references:
  - https://arcticwolf.com/resources/blog/still-in-the-meeting-bluenoroff-six-months-on/
tags:
  - attack.execution
  - attack.t1204.004
  - attack.t1059.001
logsource:
  category: process_creation
  product: windows
detection:
  padre:
    ParentImage|endswith:
      - '\chrome.exe'
      - '\msedge.exe'
      - '\firefox.exe'
      - '\brave.exe'
      - '\explorer.exe'
      - '\Teams.exe'
      - '\Zoom.exe'
  hijo:
    Image|endswith:
      - '\powershell.exe'
      - '\pwsh.exe'
      - '\cmd.exe'
      - '\mshta.exe'
      - '\wscript.exe'
      - '\cscript.exe'
      - '\curl.exe'
      - '\bitsadmin.exe'
      - '\certutil.exe'
  filtro_portales:
    ParentCommandLine|contains: '<portal corporativo que lanza scripts>'
  condition: padre and hijo and not filtro_portales
falsepositives:
  - Portales corporativos que lanzan scripts legitimos: enumerarlos antes de
    armar la regla
  - Administradores que abren una consola desde el explorador
level: critical
```

```yaml
# Sigma — Entrada sospechosa en el historial del dialogo Ejecutar
title: Comando de descarga o ejecucion en RunMRU
id: 9a2f5d61-8c07-4b3e-a254-6e1f90cb73d8
status: stable
description: >
  RunMRU conserva en texto lo que el usuario escribio o pego en el dialogo
  Ejecutar de Windows. El patron ClickFix depende de ese gesto, de modo que la
  clave contiene evidencia directa y no inferencia. Sobrevive al reinicio.
author: Celula CTI
date: 2026-11-17
tags:
  - attack.execution
  - attack.t1204.004
logsource:
  category: registry_set
  product: windows
detection:
  clave:
    TargetObject|contains: '\Explorer\RunMRU'
  sospechoso:
    Details|contains:
      - 'powershell'
      - 'pwsh'
      - 'cmd /c'
      - 'mshta'
      - 'curl'
      - 'bitsadmin'
      - 'certutil'
      - 'iex'
      - '-enc'
      - 'FromBase64String'
      - 'http'
  condition: clave and sospechoso
falsepositives:
  - Administradores de sistemas: enumerar nominalmente
level: critical
```

```yaml
# Sigma — Preparacion de destruccion de estructuras de disco
title: Escritura en disco crudo o destruccion de copias de seguridad
id: 6b0d3e94-5a71-4c28-8f63-2d94ae01b5c7
status: stable
description: >
  Precursor del componente destructivo del modelo APT38, usado en 2018 como
  senuelo de un fraude de pagos y no como objetivo. Es la unica alerta posible
  antes del impacto, y el margen de reaccion se mide en minutos.
author: Celula CTI
date: 2026-11-17
tags:
  - attack.impact
  - attack.t1561.002
  - attack.t1490
logsource:
  category: process_creation
  product: windows
detection:
  comandos:
    CommandLine|contains:
      - 'vssadmin delete shadows'
      - 'wbadmin delete'
      - 'shadowcopy delete'
      - 'bcdedit /set'
      - 'bootcfg /raw'
      - 'usn deletejournal'
  filtro:
    Image|endswith:
      - '\veeam.exe'
      - '\acronis.exe'
  condition: comandos and not filtro
falsepositives:
  - Herramientas de copia de seguridad, clonado y cifrado de disco: lista
    nominal corta y conocida
level: critical
```

## X-5. Mitigaciones de configuración con efecto directo

| Control | Corta |
|---|---|
| **Desactivar el diálogo *Ejecutar* por política en los puestos de dirección** (`NoRun` en la directiva del explorador) | **La etapa 02 del modelo B en Windows, por completo.** Es el control más barato y más desproporcionadamente eficaz del informe: elimina el mecanismo, no el indicador. Y los directivos no usan ese diálogo |
| Impedir que el navegador y el explorador lancen intérpretes, por regla de reducción de superficie o WDAC | La misma etapa, por la otra vía, y de forma menos quirúrgica |
| **En macOS: restringir `osascript` y la ejecución de comandos pegados en el terminal para puestos de dirección**, por perfil de MDM | **La variante de macOS, que es la que la fuente recuperó.** Es el control que falta con más frecuencia porque el parque de dirección es macOS y el EDR suele ser de Windows |
| Bloqueo en el proxy de dominios de «actualización» de navegador no pertenecientes a los fabricantes | La etapa de entrega de `D-3`. Exige lista blanca previa, mantenida por Arquitectura |
| **Control de doble persona efectivo para firmar transacciones**, con la condición de que un administrador de sistemas no pueda eludirlo | **El objetivo del modelo B y del A a la vez.** Si una sola persona puede mover fondos, su puesto es el perímetro |
| Vinculación de sesión a dispositivo y vida corta de sesión en aplicaciones financieras | El robo de sesión, que elude el segundo factor sin atacarlo |
| **Segmentación y línea base de ejecutables del entorno de pagos**, con registro diferenciado | La etapa 02 del modelo A, y es la condición para que `D-5` exista |
| **Copias de seguridad inmutables y fuera de línea del registro de mensajería emitida** | La etapa 03 del modelo A: permite saber **qué salió** aunque el parque esté destruido, que es la única información que importa en las primeras horas |
| Protección del sector de arranque y denegación de escritura en disco crudo en servidores | El impacto del modelo A |
| **Verificación de identidad en contratación remota, y entrega de portátil con comprobación de domicilio** | El modelo C. No es un control técnico y por eso no tiene dueño en el organigrama de seguridad |
| Prohibición explícita de ejecutar pruebas técnicas de terceros en equipo corporativo | La cara ofensiva del modelo C |
| **Retirada de la formación que enseña a detectar vídeo sintético por su aspecto** | Es una mitigación aunque sea una supresión: la fuente declara que los vídeos ya no se distinguen visualmente, de modo que esa formación entrena una confianza que el adversario ya ha derrotado |

---

## 14. Brechas de inteligencia y nuevos requisitos de colección

| # | Brecha | Impacto en el juicio | Requisito propuesto | Prioridad |
|---|---|---|---|---|
| G-1 | **Ninguna evidencia pública de actividad regional en 2026**, y una afirmación concreta del requisito —cooperativas de la SEPS en Ecuador— que no se verifica | `KJ-3` queda en confianza moderada y por ausencia de evidencia, que es el tipo de juicio más frágil que existe | Consulta formal a los CSIRT nacionales de Chile, Perú, Colombia y Ecuador, y a los supervisores financieros, sobre notificaciones compatibles con cualquiera de los tres modelos | **Crítica** |
| G-2 | **El anexo de indicadores de la fuente primaria no es extraíble** (maquetado como imagen) | El Anexo A de este informe no contiene los 98 dominios ni los hashes. **Un retrohunt contra lo que hay aquí no es un retrohunt contra la campaña** | Obtener el documento por vía de cliente, o solicitar al autor una versión en texto o un paquete STIX. Es la petición más rentable de esta tabla | **Crítica** |
| G-3 | **Las cifras de robo de criptoactivos no son auditables** y difieren entre proveedores | `KJ-6` se sostiene en tendencia y no en cifra, y así está escrito | Usar siempre dos proveedores y declarar la divergencia. No citar una cifra única sin su fuente y su fecha | Media |
| G-4 | **El informe de abril de 2026 de la fuente primaria no se leyó en original** | El detalle del modelo B anterior a noviembre se cita a través del resumen que hace de él el informe posterior | Recuperar el original. Contiene el flujo de la reunión falsa y la grabación de cámara web, que son `T1125` | Media |
| G-5 | **Sin visibilidad de si alguien de la organización está en la lista de los 677** | No se puede priorizar `E-e` por nombres, sólo por cargo | `H-11`: preguntar si se es cliente de la fuente; si no, inventariar la exposición pública en vídeo de la dirección | Alta |
| G-6 | **No hay telemetría propia, y en particular es dudoso que haya telemetría de macOS** | `O-4` sin evaluar, y la plataforma donde la fuente recuperó el flujo es precisamente la que probablemente no vigilamos | Ejecutar `H-1` —que no necesita EDR, sólo leer una clave de registro— y auditar la cobertura de EDR por sistema operativo | **Crítica** |
| G-7 | **Sin datos de permanencia de ninguno de los dos modelos** | `T-1.A` y `T-1.B` van sin franja de permanencia. La ventana de retrohunt de 180 días es convención, no dato | Para el modelo A, medir lo propio: cuánto tardamos en poder pedir el retroceso de una transferencia con el parque caído (`A-4`). **Ese número sí lo podemos obtener nosotros** | Alta |
| G-8 | **No hay material de señuelo en español documentado** | No se puede evaluar si la región es objetivo de la campaña vigente o sólo periferia de ella | `I-6`: vigilancia específica de señuelos en español con las convenciones del clúster | Media |

---

# ANEXOS

## Anexo A — Indicadores de compromiso

> ⚠ **Leer antes de usar. Este Anexo A es, a propósito, el más corto de la
> cartera, y conviene explicar por qué.**
>
> **Primero, lo que no contiene.** No contiene los **98 dominios** de la
> campaña vigente, ni sus hashes, ni sus reglas YARA. Existen, los publica la
> fuente primaria, y su anexo **está maquetado como imagen dentro del PDF**: se
> intentó la extracción y no fue posible. Reescribirlos a mano desde una
> captura de pantalla introduciría errores de transcripción en indicadores
> destinados a controles automáticos, y esta cartera ya ha documentado lo que
> eso provoca. **La fuente preferente es el anexo del informe original.** Es la
> brecha `G-2`.
>
> **Segundo, lo que sí contiene, y por qué basta para empezar.** Artefactos de
> comportamiento y patrones de línea de comandos. Son lo que `T-3` identifica
> como el nivel rentable de este expediente: no caducan con la infraestructura,
> y 73 de los 98 dominios de noviembre no existían en abril.
>
> **Tercero, la prohibición expresa.** Los indicadores de la campaña contra
> personas y activos digitales **no se ingieren en los controles del entorno de
> pagos**. Son universos disjuntos (`KJ-1`), y el ruido resultante desacredita
> el programa de inteligencia ante el equipo que más lo necesita. Es la
> decisión `E-f`.
>
> **Cuarto, sobre el incidente de 2018.** No se publican indicadores de él.
> Tienen ocho años, la infraestructura no existe, y el valor de ese expediente
> **no está en sus indicadores sino en su estructura**: es una hipótesis de
> plan de respuesta, y está en `E-c` y en `D-4`.

### A.1 — Artefactos del gesto · **el nivel que no caduca**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| clave | `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU` | **El artefacto más valioso del informe.** Guarda en texto, por usuario, lo que se escribió o pegó en el diálogo *Ejecutar* de Windows. El patrón de inducción a ejecutar depende de ese gesto, de modo que la clave contiene **evidencia directa, no inferencia**. Sobrevive al reinicio y dura lo que dure el perfil | Alta | **Sin caducidad** | **Detección y caza** (`D-2`, `H-1`) |
| pattern | `navegador → powershell.exe` · `navegador → pwsh.exe` · `navegador → cmd.exe` · `navegador → mshta.exe` · `navegador → curl.exe` · `navegador → bitsadmin.exe` · `navegador → certutil.exe` · `explorer.exe → ídem` | **Relación padre-hijo que materializa el paso invariante.** Independiente de la marca del señuelo, del dominio y de la familia de malware | Alta | **Sin caducidad** | **Detección** (`D-1`) |
| pattern | `-w hidden` · `-windowstyle hidden` · `-enc` · `-EncodedCommand` · `FromBase64String` · `iex` · `IEX(` · `Invoke-Expression` · `irm` · `Invoke-RestMethod` · `DownloadString` · `DownloadFile` · `\| iex` | **La gramática del método en Windows.** No son indicadores de este actor: son los argumentos que hacen falta para que el gesto funcione. Por eso duran | Alta | **Sin caducidad** | **Detección** (`D-1` rama 2) |
| pattern | `osascript` lanzado por navegador o terminal · `curl … \| sh` · `curl … \| bash` · `curl … \| osascript` · `do shell script` | **La variante de macOS, que es la que la fuente recuperó.** El señuelo del visor de PDF de Chrome **inicia una descarga por AppleScript**. Es la brecha de visibilidad más probable del expediente | Alta | **Sin caducidad** | **Detección** (`D-1`, `H-2`) |
| path | `~/.zsh_history` · `~/.bash_history` | Historial del intérprete en macOS y Linux: el equivalente funcional de `RunMRU` cuando el comando se pegó en un terminal | Alta | Sin caducidad | Caza y análisis forense |
| artefacto | Diálogo de **«actualización completada»** con marca de Chrome tras la ejecución | **No es un indicador técnico: es la razón por la que la víctima no reporta nada.** Se consigna porque explica por qué la detección temprana del modelo B no puede depender del usuario | Alta | Sin caducidad | Insumo de formación (`E-e`) |

### A.2 — Precursores de destrucción · **modelo de pagos**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| pattern | `\\.\PhysicalDrive*` · `\\.\Harddisk*` con acceso de **escritura** | **Apertura de manejador para escribir en estructuras de disco en crudo.** La lista de procesos con uso legítimo es corta y conocida: copia de seguridad, clonado y cifrado de disco | Alta | **Sin caducidad** | **Detección con contención automática** (`D-4`) |
| pattern | `vssadmin delete shadows` · `wbadmin delete` · `wmic shadowcopy delete` · `bcdedit /set` · `bootcfg /raw` · `fsutil usn deletejournal` | **Eliminación de la capacidad de recuperación y manipulación del arranque.** Precursores habituales de un impacto destructivo | Alta | **Sin caducidad** | **Detección con contención automática** (`D-4`) |
| herramienta | Familia `HERMES` | **Familia del borrador usado en el incidente del Banco de Chile en 2018**, desplegado como señuelo. Se consigna por su valor histórico y de modelo, **no como indicador vigente** | Media | Caducado como indicador | Contexto histórico |
| artefacto | Guion de instalador `NSIS` compartido con código de `Buhtrap` **filtrado en febrero de 2018** | **No es un indicador: es el motivo por el que la atribución de ese incidente tiene confianza moderada y no alta.** Un eje de atribución basado en identidad de código es débil cuando el código estaba público | Alta | Sin caducidad | **Calibración de la atribución** (`O-2`, `H7`) |
| artefacto | Despliegue simultáneo de un ejecutable nuevo a un número elevado de equipos por GPO, PsExec o agente de gestión | Mecanismo de distribución del componente destructivo. **Tiene uso legítimo**: es el patrón de cualquier despliegue de software | Media | Sin caducidad | Caza con contraste de ventana de cambio (`H-3`) |

### A.3 — Señales del modelo de contratación · **no son indicadores de compromiso**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| artefacto | Herramienta de control remoto de terceros instalada en los **primeros 30 días** desde el alta de un empleado remoto, no por el equipo de soporte propio | **El patrón del facilitador**: el portátil corporativo se queda en un domicilio y el acceso llega por encima. Figura aquí como señal de proceso, no de intrusión | Media | Sin caducidad | **Alerta conjunta a RR. HH. y Seguridad** (`D-7`) |
| artefacto | Discrepancia entre geolocalización efectiva del dispositivo o del acceso y residencia declarada | Señal central del modelo. **Cada falso positivo es una conversación, y la conversación es el control** | Media | Sin caducidad | Cruce con RR. HH. (`H-7`) |
| artefacto | Acceso a sistemas corporativos desde proxy residencial o VPN comercial con cuenta de empleado | Ocultación del origen real del trabajador | Media | Sin caducidad | Caza (`H-7`) |
| artefacto | Currículos de candidatos distintos con huella documental compartida; entrevistas donde la cámara falla de forma sistemática; dirección de entrega del equipo distinta de la residencia declarada | Señales de proceso de selección. **Las mira RR. HH. o no las mira nadie** | Media | Sin caducidad | Control de contratación (`E-d`) |
| pattern | `node` · `python` · `npm` · `yarn` · `pip` con directorio de trabajo bajo `Downloads`, `Desktop` o `Temp`, en equipo de perfil técnico | **La cara ofensiva del modelo:** la prueba técnica maliciosa del proceso de selección falso | Media | Sin caducidad | Detección con contexto (`D-8`, `H-8`) |

### A.4 — Indicadores de la campaña vigente · **remisión a la fuente**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| artefacto | **98 dominios de alta confianza, 73 de ellos no reportados previamente** | **No se reproducen aquí.** Están en el anexo del informe de Arctic Wolf Labs del 12 de noviembre de 2026, maquetado como imagen y por tanto no transcribible sin riesgo de error. **El dato utilizable sin la lista es la proporción:** 73 de 98 eran nuevos respecto a siete meses antes, lo que establece el ritmo de renovación de la infraestructura y descalifica cualquier programa basado en esta capa | Alta como hecho; la lista no está aquí | La lista caduca rápido; **la proporción no** | **Ir a la fuente.** Retrohunt allí, registrando la limitación de `H-10` |
| artefacto | Reglas **YARA** y mapeo **ATT&CK** de la fuente primaria | Publicados en el mismo anexo no extraíble. El mapeo ATT&CK de `T-2` de este informe es **propio** y así está declarado fila por fila | Alta | — | **Ir a la fuente** |
| artefacto | `NovaStream` | **Nombre de un señuelo concreto** —un reproductor de medios fabricado— que la fuente rastreó desde su fase de producción. Se consigna por su valor de método, no de indicador: **la marca del señuelo es lo que el adversario renueva sin coste** | Alta | Caduca de inmediato | Contexto; **no construir detección sobre nombres de señuelo** |
| servicio | Servicios comerciales de generación de imagen y vídeo empleados en la cadena de producción del actor | **Servicios legítimos y de uso masivo.** Se declaran con tipo `servicio` para que **no entren en los agregados planos** de este repositorio. No son bloqueables ni deben tratarse como IOC: son el insumo de `E-e` | Alta | Sin caducidad | **Ninguna acción técnica** |
| servicio | Plataformas de videoconferencia y profesionales suplantadas en los señuelos | Legítimas. El indicador no es la plataforma: es el gesto que se pide dentro de ella | Alta | Sin caducidad | **Ninguna acción técnica** |

## Anexo B — Fuentes y valoración

> Valoración doble tipo Admiralty/OTAN: **fiabilidad de la fuente (A–F)** ×
> **credibilidad de la información (1–6)**. Se valoran por separado.

| Fuente | Disciplina | Fiabilidad | Credibilidad | Notas de sesgo |
|---|---|---|---|---|
| **Arctic Wolf Labs, «Still in the Meeting: BlueNoroff Six Months On», 12-11-2026**, y su documento completo en PDF, marcado «Classification: Public» por su autor — ambos leídos en original | OSINT comercial · TECHINT de primera mano, **con acceso sostenido a la infraestructura del actor** | **B** | **2** | **Fuente principal.** Seis meses de seguimiento con acceso a la biblioteca de material del adversario: es una base de colección poco común y mucho más fuerte que la observación de víctimas. **Advierte expresamente** que sus cuentas describen objetivos preparados y no compromisos confirmados, y publica descargo de que la atribución es juicio analítico y no hecho jurídico. Sesgos: interés comercial; **anexo de indicadores maquetado como imagen**, lo que impide la verificación y la ingesta |
| **Arctic Wolf Labs, informe de abril de 2026 sobre la misma campaña** | OSINT comercial · TECHINT | **B** | **3** | **No leído en original**: la dirección publicada devolvió error. Se cita **a través del resumen que hace de él el informe de noviembre**, y la credibilidad se degrada en consecuencia |
| **Acusación federal del Distrito Norte de Ohio, 01-10-2026**, y la operación «Lonestar Roundup» | Fuente judicial · gubernamental | **A** | **2** | Documento oficial. **Son imputaciones, no condenas**, y así se cita. Varios medios reproducen las mismas cifras, lo que permite corroborar la lectura |
| **FireEye / Mandiant, informe APT38, 2018** | OSINT comercial · TECHINT | **B** | **3** | Fuente de la atribución del incidente chileno. El propio expediente declara que la atribución a «Lazarus» y a TEMP.Hermit se hizo **con confianza variable** y apoyada principalmente en malware compartido, lo que es honesto y es la razón de la confianza moderada de `KJ-4` |
| **Cobertura periodística del incidente del Banco de Chile, junio de 2018** | OSINT · prensa especializada | **C** | **3** | Fuente de las cifras del incidente —9.000 puestos, 500 servidores, cuatro transferencias, 10 M USD, Hong Kong—, que incluyen declaraciones del propio banco. La misma cobertura recoge que **la atribución seguía siendo incierta** y señala la coincidencia del instalador con Buhtrap |
| **TRM Labs y Chainalysis, estimaciones de robo de criptoactivos** | OSINT comercial · analítica de cadena | **C** | **4** | **No auditables desde fuera y divergentes entre sí.** Se usan como orden de magnitud y tendencia, nunca como dato. Es la limitación `3.3.3` y la brecha `G-3` |
| **Comunicación de la plataforma afectada sobre el incidente de KelpDAO, abril de 2026** | Declaración de parte | **D** | **4** | **Atribución declarada como preliminar por quien la hizo**, y recogida así. Las cifras de activos y de congelación proceden de la misma parte interesada |
| **Perfil de BlueNoroff de Securelist (Kaspersky)** | OSINT comercial · perfil de actor | **B** | **4** | Fuente de la mención histórica de **Perú** entre los países más atacados. **Tiene del orden de cuatro años**, y se cita con esa antigüedad declarada. **No se usa para priorizar nada**, sólo para completar el expediente regional |
| **Cobertura secundaria y agregadores sobre robos atribuidos en 2026** | OSINT comercial · agregada | **E** | **5** | Fuentes que listan golpes atribuidos sin informe primario detrás. **No se usa ninguna de sus cifras.** Se consignan en el Anexo B porque forman parte de lo que se leyó y se descartó |

### Anexo B.1 — Un anexo de indicadores que no se puede usar, y qué significa eso

El documento completo de la fuente principal es público —su propio pie lo marca «Classification: Public»— y su cuerpo se lee sin dificultad. **Su anexo de indicadores, en cambio, está maquetado como imagen**: las tablas de dominios, los hashes, las reglas YARA y el mapeo ATT&CK no existen como texto dentro del fichero. Se intentó la extracción con tres métodos distintos, incluida la reconstrucción de los mapas de codificación de las fuentes tipográficas del documento, y el resultado fue el mismo: el cuerpo se recupera, el anexo no.

**Por qué no se transcriben a mano.** Porque un dominio o un hash transcrito desde una captura de pantalla va a un control automático, y un carácter mal leído produce dos daños a la vez: un indicador que no detecta nada y una entrada que nadie volverá a verificar. Esta cartera documentó en `CTI-2026-031` un caso real de hash que circula truncado en cobertura secundaria, y en `CTI-2026-030` uno de cadena de búsqueda publicada con una letra de menos en el propio aviso oficial. **El modo correcto de usar una lista de indicadores es ingerirla, no copiarla.**

**Qué queda, entonces, y no es poco.** Queda el dato estructural, que es el que de verdad orienta una decisión: **73 de los 98 dominios no se habían reportado antes del informe de noviembre**, siete meses después del anterior. Esa proporción es más útil que la lista, porque no caduca y porque dice algo que la lista no dice: cualquier programa de defensa que descanse en la capa de infraestructura de esta campaña estará permanentemente por detrás, y la fecha de su última actualización marcará su obsolescencia. De ahí que todo el esfuerzo de detección de este informe esté en `T-3`/cima y en `X-3`, y que el Anexo A sea corto sin pedir disculpas.

**Y una petición, que es la brecha `G-2`.** Para quien sea cliente de la fuente, el documento y la lista están disponibles y el retrohunt es inmediato. Para quien no, la petición razonable al autor es un paquete en formato legible por máquina. Es, de todas las carencias de este informe, la más fácil de cerrar y la que más valor liberaría.

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

## Anexo D — Cómo se descompone un alias agregado, y por qué hay que hacerlo antes de gastar un euro

Este anexo no es sobre Corea del Norte. Es el método que estructura el informe, y se escribe aparte porque va a hacer falta otra vez: esta cartera tiene al menos cinco entradas —`G0032`, los bloques por alineación, los paraguas de proveedor— donde un solo nombre cubre comportamientos que exigen defensas distintas.

**El problema, enunciado con precisión.** La industria nombra actores por **origen** —quién está detrás— porque es lo que la atribución produce. Pero la defensa se organiza por **comportamiento** —qué hace y dónde—, porque es lo único sobre lo que se puede poner un control. Mientras esos dos ejes coinciden, el nombre sirve para las dos cosas y nadie nota el problema. Cuando un mismo origen desarrolla varias líneas de actividad, el nombre sigue siendo correcto como atribución y **deja de ser utilizable como unidad de defensa**, sin que nada avise de ello. El síntoma clásico es un informe que recomienda medidas heterogéneas a destinatarios distintos bajo un único titular, y un presupuesto que se asigna al titular.

**Las cinco preguntas que descomponen un alias.** Se aplican a cada expediente público del actor, y la respuesta se tabula:

1. **¿Quién es la víctima: una organización o una persona?** Es el corte más productivo y el que separa aquí el modelo A del B. Determina si el control va en el perímetro o en la formación.
2. **¿Qué se monetiza, y en qué moneda?** Mensajería interbancaria, activos digitales, nómina, rescate, información. Determina quién, dentro de la organización, es el dueño del riesgo.
3. **¿Qué paso del ataque exige intervención humana de la víctima?** Si hay uno, ahí está la detección duradera. Si no hay ninguno, la defensa vuelve a depender de parcheo.
4. **¿Cuál es el mecanismo de salida?** Destrucción, sigilo, persistencia, reutilización del acceso. Determina la forma del plan de respuesta, que es lo que no se puede improvisar.
5. **¿Comparten los expedientes algún indicador técnico?** Si la respuesta es ninguno, **no es un actor a efectos de defensa**, por mucho que lo sea a efectos de atribución.

**La regla que se sigue de todo esto, y que este informe aplica sin excepción:** ninguna medida se recomienda contra un actor. Se recomienda contra un **modelo**, y el modelo tiene un dueño nominal en el organigrama. Un informe que diga «hay que protegerse de X» sin decir contra qué modelo y quién lo ejecuta ha trasladado el trabajo difícil al lector, que es exactamente a quien le falta el contexto para hacerlo.

**Y el fallo que conviene anticipar.** La descomposición tiene un coste político: produce tres conversaciones con tres áreas distintas en lugar de una presentación a un comité. En la práctica, eso significa que la parte del informe que corresponde a un área sin cultura de seguridad —en este caso, Recursos Humanos— es la que no se ejecuta, y la que deja el hueco. **La medida más barata del informe es `E-d` y es la que tiene más probabilidades de no hacerse nunca.** Un anexo de método debería decirlo en lugar de pretender que la descomposición es gratis.

> **Y una nota sobre lo contrario, porque el exceso también cuesta.** Descomponer
> no es multiplicar. Si dos expedientes comparten víctima, monetización, paso
> humano, salida **e** indicadores, son el mismo modelo aunque dos proveedores
> les hayan puesto nombres distintos, y tratarlos por separado duplica trabajo
> sin añadir defensa. El criterio no es la cantidad de nombres: **es si la
> medida cambia**. Si dos nombres llevan a la misma medida, son uno a efectos
> de este anexo.

## Anexo E — Marcos de referencia empleados

`MITRE ATT&CK v18` · `Modelo del Diamante` · `Cyber Kill Chain` · `Pirámide del Dolor` · `F3EAD` · `ICD 203` · `ACH, supuestos clave y pre-mortem` · `TLP 2.0` · `PAP` · `Admiralty Code` · `Sigma` · `Definición de *deepfake* de la GAO de EE. UU.`, adoptada por la fuente primaria y, con ella, por este informe

## Anexo F — Paquete legible por máquina

- Las tablas `cti:ioc` de los Anexos A.1 a A.4 alimentan `ioc_index.csv` en cada construcción. **Son deliberadamente de comportamiento y no de infraestructura**, por el motivo del Anexo B.1.
- **Fuente preferente para ingesta de infraestructura:** el anexo del informe de Arctic Wolf Labs del 12 de noviembre de 2026, en el documento completo. **No disponible como texto**; véase `G-2`.
- **Reglas propias:** tres reglas Sigma en `X-4`, de autoría propia. Las dos primeras —intérprete lanzado por el navegador y entrada sospechosa en `RunMRU`— son las que conviene desplegar primero y **no contienen ningún indicador perecedero**.
- **Consultas propias:** cinco en KQL y una en SQL. La última, el cruce de geolocalización con los datos de RR. HH., no es una consulta de seguridad y por eso está escrita: es la que mide `KJ-7` en casa.

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-11-17 | Emisión inicial. Se descompone el alias agregado en tres modelos operativos con la prueba de indicadores disjuntos (`O-1.2`), se corrigen tres afirmaciones del requisito de origen en `§3.5` —incluida la de las cooperativas reguladas por la SEPS, que no se ha podido corroborar—, se recupera el expediente del Banco de Chile de 2018 como hipótesis de plan de respuesta y no como conjunto de indicadores, y se declara en el Anexo B.1 la imposibilidad de transcribir el anexo de indicadores de la fuente primaria | Célula CTI |

## Anexo H — Realimentación del consumidor

| Pregunta | Respuesta |
|---|---|
| ¿Respondió a su requisito? | |
| ¿Qué decisión tomó o cambió con este informe? | |
| ¿Se dejó de usar «Lazarus» como designación operativa (`E-a`)? | |
| **¿Qué devolvió `H-1`, el volcado del historial del diálogo *Ejecutar*?** | |
| ¿Contempla ya el plan de respuesta la destrucción masiva y el fraude de pagos como un **único** evento (`E-c`)? | |
| ¿Se habló con RR. HH. (`E-d`)? ¿Qué dijeron? | |
| ¿Se retiró la formación que enseña a detectar vídeo falso por su aspecto (`E-e`)? | |
| ¿Llegó a tiempo? | |

> Sin este anexo devuelto, el ciclo de inteligencia queda abierto y el próximo
> producto no mejora. **Dos preguntas de esta tabla valen más que el resto:** la
> de `H-1`, porque convierte el documento en inteligencia propia en una tarde y
> sin comprar nada; y la de RR. HH., porque es la medida más barata del informe
> y la que el Anexo D predice que no se hará.
