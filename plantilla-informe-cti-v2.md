---
tlp: "TLP:AMBER+STRICT"
pap: "PAP:AMBER"
id: "CTI-YYYY-NNN"
version: "1.0"
fecha: "YYYY-MM-DD"
tipo: "Informe de campaña | Perfil de actor | Alerta flash | Evaluación estratégica | Soporte a IR | Respuesta a RFI"
actor: "<Actor / campaña>"
foco_regional: "<Chile · Latinoamérica · Global>"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
pir: ["PIR-01", "PIR-04"]
ventana: "YYYY-MM-DD → YYYY-MM-DD"
coleccion: "<n fuentes externas · telemetría propia sí/no>"
autor: "<analista>"
revision: "<nombre> — YYYY-MM-DD"
aprobacion: "<jefe de inteligencia>"
caduca: "YYYY-MM-DD"
distribucion: "<Nota de distribución que aparecerá al pie del HTML>"
---

<!--
  ════════════════════════════════════════════════════════════════════════
  PLANTILLA DE INFORME CTI · v2.0 — edición «md ↔ html»
  ════════════════════════════════════════════════════════════════════════
  Este archivo sigue siendo un Markdown normal: se lee igual de bien en
  cualquier visor, y los comentarios `cti:` son invisibles al renderizarlo.

  Para obtener el informe en HTML con el sistema de diseño:

      python3 render/cti_render.py mi-informe.md

  Cada `<!-- cti:algo -->` convierte el bloque que viene INMEDIATAMENTE
  DESPUÉS en un componente visual. Si lo borras, ese bloque sale como
  tabla o párrafo normal: nada se rompe. Referencia completa de directivas
  en `render/LEEME.md`.
  ════════════════════════════════════════════════════════════════════════
-->

# `<Actor / campaña>`
## `<Qué hace + a quién afecta, en una línea>`
### `<Matiz: alcance regional, sectorial o temporal>`

> **Regla de oro del producto:** todo párrafo debe responder a un requisito de
> inteligencia (PIR) y habilitar una decisión. Si un párrafo no cambia lo que
> alguien va a hacer, va al anexo o se borra.

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-YYYY-NNN` |
| Versión / fecha | `1.0` — `YYYY-MM-DD` |
| Tipo de producto | |
| Niveles cubiertos | Estratégico · Operacional · Táctico · Técnico |
| Marcado de difusión | `TLP:AMBER+STRICT` · `PAP:AMBER` |
| Clasificación interna | |
| Requisitos atendidos | `PIR-xx`, `RFI-xx` |
| Solicitante / consumidor primario | |
| Ventana de observación | `YYYY-MM-DD` → `YYYY-MM-DD` |
| Base de colección | |
| Autor (analista) | |
| Revisión por pares | `<nombre>` — `YYYY-MM-DD` |
| Aprobación | `<jefe de inteligencia>` |
| Caducidad / revisión | `YYYY-MM-DD` |
| Productos relacionados | `CTI-YYYY-NNN` (supersede / complementa) |
| Paquete legible por máquina | `STIX 2.1 bundle: <uuid>` · `MISP event: <id>` |

> ⚠ **Limitación estructural.** `<Si el informe no incorpora telemetría propia,
> decirlo aquí y decir qué sección queda sin evaluar por ello.>`

---

## 1. BLUF — Juicios clave

Máximo 7. Cada juicio: **afirmación + probabilidad estimativa + nivel de
confianza + base**. Nunca mezclar probabilidad (cuán probable es el hecho) con
confianza (cuán sólida es la base analítica). Véase Anexo C.

<!-- cti:kj -->

**KJ-1.** `<Afirmación en una frase; esta primera frase será el titular de la tarjeta.>`
`<Desarrollo en una o dos frases más.>` Valoramos **muy probable** *(80–95 %)*.
**Confianza: alta.** *Base:* `<telemetría propia corroborada por 2 fuentes B-2>`.

**KJ-2.** `<Afirmación>`. **Probabilidad remota** *(5–15 %)*. **Confianza: baja.**
*Base:* `<fuente única no corroborada>`.

**KJ-3.** `<…>`

**Qué cambiaría estos juicios:** `<falsador concreto y observable>`.

---

## 2. Resumen ejecutivo

`<8–12 líneas, sin jerga, para dirección. Qué pasa, por qué nos importa a
nosotros en concreto, qué decisión se pide, qué pasa si no se toma. Traducir
siempre a impacto de negocio: continuidad, dinero, regulación, reputación,
terceros.>`

<!-- cti:cards -->

| Rasgo | Qué significa | Etiqueta |
|---|---|---|
| `<Ventaja competitiva 1 del adversario>` | `<Consecuencia para nosotros>` | `01 · <tema>` |
| `<Ventaja 2>` | `<Consecuencia>` | `02 · <tema>` |
| `<Ventaja 3>` | `<Consecuencia>` | `03 · <tema>` |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `868` | `<víctimas reivindicadas en 12 meses>` | `<posición en el mercado criminal>` |
| `2 días` | `<mediana de permanencia hasta el impacto>` | `<mínimo observado>` |

> ✅ **Decisión que se solicita a Dirección:** `<a, b, c — concretas y con plazo>`.

---

## 3. Alcance, requisitos y limitaciones

**3.1 Requisitos de inteligencia atendidos**

| Req. | Enunciado | ¿Respondido? | Dónde |
|---|---|---|---|
| PIR-01 | `<¿Qué actores tienen intención y capacidad contra nuestro sector?>` | Parcial | §5, §11 |

**3.2 Fuera de alcance.** `<Qué NO cubre este informe, para evitar sobrelectura.>`

**3.3 Limitaciones de la colección.** `<Sesgos: visibilidad solo en EDR de
endpoints Windows; sin telemetría OT; fuentes en ruso traducidas
automáticamente; ventana ciega entre X e Y.>`

**3.4 Metodología.** `<Disciplinas empleadas (Anexo B), técnicas analíticas
estructuradas aplicadas (§10), herramientas de análisis.>`

---

<!--
  ────────────────────────────────────────────────────────────────────────
  A partir de aquí, el informe puede organizarse por NIVELES DE CONSUMO.
  Cada `# NIVEL …` genera un divisor a todo ancho con su color propio:
      Estratégico → azul profundo · Operacional → azul medio
      Táctico     → verde menta   · Técnico     → ámbar
  El `###` que sigue al `#` se convierte en la línea «Para: … Horizonte: …».
  Numera las secciones con el prefijo del nivel (E-1, O-3, T-4, X-5) y el
  renderizador coloreará la chapa de cada sección en consecuencia.
  Si prefieres la numeración clásica 4–14, borra los `# NIVEL` y ya está.
  ────────────────────────────────────────────────────────────────────────
-->

# NIVEL ESTRATÉGICO
### Para: Consejo · CISO · Riesgo · Legal · Horizonte: 6–24 meses

## E-1. Qué representa este actor en el panorama

`<Este primer párrafo se convierte en el subtítulo de la sección si mide menos
de 260 caracteres. Para evitarlo, usa --no-leads o empieza con una tabla.>`

<!-- cti:cards -->

| Cambio estructural | Por qué nos afecta | Etiqueta |
|---|---|---|
| `<…>` | `<…>` | `<…>` |

## E-2. Victimología

<!-- cti:bars title="Países con más víctimas" -->

| País | Víctimas |
|---|---|
| `<EE. UU.>` | `156` |
| `<Alemania>` | `40` |

<!-- cti:bars title="Sectores más golpeados" -->

| Sector | Víctimas |
|---|---|
| `<Manufactura>` | `171` |

> **Lectura clave.** `<Qué dice la distribución sobre el criterio de selección
> del adversario, y qué protección NO tenemos por ser quienes somos.>`

## E-3. Tendencia y pronóstico

<!-- cti:chart title="Víctimas publicadas por mes" cap="Fuente controlada por el adversario: indicador de tendencia, no recuento." -->

| Periodo | Víctimas |
|---|---|
| `Ene` | `48` |
| `Feb` | `91` |
| `Jul` | `169` |

<!-- cti:cards -->

| Escenario | Desarrollo | Etiqueta |
|---|---|---|
| `<Más probable>` | `<…>` | `Probable · 55–70 %` |
| `<Alternativa creíble>` | `<…>` | `Poco probable · 20–35 %` |
| `<Baja prob. / alto impacto>` | `<…>` | `Remoto · 5–10 %` |

## E-4. Decisiones que este informe pide al nivel estratégico

<!-- cti:table highlight="regional|CERT|ANCI" -->

| # | Decisión | Fundamento | Plazo |
|---|---|---|---|
| E-a | `<…>` | `<KJ-n que la sostiene>` | 30 días |

---

# NIVEL OPERACIONAL
### Para: Jefatura de SOC · Respuesta a Incidentes · Threat Hunting · Horizonte: semanas–meses

## O-1. Identificación y alias

| Designación | Origen | Grado de equivalencia |
|---|---|---|
| `<Nombre>` | Autodenominación | Referencia |
| `<Storm-nnnn>` | Microsoft | Equivalente |
| `<Alias dudoso>` | `<Proveedor>` | Ambiguo |

> **Nota de tradecraft.** Declarar si los alias son **equivalentes**, **solapados
> parcialmente** o **agrupaciones distintas**. La fusión indebida de alias es una
> de las principales fuentes de error analítico.

## O-2. Estructura y atribución

| Eje de atribución | Valoración | Confianza |
|---|---|---|
| Clúster técnico | | Alta |
| Grupo organizado | | Moderada |
| Nexo estatal | | Alta |
| Identidad nominal | | Baja |

*Razonamiento:* `<solapamiento de infraestructura, reutilización de código,
horario de operación, idioma>`. *Contraargumento:* `<bandera falsa, herramienta
compartida, acceso revendido por un IAB>`.

## O-3. Modelo de negocio / de operación

`<Qué hace que este actor escale: economía, acceso, automatización.>`

## O-4. Nuestra exposición

> ⬛ **Sección sin evaluar — requiere telemetría interna.** `<Borra esta nota
> cuando la rellenes. Un informe con esta sección vacía es inteligencia genérica,
> no inteligencia propia.>`

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| X-1 | `<¿Exponemos <tecnología> a Internet? ¿Qué versión?>` | Inventario | TI/Redes |

## O-5. Cronología

<!-- cti:timeline -->

| Fecha | Hecho | Traza |
|---|---|---|
| `YYYY-MM-DD` | `<Primer acceso observado>` | Global |
| `YYYY-MM-DD` | `**<Hito: úsalo en negrita para marcarlo como hito>**` | Chile |

## O-6. Hipótesis alternativas consideradas

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| `<H1>` | `<Consistente con …>` | `Retenida` |
| `<H2>` | `<Inconsistencia: …>` | `Poco probable · 20–35 %` |
| `<H3>` | `<Sin evidencia. Se consigna para que no se reabra.>` | `Descartada` |

**Supuesto clave:** `<qué se rompe si es falso>`.
**Pre-mortem:** `<es dentro de seis meses y este informe resultó equivocado, ¿por qué?>`

## O-7. Indicadores y señales de alerta

| # | Indicador observable | Qué señalaría | Disciplina | Responsable |
|---|---|---|---|---|
| I-1 | `<…>` | `<…>` | OSINT | Célula CTI |

---

# NIVEL TÁCTICO
### Para: Analistas de SOC · Ingeniería de Detección · Threat Hunting · Horizonte: días–semanas

## T-1. Cadena de intrusión

<!-- cti:stages title="Tres etapas, un solo movimiento continuo" dwell="**Permanencia:** mediana ≈ <n> días · mínimo observado < 24 h." -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 01 · Borde | `<Entrada por el perímetro>` | `<CVE>` · `<cuenta backdoor>` · `<persistencia RMM>` |
| Etapa 02 · Dominio | `<Reconocimiento y credenciales>` | `<escáneres>` · `<volcado de credenciales>` · `<lateral>` |
| Etapa 03 · Impacto | `<Neutralizar, exfiltrar, cifrar>` | `<matar EDR>` · `<destruir respaldos>` · `<exfiltrar>` |

## T-2. Mapa MITRE ATT&CK

<!-- cti:matrix -->

| Táctica | ID | Técnica | Procedimiento observado |
|---|---|---|---|
| Acceso inicial | T1190 | Exploit Public-Facing App | `<CVE-XXXX-XXXXX en appliance de borde>` |
| Ejecución | T1059.001 | PowerShell | `<…>` |
| Impacto | T1486 | Data Encrypted for Impact | `<…>` |

## T-3. Dónde atacamos en la Pirámide del Dolor

<!-- cti:pyramid -->

| Nivel | Qué contiene en este informe y qué vale | Valor |
|---|---|---|
| Hashes | `<Anexo A. Trivial de eludir: cambia en cada build. Solo retrohunt.>` | Base · valor trivial |
| IP · Dominios | `<Rotación rápida. No construir la defensa sobre bloqueo de IP.>` | Valor bajo |
| Artefactos | `<Nombres de tareas, claves Run, recursos. Duraderos entre builds.>` | Valor medio |
| Herramientas | `<Legítimas: detectar por contexto, no por presencia.>` | Valor alto |
| TTP | `<El comportamiento. Aquí debe concentrarse el esfuerzo.>` | Cima · valor máximo |

## T-4. Hipótesis de caza prioritarias

<!-- cti:accordion critical="^(H-1|H-2|H-3)\b" regional="^H-1[0-9]\b" -->

**H-1 — `<Título de la hipótesis>`.** `<Qué buscar, en qué fuente de log, en qué
ventana. Termina indicando la fidelidad esperada y los falsos positivos.>`

**H-2 — `<Título>`.** `<…>`

## T-5. Brechas de visibilidad que hay que cerrar primero

| Brecha | Por qué importa aquí |
|---|---|
| `<Sin registro de X>` | `<Qué hipótesis de caza queda ciega sin ella>` |

---

# NIVEL TÉCNICO
### Para: Ingeniería de detección · Automatización · TIP/SIEM · Vida útil: días–semanas

## X-1. Arsenal y capacidad

| Propiedad | Valor |
|---|---|
| Lenguaje / ofuscación | |
| Criptografía | |
| Plataformas | |

## X-2. Artefactos de host persistentes entre builds

<!-- cti:cards -->

| Categoría | Artefactos | Etiqueta |
|---|---|---|
| `<Tareas programadas>` | `<nombres>` | `<persistencia>` |

## X-3. Lógica de detección prioritaria

<!-- cti:detections -->

**D-1 · CRÍTICO — `<Nombre de la detección>`**

```
process.name == "<binario>"
AND cmdline CONTAINS_ANY ("<cadena 1>", "<cadena 2>")
```

→ `<Acción de respuesta. Di explícitamente si debe ser automática.>`

**D-2 · ALTO — `<Nombre>`**

```
EID 7045 AND service_name IN ("<svc1>","<svc2>")
```

→ `<Acción>`

> ⚠ **Regla de operación.** `<Qué detecciones deben ejecutar contención
> automática sin escalado humano, y por qué la velocidad del actor lo exige.>`

## X-4. Consultas de caza

```kql
DeviceProcessEvents
| where ProcessCommandLine has_any ("<cadena>")
| project Timestamp, DeviceName, AccountName, ProcessCommandLine
```

```yaml
# Sigma — <título>
# Autor, fecha, ATT&CK ID, nivel, falsos positivos conocidos
```

## X-5. Mitigaciones de configuración con efecto directo

| Control | Corta |
|---|---|
| `<…>` | `<qué paso concreto de la cadena>` |

---

## 14. Brechas de inteligencia y nuevos requisitos de colección

| # | Brecha | Impacto en el juicio | Requisito propuesto | Prioridad |
|---|---|---|---|---|
| G-1 | `<Sin visibilidad del vector de acceso inicial>` | `<KJ-1 queda en confianza baja>` | `<Solicitar logs del proveedor X>` | Crítica |

---

# ANEXOS

## Anexo A — Indicadores de compromiso

> ⚠ **Leer antes de usar.** Los IOC son el nivel más perecedero y menos valioso
> del producto. Se entregan **con contexto, confianza y caducidad**, nunca como
> lista suelta.

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Acción permitida |
|---|---|---|---|---|
| sha256 | `<…>` | `<Loader de la familia X>` | Alta | Bloqueo |
| ipv4 | `<…>` | `<Nodo ORB compartido>` | Baja | Solo retrohunt |
| domain | `<…>` | `<C2>` | Alta | Bloqueo |

*Nota de higiene:* marcar infraestructura compartida (CDN, proxy residencial,
servicios en la nube) para evitar bloqueos con impacto operativo.

## Anexo B — Fuentes y valoración

> Valoración doble tipo Admiralty/OTAN: **fiabilidad de la fuente (A–F)** ×
> **credibilidad de la información (1–6)**. Se valoran por separado.

| Fuente | Disciplina | Fiabilidad | Credibilidad | Notas de sesgo |
|---|---|---|---|---|
| `<Telemetría EDR propia>` | Interna / TECHINT | A | 1 | `<Solo Windows>` |
| `<Informe de proveedor X>` | OSINT comercial | B | 2 | `<Interés comercial en dramatizar>` |
| `<Sitio de filtración del actor>` | OSINT | C | 4 | `<El actor controla el mensaje>` |

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

> Usar siempre el término **y** el porcentaje. No usar «podría» ni «es posible»
> como juicio: son afirmaciones no falsables.

## Anexo D — Marcos de referencia empleados

`MITRE ATT&CK vXX` · `MITRE D3FEND` · `Modelo del Diamante` · `Cyber Kill Chain`
· `Pirámide del Dolor` · `F3EAD` · `ICD 203` · `ACH, KAC, pre-mortem` ·
`TLP 2.0` · `PAP` · `STIX 2.1 / TAXII 2.1` · `Admiralty Code`

## Anexo E — Paquete legible por máquina

- Bundle STIX 2.1: `<ruta/uuid>`
- Evento MISP: `<id>` — taxonomías: `tlp`, `admiralty-scale`, `estimative-language`, `PAP`
- Reglas: `<repositorio de detección / commit>`

## Anexo F — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | `YYYY-MM-DD` | Emisión inicial | |

## Anexo G — Realimentación del consumidor

| Pregunta | Respuesta |
|---|---|
| ¿Respondió a su requisito? | |
| ¿Qué decisión tomó o cambió con este informe? | |
| ¿Qué faltó? | |
| ¿Llegó a tiempo? | |

> Sin este anexo devuelto, el ciclo de inteligencia queda abierto y el próximo
> producto no mejora.
