---
tlp: "TLP:CLEAR"
pap: "PAP:AMBER"
id: "CTI-2026-033"
version: "1.0"
tipo: "Perfil de clúster sin atribuir + análisis de un cargador diseñado contra los sensores del EDR + evaluación de exposición por aplicaciones expuestas a Internet"
foco_regional: "Colombia confirmada como país con víctima, **y el vector fue un servidor de datos geoespaciales GeoServer sin parchear (CVE-2024-36401)**. La víctima colombiana no es gubernamental ni diplomática: la fuente la sitúa en el grupo de «otras organizaciones», y el informe explica por qué esa precisión cambia la decisión"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "StrikeShark (clúster de intrusión sin atribuir, designación de Kaspersky GReAT) · cargador SharkLoader · carga final Cobalt Strike Beacon"
fecha: "2026-11-17"
caduca: "2027-02-17"
autor: "Célula CTI"
distribucion: "Elaborado íntegramente con fuentes abiertas TLP:CLEAR, con el informe técnico de Kaspersky GReAT publicado en Securelist el 24 de junio de 2026 leído en original, incluidos su anexo de indicadores y sus tablas de ganchos de API. Difusión libre, conservando la atribución de las fuentes y las salvedades metodológicas de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-033

## Un clúster que **nadie ha atribuido**, que llegó a Colombia por un servidor de datos geoespaciales sin parchear, y cuyo cargador es un **catálogo de los sensores en los que confía su EDR**

### SharkLoader ciega el registro de eventos del sistema, construye llamadas directas al núcleo en tiempo de ejecución para saltarse los ganchos del producto de seguridad, **devuelve la memoria del implante a sólo lectura mientras duerme** para que un barrido no la encuentre, y hace que todo lo que lance parezca hijo de `svchost.exe`. No es evasión improvisada: es una enumeración

#### Y la atribución: Kaspersky dice **«hablante de chino, con confianza BAJA»**, apoyada en quién escribió en GitHub tres herramientas públicas. Parte de la cobertura secundaria la publicó como confianza *moderada*. Este informe documenta ese ascenso, porque es el error que esta cartera lleva tres informes corrigiendo

> **Regla de oro del producto:** todo párrafo debe responder a un requisito de
> inteligencia (PIR) y habilitar una decisión. Si un párrafo no cambia lo que
> alguien va a hacer, va al anexo o se borra.

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-033` |
| Versión / fecha | `1.0` — 2026-11-17 (emisión inicial) |
| Tipo de producto | Perfil de **clúster de intrusión sin atribuir** —la fuente no lo asocia a ningún actor conocido—, más **análisis de una cadena de evasión dirigida contra los sensores concretos de un EDR**, más evaluación de exposición por aplicaciones expuestas a Internet, más **documentación de una inflación de confianza en la atribución** |
| Niveles cubiertos | Estratégico · Operacional · Táctico · Técnico |
| Foco regional | **Colombia, con dos precisiones que cambian la decisión.** (a) Hay una víctima colombiana confirmada, y el vector de entrada fue **un GeoServer vulnerable a `CVE-2024-36401`**. (b) Esa víctima **no es gubernamental ni diplomática**: la fuente sitúa las entidades de gobierno en Taiwán y las diplomáticas en Indonesia, y a Colombia en el grupo de «otras organizaciones». El requisito que originó este informe afirmaba lo contrario |
| Marcado de difusión | `TLP:CLEAR` · `PAP:AMBER` |
| Clasificación interna | Sin clasificar. Material íntegramente de publicación abierta |
| Requisitos atendidos | `PIR-01`, `PIR-03`, `PIR-06` (evasión de controles de endpoint y suficiencia de nuestra telemetría), `PIR-09` (superficie expuesta a Internet y gestión de parches), `RFI-2026-11-A` |
| Solicitante / consumidor primario | Jefatura de SOC e Ingeniería de Detección. **Y, de forma inusual, el responsable del producto de EDR**: este informe contiene una lista de capacidades del sensor que este cargador neutraliza, y esa lista es una conversación con el fabricante |
| Ventana de observación | 2026-01-01 → 2026-11-17. **La fuente publica el 24 de junio de 2026** y declara que la actividad sigue en seguimiento |
| Base de colección | Cuatro fuentes externas; **una primaria y técnica leída en original con su anexo completo**. Sin telemetría propia |
| Autor (analista) | Célula CTI |
| Revisión por pares | Pendiente |
| Aprobación | Pendiente |
| Caducidad / revisión | 2027-02-17 (92 días). **Revisión anticipada obligatoria si cualquier proveedor atribuye este clúster a un actor conocido**: la mitad de los juicios de este informe cambiarían de confianza |
| Productos relacionados | `CTI-2026-030` (Salt Typhoon: **comparte `CVE-2023-20198`**, y la comparación de cómo lo usan cada uno es instructiva) · `CTI-2026-028` (UNC3886: comparte el patrón de ir contra los sensores y no contra las defensas) · `CTI-2026-023` (Machete: el otro actor de esta cartera que llega a organizaciones andinas por el **eje geoespacial**) · `CTI-2026-026` (APT36: el otro informe con marco de C2 público, con la misma advertencia de que su presencia no atribuye) · `CTI-2026-019` (ARTEX) |
| Paquete legible por máquina | Las tablas `cti:ioc` del Anexo A alimentan `ioc_index.csv`. **La fuente declara expresamente que hay indicadores adicionales reservados a su servicio de inteligencia**: lo publicado es un subconjunto, y el Anexo A lo hereda |

> ⚠ **Limitación estructural, y una aclaración de naturaleza.** **Sin telemetría
> propia**: `O-4` es un cuestionario. Y una aclaración que condiciona todo el
> documento: **esto no es un perfil de actor, porque no hay actor**. Es un
> clúster de intrusión que su descubridor no atribuye, cuyos objetivos últimos
> declara desconocidos y cuyo alcance real sospecha mayor que lo observado.
> Escribir sobre eso exige una disciplina distinta: **no se puede inferir
> intención a partir de identidad, porque no hay identidad**. Lo único
> disponible es el comportamiento, y por suerte el comportamiento está
> documentado con un detalle excepcional.

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** Existe un clúster de intrusión activo en 2026, con víctimas en al menos nueve países y tres continentes, que despliega un cargador propio no documentado previamente —SharkLoader— cuya única carga observada es un **Cobalt Strike Beacon**. Kaspersky GReAT lo descubrió investigando una intrusión en una organización diplomática de Indonesia y lo amplió a una campaña. Valoramos **casi con certeza** *(≥99 %)* que el clúster exista y sea un conjunto coherente de actividad. **Confianza: alta.** *Base:* fuente primaria B-2 con análisis de código propio, cuatro dominios de mando y control publicados y siete muestras identificadas.

**KJ-2.** La cadena de SharkLoader está construida **contra los sensores concretos de los que depende un producto de detección de endpoint**, y la lista es sistemática: desvía unas treinta funciones de la interfaz de programación de Windows mediante una biblioteca legítima de desvíos, **construye en tiempo de ejecución llamadas directas al núcleo** para eludir los ganchos del producto de seguridad en espacio de usuario, **anula el registro de eventos del sistema** haciendo que tres funciones de traza devuelvan éxito sin escribir nada, **devuelve la memoria del implante a sólo lectura durante los intervalos de reposo** y la restaura a ejecutable al despertar, y **falsifica el proceso padre a `svchost.exe`** de todo lo que lanza. Valoramos **casi con certeza** *(≥99 %)* que esto sea un diseño deliberado contra mecanismos de detección concretos y no una colección de trucos genéricos. **Confianza: alta.** *Base:* la tabla de ganchos de la fuente primaria, donde cada entrada tiene una finalidad defensiva identificable.

**KJ-3.** La consecuencia práctica de `KJ-2` es que **la detección hay que trasladarla fuera del alcance del cargador**, y eso es posible porque el cargador no puede alcanzar tres cosas: la red, el programador de tareas y el sistema de ficheros antes de la ejecución. Valoramos **probable** *(55–80 %)* que una organización con detección exclusivamente basada en telemetría de proceso y barrido de memoria en el endpoint **no vea** esta cadena. **Confianza: moderada.** *Base:* inferencia desde las capacidades neutralizadas, no desde una prueba controlada; la eficacia real depende del producto concreto y de si observa en el núcleo o en espacio de usuario.

**KJ-4.** **La víctima colombiana se comprometió por un GeoServer vulnerable a `CVE-2024-36401`**, y eso convierte el caso en un problema de superficie expuesta y no de inteligencia. La fuente valora con **confianza media** que el actor use principalmente exploits de prueba de concepto **públicos**, porque las trece vulnerabilidades observadas tienen código de explotación disponible, y observó que **una de las direcciones asociadas a un dominio de mando y control hacía además rastreo masivo de Internet**. Valoramos **probable** *(55–80 %)* que la selección de la víctima colombiana haya sido **oportunista** —tenía un servicio vulnerable expuesto— y no dirigida. **Confianza: moderada.** *Base:* la propia fuente califica la victimología como mezcla de estratégica y oportunista, y su confianza en el objetivo de espionaje es **baja**.

**KJ-5.** **El requisito que originó este informe situaba a Colombia entre los organismos gubernamentales y las misiones diplomáticas afectadas, y la fuente no dice eso.** La fuente nombra entidades de gobierno en **Taiwán**, una organización diplomática en **Indonesia**, empresas de desarrollo de software en **Taiwán, Líbano y Siria**, y organizaciones adicionales en **Hong Kong, Colombia, Macedonia, Nepal y Serbia**. Valoramos **casi con certeza** *(≥99 %)* que la víctima colombiana publicada no sea una entidad gubernamental ni diplomática. **Confianza: alta.** *Base:* lectura literal de la fuente primaria, cuya redacción es inequívoca en la asignación de sectores por país.

**KJ-6.** La atribución es **«hablante de chino, con confianza baja»**, y el fundamento es más débil de lo que ese enunciado ya sugiere: la fuente declara que **no hay solapamiento de código ni de infraestructura con ningún actor conocido**, que las técnicas tampoco encajan, y que la valoración se apoya en que tres herramientas públicas de post-explotación —FScan, Searchall y Pillager— las escribieron personas identificadas como hablantes de chino en GitHub. **La propia fuente advierte que otros actores podrían estar usando esas mismas herramientas.** Valoramos **poco probable** *(20–45 %)* que esa base baste para sostener la atribución si se somete a revisión. **Confianza: moderada.** *Base:* la autoría declarada de una herramienta pública es uno de los ejes de atribución más débiles que existen, y esta cartera ya documentó el mismo problema con Mythic en `CTI-2026-026`.

**KJ-7.** **El número real de víctimas es muy probablemente mucho mayor que el publicado, y la fuente lo dice.** Declara que su visibilidad se limita a los incidentes observados en su propia telemetría y que **sospecha que el número real de compromisos puede ser significativamente superior**, dado que el actor explotó activamente varias aplicaciones expuestas a Internet. Valoramos **muy probable** *(80–95 %)* que haya víctimas no identificadas en Latinoamérica. **Confianza: moderada-alta.** *Base:* la advertencia explícita del descubridor, más el hecho de que el vector principal es la explotación oportunista de servicios públicos, que no selecciona por país.

**Qué cambiaría estos juicios.** **(a)** La atribución del clúster a un actor conocido por cualquier proveedor —cambiaría `KJ-6` y permitiría, por primera vez, inferir intención. **(b)** La aparición de una carga distinta de Cobalt Strike en esta cadena —convertiría al cargador en plataforma y obligaría a reevaluar `KJ-1`. **(c)** Evidencia de exfiltración de datos, que la fuente declara no haber observado: hoy la hipótesis de espionaje se sostiene con confianza baja precisamente por eso. **(d)** Un segundo incidente regional con un vector geoespacial, que convertiría `KJ-4` de observación en patrón y elevaría la prioridad de `E-b`.

---

## 2. Resumen ejecutivo

Este informe trata de algo que normalmente no se escribe: **un conjunto de intrusiones sin dueño**. Kaspersky investigaba un incidente en una organización diplomática de Indonesia, encontró un cargador que nadie había documentado, y al buscar más instancias descubrió que lo que parecía un caso aislado era una campaña con víctimas en Taiwán, Hong Kong, Líbano, Siria, Macedonia del Norte, Nepal, Serbia y **Colombia**. Lo llamó StrikeShark, al cargador SharkLoader, y **declaró explícitamente que no lo atribuye a ningún grupo conocido** y que sus objetivos finales siguen bajo investigación.

Hay dos cosas que hacen que esto merezca un informe propio, y una de ellas es regional.

**La primera es cómo está hecho el malware.** No es un implante con funciones de espionaje: es una máquina de ejecutar discretamente un Cobalt Strike Beacon, y su diseño parece escrito con la lista de capacidades de un producto de detección de endpoint delante. Enumeremos, porque la enumeración es el argumento: desvía unas treinta funciones de la interfaz de Windows usando una biblioteca de Microsoft pensada para eso; de las que le interesan, construye **en tiempo de ejecución** las llamadas directas al núcleo, con lo que el gancho que el producto de seguridad había puesto en espacio de usuario deja de verse atravesado; apaga el registro de eventos del sistema sustituyendo tres funciones de traza por otras que devuelven éxito sin escribir nada; **mientras el Beacon duerme, devuelve su memoria a sólo lectura y la vuelve a hacer ejecutable al despertar**, de modo que un barrido de memoria que busque regiones ejecutables anómalas no encuentre nada; y hace que cualquier proceso que el Beacon lance aparezca como hijo de `svchost.exe` en lugar del suyo. Para entrar en el sistema usa además una técnica —publicada por un investigador independiente— que manipula las estructuras internas del cargador de Windows para soltar su cerrojo y poder crear un hilo desde donde normalmente produciría un bloqueo.

Nada de eso es nuevo por separado. **Lo llamativo es que esté todo junto y que cada pieza corresponda a un sensor distinto.** No es evasión: es una revisión de inventario.

**La segunda razón es colombiana y es muy concreta.** A la víctima de Colombia se entró por un **GeoServer** —un servidor de datos geoespaciales de código abierto, ubicuo en la administración pública de la región para catastro, ordenamiento territorial, minería, ambiente e infraestructuras de datos espaciales— vulnerable a `CVE-2024-36401`. Esa vulnerabilidad tenía parche y código de explotación público. Y la fuente observó que **una de las direcciones asociadas a su infraestructura de mando y control hacía rastreo masivo de Internet**, lo que apunta a una selección oportunista: no es que alguien quisiera entrar en esa organización, es que esa organización tenía un servicio vulnerable a la vista.

**Eso cambia por completo qué hay que hacer**, y es el motivo de que este informe insista. Si la víctima fue elegida, la respuesta es contrainteligencia. Si la víctima fue encontrada, la respuesta es inventario y parcheo — y la pregunta para cualquier organización de la región no es «¿nos quieren?» sino «¿cuántos de nuestros servicios expuestos están en la lista de trece vulnerabilidades del Anexo A.1?». Hay una de esas trece que esta cartera ya documentó en otro informe y por otro actor: `CVE-2023-20198`, de Cisco IOS XE, la misma que usa el actor de `CTI-2026-030`. Dos clústeres sin relación entre sí entrando por la misma puerta sin parchear es, probablemente, el dato más útil de todo este documento.

**Y una corrección.** El requisito que pidió este informe situaba a Colombia entre los organismos gubernamentales y las misiones diplomáticas afectadas. La fuente no dice eso: las entidades de gobierno que nombra están en Taiwán, la diplomática en Indonesia, y Colombia aparece en el grupo de «otras organizaciones». La diferencia no es un detalle de redacción: decide si esto se gestiona desde el área de inteligencia o desde la de gestión de vulnerabilidades.

<!-- cti:cards -->

| Rasgo | Qué significa | Etiqueta |
|---|---|---|
| Un clúster sin atribuir | **No se puede inferir intención desde la identidad, porque no hay identidad.** Todo juicio sobre propósito tiene confianza baja, y la propia fuente lo declara así | `01 · sin dueño` |
| Evasión por enumeración de sensores | Treinta ganchos de API, llamadas directas al núcleo construidas en caliente, registro de eventos anulado y memoria que cambia de permisos al dormir. **Cada pieza corresponde a un sensor** | `02 · contra el EDR` |
| La carga final es una herramienta legítima | Cobalt Strike. **Su presencia no atribuye nada**, y toda la inversión del adversario está en entregarla sin ser visto, no en la herramienta | `03 · el que paga es el sigilo` |
| Entrada por explotación oportunista de servicios públicos | Catorce vulnerabilidades, **todas con exploit público**, y una dirección de la propia infraestructura rastreando Internet. **La víctima no fue elegida: fue encontrada** | `04 · oportunismo` |
| El eje colombiano es geoespacial | GeoServer, `CVE-2024-36401`. Un componente que la administración pública de la región despliega masivamente y que casi nunca está en el inventario de nadie | `05 · Colombia` |
| Nombres de directorio de proveedores de seguridad | El actor usa nombres como el de un fabricante de antivirus para sus carpetas de trabajo. **Detectable, y con falso positivo nulo** | `06 · el descuido` |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `14` | Vulnerabilidades de aplicaciones y dispositivos expuestos usadas para entrar | **Todas con código de explotación público.** Es el Anexo A.1 y la sección que hay que atender primero |
| `≈30` | Funciones de la interfaz de Windows desviadas por el componente de evasión | Más dos ganchos adicionales con una segunda biblioteca, sobre reserva de memoria y reposo |
| `3` | Funciones de traza del registro de eventos anuladas | `EtwEventWrite`, `EventWrite`, `EventWriteEx`. **Devuelven éxito sin escribir nada** |
| `9` | Países con víctimas identificadas | Indonesia, Taiwán, Hong Kong, Líbano, Siria, Colombia, Macedonia del Norte, Nepal, Serbia — **y la fuente dice «y más»** |
| `4` | Dominios de mando y control publicados | Tres de ellos suplantan nomenclatura de Microsoft |
| `1` | Víctimas colombianas confirmadas, **no gubernamentales** | Por **GeoServer**, `CVE-2024-36401` |
| `BAJA` | Confianza de la atribución declarada por el descubridor | «Hablante de chino, con confianza baja», apoyada en la autoría en GitHub de tres herramientas públicas |
| `0` | Casos de exfiltración de datos observados | Por eso la hipótesis de espionaje se sostiene con confianza baja. **No excluye que ocurra después** |

> ✅ **Decisiones que se solicitan, con plazo.**
> **(a) 7 días:** contrastar el Anexo A.1 —trece vulnerabilidades— contra el inventario de servicios expuestos a Internet. Es la medida de mayor efecto y no depende de ningún indicador perecedero (`E-a`).
> **(b) 14 días, y es la pregunta regional:** inventariar **GeoServer y cualquier componente geoespacial expuesto**, y comprobar su versión. Casi nunca está en el inventario de aplicaciones (`E-b`).
> **(c) 14 días:** desplegar `D-1` y `D-2`, que cazan la cadena por donde el cargador no puede llegar: el programador de tareas y la disposición de ficheros (`E-c`).
> **(d) 30 días, y es una conversación con el fabricante:** llevar al proveedor de EDR la lista de `X-3.1` y preguntar, por cada técnica, si su sensor la observa desde el núcleo o desde espacio de usuario (`E-d`).
> **(e) 30 días:** verificar que la telemetría de registro de eventos del sistema se **transporta fuera del equipo en tiempo real**, porque un anulado local es invisible si el consumidor está en el propio equipo (`E-e`).
> **(f) Inmediato:** no citar este clúster como «actor chino». La fuente dice confianza baja (`E-f`).

---

## 3. Alcance, requisitos y limitaciones

**3.1 Requisitos de inteligencia atendidos**

| Req. | Enunciado | ¿Respondido? | Dónde |
|---|---|---|---|
| PIR-01 | ¿Qué actores tienen intención y capacidad contra nuestra región? | **Parcial por naturaleza del objeto:** hay capacidad documentada y la intención es desconocida porque no hay actor | `KJ-1`, `KJ-4`, `O-2` |
| PIR-03 | ¿Qué técnicas invalidan nuestros controles? | **Sí, y es el núcleo del informe** | `KJ-2`, `X-3.1`, `T-3` |
| PIR-06 | ¿Es suficiente nuestra telemetría de endpoint frente a evasión activa? | **Sí, y la respuesta es una conversación con el fabricante** | `E-d`, `X-3.1`, `T-5` |
| PIR-09 | ¿Qué superficie expuesta a Internet nos convierte en objetivo oportunista? | **Sí, con lista concreta de trece vulnerabilidades** | `A.1`, `E-a`, `E-b` |
| RFI-2026-11-A | El requisito describía la campaña y la ubicación de sus víctimas. ¿Se sostiene? | **Parcialmente.** Véase `3.5` | `KJ-5`, `3.5` |
| PIR-04 | ¿Nos afecta? | **No.** Requiere telemetría propia | `O-4`, sin evaluar |

**3.2 Fuera de alcance.** No se evalúan: Cobalt Strike como producto ni su detección genérica, que es materia de otro producto y cuya cobertura se presupone; la atribución del clúster, que su descubridor declara preliminar y este informe no está en condiciones de mejorar; los detalles de desempaquetado de los módulos cifrados, que la fuente describe con un empaquetador propio no identificado; y la explotación de cada una de las trece vulnerabilidades, de las que la fuente declara no haber obtenido los exploits.

**3.3 Limitaciones de la colección.** Cinco, y la primera es estructural del objeto.

1. **No hay actor.** Todo lo que normalmente se deduce de la identidad —intención, prioridades, selección futura, relación con otros clústeres— aquí no se puede deducir. El informe se construye enteramente sobre comportamiento, y las secciones que normalmente hablarían de propósito declaran su vacío.
2. **Una sola fuente técnica.** No hay corroboración independiente del análisis de código: ningún otro proveedor ha publicado sobre SharkLoader que hayamos podido localizar. La fuente es de calidad y publica su método, pero **es única**, y eso limita el techo de confianza de todo el apartado técnico.
3. **El anexo de indicadores publicado es un subconjunto declarado.** La fuente dice expresamente que hay información adicional, incluidos indicadores, disponible para los clientes de su servicio de inteligencia.
4. **Visibilidad limitada a la telemetría del descubridor**, y él mismo lo advierte: sospecha que el número real de compromisos es significativamente superior.
5. **No se observó exfiltración.** De modo que el propósito del clúster es, literalmente, desconocido. Cualquier afirmación sobre lo que buscan es especulación, incluida la nuestra.

**3.4 Metodología.** ICD 203. Código Admiralty doble (Anexo B). MITRE ATT&CK v18. Pirámide del Dolor, con una lectura inusual en `T-3`. ACH y pre-mortem en `O-6`. **Y una técnica estructurada propia de este informe: el contraste entre la confianza declarada por la fuente primaria y la confianza con que la reprodujo la cobertura secundaria**, que está en `O-2.1` y es el motivo de `E-f`.

**3.5 Lo que el requisito afirmaba, y lo que la fuente sostiene**

<!-- cti:table highlight="Impreciso|Corregido" -->

| # | Afirmación del requisito | Veredicto | Qué dice la fuente |
|---|---|---|---|
| 1 | «Reportada por Kaspersky en junio/julio de 2026» | **Corroborado** | Publicación en Securelist el **24 de junio de 2026**, con comunicado de prensa de la misma fecha |
| 2 | «Operación de espionaje sigiloso» | **Parcial, y la fuente es más prudente** | El sigilo está sobradamente documentado. Pero la fuente valora el objetivo de espionaje **con confianza baja**, precisamente porque la actividad posterior al compromiso observada se limitó a acceso a credenciales, reconocimiento y movimiento lateral, **sin exfiltración observada** |
| 3 | «Apunta activamente a organismos gubernamentales, misiones diplomáticas y empresas de desarrollo de software en América Latina» | **Impreciso, y la imprecisión importa** | Esos tres tipos de víctima existen, **pero no en América Latina**: los organismos gubernamentales están en **Taiwán**, la entidad diplomática en **Indonesia**, y las empresas de desarrollo de software en **Taiwán, Líbano y Siria**. En América Latina hay **una** víctima, colombiana, que la fuente clasifica como «otra organización» |
| 4 | «Con **Colombia** confirmada entre los países directamente afectados» | **Corroborado, y es el dato más útil del requisito** | Confirmado, **y con el vector concreto**: explotación de una instancia de **GeoServer** vulnerable a `CVE-2024-36401` |
| 5 | «Emplea el cargador en memoria no documentado previamente SharkLoader» | **Corroborado con precisión** | Es exactamente así, incluido el carácter en memoria: los módulos se descifran y se cargan reflexivamente **sin escribirse en disco**, y a los PE descifrados se les ha quitado la cabecera `MZ` como medida antianálisis |
| 6 | «Clúster sin atribución consolidada» | **Corroborado, y conviene subrayarlo** | La fuente declara **no** atribuirlo a ningún APT ni grupo criminal conocido, por ausencia de solapamiento de código, de infraestructura y de técnicas |

> ⚠ **Por qué la imprecisión del punto 3 no es menor.** «Un clúster de
> espionaje apunta a gobiernos y misiones diplomáticas en América Latina» y «un
> clúster explotó un servidor geoespacial sin parchear de una empresa
> colombiana que encontró rastreando Internet» describen el mismo expediente y
> **piden decisiones opuestas**: la primera frase moviliza al área de
> inteligencia y a los enlaces institucionales; la segunda, al inventario de
> activos y al ciclo de parcheo. En este caso la fuente apoya la segunda. Y la
> ironía útil es que la segunda es **más** actuable: nadie puede impedir que un
> servicio extranjero se interese por su ministerio, pero cualquiera puede
> parchear un GeoServer.

---

# NIVEL ESTRATÉGICO
### Para: Consejo · CISO · Riesgo · Horizonte: 6–24 meses

## E-1. Qué representa un clúster sin atribuir, y por qué es más incómodo que un actor con nombre

Casi toda la cartera de este repositorio describe actores con nombre, origen valorado y motivo legible. Esa estructura es cómoda porque permite una cadena de razonamiento: sé quién es, deduzco qué quiere, deduzco a quién atacará y con qué, y priorizo. **Aquí esa cadena está cortada en el primer eslabón**, y el resultado no es menos amenaza sino menos capacidad de predecir.

Hay que resistir las dos tentaciones que produce ese vacío. **La primera es rellenarlo.** Un clúster sin atribuir resulta narrativamente insatisfactorio, y la industria tiende a resolverlo adoptando la pista más llamativa disponible —aquí, que tres herramientas públicas las escribieron hablantes de chino— y promoviéndola a conclusión. `O-2.1` documenta que eso ya ocurrió con este clúster en cuestión de días. **La segunda es desestimarlo**: sin actor no hay titular, y sin titular no hay atención. Pero lo que este expediente aporta no depende de quién esté detrás: una lista de trece vulnerabilidades con exploit público y un catálogo de técnicas de evasión son útiles exactamente igual si el autor es un servicio estatal, un contratista o un grupo criminal.

<!-- cti:cards -->

| Cambio estructural | Por qué nos afecta | Etiqueta |
|---|---|---|
| El esfuerzo del adversario se concentra en **entregar**, no en el implante | La carga final es una herramienta pública y conocida. **Lo valioso y lo caro es el sigilo**, y eso significa que la defensa basada en reconocer la carga llega tarde por diseño | `01 · dónde está la inversión` |
| La evasión va contra sensores, no contra políticas | No intenta burlar una regla: intenta que el sensor no vea. **Es un problema de arquitectura de nuestro producto de seguridad, no de nuestra configuración** | `02 · el nivel del problema` |
| La selección es, al menos en parte, de barrido | Una dirección de su infraestructura rastreaba Internet. **Ser pequeño, periférico o poco interesante no protege de nada** | `03 · oportunismo` |
| Exploits públicos, no desarrollo propio | Valorado con confianza media por la fuente. **Buena noticia operativa:** el parche existe en los trece casos y la ventana se cierra con gestión, no con inteligencia | `04 · la buena noticia` |
| Sin exfiltración observada | **Puede significar dos cosas opuestas:** que no buscan datos, o que estaban todavía en fase de reconocimiento cuando se los descubrió. La fuente no decide, y nosotros tampoco | `05 · lo que no sabemos` |
| El sector afectado es irrelevante | Diplomacia, gobierno, desarrollo de software y «otros», en tres continentes. **No hay perfil sectorial que permita a nadie excluirse** | `06 · nadie está fuera` |

## E-2. Victimología

<!-- cti:bars title="Víctimas identificadas por sector, según la clasificación literal de la fuente" -->

| Sector y país | Casos identificados |
|---|---|
| Desarrollo de software (Taiwán, Líbano, Siria) | `3` |
| Gobierno (Taiwán) | `1` |
| Diplomacia (Indonesia) | `1` |
| Otras organizaciones (Hong Kong, **Colombia**, Macedonia del Norte, Nepal, Serbia) | `5` |

> ⚠ **Dos advertencias sobre este gráfico, y la segunda es la importante.**
> **Primera:** son organizaciones identificadas, no un censo; la fuente declara
> que sospecha que el número real es significativamente mayor. **Segunda, y es
> la que corrige el requisito:** la columna de «otras organizaciones» es donde
> está Colombia. No es un gráfico de «gobiernos latinoamericanos atacados»,
> porque ese gráfico estaría vacío.

**Lo que la distribución dice, y es poco por diseño.** La fuente lo expresa con una frase que conviene leer despacio: la victimología observada sugiere una campaña de **alcance geográfico amplio y conjunto de objetivos diverso**, más que un foco estrecho en un sector o una región. Es decir: la distribución no revela un criterio de selección porque probablemente no hay uno, o hay dos superpuestos —unos objetivos buscados y otros encontrados— y no se pueden separar con lo publicado.

**Para una organización de la región, la lectura útil es ésta:** la pregunta «¿somos del perfil que ataca?» no tiene respuesta y no es la pregunta. La pregunta es `E-a`: cuántas de las trece vulnerabilidades del Anexo A.1 están vivas en nuestro perímetro. Un clúster que encuentra víctimas rastreando Internet convierte la gestión de parches en control de selección: **no se elige no ser interesante, se elige no ser alcanzable**.

## E-3. Tendencia y pronóstico

No hay serie temporal. La fuente publica una vez, en junio de 2026, y declara seguimiento en curso. Presentar un gráfico de evolución sería inventarlo, de modo que esta sección es prosa y escenarios.

<!-- cti:cards -->

| Escenario | Desarrollo | Etiqueta |
|---|---|---|
| **Más probable** | El clúster sigue operando con el mismo patrón: barrido de Internet, explotación de vulnerabilidades con exploit público, SharkLoader y Cobalt Strike. La lista de vulnerabilidades se amplía con cada publicación relevante nueva, con semanas de retraso respecto a la aparición del exploit público | `Probable · 55–80 %` |
| **Alternativa creíble** | Algún proveedor lo atribuye a un actor conocido en los próximos doce meses, muy posiblemente por solapamiento de infraestructura y no de código. **Eso no cambiaría ninguna de las medidas de `E-4`**, y conviene decirlo: la utilidad de este informe no depende de la atribución | `Posibilidad real · 45–55 %` |
| **La que importa para la detección** | El cargador se desacopla de Cobalt Strike y pasa a entregar cargas distintas, propias o de terceros. Sería la confirmación de que SharkLoader es **plataforma** y no herramienta de una campaña, y degradaría toda la detección basada en la carga | `Posibilidad real · 45–55 %` |
| **La que importa para la región** | Un segundo incidente latinoamericano por vector geoespacial o por otro componente de administración pública poco inventariado. **Convertiría `KJ-4` de observación en patrón** y haría de `E-b` una prioridad regional y no una comprobación propia | `Poco probable · 20–45 %` |
| **Descartado, y se consigna** | Que esto sea una campaña dirigida contra Latinoamérica. **La fuente lo contradice de forma inequívoca**: nueve países, tres continentes, un caso regional. Se consigna para que el requisito que lo sugirió no se reabra | `Descartada` |

## E-4. Decisiones que este informe pide al nivel estratégico

<!-- cti:table highlight="GeoServer|fabricante|Inmediato" -->

| # | Decisión | Fundamento | Plazo |
|---|---|---|---|
| E-a | **Contrastar las trece vulnerabilidades del Anexo A.1 contra el inventario de servicios expuestos a Internet**, y cerrar las vivas | `KJ-4`. Las trece tienen parche y exploit público. **Es la única medida de este informe que elimina la posibilidad de ser seleccionado** | 7 días |
| E-b | **Inventariar GeoServer y todo componente geoespacial expuesto** —servidores de mapas, nodos de infraestructura de datos espaciales, visores catastrales— y comprobar versión y parcheo | `KJ-4`, y el vector de la víctima colombiana. **Estos componentes casi nunca están en el inventario de aplicaciones** porque los despliega el área técnica de cartografía y no la de sistemas | 14 días |
| E-c | Desplegar `D-1` y `D-2`: tareas programadas con nombre suplantado y disposición de ficheros del cargador. **Cazan la cadena donde el cargador no puede llegar** | `KJ-3`. La evasión de `KJ-2` es toda intraproceso: no alcanza al programador de tareas ni al momento de escritura en disco | 14 días |
| E-d | **Llevar al fabricante de EDR la lista de `X-3.1`** y obtener respuesta por escrito, técnica por técnica: ¿se observa desde el núcleo o desde espacio de usuario? | `KJ-2`, `KJ-3`. **No es una conversación comercial, es una verificación de cobertura**, y el resultado determina si `E-c` es el principal control o sólo un refuerzo | 30 días |
| E-e | Verificar que la telemetría del registro de eventos del sistema **se transporta fuera del equipo en tiempo real** | `KJ-2`. El cargador anula la escritura de trazas en el proceso. Un consumidor local no ve lo que no se escribe; **un recolector remoto sí ve que dejaron de llegar trazas**, que es la otra mitad de la detección | 30 días |
| E-f | **No citar este clúster como «actor chino» ni «APT chino».** La fuente declara confianza baja y advierte que otros actores podrían usar las mismas herramientas | `KJ-6`, `O-2.1`. Es higiene analítica y cuesta cero | **Inmediato** |
| E-g | Revisar si las direcciones y dominios del Anexo A.3 aparecen en registros de los últimos doce meses, **declarando que un resultado negativo no es prueba de ausencia** | `KJ-7`, `3.3.3`. El subconjunto publicado es declaradamente parcial | 30 días |
| E-h | Decidir la posición ante **Cobalt Strike en la red propia**: si su detección es responsabilidad del EDR, de la red o de ambos, y quién responde si aparece | `KJ-1`. La carga final de esta cadena es la herramienta ofensiva más común del mundo, y la detección de red es la que el cargador no puede tocar | 45 días |

---

# NIVEL OPERACIONAL
### Para: Jefatura de SOC · Respuesta a Incidentes · Threat Hunting · Horizonte: semanas–meses

## O-1. Identificación y designaciones

| Designación | Origen | Qué designa | Grado de equivalencia |
|---|---|---|---|
| `StrikeShark` | Kaspersky GReAT, junio de 2026 | **El clúster de intrusión.** La fuente usa la expresión «por ahora rastreamos esta actividad como StrikeShark», que es el lenguaje con que se nombra un conjunto no atribuido | **Referencia.** No es un actor: es un clúster |
| `SharkLoader` | Kaspersky GReAT | **La familia de cargador**, no documentada previamente. Es el elemento que une los incidentes | **Familia de malware.** No confundir con el clúster |
| `Cobalt Strike Beacon` | Herramienta comercial legítima | La **única carga final observada** en esta cadena | **No es del actor y no atribuye nada.** Igual que Mythic en `CTI-2026-026` |
| `FScan` · `Searchall` · `Pillager` | Herramientas públicas de GitHub | Herramientas de post-explotación usadas por el clúster. **Su autoría declarada es el único fundamento de la atribución** | **Herramientas públicas.** Su presencia la comparten muchos actores |
| `SharpGPOAbuse` | Herramienta pública | Modificación de objetos de política de grupo en Active Directory | **Herramienta pública** |
| «APT chino» | **Cobertura secundaria** | — | **No es una designación de la fuente.** Véase `O-2.1` |

> **Nota de *tradecraft*, y aquí el riesgo es el inverso del habitual.** El error
> frecuente de esta cartera es fusionar alias distintos. Aquí el riesgo es
> **crear un alias donde no hay actor**: tratar «StrikeShark» como si fuera un
> grupo con intenciones, historia y país, cuando es una etiqueta provisional
> para un conjunto de incidentes que comparten un cargador. La fuente es
> cuidadosa con el lenguaje —habla de *clúster de intrusión*— y conviene
> heredar ese cuidado, porque la diferencia aparece en cuanto alguien pregunta
> «¿y qué quieren?». La respuesta honesta es que nadie lo sabe.

## O-2. Estructura y atribución

| Eje de atribución | Valoración | Confianza |
|---|---|---|
| Clúster técnico | **Establecido.** Una familia de cargador propia, con componentes, nombres de fichero, esquema de cifrado y cadena de ejecución consistentes a través de las víctimas | **Alta** |
| Grupo organizado | **Probable.** Desarrollo propio de un cargador con empaquetador no identificado, treinta ganchos de API con finalidad diferenciada y variantes con distintos objetivos de carga lateral indican un equipo, no un individuo | Moderada |
| Nexo estatal | **No valorado por nadie.** La fuente no lo plantea | — |
| Origen lingüístico | **«Hablante de chino, con confianza baja»**, y la base es la autoría declarada en GitHub de tres herramientas públicas de post-explotación | **Baja, declarada así por la fuente** |
| Identidad nominal | **Ninguna** | — |
| Propósito | **Desconocido.** La fuente valora un posible objetivo de espionaje **con confianza baja**, por la escasez de actividad posterior al compromiso observada, y plantea en paralelo la hipótesis oportunista | **Baja** |

*Razonamiento de la fuente, en sus términos:* no hay solapamiento de código ni de infraestructura con ningún actor existente, y las técnicas empleadas tampoco encajan con las de actores conocidos. Lo único que apunta a algún sitio es que varias herramientas de reconocimiento —FScan, Searchall, Pillager— fueron desarrolladas por personas identificadas como hablantes de chino en GitHub. **Y la fuente añade la salvedad que convierte su propia valoración en provisional:** subsiste la posibilidad de que otros actores estén utilizando esas mismas herramientas.

*Contraargumento, que aquí no hace falta construir porque la fuente ya lo construyó:* la autoría de una herramienta pública no dice nada sobre quién la usa. FScan es un escáner de red con módulos de explotación, de uso extendidísimo en pruebas de intrusión y en actividad criminal; inferir el idioma del operador a partir del idioma del autor del escáner equivale a inferir la nacionalidad de un conductor a partir de la del fabricante del coche. Esta cartera ya hizo exactamente esta advertencia con Mythic y Poseidon en `CTI-2026-026`, y la hereda aquí literalmente: **la presencia de la herramienta no atribuye**.

### O-2.1 — Una inflación de confianza, documentada

Hay un fenómeno que esta cartera viene documentando informe tras informe, y este expediente ofrece un caso limpio y pequeño, útil precisamente por ser pequeño.

**Lo que dice la fuente primaria, literalmente:** valora que StrikeShark es un actor hablante de chino **con confianza baja**; precisa que la valoración se basa en indicadores limitados y **debe considerarse preliminar**; y advierte que otros actores podrían estar usando las mismas herramientas.

**Lo que apareció en cobertura secundaria pocos días después:** que la campaña se atribuye **con confianza moderada** a un actor de habla china.

**Qué pasó en el camino.** Nada dramático: un resumen que redondeó un adverbio. Pero «baja» y «moderada» no son matices de estilo, son escalones de una escala definida —y la propia fuente publica la suya— con consecuencias distintas: una valoración de confianza baja no debería sostener una decisión, y una de confianza moderada sí puede entrar en una matriz de riesgo. **El ascenso de un escalón convierte una pista en un dato sin que nadie haya añadido una sola evidencia.**

**Por qué se consigna aquí y no en una nota al pie.** Porque es la tercera vez que esta cartera documenta el mismo mecanismo —`CTI-2026-017`, `CTI-2026-022` y `CTI-2026-030` existen por variantes de él— y porque el caso tiene valor pedagógico: es **el eslabón uno** de la cadena. Primero una cobertura secundaria sube la confianza; después alguien cita la cobertura secundaria sin leer la primaria; después el clúster es «un APT chino» en una presentación interna; y a partir de ahí las medidas se diseñan contra un adversario con prioridades geopolíticas que nadie ha demostrado que exista. **La intervención barata está al principio**, y es `E-f`.

## O-3. Modelo de operación

Tres fases, y la fuente las documenta con un desequilibrio informativo que conviene señalar: la primera y la segunda con mucho detalle, la tercera con poco. **Ese desequilibrio es, en sí, el hallazgo más importante sobre el propósito del clúster.**

**Fase 1 — Entrada, por dos vías.** La primera es explotación de aplicaciones expuestas: en el caso indonesio, vulnerabilidades de Microsoft Exchange incluida `CVE-2021-26855`; en Taiwán, Openfire con `CVE-2023-32315`; **en Colombia, una instancia de GeoServer vulnerable a `CVE-2024-36401`**. Más allá de esos tres casos, la fuente identificó explotación de otras once vulnerabilidades en aplicaciones empresariales y dispositivos de red, todas listadas en el Anexo A.1. La segunda vía es **entrega por cuentagotas disfrazados de instaladores legítimos** —Google Update, Cisco AnyConnect— con documentos PDF señuelo embebidos; la fuente declara que **no sabe cómo se distribuyeron esos cuentagotas**, lo que es una brecha honesta y relevante.

**Fase 2 — Instalación, y aquí está casi todo el trabajo del adversario.** Tras la explotación se despliegan interfaces web de administración remota para persistir; se copia una aplicación legítima de Windows a una ubicación nueva y se ejecuta desde allí para provocar la carga lateral de una biblioteca maliciosa con el mismo nombre; esa biblioteca descifra y carga en memoria dos módulos cifrados con esquemas distintos, y el conjunto termina ejecutando un Cobalt Strike Beacon **sin que nada toque el disco en forma ejecutable reconocible**. El detalle está en `T-1` y en `X-1`.

**Fase 3 — Lo que hacen después, y es llamativamente poco.** Reconocimiento de sistema con tres comandos elementales; enumeración de Active Directory; volcado de credenciales del proceso de autenticación local y extracción de la base de datos del directorio; y herramientas públicas de escaneo y búsqueda de información sensible. **La fuente declara no haber observado exfiltración de datos.**

> **Lo que ese desequilibrio significa, con las tres lecturas posibles sobre la
> mesa.** Un adversario que invierte masivamente en entrar sin ser visto y
> después hace reconocimiento elemental puede ser tres cosas distintas: **(a)**
> un actor en fase temprana al que se descubrió antes de que llegara a su
> objetivo; **(b)** un actor cuyo producto es el acceso —lo obtiene, lo
> inventaría y lo entrega o lo vende a otro, lo que explicaría tanto el sigilo
> extremo como la ausencia de recolección—; o **(c)** un actor cuyo propósito
> es el acceso persistente en sí, para usarlo cuando convenga. La fuente no
> decide y nosotros tampoco, pero la hipótesis **(b)** merece quedar escrita
> porque tiene una consecuencia defensiva propia: si el producto es el acceso,
> **el daño no lo hará quien entró**, y el intervalo entre el compromiso y el
> impacto puede ser de meses. Es `H3` de `O-6`.

## O-4. Nuestra exposición

> ⬛ **Sección sin evaluar — requiere telemetría interna.** Y una nota poco
> habitual: **las dos primeras preguntas de esta tabla se responden sin
> telemetría de seguridad**, sólo con el inventario de activos. En este
> expediente, el inventario vale más que el EDR.

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| X-1 | ¿Cuántas de las **trece** vulnerabilidades del Anexo A.1 están vivas en servicios nuestros expuestos a Internet? | Inventario · escaneo externo | TI · Vulnerabilidades |
| X-2 | **¿Tenemos GeoServer, o cualquier servidor de mapas o nodo de infraestructura de datos espaciales, expuesto? ¿En qué versión? ¿Quién lo administra?** La última pregunta es la importante: suele no ser el área de sistemas | Inventario · escaneo externo | TI · área geoespacial |
| X-3 | ¿Existe en el parque algún `SystemSettings.exe` **fuera de** `C:\Windows\ImmersiveControlPanel\`? | EDR · barrido de ficheros | SOC |
| X-4 | ¿Hay directorios con nombres de **proveedores de seguridad** —incluido el nuestro— en `%ProgramData%` o `%APPDATA%` que no haya creado ese producto? | EDR · barrido de ficheros | SOC |
| X-5 | ¿Existen tareas programadas cuyo nombre imite a las de OneDrive, Edge o Windows Update y que **apunten a un ejecutable en el perfil del usuario**? | Programador de tareas | SOC · TI/Puesto |
| X-6 | ¿Se transporta la telemetría del registro de eventos del sistema **fuera del equipo en tiempo real**, o la consume un agente local? | Arquitectura de registro | SOC · Arquitectura |
| X-7 | ¿Observa nuestro EDR las llamadas al núcleo **desde el núcleo**, o depende de ganchos en espacio de usuario? | Fabricante | SOC · Compras |
| X-8 | ¿Detectamos Cobalt Strike **en la red**, con independencia del endpoint? ¿Con qué cobertura de perfiles maleables? | Red · NDR | SOC · Redes |
| X-9 | ¿Hay interfaces web de administración remota desplegadas en nuestros servidores expuestos que no hayamos puesto nosotros? | Revisión de servidores web | TI |
| X-10 | ¿Se han ejecutado `ntdsutil` con creación de instantánea, o `procdump` contra el proceso de autenticación local, en los últimos doce meses? | EDR | SOC |

## O-5. Cronología

<!-- cti:timeline -->

| Fecha | Hecho | Traza |
|---|---|---|
| `2016-04` | Se publica `CVE-2016-4437` (Apache Shiro). **Diez años después sigue en la lista de entrada de este clúster** | Global |
| `2021-03` | Se publica `CVE-2021-26855` (ProxyLogon), el vector del caso indonesio | Global |
| `2023-05` | Se publica `CVE-2023-32315` (Openfire), el vector de los casos taiwaneses | Global |
| `2023-10` | Se publica `CVE-2023-20198` (Cisco IOS XE). **La misma vulnerabilidad que usa el actor de `CTI-2026-030`** | Global |
| `2024-06` | **Se publica `CVE-2024-36401` (GeoServer)**, el vector del caso colombiano | **LATAM** |
| `2025` | Se publica `CVE-2025-55182` (React Server Components), la más reciente de la lista | Global |
| `2026-??` | **Investigación de una intrusión en una organización diplomática de Indonesia**: el punto de partida. Se descubre un cargador no documentado | Global |
| `2026-??` | La búsqueda de más instancias convierte el caso aislado en campaña: Taiwán, Hong Kong, Líbano, Siria, **Colombia**, Macedonia del Norte, Nepal, Serbia | **LATAM** |
| `2026-??` | **El caso colombiano:** explotación de una instancia de GeoServer vulnerable a `CVE-2024-36401` | **LATAM** |
| `2026-06-24` | **Kaspersky GReAT publica el informe técnico en Securelist** y el comunicado de prensa. Declara que **no atribuye** la campaña a ningún grupo conocido y que sigue el rastreo | Global |
| `2026-06 → 07` | Cobertura secundaria. **Al menos un resumen publica la atribución con confianza *moderada* y no baja**, que es lo que dice la fuente (`O-2.1`) | Global |
| `2026-11-17` | Emisión de este informe. **Nadie ha atribuido el clúster, y no hemos localizado ninguna publicación de otro proveedor sobre SharkLoader** | Global |

> **Sobre las fechas con `??`.** La fuente no publica las fechas de los
> incidentes individuales, sólo la de su propio informe. Se consignan en orden
> relativo y con el hueco visible, en lugar de estimarlas. Es la brecha `G-4`, y
> tiene una consecuencia práctica: **no se puede calibrar la ventana de
> retrohunt con fundamento**, de modo que la de doce meses del Anexo A es
> convención y así está declarada.

## O-6. Hipótesis alternativas consideradas

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| **H1 — Espionaje** | Consistente con los objetivos de gobierno, diplomacia y desarrollo de software, y con el nivel de sigilo. **La propia fuente la sostiene con confianza baja**, porque la actividad observada se limitó a credenciales, reconocimiento y movimiento lateral, y no se observó exfiltración | `Retenida · posibilidad real 45–55 %, confianza baja` |
| **H2 — Oportunismo de barrido** | Consistente con trece vulnerabilidades con exploit público, con víctimas sin perfil sectorial común en tres continentes, y con que **una dirección asociada a un dominio de C2 hacía rastreo masivo de Internet**. La fuente la plantea en paralelo a H1, no como alternativa excluyente | `Retenida · posibilidad real 45–55 %` |
| **H3 — El producto es el acceso** | Un actor que invierte mucho en entrar sin ser visto y poco en recolectar es compatible con un intermediario de acceso. **No hay evidencia a favor ni en contra, y se consigna porque tiene una consecuencia defensiva propia:** si es cierta, el daño lo causará otro, meses después, y el compromiso inicial será para entonces indetectable | `Retenida · poco probable 20–45 %` |
| **H4 — Actor hablante de chino** | **Lo que sostiene la fuente, con confianza baja declarada**, y cuyo único fundamento es la autoría en GitHub de tres herramientas públicas. La fuente misma advierte que otros actores podrían usarlas | `Retenida · confianza baja. NO usar como premisa` |
| **H5 — Es un actor conocido todavía no identificado** | Consistente con que un clúster con esta madurez técnica surja de la nada. Inconsistencia: la fuente declara ausencia de solapamiento de código, de infraestructura **y** de técnicas, que es una triple negación poco común y relativamente fuerte | `Retenida · posibilidad real 45–55 %` |
| **H6 — Campaña dirigida contra Latinoamérica** | **Falsada.** Nueve países, tres continentes, un caso regional, y una víctima regional alcanzada por un servicio expuesto vulnerable. Se consigna porque el requisito que originó el informe lo sugería | `Descartada` |
| **H7 — SharkLoader es una plataforma, no la herramienta de una campaña** | Consistente con las variantes observadas: cuatro objetivos distintos de carga lateral, cinco nombres distintos de módulo cifrado, dos esquemas de cifrado diferentes. **Si es cierta, aparecerán cargas distintas de Cobalt Strike**, y eso es el disparador `I-3` | `Retenida · posibilidad real 45–55 %` |

**Supuesto clave.** Que la evasión de SharkLoader es **intraproceso** y por tanto no alcanza al programador de tareas, al sistema de ficheros antes de la ejecución, ni a la red. Toda la estrategia de detección de `T-4` y `X-3` depende de ello. **Qué se rompe si es falso:** si una variante manipulara el programador de tareas para ocultar sus entradas, o alcanzara el agente de recolección de registros, `D-1` y `D-2` quedarían ciegas y la detección se reduciría a la red. La mitigación es que `D-5` —detección de red de Cobalt Strike— no dependa del endpoint en ningún punto.

**Pre-mortem.** Es mayo de 2027 y este informe resultó equivocado. Los tres motivos más probables:

1. **Se leyó como un informe sobre China.** A pesar de `KJ-6`, `O-2.1` y `E-f`, alguien citó «StrikeShark, APT chino» y el expediente se archivó en la carpeta de riesgo geopolítico, donde no produce ninguna acción. **El informe, en cambio, pide dos cosas de gestión de activos y una conversación con un fabricante**, y ninguna de las tres necesita saber quién está detrás.
2. **`E-b` no se hizo porque GeoServer no es de nadie.** Los componentes geoespaciales suelen administrarlos áreas técnicas que no reportan a sistemas, y una petición de inventario que cruza esa frontera organizativa se queda esperando. Es exactamente el mecanismo por el que el caso colombiano fue posible.
3. **El fabricante contestó a `E-d` con un folleto.** La pregunta «¿observa usted esto desde el núcleo?» tiene respuesta técnica, pero la ruta comercial devuelve material de marketing. Si no se obtiene respuesta por escrito y técnica, `KJ-3` sigue sin verificar y la organización no sabe si está cubierta.

## O-7. Indicadores y señales de alerta

| # | Indicador observable | Qué señalaría | Disciplina | Responsable |
|---|---|---|---|---|
| I-1 | **Atribución del clúster a un actor conocido por cualquier proveedor** | Cambia `KJ-6`, `H4` y `H5`, y por primera vez permite inferir intención. **Revisión del informe** | OSINT | Célula CTI |
| I-2 | Publicación de otro proveedor sobre SharkLoader | Corrobora de forma independiente el apartado técnico, cuyo techo de confianza hoy lo limita la fuente única | OSINT | Célula CTI |
| I-3 | **Aparición de una carga distinta de Cobalt Strike en esta cadena** | `H7` confirmada: el cargador es plataforma. Degrada toda detección basada en la carga | OSINT · TECHINT | Célula CTI |
| I-4 | Un segundo incidente latinoamericano por vector geoespacial | `KJ-4` pasa de observación a patrón. Eleva `E-b` a prioridad regional | OSINT · CSIRT | Célula CTI |
| I-5 | Ampliación de la lista de vulnerabilidades explotadas | Mantenimiento del Anexo A.1, que es la sección operativa del informe | OSINT · avisos de fabricante | Vulnerabilidades |
| I-6 | Evidencia publicada de exfiltración de datos por este clúster | Resuelve el desequilibrio de `O-3` y decide entre `H1`, `H2` y `H3` | OSINT | Célula CTI |
| I-7 | Aparición de variantes con objetivos de carga lateral nuevos | Amplía `D-2`, que se basa en una lista cerrada de cuatro parejas de aplicación y biblioteca | OSINT · TECHINT | Célula CTI |
| I-8 | Publicación de los indicadores reservados al servicio de inteligencia de la fuente | Cierra la brecha `G-2` y permite un retrohunt con alcance real | OSINT · comercial | Célula CTI |

---

# NIVEL TÁCTICO
### Para: Analistas de SOC · Ingeniería de Detección · Threat Hunting · Horizonte: días–semanas

## T-1. Cadena de intrusión

<!-- cti:stages title="Tres etapas, y la segunda es donde está todo el dinero" dwell="next" -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 01 · Borde | Entrar por donde el parche existía desde hace meses o años | **14 CVE, todas con exploit público** · `CVE-2021-26855` (Exchange, Indonesia) · `CVE-2023-32315` (Openfire, Taiwán) · **`CVE-2024-36401` (GeoServer, Colombia)** · interfaces web de administración remota · alternativa: cuentagotas disfrazados de **Google Update** y **Cisco AnyConnect**, con PDF señuelo |
| Etapa 02 · Carga lateral y evasión | Cuatro ficheros, dos cifrados, nada ejecutable en disco | `SystemSettings.exe` **legítimo**, copiado fuera de su ruta · `SystemSettings.dll` **malicioso** cargado lateralmente · **«Perfect DLL Hijacking»** para soltar el cerrojo del cargador de Windows · `DscCoreR.mui` cifrado con **Blowfish-ECB** · `SyncRes.dat` cifrado con **AES-128** · PE sin cabecera `MZ` · empaquetador propio · carga reflexiva en memoria |
| Etapa 03 · Beacon, y lo que hacen con él | Reconocimiento elemental y credenciales. **Sin exfiltración observada** | **Cobalt Strike Beacon** en hilo suspendido reanudado · `systeminfo`, `ipconfig /all`, `tasklist /svc` · enumeración de Active Directory · `ntdsutil` con instantánea · `procdump` contra el proceso de autenticación local · **FScan, Searchall, Pillager, SharpGPOAbuse** |

**Permanencia:** no publicada. La fuente no da fechas de incidente ni medianas de permanencia, de modo que la ventana de retrohunt de doce meses del Anexo A es convención y no dato: es la brecha `G-4`. **Lo que sí se puede decir sobre tiempos es más revelador que una mediana:** una de las dos tareas programadas que crea el cuentagotas se ejecuta **cada segundo** y se borra al segundo y medio, y la otra se ejecuta **cada cinco minutos** y se queda. Es decir, el adversario quiere ejecución inmediata y después un latido discreto, y eso describe la forma de su impaciencia mejor que cualquier promedio.

**Dónde está el trabajo, y es la observación que ordena toda la defensa.** De las tres etapas, la primera usa exploits que no escribió él, la tercera usa herramientas que tampoco escribió, y **la segunda es enteramente propia y es la más elaborada del expediente**. Eso dice que el adversario no compite en capacidad ofensiva ni en capacidad de recolección: compite en **no ser visto entre una cosa y la otra**. Y tiene una consecuencia defensiva directa: atacarle en la etapa 02 es atacarle donde ha invertido —caro y probablemente infructuoso—, mientras que **las etapas 01 y 03 se defienden con gestión de parches y con detección de red y de Active Directory**, que es trabajo ordinario y bien conocido.

> ⚠ **Sobre «Perfect DLL Hijacking», y por qué no es un detalle de erudición.**
> El cargador de Windows mantiene un cerrojo mientras ejecuta la función de
> inicialización de una biblioteca, y la documentación de Microsoft advierte de
> que crear un hilo desde ahí puede producir un bloqueo. SharkLoader resuelve
> el problema **manipulando las estructuras internas no documentadas del propio
> cargador**: localiza el objeto de sección crítica del cerrojo y la variable
> interna que indica que la inicialización está en curso, libera el cerrojo a
> la fuerza, decrementa esa variable, señaliza el evento de finalización y
> entonces crea su hilo. Windows queda convencido de que la inicialización
> terminó. **Lo relevante para nosotros es lo que eso implica sobre quién lo
> escribió:** la técnica la publicó un investigador independiente en su blog, y
> usarla exige leer ese blog, entender estructuras internas no documentadas y
> depurar un bloqueo que no se reproduce igual en todas las versiones. No es
> código copiado de un foro. **El mismo adversario que usa exploits de prueba
> de concepto ajenos para entrar, escribe esto a mano para no bloquear un
> proceso.** Esa asimetría entre capacidad y pereza es, probablemente, su huella
> más característica.

## T-2. Mapa MITRE ATT&CK

La fuente no publica identificadores de técnica. La tabla es **mapeo propio** sobre su prosa, y así se declara.

<!-- cti:matrix -->

| Táctica | ID | Técnica | Procedimiento observado |
|---|---|---|---|
| Reconocimiento | T1595.002 | Active Scanning: Vulnerability Scanning | **Una de las direcciones asociadas a un dominio de C2 hacía rastreo masivo de Internet**, posiblemente para identificar y explotar sistemas vulnerables a escala |
| Desarrollo de recursos | T1588.005 | Obtain Capabilities: Exploits | La fuente valora con **confianza media** que el actor se apoya principalmente en **exploits de prueba de concepto públicos**, alojados en GitHub y otras plataformas abiertas, en lugar de desarrollar capacidad propia |
| Desarrollo de recursos | T1588.002 | Obtain Capabilities: Tool | Cobalt Strike, FScan, Searchall, Pillager, SharpGPOAbuse, MinHook, Microsoft Detours, `jitasm` |
| Acceso inicial | T1190 | Exploit Public-Facing Application | **Catorce vulnerabilidades**, Anexo A.1. Los tres casos con vector nombrado: Exchange en Indonesia, Openfire en Taiwán, **GeoServer en Colombia** |
| Acceso inicial | T1566.001 | Phishing: Spearphishing Attachment | **Probable, no establecido.** Los cuentagotas llevan PDF señuelo, pero **la fuente declara desconocer cómo se distribuyeron** |
| Ejecución | T1204.002 | User Execution: Malicious File | Cuentagotas que se hacen pasar por instaladores de Google Update y Cisco AnyConnect. **En un caso ejecutan el instalador legítimo de verdad** para que la víctima no sospeche |
| Ejecución | T1059.003 | Windows Command Shell | `cmd.exe /c` para mostrar el PDF señuelo; comandos de reconocimiento |
| Ejecución | T1059.001 | PowerShell | Enumeración de Active Directory con `Get-ADGroupMember` y `Get-ADUser`, con `-exec bypass` |
| Persistencia | T1505.003 | Server Software Component: Web Shell | Tras la explotación, despliegue de interfaces web de administración remota. **La fuente no recuperó los ficheros**, pero los comandos observados y las detecciones los implican |
| Persistencia | T1053.005 | Scheduled Task/Job: Scheduled Task | **Dos tareas creadas por interfaces COM del programador**: una cada cinco minutos que permanece, y otra **cada segundo** que se borra a los 1,5 s. Y, en otro caso, `\Microsoft\Windows\Edge\Edgeupdate` ejecutando como `SYSTEM` a diario |
| Persistencia | T1547.001 | Registry Run Keys / Startup Folder | Clave `Run` creada a mano con el valor `MFUpdate` apuntando a `SystemSettings.exe` en el perfil del usuario |
| Defensa | T1574.002 | Hijack Execution Flow: DLL Side-Loading | **El eje de la cadena.** `SystemSettings.exe` legítimo cargando `SystemSettings.dll` malicioso. Variantes con `msedge.dll`, `PrintDialog.dll` y `miracastview.dll` |
| Defensa | T1574.001 | Hijack Execution Flow: DLL | **«Perfect DLL Hijacking»:** manipulación de `LdrpLoaderLock` y `LdrpWorkInProgress` en `ntdll.dll` para soltar el cerrojo del cargador y crear un hilo desde la inicialización |
| Defensa | T1620 | Reflective Code Loading | Los dos módulos cifrados se descifran y **se cargan reflexivamente en memoria sin escribirse en disco** |
| Defensa | T1027.009 | Obfuscated Files or Information: Embedded Payloads | Beacon y biblioteca de ganchos comprimidos con `zlib` y embebidos en el módulo; PDF señuelo en el recurso `TELEMETRY` del cuentagotas |
| Defensa | T1027.002 | Software Packing | Los PE descifrados están protegidos por **un empaquetador propio no identificado** |
| Defensa | T1140 | Deobfuscate/Decode Files or Information | **Blowfish-ECB** con clave de 16 bytes al principio del fichero para un módulo; **AES-128** con clave e IV de 16 bytes cada uno para el otro |
| Defensa | T1036.005 | Masquerading: Match Legitimate Name or Location | Nombres de tarea que imitan a OneDrive, Edge y Windows Update; **directorios con nombres de proveedores de seguridad**; módulos cifrados con nombres como `NtfsLog.etl`, `diagerr.xml` o `VistaCompat.nls` |
| Defensa | T1562.006 | Impair Defenses: Indicator Blocking | **`EtwEventWrite` devuelve 1; `EventWrite` y `EventWriteEx` devuelven 0.** El registro de eventos del sistema queda anulado en el proceso |
| Defensa | T1562.001 | Impair Defenses: Disable or Modify Tools | **Treinta ganchos de API con Microsoft Detours**, más dos con MinHook sobre reserva de memoria y reposo |
| Defensa | T1106 | Native API | **Construcción en tiempo de ejecución de llamadas directas al núcleo con `jitasm`** para cerca de una veintena de funciones, eludiendo los ganchos en espacio de usuario |
| Defensa | T1134.004 | Access Token Manipulation: Parent PID Spoofing | **Los ganchos de creación de proceso buscan un `svchost.exe` del mismo contexto de seguridad y lo fijan como padre.** Todo lo que lance el Beacon aparece colgando de `svchost.exe` |
| Defensa | T1027.007 | Obfuscated Files or Information: Dynamic API Resolution | Resolución por hash: **ROR13** para `LdrLoadDll`, **Murmur32** para los nombres exportados en el gancho de resolución de funciones |
| Defensa | T1055 | Process Injection | Hilo creado en estado suspendido, *shellcode* escrito en su búfer y reanudación del hilo |
| Defensa | T1480 | Execution Guardrails | **Manejador de excepciones vectorizado** registrado para capturar violaciones de acceso y restaurar permisos de lectura, escritura y ejecución antes de continuar |
| Defensa | **T1055 / evasión de memoria** | *(sin ID específico)* | **El gancho sobre la función de reposo cambia la protección de las regiones del Beacon a sólo lectura y escritura mientras duerme, y la restaura a ejecutable al despertar.** La fuente lo lee como evasión de barrido de memoria en busca de regiones ejecutables |
| Descubrimiento | T1082 | System Information Discovery | `systeminfo`, `ipconfig /all`, `tasklist /svc` |
| Descubrimiento | T1018 | Remote System Discovery | `ping`, `netstat -ano`, `arp -a`, `net share`, `nslookup`, FScan |
| Descubrimiento | T1069.002 | Permission Groups Discovery: Domain Groups | `net group "Domain Controllers" /domain`, `"Enterprise Admins"`, `"domain admins"`, `"Organization Management"` |
| Descubrimiento | T1087.002 | Account Discovery: Domain Account | `Get-ADUser -Filter *`, `dsquery group` encadenado con `dsget`, `quser`, `query user` |
| Descubrimiento | T1083 | File and Directory Discovery | `dir \\c$\inetpub\wwwroot\` y variantes: **búsqueda de la raíz del servidor web**, coherente con el uso de interfaces web de administración |
| Credenciales | T1003.001 | OS Credential Dumping: LSASS Memory | `Procdump64.exe -accepteula -ma lsass.exe` |
| Credenciales | T1003.003 | OS Credential Dumping: NTDS | `ntdsutil "ac i ntds" "ifm" "create full …"` |
| Movimiento lateral | T1484.001 | Domain Policy Modification: Group Policy Modification | **SharpGPOAbuse** |
| Mando y control | T1071.001 | Application Layer Protocol: Web Protocols | Cobalt Strike Beacon. Cuatro dominios, tres de ellos suplantando nomenclatura de Microsoft |
| Mando y control | T1219 | Remote Access Tools | **Cobalt Strike.** Herramienta legítima de pruebas de intrusión: **su presencia no atribuye** |

> **Cuatro filas de esta tabla son la razón de ser del informe**, y conviene
> verlas juntas: `T1562.006` anula el registro de eventos; `T1106` con `jitasm`
> construye llamadas directas al núcleo para saltar los ganchos del producto de
> seguridad; `T1134.004` falsifica el padre a `svchost.exe`; y el gancho sobre
> la función de reposo devuelve la memoria a no ejecutable mientras duerme.
> **Cada una neutraliza un sensor distinto de los cuatro que un EDR moderno usa
> para encontrar precisamente esto.** No hay quinto truco porque no hace falta.

## T-3. Dónde atacamos en la Pirámide del Dolor

<!-- cti:pyramid -->

| Nivel | Qué contiene en este informe y qué vale | Valor |
|---|---|---|
| Hashes | Siete MD5 en el anexo de indicadores de la fuente, más dos que sólo aparecen en el cuerpo de su informe, y **sólo MD5**: ni SHA-1 ni SHA-256. Subconjunto declaradamente parcial. Valor preventivo nulo, **y además la fuente advierte que su visibilidad es limitada**. Solo retrohunt | Base · valor trivial |
| IP · Dominios | Cuatro dominios, tres suplantando nomenclatura de Microsoft. **Bloqueables y vale la pena bloquearlos**, pero son cuatro y la campaña es global: la cobertura es simbólica | Valor bajo |
| Artefactos | **Aquí está, excepcionalmente, el nivel más rentable de todo el expediente**, y por un motivo estructural: la evasión de `KJ-2` es **intraproceso** y no puede ocultar nada de lo que ocurre antes de que el proceso exista. Los nombres de tarea programada, la disposición de cuatro ficheros en un directorio del perfil, `SystemSettings.exe` fuera de su ruta y los nombres de directorio de proveedores de seguridad **son invisibles para todas las técnicas de `X-3.1`** | Valor medio · **el nivel que el adversario no puede tocar** |
| Herramientas | Cobalt Strike, FScan, Searchall, Pillager, SharpGPOAbuse, Microsoft Detours, MinHook, `ntdsutil`, `procdump`, `dsquery`: **todas públicas o legítimas**, y la mitad son binarios firmados por Microsoft o utilidades administrativas. Detectar por contexto, nunca por presencia | Valor alto |
| TTP | **Dos, y la segunda es la que importa.** (1) **Carga lateral de biblioteca sobre aplicación legítima copiada fuera de su ruta**, que es estable en todas las variantes. (2) **La anulación del registro de eventos del sistema**, que es la TTP de más valor porque se detecta por su ausencia: un proceso que deja de emitir trazas y sigue vivo es anómalo, y eso lo ve el **recolector remoto**, no el equipo | Cima · valor máximo |

> **La conclusión de esta pirámide invierte la doctrina y conviene razonarla.**
> Normalmente el consejo es subir: cuanto más arriba, más cuesta al adversario
> cambiarlo. Aquí hay un matiz distinto y más fuerte: **no es que al adversario
> le cueste cambiar los artefactos del tercer nivel, es que no puede ocultarlos
> con las herramientas que tiene**. Toda su maquinaria de evasión vive dentro de
> un proceso ya en ejecución; las tareas programadas, los ficheros en disco y
> el nombre del directorio existen **antes** y **fuera**. Es una ventana que el
> diseño del adversario deja abierta por construcción, no por descuido, y es
> donde `D-1` y `D-2` entran. **Y la cima, en este caso, no es un
> comportamiento que detectar sino un silencio que notar**, lo que exige
> recolección remota y no detección local.

## T-4. Hipótesis de caza prioritarias

<!-- cti:accordion critical="^(H-1|H-2|H-3)\b" regional="^H-1[0-2]\b" -->

**H-1 — Hay una tarea programada que imita el nombre de un actualizador y apunta al perfil del usuario.** La caza de mejor relación entre coste y conclusión del informe, y la que la evasión del adversario no puede tocar. Volcar todas las tareas programadas del parque y buscar: nombres que empiecen por `OneDrive Standalone Update Task` seguidos de un identificador de seguridad; nombres del tipo `MicrosoftUpdateTaskUser` con identificador; cualquier tarea bajo `\Microsoft\Windows\Edge\` que no haya creado el navegador; y, lo más generalizable, **cualquier tarea cuya acción apunte a un ejecutable situado en `%APPDATA%`, `%LOCALAPPDATA%`, `%ProgramData%` o la raíz de `C:\`**. Discriminador adicional de altísimo valor: **una tarea con disparador de repetición cada minuto o menos**; la que crea este cuentagotas se ejecuta **cada segundo** y, aunque se borre a los 1,5 s, la creación queda registrada. Fidelidad: muy alta. Falsos positivos: algunos actualizadores de terceros instalados en el perfil; se enumeran una vez. Ventana: el estado actual más el histórico de creación de tareas que haya.

**H-2 — Existe un `SystemSettings.exe` fuera de su sitio, con una biblioteca y dos ficheros cifrados al lado.** La firma estructural de la cadena, y es una **disposición de directorio**, no un fichero. Buscar cualquier `SystemSettings.exe` cuya ruta no sea `C:\Windows\ImmersiveControlPanel\`; en particular bajo `%APPDATA%\xwreg`, `%APPDATA%\xgdf`, `%APPDATA%\Identities`, `C:\ProgramData\` y rutas del tipo `C:\ADriveLogs_Logs\`. Y, de forma más robusta que los nombres literales: **un directorio que contenga a la vez un ejecutable firmado por Microsoft y una biblioteca del mismo nombre sin firma o con firma distinta**. Extender la búsqueda a las otras tres parejas conocidas: `msedge.dll`, `PrintDialog.dll` y `miracastview.dll` acompañando a sus aplicaciones legítimas respectivas. Fidelidad: muy alta para la pareja firmada/no firmada. Falsos positivos: aplicaciones portables mal empaquetadas; son pocas y se enumeran.

**H-3 — Un proceso dejó de emitir trazas al registro de eventos del sistema y sigue vivo.** La caza que corresponde a la cima de `T-3`, y la única que detecta la evasión en lugar de rodearla. No se busca un evento: **se busca una ausencia**. En un recolector remoto, identificar procesos de larga duración que emitieron trazas y dejaron de emitirlas sin terminar; y, más fácil de operacionalizar, **caídas abruptas del volumen de eventos por equipo** comparadas con su propia línea base. Fidelidad: media, y depende enteramente de que la recolección sea remota y en tiempo real —es `E-e`—. Falsos positivos: cambios de configuración de auditoría, actualizaciones del agente, problemas de red. **Su valor no es la precisión: es que es la única señal que el adversario produce al defenderse.**

**H-4 — Hay un proceso cuyo padre es `svchost.exe` y no debería serlo.** El gancho de creación de proceso fija como padre un `svchost.exe` del mismo contexto de seguridad. Cazar: procesos hijos de `svchost.exe` que no pertenezcan al conjunto corto y conocido de lo que ese proceso legítimamente lanza —y en particular `cmd.exe`, `powershell.exe`, `net.exe`, `nltest.exe`, `dsquery.exe`, `whoami.exe`, `procdump*.exe`, `ntdsutil.exe`—. Fidelidad: alta; es un patrón bien conocido y la lista blanca de hijos legítimos de ese proceso está documentada. **Y un matiz que hace esta caza mejor de lo que parece:** la falsificación de padre engaña a la telemetría de *relación*, pero no al *contenido* de la línea de comandos. Un `svchost.exe` cuyo hijo ejecuta `net group "Enterprise Admins" /domain` es un hallazgo con independencia de lo que diga el árbol.

**H-5 — Alguien volcó el proceso de autenticación local o la base del directorio.** Caza clásica y aquí especialmente rentable, porque es la única actividad posterior al compromiso que la fuente documenta con certeza. Buscar `procdump` —con cualquier nombre— con argumentos que incluyan volcado completo contra el proceso de autenticación local; `ntdsutil` con creación de instantánea e `ifm`; y accesos de lectura al proceso de autenticación por procesos no autorizados. Fidelidad: muy alta. Falsos positivos: equipos de soporte que diagnostican con volcados; raro y se enumera.

**H-6 — Hay un directorio con el nombre de un proveedor de seguridad que ese proveedor no creó.** Pequeña, concreta y de falso positivo prácticamente nulo. La fuente observó al actor usando nombres de fabricantes de seguridad como nombres de directorio de trabajo, presumiblemente para parecer legítimos — y cita el caso de un directorio con el nombre de un fabricante de antivirus bajo `C:\ProgramData\` y bajo `%APPDATA%`. Cazar: enumerar en todo el parque los directorios bajo `%ProgramData%` y `%APPDATA%` cuyo nombre coincida con el de cualquier fabricante de seguridad —**incluido el nuestro**— y contrastar con lo que ese producto crea realmente. Fidelidad: muy alta. **Es la caza más barata del informe y la que mejor ilustra que un adversario muy competente técnicamente puede ser predecible en lo humano.**

**H-7 — Hay ficheros con nombres de artefacto del sistema en rutas donde el sistema no los pone.** Los módulos cifrados se llaman `DscCoreR.mui`, `SyncRes.dat`, `GameInputInboxs32.mui`, `diagerr.xml`, `NtfsLog.etl`, `Ignored.Dat` y `VistaCompat.nls`: nombres plausibles de registro, caché o localización de Windows. Cazar esos nombres fuera de las rutas del sistema, **y el patrón generalizable: un fichero con extensión de datos o de registro cuyos primeros 16 o 32 bytes sean de alta entropía seguidos de más alta entropía**, que es la estructura de clave-más-cifrado que la fuente documenta. Fidelidad: alta para los nombres literales, media para el patrón de entropía.

**H-8 — Hubo una interfaz web de administración remota en un servidor expuesto.** La fuente no recuperó los ficheros, pero el patrón de comandos sí. Cazar en los servidores web expuestos: ficheros nuevos o modificados bajo la raíz del servidor en los últimos doce meses; procesos hijos del proceso del servidor web que sean intérpretes de comandos; y, en particular, la secuencia observada de copiar una aplicación legítima de Windows a otra ruta y ejecutarla desde allí. Fidelidad: alta. **Ésta es la caza que cierra el círculo con `E-a`:** si hay una interfaz de administración remota, la vulnerabilidad del Anexo A.1 ya se explotó.

**H-9 — Se resolvió alguno de los cuatro dominios, o se ejecutó alguno de los siete hashes.** Retrohunt convencional con el Anexo A.3 y A.2, doce meses. **Y hay que registrar el resultado negativo con su limitación**, que aquí es doble: el subconjunto publicado es parcial por declaración de la fuente, y su visibilidad se limita a su propia telemetría. Fidelidad: alta para el acierto, **nula como prueba de ausencia**.

**H-10 — ¿Tenemos un GeoServer, y lo sabíamos?** Caza de alcance regional, la más importante de este informe para la región, y no se hace en el SIEM sino en el inventario y con un escaneo externo. Buscar: instancias de GeoServer, servidores de mapas, nodos de infraestructura de datos espaciales, visores catastrales y pasarelas de servicios geográficos. Comprobar versión frente a `CVE-2024-36401`. **Y la pregunta que importa más que la versión: quién lo administra.** Si la respuesta es un área de cartografía, de catastro o de medio ambiente en lugar del área de sistemas, es muy probable que no esté en el ciclo de parcheo ni en el inventario de aplicaciones, y es el escenario exacto del caso colombiano. Fidelidad: no aplica; es un ejercicio de inventario. **Nota de contexto regional:** este componente es ubicuo en la administración pública latinoamericana precisamente porque es bueno y es libre, y por eso mismo suele estar fuera de los procesos que cubren el software adquirido.

**H-11 — Caza por la lista completa de trece, con prioridad por lo que de verdad tenemos.** Variante de alcance regional de `E-a`. No se trata de parchear trece cosas, sino de cruzar trece con nuestro inventario y actuar sobre la intersección. Y hay un atajo de prioridad: `CVE-2023-20198` de Cisco IOS XE **ya está en esta cartera por otro actor** (`CTI-2026-030`), lo que significa que dos clústeres sin relación entre sí entran por esa puerta. **Cuando dos adversarios independientes usan la misma vulnerabilidad, su prioridad de parcheo no es la suma de las dos: es mayor**, porque el parche cierra dos expedientes.

**H-12 — ¿Algún proveedor nuestro de desarrollo de software ha tenido un incidente?** Caza de alcance regional que se hace preguntando. Tres de las víctimas identificadas son **empresas de desarrollo de software**, y la fuente plantea que el interés podría ser propiedad intelectual. Para una organización que subcontrata desarrollo, una empresa de desarrollo comprometida es acceso a su código y a sus entornos. Revisar qué proveedores de esa categoría tenemos, y qué dice el contrato sobre notificación. Fidelidad: no aplica.

## T-5. Brechas de visibilidad que hay que cerrar primero

| Brecha | Por qué importa aquí |
|---|---|
| **Sin inventario de los componentes geoespaciales** | Deja ciega `H-10` y es el escenario literal del caso colombiano. **No es una brecha de seguridad: es una brecha de inventario**, y por eso la cierra TI y no el SOC |
| **Recolección de registro de eventos local y no remota** | Deja ciega `H-3`, que es la única caza que detecta la evasión. Si el consumidor de trazas está en el mismo equipo, la anulación es perfecta e invisible | 
| Sin volcado periódico del estado del programador de tareas | Deja ciegas `H-1` y la mitad de `H-2`. Es el nivel que el adversario no puede ocultar, y renunciar a él es renunciar a lo único gratis del expediente |
| Sin telemetría de creación de fichero y de firma en rutas de perfil | Deja ciegas `H-2`, `H-6` y `H-7`. El discriminador de `H-2` es **la firma**, no el nombre |
| Sin detección de red de Cobalt Strike independiente del endpoint | Deja la detección de la etapa 03 enteramente en manos del endpoint, que es precisamente donde el adversario invirtió. **Es la brecha más grave en términos de arquitectura** |
| EDR con observación en espacio de usuario y no en el núcleo | Si es el caso, `X-3.1` describe una neutralización completa y no parcial. **No lo sabemos hasta preguntar: es `E-d`** |
| Sin escaneo externo propio y recurrente | Deja `E-a` dependiendo de que el inventario esté bien, que nunca lo está. **Un clúster que encuentra víctimas rastreando Internet se defiende rastreándose uno mismo primero** |
| Sin registro de línea de comandos en servidores | Deja ciegas `H-5` y `H-8`. En los servidores expuestos es donde empieza todo y donde el registro suele ser más pobre |

---

# NIVEL TÉCNICO
### Para: Ingeniería de detección · Automatización · TIP/SIEM · Vida útil: días–semanas

## X-1. Arsenal y capacidad

| Propiedad | Valor |
|---|---|
| Componentes de la cadena | **Cuatro ficheros.** `SystemSettings.exe` (legítimo de Windows, abusado); `SystemSettings.dll` (cargador principal); `DscCoreR.mui` (módulo cifrado con el Beacon y MinHook embebidos); `SyncRes.dat` (módulo cifrado que instala los ganchos) |
| Objetivos de carga lateral alternativos | `msedge.dll` · `PrintDialog.dll` · `miracastview.dll`, cada uno con su aplicación legítima correspondiente |
| Nombres alternativos de módulo cifrado | `GameInputInboxs32.mui` · `diagerr.xml` · `NtfsLog.etl` · `Ignored.Dat` · `VistaCompat.nls` |
| Cifrado del primer módulo | **Blowfish en modo ECB**, con **P-array y S-box propios** embebidos en el cargador, y clave de 16 bytes **al principio del propio fichero** |
| Cifrado del segundo módulo | **AES-128**, con clave de 16 bytes en los primeros 16 bytes del fichero e **IV** en los 16 siguientes |
| Antianálisis de los PE | **Cabecera `MZ` eliminada** en los dos módulos descifrados, más **empaquetador propio no identificado** |
| Funciones exportadas de entrada | `SetUserProcessPriorityBoost` (primer módulo) · `StartEngineData` (segundo módulo) |
| Escape del cerrojo del cargador | **«Perfect DLL Hijacking»:** resolución de `LdrpLoaderLock` y `LdrpWorkInProgress` en `ntdll.dll`, `LeaveCriticalSection`, `InterlockedDecrement64`, `SetEvent`, y entonces `CreateThread` |
| Biblioteca de ganchos | **Microsoft Detours**, con `DetourTransactionCommitEx` para aplicar todos los desvíos en una sola confirmación |
| Segunda biblioteca de ganchos | **MinHook**, comprimida con `zlib` dentro del primer módulo; `MH_Initialize` y `MH_CreateHook` sobre reserva de memoria y reposo |
| Llamadas directas al núcleo | **Construidas en tiempo de ejecución con `jitasm`** para cerca de una veintena de funciones |
| Resolución de funciones por hash | **ROR13** para `LdrLoadDll`; **Murmur32** sobre la tabla de exportaciones en el gancho de resolución |
| Falsificación de proceso padre | Localiza un `svchost.exe` del **mismo contexto de seguridad**, construye una lista extendida de atributos de arranque y lo fija como padre. Dos variantes: por hilo dedicado y **por llamada asíncrona en cola con temporizador** |
| Anulación de trazas | `EtwEventWrite` → devuelve 1 · `EventWrite` → devuelve 0 · `EventWriteEx` → devuelve 0 |
| Evasión de barrido de memoria | El gancho sobre la función de reposo cambia las regiones del Beacon a **sólo lectura y escritura** antes de dormir y las restaura a **ejecutable** al despertar. Rastrea las tres primeras reservas de memoria con éxito |
| Manejador de excepciones | **VEH** registrado para violaciones de acceso `0xC0000005`: restaura permisos de lectura, escritura y ejecución en la página fallida y continúa. **La fuente no observó ninguna activación** |
| Carga final | **Cobalt Strike Beacon**, comprimido con `zlib`, descomprimido en el búfer de un hilo suspendido que se reanuda |
| Herramientas de post-explotación | FScan · Searchall · Pillager · SharpGPOAbuse · `ntdsutil` · `procdump` · utilidades nativas de directorio |

### X-1.1 — Lo que no hay, y es informativo

No hay: canal de exfiltración propio; módulo de recolección de ficheros, de pantalla, de teclado o de navegador; componente de cifrado o destructivo; mecanismo de actualización propio; comunicación propia con el operador —todo va por el Beacon—; ni persistencia integrada en el implante, que la fuente señala expresamente y que el actor resuelve **a mano**, con una clave de registro o una tarea programada, caso por caso.

**Un cargador sin ninguna de esas cosas no es un implante de espionaje: es un vehículo.** Toda su masa de código está dedicada a poner en memoria una herramienta de terceros sin que nadie lo vea, y después se aparta. Eso encaja con las tres hipótesis de `O-3` y no discrimina entre ellas, pero sí tiene una consecuencia defensiva que conviene aprovechar: **todo lo que el adversario haga de valor pasa por el Beacon**, y el Beacon es detectable en red por métodos que no dependen del endpoint. Es `E-h` y `D-5`.

## X-2. Artefactos de host persistentes

<!-- cti:cards -->

| Categoría | Artefactos | Etiqueta |
|---|---|---|
| **Tareas programadas** | `OneDrive Standalone Update Task-S-1-5-21-4165425321-4153752593-2322023643-1000` (cada 5 min, permanece) · `MicrosoftUpdateTaskUserS-1-5-32-2456537112-101246289-228944324-1000` (**cada segundo**, se borra a los 1,5 s) · `\Microsoft\Windows\Edge\Edgeupdate` (diaria, como `SYSTEM`) | `el nivel que la evasión no alcanza` |
| **Clave de registro** | `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`, valor `MFUpdate`, dato `$appdata\Identities\SystemSettings.exe` | `creada a mano, con `reg add`` |
| **Directorios de trabajo** | `%APPDATA%\xwreg` · `%APPDATA%\xgdf` · `%APPDATA%\Identities` · `C:\ProgramData\` · `C:\ADriveLogs_Logs\` · **`C:\ProgramData\<nombre de fabricante de seguridad>\`** | `el último es el mejor` |
| **Disposición delatora** | Un directorio con **un ejecutable firmado por Microsoft y una biblioteca homónima sin su firma**, más **dos ficheros de alta entropía** con nombres de artefacto del sistema | `la firma estructural, no un nombre` |
| **Señuelo** | PDF escrito en `%TEMP%\aswerf\` o directamente en `%TEMP%`, con **el mismo nombre que el cuentagotas** y extensión `.pdf`, lanzado con `cmd.exe /c` | `el directorio `aswerf` es muy específico` |
| **Recursos del cuentagotas** | Nombres de recurso `TELEMETRY` (PDF señuelo), `VAULTSVCD` y `UMRDPRDAT` (módulos cifrados), todos comprimidos con `zlib` | `para análisis de muestras` |
| **Rastro de la instalación** | `copy SystemSettings.exe` desde `C:\Windows\ImmersiveControlPanel\`; `%APPDATA%\reports\AnyConnect-win-4.msi` en el caso del señuelo de VPN | `la copia es el momento visible` |

## X-3. Lógica de detección prioritaria

### X-3.1 — Antes de las reglas: la lista que hay que llevar al fabricante

Esta subsección no contiene detecciones. Contiene **la conversación de `E-d`**, en forma de tabla, porque de su resultado depende si las reglas de `X-3.2` son el control principal o un refuerzo.

| Técnica del cargador | Qué sensor neutraliza | Pregunta exacta al fabricante |
|---|---|---|
| Treinta ganchos con Microsoft Detours en espacio de usuario | Los ganchos del propio EDR en espacio de usuario, si están en el mismo sitio | ¿Dónde observa usted las llamadas a la interfaz de Windows: en espacio de usuario o en el núcleo? |
| **Llamadas directas al núcleo construidas con `jitasm`** | Cualquier observación que dependa de que la llamada pase por la biblioteca del sistema | ¿Detecta usted llamadas al núcleo que **no** provienen de la biblioteca del sistema, por procedencia de la dirección de retorno? |
| **`EtwEventWrite`, `EventWrite` y `EventWriteEx` anulados** | La traza del registro de eventos del sistema como fuente de telemetría | ¿Depende alguna de sus detecciones de esa traza? ¿Detecta usted que un proceso **deja de emitirla**? |
| **Protección de memoria cambiada a no ejecutable durante el reposo** | El barrido de memoria en busca de regiones ejecutables anómalas | ¿Con qué periodicidad barre memoria y **cómo trata una región que alterna permisos**? |
| **Falsificación del proceso padre a `svchost.exe`** | El árbol de procesos como fuente de contexto | ¿Reconstruye usted la paternidad real, o usa el atributo declarado en la creación? |
| Carga reflexiva de PE sin cabecera `MZ`, con empaquetador propio | La detección de módulos cargados en memoria | ¿Detecta usted imágenes PE mapeadas que **no** corresponden a un fichero en disco? |
| **Manipulación de `LdrpLoaderLock`** | La integridad de las estructuras internas del cargador | ¿Vigila usted modificaciones de las estructuras internas del cargador de Windows? |
| Resolución de funciones por hash ROR13 y Murmur32 | Las detecciones basadas en cadenas de nombres de API | *(informativa; no suele haber sensor específico)* |

> ⚠ **Cómo hacer esta pregunta para que sirva.** Por escrito, nominalmente, y
> pidiendo respuesta técnica por fila. Un «nuestra plataforma detecta técnicas
> avanzadas de evasión» no responde a ninguna de las ocho. **Y una advertencia
> de buena fe:** es perfectamente posible que el producto cubra la mayoría de
> ellas, y en ese caso la respuesta es una buena noticia documentada, que vale
> igual. El objetivo no es acusar al fabricante: es **dejar de suponer**.

### X-3.2 — Las reglas

<!-- cti:detections -->

**D-1 · CRÍTICO — Tarea programada con nombre de actualizador apuntando al perfil del usuario**

```
event.action IN ("scheduled_task_create","scheduled_task_modify")  // EID 4698/4702
AND (
  task.action.path MATCHES "(?i)(\\\\AppData\\\\|\\\\ProgramData\\\\|^C:\\\\[^\\\\]+\\\\[^\\\\]+\\.exe$)"
  OR task.name MATCHES "(?i)^OneDrive Standalone Update Task-S-1-5-"
  OR task.name MATCHES "(?i)^MicrosoftUpdateTaskUser"
  OR (task.name MATCHES "(?i)^\\\\Microsoft\\\\Windows\\\\(Edge|UpdateOrchestrator)\\\\"
      AND task.action.path NOT MATCHES "(?i)^C:\\\\Program Files")
)
OR task.trigger.repetition_interval <= 60   // segundos
```

→ **Alerta crítica e investigación del equipo.** Es la detección de mayor valor del informe por una razón estructural: **toda la evasión de `X-3.1` es intraproceso y no alcanza al programador de tareas**. La última condición —repetición de un minuto o menos— es especialmente estrecha: ningún actualizador legítimo se ejecuta cada segundo, y la tarea que lo hace **queda registrada en su creación aunque se borre segundo y medio después**.

**D-2 · CRÍTICO — Binario firmado por Microsoft con biblioteca homónima no firmada en el mismo directorio**

```
process.start
WHERE process.code_signature.subject CONTAINS "Microsoft"
  AND process.executable NOT MATCHES "(?i)^C:\\\\(Windows|Program Files)"
  AND EXISTS dll IN process.loaded_modules
      WHERE dll.name == basename(process.executable, ".exe") + ".dll"
        AND dll.directory == process.directory
        AND (dll.code_signature.exists == false
             OR dll.code_signature.subject != process.code_signature.subject)
```

→ **Aislamiento del equipo y recogida de todo el directorio, no sólo del binario.** Esta regla es más general que el expediente: **detecta la carga lateral de biblioteca como clase**, con independencia de la pareja concreta, y por tanto cubre las cuatro variantes conocidas y las que vengan. **Recoger el directorio completo es parte de la acción**: los dos ficheros cifrados son el objeto de análisis y sin ellos no hay caso.

**D-3 · ALTO — `SystemSettings.exe`, o cualquiera de las tres parejas conocidas, fuera de su ruta**

```
(process.name == "SystemSettings.exe"
 AND process.executable NOT MATCHES "(?i)^C:\\\\Windows\\\\ImmersiveControlPanel\\\\")
OR (file.name IN ("SystemSettings.dll","msedge.dll","PrintDialog.dll","miracastview.dll")
    AND file.path MATCHES "(?i)(\\\\AppData\\\\|\\\\ProgramData\\\\|^C:\\\\[^\\\\]+\\\\)")
OR (file.name IN ("DscCoreR.mui","SyncRes.dat","SyncRest.dat","GameInputInboxs32.mui",
                  "diagerr.xml","NtfsLog.etl","Ignored.Dat","VistaCompat.nls")
    AND file.path NOT MATCHES "(?i)^C:\\\\Windows\\\\")
```

→ **Alerta alta y recogida.** Versión literal y de despliegue inmediato de `D-2`. **Caduca** cuando el actor cambie de pareja o de nombres, mientras `D-2` no; se despliegan las dos y la segunda es la que se mantiene.

**D-4 · ALTO — Directorio con nombre de fabricante de seguridad no creado por ese producto**

```
file.action == "directory_create"
AND file.path MATCHES "(?i)\\\\(ProgramData|AppData\\\\Roaming)\\\\(kaspersky\w*|eset|bitdefender|sophos|trendmicro|mcafee|symantec|crowdstrike|sentinelone|fortinet|avast|avg|norton|panda|malwarebytes|withsecure|<nuestro producto>)"
AND NOT process.code_signature.subject MATCHES "(?i)(ese mismo fabricante)"
```

→ **Alerta alta.** Falso positivo prácticamente nulo y coste de implantación mínimo. **Incluir el nombre del producto propio en la lista**: un directorio con el nombre de nuestro antivirus creado por algo que no es nuestro antivirus es el hallazgo más limpio posible.

**D-5 · CRÍTICO — Cobalt Strike en la red, con independencia del endpoint**

```
// Esta deteccion NO vive en el endpoint, y es el punto del informe.
network.beacon_analysis
WHERE flow.periodicity_jitter_profile MATCHES "cobalt_strike_sleep_pattern"
   OR tls.ja3s IN <perfiles de servidor conocidos de la herramienta>
   OR http.uri MATCHES <patrones de perfil maleable publicos conocidos>
   OR dns.question.name IN <A.3>
```

→ **Alerta crítica con escalado inmediato.** Es la contramedida arquitectónica que corresponde a `KJ-2` y `KJ-3`: **todo lo que este adversario haga de valor pasa por el Beacon, y la red es el único punto de observación que su evasión no puede tocar**. La detección de perfiles maleables es una carrera y no se gana siempre, pero **la periodicidad de las comunicaciones es más difícil de ocultar que el contenido**, y es donde conviene invertir.

**D-6 · ALTO — Reconocimiento de Active Directory en secuencia**

```
SAME host WITHIN 30m, count(distinct match) >= 3 OF:
  process.command_line CONTAINS_ANY (
    "net group \"Domain Controllers\"", "net group \"Enterprise Admins\"",
    "net group \"domain admins\"", "net group \"Organization Management\"",
    "Get-ADGroupMember", "Get-ADUser -Filter *", "dsquery group",
    "quser", "query user", "nltest /domain_trusts", "net share", "arp -a")
```

→ **Alerta alta.** Cada comando por separado tiene uso administrativo legítimo; **tres o más en media hora desde el mismo equipo, no**. Y conviene recordar `H-4`: esta detección funciona por **contenido** de la línea de comandos, de modo que la falsificación del proceso padre no la afecta.

**D-7 · CRÍTICO — Volcado de credenciales**

```
(process.command_line MATCHES "(?i)ntdsutil.*\"?ac i ntds\"?.*ifm")
OR (process.command_line MATCHES "(?i)-ma\\s+lsass"
    OR (process.command_line CONTAINS "lsass" AND process.command_line CONTAINS "-accepteula"))
OR (process.target.name == "lsass.exe" AND process.access.mask IN (0x1010, 0x1410, 0x143a)
    AND process.name NOT IN <lista blanca nominal>)
```

→ **Contención automática.** Es la única actividad posterior al compromiso que la fuente documenta con certeza, y marca el punto en que el incidente deja de ser un equipo y pasa a ser el dominio.

**D-8 · MEDIO — Intérprete lanzado por el proceso del servidor web**

```
process.parent.name IN ("w3wp.exe","httpd.exe","nginx.exe","java.exe","tomcat*.exe",
                        "php-cgi.exe","openfire-service.exe")
AND process.name IN ("cmd.exe","powershell.exe","net.exe","whoami.exe","reg.exe",
                     "schtasks.exe","certutil.exe","bitsadmin.exe","curl.exe")
```

→ **Alerta media, y alta si el servidor está expuesto a Internet.** Es la detección de la interfaz web de administración remota de `H-8`, y la que convierte una explotación del Anexo A.1 en un evento observable. **Incluir el proceso de Openfire y el de Java en la lista** no es decorativo: dos de los tres vectores nombrados por la fuente corren sobre esas plataformas.

> ⚠ **Regla de operación, y aquí hay una conclusión de arquitectura.** Dos
> detecciones admiten contención automática: `D-7`, por el valor de lo que está
> en juego, y `D-2`, por su fidelidad. Pero la regla más importante de esta
> sección no es sobre automatización: **ninguna de las detecciones que de
> verdad protegen contra este expediente vive en el mismo lugar donde el
> adversario ha concentrado su evasión.** `D-1` está en el programador de
> tareas, `D-2` y `D-3` en el sistema de ficheros antes de la ejecución, `D-5`
> en la red, `D-8` en el servidor web. **Si la respuesta de `E-d` resulta ser
> que el EDR observa en espacio de usuario, estas cinco son la defensa
> completa**, y conviene saberlo antes de necesitarlo.

## X-4. Consultas de caza

```kql
// H-1 y D-1 · Tareas programadas con nombre de actualizador apuntando al perfil.
// El nivel que la evasion del cargador NO alcanza: todo lo suyo es intraproceso.
DeviceEvents
| where Timestamp > ago(365d)
| where ActionType in ("ScheduledTaskCreated","ScheduledTaskUpdated")
| extend Tarea = tostring(AdditionalFields.TaskName),
         Accion = tostring(AdditionalFields.TaskContent)
| where Tarea startswith "OneDrive Standalone Update Task-S-1-5-"
     or Tarea startswith "MicrosoftUpdateTaskUser"
     or Tarea has @"\Microsoft\Windows\Edge\"
     or Accion has_any (@"\AppData\", @"\ProgramData\", "ADriveLogs")
| project Timestamp, DeviceName, Tarea, Accion, InitiatingProcessFileName,
          InitiatingProcessCommandLine, InitiatingProcessAccountName
| order by Timestamp desc
```

```kql
// H-2 y D-3 · SystemSettings.exe fuera de su ruta, y las cuatro parejas conocidas.
union
( DeviceProcessEvents
  | where Timestamp > ago(365d)
  | where FileName =~ "SystemSettings.exe"
  | where not(FolderPath startswith @"C:\Windows\ImmersiveControlPanel")
  | project Timestamp, DeviceName, Senal = "exe fuera de ruta", FolderPath,
            SHA256, InitiatingProcessFileName, AccountName
),
( DeviceFileEvents
  | where Timestamp > ago(365d)
  | where FileName in~ ("SystemSettings.dll","msedge.dll","PrintDialog.dll","miracastview.dll",
                        "DscCoreR.mui","SyncRes.dat","SyncRest.dat","GameInputInboxs32.mui",
                        "diagerr.xml","NtfsLog.etl","Ignored.Dat","VistaCompat.nls")
  | where not(FolderPath startswith @"C:\Windows\")
  | project Timestamp, DeviceName, Senal = strcat("componente: ", FileName), FolderPath,
            SHA256, InitiatingProcessFileName, AccountName = InitiatingProcessAccountName
)
| order by Timestamp desc
```

```kql
// H-6 y D-4 · Directorio con nombre de fabricante de seguridad.
// La caza mas barata del informe. Incluir el nombre del producto PROPIO.
DeviceFileEvents
| where Timestamp > ago(365d)
| where FolderPath matches regex
    @"(?i)\\(ProgramData|AppData\\Roaming)\\(kaspersky\w*|eset|bitdefender|sophos|trendmicro|mcafee|symantec|crowdstrike|sentinelone|fortinet|avast|avg|norton|panda|malwarebytes|withsecure)"
| summarize Ficheros = make_set(FileName, 20), Primero = min(Timestamp), Ultimo = max(Timestamp),
            Creadores = make_set(InitiatingProcessFileName, 10)
         by DeviceName, FolderPath
| order by Primero desc
// Contrastar 'Creadores' con el proceso real del producto de ese fabricante.
```

```kql
// H-4 · Hijos anomalos de svchost.exe. La falsificacion de padre engana al arbol,
// NO al contenido de la linea de comandos.
DeviceProcessEvents
| where Timestamp > ago(180d)
| where InitiatingProcessFileName =~ "svchost.exe"
| where FileName in~ ("cmd.exe","powershell.exe","pwsh.exe","net.exe","net1.exe",
                      "nltest.exe","dsquery.exe","whoami.exe","ntdsutil.exe",
                      "reg.exe","schtasks.exe","certutil.exe","systeminfo.exe")
| project Timestamp, DeviceName, AccountName, FileName, ProcessCommandLine,
          InitiatingProcessCommandLine
| order by Timestamp desc
```

```kql
// H-5 y D-7 · Volcado de credenciales: lo unico que la fuente documenta con certeza.
DeviceProcessEvents
| where Timestamp > ago(365d)
| where ProcessCommandLine matches regex @"(?i)ntdsutil.*ac i ntds.*ifm"
     or (ProcessCommandLine has "lsass" and ProcessCommandLine has_any ("-ma","-accepteula","--dump"))
| project Timestamp, DeviceName, AccountName, FileName, ProcessCommandLine,
          InitiatingProcessFileName, InitiatingProcessCommandLine
| order by Timestamp desc
```

```kql
// H-3 · El silencio. Caida abrupta de volumen de eventos por equipo.
// Solo funciona si la recoleccion es REMOTA y en tiempo real (E-e).
let ventana = 7d;
let base = DeviceEvents
  | where Timestamp between (ago(60d) .. ago(ventana))
  | summarize Media = count() / 53.0 by DeviceName;
DeviceEvents
| where Timestamp > ago(ventana)
| summarize Reciente = count() / 7.0 by DeviceName
| join kind=inner base on DeviceName
| extend Caida = 1.0 - (Reciente / Media)
| where Media > 50 and Caida > 0.7
| project DeviceName, Media = round(Media,1), Reciente = round(Reciente,1),
          CaidaPorcentual = round(Caida*100,1)
| order by CaidaPorcentual desc
// Un equipo vivo que deja de emitir trazas es la unica senal que este
// adversario produce AL DEFENDERSE. Falsos positivos: cambios de auditoria,
// actualizaciones de agente, equipos apagados. Revisar los tres antes de alertar.
```

```yaml
# Sigma — Carga lateral de biblioteca sobre binario firmado fuera de su ruta
title: Binario de Microsoft fuera de ruta con biblioteca homonima no firmada
id: 7e4b2a19-6d35-4f81-b0c7-3a9e15d8c426
status: experimental
description: >
  Detecta la carga lateral de biblioteca como CLASE, no la pareja concreta del
  expediente StrikeShark. Cubre las cuatro parejas conocidas (SystemSettings,
  msedge, PrintDialog, miracastview) y las que aparezcan. La evasion del
  cargador es intraproceso y no alcanza este momento.
author: Celula CTI
date: 2026-11-17
references:
  - https://securelist.com/strikeshark-campaign/120326/
tags:
  - attack.defense_evasion
  - attack.t1574.002
logsource:
  category: image_load
  product: windows
detection:
  binario_microsoft:
    SignatureStatus: 'Valid'
    Signature|contains: 'Microsoft'
  fuera_de_ruta:
    Image|startswith:
      - 'C:\Users\'
      - 'C:\ProgramData\'
  dll_sin_firma:
    ImageLoaded|endswith: '.dll'
    SignatureStatus:
      - 'Unavailable'
      - 'Invalid'
      - 'Expired'
  condition: binario_microsoft and fuera_de_ruta and dll_sin_firma
falsepositives:
  - Aplicaciones portables mal empaquetadas: enumerar, son pocas
level: critical
```

```yaml
# Sigma — Tarea programada con repeticion de un minuto o menos
title: Tarea programada con disparador de repeticion extremo
id: 1f93c6d2-8b04-4e57-9a61-5c27ba03e8f1
status: experimental
description: >
  El cuentagotas de SharkLoader crea una tarea que se ejecuta CADA SEGUNDO para
  garantizar ejecucion inmediata, y la borra 1,5 segundos despues; la creacion
  queda registrada. Ningun actualizador legitimo se ejecuta con esa cadencia.
author: Celula CTI
date: 2026-11-17
tags:
  - attack.persistence
  - attack.t1053.005
logsource:
  product: windows
  service: security
detection:
  creacion:
    EventID:
      - 4698
      - 4702
  cadencia:
    TaskContent|contains:
      - '<Interval>PT1S</Interval>'
      - '<Interval>PT5S</Interval>'
      - '<Interval>PT10S</Interval>'
      - '<Interval>PT30S</Interval>'
      - '<Interval>PT1M</Interval>'
  condition: creacion and cadencia
falsepositives:
  - Alguna herramienta de monitorizacion mal configurada
level: high
```

```yaml
# Sigma — Directorio con nombre de fabricante de seguridad creado por un tercero
title: Directorio de fabricante de seguridad creado por proceso ajeno
id: 3a81f47c-9e26-4b05-8d13-72c4ae69b50d
status: experimental
description: >
  El actor usa nombres de fabricantes de seguridad como nombres de directorio
  de trabajo para parecer legitimo. Falso positivo practicamente nulo. Incluir
  en la lista el nombre del producto propio.
author: Celula CTI
date: 2026-11-17
tags:
  - attack.defense_evasion
  - attack.t1036.005
logsource:
  category: file_event
  product: windows
detection:
  ruta:
    TargetFilename|contains:
      - '\ProgramData\KasperskyLab\'
      - '\ProgramData\Kaspersky'
      - '\AppData\Roaming\kasperskylab\'
      - '\ProgramData\ESET\'
      - '\ProgramData\Bitdefender\'
      - '\ProgramData\Sophos\'
      - '\ProgramData\CrowdStrike\'
      - '\ProgramData\SentinelOne\'
  filtro_legitimo:
    Image|contains:
      - '\Kaspersky'
      - '\ESET\'
      - '\Bitdefender\'
      - '\Sophos\'
      - '\CrowdStrike\'
      - '\SentinelOne\'
  condition: ruta and not filtro_legitimo
falsepositives:
  - Instaladores y desinstaladores de esos mismos productos ejecutados desde
    una ruta temporal: enumerar
level: high
```

## X-5. Mitigaciones de configuración con efecto directo

| Control | Corta |
|---|---|
| **Parchear las trece vulnerabilidades del Anexo A.1 que estén vivas en el perímetro** | **La etapa 01 completa, y es la única medida que elimina la posibilidad de ser seleccionado** por un adversario que encuentra víctimas rastreando Internet |
| **Retirar GeoServer y los componentes geoespaciales de la exposición directa a Internet**, o ponerlos detrás de autenticación y de un proxy inverso | El vector del caso colombiano. **Y conviene decirlo:** muchos de estos servicios están expuestos porque **deben** publicar datos abiertos, de modo que la medida no es cerrarlos sino separar el nodo de publicación del que tiene la consola de administración |
| Control de ejecución que impida ejecutar binarios desde `%APPDATA%`, `%ProgramData%` y la raíz de `C:\` | **La etapa 02 completa.** Las cinco rutas de trabajo observadas están ahí, y la carga lateral necesita que el ejecutable legítimo corra **desde el directorio del atacante** |
| **Transporte remoto y en tiempo real del registro de eventos del sistema** | No corta nada: **habilita `H-3`**. Es la diferencia entre que la anulación de trazas sea perfecta y que deje una ausencia visible |
| EDR con observación en el núcleo, o compensación explícita con `D-1`, `D-2`, `D-5` y `D-8` | Las llamadas directas al núcleo de `X-1`. **Si no se puede cambiar el sensor, hay que saber qué reglas lo compensan**, y están nombradas |
| **Detección de red de Cobalt Strike, independiente del endpoint** | La etapa 03. **Es el único punto de observación que la evasión del cargador no alcanza** |
| Restringir que los procesos de servidor web puedan lanzar intérpretes | La interfaz web de administración remota, y con ella la persistencia de la etapa 01 |
| Protección del proceso de autenticación local, y restricción de `ntdsutil` y de herramientas de volcado | La escalada al dominio de la etapa 03 |
| Escaneo externo propio y recurrente del perímetro | `E-a` depende de que el inventario sea correcto. **El escaneo externo es la verificación de que lo es**, y es la misma vista que tiene el adversario |
| Segregación de la consola de administración de los servicios publicados | Generaliza la medida geoespacial a cualquier servicio que deba estar público |

---

## 14. Brechas de inteligencia y nuevos requisitos de colección

| # | Brecha | Impacto en el juicio | Requisito propuesto | Prioridad |
|---|---|---|---|---|
| G-1 | **No hay actor.** El propósito del clúster es desconocido y la propia fuente lo declara así | Todo juicio sobre intención tiene confianza baja. `H1`, `H2` y `H3` de `O-6` quedan abiertas sin poder discriminar | Vigilar `I-1` e `I-6`. **Y, mientras no haya actor, no inferir intención: es la disciplina que este informe se impone** | Alta |
| G-2 | **El anexo de indicadores publicado es un subconjunto declarado**, y sólo contiene MD5 | Un retrohunt contra siete hashes y cuatro dominios es de cobertura simbólica. **Un resultado negativo no es prueba de nada** | Valorar el acceso al servicio de inteligencia de la fuente. Mientras no exista, declarar el alcance limitado en todo informe de caza negativo | **Crítica** |
| G-3 | **Fuente única.** Ningún otro proveedor ha publicado sobre SharkLoader que hayamos localizado | El techo de confianza del apartado técnico lo fija una sola fuente, sin corroboración independiente del análisis de código | Vigilar `I-2`. Y, si aparece, contrastar específicamente la tabla de ganchos, que es el fundamento de `KJ-2` | Alta |
| G-4 | **Sin fechas de los incidentes individuales** | La ventana de retrohunt de doce meses es convención. No se puede saber si la campaña empezó en enero o en mayo de 2026 | Pedir el dato a la fuente. Mientras no esté, **usar la fecha de publicación de cada CVE como cota inferior** de cada vector: es lo único defendible | Media |
| G-5 | **No se sabe cómo se distribuyeron los cuentagotas.** La fuente lo declara expresamente | `T1566.001` queda como probable y no establecido, y con ella toda la defensa de correo frente a esta cadena | Vigilar publicaciones posteriores. Mientras tanto, tratar el vector de correo como posible y aplicar los controles genéricos | Media |
| G-6 | **No se observó exfiltración** | Es la raíz de `G-1`: sin exfiltración no se puede decidir el propósito, y la fuente valora el espionaje con confianza baja por este motivo | `I-6`. Y en casa: si aparece un caso propio, **la pregunta de respuesta a incidentes prioritaria es qué salió**, no qué entró | Alta |
| G-7 | **Sin verificar la cobertura de nuestro EDR** frente a las ocho técnicas de `X-3.1` | `KJ-3` queda en confianza moderada por inferencia. **No sabemos si estamos cubiertos, y es averiguable** | `E-d`, por escrito y con respuesta técnica fila por fila | **Crítica** |
| G-8 | **Sin inventario de componentes geoespaciales** | El único vector regional confirmado es precisamente el que no tenemos inventariado | `E-b` y `H-10`. **Es la brecha de este informe que se cierra con una hoja de cálculo y dos llamadas** | **Crítica** |

---

# ANEXOS

## Anexo A — Indicadores de compromiso

> ⚠ **Leer antes de usar. Tres advertencias, y la primera cambia el orden de
> lectura del anexo.**
>
> **Primera, de prioridad.** En este expediente **el nivel más valioso del
> Anexo A no son los indicadores de red ni los hashes: es el Anexo A.1**,
> trece vulnerabilidades con parche disponible y exploit público. Esa sección
> se resuelve con una tarea de inventario y cierra la etapa de acceso inicial
> **completa**, incluido el vector del único caso regional. Todo lo demás de
> este anexo detecta lo que ya pasó; A.1 impide que pase.
>
> **Segunda, de alcance.** La fuente declara expresamente que hay información
> adicional sobre esta actividad, **incluidos indicadores de compromiso**,
> disponible para los clientes de su servicio de inteligencia. Lo publicado —y
> por tanto lo que hay aquí— es un subconjunto. **Y sólo publica MD5**, no
> SHA-256. Un retrohunt negativo contra esta lista no es prueba de ausencia: es
> la brecha `G-2`.
>
> **Tercera, de caducidad.** La fuente no publica fechas de los incidentes
> individuales. La caducidad de doce meses que figura en las filas de red es
> **convención declarada**, no dato, y se deriva de la fecha de publicación del
> informe. Es `G-4`.

### A.1 — Vulnerabilidades explotadas · **la sección que hay que atender primero**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| cve | `CVE-2024-36401` | **GeoServer. ES EL VECTOR DEL CASO COLOMBIANO.** Servidor de datos geoespaciales de código abierto, ubicuo en la administración pública de la región para catastro, ordenamiento territorial, minería, ambiente e infraestructuras de datos espaciales. **Suele administrarlo el área técnica de cartografía y no la de sistemas, de modo que queda fuera del inventario de aplicaciones y del ciclo de parcheo** | Alta | Sin caducidad: la decisión es de parcheo e inventario | **Parchear, inventariar y retirar de exposición directa** (`E-b`, `H-10`) |
| cve | `CVE-2021-26855` | **Microsoft Exchange, «ProxyLogon».** Vector del caso de la entidad diplomática de Indonesia. **Publicada en marzo de 2021** | Alta | Sin caducidad | **Parchear y verificar** |
| cve | `CVE-2023-32315` | **Openfire.** Vector de los casos taiwaneses de empresas de desarrollo de software. Servidor de mensajería instantánea empresarial | Alta | Sin caducidad | **Parchear y verificar** |
| cve | `CVE-2023-20198` | **Cisco IOS XE, interfaz web.** Elusión de autenticación. **La misma vulnerabilidad que usa el actor de `CTI-2026-030`: dos clústeres sin relación entre sí entran por esta puerta, lo que eleva su prioridad por encima de la suma de ambos expedientes** | Alta | Sin caducidad | **Parchear con prioridad máxima** (`H-11`) |
| cve | `CVE-2016-4437` | **Apache Shiro.** Ejecución remota de código. **Publicada en 2016: diez años con parche disponible y sigue en la lista de entrada de este clúster** | Alta | Sin caducidad | **Parchear y verificar** |
| cve | `CVE-2021-36260` | **Productos Hikvision.** Ejecución remota de código en dispositivos de videovigilancia. **El tipo de activo que casi nunca está en el inventario ni en el ciclo de parcheo** | Alta | Sin caducidad | **Parchear, y segregar de la red corporativa** |
| cve | `CVE-2021-27076` | **Microsoft SharePoint.** Ejecución remota. La fuente la asocia a un caso en que el actor relanzó la cadena **desde directorios distintos**, lo que leyó como actividad renovada en el entorno de la víctima | Alta | Sin caducidad | **Parchear y verificar** |
| cve | `CVE-2022-27925` | **Zimbra Collaboration Suite.** Ejecución remota. Plataforma de correo con despliegue significativo en la administración pública de la región | Alta | Sin caducidad | **Parchear y verificar** |
| cve | `CVE-2022-41082` | **Microsoft Exchange Server.** Ejecución remota | Alta | Sin caducidad | **Parchear y verificar** |
| cve | `CVE-2023-46747` | **F5 BIG-IP.** Ejecución remota en el plano de administración | Alta | Sin caducidad | **Parchear, y retirar el plano de administración de Internet** |
| cve | `CVE-2024-21762` | **Fortinet FortiOS.** Ejecución remota | Alta | Sin caducidad | **Parchear y verificar** |
| cve | `CVE-2025-55182` | **React Server Components.** Ejecución remota. **La más reciente de la lista**, lo que indica que el repertorio se amplía con las publicaciones nuevas | Alta | Sin caducidad | **Parchear y verificar** |
| cve | `CVE-2022-40684` | **Fortinet FortiOS.** Elusión de autenticación | Alta | Sin caducidad | **Parchear y verificar** |
| artefacto | **Las trece tienen código de explotación público** | **No es un indicador: es el juicio que ordena la prioridad.** La fuente valora con **confianza media** que el actor se apoya principalmente en exploits de prueba de concepto públicos y no desarrolla capacidad propia. Consecuencia: **la ventana de riesgo se abre cuando aparece el exploit público, no cuando aparece el CVE** | Media *(valoración de la fuente)* | Sin caducidad | **Criterio de priorización del ciclo de parcheo** |
| artefacto | Rastreo masivo de Internet desde una dirección asociada a un dominio de C2 | **Tampoco es un indicador de compromiso: es la explicación de por qué podemos ser víctimas sin interesar a nadie.** Convierte la gestión de exposición en control de selección | Media | Sin caducidad | **Escaneo externo propio recurrente** (`X-5`) |

### A.2 — Ficheros

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| md5 | `C559CC68986933200FD5D9E4388E2F58` | **Instalador.** Clasificado así por la fuente | Alta | Vida útil de la muestra | **Solo retrohunt** |
| md5 | `B3352B42432DEDC4A519F011DC8B5D5A` | **Cuentagotas** | Alta | Vida útil de la muestra | **Solo retrohunt** |
| md5 | `24FCEBDEECBA65004FDB0923763D74FD` | **Cuentagotas** identificado en la campaña contra una entidad de gobierno de **Taiwán**. Es la muestra que la fuente usa para su análisis detallado; su nombre de fichero es una doble extensión con un título en chino y terminación `.pdf.exe` | Alta | Vida útil de la muestra | **Solo retrohunt** |
| md5 | `1F65544978B8EA0E745E573B8EE9684B` | **Cuentagotas descubierto en un equipo situado en el Líbano.** Extrae `SystemSettings.dll` de datos comprimidos con `zlib` embebidos y los módulos cifrados de los recursos `VAULTSVCD` y `UMRDPRDAT`, todo a `%APPDATA%\xwreg` | Alta | Vida útil de la muestra | **Solo retrohunt** |
| md5 | `9C872A0D5D5A38950E8B9AC9B488BE3F` | **SharkLoader, biblioteca principal** | Alta | Vida útil de la muestra | **Solo retrohunt** |
| md5 | `AA3086BE652C8B20B0B29B2730D57119` | **SharkLoader, biblioteca principal** del caso taiwanés analizado en detalle | Alta | Vida útil de la muestra | **Solo retrohunt** |
| md5 | `A514D1BB62D7916475946FE7C07AC0AA` | **Fichero cifrado** (`DscCoreR.mui` en el caso analizado): contiene el Beacon y la biblioteca MinHook | Alta | Vida útil de la muestra | **Solo retrohunt** |
| md5 | `9CBD560F820C95D7C38342CD558CB5C6` | **Fichero cifrado** (`SyncRest.dat` en el caso analizado): instala los ganchos de API | Alta | Vida útil de la muestra | **Solo retrohunt** |
| md5 | `D98F568496512E4F98670C61C97CB07A` | **`SystemSettings.exe` legítimo de Microsoft**, tal como figura en la tabla de componentes de la fuente. **NO ES UN INDICADOR DE COMPROMISO: es un binario del sistema.** Se consigna con esta advertencia precisamente porque aparece en una tabla de componentes de malware y **bloquearlo rompería Windows** | Alta | Sin caducidad | **NO BLOQUEAR NUNCA.** Solo correlación: lo relevante es su **ubicación**, no su hash |
| filename | `GoogleUpdateStepup.exe` · `AutoUpdate.exe` · `AnyConnect-win-4.10.04071-predeploy-k9exe` | **Nombres de cuentagotas** que suplantan instaladores legítimos. **Nótese la extensión malformada del tercero** —falta el punto antes de `exe`—, que es en sí misma un indicador | Alta | Caduca con la campaña | Caza |
| filename | `319-pfd-8001-reva_traitement biologique_master.zip` | Nombre de cuentagotas con temática de ingeniería en francés. Coherente con el PDF señuelo de tratamiento biológico que la fuente describe | Alta | Caduca con la campaña | Caza |
| filename | `%APPDATA%\reports\AnyConnect-win-4.msi` | **Instalador legítimo de Cisco AnyConnect** que el cuentagotas extrae y **ejecuta de verdad** para que la víctima crea que instaló lo que quería, mientras los componentes del cargador se despliegan en otro directorio | Alta | Caduca con la campaña | Caza |

### A.3 — Red

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| domain | `connect-microsoft[.]com` | **Dominio de mando y control.** Suplanta nomenclatura de Microsoft. **El orden invertido de las palabras es el indicador de clase:** un dominio legítimo del fabricante no se llama así | Alta | 2027-06-24 (12 meses desde la publicación, por convención) | **Bloqueo** |
| domain | `ms-record[.]com` | Dominio de mando y control. Suplanta nomenclatura de Microsoft | Alta | 2027-06-24 | **Bloqueo** |
| domain | `ms-record[.]top` | Dominio de mando y control. **Mismo nombre que el anterior en otro TLD**: el patrón de registro paralelo que `CTI-2026-018` documenta | Alta | 2027-06-24 | **Bloqueo** |
| domain | `ms-tray[.]top` | Dominio de mando y control | Alta | 2027-06-24 | **Bloqueo** |
| pattern | `ms-*` · `*-microsoft*` · prefijo `ms` seguido de un término genérico de sistema, en TLD `.top` y `.com` | **Patrón de nomenclatura del clúster**, generalizado desde los cuatro dominios. Más duradero que los literales, y utilizable para vigilancia de registros nuevos | Media | Sin caducidad | Caza y vigilancia de registro |

### A.4 — Artefactos de host y de configuración · **el nivel que la evasión no alcanza**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| artefacto | `OneDrive Standalone Update Task-S-1-5-21-4165425321-4153752593-2322023643-1000` | **Nombre de tarea programada.** Disparador temporal **cada cinco minutos**: es la que permanece y da la persistencia a largo plazo | Alta | **Sin caducidad** | **Detección** (`D-1`) |
| artefacto | `MicrosoftUpdateTaskUserS-1-5-32-2456537112-101246289-228944324-1000` | **Nombre de tarea programada con ejecución cada segundo**, creada para garantizar ejecución inmediata y **borrada aproximadamente 1,5 segundos después**. La ejecución desaparece; **el registro de su creación, no** | Alta | **Sin caducidad** | **Detección** (`D-1`) |
| artefacto | `\Microsoft\Windows\Edge\Edgeupdate` | **Tarea programada creada con `schtasks`**, ejecución **diaria como `SYSTEM`**, apuntando a `C:\ADriveLogs_Logs\SystemSettings.exe`. Observada en el caso de la entidad diplomática de Indonesia | Alta | **Sin caducidad** | **Detección** (`D-1`) |
| pattern | Tarea programada con **intervalo de repetición de 60 segundos o menos** | **Generalización de mayor valor que los nombres literales.** Ningún actualizador legítimo se ejecuta con esa cadencia | Alta | **Sin caducidad** | **Detección** (`D-1`) |
| clave | `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`, valor `MFUpdate` | **Persistencia creada a mano** con `reg add`, apuntando a `SystemSettings.exe` en el perfil del usuario. Observada en el caso de Hong Kong | Alta | **Sin caducidad** | **Detección** |
| filepath | `%APPDATA%\xwreg` · `%APPDATA%\xgdf` · `%APPDATA%\Identities` · `C:\ADriveLogs_Logs\` · `%TEMP%\aswerf\` | **Directorios de trabajo observados.** Los nombres son arbitrarios y caducarán; **la ubicación no**: todos están en rutas de perfil o de datos de aplicación, que es donde el control de ejecución de `X-5` actúa | Alta | Caducan con la campaña | **Detección y caza** (`D-3`) |
| filepath | `C:\ProgramData\KasperskyLab\` · `%APPDATA%\kasperskylab\` | **Directorios con nombre de un fabricante de seguridad, usados por el actor para parecer legítimo.** Falso positivo prácticamente nulo. **Incluir en la caza el nombre del producto propio** | Alta | **Sin caducidad como patrón** | **Detección** (`D-4`, `H-6`) |
| pattern | `copy SystemSettings.exe` desde `C:\Windows\ImmersiveControlPanel\` a otra ruta, seguido de su ejecución desde allí | **La secuencia de instalación en una línea.** Es el momento en que la cadena es visible antes de que exista el proceso que la oculta | Alta | **Sin caducidad** | **Detección** (`D-2`, `D-3`) |
| filename | `SystemSettings.dll` · `msedge.dll` · `PrintDialog.dll` · `miracastview.dll` | **Las cuatro bibliotecas objetivo de carga lateral conocidas**, cada una con su aplicación legítima. **El indicador no es el nombre: es el nombre fuera de la ruta del sistema y sin la firma del fabricante** | Alta | Se amplía con variantes nuevas (`I-7`) | **Detección** (`D-2`, `D-3`) |
| filename | `DscCoreR.mui` · `SyncRes.dat` · `SyncRest.dat` · `GameInputInboxs32.mui` · `diagerr.xml` · `NtfsLog.etl` · `Ignored.Dat` · `VistaCompat.nls` | **Nombres de los módulos cifrados**, elegidos para parecer registros, cachés y ficheros de localización de Windows | Alta | Se amplía con variantes nuevas | **Detección** (`D-3`, `H-7`) |
| pattern | Fichero cuyos **primeros 16 bytes** son clave Blowfish y el resto PE cifrado en **modo ECB**; o cuyos **primeros 32 bytes** son clave e IV de **AES-128** y el resto PE cifrado | **La estructura de los módulos, generalizada.** Soporta caza por entropía con independencia del nombre | Media | **Sin caducidad** | Caza (`H-7`) |
| artefacto | `TELEMETRY` · `VAULTSVCD` · `UMRDPRDAT` | **Nombres de recurso dentro de los cuentagotas**, con el PDF señuelo y los módulos cifrados comprimidos con `zlib` | Alta | Caducan con la campaña | Análisis de muestras |

### A.5 — Técnicas de evasión · **no son indicadores: son la lista de `X-3.1`**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| pattern | `EtwEventWrite` → 1 · `EventWrite` → 0 · `EventWriteEx` → 0 | **Anulación del registro de eventos del sistema en el proceso.** Las funciones devuelven éxito sin escribir nada. **Se detecta por la ausencia de trazas, no por su presencia**, y eso exige recolección remota | Alta | **Sin caducidad** | **Caza por ausencia** (`H-3`, `E-e`) |
| pattern | `LdrpLoaderLock` · `LdrpWorkInProgress` · `LeaveCriticalSection` + `InterlockedDecrement64` + `SetEvent` + `CreateThread` desde la inicialización de una biblioteca | **«Perfect DLL Hijacking».** Manipulación de estructuras internas no documentadas del cargador de Windows para soltar su cerrojo | Alta | **Sin caducidad** | Pregunta al fabricante (`X-3.1`) |
| herramienta | `Microsoft Detours` · `MinHook` · `jitasm` | **Bibliotecas legítimas de desvío de funciones y de generación de código en tiempo de ejecución.** No son maliciosas: son lo que el adversario usa para construir su evasión | Alta | Sin caducidad | **No bloquear**; análisis |
| pattern | Llamadas directas al núcleo construidas en tiempo de ejecución para ≈15 funciones de gestión de procesos, memoria e hilos | **Elusión de los ganchos en espacio de usuario**, incluidos los del producto de seguridad. Es la pregunta central de `X-3.1` | Alta | **Sin caducidad** | Pregunta al fabricante (`E-d`) |
| pattern | Protección de memoria del Beacon cambiada a **sólo lectura y escritura durante el reposo** y restaurada a **ejecutable** al despertar | **Evasión de barrido de memoria en busca de regiones ejecutables anómalas.** La fuente la identifica expresamente con ese propósito | Alta | **Sin caducidad** | Pregunta al fabricante (`E-d`) |
| pattern | Falsificación de proceso padre a un `svchost.exe` **del mismo contexto de seguridad**, por hilo dedicado o por llamada asíncrona en cola | **Rompe el árbol de procesos como fuente de contexto.** Y la contramedida que funciona de todos modos: **detectar por contenido de la línea de comandos**, que no se falsifica (`D-6`, `H-4`) | Alta | **Sin caducidad** | **Detección** (`H-4`) |
| pattern | `ROR13` para `LdrLoadDll` · `Murmur32` sobre la tabla de exportaciones | Resolución de funciones por hash, para que no haya cadenas de nombres de API en el binario | Alta | Sin caducidad | Análisis de muestras |
| herramienta | `FScan` · `Searchall` · `Pillager` · `SharpGPOAbuse` | **Herramientas públicas de post-explotación.** **Su presencia NO atribuye nada**, y la autoría declarada de las tres primeras es el único fundamento de una atribución que la propia fuente califica de confianza baja (`O-2.1`) | Alta | Sin caducidad | Detección por contexto; **NO usar como base de atribución** |
| herramienta | `Cobalt Strike Beacon` | **La única carga final observada.** Herramienta comercial legítima de pruebas de intrusión. **Su presencia no atribuye**, igual que Mythic en `CTI-2026-026`. **Y es el punto de observación que la evasión del cargador no alcanza, porque vive en la red** | Alta | Sin caducidad | **Detección de red** (`D-5`, `E-h`) |

## Anexo B — Fuentes y valoración

> Valoración doble tipo Admiralty/OTAN: **fiabilidad de la fuente (A–F)** ×
> **credibilidad de la información (1–6)**. Se valoran por separado.

| Fuente | Disciplina | Fiabilidad | Credibilidad | Notas de sesgo |
|---|---|---|---|---|
| **Kaspersky GReAT, «StrikeShark: investigating a new campaign delivering Cobalt Strike through SharkLoader», Securelist, 24-06-2026** — leída en original con su anexo de indicadores y sus tablas de ganchos | OSINT comercial · TECHINT de primera mano con análisis de código | **B** | **2** | **Fuente primaria y única del apartado técnico.** Calidad alta: publica su método, su cadena de razonamiento, los nombres de las estructuras internas que el malware manipula y la tabla completa de funciones desviadas con la finalidad de cada desvío. **Declara explícitamente su confianza baja en la atribución, la parcialidad de su visibilidad y que reserva indicadores a sus clientes**: las tres son señales de calidad. Sesgos: interés comercial en nombrar una campaña nueva; **sin corroboración independiente** (`G-3`) |
| **Comunicado de prensa de Kaspersky de la misma fecha**, en inglés y en español, leídos en original | OSINT comercial · derivada propia | **B** | **2** | Resumen del anterior por su propio autor. **Útil por una razón concreta:** permitió verificar que la versión española del comunicado mantiene la asignación de sectores por país del informe técnico, y por tanto que la imprecisión de `§3.5`/punto 3 no proviene de la fuente |
| **Blog de Elliot Killick sobre «Perfect DLL Hijacking»** — citado por la fuente primaria, no leído en original en esta revisión | OSINT · investigación independiente | **B** | **2** *(por referencia)* | Origen público de la técnica de escape del cerrojo del cargador. Se cita por su papel en el expediente: **la técnica existe publicada y eso explica cómo un actor que no desarrolla exploits propios la implementa** |
| **Cobertura secundaria y agregadores, junio-julio de 2026** | OSINT comercial · derivada y agregada | **D** | **4** | **Se citan por un motivo distinto del habitual: son el objeto de `O-2.1`.** Al menos un resumen publicó la atribución con confianza **moderada** cuando la fuente dice **baja**. No se usa ninguno de sus datos técnicos; se usa el hecho de su desviación |
| **Avisos y bases de datos públicas de vulnerabilidades** | OSINT técnico · gubernamental y de fabricante | **A** | **1** | Para las fechas de publicación y los productos afectados de las trece vulnerabilidades del Anexo A.1. **Son la parte más verificable de este informe** |

> **Una observación sobre la calidad de la fuente que conviene dejar escrita.**
> Este informe descansa en una única fuente, lo que normalmente limitaría mucho
> su valor. Lo que compensa parcialmente ese problema es **el tipo de
> publicación**: no es un resumen de hallazgos, es un análisis de código con el
> razonamiento expuesto, que nombra estructuras internas verificables, publica
> la finalidad de cada uno de los treinta desvíos y **declara con precisión los
> límites de lo que sabe** —no atribuye, no observó exfiltración, no obtuvo los
> exploits, no sabe cómo se distribuyeron los cuentagotas, sospecha que hay más
> víctimas—. Una fuente que enumera lo que no sabe es más utilizable que tres
> que no lo hacen. **Pero sigue siendo una**, y por eso `I-2` está en `O-7`.

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

## Anexo D — Cómo se escribe sobre un clúster que nadie ha atribuido

Este anexo no es sobre StrikeShark. Es el método que este informe tuvo que improvisar y que conviene fijar, porque los clústeres sin atribuir son cada vez más frecuentes —la industria publica antes y atribuye después— y el formato de producto habitual está construido para actores con nombre.

**El problema.** Un perfil de actor normal funciona porque la identidad permite deducir intención, y la intención permite predecir selección. Sin identidad, ese motor no arranca, y el analista se encuentra con un documento que no puede responder «¿qué quieren?» ni «¿irán a por nosotros?». La tentación de rellenar ese hueco es intensa y tiene dos formas: la **inflación de confianza** —adoptar la pista más llamativa y promoverla a conclusión, como documenta `O-2.1`— y la **antropomorfización del clúster** —empezar a hablar de «StrikeShark» como si tuviera planes—.

**Las cinco reglas que este informe aplicó.**

1. **No inferir intención desde la identidad, porque no hay identidad.** Toda afirmación sobre propósito se marca con su confianza, que será baja, y se deja como hipótesis abierta en la sección de hipótesis competidoras. Si una fuente valora el propósito con confianza baja, el informe no puede valorarlo con más.
2. **Reemplazar «quién» por «cómo entra» como eje organizador.** La pregunta útil deja de ser «¿nos quieren?» y pasa a ser «¿somos alcanzables?». Eso convierte el informe en un ejercicio de reducción de exposición, que es actuable sin saber nada del adversario. Es el motivo de que el Anexo A.1 esté primero.
3. **Buscar la asimetría de inversión.** Dónde el adversario escribió código propio y dónde usó lo de otros. Es la señal más fiable de qué le importa, y no requiere identidad: aquí, exploits ajenos para entrar, herramientas ajenas para recolectar, **y código propio y elaborado sólo para no ser visto en medio**. Eso dice más sobre sus prioridades que cualquier atribución.
4. **Enumerar lo que el malware NO tiene.** En un perfil de actor nadie hace esto porque las capacidades se infieren del historial. Sin historial, la ausencia es información: un cargador sin canal de exfiltración, sin recolección y sin persistencia propia es un vehículo, y eso estrecha mucho el espacio de hipótesis. Es `X-1.1`.
5. **Separar lo que caduca de lo que no, y decirlo en cada fila.** Sin actor no hay historial que permita estimar cuánto durará la infraestructura, de modo que toda caducidad es convención. Declararla como tal evita que un indicador se trate como vigente tres años después.

**Y una regla negativa, que es la más importante.** Cuando se atribuya el clúster —y probablemente ocurra—, **hay que volver a este informe y comprobar qué juicios cambian. La respuesta muy posiblemente sea: ninguno de los que llevan a una decisión.** Las trece vulnerabilidades hay que parchearlas igual, el GeoServer hay que inventariarlo igual, la pregunta al fabricante de EDR sigue siendo la misma y las ocho detecciones siguen siendo las mismas. **Si al llegar la atribución nada cambia, eso confirma que el informe estaba bien construido**; si cambiara mucho, significaría que se habían colado inferencias apoyadas en una identidad que no existía.

> **El reverso, que también cuesta.** No atribuir no es gratis: un informe sin
> actor tiene menos tracción interna, se cita menos y compite peor por
> presupuesto que uno con bandera. Ése es el precio del rigor aquí, y la forma
> de pagarlo con menos daño es **la que este documento intenta: sustituir el
> titular de identidad por un titular de consecuencia**. «Un clúster que nadie
> ha atribuido» no moviliza a nadie; «entraron por un GeoServer sin parchear
> que nadie tenía inventariado» sí.

## Anexo E — Marcos de referencia empleados

`MITRE ATT&CK v18` · `Modelo del Diamante` · `Cyber Kill Chain` · `Pirámide del Dolor` · `F3EAD` · `ICD 203` · `ACH, supuestos clave y pre-mortem` · `TLP 2.0` · `PAP` · `Admiralty Code` · `Sigma` · `CVSS y catálogos públicos de vulnerabilidades explotadas`

## Anexo F — Paquete legible por máquina

- Las tablas `cti:ioc` de los Anexos A.1 a A.5 alimentan `ioc_index.csv` en cada construcción. **El Anexo A.1, de vulnerabilidades, es el que debe ingerirse primero**, y su destino natural no es el SIEM sino el sistema de gestión de vulnerabilidades.
- **Dos filas del Anexo A.2 llevan advertencia explícita de no bloquear**: el hash del `SystemSettings.exe` legítimo de Microsoft, porque bloquearlo rompería Windows; y las herramientas públicas del Anexo A.5, por el mismo motivo que `CTI-2026-026` advierte sobre Mythic.
- **Fuente preferente para ingesta:** el anexo del informe de Securelist, y para los indicadores completos, el servicio de inteligencia de su autor (`G-2`).
- **Reglas propias:** tres reglas Sigma en `X-4`. La de carga lateral de biblioteca sobre binario firmado fuera de ruta es la única que **no caduca con la campaña**, porque describe la clase y no la pareja.
- **Consultas propias:** seis en KQL. La última —la caída de volumen de eventos por equipo— es la más inusual del repositorio: **busca una ausencia**, y sólo funciona con recolección remota.

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-11-17 | Emisión inicial. Se corrige la ubicación sectorial de la víctima colombiana que afirmaba el requisito de origen (`§3.5`, punto 3), se documenta el vector concreto de ese caso —GeoServer, `CVE-2024-36401`— y se eleva a decisión regional el inventario de componentes geoespaciales (`E-b`), se documenta en `O-2.1` una inflación de confianza en la atribución entre la fuente primaria y su cobertura secundaria, y se añade `X-3.1`: la lista de ocho preguntas al fabricante de EDR derivada de las técnicas de evasión del cargador | Célula CTI |

## Anexo H — Realimentación del consumidor

| Pregunta | Respuesta |
|---|---|
| ¿Respondió a su requisito? | |
| ¿Qué decisión tomó o cambió con este informe? | |
| **¿Cuántas de las trece vulnerabilidades del Anexo A.1 estaban vivas (`E-a`)?** | |
| **¿Tenían un GeoServer o un componente geoespacial expuesto, y lo sabían (`E-b`, `H-10`)?** | |
| ¿Quién lo administraba? ¿Estaba en el inventario de aplicaciones? | |
| ¿Qué contestó el fabricante de EDR a las ocho preguntas de `X-3.1` (`E-d`)? | |
| ¿Se transporta la telemetría de registro de eventos fuera del equipo (`E-e`)? | |
| ¿Llegó a tiempo? | |

> Sin este anexo devuelto, el ciclo de inteligencia queda abierto y el próximo
> producto no mejora. **Tres preguntas de esta tabla valen más que las demás**, y
> ninguna es sobre el adversario: las trece vulnerabilidades, el inventario
> geoespacial y la respuesta del fabricante. En un expediente sin actor, el
> informe se mide por lo que cambió en casa.
