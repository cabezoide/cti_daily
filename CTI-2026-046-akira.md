---
tlp: "TLP:CLEAR"
pap: "PAP:AMBER"
id: "CTI-2026-046"
version: "1.1"
tipo: "Perfil de operación de extorsión"
foco_regional: "Global · Latinoamérica"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "Akira · Akira_v2 · Megazord · (linaje discutido) Conti"
fecha: "2026-11-19"
caduca: "2027-02-19"
autor: "Célula CTI"
distribucion: "Elaborado con fuentes abiertas y con medición propia sobre la interfaz pública de consulta de un rastreador de sitios de filtración. No contiene telemetría de la organización emisora ni datos de terceros. Difusión libre, conservando la atribución de las fuentes y las salvedades de §3. Se mantiene PAP:AMBER: las herramientas del Anexo A.3 son legítimas y de uso administrativo normal, y no deben cargarse en bloqueo."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-046

## Akira recauda 245 millones de dólares y lleva cinco meses cayendo, y su exposición regional es la menor de todo este lote

### De ~50 víctimas al mes entre enero y junio de 2026 a ~29 entre julio y octubre: una caída del 43 % que el dinero acumulado no refleja

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-046` |
| Versión | 1.0 — 2026-11-19 |
| Clasificación | `TLP:CLEAR` · `PAP:AMBER` |
| Objeto | **Akira**, cuarta operación del año por volumen acumulado y **décima en la ventana de siete días** que motiva este lote. El contraste entre esas dos posiciones es el informe |
| Foco regional | **La exposición regional más baja de los ocho actores de este lote: 7 víctimas latinoamericanas de 420, el 1,7 %, y ninguna chilena** |
| Horizonte | Estratégico 6–12 meses · táctico días |
| Origen de los datos | **Medición propia** sobre 420 registros de víctimas de 2026 de un rastreador público, más el aviso conjunto de noviembre de 2025 y cuatro fuentes de proveedor |
| Lo que lo distingue en este lote | Es **el único de los ocho con un aviso gubernamental conjunto**, y el que tiene el inventario de herramientas más amplio: **48 técnicas en 13 tácticas y seis herramientas de administración remota distintas** |
| Caducidad | 2027-02-19 |
| Autor | Célula CTI |

<!-- cti:note type="warn" -->

> ⚠ **Tres cosas antes de leer.**
>
> 1. **Este informe pertenece a un lote de ocho** —`CTI-2026-046` a `053`—
>    construido sobre el top 10 de actividad de siete días de un rastreador
>    público. **Los ocho no son objetos comparables**: Akira tiene aviso
>    gubernamental y tres años de historia, mientras cuatro de los otros
>    aparecieron en las últimas seis semanas y uno **el día de emisión de este
>    informe**. La comparación se hace en `E-1` y el método de triaje es el del
>    `Anexo D` de `CTI-2026-042`.
> 2. **El 26 % de su victimología medida no tiene país asignado**: 109 de 420
>    registros. Cualquier proporción geográfica de este informe se calcula
>    sobre los 311 que sí lo tienen, y se dice en cada caso.
> 3. **Las cifras de dinero y de víctimas acumuladas no son nuestras ni son
>    homogéneas.** Los 244,17 millones de dólares son del aviso conjunto y
>    están fechados a finales de septiembre de **2025**; las de 1.400 víctimas
>    y ~245 millones son de proveedor y de 2026. **No se deben sumar ni
>    promediar.**

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** **Akira está en declive medido y sostenido, y ésa es la noticia que su cifra acumulada esconde.** Un proveedor sitúa su media mensual de reclamaciones en **unas 50 entre enero y junio de 2026 y unas 29 entre julio y octubre: una caída del 43 %**. Nuestra medición propia es consistente y la extiende hasta la fecha de emisión: **420 víctimas reclamadas en 2026, de las cuales sólo 42 en los últimos treinta días y 8 en los últimos siete**. Es decir, el 10 % de su año en el último mes. **Y Akira es, de los nueve actores que pudimos medir, el único en que las dos formas defendibles de contar una ventana de siete días —por fecha de publicación y por fecha de ataque declarada— dan el mismo número** (§O-3.1), lo que hace de su curva la más fiable del lote. Valoramos **muy probable** *(80–95 %)* que el declive sea real y no un artefacto de la ventana, porque **dos mediciones independientes con métodos distintos coinciden en la dirección y en el orden de magnitud**. **Confianza: alta.** *La lectura que importa:* Akira es **cuarta del año por volumen y décima en la semana**, y un programa que la priorice por su cifra acumulada estará defendiéndose del Akira de marzo.

**KJ-2.** **El declive es de actividad, no de capacidad, y confundir las dos cosas es el error que este informe quiere evitar.** El aviso conjunto de noviembre de 2025 le atribuía **244,17 millones de dólares en ingresos por extorsión a finales de septiembre de 2025**, y fuentes de proveedor de 2026 hablan de **más de 1.400 víctimas desde 2023 y unos 245 millones**. Su inventario de herramientas, tal como lo documenta el rastreador, es **el más amplio de los ocho actores de este lote: 48 técnicas repartidas en 13 tácticas**, con **seis productos de administración remota**, diez herramientas de descubrimiento y siete de evasión. Valoramos **casi con certeza** *(≥99 %)* que conserva la capacidad de operar al ritmo de principios de año si decide hacerlo. **Confianza: alta para el inventario, que es dato publicado; moderada para la inferencia de capacidad latente.**

**KJ-3.** **Y el hallazgo regional es un negativo, que conviene enunciar con precisión porque es útil: Akira apenas toca esta región, y en 2026 no tiene ninguna víctima chilena.** De 420 registros, **7 son latinoamericanos —el 1,7 %—**: tres mexicanos, tres brasileños y uno argentino. **Ninguno chileno.** Para contraste dentro del mismo conjunto de datos y la misma metodología: Qilin acumula **122 víctimas latinoamericanas (10,0 %)** y TheGentlemen **129 (12,6 %)**. Valoramos **probable** *(55–80 %)* que la baja exposición regional sea una propiedad estable de esta operación y no un hueco del rastreador, porque **el mismo rastreador sí detecta victimología regional abundante en otros actores**. **Confianza: moderada** — es una ausencia, y una ausencia medida con una sola fuente. *Consecuencia:* para una organización de la región, **Akira es el menos probable de los ocho**, y eso es información presupuestaria.

**KJ-4.** **Su cadena de intrusión está construida casi enteramente con software legítimo, y eso determina dónde hay que detectarla.** El inventario publicado incluye **seis herramientas de administración remota** —AnyDesk, MeshAgent, MobaXterm, Radmin, RustDesk, TeamViewer—, **diez de descubrimiento** —entre ellas Advanced IP Scanner, SoftPerfect NetScan, BloodHound, SharpHound, Masscan—, y seis de exfiltración —RClone, MEGA, FileZilla, WinSCP, WinRAR y un servicio público de ficheros temporales—. Valoramos **muy probable** *(80–95 %)* que la detección basada en firmas de malware sea estructuralmente insuficiente contra este actor. **Confianza: alta.** *Consecuencia operativa:* **el control de mayor rendimiento no es un antivirus, es un inventario de qué herramientas de administración remota están autorizadas en la organización y una alerta sobre las que no lo están** (`X-4.1`).

**KJ-5.** **Usa controladores vulnerables firmados para desactivar la seguridad, y los nombres están publicados.** El inventario de evasión incluye **el controlador de ThrottleStop, el de Zemana Anti-Rootkit, `churchill_driver.sys` / `fidget.sys`**, y además **carga lateral de bibliotecas en binarios legítimos firmados**: `icardagt.exe` con `version.dll`, `mfpmp.exe` con `rtworkq.dll`, y `consent.exe` con `msimg32.dll` y `wmsgapi.dll`. Valoramos **casi con certeza** *(≥99 %)* que estos artefactos estén publicados tal como se describen. **Confianza: alta como dato; no verificamos las muestras.** *Consecuencia:* **la lista de bloqueo de controladores vulnerables de Microsoft y la prohibición de carga de controladores no firmados por la organización son medidas concretas y dirigidas** (`X-4.3`), y la carga lateral se detecta por ruta, no por fichero.

**KJ-6.** **El aviso conjunto confirma una vía que importa a quien virtualiza: de una vulnerabilidad de concentrador de red a un hipervisor.** Se documenta la explotación de **`CVE-2024-40766`** —SonicWall— para alcanzar **un entorno Nutanix**. Valoramos **casi con certeza** *(≥99 %)* el hecho, por ser de fuente gubernamental. **Confianza: alta.** *Consecuencia:* es la misma doctrina que `CTI-2026-028` documentó para otro actor: **el hipervisor no suele tener agente, y el camino hasta él suele empezar en un dispositivo de borde sin parchear.**

**KJ-7.** **Hay una variante posterior y declarada, `Akira_v2`, y el aviso la añadió sin reclasificar la operación.** Valoramos **probable** *(55–80 %)* que esto indique evolución continua del cifrador bajo la misma marca, frente a la alternativa de un cambio de operador. **Confianza: moderada.** *Y conviene anotar la precaución del propio aviso:* **el vínculo con el linaje de Conti se trata como valoración analítica y no como hecho confirmado**, y este informe lo mantiene así (`O-5`).

**KJ-8.** **Sus afiliados trabajan también para otras marcas, lo que hace de «Akira» una etiqueta de herramienta y no de equipo.** Fuentes de proveedor describen afiliados de Akira operando además con otras operaciones de extorsión. Valoramos **probable** *(55–80 %)* el solapamiento de personal. **Confianza: moderada** — es afirmación de proveedor sin base técnica publicada. *Consecuencia defensiva, que es la de toda esta cartera:* **las TTP observadas en un incidente de Akira son transferibles a incidentes de otras marcas**, y por tanto la detección construida contra este actor rinde más allá de él.

---

## 2. Resumen ejecutivo

Akira es la cuarta operación de extorsión del año por volumen acumulado y la décima de la última semana. **Esa diferencia de seis puestos es todo el informe.**

Los números que circulan sobre ella son los de su historia: más de **1.400 víctimas desde 2023** y unos **245 millones de dólares** recaudados, de los cuales **244,17 millones** están confirmados por un aviso conjunto de varias agencias fechado a finales de septiembre de 2025. Son cifras grandes y son ciertas. Pero describen un pasado.

Lo que la medición de hoy dice es otra cosa: **420 víctimas reclamadas en 2026, de las cuales sólo 42 en los últimos treinta días y 8 en los últimos siete**. Un proveedor, con otra metodología, mide la misma curva: de unas cincuenta reclamaciones mensuales entre enero y junio a unas veintinueve entre julio y octubre, **una caída del 43 %**. Dos mediciones independientes coinciden en la dirección y en el orden de magnitud, de modo que **el declive es un hecho y no un accidente de la ventana**.

Conviene separar con cuidado dos cosas que ese dato invita a confundir. **Está cayendo la actividad, no la capacidad.** Su inventario de herramientas, tal como lo publica el rastreador, es el más amplio de los ocho actores de este lote: cuarenta y ocho técnicas en trece tácticas, con seis productos de administración remota, diez herramientas de descubrimiento y siete de evasión defensiva, entre ellas tres controladores vulnerables firmados y tres binarios legítimos usados para carga lateral de bibliotecas. Nada de eso se ha perdido porque haya publicado menos víctimas en octubre.

Para una organización de esta región hay además un dato que rara vez se puede dar con este signo: **Akira apenas nos toca.** De sus 420 víctimas de 2026, **siete son latinoamericanas —el 1,7 %— y ninguna es chilena**. El contraste, medido sobre el mismo conjunto de datos y con la misma metodología, es duro: Qilin acumula **122 víctimas latinoamericanas** y TheGentlemen **129**. Akira es, de los ocho actores de este lote, **el menos probable para nosotros**, y decirlo es tan útil como señalar un riesgo, porque la atención es un recurso finito.

Lo que sí se transfiere es su manera de trabajar. Esta operación entra por el borde de red —el aviso conjunto documenta la explotación de una vulnerabilidad de SonicWall para alcanzar **un entorno de virtualización Nutanix**— y luego se mueve con software que cualquier administrador reconocería: AnyDesk, TeamViewer, RustDesk, Advanced IP Scanner, RClone. **Contra eso un antivirus no sirve de mucho; un inventario de herramientas de administración remota autorizadas sí**, y es la recomendación central de este informe porque rinde contra los ocho actores del lote y no sólo contra éste.

---

## 3. Alcance y limitaciones

### 3.1 Qué cubre

La operación Akira: su curva de actividad medida, su victimología global y regional, su inventario de capacidades publicado, las vías de acceso inicial documentadas oficialmente, y el estado de la discusión sobre su linaje. Y su posición relativa dentro del lote de ocho actores que motiva esta serie.

### 3.2 Qué NO cubre

| Fuera de alcance | Por qué |
|---|---|
| **Análisis del cifrador** | No tenemos muestras. `Akira_v2` se consigna como variante declarada en el aviso, sin análisis propio |
| **Verificación de las cifras de dinero** | Los 244,17 millones son del aviso conjunto; los ~245 millones de 2026 son de proveedor. **No verificamos ninguna de las dos y no se deben sumar** |
| **La atribución del linaje a Conti** | El propio aviso la trata como valoración analítica. Este informe la mantiene en ese grado (`O-5`) y no la resuelve |
| **Los indicadores de red** | El rastreador no los publica y no leímos el aviso original en su anexo técnico. Es `G-2` |
| **La identidad de los afiliados** | Ninguna fuente la ofrece |

### 3.3 Limitaciones de la colección

<!-- cti:note type="warn" -->

> ⚠ **Cinco limitaciones.**
>
> 1. **Las cifras de víctimas son reclamaciones de un sitio de filtración, no
>    brechas verificadas.** El rastreador lo advierte y conviene repetirlo: un
>    sitio de filtración es publicidad del adversario.
> 2. **El 26 % de los registros no tiene país** —109 de 420—, de modo que toda
>    proporción geográfica se calcula sobre 311 y queda sujeta a que los 109
>    ausentes no estén sesgados. **No podemos descartar que lo estén.**
> 3. **Fuente única para la medición propia.** Un solo rastreador. La
>    corroboración externa existe para la tendencia, no para nuestras cifras.
> 4. **El inventario de capacidades es del rastreador y no lo verificamos.**
>    Que Akira use un controlador concreto o cargue una biblioteca en un
>    binario concreto son afirmaciones de un tercero sobre muestras que no
>    hemos visto (`G-3`).
> 5. **El aviso conjunto es de noviembre de 2025 y no localizamos ninguno
>    posterior.** Todo lo de 2026 es de proveedor o de prensa, y las cifras
>    discrepan entre fuentes.

### 3.4 Qué aporta

| Aporte | Dónde |
|---|---|
| **La curva de declive medida y corroborada por dos métodos**: 43 % de caída, y el 10 % del año en el último mes | `KJ-1`, `O-3` |
| **La separación explícita entre declive de actividad y pérdida de capacidad** | `KJ-2`, `E-2` |
| **La exposición regional cuantificada como la más baja del lote**, con cero víctimas chilenas, y el contraste con Qilin y TheGentlemen sobre los mismos datos | `KJ-3`, `E-3` |
| **La lectura del inventario como cadena casi íntegramente legítima**, con la consecuencia de detección que se sigue | `KJ-4`, `X-3` |
| **Los artefactos concretos de evasión**: tres controladores y tres binarios de carga lateral | `KJ-5`, `A.2` |
| **La posición relativa dentro del lote de ocho**, que es lo que permite priorizar | `E-1` |

### 3.5 Veredicto

<!-- cti:table highlight="CORROBORADO|NO SOSTENIDO|propio" -->

| # | Elemento | Veredicto | Base |
|---|---|---|---|
| 1 | Akira está entre los actores de extorsión más activos | **CORROBORADO con matiz decisivo** | Cuarta del año, **décima de la semana** (`KJ-1`) |
| 2 | Su actividad crece | **NO SOSTENIDO** | **Cae un 43 %** en media mensual, por dos mediciones independientes |
| 3 | Es una amenaza relevante para la región | **NO SOSTENIDO** | **1,7 % de víctimas latinoamericanas y ninguna chilena** (`KJ-3`) |
| 4 | Ha perdido capacidad | **NO SOSTENIDO** | 48 técnicas, 6 herramientas de administración remota, aviso conjunto (`KJ-2`) |
| 5 | Se detecta con firmas de malware | **NO SOSTENIDO** | La cadena es casi toda software legítimo (`KJ-4`) |
| 6 | Alcanza entornos de virtualización | **CORROBORADO oficialmente** | `CVE-2024-40766` → entorno Nutanix, en el aviso conjunto (`KJ-6`) |
| 7 | Es una derivación de Conti | **SIN RESOLVER** | El propio aviso lo trata como valoración analítica, no como hecho (`O-5`) |
| 8 | «Akira» identifica un equipo estable | **NO SOSTENIDO** | Afiliados compartidos con otras marcas (`KJ-8`) |

---

# NIVEL ESTRATÉGICO
### Para: CISO, Riesgo, Arquitectura · Horizonte: 6–12 meses

## E-1. Dónde encaja Akira en el lote de ocho, y por qué la comparación es el aporte

Este informe abre una serie de ocho construida sobre el top 10 de actividad de siete días de un rastreador público, excluidos los dos actores que esta cartera ya tenía. **Los ocho no son comparables, y tratarlos como si lo fueran sería el error que `CTI-2026-042` documentó.** Aplicando los criterios de su `Anexo D`:

<!-- cti:table highlight="Akira|INC Ransom|sembrado" -->

| Actor | En el rastreador desde | Técnicas documentadas | Herramientas | Aviso oficial | Clase |
|---|---|---|---|---|---|
| **Akira** | **2023-04-26** | **48 en 13 tácticas** | **Inventario completo** | **Sí, conjunto** | **Marca con operación** |
| **INC Ransom** | **2023-08-09** | **28 en 13 tácticas** | Inventario completo | No localizado | **Marca con operación** |
| settra | 2026-06-28 | Ninguna | Sólo Rclone | No | Marca en formación |
| n0n | 2026-09-18 | 11 en 8 tácticas | Ninguna | No | **Reclamación en volumen** |
| pixelleaks | 2026-11-03 | Ninguna | Ninguna | No | Sitio reciente |
| vortex | 2026-11-10 | Ninguna | Ninguna | No | Sitio reciente |
| curious worm | 2026-11-11 | Ninguna | Ninguna | No | Sitio reciente |
| soulgroup | **2026-11-19** *(el día de emisión)* | Ninguna | Ninguna | No | **Sitio sembrado** |

**La tabla dice algo que el ranking de siete días oculta: cinco de los ocho no existían hace seis semanas.** Akira e INC Ransom son los dos únicos con historia, inventario y —en el caso de Akira— aviso gubernamental. **El ranking mide publicaciones, no operaciones**, y una tanda de veintiséis entradas publicadas en seis minutos cuenta igual que veintiséis intrusiones.

> **Y de ahí la primera decisión que este lote pide al nivel estratégico:** la
> atención debe repartirse **de forma desigual y explícita**. Akira e INC
> Ransom merecen detección; los cuatro sitios de noviembre merecen vigilancia
> y una línea en una lista. **Repartir por igual es el error más caro de los
> dos posibles.**

## E-2. Declive de actividad frente a pérdida de capacidad

<!-- cti:chart title="Actividad de Akira en 2026 (medición propia, 420 registros)" cap="La ventana de siete días que motiva este lote la sitúa décima. El año la sitúa cuarta. Fuente: medición propia sobre rastreador público, 2026-11-19." -->

| Ventana | Víctimas reclamadas |
|---|---|
| `Año 2026` | 420 |
| `Últimos 30 d` | 42 |
| `Últimos 7 d` | 8 |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `420` | Víctimas reclamadas en 2026 | Cuarta del lote, tras Qilin (1.221), TheGentlemen (1.020) e INC Ransom (435) |
| `−43 %` | Caída de la media mensual de reclamaciones | ~50/mes (ene–jun) → ~29/mes (jul–oct), según proveedor |
| `10 %` | Proporción de su año concentrada en los últimos 30 días | Medición propia |
| `8 = 8` | Víctimas de 7 días por publicación y por fecha de ataque | **Las dos bases coinciden. Es el único de los nueve medidos** (§O-3.1) |
| `244,17 M$` | Ingresos por extorsión según el aviso conjunto | **Fechado a finales de septiembre de 2025** |
| `+1.400` | Víctimas desde 2023, según proveedor | **No verificado, y de otra metodología** |
| `48` | Técnicas documentadas en 13 tácticas | **El inventario más amplio de los ocho** |
| `6` | Productos de administración remota en su inventario | AnyDesk · MeshAgent · MobaXterm · Radmin · RustDesk · TeamViewer |
| `1,7 %` | Víctimas latinoamericanas | **7 de 420. Ninguna chilena** |

**La distinción, enunciada para que no se colapse.** «Akira está cayendo» es un juicio sobre **publicaciones observadas**, y está bien soportado. «Akira es menos peligrosa» es un juicio sobre **capacidad**, y no se sigue del anterior. Las publicaciones de un sitio de filtración son función de tres cosas: cuántas víctimas hubo, **cuántas pagaron** —las que pagan no se publican— y cuánto quiere publicar el operador. Una caída del 43 % es compatible con menos intrusiones, con **más pagos**, o con una decisión de perfil bajo.

> **Lo que sí se puede afirmar, y es lo accionable:** el inventario de 48
> técnicas no se ha reducido, el dinero acumulado le da margen operativo, y la
> vía de acceso que el aviso documenta —un dispositivo de borde sin
> parchear— **sigue abierta en cualquier organización que no haya parcheado**.
> El declive es una ventana de respiro, no un cambio de postura defensiva.

## E-3. Exposición regional: el negativo más claro de este lote

| Actor del lote | Víctimas 2026 | Latinoamericanas | % | Chilenas |
|---|---|---|---|---|
| Qilin *(ya en cartera)* | 1.221 | **122** | **10,0 %** | **20** |
| TheGentlemen *(ya en cartera)* | 1.020 | **129** | **12,6 %** | **9** |
| INC Ransom | 435 | 22 | 5,1 % | 1 |
| **Akira** | **420** | **7** | **1,7 %** | **0** |
| n0n | 259 | 11 | 4,2 % | 0 |
| settra | 116 | 5 | 4,3 % | 0 |
| vortex | 35 | 0 | 0,0 % | 0 |
| pixelleaks | 34 | 3 | 8,8 % | 0 |
| curious worm | 18 | 0 | 0,0 % | 0 |

**Todas las filas salen del mismo conjunto de datos, el mismo día y con la misma metodología**, que es lo que hace la comparación utilizable. Y dice dos cosas.

La primera, sobre Akira: **1,7 % y cero víctimas chilenas en 420 registros.** Con el 26 % de registros sin país, el intervalo real podría ser algo mayor, pero no de un orden distinto.

La segunda, y es la que conviene llevarse: **los dos actores que esta cartera ya tenía documentados son, con mucha diferencia, los dos de mayor exposición regional del top 10**. Eso valida retrospectivamente la elección de `CTI-2026-014` y `CTI-2026-015` como expedientes, y es la razón por la que este lote cierra actualizándolos con estas cifras.

## E-4. Decisiones que este informe pide

| # | Decisión | A quién | Coste | Por qué |
|---|---|---|---|---|
| **1** | **Inventariar qué herramientas de administración remota están autorizadas, y alertar sobre cualquier otra** | TI · SOC | **Medio una vez, bajo después** | `KJ-4`: seis productos distintos en su inventario. **Es la medida que rinde contra los ocho actores del lote** |
| **2** | **Aplicar la lista de bloqueo de controladores vulnerables y prohibir la carga de controladores no firmados por la organización** | Ingeniería de puesto | Medio | `KJ-5`: tres controladores nombrados |
| **3** | **Parchear el borde de red con prioridad sobre el parcheo interno** | Operaciones | Medio | `KJ-6`: de SonicWall a un hipervisor Nutanix, oficialmente documentado |
| **4** | **No priorizar Akira por su cifra acumulada** | CTI | Cero | Cuarta del año, décima de la semana, 1,7 % regional |
| **5** | **Tratar las TTP de este expediente como transferibles a otras marcas** | SOC | Cero | `KJ-8`: afiliados compartidos |
| **6** | **Vigilar una reaceleración**, no una desaparición | CTI | Bajo | El declive es de actividad; la capacidad está intacta (`E-2`) |

---

# NIVEL OPERACIONAL
### Para: SOC, Respuesta a incidentes, Threat Hunting · Horizonte: semanas

## O-1. Identificación

| Campo | Valor |
|---|---|
| Nombre | **Akira** |
| Variantes declaradas | **`Akira_v2`**, añadida en la actualización del aviso conjunto de noviembre de 2025 · `Megazord` se le asocia en fuentes de proveedor |
| Primera observación | Marzo–abril de 2023 según fuentes; en el rastreador desde **2023-04-26** |
| Sitios de filtración | **Dos, los dos activos** al 19-11-2026 |
| Linaje | **Discutido.** Se le atribuye relación con el linaje de Conti, y el aviso conjunto **lo trata como valoración analítica y no como hecho** (`O-5`) |
| Modelo | Doble extorsión. Afiliados que **operan también con otras marcas** (`KJ-8`) |
| Estado | **Activa y en declive medido**: 11 víctimas en los últimos 7 días frente a una media de ~50 mensuales en el primer semestre |

## O-2. El inventario de capacidades, leído por lo que implica

Lo que el rastreador publica —y que es la base de `KJ-4` y `KJ-5`— agrupado por lo que cada bloque obliga a hacer:

| Bloque | Herramientas documentadas | Qué obliga |
|---|---|---|
| **Administración remota** | AnyDesk · MeshAgent · MobaXterm · Radmin · RustDesk · TeamViewer | **Inventario de lo autorizado + alerta sobre lo demás.** Ninguna de las seis es maliciosa: la señal es *presencia no autorizada*, no *existencia* |
| **Descubrimiento** | Advanced IP Scanner · Advanced Port Scanner · BloodHound · SharpHound · Masscan · ReconFTW · ShareFinder · SharpShares · SoftPerfect NetScan · ldapdomaindump | **Detección por comportamiento**: consultas LDAP masivas, barrido de puertos interno, enumeración de recursos compartidos |
| **Robo de credenciales** | DonPAPI · LaZagne · Mimikatz | Protección de LSASS, y vigilancia del acceso a la bóveda de credenciales de Windows |
| **Evasión defensiva** | PowerTool · controlador de ThrottleStop · controlador de Zemana Anti-Rootkit · `churchill_driver.sys` / `fidget.sys` · carga lateral en `consent.exe`, `icardagt.exe` y `mfpmp.exe` | **Lista de bloqueo de controladores + detección de carga lateral por ruta** (`X-4.3`) |
| **Exfiltración** | RClone · MEGA · FileZilla · WinSCP · WinRAR · servicio público de ficheros temporales | **Control de egreso por destino**, no por fichero |
| **Túnel y red** | Cloudflared · Ngrok · OpenSSH | **Detección de túneles salientes**, que es la señal más limpia de este bloque |
| **Ofensiva** | CrackMapExec · Impacket · NetExec | Autenticación anómala entre equipos |
| **LOLBAS** | `net` · `netsh` · `nltest` · `vssadmin` | **`vssadmin` es la señal de oro**: borrado de copias de sombra inmediatamente antes del cifrado |

> **La lectura de conjunto, y es la razón de que `KJ-4` esté redactado como
> está:** de las ocho filas, **seis están formadas íntegramente por software
> legítimo o de código abierto**. No hay nada que un antivirus deba bloquear
> por sí mismo, porque bloquear AnyDesk o RClone rompería el trabajo de
> alguien. **La detección tiene que ser contextual —quién, dónde y cuándo— y
> eso se construye con un inventario, no con una firma.**

## O-3. La curva de actividad medida

| Ventana | Víctimas | Lectura |
|---|---|---|
| **Año 2026** | **420** | Cuarta del lote |
| Últimos 30 días | **42** | **El 10 % del año en el último mes** |
| Últimos 7 días | **8** | **Décima del top 10** que motiva este lote. **Ocho por las dos bases de conteo**: es el único actor del lote en que coinciden (§O-3.1) |
| Primer registro de 2026 | 2026-01-05 | |
| Último registro | 2026-11-18 | **Activa al cierre** |
| Países distintos | **23** | Sobre los 311 registros con país asignado |
| Sin país asignado | **109 de 420 (26 %)** | `G-1` |

### O-3.1 Las dos formas de contar una ventana de siete días, y por qué importa

Al medir el lote apareció un problema de método que afecta a los ocho informes de la serie y que conviene exponer aquí, porque **Akira es el caso en que no se manifiesta** y eso la hace útil como control.

Un registro de víctima en este rastreador tiene **dos fechas**: la de **publicación** en el sitio de filtración —cuándo el rastreador lo vio— y la de **ataque declarada** —cuándo el adversario dice que ocurrió—. Una ventana de siete días se puede contar sobre cualquiera de las dos, y **las dos son defendibles**: la primera mide actividad de publicación, la segunda mide actividad de intrusión según el adversario.

**Para la mayoría de los actores del lote las dos cuentas difieren, y mucho:**

| Actor | 7 días por **fecha de ataque** | 7 días por **publicación** | Divergencia | Entradas con las dos fechas iguales |
|---|---|---|---|---|
| **Akira** | **8** | **8** | **ninguna** | 66 % |
| INC Ransom | **7** | **58** | **×8,3** | 57 % |
| n0n | 39 | **104** | ×2,7 | 53 % |
| TheGentlemen | 19 | 41 | ×2,2 | 41 % |
| vortex | 19 | 21 | ×1,1 | 63 % |
| qilin | 24 | 24 | ninguna | 93 % |
| pixelleaks | 31 | 31 | ninguna | **100 %** |
| curious worm | 9 | 9 | ninguna | **100 %** |
| settra | **0** | 10 | — | **0 %** |

**Tres cosas que esta tabla establece, y una que no.**

Establece, primero, que **la divergencia puede llegar a ser de un factor de ocho**: INC Ransom publicó **cincuenta entradas en un solo día, el 12 de noviembre de 2026**, con fechas de ataque repartidas por semanas anteriores. Contado por publicación es el actor más activo de la semana; contado por fecha de ataque es casi inactivo. **Las dos lecturas son correctas y describen cosas distintas.**

Establece, segundo, que **hay dos prácticas opuestas y consistentes en el uso de la fecha de ataque**. `settra` declara una fecha de ataque distinta de la de publicación en **el 100 % de sus entradas**; `pixelleaks` y `curious worm`, en **ninguna**. Una operación que fecha sus intrusiones está aportando un dato comprobable contra la víctima; una que publica todo con fecha del día no aporta ninguno —o el rastreador le asigna la fecha de publicación por omisión, que para el lector tiene el mismo efecto—.

Y establece, tercero, que **Akira es el control del lote**: sus dos cuentas coinciden, de modo que su curva de `O-3` no depende de qué base se elija. Por eso el declive de `KJ-1` es el juicio mejor soportado de toda la serie.

**Lo que esta tabla NO establece es cuál de las dos bases usa el ranking del sitio.** Para Akira el ranking dice 8 y las dos bases dicen 8; para INC Ransom dice 9 y las bases dicen 7 y 58; para `n0n` dice 104 y las bases dicen 39 y 104. **Los números del ranking se parecen a una base para unos actores y a la otra para otros**, y la diferencia puede deberse al momento exacto de captura y al corte de la ventana. **No lo podemos determinar desde fuera, y por tanto este informe no afirma cuál es** (`G-7`).

> **La consecuencia de método, que se aplica a los siete informes siguientes:**
> **ninguna cifra de ventana corta de esta serie se publica sin decir sobre qué
> fecha se cuenta.** Y cuando una cifra del ranking original se cite, se cita
> como lo que es —el número que el sitio mostraba a una hora concreta— y no
> como una medición propia.

**Reparto sectorial** *(sobre los 420 registros)*: **Manufactura 124**, Servicios profesionales 81, Comercio minorista 38. Es el perfil habitual de la extorsión de volumen, sin exclusiones declaradas.

**Reparto geográfico** *(sobre los 311 con país)*: Estados Unidos 207, Alemania 21, Canadá 15, Reino Unido 13, Suiza 12. **Es una operación de objetivo anglosajón y europeo occidental**, y eso explica por sí solo el `KJ-3`.

## O-4. Nuestra exposición

| Si la organización… | Exposición a Akira | Medida |
|---|---|---|
| **Opera sólo en Latinoamérica** | **Baja.** 1,7 % de su victimología, cero víctimas chilenas | No desatender: la vía de acceso es genérica |
| **Tiene filiales o matriz en EE. UU., Alemania, Canadá, Reino Unido o Suiza** | **Media-alta.** Ahí está el 87 % de su victimología con país | Parcheo de borde (`E-4.3`) |
| **Es de manufactura** | **Media-alta.** Su sector principal, 124 de 420 | Igual |
| **Tiene concentradores de red o cortafuegos sin parchear expuestos** | **Alta, independientemente de la geografía** | `CVE-2024-40766` y la clase entera de vulnerabilidades de borde |
| **Virtualiza con hipervisores sin agente de seguridad** | **Alta si se alcanza la red de gestión** | Segmentación de la red de gestión del hipervisor |

## O-5. El linaje, y por qué este informe no lo resuelve

Lo que hay: fuentes de proveedor que relacionan a Akira con el linaje de Conti, apoyadas en que tras el cierre de Conti varios afiliados migraron a operaciones independientes. Lo que **no** hay: una base técnica publicada que lo establezca.

**Y el dato que más pesa es la cautela de la fuente con más autoridad:** el aviso conjunto **describe esos vínculos como valoraciones analíticas y no como hecho confirmado**. Valoramos **aproximadamente igual de probable** *(40–60 %)* que exista continuidad de personal con el linaje de Conti, con **confianza baja**.

> **Y conviene decir por qué da igual para la defensa.** La pregunta del
> linaje importa para la atribución y para la acción policial. **Para el
> defensor, lo que determina la respuesta es el inventario de `O-2`, y ése
> está documentado con independencia de quién fuera antes.** Es la misma
> conclusión que `CTI-2026-030` sacó de una disputa de alias: **saber de quién
> deriva un actor no cambia ni una regla de detección.**

## O-6. Hipótesis alternativas y pre-mortem

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| **H-1 — El declive es real** | **Retenida como principal.** Dos mediciones independientes, métodos distintos, misma dirección y magnitud | `Muy probable · 80–95 %` |
| **H-2 — El declive refleja más pagos, no menos ataques** | **Retenida y no refutable con estos datos.** Un sitio de filtración publica a quien **no** paga: una caída es compatible con una tasa de pago mayor. **Es la hipótesis más incómoda de este informe y no se puede descartar** | `Posibilidad real · 40–60 %` |
| **H-3 — La baja exposición regional es un hueco del rastreador** | **Rebajada.** El mismo rastreador detecta 122 víctimas regionales de Qilin y 129 de TheGentlemen, de modo que su cobertura regional existe | `Poco probable · 20–45 %` |
| **H-4 — El 26 % sin país está sesgado hacia la región** | **Retenida como limitación.** Si los 109 registros sin país fueran desproporcionadamente latinoamericanos, `KJ-3` se debilitaría. No hay forma de comprobarlo con estos datos | `Poco probable · 20–45 %` |
| **H-5 — «Akira» es un equipo estable** | **Poco probable.** Afiliados compartidos con otras marcas (`KJ-8`) | `Poco probable · 20–45 %` |
| **H-6 — Hay un sucesor ya operando bajo otro nombre** | **Sin evidencia, y se consigna porque es el patrón de la cartera.** `CTI-2026-040` y `042` documentan cuatro casos en que la marca se apaga y la capacidad sigue. **Aquí no hay ningún indicio**, pero es lo que habría que buscar | `Aprox. igual de probable · 40–60 %` |

**Pre-mortem — si este informe se equivoca, será porque:**

1. **Se leyó «está cayendo» como «es menos peligrosa»** (`E-2`). Riesgo 1.
2. **Se leyó el 1,7 % regional como «no nos puede pasar»**: siete organizaciones latinoamericanas sí lo sufrieron.
3. **El declive era una tasa de pago mayor y no menos ataques** (`H-2`).
4. **Los 109 registros sin país ocultaban victimología regional** (`H-4`).
5. **Se esperó una desaparición** en lugar de una reaceleración.
6. **Se intentó bloquear las herramientas de `O-2`** en lugar de inventariarlas, rompiendo operaciones legítimas.

---

# NIVEL TÁCTICO
### Para: Analistas de SOC e ingeniería de detección · Horizonte: días

## T-1. Cadena de intrusión reconstruida

<!-- cti:stages title="De un dispositivo de borde al hipervisor" dwell="next" -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 01 · Acceso | Borde de red sin parchear | **`CVE-2024-40766` (SonicWall), documentada oficialmente** · clase entera de vulnerabilidades de concentrador y cortafuegos · **primera oportunidad: parcheo de borde** |
| Etapa 02 · Reconocimiento | Mapa del dominio | BloodHound · SharpHound · `ldapdomaindump` · Advanced IP Scanner · SoftPerfect NetScan · **segunda oportunidad: consultas LDAP masivas desde un puesto** |
| Etapa 03 · Credenciales | Escalada | Mimikatz · LaZagne · DonPAPI · `nltest` |
| Etapa 04 · Persistencia | Administración remota | Hasta **seis productos distintos** · **tercera oportunidad: herramienta de administración remota no autorizada** |
| Etapa 05 · Evasión | Desactivar la seguridad | **Controlador vulnerable firmado** · **carga lateral en binario legítimo** · PowerTool |
| Etapa 06 · Exfiltración | Robo antes del cifrado | RClone · MEGA · WinSCP · FileZilla · **cuarta oportunidad: egreso a destinos de almacenamiento no corporativos** |
| Etapa 07 · Impacto | Cifrado | `vssadmin` para borrar copias de sombra · **la última señal, y llega tarde** · alcance a **hipervisor** si la red de gestión no está segmentada |

**Las cuatro oportunidades señaladas son las que esta cartera considera accionables**, y están en orden de coste creciente y de valor decreciente: **cuanto más temprana, más barata y más útil.**

## T-2. Mapa MITRE ATT&CK

<!-- cti:matrix -->

| Táctica | ID | Técnica | Procedimiento documentado |
|---|---|---|---|
| Acceso inicial | T1190 | Exploit Public-Facing Application | **`CVE-2024-40766`** (SonicWall), en el aviso conjunto |
| Acceso inicial | T1133 | External Remote Services | Concentradores de red como punto de entrada |
| Descubrimiento | T1087.002 | Account Discovery: Domain Account | BloodHound · SharpHound · `ldapdomaindump` |
| Descubrimiento | T1046 | Network Service Discovery | Advanced IP/Port Scanner · Masscan · SoftPerfect NetScan |
| Descubrimiento | T1135 | Network Share Discovery | ShareFinder · SharpShares |
| Credenciales | T1003.001 | OS Credential Dumping: LSASS Memory | Mimikatz |
| Credenciales | T1555 | Credentials from Password Stores | LaZagne · DonPAPI |
| Evasión | **T1562.001** | **Impair Defenses: Disable or Modify Tools** | PowerTool |
| Evasión | **T1068** | **Exploitation for Privilege Escalation (BYOVD)** | Controladores de ThrottleStop y Zemana · `churchill_driver.sys` / `fidget.sys` |
| Evasión | **T1574.002** | **Hijack Execution Flow: DLL Side-Loading** | `icardagt.exe`+`version.dll` · `mfpmp.exe`+`rtworkq.dll` · `consent.exe`+`msimg32.dll`/`wmsgapi.dll` |
| Movimiento lateral | T1021.001 | Remote Services: RDP | — |
| Movimiento lateral | T1021.002 | SMB/Windows Admin Shares | Impacket · CrackMapExec · NetExec |
| Mando y control | T1572 | Protocol Tunneling | **Cloudflared · Ngrok · OpenSSH** |
| Mando y control | T1219 | Remote Access Software | **Seis productos** (`O-2`) |
| Exfiltración | T1567.002 | Exfiltration to Cloud Storage | MEGA · RClone · servicio de ficheros temporales |
| Impacto | **T1490** | **Inhibit System Recovery** | **`vssadmin`** |
| Impacto | T1486 | Data Encrypted for Impact | Akira / `Akira_v2` |

## T-3. Pirámide del Dolor

<!-- cti:pyramid -->

| Nivel | Indicador | Valor para Akira |
|---|---|---|
| Trivial | Hash | **Nulo para nosotros.** Sin muestras (`G-3`) |
| Fácil | Direcciones IP | **Nulo.** El rastreador no las publica (`G-2`) |
| Simple | Dominios | Nulo |
| **Molesto** | **Controladores vulnerables nombrados** | **Alto y accionable**: tres nombres concretos, y la medida es una lista de bloqueo que ya existe |
| **Molesto** | **Rutas de carga lateral** | **Alto**: tres pares binario-biblioteca. Se detecta por **ruta de carga**, no por fichero |
| **Irritante** | **Inventario de herramientas** | **El nivel donde está todo el valor de este expediente.** Seis productos de administración remota y diez de descubrimiento: **se defiende con inventario, no con firmas** |
| Difícil | TTP | **Borde sin parchear → descubrimiento → administración remota → exfiltración → cifrado.** No cambia por bloquear nada, y es común a casi todo el lote |

## T-4. Hipótesis de caza

<!-- cti:accordion critical="^(H-1|H-2)\b" regional="^(H-6)\b" -->

| # | Hipótesis | Cómo se comprueba | Qué significa un positivo |
|---|---|---|---|
| **H-1** | **Hay una herramienta de administración remota no autorizada instalada** | Inventario de software frente a lista de autorizadas; y procesos de los seis nombres de `O-2` | **La caza de mayor rendimiento del informe, y sirve contra los ocho actores del lote.** Un positivo no es necesariamente Akira: es un hallazgo en cualquier caso |
| **H-2** | **Se cargó un controlador vulnerable firmado** | Eventos de carga de controlador; buscar los tres nombres de `KJ-5` | Evasión en curso o ya ejecutada. **Incidente de prioridad máxima** |
| **H-3** | **Hubo carga lateral en `consent.exe`, `icardagt.exe` o `mfpmp.exe`** | Bibliotecas cargadas desde rutas no estándar por esos tres binarios | Igual |
| **H-4** | **Consultas LDAP masivas desde un puesto que no es administrativo** | Registro del controlador de dominio | Reconocimiento de dominio en curso (etapa 02) |
| **H-5** | **Túnel saliente por Cloudflared, Ngrok u OpenSSH desde un servidor** | Flujo de salida y procesos | Canal de control establecido |
| **H-6** | **Nuestros prefijos o nuestro dominio aparecen en su sitio de filtración** | Consulta al rastreador filtrando por nuestro nombre y país | Reclamación pública. **Con 1,7 % regional es poco probable, y la comprobación es gratuita** |
| **H-7** | **Hay un dispositivo de borde sin parchear expuesto** | Barrido propio del perímetro | La etapa 01, y es anterior a todo lo demás |
| **H-8** | **La red de gestión del hipervisor es alcanzable desde la red de usuarios** | Prueba de alcance | `KJ-6`: es el camino que el aviso documenta |

## T-5. Brechas de visibilidad

| # | Brecha | Por qué duele | Cómo se cierra |
|---|---|---|---|
| **V-1** | **Sin inventario de herramientas de administración remota autorizadas** | Hace inejecutable `H-1`, que es la caza principal | Inventario + política |
| **V-2** | Sin registro de carga de controladores | `H-2` y `H-3` | Auditoría de integridad de código |
| **V-3** | Sin registro de consultas LDAP del controlador de dominio | `H-4` | Auditoría de directorio |
| **V-4** | Sin control de egreso por destino | Etapa 06 | Lista de destinos de almacenamiento permitidos |
| **V-5** | Red de gestión del hipervisor no segmentada | `KJ-6` | Segmentación |

---

# NIVEL TÉCNICO
### Para: Ingeniería de detección · Vida útil: semanas

## X-1. Lógica de detección

```
# ---- 1. Administración remota no autorizada (la regla de mayor rendimiento) ----
AUTORIZADAS = { ... la lista de la organización, explícita ... }
SOSPECHOSAS = { anydesk, meshagent, mobaxterm, radmin, rustdesk, teamviewer,
                screenconnect, netsupport, atera, splashtop, ... }
si proceso.nombre in SOSPECHOSAS y proceso.nombre not in AUTORIZADAS:
    alertar "ADMINISTRACIÓN REMOTA NO AUTORIZADA"   # severidad alta
    # Nota: la lista de sospechosas NO es una lista de malware.
    # La señal es la ausencia en AUTORIZADAS, no la presencia en SOSPECHOSAS.

# ---- 2. Controlador vulnerable (BYOVD) ----
si evento == carga_de_controlador y (
       controlador.nombre in {churchill_driver.sys, fidget.sys}
    or controlador.firmante in {ThrottleStop, Zemana}
    or controlador in lista_bloqueo_microsoft):
    alertar "CONTROLADOR VULNERABLE CARGADO"        # severidad máxima

# ---- 3. Carga lateral en binario legítimo ----
PARES = { consent.exe:  [msimg32.dll, wmsgapi.dll],
          icardagt.exe: [version.dll],
          mfpmp.exe:    [rtworkq.dll] }
si proceso.nombre in PARES y biblioteca_cargada in PARES[proceso.nombre]
   y ruta_de_carga not in {C:\Windows\System32, C:\Windows\SysWOW64}:
    alertar "CARGA LATERAL DE BIBLIOTECA"           # severidad máxima
    # La condición decisiva es la RUTA, no el nombre: las tres bibliotecas
    # son legítimas y se cargan a diario desde System32.

# ---- 4. Borrado de copias de sombra (señal tardía, pero inequívoca) ----
si linea_de_ordenes contiene "vssadmin" y contiene "delete shadows":
    alertar "BORRADO DE COPIAS DE SOMBRA"           # severidad máxima
```

> **La primera regla es la importante y es la más incomprendida.** No es una
> lista de malware: **las seis herramientas son legítimas y se usan a diario en
> organizaciones sanas.** La señal es *no estar en el inventario de
> autorizadas*, y por eso la regla **no se puede desplegar sin construir antes
> ese inventario**. Ése es el trabajo, y la regla es la parte fácil.

## X-2. Mitigaciones

| # | Medida | Dónde | Efecto | Coste |
|---|---|---|---|---|
| **X-2.1** | **Inventario de administración remota autorizada + alerta sobre el resto** | Puesto · SOC | Corta la etapa 04 y vale para los ocho actores del lote | Medio una vez |
| **X-2.2** | **Lista de bloqueo de controladores vulnerables de Microsoft, activada** | Puesto | Corta la etapa 05 | **Bajo** |
| **X-2.3** | **Integridad de código con firma propia de la organización para controladores** | Puesto | Cierra BYOVD de forma general, no por nombre | Alto |
| **X-2.4** | **Parcheo prioritario de concentradores y cortafuegos expuestos** | Perímetro | Corta la etapa 01, que es la única anterior al incidente | Medio |
| **X-2.5** | **Segmentar la red de gestión del hipervisor** | Red | Corta el camino de `KJ-6` | Medio |
| **X-2.6** | **Copias inmutables y verificadas de restauración** | Respaldo | No evita la exfiltración; **sí elimina la palanca del cifrado** | Medio |
| **X-2.7** | **Lista de destinos de almacenamiento permitidos en egreso** | Perímetro | Corta la etapa 06 | Medio |

---

## 14. Brechas de inteligencia y requisitos de colección

| # | Brecha | Impacto | Cómo se cierra | Prioridad |
|---|---|---|---|---|
| **G-1** | **El 26 % de los registros de victimología no tiene país** | Condiciona `KJ-3`, que es el juicio regional del informe | Segunda fuente de rastreo; o el propio sitio de filtración | **1** |
| **G-2** | **No tenemos ningún indicador de red ni de fichero** | El informe no aporta nada ingerible salvo patrones | **Leer el anexo técnico del aviso conjunto en original**, que no se consultó | **1** |
| **G-3** | **El inventario de capacidades es de un rastreador y no está verificado** | Afirmaciones como los tres controladores son de tercero | Muestras; o análisis de proveedor leído en original | 2 |
| **G-4** | **No sabemos si el declive es menos ataques o más pagos** | Es `H-2` y cambia el pronóstico por completo | Datos de pagos en cadena de bloques; o telemetría de respuesta a incidentes | 2 |
| **G-5** | **No localizamos aviso oficial posterior a noviembre de 2025** | Todo 2026 es de proveedor, con cifras discrepantes | Vigilar publicaciones oficiales | 2 |
| **G-7** | **No sabemos sobre qué fecha cuenta el ranking del sitio su ventana de siete días** | Es el punto de partida del requisito de toda la serie, y las dos bases defendibles divergen hasta ×8,3 (§O-3.1) | **Una pregunta al operador del rastreador**, o leer su documentación de la API. Barato y cierra la duda para los ocho informes | **1** |
| **G-6** | **Sin telemetría propia** | Limitación estructural de la cartera | Retención de registros de flujo y de puesto | 2 |

**Disparadores de reevaluación.** `I-1`: que la media mensual vuelva por encima de 40 —fin del declive—. `I-2`: aparición de la primera víctima chilena, que refutaría la parte más concreta de `KJ-3`. `I-3`: un aviso oficial nuevo. `I-4`: una variante `Akira_v3` o un cifrador con esquema distinto, que indicaría cambio de desarrollador. `I-5`: aparición de un sucesor con inventario de herramientas solapado (`H-6`). `I-6`: que el rastreador reduzca su proporción de registros sin país y la cifra regional cambie.

---

# ANEXOS

## Anexo A — Indicadores

### A.1 — Patrones de detección · **leer primero**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| pattern | **Herramienta de administración remota presente y no inventariada** | **El indicador de mayor rendimiento del expediente, y el único que sirve contra los ocho actores de este lote.** Akira usa seis productos distintos. La señal es la **ausencia en el inventario de autorizadas**, no la presencia de un nombre | **Alta como señal; requiere inventario previo** | **Sin caducidad** | **Alerta** (`X-1.1`). **No automatizable sin el inventario** |
| pattern | **Carga de controlador firmado presente en la lista de bloqueo de Microsoft** | La etapa 05. Tres nombres concretos documentados (`A.2`) | Alta | Sin caducidad como método | **Incidente de prioridad máxima** |
| pattern | **Biblioteca cargada por `consent.exe`, `icardagt.exe` o `mfpmp.exe` desde ruta distinta de `System32`** | **La condición decisiva es la RUTA.** Las tres bibliotecas son legítimas y se cargan a diario | Alta | Sin caducidad | **Incidente de prioridad máxima** |
| pattern | **`vssadmin delete shadows`** | Señal inequívoca y **tardía**: el cifrado es inminente o está en curso | Alta | Sin caducidad | Incidente de prioridad máxima |
| pattern | **Consultas LDAP masivas desde un puesto no administrativo** | La etapa 02, y la más temprana que deja rastro interno | Media | Sin caducidad | Correlación |
| pattern | **Túnel saliente por Cloudflared, Ngrok u OpenSSH desde un servidor** | Canal de control. En un servidor es casi siempre anómalo | Media-alta | Sin caducidad | Alerta |

### A.2 — Artefactos de evasión nombrados

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| filename | **`churchill_driver.sys`** | Controlador usado para evasión, documentado en el inventario del rastreador | **Declarado por tercero, no verificado** | Sin caducidad | **Bloqueo por lista de controladores** |
| filename | **`fidget.sys`** | Igual | Declarado por tercero | Sin caducidad | Igual |
| herramienta | **Controlador de ThrottleStop** · **controlador de Zemana Anti-Rootkit** | **Controladores LEGÍTIMOS y firmados, abusados por su vulnerabilidad.** Van con tipo `herramienta` para que **no entren en los agregados planos**: bloquear el producto entero no es la medida, bloquear el controlador vulnerable sí | Declarado por tercero | Sin caducidad | **NO bloquear el producto.** Lista de bloqueo de controladores |
| filename | **`consent.exe`** + `msimg32.dll` / `wmsgapi.dll` · **`icardagt.exe`** + `version.dll` · **`mfpmp.exe`** + `rtworkq.dll` | **Tres pares de carga lateral.** Los seis ficheros son **legítimos de Microsoft**: la anomalía es la ruta de carga | Declarado por tercero | Sin caducidad | **Detección por ruta.** **NUNCA bloqueo por nombre** |

### A.3 — Herramientas legítimas del inventario · ⚠ **NO BLOQUEAR**

<!-- cti:note type="warn" -->

> ⚠ **Las veintiocho herramientas de `O-2` son software legítimo o de código
> abierto de uso administrativo normal.** Van con tipo `herramienta` para que
> **no entren en los agregados planos**. Bloquear AnyDesk, RClone o Advanced
> IP Scanner en una organización que los usa produce una interrupción propia,
> no una defensa. **La medida es el inventario, no el bloqueo.**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| herramienta | **AnyDesk · MeshAgent · MobaXterm · Radmin · RustDesk · TeamViewer** | Administración remota. **Seis productos: el inventario más amplio de los ocho actores del lote** | Alta como dato publicado | Sin caducidad | **Inventario y alerta contextual. NUNCA bloqueo ciego** |
| herramienta | **Advanced IP Scanner · Advanced Port Scanner · BloodHound · SharpHound · Masscan · ReconFTW · ShareFinder · SharpShares · SoftPerfect NetScan · ldapdomaindump** | Descubrimiento. **Diez herramientas** | Alta como dato | Sin caducidad | **Detección por comportamiento.** No bloqueo |
| herramienta | **RClone · MEGA · FileZilla · WinSCP · WinRAR · servicio público de ficheros temporales** | Exfiltración | Alta como dato | Sin caducidad | **Control de egreso por destino.** No bloqueo de la herramienta |
| herramienta | **Cloudflared · Ngrok · OpenSSH** | Túnel | Alta como dato | Sin caducidad | **Detección de túnel saliente** |
| herramienta | **Mimikatz · LaZagne · DonPAPI · CrackMapExec · Impacket · NetExec · PowerTool** | Credenciales y ofensiva. **Éstas sí son ofensivas y su presencia en un puesto corporativo es anómala por sí misma** | Alta como dato | Sin caducidad | **Alerta directa** |
| cve | **`CVE-2024-40766`** | SonicWall. **Explotación confirmada por el aviso conjunto, con alcance a un entorno Nutanix.** El único indicador de este informe con respaldo gubernamental | **Alta — fuente oficial** | Mientras haya dispositivos sin parchear | **Parcheo prioritario** (`X-2.4`) |

### A.4 — Victimología y decisiones de higiene

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| cartera | **420 víctimas reclamadas en 2026; 42 en 30 días; 11 en 7 días** | La curva de `KJ-1`. **Son reclamaciones de un sitio de filtración, no brechas verificadas** | Alta como recuento | 60 días | Medición |
| cartera | **7 víctimas latinoamericanas (1,7 %): MX 3 · BR 3 · AR 1. Ninguna chilena** | **La ausencia verificada que sostiene `KJ-3`**, con el 26 % de registros sin país como salvedad | Moderada | 60 días | **Priorización, no tranquilidad** |
| cartera | **No se transcribe ningún nombre de víctima** | **Decisión de higiene.** Son organizaciones atacadas; nombrarlas aquí no aporta defensa y amplifica la publicidad del extorsionador. Quien necesite la lista la tiene en el rastreador | — | — | No ingerir |
| cartera | **No se reproduce ninguna cifra de rescate ni tamaño de datos** | El rastreador no las publica para este actor: **cero registros con cifra de rescate y cero con tamaño de datos** en los 420. Se consigna el **cero** porque es informativo | Alta | — | — |

## Anexo B — Fuentes y valoración

| Fuente | Disciplina | Fiab. | Cred. | Grado | Notas |
|---|---|---|---|---|---|
| **`B-1` — Medición propia** sobre la interfaz pública de un rastreador de sitios de filtración: 420 registros de 2026, contadores por ventana, países, sectores | OSINT técnico · **medición propia** | **B** | **2** | **Medición propia** | Base de `KJ-1` y `KJ-3`. Sesgos: fuente única; **26 % sin país**; son reclamaciones y no brechas; y el recuento incluye lo que el adversario decide publicar |
| **`B-2` — Aviso conjunto del FBI, CISA y socios** (actualización de noviembre de 2025) | GOVINT · **oficial** | **A** | **1** | **Oficial** | **La fuente de más autoridad del informe.** De aquí salen los 244,17 M$ a finales de septiembre de 2025, la variante `Akira_v2`, y `CVE-2024-40766` con alcance a un entorno Nutanix. **Trata el linaje de Conti como valoración analítica, y este informe respeta ese grado.** No leímos su anexo técnico en original: es `G-2` |
| **`B-3` — Perfiles de proveedor** (Brandefense, CybelAngel, Adaptive Security, Halcyon por referencia) | OSINT comercial | **C** | **3** | Proveedor | Fuente del **declive del 43 %** —~50/mes ene–jun → ~29/mes jul–oct de 2026— y de las cifras de +1.400 víctimas y ~245 M$. **Las cifras discrepan entre ellos y con el aviso**, y están medidas en momentos y con métodos distintos: **no se deben sumar** |
| **`B-4` — Inventario de capacidades del rastreador** | OSINT · compilación técnica | **C** | **3** | Proveedor | 48 técnicas en 13 tácticas y las veintiocho herramientas de `O-2`. **Nada de esto lo verificamos** (`G-3`), y es la base de `KJ-4` y `KJ-5` |
| **`B-5` — Datos comparativos del mismo rastreador para los otros siete actores del lote** | OSINT técnico · medición propia | **B** | **2** | Medición propia | Lo que hace utilizable la tabla de `E-1` y `E-3`: **todas las filas, el mismo día, la misma metodología** |

> **La estructura de fuentes de este informe es la más sólida del lote y
> conviene decir por qué:** es **el único de los ocho con una fuente
> gubernamental**. Los juicios que descansan en `B-2` —el CVE, el alcance al
> hipervisor, la cifra de 244,17 millones— tienen un grado que ningún otro
> informe de esta serie podrá igualar. En cambio los juicios de capacidad
> descansan en `B-4`, que es compilación no verificada, **y eso está marcado
> en cada fila de `A.2` y `A.3`**.

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

> **La distinción que este informe necesita, y es la que más se descuida al
> leer un sitio de filtración: hay que separar la confianza en el RECUENTO de
> la confianza en lo que el recuento MIDE.**
>
> «Akira reclamó 420 víctimas en 2026» es un recuento: es reproducible y la
> confianza es **alta**. «Akira atacó con éxito a 420 organizaciones en 2026»
> es otra afirmación, y **no la medimos**: no sabemos cuántas reclamaciones son
> falsas, recicladas o duplicadas. Y «Akira atacó a 420 organizaciones» tampoco
> es «Akira atacó a 420 y ésas son todas»: **las que pagan no se publican**.
>
> **La regla:** un recuento de sitio de filtración acota **por abajo** el
> número de víctimas y **por arriba** nada. Es un suelo con ruido, no una
> medida. Toda la serie de ocho informes se lee con esta advertencia, y el
> `Anexo D` la convierte en método.

## Anexo D — Cómo leer un ranking de actividad de siete días

**El problema.** Un rastreador de sitios de filtración publica rankings por ventana corta, y esos rankings son el punto de partida habitual de un requisito de inteligencia: «dame el top 10». **El ranking es un dato real que mide algo distinto de lo que parece medir.**

**Lo que un ranking de siete días mide en realidad:** el número de **entradas publicadas** en un sitio de filtración durante siete días. No mide intrusiones, no mide víctimas confirmadas, no mide daño y no mide capacidad.

**Las cuatro distorsiones, con su efecto y su contramedida.**

| # | Distorsión | Efecto en el ranking | Contramedida |
|---|---|---|---|
| **1** | **La tanda, y la fecha con que se cuenta** | Un grupo que publica un lote acumulado **puede** aparecer arriba sin haber atacado esa semana, y si eso ocurre depende de **qué fecha use el ranking**. INC Ransom publicó **cincuenta entradas el 12 de noviembre**: contado por publicación es el más activo de la semana, por fecha de ataque es casi inactivo —**una divergencia de ×8,3**— (§O-3.1). Y otro actor del lote publicó **veintiséis entradas en seis minutos, todas fechadas ese mismo día** | **Contar las dos bases y publicar las dos.** Y **comparar la ventana corta con el acumulado del año**: Akira es cuarta del año y décima de la semana; el actor de las veintiséis entradas no tiene año |
| **2** | **El que paga no aparece** | Un grupo eficaz cobrando publica **menos**. Un declive del 43 % es compatible con una tasa de pago mayor (`H-2`) | **No leer una caída como debilitamiento** sin una segunda señal |
| **3** | **La entrada sin víctima** | Entradas anónimas, recicladas o duplicadas cuentan igual. En este lote hay un actor con **59 de 259 nombres anónimos** y otro cuyas listas un proveedor describe como potencialmente fabricadas | **Comprobar que las víctimas son nombradas y verificables por un tercero** — es el criterio 7 del `Anexo D` de `CTI-2026-042` |
| **4** | **La ventana premia lo nuevo** | Un sitio recién abierto publica su fondo de catálogo de golpe y domina la ventana; una operación madura publica a ritmo | **Mirar la fecha de alta del grupo en el rastreador.** Cinco de los ocho de este lote son de las últimas seis semanas |

**El procedimiento, en cuatro pasos y veinte minutos:**

1. **Tomar el ranking de la ventana corta y, al lado, el acumulado del año del mismo rastreador.** Las dos columnas juntas separan la operación de la tanda.
2. **Añadir la fecha de alta de cada grupo.** Distingue «activo» de «recién abierto».
3. **Añadir si hay inventario de capacidades y si hay aviso oficial.** Distingue «marca con operación» de «sitio».
4. **Sólo entonces repartir el esfuerzo**, y repartirlo desigual.

**Las dos advertencias de este método.**

- **No clasifica la peligrosidad, clasifica la solidez de la evidencia.** Un grupo nuevo con un solo cliente competente puede hacer más daño a una organización concreta que una marca madura que nunca la toque. **El método decide dónde invertir atención analítica.**
- **Y favorece lo documentado, que es un sesgo hacia lo anglosajón.** Akira tiene aviso conjunto porque sus víctimas están mayoritariamente en países con agencias que publican avisos. **Un actor con la misma capacidad y victimología exclusivamente latinoamericana aparecería en este método como peor documentado, no como menos peligroso.** La contramedida es el dato regional propio de `E-3`, que no depende de que nadie publique un aviso.

## Anexo E — Marcos de referencia empleados

- **ICD 203**, con la adición del `Anexo C`: **separar la confianza en el recuento de la confianza en lo que el recuento mide**, y la regla de que un recuento de sitio de filtración es un suelo con ruido.
- **Código Admiralty/OTAN**, con el grado **oficial** para `B-2` y **medición propia** para `B-1`, introducido en `CTI-2026-044`.
- **MITRE ATT&CK v18** (`T-2`), con la observación de que **la mayoría de las técnicas de este actor se ejecutan con software legítimo**, lo que desplaza la detección del fichero al contexto.
- **Pirámide del Dolor** (Bianco), en `T-3`, con dos niveles «molestos» de valor desigual: **un controlador nombrado es accionable hoy; una ruta de carga lateral es accionable siempre**.
- **ACH y pre-mortem** (`O-6`), con `H-2` —que el declive sea más pagos y no menos ataques— retenida como la hipótesis más incómoda y no refutable con estos datos.
- **Triaje de un grupo recién nombrado**, `Anexo D` de `CTI-2026-042`, aplicado en `E-1` a los ocho actores del lote.
- **Lectura de un ranking de ventana corta**, propio de este informe (`Anexo D`): cuatro distorsiones, cuatro pasos y veinte minutos.

## Anexo F — Paquete legible por máquina

Las tablas `cti:ioc` alimentan `ioc_index.csv`. **Cinco advertencias:**

1. **⚠ Las veintiocho herramientas de `A.3` llevan tipo `herramienta` y NO entran en los agregados planos.** Son software legítimo de uso administrativo normal. **Bloquear AnyDesk, RClone o Advanced IP Scanner produce una interrupción propia, no una defensa.** La medida es el inventario (`X-2.1`).
2. **Los dos controladores de producto comercial de `A.2` tampoco se bloquean como producto**: lo que se bloquea es el **controlador vulnerable**, por lista de bloqueo, no el fabricante.
3. **Los seis ficheros de carga lateral son binarios y bibliotecas legítimos de Microsoft.** **Nunca se bloquean por nombre**: la señal es la **ruta de carga**. Un bloqueo por nombre de `consent.exe` rompe Windows.
4. **`CVE-2024-40766` es el único indicador de este informe con respaldo gubernamental**, y el único con una acción inequívoca: parchear.
5. **Este informe no aporta ni una dirección, ni un dominio, ni un hash**, y conviene decirlo en lugar de disimularlo: es `G-2`. Lo que aporta son **patrones y una decisión de priorización**.

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.1 | 2026-11-19 | **Corrección de una cifra y de un razonamiento, detectados al medir el segundo informe de la serie.** La cuenta de siete días de Akira pasa de 11 a **8**: las 11 salían de contar por fecha de publicación con un corte propio, y 8 es lo que dan **las dos bases de conteo**, que en este actor coinciden. Se añade §O-3.1 con el hallazgo que lo motivó: **un registro tiene dos fechas —publicación y ataque declarado— y para algunos actores del lote las dos cuentas divergen hasta ×8,3** (INC Ransom: 7 frente a 58, por una tanda de cincuenta entradas publicadas el 12 de noviembre). Se corrige en consecuencia la distorsión 1 del `Anexo D`, que afirmaba que una tanda infla el ranking **sin señalar que eso depende de qué fecha use el ranking**, algo que §O-3.1 declara **no determinable desde fuera** (`G-7`). Y se registra un eje nuevo: `settra` declara fecha de ataque distinta en el **100 %** de sus entradas, `pixelleaks` y `curious worm` en **ninguna** | Célula CTI |
| 1.0 | 2026-11-19 | Emisión inicial, primera de la serie `046`–`053` construida sobre el top 10 de actividad de siete días de un rastreador público. Incluye: el **declive medido y corroborado por dos métodos** —43 % de caída en media mensual, y el 10 % del año en el último mes— (`KJ-1`, `O-3`); la **separación entre declive de actividad y pérdida de capacidad** (`KJ-2`, `E-2`); la **exposición regional como la más baja del lote: 1,7 % y cero víctimas chilenas**, con el contraste medido frente a Qilin (10,0 %) y TheGentlemen (12,6 %) sobre los mismos datos (`KJ-3`, `E-3`); la lectura del **inventario como cadena casi íntegramente legítima** y la consecuencia de que la detección sea un inventario y no una firma (`KJ-4`, `X-1`); los **artefactos nombrados de evasión** —tres controladores y tres pares de carga lateral— (`KJ-5`, `A.2`); la **vía oficialmente documentada de borde a hipervisor** (`KJ-6`); el tratamiento del **linaje como no resuelto**, siguiendo la cautela del propio aviso (`O-5`); la **posición relativa dentro del lote de ocho** que permite priorizar (`E-1`); y el método del `Anexo D` para leer un ranking de ventana corta | Célula CTI |

> **Nota sobre esta emisión.** Es el informe **mejor respaldado y de menor
> relevancia regional** de la serie, y las dos cosas van juntas: Akira tiene
> aviso gubernamental porque sus víctimas están donde hay agencias que
> publican avisos. **El `Anexo D` declara ese sesgo como una propiedad del
> método**, no como una propiedad del adversario, y es la razón de que `E-3`
> mida la exposición regional con datos propios en lugar de inferirla de la
> abundancia de literatura.

## Anexo H — Realimentación del consumidor

1. **¿Existe el inventario de herramientas de administración remota autorizadas?** Es `X-2.1`, `H-1` y la decisión 1 de `E-4`. **Es la única medida de este informe que rinde contra los ocho actores del lote**, y si no existe, **ésa es la conclusión del informe en esa organización**.
2. **¿Está activada la lista de bloqueo de controladores vulnerables?** Es `X-2.2`, cuesta poco y corta la etapa 05. Tres nombres concretos en `A.2`.
3. **¿Se bloqueó alguna herramienta de `A.3`?** Es la pregunta de seguridad de este informe, **al revés de lo habitual**: aquí el riesgo no es dejar de bloquear, es bloquear. Son veintiocho herramientas legítimas, y seis de ellas probablemente las usa el equipo de soporte.
4. **¿Se priorizó Akira por su cifra acumulada?** Cuarta del año, **décima de la semana**, 1,7 % regional. Si entró en el plan por los 245 millones de dólares, entró por el dato equivocado.
5. **¿Se leyó el 1,7 % como «no nos puede pasar»?** Siete organizaciones latinoamericanas sí lo sufrieron, y el 26 % de registros sin país deja margen. **La baja exposición es una razón para priorizar menos, no para no mirar.**
6. **¿Hay un dispositivo de borde sin parchear expuesto?** Es `H-7` y es anterior a todo lo demás. `CVE-2024-40766` tiene respaldo gubernamental y alcanzó un hipervisor.
7. **¿Es la red de gestión del hipervisor alcanzable desde la red de usuarios?** Es `H-8` y `KJ-6`.
8. **Y la pregunta de método, que es la que más vale:** el `Anexo D` sostiene que un ranking de siete días mide publicaciones y no operaciones. **¿Alguien ha encontrado un caso en que la ventana corta acertara y el acumulado del año se equivocara?** Un contraejemplo así valdría más que este informe, porque el método se aplica a los siete que siguen.

*Fin del informe `CTI-2026-046` v1.0.*
