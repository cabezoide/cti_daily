---
tlp: "TLP:AMBER+STRICT"
pap: "PAP:AMBER"
id: "CTI-YYYY-NNN"
version: "1.0"
tipo: "Informe de campaña | Perfil de actor | Alerta flash | Evaluación estratégica | Soporte a IR | Respuesta a RFI"
nivel: "Estratégico | Operacional | Táctico | Técnico"
pir: ["PIR-01", "PIR-04"]
caduca: "YYYY-MM-DD"
---

# INFORME DE CIBERINTELIGENCIA
## `<Título: actor/campaña + qué hace + a quién afecta>`

> **Regla de oro del producto:** todo párrafo debe responder a un requisito de
> inteligencia (PIR) y habilitar una decisión. Si un párrafo no cambia lo que
> alguien va a hacer, va al anexo o se borra.

---

## 0. Cabecera de control

| Campo | Valor |
|---|---|
| Identificador | `CTI-YYYY-NNN` |
| Versión / fecha | `1.0` — `YYYY-MM-DD` |
| Tipo de producto | |
| Nivel de inteligencia | Estratégico / Operacional / Táctico / Técnico |
| Marcado de difusión | `TLP:AMBER+STRICT` · `PAP:AMBER` |
| Clasificación interna | |
| Requisitos atendidos | `PIR-xx`, `RFI-xx` |
| Solicitante / consumidor primario | |
| Ventana de observación | `YYYY-MM-DD` → `YYYY-MM-DD` |
| Autor (analista) | |
| Revisión por pares | `<nombre>` — `YYYY-MM-DD` |
| Aprobación | `<jefe de inteligencia>` |
| Distribución | |
| Caducidad / revisión | `YYYY-MM-DD` |
| Productos relacionados | `CTI-YYYY-NNN` (supersede / complementa) |
| Paquete legible por máquina | `STIX 2.1 bundle: <uuid>` · `MISP event: <id>` |

---

## 1. BLUF — Juicios clave

> Máximo 5. Cada juicio: **afirmación + probabilidad estimativa + nivel de
> confianza + base**. Nunca mezclar probabilidad (cuán probable es el hecho) con
> confianza (cuán sólida es la base analítica). Véase Anexo C.

- **KJ-1.** `<Afirmación>`. Valoramos que es **muy probable** *(70–85 %)*.
  **Confianza: moderada.** *Base:* `<telemetría propia corroborada por 2 fuentes B-2>`.
- **KJ-2.** `<Afirmación>`. **Probabilidad remota** *(5–15 %)*. **Confianza: baja.**
  *Base:* `<fuente única no corroborada>`.
- **KJ-3.** …

**Qué cambiaría estos juicios:** `<falsador concreto y observable>`.

---

## 2. Resumen ejecutivo

`<8–12 líneas, sin jerga, para dirección. Qué pasa, por qué nos importa a
nosotros en concreto, qué decisión se pide, qué pasa si no se toma. Traducir
siempre a impacto de negocio: continuidad, dinero, regulación, reputación,
terceros.>`

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

**3.4 Metodología.** `<Disciplinas empleadas (§Anexo B), técnicas analíticas
estructuradas aplicadas (§10), herramientas de análisis.>`

---

## 4. Contexto y antecedentes

`<Lo mínimo imprescindible para que el juicio se entienda: historia del actor,
informes previos, contexto geopolítico o de mercado, evolución del ecosistema
criminal relevante.>`

---

## 5. Perfil del adversario

**5.1 Identificación y alias**

| Designación | Origen | Notas |
|---|---|---|
| `<UNCxxxx>` | Clúster interno | Sin promoción a grupo |
| `<APTxx>` | Mandiant | |
| `<Nombre>` | Microsoft (taxonomía meteorológica) | |
| `<Nombre>` | CrowdStrike | |
| `<Gxxxx>` | MITRE ATT&CK | |

> Declarar explícitamente si los alias son **equivalentes**, **solapados
> parcialmente** o **agrupaciones distintas**. La fusión indebida de alias es una
> de las principales fuentes de error analítico.

**5.2 Atribución y su confianza**

| Eje | Valoración | Confianza |
|---|---|---|
| Clúster técnico (misma actividad) | | |
| Grupo (misma organización) | | |
| Patrocinio / nexo estatal | | |
| Identidad nominal (personas, unidad) | | |

*Razonamiento:* `<solapamiento de infraestructura, reutilización de código,
horario de operación, idioma, objetivos coherentes con requisitos de
inteligencia de X>`. *Contraargumento:* `<posible bandera falsa, herramienta
compartida, acceso revendido por un IAB>`.

**5.3 Intención y motivación.** `<Espionaje, lucro, sabotaje, prepoosicionamiento,
hacktivismo, híbrido.>`

**5.4 Capacidad.** `<0-day propios / explotación rápida de n-day / commodity;
madurez de OPSEC; desarrollo propio vs. herramientas alquiladas; capacidad de
escalar; recursos humanos estimados.>`

**5.5 Oportunidad.** `<Qué de nuestra superficie expuesta encaja con su patrón de
acceso inicial.>`

**5.6 Victimología.** `<Sectores, geografías, tamaño, tecnología común entre
víctimas. Incluir el sesgo de observación: "las víctimas conocidas son las que
aparecen en sitios de filtración, no necesariamente todas".>`

---

## 6. Cronología de la actividad

| Fecha | Evento | Fuente | Valoración |
|---|---|---|---|
| `YYYY-MM-DD` | `<Primer acceso observado>` | Telemetría propia | A-1 |
| `YYYY-MM-DD` | `<Publicación en sitio de extorsión>` | OSINT | B-2 |

`<Narrativa de la intrusión o campaña. Qué ocurrió, en qué orden, con qué
velocidad. Incluir tiempos de permanencia y "time-to-ransom" si aplica.>`

---

## 7. Análisis de comportamiento (TTP)

**7.1 Mapa MITRE ATT&CK** *(versión del marco: `vXX`)*

| Táctica | Técnica | ID | Procedimiento observado | Fuente | Detectado por |
|---|---|---|---|---|---|
| Acceso inicial | Explotación de app pública | T1190 | `<CVE-XXXX-XXXXX en appliance de borde>` | IR | — |
| Ejecución | | | | | |
| Persistencia | | | | | |
| Evasión | | | | | |
| Acceso a credenciales | | | | | |
| Descubrimiento | | | | | |
| Mov. lateral | | | | | |
| Recolección | | | | | |
| C2 | | | | | |
| Exfiltración | | | | | |
| Impacto | | | | | |

**7.2 Modelo del Diamante**

| Vértice | Contenido |
|---|---|
| Adversario | |
| Capacidad | |
| Infraestructura | |
| Víctima | |
| Meta-eje socio-político | `<Qué objetivo estatal o de mercado sirve esta operación>` |

**7.3 Delta de comportamiento.** `<Qué ha cambiado desde el último informe:
nuevas técnicas, abandono de herramientas quemadas, cambio de proveedor de
hosting, adopción de IA generativa en el señuelo.>`

**7.4 Nivel en la Pirámide del Dolor.** `<Dónde ataca nuestra respuesta: hashes
(trivial de eludir) vs. TTP (costoso). Justificar por qué las detecciones
propuestas están en el nivel que están.>`

---

## 8. Infraestructura y arsenal

**8.1 Infraestructura.** `<C2, redes ORB/proxy residencial, patrones de registro
de dominios, fingerprints JARM/JA4, certificados, ASN recurrentes, servicios
legítimos abusados (living-off-trusted-sites).>`

**8.2 Arsenal.** `<Familias de malware, loaders, herramientas de acceso remoto
comerciales, binarios legítimos abusados (LOLBins), frameworks de post-explotación.>`

**8.3 Heurísticas de seguimiento (pivotes).** `<Cómo seguimos rastreando a este
actor cuando cambie la infraestructura actual. Esto es lo que tiene vida útil
larga; los IOC del Anexo A, no.>`

---

## 9. Exposición e impacto para `<ORGANIZACIÓN>`

**9.1 Superficie expuesta relevante.** `<Activos concretos, versiones, terceros.>`

**9.2 Cobertura de controles frente a los TTP observados**

| Técnica | ¿Prevenimos? | ¿Detectamos? | ¿Respondemos? | Brecha |
|---|---|---|---|---|
| T1190 | Parcial | No | — | Sin WAF virtual patching en `<appliance>` |

**9.3 Escenario de impacto.** `<En términos de negocio: días de parada, procesos
críticos, obligaciones regulatorias (notificación en 72 h, NIS2/DORA/sectorial),
exposición de terceros y de cadena de suministro.>`

**9.4 Riesgo residual y su tendencia.** `<Alto y creciente / estable / decreciente, con motivo.>`

---

## 10. Análisis alternativo (tradecraft explícito)

**10.1 Hipótesis en competencia (ACH)**

| Evidencia | H1: `<…>` | H2: `<…>` | H3: `<…>` |
|---|---|---|---|
| E1 `<…>` | Consistente | Inconsistente | Neutro |
| E2 `<…>` | | | |

*Hipótesis con menos inconsistencias:* `<H?>`. *Nota:* se selecciona por
refutación, no por confirmación.

**10.2 Verificación de supuestos clave**

| Supuesto | ¿Sostenible? | Si es falso, ¿qué se rompe? |
|---|---|---|
| `<La víctima parcheó el appliance en la fecha que declara>` | No verificado | Toda la cronología de acceso inicial |

**10.3 Hipótesis descartadas y por qué.** `<Incluirlas evita que el lector las
reabra y demuestra que se consideraron.>`

**10.4 Pre-mortem.** `<"Es dentro de seis meses y este informe resultó
equivocado. ¿Por qué?">`

---

## 11. Perspectiva e indicadores de alerta

**11.1 Escenario más probable** *(probable, 55–70 %; confianza moderada)* — `<…>`
**11.2 Alternativa creíble** *(poco probable, 15–30 %)* — `<…>`
**11.3 Baja probabilidad / alto impacto** *(remoto, <10 %)* — `<…>`

**11.4 Indicadores y señales de alerta**

| # | Indicador observable | Qué señalaría | Disciplina de colección | Responsable |
|---|---|---|---|---|
| I-1 | `<Aparición de nuestro sector en el sitio de filtración del actor>` | Transición a extorsión activa | OSINT | Célula CTI |
| I-2 | `<Venta de acceso a nuestra geografía en foro X>` | Preparación de acceso inicial | CLOSINT/HUMINT | Analista de submundo |

---

## 12. Recomendaciones (cursos de acción)

> Priorizadas, con propietario, plazo y criterio de verificación. Separadas por
> audiencia para que cada consumidor lea solo lo suyo.

| # | COA | Audiencia | TTP que mitiga | Esfuerzo | Plazo | Propietario | Verificación |
|---|---|---|---|---|---|---|---|
| R-1 | `<Parchear/aislar appliance de borde>` | TI | T1190 | Medio | 72 h | `<…>` | Escaneo de confirmación |
| R-2 | `<Desplegar regla de detección Sigma-xx>` | SOC | T1059.001 | Bajo | 5 d | `<…>` | Prueba con atomic test |
| R-3 | `<Endurecer proceso de reseteo de credenciales en service desk>` | Personas | T1078 / ing. social por voz | Alto | 30 d | `<…>` | Ejercicio de simulación |
| R-4 | `<Decisión de inversión / seguro / exigencia contractual a proveedor>` | Dirección | — | — | Q siguiente | `<…>` | Acta de comité |

---

## 13. Detección y caza de amenazas

**13.1 Hipótesis de hunting.** `<"Si el actor usa <técnica>, veríamos <artefacto>
en <fuente de log> en la ventana <X>.">`

**13.2 Contenido de detección**

```yaml
# Sigma — <título>
# Autor, fecha, referencia al ATT&CK ID, nivel, falsos positivos conocidos
```

```yara
/* YARA — <familia> */
```

**13.3 Fuentes de log necesarias y brechas de visibilidad.** `<…>`

**13.4 Falsos positivos esperados y coste de triaje.** `<…>`

---

## 14. Brechas de inteligencia y nuevos requisitos de colección

| Brecha | Impacto en el juicio | Requisito propuesto | Disciplina | Prioridad |
|---|---|---|---|---|
| `<Sin visibilidad del vector de acceso inicial>` | KJ-1 queda en confianza baja | `<Solicitar logs del proveedor X>` | Telemetría de terceros | Alta |

---

# ANEXOS

## Anexo A — Indicadores de compromiso

> Los IOC son el nivel más perecedero y menos valioso del producto. Se entregan
> **con contexto, confianza y caducidad**, nunca como lista suelta.

| Tipo | Valor | Contexto (qué hacía) | Primera vez | Última vez | Confianza | Caduca | Acción permitida (PAP) |
|---|---|---|---|---|---|---|---|
| domain | `<…>` | C2 de `<familia>` | | | Alta | +30 d | Bloqueo |
| ipv4 | `<…>` | Nodo ORB compartido | | | Baja | +7 d | Solo monitorización — **no bloquear** |
| sha256 | `<…>` | Loader | | | Alta | Indefinido | Bloqueo |

*Nota de higiene:* marcar infraestructura compartida (CDN, proxy residencial,
servicios en la nube) para evitar bloqueos con impacto operativo.

## Anexo B — Fuentes y valoración

> Valoración doble tipo Admiralty/OTAN: **fiabilidad de la fuente (A–F)** ×
> **credibilidad de la información (1–6)**. Se valoran por separado.

| Fuente | Disciplina | Fiabilidad | Credibilidad | Acceso | Notas de sesgo |
|---|---|---|---|---|---|
| Telemetría EDR propia | Interna / TECHINT | A | 1 | Directo | Solo Windows |
| Informe de proveedor `<X>` | OSINT comercial | B | 2 | Publicado | Interés comercial en dramatizar |
| Persona en foro `<Y>` | HUMINT / CLOSINT | D | 3 | Encubierto | Posible desinformación; revisado por Legal |
| Sitio de filtración del actor | OSINT | C | 4 | Público | El actor controla el mensaje |

**Escalas**
- **A** completamente fiable · **B** normalmente fiable · **C** bastante fiable · **D** normalmente no fiable · **E** no fiable · **F** no evaluable.
- **1** confirmada por otras fuentes · **2** probablemente cierta · **3** posiblemente cierta · **4** dudosa · **5** improbable · **6** no evaluable.

## Anexo C — Léxico de probabilidad y confianza

**Probabilidad estimativa** *(qué tan probable es el hecho)*

| Término | Rango |
|---|---|
| Casi con certeza no / remoto | 1–5 % |
| Muy poco probable | 5–20 % |
| Poco probable | 20–45 % |
| Posibilidad real / en torno a par | 45–55 % |
| Probable | 55–80 % |
| Muy probable | 80–95 % |
| Casi con certeza | 95–99 % |

> Usar siempre el término **y** el porcentaje. No usar "podría" ni "es posible"
> como juicio: son afirmaciones no falsables.

**Nivel de confianza** *(qué tan sólida es la base del juicio)*

| Nivel | Criterio |
|---|---|
| Alta | Múltiples fuentes de calidad, corroboradas, sin brechas relevantes, razonamiento robusto |
| Moderada | Fuentes creíbles pero corroboración parcial o brechas conocidas |
| Baja | Fuente única, no corroborada, fuerte dependencia de supuestos o de inferencia |

## Anexo D — Marcos de referencia empleados

`MITRE ATT&CK vXX` · `MITRE D3FEND` · `Modelo del Diamante` · `Cyber Kill Chain`
· `Pirámide del Dolor` · `F3EAD` · `ICD 203 (estándares analíticos)` ·
`Técnicas Analíticas Estructuradas (ACH, KAC, pre-mortem)` · `TLP 2.0` · `PAP` ·
`STIX 2.1 / TAXII 2.1` · `Admiralty Code`

## Anexo E — Paquete legible por máquina

- Bundle STIX 2.1: `<ruta/uuid>`
- Evento MISP: `<id>` — taxonomías aplicadas: `tlp`, `admiralty-scale`, `estimative-language`, `PAP`
- Reglas: `<repositorio de detección / commit>`

## Anexo F — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | | Emisión inicial | |

## Anexo G — Realimentación del consumidor

| Pregunta | Respuesta |
|---|---|
| ¿Respondió a su requisito? | |
| ¿Qué decisión tomó o cambió con este informe? | |
| ¿Qué faltó? | |
| ¿Llegó a tiempo? | |

> Sin este anexo devuelto, el ciclo de inteligencia queda abierto y el próximo
> producto no mejora.
