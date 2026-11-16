---
tlp: "TLP:CLEAR"
pap: "PAP:AMBER"
id: "CTI-2026-015"
version: "1.1"
tipo: "Perfil de actor + informe de campaña"
foco_regional: "Chile · Latinoamérica"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "Qilin (Agenda · Storm-1934)"
fecha: "2026-09-16"
caduca: "2026-12-16"
autor: "Célula CTI"
"Reclasificado a TLP:CLEAR el 2026-11-16 por decisión del emisor. Elaborado sin telemetría propia ni datos de cliente: no contiene información identificable de la organización emisora ni de terceros. Difusión libre, conservando la atribución de las fuentes y las salvedades metodológicas del informe. Se mantiene PAP:AMBER: los indicadores del Anexo A llevan acción permitida individual y no deben cargarse en bloqueo automático sin verificación previa contra telemetría propia."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-015
## Qilin (Agenda / Storm-1934): el RaaS dominante del ecosistema, con acceso por borde de red y neutralización de EDR a nivel de kernel
### Con evaluación de actividad confirmada en Chile bajo el régimen de la Ley 21.663

> **Regla de oro del producto:** todo párrafo debe responder a un requisito de
> inteligencia (PIR) y habilitar una decisión. Si un párrafo no cambia lo que
> alguien va a hacer, va al anexo o se borra.

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-015` |
| Versión / fecha | `1.1` — 2026-09-16 |
| Tipo de producto | Perfil de actor + informe de campaña |
| Niveles cubiertos | Estratégico · Operacional · Táctico · Técnico |
| Foco regional | Chile · Latinoamérica |
| Marcado de difusión | `TLP:CLEAR` · `PAP:AMBER` |
| Clasificación interna | Público — apto para difusión abierta |
| Requisitos atendidos | `PIR-01`, `PIR-02`, `PIR-04`, `PIR-07` |
| Solicitante / consumidor primario | CISO · Jefatura de SOC · Comité de Riesgo Operacional |
| Ventana de observación | 2025-04-01 → 2026-09-16 |
| Base de colección | 24 fuentes externas todo-fuente (OSINT, TECHINT de proveedor, CERT nacional, CLOSINT derivado de sitio de filtración). **Sin telemetría propia incorporada** |
| Autor (analista) | Célula CTI |
| Revisión por pares | Pendiente |
| Aprobación | Pendiente |
| Caducidad / revisión | 2026-12-16, o antes si se confirma acción policial, rebranding o cambio de esquema criptográfico |
| Productos relacionados | `CTI-2026-014` (TheGentlemen) — complementa: ambos actores compiten por el mismo nicho y comparten vector de borde |
| Paquete legible por máquina | Pendiente de generar (véase §14) |

<!-- cti:note type="warn" -->

> **Limitación estructural de este producto.** Se ha elaborado exclusivamente con
> fuentes abiertas, de proveedor y del CERT nacional. No incorpora telemetría de la
> organización, por lo que **la sección de exposición propia (§O-4) está sin
> rellenar** y todo juicio sobre riesgo para nosotros es condicional, no evaluado.
> Un informe con §O-4 vacía es inteligencia genérica, no inteligencia propia.

<!-- cti:note type="warn" -->

> **Nota sobre la denominación «APT».** El requisito se formuló como «APT Qilin».
> Qilin **no es un actor de amenaza persistente avanzada con patrocinio estatal**:
> es una operación criminal de ransomware-como-servicio con ánimo de lucro.
> La distinción no es pedante —cambia el modelo de motivación, el horizonte
> temporal y las opciones de disuasión—. El matiz relevante se trata en §O-2:
> en 2025 un actor estatal norcoreano (Moonstone Sleet) desplegó Qilin como
> afiliado, lo que difumina la frontera sin convertir a Qilin en un APT.

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** Qilin es **la operación de ransomware más activa del mundo y lo ha sido de
forma sostenida durante cinco trimestres consecutivos**, con 1.358 víctimas
reivindicadas entre abril de 2025 y marzo de 2026 —un crecimiento del 443 %
interanual— y un acumulado histórico próximo a las 2.100 organizaciones desde 2022.
Valoramos **casi con certeza** *(95–99 %)* que siga operativa durante los próximos
seis meses en ausencia de acción policial.
**Confianza: alta.** *Base:* concordancia de seis trackers independientes (Black Kite, Check Point, Emsisoft, Breachsense, Halcyon, Cyble) sobre el liderazgo, pese a discrepancias de ±5 % en las cifras absolutas.

**KJ-2.** El vector de acceso inicial dominante es **el borde de red: dispositivos
perimetrales sin parchear y portales VPN sin MFA**. En 2026 el actor ha encadenado
al menos tres vulnerabilidades de omisión de autenticación en appliances —PAN-OS
(CVE-2026-0257), Check Point Remote Access VPN (CVE-2026-50751) y el histórico Veeam
(CVE-2023-27532)— y complementa la explotación con fuerza bruta sobre SSL-VPN
Fortinet y WatchGuard. Valoramos **muy probable** *(80–95 %)* que una intrusión de
este actor contra nosotros comenzara por esa vía.
**Confianza: alta.** *Base:* Arctic Wolf (A-2, telemetría de IR), Picus, MOXFIVE y CSIRT Nacional de Chile coinciden de forma independiente.

**KJ-3.** Qilin dispone de un **módulo de neutralización de EDR que opera en el
kernel mediante controladores vulnerables firmados (BYOVD) y es capaz de desactivar
más de 300 productos de detección**, prácticamente todo el mercado. El módulo se
ejecuta íntegramente en memoria, suprime ETW y actúa **antes** de la exfiltración y
del cifrado. Esto está **confirmado por análisis de binario de Cisco Talos**
(2 de abril de 2026). **Confianza: alta.**
*Implicación de doctrina:* **no podemos asumir que el EDR estará vivo para contar la historia**. La detección debe apoyarse también en fuentes que el endpoint no controla: telemetría de red, identidad y registro de eventos centralizado con reenvío en tiempo real.

**KJ-4.** El actor **ejecuta cifradores ELF de Linux dentro del Subsistema de Windows
para Linux (WSL)** para operar en un espacio que la mayoría de los EDR centrados en
Windows no inspecciona con la misma fidelidad. Valoramos **probable** *(55–80 %)*
que nuestra pila de detección actual tenga una brecha de visibilidad en WSL.
**Confianza: moderada.** *Base:* CybelAngel y MOXFIVE describen la técnica; no hemos validado nuestra propia cobertura —es una hipótesis a falsar, no un hecho verificado sobre nosotros—.

**KJ-5.** La **ventana entre acceso inicial e impacto es de 3 a 6 días**, más holgada
que la de competidores como TheGentlemen (mediana ≈ 2 días), pero el actor dedica ese
tiempo a **destruir respaldos y exfiltrar antes de cifrar**. Valoramos **probable**
*(55–80 %)* que un proceso de respuesta que solo se active con el cifrado llegue
cuando el daño reputacional y regulatorio ya es irreversible.
**Confianza: moderada.** *Base:* MOXFIVE (3–5 días) y Cisco Talos (≈ 6 días en telemetría de Japón); ambas cifras son medianas de proveedor, no de telemetría propia.

**KJ-6.** **Qilin opera en Chile con víctimas confirmadas y con al menos un incidente
de efecto significativo sobre una entidad estratégica** notificado por el CSIRT
Nacional el 29 de enero de 2026 bajo el régimen de la Ley 21.663. El contexto agrava
el juicio: **agosto de 2026 fue el peor mes de ransomware registrado en Chile**
—al menos diez organizaciones afectadas— y los ocho primeros meses del año ya superan
cualquier año completo anterior. Valoramos **muy probable** *(80–95 %)* que la presión
sobre organizaciones chilenas se mantenga o aumente en el próximo trimestre.
**Confianza: alta.** *Base:* alerta oficial del CSIRT Nacional/ANCI (A-2) y monitorización de CronUp, corroboradas por SOCRadar y DeXpose.

**KJ-7.** La caída de volumen de junio de 2026 —cuando Qilin perdió el primer puesto
por primera vez en el año— **fue coyuntural, no estructural**: en agosto recuperó y
superó su máximo con 157 víctimas. Valoramos **poco probable** *(20–45 %)* que la
presión económica sobre los afiliados (tasa de pago en mínimo histórico, ~23 %)
degrade la operación en los próximos seis meses.
**Confianza: moderada.** *Base:* serie mensual de un único tracker (Breachsense, B-2); la interpretación económica procede de Halcyon y Group-IB y no está corroborada por evidencia interna del actor.

**KJ-8.** **Ningún gobierno ha emitido atribución formal, sanción ni acusación contra
Qilin a la fecha de este informe**, y el actor ha ampliado su plataforma con
extorsión multicanal (DDoS integrado, «Call Lawyer», periodistas internos, chatbot
de negociación). Valoramos **posibilidad real** *(45–55 %)* de rebranding o pivote de
infraestructura en los próximos 12 meses, lo que **invalidaría los indicadores
técnicos de este informe pero no sus TTP**.
**Confianza: baja.** *Base:* razonamiento por analogía con LockBit y ALPHV, no por observación directa. Se consigna marcado como especulativo.

**Qué cambiaría estos juicios:** (a) una detención, incautación o sanción confirmada
por autoridades; (b) la aparición de un cifrador con un esquema criptográfico distinto
bajo la misma marca —indicaría cambio de desarrollador—; (c) observación de acceso
inicial por phishing masivo o por cadena de suministro de software, que contradiría
el modelo actual centrado en borde de red y credenciales; (d) la publicación de un
descifrador gratuito, que colapsaría la economía del programa de afiliados.

---

## 2. Resumen ejecutivo

Qilin es un grupo criminal de habla rusa, con ánimo exclusivamente de lucro, que
opera desde julio de 2022 y que hoy concentra **entre una de cada seis y una de cada
ocho víctimas de ransomware publicadas en todo el mundo**. No es un actor estatal ni
persigue objetivos de espionaje: persigue dinero, y ha industrializado el proceso de
obtenerlo. Su ventaja competitiva descansa en tres decisiones de negocio y una
capacidad técnica.

Primera decisión: **paga a sus afiliados entre el 80 % y el 85 % del rescate**, lo que
le permitió absorber operadores experimentados cuando LockBit y ALPHV colapsaron entre
2024 y 2025. Segunda: **vende algo más que cifrado**. Su panel de afiliados incorpora
ataques de denegación de servicio contra el sitio web de la víctima, un equipo de
«periodistas» que redacta publicaciones de escarnio, un chatbot que negocia solo,
una herramienta de spam contra los correos y teléfonos corporativos de la víctima y
un botón «Call lawyer» que pone a un abogado en la sala de negociación —porque, en
palabras del propio actor, «la mera aparición de un abogado en el chat presiona a la
empresa y eleva el rescate»—. Tercera: **coopera con sus rivales**; desde septiembre
de 2025 mantiene una coalición con LockBit 5.0 y DragonForce para compartir técnicas
e infraestructura.

La capacidad técnica es la que debe preocupar al nivel operativo: **Qilin apaga el
EDR desde el kernel antes de hacer nada más**. Su módulo de cuatro etapas carga en
memoria dos controladores firmados y vulnerables, y desactiva más de trescientos
productos de detección. Cuando llega el cifrado, la organización lleva días sin
telemetría fiable de endpoint y, con frecuencia, sin respaldos: el actor los busca
y los destruye de forma deliberada, incluidas cintas y trabajos programados de Veeam.

Para nosotros, el asunto no es hipotético. El CSIRT Nacional atribuyó a Qilin un
incidente de efecto significativo contra una entidad estratégica chilena en enero de
2026, y el actor ha publicado al menos ocho víctimas chilenas identificables en lo que
va de año. Bajo la Ley 21.663, un incidente de esta naturaleza activa obligaciones de
notificación a la ANCI con plazos medidos en horas, no en días.

<!-- cti:cards -->

| Rasgo | Qué significa | Etiqueta |
|---|---|---|
| Neutraliza el EDR a nivel de kernel antes de actuar | Nuestra principal fuente de detección puede estar muerta cuando más la necesitamos. La defensa no puede descansar en un único plano de telemetría | `01 · detección` |
| Entra por el perímetro, no por el correo | La formación antiphishing no nos protege de este actor. El control que sí lo hace es el parcheo del borde y el MFA resistente a phishing | `02 · superficie` |
| Destruye respaldos antes de cifrar | La capacidad de recuperación se decide semanas antes del ataque, con respaldos inmutables y desconectados, no durante la crisis | `03 · continuidad` |
| Extorsión multicanal: DDoS, prensa, abogados, spam | El coste de un incidente no es solo el rescate; es una campaña coordinada de presión pública y regulatoria contra nosotros | `04 · reputación` |
| Actividad confirmada en Chile bajo Ley 21.663 | Un incidente de este actor contra un OIV/PSE activa obligaciones legales de notificación con plazos cortos | `05 · regulatorio` |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `1.358` | Víctimas reivindicadas entre abril de 2025 y marzo de 2026 | +443 % interanual; el mayor crecimiento del ecosistema |
| `157` | Víctimas publicadas solo en agosto de 2026 | Su máximo mensual histórico, en el mes récord global (964 víctimas, 83 grupos) |
| `300+` | Productos EDR que su módulo BYOVD puede desactivar | Prácticamente todo el mercado de detección de endpoint |
| `85 %` | Porción del rescate que se queda el afiliado | Frente al 70–80 % habitual del sector: por eso capta operadores |
| `8` | Víctimas chilenas identificables publicadas en 2026 | Más un incidente de efecto significativo notificado por el CSIRT Nacional |
| `23 %` | Tasa de pago de rescates en el ecosistema | Mínimo histórico: presiona al actor hacia más volumen y más presión |

> ✅ **Decisión que se solicita a Dirección:** (a) autorizar una ventana de parcheo de
> emergencia para todo appliance de borde expuesto a Internet, con plazo de 15 días;
> (b) aprobar el despliegue de MFA resistente a phishing en el 100 % de los accesos
> VPN y administrativos, con plazo de 60 días; (c) financiar la verificación
> trimestral de restauración desde respaldos inmutables y desconectados, con la
> primera prueba ejecutada antes de 45 días; (d) instruir a Legal y Comunicaciones la
> preparación del procedimiento de notificación a la ANCI y del guion de respuesta a
> extorsión multicanal, con plazo de 30 días.

---

## 3. Alcance, requisitos y limitaciones

**3.1 Requisitos de inteligencia atendidos**

| Req. | Enunciado | ¿Respondido? | Dónde |
|---|---|---|---|
| PIR-01 | ¿Qué actores tienen intención y capacidad contra nuestro sector y geografía? | Sí | §E-1, §E-2, §O-2 |
| PIR-02 | ¿Cuál es el vector de acceso inicial más probable contra nuestra superficie expuesta? | Sí | §KJ-2, §T-1, §T-2 |
| PIR-04 | ¿Qué capacidades adversarias invalidan controles que hoy damos por eficaces? | Sí | §KJ-3, §X-2, §X-3 |
| PIR-07 | ¿Qué obligaciones regulatorias se activan ante un incidente de este actor en Chile? | Parcial | §E-4, §14 |
| — | ¿Estamos ya comprometidos? | **No** — requiere telemetría propia | §O-4 |

**3.2 Fuera de alcance.** No se evalúa la exposición concreta de la organización
(inventario, versiones, cobertura de EDR), no se analiza el impacto financiero
cuantificado de un escenario de cifrado, y no se cubren otros actores que compiten
por el mismo nicho salvo por comparación —TheGentlemen se trata en `CTI-2026-014`—.
Tampoco se evalúa la conveniencia de pagar un rescate: es una decisión de Dirección
con asesoría legal, no un juicio de inteligencia.

**3.3 Limitaciones de la colección.** (a) Todas las cifras de víctimas proceden de
sitios de filtración **controlados por el adversario**: miden lo que el actor decide
publicar, no lo que ocurre; las víctimas que pagan rara vez aparecen. (b) Los trackers
difieren entre sí hasta un 5 % por criterios distintos de deduplicación y de fecha de
corte —Check Point contabiliza 338 víctimas en el primer trimestre de 2026 donde
Breachsense contabiliza 342—; en este informe se usa la serie de Breachsense por ser
la única mensual continua, y se declara la discrepancia. (c) No hay visibilidad de la
economía interna del actor: las cifras de reparto con afiliados proceden de anuncios
en foros, es decir, de material promocional del propio adversario. (d) Ventana ciega:
septiembre de 2026 está incompleto al cierre de este informe. (e) Sin telemetría
propia, según §0.

**3.4 Metodología.** Disciplinas empleadas: OSINT, OSINT comercial de proveedor,
CLOSINT derivado del sitio de filtración adversario y reporte de CERT nacional
(véase Anexo B). Técnicas analíticas estructuradas aplicadas: análisis de hipótesis
competidoras (§O-6), verificación de supuestos clave y pre-mortem (§O-6). Marcos de
referencia en el Anexo D. Léxico estimativo conforme a ICD 203 (Anexo C).

---

# NIVEL ESTRATÉGICO
### Para: Consejo · CISO · Riesgo · Legal · Horizonte: 6–24 meses

## E-1. Qué representa este actor en el panorama

Qilin es el resultado de una consolidación: el ecosistema de ransomware pasó de 85
grupos activos en el tercer trimestre de 2025 a 71 en el primero de 2026, y los diez
mayores concentran hoy el 71 % de todas las víctimas. Qilin es el mayor de todos.

<!-- cti:cards -->

| Cambio estructural | Por qué nos afecta | Etiqueta |
|---|---|---|
| **Consolidación del mercado criminal.** Los operadores huérfanos de LockBit, ALPHV y RansomHub se reagruparon bajo pocas marcas grandes | Enfrentamos menos adversarios, pero mejor equipados y más profesionales. La probabilidad de encontrarnos con un afiliado inexperto baja | `01 · mercado` |
| **Cooperación entre rivales.** Coalición Qilin–LockBit 5.0–DragonForce desde septiembre de 2025 para compartir técnicas e infraestructura | Una TTP observada en un grupo se propaga a los otros en semanas. La inteligencia sobre un actor ya no es específica de ese actor | `02 · difusión de TTP` |
| **La superioridad del defensor en el endpoint se erosiona.** El BYOVD a nivel de kernel neutraliza el control en el que más hemos invertido | Obliga a rediseñar la arquitectura de detección hacia múltiples planos independientes, no a comprar otro EDR | `03 · doctrina` |
| **Extorsión convertida en campaña de presión.** DDoS, prensa, abogados y spam integrados en el panel del afiliado | El incidente deja de ser técnico y pasa a ser simultáneamente de continuidad, legal, regulatorio y reputacional desde la primera hora | `04 · naturaleza del daño` |
| **La frontera criminal-estatal se difumina.** Moonstone Sleet (RPDC) usó Qilin como afiliado en 2025 | Un mismo cifrador puede servir a un objetivo de lucro o a uno de financiamiento estatal. La atribución por herramienta es menos fiable que nunca | `05 · atribución` |
| **Tasa de pago en mínimo histórico (23 %).** Menos víctimas pagan | El actor compensa con volumen y con más presión por víctima. Que paguemos menos como industria **no** reduce la probabilidad de ser atacados a corto plazo | `06 · economía` |

## E-2. Victimología

<!-- cti:bars title="Sectores más golpeados por Qilin (% de víctimas, 2026)" -->

| Sector | % |
|---|---|
| Manufactura y producción | 19.5 |
| Tecnologías de la información | 10.7 |
| Servicios profesionales, científicos y técnicos | 8.3 |
| Construcción e ingeniería | 7.0 |
| Salud | 6.2 |
| Comercio y hostelería | 5.4 |

<!-- cti:bars title="Víctimas acumuladas de Qilin por sector (valores absolutos, a junio de 2026)" -->

| Sector | Víctimas |
|---|---|
| Manufactura | 291 |
| Servicios de negocio | 245 |
| Salud | 168 |

<!-- cti:bars title="Concentración geográfica del ecosistema (% de víctimas publicadas, julio de 2026)" -->

| País | % |
|---|---|
| Estados Unidos | 40.7 |
| Alemania | 5.9 |
| Canadá | 4.4 |
| Resto del mundo | 49.0 |

> **Lectura clave.** La distribución sectorial **no describe una preferencia del
> adversario, sino el mapa de qué industrias usan el software vulnerable que sabe
> explotar**. Manufactura, construcción y salud encabezan la lista porque operan
> perímetros heredados, ventanas de mantenimiento estrechas y tecnología que no se
> puede parchear en caliente. No estamos protegidos por ser quienes somos: estamos
> expuestos en la medida en que nuestro borde de red se parezca al de esas víctimas.
> El actor opera en más de cincuenta países y la concentración en EE. UU. refleja
> densidad de objetivos, no una exclusión geográfica.

**Presencia confirmada en Chile.** Qilin ha publicado en 2026 al menos las siguientes
organizaciones chilenas: Valbifrut, Ducasse Comercial Ltda., Conectados Chile S.A.,
Graneles de Chile y Noi Hotels (entre enero y marzo), Servitelco (30 de julio) y
Difor (23 de agosto). A ello se suma un incidente de efecto significativo contra una
entidad estratégica no identificada, notificado por el CSIRT Nacional el 29 de enero
de 2026. Una fuente comercial adicional reporta a AGUNSA como víctima en 2026; **no
ha sido posible corroborar la fecha ni el alcance, y se consigna con confianza baja**.

## E-3. Tendencia y pronóstico

<!-- cti:chart title="Víctimas publicadas por Qilin, mes a mes en 2026" cap="Fuente: serie mensual de Breachsense. Los recuentos proceden del sitio de filtración controlado por el adversario: son un indicador de tendencia y de intención de publicar, no un recuento de organizaciones comprometidas. Septiembre está incompleto y se omite." -->

| Periodo | Víctimas |
|---|---|
| Ene | 107 |
| Feb | 104 |
| Mar | 131 |
| Abr | 103 |
| May | 101 |
| Jun | 71 |
| Jul | 119 |
| Ago | 157 |

La lectura de la serie importa más que cualquier punto aislado. Ocho meses
consecutivos por encima de las cien víctimas —salvo junio— **no es una campaña: es
capacidad industrial sostenida**. La caída de junio coincidió con la única pérdida
del primer puesto en el año, frente a TheGentlemen; la recuperación de julio y el
máximo histórico de agosto indican que fue una fluctuación operativa, probablemente
ligada al ciclo de publicación, y no una degradación de la operación.

<!-- cti:cards -->

| Escenario | Desarrollo | Etiqueta |
|---|---|---|
| **Continuidad con crecimiento moderado** | Qilin conserva el liderazgo, mantiene una media mensual de 110–150 víctimas y sigue rotando vulnerabilidades de borde a medida que se publican. La presión sobre Chile crece en línea con la tendencia regional | `Probable · 55–80 %` |
| **Estancamiento por presión económica** | La tasa de pago del 23 % erosiona el ingreso por víctima; los afiliados migran a programas con mejor conversión o a extorsión sin cifrado. El volumen cae pero la operación sobrevive | `Poco probable · 20–45 %` |
| **Rebranding o pivote de infraestructura** | El actor cambia de marca ante presión policial o reputacional, conservando afiliados y TTP. Los IOC de este informe caducan de golpe; las TTP siguen vigentes | `Posibilidad real · 45–55 % (a 12 meses)` |
| **Disrupción policial efectiva** | Detención, incautación o sanción internacional. A la fecha no existe ninguna acción pública contra Qilin, pese a cinco trimestres de liderazgo | `Remoto · 5–15 %` |
| **Escalada a objetivo de alto impacto social en Chile** | Un ataque contra un OIV de salud, energía o telecomunicaciones con interrupción de servicio a la población, con el precedente de Synnovis en el Reino Unido | `Poco probable · 20–45 %, alto impacto` |

## E-4. Decisiones que este informe pide al nivel estratégico

<!-- cti:table highlight="ANCI|Ley 21.663|CSIRT|regional" -->

| # | Decisión | Fundamento | Plazo |
|---|---|---|---|
| E-a | Autorizar ventana de parcheo de emergencia y despliegue de MFA resistente a phishing en todo appliance de borde y acceso remoto expuesto a Internet | KJ-2: el borde de red es el vector dominante y las tres CVE de 2026 son omisiones de autenticación | 15 días (parcheo) · 60 días (MFA) |
| E-b | Aprobar la revisión arquitectónica de la detección para no depender de un único plano de telemetría de endpoint: reenvío de logs en tiempo real fuera del host, telemetría de red e identidad | KJ-3: el EDR puede estar desactivado desde el kernel antes de cualquier acción visible | 90 días |
| E-c | Financiar respaldos inmutables, desconectados y con prueba de restauración verificada trimestralmente, incluida la infraestructura de respaldo misma (Veeam, cintas, trabajos programados) | KJ-5: el actor destruye respaldos de forma deliberada durante los días previos al cifrado | 45 días (primera prueba) |
| E-d | Instruir a Legal y Comunicaciones la preparación del procedimiento de notificación a la **ANCI** bajo la **Ley 21.663** y del guion de respuesta a extorsión multicanal (DDoS, prensa, contacto legal del adversario, spam a empleados) | KJ-6 y §E-1: el **CSIRT Nacional** ya atribuyó a Qilin un incidente de efecto significativo contra una entidad estratégica chilena | 30 días |
| E-e | Decidir y documentar **por anticipado** la postura institucional ante el pago de rescate, con criterio legal y de continuidad, para no improvisarla bajo coacción | El panel del actor está diseñado para maximizar la presión en las primeras 72 horas | 60 días |
| E-f | Encargar a la célula CTI la ejecución del cuestionario de exposición de §O-4 y la reemisión de este informe con telemetría propia incorporada | §0 y §14: sin ese paso, este producto no permite calcular riesgo propio | 30 días |

---

# NIVEL OPERACIONAL
### Para: Jefatura de SOC · Respuesta a Incidentes · Threat Hunting · Horizonte: semanas–meses

## O-1. Identificación y alias

| Designación | Origen | Grado de equivalencia |
|---|---|---|
| `Qilin` | Autodenominación (desde septiembre de 2022) | Referencia |
| `Agenda` | Nombre original de la familia (julio de 2022) | Equivalente — misma operación, antes del rebranding |
| `Water Galura` | Trend Micro | Equivalente |
| `Storm-1934` | Microsoft | Equivalente — designa al núcleo operador |
| `GOLD FEATHER` | Secureworks / Sophos | Equivalente |
| `Phantom Mantis` | Uso de proveedor | **Solapamiento parcial** — designa a un clúster de afiliados, no a la operación completa |
| `G1050` | MITRE ATT&CK | Referencia formal del marco |
| `Qilin.B` | Denominación de variante del cifrador | **No es un grupo**: es una iteración del binario. No usarlo como designación de actor |

> **Nota de tradecraft.** `Qilin`, `Agenda`, `Water Galura`, `GOLD FEATHER` y
> `Storm-1934` son **equivalentes** y pueden fusionarse sin pérdida analítica.
> `Phantom Mantis` **no**: designa un subconjunto de afiliados y fusionarlo con la
> operación completa induce a atribuir a Qilin campañas de un afiliado concreto.
> El nombre «Qilin» procede de una criatura de la mitología china y **no implica
> ningún nexo con China**: es marketing del actor. La fusión indebida de alias es
> una de las principales fuentes de error analítico en este dominio.

## O-2. Estructura y atribución

| Eje de atribución | Valoración | Confianza |
|---|---|---|
| Clúster técnico | Familia de cifradores coherente: Agenda en Go (2022) reescrita en Rust (desde finales de 2022), con variantes para Windows, Linux y VMware ESXi | Alta |
| Grupo organizado | Operación RaaS madura con núcleo desarrollador estable, panel de afiliados, soporte legal y de prensa propios, y programa de reparto del 80–85 % | Alta |
| Nexo estatal | **Ninguno para el núcleo.** Sin patrocinio estatal identificado. Un actor estatal (Moonstone Sleet, RPDC) actuó como **afiliado** en 2025 —primer caso documentado de un grupo estatal usando un RaaS de terceros en lugar de malware propio— | Moderada |
| Origen geográfico | Operación de habla rusa: artefactos de código en ruso y política documentada de no atacar países de la CEI | Moderada |
| Identidad nominal | Sin identificación de personas. **Ningún gobierno ha emitido atribución formal, acusación ni sanción** a la fecha de este informe | Baja |

*Razonamiento:* la exclusión sistemática de objetivos en la CEI, los artefactos
lingüísticos del código y del panel, y la actividad en foros criminales de habla rusa
apuntan de forma convergente al espacio post-soviético. *Contraargumento:* la
exclusión CEI es una convención de todo el ecosistema y puede adoptarse como bandera
falsa deliberada; el nombre chino del grupo es evidencia de que el actor manipula
señales de origen. **La atribución de origen no debe usarse como base para decisiones
operativas**: la defensa no cambia según dónde estén.

## O-3. Modelo de negocio / de operación

Qilin escala porque ha resuelto los tres cuellos de botella del negocio criminal: el
reclutamiento, el acceso y la conversión.

**Reclutamiento.** El reparto de 80–85 % para el afiliado supera el 70–80 % habitual
del sector. Cuando LockBit y ALPHV colapsaron entre 2024 y 2025 y RansomHub se
desintegró, Qilin fue el destino natural de los operadores desplazados. El resultado
es un grupo de afiliados heterogéneo —el tradecraft posterior a la explotación varía
notablemente entre intrusiones, lo que Arctic Wolf interpreta como múltiples
afiliados bajo la misma marca— pero experimentado.

**Acceso.** Los afiliados combinan explotación de vulnerabilidades de borde recién
publicadas con credenciales compradas en mercados clandestinos y fuerza bruta contra
portales VPN. El patrón de fuerza bruta observado por el CSIRT Nacional chileno es
deliberadamente sigiloso: **aproximadamente tres intentos fallidos por dirección IP y
rotación inmediata**, diseñado para quedar por debajo de los umbrales de bloqueo y
alerta habituales.

**Conversión.** Aquí está la innovación real. El panel del afiliado integra:
ataques DDoS contra el sitio web de la víctima; un equipo de redactores que produce
publicaciones de escarnio en el sitio de filtración; un chatbot de negociación
automatizado; una herramienta de spam masivo contra correos y teléfonos corporativos
de la víctima; y el botón **«Call lawyer»**, que incorpora a un abogado del propio
actor a la sala de negociación. La lógica está declarada por el adversario: *«la mera
aparición de un abogado en el chat puede ejercer presión indirecta sobre la empresa e
incrementar el monto del rescate, ya que las empresas quieren evitar procedimientos
judiciales»*. Qilin no vende ransomware: vende un servicio completo de coacción.

**Coalición.** Desde septiembre de 2025 mantiene un acuerdo declarado con LockBit 5.0
y DragonForce para compartir técnicas e infraestructura, ruptura de la norma histórica
de aislamiento entre programas RaaS. *Implicación para el CTI:* una TTP atribuida hoy
a Qilin puede aparecer mañana en un incidente de DragonForce, y viceversa. Las
detecciones deben escribirse contra el comportamiento, no contra la marca.

## O-4. Nuestra exposición

<!-- cti:note type="gap" -->

> ⬛ **Sección sin evaluar — requiere telemetría interna.** Este informe no puede
> responder si estamos expuestos ni si ya estamos comprometidos. Las preguntas
> siguientes son el requisito de colección mínimo para cerrar esa brecha. Mientras
> esta tabla no tenga respuestas, los juicios sobre riesgo propio son condicionales.

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| X-1 | ¿Exponemos PAN-OS a Internet? ¿Qué versión? ¿Están habilitadas las cookies de omisión de autenticación (`authentication override`) con la configuración de certificado afectada por CVE-2026-0257? | Inventario · configuración de firewall | TI/Redes |
| X-2 | ¿Exponemos Check Point Remote Access VPN o Mobile Access? ¿Parcheado CVE-2026-50751? | Inventario | TI/Redes |
| X-3 | ¿Tenemos FortiGate/FortiOS con SSL-VPN publicado? ¿Con MFA obligatorio? ¿Con bloqueo por intentos fallidos y restricción geográfica? | Inventario · configuración | TI/Redes |
| X-4 | ¿Hay firewalls WatchGuard con portal de autenticación expuesto? (vector confirmado en el incidente chileno de enero de 2026) | Inventario | TI/Redes |
| X-5 | ¿Veeam Backup & Replication está en versión vulnerable a CVE-2023-27532? ¿Sus credenciales están en la base de configuración? | Inventario de respaldo | Operaciones TI |
| X-6 | ¿Hay ConnectWise ScreenConnect, Cisco FMC o SAP NetWeaver accesibles desde Internet? | Inventario | TI/Redes |
| X-7 | ¿Qué porcentaje de nuestros accesos VPN y administrativos usa MFA **resistente a phishing** (FIDO2), no OTP? | IAM | Identidad |
| X-8 | ¿Está WSL habilitado en algún endpoint de la flota? ¿Nuestro EDR inspecciona la ejecución dentro de WSL? | Inventario de endpoints · consola EDR | SOC |
| X-9 | ¿Tenemos controles de lista blanca de controladores (WDAC / HVCI / lista de bloqueo de controladores vulnerables de Microsoft) activos? ¿Alertamos sobre carga de controladores no firmados por fabricantes conocidos? | Configuración de endpoint | SOC · Endpoint |
| X-10 | ¿Los logs de seguridad se reenvían **en tiempo real** fuera del host, de modo que su borrado local no destruya la evidencia? | Arquitectura SIEM | Ingeniería de detección |
| X-11 | ¿Nuestros respaldos son inmutables, están desconectados de la red y se ha probado la restauración en los últimos 90 días? | Operaciones de respaldo | Operaciones TI |
| X-12 | ¿Hay hipervisores ESXi/vCenter alcanzables desde la red corporativa plana, sin segmentación? | Arquitectura de red | TI/Redes |
| X-13 | ¿Tenemos RMM (AnyDesk, ScreenConnect, Splashtop, TeamViewer, LogMeIn) instalados, y un inventario de cuáles son legítimos? | Inventario de software | TI |
| X-14 | ¿Alertamos sobre ejecución de Rclone, Ngrok, FileZilla, CyberDuck o tráfico saliente a MEGA y Proton Drive? | SIEM · proxy | SOC |

## O-5. Cronología

<!-- cti:timeline -->

| Fecha | Hecho | Traza |
|---|---|---|
| 2022-07 | Primera aparición de la familia **Agenda**, escrita en Golang | Global |
| 2022-09 | Rebranding a **Qilin** y reescritura del cifrador en Rust, con soporte multiplataforma | Global |
| 2023-03 | Incorporación de CVE-2023-27532 (Veeam B&R) al repertorio de acceso | Global |
| 2024-06-03 | **Ataque a Synnovis, proveedor de servicios de patología del NHS en el sureste de Londres** | Global |
| 2024–2025 | Colapso de LockBit, ALPHV y RansomHub; Qilin absorbe afiliados desplazados | Global |
| 2025-06 | El panel de afiliados incorpora **«Call lawyer», DDoS integrado, periodistas propios y chatbot de negociación** | Global |
| 2025-06 | **King's College Hospital confirma la muerte de un paciente** como consecuencia del ataque a Synnovis: los retrasos en análisis de sangre figuran entre los factores contribuyentes | Global |
| 2025-06-27 | **CSIRT Nacional de Chile emite la alerta AIA25-00007 sobre Qilin**, con IOC y vector de fuerza bruta contra SSL-VPN Fortinet | Chile |
| 2025-06 | Qilin se convierte en el grupo más prolífico del mundo y no cede el primer puesto mensual durante doce meses | Global |
| 2025-09 | **Coalición declarada con LockBit 5.0 y DragonForce** para compartir técnicas e infraestructura | Global |
| 2025 | **Moonstone Sleet (RPDC) despliega Qilin como afiliado**: primer caso documentado de actor estatal usando un RaaS ajeno | Global |
| 2025-09-11 | Actualización de la alerta chilena AIA25-00007; se confirma muestra local en C con RSA-4096 y binario ESXi | Chile |
| 2026-01 | 107 víctimas publicadas en enero, el 15,8 % de todos los ataques del mes | Global |
| 2026-01-29 | **CSIRT Nacional alerta de un incidente de efecto significativo en una entidad estratégica chilena (OIV/PSE) y atribuye la autoría a Qilin**; el acceso inicial fue fuerza bruta contra un firewall WatchGuard | Chile |
| 2026-01 → 2026-03 | Publicación de cinco víctimas chilenas: Valbifrut, Ducasse Comercial, Conectados Chile, Graneles de Chile y Noi Hotels | Chile |
| 2026-03 | 131 víctimas: tercer mes consecutivo por encima de cien, sin precedente para un solo grupo | Global |
| 2026-03 | Compromiso de **Die Linke**, partido político alemán: expansión desde el objetivo comercial al político | Global |
| 2026-04-02 | **Cisco Talos publica el análisis del módulo neutralizador de EDR**: cadena de cuatro etapas, BYOVD con `rwdrv.sys` y `hlpdrv.sys`, más de 300 productos afectados | Global |
| 2026-05-07 | Inicio de la explotación de **CVE-2026-50751** (omisión de autenticación en Check Point Remote Access VPN y Mobile Access, CVSS 9.3), vinculada a un afiliado de Qilin con confianza media | Global |
| 2026-06 | **Primera pérdida del primer puesto mensual en el año**: 71–78 víctimas frente a las 115 de TheGentlemen | Global |
| 2026-06 | Arctic Wolf investiga múltiples intrusiones que explotan **CVE-2026-0257** (omisión de autenticación en PAN-OS) para desplegar Qilin | Global |
| 2026-07-21 | Divulgación pública de la campaña de explotación de PAN-OS | Global |
| 2026-07-30 | **Publicación de Servitelco (tecnología, Chile)** en el sitio de filtración | Chile |
| 2026-07 | Recuperación a 119 víctimas, empatando el primer puesto con TheGentlemen | Global |
| 2026-08-23 | **Publicación de Difor (Chile)** en el sitio de filtración | Chile |
| 2026-08-26 | Publicación de la ATF estadounidense en el sitio de filtración | Global |
| 2026-08 | Reivindicación del ataque a **Danone** con ~221 GB de datos internos | Global |
| 2026-08 | **157 víctimas: máximo mensual histórico del actor**, en el mes récord global de 964 víctimas y 83 grupos activos | Global |
| 2026-08 | **Agosto marca el récord histórico de ransomware en Chile**: al menos diez organizaciones afectadas; los ocho primeros meses superan cualquier año completo anterior | Chile |
| 2026-09-16 | Fecha de corte de este informe. **Sin detención, acusación, sanción ni aviso gubernamental conjunto contra Qilin** | Global |

## O-6. Hipótesis alternativas consideradas

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| **H1. Qilin es una operación criminal de habla rusa con ánimo de lucro, sin dirección estatal** | Consistente con la exclusión CEI, los artefactos lingüísticos, el modelo de afiliados y la selección de víctimas por oportunidad y no por valor de inteligencia. Ninguna evidencia la contradice | `Retenida` |
| **H2. Qilin es o tiene nexo con un actor estatal chino, como sugiere su nombre** | Inconsistencia: no hay evidencia de vínculo con China ni con otros Estados asiáticos; el nombre es una elección de marca. La victimología es financiera, no de espionaje | `Descartada` |
| **H3. Qilin es una fachada norcoreana para financiamiento estatal** | La participación de Moonstone Sleet en 2025 fue **como afiliado**, no como operador. La operación precede a esa participación en tres años y sigue activa al margen de ella. Se consigna para que no se reabra sin evidencia nueva | `Poco probable · 20–35 %` |
| **H4. La caída de junio de 2026 indica el inicio de una degradación estructural** | Inconsistencia con los datos: julio recuperó a 119 y agosto marcó el máximo histórico de 157. La hipótesis se sostuvo un mes y fue falsada por la serie | `Descartada` |
| **H5. La variación entre trackers refleja actividad real distinta y no metodología** | Sin evidencia. Las diferencias (338 vs. 342 en el primer trimestre) son compatibles con criterios de deduplicación y corte. Se consigna para no sobreinterpretar discrepancias menores | `Descartada` |
| **H6. Múltiples afiliados con tradecraft muy distinto operan bajo la misma marca** | Consistente con la observación de Arctic Wolf: el comportamiento posterior a la explotación varía entre intrusiones, desde cifrado puro hasta doble extorsión completa. **Tiene consecuencia defensiva directa:** no existe «el playbook de Qilin», sino un rango | `Retenida` |

**Supuesto clave:** que el acceso inicial seguirá concentrándose en el borde de red y
en credenciales válidas. Si el actor incorporase acceso por cadena de suministro de
software o por phishing masivo, la priorización de controles de §E-4 quedaría
desalineada y habría que reordenar el esfuerzo hacia el correo y la gestión de
terceros.

**Pre-mortem.** *Es marzo de 2027 y este informe resultó equivocado. ¿Por qué?*
Tres causas plausibles, en orden de probabilidad. Primera: **nos fijamos en la marca
y no en el comportamiento**; Qilin se renombró, los IOC del Anexo A caducaron y el
SOC dejó de buscar lo que seguía ocurriendo bajo otro nombre. Segunda: **confiamos en
que el EDR nos avisaría**; el BYOVD lo apagó y no teníamos un segundo plano de
telemetría fuera del host, de modo que la intrusión fue invisible hasta el cifrado.
Tercera: **tratamos la victimología como una preferencia del adversario** y
concluimos que nuestro sector no era objetivo, cuando la selección es oportunista y
lo que decide es nuestro perímetro, no nuestro rubro.

## O-7. Indicadores y señales de alerta

| # | Indicador observable | Qué señalaría | Disciplina | Responsable |
|---|---|---|---|---|
| I-1 | Publicación de una nueva CVE de omisión de autenticación en un appliance de borde de uso masivo | Ventana de explotación inminente: históricamente el actor la incorpora en semanas | OSINT | Célula CTI |
| I-2 | Aparición de una organización chilena de nuestro sector o cadena de suministro en el sitio de filtración | Presencia activa de un afiliado en la geografía; posible reventa de acceso a proveedores compartidos | CLOSINT | Célula CTI |
| I-3 | Alerta del CSIRT Nacional/ANCI que mencione a Qilin o a un vector de borde | Confirmación de campaña en curso contra entidades chilenas | OSINT institucional | Célula CTI |
| I-4 | Anuncio en foros de un cambio de marca, de reparto o de panel | Precursor de rebranding: caducidad anticipada de los IOC de este informe | CLOSINT | Célula CTI |
| I-5 | Publicación de una acción policial, sanción o acusación contra el actor | Falsador de KJ-1 y KJ-7; obliga a reemitir el informe | OSINT | Célula CTI |
| I-6 | Aparición de un descifrador gratuito o filtración de claves | Cambio estructural del cálculo de riesgo y de la postura ante el pago | OSINT / TECHINT | Célula CTI |
| I-7 | Picos de autenticación fallida distribuidos, con ~3 intentos por IP de origen, contra nuestros portales VPN | Patrón de fuerza bruta característico del actor, diseñado para evadir umbrales | Telemetría propia | SOC |
| I-8 | Nuevas variantes del módulo neutralizador de EDR reportadas por proveedores | Actualización necesaria de las detecciones D-1 y D-2 | TECHINT | Ingeniería de detección |

---

# NIVEL TÁCTICO
### Para: Analistas de SOC · Ingeniería de Detección · Threat Hunting · Horizonte: días–semanas

## T-1. Cadena de intrusión

<!-- cti:stages title="Cuatro movimientos: entrar, cegar, vaciar, romper" dwell="next" -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 01 · Borde | Entrada por appliance o credencial válida | CVE-2026-0257 (PAN-OS) · CVE-2026-50751 (Check Point) · CVE-2023-27532 (Veeam) · fuerza bruta SSL-VPN Fortinet/WatchGuard · RDP expuesto · credenciales de mercado |
| Etapa 02 · Ceguera | Neutralización del EDR antes de cualquier acción ruidosa | Sideload de `msimg32.dll` · cargador PE en memoria · BYOVD con `rwdrv.sys` y `hlpdrv.sys` · supresión de ETW · desactivación de Defender · `EDRSandblast` vía `upd.exe` + `avupdate.dll` |
| Etapa 03 · Saqueo | Credenciales, movimiento lateral y exfiltración | Mimikatz contra `lsass`/`winlogon`/`wininit` · GPO contra credenciales de Chrome · PsExec y RDP · Cobalt Strike · RMM (AnyDesk, ScreenConnect, LogMeIn, Ngrok) · Rclone, CyberDuck, FileZilla, MEGA, Proton Drive |
| Etapa 04 · Impacto | Destruir la recuperación y cifrar | Borrado de instantáneas VSS · destrucción de respaldos Veeam, cintas y trabajos programados · `cipher /w` · borrado de registros de eventos · cifrado Windows/Linux/ESXi · reinicio de servidores de respaldo y VPN |

**Permanencia:** mediana de 3 a 5 días entre acceso inicial e impacto, con
observaciones de hasta 6 días. El tiempo no se pierde: se invierte en localizar y
destruir los respaldos y en exfiltrar antes de cifrar.

> ⚠ **Consecuencia de doctrina.** La etapa 02 ocurre **antes** que todo lo demás.
> Si la detección depende exclusivamente del EDR, el adversario habrá eliminado el
> testigo antes de cometer el delito. Las etapas 03 y 04 solo son visibles desde
> planos de telemetría que el host no controla: red, identidad, proxy y SIEM con
> reenvío en tiempo real.

## T-2. Mapa MITRE ATT&CK

<!-- cti:matrix -->

| Táctica | ID | Técnica | Procedimiento observado |
|---|---|---|---|
| Acceso inicial | T1190 | Exploit Public-Facing Application | CVE-2026-0257 (omisión de autenticación en portal y gateway de PAN-OS), CVE-2026-50751 (Check Point Remote Access VPN / Mobile Access), CVE-2023-27532 (Veeam B&R: extracción de credenciales cifradas de la base de configuración) |
| Acceso inicial | T1133 | External Remote Services | Sesiones SSL-VPN establecidas sin credenciales válidas tras explotar la omisión de autenticación; abuso de portales VPN Fortinet y WatchGuard |
| Acceso inicial | T1110 | Brute Force | Fuerza bruta contra SSL-VPN con ~3 intentos fallidos por IP y rotación inmediata, para permanecer bajo los umbrales de bloqueo |
| Acceso inicial | T1078.002 | Valid Accounts: Domain Accounts | Uso de cuentas de dominio comprometidas y credenciales adquiridas en mercados clandestinos |
| Ejecución | T1059.001 | Command and Scripting Interpreter: PowerShell | Enumeración, borrado de registros de eventos y despliegue del cifrador |
| Ejecución | T1569.002 | System Services: Service Execution | PsExec con nombre aleatorio desde `%Temp%` |
| Ejecución | T1204.002 | User Execution: Malicious File | Ejecución del cifrador con contraseña SHA-256 pasada por línea de comandos |
| Persistencia | T1547 | Boot or Logon Autostart Execution | Claves de registro con patrón de asterisco seguido de seis caracteres alfabéticos minúsculos aleatorios |
| Escalada de privilegios | T1134 | Access Token Manipulation | Suplantación de tokens para operar con privilegios de cuentas administrativas |
| Evasión | T1211 / T1068 | Exploitation for Defense Evasion (BYOVD) | Carga de `rwdrv.sys` (ThrottleStop renombrado: acceso a memoria física en modo kernel) y `hlpdrv.sys` (terminación de procesos de más de 300 controladores EDR) |
| Evasión | T1574.002 | Hijack Execution Flow: DLL Side-Loading | `msimg32.dll` malicioso cargado por un binario legítimo; variante con `upd.exe` firmado que carga `avupdate.dll` |
| Evasión | T1562.001 | Impair Defenses: Disable or Modify Tools | Desactivación de la protección en tiempo real de Microsoft Defender; versión personalizada de `EDRSandblast` |
| Evasión | T1562.006 | Impair Defenses: Indicator Blocking | Supresión de Event Tracing for Windows (ETW) |
| Evasión | T1562.009 | Impair Defenses: Safe Mode Boot | Reinicio en modo seguro para cifrar con los productos de seguridad inactivos |
| Evasión | T1070.001 | Indicator Removal: Clear Windows Event Logs | Script PowerShell que enumera y vacía todos los registros con entradas, vía `EventLogSession.ClearLog` |
| Evasión | T1027 | Obfuscated Files or Information | Cargador con ejecución íntegramente en memoria, ofuscación del flujo de control y de las llamadas a API, neutralización de hooks en espacio de usuario |
| Evasión | T1202 | Indirect Command Execution | Ejecución de cifradores ELF de Linux dentro de WSL para operar fuera del alcance del EDR de Windows |
| Acceso a credenciales | T1003.001 | OS Credential Dumping: LSASS Memory | Módulo Mimikatz embebido contra `lsass.exe`, `winlogon.exe` y `wininit.exe` |
| Acceso a credenciales | T1555.003 | Credentials from Web Browsers | Scripts distribuidos por GPO para extraer credenciales almacenadas en Chrome |
| Descubrimiento | T1087.002 | Account Discovery: Domain Account | Enumeración de cuentas y grupos de dominio previa al movimiento lateral |
| Descubrimiento | T1018 | Remote System Discovery | Reconocimiento de red y topología para identificar hipervisores y servidores de respaldo |
| Movimiento lateral | T1021.002 | Remote Services: SMB/Windows Admin Shares | PsExec sobre recursos administrativos (`C$`); ajuste de `MaxMpxCt` a 65535 para maximizar conexiones concurrentes |
| Movimiento lateral | T1021.001 | Remote Services: Remote Desktop Protocol | RDP con credenciales de dominio comprometidas |
| Mando y control | T1219 | Remote Access Software | AnyDesk, ScreenConnect, Splashtop, TeamViewer, LogMeIn, Ngrok |
| Mando y control | T1105 | Ingress Tool Transfer | Preparación de la carga útil en `C:\PerfLogs\` |
| Exfiltración | T1567.002 | Exfiltration to Cloud Storage | Rclone, CyberDuck, FileZilla hacia MEGA y Proton Drive |
| Impacto | T1490 | Inhibit System Recovery | `vssadmin.exe Delete Shadows /all /quiet`, desactivación del servicio VSS, destrucción de respaldos en cinta, borrado de configuraciones y trabajos programados de Veeam |
| Impacto | T1485 | Data Destruction | `cipher /w:"X:\"` para sobrescribir el espacio libre e impedir la recuperación forense |
| Impacto | T1486 | Data Encrypted for Impact | Cifrado AES-256-CTR (con AES-NI) o ChaCha20, con clave protegida por RSA-4096 única por víctima; modos de pasada `fast`, `percent` y `normal` |
| Impacto | T1529 | System Shutdown/Reboot | Reinicio de servidores de respaldo y VPN tras el cifrado, para prolongar la indisponibilidad |
| Impacto | T1657 | Financial Theft | Doble extorsión con presión añadida por DDoS, prensa, contacto legal y spam corporativo |

## T-3. Dónde atacamos en la Pirámide del Dolor

<!-- cti:pyramid -->

| Nivel | Qué contiene en este informe y qué vale | Valor |
|---|---|---|
| Hashes | Anexo A: tres muestras. El cifrador se compila por víctima y la clave RSA es única: el hash cambia en cada despliegue. Solo sirve para retrohunt histórico | Base · valor trivial |
| IP · Dominios | Dos IP del CERT chileno, de 2025. Infraestructura rotada hace tiempo. **No construir la defensa sobre bloqueo de IP** | Valor bajo |
| Artefactos | Nombres de controladores (`rwdrv.sys`, `hlpdrv.sys`), DLL cargadas por sideload (`msimg32.dll`, `avupdate.dll`), ruta de preparación `C:\PerfLogs\`, patrón de clave de registro, nota `README-RECOVER-*.txt`, `MaxMpxCt=65535`. **Duraderos entre compilaciones** | Valor medio |
| Herramientas | PsExec, Mimikatz, Rclone, Cobalt Strike, AnyDesk, Ngrok, WSL. Todas legítimas o de uso dual: **detectar por contexto —quién, dónde, cuándo—, nunca por presencia** | Valor alto |
| TTP | Apagar el EDR desde el kernel antes de moverse; destruir respaldos antes de cifrar; ejecutar ELF dentro de WSL; fuerza bruta de tres intentos con rotación de IP. **Aquí debe concentrarse el esfuerzo de detección** | Cima · valor máximo |

## T-4. Hipótesis de caza prioritarias

<!-- cti:accordion critical="^(H-1|H-2|H-3|H-4)\b" regional="^(H-11|H-12)\b" -->

**H-1 — Carga de controladores vulnerables conocidos (BYOVD).** Buscar eventos de
instalación y carga de controladores en modo kernel cuyo nombre o hash corresponda a
`rwdrv.sys`, `hlpdrv.sys` o a ThrottleStop renombrado, y en general cualquier
controlador firmado que aparezca por primera vez en la flota. Fuente: eventos de
Sysmon 6 (Driver loaded), EID 7045 (instalación de servicio) y telemetría de EDR
—si sigue viva—. Ventana: 30 días hacia atrás. **Fidelidad esperada: muy alta**; un
controlador de gestión de CPU cargándose en un servidor de producción no tiene
explicación benigna. Falsos positivos: herramientas legítimas de diagnóstico de
hardware en equipos de ingeniería, y agentes de telemetría de fabricantes de portátiles.

**H-2 — Silencio súbito del EDR.** Buscar endpoints que dejan de reportar al EDR o
al SIEM sin un apagado correspondiente, especialmente si el cese es simultáneo en
varios equipos del mismo segmento. Esta hipótesis **no depende del EDR para
detectarse**, que es justamente su valor. Fuente: heartbeat del agente en la consola
de gestión, ausencia de logs en el SIEM, inventario de activos vivos. Ventana:
continua, con alerta automática a los 30 minutos de silencio. **Fidelidad: alta.**
Falsos positivos: ventanas de mantenimiento, portátiles apagados, cortes de red —por
eso la señal fuerte es la *simultaneidad* y la ausencia de apagado limpio.

**H-3 — Borrado masivo de registros de eventos.** Buscar EID 1102 (registro de
auditoría borrado) y EID 104 (registro de sistema borrado), y correlacionar con
ejecución previa de PowerShell que invoque `EventLogSession` o `Clear-EventLog`.
Fuente: Security y System de Windows reenviados **fuera del host**. Ventana: 90 días.
**Fidelidad: muy alta.** Falsos positivos: casi ninguno en producción; cierta
actividad legítima en imágenes de laboratorio y despliegues.

**H-4 — Ejecución de binarios ELF de Linux dentro de WSL.** Buscar creación de
procesos `wsl.exe`, `bash.exe` o `wslhost.exe` en hosts donde WSL no tiene
justificación de negocio, y montajes de rutas de red desde dentro de WSL. Fuente:
telemetría de creación de procesos, `Microsoft-Windows-Subsystem-Linux`. Ventana: 60
días. **Fidelidad: alta en flota corporativa no técnica, baja en equipos de
desarrollo.** Falsos positivos: desarrolladores; se resuelve con una lista de
excepción por unidad organizativa, no desactivando la regla.

**H-5 — Destrucción preparatoria de la capacidad de recuperación.** Buscar
`vssadmin delete shadows`, `wbadmin delete`, cambios del servicio VSS a estado
deshabilitado, borrado o modificación de trabajos y repositorios de Veeam, y accesos
anómalos a la consola de respaldo desde cuentas que no la administran habitualmente.
Fuente: línea de comandos, logs de la plataforma de respaldo, autenticación. Ventana:
30 días. **Fidelidad: muy alta.** Falsos positivos: scripts de mantenimiento de
almacenamiento; documentarlos y excluirlos por hash del script, no por nombre.

**H-6 — Preparación de carga útil en rutas atípicas del sistema.** Buscar escrituras
de ejecutables en `C:\PerfLogs\`, `C:\Windows\Temp\` y `%Temp%` con nombres aleatorios,
seguidas de ejecución en menos de una hora. Fuente: creación de archivos y de procesos.
Ventana: 30 días. **Fidelidad: alta** para `C:\PerfLogs\` en concreto, que rara vez
contiene ejecutables legítimos.

**H-7 — PsExec con argumentos de propagación.** Buscar líneas de comando que
contengan `-accepteula` junto con `--spread` o `-spread-vcenter`, o PsExec ejecutado
desde `%Temp%` con nombre distinto al original. Fuente: creación de procesos, EID 7045
en los destinos. Ventana: 30 días. **Fidelidad: muy alta**; el argumento `--spread`
no aparece en usos administrativos legítimos.

**H-8 — Volcado de credenciales contra procesos de autenticación.** Buscar accesos
de manejador a `lsass.exe`, `winlogon.exe` y `wininit.exe` desde procesos no
firmados por Microsoft. Fuente: Sysmon EID 10, telemetría de EDR. Ventana: 60 días.
**Fidelidad: alta** con una lista de excepción bien mantenida. Falsos positivos:
agentes de seguridad, herramientas de inventario y de gestión de parches.

**H-9 — Exfiltración previa al cifrado.** Buscar ejecución de `rclone`, `filezilla`,
`cyberduck` o `ngrok` en servidores; volúmenes de salida anómalos hacia MEGA, Proton
Drive y proveedores de almacenamiento no aprobados; y sesiones largas de subida fuera
de horario. Fuente: proxy, NetFlow, DNS, creación de procesos. Ventana: 60 días.
**Fidelidad: media-alta**; requiere línea base de volumen por servidor. Es la última
ventana real de intervención antes del impacto.

**H-10 — RMM no inventariado.** Buscar instalación o ejecución de AnyDesk,
ScreenConnect, Splashtop, TeamViewer o LogMeIn en equipos donde no consten como
software aprobado, y conexiones entrantes desde sus infraestructuras. Fuente:
inventario de software, creación de procesos, proxy. Ventana: 90 días.
**Fidelidad: alta** si el inventario de RMM legítimos está al día; sin ese inventario,
la hipótesis es inejecutable —y esa es, en sí misma, una brecha que cerrar—.

**H-11 — Fuerza bruta de baja tasa contra portales VPN.** Buscar autenticaciones
fallidas agrupadas por cuenta, no por IP: el patrón del actor es de ~3 fallos por
dirección y rotación, de modo que **el umbral clásico por IP de origen no lo detecta**.
Fuente: logs de VPN y del proveedor de identidad. Ventana: 90 días. **Fidelidad:
media**; genera ruido con contraseñas caducadas. Esta hipótesis cubre el vector
confirmado en los incidentes chilenos de 2025 y de enero de 2026.

**H-12 — Retrohunt sobre los indicadores del CERT nacional.** Buscar las IP
`168.235.85.66` y `5.61.62.32` y los hashes del Anexo A en el histórico de firewall,
proxy y EDR. Fuente: SIEM histórico. Ventana: todo el retenido. **Fidelidad: baja
como detección, alta como cierre de pregunta**: un resultado negativo no prueba nada,
pero uno positivo cambia el informe entero. Ejecutar una vez y documentar el resultado.

## T-5. Brechas de visibilidad que hay que cerrar primero

| Brecha | Por qué importa aquí |
|---|---|
| Sin reenvío de logs de Windows en tiempo real fuera del host | H-3 queda ciega: el actor borra los registros locales y la evidencia desaparece con ellos. Es la brecha más grave de la lista |
| Sin monitorización de carga de controladores (Sysmon EID 6 / EID 7045) | H-1 y H-2 quedan ciegas frente a la técnica que define a este actor |
| Sin alerta por silencio del agente EDR | H-2 queda ciega. Es la única detección que sobrevive a la etapa 02 de la cadena |
| Sin telemetría de ejecución dentro de WSL | H-4 queda ciega ante un vector diseñado precisamente para esa ausencia |
| Sin registro de auditoría de la plataforma de respaldo | H-5 queda ciega: perderíamos la capacidad de recuperación sin saberlo hasta intentar restaurar |
| Sin línea base de volumen de salida por servidor | H-9 queda ciega y se pierde la última ventana de intervención antes del cifrado |
| Sin inventario autoritativo de RMM aprobados | H-10 es inejecutable: sin saber qué es legítimo, toda ejecución de RMM es ruido |
| Sin visibilidad de autenticación en appliances de borde correlacionada con identidad | H-11 queda ciega frente al patrón de fuerza bruta de baja tasa |

---

# NIVEL TÉCNICO
### Para: Ingeniería de detección · Automatización · TIP/SIEM · Vida útil: días–semanas

## X-1. Arsenal y capacidad

| Propiedad | Valor |
|---|---|
| Familia y linaje | Agenda (julio de 2022, Golang) → Qilin (septiembre de 2022, reescritura en Rust). Coexisten compilaciones en Go, Rust y C; la muestra analizada en Chile está escrita en C |
| Lenguaje / ofuscación | Rust predominante; cargador con ejecución íntegramente en memoria, ofuscación del flujo de control y de las invocaciones a API, neutralización de hooks en espacio de usuario, supresión de ETW |
| Criptografía | AES-256 en modo CTR cuando hay aceleración por hardware (AES-NI); ChaCha20 como alternativa en su ausencia. Material de clave protegido con RSA-4096 única por víctima, incrustada en la compilación y anexada a cada archivo cifrado. Fuerza bruta inviable |
| Modos de cifrado | Multipass configurable: `fast`, `percent` y `normal`, para negociar entre velocidad e integridad del daño |
| Plataformas | Windows, Linux (ELF, también ejecutado dentro de WSL) y VMware ESXi / vCenter |
| Propagación | Argumento `--spread` para difusión por SMB con credenciales suministradas; `-spread-vcenter` para autodistribución en entornos virtualizados |
| Autenticación del binario | Requiere una contraseña en formato SHA-256 pasada por línea de comandos: sin ella, la muestra no se ejecuta ni se analiza con facilidad en sandbox |
| Marca de impacto | Extensión de archivo igual al identificador único de la compañía afectada; nota de rescate `README-RECOVER-<extension/company_id>.txt` |
| Neutralización de defensas | Módulo de cuatro etapas con BYOVD capaz de desactivar más de 300 controladores de productos EDR, de prácticamente todos los fabricantes del mercado |

## X-2. Artefactos de host persistentes entre builds

<!-- cti:cards -->

| Categoría | Artefactos | Etiqueta |
|---|---|---|
| **Controladores vulnerables (BYOVD)** | `rwdrv.sys` (ThrottleStop.sys renombrado; acceso a memoria física en modo kernel) · `hlpdrv.sys` (terminación de procesos de productos de seguridad) | `evasión · kernel` |
| **DLL cargadas por sideload** | `msimg32.dll` (cargador PE de primera etapa) · `avupdate.dll` cargada por el binario firmado `upd.exe`, que despliega una versión personalizada de `EDRSandblast` | `evasión · carga` |
| **Rutas de preparación** | `C:\PerfLogs\` (preparación de la carga útil) · `%Temp%\<nombre aleatorio>.exe` (PsExec renombrado) | `staging` |
| **Persistencia en registro** | Claves cuyo nombre sigue el patrón de un asterisco seguido de seis caracteres alfabéticos minúsculos aleatorios | `persistencia` |
| **Modificaciones de sistema** | `MaxMpxCt = 65535` (maximiza conexiones SMB concurrentes) · `fsutil behavior set SymlinkEvaluation R2R:1 R2L:1` (resolución de enlaces simbólicos remoto-a-remoto y remoto-a-local) | `preparación de lateral` |
| **Marca de impacto** | Nota `README-RECOVER-<company_id>.txt` en cada directorio cifrado · extensión de archivo igual al identificador de la víctima | `impacto` |
| **Destrucción de evidencia** | `cipher /w:"X:\"` (sobrescritura del espacio libre) · registros de eventos vaciados vía `EventLogSession.ClearLog` | `antiforense` |

> ⚠ **Estos artefactos valen más que los hashes.** Los nombres de controlador, las
> DLL cargadas por sideload, la ruta `C:\PerfLogs\` y los argumentos de propagación
> sobreviven a la recompilación del cifrador. Los hashes del Anexo A no.

## X-3. Lógica de detección prioritaria

<!-- cti:detections -->

**D-1 · CRÍTICO — Carga de controlador BYOVD conocido del actor**

```
event.code IN (6, 7045)
AND (
  file.name IN ("rwdrv.sys", "hlpdrv.sys")
  OR file.pe.original_file_name == "ThrottleStop.sys"
)
```

→ **Contención automática sin escalado humano.** Aislar el host de la red de
inmediato. La carga de estos controladores marca el punto en el que el adversario
está a punto de quedarse sin testigos: cualquier retraso por escalado manual
compromete la detección de todo lo que viene después.

**D-2 · CRÍTICO — Silencio simultáneo de agentes EDR sin apagado limpio**

```
count(distinct host.name) >= 3
WHERE agent.last_seen older_than 30m
  AND NOT exists(event.code == 1074 OR event.code == 6006)  // apagado/reinicio limpio
  AND host.network.last_seen within 30m                      // el host sigue en red
GROUP BY network.segment
```

→ **Contención automática del segmento y activación del procedimiento de respuesta.**
Esta detección es la única de la lista que **no depende del EDR**, y por eso es la
que debe funcionar cuando todas las demás han fallado.

**D-3 · CRÍTICO — Borrado de registros de eventos**

```
event.code IN (1102, 104)
OR (
  process.name == "powershell.exe"
  AND process.command_line MATCHES_ANY ("*EventLogSession*", "*Clear-EventLog*", "*wevtutil* cl *")
)
```

→ Contención automática del host. En un entorno de producción no existe una
explicación legítima para el vaciado del registro de seguridad. **Requiere que los
logs se reenvíen fuera del host**: si solo viven en local, esta regla nunca se
dispara porque su evidencia se destruye con ellos.

**D-4 · CRÍTICO — Destrucción de la capacidad de recuperación**

```
process.command_line MATCHES_ANY (
  "*vssadmin* delete shadows*",
  "*wbadmin* delete*",
  "*wmic* shadowcopy delete*",
  "*bcdedit* /set *recoveryenabled no*",
  "*cipher* /w:*"
)
OR (service.name == "VSS" AND service.start_type CHANGED_TO "Disabled")
```

→ **Contención automática.** Es el último indicador fiable antes del cifrado y
concede minutos, no horas. Nótese que `cipher /w` es antiforense y no de cifrado:
su presencia indica que el adversario ya está limpiando.

**D-5 · ALTO — PsExec con argumento de propagación**

```
process.command_line CONTAINS "-accepteula"
AND process.command_line MATCHES_ANY ("*--spread*", "*-spread-vcenter*")
```

→ Alerta de máxima prioridad con contención del host de origen. El argumento
`--spread` no tiene uso administrativo legítimo conocido.

**D-6 · ALTO — DLL de sideload en ruta no estándar**

```
dll.name IN ("msimg32.dll", "avupdate.dll")
AND NOT dll.path STARTS_WITH ("C:\\Windows\\System32", "C:\\Windows\\SysWOW64")
AND dll.code_signature.trusted == false
```

→ Alerta con recolección forense inmediata del proceso padre. `msimg32.dll` es una
biblioteca legítima de Windows: lo anómalo es su ubicación y su firma, no su nombre.

**D-7 · ALTO — Ejecutable escrito y lanzado desde `C:\PerfLogs\`**

```
file.path STARTS_WITH "C:\\PerfLogs\\"
AND file.extension IN ("exe", "dll", "sys")
```

→ Alerta con contención. `C:\PerfLogs\` casi nunca contiene ejecutables en un sistema
sano y es una ruta de preparación observada en las intrusiones vía PAN-OS.

**D-8 · ALTO — Preparación del terreno para el movimiento lateral**

```
process.command_line MATCHES_ANY (
  "*fsutil* behavior set SymlinkEvaluation*",
  "*MaxMpxCt*"
)
OR (registry.path ENDS_WITH "\\Parameters\\MaxMpxCt" AND registry.value == 65535)
```

→ Alerta de prioridad alta. Estos ajustes preceden a la propagación por SMB y rara
vez los realiza un administrador sin un ticket asociado.

**D-9 · MEDIO — Ejecución de ELF de Linux dentro de WSL en host no autorizado**

```
process.name IN ("wsl.exe", "wslhost.exe", "bash.exe")
AND host.organizational_unit NOT IN (<UO de desarrollo autorizadas>)
```

→ Alerta para triaje humano. Severidad media por su dependencia de la lista de
excepciones; en flota administrativa sin desarrolladores, elévese a alta.

**D-10 · MEDIO — Herramienta de exfiltración en servidor**

```
process.name IN ("rclone.exe", "filezilla.exe", "cyberduck.exe", "ngrok.exe")
AND host.role == "server"
```

→ Alerta para triaje humano con revisión inmediata del volumen saliente del host.
Es la última ventana práctica de intervención antes del impacto.

**D-11 · MEDIO — Fuerza bruta de baja tasa contra VPN**

```
count(event.outcome == "failure") >= 5
GROUP BY user.name
OVER window(24h)
HAVING count(distinct source.ip) >= 4
  AND max(count_per_ip) <= 4
```

→ Alerta para triaje y bloqueo de la cuenta afectada. **Agrupa por cuenta, no por IP**:
el patrón del actor —tres intentos por dirección y rotación— está diseñado para no
disparar los umbrales por IP de origen.

> ⚠ **Regla de operación.** Las detecciones **D-1 a D-4 deben ejecutar contención
> automática sin escalado humano**. Justificación explícita: la etapa 02 de la cadena
> elimina la telemetría de endpoint y las etapas 03 y 04 se completan en horas. Un
> procedimiento que exija validación de un analista en horario laboral llegará
> sistemáticamente tarde contra este actor. El coste de un aislamiento erróneo —un
> host fuera de red durante una hora— es órdenes de magnitud inferior al de una
> intrusión completada.

## X-4. Consultas de caza

```kql
// H-1 — Carga de controladores vulnerables conocidos (Microsoft Defender XDR)
DeviceEvents
| where ActionType in ("DriverLoad", "KernelDriverLoad")
| where FileName in~ ("rwdrv.sys", "hlpdrv.sys", "ThrottleStop.sys")
   or InitiatingProcessFolderPath has_any (@"C:\PerfLogs\", @"\Temp\")
| project Timestamp, DeviceName, FileName, FolderPath, InitiatingProcessCommandLine, InitiatingProcessAccountName
| order by Timestamp desc
```

```kql
// H-3 — Borrado de registros de eventos correlacionado con PowerShell previo
let clears = DeviceEvents
    | where ActionType == "SecurityLogCleared" or ActionType == "EventLogCleared"
    | project ClearTime = Timestamp, DeviceName;
DeviceProcessEvents
| where ProcessCommandLine has_any ("EventLogSession", "Clear-EventLog", "wevtutil cl")
| join kind=inner clears on DeviceName
| where Timestamp between (ClearTime - 15m .. ClearTime)
| project Timestamp, DeviceName, AccountName, ProcessCommandLine, ClearTime
```

```kql
// H-5 — Destrucción de la capacidad de recuperación
DeviceProcessEvents
| where ProcessCommandLine has_any (
    "vssadmin delete shadows", "wbadmin delete", "shadowcopy delete",
    "recoveryenabled no", "cipher /w")
| project Timestamp, DeviceName, AccountName, ProcessCommandLine, InitiatingProcessFileName
| order by Timestamp asc
```

```kql
// H-7 — PsExec con argumentos de propagación
DeviceProcessEvents
| where ProcessCommandLine has "-accepteula"
| where ProcessCommandLine has_any ("--spread", "-spread-vcenter")
   or (FolderPath has @"\Temp\" and ProcessVersionInfoOriginalFileName =~ "psexec.c")
| project Timestamp, DeviceName, AccountName, FolderPath, ProcessCommandLine
```

```kql
// H-9 — Exfiltración hacia almacenamiento en la nube desde servidores
DeviceNetworkEvents
| where RemoteUrl has_any ("mega.nz", "mega.io", "drive.proton.me", "protondrive")
   or InitiatingProcessFileName in~ ("rclone.exe", "filezilla.exe", "cyberduck.exe", "ngrok.exe")
| summarize Bytes = sum(todouble(coalesce(column_ifexists("BytesSent", 0.0), 0.0))),
            Conexiones = count()
        by DeviceName, InitiatingProcessFileName, RemoteUrl, bin(Timestamp, 1h)
| where Conexiones > 10
| order by Bytes desc
```

```kql
// H-11 — Fuerza bruta de baja tasa: agrupar por cuenta, no por IP de origen
SigninLogs
| where ResultType != 0
| where AppDisplayName has_any ("VPN", "Remote Access", "Gateway")
| summarize Fallos = count(), IPs = dcount(IPAddress), PorIP = count() / dcount(IPAddress)
        by UserPrincipalName, bin(TimeGenerated, 24h)
| where IPs >= 4 and PorIP <= 4
| order by IPs desc
```

```powershell
# Comprobación de higiene: ¿está activa la lista de bloqueo de controladores
# vulnerables de Microsoft? Sin ella, D-1 es la única barrera contra el BYOVD.
Get-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\CI\Config' `
                 -Name 'VulnerableDriverBlocklistEnable' -ErrorAction SilentlyContinue
# Valor esperado: 1. Verificar también HVCI:
Get-CimInstance -ClassName Win32_DeviceGuard -Namespace root\Microsoft\Windows\DeviceGuard |
  Select-Object -ExpandProperty SecurityServicesRunning
# Se espera que incluya 2 (HVCI / integridad de código protegida por hipervisor).
```

```yaml
# Sigma — Carga de controlador BYOVD asociado a Qilin
# Autor: Célula CTI · Fecha: 2026-09-16
# ATT&CK: T1211, T1068, T1562.001 · Nivel: critical
title: Carga de controlador vulnerable asociado a Qilin (rwdrv/hlpdrv)
id: 8f2b6c14-1d7a-4e39-9a51-3c0b7e5d2a41
status: experimental
description: >
  Detecta la carga de los controladores vulnerables utilizados por el módulo
  neutralizador de EDR de Qilin y Warlock, incluido ThrottleStop.sys renombrado.
references:
  - Cisco Talos, análisis del EDR killer de Qilin y Warlock, 2026-04-02
logsource:
  product: windows
  category: driver_load
detection:
  selection_name:
    ImageLoaded|endswith:
      - '\rwdrv.sys'
      - '\hlpdrv.sys'
  selection_original:
    OriginalFileName: 'ThrottleStop.sys'
  filter_legit_path:
    ImageLoaded|startswith:
      - 'C:\Program Files\TechPowerUp\'
  condition: (selection_name or selection_original) and not filter_legit_path
falsepositives:
  - Herramientas legítimas de gestión térmica de CPU en equipos de ingeniería.
    Excluir por ruta e identidad del firmante, nunca por nombre de archivo.
level: critical
```

## X-5. Mitigaciones de configuración con efecto directo

| Control | Corta |
|---|---|
| Parcheo prioritario de PAN-OS, Check Point Remote Access/Mobile Access, FortiOS y Veeam B&R | La etapa 01: elimina las tres omisiones de autenticación explotadas en 2026 |
| MFA resistente a phishing (FIDO2) en el 100 % de VPN y accesos administrativos | La etapa 01 por credencial válida y la fuerza bruta de baja tasa de H-11 |
| Bloqueo por intentos fallidos **agrupado por cuenta** y restricción geográfica de acceso VPN a Chile | La fuerza bruta de ~3 intentos por IP con rotación, que el umbral por IP no detecta |
| Lista de bloqueo de controladores vulnerables de Microsoft + HVCI + WDAC con firma de fabricante confiable | La etapa 02 completa: sin capacidad de cargar `rwdrv.sys`/`hlpdrv.sys`, el BYOVD falla |
| Reenvío de registros de Windows en tiempo real a un destino que el host no puede modificar | El antiforense de la etapa 04: el borrado local deja de destruir la evidencia |
| Alerta automática por silencio del agente EDR superior a 30 minutos con host vivo en red | Convierte el éxito de la etapa 02 en una señal de detección en lugar de en un punto ciego |
| Desinstalación o bloqueo de WSL por política en unidades organizativas sin justificación de desarrollo | La ejecución de cifradores ELF fuera del alcance de la inspección de Windows |
| Respaldos inmutables, desconectados, con credenciales fuera del dominio y prueba de restauración trimestral | La etapa 04: mantiene la capacidad de recuperación aunque el cifrado se complete |
| Cuentas de la plataforma de respaldo fuera del dominio de producción, con MFA propio y auditoría separada | El pivote desde credenciales de dominio hacia Veeam, incluido CVE-2023-27532 |
| Segmentación de ESXi/vCenter y de Active Directory respecto de la red plana de usuarios | La propagación `-spread-vcenter` y el salto al hipervisor |
| Restricción de SMB, RDP y SSH entre segmentos internos; bloqueo de SMB saliente a Internet | La etapa 03 y la propagación `--spread` |
| Inventario autoritativo de RMM aprobados y bloqueo del resto por control de aplicaciones | La persistencia y el C2 vía AnyDesk, ScreenConnect, LogMeIn y Ngrok |
| Bloqueo en proxy de MEGA, Proton Drive y almacenamiento en la nube no aprobado para cuentas de servidor | La exfiltración de la etapa 03, última ventana antes del impacto |

---

## 14. Brechas de inteligencia y nuevos requisitos de colección

| # | Brecha | Impacto en el juicio | Requisito propuesto | Prioridad |
|---|---|---|---|---|
| G-1 | Sin telemetría propia incorporada | §O-4 sin evaluar; todos los juicios sobre riesgo propio son condicionales | Ejecutar el cuestionario de §O-4 y reemitir como v2.0 con exposición evaluada | **Crítica** |
| G-2 | Sin visibilidad del vector de acceso inicial en las víctimas chilenas publicadas | KJ-6 no puede precisar si el vector regional coincide con el global o si predomina la fuerza bruta contra VPN | Solicitar al CSIRT Nacional/ANCI, por los canales de intercambio sectorial, el detalle técnico agregado de los incidentes atribuidos a Qilin en Chile | Alta |
| G-3 | Cifras de víctimas derivadas exclusivamente del sitio de filtración adversario | Sesgo sistemático a la baja: las víctimas que pagan no se publican. Todas las cifras del §E-3 son suelos, no totales | Contrastar con datos de aseguradoras, de firmas de respuesta a incidentes y de notificaciones regulatorias a la ANCI | Alta |
| G-4 | Sin dato propio de permanencia (tiempo entre acceso e impacto) | KJ-5 descansa en medianas de proveedor de otras geografías y sectores | Instrumentar la medición de permanencia en los próximos ejercicios de respuesta y en simulacros de mesa | Media |
| G-5 | Discrepancia no resuelta entre trackers (338 vs. 342 en el primer trimestre; 71 vs. 78 en junio) | Impide fijar una serie única con precisión mejor que ±5 % | Fijar Breachsense como serie de referencia por continuidad mensual y documentar el criterio de corte en el procedimiento de la célula | Baja |
| G-6 | Sin visibilidad de la economía interna del actor ni del volumen real de afiliados | KJ-7 depende de una interpretación económica no corroborada | Colección CLOSINT dirigida en foros y canales donde el actor recluta | Media |
| G-7 | Cobertura de detección de WSL y de carga de controladores no verificada en nuestra flota | KJ-4 se formula como hipótesis sobre nosotros y no como hecho | Prueba de emulación adversaria (purple team) de las técnicas T1211, T1562.001 y T1202 contra la pila actual | Alta |
| G-8 | IOC del Anexo A limitados y de 2025 | El Anexo A tiene valor casi nulo como bloqueo preventivo | Suscripción a la fuente de IOC de proveedor con actualización continua; integración en TIP con caducidad automática a 30 días | Media |

---

# ANEXOS

## Anexo A — Indicadores de compromiso

> ⚠ **Leer antes de usar.** Los IOC son el nivel más perecedero y menos valioso del
> producto. Los que siguen proceden mayoritariamente de la alerta AIA25-00007 del
> CSIRT Nacional de Chile (junio–septiembre de 2025) y **tienen más de un año**: su
> valor operativo es de retrohunt, no de bloqueo preventivo. El cifrador se compila
> por víctima con clave RSA única, de modo que **el hash cambia en cada despliegue**.
> Priorícense siempre los artefactos de §X-2 y las TTP de §T-2 sobre esta lista.

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Acción permitida |
|---|---|---|---|---|
| ipv4 | `168.235.85.66` | Acceso remoto del atacante, campaña contra víctima chilena (CSIRT Nacional, 2025) | Media | Solo retrohunt |
| ipv4 | `5.61.62.32` | Infraestructura del atacante, misma campaña (CSIRT Nacional, 2025) | Media | Solo retrohunt |
| sha256 | `6d0b950eceb1bcdf7517ff79eb05121f3966c3e175c8bd0804b07f103942d251` | Cifrador para VMware ESXi, muestra recuperada en Chile | Alta | Bloqueo |
| sha256 | `9f1f11a708d393e0a4109ae189bc64f1f3e312653dcf317a2bd406f18ffcc507` | Muestra de cifrador Qilin (repositorio de proveedor) | Media | Bloqueo |
| sha256 | `a31f222fc283227f5e7988d1ad9c0aecd66d58bb7b4d8518ae23e110308dbf91` | Muestra de cifrador Qilin (repositorio de proveedor) | Media | Bloqueo |
| sha256 | `e90bdaaf5f9ca900133b699f18e4062562148169b29cb4eb37a0577388c22527` | Muestra usada en escenarios de validación de detección | Media | Bloqueo |
| sha256 | `d628914c72a4294d6b67126eb8b5a08fa4974d05469852cb7ef872721b207498` | Muestra asociada a regla YARA pública de TEHTRIS | Media | Bloqueo |
| filename | `rwdrv.sys` | Controlador vulnerable (ThrottleStop renombrado) del módulo neutralizador de EDR | Alta | Alerta y contención |
| filename | `hlpdrv.sys` | Controlador que termina procesos de más de 300 productos EDR | Alta | Alerta y contención |
| filename | `msimg32.dll` (fuera de `System32`/`SysWOW64`, sin firma confiable) | Cargador PE de primera etapa por DLL side-loading | Alta | Alerta |
| filename | `avupdate.dll` cargada por `upd.exe` | Despliegue de `EDRSandblast` personalizado | Alta | Alerta |
| path | `C:\PerfLogs\*.exe` | Ruta de preparación de la carga útil observada en intrusiones vía PAN-OS | Media | Alerta |
| filename | `README-RECOVER-<company_id>.txt` | Nota de rescate; confirma impacto consumado | Alta | Alerta crítica |
| pattern | Clave de registro con nombre `*` + 6 caracteres alfabéticos minúsculos aleatorios | Persistencia observada tras la explotación de PAN-OS | Media | Alerta |
| cve | `CVE-2026-0257` | Omisión de autenticación en portal y gateway de PAN-OS (CVSS 7.8), explotada desde junio de 2026 | Alta | Parcheo prioritario |
| cve | `CVE-2026-50751` | Omisión de autenticación en Check Point Remote Access VPN y Mobile Access (CVSS 9.3), explotada desde el 7 de mayo de 2026 | Media | Parcheo prioritario |
| cve | `CVE-2023-27532` | Veeam Backup & Replication: extracción de credenciales cifradas de la base de configuración | Alta | Parcheo prioritario |

*Nota de higiene:* ninguna de las dos IP corresponde a infraestructura compartida
conocida (CDN, proxy residencial, nube pública), por lo que un bloqueo no debería
tener impacto operativo colateral; verifíquese no obstante antes de aplicarlo.
`msimg32.dll` es una biblioteca **legítima** de Windows: bloquearla por nombre
rompería el sistema. La detección debe basarse en la combinación de ruta anómala y
firma no confiable, tal como se expresa en D-6.

## Anexo B — Fuentes y valoración

> Valoración doble tipo Admiralty/OTAN: **fiabilidad de la fuente (A–F)** ×
> **credibilidad de la información (1–6)**. Se valoran por separado.

| Fuente | Disciplina | Fiabilidad | Credibilidad | Notas de sesgo |
|---|---|---|---|---|
| CSIRT Nacional / ANCI (Chile) — alerta AIA25-00007 y comunicado del 29-01-2026 | CERT nacional | A | 2 | Autoridad nacional; publica en TLP:CLEAR y omite deliberadamente detalle sensible y la identidad de las víctimas |
| Cisco Talos — análisis del módulo neutralizador de EDR (02-04-2026) | TECHINT de proveedor | A | 1 | Análisis de binario verificable; interés comercial indirecto |
| Arctic Wolf Labs — campaña CVE-2026-0257 | TECHINT / telemetría de IR | A | 2 | Telemetría real de respuesta a incidentes; sesgo de base instalada propia |
| Check Point Research — *State of Ransomware Q1 2026* | OSINT comercial | B | 2 | Metodología publicada; recuento basado en sitios de filtración |
| Black Kite — informe anual de ransomware 2026 | OSINT comercial | B | 2 | Serie interanual consistente; interés comercial en dramatizar magnitudes |
| Breachsense — informes mensuales de ransomware 2026 | OSINT comercial | B | 2 | Única serie mensual continua disponible; criterio de deduplicación no publicado en detalle |
| Emsisoft — *State of Ransomware Q2 2026* | OSINT comercial | B | 2 | Declara explícitamente que las cifras reales son mayores que las publicadas |
| Halcyon — seguimiento trimestral y perfil del actor | OSINT comercial | B | 2 | Interpretación económica de la caída de junio no corroborada |
| MOXFIVE — guía de TTP de Qilin 2026 | OSINT comercial / IR | B | 2 | Basada en casos propios; muestra sesgada hacia clientes norteamericanos |
| Picus Security — análisis técnico de Qilin | OSINT comercial | B | 2 | Orientado a validación de controles propios |
| Trend Micro — perfil de Agenda / *Water Galura* | OSINT comercial | B | 2 | Fuente primaria del alias; anterior a la actividad de 2026 |
| Microsoft — designación `Storm-1934` y actividad de Moonstone Sleet | Proveedor / TECHINT | A | 2 | Telemetría de escala global; taxonomía propietaria |
| MITRE ATT&CK — grupo `G1050` | Marco de referencia | A | 1 | Consolidado, con retraso respecto de la actividad más reciente |
| CronUp — panorama de ransomware en Chile | OSINT regional | B | 2 | La mejor cobertura disponible de la geografía; recuento sobre sitios de filtración |
| SOCRadar, DeXpose, CybelAngel, Adaptive Security | OSINT comercial | C | 3 | Agregadores; útiles para corroboración, no como fuente primaria |
| Sitio de filtración de Qilin y anuncios en foros | CLOSINT | C | 4 | **El actor controla el mensaje.** Las cifras de reparto con afiliados y las capacidades del panel son material promocional del adversario |
| Prensa especializada (The Record, The Register, Infosecurity, HIPAA Journal) sobre Synnovis | OSINT periodístico | B | 2 | Buen registro de impacto humano y regulatorio; escaso detalle técnico |
| Group-IB (vía prensa) — tasa de pago del 23 % | OSINT comercial indirecto | C | 3 | Cifra citada de segunda mano; no se ha accedido al informe original |

**Escalas**
- **A** completamente fiable · **B** normalmente fiable · **C** bastante fiable · **D** normalmente no fiable · **E** no fiable · **F** no evaluable.
- **1** confirmada por otras fuentes · **2** probablemente cierta · **3** posiblemente cierta · **4** dudosa · **5** improbable · **6** no evaluable.

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
`PAP` · `STIX 2.1 / TAXII 2.1` · `Admiralty Code` · `Ley 21.663 y marco ANCI (Chile)`

## Anexo E — Paquete legible por máquina

- Bundle STIX 2.1: pendiente de generar a partir del Anexo A y de §T-2
- Evento MISP: pendiente — taxonomías previstas: `tlp`, `admiralty-scale`, `estimative-language`, `PAP`
- Reglas: la regla Sigma de §X-4 y las detecciones D-1 a D-11 deben versionarse en el repositorio de detección antes de la emisión de la v1.1

## Anexo F — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
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
