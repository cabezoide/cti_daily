---
tlp: "TLP:CLEAR"
pap: "PAP:WHITE"
id: "CTI-2026-054"
version: "1.1"
tipo: "Evaluación de fuentes"
foco_regional: "Global · Latinoamérica como submuestra"
niveles: ["Estratégico", "Operacional"]
autor: "Célula CTI"
actor: "No aplica · Evaluación de un rastreador"
fecha: "2026-11-19"
caduca: "2027-02-19"
distribucion: "Evaluación de una fuente de terceros incorporada a la cartera el 19 de noviembre de 2026, con licencia de uso no comercial. Los seis defectos que aquí se documentan se midieron sobre los datos servidos ese día y son reproducibles con las consultas del Anexo F. No se reproduce ningún nombre de víctima salvo los de organizaciones que el propio actor desenmascaró y mantiene desenmascaradas. Difusión libre conservando la atribución y las salvedades de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-054

## De sesenta y ocho grupos de extorsión aparentemente nuevos en seis meses, catorce lo son: el resto es el rastreador ampliando cobertura

### Evaluación de cti.fyi y de CTIWatch, con los defectos que hay que corregir antes de citarlas, los tres datos que no da ninguna otra, y tres fuentes que fechan el mismo hecho con quince días de diferencia

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-054` |
| Versión | 1.0 |
| Tipo | Evaluación de fuente |
| Clasificación | `TLP:CLEAR` · `PAP:WHITE` |
| Fecha de emisión | 2026-11-19 |
| Caducidad | 2027-02-19 |
| Niveles | Estratégico · Operacional |
| Objeto | API pública de cti.fyi, nivel «community» |
| Ventana medida | 2026-05-19 a 2026-11-19 (184 días) |
| Volumen analizado | 5.144 entradas · 129 grupos · 1.895 agrupaciones de reclamación cruzada |
| Autor | Célula CTI |

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** **Sesenta y ocho grupos parecen estrenarse en la ventana de seis meses y sólo catorce lo hacen de verdad; los demás son sitios que ya existían y que el rastreador empezó a mirar.** La prueba no es un juicio, es una medición: en los cinco días en que se concentran los estrenos, el retraso entre la fecha que el sitio de filtración declara para una entrada y la fecha en que el rastreador la descubre tiene una **mediana de 41,1 días**, y el 60 % de esas entradas supera los 30 días; en todos los demás días del semestre esa mediana es de **0,5 días**. Valoramos **casi con certeza** *(≥99 %)* que los picos son incorporación de cobertura y no actividad del adversario. **Confianza: alta.** *Consecuencia:* **«fecha de primera aparición en la fuente» no es «fecha de primera actividad del grupo»**, y quien construya una curva de aparición de actores nuevos sobre este campo medirá el calendario de trabajo del rastreador (`E-1`, `O-1`).

**KJ-2.** **El endpoint de reclamaciones cruzadas anuncia 1.895 víctimas reclamadas por dos o más grupos y 706 colisiones en menos de veinticuatro horas, y ninguna de las dos cifras resiste la comprobación.** El campo del que se deriva la segunda, `delta_hours`, **discrepa de su propia definición en 205 de 500 agrupaciones recalculadas (41 %)**: declara 0,0 horas donde la separación real entre las primeras reclamaciones de dos grupos distintos es de 11.392 horas en un caso y de 18.368 en otro —475 y 765 días—. Y al restringir el conjunto a lo que pide este informe —dos grupos **léxicamente distintos** reclamando **dentro** de la ventana de seis meses— quedan **44 agrupaciones de 1.895**, de las cuales **ninguna** está por debajo de una hora de separación y el 68 % supera los treinta días. Valoramos **casi con certeza** *(≥99 %)* ambos defectos. **Confianza: alta.** *Consecuencia:* la cifra titular es la que un analista citaría sin verificar, y es la que no se sostiene (`O-2`, y el expediente completo en `CTI-2026-055`).

**KJ-3.** **La fuente mantiene expedientes separados para un mismo actor, y en un caso es el propio perfil de la fuente el que dice que son el mismo.** La ficha de `apt73` describe «el grupo, autodenominado APT73 y después Bashe»; el catálogo tiene además un expediente `bashe` con 119 entradas. En la ventana de seis meses **`bashe` tiene cero entradas** y `apt73` tiene 79, de las cuales **77 fueron descubiertas el 7 de octubre de 2026 en un solo día** y declaran fechas de publicación repartidas entre **abril de 2024 y julio de 2026**. De los once sitios registrados bajo `apt73`, **cuatro se titulan «APT73» y cinco «BASHE»**. Valoramos **casi con certeza** *(≥99 %)* que se trata de un único actor con dos expedientes y de una reindexación histórica, no de actividad. **Confianza: alta.** *Consecuencia:* el actor que un recuento por volumen situaría como el de arranque más explosivo del semestre —79 entradas en seis días— **no tuvo actividad en el semestre** (`O-3`).

**KJ-4.** **El filtro de reclamaciones retiradas existe, se puede consultar y devuelve cero sobre 35.879 entradas: es un campo muerto que induce la conclusión contraria a la verdadera.** La consulta por estado de reclamación «withdrawn» responde con un conjunto vacío en toda la base histórica. Y sabemos por una fuente independiente —el análisis de Bitdefender que recogimos en `CTI-2026-048`— que **un solo actor, n0n, retiró 126 de sus propias entradas**. Valoramos **casi con certeza** *(≥99 %)* que el evento ocurre y que la fuente no lo registra. **Confianza: alta.** *Consecuencia, y es la más peligrosa de las seis:* un analista que pregunte «¿qué reclamaciones se retiraron?» recibirá «ninguna» y concluirá que no hay retiradas, **que es exactamente lo contrario de lo que ocurre** (`O-4`).

**KJ-5.** **El campo de confianza del enriquecimiento sirve para detectar ausencia de datos y no sirve para ordenar nada, porque el 77,9 % de sus valores es exactamente 0,95.** Sí discrimina en un sentido: la puntuación media es **0,397** cuando ninguno de los tres campos duros —dominio, país, sector— está poblado, y **0,935** cuando lo están los tres. Pero dentro del conjunto con datos la distribución está colapsada en un único punto. Valoramos **casi con certeza** *(≥99 %)* la medición. **Confianza: alta.** *Consecuencia:* es un detector de registros vacíos, **no una graduación de fiabilidad**, y usarlo para priorizar víctimas no hace nada (`O-5`). Y conviene decir que la sospecha inicial de este informe —que el campo fuera arbitrario— **era demasiado fuerte y quedó refutada**.

**KJ-6.** **La hora de publicación es inutilizable para inferir husos horarios, y no hay filtro que lo arregle.** En veinte grupos el campo de publicación es una fecha sin hora en el 90 % o más de los casos —en akira, 189 de 189; en nightspire, 97 de 97—, lo que genera un pico falso a medianoche que concentra el **35,7 % de todas las publicaciones, 8,6 veces la media horaria**. Excluir esos veinte grupos reduce el pico a **20,8 %, 5,0 veces la media**, pero **no lo elimina**, porque hay grupos que declaran hora unas veces y no otras. Valoramos **casi con certeza** *(≥99 %)* que el artefacto es irrecuperable mediante filtrado agregado. **Confianza: alta.** *Consecuencia:* una publicación genuina a las 00:00 es **indistinguible** de una fecha sin hora, de modo que el análisis de huso horario sólo es legítimo grupo a grupo y sólo en los que declaran hora de forma consistente (`O-6`).

**KJ-7.** **Y pese a los seis defectos, la fuente aporta tres datos que no da ninguna otra de la cartera, y uno de ellos vale por sí solo la incorporación.** Primero, **838 entradas con marca de revisión** (16,3 % del semestre), que permiten ver que un sitio de filtración se edita después de publicar. Segundo, **41 entradas con historial de título**, que registran el instante exacto en que el extorsionador **desenmascara a la víctima**: `AuditTeam` reveló cuatro nombres el 9 de noviembre **entre las 08:04:06 y las 08:04:33**, y `nightspire` reveló uno y **volvió a ocultarlo siete segundos después**. Tercero, el inventario de infraestructura por actor, con FQDN, estado y versión de cada sitio. Valoramos **casi con certeza** *(≥99 %)* la existencia y el contenido de los tres. **Confianza: alta.** *Consecuencia:* **el desenmascaramiento progresivo es una fase medible de la extorsión**, y hasta hoy la cartera no tenía ninguna fuente que lo fechara (`E-3`, `O-7`).

**KJ-8.** **El juicio de conjunto: fuente de valor alto y uso condicionado, no sustituto de las que ya teníamos.** Sus 425 grupos y 35.879 entradas son del mismo orden que los del rastreador que la cartera ya usa, pero **ninguna de las dos es un patrón de la otra**: donde pudimos comparar el mismo actor, los recuentos no coinciden —SoulGroup 27 frente a 26, Vortex 29 frente a 35—. Valoramos **muy probable** *(80–95 %)* que la discrepancia proceda de ciclos de sondeo distintos y de criterios distintos de deduplicación, y **no** de que una de las dos esté equivocada. **Confianza: moderada**, porque no tenemos acceso al criterio de ninguna de las dos. *Consecuencia:* **se incorpora como fuente de corroboración y de los tres datos únicos, con los seis correctivos de `Anexo D` aplicados antes de cualquier cita** (`E-4`).

**KJ-9.** **Añadido en v1.1, y es el hallazgo más limpio del informe: tres rastreadores fechan la misma tanda de publicaciones con quince días de diferencia entre los extremos.** Para el actor `soul` —expediente `CTI-2026-053`—, ransomware.live sitúa la actividad el **19 de noviembre**, cti.fyi el **11 de noviembre**, y CTIWatch declara «primer ataque registrado el **4 de noviembre** de 2026». Ninguna de las tres es la fecha del adversario: las tres son **la fecha en que cada observador miró**. Valoramos **casi con certeza** *(≥99 %)* la discrepancia, verificada en las tres fuentes el mismo día. **Confianza: alta.** *Consecuencia:* es la demostración más económica de que **la fecha de descubrimiento es una propiedad del observador**, y convierte `KJ-1` de inferencia en principio: si tres fuentes discrepan quince días sobre un hecho de hace dos semanas, **ninguna serie temporal construida sobre una sola de ellas describe al adversario** (`O-9`).

**KJ-10.** **Y la cuarta fuente incorporada, CTIWatch, aporta dos capacidades que la cartera no tenía y unas fichas de actor que no se pueden usar.** Aporta un catálogo de **409.830 CVE con CVSS, EPSS y estado de explotación** —la primera fuente de la cartera que permite ordenar una cola de parcheo— y **2.322.362 indicadores** procedentes de telemetría propia de señuelos. Pero sus fichas de actor **se contradicen consigo mismas en seis de seis casos comprobados**: la cabecera y la prosa de la misma página dan cifras distintas de víctimas —qilin 2.602 frente a 2.059; krybit 183 frente a 78—, el campo «visto por última vez» vale **la misma fecha de marzo para cuatro actores** con actividad en noviembre, y clasifica a un RaaS con reparto de ingresos 80/20 como motivado por **espionaje**. La propia fuente declara que esa prosa está «generada por la tubería de análisis de CTIWatch». Valoramos **casi con certeza** *(≥99 %)* los defectos. **Confianza: alta.** *Consecuencia:* **se incorpora para CVE e indicadores, no para perfilar actores**, y con la restricción de su `robots.txt`, que prohíbe el uso de su API (`O-8`).


---

## 2. Resumen ejecutivo

El 19 de noviembre de 2026 se incorporó a la cartera una fuente nueva: la API pública de **cti.fyi**, con licencia de nivel «community» —30 peticiones por minuto, 1.000 diarias, sin exportación masiva— y condiciones de uso no comercial. Este informe es su evaluación, y la conclusión es que **sirve, con seis correcciones obligatorias**.

La pregunta que motivó la incorporación era sencilla: **qué grupos de extorsión han estado activos en los últimos seis meses**. La respuesta ingenua que la fuente permite construir es «sesenta y ocho grupos nuevos». La respuesta correcta es **catorce**, y la diferencia entre las dos cifras es el hallazgo principal.

El mecanismo es el siguiente. Cada entrada del catálogo lleva **tres fechas distintas** —la que el sitio de filtración declara, la que el rastreador registra al descubrirla, y la de la última revisión—, y la fuente, a diferencia de otras, **las expone separadas**. Eso permite restar: si un grupo aparece por primera vez el 25 de septiembre con cincuenta entradas cuyas fechas de publicación son de abril, mayo y junio, lo que ocurrió el 25 de septiembre **no fue el nacimiento del grupo, fue el primer día en que alguien lo miró**. Aplicada esa resta a los sesenta y ocho candidatos, catorce tienen retraso prácticamente nulo —son contemporáneos—, veintitrés tienen retrasos de decenas o centenas de días —son preexistentes—, veinte quedan en zona dudosa y once no son evaluables porque no declaran ninguna fecha de publicación.

Los otros cinco defectos son de distinta gravedad. El más citable y menos sólido es el de las **reclamaciones cruzadas**: la fuente anuncia 1.895 víctimas reclamadas por varios grupos y 706 colisiones en menos de un día, y al recalcular el campo del que sale la segunda cifra resulta estar mal en el 41 % de los casos. El más peligroso es el **campo muerto**: se puede filtrar por reclamaciones retiradas, el filtro funciona, y devuelve cero sobre 35.879 entradas cuando sabemos de una sola operación que retiró 126 de las suyas. El más silencioso es el de los **expedientes duplicados**, con un actor cuyo propio perfil declara que sus dos nombres son el mismo y al que la fuente cuenta dos veces.

A cambio, la fuente da tres cosas que la cartera no tenía. La que más vale es el **historial de título**: cuarenta y una entradas en las que se conserva el nombre anterior y la marca de tiempo del cambio. Lo que esas cuarenta y una entradas registran es el momento en que el extorsionador deja de proteger la identidad de la víctima —`Pe***CT` pasa a `Pelican ICT`, `A***** T******` pasa al nombre completo de una textil turca—, y en un caso registra una fuga y un repliegue: un actor reveló un nombre y volvió a enmascararlo **siete segundos más tarde**. Hasta hoy la cartera describía el desenmascaramiento como una amenaza; con este campo puede fecharlo.

El resultado práctico es una lista de catorce grupos realmente nuevos y de un conjunto de actores establecidos y activos que la cartera no cubría. Cinco de ellos reciben expediente propio en este mismo lote: **BrainCipher** (432 entradas, el mayor volumen del semestre y el perfil probatorio más débil), **krybit** (154 entradas en 46 países, el perfil más verificable), **safepay** (134 entradas con una concentración alemana del 29 %), **Booba Project** (129 entradas, 48 % sanidad y administración pública) y **Storm** (86 entradas, 73 de ellas el primer día). Un sexto candidato, `apt73`, fue retirado del lote al comprobarse que es el artefacto de `KJ-3`.

---

## 3. Alcance y limitaciones

### 3.1 Qué se midió

Todo lo que este informe afirma se midió sobre las respuestas que la API de cti.fyi devolvió el 19 de noviembre de 2026 entre las 21:08 y las 22:30 UTC, con la licencia de nivel «community» del usuario de la cartera. Las consultas exactas están en `Anexo F` y son reproducibles.

### 3.2 Qué no se pudo medir

- **La exportación masiva y el formato STIX 2.1 están vedados** en este nivel de licencia: la respuesta es un 403 con el texto «Bulk export requires an Evaluation, Enterprise or Partner license». Por tanto **no se evaluó la calidad del paquete STIX**, que es donde la fuente dice publicar técnicas de ATT&CK.
- **No hay acceso al criterio de deduplicación ni al calendario de incorporación** de la fuente. Las conclusiones de `KJ-1` y `KJ-3` se sostienen sobre la huella que esos procesos dejan en los datos, no sobre su documentación.
- **No se verificó ninguna reclamación contra la víctima.** Ninguna de las organizaciones nombradas en este informe ha confirmado nada.
- **El enriquecimiento es derivado, no observado.** Los campos de país, sector, dominio y resumen llevan una justificación del tipo «Direct match from leak blog card», que indica inferencia a partir de la ficha publicada. Todo recuento geográfico o sectorial de este informe hereda ese límite.

### 3.3 Qué se decidió no hacer

La API expone una operación `POST .../claim/{id}/reveal` descrita como «Reveal And Burn Claim». **No se invocó.** Es una escritura de efecto irreversible sobre un recurso de terceros y nada en el encargo la pedía. Tampoco se invocaron las operaciones de registro, reenvío de licencia ni telemetría.

### 3.4 Higiene aplicada a los nombres de víctima

Este informe reproduce nombres de organización en un solo supuesto: cuando el propio actor los desenmascaró y **los mantiene desenmascarados**. El caso de `nightspire` —un nombre revelado y vuelto a ocultar en siete segundos— se documenta **sin reproducir el nombre**, porque el actor revirtió su propia revelación y reproducirla aquí la haría permanente. Es la misma regla de `CTI-2026-049`.

### 3.5 Veredicto por nivel

| Nivel | Veredicto | Motivo |
|---|---|---|
| Estratégico | **Utilizable** | El recuento corregido de actores nuevos y la estructura de cobertura son sólidos |
| Operacional | **Utilizable con los seis correctivos** | `Anexo D` es condición previa a cualquier cita |
| Táctico | **No evaluado** | La fuente no expone TTP en este nivel de licencia |
| Técnico | **Parcial** | Inventario de infraestructura sí; indicadores de ejecución no |

---

# NIVEL ESTRATÉGICO

## E-1. El escalón de cobertura, y por qué parece una ola de actores nuevos

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `5.144` | Entradas en la ventana de 184 días | De 35.879 en todo el histórico |
| `129` | Grupos con al menos una entrada | De 425 en el catálogo |
| `18` | **Mediana de entradas por día** | La línea de fondo del semestre |
| `201` | Máximo diario (2026-09-30) | **11 veces la mediana** |
| `24` | Grupos que se estrenan el 25 y el 26 de septiembre | En dos días |
| `41,1 d` | **Retraso mediano publicación→descubrimiento en días de pico** | `KJ-1` |
| `0,5 d` | El mismo retraso en los demás días | **Ochenta veces menor** |
| `68 → 14` | Candidatos a grupo nuevo, y los que lo son | La corrección de este informe |

La curva de entradas descubiertas por día en el semestre tiene una línea de fondo estable de unas dieciocho al día y cinco picos que la multiplican por seis a once. Los picos no están repartidos al azar: **coinciden con los días en que se estrenan grupos en masa**.

| Fecha | Entradas | Grupos que se estrenan | Veces la mediana |
|---|---|---|---|
| 2026-09-25 | 148 | **12** | 8,2 |
| 2026-09-26 | 139 | **12** | 7,7 |
| 2026-09-30 | 201 | 7 | **11,2** |
| 2026-10-01 | 113 | 3 | 6,3 |
| 2026-10-07 | 138 | 5 | 7,7 |

Veintiséis operaciones de extorsión no nacen en dos días. Lo que ocurre es que **el rastreador amplió su lista de sitios vigilados**, y al hacerlo descargó de golpe el historial que esos sitios ya tenían publicado.

### E-1.1 La prueba, que es una resta

La fuente expone separadas la fecha que el sitio declara (`published`) y la fecha en que el rastreador la vio (`discovered`). La diferencia entre las dos es el retraso de observación. En condiciones normales es de horas: el rastreador recorre los sitios cada pocas decenas de minutos y ve las entradas casi cuando aparecen. Si un día el retraso se dispara, lo que entró ese día es **pasado**.

- En los cinco días de pico: mediana **41,1 días**, percentil 90 en **174,8 días**, y **el 60 % de las entradas por encima de 30 días**.
- En los otros 179 días: mediana **0,5 días**, y sólo el 13 % por encima de 30.

Grupos como `exitium` (183,5 días de retraso mediano), `netrunner` (175,1), `ULose` (173,1), `fulcrumsec` (147,2) o `m3rx` (106,4) no empezaron a operar en septiembre: **llevaban meses publicando y nadie los estaba mirando**. En el extremo opuesto, `N0n` tiene retraso mediano de **0,0 días** y se estrenó el mismo 25 de septiembre: ese sí apareció mientras la fuente ya vigilaba.

### E-1.2 El recuento corregido

| Clase | Criterio | Grupos | Entradas |
|---|---|---|---|
| **Nuevo contemporáneo** | Retraso mediano ≤ 3 días | **14** | 823 |
| Dudoso | Entre 3 y 30 días | 20 | 388 |
| **Preexistente incorporado** | Más de 30 días | **23** | 523 |
| No evaluable | Sin ninguna fecha de publicación | 11 | 110 |

Los catorce contemporáneos, por volumen: **N0n** (387), **Booba Project** (129), **PixelLeaks** (67), **Emperador** (49), **Deadlock** (36), **Vortex** (29), **titan** (28), **Whitearmor** (27), **soul** (27), **BYOD** (23), **UmBra** (10), **Gammax** (7), **Spirals** (3) y **0x00** (1). Cinco de ellos ya tienen expediente en la cartera; la coincidencia es una corroboración útil, porque llegaron a la cartera por otra fuente y por otro camino.

> **Nota de método.** Hubo que descartar también el borde de la ventana. Todo grupo que ya estuviera activo antes del 19 de mayo aparece «estrenándose» el primer día del conjunto: ocho grupos cayeron en ese artefacto, que es de nuestro recorte y no de la fuente.

## E-2. Las reclamaciones cruzadas, y la diferencia entre 1.895 y 44

El endpoint de reclamaciones cruzadas es la capacidad más atractiva de esta fuente y la que exige más cuidado. Su descripción promete identificar «compromisos de un corredor de acceso compartido, afiliados operando en varias marcas rivales a la vez, y reventa de datos o extorsión secundaria». Es exactamente el eje que la cartera no tenía.

Lo que devuelve son **1.895 agrupaciones de víctima** con dos o más grupos reclamándola, y una cifra destacada de **706 colisiones en menos de veinticuatro horas**. Al comprobarlo:

1. **El campo `delta_hours` está mal en el 41 % de las agrupaciones.** Recalculando la separación entre las primeras reclamaciones de cada grupo distinto, 205 de 500 discrepan en más de una hora. El patrón del error es sistemático: declara **0,0** donde la separación real son cientos de días.
2. **La mayor parte del conjunto es histórica.** Las agrupaciones abarcan desde 2022. Al exigir que dos grupos distintos reclamen **dentro** del semestre, quedan **44**.
3. **Una parte importante son alias del mismo sitio.** Los pares que más coaparecen en todo el histórico son `hive`/`hiveleak` (169 veces) y `killsec`/`killsecurity` (61): el mismo actor con dos nombres de expediente. Eso no es multi-extorsión, es ruido de normalización.

Y el resultado tras limpiar:

| Separación entre las dos primeras reclamaciones | Agrupaciones | Proporción |
|---|---|---|
| Menos de 1 hora | **0** | 0 % |
| 1 a 24 horas | 1 | 2 % |
| 1 a 7 días | 3 | 7 % |
| 7 a 30 días | 10 | 23 % |
| **Más de 30 días** | **30** | **68 %** |

**Ninguna colisión por debajo de una hora en el semestre.** El fenómeno real que domina el conjunto no es la disputa simultánea entre dos operaciones por una misma víctima, sino la **republicación con meses de retraso**. El expediente completo, con los cuatro fenómenos distintos que el endpoint mezcla bajo una sola etiqueta, es `CTI-2026-055`.

## E-3. Lo que esta fuente da y ninguna otra: el instante del desenmascaramiento

Cuarenta y una entradas del semestre conservan el título anterior y la marca de tiempo del cambio. Leídas juntas, describen un mecanismo que la cartera venía tratando como amenaza abstracta y que aquí queda fechado al segundo.

**El patrón dominante es la retirada de la máscara.** Varios actores publican primero un nombre parcialmente oculto y lo completan después:

| Actor | Antes | Después | Momento |
|---|---|---|---|
| `AuditTeam` | `Pe***CT` | `Pelican ICT` | 2026-11-09 08:04:33 |
| `AuditTeam` | `jl***om` | `jltrust.com` | 2026-11-09 08:04:24 |
| `AuditTeam` | `hn***rg` | `hnopvm.org` | 2026-11-09 08:04:17 |
| `AuditTeam` | `ro***up` | `roycegroup` | 2026-11-09 08:04:06 |
| `Doommageddon` | `A***** T******` | Nombre completo de una textil turca | 2026-11-04 07:03:46 |
| `everstake` | `caHidden names.com` | `carrollins.com` | 2026-11-09 15:06:09 |
| `EndZone` | `West-Com` | `West-Com Nurse Call Systems, Inc` | 2026-11-17 18:07:00 |

Los cuatro desenmascaramientos de `AuditTeam` ocurren **en veintisiete segundos**. No es una decisión caso por caso: es un cambio de estado del catálogo, probablemente el vencimiento de un plazo común.

**El segundo patrón es el contrario, y es el de un actor que la cartera ya tiene expediente abierto.** `Vortex` no revela identidades: añade cifras.

| Antes | Después |
|---|---|
| `APELLIS` | `Apellis Pharmaceuticals - 19,325 files - 307.64 GB` |
| `KOCH` | `Molex (Koch) - 1,803 files - 62.36 GB - 16,448,279 records` |
| `CARRINGTON` | `Mycorpass (Carrington Mortgage Services) - 74,682 files - 134.55 GB` |
| `ARTHREX - 700+ GB` | `Arthrex - 24,655,647 records - 20.90 GB` |

El último es el más informativo de los cuatro: **`700+ GB` se convierte en `20,90 GB`**. La estimación inicial era treinta y tres veces mayor que la cifra que el propio actor publica después. Eso es un dato duro sobre cómo graduar una reclamación de volumen recién publicada, y refuerza lo que `CTI-2026-050` dejó dicho sobre este actor.

**Y el tercer patrón es un accidente, con el valor que tienen los accidentes.** `nightspire` publicó una entrada con el nombre enmascarado, lo sustituyó por el nombre real a las **08:03:32** del 2 de noviembre, y **volvió a enmascararlo a las 08:03:39** — siete segundos después. Este informe no reproduce ese nombre, por la razón de `§3.4`. Lo que sí deja registrado es la inferencia: **el enmascaramiento de ese actor es deliberado, reversible y operado manualmente**, y el error de un operador abrió una ventana de siete segundos que la fuente capturó.

### E-3.1 Por qué esto importa a una víctima

El desenmascaramiento progresivo es la palanca de presión, y hasta ahora la cartera no podía decirle a nadie **cuánto dura la fase enmascarada**. Con este campo puede: `AuditTeam` mantuvo cuatro nombres ocultos y los reveló a la vez; `Doommageddon` hizo lo mismo con uno. Una organización que se encuentre publicada con el nombre parcialmente oculto **no está a salvo: está en la primera fase**, y la transición puede ser cuestión de días y ejecutarse en segundos.

## E-4. Decisiones que este informe pide

1. **Incorporar la fuente con los seis correctivos de `Anexo D` aplicados**, no como sustituto del rastreador que la cartera ya usa sino junto a él. Donde se pudo comparar, los recuentos difieren (SoulGroup 27 frente a 26; Vortex 29 frente a 35) y **ninguna de las dos es patrón de la otra**.
2. **Prohibir en la cartera el uso de la fecha de descubrimiento como fecha de aparición de un actor** sin la resta de `E-1.1`. Es el defecto que más fácilmente se cuela en un informe.
3. **No citar nunca la cifra de colisiones en menos de veinticuatro horas** de esta fuente. Está derivada de un campo que está mal en el 41 % de los casos.
4. **Añadir al recolector diario de la cartera la consulta de historial de título**, que es el dato de mayor valor y el más perecedero: registra un evento de segundos.
5. **Tratar el campo de reclamación retirada como no informativo**, y seguir obteniendo las retiradas por el método de `CTI-2026-048`: comparar recuentos de fuentes independientes.

---

# NIVEL OPERACIONAL

## O-1. Ficha de la fuente

| Campo | Valor |
|---|---|
| Nombre | cti.fyi |
| Interfaz | API REST, `/api/v1`, con OpenAPI 3.1.0 publicado |
| Autenticación | Clave de licencia en cabecera `X-License-Key` |
| Nivel usado | `community` |
| Límite declarado | 30 peticiones/minuto · 1.000 diarias |
| Capacidades activas | Enriquecimiento sí · Exportación **no** · Expediente: «overview» |
| Histórico | Sin límite declarado en el nivel |
| Licencia de contenido | CC BY-NC-SA 4.0 — **uso comercial requiere licencia aparte** |
| Catálogo | 425 grupos · 141 activos · 35.879 entradas |
| Última exploración declarada | 2026-11-19T21:08:11Z |

**La condición de licencia es una restricción operativa, no una nota al pie.** El contenido es de uso no comercial; cualquier empleo corporativo del material derivado exige licencia del proveedor. Este informe se emite con esa condición en su cabecera de distribución.

### O-1.1 Las tres bases temporales

Es la característica que distingue a esta fuente, y la que hace posible `KJ-1`:

| Campo | Qué es | Cobertura en el semestre |
|---|---|---|
| `discovered` | Cuándo lo vio el rastreador | **5.144 / 5.144 (100 %)** |
| `published` | Qué fecha declara el sitio de filtración | 3.806 / 5.144 (74 %) |
| `updated` | Cuándo cambió la entrada después | 865 / 5.144 (17 %) |

La cartera llegó a la distinción entre las dos primeras por medición propia y con esfuerzo, en `CTI-2026-046` y `CTI-2026-047`, donde documentamos que los recuentos de siete días divergen hasta un factor de 8,3 según la base elegida. **Esta fuente las expone separadas de fábrica**, y añade una tercera. Es su mayor aportación estructural.

## O-2. Defecto 2 — El campo de separación entre reclamaciones

Definición declarada: «horas entre las reclamaciones de los dos primeros grupos». Procedimiento de comprobación: para cada agrupación, tomar la primera reclamación **de cada grupo distinto**, ordenarlas y restar las dos primeras.

Resultado sobre 500 agrupaciones: **295 coinciden, 205 discrepan en más de una hora (41 %)**.

| Víctima | Declarado | Recalculado | Grupos |
|---|---|---|---|
| `hacla` | 0,0 h | **11.392,3 h** | cactus, dispossessor, lockbit3 |
| `miamimanagement` | 0,0 h | **18.368,3 h** | pear, play, sarcoma |
| `ferretornillos` | 0,0 h | **10.848,8 h** | j, krybit, l group |
| `proplastics` | 0,0 h | **2.591,3 h** | lockbit5, qilin, thegentlemen |
| `alltrucktransportation` | 0,0 h | **1.316,0 h** | qilin, spacebears |

El error apunta siempre en la misma dirección —declara cero donde hay meses— y arrastra al indicador booleano del que se deriva el recuento de 706. La hipótesis más económica es que el cálculo tome dos entradas **del mismo grupo** cuando éste tiene varias, pero **no se puede confirmar sin el código**, y así queda consignado.

## O-3. Defecto 3 — Expedientes duplicados por nomenclatura

El caso de `apt73` es el más instructivo porque **la propia fuente lo delata**: su ficha de perfil empieza «el grupo, autodenominado APT73 y después Bashe, surgió en abril de 2024». Y el catálogo tiene dos expedientes.

| Comprobación | Resultado |
|---|---|
| Entradas de `bashe` en el semestre | **0** |
| Entradas de `apt73` en el semestre | 79 |
| De ellas, descubiertas el 2026-10-07 | **77** |
| Rango de fechas de publicación que declaran | **2024-04-05 a 2026-07-27** |
| Solapamiento de títulos entre los dos expedientes | **0 %** |
| Títulos de los 11 sitios bajo `apt73` | «APT73» 4 · **«BASHE» 5** · sin título 2 |

La no intersección de títulos indica que los dos expedientes **se repartieron el catálogo** en lugar de duplicarlo, lo que significa que la suma de entradas puede ser correcta y la separación es arbitraria. En la práctica: `apt73` habría entrado en este lote como el actor de arranque más agresivo del semestre, **y no tuvo actividad en el semestre**. Fue retirado y sustituido por `safepay`.

El mismo defecto, medido sobre todo el histórico de reclamaciones cruzadas, produce los pares `hive`/`hiveleak` (169 coapariciones), `killsec`/`killsecurity` (61), `ragroup`/`raworld` (25) y `ransomed`/`ransomedvc` (2). Son alias, no colisiones.

## O-4. Defecto 4 — El campo muerto

La consulta por estado de reclamación acepta los valores `active` y `withdrawn`. Con `withdrawn`, sobre las 35.879 entradas del histórico completo y sin filtro de fecha, la respuesta es `{"total": 0, "count": 0}`.

Contraste con lo que sabemos por otra vía: en `CTI-2026-048` recogimos el análisis de Bitdefender sobre `n0n`, según el cual el grupo **retiró 126 de sus propias entradas**, pasando de 150 a un conjunto menor. El evento existe, es frecuente y es analíticamente valioso —una retirada es la señal más fuerte de que una reclamación era falsa o de que hubo pago—. **La fuente no lo registra, y su interfaz sugiere que sí.**

Es el defecto más peligroso de los seis porque **no produce un número raro que invite a comprobar, produce un cero que parece una respuesta**.

## O-5. Defecto 5 — La puntuación de confianza del enriquecimiento

| Campos duros poblados | Registros | Puntuación media | Mediana |
|---|---|---|---|
| 0 de 3 | 607 | **0,397** | 0,20 |
| 1 de 3 | 477 | 0,851 | 0,95 |
| 2 de 3 | 849 | 0,925 | 0,95 |
| 3 de 3 | 1.854 | **0,935** | 0,95 |

El campo **sí** separa los registros vacíos de los poblados, y eso es útil. Pero la distribución del conjunto está colapsada: **2.951 de 3.787 valores (77,9 %) son exactamente 0,95**, y el resto se reparte en cantidades residuales. Dentro del conjunto con datos, **el campo no ordena**.

Uso correcto: filtro binario para descartar registros sin resolver. Uso incorrecto: priorizar víctimas o graduar fiabilidad.

> **Corrección interna.** Este informe partió de una sospecha más fuerte —que la puntuación fuera arbitraria— apoyada en un registro con nombre canónico «Redacted Redacted» y puntuación 0,95. La medición la refutó: los registros con nombre anónimo son **cinco en 5.144**, de modo que el caso es anecdótico y la correlación con los campos duros es real.

## O-6. Defecto 6 — La hora de publicación

Veinte grupos declaran la fecha de publicación **sin hora** en el 90 % o más de sus entradas. Entre ellos, con cobertura del 100 %: `akira` (189/189), `nightspire` (97/97), `genesis` (50/50), `settra` (49/49), `pear` (49/49), `L Group` (28/28), `AuditTeam` (29/29), `Eclipse` (22/22), `BYOD` (21/21), `Climax Inc` (19/19).

| Medición | Pico a las 00:00 | Veces la media horaria |
|---|---|---|
| Sin filtrar | **35,7 %** | 8,6 |
| Excluyendo los 20 grupos sin hora | 20,8 % | **5,0** |

El filtro descarta el 19 % de los registros y **reduce el pico a la mitad sin eliminarlo**. La causa del residuo es que hay grupos que declaran hora de forma intermitente, y el criterio del 90 % no los captura.

La conclusión operativa es más dura que «aplíquese un filtro»: **una publicación genuina a medianoche es indistinguible de una fecha sin hora**. El campo no permite recuperar la distribución horaria real por ningún filtrado agregado. El análisis de huso horario sobre esta fuente es legítimo **sólo grupo a grupo y sólo en los que declaran hora de forma consistente**.

## O-7. El inventario de infraestructura

La ficha por grupo entrega la lista de sitios con FQDN, título, versión del servicio oculto, disponibilidad, estado y fecha de la última exploración. Es la base de los indicadores de `Anexo A`, y produce dos lecturas de interés inmediato.

**Primera: la forma de la dirección es una decisión del actor, y se puede cazar.** Los cuatro sitios activos de `krybit` empiezan por `krybit` o `krybie`. Un prefijo legible en una dirección de servicio oculto versión 3 **exige fuerza bruta sobre la clave**: es esfuerzo deliberado, y convierte el prefijo en patrón de búsqueda para localizar infraestructura nueva del mismo actor. `BrainCipher`, con **cincuenta y cuatro sitios registrados**, usa direcciones sin ningún prefijo legible: la decisión opuesta, y seguramente consciente.

**Segunda: un actor expone un dominio en Internet abierto.** Bajo `apt73` figura `eraleignews.com`, fuera de Tor. Es el indicador de mayor valor del inventario, por ser el único que no requiere Tor para observarse.

### O-7.1 Un defecto menor y una advertencia

Los campos de disponibilidad y de estado **se contradicen en 25 de los 81 sitios de los cinco actores (31 %)**: 21 casos declaran disponible y estado «offline», y 4 declaran no disponible y estado «online». Cuál de los dos manda no es determinable desde fuera. Para los indicadores de este informe se usó el campo de estado y se consignó la fecha de última exploración junto a cada valor.

---

## O-8. La cuarta fuente: CTIWatch

**Añadido en v1.1.** Evaluada el 19 de noviembre de 2026 sobre sus páginas
públicas.

| Campo | Valor |
|---|---|
| Nombre | CTIWatch — declarado «A Lear Security product» |
| Acceso | Páginas públicas. **Su `robots.txt` prohíbe `/api/`** |
| Señal de licencia | `Content-Signal: search=yes, ai-input=yes, ai-train=no` |
| Catálogo de actores | 10.957 entidades, agregando Malpedia con identificador |
| **Catálogo de CVE** | **409.830**, con CVSS, EPSS y estado de explotación |
| **Indicadores** | **2.322.362**, con tipo, confianza, fuente, etiquetas y fecha |
| Secciones | `/threats` · `/vulnerabilities` · `/iocs` · `/victims` · `/reports` · `/alerts` |

**La restricción de acceso se respeta y conviene dejarla escrita.** El
`robots.txt` de esta fuente autoriza expresamente el rastreo y la cita por
agentes de búsqueda y de recuperación, y **prohíbe `/api/`**. Toda la medición
de este apartado se hizo sobre páginas públicas.

### O-8.1 Lo que aporta, y es nuevo para la cartera

**El catálogo de vulnerabilidades es la aportación de más valor.** Cuarenta
informes de esta cartera citan identificadores CVE, y ninguno ha podido
acompañarlos de **EPSS** —la probabilidad estimada de explotación— ni de un
estado declarado de armamentización. Esta fuente ofrece los cuatro estados
`ACTIVE EXPLOITATION`, `WEAPONIZED`, `POC AVAILABLE` y `NO KNOWN EXPLOIT`, que
es lo que separa una lista de CVE de una cola de parcheo ordenada.

**El catálogo de indicadores procede de telemetría propia**, principalmente de
señuelos T-Pot, con el detalle del número de impactos, los módulos que lo
detectaron y los puertos. Es de la misma naturaleza que la fuente de
`CTI-2026-044`, y los cinco controles del `Anexo D` de aquel informe se le
aplican íntegros.

### O-8.2 Lo que no se puede usar: las fichas de actor

Seis fichas comprobadas, seis con la cabecera contradiciendo a la prosa de la
misma página:

| Actor | Cifra en cabecera | Cifra en la prosa | Diferencia |
|---|---|---|---|
| `qilin` | 2.602 | 2.059 | **543** |
| `akira` | 1.717 | 1.578 | 139 |
| `dragonforce` | 673 | 628 | 45 |
| `safepay` | 618 | 521 | 97 |
| `krybit` | 183 | **78** | **105** |
| `braincipher` | 110 | **64** | 46 |

Y tres defectos más:

1. **El campo «visto por última vez» vale `Mar 17, 2026` en cuatro actores
   distintos** —qilin, akira, safepay y dragonforce—, todos con actividad
   medida en noviembre. Es un valor por omisión, no una observación. Es el
   mismo defecto de clase que la **trampa del valor por omisión** de
   `CTI-2026-044` `§O-2.2`.
2. **La clasificación de motivación es incorrecta en un caso comprobable:**
   `krybit` figura como motivado por **espionaje**, mientras la propia
   descripción de la ficha lo define como RaaS con reparto de ingresos 80/20
   entre afiliados, que es financiero por definición.
3. **Incoherencia temporal interna:** la ficha de `krybit` declara «último
   ataque registrado el 2026-07-17 y última actividad el 2026-04-18». La
   última actividad precede al último ataque.

**La fuente declara el origen de esa prosa**, y conviene reconocérselo: cada
ficha termina con «generado por la tubería de análisis de CTIWatch a partir de
los datos seguidos de este actor». No se presenta como análisis humano. **Por
eso el defecto no es de honradez sino de aptitud**: una ficha generada que
contradice su propia cabecera no sirve para perfilar, y sí sirve —como se usó
en `CTI-2026-056` `§E-1.2`— para acotar un orden de magnitud.

### O-8.3 Y una colisión de nombres que casi se cuela

La ficha de `soul` de esta fuente presenta, bajo el mismo encabezado, dos
objetos distintos: el perfil dice «familia de malware seguida por Malpedia,
identificador `win.soul`» —una entrada de catálogo de software malicioso— y la
evaluación habla de una operación de extorsión con veinticinco víctimas en
noviembre de 2026. **No hay nada que indique que sean lo mismo**, y la fecha de
actualización del registro de Malpedia es de octubre de 2025, trece meses antes
de que el actor de extorsión apareciera.

**Si esta ficha se hubiera tomado como corroboración del expediente
`CTI-2026-053`, el error habría sido grave:** habría convertido una familia de
malware preexistente en el linaje de una marca de extorsión nueva. Es el cuarto
correctivo del `Anexo D` —comprobar los alias antes de tratar dos nombres como
el mismo objeto— aplicado a la inversa: **aquí había que comprobar que un mismo
nombre no fueran dos objetos.**

## O-9. Tres fuentes, tres fechas, quince días

**Añadido en v1.1.** La incorporación de una tercera fuente permitió una
comprobación que ninguna de las dos anteriores hacía posible: **fechar el mismo
hecho con tres observadores independientes.**

El hecho es la tanda inicial de publicaciones del actor `soul`, el objeto de
`CTI-2026-053`.

| Fuente | Fecha que atribuye | Cifra de entradas |
|---|---|---|
| ransomware.live (`CTI-2026-053` v1.0) | **2026-11-19** | 26 |
| cti.fyi | **2026-11-11** | 27 |
| CTIWatch | **2026-11-04** | 25 |

**Quince días entre los extremos, para un hecho de hace dos semanas y un actor
que no existía hace un mes.** Las tres cifras de entradas son casi iguales
—26, 27, 25—, lo que indica que las tres están mirando el mismo catálogo. Lo
que difiere es **cuándo lo vio cada una**.

Esto cierra el argumento de `KJ-1` de la forma más económica posible. Allí la
prueba de que la fecha de descubrimiento es del observador y no del adversario
exigió restar dos campos sobre cinco mil entradas. Aquí basta comparar tres
fuentes sobre un solo actor:

> **Si tres rastreadores fechan la misma publicación con quince días de
> diferencia, ninguna serie temporal construida sobre uno solo de ellos
> describe al adversario.** Describe el calendario de sondeo de ese rastreador.

Y tiene una consecuencia práctica inmediata para esta cartera: **toda cifra de
«víctimas en los últimos siete días» que cualquiera de estas fuentes publique
es, en el mejor de los casos, aproximada a ±1 semana** — lo que es del mismo
orden que la ventana que pretende medir. Refuerza lo que `CTI-2026-046`
`Anexo D` ya había establecido sobre los rankings de siete días, y añade el
motivo tercero: no sólo divergen las dos bases de fecha de una fuente, sino que
**la misma base diverge entre fuentes**.

## 14. Brechas de inteligencia y requisitos de colección

**G-1. No conocemos el calendario de incorporación de sitios de la fuente.** Es la causa de `KJ-1` y lo único que convertiría la corrección de este informe en un dato exacto en lugar de una inferencia bien apoyada.
→ **I-1.** Preguntar al proveedor si publica un registro de alta de sitios vigilados. **Disparador de reevaluación:** cualquier día del semestre siguiente con más de cinco estrenos de grupo.

**G-2. No sabemos por qué `delta_hours` falla.** La hipótesis del cálculo sobre entradas del mismo grupo es la más económica y no está confirmada.
→ **I-2.** Comunicar el defecto al proveedor con los cinco casos de `O-2`. **Disparador:** publicación de una versión nueva de la API.

**G-3. El paquete STIX 2.1 no se evaluó** por restricción de licencia, y es donde la fuente dice publicar técnicas de ATT&CK. Es la brecha más relevante para el nivel táctico de la cartera.
→ **I-3.** Evaluar si el nivel de evaluación gratuito permite medirlo.

**G-4. No sabemos si el campo de revisión registra cambios sustantivos o también cambios triviales del HTML.** `metaencryptor` presenta revisión en 39 de 39 entradas, proporción que hace sospechar artefacto.
→ **I-4.** Comparar, para una muestra de diez entradas revisadas, el contenido antes y después. **Disparador:** antes de usar el campo para medir comportamiento de actor.

**G-5. No sabemos si el historial de título captura todos los cambios o sólo los ocurridos entre dos exploraciones.** El caso de los siete segundos de `nightspire` demuestra que la resolución puede ser muy fina, pero no que sea completa.
→ **I-5.** Medir el intervalo entre exploraciones sucesivas del mismo sitio. **Disparador:** inmediato, porque condiciona `I-4` de `Anexo D`.

**G-6. Los recuentos no se reconcilian con el otro rastreador de la cartera** y no sabemos por qué.
→ **I-6.** Para tres actores con expediente, comparar entrada por entrada e identificar si la diferencia es de deduplicación o de cobertura.

**G-7. Añadida en v1.1. No se evaluó la calidad del catálogo de CVE de CTIWatch**, que es su aportación de más valor y la primera fuente de EPSS de la cartera.
→ **I-7.** Contrastar una muestra de veinte CVE de informes ya emitidos contra la referencia oficial de EPSS y comprobar la concordancia de CVSS y del estado de explotación. **Disparador:** antes de citar un EPSS de esta fuente en un informe.

**G-8. Añadida en v1.1. No sabemos cuántas de las 2.322.362 entradas de indicadores de CTIWatch son telemetría propia de señuelos y cuántas son reempaquetado de terceros.** Lo observado apunta a T-Pot propio, pero sobre una muestra pequeña.
→ **I-8.** Agrupar por campo de fuente y medir la proporción. **Disparador:** antes de ingerir cualquier indicador de ese catálogo.

**G-9. Añadida en v1.1. No sabemos si la discrepancia de quince días de `O-9` es típica o excepcional.** Se midió sobre un actor.
→ **I-9.** Repetir el cruce de tres fuentes sobre cinco actores más con fecha de aparición conocida. **Es la medición que convertiría `KJ-9` de observación en estadística**, y la más valiosa de las nueve.

---

# ANEXOS

## Anexo A — Indicadores

### A.1 — Infraestructura de los cinco actores con expediente en este lote

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| domain | `eraleignews.com` | **Único sitio en Internet abierto del inventario**, registrado bajo `apt73`/BASHE. Observable sin Tor | Alta como registro | 90 días | **Vigilancia**. Verificar antes de bloquear |
| domain | `krybitxdpxohsmjooeb3gbgpmdddreh6mnflzac6bnezz74b7yje67yd.onion` | Sitio activo de krybit al 2026-11-19 | Alta | 90 días | Vigilancia |
| domain | `krybitx3fh5krdnhegyp2ob3lhizsaiadturtio3ginf7it5gsdgu2yd.onion` | Sitio activo de krybit | Alta | 90 días | Vigilancia |
| domain | `krybitqsdzwmhnitvwuhvsntfgf2wrhxveyxroxpc44c6gkft2cqldyd.onion` | Sitio activo de krybit | Alta | 90 días | Vigilancia |
| domain | `krybieodq754vlwufrsuxaswxb5zpxyibaawmed2jaduoz2e5m56hmid.onion` | Sitio activo de krybit, **prefijo `krybie` y no `krybit`** | Alta | 90 días | Vigilancia |
| pattern | **Prefijo legible `krybit` / `krybie` en dirección de servicio oculto v3** | **Indicador de caza.** Un prefijo legible exige fuerza bruta sobre la clave: permite localizar infraestructura nueva del mismo actor por patrón (`O-7`) | **Alta como método** | Mientras mantenga la práctica | **Búsqueda proactiva** |
| domain | `7t3zi3e7ki6iseun77ofqtr6wmbpgnpc2ada6gstcxp54lw6q2zb7jad.onion` | Sitio de filtración de Booba Project, activo | Alta | 90 días | Vigilancia |
| domain | `culappkcuogv2omb37253e236mvmsfzvl4yw3p3incyzeoixhc6ocxqd.onion` | «Booba Storage», activo. **Almacenamiento separado del blog** | Alta | 90 días | Vigilancia |
| domain | `yqhecvqtdvq6p7duqcgw2qca77spbgakxcoibtx6zpvfshltsbbbhfqd.onion` | **Único sitio de Storm**, activo | Alta | 90 días | Vigilancia |
| domain | `basherq53eniermxovo3bkduw5qqq5bkqcml3qictfmamgvmzovykyqd.onion` | Sitio BASHE activo bajo expediente `apt73` | Alta | 90 días | Vigilancia |
| domain | `basherykagbxoaiaxkgqhmhd5gbmedwb3di4ig3ouovziagosv4n77qd.onion` | Sitio BASHE activo | Alta | 90 días | Vigilancia |
| artefacto | **54 sitios registrados para BrainCipher, 6 activos, ninguno con prefijo legible** | Contraste deliberado con krybit. **Rotación de infraestructura a gran escala** | Alta como recuento | 90 días | Análisis |
| artefacto | **5 sitios de safepay, 0 activos al 2026-11-19** | Con última entrada el 2026-11-07. **Posible cese o migración** (`CTI-2026-058`) | Alta como observación | **Reevaluar en 14 días** | Vigilancia |

### A.2 — Patrones de desenmascaramiento

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| pattern | **Entrada con nombre parcialmente enmascarado del tipo `Pe***CT` o `A***** T******`** | **La primera fase de la extorsión, no un estado estable.** `AuditTeam` reveló cuatro nombres en 27 segundos (`E-3`) | **Alta** | Mientras los actores mantengan la práctica | **Comprobación por la víctima.** Una organización así publicada está en fase inicial |
| pattern | **Revisión de título que añade cardinalidades: ficheros, GB, registros** | El patrón de `Vortex`. **`700+ GB` pasó a `20,90 GB` en la misma entrada**: la estimación inicial era 33 veces mayor | Alta como observación | Igual | **Graduación de reclamaciones de volumen** |
| pattern | **Máscara → nombre → máscara en segundos** | Observado una vez, en 7 segundos. **Prueba de que el enmascaramiento es deliberado, reversible y manual** | Moderada por n=1 | Sin caducidad | Análisis. **No se reproduce el nombre afectado** (`§3.4`) |
| artefacto | **41 entradas con historial de título en 5.144 (0,8 %)** | El dato más perecedero de la fuente: registra eventos de segundos | Alta como recuento | 60 días | **Añadir al recolector diario** |

### A.3 — Defectos de la fuente, como indicadores de higiene

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| artefacto | **Retraso mediano publicación→descubrimiento > 30 días en el estreno de un grupo** | **El discriminante de `KJ-1`.** Separa grupo nuevo de sitio recién vigilado | **Alta como método** | Sin caducidad | **Aplicar antes de contar actores nuevos** |
| artefacto | **Día con más de 5 estrenos de grupo** | Firma del escalón de cobertura. Cinco días del semestre | Alta | Sin caducidad | **Descartar para series temporales** |
| artefacto | **`delta_hours` = 0,0 en una agrupación con reclamaciones separadas por meses** | El defecto de `O-2`, en 41 % de los casos | Alta | Hasta nueva versión de la API | **No citar el recuento de colisiones <24 h** |
| artefacto | **Consulta de reclamaciones retiradas que devuelve 0 sobre 35.879** | El campo muerto de `O-4`. **Induce la conclusión contraria** | Alta | Hasta nueva versión | **Tratar como no informativo** |
| artefacto | **Puntuación de confianza = 0,95 en el 77,9 % de los registros** | Detecta ausencia; no ordena (`O-5`) | Alta | Sin caducidad | **Uso binario únicamente** |
| artefacto | **Pico de publicaciones a las 00:00 del 35,7 %, 8,6 veces la media** | 20 grupos declaran fecha sin hora. **Irrecuperable por filtrado** (`O-6`) | Alta | Sin caducidad | **Prohibido el análisis de huso horario agregado** |
| artefacto | **Disponibilidad y estado del sitio contradictorios en 31 % de los casos** | 25 de 81 sitios (`O-7.1`) | Alta | Sin caducidad | **Consignar siempre la fecha de exploración** |
| artefacto | **Tres fuentes fechan la misma tanda el 4, el 11 y el 19 de noviembre** | `O-9`. **Quince días para un hecho de hace dos semanas** | **Alta** | Sin caducidad | **Cruzar toda fecha que sostenga un juicio** |
| artefacto | **Ficha de actor cuya cabecera y prosa dan cifras distintas** | CTIWatch, 6 de 6 casos (`O-8.2`) | Alta | Sin caducidad | **No usar para perfilar. Sirve para orden de magnitud** |
| artefacto | **Campo «visto por última vez» con la misma fecha en cuatro actores distintos** | `Mar 17, 2026` en qilin, akira, safepay y dragonforce. **Valor por omisión** | Alta | Sin caducidad | **Descartar el campo** |
| artefacto | **Un mismo nombre designando una familia de Malpedia y una operación de extorsión** | La ficha de `soul` (`O-8.3`). **Trece meses de separación entre los dos objetos** | Alta | Sin caducidad | **Comprobar identidad antes de corroborar** |

## Anexo B — Fuentes y valoración

| # | Fuente | Grado | Qué aportó | Salvedad |
|---|---|---|---|---|
| 1 | API de cti.fyi, nivel community, consultada el 2026-11-19 | **Medición propia** sobre datos de proveedor | Todo el material cuantitativo | Es el objeto evaluado: su propia descripción no se usa como prueba de sí misma |
| 2 | Especificación OpenAPI 3.1.0 publicada por la fuente | Proveedor | Superficie, parámetros y límites declarados | Declara capacidades que la licencia community no sirve |
| 3 | Fichas de perfil por grupo de la misma fuente | **Proveedor, con indicio de redacción sintética** | Linaje declarado de BrainCipher, krybit, Storm, apt73 | El registro del texto y los caracteres de espacio fino sugieren generación automática. **Se cita como aserción del proveedor, nunca como hecho** |
| 4 | `CTI-2026-046` a `CTI-2026-053` de esta cartera | Propio | Los recuentos con los que se contrastaron los de esta fuente | — |
| 5 | Análisis de Bitdefender sobre n0n, recogido en `CTI-2026-048` | Proveedor | La prueba independiente de que las retiradas existen (`O-4`) | Recogido de segunda mano en nuestro propio informe |
| 6 | Licencia CC BY-NC-SA 4.0 declarada por la fuente | Oficial del proveedor | La restricción de uso comercial de `O-1` | — |
| 7 | **CTIWatch**, páginas públicas `/threats`, `/vulnerabilities`, `/iocs`, `/alerts` y seis fichas de actor (2026-11-19). **Añadida en v1.1** | **Medición propia** sobre datos de proveedor | La evaluación de `O-8`, la tercera fecha de `O-9`, y la corroboración de orden de magnitud usada en `CTI-2026-056` `§E-1.2` | **Su `robots.txt` prohíbe `/api/`**: sólo se consultaron páginas públicas. **Sus fichas de actor se contradicen consigo mismas en 6 de 6 casos** y su prosa está generada automáticamente, hecho que la propia fuente declara |
| 8 | `CTI-2026-053` v1.0 y el otro rastreador de la cartera | Propio | La primera de las tres fechas de `O-9` | — |

**Sobre el grado de las fichas de perfil.** Las descripciones de grupo de esta fuente son extensas, afirmativas y uniformes en estilo. Dicen, por ejemplo, que BrainCipher es «derivado del constructor filtrado de LockBit 3.0», que krybit es «derivado de Babuk con reparto 80/20» y que Storm «surgió en 2021». Ninguna de esas afirmaciones se verificó, ninguna lleva referencia, y el registro textual apunta a redacción automática. **En los cinco expedientes de actor de este lote se citan como declaración del proveedor y se marcan como no corroboradas.**

## Anexo C — Léxico de probabilidad y confianza

Se emplea ICD 203. **Casi con certeza** ≥99 % · **muy probable** 80–95 % · **probable** 55–80 % · **posible** 40–60 % · **improbable** 20–45 % · **muy improbable** 5–20 %. La **confianza** es independiente de la probabilidad y califica la base de prueba: *alta* cuando hay medición reproducible, *moderada* cuando hay inferencia bien apoyada, *baja* cuando hay una sola observación. La categoría **NO EVALUABLE**, incorporada en `CTI-2026-053`, se aplica aquí a los once grupos sin ninguna fecha de publicación.

## Anexo D — Los seis correctivos, antes de citar esta fuente

Procedimiento de aplicación obligatoria. Coste total estimado: **quince minutos** la primera vez, y después está automatizado.

**1. Antes de contar actores nuevos, restar las fechas.** Para cada grupo cuyo estreno caiga en la ventana, calcular la mediana de `discovered − published`. Si supera 30 días, **el grupo no es nuevo: es recién vigilado**. Si no hay ninguna fecha de publicación, el grupo es **NO EVALUABLE**, no «nuevo». Y descartar el primer día de la ventana, que es artefacto del recorte propio.

**2. Antes de usar una serie temporal, marcar los días de escalón.** Cualquier día con más de cinco estrenos de grupo o con más de cinco veces la mediana de entradas es candidato a incorporación de cobertura. Comprobarlo con el criterio 1 y, si se confirma, **excluirlo de la serie o anotarlo**.

**3. No citar el recuento de colisiones en menos de veinticuatro horas.** Está derivado de un campo que discrepa de su definición en el 41 % de los casos. Si se necesita la cifra, **recalcularla** tomando la primera reclamación de cada grupo distinto.

**4. Antes de tratar dos grupos como distintos, comprobar los alias.** Dos señales bastan: coaparición alta en reclamaciones cruzadas, y títulos de sitio que no coinciden con el nombre del expediente. **La ficha de perfil del propio proveedor puede decir que son el mismo**, como en el caso de `apt73`.

**5. No preguntar a esta fuente por reclamaciones retiradas.** Devuelve cero siempre. Obtenerlas comparando recuentos de fuentes independientes, que es el método de `CTI-2026-048`.

**6. No hacer análisis de huso horario sobre la hora de publicación.** Ni agregado ni filtrado. Sólo grupo a grupo, y sólo en los que declaran hora de forma consistente; comprobarlo contando qué proporción de sus entradas cae exactamente en 00:00:00.

**7. Añadido en v1.1 — antes de fechar un hecho, mirar si otra fuente lo fecha igual.** Para el mismo actor, tres rastreadores dieron tres fechas separadas por quince días (`O-9`). **Una fecha de descubrimiento de una sola fuente no es una fecha**, es una observación de esa fuente. Si la fecha importa al juicio, hay que cruzarla; si no se puede cruzar, hay que escribir «observado por X el día D», nunca «ocurrió el día D».

**8. Añadido en v1.1 — antes de tratar dos registros con el mismo nombre como el mismo objeto, comprobar que lo son.** El correctivo 4 avisa del caso en que dos nombres son un actor. **Éste es el inverso**: en CTIWatch, la ficha de `soul` mezcla una familia de malware de Malpedia actualizada en octubre de 2025 con una operación de extorsión aparecida en noviembre de 2026 (`O-8.3`). **La coincidencia de nombre no es evidencia de identidad en ninguna de las dos direcciones.**

> **El correctivo más barato y más discriminante es el primero**, igual que en el triaje de `CTI-2026-042` lo era preguntar cómo contacta la víctima. Una resta de dos campos separa catorce actores reales de cincuenta y cuatro artefactos.

## Anexo E — Marcos de referencia empleados

ICD 203 para el lenguaje estimativo. Escala de Almirantazgo para la valoración de fuentes, con los grados propios de la cartera —judicial, oficial, proveedor, propio, declaración del adversario, medición propia—. TLP 2.0 y PAP para la clasificación. El método de triaje de actor nuevo de `CTI-2026-042` `Anexo D`. La escala de prueba de ocho niveles de `CTI-2026-048` `Anexo D`, aplicada aquí a los perfiles de proveedor. Los cinco controles para telemetría viva como fuente de `CTI-2026-044` `Anexo D`, de los que este informe es la aplicación a una fuente de catálogo en lugar de a una de telemetría.

## Anexo F — Paquete legible por máquina

Consultas que reproducen cada medición. Todas requieren la cabecera `X-License-Key`.

| Medición | Consulta |
|---|---|
| Dimensionado | `GET /api/v1/stats` |
| Ventana completa | `GET /api/v1/posts?since=2026-05-19&limit=500&offset=N&sort=discovered`, N de 0 a 5000 |
| Serie diaria | `GET /api/v1/stats/history?days=180&interval=daily` |
| Reclamaciones cruzadas | `GET /api/v1/cross-claims?limit=500&offset=N`, N de 0 a 1500 |
| Revisiones | `GET /api/v1/posts?revisions_only=true&since=2026-05-19&limit=500&sort=updated` |
| El campo muerto | `GET /api/v1/posts?claim_status=withdrawn&limit=500` → `total: 0` |
| Ficha e infraestructura | `GET /api/v1/groups/{nombre}` |
| Facetas | `GET /api/v1/web/facets` → 20 sectores, 178 países |
| Límite de licencia | `GET /api/v1/stix2?group=X&days=180` → **403** |

**Cadencia empleada:** una petición cada 2,5 segundos, equivalente a 24 por minuto sobre un techo declarado de 30. Total del día: unas 35 peticiones de una cuota de 1.000.

## Anexo G — Control de cambios

| Versión | Fecha | Qué cambió | Qué juicio se movió |
|---|---|---|---|
| 1.0 | 2026-11-19 | Emisión inicial. Los seis defectos de cti.fyi, el recuento corregido de 68 a 14 actores nuevos y los tres datos únicos | — |
| 1.1 | 2026-11-19 | **Amplía el informe de una fuente a tres, y añade el hallazgo más limpio del expediente.** Incorpora `KJ-9` y `§O-9`: **tres rastreadores fechan la misma tanda de publicaciones con quince días de diferencia** (4, 11 y 19 de noviembre), lo que convierte `KJ-1` de inferencia sobre 5.144 entradas en principio demostrable sobre una. Incorpora `KJ-10` y `§O-8` con la evaluación de **CTIWatch**: aporta 409.830 CVE con EPSS y estado de explotación —primera fuente de priorización de la cartera— y 2,3 millones de indicadores de telemetría propia, pero **sus fichas de actor se contradicen consigo mismas en 6 de 6 casos** y no son utilizables para perfilar. Documenta en `§O-8.3` una **colisión de nombres que casi se tomó por corroboración**. Añade los correctivos **7 y 8** al `Anexo D`, las brechas `G-7` a `G-9`, y dos fuentes al `Anexo B`. **Ningún juicio de v1.0 se retira** | `KJ-1` se refuerza con una segunda vía de prueba |

## Anexo H — Realimentación del consumidor

Este informe se corrige si se recibe: evidencia de que alguno de los seis defectos no se reproduce; el calendario de incorporación de sitios de la fuente, que convertiría la inferencia de `KJ-1` en dato; un caso de reclamación retirada que la fuente **sí** registre, que refutaría `KJ-4`; o la reconciliación entre sus recuentos y los del otro rastreador de la cartera, que cerraría `G-6`.

Los disparadores de reevaluación están en `§14`. El más inmediato es **`I-5`**, medir el intervalo entre exploraciones, porque de él depende saber si el historial de título captura todos los desenmascaramientos o sólo una muestra.
