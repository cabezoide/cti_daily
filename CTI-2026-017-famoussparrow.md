---
tlp: "TLP:CLEAR"
pap: "PAP:AMBER"
id: "CTI-2026-017"
version: "1.2"
tipo: "Perfil de actor + informe de campaña"
foco_regional: "Latinoamérica · Chile"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "FamousSparrow (SparroWocky) · solapamiento con el ecosistema Sparrow de CopperDragon y con el clúster DarkWire (Check Point)"
fecha: "2026-09-21"
caduca: "2027-02-17"
autor: "Célula CTI"
distribucion: "Actualizado a v1.2 el 2026-11-17 con la investigación de Check Point sobre CopperDragon (10-11-2026), que obliga a revisar KJ-3, KJ-6 y el expediente de alias. Reclasificado a TLP:CLEAR el 2026-11-16 por decisión del emisor. Elaborado sin telemetría propia ni datos de cliente: no contiene información identificable de la organización emisora ni de terceros. Difusión libre, conservando la atribución de las fuentes y las salvedades metodológicas del informe. Se mantiene PAP:AMBER: los indicadores del Anexo A llevan acción permitida individual y no deben cargarse en bloqueo automático sin verificación previa contra telemetría propia."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-017
## FamousSparrow: el ciberespionaje chino concentra el 90 % de su esfuerzo en Latinoamérica y estrena SparroWocky, un implante construido para que la memoria y la pila de llamadas no delaten nada
### Ocho gobiernos de la región comprometidos entre julio de 2025 y 2026. Chile no figura en la telemetría publicada, pero sí en la alerta de agosto de 2026 sobre sus telecomunicaciones
#### **Revisión v1.2 (17-11-2026).** Una segunda investigación, publicada el 10 de noviembre de 2026, sostiene que SparroWocky **no es exclusivo de este actor**: es una pieza de un arsenal compartido que un suministrador —`CopperDragon`— entrega a varios clústeres china-nexus. Y uno de ellos, `DarkWire`, lleva desde mediados de 2025 dentro de **al menos tres grandes operadoras de telecomunicaciones latinoamericanas**, con su infraestructura de mando alojada en el mismo país que la víctima. Eso cambia dos juicios de este informe y refuerza un tercero

> **Regla de oro del producto:** todo párrafo debe responder a un requisito de
> inteligencia (PIR) y habilitar una decisión. Si un párrafo no cambia lo que
> alguien va a hacer, va al anexo o se borra.

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-017` |
| Versión / fecha | `1.2` — 2026-11-17 (emisión original: 2026-09-21) |
| Tipo de producto | Perfil de actor + informe de campaña |
| Niveles cubiertos | Estratégico · Operacional · Táctico · Técnico |
| Foco regional | Latinoamérica · Chile |
| Marcado de difusión | `TLP:CLEAR` · `PAP:AMBER` |
| Clasificación interna | Público — apto para difusión abierta |
| Requisitos atendidos | `PIR-01`, `PIR-03`, `PIR-05`, `PIR-08` |
| Solicitante / consumidor primario | CISO · Jefatura de SOC · Comité de Riesgo Operacional · Asuntos Corporativos |
| Ventana de observación | 2024-07-01 → **2026-11-10** (con antecedentes desde 2019). La ampliación de la ventana en v1.2 incorpora la investigación de Check Point sobre CopperDragon |
| Base de colección | **10** fuentes externas todo-fuente (investigación primaria de proveedor sobre binario y telemetría, prensa técnica, prensa nacional chilena, avisos de autoridad). **Sin telemetría propia incorporada** |
| Autor (analista) | Célula CTI |
| Revisión por pares | Pendiente |
| Aprobación | Pendiente |
| Caducidad / revisión | **2027-02-17** (ampliada en v1.2 desde 2026-12-21 por la incorporación de material nuevo), o antes si: se nombran los países y las operadoras de `DarkWire`; se publica un análisis que resuelva si `CopperDoor` y `SparroWocky` son el mismo binario; aparece una víctima chilena atribuida; o se resuelve públicamente la disputa de alias con Salt Typhoon |
| Productos relacionados | `CTI-2026-014` (TheGentlemen), `CTI-2026-015` (Qilin), `CTI-2026-016` (LockBit 5.0) — **no complementa: contrasta**. Los tres anteriores son actores criminales con ánimo de lucro; este es espionaje estatal y exige un modelo de amenaza distinto. **Añadidos en v1.2:** `CTI-2026-022` (Red Akodon: el otro expediente de la cartera cuyo problema central es la disputa de nombres) · `CTI-2026-027` (Mustang Panda) y `CTI-2026-028` (UNC3886), para contraste de capacidad entre actores china-nexus · **`CTI-2026-030` (Salt Typhoon), que documenta el estado de la disputa de alias del `KJ-7` de este informe y establece que sigue sin resolverse** · `CTI-2026-018` (abuso de TLD: `DarkWire` registra dominios en `.com` que imitan marcas) |
| Paquete legible por máquina | Pendiente de generar (véase §14) |

<!-- cti:note type="warn" -->

> **Limitación estructural de este producto.** Se ha elaborado exclusivamente con
> fuentes abiertas y de proveedor. No incorpora telemetría de la organización, por lo
> que **la sección de exposición propia (§O-4) está sin rellenar** y todo juicio sobre
> riesgo para nosotros es condicional, no evaluado. Un informe con §O-4 vacía es
> inteligencia genérica, no inteligencia propia.

<!-- cti:note type="warn" -->

> **Advertencia de sesgo de visibilidad — léase antes que cualquier otra cosa.** La
> afirmación «el 90 % de los objetivos están en Latinoamérica» procede de **la telemetría
> de un solo proveedor de seguridad**, y describe dónde ese proveedor tiene sensores, no
> dónde el adversario opera. Que Chile no aparezca en la lista de ocho países **no es
> evidencia de que Chile no sea objetivo**: es evidencia de que el proveedor no vio un
> compromiso chileno. La distinción es la diferencia entre no estar atacado y no estar
> mirando.

<!-- cti:note type="warn" -->

> **Nota sobre la denominación «APT».** A diferencia de los tres informes anteriores de
> esta serie, aquí el término sí corresponde: FamousSparrow es un actor de espionaje
> alineado con los intereses del Estado chino, activo desde al menos 2019, **sin ánimo de
> lucro y sin extorsión**. Esto invierte el modelo de defensa. Frente a un RaaS se compite
> por coste de oportunidad; frente a un actor de espionaje **no hay coste de oportunidad
> que subir**: si nuestra información le interesa, insistirá. Se compite por **tiempo de
> permanencia**: cuánto tarda en entrar y, sobre todo, cuánto tarda uno en verlo. El
> adversario no tiene incentivo alguno para hacer ruido, y el éxito de su operación se
> mide precisamente en que nada se rompa.

---

## 1. BLUF — Juicios clave

<!-- cti:note type="warn" -->

> ⚠ **Nota de revisión v1.2.** Los juicios `KJ-1` a `KJ-7` son los de la emisión
> original de septiembre de 2026 y **se conservan sin reescribir**, para que la
> revisión sea auditable. Dos de ellos quedan afectados por el material nuevo y
> llevan una **enmienda marcada** inmediatamente después de su texto original:
> `KJ-3` (sobre la exclusividad de SparroWocky) y `KJ-6` (sobre a quién
> atribuir el compromiso de telecomunicaciones chilenas). Los juicios `KJ-8` a
> `KJ-11` son nuevos.

<!-- cti:kj -->

**KJ-1.** **FamousSparrow ha reorientado casi por completo su esfuerzo hacia Latinoamérica
y ese giro es deliberado, no oportunista.** Desde julio de 2025, el 90 % de los objetivos
del grupo registrados en la telemetría de ESET están en la región, con entidades
gubernamentales comprometidas en **Argentina, Ecuador, Guatemala, Honduras, Panamá, Perú,
Puerto Rico y Venezuela**. Valoramos **muy probable** *(80–95 %)* que esta concentración se
mantenga durante los próximos doce meses. **Confianza: moderada.** *Base:* investigación
primaria de ESET publicada el 17-09-2026, corroborada en su contenido por tres medios
técnicos que la reproducen pero **no la verifican de forma independiente**; la cifra del
90 % no es auditable por terceros.

**KJ-2.** **El motor del giro es geopolítico, no técnico.** ESET valora que el foco responde
a la reacción de China ante la reafirmación de los intereses de Estados Unidos en la región
durante el segundo mandato de Donald Trump, que amenaza una década de inversión china en
energía, minería y telecomunicaciones. Un objetivo panameño estaba **directamente implicado
en la disputa por dos puertos del área del canal**, antes operados por una empresa china
cuya concesión el Gobierno panameño impugnó a comienzos de 2025. Valoramos **probable**
*(55–80 %)* que el criterio de selección de víctimas siga la agenda de intereses económicos
y diplomáticos chinos en la región antes que el sector o el tamaño de la organización.
**Confianza: moderada.** *Base:* es la valoración explícita del proveedor más un caso
concreto documentado; **es interpretación analítica, no declaración del actor ni evidencia
documental de tasking**.

**KJ-3.** **El nuevo implante SparroWocky está construido específicamente contra la
telemetría de endpoint moderna.** Falsifica la pila de llamadas con la técnica
SilentMoonwalk para que sus hilos parezcan originarse en `RtlUserThreadStart`, engancha
`CreateThread` con MinHook y usa `AnimateWindow` como trampolín para que la dirección de
inicio del hilo declarada sea inocente, se carga reflexivamente sin tocar disco, resuelve
la API de Windows por hashing y ejecuta complementos como **Beacon Object Files** en
memoria. Esto es **hecho confirmado por análisis de binario**, no estimación.
**Confianza: alta.** *Implicación de doctrina:* **las detecciones que dependen de la
dirección de inicio del hilo, del recorrido de la pila o de la presencia del módulo en
disco no verán este implante.** La oportunidad de detección está en la persistencia, en
el trío de ficheros del cargador y en la conexión TLS saliente a un VPS.

> ⚠ **ENMIENDA v1.2 a `KJ-3`.** El juicio original presenta SparroWocky como
> «el nuevo implante» del grupo, lo que implicaba exclusividad. **Eso ya no se
> sostiene.** La investigación de Check Point de 10-11-2026 identifica
> `CopperDoor` como el mismo implante que ESET llama `SparroWocky`, y lo sitúa
> dentro de un arsenal —el *framework* Sparrow— que un suministrador
> (`CopperDragon`) entrega a **varios** clústeres china-nexus distintos. El
> análisis técnico de `KJ-3` sigue siendo válido: las capacidades de evasión
> descritas son las de ese implante. **Lo que deja de ser válido es usar su
> presencia como base de atribución a este actor.** Véase `KJ-8` y la enmienda
> de §O-1.

**KJ-4.** **El patrón del cargador «tridente» es el artefacto más duradero y debe ser el
eje de la caza.** Cada despliegue deja tres ficheros en el mismo directorio: un ejecutable
legítimo firmado, una **DLL legítima parcheada** —conserva la firma digital, ahora inválida,
del módulo que suplanta— y un fichero `.dat` cifrado con RC4 cuyo nombre replica el del
módulo y cuya cabecera empieza por el valor mágico `0x11328712`. Valoramos **muy probable**
*(80–95 %)* que este patrón sobreviva a cambios de nombres, de binarios abusados y de
infraestructura. **Confianza: alta.** *Base:* estructura descrita en el análisis del
cargador y coherente con el esquema tridente que el mismo actor ya usaba en 2024 con
`K7AVMScn.exe` + `K7AVWScn.dll` + `K7AVWScn.doc`.

**KJ-5.** **La ausencia de Chile en la lista publicada no reduce nuestra exposición.** Ocho
de los países afectados son vecinos comerciales y diplomáticos directos, y el criterio de
selección descrito en KJ-2 —intereses chinos en energía, minería, telecomunicaciones y
puertos— describe con precisión incómoda el perfil económico chileno. Valoramos
**posibilidad real** *(45–55 %)* de que existan organizaciones chilenas dentro del conjunto
de objetivos de este actor sin que ello se haya observado ni publicado.
**Confianza: baja.** *Base:* razonamiento por analogía de intereses y sesgo conocido de la
colección; **no hay ni un solo indicador técnico que sitúe a este actor en Chile**. Se
consigna marcado como inferencia, no como hallazgo.

**KJ-6.** **El ShadowPad hallado en telecomunicaciones chilenas NO debe atribuirse a este
actor.** En agosto de 2026 se hizo pública una investigación de la Fiscalía Metropolitana
Centro Norte por sabotaje informático, tras un aviso de Estados Unidos sobre actividad
maliciosa en redes de **Entel, Movistar y Telmex**, con detección de **ShadowPad** y
referencia al clúster **Lilac Typhoon**. FamousSparrow usa ShadowPad desde julio de 2024,
pero ShadowPad es una plataforma compartida por múltiples grupos con nexo chino. Valoramos
**muy poco probable** *(5–20 %)* que ese caso sea atribuible a FamousSparrow.
**Confianza: moderada.** *Base:* el solapamiento es de **herramienta**, el nivel más débil
de la Pirámide del Dolor para atribuir; el clúster nombrado en el caso chileno es otro.
*Valor del juicio:* está aquí **para impedir una fusión indebida de alias**, que es el error
analítico más caro de este dominio.

> ⚠ **ENMIENDA v1.2 a `KJ-6`.** El juicio original —no atribuir el ShadowPad
> hallado en telecomunicaciones chilenas a este actor— **se mantiene y se
> refuerza**: sigue sin haber base para esa atribución concreta. Pero el
> material nuevo cambia el contexto en el que se lee. En septiembre de 2026 no
> existía ningún clúster china-nexus con actividad documentada contra
> **operadoras de telecomunicaciones latinoamericanas**; desde el 10 de
> noviembre de 2026 sí existe, y se llama `DarkWire`. **La pregunta deja de ser
> si hay actores de este ecosistema dentro de las telecomunicaciones de la
> región —los hay— y pasa a ser cuáles y dónde**, que es lo que la fuente no
> publica. Véase `KJ-9` y la brecha `G-5`.

**KJ-7.** **La disputa de alias con Salt Typhoon sigue sin resolverse y tiene consecuencias
operativas.** Microsoft sostiene desde septiembre de 2024 que Salt Typhoon, GhostEmperor y
FamousSparrow son el mismo grupo; ESET los rastrea por separado y señala que Microsoft **no
ha publicado indicadores técnicos ni TTP** que sostengan la fusión. Valoramos **probable**
*(55–80 %)* que se trate de clústeres distintos que comparten un proveedor común de
herramientas —un *digital quartermaster*— antes que de una sola organización.
**Confianza: moderada.** *Base:* solapamientos documentados y acotados (ProxyLogon y la IP
`27.102.113[.]240` compartida con GhostEmperor en 2021; solapamiento de código entre
SparrowDoor y HemiGate de Earth Estries) frente a arsenales propios distintos en cada clúster.
*Consecuencia:* **no importar la biblioteca de detección de Salt Typhoon como si cubriera a
FamousSparrow.** Cubre a otra cosa.

**KJ-8 (nuevo en v1.2).** **SparroWocky no identifica a este actor: identifica a un
proveedor.** Check Point publicó el 10 de noviembre de 2026 una investigación que define
`CopperDragon` como lo que denomina literalmente un **«potencial intendente digital»**
—*potential digital quartermaster*—, es decir, una entidad que **desarrolla o suministra
malware e infraestructura a varios actores china-nexus** en lugar de operar ella misma. Y
sitúa explícitamente el implante que ESET llama `SparroWocky` dentro de ese arsenal
compartido, bajo el nombre `CopperDoor`. La fuente identifica **tres clústeres** que lo
usan: `SilentDelivery` (Europa y Asia), `OceanGate` (Asia, con foco en India) y `DarkWire`
(Latinoamérica), y trata a FamousSparrow **como uno de los actores que emplean el conjunto
de herramientas, no como uno de los tres clústeres**. Valoramos **probable** *(55–80 %)*
que la tesis del suministrador compartido sea correcta. **Confianza: moderada.** *Base:*
investigación primaria de un proveedor con análisis de binario e infraestructura, que
**declara su propia tesis como hipótesis** —usa «potencial» y «puede operar como»— y no
como hecho establecido. Ninguna otra fuente la ha corroborado todavía.

**KJ-9 (nuevo en v1.2).** **Hay un clúster de este ecosistema dentro de las
telecomunicaciones latinoamericanas desde mediados de 2025, y su infraestructura está
diseñada para parecer local.** `DarkWire` ataca, según la fuente, **al menos tres grandes
operadoras de telecomunicaciones** de la región más entidades de gobierno, asuntos
exteriores y justicia, con dos puertas traseras: `CopperDoor` y `CopperDNS`. El rasgo
operativo que importa es el de la infraestructura: **la mayoría de sus direcciones de
mando están en Latinoamérica, con frecuencia en el mismo país que la víctima**, lo que hace
que el tráfico de mando se confunda con tráfico local y **anula la detección geográfica
como señal**. Valoramos **muy probable** *(80–95 %)* que esto sea así. **Confianza:
moderada.** *Base:* afirmación explícita de la fuente primaria, con treinta y seis
direcciones publicadas; **pero la fuente no nombra ni los países ni las operadoras**, de
modo que no se puede verificar si Chile está entre ellos. Es la brecha `G-5`.

**KJ-10 (nuevo en v1.2).** El vínculo entre `DarkWire` y este actor **no es una conjetura
de nomenclatura: es un dominio compartido.** La fuente señala el dominio `amelicen[.]com`
como punto de contacto, reportado previamente como servidor de mando de `SparrowDoor` —el
implante anterior de este grupo— y presente también en la infraestructura de `CopperDNS`.
Valoramos **probable** *(55–80 %)* que el solapamiento de infraestructura sea real y no
coincidencia de alojamiento. **Confianza: moderada.** *Base:* un solo indicador compartido,
señalado por una sola fuente. **Un dominio común es un indicio, no una identidad**: es el
mismo grado de evidencia que en 2021 vinculó a este grupo con GhostEmperor por una
dirección IP, y que §O-1 califica desde la emisión original como solapamiento parcial
acotado.

**KJ-11 (nuevo en v1.2).** La consecuencia metodológica es la que esta cartera ya ha
encontrado dos veces y conviene no volver a aprender: **cuando varios clústeres comparten
arsenal porque alguien se lo suministra, el implante deja de ser un indicador de actor y
pasa a ser un indicador de ecosistema.** `CTI-2026-022` documentó este mismo problema con
Red Akodon y la familia TAG-144; aquí reaparece con un grado más de abstracción, porque lo
compartido no es una técnica sino **un arsenal completo con su infraestructura**. Valoramos
**casi con certeza** *(95–99 %)* que una detección construida sobre la presencia de
`SparroWocky`/`CopperDoor` no permita, por sí sola, atribuir a FamousSparrow. **Confianza:
alta.** *Base:* se sigue directamente de `KJ-8`; es una conclusión lógica, no empírica.

**Qué cambiaría estos juicios:** (a) la publicación de indicadores técnicos por parte de
Microsoft que sostengan la fusión de alias —invalidaría KJ-7 y obligaría a reescribir §O-1—;
(b) la aparición de una víctima chilena atribuida a este actor por CSIRT Nacional o por un
proveedor con telemetría local —elevaría KJ-5 de inferencia a hallazgo—; (c) la observación
de SparroWocky fuera de Latinoamérica en volumen —falsaría el carácter deliberado de KJ-1—;
(d) un cambio del esquema tridente a un cargador de una sola pieza o sin fichero en disco
—dejaría ciega toda la caza de T-4—; (e) la identificación del vector de acceso inicial con
un CVE concreto —permitiría por fin una medida preventiva y no solo detectiva—.

---

**Qué cambiaría los juicios nuevos (v1.2):** (e) que Check Point o cualquier otro
proveedor **nombre los países y las operadoras de `DarkWire`**, lo que convertiría `KJ-9`
de amenaza regional genérica en exposición concreta — o la descartaría para Chile; (f) que
un segundo proveedor **corrobore o refute la tesis del suministrador compartido**, lo que
movería `KJ-8` de probable a cualquiera de los dos extremos; (g) que se publique un
análisis comparado de `CopperDoor` y `SparroWocky` que establezca si son **el mismo binario
o dos derivados de una misma base**, distinción que `KJ-11` deja abierta y que cambia qué
se puede atribuir con qué.

---

## 2. Resumen ejecutivo

FamousSparrow es un grupo de ciberespionaje alineado con China, activo desde al menos 2019
y conocido públicamente desde septiembre de 2021, cuando se le documentó explotando
ProxyLogon contra hoteles, gobiernos, bufetes y firmas de ingeniería en todo el mundo. Se
le dio por inactivo entre 2022 y 2024. No lo estaba: siguió desarrollando herramientas en
silencio, y reapareció en julio de 2024 dentro de la red de una asociación gremial del
sector financiero estadounidense y de un instituto de investigación mexicano.

Lo relevante ahora es otra cosa. **Desde julio de 2025 el grupo ha dejado de ser un actor
global para convertirse en un actor regional**: nueve de cada diez de sus objetivos están en
Latinoamérica, y son gobiernos. Ha abandonado el implante que lo identificaba —SparrowDoor—
y lo ha sustituido por uno nuevo, **SparroWocky**, escrito en C++, modular y diseñado
explícitamente para que las herramientas de detección de endpoint miren donde no está.

Lo que esto nos cambia no es la lista de indicadores. Es el modelo de amenaza. Los tres
informes anteriores de esta serie describían actores que necesitan que usted se entere:
cifran, extorsionan, publican. Este necesita exactamente lo contrario. Su operación es
exitosa si durante dos años nadie nota nada. No habrá rescate, no habrá sitio de filtración,
no habrá interrupción de servicio que dispare un comité de crisis. Habrá, en el mejor de los
casos, un servicio de Windows con un nombre verosímil y una conexión TLS al puerto 443 de un
VPS que nadie mira.

La decisión que se pide no es de inversión, es de reorientación: dejar de medir la defensa
por capacidad de contención y empezar a medirla por **capacidad de descubrimiento
retrospectivo**.

<!-- cti:cards -->

| Rasgo | Qué significa | Etiqueta |
|---|---|---|
| Sin monetización, sin ruido | No hay evento que dispare la respuesta. La detección debe ser proactiva o no existe | `01 · modelo de amenaza` |
| Anti-telemetría por diseño | Falsifica pila de llamadas y dirección de hilo: el EDR ve un proceso limpio | `02 · evasión` |
| Cargador sobre binario firmado | La DLL parcheada conserva la firma del módulo legítimo, ya inválida | `03 · suplantación` |
| Selección por interés geopolítico | El criterio no es nuestro sector ni nuestro tamaño, es con quién negociamos | `04 · victimología` |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `90 %` | de los objetivos del grupo están en Latinoamérica desde mediados de 2025 | Antes operaba de forma global; es un giro casi total |
| `8` | gobiernos de la región con compromiso documentado | Argentina, Ecuador, Guatemala, Honduras, Panamá, Perú, Puerto Rico y Venezuela |
| `18` | servidores de mando y control observados en 9 meses | Entre 2025-12-11 y 2026-06-17, todos sobre TLS/443 en VPS comerciales |
| `7` | años de operación sin interrupción conocida | Activo desde 2019; dado por inactivo 2022–2024 por error |

> ✅ **Decisión que se solicita a Dirección:** (a) autorizar una **caza retrospectiva de 24
> meses** sobre los artefactos de §T-4, no una revisión de indicadores de 30 días; (b)
> aprobar el cierre de la brecha de visibilidad de **creación de servicios y de escritura de
> DLL en directorios de aplicación**, sin la cual las hipótesis H-1 a H-5 son inejecutables;
> (c) incorporar al registro de riesgos el **espionaje por interés geopolítico de terceros**
> como categoría propia, distinta del cibercrimen, con dueño asignado en Asuntos
> Corporativos y no solo en TI.

---

### Adenda del resumen ejecutivo — revisión v1.2, 17 de noviembre de 2026

Siete semanas después de emitirse este informe, una segunda investigación obliga a
corregir una de sus premisas. El 10 de noviembre de 2026, Check Point publicó un análisis
que sostiene que el implante que da nombre a este documento **no pertenece a este actor en
exclusiva**.

La tesis es la siguiente. Existe una entidad —la llaman `CopperDragon`— que el propio
informe define con cautela como un **«potencial intendente digital»**: alguien que
desarrolla o suministra malware e infraestructura **a otros**, en lugar de operar. Su
arsenal, el *framework* Sparrow, lo usan al menos tres clústeres distintos, con victimología
separada: uno en Europa y Asia, otro en Asia con foco en India, y un tercero en
Latinoamérica. Y el implante que ESET analizó como `SparroWocky` es, en esa taxonomía,
`CopperDoor`: una pieza del arsenal compartido.

**Lo que esto cambia no es el análisis técnico, que sigue en pie, sino lo que se puede
concluir de encontrarlo.** El §T-4 y el §X-3 de este informe siguen siendo correctos:
describen cómo detectar ese implante y ese cargador. Lo que deja de ser correcto es la
inferencia siguiente, que ninguna sección enuncia pero que el lector haría de forma
natural: **si encuentro esto, es FamousSparrow.** Ya no. Puede ser cualquiera de los que
compran en la misma tienda.

**Y hay una segunda cosa, que es la que debería leerse con más atención en Chile.** El
clúster latinoamericano de ese ecosistema se llama `DarkWire`, lleva activo desde mediados
de 2025, y sus objetivos son **al menos tres grandes operadoras de telecomunicaciones** de
la región, además de entidades de gobierno, asuntos exteriores y justicia. La fuente no
nombra ni los países ni las operadoras.

El detalle operativo de `DarkWire` que importa es el de su infraestructura: **la mayoría de
sus direcciones de mando y control están alojadas en Latinoamérica, con frecuencia en el
mismo país que la víctima.** No es una elección estética. Significa que el tráfico de
mando sale hacia una dirección nacional, indistinguible del tráfico legítimo a un
proveedor local, y que **cualquier detección que dependa de que el C2 esté «fuera» no lo
verá**. Es el mismo principio que `CTI-2026-025` documenta para los túneles de terceros,
llevado a la geografía.

La versión original de este informe sostenía, en `KJ-6`, que el ShadowPad hallado en
telecomunicaciones chilenas no debía atribuirse a este actor. **Ese juicio se mantiene y se
refuerza.** Pero su contexto cambió: en septiembre de 2026 no había ningún clúster
china-nexus con actividad documentada contra operadoras de telecomunicaciones
latinoamericanas, y ahora hay uno. La pregunta ya no es si están ahí: es cuáles y dónde, y
eso es precisamente lo que no se publica.

Las dos decisiones nuevas que este material pide son pequeñas y concretas: **buscar el
dominio que vincula los dos expedientes** (`amelicen[.]com`, §X-3 y Anexo A.2), y **revisar
si nuestras detecciones de mando y control asumen que el servidor del adversario está en el
extranjero** — porque en este caso no lo está.

---

## 3. Alcance, requisitos y limitaciones

**3.1 Requisitos de inteligencia atendidos**

| Req. | Enunciado | ¿Respondido? | Dónde |
|---|---|---|---|
| PIR-01 | ¿Qué actores tienen intención y capacidad contra nuestro sector y nuestra geografía? | Sí | §E-1, §E-2, §O-2 |
| PIR-03 | ¿Qué actividad de actores con nexo estatal afecta a Chile y a su entorno regional? | Parcial | §E-2, §O-5, §KJ-5, §KJ-6 |
| PIR-05 | ¿Qué capacidades adversarias eluden nuestra pila de detección actual? | Sí | §KJ-3, §T-3, §X-1, §X-3 |
| PIR-08 | ¿Qué debemos cazar de forma retrospectiva y con qué prioridad? | Sí | §T-4, §T-5 |

**3.2 Fuera de alcance.** No se evalúa la actividad histórica del grupo contra el sector
hotelero (2019–2021), ya cubierta por la literatura pública y sin vigencia táctica. No se
analizan en profundidad SparrowDoor ni ShadowPad más allá de lo necesario para la atribución
y para la caza retrospectiva. **No se emite juicio sobre el caso chileno de
telecomunicaciones de agosto de 2026**, que corresponde a otro clúster y merece producto
propio.

**3.3 Limitaciones de la colección.** (a) Dependencia crítica de **una sola fuente de
investigación primaria**: toda la caracterización técnica de SparroWocky procede del análisis
de ESET del 17-09-2026; los demás medios lo reproducen. No existe corroboración
independiente. (b) La telemetría que sostiene el «90 %» es la de ese proveedor, con la
distribución de sensores que tenga en la región. (c) **No se conoce el vector de acceso
inicial con certeza**: la matriz ATT&CK del proveedor consigna explotación de servidores
Exchange expuestos, mientras que la prensa técnica derivada afirma que el vector es
desconocido; se consigna la discrepancia y se trata en §T-1. (d) Sin telemetría propia:
§O-4 vacía. (e) Las fuentes sobre el caso chileno son de prensa nacional, no técnicas, y no
permiten validar indicadores.

**3.4 Metodología.** OSINT y TECHINT de proveedor. Análisis de hipótesis alternativas (ACH)
en §O-6, pre-mortem, y valoración doble Admiralty en el Anexo B. Lenguaje estimativo según
ICD 203, con la escala del Anexo C. Mapeo a MITRE ATT&CK y priorización por Pirámide del
Dolor.

---

**3.5 Limitaciones añadidas en la revisión v1.2.** (i) **La investigación de Check Point
declara su propia tesis como hipótesis, no como hallazgo.** Los términos literales son
«potencial intendente digital» y «puede operar como»; `KJ-8` respeta ese grado y no lo
eleva. (ii) **El informe no nombra los países ni las operadoras de `DarkWire`**, ni cuántas
víctimas hay en cada uno. Dice «al menos tres grandes operadoras de telecomunicaciones» y
«varias decenas» de víctimas en el conjunto de los tres clústeres, repartidas en **21
países** que tampoco enumera individualmente. **No se puede determinar si Chile está entre
ellos**, y por tanto `KJ-9` no se puede convertir en exposición concreta. Es la brecha
`G-5`. (iii) **El artículo no se pudo leer íntegro en una sola pasada**: se leyó en dos
tramos, y los indicadores proceden del segundo. No hay indicios de inconsistencia entre
ambos. (iv) **El informe no publica mapeo MITRE ATT&CK**: describe las técnicas en prosa.
El §T-2 de este informe **no se ha ampliado** con el material nuevo, para no atribuir a la
fuente un mapeo que no hizo. (v) **No publica ningún mutex ni nombre de servicio malicioso
propio**, sólo nombres de servicio legítimos de Windows que uno de los componentes
reconfigura. (vi) **La asignación de cada dirección IP a un clúster proviene de los
encabezados de las tablas de la fuente, no de un dato por dirección.** Se conserva esa
atribución con la salvedad anotada en el Anexo A.2. (vii) **Varias claves criptográficas se
mencionan sin publicar su valor** (la clave RC4 de los módulos, el cifrado basado en el
nombre del equipo). (viii) **No se han leído la publicación de ESET sobre el reemplazo de
SparrowDoor por CopperDoor ni el análisis de Positive Technologies** que la fuente cita
para uno de los otros clústeres; ambos son requisitos de colección (`G-6`). (ix) **La
correspondencia entre `CopperDoor` y `SparroWocky` la afirma Check Point**; no se ha
localizado una comparación de binarios publicada que establezca si son el mismo fichero o
dos derivados de una base común, y la distinción importa para lo que se puede atribuir
(`KJ-11`).

---

# NIVEL ESTRATÉGICO
### Para: Consejo · CISO · Riesgo · Legal · Asuntos Corporativos · Horizonte: 6–24 meses

## E-1. Qué representa este actor en el panorama

<!-- cti:cards -->

| Cambio estructural | Por qué nos afecta | Etiqueta |
|---|---|---|
| Latinoamérica deja de ser periferia del espionaje chino | Durante años la región fue terreno de cibercrimen, no de APT estatales. Ese supuesto ya no sostiene el modelo de riesgo | `regionalización` |
| El objetivo es el Estado, y el Estado es nuestro cliente, regulador y socio | Un compromiso de la contraparte gubernamental expone nuestra información aunque nuestra red esté intacta | `tercero de confianza` |
| La amenaza se selecciona por geopolítica, no por sector | Un contrato con capital chino, una concesión portuaria o una licitación energética nos convierte en objetivo sin cambiar nada de lo que hacemos | `criterio de selección` |
| El éxito del adversario es la ausencia de evento | Nuestra métrica de seguridad —incidentes contenidos— no mide nada de esto | `métrica ciega` |

El contraste con los tres informes anteriores de esta serie es el hallazgo estratégico. Un
operador de ransomware necesita ser visto para cobrar; por eso deja huella, exige plazo y
publica. Este actor cobra en información y su producto se degrada en cuanto alguien se da
cuenta. La consecuencia práctica es que **todo nuestro instrumental de respuesta a
incidentes está calibrado sobre un disparador que aquí no va a ocurrir**.

## E-2. Victimología

<!-- cti:bars title="Distribución del esfuerzo del actor (telemetría del proveedor, mediados 2025 → 2026)" -->

| Región | Porcentaje de objetivos |
|---|---|
| Latinoamérica | 90 |
| Resto del mundo | 10 |

**Países con entidades gubernamentales comprometidas.** El proveedor no publica recuento de
víctimas por país, por lo que no se presenta distribución numérica: hacerlo sería fabricar
precisión inexistente.

<!-- cti:table highlight="Panamá|Chile" -->

| País | Tipo de entidad | Nota de contexto |
|---|---|---|
| Argentina | Gubernamental | — |
| Ecuador | Gubernamental | — |
| Guatemala | Gubernamental | — |
| Honduras | Gubernamental | Ya objetivo del grupo entre 2022 y 2024, con investigación en curso |
| Panamá | Gubernamental | Una entidad implicada en la disputa por dos puertos del área del canal, antes operados por una empresa china |
| Perú | Gubernamental | — |
| Puerto Rico | Gubernamental | Territorio estadounidense: eleva el componente de contrainteligencia del caso |
| Venezuela | Gubernamental | — |
| Chile | **No observado** | Sin ningún indicador que sitúe al actor en el país. Véase KJ-5 y la advertencia de sesgo en §0 |
| **(v1.2) Al menos 3 operadoras de telecomunicaciones de la región** | **Telecomunicaciones** | **Clúster `DarkWire`, activo desde mediados de 2025.** La fuente no nombra las operadoras ni los países. Añade además gobierno, asuntos exteriores y justicia |

<!-- cti:note type="warn" -->

> ⚠ **Adenda v1.2 a la victimología.** La tabla anterior es la de la emisión original y
> describe **objetivos gubernamentales**. El material nuevo añade un sector que no estaba:
> **telecomunicaciones**. El clúster `DarkWire` del mismo ecosistema lleva desde mediados
> de 2025 dentro de al menos tres grandes operadoras de la región, y la fuente **no publica
> ni los países ni los nombres**. En el conjunto de los tres clústeres habla de «varias
> decenas» de víctimas repartidas en **21 países**, sin enumerarlos.
>
> La consecuencia para la lectura de este informe es directa: **el párrafo siguiente, que
> argumentaba que la exposición chilena era indirecta —por socios, concesiones y cadena de
> suministro—, ya no describe el único camino.** Si una operadora chilena estuviera entre
> las tres, la exposición sería de primer orden y afectaría a cualquier organización que
> curse tráfico por ella. **No se puede afirmar ni descartar**, y eso es exactamente la
> brecha `G-5`.

> **Lectura clave.** La distribución no describe un sector: describe un mapa de intereses.
> Energía, minería, telecomunicaciones y logística portuaria son exactamente los cuatro
> dominios donde la inversión china en la región se ha concentrado durante la última década
> y donde hoy se disputa influencia. Una organización chilena no necesita ser estratégica
> para el adversario por lo que hace, sino por **con quién lo hace**: socios, concesiones,
> contrapartes estatales y cadena de suministro. Esa es la superficie que ningún inventario
> de activos refleja.

## E-3. Tendencia y pronóstico

<!-- cti:chart title="Servidores de mando y control observados por primera vez, por mes" cap="Mide aparición de infraestructura documentada por el proveedor, no número de víctimas ni de intrusiones. El repunte de febrero y marzo de 2026 puede reflejar tanto expansión de la campaña como mejora de la visibilidad del investigador." -->

| Periodo | Servidores |
|---|---|
| Dic·25 | 1 |
| Ene·26 | 3 |
| Feb·26 | 8 |
| Mar·26 | 4 |
| Abr·26 | 0 |
| May·26 | 1 |
| Jun·26 | 1 |

<!-- cti:cards -->

| Escenario | Desarrollo | Etiqueta |
|---|---|---|
| Continuidad regional | El actor mantiene el foco latinoamericano y amplía a los países de la región aún no observados, siguiendo la agenda de intereses económicos chinos. La publicación de septiembre de 2026 provoca rotación de infraestructura y cambio de nombres de servicio, pero no de esquema | `Probable · 55–80 %` |
| Retracción táctica | La exposición pública obliga a una pausa operativa y a rediseñar el cargador; reaparición en 6–12 meses con un implante distinto y sin fichero en disco | `Poco probable · 20–45 %` |
| Ampliación al sector privado estratégico | El actor extiende el objetivo desde el Estado hacia operadores privados de energía, minería, puertos y telecomunicaciones que son contraparte de esos gobiernos | `Posibilidad real · 45–55 %` |
| Convergencia de clústeres | Se publican indicadores que confirman la fusión con Salt Typhoon y el actor pasa a tener capacidades de compromiso de operador de telecomunicaciones | `Remoto · 5–20 %` |

## E-4. Decisiones que este informe pide al nivel estratégico

<!-- cti:table highlight="retrospectiv|ANCI|regional|24 meses" -->

| # | Decisión | Fundamento | Plazo |
|---|---|---|---|
| E-a | Autorizar una campaña de **caza retrospectiva de 24 meses** sobre los artefactos de §T-4, con horas de analista asignadas, no como tarea de fondo | KJ-3, KJ-4: no habrá alerta que dispare la búsqueda; si no se busca, no se encuentra | 30 días |
| E-b | Aprobar el cierre de las brechas de visibilidad de §T-5 —creación de servicios, escritura de DLL en directorios de aplicación, conexiones TLS salientes por proceso— y fijar retención mínima de 12 meses | Sin ellas, las hipótesis H-1 a H-6 no son ejecutables y este informe no cambia nada | 60 días |
| E-c | Incorporar al registro de riesgos corporativo la categoría **espionaje por interés geopolítico de terceros**, con dueño en Asuntos Corporativos y criterio de exposición basado en contrapartes y contratos, no en sector | KJ-2, E-2: el criterio de selección del adversario es relacional y hoy nadie lo modela | 90 días |
| E-d | Extender los requisitos de seguridad y el derecho de auditoría a **contrapartes gubernamentales y socios con vínculo regional**, e incluir cláusula de notificación de compromiso | E-1: el compromiso del tercero expone nuestra información sin tocar nuestra red | 90 días |
| E-e | Coordinar con **CSIRT Nacional / ANCI** la solicitud de indicadores y de contexto sobre actividad de actores con nexo chino en el país, en el marco de la Ley 21.663 | KJ-5, KJ-6: hay actividad china documentada en Chile por otras vías; nuestra ceguera es de colección, no del adversario | 60 días |

---

# NIVEL OPERACIONAL
### Para: Jefatura de SOC · Respuesta a Incidentes · Threat Hunting · Horizonte: semanas–meses

## O-1. Identificación y alias

| Designación | Origen | Grado de equivalencia |
|---|---|---|
| FamousSparrow | ESET | **Referencia de este informe** |
| Salt Typhoon | Microsoft | **Ambiguo / disputado.** Microsoft afirma equivalencia desde septiembre de 2024 sin publicar indicadores técnicos ni TTP. ESET los rastrea por separado |
| GhostEmperor | Kaspersky | **Solapamiento parcial acotado.** Ambos explotaron ProxyLogon y compartieron la IP `27.102.113[.]240` en 2021, pero cada uno tiene arsenal propio |
| Earth Estries | Trend Micro | **Solapamiento parcial.** TTP comunes y solapamiento de código entre SparrowDoor y HemiGate; la naturaleza y extensión del vínculo no está establecida |
| CrowDoor | Trend Micro | Nombre de una familia de implante, no del actor. Una de las variantes de SparrowDoor de 2024 se le parece |
| Lilac Typhoon | Microsoft | **Clúster distinto.** Es el nombrado en el caso chileno de telecomunicaciones de agosto de 2026. No confundir |
| **`CopperDragon`** *(v1.2)* | Check Point | **No es un alias de este actor: es un presunto suministrador.** La fuente lo define como «potencial intendente digital» que entrega malware e infraestructura a varios clústeres china-nexus. FamousSparrow sería **uno de los que usan su arsenal**, no el arsenal mismo |
| **`DarkWire`** *(v1.2)* | Check Point | **Clúster distinto y vinculado.** Es el clúster **latinoamericano** del mismo ecosistema: telecomunicaciones, gobierno, exteriores y justicia, desde mediados de 2025. Vinculado a este actor por el dominio compartido `amelicen[.]com`. **No fundir** |
| **`SilentDelivery`** *(v1.2)* | Check Point | **Clúster distinto** del mismo ecosistema: Europa y Asia, entrada por *watering hole* con falsa advertencia de certificado de Chrome |
| **`OceanGate`** *(v1.2)* | Check Point | **Clúster distinto** del mismo ecosistema: Asia, con foco en India, entrada por servidores Linux. La fuente dice que sus tácticas son «consistentes con» FamousSparrow — y *consistente con* no es *igual a* |
| **`CopperDoor`** *(v1.2)* | Check Point | **Es el nombre que Check Point da al implante que ESET llama `SparroWocky`.** No es un actor. Véase la enmienda de la nota de tradecraft |
| **`Melofee`** *(v1.2)* | Diversos | La fuente lo evalúa como **vinculado a `SparrowShell`**, el componente Linux del arsenal. Relación no establecida con este actor |

> ⚠ **Nota de tradecraft — el error caro de este dominio.** Fusionar FamousSparrow con Salt
> Typhoon parece un detalle de nomenclatura y no lo es. Salt Typhoon es un actor con
> capacidad documentada de comprometer operadores de telecomunicaciones y dispositivos de
> borde de red a escala global; FamousSparrow es un actor de implante de endpoint sobre
> servidores expuestos. Si se importan las detecciones de uno creyendo que cubren al otro,
> se obtiene una cobertura nominal alta y una cobertura real nula. **Hasta que Microsoft
> publique indicadores, se tratan como clústeres separados y se documenta la decisión.**

<!-- cti:note type="warn" -->

> ⚠ **ENMIENDA v1.2 a la nota de tradecraft — y el error se ha vuelto más caro.** La nota
> anterior advertía contra **fundir dos actores**. El material nuevo añade un error distinto
> y de sentido contrario: **tomar un implante por un actor.**
>
> La emisión original de este informe se construyó, legítimamente, alrededor de
> `SparroWocky` como implante característico del grupo. La investigación de Check Point de
> 10-11-2026 sostiene que ese mismo implante —al que llama `CopperDoor`— es una pieza de un
> arsenal que **un suministrador entrega a varios clústeres distintos**, con victimologías
> separadas en Europa, Asia y Latinoamérica.
>
> **La regla operativa que se deriva, y que vale para toda esta cartera:** encontrar
> `SparroWocky`/`CopperDoor` en una red establece que estamos ante **el ecosistema
> Sparrow**. No establece **cuál de sus usuarios** está dentro. Son dos afirmaciones de
> valor muy distinto, y la segunda requiere algo más: infraestructura, victimología o
> secuencia de operación.
>
> Hay dos matices que conviene no perder. El primero: la propia fuente llama a su tesis
> «potencial» y «puede operar como», de modo que **la existencia del suministrador es una
> hipótesis bien argumentada y no un hecho establecido** (`KJ-8`). El segundo: nadie ha
> publicado una comparación de binarios que determine si `CopperDoor` y `SparroWocky` son
> **el mismo fichero o dos derivados de una base común** — y de eso depende exactamente
> cuánto se puede atribuir con cuánta confianza (§3.5-ix, `KJ-11`).
>
> Esto es, en el fondo, el mismo problema que `CTI-2026-022` documentó con Red Akodon, un
> grado más arriba: allí lo compartido era el método; aquí es **el arsenal entero con su
> infraestructura**.

## O-2. Estructura y atribución

| Eje de atribución | Valoración | Confianza |
|---|---|---|
| Clúster técnico | Consistente: implante propio, esquema de cargador propio, continuidad de desarrollo 2019–2026 | Alta |
| Grupo organizado | Equipo con desarrollo interno sostenido; capacidad de reescribir su implante principal manteniendo doctrina de despliegue | Alta |
| Nexo estatal | Alineado con los intereses del Estado chino; selección de víctimas coherente con la agenda económica y diplomática de la RPC en la región | Moderada |
| Identidad nominal | Sin identificación de personas ni de unidad | Nula |
| Relación con Earth Estries / GhostEmperor | Proveedor común de herramientas (*digital quartermaster*) antes que identidad | Moderada |
| Relación con Salt Typhoon | No establecida. Afirmada por un proveedor sin evidencia publicada | Baja |

*Razonamiento:* continuidad del esquema tridente entre 2024 y 2026; reutilización de la
doctrina de despliegue pese al cambio completo de implante; victimología coherente con
intereses estatales y sin ningún componente de monetización en siete años de operación;
uso en 2024 de ShadowPad, plataforma cuyo acceso está restringido a grupos con nexo chino.

*Contraargumento:* el solapamiento de herramientas entre clústeres chinos es tan extenso
que la atribución basada en arsenal es intrínsecamente débil; la hipótesis del quartermaster
explica los solapamientos sin necesidad de identidad, pero también **impide descartar** que
varios de estos nombres sean vistas parciales de una misma estructura mayor. Ninguna de las
dos lecturas se puede cerrar con la evidencia pública disponible.

## O-3. Modelo de operación

El actor no vende, no extorsiona y no alquila acceso. Su cadena de valor es: **acceso
duradero a servidores expuestos → implante silencioso → recolección continua → exfiltración
por el mismo canal de mando**. Tres rasgos definen su economía operativa:

**Infraestructura desechable y barata.** Los dieciocho servidores de mando observados están
en VPS comerciales —Kaopu Cloud (Hong Kong y Brasil), LightNode (Brasil y México),
Constant Company/Vultr, Cogent, Latitude.sh, NTT America—, con vida corta y rotación
constante. Varios están **deliberadamente alojados en la región de las víctimas**, lo que
degrada la detección por geolocalización del destino: una conexión desde Santiago a un VPS
brasileño no levanta la misma sospecha que una a Hong Kong.

**Reutilización de doctrina, no de código.** SparrowDoor fue abandonado en agosto de 2025 y
sustituido por SparroWocky, escrito desde cero en C++. Lo que **no** cambió fue la forma de
entregarlo: el mismo esquema de tres ficheros, la misma lógica de cifrado RC4 del payload,
la misma elección de binarios legítimos firmados. Para la defensa esto es la buena noticia
del informe: **el comportamiento sobrevive al código**, y es ahí donde hay que atacar.

**Integración de componentes públicos.** Mbed TLS para el canal, MinHook para los enganches,
COFF Loader para ejecutar BOF, SilentMoonwalk para falsificar la pila. El actor no inventa
técnicas de evasión: adopta las de la comunidad ofensiva pública, lo que acorta su ciclo de
desarrollo y **hace que sus técnicas sean conocidas y, por tanto, detectables en principio**.

## O-4. Nuestra exposición

> ⬛ **Sección sin evaluar — requiere telemetría e inventario internos.** Mientras esta
> sección siga vacía, este informe es inteligencia genérica sobre un actor, no una
> evaluación de nuestro riesgo. Las preguntas de abajo son el requisito mínimo para
> cerrarla, y su respuesta debería estar disponible antes de la revisión de este producto.

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| X-1 | ¿Exponemos algún **Microsoft Exchange** a Internet? ¿Qué versión, qué nivel de parche, desde cuándo? ¿Hay algún Exchange olvidado en modo híbrido? | Inventario + escaneo externo | TI/Mensajería |
| X-2 | ¿Exponemos servidores **IIS** con aplicaciones heredadas (DotNetNuke, portales, formularios) que admitan escritura de ficheros `.ashx`? | Inventario de aplicaciones | TI/Aplicaciones |
| X-3 | ¿Registramos y retenemos **creación e instalación de servicios de Windows** (EID 7045 / 4697) en todos los servidores? ¿Cuánto tiempo? | SIEM | SOC |
| X-4 | ¿Podemos listar hoy todas las **DLL no firmadas o con firma inválida** cargadas por procesos firmados en servidores? | EDR | SOC |
| X-5 | ¿Tenemos registro de **conexiones TLS salientes por proceso** desde servidores, con IP de destino y retención de 12 meses? | EDR + NetFlow | Redes |
| X-6 | ¿Qué contrapartes **gubernamentales de la región** tienen conectividad, VPN, federación de identidad o intercambio de ficheros con nosotros? | Arquitectura + Legal | TI/Redes |
| X-7 | ¿Participamos en proyectos, concesiones o licitaciones con capital o contraparte china en energía, minería, puertos o telecomunicaciones? | Asuntos Corporativos | Dirección |

## O-5. Cronología

<!-- cti:timeline -->

| Fecha | Hecho | Traza |
|---|---|---|
| 2019 | Primera actividad conocida del grupo | Global |
| 2021-09 | **Divulgación pública inicial: explotación de ProxyLogon (CVE-2021-26855) contra hoteles, gobiernos, bufetes e ingeniería** | Global |
| 2021 | Infraestructura compartida con GhostEmperor (`27.102.113[.]240`) | Global |
| 2022–2024 | Objetivo: una institución gubernamental de Honduras. Periodo en el que se dio al grupo por inactivo | LATAM |
| 2024-03-11 | Primera observación del C2 de ShadowPad `216.238.106[.]150` | Global |
| 2024-06-27 | Alta del servidor de entrega `43.254.216[.]195` | Global |
| 2024-07 | **Reaparición: compromiso de una asociación gremial financiera en EE. UU. y de un instituto de investigación en México. Primer uso documentado de ShadowPad por el grupo** | LATAM |
| 2025-03-27 | Publicación del análisis de las nuevas variantes de SparrowDoor | Global |
| 2025-07 | **Inicio del giro: el objetivo pasa a ser casi exclusivamente latinoamericano** | LATAM |
| 2025-08 | SparrowDoor es sustituido por SparroWocky como implante principal | LATAM |
| 2025-11-17 | Marca temporal de compilación de la muestra SparroWocky v1.8 | LATAM |
| 2025-12-11 | Primer servidor de mando de SparroWocky observado (`216.238.110[.]120`) | LATAM |
| 2026-02 | Pico de despliegue de infraestructura: 8 servidores nuevos en un mes | LATAM |
| 2026-02 | **La PDI recibe los antecedentes del caso de telecomunicaciones chilenas** | Chile |
| 2026-06-17 | Último servidor de mando documentado (`91.148.134[.]115`) | LATAM |
| 2026-08-10 | **Se hace pública la alerta de EE. UU. sobre ShadowPad y Lilac Typhoon en Entel, Movistar y Telmex; la Fiscalía Metropolitana Centro Norte abre investigación por sabotaje informático** | Chile |
| 2026-09-17 | **Publicación del análisis de SparroWocky y de la campaña latinoamericana** | LATAM |
| 2026-09-21 | Emisión de este informe | Chile |
| `2025-med` | **(v1.2) Inicio de la actividad del clúster `DarkWire` contra operadoras de telecomunicaciones y entidades de gobierno, exteriores y justicia en Latinoamérica**, según Check Point | LATAM |
| `2026-ini` | **(v1.2)** Inicio de la actividad del clúster `SilentDelivery` en Europa y Asia, con *watering hole* y falsa advertencia de certificado de Chrome | Global |
| `2026-11-10` | **(v1.2) Publicación de la investigación sobre `CopperDragon`: el implante SparroWocky se identifica como `CopperDoor`, pieza de un arsenal compartido entre tres clústeres. 21 países, varias decenas de víctimas, al menos tres grandes operadoras de telecomunicaciones latinoamericanas** | LATAM |
| `2026-11-17` | **(v1.2) Revisión de este informe**: enmienda de `KJ-3` y `KJ-6`, cuatro juicios nuevos, enmienda del expediente de alias y Anexo A.2 | Chile |

## O-6. Hipótesis alternativas consideradas

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| H1 · Campaña de espionaje estatal dirigida, con selección por interés geopolítico | Consistente con toda la evidencia: victimología gubernamental, ausencia total de monetización en 7 años, caso panameño vinculado a una disputa concreta, arsenal restringido a grupos con nexo chino | `Retenida` |
| H2 · Concentración regional aparente, producto del sesgo de sensores del proveedor | No se puede descartar y explicaría parte del 90 %. Pero **no explica el contenido**: que los objetivos sean gobiernos y que uno esté implicado en la disputa portuaria no es un artefacto de dónde haya sensores | `Retenida como atenuante de KJ-1` |
| H3 · Operación de acceso inicial para revender a otro clúster chino | Inconsistente: el implante recolecta, captura pantalla y exfiltra de forma continua durante meses. Un revendedor de acceso no invierte en capacidad de recolección sostenida | `Poco probable · 20–45 %` |
| H4 · Falsa bandera de un tercero que imita herramientas chinas | Sin evidencia. Requeriría reproducir siete años de continuidad de desarrollo y el acceso a ShadowPad. Se consigna para que no se reabra sin evidencia nueva | `Descartada` |
| H5 · FamousSparrow y Salt Typhoon son el mismo actor | Afirmado por un proveedor, sin indicadores publicados. No se puede confirmar ni refutar con evidencia pública; se mantiene abierta y **no se opera sobre ella** | `Abierta · sin evidencia` |

**Supuesto clave:** que el análisis del proveedor sobre SparroWocky es técnicamente correcto
y representativo. **Si es falso** —muestra atípica, atribución errónea del implante al
grupo— toda la sección técnica de este informe pierde validez y solo sobrevive el juicio
estratégico de KJ-2. No hay forma de comprobarlo sin una muestra propia.

**Pre-mortem.** Es marzo de 2027 y este informe resultó equivocado. Las dos causas más
probables: **(1)** cazamos durante meses nombres de servicio y valores de registro que el
actor cambió la semana siguiente a la publicación, mientras el patrón estructural —trío de
ficheros, DLL firmada inválida, `.dat` con cabecera `0x11328712`— seguía intacto y sin
buscarse, porque era más difícil de consultar; **(2)** dedicamos el esfuerzo a un actor que
nunca nos miró, mientras el compromiso real entraba por una contraparte gubernamental
regional con la que tenemos federación de identidad y que nadie incluyó en el alcance.

## O-7. Indicadores y señales de alerta

| # | Indicador observable | Qué señalaría | Disciplina | Responsable |
|---|---|---|---|---|
| I-1 | Aparición de una víctima chilena atribuida a FamousSparrow por CSIRT Nacional o proveedor con telemetría local | KJ-5 pasa de inferencia a hallazgo; se activa respuesta de nivel 1 | OSINT / enlace | Célula CTI |
| I-2 | Publicación por Microsoft de indicadores técnicos que sostengan la fusión con Salt Typhoon | Obliga a reescribir §O-1 y a reevaluar la cobertura de detección | OSINT | Célula CTI |
| I-3 | Nuevo análisis que documente SparroWocky sin fichero en disco o con cargador de una pieza | Invalida H-1 a H-5 de §T-4; caza queda ciega | OSINT / TECHINT | Ingeniería de detección |
| I-4 | Anuncio de participación de la organización en proyecto, licitación o concesión con contraparte china en energía, minería, puertos o telecomunicaciones | Cambio material de exposición según el criterio de KJ-2; requiere revisión de superficie | Interna / corporativa | Asuntos Corporativos |
| I-5 | Compromiso público de una entidad gubernamental chilena o de un operador regional con el que tengamos conectividad | Riesgo de compromiso indirecto por tercero de confianza | OSINT / enlace | Célula CTI |
| I-6 | Aviso de ANCI o CSIRT Nacional sobre actividad de actores con nexo chino en sectores regulados | Posible obligación de notificación bajo Ley 21.663 según el efecto | Autoridad | Cumplimiento |

---

**Indicadores añadidos en la revisión v1.2**

| # | Indicador observable | Qué señalaría | Disciplina | Responsable |
|---|---|---|---|---|
| I-8 | **Publicación de los países y las operadoras del clúster `DarkWire`** | Convierte `KJ-9` de amenaza regional genérica en exposición concreta, o la descarta para Chile. **Es el indicador de mayor valor de la revisión** | OSINT | Célula CTI |
| I-9 | Corroboración o refutación de la tesis del suministrador compartido por un segundo proveedor | Mueve `KJ-8` de probable a cualquiera de los dos extremos, y con él toda la enmienda de §O-1 | OSINT | Célula CTI |
| I-10 | **Publicación de una comparación de binarios entre `CopperDoor` y `SparroWocky`** | Determina si son el mismo fichero o dos derivados. De ello depende cuánto se puede atribuir (`KJ-11`, §3.5-ix) | OSINT | Célula CTI |
| I-11 | Aparición de infraestructura de mando **alojada en Chile** asociada a este ecosistema | Es el rasgo operativo distintivo de `DarkWire`. Un C2 nacional anula la detección geográfica y exige revisar las reglas de egreso | OSINT / telemetría | Célula CTI / SOC |
| I-12 | Nueva publicación de ESET que confirme o matice el reemplazo de `SparrowDoor` por `CopperDoor` | Es la fuente que la investigación nueva cita y que no se ha leído (`G-6`) | OSINT | Célula CTI |

---

# NIVEL TÁCTICO
### Para: Analistas de SOC · Ingeniería de Detección · Threat Hunting · Horizonte: días–semanas

## T-1. Cadena de intrusión

<!-- cti:stages title="Del servidor expuesto al implante que no aparece en ninguna parte" dwell="next" -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 01 · Borde | Servidor expuesto a Internet | Exchange alcanzable públicamente · webshell `.ashx` sobre IIS · descarga por HTTP desde servidor de entrega |
| Etapa 02 · Dominio | Consolidación y credenciales | PowerShell remoto interactivo · PowerHub · `Invoke-BadPotato` a SYSTEM · volcado de SAM/SYSTEM/SECURITY · Impacket / NetExec · volcado de LSASS por DLL sideloading |
| Etapa 03 · Permanencia | Implante silencioso y recolección continua | Cargador tridente · SparroWocky reflexivo en memoria · servicio o clave Run · captura de pantalla cíclica · proxy TCP · exfiltración por el mismo canal TLS |

**Permanencia:** no publicada para esta campaña. El precedente del propio actor la sitúa en
**años, no en días**: la institución hondureña estuvo comprometida entre 2022 y 2024, y el
grupo fue dado por inactivo durante ese mismo periodo.

> ⚠ **Discrepancia de fuentes sobre el acceso inicial — decisión de este informe.** La
> matriz ATT&CK del análisis primario consigna `T1190` con el procedimiento «obtuvo acceso
> explotando servidores Exchange alcanzables públicamente». La prensa técnica derivada
> afirma que «el vector de acceso inicial es desconocido». Ambas cosas pueden ser ciertas a
> la vez: Exchange como vector observado, **sin CVE identificado**. Operamos sobre la
> lectura del análisis primario —tratar todo Exchange expuesto como superficie prioritaria—
> y consignamos en §14 la identificación del CVE como brecha de inteligencia crítica: **sin
> ella no hay medida preventiva posible, solo detectiva**.

## T-2. Mapa MITRE ATT&CK

<!-- cti:matrix -->

| Táctica | ID | Técnica | Procedimiento observado |
|---|---|---|---|
| Desarrollo de recursos | T1583.003 | Acquire Infrastructure: VPS | 18 servidores en VPS comerciales (Kaopu Cloud, LightNode, Constant/Vultr, Cogent, Latitude.sh, NTT America), varios en la región de las víctimas |
| Desarrollo de recursos | T1587.001 | Develop Capabilities: Malware | Desarrollo propio de SparroWocky y de su cargador; sustitución completa de SparrowDoor |
| Desarrollo de recursos | T1608.001 | Stage Capabilities: Upload Malware | Cargador tridente alojado en servidores de entrega controlados por el actor |
| Acceso inicial | T1190 | Exploit Public-Facing Application | Explotación de servidores Exchange alcanzables públicamente; en 2024, webshell `.ashx` sobre IIS y DotNetNuke |
| Ejecución | T1059.003 | Windows Command Shell | Comando `0x17` ejecuta órdenes vía `cmd.exe` |
| Ejecución | T1569.002 | Service Execution | El implante arranca directamente el servicio que crea para persistir |
| Ejecución | T1106 | Native API | Uso intensivo de la API nativa de Windows resuelta dinámicamente |
| Ejecución | T1559 | Inter-Process Communication | Mecanismo IPC para sincronizar instancias (`MyMutexName`, `MyEventName`, `MySharedMemName`) |
| Ejecución / Persistencia | T1574.001 | DLL Side-Loading | Ejecutable legítimo carga una DLL legítima **parcheada** (`.text` sustituida y punto de entrada redirigido) |
| Persistencia | T1547.001 | Registry Run Keys | Valor `SnapCart` en `SOFTWARE\Microsoft\Windows\CurrentVersion\Run` (HKLM o HKCU según privilegio) |
| Persistencia | T1543.003 | Windows Service | Servicio `ProcAuditManager` — «Tracks process creation, termination, and related system audit events» |
| Evasión | T1036.001 | Invalid Code Signature | La DLL parcheada conserva la firma digital, ya inválida, del módulo legítimo que suplanta |
| Evasión | T1036.004 | Masquerade Task or Service | Nombre y descripción de servicio verosímiles, indistinguibles de un componente de auditoría del sistema |
| Evasión | T1027.007 | Dynamic API Resolution | Algoritmo propio de hashing de API |
| Evasión | T1620 | Reflective Code Loading | Carga reflexiva del payload en memoria; cabeceras MZ/PE eliminadas antes de mapear |
| Evasión | T1564.010 | Process Argument Spoofing | Engancha `GetCommandLine[AW]`, `__[w]getmainargs`, `__p___argc`, `__p__[w]argv` para entregar argumentos desde stdin al PE cargado |
| Evasión | T1134.002 | Create Process with Token | Comando `0x2F`: duplica el token de cualquier sesión activa para ejecutar como otro usuario |
| Evasión | T1140 | Deobfuscate/Decode Files | Configuración y payload descifrados con RC4 desde el fichero `.dat` |
| Evasión | T1480.002 | Mutual Exclusion | Mutex para impedir instancias concurrentes |
| Evasión | T1070.004 | File Deletion | Autoborrado mediante `.bat` temporal que elimina ejecutable, DLL, payload y a sí mismo |
| Evasión | T1070.009 | Clear Persistence | Comando `0x13`: elimina su propia persistencia y termina |
| Evasión | *(sin ID)* | Call Stack Spoofing | SilentMoonwalk: cadenas JOP/ROP sobre gadgets de `kernel32.dll` para simular origen en `RtlUserThreadStart` / `BaseThreadInitThunk` |
| Evasión | *(sin ID)* | Thread Start Address Hiding | Engancha `CreateThread` con MinHook y usa `AnimateWindow` como trampolín; la dirección de inicio declarada es legítima |
| Descubrimiento | T1082 | System Information Discovery | Comando `0x10`: GUID, PID, hostname, IP de interfaces, usuario, versión de Windows, dominio |
| Descubrimiento | T1033 | System Owner/User Discovery | Usuario actual y usuarios con sesión activa (comando `0x2E`) |
| Descubrimiento | T1083 | File and Directory Discovery | Listado de ficheros y directorios en unidades mapeadas |
| Descubrimiento | T1120 | Peripheral Device Discovery | Comando `0x29`: enumeración de dispositivos de visualización |
| Recolección | T1113 | Screen Capture | Comando `0x2A`: captura cíclica cada 500 ms con compresión por diferencias |
| Recolección | T1005 | Data from Local System | Exfiltración de ficheros desde almacenamiento mapeado, en bloques de 4 kB |
| Mando y control | T1573.002 | Encrypted Channel: Asymmetric | TLS mediante Mbed TLS |
| Mando y control | T1573.001 | Encrypted Channel: Symmetric | RC4 por comando, con clave de 8 bytes regenerada en cada mensaje |
| Mando y control | T1095 | Non-Application Layer Protocol | TLS sobre TCP directo a IP, puertos 443 y 8080 |
| Mando y control | T1090.001 | Internal Proxy | Comandos `0x1A`–`0x1D`: proxy TCP y listener `PortmapReverseServer` |
| Mando y control | T1090.002 | External Proxy | Soporte de proxy HTTP (Negotiate/NTLM/Basic) y SOCKS5 para salir de la red |
| Exfiltración | T1041 | Exfiltration Over C2 Channel | Todo sale por la misma conexión por la que entran los comandos |

## T-3. Dónde atacamos en la Pirámide del Dolor

<!-- cti:pyramid -->

| Nivel | Qué contiene en este informe y qué vale | Valor |
|---|---|---|
| Hashes | Cinco SHA-1 de cargadores y de payload en memoria, más los de 2024. Perecederos: el cargador se recompila por objetivo. Solo para retrohunt, nunca como base de la defensa | Base · valor trivial |
| IP · Dominios | 18 servidores de mando en VPS comerciales con rotación mensual y **vida media inferior a la publicación de este informe**. Varios en la región: bloquear por geolocalización no sirve. Solo retrohunt | Valor bajo |
| Artefactos | Servicio `ProcAuditManager`, valor Run `SnapCart`, mutex `MyMutexName`, cadena `acdbenus`, cabecera `0x11328712`, trío de ficheros homónimos. Duraderos entre compilaciones, aunque los nombres concretos cambiarán tras la publicación | Valor medio |
| Herramientas | Mbed TLS, MinHook, COFF Loader, SilentMoonwalk, PowerHub, BadPotato, Impacket/NetExec. Todas públicas y legítimas en otros contextos: detectar por composición y contexto, jamás por presencia | Valor alto |
| TTP | **Ejecutable firmado que carga una DLL con firma inválida desde su propio directorio, acompañada de un `.dat` homónimo, que persiste como servicio y abre TLS a una IP sin nombre.** Esa frase es la detección. Sobrevivió al cambio completo de implante en agosto de 2025 | Cima · valor máximo |

> **Lectura de doctrina.** Este actor cambió de implante por completo y mantuvo intacta su
> doctrina de entrega. Eso es una declaración sobre dónde invertir: una regla escrita sobre
> el trío de ficheros y la firma inválida habría sobrevivido a la sustitución de SparrowDoor
> por SparroWocky; una biblioteca de hashes no habría sobrevivido ni al cambio de objetivo.

## T-4. Hipótesis de caza prioritarias

<!-- cti:accordion critical="^(H-1|H-2|H-3)\b" regional="^H-1[0-2]\b" -->

**H-1 — Trío de ficheros homónimos en directorio de aplicación.** Buscar en servidores y
estaciones cualquier directorio —especialmente fuera de `Program Files`, y con prioridad en
`C:\Users\Public`, `ProgramData`, `Temp` y rutas de perfil— que contenga simultáneamente un
`.exe` firmado, una `.dll` y un fichero de datos **con el mismo nombre base que la DLL** y
extensión `.dat`, `.doc`, `.bin` o similar. Fuente: inventario de ficheros del EDR o barrido
de sistema de ficheros. Ventana: 24 meses. Fidelidad esperada **alta**; falsos positivos:
instaladores portables y algunas suites de respaldo que sí usan este patrón legítimamente —
se resuelven en segundos mirando la firma de la DLL. Es la hipótesis de mayor rendimiento
del informe y la que sobrevive a cualquier cambio de nombres.

**H-2 — DLL con firma digital inválida cargada por proceso firmado.** Consultar todas las
cargas de módulo donde el proceso padre está firmado y válido, y el módulo cargado tiene
firma **presente pero inválida** —no ausente: inválida—. Esa combinación es la huella exacta
de una DLL legítima parcheada en su sección `.text`. Fuente: eventos de carga de imagen del
EDR con estado de firma. Ventana: 24 meses. Fidelidad **muy alta**; falsos positivos
escasos, típicamente software mal empaquetado o modificado por el propio fabricante.

**H-3 — Fichero con la cabecera mágica del payload.** Barrer el parque buscando ficheros
cuyos primeros cuatro bytes sean `12 87 32 11` (`0x11328712` en little-endian) o
`11 32 87 12`. Es un indicador estructural del formato de payload, independiente del nombre,
del tamaño y de la campaña. Fuente: barrido con YARA o equivalente. Ventana: 24 meses.
Fidelidad **muy alta**, falsos positivos prácticamente nulos. Requiere capacidad de barrido
de contenido, no solo de metadatos: si no la tenemos, es una brecha de §T-5, no una
hipótesis descartable.

**H-4 — Servicios con nombre verosímil creados fuera de ventana de cambio.** Revisar EID
7045 y 4697 en 24 meses buscando servicios cuyo `ImagePath` apunte a un ejecutable fuera de
`C:\Windows\System32` o `Program Files`, y en particular el nombre exacto `ProcAuditManager`
y su descripción «Tracks process creation, termination, and related system audit events».
Cruzar con el calendario de cambios: un servicio creado un domingo a las 03:00 y sin ticket
asociado es la definición de hallazgo. Fidelidad **alta** si hay retención; nula si no la hay.

**H-5 — Persistencia por clave Run con valor `SnapCart` o anómalo en servidores.** Consultar
`HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` y su equivalente `HKCU` en **servidores**
—donde una clave Run es de por sí sospechosa, a diferencia de una estación— buscando el valor
`SnapCart` y, en general, cualquier entrada que apunte a un ejecutable en directorio de
usuario o temporal. Fidelidad **alta** en servidores, media en estaciones.

**H-6 — Conexiones TLS salientes a IP literal sin resolución DNS previa.** Cazar sesiones TLS
a puerto 443 u 8080 cuyo destino sea una IP **que no fue precedida de una consulta DNS** en
los 60 segundos anteriores, originadas por procesos que no son navegadores ni clientes
conocidos. El implante se conecta directamente a IP configurada, sin dominio. Cruzar con los
18 destinos del Anexo A y con los ASN de los proveedores citados. Fidelidad **media**: los
falsos positivos son agentes de monitorización y actualizadores; el valor está en el cruce
con H-1 o H-2 sobre el mismo host.

**H-7 — Hilos cuya dirección de inicio apunta a `AnimateWindow` o a `user32.dll`.** El
implante engancha `CreateThread` y declara `AnimateWindow` como dirección de inicio. Un hilo
cuyo punto de arranque sea esa función —o cualquier función de `user32.dll` en un proceso sin
interfaz gráfica— es una anomalía de altísimo valor. Fuente: telemetría de creación de hilos
del EDR, si existe. Fidelidad **muy alta**, volumen muy bajo. Es la detección que convierte
en indicador la propia técnica de evasión del actor.

**H-8 — Carga de ficheros MUI desde `C:\Windows\System32\en-US\` por procesos no
localizados.** El implante camufla su proceso anfitrión cargando ficheros MUI en inglés. En
un parque mayoritariamente en español, un proceso que lee MUI de `en-US` sin motivo es una
señal barata y poco ruidosa. Fidelidad **media-alta**; requiere telemetría de acceso a
ficheros.

**H-9 — Cadena de autoborrado por `.bat` con `timeout /t` y `del %0`.** Buscar creación y
ejecución de ficheros `.bat` temporales cuya línea de órdenes contenga `timeout /t` seguido
de varios `del` con `/f /q` y un `del "%0"` final. Es el rastro que deja la limpieza del
implante y **puede ser lo único que quede** si el adversario ya se retiró. Fidelidad **alta**,
falsos positivos bajos; especialmente valiosa en caza retrospectiva.

**H-10 — Artefactos de la fase de consolidación de 2024.** Aunque pertenecen a la campaña
anterior, conservan valor retrospectivo: webshells `.ashx` en directorios de DotNetNuke o
IIS —en particular `DotNetNuke.ashx` y `C:\users\public\s.ashx`—, ejecución de PowerHub,
invocaciones de `Invoke-BadPotato`, y volcados de las ramas `SYSTEM`, `SAM` y `SECURITY`.
Fidelidad **alta**; cualquier hallazgo abre incidente de inmediato.

**H-11 — Conectividad y federación con contrapartes gubernamentales regionales.** Enumerar
—y luego vigilar— todo túnel, federación de identidad, conector de correo, transferencia de
ficheros o acceso de proveedor que nos una con entidades de los ocho países afectados. No es
una consulta de SIEM: es un trabajo de arquitectura que habilita la vigilancia posterior. Es
la hipótesis que cubre el escenario del pre-mortem de §O-6.

**H-12 — Exchange e IIS expuestos: inventario y estado real.** Enumerar todo Exchange e IIS
alcanzable desde Internet, incluidos los olvidados en modo híbrido y los publicados por
error, con su versión y nivel de parche. Revisar además la existencia de ficheros `.ashx`,
`.aspx` o `.asmx` con fecha de modificación posterior al despliegue de la aplicación.
Fidelidad **alta**; es prevención, no caza, pero sin ella la caza es perpetua.

## T-5. Brechas de visibilidad que hay que cerrar primero

| Brecha | Por qué importa aquí |
|---|---|
| Sin estado de firma en los eventos de carga de módulo | H-2 —la hipótesis de mayor fidelidad del informe— es inejecutable. Sin ella no se distingue una DLL parcheada de una legítima |
| Sin capacidad de barrido de contenido (YARA) sobre el parque | H-3 es inejecutable. Se pierde el único indicador que no depende de nombres ni de infraestructura |
| Retención de EID 7045 / 4697 inferior a 12 meses | H-4 queda limitada a una ventana en la que este actor, con permanencia de años, casi con certeza no aparecerá |
| Sin telemetría de creación de hilos | H-7 es inejecutable, y con ella se pierde la detección que ataca la técnica de evasión más distintiva del implante |
| Sin registro de conexiones salientes por proceso, con IP y proceso correlacionados | H-6 se degrada a un bloqueo de IP inútil: se sabe que alguien habló con el destino, no quién |
| Sin inventario vivo de superficie expuesta a Internet | H-12 se convierte en un proyecto en lugar de una consulta, y el vector de acceso inicial queda sin cubrir |

---

# NIVEL TÉCNICO
### Para: Ingeniería de detección · Automatización · TIP/SIEM · Vida útil: días–semanas

## X-1. Arsenal y capacidad

| Propiedad | Valor |
|---|---|
| Implante principal | **SparroWocky** — backdoor modular en C++, versión 1.8, marca de compilación 2025-11-17. Nombre derivado de la primera estrofa de *Jabberwocky* de Lewis Carroll, incrustada en las primeras muestras |
| Implante anterior | **SparrowDoor** — dos variantes documentadas en 2025: una emparentada con CrowDoor de Earth Estries, otra modular con sistema de complementos. Abandonado en agosto de 2025 |
| Implante secundario | **ShadowPad**, usado por primera vez por el grupo en julio de 2024. Plataforma compartida entre múltiples grupos con nexo chino |
| Esquema de entrega | Cargador «tridente»: ejecutable legítimo + DLL legítima **parcheada** (sección `.text` sustituida y punto de entrada redirigido) + payload `.dat` cifrado con RC4 |
| Cabecera del payload | Valor mágico `0x11328712`, tamaño de configuración, tamaño de payload, clave RC4 de 16 bytes |
| Bibliotecas de terceros | Mbed TLS (canal), MinHook (enganches), COFF Loader (ejecución de BOF), variante de SilentMoonwalk/StackMoonwalk (falsificación de pila) |
| Criptografía | TLS para el transporte; RC4 para el payload en disco y para cada mensaje de comando, con clave de 8 bytes regenerada por mensaje. Cadena de personalización del DRBG: `acdbenus` |
| Canal de mando | TCP directo a IP configurada, puertos 443 y 8080. Saludo inicial: `0x11223344` en big-endian. Reintento cada 10 segundos. Soporte de proxy de sistema, HTTP (Negotiate/NTLM/Basic, User-Agent `Mozilla/5.0`) y SOCKS5 |
| Persistencia | Servicio de Windows (`ProcAuditManager`) o valor de registro Run (`SnapCart`), según configuración y privilegio |
| Extensibilidad | Ejecución de **Beacon Object Files** en memoria (comando `0x14`) y de PE externos con tiempo límite (`0x16`). Los complementos nunca tocan disco |
| Plataformas | Windows (x64) |
| Firmas del proveedor | `Win64/Agent.HUP`, `Win64/Agent.ISF` (cargadores), `Win64/Agent.ASW` (implante) |

**Conjunto de comandos observado.** `0x10` huella del sistema · `0x11` sesión interactiva ·
`0x12` terminar proceso · `0x13` eliminar persistencia y terminar · `0x14` cargar y ejecutar
BOF · `0x16` ejecutar PE con tiempo límite · `0x17` ejecutar orden por `cmd.exe` · `0x1A`
proxy TCP · `0x1B`–`0x1D` gestión del listener `PortmapReverseServer` · `0x1E`–`0x26`
operaciones de ficheros y directorios · `0x27` subida en bloques de 4 kB · `0x28` descarga ·
`0x29` enumerar dispositivos de visualización · `0x2A` captura de pantalla cíclica (500 ms,
compresión por diferencias) · `0x2E` enumerar sesiones de usuario · `0x2F` ejecutar como
otro usuario por duplicación de token · `0x30`–`0x31` eco · `0x33` ejecución arbitraria vía
`CreateProcess`.

## X-2. Artefactos de host persistentes entre builds

<!-- cti:cards -->

| Categoría | Artefactos | Etiqueta |
|---|---|---|
| Servicio | Nombre y nombre mostrado `ProcAuditManager`; descripción «Tracks process creation, termination, and related system audit events» | `persistencia` |
| Registro | Valor `SnapCart` en `SOFTWARE\Microsoft\Windows\CurrentVersion\Run` (HKLM o HKCU) | `persistencia` |
| Objetos de sincronización | `MyMutexName`, `MyEventName`, `MySharedMemName` | `ejecución` |
| Ficheros del cargador | DLL parcheadas observadas: `winfsp-x64.dll`, `DukeQt.dll`. Payload `.dat` con el mismo nombre base que el módulo | `entrega` |
| Estructura del payload | Cabecera `0x11328712` + tamaños + clave RC4 de 16 bytes | `entrega` |
| Cadena del DRBG | `acdbenus` como cadena de personalización | `mando y control` |
| Rutas de camuflaje | Lectura de ficheros MUI desde `C:\Windows\System32\en-US\` | `evasión` |
| Autoborrado | `.bat` temporal con `timeout /t 2` y `del` sobre ejecutable, DLL, payload y sí mismo | `limpieza` |
| Herencia 2024 | `K7AVMScn.exe` + `K7AVWScn.dll` + `K7AVWScn.doc`; servicio `K7Soft`; `imjp14k.exe` + `imjp14k.dll` + `imjp14k.dll.dat` (ShadowPad); `HKLM\Software\CLASSES\CLSID\ID` como identificador de sesión | `retrohunt` |

> ⚠ **Caducidad de estos artefactos.** Los **nombres** —`ProcAuditManager`, `SnapCart`,
> `winfsp-x64.dll`— casi con certeza cambiarán en las semanas siguientes a la publicación
> del análisis, el 17-09-2026. La **estructura** —trío de ficheros, firma inválida, cabecera
> mágica, mutex fijo— es lo que persiste. Escribir las reglas en ese orden de prioridad.

## X-3. Lógica de detección prioritaria

<!-- cti:detections -->

**D-1 · CRÍTICO — DLL con firma inválida cargada por proceso firmado**

```
image_load.signature_status == "invalid"
AND process.signature_status == "valid"
AND image_load.path NOT STARTSWITH ("C:\Windows\System32\", "C:\Program Files\")
AND image_load.path DIRNAME == process.path DIRNAME
```

→ Alerta crítica con aislamiento automático del host. La combinación «firma presente pero inválida en el mismo directorio que un ejecutable firmado» no tiene explicación benigna frecuente y es el corazón del esquema tridente.

**D-2 · CRÍTICO — Payload del cargador por cabecera mágica**

```yara
rule FamousSparrow_SparroWocky_Payload_Header
{
    meta:
        description = "Cabecera del payload cifrado del cargador tridente de SparroWocky"
        reference   = "CTI-2026-017"
        author      = "Celula CTI"
        date        = "2026-09-21"
    strings:
        $magic = { 12 87 32 11 }
    condition:
        $magic at 0 and filesize < 5MB
}
```

→ Cualquier coincidencia abre incidente. Ejecutar como barrido retrospectivo sobre todo el parque, no solo como regla en tiempo real.

**D-3 · CRÍTICO — Creación del servicio de persistencia**

```
EID 7045
AND (service_name == "ProcAuditManager"
     OR service_description CONTAINS "Tracks process creation, termination, and related system audit events"
     OR (image_path NOT STARTSWITH ("C:\Windows\", "C:\Program Files") AND image_path CONTAINS_ANY ("\Users\", "\ProgramData\", "\Temp\")))
```

→ Contención automática en servidores; en estaciones, alerta de prioridad alta con verificación contra el calendario de cambios.

**D-4 · ALTO — Objetos de sincronización del implante**

```
mutex_created IN ("MyMutexName", "MySharedMemName")
OR event_created == "MyEventName"
```

→ Alta fidelidad mientras el actor no los cambie, y coste de implantación casi nulo. Tratar como detección de oportunidad: alta señal hoy, obsolescencia probable en semanas.

**D-5 · ALTO — Hilo con dirección de inicio en `AnimateWindow`**

```
thread_create.start_address_symbol == "user32.dll!AnimateWindow"
OR (thread_create.start_module == "user32.dll" AND process.has_gui == false)
```

→ Alerta de prioridad alta. Detecta directamente la técnica de ocultación de dirección de hilo del implante, con volumen legítimo prácticamente nulo en servidores.

**D-6 · ALTO — Persistencia por clave Run en servidor**

```
registry.path ENDSWITH "\Microsoft\Windows\CurrentVersion\Run"
AND host.role == "server"
AND (registry.value_name == "SnapCart"
     OR registry.data CONTAINS_ANY ("\Users\Public\", "\ProgramData\", "\AppData\", "\Temp\"))
```

→ Alerta alta. En un servidor, una clave Run nueva es por sí sola una anomalía de configuración, con independencia de este actor.

**D-7 · MEDIO — Autoborrado del implante**

```
process.name == "cmd.exe"
AND cmdline MATCHES "timeout\s+/t\s+\d+"
AND cmdline CONTAINS "del "
AND cmdline CONTAINS "%0"
```

→ Alerta media, pero **preservar de inmediato** el host y su telemetría: la ejecución de este patrón indica que el adversario está retirándose y que la ventana forense se está cerrando.

**D-8 · MEDIO — Webshell reciente en directorio web (retrohunt de la campaña de 2024)**

```
file.extension IN (".ashx", ".aspx", ".asmx")
AND file.path CONTAINS_ANY ("\inetpub\", "\DotNetNuke\", "\wwwroot\")
AND file.created > application_deployment_date
```

→ Revisión manual de cada resultado. Buscar específicamente `DotNetNuke.ashx` y `C:\users\public\s.ashx`.

> ⚠ **Regla de operación.** D-1, D-2 y D-3 deben ejecutar **contención automática sin
> escalado humano** en servidores. El argumento no es la velocidad del adversario —aquí es
> lento— sino la asimetría del coste: el falso positivo cuesta una hora de un administrador;
> el falso negativo cuesta dos años de exfiltración continua que nadie va a notar porque
> **no habrá ningún otro síntoma**.

**D-7 · ALTO — (v1.2) Resolución o conexión al dominio que vincula los dos expedientes**

```
destination.domain ENDS_WITH_ANY (
      "amelicen.com", "seosnskorea.com", "jamvybez.com",
      "artfingo.com", "faceorkut.com", "aauctioneer.com" )
```

→ Investigación prioritaria con plazo de una hora, y **retrohunt de 24 meses**. El primero
de la lista es el dominio que la fuente señala como punto de contacto entre `DarkWire` y
este actor: fue servidor de mando de `SparrowDoor` y aparece en la infraestructura de
`CopperDNS`. Los otros cinco son los dominios publicados de `DarkWire`.

**D-8 · ALTO — (v1.2) Tráfico TCP crudo encapsulado en TLS hacia el puerto 443 sin negociación coherente**

```
network.direction == "outbound" AND destination.port == 443
AND tls.established == true
AND NOT ( tls.client.ja4 IN ( <huellas de navegadores y clientes conocidos> ) )
AND destination.as.number IN ( 20473, 138915, 396356, 6134, 212238, 136258 )
```

→ Investigación prioritaria. `CopperDoor` encapsula TCP crudo dentro de TLS sobre el puerto
443, y los seis sistemas autónomos son los que la fuente documenta para esa familia. **La
condición del sistema autónomo es la que caduca; la de la huella del cliente TLS no.**

**D-9 · CRÍTICO — (v1.2) Tunelado de mando sobre consultas DNS de tipo MX**

```
dns.question.type == "MX"
AND ( dns.question.name_length > 50
      OR dns.question.name MATCHES_REGEX "^[A-Za-z0-9+/=_-]{30,}\." )
AND source NOT IN ( <servidores de correo propios> )
```

→ Contención automática. `CopperDNS` tunela su canal de mando en consultas DNS de tipo
`MX`. **Un equipo que no es un servidor de correo no tiene ninguna razón para emitir
consultas MX**, y menos con etiquetas largas y codificadas. Es una detección conductual que
no depende de ningún indicador.

**D-10 · ALTO — (v1.2) Certificado TLS autofirmado que se hace pasar por un resolutor público**

```
tls.server.certificate.subject.common_name IN ( "8.8.8.8", "1.1.1.1", "9.9.9.9" )
AND tls.server.certificate.self_signed == true
```

```
// Variante por huella, de fidelidad máxima mientras el actor no rote el certificado:
tls.server.certificate.fingerprint.sha256 ==
  "ee4a8b81fe3864582efc27a77f806990e2602dcc36447ddda4b3a230a473d575"
OR tls.server.certificate.fingerprint.sha1 ==
  "de32c58a8087cc4f24b9eb65c8ff4516f0f65f13"
```

→ Contención automática. El certificado de los nodos de `CopperDNS` tiene **sujeto y emisor
`CN=8.8.8.8`**, es autofirmado y está reutilizado en varios nodos. La primera variante es la
conductual y la que perdura: **ningún servidor legítimo presenta un certificado autofirmado
cuyo nombre común sea la dirección de un resolutor DNS público.**

**D-11 · MEDIO — (v1.2) Artefactos de host del ecosistema Sparrow**

```
( process.command_line CONTAINS "RasiUwpApp" )                      // regla de cortafuegos
OR ( process.command_line MATCHES_REGEX "(?i)net\s+user\s+admin\$" )  // cuenta creada
OR ( registry.path CONTAINS "LocalAccountTokenFilterPolicy"
     AND registry.data.strings == "1" )
OR ( file.directory IN ( "C:\\Program Files\\7-Zip\\Lang",
                         "C:\\Windows\\debug",
                         "C:\\ProgramData\\vmware\\logs",
                         "C:\\ProgramData\\Oracle\\Java",
                         "C:\\ProgramData\\USOShared",
                         "C:\\ProgramData\\Waves" )
     AND file.extension IN ( "dll", "dat", "png" ) )
```

→ Investigación prioritaria para las tres primeras condiciones; en el día para la cuarta.
La cuenta `admin$` con contraseña fija, la regla de cortafuegos `RasiUwpApp` que abre el
puerto 445 y la política que desactiva el filtrado de token para cuentas locales son
**artefactos de configuración, no binarios**: perduran entre compilaciones. Las seis rutas
son directorios legítimos existentes que el cargador usa para alojarse.

## X-4. Consultas de caza

```kql
// H-1 · Trío de ficheros del cargador tridente: exe + dll + fichero de datos homónimo
// Microsoft Defender XDR — ventana de 24 meses, ejecutar por lotes mensuales
let candidatos = DeviceFileEvents
| where Timestamp > ago(730d)
| where FolderPath !startswith "C:\\Windows\\" and FolderPath !startswith "C:\\Program Files"
| extend Dir = strcat_array(array_slice(split(FolderPath, "\\"), 0, -2), "\\")
| extend Base = tostring(split(FileName, ".")[0]), Ext = tostring(split(FileName, ".")[-1])
| where Ext in~ ("exe", "dll", "dat", "doc", "bin", "log")
| distinct DeviceName, Dir, Base, Ext, FileName, SHA1;
candidatos
| summarize Exts = make_set(Ext), Ficheros = make_set(FileName) by DeviceName, Dir, Base
| where set_has_element(Exts, "dll") and array_length(Exts) >= 2
| where Exts has_any ("dat", "doc", "bin", "log")
| project DeviceName, Dir, Base, Ficheros
```

```kql
// H-2 · DLL con firma inválida cargada por proceso firmado, desde su propio directorio
DeviceImageLoadEvents
| where Timestamp > ago(730d)
| where InitiatingProcessSignatureStatus == "Valid"
| where FolderPath !startswith "C:\\Windows\\System32" and FolderPath !startswith "C:\\Program Files"
| join kind=inner (
    DeviceFileCertificateInfo
    | where IsSigned == true and IsTrusted == false
    | project SHA1, SignatureStatus = "Invalid", Signer
  ) on SHA1
| project Timestamp, DeviceName, InitiatingProcessFileName, FileName, FolderPath, Signer, SHA1
| sort by Timestamp asc
```

```kql
// H-6 · TLS saliente a IP literal sin resolución DNS previa, desde proceso no navegador
let ventana = 60s;
let dns = DeviceEvents
| where ActionType == "DnsQueryResponse"
| extend IPs = extract_all(@"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", tostring(AdditionalFields))
| mv-expand IP = IPs to typeof(string)
| project DnsTime = Timestamp, DeviceName, IP;
DeviceNetworkEvents
| where Timestamp > ago(90d)
| where RemotePort in (443, 8080) and RemoteIPType == "Public"
| where InitiatingProcessFileName !in~ ("chrome.exe","msedge.exe","firefox.exe","svchost.exe")
| join kind=leftouter dns on DeviceName, $left.RemoteIP == $right.IP
| where isnull(DnsTime) or Timestamp - DnsTime > ventana
| summarize Conexiones = count(), Primera = min(Timestamp), Ultima = max(Timestamp)
    by DeviceName, InitiatingProcessFileName, InitiatingProcessFolderPath, RemoteIP
| where Conexiones > 5
| sort by Conexiones desc
```

```kql
// H-7 · Hilos cuya dirección de inicio cae en user32.dll (AnimateWindow como trampolín)
// Requiere telemetría de creación de hilos; si no existe, es la brecha T-5 número 4
DeviceEvents
| where Timestamp > ago(180d)
| where ActionType == "CreateRemoteThreadApiCall" or ActionType == "ThreadCreated"
| extend Start = tostring(AdditionalFields.StartAddressModule)
| where Start has "user32.dll"
| project Timestamp, DeviceName, InitiatingProcessFileName, InitiatingProcessFolderPath, Start
```

```yaml
# Sigma — Servicio de persistencia con ruta fuera de directorios de sistema
title: Creacion de servicio con ImagePath en directorio de usuario o temporal
id: 8f3c1a92-0d54-4c7b-b1a6-2f77c9b0e401
status: experimental
description: >
  Detecta la creacion de servicios de Windows cuyo ejecutable reside fuera de
  System32 o Program Files, patron de persistencia de SparroWocky (FamousSparrow).
  Incluye el nombre y la descripcion observados en la campana latinoamericana 2025-2026.
references:
  - CTI-2026-017
author: Celula CTI
date: 2026/09/21
tags:
  - attack.persistence
  - attack.t1543.003
  - attack.defense_evasion
  - attack.t1036.004
logsource:
  product: windows
  service: system
detection:
  seleccion:
    EventID: 7045
  nombres_conocidos:
    ServiceName: 'ProcAuditManager'
  ruta_anomala:
    ImagePath|contains:
      - '\Users\'
      - '\ProgramData\'
      - '\Temp\'
      - '\AppData\'
  condition: seleccion and (nombres_conocidos or ruta_anomala)
falsepositives:
  - Instaladores de software empresarial mal empaquetados
  - Agentes de gestion desplegados fuera de rutas estandar
level: high
```

```yaml
# Sigma — Autoborrado del cargador mediante script por lotes
title: Script por lotes de autoborrado con eliminacion de si mismo
id: c41b77e6-9a2f-4b18-8d30-5e6a1c9f2d88
status: experimental
description: >
  Detecta la cadena de limpieza empleada por SparroWocky al desinstalarse:
  espera con timeout, borrado forzado de varios ficheros y borrado del propio script.
  Indica retirada del adversario y cierre inminente de la ventana forense.
references:
  - CTI-2026-017
author: Celula CTI
date: 2026/09/21
tags:
  - attack.defense_evasion
  - attack.t1070.004
logsource:
  category: process_creation
  product: windows
detection:
  proceso:
    Image|endswith: '\cmd.exe'
  espera:
    CommandLine|contains: 'timeout /t'
  borrado:
    CommandLine|contains|all:
      - 'del '
      - '/f'
      - '/q'
  autoborrado:
    CommandLine|contains: '%0'
  condition: proceso and espera and borrado and autoborrado
falsepositives:
  - Rutinas de desinstalacion legitimas de software empaquetado
level: medium
```

## X-5. Mitigaciones de configuración con efecto directo

| Control | Corta |
|---|---|
| Retirar de Internet todo Exchange e IIS que no tenga justificación vigente; publicar el resto tras proxy con autenticación previa | La Etapa 01 completa: el único vector de acceso inicial observado |
| Regla WDAC/AppLocker que impida la carga de DLL no firmadas o con firma inválida en servidores | El cargador tridente, con independencia del nombre del binario abusado |
| Política que restrinja la creación de servicios a cuentas de gestión y desde rutas autorizadas | La persistencia principal del implante (`T1543.003`) |
| Denegar escritura en directorios de aplicación al usuario del servicio web y separar el directorio de contenido del de ejecución | La escritura de webshells `.ashx` y la colocación del trío de ficheros |
| Salida a Internet desde servidores solo a través de proxy explícito con lista de permitidos por destino | La conexión TLS directa a IP literal, que es como el implante llama a casa |
| Desactivar la carga de MUI innecesarios y normalizar el idioma del parque | Degrada el camuflaje de proceso anfitrión y hace visible H-8 |
| Retención mínima de 12 meses para EID 7045/4697, carga de módulos y conexiones salientes por proceso | No corta ningún paso, pero es el prerrequisito de que exista la caza retrospectiva de §T-4 |

---

## 14. Brechas de inteligencia y nuevos requisitos de colección

| # | Brecha | Impacto en el juicio | Requisito propuesto | Prioridad |
|---|---|---|---|---|
| G-1 | **Vector de acceso inicial sin CVE identificado**, con discrepancia explícita entre fuentes | KJ-3 y toda §T-1 quedan sin medida preventiva: solo se puede detectar, no prevenir | Solicitar al proveedor y a pares regionales el detalle del compromiso de Exchange; vigilar publicaciones de seguimiento | Crítica |
| G-2 | **Fuente primaria única** para toda la caracterización técnica | Si el análisis es erróneo o no representativo, cae toda la sección técnica (supuesto clave de §O-6) | Buscar corroboración independiente: sandbox propio sobre muestra, o informe de un segundo proveedor | Crítica |
| G-3 | **Sin telemetría propia** | §O-4 vacía; KJ-5 no pasa de inferencia | Ejecutar §T-4 y volcar resultados en la versión 1.1 de este informe | Crítica |
| G-4 | **Ausencia de visibilidad regional chilena** sobre este actor | No se puede confirmar ni descartar presencia en el país | Enlace con CSIRT Nacional / ANCI y con pares del sector; solicitar indicadores y contexto | Alta |
| G-5 | **Disputa de alias con Salt Typhoon sin resolver** | KJ-7 con confianza moderada; riesgo de cobertura de detección nominal pero falsa | Vigilar publicación de indicadores por Microsoft; no mezclar bibliotecas de detección hasta entonces | Alta |
| G-6 | **Sin muestras de SparroWocky en nuestro poder** | No podemos validar ni ajustar D-2 ni las consultas de §X-4 contra el binario real | Solicitar muestra a proveedor bajo acuerdo; alternativamente, validar la regla YARA contra el script de extracción publicado | Media |
| G-7 | **Se desconoce qué objetivos NO fueron comprometidos** entre los seleccionados | Impide estimar la tasa de éxito del actor y, con ella, la eficacia real de los controles estándar | Requisito de colección a largo plazo; probablemente irresoluble con fuente abierta | Baja |

---

**Brechas añadidas en la revisión v1.2**

| # | Brecha | Impacto en el juicio | Requisito propuesto | Prioridad |
|---|---|---|---|---|
| G-5 | **La fuente no nombra los países ni las operadoras del clúster `DarkWire`** | **Es la brecha que determina si esta revisión describe una amenaza o un contexto.** `KJ-9` no se puede convertir en exposición concreta: no se sabe si Chile está entre los países ni si alguna operadora nacional está entre las tres | Vigilar publicaciones de seguimiento de Check Point y de otros proveedores; **y considerar una consulta directa al equipo nacional de respuesta a incidentes**, que es quien podría saberlo y quien tendría motivo para avisar. Indicador `I-8` | **Crítica** |
| G-6 | **Sin corroboración independiente de la tesis del suministrador compartido** | `KJ-8` queda en probable con confianza moderada, y de él dependen la enmienda de `KJ-3` y toda la enmienda del expediente de alias | Leer la publicación de ESET sobre el reemplazo de `SparrowDoor` por `CopperDoor` y el análisis de Positive Technologies que la fuente cita. Indicadores `I-9` e `I-12` | Alta |
| G-7 | **Sin comparación publicada de binarios entre `CopperDoor` y `SparroWocky`** | `KJ-11` deja abierto si son el mismo fichero o dos derivados de una base común, y de eso depende cuánto se puede atribuir con cuánta confianza | Localizar o solicitar un análisis comparado. Indicador `I-10` | Alta |
| G-8 | Ausencia de mapeo MITRE ATT&CK en la fuente nueva | El §T-2 no se ha ampliado, para no atribuir a la fuente un mapeo que no hizo. **La consecuencia es que las técnicas del material nuevo no están en la matriz navegable** del informe | Construir el mapeo propio a partir de la prosa de la fuente, marcándolo como inferencia nuestra | Media |
| G-9 | **País de cada dirección del clúster `DarkWire`** | La afirmación de que el mando está en el país de la víctima es la más consecuente de la revisión —anula la detección geográfica— y no se puede verificar dirección por dirección | Resolución propia de geolocalización y de titularidad del rango sobre las 36 direcciones del Anexo A.2.2, **antes de bloquear ninguna** | Alta |

---

# ANEXOS

## Anexo A — Indicadores de compromiso

> ⚠ **Leer antes de usar.** Los IOC son el nivel más perecedero y menos valioso del
> producto. Toda la infraestructura listada fue observada por última vez antes del
> 17-09-2026 y **es casi seguro que haya rotado tras la publicación del análisis**. Se
> entregan con contexto, confianza y acción permitida; **no** como lista suelta para cargar
> en un bloqueo perimetral y dar el trabajo por hecho. El valor real de esta tabla es el
> retrohunt de 24 meses, no el bloqueo.

### A.1 — Indicadores de la emisión original (septiembre de 2026)

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Acción permitida |
|---|---|---|---|---|
| sha1 | `3209689E509205CCDB7E49062B7B407DDC23CAC1` | Cargador SparroWocky — `winfsp-x64.dll` parcheada | Alta | Bloqueo + retrohunt |
| sha1 | `52C6646759CF6037BB17466203631C4BD794532F` | Cargador SparroWocky — `winfsp-x64.dll` parcheada | Alta | Bloqueo + retrohunt |
| sha1 | `99E7070B5AF24A0FE1E6FEBE5954B03CB385E91F` | Cargador SparroWocky — `DukeQt.dll` parcheada | Alta | Bloqueo + retrohunt |
| sha1 | `44F0A22B143B79FA760BF31E14C8FFF714C8A2A1` | SparroWocky descifrado, solo en memoria | Alta | Retrohunt (no aparecerá en disco) |
| sha1 | `9AA9FF61BC63CCAB9074FE837F39C980CA9DDC8C` | SparroWocky descifrado, solo en memoria | Alta | Retrohunt (no aparecerá en disco) |
| ipv4 | `216.238.110[.]120` | C2 SparroWocky · Constant Company/Vultr · 2025-12-11 | Alta | Bloqueo + retrohunt |
| ipv4 | `216.238.105[.]53` | C2 SparroWocky · Constant Company/Vultr · 2026-01-22 | Alta | Bloqueo + retrohunt |
| ipv4 | `38.60.241[.]193` | C2 SparroWocky · Kaopu Cloud Brasil · 2026-01-22 | Alta | Bloqueo + retrohunt |
| ipv4 | `149.104.90[.]203` | C2 SparroWocky · BEDGE CO LIMITED · 2026-01-22 | Alta | Bloqueo + retrohunt |
| ipv4 | `38.60.224[.]235` | C2 SparroWocky · Kaopu Cloud HK · 2026-02-24 | Alta | Bloqueo + retrohunt |
| ipv4 | `149.104.87[.]228` | C2 SparroWocky · LightNode México · 2026-02-24 | Alta | Bloqueo + retrohunt |
| ipv4 | `38.54.57[.]17` | C2 SparroWocky · LightNode Brasil · 2026-02-25 | Alta | Bloqueo + retrohunt |
| ipv4 | `38.60.224[.]51` | C2 SparroWocky · Kaopu Cloud HK · 2026-02-25 | Alta | Bloqueo + retrohunt |
| ipv4 | `216.238.92[.]2` | C2 SparroWocky · Constant Company/Vultr · 2026-02-25 | Alta | Bloqueo + retrohunt |
| ipv4 | `38.60.209[.]106` | C2 SparroWocky · Kaopu Cloud HK · 2026-02-26 | Alta | Bloqueo + retrohunt |
| ipv4 | `130.94.101[.]82` | C2 SparroWocky · NTT America · 2026-02-26 | Alta | Bloqueo + retrohunt |
| ipv4 | `140.99.164[.]199` | C2 SparroWocky · cliente privado · 2026-02-26 | Alta | Bloqueo + retrohunt |
| ipv4 | `38.60.241[.]127` | C2 SparroWocky · Cogent Communications · 2026-03-04 | Alta | Bloqueo + retrohunt |
| ipv4 | `38.60.241[.]65` | C2 SparroWocky · Cogent Communications · 2026-03-10 | Alta | Bloqueo + retrohunt |
| ipv4 | `38.60.197[.]55` | C2 SparroWocky · Kaopu Cloud HK · 2026-03-16 | Alta | Bloqueo + retrohunt |
| ipv4 | `216.238.121[.]164` | C2 SparroWocky · Constant Company/Vultr · 2026-03-16 | Alta | Bloqueo + retrohunt |
| ipv4 | `77.111.101[.]40` | C2 SparroWocky · Latitude.sh · 2026-05-20 | Alta | Bloqueo + retrohunt |
| ipv4 | `91.148.134[.]115` | C2 SparroWocky · Charles-R Paquet · 2026-06-17 | Alta | Bloqueo + retrohunt |
| ipv4 | `43.254.216[.]195` | Campaña 2024 · servidor de entrega y C2 · Hongkong Wen Jing Network · 2024-06-27 | Moderada | Solo retrohunt |
| ipv4 | `45.131.179[.]24` | Campaña 2024 · C2 de SparrowDoor · XNNET LLC · 2024-07-05 | Moderada | Solo retrohunt |
| domain | `amelicen[.]com` | Campaña 2024 · dominio de C2 de SparrowDoor | Moderada | Solo retrohunt |
| ipv4 | `103.85.25[.]166` | Campaña 2024 · C2 de SparrowDoor · Starry Network Limited · 2024-06-06 | Moderada | Solo retrohunt |
| ipv4 | `216.238.106[.]150` | Campaña 2024 · C2 de ShadowPad · Vultr · 2024-03-11 | Moderada | Solo retrohunt |
| ipv4 | `27.102.113[.]240` | Infraestructura compartida con GhostEmperor en 2021 | Baja | Solo retrohunt histórico |
| sha1 | `C26F04790C6FB7950D89AB1B08207ACE01EFB536` | Campaña 2024 · webshell `DotNetNuke.ashx` | Moderada | Bloqueo + retrohunt |
| sha1 | `EF189737FB7D61B110B9293E8838526DCE920127` | Campaña 2024 · cargador de SparrowDoor `libvlc.dll` | Moderada | Bloqueo + retrohunt |
| sha1 | `1B06E877C2C12D74336E7532BC0ECF761E5FA5D4` | Campaña 2024 · cargador de SparrowDoor `K7AVWScn.dll` | Moderada | Bloqueo + retrohunt |
| sha1 | `5265E8EDC9B5F7DD00FC772522511B8F3BE217E3` | Campaña 2024 · cargador de ShadowPad `imjp14k.dll` | Moderada | Bloqueo + retrohunt |
| sha1 | `5DF3C882DB6BE14887182B7439B72A86BD28B83F` | Campaña 2024 · `taskhosk.exe` — SparrowDoor/HemiGate | Moderada | Bloqueo + retrohunt |
| sha1 | `BAED2895C80EB6E827A6D47C3DD7B8EFB61ED70B` | Campaña 2024 · huella del certificado TLS del C2 de ShadowPad, con formato que suplanta a Dell | Moderada | Retrohunt en telemetría TLS |
| artefacto | `ProcAuditManager` | Nombre y nombre mostrado del servicio de persistencia | Alta | Caza (véase D-3) |
| artefacto | `SnapCart` | Valor de la clave Run de persistencia | Alta | Caza (véase D-6) |
| artefacto | `MyMutexName` · `MyEventName` · `MySharedMemName` | Objetos de sincronización del implante | Alta | Caza (véase D-4) |
| artefacto | `0x11328712` | Valor mágico al inicio del payload `.dat` del cargador | Alta | Caza (véase D-2) |
| artefacto | `acdbenus` | Cadena de personalización del generador de bits aleatorios | Moderada | Caza en memoria |

*Nota de higiene.* Ninguno de los destinos listados es CDN, proxy residencial ni servicio en
la nube de uso compartido: son **VPS dedicados a la operación**, por lo que el bloqueo no
tiene impacto operativo previsible. Aun así, verificar antes de bloquear los rangos de
Cogent, NTT America y Vultr, donde pueden convivir servicios legítimos en direcciones
vecinas. **Bloquear la IP exacta, nunca el rango.**

### A.2 — Indicadores del ecosistema Sparrow y del clúster `DarkWire` *(añadido en v1.2)*

> ⚠ **Tres advertencias propias de esta sección.**
>
> **Primera, de atribución.** Estos indicadores **no son de FamousSparrow**: son del
> ecosistema que la investigación nueva describe. Encontrar uno establece contacto con el
> ecosistema Sparrow, **no identifica a este actor** (`KJ-11`, enmienda de §O-1). Se
> publican aquí porque el expediente está vinculado por un dominio compartido, no porque
> sean del mismo operador.
>
> **Segunda, de geografía.** La fuente afirma que **la mayoría de las direcciones de
> `DarkWire` están alojadas en Latinoamérica, con frecuencia en el mismo país que la
> víctima**, pero **no publica el país de cada dirección**. Eso significa dos cosas: que
> parte de estas direcciones puede estar en infraestructura de proveedores regionales con
> clientes legítimos, y que **bloquearlas sin verificación puede cortar tráfico propio**.
> Verificar cada una antes de actuar.
>
> **Tercera, de clasificación.** La asignación de cada dirección a un clúster proviene de
> los **encabezados de las tablas de la fuente**, no de un dato por dirección. Dos
> direcciones aparecen en más de un clúster en el original (`91.210.164[.]5` y
> `109.205.195[.]131`), lo que sugiere infraestructura compartida entre clústeres y debilita
> el valor de la etiqueta.

#### A.2.1 — Dominios

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Acción permitida |
|---|---|---|---|---|
| domain | `amelicen[.]com` | **El dominio que vincula los dos expedientes.** Reportado previamente como C2 de `SparrowDoor` —el implante anterior de este actor— y presente en la infraestructura de `CopperDNS` del clúster `DarkWire`. Es la base de `KJ-10` | Alta | Bloqueo + **retrohunt de 24 meses** |
| domain | `seosnskorea[.]com` | Infraestructura del clúster `DarkWire` (Latinoamérica) | Alta | Bloqueo |
| domain | `jamvybez[.]com` | Infraestructura del clúster `DarkWire` | Alta | Bloqueo |
| domain | `artfingo[.]com` | Infraestructura del clúster `DarkWire` | Alta | Bloqueo |
| domain | `faceorkut[.]com` | Infraestructura del clúster `DarkWire`. **El nombre imita dos marcas de redes sociales**; véase `CTI-2026-018` | Alta | Bloqueo |
| domain | `aauctioneer[.]com` | Infraestructura del clúster `DarkWire` | Alta | Bloqueo |
| domain | `microsfot[.]vip` | Infraestructura del clúster `SilentDelivery` (Europa y Asia). **Error tipográfico deliberado de una marca conocida** | Alta | Bloqueo |
| domain | `microscoft[.]vip` | Infraestructura del clúster `SilentDelivery`. Misma técnica de suplantación | Alta | Bloqueo |
| domain | `aistei[.]com` | Infraestructura del clúster `SilentDelivery` | Alta | Bloqueo |
| domain | `astorialaza[.]com` | Infraestructura del clúster `SilentDelivery` | Alta | Bloqueo |
| domain | `windowsupdates[.]us` | Infraestructura del clúster `OceanGate` (Asia). Suplanta el servicio de actualización del sistema | Alta | Bloqueo |
| domain | `microupdate[.]me` | Infraestructura del clúster `OceanGate` | Alta | Bloqueo |
| domain | `windefender[.]net` | Infraestructura del clúster `OceanGate`. Suplanta el producto de seguridad del sistema | Alta | Bloqueo |
| domain | `windowsdefender[.]it[.]com` | Infraestructura del clúster `OceanGate`. *Nota: en la fuente aparece como `windowsdefender.it[.]com`; se normaliza el ofuscado y se consigna la discrepancia* | Media | Bloqueo tras verificación |

#### A.2.2 — Direcciones del clúster `DarkWire` (Latinoamérica)

> ⚠ **Mayoritariamente alojadas en Latinoamérica, con frecuencia en el país de la víctima.
> VERIFICAR CADA UNA antes de bloquear**: el riesgo de cortar tráfico propio es real.

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Acción permitida |
|---|---|---|---|---|
| ipv4 | `38.54.57[.]12` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `38.54.45[.]155` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `38.60.206[.]85` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `38.60.209[.]65` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `38.60.242[.]182` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `38.60.241[.]65` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `38.60.241[.]193` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `38.60.214[.]237` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `149.104.87[.]222` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `149.104.87[.]228` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `149.104.12[.]128` | C2 del clúster `DarkWire`. *Aparece duplicada en la fuente* | Media | Bloqueo tras verificar reasignación |
| ipv4 | `156.244.2[.]26` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `181.41.201[.]244` | C2 del clúster `DarkWire`. **Rango asignado a Latinoamérica: candidato a C2 en el país de la víctima** | Media | Bloqueo tras verificar reasignación |
| ipv4 | `77.111.101[.]153` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `77.111.101[.]227` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `77.111.101[.]11` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `216.238.110[.]120` | C2 del clúster `DarkWire`. **Coincide con el primer servidor de SparroWocky documentado en la emisión original de este informe (§O-5, 2025-12-11): es un segundo punto de solapamiento entre ambos expedientes** | Alta | Bloqueo |
| ipv4 | `216.238.71[.]215` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `216.238.73[.]14` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `216.238.111[.]30` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `216.238.119[.]130` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `216.238.90[.]160` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `216.238.85[.]243` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `216.238.107[.]140` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `216.238.115[.]152` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `216.238.106[.]177` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `216.238.113[.]122` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `216.238.121[.]254` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `216.238.120[.]8` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `64.176.10[.]7` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `64.176.6[.]27` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `45.76.215[.]17` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `185.93.173[.]30` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `188.214.157[.]51` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `108.61.161[.]250` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |
| ipv4 | `167.179.109[.]141` | C2 del clúster `DarkWire` | Media | Bloqueo tras verificar reasignación |

#### A.2.3 — Hashes del clúster `DarkWire` (SHA-256)

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Acción permitida |
|---|---|---|---|---|
| sha256 | `de6a3140797f7c00a48b2068127965c3994f92867466259e69c861880e6ec2d8` | **`CopperDoor`, solo en memoria. Es el implante que ESET analiza como `SparroWocky`** | Alta | Retrohunt (no aparecerá en disco) |
| sha256 | `d08e09a17df22fb39838dcc9e99756830ef5175bc9e03d615adf979dc85ed052` | `CopperDoor`, segunda muestra, solo en memoria | Alta | Retrohunt |
| sha256 | `417664cc34360d8519adc7a019408cf8f37f59c95a44e50092d73e38b7889a21` | **`CopperDNS`, solo en memoria.** Tunela el mando sobre consultas DNS de tipo `MX` | Alta | Retrohunt |
| sha256 | `4cafda69af3179ceb4a1f5ed864c501279796254709c86ca236be1cf74a8643f` | `CopperLoader` — `ncpmif32.dll`, cargada lateralmente por `ncptrcw.exe` | Alta | Bloqueo + retrohunt |
| sha256 | `48dcc07d9f87129e937f5ca2ad5ba56975600efb8a7280a170b2aeeff503f595` | `CopperLoader` — `ncpmif32.dll`, segunda muestra | Alta | Bloqueo + retrohunt |
| sha256 | `a47279e4ee703092263e7030c43c61533146c00689e7cb8f2080f18e57d5cf7f` | `CopperLoader` — `libjpeg-62.dll` | Alta | Bloqueo + retrohunt |
| sha256 | `d4e4a3f55b875673cfdb6d0687cc3f8890585210806b03082d11fb4fa40b57de` | `CopperLoader` — `libvlccore.dll`, cargada lateralmente por `vlc.exe` | Alta | Bloqueo + retrohunt |
| sha256 | `3317789219e9b3e48fbb8f7af23359a37539597fc4d84649086aec71a21553ee` | `CopperLoader` — `libvlc.dll` | Alta | Bloqueo + retrohunt |
| sha256 | `c049e5e03a04cf54f8aa089c65861342d3fb4aa8d6a2b1c9484637c46ddc3882` | `CopperLoader` — `winfsp.dll`, cargada lateralmente por `fsptool.exe` | Alta | Bloqueo + retrohunt |
| sha256 | `f01a73f651f8113bf9672dbe4c50c63ed365a41e4187aaf0a5ab34cd21154046` | `CopperLoader` — `winfsp.dll`, segunda muestra | Alta | Bloqueo + retrohunt |
| sha256 | `9332f9cd283d69e9a2a2bb71575054cc71c14b6496ac55f7ff43efdcb6d97a01` | `CopperLoader` — `winfsp-x64.dll`. **Mismo nombre de fichero que los cargadores de SparroWocky del Anexo A.1**: es un tercer punto de solapamiento | Alta | Bloqueo + retrohunt |
| sha256 | `12b6d5ca7aca7134032721b6feb8e4d5ad75c886fbf8a5889d3d36971a083681` | `CopperLoader` — `libeay32.dll` | Alta | Bloqueo + retrohunt |
| sha256 | `125525a38abc45e855f848d499582a8100f1428938d4bd3d3eba957072e64e7a` | `CopperLoader` — `libeay32.dll`, segunda muestra | Alta | Bloqueo + retrohunt |
| sha256 | `4b1fea3265492ad1d272428447fb5919bbe3184131b12a0ae84caf3bc442718e` | `CopperLoader` — `zCrashReport64.dll`, cargada lateralmente por `zCrashReport64.exe` | Alta | Bloqueo + retrohunt |
| sha256 | `4e50f53b5294a6dbd601fc20a607ae85725162b596119f4867311ef0b3f75a6a` | Cargador de código shell, variante de `CopperLoader` — `DukeQt.dll`, cargada por `gethwid.exe`. **`DukeQt.dll` aparece también en el Anexo A.1 como cargador de SparroWocky** | Alta | Bloqueo + retrohunt |
| sha256 | `f42461c386834d61780da13760a130ed2ea620627b5eebf97b56237058ea380d` | `CopperSplity` — `zCrashReport64.dll`. *El nombre de familia aparece así en la fuente* | Alta | Bloqueo + retrohunt |
| sha256 | `b7060cf7955a1f1caac2bc3d0918c9b1d9daa315c5d82b329acd3bbddb413948` | `CopperSplity` — `tempdir.dll` | Alta | Bloqueo + retrohunt |
| sha256 | `cb714decdcabe30008546e6fb71bb28e390c9bd186bf2549aaa8fe5b999200a5` | Auxiliar de `CopperSplity` — `asinteg.dll` | Alta | Bloqueo + retrohunt |
| sha256 | `fd0861a8269f2bb2fe0adfb4b4610d9675e68474503598f83e87c29b88906f99` | `CopperLsass` — inyector en el proceso de autoridad de seguridad local por RPC, solo en memoria | Alta | Retrohunt |
| sha256 | `916a16a4a1eb7393b17574835312725e5cb146995a3cbcdf42fa8b9bebaa51b1` | `CopperLsass` — volcado de memoria del proceso de autoridad de seguridad local, `slave.dll` | Alta | Bloqueo + retrohunt |
| sha256 | `675a44c679dea8d40b3885c37168929f976e3a0ecacc7e02c6b07936ac58a9fc` | `CopperLsass` — auxiliar, `dep.dll` | Alta | Bloqueo + retrohunt |
| sha256 | `3a1b7ec461d656524e612b228ce969bfa612c799fb7117bb066352ff776d88da` | `CopperProxy`, solo en memoria. Hasta 300 clientes; abre la regla de cortafuegos `ss1` | Alta | Retrohunt |
| sha256 | `ee8c148518c5a416fc7d9b33246e9c98d955f2379aa9c82225e045322c97a043` | `PyProxy` — **distribuido con el nombre `sqlmap.exe`**, que es el de una herramienta legítima de pruebas de intrusión | Alta | Bloqueo + retrohunt |
| sha256 | `4f9d9a6cba88832fcb7cfb845472b63ff15cb9b417f4f02cb8086552c19ceffc` | **SoftEther VPN renombrado a `vmtoolsd.exe`**, el nombre del proceso de las herramientas de VMware. Túnel de red con nombre de componente legítimo | Alta | Bloqueo + retrohunt |

#### A.2.4 — Certificados TLS

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Acción permitida |
|---|---|---|---|---|
| sha256 | `ee4a8b81fe3864582efc27a77f806990e2602dcc36447ddda4b3a230a473d575` | **Huella del certificado TLS de los nodos de `CopperDNS`**, reutilizado en varios. **Sujeto y emisor `CN=8.8.8.8`**, autofirmado, válido del 2025-07-16 al 2026-07-16, número de serie `0x20a61422b0352cfc9ef688dc800bcdf810f1fe7d`. Es el mejor indicador de esta sección | Alta | Bloqueo + retrohunt (`D-10`) |
| sha1 | `de32c58a8087cc4f24b9eb65c8ff4516f0f65f13` | El mismo certificado, huella SHA-1 | Alta | Bloqueo + retrohunt |
| sha1 | `760be920fad07881b8ce9d94e074a35b4f806717` | **Certificado reutilizado entre la infraestructura de `SilentDelivery` y de `OceanGate`.** Sujeto y emisor suplantan a dos empresas de seguridad conocidas, con validez del 2023-04-28 al 2024-04-27: **caducado y reutilizado**, mismo patrón que `CTI-2026-027` | Alta | Bloqueo + retrohunt |

#### A.2.5 — Artefactos de host y de protocolo

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Acción permitida |
|---|---|---|---|---|
| artefacto | `RasiUwpApp` | **Nombre de la regla de cortafuegos que crea `CopperAdu`** para abrir el puerto TCP 445. Comando literal: `netsh advfirewall firewall add rule name="RasiUwpApp" dir=in action=allow protocol=TCP localport=445 profile=any` | Alta | Detección (`D-11`) |
| artefacto | `admin$` | **Cuenta local que crea `CopperAdu`** con `net user admin$ "Admin@123456" /add /expires:never /passwordchg:no`, la añade a administradores y le desactiva la caducidad de contraseña. **Oculta además la cuenta de la pantalla de inicio de sesión** | Alta | Detección (`D-11`) |
| clave | `Admin@123456` | Contraseña codificada de la cuenta anterior | Alta | Detección |
| clave | `LocalAccountTokenFilterPolicy` = `1` | Valor de registro que `CopperAdu` establece para permitir el uso remoto de credenciales de cuenta local | Alta | Detección (`D-11`) |
| artefacto | `ss1` | Nombre de la regla de cortafuegos que crea `CopperProxy` | Alta | Detección |
| artefacto | `kbl` | Nombre de la ventana oculta de `CopperLogger`, que registra la entrada de teclado por la interfaz de entrada en bruto | Alta | Detección |
| artefacto | `WindowsUpdateAssist` | Clave de arranque automático que usa `SquadC` (clúster `SilentDelivery`) para persistir | Alta | Detección |
| path | `C:\Program Files\7-Zip\Lang` · `C:\Windows\debug` · `C:\Windows\System32` · `C:\ProgramData\vmware\logs` · `C:\ProgramData\Oracle\Java` · `C:\ProgramData\USOShared` · `C:\ProgramData\Waves` | **Directorios legítimos y existentes** donde el cargador se aloja para no crear rutas nuevas. **El indicador no es el directorio: es un fichero `.dll`, `.dat` o `.png` nuevo dentro de él** | Alta | Caza (`D-11`) |
| filename | `ncpmif32.dll` ← `ncptrcw.exe` · `winfsp.dll` ← `fsptool.exe` · `libvlccore.dll` ← `vlc.exe` · `DukeQt.dll` ← `gethwid.exe` · `zCrashReport64.dll` ← `zCrashReport64.exe` | **Pares de carga lateral de DLL documentados.** El ejecutable es legítimo y firmado; la biblioteca que carga del mismo directorio, no | Alta | Detección por discordancia de firmante |
| filename | `1.png` | Nombre al que se renombra el volcado cifrado de memoria del proceso de autoridad de seguridad local antes de exfiltrarlo. **Un `.png` que no es una imagen** | Alta | Caza |
| puerto | `6532` | Puerto más frecuente de los nodos de `CopperDNS`, sobre hosts Windows en el sistema autónomo `AS20473` | Alta | Caza |
| puerto | `445` | Puerto que abre la regla de cortafuegos `RasiUwpApp` | Alta | Detección |
| asn | `AS20473` · `AS138915` · `AS396356` · `AS6134` · `AS212238` · `AS136258` | **Sistemas autónomos del mando y control de `CopperDoor`**, puerto 443 con TCP crudo encapsulado en TLS. Son proveedores con clientes legítimos: **no bloquear el sistema autónomo completo** | Media | Caza (`D-8`) — **no bloquear el ASN** |
| pattern | `0x11223344` | **Valor mágico que valida el tráfico** en `SparrowDoor` y `SparrowShell`. Es el indicador de protocolo más duradero del ecosistema | Alta | Detección |
| pattern | `0x0e0e0e0e` | Interfaz de control del rootkit Reptile modificado que usa `SparrowShell` en Linux | Alta | Detección |
| pattern | `consultas DNS de tipo MX con etiquetas largas y codificadas desde un equipo que no es servidor de correo` | **Canal de mando de `CopperDNS`.** Patrón conductual, no indicador: no caduca | Alta | Detección (`D-9`) |
| herramienta | `SoftEther VPN` · `FRPC` · `Chisel` · `sqlmap` | Herramientas legítimas de red y de pruebas de intrusión, **renombradas y reutilizadas** por los clústeres del ecosistema. Detectar por ubicación y por nombre discordante, nunca por presencia | Alta | **No bloquear por presencia** |

## Anexo B — Fuentes y valoración

> Valoración doble tipo Admiralty/OTAN: **fiabilidad de la fuente (A–F)** ×
> **credibilidad de la información (1–6)**. Se valoran por separado.

| Fuente | Disciplina | Fiabilidad | Credibilidad | Notas de sesgo |
|---|---|---|---|---|
| ESET Research — *Beware the SparroWock* (2026-09-17) | TECHINT de proveedor | B | 2 | Investigación primaria con análisis de binario y telemetría propia. **Fuente única de todo el contenido técnico.** Interés comercial en la visibilidad del hallazgo; telemetría sesgada por su base instalada |
| ESET Research — *You will always remember this as the day you finally caught FamousSparrow* (2025-03-27) | TECHINT de proveedor | B | 2 | Base de la campaña 2024 y de la discusión de atribución. Mismo emisor: **no constituye corroboración independiente** de la fuente anterior |
| ESET / GlobeNewswire — nota de prensa (2026-09-17) | Comunicación corporativa | B | 3 | Contiene la valoración geopolítica y las citas del investigador. Formato promocional: el marco interpretativo está más afirmado que en el análisis técnico |
| The Hacker News (2026-09-17) | Prensa técnica | C | 3 | Reproduce el análisis primario. **Discrepa sobre el vector de acceso inicial** («desconocido»), lo que obliga a la salvedad de §T-1 |
| Infosecurity Magazine (2026-09) | Prensa técnica | C | 3 | Reproduce el análisis primario; aporta el detalle de la disputa portuaria panameña |
| Microsoft Threat Intelligence (2024-09, vía prensa) | TECHINT de proveedor | B | 4 | Origen de la fusión de alias con Salt Typhoon y GhostEmperor. **Sin indicadores ni TTP publicados**: la afirmación no es verificable |
| Trend Micro — Earth Estries / CrowDoor | TECHINT de proveedor | B | 3 | Base del solapamiento de código con HemiGate. Distinto esquema de denominación, riesgo de fusión indebida |
| BioBioChile / Infobae / DPL News (2026-08) | OSINT prensa nacional | C | 4 | Caso chileno de telecomunicaciones. Prensa generalista sin detalle técnico verificable; nombres de empresas y de actor citados a partir de un dossier no público |
| CISA/NSA/FBI — aviso conjunto sobre Salt Typhoon (2025-08-27) | Autoridad gubernamental | A | 2 | Alta fiabilidad, pero **sobre otro clúster**. Se cita solo para delimitar qué NO cubre este informe |

**Escalas**
- **A** completamente fiable · **B** normalmente fiable · **C** bastante fiable · **D** normalmente no fiable · **E** no fiable · **F** no evaluable.
- **1** confirmada por otras fuentes · **2** probablemente cierta · **3** posiblemente cierta · **4** dudosa · **5** improbable · **6** no evaluable.

> ⚠ **Advertencia sobre la base de fuentes.** Tres de las nueve fuentes son el mismo emisor y
> cuatro reproducen a ese emisor sin verificarlo. **Este informe tiene una única fuente
> primaria real.** La convergencia aparente entre medios no es corroboración: es difusión.
> Todo juicio de nivel técnico hereda esa fragilidad, y por eso G-2 está marcada como brecha
> crítica en §14.

**Fuente añadida en la revisión v1.2**

| Fuente | Disciplina | Fiabilidad | Credibilidad | Notas de sesgo |
|---|---|---|---|---|
| Check Point Research, «Not All That Glitters Is Gold: Tracking CopperDragon's Sparrow Framework Around the Globe», **2026-11-10**, y la nota de blog asociada del mismo día | OSINT comercial de primera mano | **B** | **3** | **Fuente única de todo el material de la revisión v1.2.** Análisis de binario e infraestructura, con 50 hashes, 14 dominios, cerca de 100 direcciones y dos certificados publicados. Leída íntegra en dos tramos; los indicadores proceden del segundo. **Credibilidad 3 y no 2 por tres razones**, todas ellas declaradas por la propia fuente o verificables: (a) **su tesis central es explícitamente una hipótesis** —«potencial intendente digital», «puede operar como»— y no un hallazgo; (b) **no está corroborada por ningún otro proveedor** en el momento de esta revisión, y en particular ESET no se ha pronunciado sobre la taxonomía de los tres clústeres; (c) **no nombra los países ni las operadoras del clúster latinoamericano**, que es precisamente el dato que convertiría `KJ-9` en exposición verificable. A su favor: distingue con cuidado lo que afirma de lo que evalúa, publica el conjunto de indicadores completo y señala por sí misma el solapamiento con el trabajo de ESET en lugar de reclamar el hallazgo |

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

> Usar siempre el término **y** el porcentaje. No usar «podría» ni «es posible» como juicio:
> son afirmaciones no falsables.

## Anexo D — Marcos de referencia empleados

`MITRE ATT&CK v17` · `MITRE D3FEND` · `Modelo del Diamante` · `Cyber Kill Chain` ·
`Pirámide del Dolor` · `F3EAD` · `ICD 203` · `ACH, KAC, pre-mortem` · `TLP 2.0` · `PAP` ·
`STIX 2.1 / TAXII 2.1` · `Admiralty Code` · `Ley 21.663 y normativa ANCI`

## Anexo E — Paquete legible por máquina

- Bundle STIX 2.1: pendiente de generar a partir del Anexo A
- Evento MISP: pendiente — taxonomías: `tlp`, `admiralty-scale`, `estimative-language`, `PAP`
- Reglas: `D-2` (YARA) y los dos bloques Sigma de §X-4 quedan pendientes de commit en el repositorio de detección
- Herramienta de descifrado del payload publicada por el proveedor (`extract_sparrowocky.py`): pendiente de validación interna antes de su uso sobre muestras propias

## Anexo F — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-09-21 | Emisión inicial | Célula CTI |
| 1.2 | 2026-11-17 | **Revisión por material nuevo: la investigación de Check Point sobre `CopperDragon` (10-11-2026).** Cambios: (a) **enmienda de `KJ-3`** — SparroWocky deja de ser exclusivo de este actor y pasa a ser pieza de un arsenal compartido, de modo que su presencia ya no atribuye; (b) **enmienda de `KJ-6`** — el juicio se mantiene y se refuerza, pero cambia su contexto al existir ya un clúster china-nexus documentado contra telecomunicaciones latinoamericanas; (c) **cuatro juicios nuevos** `KJ-8` a `KJ-11`; (d) adenda al resumen ejecutivo; (e) §3.5 con nueve limitaciones nuevas; (f) fila de telecomunicaciones y adenda en §E-2; (g) **seis designaciones nuevas en §O-1 y enmienda de la nota de tradecraft**, que pasa de advertir contra fundir actores a advertir contra tomar un implante por un actor; (h) cuatro entradas de cronología en §O-5; (i) cinco indicadores de alerta `I-8` a `I-12`; (j) **cinco detecciones nuevas `D-7` a `D-11`** en §X-3, incluidas las del tunelado DNS sobre registros MX y del certificado que suplanta un resolutor público; (k) **Anexo A.2 con 14 dominios, 36 direcciones, 24 hashes, 3 certificados y 22 artefactos**, con tres advertencias propias; (l) fuente añadida en el Anexo B con credibilidad 3 y el motivo; (m) cinco brechas nuevas `G-5` a `G-9`; (n) caducidad ampliada de 2026-12-21 a 2027-02-17. **Los juicios `KJ-1` a `KJ-7` se conservan sin reescribir para que la revisión sea auditable** | Célula CTI |
| 1.1 | 2026-11-16 | **Reclasificación de TLP:AMBER a TLP:CLEAR** por decisión del emisor, para publicación en el repositorio abierto `cti_daily`. Verificado previamente que el documento no contiene referencias a la organización emisora ni a marcas asociadas, telemetría propia, direccionamiento interno, nombres de personas ni datos de terceros. **Sin cambios en los juicios analíticos ni en los indicadores.** Se mantiene PAP:AMBER | Célula CTI |

## Anexo G — Realimentación del consumidor

| Pregunta | Respuesta |
|---|---|
| ¿Respondió a su requisito? | |
| ¿Qué decisión tomó o cambió con este informe? | |
| ¿Qué faltó? | |
| ¿Llegó a tiempo? | |

> Sin este anexo devuelto, el ciclo de inteligencia queda abierto y el próximo producto no
> mejora.
