---
tlp: "TLP:CLEAR"
pap: "PAP:WHITE"
id: "CTI-2026-064"
version: "1.0"
tipo: "Perfil de actor y evaluacion de continuidad de marca"
foco_regional: "Global · lectura para Latinoamérica y Chile"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "ShinyHunters, INCEPTION y el clúster de intrusión O-UNC-053"
fecha: "2026-11-24"
caduca: "2026-12-24"
autor: "Célula CTI"
distribucion: "Elaborado sobre tres fuentes de primera mano leídas en original —el expediente de Okta Threat Intelligence del 24-11-2026, la investigación de ReversingLabs y el aviso público `I-051526-PSA` del IC3 del FBI— más **medición propia del 24-11-2026** sobre servidores de claves OpenPGP, DNS, WHOIS, RDAP, RIPEstat, NVD y dos agregadores de sitios de extorsión. **No se reproducen los nombres de las personas detenidas** —§3.2— ni los nombres de las organizaciones que un sitio de filtración reivindica sin muestras. **Advertencia de uso: las dos direcciones de `breachforums.hn` son de Cloudflare y NO deben bloquearse**; van en el Anexo A con tipo artefacto y marca NUNCA bloqueo. Difusión libre conservando la atribución de las fuentes y las salvedades de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-064
## La marca volvió el 23 de noviembre firmada con dos claves que su propio dueño había retirado en marzo
### Tres objetos distintos reclaman hoy el nombre ShinyHunters, el clúster que alimentaba su sitio de filtración nunca se detuvo, y la única prueba criptográfica del regreso es verificable desde fuera —lo hicimos— y no acredita lo que se le atribuye

> **Regla de oro del producto:** todo párrafo debe responder a un requisito de
> inteligencia (PIR) y habilitar una decisión. Si un párrafo no cambia lo que
> alguien va a hacer, va al anexo o se borra.

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-064` |
| Versión / fecha | `1.0` — 2026-11-24 |
| Tipo de producto | Perfil de actor y evaluación de continuidad de marca |
| Niveles cubiertos | Estratégico · Operacional · Táctico · Técnico |
| Foco regional | Global, con lectura para Latinoamérica y Chile |
| Marcado de difusión | `TLP:CLEAR` · `PAP:WHITE` |
| Requisitos atendidos | `PIR-01` (actores con capacidad e intención sobre nuestro sector), `PIR-02` (robo de datos y extorsión sin cifrado), `PIR-03` (capacidades que degradan nuestros controles de identidad), `PIR-05` (riesgo de terceros y cadena de suministro SaaS), `PIR-09` (indicadores tempranos de campaña) |
| Consumidor primario | CISO · Jefatura de SOC · Responsable de identidad y accesos · Mesa de ayuda · Comunicación de crisis |
| Ventana de observación | 2020-01-28 → 2026-11-24, con foco en 2026-09-15 → 2026-11-24 |
| Base de colección | Tres fuentes de primera mano leídas en original: expediente de **Okta Threat Intelligence** (24-11-2026), investigación de **ReversingLabs** y aviso **`I-051526-PSA`** del **IC3 del FBI** (15-05-2026). Prensa especializada con verificación propia declarada: **BleepingComputer** (23-11-2026). **Medición propia del 24-11-2026**: servidores de claves OpenPGP, `gpg --list-packets`, validación de suma de control de seis direcciones de servicio oculto, DNS, WHOIS, RDAP, RIPEstat, NVD y dos agregadores de extorsión. **Sin telemetría propia de identidad ni de extremo** |
| Autor (analista) | Célula CTI |
| Caducidad / revisión | 2026-12-24 |
| Productos relacionados | `CTI-2026-018` (el clúster `.report`, donde la atribución a este actor se descartó como hecho) · `CTI-2026-047` (evaluar una afirmación de rebranding) · `CTI-2026-055` (reclamaciones cruzadas) · `CTI-2026-058` (decidir si un actor cesó o migró) · `CTI-2026-048` (escala de prueba de ocho niveles) · `CTI-2026-063` (el parche que existía y la campaña que entró por otra puerta) |
| Paquete legible por máquina | Anexo F |

> ⚠ **Limitación estructural.** Este informe **no incorpora telemetría propia de
> identidad, de correo ni de extremo**. Todo lo que se afirma sobre el modo de entrada
> del adversario procede de dos proveedores; lo que es medición propia está marcado como
> tal y es reproducible con los comandos del `Anexo F`. En consecuencia, **no se evalúa la
> eficacia real de ninguna detección** en nuestro entorno: §T-2 propone hipótesis de caza,
> no resultados.

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** **La única prueba criptográfica del regreso está firmada con dos claves que su propio titular revocó ocho meses antes, y la clave que declaró vigente no aparece.** Medición propia del 24-11-2026 sobre `keys.openpgp.org` y `keyserver.ubuntu.com`: las dos claves de 2020 usadas para autenticar el anuncio del 23-11-2026 —`1FC4D0B1…C989B3` y `828537C1…C7CE51`— llevan **certificado de autorrevocación fechado el 17-03-2026**, con razón **`0x01`, «clave sustituida»**, y con un puntero a la sustituta. Recuperamos ese puntero y la clave que designa es `F4953411…20978A`, **que no está revocada**. Ninguno de los mensajes de noviembre examinados por la fuente que los verificó está firmado con ella. Que las firmas son válidas y que las claves están revocadas es **hecho medido, no estimación**; **confianza: alta**. Sobre lo que eso significa, valoramos **probable** *(55–80 %)* que quien publicó el anuncio **no tenga** la clave vigente de marzo. *Base:* medición propia reproducible, §X-1. *Consecuencia:* la continuidad del operador no está acreditada, y tratar al que volvió como «el mismo actor» es una decisión, no una lectura de la evidencia.

**KJ-2.** **Hoy hay tres objetos distintos reclamando el nombre, y la atribución por marca ya no identifica a un operador.** A 24-11-2026 conviven: el **sitio nuevo del 23-11** que reivindica ser ShinyHunters; **INCEPTION**, aparecido el 16-11 y alimentado por el clúster de intrusión que durante seis meses alimentó el sitio anterior; y **ShinySp1d3r**, la plataforma de cifrado anunciada hace doce meses. Valoramos **muy probable** *(80–95 %)* que un incidente nuevo atribuido «a ShinyHunters» en las próximas semanas corresponda a uno de estos tres y no se pueda asignar sin medir infraestructura. **Confianza: alta.** *Base:* las tres apariciones están datadas por fuentes distintas y medidas por nosotros, §O-1. *Consecuencia:* en una comunicación de crisis, el nombre del grupo **no** es un dato; la vía de entrada sí.

**KJ-3.** **El clúster que ejecuta las intrusiones no se detuvo en ningún momento: lo que se cayó fue el escaparate.** Okta documenta que `O-UNC-053` siguió registrando infraestructura de suplantación durante octubre y la primera mitad de noviembre **sin ningún sitio donde publicar**, y que reaparece en INCEPTION con la misma infraestructura y las mismas tácticas. Valoramos **muy probable** *(80–95 %)* que las detenciones de septiembre hayan afectado a la publicación y al cobro, **no** a la capacidad de intrusión. **Confianza: alta.** *Base:* fuente primaria con serie temporal de registros propia, corroborada por nuestra medición de WHOIS en tres dominios, §X-2. *Consecuencia:* una defensa dimensionada contra «el grupo desarticulado» se dimensiona contra el objeto equivocado.

**KJ-4.** **El catálogo de 161 entradas no mide 161 víctimas, y la propia fuente permite demostrarlo.** Medición propia del 24-11-2026 sobre `ransomware.live`: **dos entradas no son víctimas** sino comunicados del adversario dirigidos al FBI; el campo de rescate está vacío en **161 de 161**, el de volumen de datos en **161 de 161**, y hay captura de pantalla en sólo **47 de 161 (29,2 %)**. El segundo agregador que esta cartera usa cuenta **109** entradas para el mismo actor: **una discrepancia del 32,3 %**. Y el conjunto anual de la primera fuente da **110**, que **no es un tercer recuento sino el subconjunto de 2026** —parecido engañoso que invita a tomar dos cifras incomparables por corroboración mutua, §O-2.3—. Valoramos **casi con certeza** *(≥99 %)* que cualquier cifra de víctimas de este actor citada sin declarar su fuente y su base de conteo sea incorrecta. **Confianza: alta.** *Base:* medición propia, §O-2. *Consecuencia:* es el mismo defecto que `CTI-2026-060` y `CTI-2026-061` documentaron en otros catálogos, aquí con un agravante: **el adversario publica en su propio catálogo entradas que no son reclamaciones**.

**KJ-5.** **La reivindicación de «día cero» contra el FBI no se sostiene si el identificador que la cobertura asigna es correcto.** `CVE-2026-35273` —PeopleSoft Enterprise PeopleTools 8.61 y 8.62, toma de control sin autenticar— figura en el NVD **publicada el 11-06-2026**, con **CVSS 9.8** y estado *Analyzed*: medición propia del 24-11-2026. La reivindicación es de **septiembre de 2026**, tres meses después. Valoramos **probable** *(55–80 %)* que lo ocurrido fuese un parche crítico no aplicado por un tercero y **improbable** *(20–45 %)* que hubiera día cero. **Confianza: moderada**, porque el identificador lo aporta cobertura secundaria y no la fuente primaria. *Base:* §O-4.2. *Consecuencia:* es exactamente el patrón de `CTI-2026-063`, y la decisión que habilita es de gestión de parches en terceros, no de capacidad adversaria.

**KJ-6.** **Chile no aparece en este expediente como víctima, sino como un dato de registrante en el WHOIS de la infraestructura de señuelo, y eso no es corroborable desde fuera.** De las 161 entradas del catálogo, **ninguna** tiene país `CL`; hay dos latinoamericanas, una colombiana y una mexicana. En cambio, ReversingLabs declara que los dominios de señuelo registrados en NICENIC repiten **tres perfiles de ubicación de registrante: Carolina del Norte, Chile y Bermudas**. Comprobamos el WHOIS público de tres de esos dominios el 24-11-2026 y **el campo de registrante viene redactado o vacío en los tres**: el dato existe para quien tiene acceso a WHOIS histórico o no redactado, y **nosotros no podemos confirmarlo**. Valoramos **probable** *(55–80 %)* que el perfil chileno sea un dato de registro falso y no un indicio de operación en el país. **Confianza: baja.** *Base:* afirmación de proveedor no corroborable con los medios de esta célula, §E-4 y brecha `G-3`.

**KJ-7.** **El sitio de filtración cayó, pero los prefijos que lo alojaban siguen anunciados y en manos del mismo alojador.** Medición propia del 24-11-2026: las cuatro direcciones que los agregadores asocian al sitio están en **`PROSPERO OOO` (`AS200593`)** y **`Proton66 OOO` (`AS198953`)**; `91.202.233.0/24` lo anuncia `AS200593` con **313 de 322** pares RIS viéndolo y `176.120.22.0/24` lo anuncia `AS198953` con **311 de 322**, ambos con última observación de **hoy a las 08:00 UTC**. Valoramos **muy probable** *(80–95 %)* que el bloque `/24` del alojador sobreviva a cualquier marca que opere sobre él. **Confianza: alta.** *Base:* RDAP y RIPEstat, §X-2. *Consecuencia:* el indicador duradero es el prefijo, no la dirección de servicio oculto, que no se resuelve por DNS y cuyo bloqueo no produce efecto alguno.

**Qué cambiaría estos juicios.** Tres falsadores concretos y observables: **(1)** que aparezca un mensaje firmado con `F4953411…20978A`, la clave vigente de marzo —eso convertiría `KJ-1` en lo contrario y acreditaría continuidad—; **(2)** que una organización nombrada en INCEPTION o en el sitio nuevo **confirme** una brecha, lo que daría por primera vez un numerador a las reclamaciones; **(3)** que `ShinySp1d3r` publique una primera víctima verificable, lo que lo movería de «plataforma anunciada» a «capacidad en uso» y cambiaría por completo el perfil de impacto de §E-1.

---

## 2. Resumen ejecutivo

El 30 de septiembre de 2026 el sitio de filtración de ShinyHunters dejó de estar
disponible, un día después de que expirase un plazo que el propio grupo había dado al FBI
y quince días después de la primera de las detenciones de ese mes. Siete semanas más
tarde el nombre ha vuelto, pero no en un sitio: **en tres**. El 16 de noviembre apareció
INCEPTION, que publica a organizaciones atacadas por el mismo clúster de llamadas
telefónicas fraudulentas que alimentaba el sitio anterior. El 23 de noviembre apareció un
servicio oculto que reivindica ser ShinyHunters y que, para probarlo, publica dos
mensajes firmados con claves criptográficas históricas del grupo. Y sigue en catálogo,
desde hace doce meses y sin una sola víctima, la plataforma de cifrado ShinySp1d3r.

**Lo que este informe aporta y no estaba publicado es que la prueba criptográfica se
puede comprobar desde fuera, y que al comprobarla no dice lo que se le atribuye.** Las
dos claves de 2020 con que se firmó el anuncio del 23 de noviembre **las revocó su propio
titular el 17 de marzo de 2026**, declarando el motivo «clave sustituida» y dejando en el
propio certificado un puntero a la sustituta. Recuperamos el puntero, recuperamos la
clave que designa, y comprobamos que **no está revocada**: es la única que el grupo
declaró vigente. No se usó. Firmar con ella era gratis y zanjaba la cuestión.

Para la organización esto se traduce en tres cosas concretas. **Primera**, que el nombre
del grupo ha dejado de ser un dato útil: lo que identifica al adversario que nos
importaría es la vía de entrada, y la de este ecosistema es una llamada de teléfono a una
persona de la casa para que teclee sus credenciales y apruebe un segundo factor en una
página que imita exactamente nuestro proveedor de identidad. **Segunda**, que el control
que lo detiene está identificado y es uno: autenticación resistente a suplantación. El
kit que estos operadores usan **no** es capaz de superar FIDO2 o passkeys, y eso lo afirma
el proveedor de identidad cuyos clientes están siendo atacados. **Tercera**, que la
infraestructura previa de los señuelos es visible días antes del ataque: los dominios se
registran con nuestro nombre y una palabra jurídica, en ventana vespertina UTC, sin
registros de correo —no sirven para enviar correo porque el engaño llega por teléfono—, y
entre uno y veintiocho días antes de que la organización aparezca en un sitio de
filtración.

**Lo que no se puede decir** es cuántas víctimas tiene este actor. Las dos fuentes que
esta cartera usa a diario discrepan en un tercio, dos de las entradas del catálogo no son
víctimas sino comunicados al FBI, y el 71 % de las entradas no alcanza ni el nivel de
prueba de una captura de pantalla.

<!-- cti:cards -->

| Rasgo | Qué significa | Etiqueta |
|---|---|---|
| La marca es separable del operador | Desarticular a quien cobra no desarticula a quien entra; el escaparate se reconstruye en semanas | `01 · continuidad` |
| El objetivo es la capa de identidad, no el extremo | Ningún antivirus participa en esta cadena: el adversario entra autenticado y a la primera | `02 · identidad` |
| El engaño llega fuera de banda | La llamada no pasa por el filtro de correo, y el dominio del señuelo no tiene ni MX | `03 · teléfono` |
| El kit se adapta a nuestro proveedor | La página imita el inquilino concreto de la víctima, comprobado antes de llamar | `04 · suplantación` |
| La prueba de la reclamación casi nunca existe | Rescate y volumen vacíos en 161 de 161 entradas; captura en 47 | `05 · prueba` |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `3` | marcas distintas reclamando el nombre a 24-11-2026 | Sitio nuevo del 23-11, INCEPTION del 16-11 y ShinySp1d3r desde 2025-11-15 |
| `17-03-2026` | fecha de revocación de las dos claves usadas como prueba el 23-11-2026 | Razón declarada por el titular: «clave sustituida» |
| `0` | mensajes de noviembre firmados con la clave vigente de marzo | Es la omisión sobre la que descansa `KJ-1` |
| `161` vs `109` | entradas del mismo actor en los dos agregadores de la cartera | Discrepancia del **32,3 %** |
| `0 de 161` | entradas con cifra de rescate o volumen de datos | La prueba de la reclamación no está en el catálogo |
| `0` | víctimas chilenas en el catálogo | Chile aparece como perfil de registrante en WHOIS, no como objetivo |
| `12 meses` | desde el anuncio de ShinySp1d3r sin una sola víctima publicada | La API responde «no victims found» |
| `313 de 322` | pares RIS que ven el prefijo del alojador del sitio caído, hoy | El escaparate cae; el bloque `/24` no |

> ✅ **Decisión que se solicita a Dirección:** **(a)** declarar la autenticación resistente
> a suplantación —FIDO2, passkeys, autenticadores ligados al origen— **obligatoria** para
> todo acceso administrativo y para todo acceso a SaaS con datos de clientes, con plazo de
> 60 días; **(b)** aprobar un procedimiento de verificación de identidad para la mesa de
> ayuda que **prohíba** restablecer credencial o segundo factor a partir de una llamada
> entrante, con plazo de 15 días; **(c)** encargar a gestión de proveedores el inventario
> de aplicaciones conectadas con tokens de larga vida sobre nuestro CRM y nuestra
> mensajería, con plazo de 30 días.

---

## 3. Alcance y limitaciones

### 3.1 Qué contiene este informe

La evaluación de **continuidad de marca** de ShinyHunters entre el 15 de septiembre y el
24 de noviembre de 2026, con el método para resolverla desde fuera; el perfil del clúster
de intrusión que alimentaba su sitio de filtración y que hoy alimenta otro; la medición
propia de la infraestructura de los tres objetos que reclaman el nombre; la medición del
catálogo de víctimas y de lo que ese catálogo no prueba; y la lectura de todo ello para
una organización chilena o latinoamericana.

### 3.2 Qué NO contiene, por decisión

- **No se reproducen los nombres de las personas detenidas.** Son personas físicas con
  presunción de inocencia, los cargos no están probados y ninguno de los juicios de este
  informe depende de su identidad: lo que los sostiene son **las fechas**. Las fuentes que
  los nombran están en el `Anexo B` para quien necesite seguirlas.
- **No se reproducen los nombres de las organizaciones reivindicadas** en ningún sitio de
  filtración, ni las siete de INCEPTION ni las del catálogo anterior. Son reclamaciones
  del adversario sin muestras verificadas; reproducirlas es amplificarlas. **Sí se
  publican los dominios de señuelo**, que contienen marcas de terceros: la justificación
  de esa asimetría está en el `Anexo A.1` y no es cómoda, pero es defendible.
- **No se evalúa el contenido de ningún conjunto de datos filtrado.** No se descarga, no
  se abre y no se cuentan registros.
- **No hay análisis de binario.** No existe muestra pública del kit de suplantación: la
  propia Okta declara que los retos de Cloudflare delante de los dominios **le impidieron
  analizarlo en profundidad**. El nivel técnico de este informe es, por tanto, medición de
  infraestructura y de criptografía, no ingeniería inversa.

### 3.3 La base de este informe, y su desigualdad

Hay **tres fuentes de primera mano leídas en original**: el expediente de Okta, la
investigación de ReversingLabs y el aviso del IC3. Hay **una fuente de prensa
especializada que declara verificación propia** —BleepingComputer verificó las firmas PGP
con la clave pública que ya había usado en agosto de 2025— y esa declaración es la que
permite que `KJ-1` exista: nosotros podemos comprobar el estado de las claves, pero **no
tenemos los dos mensajes firmados**, que viven en un servicio oculto al que esta célula
no accede. Esa es la asimetría, y conviene verla con claridad:

| Lo que medimos nosotros | Lo que tomamos de un tercero |
|---|---|
| Que las dos claves de 2020 están revocadas el 17-03-2026, con razón `0x01` | Que los mensajes del 23-11-2026 se firmaron con ellas |
| Que el puntero de la revocación lleva a `F4953411…20978A` y que esa clave no está revocada | Que ninguno de los mensajes de noviembre se firmó con ella |
| Que la clave presentada el 23-11 se creó el **31-10-2026** y no lleva certificación de terceros en dos servidores | Que el sitio nuevo existe y qué dice |

**Si la verificación de BleepingComputer fuera errónea, `KJ-1` cae.** Se consigna así en
lugar de presentarlo como medición completa propia.

### 3.4 Lo que la ausencia de telemetría propia deja sin evaluar

Sin registros de nuestro proveedor de identidad no podemos decir si esta campaña nos ha
llamado. La pregunta **sí tiene respuesta** y está en §T-2: son cuatro consultas sobre
registros que la organización ya tiene. Mientras no se ejecuten, la afirmación «no nos
afecta» no tiene base, y este informe no la hace.

### 3.5 Lo que se afirma sobre este actor, y lo que las fuentes sostienen

<!-- cti:table highlight="Veredicto" -->

| Afirmación de partida | Veredicto | En qué se apoya |
|---|---|---|
| «ShinyHunters ha vuelto» | **No sostenida como hecho** | La prueba son dos firmas con claves revocadas por su titular en marzo; la clave vigente no aparece (`KJ-1`) |
| «INCEPTION es ShinyHunters con otro nombre» | **No sostenida** | Okta afirma el cambio de afiliación del **clúster de intrusión**, y dice expresamente que **no** puede determinar con confianza alta quién opera el sitio (`KJ-2`) |
| «Las detenciones desarticularon al grupo» | **Refutada** | El clúster siguió registrando infraestructura todo octubre y noviembre; lo que cesó fue la publicación (`KJ-3`) |
| «El actor tiene N víctimas» | **Indeterminable con las fuentes públicas** | 161 frente a 109 según el agregador, dos entradas que no son víctimas, y cero con rescate o volumen (`KJ-4`) |
| «Explotaron un día cero de PeopleSoft» | **Improbable** | El CVE que la cobertura asigna se publicó el 11-06-2026, tres meses antes de la reivindicación (`KJ-5`) |
| «El FBI publicó un informe FLASH sobre el grupo en el segundo trimestre» | **Inexacta** | El documento es un **PSA** del IC3, `I-051526-PSA`, del 15-05-2026, y versa sobre el ataque a una plataforma educativa (`O-4.1`) |
| «El grupo opera desde Chile» | **Sin base** | El único vínculo es un perfil de registrante en WHOIS que no es corroborable con medios públicos (`KJ-6`) |
| «ShinySp1d3r es una capacidad de cifrado en uso» | **No sostenida** | Doce meses sin una víctima publicada, y la dirección que el agregador le atribuye **no es una dirección de Tor válida** (`O-1.3`) |

---

# NIVEL ESTRATÉGICO

### Para: CISO · Comité de Riesgo · Comunicación de crisis · Horizonte: semanas–meses

## E-1. Lo que el expediente mide, y lo que no

<!-- cti:bars title="Entradas del catálogo por mes de ataque declarado" -->

| Mes | Entradas |
|---|---|
| 2025-05 | 7 |
| 2025-06 | 11 |
| 2025-07 | 7 |
| 2025-08 | 6 |
| 2025-09 | 7 |
| 2025-10 | 5 |
| 2026-01 | 2 |
| 2026-02 | 9 |
| 2026-03 | 16 |
| 2026-04 | 23 |
| 2026-05 | 9 |
| 2026-06 | 19 |
| 2026-07 | 6 |
| 2026-08 | 18 |
| 2026-09 | 7 |
| 2026-10 | 0 |
| 2026-11 | 0 |

**Tres lecturas, y la tercera es la que vale.** La primera, la obvia: la actividad crece
a lo largo de 2026 y se detiene en seco en septiembre. La segunda, la cautelosa: el mes
de ataque lo declara el adversario y no lo verifica nadie, de modo que la serie mide
**lo que el adversario dice haber hecho y cuándo**. La tercera, que es la útil: **la
última entrada del catálogo es del 24 de septiembre de 2026 y las dos siguientes casillas
están a cero**, lo que sitúa el cese de publicación —no el cese de actividad— entre la
primera detención y el final del plazo que el grupo había dado al FBI.

**Y hay un escalón de cobertura que invalida cualquier medida de «cuándo apareció este
actor».** Por fecha de descubrimiento, **45 de las 161 entradas se registraron en octubre
de 2025**, el mes en que el sitio se dio de alta en el agregador, con fechas de ataque
declaradas que van de noviembre de 2023 a octubre de 2025. Es el defecto que el `Anexo D`
de `CTI-2026-054` describe y cuyo correctivo es restar: **la antigüedad del expediente
mide al observador, no al observado**.

## E-2. La marca como activo separable, que es la novedad de este expediente

Esta cartera ha documentado ya rebranding (`CTI-2026-047`), cese frente a migración
(`CTI-2026-058`) y reclamaciones cruzadas entre actores (`CTI-2026-055`). Lo de ahora es
distinto y conviene nombrarlo bien: **no es que un grupo se cambie de nombre, es que un
nombre se queda sin dueño determinable y varios lo usan a la vez.**

La estructura que lo hace posible la describe la propia fuente primaria: el operador del
sitio de filtración **tenía relación con varios operadores de intrusión a la vez**
—Okta lo afirma porque observó en ese sitio organizaciones que su clúster no había
atacado—, de modo que el sitio era un **servicio de publicación y cobro** y no el grupo.
Separados el escaparate y la intrusión, cada parte sobrevive por su cuenta: la intrusión
cambió de escaparate en siete semanas, y el nombre del escaparate quedó disponible para
quien tuviera con qué reclamarlo.

<!-- cti:timeline -->

| Fecha | Hecho | Grado |
|---|---|---|
| 2020-01-28 | Creación de la primera de las dos claves PGP históricas | Medición propia |
| 2020-08-25 | Creación de la segunda | Medición propia |
| 2025-10-03 | Alta del sitio de filtración en el agregador, con volcado retrospectivo de 45 entradas | Medición propia |
| 2025-11-15 | Alta de ShinySp1d3r en el agregador, como plataforma de cifrado | Medición propia |
| 2026-03-16 | Publicación de la clave sustituta `F4953411…20978A` | Medición propia sobre copia archivada |
| 2026-03-17 | **Autorrevocación de las dos claves de 2020**, razón «clave sustituida» | Medición propia |
| 2026-05-15 | Aviso `I-051526-PSA` del IC3 del FBI sobre el actor | Fuente oficial |
| 2026-09-15 | Primera detención del mes, en los Países Bajos | Prensa, citada por fuente primaria |
| 2026-09-22 | El actor publica en su propio sitio un comunicado dirigido al FBI con un plazo de una semana | Medición propia sobre el catálogo |
| 2026-09-24 | **Última entrada del catálogo** | Medición propia |
| 2026-09-29 | Segunda detención del mes, en Jordania | Prensa, citada por fuente primaria |
| 2026-09-30 | El sitio de filtración deja de estar disponible | Prensa, citada por fuente primaria |
| 2026-10-26 | Arranca la campaña de señuelos con tema jurídico | Fuente primaria |
| 2026-10-31 | **Creación de la clave que se presentará el 23-11** | Medición propia |
| 2026-11-16 | Aparece INCEPTION | Dos fuentes primarias |
| 2026-11-23 | Aparece el sitio que reivindica ser ShinyHunters, con dos firmas de 2020 | Prensa con verificación declarada |
| 2026-11-24 | Okta publica la evaluación de cambio de afiliación; esta célula mide la cadena de claves | Fuente primaria y medición propia |

## E-3. Decisiones

<!-- cti:accordion critical="E-a" -->

| Decisión | Qué implica | Por qué ahora |
|---|---|---|
| **E-a · Autenticación resistente a suplantación, obligatoria** | FIDO2, passkeys o autenticadores ligados al origen en todo acceso administrativo y a SaaS con datos de clientes. Plazo 60 días | Es el **único** control que las dos fuentes primarias señalan como efectivo: el kit **no** puede superarlo. Un segundo factor por código o por notificación **no protege** aquí, porque el adversario está al teléfono pidiendo que se apruebe |
| **E-b · La mesa de ayuda no restablece nada desde una llamada entrante** | Procedimiento de verificación por canal alternativo antes de tocar credencial o segundo factor. Plazo 15 días | Es la puerta concreta de esta cadena, y es un cambio de proceso que no cuesta licencias |
| **E-c · Inventario de aplicaciones conectadas con token de larga vida** | Sobre CRM, mensajería y repositorios documentales; revocación de lo que no tenga dueño. Plazo 30 días | El historial de este ecosistema incluye el abuso de tokens de integración de terceros, y un token no se detiene con autenticación fuerte: ya está autenticado |
| **E-d · Vigilancia de registros de dominio con nuestra marca y término jurídico** | Alta en transparencia de certificados y en registros nuevos, con el patrón de §T-2 | La infraestructura aparece entre **1 y 28 días** antes de la publicación: es aviso previo real y gratuito |
| **E-e · Protocolo de comunicación que no nombre al grupo** | La nota pública describe vía de entrada y alcance, no marca | `KJ-2`: hoy el nombre no identifica operador, y atribuir a un grupo desarticulado invita a una corrección pública |

## E-4. Lectura regional: dónde aparece Chile en este expediente, y dónde no

**No aparece como víctima.** De las 161 entradas, **ninguna** lleva país `CL`. Hay dos
latinoamericanas —una colombiana con fecha de ataque declarada en mayo de 2026 y una
mexicana de julio de 2025— sobre 151 entradas con país asignado, es decir **un 1,3 %**.
El reparto está dominado por Estados Unidos, con **114 de 161 (70,8 %)**, y detrás vienen
Francia con 6, Alemania con 5 y Suiza, Países Bajos y Japón con 3 cada uno. **Diez
entradas no tienen país**, de modo que el denominador real es 151 y no 161.

**Aparece, en cambio, en el registro de la infraestructura.** ReversingLabs declara que
los dominios de señuelo registrados a través de NICENIC repiten tres perfiles de
ubicación de registrante, y uno de los tres es **Chile**. Esto no dice que el adversario
opere desde Chile: un perfil de registrante es un dato que el registrante escribe. Lo
comprobamos en el WHOIS público de tres dominios del conjunto el 24-11-2026 y **el campo
viene redactado o vacío en los tres**, de modo que **no podemos corroborarlo** y queda
como `G-3`.

**La lectura que sí sirve para una organización chilena es la tercera.** Este adversario
no selecciona por país: selecciona por **marca reconocible con mesa de ayuda centralizada
y proveedor de identidad estándar**, y la lista de señuelos que ReversingLabs publica
—donde hay cadenas de comida rápida, estudios de videojuegos, aerolíneas, un bufete y
operadores de medios— se explica por tamaño y por reconocimiento, no por geografía. La
pregunta útil no es «¿nos tienen por objetivo?» sino la del `Anexo D` de `CTI-2026-036`:
**¿tendríamos el dato si la respuesta fuera sí?** Y la respuesta está en §T-2: cuatro
consultas sobre registros que ya existen.

---

# NIVEL OPERACIONAL

### Para: Jefatura de SOC · Respuesta a incidentes · Gestión de identidad · Horizonte: días–semanas

## O-1. Los tres objetos que reclaman el nombre, y cómo se distinguen

### O-1.1 El clúster de intrusión, que es el único cuya continuidad está acreditada

Okta lo rastrea como **`O-UNC-053`** desde **marzo de 2026**. Lo que hace, en la
descripción de la fuente primaria: **ingeniería social por teléfono en varias etapas**,
en la que quien llama se hace pasar por personal de soporte y empuja al usuario a
restablecer su contraseña con urgencia. Detrás hay un kit que intercepta el flujo de
autenticación: primero recoge usuario y contraseña, después pide los segundos factores, y
mientras tanto el operador —al teléfono— convence a la persona de que le dicte el código
o apruebe la notificación. Con eso entra en las aplicaciones SaaS y extrae datos.

Dos rasgos importan para la defensa. El primero, que la fuente declara el límite del kit:
**no puede superar autenticación resistente a suplantación**. El segundo, que los temas
de los dominios de señuelo **cambian cada cuatro a seis semanas**, y el actual, desde
finales de octubre de 2026, es **jurídico**.

### O-1.2 INCEPTION, que es un escaparate nuevo sobre el mismo canal de entrada

Apareció el **16 de noviembre de 2026**. Lo que Okta afirma, y conviene citar con
precisión porque la cobertura lo ha redondeado: que `O-UNC-053` **ha cambiado muy
probablemente de afiliación de marca**, y que **no puede valorar con confianza alta** si
ese clúster opera el sitio por sí mismo o se ha asociado con otro actor de extorsión. El
apoyo es un intervalo medido: la infraestructura de señuelo de los objetivos que INCEPTION
nombra se registró **entre 6 y 19 días antes** de que aparecieran en el sitio, igual que
antes aparecían en el sitio anterior **entre 1 y 28 días** después del registro.

### O-1.3 ShinySp1d3r, que en doce meses no ha publicado una víctima — y cuya dirección no es válida

Se dio de alta en el agregador el **15-11-2025** como plataforma de cifrado como servicio
contra entornos VMware ESXi. Medición propia del 24-11-2026: la consulta de víctimas de
ese grupo devuelve **`No victims found for group 'ShinySp1d3r'`**. Doce meses, cero
entradas.

**Y hay un defecto en la fuente que conviene documentar porque afecta a cualquiera que la
ingiera.** La dirección de servicio oculto que el agregador atribuye a ShinySp1d3r es
`sh1nysp1d3rxyz123456789abcdefghijklmnopqrstuvwxyz.onion`. Aplicando la validación de
suma de control que esta cartera adoptó el 22-11-2026: **tiene 49 caracteres y una
dirección v3 tiene exactamente 56**, y el cuerpo es la secuencia `xyz` seguida de los
dígitos y el alfabeto en orden. **No es una dirección: es un marcador de posición.** No
decodifica, no corresponde a ninguna clave Ed25519 y no puede validarse. Quien la ingiera
como indicador distribuye una cadena inventada. Las otras cinco direcciones del mismo
expediente **sí** validan, y eso es lo que hace al defecto detectable: el control no es
una sospecha, es aritmética. Va al `Anexo A.4` con tipo `artefacto` y marca de no bloqueo,
y a la brecha `G-5`.

## O-2. El catálogo, medido

### O-2.1 Lo que hay, y lo que falta

<!-- cti:table highlight="Cobertura" -->

| Campo | Relleno | Cobertura | Qué se puede preguntar con él |
|---|---|---|---|
| `activity` (sector) | 160 / 161 | 99,4 % | Reparto sectorial, con una entrada «Not Found» ×4 dentro del propio campo |
| `country` | 151 / 161 | 93,8 % | Reparto geográfico **sobre 151**, nunca sobre 161 |
| `domain` | 108 / 161 | 67,1 % | Correlación con exposición propia, por quien tenga el dominio |
| `screenshot` | 47 / 161 | **29,2 %** | Nivel 3 de la escala de prueba de `CTI-2026-048`, el que más engaña |
| `press` | 17 / 161 | **10,6 %** | Único camino hacia confirmación independiente |
| `data_size` | **0 / 161** | **0 %** | Nada |
| `ransom` | **0 / 161** | **0 %** | Nada |

**Las dos últimas filas son el hallazgo.** Un catálogo de extorsión en el que **ninguna**
entrada declara volumen ni importe no permite ninguna afirmación sobre el tamaño del
daño. Y el 71 % que no llega ni a captura de pantalla no permite afirmar que el conjunto
de datos exista: es exactamente la advertencia que el **aviso oficial del FBI** hace al
público —que los actores *«pueden afirmar falsamente tener información sensible o
comprometedora […] que con frecuencia no existe»*— y que el propio actor, en su
comunicado, califica de alegación falsa. **La cobertura de campos del catálogo da la razón
al aviso, y no hace falta creer a ninguna de las dos partes para verlo.**

### O-2.2 Dos entradas que no son víctimas, y por qué importa el detalle

Dos de las 161 entradas son **comunicados del adversario** colocados en el catálogo con
formato de víctima: uno del 22-09-2026, dirigido nominalmente a dos cargos del FBI, y su
seguimiento del 24-09-2026. El agregador los indexa como entradas porque su recolector lee
el sitio y cada publicación es una fila.

La consecuencia es doble. **Para el recuento**, que el total bruto sobreestima en al menos
dos —y «al menos» porque hay además una entrada cuyo nombre aparece parcialmente
enmascarado, que es una reclamación en curso y no una víctima publicada—. **Para el
análisis**, que esas dos filas son **fuente primaria del adversario** y valen más que
cualquier víctima del catálogo: es el actor explicando por escrito su propio móvil
(§O-4).

### O-2.3 Las dos fuentes discrepan en un tercio

El mismo actor, el mismo día, en los dos agregadores que esta cartera usa:
**161 entradas** en uno y **109** en el otro. Una diferencia de 52 entradas, el **32,3 %**
del mayor. No es contradicción de nadie: son recolectores con cadencias, históricos y
criterios de deduplicación distintos. Es la razón por la que **ninguna cifra de volumen de
este informe se cita sin decir de qué fuente sale y en qué fecha se midió**, y es el
mismo defecto que `CTI-2026-056`, `060` y `061` documentaron en otros catálogos.

**Y hay una tercera cifra, que es la que de verdad engaña.** El recolector diario de esta
cartera consulta el **conjunto anual** de la primera fuente y para este actor obtiene
**110**. Medido el 24-11-2026, eso **no es un tercer recuento del catálogo**: es el
subconjunto de entradas **descubiertas en 2026**. Se demuestra con dos entradas que ese
conjunto incluye y cuya **fecha de ataque declarada es de 2023 y de 2024**, de modo que el
año del endpoint se calcula sobre la fecha de publicación y no sobre la del ataque.

**La trampa está en el parecido.** `110` del conjunto anual de una fuente y `109` del
histórico completo de la otra son dos cifras casi idénticas que miden cosas distintas, y
quien ponga una al lado de la otra concluirá que **dos fuentes independientes se
corroboran**. No se corroboran: una cuenta un año y la otra cuenta todo. Es corroboración
circular con otro disfraz, el mismo que `N6` de la compuerta de enriquecimiento vigila en
los indicadores.

**Y una discrepancia interna de la misma fuente, que conviene conocer antes de fiarse del
delta diario.** Filtrando el histórico del grupo por fecha de descubrimiento en 2026 salen
**116** entradas; el conjunto anual trae **110**. Las **seis** que faltan están en el
histórico y no en el conjunto anual —cinco de enero y una de abril de 2026, todas con
nombre de organización reconocible—, y en el sentido contrario no falta ninguna: el
conjunto anual es un **subconjunto estricto** del histórico del grupo. La consecuencia
operativa es concreta y afecta a cualquiera que vigile con el endpoint anual: **esas seis
entradas no aparecerán nunca como víctimas nuevas en ningún parte diario**, porque no
están en el conjunto que el parte compara. Se consigna como `G-8`.

### O-2.4 El reparto sectorial, con su salvedad

Tecnología 35, comercio y venta en línea 27, servicios financieros 22, servicios
profesionales 15, educación 15, salud 14, transporte 7, hostelería 6, manufactura 5,
administración y defensa 3, alimentación 3. **La salvedad es que el sector lo asigna el
agregador, no la víctima**, y que la lista de objetivos de señuelo que ReversingLabs
publica incluye sectores que el catálogo apenas tiene —medios, videojuegos, un bufete—,
lo que indica que **el catálogo refleja quién acabó publicado, no quién fue atacado**.

## O-3. La infraestructura, medida

### O-3.1 El sitio caído sigue alojado donde estaba

Las cuatro direcciones que los agregadores asocian al sitio de filtración se reparten en
dos alojadores, los dos rusos: **`PROSPERO OOO`, `AS200593`** —tres direcciones en
`91.202.233.0/24` y `91.215.85.0/24`— y **`Proton66 OOO`, `AS198953`**, una dirección en
`176.120.22.0/24`. Medición propia del 24-11-2026 contra RDAP y RIPEstat: los dos prefijos
**siguen anunciados por esos mismos sistemas autónomos**, vistos respectivamente por
**313 y 311 de 322** pares RIS, con última observación de **hoy a las 08:00 UTC**. El
`/24` de Proton66 aparece por primera vez en enero de 2026; el de Prospero viene de 2015,
con otro origen.

**La lectura operativa es la de `CTI-2026-040`:** lo que cae es la marca y el servicio
oculto; **el bloque del alojador sobrevive**, y es el objeto que conviene vigilar.

### O-3.2 Un dato de tercero que matiza la narrativa del cese, y su salvedad

El segundo agregador marca las **cinco direcciones de servicio oculto** del expediente
como **no disponibles**, con últimos sondeos repartidos entre abril y octubre de 2026,
y marca en cambio las **cuatro direcciones IP** como **disponibles**, con sondeos del
**23 y 24 de noviembre de 2026**, uno de ellos de las 16:24 UTC de hoy.

**Hay que leerlo con cuidado y no concluir más de lo que dice.** Que una dirección
responda a un sondeo no significa que sirva el sitio de filtración: puede ser el mismo
alojador sirviendo otra cosa, o un servicio cualquiera en el puerto que el recolector
prueba. **Esta célula no ha sondeado esas direcciones** y no va a hacerlo. Lo que el dato
sostiene es modesto y suficiente: **la infraestructura de red no se ha retirado**, aunque
los servicios ocultos no respondan. Queda como `G-4`.

### O-3.3 El dominio público del grupo está retirado por el registro nacional

`shinyhunte.rs` —el dominio que el propio grupo designó en marzo de 2026 para publicar su
clave sustituta— **no tiene delegación DNS** al 24-11-2026, y el registro de Serbia lo
declara en estado **`Inactive`** y **`serverHold`**, con prohibiciones de actualización,
transferencia y borrado impuestas por el servidor. Es decir: **retirado por el registro, no
abandonado por el titular**. Esto tiene una consecuencia directa sobre `KJ-1` y es la
razón por la que la cadena de claves hubo que reconstruirla desde una copia archivada
(§X-1).

## O-4. El comunicado contra el FBI, comparado con el documento original

### O-4.1 Las tres citas son textuales; el tipo de documento no

El comunicado del 22-09-2026 reprocha al FBI un documento del segundo trimestre de 2026 y
cita de él tres frases. Descargamos el documento oficial y comparamos:

| Lo que el actor cita | Está en el documento oficial | Observación |
|---|---|---|
| *«Threat actors often use their real or exaggerated claims of access to sensitive or personal information to prompt payment from victims»* | **Sí, literal** | — |
| *«To exert pressure on victims[1], SH actors commonly use harassment strategies, sending threatening text messages and phone calls to victims and their family members, and in some cases, swatting»* | **Sí, literal** | Arrastró incluso **el marcador de nota al pie `[1]`**, lo que indica copia desde la versión web |
| *«Threat actors may falsely claim to ha[ve sensitive or compromising information]»* | **Sí, literal** | — |

**Pero el documento no es lo que el actor dice que es.** Lo llama *«FLASH report»* y
*«2026 Quarter 2 FLASH report»*; el documento es un **Public Service Announcement del
IC3**, identificado **`I-051526-PSA`** y fechado el **15-05-2026** —que sí cae en el
segundo trimestre—, y su asunto no es el grupo: es **advertir al público del posible
impacto de un ataque a una plataforma educativa de gestión del aprendizaje**, con
recomendaciones dirigidas a estudiantes y centros. Las tres frases que el actor califica
de «alegaciones falsas» son **advertencias genéricas al público sobre tácticas de
presión**, no imputaciones sobre un incidente concreto.

**Y una nota de honestidad sobre el propio documento del FBI:** su nota al pie número 1
aclara que el uso de la palabra «víctima» **no implica** que quien la recibe cumpla la
definición legal de víctima ni que haya sido identificada como tal en una investigación.
Es la misma cautela que esta cartera aplica en sus propios anexos, y conviene señalar que
la fuente oficial la aplica también.

### O-4.2 Lo que el actor dijo querer, y por qué eso es el dato

El comunicado pide **la retirada o corrección del aviso en el plazo de una semana**, y el
seguimiento del 24-09 insiste: *«no estamos extorsionando a la entidad en cuestión, esto
NO tiene motivación financiera y NO es un rescate»*. **El móvil declarado es
reputacional.** Para una organización, el dato aprovechable es que este ecosistema trata
el relato público como objetivo operativo, lo que convierte la comunicación de crisis en
parte de la superficie de ataque y refuerza la decisión §E-3 `E-e`.

Sobre la vía de entrada reivindicada —día cero en el portal de empleo— la medición dice
otra cosa: **`CVE-2026-35273`**, el identificador que la cobertura secundaria asigna,
consta en el NVD **publicado el 11-06-2026**, con **CVSS 9.8** y estado *Analyzed*, y
afecta a PeopleSoft Enterprise PeopleTools **8.61 y 8.62** permitiendo la toma de control
**sin autenticación previa**. Si el identificador es correcto, en septiembre no había día
cero: había **un parche crítico de tres meses sin aplicar en un tercero**, que es el patrón
de `CTI-2026-063`. La confianza es **moderada** porque el identificador no lo aporta la
fuente primaria; lo que **sí** es medición propia es la fecha y la puntuación del CVE.

## O-5. Hipótesis sobre quién publicó el 23 de noviembre

| Hipótesis | A favor | En contra | Valoración |
|---|---|---|---|
| **H1 · Operadores remanentes del grupo original** | Poseen las privadas de 2020; conocen la historia interna y los detalles de los detenidos | **No usan la clave que ellos mismos declararon vigente en marzo**, que es gratis y zanjaría la duda | **Posibilidad real** *(45–55 %)* |
| **H2 · Antiguos allegados con acceso a las claves de 2020** | Las claves de 2020 **circularon entre varias personas**, según la fuente que las verificó; la de 2020 es la única prueba que presentan | No explica el conocimiento de detalle sobre los detenidos, que también podría ser público | **Posibilidad real** *(45–55 %)* |
| **H3 · Suplantación oportunista sin relación previa** | El nombre tiene valor de mercado y el escaparate quedó libre | **Las firmas son criptográficamente válidas**: quien firmó tenía las privadas. Esto no es gratis | **Improbable** *(20–45 %)* |
| **H4 · Operación de desinformación de un tercero hostil al grupo** | Coherente con la mención a antiguos miembros y con el móvil reputacional | Ninguna evidencia positiva; requiere también las privadas | **Remota** *(5–15 %)* |

**Lo que separaría H1 de H2 es observable y está en el falsador de `KJ-1`:** un mensaje
firmado con `F4953411…20978A`. Mientras no aparezca, **la cartera no declara continuidad**
—es la misma cautela de `CTI-2026-045` con el alias de Jackskid y la de `CTI-2026-018` con
el clúster `.report`, donde la atribución a este mismo actor se descartó como hecho—.

---

# NIVEL TÁCTICO

### Para: Ingeniería de detección · Threat hunting · Mesa de ayuda · Horizonte: días

## T-1. Mapa MITRE ATT&CK

<!-- cti:matrix -->

| Táctica | ID | Técnica | Procedimiento observado |
|---|---|---|---|
| Reconocimiento | T1591 | Gather Victim Org Information | El kit se adapta al proveedor de identidad **concreto** del objetivo: la mayoría imita Okta y uno imita NetIQ / OpenText Access Manager, de modo que el operador comprueba el inquilino **antes** de llamar |
| Reconocimiento | T1598.004 | Phishing for Information: Spearphishing Voice | Llamada en la que quien llama se hace pasar por personal de soporte y empuja a un restablecimiento urgente de contraseña |
| Desarrollo de recursos | T1583.001 | Acquire Infrastructure: Domains | **Dos procedimientos distintos, en una sola fila porque ATT&CK no los separa.** *Denominación y registro:* patrones `legal-<objetivo>[.]com`, `legaldept-<objetivo>[.]com`, `<objetivo>[.]legal`, `<objetivo>-legal[.]com`; registro en **NICENIC** sobre todo, y también Spaceship, NameSilo y Tucows, y **medición propia añade Dynadot** (§X-2). *Configuración:* **ausencia deliberada de MX, DKIM y DMARC** —el dominio sólo sirve web porque el engaño llega por teléfono—, verificada por medición propia en 13 de 13 dominios |
| Desarrollo de recursos | T1586.002 | Compromise Accounts: Email Accounts | Cuenta de contacto en `onionmail[.]org` declarada en el identificador de usuario de la clave presentada el 23-11-2026 |
| Acceso inicial | T1566.004 | Phishing: Spearphishing Voice | Vector principal del clúster: voz, no correo |
| Acceso inicial | T1078.004 | Valid Accounts: Cloud Accounts | Acceso autenticado a aplicaciones SaaS con la credencial de inicio de sesión único de la víctima |
| Acceso inicial | T1190 | Exploit Public-Facing Application | Vía reivindicada en septiembre de 2026 contra un portal PeopleSoft; `CVE-2026-35273`, CVSS 9.8, **publicado tres meses antes** (`KJ-5`) |
| Acceso a credenciales | T1111 | Multi-Factor Authentication Interception | El kit intercepta el flujo: recoge usuario y contraseña y a continuación solicita los factores |
| Acceso a credenciales | T1621 | Multi-Factor Authentication Request Generation | El operador, al teléfono, induce a aprobar la notificación o a dictar el código de un solo uso |
| Sigilo | T1684.001 | Masquerading: Impersonation | Suplantación de personal de soporte en la llamada, y del portal de identidad en la página |
| Mando y control | T1665 | Hide Infrastructure | Sitios de suplantación servidos **detrás de Cloudflare**, cuyos retos impidieron a la propia Okta analizar el kit; filtrado de visitantes y reenvío del tráfico no deseado al portal legítimo de la víctima |
| Movimiento lateral | T1550.001 | Use Alternate Authentication Material: Application Access Token | Patrón histórico del ecosistema: abuso de tokens de integración de terceros sobre el CRM de la víctima; sostiene la decisión §E-3 `E-c` |
| Recolección | T1213.002 | Data from Information Repositories: Sharepoint | Extracción desde repositorios documentales alcanzables con la sesión obtenida |
| Recolección | T1213.005 | Data from Information Repositories: Messaging Applications | Extracción desde mensajería corporativa |
| Recolección | T1530 | Data from Cloud Storage | Extracción desde almacenamiento en la nube del inquilino |
| Exfiltración | T1567.002 | Exfiltration Over Web Service: Exfiltration to Cloud Storage | Los operadores anuncian una red de distribución propia para alojar los datos robados |
| Impacto | T1657 | Financial Theft | Extorsión bajo amenaza de publicación, sin cifrado; `ShinySp1d3r` añadiría `T1486` **si llegara a usarse**, lo que a 24-11-2026 no consta |

**Nota de versión.** Alineado a **ATT&CK v20.1**. `T1656` *Impersonation* está **revocada**
y aquí se usa su sustituta **`T1684.001`**; *Defense Evasion* se denomina **Sigilo** en
esta versión.

## T-2. Hipótesis de caza, y las cuatro consultas que responden «¿nos han llamado?»

**Las cuatro se ejecutan sobre registros que la organización ya tiene**, y ninguna necesita
una herramienta nueva.

1. **Dominios con nuestra marca y término jurídico.** Buscar en registros de DNS, proxy y
   transparencia de certificados, desde el **21-10-2026**, cualquier resolución o
   certificado para `legal-<nuestra marca>`, `<nuestra marca>-legal`, `legaldept-<nuestra
   marca>`, `law-<nuestra marca>` y `<nuestra marca>.legal`. **Es la consulta más barata y
   la que da aviso previo**: la infraestructura se registra entre 1 y 28 días antes de la
   publicación.
2. **Referente de origen cruzado en el inicio de sesión único.** Autenticaciones correctas
   cuyo referente no sea nuestro dominio ni el del proveedor de identidad. Un inicio de
   sesión legítimo no llega desde un dominio de terceros recién registrado.
3. **Restablecimientos de credencial o de segundo factor seguidos de acceso inmediato.**
   Secuencia: restablecimiento → inscripción de un factor nuevo → acceso a SaaS con datos
   de clientes, todo en menos de una hora. **Es la firma de esta cadena**, y la
   contramedida de proceso es la decisión §E-3 `E-b`.
4. **Inscripción de dispositivo o de factor desde red no habitual.** Combinar con
   geolocalización y tipo de dirección; en esta campaña el operador necesita inscribir algo
   para conservar el acceso.

**Y una hipótesis de caza negativa, que es la que evita gastar en el sitio equivocado:**
no buscar muestras en los extremos. **En esta cadena no hay binario.** Quien dedique la
caza al extremo no encontrará nada y concluirá que no le afecta.

## T-3. Lo que NO hay que hacer con este expediente

- **No bloquear las direcciones de Cloudflare.** Las dos a las que resuelve el foro
  asociado al actor son de Cloudflare; bloquearlas corta a terceros y posiblemente a
  nosotros. Van al `Anexo A` con tipo `artefacto`. Es el mismo fallo que `CTI-2026-063`
  documentó con el aviso de Microsoft y `CTI-2026-044` con `AA26-293A`.
- **No bloquear direcciones de servicio oculto.** Un `.onion` no se resuelve por DNS: la
  entrada en una lista de bloqueo no produce ningún efecto. Sirven para correlacionar
  reclamaciones y para detectar uso de Tor desde la red propia.
- **No ingerir la dirección de ShinySp1d3r del agregador.** Es un marcador de posición
  (§O-1.3).
- **No citar un recuento de víctimas de este actor sin fuente y fecha.** Las dos fuentes
  discrepan en un 32,3 % (§O-2.3).
- **No atribuir un incidente nuevo «a ShinyHunters» en comunicación pública.** `KJ-2`.

---

# NIVEL TÉCNICO

### Para: Ingeniería de detección · TIP/SIEM · Analistas de infraestructura · Vida útil: la medición es del 24-11-2026

## X-1. La cadena de claves, medida paso a paso

Todo lo de esta sección es **medición propia del 24-11-2026**, reproducible con los
comandos del `Anexo F`. El procedimiento generalizado está en el `Anexo D`.

**Paso 1 · Las dos claves presentadas como prueba existen y están revocadas.**
Descargadas de `keys.openpgp.org` por huella y analizadas con `gpg --list-packets`:

| Huella | Creada | Paquete de revocación | Razón declarada |
|---|---|---|---|
| `1FC4D0B1DEE914BB05B57FABF1F1B98A51C989B3` | **2020-08-25** | Firma `sigclass 0x20` de **2026-03-17** | `0x01` — **clave sustituida** |
| `828537C15F43F135A8317153CD16A1660CC7CE51` | **2020-01-28** | Firma `sigclass 0x20` de **2026-03-17** | `0x01` — **clave sustituida** |

`sigclass 0x20` es, en OpenPGP, la revocación de la clave primaria, y va **firmada por la
propia clave**: no la puede emitir un tercero. Es decir, **las revocó su titular**.

**Paso 2 · La razón de revocación trae un puntero, y el puntero funciona a medias.** El
subpaquete 29 de las dos revocaciones contiene el mismo texto: *«New key can be found at
this location https://shinyhunte.rs/newpgp or https://web.archive.org/…/pastebin.com/raw/…»*.
**La primera vía está muerta** —`shinyhunte.rs` sin delegación DNS y en `serverHold` en el
registro serbio, §O-3.3—. **La segunda funciona**: la copia archivada del 16-03-2026 a las
23:55 UTC contiene un bloque de clave pública.

**Paso 3 · La clave archivada es la sustituta, y no está revocada.** Importada, su huella
es **`F4953411767DE71BEDCDABCB76F4E26F7A20978A`**, RSA de 4096 bits, creada el
**2026-03-16**, identificador de usuario `ShinyHunters`, **sin paquete de revocación**.
Coincide con la clave que la cobertura de marzo describió como sustituta. **Esta es, por
declaración de su propio titular, la clave vigente.**

**Paso 4 · La clave presentada el 23-11-2026 es nueva, y de después de las detenciones.**
**`27DA9D5B183247CADFC322880ABC63E30F73822E`**, Ed25519, creada el **2026-10-31**,
identificador `ShinyHunters <shcorp@onionmail[.]org>`. Dos semanas y media antes de
aparecer el sitio; **seis semanas después** de las detenciones de septiembre.

**Paso 5 · La clave nueva no lleva aval criptográfico de ninguna de las anteriores en los
servidores públicos.** Consultados dos: en `keys.openpgp.org` sólo trae su autofirma, y
ahí **no prueba nada** porque ese servidor **no distribuye certificaciones de terceros por
política**; pero en **`keyserver.ubuntu.com`, que sí las distribuye**, tampoco aparece
ninguna. El aval que la respalda es **textual** —el anuncio dice que las claves viejas
autentican la nueva—, no una firma cruzada publicada.

**Paso 6 · La omisión, que es el hallazgo.** Los mensajes de noviembre se firmaron con las
**dos claves revocadas** y, según la fuente que los verificó, **ninguno con
`F4953411…20978A`**. Cualquier implementación conforme de OpenPGP marca una firma hecha
con una clave revocada como **no válida para autenticar**: la revocación es precisamente la
declaración del titular de que esa clave ya no le representa. Y aquí la razón declarada no
es compromiso, es sustitución, de modo que el titular dejó dicho **cuál** le representa.

**Por qué la omisión es el dato y no un detalle.** Firmar con la clave vigente **no cuesta
nada** a quien la tenga, y resuelve la duda por completo. Que se recurra a dos claves
retiradas ocho meses antes, de las que la propia fuente dice que **circularon entre varias
personas**, admite dos explicaciones: que no se disponga de la vigente, o que se prefiera
el valor simbólico de las de 2020. La primera es más económica y tiene una consecuencia
operativa: **quien volvió no es quien operaba el sitio en marzo**. De ahí `KJ-1`, con su
probabilidad y no como certeza.

## X-2. Medición de la infraestructura de señuelo

Trece dominios del conjunto publicado, medidos el 24-11-2026 con `dig` y `whois`:

<!-- cti:table highlight="Hallazgo" -->

| Qué se midió | Resultado | Hallazgo |
|---|---|---|
| Registros MX | **0 de 13** | Corrobora de forma independiente la afirmación de ReversingLabs: el dominio **no puede recibir correo** |
| `_dmarc` y TXT | **0 de 13** | Igual. No hay intención de enviar correo desde ellos |
| Registro A | **2 de 13** resuelven | La campaña del 16-11 ya está en gran parte retirada ocho días después |
| Servidores de nombres | 2 de 13 con `ns3`/`ns4.my-ndns[.]com` | Son los servidores **por omisión de NICENIC** —dominio registrado en el propio NICENIC en 2022—: confirma registrador y confirma que están **aparcados de vuelta** |
| Estado del registro | `legal-anthropic[.]com` en **`clientHold`** | **Suspendido por el registrador**, no sólo sin DNS |
| Fechas y hora de registro | `legal-anthropic[.]com` **2026-11-15 19:20 UTC**; `legal-mcdonalds[.]com` **2026-11-17 19:17 UTC** | Corrobora la **ventana vespertina UTC** que describen las dos fuentes |
| Registrador | `legal-autozone[.]com` en **DYNADOT**, creado 2026-11-16 | **Quinto registrador, no mencionado por la fuente.** Amplía el conjunto a vigilar |
| Dirección de ese dominio | `137.131.40.164` → **Oracle Corporation** | **Divergencia:** la fuente describe el conjunto fronteado por Cloudflare. Lo más económico es un aparcamiento posterior a la fase activa; **no se concluye más** |
| Campo de registrante | Redactado o vacío en 3 de 3 consultados | **No podemos corroborar** el perfil «Chile» de la fuente (`KJ-6`, `G-3`) |

**Y la medición de la infraestructura del sitio de filtración**, con RDAP y RIPEstat:

| Prefijo | Origen | Titular | Visibilidad RIS | Primera observación | Última |
|---|---|---|---|---|---|
| `91.202.233.0/24` | `AS200593` | PROSPERO OOO, RU | **313 / 322** | 2015-04-30, con otro origen | **2026-11-24 08:00 UTC** |
| `91.215.85.0/24` | `AS200593` | PROSPERO OOO, RU | — | — | activo |
| `176.120.22.0/24` | `AS198953` | Proton66 OOO, RU | **311 / 322** | 2026-01-14 | **2026-11-24 08:00 UTC** |

## X-3. Detección y mitigación, en orden de efecto

```
# 1 · Dominios con nuestra marca más término jurídico (el aviso previo)
#     Fuentes: transparencia de certificados, registros de DNS recursivo, proxy.
#     Patrones: legal-<marca>.com | <marca>-legal.com | legaldept-<marca>.com
#               law-<marca>.com   | <marca>.legal
#     Ventana: desde 2026-10-21. Ojo: el tema cambia cada 4-6 semanas,
#     así que el patrón «legal» caduca; lo estable es «nuestra marca
#     en un dominio que no es nuestro».

# 2 · Autenticación correcta con referente de origen cruzado
#     Registro del proveedor de identidad: éxito de inicio de sesión
#     cuyo referente no sea nuestro dominio ni el del proveedor.

# 3 · La secuencia de la mesa de ayuda (la firma de esta cadena)
#     restablecimiento de contraseña
#       -> inscripción de factor nuevo
#         -> acceso a SaaS con datos de clientes
#     en una ventana de 60 minutos, para la misma identidad.

# 4 · Inscripción de factor o dispositivo desde red no habitual
#     Correlacionar con tipo de dirección: proxy anonimizador,
#     red residencial de un país donde no tenemos personal.

# 5 · Lo que NO sirve, dicho para que nadie lo intente
#     - Buscar hashes de muestra: no hay binario en esta cadena.
#     - Bloquear direcciones de Cloudflare del Anexo A: corta a terceros.
#     - Bloquear .onion: no se resuelve por DNS, no produce efecto.
```

**Mitigaciones, por efecto decreciente:**

1. **Autenticación resistente a suplantación** —FIDO2, passkeys, autenticadores ligados al
   origen— en acceso administrativo y a SaaS con datos de clientes. Es el único control que
   la fuente primaria declara **efectivo contra el kit**.
2. **Prohibición de restablecer credencial o factor desde llamada entrante**, con
   verificación por canal alternativo. Cambio de proceso, coste cero en licencias.
3. **Restricción de acceso a dispositivo gestionado** para las aplicaciones sensibles.
4. **Alerta obligatoria al titular** ante cualquier cambio de factor, por canal
   independiente.
5. **Revisión de aplicaciones conectadas con token de larga vida** (§E-3 `E-c`): un token ya
   está autenticado y la autenticación fuerte no lo detiene.
6. **Parcheo de aplicaciones expuestas en terceros con acuerdo de plazo verificable**, que
   es la lección de `KJ-5` y de `CTI-2026-063`.

---

## 14. Brechas de inteligencia y requisitos de colección

| Id | Brecha | Efecto en los juicios | Cómo se cerraría | Prioridad |
|---|---|---|---|---|
| `G-1` | No tenemos los dos mensajes firmados del 23-11-2026: viven en un servicio oculto al que esta célula no accede | `KJ-1` depende de la verificación declarada por un tercero (§3.3) | Obtención de los mensajes por una fuente con acceso, o publicación del texto firmado por cualquier proveedor | **Alta** |
| `G-2` | No hay muestra pública del kit de suplantación; los retos de Cloudflare impidieron a la propia Okta analizarlo | Sin lógica de detección de contenido; §T-2 sólo propone caza por comportamiento | Una muestra o una captura del flujo por parte de una víctima | **Alta** |
| `G-3` | El perfil de registrante «Chile» no es corroborable: el WHOIS público viene redactado | `KJ-6` queda en confianza baja | Acceso a WHOIS histórico o no redactado del conjunto NICENIC | Media |
| `G-4` | No sabemos qué sirven hoy las cuatro direcciones del alojador que un tercero marca como disponibles | §O-3.2 no puede ir más allá de «la red no se ha retirado» | Sondeo autorizado, o telemetría de un tercero que declare qué puerto y qué servicio | Media |
| `G-5` | El expediente de ShinySp1d3r en el agregador contiene una dirección que es un marcador de posición | No afecta a ningún juicio; afecta a cualquiera que ingiera la fuente | Aviso al agregador y comprobación de si hay más expedientes con el mismo defecto | Media |
| `G-6` | No tenemos telemetría propia de identidad: no sabemos si esta campaña nos ha llamado | §3.4; la afirmación «no nos afecta» no tiene base | Ejecución de las cuatro consultas de §T-2 | **Alta** |
| `G-7` | El identificador `CVE-2026-35273` lo asigna cobertura secundaria, no la fuente primaria | `KJ-5` queda en confianza moderada | Confirmación oficial del vector, o del propio proveedor del portal afectado | Media |
| `G-8` | El conjunto anual de la primera fuente es un **subconjunto estricto** de su propio histórico de grupo: 110 frente a 116 para 2026, y faltan seis entradas | Ninguna cifra de este informe depende de ello, porque todas salen del histórico. **Afecta al recolector diario de la cartera**, que consulta el conjunto anual | Reproducir la comparación para otros actores y, si el defecto es general, consultar el histórico por grupo en lugar del conjunto anual | **Alta** para el utillaje, baja para este informe |

**Disparadores de reevaluación.** Cada uno, si se cumple, obliga a abrir versión:

| Id | Disparador | Qué movería |
|---|---|---|
| `I-1` | Aparece un mensaje firmado con `F4953411…20978A` | **Invierte `KJ-1`**: acreditaría continuidad del operador |
| `I-2` | Una organización nombrada en INCEPTION o en el sitio nuevo **confirma** la brecha | Daría numerador a las reclamaciones; movería `KJ-4` |
| `I-3` | `ShinySp1d3r` publica una primera víctima verificable | Cambia el perfil de impacto de §E-1 y añade `T1486` a §T-1 |
| `I-4` | Okta o ReversingLabs atribuyen con confianza alta la operación del sitio INCEPTION | Movería `KJ-2` y la tabla de §3.5 |
| `I-5` | Aparece una campaña de señuelos con **tema distinto** del jurídico | Caduca el patrón de §X-3 punto 1; hay que reescribirlo |
| `I-6` | Los prefijos de PROSPERO o Proton66 dejan de anunciarse, o el sitio reaparece en otro alojador | Movería `KJ-7` y el objeto a vigilar |
| `I-7` | Una víctima chilena o latinoamericana aparece en cualquiera de los tres sitios | Reabre §E-4 por completo |

---

# ANEXOS

## Anexo A — Indicadores de compromiso

### A.1 — Una decisión de publicación que conviene explicar

Este anexo publica **dominios que contienen marcas de terceros** y **no publica los
nombres de las organizaciones reivindicadas** en ningún sitio de filtración. La asimetría
es deliberada y éstas son las razones:

- Un **dominio de señuelo** es infraestructura del adversario. Prueba un **intento** —el
  registro existe, está medido y lo publican dos proveedores con nombre—, y su publicación
  tiene valor defensivo inmediato: un equipo puede bloquearlo hoy. No afirma que la
  organización haya sido comprometida.
- Una **entrada en un sitio de filtración** es una reclamación del adversario. En este
  expediente, **el 71 % no llega ni a captura de pantalla** y **ninguna** declara volumen
  ni importe. Reproducir el nombre amplifica la reclamación y hace el trabajo de presión
  del adversario, que es exactamente lo que el aviso oficial del FBI recomienda no hacer.
- Para quien necesite comprobar **su propio** caso, el `Anexo F` da el procedimiento
  completo. Es la misma solución que `CTI-2026-062` adoptó con las víctimas chilenas de
  otro catálogo.

**Vida útil.** Los dominios de esta campaña **se queman en días**: la medición del
24-11-2026 encontró que **11 de 13 ya no resuelven** y uno está suspendido por su
registrador. Lo que dura es el **patrón** y los **prefijos** del alojador, no la lista.

### A.2 — Dominios de señuelo del clúster de intrusión

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Acción |
|---|---|---|---|---|
| pattern | `legal-<objetivo>[.]com` · `legaldept-<objetivo>[.]com` · `<objetivo>[.]legal` · `<objetivo>-legal[.]com` · `law-<objetivo>[.]com` | **Patrones de denominación del clúster a noviembre de 2026.** Valen más que la lista: el tema cambia cada 4–6 semanas y el patrón estable es «marca ajena en dominio que no es suyo» | Alta | Caza y bloqueo preventivo con la marca propia |
| domain | `legal-duolingo[.]com` · `legal-morningstar[.]com` · `legal-westernunion[.]com` · `legal-ea[.]com` · `legal-dropbox[.]com` · `legal-riotgames[.]com` · `legal-indeed[.]com` · `legal-creditkarma[.]com` · `legal-vrtx[.]com` · `legal-aexp[.]com` | Conjunto **confirmado** por ReversingLabs con comportamiento de kit de suplantación de inicio de sesión único | Alta | Bloqueo |
| domain | `legal-expeditors[.]com` · `legal-twitch[.]tv` · `legal-lvmh[.]com` · `legal-amd[.]com` · `legal-carvana[.]com` · `legal-pepsico[.]com` · `legal-caesars[.]com` · `legal-rbi[.]com` · `legal-grubhub[.]com` · `legal-lucidmotors[.]com` · `activisionblizzard-legal[.]com` | Conjunto **confirmado**, continuación. `legal-lucidmotors[.]com` es el que imita **NetIQ / OpenText**, no Okta | Alta | Bloqueo |
| domain | `legal-cigna[.]com` · `legal-paychex[.]com` · `legal-henryschein[.]com` · `henryschein-legal[.]com` · `law-henryschein[.]com` · `legal-lucid[.]com` · `legal-autozone[.]com` | Dominios asociados a organizaciones que el sitio nombró. **Tres variantes de un mismo objetivo registradas en registradores distintos en trece minutos y al día siguiente**: indicio de una sola mano | Alta | Bloqueo |
| domain | `legal-anthropic[.]com` · `legal-openai[.]com` · `legal-tesla[.]com` · `legal-netflix[.]com` · `legal-adobe[.]com` · `legal-nestle[.]com` · `legal-delta[.]com` · `legal-kfc[.]com` · `legal-starbucks[.]com` · `legal-mcdonalds[.]com` · `mcdonalds-legal[.]com` | **Alta confianza**, sin prueba directa de kit: coinciden en denominación, registrador, ventana horaria y servidores de nombres. **Medición propia: `legal-anthropic[.]com` registrado 2026-11-15 19:20 UTC, hoy en `clientHold`** | Moderada–alta | Bloqueo |
| domain | `legal-nintendo[.]com` · `nintendo-legal[.]com` · `legal-paramount[.]com` · `paramount[.]legal` · `legal-warnerbros[.]com` · `warnerbros-legal[.]com` · `legal-wernerbros[.]com` · `legal-nbcuniversal[.]com` · `legal-ubisoft[.]com` · `legal-epicgames[.]com` · `legal-reddit[.]com` · `reddit-legal[.]com` | **Alta confianza**, continuación. `legal-wernerbros[.]com` conserva el error ortográfico del registrante, que es útil como huella | Moderada–alta | Bloqueo |
| domain | `legal-alaskaair[.]com` · `legal-jcpenney[.]com` · `legal-mtb[.]com` · `legal-molinahealthcare[.]com` · `legal-verisk[.]com` · `verisk-legal[.]com` · `verisk-law[.]com` · `legal-colpipe[.]com` · `legal-ssctech[.]com` · `legal-ulta[.]com` · `legal-nfl[.]com` · `legal-arthrex[.]com` · `legal-ml[.]com` · `legal-jonesday[.]com` · `legal-iheartmedia[.]com` · `iheartmedia-legal[.]com` · `legal-wynnresorts[.]com` · `wynnresorts[.]legal` · `legal-everpuredata[.]com` | **Alta y media confianza.** Ninguna de estas organizaciones figura en ningún sitio de filtración: son objetivos **preparados**, no víctimas | Moderada | Bloqueo |
| pattern | `ns3[.]my-ndns[.]com` · `ns4[.]my-ndns[.]com` | **Servidores de nombres por omisión de NICENIC.** Medición propia: dos de los trece dominios medidos han vuelto a ellos, señal de dominio **aparcado tras la fase activa**. No es infraestructura de ataque: es huella de registrador | Alta | Caza y correlación de registrador |
| artefacto | `137.131.40.164` | **Oracle Corporation.** Dirección a la que resuelve `legal-autozone[.]com` el 24-11-2026. **Divergencia con la fuente**, que describe el conjunto detrás de Cloudflare; explicación más económica: aparcamiento posterior. **Infraestructura de un proveedor de nube con millones de clientes** | Moderada | **NUNCA bloqueo** |

### A.3 — Infraestructura del sitio de filtración caído

<!-- cti:note type="warn" -->

> ⚠ **Leer antes de usar.** Las dos direcciones del foro asociado son de **Cloudflare** y
> van con tipo `artefacto` y marca **NUNCA bloqueo**: bloquearlas corta a terceros. Las
> cuatro direcciones de los alojadores **sí** son bloqueables —son espacio de un cliente,
> no infraestructura compartida—. Y **ninguna dirección de servicio oculto se bloquea**:
> no se resuelve por DNS y la entrada en una lista no produce efecto.

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Acción |
|---|---|---|---|---|
| ipv4 | `91.202.233.104` | Dirección asociada al sitio de filtración. **PROSPERO OOO, `AS200593`, Rusia** (medición propia RDAP, 24-11-2026) | Alta | Bloqueo |
| ipv4 | `91.215.85.22` · `91.215.85.103` | Ídem, mismo titular y mismo `/24` | Alta | Bloqueo |
| ipv4 | `176.120.22.24` | Ídem. **Proton66 OOO, `AS198953`, Rusia** | Alta | Bloqueo |
| pattern | `91.202.233.0/24` · `91.215.85.0/24` · `176.120.22.0/24` | **Los prefijos son el indicador duradero**, no las direcciones: los tres siguen anunciados por los mismos sistemas autónomos el 24-11-2026, con 313 y 311 de 322 pares RIS viéndolos | Alta | Vigilancia del prefijo y bloqueo selectivo tras verificación |
| asn | `AS200593` · `AS198953` | PROSPERO OOO y Proton66 OOO. **El alojador sobrevive a la marca**: es el objeto a vigilar según `KJ-7` | Alta | Vigilancia de anuncios y de prefijos nuevos |
| artefacto | `172.67.165.58` · `104.21.81.218` | **Cloudflare.** Direcciones a las que resuelve `breachforums[.]hn` el 24-11-2026 (medición propia). Sirven a millones de terceros | Alta | **NUNCA bloqueo** |
| domain | `breachforums[.]hn` | Foro asociado al actor en el inventario de los dos agregadores. Registrado 2024-04-19, registrador 101Domain | Moderada | Bloqueo del nombre; **no de sus direcciones** |
| artefacto | `shinypogk4jjniry5qi7247tznop6mxdrdte2k6pdu5cyo43vdzmrwid[.]onion` | Sitio de filtración principal. **Suma de control validada: `c8d9` coincidente**, luego corresponde a una clave Ed25519 real. Marcado **no disponible** por el segundo agregador, último sondeo 2026-07-17 | Alta | Correlación y detección de uso de Tor; **no bloqueo** |
| artefacto | `espeonsh2drryv4bsonur5ud7d6gooho2mvktqdmakdpoxkwwersinid[.]onion` · `toolatedhs5dtr2pv6h5kdraneak5gs3sxrecqhoufc5e45edior7mqd[.]onion` · `shnyhntww34phqoa6dcgnvps2yu7dlwzmy5lkvejwjdo6z7bmgshzayd[.]onion` | Sitios de respaldo del mismo actor. **Sumas validadas: `2435`, `1fb2`, `7c83`.** Los tres, no disponibles | Alta | Correlación; **no bloqueo** |
| artefacto | `shinyazvxkdfoqmpht7xyqo2xa2vlqzzalkqqmkfq3nsfbinmkukhjad[.]onion` | **Sitio aparecido el 23-11-2026** que reivindica ser el actor. **Suma validada: `a3a4` coincidente.** El segundo agregador lo marca disponible; esta célula **no ha comprobado que esté servido** | Moderada | Correlación; **no bloqueo** |
| artefacto | `incptbug3ziqym4rhgsj7h7hbpzt3v4ympcf42gsdb5haqq237fziaad[.]onion` | **Sitio INCEPTION**, indexado el 17-11-2026. **Suma validada: `9400` coincidente** | Alta | Correlación; **no bloqueo** |
| artefacto | `sh1nysp1d3rxyz123456789abcdefghijklmnopqrstuvwxyz[.]onion` | **NO ES UNA DIRECCIÓN VÁLIDA.** 49 caracteres frente a los 56 de una v3, y cuerpo con el alfabeto en orden: es un **marcador de posición** del agregador. Se consigna para que nadie lo ingiera (`G-5`) | Alta, en cuanto a que es inválida | **NUNCA ingerir como indicador** |
| domain | `shinyhunte[.]rs` | Dominio público del actor, designado por él mismo en marzo de 2026 para publicar su clave. **Medición propia: sin delegación DNS y en `Inactive` / `serverHold` en el registro serbio** | Alta | Bloqueo del nombre; vigilancia de reactivación |

### A.4 — Material criptográfico, que es la prueba del expediente

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Acción |
|---|---|---|---|---|
| artefacto | `1FC4D0B1DEE914BB05B57FABF1F1B98A51C989B3` | Clave PGP del actor creada **2020-08-25**. **REVOCADA por su titular el 2026-03-17**, razón `0x01` «clave sustituida». Usada para firmar el anuncio del 23-11-2026 | Alta, medición propia | Correlación y atribución; **NUNCA bloqueo** |
| artefacto | `828537C15F43F135A8317153CD16A1660CC7CE51` | Clave PGP creada **2020-01-28**. **REVOCADA el 2026-03-17**, misma razón. Usada también el 23-11-2026 | Alta, medición propia | Correlación y atribución; **NUNCA bloqueo** |
| artefacto | `F4953411767DE71BEDCDABCB76F4E26F7A20978A` | **La clave vigente según su propio titular.** RSA 4096, creada 2026-03-16, **sin revocación**. Recuperada de la copia archivada que el certificado de revocación señala. **Su ausencia en las firmas de noviembre es el hallazgo de `KJ-1`** | Alta, medición propia | Correlación; vigilar su aparición en cualquier firma nueva (`I-1`) |
| artefacto | `27DA9D5B183247CADFC322880ABC63E30F73822E` | Clave presentada el 23-11-2026. **Ed25519, creada 2026-10-31** —seis semanas después de las detenciones—. Sin certificación de terceros en los dos servidores consultados | Alta, medición propia | Correlación y atribución; **NUNCA bloqueo** |
| email | `shcorp@onionmail[.]org` | Identificador de usuario de la clave anterior. Único contacto nuevo publicado | Moderada | Detección en correo entrante y en notas de extorsión |
| cve | `CVE-2026-35273` | PeopleSoft Enterprise PeopleTools 8.61 y 8.62; toma de control **sin autenticar**. **CVSS 9.8**, publicada **2026-06-11**, estado *Analyzed* en el NVD (medición propia). Vía reivindicada en septiembre de 2026 | Moderada en la atribución, alta en el dato del CVE | **Parcheo prioritario**, propio y en terceros |

### A.5 — Lo que NO se publica, y por qué

- **Los nombres de las 161 entradas del catálogo** y de las siete de INCEPTION. Son
  reclamaciones sin muestras verificadas (`A.1`).
- **Los nombres de las personas detenidas.** Personas físicas, cargos no probados, y
  ningún juicio depende de su identidad (§3.2).
- **El nombre parcialmente enmascarado** de una entrada del catálogo: es un nombre que el
  adversario ocultó a medias, y completarlo o difundirlo haría permanente lo que él mismo
  no publicó. Regla de la casa desde `CTI-2026-054` §E-3.
- **Los cargos públicos nombrados en el comunicado del adversario** se citan en §O-4 por su
  función institucional, porque la cita es necesaria para fechar y caracterizar el
  comunicado, y porque son cargos públicos actuando como tales.

---

## Anexo B — Fuentes y valoración

| Fuente | Qué aportó | Valoración | Vía |
|---|---|---|---|
| **Okta Threat Intelligence**, «Former ShinyHunters-affiliated cluster O-UNC-053 moves to new INCEPTION leak site» | El clúster, sus patrones de dominio, el intervalo registro→publicación, la evaluación de cambio de marca y el límite del kit | **A-1.** Primaria, leída en original; declara sus límites y distingue lo que no puede valorar con confianza alta | Descarga directa |
| **ReversingLabs**, «Threat Researcher's Notebook: SSO Vishing Campaign Associated with Emerging Inception Extortion Group» | Los tres niveles de confianza de dominios, la ausencia de MX/DKIM/DMARC, los registradores, los pares de servidores de nombres y los perfiles de registrante | **A-1.** Primaria, leída en original; publica su lista completa y separa confirmado de inferido | Descarga directa |
| **IC3 / FBI**, aviso `I-051526-PSA` del 15-05-2026 | El documento que el actor exigió retirar, íntegro, con sus tres frases citadas y su nota al pie sobre el término «víctima» | **Oficial.** Fuente de Estado, leída en original | Descarga directa |
| **NVD**, `CVE-2026-35273` | Fecha de publicación, CVSS 9.8, versiones afectadas y estado | **Oficial.** Consulta a la API | Medición propia |
| **BleepingComputer** (23-11-2026) | Existencia y contenido del sitio del 23-11, y **verificación propia declarada** de las dos firmas PGP contra la clave pública que ya usó en agosto de 2025 | **B-2.** Prensa especializada que declara el método de verificación y sus límites —dice expresamente que las claves circularon y que no prueban identidad— | Descarga directa |
| **Help Net Security** (24-11-2026) | Cobertura del expediente de Okta y de la investigación de ReversingLabs, con citas atribuidas | **B-2.** Secundaria usada como vehículo de citas, no como análisis | Descarga directa |
| **Reuters** (30-09-2026 y 03-10-2026) | Caída del sitio tras el vencimiento del plazo, y la segunda detención | **B-2**, **citada a través del expediente de Okta**: no se accedió al original. La credibilidad se degrada **por la vía**, no por la fuente | Vía terciaria |
| **`ransomware.live`** | Catálogo de 161 entradas con sus campos, inventario de sitios, y el expediente de ShinySp1d3r | **C-2** como fuente, **medición propia** en lo que se midió sobre ella. Con los cuatro defectos ya documentados por esta cartera | API |
| **`cti.fyi`** | Recuento alternativo de 109 entradas, estado de disponibilidad de los sitios y dos sitios que la otra fuente no lista | **C-2**, ídem. Consultada **sin clave**: el expediente de grupo respondió público | API |
| **RIPEstat · RDAP · WHOIS · DNS · servidores de claves OpenPGP** | Todo lo marcado como medición propia | **Medición propia**, reproducible con el `Anexo F` | Directa |
| **Security Boulevard**, «Aftermath of the September ShinyHunters Arrests: Battle Over the Brand Name» | — | **Consultada y NO accesible**: el servidor devolvió `403` a la descarga. **No se cita su contenido**, ni siquiera a través de resúmenes de buscador, porque no pudimos leer el original | No accesible |
| Diversos sitios agregadores de noticias de seguridad | — | **Descartados.** Varios de los resultados de búsqueda sobre este actor son sitios con cifras que no citan fuente y que se contradicen entre sí. **Ninguna cifra de este informe procede de ellos** | Descartada |

**Nota sobre lo que no se corroboró.** Las cifras que circulan sobre este ecosistema
—«más de 400 organizaciones», «más de 140 organizaciones y 70 millones de dólares en
pagos», «mil millones de registros»— **no se reproducen como medidas** en este informe.
Unas son reclamaciones del adversario, otras declaraciones de funcionarios recogidas en
cobertura secundaria, y ninguna viene con base de conteo. Se consignan aquí como
existentes y no verificadas, que es lo que esta cartera hace con lo que no puede medir.

---

## Anexo C — Léxico de probabilidad y confianza

Se usa el léxico ICD 203 ya adoptado por la cartera. **Probabilidad**: remota *(5–15 %)*,
improbable *(20–45 %)*, posibilidad real *(45–55 %)*, probable *(55–80 %)*, muy probable
*(80–95 %)*, casi con certeza *(≥99 %)*. **Confianza**: alta, moderada, baja, según la
calidad y la corroboración de la base, **nunca según lo probable que parezca el hecho**.
Un **hecho medido** no lleva probabilidad: lleva la declaración de que es medición y la
confianza en el método.

---

## Anexo D — Método: cómo evaluar una prueba criptográfica de continuidad de marca

**El problema.** Un actor desaparece y vuelve. Para probar que es el mismo, publica algo
firmado con una clave histórica. ¿Qué acredita eso? La respuesta por defecto —«la firma
verifica, luego es él»— es falsa, y este expediente da el contraejemplo. El método tiene
**seis pasos, cuesta veinte minutos y no necesita acceso al sitio del adversario.**

**1 · Obtener la clave por su huella, no por su nombre.** Un identificador de usuario es
texto libre; la huella es el objeto. Dos servidores como mínimo, y conviene saber por qué:
`keys.openpgp.org` **no distribuye certificaciones de terceros por política**, de modo que
su ausencia ahí no significa nada; `keyserver.ubuntu.com` sí las distribuye, y ahí la
ausencia **sí** es un dato.

**2 · Buscar el paquete de revocación antes que nada.** `gpg --list-packets` y mirar si
hay una firma `sigclass 0x20`. Si la hay, **la clave está muerta por decisión de su
titular** y cualquier firma hecha con ella es, para una implementación conforme, no válida
para autenticar. Esto es lo que casi nadie comprueba.

**3 · Leer la RAZÓN de la revocación, que es donde está la inteligencia.** El subpaquete
29 trae un código y un texto libre. El código distingue dos mundos:
`0x02` **clave comprometida** —el titular avisa de que alguien más la tiene, y entonces
una firma posterior no prueba nada en absoluto— frente a `0x01` **clave sustituida** —el
titular dice cuál le representa ahora—. Y el texto libre suele traer **dónde** está la
sustituta, que es un indicador en sí mismo: aquí dio un dominio propio y una copia
archivada.

**4 · Seguir el puntero y determinar la clave VIGENTE.** Si el puntero está muerto, buscar
la copia archivada: un archivo web con fecha anterior al suceso que se investiga es
**evidencia contemporánea**, y eso es más valioso que cualquier recuerdo de la cobertura.
Importar la clave y comprobar que **no** está revocada.

**5 · Fechar la clave nueva y compararla con los sucesos.** La fecha de creación va en el
paquete de clave pública y no se puede falsear sin invalidar las autofirmas. Una clave
creada **después** del suceso que explica la desaparición es un dato duro.

**6 · Preguntar qué clave NO se usó, que es la pregunta que decide.** La escala:

| Nivel | Qué se presenta | Qué acredita |
|---|---|---|
| **5** | Firma con la clave **vigente** declarada por el titular | Continuidad acreditada, salvo robo de la privada |
| **4** | Firma con la vigente **más** certificación cruzada publicada de la nueva | Ídem, y además transición ordenada |
| **3** | Firma con clave **revocada por sustitución**, pudiendo usar la vigente | **Posesión de una privada retirada. No acredita continuidad** |
| **2** | Firma con clave **revocada por compromiso** | No acredita nada: el titular ya dijo que otros la tienen |
| **1** | Publicación de la clave **pública** sin firmar nada | Nada: una clave pública la tiene cualquiera |
| **0** | Afirmación textual sin material criptográfico | Nada |

**El caso de este informe queda en el nivel 3**, y la razón por la que eso es informativo
—y no simplemente insuficiente— es económica: **usar la clave vigente no cuesta nada a
quien la tenga**. Cuando un adversario elige la prueba más débil pudiendo elegir la más
fuerte, la elección es el dato.

**Los tres errores que este método evita.** **(a)** Tomar «la firma verifica» por
«es el mismo actor»: verifica que alguien tiene una privada, y las privadas se copian,
se heredan y se incautan. **(b)** Tomar la ausencia de firmas cruzadas en un servidor
moderno por prueba de nada o por prueba de todo: depende de la política del servidor, y
hay que saber cuál es. **(c)** Fiarse de la memoria de la cobertura sobre qué clave era la
vigente: el certificado de revocación lo dice, con fecha y firmado.

**Dónde encaja con lo que ya teníamos.** Es el eslabón criptográfico que faltaba a los
tres métodos de marca de esta cartera: `CTI-2026-047` evalúa un rebranding por solapamiento
temporal, `CTI-2026-055` clasifica reclamaciones cruzadas por dirección, y `CTI-2026-058`
decide cese frente a migración midiendo el silencio en unidades de la propia cadencia del
actor. Ninguno de los tres responde «¿es el mismo operador?». Éste lo responde cuando el
adversario comete la cortesía de ofrecer una prueba.

---

## Anexo E — Marcos de referencia empleados

| Marco | Uso en este informe |
|---|---|
| **MITRE ATT&CK v20.1** | §T-1. Tres matrices en el catálogo local; `T1656` revocada sustituida por `T1684.001`; *Defense Evasion* ahora **Sigilo** |
| **ICD 203** | Léxico de probabilidad y confianza en los siete juicios clave (`Anexo C`) |
| **Escala de prueba de `CTI-2026-048`** | §O-2.1, para situar el 29,2 % de entradas con captura de pantalla en el nivel 3, el que más engaña |
| **OpenPGP (RFC 4880 y sucesores)** | §X-1 y `Anexo D`: clases de firma, códigos de razón de revocación y subpaquetes |
| **Validación de dirección de servicio oculto v3** | §O-1.3 y `Anexo A.3`: 56 caracteres base32, 35 bytes, suma `sha3_256` de dos bytes |
| **Admiralty / OTAN** | `Anexo B`, con la convención de la casa de degradar **por la vía** y no por la fuente |
| **TLP 2.0 · PAP** | Marcado de difusión |

---

## Anexo F — Paquete legible por máquina y reproducción de las mediciones

Todo lo marcado como medición propia se reproduce con lo siguiente. **Ninguno de estos
comandos toca infraestructura del adversario**, salvo el que recupera una copia archivada
de una clave pública.

```bash
# ── 1 · La cadena de claves (§X-1) ────────────────────────────────────
for F in 1FC4D0B1DEE914BB05B57FABF1F1B98A51C989B3 \
         828537C15F43F135A8317153CD16A1660CC7CE51 \
         F4953411767DE71BEDCDABCB76F4E26F7A20978A \
         27DA9D5B183247CADFC322880ABC63E30F73822E; do
  curl -s "https://keys.openpgp.org/vks/v1/by-fingerprint/$F" -o "k-$F.asc"
  echo "── $F"; gpg --list-packets "k-$F.asc" | grep -E "created|sigclass|revocation|user ID"
done
# Lo que hay que ver: sigclass 0x20 en las dos primeras, con fecha 2026-03-17
# y subpaquete 29 con razon 0x01. Y el puntero de ese subpaquete.

# Firmas de terceros: hay que preguntar al servidor que las distribuye
curl -s "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x<HUELLA>&options=mr"

# ── 2 · Validacion de una direccion de servicio oculto v3 (§O-1.3) ────
python3 -I - <<'PY'
import base64, hashlib
d = "incptbug3ziqym4rhgsj7h7hbpzt3v4ympcf42gsdb5haqq237fziaad"
assert len(d) == 56, f"longitud {len(d)}: no es una direccion v3"
raw = base64.b32decode(d.upper())
clave, suma, version = raw[:32], raw[32:34], raw[34]
calc = hashlib.sha3_256(b".onion checksum" + clave + bytes([version])).digest()[:2]
print(version, suma.hex(), calc.hex(), "OK" if suma == calc else "NO CUADRA")
PY

# ── 3 · Infraestructura de senuelo (§X-2) ─────────────────────────────
for D in legal-anthropic.com legal-mcdonalds.com legal-autozone.com; do
  echo "── $D"
  dig +short A "$D"; dig +short NS "$D"; dig +short MX "$D"
  dig +short TXT "_dmarc.$D"
  whois "$D" | grep -iE "^(registrar:|creation date|domain status|registrant)"
done

# ── 4 · Titularidad y visibilidad de los prefijos (§X-2) ──────────────
for IP in 91.202.233.104 176.120.22.24; do
  whois "$IP" | grep -iE "^(inetnum|netname|org-name|country|origin)"
  curl -s "https://stat.ripe.net/data/routing-status/data.json?resource=$IP" |
    python3 -I -c 'import json,sys; d=json.load(sys.stdin)["data"]; print(d["origins"], d["visibility"], d["last_seen"])'
done

# ── 5 · El catalogo, y sus dos bases de conteo (§O-2) ─────────────────
curl -s "https://api.ransomware.live/v2/groupvictims/shinyhunters" -o v.json
python3 -I -c '
import json, collections
v = json.load(open("v.json"))
print("entradas:", len(v))
print("sin pais:", sum(1 for x in v if not x.get("country")))
for campo in ("ransom", "data_size", "screenshot", "press"):
    print(campo, "relleno:", sum(1 for x in v if x.get(campo)), "/", len(v))
print(collections.Counter(x.get("country") or "«vacio»" for x in v).most_common())
'
# Segunda base de conteo, para la discrepancia del 32,3 %:
curl -s "https://cti.fyi/api/v1/groups/shinyhunters" |
  python3 -I -c 'import json,sys; print("post_count:", json.load(sys.stdin)["post_count"])'

# ── 6 · El CVE (§O-4.2) ───────────────────────────────────────────────
curl -s "https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-35273"

# ── 7 · El aviso oficial, y la comparacion de citas (§O-4.1) ──────────
curl -s "https://www.ic3.gov/psa/2026/psa260515" -o ic3.html
python3 -I h2t.py ic3.html | grep -i "harassment strategies"
```

**Para comprobar el propio caso sin reproducir el nombre de nadie** (el procedimiento que
`A.1` promete): descargar el catálogo con el bloque 5, y buscar **el dominio propio** en el
campo `domain` y **el propio nombre** en el campo `victim`. Si aparece, la entrada trae sus
dos fechas, su sector y si hay captura o prensa. Si no aparece, no hay reclamación en esa
fuente, que no es lo mismo que no haber sido atacado.

---

## Anexo G — Control de cambios

| Versión | Fecha | Qué juicio se movió | Autor |
|---|---|---|---|
| `1.0` | 2026-11-24 | Primera emisión. Establece los siete juicios clave. El que sostiene el informe es **`KJ-1`**: la prueba criptográfica del regreso del 23-11-2026 **no acredita continuidad del operador**, porque está firmada con dos claves autorrevocadas el 17-03-2026 por razón de sustitución y omite la clave que el propio titular declaró vigente —medición propia reproducible, §X-1—. Se establece además que **la atribución por marca ha dejado de identificar operador** (`KJ-2`), que **el clúster de intrusión nunca se detuvo** (`KJ-3`), y que **el catálogo de este actor no permite ninguna cifra de víctimas** (`KJ-4`). Aporta `Anexo D` nuevo: evaluación de una prueba criptográfica de continuidad de marca, con escala de seis niveles. Se consignan dos defectos de fuentes que esta cartera usa a diario: una dirección de servicio oculto que es un **marcador de posición** en un agregador (`G-5`) y una discrepancia del **32,3 %** entre los dos recuentos del mismo actor | Célula CTI |

---

## Anexo H — Realimentación del consumidor

Tres preguntas, y la tercera es la que más vale:

1. ¿Alguna de las cuatro consultas de §T-2 devolvió algo? **Un resultado negativo también
   es información**, y cierra `G-6`.
2. ¿La decisión §E-3 `E-b` —la mesa de ayuda no restablece nada desde una llamada entrante— se
   puede implantar en quince días, o hay un proceso de negocio que lo impide? Si lo hay,
   **ese proceso es la exposición** y conviene que esté escrito.
3. ¿Hay en la organización algún caso de recepción de llamada de supuesto soporte pidiendo
   restablecer contraseña, aunque no haya prosperado? **Los intentos fallidos son la mejor
   telemetría disponible** de este adversario, y hoy no se recogen en ninguna parte.
