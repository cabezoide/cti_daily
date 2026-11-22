---
tlp: "TLP:CLEAR"
pap: "PAP:WHITE"
id: "CTI-2026-063"
version: "1.0"
tipo: "Perfil de campaña contra proveedor de servicios gestionados"
foco_regional: "Global · lectura para Latinoamérica y Chile"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "SCKit · conjunto de herramientas sobre ConnectWise ScreenConnect"
fecha: "2026-11-21"
caduca: "2026-12-21"
autor: "Célula CTI"
distribucion: "Elaborado sobre el aviso de Microsoft Threat Intelligence del 13-11-2026, leído en original, más el centro de avisos de ConnectWise y medición propia de resolución DNS y titularidad de direcciones. **Advertencia de uso: cuatro de las siete direcciones a las que resuelven los dominios publicados por Microsoft son de Cloudflare y NO deben bloquearse** —van en el Anexo A con tipo artefacto y marca NUNCA bloqueo—. Difusión libre conservando la atribución de las fuentes y las salvedades de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-063
## SCKit: el parche llevaba dos meses publicado y la campaña entró por otra puerta
### Diez días de actividad sobre instancias ScreenConnect de proveedores gestionados, un gusano que nadie ha visto propagarse, y cuatro direcciones de Cloudflare en la lista de indicadores

> **Regla de oro del producto:** todo párrafo debe responder a un requisito de
> inteligencia (PIR) y habilitar una decisión. Si un párrafo no cambia lo que
> alguien va a hacer, va al anexo o se borra.

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-063` |
| Versión / fecha | `1.0` — 2026-11-21 |
| Tipo de producto | Perfil de campaña contra proveedor de servicios gestionados |
| Niveles cubiertos | Estratégico · Operacional · Táctico · Técnico |
| Foco regional | Global, con lectura para Latinoamérica y Chile |
| Marcado de difusión | `TLP:CLEAR` · `PAP:WHITE` |
| Requisitos atendidos | `PIR-03` (capacidades adversarias que degradan nuestros controles), `PIR-05` (riesgo de terceros y cadena de suministro), `PIR-07` (superficie expuesta a Internet), `PIR-09` (indicadores tempranos de campaña) |
| Consumidor primario | CISO · Jefatura de SOC · Gestión de proveedores · Responsable de herramientas de administración remota |
| Base de colección | Dos fuentes de primera mano: aviso de Microsoft Threat Intelligence (13-11-2026) y centro de avisos de ConnectWise. **Medición propia** de resolución DNS y titularidad de las direcciones, 22-11-2026 02:36 UTC. **Sin telemetría propia de endpoint** |

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** **El gusano no está confirmado, y la fuente lo dice con todas las letras.** La cobertura de esta campaña la describe de forma casi unánime como *malware tipo gusano que se propaga entre proveedores*, pero el aviso de Microsoft escribe, sobre su propio diagrama: *«The dashed path describes the toolkit's propagation design, not a confirmed sequence of infections»*. Es el **diseño** del conjunto de herramientas, no una secuencia de infecciones observada. Valoramos **probable** *(55–80 %)* que la capacidad de propagación exista en el código y **improbable** *(20–45 %)* que se haya ejecutado con éxito en la campaña observada. **Confianza: moderada.** *Base:* afirmación explícita de la fuente primaria sobre el alcance de su propio hallazgo. *Consecuencia:* una respuesta dimensionada para contener un gusano activo gasta en el sitio equivocado; lo que hay que cerrar es el acceso a la consola, no la propagación lateral.

**KJ-2.** **El parche existía desde hacía dos meses, y la campaña no entró por donde el parche cierra.** `CVE-2026-84869` se corrigió en ScreenConnect **26.6.5 el 8 de septiembre de 2026**, y la campaña arranca el **11 de noviembre**. Pero ese CVE bloquea, según ConnectWise, la transferencia de extremo a técnico —la propagación—, **no el acceso inicial**: Microsoft describe la entrada como *«an authentication flaw in RMM+ versions 1.0.31 and 1.0.32»*, una extensión que aceptaba una clave de acceso vacía cuando no se había configurado ninguna, y añade que *«the entry method for the reported campaign remains under investigation»*. Valoramos **muy probable** *(80–95 %)* que parchear el cliente sin desactivar las extensiones deje la puerta de entrada abierta. **Confianza: alta.** *Base:* las dos fuentes de primera mano coinciden en separar las dos cosas.

**KJ-3.** **Cuatro de las siete direcciones a las que resuelven los indicadores publicados son de Cloudflare, y bloquearlas corta a terceros.** Medición propia del 22-11-2026: de los cinco dominios que Microsoft publica, tres —`ns.mo7sen[.]dev`, `cdn007-digitaldownloads[.]com` y, por delegación, el conjunto registrado— resuelven a direcciones de Cloudflare con uso declarado *Content Delivery Network* y en lista blanca de AbuseIPDB. Valoramos **casi con certeza** *(≥99 %)* que una ingesta que resuelva los dominios del aviso y bloquee el resultado provoque un corte propio. **Confianza: alta.** *Base:* medición propia reproducible, §X-1. *Consecuencia:* es el mismo fallo que `CTI-2026-044` documentó en el aviso `AA26-293A`, repetido en otro aviso y a diez días de distancia (`Anexo D`).

**KJ-4.** **La infraestructura propia del actor se reparte en tres alojadores, y dos de ellos son del mismo proveedor.** Descontadas las direcciones de Cloudflare, quedan tres: `185.99.255.28` (DATAWAGON, Reino Unido), `155.94.150.39` (DataWagon LLC, Estados Unidos) y `124.198.131.155` (1337 Services GmbH). **Dos de las tres son DataWagon.** Valoramos **probable** *(55–80 %)* que la concentración refleje una sola decisión de aprovisionamiento y no una coincidencia. **Confianza: moderada.** *Base:* medición propia; dos puntos no sostienen una serie. *Consecuencia:* son direcciones de alojamiento de un cliente, no de infraestructura compartida, y **sí son bloqueables** (`N1`).

**KJ-5.** **Los tres dominios registrados comparten el mismo par de servidores de nombres de Cloudflare.** `mo7sen[.]dev`, `payproofkit[.]com` y `cdn007-digitaldownloads[.]com` delegan los tres en `achiel.ns.cloudflare.com` y `pola.ns.cloudflare.com`. Cloudflare asigna el par de servidores de nombres **por cuenta**, de modo que el mismo par es indicio de la misma cuenta. Valoramos **probable** *(55–80 %)* que los tres dominios se gestionen desde una sola cuenta. **Confianza: moderada.** *Base:* medición propia y comportamiento documentado de la plataforma; no hemos verificado la asignación con el proveedor. *Consecuencia:* es la señal más duradera del expediente —un dominio se quema en días, una cuenta sobrevive— y es la que conviene vigilar (`I-2`).

**KJ-6.** **La cifra de «400 entornos» no mide compromisos, y su propia fuente lo advierte.** ConnectWise comunica alrededor de **400 entornos de socios con al menos una de las extensiones instalada**, y el aviso aclara que eso **no equivale a compromisos confirmados**. Las cifras que circulan en cobertura secundaria —288 extremos en 48 organizaciones— no aparecen en el aviso de Microsoft, que **no publica ninguna cifra de víctimas**. Valoramos **casi con certeza** *(≥99 %)* que citar «400 entornos comprometidos» sea incorrecto. **Confianza: alta.** *Base:* el propio aviso. *Consecuencia:* es un denominador de exposición, no un numerador de impacto (`CTI-2026-046` §O-3.1).

**KJ-7.** **Lo que esta campaña ataca no es un producto, es una relación de confianza.** El acceso se obtiene en la consola del proveedor gestionado y se ejerce sobre los extremos de sus clientes, que no tienen forma de distinguirlo de una intervención legítima de soporte: el agente es el mismo, el canal es el mismo y el técnico es el mismo. Valoramos **muy probable** *(80–95 %)* que una organización que subcontrata administración remota no tenga hoy telemetría propia para detectarlo. **Confianza: moderada.** *Base:* inferencia a partir de la arquitectura descrita, sin telemetría propia que lo mida. *Consecuencia:* la decisión que habilita este informe es contractual antes que técnica (§E-3, `E-b`).

---

## 2. Resumen ejecutivo

El 11 de noviembre de 2026 ConnectWise comunicó que un actor estaba accediendo sin
autorización a instancias de **ScreenConnect alojadas en la nube** pertenecientes a
proveedores de servicios gestionados. El 13 de noviembre Microsoft confirmó la actividad
y publicó el análisis de un conjunto de herramientas al que llama **SCKit**, que el
atacante despliega desde la consola comprometida hacia los extremos de los clientes del
proveedor.

Tres cosas de este expediente no coinciden con cómo se ha contado.

**La primera es el gusano.** La cobertura lo describe como malware de propagación
automática entre proveedores. Microsoft dice explícitamente que el recorrido de
propagación de su diagrama es el **diseño** del conjunto de herramientas y no una
secuencia de infecciones confirmada. La diferencia no es de matiz: cambia dónde hay que
gastar la respuesta.

**La segunda es el parche.** `CVE-2026-84869` está corregido desde el 8 de septiembre en
ScreenConnect 26.6.5, dos meses antes de la campaña. Pero ese arreglo bloquea la
transferencia del extremo hacia el técnico, no la entrada. La entrada que ambas fuentes
describen es otra: una extensión, **RMM+ 1.0.31 y 1.0.32**, que aceptaba una clave de
acceso vacía cuando no se había configurado ninguna. Una organización que actualice el
cliente y deje las extensiones puestas se queda con la puerta abierta.

**La tercera la encontramos nosotros.** De los cinco dominios que Microsoft publica como
indicadores, **cuatro de las siete direcciones a las que resuelven son de Cloudflare**.
Están en lista blanca y su uso declarado es red de distribución de contenidos. Una
ingesta que resuelva los dominios del aviso y bloquee el resultado no corta al adversario:
corta a quien comparta ese frente. Es exactamente el fallo que esta cartera documentó en
el aviso conjunto `AA26-293A` hace apenas un mes, y la segunda vez que lo vemos en un
aviso de primer nivel.

Descontado Cloudflare, la infraestructura propia del actor son tres direcciones en dos
proveedores de alojamiento, **dos de ellas de DataWagon**, y esas sí se bloquean. Y los
tres dominios registrados comparten el mismo par de servidores de nombres de Cloudflare,
que es la señal más duradera que deja el expediente.

---

## 3. Alcance y limitaciones

**3.1 Qué cubre.** La campaña comunicada entre el 11 y el 16 de noviembre de 2026 contra
instancias de ConnectWise ScreenConnect de proveedores gestionados, el conjunto de
herramientas SCKit que se despliega desde ellas, y la higiene de los indicadores
publicados.

**3.2 Qué NO cubre.** No es un perfil de actor: **ninguna de las dos fuentes nombra a un
actor ni propone atribución**, y este informe no la inventa. No evalúa el resto del
catálogo de ConnectWise ni otras plataformas de administración remota, aunque §E-3 señala
por qué el problema no es exclusivo de ésta.

**3.3 Limitaciones de la colección.**

**(i) Sin telemetría propia de endpoint.** Todo lo que este informe dice sobre
comportamiento en el extremo es lectura de un análisis ajeno.

**(ii) El aviso de Microsoft se leyó en original pero no entero.** La extracción devolvió
unos 39.900 de 53.167 caracteres de forma literal, y el corte cae **a mitad de la tabla
de hashes**. Los quince valores SHA-256 del `Anexo A` son los que se leyeron literalmente;
**puede haber más y no los tenemos**. Los tres SHA-1 proceden de una consulta de caza del
propio aviso que los enumera sin asignar cada uno a su fichero, y así se consignan. Se
descartaron dos identificadores de cliente y una asignación de hashes que solo aparecían
en un resumen automático de la parte no leída: **un resumen de la fuente no es la fuente**
(`CTI-2026-054` Anexo D).

**(iii) El aviso de ConnectWise no se leyó literalmente.** Su centro de avisos devolvió el
texto por tramos y el de noviembre cayó fuera de los leídos. Lo que este informe le
atribuye —las cifras de 400 entornos, los nombres de las extensiones, las fechas de
actualización— procede de un resumen automático y se marca como **no verificado en
original** en el `Anexo B`. Es una brecha, no un detalle: la cifra de 400 es la más citada
del expediente.

**(iv) La medición propia es de un solo momento.** Las resoluciones DNS y las
titularidades del `Anexo A` se tomaron el **22-11-2026 a las 02:36 UTC**. La
infraestructura detrás de Cloudflare puede cambiar sin que el dominio cambie, y los dos
dominios de DNS dinámico pueden reapuntar en minutos.

**(v) La asignación de servidores de nombres por cuenta en Cloudflare** es comportamiento
documentado de la plataforma, no una confirmación del proveedor. `KJ-5` se apoya en eso y
por eso es *probable* y no *casi cierto*.

**3.4 Lo que se buscó y no se encontró.** No hay en ninguna de las dos fuentes: nombre de
actor, atribución geográfica, motivación declarada, nota de rescate, cifrado de datos, ni
víctima nombrada. No hemos encontrado ningún informe de tercero que documente una
propagación de extremo a técnico **ejecutada con éxito**.

### 3.5 Lo que el requisito afirmaba, y lo que las fuentes sostienen

<!-- cti:table highlight="Veredicto" -->

| Afirmación de partida | Veredicto | En qué se apoya |
|---|---|---|
| «Un gusano se propaga entre proveedores gestionados» | **No sostenida** | Microsoft describe el recorrido como *diseño*, no como secuencia confirmada (`KJ-1`) |
| «El CVE del producto es la vía de entrada» | **Refutada** | El CVE bloquea la propagación; la entrada descrita es la extensión RMM+ con clave vacía (`KJ-2`) |
| «400 entornos comprometidos» | **Refutada** | Son entornos con la extensión instalada, y el aviso dice que no equivale a compromiso (`KJ-6`) |
| «Los indicadores del aviso son bloqueables» | **Refutada para cuatro de siete** | Resuelven a Cloudflare, en lista blanca y uso CDN (`KJ-3`) |
| «Parchear ScreenConnect resuelve la exposición» | **No sostenida** | Hay que actualizar el cliente de técnico **y** desactivar las extensiones; son acciones distintas (`KJ-2`, `E-a`) |
| «Es una campaña de extorsión» | **Sin base** | Ninguna fuente menciona cifrado, nota ni sitio de filtración |

---

# NIVEL ESTRATÉGICO

### Para: CISO · Comité de Riesgo · Gestión de proveedores · Horizonte: semanas–meses

## E-1. Por qué esto importa aunque no uses ScreenConnect

El objeto atacado no es un producto: es la **relación de confianza** con quien administra
tus equipos. Un proveedor gestionado mantiene un agente privilegiado y permanente en los
extremos de sus clientes, y ese agente está diseñado precisamente para que las acciones
remotas sean indistinguibles del trabajo legítimo de soporte. Cuando el atacante opera
desde la consola del proveedor, la víctima observa exactamente lo que observaría un
martes cualquiera.

La consecuencia es incómoda y conviene decirla sin rodeos: **la organización cliente no
suele tener forma propia de detectar esto**, porque ha subcontratado justo la capa desde
la que se detectaría (`KJ-7`).

## E-2. La ventana de dos meses, que es el dato de gestión

<!-- cti:timeline -->

| Fecha | Suceso |
|---|---|
| `2026-09-08` | ConnectWise publica la corrección de `CVE-2026-84869` en ScreenConnect 26.6.5 |
| `2026-11-11` | ConnectWise comunica acceso no autorizado a instancias en la nube de proveedores gestionados |
| `2026-11-12` | ConnectWise cifra en unos **400 entornos de socios** los que tienen al menos una extensión instalada, y advierte que no equivale a compromisos |
| `2026-11-13` | Microsoft confirma la actividad y publica el análisis de SCKit. ConnectWise desactiva preventivamente tres integraciones más |
| `2026-11-16` | ConnectWise da por terminada su investigación; las acciones de protección siguen siendo obligatorias |
| `2026-11-22` | Medición propia de resolución y titularidad (`§X-1`) |

**Sesenta y cuatro días** entre el parche y el inicio de la campaña. Esa es la ventana
real de decisión, y es la cifra que un comité de riesgo debe mirar: no cuánto tardó el
proveedor en corregir, sino cuánto tardó el parque en aplicarlo.

Y hay un matiz operativo que explica buena parte del retraso, porque Microsoft lo señala
expresamente: **actualizar la consola en la nube no actualiza los clientes de técnico**.
Son dos acciones, y la segunda se olvida.

## E-3. Decisiones

<!-- cti:accordion critical="E-a" -->

| Ref | Decisión | Por qué | Plazo |
|---|---|---|---|
| **E-a** | **Exigir al proveedor gestionado constancia escrita de dos cosas por separado:** versión del cliente de técnico ≥ 26.6.5 **y** extensiones RMM+ desactivadas | Son controles distintos contra problemas distintos; el parche no cubre la entrada (`KJ-2`) | 7 días |
| **E-b** | **Incorporar al contrato con proveedores de administración remota la obligación de notificar incidentes en su propia plataforma**, con plazo, y el derecho a exigir registros de sesión | Hoy la organización cliente depende de que el proveedor quiera contarlo (`KJ-7`) | 60 días |
| **E-c** | **Inventariar qué proveedores tienen agente privilegiado permanente** en nuestros extremos, y con qué producto | Sin inventario no hay forma de responder a la pregunta «¿nos afecta?» en menos de una semana | 30 días |
| **E-d** | **No bloquear las direcciones del aviso sin resolver su titularidad.** Cuatro de siete son Cloudflare | Un corte propio por ingesta ingenua (`KJ-3`) | Inmediato |
| **E-e** | Revisar si el contrato permite que el proveedor instale extensiones de terceros en la consola sin aprobación | La vía de entrada fue una extensión, no el producto | 60 días |

## E-4. Lectura regional

Ninguna de las dos fuentes nombra países ni víctimas, de modo que **no hay dato regional
que reportar** y no se va a fabricar uno. Lo que sí es específico de la región es la
estructura del mercado: la administración de sistemas subcontratada a proveedores
pequeños y medianos es la norma en buena parte del tejido empresarial latinoamericano, y
esos proveedores rara vez tienen un equipo de seguridad propio que aplique un parche de
septiembre antes de noviembre. **La exposición regional es plausible y no está medida**,
y así se consigna (`G-3`).

---

# NIVEL OPERACIONAL

### Para: Jefatura de SOC · Respuesta a incidentes · Horizonte: días–semanas

## O-1. La cadena, con lo que está confirmado y lo que no

<!-- cti:stages title="Cadena observada" dwell="next" -->

| Etapa | Qué ocurre | Estado |
|---|---|---|
| 01 · Acceso a la consola | Acceso no autorizado a instancias de ScreenConnect en la nube de proveedores gestionados. Microsoft describe un fallo de autenticación en la extensión **RMM+ 1.0.31 y 1.0.32**, que aceptaba clave vacía si no se había configurado ninguna | **Confirmado** como actividad; el método de entrada sigue *bajo investigación* según la fuente |
| 02 · Despliegue al extremo | Desde la consola, instalación de clientes de acceso remoto no autorizados en los extremos de los clientes del proveedor, con `sc.msi` descargado a `C:\Windows\Temp\` | **Confirmado** |
| 03 · Preparación | Extracción del paquete a `%TEMP%\SCKitBundle` y del payload a `%TEMP%\SCKit\trapkit\payload`; recuperación de decodificador, paquete y utilidad desde `ns.mo7sen[.]dev/EadF.php` con parámetros `p=1`…`p=6` y el `MachineGuid` del equipo | **Confirmado** |
| 04 · Persistencia | Scripts en `C:\ProgramData\RelayTrap`, valor `RelayTrapLiteAlert` en la clave `Run` de máquina, y tarea programada que arranca un vigilante con `-PollSeconds 10` | **Confirmado** |
| 05 · Degradación de defensas | Exclusiones plantadas en la clave de rutas excluidas de Microsoft Defender para las copias del MSI y el instalador | **Confirmado** |
| 06 · Hacia el técnico | Transferencia del extremo hacia la estación del técnico de soporte, con el objetivo declarado de alcanzar sus sesiones | **DISEÑO, no confirmado** (`KJ-1`) |

## O-2. Por qué la etapa 06 es la que hay que leer con cuidado

Es la etapa que da titulares y la única que la fuente marca como no observada. Microsoft
escribe que *«the dashed path describes the toolkit's propagation design, not a confirmed
sequence of infections»*, y en la misma página dice haber identificado que el gusano
*«targets IT support technician workstations»* — identificar un objetivo en el código no
es observar que lo alcanzó.

Hay además una asimetría que refuerza la lectura prudente: ConnectWise afirma que el
arreglo de `CVE-2026-84869`, publicado en septiembre, **bloquea** esa transferencia. Si la
corrección llevaba dos meses disponible y el mecanismo depende de ella, el conjunto de
extremos donde la propagación podía funcionar era el de los clientes sin actualizar, que
es un subconjunto y no el parque.

**Lo que cambia en la práctica:** la prioridad no es cazar propagación lateral entre
proveedores. Es (a) cerrar el acceso a la consola, (b) encontrar los clientes de acceso
remoto no autorizados ya instalados, y (c) revocar sesiones de técnico, que es lo que el
diseño perseguía aunque no conste que lo lograra.

## O-3. Hipótesis consideradas

| Hipótesis | Evaluación | Estado |
|---|---|---|
| H1 — Es una operación de extorsión en fase previa al cifrado | Ninguna fuente menciona cifrado, nota de rescate ni sitio de filtración. El conjunto de herramientas está orientado a acceso y persistencia | `Posible, sin evidencia` |
| H2 — El objetivo final son las sesiones del técnico, para alcanzar a muchos clientes desde una credencial | Es lo que el diseño del kit persigue según la fuente, y explica la arquitectura observada | `Probable` |
| H3 — La campaña es obra del mismo actor que preparó la infraestructura en julio | BleepingComputer informa de un fichero por lotes subido a VirusTotal el 25-07-2026 que referencia un identificador de cliente luego vinculado a SCKit. **No verificado por nosotros ni por la fuente primaria** | `Sin resolver` |
| H4 — Se trata de explotación oportunista de instancias expuestas, sin selección de víctima | Coherente con un denominador de 400 entornos y sin víctimas nombradas, pero nada lo sostiene positivamente | `Posible` |

## O-4. Lo que una organización cliente puede preguntar hoy

Tres preguntas que no exigen telemetría propia y que el proveedor debe poder responder
por escrito en 48 horas:

1. ¿Qué versión tiene **cada** cliente de técnico, no la consola? *(Microsoft advierte que actualizar la consola no actualiza los clientes.)*
2. ¿Estuvieron instaladas en algún momento las extensiones **Labtech Plus, RMM Plus, RMM+, RMM Plus Password Link o RMM+ Password Link**, y cuándo se desactivaron?
3. ¿Se han revocado las sesiones web de ScreenConnect **y las del proveedor de identidad**, desde un equipo limpio, y se han rotado las credenciales? *(Cambiar la contraseña no invalida una sesión ya robada.)*

---

# NIVEL TÁCTICO

### Para: Ingeniería de detección · Threat hunting · Horizonte: días

## T-1. Mapa MITRE ATT&CK

<!-- cti:matrix -->

| Táctica | ID | Técnica | Procedimiento observado |
|---|---|---|---|
| Desarrollo de recursos | T1583.001 | Acquire Infrastructure: Domains | Tres dominios registrados —`mo7sen[.]dev`, `payproofkit[.]com`, `cdn007-digitaldownloads[.]com`— delegados en el **mismo par de servidores de nombres de Cloudflare** (`KJ-5`) |
| Acceso inicial | T1199 | Trusted Relationship | Acceso a los extremos del cliente **a través de la consola del proveedor gestionado**, por un canal que la víctima no puede distinguir del soporte legítimo |
| Acceso inicial | T1078 | Valid Accounts | Fallo de autenticación en la extensión RMM+ 1.0.31/1.0.32: clave de acceso vacía aceptada cuando no había ninguna configurada |
| Mando y control | T1219 | Remote Access Tools | Instalación de clientes **ScreenConnect no autorizados** apuntando a servidor propio; la herramienta es legítima y el abuso está en la instancia |
| Sigilo | T1218.007 | System Binary Proxy Execution: Msiexec | Paquete `sc.msi` descargado a `C:\Windows\Temp\` e instalado |
| Ejecución | T1059.001 | Command and Scripting Interpreter: PowerShell | `Stage0Loader.ps1`, `Panel-Lateral.ps1`, `TrapWatch.ps1`, `Lite-Alert.ps1` y un script temporal `%TEMP%\k<32-hex>.ps1` |
| Persistencia | T1547.001 | Boot or Logon Autostart: Registry Run Keys | Valor **`RelayTrapLiteAlert`** en la clave `Run` de ámbito de máquina |
| Ejecución · Persistencia | T1053.005 | Scheduled Task/Job: Scheduled Task | Tarea que arranca el vigilante con `-PollSeconds 10`. **El aviso no publica el nombre de la tarea** |
| Degradación de defensas | T1685 | Disable or Modify Tools | Exclusiones de ruta plantadas en la clave de exclusiones de Microsoft Defender para las copias del MSI y el instalador |
| Degradación de defensas · Persistencia | T1112 | Modify Registry | Escritura en `Run`, en exclusiones de Defender y lectura de `Cryptography\MachineGuid` |
| Descubrimiento | T1082 | System Information Discovery | `MachineGuid` de `HKLM\SOFTWARE\Microsoft\Cryptography` usado como identificador del equipo en las peticiones |
| Descubrimiento | T1012 | Query Registry | Lectura del registro para obtener el identificador anterior |
| Acceso a credenciales | T1539 | Steal Web Session Cookie | **Objetivo declarado del diseño**: las sesiones autenticadas de los técnicos de soporte. No consta que se alcanzara (`KJ-1`) |
| Mando y control | T1071.001 | Application Layer Protocol: Web Protocols | Peticiones HTTP a `ns.mo7sen[.]dev/EadF.php` con parámetros `p=1` a `p=6` y el `MachineGuid` |
| Mando y control | T1105 | Ingress Tool Transfer | Recuperación escalonada de decodificador, paquete, script y utilidad desde el mismo punto |
| Mando y control | T1568 | Dynamic Resolution | Dos relés sobre **DNS dinámico**: `newnewnew[.]gotdns[.]org` y `soxnewwork[.]homedns[.]org` |
| Sigilo | T1036 | Masquerading | El cliente de acceso remoto instalado es ScreenConnect legítimo; lo ilegítimo es a qué servidor apunta |

## T-2. Hipótesis de caza

| Ref | Hipótesis | Dónde mirar | Por qué funciona |
|---|---|---|---|
| **H-1** | Hay un cliente de ScreenConnect instalado que apunta a un servidor que no es el de nuestro proveedor | Inventario de servicios y configuración de los agentes ScreenConnect; relés y servidores configurados | **Es la detección de más valor del expediente.** El binario es legítimo y firmado; lo anómalo es el destino |
| **H-2** | Existe la carpeta `C:\ProgramData\RelayTrap` o un valor `RelayTrapLiteAlert` en `Run` | Sistema de ficheros y registro | Artefactos de persistencia con nombre propio, triviales de buscar y específicos |
| **H-3** | Alguien ha añadido exclusiones de ruta a Defender que nadie documentó | Clave de exclusiones de rutas de Defender, comparada con la línea base de configuración | Una exclusión no autorizada es señal con independencia de esta campaña |
| **H-4** | Hay tareas programadas con intervalo de sondeo de 10 segundos creadas en la ventana del 11 al 16 de noviembre | Inventario de tareas con fecha de creación | El intervalo es inusualmente corto para una tarea legítima |
| **H-5** | Un equipo resolvió alguno de los cinco dominios del `Anexo A` | Registros de DNS recursivo | **Funciona aunque las direcciones cambien**, que es justo lo que las vuelve inútiles (`KJ-3`) |
| **H-6** | Una sesión de técnico se usó desde una dirección o un horario que no cuadra | Registros de autenticación de ScreenConnect y del proveedor de identidad | Es lo que el diseño perseguía; conviene mirarlo aunque no conste que se lograra |

**H-5 merece una nota:** cazar por **dominio** en los registros de DNS es superior a cazar
por dirección en este expediente, porque las direcciones de tres de los cinco dominios son
de Cloudflare y por tanto no identifican nada, mientras que el nombre sí.

---

# NIVEL TÉCNICO

### Para: Ingeniería de detección · TIP/SIEM · Vida útil: días–semanas

## X-1. Medición propia: qué hay detrás de cada indicador publicado

Resolución y titularidad tomadas el **22-11-2026 a las 02:36 UTC** — es decir, la noche del 21 en hora de Chile, que es la fecha de emisión de este informe. La marca se da en UTC porque es la que permite reproducir la consulta. El método es
reproducible con `dig` y una consulta de titularidad; se detalla en el `Anexo D`.

<!-- cti:table highlight="Acción" -->

| Dominio publicado | Resuelve a | Titular | Acción |
|---|---|---|---|
| `ns.mo7sen[.]dev` | `104.21.17.120`, `172.67.176.189` | **Cloudflare** (CDN, lista blanca) | Bloquear el **dominio**; **NUNCA** las direcciones |
| `cdn007-digitaldownloads[.]com` | `104.21.41.192`, `172.67.166.210` | **Cloudflare** (CDN, lista blanca) | Bloquear el **dominio**; **NUNCA** las direcciones |
| `sc.payproofkit[.]com` | `155.94.150.39` | DataWagon LLC (EE. UU.) | Bloquear dominio y dirección |
| `newnewnew[.]gotdns[.]org` | `185.99.255.28` | DATAWAGON (Reino Unido) | Bloquear dominio y dirección |
| `soxnewwork[.]homedns[.]org` | `124.198.131.155` | 1337 Services GmbH | Bloquear dominio y dirección |

**Cuatro de las siete direcciones son de Cloudflare.** Las dos que Microsoft publica
directamente como indicadores —`185.99.255.28` y `155.94.150.39`— **sí** son de
alojamiento de un solo cliente y sí se bloquean; el problema aparece cuando alguien
resuelve los dominios y añade el resultado a la misma lista. Eso es un `N1` de libro
(`tools/cti_enriquecer.py`).

**Y la señal duradera:** los tres dominios registrados delegan en el mismo par de
servidores de nombres, `achiel.ns.cloudflare.com` y `pola.ns.cloudflare.com`. Cloudflare
asigna ese par por cuenta.

## X-2. Lógica de detección prioritaria

```
# 1 · Agente ScreenConnect que apunta a un servidor que no es el nuestro
#     Ajustar la lista blanca al relé legítimo del proveedor.
DeviceProcessEvents
| where FileName =~ "ScreenConnect.ClientService.exe"
   or ProcessCommandLine has_any ("ScreenConnect", "ConnectWiseControl")
| where not(ProcessCommandLine has_any (<RELES_LEGITIMOS>))
```

```
# 2 · Persistencia con nombre propio
DeviceRegistryEvents
| where RegistryKey has @"\CurrentVersion\Run"
| where RegistryValueName =~ "RelayTrapLiteAlert"
```

```
# 3 · Exclusión de Defender añadida fuera de proceso de cambio
DeviceRegistryEvents
| where RegistryKey has @"Windows Defender\Exclusions\Paths"
| where ActionType == "RegistryValueSet"
```

```
# 4 · Resolución de los dominios del expediente (vale aunque cambien las IP)
DeviceNetworkEvents
| where RemoteUrl has_any ("mo7sen.dev", "payproofkit.com",
                           "cdn007-digitaldownloads.com",
                           "newnewnew.gotdns.org", "soxnewwork.homedns.org")
```

**Detecciones del proveedor** que el aviso nombra y que conviene comprobar que están
activas: `Trojan:Win32/SuspScreenConnectDownload.EA` y
`Trojan:PowerShell/RelayPersist.FC!MTB`.

## X-3. Mitigaciones con efecto directo

1. **Actualizar cada cliente de técnico a 26.6.5 o posterior, uno a uno.** La consola no los actualiza.
2. **Mantener desactivadas** Labtech Plus, RMM Plus, RMM+, RMM Plus Password Link y RMM+ Password Link, y revisar su historial de instalación.
3. **Investigar por un canal fuera de banda**, nunca a través de ScreenConnect. Si la consola está comprometida, el canal de respuesta también.
4. **Revocar sesiones** de ScreenConnect y del proveedor de identidad desde un equipo limpio, y rotar credenciales. Cambiar la contraseña no basta.
5. **No usar el script de limpieza del propio kit.**
6. **Conservar evidencia antes de limpiar**: registros de extensiones, de autenticación, de ejecución de comandos y del Toolbox.

---

## 14. Brechas de inteligencia y requisitos de colección

**G-1.** **El aviso de ConnectWise no se ha leído en original** (§3.3-iii). La cifra de 400
entornos, los nombres de las extensiones y las fechas de actualización dependen de un
resumen automático. *Requisito:* localizar la URL propia del aviso de noviembre y leerlo.

**G-2.** **La tabla de hashes de Microsoft está incompleta** (§3.3-ii): el corte cae a
mitad. *Requisito:* obtener el resto.

**G-3.** **No hay dato de exposición regional.** Ninguna fuente nombra países. *Requisito:*
preguntar a los proveedores gestionados del entorno chileno si usan ScreenConnect y en qué
versión; es colección propia y barata.

**G-4.** **No sabemos si la propagación al técnico se ejecutó alguna vez.** Es la brecha que
sostiene `KJ-1`.

**Disparadores de reevaluación.**
`I-1`: **cualquier informe que documente una transferencia de extremo a técnico ejecutada con éxito** — convertiría `KJ-1` en refutado y cambiaría la prioridad de respuesta.
`I-2`: **aparición de un dominio nuevo delegado en `achiel.ns.cloudflare.com` + `pola.ns.cloudflare.com` con patrón de nombre similar** — confirmaría `KJ-5` y daría indicador anticipado.
`I-3`: atribución de la campaña a un actor con nombre, que hoy no existe en ninguna fuente.
`I-4`: aparición de cifrado o de sitio de filtración, que convertiría esto en una operación de extorsión y resolvería `H1`.
`I-5`: que alguna de las tres direcciones de alojamiento aparezca en otra campaña —vigilable con `tools/cti_enriquecer.py`—.

---

# ANEXOS

## Anexo A — Indicadores de compromiso

<!-- cti:note type="warn" -->

> ⚠ **Leer antes de usar.** **Cuatro de las siete direcciones a las que resuelven los
> dominios de este expediente son de Cloudflare**, con uso declarado de red de
> distribución de contenidos y en lista blanca de AbuseIPDB. Van abajo con tipo
> `artefacto` y marca **NUNCA bloqueo**, y **no entran en ninguna lista plana**. Bloquear
> el **dominio** es correcto; bloquear su dirección corta a terceros. Es el mismo fallo
> que `CTI-2026-044` documentó en el aviso `AA26-293A`.

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Acción |
|---|---|---|---|---|
| domain | `ns.mo7sen[.]dev` | Punto de recuperación de decodificador, paquete, script y utilidad (`/EadF.php`) | Alta | Bloqueo |
| domain | `sc.payproofkit[.]com` | Panel y fuente de instalador de ScreenConnect no autorizados | Alta | Bloqueo |
| domain | `cdn007-digitaldownloads[.]com` | Infraestructura de campaña; fuente de instalador configurada | Alta | Bloqueo |
| domain | `newnewnew[.]gotdns[.]org` | Relé de ScreenConnect asociado, sobre DNS dinámico | Alta | Bloqueo |
| domain | `soxnewwork[.]homedns[.]org` | Relé de ScreenConnect asociado, sobre DNS dinámico | Alta | Bloqueo |
| ipv4 | `185.99.255[.]28` | Servidor ScreenConnect no autorizado y fuente de instalador. DATAWAGON, Reino Unido | Alta | Bloqueo |
| ipv4 | `155.94.150[.]39` | Panel no autorizado. DataWagon LLC, Estados Unidos | Alta | Bloqueo |
| ipv4 | `124.198.131[.]155` | Destino de `soxnewwork[.]homedns[.]org` el 22-11-2026. 1337 Services GmbH. **Medición propia, no publicada por la fuente** | Moderada | Bloqueo tras verificación |
| artefacto | `104.21.17[.]120` · `172.67.176[.]189` · `104.21.41[.]192` · `172.67.166[.]210` | **Cloudflare.** Destinos de `ns.mo7sen[.]dev` y `cdn007-digitaldownloads[.]com`. Uso declarado CDN, en lista blanca | Alta | **NUNCA bloqueo** |
| artefacto | `achiel.ns.cloudflare.com` · `pola.ns.cloudflare.com` | Par de servidores de nombres compartido por los tres dominios registrados. Cloudflare los asigna por cuenta (`KJ-5`) | Moderada | Caza y vigilancia; **NUNCA bloqueo** |
| sha256 | `61a672a13f03a9e81f573535ee92b1ed6cb7e848a33a06048865312d4e185ae2` | Paquete `sc.msi` | Alta | Bloqueo |
| sha256 | `8e6912deed82e80bb6bd66f73509d024b1f78b993515366d8317e69a97cff4f4` | ZIP de conjunto de herramientas preparado | Alta | Bloqueo |
| sha256 | `8cb5f48bbe70b5248db7f327f3d1ad6649df5c767d2a7e0711ee147fd92e06af` | `ToolboxRelayUploader.exe` | Alta | Bloqueo |
| sha256 | `94b93c649b0ae0281352da9d01761fa9195ab1e6ac7010af3b9ba1646355eb11` | `Panel-Lateral-free.ps1` | Alta | Bloqueo |
| sha256 | `7a9aca9fdd4dcc13fe497cabdb13ca1e5d6a529271c8aa495e5ca1c1c80271ec` | `Panel-Lateral.ps1` | Alta | Bloqueo |
| sha256 | `b93f10f30ee453d1e1c046fec9d141c41d7680be5cd46c3aeb3febe0f4953b4d` | Auxiliar `LabConfig.ps1` | Alta | Bloqueo |
| sha256 | `3c7a98f0fdb6235b8076319c74dc1085f7b349b6d750416dd0cadb07d7972ec4` | `RelayTrap.cs` | Alta | Bloqueo |
| sha256 | `d2ed7a7bf4f8ac9c7969e9b3a07ebd4dda0d858f372c876ac0a041611698de9a` | `TrapWatch.ps1` | Alta | Bloqueo |
| sha256 | `4a1dd3cd2ea14368afadf7e9dfdd63b104e3981ef8c85bbb6510919b810af04b` | `trapkit\install.ps1` | Alta | Bloqueo |
| sha256 | `cf50d73fa8117a758093b1344de41cd6a6ccddc645cdda1fa91a9264efe93956` | `Lite-Alert.ps1` | Alta | Bloqueo |
| sha256 | `81cc2baa35b798d6084bd078662fa29ff28df02c46c6ccdb2b43bde97d19f781` | `Stage0Loader.ps1` | Alta | Bloqueo |
| sha256 | `43b7a5e56f9e6c7b74e1ce2b7b5af63f383084625fcc2d3a5985fa1059e2db95` | `Run-Lateral-Full.bat` | Alta | Bloqueo |
| sha256 | `50659748723e906c8b3d3c0386bd4cf692f693a3e23639398c1a14d0c31fed61` | `runnew.cmd` | Alta | Bloqueo |
| sha256 | `5dd3a6ba806ac472663e243cfc1c034c534d5d9a42ec362c3dbf0f8d950148d0` | `Stop-LabTrap.bat` | Alta | Bloqueo |
| sha256 | `454c43d296b1276bde9a4f6ff1da2221cb35ccdb2fc7991bdd572e45bce12a8a` | `TRAP-PROOF.bat` | Alta | Bloqueo |
| sha1 | `0be01e7bd69cfdd222645d49bb5ad9961372fef2` | Instalador, archivo o utilidad de subida. **El aviso los enumera sin asignar cada hash a su fichero** | Moderada | Retrohunt |
| sha1 | `3f81c9c874a896c46e4bccea2fad2eaa3d9f2054` | Ídem | Moderada | Retrohunt |
| sha1 | `13ce33b19daee3963f7e15d461b191c38f6bc0d3` | Ídem | Moderada | Retrohunt |
| filepath | `C:\ProgramData\RelayTrap` | Directorio de scripts de persistencia | Alta | Detección y caza |
| filepath | `C:\Windows\Temp\sc.msi` | Instalador descargado | Alta | Detección |
| filepath | `%TEMP%\SCKitBundle` · `%TEMP%\SCKit\trapkit\payload` | Extracción del paquete y preparación del payload | Alta | Detección |
| artefacto | Valor `RelayTrapLiteAlert` en la clave `Run` de máquina | Persistencia con nombre propio | Alta | Detección y caza |
| artefacto | Tarea programada con `-PollSeconds 10` | Vigilante de persistencia. **El aviso no publica el nombre de la tarea** | Moderada | Caza |
| pattern | `%TEMP%\k<32 hex>.ps1` | Script temporal del cargador | Moderada | Detección por patrón |
| pattern | `/EadF.php?p=1..6&m=<MachineGuid>` | Protocolo de recuperación escalonada | Alta | Detección en egreso |
| servicio | `gotdns.org` · `homedns.org` | **Servicios legítimos de DNS dinámico** usados para los relés. Bloquear el dominio completo rompe a terceros | Alta | Bloqueo del subdominio concreto únicamente |
| herramienta | ConnectWise ScreenConnect | **Producto legítimo.** El abuso está en la instancia a la que apunta el cliente, no en el binario | Alta | Inventario, nunca bloqueo |

## Anexo B — Fuentes y valoración

| # | Fuente | Fecha | Admiralty | Nota |
|---|---|---|---|---|
| 1 | Microsoft Threat Intelligence, *SCKit abuses ScreenConnect…* | 2026-11-13 | **B1** | **Leída en original**, de forma literal hasta ~39.900 de 53.167 caracteres (§3.3-ii) |
| 2 | ConnectWise, centro de avisos | 2026-11-11 a 16 | **B2** | **NO leída en original** (§3.3-iii). Lo que se le atribuye procede de un resumen automático |
| 3 | Medición propia de resolución DNS y titularidad | 2026-11-22 02:36 UTC (noche del 21 en Chile) | **A1** | Reproducible; método en el `Anexo D` |
| 4 | Cobertura secundaria (BleepingComputer, Blackpoint, Field Effect) | 2026-11 | **C3** | Consultada para contraste. **Sus cifras de víctimas no se reproducen**: no aparecen en las fuentes primarias (`KJ-6`) |

**B.1 — Lo que se consultó y no se reprodujo.** Las cifras «288 extremos en 48
organizaciones» y «400+ entornos comprometidos» circulan en cobertura secundaria, se
contradicen entre sí y **no están en ninguna de las dos fuentes primarias**. No se
reproducen (`KJ-6`).

## Anexo C — Léxico

Probabilidad y confianza se declaran por separado, según ICD 203. Probabilidad:
*casi con certeza* (≥99 %), *muy probable* (80–95 %), *probable* (55–80 %),
*posibilidad real* (45–55 %), *improbable* (20–45 %), *muy improbable* (5–20 %).
Confianza: *alta*, *moderada*, *baja*, y mide la calidad de la base, no la fuerza del juicio.

## Anexo D — Método: comprobar la higiene de los indicadores de un aviso antes de ingerirlos

**El problema.** Un aviso de primer nivel publica dominios y direcciones. La ingesta
resuelve los dominios y añade todo a la lista de bloqueo. Si alguno está detrás de una red
de distribución de contenidos, la lista corta a terceros y el fallo es **silencioso**:
nadie relaciona la caída de un servicio con la lista que se cargó anteayer.

**Es la segunda vez en un mes.** `CTI-2026-044` lo documentó en el aviso conjunto
`AA26-293A`, donde cuatro de nueve direcciones eran Cloudflare, GitHub y Google. Aquí son
cuatro de siete. **No es un descuido de un aviso concreto: es una propiedad de publicar
indicadores de infraestructura moderna.**

**El procedimiento, que cuesta dos minutos por aviso:**

1. **Resolver cada dominio** del aviso, no solo leer las direcciones que publica:
   `dig +short <dominio> A`. Las direcciones peligrosas suelen ser las que el aviso **no**
   lista, porque aparecen al resolver.
2. **Consultar la titularidad** de cada dirección resultante. Las tres señales que
   descalifican el bloqueo son: **lista blanca** del servicio de reputación, **uso
   declarado «Content Delivery Network»**, e **ISP en la lista de infraestructura
   compartida**. Ojo: *Data Center/Web Hosting* con puntuación cero **no** descalifica —
   describe cualquier servidor privado virtual, incluido el del adversario
   (`tools/cti_enriquecer.py`, regla `N1`).
3. **Separar en la tabla** lo bloqueable de lo que no, con tipo distinto. En esta cartera,
   `ipv4` entra en los agregados planos y `artefacto` no: el tipo es el mecanismo, no una
   etiqueta descriptiva.
4. **Consultar los servidores de nombres** (`dig +short <dominio> NS`). Si varios dominios
   del aviso comparten par, hay un vínculo de cuenta y una señal que dura más que
   cualquier dirección.
5. **Preferir la caza por dominio** en los registros de DNS recursivo. Sobrevive a la
   rotación de direcciones y no se contamina con la infraestructura compartida.

**El criterio que resume todo:** *una dirección detrás de una red de distribución de
contenidos no identifica a nadie.* El nombre sí.

## Anexo E — Marcos empleados

MITRE ATT&CK Enterprise v20.1 para los procedimientos; ICD 203 para el lenguaje
estimativo; código Admiralty para la valoración de fuentes.

## Anexo F — Paquete legible por máquina

Los indicadores de este informe se exportan a `ioc_index.csv` con su tipo, contexto,
confianza y acción permitida. Las entradas con tipo `artefacto`, `servicio` y
`herramienta` **no** entran en `ioc_ipv4.txt` ni en `ioc_url.txt` por diseño.

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-11-21 | Emisión inicial. Establece tres cosas que la cobertura de la campaña no sostiene: que el gusano es **diseño y no propagación observada** (`KJ-1`), que el parche de septiembre **no cubre la vía de entrada** (`KJ-2`), y que la cifra de 400 entornos es un **denominador de exposición y no de compromiso** (`KJ-6`). Aporta medición propia de resolución y titularidad que encuentra **cuatro direcciones de Cloudflare entre los destinos de los indicadores publicados** (`KJ-3`), la concentración en DataWagon (`KJ-4`) y el par de servidores de nombres compartido (`KJ-5`). `Anexo D` con el procedimiento de higiene de indicadores de un aviso, que es la segunda vez que esta cartera lo necesita | Célula CTI |

## Anexo H — Realimentación del consumidor

Este informe cambia si aparece: una propagación de extremo a técnico documentada
(`I-1`), un dominio nuevo con el mismo par de servidores de nombres (`I-2`), o una
atribución con nombre (`I-3`). Quien observe cualquiera de las tres, que lo diga.
