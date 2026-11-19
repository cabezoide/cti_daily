---
tlp: "TLP:CLEAR"
pap: "PAP:AMBER"
id: "CTI-2026-047"
version: "1.0"
tipo: "Perfil de operación de extorsión"
foco_regional: "Global · Brasil · Latinoamérica"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "INC Ransom · Inc Ransom · (marca hermana) Lynx"
fecha: "2026-11-19"
caduca: "2027-02-19"
autor: "Célula CTI"
distribucion: "Elaborado con fuentes abiertas y con medición propia sobre la interfaz pública de consulta de un rastreador de sitios de filtración. No contiene telemetría de la organización emisora ni datos de terceros. Difusión libre, conservando la atribución de las fuentes y las salvedades de §3. Se mantiene PAP:AMBER: las herramientas del Anexo A.3 son legítimas y de uso administrativo normal, y no deben cargarse en bloqueo."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-047

## INC Ransom publicó cincuenta víctimas en un solo día, y según la fecha con que se cuente es el actor más activo de la semana o casi inactivo

### Ocho sitios de filtración abiertos y sólo dos en pie · y «Lynx» no es su sucesor sino su marca hermana, operando a la vez

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-047` |
| Versión | 1.0 — 2026-11-19 |
| Clasificación | `TLP:CLEAR` · `PAP:AMBER` |
| Objeto | **INC Ransom**, tercera operación del lote por volumen de 2026 y la que mejor ilustra el problema de medición que `CTI-2026-046` §O-3.1 estableció |
| Foco regional | **22 víctimas latinoamericanas de 435 (5,1 %), con Brasil a la cabeza (9) y una chilena.** Tercera del lote en exposición regional, muy por detrás de Qilin y TheGentlemen |
| Horizonte | Estratégico 6–12 meses · táctico días |
| Origen de los datos | **Medición propia** sobre 435 registros de víctimas de 2026, más cinco fuentes de proveedor y un análisis industrial |
| Lo que lo distingue en este lote | Es **el caso extremo de divergencia de conteo** —7 frente a 58 víctimas en siete días, un factor de 8,3— y el único con **una marca hermana documentada que opera simultáneamente** |
| Caducidad | 2027-02-19 |
| Autor | Célula CTI |

<!-- cti:note type="warn" -->

> ⚠ **Tres advertencias, y la primera es de aritmética.**
>
> 1. **Toda cifra de ventana corta de este informe lleva su base de conteo.**
>    `CTI-2026-046` §O-3.1 estableció que un registro tiene dos fechas
>    —publicación y ataque declarado— y que para este actor las dos cuentas de
>    siete días difieren en **un factor de 8,3**. Es el caso más extremo del
>    lote y el motivo de que la regla exista.
> 2. **Los recuentos acumulados de las fuentes externas no son homogéneos y no
>    se deben sumar**: 991 víctimas reclamadas al 9 de noviembre de 2026 según
>    un proveedor, «más de 830 desde 2023» según otro en junio, y **435 en
>    2026** según nuestra medición. Son tres métodos y tres momentos.
> 3. **No tenemos aviso gubernamental para este actor.** A diferencia de
>    `CTI-2026-046`, todo lo que aquí se afirma sobre capacidades y vías de
>    acceso procede de proveedores, con el grado que `Anexo B` les asigna.

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** **El dato más importante de este informe es una tanda: INC Ransom publicó cincuenta entradas en su sitio de filtración el 12 de noviembre de 2026, y eso hace que su actividad semanal valga 7 o 58 según cómo se cuente.** Contado por **fecha de ataque declarada**, tiene **7 víctimas** en los últimos siete días; contado por **fecha de publicación**, tiene **58**. La divergencia es de **×8,3**, la mayor de los nueve actores que pudimos medir. El ranking del sitio que motiva este lote le asigna 9, y por tanto se parece a la primera base. Valoramos **casi con certeza** *(≥99 %)* la existencia de la tanda y la magnitud de la divergencia, ambas verificadas en los datos. **Confianza: alta.** *Corroboración independiente:* un recuento semanal de tercero registró **cincuenta publicaciones de INC en la semana del 9 al 15 de noviembre, frente a una la semana anterior**, lo que coincide con nuestra medición sin compartir método. *Consecuencia:* **cualquier afirmación sobre «la actividad de INC esta semana» es indeterminada sin declarar la base**, y ésa es la lección que el lote entero hereda.

**KJ-2.** **Ha abierto ocho sitios de filtración y sólo dos siguen en pie, y esa rotación es una propiedad medible de la operación.** El rastreador registra **ocho ubicaciones** asociadas a esta marca, de las cuales **seis están marcadas como no disponibles y dos como activas**. Valoramos **muy probable** *(80–95 %)* que esto refleje pérdida y reposición repetida de infraestructura de publicación —por caída, por bloqueo o por decisión propia— frente a la alternativa de ocho sitios simultáneos de los que seis se abandonaron. **Confianza: moderada**, porque el rastreador no fecha las bajas. *Consecuencia:* **un indicador basado en la dirección de su sitio de filtración caduca con rapidez**, y la vigilancia tiene que ser por marca, no por dirección.

**KJ-3.** **«Lynx» se describe habitualmente como el cambio de marca de INC Ransom, y esa descripción es incorrecta en el punto que importa: las dos marcas operan a la vez.** El vínculo técnico está bien soportado —se le atribuye compartir una proporción grande del código, y un análisis de proveedor publicó la tesis del cambio de marca— pero **los datos de actividad de 2026 muestran a las dos publicando víctimas en el mismo período**, y un análisis industrial registra que **las reclamaciones industriales de INC subieron de 50 a 58 entre el segundo y el tercer trimestre de 2026 mientras las de Lynx bajaban a una**. Valoramos **probable** *(55–80 %)* que se trate de **dos marcas de una misma operación con políticas declaradas distintas**, y **poco probable** *(20–45 %)* que sea una sucesión. **Confianza: moderada.** *La evidencia más dura la aporta un tercero:* **un operador conectado a los paneles de negociación de las dos marcas**. *Consecuencia defensiva:* **la detección construida contra una sirve contra la otra**, y un incidente atribuido a Lynx debe tratarse con este expediente.

**KJ-4.** **Y la diferencia entre las dos marcas no es técnica sino declarativa, lo que convierte sus «reglas» en marketing.** A Lynx se le atribuyen reglas de afiliación que **excluyen sanidad y gobierno**; la victimología documentada de INC incluye **un servicio de salud público británico y un ayuntamiento**, y un proveedor sitúa la sanidad en torno al **15 %** de sus víctimas conocidas. Valoramos **probable** *(55–80 %)* que la misma base de código y plausiblemente el mismo personal estén operando bajo dos conjuntos de reglas incompatibles. **Confianza: moderada.** *La lectura, que esta cartera ya hizo en `CTI-2026-042`:* **una lista de exclusiones es un instrumento de reputación de marca, no un compromiso**, y la forma de comprobarlo es exactamente ésta: buscar la misma capacidad operando sin esa lista bajo otro nombre.

**KJ-5.** **Su exposición regional es baja pero no nula, y tiene nombre de país: Brasil.** De 435 registros de 2026, **22 son latinoamericanos —el 5,1 %—**: **Brasil 9**, México 6, Argentina 3, **Chile 1**, y uno cada uno en Costa Rica, Panamá y Colombia. Es la tercera exposición regional del lote, por detrás de Qilin (122) y TheGentlemen (129) y por delante de Akira (7, y ninguna chilena). Valoramos **probable** *(55–80 %)* que el perfil regional sea estable. **Confianza: moderada** — fuente única. *Consecuencia:* para una organización brasileña, INC Ransom entra en el grupo de amenazas a considerar; para una chilena, está en el límite inferior.

**KJ-6.** **Hay una vía de acceso inicial compartida entre marcas, y si se confirma es la medida defensiva más rentable de este informe.** Un análisis industrial valora **con confianza moderada** que una campaña de explotación concreta funciona como **conducto de acceso inicial que sirve a INC, a Lynx y posiblemente a otras marcas**, y documenta además explotación de **vulnerabilidades de SonicWall SMA 1000**. Valoramos **probable** *(55–80 %)* la existencia de un conducto compartido de acceso, respetando la confianza moderada de la fuente y sin elevarla. **Confianza: moderada.** *Consecuencia:* **parchear el borde no defiende de una marca, defiende de un mercado**, porque el acceso se compra y se revende aguas arriba de la decisión de qué marca despliega.

**KJ-7.** **Su cadena está construida con software legítimo, igual que la de Akira, pero con una peculiaridad: usa herramientas de respaldo para exfiltrar.** El inventario publicado incluye **BackBlaze, Restic y `s5cmd`** —dos productos de copia de seguridad y un cliente de almacenamiento de objetos— además de RClone, MEGA, 7-Zip y WinRAR. Valoramos **muy probable** *(80–95 %)* que esto haga la exfiltración especialmente difícil de distinguir del tráfico legítimo de respaldo. **Confianza: alta como dato publicado.** *Consecuencia operativa, y es específica de este actor:* **el control de egreso tiene que distinguir el destino de respaldo autorizado de cualquier otro**, porque aquí el adversario usa la misma clase de herramienta que el equipo de operaciones.

**KJ-8.** **Los recuentos acumulados que circulan sobre este actor difieren en cientos de víctimas, y conviene no promediarlos.** Un proveedor cifra en **991 las víctimas reclamadas al 9 de noviembre de 2026**; otro hablaba de **más de 830 desde 2023** en junio de 2026; su propia ficha en el rastreador menciona **más de 200 en 2025**; y nuestra medición da **435 en 2026**. Valoramos **casi con certeza** *(≥99 %)* que las cuatro cifras sean correctas para su método y su fecha, y **muy probable** *(80–95 %)* que **sumarlas o promediarlas produzca un número sin significado**. **Confianza: alta.** *Es el mismo problema de `KJ-1` a otra escala: el recuento no es la víctima.*

---

## 2. Resumen ejecutivo

INC Ransom es la tercera operación de este lote por volumen de 2026 —**435 víctimas reclamadas**— y la que mejor enseña por qué los rankings de actividad semanal no se pueden leer sin preguntar cómo se cuentan.

**El 12 de noviembre de 2026 publicó cincuenta entradas en su sitio de filtración en un solo día.** Las fechas de ataque que declara para ellas están repartidas por las semanas anteriores. El resultado es que, en la ventana de siete días que motiva este lote, **esta operación tiene 7 víctimas si se cuenta por fecha de ataque y 58 si se cuenta por fecha de publicación**: una divergencia de **8,3 veces**. Un recuento semanal independiente registró lo mismo sin compartir método —cincuenta publicaciones en la semana del 9 al 15 de noviembre frente a una la semana anterior—, de modo que la tanda es un hecho y no un artefacto de nuestra medición. **Las dos cifras son correctas y describen cosas distintas**, y a partir de este informe la serie declara siempre la base.

Dos cosas más sobre la operación en sí merecen la atención del lector.

La primera es que **ha abierto ocho sitios de filtración y sólo dos siguen en pie.** Seis están registrados como no disponibles. No sabemos por qué cayeron, pero el patrón importa para la práctica: **vigilar a este actor por la dirección de su sitio es perder el rastro cada pocos meses**, y la vigilancia tiene que ser por marca.

La segunda es la relación con **Lynx**, que se describe habitualmente como «el cambio de marca de INC Ransom». Esa descripción es cómoda y falla en lo esencial: **las dos marcas publican víctimas en el mismo período de 2026**. No es una sucesión, son dos marcas a la vez. La evidencia más dura la aporta un tercero —**un operador conectado a los paneles de negociación de ambas**— y un análisis industrial muestra sus curvas divergiendo en el mismo trimestre. Y aquí aparece lo interesante: **a Lynx se le atribuyen reglas que excluyen sanidad y gobierno, mientras la victimología documentada de INC incluye un servicio de salud público británico y un ayuntamiento**, con la sanidad en torno al 15 % de sus víctimas. La misma base de código, plausiblemente el mismo personal, y dos conjuntos de reglas incompatibles. **Una lista de exclusiones no es un compromiso: es un argumento de venta**, y este caso es la demostración limpia.

Para esta región la exposición es baja pero tiene nombre: **22 víctimas latinoamericanas, con Brasil a la cabeza con nueve y una sola chilena.** Está por delante de Akira —que no tiene ninguna chilena— y muy por detrás de Qilin y TheGentlemen, los dos actores que esta cartera ya documentaba.

Y hay una recomendación que paga más que cualquier detección: un análisis industrial valora con confianza moderada que **una campaña de explotación concreta funciona como conducto de acceso inicial compartido por INC, por Lynx y posiblemente por otras marcas**. Si eso es cierto —y la fuente no lo afirma con más fuerza— **parchear el borde no defiende de un grupo, defiende de un mercado**, porque el acceso se compra aguas arriba de la decisión de qué marca cifra.

---

## 3. Alcance y limitaciones

### 3.1 Qué cubre

La operación INC Ransom: su curva de actividad medida sobre las dos bases de conteo, su rotación de infraestructura de publicación, su relación con la marca Lynx, su victimología global y regional, su inventario de capacidades publicado, y las vías de acceso inicial que los proveedores le atribuyen.

### 3.2 Qué NO cubre

| Fuera de alcance | Por qué |
|---|---|
| **Análisis del cifrador** | Sin muestras. La afirmación de código compartido con Lynx es de proveedor (`O-5`) |
| **La identidad del conducto de acceso** | El análisis industrial nombra una campaña concreta; **no verificamos ni su existencia ni su alcance**, y respetamos su confianza moderada (`KJ-6`) |
| **Un expediente de Lynx** | Esta cartera no lo tiene. `KJ-3` sostiene que **debería ser una sección de este expediente y no un documento aparte**, y es `G-5` |
| **Los recuentos acumulados** | Cuatro cifras incompatibles de cuatro fuentes. Se citan con su método y su fecha, **sin reconciliarlas** |
| **Indicadores de red o de fichero** | El rastreador no los publica. Es `G-2` y, como en `CTI-2026-046`, significa que este informe **no aporta nada ingerible salvo patrones** |

### 3.3 Limitaciones de la colección

<!-- cti:note type="warn" -->

> ⚠ **Seis limitaciones.**
>
> 1. **Sin fuente gubernamental.** Todo lo de capacidades y acceso es de
>    proveedor. Es la diferencia principal con `CTI-2026-046`.
> 2. **Las cifras son reclamaciones de un sitio de filtración**, no brechas
>    verificadas, y este actor acaba de demostrar que **publica en tandas**.
> 3. **El rastreador no fecha la baja de los seis sitios caídos**, de modo que
>    `KJ-2` describe un estado y no una cronología.
> 4. **El inventario de capacidades no está verificado** por nosotros (`G-3`).
> 5. **La tesis del código compartido con Lynx la leímos por referencia**, no
>    en el análisis original. Es `G-4`.
> 6. **Y una limitación propia: nuestra cuenta de siete días por publicación
>    (58) incluye la tanda del día 12, y la del ranking (9) no.** No publicamos
>    una sola cifra: publicamos las dos y la base de cada una.

### 3.4 Qué aporta

| Aporte | Dónde |
|---|---|
| **La tanda del 12 de noviembre medida**, con la divergencia de ×8,3 y su corroboración independiente | `KJ-1`, `O-3` |
| **La rotación de infraestructura cuantificada**: ocho sitios abiertos, dos en pie | `KJ-2` |
| **La refutación de «Lynx es el sucesor de INC»**: operan a la vez | `KJ-3`, `O-5` |
| **La contradicción entre las reglas declaradas de una marca y la victimología de la otra** | `KJ-4`, `E-3` |
| **La exposición regional con nombre de país**: 22, Brasil 9, Chile 1 | `KJ-5`, `E-4` |
| **La peculiaridad de exfiltrar con herramientas de respaldo**, y la medida que se sigue | `KJ-7`, `X-2.3` |
| **Las cuatro cifras acumuladas incompatibles, consignadas sin reconciliar** | `KJ-8` |

### 3.5 Veredicto

<!-- cti:table highlight="CORROBORADO|NO SOSTENIDO|propio|REENCUADRADO" -->

| # | Elemento | Veredicto | Base |
|---|---|---|---|
| 1 | INC Ransom es uno de los actores más activos de la semana | **INDETERMINADO SIN BASE DE CONTEO — y es el hallazgo** | 7 por fecha de ataque, **58 por publicación** (`KJ-1`) |
| 2 | Es una operación de alto volumen sostenido | **CORROBORADO** | 435 víctimas en 2026, tercera del lote |
| 3 | Su infraestructura de publicación es estable | **NO SOSTENIDO** | **Ocho sitios abiertos, seis caídos** (`KJ-2`) |
| 4 | Lynx es su sucesor | **NO SOSTENIDO — REENCUADRADO** | **Operan simultáneamente en 2026.** Son marcas hermanas (`KJ-3`) |
| 5 | Lynx excluye sanidad y gobierno | **CORROBORADO como declaración, IRRELEVANTE como garantía** | INC ataca sanidad (~15 %) y gobierno con la misma base de código (`KJ-4`) |
| 6 | Es una amenaza de primer orden para la región | **NO SOSTENIDO** | 5,1 % latinoamericanas, **una chilena** (`KJ-5`) |
| 7 | Hay un conducto de acceso compartido entre marcas | **PROBABLE, con la confianza moderada de su fuente** | Análisis industrial; SonicWall SMA 1000 (`KJ-6`) |
| 8 | Sus cifras acumuladas son comparables entre fuentes | **NO SOSTENIDO** | 991 · 830+ · 200+ · 435, cuatro métodos (`KJ-8`) |

---

# NIVEL ESTRATÉGICO
### Para: CISO, Riesgo, Arquitectura · Horizonte: 6–12 meses

## E-1. Qué clase de operación es

<!-- cti:cards -->

| Rasgo | Qué significa | Etiqueta |
|---|---|---|
| **Publica en tandas, no a ritmo** | Cualquier métrica de «actividad reciente» sobre este actor es inestable por construcción. **Hay que mirar el mes, no la semana** | `01 · ritmo` |
| **Ocho sitios abiertos, dos en pie** | La marca sobrevive a su infraestructura. Vigilancia por marca, no por dirección | `02 · infraestructura` |
| **Dos marcas a la vez con reglas distintas** | Las reglas declaradas son marketing. **Y la detección de una vale para la otra** | `03 · doble marca` |
| **Cadena de software legítimo, con herramientas de respaldo** | La exfiltración se parece al respaldo. **El control tiene que ser por destino autorizado** | `04 · indistinguibilidad` |
| **Acceso plausiblemente comprado aguas arriba** | Parchear el borde defiende de varias marcas a la vez | `05 · mercado de acceso` |
| **Sanidad y gobierno sin exclusión** | Un servicio de salud público y un ayuntamiento entre sus víctimas documentadas | `06 · sin límites` |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `435` | Víctimas reclamadas en 2026 (medición propia) | Tercera del lote, tras Qilin (1.221) y TheGentlemen (1.020) |
| `50` | Entradas publicadas **en un solo día**, el 12-11-2026 | **El 11,5 % de su año en una jornada** |
| `7 / 58` | Víctimas de 7 días por **fecha de ataque** / por **publicación** | **Divergencia de ×8,3: la mayor del lote** |
| `8 → 2` | Sitios de filtración abiertos → activos | Seis caídos |
| `73` | Víctimas en los últimos 30 días (por publicación) | El 17 % de su año |
| `22` | Víctimas latinoamericanas | **5,1 %. Brasil 9 · México 6 · Argentina 3 · Chile 1** |
| `58` | Países distintos alcanzados en 2026 | La operación de mayor dispersión geográfica del lote tras Qilin |
| `~15 %` | Proporción de sanidad entre sus víctimas, según proveedor | Con un servicio de salud público y un ayuntamiento documentados |

## E-2. Lo que la tanda del 12 de noviembre enseña

**El hecho:** cincuenta entradas publicadas en un día, con fechas de ataque declaradas repartidas por semanas anteriores.

**Las tres lecturas posibles, y por qué no hace falta decidir entre ellas para actuar:**

| Lectura | Qué implicaría | Estado |
|---|---|---|
| **Vaciado de cola de negociación** | Cincuenta víctimas cuyos plazos vencieron a la vez o cuyas negociaciones fracasaron en bloque | **Retenida como principal.** Es compatible con las fechas de ataque repartidas |
| **Decisión de visibilidad** | Publicar en bloque para ocupar los rankings y los titulares de la semana | Retenida como concurrente |
| **Reciclaje o relleno** | Entradas antiguas, duplicadas o de terceros republicadas | **Poco probable aquí**, porque las fechas de ataque están repartidas y son verosímiles. **Es la lectura que sí aplica a otros actores de este lote** |

> **Y la consecuencia de gestión, que es la única que importa:** si alguien
> construye un panel de «grupos más activos esta semana» alimentado por este
> rastreador, **ese panel subirá y bajará a este actor en un factor de ocho
> según el día de la consulta y la base de conteo**. La métrica estable para
> priorizar es **el acumulado de treinta días o del año**, y la semanal sirve
> para detectar tandas, que es otra cosa y también útil.

## E-3. Las dos marcas y lo que su contradicción enseña

| Dimensión | **INC Ransom** | **Lynx** |
|---|---|---|
| Relación | — | Se describe como **cambio de marca de INC**; comparte una proporción grande del código según proveedor |
| Actividad en 2026 | **435 víctimas** reclamadas; reclamaciones industriales **50 → 58** entre 2.º y 3.º trimestre | Reclamaciones industriales **bajando a una** en el 3.º trimestre |
| ¿Simultáneas? | **Sí.** Las dos publican en el mismo período | **Sí** |
| Reglas declaradas | **Ninguna exclusión conocida** | **Excluye sanidad y gobierno**, según sus reglas de afiliación |
| Victimología real | **Sanidad ~15 %**, con un servicio de salud público y un ayuntamiento documentados | Reclamó un proveedor de ciclo de ingresos sanitario en abril de 2026 según un recuento |
| Evidencia dura del vínculo | **Un operador conectado a los paneles de negociación de las dos marcas**, según un proveedor | |

**La conclusión que este cuadro soporta, y es `KJ-4`:** cuando una operación mantiene dos marcas y sólo una declara exclusiones éticas, **la lista de exclusiones no describe lo que el grupo hace: describe lo que quiere que se crea de una de sus marcas.** `CTI-2026-042` llegó a la misma conclusión por otro camino —una política de afiliados que prohibía la salud infantil y autorizaba la infraestructura crítica—, y aquí el mecanismo es más limpio: **la misma capacidad opera sin la lista bajo otro nombre.**

**Y la consecuencia defensiva es económica:** si son dos marcas de una operación, **no hacen falta dos programas de detección**. Un incidente atribuido a Lynx se trata con este expediente, y al revés. Es `G-5`: la cartera no necesita un informe de Lynx, necesita una sección aquí.

## E-4. Exposición regional

| Actor del lote | Víctimas 2026 | Latinoamericanas | % | Chilenas | Brasileñas |
|---|---|---|---|---|---|
| Qilin *(en cartera)* | 1.221 | **122** | 10,0 % | **20** | 10 |
| TheGentlemen *(en cartera)* | 1.020 | **129** | 12,6 % | 9 | **36** |
| **INC Ransom** | **435** | **22** | **5,1 %** | **1** | **9** |
| Akira | 420 | 7 | 1,7 % | **0** | 3 |
| n0n | 259 | 11 | 4,2 % | 0 | 6 |
| settra | 116 | 5 | 4,3 % | 0 | 3 |
| pixelleaks | 34 | 3 | 8,8 % | 0 | 0 |
| vortex | 35 | 0 | 0,0 % | 0 | 0 |
| curious worm | 18 | 0 | 0,0 % | 0 | 0 |

**Todas las filas, el mismo conjunto de datos, el mismo día, la misma metodología.** INC Ransom es la tercera exposición regional del lote y su país regional es **Brasil**, con nueve víctimas. Para Chile, **una sola víctima en 435 registros**: presente, marginal.

> **Y una observación sobre el conjunto de la tabla que ya apareció en
> `CTI-2026-046` y que este informe confirma: los dos actores que esta cartera
> ya tenía documentados son, con mucha diferencia, los dos de mayor exposición
> regional del top 10.** El lote de ocho añade cobertura, no corrige una
> omisión.

## E-5. Decisiones que este informe pide

| # | Decisión | A quién | Coste | Por qué |
|---|---|---|---|---|
| **1** | **No priorizar por métricas de ventana semanal de este rastreador** | CTI | Cero | `KJ-1`: ×8,3 de divergencia. Usar treinta días o el año |
| **2** | **Distinguir en el control de egreso el destino de respaldo autorizado de cualquier otro** | Red · Operaciones | Medio | `KJ-7`: exfiltra con BackBlaze, Restic y `s5cmd` |
| **3** | **Tratar Lynx e INC como un solo expediente de detección** | SOC · CTI | **Cero, y ahorra** | `KJ-3`: dos marcas, una operación |
| **4** | **Parchear concentradores de acceso remoto expuestos con prioridad** | Operaciones | Medio | `KJ-6`: SonicWall SMA 1000 y un conducto de acceso compartido |
| **5** | **No usar las listas de exclusión declaradas de ningún grupo en el análisis de riesgo** | Riesgo | Cero | `KJ-4`: la misma operación opera sin ellas bajo otro nombre |
| **6** | **Si somos prestador de salud o administración pública: asumir que no hay exclusión** | Dirección | Cero decidirlo | ~15 % de sanidad, con un servicio público y un ayuntamiento documentados |
| **7** | **Vigilar por marca y no por dirección del sitio de filtración** | CTI | Bajo | `KJ-2`: ocho abiertos, seis caídos |

---

# NIVEL OPERACIONAL
### Para: SOC, Respuesta a incidentes, Threat Hunting · Horizonte: semanas

## O-1. Identificación

| Campo | Valor |
|---|---|
| Nombre | **INC Ransom** · también escrito `Inc Ransom` |
| Marca hermana | **Lynx** — se le atribuye compartir una proporción grande del código; **opera simultáneamente** (`KJ-3`) |
| Primera observación | **Julio–agosto de 2023**; en el rastreador desde **2023-08-09** |
| Sitios de filtración | **Ocho registrados, dos activos** al 19-11-2026 |
| Modelo | Extorsión por datos con cifrado, afiliados. **Sin exclusiones declaradas conocidas** |
| Capacidades documentadas | **28 técnicas en 13 tácticas** según el rastreador |
| Estado | **Activa**, con tanda de cincuenta publicaciones el 12-11-2026 |
| Aviso gubernamental | **Ninguno localizado** |

## O-2. El inventario de capacidades

| Bloque | Herramientas documentadas | Qué obliga |
|---|---|---|
| **Administración remota** | **AnyDesk** | Inventario de autorizadas + alerta (`X-2.1`). Una sola, frente a las seis de Akira |
| **Descubrimiento** | AdFind · Advanced IP Scanner · SoftPerfect NetScan | Enumeración de directorio y barrido interno |
| **Credenciales** | Mimikatz | **La única herramienta inequívocamente ofensiva del inventario** |
| **Exfiltración** | **7-Zip · BackBlaze · MEGA · RClone · Restic · WinRAR · `s5cmd`** | **Siete herramientas, y tres son de respaldo o almacenamiento de objetos.** Es la peculiaridad de `KJ-7` |
| **LOLBAS** | `Finger` · PsExec | **`Finger` es inusual y por eso es buena señal**: casi ninguna organización lo usa legítimamente hoy |
| **Red** | Bitvise SSH Client | Túnel o transferencia cifrada |

> **Dos lecturas del inventario.**
>
> La primera: **es notablemente más pequeño que el de Akira** —28 técnicas
> frente a 48, una herramienta de administración remota frente a seis—. Eso no
> significa menos capacidad: significa **menos documentada**, y la diferencia
> puede estar en cuántos equipos de respuesta han publicado sobre cada una.
> **No se debe leer el tamaño del inventario como medida de sofisticación**
> (`H-4`).
>
> La segunda, y es la aportación práctica: **`Finger` en una red moderna es
> casi siempre anómalo.** Es un protocolo de 1977 que ninguna organización
> actual usa para administrar, y su presencia en una línea de órdenes es una
> señal de coste de falso positivo muy bajo. **De todo el inventario, es el
> indicador más específico y el más barato.**

## O-3. La actividad medida, sobre las dos bases

| Ventana | Por **fecha de ataque** | Por **publicación** | Nota |
|---|---|---|---|
| Año 2026 | 435 | 435 | Coinciden por construcción |
| Últimos 30 días | 48 | **73** | ×1,5 |
| **Últimos 7 días** | **7** | **58** | **×8,3 — la mayor divergencia del lote** |
| Ranking del sitio *(16:20 UTC del 19-11)* | — | — | **9** |

**El perfil diario de publicación en noviembre**, que es lo que explica todo lo anterior:

<!-- cti:chart title="Publicaciones diarias de INC Ransom en noviembre de 2026" cap="La barra del día 12 son cincuenta entradas: el 11,5 % de su año en una jornada. Medición propia." -->

| Día | Entradas publicadas |
|---|---|
| `03-nov` | 6 |
| `08-nov` | 3 |
| `11-nov` | 1 |
| `12-nov` | 50 |
| `13-nov` | 2 |
| `16-nov` | 2 |
| `19-nov` | 2 |

**Y el reparto, sobre los 435 registros:** sectorialmente, **Servicios profesionales 113**, Manufactura 60, Tecnología 43. Geográficamente, **Estados Unidos 256**, Canadá 15, Alemania 12, **Brasil 9**, India 8, Australia 8. **Veinticuatro registros llevan referencia de prensa**, lo que es un indicador indirecto de que esas víctimas fueron confirmadas por terceros.

## O-4. Nuestra exposición

| Si la organización… | Exposición | Medida |
|---|---|---|
| **Es brasileña** | **La más alta de la región para este actor**: 9 de las 22 víctimas regionales | Parcheo de borde + control de egreso |
| **Es chilena** | **Baja**: una víctima en 435 | No desatender; la vía es genérica |
| **Es prestador de salud o administración pública** | **Alta.** ~15 % de sanidad, con un servicio público y un ayuntamiento documentados. **Y sin exclusión declarada** | `E-5.6` |
| **Es de servicios profesionales** | **Alta.** Su sector principal: 113 de 435 | Igual |
| **Usa BackBlaze, Restic o `s5cmd` legítimamente** | **Alta en términos de detección**: su exfiltración se confunde con su respaldo | **`X-2.3` es la medida específica** |
| **Tiene concentradores de acceso remoto expuestos** | **Alta** | `KJ-6` |

## O-5. La relación con Lynx, evaluada

**Lo que sostiene el vínculo:**

1. **Código compartido** en proporción grande, según proveedor, y un análisis titulado explícitamente como la tesis del cambio de marca. **Lo leímos por referencia, no en original** (`G-4`).
2. **Un operador conectado a los paneles de negociación de las dos marcas**, según otro proveedor. **Es la evidencia más dura del conjunto**, porque es una observación de infraestructura y no una comparación de código.
3. **Curvas de actividad complementarias** en el mismo trimestre según un análisis industrial: INC subiendo de 50 a 58 reclamaciones industriales mientras Lynx baja a una.

**Lo que refuta la lectura de «sucesión»:** las dos publican en 2026. Un cambio de marca implica que la anterior deja de publicar; aquí no ocurre.

**El juicio, en dos partes:**

| Afirmación | Probabilidad | Confianza |
|---|---|---|
| INC y Lynx comparten código y plausiblemente personal | **Probable** *(55–80 %)* | Moderada |
| Lynx **sucedió** a INC | **Poco probable** *(20–45 %)* | Moderada |
| Son dos marcas de una misma operación, con políticas declaradas distintas | **Probable** *(55–80 %)* | Moderada |

> **Y por qué esto no es una discusión de taxonomía.** Si son dos marcas de
> una operación, **la detección es una y el expediente es uno**. Si fueran dos
> operaciones distintas con código común, harían falta dos expedientes y dos
> seguimientos de victimología. **La respuesta determina cuánto cuesta
> defenderse**, y por eso `G-5` pide cerrar la pregunta en lugar de dejarla
> como curiosidad.

## O-6. Hipótesis alternativas y pre-mortem

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| **H-1 — La tanda del 12-11 es un vaciado de cola de negociación** | **Retenida como principal.** Las fechas de ataque están repartidas y son verosímiles | `Probable · 55–80 %` |
| **H-2 — La tanda es relleno o reciclaje** | **Poco probable para este actor**, por las fechas repartidas y por las veinticuatro referencias de prensa del conjunto. **Sí es la hipótesis principal para otros actores del lote** | `Poco probable · 20–45 %` |
| **H-3 — INC y Lynx son dos marcas de una operación** | **Retenida como principal**, con la evidencia de `O-5` | `Probable · 55–80 %` |
| **H-4 — El inventario menor que el de Akira indica menos sofisticación** | **Descartada como inferencia.** 28 técnicas frente a 48 mide **documentación publicada**, no capacidad. Se consigna para que nadie lo reabra | `Poco probable · 20–45 %` |
| **H-5 — El conducto de acceso compartido existe** | **Retenida con la confianza moderada de su fuente**, sin elevarla. Si se confirma, es la medida más rentable del informe | `Probable · 55–80 %` |
| **H-6 — Los seis sitios caídos lo fueron por acción policial** | **Sin evidencia.** No hay ninguna fuente que lo afirme y el rastreador no fecha las bajas. Se consigna sólo para que no se asuma | `Aprox. igual de probable · 40–60 %` |

**Pre-mortem — si este informe se equivoca, será porque:**

1. **Alguien citó una de las dos cifras de siete días sin su base** y construyó una prioridad sobre un número que podía ser ocho veces mayor o menor.
2. **Se sumaron o promediaron los recuentos acumulados** de las cuatro fuentes (`KJ-8`).
3. **Se abrió un expediente separado de Lynx**, duplicando trabajo sobre la misma operación (`G-5`).
4. **Se usó la lista de exclusiones de Lynx en un análisis de riesgo** y una organización de salud concluyó que no era objetivo.
5. **Se leyó el inventario menor como menor peligro** (`H-4`).
6. **Se bloquearon BackBlaze, Restic o `s5cmd`** rompiendo el respaldo propio, en lugar de controlar el destino (`X-2.3`).

---

# NIVEL TÁCTICO
### Para: Analistas de SOC e ingeniería de detección · Horizonte: días

## T-1. Cadena de intrusión

<!-- cti:stages title="De un concentrador de acceso remoto a la exfiltración disfrazada de respaldo" dwell="next" -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 01 · Acceso | Borde de acceso remoto | **SonicWall SMA 1000** según análisis industrial · **conducto de acceso plausiblemente compartido con otras marcas** · **primera oportunidad: parcheo de borde** |
| Etapa 02 · Reconocimiento | Mapa del dominio | AdFind · Advanced IP Scanner · SoftPerfect NetScan · **`Finger`, que es la señal más específica del expediente** |
| Etapa 03 · Credenciales | Escalada | Mimikatz |
| Etapa 04 · Movimiento | Lateral | PsExec · Bitvise SSH Client |
| Etapa 05 · Persistencia | Administración remota | AnyDesk · **segunda oportunidad: herramienta no inventariada** |
| Etapa 06 · Exfiltración | **Disfrazada de respaldo** | 7-Zip · WinRAR para empaquetar · **BackBlaze · Restic · `s5cmd` · RClone · MEGA** para salir · **tercera oportunidad, y es la específica de este actor: destino de respaldo no autorizado** |
| Etapa 07 · Impacto | Cifrado y publicación | Cifrado · y **publicación en tanda** semanas después (`E-2`) |

## T-2. Mapa MITRE ATT&CK

<!-- cti:matrix -->

| Táctica | ID | Técnica | Procedimiento documentado |
|---|---|---|---|
| Acceso inicial | T1190 | Exploit Public-Facing Application | **SonicWall SMA 1000**, según análisis industrial |
| Acceso inicial | T1133 | External Remote Services | Concentradores de acceso remoto |
| Acceso inicial | T1078 | Valid Accounts | **Conducto de acceso compartido entre marcas** (`KJ-6`), confianza moderada |
| Descubrimiento | T1087.002 | Account Discovery: Domain Account | AdFind |
| Descubrimiento | T1046 | Network Service Discovery | Advanced IP Scanner · SoftPerfect NetScan |
| Descubrimiento | **T1087** | **Account Discovery** | **`Finger`** — protocolo heredado, anómalo en una red moderna |
| Credenciales | T1003.001 | OS Credential Dumping: LSASS Memory | Mimikatz |
| Movimiento lateral | T1021.002 | SMB/Windows Admin Shares | PsExec |
| Movimiento lateral | T1021.004 | Remote Services: SSH | Bitvise SSH Client |
| Mando y control | T1219 | Remote Access Software | AnyDesk |
| Recopilación | T1560.001 | Archive via Utility | 7-Zip · WinRAR |
| **Exfiltración** | **T1567.002** | **Exfiltration to Cloud Storage** | **BackBlaze · Restic · `s5cmd` · RClone · MEGA.** Tres de los cinco son herramientas de respaldo o de almacenamiento de objetos |
| Impacto | T1486 | Data Encrypted for Impact | Cifrador no analizado por nosotros |

## T-3. Pirámide del Dolor

<!-- cti:pyramid -->

| Nivel | Indicador | Valor para INC Ransom |
|---|---|---|
| Trivial | Hash | **Nulo.** Sin muestras |
| Fácil | Direcciones IP | **Nulo.** No publicadas (`G-2`) |
| Simple | **Dirección del sitio de filtración** | **Explícitamente malo aquí**: ocho abiertos, seis caídos (`KJ-2`). **Vigilar por marca** |
| **Molesto** | **`Finger` en una línea de órdenes** | **Alto y muy específico.** Protocolo heredado sin uso legítimo moderno: coste de falso positivo mínimo |
| **Molesto** | **Destino de egreso de respaldo no autorizado** | **El indicador propio de este actor** (`KJ-7`). Requiere una lista de destinos autorizados, que es trabajo de inventario |
| Irritante | Inventario de herramientas | Medio. Siete de exfiltración y una de administración remota |
| Difícil | TTP | **Borde → descubrimiento → exfiltración por canal de respaldo → cifrado → publicación en tanda.** Común con el resto del lote salvo el canal de respaldo |

## T-4. Hipótesis de caza

<!-- cti:accordion critical="^(H-1|H-2)\b" regional="^(H-6)\b" -->

| # | Hipótesis | Cómo se comprueba | Qué significa un positivo |
|---|---|---|---|
| **H-1** | **Hay egreso hacia un destino de respaldo o almacenamiento de objetos no autorizado** | Flujo de salida frente a la lista de destinos de respaldo corporativos. Buscar BackBlaze, almacenamiento S3 ajeno, Restic, `s5cmd`, RClone, MEGA | **La caza propia de este expediente.** Exfiltración en curso, disfrazada del tráfico más aburrido que existe |
| **H-2** | **Se ejecutó `finger` en algún equipo** | Líneas de órdenes de 90 días | **Coste de falso positivo casi nulo.** Reconocimiento con una herramienta que nadie usa |
| **H-3** | **AnyDesk presente y no inventariado** | Inventario frente a autorizadas | Etapa 05. **Vale igual contra los ocho actores del lote** |
| **H-4** | **AdFind ejecutado desde un puesto no administrativo** | Líneas de órdenes | Etapa 02 |
| **H-5** | **Bitvise SSH Client en un servidor Windows** | Inventario de software | Túnel o transferencia. Inusual en parque corporativo |
| **H-6** | **Aparecemos en su sitio de filtración** | Consulta al rastreador por nuestro nombre y país | Reclamación pública. **Con una víctima chilena en 435 es poco probable; la consulta es gratuita** |
| **H-7** | **Concentrador de acceso remoto expuesto sin parchear** | Barrido del perímetro | Etapa 01, y **defiende contra varias marcas a la vez** (`KJ-6`) |

## T-5. Brechas de visibilidad

| # | Brecha | Por qué duele | Cómo se cierra |
|---|---|---|---|
| **V-1** | **Sin lista de destinos de respaldo autorizados** | Hace inejecutable `H-1`, la caza propia del expediente | Inventario de destinos + política de egreso |
| **V-2** | Sin registro de líneas de órdenes 90 días | `H-2` y `H-4` | Auditoría de creación de procesos |
| **V-3** | Sin inventario de administración remota | `H-3` | Inventario + política |
| **V-4** | Sin visibilidad del volumen de egreso por destino | La etapa 06 pasa por un canal que parece legítimo | Métrica de bytes salientes por destino y por hora |

---

# NIVEL TÉCNICO
### Para: Ingeniería de detección · Vida útil: semanas

## X-1. Lógica de detección

```
# ---- 1. Exfiltración disfrazada de respaldo (la regla propia de este actor) ----
DESTINOS_RESPALDO_OK = { ... los destinos de respaldo de la organización ... }
HERRAMIENTAS_RESPALDO = { restic, s5cmd, rclone, backblaze, duplicati, ... }

si (proceso.nombre in HERRAMIENTAS_RESPALDO or destino in PROVEEDORES_ALMACENAMIENTO)
   y destino not in DESTINOS_RESPALDO_OK:
    alertar "EGRESO A DESTINO DE RESPALDO NO AUTORIZADO"      # severidad alta

# Y la variante que no depende de conocer la herramienta:
si bytes_salientes(host, ventana=1h) > umbral(host) y destino not in DESTINOS_OK:
    alertar "VOLUMEN DE EGRESO ANÓMALO A DESTINO NO AUTORIZADO"

# ---- 2. Finger: el indicador más específico y más barato ----
si linea_de_ordenes coincide /\bfinger(\.exe)?\b/:
    alertar "USO DE FINGER"                                   # severidad alta
    # Protocolo de 1977. En una red moderna no tiene uso legítimo conocido.

# ---- 3. AdFind desde un puesto que no es administrativo ----
si proceso.nombre == "adfind.exe" y host not in PUESTOS_ADMIN:
    alertar "ENUMERACIÓN DE DIRECTORIO CON ADFIND"

# ---- 4. Administración remota no inventariada (común a todo el lote) ----
si proceso.nombre in SOSPECHOSAS y proceso.nombre not in AUTORIZADAS:
    alertar "ADMINISTRACIÓN REMOTA NO AUTORIZADA"
```

> **La regla 1 es la que distingue este expediente y la que cuesta trabajo.**
> No se puede escribir sin una **lista de destinos de respaldo autorizados**,
> y esa lista no existe en la mayoría de las organizaciones porque nadie la ha
> necesitado nunca. **Construirla es el trabajo; la regla es la parte fácil.**
> Y conviene notar la asimetría: **el adversario usa exactamente las mismas
> herramientas que el equipo de operaciones**, de modo que la única variable
> discriminante es el destino.

## X-2. Mitigaciones

| # | Medida | Dónde | Efecto | Coste |
|---|---|---|---|---|
| **X-2.1** | **Inventario de administración remota autorizada + alerta sobre el resto** | Puesto · SOC | Común a los ocho actores del lote | Medio una vez |
| **X-2.2** | **Bloquear `finger` en el parque** | Puesto | Elimina una técnica de reconocimiento sin coste operativo | **Muy bajo** |
| **X-2.3** | **Lista de destinos de respaldo autorizados + bloqueo del resto en egreso** | Perímetro | **La medida específica de este actor.** Corta la etapa 06 | Medio |
| **X-2.4** | **Parchear concentradores de acceso remoto expuestos** | Perímetro | Corta la etapa 01 y **defiende contra varias marcas** | Medio |
| **X-2.5** | **Copias inmutables y verificadas** | Respaldo | Elimina la palanca del cifrado; no la de la publicación | Medio |
| **X-2.6** | **Segundo factor resistente a suplantación en acceso remoto** | Identidad | Cierra la vía de cuenta válida del conducto compartido | Medio |

---

## 14. Brechas de inteligencia y requisitos de colección

| # | Brecha | Impacto | Cómo se cierra | Prioridad |
|---|---|---|---|---|
| **G-1** | **No sabemos sobre qué fecha cuenta el ranking del sitio** | Heredada de `CTI-2026-046` `G-7`, y aquí es crítica: la divergencia es de ×8,3 | Pregunta al operador del rastreador o su documentación | **1** |
| **G-2** | **Sin ningún indicador de red, dominio o hash** | El informe no aporta nada ingerible salvo patrones | Informes de respuesta a incidentes; muestras | **1** |
| **G-3** | **El inventario de capacidades no está verificado** | `KJ-7` descansa en él | Muestras o análisis leído en original | 2 |
| **G-4** | **La tesis del código compartido con Lynx se leyó por referencia** | Sostiene `KJ-3`, que es el juicio estructural del informe | **Leer el análisis original** | **1** |
| **G-5** | **La cartera no tiene expediente de Lynx y este informe sostiene que no debe tenerlo aparte** | Si la decisión es errónea, hay un actor sin cubrir | Resolver `O-5` y, si son dos marcas de una operación, **añadir aquí una sección de Lynx en la versión 1.1** | **1** |
| **G-6** | **No sabemos por qué cayeron seis de sus ocho sitios** | `H-6`. Si fue acción policial, cambia el pronóstico | Vigilar anuncios oficiales; preguntar al rastreador por las fechas de baja | 2 |
| **G-7** | **Sin telemetría propia** | Estructural | Registros de flujo y de procesos | 2 |

**Disparadores de reevaluación.** `I-1`: otra tanda de más de veinte publicaciones en un día, que confirmaría el patrón de `E-2`. `I-2`: que Lynx deje de publicar mientras INC sigue, lo que apoyaría la lectura de sucesión invertida. `I-3`: aparición de un aviso gubernamental, que elevaría el grado de todo el informe. `I-4`: segunda víctima chilena. `I-5`: confirmación o refutación del conducto de acceso compartido. `I-6`: caída de los dos sitios activos restantes.

---

# ANEXOS

## Anexo A — Indicadores

### A.1 — Patrones de detección · **leer primero**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| pattern | **Egreso hacia un destino de respaldo o almacenamiento de objetos que no está en la lista de destinos autorizados** | **El indicador propio de este expediente.** Su inventario incluye **BackBlaze, Restic y `s5cmd`** además de RClone y MEGA: **usa las mismas herramientas que el equipo de operaciones**, de modo que **la única variable discriminante es el destino** | **Alta como señal; requiere la lista previa** | Sin caducidad | **Alerta** (`X-1.1`). **No automatizable sin la lista de destinos autorizados** |
| pattern | **Ejecución de `finger`** | **El indicador más específico y más barato del informe.** Protocolo de 1977 sin uso legítimo conocido en una red moderna. Coste de falso positivo mínimo | **Alta** | Sin caducidad | **Alerta directa**, y **bloqueo** del binario (`X-2.2`) |
| pattern | **`adfind.exe` ejecutado desde un equipo que no es puesto administrativo** | Enumeración de directorio, etapa 02 | Media-alta | Sin caducidad | Alerta |
| pattern | **Herramienta de administración remota presente y no inventariada** | Común a los ocho actores del lote. Aquí es **AnyDesk**, una sola | Alta como señal; requiere inventario | Sin caducidad | Alerta (`X-2.1`) |
| pattern | **Bitvise SSH Client en un servidor Windows corporativo** | Inusual en parque gestionado; túnel o transferencia cifrada | Media | Sin caducidad | Correlación |
| pattern | **Tanda de publicaciones en su sitio de filtración: más de veinte entradas en un día** | **No es un indicador de compromiso: es un indicador de inteligencia.** Señala vencimiento de plazos en bloque, y por tanto que hubo negociaciones fracasadas semanas antes | Alta | Sin caducidad como método | **Vigilancia** (`I-1`) |

### A.2 — Herramientas del inventario · ⚠ **NO BLOQUEAR LAS LEGÍTIMAS**

<!-- cti:note type="warn" -->

> ⚠ **Tres de sus siete herramientas de exfiltración son productos de respaldo
> o de almacenamiento de objetos**, y es muy probable que el equipo de
> operaciones use alguna. Van con tipo `herramienta` para que **no entren en
> los agregados planos**. **Bloquear Restic, `s5cmd` o BackBlaze puede romper
> el respaldo de la propia organización**, que es exactamente lo que no se
> quiere antes de un incidente de cifrado. La medida es `X-2.3`: controlar el
> **destino**.

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| herramienta | **BackBlaze · Restic · `s5cmd`** | **Productos de respaldo y almacenamiento de objetos usados para exfiltrar.** La peculiaridad de `KJ-7` | Alta como dato publicado | Sin caducidad | **NO bloquear.** Control por destino (`X-2.3`) |
| herramienta | **RClone · MEGA · 7-Zip · WinRAR** | Exfiltración y empaquetado. Comunes a casi todo el lote | Alta como dato | Sin caducidad | **NO bloquear.** Control por destino |
| herramienta | **AnyDesk** | Administración remota. **Una sola, frente a las seis de Akira** | Alta como dato | Sin caducidad | **Inventario y alerta contextual** |
| herramienta | **AdFind · Advanced IP Scanner · SoftPerfect NetScan** | Descubrimiento | Alta como dato | Sin caducidad | Detección por comportamiento |
| herramienta | **Bitvise SSH Client** | Túnel o transferencia | Alta como dato | Sin caducidad | Inventario |
| herramienta | **Mimikatz** | **La única inequívocamente ofensiva del inventario.** Su presencia en un puesto corporativo es anómala por sí misma | Alta como dato | Sin caducidad | **Alerta directa** |
| filename | **`finger.exe`** | **Protocolo heredado sin uso legítimo moderno.** Va como `filename` y **sí** es razonable bloquearlo: a diferencia de las demás, nada depende de él | Alta | Sin caducidad | **Bloqueo** (`X-2.2`) |

### A.3 — Victimología

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| cartera | **435 víctimas reclamadas en 2026 · 73 en 30 días (por publicación) · 7 u 58 en 7 días según la base** | La curva de `KJ-1`. **Reclamaciones, no brechas verificadas** | Alta como recuento | 60 días | **Medición, declarando siempre la base** |
| cartera | **50 entradas publicadas el 2026-11-12** | **El 11,5 % de su año en un día.** Corroborado por un recuento semanal independiente | **Alta** | Histórico | Análisis |
| cartera | **22 víctimas latinoamericanas (5,1 %): BR 9 · MX 6 · AR 3 · CL 1 · CR 1 · PA 1 · CO 1** | La exposición regional de `KJ-5`. Tercera del lote | Moderada | 60 días | Priorización |
| cartera | **Ocho sitios de filtración registrados, dos activos** | `KJ-2`. **Las direcciones no se transcriben**: caducan, y publicar una dirección de sitio de filtración no aporta defensa | Alta | Volátil | Vigilancia por marca |
| cartera | **Cero registros con cifra de rescate y cero con tamaño de datos declarado, de 435** | **El cero es informativo**: a diferencia de otros actores del lote, no publica magnitudes | Alta | — | — |
| cartera | **No se transcribe ningún nombre de víctima** | Decisión de higiene de la serie: son organizaciones atacadas, y nombrarlas amplifica la publicidad del extorsionador sin aportar defensa | — | — | No ingerir |

## Anexo B — Fuentes y valoración

| Fuente | Disciplina | Fiab. | Cred. | Grado | Notas |
|---|---|---|---|---|---|
| **`B-1` — Medición propia** sobre la interfaz pública del rastreador: 435 registros de 2026, dos bases de conteo, perfil diario de noviembre, países y sectores | OSINT técnico · **medición propia** | **B** | **2** | **Medición propia** | Base de `KJ-1`, `KJ-2`, `KJ-5` y `KJ-8`. Sesgos: fuente única; reclamaciones y no brechas; **y este actor publica en tandas**, lo que hace a toda métrica de ventana corta inestable por construcción |
| **`B-2` — Análisis industrial trimestral** (Dragos, 3.º trimestre de 2026) | OSINT comercial · **análisis sectorial** | **B** | **2** | Proveedor | Fuente de las reclamaciones industriales 50 → 58, de la explotación de **SonicWall SMA 1000**, y del **conducto de acceso compartido con confianza moderada declarada**. **Respetamos ese grado y no lo elevamos** (`KJ-6`). Sesgo: su foco es industrial, de modo que sus cifras no son del total |
| **`B-3` — Perfiles y recuentos de proveedor** (ProvenData, The Hacker News, NHIMG, Dexpose, SecurityArsenal) | OSINT comercial y prensa | **C** | **3** | Proveedor | Fuente de los recuentos acumulados —**991 al 9 de noviembre de 2026**, «más de 830 desde 2023» en junio—, del **~15 % de sanidad**, de las víctimas documentadas de sanidad pública y administración local, y de las **reglas de exclusión atribuidas a Lynx**. **Las cifras no son homogéneas y no se reconcilian** (`KJ-8`) |
| **`B-4` — Tesis del cambio de marca Lynx/INC** (Unit 42, por referencia) y **operador en los dos paneles** (SOCRadar, por referencia) | OSINT comercial, **leído por referencia** | **B** | **3** *(por la vía)* | Proveedor, por cita | **Sostiene `KJ-3`, que es el juicio estructural del informe, y no lo leímos en original.** La observación del operador conectado a los dos paneles es la evidencia más dura del conjunto precisamente porque es de infraestructura y no de código. Es `G-4` |
| **`B-5` — Recuento semanal de tercero** (Scrutex, semana del 9 al 15 de noviembre) | OSINT · compilación | **C** | **3** | Recuento | **Corrobora la tanda de `KJ-1` sin compartir método**: cincuenta publicaciones esa semana frente a una la anterior. Es la mejor corroboración independiente del informe |
| **`B-6` — Inventario de capacidades del rastreador** | OSINT · compilación técnica | **C** | **3** | Proveedor | 28 técnicas en 13 tácticas y las herramientas de `A.2`. **No verificado** (`G-3`) |

> **Lo que esta estructura de fuentes tiene de débil, dicho sin rodeos: el
> juicio más original del informe —que Lynx no es el sucesor de INC sino su
> marca hermana— descansa en una fuente leída por referencia** (`B-4`) **más
> una inferencia propia sobre datos de actividad** (`B-1`). La inferencia es
> sólida, porque la simultaneidad de publicaciones es un hecho verificable en
> los datos; pero el vínculo de código no lo leímos. **`G-4` es por eso
> prioridad 1**, al mismo nivel que la brecha de indicadores.

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

> **La regla que este informe añade al léxico, y es de aritmética antes que de
> estimación: una cifra de ventana temporal no es un dato hasta que se declara
> su base.**
>
> «INC Ransom tuvo 58 víctimas esta semana» y «INC Ransom tuvo 7 víctimas esta
> semana» son **las dos verdaderas**, difieren en un factor de 8,3, y la
> diferencia no es de estimación ni de confianza: **es de qué se cuenta**. Una
> cuenta publicaciones, la otra fechas de ataque declaradas por el adversario.
>
> **Por tanto, en esta serie, ninguna cifra de ventana corta se publica sola.**
> Y cuando se cita el número del ranking original, se cita como lo que es: el
> valor que el sitio mostraba a una hora concreta, cuya base **no conocemos**
> (`G-1`).

## Anexo D — Cómo evaluar la afirmación «B es el cambio de marca de A»

**El problema.** «Lynx es el cambio de marca de INC Ransom» es la clase de afirmación que circula sin discusión porque es útil: resume, ahorra un expediente y suena resuelta. **Y es caro equivocarse en las dos direcciones**: si son la misma operación y abrimos dos expedientes, duplicamos trabajo; si son dos y abrimos uno, dejamos un actor sin cubrir.

**La prueba que casi nadie hace y que resuelve la mayoría de los casos en cinco minutos:**

> **¿Publican las dos marcas víctimas en el mismo período?**

Si la respuesta es sí, **no es un cambio de marca**. Un cambio de marca implica abandono de la anterior; dos marcas publicando a la vez son dos marcas, con independencia de cuánto código compartan. En este caso la respuesta es sí, y por eso `KJ-3` reencuadra la afirmación en lugar de aceptarla.

**Los cinco criterios, en orden de poder discriminante:**

| # | Criterio | Qué indica |
|---|---|---|
| **1** | **¿Hay solapamiento temporal de publicaciones?** | **El criterio decisivo y el más barato.** Solapamiento ⇒ no es sucesión. Se comprueba con dos consultas a un rastreador |
| **2** | **¿Hay evidencia de infraestructura compartida o de un mismo operador en los dos paneles?** | **Es la evidencia más dura posible**, mejor que la comparación de código: el código se copia y se filtra, una sesión de operador no |
| **3** | **¿Comparten base de código?** | **Necesario y no suficiente.** Un cifrador filtrado produce decenas de marcas sin relación entre sí — es el error que `CTI-2026-035` documentó con cuatro cosas llamadas «Medusa» |
| **4** | **¿Declaran políticas distintas?** | **Si sí, y comparten código, las políticas son marketing** (`KJ-4`). Y es además un indicio de que la separación de marcas es deliberada y no accidental |
| **5** | **¿Divergen sus curvas de actividad?** | Curvas complementarias apuntan a reparto interno; curvas independientes, a operaciones distintas |

**Las cuatro clases que resultan:**

| Clase | Señales | Qué merece |
|---|---|---|
| **Sucesión** | Sin solapamiento temporal · código compartido | **Un expediente**, con la anterior como capítulo histórico |
| **Marcas hermanas** | **Solapamiento** · código compartido · políticas distintas | **Un expediente con dos secciones.** Es el caso de INC y Lynx |
| **Linaje sin relación operativa** | Código compartido por filtración · sin infraestructura común | **Dos expedientes.** El código común no es un vínculo |
| **Coincidencia de nombre** | Nada compartido salvo el nombre | **Desambiguación explícita**, como la de `CTI-2026-035` |

**Las tres advertencias de uso.**

1. **El criterio 1 sólo refuta la sucesión; no establece el vínculo.** Dos marcas que publican a la vez pueden ser dos operaciones sin ninguna relación. El vínculo lo dan los criterios 2 y 3.
2. **El criterio 3 es el que más se usa y el que menos vale.** La comparación de código es el instrumento favorito de los informes de proveedor porque es demostrable, y es precisamente el que produce más falsos vínculos: **un cifrador filtrado genera descendencia sin parentesco operativo.**
3. **Y el criterio 4 tiene un uso que va más allá de la taxonomía:** cuando una operación mantiene dos marcas y sólo una declara exclusiones éticas, **se puede medir el valor real de esas exclusiones mirando la victimología de la otra.** Es la contribución de `KJ-4` y se generaliza: **la forma de evaluar una lista de exclusiones no es leerla, es buscar la misma capacidad operando sin ella.**

## Anexo E — Marcos de referencia empleados

- **ICD 203**, con la adición del `Anexo C`: **una cifra de ventana temporal no es un dato hasta que se declara su base de conteo**, porque aquí las dos bases difieren en un factor de 8,3.
- **Código Admiralty/OTAN**, con el grado **medición propia** de `CTI-2026-044` y la degradación por vía de `B-4`, que sostiene el juicio estructural y se leyó por referencia.
- **MITRE ATT&CK v18** (`T-2`), con `T1567.002` como la técnica central del expediente: **tres de sus cinco herramientas de exfiltración a la nube son productos de respaldo**.
- **Pirámide del Dolor** (Bianco), en `T-3`, con el nivel «simple» —la dirección del sitio de filtración— marcado **explícitamente como inútil para este actor**: ocho abiertos, seis caídos.
- **ACH y pre-mortem** (`O-6`), con `H-4` —que el inventario menor indique menos sofisticación— **descartada como inferencia y consignada para que no se reabra**.
- **Evaluación de una afirmación de cambio de marca**, propio de este informe (`Anexo D`): cinco criterios, cuatro clases, y la prueba de cinco minutos del solapamiento temporal.
- **Lectura de listas de exclusión declaradas**, desarrollado en `KJ-4` y generalizado en la advertencia 3 del `Anexo D`, continuando lo que `CTI-2026-042` estableció.

## Anexo F — Paquete legible por máquina

Las tablas `cti:ioc` alimentan `ioc_index.csv`. **Seis advertencias:**

1. **⚠ Las herramientas de `A.2` llevan tipo `herramienta` y NO entran en los agregados planos.** Y aquí la advertencia es más aguda que en `CTI-2026-046`: **tres de ellas son productos de respaldo**, y bloquearlas puede romper el respaldo de la propia organización justo antes de un incidente de cifrado. La medida es el control por **destino** (`X-2.3`).
2. **`finger.exe` es la excepción y va como `filename`**: a diferencia de las demás, **nada legítimo depende de él en una red moderna**, y por eso sí es razonable bloquearlo.
3. **Toda cifra de ventana corta lleva su base de conteo.** `7` y `58` describen la misma semana. Extraer una sin la base produce una afirmación indeterminada (`Anexo C`).
4. **Los recuentos acumulados de las fuentes externas no se reconcilian y no se deben sumar**: 991, 830+, 200+ y 435 son cuatro métodos y cuatro fechas (`KJ-8`).
5. **Las direcciones de los sitios de filtración no se transcriben.** Ocho abiertos y seis caídos: una dirección aquí sería basura en semanas, y publicarla no aporta defensa.
6. **Y este informe no aporta ni una dirección IP, ni un dominio, ni un hash.** Es `G-2`, está declarado, y lo que aporta son **patrones, dos reglas de detección específicas y una decisión de encuadre** sobre Lynx.

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-11-19 | Emisión inicial, segunda de la serie `046`–`053`. Incluye: la **tanda del 12 de noviembre medida** —cincuenta entradas en un día, el 11,5 % de su año— y la **divergencia de ×8,3 entre las dos bases de conteo**, con corroboración independiente de un recuento semanal de tercero (`KJ-1`, `O-3`); la **rotación de infraestructura de publicación cuantificada**: ocho sitios abiertos y dos en pie (`KJ-2`); la **refutación de que Lynx sea el sucesor de INC** mediante el solapamiento temporal de publicaciones, y su reencuadre como marcas hermanas (`KJ-3`, `O-5`); la **contradicción entre las exclusiones declaradas de una marca y la victimología de la otra**, con la generalización de que una lista de exclusiones se evalúa buscando la misma capacidad operando sin ella (`KJ-4`, `E-3`); la **exposición regional con nombre de país** —22 latinoamericanas, Brasil 9, Chile 1— (`KJ-5`, `E-4`); la **peculiaridad de exfiltrar con herramientas de respaldo** y la regla de detección por destino que se sigue (`KJ-7`, `X-1`); **`finger` como el indicador más específico y barato del expediente**; las **cuatro cifras acumuladas incompatibles consignadas sin reconciliar** (`KJ-8`); y el método del `Anexo D` para evaluar una afirmación de cambio de marca | Célula CTI |

> **Nota sobre esta emisión.** Es el informe de la serie **con la brecha más
> incómoda**: su juicio más original —el reencuadre de Lynx— descansa en parte
> en una fuente que no leímos en original (`G-4`, prioridad 1). La parte que sí
> es nuestra, el solapamiento temporal de publicaciones, **es verificable por
> cualquiera con dos consultas al mismo rastreador**, y se publica precisamente
> para que se pueda atacar.

## Anexo H — Realimentación del consumidor

1. **¿Existe una lista de destinos de respaldo autorizados?** Es `X-2.3`, `H-1` y la decisión 2 de `E-5`. **Es la única medida de este informe específica de este actor**, y si no existe, **ésa es la conclusión del informe en esa organización**: su exfiltración será indistinguible de su respaldo.
2. **¿Se ha buscado `finger` en los registros de líneas de órdenes?** Es `H-2`, cuesta una consulta y el coste de falso positivo es casi nulo. **Es el mejor indicador por unidad de esfuerzo de los dos informes de la serie emitidos hasta ahora.**
3. **¿Se citó una cifra de siete días sin decir sobre qué fecha se cuenta?** Es el riesgo 1 del pre-mortem. **7 y 58 describen la misma semana.**
4. **¿Se abrió, o se piensa abrir, un expediente separado de Lynx?** Es `G-5`. Si son dos marcas de una operación —y `O-5` lo valora como probable— **ese expediente duplica trabajo y la detección ya está aquí**.
5. **¿Alguien usó las exclusiones declaradas de Lynx en un análisis de riesgo?** Es `KJ-4`. Una organización de salud que concluya que no es objetivo porque una marca excluye la sanidad **estará mirando la marca equivocada de la misma operación**.
6. **Si somos prestador de salud o administración pública: ¿se ha asumido que no hay exclusión?** ~15 % de sanidad, con un servicio de salud público y un ayuntamiento documentados.
7. **Si somos brasileños: ¿está este actor en el plan?** Nueve de sus veintidós víctimas regionales son brasileñas, y es su país regional principal.
8. **¿Puede alguien leer en original el análisis del vínculo de código con Lynx?** Es `G-4` y es prioridad 1. **Sostiene el juicio más original del informe y es lo único que no verificamos.**
9. **Y la pregunta de método:** el `Anexo D` sostiene que la comparación de código es el criterio más usado y el que menos vale para establecer un vínculo entre marcas, porque un cifrador filtrado genera descendencia sin parentesco. **¿Alguien tiene un caso en que el código compartido fuera el único indicio y resultara ser la misma operación?** Un contraejemplo así obligaría a reordenar los cinco criterios.

*Fin del informe `CTI-2026-047` v1.0.*
