---
tlp: "TLP:CLEAR"
pap: "PAP:AMBER"
id: "CTI-2026-016"
version: "1.2"
tipo: "Perfil de actor"
foco_regional: "Chile · Latinoamérica"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "LockBit 5.0 · ChuongDong"
fecha: "2026-09-16"
caduca: "2026-12-16"
autor: "Célula CTI"
distribucion: "Reclasificado a TLP:CLEAR el 2026-11-16 por decisión del emisor. Elaborado sin telemetría propia ni datos de cliente: no contiene información identificable de la organización emisora ni de terceros. Difusión libre, conservando la atribución de las fuentes y las salvedades metodológicas del informe. Se mantiene PAP:AMBER: los indicadores del Anexo A llevan acción permitida individual y no deben cargarse en bloqueo automático sin verificación previa contra telemetría propia."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-016
## LockBit 5.0: una marca degradada con un cifrador mejor que nunca, y la presión desplazada a Latinoamérica
### Con víctima confirmada en Chile y evaluación bajo el régimen de la Ley 21.663

> **Regla de oro del producto:** todo párrafo debe responder a un requisito de
> inteligencia (PIR) y habilitar una decisión. Si un párrafo no cambia lo que
> alguien va a hacer, va al anexo o se borra.

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-016` |
| Versión / fecha | `1.2` — 2026-11-21 |
| Tipo de producto | Perfil de actor + informe de campaña |
| Niveles cubiertos | Estratégico · Operacional · Táctico · Técnico |
| Foco regional | Chile · Latinoamérica |
| Marcado de difusión | `TLP:CLEAR` · `PAP:AMBER` |
| Clasificación interna | Público — apto para difusión abierta |
| Requisitos atendidos | `PIR-01`, `PIR-02`, `PIR-04`, `PIR-07` |
| Solicitante / consumidor primario | CISO · Jefatura de SOC · Comité de Riesgo Operacional |
| Ventana de observación | 2025-09-01 → 2026-09-16 |
| Base de colección | 21 fuentes externas todo-fuente (OSINT, TECHINT de proveedor, análisis de binario independiente, CLOSINT derivado de sitio de filtración y de foro RAMP, CERT nacional). **Sin telemetría propia incorporada** |
| Autor (analista) | Célula CTI |
| Revisión por pares | Pendiente |
| Aprobación | Pendiente |
| Caducidad / revisión | 2026-12-16, o antes si se confirma nueva acción policial, rebranding, filtración de claves o cambio del esquema criptográfico |
| Productos relacionados | `CTI-2026-015` (Qilin) y `CTI-2026-014` (TheGentlemen) — complementa: los tres actores integran o rodean la misma coalición y compiten por los mismos afiliados |
| Paquete legible por máquina | Pendiente de generar (véase §14) |

<!-- cti:note type="warn" -->

> **Limitación estructural de este producto.** Se ha elaborado exclusivamente con
> fuentes abiertas, de proveedor y de análisis independiente de binario. No incorpora
> telemetría de la organización, por lo que **la sección de exposición propia (§O-4)
> está sin rellenar** y todo juicio sobre riesgo para nosotros es condicional, no
> evaluado. Un informe con §O-4 vacía es inteligencia genérica, no inteligencia propia.

<!-- cti:note type="warn" -->

> **Nota sobre la denominación «APT».** El requisito se formuló como «APT LockBit 5».
> LockBit **no es un actor de amenaza persistente avanzada con patrocinio estatal**:
> es una operación criminal de ransomware-como-servicio con ánimo de lucro, y lo ha
> sido desde 2019. La distinción cambia el modelo de motivación, el horizonte temporal
> y las opciones de disuasión: frente a un APT se compite por resistencia; frente a un
> RaaS se compite por coste de oportunidad —hacer que atacarnos salga más caro que
> atacar a otro—. El matiz relevante se trata en §O-2.

<!-- cti:note type="warn" -->

> **Nota de precisión histórica.** El ataque al **Poder Judicial de Chile fue en
> septiembre de 2022 y se ejecutó con LockBit Black (3.0)**, no con LockBit 5.0.
> Varias fuentes secundarias mezclan ambos hechos. Se consigna como precedente
> nacional del actor —§O-5—, pero **no debe citarse como actividad de la versión 5.0**.

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** LockBit volvió con la versión 5.0 en septiembre de 2025, pero **no ha
recuperado su escala anterior y su ritmo está en declive desde abril de 2026**. El
sitio de filtración acumula 362 organizaciones en doce meses, frente a las más de
7.000 reivindicadas históricamente por la marca; el ritmo pasó de una media de
54 víctimas al mes en el primer trimestre de 2026 a aproximadamente 18 al mes entre
abril y septiembre. Valoramos **probable** *(55–80 %)* que la operación siga sin
volver al primer puesto del ecosistema en los próximos seis meses.
**Confianza: moderada.** *Base:* concordancia aritmética entre Check Point (79 víctimas en Q4-2025, 163 en Q1-2026), Halcyon (335 acumuladas al 17-08-2026) y ransomware.live (362 al 14-09-2026); ninguna fuente publica la serie mensual completa, por lo que las medias son derivadas.

**KJ-2.** **La degradación de la marca es el hecho estratégico central.** Tras la
Operación Cronos (febrero de 2024), la identificación y sanción de su administrador
Dmitry Khoroshev y el hackeo de su propio panel de administración en mayo de 2025,
LockBit redujo la barrera de entrada de afiliados a **un depósito de unos 500 dólares
en bitcoin**. Valoramos **muy probable** *(80–95 %)* que esto traduzca en afiliados
menos experimentados y más oportunistas: tradecraft inconsistente, más ruido, menos
sigilo, pero también menos predecibilidad.
**Confianza: moderada.** *Base:* Check Point y Flare documentan el depósito y la reapertura del reclutamiento; Flare recoge además que «los afiliados en gran medida no quieren trabajar con ellos». Es inferencia razonada sobre la calidad del afiliado, no observación directa de su desempeño.

**KJ-3.** **El cifrador 5.0 opera sin red.** Usa ChaCha20/XChaCha20 con intercambio de
claves Curve25519 y **clave pública embebida en el binario**; un análisis dinámico
independiente registró **cero paquetes capturados** durante el cifrado completo. Esto
es **un hecho confirmado por análisis de binario**, no una estimación.
**Confianza: alta.**
*Implicación de doctrina:* **ninguna detección basada en red —C2, DNS, beaconing— verá la fase de cifrado.** La oportunidad de detección en red existe *antes*, en la exfiltración y el movimiento lateral, y *nunca* durante el impacto. Un corte de conectividad no detiene el cifrado.

**KJ-4.** El cifrador **ciega deliberadamente la telemetría de endpoint antes de
actuar**: parchea `EtwEventWrite` con una instrucción de retorno (`0xC3`) para
desactivar Event Tracing for Windows, retira los enganches de usuario del EDR
(*unhooking*), ejecuta por reflexión de DLL sin tocar disco, termina 63 servicios
identificados por hash —incluidos VSS, Veeam, Acronis, BackupExec y Windows Search—
y borra los registros de eventos con `EvtClearLog` al terminar. Valoramos **muy
probable** *(80–95 %)* que un análisis forense posterior al cifrado, apoyado solo en
artefactos del host, sea insuficiente para reconstruir la intrusión.
**Confianza: alta.** *Base:* Trend Micro, LevelBlue/SpiderLabs y ASEC coinciden de forma independiente sobre el conjunto de técnicas.

**KJ-5.** **El actor ha desplazado su presión fuera de Estados Unidos de forma
deliberada.** La proporción de víctimas estadounidenses cayó de más del 50 %
histórico al **21,2 % en el primer trimestre de 2026**, mientras crecían Italia
(8,6 %), Brasil (8,6 %), Turquía (5,1 %) y México. En el acumulado de la versión 5.0,
**Brasil y México suman 44 de 362 víctimas** y Latinoamérica representa en torno al
12–15 % del total. Valoramos **probable** *(55–80 %)* que la exposición relativa de
organizaciones chilenas y latinoamericanas a este actor sea hoy mayor que en cualquier
momento anterior de la marca.
**Confianza: moderada.** *Base:* Check Point (Q1-2026) y ransomware.live (acumulado) concuerdan en la dirección; la interpretación como evasión deliberada de jurisdicciones con presión policial agresiva es inferencia analítica, no declaración del actor.

**KJ-6.** **Hay actividad confirmada de LockBit 5.0 en Chile.** El 20 de febrero de
2026 el actor reivindicó públicamente el compromiso de **Red Dávila**, prestador de
salud, con amenaza de publicación de datos sensibles. El contexto nacional agrava el
juicio: **agosto de 2026 fue el peor mes de ransomware registrado en Chile** —al
menos diez organizaciones afectadas según CronUp— y los ocho primeros meses del año
superan cualquier año completo anterior. Valoramos **probable** *(55–80 %)* que
aparezcan nuevas víctimas chilenas de este actor en los próximos seis meses.
**Confianza: moderada.** *Base:* la reivindicación de Red Dávila está documentada por una única fuente comercial (DeXpose) sin corroboración de CSIRT nacional; el contexto de agosto procede de CronUp, con buen historial en el país.

**KJ-7.** LockBit forma parte de la **coalición anunciada en septiembre de 2025 con
DragonForce y Qilin** para «dictar las condiciones del mercado» y compartir técnicas
e infraestructura. Valoramos **posibilidad real** *(45–55 %)* de que capacidades hoy
características de Qilin —en particular la neutralización de EDR desde el kernel
mediante controladores vulnerables firmados— aparezcan en intrusiones de afiliados de
LockBit dentro de los próximos doce meses.
**Confianza: baja.** *Base:* el anuncio de la coalición está corroborado por múltiples fuentes, pero **no se ha observado todavía transferencia técnica verificada entre los tres grupos**. Es un pronóstico por razonamiento, no por evidencia. Se consigna marcado como especulativo.

**Qué cambiaría estos juicios:** (a) una detención, incautación o filtración de claves
privadas que permita un descifrador gratuito —colapsaría la operación—; (b) la
observación de un cifrador LockBit con esquema criptográfico distinto, que indicaría
cambio de desarrollador o suplantación de marca por terceros; (c) la aparición
documentada de BYOVD o de un módulo de neutralización de EDR a nivel de kernel en una
intrusión LockBit, que confirmaría KJ-7 y elevaría la severidad; (d) un repunte
sostenido por encima de 50 víctimas mensuales, que invalidaría el declive de KJ-1;
(e) la atribución por el CSIRT Nacional de un incidente de efecto significativo a este
actor en Chile.

---

## 2. Resumen ejecutivo

LockBit fue durante cuatro años la mayor operación de ransomware del mundo. En
febrero de 2024 una acción policial internacional —Operación Cronos— incautó su
infraestructura y sus claves; en mayo de 2024 se identificó y sancionó a su
administrador, el ciudadano ruso Dmitry Khoroshev, con una recompensa de diez
millones de dólares por información que lleve a su detención; en mayo de 2025 el
propio grupo fue hackeado y su base de datos de negociaciones, afiliados y carteras
quedó expuesta. **La marca sobrevivió a todo eso, pero no intacta.**

En septiembre de 2025, coincidiendo con su sexto aniversario, LockBit anunció en el
foro ruso RAMP la versión 5.0, de nombre interno «ChuongDong», con un cifrador
reescrito para Windows, Linux y VMware ESXi. Doce meses después ha reivindicado
362 organizaciones en 68 países. Es una cifra significativa en términos absolutos
—cualquiera de esas organizaciones tuvo un día muy malo— pero **modesta para lo que
fue LockBit**, y en clara desaceleración: la operación alcanzó su máximo en el primer
trimestre de 2026, cuando fue el cuarto grupo más activo del mundo, y desde abril su
ritmo ha caído en torno a dos tercios.

Lo relevante para nosotros no es el volumen, sino **dónde y cómo**. Dónde: el actor
ha reducido su presión sobre Estados Unidos del 50 % histórico al 21 % y la ha
redirigido hacia Italia, Brasil, Turquía y México. Latinoamérica pesa ya entre el 12 %
y el 15 % de sus víctimas, y hay una reivindicación confirmada en Chile —Red Dávila,
prestador de salud, en febrero de 2026—. Cómo: el cifrador 5.0 es **técnicamente
mejor que cualquier versión anterior de LockBit**. Cifra sin necesidad de red alguna,
lo que hace inútil toda detección de C2 durante el impacto; apaga el Event Tracing
for Windows parcheando una sola API; retira los enganches del EDR en espacio de
usuario; mata 63 servicios de respaldo y seguridad identificados por hash; y borra
los registros de eventos al terminar. Contra hipervisores ESXi puede cifrar una
infraestructura virtual completa en un solo movimiento.

La paradoja gobierna la decisión: **una operación en decadencia comercial con una
herramienta en mejora técnica, ofrecida a afiliados de menor nivel por un depósito de
quinientos dólares**. El riesgo no es un adversario de élite: es un operador mediocre
con un arma excelente, más difícil de predecir y menos disciplinado en su selección
de objetivos.

<!-- cti:cards -->

| Rasgo | Qué significa | Etiqueta |
|---|---|---|
| Cifra sin tocar la red: clave pública embebida, cero tráfico | Nuestra detección de red no verá el impacto. La única ventana útil en red es anterior: exfiltración y movimiento lateral | `01 · detección` |
| Ciega el ETW y desengancha el EDR antes de cifrar | La telemetría de endpoint puede estar muerta cuando ocurre el daño. El reenvío de logs fuera del host deja de ser opcional | `02 · telemetría` |
| Mata 63 servicios, entre ellos VSS, Veeam, Acronis y BackupExec | La capacidad de recuperación se decide antes del ataque, con respaldos inmutables y fuera de dominio | `03 · continuidad` |
| Variante ESXi dedicada: cifra la infraestructura virtual completa | Un solo acierto en el hipervisor equivale a cientos de servidores. La administración de virtualización necesita su propio perímetro de identidad | `04 · virtualización` |
| Desplazamiento deliberado de EE. UU. hacia el sur de Europa y LATAM | Nuestra geografía ha dejado de ser un factor de protección relativa frente a este actor | `05 · exposición regional` |
| Barrera de entrada de afiliados de 500 USD | Operadores menos capaces, pero más impredecibles y menos disciplinados en la selección de objetivos | `06 · perfil del adversario` |
| Víctima confirmada en Chile: prestador de salud, febrero 2026 | La amenaza es local y sectorialmente sensible; activa consideraciones de datos de salud y de notificación regulatoria | `07 · regulatorio` |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `362` | Organizaciones reivindicadas por LockBit 5.0 desde septiembre de 2025 | Frente a más de 7.000 atribuidas históricamente a la marca LockBit |
| `68` | Países con víctimas de la versión 5.0 | Alcance global sin discriminación geográfica, salvo la exclusión de la CEI |
| `163` | Víctimas en el primer trimestre de 2026 | Su máximo: cuarto puesto mundial, +106 % sobre el trimestre anterior |
| `21,2 %` | Proporción de víctimas en EE. UU. en Q1-2026 | Frente a más del 50 % histórico: desplazamiento deliberado de jurisdicción |
| `0` | Paquetes de red observados durante el cifrado | Cifrado totalmente autónomo: la detección de red no cubre la fase de impacto |
| `63` | Servicios de seguridad y respaldo que termina por hash | Incluye VSS, Veeam, Acronis, BackupExec y Windows Search |
| `500 USD` | Depósito de entrada para nuevos afiliados | Barrera mínima: capta operadores de bajo nivel y difícil de perfilar |
| `80,6 días` | Retraso medio entre el ataque y su publicación en el sitio de filtración | La ausencia de publicación no es prueba de ausencia de compromiso |

> ✅ **Decisión que se solicita a Dirección:** (a) instruir el reenvío en tiempo real
> de los registros de eventos de Windows a un destino fuera del host, con plazo de
> 60 días, porque la telemetría que vive solo en el endpoint es destruible por este
> actor; (b) aprobar el aislamiento de la administración de la plataforma de
> virtualización (ESXi/vCenter) en un plano de identidad y red separado, con MFA
> propio, plazo de 90 días; (c) financiar la verificación trimestral de restauración
> desde respaldos inmutables, desconectados y fuera del dominio de Active Directory,
> con la primera prueba antes de 45 días; (d) autorizar la ejecución del cuestionario
> de exposición de §O-4 y la reemisión de este informe con telemetría propia, plazo
> 30 días.

---

## 3. Alcance, requisitos y limitaciones

**3.1 Requisitos de inteligencia atendidos**

| Req. | Enunciado | ¿Respondido? | Dónde |
|---|---|---|---|
| PIR-01 | ¿Qué actores tienen intención y capacidad contra nuestro sector y geografía? | Sí | §E-1, §E-2, §O-2 |
| PIR-02 | ¿Cuál es el vector de acceso inicial más probable contra nuestra superficie expuesta? | **Parcial** — el actor no tiene un vector dominante documentado | §T-1, §14 (G-1) |
| PIR-04 | ¿Qué capacidades adversarias invalidan controles que hoy damos por eficaces? | Sí | §KJ-3, §KJ-4, §X-1, §X-3 |
| PIR-07 | ¿Qué obligaciones regulatorias se activan ante un incidente de este actor en Chile? | Parcial | §E-4, §14 |
| — | ¿Estamos ya comprometidos? | **No** — requiere telemetría propia | §O-4 |

**3.2 Fuera de alcance.** No se evalúa la exposición concreta de la organización
(inventario, versiones, cobertura de EDR, superficie ESXi), no se cuantifica el
impacto financiero de un escenario de cifrado, y no se cubren los otros integrantes
de la coalición salvo por comparación —Qilin se trata en `CTI-2026-015`—. Tampoco se
evalúa la conveniencia de pagar un rescate: es una decisión de Dirección con asesoría
legal, no un juicio de inteligencia.

**3.3 Limitaciones de la colección.** (a) Todas las cifras de víctimas proceden de un
sitio de filtración **controlado por el adversario**: miden lo que el actor decide
publicar, no lo que ocurre; las víctimas que pagan rara vez aparecen, y el retraso
medio documentado entre ataque y publicación es de **80,6 días**. (b) **Ninguna
fuente pública ofrece la serie mensual completa de LockBit 5.0 en 2026**: las medias
mensuales de este informe son *derivadas* por diferencia entre acumulados de fuentes
distintas —Check Point, Halcyon, ransomware.live— con criterios de deduplicación que
no coinciden; se declaran como estimación y no deben citarse como recuento.
(c) Durante la colección se detectó **contaminación cruzada de fuentes secundarias**
entre la actividad de LockBit 3.0 tras Cronos (2024) y la de LockBit 5.0 (2026), y
entre el ataque al Poder Judicial de Chile de 2022 y la versión actual; ambas se han
descartado y se documentan en §O-6 como hipótesis rechazadas. (d) No existe un vector
de acceso inicial dominante documentado ni un conjunto de CVE atribuido a esta versión:
es la principal brecha de este producto (§14, G-1). (e) Sin telemetría propia, según §0.

**3.4 Metodología.** Disciplinas empleadas: OSINT, OSINT comercial de proveedor,
análisis independiente de binario publicado por terceros (TECHINT de segunda mano),
CLOSINT derivado del sitio de filtración adversario y del foro RAMP, y reporte de
CERT nacional (véase Anexo B). Técnicas analíticas estructuradas aplicadas: análisis
de hipótesis competidoras (§O-6), verificación de supuestos clave y pre-mortem (§O-6),
y triangulación aritmética de acumulados discordantes (§E-3). Marcos de referencia en
el Anexo D. Léxico estimativo conforme a ICD 203 (Anexo C).

---

# NIVEL ESTRATÉGICO
### Para: Consejo · CISO · Riesgo · Legal · Horizonte: 6–24 meses

## E-1. Qué representa este actor en el panorama

<!-- cti:cards -->

| Cambio estructural | Por qué nos afecta | Etiqueta |
|---|---|---|
| **La acción policial funciona, pero no mata la marca.** Cronos incautó infraestructura y claves en 2024; LockBit volvió en 2025 con un producto mejor y una cuarta parte de su tamaño | No podemos esperar que la disuasión externa resuelva el problema. La desarticulación degrada al adversario; no lo elimina, y el que vuelve suele volver técnicamente mejorado | `01 · disuasión` |
| **Cartelización del ecosistema.** Coalición LockBit–Qilin–DragonForce anunciada en septiembre de 2025 para «dictar las condiciones del mercado» | Una TTP observada en un grupo puede propagarse a los otros. La inteligencia sobre un actor deja de ser específica de ese actor: hay que defenderse del repertorio conjunto | `02 · difusión de TTP` |
| **Fragmentación simultánea.** El ecosistema pasó de 71 grupos activos en Q1-2026 a 93 en Q2, el máximo histórico, y la concentración del top-10 cayó del 71 % al 57,6 % | Más marcas, más pequeñas y más volátiles. El valor de la inteligencia centrada en un único grupo baja; el valor de la inteligencia centrada en TTP sube | `03 · mercado` |
| **Devaluación de la marca como activo criminal.** Tras la sanción de su administrador y el hackeo de su propio panel, los afiliados de primer nivel evitan a LockBit | Nos enfrentamos con más probabilidad a un operador de segundo nivel: menos sigiloso, más ruidoso, pero también menos previsible y más propenso a errores con consecuencias destructivas | `04 · perfil del adversario` |
| **Arbitraje de jurisdicción.** La caída de víctimas estadounidenses del 50 % al 21 % coincide con la mayor presión policial y de sanciones sobre ataques a EE. UU. | El adversario optimiza por riesgo legal, no solo por rentabilidad. Latinoamérica es atractiva precisamente por su menor densidad de acción policial internacional | `05 · geografía del riesgo` |
| **Ataque al hipervisor como estrategia.** Variante ESXi dedicada, presente desde el lanzamiento en las tres plataformas | La consolidación en virtualización que abarató nuestra infraestructura también concentró el radio de daño. Un hipervisor comprometido no es un servidor: son todos | `06 · arquitectura` |

## E-2. Victimología

<!-- cti:bars title="Países con más víctimas de LockBit 5.0 (acumulado, sep. 2025 – sep. 2026)" -->

| País | Víctimas |
|---|---|
| Estados Unidos | 66 |
| Italia | 28 |
| Brasil | 28 |
| Alemania | 25 |
| México | 16 |

<!-- cti:bars title="Sectores más golpeados por LockBit 5.0 (acumulado)" -->

| Sector | Víctimas |
|---|---|
| Servicios profesionales | 62 |
| Manufactura | 62 |
| Tecnología | 48 |
| Salud | 32 |
| Agricultura y alimentación | 25 |

<!-- cti:bars title="Distribución geográfica en el primer trimestre de 2026 (% de víctimas)" -->

| País | % |
|---|---|
| Estados Unidos | 21.2 |
| Italia | 8.6 |
| Brasil | 8.6 |
| Turquía | 5.1 |
| Resto del mundo | 56.5 |

> **Lectura clave.** Dos cosas importan aquí y ninguna es el primer puesto de la
> tabla. La primera: **Estados Unidos ha dejado de ser la mitad del negocio**. Pasar
> del 50 % al 21 % en una operación que conserva capacidad global no es azar
> estadístico, es política de selección. La segunda: **Brasil empata con Italia en el
> segundo puesto**, y con México suma 44 de 362 víctimas. Latinoamérica pesa entre el
> 12 % y el 15 % del total de esta versión. La distribución sectorial —servicios
> profesionales, manufactura, tecnología, salud, agroalimentación— no describe una
> preferencia ideológica: describe **qué industrias operan infraestructura heredada,
> ventanas de mantenimiento estrechas y accesos remotos de proveedor sin MFA**. No
> estamos protegidos por ser quienes somos; estamos expuestos en la medida en que
> nuestro acceso remoto y nuestra virtualización se parezcan a los de esas víctimas.

**Presencia confirmada en Chile.** El 20 de febrero de 2026, LockBit 5.0 reivindicó
en su sitio de filtración el compromiso de **Red Dávila** (`davila.cl`), prestador de
salud, con amenaza de divulgación de datos sensibles. Es la única víctima chilena
identificable de esta versión documentada en fuentes abiertas al cierre de este
informe, y procede de **una sola fuente comercial sin corroboración de CSIRT
nacional**: se consigna con confianza moderada. El contexto nacional, en cambio, está
bien establecido: según la monitorización de CronUp, **agosto de 2026 fue el peor mes
de ransomware registrado en Chile**, con al menos diez organizaciones afectadas, y la
media mensual de 2026 —unas cuatro víctimas— cuadruplica la de 2023.

## E-3. Tendencia y pronóstico

<!-- cti:chart title="Víctimas acumuladas en el sitio de filtración de LockBit 5.0" cap="Serie construida por triangulación de acumulados de tres fuentes con criterios de deduplicación distintos (Check Point, Halcyon, ransomware.live). Los puntos intermedios son derivados, no recuentos publicados. Fuente controlada por el adversario: indica intención de publicar, no organizaciones comprometidas." -->

| Periodo | Víctimas |
|---|---|
| Oct·25 | 21 |
| Dic·25 | 100 |
| Mar·26 | 263 |
| Ago·26 | 335 |
| Sep·26 | 362 |

<!-- cti:bars title="Ritmo de publicación: media de nuevas víctimas al mes (derivada)" -->

| Periodo | Víctimas/mes |
|---|---|
| Q4 2025 | 26 |
| Q1 2026 | 54 |
| Abr–sep 2026 | 18 |

La forma de la curva es el juicio. LockBit 5.0 **creció rápido hasta marzo de 2026 y
después se aplanó**: el acumulado sube 163 víctimas en un trimestre y apenas 99 en
los cinco meses y medio siguientes. En septiembre de 2026 el ritmo de publicación
cayó un 42 % respecto del mes anterior. Esto no describe una operación en expansión,
sino una que **alcanzó su techo en el primer trimestre y desde entonces retrocede**,
en un ecosistema que mientras tanto batía su récord mensual absoluto —964 víctimas en
agosto de 2026 repartidas entre 83 grupos—. LockBit ya no marca el ritmo: lo sigue.

<!-- cti:cards -->

| Escenario | Desarrollo | Etiqueta |
|---|---|---|
| **Declive sostenido con capacidad intacta** | El volumen se estabiliza entre 15 y 25 víctimas al mes. La operación sobrevive como marca de segundo nivel con un cifrador de primer nivel, alimentada por afiliados de bajo coste. La amenaza técnica no baja aunque el volumen sí | `Probable · 55–80 %` |
| **Transferencia técnica desde la coalición** | Capacidades de Qilin —BYOVD, neutralización de EDR en kernel— aparecen en intrusiones de afiliados LockBit. El volumen no cambia, pero la severidad por incidente sube de golpe | `Posibilidad real · 45–55 % (a 12 meses)` |
| **Rebranding o disolución** | La marca, ya devaluada, se abandona; el desarrollador de «ChuongDong» reaparece bajo otro nombre conservando el cifrador. Los IOC de este informe caducan de golpe; las TTP siguen vigentes | `Poco probable · 20–45 %` |
| **Recuperación del liderazgo** | LockBit vuelve al primer puesto del ecosistema. Requeriría recuperar afiliados de élite, lo que la reputación actual de la marca no sostiene | `Muy poco probable · 5–20 %` |
| **Segunda disrupción policial efectiva** | Nueva operación internacional con incautación de claves y publicación de descifrador. Existe precedente directo —Cronos— y el administrador está identificado y sancionado | `Poco probable · 20–45 %` |
| **Suplantación de marca por terceros** | Grupos no afiliados usan cifradores LockBit filtrados o construidos con builders robados. Ya ocurrió con LockBit 3.0 en 2022–2023. Contamina la atribución y la estadística | `Posibilidad real · 45–55 %, impacto analítico` |

## E-4. Decisiones que este informe pide al nivel estratégico

<!-- cti:table highlight="ANCI|Ley 21.663|CSIRT|Chile|regional" -->

| # | Decisión | Fundamento | Plazo |
|---|---|---|---|
| E-a | Instruir el **reenvío en tiempo real de los registros de eventos de Windows y de los hipervisores a un destino fuera del host**, con retención independiente del endpoint | KJ-4: el actor parchea ETW y borra los registros con `EvtClearLog`. La telemetría que vive solo en el equipo es destruible por diseño | 60 días |
| E-b | Aprobar el **aislamiento del plano de administración de la virtualización** (ESXi, vCenter, Proxmox): red segregada, cuentas dedicadas no vinculadas al dominio, MFA propio y bastión | KJ-3 y §X-1: existe una variante ESXi dedicada capaz de cifrar toda la infraestructura virtual en un movimiento | 90 días |
| E-c | Financiar **respaldos inmutables, desconectados y fuera del dominio**, con prueba de restauración verificada trimestralmente, incluida la infraestructura de respaldo misma (Veeam, Acronis, BackupExec, VSS) | KJ-4: el cifrador termina 63 servicios por hash, entre ellos los de las tres suites de respaldo más habituales | 45 días (primera prueba) |
| E-d | Exigir **MFA resistente a phishing en el 100 % de los accesos remotos**, incluidos los de proveedores y los de administración de virtualización, y eliminar todo RDP expuesto a Internet | §T-1: sin vector dominante documentado, las credenciales válidas sin MFA sobre accesos remotos expuestos son el denominador común de los casos descritos | 60 días |
| E-e | Instruir a Legal y Comunicaciones la preparación del procedimiento de notificación a la **ANCI** bajo la **Ley 21.663** y del guion de respuesta a doble extorsión, con atención específica a datos de salud y de terceros | KJ-6: hay víctima confirmada en Chile en el sector salud, y **agosto de 2026 fue el peor mes de ransomware del país** | 30 días |
| E-f | Decidir y documentar **por anticipado** la postura institucional ante el pago de rescate, con criterio legal y de continuidad | El administrador de LockBit está **sancionado por OFAC, el Reino Unido y Australia**: un pago a esta operación puede constituir incumplimiento de régimen de sanciones, además de una decisión de negocio | 60 días |
| E-g | Encargar a la célula CTI la ejecución del cuestionario de exposición de §O-4 y la reemisión de este informe con telemetría propia incorporada | §0 y §14: sin ese paso, este producto no permite calcular riesgo propio | 30 días |

> ⚠ **Advertencia de sanciones.** Dmitry Khoroshev, administrador de LockBit, fue
> identificado y sancionado en mayo de 2024 por OFAC (EE. UU.), el FCDO (Reino Unido)
> y el Departamento de Asuntos Exteriores de Australia, con una recompensa de hasta
> 10 millones de dólares por información que conduzca a su detención. **Un pago de
> rescate a esta operación tiene una dimensión de cumplimiento normativo que no
> tienen otros actores.** Esta advertencia no constituye asesoría legal: la decisión
> E-f debe tomarse con asesoría jurídica formal.

---

# NIVEL OPERACIONAL
### Para: Jefatura de SOC · Respuesta a Incidentes · Threat Hunting · Horizonte: semanas–meses

## O-1. Identificación y alias

| Designación | Origen | Grado de equivalencia |
|---|---|---|
| `LockBit` | Autodenominación (desde septiembre de 2019) | Referencia — designa la operación completa |
| `LockBit 5.0` | Autodenominación de la versión (septiembre de 2025) | Referencia — designa la generación actual del cifrador y su programa de afiliados |
| `ChuongDong` | Nombre interno de la compilación, presente en los artefactos | Equivalente a LockBit 5.0 — **es un identificador de build, no un grupo ni una persona** |
| `LB_Black_14_01_2026`, `LB_Linux_14_01_2026`, `LB_ESXi_14_01_2026`, `LB_ChuongDong_14_01_2026` | Nombres de variante en el panel de afiliados | **No son grupos**: son variantes de compilación datadas |
| `Bitwise Spider` | CrowdStrike | Equivalente — designa al núcleo operador |
| `Storm-0506` / clústeres afiliados | Microsoft | **Solapamiento parcial** — designan afiliados concretos, no la operación |
| `LockBitSupp` | Alias del administrador en foros | Persona, no grupo. Identificado como Dmitry Khoroshev (NCA, mayo de 2024) |
| `G0128` | MITRE ATT&CK | Referencia formal del marco |
| `LockBit Black` / `LockBit 3.0` | Versión anterior (2022) | **Generación distinta.** Su builder fue filtrado en 2022 y usado por terceros no afiliados |

> **Nota de tradecraft.** Tres errores frecuentes con este actor, todos con
> consecuencias analíticas reales. **Primero:** tratar `ChuongDong` como un grupo o un
> autor; es el nombre interno de la compilación. **Segundo:** fusionar LockBit 3.0 con
> LockBit 5.0; el builder de 3.0 se filtró en septiembre de 2022 y desde entonces
> cualquiera puede generar un cifrador «LockBit» sin relación alguna con la operación
> —una parte no determinada de los incidentes atribuidos a la marca entre 2023 y 2025
> corresponde a terceros—. **Tercero:** atribuir a LockBit 5.0 hechos anteriores a
> septiembre de 2025, en particular el ataque al Poder Judicial de Chile de 2022. La
> fusión indebida de alias y generaciones es una de las principales fuentes de error
> analítico en este dominio.

## O-2. Estructura y atribución

| Eje de atribución | Valoración | Confianza |
|---|---|---|
| Clúster técnico | Familia de cifradores coherente y documentada desde 2019, con reescritura completa en la generación 5.0: ChaCha20/XChaCha20 + Curve25519, builds para Windows, Linux y ESXi | Alta |
| Grupo organizado | RaaS con panel de afiliados, builders propios, portal de negociación en Tor, reglas de targeting publicadas y depósito de entrada de ~500 USD | Alta |
| Nexo estatal | **Ninguno identificado.** Operación con ánimo exclusivamente de lucro. La exclusión de trece países post-soviéticos es tolerancia de facto, no patrocinio | Moderada |
| Origen geográfico | Operación de habla rusa: actividad en el foro RAMP, comprobación de configuración regional e idioma ruso en el binario con terminación de la ejecución | Alta |
| Identidad nominal | **Dmitry Yuryevich Khoroshev**, alias `LockBitSupp`, identificado y sancionado por NCA, OFAC y Australia en mayo de 2024 como administrador y desarrollador | Alta — caso excepcional en este dominio |

*Razonamiento:* la atribución de LockBit es, de forma inusual, **sólida y oficial**.
No descansa en inferencia de proveedor sino en una identificación gubernamental
formal acompañada de sanciones y acusación. A ello se suma evidencia técnica directa:
el cifrador 5.0 **termina su ejecución al detectar configuración de idioma o
geolocalización rusa**, comportamiento que solo tiene sentido como seguro de
supervivencia dentro de la jurisdicción de origen.

*Contraargumento:* la identificación del administrador **no se extiende a los
afiliados**, que son quienes ejecutan las intrusiones y cuyo tradecraft varía
enormemente. Atribuir una intrusión «a LockBit» dice poco sobre quién estuvo
realmente dentro de la red. Además, el builder filtrado de la generación 3.0 permite
que terceros sin vínculo alguno generen cifradores de marca LockBit: **la presencia
de la marca no prueba la participación de la operación**.

## O-3. Modelo de negocio / de operación

LockBit 5.0 es una reconstrucción a la baja de un negocio que antes fue dominante.

**Reclutamiento.** El anuncio de la versión 5.0 se publicó en el foro ruso RAMP en
septiembre de 2025, coincidiendo con el sexto aniversario de la marca y planteado
explícitamente como una llamada a nuevos afiliados. La barrera de entrada se fijó en
un depósito de aproximadamente **500 dólares en bitcoin** —una cifra simbólica frente
a los estándares del sector—, lo que revela el problema real del actor: **no consigue
afiliados de calidad**. El análisis de Flare sobre el panel filtrado recoge que «la
reputación de LockBit ya no está tan bien considerada y los afiliados en gran medida
no quieren trabajar con ellos».

**Reglas de targeting.** El programa **permite explícitamente** atacar infraestructura
crítica, centros médicos y organismos de gobierno, y **prohíbe** operar contra trece
países post-soviéticos. No existe restricción sectorial que nos proteja.

**Economía.** El reparto histórico es de 70–80 % para el afiliado. El hackeo del panel
en mayo de 2025 expuso la escala real del negocio en su etapa previa: en cinco meses
—diciembre de 2024 a abril de 2025— el conjunto de la operación movió unos 2,3
millones de dólares, de los que el núcleo retuvo alrededor de 456.000. Los rescates
se concentraban entre **2.000 y 40.000 dólares**, con demandas excepcionales de hasta
4,5 millones. Es una operación de **volumen y ticket bajo**, no de caza mayor; el
corolario defensivo es que **una organización mediana es un objetivo perfectamente
rentable para este actor**.

**Producto.** El panel entrega al afiliado builders para Windows, Linux y ESXi, carga
autónoma de datos robados y de imágenes al sitio de filtración sin intervención del
operador, y chat de negociación en Tor. La herramienta propia de exfiltración es
**StealBit**, con búsqueda automática de archivos de interés.

## O-4. Nuestra exposición

> ⬛ **Sección sin evaluar — requiere telemetría interna.** Este informe no incorpora
> datos de la organización. Hasta que este cuestionario se responda, todo juicio de
> riesgo propio es condicional. Borrar esta nota al rellenarla.

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| X-1 | ¿Qué servicios de acceso remoto exponemos a Internet (RDP, VPN, portales de proveedor, RMM) y cuáles carecen de MFA resistente a phishing? | Inventario externo + IAM | TI/Redes |
| X-2 | ¿Están nuestros hosts ESXi/vCenter accesibles desde la red de usuarios? ¿Con qué cuentas y con qué MFA? | Inventario de virtualización | TI/Infraestructura |
| X-3 | ¿Reenviamos los registros de eventos de Windows fuera del host en tiempo real? ¿Cuánto tiempo sobreviviría la evidencia a un `EvtClearLog`? | Arquitectura de SIEM | SOC |
| X-4 | ¿Nuestro EDR detecta el parcheo de `EtwEventWrite` y el *unhooking* en espacio de usuario? ¿Está la protección antimanipulación activa y verificada? | Configuración de EDR | SOC / Ingeniería |
| X-5 | ¿Tenemos cobertura de EDR o telemetría equivalente en hosts Linux y en los hipervisores, o solo en Windows? | Inventario de agentes | SOC |
| X-6 | ¿Nuestros respaldos son inmutables, están desconectados y viven **fuera** del dominio de Active Directory? ¿Cuándo se probó la última restauración completa? | Plataforma de respaldo | TI/Continuidad |
| X-7 | ¿Las cuentas de servicio de las suites de respaldo (Veeam, Acronis, BackupExec) tienen privilegios de dominio innecesarios? | Revisión de AD | IAM |
| X-8 | ¿Detectamos transferencias salientes anómalas de gran volumen **con independencia** de que haya cifrado? | Telemetría de red / DLP | SOC |
| X-9 | ¿Algún proveedor nuestro figura entre las víctimas publicadas por este actor en los últimos doce meses? | Gestión de terceros | Riesgo / Compras |

## O-5. Cronología

<!-- cti:timeline -->

| Fecha | Hecho | Traza |
|---|---|---|
| 2019-09 | Aparece LockBit (inicialmente «ABCD»). Inicio de la operación RaaS | Global |
| 2022-06 | Lanzamiento de LockBit 3.0 «LockBit Black» | Global |
| 2022-09 | **Ataque al Poder Judicial de Chile con LockBit Black: unos 150 equipos infectados, mayoritariamente Windows 7.** Generación 3.0 — **no confundir con 5.0** | Chile |
| 2022-09 | Filtración del builder de LockBit 3.0. Desde aquí, terceros no afiliados pueden generar cifradores de marca LockBit | Global |
| 2024-02-20 | **Operación Cronos: NCA, FBI y Europol incautan infraestructura, servidores y claves de descifrado** | Global |
| 2024-05-07 | **Identificación y sanción de Dmitry Khoroshev (`LockBitSupp`) por NCA, OFAC y Australia. Recompensa de 10 M USD** | Global |
| 2025-05-07 | El panel de administración de LockBit es hackeado: se filtran 4.400 mensajes de negociación, 62.400 carteras bitcoin y 75 cuentas de afiliado con contraseñas en claro | Global |
| 2025-09 | **Anuncio de LockBit 5.0 «ChuongDong» en el foro RAMP. Nuevo sitio de filtración, reclutamiento abierto con depósito de ~500 USD** | Global |
| 2025-09 | DragonForce propone públicamente una coalición con LockBit y Qilin; LockBit acepta y el cartel se declara activo | Global |
| 2025-10 | Primeras 21 víctimas publicadas en el nuevo sitio de filtración | Global |
| 2026-01-14 | Nuevas variantes datadas en el panel: `LB_Black`, `LB_Linux`, `LB_ESXi`, `LB_ChuongDong` | Global |
| 2026-02-20 | **LockBit 5.0 reivindica el compromiso de Red Dávila, prestador de salud chileno** | Chile |
| 2026-03-31 | Cierre de su mejor trimestre: 163 víctimas, cuarto puesto mundial, +106 % sobre Q4-2025 | Global |
| 2026-08 | **Mes récord de ransomware en Chile: al menos diez organizaciones afectadas (todos los actores)** | Chile |
| 2026-09-14 | Última víctima publicada al cierre de este informe. Acumulado 362 en 68 países; ritmo mensual −42 % | Global |

## O-6. Hipótesis alternativas consideradas

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| **H1 — LockBit 5.0 está en declive estructural y no recuperará el liderazgo** | Consistente con la serie de acumulados, con el aplanamiento desde abril de 2026, con el −42 % de septiembre y con la evidencia sobre la reputación de la marca entre afiliados | `Retenida — hipótesis principal` |
| **H2 — El declive es aparente: el actor publica menos porque cobra más** | Inconsistente con el modelo de ticket bajo documentado en el panel filtrado (2.000–40.000 USD) y con la tasa de pago del ecosistema en mínimos. Un actor que cobra más publica más, no menos: la publicación **es** el instrumento de presión | `Poco probable · 20–45 %` |
| **H3 — Parte de las víctimas atribuidas no corresponde a la operación, sino a terceros con builders filtrados** | Plausible y **no descartable**: el builder de 3.0 circula desde 2022. Sin embargo, las variantes 5.0 no se han filtrado públicamente, lo que limita el efecto a incidentes mal clasificados por marca | `Retenida como factor de ruido` |
| **H4 — La coalición con Qilin y DragonForce es propaganda sin contenido operativo** | **Consistente con la evidencia disponible.** Un año después del anuncio no se ha documentado transferencia técnica verificada entre los tres grupos. KJ-7 se emite con confianza baja precisamente por esto | `Retenida en paralelo a KJ-7` |
| **H5 — El Poder Judicial de Chile fue víctima de LockBit 5.0** | **Falsa.** El incidente es de septiembre de 2022 y se ejecutó con LockBit Black (3.0), documentado por el CSIRT Nacional con cadena de infección `123.cmd → injector.exe → lbb.dll`. Varias fuentes secundarias lo mezclan con la versión actual | `Descartada` |
| **H6 — LockBit es un actor patrocinado por un Estado** | Sin evidencia. La tolerancia jurisdiccional y la exclusión de la CEI son rasgos comunes a todo el ecosistema criminal ruso-parlante. Se consigna para que no se reabra | `Descartada` |

**Supuesto clave:** que el sitio de filtración refleja de forma razonablemente
consistente el volumen real de la operación. **Si es falso** —por ejemplo, si el actor
ha cambiado su política de publicación, o si negocia en privado con la mayoría de sus
víctimas— entonces KJ-1 se invierte y estaríamos ante una operación activa que
simplemente se ha vuelto silenciosa, lo cual es peor. El retraso medio de **80,6 días**
entre ataque y publicación hace que este supuesto sea frágil en el corto plazo: **el
volumen de los dos últimos meses siempre está subestimado**.

**Pre-mortem:** es marzo de 2027 y este informe resultó equivocado. La explicación más
probable: tratamos el descenso de volumen como descenso de amenaza. Un afiliado de
bajo coste entró por un acceso de proveedor sin MFA, encontró el vCenter alcanzable
desde la red de usuarios y cifró toda la granja virtual en una noche. El volumen
global del actor siguió siendo bajo todo el año; el nuestro fue del 100 %. **El
volumen de un actor no es su severidad.**

## O-7. Indicadores y señales de alerta

| # | Indicador observable | Qué señalaría | Disciplina | Responsable |
|---|---|---|---|---|
| I-1 | Aparición de una organización chilena o de un proveedor nuestro en el sitio de filtración de LockBit 5.0 | Actividad regional activa; posible exposición por terceros | OSINT / CLOSINT | Célula CTI |
| I-2 | Publicación de un cifrador LockBit con esquema criptográfico distinto de ChaCha20/Curve25519 | Cambio de desarrollador, suplantación de marca o nueva generación | TECHINT | Célula CTI |
| I-3 | Primer caso documentado de BYOVD o neutralización de EDR en kernel en una intrusión LockBit | Confirmación de KJ-7: transferencia técnica desde la coalición. Elevaría la severidad | TECHINT / OSINT | Célula CTI |
| I-4 | Anuncio de descifrador gratuito o incautación de claves privadas | Colapso de la operación; oportunidad de recuperación para víctimas históricas | OSINT | Célula CTI |
| I-5 | Repunte sostenido por encima de 50 víctimas mensuales durante dos meses consecutivos | Invalidación de KJ-1: la operación se recupera | OSINT | Célula CTI |
| I-6 | Alerta del CSIRT Nacional o de la ANCI que mencione a LockBit o a `ReadMeForDecrypt.txt` | Actividad confirmada en territorio nacional con validación oficial | CERT nacional | Célula CTI |
| I-7 | Aparición de nuevas variantes datadas en el panel (patrón `LB_*_DD_MM_AAAA`) | Desarrollo activo: el cifrador sigue mantenido pese al declive comercial | CLOSINT | Célula CTI |
| I-8 | Actividad del alias `LockBitSupp` o sucesor en RAMP tras un periodo de silencio | Señal temprana de rebranding o de nueva campaña de reclutamiento | CLOSINT | Célula CTI |

---

# NIVEL TÁCTICO
### Para: Analistas de SOC · Ingeniería de Detección · Threat Hunting · Horizonte: días–semanas

## T-1. Cadena de intrusión

<!-- cti:stages title="Tres etapas, y solo las dos primeras son observables" dwell="next" -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 01 · Acceso | Credencial válida antes que exploit | Acceso remoto sin MFA (RDP, VPN, portal de proveedor) · credenciales compradas a infostealers · fuerza bruta · phishing (~22 %) · explotación de servicio expuesto (~22 %) |
| Etapa 02 · Dominio | Identidad, no malware | Volcado de credenciales y robo de token · propagación por SMB y RDP · cuentas de servicio sobreprivilegiadas · abuso de RMM · Cobalt Strike (observado en ESXi como `_.sf_`) · Volatility reutilizado para extraer credenciales de memoria de máquinas virtuales |
| Etapa 03 · Impacto | Ciega, destruye, cifra — sin red | ETW parcheado · *unhooking* de EDR · 63 servicios terminados por hash · exfiltración con StealBit · borrado de instantáneas y de TEMP · cifrado ChaCha20 sin tráfico de red · `EvtClearLog` · borrado de espacio libre (`-w`) · autoeliminación |

**Permanencia:** no existe una mediana publicada para LockBit 5.0 —es una brecha
declarada en §14—. La referencia disponible del ecosistema sitúa las intrusiones más
rápidas en **exfiltración a los ~72 minutos** del acceso inicial. Planificar la
respuesta sobre horas, no sobre días.

> ⚠ **La etapa 03 no es detectable en red.** El cifrador lleva la clave pública
> Curve25519 embebida y genera sus claves de sesión localmente desde `/dev/urandom` o
> desde tiempo y memoria del sistema. **Cero paquetes durante el cifrado.** Toda la
> oportunidad de detección en red está en las etapas 01 y 02; una vez iniciada la 03,
> desconectar la red no detiene nada.

## T-2. Mapa MITRE ATT&CK

<!-- cti:matrix -->

| Táctica | ID | Técnica | Procedimiento observado |
|---|---|---|---|
| Acceso inicial | T1078 | Valid Accounts | Credenciales válidas sin MFA sobre accesos remotos expuestos; compra en mercados de infostealers |
| Acceso inicial | T1133 | External Remote Services | RDP y portales VPN expuestos a Internet |
| Acceso inicial | T1190 | Exploit Public-Facing Application | Explotación de servicios expuestos (~22 % de los casos). **Sin CVE específica atribuida a esta versión** |
| Acceso inicial | T1566 | Phishing | ~22 % de los casos; señuelos asistidos por IA |
| Ejecución | T1059.001 | PowerShell | Cadenas de ejecución ofuscadas para descarga y carga de componentes |
| Ejecución | T1106 | Native API | Resolución dinámica de API y ejecución en memoria |
| Persistencia | T1543.003 | Create or Modify System Process: Windows Service | Creación de servicios para ejecución privilegiada |
| Escalada | T1134 | Access Token Manipulation | Robo y suplantación de token para movimiento con privilegios |
| Evasión | T1055.012 | Process Injection: Process Hollowing | Ejecución del cifrador dentro de un proceso legítimo vaciado |
| Evasión | T1620 | Reflective Code Loading | Carga del payload por reflexión de DLL, sin escritura en disco |
| Degradación de defensas | T1685 | Disable or Modify Tools | Terminación de 63 servicios de seguridad y respaldo identificados por hash CRC32. **Y el cegado del canal de telemetría**, que hasta la v20 era técnica aparte (`T1562.006`): parcheo de `EtwEventWrite` con `0xC3`, *unhooking* de las funciones enganchadas por el EDR en espacio de usuario, y evasión de AMSI |
| Degradación de defensas | T1685.005 | Clear Windows Event Logs | `EvtClearLog` tras completar el cifrado |
| Evasión | T1070.004 | Indicator Removal: File Deletion | Borrado de TEMP, autoeliminación (desactivable con `-k`) y borrado de espacio libre (`-w`) |
| Evasión | T1027.002 | Obfuscated Files or Information: Software Packing | Empaquetado y ofuscación del loader; carga XOR + LZ del payload |
| Evasión | T1497 | Virtualization/Sandbox Evasion | Detección de `TracerPid` en `/proc/self/status` y huella de VM por `/proc/ioports` (Linux); retardo de ejecución configurable |
| Evasión | T1614.001 | System Location Discovery: Language Discovery | **Termina la ejecución ante configuración de idioma o geolocalización rusa** |
| Acceso a credenciales | T1003 | OS Credential Dumping | Volcado de credenciales; **Volatility reutilizado contra memoria de máquinas virtuales** |
| Descubrimiento | T1082 | System Information Discovery | Enumeración previa a la selección de modo de cifrado (`all`/`local`/`net`) |
| Movimiento lateral | T1021.001 | Remote Services: Remote Desktop Protocol | Propagación por RDP con credenciales válidas |
| Movimiento lateral | T1021.002 | Remote Services: SMB/Windows Admin Shares | Propagación y despliegue por recursos administrativos |
| Recolección | T1560 | Archive Collected Data | Preparación de datos para exfiltración |
| Exfiltración | T1567 | Exfiltration Over Web Service | **Vector principal de robo**: servicios en la nube, FTP/SFTP y túneles propios. Herramienta: StealBit |
| Impacto | T1486 | Data Encrypted for Impact | ChaCha20/XChaCha20 + Curve25519; extensión aleatoria de 16 caracteres; cifrado parcial configurable (`-r 10-90`) |
| Impacto | T1490 | Inhibit System Recovery | Borrado de instantáneas de volumen; terminación de VSS y de los servicios de las suites de respaldo |
| Impacto | T1489 | Service Stop | Detención masiva de servicios antes del cifrado |
| Impacto | T1675 | Unauthorized Virtualization Administration Activity | Cifrado de infraestructura ESXi completa desde el plano de administración del hipervisor |

## T-3. Dónde atacamos en la Pirámide del Dolor

<!-- cti:pyramid -->

| Nivel | Qué contiene en este informe y qué vale | Valor |
|---|---|---|
| Hashes | Anexo A: cinco SHA-256 y cinco MD5 de muestras públicas. Cada afiliado compila su propia variante desde el panel —hay builds datadas cada pocas semanas—. Sirven solo para retrohunt | Base · valor trivial |
| IP · Dominios | **Prácticamente nulo en este actor.** El cifrado no genera tráfico y la negociación vive en Tor. No hay infraestructura de C2 que bloquear durante el impacto | Valor bajo |
| Artefactos | `ReadMeForDecrypt.txt`, extensión aleatoria de 16 caracteres hexadecimales, tamaño original embebido en el pie del archivo cifrado, nombres de servicio detenidos. Duraderos entre builds | Valor medio |
| Herramientas | Cobalt Strike, StealBit, RMM legítimos, **Volatility contra memoria de máquinas virtuales**. Legítimas o de doble uso: detectar por contexto, nunca por presencia | Valor alto |
| TTP | Parcheo de `EtwEventWrite`, *unhooking* de EDR, terminación masiva de servicios por hash, `EvtClearLog`, cifrado ESXi desde el plano de administración. **Aquí debe concentrarse el esfuerzo** | Cima · valor máximo |

> **Lectura clave.** Este actor **invierte la economía habitual de los IOC**. En un
> ransomware con C2 activo, bloquear dominios compra tiempo. Aquí no: el impacto es
> autónomo y silencioso en red. Todo el presupuesto de detección debe subir a los dos
> pisos superiores de la pirámide, y muy especialmente al comportamiento previo:
> identidad anómala, exfiltración y administración inusual del hipervisor.

## T-4. Hipótesis de caza prioritarias

<!-- cti:accordion critical="^(H-1|H-2|H-3|H-4)\b" regional="^(H-11|H-12)\b" -->

**H-1 — Parcheo de ETW en memoria.** Buscar escrituras en la página de código de
`ntdll!EtwEventWrite` dentro de procesos que no sean depuradores legítimos, o la
ausencia súbita de eventos ETW de un proceso que estaba emitiendo. Fuente: telemetría
de EDR con visibilidad de modificación de memoria de módulo; ventana de 30 días.
Fidelidad esperada alta, falsos positivos concentrados en herramientas de seguridad,
perfiladores y anticheat. **Si el EDR no puede responder a esta consulta, esa es la
brecha número uno y debe escalarse como hallazgo, no como carencia de la caza.**

**H-2 — Desenganche de EDR en espacio de usuario.** Buscar procesos que releen
`ntdll.dll` desde disco o desde `\KnownDlls` y reescriben secciones de código ya
cargadas. Fuente: EDR, eventos de acceso a `\Device\HarddiskVolume*\Windows\System32\ntdll.dll`
con posterior `WriteProcessMemory` sobre el propio proceso. Fidelidad media-alta;
falsos positivos en EDR competidores, empaquetadores comerciales y algunos motores
antitrampa.

**H-3 — Terminación masiva de servicios seguida de silencio de respaldo.** Buscar la
detención de tres o más servicios del conjunto {`VSS`, `vmms`, `WSearch`,
`BackupExecVSSProvider`, `VeeamTransportSvc`, `AcrSch2Svc`, `EdgeUpdate`} en una
ventana de cinco minutos en un mismo host. Fuente: EID 7036/7040 del registro de
sistema y telemetría de EDR. **Fidelidad muy alta**: es un patrón que casi nunca
ocurre de forma legítima fuera de una ventana de mantenimiento planificada. Cruzar
con el calendario de cambios para eliminar el único falso positivo real.

**H-4 — Administración anómala del hipervisor.** Buscar sesiones SSH o de consola
contra hosts ESXi desde direcciones que no sean el bastión de administración,
habilitación de SSH en hosts donde estaba deshabilitado, y ejecución de `esxcli vm
process kill` o apagados masivos de máquinas virtuales fuera de ventana. Fuente:
`hostd`/`vpxa`, registros de vCenter, NetFlow hacia la VLAN de gestión.
**Fidelidad muy alta y es la hipótesis con mayor relación daño evitado/esfuerzo de
todo este informe**: un solo acierto aquí evita el escenario de peor caso.

**H-5 — Borrado de registros de eventos.** Buscar EID 1102 (Security) y 104 (System)
en cualquier host, y muy especialmente su ausencia posterior de eventos. Fuente: SIEM
con reenvío en tiempo real. **La consulta solo funciona si los logs salen del host
antes del borrado**: si la única copia está en el equipo, este evento se borra a sí
mismo. Fidelidad alta cuando hay reenvío; nula cuando no lo hay.

**H-6 — Creación masiva de archivos con extensión aleatoria de 16 caracteres.**
Buscar en telemetría de sistema de archivos renombrados en cadena hacia extensiones
de exactamente 16 caracteres hexadecimales, con más de 500 eventos por proceso y
minuto. Fuente: EDR o auditoría de archivos. **Es una detección de última milla**: si
dispara, el cifrado ya empezó. Debe ejecutar contención automática sin escalado.

**H-7 — Aparición de `ReadMeForDecrypt.txt`.** Buscar la creación de ese nombre exacto
en cualquier ruta, incluidos recursos compartidos y almacenes de respaldo. Fidelidad
máxima, falsos positivos nulos, valor temporal mínimo —llega tarde—, pero es el
disparador natural de la declaración de incidente y del reloj regulatorio.

**H-8 — Exfiltración previa al cifrado.** Buscar transferencias salientes superiores
a 1 GB hacia servicios de almacenamiento en la nube, FTP/SFTP o destinos nuevos,
desde servidores que normalmente no originan tráfico saliente masivo. Fuente: NetFlow,
proxy, DLP. Fidelidad media, muchos falsos positivos en entornos con respaldo en la
nube: **hay que construir primero la línea base por host, no por organización**.
Esta es la última ventana de detección con margen real de reacción.

**H-9 — Cobalt Strike disfrazado en almacén de datos ESXi.** Buscar archivos con
nombres tipo `_.sf_` o extensiones atípicas en los datastores, y procesos no
pertenecientes a VMware ejecutándose en el hipervisor. Fuente: inventario de
datastore, integridad de host ESXi. Fidelidad alta, volumen bajo.

**H-10 — Volatility o herramientas forenses contra memoria de máquinas virtuales.**
Buscar lectura o copia de archivos `.vmem`, `.vmsn` y `.vmss` por procesos ajenos a
la plataforma de respaldo aprobada. Fuente: auditoría de acceso a archivos en
datastores. **Técnica poco conocida y muy poco cubierta**: el adversario extrae
credenciales de la memoria de una VM sin tocar el sistema operativo invitado, con lo
que el EDR de esa VM nunca ve nada.

**H-11 — Accesos desde ASN o geografías anómalas a portales de acceso remoto.** Buscar
autenticaciones exitosas sin MFA, o con MFA satisfecho de forma sospechosa, contra
VPN, RDP Gateway y portales de proveedor. Priorizar cuentas de proveedores y cuentas
de servicio. Fuente: IdP y concentradores VPN. **Prioridad regional**: es el vector
común de los casos LATAM documentados.

**H-12 — Credenciales de la organización en volcados de infostealer.** Buscar dominios
corporativos y de filiales en colecciones de credenciales robadas. El 35,6 % de las
víctimas de este actor presenta datos de dominio asociados a infostealers. Fuente:
servicios de monitorización de credenciales. **Prioridad regional y de tercera parte**:
incluir a proveedores con acceso a nuestra red.

## T-5. Brechas de visibilidad que hay que cerrar primero

| Brecha | Por qué importa aquí |
|---|---|
| Registros de eventos que solo viven en el host | H-5 queda anulada por diseño: el actor borra la única copia. Sin reenvío en tiempo real no hay forense posterior |
| Sin telemetría en hipervisores ESXi | H-4, H-9 y H-10 quedan ciegas, y son las tres hipótesis de mayor valor contra el escenario de peor caso |
| Sin visibilidad de modificación de memoria de módulos | H-1 y H-2 quedan ciegas. El actor opera precisamente en esa capa |
| Cobertura de EDR solo en Windows | La variante Linux es funcionalmente equivalente y **totalmente autónoma**: sin agente no hay ninguna señal |
| Sin línea base de tráfico saliente por host | H-8 genera demasiado ruido para ser operable, y es la última oportunidad de detección con margen |
| Protección antimanipulación del EDR no verificada | Todo el capítulo de evasión de este actor asume que el agente puede ser degradado desde espacio de usuario |
| Sin inventario de accesos remotos de proveedores | H-11 no puede priorizarse sin saber qué cuentas de tercero existen y qué alcanzan |

---

# NIVEL TÉCNICO
### Para: Ingeniería de detección · Automatización · TIP/SIEM · Vida útil: días–semanas

## X-1. Arsenal y capacidad

| Propiedad | Valor |
|---|---|
| Nombre interno de la generación | `ChuongDong` (LockBit 5.0), anunciada en septiembre de 2025 |
| Arquitectura | **Dos componentes**: loader + payload. El loader descifra el payload con XOR y descompresión LZ y lo ejecuta **en memoria**, por reflexión de DLL |
| Criptografía | **ChaCha20 / XChaCha20** para el contenido; **Curve25519 (X25519)** para el envoltorio de clave, con **clave pública embebida en el binario**; derivación con **BLAKE2b**. Nonce de 24 bytes en la cabecera del archivo |
| Generación de claves | Dos valores aleatorios de 32 bytes derivados de tiempo del sistema y estado de memoria (Windows) o de `/dev/urandom` (Linux). **Sin comunicación con el operador** |
| Dependencia de red | **Ninguna.** Análisis dinámico independiente: 0 paquetes capturados durante el cifrado completo |
| Umbral de cifrado por tamaño | Archivos ≤ `0x5000000` (80 MB): una sola pasada. Mayores: por bloques de `0x800000` con hash propio |
| Cifrado parcial | Configurable por el afiliado entre el 10 % y el 90 % del archivo (`-r`) |
| Extensión | Aleatoria de **16 caracteres hexadecimales** por ejecución; el binario precalcula un conjunto de 100 extensiones de 8 bytes |
| Marcador de infección | **No hay marcador al final del archivo.** Sí se conserva el **tamaño original embebido en el pie** del archivo cifrado |
| Nota de rescate | `ReadMeForDecrypt.txt`, distribuida por directorios. Remite al sitio Tor con chat de soporte |
| Plataformas | Windows (~80 % de los ataques observados), Linux y **VMware ESXi** (~20 % conjunto). Builds datadas: `LB_Black`, `LB_Linux`, `LB_ESXi`, `LB_ChuongDong` |
| Exclusiones de cifrado | Directorios de Windows y Program Files; extensiones `exe`, `dll`, `sys`, `lnk`, `cpl` |
| Salvaguarda geopolítica | **Termina la ejecución ante configuración de idioma o geolocalización rusa** |
| Anti-análisis (Linux) | Detección de depurador por `TracerPid` en `/proc/self/status`; huella de máquina virtual por `/proc/ioports`. `ptrace`/`strace` resultan inoperantes; se requiere eBPF |
| Anti-análisis (Windows) | Empaquetado y ofuscación, retardo de ejecución configurable, *unhooking* de espacio de usuario, evasión de AMSI, parcheo de ETW, process hollowing |
| Higiene post-impacto | Borrado de TEMP, `EvtClearLog`, borrado de espacio libre (`-w`), autoeliminación activada por defecto (`-k` la desactiva) |
| Herramienta de exfiltración | **StealBit**, con búsqueda automática de archivos de interés |
| Novedades frente a 4.0 | Mutex, retardo de ejecución, barra de estado, borrado de TEMP, **módulo de borrado destructivo (wiper)** y reescritura completa del borrado de instantáneas y del cifrado de archivos grandes |

> ⚠ **Sobre el módulo de borrado.** La generación 5.0 incorpora capacidad de
> **destrucción**, no solo de cifrado. Un afiliado descontento, torpe o con
> instrucciones de sabotaje puede dejar datos irrecuperables **aunque se pague**.
> Esto debilita el argumento económico del pago y refuerza la decisión E-c: la
> recuperación debe descansar en respaldos verificados, no en la buena fe del actor.

## X-2. Artefactos de host persistentes entre builds

<!-- cti:cards -->

| Categoría | Artefactos | Etiqueta |
|---|---|---|
| **Nota de rescate** | `ReadMeForDecrypt.txt` en múltiples directorios, incluidos recursos compartidos y almacenes de respaldo | `impacto` |
| **Archivos cifrados** | Extensión aleatoria de 16 caracteres hexadecimales (p. ej. `.840d22e34b8e1f9e`); sin marcador final; tamaño original en el pie del archivo | `impacto` |
| **Servicios detenidos** | `VSS`, `vmms`, `WSearch`, `EdgeUpdate`, `BackupExecVSSProvider`, `VeeamTransportSvc`, `AcrSch2Svc` y 56 más identificados por hash CRC32 | `evasión` |
| **Registro de eventos** | EID 1102 (Security) y 104 (System) por `EvtClearLog`; **corte abrupto de eventos ETW** en procesos activos | `antiforense` |
| **Memoria** | Sección de código de `ntdll!EtwEventWrite` modificada con `0xC3`; `ntdll` desenganchada; proceso hospedador vaciado (hollowed) | `evasión` |
| **Sistema de archivos** | Contenido de `%TEMP%` eliminado antes del cifrado; espacio libre sobrescrito si se usó `-w`; binario autoeliminado salvo `-k` | `antiforense` |
| **ESXi** | Archivos atípicos en datastores (`_.sf_` observado para Cobalt Strike); SSH habilitado fuera de política; apagado masivo de máquinas virtuales | `virtualización` |
| **Linux** | Lecturas secuenciales de `/proc/self/status` y `/proc/ioports`; renombrado masivo de archivos sin tráfico de red asociado | `anti-análisis` |

## X-3. Lógica de detección prioritaria

<!-- cti:detections -->

**D-1 · CRÍTICO — Terminación coordinada de servicios de respaldo y sombra**

```
EID 7036 OR 7040
AND service_name IN ("VSS","vmms","WSearch","EdgeUpdate",
                     "BackupExecVSSProvider","VeeamTransportSvc","AcrSch2Svc")
AND count(distinct service_name) >= 3 WITHIN 5 minutes BY host
AND NOT host IN change_window_assets
```

→ **Contención automática sin escalado humano: aislar el host de inmediato.** Este
patrón precede al cifrado en minutos. Esperar validación humana consume la ventana
completa de reacción.

**D-2 · CRÍTICO — Parcheo de EtwEventWrite**

```
memory_write TARGET module="ntdll.dll" symbol="EtwEventWrite"
AND writing_process NOT IN (approved_debuggers, approved_edr_agents)
```

→ **Aislar el host y preservar volcado de memoria antes de reiniciar.** Sin el volcado,
la evidencia de esta técnica desaparece con el proceso.

**D-3 · CRÍTICO — Creación masiva de archivos con extensión aleatoria de 16 caracteres**

```
file_rename_or_create WHERE extension MATCHES "^\.[0-9a-f]{16}$"
AND count() > 500 WITHIN 60 seconds BY process_guid
```

→ **Matar el proceso y aislar el host automáticamente.** Es detección de última milla:
cada segundo de retraso equivale a archivos perdidos.

**D-4 · CRÍTICO — Administración no autorizada de hipervisor**

```
(esxi_ssh_session WHERE source_ip NOT IN admin_bastions)
OR (config_change WHERE setting="SSH" AND value="enabled")
OR (command MATCHES "esxcli vm process kill" AND count() > 5 WITHIN 10 minutes)
```

→ **Cortar la sesión, aislar la VLAN de gestión y escalar a guardia de infraestructura.**
Es el único punto donde se puede evitar el escenario de peor caso.

**D-5 · ALTO — Borrado de registros de eventos**

```
EID 1102 (Security) OR EID 104 (System)
AND NOT initiated_by IN (approved_maintenance_accounts)
```

→ Escalar a incidente de inmediato. **Requiere reenvío en tiempo real:** si el evento
solo se registra localmente, se borra junto con el resto.

**D-6 · ALTO — Aparición de la nota de rescate**

```
file_create WHERE file_name == "ReadMeForDecrypt.txt"
```

→ Declarar incidente mayor, activar el procedimiento de notificación a la **ANCI** y
congelar la infraestructura de respaldo. Fidelidad máxima, valor temporal mínimo.

**D-7 · ALTO — Desenganche de ntdll en espacio de usuario**

```
process_reads_file WHERE path ENDS_WITH "\\System32\\ntdll.dll"
AND SAME process LATER performs WriteProcessMemory ON module="ntdll.dll"
```

→ Aislar y analizar. Falsos positivos conocidos: agentes EDR de otros fabricantes,
empaquetadores comerciales, motores antitrampa. Requiere lista de excepciones curada.

**D-8 · MEDIO — Acceso a memoria de máquinas virtuales por proceso no autorizado**

```
file_read WHERE path MATCHES "\.(vmem|vmsn|vmss)$"
AND process NOT IN (approved_backup_platform, vmware_native_processes)
```

→ Escalar a caza. Es el precursor de la extracción de credenciales sin tocar el
sistema operativo invitado.

**D-9 · MEDIO — Exfiltración masiva desde servidor sin línea base de salida**

```
outbound_bytes > 1GB WITHIN 1 hour
AND source_host IN server_segment
AND destination NOT IN (approved_cloud_backup, corporate_saas)
```

→ Escalar a analista con contexto del host. Requiere línea base por host construida
previamente; sin ella, la regla es inoperable por volumen de falsos positivos.

> ⚠ **Regla de operación.** **D-1, D-3 y D-4 deben ejecutar contención automática sin
> escalado humano.** La justificación es aritmética: el cifrado por bloques de este
> actor procesa volúmenes grandes en minutos y no genera tráfico de red que permita
> detectarlo por otra vía. Un flujo de trabajo que requiera confirmación de un analista
> de turno noche llega, en el mejor de los casos, a documentar el desastre. La objeción
> legítima —el coste de aislar un servidor por un falso positivo— se responde con la
> curación de las listas de excepción (`change_window_assets`, `admin_bastions`), no
> con la desactivación de la respuesta automática.

## X-4. Consultas de caza

```kql
// H-3 · Terminación coordinada de servicios de respaldo y sombra (Defender XDR)
let objetivo = dynamic(["VSS","vmms","WSearch","EdgeUpdate",
                        "BackupExecVSSProvider","VeeamTransportSvc","AcrSch2Svc"]);
DeviceProcessEvents
| where Timestamp > ago(30d)
| where ProcessCommandLine has_any ("sc stop","sc  config","net stop","Stop-Service")
| where ProcessCommandLine has_any (objetivo)
| summarize servicios = dcount(ProcessCommandLine), muestras = make_set(ProcessCommandLine, 10)
    by DeviceName, AccountName, bin(Timestamp, 5m)
| where servicios >= 3
| order by Timestamp desc
```

```kql
// H-6 · Renombrado masivo hacia extensión aleatoria de 16 caracteres hexadecimales
DeviceFileEvents
| where Timestamp > ago(7d)
| where ActionType in ("FileRenamed","FileCreated")
| extend ext = tostring(extract(@"(\.[0-9a-f]{16})$", 1, FileName))
| where isnotempty(ext)
| summarize archivos = count(), extensiones = dcount(ext), inicio = min(Timestamp)
    by DeviceName, InitiatingProcessFileName, InitiatingProcessId
| where archivos > 500
| order by inicio asc
```

```kql
// H-7 · Nota de rescate, incluidos recursos compartidos y almacenes de respaldo
DeviceFileEvents
| where Timestamp > ago(30d)
| where FileName =~ "ReadMeForDecrypt.txt"
| project Timestamp, DeviceName, FolderPath, InitiatingProcessFileName, InitiatingProcessAccountName
| order by Timestamp asc
```

```kql
// H-5 · Borrado de registros de eventos, con detección de silencio posterior
DeviceEvents
| where Timestamp > ago(30d)
| where ActionType == "SecurityLogCleared" or AdditionalFields has "1102"
| join kind=leftouter (
    DeviceEvents
    | where Timestamp > ago(30d)
    | summarize ultimo_evento = max(Timestamp) by DeviceName
  ) on DeviceName
| project Timestamp, DeviceName, InitiatingProcessAccountName, ultimo_evento
| order by Timestamp desc
```

```bash
# H-10 · Acceso a memoria de máquinas virtuales desde el hipervisor (ESXi)
# Ejecutar contra el registro de shell del host; alertar sobre cualquier resultado
grep -E "\.(vmem|vmsn|vmss)" /var/log/shell.log /var/log/hostd.log \
  | grep -vE "vmx|hostd|vpxa|(plataforma de respaldo aprobada)"
```

```yaml
# Sigma — Parcheo de EtwEventWrite por proceso no autorizado
title: Parcheo de EtwEventWrite compatible con LockBit 5.0
id: 6a1f0c2e-7d3b-4a91-9c55-2f8e41b0d7aa
status: experimental
description: >
  Detecta la escritura en la sección de código de ntdll!EtwEventWrite, técnica
  empleada por el cifrador LockBit 5.0 (ChuongDong) para desactivar Event Tracing
  for Windows antes del cifrado. Requiere un EDR con visibilidad de modificación de
  memoria de módulo; Sysmon por sí solo no es suficiente.
author: Célula CTI
date: 2026-09-16
references:
  - CTI-2026-016
tags:
  - attack.defense_evasion
  - attack.t1562.006
logsource:
  product: windows
  category: process_access
detection:
  selection:
    TargetImage|endswith: '\ntdll.dll'
    GrantedAccess|contains:
      - '0x0008'   # VM_WRITE
      - '0x0020'   # VM_OPERATION
  filtro_legitimo:
    SourceImage|endswith:
      - '\windbg.exe'
      - '\vsdebugconsole.exe'
  condition: selection and not filtro_legitimo
falsepositives:
  - Depuradores y perfiladores legítimos
  - Agentes EDR de otros fabricantes y motores antitrampa
  - Empaquetadores comerciales de protección de software
level: high
```

```yaml
# Sigma — Terminación coordinada de servicios de respaldo previa al cifrado
title: Terminación coordinada de servicios de respaldo y sombra (LockBit 5.0)
id: 9c4d7b18-2e55-4f60-8a37-11d9c6e0b342
status: stable
description: >
  Tres o más servicios del conjunto de respaldo y sombra detenidos en menos de cinco
  minutos en un mismo host. Precede al cifrado en minutos. Debe ejecutar contención
  automática (véase D-1 de CTI-2026-016).
author: Célula CTI
date: 2026-09-16
tags:
  - attack.impact
  - attack.t1489
  - attack.t1490
logsource:
  product: windows
  service: system
detection:
  selection:
    EventID:
      - 7036
      - 7040
    ServiceName:
      - 'VSS'
      - 'vmms'
      - 'WSearch'
      - 'EdgeUpdate'
      - 'BackupExecVSSProvider'
      - 'VeeamTransportSvc'
      - 'AcrSch2Svc'
  condition: selection | count(ServiceName) by Computer > 2
  timeframe: 5m
falsepositives:
  - Ventanas de mantenimiento planificadas
  - Actualización simultánea de la suite de respaldo
level: critical
```

## X-5. Mitigaciones de configuración con efecto directo

| Control | Corta |
|---|---|
| Reenvío de registros de eventos de Windows en tiempo real fuera del host | Anula el efecto de `EvtClearLog`: la evidencia ya salió cuando el actor borra la copia local |
| Protección antimanipulación del EDR activada **y verificada en simulacro** | Eleva el coste del *unhooking* y del parcheo de ETW, y genera alerta donde antes había silencio |
| MFA resistente a phishing en todo acceso remoto, incluidos proveedores y cuentas de servicio | Corta la etapa 01 en su forma más común: credencial válida sin segundo factor |
| Eliminación de RDP expuesto a Internet; acceso solo por bastión | Corta simultáneamente el acceso inicial y la propagación lateral por T1021.001 |
| Plano de administración de virtualización segregado, con cuentas propias no federadas al dominio | Corta T1675: impide llegar al hipervisor con credenciales de dominio comprometidas |
| SSH deshabilitado por defecto en hosts ESXi, con alerta ante su habilitación | Corta el acceso interactivo al hipervisor y dispara D-4 |
| Respaldos inmutables, desconectados y **fuera del dominio de AD** | Neutraliza T1490 y la terminación de servicios de respaldo: no basta con tener respaldos, deben estar fuera del alcance de la credencial comprometida |
| Cuentas de servicio de respaldo sin privilegios de administrador de dominio | Rompe la ruta habitual desde el compromiso del servidor de respaldo hasta el dominio completo |
| Bloqueo de ejecución desde `%TEMP%` y rutas de usuario mediante WDAC o AppLocker | Eleva el coste de la etapa de carga del loader |
| Segmentación del tráfico SMB entre estaciones de trabajo | Corta T1021.002 y contiene la propagación del cifrador |
| Línea base de tráfico saliente por host, con alerta por desviación | Habilita H-8 y D-9: la última ventana de detección con margen real de reacción |
| Cobertura de EDR o telemetría equivalente en Linux y en hipervisores | Elimina el punto ciego donde la variante autónoma opera sin ninguna señal |

---

## 14. Brechas de inteligencia y nuevos requisitos de colección

| # | Brecha | Impacto en el juicio | Requisito propuesto | Prioridad |
|---|---|---|---|---|
| G-1 | **No existe vector de acceso inicial dominante ni conjunto de CVE atribuido a LockBit 5.0** en fuentes públicas | PIR-02 queda respondido solo parcialmente; §T-1 etapa 01 se sostiene sobre patrones del ecosistema, no sobre observación de este actor | Solicitar a proveedores de IR casuística desagregada por vector para intrusiones LockBit 5.0 posteriores a enero de 2026 | **Crítica** |
| G-2 | Sin serie mensual publicada de víctimas en 2026 | KJ-1 descansa en medias derivadas por diferencia de acumulados de fuentes con criterios distintos | Instrumentar recolección propia y diaria del sitio de filtración, con deduplicación documentada | Alta |
| G-3 | Sin mediana de permanencia (*dwell time*) para este actor | §T-1 no puede dimensionar la ventana de respuesta; los plazos de contención se fijan por analogía | Solicitar métricas de permanencia a proveedores de IR y a la aseguradora cibernética | Alta |
| G-4 | **Sin telemetría propia**: exposición, cobertura de EDR, superficie ESXi y visibilidad de ETW sin evaluar | §O-4 vacía. Ningún juicio de riesgo propio es calculable | Ejecutar el cuestionario de §O-4 y reemitir este informe como versión 2.0 | **Crítica** |
| G-5 | Una sola víctima chilena identificada, de fuente comercial única | KJ-6 se emite con confianza moderada cuando el hecho podría verificarse | Consultar al CSIRT Nacional y a CronUp por actividad LockBit 5.0 en Chile; contrastar con el sitio de filtración | Alta |
| G-6 | Sin verificación de transferencia técnica dentro de la coalición | KJ-7 se emite con confianza baja y H4 permanece abierta en paralelo | Vigilancia dirigida sobre I-3: primera aparición de BYOVD en intrusión LockBit | Media |
| G-7 | Proporción desconocida de incidentes de marca LockBit atribuibles a terceros con builders filtrados | Contamina toda estadística de victimología (H3) | Verificar, en cada caso de interés, la generación del cifrador por esquema criptográfico antes de atribuir | Media |
| G-8 | Sin visibilidad de la economía de la operación posterior a mayo de 2025 | §O-3 usa cifras de rescate anteriores al lanzamiento de la versión 5.0 | Monitorizar análisis de blockchain sobre carteras asociadas al nuevo programa | Baja |

---

# ANEXOS

## Anexo A — Indicadores de compromiso

> ⚠ **Leer antes de usar.** Los IOC son el nivel más perecedero y menos valioso del
> producto, y en **este actor en particular valen menos de lo habitual**: cada afiliado
> compila su propia variante desde el panel —hay builds datadas cada pocas semanas— y
> el cifrado **no genera tráfico de red**, por lo que no existe infraestructura de C2
> que bloquear durante el impacto. Los hashes sirven para **retrohunt**, no para
> defensa. El valor real de este informe está en §T-4 y §X-3.

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Acción permitida |
|---|---|---|---|---|
| sha256 | `7ea5afbc166c4e23498aa9747be81ceaf8dad90b8daa07a6e4644dc7c2277b82` | Cifrador LockBit 5.0, muestra Windows | Alta | Bloqueo y retrohunt |
| sha256 | `180e93a091f8ab584a827da92c560c78f468c45f2539f73ab2deb308fb837b38` | Cifrador LockBit 5.0, muestra Windows | Alta | Bloqueo y retrohunt |
| sha256 | `4dc06ecee904b9165fa699b026045c1b6408cc7061df3d2a7bc2b7b4f0879f4d` | Cifrador LockBit 5.0, muestra Linux (ELF, autónoma) | Alta | Bloqueo y retrohunt |
| sha256 | `90b06f07eb75045ea3d4ba6577afc9b58078eafeb2cdd417e2a88d7ccf0c0273` | Cifrador LockBit 5.0, muestra Linux/ESXi | Alta | Bloqueo y retrohunt |
| sha256 | `98d8c7870c8e99ca6c8c25bb9ef79f71c25912fbb65698a9a6f22709b8ad34b6` | Cifrador LockBit 5.0, muestra Linux/ESXi | Alta | Bloqueo y retrohunt |
| md5 | `95daa771a28eaed76eb01e1e8f403f7c` | Muestra LockBit 5.0 (ASEC) | Moderada | Retrohunt |
| md5 | `97e97e8cde5cc795b4d0a1fb7202b5ed` | Muestra LockBit 5.0 (ASEC) | Moderada | Retrohunt |
| md5 | `c15a79d4b3c17bdb01edb097bae53212` | Muestra LockBit 5.0 (ASEC) | Moderada | Retrohunt |
| md5 | `c462c6b02b35df2910689947c5090fae` | Muestra LockBit 5.0 (ASEC) | Moderada | Retrohunt |
| md5 | `cd6e182fe655724f3d8e711b451a2e93` | Muestra LockBit 5.0 (ASEC) | Moderada | Retrohunt |
| filename | `ReadMeForDecrypt.txt` | Nota de rescate, constante en Windows, Linux y ESXi. **El artefacto de mayor fidelidad de esta lista** | Alta | Detección y alerta |
| pattern | `^\.[0-9a-f]{16}$` | Extensión aleatoria de 16 caracteres hexadecimales de los archivos cifrados | Alta | Detección y alerta |
| filename | `_.sf_` | Cobalt Strike observado con este nombre en almacenes de datos ESXi | Moderada | Detección; **verificar contexto antes de bloquear** |
| mutex | `<variable por build>` | La versión 5.0 introduce mutex configurable; **no hay valor constante publicado**. Desactivable con `-nomutex` | Baja | Solo contexto |

**IOC históricos — no aplicar a la versión 5.0**

| Tipo | Valor | Contexto | Confianza | Acción permitida |
|---|---|---|---|---|
| sha256 | `385D4FBD3A3AAB0CFE109F0EB2626863B91EC02CEAA4C3E4C104F63CA6DC0C93` | `123.cmd` — **LockBit Black (3.0)**, ataque al Poder Judicial de Chile, 2022. CSIRT Nacional | Alta | Solo retrohunt histórico |
| sha256 | `0DA8CFBA645951768B16DB7707ED2C75BBBB2E396E7DA6DA71A9DCA6EF35DF17` | `injector.exe` — LockBit Black (3.0), 2022. CSIRT Nacional | Alta | Solo retrohunt histórico |
| sha256 | `5EF365469867CB30F5094D668E596819BF7163411E2A92CC1D7BD117FCD11BFE` | `lbb.dll` — LockBit Black (3.0), 2022. CSIRT Nacional | Alta | Solo retrohunt histórico |

*Nota de higiene:* no se incluyen direcciones IP ni dominios porque **este actor no
los usa durante el impacto**; la negociación vive en Tor y la exfiltración se apoya en
servicios de almacenamiento legítimos —bloquearlos por su aparición en un incidente
tiene alto riesgo de impacto operativo—. Los hashes de las muestras públicas **no
cubren las variantes compiladas por cada afiliado**: úsense para retrohunt, nunca como
medida de protección principal.

## Anexo B — Fuentes y valoración

> Valoración doble tipo Admiralty/OTAN: **fiabilidad de la fuente (A–F)** ×
> **credibilidad de la información (1–6)**. Se valoran por separado.

| Fuente | Disciplina | Fiabilidad | Credibilidad | Notas de sesgo |
|---|---|---|---|---|
| CSIRT Nacional de Chile | CERT nacional | A | 1 | Solo cubre el incidente de 2022 (LockBit Black); no hay alerta pública sobre la versión 5.0 |
| National Crime Agency (Operación Cronos, sanción de Khoroshev) | Gubernamental | A | 1 | Interés institucional en subrayar el éxito de la disrupción |
| Check Point Research (*State of Ransomware* Q1 y Q2 2026) | OSINT comercial | B | 2 | Serie trimestral consistente; criterios de deduplicación no publicados en detalle |
| Trend Micro / TrendAI Security (análisis de binario 5.0) | TECHINT de proveedor | B | 1 | Análisis de muestra verificable; interés comercial en dramatizar |
| LevelBlue / SpiderLabs (análisis de binario 5.0) | TECHINT de proveedor | B | 1 | Coincide de forma independiente con Trend Micro y ASEC |
| ASEC / AhnLab (análisis de binario y servicios terminados) | TECHINT de proveedor | B | 1 | Detalle de servicios y umbrales de cifrado; visibilidad sesgada hacia Corea |
| S2W TALON (análisis detallado 5.0) | TECHINT de proveedor | B | 2 | No accesible directamente en esta colección; citado a través de referencias secundarias |
| Análisis independiente de la variante Linux (netacoding) | TECHINT independiente | C | 2 | Metodología publicada y reproducible; autor individual sin revisión por pares |
| MOXFIVE (*Threat Actor Spotlight*) | TECHINT de IR | B | 2 | Basado en casos reales de respuesta; muestra sesgada hacia sus clientes |
| Flare (panel de afiliados filtrado) | CLOSINT comercial | B | 3 | Material filtrado de valor alto; no verificable de forma independiente |
| Halcyon (ficha de actor, acumulados) | OSINT comercial | B | 3 | Cifras de acumulado sin metodología publicada |
| ransomware.live | OSINT agregador | B | 2 | Recolección automatizada verificable; deduplicación propia no auditable |
| Breachsense (informes mensuales del ecosistema) | OSINT comercial | B | 2 | Serie mensual continua; discrepa de otros trackers hasta un 5 % |
| Analyst1, Trellix, TRM Labs, Qualys (filtración del panel, mayo de 2025) | OSINT / CLOSINT | B | 2 | Coinciden sobre cifras económicas; los datos proceden del propio adversario |
| CronUp (monitorización de ransomware en Chile) | OSINT regional | B | 2 | Mejor visibilidad nacional disponible; recolección manual, posible subregistro |
| DeXpose (reivindicación de Red Dávila) | OSINT comercial | C | 3 | **Fuente única sin corroboración**; base de KJ-6, declarada como tal |
| WeLiveSecurity / ESET (cobertura LATAM) | OSINT de proveedor | B | 3 | Buena cobertura regional; cifras agregadas sin desglose metodológico |
| Cybernews, CSO Online, Dark Reading, Quorum Cyber (coalición) | OSINT periodístico | C | 3 | Todas remiten a la misma publicación original en foro; corroboración aparente, no real |
| Proven Data (TTP y mitigaciones 5.0) | OSINT comercial | C | 3 | Compilación de terceros; porcentajes de vector sin muestra declarada |
| Sitio de filtración de LockBit 5.0 | CLOSINT | C | 4 | **El actor controla el mensaje**: publica lo que le conviene, cuando le conviene |
| Foro RAMP (anuncios del actor) | CLOSINT | C | 4 | Material promocional del adversario dirigido a reclutar |

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

> Usar siempre el término **y** el porcentaje. No usar «podría» ni «es posible» como
> juicio: son afirmaciones no falsables.

## Anexo D — Marcos de referencia empleados

`MITRE ATT&CK v18` · `MITRE D3FEND` · `Modelo del Diamante` · `Cyber Kill Chain` ·
`Pirámide del Dolor` · `F3EAD` · `ICD 203` · `ACH, KAC, pre-mortem` · `TLP 2.0` ·
`PAP` · `STIX 2.1 / TAXII 2.1` · `Admiralty Code` · `Ley 21.663 (Chile) y marco ANCI`

## Anexo E — Paquete legible por máquina

- Bundle STIX 2.1: pendiente de generar (véase §14, G-2)
- Evento MISP: pendiente — taxonomías previstas: `tlp`, `admiralty-scale`, `estimative-language`, `PAP`
- Reglas Sigma de §X-4: pendientes de commit en el repositorio de detección
- Consultas KQL de §X-4: pendientes de despliegue como detecciones programadas

## Anexo F — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| **1.2** | **2026-11-21** | **Alineamiento con MITRE ATT&CK v20.1.** ATT&CK reorganizó la matriz y este informe citaba identificadores que la fuente ha **revocado**: `T1070.001`, `T1562.001`, `T1562.006` → `T1685`, `T1685.005`. Son referencias que un `Tnnnn` bien formado no delata y que se copian de informes viejos. **Dos filas se funden en una:** `T1562.001` y `T1562.006` van las dos a `T1685`; se conservan la terminación de 63 servicios por CRC32 y el cegado del canal de telemetría (`EtwEventWrite`, *unhooking*, AMSI). **No se extiende `caduca`: se ha puesto al día la nomenclatura de los TTP, no revalidado ningún juicio.** Lo comprueba en adelante la familia `G7` de `tools/cti_gate.py` contra el catálogo oficial | Célula CTI |
| 1.0 | 2026-09-16 | Emisión inicial | Célula CTI |
| 1.1 | 2026-11-16 | **Reclasificación de TLP:AMBER a TLP:CLEAR** por decisión del emisor, para publicación en el repositorio abierto `cti_daily`. Verificado previamente que el documento no contiene referencias a la organización emisora ni a marcas asociadas, telemetría propia, direccionamiento interno, nombres de personas ni datos de terceros. **Sin cambios en los juicios analíticos ni en los indicadores.** Se mantiene PAP:AMBER | Célula CTI |

## Anexo G — Realimentación del consumidor

| Pregunta | Respuesta |
|---|---|
| ¿Respondió a su requisito? | |
| ¿Qué decisión tomó o cambió con este informe? | |
| ¿Qué faltó? | |
| ¿Llegó a tiempo? | |

> Sin este anexo devuelto, el ciclo de inteligencia queda abierto y el próximo
> producto no mejora.
