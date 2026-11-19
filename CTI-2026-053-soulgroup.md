---
tlp: "TLP:CLEAR"
pap: "PAP:WHITE"
id: "CTI-2026-053"
version: "1.2"
tipo: "Perfil de operación de extorsión"
foco_regional: "EE. UU. · España · Argentina"
niveles: ["Estratégico", "Operacional"]
autor: "Célula CTI"
actor: "SoulGroup · Soulgroup"
fecha: "2026-11-19"
caduca: "2026-12-19"
distribucion: "Elaborado con fuentes abiertas el mismo día en que el objeto fue observado por primera vez. ADVERTENCIA, MODIFICADA EN v1.1: la versión 1.0 se emitió sin ninguna fuente independiente. La v1.1 incorpora una segunda fuente que resuelve la pregunta central: el 59 % del catálogo de este actor estaba ya publicado por otro grupo noventa y cuatro días antes. No se reproduce ningún nombre de víctima. Difusión libre, conservando la atribución y las salvedades de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-053

## SoulGroup apareció hoy con veintiséis entradas publicadas en trece minutos, y no hay una sola fuente independiente sobre él

### Este informe no es un perfil: es el registro de línea base que permitirá, en dos semanas, saber si esto fue una operación o un escaparate

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-053` |
| Versión | 1.0 — 2026-11-19 |
| Clasificación | `TLP:CLEAR` · **`PAP:WHITE`** — sin indicadores, sin TTP, sin nada accionable |
| Objeto | **`SoulGroup`**, tercer puesto del ranking de siete días que motiva esta serie, y **añadido al rastreador el mismo día de emisión de este informe** |
| Antigüedad observada | **Horas** |
| Foco regional | Sus entradas abarcan **Estados Unidos, España y Argentina** según los campos de país del rastreador. **Es el único actor nuevo del lote con una posible víctima argentina** |
| Lo que lo distingue en este lote | **Es el objeto menos caracterizable de los ocho, y por mucho.** Cero fuentes independientes, cero TTP, cero herramientas, cero análisis, y **su propia fuente tenía un registro incompleto de él al escribir esto** |
| **Qué es este informe** | **No es un perfil de actor.** Es un **registro de línea base**: lo que hay que anotar hoy para poder decidir en dos semanas si esto fue una operación real o un sitio sembrado (`Anexo D`) |
| Caducidad | **2026-12-19 (30 días) — la más corta de toda la cartera**, y deliberada |
| Autor | Célula CTI |

<!-- cti:note type="warn" -->

> ⚠ **Lea esto antes de seguir, porque condiciona el documento entero.**
>
> **Este actor fue observado por primera vez el mismo día en que se escribe
> este informe.** No hay análisis de proveedor, no hay cobertura de prensa, no
> hay aviso oficial, no hay muestras, no hay indicadores y no hay una segunda
> fuente. **Todo lo que sigue procede de un único rastreador**, y durante la
> redacción **ni su API de víctimas ni su instantánea de víctimas recientes
> tenían registro de este actor**, mientras su portada sí listaba sus entradas
> (`KJ-2`).
>
> **Por eso este documento no pretende ser un perfil.** Un perfil de un objeto
> de horas sería una ficción con estructura de informe. **Lo que se emite es el
> registro de lo que se pudo medir hoy**, con la fecha y la hora, para que en
> dos semanas se pueda comparar. El `Anexo D` explica por qué ese registro vale
> más que el perfil que no se puede escribir.

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** **Publicó veintiséis entradas en aproximadamente trece minutos, todas con fecha de ataque igual a la de publicación.** En la captura de la portada del rastreador que tomamos el 19 de noviembre de 2026, las entradas de este actor aparecen con marcas de descubrimiento entre las **14:09 y las 14:22 UTC**, y el ranking de siete días del sitio le asigna **26 víctimas**. Valoramos **casi con certeza** *(≥99 %)* los hechos observados. **Confianza: alta para la observación.** *Lectura:* **ninguna operación ataca veintiséis organizaciones y las publica en trece minutos.** El catálogo **llegó hecho**, y eso es compatible con dos cosas: víctimas acumuladas antes de abrir escaparate, o un sitio sembrado. **Con las fechas de ataque todas iguales al día de publicación, no hay ni un dato que permita distinguirlas** (`E-2`).

**KJ-2.** **Y el hallazgo de método es una discrepancia dentro de una misma fuente: su portada listaba las víctimas mientras su API no tenía registro del actor.** Al consultar la interfaz de víctimas por grupo, la respuesta fue **«no se encontraron víctimas para el grupo»**; la instantánea de víctimas recientes, pedida dos veces con quince minutos de diferencia, **devolvió el mismo contenido y sin una sola entrada de este actor**; y la ficha de grupos sí lo registraba, con fecha de alta de hoy y sin descripción, TTP ni herramientas. Valoramos **casi con certeza** *(≥99 %)* la discrepancia, verificada con cuatro consultas. **Confianza: alta.** *Consecuencia para toda la serie, y es la aportación de este informe:* **el front-end y la API de un mismo rastreador pueden no coincidir, y un analista que consulte sólo la API concluirá que un actor con veintiséis reclamaciones no existe.** Es la hermana de la trampa de `CTI-2026-044` `O-2.2`.

**KJ-3.** **No existe ninguna fuente independiente sobre este actor, y la ausencia es total.** Todas las referencias que localizamos remiten a fichas de víctima **del mismo rastreador**. No hay análisis de proveedor, ni cobertura de prensa especializada, ni aviso oficial, ni mención en recuentos de terceros. Valoramos **casi con certeza** *(≥99 %)* la ausencia, con la salvedad obvia de que **el actor tiene horas de vida y la ausencia de literatura es lo esperable**. **Confianza: alta.** *Consecuencia:* **este expediente no se puede corroborar en ningún punto**, y su único valor es el registro de `Anexo A`.

**KJ-4.** **Su catálogo abarca Estados Unidos, España y Argentina, y es el único actor nuevo del lote con una posible víctima argentina.** Las entradas que pudimos leer incluyen organizaciones estadounidenses —sanidad, energía, tecnología, servicios profesionales, manufactura, comercio minorista— **y al menos una española y una argentina** según los campos de país del rastreador. Valoramos **probable** *(55–80 %)* que haya al menos una víctima reclamada en Latinoamérica. **Confianza: moderada** — **no pudimos obtener los campos de país directamente**, porque la API no tenía los registros, y esto procede de la lectura de la portada y de fichas de terceros que la reproducen. *Consecuencia:* **para una organización argentina es la única razón por la que este informe existe**, y la comprobación es inmediata (`E-3.1`).

**KJ-5.** **No hay concentración sectorial: seis sectores distintos en las primeras diez entradas legibles.** Sanidad, energía y servicios públicos, tecnología, servicios profesionales, manufactura y comercio minorista. Valoramos **moderada** la confianza, sobre una base de diez entradas. *Lectura:* **la dispersión sectorial en una tanda inicial es, en sí misma, un indicio débil a favor del sitio sembrado**, porque una operación con capacidad suele mostrar algún sesgo de sector o de geografía derivado de cómo obtiene el acceso. **Es débil y se marca como tal.**

**KJ-6.** **Y el juicio honesto sobre el conjunto: este objeto no se puede evaluar todavía, y decirlo es la conclusión.** Aplicando el método de triaje del `Anexo D` de `CTI-2026-042`, cumple **un criterio de siete** —tiene sitio de filtración con víctimas nombradas— y falla los seis restantes: sin análisis primario, sin aviso de autoridad, sin familia identificable, sin linaje conocido, sin víctima verificable por tercero, y **sin que sepamos ni cómo se contacta con él**. Valoramos **muy probable** *(80–95 %)* que no exista base suficiente para un perfil de actor. **Confianza: alta.** *Clasificación provisional:* **reclamación sin respaldo, pendiente de evidencia** — la clase más baja del método, y la que merece **una línea en una lista de vigilancia y un disparador de reevaluación**, no un expediente.

**KJ-7.** **Y en v1.1 la pregunta central queda respondida, con una segunda fuente y en contra de las dos hipótesis que `KJ-1` ofrecía: el catálogo no se acumuló ni se sembró, se copió.** De las veintisiete entradas que este actor tiene en la ventana de seis meses, **dieciséis (59 %) corresponden a víctimas publicadas por `insomnia` entre el 9 de agosto y el 15 de septiembre de 2026**. La dirección es unánime —**dieciséis casos de dieciséis** con este actor en segundo lugar— y la separación es consistente: mediana de **94 días**, con todos los casos entre 57 y 94. Valoramos **muy probable** *(80–95 %)* que se trate de republicación del catálogo de otro actor, y **muy improbable** *(5–20 %)* que las dieciséis coincidencias sean accesos propios. **Confianza: alta para el solapamiento, moderada para la interpretación.** *Consecuencia:* **esto explica la tanda de `KJ-1`** —un catálogo que llega hecho porque no se construyó— y **reclasifica el expediente**: de «reclamación sin respaldo, pendiente de evidencia» a **marca republicadora** (`E-5`). El método está en `CTI-2026-055` `Anexo D`; el disparador que se cumplió es el `I-3` de `§14`.


---

## 2. Resumen ejecutivo

`SoulGroup` fue añadido al rastreador que motiva esta serie **el mismo día en que se escribe este informe**, y ocupa su tercer puesto con veintiséis reclamaciones. Las entradas que pudimos leer se publicaron **entre las 14:09 y las 14:22 UTC: veintiséis en unos trece minutos**, todas con fecha de ataque igual a la de publicación.

**Ninguna operación ataca veintiséis organizaciones y las publica en trece minutos.** El catálogo llegó hecho. Eso es compatible con una operación que acumuló víctimas antes de abrir escaparate y con un sitio sembrado con material ajeno o antiguo, **y no hay un solo dato que permita distinguir las dos cosas**, precisamente porque ninguna entrada declara cuándo ocurrió el acceso.

No hay nada más. **No existe ningún análisis de proveedor, ninguna cobertura de prensa, ningún aviso oficial, ninguna muestra y ninguna segunda fuente.** El rastreador no le registra ni una TTP ni una herramienta ni una descripción. Y hubo una dificultad de colección que vale la pena contar: **la portada del rastreador listaba sus víctimas mientras su propia API respondía «no se encontraron víctimas para el grupo»**, y la instantánea de víctimas recientes, pedida dos veces, no traía ninguna. **Un analista que hubiera consultado sólo la API habría concluido que un actor con veintiséis reclamaciones no existía.**

Lo único con relevancia regional —y la razón por la que este documento se emite— es que **sus entradas abarcan Estados Unidos, España y Argentina**, lo que lo convierte en **el único de los seis actores nuevos del lote con una posible víctima argentina**. Para una organización argentina la comprobación es inmediata y vale la pena hacerla hoy.

Aplicando el método de triaje que esta cartera desarrolló para grupos recién nombrados, **cumple un criterio de siete** y queda clasificado en la clase más baja: **reclamación sin respaldo, pendiente de evidencia**. Lo que eso merece es una línea en una lista de vigilancia, no un expediente.

**Por eso este informe no es un perfil, y conviene decirlo sin rodeos: es un registro de línea base.** Lo que se anota hoy —cuántas entradas, con qué fechas, con qué campos, en qué minutos— es lo único que permitirá, en dos semanas, decidir si esto fue una operación o un escaparate. **La primera jornada es el único momento en que esa línea base se puede capturar, y es la aportación del `Anexo D`.**

---

## 3. Alcance y limitaciones

### 3.1 Qué cubre

Lo que se pudo observar de `SoulGroup` el 19 de noviembre de 2026: el volumen y la cadencia de su tanda inicial, la dispersión sectorial y geográfica de sus reclamaciones, la discrepancia entre el front-end y la API de su única fuente, y su clasificación provisional. **Y el registro de línea base del `Anexo A`.**

### 3.2 Qué NO cubre, que es casi todo

| Fuera de alcance | Por qué |
|---|---|
| **Un perfil de actor** | **No hay base.** Horas de existencia, una fuente, cero análisis |
| **Cadena de intrusión, TTP, herramientas, cifrado, canal de negociación** | **Nada de eso está registrado ni observado** |
| **La veracidad de sus reclamaciones** | Ninguna confirmada por nadie |
| **Los nombres de las víctimas** | **No se reproducen** (`CTI-2026-048` `E-4`). Son reclamaciones de horas sin confirmar |
| **La composición exacta por país** | **No la pudimos obtener de la API**, que no tenía los registros (`KJ-4`) |
| **Indicadores** | No hay ninguno. `PAP:WHITE` |
| **Niveles táctico y técnico** | **Se omiten por completo**, y es la primera vez en la cartera. No hay un solo dato que los sostendría |

### 3.3 Limitaciones de la colección

<!-- cti:note type="warn" -->

> ⚠ **Siete limitaciones, y son la mayor parte del informe.**
>
> 1. **Horas de existencia observada.**
> 2. **Fuente única, y con registro incompleto de sí misma** (`KJ-2`).
> 3. **La API de víctimas no devolvía datos**, de modo que no pudimos medir
>    campos presentes y ausentes como en los seis informes anteriores de la
>    serie. **Las cifras de este informe son de lectura de portada**, no de
>    datos estructurados.
> 4. **Cero fuentes independientes.**
> 5. **Las veintiséis entradas del ranking no las pudimos enumerar todas**:
>    leímos diez en la captura de portada y localizamos otras cinco por fichas
>    de terceros que reproducen la misma fuente.
> 6. **La composición por país es de segunda mano** (`KJ-4`).
> 7. **Y el informe se escribe el mismo día**, de modo que **no hay ninguna
>    perspectiva temporal**: no sabemos si el catálogo seguirá creciendo, se
>    detendrá o desaparecerá.

### 3.4 Qué aporta

| Aporte | Dónde |
|---|---|
| **El registro de línea base** del primer día: volumen, cadencia, fechas y campos | `Anexo A` |
| **La tanda de 26 entradas en 13 minutos**, medida con marcas de tiempo | `KJ-1` |
| **La discrepancia entre el front-end y la API de un mismo rastreador** — hallazgo de método | `KJ-2` |
| **La única posible víctima argentina de los seis actores nuevos** | `KJ-4` |
| **La clasificación provisional honesta**: un criterio de siete | `KJ-6` |
| **Un protocolo para las primeras veinticuatro horas de un actor nuevo** | `Anexo D` |

### 3.5 Veredicto

<!-- cti:table highlight="NO EVALUABLE|NO SOSTENIDO|propio" -->

| # | Elemento | Veredicto | Base |
|---|---|---|---|
| 1 | `SoulGroup` es una operación de extorsión caracterizable | **NO EVALUABLE** | Horas de vida, una fuente, cero análisis (`KJ-6`) |
| 2 | Tiene 26 víctimas | **NO SOSTENIDO** | Tiene **26 entradas publicadas en 13 minutos**. No es lo mismo (`KJ-1`) |
| 3 | Es un sitio sembrado | **NO EVALUABLE — y ningún dato discrimina** | Las fechas de ataque son todas del día de publicación (`E-2`) |
| 4 | Hay fuentes independientes sobre él | **NO SOSTENIDO** | **Cero.** Todas remiten al mismo rastreador (`KJ-3`) |
| 5 | Su victimología es evaluable | **NO SOSTENIDO** | La API no devolvía registros; los datos son de lectura de portada (`KJ-2`) |
| 6 | Tiene exposición latinoamericana | **PROBABLE** | **España y Argentina entre sus países**, de segunda mano (`KJ-4`) |
| 7 | Merece un expediente de actor | **NO SOSTENIDO** | **Un criterio de siete** en el triaje de `CTI-2026-042` (`KJ-6`) |
| 8 | La API de un rastreador refleja lo que muestra su portada | **NO SOSTENIDO — hallazgo de método** | Cuatro consultas; la API decía que no tenía víctimas (`KJ-2`) |

---

# NIVEL ESTRATÉGICO
### Para: CTI, CISO · Horizonte: 2 semanas

## E-1. Qué se pudo observar, y nada más

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `26` | Entradas que el ranking le asigna | Tercer puesto del top 10 |
| `~13 min` | **Ventana en que se publicaron las entradas legibles** | Entre las 14:09 y las 14:22 UTC del 2026-11-19 |
| `10` | Entradas que pudimos leer en la captura de portada | Más cinco localizadas por fichas de terceros |
| `6` | Sectores distintos en esas diez entradas | **Sin concentración** (`KJ-5`) |
| `3` | Países en sus entradas | **EE. UU., España y Argentina** |
| `0` | **Fuentes independientes** | `KJ-3` |
| `0` | TTP, herramientas, muestras, indicadores y descripciones registradas | |
| `0` | Registros que devolvía su API de víctimas | **Mientras su portada los listaba** (`KJ-2`) |
| `1 / 7` | **Criterios de triaje que cumple** | Método de `CTI-2026-042` `Anexo D` (`KJ-6`) |
| `30 d` | Caducidad de este informe | **La más corta de la cartera** |

## E-2. La tanda de trece minutos, y por qué no se puede interpretar

**El hecho:** veintiséis entradas publicadas en una ventana de unos trece minutos, todas con fecha de ataque igual a la de publicación.

**Las dos explicaciones, y lo que cada una implicaría:**

| Explicación | Qué implicaría | Qué la apoyaría |
|---|---|---|
| **Operación que acumuló víctimas antes de abrir escaparate** | Hay un actor con capacidad de intrusión sobre veintiséis organizaciones, no caracterizado por nadie | **Fechas de ataque anteriores y distintas** — y no las hay |
| **Sitio sembrado con material ajeno, antiguo o inventado** | No hay capacidad de intrusión; la respuesta es de comunicación | **Coincidencia del material con brechas ya divulgadas** — comprobable sólo por las víctimas |

**Ningún dato disponible discrimina**, y la razón es precisa: **la única variable que distinguiría las dos hipótesis es la fecha de acceso, y este actor no la declara en ninguna entrada.** `CTI-2026-052` se encontró con el mismo problema y `CTI-2026-049` con lo contrario —un actor que declara fecha distinta en el 100 % de sus entradas—, lo que convierte ese campo en el discriminante más útil de toda la serie.

> **Y conviene una comparación que sitúa este caso en el lote: de los seis
> actores nuevos, tres publicaron más del 40 % de su catálogo en su primer
> día** —`Vortex` el 40 %, `Curious Worm` el 50 %, y éste el 100 %—. **La
> tanda inicial no es una anomalía: es cómo nacen estos sitios.** Lo que varía
> es si después crecen a ritmo, y eso sólo se ve con el tiempo. **Es la razón
> del `Anexo D`.**

## E-3. Lo único con relevancia regional

### E-3.1 La posible víctima argentina

**Lo que hay:** las entradas de este actor abarcan **Estados Unidos, España y Argentina** según los campos de país del rastreador, en la lectura que pudimos hacer. **Es el único de los seis actores nuevos del lote con una posible víctima argentina**; los demás reparten así su exposición latinoamericana: `pixelleaks` tres mexicanas, `settra` tres brasileñas y una mexicana y una ecuatoriana, `n0n` seis brasileñas, `Vortex` y `curious worm` ninguna.

**Lo que no hay:** confirmación directa. **No pudimos obtener los campos de país de la API**, de modo que `KJ-4` descansa en la lectura de la portada y en fichas de terceros que reproducen la misma fuente.

| # | Acción | A quién | Coste | Cuándo |
|---|---|---|---|---|
| **1** | **Si operamos en Argentina o España: comprobar si aparecemos listados** | CISO · CTI | **Muy bajo** | **Hoy.** Es la única acción con urgencia de este informe |
| **2** | **Si aparecemos: comprobar primero si el material coincide con una brecha ya divulgada** | CISO · Legal | Bajo | Antes de cualquier otra cosa (`CTI-2026-052` `Anexo D`) |
| **3** | **Tener respuesta de comunicación preparada** | Comunicación | Medio | Antes de necesitarla: este actor publicó sin aviso previo |

## E-4. Decisiones que este informe pide

| # | Decisión | A quién | Coste | Por qué |
|---|---|---|---|---|
| **1** | **No abrir expediente de seguimiento para este actor** | CTI | **Cero, y ahorra** | `KJ-6`: un criterio de siete. **Lo que merece es una línea en una lista de vigilancia** |
| **2** | **Registrar hoy la línea base del `Anexo A` y fijar la reevaluación a dos semanas** | CTI | **Muy bajo** | **La única acción de este informe que no se puede hacer después** (`Anexo D`) |
| **3** | **Si operamos en Argentina o España: comprobar listado hoy** | CISO | Muy bajo | `E-3.1` |
| **4** | **No citar este actor en materiales de riesgo ni en informes a dirección** | CTI | Cero | **Un actor de horas con una fuente no sostiene ninguna afirmación**, y citarlo gasta credibilidad |
| **5** | **Y al consultar cualquier rastreador: no concluir desde la API sin mirar el front-end** | CTI | Cero | `KJ-2`: la API decía que este actor no tenía víctimas |

---

# NIVEL OPERACIONAL

## O-1. Identificación, con lo poco que hay

| Campo | Valor |
|---|---|
| Nombre | **`SoulGroup`** · también `Soulgroup` |
| Alias | Ninguno conocido |
| En el rastreador desde | **2026-11-19** — el día de emisión de este informe |
| Sitios de filtración | **Uno, activo** |
| Descripción en el rastreador | **Ninguna** |
| TTP registradas | **Ninguna** |
| Herramientas registradas | **Ninguna** |
| Cifrado | **Sin información** |
| Canal de negociación | **Sin información.** Es el criterio 1 del triaje de `CTI-2026-042` y **no lo pudimos determinar**, lo que impide incluso clasificarlo entre «operación» y «herramienta» |
| Fuentes independientes | **Ninguna** |
| Aviso gubernamental | Ninguno |

## O-2. La dificultad de colección, y por qué se cuenta

**Lo que ocurrió, en orden:**

1. La **portada** del rastreador, capturada el 19-11-2026, listaba entradas de este actor con marcas de descubrimiento entre las **14:09 y las 14:22 UTC**.
2. La consulta a la **interfaz de víctimas por grupo** devolvió `{"error": "No victims found for group 'soulgroup'."}`, y lo mismo con la grafía `SoulGroup`.
3. La **instantánea de víctimas recientes** —cien registros— **no contenía ninguna entrada de este actor**, y su rango temporal terminaba a las **11:25 UTC**, antes de las publicaciones.
4. Pedida **una segunda vez** quince minutos más tarde, devolvió **exactamente el mismo contenido y el mismo tamaño**: venía de caché.
5. La **ficha de grupos** sí registraba al actor, con fecha de alta de hoy, un sitio activo y **ningún otro campo**.

**La conclusión de método, y es la aportación transferible de este informe:**

> **El front-end y la API de un mismo rastreador pueden no coincidir, y la
> diferencia puede ser de horas.** Un analista que consulte únicamente la API
> —que es lo razonable, porque devuelve datos estructurados— **concluirá que un
> actor con veintiséis reclamaciones publicadas no existe.**
>
> Es la hermana de la trampa de `CTI-2026-044` `O-2.2`, donde una consulta sin
> parámetros devolvía en silencio una sola familia. **La forma del error es la
> misma: la herramienta responde correctamente a una pregunta que no era la que
> se quería hacer.** Y la contramedida es la misma y es el control 1 del
> `Anexo D` de ese informe: **comparar la consulta con la vista para humanos en
> el mismo minuto.**

## O-3. Lo que se pudo leer de su catálogo

**Sin nombrar a nadie**, las diez entradas legibles en la captura de portada corresponden a: dos organizaciones de **sanidad**, una de **energía y servicios públicos**, dos de **tecnología**, dos de **servicios profesionales**, una de **manufactura**, una de **comercio minorista** y una sin sector asignado. **Todas con fecha de ataque 2026-11-19** y marcas de descubrimiento entre las 14:09 y las 14:22 UTC.

Fichas de terceros que reproducen la misma fuente añaden otras cinco, entre ellas **una organización española** y **una que por su denominación corresponde a Latinoamérica**, además de otra de **gestión sanitaria** y una **tecnológica**.

**No hay en ninguna de ellas:** cifra de rescate, tamaño de datos, referencia de prensa, ni fecha de acceso distinta de la de publicación.

## O-4. Clasificación provisional

**Aplicando los siete criterios del `Anexo D` de `CTI-2026-042`:**

| # | Criterio | `SoulGroup` |
|---|---|---|
| **1** | ¿Cómo contacta la víctima con el adversario? | **No determinado.** No pudimos ver el canal |
| **2** | ¿Hay sitio de filtración con víctimas nombradas? | **Sí** — el único criterio que cumple |
| **3** | ¿Existe análisis primario con muestra desmontada? | **No** |
| **4** | ¿Lo ha nombrado alguna autoridad? | **No** |
| **5** | ¿Las herramientas públicas identifican la familia? | **No aplicable**: no se conoce malware |
| **6** | ¿Hay linaje de código o de personal? | **Desconocido** |
| **7** | ¿Hay víctimas verificables por un tercero? | **No.** Ninguna confirmación |

**Resultado: uno de siete.** Clase: **reclamación sin respaldo, pendiente de evidencia.** Lo que merece, según el propio método, es **una línea en una lista de vigilancia**, y es exactamente lo que `E-4.1` recomienda.

> **Y conviene decir por qué se emite un informe para algo que merece una
> línea.** Porque el requisito pedía los ocho actores del top 10, y **la
> respuesta correcta a «perfila este actor» cuando no hay base es un documento
> que lo diga, no un silencio ni un perfil inventado.** Este informe es
> deliberadamente el más corto de la cartera, no tiene niveles táctico ni
> técnico, y su valor está en el `Anexo A` y en el `Anexo D`.

## O-5. Hipótesis y pre-mortem

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| **H-1 — Sitio sembrado con material ajeno, antiguo o inventado** | **Retenida al mismo nivel que su contraria.** Veintiséis entradas en trece minutos, sin fechas de acceso, sin confirmaciones | `Aprox. igual de probable · 40–60 %` |
| **H-2 — Operación real que acumuló víctimas antes de abrir escaparate** | **Retenida al mismo nivel.** Es como nacieron otros tres sitios de este lote | `Aprox. igual de probable · 40–60 %` |
| **H-3 — Es una marca nueva de un actor conocido** | **Sin evidencia, y es el patrón que la cartera ha visto cinco veces.** Lo que habría que buscar: solapamiento de víctimas con otro actor en los próximos días | `Aprox. igual de probable · 40–60 %` |
| **H-4 — Desaparecerá en dos semanas sin volver a publicar** | **Retenida.** Es el destino de una parte de los sitios que nacen con una tanda | `Posibilidad real · 40–60 %` |
| **H-5 — La dispersión sectorial indica siembra** | **Retenida como indicio débil y marcada como tal.** Una operación con capacidad suele mostrar algún sesgo derivado de cómo obtiene el acceso | `Posibilidad real · 40–60 %` |

**Pre-mortem — si este informe se equivoca, será porque:**

1. **Alguien lo citó como si fuera un perfil de actor.** **Es el riesgo 1**, y la cabecera y `O-4` existen para prevenirlo.
2. **No se registró la línea base hoy**, y en dos semanas no habrá con qué comparar (`E-4.2`).
3. **Una organización argentina o española no comprobó si estaba listada** porque el informe parecía menor.
4. **Se concluyó desde la API que el actor no tenía víctimas** (`KJ-2`).
5. **Se abrió un expediente de seguimiento** y se gastó esfuerzo en un objeto de un criterio de siete.
6. **O el objeto resultó ser una operación grande y real**, y haber recomendado una línea en una lista de vigilancia fue insuficiente. **Es el riesgo simétrico y se asume**: con un criterio de siete, la apuesta correcta es la vigilancia, aunque a veces pierda.

---

## E-5. Lo que v1.1 descubrió: el catálogo venía de otro sitio

**Añadido el 19 de noviembre de 2026, horas después de la emisión inicial.** La
incorporación de una segunda fuente a la cartera —`CTI-2026-054`— permitió
someter este actor a la comprobación que `G-3` y el disparador `I-3` pedían, y
el resultado responde la pregunta que `KJ-1` había dejado abierta entre dos
hipótesis. **No era ninguna de las dos.**

| Medición | Resultado |
|---|---|
| Entradas de este actor en la ventana de seis meses | 27 |
| De ellas, víctimas ya publicadas por `insomnia` | **16 (59 %)** |
| Casos en que este actor publica después | **16 de 16 (100 %)** |
| Separación mediana | **94,0 días** |
| Separación mínima / máxima | 57 / 94 días |
| `insomnia` sigue publicando | **Sí**, 23 entradas en el semestre, la última el 14-11-2026 |

Las dieciséis son organizaciones estadounidenses de sanidad, servicios
jurídicos y administración local, más una española y una alemana, publicadas
por `insomnia` entre el 9 de agosto y el 15 de septiembre y reaparecidas aquí
**el 11 de noviembre**.

### E-5.1 Dos correcciones a la versión 1.0

**Primera, y es una corrección a una medición propia.** `KJ-1` midió una ventana
de «aproximadamente trece minutos» para la publicación de las veintiséis
entradas. En la segunda fuente, **veinticinco de las veintisiete llevan la misma
marca de observación exacta**. Lo que medimos no fue la duración de la
publicación: fue **el intervalo entre dos sondeos del rastreador**. Es la lección
de `CTI-2026-045` `§O-5.2` —las marcas de tiempo son horas de observación—
aplicada ahora contra nuestro propio informe. La tanda sigue siendo un hecho;
su duración de trece minutos, no.

**Segunda, sobre la clasificación.** `O-4` clasificó el expediente como
**«reclamación sin respaldo, pendiente de evidencia»**, la clase más baja del
método de `CTI-2026-042`. Con `KJ-7` la clasificación cambia a **marca
republicadora**: hay respaldo para dieciséis de sus veintisiete entradas, pero
**el respaldo es de otro actor**. El triaje pasa de **uno** a **tres criterios
de siete** cumplidos: tiene sitio con víctimas nombradas, tiene ahora una
víctima verificable por tercero —las dieciséis lo son, en el catálogo de
insomnia—, y tiene un linaje identificable, aunque sea de procedencia y no de
código.

### E-5.2 Qué cambia para una víctima

**Si una organización aparece en este catálogo, lo primero que debe comprobar es
si ya apareció en `insomnia` entre agosto y septiembre de 2026.** En dieciséis
de veintisiete casos la respuesta es sí, y entonces **no hubo un segundo acceso**:
los datos son los de agosto, y el incidente que hay que revisar es aquél.

Para las once entradas restantes la pregunta sigue abierta y es la de `G-3` en su
forma nueva: **o son accesos propios de este actor, o proceden de un tercer
catálogo que no hemos contrastado.**

### E-5.3 Y una tercera fuente da una tercera fecha

**Añadido en v1.2.** Consultada una tercera fuente el mismo día, la tanda
inicial de este actor queda fechada así:

| Fuente | Fecha que atribuye | Entradas que cuenta |
|---|---|---|
| El rastreador de v1.0 | **2026-11-19** | 26 |
| cti.fyi (`E-5`) | **2026-11-11** | 27 |
| CTIWatch | **2026-11-04** | 25 |

**Quince días entre los extremos.** Las tres cifras de entradas son casi
iguales —26, 27, 25—, señal de que las tres miran el mismo catálogo; lo que
difiere es cuándo lo vio cada una. **Ninguna de las tres es la fecha del
adversario.**

Esto obliga a una corrección más de v1.0, y afecta al título del informe: la
afirmación de que este actor «apareció hoy» era cierta **para nuestro
observador**, no para el actor. Según CTIWatch llevaba quince días publicado
cuando lo vimos. El hecho —una tanda que llega hecha— se mantiene; **su fecha,
no**.

El análisis completo está en `CTI-2026-054` `§O-9`. La ficha de CTIWatch sobre
este actor tiene además un defecto que conviene consignar aquí: **mezcla una
familia de malware de Malpedia actualizada en octubre de 2025 con esta
operación de noviembre de 2026**. Si se hubiera tomado por corroboración de
linaje, el error habría sido grave (`CTI-2026-054` `§O-8.3`).


## 14. Brechas de inteligencia y requisitos de colección

| # | Brecha | Impacto | Cómo se cierra | Prioridad |
|---|---|---|---|---|
| **G-1** | **No se pudo enumerar su catálogo completo** | Las cifras de este informe son de lectura de portada, no de datos estructurados | **Reintentar la API en 24–48 horas**, cuando haya ingerido los registros | **1** |
| **G-2** | **No se conoce el canal de contacto con la víctima** | Es el criterio 1 del triaje y **el más discriminante**: impide clasificar entre operación y herramienta | Lectura del sitio de filtración. Requiere acceso a la red oscura | **1** |
| **G-3** | ~~**Cero fuentes independientes**~~ → **RESUELTA PARCIALMENTE en v1.1.** Una segunda fuente corrobora 16 de las 27 entradas, **como catálogo de otro actor** (`E-5`) | Ya no es cierto que nada sea corroborable | Hecho. Queda la forma nueva en `G-7` | — |
| **G-4** | **No sabemos si el catálogo crecerá, se detendrá o desaparecerá** | Sigue abierta, pero **ya no decide todo**: `E-5` responde de dónde vino lo publicado | **La reevaluación a dos semanas del `Anexo D`** | 2 |
| **G-7** | **No sabemos el origen de las once entradas que NO están en `insomnia`** | **Es la pregunta central de v1.1.** O son accesos propios, o vienen de un tercer catálogo | Contrastarlas contra los demás actores del semestre con el método de `CTI-2026-055` `Anexo D` | **1** |
| **G-5** | **La composición por país es de segunda mano** | Afecta a `KJ-4`, que es el único juicio con relevancia regional | Reintento de la API (`G-1`) | **1** |
| **G-6** | **No hay TTP, herramientas, muestras ni indicadores** | Ninguna detección posible | Informe de incidente de una víctima | 2 |

**Disparadores de reevaluación.** `I-1`: **que el catálogo crezca a ritmo en los próximos catorce días** —apoyaría `H-2`—. `I-2`: **que no publique nada más en catorce días** —apoyaría `H-1` y `H-4`—. `I-3`: **solapamiento de víctimas con otro actor conocido** —apoyaría `H-3`—. **CUMPLIDO el 19-11-2026: dieciséis víctimas comunes con `insomnia`, dirección unánime, 94 días de separación** (`E-5`, `KJ-7`). `I-4`: aparición de la primera ficha de proveedor o de prensa. `I-5`: confirmación o negación de una víctima. `I-6`: que una víctima identifique el material como de una brecha anterior ya divulgada, lo que confirmaría la siembra.

---

# ANEXOS

## Anexo A — Registro de línea base del 19 de noviembre de 2026

> **Este anexo es el contenido principal del informe.** No son indicadores: es
> la fotografía del primer día, con la hora, para que en dos semanas se pueda
> comparar. **Es lo único de este expediente que no se puede obtener después.**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| cartera | **Alta en el rastreador: 2026-11-19.** Un sitio de filtración, activo | El punto de partida de toda comparación futura | Alta | — | **Registro** |
| cartera | **26 entradas según el ranking de siete días del sitio**, consultado a las 16:20 UTC del 2026-11-19 | **La cifra de referencia.** Si en dos semanas son 26, el sitio está muerto; si son 200, es una operación | Alta como lectura | **Comparar el 2026-12-03** | **Registro y comparación** |
| cartera | **Diez entradas legibles con marcas de descubrimiento entre las 14:09 y las 14:22 UTC** | **La cadencia de la tanda inicial: veintiséis en unos trece minutos** (`KJ-1`) | Alta | — | Registro |
| cartera | **Todas las entradas legibles con fecha de ataque 2026-11-19, igual a la de publicación** | **El dato que impide discriminar entre operación y siembra** (`E-2`). Si aparecen entradas con fecha anterior y distinta, **eso es `I-1`** | Alta | — | **Registro y vigilancia del campo** |
| cartera | **Seis sectores distintos en diez entradas; sin concentración** | `KJ-5`, indicio débil | Moderada | — | Registro |
| cartera | **Países observados: EE. UU., España, Argentina** | `KJ-4`, **de segunda mano** (`G-5`). **La única relevancia regional del expediente** | **Moderada** | — | **Comprobación inmediata si se opera en esos países** |
| cartera | **Cero: descripción, TTP, herramientas, muestras, indicadores, cifras de rescate, tamaños de datos, referencias de prensa y fuentes independientes** | **La lista de ausencias es el perfil.** Cualquiera de ellas que aparezca es un disparador | Alta | — | **Registro.** Cada cero es un disparador |
| cartera | **Su API de víctimas devolvía «no se encontraron víctimas» mientras su portada las listaba** | `KJ-2`, verificado con cuatro consultas, dos de ellas servidas desde caché | **Alta** | — | **Lección de método** (`O-2`) |
| cartera | **No se reproduce ningún nombre de víctima** | Reclamaciones de horas, sin confirmar, sobre organizaciones nombradas. Regla de `CTI-2026-048` `E-4` | — | — | No ingerir |

## Anexo B — Fuentes y valoración

| Fuente | Disciplina | Fiab. | Cred. | Grado | Notas |
|---|---|---|---|---|---|
| **`B-1` — Captura de la portada del rastreador** (2026-11-19) y su ficha de grupos | OSINT técnico · **medición propia** | **B** | **3** | **Medición propia, sobre lectura de portada** | **La única fuente real del informe.** Credibilidad degradada a 3 respecto de los informes anteriores de la serie porque **no son datos estructurados**: son texto extraído de una página, y su API no los servía (`KJ-2`) |
| **`B-2` — Fichas de víctima de terceros que reproducen la misma fuente** | OSINT · compilación | **C** | **4** | Compilación derivada | Añaden cinco nombres y los campos de país de `KJ-4`. **No son una segunda fuente: reproducen `B-1`**, y por eso no corroboran nada |
| **`B-3` — Datos comparativos del mismo rastreador para los otros actores del lote** | OSINT técnico · medición propia | **B** | **2** | Medición propia | Lo que permite situar la tanda inicial de este actor junto a las de `Vortex` y `Curious Worm` (`E-2`) |
| **`B-4` — API de cti.fyi**, endpoints de reclamaciones cruzadas y de entradas (2026-11-19). **Añadida en v1.1** | OSINT técnico · **medición propia** sobre datos de proveedor | **B** | **2** | **Medición propia** | **La segunda fuente que v1.0 no tenía, y la que resuelve el informe:** corrobora 16 de las 27 entradas **como catálogo de `insomnia`** (`E-5`, `KJ-7`). Evaluada en `CTI-2026-054` con seis defectos documentados; **ninguno afecta a esta medición**, que no emplea su campo de separación horaria |

> **Esta es la estructura de fuentes más débil de toda la cartera, y conviene
> enunciarlo sin matizarlo: hay una fuente, de lectura de portada, y una
> compilación que la reproduce.** `B-2` **no corrobora** `B-1`: cita a `B-1`.
> **Un informe con una sola fuente y ninguna corroboración posible no puede
> sostener un perfil**, y de ahí que `O-4` clasifique y no describa.

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

> **La categoría que este informe necesita y que el léxico no tiene: NO
> EVALUABLE.**
>
> «Poco probable» y «aproximadamente igual de probable» son juicios: afirman
> algo sobre el mundo a partir de evidencia. **Cuando la evidencia es de horas y
> de una fuente, el analista no tiene un juicio débil: no tiene juicio.** Y
> escribir «aproximadamente igual de probable» en ese caso **simula una
> indeterminación medida donde sólo hay ignorancia.**
>
> **La regla que se adopta:** `NO EVALUABLE` se usa en `§3.5` para los
> elementos sobre los que no hay base, y se distingue de `SIN RESOLVER`, que
> significa que hay evidencia en los dos sentidos y no basta. **La diferencia
> importa porque la acción es distinta: lo no evaluable necesita colección; lo
> sin resolver necesita una prueba discriminante.**

## Anexo D — Protocolo de las primeras veinticuatro horas de un actor nuevo

**El problema.** Cuando un sitio de filtración aparece, **la única cosa que un analista externo puede hacer de forma útil no es analizarlo: es fotografiarlo.** Las propiedades que permitirán decidir, dos semanas después, si era una operación o un escaparate **son propiedades del cambio**, y el cambio sólo se mide contra una línea base que hay que capturar ahora. **Pasadas las primeras horas, esa línea base ya no se puede obtener.**

**Qué registrar hoy, en seis campos y diez minutos:**

| # | Campo | Por qué importa en dos semanas |
|---|---|---|
| **1** | **Número de entradas, con la hora exacta de la consulta** | **La métrica de crecimiento.** Si no cambia, el sitio está muerto; si se multiplica, es una operación |
| **2** | **Cadencia de la tanda inicial**: cuántas entradas en cuántos minutos | **La firma del nacimiento.** Veintiséis en trece minutos es un fondo preparado, no una semana de trabajo |
| **3** | **Proporción de entradas con fecha de ataque distinta de la de publicación** | **El discriminante más útil de toda esta serie.** Un actor que empieza a declarar fechas anteriores está aportando datos comprobables; uno que nunca lo hace, no |
| **4** | **Dispersión sectorial y geográfica** | Un sesgo que aparece con el tiempo indica **cómo obtiene el acceso**; la dispersión persistente apunta a material heterogéneo de origen ajeno |
| **5** | **La lista de ceros**: qué campos están vacíos —rescate, tamaño, prensa, muestras, TTP— | **Cada cero es un disparador.** El primer campo que se llene dice en qué dirección evoluciona el objeto |
| **6** | **El canal de contacto con la víctima** | **El criterio más discriminante del triaje** de `CTI-2026-042`: portal es operación, correo es herramienta. **En este caso no se pudo obtener, y es `G-2`** |

**Y la regla de decisión a dos semanas:**

| Si a los catorce días… | Entonces |
|---|---|
| **El catálogo no ha crecido** | **Sitio sembrado o abandonado.** Cerrar la línea de vigilancia |
| **Ha crecido a ritmo, con fechas de ataque anteriores y distintas** | **Operación real.** Abrir expediente |
| **Ha crecido en tandas, todo con fecha del día** | **Sigue sin discriminar.** Mantener vigilancia y buscar solapamiento de víctimas con otros actores |
| **Ha desaparecido** | **Registrar y cerrar.** Y buscar el mismo material bajo otra marca, que es el patrón que esta cartera ha visto cinco veces |

**Las tres advertencias de uso.**

1. **Este protocolo no analiza: prepara el análisis.** Es deliberado. **La tentación en el primer día es escribir un perfil, y un perfil de un objeto de horas es una ficción con estructura de informe.**
2. **El campo 3 es el que más rinde y el que nadie mira.** De los seis actores nuevos de esta serie, uno declara fecha de ataque distinta en el 100 % de sus entradas y dos en el 0 %. **Esa diferencia separó, en esta serie, a la operación mejor evidenciada de las dos peores.**
3. **Y la decisión por omisión a los catorce días debe ser cerrar, no continuar.** Una lista de vigilancia que sólo crece deja de ser una lista de vigilancia. **El coste de cerrar una línea que luego resulta importante es un expediente tardío; el de mantener cuarenta líneas abiertas es no mirar ninguna.**

## Anexo E — Marcos de referencia empleados

- **ICD 203**, con la adición de la categoría **`NO EVALUABLE`** del `Anexo C`, distinta de `SIN RESOLVER`: la primera pide colección, la segunda pide una prueba discriminante.
- **Código Admiralty/OTAN**, con credibilidad degradada a **3** para la fuente propia por tratarse de lectura de portada y no de datos estructurados, y con la observación de que `B-2` **no corrobora** `B-1` sino que la reproduce.
- **Triaje de un grupo recién nombrado**, `Anexo D` de `CTI-2026-042`, aplicado en `O-4`: **un criterio de siete**, clase «reclamación sin respaldo».
- **MITRE ATT&CK, niveles táctico y técnico: omitidos por completo.** Primera vez en la cartera, y es la decisión correcta: no hay un solo dato que los sostendría.
- **Protocolo de las primeras veinticuatro horas**, propio de este informe (`Anexo D`): seis campos, diez minutos, y una regla de decisión a catorce días cuyo valor por omisión es **cerrar**.

## Anexo F — Paquete legible por máquina

Las tablas `cti:ioc` alimentan `ioc_index.csv`. **Cuatro advertencias:**

1. **No hay indicadores de compromiso de ningún tipo.** `PAP:WHITE`. **Las nueve filas del `Anexo A` son un registro de línea base**, no indicadores, y van con tipo `cartera` para que **no entren en los agregados planos**.
2. **No se reproduce ningún nombre de víctima.**
3. **La fila con mayor valor del anexo es la lista de ceros**: cada campo vacío es un disparador, y el primero que se llene dirá en qué dirección evoluciona el objeto.
4. **Y este informe caduca el 2026-12-19, treinta días**, la vida más corta de la cartera. **La comparación del `Anexo A` debe hacerse el 2026-12-03**, a los catorce días, que es la regla de decisión del `Anexo D`.

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-11-19 | Emisión inicial, **octava y última de la serie `046`–`053`**, y la más corta de la cartera. Incluye: la **tanda de veintiséis entradas en trece minutos** con marcas de tiempo (`KJ-1`); el **hallazgo de método de la discrepancia entre el front-end y la API de un mismo rastreador**, verificado con cuatro consultas, dos de ellas servidas desde caché (`KJ-2`, `O-2`); la constatación de **cero fuentes independientes** (`KJ-3`); la **única posible víctima argentina de los seis actores nuevos del lote**, con la salvedad de que el dato es de segunda mano (`KJ-4`); la **clasificación provisional honesta: un criterio de siete, clase «reclamación sin respaldo»** (`KJ-6`, `O-4`); la **omisión completa de los niveles táctico y técnico**, primera vez en la cartera; la adición de la categoría **`NO EVALUABLE`** al léxico (`Anexo C`); el **registro de línea base** del `Anexo A`, que es el contenido principal; y el **protocolo de las primeras veinticuatro horas** del `Anexo D` | Célula CTI |
| 1.2 | 2026-11-19 | **Añade `§E-5.3`: una tercera fuente fecha la tanda el 4 de noviembre**, frente al 11 de cti.fyi y el 19 de v1.0 — **quince días entre los extremos**, con las tres contando 25, 27 y 26 entradas. **Corrige el supuesto de v1.0 de que el actor «apareció hoy»**: apareció hoy para nuestro observador. Consigna la colisión de nombres de la ficha de CTIWatch con una familia de Malpedia de 2025 | La fecha de `KJ-1` deja de ser un hecho del actor |
| 1.1 | 2026-11-19 | **Se responde la pregunta central del informe, y en contra de las dos hipótesis de `KJ-1`.** Incorpora `KJ-7` y `§E-5`: **el 59 % del catálogo de este actor (16 de 27 entradas) estaba ya publicado por `insomnia` entre agosto y septiembre de 2026**, con dirección unánime en 16 de 16 casos y separación mediana de **94 días**. **Cambia la clasificación** de «reclamación sin respaldo» a **marca republicadora**, y el triaje de **uno a tres criterios de siete**. **Corrige una medición propia de v1.0:** la ventana de «trece minutos» de `KJ-1` era el intervalo entre dos sondeos del rastreador, no la duración de la publicación. Cierra `G-3` parcialmente, degrada `G-4` a prioridad 2 y abre **`G-7`** sobre las once entradas sin contrastar. **El disparador `I-3` se cumplió.** La caducidad **no se extiende**: ningún juicio sobre capacidad del actor se ha revalidado | Célula CTI |

> **Nota sobre esta emisión, y cierra la serie.** Este informe es
> deliberadamente el más corto y el más pobre de la cartera, porque su objeto
> lo es. **El requisito pedía los ocho actores del top 10 de un ranking de
> siete días, y el tercer puesto de ese ranking resultó ser un sitio de horas
> sin una sola fuente independiente.** La respuesta correcta a «perfila este
> actor» cuando no hay base no es el silencio ni un perfil inventado: es un
> documento que lo diga, que registre lo que se pudo medir, y que fije la fecha
> en que habrá que volver a mirar.
>
> **Y ése es también el juicio de la serie entera sobre su propio punto de
> partida:** de los ocho actores del top 10, **dos tenían historia, inventario
> y —en un caso— aviso gubernamental; cinco habían aparecido en las últimas
> seis semanas; y uno apareció el día de emisión.** El ranking no estaba
> equivocado: medía publicaciones, que es lo que dice medir. **Lo que no se
> puede hacer es leerlo como un orden de prioridades.**

## Anexo H — Realimentación del consumidor

1. **¿Se registró hoy la línea base del `Anexo A`?** Es la decisión 2 de `E-4` y **la única acción de este informe que no se puede hacer después**. Si no se hizo, en dos semanas no habrá con qué comparar y el expediente no servirá para nada.
2. **¿Está fijada la reevaluación para el 3 de diciembre de 2026?** Es la regla del `Anexo D`, a catorce días, **y su valor por omisión es cerrar la línea de vigilancia**, no continuarla.
3. **Si operamos en Argentina o España: ¿se comprobó hoy si aparecemos listados?** Es `E-3.1` y **la única urgencia del informe**.
4. **¿Alguien citó este informe como si fuera un perfil de actor?** Es el riesgo 1 del pre-mortem. **Un criterio de siete, una fuente, horas de vida.** Citarlo en un material de riesgo gasta credibilidad sin aportar nada.
5. **¿Se abrió un expediente de seguimiento?** `E-4.1` dice que no se debe: **lo que merece es una línea en una lista de vigilancia**.
6. **¿Alguien consultó sólo la API de un rastreador y concluyó que un actor no existía?** Es `KJ-2` y es la lección transferible: **la portada y la API de una misma fuente pueden diferir en horas**.
7. **Y la pregunta de método, que cierra la serie:** el `Anexo D` sostiene que **la proporción de entradas con fecha de ataque distinta de la de publicación es el discriminante más útil de toda esta serie** —uno de los seis actores nuevos la declara en el 100 % de sus entradas, dos en el 0 %—. **¿Alguien ha encontrado un caso en que ese campo no discrimine, o un actor que lo falsee sistemáticamente?** Si existe, el campo 3 del protocolo pierde su valor y hay que buscar otro.

*Fin del informe `CTI-2026-053` v1.0.*
