---
tlp: "TLP:CLEAR"
pap: "PAP:AMBER"
id: "CTI-2026-036"
version: "1.0"
tipo: "Perfil de actor estatal"
foco_regional: "Latinoamérica · EE. UU."
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "Volt Typhoon · Vanguard Panda · VOLTZITE · Insidious Taurus"
fecha: "2026-11-18"
caduca: "2027-02-18"
autor: "Célula CTI"
distribucion: "Elaborado íntegramente con fuentes abiertas, con cuatro documentos gubernamentales leídos en original —los avisos conjuntos AA23-144A y AA24-038A, el aviso NCSC-UK de abril de 2026 sobre redes encubiertas, y la Directiva de Emergencia ED 26-03 con su versión V1— más el informe de Lumen de octubre de 2026 y el informe de Cisco Talos del mismo día. Difusión libre, conservando la atribución de las fuentes y las salvedades metodológicas de §3. Véase el Anexo B.1 para la decisión sobre una fuente con marcado de propiedad."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-036

## Cinco años en una red sin dejar un fichero, y después cuatro días cero contra los paneles de administración

### El aviso conjunto de 2024 lo describía viviendo de la tierra, sin malware y sin día cero

> **Regla de oro del producto:** todo párrafo debe responder a un requisito de
> inteligencia (PIR) y habilitar una decisión. Si un párrafo no cambia lo que
> alguien va a hacer, va al anexo o se borra.

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-036` |
| Versión / fecha | `1.0` — 2026-11-18 (emisión inicial) |
| Tipo de producto | Perfil de **actor estatal de preposicionamiento**, más evaluación de un adversario cuyo vínculo documentado con la región es de **infraestructura y no de victimología**, más **confirmación del eje geoespacial** que esta cartera declaró como hipótesis en `CTI-2026-034` |
| Niveles cubiertos | Estratégico · Operacional · Táctico · Técnico |
| Foco regional | **Cero víctimas latinoamericanas documentadas.** Y dos huellas regionales de otra naturaleza: módems **Intelbras** (fabricante brasileño) como nodos de relé asignados, y concentración sudamericana en la red de reconocimiento `JDY`. **Se consigna además un incidente eléctrico chileno sin atribuir** —el parque fotovoltaico de Huatacondo— con la advertencia expresa de que **no hay ninguna evidencia que lo vincule a este actor** |
| Marcado de difusión | `TLP:CLEAR` · `PAP:AMBER` |
| Clasificación interna | Sin clasificar. Fuentes principales gubernamentales y públicas |
| Requisitos atendidos | `PIR-01`, `PIR-05` (infraestructura crítica y tecnología de operación), `PIR-09` (superficie expuesta), `PIR-11` (plataformas fuera del inventario de TI), `PIR-12` (nuestros equipos de borde como infraestructura ajena), `RFI-2026-11-B` |
| Solicitante / consumidor primario | Dirección, Jefatura de SOC, **el área de Operaciones/Planta en organizaciones con tecnología de operación**, y —destinatario inusual y deliberado— **el área de Redes, que es la única que puede responder si somos trayecto** |
| Ventana de observación | 2021-06-01 → 2026-11-18. **Ventanas densas:** mayo de 2023 (primer aviso conjunto y publicación de Microsoft), diciembre de 2023 a enero de 2024 (`KV Botnet` y su desarticulación), febrero de 2024 (aviso `AA24-038A`), noviembre de 2023 a julio de 2026 (ventana de observación de `Silent Train`), febrero de 2026 (directiva de emergencia por el día cero de SD-WAN), abril de 2026 (aviso conjunto sobre redes encubiertas), octubre de 2026 (informe de Lumen y de Talos, el mismo día) |
| Base de colección | Catorce fuentes externas, **cuatro primarias gubernamentales leídas en original** (dos avisos conjuntos de EE. UU., un aviso NCSC-UK y de otras quince organizaciones de diez países, y una directiva de emergencia en sus dos versiones), más dos informes técnicos de proveedor leídos en original y el catálogo oficial de vulnerabilidades explotadas consultado por su fichero de datos. **Sin telemetría propia** |
| Autor (analista) | Célula CTI |
| Revisión por pares | Pendiente |
| Aprobación | Pendiente |
| Caducidad / revisión | 2027-02-18 (92 días). **Revisión anticipada** si se publica un caso confirmado en la región, si se publica detalle técnico de la investigación de Huatacondo, o si aparece una sexta campaña de día cero |
| Productos relacionados | **`CTI-2026-034` (Flax Typhoon: el informe con el que este forma par, y la relación es más estrecha de lo que parecía)** · `CTI-2026-030` (Salt Typhoon: el tercer actor chino de infraestructura de esta cartera) · `CTI-2026-033` (StrikeShark: eje geoespacial, y comparte `FRP`) · `CTI-2026-023` (Machete: el primer informe del eje geoespacial) · `CTI-2026-028` (UNC3886: el otro actor de esta cartera que vive en dispositivos sin agente) · `CTI-2026-018` (abuso de TLD) |
| Paquete legible por máquina | **El aviso `AA24-038A` publica su propio paquete STIX 2.1** (`MAR-10448362.c1.v2.CLEAR_stix2.json`) y `AA23-144A` publica el suyo. **Son la fuente preferente para ingesta**, con la salvedad de `A.0`: en este expediente los indicadores de red tienen una propiedad que los hace estructuralmente poco útiles, y está explicada antes del Anexo A |

> ⚠ **Limitación estructural, y una advertencia sobre la naturaleza del sujeto
> que cambia cómo hay que leer todo el documento.** **Sin telemetría propia:**
> `O-4` es un cuestionario. Y hay algo más grave, que no es una limitación de
> esta célula sino del estado del arte: **este actor está diseñado para que la
> pregunta «¿estamos comprometidos?» no se pueda responder con los datos que
> una organización normal conserva**. No deja malware. Borra registros de forma
> selectiva. Sus cadenas de retransmisión se desmontan y se limpian al acabar
> cada sesión. El aviso conjunto de 2024 lo dice sin rodeos —los defensores
> deben **asumir permanencia significativa** y mirar registros de aplicación
> porque son los que duran— y el proveedor de tecnología de operación que más
> casos ha visto estima que **menos del 10 % de las redes de operación del
> mundo tienen visibilidad y monitorización**. Todo lo que este informe afirma
> sobre alcance sale de esa fracción. **La ausencia de casos regionales hay que
> leerla con eso delante.**

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** Este actor no busca datos: busca **estar dentro cuando haga falta**. Tres agencias estadounidenses valoran **con confianza alta** que se preposiciona en redes de tecnología de la información para habilitar movimiento lateral a activos de tecnología de operación y **perturbar funciones físicas** en caso de crisis o conflicto, y declaran que su elección de objetivos y su patrón de conducta **no son consistentes con espionaje tradicional**. En uno de los casos confirmados llevaba dentro **al menos cinco años**. Valoramos **casi con certeza** *(≥99 %)* que el propósito sea el preposicionamiento y no la recolección. **Confianza: alta.** *Base:* aviso conjunto `AA24-038A` de seis organizaciones estadounidenses más cuatro aliadas, leído en original, basado en respuestas a incidentes propias.

**KJ-2.** **Y en 2026 dejó de ser cierto lo que lo definía.** El retrato canónico —vive de la tierra, no usa malware, no usa días cero— describe la fase de posexplotación, y para el acceso inicial ya no se sostiene: Lumen documentó en octubre de 2026 **cuatro campañas de día cero confirmadas y una probable**, todas contra **plataformas de gestión centralizada** —un gestor unificado de puestos, un sistema de administración remota de proveedores de servicio, y **tres orquestadores de SD-WAN distintos**—, y una de ellas se siguió explotando mucho después de que el fabricante publicara el parche. Valoramos **muy probable** *(80–95 %)* que la capacidad de descubrir y explotar días cero contra planos de control sea hoy un rasgo estable de este actor y no un episodio. **Confianza: moderada-alta.** *Base:* fuente única de proveedor con tres años de telemetría de red troncal, **corroborada por una directiva de emergencia gubernamental** y por el catálogo oficial de vulnerabilidades explotadas, que incorporó las cuatro.

**KJ-3.** **Es la inversión exacta del informe anterior de esta cartera, y la consecuencia defensiva es la contraria.** `CTI-2026-034` concluyó que contra Flax Typhoon *toda la defensa cabe en el ciclo de parcheo*, porque sus ocho vulnerabilidades explotadas con éxito eran públicas y antiguas. Aquí el parcheo **llega tarde por definición**: cuatro de cinco campañas usaron vulnerabilidades que no existían públicamente cuando se usaron. Y hay un dato que lo cierra: Dragos sitúa al grupo que solapa con Flax Typhoon y a este actor **probablemente bajo el mismo cliente**. Valoramos **posibilidad real** *(45–55 %)* que ambos modelos respondan a una misma autoridad de tarea con reparto de funciones. **Confianza: moderada.** *Base:* valoración de un proveedor, declarada como *probable* por él mismo, más la coincidencia de que un aviso conjunto de abril de 2026 trate a los dos como usuarios del mismo tipo de infraestructura.

**KJ-4.** **La afirmación del requisito de que este actor es «fundamental para Perú y Chile» no la sostiene ninguna fuente pública localizada.** Los tres documentos gubernamentales principales circunscriben las víctimas a Estados Unidos continental y no continental **y sus territorios, incluido Guam**; el informe de Lumen concentra la selección en **Hawái, California y Texas**; y ninguna agencia latinoamericana figura entre las firmantes de ninguno de los avisos. Valoramos **poco probable** *(20–45 %)* que exista un caso confirmado y no publicado en la región. **Confianza: moderada.** *Base:* ausencia de evidencia en colección dirigida en inglés y en español, **más un mecanismo de selección coherente con esa ausencia**: lo que este actor busca es alcance al Indo-Pacífico, y la región no está en esa ruta.

**KJ-5.** **Pero la región sí está en el expediente, y no como víctima: como infraestructura.** Lumen documenta que en la red de retransmisión del actor los tipos de dispositivo tienen papel fijo, y que los **módems de Intelbras** —fabricante brasileño— aparecen **exclusivamente como nodos de relé extranjeros**, mientras que los equipos de otro fabricante hacen el salto final dentro de Estados Unidos; y la red de reconocimiento asociada, de más de mil quinientos dispositivos, tiene **concentración sudamericana** entre sus nodos. Valoramos **probable** *(55–80 %)* que haya equipos de borde comprometidos en la región formando parte de esta infraestructura hoy. **Confianza: moderada.** *Base:* dos observaciones independientes del mismo proveedor, una nominal por fabricante y otra geográfica; es inferencia sobre el agregado, no un caso confirmado.

**KJ-6.** **El eje geoespacial que esta cartera declaró como hipótesis en `CTI-2026-034` queda confirmado, y por la vía más fuerte posible: ya no son tres casos independientes, es un requisito de colección declarado de un actor estatal.** Dragos define a este actor, literalmente, como un grupo con foco dedicado en datos de tecnología de operación que **usa redes de proxy para robar datos de sistemas de información geográfica, diagramas de red de operación y datos geoespaciales con información crítica sobre la disposición y la arquitectura de los sistemas de energía**; en la misma ficha documenta la explotación de una vulnerabilidad de ejecución remota en un **software de gestión de activos basado en información geográfica**; y Lumen incluye **ArcGIS** entre las plataformas que vio atacar. Valoramos **muy probable** *(80–95 %)* que los datos geoespaciales de infraestructura sean un objetivo de colección prioritario y explícito de al menos un actor estatal. **Confianza: alta.** *Base:* dos proveedores independientes, uno de ellos especializado en tecnología de operación, más el disparador `I-5` de `CTI-2026-034`, que esto activa.

**KJ-7.** **Y el juicio que importa para nosotros, que no es sobre el adversario sino sobre nuestra capacidad de preguntarnos nada.** El 26 o el 27 de agosto de 2026 —las fuentes discrepan en un día— un parque fotovoltaico chileno de 103 MW con un sistema de baterías de 98 MW y 312 MWh quedó desconectado del Sistema Eléctrico Nacional por un ataque informático, y **casi tres meses después sigue con disponibilidad cero**. **No hay ni un indicio que lo vincule a este actor, y este informe no lo insinúa.** Lo que sí afirma es esto: si hubiera sido preposicionamiento, **nadie en la región estaría en condiciones de demostrarlo ni de descartarlo**, porque el 30 % de las investigaciones de incidente en entornos de operación empiezan con alguien diciendo que *algo va mal* y sin los datos para saber si hubo un ataque. Valoramos **casi con certeza** *(≥99 %)* que la incapacidad regional de investigar un incidente de operación sea hoy un riesgo mayor que la probabilidad de ser objetivo de este actor. **Confianza: alta.** *Base:* mediciones publicadas por el proveedor con más casos de respuesta en entornos de operación, más el caso chileno en curso y la ausencia de información técnica pública sobre él a los tres meses.

**Qué cambiaría estos juicios.** **(a)** Un caso confirmado en cualquier país de la región, que invalidaría `KJ-4` y obligaría a rehacer `E-2` entero. **(b)** La publicación de los hallazgos técnicos de la investigación de Huatacondo, que convertiría `KJ-7` de juicio sobre una incapacidad en un caso con nombre, en un sentido o en el otro. **(c)** Evidencia de que las cadenas de retransmisión incluyen nodos en Chile, Perú o Colombia, que subiría `KJ-5` a confianza alta y haría de `E-c` una medida urgente en lugar de preventiva. **(d)** Un aviso conjunto que afirme identidad —no solapamiento— entre este actor y el clúster que Talos designó por separado sobre el mismo día cero, que cerraría la brecha `G-3`. **(e)** Que un gobierno desmienta formalmente el preposicionamiento, o que la contranarrativa china aporte evidencia verificable, lo que afectaría a `KJ-1`; a día de hoy esa contranarrativa existe, está leída, y se trata en `O-2.B`.

---

## 2. Resumen ejecutivo

Hay dos maneras de equivocarse con este actor, y la segunda es nueva.

**La primera es leerlo como espionaje.** No lo es, y lo dicen tres agencias estadounidenses con confianza alta: su elección de objetivos y su patrón de conducta **no son consistentes con recolección de inteligencia**. Entra, roba la base de datos de credenciales del dominio, aprende cómo está hecha la red, **y se queda quieto**. En un caso confirmado extrajo esa base de datos de tres controladores de dominio **a lo largo de cuatro años**; en otro, dos veces en nueve meses. No se lleva información para analizarla: se lleva credenciales para seguir pudiendo entrar, y mapas para saber qué apagar. El aviso documenta que en un compromiso llegó a un sistema de control y estaba en posición de llegar a un segundo, y que en otro tuvo acceso a perfiles de conexión guardados de **plantas de tratamiento de agua, pozos, una subestación eléctrica y sistemas de operación**.

**La segunda manera de equivocarse es la que este informe corrige, y hasta octubre de 2026 era razonable.** El retrato canónico de este actor —el de 2023 y 2024— dice que vive de la tierra, que casi no usa malware, que su rastro es de comandos y no de ficheros. Todo eso sigue siendo cierto **dentro** de la víctima. Lo que ha cambiado es cómo llega: Lumen publicó en octubre de 2026 el resultado de tres años siguiendo su red de retransmisión, y el hallazgo es que ese actor **ha usado al menos cuatro días cero confirmados y uno probable**, todos contra la misma clase de objetivo: **plataformas de gestión centralizada**. Un gestor unificado de puestos de trabajo. Un sistema de administración remota de los que usan los proveedores de servicios gestionados para administrar a sus clientes. Y **tres orquestadores de SD-WAN distintos**, uno tras otro.

**La lógica de esa elección es la parte que hay que llevar a Dirección**, porque es un cambio de modelo de riesgo. Un atacante normal entra por un sitio y luego tiene que recorrer la red, encontrar administradores, localizar sistemas clave y establecer varios puntos de apoyo; cada uno de esos pasos genera autenticaciones, procesos, artefactos. **Una plataforma de gestión ya tiene todo eso**: visibilidad del inventario, acceso administrativo a miles de equipos, relaciones de confianza con las redes de los clientes. Comprometerla da el alcance de una intrusión completa **sin movimiento lateral**. Para un adversario cuyo rasgo definitorio es el sigilo, no es una vía más: es la vía que mejor encaja con lo que es.

**Y hay un dato que reordena esta cartera.** `CTI-2026-034` describió a Flax Typhoon como el actor estatal menos sofisticado del expediente —ocho vulnerabilidades públicas de 2014 a 2023, ningún día cero, escaneo masivo— y concluyó que contra él *toda la defensa cabe en el ciclo de parcheo*. Este informe describe lo contrario. Y Dragos, al dar de alta en febrero de 2026 un grupo nuevo que **solapa con Flax Typhoon**, añade una línea que vale más que varias páginas: **probablemente tiene el mismo cliente que este actor**. Si eso es así, no estamos ante dos actores chinos que hacen cosas distintas: estamos ante **un comprador con dos proveedores y dos modelos** —uno industrial y barato que encuentra víctimas por barrido, y uno artesanal y caro que elige plataformas de gestión y gasta días cero en ellas—. Para un defensor eso significa que **las dos defensas son necesarias y ninguna sustituye a la otra**.

**Sobre la región, la respuesta al requisito es un no, y conviene decirlo con todas las letras.** Ninguna fuente pública localizada documenta una sola víctima de este actor en Perú, Chile, Colombia, Ecuador o cualquier otro país latinoamericano. Los documentos gubernamentales circunscriben las víctimas a Estados Unidos y sus territorios, Guam incluido; la selección que Lumen observó se concentra en **Hawái, California y Texas**, y la explicación que el propio informe propone es coherente: lo que este actor quiere es acceso a los ecosistemas de comunicaciones, defensa y logística que sostienen las operaciones estadounidenses **en el Indo-Pacífico**. La región no está en esa ruta.

**Pero sí está en el expediente, y por eso este informe existe.** Al leer el informe de Lumen aparece un detalle que ninguna fuente comenta: en esa red de retransmisión los tipos de dispositivo **tienen papel fijo y no rotan**, y los módems de **Intelbras** —un fabricante brasileño— aparecen **exclusivamente como nodos de relé extranjeros**, mientras que los equipos de otro fabricante se reservan para el último salto dentro de Estados Unidos. A eso se suma que la red de reconocimiento asociada, de más de mil quinientos dispositivos, tiene **concentración sudamericana**. Juntando las dos cosas: **el papel documentado de la región en las operaciones de este actor es el de trayecto**. Nuestros equipos de borde no son su objetivo; son su tapadera.

**Eso cambia las tres preguntas que hay que hacerse**, y es la aportación propia de este documento. La primera no es «¿nos atacan?» sino **«¿nuestros equipos de borde y los de nuestros clientes forman parte de la cadena de alguien?»**. La segunda es **«¿aceptaríamos una conexión a nuestra VPN corporativa desde un rango de banda ancha residencial sin que nadie lo mirase?»** —que es, literalmente, la comprobación que el aviso conjunto de abril de 2026 pone por delante de todas las demás—. Y la tercera, la que más duele: **«si esto nos hubiera pasado, ¿tendríamos los datos para saberlo?»**.

**Esa tercera pregunta tiene un ejemplo regional en curso y sin atribuir.** El 26 o el 27 de agosto de 2026, un parque fotovoltaico de 103 MW en Tarapacá, con un sistema de baterías de 98 MW y 312 MWh, quedó fuera del Sistema Eléctrico Nacional chileno tras un ataque informático; el Coordinador Eléctrico Nacional activó el protocolo de desconexión; casi tres meses después ambas instalaciones siguen con **disponibilidad cero** y el Congreso ha pedido explicaciones. **No hay ningún indicio que vincule ese incidente a este actor, y sugerirlo sería exactamente el error que tres informes de esta cartera existen para documentar.** Lo que el caso demuestra es otra cosa, y es verificable: a los tres meses no hay información técnica pública, y en un sector donde menos del 10 % de las redes de operación del mundo tienen monitorización, **la pregunta «¿fue preposicionamiento?» no se puede responder**. No por secreto: por falta de datos.

<!-- cti:cards -->

| Rasgo | Qué significa | Etiqueta |
|---|---|---|
| Preposicionamiento, no espionaje | **No viene a llevarse información: viene a estar dentro.** Eso rompe el modelo de impacto habitual: el daño no es la fuga, es la capacidad de parar algo físico más adelante | `01 · propósito` |
| Cinco años de permanencia | El máximo observado en un caso confirmado. **Y extracción repetida de credenciales de dominio para que el acceso no caduque**: tres controladores en cuatro años | `02 · tiempo` |
| Cuatro días cero contra planos de control | **La noticia de 2026, y lo que invalida la defensa de `CTI-2026-034` aplicada aquí.** Gestión de puestos, administración remota y tres orquestadores de SD-WAN | `03 · el cambio` |
| Una plataforma de gestión equivale a una intrusión completa | Acceso administrativo a miles de equipos **sin movimiento lateral**, y por tanto sin los artefactos que delatan una intrusión | `04 · por qué ahí` |
| Cadenas que se autodestruyen | Sesiones de **cuatro horas de media**, hasta seis saltos, limpieza completa al salir. **Los indicadores de red se extinguen por diseño**, no por rotación | `05 · extinción de indicadores` |
| La región es el trayecto | Módems de un fabricante **brasileño** reservados como relé extranjero; red de reconocimiento con concentración sudamericana. **No somos objetivo: somos tapadera** | `06 · nuestro papel real` |
| Datos geoespaciales como objetivo declarado | **El eje que esta cartera seguía desde `CTI-2026-023` deja de ser hipótesis**: hay un actor estatal cuya definición de proveedor incluye robar datos de sistemas de información geográfica de energía | `07 · eje confirmado` |
| No podríamos investigarlo | Menos del 10 % de las redes de operación del mundo tienen visibilidad. **El 30 % de los casos de respuesta empiezan con «algo va mal» y sin datos** | `08 · la brecha propia` |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `5 años` | Permanencia máxima observada en un caso confirmado | Declarado por las agencias estadounidenses en 2024. **Es el dato de permanencia más alto de toda esta cartera** |
| `4 + 1` | Campañas de **día cero** confirmadas y probable | Todas contra **plataformas de gestión centralizada**. Las cuatro vulnerabilidades están en el catálogo oficial de explotadas conocidas |
| `27` | Clases de dispositivo usadas en la red de retransmisión | De módems domésticos a cortafuegos de empresa. **Algunas sin vulnerabilidad conocida**, lo que implica más días cero sólo para montar un salto |
| `4 h` | Duración media de una sesión operativa | Algunas de **minutos**. Montan la cadena en menos de dos minutos y la limpian al salir |
| `6` | Saltos máximos entre el operador y la víctima | Dos servidores privados virtuales, varios dispositivos extranjeros y uno o dos dentro del país de la víctima |
| `>1.500` | Dispositivos en la red de reconocimiento asociada | Partió de unos **650** en enero de 2024, tras la desarticulación. **Se ha más que duplicado después de la intervención policial** |
| `0` | Víctimas latinoamericanas documentadas | En catorce fuentes, cuatro de ellas gubernamentales. **Y cero agencias latinoamericanas firmantes de los avisos** |
| `0 %` | Disponibilidad del parque fotovoltaico chileno de Huatacondo | A casi tres meses del ataque del 26–27 de agosto de 2026. **Sin atribución, sin informe técnico público** |
| `<10 %` | Redes de operación del mundo con visibilidad y monitorización | Estimación del proveedor con más casos. **Todo lo que se sabe de este actor sale de esa fracción** |

> ✅ **Decisiones que se solicitan, con plazo.**
> **(a) 7 días:** inventariar **las plataformas de gestión centralizada** —orquestadores de SD-WAN, gestores de puestos, consolas de administración remota, plataformas de monitorización— y comprobar que ninguna tiene su interfaz de administración accesible desde Internet. **Es el objetivo declarado de las cinco campañas de día cero** (`E-a`).
> **(b) 14 días, y es la medida más rentable del informe:** pasar las conexiones a la VPN corporativa de **lista de denegación a lista de permisión**, y mientras eso no sea posible, **alertar sobre cualquier autenticación correcta desde un rango de banda ancha residencial**. Es la recomendación que el aviso conjunto de abril de 2026 pone primera, y es la única que detecta el último salto de la cadena (`E-b`).
> **(c) 21 días:** responder si **nuestros propios equipos de borde y el parque de equipos en casa de clientes** pueden estar formando parte de la infraestructura de alguien: interfaces de administración expuestas, firmware fuera de soporte, credenciales por omisión. **Esta es la pregunta que nos corresponde por ser de esta región** (`E-c`).
> **(d) 30 días:** en organizaciones con tecnología de operación, determinar **si existirían los datos** para investigar un incidente como el de Huatacondo: registro de la pasarela celular, telemetría de la frontera entre operación e informática, retención suficiente. **No es una medida de detección: es la condición para poder preguntar algo** (`E-d`).
> **(e) 30 días:** inventariar **las plataformas geoespaciales y los datos geoespaciales de infraestructura**, con el criterio de `CTI-2026-034` más el de este informe: ya no es sólo una plataforma vulnerable, es **un objetivo de colección declarado** (`E-e`).
> **(f) 45 días:** revisar si los contratos con proveedores de servicios gestionados y de telecomunicaciones **obligan a notificarnos** un compromiso de sus plataformas de administración, que es el camino por el que este actor llega a los clientes de sus víctimas (`E-f`).
> **(g) Inmediato:** retirar de cualquier matriz de riesgo la idea de que **el parcheo diligente es defensa suficiente contra este actor**. Lo es contra el de `CTI-2026-034`. Aquí llega tarde por construcción (`E-g`).

---

## 3. Alcance, requisitos y limitaciones

**3.1 Requisitos de inteligencia atendidos**

| Req. | Enunciado | ¿Respondido? | Dónde |
|---|---|---|---|
| PIR-01 | ¿Qué actores tienen intención y capacidad contra nuestra región? | **Sí, y la respuesta es contraintuitiva**: este no nos tiene por objetivo, y aun así nos concierne | `KJ-4`, `KJ-5`, `E-2` |
| PIR-05 | ¿Qué amenaza hay sobre infraestructura crítica y tecnología de operación? | **Sí, y es la amenaza mejor documentada de esta cartera en ese terreno** | `KJ-1`, `O-3`, `E-1` |
| PIR-09 | ¿Qué superficie expuesta nos convierte en alcanzables? | **Sí, y cambia de sitio**: no es el perímetro clásico, son las **plataformas de gestión** | `KJ-2`, `E-a`, `A.1` |
| PIR-11 | ¿Qué plataformas quedan fuera del inventario de TI? | **Sí, y el eje geoespacial pasa de hipótesis a objetivo declarado** | `KJ-6`, `O-3.D`, `E-e` |
| PIR-12 | ¿Pueden nuestros activos ser infraestructura de un tercero hostil? | **Sí, y es la aportación propia del informe** | `KJ-5`, `E-c`, `Anexo D` |
| RFI-2026-11-B | El requisito afirmaba que este actor es «fundamental para Perú y Chile». ¿Se sostiene? | **No.** Véase `3.5` | `KJ-4`, `3.5` |
| PIR-04 | ¿Nos afecta? | **No.** Requiere telemetría e inventario propios | `O-4`, sin evaluar |

**3.2 Fuera de alcance.** No se evalúan: la atribución estatal en su última milla, que está establecida por tres agencias estadounidenses y refrendada por los firmantes de dos avisos conjuntos multinacionales, más allá de lo necesario para `O-2`; el detalle técnico completo de la red de bots desarticulada en enero de 2024, cubierta por fuentes de entonces; la política de disuasión y de respuesta estatal ante el preposicionamiento, que es materia de otro tipo de producto; el expediente de Salt Typhoon, que es `CTI-2026-030` y **no es este actor** aunque los dos sean chinos y los dos vivan en infraestructura de red; y el detalle de ingeniería de los cuatro días cero, que corresponde a los avisos de sus fabricantes.

**3.3 Limitaciones de la colección.** Siete, y la cuarta es la que más condiciona el documento.

1. **Sin telemetría propia.** `O-4` es un cuestionario.
2. **Los avisos cubren lo observado en respuestas a incidentes de agencias estadounidenses**, y lo declaran. No son un censo.
3. **El informe de Lumen de octubre de 2026 es fuente única** para las campañas de día cero y para la estructura de la red de retransmisión. Es un proveedor con visibilidad excepcional —telemetría de red troncal global— y tres años de seguimiento, y sus hallazgos están **parcialmente corroborados** por la directiva de emergencia y por el catálogo oficial de explotadas; pero el relato completo lo sostiene él solo.
4. **Este actor está diseñado contra la colección, y eso incluye la nuestra.** No deja malware, borra registros selectivamente y **limpia sus cadenas de retransmisión al terminar cada sesión**. El aviso NCSC-UK de abril de 2026 recoge el nombre que la industria le dio al problema: **extinción de indicadores**. Cualquier afirmación de este informe sobre alcance geográfico hay que leerla sabiendo que el sujeto trabaja para que no se pueda medir.
5. **La información sobre la región es, por su naturaleza, agregada.** `KJ-5` no descansa en un caso: descansa en una asignación de papeles por fabricante y en una distribución geográfica de nodos. Es inferencia sobre un conjunto, y así se declara.
6. **El caso chileno de Huatacondo se conoce por prensa y por la bitácora del operador del sistema, no por informe técnico.** No hay vector, ni indicadores, ni atribución. Y las fuentes **discrepan en la fecha** —26 o 27 de agosto— y **en el código de la solicitud parlamentaria**. Se cita con esa salvedad y sin vincularlo a nadie.
7. **Una fuente lleva marcado de propiedad de su autor.** El informe anual de Dragos de febrero de 2026, que es la mejor fuente disponible sobre la actividad de este actor en entornos de operación en 2025, lleva en cada página la leyenda «Proprietary & Confidential» aunque se publique con descarga libre y se anuncie por nota de prensa. **La decisión tomada y su razonamiento están en el Anexo B.1**, porque esta cartera tiene precedente en contrario y conviene que la diferencia quede escrita.

**3.4 Metodología.** ICD 203. Código Admiralty doble (Anexo B). **MITRE ATT&CK v14** para lo que viene de `AA24-038A`, que es la versión que ese aviso declara, con las técnicas de 2026 mapeadas aparte y marcadas. Pirámide del Dolor, **con una corrección estructural que este expediente obliga a hacer y que está en `T-3`**. ACH, supuestos clave y pre-mortem en `O-6`. **Y dos técnicas estructuradas propias:** la lectura del requisito contra las fuentes de `3.5`, que esta cartera aplica desde el lote de noviembre, y **la inversión de la pregunta de exposición** —de «¿somos objetivo?» a «¿somos infraestructura?»—, cuyo método está generalizado en el Anexo D.

**3.5 Lo que el requisito afirmaba, y lo que las fuentes sostienen**

<!-- cti:table highlight="NO corroborado|Corregido|Ampliado" -->

| # | Afirmación del requisito | Veredicto | Qué dicen las fuentes |
|---|---|---|---|
| 1 | «Volt Typhoon (Bronze Silhouette)… para Perú y Chile» | **NO corroborado** | Ninguna de las catorce fuentes consultadas documenta una víctima de este actor en Perú, Chile ni en ningún otro país de la región. Los documentos gubernamentales circunscriben las víctimas a **EE. UU. continental y no continental y sus territorios, incluido Guam**; Lumen concentra la selección en **Hawái, California y Texas** |
| 2 | «Avisos conjuntos de CISA sobre preposicionamiento en infraestructura crítica» | **Corroborado, y leídos en original** | `AA23-144A` (mayo de 2023) y `AA24-038A` (febrero de 2024, con actualización de marzo). **Con un matiz que es un dato en sí:** entre los firmantes de ambos, y del aviso NCSC-UK de abril de 2026, **no hay una sola agencia latinoamericana**; el único firmante hispanohablante es español, igual que en `CTI-2026-034` |
| 3 | «Contrastar con `CTI-2026-034`: Volt es sigilo artesanal, Flax es escala industrial» | **Corroborado y ampliado en una dirección que el requisito no preveía** | El contraste es exacto y es el eje de `E-1`. **Y hay más:** al dar de alta en febrero de 2026 un grupo que solapa con Flax Typhoon, Dragos valora que **probablemente tiene el mismo cliente que este actor**. Dejan de ser dos expedientes paralelos y pasan a ser **dos proveedores de un mismo comprador** |
| 4 | Caracterización implícita de 2024: «vive de la tierra, sin malware, sin días cero» | **Corregido para 2026** | Sigue siendo exacto **dentro** de la víctima. Para el **acceso inicial** ya no: cuatro campañas de día cero confirmadas y una probable, documentadas en octubre de 2026, todas contra plataformas de gestión centralizada. **Una de ellas se siguió explotando mucho después del parche del fabricante** |
| 5 | «Preposicionamiento en infraestructura crítica» como estado final | **Corregido: se ha movido** | Dragos sitúa a este actor en la **etapa 2** de la cadena de ataque a sistemas de control y documenta que **modificó software de puesto de ingeniería** para extraer ficheros de configuración y datos de alarma **con el fin de averiguar qué condiciones disparan una parada de proceso**. Eso no es preposicionarse: es estudiar el disparador |
| 6 | Modelo de red de retransmisión basado en equipos domésticos comprometidos | **Corroborado, y con una propiedad nueva** | Sigue siendo el modelo. **Pero ha mutado:** ya no es una red de bots persistente —esa se desarticuló en enero de 2024— sino **cadenas desechables que se montan y se destruyen por sesión**, con papeles fijos por tipo de dispositivo y limpieza completa al salir |

> ⚠ **Por qué la corrección del punto 4 es la más importante del informe, y
> qué hay que hacer con ella.** La frase «no usa días cero» es, en el retrato de
> un adversario, una frase de política de defensa disfrazada de dato técnico:
> **si es verdad, el parcheo basta; si es falsa, el parcheo es necesario pero no
> suficiente y hace falta detección**. En `CTI-2026-034` era verdad y la
> conclusión de aquel informe —toda la defensa cabe en el ciclo de parcheo— era
> correcta y barata. Aquí es falsa desde al menos 2023, y sólo lo supimos en
> octubre de 2026 porque un proveedor con visibilidad de red troncal estuvo tres
> años mirando una red de retransmisión. **La consecuencia de gestión es
> incómoda y hay que decirla: contra este actor, el día en que nos enteremos de
> la vulnerabilidad será, con cierta probabilidad, posterior al día en que la
> usaron.** De ahí que `E-a`, `E-b` y `E-d` no sean medidas de parcheo sino de
> **reducción de exposición, de validación de origen y de capacidad de
> investigar**.

---

# NIVEL ESTRATÉGICO
### Para: Consejo · CISO · Riesgo · Legal · Dirección de Operaciones · Horizonte: 6–24 meses

## E-1. Qué representa un adversario que no quiere nada de nosotros hoy

Esta cartera tiene actores que roban dinero, actores que roban información y actores que extorsionan. Este no hace ninguna de las tres cosas, y por eso rompe tres supuestos que están incorporados en casi todas las matrices de riesgo que existen.

**El primero: el daño no está correlacionado con lo que se llevan.** La evaluación gubernamental es explícita en que la conducta observada no es consistente con espionaje; el propio aviso recoge que la industria observó al actor **quedarse silencioso en la red tras volcar credenciales**, hacer reconocimiento para entender el entorno **y no exfiltrar datos**. Una organización con un programa de seguridad orientado a prevenir fugas —que son la mayoría, porque las fugas son lo que genera multas y titulares— **no tiene ningún indicador que se active ante esto**. El activo que se llevan es el conocimiento de cómo está construida la red y un juego de credenciales válidas, y los dos son invisibles en cualquier cuadro de mando de pérdida de datos.

**El segundo: la métrica de permanencia deja de ser un indicador de gestión y pasa a ser el objetivo del adversario.** Todo el sector mide el tiempo de permanencia como un fallo a reducir. Aquí la permanencia **es el producto**: cinco años en un caso confirmado, y extracción repetida de la base de datos de credenciales del dominio —tres controladores en cuatro años, dos veces en nueve meses en otra víctima— precisamente para que el acceso no caduque. Un adversario que vuelve cada cierto tiempo a refrescar sus credenciales no está fallando en su intento de robar: está haciendo mantenimiento.

**El tercero, y es el que cambia la conversación con Dirección: el impacto previsible es físico y diferido.** Lo que el aviso documenta no es una capacidad abstracta. Es acceso a perfiles guardados de conexión a **plantas de tratamiento de agua, pozos, una subestación eléctrica y dispositivos de seguridad de red**; capacidad, en algunos casos, de acceder a **sistemas de videovigilancia de instalaciones críticas**; capacidad de manipular climatización de salas de servidores; y movimiento confirmado hasta un sistema de control con posición para alcanzar un segundo. Y la evolución de 2025 que Dragos documenta cierra el razonamiento: el actor **modificó software de puesto de ingeniería para extraer configuración y datos de alarma, con el propósito de averiguar qué condiciones provocan una parada de proceso**. Eso ya no es acceso: es estudio del disparador.

### E-1.A — El par con `CTI-2026-034`, y por qué conviene leer los dos informes juntos

Este es, de los informes de esta cartera, el que forma par más estrecho con otro. Y la utilidad del par no es comparativa sino operativa: **las defensas que cada uno pide son distintas, y ninguna cubre al otro**.

| Eje | `CTI-2026-034` · Flax Typhoon | `CTI-2026-036` · Volt Typhoon |
|---|---|---|
| Modelo | Empresa con ánimo de lucro, 1.300 guiones, panel de cliente | Operación artesanal, selección deliberada, uno a cinco objetivos por sesión |
| Vulnerabilidades | **Ocho públicas, de 2014 a 2023. Ningún día cero** | **Cuatro días cero confirmados y uno probable, 2023–2026** |
| Selección | **Encuentra** víctimas por barrido | **Elige** víctimas por su posición en un ecosistema |
| Objetivo técnico | Lo que esté expuesto y sin parchear | **Planos de control**: gestión de puestos, SD-WAN, administración remota |
| Propósito | Correo robado, revendido a terceros | **Estar dentro para poder perturbar** |
| Persistencia | VPN legítima renombrada | **Credenciales válidas, nada más** |
| Permanencia | Un año en un servidor de mapas | **Cinco años, y refresco periódico de credenciales** |
| Defensa que lo detiene | **Parcheo, doble factor e inventario** | Reducción de exposición, validación de origen, **detección de comportamiento** |
| Huella regional | **Un caso confirmado: Paraguay** | **Ninguno. Pero nuestros equipos aparecen como relé** |

> **Y el dato que convierte la tabla en algo más que una comparación.** En
> febrero de 2026, al dar de alta un grupo nuevo que **solapa con Flax Typhoon,
> Ethereal Panda y la red de bots de `CTI-2026-034`**, Dragos añadió una línea:
> **probablemente tiene el mismo cliente que este actor**. Un mes y medio
> después, un aviso conjunto de dieciséis organizaciones de diez países situó a los
> dos en el mismo documento como usuarios del mismo tipo de infraestructura
> encubierta, señalando además que **una misma red encubierta puede estar siendo
> usada por varios actores**.
>
> Si eso es así —y es valoración de proveedor, declarada como probable, no un
> hecho establecido—, entonces la lectura correcta de esta cartera es que
> **`CTI-2026-034` y `CTI-2026-036` describen dos proveedores de un mismo
> comprador**: uno que produce volumen barato, y otro que produce acceso
> estratégico caro. Para un defensor eso tiene una consecuencia muy concreta:
> **no se puede elegir entre las dos defensas**. El programa de parcheo cierra
> al proveedor industrial y no toca al artesanal; la detección de comportamiento
> y la reducción de exposición de los planos de control cierran al artesanal y
> no sustituyen al parcheo. Es la misma lección que `CTI-2026-030` aprendió por
> otra vía: **el solapamiento de infraestructura no identifica actores, pero el
> reparto de funciones sí informa sobre la organización que los contrata.**

### E-1.B — La extinción de indicadores, y por qué afecta a lo que este repositorio publica

El aviso conjunto de abril de 2026 —NCSC-UK y quince organizaciones más, entre ellas el Centro Criptológico Nacional español— formaliza un problema que esta cartera arrastra en varios informes y que aquí es estructural. Lo llama, recogiendo el término de la industria, **extinción de indicadores**: si un actor puede operar desde cualquiera de varias redes encubiertas, cada una con cientos de miles de nodos, **y cada una usada por varios actores distintos**, entonces los paradigmas de defensa basados en listas estáticas de direcciones maliciosas pierden casi todo su valor. Y se agrava porque esas redes son dinámicas: entran nodos nuevos a medida que los viejos se parchean o se retiran.

En este expediente eso no es una tendencia: es diseño. Las cadenas de retransmisión **se montan para una sesión y se limpian al terminarla**, con una duración media de cuatro horas y algunas de minutos. Los artefactos que se dejan en el nodo intermedio —un servicio de SSH temporal, una clave, un fichero de configuración— **se borran al salir**. Y el informe de Talos del mismo día de octubre de 2026 publica algo revelador por lo que no publica: para la familia de implantes que analizó, **da rutas de ficheros, nombres de módulos y reglas de red, pero no publica hashes**.

> ⚠ **Consecuencia para este repositorio, y es una decisión de producto.** Los
> agregados planos `ioc_ipv4.txt` y `ioc_url.txt` **no deben crecer con este
> informe**, y de hecho no crecen: el Anexo A de este documento aporta
> indicadores de **artefacto, patrón, ruta y herramienta**, y los pocos valores
> de red que consigna van con su advertencia. No es una carencia de la
> colección: es la respuesta correcta a un adversario cuya infraestructura
> caduca en horas. **Publicar una lista de direcciones de este actor sería
> publicar una lista de víctimas de ayer** —dueños de módems domésticos
> comprometidos— y no una lista de infraestructura del adversario. Es el mismo
> criterio de higiene que `CTI-2026-034` aplicó a los servicios de DNS dinámico
> y `CTI-2026-043` a una errata de un proveedor, llevado a su conclusión.

<!-- cti:cards -->

| Cambio estructural | Por qué nos afecta | Etiqueta |
|---|---|---|
| El daño no es la fuga | **Ningún indicador de pérdida de datos se activa.** Un programa orientado a confidencialidad no ve a este adversario | `01 · modelo de impacto` |
| La permanencia es su producto | Cinco años, con refresco periódico de credenciales. **Medir permanencia como fallo propio pierde sentido cuando es el objetivo ajeno** | `02 · métrica invertida` |
| Días cero contra planos de control | **El parcheo llega tarde por construcción.** Lo que queda es reducir exposición y detectar comportamiento | `03 · el parche no basta` |
| Dos proveedores, un comprador probable | **No se puede elegir entre la defensa de `CTI-2026-034` y la de este informe.** Hacen falta las dos | `04 · la cartera, junta` |
| Extinción de indicadores | Cadenas desechables, limpieza por sesión, nodos compartidos entre actores. **Las listas estáticas de direcciones dejan de servir** | `05 · fin de una era` |
| Nuestros equipos como infraestructura ajena | La región aparece como **trayecto**. Eso convierte a Redes en destinatario de inteligencia, no sólo a Seguridad | `06 · papel invertido` |
| El dato geoespacial como objetivo | **Robar la disposición y la arquitectura de los sistemas de energía está en la definición del actor.** Ya no es una plataforma descuidada: es un requisito de colección | `07 · eje confirmado` |
| No podríamos investigar | Menos del 10 % de redes de operación con visibilidad. **La incapacidad de responder es un riesgo propio, independiente del adversario** | `08 · la pregunta sin datos` |

## E-2. Victimología, y por qué la región no está en ella

<!-- cti:bars title="Sectores que las fuentes nombran como afectados (presencia declarada, no recuento de víctimas)" -->

| Sector | Presencia declarada |
|---|---|
| Comunicaciones y telecomunicaciones | `3` |
| Energía | `3` |
| Sistemas de transporte | `3` |
| Agua y aguas residuales | `2` |
| Gobierno | `2` |
| Base industrial de defensa y contratistas | `2` |
| Tecnologías de la información y proveedores gestionados | `2` |
| Satélite y comunicaciones de misión crítica | `1` |
| Marítimo, ferroviario y aviación | `1` |
| Manufactura y construcción | `1` |
| Universidades con vínculos militares | `1` |

> **Cómo leer ese gráfico, porque no mide lo que parece.** La escala es el
> número de fuentes independientes que nombran cada sector, de un máximo de
> tres —los dos avisos conjuntos y el informe de Lumen—, no un recuento de
> víctimas. **Y la forma importa:** lo que está arriba es comunicaciones,
> energía y transporte, es decir **los sistemas que hacen falta para mover y
> sostener una operación militar**. Lo que aparece abajo, satélite, marítimo,
> ferroviario, aviación, universidades con programas de defensa y proveedores
> gestionados, encaja en la misma lógica por otra vía: **son los que dan acceso
> a los de arriba**. No hay un sector preferido: hay una **cadena logística y de
> comunicaciones** y el actor entra por donde esa cadena es más blanda.

**Y la geografía dice lo mismo con más claridad todavía.** Los avisos circunscriben las víctimas confirmadas a Estados Unidos continental y no continental **y sus territorios, incluido Guam** —y Guam no es un detalle: es el nudo de comunicaciones y la base de proyección de fuerza del Pacífico occidental—. El informe de Lumen, con tres años de observación, señala **Hawái, California y Texas** como las concentraciones repetidas, y propone la explicación que mejor encaja: esos estados albergan instalaciones militares, infraestructura de telecomunicaciones, contratistas de defensa, proveedores de comunicaciones por satélite y redes logísticas críticas **que sostienen operaciones estadounidenses en el Indo-Pacífico**.

**De ahí sale la respuesta al requisito, y conviene enunciarla como mecanismo y no como ausencia.** Si el criterio de selección es la utilidad en un escenario de crisis en el Indo-Pacífico, entonces Perú y Chile no son objetivos probables **por una razón estructural, no por suerte**: no están en esa ruta, no alojan esas instalaciones y no son el camino hacia ellas. Esto es distinto de lo que concluyó `CTI-2026-034` sobre Paraguay: allí el criterio era político —el reconocimiento de Taiwán— y por tanto podía cambiar con una decisión diplomática. **Aquí el criterio es geográfico y logístico, y no cambia.**

> ⚠ **Pero hay dos excepciones concretas y verificables, y no son teóricas.**
> **(1) Las filiales y los proveedores.** Una organización latinoamericana con
> matriz, filial o cliente en Estados Unidos, o que preste servicios gestionados
> a uno, **está dentro del universo de víctimas por vía indirecta**: la
> victimología de Lumen incluye expresamente proveedores de servicios
> gestionados y empresas de tecnología de la información **porque mantienen
> acceso privilegiado al entorno de sus clientes**. El vector no es que nos
> quieran a nosotros: es que somos el camino. **(2) El material submarino y
> satelital.** Los operadores de cable submarino y de comunicaciones por
> satélite con presencia regional sí están en la cadena del Pacífico, y el
> sector aparece nombrado. Ninguna de las dos excepciones tiene caso público en
> la región, y por eso son hipótesis de caza (`I-2`, `I-3`) y no juicios.

## E-3. Tendencia y pronóstico

<!-- cti:chart title="Escalada documentada: de proxy doméstico a día cero contra planos de control" cap="El eje mide el número acumulado de capacidades distintas documentadas públicamente: proxy en equipos domésticos, red de bots persistente, exfiltración de datos geoespaciales, red de retransmisión desechable, días cero contra planos de control, modificación de software de puesto de ingeniería. No mide número de víctimas." -->

| Periodo | Capacidades |
|---|---|
| `2021` | `1` |
| `May·23` | `2` |
| `Dic·23` | `3` |
| `Feb·24` | `4` |
| `2025` | `6` |
| `Oct·26` | `8` |

Las ocho capacidades acumuladas de la serie son: proxy sobre equipos domésticos comprometidos (2021); vivir de la tierra con credenciales válidas y volcado repetido de la base de datos del dominio (mayo de 2023); red de bots persistente para ocultar el origen (diciembre de 2023); posición confirmada en activos adyacentes a sistemas de control (febrero de 2024); robo de datos geoespaciales de infraestructura y entrada por pasarelas celulares industriales (2025); modificación de software de puesto de ingeniería para estudiar los disparadores de parada (2025); red de retransmisión desechable con limpieza por sesión (continuada, documentada en 2026); y **días cero contra planos de control** (documentado en octubre de 2026, con actividad desde al menos 2023). **La serie no baja en ningún punto, y los dos hitos de intervención policial —la desarticulación de la red de bots en enero de 2024 y la directiva de emergencia de febrero de 2026— no producen descenso.**

<!-- cti:cards -->

| Escenario | Desarrollo | Etiqueta |
|---|---|---|
| **Más probable** | Continuidad del modelo: más días cero contra plataformas de gestión, más cadenas desechables, y descubrimiento retrospectivo —meses o años después— de campañas que ya estaban en curso. **El patrón de los últimos tres años es que nos enteramos tarde** | `Probable · 55–80 %` |
| **El que cambia la conversación** | Un uso efectivo de la capacidad: una perturbación física atribuida a este actor en un servicio esencial. **Convertiría todo el expediente de preposicionamiento en precedente**, y las matrices de riesgo de infraestructura crítica de medio mundo tendrían que rehacerse | `Poco probable · 20–45 %` |
| **El que nos afecta a nosotros** | Publicación de que nodos de la cadena de retransmisión están en la región, o de que una filial o un proveedor regional fue vía de acceso. **Es el desarrollo más probable de los que nos conciernen directamente** | `Posibilidad real · 45–55 %` |
| **El que cerraría la brecha regional** | Publicación de los hallazgos técnicos del incidente de Huatacondo, cualquiera que sea su autor. **Demostraría que la región puede investigar un incidente de operación**, que es hoy la duda principal de `KJ-7` | `Posibilidad real · 45–55 %` |
| **Descartado, y se consigna** | Que la desarticulación de infraestructura degrade la capacidad. **La red de reconocimiento asociada pasó de 650 nodos tras la intervención de enero de 2024 a más de 1.500**: se ha más que duplicado después de la operación policial. Se consigna porque la intuición dice lo contrario | `Descartada` |
| **Descartado, y se consigna** | Que un programa de parcheo diligente sea defensa suficiente. **Cuatro de cinco campañas usaron vulnerabilidades inexistentes públicamente en el momento del uso.** Se consigna porque es la conclusión que `CTI-2026-034` autoriza para otro actor y que aquí sería un error | `Descartada` |

## E-4. Decisiones que este informe pide al nivel estratégico

<!-- cti:table highlight="plano de control|banda ancha residencial|trayecto|geoespacial" -->

| # | Decisión | Fundamento | Plazo |
|---|---|---|---|
| E-a | **Inventariar las plataformas de gestión centralizada y retirar de Internet sus interfaces de administración.** Orquestadores de SD-WAN, gestores unificados de puestos, consolas de administración remota, plataformas de monitorización de red, portales de proveedor | `KJ-2`. **Las cinco campañas de día cero fueron contra esta clase de objetivo**, y una plataforma de gestión comprometida equivale a una intrusión completa sin movimiento lateral | 7 días |
| E-b | **Pasar el acceso a la VPN corporativa de lista de denegación a lista de permisión**, y mientras no sea viable, **alertar sobre toda autenticación correcta procedente de rangos de banda ancha residencial** | `KJ-5`, `E-1.B`. **Es la primera recomendación del aviso conjunto de abril de 2026** y la única medida que detecta el último salto de una cadena desechable. Las listas de direcciones maliciosas no sirven aquí | 14 días |
| E-c | **Responder si somos trayecto.** Auditar los equipos de borde propios y el parque instalado en casa de clientes: interfaces de administración expuestas, firmware fuera de soporte, credenciales por omisión | `KJ-5`, `Anexo D`. **Es la decisión que nos corresponde por ser de esta región**, y la que ninguna fuente nos va a pedir. Afecta especialmente a operadores, integradores y proveedores de servicios gestionados | 21 días |
| E-d | **Determinar si existirían los datos para investigar un incidente de operación.** Registro de pasarelas celulares y de acceso remoto, telemetría de la frontera entre operación e informática, retención suficiente, y una decisión escrita sobre quién investiga | `KJ-7`. **No es detección: es la condición para poder preguntar.** El caso chileno en curso lo ilustra: a tres meses no hay información técnica pública | 30 días |
| E-e | **Inventariar plataformas y datos geoespaciales de infraestructura**, con el criterio reforzado: planos de red, diagramas de instalaciones, capas de activos, y quién tiene copia | `KJ-6`. **El eje que `CTI-2026-034` dejó como hipótesis queda confirmado**, y ya no es «una plataforma que nadie parchea» sino **un objetivo de colección declarado de un actor estatal** | 30 días |
| E-f | **Revisar las cláusulas de notificación de incidentes en contratos con proveedores gestionados, de telecomunicaciones y de plataformas de administración** | `E-2`. La victimología incluye expresamente proveedores con acceso privilegiado al entorno de sus clientes. **Si comprometen a nuestro proveedor, nos enteramos si el contrato lo obliga** | 45 días |
| E-g | **Retirar de toda matriz de riesgo la premisa de que el parcheo diligente es defensa suficiente frente a este actor** | `KJ-2`, `KJ-3`. Es cierto para `CTI-2026-034` y falso aquí. **Dejar la premisa genérica en una matriz hace que la medida correcta para un actor se cuente como mitigación del otro** | Inmediato |
| E-h | **Decisión de Dirección:** posición explícita sobre el riesgo de **permanencia silenciosa prolongada** —qué se hace si se encuentra un acceso de años sin exfiltración— incluidos los supuestos de notificación, de contención sin alertar al adversario y de relación con el regulador sectorial | `KJ-1`. La recomendación oficial para este actor es **asumir compromiso total del dominio** y, si la decisión es no alertar, **reducir privilegios en lugar de revocarlos**. Eso es una decisión de Dirección, no del SOC | 60 días |

---

# NIVEL OPERACIONAL
### Para: Jefatura de SOC · Respuesta a Incidentes · Threat Hunting · Redes · Horizonte: semanas–meses

## O-1. Identificación y alias

Este expediente tiene **tres clases de nombre** y confundirlas produce errores concretos, así que la tabla las separa en columna propia: nombres del **actor**, nombres de **infraestructura** y nombres de **clúster de actividad que no son el actor**.

| Designación | Origen | Qué designa | Grado de equivalencia |
|---|---|---|---|
| `Volt Typhoon` | Microsoft | **El actor.** Nombre de referencia | **Referencia.** Es el que usa el aviso conjunto |
| `Vanguard Panda` | CrowdStrike | El actor | **Equivalente.** Listado en `AA24-038A` |
| `BRONZE SILHOUETTE` | Secureworks | El actor | **Equivalente.** Listado en `AA24-038A` |
| `DEV-0391` | Microsoft (designación antigua) | El actor, antes de recibir nombre estable | **Equivalente, histórico** |
| `UNC3236` | Mandiant / Google | El actor | **Equivalente.** Listado en `AA24-038A` |
| `VOLTZITE` | Dragos | El actor, **visto desde los entornos de tecnología de operación** | **Equivalente.** Listado en `AA24-038A`. **Y es la designación con el expediente de operación más rico**: es la que documenta el robo de datos geoespaciales y la etapa 2 |
| `Insidious Taurus` | Palo Alto Networks (Unit 42) | El actor | **Equivalente.** Listado en `AA24-038A` |
| `KV Botnet` | Lumen Black Lotus Labs | **Infraestructura, no el actor.** Red de bots sobre routers Cisco y NETGEAR fuera de soporte, usada como red de transferencia encubierta. **Desarticulada entre finales de 2023 y principios de 2024** | **Es una red, no un grupo.** Y está muerta: citarla como método vigente es el error del punto 6 de `3.5` |
| `JDY` | Lumen Black Lotus Labs | **Infraestructura.** Clúster hermano del anterior, dedicado a **escaneo y reconocimiento**. Sobrevivió a la desarticulación y **pasó de unos 650 nodos a más de 1.500** | **Es una red, y la comparte con otros actores chinos.** Su presencia no atribuye |
| `Silent Train` | Lumen Black Lotus Labs | **Infraestructura, y la que importa hoy.** Marco de acceso encubierto con cadenas desechables de dispositivos comprometidos, observado desde noviembre de 2023 | **Es un marco operativo, no un grupo.** Lumen lo distingue expresamente de una red de bots, de una red de proxy y de una red de cajas de retransmisión |
| `UAT-11473` | Cisco Talos | **Clúster de actividad.** El que explotó el día cero de SD-WAN e instaló una familia de implantes propia | **Solapamiento, NO identidad.** Talos valora **con confianza alta** que su infraestructura **solapa considerablemente** con `Silent Train`. **No dice que sean el mismo actor** |
| `UAT-8616` | Cisco Talos | **Otro clúster**, designado en febrero de 2026 por la explotación activa **del mismo día cero y en la misma plataforma** | **Relación no declarada.** Talos no afirma que `UAT-8616` y `UAT-11473` sean el mismo, ni los vincula a este actor. **Es la brecha `G-3`** |
| `SYLVANITE` | Dragos | **Grupo distinto y de etapa 1**: proveedor de acceso inicial a escala que **entrega puntos de apoyo ya establecidos** a grupos con capacidad en entornos de control, entre ellos este | **NO es el mismo actor.** Es su proveedor, y Dragos lo observó dentro de una eléctrica estadounidense |
| `AZURITE` | Dragos | **Grupo distinto**, que solapa con **Flax Typhoon, Ethereal Panda y la red de bots de `CTI-2026-034`**, y que según Dragos **probablemente tiene el mismo cliente que este actor** | **NO es el mismo actor.** Es, probablemente, **el otro proveedor del mismo comprador**. Es `E-1.A` |
| `TAT25-09` | Dragos | Designación de actividad bajo la que Dragos consigna, en su ficha de este actor, **la explotación de la vulnerabilidad del software de gestión de activos geoespaciales** | **Actividad consignada en el expediente de este actor**, con designación propia. Se cita tal cual, sin componer |

> ⚠ **Nota de *tradecraft*, y es la razón de que esta tabla tenga cuatro
> columnas en lugar de tres.** En este expediente hay **siete nombres del mismo
> actor, tres nombres de infraestructura y cinco nombres de otras cosas**, y los
> tres grupos se citan en la prensa con el mismo tono. Tres consecuencias
> prácticas:
>
> **(1) La infraestructura se comparte y por tanto no atribuye.** El aviso
> conjunto de abril de 2026 lo dice expresamente: **una misma red encubierta
> puede estar siendo usada por varios actores**. Encontrar una conexión desde un
> nodo de `JDY` no significa que sea este actor; significa que es alguien que
> usa `JDY`.
>
> **(2) El solapamiento de infraestructura no es identidad, y aquí hay un caso
> de manual.** Talos designó `UAT-11473` y dijo —con confianza alta— que su
> infraestructura **solapa considerablemente** con `Silent Train`. Lumen, el
> mismo día, atribuyó la explotación de ese mismo día cero a este actor.
> **Las dos cosas pueden ser ciertas sin que los clústeres sean el mismo**, y
> esta cartera ya tiene tres informes —`CTI-2026-017`, `CTI-2026-022` y
> `CTI-2026-030`— que existen porque alguien compuso un solapamiento con una
> equivalencia. Aquí se consigna el solapamiento tal como lo declara su autor y
> **no se compone**.
>
> **(3) Hay dos designaciones de Talos sobre el mismo día cero y la misma
> plataforma, y su relación no está declarada.** `UAT-8616` en febrero de 2026 y
> `UAT-11473` en octubre. Pueden ser el mismo clúster visto en dos momentos, dos
> clústeres del mismo actor, o dos actores que aprovecharon la misma
> vulnerabilidad. **No lo sabemos y no lo vamos a suponer:** es la brecha `G-3`.

## O-2. Estructura y atribución

### O-2.A — Lo que está establecido

| Eje de atribución | Valoración | Confianza |
|---|---|---|
| Nexo con la República Popular China | **Establecido por tres agencias estadounidenses** —CISA, NSA y FBI— y refrendado por los firmantes de dos avisos conjuntos multinacionales | **Alta** |
| Propósito de preposicionamiento para perturbación | **Valorado con confianza alta por las agencias estadounidenses**, sobre la base de respuestas a incidentes propias, y declarado **no consistente con espionaje tradicional** | **Alta** |
| Que la actividad de operación de 2025 sea de este actor | **Valoración de un proveedor especializado** en tecnología de operación, bajo su designación `VOLTZITE`, que `AA24-038A` reconoce como equivalente | Moderada-alta |
| Que las cinco campañas de día cero sean de este actor | **Fuente única de proveedor**, con tres años de telemetría de red troncal, **corroborada indirectamente** por una directiva de emergencia y por la incorporación de las cuatro vulnerabilidades al catálogo oficial de explotadas | Moderada-alta |
| Horario de operación | **Lunes a viernes, entre las 09:00 y las 22:00 de la hora estándar de China**, con pausas de varias semanas en el Año Nuevo chino. Lumen lo lee como **tempo de turnos rotatorios de tipo militar** | **Alta como observación; moderada como inferencia** |
| Que `UAT-11473` sea este actor | **Solapamiento considerable de infraestructura, declarado con confianza alta por Talos. No identidad** | Baja como identidad |
| Identidad nominal de operadores | **Ninguna.** No hay acusaciones penales públicas contra personas nombradas en este expediente | Baja |
| Vínculo con una empresa contratista nombrada | **Ninguno para este actor.** A diferencia de `CTI-2026-034`, aquí no hay empresa designada ni sanción. **La infraestructura sí está vinculada a empresas chinas de seguridad de la información** por el aviso de abril de 2026, pero de forma genérica | Baja |

*Razonamiento:* la pieza de atribución más sólida no es técnica sino de método: **el patrón horario**. Tres años de sesiones concentradas de lunes a viernes en horario de oficina chino, con caída los fines de semana y pausas en el Año Nuevo chino, es un argumento que no depende de ninguna huella de código y que **no se puede falsificar fácilmente** sin degradar la operación. Es, además, el mismo tipo de argumento que esta cartera usó en `CTI-2026-043` desde otro ángulo —artefactos de desarrollo en chino— y conviene notar la diferencia: **aquel era un indicio de quién escribió el código; este es un indicio de quién está al teclado, y en un actor que opera a mano vale más**.

*Contraargumento que hay que mantener vivo:* la atribución del **propósito** es más frágil que la del **origen**. Que un actor esté dentro de una red eléctrica sin exfiltrar datos es compatible con preposicionamiento para perturbar **y también** con espionaje muy disciplinado cuyo producto no vemos. Las agencias lo resuelven por la vía del contexto —qué sistemas tocó, qué documentación recogió, qué perfiles de conexión enumeró— y la evolución de 2025 refuerza su lectura: **estudiar qué condiciones disparan una parada de proceso no tiene explicación de espionaje**. Pero es una inferencia de propósito, y las inferencias de propósito son las primeras que se caen.

### O-2.B — La contranarrativa china, leída en original

Este es el único actor de la cartera cuyo Estado presunto ha publicado una refutación formal, y conviene tratarla como lo que es: **una fuente de parte, con tesis verificables y no verificadas, que hay que leer porque forma parte del entorno de información en el que este informe se consume**.

El Centro Nacional de Respuesta a Emergencias de Virus Informáticos de China, junto con un laboratorio nacional y una empresa de seguridad, publicó **tres informes** —el 15 de abril, el 8 de julio y el 14 de octubre de 2024— sosteniendo que este actor es una fabricación del gobierno estadounidense. **El tercero se ha leído en original.** Sus tesis principales, resumidas sin adornos:

1. **Que el relato existe para sostener la vigilancia sin orden judicial.** El informe sitúa el motivo en la renovación de las facultades de vigilancia exterior estadounidenses y en los intereses de los grupos que se benefician de ellas.
2. **Que Estados Unidos dispone de un juego de herramientas de ocultación** —cuyo nombre en clave cita— **diseñado para atribuir sus propias operaciones a otros países**, y nombra expresamente a China, Rusia, Corea del Norte, Irán y países árabes como destinos previstos de esa atribución falsa.
3. **Que Guam, lejos de ser víctima, es el origen.** Afirma que la base estadounidense en Guam no ha sido víctima de este actor «en absoluto», sino el punto de partida de ataques contra China y países del sudeste asiático.
4. **Que el gobierno estadounidense, sus agencias de inteligencia y Microsoft guardaron silencio** tras los dos primeros informes, y que más de cincuenta expertos de Estados Unidos, Europa y Asia contactaron con el centro para expresar dudas sobre la falta de evidencia. **No nombra a ninguno.**

> ⚠ **Cómo se usa esto, y cómo no.** Se usa de tres maneras legítimas.
> **Primera:** como **dato de entorno**. Si alguien en nuestra organización lee
> que «China dice que Volt Typhoon no existe», conviene que el informe propio ya
> lo haya tratado en lugar de ignorarlo. **Segunda:** como recordatorio de que
> la atribución de este expediente **descansa en respuestas a incidentes que no
> son públicas en su detalle**, y eso es una debilidad real de la evidencia
> disponible, no una invención del refutador. **Tercera:** porque una de sus
> afirmaciones es comprobable y se comprobó: la tesis de que el relato se
> apoyaba en una investigación sobre un grupo de extorsión está construida
> citando trabajo ajeno, y **el investigador citado objetó públicamente que su
> blog se usaba para sostener una conclusión que su investigación no
> respalda**.
>
> **Y cómo no se usa:** como contrapeso simétrico. Los informes de este centro
> **no aportan evidencia técnica verificable** sobre el punto que importa —si
> hubo o no intrusiones con las características que los avisos describen— y
> buena parte de su contenido es argumentación política. Se valora como fuente
> **D–5** en el Anexo B: normalmente no fiable, información improbable. Está
> consignada, está leída, y no modifica `KJ-1`.

## O-3. Modelo de operación

### O-3.A — La cadena clásica, en una frase por fase

**Reconocimiento.** Reconocimiento previo extensivo sobre la organización, su red y su personal, con búsquedas web —incluidos los propios sitios de la víctima— y con especial interés en **quiénes son los administradores de red y de sistemas**. Según el aviso, usa motores de búsqueda de dispositivos expuestos. Y hay una conducta que conviene subrayar porque no es habitual: **en algunos casos ataca los correos personales del personal clave de red y de sistemas** después del compromiso.

**Acceso inicial.** Explotación de vulnerabilidades en equipos de red expuestos —Fortinet, Ivanti, NETGEAR, Citrix, Cisco—, con código de explotación público **pero también con días cero propios**, que es lo que `KJ-2` actualiza. En un compromiso confirmado entró probablemente por una vulnerabilidad de 2022 en un cortafuegos perimetral sin parchear, **y encontró en ese mismo dispositivo una cuenta de administrador de dominio almacenada indebidamente**. Después se conecta por VPN como un usuario legítimo.

**Credenciales.** Primero las del propio dispositivo de borde, por escalada de privilegios o por estar guardadas en claro. Luego, el objetivo real: **la base de datos de Active Directory**, extraída creando una copia de volumen con la utilidad del sistema y copiándola con otra utilidad del sistema, para romper las contraseñas fuera de línea. En algunos casos vuelca la memoria del proceso de autenticación local usando **una versión antigua de una biblioteca legítima de Windows descargada a una carpeta no estándar**. Y usa herramientas públicas de volcado de credenciales y de manipulación de protocolos cuando hace falta.

**Descubrimiento.** Enteramente con utilidades del sistema: una veintena de binarios que están en cualquier Windows. Con un refinamiento que merece atención: **consulta los registros de seguridad del controlador de dominio filtrando por el identificador de inicio de sesión correcto y por usuario concreto**, y vuelca el resultado a un fichero con extensión de datos. No busca el evento de error: busca **quién entra, desde dónde y cuándo**, para moverse con el mismo patrón que la víctima y no disparar alertas de actividad anómala.

**Movimiento lateral.** Escritorio remoto con credenciales válidas de administrador. En un caso del sector de agua, en nueve meses se movió a un servidor de ficheros, a un controlador de dominio, a un servidor de gestión de base de datos y a un **servidor de virtualización adyacente a los activos de operación**, donde enumeró los perfiles guardados de una aplicación de conexión remota: plantas de tratamiento, pozos, una subestación y dispositivos de seguridad de red.

**Recolección.** No datos personales ni propiedad intelectual: **diagramas y documentación de equipos de operación, incluidos sistemas de supervisión y control, relés y aparamenta de maniobra**. En otro caso, documentación de instalaciones y planos de construcción. Y los datos del navegador del administrador de red: historial y credenciales guardadas, incluida la clave de cifrado local que permite descifrarlas.

**Mando y control.** Proxy sobre equipos domésticos comprometidos; una modificación del registro con una utilidad del sistema para convertir un servidor de monitorización de red de la víctima en un proxy propio; y clientes de un proxy inverso libre, **empaquetados con un compresor de ejecutables y con nombres de servicio de Windows**.

**Antiforense.** Borrado selectivo de registros de eventos de Windows y de sistema, borrado de ficheros intermedios y suplantación de nombres de fichero. El aviso añade una instrucción a los defensores que vale su peso: **todo evento de borrado del registro de seguridad hay que investigarlo**, porque los registros no se borran solos y este actor sí los borra.

### O-3.B — La red de retransmisión, que es la novedad de 2026

Esto es lo que Lumen documentó tras tres años de seguimiento, y es la parte del expediente que menos se parece a lo que la mayoría de los defensores espera.

**No es una red de bots.** Una red de bots es persistente, centralizada y repetitiva, y por eso es detectable. Lo que este actor construyó es lo contrario: **cadenas que se montan para una sesión y se destruyen al terminarla**. La estructura es fija aunque los nodos cambien constantemente:

1. Un **servidor privado virtual fuera de Estados Unidos**, provisionado y descartado por sesión.
2. Un **segundo servidor privado virtual** con otro proveedor y otra geografía, para separar más al operador.
3. Varios **dispositivos domésticos o de Internet de las cosas comprometidos fuera de Estados Unidos**, que meten países, proveedores y fabricantes distintos por medio.
4. Uno o dos **dispositivos comprometidos dentro de Estados Unidos**, que dan un punto de salida nacional **para que el tráfico malicioso se mezcle con el legítimo y eluda el bloqueo geográfico y los filtros de reputación de direcciones**.

**Y aquí está el detalle que ninguna fuente comenta y que es el motivo de `KJ-5`.** Lumen observó que los tipos de dispositivo tienen **papel fijo y no rotan**: los módems de un fabricante aparecen **sólo** como nodos de relé extranjeros, y los equipos de otro **sólo** como saltos dentro de Estados Unidos que interactúan con la víctima; y lo mismo con todos los demás tipos. Teniendo infraestructura global suficiente para intercambiarlos, **el actor mantuvo esos papeles fijos durante los tres años de observación**. El fabricante citado para el papel de relé extranjero es **Intelbras, una empresa brasileña**.

> **Qué significa eso para una organización de esta región, dicho sin
> dramatizar.** Significa que, en el único reparto de papeles documentado de
> este actor, **los equipos de fabricación regional tienen asignado el papel de
> trayecto y no el de destino**. No significa que los nodos estén en Brasil
> —Intelbras exporta a varios países de la región y un equipo suyo puede estar
> en cualquier parte—, ni que haya un caso confirmado en la región. Significa
> que, si hay que buscar algo de este actor en nuestra geografía, **lo que hay
> que buscar es un equipo de borde comprometido actuando como relé, no una
> víctima**. Y eso lo busca Redes, no el SOC. Es `E-c` y el Anexo D.

**Operativa:** más de **27 clases de dispositivo** usadas, desde módems domésticos y equipos de malla hasta cortafuegos de empresa y paneles de hospedaje; **algunas sin vulnerabilidad conocida**, lo que implica que el actor gastó días cero **sólo para montar un salto intermedio** —una señal de cuánto valora proteger su acceso—. Montan la cadena explotando interfaces web expuestas, despliegan **sólo** lo necesario para encadenar acceso por SSH —un servicio temporal, una clave, un fichero de configuración, utilidades del propio sistema— y **borran todo al salir**. Sesiones de **cuatro horas de media**, algunas de minutos, y la cadena se levanta en **menos de dos minutos**. Añadían una clase de dispositivo nueva por trimestre, y hasta una por mes en la fase de construcción de 2023–2024, siempre con el mismo patrón: **pruebas fuera de Estados Unidos primero, uso real meses después**.

**Evolución a híbrido:** desde principios de 2025 incorporaron plataformas de empresa —cortafuegos, equipos de red, plataformas de monitorización, servidores de integración sanitaria, paneles de hospedaje— que **permanecen de uno a tres meses** y sirven varias intrusiones, en lugar de descartarse por sesión. Y añadieron variantes de **túnel inverso** con proxys libres, sin sustituir el encadenamiento por SSH: los dos modelos conviven.

**Selectividad:** de uno a cinco objetivos por sesión, **a menudo uno solo**. Esta red no se usa para reconocimiento —para eso están otras— sino **para explotación, acceso a credenciales, exfiltración y trabajo dentro de la víctima**. Es la infraestructura que se reserva para lo que importa.

### O-3.C — La escalada en entornos de operación, que es lo que de verdad ha cambiado

Si `O-3.B` es la novedad técnica, esto es la novedad consecuente. El informe anual de un proveedor especializado en tecnología de operación, publicado en febrero de 2026 sobre la actividad de 2025, documenta tres cosas sobre este actor que, juntas, describen un cambio de fase.

**Primera: entrada por pasarelas celulares industriales.** Compromiso de pasarelas celulares de un fabricante concreto —modelos de uso extendido en energía y en petróleo y gas— **a través de sus interfaces web**, en dos puertos altos. Esas pasarelas son routers industriales que dan conectividad inalámbrica a equipamiento remoto, y el proveedor enumera por qué son peligrosas con una claridad que conviene reproducir en sustancia: **saltan el perímetro** porque la conexión celular crea un camino no autorizado hacia la red de operación; **son invisibles** porque el equipo de seguridad informática a menudo no sabe que existen; **arrastran integración heredada** porque suelen conectar equipos antiguos sin funciones de seguridad; y **son físicamente accesibles** porque están en instalaciones remotas. La actividad analizada apuntó principalmente a **operaciones de oleoducto y gasoducto de transporte medio** en Estados Unidos.

**Segunda: modificación de software de puesto de ingeniería.** Este es el dato. El actor **modificó software en puestos de ingeniería para extraer ficheros de configuración y datos de alarma**, con el propósito declarado por el analista de **averiguar qué condiciones dispararían una parada de proceso**. Y el mismo informe sitúa a este actor en la **etapa 2** de la cadena de ataque a sistemas de control, es decir: ya no está preparándose para poder intentar algo, está **aprendiendo a hacerlo**.

**Tercera: un proveedor de acceso que le entrega el trabajo hecho.** El proveedor dio de alta un grupo nuevo de **etapa 1** cuya función es **comprometer sistemas expuestos a escala y entregar puntos de apoyo ya establecidos** a grupos con capacidad en entornos de control, entre ellos este, **en cuestión de días**; y lo observó dentro de una eléctrica estadounidense, explotando productos de acceso remoto y robando credenciales de directorio. El informe lo resume en una frase que es la que hay que llevarse: **ese reparto de trabajo comprime el plazo entre la brecha inicial y el impacto operativo**.

> ⚠ **Y el caso que pone número a todo esto, publicado en 2025.** Una compañía
> eléctrica y de agua pequeña de Massachusetts tuvo a este actor dentro de su
> entorno informático **más de 300 días**: desde febrero de 2023 hasta que se
> detectó, por aviso del FBI, cerca de noviembre. Lo que el actor buscaba,
> según el proveedor que llevó la respuesta, eran **procedimientos operativos de
> tecnología de operación y datos de disposición espacial de la red eléctrica**.
> Dos observaciones que importan más que el caso:
>
> **(1) Era una organización pequeña**, y el aviso conjunto ya advertía de esto
> en 2024: *algunas víctimas son organizaciones pequeñas con capacidades de
> ciberseguridad limitadas que prestan servicios críticos a organizaciones
> mayores o a localizaciones geográficas clave*. **El criterio no es el tamaño:
> es la posición.** Para esta región eso se traduce en una pregunta concreta y
> rara: ¿qué cooperativa eléctrica, qué empresa sanitaria municipal, qué
> operador portuario pequeño es imprescindible para alguien grande?
>
> **(2) Lo detectó el FBI, no la víctima.** Es el patrón de este expediente
> entero, y es la base de `KJ-7` y de `E-d`: **en la región no hay ninguna
> agencia que haga esa llamada.**

### O-3.D — El eje geoespacial, que con este informe deja de ser una hipótesis

`CTI-2026-034` cerró con un hallazgo propio declarado como **hipótesis retenida con confianza moderada**: tres informes de esta cartera, tres actores sin relación entre sí, y una misma clase de plataforma desatendida. Y dejó un disparador de revisión, `I-5`: *un cuarto caso del mismo eje, en cualquier actor*. **Este informe lo activa, y no con un cuarto caso sino con tres a la vez y de una clase distinta.**

**Primero: el robo de datos geoespaciales está en la definición del actor.** La ficha que el proveedor de tecnología de operación mantiene sobre este actor lo describe —y esto no es un caso, es una caracterización— como un grupo con foco dedicado en datos de tecnología de operación que **usa redes de proxy para robar datos de sistemas de información geográfica, diagramas de red de operación y datos geoespaciales que contienen información crítica sobre la disposición y la arquitectura de los sistemas de energía**. No es que haya entrado por un servidor de mapas: es que **el dato geoespacial de infraestructura es el objetivo**.

**Segundo: explotación de software de gestión de activos basado en información geográfica.** La misma ficha consigna, bajo una designación de actividad propia, la explotación a principios de 2025 de una vulnerabilidad de ejecución remota en un software de gestión de activos geoespaciales, por deserialización insegura en el servidor web de Microsoft, **sin autenticación**; con despliegue de un cargador libre escrito en Rust para entregar cargas de postexplotación. Y el propio proveedor saca la conclusión que esta cartera venía buscando: **los sistemas de información geográfica cartografían activos físicos y relaciones operativas; el dato robado permite planificar ataques precisos y disruptivos contra eléctricas y empresas de agua**, y su recomendación es retirar de Internet los servidores geoespaciales innecesarios **y asumir que ese dato ya robado se usará en intrusiones futuras**.

**Tercero: ArcGIS en la lista de plataformas atacadas.** El informe de Lumen enumera las tecnologías de borde, identidad, red y gestión que vio atacar a este actor, y entre ellas, junto a los nombres previsibles de cortafuegos y gestores de identidad, **aparece ArcGIS**. Con la salvedad que el propio informe declara: su telemetría no siempre permitía determinar si el acceso usó una vulnerabilidad conocida o no divulgada. Es decir: **es selección observada, no compromiso confirmado**. Y es exactamente la misma plataforma en la que `CTI-2026-034` documentó un año de persistencia, en un actor sin relación con este.

> ✅ **Qué cambia, en términos de producto.** El eje geoespacial pasa de
> **hipótesis con confianza moderada apoyada en tres casos independientes** a
> **juicio con confianza alta apoyado en un requisito de colección declarado**.
> La diferencia práctica es grande y conviene decirla sin rodeos:
>
> - Antes, el argumento para inventariar las plataformas geoespaciales era
>   **que nadie las parchea**. Es un argumento de higiene, y los argumentos de
>   higiene pierden siempre contra la falta de tiempo.
> - Ahora el argumento es **que el contenido de esas plataformas es el
>   objetivo**: la disposición y la arquitectura de los sistemas de energía,
>   los diagramas de red de operación, los procedimientos operativos. Eso no es
>   higiene: es protección de un activo identificado por el adversario.
> - Y hay una consecuencia que el enfoque anterior no veía: **el dato ya
>   exfiltrado no se puede parchear**. Si una organización perdió sus capas de
>   activos y sus planos de red hace tres años, la medida no es cerrar el
>   servidor —aunque haya que cerrarlo— sino **asumir que el adversario conoce
>   la topología y diseñar en consecuencia**, que es lo que el proveedor
>   recomienda y lo que `E-e` traslada.
>
> El `Anexo D` de `CTI-2026-034` sigue siendo el borrador del producto propio
> sobre esta superficie, y este informe aporta lo que le faltaba: **la razón por
> la que el adversario la quiere.**

## O-4. Nuestra exposición

> ⬛ **Sección sin evaluar — requiere telemetría e inventario interno.** Y una
> nota sobre la forma: en este expediente **el primer bloque no es del SOC ni de
> TI, es de Redes**, y el segundo no es de Seguridad sino de Operaciones. Es la
> consecuencia directa del Anexo D: si nuestro papel documentado es el de
> trayecto, quien tiene las respuestas es quien administra los equipos de borde.

**¿Somos trayecto? — responde Redes. Es `E-c` y no tiene equivalente en ningún otro informe de esta cartera**

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| R-1 | **¿Cuántos equipos de borde propios tienen su interfaz de administración accesible desde Internet?** Incluidos los que no están en el inventario: equipos de sede remota, de obra, de respaldo celular | Escaneo externo propio | Redes |
| R-2 | **¿Cuántos equipos de nuestro parque están fuera de soporte del fabricante?** Es la condición que el aviso de abril de 2026 señala como razón de que estos equipos sean reclutables | Inventario · fin de vida | Redes |
| R-3 | **Si gestionamos equipamiento en casa de clientes —operadores, integradores, proveedores gestionados—, ¿cuántos de esos equipos tienen administración expuesta o credenciales por omisión?** | Inventario de servicio | Redes · Servicio |
| R-4 | ¿Tenemos registro de tráfico saliente de los equipos de borde, y lo conservamos? **Un relé no genera tráfico hacia nosotros: lo genera desde nosotros hacia un tercero** | NetFlow · registros de dispositivo | Redes · SOC |
| R-5 | ¿Hay servicios de SSH escuchando en puertos no estándar en equipos de borde? **Es el artefacto que la cadena deja mientras la sesión dura, y que se borra al terminar** | Escaneo interno y externo | Redes |

**Planos de control — responde TI y Arquitectura. Es `E-a`**

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| P-1 | **¿Qué plataformas de gestión centralizada tenemos?** Orquestadores de SD-WAN, gestores unificados de puestos, consolas de administración remota, plataformas de monitorización, servidores de integración | Inventario de aplicaciones | TI · Arquitectura |
| P-2 | **¿Alguna tiene su interfaz de administración o su plano de control accesible desde Internet?** | Escaneo externo | TI · Redes |
| P-3 | ¿Cuántos equipos administra cada una, y **a qué entornos de cliente o de filial llega su confianza**? | Arquitectura | Arquitectura |
| P-4 | ¿Están esas plataformas en el programa de gestión de vulnerabilidades con prioridad máxima, o con la del resto? | Vulnerabilidades | Vulnerabilidades |
| P-5 | ¿Conservamos registro de las autenticaciones administrativas y de los cambios de configuración de esas plataformas, y cuánto tiempo? | Configuración de registro | TI · SOC |

**Tecnología de operación — responde Operaciones/Planta. Es `E-d`**

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| O-1 | **¿Cuántas pasarelas celulares hay en nuestras instalaciones remotas, quién las puso y quién las administra?** La pregunta de quién las puso es la importante | Inventario físico · entrevista | Operaciones · Redes |
| O-2 | ¿Alguna tiene interfaz web accesible, y en qué puertos? | Escaneo · inventario | Operaciones · Redes |
| O-3 | **¿Qué puestos de ingeniería existen, y detectaríamos una modificación de su software?** | Inventario · integridad de ficheros | Operaciones |
| O-4 | **¿Dónde están los ficheros de configuración y los datos de alarma, y quién puede leerlos?** Es lo que este actor extrae | Inventario de datos | Operaciones |
| O-5 | ¿Existe telemetría de la frontera entre informática y operación, y se conserva? **Sin esto, `E-d` se responde con un no** | Arquitectura de red | Operaciones · SOC |
| O-6 | ¿Hay un procedimiento escrito de quién investiga un incidente de operación, con qué datos y en qué plazo? | Plan de respuesta | Operaciones · Seguridad |

**Identidad y dominio — responde Sistemas y SOC**

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| I-1 | ¿Hay cuentas de administrador de dominio almacenadas en dispositivos de borde o en ficheros de configuración de equipos? **Es exactamente lo que este actor encontró en un cortafuegos** | Auditoría de configuración | Redes · Sistemas |
| I-2 | **¿Detectaríamos una copia de la base de datos de Active Directory?** Concretamente, ¿recogemos los identificadores de evento del motor de almacenamiento de Windows que la delatan? | Configuración de registro | SOC |
| I-3 | ¿Hay alertas por borrado del registro de seguridad? **El aviso dice que todo borrado debe investigarse** | SIEM | SOC |
| I-4 | ¿Se exige doble factor resistente a suplantación en **todos** los accesos remotos, incluidos los de proveedor y los de operación? | Configuración de identidad | Sistemas |
| I-5 | ¿Revisamos inicios de sesión imposibles por geografía y duración en la VPN? **Es la detección del último salto** | Registros de VPN | SOC |

## O-5. Cronología

<!-- cti:timeline -->

| Fecha | Hecho | Traza |
|---|---|---|
| `2021` (mediados) | **Inicio de la actividad documentada.** Microsoft fija el comienzo a mediados de 2021, con objetivos en **Guam** y el resto de Estados Unidos | Global |
| `2022-12` | Se publica `CVE-2022-42475` en cortafuegos Fortinet. **En un compromiso confirmado, este actor entró probablemente por ella, sin parchear, y encontró en el propio dispositivo una cuenta de administrador de dominio** | Global |
| `2023-02` | **Comienza el acceso a una eléctrica y empresa de agua pequeña de Massachusetts** que duraría más de 300 días | Global |
| `2023-05-24` | **Primer aviso conjunto (`AA23-144A`) y publicación de Microsoft.** Se nombra al actor, se documenta la entrada por dispositivos Fortinet y el proxy sobre equipos domésticos de cinco fabricantes | Global |
| `2023` | **Primer uso del día cero más antiguo documentado**: la actividad de explotación del orquestador de SD-WAN se remonta, según la investigación posterior, al menos a este año | Global |
| `2023-11` | **Primera actividad consistente de la red de retransmisión desechable**, poco antes de la primera desarticulación de la red de bots | Global |
| `2023-12` | Publicación de la investigación sobre la red de bots de routers fuera de soporte usada para ocultar el origen | Global |
| `2024-01` | **Desarticulación judicial de la red de bots.** El clúster de reconocimiento asociado cae a unos **650 nodos**: su punto más bajo | Global |
| `2024-02-07` | **Aviso conjunto `AA24-038A`.** Siete organizaciones estadounidenses y cuatro aliadas. **Confianza alta en el preposicionamiento para perturbar.** Se publica el dato de **cinco años** de permanencia | Global |
| `2024-03-07` | Actualización del aviso: se añade la recomendación de **planificar el fin de vida** de la tecnología fuera de soporte del fabricante | Global |
| `2024-04-15` · `2024-07-08` · `2024-10-14` | **Tres informes del centro chino de respuesta a virus informáticos** sosteniendo que el actor es una fabricación estadounidense. El tercero, leído en original, está evaluado en `O-2.B` | Global |
| `2024-08` | Explotación del primero de los tres orquestadores de SD-WAN, documentada públicamente ese año | Global |
| `2024` (mediados) → `2025` | Campaña contra un **gestor unificado de puestos de trabajo** con más de **treinta víctimas**, que decae tras las actualizaciones de seguridad del fabricante de octubre de 2025 | Global |
| `2025-02` | **Explotación de la vulnerabilidad del software de gestión de activos geoespaciales**, consignada en el expediente de operación de este actor | Global |
| `2025` (principios) | La red de retransmisión **se vuelve híbrida**: incorpora plataformas de empresa que duran de uno a tres meses | Global |
| `2025-08` | Dos vulnerabilidades no divulgadas en una plataforma de administración remota de proveedores de servicio entran en el catálogo oficial de explotadas | Global |
| `2025` | **Escalada en entornos de operación:** entrada por pasarelas celulares industriales, y **modificación de software de puesto de ingeniería para averiguar qué dispara una parada de proceso** | Global |
| `2025` (finales) | **Explotación del día cero del orquestador de SD-WAN**, meses antes de su divulgación | Global |
| `2026-02-25` | **Directiva de emergencia `ED 26-03`** y divulgación del día cero de SD-WAN con puntuación máxima. Talos publica la explotación activa bajo una designación de clúster propia | Global |
| `2026-04-23` | **Aviso conjunto NCSC-UK y quince organizaciones más** sobre redes encubiertas de dispositivos comprometidos, **con este actor y el de `CTI-2026-034` nombrados como usuarios**. **Ningún firmante latinoamericano**; el único hispanohablante es español | Global |
| `2026-07-27` | El día cero del tercer orquestador de SD-WAN entra en el catálogo oficial de explotadas | Global |
| `2026-08-26/27` | **CHILE. Un parque fotovoltaico de 103 MW con baterías de 98 MW y 312 MWh queda desconectado del Sistema Eléctrico Nacional por un ataque informático. Sin atribución. Nada lo vincula a este actor** | **LATAM** |
| `2026-10-28` | **Informe de Lumen sobre la red de retransmisión** —tres años, cuatro días cero confirmados y uno probable— **y, el mismo día, informe de Talos** sobre la familia de implantes del día cero de SD-WAN, con solapamiento de infraestructura declarado | Global |
| `2026-11-14` | El informe diario del operador del sistema chileno sigue mostrando **disponibilidad cero** en las dos instalaciones de Huatacondo, casi tres meses después | **LATAM** |
| `2026-11-18` | Emisión de este informe. **Cero víctimas latinoamericanas documentadas; dos huellas regionales de infraestructura; el eje geoespacial confirmado** | **Chile / LATAM** |

## O-6. Hipótesis alternativas consideradas

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| **H1 — El propósito es preposicionamiento para perturbar, no espionaje** | Valorado con confianza alta por tres agencias estadounidenses sobre respuestas a incidentes propias, y **reforzado en 2025** por la modificación de software de puesto de ingeniería para estudiar los disparadores de parada. Espionaje no explica ese paso | `Retenida · casi con certeza ≥99 %` |
| **H2 — La capacidad de día cero contra planos de control es estable y no episódica** | Cinco campañas en tres años contra la misma clase de objetivo, con **días cero gastados incluso para montar nodos de relé**. La alternativa —una racha— es incompatible con esa inversión | `Retenida · muy probable 80–95 %` |
| **H3 — Este actor y el de `CTI-2026-034` responden al mismo cliente** | **Valoración de un proveedor, declarada por él como probable**, al dar de alta un grupo que solapa con Flax Typhoon. Coherente con que un aviso conjunto los trate como usuarios del mismo tipo de infraestructura. **No es un hecho establecido y así se declara** | `Retenida · posibilidad real 45–55 %, confianza moderada` |
| **H4 — La región no es objetivo de este actor** | Consistente con catorce fuentes, cuatro gubernamentales, **y con un mecanismo**: la selección sigue a los ecosistemas que sostienen operaciones estadounidenses en el Indo-Pacífico, y la región no está en esa ruta | `Retenida · probable 55–80 %` |
| **H5 — La región sí está en el expediente, como infraestructura de retransmisión** | Dos observaciones independientes: **asignación de papel fijo a los módems de un fabricante brasileño** como relé extranjero, y **concentración sudamericana** en la red de reconocimiento. Es inferencia sobre el agregado, no un caso | `Retenida · probable 55–80 %, confianza moderada` |
| **H6 — El dato geoespacial de infraestructura es un objetivo de colección prioritario** | **Dos proveedores independientes**, uno especializado en tecnología de operación que lo incluye **en la definición misma del actor**, más una vulnerabilidad explotada en software de gestión de activos geoespaciales y la aparición de ArcGIS entre las plataformas atacadas | `Retenida · muy probable 80–95 %, confianza alta` |
| **H7 — El incidente chileno de agosto de 2026 guarda relación con este actor** | **Sin ninguna evidencia.** No hay vector público, ni indicadores, ni atribución, y el perfil geográfico del actor apunta en contra. **Se consigna expresamente para que no se reabra ni se insinúe**: componer un incidente sin atribuir con un actor documentado es el error que `CTI-2026-017`, `CTI-2026-022` y `CTI-2026-030` existen para ilustrar | `Descartada por falta de evidencia` |
| **H8 — `UAT-11473` es este actor** | **Solapamiento considerable de infraestructura declarado con confianza alta por Talos, que no afirma identidad.** Y como la infraestructura encubierta **se comparte entre actores** según el aviso de abril de 2026, el solapamiento es compatible con que sean distintos. Se retiene sólo como solapamiento | `Retenida como solapamiento, NO como identidad` |
| **H9 — La desarticulación de infraestructura degrada la capacidad** | **Inconsistente con la medición**: el clúster de reconocimiento pasó de unos 650 nodos tras la operación de enero de 2024 a **más de 1.500**, y la red de retransmisión desechable **ya estaba en marcha antes** de la primera desarticulación. La intervención eliminó una capacidad y aceleró su sustituta | `Descartada` |
| **H10 — El relato es una fabricación, como sostiene la contranarrativa china** | **Inconsistente con la evidencia disponible**: dos avisos conjuntos basados en respuestas a incidentes, un aviso de dieciséis organizaciones de diez países, una directiva de emergencia, cuatro vulnerabilidades en el catálogo oficial de explotadas y dos informes técnicos independientes de proveedor. La contranarrativa **no aporta evidencia técnica verificable** y una de sus citas fue objetada por el investigador citado. Se consigna porque existe y porque se ha leído en original | `Descartada` |

**Supuesto clave.** Que la ausencia de víctimas regionales documentadas refleja **ausencia de actividad regional** y no **ausencia de capacidad regional de detección**. Es el supuesto más frágil de este informe y conviene decirlo con todas sus consecuencias: en una región donde —según la mejor medición disponible— menos del 10 % de las redes de operación del mundo tienen visibilidad, y donde el patrón de detección de este actor es **que una agencia extranjera llame por teléfono a la víctima**, la ausencia de casos publicados es un dato **mucho más débil** de lo que parece. **Qué se rompe si es falso:** `KJ-4` y toda la priorización de `E-2`; lo que **no** se rompe son `E-a` a `E-d`, que están escritas para ser correctas en cualquiera de los dos casos. El falsador es `(a)` de `§1` y el disparador es `I-1`.

**Pre-mortem.** Es mayo de 2027 y este informe resultó equivocado. Los cuatro motivos más probables, en orden:

1. **Se leyó «no nos tiene por objetivo» como «no nos concierne».** Es el riesgo central del documento, porque es la lectura cómoda y porque el titular lo invita. `KJ-5`, `E-c` y el Anexo D dicen lo contrario: nuestro papel documentado es el de trayecto, y ser trayecto tiene coste propio —responsabilidad sobre equipos de clientes, reputación, exposición legal y, en el caso de proveedores gestionados, ser el camino hacia la víctima real—.
2. **`E-d` no se hizo, y entonces el informe no cambió nada.** La decisión más importante de este documento no es técnica ni barata: es determinar si existirían los datos para investigar un incidente de operación. No produce ninguna detección nueva, no cierra ninguna vulnerabilidad y no se ve en ningún cuadro de mando. Y es la única que convierte el próximo incidente en algo investigable. **Si sólo se hace una cosa de este informe, que sea ésta.**
3. **Alguien compuso el caso chileno con este actor.** El informe lo descarta expresamente en `H7`, lo dice tres veces y lo marca en la cronología. Aun así, es la composición más tentadora del documento —un ataque a una planta eléctrica y un actor que se preposiciona en plantas eléctricas— y bastaría una diapositiva mal hecha para que esta cartera cometiera el error que tres de sus informes documentan en otros.
4. **La capacidad de día cero se tomó como razón para no parchear.** `KJ-2` dice que el parcheo es insuficiente, no que sea inútil: una de las cinco campañas siguió explotándose **mucho después del parche del fabricante**, y la entrada confirmada de 2023 fue por una vulnerabilidad de 2022 **sin parchear**. El parcheo sigue siendo necesario; lo que ya no es, es suficiente.

## O-7. Indicadores y señales de alerta

| # | Indicador observable | Qué señalaría | Disciplina | Responsable |
|---|---|---|---|---|
| I-1 | **Un caso confirmado de este actor en cualquier país de la región** | Falsa `H4` y el supuesto clave. **Obliga a rehacer `E-2` y a revisar este informe entero** | OSINT · CSIRT | Célula CTI |
| I-2 | **Publicación de un caso en el que una filial o un proveedor latinoamericano fuera vía de acceso a una víctima estadounidense** | Confirma la primera excepción de `E-2` y convierte `E-f` en urgente | OSINT · sector | Célula CTI |
| I-3 | Actividad de este actor contra operadores de cable submarino o de comunicaciones por satélite con presencia regional | Confirma la segunda excepción de `E-2` | OSINT | Célula CTI |
| I-4 | **Publicación de que nodos de la cadena de retransmisión están en Chile, Perú, Colombia o Brasil** | Sube `KJ-5` a confianza alta. **Convierte `E-c` de medida preventiva en respuesta a incidente** | OSINT · telemetría de operador | Célula CTI · Redes |
| I-5 | **Publicación de los hallazgos técnicos del incidente de Huatacondo** | Cierra la brecha `G-6`, en un sentido o en otro. **Y demostraría que la región puede investigar un incidente de operación** | OSINT · regulador sectorial | Célula CTI |
| I-6 | **Una sexta campaña de día cero contra una plataforma de gestión** | Confirma `H2` como rasgo estable y refuerza `E-a` | OSINT · avisos de fabricante | Vulnerabilidades |
| I-7 | Un aviso conjunto o un informe que afirme **identidad** —no solapamiento— entre este actor y `UAT-11473`, o que relacione `UAT-8616` con alguno de los dos | Cierra la brecha `G-3` | OSINT | Célula CTI |
| I-8 | **Una perturbación física atribuida públicamente a este actor** | Cambia el escenario de `E-3` y, con él, la evaluación de riesgo de infraestructura crítica de cualquier organización | OSINT · gubernamental | Célula CTI · Dirección |
| I-9 | **Un cuarto caso del eje geoespacial en un actor nuevo** | Ya no haría falta para confirmar `KJ-6`, pero **justificaría el producto propio** que el Anexo D de `CTI-2026-034` dejó en borrador | OSINT | Célula CTI |
| I-10 | Evidencia de que la directiva de emergencia de febrero de 2026 no detuvo la explotación del orquestador de SD-WAN | Refuerza `E-g` y `H9`: la intervención no es contención. **Ya hay un indicio: Lumen afirma que la explotación continuó mucho después de la divulgación** | OSINT | Célula CTI |
| I-11 | Aparición de este actor —o de su marco de retransmisión— en un informe de un CSIRT nacional de la región | Primera señal de que la región **puede ver** a este actor, con independencia de que sea objetivo | OSINT · CSIRT | Célula CTI |

---

# NIVEL TÁCTICO
### Para: Analistas de SOC · Ingeniería de Detección · Threat Hunting · Redes · Horizonte: días–semanas

## T-1. Cadena de intrusión

<!-- cti:stages title="Cuatro etapas, y la primera no ocurre en nuestra red" dwell="next" -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 00 · La cadena | Montar un camino que se destruye al salir | **2 servidores privados virtuales** fuera del país · **varios equipos domésticos comprometidos extranjeros** —papel fijo por fabricante— · **1–2 equipos dentro del país de la víctima** para el salto final · SSH encadenado o túnel inverso con proxys libres · **limpieza completa al terminar** · sesiones de **4 h de media**, montaje en **<2 min**, hasta **6 saltos** |
| Etapa 01 · Entrar | Por el plano de control, y a menudo con un día cero | Vulnerabilidades en **Fortinet · Ivanti · NETGEAR · Citrix · Cisco** · **4 días cero confirmados + 1 probable** contra **gestor de puestos, administración remota y 3 orquestadores de SD-WAN** · **credenciales de administrador de dominio guardadas en el propio dispositivo de borde** · pasarelas celulares industriales por su interfaz web · después, **VPN como un usuario normal** |
| Etapa 02 · Hacerse con el dominio | Sin malware, con utilidades del sistema | Copia de volumen con `vssadmin` · `ntdsutil` por `wmic` para copiar **`NTDS.dit` y la rama `SYSTEM`** · rotura de contraseñas **fuera de línea** · versión antigua de `comsvcs.dll` en carpeta no estándar para volcar la memoria de autenticación · **consulta del registro de seguridad filtrando por usuario y por inicio de sesión correcto** · datos del navegador del administrador, **incluida la clave que descifra sus contraseñas** |
| Etapa 03 · Quedarse y aprender | Credenciales válidas, y en 2025, el disparador | **Sin implante: sólo cuentas válidas** · reextracción periódica de credenciales —**tres controladores en cuatro años**— · escritorio remoto · perfiles guardados de conexión a **plantas de agua, pozos, subestación** · **diagramas de supervisión y control, relés y aparamenta** · **modificación de software de puesto de ingeniería para extraer configuración y datos de alarma y averiguar qué dispara una parada** · borrado selectivo de registros |

**Permanencia:** el aviso conjunto publica el dato que define este expediente: **al menos cinco años** en algunas víctimas. El caso con número propio son **más de 300 días** en una eléctrica pequeña, detectados **por aviso del FBI**. Y hay un tercer número, del lado del adversario, que es el inverso y conviene poner junto a los otros dos: **cuatro horas de media por sesión operativa**. Es decir: **años dentro de la víctima, horas dentro de la infraestructura intermedia**. Lo que dura es el acceso; lo que no deja rastro es el camino.

**Y una observación sobre la forma de esta cadena, que determina toda la detección.** La etapa 00 **no ocurre en nuestra red** —ocurre en equipos domésticos de terceros— y por tanto es invisible para cualquier control nuestro salvo por un detalle: **el último salto sí nos habla**, y lo hace desde una dirección que no debería estar hablándonos. La etapa 01 ocurre en el borde, donde con frecuencia no hay agente. La etapa 02 se hace íntegramente con binarios que vienen con Windows. Y la etapa 03 **no tiene artefactos propios en absoluto**: son cuentas legítimas usadas en horario laboral. **De las cuatro etapas, sólo la segunda deja algo que un motor de firmas pueda encontrar**, y lo que deja no es un fichero sino un patrón de uso de utilidades legítimas. Por eso `T-5` —las brechas de visibilidad— es, en este informe, más importante que `X-3`.

## T-2. Mapa MITRE ATT&CK

El aviso `AA24-038A` publica su mapeo sobre **ATT&CK v14**, que es la versión que declara y que este informe hereda para esas filas. Las técnicas que proceden de las fuentes de 2026 —la red de retransmisión, los días cero, la familia de implantes del orquestador de SD-WAN y la actividad en entornos de operación— **van marcadas como tales**, porque no proceden del aviso.

<!-- cti:matrix -->

| Táctica | ID | Técnica | Procedimiento observado |
|---|---|---|---|
| Reconocimiento | T1592 | Gather Victim Host Information | Reconocimiento previo extensivo sobre la organización, su red y su personal, con búsquedas web incluidos los sitios propios de la víctima |
| Reconocimiento | T1589.002 | Gather Victim Identity Information: Email Addresses | **Ataque a los correos personales del personal clave de red y de sistemas**, tras el compromiso |
| Desarrollo de recursos | T1583.003 | Acquire Infrastructure: Virtual Private Server | **Dos servidores privados virtuales fuera del país, con proveedores y geografías distintas**, provisionados y descartados por sesión *(2026)* |
| Desarrollo de recursos | T1584.005 | Compromise Infrastructure: Botnet | Routers Cisco y NETGEAR fuera de soporte implantados para sostener las operaciones. **Desarticulada en enero de 2024** |
| Desarrollo de recursos | T1584.008 | Compromise Infrastructure: Network Devices | **Más de 27 clases de dispositivo** en la red de retransmisión, con **papel fijo por tipo** *(2026)* |
| Desarrollo de recursos | T1584.004 | Compromise Infrastructure: Server | Conversión del servidor de monitorización de red de la víctima en proxy propio, mediante modificación del registro |
| Desarrollo de recursos | T1587.004 | Develop Capabilities: Exploits | **Cuatro días cero confirmados y uno probable contra plataformas de gestión centralizada.** El aviso ya declaraba en 2024 que el actor es «hábil en descubrir y explotar vulnerabilidades como días cero» |
| Desarrollo de recursos | T1588.005 | Obtain Capabilities: Exploits | Código de explotación público para vulnerabilidades conocidas |
| Acceso inicial | T1190 | Exploit Public-Facing Application | Fortinet, Ivanti, NETGEAR, Citrix, Cisco. **Y, en 2025–2026, orquestadores de SD-WAN, gestores de puestos, plataformas de administración remota, software de gestión de activos geoespaciales y pasarelas celulares industriales** |
| Acceso inicial | T1133 | External Remote Services | Conexión por **VPN con credenciales válidas** tras el acceso inicial, para mezclarse con el tráfico normal |
| Acceso inicial | T1078 | Valid Accounts | **Cuenta de administrador de dominio almacenada indebidamente en un cortafuegos perimetral** |
| Ejecución | T1059 | Command and Scripting Interpreter | **Actividad con las manos en el teclado**, por línea de comandos. Algunos comandos son exploratorios y se repiten con variantes, **incluidas erratas** |
| Ejecución | T1059.001 | PowerShell | Guion propio de descubrimiento de inicios de sesión contra todos los controladores de dominio |
| Ejecución | T1047 | Windows Management Instrumentation | `wmic process call create` para lanzar `ntdsutil` y para crear el proxy de puertos |
| Ejecución | T1218 | System Binary Proxy Execution | Una veintena de binarios del sistema como única herramienta de posexplotación |
| Persistencia | T1078 | Valid Accounts | **La persistencia es exclusivamente credencial.** No hay implante en la víctima |
| Persistencia | T1037 | Boot or Logon Initialization Scripts | **Modificación de guiones de servicio** del sistema de arranque del orquestador de SD-WAN para lanzar los componentes del implante *(2026, fuente distinta del aviso)* |
| Escalada | T1068 | Exploitation for Privilege Escalation | Escalada en el sistema operativo o en los servicios de red del dispositivo de borde para obtener las primeras credenciales |
| Evasión | T1006 | Direct Volume Access | `vssadmin create shadow` para esquivar el bloqueo de ficheros de la base de datos del directorio |
| Evasión | T1070.001 | Indicator Removal: Clear Windows Event Logs | Borrado **selectivo** de registros de eventos. **El aviso instruye investigar todo evento `1102`** |
| Evasión | T1070.004 | Indicator Removal: File Deletion | Creación y posterior borrado de `systeminfo.dat` en `C:\Users\Public\Documents` |
| Evasión | T1070.006 | Timestomp | Copia de metadatos de un fichero de referencia con `touch --reference=` y `chmod --reference=` en el orquestador comprometido *(2026)* |
| Evasión | T1027.002 | Obfuscated Files or Information: Software Packing | Clientes de proxy inverso y utilidad de escaneo de puertos **empaquetados con UPX**. Y, en 2026, **carga ELF cifrada con RC4 dentro de un cargador estático sin cabeceras de sección** |
| Evasión | T1036.005 | Masquerading: Match Legitimate Name or Location | Nombres de fichero suplantados: `SMSvcService.exe`, `WmiPrvSE.exe`, `cisco_up.exe`, `vm3dservice.exe`. **Y, en 2026, un servicio que se hace pasar por el de autenticación de la plataforma** |
| Evasión | T1497.001 | Virtualization/Sandbox Evasion: System Checks | El cargador de 2026 **comprueba si hay un depurador** antes de desempaquetar *(2026)* |
| Evasión | T1562 | Impair Defenses | **No por ataque, sino por diseño:** sin malware en la víctima no hay nada que un motor de firmas pueda marcar *(mapeo propio del razonamiento)* |
| Credenciales | T1003.003 | OS Credential Dumping: NTDS | **El objetivo real.** Extracción de `NTDS.dit` y de la rama `SYSTEM`, **repetida en el tiempo sobre la misma víctima** |
| Credenciales | T1003.001 | OS Credential Dumping: LSASS Memory | Versión antigua de `comsvcs.dll` en carpeta no estándar, con `MiniDump` y el identificador del proceso de autenticación |
| Credenciales | T1110.002 | Brute Force: Password Cracking | Rotura de los resúmenes **fuera de línea**, después de exfiltrar la base de datos |
| Credenciales | T1552 | Unsecured Credentials | Credenciales guardadas en claro en el dispositivo de borde |
| Credenciales | T1552.004 | Unsecured Credentials: Private Keys | Fichero de estado local del navegador, **que contiene la clave que descifra las contraseñas guardadas** |
| Credenciales | T1555.003 | Credentials from Password Stores: Web Browsers | Historial y credenciales del navegador **del administrador de red**, deliberadamente |
| Credenciales | T1040 | Network Sniffing | **Intercepción del tráfico del plano de control del orquestador de SD-WAN desde dentro del proceso legítimo**, con extracción de material de clave *(2026)* |
| Descubrimiento | T1654 | Log Enumeration | **Consulta de los eventos de inicio de sesión correcto filtrando por usuario**, con volcado a un fichero `.dat` |
| Descubrimiento | T1012 | Query Registry | Enumeración de los perfiles guardados de una aplicación de conexión remota: **plantas de agua, pozos, subestación, sistemas de operación** |
| Descubrimiento | T1083 | File and Directory Discovery | Enumeración de directorios con contenido de pruebas de vulnerabilidad, de ciberseguridad y de instalaciones, **incluidos planos de construcción** |
| Descubrimiento | T1010 | Application Window Discovery | Fichero `rult3uil.log` en `System32` con títulos de ventana, cambios de foco, pulsaciones y comandos, con marcas de tiempo |
| Descubrimiento | T1046 · T1082 · T1033 · T1069 | Network Service · System Information · Owner/User · Permission Groups Discovery | Enteramente con utilidades del sistema |
| Lateral | T1021.001 | Remote Services: Remote Desktop Protocol | Escritorio remoto con credenciales válidas de administrador de dominio |
| Lateral | T1563 | Remote Service Session Hijacking | Acceso potencial a los sistemas críticos a través de los perfiles de conexión guardados en el servidor de virtualización |
| Lateral | T1550 | Use Alternate Authentication Material | Capacidad de **pasar el resumen o el tique** tras el compromiso completo del directorio |
| Recolección | T1560.001 | Archive Collected Data: Archive via Utility | `ronf.exe`, probablemente una copia renombrada de la utilidad de compresión, sobre la base de datos del directorio |
| Recolección | T1074.001 | Data Staged: Local Data Staging | Directorios temporales creados por `wmic` para preparar la extracción |
| Recolección | T1113 | Screen Capture | Captura de pantalla con dos bibliotecas gráficas del sistema |
| Exfiltración | T1048 | Exfiltration Over Alternative Protocol | Exfiltración por **SMB** de los ficheros comprimidos del servidor de ficheros |
| Mando y control | T1090.003 | Proxy: Multi-hop Proxy | **La cadena completa de `O-3.B`.** Es la técnica central del expediente |
| Mando y control | T1090.001 | Proxy: Internal Proxy | `netsh interface portproxy add v4tov4` sobre el servidor de monitorización de la víctima |
| Mando y control | T1573 | Encrypted Channel | Clientes de proxy inverso libre para abrir un canal encubierto |
| Mando y control | T1055.008 | Process Injection: Ptrace System Calls | Inyección de la biblioteca del implante **en el proceso legítimo del demonio del orquestador**, por identificador de proceso *(2026)* |
| Mando y control | T1574.006 | Hijack Execution Flow: Dynamic Linker Hijacking | Interposición de funciones de socket, de cifrado de transporte y del enlazador dinámico desde dentro del proceso legítimo *(2026)* |

> **Tres filas de esta tabla son el informe entero, y conviene leerlas juntas.**
> `T1078` **en la fila de persistencia**: la persistencia es una cuenta, no un
> fichero, y por tanto **no hay nada que buscar en disco**. `T1090.003`: el
> camino son equipos domésticos de terceros que cambian cada sesión, y por tanto
> **no hay nada que bloquear de forma durable**. Y `T1003.003`: la extracción de
> la base de datos del directorio, **repetida en el tiempo sobre la misma
> víctima**, que es lo único de todo el expediente que deja una traza fiable y
> específica. De ahí sale la prioridad de detección de este informe:
> **`D-1` y `D-2` cubren esa traza, y son la inversión con mejor retorno de
> todo el documento.**

## T-3. Dónde atacamos en la Pirámide del Dolor

<!-- cti:pyramid -->

| Nivel | Qué contiene en este informe y qué vale | Valor |
|---|---|---|
| Hashes | **Hay treinta y uno, más dos resúmenes MD5 de dos de esos mismos ficheros, y casi todos son de 2023.** Diecinueve de clientes de proxy inverso modificados publicados por un proveedor, diez más de un aviso de 2023 —el undécimo de ese aviso coincide con uno de los diecinueve, lo que corrobora entre fuentes— y dos del aviso de 2024. Sirven para búsqueda retrospectiva y nada más. **Y el dato que lo resume: el informe técnico de octubre de 2026 sobre la familia de implantes del orquestador de SD-WAN no publica un solo hash** —publica rutas, nombres de módulo y reglas de red— | Base · **valor trivial, y el propio sector ya lo asume** |
| IP · Dominios | **El nivel que en este expediente hay que declarar inservible, y es una conclusión, no una queja.** La infraestructura es un conjunto de equipos domésticos de terceros que se usan durante una sesión de cuatro horas y se limpian al salir. **Publicar esas direcciones es publicar una lista de víctimas de ayer**, no de infraestructura del adversario. El aviso conjunto de abril de 2026 formaliza el problema con nombre propio: **extinción de indicadores** | **Valor nulo o negativo.** Es la razón de `E-1.B` |
| Artefactos | **El nivel decisivo, y tiene dos mitades.** La primera, en la víctima: los identificadores de evento del motor de almacenamiento de Windows que delatan la copia de la base de datos del directorio, un `comsvcs.dll` fuera de `System32`, `rult3uil.log`, `user.dat` y `systeminfo.dat` en directorios públicos, un `netsh portproxy` que nadie configuró. La segunda, en los equipos de borde: **un servicio de SSH en un puerto no estándar, una clave autorizada que nadie añadió, un servicio de arranque modificado** | Valor medio-alto · **empezar aquí, por las dos mitades** |
| Herramientas | `vssadmin`, `ntdsutil`, `wmic`, `netsh`, `PowerShell`, `certutil`, `ldifde`, `makecab`, `nltest`, `wevtutil`, `xcopy`, el proxy inverso libre, la utilidad de volcado de credenciales, el conjunto de manipulación de protocolos, los proxys de túnel inverso. **Todo legítimo o público. Y `FRP` aparece también en `CTI-2026-033` y en `CTI-2026-043`, usado por clústeres sin relación con éste** | Valor alto · **detectar por contexto, nunca por presencia** |
| TTP | **Cuatro, y la cuarta no está en ningún otro informe de esta cartera.** (1) **Extracción repetida de la base de datos del directorio** a lo largo de años sobre la misma víctima. (2) **Explotación de planos de control** como atajo que evita el movimiento lateral. (3) **Reconocimiento de los registros de inicio de sesión para imitar el patrón horario de la víctima.** (4) **Entrada por el último salto de una cadena desechable**, es decir: una autenticación correcta procedente de un rango que no debería autenticarse nunca | Cima · valor máximo |

> **La corrección que este expediente obliga a hacerle a la doctrina, y es la
> única vez que esta cartera la hace.** La Pirámide del Dolor asume que las
> capas bajas son **poco valiosas pero no dañinas**: hashes y direcciones que
> caducan rápido, se usan y se tiran. Aquí la capa de direcciones es
> **activamente perjudicial**, y por dos razones distintas. La primera es de
> eficacia: una dirección que vive cuatro horas no se puede bloquear a tiempo.
> **La segunda es de daño colateral, y es la que importa:** esas direcciones son
> **conexiones domésticas de terceros inocentes** —el router de una casa, la
> cámara de una tienda—, de modo que una lista de bloqueo construida con ellas
> corta tráfico legítimo de personas que son, ellas mismas, las víctimas del
> compromiso. **Es el mismo mecanismo que la portada de este repositorio
> advierte sobre cargar un `ioc_*.txt` sin filtrar, llevado a su extremo: aquí
> el indicador no sólo es inútil, es que su uso previsible produce daño a un
> tercero.** De ahí que el Anexo A de este informe sea, deliberadamente, un
> anexo sin direcciones de la cadena.

## T-4. Hipótesis de caza prioritarias

<!-- cti:accordion critical="^(H-1|H-2|H-3)\b" regional="^H-1[0-2]\b" -->

**H-1 — Alguien copió la base de datos de Active Directory.** La caza de mayor valor del informe, porque es **el único paso del expediente que deja una traza fiable y específica**, y porque si acierta el incidente ya no es un equipo: es el dominio. Buscar en el registro de aplicación de Windows los identificadores de evento del motor de almacenamiento **`216`, `325`, `326`, `327` y `637`**, que delatan respectivamente el cambio de ubicación de la base de datos hacia una copia de volumen, la creación de una base nueva en un directorio temporal, el montaje de una base procedente de una copia de volumen, su desmontaje, y la creación del fichero de mapa de volcado. Buscar además `vssadmin create shadow` y `ntdsutil` con los argumentos `ac i ntds` e `ifm` —**en forma larga y corta, y combinadas**—, y en especial lanzados a través de `wmic process call create`. **Ventana: toda la que haya.** El aviso recomienda expresamente mirar los registros de aplicación **porque duran más que los de seguridad**, y asumir permanencia significativa. Fidelidad: **muy alta**. Falsos positivos: tareas legítimas de promoción de controlador y de recuperación, que son contadas y documentables.

**H-2 — Hay una autenticación correcta en la VPN desde una dirección que no debería autenticarse nunca.** La otra caza crítica, y la única que ve el último salto de la cadena. No busca malware ni exploits: busca **procedencia**. Extraer todas las autenticaciones correctas en la VPN corporativa y en los accesos remotos de los últimos doce meses y clasificar el origen por tipo de red: ¿cuántas vienen de **rangos de banda ancha residencial**, de redes de operadores móviles ajenos o de rangos asignados a proveedores de hospedaje que no usamos? La pregunta exacta que el aviso conjunto de abril de 2026 pone por delante de todas: **¿esperaríamos una conexión desde un rango de banda ancha de consumo?** Complementar con la comprobación clásica de **viaje imposible** —el aviso de 2024 la pide expresamente para este actor— y con duración y frecuencia anómalas de sesión. Fidelidad: **alta, y mejora muchísimo con una lista de permisión**. Falsos positivos: teletrabajo legítimo, que es precisamente lo que hay que enumerar para poder distinguirlo. **Es `E-b` y, de todo el informe, la medida con mejor relación entre coste y cobertura.**

**H-3 — Hay un plano de control expuesto o comprometido.** La caza que corresponde a la novedad de 2026. Primero inventario: orquestadores de SD-WAN, gestores unificados de puestos, consolas de administración remota, plataformas de monitorización de red, servidores de integración. Después, para cada uno: **¿está su interfaz de administración o su plano de control accesible desde Internet?** Y después los artefactos: en los sistemas de tipo controlador de SD-WAN, **guiones de servicio del sistema de arranque modificados**, servicios con nombre de servicio legítimo que no deberían existir como ejecutable compilado, bibliotecas inyectadas en los procesos del demonio, ficheros de puesta en escena en `/var/tmp`, claves de SSH autorizadas para cuentas de administración de la plataforma, y **eventos de emparejamiento del plano de control cuyo origen o tipo de nodo no cuadre con la topología**. Fidelidad: alta para la parte de inventario, **media para los artefactos y dependiente de que exista registro externo**. Y una nota de respuesta que la directiva de emergencia estadounidense impone a sus agencias y que conviene adoptar: **si se confirma compromiso de la cuenta de superusuario, la recomendación no es limpiar, es reconstruir el plano de control desde imágenes parcheadas y migrar los nodos**.

**H-4 — Hay un binario del sistema en un sitio donde no vive.** El actor descargó **una versión antigua de `comsvcs.dll` a una carpeta no estándar** de un controlador de dominio para volcar la memoria del proceso de autenticación. Cazar: bibliotecas y ejecutables con nombre de componente del sistema **fuera de `System32`, `SysWOW64` y `WinSxS`**, con prioridad en `C:\Windows\Temp`, `C:\Users\Public` y `C:\PerfLogs`, que son las tres rutas que el aviso de 2023 señala como habituales. Añadir los nombres de fichero conocidos del Anexo `A.2`. Fidelidad: muy alta. Falsos positivos: pocos y explicables. **Es la caza más corta del informe.**

**H-5 — Alguien consultó los registros de inicio de sesión para aprender nuestro horario.** La caza más característica de este actor y la que casi nadie hace. El procedimiento documentado es un comando de PowerShell que extrae los eventos de inicio de sesión correcto posteriores a una fecha, **los filtra por una cuenta concreta** y los vuelca a un fichero. Cazar: uso de `Get-EventLog` o `Get-WinEvent` con filtro por el identificador de inicio de sesión correcto en controladores de dominio; escritura de ficheros con extensión `.dat` o `.log` en `C:\Users\Public\Documents`; y el guion propio del actor, que **enumera todos los controladores del dominio y consulta los registros de seguridad de cada uno**. Fidelidad: alta en controladores de dominio, donde esa consulta tiene pocos usos legítimos interactivos. **Y el valor estratégico de esta caza:** si acierta, nos dice que el adversario está aprendiendo **cuándo** operamos para operar a la misma hora, lo que a su vez explica por qué las alertas de actividad anómala no se disparan.

**H-6 — Hay un proxy de puertos que nadie configuró.** El actor usa `netsh interface portproxy add v4tov4` para convertir un servidor de la víctima en proxy. Cazar: la clave del registro de proxy de puertos en todos los servidores; ejecuciones de `netsh` con `portproxy`, **tanto de alta como de baja** —el actor también lo borra, y el borrado es igual de delator—; y puertos a la escucha que no correspondan a ningún servicio conocido. Fidelidad: muy alta. **Falsos positivos: prácticamente ninguno en un parque gestionado, porque casi nadie usa esta función legítimamente.**

**H-7 — Hay un proxy inverso libre en algún servidor.** Cazar los nombres de fichero documentados —`SMSvcService.exe`, `Brightmetricagent.exe`, `cisco_up.exe`, `vm3dservice.exe`, `watchdogd.exe`, `WmiPreSV.exe`, `WmiPrvSE.exe` fuera de su sitio, `cl64.exe`, `Win.exe`, `nc.exe`— y, sobre todo, **las cadenas del proyecto libre dentro de ejecutables**, con la regla de reconocimiento del Anexo `A.2`. Hay un detalle que el aviso de 2023 publica y que es un indicador casi perfecto: la variante propia del actor contiene una **cadena fija de nueve caracteres con contenido político**, que no aparece en el proyecto original. Un ejecutable que la contenga no admite explicación alternativa. Fidelidad: **máxima para la cadena fija; media-alta para los nombres**, que son antiguos. Y la salvedad de cartera: **este proxy lo usan también `CTI-2026-033` y `CTI-2026-043`**, así que su presencia no atribuye.

**H-8 — Se borró un registro de seguridad.** Caza mínima y barata. **Todo evento de borrado del registro de seguridad —identificador `1102`— debe investigarse**, porque los registros no se borran por sí solos y éste es un procedimiento documentado del actor. Extender a borrado selectivo de registros de sistema y a huecos inexplicados en la serie temporal de eventos. Fidelidad: alta. **Y si esta caza no se puede hacer porque no conservamos el registro de seguridad centralizado, eso es el primer hallazgo y es `T-5`.**

**H-9 — Alguien tocó el navegador del administrador de red.** El actor accedió por red compartida al historial y al fichero de estado local del navegador de un administrador, **que contiene la clave que descifra sus contraseñas guardadas**, y en un caso volvió a por más **cuatro meses después**. Cazar: accesos por red a rutas de datos de usuario de navegador en estaciones de administradores; creación de ficheros comprimidos en `Downloads` con nombres de datos de navegador; y el evento de sistema de cierre forzado de manejador sobre la comparticion administrativa con ficheros de esa clase. Fidelidad: media-alta. **Medida preventiva asociada, que es más barata que la caza: prohibir por política el almacenamiento de contraseñas en el navegador en los equipos de administración.**

**H-10 — ¿Somos trayecto? Los equipos de borde propios.** Primera de las tres cazas de alcance regional, y la que nos corresponde por `KJ-5`. No se hace en el SIEM: **se hace desde fuera, con un escáner, y la hace Redes**. Enumerar desde Internet todo el rango propio buscando **interfaces de administración de equipos de borde accesibles** —web, SSH, Telnet— y cruzar el resultado con el inventario de fin de vida. Después, en los equipos encontrados: servicios de SSH en puertos no estándar, claves autorizadas que nadie añadió, usuarios nuevos, procesos que no pertenecen al firmware, y tráfico saliente hacia direcciones que no corresponden a ningún servicio nuestro. **Qué estamos buscando:** no un ataque contra nosotros, sino **un salto de la cadena de alguien**. Fidelidad: no aplica, es inventario. **Y una advertencia honesta: si la cadena se limpió al terminar la sesión, no habrá nada que encontrar, y lo único que queda es la condición que permitió el reclutamiento —administración expuesta y firmware sin soporte—, que es lo que de verdad hay que cerrar.**

**H-11 — ¿Somos trayecto? El parque instalado en casa de clientes.** Variante de la anterior, y aplica a operadores de telecomunicaciones, integradores, proveedores de servicios gestionados y a cualquier empresa que instale equipamiento en instalaciones de terceros. La pregunta: **¿cuántos de los equipos que gestionamos o que vendimos tienen la administración expuesta, el firmware fuera de soporte o las credenciales por omisión?** Es una pregunta de responsabilidad sobre producto y servicio, no de seguridad propia, y tiene consecuencias contractuales y reputacionales que convienen a Dirección. **Contexto regional, y es el motivo de que esta caza exista:** el único reparto de papeles documentado de este actor asigna a los módems de un fabricante **brasileño** el papel de relé extranjero, y la red de reconocimiento asociada tiene **concentración sudamericana**. Fidelidad: no aplica. **Coste: medio. Valor: es la única caza de este informe que nadie más va a hacer por nosotros.**

**H-12 — ¿Tendríamos los datos? La caza que no busca al adversario.** Última caza de alcance regional y la más incómoda, porque su resultado previsible es un no. Tomar el caso chileno de agosto de 2026 como ejercicio: **un parque de generación queda fuera del sistema por un ataque informático y el operador del sistema activa el protocolo de desconexión.** Y responder, para una instalación nuestra equivalente: ¿qué registros existirían del día anterior? ¿Está registrado el acceso a la pasarela celular? ¿Hay telemetría de la frontera entre informática y operación, y cuánto se conserva? ¿Quién investigaría, con qué autoridad y en qué plazo? ¿Sabríamos distinguir un fallo de un ataque? Fidelidad: no aplica, es un ejercicio de mesa. **Y su valor es exactamente el que `KJ-7` afirma: en un sector donde menos del 10 % de las redes de operación tienen visibilidad y donde el 30 % de las investigaciones empiezan con alguien diciendo que algo va mal, la pregunta «¿nos pasó?» no tiene respuesta posible. Esta caza mide cuánto nos falta para que la tenga.** Es `E-d`.

## T-5. Brechas de visibilidad que hay que cerrar primero

| Brecha | Por qué importa aquí |
|---|---|
| **Sin registro de aplicación de Windows conservado en los controladores de dominio** | Deja ciega `H-1`, que es la caza de mayor valor. **Y es la peor de todas por una razón específica: el aviso recomienda mirar esos registros precisamente porque duran más que los de seguridad**, de modo que son la única esperanza frente a un actor con permanencia de años |
| **Sin clasificación del origen de las autenticaciones remotas** | Deja ciega `H-2`. Si los registros de VPN no permiten responder «¿de qué tipo de red viene esta conexión?», **el último salto de la cadena es indistinguible de un teletrabajador** |
| **Sin registro externo de las plataformas de gestión** | Deja ciega `H-3`. Y tiene un agravante: **un actor que compromete el plano de control puede borrar los registros que viven en él**. La directiva de emergencia estadounidense obliga a sus agencias a almacenar esos registros **fuera** del propio sistema, y es la razón correcta |
| **Sin visibilidad en los equipos de borde y sin escaneo externo propio** | Deja ciegas `H-10` y `H-11`, que son las cazas regionales. **No es una brecha de seguridad: es una brecha de inventario**, y la vista que hace falta es la del adversario, es decir, desde fuera |
| **Sin telemetría de la frontera entre informática y operación, ni de las pasarelas celulares** | Deja ciega `H-12` y hace imposible `E-d`. **Es la brecha que el proveedor de tecnología de operación mide: menos del 10 % de las redes de operación del mundo la tienen cerrada** |
| **Sin alerta por borrado del registro de seguridad** | Deja ciega `H-8`, que cuesta una regla |
| **Sin registro de creación de proxy de puertos ni de ejecución de `netsh`** | Deja ciega `H-6`, que es la de menor tasa de falsos positivos del informe |
| **Sin registro de ejecución de PowerShell** | Deja ciega `H-5`. Y conviene conocer la medición: **en menos del 5 % de los servicios prestados por el proveedor especializado en entornos de operación estaba habilitado el registro de ejecución de PowerShell** |
| **Sin inventario de fin de vida del equipamiento de red** | No es de visibilidad sino de gestión, y es la que permite el reclutamiento: **el aviso de abril de 2026 señala que estos equipos se comprometen porque están fuera de soporte y ya no reciben actualizaciones** |

---

# NIVEL TÉCNICO
### Para: Ingeniería de detección · Automatización · TIP/SIEM · Redes · Vida útil: meses

## X-1. Arsenal y capacidad

| Propiedad | Valor |
|---|---|
| Malware propio en la víctima | **Ninguno, y es el rasgo definitorio.** La posexplotación es línea de comandos con binarios del sistema. Lo único no nativo son clientes de proxy inverso, una utilidad de volcado de credenciales, un conjunto de manipulación de protocolos y una herramienta forense de captura de memoria |
| Acceso inicial | Vulnerabilidades en **Fortinet, Ivanti, NETGEAR, Citrix y Cisco**, con código público **y con días cero propios**. En un caso confirmado, `CVE-2022-42475` en un cortafuegos sin parchear, con evidencia de desbordamiento en los registros de caída del servicio de VPN |
| Días cero documentados | **Cuatro confirmados y uno probable, todos contra plataformas de gestión:** un gestor unificado de puestos *(probable, >30 víctimas, decae tras las actualizaciones de octubre de 2025)*; un orquestador de SD-WAN *(2024)*; una plataforma de administración remota de proveedores de servicio *(dos vulnerabilidades encadenadas, 2025)*; un segundo orquestador de SD-WAN *(explotado desde finales de 2025, divulgado en febrero de 2026, puntuación 10.0)*; y un tercero *(divulgado en julio de 2026, puntuación 10.0)* |
| Plataformas vistas atacar | Fortinet · Cisco · ManageEngine · Ivanti · F5 · Check Point · Palo Alto · ServiceNow · **ArcGIS**, según la telemetría de red troncal, sin poder determinar siempre si el acceso usó vulnerabilidad conocida o no divulgada |
| Credenciales | **`NTDS.dit` + rama `SYSTEM`** por copia de volumen, con `vssadmin` y `ntdsutil` vía `wmic`; rotura **fuera de línea**. Volcado de la memoria del proceso de autenticación con **`comsvcs.dll` antiguo en carpeta no estándar** y `MiniDump`. Utilidad pública de volcado de credenciales por escritorio remoto. Conjunto público de manipulación de protocolos. Datos del navegador del administrador, **incluida la clave de descifrado local** |
| Descubrimiento | `cmd` · `certutil` · `dnscmd` · `ldifde` · `makecab` · `net user/group/use` · `netsh` · `nltest` · `netstat` · `ntdsutil` · `ping` · `PowerShell` · `quser` · `reg query/save` · `systeminfo` · `tasklist` · `wevtutil` · `whoami` · `wmic` · `xcopy`. Y un escáner comercial **que ya estaba en la red para uso de administración** |
| Persistencia | **Credenciales válidas, nada más.** Reextracción periódica de la base de datos del directorio para que el acceso no caduque |
| Mando y control | Proxy multisalto sobre la cadena de `O-3.B` · **`netsh portproxy`** sobre un servidor de monitorización de la víctima · clientes de proxy inverso libre empaquetados con UPX, con retrollamadas fijas a los puertos **8080, 8443, 8043, 8000 y 10443** · variantes con `Earthworm` · túneles inversos con proxys libres *(2026)* |
| Antiforense | Borrado **selectivo** de registros de eventos y de sistema · borrado de ficheros intermedios · suplantación de nombres · **limpieza completa de la cadena de retransmisión al terminar cada sesión** · copia de metadatos de ficheros de referencia *(2026)* |
| Red de retransmisión | **>27 clases de dispositivo** con **papel fijo por tipo**: módems **Intelbras** sólo como relé extranjero, equipos de malla de otro fabricante sólo como salto final en el país de la víctima. TP-Link, Ruckus, SATO, NETGEAR, Zyxel, Cambium como rotación inicial; Fortinet, Cisco, plataformas de monitorización, servidores de integración sanitaria y paneles de hospedaje como capa de empresa de **uno a tres meses** |
| Red de reconocimiento | **>1.500 dispositivos** —Cisco RV320/RV325 en su mayoría, más Araknis, Mimosa, Ubiquiti, DrayTek, Hikvision, Linksys—, con binarios **MIPS, MIPS64 y MIPSEL**, proceso `auditdy`, gestión por **servicios ocultos de Tor**, tareas cifradas con **clave AES fija**, escaneo SYN con **puerto de origen fijo 19000** y sondeo ICMP con **identificador 19037 y secuencia 35765** |
| Familia de implantes del orquestador *(2026)* | Módulo residente en memoria inyectado por `ptrace` **en el proceso legítimo del demonio del plano de control**; interposición de `recvfrom`, `sendto`, `getpeername`, `dlopen`, `dlsym` y `mprotect`; **sin dirección, puerto, dominio ni intervalo fijos** —el mando llega **en banda, por el propio tráfico del plano de control**—; comprobación de que el resumen MD5 de la fecha enviada por el mando coincide con la fecha local **antes de ejecutar nada**; módulo de recolección que engancha `SSL_read` y extrae **material de clave simétrica del plano de datos** de los mensajes de control descifrados, lo cifra con clave pública y lo deja en un fichero de puesta en escena |
| Actividad en entornos de operación *(2025)* | Pasarelas celulares industriales por **interfaz web en los puertos 9191 y 9443** · enumeración de pasarelas de acceso remoto y concentradores de VPN de cuatro fabricantes · **modificación de software de puesto de ingeniería** para extraer configuración y datos de alarma **y averiguar qué dispara una parada de proceso** · exfiltración de **datos de sistemas de información geográfica, diagramas de red de operación y procedimientos operativos** |
| Horario | **Lunes a viernes, 09:00–22:00 hora estándar de China**, con picos a media mañana, media tarde y noche, y **pausas de varias semanas en el Año Nuevo chino** |

### X-1.1 — Lo que no hay, y es la clave de la detección

No hay: familia de malware propia desplegada en la víctima; cifrado ni destrucción; mecanismo de persistencia distinto de una cuenta; canal de mando y control fijo; dominio propio que bloquear; ni infraestructura durable.

**Este adversario no tiene nada que un producto de endpoint pueda detectar como malicioso**, y no por casualidad: **el aviso conjunto declara expresamente que los indicadores de compromiso convencionales asociados a esta actividad son, en general, escasos**, lo que complica identificar, seguir y clasificar esta clase de conducta. La consecuencia operativa es que la detección tiene que ser de **comportamiento, de procedencia y de configuración**: un patrón de uso de utilidades legítimas sobre un controlador de dominio; una autenticación correcta desde una red donde no tenemos a nadie; una plataforma de gestión accesible desde Internet. De ahí que en este informe **`X-5` y `T-5` pesen más que `X-3`**, y que `X-3` tenga sólo seis reglas: son las seis que cubren algo real.

## X-2. Artefactos persistentes

<!-- cti:cards -->

| Categoría | Artefactos | Etiqueta |
|---|---|---|
| **Copia de la base de datos del directorio** | Eventos del motor de almacenamiento de Windows **`216`, `325`, `326`, `327`, `637`** · directorios `C:\Windows\Temp\tmp\Active Directory` y `...\registry` · `C:\Users\Public\pro` · `C:\Windows\Temp\McAfee_Logs` | `el artefacto más valioso` |
| **Binarios del sistema fuera de su sitio** | `comsvcs.dll` fuera de `System32` · `WmiPrvSE.exe` fuera de su ruta · ejecutables aleatorios con el patrón `C:\Windows\[a-zA-Z]{8}.exe` | `regla corta` |
| **Ficheros de reconocimiento** | `user.dat` y `systeminfo.dat` en `C:\Users\Public\Documents` · **`rult3uil.log` en `C:\Windows\System32\`** · `History.zip` en `Downloads` · `logins.ps1` | `muy específicos` |
| **Rutas de puesta en escena** | `C:\Users\Public\Appfile` · `C:\PerfLogs` · `C:\Windows\Temp`, con subdirectorios | `las tres de siempre` |
| **Nombres suplantados** | `SMSvcService.exe` · `Brightmetricagent.exe` · `cisco_up.exe` · `vm3dservice.exe` · `watchdogd.exe` · `WmiPreSV.exe` · `cl64.exe` · `Win.exe` · `nc.exe` · `billagent.exe` · `billaudit.exe` · `ronf.exe` · `rdpservice.exe` | `antiguos, pero gratis de buscar` |
| **Proxy de puertos** | Clave de registro de proxy de puertos · `netsh interface portproxy add/delete v4tov4` · puertos a la escucha sin servicio asociado | `casi sin falsos positivos` |
| **Equipos de borde** *(2026)* | **Servicio de SSH en puerto no estándar** · clave autorizada no inventariada · usuario nuevo en el firmware · **y la propiedad que hay que asumir: todo esto se borra al terminar la sesión** | `la mitad que nadie mira` |
| **Plano de control** *(2026)* | Guion de servicio del sistema de arranque modificado · servicio con nombre del componente de autenticación **como ELF compilado donde debería haber un paquete interpretado** · biblioteca inyectada en el proceso del demonio · fichero de puesta en escena en `/var/tmp` · clave autorizada para la cuenta de administración de la plataforma · **eventos de emparejamiento con origen o tipo de nodo incoherente** | `la aportación de 2026` |

## X-3. Lógica de detección prioritaria

<!-- cti:detections -->

**D-1 · CRÍTICO — Copia de la base de datos de Active Directory**

```
(eventlog == "Application" AND provider == "ESENT"
 AND event_id IN (216, 325, 326, 327, 637)
 AND message CONTAINS_ANY ("ntds.dit", "ntds.jfm"))
OR (process.cmdline MATCHES "(?i)vssadmin.*create shadow")
OR (process.cmdline MATCHES "(?i)ntdsutil.*(ac i ntds|activate instance ntds).*(ifm|install from media)")
OR (process.cmdline MATCHES "(?i)wmic.*process call create.*ntdsutil")
```

→ **Contención automática en controladores de dominio.** Es la detección de mayor valor del informe: cubre **el único paso del expediente que deja una traza fiable**. Si acierta, la recomendación oficial es **asumir compromiso total del dominio** —no del equipo— con todo lo que eso implica, incluido restablecer dos veces la cuenta de servicio de tiques Kerberos respetando la replicación entre ambos restablecimientos. **Y la condición de operación: si esta regla no se puede escribir porque no se conserva el registro de aplicación de los controladores, eso es la primera brecha de `T-5` y hay que cerrarla antes que cualquier otra cosa.**

**D-2 · CRÍTICO — Autenticación remota correcta desde un origen que no corresponde**

```
auth.success
WHERE service IN ("vpn","remote_access","admin_portal","sdwan_manager")
  AND NOT source.ip IN <lista de permisión de rangos propios y de teletrabajo enumerado>
  AND (source.network.type IN ("consumer_broadband","mobile_carrier","hosting")
       OR source.asn NOT IN <ASN esperados>)
```

→ **Alerta crítica y verificación con el usuario por un canal distinto.** No es una detección de malware: es una **detección de procedencia**, y es la única que ve el último salto de una cadena desechable. **La lista de permisión es la mitad eficaz de la regla**; con lista de denegación esta detección no funciona, porque las direcciones caducan en horas. Complementar con viaje imposible y con duración anómala de sesión, que el aviso de 2024 pide expresamente para este actor.

**D-3 · CRÍTICO — Binario del sistema fuera de su directorio, en un controlador de dominio**

```
(file.name IN ("comsvcs.dll","WmiPrvSE.exe","svchost.exe","lsass.exe")
 AND file.path NOT MATCHES "(?i)^C:\\\\Windows\\\\(System32|SysWOW64|WinSxS)\\\\")
OR file.path MATCHES "(?i)^C:\\\\Windows\\\\[a-zA-Z]{8}\\.exe$"
OR (file.path MATCHES "(?i)^C:\\\\(Users\\\\Public|PerfLogs|Windows\\\\Temp)\\\\"
    AND file.extension IN ("exe","dll"))
```

→ **Contención automática en servidores; alerta alta en puestos.** Regla corta, fidelidad muy alta y cobertura muy superior a este expediente. El patrón de ocho caracteres aleatorios en `C:\Windows\` lo publica el aviso de 2023 como formato de nombre usado por el actor.

**D-4 · ALTO — Proxy de puertos creado o borrado**

```
process.cmdline MATCHES "(?i)netsh\s+interface\s+portproxy\s+(add|delete)\s+v4tov4"
OR registry.key MATCHES "(?i)\\\\Services\\\\PortProxy\\\\v4tov4\\\\tcp"
```

→ **Alerta alta e investigación del servidor.** **Incluir el borrado es deliberado:** el actor también retira el proxy, y en un parque gestionado nadie usa esta función. De todas las reglas del informe, la de menor tasa de falsos positivos.

**D-5 · ALTO — Reconocimiento de inicios de sesión y borrado de registros**

```
(process.cmdline MATCHES "(?i)(Get-EventLog|Get-WinEvent).*(4624|instanceid 4624)"
 AND host.role == "domain_controller")
OR (process.cmdline MATCHES "(?i)Out-File.*\\\\(Users\\\\Public|Windows\\\\Temp)\\\\.*\\.dat")
OR (event_id == 1102)
```

→ **Alerta alta, y el evento `1102` siempre se investiga.** El aviso es explícito: los registros de seguridad **no se borran solos** y este actor los borra. La primera condición detecta el reconocimiento que le permite imitar nuestro horario, que es la razón por la que las alertas de actividad anómala no se disparan después.

**D-6 · ALTO — Proxy inverso libre, por su cadena fija**

```
file.content CONTAINS "github.com/fatedier/frp/cmd/frpc"
AND (file.content CONTAINS "MAGA2024!!!"            // variante propia del actor
     OR file.content CONTAINS "HTTP_PROXYHost: %s")
OR (network.connection.dest_port IN (8000,8043,8080,8443,10443)
    AND process.name IN <nombres suplantados del Anexo A.2>)
```

→ **Alerta alta; concluyente si aparece la cadena fija.** La cadena de nueve caracteres con contenido político **no existe en el proyecto original** y la publica el aviso de 2023 en su propia regla de reconocimiento: un ejecutable que la contenga no admite explicación alternativa. **Pero cuidado con la atribución:** el proyecto libre lo usan también los clústeres de `CTI-2026-033` y `CTI-2026-043`, de modo que la detección del proyecto **no atribuye** y sólo la cadena propia lo hace.

> ⚠ **Regla de operación, y una advertencia sobre lo que estas seis reglas no
> cubren.** Tres admiten contención automática: `D-1` y `D-3` en servidores por
> fidelidad, y `D-5` sólo como alerta porque el borrado de registros ya ocurrió
> cuando se detecta. Y lo que hay que decir en voz alta: **ninguna de las seis
> detecta las etapas 00 y 01 de `T-1`**. La cadena de retransmisión no pasa por
> nuestros sensores y el día cero contra un plano de control no tiene firma
> antes de existir. **Contra esas dos etapas no hay detección: hay reducción de
> exposición, y está en `X-5`.** Si el programa de seguridad de la organización
> está construido enteramente alrededor de la detección, este expediente lo
> atravesará por delante.

## X-4. Consultas de caza

```kql
// H-1 y D-1 · Copia de NTDS.dit. La caza de mayor valor del informe.
// El aviso recomienda mirar el registro de APLICACION porque dura mas que
// el de seguridad, y asumir permanencia significativa. Ventana: toda.
union
( DeviceEvents
  | where ActionType == "WindowsEventLog"
  | where AdditionalFields has_any ("ESENT")
  | where AdditionalFields has_any ("216","325","326","327","637")
  | where AdditionalFields has_any ("ntds.dit","ntds.jfm")
  | project Timestamp, DeviceName, Senal = "ESENT: copia de NTDS", AdditionalFields
),
( DeviceProcessEvents
  | where ProcessCommandLine has_all ("vssadmin","create","shadow")
     or (ProcessCommandLine has "ntdsutil" and ProcessCommandLine has_any ("ifm","install from media"))
     or (ProcessCommandLine has_all ("wmic","process call create") and ProcessCommandLine has "ntdsutil")
  | project Timestamp, DeviceName, Senal = "cmdline: volcado de directorio", AccountName, ProcessCommandLine
)
| order by Timestamp asc
// Un solo acierto en un controlador de dominio => asumir compromiso total
// del dominio, no del equipo.
```

```kql
// H-2 y D-2 · Procedencia de las autenticaciones remotas correctas.
// La deteccion del ULTIMO SALTO de la cadena. No busca malware: busca origen.
let ventana = 365d;
let rangos_propios = dynamic(["<prefijos propios>","<rangos de sede>"]);
SigninLogs
| where TimeGenerated > ago(ventana)
| where ResultType == 0
| where AppDisplayName has_any ("VPN","Remote","Portal") or ConditionalAccessStatus != "notApplied"
| extend ASN = tostring(AutonomousSystemNumber)
| where not(ipv4_is_in_any_range(IPAddress, rangos_propios))
| summarize Accesos = count(), Cuentas = make_set(UserPrincipalName, 20),
            Primero = min(TimeGenerated), Ultimo = max(TimeGenerated)
         by IPAddress, ASN, Pais = tostring(LocationDetails.countryOrRegion)
| order by Accesos asc
// Mirar PRIMERO las filas con pocos accesos: una cadena desechable produce
// una o dos autenticaciones desde una direccion que no vuelve a aparecer.
// Clasificar el ASN: banda ancha de consumo, operador movil ajeno y
// hospedaje no contratado son los tres tipos que no deberian aparecer.
```

```kql
// H-5 y D-5 · Reconocimiento de inicios de sesion y borrado de registros.
union
( DeviceProcessEvents
  | where ProcessCommandLine has_any ("Get-EventLog","Get-WinEvent")
  | where ProcessCommandLine has_any ("4624","instanceid 4624")
  | project Timestamp, DeviceName, Senal = "reconocimiento de logons", ProcessCommandLine
),
( DeviceProcessEvents
  | where ProcessCommandLine has "Out-File"
  | where ProcessCommandLine has_any (@"\users\public", @"\windows\temp")
  | project Timestamp, DeviceName, Senal = "volcado a fichero .dat", ProcessCommandLine
),
( DeviceEvents
  | where ActionType == "SecurityLogCleared"
  | project Timestamp, DeviceName, Senal = "EVENTO 1102: registro borrado", AdditionalFields
)
| order by Timestamp desc
// El 1102 se investiga SIEMPRE: los registros no se borran solos.
```

```bash
#!/bin/sh
# H-10 y E-c · Somos trayecto? Vista externa del propio borde.
# Esta no es una consulta de seguridad: es un inventario, y lo hace Redes.
# Lo que se busca no es un ataque contra nosotros: es un salto de la cadena
# de alguien.

RANGOS="<prefijos propios anunciados, incluidos los de sedes y los de servicio>"

echo "== interfaces de administracion de equipos de borde visibles desde Internet =="
nmap -Pn -sS -p 22,23,80,443,8080,8443,9191,9443,7547 --open $RANGOS 2>/dev/null \
  | grep -E "Nmap scan report|open"

echo
echo "== SSH en puertos no estandar: el artefacto de la cadena mientras dura =="
nmap -Pn -sV -p 2222,2022,8103,14737,22000-22100 --open $RANGOS 2>/dev/null \
  | grep -E "Nmap scan report|ssh"

echo
echo "== pasarelas celulares industriales (puertos documentados) =="
nmap -Pn -p 9191,9443 --open $RANGOS 2>/dev/null | grep -E "Nmap scan report|open"

# Y LAS CUATRO PREGUNTAS QUE NO RESPONDE NINGUN ESCANER:
#   1. Cuantos de estos equipos estan fuera de soporte del fabricante?
#      (es la condicion que permite el reclutamiento, segun el aviso de
#       abril de 2026)
#   2. Quien los administra, y estan en el inventario?
#   3. Gestionamos equipos en casa de clientes con esta misma exposicion?
#   4. Conservamos su trafico saliente? Un rele no nos habla: habla DESDE
#      nosotros hacia un tercero.
#
# ADVERTENCIA HONESTA: si la cadena se limpio al terminar la sesion, no habra
# nada que encontrar. Lo que queda, y es lo que hay que cerrar, es la
# condicion que lo hizo posible.
```

```yaml
# Sigma — Copia de la base de datos de Active Directory
title: Copia de NTDS.dit mediante copia de volumen o ntdsutil
id: 4a1c7e96-3d52-4f81-9b27-6ac0d5f1e3b8
status: stable
description: >
  Unico paso del expediente de este actor que deja una traza fiable y
  especifica. El aviso conjunto AA24-038A recomienda vigilar los eventos del
  motor de almacenamiento de Windows porque permanecen mas tiempo que los
  registros de seguridad, y asumir permanencia significativa.
author: Celula CTI
date: 2026-11-18
references:
  - https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a
  - https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a
tags:
  - attack.credential_access
  - attack.t1003.003
  - attack.defense_evasion
  - attack.t1006
logsource:
  product: windows
  category: process_creation
detection:
  vss:
    CommandLine|contains|all:
      - 'vssadmin'
      - 'create shadow'
  ntdsutil_largo:
    CommandLine|contains|all:
      - 'ntdsutil'
      - 'activate instance ntds'
  ntdsutil_corto:
    CommandLine|contains|all:
      - 'ntdsutil'
      - 'ac i ntds'
  ifm:
    CommandLine|contains:
      - 'ifm'
      - 'install from media'
      - 'create full'
  condition: vss or ((ntdsutil_largo or ntdsutil_corto) and ifm)
falsepositives:
  - Promocion legitima de controlador de dominio y procedimientos de
    recuperacion. Son contados y documentables: enumerarlos nominalmente.
level: critical
```

```yaml
# Sigma — Proxy de puertos nativo creado o retirado
title: netsh portproxy usado para convertir un servidor en proxy
id: 9f3b5d04-8c17-4a6e-bd92-70e4a1c8f255
status: stable
description: >
  El actor convierte un servidor de la victima en proxy de su mando y control
  con una funcion nativa de Windows. Se incluye el borrado porque el actor
  tambien retira el proxy y el borrado es igual de delator.
author: Celula CTI
date: 2026-11-18
tags:
  - attack.command_and_control
  - attack.t1090.001
  - attack.defense_evasion
  - attack.t1112
logsource:
  product: windows
  category: process_creation
detection:
  netsh:
    CommandLine|contains|all:
      - 'netsh'
      - 'portproxy'
      - 'v4tov4'
  condition: netsh
falsepositives:
  - Practicamente ninguno en un parque gestionado. Si aparece, es un hallazgo
    de configuracion aunque no sea este actor.
level: high
```

## X-5. Mitigaciones de configuración con efecto directo

**Esta sección es, en este informe, más importante que la de detección**, y por una razón que no es ideológica sino aritmética: de las cuatro etapas de `T-1`, **dos no son detectables con nuestros sensores** y sólo se cierran reduciendo exposición.

| Control | Corta |
|---|---|
| **Retirar de Internet las interfaces de administración y los planos de control de las plataformas de gestión** | **La etapa 01 por la vía de 2026, que es la que no se puede parchear a tiempo.** Las cinco campañas de día cero fueron contra esta clase de objetivo |
| **Lista de permisión —no de denegación— para el acceso remoto corporativo**, con perfilado de origen por tipo de red | **La etapa 00 completa, que es lo único que la alcanza.** Es la primera recomendación del aviso conjunto de abril de 2026, y la única medida de este informe que convierte una cadena indetectable en un hecho visible |
| **No almacenar credenciales en dispositivos de borde, y verificar que ninguna cuenta del dispositivo da acceso de administrador de dominio** | **El puente entre la etapa 01 y la 02.** Es literalmente lo que ocurrió en un compromiso confirmado: una cuenta de administrador de dominio guardada en un cortafuegos |
| **Doble factor resistente a suplantación en todo acceso remoto**, incluidos proveedor, operación y administración de plataformas | La etapa 01 por la vía de credenciales, y la reutilización del acceso tras el volcado del directorio |
| **Plan de fin de vida del equipamiento de red**, con sustitución del material sin soporte | **Es la medida que nos quita del papel de trayecto.** El aviso de abril de 2026 señala que estos equipos son reclutables **porque están fuera de soporte y ya no reciben parches**. Es `E-c` |
| **Conservar los registros de las plataformas de gestión fuera de la propia plataforma** | **El antiforense de la etapa 03.** Un actor que compromete el plano de control puede borrar los registros que viven en él; la directiva de emergencia estadounidense obliga por eso a almacenarlos externamente |
| **Conservar el registro de aplicación de los controladores de dominio, con retención larga** | Hace posible `D-1`. **Es la medida de una línea con mejor retorno del informe**, porque esos eventos sobreviven cuando los de seguridad ya no están |
| **Separar las cuentas administrativas y prohibir el almacenamiento de contraseñas en el navegador en equipos de administración** | La recolección de la etapa 02 contra el navegador del administrador de red, **incluida la clave que descifra sus contraseñas** |
| **Segmentar informática y operación, con paso obligado por un intermediario vigilado**, y **sacar de Internet las pasarelas celulares, los HMI y la telemetría de campo** | La escalada de 2025: la pasarela celular es el camino documentado hacia la red de operación, **y crea una vía que salta el perímetro sin pasar por él** |
| **Telemetría de la frontera informática–operación y de las pasarelas de acceso remoto, conservada** | No corta ninguna etapa: **hace posible investigar.** Es `E-d`, y sin ella la pregunta de `KJ-7` seguirá sin respuesta |
| **Retirar de Internet los servidores geoespaciales innecesarios, y asumir que lo ya exfiltrado está perdido** | El objetivo de colección de `KJ-6`. **La segunda mitad no es una medida técnica sino de diseño: si el adversario conoce nuestra topología, hay que diseñar como si la conociera** |
| **Planificar la recuperación suponiendo compromiso total del dominio** | No es prevención: es la consecuencia de `D-1`. La recomendación oficial incluye restablecer **dos veces** la cuenta de servicio de tiques Kerberos, respetando la replicación entre ambos restablecimientos |

---

## 14. Brechas de inteligencia y nuevos requisitos de colección

| # | Brecha | Impacto en el juicio | Requisito propuesto | Prioridad |
|---|---|---|---|---|
| G-1 | **No hay ninguna fuente regional sobre este actor**, ni víctimas, ni nodos de su infraestructura, ni firmantes latinoamericanos en ninguno de los tres avisos | `KJ-4` y el supuesto clave descansan en ausencia de evidencia **en una región con poca capacidad de detección**. Es la debilidad estructural del informe | Consultar a los CSIRT nacionales de la región si han visto **tráfico saliente de equipos de borde propios hacia la infraestructura descrita**, que es la pregunta correcta para esta geografía y que nadie está haciendo | **Crítica** |
| G-2 | **`KJ-5` es inferencia sobre un agregado, no un caso** | Que los módems de un fabricante brasileño tengan papel fijo de relé no prueba que haya nodos en la región | Pedir a los operadores regionales y al fabricante **si han observado compromiso de ese material con servicios de SSH anómalos**. Y vigilar `I-4` | Alta |
| G-3 | **Dos designaciones de Talos sobre el mismo día cero y la misma plataforma, con relación no declarada** | `H8` queda en solapamiento. Si `UAT-8616` y `UAT-11473` fueran el mismo y fueran este actor, la ventana de explotación del día cero se extendería **a 2023** con confianza mayor | Vigilar `I-7`. **Y no componer mientras tanto**, que es la regla de esta cartera | Media |
| G-4 | **Las cinco campañas de día cero proceden de una sola fuente de proveedor** | `KJ-2` queda en confianza moderada-alta. Está corroborada indirectamente —directiva de emergencia, catálogo oficial— pero el relato lo sostiene un solo actor con visibilidad única | Buscar corroboración gubernamental. **Y entretanto actuar sobre el mecanismo, no sobre el actor**: `E-a` es correcta aunque la atribución falle | Alta |
| G-5 | **No hay detalle público del vector de las pasarelas celulares ni del software de puesto de ingeniería modificado** | La escalada de 2025, que es el dato más grave del informe, se conoce por descripción y no por análisis. No hay indicadores | Solicitar al fabricante de las pasarelas y al proveedor que lo documentó el detalle técnico y los indicadores, si existen | Alta |
| G-6 | **No hay información técnica pública del incidente chileno de Huatacondo a casi tres meses** | `KJ-7` descansa en la ausencia misma. **Y la discrepancia de fechas entre fuentes —26 o 27 de agosto— sin resolver es un síntoma, no un detalle** | Vigilar la respuesta a la solicitud parlamentaria y las publicaciones del operador del sistema y del regulador sectorial. `I-5` | **Crítica para la región** |
| G-7 | **Sin telemetría propia y sin inventario de equipos de borde propios y de cliente** | `O-4` sin evaluar, y **el primer bloque del cuestionario no lo puede responder Seguridad**: lo tiene que responder Redes | `E-c`, que antes que una medida técnica es **una conversación con Redes y con el área de servicio** | **Crítica** |
| G-8 | **No se ha medido si nuestros registros permitirían ejecutar `D-1` y `D-2`** | Las dos detecciones de mayor valor del informe pueden ser inescribibles en nuestra casa, y no lo sabemos | Comprobarlo esta semana: ¿hay registro de aplicación de controladores de dominio con retención larga? ¿Clasificamos el origen de las autenticaciones remotas? | Alta |
| G-9 | **La contranarrativa china no es verificable ni refutable en su totalidad** | `H10` está descartada por falta de evidencia del refutador, no por refutación positiva. **Es una asimetría incómoda y conviene consignarla** | Ninguno accionable. Se consigna para que el informe no aparente una certeza que no tiene sobre la motivación última | Baja |

---

# ANEXOS

## Anexo A — Indicadores de compromiso

> ⚠ **Leer antes de usar. Cuatro advertencias, y la segunda es la más
> importante de todo el anexo.**
>
> **Primera, de procedencia.** Los dos avisos conjuntos publican **su propio
> paquete STIX 2.1**, y `AA24-038A` publica además un informe de análisis de
> malware con sus indicadores. **Esa es la fuente preferente para ingesta
> automática.** Lo que sigue es una selección razonada con fecha, para lectura
> humana y para el índice con contexto de este repositorio, y está subordinada
> al original. Es el mismo criterio que `CTI-2026-030` y `CTI-2026-034`.
>
> **Segunda, y es una decisión de producto que conviene entender: este anexo no
> contiene las direcciones de la cadena de retransmisión, y la omisión es
> deliberada.** Esas direcciones son **equipos domésticos y de pequeña empresa
> de terceros inocentes** —el router de una casa, la cámara de una tienda—
> comprometidos, usados durante una sesión de cuatro horas y limpiados al
> salir. Publicarlas tendría dos efectos y ninguno bueno: **no protegerían a
> nadie**, porque caducan antes de que una lista de bloqueo se despliegue, y
> **cortarían tráfico legítimo de las víctimas del compromiso**. El aviso
> conjunto de abril de 2026 recoge el nombre del problema —**extinción de
> indicadores**— y la medida que sí funciona, que no es una lista de bloqueo
> sino **una lista de permisión**: está en `D-2` y en `X-5`. Esta es la
> conclusión extrema del aviso que la portada de este repositorio lleva sobre
> cargar un `ioc_*.txt` sin filtrar.
>
> **Tercera, de prioridad.** Como en `CTI-2026-033` y `CTI-2026-034`, **el
> nivel más valioso de este anexo no son los indicadores de red: es `A.1`**, y
> aquí con un matiz propio. `A.1` tiene **dos mitades que exigen acciones
> distintas**: vulnerabilidades que tenían parche disponible cuando se usaron
> —gestión de parches— y vulnerabilidades que **no existían públicamente
> cuando se usaron** —reducción de exposición—. Mezclarlas produce la ilusión
> de que parchear basta.
>
> **Cuarta, sobre los hashes.** Hay treinta y uno, más dos resúmenes MD5 de los mismos ficheros, y casi todos son de 2023.
> Van con acción `Solo retrohunt` sin excepción. **Y el dato que los pone en su
> sitio: el informe técnico de octubre de 2026 sobre la familia de implantes de
> 2026 no publica ni un hash** — publica rutas, nombres de módulo y reglas de
> red. El sector ya ha dejado de esperar valor de esta capa frente a este
> adversario.

### A.1 — Vulnerabilidades · **leer la división en dos mitades**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| cve | `CVE-2022-42475` | **Fortinet FortiOS.** Desbordamiento de montículo en el servicio de VPN. **Vía de acceso probable en un compromiso confirmado, sobre un cortafuegos perimetral sin parchear**, con evidencia en los registros de caída del servicio. En el catálogo oficial de explotadas desde 2022-12-13. **Primera mitad: tenía parche** | Alta | Sin caducidad: la decisión es de parcheo | **Parchear, y rotar credenciales si el dispositivo estuvo expuesto** |
| cve | `CVE-2021-40539` · `CVE-2021-27860` | **ManageEngine ADSelfService Plus** y **FatPipe WARP/IPVPN/MPVPN.** Las dos que `AA23-144A` nombra expresamente como explotadas por este actor. **Primera mitad: tenían parche** | Alta | Sin caducidad | **Parchear y verificar** |
| cve | `CVE-2025-0994` | **Trimble Cityworks**, software de gestión de activos **basado en información geográfica**. Deserialización insegura en IIS, ejecución remota **sin autenticación**. Explotada a principios de 2025 con un cargador libre en Rust. En el catálogo oficial desde 2025-02-07. **Es `KJ-6` y la razón de `E-e`** | Alta | Sin caducidad | **Parchear, retirar de Internet, y asumir el dato ya exfiltrado como perdido** |
| cve | `CVE-2024-39717` | **Versa Director**, primer orquestador de SD-WAN. Subida de fichero de tipo peligroso. **Día cero documentado públicamente en 2024**; tras la explotación, interfaz web residente en memoria para minimizar la traza forense. En el catálogo oficial desde 2024-08-23. **Segunda mitad: era día cero** | Alta | Sin caducidad | **Parchear. Y revisar el plano de control, no sólo la versión** |
| cve | `CVE-2025-8875` · `CVE-2025-8876` | **N-able N-central**, plataforma de administración remota usada por proveedores de servicio. **Cadena de dos vulnerabilidades no divulgadas previamente**: deserialización insegura e inyección de comandos. En el catálogo oficial desde 2025-08-13. **Un compromiso aquí alcanza a cientos o miles de activos de clientes** | Alta | Sin caducidad | **Parchear, y exigir notificación contractual al proveedor** (`E-f`) |
| cve | `CVE-2026-20127` | **Cisco Catalyst SD-WAN Controller y Manager.** Elusión de autenticación, **puntuación 10.0**, administrador remoto sin autenticar por petición manipulada. **Explotada desde finales de 2025, divulgada el 2026-02-25, y la explotación continuó mucho después del parche.** Motivó la **Directiva de Emergencia `ED 26-03`**. En el catálogo oficial desde 2026-02-25 | Alta | Sin caducidad | **Parchear. Y si hay compromiso de superusuario: reconstruir el plano de control, no limpiarlo** |
| cve | `CVE-2022-20775` | **Cisco SD-WAN.** Recorrido de ruta con escalada a superusuario. **Se usa en combinación con la anterior**, mediante degradación de versión y restauración posterior, para obtener raíz. Añadida al catálogo oficial el **2026-02-25**, cuatro años después de su publicación | Alta | Sin caducidad | **Parchear, y alertar sobre degradaciones de versión no autorizadas** |
| cve | `CVE-2026-16812` | **Arista VeloCloud Orchestrator** local, tercer orquestador de SD-WAN. Inyección de comandos del sistema, **puntuación 10.0 en las dos versiones de la escala**. **Día cero explotado por este actor**; en el catálogo oficial desde 2026-07-27 | Alta | Sin caducidad | **Parchear y retirar de Internet la interfaz de administración** |
| artefacto | **Un gestor unificado de puestos de trabajo, >30 víctimas, vulnerabilidad no identificada** | **Campaña valorada con confianza moderada como día cero**, que decayó tras las actualizaciones de seguridad del fabricante de octubre de 2025. **No hay CVE público asociado.** El actor permaneció en el propio servidor usando sus capacidades administrativas, **sin movimiento lateral** | Media *(confianza moderada declarada por la fuente)* | Sin caducidad | **Vigilancia y reducción de exposición.** No hay nada que parchear con nombre |
| artefacto | **La división de `A.1` en dos mitades: tres vulnerabilidades con parche disponible frente a cinco que eran día cero** | **No es un indicador: es el juicio que ordena la defensa de este informe.** Contra las primeras funciona el ciclo de parcheo —que es lo que `CTI-2026-034` concluyó para otro actor—; contra las segundas sólo funciona reducir exposición y detectar comportamiento. **Es `KJ-2`, `KJ-3` y `E-g`** | Alta | Sin caducidad | **Criterio de priorización** |
| puerto | `9191` · `9443` | **Puertos de la interfaz web de las pasarelas celulares industriales** comprometidas en 2025 en organizaciones de electricidad y de petróleo y gas. **No deberían estar accesibles desde Internet nunca** | Alta | Sin caducidad | **Revisión de exposición** (`X-5`, `O-2` del cuestionario) |
| puerto | `8000` · `8043` · `8080` · `8443` · `10443` | **Puertos de retrollamada fijos de los clientes de proxy inverso** que el aviso de 2023 documenta | Media *(antiguos)* | Caducan con la campaña | **Detección por contexto** (`D-6`) |

### A.2 — Artefactos de host y de plataforma

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| pattern | Eventos del motor de almacenamiento de Windows `216` · `325` · `326` · `327` · `637` con referencia a `ntds.dit` o `ntds.jfm` | **El indicador más valioso de todo el informe.** Delatan, en este orden, el cambio de ubicación de la base de datos del directorio hacia una copia de volumen, la creación de una base nueva en un directorio temporal, el montaje de una base procedente de copia de volumen, su desmontaje y la creación del fichero de mapa de volcado. **Viven en el registro de aplicación, que dura más que el de seguridad** | Alta | **Sin caducidad** | **Detección con contención automática** (`D-1`) |
| pattern | `vssadmin create shadow` · `ntdsutil "ac i ntds" ifm "create full ..."` · `ntdsutil "activate instance ntds" ifm` · `wmic process call create "...ntdsutil..."` | **Procedimiento de extracción de la base de datos del directorio, en forma larga y corta.** El aviso publica las dos notaciones y advierte de que se combinan | Alta | **Sin caducidad** | **Detección** (`D-1`) |
| path | `C:\Windows\Temp\tmp\Active Directory` · `C:\Windows\Temp\tmp\registry` · `C:\Users\Public\pro` · `C:\Windows\Temp\McAfee_Logs` · `C:\Users\Public\Appfile` · `C:\PerfLogs` | **Rutas de puesta en escena documentadas**, incluida una que imita el directorio de registros de un antivirus | Alta | **Sin caducidad** | **Detección** (`D-3`) |
| filename | `rult3uil.log` | **Fichero creado en `C:\Windows\System32\` con la actividad del usuario del sistema comprometido**: títulos de ventana, cambios de foco, pulsaciones y comandos, con marcas de tiempo. **No tiene uso legítimo** | Alta | **Sin caducidad** | **Detección, indicador concluyente** |
| filename | `user.dat` · `systeminfo.dat` · `History.zip` · `logins.ps1` · `ttt.dat` | Ficheros de reconocimiento y de recolección: volcado de eventos de inicio de sesión, información de sistema **que después se borró**, datos del navegador del administrador comprimidos en `Downloads`, y el guion que enumera los controladores de dominio | Alta | **Sin caducidad** | **Detección** (`D-5`, `H-9`) |
| filename | `comsvcs.dll` **fuera de `C:\Windows\System32`** | **Versión antigua de una biblioteca legítima de Windows**, descargada a una carpeta no estándar de un controlador de dominio para volcar la memoria del proceso de autenticación. El indicador no es el nombre: **es el nombre fuera de su sitio** | Alta | **Sin caducidad** | **Detección con contención automática** (`D-3`) |
| filename | `SMSvcService.exe` · `Brightmetricagent.exe` · `cisco_up.exe` · `vm3dservice.exe` · `watchdogd.exe` · `WmiPreSV.exe` · `cl64.exe` · `Win.exe` · `nc.exe` · `billagent.exe` · `billaudit.exe` · `ronf.exe` · `rdpservice.exe` · `backup.bat` · `update.bat` · `update.exe` | **Nombres suplantados documentados**, varios imitando servicios de Windows y de fabricantes de red. `ronf.exe` es probablemente una copia renombrada de la utilidad de compresión | Media *(antiguos; el patrón vale más que los nombres)* | Caducan con la campaña | **Solo retrohunt y detección por contexto** |
| pattern | `C:\Windows\[a-zA-Z]{8}.exe` | **Formato de nombre aleatorio** que el aviso de 2023 documenta para ejecutables de este actor. **Es más duradero que los nombres concretos** | Alta | **Sin caducidad** | **Detección** (`D-3`) |
| pattern | `netsh interface portproxy add v4tov4` · `netsh interface portproxy delete v4tov4` · clave de registro del proxy de puertos | **Conversión de un servidor de la víctima en proxy del mando y control.** Se incluye el borrado porque el actor también retira el proxy. **Casi sin uso legítimo en un parque gestionado** | Alta | **Sin caducidad** | **Detección** (`D-4`) |
| pattern | `cmd.exe /Q /c * 1> \\127.0.0.1\ADMIN$\__*.*>&1` · `cmd.exe /C dir /S \\* >> *` · `powershell start-process -filepath c:\windows\temp\*.exe -windowstyle hidden` | **Patrones de línea de comandos** que el aviso de 2023 publica como característicos. El primero es el patrón de ejecución remota de la herramienta pública de manipulación de protocolos | Alta | **Sin caducidad** | **Detección** |
| clave | `MAGA2024!!!` | **Cadena fija presente en la variante propia del actor del cliente de proxy inverso, y ausente del proyecto libre original.** Publicada en la regla de reconocimiento del aviso de 2023. **Un ejecutable que la contenga no admite explicación alternativa** | Alta | **Sin caducidad mientras no se recompile** | **Detección, indicador concluyente** (`D-6`) |
| useragent | `Mozilla/5.0 (Windows NT 6.1; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0` | Cadena de agente de usuario observada en actividad de reconocimiento. **El indicador real es el espaciado anómalo** que el aviso documenta: tres tabuladores y cuatro espacios entre el paréntesis de cierre y la palabra siguiente | Media | Caduca con la campaña | **Solo retrohunt** |
| path | `/etc/sv/sshd/run` · `/etc/sv/aaamgr/` · `/tmp/system-vdaemon` · `/var/tmp/vdaemon.bin` · `/var/tmp/vdaemon.conf` · `/rootfs.rw` remontado como ejecutable | **Artefactos de la familia de implantes del orquestador de SD-WAN (2026):** guiones de servicio del sistema de arranque modificados, lista de identificadores del proceso del demonio, fichero cifrado de puesta en escena del material de clave, **y su fichero de configuración, que el implante borra tras leerlo** | Alta | **Sin caducidad mientras la plataforma no cambie** | **Detección e investigación forense** (`H-3`) |
| filename | `libdssl.so` · `libcommon.so` · `rsshd` · `conf_sshd` · `aaamgrd` | **Nombres de los componentes de esa familia:** módulo residente, módulo de recolección, inyector por `ptrace`, guion de enumeración de procesos y cargador empaquetado. **`aaamgrd` es especialmente delator: el componente legítimo con ese nombre es un paquete interpretado, no un ejecutable compilado** | Alta | **Sin caducidad** | **Detección** (`H-3`) |
| pattern | Enganches de `recvfrom` · `sendto` · `getpeername` · `dlopen` · `dlsym` · `mprotect` · `SSL_read` dentro del proceso del demonio del plano de control | **Mecanismo de intercepción del tráfico del plano de control desde dentro del proceso legítimo.** Sin dirección, puerto ni dominio fijos: **el mando llega en banda**, por el propio tráfico de la plataforma | Alta | **Sin caducidad como técnica** | **Detección por integridad de proceso** |
| pattern | Comprobación de que el resumen MD5 de la fecha local coincide con el enviado por el mando, **antes de ejecutar** · marcadores `40 03 06`, `40 0C 04` y `05 01 0C 06 40` en el tráfico de control descifrado, el último seguido de **32 bytes de material de clave simétrica del plano de datos** | **Dos propiedades de esa familia que valen como firma de comportamiento:** un interruptor temporal que impide el análisis fuera de fecha, y el formato exacto de lo que el actor extrae. **Lo que se roba no son datos: son las claves del plano de datos** | Alta | **Sin caducidad** | **Detección y evaluación de impacto: si acierta, hay que rotar material de clave** |
| pattern | `auditdy` como nombre de proceso · `/dispatch_service/v2/probe_status` · `/dispatch_service/v2/probe_task/` · `/data/v2/pscan` con fichero `attr.json` · puerto de origen fijo `19000` en escaneo SYN · identificador ICMP `19037` y secuencia `35765` | **Artefactos del agente de la red de reconocimiento**, en binarios MIPS para equipos de borde. **Útiles para que un operador o un fabricante detecte sus propios equipos reclutados**, que es la pregunta de `E-c` | Alta | Sin caducidad mientras no cambie la versión | **Detección en equipos de borde** (`H-10`, `H-11`) |
| clave | `0000000000000000bdb718bdf47cbcde` | **Clave simétrica fija de las tareas cifradas** del agente de reconocimiento. Escrita a mano en el binario: no rota | Alta | **Sin caducidad mientras no se recompile** | **Detección** |

### A.3 — Hashes · **todos con la misma acción**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| sha256 | `baeffeb5fdef2f42a752c65c2d2a52e84fb57efc906d981f89dd518c314e231c` · `b4f7c5e3f14fb57be8b5f020377b993618b6e3532a4e1eb1eae9976d4130cc74` · `4b0c4170601d6e922cf23b1caf096bba2fade3dfcf92f0ab895a5f0b9a310349` · `c0fc29a52ec3202f71f6378d9f7f9a8a3a10eb19acb8765152d758aded98c76d` · `d6ab36cb58c6c8c3527e788fc9239d8dcc97468b6999cf9ccd8a815c8b4a80af` · `9dd101caee49c692e5df193b236f8d52a07a2030eed9bd858ed3aaccb406401a` · `450437d49a7e5530c6fb04df2e56c3ab1553ada3712fab02bd1eeb1f1adbc267` · `93ce3b6d2a18829c0212542751b309dacbdc8c1d950611efe2319aa715f3a066` · `7939f67375e6b14dfa45ec70356e91823d12f28bbd84278992b99e0d2c12ace5` · `389a497f27e1dd7484325e8e02bbdf656d53d5cf2601514e9b8d8974befddf61` | **Clientes de proxy inverso modificados por el actor**, publicados por Microsoft en mayo de 2023 | Alta como procedencia | Caducados a efectos preventivos | **Solo retrohunt** |
| sha256 | `c4b185dbca490a7f93bc96eefb9a597684fdf532d5a04aa4d9b4d4b1552c283b` · `e453e6efc5a002709057d8648dbe9998a49b9a12291dee390bb61c98a58b6e95` · `6036390a2c81301a23c9452288e39cb34e577483d121711b6ba6230b29a3c9ff` · `cd69e8a25a07318b153e01bba74a1ae60f8fc28eb3d56078f448461400baa984` · `17506c2246551d401c43726bdaec800f8d41595d01311cf38a19140ad32da2f4` · `8fa3e8fdbaa6ab5a9c44720de4514f19182adc0c9c6001c19cf159b79c0ae9c2` · `d17317e1d5716b09cee904b8463a203dc6900d78ee2053276cc948e4f41c8295` · `472ccfb865c81704562ea95870f60c08ef00bcd2ca1d7f09352398c05be5d05d` · `3e9fc13fab3f8d8120bd01604ee50ff65a40121955a4150a6d2c007d34807642` | Resto de los clientes de proxy inverso de la misma publicación. **El penúltimo aparece también en `AA23-144A`**, lo que corrobora entre fuentes | Alta como procedencia | Caducados a efectos preventivos | **Solo retrohunt** |
| sha256 | `f4dd44bc19c19056794d29151a5b1bb76afd502388622e24c863a8494af147dd` · `ef09b8ff86c276e9b475a6ae6b54f08ed77e09e169f7fc0872eb1d427ee27d31` · `d6ebde42457fe4b2a927ce53fc36f465f0000da931cfab9b79a36083e914ceca` · `66a19f7d2547a8a85cee7a62d0b6114fd31afdee090bd43f36b89470238393d7` · `3c2fe308c0a563e06263bbacf793bbe9b2259d795fcc36b953793a7e499e7f71` · `41e5181b9553bbe33d91ee204fe1d2ca321ac123f9147bb475c0ed32f9488597` · `c7fee7a3ffaf0732f42d89c4399cbff219459ae04a81fc6eff7050d53bd69b99` · `3a9d8bb85fbcfe92bae79d5ab18e4bca9eaf36cea70086e8d1ab85336c83945f` · `fe95a382b4f879830e2666473d662a24b34fccf34b6b3505ee1b62b32adafa15` · `ee8df354503a56c62719656fae71b3502acf9f87951c55ffd955feec90a11484` | **Hashes del aviso conjunto `AA23-144A`** de mayo de 2023, incluidas interfaces web derivadas de una pública conocida | Alta como procedencia | Caducados a efectos preventivos | **Solo retrohunt** |
| sha256 | `edc0c63065e88ec96197c8d7a40662a15a812a9583dc6c82b18ecd7e43b13b70` · `99b80c5ac352081a64129772ed5e1543d94cad708ba2adc46dc4ab7a0bd563f1` | **Los dos del aviso conjunto `AA24-038A`**, correspondientes a los clientes de proxy inverso `BrightmetricAgent.exe` y `SMSvcService.exe`, ambos empaquetados con UPX | Alta | Caducados a efectos preventivos | **Solo retrohunt** |
| md5 | `fd41134e8ead1c18ccad27c62a260aa6` · `b1de37bf229890ac181bdef1ad8ee0c2` | Resúmenes MD5 de los dos anteriores, tal como los publica el aviso | Alta | Caducados a efectos preventivos | **Solo retrohunt** |
| artefacto | **El informe técnico de octubre de 2026 sobre la familia de implantes de 2026 no publica ningún hash** | **No es un indicador: es una observación sobre el estado del arte.** Publica rutas, nombres de módulo, códigos de orden y reglas de red. Cuando el proveedor que analizó el implante no considera que el hash aporte, el defensor tampoco debería | Alta | Sin caducidad | **Criterio: no construir la defensa sobre esta capa** |

### A.4 — Infraestructura, herramientas y servicios · **no todo esto es malicioso**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| ipv4 | `149.248.3[.]38` | **Servidor de carga de la red de reconocimiento**, con un servidor de gestión de agentes de código libre escuchando en el puerto `13339`. **Es infraestructura del adversario, no un equipo de víctima**, y por eso sí entra en este anexo cuando las direcciones de la cadena no entran | Media | 2027-10-28 (12 meses desde la publicación) | **Bloqueo** |
| puerto | `13339` | Puerto por omisión del servidor de gestión de agentes usado en esa red. **Su presencia en un equipo de borde propio es un hallazgo** | Media | Sin caducidad | **Detección** (`H-10`) |
| artefacto | **Las direcciones de la cadena de retransmisión se omiten deliberadamente de este anexo** | **Es la segunda advertencia de la cabecera, consignada también como fila para que quede en el índice con contexto.** Son equipos domésticos de terceros, viven cuatro horas y su bloqueo corta tráfico legítimo de las propias víctimas del compromiso. **La medida que sí funciona es una lista de permisión** (`D-2`, `X-5`) | Alta | Sin caducidad como criterio | **No bloquear por dirección. Validar procedencia** |
| herramienta | `vssadmin` · `ntdsutil` · `wmic` · `netsh` · `PowerShell` · `certutil` · `dnscmd` · `ldifde` · `makecab` · `nltest` · `netstat` · `quser` · `reg` · `systeminfo` · `tasklist` · `wevtutil` · `whoami` · `xcopy` · `PsExec` | **Utilidades del propio sistema operativo**, que son el arsenal completo de posexplotación de este actor. **Su presencia no significa nada: el indicador es el contexto** —qué equipo, qué cuenta, qué secuencia, a qué hora— | Alta | **Sin caducidad** | **NO bloquear. Detección por contexto y por secuencia** |
| herramienta | `Fast Reverse Proxy (frp)` · `Earthworm` · `Chisel` | **Proxys inversos de código libre.** El primero con una variante propia del actor identificable por la cadena fija de `A.2`. **Observación de cartera: `frp` aparece también en `CTI-2026-033` y en `CTI-2026-043`, usado por clústeres sin ninguna relación con éste.** Es la ilustración más limpia de por qué la herramienta no atribuye | Alta | Sin caducidad | **Detección por contexto. NO usar como base de atribución** |
| herramienta | `Mimikatz` · `Impacket` · `Magnet RAM Capture 1.20` · `ScanLine` · `Advanced IP Scanner` | Herramientas públicas de volcado de credenciales, de manipulación de protocolos, **de captura forense de memoria** y de escaneo. La última **ya estaba en la red de la víctima para uso de administración**, y el actor la usó | Alta | Sin caducidad | **Detección por contexto** |
| servicio | **Plataformas de gestión centralizada:** orquestadores de SD-WAN, gestores unificados de puestos, plataformas de administración remota de proveedores de servicio, plataformas de monitorización de red, servidores de integración | **No son indicadores: son la superficie, y es la novedad de 2026.** Comprometer una equivale a una intrusión completa sin movimiento lateral. **Declaradas con tipo `servicio` para que no entren en los agregados planos** | Alta como superficie | Sin caducidad | **Inventario, retirada de Internet y prioridad máxima de parcheo** (`E-a`) |
| servicio | **Plataformas y datos geoespaciales de infraestructura:** ArcGIS, software de gestión de activos geoespaciales, capas de activos, diagramas de red de operación, procedimientos operativos | **Objetivo de colección declarado de este actor.** Y el dato ya exfiltrado **no se puede parchear** | Alta como superficie | Sin caducidad | **Inventario, retirada de Internet, y diseño que asuma la topología conocida** (`E-e`) |
| servicio | **Pasarelas celulares industriales de acceso remoto** | Vía de entrada documentada en 2025 hacia redes de operación. **No son maliciosas: son equipamiento legítimo que a menudo no está en el inventario de nadie** | Alta como superficie | Sin caducidad | **Inventario y retirada de Internet** (`X-5`) |
| servicio | **Fabricantes cuyos equipos se han observado reclutados en las redes de este actor:** Cisco, NETGEAR, TP-Link, Zyxel, ASUS, D-Link, DrayTek, Ruckus, Cambium, SATO, Ubiquiti, Hikvision, Araknis, Mimosa, **Intelbras**, FatPipe, Fortinet | **No son indicadores de compromiso ni acusaciones contra los fabricantes.** Es la lista de material que hay que mirar al responder `E-c`, y la razón de que `KJ-5` concierna a esta región: **el último es brasileño y tiene papel asignado de relé extranjero** | Alta | Sin caducidad | **Inventario de fin de vida y de exposición de administración. NO bloquear por fabricante** |

## Anexo B — Fuentes y valoración

> Valoración doble tipo Admiralty/OTAN: **fiabilidad de la fuente (A–F)** ×
> **credibilidad de la información (1–6)**. Se valoran por separado.

| Fuente | Disciplina | Fiabilidad | Credibilidad | Notas de sesgo |
|---|---|---|---|---|
| **Aviso conjunto `AA24-038A`, 07-02-2024** (act. 07-03-2024) — CISA, NSA, FBI, Departamento de Energía, Agencia de Protección Ambiental y Administración de Seguridad en el Transporte de EE. UU., más ACSC australiana, Centro Canadiense, NCSC británico y NCSC neozelandés. **Leído en original con sus tres anexos** | Gubernamental multinacional · TECHINT de respuestas a incidentes | **A** | **1** | **Fuente principal.** Confianza alta declarada en el preposicionamiento. **Declara su propio alcance** —lo observado en respuestas a incidentes de las agencias estadounidenses—, lo que no es un censo. Sesgo de jurisdicción: la geografía del aviso es la de sus firmantes, **y ninguno es latinoamericano** |
| **Aviso conjunto `AA23-144A`, 24-05-2023.** Leído en original | Gubernamental multinacional | **A** | **1** | Fuente de los comandos, rutas, nombres de fichero, hashes, agente de usuario y reglas de reconocimiento. **Y de la advertencia metodológica más útil del expediente:** algunos de esos comandos **pueden aparecer por actividad benigna**, y el defensor debe evaluar cada coincidencia contra su línea base |
| **Aviso conjunto «Defendiendo frente a redes encubiertas de dispositivos comprometidos con nexo chino», 23-04-2026** — NCSC-UK y quince organizaciones más, de diez países en total, entre ellas el **Centro Criptológico Nacional** español. Leído en original | Gubernamental multinacional | **A** | **1** | Fuente del concepto de **extinción de indicadores**, de la medida de lista de permisión, y de la constatación de que **una misma red encubierta puede ser usada por varios actores**. **Nombra a este actor y al de `CTI-2026-034` en el mismo documento.** Ningún firmante latinoamericano; el único hispanohablante es español |
| **Directiva de Emergencia `ED 26-03` (25-02-2026) y su versión V1 (11-03-2026)**, con la dirección suplementaria. Leídas en original | Gubernamental · obligación normativa | **A** | **1** | **Corrobora la explotación del día cero de SD-WAN por vía independiente del proveedor.** No nombra al actor: habla de «un actor de amenaza» y de «amenaza inminente». Fuente de las instrucciones de recolección forense y de la de **reconstruir el plano de control** en caso de compromiso de superusuario |
| **Catálogo de vulnerabilidades explotadas conocidas de CISA**, consultado por su fichero de datos el 18-11-2026 (versión 2026.11.17, 1.782 entradas) | Gubernamental · datos | **A** | **1** | Fuente de las fechas exactas de incorporación de las ocho vulnerabilidades de `A.1`. **Es el contraste más barato y más duro que existe** contra una afirmación de explotación |
| **Lumen Black Lotus Labs, informe sobre la red de retransmisión, 28-10-2026.** Leído en original | OSINT comercial · TECHINT de red troncal | **B** | **2** | **Fuente única del hallazgo central de 2026** y de las dos observaciones regionales de `KJ-5`. Visibilidad excepcional —telemetría de red troncal global, tres años— y **declara sus propias limitaciones**: su telemetría no siempre permitía distinguir si el acceso usó vulnerabilidad conocida o no divulgada. Sesgo: es un proveedor que vende el servicio basado en esa visibilidad |
| **Lumen Black Lotus Labs, informe sobre la red de reconocimiento.** Leído en original | OSINT comercial · TECHINT | **B** | **2** | Fuente de la concentración sudamericana, del crecimiento tras la desarticulación, de los fabricantes reclutados y de los artefactos del agente | 
| **Cisco Talos, análisis de la familia de implantes del orquestador, 28-10-2026**, y su aviso de explotación activa de 25-02-2026. Leídos en original | OSINT comercial · TECHINT | **B** | **2** | **Fuente del detalle técnico más fino del expediente.** Y de la salvedad de alias que `O-1` recoge: declara **solapamiento considerable de infraestructura con confianza alta**, no identidad. **No publica hashes**, lo que es en sí un dato |
| **Microsoft Threat Intelligence, 24-05-2023.** Leído en original | OSINT comercial · TECHINT | **B** | **2** | Origen del nombre y del expediente. Fuente de la fecha de inicio —mediados de 2021—, de Guam, de los sectores iniciales, del vector por dispositivos Fortinet, de los fabricantes de equipos usados como proxy y de diecinueve hashes. **Confianza moderada declarada** en su propia valoración sobre el desarrollo de capacidades de perturbación |
| **Informe anual de Dragos de febrero de 2026 sobre el año 2025** | OSINT comercial · TECHINT de entornos de operación | **B** | **2** | **La mejor fuente sobre la actividad de este actor en entornos de operación**, y la única del eje geoespacial como requisito de colección, de la etapa 2, de la modificación de software de puesto de ingeniería, del grupo proveedor de acceso y de la relación de cliente con el actor de `CTI-2026-034`. **Lleva marcado de propiedad: véase `B.1`** |
| **Dragos, publicación pública sobre amenazas a la red eléctrica, 2026** | OSINT comercial | **B** | **2** | Versión pública y sin marcado de propiedad de parte de lo anterior: el grupo proveedor de acceso de etapa 1 observado dentro de una eléctrica estadounidense, y el marco general |
| **Cobertura del caso de la eléctrica pequeña de Massachusetts (2025)** | OSINT · prensa especializada y proveedor | **C** | **3** | Fuente de los **más de 300 días**, del aviso del FBI como vía de detección, y del objetivo declarado —procedimientos operativos y datos de disposición espacial de la red—. **Un detalle sobre el cortafuegos como vector aparece en una sola fuente secundaria y no se da por bueno** |
| **Bitácora y informes diarios del Coordinador Eléctrico Nacional de Chile, y prensa chilena y sectorial, noviembre de 2026** | OSINT · operador del sistema y prensa | **C** | **3** | Única fuente del caso de Huatacondo. **Las fuentes discrepan en la fecha del incidente —26 o 27 de agosto— y en el código de la solicitud parlamentaria**, y así se cita. **No hay informe técnico, no hay atribución, y este informe no la insinúa** |
| **Informes del Centro Nacional de Respuesta a Emergencias de Virus Informáticos de China, 2024.** El tercero, leído en original | Fuente estatal de parte · contranarrativa | **D** | **5** | **Normalmente no fiable, información improbable.** No aporta evidencia técnica verificable sobre si hubo o no las intrusiones descritas, y una de sus citas fue objetada por el investigador citado. **Se lee, se consigna y no modifica ningún juicio.** Está evaluada en `O-2.B` y descartada en `H10`, y se incluye porque forma parte del entorno de información en que este informe se consume |

### B.1 — Una fuente con marcado de propiedad, y la decisión tomada

Esta cartera tiene una regla de higiene con precedente: **una fuente marcada por su autor como de distribución restringida no se reproduce en un informe `TLP:CLEAR`, aunque sea accesible por una URL pública**. Se aplicó en `CTI-2026-031` con un documento de proveedor, que se consignó como consultado y no reproducido.

El informe anual de Dragos de febrero de 2026 **no es ese caso, y conviene explicar por qué para que la diferencia quede escrita**:

- **Su autor lo publica deliberadamente**, con descarga abierta y sin registro de acceso previo, y lo anuncia por nota de prensa. Su propósito declarado es que la comunidad lo lea.
- **El marcado que lleva es una leyenda de propiedad intelectual al pie de cada página** —«propiedad y confidencial»— y no una marca de distribución dirigida al lector, del tipo «no redistribuir» o un marcado de la escala TLP. En el documento de `CTI-2026-031` la restricción **sí** era de distribución.
- Su contenido sobre este actor **es insustituible**: es la única fuente del eje geoespacial como requisito de colección, de la etapa 2, de la modificación de software de puesto de ingeniería y de la relación de cliente con el actor de `CTI-2026-034`.

**Decisión, y su razonamiento:** se **cita y se atribuye en prosa**, como corresponde a un informe público de un autor identificado, y **no se reproducen sus tablas, sus gráficos ni pasajes extensos textuales**, que es lo que su leyenda de propiedad protege. Donde el mismo hallazgo existe en su publicación pública sin marcado, se usa esa. Y se declara aquí para que un lector pueda discrepar de la decisión con la información delante, que es el único control de calidad que esta clase de juicio admite.

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

## Anexo D — Inteligencia útil sobre un adversario que no nos tiene por objetivo

Este anexo no es sobre Volt Typhoon. Es el método que la escritura de este informe obligó a improvisar, generalizado para reutilizarlo, porque **va a volver a hacer falta**: esta cartera tiene y tendrá actores cuyo expediente, leído honradamente, no documenta ninguna víctima en la región.

**El problema.** Un requisito pide un informe sobre un actor «para Perú y Chile». La colección se hace bien y el resultado es un no: ninguna víctima regional documentada, y además **un mecanismo de selección que explica por qué no la hay**. En ese punto hay tres salidas malas y una buena.

- **Mala 1: escribirlo igual**, trasladando la victimología estadounidense como si fuera aplicable. Produce un documento que nadie puede usar para decidir nada y que, peor, **gasta la credibilidad del siguiente**.
- **Mala 2: no escribirlo**, y responder al requisito con un «no aplica». Es honrado y es inútil: el requisito existía por una razón, y la razón no desaparece porque la respuesta sea negativa.
- **Mala 3: forzar una conexión regional**, componiendo el actor con un incidente local sin atribuir. Es la tentación más fuerte y la más dañina: esta cartera tiene **tres informes** —`CTI-2026-017`, `CTI-2026-022` y `CTI-2026-030`— que existen precisamente porque alguien hizo eso en otro expediente.
- **La buena: cambiar la pregunta.** «¿Nos atacan?» no es la única pregunta que un expediente de amenaza responde. Hay tres más, y **las tres tienen respuesta aunque la primera sea negativa**.

**Las tres preguntas, en orden de dificultad creciente.**

**Primera: ¿somos infraestructura?** Todo actor que opera a distancia necesita camino, y el camino son equipos de terceros. La pregunta es si **nuestros activos, o los de nuestros clientes, están en ese camino** —como relé, como punto de salida, como proveedor de hospedaje—. Cómo se responde: buscar en el expediente del actor **la lista de material que usa como infraestructura** y cruzarla con lo que fabricamos, vendemos, administramos o tenemos instalado. En este informe esa búsqueda dio un fabricante regional con papel asignado y una concentración geográfica de nodos, y de ahí salió `KJ-5`, `E-c` y dos hipótesis de caza. **Y el destinatario de esa parte del informe no es el SOC: es Redes**, que es una consecuencia organizativa que conviene prever.

**Segunda: ¿somos el camino hacia la víctima real?** Distinta de la anterior, y más incómoda. Si el actor ataca proveedores de servicios gestionados, operadores de telecomunicaciones y empresas de tecnología **porque mantienen acceso privilegiado al entorno de sus clientes**, entonces una organización regional con clientes, filiales o matriz en la geografía del actor **está dentro del universo de víctimas por su posición, no por su interés**. Cómo se responde: inventariar las relaciones de confianza que salen de nuestras plataformas de administración, y revisar qué obliga el contrato a notificarnos. En este informe es `E-f`.

**Tercera, y es la que más vale: ¿tendríamos los datos si la respuesta fuera sí?** Un expediente de un actor que no nos ataca sigue sirviendo para una cosa: **como guion de un ejercicio**. Se toma su cadena de intrusión y, paso por paso, se pregunta qué registro existiría en nuestra casa. El resultado no depende del actor —sirve igual contra cualquiera que haga lo mismo— y es el único hallazgo de esta clase de informe que **no caduca**. En este documento es `E-d`, `H-12` y la mitad de `T-5`.

> **Y la regla de redacción que hace falta para que esto funcione, porque sin
> ella el método se vuelve en contra.** Un informe construido así **tiene que
> decir que la respuesta a la primera pregunta es no, con todas las letras y en
> el lugar más visible**, y repetirlo donde haga falta. Si no lo hace, el lector
> que hojea concluye lo contrario de lo que el informe dice, y el documento pasa
> a engordar la misma confusión que pretendía corregir. En este informe el «no»
> está en el título, en el campo de foco regional, en `KJ-4`, en `3.5`, en `E-2`
> y en `H7` — **y aun así el pre-mortem predice que será el malentendido más
> probable.** Escribir sobre un adversario que no nos ataca exige repetirse: es
> el coste del método.

## Anexo E — Marcos de referencia empleados

`MITRE ATT&CK v14` —la versión que declara `AA24-038A` y que este informe hereda para las filas procedentes de él, con las de 2026 marcadas aparte— · `Cadena de ataque a sistemas de control industrial (SANS)`, para la clasificación por etapas de `O-3.C` · `Modelo del Diamante` · `Pirámide del Dolor`, **con la corrección estructural de `T-3`** · `F3EAD` · `ICD 203` · `ACH, supuestos clave y pre-mortem` · `TLP 2.0` · `PAP` · `Código Admiralty` · `Sigma` · `STIX 2.1` · `Catálogo de vulnerabilidades explotadas conocidas de CISA`

## Anexo F — Paquete legible por máquina

- **Fuente preferente para ingesta:** los paquetes STIX 2.1 de `AA23-144A` y de `AA24-038A`, y el informe de análisis de malware asociado al segundo. Mantenidos por sus firmantes.
- Las tablas `cti:ioc` de los anexos `A.1` a `A.4` alimentan `ioc_index.csv` en cada construcción, como **selección razonada con fecha** y subordinada a los originales.
- **Una decisión de contenido que conviene no deshacer:** este informe **no aporta ni una dirección de la cadena de retransmisión** a los agregados planos, y la omisión está consignada como fila propia en `A.4` para que figure en el índice con contexto con su razón. Es la aplicación extrema de la advertencia de la portada de este repositorio: **aquí el indicador de red no sólo es inútil, es que su uso previsible daña a un tercero inocente.**
- **Cuatro filas llevan advertencia explícita de no bloquear:** las utilidades del sistema operativo, los proxys inversos de código libre —compartidos con otros dos informes de esta cartera—, la lista de fabricantes de equipos reclutados, y las direcciones de la cadena, que directamente no están.
- **Reglas propias:** dos reglas Sigma en `X-4`, ninguna de las dos basada en un indicador perecedero: una sobre eventos del motor de almacenamiento y comandos nativos, y otra sobre una función nativa de Windows.
- **Guiones propios:** tres consultas en el lenguaje de consulta de la plataforma de endpoint y **un guion de inventario externo en `sh`** que no es una herramienta de seguridad: es la vista del adversario sobre nuestro propio borde, y sus cuatro preguntas finales no las responde ningún escáner.

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-11-18 | Emisión inicial. **Se corrigen o amplían seis afirmaciones del requisito en `§3.5`** —entre ellas la actividad en Perú y Chile, que no se sostiene, y la caracterización de «sin días cero», que dejó de ser cierta para el acceso inicial—; se establece que **la huella regional documentada de este actor es de infraestructura y no de victimología** (`KJ-5`), con un método generalizado en el `Anexo D`; se **confirma el eje geoespacial** que `CTI-2026-034` declaró como hipótesis, activando su disparador `I-5`, y se eleva a confianza alta sobre la base de un requisito de colección declarado (`KJ-6`); se consigna la valoración de proveedor según la cual **este actor y el de `CTI-2026-034` responden probablemente al mismo cliente** (`H3`, `E-1.A`); se **declara inservible y potencialmente dañina la capa de indicadores de red** de este expediente, con la consecuencia de que el informe no aporta direcciones de la cadena a los agregados planos (`T-3`, `E-1.B`, `A.4`); se consigna el incidente chileno de Huatacondo **sin atribución y con descarte expreso de cualquier vínculo** (`H7`); y se documenta la decisión sobre una fuente con marcado de propiedad en el `Anexo B.1`, distinguiéndola del precedente de `CTI-2026-031` | Célula CTI |

## Anexo H — Realimentación del consumidor

| Pregunta | Respuesta |
|---|---|
| ¿Respondió a su requisito? | |
| ¿Qué decisión tomó o cambió con este informe? | |
| **¿Cuántas plataformas de gestión centralizada tenían su administración accesible desde Internet (`E-a`)?** | |
| **¿Se pudo pasar el acceso remoto a lista de permisión? Y si no, ¿cuántas autenticaciones correctas venían de rangos residenciales (`E-b`)?** | |
| **¿Somos trayecto? ¿Cuántos equipos de borde propios o de cliente tenían administración expuesta o firmware sin soporte (`E-c`)?** | |
| **¿Existirían los datos para investigar un incidente de operación (`E-d`)? ¿Qué faltaba?** | |
| ¿Se pudo escribir `D-1`, o faltaba el registro de aplicación de los controladores de dominio? | |
| ¿Apareció algo en el inventario de plataformas y datos geoespaciales (`E-e`)? | |
| ¿Llegó a tiempo? | |

> Sin este anexo devuelto, el ciclo de inteligencia queda abierto y el próximo
> producto no mejora. **Las dos preguntas que más importan de esta tabla son la
> quinta y la sexta**, y no por este adversario: porque sus respuestas —si
> nuestros equipos son infraestructura de alguien, y si podríamos investigar un
> incidente de operación— **no dependen de ningún actor** y seguirán siendo
> ciertas o falsas cuando este expediente haya caducado.
