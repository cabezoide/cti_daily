---
tlp: "TLP:CLEAR"
pap: "PAP:WHITE"
id: "CTI-2026-049"
version: "1.0"
tipo: "Perfil de operación de extorsión"
foco_regional: "Global · Brasil · Latinoamérica"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "settra · Settra"
fecha: "2026-11-19"
caduca: "2027-01-19"
autor: "Célula CTI"
distribucion: "Elaborado con fuentes abiertas y con medición propia sobre la interfaz pública de consulta de un rastreador de sitios de filtración. ADVERTENCIA DE CONTENIDO: el catálogo de este actor contiene datos personales de particulares —números de identificación fiscal, domicilios, teléfonos y correos personales de propietarios de las empresas atacadas—. Nada de ese material se reproduce en este informe, ni censurado ni parcialmente: se documenta el patrón y no el dato. Difusión libre, conservando la atribución y las salvedades de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-049

## Settra no extorsiona a la empresa: extorsiona al dueño, publicando su número de identificación fiscal y su domicilio

### Hallazgo propio no documentado en ninguna fuente · once sitios de filtración en cinco meses y sólo tres en pie

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-049` |
| Versión | 1.0 — 2026-11-19 |
| Clasificación | `TLP:CLEAR` · **`PAP:WHITE`** — no contiene indicadores accionables |
| Objeto | **`settra`**, séptimo puesto del ranking de siete días que motiva esta serie |
| Foco regional | **5 víctimas latinoamericanas de 116 (4,3 %): Brasil 3, México 1, Ecuador 1. Ninguna chilena** |
| Lo que lo distingue en este lote | **El modelo de presión: la exposición personal del propietario, no sólo los datos de la empresa.** Es un hallazgo propio: **ninguna de las cinco fuentes de proveedor consultadas lo describe** |
| Y lo que lo distingue en el otro sentido | **Es el catálogo más cuidadoso de los nuevos**: **116 de 116 entradas traen dominio** y **ninguna comparte fecha de ataque con la de publicación** |
| Horizonte | Estratégico 3–9 meses |
| Origen de los datos | **Medición propia** sobre 116 registros, más cinco fuentes de proveedor |
| Caducidad | **2027-01-19 (60 días)** |
| Autor | Célula CTI |

<!-- cti:note type="warn" -->

> ⚠ **Advertencia de contenido y decisión editorial, por delante de todo.**
>
> El catálogo de este actor contiene **datos personales de personas físicas**:
> números de identificación fiscal, domicilios particulares, teléfonos
> personales, correos personales y documentos laborales de propietarios y
> empleados de las empresas atacadas.
>
> **Este informe no reproduce ninguno de esos datos, ni censurados, ni
> parcialmente, ni como ejemplo.** No se transcribe un nombre, ni una
> dirección, ni un fragmento. **Se documenta el patrón y no el dato**, y la
> justificación del criterio está en el `Anexo D`, que lo convierte en método
> para la cartera.
>
> Y una segunda advertencia, de signo contrario: **el modelo de doxing que
> este informe describe no está documentado en ninguna de las cinco fuentes
> externas consultadas.** Es una observación propia sobre el catálogo público
> del actor. Se publica porque es verificable por cualquiera en la misma
> fuente, y se marca como propia y no corroborada (`B-1`, `G-1`).

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** **La palanca de extorsión de este actor no es la empresa: es el propietario como persona física, y eso es un cambio de modelo que ninguna fuente externa recoge.** En las descripciones de su propio sitio de filtración, las entradas detallan el contenido ofrecido en términos de **la exposición personal del dueño**: su número de identificación fiscal, su domicilio particular, su teléfono y su correo personales, sus declaraciones de retenciones fiscales, y el identificador fiscal de sus sociedades. Valoramos **casi con certeza** *(≥99 %)* que el patrón exista tal como lo describimos, porque lo leímos directamente en el catálogo publicado. **Confianza: alta para el patrón; y declaramos que es nuestra: ninguna de las cinco fuentes de proveedor consultadas lo menciona**, y una búsqueda dirigida a ello no devolvió nada. *Consecuencia, y es la que cambia la respuesta a un incidente:* **la negociación no la soporta la empresa, la soporta una persona**, y eso altera quién decide, con qué información y bajo qué presión (`E-2`).

**KJ-2.** **Y en el otro extremo del mismo catálogo hay un dato que lo distingue favorablemente de todos los actores nuevos del lote: sus entradas sí son verificables.** De sus **116 registros, los 116 traen dominio** y **113 traen captura de pantalla**. Para contraste, en el mismo conjunto de datos: `n0n` tiene **22 de 259** con dominio. Valoramos **casi con certeza** *(≥99 %)* las proporciones. **Confianza: alta.** *Consecuencia:* **este actor ofrece lo que hace falta para que un tercero compruebe sus reclamaciones**, y eso lo sitúa en un nivel de prueba muy superior al del resto de los nuevos (`Anexo D` de `CTI-2026-048`, nivel 2 y 5 frente a nivel 0).

**KJ-3.** **Es el único actor del lote que nunca publica con fecha del día: el 100 % de sus entradas declara una fecha de ataque distinta de la de publicación.** De 116 registros, **ninguno** tiene las dos fechas iguales. En el mismo conjunto de datos, `pixelleaks` y `curious worm` tienen el **100 %** de sus entradas con las dos fechas iguales, y `n0n` el 53 %. Valoramos **casi con certeza** *(≥99 %)* el dato. **Confianza: alta.** *Lectura:* **declarar cuándo ocurrió el ataque es aportar un dato comprobable contra la víctima, y es exactamente lo que un sitio sembrado no puede hacer.** Junto con `KJ-2`, sitúa a `settra` como una operación real con intrusiones reales, y no como un catálogo.

**KJ-4.** **Ha abierto once sitios de filtración en cinco meses y sólo tres siguen en pie, que es la rotación de infraestructura más rápida del lote.** El rastreador registra **once ubicaciones**, de las cuales **tres están marcadas como disponibles y ocho como no disponibles**, para una operación observada desde el 28 de junio de 2026. Para contraste, INC Ransom lleva ocho sitios en tres años. Valoramos **muy probable** *(80–95 %)* que esto refleje pérdida y reposición repetida de infraestructura. **Confianza: moderada** — el rastreador no fecha las bajas. *Consecuencia:* **cualquier vigilancia de este actor por la dirección de su sitio se pierde en semanas.**

**KJ-5.** **Su modelo de presión es regulatorio y relacional antes que técnico: amenaza con notificar a clientes, empleados, reguladores y potenciales demandantes.** Es la descripción que dan las fuentes de proveedor, y encaja con el contenido que publica —relaciones bancarias, documentos de terminación de empleados, pólizas de seguro, acuerdos de confidencialidad entre compañías—. Valoramos **probable** *(55–80 %)* que la amenaza de notificación a terceros sea un instrumento central y no accesorio. **Confianza: moderada.** *Consecuencia:* **el coste de no pagar no se mide en indisponibilidad sino en litigio, sanción y relación comercial**, y eso traslada la decisión de Seguridad a Legal (`E-4`).

**KJ-6.** **No está establecido que cifre, y las fuentes se contradicen.** Un proveedor afirma que **roba datos, cifra sistemas Windows y amenaza con publicar**; otro sostiene que **roba y publica datos a través de un sitio Tor sin un cifrador confirmado**. Nuestra medición aporta un dato compatible con la segunda: **de 116 entradas, ninguna declara tamaño de datos y ninguna declara cifra de rescate**, y el rastreador sólo le registra **una herramienta: Rclone, para exfiltración**. Valoramos **aproximadamente igual de probable** *(40–60 %)* cada posición. **Confianza: baja.** *Y la consecuencia es la misma que en `CTI-2026-048`:* **elegir medidas válidas en las dos ramas**, lo que aquí significa control de egreso antes que restauración.

**KJ-7.** **Su exposición regional es baja y su país regional es Brasil, con tres víctimas. Ninguna chilena.** De 116 registros, **5 son latinoamericanos —el 4,3 %—**: Brasil 3, México 1, Ecuador 1. Su geografía es Estados Unidos 55, Alemania 9, Reino Unido 8, Canadá 4, con **once registros sin país**. Valoramos **moderada** la confianza. *Consecuencia:* para una organización chilena es hoy **ruido del ranking**; para una brasileña pequeña o mediana, una amenaza marginal pero presente.

**KJ-8.** **Y hay un desajuste de recuentos que conviene consignar: un proveedor habla de 65 víctimas confirmadas donde nosotros contamos 116 entradas.** Valoramos **casi con certeza** *(≥99 %)* que las dos cifras sean correctas para su método y su fecha. **Confianza: alta.** *Y la lectura, que es menos alarmante que en `CTI-2026-048`:* la diferencia es de **1,8 veces**, no de un orden de magnitud, y es compatible con momentos de medición distintos y con criterios distintos de «confirmada». **Con 116 de 116 entradas con dominio, este catálogo no da la impresión de estar inflado.**

---

## 2. Resumen ejecutivo

`settra` apareció el 28 de junio de 2026 y ocupa el séptimo puesto del ranking que motiva esta serie. De los seis actores nuevos del lote es, con diferencia, **el más sólido**: sus **116 entradas traen las 116 un dominio identificable**, 113 traen captura de pantalla, y **ninguna publica con fecha del día** —el 100 % declara una fecha de ataque anterior y distinta—. Nada de eso lo puede hacer un sitio sembrado. Son intrusiones reales, y se pueden comprobar.

Lo que hace a este actor distinto no es su volumen sino **a quién aprieta**. Al leer su catálogo, la palanca que ofrece no es «tenemos los datos de su empresa»: es **la exposición personal del propietario**. Las entradas detallan lo que van a publicar en términos del dueño como persona física —su número de identificación fiscal, su domicilio particular, su teléfono y su correo personales, sus declaraciones fiscales— junto a material corporativo elegido por su capacidad de dañar relaciones: acuerdos de confidencialidad entre compañías, relaciones bancarias, documentos de terminación de empleados, pólizas de seguro.

**Ese modelo no está descrito en ninguna de las cinco fuentes de proveedor que consultamos**, y una búsqueda dirigida a encontrarlo no devolvió nada. Es una observación propia, verificable por cualquiera en la misma fuente pública, y se publica marcada como tal. **Este informe no reproduce ninguno de esos datos personales** —ni censurados, ni como ejemplo— y el `Anexo D` convierte ese criterio en método para la cartera, porque es la primera vez que esta serie se topa con un catálogo cuyo contenido daña a terceros sólo por citarlo.

La consecuencia práctica es de gobierno y no de tecnología. Cuando la palanca es la empresa, la decisión de pagar la toma un comité con asesoría. **Cuando la palanca es el domicilio y el número fiscal de una persona concreta —que en una empresa pequeña o mediana suele ser quien decide—, la negociación la soporta esa persona, bajo una presión que no es la del comité.** Y el coste de no pagar no se mide en horas de indisponibilidad sino en **litigio, sanción regulatoria y relación comercial rota**, porque este actor amenaza explícitamente con notificar a clientes, empleados, reguladores y potenciales demandantes. Eso traslada la decisión de Seguridad a Legal, y conviene que Legal lo sepa antes y no durante.

Dos cosas más. **No está establecido que cifre**: un proveedor dice que sí, otro que no hay cifrador confirmado, y el rastreador sólo le registra una herramienta —Rclone, para exfiltrar—. Y **ha abierto once sitios de filtración en cinco meses, de los que sólo tres siguen en pie**: la rotación de infraestructura más rápida del lote, lo que hace inútil cualquier vigilancia por dirección.

Para esta región: **cinco víctimas latinoamericanas de 116, tres brasileñas, ninguna chilena.**

---

## 3. Alcance y limitaciones

### 3.1 Qué cubre

La operación `settra`: la estructura y verificabilidad de su catálogo, **el modelo de presión por exposición personal del propietario**, su rotación de infraestructura, su victimología, la cuestión abierta del cifrado, y el criterio de tratamiento de datos personales de terceros que su caso obligó a establecer.

### 3.2 Qué NO cubre

| Fuera de alcance | Por qué |
|---|---|
| **Los datos personales de su catálogo** | **Decisión editorial expresa.** No se reproducen ni censurados. `Anexo D` |
| **Una cadena de intrusión** | **No hay material.** El rastreador no le registra TTP y sólo una herramienta. Es `G-2` |
| **El cifrador** | Dos fuentes incompatibles (`KJ-6`) |
| **Los nombres de las víctimas** | Decisión de higiene de la serie, y aquí es más grave que en los demás informes porque las entradas contienen datos de personas asociadas a esas empresas |
| **Indicadores** | **No hay ninguno.** `PAP:WHITE` |

### 3.3 Limitaciones de la colección

<!-- cti:note type="warn" -->

> ⚠ **Seis limitaciones.**
>
> 1. **El hallazgo central es propio y no está corroborado.** Ninguna fuente
>    externa describe el modelo de doxing. Es verificable por cualquiera en la
>    fuente pública, **pero nadie más lo ha publicado** (`G-1`).
> 2. **Fuente única para la medición propia.**
> 3. **Once registros sin país** de 116, y el rastreador no asigna sector a
>    todos.
> 4. **No podemos citar la evidencia del hallazgo central.** Es la consecuencia
>    directa de la decisión editorial: **el lector no puede comprobar `KJ-1` a
>    partir de este documento**, sólo desde la fuente. Se asume como coste y se
>    declara.
> 5. **Las fuentes de proveedor discrepan** sobre el cifrado y sobre el
>    recuento (65 frente a 116).
> 6. **El rastreador no fecha la baja de los ocho sitios caídos**, de modo que
>    `KJ-4` describe un estado y no una cronología.

### 3.4 Qué aporta

| Aporte | Dónde |
|---|---|
| **El modelo de presión por exposición personal del propietario** — hallazgo propio no documentado | `KJ-1`, `E-2` |
| **La medición de verificabilidad**: 116 de 116 con dominio, frente a 22 de 259 de `n0n` | `KJ-2`, `O-2` |
| **El 0 % de entradas con fecha de ataque igual a la de publicación**, como señal de operación real | `KJ-3` |
| **La rotación de infraestructura más rápida del lote**: once sitios en cinco meses, tres en pie | `KJ-4` |
| **El traslado de la decisión de Seguridad a Legal** que el modelo de notificación impone | `KJ-5`, `E-4` |
| **Un criterio de tratamiento de datos personales de terceros en un producto CTI** | `Anexo D` |

### 3.5 Veredicto

<!-- cti:table highlight="CORROBORADO|NO SOSTENIDO|SIN RESOLVER|propio" -->

| # | Elemento | Veredicto | Base |
|---|---|---|---|
| 1 | `settra` extorsiona publicando datos de la empresa | **INCOMPLETO — y la parte que falta es el hallazgo** | **Publica datos personales del propietario** (`KJ-1`, hallazgo propio) |
| 2 | Su catálogo es verificable por terceros | **CORROBORADO, y es el mejor del lote de nuevos** | **116 de 116 con dominio** (`KJ-2`) |
| 3 | Es un sitio sembrado con datos reciclados | **NO SOSTENIDO** | **0 % de entradas con fecha del día**; 116 con dominio (`KJ-3`) |
| 4 | Su infraestructura de publicación es estable | **NO SOSTENIDO** | **Once sitios en cinco meses, ocho caídos** (`KJ-4`) |
| 5 | Es una operación de ransomware con cifrado | **SIN RESOLVER** | Dos fuentes incompatibles; cero magnitudes en 116 entradas (`KJ-6`) |
| 6 | La presión es técnica (indisponibilidad) | **NO SOSTENIDO** | Es **regulatoria y relacional**: notificación a clientes, empleados, reguladores y demandantes (`KJ-5`) |
| 7 | Es una amenaza medida para Chile | **NO SOSTENIDO** | **Cero víctimas chilenas** de 116 (`KJ-7`) |
| 8 | Su recuento está inflado | **NO SOSTENIDO** | 65 confirmadas frente a 116 entradas: **×1,8, no un orden de magnitud** (`KJ-8`) |

---

# NIVEL ESTRATÉGICO
### Para: CISO, Legal, Dirección, Riesgo · Horizonte: 3–9 meses

## E-1. Qué clase de operación es

<!-- cti:cards -->

| Rasgo | Qué significa | Etiqueta |
|---|---|---|
| **Extorsiona al propietario como persona física** | La negociación la soporta una persona, no un comité. **Es el rasgo que cambia la respuesta** | `01 · palanca personal` |
| **116 de 116 entradas con dominio** | Sus reclamaciones son comprobables. **No es un catálogo inflado** | `02 · verificable` |
| **Nunca publica con fecha del día** | Declara cuándo ocurrió el ataque: aporta un dato contra sí mismo | `03 · fecha declarada` |
| **Amenaza con notificar a reguladores y demandantes** | El coste de no pagar es litigio y sanción, no indisponibilidad | `04 · presión regulatoria` |
| **Once sitios en cinco meses** | Vigilancia por marca, nunca por dirección | `05 · rotación extrema` |
| **Una sola herramienta registrada: Rclone** | **No hay material para detección específica.** El control es de egreso | `06 · sin TTP útiles` |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `116` | Entradas en 2026 | Desde el 2026-06-28 |
| `116 / 116` | Entradas **con dominio identificable** | **El 100 %. Frente a 22 de 259 de `n0n`** |
| `113 / 116` | Entradas con captura de pantalla | El 97 % |
| `0 %` | Entradas con fecha de ataque igual a la de publicación | **El único del lote.** `pixelleaks` y `curious worm`: 100 % |
| `11 → 3` | Sitios de filtración abiertos → activos | **En cinco meses.** La rotación más rápida del lote |
| `1` | Herramientas registradas | Rclone, para exfiltración |
| `0` | Entradas con tamaño de datos o cifra de rescate | De 116 |
| `4` | Entradas con referencia de prensa | De 116. **Pocas, pero no cero** — frente a 0 de 259 de `n0n` |
| `5` | Víctimas latinoamericanas | **4,3 %. Brasil 3 · México 1 · Ecuador 1. Ninguna chilena** |
| `65 ≠ 116` | Víctimas «confirmadas» por un proveedor ≠ entradas medidas | **×1,8**, no un orden de magnitud |

## E-2. El modelo de presión, y por qué cambia la respuesta

**Lo que este actor ofrece en sus entradas, agrupado por a quién daña:**

| Clase de material | A quién expone | Efecto buscado |
|---|---|---|
| **Número de identificación fiscal, domicilio, teléfono y correo personales del propietario** | **Una persona física** | **Presión directa sobre quien decide.** En una empresa pequeña o mediana, el dueño y el decisor son la misma persona |
| **Declaraciones fiscales de retenciones e identificadores fiscales de sus sociedades** | La persona y sus empresas | Exposición patrimonial y riesgo fiscal |
| **Documentos de terminación de empleados** | **Terceros que no son parte** | Daño reputacional y riesgo laboral |
| **Acuerdos de confidencialidad entre compañías, firmados a nivel de dirección** | **Contrapartes comerciales** | Rotura de relaciones y posible incumplimiento contractual |
| **Relaciones bancarias y pólizas de seguro** | La empresa | Riesgo financiero y de cobertura |

**Por qué eso no es «lo mismo con otro nombre».** Una extorsión clásica por datos amenaza con una consecuencia **de la organización**: pérdida de propiedad intelectual, exposición de clientes, incumplimiento normativo. La decisión de pagar se toma con asesoría, con seguro y con un cálculo institucional.

**Este modelo amenaza con una consecuencia de una persona.** Y hay tres diferencias que importan:

1. **Quien sufre la presión suele ser quien decide**, de modo que desaparece la separación entre el afectado y el decisor que hace posible una decisión fría.
2. **El daño no se puede remediar con medidas de la organización.** Una copia de seguridad no devuelve un domicilio a la privacidad. **No hay restauración posible**, y por tanto la única defensa es que los datos no salgan.
3. **Y el daño alcanza a terceros que no son parte del incidente** —empleados despedidos, contrapartes de un acuerdo de confidencialidad—, lo que convierte la respuesta en un problema de notificación y de responsabilidad que excede a Seguridad.

> **La consecuencia de gobierno, y es la razón de que este informe esté
> dirigido a Legal y a Dirección antes que al SOC: el plan de respuesta a
> extorsión de la mayoría de las organizaciones supone que la víctima es la
> organización.** Si la palanca es la exposición personal de una persona
> concreta, **ese plan no contempla ni quién decide, ni con qué apoyo, ni qué
> se le debe a esa persona.** Y es exactamente la clase de pregunta que no se
> puede responder durante un incidente.

## E-3. Lo que su catálogo tiene de sólido, y por qué conviene decirlo

Este informe es duro con el modelo de este actor y tiene que ser justo con su catálogo, porque la diferencia con los otros nuevos del lote es grande y es medible:

| Medida | `settra` | `n0n` | `pixelleaks` | `curious worm` |
|---|---|---|---|---|
| Entradas | 116 | 259 | 34 | 18 |
| **Con dominio** | **116 (100 %)** | **22 (8,5 %)** | 13 (38 %) | — |
| Con captura | 113 (97 %) | 259 (100 %) | **0 (0 %)** | — |
| **Con fecha de ataque distinta de la publicación** | **116 (100 %)** | 47 % | **0 (0 %)** | **0 (0 %)** |
| Con referencia de prensa | 4 | **0** | — | — |
| Antigüedad | **5 meses** | 2 meses | 16 días | 8 días |

**Las dos filas en negrita son las que separan una operación de un catálogo.** Un sitio que publica el 100 % de sus entradas con dominio y el 100 % con una fecha de ataque anterior y distinta **está ofreciendo a la víctima y a los terceros exactamente los dos datos necesarios para comprobarlo**. Un sitio sembrado no puede hacer eso: no sabe cuándo ocurrió nada.

> **Y la observación incómoda que se sigue: el actor con el modelo de presión
> más agresivo del lote es también el que publica el catálogo más honesto.**
> Las dos cosas son coherentes, y conviene entender por qué: **un extorsionador
> que apunta al propietario necesita ser creído por él**, y la credibilidad se
> compra con datos comprobables. **La precisión del catálogo no es un signo de
> escrúpulo: es un instrumento de la misma presión.**

## E-4. Decisiones que este informe pide

| # | Decisión | A quién | Coste | Por qué |
|---|---|---|---|---|
| **1** | **Revisar si el plan de respuesta a extorsión contempla que la palanca sea la exposición personal de una persona concreta** | **Legal · Dirección** | Bajo decidirlo | `E-2`. **La medida principal de este informe, y no es técnica.** Quién decide, con qué apoyo, y qué se le debe a esa persona |
| **2** | **Control de egreso: destinos autorizados y volumen por destino** | Red | Medio | Vale **con y sin cifrado** (`KJ-6`), y es la única defensa de un daño que no se puede restaurar |
| **3** | **Si somos una pyme: asumir que el dueño es el objetivo de la presión** | Dirección | Cero | `E-2`. Y preparar apoyo legal personal, no sólo corporativo |
| **4** | **Anticipar la vía de notificación a reguladores y a terceros afectados** | Legal · Comunicación | Medio | `KJ-5`: el actor amenaza con hacerlo él. **Hacerlo primero quita la palanca** |
| **5** | **Inventariar qué datos personales de directivos y empleados hay en sistemas corporativos** | Cumplimiento · TI | Medio | Es lo que este actor busca. **La mayoría de las organizaciones no lo sabe** |
| **6** | **No vigilar este actor por dirección de sitio** | CTI | Cero | `KJ-4`: once en cinco meses |
| **7** | **No reproducir su material en informes internos** | CTI | Cero | `Anexo D`. Citarlo daña a los terceros otra vez |

---

# NIVEL OPERACIONAL
### Para: SOC, CTI, Cumplimiento · Horizonte: semanas

## O-1. Identificación

| Campo | Valor |
|---|---|
| Nombre | **`settra`** · también **`Settra`** |
| Alias | Ninguno conocido |
| En el rastreador desde | **2026-06-28** |
| Primera identificación por proveedores | **Junio de 2026** |
| Sitios de filtración | **Once registrados, tres activos** |
| Canales de negociación | **Tox y portales de chat en la red oscura**, según proveedor; panel de chat para la víctima; notificaciones privadas de filtración tras el vencimiento |
| Herramientas registradas | **Una: Rclone** (exfiltración) |
| TTP registradas | **Ninguna** |
| Cifrado | **En disputa** (`KJ-6`) |
| Aviso gubernamental | Ninguno |

## O-2. La anatomía de una entrada suya

| Campo | Presente en | Lectura |
|---|---|---|
| **Dominio** | **116 de 116 (100 %)** | **El dato que hace comprobable una reclamación.** El mejor del lote |
| Captura de pantalla | 113 de 116 (97 %) | |
| **Fecha de ataque distinta de la de publicación** | **116 de 116 (100 %)** | **Único en el lote.** Aporta un dato comprobable contra sí mismo |
| Referencia de prensa | **4 de 116** | Pocas, **pero no cero**: hay casos recogidos por terceros |
| Tamaño de datos | 0 de 116 | No publica magnitudes |
| Cifra de rescate | 0 de 116 | Tampoco |
| **Descripción con inventario del material** | La mayoría | **Y es donde está el hallazgo de `KJ-1`**: el inventario se expresa en términos de exposición personal |

**La forma de sus descripciones**, descrita sin reproducir ningún dato: una sección que anuncia **qué hay dentro**, enumerando documentos concretos con su clase —identificación fiscal del propietario, domicilio, contacto personal, declaraciones fiscales, identificador fiscal de sociedades—; y en otras entradas, un documento corporativo singular presentado por su valor de daño relacional, como un acuerdo de confidencialidad entre dos compañías firmado a nivel de dirección, con una nota sobre el objeto de la negociación.

> **Y conviene notar la precisión del lenguaje, porque es informativa: las
> descripciones no son genéricas.** Enumeran documentos nombrados, con sus
> identificadores y sus fechas. **Eso no se puede escribir sin tener el
> material delante**, y es, junto con `KJ-2` y `KJ-3`, la tercera razón para
> valorar que las intrusiones son reales.

## O-3. La actividad medida, sobre las dos bases

| Ventana | Por **fecha de ataque** | Por **publicación** | Nota |
|---|---|---|---|
| Total 2026 | 116 | 116 | Desde el 28-06 |
| Últimos 30 días | 15 | **22** | |
| **Últimos 7 días** | **0** | **10** | **El caso opuesto a INC Ransom**: aquí la cuenta por fecha de ataque da cero |
| Ranking del sitio *(16:20 UTC del 19-11)* | — | — | **13** |
| Pico en un día | — | 11 el 2026-06-30 | Modesto: no publica en tandas grandes |

**El cero de la cuenta por fecha de ataque merece explicación.** Significa que **ninguna de las entradas publicadas en los últimos siete días declara un ataque ocurrido en esos siete días**: todas se refieren a intrusiones anteriores. Es coherente con `KJ-3` y con una operación que negocia antes de publicar.

**Geografía** *(sobre los 105 con país)*: Estados Unidos 55, Alemania 9, Reino Unido 8, Canadá 4, **Brasil 3**. **Sectores**: Servicios profesionales 21, Manufactura 17, Tecnología 17, Comercio minorista 13.

## O-4. Nuestra exposición

| Si la organización… | Exposición | Medida |
|---|---|---|
| **Es una pyme con propietario identificable** | **La más alta para este actor, con independencia del país** | `E-4.1` y `E-4.3`: el plan de respuesta y el apoyo a la persona |
| **Es chilena** | **Ninguna medida**: cero víctimas de 116 | Vigilancia pasiva |
| **Es brasileña** | **Baja**: tres víctimas | Control de egreso |
| **Tiene datos personales de directivos en sistemas corporativos** | **Alta en términos de daño** | `E-4.5`: inventariarlos |
| **Opera bajo acuerdos de confidencialidad relevantes** | **Alta en términos de daño relacional** | Igual |
| **Es de servicios profesionales, manufactura o tecnología** | Baja-media | Sus tres sectores principales |

## O-5. Hipótesis alternativas y pre-mortem

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| **H-1 — El doxing del propietario es un modelo deliberado y sistemático** | **Retenida como principal.** Aparece en las descripciones con estructura de inventario, no como anécdota | `Probable · 55–80 %` |
| **H-2 — Es un rasgo de las víctimas y no del actor** | **Retenida como alternativa seria.** Si ataca sobre todo a pymes, el material disponible **será** personal del dueño sin que haya elección deliberada: en una empresa pequeña los datos del propietario están en los mismos sistemas. **No podemos distinguirlo con estos datos**, y es `G-3` | `Posibilidad real · 40–60 %` |
| **H-3 — No tiene cifrador** | **Retenida al mismo nivel que su contraria.** Una herramienta registrada —Rclone— y cero magnitudes publicadas lo apoyan | `Aprox. igual de probable · 40–60 %` |
| **H-4 — Los ocho sitios caídos lo fueron por acción de terceros** | **Sin evidencia.** El rastreador no fecha las bajas | `Aprox. igual de probable · 40–60 %` |
| **H-5 — El catálogo está inflado** | **Poco probable.** 116 de 116 con dominio y 100 % con fecha de ataque declarada. La diferencia con las 65 «confirmadas» de un proveedor es de ×1,8 | `Poco probable · 20–45 %` |
| **H-6 — El hallazgo de `KJ-1` ya está documentado y no lo encontramos** | **Retenida como limitación nuestra.** Buscamos expresamente y no apareció, pero **la ausencia en una búsqueda no es ausencia en la literatura** | `Posibilidad real · 40–60 %` |

**Pre-mortem — si este informe se equivoca, será porque:**

1. **`H-2` es cierta**: el doxing es un subproducto de atacar pymes y no un modelo. **Es el riesgo 1**, y cambiaría el encuadre aunque no las medidas de `E-4`.
2. **Alguien reprodujo el material** en un informe interno, dañando otra vez a los terceros (`Anexo D`).
3. **Se leyó «catálogo honesto» como «actor menos dañino»** (`E-3`), cuando la precisión del catálogo es un instrumento de la presión.
4. **Se dimensionó la respuesta suponiendo cifrado**, o suponiendo que no lo hay (`KJ-6`).
5. **Se tomó la ausencia de víctimas chilenas como garantía** con once registros sin país.
6. **El hallazgo central estaba publicado y no lo encontramos** (`H-6`), en cuyo caso el informe acierta en el fondo y se equivoca al reclamarlo como propio.

---

# NIVEL TÁCTICO Y TÉCNICO
### Para: SOC, Cumplimiento · Horizonte: días

<!-- cti:note type="warn" -->

> ⚠ **Como en `CTI-2026-048`, este informe no tiene nivel táctico en el
> sentido habitual, y se dice en lugar de rellenarlo.** El rastreador no le
> registra ninguna TTP y una sola herramienta. No hay muestras, no hay
> indicadores y no hay análisis técnico de proveedor con detalle.
>
> **Lo que sigue son las comprobaciones posibles, y la única regla de detección
> que su inventario permite escribir.**

## T-1. Comprobaciones posibles

| # | Comprobación | Cómo | Qué significa |
|---|---|---|---|
| **H-1** | **¿Hay egreso con Rclone, o a destinos de almacenamiento no corporativos?** | Procesos y flujo de salida | **La única herramienta registrada del actor**, y la medida vale contra todo el lote |
| **H-2** | **¿Aparecemos listados?** | Buscar nuestro dominio en el rastreador. **Con 116 de 116 entradas con dominio, aquí la búsqueda sí es concluyente** | A diferencia de `CTI-2026-048`, **la ausencia en su catálogo es informativa** |
| **H-3** | **¿Qué datos personales de directivos y empleados hay en sistemas corporativos, y quién accede a ellos?** | Inventario de cumplimiento | **La comprobación propia de este expediente.** Es lo que el actor busca, y casi ninguna organización lo sabe |
| **H-4** | **¿Hay acceso amplio a repositorios de recursos humanos, nóminas o legal desde cuentas que no lo necesitan?** | Revisión de permisos | Reduce el material disponible para esta clase de presión |
| **H-5** | **¿Hay segundo factor resistente a suplantación en todos los accesos remotos?** | Identidad | Medida general del lote |

## T-2. La única regla específica que su inventario permite

```
# Rclone es la única herramienta registrada de este actor, y es legítima:
# se usa a diario para sincronizar y respaldar. La señal es el DESTINO.
DESTINOS_OK = { ... destinos de sincronización y respaldo autorizados ... }

si proceso.nombre == "rclone" o linea_de_ordenes contiene "rclone":
    si destino not in DESTINOS_OK:
        alertar "RCLONE A DESTINO NO AUTORIZADO"      # severidad alta
    si no:
        registrar    # el uso legítimo también interesa, para la línea base

# Y la variante que no depende de reconocer la herramienta:
si bytes_salientes(host, 1h) > umbral(host) y destino not in DESTINOS_OK:
    alertar "VOLUMEN DE EGRESO ANÓMALO A DESTINO NO AUTORIZADO"
```

> **La segunda regla es la que importa y es la misma que `CTI-2026-047` pedía
> por otra razón.** Cuando un actor no deja TTP conocidas, **la detección
> tiene que apoyarse en lo que cualquier exfiltración produce
> inevitablemente: volumen saliente hacia un destino que no es nuestro.** Es
> la medida con mejor relación coste-beneficio de los cuatro informes de esta
> serie emitidos hasta ahora.

---

## 14. Brechas de inteligencia y requisitos de colección

| # | Brecha | Impacto | Cómo se cierra | Prioridad |
|---|---|---|---|---|
| **G-1** | **El hallazgo central no está corroborado por ninguna fuente externa** | `KJ-1` es propio y solitario | **Que alguien más lo publique, o que un proveedor lo refute.** Y mientras, está marcado como propio | **1** |
| **G-2** | **Ninguna TTP registrada y una sola herramienta** | Hace imposible una detección específica. `PAP:WHITE` | Informe de respuesta a incidentes de una víctima real | **1** |
| **G-3** | **No sabemos si el doxing es modelo del actor o subproducto de atacar pymes** | Es `H-2`, el riesgo 1 del pre-mortem | **Comprobar si sus víctimas grandes también traen datos del propietario.** Se puede hacer con los datos que ya tenemos, con un criterio de tamaño de víctima definido antes de mirar | **1** |
| **G-4** | **No está establecido si cifra** | `KJ-6`, y determina qué defensa aplica | Muestra o informe de incidente | 2 |
| **G-5** | **No sabemos por qué cayeron ocho de sus once sitios** | `H-4` | Fechas de baja del rastreador; anuncios oficiales | 2 |
| **G-6** | **El desajuste 65 frente a 116 no está explicado** | `KJ-8` | Criterio de «confirmada» del proveedor | 3 |
| **G-7** | **No sabemos qué proporción de su material corporativo es de terceros no atacados** | Los acuerdos de confidencialidad exponen a la contraparte, que no es víctima del incidente. **Es un problema de notificación que nadie está mirando** | Análisis del catálogo con criterio de «tercero no atacado» | 2 |

**Disparadores de reevaluación.** `I-1`: que una fuente externa documente o refute el modelo de doxing (`G-1`). `I-2`: aparición de una víctima grande con datos del propietario publicados, que apoyaría `H-1` frente a `H-2`. `I-3`: aparición de muestras del cifrador. `I-4`: primera víctima chilena. `I-5`: caída de los tres sitios activos. `I-6`: que empiece a publicar magnitudes —tamaños o cifras de rescate—, lo que indicaría cambio de modelo.

---

# ANEXOS

## Anexo A — Indicadores

### A.1 — ⚠ Sin indicadores de compromiso, y con una prohibición expresa

<!-- cti:note type="warn" -->

> ⚠ **No hay indicadores:** ni direcciones, ni dominios, ni hashes, ni
> ficheros. Una sola herramienta registrada, y es legítima. De ahí el
> **`PAP:WHITE`**.
>
> **Y hay una prohibición que este informe establece y que no es técnica: no
> se reproduce, ni en este anexo ni en ningún otro lugar, ningún dato personal
> procedente del catálogo de este actor.** No se ingiere, no se cita, no se
> conserva censurado. El `Anexo D` explica por qué y lo convierte en criterio
> de la cartera.

### A.2 — Patrones de reconocimiento y de detección

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| pattern | **Egreso con Rclone hacia un destino que no está en la lista de destinos autorizados** | **La única regla específica que su inventario permite escribir.** Rclone es legítimo: la señal es el destino | Media-alta; requiere la lista previa | Sin caducidad | **Alerta** (`T-2`) |
| pattern | **Volumen de egreso anómalo hacia un destino no corporativo** | **La regla que no depende de conocer la herramienta**, y la de mejor relación coste-beneficio de la serie | Media-alta | Sin caducidad | Alerta |
| pattern | **Entrada de sitio de filtración cuyo inventario de material enumera datos personales del propietario** | **El patrón de reconocimiento de este actor** (`KJ-1`), descrito sin reproducir ningún dato | **Alta como observación propia; no corroborada** | Mientras mantenga el modelo | **Reconocimiento.** No es indicador de compromiso |
| pattern | **Entrada con dominio y con fecha de ataque anterior y distinta de la de publicación** | **La firma de una operación real frente a un sitio sembrado** (`KJ-2`, `KJ-3`). Se generaliza en `CTI-2026-048` `Anexo D` | Alta | Sin caducidad como método | Graduación de la prueba |

### A.3 — Victimología y decisiones de higiene

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| cartera | **116 entradas · 116 con dominio · 113 con captura · 4 con prensa · 0 con tamaño · 0 con rescate · 0 % con fecha del día** | La anatomía de `O-2`. **El catálogo más verificable de los nuevos del lote** | Alta como recuento | 60 días | Medición |
| cartera | **5 víctimas latinoamericanas (4,3 %): BR 3 · MX 1 · EC 1. Ninguna chilena** | `KJ-7`, con once registros sin país como salvedad | Moderada | 60 días | Priorización |
| cartera | **Once sitios de filtración registrados, tres activos** | `KJ-4`. **Las direcciones no se transcriben**: ocho ya cayeron en cinco meses | Alta | Volátil | Vigilancia por marca |
| cartera | **⚠ NO se reproduce ningún dato personal del catálogo de este actor**, ni censurado, ni parcial, ni como ejemplo | **La decisión central del informe.** Son datos de personas físicas que no son parte del incidente más allá de ser su víctima. Citarlos las daña otra vez, y un informe de inteligencia **no es un vehículo neutral**: añade alcance y credibilidad | — | — | **Prohibido ingerir.** `Anexo D` |
| cartera | **No se transcribe ningún nombre de víctima** | Regla de la serie, y aquí más grave: las entradas asocian personas concretas a esas empresas | — | — | No ingerir |

## Anexo B — Fuentes y valoración

| Fuente | Disciplina | Fiab. | Cred. | Grado | Notas |
|---|---|---|---|---|---|
| **`B-1` — Medición propia** sobre 116 registros, incluida la **lectura directa de las descripciones del catálogo** | OSINT técnico · **medición propia** | **B** | **2** | **Medición propia** | **Es la única fuente del hallazgo central** (`KJ-1`). Su virtud: el patrón se lee directamente en el material público del adversario y **cualquiera puede comprobarlo en la misma fuente**. Su debilidad: **nadie más lo ha publicado** (`G-1`), y este informe no puede citar la evidencia por la decisión editorial de `Anexo D` |
| **`B-2` — Perfiles de proveedor** (Cynet, Moxfive, Halcyon, CyberXtron, Derp.ca) | OSINT comercial | **C** | **3** | Proveedor | Fuente de la primera identificación en **junio de 2026**, de los canales de negociación —**Tox y portales de chat**—, del contenido genérico de las páginas de víctima —información financiera, correos, detalles legales, relaciones bancarias, **documentos de terminación de empleados**, seguros—, de los **temporizadores de cuenta atrás**, de la **amenaza de notificar a clientes, empleados, reguladores y potenciales demandantes**, y de las **65 víctimas confirmadas**. **Discrepan entre sí sobre el cifrado** (`KJ-6`). Una de ellas menciona de forma vaga «acceso a información de usuarios», que es lo más cerca que la literatura llega del hallazgo de `KJ-1` **sin llegar** |
| **`B-3` — Fichas de víctima de terceros** (GalaxyWarden, cyberthreatintelligence.net) | OSINT · compilación | **C** | **4** | Compilación | Confirman la continuidad de publicaciones hasta el otoño de 2026 y **advierten expresamente de que las reclamaciones no están verificadas de forma independiente** |
| **`B-4` — Datos comparativos del mismo rastreador para los otros actores del lote** | OSINT técnico · medición propia | **B** | **2** | Medición propia | Lo que hace utilizable la tabla de `E-3`: todas las filas, el mismo día, la misma metodología |

> **Una observación franca sobre esta estructura: el hallazgo central de este
> informe tiene una sola fuente, es nuestra, y el informe se ha privado
> deliberadamente de poder citarla.** Es una combinación incómoda y hay que
> enunciarla: **el lector no puede verificar `KJ-1` leyendo este documento.**
> Puede verificarlo en la fuente pública, que está identificada, y eso es todo
> lo que podemos ofrecer sin reproducir datos de personas. **Preferimos un
> juicio verificable sólo en origen a un juicio ilustrado con el domicilio de
> alguien.**

## Anexo C — Léxico de probabilidad y confianza

<!-- cti:bars title="Probabilidad estimativa" -->

| Etiqueta | Valor |
|---|---|
| Casi con certeza (≥99 %) | 99 |
| Muy probable (80–95 %) | 88 |
| Probable (55–80 %) | 68 |
| Aproximadamente igual de probable (40–60 %) | 50 |
| Poco probable (20–45 %) | 32 |
| Muy poco probable (5–20 %) | 12 |
| Remoto (≤5 %) | 4 |

**Confianza**: **alta** —fuentes múltiples corroboradas, método expuesto—; **moderada** —fuente única de calidad, o inferencia propia sobre datos verificables—; **baja** —dato ausente o inferencia indirecta—.

> **La distinción que este informe obliga a hacer: hay que separar la
> confianza en que el PATRÓN existe de la confianza en que el patrón sea
> DELIBERADO.**
>
> «Las descripciones de este actor enumeran datos personales del propietario»
> es una observación directa sobre material público: confianza **alta**. «Este
> actor elige deliberadamente al propietario como palanca» es una **atribución
> de intención**, y su alternativa —que sea un subproducto de atacar pymes,
> donde esos datos están en los mismos sistemas— es seria y no se puede
> descartar: confianza **moderada** y probabilidad *probable*, no *muy
> probable*.
>
> **La regla:** un patrón observado en el material del adversario se afirma con
> la confianza de la observación; **su intención, nunca.** Y conviene que la
> diferencia se note en la redacción, porque la frase «extorsiona al dueño»
> arrastra una intención que la frase «sus entradas enumeran datos del dueño»
> no arrastra.

## Anexo D — Qué hacer con un catálogo de extorsión que contiene datos de personas

**El problema, y es nuevo para esta cartera.** Un sitio de filtración publica material robado. Hasta ahora, en los informes de extorsión de esta cartera, ese material era corporativo: contratos, código, bases de clientes. **El catálogo de este actor contiene datos de personas físicas identificables** —identificación fiscal, domicilio, teléfono, correo personal, documentos laborales de empleados despedidos—, y un informe de inteligencia que los cite **vuelve a publicarlos, con el alcance y la credibilidad de un informe de inteligencia**.

**El criterio que esta cartera adopta, en cinco reglas.**

| # | Regla | Razón |
|---|---|---|
| **1** | **El patrón se documenta; el dato no se reproduce.** «Sus entradas enumeran el identificador fiscal y el domicilio del propietario» es informativo. Transcribir uno no añade nada analítico | Un informe se juzga por las decisiones que habilita. **Un domicilio concreto no habilita ninguna** |
| **2** | **No se reproduce ni censurado.** Ni con dígitos ocultos, ni con el nombre abreviado, ni «como ejemplo» | La censura parcial es reversible por correlación, y la completa **no aporta nada que la descripción del patrón no diera** |
| **3** | **No se nombra a la víctima cuando la entrada asocia a personas concretas con ella** | Nombrar la empresa permite localizar a las personas. **El daño es por identificabilidad, no por el nombre** |
| **4** | **Se identifica la fuente para que el patrón sea verificable en origen** | **Es el coste de la regla 1**: el lector no puede comprobarlo en el documento. Se asume y se declara (`Anexo B`) |
| **5** | **Y se consigna el daño a terceros que no son parte** | Documentos de empleados despedidos y acuerdos con contrapartes exponen a quien no fue atacado. **Es un problema de notificación que nadie suele mirar** (`G-7`) |

**Las dos objeciones razonables, y la respuesta.**

- **«Sin el dato, el hallazgo no es verificable.»** Es cierto y es el coste declarado. La mitigación es la regla 4: la fuente está identificada y el patrón es comprobable por cualquiera en origen. **Un informe que ilustra un hallazgo con el domicilio de una persona compra verificabilidad con el daño de un tercero**, y ésa es una mala compra.
- **«El dato ya es público.»** Lo es en el sitio del extorsionador, con el alcance del sitio de un extorsionador. **Un informe de inteligencia tiene otro alcance y otra credibilidad**, y reproducirlo no es neutral: es amplificación. Es el mismo razonamiento de `CTI-2026-048` `E-4` sobre las reclamaciones nominales, aplicado a personas en lugar de a compañías.

**Dónde más se aplica.** En cualquier informe sobre extorsión por datos donde el material incluya personas identificables, que es un número creciente de casos: `CTI-2026-042` ya tomó esta decisión con los registros de pacientes de un hospital, y `CTI-2026-041` con los registros de empleados de una energética. **Este informe generaliza lo que allí fueron decisiones puntuales, y lo deja escrito como criterio.**

## Anexo E — Marcos de referencia empleados

- **ICD 203**, con la adición del `Anexo C`: **separar la confianza en que un patrón existe de la confianza en que sea deliberado**, porque la atribución de intención nunca hereda la confianza de la observación.
- **Código Admiralty/OTAN**, con el grado **medición propia** de `CTI-2026-044`, y con la particularidad declarada de que **la única fuente del hallazgo central es propia y el informe no puede citarla**.
- **MITRE ATT&CK: deliberadamente sin mapa.** Ninguna TTP registrada y una sola herramienta. Como en `CTI-2026-048`, una tabla de identificadores sin procedimiento daría apariencia de conocimiento.
- **Graduación de la prueba de una entrada de sitio de filtración**, `Anexo D` de `CTI-2026-048`: este actor opera en los niveles 2 y 5, frente al 0 y 3 de `n0n`, y la tabla de `E-3` es la aplicación directa.
- **Tratamiento de datos de personas en un catálogo de extorsión**, propio de este informe (`Anexo D`): cinco reglas, y la generalización de decisiones que `CTI-2026-041` y `042` tomaron puntualmente.

## Anexo F — Paquete legible por máquina

Las tablas `cti:ioc` alimentan `ioc_index.csv`. **Cinco advertencias:**

1. **⚠ PROHIBIDO ingerir cualquier dato personal del catálogo de este actor.** No hay ninguno en este informe y no debe añadirse. `Anexo D`.
2. **No hay indicadores de compromiso.** `PAP:WHITE`. Una sola herramienta registrada —Rclone— y es legítima: va como patrón con control por destino, no como valor de bloqueo.
3. **No se transcriben las direcciones de sus once sitios de filtración.** Ocho cayeron en cinco meses.
4. **Toda cifra de ventana corta lleva su base**: **0 por fecha de ataque, 10 por publicación**. Este actor es el caso en que la primera base da cero, el opuesto de `CTI-2026-047`.
5. **Y las cuatro filas de `A.3` son medición, no indicadores**: describen la anatomía de un catálogo y sirven para graduar la prueba, no para detectar una intrusión.

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-11-19 | Emisión inicial, cuarta de la serie `046`–`053`. Incluye: el **hallazgo propio y no corroborado de que la palanca de extorsión es la exposición personal del propietario** —identificación fiscal, domicilio, contacto personal, declaraciones fiscales—, con la alternativa de que sea subproducto de atacar pymes retenida como seria (`KJ-1`, `E-2`, `H-2`); la **medición de verificabilidad del catálogo**: 116 de 116 entradas con dominio frente a 22 de 259 de `n0n` (`KJ-2`, `E-3`); el **0 % de entradas con fecha de ataque igual a la de publicación**, único en el lote y señal de operación real frente a sitio sembrado (`KJ-3`); la **rotación de infraestructura más rápida del lote**: once sitios en cinco meses, tres en pie (`KJ-4`); el **modelo de presión regulatoria y relacional** que traslada la decisión de Seguridad a Legal (`KJ-5`, `E-4`); la **cuestión abierta del cifrado** (`KJ-6`); la exposición regional de **cinco víctimas, tres brasileñas, ninguna chilena** (`KJ-7`); y el **criterio de tratamiento de datos de personas en un catálogo de extorsión** del `Anexo D`, que generaliza decisiones puntuales de `CTI-2026-041` y `042` | Célula CTI |

> **Nota sobre esta emisión.** Es el informe de la serie con la combinación de
> fuentes más incómoda: **su hallazgo central tiene una sola fuente, es
> nuestra, y el informe se priva deliberadamente de citarla** para no
> reproducir datos de personas. Se publica así porque las dos alternativas son
> peores: **omitir el hallazgo**, que sería ocultar lo más importante que se
> sabe de este actor; o **ilustrarlo**, que sería dañar otra vez a quien ya fue
> dañado. **La regla queda escrita en el `Anexo D` para no volver a decidirlo
> caso por caso.**

## Anexo H — Realimentación del consumidor

1. **¿Contempla el plan de respuesta a extorsión que la palanca sea la exposición personal de una persona concreta?** Es la decisión 1 de `E-4` y **la pregunta central de este informe**. No es técnica y va dirigida a Legal y a Dirección. Si el plan supone que la víctima es la organización, **no contempla ni quién decide ni qué se le debe a esa persona**.
2. **Si somos una pyme: ¿sabe el propietario que es él el objetivo de la presión?** Es `E-4.3`, y es una conversación, no un control.
3. **¿Existe un inventario de qué datos personales de directivos y empleados hay en sistemas corporativos, y quién accede a ellos?** Es `H-3` y `E-4.5`. **Es lo que este actor busca y casi ninguna organización lo sabe.**
4. **¿Hay control de egreso por destino y por volumen?** Es `T-2` y la decisión 2 de `E-4`: la única defensa de un daño que **no se puede restaurar**.
5. **¿Se reprodujo material de su catálogo en algún informe o correo interno?** Es `Anexo D`. Si se citó un dato personal «como ejemplo», se dañó otra vez a esa persona con el alcance del canal interno.
6. **¿Se ha anticipado la vía de notificación a reguladores y a terceros afectados?** Es `KJ-5` y `E-4.4`: **el actor amenaza con hacerlo él, y hacerlo primero le quita la palanca**.
7. **¿Alguien ha visto este modelo de doxing documentado en otra fuente?** Es `G-1` y la petición más valiosa de este informe: **el hallazgo central no está corroborado**, y tanto una confirmación como una refutación valen más que el informe.
8. **¿Puede alguien comprobar si sus víctimas grandes también traen datos del propietario?** Es `G-3` y resolvería `H-2`, el riesgo 1 del pre-mortem. **Se puede hacer con los datos que ya tenemos, fijando antes el criterio de tamaño.**
9. **Y la pregunta de método:** el `Anexo D` sostiene que un informe de inteligencia no es un vehículo neutral y que reproducir un dato personal ya publicado por un extorsionador es amplificarlo. **¿Hay algún caso en que reproducir el dato habilitara una decisión que la descripción del patrón no habilitaba?** Si existe, la regla 1 necesita una excepción escrita.

*Fin del informe `CTI-2026-049` v1.0.*
