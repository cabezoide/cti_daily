---
tlp: "TLP:CLEAR"
pap: "PAP:WHITE"
id: "CTI-2026-052"
version: "1.0"
tipo: "Perfil de operación de extorsión"
foco_regional: "EE. UU. · sin exposición latinoamericana medida"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "Curious Worm · curiousworm"
fecha: "2026-11-19"
caduca: "2027-01-19"
autor: "Célula CTI"
distribucion: "Elaborado con fuentes abiertas y con medición propia sobre la interfaz pública de consulta de un rastreador de sitios de filtración. No se reproduce ningún nombre de víctima: sus reclamaciones no están confirmadas por ninguna de ellas y un proveedor sugiere que su catálogo podría estar sembrado con datos reciclados. Difusión libre, conservando la atribución y las salvedades de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-052

## Curious Worm invierte la secuencia de la extorsión: publica primero y extorsiona después, sin fase de presión previa

### Ocho días de vida, nueve de sus dieciocho entradas publicadas el primer día, y casi la mitad de su catálogo son hospitales estadounidenses

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-052` |
| Versión | 1.0 — 2026-11-19 |
| Clasificación | `TLP:CLEAR` · **`PAP:WHITE`** — sin indicadores accionables |
| Objeto | **`Curious Worm`**, octavo puesto del ranking de siete días que motiva esta serie. **Ocho días de existencia observada** |
| Foco regional | **Cero víctimas latinoamericanas de 18.** Su geografía es Estados Unidos |
| Lo que lo distingue en este lote | **No tiene fase de presión previa a la publicación**: un proveedor observa que **publica primero y extorsiona después**, lo que invierte la secuencia estándar de la extorsión por datos |
| Y su concentración sectorial | **8 de 18 entradas son de sanidad (44 %)**, con sistemas hospitalarios estadounidenses nombrados por terceros |
| Horizonte | Estratégico 3–6 meses |
| Origen de los datos | **Medición propia** sobre 18 registros, más cuatro fuentes externas |
| Caducidad | **2027-01-19 (60 días)** |
| Autor | Célula CTI |

<!-- cti:note type="warn" -->

> ⚠ **Cuatro advertencias, y es el expediente con la base más estrecha de la
> serie junto con `CTI-2026-053`.**
>
> 1. **Ocho días de existencia observada y dieciocho entradas.** No hay patrón:
>    hay una ventana.
> 2. **Ninguna de sus víctimas ha confirmado nada**, según la cobertura
>    localizada, y el rastreador marca al actor como emergente con advertencia
>    expresa de cautela.
> 3. **Un proveedor sugiere que podría estar sembrando su sitio con datos
>    reciclados o obtenidos previamente**, y no hay forma de descartarlo desde
>    fuera (`KJ-3`).
> 4. **Y por eso no se reproduce ningún nombre de víctima**, aunque terceros
>    los hayan publicado: son reclamaciones sin confirmar contra hospitales y
>    un despacho de abogados, y la regla de `CTI-2026-048` `E-4` se aplica.

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** **Invierte la secuencia estándar de la extorsión por datos: no hay fase de presión previa, publica primero y extorsiona después.** Es la observación de un proveedor, y nuestra medición es compatible: **nueve de sus dieciocho entradas se publicaron el día de su aparición**, y las dieciocho tienen la fecha de ataque igual a la de publicación —es decir, **ninguna declara un plazo transcurrido entre el acceso y la publicación**—. Valoramos **probable** *(55–80 %)* que la inversión sea real y no un artefacto de la juventud del sitio. **Confianza: moderada.** *Consecuencia, y es la que cambia la respuesta:* **la víctima no recibe un aviso previo con cuenta atrás; se entera por la publicación.** No hay ventana de negociación, y por tanto **tampoco hay ventana para decidir**: cuando la organización lo sabe, el daño reputacional ya empezó.

**KJ-2.** **Su concentración sectorial es la más alta del lote: casi la mitad de su catálogo es sanidad estadounidense, con sistemas hospitalarios entre las víctimas reclamadas.** De 18 registros, **8 son de sanidad (44 %)** y 7 están en Estados Unidos, con un registro cada uno en Alemania, Canadá, Irlanda y Reino Unido. Fuentes externas nombran, entre sus primeras reclamaciones, **dos sistemas hospitalarios estadounidenses y un despacho de abogados**, y señalan que **más de la mitad de los incidentes de su sitio implican entidades sanitarias estadounidenses**. Valoramos **probable** *(55–80 %)* que la orientación a la sanidad sea deliberada. **Confianza: moderada** — ocho días no establecen una política. *Consecuencia:* **no declara ninguna exclusión, y los hospitales están entre sus primeras elecciones.**

**KJ-3.** **Un proveedor sugiere que su catálogo podría estar sembrado con datos reciclados, y nuestra medición no lo descarta ni lo confirma.** Lo que sí medimos: **el 50 % del catálogo publicado el primer día** y **el 100 % de las entradas con fecha de ataque igual a la de publicación**, lo que significa que **el actor no aporta ni una fecha de acceso comprobable en ninguna de sus dieciocho entradas**. Valoramos **aproximadamente igual de probable** *(40–60 %)* que haya reciclaje significativo frente a que se trate de intrusiones propias publicadas de golpe. **Confianza: baja, y es el juicio que más importa resolver** (`G-2`). *La prueba discriminante existe y no la podemos hacer:* **comparar el material reclamado con brechas ya divulgadas por esas organizaciones** (`Anexo D`).

**KJ-4.** **No está establecido que cifre.** Un proveedor lo señala expresamente —el cifrado **no está confirmado**— y el rastreador no le registra ninguna herramienta ni ninguna TTP. Valoramos **probable** *(55–80 %)* que opere como extorsión por datos sin cifrado. **Confianza: moderada.** *Consecuencia, común a los cuatro actores sin cifrado de esta serie:* **la copia de seguridad no defiende de nada**, y lo que vale es el control de egreso y la identidad.

**KJ-5.** **Para esta región no hay exposición medida: cero víctimas latinoamericanas de 18.** Junto con `CTI-2026-050`, es uno de los dos únicos actores del lote sin ninguna. Valoramos **baja** la confianza en esto como propiedad estable, porque **ocho días y dieciocho entradas no permiten afirmar una ausencia**, y además **seis de las dieciocho no tienen país asignado**. *Consecuencia:* hoy es exclusivamente ruido del ranking para una organización de la región, **con la salvedad de que un tercio de su catálogo es de país desconocido**.

**KJ-6.** **Los recuentos públicos sobre él difieren casi al doble: 18, 10 y 9 según tres fuentes.** Nosotros medimos **18 entradas** en el rastreador; un proveedor contó **nueve en su lanzamiento** y otro **diez en total**. Valoramos **casi con certeza** *(≥99 %)* que las tres sean correctas para su momento, y la diferencia se explica por el crecimiento del catálogo entre el 11 y el 18 de noviembre. **Confianza: alta.** *Es un recordatorio de la regla de la serie:* **ninguna cifra sobre un actor de ocho días se cita sin su fecha.**

**KJ-7.** **Y hay una señal de interés externo que conviene registrar: un medio especializado en notificación de brechas publicó una pieza sobre él a los dos días de su aparición.** Valoramos **probable** *(55–80 %)* que eso indique que **alguien con acceso a las organizaciones afectadas está comprobando las reclamaciones**, porque es la práctica habitual de ese tipo de publicación. **Confianza: moderada.** *Consecuencia práctica:* **es la fuente que más probablemente resolverá `KJ-3`**, y vigilarla es más rentable que cualquier medida técnica contra este actor (`I-1`).

---

## 2. Resumen ejecutivo

`Curious Worm` abrió su sitio de filtración el 11 de noviembre de 2026 y ocho días después tiene dieciocho entradas y el octavo puesto del ranking que motiva esta serie.

Lo que lo distingue es **el orden en que hace las cosas**. La extorsión por datos tiene una secuencia estándar: se roba, se avisa a la víctima, se abre una cuenta atrás, y sólo si no hay pago se publica. Un proveedor observa que este actor **no tiene fase de presión previa: publica primero y extorsiona después**. Nuestra medición es compatible: **nueve de sus dieciocho entradas aparecieron el día en que abrió el sitio**, y **las dieciocho tienen la fecha de ataque igual a la de publicación**, es decir, no declara ni un día transcurrido entre el acceso y la exposición.

**Eso cambia la respuesta de forma concreta.** Contra una operación con cuenta atrás, la organización tiene días para investigar, decidir y preparar comunicación. Contra ésta, **la organización se entera por la publicación**, y cuando lo sabe el daño reputacional ya ha empezado. No hay ventana de negociación y —lo que importa más— **no hay ventana para decidir**.

Su elección de víctimas es la más concentrada del lote: **ocho de dieciocho entradas son de sanidad, el 44 %**, y fuentes externas nombran entre sus primeras reclamaciones dos sistemas hospitalarios estadounidenses y un despacho de abogados, señalando que más de la mitad de los incidentes de su sitio implican entidades sanitarias de ese país. **No declara ninguna exclusión**, y los hospitales están entre sus primeras elecciones.

Hay una duda central que este informe no puede cerrar y que conviene no disimular: **un proveedor sugiere que el catálogo podría estar sembrado con datos reciclados o obtenidos previamente**. Lo que medimos no lo descarta: la mitad del catálogo publicada el primer día y **ninguna de las dieciocho entradas aportando una fecha de acceso comprobable**. La prueba discriminante existe —comparar el material reclamado con brechas que esas organizaciones ya hayan divulgado— y **no la podemos hacer desde fuera**. El `Anexo D` la deja escrita como método.

Tampoco está establecido que cifre: un proveedor lo dice expresamente, y el rastreador no le registra ninguna herramienta.

Para esta región: **cero víctimas latinoamericanas de 18**, con la salvedad de que **seis de las dieciocho no tienen país asignado**. Y una observación que vale más que cualquier medida técnica: **un medio especializado en notificación de brechas publicó sobre este actor a los dos días de aparecer**, lo que suele significar que alguien está comprobando sus reclamaciones con las organizaciones afectadas. **Vigilar esa fuente es, hoy, la acción de mayor rendimiento frente a este actor.**

---

## 3. Alcance y limitaciones

### 3.1 Qué cubre

El objeto `Curious Worm` en sus ocho días de existencia observada: la secuencia invertida de publicación y extorsión, su concentración en la sanidad estadounidense, la duda sobre el reciclaje de su catálogo, su victimología, y el método para resolver esa duda.

### 3.2 Qué NO cubre

| Fuera de alcance | Por qué |
|---|---|
| **Una cadena de intrusión** | Ninguna TTP, herramienta ni muestra. Es `G-1` |
| **La veracidad de sus reclamaciones** | Ninguna víctima ha confirmado; un proveedor sugiere reciclaje |
| **Los nombres de las víctimas** | **No se reproducen**, aunque terceros los hayan publicado (`CTI-2026-048` `E-4`) |
| **El cifrado** | No confirmado por ninguna fuente (`KJ-4`) |
| **Indicadores** | No hay ninguno. `PAP:WHITE` |

### 3.3 Limitaciones de la colección

<!-- cti:note type="warn" -->

> ⚠ **Cinco limitaciones, y la primera es decisiva.**
>
> 1. **Ocho días y dieciocho entradas.** Es la base más estrecha de la serie
>    junto con `CTI-2026-053`. **Ninguna proporción de este informe es una
>    medida de un patrón.**
> 2. **Seis de las dieciocho entradas no tienen país**, es decir **un tercio**,
>    lo que debilita directamente `KJ-5`.
> 3. **Fuente única para la medición propia**, y sobre un catálogo que un
>    proveedor considera posiblemente reciclado.
> 4. **La observación de la secuencia invertida es de un proveedor**, no
>    nuestra: nosotros aportamos datos compatibles, no la observación.
> 5. **Y la duda central —`KJ-3`— no se puede resolver desde fuera**, porque
>    requiere comparar material reclamado con divulgaciones de las propias
>    organizaciones.

### 3.4 Qué aporta

| Aporte | Dónde |
|---|---|
| **La secuencia invertida corroborada con datos propios**: 50 % del catálogo el primer día, 100 % sin fecha de acceso declarada | `KJ-1`, `KJ-3` |
| **La concentración sectorial medida**: 44 % sanidad, la más alta del lote | `KJ-2` |
| **La consecuencia operativa de no tener fase de presión**: no hay ventana para decidir | `E-2` |
| **La señal de interés de un medio de notificación de brechas** como mejor vía de resolución | `KJ-7`, `I-1` |
| **Un método para comprobar si un catálogo está sembrado con datos reciclados** | `Anexo D` |

### 3.5 Veredicto

<!-- cti:table highlight="CORROBORADO|NO SOSTENIDO|SIN RESOLVER|propio" -->

| # | Elemento | Veredicto | Base |
|---|---|---|---|
| 1 | Es una operación de ransomware | **NO SOSTENIDO** | Cifrado **no confirmado**; ninguna herramienta registrada (`KJ-4`) |
| 2 | Sigue la secuencia estándar de extorsión | **NO SOSTENIDO — y es el hallazgo** | **Publica primero y extorsiona después** (`KJ-1`) |
| 3 | Sus reclamaciones son material propio | **SIN RESOLVER** | Un proveedor sugiere reciclaje; **ninguna entrada aporta fecha de acceso** (`KJ-3`) |
| 4 | Sus reclamaciones son verificables | **NO SOSTENIDO** | Ninguna víctima ha confirmado; cero referencias de prensa en los datos |
| 5 | Ataca sin preferencia sectorial | **NO SOSTENIDO** | **44 % sanidad**, con hospitales entre sus primeras reclamaciones (`KJ-2`) |
| 6 | Declara exclusiones éticas | **NO SOSTENIDO** | Ninguna conocida, y los hospitales están entre sus primeras elecciones |
| 7 | Es una amenaza medida para la región | **NO SOSTENIDO** | **Cero víctimas latinoamericanas**, con un tercio del catálogo sin país (`KJ-5`) |
| 8 | Los recuentos públicos son consistentes | **NO SOSTENIDO** | 18 · 10 · 9, según fuente y fecha (`KJ-6`) |

---

# NIVEL ESTRATÉGICO
### Para: CISO, Comunicación, Legal, Riesgo · Horizonte: 3–6 meses

## E-1. Qué clase de objeto es

<!-- cti:cards -->

| Rasgo | Qué significa | Etiqueta |
|---|---|---|
| **Publica antes de extorsionar** | **No hay ventana de negociación ni de decisión.** La víctima se entera por la publicación | `01 · secuencia invertida` |
| **50 % del catálogo el primer día** | El sitio nació cargado. Compatible con acumulación previa **y** con siembra | `02 · catálogo de golpe` |
| **Ninguna entrada declara fecha de acceso** | La víctima no tiene ventana que investigar | `03 · sin ventana` |
| **44 % sanidad, con hospitales** | Sin exclusiones declaradas. **Sector con daño a pacientes** | `04 · sanidad` |
| **Cifrado no confirmado** | La restauración no defiende | `05 · sin cifrado` |
| **Ocho días de vida** | Todo lo anterior es provisional | `06 · objeto nuevo` |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `18` | Entradas medidas | Desde el 2026-11-11 |
| `9` | Entradas publicadas el **primer día** | **El 50 % del catálogo** |
| `100 %` | Entradas con fecha de ataque igual a la de publicación | **Ninguna ventana temporal declarada.** Sólo `pixelleaks` comparte |
| `8 / 18` | Entradas de **sanidad** | **El 44 %: la concentración sectorial más alta del lote** |
| `7 / 18` | Entradas en Estados Unidos | |
| `6 / 18` | **Entradas sin país asignado** | **Un tercio.** Debilita `KJ-5` |
| `0` | **Víctimas latinoamericanas** | De 18 |
| `0` | Entradas con referencia de prensa en los datos | Ninguna recogida como confirmada |
| `18 · 10 · 9` | Recuentos de tres fuentes | Según fecha de consulta |

## E-2. La secuencia invertida, y por qué es la única cosa de este informe que cambia un plan

**La secuencia estándar de la extorsión por datos, con sus ventanas:**

| Fase | Qué ocurre | **Ventana para la víctima** |
|---|---|---|
| 1 · Exfiltración | El actor obtiene los datos | Ninguna, si no se detecta |
| 2 · Contacto | Nota, correo o portal | **Empieza la ventana** |
| 3 · Cuenta atrás | Plazo público o privado | **Días para investigar, decidir y preparar comunicación** |
| 4 · Publicación | Si no hay pago | Fin de la ventana |

**La secuencia de este actor, según la observación de un proveedor y los datos compatibles que medimos:**

| Fase | Qué ocurre | Ventana |
|---|---|---|
| 1 · Exfiltración | Igual | Ninguna |
| 2 · **Publicación** | **Entrada en el sitio de filtración** | **Ninguna: la organización se entera aquí** |
| 3 · Extorsión | Después de publicar | La negociación empieza con el daño ya hecho |

**Las tres consecuencias prácticas:**

1. **No hay tiempo para investigar antes de que el asunto sea público.** El plan habitual —detectar, acotar, decidir, comunicar— se ejecuta con la prensa ya enterada.
2. **La comunicación tiene que estar preparada antes, no durante.** Es la misma conclusión que `CTI-2026-051` `E-2` por otra vía: **dos de los seis actores nuevos de esta serie obligan a tener respuesta de comunicación lista de antemano.**
3. **Y el incentivo del pago se debilita.** Si el material ya está publicado, pagar no lo retira de donde ya estuvo. **Eso hace a este actor peor negociador y, paradójicamente, más dañino**: tiene menos que vender y menos que perder.

> **La salvedad honesta: la observación de la secuencia es de un proveedor, y
> ocho días de catálogo no la establecen.** Lo que nosotros aportamos es
> compatible —ninguna de las dieciocho entradas declara una fecha de acceso
> anterior— **pero hay una explicación alternativa trivial**: que el actor no
> rellene ese campo y el rastreador ponga la fecha de publicación por omisión.
> **En ese caso la secuencia podría ser la normal y nosotros no veríamos la
> diferencia.** Es `G-3`.

## E-3. La duda del reciclaje

**Lo que un proveedor sugiere:** que el sitio podría estar **sembrado con datos reciclados o obtenidos previamente**.

**Lo que medimos, y es compatible con las dos explicaciones:**

| Dato | Compatible con reciclaje | Compatible con operación propia |
|---|---|---|
| 50 % del catálogo el primer día | **Sí**: un fondo preparado | **Sí**: víctimas acumuladas antes de abrir escaparate |
| Ninguna fecha de acceso declarada | **Sí**: un dato reciclado no tiene fecha propia que dar | **Sí**: el actor puede no declararla por opsec |
| 44 % sanidad | **Sí**: la sanidad es el sector con más brechas divulgadas públicamente, y por tanto el más fácil de reciclar | **Sí**: es también un sector muy atacado |
| Cero confirmaciones de víctima | **Sí** | **Sí**: ocho días es poco |

**Ningún dato propio discrimina**, y conviene decirlo así en lugar de inclinarse. **La prueba que sí discriminaría está en el `Anexo D`** y requiere algo que esta célula no puede hacer: comparar el material reclamado con las brechas que esas organizaciones ya hayan divulgado.

> **Y la razón de que esta duda importe más que de costumbre: si el catálogo es
> reciclado, el actor no tiene capacidad de intrusión y la respuesta correcta
> es de comunicación y nada más.** Si es propio, hay un actor con acceso a
> hospitales que nadie ha caracterizado. **Las dos hipótesis piden cosas
> distintas**, y por eso `G-2` es prioridad 1.

## E-4. Decisiones que este informe pide

| # | Decisión | A quién | Coste | Por qué |
|---|---|---|---|---|
| **1** | **Si somos prestador de salud en EE. UU.: comprobar si aparecemos listados, hoy** | CISO | **Bajo** | `KJ-2`: 44 % de su catálogo, con sistemas hospitalarios entre sus primeras reclamaciones |
| **2** | **Tener preparada la respuesta de comunicación ANTES de aparecer** | **Comunicación · Legal** | Medio | `E-2`: **no hay fase de presión previa.** Cuando se sabe, ya es público |
| **3** | **Si aparecemos: comprobar primero si el material coincide con una brecha ya divulgada por nosotros** | CISO · Legal | **Bajo** | **`Anexo D`.** Si es material antiguo, la respuesta es notificación y no negociación |
| **4** | **Control de egreso por destino y volumen** | Red | Medio | Medida común a los cuatro actores sin cifrado de la serie |
| **5** | **Vigilar el medio especializado en notificación de brechas que ya publicó sobre él** | CTI | **Muy bajo** | `KJ-7`: **es la vía más probable de resolución**, y más rentable que cualquier medida técnica contra este actor |
| **6** | **No priorizarlo por su octavo puesto** | CTI | Cero | Ocho días, 18 entradas, mitad publicada el primer día |

---

# NIVEL OPERACIONAL
### Para: SOC, CTI, Comunicación · Horizonte: semanas

## O-1. Identificación

| Campo | Valor |
|---|---|
| Nombre | **`Curious Worm`** · identificador en el rastreador **`curiousworm`** |
| Alias | Ninguno conocido |
| En el rastreador desde | **2026-11-11** |
| Sitios de filtración | **Uno, activo**, con el nombre del grupo como título |
| TTP registradas | **Ninguna** |
| Herramientas registradas | **Ninguna** |
| Cifrado | **No confirmado** por ninguna fuente |
| Secuencia | **Publica antes de extorsionar**, según proveedor (`KJ-1`) |
| Aviso gubernamental | Ninguno |

> **Y una nota de desambiguación que conviene dejar escrita: el identificador
> del grupo en el rastreador es `curiousworm` sin espacio, mientras sus
> registros de víctima van bajo `Curious Worm` con espacio.** Al consultar su
> histórico por identificador de grupo, la consulta devuelve vacío; los datos
> están bajo la otra forma. **Es un detalle trivial que puede llevar a concluir
> que el actor no tiene víctimas**, y lo mencionamos porque nos pasó.

## O-2. La anatomía de su catálogo

| Campo | Presente en | Lectura |
|---|---|---|
| País | 12 de 18 | **Seis sin país: un tercio** |
| Sector | 15 de 18 | Tres marcados «Not Found» |
| **Fecha de ataque distinta de la publicación** | **0 de 18** | `KJ-1`, `KJ-3` |
| Tamaño de datos | 0 de 18 | |
| Cifra de rescate | 0 de 18 | |
| Referencia de prensa en los datos | **0 de 18** | Ninguna confirmada como tal |

**Sectores** *(sobre los 15 con sector)*: **Sanidad 8**, Tecnología 4, otros 3. **Geografía** *(sobre los 12 con país)*: Estados Unidos 7, y uno cada uno en Alemania, Canadá, Irlanda y Reino Unido.

**Lo que fuentes externas añaden sobre sus víctimas**, sin que las nombremos: dos **sistemas hospitalarios estadounidenses** —uno en un distrito urbano del noreste, otro en el oeste de Texas—, un **despacho de abogados**, una compañía de **servicios de salud ocupacional**, una **farmacéutica** y un operador de **residencias para mayores**. Fuentes externas señalan que **más de la mitad de los incidentes de su sitio implican entidades sanitarias estadounidenses**.

## O-3. La actividad medida

| Ventana | Por **fecha de ataque** | Por **publicación** | Nota |
|---|---|---|---|
| Total | 18 | 18 | Ocho días |
| Últimos 7 días | **9** | **9** | **Idénticas**, por el 100 % de `KJ-1` |
| Ranking del sitio *(16:20 UTC del 19-11)* | — | — | **9** |
| Pico en un día | — | **9 el 2026-11-11** | **El 50 % del catálogo el día de apertura** |

## O-4. Nuestra exposición

| Si la organización… | Exposición | Medida |
|---|---|---|
| **Es prestador de salud en EE. UU.** | **La más alta.** 44 % de su catálogo | `E-4.1` **hoy** |
| **Es un despacho de abogados o servicios profesionales** | Media | Igual |
| **Es latinoamericana** | **Ninguna medida**, con un tercio del catálogo sin país como salvedad | Vigilancia pasiva |
| **Tiene plan de comunicación reactivo y no preparado** | **Alta en términos de daño** | `E-4.2`: **con este actor no hay aviso previo** |

## O-5. Hipótesis alternativas y pre-mortem

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| **H-1 — Publica antes de extorsionar** | **Retenida como principal**, con la observación de un proveedor y datos propios compatibles | `Probable · 55–80 %` |
| **H-2 — El actor no rellena la fecha de acceso y el rastreador la pone por omisión** | **Retenida como alternativa trivial.** En ese caso la secuencia podría ser la normal y no lo veríamos (`G-3`) | `Posibilidad real · 40–60 %` |
| **H-3 — El catálogo está sembrado con datos reciclados** | **Retenida al mismo nivel que su contraria, y es la duda central.** Ningún dato propio discrimina (`E-3`) | `Aprox. igual de probable · 40–60 %` |
| **H-4 — La orientación a la sanidad es deliberada** | **Retenida.** 44 % en ocho días, con hospitales entre las primeras elecciones | `Probable · 55–80 %` |
| **H-5 — La sanidad predomina porque es el sector con más brechas divulgadas y por tanto el más fácil de reciclar** | **Retenida, y es la versión interesante de `H-3`.** Si el catálogo es reciclado, el sesgo sectorial **no dice nada del actor**: dice qué material había disponible | `Posibilidad real · 40–60 %` |
| **H-6 — Es una marca nueva de un actor conocido** | **Sin evidencia.** Ninguna fuente lo sugiere | `Aprox. igual de probable · 40–60 %` |

**Pre-mortem — si este informe se equivoca, será porque:**

1. **`H-3` es cierta** y el actor no tiene capacidad de intrusión: el expediente habría caracterizado un escaparate. **Es el riesgo 1.**
2. **`H-2` es cierta** y la secuencia invertida era un artefacto del rastreador.
3. **`H-5` es cierta** y el 44 % de sanidad describía la disponibilidad de material reciclado y no una preferencia del actor.
4. **Un prestador de salud no comprobó si estaba listado** porque el actor parecía menor en el ranking.
5. **Alguien negoció con él sin comprobar primero si el material era de una brecha ya divulgada** (`E-4.3`).
6. **Se tomó la ausencia de víctimas latinoamericanas como garantía** con un tercio del catálogo sin país.

---

# NIVEL TÁCTICO Y TÉCNICO

<!-- cti:note type="warn" -->

> ⚠ **Sin TTP, sin herramientas, sin muestras y sin indicadores.** No se incluye
> mapa ATT&CK. Es el cuarto informe consecutivo de esta serie en esta
> situación, y la acumulación es en sí misma un dato sobre la calidad de la
> evidencia que sostiene un ranking de ventana corta.
>
> **La única comprobación específica que este actor permite es la del `Anexo
> D`, y la hace la víctima.**

## T-1. Las comprobaciones posibles

| # | Comprobación | Cómo | Qué establece |
|---|---|---|---|
| **H-1** | **¿Aparecemos listados?** | Búsqueda en el rastreador. **Atención a la forma del identificador** (`O-1`) | Con este actor, un positivo significa que **ya es público** |
| **H-2** | **¿El material reclamado coincide con una brecha que ya divulgamos?** | Comparación con el historial propio de incidentes | **La comprobación decisiva** (`Anexo D`). Si coincide, la respuesta es notificación y no negociación |
| **H-3** | **¿Hay egreso anómalo a destinos no corporativos en los últimos 90 días?** | Registros de flujo | Vale contra los cuatro actores sin cifrado de la serie |
| **H-4** | **¿Está preparada la respuesta de comunicación?** | Revisión con Comunicación y Legal | **Es la medida, no la comprobación**, y con este actor no hay tiempo de improvisarla |

---

## 14. Brechas de inteligencia y requisitos de colección

| # | Brecha | Impacto | Cómo se cierra | Prioridad |
|---|---|---|---|---|
| **G-1** | **Ninguna TTP, herramienta, muestra ni indicador** | Sin detección específica. `PAP:WHITE` | Informe de respuesta a incidentes de una víctima | **1** |
| **G-2** | **No sabemos si el catálogo está sembrado con datos reciclados** | **Es la duda central**: determina si hay o no un actor con acceso a hospitales | **`Anexo D`**: que una víctima compare el material con sus brechas divulgadas. **O el medio especializado de `KJ-7`** | **1** |
| **G-3** | **No sabemos si la ausencia de fecha de acceso es del actor o del rastreador** | Afecta a `KJ-1`, el hallazgo del informe | Comparar una entrada con el sitio original | **1** |
| **G-4** | **Un tercio de las entradas sin país** | Debilita `KJ-5` | Segunda fuente de rastreo | 2 |
| **G-5** | **Ocho días de observación** | Nada es un patrón | Tiempo | 2 |
| **G-6** | **No se ha confirmado el cifrado ni su ausencia** | `KJ-4` | Muestra o informe de incidente | 2 |

**Disparadores de reevaluación.** `I-1`: **publicación del medio especializado de `KJ-7` con confirmación o refutación de una víctima** —la vía más probable de resolver `G-2`—. `I-2`: aparición de una entrada con fecha de ataque anterior a la publicación, que refutaría `KJ-1`. `I-3`: que una víctima identifique el material como procedente de una brecha anterior ya divulgada, lo que confirmaría `H-3`. `I-4`: aparición de muestras o de cifrador. `I-5`: primera víctima latinoamericana. `I-6`: que el catálogo deje de crecer, señal de fondo agotado.

---

# ANEXOS

## Anexo A — Indicadores

### A.1 — ⚠ Sin indicadores de compromiso

<!-- cti:note type="warn" -->

> ⚠ **No hay ninguno.** `PAP:WHITE`. Y **no se reproduce ningún nombre de
> víctima**, aunque terceros los hayan publicado: son reclamaciones sin
> confirmar contra hospitales y un despacho de abogados, sobre un catálogo que
> un proveedor considera posiblemente reciclado.

### A.2 — Patrones de reconocimiento

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| pattern | **Catálogo sin fase de presión previa: entradas publicadas sin aviso ni cuenta atrás anterior** | **El rasgo distintivo del actor** (`KJ-1`). Para el defensor significa que **no hay ventana de decisión** | Moderada *(observación de proveedor + datos propios compatibles)* | Mientras mantenga el patrón | **Reconocimiento.** Obliga a tener comunicación preparada (`E-4.2`) |
| pattern | **Catálogo con el 50 % de entradas publicadas el día de apertura y ninguna fecha de acceso declarada** | Compatible con acumulación previa **y** con siembra. **No discrimina** (`E-3`) | Alta como medición | Histórico | **Graduación de la prueba**, no detección |
| pattern | **Concentración de sanidad superior al 40 % en un catálogo nuevo** | `KJ-2`. **Y conviene recordar `H-5`**: si el catálogo es reciclado, el sesgo describe el material disponible y no la preferencia del actor | Alta como medición | 60 días | Priorización sectorial |
| pattern | **Egreso anómalo a destinos no corporativos** | **El único patrón de detección aplicable**, y es genérico: vale contra los cuatro actores sin cifrado de esta serie | Media | Sin caducidad | Alerta |

### A.3 — Victimología y decisiones de higiene

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| cartera | **18 entradas · 9 el primer día · 0 con fecha de acceso declarada · 6 sin país · 0 con prensa** | La anatomía de `O-2` | Alta como recuento | 60 días | Medición |
| cartera | **8 de 18 entradas de sanidad (44 %)**, con sistemas hospitalarios entre las víctimas reclamadas por terceros | **La concentración sectorial más alta del lote** (`KJ-2`) | Moderada | 60 días | Priorización |
| cartera | **Cero víctimas latinoamericanas de 18** | `KJ-5`, **con un tercio del catálogo sin país**: la ausencia es débil | **Baja** | 60 días | **No usar como garantía** |
| cartera | **Recuentos de tres fuentes: 18 · 10 · 9** | `KJ-6`, por fecha de consulta | Alta | — | Citar siempre con fecha |
| cartera | **No se reproduce ningún nombre de víctima** | Regla de la serie, y aquí refuerza: hospitales con reclamaciones sin confirmar | — | — | No ingerir |

## Anexo B — Fuentes y valoración

| Fuente | Disciplina | Fiab. | Cred. | Grado | Notas |
|---|---|---|---|---|---|
| **`B-1` — Medición propia** sobre 18 registros | OSINT técnico · **medición propia** | **B** | **2** | **Medición propia** | Base de `KJ-2`, `KJ-3`, `KJ-5` y `KJ-6`. **Su límite es el tamaño**: dieciocho registros en ocho días no sostienen ninguna proporción como patrón |
| **`B-2` — Análisis de CyberXtron** | OSINT comercial | **C** | **3** | Proveedor | **La fuente del hallazgo de `KJ-1`**: ausencia de fase de presión previa, publicación antes de la extorsión. **Y de la sugerencia de reciclaje** que es la duda central (`KJ-3`). También: cifrado **no confirmado** |
| **`B-3` — Cobertura de inteligencia de red oscura y fichas de terceros** (Dark Web Intelligence, SOCRadar, Offset7, HookPhish) | OSINT · observación y compilación | **C** | **3** | Compilación | Fuente de la fecha de apertura, de la composición sectorial —**más de la mitad sanidad estadounidense**— y de los nombres de víctimas, **que no reproducimos**. Recuentos alternativos de 9 y 10 |
| **`B-4` — Medio especializado en notificación de brechas** (databreaches.net, pieza del 2026-11-13) | OSINT · periodismo especializado | **B** | **3** | Periodístico especializado | **Su valor no está en lo que publicó sino en lo que indica**: ese tipo de medio **contrasta con las organizaciones afectadas**. Es la vía más probable de resolver `G-2`, y vigilarla es la acción de mayor rendimiento del informe (`KJ-7`, `I-1`) |

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

> **La regla que este informe necesita: cuando un dato es compatible con dos
> hipótesis opuestas, hay que decirlo y no elegir.**
>
> El 50 % del catálogo publicado el primer día es **igual de compatible** con
> «acumuló víctimas antes de abrir escaparate» que con «sembró el sitio con
> material reciclado». La tabla de `E-3` lo expone así, fila por fila, y
> **ninguna de las cuatro filas discrimina**.
>
> **La tentación es elegir la hipótesis más interesante y presentar el dato
> como si la apoyara.** Este informe no lo hace, y el coste es que su juicio
> central —`KJ-3`— queda al 40–60 % con confianza baja. **Un informe con un
> juicio honestamente indeciso es más útil que uno con un juicio inventado**,
> porque dice exactamente qué hay que averiguar.

## Anexo D — Cómo comprobar si un catálogo está sembrado con datos reciclados

**El problema.** Un sitio de filtración nuevo publica un lote de víctimas de golpe. Las dos explicaciones —acumulación previa real y siembra con material ajeno o antiguo— **tienen consecuencias opuestas**: en la primera hay un actor con capacidad de intrusión al que hay que caracterizar; en la segunda hay un escaparate y la respuesta es de comunicación. **Y desde fuera no se distinguen.**

**La prueba discriminante, y sólo la puede hacer la víctima:**

> **¿El material reclamado coincide con una brecha que esta organización ya
> sufrió y divulgó?**

**El procedimiento, en cinco pasos:**

| # | Paso | Cómo | Qué establece |
|---|---|---|---|
| **1** | **Comparar con el propio historial de incidentes** | Registro interno de brechas e incidentes de los últimos tres años | **El paso decisivo.** Si el material es de una brecha ya conocida, el actor está revendiendo |
| **2** | **Comparar con las divulgaciones públicas propias** | Comunicados, notificaciones a reguladores | Si el actor pudo construir la reclamación con lo divulgado, **no prueba acceso** |
| **3** | **Comparar con brechas conocidas de proveedores** | Inventario de terceros y sus incidentes | **El origen más frecuente del material reciclado**: una brecha de un proveedor se presenta como brecha del cliente |
| **4** | **Comprobar la fecha más reciente del material** | Fechas internas de los documentos o registros reclamados | **Si el dato más nuevo es antiguo, el acceso es antiguo** — y acota si hay o no una intrusión activa |
| **5** | **Y si no hay material publicado, pedirlo** | Por el canal que el actor ofrezca | Un actor que recicla **suele no poder entregar material nuevo a demanda** |

**Las tres advertencias.**

1. **El paso 3 es el que más veces acierta y el que menos se hace.** Una proporción grande de las reclamaciones contra organizaciones grandes corresponde a **brechas de sus proveedores**, presentadas con el nombre del cliente porque vale más. `CTI-2026-014` documentó exactamente ese patrón con una compañía de primer nivel y dos de sus proveedores.
2. **«Reciclado» no significa «inofensivo».** Material antiguo republicado produce daño reputacional y obligaciones de notificación reales. **Lo que cambia es la respuesta: notificación y comunicación, no negociación ni respuesta a incidente activo.**
3. **Y el resultado puede ser mixto.** Un catálogo puede mezclar intrusiones propias con material reciclado, que es precisamente lo que `CTI-2026-050` midió en otro actor. **La pregunta correcta no es «¿es falso?» sino «¿qué parte es nueva?».**

**Para quien no es víctima.** Un analista externo **no puede ejecutar ninguno de los cinco pasos**, y conviene reconocerlo: todos requieren información que sólo la organización afectada tiene. **Lo que un analista externo sí puede hacer es vigilar a quien sí puede** — los medios especializados en notificación de brechas, que contrastan con las organizaciones. Es `KJ-7` y es la razón de que `E-4.5` sea una medida de vigilancia y no de análisis.

## Anexo E — Marcos de referencia empleados

- **ICD 203**, con la regla del `Anexo C`: **cuando un dato es compatible con dos hipótesis opuestas, se dice y no se elige**, aunque el coste sea un juicio central indeciso.
- **Código Admiralty/OTAN**, con el grado **medición propia**, y con la valoración de `B-4` por **lo que indica y no por lo que publicó**.
- **MITRE ATT&CK: sin mapa.** Cuarto informe consecutivo de la serie en esa situación, y la acumulación es un dato sobre la evidencia que sostiene un ranking de ventana corta.
- **Graduación de la prueba de una entrada de sitio de filtración**, `Anexo D` de `CTI-2026-048`: este actor opera en los niveles 0 y 1, sin captura, sin magnitud y sin confirmación.
- **Comprobación de reciclaje de un catálogo**, propio de este informe (`Anexo D`): cinco pasos, el tercero como el más rentable, y el reconocimiento de que **sólo la víctima puede ejecutarlos**.

## Anexo F — Paquete legible por máquina

Las tablas `cti:ioc` alimentan `ioc_index.csv`. **Cuatro advertencias:**

1. **No hay indicadores de compromiso.** `PAP:WHITE`. El único patrón de detección —egreso anómalo— es genérico y vale para toda la serie.
2. **No se reproduce ningún nombre de víctima**, aunque terceros los hayan publicado.
3. **La ausencia de víctimas latinoamericanas se consigna con confianza BAJA**, porque un tercio del catálogo no tiene país. **No se debe extraer como garantía.**
4. **Y ninguna proporción de este informe es un patrón**: ocho días y dieciocho entradas. Toda cifra lleva su fecha.

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-11-19 | Emisión inicial, séptima de la serie `046`–`053`. Incluye: la **secuencia invertida de publicación y extorsión** —observación de proveedor corroborada con datos propios compatibles— y su consecuencia de que **no hay ventana de decisión para la víctima** (`KJ-1`, `E-2`); la **concentración sectorial más alta del lote**: 44 % sanidad con sistemas hospitalarios entre las reclamaciones (`KJ-2`); la **duda del reciclaje del catálogo expuesta sin resolver**, con la tabla de `E-3` mostrando que **ninguno de los cuatro datos propios discrimina** (`KJ-3`, `H-3`); la constatación de que **el cifrado no está confirmado** (`KJ-4`); la **ausencia regional consignada con confianza baja** por tener un tercio del catálogo sin país (`KJ-5`); la **señal de interés de un medio especializado en notificación de brechas** como vía más probable de resolución y acción de mayor rendimiento (`KJ-7`); la nota de desambiguación del identificador del grupo (`O-1`); y el método del `Anexo D` para comprobar si un catálogo está sembrado con datos reciclados | Célula CTI |

> **Nota sobre esta emisión.** Es, junto con `CTI-2026-053`, el informe de la
> serie con la base más estrecha, y su juicio central queda **honestamente
> indeciso al 40–60 %**. Se emite así porque la alternativa —elegir la
> hipótesis más interesante y presentar los datos como si la apoyaran— sería
> peor que un informe que dice exactamente qué hay que averiguar y quién puede
> averiguarlo.

## Anexo H — Realimentación del consumidor

1. **Si somos prestador de salud en Estados Unidos: ¿se comprobó hoy si aparecemos listados?** Es la decisión 1 de `E-4`. **El 44 % de su catálogo es sanidad y hay sistemas hospitalarios entre sus primeras reclamaciones.**
2. **¿Está preparada la respuesta de comunicación, antes de necesitarla?** Es `E-4.2` y la consecuencia directa de `KJ-1`: **con este actor no hay aviso previo ni cuenta atrás.** Cuando la organización lo sabe, ya es público.
3. **Si aparecemos: ¿se comparó el material con nuestras propias brechas divulgadas y con las de nuestros proveedores?** Es `Anexo D`, pasos 1 a 3, **y el paso 3 es el que más veces acierta y el que menos se hace.**
4. **¿Se negoció con él sin hacer antes esa comparación?** Si el material es de una brecha ya divulgada, **la respuesta correcta era notificación y no negociación**.
5. **¿Alguien vigila el medio especializado que ya publicó sobre él?** Es `E-4.5` y `KJ-7`: **cuesta casi nada y es la vía más probable de resolver la duda central del informe.**
6. **¿Se tomó la ausencia de víctimas latinoamericanas como garantía?** Un tercio del catálogo no tiene país. La confianza de ese juicio es **baja** y está declarada así.
7. **¿Alguien puede comparar una entrada del rastreador con el sitio original?** Es `G-3`: resolvería si la ausencia de fecha de acceso es del actor o de la herramienta, y de ello depende `KJ-1`.
8. **Y la pregunta de método:** el `Anexo D` sostiene que **sólo la víctima puede comprobar si un catálogo está reciclado**, y que un analista externo únicamente puede vigilar a quien sí puede. **¿Hay alguna comprobación de reciclaje que un externo pueda hacer y que no hayamos considerado?** Si existe, este informe se queda corto en su parte más importante.

*Fin del informe `CTI-2026-052` v1.0.*
