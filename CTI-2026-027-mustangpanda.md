---
tlp: "TLP:CLEAR"
pap: "PAP:AMBER"
id: "CTI-2026-027"
version: "1.1"
tipo: "Perfil de actor"
foco_regional: "Global · Chile · Latinoamérica"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "Mustang Panda · Earth Preta · RedDelta · Twill Typhoon · G0129"
fecha: "2026-11-17"
caduca: "2027-02-17"
autor: "Célula CTI"
distribucion: "Elaborado íntegramente con fuentes abiertas TLP:CLEAR: el análisis de Kaspersky GReAT de agosto de 2026 sobre el rootkit de kernel firmado, la investigación de Google GTIG sobre UNC6384, los documentos judiciales del desmantelamiento del Departamento de Justicia de EE. UU. de enero de 2025, el informe de telemetría de Trellix de noviembre de 2026 y cinco informes de proveedor adicionales. Difusión libre, conservando la atribución de las fuentes y las salvedades metodológicas de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-027

## El tercero del ranking global sí es tan peligroso como su puesto sugiere, y eso desmonta los dos informes anteriores

### El FBI le borró el malware de 4 258 ordenadores, se rearmó en meses, y en 2026 firmó un rootkit con certificado válido

> **Regla de oro del producto:** todo párrafo debe responder a un requisito de
> inteligencia (PIR) y habilitar una decisión. Si un párrafo no cambia lo que
> alguien va a hacer, va al anexo o se borra.

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-027` |
| Versión / fecha | `1.1` — 2026-11-21 |
| Tipo de producto | Perfil de actor, más **evaluación de capacidad** —el actor con mayor capacidad técnica demostrada de este lote— y **evaluación de resiliencia a la acción policial**: es el único de la cartera que sobrevivió a un desmantelamiento judicial documentado |
| Niveles cubiertos | Estratégico · Operacional · Táctico · Técnico |
| Foco regional | **Sin víctimas latinoamericanas documentadas, pero con victimología global real**: Europa, Estados Unidos, Indo-Pacífico, y sectores que sí tenemos (marítimo-portuario, hidroeléctrico, diplomático). **Es el primer actor de este lote cuya exposición indirecta no es hipotética** |
| Marcado de difusión | `TLP:CLEAR` · `PAP:AMBER` |
| Clasificación interna | Público — apto para difusión abierta |
| Requisitos atendidos | `PIR-01`, `PIR-04`, `PIR-07`, `PIR-10`, `PIR-11`, `PIR-14` |
| Solicitante / consumidor primario | Célula CTI (producción propia) · CISO · Jefatura de SOC · Ingeniería de Detección · Arquitectura de plataforma Windows |
| Ventana de observación | 2024-08-01 → 2026-09-30 |
| Base de colección | 8 fuentes de primera mano, **incluida una judicial** · 1 informe de telemetría agregada · **sin telemetría propia** |
| Autor (analista) | Célula CTI |
| Revisión por pares | Pendiente |
| Aprobación | Pendiente |
| Caducidad / revisión | 2027-02-17 — 92 días |
| Productos relacionados | **`CTI-2026-025` y `CTI-2026-026`: este informe los corrige parcialmente.** Leer los tres juntos y en orden · `CTI-2026-017` (FamousSparrow, actor china-nexus con victimología regional) · `CTI-2026-028` (UNC3886, lote de noviembre de 2026) |
| Paquete legible por máquina | `ioc_index.csv` del repositorio · sin bundle STIX propio |

> ⚠ **Limitación estructural.** Sin telemetría propia: §O-4 se entrega como
> cuestionario. Y una salvedad sobre la calidad del expediente que es la
> contraria a la de `CTI-2026-026`: aquí **las fuentes sí se corroboran**, hay
> una fuente judicial con valor probatorio, y dos de los hallazgos técnicos
> principales proceden de análisis de ingeniería inversa de un laboratorio con
> telemetría global. **Es el expediente mejor sostenido del lote**, y conviene
> notar que el actor mejor documentado resulta ser también el más capaz.

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** Mustang Panda ocupa el **tercer puesto del ranking de actividad estatal global** de Trellix para abril–septiembre de 2026, con el 7,52 %, y sube al 8,78 % en el tercer trimestre aislado. Es el actor china-nexus más prevalente de ese ranking, en un semestre en que Trellix reporta además una **caída del 41,4 % de la actividad estatal china detectada en conjunto**: es decir, sube en términos relativos mientras su bloque baja. Valoramos **casi con certeza** *(95–99 %)* que son las cifras publicadas. **Confianza: alta.** *Base:* página del proveedor y cobertura coincidentes, con la limitación de lectura de §3.3-ii.

**KJ-2.** Y aquí este informe **corrige a los dos anteriores de este lote.** `CTI-2026-025` y `CTI-2026-026` sostuvieron que un puesto alto en un ranking de prevalencia indica ruido y no capacidad. En este caso **eso es falso**: el actor tiene un rootkit de kernel firmado desplegado en operaciones, sobrevivió a un desmantelamiento judicial internacional, abusa de certificados de firma de código, y tiene víctimas documentadas en Europa y Estados Unidos. La conclusión correcta, que es más incómoda y más útil, es que **el ranking no discrimina**: los tres primeros puestos de noviembre de 2026 contienen dos actores ruidosos y uno peligroso, y el ranking los presenta igual. Valoramos **casi con certeza** *(95–99 %)* que esto sea así. **Confianza: alta.** *Base:* contraste directo de los tres expedientes de este lote; el razonamiento es nuestro pero los hechos de cada uno están documentados.

**KJ-3.** El mecanismo por el que este actor acumula detecciones está identificado y **no es el mismo que su capacidad**: tiene al menos tres gusanos de USB documentados —`HIUPAN` (también `MISTCLOAK` o `U2DiskWatch`), `SnakeDisk` y las variantes de `PlugX`/`DOPLUGS`— y la propagación por medios extraíbles genera artefactos en cada unidad que toca, igual que en Gamaredon. **El ranking está midiendo el gusano; la operación está en el kernel.** Valoramos **probable** *(55–80 %)* que la propagación por USB sea la causa principal de su volumen de telemetría. **Confianza: moderada.** *Base:* inferencia nuestra sobre el mecanismo, consistente con el caso de Gamaredon y con la naturaleza de las herramientas documentadas.

**KJ-4.** El hallazgo técnico más grave del expediente es de agosto de 2026: Kaspersky GReAT documentó que el actor añadió un **rootkit de kernel con firma digital válida** a su puerta trasera `CoolClient`. El controlador se llama `msagent.sys`, se instala como servicio de Windows, y hace tres cosas: oculta procesos, protege ficheros y claves de registro, y **filtra el tráfico de red de modo que las direcciones de mando y control configuradas desaparecen de la información que el sistema devuelve al espacio de usuario**. La puerta trasera se comunica con él por peticiones `IOCTL`. Valoramos **casi con certeza** *(95–99 %)* la existencia y las capacidades de este componente. **Confianza: alta.** *Base:* análisis de ingeniería inversa de un laboratorio de primera línea, reproducido de forma coincidente por múltiples coberturas.

**KJ-5.** El detalle del certificado merece su propio juicio porque es el que convierte un hallazgo técnico en una decisión de arquitectura: **el certificado que firma el controlador era válido entre agosto de 2013 y septiembre de 2014**, es decir, **caducó hace doce años**, y sin embargo la aplicación de firma de controladores de Windows lo acepta. Esto no es un fallo del actor: es una propiedad del modelo de confianza de Windows, que acepta controladores firmados antes de la fecha de corte de aplicación de firmas. Valoramos **casi con certeza** *(95–99 %)* que cualquier organización sin lista de bloqueo de controladores vulnerables sea susceptible al mismo mecanismo, con este controlador o con otro. **Confianza: alta.** *Base:* es una propiedad documentada de la plataforma, no una conjetura.

**KJ-6.** El actor **sobrevivió a una acción policial internacional y se rearmó en meses**, y eso lo distingue de todos los demás de esta cartera. Entre agosto de 2024 y enero de 2025, el Departamento de Justicia y el FBI de Estados Unidos, con una técnica desarrollada por la policía francesa, **borraron una variante de `PlugX` de 4 258 ordenadores** en jurisdicción estadounidense, con órdenes judiciales del Distrito Este de Pensilvania. El actor no cesó: en 2026 estaba operando con `LOTUSLITE`, `SnakeDisk`, `CoolClient` y tres familias nuevas. Valoramos **casi con certeza** *(95–99 %)* que el desmantelamiento no degradó la capacidad del actor de forma duradera. **Confianza: alta.** *Base:* documentos judiciales para el desmantelamiento, y seis informes de proveedor posteriores que documentan actividad y herramientas nuevas.

**KJ-7.** Los documentos judiciales aportan además el elemento de atribución más fuerte de todo este lote: afirman que **el gobierno de la República Popular China pagó a Mustang Panda por servicios de intrusión informática**, incluido el uso de `PlugX`. Es una afirmación hecha ante un tribunal, no una valoración de proveedor. **Pero no hay personas acusadas ni servicio concreto designado públicamente**, y la acción de enero de 2025 fue una disrupción técnica y no una imputación. Valoramos **muy probable** *(80–95 %)* la relación contractual con el Estado chino. **Confianza: moderada.** *Base:* fuente judicial de alto valor, pero sin imputación nominal que permita verificar el fundamento; y las fuentes secundarias discrepan sobre el alcance de lo que el tribunal estableció.

**KJ-8.** La victimología **no nos incluye, pero por primera vez en este lote tampoco nos excluye limpiamente.** No hay una sola víctima latinoamericana documentada en ocho fuentes. Pero el conjunto de objetivos de este actor es global y contiene sectores que sí tenemos: los documentos judiciales nombran **empresas navieras europeas** y varios gobiernos europeos; el expediente de 2026 documenta el **sector hidroeléctrico** indio, el **sector bancario** indio, y círculos de política exterior en Estados Unidos y Corea; y hay una línea sostenida contra **personal diplomático** y contra grupos de disidentes chinos. Valoramos **posibilidad real** *(45–55 %)* de que exista exposición indirecta material en nuestra cartera por la vía marítimo-portuaria o diplomática. **Confianza: baja.** *Base:* inferencia nuestra desde el perfil sectorial; no hay ningún caso regional documentado.

**KJ-9.** Y hay un rasgo de la atribución de 2026 que conviene registrar por lo que dice del método, no del actor: la vinculación de las tres familias nuevas de junio de 2026 —`SHARDLOADER`, `MINIRECON` y `ZOHOMURK`— al actor se sostiene en solapamiento de código con `TONESHELL` **y en una falta de ortografía compartida entre los implantes**. Valoramos **probable** *(55–80 %)* que la atribución sea correcta. **Confianza: moderada.** *Base:* es un indicio de autoría legítimo y bien establecido en la disciplina; pero es el tipo de artefacto que un actor puede plantar deliberadamente, y la fuente no discute esa posibilidad.

**Qué cambiaría estos juicios:** la publicación de un informe de primera mano que documente a este actor contra un objetivo latinoamericano, que convertiría `KJ-8` de inferencia en hecho y cambiaría la clase de este informe de «método» a «amenaza». Y, en el eje de capacidad, la aparición del mismo mecanismo de controlador firmado caducado en un actor distinto, que convertiría `KJ-5` en un problema de plataforma y no de actor. Son los indicadores `I-1` e `I-3` de §O-7.

---

## 2. Resumen ejecutivo

Los dos informes anteriores de este lote llegaron a la misma conclusión por caminos distintos: el primer y el segundo actor del ranking de prevalencia de noviembre de 2026 están ahí por ser ruidosos, no por ser capaces. Uno porque todo su arsenal son scripts sin compilar; el otro porque generó sus implantes con inteligencia artificial y le salieron mal.

**Este informe existe, en parte, para impedir que esa conclusión se generalice**, porque el tercer actor de la misma lista es genuinamente peligroso y la lista no lo distingue de los otros dos.

Mustang Panda lleva al menos doce años operando para los intereses del Estado chino. En enero de 2025, el Departamento de Justicia de Estados Unidos reveló que el FBI, usando una técnica que había desarrollado la policía francesa, había borrado una variante de su malware `PlugX` de 4 258 ordenadores en territorio estadounidense, con autorización judicial. Los documentos del caso contienen la afirmación de atribución más fuerte de todo este lote: que **el gobierno chino pagó a este grupo por servicios de intrusión informática**. Y los objetivos que el tribunal enumera incluyen empresas navieras europeas, varios gobiernos europeos, grupos de disidentes chinos y gobiernos del Indo-Pacífico.

El grupo no se detuvo. Para mediados de 2026 tenía un arsenal renovado, y en agosto de 2026 Kaspersky publicó el hallazgo que define este informe: la puerta trasera `CoolClient` del grupo viene ahora acompañada de un **rootkit que se instala en el núcleo de Windows como un servicio del sistema**, con un controlador llamado `msagent.sys`. Ese rootkit oculta procesos, protege ficheros y claves de registro frente a inspección, y hace algo especialmente grave: **filtra el tráfico de red de manera que las direcciones de su servidor de mando desaparecen de lo que el sistema operativo le cuenta a cualquier programa que pregunte**, incluidos los productos de seguridad. Las víctimas documentadas son organismos gubernamentales de Myanmar, Mongolia, Pakistán y Rusia.

Y el detalle que convierte esto en una decisión nuestra: **el controlador está firmado con un certificado digital válido que caducó en septiembre de 2014.** No es un certificado robado reciente ni una firma falsificada. Es una firma antigua y legítima que Windows sigue aceptando, porque su mecanismo de aplicación de firmas de controladores admite lo firmado antes de una fecha de corte. Doce años después de caducar, ese certificado sigue abriendo la puerta del núcleo del sistema operativo. Cualquier organización que no mantenga una lista de bloqueo de controladores vulnerables tiene esa puerta abierta, y no sólo para este actor.

Hay un segundo mecanismo de abuso de confianza en el expediente, y es de 2025: la investigación de Google sobre un grupo vinculado documentó el secuestro de **portales cautivos de redes wifi** —esas pantallas de «inicie sesión para conectarse» de hoteles y aeropuertos— para redirigir a personal diplomático a una página que imitaba una actualización de un complemento de Adobe. El descargador también estaba firmado digitalmente, y Google pidió públicamente que se tratasen como no confiables los certificados de firma de código emitidos a una empresa concreta de Chengdu.

Entonces, ¿por qué este actor aparece en el ranking de prevalencia junto a los dos ruidosos? Porque hace las dos cosas a la vez. Tiene al menos tres gusanos que se propagan por memorias USB, y un gusano genera detecciones en cada unidad que toca. **El ranking está contando el gusano. La operación de verdad está en el kernel, y ahí no hay nada que contar porque el rootkit se encarga de que no lo haya.**

Para nosotros no hay una sola víctima latinoamericana documentada en ocho fuentes. Pero a diferencia de los dos informes anteriores, aquí la exclusión no es limpia: este actor opera globalmente y ataca sectores que tenemos —naviero y portuario, hidroeléctrico, bancario, diplomático—. Lo que pedimos no es que se trate como amenaza probable; es que se cierren dos puertas de confianza que están abiertas y que cuestan poco cerrar.

<!-- cti:cards -->

| Rasgo | Qué significa | Etiqueta |
|---|---|---|
| Tercero del ranking **y** genuinamente capaz | El ranking no discrimina entre ruido y peligro. Corrige la lectura fácil de los dos informes anteriores | `01 · corrección` |
| Rootkit con firma válida en el kernel de Windows | Oculta procesos, protege ficheros y **borra su C2 de lo que el sistema le cuenta al EDR** | `02 · kernel` |
| Certificado caducado en 2014 que Windows sigue aceptando | No es un fallo del actor: es el modelo de confianza de la plataforma. **Es una decisión de arquitectura, no de SOC** | `03 · confianza` |
| Sobrevivió a que el FBI le borrara 4 258 equipos | El desmantelamiento judicial no degradó su capacidad. Rearmado en meses | `04 · resiliencia` |
| Secuestro de portales cautivos de wifi | Vector contra personal en viaje, en hoteles y aeropuertos. No hay control de red propio que lo cubra | `05 · movilidad` |
| Tres gusanos de USB documentados | Explican su volumen en el ranking y son la parte visible. **La parte visible es la señuelo** | `06 · ruido` |
| Documentos judiciales: el Estado chino **pagó** al grupo | La atribución más fuerte del lote, y aun así sin personas acusadas | `07 · atribución` |
| Objetivos: naviero europeo, hidroeléctrico, bancario, diplomático | Sectores que sí tenemos. La exposición indirecta deja de ser hipotética | `08 · exposición` |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `7,52` | Porcentaje de la actividad estatal global que Trellix le atribuye, abr–sep 2026 | **Tercer puesto**, y primero entre los actores china-nexus |
| `8,78` | Porcentaje en el tercer trimestre de 2026 aislado | Sube, **mientras el bloque chino en conjunto cae un 41,4 % en el semestre** |
| `4 258` | Ordenadores de los que el FBI borró `PlugX` entre agosto de 2024 y enero de 2025 | Con órdenes del Distrito Este de Pensilvania y técnica desarrollada por la policía francesa |
| `2014` | Año en que caducó el certificado que firma el rootkit de kernel | **Válido de agosto de 2013 a septiembre de 2014. Windows lo acepta doce años después** |
| `4` | Países con víctimas gubernamentales del rootkit de `CoolClient` | Myanmar, Mongolia, Pakistán y Rusia |
| `3` | Gusanos de medios extraíbles documentados | `HIUPAN`, `SnakeDisk` y las variantes `PlugX`/`DOPLUGS` |
| `2` | Veces que el actor ha llevado código al kernel de Windows en doce meses | Diciembre de 2025 (cargando `TONESHELL`) y agosto de 2026 (`CoolClient`) |
| `12` | Designaciones comerciales y estatales distintas del mismo actor | Más una vinculada por Google. Véase §O-1 |
| `~24` | Víctimas de la campaña de secuestro de portales cautivos | Personal diplomático del Sudeste Asiático y de otros lugares |
| `3` | Familias de implante nuevas documentadas sólo en junio de 2026 | `SHARDLOADER`, `MINIRECON`, `ZOHOMURK` |
| `0` | Víctimas latinoamericanas documentadas en ocho fuentes de primera mano | **Pero el perfil sectorial sí nos alcanza.** Véase `KJ-8` |
| `2012` | Año de inicio de actividad según la ficha de MITRE | Las fuentes discrepan: 2011, 2012 y 2014 según cuál se lea |

<!-- cti:note type="good" -->

> ✅ **Decisiones que se solicitan a Dirección.** (a) **Activar la lista de bloqueo de controladores vulnerables de Microsoft y, donde sea viable, exigir controladores firmados con certificado vigente**, con política de integridad de código que rechace firmas anteriores a la fecha de corte. Es la única decisión de este informe que cierra una puerta real y abierta, y aplica contra cualquier actor, no contra éste — 60 días. (b) **Resolver la visibilidad en el arranque de controladores**: inventario de controladores de terceros cargados en el parque y alerta sobre la creación de servicios de tipo controlador de núcleo. Sin esto, un rootkit firmado es invisible por diseño — 90 días. (c) **Política de medios extraíbles**: la misma decisión `E-e` de `CTI-2026-025`, que ahora tiene un segundo actor de apoyo y tres gusanos distintos — 90 días. (d) **Política de conexión en redes no confiables** para personal en viaje: túnel obligatorio antes de cualquier navegación, y prohibición de instalar actualizaciones de software ofrecidas por un portal cautivo. Cubre el vector de `KJ-5` del expediente de 2025 y cuesta una circular — 45 días. (e) **Revisión de cartera marítimo-portuaria, hidroeléctrica y de representación diplomática**: qué contratos nuestros o de nuestros clientes tocan esos sectores. Es la decisión que determina si `KJ-8` nos aplica — 90 días. (f) **Corregir la nota de priorización emitida tras `CTI-2026-025` y `CTI-2026-026`**: el criterio no es «puesto alto implica ruido» sino «el puesto no informa en ninguna dirección» — 15 días, y es urgente porque una instrucción mal entendida es peor que ninguna.

---

## 3. Alcance, requisitos y limitaciones

**3.1 Requisitos de inteligencia atendidos**

| Req. | Enunciado | ¿Respondido? | Dónde |
|---|---|---|---|
| PIR-01 | ¿Qué actores tienen intención y capacidad contra nuestro sector y geografía? | **Parcialmente**: capacidad sí, intención sobre nuestra geografía no documentada | `KJ-8`, §E-2 |
| PIR-04 | ¿Qué amenazas operan contra la región hispanohablante? | **Ninguna documentada de este actor** | §E-2 |
| PIR-07 | ¿Qué técnicas invalidan nuestros controles actuales? | **Sí, y es la aportación central**: un rootkit de kernel firmado invalida el EDR en el mismo plano | `KJ-4`, `KJ-5`, §O-3 |
| PIR-10 | ¿Está vigente y es fiable la inteligencia de la que dependemos? | **Sí, y aquí la respuesta es positiva**: el expediente mejor sostenido del lote | §O-6, Anexo B |
| PIR-11 | ¿Qué abusos de la cadena de confianza (firma de código, certificados) nos afectan? | **Sí — dos mecanismos distintos documentados** | `KJ-5`, §T-1, §X-5 |
| PIR-14 | ¿Degrada la acción policial internacional la capacidad de los actores que nos preocupan? | **Sí, y la respuesta es que no de forma duradera** | `KJ-6`, §E-3 |
| — | ¿Es fiable el ranking de prevalencia como criterio de priorización? | **Sí, y corrige la respuesta de los dos informes anteriores** | `KJ-2`, §E-1 |
| — | ¿Estamos ya comprometidos? | **No evaluable** — sin telemetría propia | §O-4, `G-1` |

**3.2 Fuera de alcance.** No se evalúa: la actividad del actor anterior a agosto de 2024, salvo lo que los documentos judiciales aportan como contexto; el análisis de ingeniería inversa de cada familia del arsenal, para el que las fuentes citadas son la referencia; la relación con los clústeres `CL-STA-1048` y `CL-STA-1049`, que una fuente documenta operando en paralelo contra los mismos objetivos del Sudeste Asiático y que exigirían producto propio; la actividad del grupo contra la comunidad tibetana y contra grupos de disidentes, que está documentada y cuyo tratamiento requiere consideraciones de derechos humanos fuera del alcance de este producto; y la evaluación del marco jurídico de las operaciones de borrado remoto autorizadas judicialmente, que es materia legal y no de inteligencia.

**3.3 Limitaciones de la colección.** (i) **El informe primario de Kaspersky sobre el rootkit no se leyó íntegro.** `KJ-4` y `KJ-5` se sostienen en coberturas múltiples y coincidentes que citan el análisis, no en el análisis mismo. Las coberturas concuerdan en el nombre del controlador, en su mecanismo, en el rango de validez del certificado y en los cuatro países víctima, lo que eleva la confianza; pero **ninguna de ellas nombra al titular del certificado**, que es el dato que permitiría comprobar si está en alguna lista de revocación. Brecha `G-2`. (ii) **La página del informe de Trellix no pudo leerse** (HTTP 403): misma limitación que los dos informes anteriores del lote. (iii) **Los documentos judiciales no se leyeron en original.** La afirmación de `KJ-7` —que el Estado chino pagó al grupo— proviene de coberturas que citan los documentos del caso. **Y las fuentes secundarias discrepan sobre su alcance**: una presenta la afirmación como establecida por el tribunal, otra subraya que no hay personas acusadas ni servicio designado y que la acción fue una disrupción técnica. Se recoge la versión conservadora. Brecha `G-3`. (iv) **Sin telemetría propia.** (v) **Las fuentes discrepan sobre el año de inicio del actor**: 2011, 2012 y 2014 según cuál se lea. Se toma 2012 por ser el de MITRE y se anota. (vi) **El expediente de alias tiene una ambigüedad declarada**: una fuente de referencia cruzada entre proveedores advierte que `Camaro Dragon` es sólo una **coincidencia parcial**, por corresponder a un clúster solapado de implantes en enrutadores. Se recoge en §O-1 con ese matiz. (vii) **La vinculación de `UNC6384` a este actor es de la propia fuente que lo designó**, con el grado de certeza que ella declara; y hubo al menos una confusión pública relevante, con un medio especializado atribuyendo inicialmente la campaña a otro actor chino y emitiendo después una corrección. Se consigna porque ilustra el riesgo de propagación de error en esta clase de expediente. (viii) **La campaña de junio de 2026 contra India y sus tres familias nuevas** proviene de un perfil agregador que cita a los investigadores originales, no del informe original. Las cifras y los nombres se recogen con esa salvedad. (ix) **Una fuente sobre el rootkit no es verificable**: la referencia a cuatro gobiernos víctima aparece en una sola cobertura de baja fiabilidad y coincide con la lista de la cobertura principal, por lo que se recoge; cualquier dato que apareciera **sólo** en ella se ha descartado. (x) **No se ha podido determinar si existe lista de revocación aplicable al certificado del controlador**, lo que es precisamente la información que haría operable la decisión `E-a` de forma dirigida. Brecha `G-2`.

**3.4 Metodología.** Disciplinas: OSINT comercial de primera mano (análisis de ingeniería inversa de laboratorio con telemetría global; investigación de inteligencia de amenazas de un gran proveedor de nube), **OSINT judicial** (documentos de un procedimiento federal estadounidense, por vía secundaria), OSINT de marco (MITRE `G0129`), OSINT comercial de telemetría agregada, y **análisis comparativo entre productos propios**: la corrección de `KJ-2` se obtiene contrastando este expediente con los de `CTI-2026-025` y `CTI-2026-026`, que es una técnica que esta cartera puede aplicar precisamente porque los tres se escribieron con el mismo método. Técnicas analíticas estructuradas: análisis de hipótesis competidoras sobre el origen del volumen de telemetría y sobre el efecto del desmantelamiento (§O-6), comprobación de supuestos clave, pre-mortem. Marcos: MITRE ATT&CK v19, Pirámide del Dolor, Cadena de Intrusión, ICD 203, código Admiralty.

---

# NIVEL ESTRATÉGICO
### Para: Consejo · CISO · Riesgo · Arquitectura de plataforma · Dirección de Contratos · Horizonte: 6–24 meses

## E-1. Qué representa este actor: la corrección del lote

Los dos informes anteriores de noviembre de 2026 construyeron un argumento sólido y lo llevaron demasiado lejos. El argumento era que el ranking de prevalencia de proveedor mide fricción entre adversario y sensor, no amenaza. Es correcto. La extensión indebida fue tratar el puesto alto como **indicador de inocuidad**, y este expediente la refuta.

Mustang Panda es tercero en el mismo ranking, por los mismos mecanismos de ruido —tiene tres gusanos de USB—, y es simultáneamente el actor con mayor capacidad técnica demostrada de todo este lote:

| | `CTI-2026-025` Gamaredon | `CTI-2026-026` APT36 | **`CTI-2026-027` Mustang Panda** |
|---|---|---|---|
| Puesto en el ranking | 1.º (9,03 %) | 2.º (7,84 %) | **3.º (7,52 %)** |
| Causa del volumen | Arsenal íntegramente en script, propagación por USB | Producción masiva asistida por IA | **Tres gusanos de USB** |
| Código en el núcleo del sistema | No | No | **Sí, dos veces en doce meses** |
| Abuso de firma de código | No | No | **Sí, dos mecanismos distintos** |
| Víctimas en Europa o EE. UU. | No documentadas | No documentadas | **Documentadas en tribunal** |
| Resistió acción policial | Sin acción policial conocida | Sin acción policial conocida | **Sí, se rearmó en meses** |
| Calidad del expediente público | Un proveedor, metodología declarada | Siete proveedores sin corroborarse | **Ocho fuentes corroboradas, una judicial** |

**La conclusión correcta es que el ranking no informa en ninguna dirección.** No es que el puesto alto signifique ruido; es que el puesto no significa nada sobre la amenaza, y hay que ir a mirar cada caso. Esto es menos satisfactorio que una regla y es lo que hay.

Y hay un segundo hallazgo estructural, más duradero. **Este actor atacó dos veces la misma cosa: la confianza.** Una vez por abajo, metiendo un controlador firmado en el núcleo del sistema operativo con un certificado caducado que el sistema sigue aceptando. Otra por el lado del usuario, secuestrando el portal cautivo de una red wifi para ofrecer una actualización de software firmada digitalmente. En ambos casos **el control que falló no fue un control de seguridad que no estuviera puesto: fue un mecanismo de confianza que funcionó como está diseñado.**

<!-- cti:cards -->

| Cambio estructural | Por qué nos afecta | Etiqueta |
|---|---|---|
| El adversario entra en el núcleo del sistema | Un rootkit en el kernel está en el mismo plano de privilegio que el EDR, o por debajo. **Puede mentirle.** La detección deja de ser fiable en el propio equipo | `01 · plano de privilegio` |
| Un certificado caducado hace doce años sigue abriendo el kernel | La aplicación de firma de controladores acepta lo firmado antes de la fecha de corte. **Es deuda de compatibilidad de la plataforma, y la paga el defensor** | `02 · confianza heredada` |
| La red en la que trabaja el empleado no es nuestra | El portal cautivo de un hotel es infraestructura de un tercero desconocido con capacidad de redirigir tráfico. El control es de política de movilidad | `03 · movilidad` |
| El desmantelamiento judicial no degrada la capacidad | 4 258 equipos limpiados y el actor rearmado en meses. **La acción policial compra tiempo, no seguridad** | `04 · resiliencia` |
| La atribución más fuerte viene de un tribunal, no de un proveedor | Documentos judiciales afirman pago estatal por servicios de intrusión. Tiene consecuencias de cumplimiento y de cadena de suministro | `05 · atribución` |
| Un gusano de USB tapa una operación de kernel | **El ruido de un actor puede ser la medida equivocada de su capacidad, y a veces es deliberado** | `06 · instrumentación` |

## E-2. Victimología

<!-- cti:bars title="Países y regiones con víctimas documentadas, por número de fuentes que lo afirman" -->

| Objetivo | Fuentes |
|---|---|
| Taiwán | `4` |
| India (gobierno, hidroeléctrico, banca) | `3` |
| Gobiernos del Sudeste Asiático | `3` |
| Myanmar | `2` |
| Mongolia | `2` |
| Pakistán | `2` |
| Gobiernos europeos | `2` |
| Estados Unidos (círculos de política exterior) | `2` |
| Filipinas | `2` |
| Vietnam | `1` |
| Rusia | `1` |
| Empresas navieras europeas | `1` |
| Grupos de disidentes chinos | `1` |
| Comunidad tibetana | `1` |
| Corea del Sur (círculos de política) | `1` |
| **Latinoamérica** | `0` |

<!-- cti:bars title="Sectores objetivo documentados" -->

| Sector | Fuentes |
|---|---|
| Gobierno y administración pública | `6` |
| Cuerpo diplomático y exteriores | `3` |
| Política exterior y centros de análisis | `2` |
| Marítimo y naviero | `1` |
| Energía (hidroeléctrica) | `1` |
| Banca | `1` |
| Sociedad civil y grupos disidentes | `2` |

> **Lectura clave, y es distinta de la de los dos informes anteriores.** En
> Gamaredon y en APT36 la exclusión geográfica era limpia: actores de teatro
> único cuyo conjunto de objetivos no nos contiene ni nos contendría. **Aquí no
> es así.** Este actor opera en cuatro continentes, ataca gobiernos europeos y
> círculos de política estadounidenses, y los documentos judiciales nombran
> **empresas navieras europeas**. Un actor de recolección estratégica china con
> interés documentado en logística marítima, hidroelectricidad y banca **no
> tiene ninguna razón estructural para excluir el Pacífico sur**, y la ausencia
> de víctimas regionales documentadas puede reflejar falta de telemetría
> publicada antes que falta de actividad. Es la misma lectura de ausencia que
> `CTI-2026-023` aplicó a Machete, y conduce a la misma recomendación: no tratar
> el cero como un hecho, sino como una pregunta de colección (brecha `G-5`).
>
> El contraste útil está dentro de esta misma cartera: `CTI-2026-017` documenta
> un actor alineado con los intereses de China con **el 90 % de sus objetivos en
> Sudamérica**. La región no está fuera del interés de recolección chino; está
> fuera del expediente público **de este actor concreto**.

## E-3. Tendencia y pronóstico

La serie de dos años tiene una forma clara: desmantelamiento, rearme, y escalada de privilegio.

<!-- cti:chart title="Hitos de capacidad documentados por semestre" cap="Cuenta cambios documentados de capacidad o de herramienta, no víctimas ni detecciones." -->

| Periodo | Hitos |
|---|---|
| `H2 2024` | `2` |
| `H1 2025` | `4` |
| `H2 2025` | `4` |
| `H1 2026` | `5` |
| `H2 2026` | `2` |

<!-- cti:cards -->

| Escenario | Desarrollo | Etiqueta |
|---|---|---|
| Consolidación en el kernel | El actor mantiene y extiende el componente de núcleo, que pasa a ser estándar en su cadena. **Es el escenario que obliga a la decisión `E-a`**, porque la detección en el espacio de usuario deja de ser fiable | `Probable · 55–80 %` |
| Difusión del abuso de controlador firmado caducado | Otros actores adoptan el mismo mecanismo, que no requiere capacidad especial: sólo un controlador antiguo firmado y vulnerable. **El escenario de mayor impacto para nosotros, porque no depende de este actor** | `Probable · 55–80 %` |
| Continuidad de la propagación por USB | Mantiene sus gusanos y por tanto su puesto en los rankings, independientemente de su actividad real | `Probable · 55–80 %` |
| Segunda acción policial internacional | Dado el precedente de 2025 y la atribución judicial existente, es plausible. **El pronóstico asociado es que tampoco degradará la capacidad de forma duradera**, por `KJ-6` | `Posibilidad real · 45–55 %` |
| Ampliación documentada a Latinoamérica | No por cambio de intención del actor, sino porque **aparezca telemetría regional publicada**. Es `KJ-8` y la brecha `G-5` | `Posibilidad real · 45–55 %` |
| Abuso de certificados de firma vigentes, no caducados | Escalada natural del mecanismo: comprometer o comprar una entidad firmante activa. El expediente de 2025 ya muestra el uso de certificados emitidos a una empresa concreta | `Poco probable · 20–45 %` |
| Capacidad destructiva | Ninguna documentada en doce años. Es un actor de recolección | `Remoto · 5–10 %` |

## E-4. Decisiones que este informe pide al nivel estratégico

<!-- cti:table highlight="controlador|kernel|certificado|portal cautivo" -->

| # | Decisión | Fundamento | Plazo |
|---|---|---|---|
| E-a | **Activar la lista de bloqueo de controladores vulnerables de Microsoft** en todo el parque Windows, y donde la compatibilidad lo permita exigir por política de integridad de código que los controladores lleven certificado vigente, rechazando las firmas anteriores a la fecha de corte. **Es la única decisión de este informe que cierra una puerta demostrablemente abierta**, y cubre a cualquier actor que use el mismo mecanismo | `KJ-4`, `KJ-5`, §X-5 | 60 días |
| E-b | **Resolver la visibilidad en la carga de controladores**: inventario de controladores de terceros presentes en el parque, y alerta sobre la creación de servicios de tipo controlador de núcleo. Sin esto, el componente de `KJ-4` es invisible por diseño | `KJ-4`, §T-5, §X-3 | 90 días |
| E-c | **Política de conexión en redes no confiables** para personal en viaje: túnel obligatorio antes de cualquier navegación, y prohibición expresa de instalar actualizaciones de software ofrecidas tras conectarse a una red ajena. Cubre el secuestro de portal cautivo y **cuesta una circular y una configuración de cliente** | §T-1, §X-5 | 45 días |
| E-d | **Política de medios extraíbles y de unidades compartidas.** Es la misma decisión `E-e` de `CTI-2026-025`, que ahora tiene dos actores de apoyo y cuatro gusanos distintos entre ambos expedientes. Si quedó pendiente entonces, este informe es el argumento para desbloquearla | `KJ-3`, §T-1 | 90 días |
| E-e | **Revisión de cartera marítimo-portuaria, hidroeléctrica, bancaria y de representación diplomática**: qué contratos propios o de subcontratistas tocan esos sectores. Es la decisión que determina si `KJ-8` nos aplica, y es de Contratos y Riesgo, no de SOC | `KJ-8`, §E-2 | 90 días |
| E-f | **Corregir por escrito la instrucción de priorización emitida tras los dos informes anteriores.** El criterio correcto no es «puesto alto implica ruido» sino «el puesto no informa: hay que mirar el expediente». **Urgente**, porque una instrucción mal entendida produce peores decisiones que ninguna instrucción | `KJ-2`, §E-1 | 15 días |
| E-g | **Incorporar al plan de colección permanente la vigilancia de dos indicadores**: aparición de este actor contra objetivos latinoamericanos (`I-1`), y aparición del mecanismo de controlador firmado caducado en cualquier otro actor (`I-3`) | `KJ-5`, `KJ-8`, §O-7 | 30 días |
| E-h | **Aceptar formalmente que la acción policial internacional no es un control de riesgo propio.** El precedente de este expediente —4 258 equipos limpiados, actor rearmado en meses— debe informar cómo se comunican a Dirección las noticias de desmantelamientos, que suelen presentarse como resolución y no lo son | `KJ-6`, §E-3 | 30 días |

---

# NIVEL OPERACIONAL
### Para: Jefatura de SOC · Respuesta a Incidentes · Threat Hunting · Arquitectura Windows · Horizonte: semanas–meses

## O-1. Identificación y alias

| Designación | Origen | Grado de equivalencia |
|---|---|---|
| `Mustang Panda` | CrowdStrike; es el nombre de uso más general y el que emplea el ranking de Trellix | **Referencia** |
| `Earth Preta` | Trend Micro | Equivalente |
| `TA416` | Proofpoint | Equivalente |
| `RedDelta` | Recorded Future | Equivalente |
| `BRONZE PRESIDENT` | Secureworks | Equivalente |
| `Stately Taurus` | Palo Alto Networks Unit 42 | Equivalente |
| `Twill Typhoon` | Microsoft (taxonomía vigente) | Equivalente |
| `TANTALUM` | Microsoft (taxonomía anterior) | Equivalente — precede a `Twill Typhoon` |
| `HoneyMyte` | Kaspersky | Equivalente — **es el nombre bajo el que se publicó el hallazgo del rootkit de `KJ-4`** |
| `TEMP.Hex` | Mandiant / Google | Equivalente |
| `Red Lich` · `ClumsyToad` | Diversos | Equivalentes, de uso minoritario |
| `G0129` | MITRE ATT&CK | Equivalente — ficha de grupo |
| `Camaro Dragon` | Check Point | **Coincidencia parcial.** Una fuente de referencia cruzada entre proveedores advierte expresamente que corresponde a un **clúster solapado de implantes en enrutadores** y no es equivalencia plena. Tratarlo como alias sin más introduce actividad que puede no ser de este grupo |
| `UNC6384` | Google GTIG | **Vinculado, no equivalente.** Designación propia para el clúster del secuestro de portales cautivos, que su autor relaciona con `TEMP.Hex` por herramientas, objetivos e infraestructura. Es una **vinculación declarada por la fuente**, no una fusión |

> **Nota de tradecraft.** Doce designaciones equivalentes y **dos que no lo
> son**, y las dos excepciones son las que importan.
>
> La primera, `Camaro Dragon`, es un caso de libro del problema que
> `CTI-2026-022` documentó como asunto operativo: un nombre que la industria usa
> como sinónimo y que su propio origen define sobre un clúster distinto. Quien
> busque «Camaro Dragon» y vuelque el resultado en el expediente de Mustang
> Panda estará mezclando actividad de implantes de enrutador que puede ser de
> otro operador.
>
> La segunda, `UNC6384`, ilustra el riesgo de propagación de error. Es una
> designación de clúster que su autor vincula a este grupo con el grado de
> certeza que declara. Cuando se publicó, **al menos un medio especializado
> atribuyó la campaña a otro actor chino y tuvo que emitir una corrección
> posterior**, y una fuente agregadora sigue sosteniendo la atribución errónea.
> La lección es la del Anexo D de `CTI-2026-026`: en expedientes china-nexus, la
> designación de clúster se propaga más rápido que la corrección.

## O-2. Estructura y atribución

| Eje de atribución | Valoración | Confianza |
|---|---|---|
| Clúster técnico | **Coherente y bien documentado.** Doce años de continuidad, linaje de herramientas trazable (`PlugX` → `TONESHELL` → `LOTUSLITE` / `CoolClient`), y en 2026 una atribución por solapamiento de código y por falta de ortografía compartida | Alta |
| Grupo organizado | **Sí, con capacidad de desarrollo en el espacio de núcleo**, que es un umbral que la mayoría de los actores de esta cartera no alcanza. Y con capacidad de rearme tras pérdida de infraestructura | Alta |
| Nexo estatal | **República Popular China.** Los documentos judiciales afirman que el gobierno **pagó** al grupo por servicios de intrusión, incluido el uso de `PlugX`. **Es la atribución más fuerte de todo el lote** | Moderada–Alta |
| Servicio u organismo concreto | **Ninguno designado públicamente** | Nula |
| Identidad nominal | **Ninguna persona acusada.** La acción de enero de 2025 fue una disrupción técnica, no una imputación | Nula |
| Relación con `UNC6384` | Vinculación declarada por la fuente que lo designó | Moderada |
| Relación con `CL-STA-1048` y `CL-STA-1049` | Operación en paralelo contra los mismos objetivos del Sudeste Asiático, documentada por una fuente. Fuera de alcance | Baja |

*Razonamiento.* La atribución de este actor es la más sólida de la cartera por una razón de **clase de fuente**: proviene de un procedimiento judicial federal, donde la afirmación de que un gobierno pagó por servicios de intrusión se hace con consecuencias procesales. Ninguna valoración de proveedor tiene ese peso.

A eso se añade coherencia de doce años: un linaje de herramientas trazable, una victimología consistente con las prioridades de recolección estratégica de un Estado —diplomacia, política exterior, logística marítima, energía, disidencia— y ninguna monetización en doce años pese a tener gusanos capaces de propagarse indiscriminadamente.

*Contraargumento, y es importante no pasarlo por alto.* **No hay personas acusadas y no hay servicio designado.** La diferencia con el expediente de Gamaredon en `CTI-2026-025` es instructiva: allí hay cinco personas identificadas nominalmente por un servicio de seguridad nacional y una unidad concreta señalada; aquí hay una afirmación en un escrito judicial sin imputación. Y las fuentes secundarias discrepan sobre qué estableció exactamente el tribunal: una lo presenta como hecho probado, otra subraya que la acción fue técnica. **Este informe recoge la versión conservadora** y marca la discrepancia como brecha `G-3`.

*Observación sobre el método de atribución de 2026.* La vinculación de `SHARDLOADER`, `MINIRECON` y `ZOHOMURK` descansa en solapamiento de código con `TONESHELL` y en **una falta de ortografía compartida entre los implantes**. Es un indicio de autoría legítimo y de uso corriente en la disciplina: una errata idiosincrásica reutilizada sugiere un mismo desarrollador o una misma base de código. Pero es también **exactamente el tipo de artefacto que se puede plantar**, y la fuente no discute esa posibilidad. Se recoge en `KJ-9` con confianza moderada por ese motivo.

## O-3. Modelo de operación: el ruido arriba, la operación abajo

Lo que distingue a este actor no es ninguna de sus piezas por separado, sino **la separación entre la capa que se ve y la que opera**.

**La capa visible: propagación por medios extraíbles.** Hay al menos tres gusanos documentados. `HIUPAN` —también llamado `MISTCLOAK` o `U2DiskWatch` según el proveedor— oculta sus ficheros en un directorio escondido de la unidad y deja visible **un único ejecutable de aspecto legítimo llamado `USBConfig.exe`**, para que el usuario que abre el pendrive vea algo plausible. Su función es entregar la puerta trasera `PUBLOAD` mediante una DLL maliciosa que una fuente llama `Claimloader` y otra pliega dentro de `PUBLOAD`. `SnakeDisk` es un segundo gusano, documentado en septiembre de 2025 junto a una versión actualizada de `TONESHELL`. Y las variantes `PlugX`/`DOPLUGS` llevan años propagándose por el mismo medio: fue precisamente la masa de infecciones de `PlugX` acumulada en ordenadores de particulares y pequeñas organizaciones la que motivó la operación de borrado del FBI.

Esta capa es la que alimenta el ranking. Un gusano en un pendrive que circula por una oficina produce detecciones en cada equipo que lo lee, sin que ninguno de ellos sea un objetivo.

**La capa operativa: el núcleo del sistema.** En agosto de 2026, la puerta trasera `CoolClient` apareció acompañada de un controlador de núcleo llamado `msagent.sys`, instalado como servicio de Windows. Sus tres capacidades, en orden de gravedad creciente:

1. **Ocultación de procesos.** El proceso del implante desaparece de las enumeraciones.
2. **Protección de ficheros y claves de registro.** Los artefactos del implante resisten la inspección y el borrado desde el espacio de usuario.
3. **Filtrado del tráfico de red.** Y ésta es la grave: el controlador **retira las direcciones de mando y control configuradas de la información de red que el sistema devuelve al espacio de usuario**. Es decir, un programa que pregunte al sistema operativo por sus conexiones activas **recibe una respuesta en la que el canal del adversario no existe**. Eso incluye, en principio, a cualquier producto de seguridad que obtenga su visibilidad de red por esa vía.

La puerta trasera y el controlador se comunican por peticiones `IOCTL`, el mecanismo estándar de control de dispositivos de Windows.

Y no es la primera vez: en diciembre de 2025 el mismo laboratorio había documentado **otro** rootkit de núcleo de este actor, usado para cargar `TONESHELL`. Dos incursiones en el kernel en doce meses, con diseños comparables.

**La llave: el certificado.** El controlador está firmado con un certificado **válido entre agosto de 2013 y septiembre de 2014**. Caducado hace doce años, y aceptado. El mecanismo de aplicación de firma de controladores de Windows admite controladores firmados antes de su fecha de corte, para no romper la compatibilidad con hardware antiguo. **Esa decisión de compatibilidad es la puerta.** No hace falta robar un certificado vigente ni comprometer una entidad de certificación: basta con conseguir un controlador antiguo firmado, o la clave de uno.

**El tercer vector, para objetivos en movimiento: el portal cautivo.** La campaña de 2025 del clúster vinculado explotó el comportamiento de comprobación de conectividad de los navegadores. Cuando un equipo se conecta a una red wifi, el navegador solicita una dirección fija para comprobar si hay acceso a internet; si la red responde con una redirección, el navegador muestra la página de inicio de sesión. **Quien controla la red controla esa página.** Los operadores dirigieron a personal diplomático a una página que imitaba el sitio de actualización de un complemento de Adobe, y entregaron un descargador llamado `STATICPLUGIN` **firmado digitalmente**, que a su vez traía `CANONSTAGER`, que cargaba en memoria una variante cifrada de `PlugX` etiquetada `SOGU.SEC`. Unas dos docenas de víctimas. Y el proveedor que lo investigó pidió públicamente que se tratasen como no confiables **los certificados de firma de código emitidos a una empresa concreta de Chengdu**.

> **La lectura conjunta.** Tres vectores, y los tres atacan un mecanismo de
> confianza en vez de una vulnerabilidad: la confianza del usuario en el icono de
> un fichero en un pendrive, la confianza del navegador en la red a la que se
> acaba de conectar, y la confianza del sistema operativo en una firma de hace
> doce años. **Ninguno de los tres se parchea.** Los tres se cierran con
> política, y por eso las decisiones del §E-4 son casi todas de política y no de
> herramienta.

## O-4. Nuestra exposición

> ⬛ **Sección sin evaluar — requiere inventario y telemetría internos.** A
> diferencia de los dos informes anteriores del lote, aquí **algunas preguntas sí
> buscan compromiso**, porque el actor tiene victimología global y nuestra
> ausencia del expediente puede ser falta de observación (brecha `G-5`).

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| X-1 | **¿Está activada la lista de bloqueo de controladores vulnerables de Microsoft en el parque Windows?** ¿En todos los equipos o sólo en los nuevos? | Configuración de integridad de código | Arquitectura Windows |
| X-2 | **¿Qué controladores de terceros están cargados en el parque, y cuántos llevan certificado caducado?** | Inventario de controladores | Arquitectura Windows / TI |
| X-3 | ¿Alertamos sobre la creación de servicios de tipo controlador de núcleo? ¿Tenemos registro de carga de controladores? | EDR / auditoría | SOC |
| X-4 | ¿Existe `msagent.sys` en el parque, con esa ruta o con otra? ¿Coincide su firma con la del controlador legítimo de Microsoft de nombre similar? | Búsqueda de ficheros | SOC |
| X-5 | ¿Confía nuestro EDR en la enumeración de red del sistema operativo, o tiene su propia vista del tráfico? **Pregunta directa al proveedor** | Proveedor de EDR | SOC |
| X-6 | ¿Tenemos telemetría de red independiente del endpoint (NetFlow, registros de proxy, DNS) con la que **contrastar** lo que el endpoint reporta? | Arquitectura de red | SOC / Redes |
| X-7 | ¿Permitimos la ejecución desde medios extraíbles? ¿Existe `USBConfig.exe` en algún medio o equipo del parque? | Política / búsqueda | TI / SOC |
| X-8 | ¿Qué equipos se han conectado a redes wifi ajenas en los últimos 90 días, y navegaron antes de establecer el túnel? | Registros de VPN / cliente | SOC / Redes |
| X-9 | ¿Hay software instalado desde descargas realizadas tras conectarse a una red no corporativa? | Inventario de software | TI |
| X-10 | ¿Están en nuestras listas de confianza los certificados de firma de código que el proveedor de nube señaló como no confiables? | Almacén de certificados | Arquitectura Windows |
| X-11 | ¿Tocan nuestros contratos, o los de nuestros subcontratistas, los sectores marítimo-portuario, hidroeléctrico, bancario o de representación diplomática? | Cartera de contratos | Contratos / Riesgo |
| X-12 | ¿Hemos buscado alguna vez indicadores de `PlugX` histórico en nuestros datos de retención? Es la familia de la que el FBI limpió 4 258 equipos | Retrohunt | SOC |

## O-5. Cronología

<!-- cti:timeline -->

| Fecha | Hecho | Traza |
|---|---|---|
| `2012` | Año de inicio de actividad según MITRE. *Otras fuentes dicen 2011 o 2014* | Global |
| `2022-fin` | Primer uso registrado de `Claimloader` contra organismos del gobierno filipino | Filipinas |
| `2024-08` | **Comienza la operación de borrado remoto de `PlugX`** autorizada judicialmente, con técnica desarrollada por la policía francesa | EE. UU. |
| `2024-fin` → `2025-05` | Campaña contra Filipinas, Estados Unidos, Pakistán y Taiwán | Multirregional |
| `2025-01-15` | **Se revela públicamente el desmantelamiento: `PlugX` borrado de 4 258 ordenadores**, con órdenes del Distrito Este de Pensilvania. Los documentos afirman que el gobierno chino pagó al grupo por servicios de intrusión | EE. UU. |
| `2025-06` | Campaña específica contra la comunidad tibetana, con `PUBLOAD` y `Pubshell` | Tibet / diáspora |
| `2025-06-01` → `2025-08-15` | **Campaña del gusano `HIUPAN`**, que entrega `PUBLOAD` por medio de la DLL `Claimloader`. Foco en Taiwán | Taiwán |
| `2025-08` | **Campaña de secuestro de portales cautivos de wifi** contra personal diplomático: `STATICPLUGIN` firmado → `CANONSTAGER` → `SOGU.SEC` en memoria. ~24 víctimas. Un medio especializado atribuye erróneamente la campaña a otro actor chino y corrige después | Sudeste Asiático y global |
| `2025-09` | **Aparición del gusano `SnakeDisk`** junto a una versión actualizada de `TONESHELL` | Multirregional |
| `2025-12` | **Primera incursión documentada en el núcleo de Windows**: rootkit de kernel usado para cargar `TONESHELL` | Multirregional |
| `2026-03-30` | Informe sobre **tres clústeres china-nexus operando en paralelo** contra un gobierno del Sudeste Asiático: este actor más `CL-STA-1048` y `CL-STA-1049` | Sudeste Asiático |
| `2026-04` | Oleada contra el **sector bancario indio** y círculos de política de Estados Unidos y Corea. Cadena ZIP/LNK que entrega `PlugX`/`DOPLUGS` | India, EE. UU., Corea |
| `2026-06-12` → `2026-06-22` | **Dos campañas simultáneas contra el gobierno y el sector hidroeléctrico de India**, con tres familias nuevas: `SHARDLOADER`, `MINIRECON` y `ZOHOMURK`. Atribución por solapamiento de código con `TONESHELL` **y por una falta de ortografía compartida** | India |
| `2026` | Rearme posterior al desmantelamiento consolidado: `LOTUSLITE` como puerta trasera principal y **vector de ficheros `.msc`** (consola de administración de Microsoft). Objetivos: organizaciones de política de EE. UU. | EE. UU. |
| `2026-08-14` | **Publicación del hallazgo central: rootkit de kernel firmado `msagent.sys` acompañando a `CoolClient`.** Certificado válido de agosto de 2013 a septiembre de 2014. Víctimas gubernamentales en Myanmar, Mongolia, Pakistán y Rusia | Multirregional |
| `2026-10-28` | El informe trimestral de ESET sobre abril–septiembre de 2026 **no nombra a este actor** entre los clústeres china-nexus que destaca, y sí a otros dos. Dato de contraste de visibilidad entre proveedores | — |
| `2026-11-04` | **Trellix lo publica en tercer puesto del ranking global (7,52 %; 8,78 % en Q3), primero entre los china-nexus, en un semestre con caída del 41,4 % del bloque chino** | Global |

## O-6. Hipótesis alternativas consideradas

Tres cuestiones requieren análisis en este expediente.

**Cuestión 1 — ¿Por qué un actor con rootkit de kernel aparece en un ranking de prevalencia?**

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| **H1 — El ranking cuenta el gusano, no la operación** | Tres gusanos de USB documentados. La propagación por medios extraíbles produce detecciones en equipos que no son objetivo. La operación de núcleo, por construcción, no produce detecciones que contar. **Es la que se retiene** | `Retenida · probable 55–80 %` |
| **H2 — Las dos capas son deliberadamente separadas** | Que el actor mantenga una capa ruidosa y desechable —gusanos y `PlugX` heredado— que absorbe la atención y el esfuerzo defensivo, mientras la operación selectiva va por el kernel. **No hay evidencia de intención**, y la explicación más simple es acumulación histórica de herramientas. Se consigna porque, si fuera cierta, el ruido sería un control de contrainteligencia y no un descuido | `Posibilidad real · 45–55 %` |
| **H3 — Volumen genuinamente alto de operaciones** | El expediente de 2026 documenta campañas simultáneas en India, el Sudeste Asiático, EE. UU. y Corea, más cuatro países con el rootkit. **Compatible con H1 y probablemente aditiva**: este actor sí opera mucho | `Retenida parcialmente · probable 55–80 %` |

**Cuestión 2 — ¿Qué efecto tuvo el desmantelamiento de enero de 2025?**

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| **H4 — Efecto táctico sin efecto estratégico** | Limpió una base instalada heredada de `PlugX` en equipos de terceros, muchos de ellos no objetivo, y no afectó a la capacidad de desarrollo ni a las operaciones dirigidas. El actor estaba rearmado con familias nuevas en el mismo año. **Es la que se retiene** | `Retenida · muy probable 80–95 %` |
| **H5 — El desmantelamiento forzó la escalada al kernel** | Que la pérdida de infraestructura y el escrutinio internacional empujaran al actor a buscar sigilo de otro orden. **Cronológicamente encaja** —el primer rootkit es de diciembre de 2025, once meses después— pero la correlación temporal no es evidencia, y el desarrollo en el espacio de núcleo no se improvisa en once meses | `Posibilidad real · 45–55 %` |
| **H6 — Sin relación entre ambos hechos** | La escalada al kernel responde a la mejora general de los productos de seguridad en el espacio de usuario, no a la acción policial. **Es la explicación más económica** y no se puede distinguir de H5 con las fuentes disponibles | `Retenida como alternativa · posibilidad real 45–55 %` |

**Cuestión 3 — ¿Qué significa la ausencia de víctimas latinoamericanas?**

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| **H7 — Falta de telemetría publicada, no de actividad** | El actor opera en cuatro continentes y ataca sectores presentes en la región. Ningún proveedor con telemetría regional publica sobre él. **Y el contraste interno de la cartera lo apoya**: `CTI-2026-017` documenta un actor alineado con China con el 90 % de sus objetivos en Sudamérica, es decir, la región **sí** está en el interés de recolección chino. Se retiene | `Retenida · posibilidad real 45–55 %` |
| **H8 — Decisión real del actor sobre su conjunto de objetivos** | Que la recolección estratégica china sobre el Pacífico sur esté asignada a otros clústeres, y que este grupo tenga un mandato geográfico distinto. **Es plausible y consistente con la especialización documentada de los clústeres china-nexus**, y con que `CTI-2026-017` exista como actor separado | `Retenida · posibilidad real 45–55 %` |
| **H9 — Ausencia real de actividad** | Que el actor no haya operado nunca en la región. **No se puede distinguir de H7 y H8**, y doce años sin una sola mención en ocho fuentes le da algún peso | `Poco probable · 20–45 %` |

**Supuesto clave.** El informe asume que **el filtrado de red del rootkit afecta a los productos de seguridad**, es decir, que un EDR que obtenga su visibilidad de red a través del sistema operativo recibirá información manipulada. La fuente describe el mecanismo —retirada de las direcciones de C2 de la información devuelta al espacio de usuario— pero **no afirma que un EDR concreto se vea afectado**, y los productos modernos suelen tener su propio sensor de red. Si el supuesto es falso, la gravedad de `KJ-4` baja, pero las decisiones `E-a` y `E-b` siguen siendo correctas porque el resto de las capacidades del rootkit —ocultación de procesos y protección de artefactos— no dependen de él. **Es la pregunta `X-5` y debería hacerse al proveedor por escrito.**

**Pre-mortem.** Es mayo de 2027 y este informe resultó equivocado. La causa más probable: dedicamos la atención a un rootkit de kernel que nunca nos iba a tocar, y la decisión `E-a` —la lista de bloqueo de controladores— se retrasó por riesgo de compatibilidad hasta que otro actor, mucho más ordinario, usó el mismo mecanismo contra nosotros. **El informe habría tenido razón en el análisis y habría fallado en el encuadre**, por presentar un control de plataforma general como una respuesta a un actor concreto. Segunda causa posible: `KJ-2` corrigió el mensaje de los dos informes anteriores con tanto énfasis que nadie supo ya qué hacer con los rankings, y el criterio de priorización volvió a ser el que había antes.

## O-7. Indicadores y señales de alerta

| # | Indicador observable | Qué señalaría | Disciplina | Responsable |
|---|---|---|---|---|
| I-1 | **Informe de primera mano que documente este actor contra un objetivo latinoamericano** | Convierte `KJ-8` de inferencia en hecho y cambia la clase del informe de método a amenaza. Resuelve la cuestión 3 de §O-6 | OSINT | Célula CTI |
| I-2 | Publicación del titular del certificado del controlador `msagent.sys`, o de una lista de revocación aplicable | Cierra la brecha `G-2` y permite dirigir la decisión `E-a` en vez de aplicarla a ciegas | OSINT | Célula CTI / Arquitectura |
| I-3 | **Uso del mecanismo de controlador firmado con certificado caducado por cualquier otro actor** | Convierte `KJ-5` en un problema de plataforma, no de actor, y eleva `E-a` a prioridad inmediata. **Es el indicador de mayor valor práctico del informe** | OSINT / telemetría | Célula CTI / SOC |
| I-4 | Tercera incursión documentada en el núcleo de Windows por este actor | Confirma el escenario de consolidación de §E-3: el componente de kernel pasa a ser estándar y no excepcional | OSINT | Célula CTI |
| I-5 | Abuso de un certificado de firma de código **vigente** por este actor | Escalada del mecanismo. Las listas de bloqueo por fecha de firma dejarían de cubrir | OSINT | Célula CTI / Arquitectura |
| I-6 | Segunda acción policial internacional contra el actor | Dado el precedente, es plausible. **El indicador útil no es la acción: es qué hace el actor en los doce meses siguientes** | OSINT | Célula CTI |
| I-7 | Aparición de este actor en informes de proveedores con telemetría regional | Primer paso de `I-1`. Vigilar específicamente a los proveedores que publican sobre la región | OSINT | Célula CTI |
| I-8 | Imputación nominal o designación de servicio concreto | Elevaría §O-2 a confianza alta y tendría efectos de cumplimiento y de cadena de suministro | OSINT | Legal / Cumplimiento |
| I-9 | Uso del vector de ficheros `.msc` por otros actores | El vector de consola de administración de Microsoft es nuevo y transferible. Obligaría a una decisión de bloqueo equivalente a la de `.desktop` en `CTI-2026-026` | OSINT | Célula CTI / SOC |

---

# NIVEL TÁCTICO
### Para: Analistas de SOC · Ingeniería de Detección · Threat Hunting · Arquitectura Windows · Horizonte: días–semanas

## T-1. Cadenas de intrusión

> Tres vectores de entrada documentados, con una cadena posterior que converge.
> Se describen por separado porque **las mitigaciones son distintas y ninguna
> cubre a las otras dos**.

<!-- cti:stages title="Vector A · Medios extraíbles: el que alimenta el ranking" dwell="**Permanencia:** la campaña del gusano HIUPAN se midió activa del 2025-06-01 al 2025-08-15, once semanas." -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 01 · Unidad | Gusano en memoria USB con señuelo visible | `HIUPAN` (`MISTCLOAK` · `U2DiskWatch`) · `SnakeDisk` · `PlugX`/`DOPLUGS` · **directorio oculto más `USBConfig.exe` como único fichero visible** |
| Etapa 02 · Carga | Carga lateral de DLL | `Claimloader` (DLL maliciosa) · carga lateral sobre ejecutable legítimo · entrega de `PUBLOAD` |
| Etapa 03 · Mando | Puerta trasera | `PUBLOAD` · `Pubshell` · `PlugX`/`SOGU` |

<!-- cti:stages title="Vector B · Portal cautivo de wifi: el que alcanza al personal en viaje" dwell="**Permanencia:** no publicada. ~24 víctimas documentadas." -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 01 · Red | Secuestro de la comprobación de conectividad del navegador | El navegador solicita una dirección fija para comprobar acceso a internet · **la red responde con redirección** · se muestra la página de «inicio de sesión» |
| Etapa 02 · Señuelo | Página que imita una actualización de software conocida | Imitación del sitio de actualización de un complemento de Adobe |
| Etapa 03 · Descarga | Descargador **firmado digitalmente** | `STATICPLUGIN`, con firma válida · certificados de firma de código emitidos a una empresa de Chengdu |
| Etapa 04 · Carga | Preparador y carga lateral | `CANONSTAGER` · carga en memoria de variante cifrada de `PlugX` (`SOGU.SEC`) |

<!-- cti:stages title="Vector C · Correo y ficheros de administración: el convencional" dwell="**Permanencia:** no publicada." -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 01 · Entrega | Archivador con acceso directo, o fichero de consola de administración | ZIP con `LNK` · **ficheros `.msc` (consola de administración de Microsoft)** |
| Etapa 02 · Carga | Puerta trasera | `PlugX`/`DOPLUGS` · `LOTUSLITE` · `TONESHELL` y variante `ToneShellws` |
| Etapa 03 · Mando | Familias de 2026 | `CoolClient` · `SHARDLOADER` · `MINIRECON` · `ZOHOMURK` · `FDMTP` |

<!-- cti:stages title="Etapa común · Escalada al núcleo: donde deja de verse" dwell="**Permanencia:** indefinida por diseño. El componente existe para que no haya nada que medir." -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 04 · Núcleo | Instalación del rootkit como servicio de controlador | `msagent.sys` · **servicio de Windows de tipo controlador de núcleo** · firma con certificado válido de 2013-08 a 2014-09 |
| Etapa 05 · Ocultación | Tres capacidades del controlador | Ocultación de procesos · protección de ficheros y claves de registro · **filtrado de direcciones de C2 de la información de red devuelta al espacio de usuario** |
| Etapa 06 · Control | Comunicación entre puerta trasera y controlador | Peticiones `IOCTL` desde `CoolClient` hacia el controlador |

**El vector A en detalle, y por qué importa fuera de este actor.** El gusano `HIUPAN` hace algo deliberado con la presentación: crea un directorio oculto donde guarda sus componentes y **deja visible un solo fichero, llamado `USBConfig.exe`**, de modo que el usuario que abre el pendrive ve un ejecutable con nombre plausible y ningún contenido que le haga sospechar que falta algo. Es la misma lógica de los accesos directos con nombre de carpeta de `CTI-2026-025`: **el engaño no está en el fichero malicioso, está en lo que se oculta alrededor.** La carga posterior se hace por carga lateral de DLL, el método más usado de esta cartera.

**El vector B en detalle, y es el que ninguna organización controla.** Cuando un portátil se conecta a una red wifi, el navegador comprueba si hay acceso real a internet solicitando una dirección fija y conocida. Si la respuesta no es la esperada, deduce que hay un portal cautivo y abre la página a la que la red le redirige. Este comportamiento es correcto y necesario: es lo que hace que aparezca la pantalla de «acepte las condiciones» de un hotel.

**Quien controla la red controla esa primera página que el usuario ve, antes de que haya navegado a ningún sitio.** Los operadores la usaron para presentar una imitación del sitio de actualización de un complemento de Adobe, y el fichero que se descargaba estaba **firmado digitalmente con un certificado válido**, de modo que ni el navegador ni el sistema advertían nada. Las dos defensas posibles son de política, no técnicas: **establecer el túnel antes de navegar**, y **prohibir instalar software ofrecido tras conectarse a una red ajena**. Es la decisión `E-c` y cuesta una circular.

**El vector C y el fichero `.msc`.** El uso de ficheros de consola de administración de Microsoft como vector de entrega es la novedad de 2026 de este actor y pertenece a la misma familia de problema que el `.desktop` de `CTI-2026-026`: **una extensión funcional, legítima, poco vigilada por las pasarelas de correo y que la mayoría de las organizaciones no tiene ninguna razón para recibir por correo.** La recomendación es idéntica y está en §X-5.

**La etapa de núcleo en detalle.** El controlador se instala como un servicio de Windows de tipo controlador de núcleo. Una vez cargado, opera en el anillo de privilegio del sistema operativo, es decir, **en el mismo plano que los componentes de núcleo de los productos de seguridad, o por debajo de ellos según el orden de carga**. Sus tres funciones ya se han descrito; la tercera es la que exige una pregunta al proveedor (`X-5`): si nuestro EDR obtiene la lista de conexiones activas preguntándole al sistema operativo, y el controlador filtra esa respuesta, **el EDR informará de un equipo sin conexiones sospechosas con total convicción**. La única verificación independiente posible es contrastar lo que dice el endpoint con lo que dice la red (`X-6`), y eso requiere telemetría de red que no dependa del endpoint.

## T-2. Mapa MITRE ATT&CK

> Construido sobre la conducta documentada en las ocho fuentes. Marco ATT&CK
> v19. Se marca con `(inf.)` lo que es inferencia nuestra a partir de
> descripciones que la fuente no mapea.

<!-- cti:matrix -->

| Táctica | ID | Técnica | Procedimiento observado |
|---|---|---|---|
| Desarrollo de recursos | T1588.003 | Obtain Capabilities: Code Signing Certificates | **Certificado de firma de controlador válido de 2013-08 a 2014-09**; certificados de firma de código emitidos a una empresa de Chengdu |
| Desarrollo de recursos | T1587.002 | Develop Capabilities: Code Signing Certificates | Firma del descargador `STATICPLUGIN` (inf.) |
| Desarrollo de recursos | T1587.001 | Develop Capabilities: Malware | Linaje propio: `PlugX` → `TONESHELL` → `LOTUSLITE` / `CoolClient`, más tres familias nuevas en 2026 |
| Desarrollo de recursos | T1584.004 | Compromise Infrastructure: Server | Control de la infraestructura de red que sirve el portal cautivo (inf.) |
| Acceso inicial | T1091 | Replication Through Removable Media | `HIUPAN`, `SnakeDisk`, `PlugX`/`DOPLUGS` |
| Acceso inicial | T1566.001 | Phishing: Spearphishing Attachment | ZIP con `LNK`; ficheros `.msc` |
| Acceso inicial | T1557 | Adversary-in-the-Middle | **Secuestro del portal cautivo y de la comprobación de conectividad del navegador** |
| Acceso inicial | T1189 | Drive-by Compromise | Página de actualización de complemento falsa servida por la red (inf.) |
| Ejecución | T1204.002 | User Execution: Malicious File | `USBConfig.exe`; descargador firmado presentado como actualización |
| Ejecución | T1204.001 | User Execution: Malicious Link | `LNK` dentro de archivador |
| Ejecución | T1218.014 | System Binary Proxy Execution: MMC | **Ficheros `.msc` de consola de administración de Microsoft** |
| Ejecución | T1569.002 | System Services: Service Execution | Carga del rootkit como servicio |
| Persistencia | T1543.003 | Create or Modify System Process: Windows Service | **Instalación de `msagent.sys` como servicio de Windows** |
| Escalada de privilegios | T1068 | Exploitation for Privilege Escalation | Acceso al espacio de núcleo por controlador firmado (inf.) |
| Sigilo | T1574.001 | Hijack Execution Flow: DLL | `Claimloader`, `CANONSTAGER`, y el método dominante del arsenal |
| Sigilo | T1014 | **Rootkit** | **`msagent.sys`: ocultación de procesos, protección de ficheros y claves, filtrado de red.** Es la técnica central del expediente |
| Sigilo | T1553.002 | Subvert Trust Controls: Code Signing | **El controlador y el descargador llevan firma digital válida** |
| Degradación de defensas | T1685 | Disable or Modify Tools | El filtrado de red del rootkit degrada la visibilidad de los productos de seguridad (inf., y es el supuesto clave de §O-6) |
| Sigilo | T1564.001 | Hide Artifacts: Hidden Files and Directories | Directorio oculto en la unidad USB, con `USBConfig.exe` como único fichero visible |
| Sigilo | T1036.005 | Masquerading: Match Legitimate Name or Location | **`msagent.sys` imita el nombre de un componente legítimo de Windows** |
| Sigilo | T1055 | Process Injection | Carga en memoria de la variante cifrada de `PlugX` (`SOGU.SEC`) |
| Sigilo | T1027.013 | Obfuscated Files or Information: Encrypted/Encoded File | Variante de `PlugX` cifrada y cargada en memoria |
| Sigilo | T1620 | Reflective Code Loading | Carga de `SOGU.SEC` directamente en memoria (inf.) |
| Descubrimiento | T1120 | Peripheral Device Discovery | Los gusanos detectan la conexión de unidades extraíbles |
| Descubrimiento | T1082 | System Information Discovery | `MINIRECON` por su nombre y función declarada |
| Movimiento lateral | T1091 | Replication Through Removable Media | Mismo mecanismo que el acceso inicial |
| Mando y control | T1071.001 | Application Layer Protocol: Web Protocols | HTTP/HTTPS en las familias documentadas |
| Mando y control | T1105 | Ingress Tool Transfer | Descarga de etapas posteriores |
| Mando y control | T1665 | Hide Infrastructure | **El rootkit retira las direcciones de C2 de la información de red del sistema** |
| Mando y control | T1573 | Encrypted Channel | Variante `PlugX` cifrada |
| Exfiltración | T1041 | Exfiltration Over C2 Channel | Por el canal de mando |

## T-3. Dónde atacamos en la Pirámide del Dolor

<!-- cti:pyramid -->

| Nivel | Qué contiene en este informe y qué vale | Valor |
|---|---|---|
| Hashes | Pocos y de poca utilidad: el expediente de este actor es rico en análisis y pobre en indicadores publicados, al contrario que el de `CTI-2026-026`. **Sólo retrohunt** | Base · valor trivial |
| IP · Dominios | Apenas publicados en las fuentes leídas. Y en el vector del portal cautivo **el dominio relevante es la dirección de comprobación de conectividad del propio navegador**, que no se puede bloquear | Valor bajo |
| Artefactos | **El nombre del controlador (`msagent.sys`), el nombre del servicio, `USBConfig.exe`, y sobre todo el certificado de firma con su rango de validez.** El rango de fechas del certificado es el artefacto más valioso del informe: **es una propiedad criptográfica, no una cadena, y no se cambia sin cambiar de certificado** | Valor medio–alto |
| Herramientas | Carga lateral de DLL, `IOCTL`, servicios de controlador, `.msc`. Todas legítimas: detectar por contexto | Valor alto |
| TTP | Los tres vectores de §T-1 y la escalada al núcleo. **Y un nivel por encima: el abuso de tres mecanismos de confianza distintos**, que es lo que define a este actor y lo que no puede cambiar sin dejar de ser él | Cima · valor máximo |

> **Observación de método: hay un cuarto nivel por encima de la pirámide en este
> expediente.** La Pirámide del Dolor mide cuánto le cuesta al adversario que
> detectemos cada cosa. Contra un rootkit de núcleo, **toda la pirámide se vuelve
> sospechosa a la vez**, porque los hashes, los artefactos y las conexiones que
> el equipo nos reporta pasan por un filtro que el adversario controla. La
> respuesta no está en subir de nivel dentro de la pirámide: está en **tener una
> segunda fuente de verdad que no venga del equipo comprometido** —telemetría de
> red independiente, inventario de controladores desde una consola central,
> contraste entre lo que dice el endpoint y lo que dice el conmutador—. Es la
> pregunta `X-6` y es la conclusión arquitectónica de este informe.

## T-4. Hipótesis de caza prioritarias

<!-- cti:accordion critical="^(H-1|H-2|H-3)\b" regional="^H-(9|10)\b" -->

**H-1 — Controladores de núcleo firmados con certificado caducado.** Inventariar todos los controladores de terceros cargados en el parque y extraer de cada uno la fecha de validez de su certificado de firma. Marcar todo el que esté firmado con un certificado **caducado antes de 2016**, y especialmente los de validez anterior a 2015. Ventana: estado actual. **Es la hipótesis central del informe y la única que vale la pena ejecutar aunque este actor no nos toque nunca**: el resultado será una lista de puertas abiertas al núcleo del sistema, y el actor que las use puede ser cualquiera. Fidelidad **alta** como hallazgo de exposición, no como detección de compromiso. Falsos positivos: abundantes y legítimos —controladores de hardware antiguo en servidores heredados, impresoras, equipos industriales—, y **cada uno de ellos es un hallazgo de riesgo, no un falso positivo**.

**H-2 — Creación de servicios de tipo controlador de núcleo.** Buscar en el registro de eventos la creación de servicios cuyo tipo sea controlador de núcleo (`SERVICE_KERNEL_DRIVER`, valor `1` en la clave `Type` del servicio), fuera de las ventanas de instalación de software autorizada. Ventana: 180 días. Fidelidad **muy alta**: en un parque gestionado, la instalación de un controlador de núcleo es un acontecimiento infrecuente y atribuible. Falsos positivos: instaladores de software legítimo, actualizaciones de hardware, agentes de seguridad; todos identificables por el proceso padre y por el ticket de cambio.

**H-3 — Presencia de `msagent.sys` con firma o ruta que no corresponda.** Buscar el fichero `msagent.sys` en el parque. **El criterio no es su presencia** —existe un componente legítimo de Windows de nombre similar— **sino la discordancia**: ruta fuera de `%SystemRoot%\System32\drivers\`, firma que no sea de Microsoft, o fecha de firma anterior a 2015. Fidelidad **muy alta** con el contraste aplicado, **inservible sin él**. Es el mismo principio que la hipótesis `H-4` de `CTI-2026-025`: contrastar el nombre con la propiedad, no buscar el nombre.

**H-4 — Discordancia entre la vista de red del endpoint y la de la infraestructura.** Comparar, para una muestra de equipos, las conexiones salientes que reporta el agente de endpoint con los flujos que registran el cortafuegos, el proxy y el servidor DNS en la misma ventana. **Buscar conexiones que la red vea y el endpoint no.** Ventana: 30 días sobre una muestra. Fidelidad **máxima en concepto** y coste alto en ejecución; es la única caza del informe que puede detectar un rootkit de núcleo **sin confiar en el equipo comprometido**. Es la materialización de `X-6` y la recomendación arquitectónica de §T-3.

**H-5 — Gusanos en medios extraíbles: el señuelo visible.** Buscar en el parque y en los medios extraíbles la presencia de `USBConfig.exe`, y en general **unidades extraíbles que contengan un solo fichero ejecutable visible y uno o más directorios ocultos**. Esa combinación es la firma de presentación de `HIUPAN` y no requiere ningún indicador. Correlacionar con creación de ficheros en directorios ocultos de la unidad. Fidelidad **alta**. Falsos positivos: unidades de instalación de software y llaves de arranque; pocas y enumerables.

**H-6 — Carga lateral de DLL en rutas de perfil o temporales.** Buscar ejecutables legítimos y firmados que carguen una DLL desde el mismo directorio cuando esa DLL **no esté firmada o no corresponda al fabricante del ejecutable**. Es el método de carga dominante de este actor y de buena parte de esta cartera. Fidelidad **alta**, coste de implantación medio: requiere telemetría de carga de módulos, que no todos los productos ofrecen.

**H-7 — Ficheros `.msc` recibidos por correo o descargados.** Buscar en el histórico de la pasarela de correo y de descarga web ficheros con extensión `.msc`, incluidos los contenidos en archivadores. **Si el resultado es cero porque la pasarela no inspecciona dentro de archivadores, ése es el hallazgo**, igual que en `H-10` de `CTI-2026-026`. Fidelidad dependiente de la configuración; valor alto y transferible.

**H-8 — Instalación de software tras conexión a red no corporativa.** Correlacionar los registros de conexión a redes wifi ajenas con la instalación de software o la descarga de ejecutables en las veinticuatro horas siguientes, en equipos de personal que viaja. Ventana: 180 días. Fidelidad **moderada**, y su valor principal es **descubrir si la política de `E-c` se está cumpliendo**, no encontrar un compromiso. Falsos positivos: numerosos y en su mayoría instructivos.

**H-9 — Certificados señalados como no confiables presentes en el almacén de confianza.** Comprobar si los certificados de firma de código que el proveedor de nube señaló públicamente —los emitidos a la empresa de Chengdu mencionada en el expediente de 2025— están presentes o son aceptados en nuestro almacén de confianza. Fidelidad **muy alta** como comprobación de higiene; es una tarea de una hora y responde a `X-10`.

**H-10 — Retrohunt de `PlugX` histórico.** Ejecutar una búsqueda retrospectiva de las familias `PlugX`/`SOGU`/`DOPLUGS` sobre los datos de retención que conservemos. **Es la familia de la que el FBI limpió 4 258 equipos**, en buena parte de particulares y organizaciones pequeñas que nunca fueron objetivo, lo que significa que es una infección de amplia circulación y no dirigida. Fidelidad **moderada** y coste bajo; su valor es cerrar `X-12` con una respuesta por escrito aunque sea negativa.

## T-5. Brechas de visibilidad que hay que cerrar primero

| Brecha | Por qué importa aquí |
|---|---|
| **Sin inventario de controladores de terceros con fecha de certificado** | Es la brecha dominante y la que bloquea `H-1`, que es la única hipótesis del informe con valor independiente del actor. **No es una brecha de registro: es una tarea de inventario que nadie ha hecho** |
| **Sin alerta sobre creación de servicios de controlador de núcleo** | Deja ciega `H-2`. Un rootkit firmado que se instala como servicio es **invisible por diseño** si no se vigila el momento de la instalación: después, él decide qué se ve |
| **Sin telemetría de red independiente del endpoint** | Deja ciega `H-4`, que es la única verificación posible frente a un componente de núcleo. **Es también la conclusión arquitectónica del informe**: contra un rootkit, la segunda fuente de verdad no es un lujo |
| Sin respuesta del proveedor de EDR sobre su fuente de visibilidad de red | Deja sin resolver el supuesto clave de §O-6. Es la pregunta `X-5` y se responde con un correo |
| Sin telemetría de carga de módulos | Deja ciega `H-6`, y con ella el método de carga dominante de este actor y de la mayoría de los de esta cartera |
| Sin inspección recursiva de archivadores en la pasarela de correo | Deja ciega `H-7`. **Es la misma brecha que `CTI-2026-026` identificó para `.desktop`**: dos informes, dos extensiones, un solo control pendiente |
| Sin registro de conexión a redes wifi ajenas | Deja ciega `H-8` y hace imposible verificar el cumplimiento de la decisión `E-c` |
| Sin visibilidad en medios extraíbles | Deja ciega `H-5`. **Tercer informe consecutivo de esta cartera que señala la misma brecha** |
| Sin inventario de certificados aceptados en el almacén de confianza | Deja ciega `H-9`, que es la comprobación más barata del informe |

---

# NIVEL TÉCNICO
### Para: Ingeniería de detección · Arquitectura Windows · Automatización · TIP/SIEM · Vida útil: las detecciones conductuales y las de certificado no caducan

## X-1. Arsenal y capacidad

| Propiedad | Valor |
|---|---|
| **Capacidad diferencial** | **Desarrollo en el espacio de núcleo de Windows.** Dos rootkits distintos en doce meses: diciembre de 2025 (cargando `TONESHELL`) y agosto de 2026 (`msagent.sys` con `CoolClient`). Es el umbral que separa a este actor del resto de este lote |
| Puertas traseras | `PlugX`/`SOGU` y variantes (`DOPLUGS`, `SOGU.SEC`) · `TONESHELL` y `ToneShellws` · `LOTUSLITE` · `CoolClient` · `PUBLOAD` · `Pubshell` · `FDMTP` |
| Familias nuevas de 2026 | `SHARDLOADER` · `MINIRECON` · `ZOHOMURK` — vinculadas por solapamiento de código con `TONESHELL` **y por una falta de ortografía compartida** |
| Gusanos de medios extraíbles | `HIUPAN` (`MISTCLOAK` · `U2DiskWatch`) · `SnakeDisk` · `PlugX`/`DOPLUGS` |
| Preparadores y cargadores | `Claimloader` (plegado dentro de `PUBLOAD` por un proveedor) · `CANONSTAGER` · `STATICPLUGIN` (descargador firmado) |
| Componente de núcleo | **`msagent.sys`**: servicio de Windows de tipo controlador de núcleo. Ocultación de procesos, protección de ficheros y claves de registro, **filtrado de direcciones de C2 de la información de red devuelta al espacio de usuario**. Control por `IOCTL` desde la puerta trasera |
| **Firma de código** | **Dos abusos distintos.** (1) Certificado de firma de controlador emitido a **`Nanjing Ranyi Technology Co., Ltd.`**, **válido de agosto de 2013 a septiembre de 2014**: caducado hace doce años y aceptado por la aplicación de firma de controladores de Windows. **La misma clave firmó varios controladores maliciosos anteriores compilados alrededor de 2013**, sin vínculo establecido con esta actividad. (2) Certificados de firma de código emitidos a una empresa de Chengdu, señalados públicamente como no confiables por el proveedor que investigó la campaña del portal cautivo |
| Método de carga dominante | **Carga lateral de DLL** sobre ejecutables legítimos y firmados |
| Vectores de acceso inicial | Medios extraíbles · **secuestro de portal cautivo de wifi** · ZIP con `LNK` · **ficheros `.msc` de consola de administración** |
| Carga en memoria | Variante cifrada de `PlugX` (`SOGU.SEC`) cargada directamente en memoria por `CANONSTAGER` |
| Plataformas | Windows. Una designación de alias corresponde a un clúster solapado de implantes en **enrutadores**, con la salvedad de equivalencia parcial de §O-1 |
| Capacidad destructiva | **Ninguna documentada en doce años.** Actor de recolección estratégica |
| Resiliencia | **Demostrada.** Rearmado con familias nuevas en el mismo año del desmantelamiento judicial que le borró `PlugX` de 4 258 equipos |
| Disciplina operativa | Mixta: alta en la capa de núcleo, baja en la capa de gusano. **Y una errata reutilizada entre implantes** que sirvió para atribuirlo |

## X-2. Artefactos de host persistentes

<!-- cti:cards -->

| Categoría | Artefactos | Etiqueta |
|---|---|---|
| Componente de núcleo | `msagent.sys` · servicio de Windows de tipo controlador de núcleo (`Type=1`) · **certificado de firma válido de 2013-08 a 2014-09** | `rootkit` |
| Señuelo de medios extraíbles | `USBConfig.exe` como **único fichero visible** en la unidad, con uno o más directorios ocultos junto a él | `gusano` |
| Descargador firmado del vector de portal cautivo | `STATICPLUGIN` · imitación del sitio de actualización de un complemento de Adobe · certificados de firma de código de una empresa de Chengdu | `confianza` |
| Preparador en memoria | `CANONSTAGER` · variante `SOGU.SEC` de `PlugX` cargada sin tocar disco | `memoria` |
| Carga lateral de DLL | `Claimloader` y la técnica general: ejecutable legítimo firmado que carga una DLL del mismo directorio no firmada o de otro fabricante | `carga lateral` |
| Vector de administración | Ficheros `.msc` de consola de administración de Microsoft recibidos por correo o descargados | `vector` |
| Mecanismo de control núcleo-usuario | Peticiones `IOCTL` entre `CoolClient` y el controlador | `protocolo` |
| Artefacto de atribución | **Falta de ortografía compartida** entre `SHARDLOADER`, `MINIRECON` y `ZOHOMURK`, más solapamiento de código con `TONESHELL` | `autoría` |

> ⚠ **Dos advertencias sobre esta tabla, y la segunda es la que importa.**
>
> La primera: **`msagent.sys` es un nombre que imita un componente legítimo de
> Windows.** Buscar el nombre produce falsos positivos; el criterio válido es la
> discordancia de ruta, de firmante o de fecha de firma (`H-3`, `D-3`).
>
> La segunda, y es la razón por la que este informe pide una decisión de
> arquitectura y no una regla: **el artefacto de verdad valioso de este
> expediente no es un nombre ni un hash, es un rango de fechas.** Un certificado
> válido entre agosto de 2013 y septiembre de 2014 que firma un controlador de
> núcleo es una propiedad criptográfica verificable, no una cadena que el
> adversario pueda cambiar al recompilar. **Y es generalizable**: la detección
> correcta no busca este certificado, busca **cualquier controlador de núcleo
> firmado con un certificado caducado**, que es la clase entera del problema.
> Véase `D-1` y la decisión `E-a`.

## X-3. Lógica de detección prioritaria

<!-- cti:detections -->

**D-1 · CRÍTICO — Controlador de núcleo firmado con certificado caducado**

```
event.category == "driver" AND event.action == "load"
AND file.code_signature.exists == true
AND file.code_signature.valid == true
AND file.code_signature.not_after < "2016-01-01"
AND file.code_signature.subject_name NOT IN ( <lista de firmantes autorizados del parque> )
```

→ **Investigación prioritaria con plazo de una hora, y bloqueo por política como objetivo final.** Ésta no es una detección de Mustang Panda: es la detección de **la clase entera de abuso**, y su valor es independiente de este actor. La forma correcta de cerrarla no es detectar sino impedir: lista de bloqueo de controladores vulnerables de Microsoft más política de integridad de código (§X-5, decisión `E-a`). Mientras eso se implanta, esta regla da visibilidad.

**D-2 · CRÍTICO — Creación de un servicio de tipo controlador de núcleo**

```
event.code == 7045                    # Servicio instalado en el sistema
AND service.type == "kernel mode driver"
AND process.parent.executable NOT IN ( <instaladores y agentes autorizados> )
```

```
// Variante por registro, para cubrir la instalación sin pasar por el gestor de servicios:
registry.path MATCHES_REGEX "(?i)\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\[^\\\\]+\\\\Type$"
AND registry.data.strings == "1"
```

→ Contención automática en un parque gestionado, investigación prioritaria en uno heterogéneo. **La instalación de un controlador de núcleo es un acontecimiento infrecuente y atribuible a un cambio**: si no hay ticket, hay incidente.

**D-3 · CRÍTICO — `msagent.sys` con ruta, firmante o fecha discordantes**

```
file.name == "msagent.sys"
AND ( file.directory NOT IN ( "C:\\Windows\\System32\\drivers" )
      OR file.code_signature.subject_name NOT CONTAINS "Microsoft"
      OR file.code_signature.not_after < "2016-01-01" )
```

→ Contención automática. **El criterio es la discordancia, no el nombre.** Existe un componente legítimo de nombre similar; sin las tres condiciones alternativas esta regla sería inservible.

**D-4 · ALTO — Discordancia entre la vista de red del endpoint y la de la infraestructura**

```
// No es una regla de correlación simple: es un trabajo programado de contraste.
// Para cada equipo y ventana de una hora:
CONJUNTO_RED      = destinos observados en NetFlow, proxy y DNS para esa IP
CONJUNTO_ENDPOINT = destinos reportados por el agente en el mismo equipo y ventana
ALERTA SI ( CONJUNTO_RED - CONJUNTO_ENDPOINT ) contiene destinos externos
           no atribuibles a tráfico de sistema operativo o de agente
```

→ Investigación prioritaria. **Es la única detección del informe que no confía en el equipo potencialmente comprometido**, y por tanto la única con validez frente a un rootkit de núcleo. Coste de implantación alto; es la recomendación arquitectónica de §T-3 y la pregunta `X-6`.

**D-5 · ALTO — Carga lateral de DLL: ejecutable firmado cargando módulo discordante**

```
event.category == "library" AND event.action == "load"
AND process.code_signature.valid == true
AND dll.directory == process.executable_directory
AND ( dll.code_signature.exists == false
      OR dll.code_signature.subject_name != process.code_signature.subject_name )
AND process.executable_directory MATCHES_REGEX
      "(?i)\\\\(Users|AppData|Temp|ProgramData|Windows\\\\Temp)\\\\"
```

→ Investigación prioritaria. Cubre `Claimloader`, `CANONSTAGER` y el método dominante de este actor. **Y de buena parte de esta cartera**: es la regla con mayor reutilización entre informes.

**D-6 · ALTO — Unidad extraíble con un único ejecutable visible y directorios ocultos**

```
volume.type == "removable"
AND COUNT( ficheros visibles con extensión ejecutable en la raíz ) == 1
AND COUNT( directorios con atributo oculto en la raíz ) >= 1
```

```
// Variante por nombre literal, de fidelidad alta y cobertura estrecha:
file.name == "USBConfig.exe" AND volume.type == "removable"
```

→ Investigación en el día y **cuarentena del medio**. La primera variante es la conductual y la valiosa: describe la firma de presentación del gusano sin depender de ningún nombre.

**D-7 · ALTO — Fichero `.msc` recibido por correo o descargado de internet**

```
( email.attachment.extension == "msc"
  OR email.attachment.nested.extension == "msc" )
OR ( file.extension == "msc" AND file.origin == "internet" )
```

→ Cuarentena. **La recomendación de fondo es bloquear la extensión en la pasarela**, igual que `.desktop` en `CTI-2026-026`: una organización no tiene ninguna razón legítima para recibir ficheros de consola de administración por correo.

**D-8 · MEDIO — Instalación de software en las 24 horas siguientes a una conexión a red no corporativa**

```
// Correlación temporal sobre dos fuentes.
EVENTO_A: conexión a SSID no corporativo, o sesión de red sin túnel establecido
EVENTO_B: instalación de software, o ejecución de un binario descargado,
          en el mismo equipo dentro de las 24 h siguientes
ALERTA SI A seguido de B
```

→ Investigación en el día. **Su propósito principal es verificar el cumplimiento de la política de `E-c`**, no cazar un compromiso. Los falsos positivos de esta regla son el entregable.

**D-9 · MEDIO — Certificados señalados como no confiables presentes en el almacén**

```
certificate.subject.organization CONTAINS_ANY ( <firmantes señalados públicamente> )
AND certificate.store IN ( "Trusted Publishers", "Trusted Root", "Intermediate CA" )
```

→ Retirada inmediata del almacén. Es una comprobación de higiene de una hora, no una detección continua, y responde a `X-10`.

> ⚠ **Regla de operación, y es distinta de la de los dos informes anteriores.**
> En `CTI-2026-025` y `CTI-2026-026` la advertencia era sobre listas de excepción
> y sobre brechas de visibilidad. Aquí es más de fondo: **`D-1` y `D-2` no deben
> desplegarse como detecciones permanentes, sino usarse una vez para producir un
> inventario y después sustituirse por una política de bloqueo.** Detectar
> continuamente la carga de controladores firmados con certificados caducados es
> aceptar que siguen cargándose. El objetivo es `E-a`, y estas reglas son el
> camino, no el destino.
>
> Y una advertencia sobre `D-4`: es la única regla de este informe con validez
> frente a un equipo comprometido en el núcleo, **y es también la única que no se
> puede comprar.** Requiere que exista telemetría de red independiente y que
> alguien construya el contraste. Si sólo se implanta una cosa de este §X-3 y el
> parque ya tiene la lista de bloqueo de controladores, que sea ésta.

## X-4. Consultas de caza

```kql
// H-1 · Controladores de nucleo firmados con certificado caducado.
// La consulta central del informe. Produce un inventario de exposicion, no de compromiso.
DeviceEvents
| where ActionType in ("DriverLoad", "KernelDriverLoad")
| extend Firmante = tostring(parse_json(AdditionalFields).SignerName),
         FinValidez = todatetime(parse_json(AdditionalFields).NotAfter)
| where isnotempty(FinValidez)
| where FinValidez < datetime(2016-01-01)
| summarize Equipos = dcount(DeviceName), Visto = max(Timestamp),
            Muestra = make_set(DeviceName, 10)
          by FileName, Firmante, FinValidez
| order by Equipos desc
```

```kql
// H-2 · Creacion de servicios de tipo controlador de nucleo fuera de ventana de cambio.
DeviceRegistryEvents
| where ActionType in ("RegistryValueSet", "RegistryKeyCreated")
| where RegistryKey matches regex @"(?i)\\SYSTEM\\CurrentControlSet\\Services\\[^\\]+$"
     or RegistryKey matches regex @"(?i)\\SYSTEM\\CurrentControlSet\\Services\\[^\\]+\\Type$"
| where RegistryValueName =~ "Type" and RegistryValueData == "1"
| join kind=leftouter (
    DeviceProcessEvents
    | project DeviceName, Timestamp, InitiatingProcessFileName, ProcessCommandLine
  ) on DeviceName
| project Timestamp, DeviceName, RegistryKey, RegistryValueData,
          InitiatingProcessFileName, ProcessCommandLine
| order by Timestamp desc
```

```kql
// H-3 · msagent.sys con ruta, firmante o fecha discordantes.
// El criterio es la discordancia: existe un componente legitimo de nombre similar.
DeviceFileEvents
| where FileName =~ "msagent.sys"
| extend Firmante = tostring(parse_json(AdditionalFields).SignerName)
| where FolderPath !startswith @"C:\Windows\System32\drivers"
     or Firmante !has "Microsoft"
| project Timestamp, DeviceName, ActionType, FileName, FolderPath, Firmante,
          SHA256, InitiatingProcessFileName, InitiatingProcessCommandLine
| order by Timestamp desc
```

```kql
// H-6 · Carga lateral de DLL: ejecutable firmado cargando modulo discordante del mismo directorio.
// La regla de mayor reutilizacion entre los informes de esta cartera.
DeviceImageLoadEvents
| where FolderPath matches regex @"(?i)\\(Users|AppData|Temp|ProgramData|Windows\\Temp)\\"
| extend DirDll = strcat_array(array_slice(split(FolderPath, "\\"), 0, -1), "\\")
| extend DirExe = strcat_array(array_slice(split(InitiatingProcessFolderPath, "\\"), 0, -1), "\\")
| where DirDll =~ DirExe
| where InitiatingProcessVersionInfoCompanyName != "" 
| extend FirmanteDll = tostring(parse_json(AdditionalFields).SignerName)
| where isempty(FirmanteDll)
     or FirmanteDll != InitiatingProcessVersionInfoCompanyName
| project Timestamp, DeviceName, InitiatingProcessFileName,
          InitiatingProcessVersionInfoCompanyName, FileName, FolderPath, FirmanteDll, SHA256
| order by Timestamp desc
```

```kql
// H-4 · Contraste entre la vista de red del endpoint y la de la infraestructura.
// Esqueleto. Requiere una tabla de flujos de red externa al endpoint (NetFlow, proxy, DNS).
let ventana = 1h;
let desde = ago(7d);
let VistaEndpoint =
    DeviceNetworkEvents
    | where Timestamp > desde and RemoteIPType == "Public"
    | summarize DestinosEndpoint = make_set(RemoteIP, 500)
              by DeviceName, Bucket = bin(Timestamp, ventana);
let VistaRed =
    externaldata(ts: datetime, src_ip: string, dst_ip: string)
      [@"<ruta a los flujos de red: NetFlow, proxy o DNS>"]
    | where ts > desde
    | summarize DestinosRed = make_set(dst_ip, 500)
              by src_ip, Bucket = bin(ts, ventana);
VistaRed
| join kind=inner ( DeviceNetworkEvents
                    | distinct DeviceName, LocalIP ) on $left.src_ip == $right.LocalIP
| join kind=leftouter VistaEndpoint on DeviceName, Bucket
| extend SoloEnRed = set_difference(DestinosRed, coalesce(DestinosEndpoint, dynamic([])))
| where array_length(SoloEnRed) > 0
| project Bucket, DeviceName, src_ip, SoloEnRed
| order by Bucket desc
```

```yaml
# Sigma — Controlador de nucleo firmado con certificado caducado
# Autor: Célula CTI · Fecha: 2026-11-17 · ATT&CK: T1014, T1553.002, T1543.003
# Nivel: critical · Estado: estable
# No detecta a Mustang Panda: detecta la clase entera de abuso. Valor independiente del actor.
title: Carga de controlador de nucleo firmado con certificado caducado
id: 5b2e8c47-1fa9-4d63-90e7-8c3b14f7a2d0
status: stable
description: >
  Mustang Panda firma su rootkit msagent.sys con un certificado valido entre
  agosto de 2013 y septiembre de 2014. La aplicacion de firma de controladores
  de Windows acepta controladores firmados antes de su fecha de corte, por
  compatibilidad con hardware antiguo. Cualquier controlador antiguo firmado es
  por tanto una puerta al nucleo, para este actor o para cualquier otro.
references:
  - https://securityaffairs.com/197274/apt/mustang-panda-upgrades-coolclient-with-a-kernel-rootkit.html
logsource:
  category: driver_load
  product: windows
detection:
  seleccion:
    Signed: 'true'
  caducado:
    SignatureNotAfter|lt: '2016-01-01'
  condition: seleccion and caducado
falsepositives:
  - Controladores de hardware antiguo en servidores y equipos heredados,
    impresoras y equipamiento industrial. CADA UNO ES UN HALLAZGO DE RIESGO,
    no un falso positivo: inventariarlos es el objetivo de la regla.
level: critical
```

```yaml
# Sigma — Instalacion de un servicio de tipo controlador de nucleo
# Autor: Célula CTI · Fecha: 2026-11-17 · ATT&CK: T1543.003, T1014
# Nivel: high · Estado: estable
title: Servicio de Windows de tipo controlador de nucleo instalado
id: a4d91f06-8b57-42ce-b1d3-7e62c0a95f84
status: stable
description: >
  El rootkit msagent.sys se instala como servicio de Windows de tipo controlador
  de nucleo. En un parque gestionado la instalacion de un controlador de nucleo
  es infrecuente y atribuible a un cambio autorizado.
logsource:
  product: windows
  service: system
detection:
  seleccion:
    EventID: 7045
    ServiceType: 'kernel mode driver'
  condition: seleccion
falsepositives:
  - Instaladores de software legitimo, actualizaciones de hardware y agentes de
    seguridad. Todos identificables por el proceso padre y por el ticket de cambio.
level: high
```

```yaml
# Sigma — msagent.sys con ruta o firmante discordantes
# Autor: Célula CTI · Fecha: 2026-11-17 · ATT&CK: T1036.005, T1014
# Nivel: critical · Estado: estable
# El criterio es la DISCORDANCIA: existe un componente legitimo de nombre similar.
title: msagent.sys fuera de System32 o sin firma de Microsoft
id: f17b3e58-6c04-4a92-85df-2b9a7c41e063
status: stable
description: >
  Mustang Panda nombra su controlador de rootkit imitando un componente legitimo
  de Windows. Buscar el nombre produce falsos positivos; el criterio valido es la
  ruta fuera de System32\drivers, un firmante que no sea Microsoft, o una fecha
  de validez de certificado anterior a 2015.
logsource:
  category: file_event
  product: windows
detection:
  seleccion:
    TargetFilename|endswith: '\msagent.sys'
  filtro_legitimo:
    TargetFilename|startswith: 'C:\Windows\System32\drivers\'
  condition: seleccion and not filtro_legitimo
falsepositives:
  - Copias de respaldo o de recuperacion del componente legitimo. Verificar firmante.
level: critical
```

```yaml
# Sigma — Unidad extraible con un unico ejecutable visible y directorios ocultos
# Autor: Célula CTI · Fecha: 2026-11-17 · ATT&CK: T1091, T1564.001
# Nivel: high · Estado: experimental
title: Patron de presentacion de gusano en medio extraible
id: 3c6a0d92-7e14-48b5-a0f7-9d51b8e23c47
status: experimental
description: >
  HIUPAN oculta sus componentes en un directorio escondido de la unidad y deja
  visible un unico ejecutable de aspecto legitimo (USBConfig.exe), para que el
  usuario vea algo plausible. El patron de presentacion no depende del nombre.
logsource:
  category: file_event
  product: windows
detection:
  seleccion_nombre:
    TargetFilename|endswith: '\USBConfig.exe'
  seleccion_oculto:
    TargetFilename|re: '(?i)^[D-Z]:\\\..*'
    FileAttributes|contains: 'HIDDEN'
  condition: seleccion_nombre or seleccion_oculto
falsepositives:
  - Unidades de instalacion de software y llaves de arranque. Pocas y enumerables.
level: high
```

## X-5. Mitigaciones de configuración con efecto directo

| Control | Corta |
|---|---|
| **Activar la lista de bloqueo de controladores vulnerables de Microsoft** en todo el parque | La carga del rootkit y la de cualquier otro controlador antiguo conocido. **Es la mitigación de mayor efecto del informe** y la decisión `E-a` |
| **Política de integridad de código (WDAC) que exija certificado vigente** en controladores, rechazando firmas anteriores a la fecha de corte, donde la compatibilidad lo permita | La clase entera de abuso de `KJ-5`, no sólo este controlador. Requiere inventario previo (`H-1`) para no romper hardware heredado |
| **Arranque seguro y, donde sea viable, integridad de código protegida por hipervisor** | Eleva sustancialmente el coste de cargar código no autorizado en el núcleo |
| **Restringir la instalación de controladores a cuentas administrativas y a ventanas de cambio**, con auditoría de EID 7045 | La etapa 04 de la cadena común: si el controlador no se puede instalar, el resto del rootkit no importa |
| **Túnel obligatorio antes de cualquier navegación** en redes no corporativas, con cliente que lo imponga y no lo sugiera | **El vector del portal cautivo completo.** Si el túnel se establece antes de la primera petición del navegador, la red ajena no puede presentar su página |
| **Prohibición expresa de instalar software ofrecido tras conectarse a una red ajena**, por circular y por recordatorio en el cliente de VPN | La etapa 03 del vector B. Es la decisión `E-c` y cuesta una circular |
| **Retirar del almacén de confianza los certificados de firma de código señalados públicamente** como no confiables | La firma del descargador del vector B. Comprobación de una hora (`H-9`, `X-10`) |
| **Bloquear la extensión `.msc` en la pasarela de correo**, con inspección recursiva dentro de archivadores | El vector C de 2026. **Mismo control pendiente que `.desktop` en `CTI-2026-026`: dos informes, una sola tarea de pasarela** |
| **Bloquear la ejecución desde medios extraíbles** (AppLocker o WDAC) | Los tres gusanos. **Tercer informe consecutivo que pide este control**: `CTI-2026-025` por dos herramientas, `CTI-2026-026` por ninguna, éste por tres |
| **Inspección de archivadores en la pasarela con bloqueo de `LNK` y `.msc` en cualquier nivel de anidamiento** | La entrega del vector C |
| **Telemetría de red independiente del endpoint** (NetFlow, registros de proxy y DNS centralizados) y contraste periódico | No corta nada, pero es **la única forma de ver a un adversario que controla lo que el equipo informa**. Decisión `E-b` y regla `D-4` |
| **Pregunta por escrito al proveedor de EDR**: ¿de dónde obtiene su visibilidad de red? | No es una mitigación sino la resolución del supuesto clave de §O-6. Cuesta un correo (`X-5`) |

---

## 14. Brechas de inteligencia y nuevos requisitos de colección

| # | Brecha | Impacto en el juicio | Requisito propuesto | Prioridad |
|---|---|---|---|---|
| G-1 | **Sin inventario de controladores de terceros con fecha de certificado** | Deja sin dimensionar la decisión `E-a`, que es la principal del informe. **No es una brecha de inteligencia: es una tarea de inventario pendiente** | Ejecutar `H-1` y producir la lista de exposición | **Crítica** |
| G-2 | **El informe primario sobre el rootkit no se leyó íntegro, y ninguna cobertura nombra al titular del certificado** | `KJ-4` y `KJ-5` se sostienen en coberturas coincidentes. **Y sin el titular del certificado no se puede comprobar si existe lista de revocación aplicable**, que es lo que haría dirigida la decisión `E-a` | Obtener el análisis original del laboratorio. Indicador `I-2` | **Crítica** |
| G-3 | **Los documentos judiciales no se leyeron en original, y las fuentes secundarias discrepan sobre su alcance** | `KJ-7` —la atribución más fuerte del lote— se recoge en versión conservadora. Afecta a cumplimiento y a cadena de suministro, no a detección | Obtener los escritos del procedimiento del Distrito Este de Pensilvania, que son de acceso público | Alta |
| G-4 | **Sin respuesta del proveedor de EDR sobre su fuente de visibilidad de red** | Es el supuesto clave de §O-6. Si el EDR tiene sensor propio, la gravedad de `KJ-4` baja; si no, es máxima | Pregunta formal por escrito. Es `X-5` y cuesta un correo | Alta |
| G-5 | **Ausencia de telemetría regional publicada sobre este actor** | Es `KJ-8` y la cuestión 3 de §O-6: no se puede distinguir entre falta de actividad y falta de observación. **Es la brecha que determina si este informe describe un método o una amenaza** | **Requisito de colección permanente**: vigilar informes de proveedores con telemetría latinoamericana. Indicadores `I-1` e `I-7` | **Crítica** |
| G-6 | Informe original de la campaña de junio de 2026 contra India y sus tres familias nuevas | Los nombres y la victimología provienen de un agregador que cita a los investigadores originales. `KJ-9` queda en confianza moderada | Localizar el informe original de los investigadores citados | Media |
| G-7 | No se pudo leer la metodología del ranking de telemetría (HTTP 403) | Tercera vez en este lote. Afecta a la comparabilidad de las cifras de `KJ-1` entre los tres informes | Obtener el informe completo por vía comercial o institucional | Alta |
| G-8 | **Relación entre el desmantelamiento de 2025 y la escalada al kernel de finales de 2025** | Las hipótesis H5 y H6 de §O-6 no se pueden distinguir. Afecta al pronóstico sobre el efecto de una futura acción policial | Buscar análisis que daten el inicio del desarrollo del componente de núcleo | Media |
| G-9 | Alcance real del clúster `Camaro Dragon` y de los implantes en enrutadores | La salvedad de equivalencia parcial de §O-1 queda sin resolver. **Riesgo de contaminar el expediente con actividad de otro operador** | Localizar el informe original que acuñó la designación y determinar su solapamiento | Media |
| G-10 | Relación con `CL-STA-1048` y `CL-STA-1049`, que operan en paralelo contra los mismos objetivos | Fuera de alcance de este producto, pero es el tipo de información que explicaría la distribución geográfica de la recolección china y, con ella, `KJ-8` | Producto separado, o requisito para el próximo informe china-nexus de la cartera | Media |

---

# ANEXOS

## Anexo A — Indicadores de compromiso

> ⚠ **Leer antes de usar.** Este expediente es el inverso del de
> `CTI-2026-026`: **rico en análisis y pobre en indicadores publicados.** Las
> fuentes de mayor valor —el análisis del rootkit y la investigación del portal
> cautivo— describen mecanismos con detalle y publican pocos valores concretos.
>
> **Por eso el Anexo A de este informe es corto y el §X-3 es largo**, y eso es
> lo correcto: contra un actor con un componente de núcleo que filtra lo que el
> sistema informa, una lista de indicadores es el peor instrumento posible,
> porque **el adversario controla la respuesta a la pregunta que el indicador
> hace**. Lo utilizable de este anexo es la sección A.2: nombres de artefacto,
> rangos de certificado y patrones de conducta.
>
> El valor más alto de todo el anexo es **una sola fila**: el rango de validez
> del certificado que firma el rootkit. No es un indicador de este actor; es la
> descripción de una clase de exposición.

### A.1 — Artefactos del componente de núcleo y de la firma de código

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| filename | `msagent.sys` | **Controlador del rootkit de `CoolClient`**, instalado como servicio de Windows de tipo controlador de núcleo. **Imita el nombre de un componente legítimo de Windows: el criterio de detección es la discordancia de ruta, firmante o fecha, no el nombre** | Alta | Sin caducidad | Caza con contraste (`D-3`, `H-3`) — **no bloquear por nombre** |
| pattern | `certificado de firma de controlador con validez 2013-08 → 2014-09` | **El artefacto de mayor valor del informe.** Rango de validez del certificado que firma el rootkit: caducado hace doce años y aceptado por la aplicación de firma de controladores de Windows. **El titular del certificado no está publicado en ninguna fuente leída (brecha `G-2`)** | Alta | Sin caducidad | **Detección de clase** (`D-1`) — generalizar a cualquier certificado caducado |
| pattern | `servicio de Windows con Type=1 (controlador de núcleo) creado fuera de ventana de cambio` | Mecanismo de instalación del rootkit. **Patrón conductual, no indicador de actor** | Alta | Sin caducidad | Detección (`D-2`, `H-2`) |
| artefacto | `IOCTL` entre puerta trasera en espacio de usuario y controlador de núcleo | Mecanismo de control de `CoolClient` sobre su rootkit | Alta | Sin caducidad | Caza |
| artefacto | `filtrado de direcciones de C2 de la información de red devuelta al espacio de usuario` | **Capacidad del rootkit con mayor consecuencia defensiva**: lo que el equipo informa sobre sus propias conexiones no es fiable. Obliga a `D-4` | Alta | Sin caducidad | Contraste independiente (`D-4`, `H-4`) |
| herramienta | `STATICPLUGIN` | Descargador **firmado digitalmente** del vector del portal cautivo | Alta | Sin caducidad | Caza |
| herramienta | `CANONSTAGER` | Preparador que carga en memoria la variante cifrada de `PlugX` | Alta | Sin caducidad | Caza |
| herramienta | `SOGU.SEC` | Variante cifrada de `PlugX` cargada directamente en memoria | Alta | Sin caducidad | Caza |
| artefacto | `certificados de firma de código emitidos a una empresa de Chengdu, señalados públicamente como no confiables` | Firma del descargador del vector B. **El proveedor que investigó la campaña pidió públicamente tratarlos como no confiables**: comprobar su presencia en el almacén propio es una tarea de una hora | Alta | Sin caducidad | **Retirada del almacén de confianza** (`D-9`, `H-9`, `X-10`) |

### A.2 — Artefactos de gusano, de carga y de vector

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| filename | `USBConfig.exe` | **Único fichero visible que el gusano `HIUPAN` deja en la unidad extraíble**, junto a uno o más directorios ocultos donde guarda sus componentes | Alta | Sin caducidad | Bloqueo por detección (`D-6`, `H-5`) |
| pattern | `unidad extraíble con un único ejecutable visible en la raíz y uno o más directorios ocultos` | **Patrón de presentación del gusano, independiente del nombre.** Es la forma correcta de buscarlo | Alta | Sin caducidad | Detección (`D-6`) |
| herramienta | `HIUPAN` · `MISTCLOAK` · `U2DiskWatch` | **Tres nombres del mismo gusano** según el proveedor. Entrega `PUBLOAD` por carga lateral de DLL | Alta | Sin caducidad | Caza |
| herramienta | `SnakeDisk` | Segundo gusano de medios extraíbles, documentado en septiembre de 2025 junto a una versión actualizada de `TONESHELL` | Alta | Sin caducidad | Caza |
| herramienta | `Claimloader` | DLL maliciosa de carga lateral que entrega `PUBLOAD`. **Un proveedor la nombra así y otro la pliega dentro de `PUBLOAD`**: la misma cosa con dos nombres | Alta | Sin caducidad | Caza |
| pattern | `ejecutable firmado que carga una DLL del mismo directorio sin firma o de otro fabricante, en ruta de perfil o temporal` | **Patrón de carga lateral de DLL.** Método dominante de este actor y la regla con mayor reutilización entre informes de esta cartera | Alta | Sin caducidad | Detección (`D-5`, `H-6`) |
| artefacto | `.msc` | **Ficheros de consola de administración de Microsoft como vector de entrega**, nuevo en 2026. Misma clase de problema que `.desktop` en `CTI-2026-026`: extensión funcional, legítima y poco vigilada | Alta | Sin caducidad | **Bloqueo de la extensión en la pasarela** (`D-7`, `X-5`) |
| artefacto | `redirección de la comprobación de conectividad del navegador por el portal cautivo de una red wifi` | **Vector B completo.** No se mitiga con un indicador: se mitiga con túnel obligatorio antes de navegar (decisión `E-c`) | Alta | Sin caducidad | Política, no bloqueo |
| artefacto | `página que imita el sitio de actualización de un complemento de Adobe` | Señuelo del vector B | Alta | Sin caducidad | Caza |
| herramienta | `PlugX` · `SOGU` · `DOPLUGS` | Familia histórica del actor. **Es la familia de la que el FBI borró 4 258 infecciones** entre agosto de 2024 y enero de 2025, en buena parte de particulares y organizaciones pequeñas: es de amplia circulación y no dirigida | Alta | Sin caducidad | Retrohunt (`H-10`, `X-12`) |
| herramienta | `TONESHELL` · `ToneShellws` | Puerta trasera principal del actor en 2025. **Cargada en diciembre de 2025 por un primer rootkit de núcleo, distinto del de `CoolClient`** | Alta | Sin caducidad | Caza |
| herramienta | `LOTUSLITE` | Puerta trasera principal del rearme posterior al desmantelamiento. Objetivos: organizaciones de política de Estados Unidos | Alta | Sin caducidad | Caza |
| herramienta | `CoolClient` | Puerta trasera que opera con el rootkit de `A.1`. Víctimas gubernamentales en Myanmar, Mongolia, Pakistán y Rusia | Alta | Sin caducidad | Caza |
| herramienta | `PUBLOAD` · `Pubshell` · `FDMTP` | Puertas traseras y herramientas del linaje del actor | Alta | Sin caducidad | Caza |
| herramienta | `SHARDLOADER` · `MINIRECON` · `ZOHOMURK` | **Tres familias nuevas de junio de 2026**, contra el gobierno y el sector hidroeléctrico de India. Vinculadas al actor por solapamiento de código con `TONESHELL` **y por una falta de ortografía compartida entre los implantes** | Media | Sin caducidad | Caza |
| artefacto | `falta de ortografía compartida entre implantes` | **Artefacto de autoría**, no de compromiso. Indicio legítimo y de uso corriente, **pero plantable**: véase `KJ-9` | Media | Sin caducidad | Análisis, no detección |

### A.3 — Servicios y componentes legítimos implicados · **NO BLOQUEAR**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| servicio | `dirección de comprobación de conectividad del navegador` | El navegador solicita una dirección fija para detectar portales cautivos. **Es el mecanismo que el vector B secuestra, y es imprescindible para que funcione el wifi de cualquier hotel.** No se puede bloquear | Alta | Sin caducidad | **No bloquear.** Mitigación por política de túnel (`E-c`) |
| herramienta | `mmc.exe` | Consola de administración de Microsoft, que ejecuta los ficheros `.msc`. Componente legítimo del sistema | Alta | Sin caducidad | **No bloquear el binario.** Bloquear la extensión en la pasarela |
| herramienta | `carga lateral de DLL` | No es una herramienta sino una técnica sobre software legítimo y firmado. **El indicador es la discordancia de firmante, nunca el ejecutable** | Alta | Sin caducidad | **No bloquear.** Detección por discordancia (`D-5`) |
| servicio | `componente legítimo de Windows de nombre similar a msagent.sys` | Existe, y es la razón por la que `D-3` y `H-3` se construyen sobre la discordancia y no sobre el nombre | Alta | Sin caducidad | **No bloquear por nombre** |

## Anexo B — Fuentes y valoración

| # | Fuente | Disciplina | Fiab. | Cred. | Notas de sesgo |
|---|---|---|---|---|---|
| 1 | Kaspersky GReAT, análisis del rootkit de núcleo de `CoolClient`, 2026-08-14 — **leída por coberturas múltiples, no en original** | OSINT comercial de primera mano, vía secundaria | **B** | **2** | **Fuente de `KJ-4` y `KJ-5`, los hallazgos centrales.** Credibilidad 2 y no 3 porque **cuatro coberturas independientes concuerdan** en el nombre del controlador, su mecanismo, el rango de validez del certificado y los cuatro países víctima. **Ninguna nombra al titular del certificado**: brecha `G-2`. Publica bajo la designación propia del laboratorio (`HoneyMyte`) |
| 2 | Kaspersky, rootkit de núcleo que carga `TONESHELL`, diciembre de 2025 — citada por la fuente 1 | OSINT comercial de primera mano, vía terciaria | **B** | **3** | Establece que la incursión de agosto de 2026 **no es la primera**, que es lo que convierte un hallazgo puntual en una capacidad consolidada |
| 3 | Google GTIG, investigación de `UNC6384` y el secuestro de portales cautivos, agosto de 2025 — leída por coberturas | OSINT comercial de primera mano, vía secundaria | **B** | **2** | Fuente del vector B, de la cadena `STATICPLUGIN` → `CANONSTAGER` → `SOGU.SEC` y del aviso público sobre los certificados de Chengdu. **Vincula el clúster a este actor con el grado de certeza que declara, sin fundirlo.** Nota de interés: hubo una atribución pública errónea a otro actor chino, con corrección posterior (§O-1) |
| 4 | Documentos judiciales del procedimiento del Distrito Este de Pensilvania y comunicación del Departamento de Justicia de EE. UU., enero de 2025 — **leídos por coberturas, no en original** | **OSINT judicial**, vía secundaria | **B** | **3** | **La fuente de mayor peso del lote por su clase**, y la de `KJ-6` y `KJ-7`. Credibilidad 3 porque **las coberturas discrepan sobre su alcance**: una presenta el pago estatal como establecido, otra subraya que no hay imputación nominal y que la acción fue técnica. Se recoge la versión conservadora. Brecha `G-3` |
| 5 | Picus Security, campaña de `LOTUSLITE`, `SnakeDisk` y `ToneShellws`, 2026 | OSINT comercial | **C** | **3** | Fuente del rearme posterior al desmantelamiento y del vector `.msc`. Perfil de proveedor de simulación, con interés comercial en el catálogo de técnicas |
| 6 | Breakglass Intelligence, análisis de 25 muestras de 2024 a 2026 y vector `.msc` | OSINT comercial de primera mano | **B** | **3** | Aporta el linaje de herramientas (`PlugX` → `LOTUSLITE` → `TONESHELL` → `SnakeDisk` → `PUBLOAD` → `FDMTP`). **Es la misma fuente que en `CTI-2026-026` declaraba honestamente qué no había verificado**, lo que sostiene su fiabilidad |
| 7 | Cobertura de la campaña de `HIUPAN` y `Claimloader`, junio–agosto de 2025, citando a Trend Micro e IBM X-Force | OSINT comercial, vía secundaria | **C** | **3** | Fuente de la ventana exacta de la campaña del gusano, del señuelo `USBConfig.exe` y de la discrepancia de nombres entre proveedores (`Claimloader` frente a `PUBLOAD`) |
| 8 | Perfil agregador de la campaña de junio de 2026 contra India, citando a los investigadores originales | OSINT comercial agregado | **C** | **4** | **Única fuente de `SHARDLOADER`, `MINIRECON` y `ZOHOMURK` y del método de atribución por errata compartida.** No es el informe original: brecha `G-6`. `KJ-9` queda en confianza moderada por esto |
| 9 | Trellix, «The CyberThreat Report: November 2026», 2026-11-04 | OSINT comercial de telemetría agregada | **B** | **3** | Origen de `KJ-1`. **Tercera vez en este lote con la misma limitación**: HTTP 403, metodología no leída. Brecha `G-7` |
| 10 | MITRE ATT&CK, ficha de grupo `G0129` | OSINT de marco | **B** | **2** | Base de la tabla de alias y del año de inicio |
| 11 | Referencia cruzada de nombres entre proveedores (*crosswalk*) | OSINT de referencia | **C** | **3** | **Aporta la salvedad más valiosa del expediente de alias**: que `Camaro Dragon` es coincidencia **parcial** por corresponder a un clúster solapado de implantes en enrutadores. Es el tipo de matiz que ningún perfil de actor recoge y que evita contaminar el expediente (brecha `G-9`) |
| 12 | ESET, «ESET APT Activity Report Q2 2026–Q3 2026», 2026-10-28 | OSINT comercial de primera mano | **B** | **2** | Se consigna **por lo que no dice**: cubriendo exactamente la misma ventana que el ranking de Trellix, no nombra a este actor entre los clústeres china-nexus que destaca, y sí a otros dos. Es un dato de contraste de visibilidad entre proveedores, no una contradicción |
| 13 | Coberturas sobre `CoolClient` de baja fiabilidad (agregadores y sitios de noticias automatizados) | Prensa automatizada | **D** | **4** | **Usadas sólo como corroboración de datos que ya aparecían en la fuente 1.** Ningún dato que apareciera únicamente en ellas se ha recogido en este informe |

**Escalas**
- **A** completamente fiable · **B** normalmente fiable · **C** bastante fiable · **D** normalmente no fiable · **E** no fiable · **F** no evaluable.
- **1** confirmada por otras fuentes · **2** probablemente cierta · **3** posiblemente cierta · **4** dudosa · **5** improbable · **6** no evaluable.

> **Observación sobre este anexo.** Es el mejor expediente de los tres de este
> lote, y conviene decir por qué con precisión: **no por tener más fuentes**
> —`CTI-2026-026` tenía doce— **sino porque sus fuentes se corroboran y una de
> ellas es judicial.** Cuatro coberturas independientes concuerdan en los
> detalles técnicos del rootkit; dos laboratorios distintos documentan dos
> incursiones en el núcleo; un procedimiento judicial aporta la atribución. La
> lección, enunciada en el Anexo B de `CTI-2026-026` y confirmada aquí: **la
> calidad de un expediente no se mide en número de fuentes, sino en grado de
> corroboración entre ellas.**
>
> La debilidad estructural, en cambio, es de **vía de acceso**: las dos fuentes
> más importantes del informe —el análisis del rootkit y los documentos
> judiciales— se leyeron por coberturas y no en original. Es lo que impide que
> `KJ-4`, `KJ-5` y `KJ-7` tengan confianza alta sin matices, y está recogido en
> `G-2` y `G-3`.

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

## Anexo D — Qué se puede y qué no se puede concluir de un desmantelamiento judicial

Este anexo es el entregable transversal del informe, y existe porque los desmantelamientos se comunican a Dirección como resoluciones y rara vez lo son. Son las cinco preguntas que hay que hacer a la noticia de una acción policial contra un actor que nos preocupa.

| # | Pregunta | Por qué | Respuesta en este caso |
|---|---|---|---|
| D-1 | **¿Qué se desmanteló: la capacidad del actor o su base instalada?** | Borrar malware de equipos de terceros limpia infecciones; no toca el desarrollo, los operadores ni las operaciones dirigidas | **La base instalada.** 4 258 equipos limpiados, en buena parte de particulares y organizaciones pequeñas que no eran objetivo |
| D-2 | **¿Hubo imputación de personas, o sólo acción técnica?** | Una imputación impone coste personal a los operadores; una acción técnica impone coste de reconstrucción, que es mucho menor | **Sólo acción técnica.** Ninguna persona acusada, ningún servicio designado |
| D-3 | **¿Qué hizo el actor en los doce meses siguientes?** | Es la única medida real del efecto, y casi nunca se publica junto a la noticia del desmantelamiento | **Se rearmó**: familias nuevas en el mismo año y, once meses después, su primera incursión en el núcleo de Windows |
| D-4 | **¿Afectó a la infraestructura de mando o sólo a los clientes?** | Si el actor conserva su infraestructura y su cadena de desarrollo, la reconstrucción es cuestión de semanas | **Sólo a los clientes**, por lo que las fuentes describen |
| D-5 | **¿Se comunicó internamente como resolución del riesgo?** | Es el error de gestión que este anexo quiere evitar. Un desmantelamiento es una **reducción temporal de volumen**, no una eliminación de amenaza | Pendiente de verificar en nuestra propia comunicación interna. **Es la decisión `E-h`** |

> **Qué hacer con esto.** Cuando llegue la noticia del próximo
> desmantelamiento, y llegará, estas cinco preguntas se responden en media hora
> y producen una nota de una página que evita que Dirección cierre un riesgo que
> sigue abierto. En este expediente, las cinco respuestas apuntan en la misma
> dirección: **la acción policial de enero de 2025 compró tiempo y no compró
> seguridad.**

## Anexo E — Marcos de referencia empleados

`MITRE ATT&CK v19` · `Modelo del Diamante` · `Cyber Kill Chain` · `Pirámide del Dolor` (con la salvedad de §T-3 sobre su validez frente a componentes de núcleo) · `F3EAD` · `ICD 203` · `Análisis de Hipótesis Competidoras (ACH)` · `Comprobación de Supuestos Clave (KAC)` · `pre-mortem` · `TLP 2.0` · `PAP` · `Admiralty Code` · `Sigma` · `KQL` · `Windows Driver Signature Enforcement` y `WDAC` como marcos de control de plataforma

## Anexo F — Paquete legible por máquina

- Índice con contexto: [`ioc_index.csv`](ioc_index.csv) — el fichero que debe ingerir una plataforma de inteligencia
- Listas planas: [`ioc_hash.txt`](ioc_hash.txt), [`ioc_url.txt`](ioc_url.txt), [`ioc_ipv4.txt`](ioc_ipv4.txt) — **este informe aporta muy poco a ellas por diseño**: su contenido utilizable son artefactos, patrones y propiedades de certificado, que no son direcciones ni hashes
- Reglas Sigma: cuatro reglas en §X-4, más el esqueleto de la consulta de contraste endpoint/red (`D-4`), que es la pieza que requiere trabajo propio
- Bundle STIX 2.1: no generado
- Evento MISP: no generado

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| **1.1** | **2026-11-21** | **Alineamiento con MITRE ATT&CK v20.1.** ATT&CK reorganizó la matriz y este informe citaba identificadores que la fuente ha **revocado**: `T1562.001`, `T1574.002` → `T1574.001`, `T1685`. Son referencias que un `Tnnnn` bien formado no delata y que se copian de informes viejos. **No se extiende `caduca`: se ha puesto al día la nomenclatura de los TTP, no revalidado ningún juicio.** Lo comprueba en adelante la familia `G7` de `tools/cti_gate.py` contra el catálogo oficial | Célula CTI |
| 1.0 | 2026-11-17 | Emisión inicial. Perfil de capacidad construido sobre ocho fuentes, una de ellas judicial. **Corrige parcialmente la conclusión de `CTI-2026-025` y `CTI-2026-026` sobre la lectura de los rankings de prevalencia** | Célula CTI |

## Anexo H — Realimentación del consumidor

| Pregunta | Respuesta |
|---|---|
| ¿Respondió a su requisito? | |
| ¿Cuántos controladores de núcleo firmados con certificado caducado resultó haber en el parque? (hipótesis `H-1`, decisión `E-a`) | |
| ¿Se activó la lista de bloqueo de controladores vulnerables? ¿Rompió algo? | |
| ¿Qué respondió el proveedor de EDR sobre su fuente de visibilidad de red? (pregunta `X-5`) | |
| ¿Se emitió la corrección de la instrucción de priorización? (decisión `E-f`) | |
| ¿Estaban en el almacén de confianza los certificados señalados públicamente? (hipótesis `H-9`) | |
| ¿Qué faltó? | |
| ¿Llegó a tiempo? | |

> Sin este anexo devuelto, el ciclo de inteligencia queda abierto. En este
> informe interesan especialmente la segunda y la quinta pregunta: la segunda
> porque es el único hallazgo de exposición real que el informe puede producir,
> y la quinta porque corrige un mensaje que este lote transmitió mal.
