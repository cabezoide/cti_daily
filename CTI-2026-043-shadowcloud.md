---
tlp: "TLP:CLEAR"
pap: "PAP:AMBER"
id: "CTI-2026-043"
version: "1.0"
tipo: "Perfil de operación sin atribuir"
foco_regional: "Latinoamérica"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "Operation ShadowCloud · BRONZE SANDCASTLE · GitDoor · GraphDoor"
fecha: "2026-11-17"
caduca: "2027-02-17"
autor: "Célula CTI"
distribucion: "Elaborado íntegramente con fuentes abiertas TLP:CLEAR. Las dos partes del análisis de Kaspersky GReAT publicadas el 17 de noviembre de 2026 se leyeron en original, con sus tablas y sus anexos de indicadores completos. El informe de Sophos CTU del 20 de octubre de 2026 se leyó en original. Las verificaciones de registro y resolución de dominios del Anexo A.5 son propias, ejecutadas el 2026-11-17, y se declaran como tales. Difusión libre, conservando la atribución de las fuentes y las salvedades metodológicas de §3. Se mantiene PAP:AMBER: el Anexo A contiene una dirección IP que casi con certeza es un error tipográfico de la fuente primaria y que apunta a una cooperativa eléctrica rural ajena a este expediente — leer A.4 antes de cargar nada en bloqueo."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-043

## Dos proveedores describieron la misma operación con dos nombres, y ninguno vio que comparten una cuenta de GitHub

### Sophos la llamó `BRONZE SANDCASTLE` y Kaspersky `Operation ShadowCloud`, con diez semanas de diferencia

> **Regla de oro del producto:** todo párrafo debe responder a un requisito de
> inteligencia (PIR) y habilitar una decisión. Si un párrafo no cambia lo que
> alguien va a hacer, va al anexo o se borra.

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-043` |
| Versión / fecha | `1.0` — 2026-11-17 (emisión inicial) |
| Tipo de producto | Perfil de **operación de espionaje sin atribuir**, más **reconciliación de dos expedientes de proveedor** que describen el mismo objeto con nombres distintos y sin citarse entre sí, más evaluación de **la nube corporativa legítima como canal de mando y control**, más análisis de la cadena de carga y del repertorio de módulos |
| Niveles cubiertos | Estratégico · Operacional · Táctico · Técnico |
| Foco regional | **No hay foco regional, y es un dato, no una omisión.** Las dos fuentes, sumadas, sitúan víctimas en Filipinas, Taiwán, Afganistán, Namibia y probablemente Corea del Sur, más «Asia y África, principalmente gobierno». **Ni una sola víctima en América**. Este informe se emite por el método y por su efecto sobre `CTI-2026-017`, no por exposición propia — y `O-4` explica por qué eso no lo hace irrelevante |
| Marcado de difusión | `TLP:CLEAR` · `PAP:AMBER` |
| Clasificación interna | Sin clasificar. Material íntegramente de publicación abierta |
| Requisitos atendidos | `PIR-01`, `PIR-03`, `PIR-05` (canales de mando y control que atraviesan nuestros controles de salida), `PIR-07` (identidad y aplicaciones en la nube), `RFI-2026-11-B` |
| Solicitante / consumidor primario | Jefatura de SOC e Ingeniería de Detección. **Y, de forma inusual para un informe de actor, la administración de Microsoft 365 y de identidad**: tres de las cinco mitigaciones de `X-5` no se aplican en el endpoint ni en el cortafuegos, sino en la configuración de acceso entre inquilinos |
| Ventana de observación | **2024-09-03 → 2026-11-17.** La fecha inicial no es la de descubrimiento de ninguna de las dos fuentes: es la creación de la primera cuenta de GitHub del conjunto, que es el dato que fija el comienzo real de la preparación |
| Base de colección | Seis fuentes externas; **tres primarias leídas en original** —las dos partes de Kaspersky y el informe de Sophos—, más verificación propia de registro y resolución de dominios. Sin telemetría propia |
| Autor (analista) | Célula CTI |
| Revisión por pares | Pendiente |
| Aprobación | Pendiente |
| Caducidad / revisión | 2027-02-17 (92 días). **Revisión anticipada obligatoria si:** cualquiera de los dos proveedores reconoce públicamente la equivalencia que sostiene `KJ-2` (confirmaría o refutaría el juicio central); se publica el identificador de la aplicación de Entra ID que Kaspersky redactó; aparece una víctima americana; o se atribuye la operación a un actor con nombre |
| Productos relacionados | **`CTI-2026-017` (FamousSparrow) — no complementa: tensiona.** Su titular sostiene que el actor concentra el 90 % de su esfuerzo en Latinoamérica, y esta operación lo sitúa dentro de víctimas asiáticas y africanas en marzo de 2026. Véase `O-2.3` · **`CTI-2026-027` (Mustang Panda / BRONZE PRESIDENT)**, con quien Sophos declara solapamiento de objetivos sin poder vincularlo · `CTI-2026-033` (StrikeShark): **el otro clúster sin atribuir de esta cartera, y el molde metodológico de este informe** · `CTI-2026-034` (Flax Typhoon): el eje taiwanés · `CTI-2026-035` (Medusa): el precedente de administración remota legítima como vector · `CTI-2026-018` (abuso de TLD): `ekmt[.]tw` y `twnic[.]top` son material de ese expediente |
| Paquete legible por máquina | Las tablas `cti:ioc` del Anexo A alimentan `ioc_index.csv`. **Advertencia de higiene:** los servicios legítimos de terceros —GitHub, Microsoft Graph, Ably, `gofile.io`, `file.io`, `ip.sb`, MeshCentral— se consignan con tipo `servicio` precisamente para que **no** entren en los agregados planos `ioc_ipv4.txt` / `ioc_url.txt`. Bloquear `github.com` por este informe sería un corte autoinfligido |

> ⚠ **Tres limitaciones, y la tercera es inusual.** (1) **Sin telemetría
> propia**: `O-4` es un cuestionario, no una medición. (2) **No hay actor**:
> Kaspersky declara expresamente que no puede atribuir, y este informe no
> mejora esa atribución —lo que hace es unir dos descripciones del mismo
> comportamiento—. (3) **El juicio central de este informe, `KJ-2`, es nuestro
> y no está publicado por nadie.** Se apoya en coincidencias verificables entre
> dos documentos públicos, cualquiera puede comprobarlas en veinte minutos, y
> están enumeradas una por una en `O-2.1` para que se comprueben. Pero ninguna
> de las dos fuentes afirma lo que aquí se afirma, y si se demuestra falso, la
> mitad de este documento se cae. Está escrito para ser refutable.

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** Existe una operación de espionaje activa que usa **servicios de nube corporativa legítimos como canal completo de mando y control** —repositorios de GitHub, bibliotecas de documentos de SharePoint a través de la API de Microsoft Graph, y el servicio de mensajería en tiempo real Ably— con dos puertas traseras modulares no documentadas previamente, `GitDoor` y `GraphDoor`, que descargan módulos a demanda y ejecutan código en memoria sin tocar el disco. Valoramos **casi con certeza** *(≥99 %)* que la operación exista y sea un conjunto coherente de actividad. **Confianza: alta.** *Base:* fuente primaria `B-1` y `B-2`, dos entregas de análisis de código con protocolo de mando y control reconstruido petición a petición, anexos de indicadores completos y 22 direcciones de proxy publicadas; corroborada de forma independiente por `B-3`, que analizó versiones adyacentes del mismo implante sin saberlo.

**KJ-2.** **`Operation ShadowCloud` (Kaspersky, 17-11-2026) y `BRONZE SANDCASTLE` (Sophos, 20-10-2026) son la misma operación.** No es un solapamiento parcial ni un suministrador compartido: los dos informes citan **la misma cuenta de GitHub** (`LatonyCharnleyaW`), los mismos nombres de fichero con el mismo esquema (`main.<ocho caracteres>.js.map`), tres de los mismos pares de carga lateral de DLL, el mismo fichero de carga cifrada (`config.ini`), el mismo servicio de mensajería (Ably) y el mismo servicio de subida (`gofile.io`); y las versiones de implante se intercalan sin huecos —Sophos analiza `1.1.5` y `1.1.7`, `GitDoor` declara `1.1.6` y `GraphDoor` `1.2.7`—. Valoramos **muy probable** *(80–95 %)* que se trate de la misma operación, y **probable** *(55–80 %)* que además sea la misma familia de código en desarrollo continuo y no dos herramientas de un arsenal compartido. **Confianza: moderada.** *Base:* trece coincidencias independientes enumeradas en `O-2.1`, clasificadas por su peso probatorio, todas verificables en los dos documentos públicos. **Ninguna de las dos fuentes afirma esto**: Kaspersky dice únicamente que Sophos «tocó un fragmento» de la campaña y que hay «cierto grado de solapamiento».

**KJ-3.** **La consecuencia de `KJ-2` es el dato más útil de este informe para quien tenga que decidir algo.** Si es la misma operación, el conjunto de víctimas conocido no es «Asia y África, sector gobierno» sino la unión de los dos: **Filipinas, Taiwán, Afganistán, Namibia y probablemente Corea del Sur**, más gobiernos asiáticos y africanos sin nombrar; la ventana de actividad no empieza a «principios de 2026» sino en **agosto de 2025** como observación y **septiembre de 2024** como preparación de infraestructura; y la operación lleva **al menos quince meses** con desarrollo activo, no diez. Valoramos **probable** *(55–80 %)* que el conjunto real de víctimas siga siendo mayor que esa unión. **Confianza: moderada.** *Base:* las dos fuentes declaran por separado que su visibilidad es parcial, y la unión de dos telemetrías parciales sigue siendo parcial.

**KJ-4.** **El indicador más accionable del expediente no figura en ninguna lista de indicadores.** `GraphDoor` se autentica como *aplicación* —no como usuario— contra un inquilino de Entra ID controlado por el adversario, y Kaspersky redactó el identificador de cliente y el secreto pero **dejó el GUID del inquilino visible en la ruta de la petición de token**: `8f50c589-a4d6-4df4-95bb-2fb7f5983fe5`. No aparece en su sección de indicadores de compromiso, ni en la cobertura secundaria, ni —hasta donde hemos podido comprobar— en ningún otro documento público. Valoramos **casi con certeza** *(≥99 %)* que cualquier petición de token contra ese inquilino originada en una red corporativa sea maligna. **Confianza: alta.** *Base:* el flujo `client_credentials` contra un inquilino de tercero no tiene ningún uso legítimo en un endpoint de usuario; el valor es literal de la fuente primaria `B-2`.

**KJ-5.** **El modelo de sigilo del adversario tiene un punto débil, y no es ni GitHub ni Microsoft Graph.** El argumento de las dos fuentes es correcto: las llamadas a la API de Graph y a la de GitHub son indistinguibles del uso corporativo normal, y por tanto la detección por destino de red no sirve. Pero el tercer servicio, **Ably**, no tiene presencia legítima plausible en el parque de puestos de una administración pública o de una gran empresa: es un servicio para desarrolladores de aplicaciones en tiempo real, y aparece en los dos expedientes como transporte de proxy y como canal de distribución de configuración. Valoramos **probable** *(55–80 %)* que la vigilancia de `ably.io` / `ably.net` desde endpoints de usuario tenga una tasa de falsos positivos manejable en un entorno corporativo típico, y **muy probable** *(80–95 %)* que sea el control de mayor rendimiento por unidad de esfuerzo de todo el expediente. **Confianza: moderada.** *Base:* los dos informes coinciden en el uso de Ably; la valoración del coste de los falsos positivos es nuestra, no está medida y depende del entorno.

**KJ-6.** **La configuración embebida de los dos implantes contiene marcas de un desarrollador de habla china, por una vía que ninguna fuente usa.** El campo que nombra el ejecutable legítimo anfitrión de la carga lateral se llama `dhj_exe`, que son las **iniciales de pinyin de «DLL 劫持»** (*DLL jiéchí*, secuestro de DLL); y el campo `is_need_lock` es un calco sintáctico de «是否需要锁». Valoramos **probable** *(55–80 %)* que esta lectura sea correcta y refuerce —por una vía independiente de las que usan los proveedores— el juicio de que el desarrollo es de habla china. **Confianza: moderada, y es una inferencia propia.** *Base:* los dos campos son literales de la fuente primaria `B-1` y `B-2`; la lectura es nuestra. **No es atribución**: identifica el idioma de quien escribió el código, no el patrocinador, y esta cartera lleva tres informes insistiendo en que eso no es lo mismo.

**KJ-7.** **Kaspersky sitúa implantes de FamousSparrow en marzo de 2026 dentro de víctimas de una campaña cuyo conjunto declarado es Asia y África, y eso tensiona el titular de `CTI-2026-017`.** Nuestro propio informe sostiene que ese actor concentra el 90 % de su esfuerzo en Latinoamérica desde mediados de 2025. La fuente **no dice de qué país es el sistema concreto** donde coexisten el implante de FamousSparrow y `GitDoor`, de modo que no hay contradicción probada. Valoramos **aproximadamente igual de probable** *(40–60 %)* que el sistema en cuestión esté fuera de Latinoamérica, lo que obligaría a matizar ese titular. **Confianza: baja.** *Base:* ausencia de dato geográfico en `B-2` para ese sistema concreto. *Consecuencia:* queda abierto como requisito de colección `I-1`, no como corrección.

**KJ-8.** **El expediente no añade un cuarto caso al eje geoespacial de `CTI-2026-034`.** Se buscó expresamente: aquí no hay plataforma de información geográfica, ni catastral, ni ninguna aplicación comprada por un área funcional. El vector inicial es un **agente de administración remota legítimo (MeshCentral)** cuya vía de instalación la propia fuente declara desconocida, atribuyéndola a la reutilización de una infección anterior. Valoramos **casi con certeza** *(≥99 %)* que este informe no sirva como disparador `I-5` de aquel. **Confianza: alta.** *Base:* lectura completa de las dos entregas primarias. *Lo que sí aporta* es un caso del patrón hermano, que `E-2` desarrolla: la herramienta de administración que nadie inventarió.

---

## 2. Resumen ejecutivo

Un adversario que no conocemos lleva **al menos desde finales de 2024** preparando una operación de espionaje contra administraciones públicas de Asia y África, y la lleva adelante sin infraestructura propia de mando y control en el sentido clásico. No hay un dominio que bloquear ni una dirección IP que meter en una lista. Hay una cuenta de GitHub que recibe órdenes en ficheros con nombre de mapa de código JavaScript, un inquilino de Microsoft 365 ajeno contra el que el implante se autentica como si fuera una aplicación empresarial, y un servicio de mensajería para desarrolladores que transporta el túnel. Los tres son servicios legítimos, de pago, con certificado válido y reputación impecable.

Lo que convierte este expediente en algo más que una curiosidad técnica es un hallazgo de archivo: **otro proveedor ya lo había publicado diez semanas antes, con otro nombre, y ninguno de los dos documentos reconoce al otro**. Sophos describió en octubre un «Meterpreter modificado» del que analizó dos versiones; Kaspersky describió en noviembre dos puertas traseras cuya versión embebida cae exactamente entre esas dos. Los dos informes citan la misma cuenta de GitHub. Reconstruir esa unión —que es la aportación propia de este informe y su `Anexo D`— cambia tres cosas que importan: cuántas víctimas se conocen, desde cuándo, y con qué confianza se puede decir que el desarrollo es continuo y no oportunista.

<!-- cti:cards -->

| Título | Texto | Etiqueta |
|---|---|---|
| El canal es el producto | La innovación no está en las puertas traseras, que son competentes y convencionales. Está en que **todo el canal de mando y control vive en servicios que ya están permitidos**: GitHub para las órdenes, SharePoint para los datos, Ably para el túnel. La detección por destino de red no tiene nada que morder | Modelo |
| Dos nombres, una operación | `BRONZE SANDCASTLE` y `Operation ShadowCloud` comparten cuenta de GitHub, esquema de nombres de fichero, pares de carga lateral, fichero de configuración, servicio de mensajería y servicio de subida. Y las versiones se intercalan: `1.1.5` · **`1.1.6`** · `1.1.7` · **`1.2.7`** | Hallazgo propio |
| El dato que nadie listó | El GUID del inquilino de Entra ID quedó a la vista en la ruta del token mientras el identificador de la aplicación iba redactado. Es una regla de detección de una línea, y no está en ninguna lista de indicadores publicada | Hallazgo propio |
| Ably es el eslabón flojo | GitHub y Graph son indistinguibles del tráfico normal; **Ably no**. No hay razón plausible para que un puesto de trabajo de una administración hable con un servicio de mensajería para desarrolladores. Es el control más barato del expediente | Decisión |
| Una IP que no hay que bloquear | De las 22 direcciones de proxy publicadas, `38.52.17[.]113` pertenece a una **cooperativa eléctrica rural de Estados Unidos** y difiere en un dígito de otra de la misma lista. Casi con certeza es un error tipográfico de la fuente. Léase `A.4` antes de cargar nada | Higiene |
| Y lo que no es | No hay víctimas americanas, no hay día cero, no hay exploit, **y no hay plataforma geoespacial**. El vector inicial es un agente de administración remota legítimo cuya vía de entrada la propia fuente declara desconocida | Alcance |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| 2 | Designaciones de proveedor para la misma operación | `Operation ShadowCloud` (Kaspersky) y `BRONZE SANDCASTLE` (Sophos). Diez semanas de diferencia, ninguna cita a la otra |
| 9 | Cuentas de GitHub del conjunto | Con dirección de correo y fecha de creación publicadas. La más antigua, del **3 de septiembre de 2024** |
| 4 | Versiones de implante conocidas, sin huecos | `1.1.5` y `1.1.7` (Sophos) · `1.1.6` en GitDoor y `1.2.7` en GraphDoor (Kaspersky) |
| 5 | Países con víctima nombrados | Filipinas, Taiwán, Afganistán, Namibia y —como probable— Corea del Sur. **Ninguno americano** |
| 26 | Órdenes que admite GitDoor | En cinco familias: gestión de ficheros, registro de pulsaciones, proxy, proxy sobre Ably y carga de shellcode |
| 30 | Módulos de shellcode propios catalogados | Casi todos binarios COFF. Incluyen Mimikatz, CookieKatz, PetitPotam y un extractor de la clave de la base de datos de WhatsApp |
| 22 | Direcciones de proxy publicadas | De las que **una es casi con certeza un error de transcripción** y otra está en un operador taiwaneso |
| 0 | Días cero | Ni uno. Tampoco un exploit. La entrada es una herramienta de administración remota legítima |

---

## 3. Alcance, requisitos y limitaciones

**3.1 Requisitos de inteligencia atendidos**

| Req. | Enunciado | ¿Respondido? | Dónde |
|---|---|---|---|
| PIR-01 | ¿Qué actores tienen intención y capacidad contra nuestra región? | **No, y la respuesta negativa es el dato.** Capacidad documentada en detalle; intención desconocida porque no hay actor; **y ninguna víctima americana observada** | `KJ-1`, `O-2`, `O-4` |
| PIR-03 | ¿Qué técnicas invalidan nuestros controles? | **Sí, y es el núcleo del informe.** El canal de mando y control atraviesa íntegramente los controles de salida por destino | `KJ-1`, `KJ-5`, `X-3`, `T-3` |
| PIR-05 | ¿Qué canales de mando y control atraviesan nuestro perímetro de salida? | **Sí, con tres servicios nombrados y una jerarquía de tratamiento para cada uno** | `X-3`, `X-5`, `A.4` |
| PIR-07 | ¿Qué exposición tenemos por identidad y aplicaciones en la nube? | **Sí, y es la parte del informe con mitigación más concreta y menos conocida** | `KJ-4`, `X-5.2`, `X-5.3` |
| RFI-2026-11-B | El requisito pedía investigar la operación extensivamente, con dos enlaces de prensa, y traducir fuentes asiáticas si era necesario. ¿Qué sostienen las fuentes? | **Sí.** Véase `3.5`, y en particular el punto 7 sobre las fuentes asiáticas | `3.5` |
| PIR-04 | ¿Nos afecta? | **No.** Requiere telemetría propia | `O-4`, sin evaluar |

**3.2 Fuera de alcance.** No se evalúan: la seguridad de GitHub, de Microsoft 365 ni de Ably como productos, que no están comprometidos y cuyo papel aquí es el de servicio abusado; la detección genérica de Cobalt Strike, que es materia de otro producto y cuya cobertura se presupone; el desempaquetado de cada uno de los treinta módulos de shellcode, que la fuente describe funcionalmente sin publicar muestras; la atribución de la operación a un Estado, que ninguna fuente hace y este informe tampoco; y la auditoría de MeshCentral como proyecto de software libre, que es legítimo y ampliamente utilizado.

**3.3 Limitaciones de la colección.** Cinco, y la cuarta es la que condiciona más el valor del documento.

1. **No hay actor.** Kaspersky declara expresamente que carece de información suficiente para atribuir. Todo lo que normalmente se deduce de la identidad —intención, prioridades, selección futura— aquí no se puede deducir. El informe se construye sobre comportamiento.
2. **La vía de entrada inicial es desconocida, y lo dice la fuente.** El expediente empieza con un agente de MeshCentral ya instalado en una organización taiwanesa. Cómo llegó ahí no se sabe; la fuente lo atribuye a la reutilización de una infección previa. Eso significa que **no hay vector inicial documentado y por tanto no hay mitigación de vector inicial que recomendar**. Lo que hay es detección de lo que vino después.
3. **Dos telemetrías parciales, declaradas como tales.** Las dos fuentes advierten que su visibilidad es limitada. La unión de las dos sigue siendo una cota inferior.
4. **El juicio central es nuestro y no está corroborado por sus propios autores.** `KJ-2` sostiene una equivalencia que ni Kaspersky ni Sophos afirman. Se apoya en coincidencias documentales verificables, enumeradas una por una en `O-2.1` para que cualquiera pueda comprobarlas o romperlas, pero **es una inferencia de este informe**, no un hallazgo de proveedor. Si alguno de los dos publica que son operaciones distintas por motivos que no vemos, este documento necesita una versión 2.0.
5. **No se obtuvieron muestras.** Todas las valoraciones técnicas son lecturas de análisis de terceros. No hay verificación propia de ningún hash, ni ejecución controlada, ni confirmación independiente del comportamiento descrito. Las únicas verificaciones propias de este informe son de registro y resolución de dominios, están en `A.5` y se declaran como tales.

**3.4 Metodología.** ICD 203 para el léxico de probabilidad y confianza (Anexo C). Código Admiralty doble para las fuentes (Anexo B). MITRE ATT&CK v18 en `T-2`. Pirámide del Dolor en `T-3`, con una lectura que el modelo de este adversario obliga a invertir. ACH y pre-mortem en `O-6`. **Y una técnica estructurada propia, que es la aportación generalizable de este informe y está en el `Anexo D`: la reconciliación de dos expedientes de proveedor que describen el mismo objeto sin saberlo, a partir de artefactos operativos compartidos en lugar de infraestructura compartida.**

**3.5 Lo que el requisito afirmaba, y lo que las fuentes sostienen**

El requisito que originó este informe consistió en una instrucción de investigar la operación «extensivamente», dos enlaces de prensa —uno a The Hacker News y otro a `cybersecuritynews.com`— y la indicación de traducir fuentes asiáticas si era necesario. Los enunciados evaluables son los de esos dos artículos y los de la propia instrucción.

<!-- cti:table highlight="NO corroborado|Impreciso|Incompleto|No se pudo" -->

| # | Afirmación del requisito o de la prensa citada | Veredicto | Qué dicen las fuentes primarias |
|---|---|---|---|
| 1 | «Kaspersky bautizó la actividad como Operation ShadowCloud y la identificó a principios de 2026» | **Corroborado** | Literal de `B-1`. Dos entregas publicadas el **17 de noviembre de 2026**, firmadas por Saurabh Sharma y Noushin Shabab |
| 2 | «Sectores gubernamentales de Asia y África han sido objetivo» | **Corroborado, pero incompleto** | Literal de `B-1`. **Incompleto porque `B-3` nombra cinco países** —Filipinas, Taiwán, Afganistán, Namibia y probablemente Corea del Sur— que la prensa no recoge porque no relaciona los dos informes. Véase `KJ-3` |
| 3 | «Las puertas traseras usan SharePoint, GitHub y Ably para mando y control» | **Corroborado con precisión** | Exacto, y con el protocolo reconstruido petición a petición en las dos entregas, incluidos los nombres de fichero, los esquemas de cifrado y la estructura JSON |
| 4 | «Comparte cierto grado de solapamiento con la actividad que Sophos rastrea como Bronze Sandcastle» | **Corroborado, y es un eufemismo** | Es literal de `B-2`, que además dice que Sophos «tocó un fragmento» de la campaña. **Pero los dos informes citan la misma cuenta de GitHub, `LatonyCharnleyaW`**, y doce coincidencias más. «Cierto grado de solapamiento» describe mal lo que hay. Véase `O-2.1` y `KJ-2` |
| 5 | «Se han observado similitudes tácticas con campañas previas de FamousSparrow y CopperTurtle» | **Corroborado, con la naturaleza exacta de la evidencia** | `B-2` lo precisa: no son «similitudes tácticas» difusas, son **directorios de preparación compartidos en los mismos sistemas víctima, con los implantes desplegados en una ventana de un día** —6 y 5 de marzo de 2026 para FamousSparrow; 3 y 4 de mayo de 2026 para CopperTurtle—. La fuente dice expresamente que eso «no prueba un vínculo directo» |
| 6 | «Sugiere que un grupo de habla china puede estar desarrollando o utilizando las puertas traseras» | **Corroborado como cita, y conviene no ascenderlo** | Es la conclusión literal de `B-2`, y está formulada con esa prudencia. **No es una atribución**, y la cobertura secundaria que la convierte en «hackers vinculados a China» está añadiendo una afirmación que la fuente no hace. `O-2.2` documenta el margen |
| 7 | «Si es necesario, traducir sitios de Asia» | **No fue necesario, y la comprobación es el resultado** | Se buscó expresamente en chino, incluidos los centros de inteligencia de amenazas de Qi An Xin (奇安信), Antiy (安天) y Threatbook (微步), y en TWCERT/CC de Taiwán. **No existe investigación primaria asiática sobre esta operación**: todo el material en chino localizado es reescritura de Kaspersky o de The Hacker News, y las publicaciones de TWCERT que aparecen corresponden a otras campañas. No hay nada original que traducir |
| 8 | El segundo enlace del requisito, a `cybersecuritynews.com` | **No se pudo leer, y se declara** | El servidor **rechaza la conexión** (`ECONNREFUSED`, no agotamiento de espera), tanto desde este entorno como delegando la lectura. Por su propio titular —que nombra SharePoint y Ably— es una reescritura de la segunda entrega de `B-2`. **No se usa ningún dato suyo en este informe**, y la limitación queda consignada en `B-6` |

> ⚠ **Por qué el punto 4 no es un matiz de redacción.** «Dos operaciones que se
> solapan» y «una operación con dos nombres» piden decisiones distintas. Lo
> primero sugiere un ecosistema con herramientas compartidas, del tipo que
> `CTI-2026-017` documenta con `CopperDragon`, y obliga a tratar cada
> expediente por separado. Lo segundo permite **sumar los dos conjuntos de
> víctimas, los dos rangos temporales y los dos catálogos de indicadores en un
> único expediente**, que es exactamente lo que hace falta para responder «¿desde
> cuándo?» y «¿a quién?». Este informe sostiene lo segundo, con la confianza
> declarada en `KJ-2` y con las coincidencias enumeradas para que se puedan
> romper. Si alguien las rompe, hace un favor.

---

# NIVEL ESTRATÉGICO
### Para: Consejo · CISO · Riesgo · Legal · Horizonte: 6–24 meses

## E-1. Qué significa que el mando y control sea un servicio que pagamos nosotros

Durante veinte años la defensa de red se construyó sobre una premisa que este expediente retira: que la infraestructura del adversario es *suya*, y que por tanto se puede nombrar, listar, bloquear y dar de baja. Esa premisa sostiene los indicadores de compromiso, las listas de reputación, el filtrado de salida por destino, los acuerdos de retirada con registradores y buena parte del valor comercial de la inteligencia de amenazas. Cuando el canal de mando y control es un repositorio de GitHub, una biblioteca de documentos de SharePoint y un canal de mensajería de Ably, **no hay nada que nombrar que no sea algo que la organización necesita**.

Conviene ser preciso sobre qué es nuevo y qué no. El uso de servicios legítimos como punto de depósito no es nuevo: esta cartera lo documenta en `CTI-2026-025` con los *dead drop resolvers* de Gamaredon sobre Telegra.ph y Mastodon, y en `CTI-2026-019` con almacenamiento comercial compatible con S3 como destino de exfiltración. Lo que este expediente añade es de grado y de completitud: no es un punto de depósito auxiliar para resolver la dirección del verdadero servidor, es **el canal entero**. Las órdenes llegan en ficheros de un repositorio; los resultados se suben a otro repositorio; el inventario de víctimas vive en un *issue* de GitHub cuyo número de incidencia hace de identificador de sesión; la configuración del túnel llega por un canal de mensajería; y los módulos adicionales se descargan del mismo repositorio. No hay un segundo salto hacia un servidor propio. El adversario ha externalizado su infraestructura a tres proveedores con acuerdo de nivel de servicio.

Las consecuencias estratégicas son cuatro, y ninguna es técnica.

<!-- cti:cards -->

| Título | Texto | Etiqueta |
|---|---|---|
| El bloqueo deja de ser una opción | No se puede bloquear GitHub en una organización que desarrolla software, ni Microsoft Graph en una que usa Microsoft 365. **El control tiene que mudarse del destino al comportamiento y a la identidad**, que son más caros de instrumentar y exigen telemetría que muchas organizaciones no recogen | Control |
| La retirada deja de ser una mitigación | Las cuentas de GitHub de este expediente se dan de baja —la principal ya está retirada— y el adversario abre otra. Hay **nueve cuentas documentadas** con fechas de creación escalonadas a lo largo de quince meses: el recambio ya está en el diseño | Resiliencia |
| La atribución se queda sin su mejor insumo | Sin servidores propios no hay registros de alojamiento, ni patrones de registro de dominios, ni reutilización de certificados, que son la materia prima habitual de la atribución por infraestructura. Lo que queda son **artefactos operativos**: nombres de cuenta, direcciones de correo, rutas de compilación, mensajes de *commit* | Atribución |
| El riesgo se traslada al tercero | Dos inquilinos ajenos de Microsoft 365 aparecen alojando los datos de las víctimas. Si fueran inquilinos comprometidos de pequeñas empresas, **esas empresas son parte de la cadena sin saberlo**, con las implicaciones legales y de notificación que eso arrastra en cualquier jurisdicción con régimen de protección de datos | Legal |

> **La pregunta de consejo que este expediente plantea.** No es «¿estamos
> expuestos a ShadowCloud?» —no lo estamos, no hay víctimas americanas—. Es
> **«¿cuántos de nuestros controles de salida siguen siendo listas de
> destinos?»**. Si la respuesta es «la mayoría», entonces la organización está
> preparada para el adversario de 2015 y este informe describe el de 2026, con
> independencia de quién sea y de a quién ataque hoy.

## E-2. Victimología, y el agujero organizativo que este caso ilumina

La victimología conocida, una vez unidos los dos expedientes conforme a `KJ-2`, es la siguiente. Conviene leer la tabla sabiendo que **mezcla dos telemetrías de dos proveedores con criterios de clasificación distintos**, y que ninguno publica recuentos.

<!-- cti:bars title="Países con víctima nombrados por las dos fuentes (presencia declarada, no recuento de víctimas)" -->

| Etiqueta | Valor |
|---|---|
| Taiwán (las dos fuentes; origen de la investigación de Kaspersky) | 3 |
| Filipinas (Sophos) | 2 |
| Afganistán (Sophos) | 2 |
| Namibia (Sophos) | 2 |
| Corea del Sur (Sophos, como probable) | 1 |
| «Asia y África, principalmente gobierno», sin desglose (Kaspersky) | 3 |
| América (cualquier país) | 0 |

El criterio de selección que se desprende es el de un servicio de inteligencia con intereses regionales en el Indo-Pacífico y presencia puntual en África austral y en Asia Central. Taiwán aparece en los dos expedientes, y es donde arranca la investigación de Kaspersky. Namibia es el caso que rompe la lectura puramente regional, y conviene no sobreinterpretarlo: una víctima en África austral puede responder a intereses de minería, de infraestructura o de posición diplomática, y ninguna fuente lo explica.

**Lo que este expediente ilumina, y es la aportación que se puede reutilizar, es un patrón organizativo hermano del que `CTI-2026-034` identificó para las plataformas geoespaciales.** Allí el hueco era «plataforma empresarial comprada por un área funcional y administrada por ella, fuera del inventario y del ciclo de parcheo». Aquí el hueco es distinto y más extendido: **la herramienta de administración remota que entró por un proyecto y se quedó**.

El vector inicial documentado de esta operación es un agente de MeshCentral ya presente en la red. La fuente dice que no sabe cómo llegó y que probablemente se reutilizó una infección anterior; pero el dato operativo relevante es otro, y es que **un agente de administración remota con un servidor de mando codificado a fuego dentro, apuntando a una dirección IP en el extranjero, estuvo funcionando en una organización el tiempo suficiente para que un adversario lo usara como punto de partida**. Esto no es una vulnerabilidad: es un problema de inventario. Y es exactamente el mismo problema que `CTI-2026-035` documentó para los ocho productos comerciales de administración remota que una operación de extorsión elige según lo que ya esté instalado.

<!-- cti:cards -->

| Título | Texto | Etiqueta |
|---|---|---|
| El criterio que funciona | No es «¿este producto es malicioso?» —MeshCentral no lo es, es software libre legítimo y muy usado—. Es **«¿quién autorizó este agente, contra qué servidor habla, y sigue siendo necesario?»**. Las tres preguntas son de inventario, no de seguridad | Método |
| Por qué se escapa | Los agentes de administración remota los instala, casi siempre, alguien con una razón legítima y con prisa: un proveedor durante una migración, un integrador durante un despliegue, un área técnica durante una incidencia. **Y casi nunca los desinstala nadie**, porque desinstalarlos no es tarea de nadie en particular | Causa |
| La generalización | El criterio común con el eje de `CTI-2026-034` es **toda capacidad de acceso remoto o de administración que entró por un proyecto y sobrevivió al proyecto**: agentes de RMM, cuentas de servicio de integrador, túneles de soporte, VPN de proveedor, extensiones de plataforma | Reutilizable |
| Lo que lo distingue | A diferencia del eje geoespacial, aquí **el adversario no explotó nada**. Encontró una puerta ya abierta y la usó. Eso lo hace más difícil de prevenir con parches y más fácil de prevenir con inventario | Contraste |

## E-3. Tendencia y pronóstico

La serie que importa no es la de víctimas —no hay datos— sino la de **preparación de infraestructura**, porque es la única que las fuentes publican con fechas exactas: las fechas de creación de las nueve cuentas de GitHub del conjunto, más las fechas de registro de los dominios verificadas en `A.5`.

<!-- cti:chart title="Preparación de infraestructura por trimestre: cuentas de GitHub creadas y dominios registrados" cap="El eje mide altas nuevas de infraestructura en el trimestre, sumando cuentas de GitHub (fechas publicadas por Kaspersky) y dominios verificados en A.5. No mide actividad ni víctimas: mide aprovisionamiento. La serie empieza quince meses antes de la primera observación de cualquiera de los dos proveedores." -->

| Periodo | Valor |
|---|---|
| 3T·24 | 1 |
| 4T·24 | 0 |
| 1T·25 | 1 |
| 2T·25 | 0 |
| 3T·25 | 0 |
| 4T·25 | 6 |
| 1T·26 | 0 |
| 2T·26 | 1 |
| 3T·26 | 0 |
| 4T·26 | 0 |

La forma de la serie dice tres cosas. Primero, que **la preparación empieza en septiembre de 2024**, once meses antes de la primera observación de Sophos y quince antes de la de Kaspersky: quien quiera estimar la antigüedad de esta operación por la fecha de los informes se equivoca en más de un año. Segundo, que **el cuarto trimestre de 2025 concentra seis de las nueve cuentas**, lo que es compatible con una expansión deliberada de capacidad —más cuentas, más víctimas simultáneas, menos riesgo de que una baja lo tire todo— y es el período que mejor explica por qué dos proveedores distintos empiezan a verlo en 2026. Tercero, que **la serie no se detiene con la exposición**: `ekmt[.]tw` se registró en abril de 2026, bien entrada la ventana de observación de Sophos.

<!-- cti:cards -->

| Título | Texto | Etiqueta |
|---|---|---|
| Pronóstico a 6 meses | **Muy probable** *(80–95 %)* que la operación continúe con cuentas nuevas y nombres de repositorio nuevos, y que los indicadores de cuenta de `A.2` caduquen antes que cualquier otro indicador del expediente. El recambio está en el diseño, no es una reacción | Continuidad |
| Pronóstico a 12 meses | **Probable** *(55–80 %)* que aparezca una tercera designación de proveedor para esta misma operación antes de que alguien publique la equivalencia. El patrón de este expediente —dos informes sin citarse— es un problema estructural del mercado, no un accidente | Taxonomía |
| Difusión del modelo | **Probable** *(55–80 %)* que el patrón de «canal entero sobre nube corporativa» aparezca en operaciones no relacionadas, incluidas criminales, en los próximos doce meses. Es barato, no requiere comprar nada y derrota los controles más extendidos | Imitación |
| Lo que lo frenaría | Que los proveedores de nube instrumenten la detección del abuso **del lado del servicio**: patrones de uso de API incompatibles con un cliente de desarrollo, cuentas recién creadas con un único repositorio y actividad de escritura constante. No está en nuestras manos, y no hay señales de que esté en curso | Dependencia |

## E-4. Decisiones que este informe pide al nivel estratégico

<!-- cti:table highlight="Ably|inquilino|inventario|30 días" -->

| # | Decisión | Por qué ahora | Plazo | Responsable |
|---|---|---|---|---|
| E-a | **Aprobar la vigilancia de `ably.io` y `ably.net` desde el parque de puestos de usuario**, en modo alerta primero y bloqueo después si el ruido es tolerable | Es el único de los tres servicios de este expediente sin uso corporativo plausible en un puesto de trabajo, y por tanto el único con relación coste-beneficio favorable. `KJ-5` | 30 días | CISO · Operación de red |
| E-b | **Añadir el GUID de inquilino `8f50c589-a4d6-4df4-95bb-2fb7f5983fe5` a la vigilancia de autenticación**, y decidir si se adopta una política de acceso entre inquilinos que restrinja los inquilinos ajenos permitidos | Indicador de altísima especificidad y coste de falso positivo nulo. `KJ-4`, `X-5.2`. **Y la decisión de fondo —restringir inquilinos ajenos— tiene impacto en negocio y no la puede tomar el SOC** | 30 días para la vigilancia; 90 para la política | CISO · Administración de identidad |
| E-c | **Encargar un inventario de agentes de administración remota y de capacidades de acceso de proveedor**, con las tres preguntas de `E-2`: quién lo autorizó, contra qué servidor habla, sigue siendo necesario | El vector inicial de esta operación fue un agente legítimo ya instalado. No es un problema de parcheo y por tanto el ciclo de parcheo no lo va a encontrar | 90 días | CISO · Gobierno de TI |
| E-d | **No incorporar los agregados planos de este informe a bloqueo automático sin leer `A.4`** | El Anexo A contiene una dirección IP que casi con certeza es un error tipográfico de la fuente primaria y que pertenece a una cooperativa eléctrica rural ajena al expediente. Es el tipo de corte autoinfligido que la portada de este repositorio advierte | Inmediato | Ingeniería de detección |
| E-e | **Decidir si se abre revisión de `CTI-2026-017`** a raíz de `KJ-7` | Nuestro propio informe sostiene una concentración del 90 % del esfuerzo de FamousSparrow en Latinoamérica, y esta operación lo sitúa en víctimas asiáticas y africanas en marzo de 2026. **No hay contradicción probada** —falta el dato geográfico del sistema concreto—, pero hay tensión y queda como `I-1` | 60 días | Célula CTI |
| E-f | **Comunicar a la dirección que este expediente no supone exposición propia**, y explicar por qué se emite igualmente | Media parte del valor de un servicio de inteligencia es decir «esto no nos afecta» con argumentos, en lugar de reenviar todo lo que publica un proveedor. **Y la otra media es explicar qué del método sí nos afecta** | 30 días | CISO |

---

# NIVEL OPERACIONAL
### Para: Jefatura de SOC · Respuesta a Incidentes · Threat Hunting · Horizonte: semanas–meses

## O-1. Identificación y alias

<!-- cti:table highlight="misma operación|Sin atribuir" -->

| Designación | Quién la usa | Estado en este informe |
|---|---|---|
| **Operation ShadowCloud** | Kaspersky GReAT, 17-11-2026 | **Designación de campaña, sin atribuir.** Nombre de la operación, no del actor. Es la etiqueta que este informe usa por ser la más descriptiva del conjunto |
| **BRONZE SANDCASTLE** | Sophos CTU, 20-10-2026 | **La misma operación**, con confianza *muy probable* (`KJ-2`). Designación de actor en la taxonomía de Secureworks heredada por Sophos, donde el prefijo `BRONZE` marca nexo con China |
| **GitDoor** | Kaspersky | Puerta trasera con mando y control en repositorios de GitHub. Versión embebida observada: `1.1.6` |
| **GraphDoor** | Kaspersky | Puerta trasera con mando y control en SharePoint a través de la API de Microsoft Graph. Versión embebida observada: `1.2.7` |
| «Meterpreter modificado», versiones `1.1.5` y `1.1.7` | Sophos | **Casi con certeza la misma familia de código** que `GitDoor`, por intercalado de versiones y coincidencia de artefactos (`O-2.1`). Sophos advierte que, pese al parecido con el cargador reflexivo de Metasploit, **no es un artefacto estándar de ese marco** |
| **FamousSparrow** · *SparroWocky* | ESET, Kaspersky | **Actor distinto, coexistente.** `CTI-2026-017` es su expediente. Aquí aparece compartiendo directorio de preparación, no como operador de estas puertas traseras |
| **CopperTurtle** · *BlackTech* | Kaspersky; alias recogido por `B-4` | **Actor distinto, coexistente.** Despliega el RAT `PLEAD`. Mismo patrón de coexistencia que el anterior |
| BRONZE PRESIDENT · BRONZE ATLAS | Sophos | **No son este actor.** Sophos declara solapamiento **de zona geográfica de objetivos** y dice expresamente que no pudo vincular la actividad a ninguno de los dos, razón por la cual creó una designación nueva. `BRONZE PRESIDENT` es Mustang Panda, expediente `CTI-2026-027` |

> ⚠ **Lo que no se debe hacer con esta tabla.** `FamousSparrow` y `CopperTurtle`
> **no son alias de esta operación**, y tratarlos como tales sería cometer el
> error que esta cartera corrige en tres informes (`CTI-2026-017`,
> `CTI-2026-022`, `CTI-2026-030`). Lo que la fuente documenta es
> **coexistencia en la misma víctima con un día de diferencia**, que es un dato
> fuerte sobre relación operativa y **ninguno** sobre identidad. Importar la
> biblioteca de detección de FamousSparrow no cubre esta operación, y al revés
> tampoco.

## O-2. Estructura y atribución

### O-2.1 — Las trece coincidencias entre los dos expedientes

Esta es la sección que sostiene `KJ-2` y, por tanto, la aportación propia del informe. Cada fila es verificable contra los dos documentos públicos citados en `B-1`, `B-2` y `B-3`. **Se publican para que se puedan romper**: si alguna es falsa o se explica mejor por un arsenal compartido que por una identidad común, el juicio baja.

| # | Coincidencia | En Kaspersky (`ShadowCloud`) | En Sophos (`BRONZE SANDCASTLE`) | Peso |
|---|---|---|---|---|
| 1 | **La cuenta de GitHub** | `/repos/LatonyCharnleyaW/Havo` y `/repos/LatonyCharnleyaW/Trix` como canal de órdenes y de resultados | `hxxps://api[.]github[.]com/repos/LatonyCharnleyaW` como origen de la configuración de la versión `1.1.7` | **Decisivo.** Una cuenta no es una dirección IP: no se comparte por alojamiento común ni por un proveedor de servicios. Es una credencial operativa |
| 2 | **El esquema de nombres de fichero** | `main.%victim_unique_code%.js.map`, con el código de ocho caracteres alfanuméricos | Tres ficheros concretos en ese repositorio: `main.3ku8inqb.js.map`, `main.lhxjkkai.js.map`, `main.y8hnze7q.js.map` | **Decisivo.** Los tres encajan carácter a carácter con el esquema que Kaspersky describe, incluida la longitud del código |
| 3 | **Los módulos con extensión `.ts`** | Plugins `kl.ts`, `pr.ts`, `scr.ts`, `moveDir.ts`, `channel.ts`, `abchannel.ts`, `ab2channel.ts` descargados del repositorio | Sophos observa «ficheros `.ts` cifrados» en el mismo repositorio sin identificar su función | **Alto.** Sophos vio los módulos sin saber qué eran; Kaspersky los documenta uno por uno |
| 4 | **El fichero de carga cifrada** | `config.ini` junto al cargador, leído con `NtCreateFile`/`NtReadFile` | `config.ini` con la carga cifrada, decodificada en memoria | **Alto** |
| 5 | **El par `javaw.exe` + `jli.dll`** | `jli.dll` como cargador, anfitrión `javaw.exe` (OpenJDK) | Primera fila de su tabla de carga lateral: `javaw.exe` con `jli.dll` | **Alto** |
| 6 | **El par Sandboxie `Start.exe` + `sbiedll.dll`** | `start.exe` (Sandboxie Start) con `SbieDll.dll`; el cargador se identifica internamente como `SbieDll_st.dll` | `Start.exe` (ejecutable de Sandboxie renombrado) con `sbiedll.dll`, y además `SandboxieWUAU.exe` | **Alto.** Es la firma que da nombre a la cobertura secundaria de Sophos |
| 7 | **`libcef.dll` como cargador** | `libcef.dll` en su lista de cargadores | `Jcef_helper.exe` con `Libcef.dll` | **Medio.** Par de carga lateral conocido y usado por otros actores |
| 8 | **Ably** | Plugins `abchannel.ts` y `ab2channel.ts`; proxy SOCKS5 sobre el servicio compatible con Pusher; la clase de los hilos vive en el *namespace* `ably` | `ably[.]net` y `ably[.]io` entre los servicios legítimos usados para tareas | **Alto.** Ably es un servicio poco común; su aparición en los dos expedientes no es casual |
| 9 | **`gofile.io`** | Módulo `Fileupload` que sube a `upload.gofile[.]io` | `gofile[.]io` y `file[.]io` entre los servicios legítimos usados | **Medio-alto** |
| 10 | **Cargador de COFF propio** | Orden `scload`: bytes COFF en Base64, cargados en memoria, invocando la función de entrada `go` | Sophos identifica elementos de `COFFLoader` en el implante y deduce un BOF propio | **Alto.** La convención de la función de entrada `go` y el uso de BOF coinciden |
| 11 | **Aplanamiento del flujo de control** | Declarado expresamente, más envoltorios anidados y llamadas indirectas | «Despachador de flujo aplanado (máquina de estados)» | **Medio.** Técnica de ofuscación extendida, pero suma |
| 12 | **El intercalado de versiones** | `"client_version":"1.1.6"` en `GitDoor`; `"client_version":"1.2.7"` en `GraphDoor` | Dos versiones analizadas: `1.1.5` y `1.1.7` | **Decisivo para la lectura de familia única.** Cuatro versiones de cuatro muestras distintas, de dos proveedores, sin un hueco: `1.1.5` → `1.1.6` → `1.1.7` → `1.2.7` |
| 13 | **Taiwán** | Origen de la investigación: dos instancias de MeshCentral en una organización taiwanesa | Taiwán entre los cinco países con víctima | **Medio.** Por sí solo no probaría nada; con los doce anteriores, encaja |

> ✅ **Cómo leer el peso de la fila 1, que es la que decide.** Dos informes que
> comparten una dirección IP pueden estar describiendo a dos actores que
> alquilan al mismo proveedor. Dos informes que comparten un dominio pueden
> estar describiendo a dos actores que compran al mismo intermediario. **Dos
> informes que comparten una cuenta de usuario con credencial de escritura
> están describiendo a quien tiene esa credencial.** Una cuenta de GitHub con
> un *personal access token* que escribe en un repositorio privado no es
> infraestructura compartible: es la mano del operador. Por eso el juicio de
> `KJ-2` está en *muy probable* y no en *probable*.

### O-2.2 — La atribución, y el margen que conviene no cruzar

Lo que cada fuente afirma, literalmente:

- **Kaspersky** dice que carece de información suficiente para atribuir la actividad a un grupo concreto; que observa solapamientos con grupos de habla china como FamousSparrow y CopperTurtle; y que ese solapamiento **«no prueba un vínculo directo»**, aunque «sugiere que un grupo de habla china puede estar desarrollando y/o utilizando» las dos puertas traseras.
- **Sophos** califica al grupo de «con base en China» pero marcándolo como **sospecha**, y apoya esa sospecha en dos cosas: el solapamiento geográfico de objetivos con `BRONZE PRESIDENT` y `BRONZE ATLAS` —sin poder vincularlo a ninguno de los dos— y la **concentración horaria de la actividad en UTC+8**, que relaciona con la jornada laboral conocida como «996».

Son dos bases de atribución **de calidad distinta y ninguna de las dos fuerte**. La concentración horaria es un indicio real pero compatible con una franja que incluye China continental, Taiwán, Hong Kong, Singapur, Malasia, Filipinas y Australia Occidental. El solapamiento geográfico de objetivos es el indicio más débil de todos, porque los objetivos de interés para un servicio son objetivos de interés para varios. Y la coexistencia en la misma víctima que documenta Kaspersky admite al menos tres lecturas, que `O-6` desarrolla.

**Este informe añade una tercera base, independiente de las dos anteriores, y es `KJ-6`.** No es más fuerte que las otras, pero es de otra naturaleza —lingüística y de artefacto de desarrollo, no de telemetría— y por eso suma:

| Artefacto | Dónde aparece | Lectura |
|---|---|---|
| `dhj_exe` | Campo de la configuración embebida de `GitDoor` (`"dhj_exe":"start.exe"`) y de `GraphDoor` (`"dhj_exe":"javaw.exe"`). Nombra el ejecutable legítimo anfitrión de la carga lateral | **Iniciales de pinyin de «DLL 劫持»** (*DLL jiéchí*, secuestro de DLL). El campo describe exactamente eso: el binario sobre el que se hace el secuestro. **Inferencia propia, confianza moderada** |
| `is_need_lock` | Campo de la configuración embebida de las dos puertas traseras | Calco sintáctico de **«是否需要锁»** (*shìfǒu xūyào suǒ*, «si hace falta cerrojo»). La construcción `is_need_*` no es inglés nativo. **Inferencia propia** |
| `imzimzgo 2.2.0 x64` | Nombre interno del módulo de volcado de credenciales | Mimikatz renombrado. El patrón `imz`-`imz`-`go` parece una ofuscación por repetición de sílaba, con el sufijo `go` de la convención de entrada de los COFF. **Observación, sin lectura idiomática** |
| `commit from INSOMNIA` | Mensaje de *commit* en las subidas a GitHub **y** en las subidas a SharePoint | **Artefacto de desarrollo, no de idioma.** El operador prototipó las peticiones HTTP en el cliente Insomnia y dejó el mensaje por omisión. **Es la prueba más limpia de que las dos puertas traseras salen del mismo banco de trabajo**: el mismo literal viaja en dos protocolos distintos |
| `C:/Users/user/Desktop/pythonrat/proxytest/Erfrp-0.1/frpc.go` | Ruta de compilación dentro del cliente de proxy en Go | Carpeta de desarrollo llamada `pythonrat` para un proyecto escrito en Go. Sugiere **un banco de trabajo reutilizado** entre proyectos, y el nombre del directorio padre nombra la función: RAT |
| `C:\src\Dll1\WhatsAppCS\x64\Release\WhatKeyCPP.pdb` | Ruta PDB del módulo extractor de la clave de WhatsApp | `Dll1` es el nombre por omisión que Visual Studio da a un proyecto de DLL. **Indica desarrollo poco disciplinado en los módulos periféricos**, en contraste con la ofuscación cuidada del núcleo |

> ⚠ **El margen que no hay que cruzar.** Todo lo anterior sostiene, como mucho,
> que **quien escribió este código habla chino y trabaja en una franja horaria
> compatible con Asia oriental**. No sostiene qué Estado lo patrocina, ni si
> hay patrocinio, ni qué servicio lo dirige. La cobertura secundaria que titula
> «hackers vinculados a China» está añadiendo un eslabón que ninguna de las dos
> fuentes pone. Esta cartera documenta en `CTI-2026-033` un caso idéntico de
> ascenso de confianza en la cobertura secundaria, y el remedio es el mismo:
> citar el grado que declara la fuente, no el que resulta más legible.

### O-2.3 — La tensión con `CTI-2026-017`, y por qué se deja abierta

`CTI-2026-017` lleva por titular que FamousSparrow «concentra el 90 % de su esfuerzo en Latinoamérica» desde mediados de 2025, y su nodo en el grafo de actores lo repite. Kaspersky documenta ahora que, el **6 de marzo de 2026**, un implante de FamousSparrow —`excint.exe`, un componente renombrado de Avast Antivirus, cargando lateralmente `wtsapi32.dll`, con carga descifrada por RC4 con la clave `iotrh^%4CFGTj` ya conocida de ese actor— estaba en un sistema donde `GitDoor` se había instalado **el día anterior**, en un subdirectorio del mismo directorio de preparación (`%ProgramData%\excInt\sg\`).

El conjunto de víctimas declarado de esta operación es Asia y África. Si ese sistema concreto está en Asia o África, entonces FamousSparrow tenía actividad fuera de Latinoamérica en marzo de 2026, y el «90 %» de nuestro informe necesita al menos una nota. **Pero la fuente no dice de qué país es el sistema**, y no se puede deducir: la tabla de Kaspersky da el directorio y la fecha, no la ubicación.

Por eso `KJ-7` está en *aproximadamente igual de probable* con **confianza baja**, y la consecuencia no es una corrección sino un requisito de colección (`I-1`). Lo que sí se puede afirmar sin ambigüedad, y es útil, es que **la clave RC4 `iotrh^%4CFGTj` y el par `excint.exe` + `wtsapi32.dll` no figuran en `CTI-2026-017`**: son material nuevo para ese expediente con independencia de cómo se resuelva la cuestión geográfica, y van al Anexo A de este informe marcados como tales.

## O-3. Modelo de operación

### O-3.A — La cadena, en una frase por fase

1. **Entrada.** Desconocida. El expediente arranca con un agente de MeshCentral ya instalado, apuntando a `wss://27.102.66[.]162:443/agent.ashx`. La fuente atribuye su presencia a la reutilización de una infección anterior.
2. **Despliegue.** Desde el agente se dejan tres ficheros en el mismo directorio: un binario legítimo firmado, una DLL maliciosa que ese binario carga implícitamente, y un `config.ini` con la carga cifrada.
3. **Carga.** La DLL descifra el `config.ini` —con RC4 más XOR, o sólo XOR, según el tipo de cargador— y **inyecta el resultado en la memoria del propio proceso legítimo**. Nada de la puerta trasera toca el disco en claro.
4. **Registro.** La puerta trasera abre un *issue* en el repositorio privado de GitHub, o sube un fichero a la biblioteca de SharePoint, con la información del sistema cifrada. **El número de incidencia que devuelve GitHub es el identificador de sesión.**
5. **Trabajo.** El operador deja ficheros de órdenes en el repositorio público; la puerta trasera los busca por su propio código de víctima, los descifra y ejecuta. Los módulos adicionales se descargan del mismo sitio y se ejecutan en memoria.
6. **Tránsito.** Cuando hace falta alcanzar algo que no está en Internet, se levanta un proxy: un cliente de `frp` modificado hacia una de las 22 direcciones publicadas, o un SOCKS5 tunelado sobre WebSocket de Ably.
7. **Cosecha.** Credenciales con Mimikatz, *cookies* de navegador con CookieKatz directamente de la memoria del proceso, pulsaciones de teclado a `logs.dat`, capturas de pantalla, y la clave de descifrado de la base de datos de WhatsApp.

### O-3.B — Lo que revela el diseño del canal

Tres decisiones de diseño merecen atención operativa porque determinan dónde se puede detectar.

**La primera es la separación de repositorios.** Las órdenes bajan de un repositorio **público** y los resultados suben a uno **privado**. Es una asimetría deliberada y tiene una consecuencia defensiva: la mitad descendente del canal **no necesita credencial**, y por tanto una petición `GET` anónima a un repositorio público es indistinguible de cualquier otra. La mitad ascendente sí lleva un *personal access token*, y eso sí deja rastro distinguible —una cabecera `Authorization` hacia `api.github.com` desde un proceso que no es un cliente de desarrollo—.

**La segunda es el disfraz de proyecto de desarrollo web.** Los ficheros de órdenes se llaman `main.<código>.<4 caracteres>.js.<extensión>`; los de datos, `main.<código>.js.map`; los módulos, `.ts`. Un repositorio lleno de mapas de código y de ficheros TypeScript **es exactamente lo que parece un proyecto de interfaz web**. No es ofuscación criptográfica: es camuflaje semántico, dirigido a un analista humano que mire la lista de ficheros y pase de largo.

**La tercera, y la más interesante, es que `GraphDoor` no lleva dominio de mando y control.** La fuente lo dice expresamente: la dirección y el puerto del proxy llegan **en tiempo de ejecución**, por la orden `info` del plugin de canal o por un canal de Ably. Eso está diseñado contra el análisis estático: quien obtenga la muestra no obtiene la infraestructura. Y tiene un corolario defensivo que conviene explotar: **si la infraestructura no está en la muestra, la muestra tampoco puede delatar a la infraestructura, pero la infraestructura tiene que llegar por un canal — y ese canal es Ably**. Por eso `KJ-5` señala Ably como el eslabón flojo: no es sólo tráfico anómalo, es **el único punto por el que el adversario está obligado a pasar para que su propio diseño funcione**.

### O-3.C — Las nueve cuentas, y lo que dicen de la operación

Kaspersky publica la tabla completa de cuentas de GitHub con su fecha de creación y una versión parcialmente ocultada de la dirección de correo asociada. Es el artefacto más revelador del expediente sobre cómo se gestiona la operación, y merece leerse como tal:

| Cuenta | Repositorio de subida | Repositorio de descarga | Creación | Correo |
|---|---|---|---|---|
| `LatonyCharnleyaW` | `Trix` | `Havo` | *(retirada)* | *(retirada)* |
| `StevenDFournier` | `spaceJS` | — | 2024-09-03 | `steve***@outlook.com` |
| `JeneLeo` | `silverPot` | `laughbot` | 2025-03-21 | `Jenevie***@yahoo.com` |
| `VenoraKlanimU` | `logdata` | `appdb` | 2025-10-20 | `Venora***@yahoo.com` |
| `AlexandaJazzmynwC` | `PulseHub` | `QuantumVault` | 2025-11-19 | `Alexanda***@yahoo.com` |
| `FloraineSuvitC` | `NexaCore` | `DataFlowX` | 2025-11-19 | `Floraine***@yahoo.com` |
| `bvgarciajocelynxccZ` | `DataSphere` | `CodeForge` | 2025-12-04 | `bvgarcia***@yahoo.com` |
| `Eclemensadolph1n` | `DataCore` | `alpha` | 2025-12-04 | `Eclemen***@yahoo.com` |
| `aYulysseserinYtas` | `Solix` | `Zephyr` | 2025-12-05 | `aYulysses***@yahoo.com`|

Cuatro lecturas operativas, y la cuarta es la que importa para la detección:

1. **El nombre de la cuenta deriva del nombre del correo**, no al revés, y los nombres de persona son occidentales con sufijos aleatorios añadidos (`...aW`, `...wC`, `...xccZ`, `...1n`, `...Ytas`). Es el patrón de quien automatiza la creación de identidades a partir de una lista de nombres.
2. **El proveedor de correo cambia una sola vez**: la primera cuenta usa Outlook y las ocho siguientes, Yahoo. Alguien tomó una decisión después del primer intento.
3. **Los nombres de repositorio son genéricos de producto tecnológico** —`DataSphere`, `CodeForge`, `QuantumVault`, `NexaCore`, `PulseHub`— y refuerzan el camuflaje semántico de `O-3.B`.
4. **Las parejas se crean el mismo día, y dos pares comparten día exacto** (19 de noviembre y 4 de diciembre de 2025). Eso significa que **la unidad de aprovisionamiento es la pareja de repositorios, no la cuenta**, y que hubo al menos dos sesiones de aprovisionamiento por lotes. Para la caza, la consecuencia es que **si se encuentra una de las dos mitades en el tráfico, la otra está en el mismo entorno**: buscar sólo el repositorio de descarga deja la mitad del canal sin ver.

## O-4. Nuestra exposición

**No hay exposición observada, y este apartado es un cuestionario.** Sin telemetría propia no se puede medir nada; lo que sigue son las seis preguntas cuya respuesta decide si este expediente es irrelevante o sólo no observado.

| # | Pregunta | Por qué decide | Dónde está la respuesta |
|---|---|---|---|
| Q-1 | ¿Hay agentes de MeshCentral, o de cualquier otro RMM, en el parque, y sabemos quién autorizó cada uno y contra qué servidor habla? | Es el vector inicial documentado. Y es la pregunta de `E-c` | Inventario de software · `H-1` |
| Q-2 | ¿Vemos tráfico a `ably.io` o `ably.net` desde puestos de usuario o servidores que no sean de desarrollo? | Es el eslabón flojo de `KJ-5` y el control de `E-a` | Registros de proxy o DNS · `H-2` |
| Q-3 | ¿Registramos las peticiones a `login.microsoftonline.com` con la ruta completa, de modo que el GUID de inquilino sea consultable? | Sin la ruta, el indicador de `KJ-4` es inutilizable: todo el mundo habla con ese host | Proxy con inspección TLS · `H-3`, `T-5` |
| Q-4 | ¿Podemos distinguir una llamada a `api.github.com` con cabecera de autorización hecha por un proceso que no es un cliente de desarrollo? | Es la mitad ascendente del canal de `GitDoor`, y la única que lleva credencial | Telemetría de proceso + red · `H-4` |
| Q-5 | ¿Alertamos cuando un binario firmado legítimo se ejecuta desde `C:\Windows\System32\` o desde `%ProgramData%\` fuera de su ruta de instalación, con una DLL de su mismo nombre al lado? | Es la firma de carga de toda la cadena, en las dos designaciones de proveedor | EDR · `H-5`, `H-6` |
| Q-6 | ¿Tenemos política de acceso entre inquilinos, y sabemos qué inquilinos ajenos de Microsoft 365 alcanzan nuestros puestos? | Es la mitigación estructural de `X-5.2`, y la única que mata la técnica en vez de detectarla | Administración de identidad · `E-b` |

> ⚠ **La trampa de este apartado.** La tentación, en un informe sin exposición
> propia, es cerrarlo con «no nos afecta» y archivar. Las seis preguntas de
> arriba **no son sobre este adversario**: son sobre si nuestros controles
> verían a *cualquiera* que use este modelo. Y `E-3` valora como *probable* que
> el modelo se difunda a operaciones no relacionadas en doce meses. El
> expediente es ajeno; el hueco que describe, no necesariamente.

## O-5. Cronología

<!-- cti:timeline -->

| Fecha | Hecho | Traza |
|---|---|---|
| **2024-09-03** | **Se crea `StevenDFournier`, la primera cuenta de GitHub conocida del conjunto.** Es la fecha que fija el comienzo real de la preparación: once meses antes de la primera observación de cualquier proveedor | Infraestructura |
| 2025-03-21 | Se crea `JeneLeo`, con su pareja de repositorios `silverPot` / `laughbot` | Infraestructura |
| **2025-08** | **Comienza la ventana de observación de Sophos** sobre la actividad que llamará `BRONZE SANDCASTLE` | Sophos |
| 2025-10-20 | Se crea `VenoraKlanimU` | Infraestructura |
| **2025-11-19** | **Dos cuentas creadas el mismo día** (`AlexandaJazzmynwC`, `FloraineSuvitC`): primera sesión de aprovisionamiento por lotes | Infraestructura |
| 2025-12-04 | Otras dos cuentas el mismo día (`bvgarciajocelynxccZ`, `Eclemensadolph1n`) | Infraestructura |
| 2025-12-05 | Se crea `aYulysseserinYtas`, la última cuenta documentada | Infraestructura |
| **2026-principios** | **Kaspersky identifica la campaña** que llamará `Operation ShadowCloud`, investigando dos instancias de MeshCentral en una organización **taiwanesa** | Kaspersky |
| **2026-03-05** | **`GitDoor` se instala en `%ProgramData%\excInt\sg\`** (`zoomit.exe` + `WINMM.dll`) en un sistema víctima | Coexistencia |
| **2026-03-06** | **Al día siguiente, un implante de FamousSparrow aparece en el directorio padre** (`excint.exe` + `wtsapi32.dll`, clave RC4 `iotrh^%4CFGTj`). Es la base de `KJ-7` y de `O-2.3` | Coexistencia |
| 2026-04-23 | **Se registra `ekmt[.]tw`** (verificación propia, `A.5`). La operación sigue aprovisionando con Sophos ya observándola | Infraestructura |
| **2026-05-03** | Un ejecutable de CopperTurtle (`pdfset.exe`) inyecta el RAT `PLEAD` desde `C:\Program Files\PDF24\` | Coexistencia |
| **2026-05-04** | **Al día siguiente, `GitDoor` se instala en el mismo directorio** (`pdf.exe` + `SbieDll.dll`) | Coexistencia |
| **2026-08** | **Termina la ventana de observación de Sophos** | Sophos |
| **2026-10-20** | **Sophos publica `BRONZE SANDCASTLE`**, con las versiones `1.1.5` y `1.1.7`, citando la cuenta `LatonyCharnleyaW` **sin saber qué es** | Publicación |
| **2026-11-17** | **Kaspersky publica las dos partes de `Operation ShadowCloud`**, con `GitDoor` (`1.1.6`) y `GraphDoor` (`1.2.7`), citando la misma cuenta y mencionando a Sophos sólo como «un fragmento» | Publicación |
| 2026-11-17 | Verificación propia: `ms.twnic[.]top` y `dc.cathaypacifice[.]com` ya no resuelven; `dpworldto[.]com` sigue registrado **con reenvío de correo**; los dos inquilinos de SharePoint siguen vivos (`A.5`) | Propia |

## O-6. Hipótesis alternativas consideradas

El hecho que más admite lecturas distintas es la **coexistencia** de implantes de tres actores distintos en los mismos sistemas, con ventanas de un día. Kaspersky se queda, prudentemente, en «no prueba un vínculo directo». Estas son las lecturas posibles, con su probabilidad:

<!-- cti:cards -->

| Título | Texto | Etiqueta |
|---|---|---|
| H-A · Un operador, varios arsenales | El mismo equipo opera `GitDoor` y también los implantes de FamousSparrow y CopperTurtle, que usa según convenga. Explica la ventana de un día y el directorio compartido con naturalidad. **Pero exige que un solo grupo tenga acceso a tres arsenales distintos**, incluido el de dos actores con historia propia larga | `Probable · 40–55 %` |
| H-B · Un suministrador común | Un intendente digital entrega `GitDoor`/`GraphDoor` a varios clústeres, como `CTI-2026-017` documenta para `CopperDragon`. Explica el reparto sin exigir un operador único. **Pero no explica bien la ventana de un día ni el directorio idéntico**: dos clientes de un mismo proveedor no coordinan su despliegue al día | `Probable · 25–40 %` |
| H-C · Traspaso de acceso | Un grupo compromete y otro recibe el acceso, en el modelo de corredor de accesos que esta cartera documenta en `CTI-2026-025` entre Gamaredon y Turla. La ventana de un día sería el traspaso. **Encaja bien con las fechas**, y es compatible con H-B | `Probable · 20–35 %` |
| H-D · Víctima de interés común, sin relación | Tres servicios se interesan por la misma organización y coinciden sin coordinarse. **Ocurre.** Pero el directorio de preparación compartido —no sólo el sistema, el directorio— es muy difícil de explicar así | `Poco probable · 5–15 %` |
| H-E · Y la que rompería `KJ-2` | Que `BRONZE SANDCASTLE` y `ShadowCloud` compartan la cuenta de GitHub porque **un tercero vende el acceso a ese canal** como servicio, y los dos proveedores estén viendo a dos clientes distintos. Sería la única lectura que mantiene la cuenta compartida sin identidad común. **Nada en los dos informes la sugiere**, y exigiría un modelo de negocio no documentado | `Remoto · 5–10 %` |

> **Pre-mortem: ¿cómo se vería dentro de seis meses que este informe se
> equivocó?** Tres formas. (1) Sophos o Kaspersky publican que son operaciones
> distintas con un argumento que no vemos —muy probablemente de telemetría
> propia, que es lo que no tenemos—, y `KJ-2` cae. (2) Aparece una tercera
> designación de proveedor que reparte los artefactos de otra manera, y la
> reconciliación de `O-2.1` resulta ser una fusión de tres cosas en dos. (3) El
> dato geográfico de `KJ-7` aparece y sitúa ese sistema en Latinoamérica, con
> lo cual la tensión con `CTI-2026-017` se disuelve y `O-2.3` sobra. **De las
> tres, la segunda es la que más daño haría**, porque invalidaría el método del
> `Anexo D` y no sólo su aplicación.

## O-7. Indicadores y señales de alerta

| Id | Señal observable | Qué significaría | Acción |
|---|---|---|---|
| `I-1` | Que alguna fuente publique el país del sistema donde coexisten FamousSparrow y `GitDoor` en marzo de 2026 | Resuelve `KJ-7` en un sentido o en otro | **Requisito de colección abierto.** Si está fuera de Latinoamérica: abrir revisión de `CTI-2026-017` |
| `I-2` | Que se publique el identificador de la aplicación de Entra ID que Kaspersky redactó | Convertiría `KJ-4` en un indicador de dos campos en vez de uno, y permitiría buscar la aplicación en los registros de consentimiento | Vigilar publicaciones de los dos proveedores |
| `I-3` | Que cualquiera de los dos proveedores reconozca la equivalencia de `KJ-2`, o la niegue | Confirma o rompe el juicio central | Revisión inmediata del informe |
| `I-4` | Aparición de cuentas de GitHub nuevas con el patrón de `O-3.C`: nombre occidental con sufijo aleatorio, pareja de repositorios creada el mismo día, nombres de producto tecnológico genérico | Continuidad de la operación con infraestructura nueva | Actualizar `A.2`; el patrón es más duradero que los valores |
| `I-5` | Una víctima en América, de cualquier país | Cambia el foco regional del expediente y obliga a reemitir con nivel de prioridad distinto | Revisión inmediata |
| `I-6` | Aparición del modelo —canal completo sobre nube corporativa con repositorio público para órdenes y privado para resultados— en una operación no relacionada | Confirmaría el pronóstico de difusión de `E-3` y justificaría un producto propio sobre el modelo, no sobre el actor | Disparador de producto nuevo |
| `I-7` | Que `dpworldto[.]com` empiece a enviar correo, o que aparezca en una campaña de suplantación | El reenvío de correo activo verificado en `A.5` es capacidad de *phishing* sin usar. Su activación indicaría un cambio de modo de entrada | Vigilancia de dominio |

---

# NIVEL TÁCTICO
### Para: Analistas de SOC · Ingeniería de Detección · Threat Hunting · Horizonte: días–semanas

## T-1. Cadena de intrusión

<!-- cti:stages title="Tres etapas, y la primera no está documentada" dwell="next" -->

| Etapa | Título | Elementos |
|---|---|---|
| 1 | Acceso ya existente | Agente de MeshCentral legítimo ya instalado · servidor codificado a fuego en `wss://27.102.66[.]162:443/agent.ashx` · **vía de instalación desconocida: la fuente la atribuye a reutilización de una infección anterior** · ninguna vulnerabilidad explotada, ningún día cero, ninguna credencial robada documentada |
| 2 | Carga en memoria | Tres ficheros en un mismo directorio: binario legítimo firmado + DLL maliciosa homónima de una legítima + `config.ini` cifrado · descifrado con RC4+XOR (tipo 1) o XOR a secas (tipo 2) · inyección en el propio proceso · salto a la cabecera `MZ` como trampolín · resolución de API por CRC32, FNV-1 o DJB2 · comprobación de la versión del sistema para elegir entre API nativas y estándar |
| 3 | Operación sobre nube ajena | Registro de la víctima en un *issue* de GitHub o en una biblioteca de SharePoint · órdenes en ficheros con nombre de mapa de código · módulos COFF en memoria · proxy `frp` modificado o SOCKS5 sobre WebSocket de Ably · cosecha de credenciales, *cookies*, pulsaciones, pantalla y clave de WhatsApp · subida a `gofile.io` |

**Permanencia:** no publicada por ninguna de las dos fuentes. Los únicos datos temporales de permanencia disponibles son indirectos: la coexistencia con otros implantes a un día de distancia (marzo y mayo de 2026) y la ventana de observación de Sophos, de **doce meses**, sobre una operación cuya infraestructura se aprovisionó desde septiembre de 2024. **Un expediente sin dato de permanencia no permite calcular ventana de detección**, y eso es una limitación, no un detalle.

## T-2. Mapa MITRE ATT&CK

<!-- cti:matrix -->

| Táctica | ID | Técnica | Procedimiento observado |
|---|---|---|---|
| Desarrollo de recursos | T1585 | Establish Accounts | Nueve cuentas de GitHub con nombre occidental más sufijo aleatorio, creadas por lotes entre 2024-09 y 2025-12 |
| Desarrollo de recursos | T1583.001 | Acquire Infrastructure: Domains | `ekmt[.]tw` registrado el 2026-04-23; `twnic[.]top` suplanta al registro nacional de Taiwán; `cathaypacifice[.]com` y `dpworldto[.]com` suplantan marcas de aviación y de logística portuaria |
| Desarrollo de recursos | T1583.006 | Acquire Infrastructure: Web Services | Inquilino de Entra ID `8f50c589-a4d6-4df4-95bb-2fb7f5983fe5` con una aplicación registrada; dos inquilinos de SharePoint (`buildersemp`, `cskautogo`) |
| Acceso inicial | T1133 | External Remote Services | **No documentado.** El expediente arranca con el agente de MeshCentral ya presente; la fuente declara desconocida la vía de instalación |
| Ejecución | T1059.003 | Windows Command Shell | Módulo de ejecución por `cmd.exe`; consola interactiva completa con WinPTY (`winpty.dll` + `winpty-agent.exe` en `%TEMP%`, terminal 80×25) |
| Ejecución | T1106 | Native API | `NtCreateFile`, `NtReadFile`, `NtAllocateVirtualMemory`, `NtCreateThreadEx`; los módulos de inyección por APC y por tabla de retrollamadas usan llamadas al sistema directas, no la API de Windows |
| Ejecución | T1620 | Reflective Code Loading | Las dos puertas traseras se inyectan en el proceso del binario legítimo; los módulos COFF se cargan en memoria invocando su función de entrada `go` |
| Ejecución | T1053.005 | Scheduled Task/Job | Módulos `EnumTasks`, `CreateTask`, `RunTask` sobre la API COM del planificador |
| Persistencia | T1543.003 | Create or Modify System Process: Windows Service | `zoomit.exe` arrancado como servicio de Windows; módulos `CreateService`, `start_service`, `stop_service`, `DeleteService` |
| Persistencia | T1136.001 | Create Account: Local Account | Módulos `AddUser` (`NetUserAdd`) y `AddUserToGroup`, para grupos globales y locales |
| Persistencia | T1547 | Boot or Logon Autostart Execution | Fichero cerrojo `%APPDATA%\log.lock`: si existe al arrancar la puerta trasera, el registro de pulsaciones se reanuda solo |
| Escalada / Evasión | T1574.002 | Hijack Execution Flow: DLL Side-Loading | `jli.dll` con `javaw.exe`; `SbieDll.dll` con `start.exe`; `python39.dll` con una aplicación Python; `WINMM.dll` con `zoomit.exe`; `libcef.dll` |
| Evasión | T1574.013 | Hijack Execution Flow: KernelCallbackTable | Módulo de inyección por manipulación de la tabla de retrollamadas del proceso, con llamadas al sistema directas |
| Evasión | T1027 | Obfuscated Files or Information | Aplanamiento del flujo de control; envoltorios anidados de funciones auxiliares; llamadas indirectas; Base64 con alfabeto propio `ABCDEFGHIJ01234ZYXWVUTSRQPONMLKzyxwvutsrqponmlkjihgfedcba98765/+` |
| Evasión | T1027.007 | Dynamic API Resolution | Resolución por hash del nombre: CRC32 en el cargador tipo 1, FNV-1 (`FNV_prime` = `0x1000193`) en su variante, DJB2 en `GraphDoor`; nombres de biblioteca y de función descifrados con XOR de 7 bytes `\x11\xAF\xCE\xDC\xA6\x12\x05` |
| Evasión | T1027.009 | Embedded Payloads | Carga cifrada en `config.ini` junto al cargador; en una variante, el blob descifra a código de arranque **más** la puerta trasera |
| Evasión | T1036.005 | Masquerading: Match Legitimate Name or Location | `excint.exe` es un componente renombrado de Avast; `pdf.exe` y `pdfset.exe` dentro de `C:\Program Files\PDF24\`; `imzimzgo 2.2.0 x64` es Mimikatz renombrado |
| Evasión | T1036.008 | Masquerading: Masquerade File Type | Ficheros de órdenes y de datos con extensión `.js.map` (mapa de código JavaScript) y módulos con extensión `.ts` (TypeScript) |
| Evasión | T1622 | Debugger Evasion | El cargador tipo 2 instala un manejador vectorizado de excepciones y **pone a cero el registro `DR7`** para borrar los puntos de ruptura por hardware; comprueba además el nombre del proceso anfitrión |
| Evasión | T1562.004 | Impair Defenses: Disable or Modify System Firewall | Módulo `Firewall`: añade, elimina y enumera reglas de entrada y de salida |
| Evasión | T1070.004 | Indicator Removal: File Deletion | Módulos `WipeFileContent` (sobrescritura con ceros) y `DeleteDirectoryRecursively` |
| Evasión | T1140 | Deobfuscate/Decode Files or Information | Cadena completa: Base64 → XOR con el nombre del fichero como clave → Base64 → AES-256-ECB con clave aleatoria transportada en el propio JSON |
| Acceso a credenciales | T1003.001 | OS Credential Dumping: LSASS Memory | Mimikatz con `sekurlsa::logonpasswords full` |
| Acceso a credenciales | T1003.002 | OS Credential Dumping: Security Account Manager | Mimikatz con `lsadump::sam` |
| Acceso a credenciales | T1539 | Steal Web Session Cookie | CookieKatz contra Chrome, Edge y `Msedgewebview2`, **directamente de la memoria del proceso** |
| Acceso a credenciales | T1056.001 | Input Capture: Keylogging | Pulsaciones a `%APPDATA%\Microsoft\SystemCertificates\Cache\logs.dat`; plugin `kl.ts` en `GraphDoor` |
| Acceso a credenciales | T1187 | Forced Authentication | PetitPotam sobre EFSRPC: tubería `\\.\pipe\%08X\pipe\srvsvc`, UUID `df1941c5-fe89-4e79-bf10-463657acf44d`, ruta UNC `\\localhost\pipe\<8 car>\C$\hiddenfile.txt`, operación `EfsRpcOpenFileRaw`, con `winlogon.exe` como proceso padre |
| Acceso a credenciales | T1550.001 | Use Alternate Authentication Material: Application Access Token | `GraphDoor` obtiene un token con `grant_type=client_credentials` y `scope=https://graph.microsoft.com/.default`, y lo usa contra `graph.microsoft.com` |
| Descubrimiento | T1057 | Process Discovery | Plugin `pr.ts`; módulo `GetProcessUserInfo` (obtiene `SeDebugPrivilege` y consulta `explorer.exe` y `winlogon.exe`) |
| Descubrimiento | T1016 | System Network Configuration Discovery | Módulos `IPInfo` y `ARP`; IP pública consultada a `https://ip.sb/` |
| Descubrimiento | T1049 | System Network Connections Discovery | Módulo `Netstat` con información de proceso |
| Descubrimiento | T1087 | Account Discovery | Módulos `whoami` (usuario, SID, grupos, privilegios), `EnumNetUser` con cuatro modos, `ListServerGroups`, `ListServerGroupMembers` |
| Descubrimiento | T1007 | System Service Discovery | Módulo `EnumServices`: nombre, tipo, estado, ruta del binario, tipo de arranque y dependencias |
| Descubrimiento | T1012 | Query Registry | Módulo de línea de órdenes de registro, con enumeración recursiva de claves y valores |
| Recolección | T1113 | Screen Capture | Pantalla completa o ventana concreta identificada por el PID del proceso; plugin `scr.ts`, salida en JPEG |
| Recolección | T1005 | Data from Local System | Módulo `WhatsAppKey`: extrae la clave de descifrado de la base de datos de WhatsApp (PDB `C:\src\Dll1\WhatsAppCS\x64\Release\WhatKeyCPP.pdb`) |
| Mando y control | T1102.002 | Web Service: Bidirectional Communication | **El núcleo del expediente.** Repositorio público de GitHub para órdenes, privado para resultados; biblioteca de documentos de SharePoint vía Graph; canales de Ably |
| Mando y control | T1219 | Remote Access Software | MeshCentral Agent como punto de partida, con servidor codificado a fuego |
| Mando y control | T1573.001 | Encrypted Channel: Symmetric Cryptography | AES-256-ECB con clave aleatoria por mensaje; RC4; XOR con el nombre del fichero como clave |
| Mando y control | T1132.001 | Data Encoding: Standard Encoding | Base64 en dos pasadas alrededor del XOR |
| Mando y control | T1572 | Protocol Tunneling | `ab2channel.ts`: SOCKS5 encapsulado en el WebSocket compatible con Pusher de Ably |
| Mando y control | T1090 | Proxy | Cliente `frp` modificado (`Erfrp`) que lee su configuración de la memoria compartida `Local\pc<PID>`; 22 direcciones de proxy publicadas |
| Mando y control | T1105 | Ingress Tool Transfer | Módulos y plugins descargados a demanda del repositorio o de la biblioteca de documentos |
| Exfiltración | T1567.002 | Exfiltration Over Web Service: Exfiltration to Cloud Storage | Módulo `Fileupload` a `upload.gofile[.]io`; Sophos documenta además `file[.]io` |

> ⚠ **La fila que no hay que pasar por alto es `T1102.002`.** No es una técnica
> auxiliar de este expediente: es su arquitectura. Y la mayoría de las
> bibliotecas de detección la cubren con reglas que buscan **servicios de
> consumo** —Telegram, Discord, Pastebin, Dropbox— porque es donde apareció
> primero. Aquí los servicios son **corporativos y de pago**, lo que invierte
> el signo del indicador: no es «un puesto habla con un servicio raro», es «un
> puesto habla con el servicio que todos usamos, de una forma que no es la
> nuestra».

## T-3. Dónde atacamos en la Pirámide del Dolor

<!-- cti:pyramid -->

| Nivel | Descripción | Valor |
|---|---|---|
| Valores de hash | Doce hashes MD5 publicados entre las dos entregas, de cargadores, cargas cifradas y puertas traseras | **Casi nulo, y por un motivo estructural.** Las cargas se cifran con clave por muestra: cada despliegue produce un `config.ini` distinto. Los hashes de los cargadores valen más, pero son DLL pequeñas y fáciles de recompilar |
| Direcciones IP | 22 direcciones de proxy, más la del servidor de MeshCentral | **Bajo, y con riesgo.** Son proxys alquilados en una docena de proveedores distintos, y **una de ellas es casi con certeza un error de transcripción de la fuente** (`A.4`). El coste de equivocarse es mayor que el beneficio de acertar |
| Nombres de dominio | `twnic[.]top`, `ekmt[.]tw`, y los de Sophos `cathaypacifice[.]com` y `dpworldto[.]com` | **Bajo-medio.** Dos de los cuatro ya no resuelven. Útiles retrospectivamente para búsqueda en registros históricos, no para bloqueo preventivo |
| Artefactos de red | **El GUID de inquilino de Entra ID**; el esquema `main.<8>.<4>.js.<ext>` en rutas de API; la cabecera `X-CSRF-TOKEN` hacia `api.github.com`; el *User-Agent* de Chrome 122 fijo; el mensaje `commit from INSOMNIA` | **Alto, y es la anomalía de este expediente.** El GUID de inquilino tiene la especificidad de un hash y la durabilidad de una TTP: cambiarlo obliga al adversario a registrar otro inquilino, pagar otra suscripción y volver a consentir una aplicación |
| Artefactos de host | `C:\ProgramData\Intel_Log\<GUID>`; `%APPDATA%\log.lock`; `%APPDATA%\Microsoft\SystemCertificates\Cache\logs.dat`; tuberías `\\.\pipe\p<PID>` y `\\.\pipe\MyInputPipe`; memoria compartida `Local\pc<PID>`, `Local\pcs<PID>`, `Local\sm<PID>` | **Alto.** Son nombres elegidos a mano, con estructura estable entre muestras y versiones. Las tuberías y los segmentos de memoria compartida son el punto más fuerte: cambiarlos exige tocar el protocolo entre la puerta trasera y sus propios módulos |
| Herramientas | Mimikatz renombrado, CookieKatz, PetitPotam, WinPTY, cliente `frp` modificado, cargador COFF propio | **Medio-alto.** Las cuatro primeras son públicas y detectables con firmas de comportamiento maduras. El cargador COFF propio y el `frp` modificado son los que exigen trabajo |
| Tácticas, técnicas y procedimientos | Carga lateral sobre binario firmado con la carga en un `.ini` al lado · canal completo sobre nube corporativa · repositorio público para órdenes y privado para resultados · configuración de infraestructura entregada en tiempo de ejecución | **Máximo, y es donde hay que invertir.** El diseño del canal es la decisión más costosa de cambiar de toda la operación, porque es la que le da su ventaja |

> ✅ **La inversión que este expediente obliga a hacer en la pirámide.** La
> lectura ortodoxa dice que las direcciones IP son indicadores baratos y
> frágiles, y los artefactos de red algo mejor. Aquí **el artefacto de red más
> valioso del expediente —el GUID de inquilino— es más duradero que la mayoría
> de las TTP de otros actores**, porque cambiarlo tiene coste económico y
> administrativo, no sólo técnico. Y al revés: los nombres de dominio, que
> normalmente dan juego, aquí casi no aparecen, porque el canal principal no
> usa dominios propios. **No es que la pirámide falle: es que este adversario
> ha reubicado su infraestructura en un nivel distinto del habitual.**

## T-4. Hipótesis de caza prioritarias

<!-- cti:accordion critical="^(H-1|H-2|H-3)\b" regional="^H-9\b" -->

**H-1 — El inquilino ajeno de Entra ID.** Buscar, en los registros del proxy con inspección TLS o en cualquier telemetría que conserve la **ruta completa** de las peticiones a `login.microsoftonline.com`, el GUID `8f50c589-a4d6-4df4-95bb-2fb7f5983fe5`. Es la hipótesis de mayor valor del expediente: coste de falso positivo nulo, especificidad máxima. **Y la más probable que falle por falta de datos**, no por ausencia de la amenaza: muchas organizaciones registran el host de destino pero no la ruta, y sin la ruta el indicador es invisible. Si el dato no existe, la conclusión de la caza no es «no estamos comprometidos», es «no podemos saberlo», y eso va a `T-5`.

**H-2 — Ably desde donde no debe.** Buscar resoluciones DNS o conexiones a `ably.io`, `ably.net`, `rest.ably.io` y `realtime.ably.io` desde cualquier sistema que no sea un puesto de desarrollo con justificación conocida. Ably es un servicio de mensajería en tiempo real para desarrolladores de aplicaciones; su presencia en un servidor de ficheros, en un controlador de dominio o en el puesto de un administrativo no tiene explicación benigna evidente. **Es la hipótesis con mejor relación coste-beneficio del informe** (`KJ-5`), y la que sustenta la decisión `E-a`.

**H-3 — Binario firmado fuera de su sitio con su DLL al lado.** Buscar ejecuciones de binarios legítimos firmados desde rutas donde no se instalan: `start.exe`, `javaw.exe`, `pythonw.exe`, `zoomit.exe`, `bginfo64.exe`, `vmmap.exe`, `krita.exe`, `nvdahelper.exe` en `C:\Windows\System32\`, en `%ProgramData%\` o en subdirectorios de `C:\Program Files\` que no les correspondan — **y con un `config.ini` en el mismo directorio**. La combinación de las tres condiciones (binario firmado + ruta anómala + `.ini` adyacente) es la firma de carga común a las dos designaciones de proveedor, y es la más estable del expediente porque es la que el adversario repite desde 2025.

**H-4 — GitHub con credencial desde un proceso que no es de desarrollo.** Buscar peticiones a `api.github.com` que lleven cabecera `Authorization` y cuyo proceso de origen no sea `git.exe`, un cliente de integración continua, un IDE o un gestor de paquetes conocido. Es la mitad ascendente del canal de `GitDoor`, y la única que está obligada a autenticarse. Complementaria: peticiones `PUT` o `POST` a rutas `/repos/*/contents/*` y `/repos/*/issues/*` desde sistemas que no publican código.

**H-5 — Las tuberías con nombre y la memoria compartida.** Buscar objetos con los nombres `\\.\pipe\p<número>`, `\\.\pipe\MyInputPipe`, y secciones de memoria compartida `Local\pc<número>`, `Local\pcs<número>`, `Local\sm<número>`. Son nombres de protocolo interno entre la puerta trasera y sus módulos, no de comunicación externa, y por tanto **no se cambian sin romper la compatibilidad entre versiones** — el intercalado de versiones de `O-2.1` sugiere que mantienen esa compatibilidad deliberadamente.

**H-6 — El directorio `Intel_Log`.** Buscar la existencia de `C:\ProgramData\Intel_Log\` y, dentro, subdirectorios con nombre de GUID. Es creación de `GraphDoor` y el nombre está elegido para pasar por telemetría de un fabricante de procesadores. Coste de la caza: trivial. Cobertura: sólo una de las dos puertas traseras.

**H-7 — El cerrojo del registrador de pulsaciones.** Buscar el fichero `%APPDATA%\log.lock` y el fichero de salida `%APPDATA%\Microsoft\SystemCertificates\Cache\logs.dat`. El primero es un fichero vacío cuyo único propósito es que el registro de pulsaciones se reanude solo tras un reinicio; el segundo está escondido en una ruta de certificados del sistema donde nadie mira. **Un `logs.dat` en ese directorio no tiene uso legítimo conocido.**

**H-8 — WinPTY en `%TEMP%`.** Buscar `winpty.dll` y `winpty-agent.exe` en `%TEMP%` o en rutas de usuario. Son componentes legítimos de un proyecto de consola para Windows, incrustados en Base64 dentro del módulo de consola interactiva y volcados al disco en el momento de usarse. Su presencia en `%TEMP%` sin un terminal instalado que los justifique es anómala. Complementaria: la cadena fija `hklnwqxaa123`, que es la señal de terminación de esa consola y **no tiene ninguna razón para aparecer en ningún otro sitio**.

**H-9 — Coexistencia, que es la hipótesis de caza regional de este informe.** Si en algún momento aparece actividad compatible con este expediente, **buscar inmediatamente en el mismo directorio y en su directorio padre**, y en una ventana de ±48 horas, artefactos de FamousSparrow y de CopperTurtle: `excint.exe` con `wtsapi32.dll`, carga descifrada con RC4 y clave `iotrh^%4CFGTj`, `pdfset.exe` en `C:\Program Files\PDF24\`, o un RAT `PLEAD` en memoria. Es el patrón que Kaspersky documenta dos veces con un día de diferencia, **y es la única hipótesis de este informe con conexión directa con un expediente de foco latinoamericano** (`CTI-2026-017`).

**H-10 — Suplantación de marca en los registros históricos.** Buscar en los registros de DNS y de proxy, retrospectivamente y hasta donde llegue la retención, dominios que imiten a registros de Internet nacionales, a aerolíneas y a operadores portuarios: el patrón de este adversario incluye `twnic[.]top` (por TWNIC, el registro de `.tw`), `cathaypacifice[.]com` y `dpworldto[.]com`. **No es una caza de este adversario: es una caza del patrón**, y `CTI-2026-018` es el expediente que lo trata como clase.

**H-11 — `gofile.io` y `file.io` como destino de subida.** Buscar subidas a `upload.gofile[.]io` y a `file[.]io` desde sistemas corporativos. Son servicios de intercambio de ficheros anónimo y gratuito, con uso legítimo ocasional por parte de usuarios que intentan sortear límites de tamaño del correo; el ruido es real pero manejable, y el valor es que es el **único punto de exfiltración masiva documentado** del expediente.

**H-12 — El mensaje de *commit*.** Para quien tenga visibilidad del contenido de las peticiones: la cadena `commit from INSOMNIA` viaja en el cuerpo de las subidas tanto a GitHub como a SharePoint. Es un literal del adversario, no una convención de ninguna herramienta legítima, y **la misma cadena en dos protocolos distintos es el indicador más limpio de que se trata del mismo banco de trabajo** (`O-2.2`). Caza de bajo rendimiento y altísima especificidad.

## T-5. Brechas de visibilidad que hay que cerrar primero

| # | Brecha | Qué hipótesis deja ciega | Coste de cerrarla |
|---|---|---|---|
| V-1 | **No se conserva la ruta de las peticiones HTTPS a los puntos de autenticación de Microsoft** | `H-1`, que es la de mayor valor del informe. Sin la ruta, el GUID de inquilino es inobservable | Medio-alto: exige inspección TLS en los cuatro hosts de inicio de sesión de Microsoft, con las implicaciones de privacidad y de ruptura de fijación de certificado que eso arrastra |
| V-2 | **No se correlaciona proceso de origen con destino de red** | `H-4` y buena parte de `H-2`. «Alguien habló con `api.github.com`» no sirve; «`zoomit.exe` habló con `api.github.com`» es concluyente | Medio: exige telemetría de EDR con red, o correlación entre EDR y proxy |
| V-3 | **No se inventarían objetos del sistema** (tuberías con nombre, secciones de memoria compartida) | `H-5`, que es la hipótesis más duradera del expediente | Bajo si el EDR ya los recoge; alto si hay que añadirlos |
| V-4 | **No hay inventario fiable de agentes de administración remota** | `Q-1` de `O-4`, y con ella la única mitigación del vector inicial | Bajo en coste técnico, alto en coste organizativo: es un trabajo de gobierno, no de herramienta |
| V-5 | **No hay política de acceso entre inquilinos de Microsoft 365, ni visibilidad de qué inquilinos ajenos alcanzan los puestos** | La mitigación estructural de `X-5.2`, que es la única que mata la técnica de `GraphDoor` en lugar de detectarla | Alto: afecta a colaboración con terceros y requiere decisión de negocio (`E-b`) |
| V-6 | **Retención de registros de DNS y de proxy inferior a doce meses** | `H-10` y toda caza retrospectiva. La preparación de esta operación empezó hace **veintiséis meses** | Medio: es coste de almacenamiento, y la decisión es presupuestaria |

---

# NIVEL TÉCNICO
### Para: Ingeniería de detección · Automatización · TIP/SIEM · Vida útil: meses

## X-1. Arsenal y capacidad

| Componente | Naturaleza | Nota técnica decisiva |
|---|---|---|
| **MeshCentral Agent** | **Software libre legítimo** | Punto de partida, no malware. Servidor codificado a fuego. **No es un indicador de compromiso: es un indicador de inventario** |
| **Cargador tipo 1** (`jli.dll`) | Propio | Base64 con alfabeto propio → RC4 (clave de 16 bytes por muestra) → XOR (clave de 16 bytes por muestra). Luego **abusa de `RtlEthernetAddressToStringA` y `RtlEthernetStringToAddressA`** para transformar los bytes descifrados pasándolos por una representación de dirección MAC, y escribe el resultado en memoria obtenida con `AllocADsMem`. Es evasión por uso de API inesperadas, no por cifrado |
| **Cargador tipo 1, variante** (`jli.dll`) | Propio | Resolución de API por FNV-1 con `FNV_prime` constante `0x1000193` y base variable. Crea el objeto de proyección `Local\sm<PID>`. Si la carga es una DLL, **compara el hash FNV-1 de cada nombre exportado con el valor fijo `0x974C9EB`** y ejecuta el que case |
| **Cargador tipo 2** (`SbieDll_st.dll`) | Propio | Busca el patrón `\x48\x83\xC4\x68\xC3` en `KERNEL32.DLL` y `KernelBase.dll`; instala manejador vectorizado de excepciones; **pone `DR7` a cero**; verifica el nombre del proceso anfitrión; sólo entonces descifra (Base64 → XOR de 16 bytes) |
| **GitDoor** | Propio | 26 órdenes en cinco familias. Mando y control en dos repositorios de GitHub. `"client_version":"1.1.6"` |
| **GraphDoor** | Propio | Siete plugins. Mando y control en SharePoint vía Graph, autenticándose **como aplicación**. `"client_version":"1.2.7"`. **Sin dominio de mando y control embebido** |
| **Erfrp** (cliente `frp` modificado) | **Derivado de software libre** | Go. MD5 `d89b2fe0759df2d534e7a728700a6f8c`. Modificado para **no leer fichero de configuración**: la toma de `Local\pc<PID>`. Ruta de compilación `C:/Users/user/Desktop/pythonrat/proxytest/Erfrp-0.1/frpc.go` |
| **`ab2channel.ts`** | Propio | Proxy SOCKS5 sobre el WebSocket compatible con Pusher de Ably. Órdenes `socks5:open`, datos en Base64, `socks5:close` con identificador de sesión |
| **Mimikatz** (`imzimzgo 2.2.0 x64`) | **Público, renombrado** | `sekurlsa::logonpasswords full` y `lsadump::sam` |
| **CookieKatz** | **Público** | Volcado de *cookies* de Chrome, Edge y `Msedgewebview2` **de la memoria del proceso**, sin tocar la base de datos en disco ni necesitar la clave de DPAPI |
| **PetitPotam** | **Público** | Autenticación NTLM forzada por EFSRPC |
| **WinPTY** | **Público, legítimo** | Incrustado en Base64 y volcado a `%TEMP%` para montar una consola interactiva real |
| **Cobalt Strike** | **Comercial legítimo** | Beacons desplegados en máquinas ya infectadas con `GraphDoor`, con mando y control en `twnic[.]top` y `ekmt[.]tw`. **Su presencia no atribuye** |
| **30 módulos COFF propios** | Propio | Inyección (cuatro técnicas), servicios, ficheros, red, procesos, consola, tareas, registro, usuarios, pulsaciones, *cookies*, credenciales, pantalla, WhatsApp, PetitPotam |

### X-1.1 — Lo que no hay, y es la clave de la detección

**No hay exploit.** Ni un día cero, ni un día n, ni una vulnerabilidad citada en ninguna de las dos entregas primarias ni en el informe de Sophos. Tampoco hay credenciales robadas documentadas como vector, ni *phishing*, ni documento malicioso. El expediente empieza con un acceso que ya existía.

**No hay rootkit, ni driver, ni manipulación del núcleo.** Toda la evasión es de modo usuario: resolución dinámica de API, llamadas al sistema directas para esquivar los ganchos del producto de seguridad, borrado de puntos de ruptura por hardware, ofuscación del flujo de control. Es competente y convencional.

**No hay persistencia sofisticada.** Un servicio de Windows, una tarea programada, un fichero cerrojo en `%APPDATA%`. Nada de WMI, nada de COM *hijacking*, nada en el arranque.

**La consecuencia defensiva es importante y conviene decirla sin adornos:** este adversario no se vence con parches, ni con filtrado de correo, ni con controles de aplicación basados en reputación de firma —porque los binarios que ejecuta están firmados por Oracle, por Microsoft, por Sandboxie y por la Python Software Foundation—. Se vence con **inventario** (qué agentes de administración remota hay), **telemetría de proceso correlacionada con red** (quién habla con qué) e **identidad en la nube** (qué inquilinos ajenos pueden autenticarse desde nuestra red). Las tres son inversiones estructurales, no reglas.

## X-2. Artefactos de host persistentes

<!-- cti:cards -->

| Título | Texto | Etiqueta |
|---|---|---|
| `C:\ProgramData\Intel_Log\<GUID>` | Directorio creado por `GraphDoor` al arrancar, con un subdirectorio de nombre GUID aleatorio. El nombre está elegido para parecer telemetría de un fabricante de procesadores | Alta confianza |
| `%APPDATA%\log.lock` | Fichero cerrojo del registrador de pulsaciones. Si existe al arrancar la puerta trasera, el registro se reanuda automáticamente. **Es un fichero vacío con un único propósito** | Alta confianza |
| `%APPDATA%\Microsoft\SystemCertificates\Cache\logs.dat` | Salida del registrador de pulsaciones, en las dos puertas traseras. Ruta de certificados del sistema, donde nadie mira | **Máxima confianza.** Sin uso legítimo conocido |
| `config.ini` junto a un binario firmado | La carga cifrada. **Es el artefacto más repetido del expediente**: aparece en las dos designaciones de proveedor y en todas las variantes de cargador | Alta confianza en combinación |
| `\\.\pipe\p<PID>` · `\\.\pipe\MyInputPipe` | Tuberías con nombre. La primera la abre `GraphDoor` para recibir el estado de sus plugins; la segunda la crea la consola WinPTY | Alta confianza |
| `Local\pc<PID>` · `Local\pcs<PID>` · `Local\sm<PID>` | Secciones de memoria compartida: configuración del proxy, del proxy de Ably, y argumentos de shellcode. **Protocolo interno: cambiarlos rompe la compatibilidad entre versiones** | Alta confianza |
| `winpty.dll` · `winpty-agent.exe` en `%TEMP%` | Volcados desde Base64 al montar la consola interactiva | Media-alta |
| `%ProgramData%\excint\` · `C:\Program Files\PDF24\` | Los dos directorios de preparación compartidos con FamousSparrow y CopperTurtle. **No son artefactos de este malware: son el lugar donde buscar al vecino** (`H-9`) | Contexto |

## X-3. Lógica de detección prioritaria

<!-- cti:detections -->

**D-1 · CRÍTICO — Autenticación contra el inquilino de Entra ID del adversario**

```kql
// El indicador de mayor valor del expediente, y el que no esta en ninguna
// lista publicada. Requiere conservar la RUTA de la peticion, no solo el host.
// Sin inspeccion TLS en login.microsoftonline.com esto es inobservable: ver V-1.
let inquilino_adversario = "8f50c589-a4d6-4df4-95bb-2fb7f5983fe5";
CommonSecurityLog
| where DestinationHostName has_any ("login.microsoftonline.com",
                                     "login.microsoft.com",
                                     "login.windows.net",
                                     "login.live.com")
| where RequestURL contains inquilino_adversario
| project TimeGenerated, SourceIP, SourceHostName, SourceUserName,
          RequestURL, DeviceAction
| order by TimeGenerated desc
```

→ **Respuesta inmediata.** Aislar el sistema de origen. No hay escenario benigno: un flujo `client_credentials` contra un inquilino de tercero desde un puesto corporativo no tiene uso legítimo. Buscar acto seguido `C:\ProgramData\Intel_Log\` y las tuberías de `H-5` en ese sistema.

**D-2 · CRÍTICO — Binario firmado en ruta anómala con su carga cifrada al lado**

```kql
// La firma de carga comun a las DOS designaciones de proveedor, y la mas
// estable del expediente: el adversario la repite desde 2025.
// Tres condiciones; las tres juntas son concluyentes, por separado son ruido.
let anfitriones = dynamic(["start.exe","javaw.exe","javaws.exe","pythonw.exe",
                           "zoomit.exe","bginfo64.exe","vmmap.exe","krita.exe",
                           "nvdahelper.exe","jcef_helper.exe","lineappmgr.exe",
                           "sandboxiewuau.exe","dtsapo4service.exe","pdf.exe"]);
let dll_cargadas = dynamic(["jli.dll","sbiedll.dll","python39.dll","winmm.dll",
                            "libcef.dll","krita.dll","nvdahelperremote.dll",
                            "version.dll","msvcp140.dll","snmpapi.dll",
                            "wtsapi32.dll"]);
DeviceImageLoadEvents
| where tolower(FileName) in (dll_cargadas)
| extend dir = tolower(strcat(FolderPath))
| join kind=inner (
    DeviceProcessEvents
    | where tolower(FileName) in (anfitriones)
    | project DeviceId, ProcessId = ProcessId, anfitrion = FileName,
              ruta_anfitrion = tolower(FolderPath), SHA256, TimeGenerated
  ) on DeviceId
| where ruta_anfitrion has_any ("\\windows\\system32\\", "\\programdata\\",
                                "\\users\\public\\", "\\appdata\\")
      or ruta_anfitrion !has "program files"
| project TimeGenerated, DeviceName, anfitrion, ruta_anfitrion, FileName, SHA256
```

→ **Investigación prioritaria.** Comprobar si existe un `config.ini` en el mismo directorio: si existe, es la cadena completa. Recoger el `config.ini` **antes** de aislar: es la carga cifrada y es la única muestra que se va a obtener.

**D-3 · ALTO — Ably desde un sistema sin justificación de desarrollo**

```kql
// El eslabon flojo del modelo de sigilo del adversario (KJ-5) y el control
// de mejor relacion coste-beneficio del informe (E-a).
// Excluir explicitamente el parque de desarrollo antes de alertar.
let hosts_ably = dynamic(["ably.io","ably.net","rest.ably.io","realtime.ably.io",
                          "ably-realtime.com"]);
DeviceNetworkEvents
| where RemoteUrl has_any (hosts_ably)
| where DeviceName !in (_GetWatchlist("puestos_desarrollo") | project DeviceName)
| summarize intentos = count(), procesos = make_set(InitiatingProcessFileName),
            primera = min(TimeGenerated), ultima = max(TimeGenerated)
          by DeviceName, RemoteUrl
| order by intentos desc
```

→ **Alerta.** Si el proceso iniciador no es un navegador ni una herramienta de desarrollo conocida, escalar a `D-2` sobre ese mismo sistema. Ably es el canal por el que `GraphDoor` recibe la dirección de su propio proxy: encontrarlo aquí significa que la puerta trasera está operativa, no sólo instalada.

**D-4 · ALTO — GitHub con credencial desde un proceso que no publica código**

```kql
// La mitad ASCENDENTE del canal de GitDoor es la unica obligada a autenticarse
// (O-3.B). La descendente es anonima y no se distingue.
let procesos_legitimos = dynamic(["git.exe","code.exe","devenv.exe","idea64.exe",
                                  "gh.exe","npm.exe","node.exe","pip.exe",
                                  "python.exe","msbuild.exe","dotnet.exe",
                                  "curl.exe","powershell.exe"]);
DeviceNetworkEvents
| where RemoteUrl has "api.github.com"
| where InitiatingProcessFileName !in~ (procesos_legitimos)
| extend sospechoso = InitiatingProcessFileName
| summarize conexiones = count(), by DeviceName, sospechoso, InitiatingProcessFolderPath
| where conexiones > 1
```

→ **Investigación.** Un proceso que no es un cliente de desarrollo hablando con la API de GitHub de forma repetida es, por sí solo, anómalo. Si además el proceso es un binario firmado ejecutándose desde una ruta anómala, es `D-2` y la respuesta es inmediata.

**D-5 · ALTO — El fichero de salida del registrador de pulsaciones**

```yaml
title: ShadowCloud - salida del registrador de pulsaciones en ruta de certificados
id: 7a2f1c84-3d9e-4b61-9f20-1c6e8a4b55d2
status: experimental
description: >
  Crea o modifica %APPDATA%\Microsoft\SystemCertificates\Cache\logs.dat, ruta
  usada por GitDoor y por el plugin kl.ts de GraphDoor. No se conoce uso
  legitimo de un fichero logs.dat en el almacen de certificados del usuario.
references:
  - https://securelist.com/operation-shadowcloud-gitdoor/122004/
  - https://securelist.com/operation-shadowcloud-graphdoor/122005/
logsource:
  category: file_event
  product: windows
detection:
  seleccion:
    TargetFilename|endswith: '\Microsoft\SystemCertificates\Cache\logs.dat'
  cerrojo:
    TargetFilename|endswith: '\AppData\Roaming\log.lock'
  condition: seleccion or cerrojo
falsepositives:
  - Ninguno conocido para logs.dat en esa ruta.
  - log.lock es un nombre generico: verificar que el fichero este vacio.
level: high
```

→ **Investigación prioritaria.** `logs.dat` en esa ruta es concluyente. `log.lock` por sí solo es más débil —el nombre es genérico— pero si está vacío y acompaña a cualquier otro indicador del expediente, confirma que el registro de pulsaciones está configurado para reanudarse tras reinicio.

**D-6 · MEDIO — Tuberías con nombre y memoria compartida del protocolo interno**

```yaml
title: ShadowCloud - objetos del protocolo interno entre puerta trasera y modulos
id: c41b8e07-5a2d-4f93-8e17-93b0d2f7a6c1
status: experimental
description: >
  Tuberias con nombre y secciones de memoria compartida que GitDoor y GraphDoor
  usan para hablar con sus propios modulos. Al ser protocolo interno entre
  versiones, son mas estables que cualquier indicador de red del expediente.
logsource:
  category: pipe_created
  product: windows
detection:
  tuberia_graphdoor:
    PipeName|re: '^\\\\\.\\pipe\\p[0-9]{2,6}$'
  tuberia_winpty:
    PipeName|endswith: '\MyInputPipe'
  tuberia_petitpotam:
    PipeName|re: '\\pipe\\[0-9A-F]{8}\\pipe\\srvsvc$'
  condition: tuberia_graphdoor or tuberia_winpty or tuberia_petitpotam
falsepositives:
  - El patron p<numero> puede casar con software legitimo: correlacionar
    siempre con el proceso creador antes de alertar.
level: medium
```

→ **Correlación.** Ninguna de las tres por sí sola justifica una respuesta. `MyInputPipe` y la tubería de PetitPotam son mucho más específicas que la primera. **La de PetitPotam es, además, un indicador de movimiento lateral inminente**, no de presencia: si aparece, hay una autenticación NTLM forzada en curso.

**D-7 · MEDIO — El literal del banco de trabajo del adversario**

```kql
// Caza de bajisimo rendimiento y altisima especificidad (H-12).
// Requiere visibilidad del CUERPO de las peticiones: solo util con proxy
// que registre payloads, o en analisis forense de captura de red.
search "commit from INSOMNIA" or "hklnwqxaa123" or "imzimzgo"
| project TimeGenerated, Type, Computer, $table
```

→ **Confirmación, no detección.** Estos tres literales no van a aparecer en telemetría normal de red. Sirven para confirmar un caso ya sospechoso y, sobre todo, para búsqueda retrospectiva en capturas guardadas. `commit from INSOMNIA` viaja tanto hacia GitHub como hacia SharePoint, y es la prueba de banco de trabajo común de `O-2.2`.

## X-4. Consultas de caza

```powershell
# H-1 y Q-1 · Inventario de agentes de administracion remota.
# Esta es la consulta que corresponde al vector inicial documentado, y es la
# unica mitigacion de vector inicial que este expediente permite recomendar.
# No busca malware: busca software legitimo que nadie recuerda haber aprobado.

$sospechosos = @(
    'MeshAgent','Mesh Agent','MeshCentral',
    'AnyDesk','Atera','ScreenConnect','ConnectWise','eHorus','N-able',
    'BeyondTrust','SimpleHelp','Splashtop','TeamViewer','RustDesk','Tactical RMM'
)

# 1. Servicios instalados
Get-CimInstance Win32_Service |
  Where-Object { $n = $_.Name + $_.DisplayName + $_.PathName
                 $sospechosos | Where-Object { $n -match [regex]::Escape($_) } } |
  Select-Object Name, DisplayName, State, StartMode, PathName

# 2. Software registrado
Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*',
                 'HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*' |
  Where-Object { $d = $_.DisplayName
                 $d -and ($sospechosos | Where-Object { $d -match [regex]::Escape($_) }) } |
  Select-Object DisplayName, Publisher, InstallDate, InstallLocation

# 3. LA PREGUNTA QUE IMPORTA, y que ningun escaner responde:
#    para cada agente encontrado, contra que servidor habla.
#    En MeshCentral la URL del servidor esta en el .msh junto al ejecutable.
Get-ChildItem -Path C:\ -Filter '*.msh' -Recurse -ErrorAction SilentlyContinue |
  ForEach-Object {
      [pscustomobject]@{
          Fichero = $_.FullName
          Servidor = (Select-String -Path $_.FullName -Pattern 'MeshServer=|ServerID=').Line
      }
  }

# Y LAS TRES PREGUNTAS DE E-2, que no las responde PowerShell:
#   1. Quien autorizo este agente, y sigue trabajando aqui?
#   2. El servidor contra el que habla, es nuestro o de un tercero?
#   3. El proyecto que lo trajo, termino? Si termino, por que sigue instalado?
```

```powershell
# H-3 y D-2 · Binario firmado en ruta anomala con su carga cifrada al lado.
# Las TRES condiciones juntas. Por separado cada una es ruido.

$pares = @{
    'start.exe'          = 'SbieDll.dll'
    'javaw.exe'          = 'jli.dll'
    'pythonw.exe'        = 'python39.dll'
    'zoomit.exe'         = 'WINMM.dll'
    'jcef_helper.exe'    = 'libcef.dll'
    'bginfo64.exe'       = 'snmpapi.dll'
    'vmmap.exe'          = 'version.dll'
    'krita.exe'          = 'krita.dll'
    'excint.exe'         = 'wtsapi32.dll'   # FamousSparrow, H-9
}

$rutas = @("$env:SystemRoot\System32", "$env:ProgramData", 'C:\Program Files',
           'C:\Program Files (x86)', "$env:Public")

foreach ($raiz in $rutas) {
    Get-ChildItem -Path $raiz -Include $pares.Keys -Recurse -File -ErrorAction SilentlyContinue |
      ForEach-Object {
          $dir = $_.DirectoryName
          $dll = $pares[$_.Name]
          $hay_dll = Test-Path (Join-Path $dir $dll)
          $hay_ini = Test-Path (Join-Path $dir 'config.ini')
          if ($hay_dll -and $hay_ini) {
              [pscustomobject]@{
                  Veredicto = 'CADENA COMPLETA — recoger config.ini ANTES de aislar'
                  Anfitrion = $_.FullName
                  Firma     = (Get-AuthenticodeSignature $_.FullName).Status
                  DLL       = Join-Path $dir $dll
                  Carga     = Join-Path $dir 'config.ini'
              }
          }
          elseif ($hay_dll) {
              [pscustomobject]@{
                  Veredicto = 'Par de carga lateral sin carga visible — investigar'
                  Anfitrion = $_.FullName
                  Firma     = (Get-AuthenticodeSignature $_.FullName).Status
                  DLL       = Join-Path $dir $dll
                  Carga     = '(ausente)'
              }
          }
      }
}

# AVISO: la firma del anfitrion sera VALIDA. Esta cadena no falsifica firmas:
# abusa de binarios legitimamente firmados por Oracle, Microsoft, Sandboxie y
# la Python Software Foundation. Un control de aplicaciones basado en
# reputacion de firma NO ve nada de esto.
```

```powershell
# H-5, H-6 y H-7 · Artefactos de host, barrido rapido.
# Coste trivial, cobertura alta, y sirve como triaje de un sistema sospechoso.

# Directorio de GraphDoor
if (Test-Path "$env:ProgramData\Intel_Log") {
    Write-Warning "Intel_Log presente — GraphDoor"
    Get-ChildItem "$env:ProgramData\Intel_Log" -Directory
}

# Cerrojo y salida del registrador de pulsaciones
$kl = @(
    "$env:APPDATA\log.lock",
    "$env:APPDATA\Microsoft\SystemCertificates\Cache\logs.dat"
)
$kl | Where-Object { Test-Path $_ } | ForEach-Object {
    [pscustomobject]@{ Fichero = $_; Tamano = (Get-Item $_).Length
                       Nota = 'logs.dat en esta ruta NO tiene uso legitimo conocido' }
}

# WinPTY volcado a TEMP
Get-ChildItem $env:TEMP -Include 'winpty.dll','winpty-agent.exe' -ErrorAction SilentlyContinue

# Tuberias con nombre activas
[System.IO.Directory]::GetFiles('\\.\pipe\') |
  Where-Object { $_ -match '\\p\d{2,6}$' -or $_ -match 'MyInputPipe' }
```

## X-5. Mitigaciones de configuración con efecto directo

**X-5.1 — Inventario y retirada de agentes de administración remota.** Es la única mitigación del vector inicial que el expediente permite formular, y no es técnica. La regla operativa que funciona: **un agente de administración remota sin propietario nombrado y sin servidor verificado se desinstala, no se documenta.** La consulta de `X-4` encuentra los agentes; las tres preguntas de `E-2` deciden qué hacer con cada uno.

**X-5.2 — Restricciones de inquilino, con una salvedad que hay que verificar antes de prometer nada.** Microsoft ofrece *tenant restrictions v2*, que se aplican inyectando la cabecera `sec-Restrict-Tenant-Access-Policy` con el valor `<IdInquilino>:<GuidPolítica>` en el tráfico hacia `login.microsoftonline.com`, `login.microsoft.com`, `login.windows.net` y `login.live.com`. En el caso de `GraphDoor` esto sería exactamente la mitigación estructural: el implante se autentica contra un inquilino ajeno, y una política que restrinja los inquilinos permitidos lo cortaría en el plano de autenticación.

> ⚠ **La salvedad, y no es menor.** La documentación pública describe la
> aplicación de la política sobre el **plano de autenticación** y requiere
> inspección TLS de los puntos de inicio de sesión para poder inyectar la
> cabecera. **No hemos localizado documentación que confirme que la política
> alcance a un flujo `client_credentials` de un principal de servicio**, que es
> precisamente el que `GraphDoor` usa; y la cobertura del plano de datos de
> Microsoft Graph se describe asociada a la opción de Global Secure Access, no
> a la inyección de cabecera por proxy. **Antes de presentar esto como
> mitigación hay que probarlo en el entorno propio**, con una aplicación de
> prueba en un inquilino ajeno. Presentar un control no verificado como
> resuelto es peor que no tenerlo.

**X-5.3 — Conservar la ruta de las peticiones de autenticación.** Sin esto, `D-1` —el indicador de mayor valor del expediente— es inobservable, y lo mismo le ocurrirá a cualquier indicador futuro del mismo tipo. Es la brecha `V-1`, tiene coste real en privacidad y en gestión de certificados, y la decisión no es del SOC.

**X-5.4 — Tratamiento diferenciado de los tres servicios de nube.** No todos merecen la misma política, y tratarlos igual produce o bien un corte autoinfligido o bien una falsa sensación de cobertura:

| Servicio | Política recomendada | Por qué |
|---|---|---|
| **GitHub** (`api.github.com`) | **No bloquear.** Vigilar por proceso de origen y por cabecera de autorización (`D-4`) | Imprescindible en cualquier organización que desarrolle. El bloqueo rompe la integración continua, los gestores de paquetes y los IDE |
| **Microsoft Graph** (`graph.microsoft.com`) | **No bloquear.** Controlar por inquilino, no por destino (`X-5.2`) | Es el plano de datos de Microsoft 365 entero |
| **Ably** (`ably.io`, `ably.net`) | **Alerta, y bloqueo tras evaluar el ruido** en el parque que no sea de desarrollo | Sin uso corporativo plausible fuera del desarrollo de aplicaciones en tiempo real. **Es el eslabón flojo** (`KJ-5`) |
| **`gofile.io`, `file.io`** | **Bloqueo**, salvo excepción documentada | Intercambio de ficheros anónimo. El uso legítimo existe pero tiene alternativas corporativas |
| **`ip.sb`** | **Alerta.** No bloquear por sí solo | Servicio de consulta de IP pública. Usado por la orden `publicip`, pero también por software legítimo |

**X-5.5 — Y la mitigación que no es de configuración: no cargar el Anexo A en bloqueo automático.** Está desarrollada en `A.4` y es el motivo del marcado `PAP:AMBER` de este informe.

---

## 14. Brechas de inteligencia y nuevos requisitos de colección

| Id | Brecha | Por qué importa | Cómo se cerraría |
|---|---|---|---|
| `G-1` | **El vector de acceso inicial es desconocido**, y lo declara la fuente | Sin él no hay mitigación preventiva que recomendar, sólo detección posterior. Es la brecha más importante del expediente | Publicación de cualquiera de los dos proveedores sobre cómo se instaló el agente de MeshCentral, o un caso nuevo con la cadena completa |
| `G-2` | **El identificador de la aplicación de Entra ID está redactado** | Con él, `D-1` pasaría de un campo a dos y se podría buscar la aplicación en los registros de consentimiento y de principales de servicio | Petición al proveedor, o publicación de un tercero que obtenga la muestra |
| `G-3` | **Ninguna de las dos fuentes publica recuento de víctimas ni dato de permanencia** | Sin permanencia no se puede calcular ventana de detección, que es la métrica que convierte un informe en un objetivo de programa | Informes de respuesta a incidentes de las víctimas, improbables en este sector |
| `G-4` | **El país del sistema donde coexisten FamousSparrow y `GitDoor` no está publicado** | Es `KJ-7` e `I-1`, y decide si `CTI-2026-017` necesita revisión | Publicación de Kaspersky con desglose geográfico, o pregunta directa a la fuente |
| `G-5` | **La naturaleza de los dos inquilinos de SharePoint es desconocida**: no se sabe si son del adversario o de terceros comprometidos | Cambia por completo el tratamiento: si son víctimas, hay notificación que hacer; si son del adversario, son indicador puro | Verificación con Microsoft, o publicación que lo aclare. **Los dos siguen vivos a 2026-11-17** (`A.5`) |
| `G-6` | **No hay corroboración independiente de `KJ-2`** | Es el juicio central y es nuestro | Que cualquiera de los dos proveedores, o un tercero, publique la equivalencia. Es `I-3` |
| `G-7` | **El informe de indicadores en CSV de SophosLabs no se ha procesado** | Contiene los hashes y direcciones del lado de Sophos, que permitirían ampliar el Anexo A y comprobar si hay solapamiento directo de muestras con Kaspersky — lo que elevaría `KJ-2` a *casi con certeza* | Descargar y cruzar `BRONZESANDCASTLE_Meterpreter_IOCs.csv`. **Es la tarea de colección más barata y de mayor retorno de esta lista** |

---

# ANEXOS

## Anexo A — Indicadores de compromiso

> ⚠ **`PAP:AMBER` — acción permitida individual.** Cada indicador lleva su
> acción. **Tres advertencias antes de usar este anexo:** (1) `A.4` contiene una
> dirección IP que casi con certeza es un error tipográfico de la fuente
> primaria y que apunta a una organización ajena al expediente; (2) los
> servicios legítimos de `A.6` **no son maliciosos** y se consignan con tipo
> `servicio` para que no entren en los agregados planos; (3) las cargas
> cifradas se cifran con clave por muestra, de modo que **sus hashes no son
> reutilizables entre despliegues**.

### A.1 — El indicador que no está en ninguna lista publicada · **leer primero**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| appid | `8f50c589-a4d6-4df4-95bb-2fb7f5983fe5` | **GUID del inquilino de Entra ID contra el que `GraphDoor` se autentica como aplicación.** Kaspersky redactó el identificador de cliente y el secreto, pero el GUID quedó visible en la ruta de la petición de token (`POST /8f50c589-…/oauth2/v2.0/token`). **No figura en su sección de indicadores, ni en la cobertura secundaria, ni en ninguna otra fuente que hayamos podido localizar.** Es `KJ-4` | **Alta** | Sin caducidad mientras el inquilino exista; el adversario puede registrar otro, y entonces caduca de golpe | **Detección y alerta inmediata** (`D-1`). Coste de falso positivo nulo: un flujo `client_credentials` contra un inquilino de tercero desde un puesto corporativo no tiene uso legítimo |
| pattern | `grant_type=client_credentials` con `scope=https://graph.microsoft.com/.default` originado en un **puesto de usuario** | Un endpoint de usuario no se autentica como aplicación. El patrón es más duradero que el GUID concreto | Media-alta | Sin caducidad como método | **Caza** (`H-1`) |
| appid | *(redactado por la fuente)* — identificador de cliente y secreto de la aplicación maliciosa | **Brecha de colección `G-2`.** Con estos dos valores, `D-1` pasaría de un campo a dos y permitiría buscar la aplicación en los registros de consentimiento y de principales de servicio | — | — | **Requisito de colección abierto** (`I-2`) |

### A.2 — Identidades e infraestructura de cuentas

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| url | `github[.]com/LatonyCharnleyaW` — repositorios `Havo` (descarga, público) y `Trix` (subida, privado) | **La cuenta que citan los dos proveedores, y la base de `KJ-2`.** Ya retirada por GitHub | Alta | Retirada; valor retrospectivo | **Búsqueda retrospectiva** en registros de proxy |
| url | `github[.]com/StevenDFournier` (`spaceJS`) · `github[.]com/JeneLeo` (`silverPot`/`laughbot`) · `github[.]com/VenoraKlanimU` (`logdata`/`appdb`) · `github[.]com/AlexandaJazzmynwC` (`PulseHub`/`QuantumVault`) · `github[.]com/FloraineSuvitC` (`NexaCore`/`DataFlowX`) · `github[.]com/bvgarciajocelynxccZ` (`DataSphere`/`CodeForge`) · `github[.]com/Eclemensadolph1n` (`DataCore`/`alpha`) · `github[.]com/aYulysseserinYtas` (`Solix`/`Zephyr`) | Las ocho cuentas restantes del conjunto, creadas entre 2024-09-03 y 2025-12-05. **La fecha de la primera fija el comienzo real de la preparación** (`O-5`) | Alta | **Caducidad corta**: el recambio está en el diseño (`I-4`) | **Búsqueda retrospectiva.** No bloquear `github.com` |
| email | `steve***@outlook.com` · `Jenevie***@yahoo.com` · `Venora***@yahoo.com` · `Alexanda***@yahoo.com` · `Floraine***@yahoo.com` · `bvgarcia***@yahoo.com` · `Eclemen***@yahoo.com` · `aYulysses***@yahoo.com` | **Parcialmente ocultadas por la fuente.** Se consignan por el patrón, no por el valor: el nombre de la cuenta deriva del nombre del correo, con sufijo aleatorio añadido | Media | Sin caducidad como patrón | **Contexto de atribución.** No utilizable como indicador operativo |
| pattern | Cuenta de GitHub con **nombre de persona occidental más sufijo alfanumérico aleatorio** (`...aW`, `...wC`, `...xccZ`, `...1n`, `...Ytas`), **pareja de repositorios creada el mismo día**, con nombres de producto tecnológico genérico | **Más duradero que cualquiera de los valores anteriores.** Es la huella del aprovisionamiento automatizado descrito en `O-3.C` | Media-alta | Sin caducidad como método | **Caza** (`I-4`) |

### A.3 — Artefactos de host y muestras

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| path | `C:\ProgramData\Intel_Log\<GUID>` | Directorio creado por `GraphDoor`. Nombre elegido para parecer telemetría de un fabricante de procesadores | Alta | Sin caducidad | **Detección** (`H-6`) |
| filepath | `%APPDATA%\Microsoft\SystemCertificates\Cache\logs.dat` | Salida del registrador de pulsaciones en las dos puertas traseras. **Sin uso legítimo conocido en esa ruta** | **Alta** | Sin caducidad | **Detección** (`D-5`) |
| filepath | `%APPDATA%\log.lock` | Fichero cerrojo vacío: su existencia hace que el registro de pulsaciones se reanude tras reinicio | Media | Sin caducidad | **Detección con correlación**: el nombre es genérico |
| mutex | `\\.\pipe\p<PID>` · `\\.\pipe\MyInputPipe` · `\\.\pipe\<8 hex>\pipe\srvsvc` | Tuberías con nombre: protocolo interno de `GraphDoor`, consola WinPTY y PetitPotam respectivamente. **La tercera indica movimiento lateral en curso** | Alta | Sin caducidad | **Detección** (`D-6`) |
| mutex | `Local\pc<PID>` · `Local\pcs<PID>` · `Local\sm<PID>` | Secciones de memoria compartida: configuración del proxy, del proxy de Ably y argumentos de shellcode. **Cambiarlos rompe la compatibilidad entre versiones** | Alta | Sin caducidad | **Detección** (`H-5`) |
| filename | `config.ini` junto a un binario firmado en ruta anómala | **El artefacto más repetido del expediente**, presente en las dos designaciones de proveedor | Alta **sólo en combinación** | Sin caducidad | **Detección combinada** (`D-2`). Por sí solo es ruido puro |
| herramienta | `74b025084026d8d9a64661bf995d835b` | MeshCentral Agent. **Software legítimo**: la muestra concreta usada, no el producto | Alta | Sin caducidad | **Detección con verificación.** No bloquear MeshCentral como producto |
| md5 | `32151547d912488ac5242731057170a3` · `e9d4081fac4a5111e6856f333d490439` | Cargadores tipo 1 (`jli.dll`) | Alta | 2027-05-17 | **Bloqueo** |
| md5 | `e63ec733393e4e7e3424cbff918003a3` | Cargador tipo 2 (`SbieDll_st.dll`) | Alta | 2027-05-17 | **Bloqueo** |
| md5 | `552f0a9cc5fc3755721fa49be05e8035` | **GitDoor** | Alta | 2027-05-17 | **Bloqueo** |
| md5 | `14ec33ea808e697870d00c5e434c2952` | **GraphDoor** | Alta | 2027-05-17 | **Bloqueo** |
| md5 | `d89b2fe0759df2d534e7a728700a6f8c` | Cliente `frp` modificado (`Erfrp`), en Go | Alta | 2027-05-17 | **Bloqueo** |
| md5 | `3896d44bc6d517291c60ee3f70543a31` · `b930fb3ab14fe45b378d5acfa6e0a763` · `6a54f8008ee659b6923abf5dba2b2cc1` | Cargas cifradas (`config.ini`). **Advertencia: cifradas con clave por muestra.** Cada despliegue produce un hash distinto, así que estos tres valen para los casos observados y para nada más | Alta para la muestra; **nula como clase** | 2027-05-17 | **Bloqueo, sin expectativa de cobertura** |
| herramienta | `8b78ef5609d942036e93721d75bd1f29` (`javaw.exe`) · `be739a7036dc8e2ee8608fba13c8c3a4` (`start.exe`) · `84802caf2579cfe7a38f079a64a3cd22` (`pythonw.exe`) · `d955d03104f988582cbd2967177693d3` (`zoomit.exe`) | **Binarios legítimos firmados** usados como anfitriones de carga lateral | Alta como anfitrión; **no son maliciosos** | Sin caducidad | **NO bloquear.** Vigilar su ejecución **desde rutas anómalas** (`D-2`) |
| clave | RC4 de 16 bytes y XOR de 16 bytes, **variables por muestra** · XOR de 7 bytes `\x11\xAF\xCE\xDC\xA6\x12\x05` (resolución de API) · alfabeto Base64 propio `ABCDEFGHIJ01234ZYXWVUTSRQPONMLKzyxwvutsrqponmlkjihgfedcba98765/+` | **Las dos últimas sí son fijas y por tanto utilizables.** El alfabeto Base64 propio es especialmente útil: es una cadena de 64 caracteres buscable en memoria y en muestras | Alta | Sin caducidad | **Firma de memoria y de fichero** |
| pattern | `\x48\x83\xC4\x68\xC3` buscado en `KERNEL32.DLL` y `KernelBase.dll` · puesta a cero de `CONTEXT.DR7` · hash FNV-1 de exportación comparado con `0x974C9EB` | Comprobaciones antianálisis del cargador tipo 2 y de la variante del tipo 1 | Alta | Sin caducidad | **Firma de comportamiento** |
| useragent | `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.96 Safari/537.36` | *User-Agent* **fijo** de las dos puertas traseras. Chrome 122 es de principios de 2024: **queda cada mes más desfasado respecto al parque real**, y eso lo hace progresivamente más detectable | Media-alta | **Mejora con el tiempo** | **Caza por anomalía de versión** |
| pattern | `commit from INSOMNIA` · `hklnwqxaa123` · `imzimzgo` | Literales del adversario. El primero viaja **tanto a GitHub como a SharePoint** y es la prueba de banco de trabajo común (`O-2.2`) | Alta | Sin caducidad | **Confirmación** (`D-7`), no detección |
| path | `C:/Users/user/Desktop/pythonrat/proxytest/Erfrp-0.1/frpc.go` · `C:\src\Dll1\WhatsAppCS\x64\Release\WhatKeyCPP.pdb` | Rutas de compilación. **No son indicadores operativos**: son material de atribución | Alta | Sin caducidad | **Contexto de atribución** |

### A.4 — Red · **leer esta advertencia antes de bloquear nada**

> ⚠ **`38.52.17[.]113` casi con certeza no pertenece a este expediente.** La
> lista de proxys publicada por Kaspersky incluye, en filas consecutivas,
> `38.54.17[.]113` —atribuida a `AS 154177 (LIGHT NODE LIMITED)`— y
> `38.52.17[.]113`, atribuida a `AS 33152 (Kit Carson Electric Cooperative,
> Inc)`, que es una **cooperativa eléctrica rural de Estados Unidos**. Las dos
> direcciones difieren en un dígito, aparecen seguidas, y la segunda apunta a
> una organización sin ninguna relación plausible con una operación de
> espionaje asiática. **Valoramos *probable* (55–80 %) que sea una
> transposición tipográfica de la primera en el informe de origen.** Cargarla
> en bloqueo automático es exactamente el corte autoinfligido contra el que
> advierte la portada de este repositorio, y además dirigido contra un
> operador de servicio esencial. **Se consigna con acción «verificación previa
> obligatoria» y no entra en los agregados planos.**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| ipv4:puerto | `27.102.66[.]162:443` | **Servidor del agente de MeshCentral** (`wss://27.102.66[.]162:443/agent.ashx`). Es el punto de partida del expediente | Alta | 2027-05-17 | **Bloqueo** |
| domain | `twnic[.]top` · `ms.twnic[.]top` | Mando y control de Cobalt Strike, en máquinas ya infectadas con `GraphDoor`. **Suplanta a TWNIC**, el registro nacional de dominios de Taiwán. `ms.twnic[.]top` ya no resuelve (`A.5`) | Alta | 2027-05-17 | **Bloqueo** |
| domain | `ekmt[.]tw` | Mando y control de Cobalt Strike. **Registrado el 2026-04-23** (verificación propia, `A.5`): es del adversario, no un dominio taiwanés legítimo comprometido | Alta | 2027-05-17 | **Bloqueo** |
| domain | `cathaypacifice[.]com` · `dc.cathaypacifice[.]com` | Mando y control de la versión `1.1.5` (Sophos). **Suplanta a Cathay Pacific.** Ya no resuelve | Alta | Retirado; valor retrospectivo | **Bloqueo** y búsqueda retrospectiva |
| domain | `dpworldto[.]com` · `net.dpworldto[.]com` | Mando y control de la versión `1.1.5` (Sophos). **Suplanta a DP World.** Sigue registrado y **con reenvío de correo configurado** (`A.5`): capacidad de *phishing* sin usar (`I-7`) | Alta | 2027-05-17 | **Bloqueo** y vigilancia |
| ipv4 | `103.106.230[.]33` (→ `ms.twnic[.]top`, AS 136258) · `123.58.205[.]105` (→ `ekmt[.]tw`, AS 135377) | Proxys que además resuelven a los dominios de Cobalt Strike. **Credenciales de proxy publicadas: `google` / `1qaz2wsx-pl` en los dos** | Alta | 2027-05-17 | **Bloqueo** |
| ipv4 | `104.194.154[.]28` · `104.194.152[.]173` · `104.194.153[.]161` · `172.86.66[.]19` · `153.75.94[.]148` · `153.75.95[.]27` · `45.59.124[.]164` (AS 14956, RouterHosting LLC) | Siete proxys en un mismo proveedor. **La concentración es el dato**: un único proveedor aloja un tercio de la infraestructura de tránsito | Alta | 2027-05-17 | **Bloqueo** |
| ipv4 | `216.73.158[.]72` · `216.73.158[.]117` · `103.214.68[.]20` (AS 53724, EXTRAVM LLC) | Proxys. Credenciales publicadas: `abc`/`abc`, `aaa`/`zzljq6Qj` | Alta | 2027-05-17 | **Bloqueo** |
| ipv4 | `122.147.252[.]16` (AS 9919, New Century InfoComm, **Taiwán**) | Proxy alojado en un operador taiwanés. **Encaja con el eje de victimología**: tránsito desde dentro del país objetivo | Alta | 2027-05-17 | **Bloqueo** |
| ipv4 | `223.165.4[.]203` (AS 136258) · `216.146.25[.]173` (AS 63018) · `103.137.63[.]39` (AS 131642) · `103.227.224[.]189` (AS 148996) · `66.42.52[.]137` (AS 20473) · `154.205.154[.]209` · `38.54.17[.]113` (AS 154177) · `43.134.62[.]111` (AS 132203, Tencent) | Resto de proxys publicados. Credenciales publicadas, entre otras: `admin123`/`1qaz@WSX!@#`, `xyz`/`abc`, `whatfuck`/`BQdTQYer123123`, `user`/`IKtxbUi7`, `abc`/`rrVa8mhb` | Alta | 2027-05-17 | **Bloqueo** |
| artefacto | `38.52.17[.]113` (AS 33152, Kit Carson Electric Cooperative) — **consignada con tipo `artefacto`, no `ipv4`, precisamente para que no entre en los agregados planos** | **CASI CON CERTEZA UN ERROR TIPOGRÁFICO DE LA FUENTE.** Difiere en un dígito de `38.54.17[.]113`, aparece en la fila siguiente, y apunta a una cooperativa eléctrica rural estadounidense. Léase la advertencia de encabezado | **Baja como indicador** | — | **NO BLOQUEAR. Verificación previa obligatoria.** No entra en los agregados planos |
| pattern | Contraseñas de proxy con teclado en secuencia: `1qaz2wsx-pl`, `1qaz@WSX!@#` | Patrón de contraseñas reutilizado. **Útil para pivotar** sobre otra infraestructura del mismo operador | Media | Sin caducidad | **Contexto / pivote** |

### A.5 — Verificación propia de dominios e inquilinos · **ejecutada el 2026-11-17**

> **Esto no es material de la fuente.** Son consultas de resolución y de
> registro hechas por esta célula el día de emisión, y se declaran como
> propias. Ninguna requirió interacción con infraestructura del adversario más
> allá de DNS y WHOIS públicos.

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| domain | `ekmt[.]tw` | **Registrado el 2026-04-23 11:22:24 (UTC+8), expira 2026→2028-04-23, estado `clientTransferProhibited`.** Resuelve hoy a `104.21.82[.]112` y `172.67.200[.]174`, que son de Cloudflare. **Conclusión: dominio del adversario, registrado durante la ventana de observación de Sophos, y hoy tras una red de distribución** | **Alta (verificación propia)** | — | **Contexto.** Confirma aprovisionamiento activo en abril de 2026 |
| domain | `twnic[.]top` | Resuelve a `172.67.137[.]148` y `104.21.64[.]231` (Cloudflare). **El subdominio operativo `ms.twnic[.]top` está en `NXDOMAIN`**: retirado | Alta (propia) | — | **Contexto** |
| domain | `cathaypacifice[.]com` | **`NXDOMAIN`.** Retirado tras la publicación de Sophos | Alta (propia) | — | **Contexto** |
| domain | `dpworldto[.]com` | **Sigue registrado, con registros MX de reenvío** (`eforward1.registrar-servers.com`, `eforward2...`). Es decir: **tiene correo configurado, no sólo mando y control**. Es `I-7` | Alta (propia) | — | **Vigilancia prioritaria** |
| servicio | `buildersemp[.]sharepoint[.]com` · `cskautogo[.]sharepoint[.]com` | **Los dos inquilinos de SharePoint siguen resolviendo** a granjas activas de Microsoft 365 (`dprodmgd105`). **No se puede determinar si son del adversario o de terceros comprometidos**, y eso es la brecha `G-5`: si son terceros, hay notificación pendiente que nadie ha hecho | Alta para la resolución; **nula para la naturaleza** | — | **No bloquear `*.sharepoint.com`.** Vigilar estos dos nombres en rutas de peticiones a Graph |
| artefacto | Patrón de suplantación de marca: **TWNIC** (registro nacional de Internet), **Cathay Pacific** (aviación), **DP World** (logística portuaria) | **Observación propia.** Los tres dominios de mando y control con marca reconocible imitan gobernanza de Internet, aviación y logística marítima. Sugiere un interés de objetivos **más amplio que el sector gobierno observado**, pero es lectura nuestra y no está corroborada | **Media (inferencia propia)** | Sin caducidad | **Hipótesis de caza** (`H-10`) y material para `CTI-2026-018` |

### A.6 — Servicios legítimos de terceros · **no son maliciosos**

> ⚠ **Tipo `servicio` deliberado.** Estas entradas **no** se vuelcan a
> `ioc_ipv4.txt` ni a `ioc_url.txt`. Bloquear cualquiera de las tres primeras
> por este informe produciría un corte propio mayor que el riesgo que mitiga.
> La política diferenciada está en `X-5.4`.

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| servicio | `api.github[.]com` · `github[.]com` | Canal de órdenes y de resultados de `GitDoor`. **Servicio imprescindible** | — | — | **NO bloquear.** Vigilar por proceso de origen y cabecera de autorización (`D-4`) |
| servicio | `graph.microsoft[.]com` · `login.microsoftonline[.]com` | Plano de datos y de autenticación de `GraphDoor`. **Servicio imprescindible** | — | — | **NO bloquear.** Controlar por inquilino (`X-5.2`) |
| servicio | `ably[.]io` · `ably[.]net` · `rest.ably[.]io` · `realtime.ably[.]io` | Transporte del proxy SOCKS5 y canal de entrega de configuración. **El eslabón flojo del modelo del adversario** (`KJ-5`) | — | — | **Alerta, y bloqueo tras evaluar ruido** fuera del parque de desarrollo (`E-a`, `D-3`) |
| servicio | `upload.gofile[.]io` · `file[.]io` | Destino de exfiltración del módulo `Fileupload`. Intercambio anónimo de ficheros | — | — | **Bloqueo**, salvo excepción documentada |
| servicio | `ip.sb` | Consultado por la orden `publicip` | — | — | **Alerta.** No bloquear por sí solo |
| herramienta | MeshCentral / MeshCentral Agent | **Software libre legítimo y ampliamente usado.** Vector inicial documentado por reutilización, no por vulnerabilidad | — | — | **Inventario, no bloqueo** (`X-5.1`) |
| herramienta | Mimikatz · CookieKatz · PetitPotam · WinPTY · `frp` · COFFLoader · Cobalt Strike | Herramientas públicas o comerciales legítimas incorporadas al arsenal. **Su presencia no atribuye** | — | — | **Detección por comportamiento**, no por atribución |

### A.7 — Material nuevo para `CTI-2026-017` y para el expediente de CopperTurtle

> **Esta sección existe porque estos indicadores no están en nuestro propio
> informe de FamousSparrow**, y son útiles para él con independencia de cómo se
> resuelva `KJ-7`.

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| clave | `iotrh^%4CFGTj` | **Clave RC4 fija, atribuida previamente a FamousSparrow**, que descifra la carga leída por `wtsapi32.dll`. **No figura en `CTI-2026-017`** | Alta | Sin caducidad | **Firma de fichero y de memoria.** Incorporar a `CTI-2026-017` en su próxima revisión |
| md5 | `86a46af43e18288e1df439b2a9a6f7ca` (`excint.exe`, componente renombrado de Avast) · `733f8002aa9531b25384c0014d15cc1f` (`wtsapi32.dll`) | Cadena de carga lateral de FamousSparrow observada el 2026-03-06 | Alta | 2027-05-17 | **Bloqueo** |
| path | `%ProgramData%\excint\` · `%ProgramData%\excInt\sg\` | **Directorio de preparación compartido**: FamousSparrow en el padre, `GitDoor` en el subdirectorio, con un día de diferencia. Es la base de `H-9` | Alta | Sin caducidad | **Caza** (`H-9`) |
| md5 | `91bee19d31d32346cd4d1febb4308606` (`WINMM.dll`, cargador de `GitDoor` en ese caso) | La mitad `GitDoor` de la coexistencia de marzo de 2026 | Alta | 2027-05-17 | **Bloqueo** |
| md5 | `45b3aa39bc33528650d9181cd946b2df` (`pdfset.exe`, inyector del RAT `PLEAD`) · `9a5e0ab7466594dcf46943c413db7b81` (`SbieDll.dll`) | Coexistencia con CopperTurtle en `C:\Program Files\PDF24\`, 3 y 4 de mayo de 2026 | Alta | 2027-05-17 | **Bloqueo** |
| path | `C:\Program Files\PDF24\` | Segundo directorio de preparación compartido. **PDF24 es un producto legítimo**: el directorio no es malicioso, es el escondite elegido | Alta en combinación | Sin caducidad | **Caza** (`H-9`) |

## Anexo B — Fuentes y valoración

> Valoración doble tipo Admiralty/OTAN: **fiabilidad de la fuente (A–F)** ×
> **credibilidad de la información (1–6)**. Se valoran por separado.

| Fuente | Disciplina | Fiabilidad | Credibilidad | Notas de sesgo |
|---|---|---|---|---|
| **`B-1` — Kaspersky GReAT, «Operation ShadowCloud… Part 1», Securelist, 17-11-2026** (Saurabh Sharma, Noushin Shabab) — **leída en original**, con su anexo de indicadores completo | OSINT comercial · TECHINT de primera mano con análisis de código | **B** | **2** | **Fuente primaria.** Calidad alta: reconstruye el protocolo petición a petición, publica el alfabeto Base64 propio, las claves fijas, la tabla completa de órdenes y el catálogo de módulos. Declara expresamente que **no atribuye**, que la vía de entrada es desconocida y que su visibilidad es parcial: las tres son señales de calidad. Sesgos: interés comercial en nombrar una campaña nueva; proveedor de origen ruso, lo que en algunos entornos de consumo condiciona la aceptación del producto pero no afecta a la verificabilidad del análisis técnico |
| **`B-2` — Kaspersky GReAT, «Operation ShadowCloud… Part 2», Securelist, 17-11-2026** — **leída en original** | OSINT comercial · TECHINT de primera mano | **B** | **2** | Segunda entrega: `GraphDoor`, los siete plugins, la tabla de proxys y la sección de atribución. **Es la fuente del GUID de inquilino de `A.1`**, que la propia fuente no identifica como indicador. Contiene además las dos tablas de coexistencia que sostienen `O-2.3` |
| **`B-3` — Sophos CTU y Gabor Szappanos, «BRONZE SANDCASTLE deploys modified Meterpreter shells», 20-10-2026** — **leída en original** | OSINT comercial · TECHINT de primera mano | **B** | **2** | **La fuente que convierte este informe en algo más que un resumen.** Cubre agosto 2025 – agosto 2026, nombra cinco países con víctima, publica la tabla de pares de carga lateral y **cita la cuenta `LatonyCharnleyaW` sin reconocer su papel**. Su atribución a China es declarada como sospecha, apoyada en UTC+8 y en solapamiento geográfico con `BRONZE PRESIDENT` y `BRONZE ATLAS`, y dice expresamente que no pudo vincularla a ninguno de los dos. Sesgo relevante: hereda la taxonomía `BRONZE` de Secureworks, cuyo prefijo **presupone** el nexo chino que el informe declara como sospecha |
| **`B-4` — The Hacker News, 17-11-2026** — leída en original | OSINT · prensa especializada derivada | **D** | **3** | Uno de los dos enlaces del requisito. Resumen fiel de las dos entregas de Kaspersky, sin datos propios. **Se usa para una sola cosa**: es la fuente del alias «CopperTurtle (aka BlackTech)», que las entregas de Kaspersky no explicitan. No se usa ninguno de sus datos técnicos |
| **`B-5` — CSV de indicadores de SophosLabs** (`BRONZESANDCASTLE_Meterpreter_IOCs.csv`) | OSINT comercial · indicadores estructurados | **B** | **2** *(por referencia)* | **Citado y NO procesado**, y se declara: es la brecha `G-7`. Es la tarea de colección pendiente de mayor retorno del expediente, porque cruzar sus hashes con los de `B-1`/`B-2` podría elevar `KJ-2` a *casi con certeza* |
| **`B-6` — `cybersecuritynews.com`, artículo sobre GraphDoor** | OSINT · prensa derivada | **—** | **—** | **No leída, y la limitación se declara.** Segundo enlace del requisito. El servidor **rechaza la conexión** (`ECONNREFUSED`), tanto por acceso directo como delegando la lectura; no es un agotamiento de espera. Por su propio titular es una reescritura de `B-2`. **No se usa ningún dato suyo** |
| **`B-7` — Búsquedas en chino y en fuentes taiwanesas** (incluidos Qi An Xin 奇安信, Antiy 安天, Threatbook 微步 y TWCERT/CC) | OSINT · búsqueda negativa | **—** | **—** | **Resultado negativo, y es un hallazgo.** No existe investigación primaria asiática sobre esta operación: todo el material localizado en chino es reescritura de `B-1`/`B-2` o de `B-4`. Las publicaciones de TWCERT/CC que aparecen corresponden a otras campañas. Se consigna para que nadie repita la búsqueda (`3.5`, punto 7) |
| **`B-8` — Consultas propias de DNS y WHOIS**, 2026-11-17 | Verificación propia · técnica | **A** | **1** | Base de `A.5`. **Es la parte más verificable de este informe** y la única con evidencia de primera mano. Limitación: una resolución DNS de un día no dice nada sobre el histórico, y no hay DNS pasivo disponible en este entorno |
| **`B-9` — Documentación de Microsoft sobre restricciones de inquilino v2** | OSINT · documentación de fabricante | **A** | **2** | Base de `X-5.2`. **Y de su salvedad**: la documentación describe el plano de autenticación y no confirma la cobertura del flujo `client_credentials` de un principal de servicio. La salvedad está escrita precisamente porque la fuente no dice lo que haría falta que dijera |

> **Una observación sobre la estructura de fuentes de este informe.** Tres
> fuentes primarias técnicas independientes —dos del mismo proveedor y una de
> otro— es una base mejor que la de la mayoría de los informes de esta cartera,
> y bastante mejor que la de `CTI-2026-033`, que descansaba en una sola. **Pero
> el juicio central no sale de ninguna de las tres: sale de ponerlas una al
> lado de la otra.** Eso significa que su solidez no depende de la calidad de
> las fuentes —que es buena— sino de la corrección de nuestra propia lectura, y
> por eso `O-2.1` publica las trece coincidencias en lugar de resumirlas.

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

> **Por qué los dos ejes van separados, y en este informe importa.** `KJ-2` es
> *muy probable* con confianza *moderada*: creemos bastante que es cierto, y
> sabemos que la base es nuestra lectura y no el hallazgo de un tercero.
> `KJ-7` es *aproximadamente igual de probable* con confianza *baja*: no
> sabemos, y sabemos que no sabemos. Colapsar los dos ejes en un único
> «probable» borraría justamente la diferencia que permite decidir cuál de los
> dos juicios se puede usar y cuál hay que ir a cerrar.

## Anexo D — Cómo reconciliar dos expedientes que describen el mismo objeto sin saberlo

**El problema.** Dos proveedores publican, con semanas o meses de diferencia, sobre lo que resulta ser la misma operación, con nombres distintos, sin citarse y sin solapamiento declarado. No es raro: es el estado normal del mercado de inteligencia de amenazas, donde cada proveedor ve su propia telemetría y bautiza lo que ve. El consumidor recibe dos expedientes y, si no los une, se queda con dos descripciones parciales y con dos conjuntos de víctimas incompletos — que es el error que este informe corrige en su propia cartera.

**Lo que no funciona.** La reconciliación por **infraestructura compartida** —direcciones IP, dominios, certificados, ASN— es la práctica habitual y es la que falla con este tipo de adversario, por dos razones. Primera, porque una infraestructura compartida es compatible con muchas explicaciones que no son identidad: proveedores comunes, intermediarios comunes, arsenales suministrados. Segunda, y decisiva aquí, porque **un adversario cuyo canal vive en servicios de nube de terceros casi no tiene infraestructura propia que comparar**.

**Lo que funciona: artefactos operativos en lugar de infraestructura.** Un artefacto operativo es algo que sólo puede poseer quien opera, no quien aloja ni quien suministra. La jerarquía, de más a menos concluyente:

| Nivel | Artefacto | Por qué pesa | Ejemplo en este expediente |
|---|---|---|---|
| 1 | **Cuenta con credencial de escritura** | No se comparte por alojamiento ni por compra. Quien escribe en un repositorio privado tiene el token. **Es la mano del operador** | La cuenta `LatonyCharnleyaW` en los dos informes |
| 2 | **Esquema de nombres generado por código** | No es una convención humana imitable: es una plantilla con partes aleatorias de longitud fija. Dos informes que publican instancias del mismo esquema están viendo la misma plantilla | `main.<8 car>.js.map`, con tres instancias concretas en un informe y la plantilla en el otro |
| 3 | **Cadenas de versión de la propia herramienta** | Son autodeclaradas por el implante y forman una serie. **Si las versiones de dos informes se intercalan sin huecos, hay una única línea de desarrollo** | `1.1.5` · `1.1.6` · `1.1.7` · `1.2.7` |
| 4 | **Literales del banco de trabajo** | Mensajes por omisión de herramientas de desarrollo, rutas de compilación, nombres de proyecto. **No tienen función operativa**, y por eso nadie los rota | `commit from INSOMNIA` en dos protocolos distintos; `pythonrat` en una ruta de Go |
| 5 | **Nombres de objetos del protocolo interno** | Tuberías, mutex, memoria compartida. Cambiarlos rompe la compatibilidad entre versiones del propio adversario | `Local\pc<PID>`, `\\.\pipe\p<PID>` |
| 6 | **Pares de carga lateral y ficheros auxiliares** | Útiles pero débiles por separado: los pares populares circulan entre actores | `javaw.exe`+`jli.dll`, `config.ini` |
| 7 | **Infraestructura y ofuscación** | El nivel habitual, y el más débil con este tipo de adversario | ASN de proxys, aplanamiento del flujo de control |

**El procedimiento, en cinco pasos.**

1. **Inventariar los artefactos de cada expediente por nivel**, sin mirar todavía al otro. Si se empieza buscando coincidencias se encuentran coincidencias.
2. **Cruzar y clasificar cada coincidencia por su nivel**, no contarlas. Trece coincidencias de nivel 6 y 7 no valen una de nivel 1.
3. **Buscar activamente la explicación alternativa de cada coincidencia de nivel alto.** Para la cuenta compartida, la alternativa es «alguien vende acceso a ese canal»: en este caso es `H-E` de `O-6`, valorada como *remota* porque nada la sugiere y exigiría un modelo de negocio no documentado.
4. **Comprobar si las series temporales son compatibles.** Dos expedientes de la misma operación deben poder ordenarse en una única cronología sin contradicciones. Aquí la de `O-5` se ordena sin forzar nada, y las ventanas de observación se solapan parcialmente, que es lo esperable.
5. **Publicar las coincidencias una por una, con su nivel, para que se puedan romper.** Una reconciliación es una hipótesis, y una hipótesis que no se puede atacar no vale. `O-2.1` está escrita para eso.

**Qué se gana, y qué hay que declarar.** Se gana la unión de los conjuntos de víctimas, la unión de los rangos temporales, la unión de los catálogos de indicadores, y la posibilidad de leer el desarrollo como continuo. Hay que declarar tres cosas: que la reconciliación es propia y no de las fuentes; que la confianza no puede ser alta mientras ninguna de las dos la reconozca; y **que si se rompe, se cae todo lo que se construyó encima**. En este informe esa declaración está en `3.3`, punto 4, y en el pre-mortem de `O-6`.

**Dónde más se aplica en esta cartera.** El método no es específico de este caso. `CTI-2026-022` (Red Akodon) y `CTI-2026-030` (Salt Typhoon) son los otros dos expedientes cuyo problema central es una disputa de nombres, y los dos se resolvieron **separando** en lugar de unir. Este es el primero de la cartera que une, y la asimetría es instructiva: **separar exige demostrar que los arsenales son distintos; unir exige demostrar que el operador es el mismo.** La carga de la prueba no está en el mismo sitio, y la jerarquía de artefactos de arriba es lo que permite saber cuándo se ha satisfecho.

## Anexo E — Marcos de referencia empleados

- **ICD 203** (*Analytic Standards*), para el léxico de probabilidad estimativa y la separación de los ejes de probabilidad y confianza (Anexo C).
- **Código Admiralty/OTAN**, doble valoración de fuente e información (Anexo B).
- **MITRE ATT&CK v18** (`T-2`), con la advertencia de que `T1102.002` es aquí arquitectura y no técnica auxiliar.
- **Pirámide del Dolor** (Bianco), con la reubicación de niveles que `T-3` justifica.
- **Análisis de Hipótesis Competidoras (ACH)** y **pre-mortem**, en `O-6`.
- **TLP 2.0** y **PAP**, para el marcado de difusión y de acción permitida.
- **Jerarquía de artefactos operativos**, propia de este informe (`Anexo D`).

## Anexo F — Paquete legible por máquina

Las tablas `cti:ioc` de este anexo alimentan `ioc_index.csv` en la construcción del repositorio. Tres advertencias de ingesta:

1. **Las entradas de tipo `servicio` no se vuelcan a los agregados planos** `ioc_ipv4.txt` / `ioc_url.txt`, por diseño. GitHub, Microsoft Graph, Ably, `gofile.io`, `file.io`, `ip.sb` y MeshCentral son servicios legítimos y bloquearlos por este informe produce cortes propios.
2. **`38.52.17[.]113` lleva acción «verificación previa obligatoria» y no entra en los agregados planos.** Véase la advertencia de `A.4`.
3. **Los hashes de `config.ini` no son reutilizables entre despliegues**: la carga se cifra con clave por muestra. Se ingieren por completitud, no por cobertura esperada.

Ninguna de las dos fuentes primarias publica paquete STIX. Si alguna lo hace, **esa será la fuente preferente para ingesta** y este anexo pasa a ser derivado.

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-11-17 | Emisión inicial. Incluye la reconciliación de `KJ-2` con sus trece coincidencias (`O-2.1`), el indicador de inquilino de `A.1` que no figura en ninguna lista publicada, los indicios lingüísticos de `KJ-6`, la advertencia sobre `38.52.17[.]113` de `A.4`, la verificación propia de dominios de `A.5`, el material nuevo para `CTI-2026-017` de `A.7` y el método del `Anexo D` | Célula CTI |

## Anexo H — Realimentación del consumidor

Este informe sostiene un juicio central que no está publicado por nadie, y su valor depende de que sea correcto. **La realimentación más útil que puede recibir es que alguien rompa `O-2.1`.** Concretamente:

1. ¿Alguna de las trece coincidencias de `O-2.1` se explica mejor por un arsenal compartido que por un operador común? La más atacable es, probablemente, la 7 (`libcef.dll`), que es un par de carga lateral popular.
2. ¿Hay acceso a `BRONZESANDCASTLE_Meterpreter_IOCs.csv` (`G-7`)? Cruzarlo con los hashes de `A.3` es la tarea de colección más barata y de mayor retorno del expediente.
3. ¿Existe inspección TLS sobre los puntos de autenticación de Microsoft en el entorno del consumidor? Si no, `D-1` —el indicador de mayor valor— es inobservable, y conviene saberlo antes de darlo por desplegado.
4. ¿Se ha probado si una política de restricción de inquilino corta efectivamente un flujo `client_credentials` de principal de servicio (`X-5.2`)? Si alguien lo prueba, el resultado corrige o confirma la única salvedad declarada de ese apartado.
5. ¿Debe abrirse revisión de `CTI-2026-017` por `KJ-7`, o se espera a que aparezca el dato geográfico (`I-1`)?

*Fin del informe `CTI-2026-043` v1.0.*
