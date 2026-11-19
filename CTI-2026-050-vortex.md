---
tlp: "TLP:CLEAR"
pap: "PAP:WHITE"
id: "CTI-2026-050"
version: "1.0"
tipo: "Perfil de operación de extorsión"
foco_regional: "EE. UU. · sin exposición latinoamericana medida"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "Vortex"
fecha: "2026-11-19"
caduca: "2027-01-19"
autor: "Célula CTI"
distribucion: "Elaborado con fuentes abiertas y con medición propia sobre la interfaz pública de consulta de un rastreador de sitios de filtración. No se reproduce ningún nombre de víctima: las reclamaciones de este actor no están confirmadas por ninguna de ellas y un tercero advierte de que su catálogo incluye reclamaciones no verificadas o fabricadas. Difusión libre, conservando la atribución y las salvedades de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-050

## Vortex no cifra nada: reclama capturas completas de inquilinos de Microsoft 365, y su catálogo lista la misma víctima dos veces

### Hallazgo propio: 35 entradas, 26 descripciones distintas, cuatro víctimas duplicadas bajo dos nombres y seis descripciones reutilizadas entre víctimas diferentes

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-050` |
| Versión | 1.0 — 2026-11-19 |
| Clasificación | `TLP:CLEAR` · **`PAP:WHITE`** — sin indicadores accionables |
| Objeto | **`Vortex`**, quinto puesto del ranking de siete días que motiva esta serie. **Nueve días de existencia observada** |
| Foco regional | **Cero víctimas latinoamericanas de 35.** Su geografía es Estados Unidos (29 de 35) |
| Lo que lo distingue en este lote | **Es el único que no menciona el cifrado en ninguna de sus 35 entradas**, y el único que reclama **capturas de inquilinos de Microsoft 365** con cifras precisas de ficheros, gigabytes y cuentas de directorio |
| Y el hallazgo propio | **Su catálogo se duplica y se reutiliza**: 35 entradas para 26 descripciones distintas, con al menos **cuatro víctimas listadas dos veces bajo dos nombres** |
| Horizonte | Estratégico 3–6 meses |
| Origen de los datos | **Medición propia** sobre 35 registros, más cuatro fuentes externas |
| Caducidad | **2027-01-19 (60 días)** |
| Autor | Célula CTI |

<!-- cti:note type="warn" -->

> ⚠ **Cuatro advertencias, y las cuatro apuntan en la misma dirección.**
>
> 1. **Este actor tiene nueve días de existencia observada.** Apareció en el
>    rastreador el 10 de noviembre de 2026. Todo lo que aquí se dice describe
>    una ventana de nueve días.
> 2. **Ninguna de sus víctimas ha confirmado relación con él**, según la
>    cobertura localizada, y **un tercero advierte expresamente de que su
>    catálogo incluye reclamaciones no verificadas o fabricadas**.
> 3. **Nuestra propia medición apoya esa advertencia**: encontramos víctimas
>    listadas dos veces bajo dos nombres y descripciones idénticas repetidas
>    entre víctimas distintas (`KJ-2`).
> 4. **Por eso no se reproduce ningún nombre de víctima.** Son reclamaciones
>    sin confirmar contra organizaciones nombradas, y la regla de `CTI-2026-048`
>    `E-4` se aplica aquí con más razón: repetirlas en un informe de
>    inteligencia les presta un crédito que no tienen.

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** **No es una operación de ransomware: en sus 35 entradas no hay una sola mención al cifrado.** Lo que reclama es **tenencia de datos** —sus descripciones empiezan literalmente por «Type: data held»— y en la parte más detallada de su catálogo, **capturas completas de inquilinos de Microsoft 365**, con cifras de ficheros, gigabytes, cuentas de directorio, grupos y asignaciones de rol. Valoramos **casi con certeza** *(≥99 %)* que el cifrado no forma parte de su propuesta, porque medimos su ausencia en los 35 registros, y una fuente externa lo confirma al señalar que una de sus entradas **no afirma que los sistemas de la víctima fueran cifrados**. **Confianza: alta.** *Consecuencia:* **la copia de seguridad no defiende de nada aquí**, y la defensa es de identidad y de egreso, no de puesto (`E-3`).

**KJ-2.** **Y el hallazgo propio es que su catálogo se duplica y se recicla, lo que corrobora de forma independiente la advertencia de un tercero.** De **35 entradas sólo hay 26 descripciones distintas**. Cinco descripciones están compartidas por más de una entrada, y el detalle importa: **al menos cuatro víctimas aparecen listadas dos veces bajo dos nombres distintos** —una vez con su nombre comercial y otra en mayúsculas, o una vez con la cifra de datos en el título y otra sin ella—, y **dos grupos de tres víctimas diferentes comparten una descripción idéntica**, es decir, una plantilla. Valoramos **casi con certeza** *(≥99 %)* las proporciones medidas, y **muy probable** *(80–95 %)* que **el número real de organizaciones distintas de su catálogo sea del orden de 31 y no de 35**. **Confianza: alta.** *Y la corroboración externa es exacta:* un tercero advierte de que las entradas atribuidas a este actor **se han reportado como incluyendo reclamaciones no verificadas o fabricadas**.

**KJ-3.** **La reclamación de Microsoft 365 no cubre todo su catálogo, y la proporción importa: sólo 9 de 35 entradas la mencionan y sólo 8 traen cifras de captura.** El resto se expresa en **recuentos de registros** —millones de registros por víctima— o sin magnitud alguna. Valoramos **casi con certeza** *(≥99 %)* las proporciones. **Confianza: alta.** *Y es una corrección a la primera impresión que conviene dejar escrita:* **las tres primeras entradas que examinamos eran todas de Microsoft 365, y de ahí se seguía la conclusión de que todo su catálogo lo era. No lo es: es una cuarta parte.** Es el mismo error de muestreo que `CTI-2026-044` `O-2.2` documentó, a escala menor.

**KJ-4.** **Lo que sí ofrece —y lo distingue de los demás actores nuevos del lote— son magnitudes precisas, y eso lo sitúa alto en la escala de prueba y bajo en verificabilidad a la vez.** Ocho entradas declaran cifras del tipo «captura completa: 656.824 ficheros, 1.094,12 GB» junto a «directorio: 20.233 cuentas de usuario, 8.001 grupos con listas completas de pertenencia y asignaciones de rol de aplicación». Pero **sólo 7 de 35 entradas traen dominio**, y **las 35 traen captura de pantalla**. Valoramos **muy probable** *(80–95 %)* que este perfil —magnitudes muy detalladas, identificación escasa— sea **deliberado**: la precisión numérica produce credibilidad sin permitir comprobación. **Confianza: moderada.** *En la escala de `CTI-2026-048` `Anexo D`, opera en los niveles 4 y 5 sin pasar por el 2.*

**KJ-5.** **Su foco es la sanidad estadounidense, y es el más concentrado del lote.** De 35 registros, **16 son de sanidad (46 %)** y **29 están en Estados Unidos (83 %)**, con dos en Alemania y uno en Irlanda. Valoramos **moderada** la confianza, porque nueve días no establecen un patrón. *Consecuencia:* es un actor **sectorial y nacional**, al menos por ahora.

**KJ-6.** **Y para esta región no hay exposición medida: cero víctimas latinoamericanas de 35.** Junto con `curious worm`, es uno de los dos únicos actores del lote sin ninguna. Valoramos **moderada** la confianza, con la salvedad obvia de que **nueve días y 35 entradas no permiten afirmar una ausencia estructural**. *Consecuencia:* hoy, para una organización de la región, este actor es exclusivamente ruido del ranking.

**KJ-7.** **Si sus reclamaciones de Microsoft 365 fueran ciertas, el vector sería la identidad y no el puesto, y eso cambia por completo la defensa.** Una captura de directorio con cuentas, grupos y asignaciones de rol de aplicación **no se obtiene desde un portátil cifrado: se obtiene con credenciales válidas y permisos de lectura en el inquilino**. Valoramos **probable** *(55–80 %)* que, en los casos reales que haya, la vía sea **cuenta comprometida o consentimiento de aplicación**, y no intrusión de puesto. **Confianza: moderada** — es inferencia nuestra a partir de lo que esas cifras implican técnicamente, no una observación. *Consecuencia, y es la recomendación central:* **la defensa es acceso condicional, segundo factor resistente a suplantación y revisión de aplicaciones con consentimiento, no EDR** (`X-2`).

**KJ-8.** **Hay una coincidencia con un incidente real divulgado por una de las organizaciones listadas, y no se puede establecer ninguna relación.** Una de ellas había divulgado por su cuenta, el mes anterior, **una intrusión en una cuenta de Microsoft 365 ocurrida entre finales de agosto y principios de septiembre de 2026**. Valoramos **aproximadamente igual de probable** *(40–60 %)* que la entrada del catálogo se refiera a ese incidente frente a que sea una reclamación oportunista construida sobre una divulgación pública. **Confianza: baja, y es importante no resolverla:** **un extorsionador que lea divulgaciones públicas puede reclamar incidentes que no causó**, y eso es indistinguible desde fuera. Es `G-3`.

---

## 2. Resumen ejecutivo

`Vortex` apareció el 10 de noviembre de 2026 y nueve días después ocupa el quinto puesto del ranking que motiva esta serie, con 35 entradas. Dos cosas lo separan del resto del lote.

La primera: **no cifra nada.** En sus 35 entradas no hay una sola mención al cifrado. Lo que reclama es tenencia de datos —sus descripciones empiezan por «Type: data held»— y en su parte más detallada, **capturas completas de inquilinos de Microsoft 365** con cifras muy concretas: tantos ficheros, tantos gigabytes, tantas cuentas de directorio, tantos grupos con sus listas de pertenencia y sus asignaciones de rol de aplicación. Una fuente externa confirma el punto al señalar que una de sus entradas **no afirma que los sistemas de la víctima hayan sido cifrados**.

La segunda, y es nuestra: **su catálogo se duplica y se recicla.** De 35 entradas sólo hay **26 descripciones distintas**. Al menos **cuatro víctimas aparecen listadas dos veces bajo dos nombres** —una con el nombre comercial y otra en mayúsculas, o una con la cifra de datos en el título y otra sin ella—, y **dos grupos de tres víctimas diferentes comparten una descripción idéntica**, lo que sólo puede ser una plantilla. El número real de organizaciones distintas es del orden de **31, no de 35**. Esa medición corrobora, por un camino independiente, la advertencia de un tercero: **las entradas atribuidas a este actor se han reportado como incluyendo reclamaciones no verificadas o fabricadas**, y **ninguna de las organizaciones listadas ha confirmado relación con él**.

Conviene además una corrección de nuestra propia primera lectura, porque es instructiva. Las tres primeras entradas que examinamos eran todas de Microsoft 365, y de ahí concluimos que ése era su modelo entero. **No lo es: sólo 9 de 35 lo mencionan y sólo 8 traen cifras de captura.** El resto se expresa en recuentos de registros o sin magnitud. Es el mismo error de muestreo que esta serie ya documentó a mayor escala, y se deja escrito.

Lo que sí es cierto —y es lo único accionable del informe— es que **si alguna de esas capturas de inquilino es real, el vector no es el puesto de trabajo: es la identidad.** Una lista de 20.000 cuentas con sus grupos y sus asignaciones de rol de aplicación no se saca de un portátil: se saca con credenciales válidas y permisos de lectura en el inquilino. Por tanto **la defensa es acceso condicional, segundo factor resistente a suplantación y revisión de aplicaciones con consentimiento**, y no una herramienta de puesto. Para una organización que use Microsoft 365 —es decir, casi cualquiera— ésa es una revisión que paga con independencia de que este actor exista o no.

Para esta región: **cero víctimas latinoamericanas de 35.** Su foco es la sanidad estadounidense: 16 de 35 entradas de sanidad y 29 de 35 en Estados Unidos.

---

## 3. Alcance y limitaciones

### 3.1 Qué cubre

El objeto `Vortex` en sus nueve días de existencia observada: la estructura de su catálogo y sus duplicaciones, la naturaleza de sus reclamaciones, la proporción real de reclamaciones de Microsoft 365, su victimología, y la inferencia defensiva que se sigue de lo que esas reclamaciones implicarían si fueran ciertas.

### 3.2 Qué NO cubre

| Fuera de alcance | Por qué |
|---|---|
| **Una cadena de intrusión** | **No hay material.** Ninguna TTP registrada, ninguna herramienta, ninguna muestra. Es `G-1` |
| **La veracidad de las reclamaciones** | **No se puede establecer.** Ninguna víctima ha confirmado; un tercero advierte de posibles fabricaciones; nuestra medición encuentra duplicados |
| **Los nombres de las víctimas** | **No se reproducen**, y aquí con más razón que en el resto de la serie (`E-4` de `CTI-2026-048`) |
| **La relación con el incidente divulgado por una de ellas** | `KJ-8`, indistinguible desde fuera. Es `G-3` |
| **Indicadores** | No hay ninguno. `PAP:WHITE` |

### 3.3 Limitaciones de la colección

<!-- cti:note type="warn" -->

> ⚠ **Seis limitaciones, y la primera lo condiciona todo.**
>
> 1. **Nueve días de existencia observada y 35 entradas.** Ninguna proporción
>    de este informe es una medida de un patrón: son descripciones de una
>    ventana muy corta.
> 2. **Fuente única para la medición propia**, y un tercero cuestiona la
>    fiabilidad del material que esa fuente indexa.
> 3. **Nuestra primera lectura fue errónea** por muestrear las tres primeras
>    entradas (`KJ-3`), y se deja escrito.
> 4. **Dos de las 35 entradas no tienen país** y sólo 7 tienen dominio.
> 5. **La inferencia sobre el vector de identidad es nuestra** (`KJ-7`): se
>    deduce de lo que las cifras declaradas implicarían técnicamente, **no de
>    ninguna observación**.
> 6. **Y no hay ninguna fuente de proveedor con análisis técnico**: sólo
>    cobertura de listados y advertencias de verificación.

### 3.4 Qué aporta

| Aporte | Dónde |
|---|---|
| **La ausencia de cifrado medida** en las 35 entradas | `KJ-1` |
| **La duplicación y el reciclaje del catálogo** — hallazgo propio que corrobora una advertencia de tercero | `KJ-2`, `O-2` |
| **La proporción real de reclamaciones de Microsoft 365**: 9 de 35, no todas | `KJ-3` |
| **El perfil de prueba invertido**: magnitudes precisas con identificación escasa | `KJ-4` |
| **La inferencia del vector de identidad** y la medida que se sigue | `KJ-7`, `X-2` |
| **Un método para evaluar una reclamación de captura de inquilino en la nube** | `Anexo D` |

### 3.5 Veredicto

<!-- cti:table highlight="CORROBORADO|NO SOSTENIDO|SIN RESOLVER|propio" -->

| # | Elemento | Veredicto | Base |
|---|---|---|---|
| 1 | `Vortex` es un grupo de ransomware | **NO SOSTENIDO** | **Cero menciones al cifrado en 35 entradas** (`KJ-1`) |
| 2 | Tiene 35 víctimas | **NO SOSTENIDO** | **26 descripciones distintas; al menos 4 víctimas duplicadas.** Del orden de 31 (`KJ-2`) |
| 3 | Su modelo son las capturas de Microsoft 365 | **PARCIALMENTE — y nuestra primera lectura se equivocó** | **9 de 35 entradas**, no todas (`KJ-3`) |
| 4 | Sus reclamaciones son verificables | **NO SOSTENIDO** | 7 de 35 con dominio; ninguna víctima lo ha confirmado (`KJ-4`) |
| 5 | Es una amenaza para la región | **NO SOSTENIDO** | **Cero víctimas latinoamericanas** (`KJ-6`) |
| 6 | La defensa es la copia de seguridad | **NO SOSTENIDO** | Sin cifrado, **la restauración no devuelve nada** (`E-3`) |
| 7 | El vector sería el puesto de trabajo | **NO SOSTENIDO — inferencia propia** | Una captura de directorio implica **identidad con permisos**, no puesto (`KJ-7`) |
| 8 | La entrada que coincide con un incidente divulgado se refiere a él | **SIN RESOLVER** | Indistinguible desde fuera (`KJ-8`, `G-3`) |

---

# NIVEL ESTRATÉGICO
### Para: CISO, Identidad, Riesgo · Horizonte: 3–6 meses

## E-1. Qué clase de objeto es

<!-- cti:cards -->

| Rasgo | Qué significa | Etiqueta |
|---|---|---|
| **Cero menciones al cifrado en 35 entradas** | No es ransomware. **La restauración no defiende de nada** | `01 · sin cifrado` |
| **Catálogo con duplicados y plantillas** | 26 descripciones para 35 entradas. **El recuento sobreestima** | `02 · catálogo reciclado` |
| **Magnitudes muy precisas, identificación escasa** | 8 entradas con cifras al segundo decimal; 7 de 35 con dominio. **Credibilidad sin comprobabilidad** | `03 · prueba invertida` |
| **Si fuera cierto, el vector es identidad** | Acceso condicional y revisión de consentimientos, no EDR | `04 · identidad` |
| **Sanidad estadounidense** | 16 de 35 de sanidad, 29 de 35 en EE. UU. | `05 · foco estrecho` |
| **Nueve días de vida** | Nada de lo anterior es un patrón establecido | `06 · objeto nuevo` |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `35` | Entradas en su sitio | Desde el 2026-11-10 |
| `26` | **Descripciones distintas** | **Nueve entradas comparten descripción con otra** |
| `≥4` | **Víctimas listadas dos veces bajo dos nombres** | El recuento real es del orden de 31 |
| `0` | Entradas que mencionan cifrado | **De 35** |
| `9` | Entradas que mencionan Microsoft 365 | **El 26 %, no el 100 %** (`KJ-3`) |
| `8` | Entradas con cifras de captura | Hasta 656.824 ficheros y 1.094,12 GB |
| `7 / 35` | Entradas con dominio identificable | El 20 % |
| `35 / 35` | Entradas con captura de pantalla | El 100 % |
| `16 / 35` | Entradas de sanidad | **El 46 %** |
| `29 / 35` | Entradas en Estados Unidos | El 83 % |
| `0` | **Víctimas latinoamericanas** | De 35 |
| `0` | Entradas con referencia de prensa | Ninguna recogida por un tercero |

## E-2. La duplicación del catálogo, medida

**Lo que encontramos al agrupar las 35 entradas por descripción idéntica:**

| Patrón | Entradas implicadas | Lectura |
|---|---|---|
| **Misma víctima, dos entradas** | Al menos **cuatro pares**: una entrada con el nombre comercial y otra con el nombre en mayúsculas, o una con la cifra de datos en el título y otra sin ella | **Duplicación.** El recuento se infla sin añadir víctimas |
| **Tres víctimas distintas, una descripción idéntica** | **Dos grupos de tres** | **Plantilla.** La descripción no describe a esa víctima: describe a la clase |
| Descripción única | 26 | Lo que queda |

> **Por qué esto es más grave que un error de maquetación.** Un catálogo que
> lista la misma víctima dos veces y que reutiliza descripciones entre
> víctimas distintas **no está describiendo lo que tiene: está rellenando un
> escaparate.** Y coincide con lo que un tercero advierte por su cuenta: que
> las entradas atribuidas a este actor **se han reportado como incluyendo
> reclamaciones no verificadas o fabricadas.**
>
> **Lo que no se puede concluir** es que todo sea falso. Una de las
> organizaciones listadas había divulgado por su cuenta una intrusión real en
> Microsoft 365 el mes anterior (`KJ-8`). **Hay material real en alguna parte
> de este catálogo, y no se puede saber en cuál.**

## E-3. Por qué la defensa correcta no es la habitual

**Si la propuesta de un extorsionador es tenencia de datos sin cifrado, las medidas se reordenan:**

| Medida | Contra ransomware clásico | **Contra este modelo** |
|---|---|---|
| Copias inmutables y verificadas | **Esencial** | **No sirve de nada.** Los datos ya salieron; restaurar no los recupera de nadie |
| EDR en el puesto | Esencial | **Marginal.** El puesto puede no estar implicado |
| **Acceso condicional y segundo factor resistente a suplantación** | Importante | **Esencial** |
| **Revisión de aplicaciones con consentimiento en el inquilino** | Secundario | **Esencial** |
| **Registro de auditoría del inquilino y de acceso a buzones** | Útil | **Esencial: es la única forma de comprobar si la reclamación es cierta** |
| Control de egreso | Importante | **Importante, pero el egreso ocurre en la nube y no en nuestro perímetro** |

> **Y de ahí la consecuencia menos cómoda de este informe: contra un actor
> cuyo material sale del inquilino en la nube, el perímetro de red de la
> organización no ve nada.** El tráfico de exfiltración va de la
> infraestructura del proveedor a la del adversario, y nunca pasa por nuestro
> cortafuegos. **La única visibilidad es el registro de auditoría del propio
> inquilino**, y la pregunta de `H-1` es si ese registro existe, se retiene y
> alguien lo mira.

## E-4. Decisiones que este informe pide

| # | Decisión | A quién | Coste | Por qué |
|---|---|---|---|---|
| **1** | **Verificar que el registro de auditoría del inquilino de Microsoft 365 está activo, se retiene al menos 90 días y es consultable** | **Identidad · TI** | **Bajo** | **La medida principal, y vale con independencia de que este actor exista.** Es la única forma de comprobar una reclamación de captura de inquilino (`H-1`) |
| **2** | **Revisar las aplicaciones con consentimiento y los permisos de lectura amplia sobre directorio y correo** | Identidad | Medio | `KJ-7`: una captura de directorio requiere exactamente eso |
| **3** | **Segundo factor resistente a suplantación en todas las cuentas, incluidas las de servicio y las de administración** | Identidad | Medio | Vía más probable de una captura de inquilino |
| **4** | **Acceso condicional por dispositivo y por ubicación para operaciones de lectura masiva** | Identidad | Medio | Limita lo que una credencial robada puede extraer |
| **5** | **No priorizar este actor por su puesto en el ranking** | CTI | Cero | Nueve días, 35 entradas, duplicados y ninguna confirmación |
| **6** | **Si aparecemos listados: comprobar en el registro de auditoría, no deducir** | CISO | Bajo | `KJ-2` y `KJ-8`: hay duplicados **y** hay material real. **Ninguna deducción sirve** |
| **7** | **No repetir sus reclamaciones nominales** | CTI · Comunicación | Cero | Ninguna víctima ha confirmado; un tercero advierte de fabricaciones |

---

# NIVEL OPERACIONAL
### Para: SOC, Identidad, CTI · Horizonte: semanas

## O-1. Identificación

| Campo | Valor |
|---|---|
| Nombre | **`Vortex`** |
| Alias | Ninguno conocido. **Atención: «Vortex» es un nombre reutilizado en el ecosistema del malware**, y este informe se refiere exclusivamente al sitio de filtración observado desde el 2026-11-10 |
| En el rastreador desde | **2026-11-10** |
| Sitios de filtración | **Uno, activo** |
| TTP registradas | **Ninguna** |
| Herramientas registradas | **Ninguna** |
| Cifrado | **Ninguna mención en 35 entradas** |
| Modelo declarado | **«Type: data held»** — tenencia de datos |
| Aviso gubernamental | Ninguno |

## O-2. La anatomía de su catálogo

| Campo | Presente en | Lectura |
|---|---|---|
| **Captura de pantalla** | **35 de 35 (100 %)** | La única prueba constante |
| **Dominio** | **7 de 35 (20 %)** | **Poca comprobabilidad** |
| País | 33 de 35 | Dos sin país |
| **Mención de Microsoft 365** | **9 de 35 (26 %)** | **No es su modelo único** (`KJ-3`) |
| **Cifras de captura** (ficheros y GB) | **8 de 35** | Hasta 656.824 ficheros / 1.094,12 GB |
| Recuento de registros en el título | Varias | Formato alternativo: «N registros», con cifras de millones |
| **Mención de cifrado** | **0 de 35** | `KJ-1` |
| Tamaño de datos en el campo estructurado | 0 de 35 | Las magnitudes van en la descripción, no en el campo |
| Cifra de rescate | 0 de 35 | |
| Referencia de prensa | **0 de 35** | **Ninguna víctima recogida por un tercero** |
| **Descripciones distintas** | **26 de 35** | **La duplicación de `KJ-2`** |

**La forma de sus descripciones de inquilino**, descrita sin nombrar a nadie: una cabecera `Type: data held`; una línea de captura con el número exacto de ficheros y los gigabytes con dos decimales; y después un desglose por servicio —directorio con número de cuentas de usuario, número de grupos «con listas completas de pertenencia y asignaciones de rol de aplicación», y secciones de almacenamiento documental—.

> **La precisión de esas cifras es su principal instrumento de credibilidad, y
> conviene entender por qué funciona y por qué no prueba nada.** «1.094,12 GB»
> suena a inventario real porque tiene dos decimales. Pero **un número preciso
> es tan fácil de inventar como uno redondo**, y el actor no ofrece ninguna
> forma de comprobarlo: no hay muestra, no hay árbol de ficheros descargable y
> en el 80 % de los casos no hay ni dominio. **Es prueba de nivel 4 en la
> escala de `CTI-2026-048` sin haber pasado por el nivel 2.**

## O-3. La actividad medida

| Ventana | Por **fecha de ataque** | Por **publicación** | Nota |
|---|---|---|---|
| Total | 35 | 35 | **Nueve días** |
| Últimos 7 días | **19** | **21** | Divergencia mínima (×1,1) |
| Ranking del sitio *(16:20 UTC del 19-11)* | — | — | **21** |
| Pico en un día | — | **14 el 2026-11-10** | **El 40 % del catálogo el día de su aparición** |

**El 63 % de sus entradas tiene la fecha de ataque igual a la de publicación.**

> **El pico del primer día es el dato de contexto que más importa: 14 de sus 35
> entradas se publicaron el día en que apareció.** Un sitio que nace con el
> 40 % de su catálogo ya cargado **no estaba construyendo ese catálogo en
> público: lo trajo hecho.** Eso es compatible con una operación que acumuló
> víctimas antes de abrir escaparate, y también con un sitio sembrado. **Las
> dos cosas se distinguirían con una sola muestra verificable, y no hay
> ninguna.**

## O-4. Nuestra exposición

| Si la organización… | Exposición | Medida |
|---|---|---|
| **Es latinoamericana** | **Ninguna medida.** Cero víctimas de 35 | Vigilancia pasiva |
| **Es prestador de salud en Estados Unidos** | **La más alta.** 16 de 35 entradas de sanidad, 29 en EE. UU. | `E-4` completo |
| **Usa Microsoft 365** *(es decir, casi cualquiera)* | **Alta en términos de la medida recomendada, baja en términos de este actor** | `E-4.1` a `E-4.4`: **la revisión paga aunque este actor sea ficticio** |
| **Aparece listada** | **Requiere comprobación en el registro de auditoría del inquilino** | `H-1`. **Ni deducir que es cierto ni que es falso** |

## O-5. Hipótesis alternativas y pre-mortem

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| **H-1 — El catálogo mezcla reclamaciones reales con relleno** | **Retenida como principal.** Hay duplicados y plantillas, **y** hay al menos una organización con un incidente real divulgado por ella misma | `Probable · 55–80 %` |
| **H-2 — Todo el catálogo es fabricado** | **Retenida.** Un tercero advierte de fabricaciones y ninguna víctima ha confirmado. **Pero la coincidencia de `KJ-8` la debilita** | `Posibilidad real · 40–60 %` |
| **H-3 — Los duplicados son un error de ingesta del rastreador y no del actor** | **Retenida como alternativa seria y no comprobada.** Si el rastreador indexó dos veces la misma entrada del sitio, el duplicado es nuestro y no suyo. **No lo verificamos contra el sitio original** y es `G-2` | `Posibilidad real · 40–60 %` |
| **H-4 — El vector es la identidad en la nube** | **Retenida como inferencia propia**, deducida de lo que las cifras implicarían | `Probable · 55–80 %` |
| **H-5 — Reclama incidentes divulgados por otros** | **Retenida y no descartable.** Un extorsionador que lea divulgaciones públicas puede reclamar lo que no causó (`KJ-8`) | `Posibilidad real · 40–60 %` |
| **H-6 — Es una marca nueva de un actor conocido** | **Sin evidencia.** Ninguna fuente lo sugiere. Se consigna porque es el patrón que la cartera ha visto cuatro veces | `Aprox. igual de probable · 40–60 %` |

**Pre-mortem — si este informe se equivoca, será porque:**

1. **Los duplicados eran del rastreador y no del catálogo** (`H-3`). **Es el riesgo 1** y se cierra verificando contra el sitio original, que no hicimos.
2. **Se leyó «catálogo con duplicados» como «actor falso»**, cuando hay indicios de material real.
3. **Alguien asumió que las capturas de inquilino son ciertas** y notificó a reguladores sobre la base de una reclamación sin verificar.
4. **Alguien asumió que son falsas** y no revisó su registro de auditoría.
5. **Se generalizó la reclamación de Microsoft 365 al catálogo entero**, que es el error que nosotros cometimos primero (`KJ-3`).
6. **Se priorizó el actor por su quinto puesto** en un ranking de nueve días.

---

# NIVEL TÁCTICO Y TÉCNICO
### Para: Identidad, SOC · Horizonte: días

<!-- cti:note type="warn" -->

> ⚠ **Sin TTP registradas, sin herramientas, sin muestras y sin indicadores.**
> Como en `CTI-2026-048` y `049`, no se incluye mapa ATT&CK: sería una lista de
> identificadores sin procedimiento observado.
>
> **Lo que sigue es la comprobación que una organización listada puede hacer, y
> es la aportación práctica del informe.**

## T-1. Cómo comprobar una reclamación de captura de inquilino

Si una organización aparece listada con una reclamación del tipo «captura completa: N ficheros, X GB, directorio con M cuentas», **esto es lo que se puede comprobar y en qué orden**:

| # | Comprobación | Dónde | Qué establece |
|---|---|---|---|
| **1** | **¿Coinciden las magnitudes declaradas con la realidad del inquilino?** Número de cuentas de usuario, número de grupos | Consola de administración | **La comprobación más rápida y la más discriminante.** Si declara 20.233 cuentas y el inquilino tiene 400, la reclamación es falsa. **Si coincide, no prueba la intrusión —el número de empleados suele ser público— pero sube mucho el prior** |
| **2** | **¿Hay operaciones de enumeración masiva de directorio en el registro de auditoría?** | Registro de auditoría del inquilino | **La evidencia directa.** Una captura de directorio deja rastro de consultas masivas |
| **3** | **¿Hay accesos de aplicación con permisos de lectura amplia que nadie reconoce?** | Aplicaciones empresariales y consentimientos | La vía más silenciosa: un consentimiento concedido una vez |
| **4** | **¿Hay descargas masivas desde almacenamiento documental o buzones?** | Registro de actividad de ficheros y de buzón | Explica el volumen en gigabytes |
| **5** | **¿Hay inicios de sesión correctos desde ubicaciones o dispositivos anómalos en la ventana declarada?** | Registro de inicios de sesión | Acota la ventana y la cuenta |
| **6** | **¿Existe y se retiene ese registro?** | — | **Si la respuesta es no, ninguna de las cinco anteriores se puede responder**, y ésa es la conclusión del informe en esa organización |

> **El paso 6 es el que importa de verdad y el que conviene resolver antes de
> necesitarlo.** La retención por omisión del registro de auditoría de un
> inquilino es limitada, y una reclamación puede referirse a una ventana
> anterior a ella. **Una organización que amplíe la retención hoy está
> comprando la capacidad de responder a una reclamación de mañana**, y el coste
> es de configuración y de licencia, no de proyecto.

## T-2. Mitigaciones

| # | Medida | Dónde | Efecto | Coste |
|---|---|---|---|---|
| **X-2.1** | **Registro de auditoría del inquilino activo, con retención ≥90 días y consultable** | Identidad | **Habilita toda la comprobación de `T-1`.** Sin esto no hay respuesta posible | **Bajo** |
| **X-2.2** | **Revisión de aplicaciones con consentimiento y de permisos de lectura amplia sobre directorio y correo** | Identidad | Cierra la vía más silenciosa | Medio |
| **X-2.3** | **Segundo factor resistente a suplantación en todas las cuentas, de servicio y de administración incluidas** | Identidad | Cierra la vía de credencial robada | Medio |
| **X-2.4** | **Acceso condicional por dispositivo y ubicación para lecturas masivas** | Identidad | Limita el alcance de una credencial comprometida | Medio |
| **X-2.5** | **Alerta sobre enumeración masiva de directorio** | SOC | Detecta la captura mientras ocurre | Bajo |
| **X-2.6** | **Alerta sobre descarga masiva desde almacenamiento documental** | SOC | Detecta el volumen | Bajo |

> **Y la observación de encuadre: ninguna de las seis medidas es específica de
> este actor.** Todas son higiene de identidad en la nube, y todas pagan con
> independencia de que `Vortex` exista, sea real o desaparezca el mes que
> viene. **Ése es el único uso defendible de un informe sobre un objeto de
> nueve días: encontrar la medida que vale aunque el objeto no valga.**

---

## 14. Brechas de inteligencia y requisitos de colección

| # | Brecha | Impacto | Cómo se cierra | Prioridad |
|---|---|---|---|---|
| **G-1** | **Ninguna TTP, herramienta, muestra ni indicador** | No hay detección específica posible. `PAP:WHITE` | Informe de respuesta a incidentes de una víctima real | **1** |
| **G-2** | **No verificamos los duplicados contra el sitio original del actor** | Es `H-3`, el riesgo 1 del pre-mortem: **los duplicados podrían ser del rastreador y no del catálogo** | **Comparar las entradas del rastreador con el sitio del adversario.** Requiere acceso a la red oscura, que esta célula no tiene | **1** |
| **G-3** | **No se puede distinguir si reclama incidentes divulgados por otros** | `KJ-8`, `H-5`. Determinaría si hay capacidad o sólo lectura de noticias | Que una víctima listada confirme o niegue públicamente | **1** |
| **G-4** | **Nueve días de observación** | Ninguna proporción es un patrón | Tiempo | 2 |
| **G-5** | **No sabemos si las magnitudes declaradas coinciden con la realidad de los inquilinos** | Es la comprobación 1 de `T-1` y **no la podemos hacer desde fuera** | **Una víctima que lo compruebe y lo publique.** Es la petición más valiosa del informe | **1** |
| **G-6** | **Cero referencias de prensa en 35 entradas** | Ninguna víctima recogida por un tercero | — Es un dato, no sólo una brecha | — |

**Disparadores de reevaluación.** `I-1`: **que una víctima confirme o niegue públicamente**, lo que resolvería `G-3` y `G-5` de golpe. `I-2`: publicación de una muestra verificable. `I-3`: aparición de la primera víctima latinoamericana. `I-4`: que empiece a mencionar cifrado, lo que cambiaría su clase. `I-5`: que el catálogo deje de crecer, señal de sitio sembrado agotado. `I-6`: aparición de un análisis de proveedor con detalle técnico.

---

# ANEXOS

## Anexo A — Indicadores

### A.1 — ⚠ Sin indicadores de compromiso

<!-- cti:note type="warn" -->

> ⚠ **No hay ninguno**: ni direcciones, ni dominios, ni hashes, ni ficheros, ni
> herramientas. De ahí el **`PAP:WHITE`**. Y no se reproduce **ningún nombre de
> víctima**: son reclamaciones sin confirmar, con duplicados medidos y con una
> advertencia de tercero sobre posibles fabricaciones.

### A.2 — Patrones de reconocimiento y de detección

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| pattern | **Enumeración masiva de directorio en el registro de auditoría del inquilino** | **El indicador accionable de este informe** (`X-2.5`). Una captura de directorio con cuentas, grupos y asignaciones de rol deja exactamente este rastro | **Media-alta como inferencia propia** | Sin caducidad | **Alerta.** Vale con independencia de este actor |
| pattern | **Descarga masiva desde almacenamiento documental o buzones en una ventana corta** | Explica el volumen declarado en gigabytes | Media-alta | Sin caducidad | Alerta (`X-2.6`) |
| pattern | **Aplicación con consentimiento y permisos de lectura amplia sobre directorio o correo que nadie reconoce** | La vía más silenciosa de una captura de inquilino | Media | Sin caducidad | **Revisión periódica** (`X-2.2`) |
| pattern | **Entrada de sitio de filtración con cabecera `Type: data held` y cifras de captura de inquilino con decimales** | **Reconocimiento de este actor**, no de compromiso. La precisión decimal es su instrumento de credibilidad y **no prueba nada** | Alta | Mientras mantenga el formato | Reconocimiento |
| pattern | **Catálogo con descripciones repetidas entre víctimas distintas y víctimas listadas dos veces bajo dos nombres** | **El patrón de `KJ-2`**, y se generaliza: **es una señal de relleno de escaparate** aplicable a cualquier sitio de filtración | **Alta como medición** | Sin caducidad como método | **Graduación de la prueba** (`Anexo D`) |

### A.3 — Victimología y decisiones de higiene

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| cartera | **35 entradas · 26 descripciones distintas · ≥4 víctimas duplicadas · 7 con dominio · 35 con captura · 0 con prensa · 0 con mención de cifrado** | La anatomía de `O-2`. **El recuento sobreestima el número de organizaciones** | Alta como recuento | 60 días | Medición |
| cartera | **9 de 35 entradas mencionan Microsoft 365; 8 traen cifras de captura** | `KJ-3`, **y la corrección de nuestra propia primera lectura** | Alta | 60 días | — |
| cartera | **Cero víctimas latinoamericanas de 35.** 29 en EE. UU., 16 de sanidad | `KJ-6`, con nueve días de observación como salvedad | Moderada | 60 días | Priorización |
| cartera | **14 de sus 35 entradas se publicaron el día de su aparición** | `O-3`: **nació con el 40 % del catálogo cargado** | Alta | Histórico | Análisis |
| cartera | **No se reproduce ningún nombre de víctima** | Ninguna ha confirmado; hay duplicados medidos; un tercero advierte de fabricaciones. **Regla de `CTI-2026-048` `E-4`** | — | — | No ingerir |

## Anexo B — Fuentes y valoración

| Fuente | Disciplina | Fiab. | Cred. | Grado | Notas |
|---|---|---|---|---|---|
| **`B-1` — Medición propia** sobre 35 registros: agrupación por descripción idéntica, campos presentes, perfil diario | OSINT técnico · **medición propia** | **B** | **2** | **Medición propia** | **Fuente del hallazgo de `KJ-2`.** Su virtud: la duplicación se detecta agrupando, y es reproducible. **Su límite, declarado: no verificamos los duplicados contra el sitio del adversario**, de modo que podrían ser del rastreador (`H-3`, `G-2`) |
| **`B-2` — Cobertura de inteligencia de red oscura** (Dark Web Intelligence) | OSINT · observación de sitios | **C** | **3** | Compilación | Fuente de la aparición del sitio con un lote de víctimas de sanidad y tecnología médica estadounidenses, **y de que ninguna víctima ha confirmado relación** |
| **`B-3` — Fichas de víctima de terceros** (RedPacket Security, ransomware.live) | OSINT · compilación | **C** | **4** | Compilación | **La fuente de la advertencia más importante**: las entradas atribuidas a este actor **se han reportado como incluyendo reclamaciones no verificadas o fabricadas**; y la observación de que una de ellas **no afirma cifrado**. También las cifras de dos entradas concretas, que coinciden con nuestra medición |
| **`B-4` — Divulgación propia de una organización listada** | OSINT · comunicación de la afectada | **B** | **2** | **Declaración de la víctima** | Una de las organizaciones listadas había divulgado por su cuenta una intrusión en una cuenta de Microsoft 365 en una ventana anterior. **Es la única evidencia de que puede haber material real**, y **no se puede vincular** (`KJ-8`, `G-3`) |

> **Lo notable de esta estructura de fuentes es que la fuente más fiable
> —`B-4`, una divulgación de la propia afectada— es la que menos se puede
> usar.** Confirma que hubo una intrusión real en un inquilino de Microsoft
> 365 de una organización que este actor lista, y **no permite concluir que
> sea la misma**. Un extorsionador que lea divulgaciones públicas puede
> reclamar lo que no causó, y eso es indistinguible desde fuera. **La fuente
> buena sirve para plantear la duda, no para resolverla.**

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

> **La advertencia que este informe añade: la precisión de una cifra no es
> evidencia de su veracidad, y conviene decirlo porque el efecto psicológico
> es fuerte.**
>
> «1.094,12 GB» y «unos mil gigabytes» son igual de verificables desde fuera:
> **ninguna de las dos lo es.** La primera produce más confianza porque los
> decimales sugieren un inventario real. **Pero inventar un número con
> decimales cuesta exactamente lo mismo que inventar uno redondo**, y este
> actor no ofrece ninguna forma de comprobarlo.
>
> **La regla:** la confianza en una magnitud declarada por un adversario
> depende de **si existe un camino para comprobarla**, no de cuántas cifras
> significativas tenga. Aquí ese camino existe —`T-1`— **y está del lado de la
> víctima, no del nuestro**.

## Anexo D — Cómo evaluar una reclamación de captura de inquilino en la nube

**El problema, y es creciente.** La extorsión por datos se está desplazando del puesto al inquilino. Una reclamación del tipo «tenemos la captura completa de su Microsoft 365: N ficheros, X GB, M cuentas de directorio» tiene tres propiedades que la hacen difícil de tratar: **es muy concreta**, **no deja rastro en el perímetro de la organización**, y **se puede construir en parte con información pública**.

**Las tres piezas de una reclamación así, con su verificabilidad:**

| Pieza | Ejemplo | ¿Se puede inventar? | ¿Se puede comprobar? |
|---|---|---|---|
| **Número de cuentas de directorio** | «20.233 cuentas de usuario» | **Sí, con facilidad**: el tamaño de la plantilla es información pública o estimable | **Sí, y es la comprobación más rápida.** La organización sabe cuántas cuentas tiene |
| **Número de grupos y asignaciones de rol** | «8.001 grupos con listas de pertenencia» | **Difícil**: no es información pública y guarda una relación no trivial con el tamaño | **Sí**, y es **la pieza más discriminante** |
| **Ficheros y volumen** | «656.824 ficheros, 1.094,12 GB» | **Sí**: plausible para cualquier organización mediana | **Aproximadamente**, comparando con el consumo real del inquilino |

**El procedimiento, en cuatro pasos y por orden de coste:**

1. **Comparar el número de cuentas con la realidad.** Minutos. **Un desajuste grande refuta la reclamación**; una coincidencia no la confirma, porque el dato es estimable.
2. **Comparar el número de grupos.** Minutos, y **es el paso decisivo**: la relación entre número de empleados y número de grupos de un inquilino es idiosincrásica y no se deduce de fuera. **Una coincidencia aquí es un indicio fuerte de que alguien leyó el directorio.**
3. **Buscar enumeración masiva de directorio en el registro de auditoría** de la ventana declarada. Horas, **si el registro existe y se retiene**.
4. **Buscar descargas masivas y accesos anómalos.** Horas.

**Las tres advertencias de uso.**

1. **El paso 2 es el que nadie hace y el que resuelve.** La intuición lleva al número de ficheros, que es el más impresionante y el menos informativo. **El número de grupos es la huella digital del inquilino.**
2. **Todo el procedimiento depende de que el registro de auditoría exista y cubra la ventana declarada**, y la retención por omisión suele ser menor de lo que la gente cree. **Ampliarla es barato y hay que hacerlo antes, no después.**
3. **Y hay un resultado posible que conviene anticipar: que la reclamación sea cierta y corresponda a un incidente ya conocido y cerrado.** Un extorsionador puede reclamar material de una intrusión que la organización ya divulgó y remedió. **No es una contradicción: es reventa de material antiguo**, y la respuesta —notificación, no pago— es distinta de la de una brecha nueva.

## Anexo E — Marcos de referencia empleados

- **ICD 203**, con la advertencia del `Anexo C`: **la precisión decimal de una magnitud declarada por un adversario no es evidencia de su veracidad**; lo que cuenta es si existe un camino para comprobarla.
- **Código Admiralty/OTAN**, con el grado **medición propia** y con la observación de que aquí **la fuente más fiable es la que menos se puede usar** (`Anexo B`).
- **MITRE ATT&CK: deliberadamente sin mapa.** Sin TTP registradas ni procedimientos observados, como en `CTI-2026-048` y `049`.
- **Graduación de la prueba de una entrada de sitio de filtración**, `Anexo D` de `CTI-2026-048`: este actor opera en **niveles 3 y 4 sin pasar por el 2**, que es el perfil de prueba invertido de `KJ-4`.
- **Evaluación de una reclamación de captura de inquilino**, propio de este informe (`Anexo D`): cuatro pasos, y la observación de que **el número de grupos es la huella digital del inquilino** y el dato que nadie comprueba.

## Anexo F — Paquete legible por máquina

Las tablas `cti:ioc` alimentan `ioc_index.csv`. **Cinco advertencias:**

1. **No hay indicadores de compromiso.** `PAP:WHITE`. Los patrones de `A.2` son de **auditoría de inquilino**, no de red ni de puesto.
2. **No se reproduce ningún nombre de víctima.** Ninguna ha confirmado, hay duplicados medidos y un tercero advierte de posibles fabricaciones.
3. **El recuento de 35 no es un recuento de organizaciones.** Son **26 descripciones distintas** con al menos cuatro víctimas duplicadas: del orden de **31**. Extraer «35 víctimas» sería el error que el informe mide.
4. **Las magnitudes declaradas no se transcriben como datos de la víctima**, sino como ejemplos del formato del actor. **No están verificadas y la organización que las vea referidas a ella debe comprobarlas con `T-1`.**
5. **Y los tres patrones de auditoría de `A.2` valen con independencia de este actor.** Son higiene de identidad en la nube, y es el único uso defendible de un informe sobre un objeto de nueve días.

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-11-19 | Emisión inicial, quinta de la serie `046`–`053`. Incluye: la **ausencia de cifrado medida en las 35 entradas** y la reclasificación del actor como extorsión por tenencia de datos (`KJ-1`); el **hallazgo propio de duplicación y reciclaje del catálogo** —26 descripciones distintas para 35 entradas, al menos cuatro víctimas listadas dos veces y dos grupos de tres víctimas con descripción idéntica—, que corrobora de forma independiente la advertencia de un tercero sobre reclamaciones no verificadas o fabricadas (`KJ-2`, `E-2`); la **corrección de nuestra propia primera lectura**: las reclamaciones de Microsoft 365 son 9 de 35 y no el catálogo entero (`KJ-3`); el **perfil de prueba invertido** —magnitudes con decimales y 7 de 35 entradas con dominio— (`KJ-4`); la **inferencia de que el vector sería la identidad y no el puesto**, con el reordenamiento de medidas que implica (`KJ-7`, `E-3`); la **ausencia de exposición latinoamericana** (`KJ-6`); el dato de que **nació con el 40 % de su catálogo ya cargado** (`O-3`); y el método del `Anexo D` para evaluar una reclamación de captura de inquilino, con el número de grupos como huella digital | Célula CTI |

> **Nota sobre esta emisión.** Es el informe de la serie sobre el objeto más
> joven —**nueve días**— y el que mejor ilustra por qué un ranking de ventana
> corta no es un orden de prioridades: un sitio que nace con catorce entradas
> en un día ocupa el quinto puesto sin que nadie haya confirmado una sola de
> sus reclamaciones.
>
> **Y su aportación duradera no es sobre el actor sino sobre la clase de
> reclamación**: la captura de inquilino en la nube es un modelo de extorsión
> en crecimiento, invisible al perímetro de la organización, y el `Anexo D`
> queda escrito para la próxima.

## Anexo H — Realimentación del consumidor

1. **¿Está activo el registro de auditoría del inquilino, con retención de al menos 90 días y consultable?** Es `X-2.1`, la decisión 1 de `E-4` y **el paso 6 de `T-1`**. **Si la respuesta es no, ninguna reclamación de captura de inquilino podrá comprobarse nunca**, y ésa es la conclusión del informe en esa organización.
2. **¿Se han revisado las aplicaciones con consentimiento y los permisos de lectura amplia sobre directorio y correo?** Es `X-2.2`: la vía más silenciosa de una captura como las que este actor describe.
3. **Si aparecemos listados: ¿se comparó el número de grupos del inquilino con el declarado?** Es el **paso 2 de `T-1`** y el que nadie hace. **El número de ficheros impresiona; el número de grupos discrimina.**
4. **¿Alguien asumió que la reclamación es cierta y notificó a un regulador?** O **¿alguien asumió que es falsa y no revisó nada?** Las dos son errores del pre-mortem: **hay duplicados medidos y hay indicios de material real.**
5. **¿Se priorizó este actor por su quinto puesto en el ranking?** Nueve días de vida, 35 entradas, cuatro duplicados y ninguna confirmación.
6. **¿Puede alguien verificar los duplicados contra el sitio original del adversario?** Es `G-2` y el riesgo 1 del pre-mortem: **si los duplicados son del rastreador y no del catálogo, `KJ-2` se cae**. Esta célula no tiene acceso a la red oscura.
7. **¿Hay alguna víctima listada que haya confirmado o negado públicamente?** Es `G-3` y `G-5`, y **resolvería de golpe las dos dudas centrales del informe**.
8. **Y la pregunta de método:** el `Anexo D` sostiene que el número de grupos de un inquilino es su huella digital, porque la relación entre plantilla y grupos es idiosincrásica y no se deduce desde fuera. **¿Alguien ha comprobado esa relación en un inquilino real y ha encontrado que sí es estimable?** Si lo es, el paso 2 pierde su poder discriminante y el método necesita otro.

*Fin del informe `CTI-2026-050` v1.0.*
