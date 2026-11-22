---
tlp: "TLP:CLEAR"
pap: "PAP:AMBER"
id: "CTI-2026-014"
version: "1.5"
tipo: "Perfil de actor"
foco_regional: "Chile · Latinoamérica"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "TheGentlemen · Storm-2697"
fecha: "2026-09-15"
caduca: "2026-12-15"
autor: "Célula CTI"
distribucion: "Actualizado el 2026-11-19 con medición propia de victimología (§E-2.3: 1.020 víctimas reclamadas en 2026 y 129 latinoamericanas, 9 de ellas chilenas) y con las dos reivindicaciones de alto perfil del mes (§E-2.2): la de NVIDIA, listada sin prueba y negada por la compañía, y la de DirecTV, que no aparece en ninguna fuente. Reclasificado a TLP:CLEAR el 2026-11-16 por decisión del emisor. Elaborado sin telemetría propia ni datos de cliente: no contiene información identificable de la organización emisora ni de terceros. Difusión libre, conservando la atribución de las fuentes y las salvedades metodológicas del informe. Se mantiene PAP:AMBER: los indicadores del Anexo A llevan acción permitida individual y no deben cargarse en bloqueo automático sin verificación previa contra telemetría propia."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-014
## TheGentlemen: RaaS de alto volumen con cifrador auto-propagante y acceso por borde de red
### Con evaluación de actividad confirmada en Chile y Latinoamérica

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-014` |
| Versión / fecha | `1.5` — 2026-11-21 |
| Tipo de producto | Perfil de actor + informe de campaña |
| Niveles cubiertos | Estratégico · Operacional · Táctico · Técnico |
| Foco regional | Chile · Latinoamérica |
| Marcado de difusión | `TLP:CLEAR` · `PAP:AMBER` |
| Ventana de observación | 2025-07-17 → 2026-09-15 |
| Base de colección | 17 fuentes externas todo-fuente (OSINT, TECHINT de proveedor, CLOSINT derivado de filtración adversaria, CERT nacional). **Sin telemetría propia incorporada** |
| Caducidad / revisión | 2026-12-15, o antes si se confirma rebranding |
| Productos relacionados | — (emisión inicial) |
| Paquete legible por máquina | Pendiente de generar (véase §14) |

<!-- cti:note type="warn" -->

> **Limitación estructural de este producto.** Se ha elaborado exclusivamente con
> fuentes abiertas y de proveedor. No incorpora telemetría de la organización, por
> lo que **la sección de exposición propia (§Operacional-4) está sin rellenar** y
> los juicios sobre riesgo para nosotros son condicionales, no evaluados.

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** TheGentlemen es, a la fecha de este informe, **la segunda operación de
ransomware-como-servicio más activa del mundo por volumen de víctimas
publicadas**, solo por detrás de Qilin, con ~868 víctimas reivindicadas en 12
meses. Valoramos **casi con certeza (95–99 %)** que siga operativa durante los
próximos seis meses en ausencia de acción policial.
**Confianza: alta.** *Base:* concordancia de cinco fuentes independientes (A-2 a C-2) sobre la tendencia, pese a discrepancias en las cifras absolutas.

**KJ-2.** El vector de acceso inicial dominante es **el borde de red: appliances
Fortinet sin parchear (CVE-2024-55591) y portales VPN/SSL sin MFA**. El grupo
mantiene un inventario de aproximadamente **14.700 dispositivos FortiGate ya
comprometidos** que distribuye a sus afiliados. Valoramos **muy probable
(80–95 %)** que una intrusión de este actor contra nosotros comenzara por esa vía.
**Confianza: alta.** *Base:* coincidencia de Unit 42, Sophos, Group-IB y Halcyon.

**KJ-3.** El cifrador **se auto-propaga sin intervención del operador**: con unas
credenciales de dominio válidas, un solo host comprometido intenta 21 operaciones
de ejecución remota contra cada máquina alcanzable. Esto está **confirmado por
análisis de binario**. Valoramos **casi con certeza** *(≥99 %)* el mecanismo
descrito, por estar verificado en el binario. **Confianza: alta.**
*Implicación de doctrina:* la premisa clásica de contención —"aislar el host
paciente cero y luego investigar"— **no es válida contra este actor**. La ventana
de contención efectiva se mide en minutos.

**KJ-4.** La **mediana de permanencia entre acceso inicial y cifrado es de
aproximadamente 2 días**, con casos observados por debajo de 24 horas. Valoramos
**probable (55–80 %)** que un proceso de respuesta que dependa de escalado manual
en horario laboral llegue tarde.
**Confianza: moderada.** *Base:* Sophos (A-2, telemetría de IR propia); una fuente secundaria discrepa al alza (3–5 días).

**KJ-5.** La filtración de su infraestructura interna del **4 de mayo de 2026 no
ha degradado su operación** —el volumen de víctimas siguió creciendo después—.
Valoramos **probable (55–80 %)** un rebranding o pivote de infraestructura en los
próximos 6–12 meses, lo que **invalidará los indicadores técnicos de este informe
pero no sus TTP**.
**Confianza: moderada.** *Base:* precedente de LockBit y ALPHV; razonamiento por analogía, no por observación directa.

**KJ-6.** Las cifras públicas **subestiman el volumen real de víctimas en torno a
un 54 %**: un servidor C2 incautado apuntaba a más de 1.570 víctimas frente a las
**1.020 publicadas en el sitio de filtración a 19-11-2026** —la cifra original de
este juicio eran ~868 y un 45 %, medida en septiembre—. **Y en la versión 1.4 el
dato gana corroboración**: la ficha del propio rastreador que medimos recoge por
su cuenta que **un servidor de mando y control comprometido en 2026 reveló más de
1.570 víctimas vinculadas**, lo que convierte la fuente única original en dos
fuentes concordantes sobre la misma cifra. Valoramos **muy probable**
*(80–95 %)* que las cifras públicas subestimen el volumen real, y **casi con
certeza** *(≥99 %)* los dos recuentos de partida.
**Confianza: elevada de baja a MODERADA en la versión 1.4**, por la concordancia de dos fuentes sobre la cifra de 1.570 y porque el denominador es ahora medición propia. *Base:* la fuente original más la ficha del rastreador. **Sigue sin confirmación independiente del contenido de ese servidor**, y el juicio es sobre un recuento ajeno, no sobre brechas verificadas.

**KJ-7.** **TheGentlemen opera en Latinoamérica con víctimas confirmadas en al
menos doce países, Chile incluido**, donde reivindicó el ataque a un organismo
público en febrero de 2026. El contexto agrava el juicio: **Chile atraviesa el
peor momento de ransomware de su historia registrada** —agosto de 2026 marcó el
máximo histórico mensual de víctimas y los ocho primeros meses de 2026 ya superan
cualquier año completo anterior—. Valoramos **muy probable (80–95 %)** que la
presión sobre organizaciones chilenas se mantenga o aumente en el próximo
trimestre.
**Confianza: alta.** *Base:* monitorización de CronUp (ATRc®) y alerta oficial del CSIRT Nacional/ANCI, corroboradas por ESET y a3sec.

**Qué cambiaría estos juicios:** (a) una detención o incautación de
infraestructura confirmada por autoridades; (b) la aparición de un cifrador con
un esquema criptográfico distinto bajo la misma marca —indicaría cambio de
desarrollador—; (c) observación de acceso inicial por phishing masivo, que
contradiría el modelo actual centrado en borde de red.

**KJ-8.** **Las dos reivindicaciones de alto perfil de noviembre de 2026 no están al mismo nivel, y ninguna de las dos es una brecha confirmada.** El **18 de noviembre de 2026** el grupo añadió a **NVIDIA** a su sitio de filtración con una cuenta atrás de unas 234 horas —vencimiento el 28 de noviembre— **sin publicar ni un fichero de muestra, ni un documento, ni una cifra de rescate**; y la compañía declaró que **no ha encontrado indicio de que sus sistemas o redes se vieran afectados**, añadiendo que investiga **un incidente separado que podría haber afectado a uno de sus proveedores de servicios**. De **DirecTV**, en cambio, **no hay ninguna fuente**: no aparece en el sitio de filtración según la cobertura localizada, ni en los rastreadores, ni en prensa especializada. Valoramos **casi con certeza** *(≥99 %)* que el listado de NVIDIA exista, **poco probable** *(20–45 %)* que corresponda a un compromiso directo de esa compañía, y **muy poco probable** *(5–20 %)* que la reivindicación sobre DirecTV exista como tal. **Confianza: alta para los hechos del listado; moderada para la lectura del alcance.** *Base:* fuentes 23 a 26, más la declaración de la propia compañía. **Y el dato que más pesa en el juicio es del historial del propio actor**: una de las fuentes señala que **el grupo ha exagerado reivindicaciones y ha identificado mal a organizaciones objetivo con anterioridad**. §E-2.2 desarrolla la lectura y qué hacer con ella.

**KJ-9.** **Medición propia del 19-11-2026: es el actor de mayor dispersión geográfica de toda la cartera —90 países— y el segundo de mayor exposición regional, con 129 víctimas latinoamericanas y nueve chilenas.** Sobre **1.020 víctimas reclamadas en 2026**, el reparto latinoamericano es: **Brasil 36**, México 24, Argentina 18, Colombia 11, **Chile 9**, Perú 8, Ecuador 5, Venezuela 4, Puerto Rico 4, Belice 3, Paraguay 2, y una cada uno en Bolivia, Nicaragua, Guatemala, Panamá y República Dominicana — **dieciséis países de la región**. Y **46 de sus registros llevan referencia de prensa**. Valoramos **casi con certeza** *(≥99 %)* las cifras, con la salvedad de que son reclamaciones y no brechas verificadas. **Confianza: alta para el recuento.** *Y la comparación que importa, sobre los mismos datos y el mismo día:* **Qilin tiene 20 víctimas chilenas frente a nuestras 9**, de modo que **en exposición chilena este actor es el segundo y no el primero**; pero **en número de países de la región alcanzados —dieciséis— no tiene rival**. *Consecuencia:* para una organización con operación multinacional en la región, **es el actor con más probabilidad de alcanzar alguna de sus filiales** (§E-2.3).

**KJ-10.** **Su inventario de capacidades publicado tiene 55 técnicas en 13 tácticas, y añade tres elementos que el informe original no recogía y que cambian una hipótesis de caza.** El primero: **una cadena completa de relevo de NTLM** —`PetitPotam`, `ntlmrelayx`, `RelayKing`, `Responder`— que es un camino a administración de dominio **sin explotar ninguna vulnerabilidad de software**. El segundo: **`Velociraptor`, una herramienta legítima de respuesta a incidentes y análisis forense**, usada ofensivamente, lo que significa que **su presencia en un servidor puede parecer trabajo del propio equipo de seguridad**. El tercero: **`Censys` y `Shodan`** como herramientas de reconocimiento, es decir, **servicios de escaneo de Internet usados para elegir objetivo antes de tocarlos**. Valoramos **casi con certeza** *(≥99 %)* el contenido del inventario **como dato
publicado** —y **no lo verificamos**—, y **probable** *(55–80 %)* que las tres
capacidades nuevas estén en uso real. **Confianza: alta para el registro, baja
para el uso.** *Consecuencia:* se añade la hipótesis de caza `H-13` (`T-4`) sobre relevo de NTLM, y una advertencia operativa: **`Velociraptor` en un servidor que no esté en el inventario de respuesta a incidentes es una anomalía, no una tranquilidad.**

---

## 2. Resumen ejecutivo

TheGentlemen es un grupo criminal de habla rusa, con ánimo exclusivamente de
lucro, que en catorce meses ha pasado de no existir a copar aproximadamente el
10 % de todos los ataques de ransomware reivindicados a escala mundial. No innova:
**industrializa**. Su ventaja competitiva son tres decisiones de negocio.

Primera, paga a sus afiliados **el 90 % del rescate**, frente al 70–80 % habitual
del sector, lo que le ha permitido captar operadores experimentados de programas
rivales. Segunda, **entrega el acceso ya hecho**: en lugar de exigir a sus
afiliados que consigan la entrada, les reparte un inventario de miles de
cortafuegos Fortinet previamente comprometidos, eliminando la parte más lenta y
más cara de una intrusión. Tercera, su cifrador **se propaga solo por la red**,
de modo que un afiliado con poca pericia técnica puede provocar un cifrado de
dominio completo.

Para nosotros, esto se traduce en tres consecuencias concretas. **Una:** el
riesgo se concentra en los activos perimetrales —VPN, cortafuegos, portales de
acceso remoto—, que son precisamente los que no tienen agente EDR y peor
telemetría generan. **Dos:** el margen de reacción es de unas 48 horas desde el
acceso hasta el cifrado, y menos de 24 en el peor caso observado; cualquier
proceso de respuesta que dependa de escalado humano en horario de oficina llega
tarde. **Tres:** el grupo ataca deliberadamente la infraestructura de respaldo
(Veeam, VMware ESXi) antes de cifrar, por lo que la copia de seguridad solo es
una defensa si está fuera del dominio y es inmutable.

**Decisión que se solicita a Dirección:** aprobar (a) una revisión extraordinaria
de la exposición perimetral con plazo de 30 días, (b) la validación de la
inmutabilidad y el aislamiento de las copias de seguridad, y (c) la autorización
de contención automatizada fuera de horario —aislar un host sin esperar
aprobación humana—, que es la única contramedida proporcionada a la velocidad de
propagación descrita en §Técnico-3.

---

## 3. Alcance y limitaciones

**Requisitos atendidos.** Perfilado de un actor de alta actividad con relevancia
potencial para nuestra superficie expuesta; caracterización de su modelo de
acceso inicial; extracción de contenido de detección accionable.

**Fuera de alcance.** Evaluación de nuestra exposición real (requiere telemetría
propia); valoración de terceros y proveedores; análisis de la viabilidad de pago.

**Limitaciones de la colección.**
- **Ninguna fuente primaria propia.** Todo procede de terceros.
- **Las cifras de víctimas proceden del sitio de filtración del propio
  adversario**, que es una fuente que él controla: puede inflar (reivindicaciones
  falsas), omitir (víctimas que pagaron) y duplicar. Se usan como indicador de
  tendencia, no como recuento.
- **Parte del material sobre estructura interna procede de datos filtrados por un
  tercero criminal** (§Operacional-5). Un adversario puede haber salado esa
  filtración. Se le asigna credibilidad limitada.
- **Discrepancia no resuelta sobre el liderazgo** del grupo entre dos proveedores
  de primer nivel (§Operacional-2).
- **Sesgo de proveedor:** una de las fuentes es el fabricante cuyo producto
  constituye el vector principal, y otra es un proveedor con incentivo comercial
  a dramatizar la escala. Ambos marcados en el Anexo B.
- **Cobertura regional asimétrica.** Los datos de Chile son de buena calidad
  (CERT nacional + proveedor local con monitorización continua). Los del resto de
  Latinoamérica proceden en su mayoría de un único análisis regional, por lo que
  **la ausencia de víctimas reportadas en un país no es evidencia de ausencia de
  actividad**, sino probablemente de menor cobertura de reporte.

---

# NIVEL ESTRATÉGICO
### Para: Consejo, CISO, Riesgo, Legal · Horizonte: 6–24 meses

## E-1. Qué representa este actor en el panorama

TheGentlemen no es una amenaza *nueva* en términos técnicos; es la evidencia de
**tres cambios estructurales del mercado criminal que ya afectan a cualquier
organización expuesta a Internet**:

**La barrera de entrada ha desaparecido.** El grupo vende no solo el cifrador,
sino el acceso. Un afiliado ya no necesita saber explotar un cortafuegos: recibe
una lista de dispositivos ya comprometidos. Esto desacopla la capacidad ofensiva
de la pericia técnica, y explica por qué el volumen crece más rápido que la
sofisticación.

**La marca ya no informa.** El grupo nació escindido de Qilin —sus operadores
eran el afiliado «ArmCorp»— tras una disputa por 48.000 USD de comisiones
impagadas. Sus miembros rotan, colaboran con LockBit, DragonForce y otros, y
someten a ingeniería inversa los cifradores de Babuk, Qilin, LockBit 5.0 y Medusa
para incorporar lo mejor de cada uno. **Defenderse "de TheGentlemen" es un error
de marco: hay que defenderse de los comportamientos, porque los afiliados y las
técnicas sobreviven a las marcas.**

**La IA ya está integrada en el flujo de trabajo ofensivo.** Las comunicaciones
internas filtradas muestran uso corriente de asistentes comerciales y de modelos
abiertos sin restricciones para desarrollo de código y de scripts. La consecuencia
defensiva no es alarmista sino concreta: **las heurísticas que dependen de
"errores del atacante" —redacción defectuosa, código torpe— pierden valor**.

## E-2. Victimología: dónde cae y qué significa para nosotros

| Dimensión | Distribución observada (a 2026-09-15) |
|---|---|
| **Países** | EE. UU. 156 · Alemania 40 · Tailandia 39 · Francia 38 · Reino Unido 37 · 70+ países en total |
| **Sectores** | Manufactura 171 · Tecnología 114 · Servicios profesionales 108 · Sanidad 76 · Retail 68 |
| **Exclusión** | Rusia y CEI, por prohibición interna de los operadores |

Dos lecturas relevantes para el cálculo de riesgo:

**El grupo es geográficamente indiferente.** A diferencia del patrón habitual del
ransomware —donde en torno al 50 % de las víctimas son estadounidenses—, aquí la
cuota de EE. UU. es marcadamente menor. Esto indica **selección oportunista por
exposición técnica, no por geografía o tamaño**. No existe la protección de «somos
poco interesantes» ni la de «no operamos en el mercado estadounidense»: el
criterio de selección es tener un FortiGate sin parchear accesible desde Internet.

**Ataca sanidad sin restricción.** El grupo no aplica las limitaciones
autoimpuestas que algunos programas de RaaS declararon históricamente. Sanidad es
su cuarto sector.

## E-2.2 Actualización de noviembre de 2026: dos reivindicaciones de alto perfil, y lo que sostiene cada una

Esta sección se añade en la versión 1.3 y es la aplicación directa de dos métodos que esta cartera desarrolló después de la emisión original de este informe: el del `Anexo D` de `CTI-2026-041` —**cómo leer lo que publica un extorsionador cuando es la única fuente**— y el criterio 7 del `Anexo D` de `CTI-2026-042` —**¿hay víctimas verificables por un tercero?**—.

### El listado de NVIDIA

**Los hechos observables.** El **18 de noviembre de 2026**, el grupo añadió a **NVIDIA** a su sitio de filtración, con una **cuenta atrás de unas 234 horas** que vence el **28 de noviembre**. El listado **no incluye ficheros de muestra, ni documentos robados, ni una cifra de rescate**.

**La respuesta de la compañía.** NVIDIA declaró que **no ha encontrado indicación de que sus sistemas o redes se vieran afectados**, que continúa vigilando la situación, y que **investiga un incidente separado que podría haber afectado a uno de sus proveedores de servicios**.

**Y el contexto que la propia cobertura aporta y que es el dato más informativo:** el mismo sitio de filtración lista a **Jentech**, proveedor de NVIDIA, el **6 de octubre**, y a **FPT Software** el **27 de octubre**.

**La lectura, aplicando el marco de `CTI-2026-041`:**

| Afirmación | Quién lo dice | Incentivo | Credibilidad |
|---|---|---|---|
| El listado existe, con cuenta atrás al 28 de noviembre | **Hecho observable** por terceros | — | **Alta** |
| NVIDIA fue comprometida | **El atacante**, sin publicar ni un fichero | **Máximo para exagerar**: es la marca de mayor valor reputacional que podría reclamar | **Baja** |
| Los sistemas y redes de NVIDIA no se vieron afectados | **La compañía** | Minimizar | **Media-alta**, y es una afirmación **negativa y verificable a posteriori**, que es costosa de hacer en falso |
| Un **proveedor de servicios** puede haber sido afectado | **La compañía**, voluntariamente | **Ninguno para admitirlo.** Es una admisión que le resta | **Alta.** Lo que una víctima admite sin necesidad es lo más creíble que dice |
| Dos proveedores de NVIDIA figuran listados semanas antes | **Hecho observable** | — | **Alta** |

**Las dos últimas filas, juntas, dan la hipótesis más económica y es la que este informe sostiene:** **el grupo probablemente tiene material de un proveedor y ha listado la marca del cliente final.** Es un patrón conocido en este mercado —listar el nombre con más valor reputacional de la cadena— y encaja con los tres datos a la vez: la ausencia de muestras, la negativa específica de la compañía sobre *sus* sistemas, y los dos proveedores previamente listados. Valorado en `KJ-8` como *poco probable* que haya compromiso directo.

**Y el factor que inclina el juicio, que es de historial y no de este caso:** una de las fuentes señala que **este grupo ha exagerado reivindicaciones y ha identificado mal a organizaciones objetivo con anterioridad**. Un actor con ese historial que publica una marca de primer nivel **sin una sola muestra** está haciendo lo que ya se le ha visto hacer.

### El listado de DirecTV

**No se localizó ninguna fuente.** La reivindicación sobre **DirecTV** no aparece en la cobertura especializada localizada, ni en los rastreadores de sitios de filtración consultados, ni en prensa. Se buscó expresamente junto al nombre del grupo.

**Y conviene enunciar con precisión qué significa este «no», porque hay tres explicaciones y conducen a decisiones distintas:**

| Explicación | Qué implicaría |
|---|---|
| **El listado no existe** | La afirmación es un error de atribución o una confusión con otro grupo o con otro incidente |
| **El listado existe y es demasiado reciente** para haber sido recogido | Reaparecería en días. **Es el disparador `I-a` de abajo** |
| **El listado existió y se retiró** | Suele indicar **pago**, y en ese caso no habrá fuente pública nunca |

Valoramos **muy poco probable** *(5–20 %)* que la reivindicación exista en la forma afirmada, y **se consigna como no corroborada en lugar de omitirse**, que es la regla de esta cartera: una afirmación que no se sostiene se documenta con lo que se buscó, para que nadie repita el trabajo ni la dé por buena.

### El volumen acumulado, y por qué las cifras no concuerdan

La emisión original de este informe situaba ~868 víctimas acumuladas a septiembre de 2026. Los recuentos de noviembre difieren entre rastreadores, y la discrepancia es informativa:

| Recuento | Cifra | Fecha |
|---|---|---|
| Un rastreador de sitios de filtración | **1.123 víctimas en 95 países** | 2026-11-18 |
| Un informe de proveedor | **1.012 reivindicaciones** entre enero y el 27 de octubre | 2026-10-27 |
| Otro análisis | **1.002 víctimas**, con **135 en los últimos 30 días** | 2026-10-19 |

**Las tres son recuentos de reivindicaciones y no de brechas verificadas**, y conviene no promediarlas: miden cosas ligeramente distintas con criterios de deduplicación distintos. Lo que las tres sostienen a la vez es el orden de magnitud —**más de mil**— y la tendencia: **el grupo sigue siendo uno de los de mayor volumen del mercado**, y Microsoft lo sitúa entre los de mayor número de víctimas reclamadas de los últimos tres meses.

**Y una observación que `KJ-6` ya anticipaba y que esta actualización refuerza en sentido contrario al esperado:** aquel juicio sostenía que las cifras públicas *subestiman* el volumen real. El caso de NVIDIA muestra el error opuesto —**una reivindicación que probablemente sobreestima el alcance de un compromiso concreto**— y las dos cosas son compatibles: **un sitio de filtración puede tener menos víctimas de las que hubo y, a la vez, atribuirse más de lo que consiguió en un caso concreto.** La primera distorsión viene de quien paga y no aparece; la segunda, de quien lista una marca que no comprometió.

### Lo que esta actualización pide hacer

| # | Acción | Quién | Coste |
|---|---|---|---|
| 1 | **No tratar el listado de NVIDIA como una brecha confirmada** en ningún material interno o externo. Es un listado sin prueba, con negativa específica de la compañía | CTI | Cero |
| 2 | **Vigilar el vencimiento del 28 de noviembre.** Si publica datos, el juicio de `KJ-8` se puede cerrar en un sentido o en otro mirando **de quién son los documentos**: si son de un proveedor, confirma la hipótesis de este informe | CTI | Bajo |
| 3 | **Revisar si alguno de los dos proveedores listados —o cualquier otro de la cadena— es también proveedor nuestro.** Es la única acción de esta actualización con efecto defensivo directo, y aplica a cualquier organización, no sólo a las del sector | Riesgo de terceros | Bajo |
| 4 | **Devolver la corrección sobre DirecTV** a quien aportó la afirmación, con lo que se buscó | CTI | Cero |

**Disparadores de reevaluación añadidos en esta versión.** `I-a`: aparición de un listado de **DirecTV** en el sitio de filtración del grupo o en un rastreador, que refutaría la parte negativa de `KJ-8`. `I-b`: publicación de datos tras el vencimiento del 28 de noviembre, **con identificación de a quién pertenecen**. `I-c`: confirmación por NVIDIA o por el proveedor afectado del alcance real del incidente de cadena de suministro. `I-d`: retirada del listado sin publicación, que sugeriría pago y cerraría la vía pública.

## E-2.3 Medición propia del 19 de noviembre de 2026

> **Esta sección se añade en la versión 1.4.** Las cifras de §E-2 son de
> proveedor y de septiembre de 2026. Las que siguen son **medición propia**
> sobre un rastreador público, tomadas el 19-11-2026, y permiten comparar a
> este actor con el resto de la cartera **sobre el mismo conjunto de datos y la
> misma metodología**.

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `1.020` | Víctimas reclamadas en 2026 | Frente a ~868 medidas en septiembre. **Segunda del top 10 tras Qilin (1.221)** |
| `129` | **Víctimas latinoamericanas** | **El 12,6 %: la proporción regional más alta del top 10** |
| `16` | **Países de la región alcanzados** | **Sin rival en la cartera.** Qilin alcanza 13 |
| `9` | Víctimas chilenas | **Segundo tras Qilin, que tiene 20** |
| `90` | Países alcanzados en total | **La mayor dispersión geográfica de toda la cartera** |
| `46` | Registros con referencia de prensa | Indicio de confirmación por terceros |
| `55` | Técnicas documentadas, en 13 tácticas | Segundo inventario del top 10 tras Qilin (71) |
| `41 %` | Entradas con fecha de ataque igual a la de publicación | **Declara fecha anterior y distinta en el 59 %** |
| `19 / 41` | Víctimas de 7 días por fecha de ataque / por publicación | **×2,2** (`CTI-2026-046` §O-3.1) |
| `50` | Pico de publicaciones en un día (31-10-2026) | **Publica en tandas**, como INC Ransom |

### El reparto regional: dieciséis países

| País | 2026 | | País | 2026 |
|---|---|---|---|---|
| **Brasil** | **36** | | Puerto Rico | 4 |
| **México** | **24** | | Belice | 3 |
| **Argentina** | **18** | | Paraguay | 2 |
| Colombia | 11 | | Bolivia · Nicaragua · Guatemala · Panamá · R. Dominicana | 1 cada uno |
| **Chile** | **9** | | | |
| Perú | 8 | | **Total** | **129** |
| Ecuador | 5 | | | |
| Venezuela | 4 | | | |

### Lo que la comparación con Qilin establece, y corrige una impresión

| Dimensión | **TheGentlemen** | **Qilin** | Quién gana |
|---|---|---|---|
| Víctimas 2026 | 1.020 | **1.221** | Qilin |
| **Proporción latinoamericana** | **12,6 %** | 10,0 % | **TheGentlemen** |
| Víctimas latinoamericanas | 129 | 122 | TheGentlemen, por poco |
| **Víctimas chilenas** | 9 | **20** | **Qilin, con diferencia** |
| **Países de la región alcanzados** | **16** | 13 | **TheGentlemen** |
| Países en total | **90** | 81 | **TheGentlemen** |
| Técnicas documentadas | 55 | **71** | Qilin |
| Ritmo de publicación | **En tandas** (50 en un día) | **Sostenido** (máx. 19) | — |

> **La corrección de impresión que esta tabla obliga a hacer, y conviene
> decirla: en exposición CHILENA este actor es el segundo, no el primero.**
> Veinte víctimas chilenas de Qilin frente a nueve de éste. La versión 1.1 de
> este informe incorporó el eje chileno y lo trató como el dato regional
> central; **con datos comparables, el dato regional central de este actor no
> es Chile: es la amplitud.** Dieciséis países de la región y noventa en total
> —las dos cifras más altas de la cartera— describen una operación que **no
> elige geografía**, y por eso alcanza a dieciséis países donde Qilin alcanza
> trece.
>
> **La consecuencia práctica es para una organización multinacional: contra
> Qilin, la pregunta es si se opera en Chile o México; contra este actor, la
> pregunta es si se opera en algún sitio.**

### Lo que el inventario añade al expediente

Tres elementos del inventario publicado no estaban en las versiones anteriores:

| Elemento | Qué es | Qué obliga |
|---|---|---|
| **`PetitPotam` · `ntlmrelayx` · `RelayKing` · `Responder`** | **Una cadena completa de relevo de NTLM**: camino a administración de dominio **sin explotar ninguna vulnerabilidad de software** | **Nueva hipótesis de caza `H-13`** (`T-4`). Y las medidas son de configuración: firma de LDAP, protección extendida de la autenticación, y deshabilitar NTLM donde se pueda |
| **`Velociraptor`** | **Herramienta legítima de respuesta a incidentes y análisis forense**, usada ofensivamente | **Su presencia en un servidor puede parecer trabajo del propio equipo de seguridad.** La medida es un **inventario de en qué equipos está autorizada**, y alerta fuera de él |
| **`Censys` · `Shodan`** | **Servicios de escaneo de Internet**, usados para reconocimiento | **El reconocimiento ocurre sin tocar nuestra red y no deja rastro en nuestros registros.** La única contramedida es **reducir la superficie que esos servicios indexan**, que es una medida de higiene de perímetro |

> **La fila de `Velociraptor` es la que más conviene retener, porque invierte
> una intuición.** La presencia de una herramienta forense en un servidor
> comprometido se suele leer como señal de que **alguien está investigando**.
> Aquí puede ser señal de que **alguien está dentro**, y la única forma de
> distinguirlo es un inventario de dónde la ha desplegado el propio equipo.

## E-2.1 Foco regional: Chile y Latinoamérica

### El actor en la región

TheGentlemen no trata a Latinoamérica como periferia. Su expansión regional
—Colombia primero, después Argentina y Chile— es coherente con su criterio global
de selección: **exposición técnica, no relevancia económica**.

| País | Víctima / sector | Fecha |
|---|---|---|
| **Chile** | Organismo público de derechos humanos (Instituto Nacional de Derechos Humanos) | Feb 2026 |
| Argentina | Instituto público de investigación científica | Feb 2026 |
| Colombia | Dos organizaciones: sanidad y medios de comunicación | Mar 2026 |
| Brasil · Perú · Ecuador · Venezuela · Guatemala · Rep. Dominicana · Costa Rica · Panamá · México | Presencia confirmada, detalle no publicado | 2026 |

> **Lectura clave.** Las tres primeras víctimas latinoamericanas conocidas son
> **organismos públicos e instituciones de investigación**, no grandes
> corporaciones. Esto es consistente con KJ-2 y refuerza el juicio: el grupo entra
> por donde el perímetro está sin parchear, y el sector público regional concentra
> appliances de borde con ciclos de actualización largos.

### El contexto chileno: por qué este informe es urgente aquí

Chile ha dejado de ser un objetivo oportunista para integrarse en campañas
sostenidas alineadas con la dinámica global. Los datos de monitorización continua
del mercado local dibujan un deterioro sin precedentes:

| Indicador | Valor |
|---|---|
| **Agosto 2026** | **Máximo histórico mensual**: al menos 10 organizaciones afectadas |
| Enero–agosto 2026 | Ya supera el total de **cualquier año completo anterior** |
| Promedio mensual 2026 | ~4 víctimas/mes — **cuadruplica** el promedio de 2023 |
| Dic 2025 – mar 2026 | 13 organizaciones atacadas en 4 meses · 15 publicaciones · 9 grupos distintos |
| Grupos activos simultáneamente en Chile | Qilin · Inc Ransom · **The Gentlemen** · Akira · Direwolf · Aurora · LockBit5 · Leakeddata · DragonForce · Pear |
| Sectores más golpeados | Salud · Educación · Servicios profesionales · Manufactura · Sector público |

Casos públicos del periodo que ilustran el patrón: una clínica privada (Devman,
dic 2025, ~250 GB exfiltrados), el sector energético (Anubis, ene 2026), varias
empresas de logística, comercio y agroindustria (Qilin, Lynx/Minteye), hotelería,
y en septiembre de 2026 un hospital clínico universitario (Direwolf).

**Los vectores de acceso observados en Chile coinciden con el perfil de este
informe y añaden uno propio de la región:**

1. **Credenciales comprometidas y VPN sin MFA** — incluido al menos un caso
   documentado donde usuario y contraseña eran idénticos.
2. **Superficies expuestas sin parchear** — el patrón de KJ-2.
3. **Cloud y SaaS mal configurados, señaladamente Microsoft 365** — vector con
   **más peso en Chile que en la media global** reflejada en §Táctico.
4. **Credenciales procedentes de infostealers**, según la alerta del CERT nacional.
5. **Re-victimización**: organizaciones atacadas más de una vez.

> **Implicación para nuestro plan de detección.** El peso del compromiso de
> identidad en M365 en el escenario chileno significa que **las hipótesis de caza
> de §Táctico deben complementarse con vigilancia del plano de identidad en la
> nube** —autenticaciones anómalas, reglas de reenvío de correo, consentimientos
> OAuth—, que el análisis global centrado en el cifrador no cubre.

### Obligación regulatoria (Chile)

Chile cuenta desde 2024 con Ley Marco de Ciberseguridad y con la **Agencia
Nacional de Ciberseguridad (ANCI)**, que opera el CSIRT Nacional. Las entidades
sujetas a la ley tienen **deber de reportar incidentes de efecto significativo en
plazos muy breves —del orden de horas para la alerta temprana—**.

> ⚠ **Verificar con Legal** el plazo exacto vigente y si nuestra organización está
> dentro del ámbito de aplicación. Este informe no sustituye ese análisis. El
> punto relevante para Dirección es que **el reloj regulatorio empieza a correr
> antes de que el análisis técnico haya concluido**, lo que exige tener decidido
> de antemano quién declara un incidente como significativo.
>
> Canal del CSIRT Nacional / ANCI: `+56 2 1510` · `soc@anci.gob.cl`

**El CSIRT Nacional emitió alerta específica sobre este actor** (`AIA26-00012`,
10 de febrero de 2026, TLP:CLEAR), lo que constituye reconocimiento oficial de la
amenaza en el país y refuerza la exigibilidad de las medidas de §Técnico-8.

## E-3. Tendencia y pronóstico

<!-- cti:chart title="Víctimas publicadas por mes" cap="Fuente: sitio de filtración del adversario. Indicador de tendencia, no recuento." -->

| Periodo | Víctimas publicadas/mes |
|---|---|
| Últimos meses de 2025 | < 20 |
| Enero 2026 | 48 |
| Febrero 2026 | 91 |
| Junio 2026 | 117 |
| Julio 2026 | 169 |

Alcanzó en cinco meses el volumen que a Akira le costó doce y a Qilin dieciocho.

**Escenario más probable** *(probable, 55–70 %; confianza moderada)* — Continuidad
con crecimiento moderado. El grupo mantiene el modelo de 90 %, sigue explotando
appliances de borde y añade CVE nuevos a medida que se publican. El volumen se
estabiliza en la horquilla de 100–170 víctimas mensuales.

**Alternativa creíble** *(poco probable, 20–35 %)* — **Rebranding**. La filtración
de mayo de 2026 expuso su cadena de herramientas completa a investigadores y
fuerzas de seguridad. El precedente del sector indica que esto suele preceder a un
cambio de marca con continuidad de personal. *Consecuencia defensiva:* los
indicadores caducan, los TTP no.

**Baja probabilidad / alto impacto** *(remoto, 5–10 %)* — Acción policial
coordinada con detenciones. Reduciría el volumen de forma transitoria; el
precedente de LockBit sugiere reconstitución parcial en meses.

## E-4. Decisiones que este informe pide al nivel estratégico

| # | Decisión | Fundamento | Plazo |
|---|---|---|---|
| E-a | Revisión extraordinaria de superficie perimetral expuesta, con inventario nominal de appliances y su versión | KJ-2: el 100 % del acceso inicial documentado pasa por ahí | 30 días |
| E-b | Validar que las copias de seguridad son inmutables y están **fuera del dominio de Windows** | El actor destruye respaldos antes de cifrar, con credenciales de dominio | 30 días |
| E-c | Autorizar contención automatizada 24×7 sin aprobación humana previa | KJ-3 + KJ-4: la propagación es automática y la mediana de permanencia es de 2 días | 60 días |
| E-d | Extender la exigencia de MFA en acceso remoto a **proveedores y terceros** por vía contractual | La ausencia de MFA en VPN es el habilitador documentado | Trimestre siguiente |
| E-e | Asumir en el plan de continuidad un escenario de **cifrado simultáneo de dominio completo, incluida la capa de virtualización** | El cifrador tiene variantes para ESXi, Linux, NAS y BSD | Próximo ejercicio |
| E-f | **Confirmar con Legal el ámbito de aplicación de la Ley Marco y el plazo de reporte a la ANCI**, y designar nominalmente quién declara un incidente «de efecto significativo» | El plazo de alerta temprana corre en horas, antes de que exista análisis técnico concluyente | 30 días |
| E-g | Extender el alcance de la revisión de identidad a **Microsoft 365** (MFA resistente a phishing, revisión de consentimientos OAuth, reglas de reenvío) | Vector con peso específico mayor en el escenario chileno que en el global | 60 días |
| E-h | Suscribir la organización a las alertas del **CSIRT Nacional / ANCI** y a monitorización regional continua | La alerta `AIA26-00012` sobre este actor se publicó 7 meses antes que buena parte del análisis internacional | 15 días |

---

# NIVEL OPERACIONAL
### Para: Jefatura de SOC, Respuesta a Incidentes, Threat Hunting · Horizonte: semanas–meses

## O-1. Identificación y alias

| Designación | Origen | Grado de equivalencia |
|---|---|---|
| The Gentlemen / TheGentlemen | Autodenominación (sitio de filtración) | Referencia |
| **Storm-2697** | Microsoft | Equivalente |
| ArmCorp | Identidad previa como afiliado de Qilin | Antecesor, no equivalente |
| «Spikey Scorpius» | Unit 42 | **Ambiguo** — la redacción de la fuente no permite determinar si designa a TheGentlemen, a ArmCorp o a Qilin. **No usar hasta aclaración** |

> **Nota de tradecraft.** El cuarto alias se deja marcado como ambiguo en lugar de
> resolverlo por conveniencia. Fusionar alias mal atribuidos es una de las
> principales fuentes de error en correlación de inteligencia.

## O-2. Estructura y atribución

| Eje de atribución | Valoración | Confianza |
|---|---|---|
| Clúster técnico | Actividad coherente: mismo cifrador, misma nota, mismo esquema criptográfico | **Alta** |
| Grupo organizado | ~20 miembros, 8 en el núcleo, con roles diferenciados | **Moderada** |
| Nexo estatal | **Ninguno.** Motivación exclusivamente económica | **Alta** |
| Identidad nominal | Alias de foro conocidos; sin identificación real pública | **Baja** |
| Origen geográfico | Habla rusa; prohibición de atacar CEI | **Moderada** (inferencia por comportamiento, no por evidencia directa) |

**Roles identificados en la filtración interna:** `zeta88` como administrador
—percibe el 10 % de cada rescate—; `Wick` y `mAst3r` como operadores de intrusión;
`Kunder` como validador de accesos; `qbit`, `quant`, `Protagor` y `JeLLy` en
funciones de soporte y herramientas; `hastalamuerte` como corredor de accesos
iniciales colaborador.

> **⚠ Discrepancia de fuentes no resuelta.** Group-IB presenta a `hastalamuerte`
> como **administrador principal** del grupo, mientras que el análisis de la
> filtración interna lo sitúa como **colaborador externo de acceso inicial**, con
> `zeta88` en la administración. Ambas fuentes son de calidad. Posibles
> explicaciones: (a) cambio de rol entre el periodo analizado por cada una;
> (b) `hastalamuerte` es el rostro público y `zeta88` el operador real;
> (c) error de una de las dos. **No se resuelve en este informe.** Impacto
> práctico: ninguno sobre la defensa, relevante solo para correlación con futuros
> informes y para eventual acción legal.

## O-3. Modelo de negocio: por qué escala

**Reparto 90/10.** Anunciado en el foro RAMP en septiembre de 2025 y corroborado
por la filtración interna, donde el administrador percibe el 10 %. Es el reparto
más agresivo del mercado y explica la captación de operadores veteranos.
*(Group-IB indica 70/30; valoramos que corresponde a una condición anterior o a un
nivel distinto de afiliado — discrepancia menor, sin efecto defensivo.)*

**Acceso entregado, no exigido.** Es la diferencia de fondo con un RaaS clásico.
El operador reparte entre sus afiliados:
- Un inventario de **~14.700 dispositivos FortiGate comprometidos**, distribuido como documento HTML.
- **969 credenciales de VPN validadas** por fuerza bruta.
- Scripts, herramientas de evasión de EDR y guía técnica.

**Criterios de selección de víctima** documentados internamente: capacidad de pago
alta; presión legal o regulatoria que incentive pagar; parque relevante de cuentas
VPN de Fortinet; servicios críticos; autenticación débil o integración LDAP
expuesta.

**Reconocimiento previo de honeypots.** Su diccionario de fuerza bruta incluye
combinaciones deliberadamente absurdas para detectar si el dispositivo es un
señuelo antes de invertir esfuerzo. *Consecuencia:* un honeypot perimetral mal
construido será descartado por el atacante y no generará inteligencia.

## O-4. Nuestra exposición

> **⬛ SECCIÓN SIN EVALUAR — requiere telemetría interna.**
>
> Esta es la sección que convierte un informe genérico en inteligencia útil, y es
> la que este producto **no puede rellenar** con las fuentes disponibles. Debe
> completarse antes de dar el informe por cerrado. Preguntas a responder:
>
> | # | Pregunta | Fuente | Responsable |
> |---|---|---|---|
> | X-1 | ¿Exponemos appliances Fortinet a Internet? ¿Qué versión de FortiOS? ¿Parcheadas frente a CVE-2024-55591? | Inventario + escaneo externo | TI/Redes |
> | X-2 | ¿Hay algún portal de acceso remoto **sin MFA**, incluidos los de proveedores? | Gestión de identidad | IAM |
> | X-3 | ¿Existen cuentas administrativas en los appliances con nombres anómalos (`support_fortinet`, `badmin`, `forti-api`, cuentas «guest»)? | Config de los dispositivos | TI/Redes |
> | X-4 | ¿Nuestro Veeam/backup usa credenciales de dominio? ¿Es inmutable? ¿Está fuera del dominio? | Backup | Infraestructura |
> | X-5 | ¿Tenemos SMB1 habilitado en algún segmento? ¿Y `EveryoneIncludesAnonymous`? | GPO / auditoría | Sistemas |
> | X-6 | ¿Registramos y alertamos la creación de servicios y tareas programadas remotas? | SIEM/EDR | SOC |
> | X-7 | ¿Qué cobertura de EDR tenemos en hosts ESXi y NAS? | Inventario | Infraestructura |

## O-5. Acontecimiento de mayo de 2026: la filtración interna

| Fecha | Hecho |
|---|---|
| 2026-05-04 | El administrador reconoce públicamente en Exploit.in el compromiso de su base de datos interna |
| 2026-05-05 | La cuenta `n7778` pone a la venta «The Gentlemen – Hacked Data for Sale» en el foro Cracked por 10.000 USD en BTC |
| — | Contenido: registros de chat, listado de afiliados, transcripciones de negociación, discusiones de herramientas y credenciales de servidor. Ventana 2025-11-07 → 2026-04-30 |
| — | Los investigadores obtuvieron ~44,4 MB de un conjunto total estimado en ~16,22 GB |

**Valoración.** La filtración expuso la cadena de herramientas completa del grupo.
No obstante, **julio de 2026 fue su mes de mayor actividad (169 víctimas)**, es
decir, posterior a la filtración. Valoramos por tanto que **el impacto operativo
fue nulo o marginal (confianza moderada)** y que su principal efecto será
acelerar un eventual rebranding (KJ-5).

*Nota de fuente:* estos datos proceden de una filtración publicada por un actor
criminal. No puede descartarse contaminación deliberada. Se tratan con credibilidad 3.

## O-6. Cronología del actor

<!-- cti:timeline -->

| Fecha | Acontecimiento |
|---|---|
| ~2025 (1S) | Opera como «ArmCorp», afiliado de Qilin |
| 2025-07-17 | Primera muestra Windows del cifrador subida a VirusTotal — desarrollo propio ya en marcha estando aún en Qilin |
| 2025-07-22 | Arbitraje en el foro RAMP contra Qilin por 48.000 USD de comisiones |
| 2025-07 (mediados) | Sitio de filtración operativo, aún sin anuncio público |
| 2025-09 (inicio) | Anuncio público del sitio de filtración — 94 víctimas |
| 2025-09-10 | Publicación de la variante específica para ESXi |
| 2025-09-21 | Se añade temporizador en segundo plano y propagación agresiva por WMI |
| 2025-12 | Disputa pública con el afiliado `Devman` sobre prácticas de OpSec |
| 2026-01 → 2026-05 | 328 víctimas; ~10 % de las reivindicaciones mundiales |
| 2026-05-04/05 | Filtración de su base de datos interna |
| 2026-05 | Acuerdo con BreachForums para captación de pentesters y corredores de acceso |
| 2026-06 | 117 víctimas en el mes |
| 2026-07 | **Pico: 169 víctimas**; total acumulado ~683 |
| 2026-09-15 | ~868 víctimas acumuladas; actividad sostenida |
| 2026-10-06 | Listado de **Jentech**, proveedor de NVIDIA |
| 2026-10-19 | ~1.002 víctimas según un análisis, con **135 en los 30 días previos** |
| 2026-10-27 | Listado de **FPT Software**. Y 1.012 reivindicaciones acumuladas en el año según otro recuento |
| 2026-11-18 | **Listado de NVIDIA**, con cuenta atrás de ~234 h al 28 de noviembre, **sin ficheros de muestra, sin documentos y sin cifra de rescate**. ~1.123 víctimas en 95 países según un rastreador. **La compañía declara no haber encontrado indicio de afectación de sus sistemas, e investiga un incidente separado en un proveedor de servicios** (§E-2.2) |

## O-6.1 Actividad confirmada en Chile y Latinoamérica

### Cronología regional

<!-- cti:timeline -->

| Fecha | Hecho |
|---|---|
| 2026-02-04 | Detección del ataque a un **organismo público chileno de derechos humanos** (INDH). Primer caso confirmado del actor en Chile |
| 2026-02 | Argentina: instituto público de investigación científica |
| **2026-02-10** | **El CSIRT Nacional / ANCI de Chile publica la alerta `AIA26-00012` sobre The Gentlemen** (TLP:CLEAR) |
| 2026-02 | El actor es el **segundo grupo más activo del mundo** en el mes, con 78 víctimas |
| 2026-02-26 | CronUp publica el análisis del deterioro del escenario chileno: 13 organizaciones en 4 meses, 9 grupos |
| 2026-03 | Colombia: dos organizaciones —sanidad y medios de comunicación— |
| 2026-03-26 | ESET documenta la expansión latinoamericana del actor |
| 2026-04-07 | a3sec emite boletín regional: expansión Colombia → Argentina → Chile |
| 2026-08 | **Chile registra su máximo histórico mensual de víctimas de ransomware** (≥10 organizaciones) |
| 2026-09-04 | CronUp confirma la continuidad del pico; The Gentlemen sigue entre los grupos activos en el país |

### Lo que aporta el CERT nacional que no aporta el análisis internacional

La alerta `AIA26-00012` describe un perfil de intrusión **parcialmente distinto**
al de los informes globales, y la diferencia es operativamente relevante:

| Aspecto | Informes internacionales | **CSIRT Nacional de Chile** |
|---|---|---|
| Acceso inicial | Explotación de CVE en appliance (T1190) | **Cuentas válidas (T1078) con credenciales procedentes de infostealers** |
| Movimiento lateral | PsExec, SMB, WMI | **RDP (T1021.001)** hacia servidores internos |
| Señal temprana | Artefactos del cifrador | **Autenticaciones VPN exitosas desde geografías inusuales fuera de Chile** y ráfagas de autenticación fallida contra cuentas privilegiadas |

> **Valoración analítica.** Esto **no contradice** los informes internacionales:
> refleja que los afiliados que operan en la región **no siempre necesitan
> explotar un CVE**, porque disponen de credenciales válidas compradas a corredores
> de acceso o extraídas de registros de infostealers. Es una vía más barata y más
> silenciosa que la explotación.
>
> **Consecuencia práctica:** parchear CVE-2024-55591 **no cierra el vector
> chileno**. Si no hay MFA, un parche perfecto no impide la entrada. Esto eleva la
> prioridad de las decisiones E-d, E-g y de la hipótesis de caza H-10.

### Indicadores y recomendaciones del CSIRT Nacional (AIA26-00012)

**Indicadores citados oficialmente:**
- Tarea programada `gentlemen_system`
- Volúmenes anómalos de tráfico RDP
- Múltiples intentos fallidos de autenticación contra cuentas privilegiadas

**Medidas recomendadas** —coincidentes con §Técnico-8, con dos añadidos propios:
MFA en VPN, acceso administrativo y sistemas críticos · **restricciones
geográficas en el SSL VPN de Fortinet** · EDR con protección contra manipulación ·
mínimo privilegio · respaldos inmutables y fuera de línea (3-2-1) · **pruebas
mensuales de restauración** · segmentación de Directorio Activo, hipervisores y
respaldos · restricción de SMB, RDP y SSH entre segmentos internos.

> La **restricción geográfica del SSL VPN** es la medida de mayor relación
> eficacia/coste para una organización chilena frente a este actor concreto, dado
> el indicador de autenticaciones desde fuera del país.

### Diferencias con el perfil global, y qué significan

| Hallazgo regional | Divergencia respecto al perfil global | Implicación |
|---|---|---|
| Peso de **Microsoft 365** como superficie comprometida en Chile | Los informes globales sobre este actor apenas lo mencionan | Añadir vigilancia de identidad en la nube (no cubierta por §Táctico) |
| Acceso vía **infostealers** | Los informes globales priorizan CVE de borde | Vigilar credenciales corporativas en volcados de infostealers |
| **Re-victimización** observada en Chile | No documentada globalmente para este actor | Una organización ya atacada sigue siendo objetivo: el acceso puede persistir |
| Sector público como primera víctima regional | Globalmente domina manufactura | El sector público chileno concentra riesgo por ciclos de parcheo largos |

> **Nota de tradecraft.** Estas divergencias pueden deberse a (a) diferencias
> reales de comportamiento de los afiliados que operan en la región, o (b) a un
> sesgo de observación: el CERT nacional ve incidentes reportados por
> organizaciones chilenas, mientras que los proveedores globales ven su propia
> base de clientes. **No se resuelve con las fuentes disponibles**; se consigna
> porque afecta a cómo se ponderan las recomendaciones.

## O-7. Hipótesis alternativas consideradas

**H1 — Es un RaaS genuino con afiliados independientes.** *(Hipótesis retenida.)*
Consistente con el programa público, el reparto 90/10, el reclutamiento en foros
y la variabilidad de TTP entre incidentes.

**H2 — Es un equipo central compacto que simula un programa de afiliados.**
No descartable. Una fuente observa que la «precisión operativa» es más propia de
un equipo coordinado que de afiliados heterogéneos, y la filtración muestra solo
ocho miembros nucleares. *Inconsistencia:* el volumen de 169 víctimas mensuales
es difícil de sostener con ocho personas. **Se valora poco probable (20–35 %).**

**H3 — Existe un patrocinio o tolerancia estatal.** *(Descartada.)* No hay
evidencia. La exclusión de la CEI es característica común de la criminalidad
rusófona y **no constituye por sí sola indicio de patrocinio**. Se consigna
explícitamente para evitar que se reabra sin evidencia nueva.

**Supuesto clave que sostiene buena parte del informe:** que las víctimas
publicadas en el sitio de filtración son reales y no reivindicaciones infladas. Si
fuera falso, la magnitud del actor estaría sobrestimada —aunque no su capacidad
técnica, que está corroborada por análisis de binario independiente.

**Pre-mortem.** Si dentro de seis meses este informe resulta equivocado, la causa
más probable será haber tratado un ecosistema de afiliados rotatorios como si
fuera una organización estable, y haber orientado la defensa a la marca en lugar
de al comportamiento.

## O-8. Indicadores y señales de alerta

| # | Indicador observable | Qué señalaría | Disciplina | Responsable |
|---|---|---|---|---|
| I-1 | Aparición de nuestra organización o de un proveedor nuestro en su sitio de filtración | Compromiso ya consumado en la cadena | OSINT | Célula CTI |
| I-2 | Publicación de un CVE crítico en appliance de borde que nosotros exponemos | Ventana de explotación de días | OSINT / KEV | Vulnerabilidades |
| I-3 | Nueva marca de RaaS con cifrador Go + Curve25519/XChaCha20 y nota análoga | Rebranding consumado (KJ-5) | TECHINT | CTI |
| I-4 | Venta de accesos a nuestra geografía/sector en RAMP, Rehub o Exploit.in | Preparación de acceso inicial | CLOSINT | CTI |
| I-5 | Autenticación correcta en VPN desde ASN inhabitual fuera de horario | Uso de credencial comprometida | Telemetría propia | SOC |
| I-6 | Cuenta administrativa nueva en un appliance perimetral | Puerta trasera post-explotación | Telemetría propia | TI/Redes |
| I-7 | **Autenticación VPN exitosa desde geografía inusual fuera de Chile** | Uso de credencial comprometida — indicador oficial del CSIRT Nacional | Telemetría propia | SOC |
| I-8 | **Aparición de credenciales corporativas en volcados de infostealers** | Vector de acceso regional documentado | OSINT / CLOSINT | CTI |
| I-9 | **Nueva alerta del CSIRT Nacional / ANCI sobre este actor o sobre un CVE de borde** | Reconocimiento oficial de campaña activa en el país | CERT nacional | CTI |
| I-10 | Publicación de una organización chilena de nuestro sector en cualquier sitio de filtración | Campaña sectorial en curso | OSINT | CTI |

---

# NIVEL TÁCTICO
### Para: Analistas de SOC, Ingeniería de Detección, Threat Hunting · Horizonte: días–semanas

## T-1. Cadena de intrusión

Del borde de red al cifrado de dominio completo, en una mediana de dos días.

<!-- cti:stages title="Tres etapas, un solo movimiento continuo" dwell="next" -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 01 · Borde | Entrada por el perímetro | `CVE-2024-55591` en FortiGate; VPN sin MFA; Cuenta backdoor: `support_fortinet`, `badmin`, `forti-api`; Persistencia RMM: AnyDesk, Cloudflared, MeshCentral, Datto |
| Etapa 02 · Dominio | Reconocimiento y credenciales | Advanced IP Scanner, SoftPerfect, Nmap; Credenciales: NetExec, DonPAPI, DPAPI, relay NTLM, Chrome; Movimiento lateral: RDP, PsExec, SMB |
| Etapa 03 · Impacto | Neutralizar, exfiltrar, cifrar | Matar EDR por BYOVD: `ThrottleBlood.sys`, `viragt64.sys`; Destruir respaldos: Veeam, VSS, ESXi; Exfiltrar: `avastrclone.exe`, Restic, MinIO, WinSCP; **Cifrar y auto-propagar**: NETLOGON, GPO, 21 métodos |

**Permanencia:** mediana ≈ **2 días** · mínimo observado **< 24 h** — una vez arranca el cifrador, la ventana de contención efectiva se mide en **minutos**.

## T-2. Mapa MITRE ATT&CK

<!-- cti:matrix -->

| Táctica | ID | Técnica | Procedimiento observado en este actor |
|---|---|---|---|
| Acceso inicial | T1190 | Exploit Public-Facing App | CVE-2024-55591 (FortiOS/FortiProxy), CVE-2025-32433 (Erlang/OTP SSH), CVE-2025-55182 |
| Acceso inicial | T1133 | External Remote Services | SSL VPN sin MFA, RDP expuesto |
| Acceso inicial | T1078.002 | Valid Accounts: Domain | Cuenta administrativa de FortiGate comprometida |
| Acceso inicial | T1110.001 | Password Guessing | Diccionario Fortinet + detección de honeypots |
| Ejecución | T1059.001 | PowerShell | Comandos codificados en Base64 para evasión y despliegue |
| Ejecución | T1059.003 | Windows Command Shell | `cmd.exe` para servicios y procesos |
| Ejecución | T1047 | WMI | `WMIC` y `Win32_Process` para ejecución remota |
| Ejecución | T1053.005 | Scheduled Task | Tareas con patrón `gentlemen*`, `UpdateUser`, `UpdateSystem` |
| Persistencia | T1219 | Remote Access Software | AnyDesk, MeshCentral, Datto RMM, Cloudflared como servicio |
| Persistencia | T1547.001 | Registry Run Keys | `GupdateS` (HKLM), `GupdateU` (HKCU) |
| Persistencia | T1136.002 | Create Account: Domain | Cuentas tipo `MicrosoftSupporte` con acceso a SQL/Veeam |
| Persistencia | T1098 | Account Manipulation | Reseteo de contraseña root en ESXi |
| Escalada de privilegios | T1068 | Exploitation for Privilege Escalation | CVE-2025-7771 en `ThrottleStop.sys`: controlador firmado y vulnerable cargado para escalar (BYOVD). **La versión anterior lo mapeaba a `T1548.008`, que no existe en ATT&CK** |
| Escalada | T1484.001 | Domain Policy Modification | GPO vía `gpme.msc` para distribución dominio-completo |
| Escalada | T1068 | Exploitation for Priv Esc | BadSuccessor, CVE-2025-32463, CVE-2024-37085 (ESXi) |
| Degradación de defensas | T1685 | Disable or Modify Tools | `Set-MpPreference -DisableRealtimeMonitoring`; exclusión de `C:\` |
| Degradación de defensas | T1686 | Disable or Modify System Firewall | `Set-NetFirewallProfile -Enabled False` |
| Degradación de defensas | T1685.001 | Disable or Modify Windows Event Log | `wevtutil`; registro AutoLogger/GlobalLogger de WMI |
| Evasión | T1014 | Rootkit / BYOVD | `ThrottleBlood.sys`, `viragt64.sys`, `nogbc.sys`, `G11.sys` |
| Evasión | T1036.005 | Masquerading | `avastrclone.exe`, `svchost32.exe`, EDR killers con nombre de AV |
| Evasión | T1112 | Modify Registry | `RestrictSendingNTLMTraffic=0`, `DisableRestrictedAdmin=0`, `EveryoneIncludesAnonymous=1` |
| Degradación de defensas | T1685.005 | Clear Windows Event Logs | Security, System, Application (EID 1102 / 104) |
| Acceso credenciales | T1003.004 | DPAPI Backup Key | Impacket `dpapi.py`, DonPAPI |
| Acceso credenciales | T1555 | Credentials from Password Stores | `ChromeKB3.exe`, bases de datos de Veeam (CVE-2023-27532) |
| Acceso credenciales | T1557.001 | LLMNR/NBT-NS Poisoning y SMB Relay | Módulo `coerce_plus` de NetExec; PetitPotam, PrinterBug |
| Descubrimiento | T1018 | Remote System Discovery | Advanced IP Scanner, SoftPerfect (crackeado), Nmap 7.97 |
| Descubrimiento | T1087.002 | Domain Account Discovery | `1.bat` enumerando 60+ cuentas |
| Descubrimiento | T1615 | Group Policy Discovery | `gpresult`, `repadmin` |
| Mov. lateral | T1021.001 | RDP | Habilitado por registro; manipulación de grupo RDP |
| Mov. lateral | T1021.002 | SMB / Admin Shares | PsExec; `C$`; `NETLOGON` |
| Mov. lateral | T1021.006 | WinRM / PS Remoting | `Invoke-Command` |
| Mov. lateral | T1570 | Lateral Tool Transfer | Copia a `C:\Temp` + recurso oculto `share$` |
| Mov. lateral | T1550.002 | Pass the Token | `--spread ""` reutiliza el token de sesión actual |
| C2 | T1071.001 | Web Protocols | WebDAV; SystemBC en puertos no estándar |
| C2 | T1572 | Protocol Tunneling | Chisel (SOCKS) |
| Recolección | T1074.001 | Local Data Staging | `C:\ProgramData\data\`, `C:\PerfLogs`, `C:\Temp` |
| Exfiltración | T1048 | Exfil over Alternative Protocol | Rclone (SFTP), Restic, MinIO `mc`, WinSCP, FileZilla, MEGAsync |
| Impacto | T1489 | Service Stop | 80+ servicios: Veeam, SQL, backup, EDR, virtualización |
| Impacto | T1490 | Inhibit System Recovery | `vssadmin delete shadows`, `wmic shadowcopy delete` |
| Impacto | T1486 | Data Encrypted for Impact | Cifrador Go; Windows, Linux, ESXi, NAS, BSD |
| Impacto | T1561 | Disk Wipe | Argumento `--wipe` |
| Impacto | T1491.001 | Internal Defacement | Fondo de escritorio `%TEMP%\gentlemen.bmp` |

## T-3. Dónde atacamos en la Pirámide del Dolor

<!-- cti:pyramid -->

| Nivel | Contenido de este informe | Valor |
|---|---|---|
| Hashes | Anexo A | **Trivial de eludir.** Cada build cambia. Solo retrohunt |
| IP / dominios | Anexo A | **Bajo.** Rotación rápida, VPS bulletproof |
| Artefactos de red/host | Nombres de tareas, claves Run, `share$`, extensiones | **Medio.** Duraderos entre builds |
| Herramientas | Rclone, NetExec, AnyDesk, PsExec, BYOVD | **Alto**, pero son legítimas: detectar por contexto, no por presencia |
| **TTP** | **§T-4** | **Máximo.** Aquí debe concentrarse el esfuerzo |

> Las detecciones propuestas en §T-4 se sitúan deliberadamente en los dos niveles
> superiores. Las del Anexo A son complementarias y caducan.

## T-4. Hipótesis de caza prioritarias

<!-- cti:accordion critical="^(H-1|H-2|H-3|H-4|H-8)$" regional="^H-1[0-2]$" -->

**H-1 — Preparación de evasión (la señal más fiable).**
Buscar exclusiones amplias de Defender, especialmente `-ExclusionPath C:\`, y
`Set-MpPreference -DisableRealtimeMonitoring`. *Ningún administrador legítimo
excluye la unidad completa.* Precisión muy alta; casi sin falsos positivos.

**H-2 — Carga de driver vulnerable (BYOVD).**
Carga de driver firmado no presente en la línea base, seguida en minutos de
terminación de procesos de EDR. Buscar `ThrottleBlood.sys`, `viragt64.sys`,
`nogbc.sys`, `G11.sys`; y genéricamente, cualquier driver nuevo escrito en
`C:\Windows\Temp`, `C:\PerfLogs` o `C:\ProgramData`.

**H-3 — Recurso SMB oculto creado en un endpoint.**
Creación del recurso `share$` apuntando a `C:\Temp`, junto con modificación del
registro para acceso anónimo. **Es firma del mecanismo de auto-propagación.**
Un endpoint de usuario no comparte carpetas.

**H-4 — Ráfaga de ejecución remota multi-método.**
El cifrador intenta 21 operaciones por host objetivo. Buscar el **patrón temporal**:
un mismo origen creando servicios (`DefSvc`, `UpdateSvc`, `UpdateSvc2`), tareas
programadas y procesos WMI contra múltiples destinos en una ventana de minutos.
Alta fidelidad: es un comportamiento que ninguna herramienta de administración
legítima reproduce.

**H-5 — Habilitación de SMB1 y relajación de LSA.**
`Enable-WindowsOptionalFeature -FeatureName SMB1Protocol` o
`EveryoneIncludesAnonymous=1`. En 2026 esto es **siempre** anómalo.

**H-6 — Servicios de descubrimiento de red activados en masa.**
Arranque de `fdrespub`, `fdPHost`, `SSDPSRV`, `upnphost` en varios hosts a la vez,
con habilitación de reglas de cortafuegos de Detección de redes.

**H-7 — Exfiltración enmascarada.**
Proceso con nombre de producto de seguridad (`avastrclone.exe`, `acronis.exe`,
`sophos.exe`) que establece conexiones salientes de gran volumen. Contrastar
nombre de archivo contra firma digital y ruta esperada.

**H-8 — Preparación anti-recuperación.**
`vssadmin delete shadows /all /quiet` o `wmic shadowcopy delete`, y comandos
`sc config` contra `VeeamBackupSvc`, `SQLWriter`, `BackupExecAgent`. **Si esto se
detecta, el cifrado es inminente: la respuesta debe ser automática.**

**H-9 — Retrohunt en el perímetro.**
Buscar cuentas administrativas creadas en appliances Fortinet con nombres
`support_fortinet`, `badmin`, `forti-api`, o cuentas `guest` con acceso SSLVPN no
registrado. Cubrir **hacia atrás** hasta la fecha de parcheo de CVE-2024-55591.

**H-10 — Acceso por credencial válida (vía regional prioritaria).**
Derivada de la alerta `AIA26-00012` del CSIRT Nacional. Es la hipótesis de mayor
prioridad para una organización chilena, porque **el parcheo no la cubre**:
- Autenticación VPN **exitosa** desde ASN o país fuera del perfil operativo —con
  atención específica a conexiones desde fuera de Chile.
- «Viaje imposible»: dos autenticaciones geográficamente incompatibles.
- Ráfagas de autenticación fallida contra cuentas privilegiadas seguidas de un
  éxito.
- Cuentas de servicio o genéricas autenticando de forma interactiva en VPN.
- Cruce con volcados de *infostealers*: credenciales corporativas expuestas.

**H-11 — Compromiso de identidad en Microsoft 365.**
No documentada en el análisis global de este actor, pero con peso específico en el
escenario chileno:
- Reglas de reenvío o de ocultación de correo creadas por el usuario.
- Consentimientos OAuth a aplicaciones de terceros no aprobadas.
- Descarga masiva desde SharePoint/OneDrive fuera de patrón.
- Registro de un nuevo método de MFA inmediatamente tras un inicio de sesión
  desde geografía anómala.

**H-12 — Retrohunt de re-victimización.**
Si la organización ha sufrido un incidente previo, buscar persistencia residual:
cuentas creadas en el periodo del incidente anterior, herramientas de RMM no
inventariadas, claves SSH y tokens no rotados. La re-victimización está
documentada en el escenario chileno.

### H-13 · Relevo de NTLM *(añadida en la versión 1.4)*

| Campo | Contenido |
|---|---|
| **Hipótesis** | Un adversario ha forzado autenticación de una cuenta de equipo y la ha relevado contra un servicio que no exige firma, obteniendo privilegios sin explotar ninguna vulnerabilidad de software |
| **Por qué** | `KJ-10`: el inventario publicado incluye **`PetitPotam`, `ntlmrelayx`, `RelayKing` y `Responder`**, que son la cadena completa |
| **Cómo se comprueba** | Autenticaciones NTLM entrantes hacia servicios de directorio o de certificados **desde equipos que no son servidores**; conexiones a `MS-EFSRPC` no esperadas; solicitudes de certificado a nombre de cuentas de equipo |
| **Qué significa un positivo** | **Camino abierto a administración de dominio.** Incidente de prioridad máxima |
| **Medidas, y son de configuración y no de producto** | Firma de LDAP y de SMB obligatoria · **protección extendida de la autenticación** en los servicios de certificados y de directorio · deshabilitar NTLM donde la compatibilidad lo permita · auditoría de solicitudes de certificado por cuenta de equipo |

> **Es la hipótesis de caza más rentable que esta actualización añade, y por una
> razón concreta: la cadena de relevo de NTLM no depende de que falte un
> parche.** Funciona contra sistemas completamente actualizados cuya
> configuración no exija firma, de modo que **un programa de parcheo impecable
> no la cierra**. Las cuatro medidas de la fila anterior sí.

## T-5. Brechas de visibilidad que hay que cerrar primero

| Brecha | Por qué importa aquí |
|---|---|
| Sin EDR en appliances de borde | Es el punto de entrada y no genera telemetría |
| Sin registro de creación de servicios remotos (EID 7045) centralizado | Es uno de los 8 métodos de propagación |
| Sin auditoría de creación de recursos compartidos | H-3 es indetectable sin ella |
| Sin cobertura en ESXi / NAS | Existen variantes específicas del cifrador |
| Registro de PowerShell (ScriptBlock, EID 4104) desactivado | La evasión y la propagación pasan por ahí |
| Logs del appliance no centralizados | El actor borra los locales |
| **Sin geolocalización ni alerta sobre autenticaciones VPN exitosas** | Es el indicador oficial del CSIRT Nacional y la vía de acceso regional (H-10) |
| **Sin monitorización de identidad en Microsoft 365** | Superficie con peso propio en el escenario chileno (H-11) |
| **Sin vigilancia de credenciales corporativas en volcados de infostealers** | Alimenta el acceso por cuenta válida antes de cualquier explotación |

---

# NIVEL TÉCNICO
### Para: Ingeniería de detección, automatización, TIP/SIEM · Vida útil: días–semanas

## X-1. El cifrador

| Propiedad | Valor |
|---|---|
| Lenguaje / ofuscación | Go, ofuscado con **Garble** |
| Criptografía | **Curve25519 efímera por archivo + XChaCha20**. ECDH con clave pública del operador embebida; nonce derivado de los primeros 24 bytes de la pública efímera; se añade la pública efímera en Base64 al pie del archivo |
| Archivos > 1 MB | Tres fragmentos; el último byte del nonce se XOR-ea con el índice de fragmento (0,1,2) para evitar reutilización de flujo |
| Recuperación sin clave | **Inviable.** Clave efímera por archivo; no hay fallo criptográfico conocido |
| Extensión | **Variable por build**, 6 caracteres — observadas `.umc16h`, `.7mtzhh`. Coincide con el nombre del binario: `locker_<ext>_windows_amd64.exe` |
| Nota de rescate | `README-GENTLEMEN.txt` |
| Plataformas | Windows, Linux, ESXi, NAS, BSD |
| Autenticación | Contraseña de 8 bytes embebida en el build (p. ej. `9VoAvR7G`); sin ella responde `bad args` y termina |

**Argumentos de línea de comandos** — su presencia en una línea de proceso es, por
sí sola, indicador de alta fidelidad:

| Argumento | Efecto |
|---|---|
| `--password <pwd>` | Obligatorio |
| `--path <rutas>` | Objetivos separados por comas |
| `--T <minutos>` | Retardo antes de cifrar (evasión de sandbox y de turno de SOC) |
| `--silent` | No cambia fondo de escritorio |
| `--system` | Cifra unidades locales como SYSTEM |
| `--shares` | Recursos mapeados y UNC |
| `--full` | Dos fases: sistema + recursos |
| `--spread <dom/user:pass>` | **Auto-propagación.** Con `""` reutiliza el token actual |
| `--fast` / `--superfast` / `--ultrafast` | 9 % / 3 % / 1 % / 0,3 % por fragmento |
| `--keep` | No se autoelimina |
| `--wipe` | Sobrescribe espacio libre en bloques de 64 MB vía `wipefile.tmp` |

## X-2. Artefactos de host persistentes entre builds

> **Esto es lo que hay que detectar.** A diferencia de los hashes, estos artefactos
> sobreviven a la recompilación.

```
TAREAS PROGRAMADAS   UpdateSystem · UpdateUser · gentlemen_system · gentlemen*
SERVICIOS            DefSvc · UpdateSvc · UpdateSvc2
CLAVES RUN           HKLM\...\Run\GupdateS     HKCU\...\Run\GupdateU
RECURSO SMB          share$  →  C:\Temp        (+ acceso anónimo por registro)
VARIABLE ENTORNO     LOCKER_BACKGROUND=1
FONDO ESCRITORIO     %TEMP%\gentlemen.bmp
AUTOBORRADO          <ruta_binario>.bat  (retardo mediante ping ICMP)
ESPACIO LIBRE        wipefile.tmp
STAGING              C:\Temp · C:\PerfLogs · C:\ProgramData\data\
```

**Registro modificado:**
```
HKLM\SYSTEM\CurrentControlSet\Control\Lsa\MSV1_0  RestrictSendingNTLMTraffic = 0
HKLM\SYSTEM\CurrentControlSet\Control\Lsa         DisableRestrictedAdmin     = 0
HKLM\SYSTEM\CurrentControlSet\Control\Lsa         EveryoneIncludesAnonymous  = 1
HKLM\SYSTEM\...\Terminal Server\WinStations\RDP-Tcp  SecurityLayer = 1
HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run   GupdateU
```

## X-3. Cadena de auto-propagación (detalle)

1. **Preparación local** — copia el binario a `C:\Temp`, crea el recurso oculto
   `share$` y habilita acceso anónimo por registro.
2. **PsExec** — usa una copia embebida o la descarga de Sysinternals Live.
3. **Descubrimiento** — enumera estaciones, servidores y controladores de dominio;
   arranca `fdrespub`, `fdPHost`, `SSDPSRV`, `upnphost`; habilita las reglas de
   cortafuegos de Detección de redes.
4. **Evasión remota previa** — ejecuta en cada objetivo:
   ```powershell
   Set-MpPreference -DisableRealtimeMonitoring $true;
   Add-MpPreference -ExclusionPath 'C:\';
   Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False;
   Enable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol -NoRestart;
   reg add 'HKLM\SYSTEM\CurrentControlSet\Control\Lsa' /v EveryoneIncludesAnonymous /t REG_DWORD /d 1 /f
   ```
5. **Ejecución — 8 familias de método, 21 operaciones por host:**
   copia remota por `C$` · PsExec · `WMIC process call create` (3 variantes) ·
   tareas programadas en contexto de usuario (3) · tareas en contexto SYSTEM (3) ·
   servicios `DefSvc`/`UpdateSvc`/`UpdateSvc2` · PowerShell remoting por WinRM ·
   WMI `Win32_Process`.
   Cada método intenta cargar desde `\\<origen>\share$\<payload>` y desde
   `C:\Temp\<payload>`. **Basta un éxito para que el ciclo se repita desde el nuevo host.**

## X-4. Anti-forense

```cmd
vssadmin delete shadows /all /quiet
wmic shadowcopy delete
wevtutil cl System  &  wevtutil cl Application  &  wevtutil cl Security
del /f /q %SystemRoot%\Prefetch\*.pf
del  %AppData%\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
:: + logs de RDP, logs de diagnóstico de Defender, papelera de reciclaje
```
Termina **más de 50 procesos** y deshabilita **más de 80 servicios** (`taskkill /IM`,
`sc stop`): virtualización, bases de datos, respaldo, EDR, SAP, Office, correo,
servidores web, navegadores, acceso remoto.

## X-5. Lógica de detección prioritaria (pseudocódigo para portar a Sigma/KQL/SPL)

```
D-1  CRÍTICO  Exclusión total de Defender
     process.name == "powershell.exe"
     AND cmdline CONTAINS_ANY ("ExclusionPath C:\", "ExclusionPath 'C:\'",
                               "DisableRealtimeMonitoring $true")
     → Aislar host. Falsos positivos ≈ 0.

D-2  CRÍTICO  Recurso oculto de propagación
     (net share OR Win32_Share create) AND share_name == "share$"
     AND path CONTAINS "\Temp"
     → Aislar host y bloquear SMB saliente del host.

D-3  CRÍTICO  Servicios de la cadena de propagación
     EID 7045 AND service_name IN ("DefSvc","UpdateSvc","UpdateSvc2")
     → Aislar host de origen.

D-4  CRÍTICO  Argumentos del cifrador
     cmdline MATCHES "--password\s+\S{8}" AND cmdline CONTAINS_ANY ("--spread","--superfast","--ultrafast","--wipe")
     → Matar proceso y aislar.

D-5  ALTO     Persistencia por clave Run
     registry_path ENDSWITH "\CurrentVersion\Run" AND value_name IN ("GupdateS","GupdateU")

D-6  ALTO     Tareas de la cadena
     EID 4698 AND task_name IN ("UpdateSystem","UpdateUser") OR task_name STARTSWITH "gentlemen"

D-7  ALTO     Reactivación de SMB1 / relajación de LSA
     cmdline CONTAINS_ANY ("SMB1Protocol", "EveryoneIncludesAnonymous",
                           "RestrictSendingNTLMTraffic", "DisableRestrictedAdmin")

D-8  ALTO     Anti-recuperación  → respuesta AUTOMÁTICA, no escalado manual
     cmdline CONTAINS_ANY ("vssadmin delete shadows", "wmic shadowcopy delete",
                           "wbadmin delete", "bcdedit /set recoveryenabled no")
     OR (sc config AND target IN ("VeeamBackupSvc","SQLWriter","BackupExecAgent"))

D-9  ALTO     Borrado de rastro
     EID 1102 (Security cleared) OR EID 104 (System/App cleared)
     OR cmdline CONTAINS "wevtutil cl"
     OR file_delete PATH CONTAINS "\Prefetch\"

D-10 ALTO     BYOVD
     driver_load AND (driver_name IN ("ThrottleBlood.sys","viragt64.sys","nogbc.sys","G11.sys")
                      OR driver_path CONTAINS_ANY ("\Temp\","\PerfLogs\","\ProgramData\"))

D-11 MEDIO    Enmascaramiento con nombre de producto de seguridad
     process.name IN ("avastrclone.exe","acronis.exe","sophos.exe","g111.exe","svchost32.exe")
     OR (process.name MATCHES "(avast|acronis|sophos|defender|eset)" AND signer NOT IN allowlist)

D-12 MEDIO    Ráfaga de ejecución remota multi-método
     COUNT(DISTINCT dest_host) > 5
     WHERE (EID 7045 OR EID 4698 OR wmic_process_create) AND source_host == X
     WITHIN 10 minutes
```

```
D-13 ALTO     Autenticación VPN desde geografía inusual  [origen: CSIRT Nacional AIA26-00012]
     vpn_auth.result == "success"
     AND geo_country NOT IN (paises_operativos)
     → Verificación fuera de banda con el titular de la cuenta. No basta con alertar.

D-14 MEDIO    Fuerza bruta contra cuenta privilegiada seguida de éxito
     COUNT(auth.result=="failure" AND account IN privileged) > 10 WITHIN 15 minutes
     FOLLOWED BY auth.result=="success" SAME account WITHIN 60 minutes
```

> **Regla de operación derivada de KJ-3/KJ-4.** D-1 a D-4 y D-8 deben ejecutar
> **aislamiento automático** del host, sin escalado humano previo. Con una mediana
> de permanencia de 2 días y propagación automática, un flujo que dependa de
> validación manual fuera de horario llega tarde.

## X-6. Consultas de caza

**Microsoft Defender XDR (KQL)** — exclusiones amplias:
```kql
DeviceProcessEvents
| where FileName in~ ("powershell.exe","pwsh.exe")
| where ProcessCommandLine has_any ("ExclusionPath C:\\","DisableRealtimeMonitoring",
                                    "EnableControlledFolderAccess Disabled")
| project Timestamp, DeviceName, AccountName, ProcessCommandLine, InitiatingProcessFileName
```

**Recurso de propagación:**
```kql
DeviceProcessEvents
| where ProcessCommandLine has "share$"
   or (ProcessCommandLine has "net share" and ProcessCommandLine has @"C:\Temp")
| project Timestamp, DeviceName, ProcessCommandLine
```

**Ráfaga multi-método (correlación):**
```kql
DeviceEvents
| where ActionType in ("ServiceInstalled","ScheduledTaskCreated")
| summarize Destinos=dcount(DeviceName), Metodos=make_set(ActionType)
    by InitiatingProcessRemoteSessionDeviceName, bin(Timestamp, 10m)
| where Destinos > 5
```

## X-7. Nombres de detección de proveedor

| Proveedor | Firma |
|---|---|
| Microsoft | `Ransom:Win64/Gentlemen` · `Ransom:Win64/Gentlemen.SH!MTB` · `Trojan:Win32/MpTamperBulkExcl.H` |
| Trend | `Ransom.Win64.GENTLEMAN.THHAIBE` · `Trojan.Win64.KILLAV.THHBHBE` · `HackTool.Win32.PowerRun.THHBHBE` |

## X-8. Mitigaciones de configuración con efecto directo

| Control | Corta |
|---|---|
| MFA obligatorio en **todo** acceso remoto, terceros incluidos | Acceso inicial por credencial |
| Parcheo de CVE-2024-55591 + **auditoría de cuentas creadas** en el appliance | Vector primario y su puerta trasera |
| Protección contra manipulación (Tamper Protection) de Defender | D-1 |
| Lista de bloqueo de drivers vulnerables (HVCI / WDAC / Microsoft vulnerable driver blocklist) | BYOVD |
| SMB1 deshabilitado y **bloqueado por política** | Paso 4 de la propagación |
| Firma SMB obligatoria y `RestrictSendingNTLMTraffic` forzado por GPO | Relay NTLM, PetitPotam, PrinterBug |
| Bloquear creación de procesos por PsExec y WMI (regla ASR) | 4 de los 8 métodos de propagación |
| Restringir `C$` / admin shares entre estaciones | Copia remota |
| Cuentas de respaldo **fuera del dominio**, repositorio inmutable | Destrucción de respaldos |
| EDR en modo bloqueo + interrupción automática de ataque | Ventana de 2 días |
| Segmentación que impida SMB estación↔estación | Auto-propagación |
| **Restricción geográfica en el SSL VPN** (recomendación explícita del CSIRT Nacional) | Acceso por credencial comprometida desde fuera del país |
| **MFA resistente a phishing en Microsoft 365** + revisión de consentimientos OAuth | Vector de identidad con peso regional |
| Rotación de credenciales cruzada con volcados de infostealers | Acceso por cuenta válida (T1078) |

---

## 14. Brechas de inteligencia y requisitos de colección

| # | Brecha | Impacto | Requisito propuesto | Prioridad |
|---|---|---|---|---|
| G-1 | **Exposición propia sin evaluar** (§O-4) | El informe no puede cuantificar nuestro riesgo | Responder X-1 a X-7 con inventario y telemetría | **Crítica** |
| G-2 | IOC de red muy escasos y de vida corta | Detección técnica limitada | Suscripción a fuente con C2 de este actor; unirse a canal ISAC sectorial | Alta |
| G-3 | Conflicto de fuentes sobre liderazgo | Afecta a correlación futura | Solicitar aclaración a proveedores; seguimiento de RAMP/Exploit.in | Baja |
| G-4 | Sin muestra propia del cifrador | No podemos validar detecciones contra binario real | Solicitar muestra a ISAC o proveedor; alternativamente pruebas atómicas | Alta |
| G-5 | Cifras de víctimas no verificables (fuente controlada por el adversario) | Magnitud posiblemente sesgada | Contraste con datos de aseguradoras/reguladores | Media |
| G-6 | CVE atribuidos por agregación de proveedor sin evidencia publicada | Riesgo de parchear por ruido | Verificar cada CVE contra informe con evidencia antes de priorizar | Media |
| G-7 | Sin datos sobre variantes Linux/ESXi/NAS con el detalle de la de Windows | Cobertura de detección incompleta en virtualización | Solicitar análisis específico | Alta |
| G-8 | **Sin IOC técnicos asociados al caso chileno** (la alerta nacional es conductual, sin hashes ni IP) | No podemos hacer retrohunt específico del incidente regional | Solicitar al CSIRT Nacional / ANCI los IOC bajo el marcado que corresponda; explorar canal sectorial | **Alta** |
| G-9 | **Cobertura desigual del resto de LATAM**: ausencia de datos ≠ ausencia de actividad | Subestimación del riesgo en la cadena de suministro regional | Monitorizar CERT de los países donde operamos o tenemos proveedores | Media |
| G-10 | **Desconocemos si nuestras credenciales corporativas figuran en volcados de infostealers** | Es el vector de acceso documentado en Chile, y es previo a cualquier explotación | Contratar o activar vigilancia de credenciales filtradas | **Crítica** |
| G-11 | Ámbito de aplicación de la Ley Marco y plazo exacto de reporte a la ANCI sin confirmar | Riesgo de incumplimiento en las primeras horas de un incidente | Consulta a Legal (decisión E-f) | **Alta** |

---

# ANEXOS

## Anexo A — Indicadores de compromiso

> ⚠ **Leer antes de usar.** Los indicadores siguientes son el componente de **menor
> valor y más perecedero** de este informe. El cifrador se recompila por víctima:
> los hashes son válidos para retrohunt, **no** para bloqueo preventivo. La defensa
> real está en §T-4 y §X-5.

### A.1 Hashes — cifrador y componentes

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Uso |
|---|---|---|---|---|
| SHA-256 | `22b38dad7da097ea03aa28d0614164cd25fafeb1383dbc15047e34c8050f6f67` | Cifrador Gentlemen | Alta | Retrohunt |
| SHA-256 | `f918535f974591ef031bd0f30a8171e3da27a6754e6426a8ba095f83195661c8` | `G_hlm7jj_windows_amd64.exe` | Alta | Retrohunt |
| herramienta | `078163d5c16f64caa5a14784323fd51451b8c831c73396b967b4e35e6879937b` | **PsExec embebido.** Tipo `herramienta` y no `SHA-256` **deliberadamente**: con tipo de hash entraría en `ioc_hash.txt`, que es una lista de bloqueo, y PsExec es utillaje legítimo de administración. La medida es el inventario, no el bloqueo | Alta | **No bloquear** — herramienta legítima |
| SHA-256 | `fe1033335a045c696c900d435119d210361966e2fb5cd1ba3382608cfa2c8e68` | Bitmap del fondo de escritorio | Alta | Retrohunt |
| SHA-1 | `c12c4d58541cc4f75ae19b65295a52c559570054` | Cifrador (muestra Trend) | Alta | Retrohunt |

### A.2 Hashes — evasión de EDR y drivers vulnerables

<!-- cti:ioc search="no" -->

| Tipo | Valor | Contexto | Uso |
|---|---|---|---|
| SHA-256 | `a348f5fa048a09188bd706fd3d4efca978990caf3355ecfee501c9f1e19c0efd` | `acronis.exe` (EDR killer) | Bloqueo |
| SHA-256 | `3c71537b64487bbf4d1793f72c75d332650d09a77b71e4d884ff15c266a847f6` | `y7D0.exe` (EDR killer) | Bloqueo |
| SHA-256 | `50f2cdf16f05da9253fa2d6eb60d5a42da14c02c551c0874c9e953d4119da69c` | `sophos.exe` (EDR killer) | Bloqueo |
| SHA-256 | `81053c2c3be8b7dbf7d5087dba05c940b3ee4fd95524272651c816b72c5a9443` | `g111.exe` (EDR killer) | Bloqueo |
| SHA-256 | `0be8f415a485b11747bcfd71c9cd9781e090354728f076791ed6845b69ed78fb` | `nogbc.sys` (driver vulnerable) | Lista de bloqueo de drivers |
| SHA-256 | `2d91a78e739891c9854c254f5b2a6b84c0e167dfa253466cbccd2cdd1c20145d` | `G11.sys` (driver vulnerable) | Lista de bloqueo de drivers |
| SHA-1 | `c0979ec20b87084317d1bfa50405f7149c3b5c5f` | `All.exe` (anti-AV) | Bloqueo |
| SHA-1 | `df249727c12741ca176d5f1ccba3ce188a546d28` | `Allpatch2.exe` (anti-AV a medida) | Bloqueo |
| SHA-1 | `e00293ce0eb534874efd615ae590cf6aa3858ba4` | `PowerRun.exe` (escalada) | Bloqueo |
| MD5 | `d65c293efb5e6d033c83b2ac472bf0cb` | SoftPerfect Network Scanner crackeado | Bloqueo |
| MD5 | `42c062d6299ca9f76554441a29429404` | `VCENTER.ps1` — desactiva HA/DRS y apaga VM | Bloqueo |

### A.3 Infraestructura de red

<!-- cti:ioc search="no" -->

| Tipo | Valor | Contexto | Confianza | Caducidad | **Acción permitida** |
|---|---|---|---|---|---|
| ipv4:puerto | `193.233.202[.]17:44729` | C2 (proxy SOCKS vía tarea programada) | Media | **Caducado — observación de 2025** | Solo retrohunt |
| ipv4:puerto | `77.110.122[.]137:37182` | C2 | Media | **Caducado — observación de 2025** | Solo retrohunt |

> **Advertencia operativa.** Solo se dispone públicamente de dos direcciones, ambas
> antiguas. El grupo usa VPS *bulletproof*, Amnezia VPN y Cloudflare Tunnel. **No
> construir la defensa sobre bloqueo de IP.** Además, bloquear infraestructura
> compartida —Cloudflare, MEGA, servicios de RMM— tiene impacto operativo:
> restringir por política de uso, no por lista negra.

### A.4 Artefactos de nombre (mayor vida útil que los hashes)

```
README-GENTLEMEN.txt · gentlemen.bmp · wipefile.tmp · share$ · 1.bat
All.exe · Allpatch2.exe · PowerRun.exe · ThrottleBlood.sys · viragt64.sys
avastrclone.exe · svchost32.exe · ChromeKB3.exe · userpassfort.py · VCENTER.ps1
locker_<6 caracteres>_windows_amd64.exe · G_<6 caracteres>_windows_amd64.exe
Cuentas backdoor en appliance: support_fortinet · badmin · forti-api · guest
Cuentas de dominio: MicrosoftSupporte
```

## Anexo B — Fuentes y valoración

> La numeración de esta tabla es propia del anexo y agrupa fuentes; no coincide
> con la de la lista bibliográfica del final del documento.

| # | Fuente | Fecha | Disciplina | Fiab. | Cred. | Sesgo declarado |
|---|---|---|---|---|---|---|
| 1 | Microsoft Security Blog — análisis del cifrador Go | 2026-05-28 | TECHINT (análisis de binario) | **A** | **1** | Telemetría propia amplia; promociona su producto |
| 2 | Unit 42 (Palo Alto) — «No Manners Here» | 2026-07-10 | TECHINT + OSINT | **A** | **2** | — |
| 3 | Sophos — «Ungentlemanly behavior» | 2026-09 | TECHINT + telemetría de IR | **A** | **2** | Base de casos propios, no representativa del universo |
| 4 | Trend Micro — «Unmasking The Gentlemen» | 2025-09-09 | TECHINT (caso de IR único) | **A** | **2** | **Un solo incidente**: no generalizar la victimología (Tailandia) |
| 5 | Huntress — TTP de evasión | 2026 | TECHINT | **A** | **2** | Sesgo hacia PYME |
| 6 | Group-IB — «Hastalamuerte / Gentlemen RaaS» | 2026 | CLOSINT + HUMINT | **B** | **2** | **Conflicto con la fuente 7 sobre liderazgo** y sobre el reparto 70/30 |
| 7 | KELA — análisis de la filtración interna | 2026-05-14 | CLOSINT (datos de origen adversario) | **B** | **3** | Material filtrado por un criminal; posible contaminación deliberada |
| 8 | Halcyon — evaluación de amenaza | 2026 (mediados) | OSINT comercial | **B** | **3** | Incentivo comercial a enfatizar la escala |
| 9 | Picus Security | 2026-07-06 | OSINT derivado | **B** | **3** | Derivado en gran medida de la fuente 1; **no es corroboración independiente** |
| 10 | FortiGuard Labs | 2026-09-15 | OSINT agregado | **B** | **4** | **Doble cautela:** listado de 14 CVE sin evidencia publicada por CVE; además el fabricante es el del producto que constituye el vector principal |
| 11 | ransomware.live | 2026-09-15 | OSINT (raspado de DLS) | **C** | **2** | **Fuente controlada por el adversario.** Contiene además un artefacto evidente («primera víctima: 2023-02-28»), que se descarta |
| 12 | Darkfield / SOCRadar / Smarttech247 | 2026 | OSINT (raspado de DLS) | **C** | **3** | Metodologías de recuento divergentes |
| **13** | **CSIRT Nacional / ANCI (Chile) — alerta `AIA26-00012`** | 2026-02-10 | **CERT nacional oficial** | **A** | **1** | Máxima fiabilidad y autoridad en el ámbito chileno. Refleja incidentes **reportados** en Chile: no es una muestra del universo global |
| **14** | **CronUp Ciberseguridad (Chile) — «Chile en el radar del ransomware»** | 2026-02-26 | OSINT + monitorización propia (ATRc®) | **A** | **2** | Proveedor nacional con monitorización continua del país; la mejor cobertura disponible del escenario chileno. Proveedor comercial de servicios de CTI |
| **15** | **CronUp — Panorama semanal de ciberseguridad** | 2026-09-04 | OSINT + ATRc® | **A** | **2** | Dato más reciente disponible sobre el pico de agosto de 2026 |
| **16** | ESET WeLiveSecurity (C. Ali Bravo) — expansión LATAM | 2026-03-26 | OSINT + TECHINT | **B** | **2** | Fuente regional con investigación propia; base de telemetría con fuerte implantación en LATAM |
| **17** | a3sec — boletín de alerta regional | 2026-04-07 | OSINT derivado | **B** | **3** | Integrador regional; contenido en parte derivado de las fuentes 4 y 16 — **no es corroboración independiente** |
| — | securityarsenal · tech-insider · decryptiondigest · bmsp.tech · paubox | 2026 | OSINT derivado | **D** | **4** | Contenido derivado sin investigación original. **No usados como base de ningún juicio** |

### B.1 Nota sobre la discrepancia de cifras

| Fuente | Cifra | Fecha de corte |
|---|---|---|
| Group-IB | 94 | 2025-09 |
| Halcyon | ~300 (66+ países) | 2026 (mediados) |
| KELA | 328 (ene–may) | 2026-05 |
| Unit 42 | 580 (77 países) | 2026-07-07 |
| Sophos | 683 | 2026-07 |
| Darkfield | 838 | 2026-09-09 |
| ransomware.live | 868 | 2026-09-15 |
| Smarttech247 | ~330 (70+ países) | 2026-09 |
| — *sin publicar* — | **>1.570** (servidor C2 incautado) | 2026 |

**Valoración:** la serie temporal es internamente coherente salvo la fuente 12,
cuya cifra parece corresponder a un corte anterior o a un criterio de recuento
distinto. Se adopta **~868 como cifra de referencia a 2026-09-15**, con la
advertencia explícita de que procede del sitio del propio adversario, y que la
cifra de 1.570 —de fuente única, no corroborada— sugiere que las víctimas reales
podrían casi doblar a las publicadas.

### B.2 Nota sobre la convergencia y divergencia regional

Las fuentes 13 a 17 **convergen** con las internacionales en lo esencial —el actor,
su modelo de doble extorsión, su presencia en la región— y **divergen** en el
vector de acceso predominante: el CERT chileno documenta cuentas válidas con
credenciales de infostealers y RDP, mientras los proveedores globales priorizan la
explotación de CVE en appliances de borde.

Esta divergencia **eleva la confianza en el perfil combinado** en lugar de
reducirla: dos observadores con visibilidad distinta describen dos vías de entrada
que coexisten. La conclusión defensiva es acumulativa, no alternativa —hay que
cerrar ambas—, y así se refleja en §Estratégico E-4 y §Técnico X-8.

## Anexo C — Léxico de probabilidad y confianza

**Probabilidad estimativa** — cuán probable es que el hecho sea cierto:

| Término | Rango |
|---|---|
| Remoto / casi con certeza no | 1–5 % |
| Muy poco probable | 5–20 % |
| Poco probable | 20–45 % |
| Posibilidad real | 45–55 % |
| Probable | 55–80 % |
| Muy probable | 80–95 % |
| Casi con certeza | 95–99 % |

**Nivel de confianza** — cuán sólida es la base analítica:

| Nivel | Criterio |
|---|---|
| Alta | Varias fuentes de calidad corroboradas, sin brechas relevantes |
| Moderada | Fuentes creíbles con corroboración parcial o brechas conocidas |
| Baja | Fuente única, sin corroborar, o dependiente de supuestos |

## Anexo D — Marcos empleados

MITRE ATT&CK · Cyber Kill Chain · Pirámide del Dolor (Bianco) · ICD 203
(estándares analíticos) · Técnicas Analíticas Estructuradas: ACH, verificación de
supuestos clave, pre-mortem · TLP 2.0 · PAP · Admiralty Code (OTAN)

## Anexo E — Paquete legible por máquina

Pendiente. Generar bundle STIX 2.1 y evento MISP con los indicadores del Anexo A,
aplicando las taxonomías `tlp`, `PAP`, `admiralty-scale` y `estimative-language`, y
**fijando fecha de caducidad en los objetos de red** conforme a las advertencias
de A.3.

## Anexo F — Control de cambios

| Versión | Fecha | Cambio |
|---|---|---|
| **1.5** | **2026-11-21** | **Alineamiento con MITRE ATT&CK v20.1.** ATT&CK reorganizó la matriz y este informe citaba identificadores que la fuente ha **revocado**: `T1070.001` → `T1685.005`, `T1562.001` → `T1685`, `T1562.004` → `T1686`. **Y corrige dos errores de origen que la comprobación contra el catálogo destapó:** `T1548.008` **no existe en ATT&CK**, y el procedimiento que describía —CVE-2025-7771 en `ThrottleStop.sys`, un controlador firmado y vulnerable— es `T1068`; y `T1562.008` era *Disable Cloud Logs*, mientras que el procedimiento escrito (`wevtutil`, registro AutoLogger/GlobalLogger de WMI) es el de eventos de **Windows**, de modo que migra a `T1685.001` y no a `T1685.002` como indicaría la tabla de revocación. **No se extiende `caduca`: se ha puesto al día la nomenclatura de los TTP, no revalidado ningún juicio.** Lo comprueba en adelante la familia `G7` de `tools/cti_gate.py` | Célula CTI |
| 1.0 | 2026-09-15 | Emisión inicial. Todo-fuente externa; §O-4 pendiente de telemetría propia |
| 1.1 | 2026-09-15 | **Incorporación del eje regional Chile/LATAM** (fuentes 13–17): nuevo KJ-7; §E-2.1 con contexto chileno y obligación regulatoria; §O-6.1 con cronología regional y contraste con la alerta `AIA26-00012` del CSIRT Nacional; hipótesis de caza H-10 a H-12; detecciones D-13 y D-14; decisiones E-f a E-h; brechas G-8 a G-11. **Cambio de juicio:** el acceso inicial deja de considerarse exclusivamente por explotación de CVE — se añade la vía de cuenta válida con credenciales de infostealer como concurrente y no cubierta por el parcheo |
| 1.4 | 2026-11-19 | **Medición propia de victimología** sobre un rastreador público (§E-2.3, nuevos `KJ-9` y `KJ-10`): **1.020 víctimas reclamadas en 2026, 129 latinoamericanas en dieciséis países de la región y 90 países en total** —las dos cifras de dispersión más altas de la cartera—, con nueve víctimas chilenas. **Y una corrección de impresión que la comparación obliga a hacer: en exposición chilena este actor es el SEGUNDO**, con nueve frente a las veinte de Qilin; su dato regional central no es Chile sino **la amplitud**. **Se eleva `KJ-6` de confianza baja a moderada** y se recalcula su cifra del 45 % al **54 %**, porque el denominador es ahora medición propia (1.020 en lugar de ~868) y porque **la ficha del rastreador corrobora por su cuenta la cifra de más de 1.570 víctimas reveladas por un servidor de mando y control comprometido**, convirtiendo una fuente única en dos concordantes. Se añaden además tres elementos del inventario publicado que no estaban: **la cadena completa de relevo de NTLM** —de la que sale la nueva hipótesis de caza `H-13`, que **funciona contra sistemas totalmente parcheados** y se cierra con configuración—, **`Velociraptor` usado ofensivamente**, cuya presencia puede confundirse con trabajo del propio equipo de seguridad, y **`Censys` y `Shodan`** como reconocimiento que no deja rastro en nuestros registros. **La caducidad no se extiende**: sigue en 2026-12-15 | Célula CTI |
| 1.3 | 2026-11-19 | **Actualización de victimología con las dos reivindicaciones de alto perfil de noviembre de 2026** (§E-2.2, nuevo `KJ-8`, cuatro filas nuevas en §O-6, fuentes 23–26). **La de NVIDIA está listada y no está confirmada**: sin ficheros de muestra, sin documentos y sin cifra de rescate, con negativa específica de la compañía sobre sus propios sistemas y con dos proveedores suyos listados semanas antes — de donde sale la hipótesis de que el grupo tenga material de un proveedor y haya listado la marca del cliente. **La de DirecTV no aparece en ninguna fuente** y se consigna como no corroborada con lo que se buscó, en lugar de omitirse. Se añaden los disparadores `I-a` a `I-d`. **La caducidad NO se extiende**: sigue en 2026-12-15, porque esta versión añade victimología y no revalida los juicios técnicos del documento, que son de septiembre de 2026 y necesitan revisión propia. **Sin cambios en los indicadores del Anexo A** |
| 1.2 | 2026-11-16 | **Reclasificación de TLP:AMBER a TLP:CLEAR** por decisión del emisor, para publicación en el repositorio abierto `cti_daily`. Verificado previamente que el documento no contiene referencias a la organización emisora ni a marcas asociadas, telemetría propia, direccionamiento interno, nombres de personas ni datos de terceros. **Sin cambios en los juicios analíticos ni en los indicadores.** Se mantiene PAP:AMBER |

## Anexo G — Realimentación del consumidor

| Pregunta | Respuesta |
|---|---|
| ¿Respondió a su requisito? | |
| ¿Qué decisión tomó o cambió? | |
| ¿Qué faltó? | |
| ¿Llegó a tiempo? | |

---

## Fuentes consultadas

1. [Microsoft Security Blog — The Gentlemen ransomware: dissecting a self-propagating Go encryptor](https://www.microsoft.com/en-us/security/blog/2026/05/28/the-gentlemen-ransomware-dissecting-a-self-propagating-go-encryptor/) (2026-05-28)
2. [Unit 42 — No Manners Here: The Ruthless Rise of The Gentlemen Ransomware](https://unit42.paloaltonetworks.com/the-gentlemen-ransomware/) (2026-07-10)
3. [Sophos — Ungentlemanly behavior: Insights into a ransomware operation](https://www.sophos.com/en-us/blog/ungentlemanly-behavior-insights-into-a-ransomware-operation) (2026-09)
4. [Trend Micro — Unmasking The Gentlemen Ransomware](https://www.trendaisecurity.com/en-us/resources-insights/trendai-security-blog/unmasking-the-gentlemen-ransomware) (2025-09-09)
5. [Huntress — The Gentlemen Ransomware: Defense Evasion TTPs](https://www.huntress.com/blog/the-gentlemen-ransomware-defense-evasion-ttps)
6. [Group-IB — How Hastalamuerte Operates: The Gentlemen's Attack Methods](https://www.group-ib.com/blog/hastalamuerte-gentlemen-raas-ttps/)
7. [KELA — Inside The Gentlemen Leak](https://www.kelacyber.com/blog/the-gentlemen-ransomware-internal-chat-leak-analysis-2026/) (2026-05-14)
8. [Halcyon — Threat Assessment: The Gentlemen Ransomware Group](https://www.halcyon.ai/ransomware-research-reports/threat-assessment-the-gentlemen-ransomware-group)
9. [Picus Security — How The Gentlemen Ransomware Spreads and Encrypts Entire Networks](https://www.picussecurity.com/resource/blog/how-the-gentlemen-ransomware-spreads-and-encrypts-entire-networks) (2026-07-06)
10. [FortiGuard Labs — The Gentlemen Ransomware Threat Actor](https://www.fortiguard.com/threat-actor/6387/the-gentlemen-ransomware) (2026-09-15)
11. [Ransomware.live — Thegentlemen](https://www.ransomware.live/group/Thegentlemen) (2026-09-15)
12. [SOCRadar — Inside The Gentlemen Ransomware Leak](https://socradar.io/blog/gentlemen-ransomware-leak/)
13. [Smarttech247 — Escalated Activity from The Gentlemen Ransomware Group](https://www.smarttech247.com/threat-intel-reports/escalated-activity-from-the-gentlemen-ransomware-group)
14. [Darkfield — thegentlemen ransomware group](https://darkfield.orizon.one/groups/thegentlemen)
15. [BankInfoSecurity — Tables Turned: Gentlemen Ransomware Group Suffers Data Leak](https://www.bankinfosecurity.com/tables-turned-gentlemen-ransomware-group-suffers-data-leak-a-31654)

### Fuentes regionales — Chile y Latinoamérica

16. [CSIRT Nacional / ANCI (Chile) — Alerta AIA26-00012: The Gentlemen Ransomware](https://csirt.gob.cl/alertas/aia26-00012/) (2026-02-10, TLP:CLEAR)
17. [CronUp Ciberseguridad — Chile en el radar del ransomware: meses que cambiaron el escenario](https://www.cronup.com/chile-en-el-radar-del-ransomware-meses-que-cambiaron-el-escenario/) (2026-02-26)
18. [CronUp Ciberseguridad — Panorama de ciberseguridad: semana del 31 de agosto al 04 de septiembre de 2026](https://www.cronup.com/panorama-de-ciberseguridad-semana-del-31-de-agosto-al-04-de-septiembre-de-2026/) (2026-09-04)
19. [CronUp Ciberseguridad — Panorama de ciberseguridad: semana del 24 al 28 de agosto de 2026](https://www.cronup.com/panorama-de-ciberseguridad-semana-del-24-al-28-de-agosto-de-2026/)
20. [ESET WeLiveSecurity — The Gentlemen: la nueva generación de ransomware que ataca a medida](https://www.welivesecurity.com/es/ransomware/the-gentlemen-la-nueva-generacion-de-ransomware-que-ataca-a-medida/) (2026-03-26)
21. [a3sec — «The Gentlemen»: la creciente operación de RaaS constituye una grave amenaza en América Latina](https://a3sec.com/alertas/the-gentlemen-ransomware-as-a-service-amenaza-en-america-latina) (2026-04-07)
22. [NetProvider — Ransomware en Chile y Latinoamérica 2026: ataques que cambiaron el escenario](https://www.netprovider.com/post/ransomware-en-chile-2026-ataques-que-cambiaron-el-escenario) (2026-03-10) — *fuente derivada, cita a CronUp*

### Fuentes de la actualización de noviembre de 2026 (versión 1.3)

23. [BleepingComputer — NVIDIA investigating Gentlemen ransomware breach claims](https://www.bleepingcomputer.com/news/security/nvidia-investigating-gentlemen-ransomware-breach-claims/) (2026-11) — **fuente de la declaración de la compañía**: no ha encontrado indicio de afectación de sus sistemas o redes, e investiga un incidente separado en un proveedor de servicios
24. [SecurityWeek — Nvidia Responds to Gentlemen Ransomware Claim](https://www.securityweek.com/nvidia-responds-to-gentlemen-ransomware-claim/) (2026-11) — corrobora la respuesta de la compañía y la ausencia de muestras en el listado
25. [Check Point Research — Thus Spoke…The Gentlemen](https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/) (2026) — sitúa al grupo entre los de mayor volumen del mercado
26. [Ransomware.live — Thegentlemen](https://www.ransomware.live/group/thegentlemen) (2026-11-18) — recuento de 1.123 reivindicaciones en 95 países. **Recuento de reivindicaciones, no de brechas verificadas**
