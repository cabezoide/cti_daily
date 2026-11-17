---
tlp: "TLP:CLEAR"
pap: "PAP:AMBER"
id: "CTI-2026-025"
version: "1.0"
tipo: "Perfil de actor + evaluación de pertinencia regional"
foco_regional: "Ucrania (único teatro documentado) · Chile y Latinoamérica: exposición indirecta y transferencia de método"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "Gamaredon (Armageddon · Primitive Bear · ACTINIUM · Shuckworm · Aqua Blizzard · IRON TILDEN · DEV-0157 · NastyShrew · G0047)"
fecha: "2026-11-17"
caduca: "2027-01-16"
autor: "Célula CTI"
distribucion: "Elaborado íntegramente con fuentes abiertas TLP:CLEAR: el whitepaper «Gamaredon in 2025» de ESET (25 de junio de 2026), su repositorio público de indicadores, el informe de telemetría de Trellix de noviembre de 2026 y el ESET APT Activity Report Q2–Q3 2026. Difusión libre, conservando la atribución de las fuentes y las salvedades metodológicas de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-025

## El actor número uno del ranking de telemetría global de noviembre de 2026 no tiene una sola víctima documentada fuera de Ucrania, y ese desajuste es el informe

### Trellix le atribuye el 9,03 % de toda la actividad estatal observada y el 19,88 % de las detecciones en EE. UU.; ESET, que le dedica un whitepaper anual completo, afirma que en 2025 atacó **exclusivamente** instituciones gubernamentales y militares ucranianas. Las dos cosas no pueden ser verdad del mismo modo, y de cuál sea falsa depende cómo se prioriza

> **Regla de oro del producto:** todo párrafo debe responder a un requisito de
> inteligencia (PIR) y habilitar una decisión. Si un párrafo no cambia lo que
> alguien va a hacer, va al anexo o se borra.

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-025` |
| Versión / fecha | `1.0` — 2026-11-17 |
| Tipo de producto | Perfil de actor más **evaluación de pertinencia regional**. La segunda mitad es la que justifica el producto: el actor es irrelevante para nuestra geografía como amenaza directa y muy relevante como fuente de método |
| Niveles cubiertos | Estratégico · Operacional · Táctico · Técnico |
| Foco regional | **Ninguno documentado en la región.** El informe se escribe por tres razones: el actor encabeza el ranking de telemetría que alimenta las herramientas de priorización del mercado; su modelo de infraestructura ya está en uso por actores que sí operan aquí; y explota una vulnerabilidad de WinRAR que nos afecta igual que a cualquiera |
| Marcado de difusión | `TLP:CLEAR` · `PAP:AMBER` |
| Clasificación interna | Público — apto para difusión abierta |
| Requisitos atendidos | `PIR-01`, `PIR-04`, `PIR-07`, `PIR-10`, `PIR-12` |
| Solicitante / consumidor primario | Célula CTI (producción propia) · Jefatura de SOC · Ingeniería de Detección |
| Ventana de observación | 2025-01-01 → 2026-09-30 (whitepaper de ESET sobre 2025, ampliado con el periodo abril–septiembre de 2026 del informe trimestral) |
| Base de colección | 4 fuentes externas de primera mano · **sin telemetría propia** |
| Autor (analista) | Célula CTI |
| Revisión por pares | Pendiente |
| Aprobación | Pendiente |
| Caducidad / revisión | **2027-01-16 — 60 días, deliberadamente más corto que los 92 habituales de esta cartera.** Véase §3.5: la infraestructura de este actor rota en días y el Anexo A envejece más rápido que el informe |
| Productos relacionados | `CTI-2026-018` (abuso de TLD: este actor registró 189 dominios `.ru` en 2025) · `CTI-2026-020` y `CTI-2026-022` (actores regionales que usan el mismo modelo de servicios legítimos) · `CTI-2026-026`, `CTI-2026-027`, `CTI-2026-028` (lote de noviembre de 2026) |
| Paquete legible por máquina | `ioc_index.csv` del repositorio · sin bundle STIX propio |

> ⚠ **Limitación estructural.** Este informe **no incorpora telemetría propia**.
> La sección §O-4 (nuestra exposición) queda sin evaluar y se entrega como
> cuestionario. En un actor cuya victimología documentada no nos incluye, esa
> limitación tiene menos peso que en el resto de la cartera: no se trata de
> averiguar si estamos comprometidos por Gamaredon, sino de si los **patrones**
> que Gamaredon populariza están ocurriendo en nuestra red por cuenta de otro.

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** Gamaredon es, según la única fuente que le dedica análisis de primera mano sostenido, un actor de teatro único: Ucrania. El whitepaper de ESET de 25 de junio de 2026 abre sus hallazgos clave con una frase sin matices: «a lo largo de 2025, Gamaredon atacó **exclusivamente** instituciones gubernamentales y militares en Ucrania». La sección de victimología repite la misma palabra. No hay un solo país adicional en 47 páginas. Valoramos **muy probable** *(80–95 %)* que la victimología de 2025 sea efectivamente exclusiva de Ucrania. **Confianza: alta.** *Base:* fuente única pero con telemetría de producto desplegada, seguimiento continuado desde 2013 y tres whitepapers anuales consecutivos; la afirmación es explícita y repetida, no una inferencia nuestra.

**KJ-2.** Y sin embargo, el informe de telemetría de Trellix de noviembre de 2026 lo sitúa como **el actor estatal más prevalente del mundo**, con el 9,03 % de toda la actividad observada entre abril y septiembre de 2026, por delante de APT36 (7,84 %) y Mustang Panda (7,52 %), y le atribuye el **19,88 % de las detecciones en Estados Unidos**. En el desglose trimestral sube al 10,72 % en Q3. Estas dos lecturas del mismo actor no son conciliables sin una explicación, y la explicación importa más que cualquier indicador de este informe. Valoramos **probable** *(55–80 %)* que la diferencia se explique por **qué mide cada fuente** y no por una discrepancia de hecho sobre dónde opera el actor. **Confianza: moderada.** *Base:* razonamiento nuestro sobre la metodología declarada de ambas fuentes; ninguna de las dos aborda la contradicción. Desarrollo en §E-1 y §O-6.

**KJ-3.** La hipótesis que retenemos sobre esa contradicción es que el ranking de Trellix cuenta **detecciones de firma, no intrusiones**, y que Gamaredon es el actor estatal más ruidoso y peor ocultado del mundo. Su arsenal completo está escrito en VBScript y PowerShell —ESET lo declara explícitamente: todas las herramientas del whitepaper están en uno de esos dos lenguajes—, se distribuye por correo masivo en 35 campañas anuales, propaga por USB y unidades de red compartidas, y lleva trece años con la misma familia de detección (`Pterodo`). Un actor así genera volúmenes de detección desproporcionados a su alcance real: cada LNK copiado en cada pendrive cuenta. Valoramos **probable** *(55–80 %)* que ésta sea la explicación principal. **Confianza: moderada.** *Base:* inferencia nuestra a partir del arsenal documentado y del modelo de propagación; es consistente con ambas fuentes y no requiere que ninguna mienta.

**KJ-4.** La consecuencia operativa es la que debe leerse dos veces: **un actor que encabeza el ranking de prevalencia puede ser simultáneamente irrelevante para nuestra priorización**, y las herramientas que ordenan amenazas por volumen de telemetría no distinguen esos dos casos. Quien alimente su proceso de priorización con el ranking de noviembre de 2026 pondrá a Gamaredon por delante de actores que sí tienen víctimas documentadas en la región —los de `CTI-2026-020`, `CTI-2026-021`, `CTI-2026-022` y `CTI-2026-024`—. Valoramos **casi con certeza** *(95–99 %)* que ese error de priorización se esté produciendo en el mercado. **Confianza: alta.** *Base:* es una propiedad del instrumento, no una predicción: el ranking ordena por porcentaje de detección y publica ese orden como «los más activos».

**KJ-5.** Lo que sí es transferible —y es la razón técnica de este informe— es el **modelo de infraestructura**, que ESET documenta con un detalle que no existe para ningún actor regional. Gamaredon dejó de depender de servidores propios: esconde su mando y control detrás de cuatro servicios de túnel y *worker* de terceros (`trycloudflare.com`, `workers.dev`, `devtunnels.ms`, `loophole.site`, usados en rotación con dos de reserva), resuelve a cuál conectarse mediante *dead drops* en nueve servicios legítimos distintos (Telegra.ph, Teletype, Telegram, Rentry, Write.as, dev.to, Mastodon, Dropbox, GoFile), y exfiltra a almacenamiento S3 comercial (Wasabi, Tebi, Intercolo). Valoramos **muy probable** *(80–95 %)* que este modelo sea adoptado por actores con victimología latinoamericana en los próximos doce meses, si no lo ha sido ya. **Confianza: moderada.** *Base:* `CTI-2026-020` y `CTI-2026-022` ya documentan abuso de servicios legítimos por actores regionales; la extrapolación del grado de sofisticación es nuestra.

**KJ-6.** La única pieza del informe que nos aplica de forma directa e inmediata es **CVE-2025-8088**, el fallo de recorrido de ruta de WinRAR mediante flujos de datos alternativos NTFS. Gamaredon lo incorporó el 26 de septiembre de 2025 y, en palabras de ESET, «desde entonces lo ha empleado en todas las campañas posteriores». El exploit extrae un descargador HTA a la carpeta de inicio del usuario sin que la víctima lo sepa, garantizando persistencia al siguiente inicio de sesión. WinRAR lo corrigió en la versión 7.13 en julio de 2025. Valoramos **casi con certeza** *(95–99 %)* que haya instalaciones de WinRAR sin actualizar en cualquier parque de tamaño medio. **Confianza: alta.** *Base:* el vector es el gestor de archivadores más instalado del mundo en su variante no gestionada, fuera de ciclo de parcheo corporativo en la mayoría de organizaciones.

**KJ-7.** La atribución estatal de este actor es, excepcionalmente, de las más sólidas que existen: el Servicio de Seguridad de Ucrania lo atribuye al **18.º Centro de Seguridad de la Información del FSB, operando desde Crimea ocupada**, y ESET aporta un indicio independiente y poco común — las actualizaciones de las herramientas se concentran **en los días previos a los festivos de Rusia y Crimea, y cesan durante y después de ellos**, lo que la propia fuente lee como que los operadores son «probablemente empleados afiliados al gobierno». Valoramos **muy probable** *(80–95 %)* el nexo con el FSB. **Confianza: alta.** *Base:* atribución de servicio estatal con identificación nominal de cinco miembros, corroborada por un patrón de calendario laboral medido por un proveedor con telemetría.

**KJ-8.** Desde principios de 2025 existe **colaboración documentada entre Gamaredon y Turla**, y su forma es la que importa: Gamaredon aporta el acceso y Turla selecciona dentro de él. ESET observó siete máquinas en Ucrania con indicadores de Turla en dieciocho meses, frente a los «cientos, si no miles» de compromisos de Gamaredon, y documentó la secuencia: PteroGraphin reinició una puerta trasera Kazuar v3 el 27 de febrero de 2025; PteroOdd y PteroPaste desplegaron Kazuar v2 en abril y junio. Dos de las seis herramientas nuevas de 2025 existen únicamente para entregar cargas de Turla, lo que ESET sugiere que pudieron desarrollarse **en preparación** de la colaboración. Valoramos **probable** *(55–80 %)* que la relación sea coordinación entre unidades del mismo servicio y no compromiso de una por la otra. **Confianza: moderada.** *Base:* fuente única, con hipótesis alternativas declaradas y descartadas por la propia fuente.

**Qué cambiaría estos juicios:** un informe de primera mano que documente una víctima de Gamaredon **fuera de Ucrania**. Eso invalidaría `KJ-1`, convertiría `KJ-2` en una discrepancia de hecho y no de método, y obligaría a reescribir toda la evaluación de pertinencia regional de este informe. Es el indicador `I-1` de §O-7 y el único que justificaría una revisión anticipada antes del 16 de enero de 2027.

---

## 2. Resumen ejecutivo

Si alguien de esta organización consulta en noviembre de 2026 cuál es el grupo de espionaje estatal más activo del mundo, la respuesta que encontrará es Gamaredon. El informe semestral de Trellix, publicado el 4 de noviembre, le atribuye el 9,03 % de toda la actividad estatal observada entre abril y septiembre, por delante de los actores pakistaníes y chinos, y le asigna casi una de cada cinco detecciones registradas en Estados Unidos.

La respuesta es, para nuestros fines, engañosa. El mismo actor tiene un whitepaper anual dedicado, de 47 páginas, publicado por ESET en junio de 2026, y ese documento afirma sin matices que en 2025 Gamaredon atacó **exclusivamente** instituciones gubernamentales y militares ucranianas. No hay un segundo país. Ni uno.

**Este informe existe para explicar esa contradicción y extraer de ella algo utilizable**, porque la contradicción no es un error de una de las dos fuentes: es lo que ocurre cuando se confunde volumen de detección con alcance de amenaza. Gamaredon es, con casi total seguridad, el actor estatal más ruidoso del planeta. Todo su arsenal —veintiséis herramientas documentadas— está escrito en VBScript y PowerShell, sin un solo binario compilado. Envía 35 campañas de correo dirigido al año. Infecta pendrives y unidades de red compartidas creando accesos directos falsos con nombres en ucraniano. Reemplaza instaladores de software legítimos en los discos que encuentra. Cada una de esas acciones genera detecciones, y las detecciones son lo que el ranking cuenta. Un actor sigiloso con diez víctimas de altísimo valor no aparece en esa lista; Gamaredon la encabeza.

La lección es de procedimiento y vale para toda la cartera: **un ranking ordenado por prevalencia de telemetría no es un orden de prioridad defensiva.** Quien lo use como tal pondrá a un actor sin una sola víctima documentada en nuestro hemisferio por delante de los cuatro actores con víctimas chilenas o regionales confirmadas que ya tenemos perfilados.

Dicho eso, hay tres cosas concretas de Gamaredon que sí nos aplican, y por eso el informe no termina aquí.

La primera es **CVE-2025-8088**, un fallo de WinRAR que permite escribir ficheros fuera del directorio de extracción usando flujos de datos alternativos de NTFS. Gamaredon lo empezó a usar el 26 de septiembre de 2025 y desde entonces lo usa en todas sus campañas: el archivador deja un descargador en la carpeta de Inicio del usuario sin que éste lo sepa, y se ejecuta al siguiente arranque de sesión. WinRAR lo corrigió en julio de 2025, en la versión 7.13. WinRAR está instalado en casi cualquier parque de ordenadores de oficina y casi nunca está en el ciclo de parcheo corporativo. Esto es una decisión de inventario y despliegue, no de SOC.

La segunda es el **modelo de infraestructura**, y es la parte que recomendamos leer con más atención. Gamaredon ya no tiene servidores que se puedan bloquear. Esconde su mando y control detrás de túneles y *workers* de Cloudflare, Microsoft y Loophole; averigua a cuál conectarse leyendo publicaciones en Telegra.ph, Rentry, Write.as, dev.to y Mastodon; y se lleva los ficheros robados a almacenamiento S3 comercial de Wasabi, Tebi e Intercolo. Todo lo que toca es un servicio legítimo que no se puede meter en una lista de bloqueo sin romper algo propio. Esto no es un problema de Gamaredon: es el futuro de la detección de mando y control, y los actores que sí operan en nuestra región —los de `CTI-2026-020` y `CTI-2026-022`— ya van por ese camino con menos refinamiento.

La tercera es el **movimiento lateral por medios compartidos**: USB, unidades de red mapeadas e instaladores de software. Tres herramientas distintas hacen eso, y ninguna necesita una vulnerabilidad: necesitan que alguien haga doble clic en lo que parece una carpeta. Cualquier organización con carpetas compartidas y usuarios que llevan pendrives entre sedes es vulnerable a ese patrón, venga de Gamaredon o de quien sea.

Lo que pedimos a Dirección es, en consecuencia, casi todo de inventario y de política, y muy poco de bloqueo.

<!-- cti:cards -->

| Rasgo | Qué significa | Etiqueta |
|---|---|---|
| Primero del ranking, cero víctimas en la región | El instrumento de priorización del mercado nos apunta a un actor que no nos ataca. Corregirlo es la decisión más valiosa de este informe | `01 · priorización` |
| Arsenal íntegramente en script | Ni un binario compilado en 26 herramientas. Explica el volumen de detección y dice dónde hay que mirar: registro de ejecución de scripts, no de procesos | `02 · arsenal` |
| Sin servidores propios que bloquear | Túneles, *workers*, *dead drops* y S3 de terceros. La lista de bloqueo deja de funcionar como control | `03 · infraestructura` |
| Explota CVE-2025-8088 en todas las campañas desde sep-2025 | Persistencia en la carpeta de Inicio sin interacción visible. Nos aplica igual que a Ucrania | `04 · vector` |
| Propaga por USB, unidades de red e instaladores | No necesita exploit: necesita una carpeta compartida y un doble clic | `05 · lateral` |
| Actualiza antes de los festivos rusos y para durante | Indicio de calendario laboral estatal. Es el mejor argumento de atribución del expediente | `06 · atribución` |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `9,03` | Porcentaje de la actividad estatal global que Trellix le atribuye, abr–sep 2026 | Primer puesto del ranking. En Q3 aislado sube a 10,72 % |
| `19,88` | Porcentaje de las detecciones de actor estatal en EE. UU. que Trellix le atribuye | Base distinta de la cifra global. **Ninguna víctima estadounidense documentada por ESET** |
| `1` | Países con víctimas documentadas por ESET en 2025 | Ucrania. La palabra que usa la fuente es «exclusivamente» |
| `35` | Campañas de correo dirigido distintas identificadas en 2025 | Al menos una en cada mes del año salvo enero; mayores y más frecuentes en el segundo semestre |
| `26` | Herramientas del arsenal documentadas en el whitepaper de 2025 | Seis de ellas nuevas en 2025; dos descontinuadas ese mismo año |
| `0` | Herramientas escritas en un lenguaje compilado | Todo es VBScript o PowerShell. Dato declarado explícitamente por la fuente |
| `189` | Dominios registrados y usados por el actor en 2025 | Mayoría con TLD `.ru`, unos pocos `.online`. Cifra similar a 2024 |
| `4` | Servicios de túnel y *worker* usados como estándar de C2 | Cloudflare tunnels, Cloudflare workers, Microsoft devtunnels, Loophole. Más dos en pruebas |
| `9` | Servicios legítimos abusados como *dead drop* | Telegra.ph, Teletype, Telegram, Rentry, Write.as, dev.to, Mastodon, Dropbox, GoFile |
| `3` | Servicios de almacenamiento S3 comercial usados para exfiltración | Wasabi, Tebi e Intercolo (`de-fra.i3storage.com`), en ese orden cronológico |
| `7` | Máquinas en Ucrania con indicadores de Turla en 18 meses | Frente a «cientos, si no miles» comprometidas por Gamaredon. Es la proporción que define la relación entre ambos |
| `18` | Centro del FSB al que el SSU atribuye el grupo | Centro de Seguridad de la Información, operando desde Crimea ocupada |

<!-- cti:note type="good" -->

> ✅ **Decisiones que se solicitan a Dirección.** (a) **Corregir el criterio de priorización**: instruir por escrito que los rankings de prevalencia de proveedor no se usen como orden de prioridad defensiva sin un cruce previo contra victimología regional documentada — 30 días, coste cero, es la decisión de mayor valor de este informe. (b) **Inventariar y actualizar WinRAR** en todo el parque, con umbral mínimo 7.13, e incorporarlo al ciclo de parcheo gestionado o eliminarlo en favor del gestor de archivadores integrado del sistema — 45 días. (c) Desplegar las detecciones `D-1` a `D-5` del §X-3, que son **conductuales y no dependen de ningún indicador de este actor** — 60 días. (d) Resolver la **brecha de visibilidad de ejecución de scripts** (§T-5): sin registro de bloque de script de PowerShell y sin registro de `mshta.exe`, este actor y cualquiera que copie su método son invisibles — 90 días, es la decisión más cara y la que más cobertura aporta. (e) Decidir la **política sobre medios extraíbles y unidades compartidas**: `D-4` detecta la propagación, pero sólo una política la impide — 90 días. (f) **No** cargar el Anexo A en bloqueo sin filtrar por la columna de acción permitida: catorce de sus entradas son servicios legítimos de terceros y bloquearlas provoca cortes propios. Véase la advertencia del Anexo A.

---

## 3. Alcance, requisitos y limitaciones

**3.1 Requisitos de inteligencia atendidos**

| Req. | Enunciado | ¿Respondido? | Dónde |
|---|---|---|---|
| PIR-01 | ¿Qué actores tienen intención y capacidad contra nuestro sector y geografía? | **Sí, y la respuesta es que este no** | `KJ-1`, §E-1, §E-2 |
| PIR-04 | ¿Qué amenazas operan contra la región hispanohablante y con qué método? | **No aplica a este actor** — se documenta la transferencia de método, no de amenaza | `KJ-5`, §E-4 |
| PIR-07 | ¿Qué técnicas de ocultación de mando y control invalidan nuestros controles actuales? | Sí — es la aportación central del informe | §O-3, §X-1, §T-3 |
| PIR-10 | ¿Está vigente la inteligencia de la que dependemos, y mide lo que creemos que mide? | **Sí, y es el hallazgo del informe** | `KJ-2`, `KJ-3`, `KJ-4`, §O-6 |
| PIR-12 | ¿Qué vulnerabilidades explotadas activamente tenemos expuestas? | Sí — una, `CVE-2025-8088` | `KJ-6`, §T-1, §X-5 |
| — | ¿Hay víctimas chilenas o latinoamericanas? | **Ninguna documentada en ninguna fuente** | §E-2 |
| — | ¿Estamos ya comprometidos por este actor? | **No evaluable** — sin telemetría propia | §O-4, §14 (`G-1`) |

**3.2 Fuera de alcance.** No se evalúa: la actividad de Turla como actor propio, que merece producto separado y aquí aparece sólo como consumidor del acceso de Gamaredon; el análisis de ingeniería inversa de las herramientas individuales, para el que el whitepaper de ESET es la fuente y este informe no lo sustituye; la actividad de Gamaredon anterior a 2025, cubierta por los whitepapers de 2024 y de 2022–2023 del mismo proveedor; la relación con InvisiMole, que ESET afirma y no desarrolla en el documento leído; y la atribución nominal de los cinco miembros identificados por el SSU, que es materia judicial ucraniana y no aporta a ninguna decisión nuestra.

**3.3 Limitaciones de la colección.** (i) **Dependencia de fuente única para la victimología.** La afirmación de exclusividad ucraniana de `KJ-1` descansa en un solo proveedor. Ningún otro informe leído la contradice, pero ninguno la corrobora de forma independiente: el resto de fuentes no se pronuncia sobre geografía. Esto es relevante porque es precisamente el punto en disputa con el ranking de Trellix. (ii) **La página del informe de Trellix no pudo leerse directamente**: responde con HTTP 403 a lectura automatizada. Las cifras de 9,03 %, 7,84 %, 7,52 %, 10,72 % y 19,88 % provienen de la página indexada por el buscador y de la cobertura de *Infosecurity Magazine*, que las reproduce de forma coincidente. **No se ha leído la metodología declarada del ranking**, y eso significa que `KJ-3` —nuestra explicación de la contradicción— no pudo verificarse contra la definición que el proveedor da de «actividad observada». Es la limitación más seria del informe y está recogida como brecha `G-2`. (iii) **Sin telemetría propia**: §O-4 sin rellenar. (iv) **Las figuras del whitepaper son imágenes** y sus valores no se pudieron leer; en particular la figura 2, que grafica muestras únicas de descargadores HTA por mes y permitiría cuantificar la estacionalidad de las campañas. El dato textual que sí se usa es que hubo al menos una campaña en cada mes de 2025 salvo enero, y que el segundo semestre fue más activo. (v) **Los indicadores de red del whitepaper son explícitamente un muestreo**: la propia fuente advierte que «son sólo los servidores de C&C extraídos de muestras seleccionadas, proporcionados como ejemplos y no una lista exhaustiva», y que las listas completas están en eventos MISP de acceso comercial. El Anexo A de este informe hereda esa parcialidad. (vi) **Los hashes publicados son SHA-1 y uno por herramienta o variante.** La fuente no publica SHA-256 y declara que ofrece «sólo un ejemplo por herramienta o variante». Un retrohunt basado en ellos encontrará una muestra de cada familia, no la familia. (vii) **El repositorio público de indicadores del proveedor no publica artefactos de host** —tareas programadas, claves de registro, mutex, rutas—; esos valores se tomaron de los apéndices A a H del whitepaper, que sí los detalla y que son la parte más duradera del Anexo A. (viii) **La discrepancia sobre qué centro del FSB** opera el grupo no está resuelta: la mayoría de fuentes, incluida ESET, dice 18.º Centro; una fuente secundaria menciona los centros 16.º y 18.º; otra sitúa la orden en el Centro de Seguridad de la Información de Moscú. Se consigna el 18.º por ser el que afirma la fuente de primera mano, con la salvedad anotada en §O-2. (ix) **La afirmación de que Gamaredon usó CVE-2025-8088 para desplegar un borrador de datos (*wiper*)** aparece en cobertura secundaria de junio de 2026 y **no en el whitepaper leído**, que trata el CVE únicamente como vector de acceso inicial para descargadores HTA. Una fuente secundaria distinta atribuye un *wiper* denominado GamaWiper a noviembre de 2025 según un tercer proveedor. **No se sostiene en este informe ninguna capacidad destructiva de Gamaredon**; se consigna como brecha `G-3`.

**3.4 Metodología.** Disciplinas: OSINT comercial de proveedor de primera mano (un whitepaper técnico de 47 páginas con metodología de atribución declarada, más un informe trimestral del mismo proveedor), OSINT comercial de telemetría agregada (el ranking de Trellix, con la limitación (ii)), OSINT de repositorio de indicadores, y OSINT de atribución estatal (declaraciones del SSU, por vía secundaria). Técnicas analíticas estructuradas: **análisis de hipótesis competidoras** aplicado a la contradicción entre fuentes (§O-6), que es el núcleo analítico del producto; comprobación de supuestos clave; pre-mortem. Marcos: MITRE ATT&CK v19 —versión que declara el whitepaper y que este informe conserva—, Pirámide del Dolor, Cadena de Intrusión, ICD 203, código Admiralty.

**3.5 Por qué este informe caduca antes que los demás.** La cartera usa 92 días para perfiles de actor vigentes. Aquí se fija 60. La razón es medible en el propio Anexo A: de los 32 dominios de C2 publicados por ESET para 2025, veintiséis son subdominios efímeros de servicios de túnel con fecha de primera observación concentrada en las últimas dos semanas de diciembre de 2025. Esos nombres no existen ya. Los seis dominios `.ru` registrados tienen más vida, pero el actor registró 189 en el año: los seis publicados son el 3 % de su inventario. **El componente de indicadores de este informe nace caducado y se entrega sabiéndolo**; lo que no caduca son los artefactos de host del Anexo A.2 y las detecciones conductuales del §X-3, y es ahí donde debe invertirse el esfuerzo.

---

# NIVEL ESTRATÉGICO
### Para: Consejo · CISO · Riesgo · Responsables de priorización y de inventario de software · Horizonte: 6–24 meses

## E-1. Qué representa este actor en el panorama, y por qué el ranking miente sin querer

Gamaredon no representa una amenaza para esta organización. Representa un **problema de instrumentación**, y ése es un hallazgo más útil que la mayoría de perfiles de actor, porque afecta a cómo se decide todo lo demás.

El mecanismo es el siguiente. Un informe de telemetría agregada ordena actores por porcentaje de actividad detectada sobre el total de actividad estatal detectada. Ese porcentaje es una función de tres cosas: cuánto opera el actor, **con qué nivel de sigilo**, y dónde está desplegada la telemetría que lo mide. Las tres se suman en un solo número y el número se publica como un orden de importancia.

Gamaredon maximiza la segunda variable en la dirección equivocada. Su arsenal completo —veintiséis herramientas— está escrito en VBScript y PowerShell, sin un solo binario compilado; lo declara la fuente de primera mano de forma expresa. Trece años con la misma familia de detección significa trece años de firmas acumuladas. El modelo de propagación por USB y unidades de red multiplica artefactos: cada pendrive que pasa por una máquina protegida devuelve detecciones de los mismos accesos directos. Las 35 campañas anuales de correo generan, en palabras de la fuente, muestras únicas de descargador HTA que se cuentan por mes. Un actor construido así es, por diseño, el más detectado del mundo.

El contraste útil es con el actor de `CTI-2026-028`, UNC3886, al que la inteligencia de Google describe como uno de los más capaces y prolíficos que ha observado, y que no aparece en ningún ranking de prevalencia: opera en hipervisores y dispositivos de borde donde no hay agente que lo cuente. **El ranking no mide amenaza; mide fricción entre el adversario y el sensor.**

<!-- cti:cards -->

| Cambio estructural | Por qué nos afecta | Etiqueta |
|---|---|---|
| El C2 se desplazó a servicios legítimos de terceros | La lista de bloqueo deja de ser un control. Si `trycloudflare.com` y `workers.dev` son C2, bloquearlos rompe desarrollo propio y no bloquearlos deja el canal abierto | `01 · fin del bloqueo` |
| La resolución de C2 se desplazó a redes sociales y pastebins | La detección debe mirar **qué proceso** accede a `telegra.ph` o `mastodon.social`, no si se accede. Un navegador es normal; `powershell.exe` no | `02 · dead drop` |
| La exfiltración se desplazó a almacenamiento S3 comercial | El tráfico de salida de datos robados es indistinguible del respaldo legítimo en nube. El control pasa a ser de egreso y de inventario de servicios autorizados | `03 · exfiltración` |
| El acceso inicial se desplazó a un fallo de archivador de escritorio | WinRAR no está en el ciclo de parcheo de casi nadie. El parque de software no gestionado es el vector | `04 · software gris` |
| La división del trabajo entre actores estatales se formalizó | Un actor de volumen entrega acceso a un actor de precisión. Nuestra detección del primero es el único momento en que el segundo es visible | `05 · cadena de acceso` |
| Los rankings de prevalencia entraron en los flujos de priorización automatizados | Un dato correcto se convierte en una decisión equivocada sin que nadie mienta en ningún punto de la cadena | `06 · instrumentación` |

## E-2. Victimología: el dato más limpio del informe

En 2025, según la fuente de primera mano, Gamaredon atacó instituciones gubernamentales y militares **de Ucrania, y de ningún otro país**. No hay distribución por países que graficar porque hay un solo país. No hay distribución sectorial más allá de dos sectores: gobierno y defensa.

<!-- cti:bars title="Víctimas documentadas por país, 2025 (fuente de primera mano)" -->

| País | Víctimas documentadas |
|---|---|
| Ucrania | `Todas` |
| Resto del mundo | `0` |

<!-- cti:bars title="Dónde dice la telemetría agregada que está la actividad (abr–sep 2026)" -->

| Medida | Porcentaje |
|---|---|
| Cuota en detecciones estatales de EE. UU. | `19,88` |
| Cuota en actividad estatal global | `9,03` |
| Cuota en Q3 2026 aislado | `10,72` |

> **Lectura clave.** Las dos tablas anteriores describen el mismo actor y son
> ambas correctas. La primera cuenta organizaciones comprometidas; la segunda
> cuenta detecciones de firma. Una organización ucraniana comprometida produce
> una víctima y miles de detecciones; un pendrive infectado que circula por una
> empresa estadounidense produce cero víctimas y decenas de detecciones. **Lo
> que el 19,88 % mide con mayor probabilidad no es intrusión en EE. UU. sino
> contacto con artefactos de este actor en un parque con mucha telemetría
> instalada**: adjuntos bloqueados en pasarelas de correo, muestras subidas a
> plataformas de análisis, medios extraíbles. Es una hipótesis nuestra y está
> declarada como tal en `KJ-3` y examinada contra sus alternativas en §O-6.

**Lo que esta victimología nos quita y lo que nos deja.** Nos quita la necesidad de cazar a Gamaredon: no hay escenario razonable en el que una organización chilena sea objetivo de un servicio ruso de recolección sobre el teatro ucraniano. Nos deja tres cosas: la vulnerabilidad de WinRAR, que es indiferente a la geografía; el método, que se copia; y la advertencia de instrumentación, que es reutilizable.

## E-3. Tendencia y pronóstico

Hay una tensión entre las dos ventanas de observación que conviene explicitar. El whitepaper, sobre 2025, describe un actor en expansión: seis herramientas nuevas, 35 campañas con el segundo semestre más intenso que el primero, un vector de acceso nuevo desde septiembre, y migración de toda la exfiltración a nube. El informe trimestral del mismo proveedor, sobre abril–septiembre de 2026, describe lo contrario: un **descenso significativo** de actividad, con tres explicaciones barajadas y ninguna confirmada —ataques ucranianos sobre Crimea, reestructuración interna, u otra causa aún en evaluación—. Y Trellix, sobre la misma ventana de 2026, lo sitúa en el primer puesto y **subiendo** en Q3.

Las tres observaciones pueden coexistir si el descenso es de intrusiones y la subida es de detecciones, lo que reforzaría `KJ-3`. También puede ocurrir que el descenso sea real y el ranking esté midiendo cola de artefactos de campañas anteriores. No podemos distinguirlo con las fuentes disponibles.

<!-- cti:chart title="Hitos de capacidad declarados por la fuente de primera mano, 2025" cap="Serie de hitos, no de volumen: cuenta cambios documentados de capacidad, no víctimas ni detecciones." -->

| Periodo | Hitos documentados |
|---|---|
| `Q1 2025` | `5` |
| `Q2 2025` | `4` |
| `Q3 2025` | `3` |
| `Q4 2025` | `4` |

<!-- cti:cards -->

| Escenario | Desarrollo | Etiqueta |
|---|---|---|
| Continuidad en teatro único | El actor sigue operando exclusivamente contra Ucrania, con el arsenal en script y la infraestructura en servicios de terceros. Sigue encabezando rankings de prevalencia y sigue siendo irrelevante para nuestra priorización | `Probable · 55–80 %` |
| Difusión del método, no del actor | El modelo de túneles, *workers*, *dead drops* y exfiltración a S3 aparece replicado en actores con victimología regional. **Es el escenario que nos obliga a actuar, y la acción que exige es la del §X-3** | `Probable · 55–80 %` |
| Degradación real de la capacidad | El descenso que observa el informe trimestral de 2026 es estructural —pérdida de infraestructura en Crimea o reorganización del 18.º Centro— y el actor se repliega o se disuelve en otra designación | `Posibilidad real · 45–55 %` |
| Ampliación de la victimología | El actor extiende objetivos a Estados de la OTAN o a proveedores de la cadena de suministro militar ucraniana fuera de Ucrania. Invalidaría `KJ-1` | `Poco probable · 20–45 %` |
| Capacidad destructiva confirmada | Se confirma de primera mano el uso de *wiper* que la cobertura secundaria afirma y el whitepaper no recoge. Cambiaría la clase de amenaza, no la geografía | `Poco probable · 20–45 %` |
| Ampliación a Latinoamérica | Sin ningún indicio en ninguna fuente, en trece años de seguimiento | `Remoto · 5–10 %` |

## E-4. Decisiones que este informe pide al nivel estratégico

<!-- cti:table highlight="priorización|WinRAR|ranking" -->

| # | Decisión | Fundamento | Plazo |
|---|---|---|---|
| E-a | **Instruir por escrito que los rankings de prevalencia de proveedor no determinen prioridad defensiva** sin cruce previo contra victimología regional documentada. Nombrar responsable del cruce | `KJ-2`, `KJ-3`, `KJ-4`, §E-1 | 30 días |
| E-b | **Inventariar WinRAR en todo el parque** y llevarlo a 7.13 o superior, o retirarlo en favor del gestor de archivadores del sistema operativo. Incorporarlo al ciclo de parcheo gestionado | `KJ-6`, §T-1 | 45 días |
| E-c | Aprobar la **lista de servicios de túnel, *worker*, *dead drop* y almacenamiento en nube autorizados** en la organización, como requisito previo a que la detección de egreso sea posible. Sin esta lista, `D-6` y `D-10` generan sólo ruido | §O-3, `KJ-5`, §X-3 | 60 días |
| E-d | Financiar el cierre de la **brecha de visibilidad de ejecución de scripts**: registro de bloque de script de PowerShell, registro de línea de comandos de procesos y auditoría de `mshta.exe`. Es la decisión más costosa y la que más cobertura aporta frente a esta clase entera de adversario | §T-5, `G-1` | 90 días |
| E-e | Decidir la **política de medios extraíbles y de unidades compartidas**: bloqueo de ejecución desde medios extraíbles, y revisión de permisos de escritura en recursos compartidos de red | §T-1, `D-4` | 90 días |
| E-f | Aceptar formalmente que **el Anexo A de este informe no es material de bloqueo** y que su valor es de retrohunt y de reconocimiento de patrón. Confirmar que la plataforma de inteligencia respeta la columna de acción permitida | Anexo A, §3.5 | 30 días |

---

# NIVEL OPERACIONAL
### Para: Jefatura de SOC · Respuesta a Incidentes · Threat Hunting · Gestión de Vulnerabilidades · Horizonte: semanas–meses

## O-1. Identificación y alias

| Designación | Origen | Grado de equivalencia |
|---|---|---|
| `Gamaredon` | Palo Alto Networks (2015), de uso general en la industria | **Referencia** — es el nombre que usa la fuente de primera mano |
| `Armageddon` | Servicio de Seguridad de Ucrania (SSU), designación interna | **Equivalente** — es el mismo grupo; el nombre comercial derivó de un anagrama de este |
| `Primitive Bear` | CrowdStrike | Equivalente |
| `ACTINIUM` | Microsoft (taxonomía anterior) | Equivalente |
| `Aqua Blizzard` | Microsoft (taxonomía de meteorología, vigente) | Equivalente |
| `Shuckworm` | Broadcom / Symantec | Equivalente |
| `IRON TILDEN` | Secureworks | Equivalente |
| `DEV-0157` | Microsoft, designación temporal histórica | Equivalente — precede a la asignación de `ACTINIUM` |
| `NastyShrew` | PwC | Equivalente |
| `G0047` | MITRE ATT&CK | Equivalente — ficha de grupo |
| `Pterodo` | ESET | **No es un alias de grupo.** Es el nombre de **familia de malware** que ESET asigna a las herramientas del actor. Las detecciones tienen la forma `PowerShell/Pterodo.*`, `VBS/Pterodo.*`, `Win32/Pterodo.*` |
| `UAC-0010` | CERT-UA | Equivalente — designación del equipo nacional ucraniano |

> **Nota de tradecraft.** Éste es, excepcionalmente, un expediente de alias
> **sin disputa**: once designaciones comerciales y estatales que todas las
> fuentes tratan como el mismo grupo, sin solapamientos parciales ni
> agrupaciones divergentes. Contrástese con `CTI-2026-022`, donde la disputa de
> nombres era el problema operativo principal. La única confusión posible aquí
> es la de la última fila: **`Pterodo` nombra el malware, no el grupo**, y los
> nombres `PteroXxx` del arsenal son designaciones de componente del mismo
> proveedor. Quien busque «Pterodo» en una plataforma de inteligencia encontrará
> familias de malware; quien busque «Gamaredon» encontrará el actor.

## O-2. Estructura y atribución

| Eje de atribución | Valoración | Confianza |
|---|---|---|
| Clúster técnico | **Coherente y estable.** Trece años de continuidad de arsenal, ofuscación característica reutilizada y familia de detección única | Alta |
| Grupo organizado | **Sí**, con desarrollo de herramientas propio y sostenido: seis herramientas nuevas en un solo año, mantenimiento paralelo de veintiséis, y rollback documentado de una actualización fallida —señal de control de versiones y de decisión técnica deliberada— | Alta |
| Nexo estatal | **18.º Centro de Seguridad de la Información del FSB**, operando desde Crimea ocupada, según atribución del SSU. Corroborado indirectamente por el patrón de calendario laboral | Alta |
| Identidad nominal | Cinco miembros identificados nominalmente por el SSU en su atribución pública | Moderada — no verificable con fuentes abiertas técnicas |
| Relación con Turla | **Colaboración operativa**, con Gamaredon aportando acceso y Turla seleccionando objetivos dentro de él | Moderada |
| Relación con InvisiMole | Afirmada por la fuente de primera mano, sin desarrollo en el documento leído | Baja |

*Razonamiento.* La atribución estatal no descansa sólo en la declaración del SSU. El argumento técnico más interesante del whitepaper es de calendario: la fuente observó que **muchas actualizaciones de las herramientas se hicieron en los días previos a festivos importantes en Rusia y Crimea, y que no se observó ninguna durante ni inmediatamente después de esos festivos**, y concluye de ahí que los operadores son «probablemente empleados afiliados al gobierno». Es un indicio de comportamiento laboral, no de código, y por eso es difícil de falsificar: un actor criminal no cierra por fiesta nacional, y un actor que quisiera simular nexo estatal tendría que mantener la simulación durante años de desarrollo continuo.

A eso se añade la coherencia del objetivo: trece años sin desviarse de instituciones gubernamentales y militares de un solo país, incluso cuando su arsenal propaga indiscriminadamente por USB y podría haber derivado a monetización en cualquier momento. Un actor que puede robar documentos a cualquiera y sólo roba a ministerios ucranianos está cumpliendo un requisito de recolección, no persiguiendo un beneficio.

*Contraargumento.* La parte débil es el **18.º Centro frente al 16.º**. Las fuentes secundarias divergen: una menciona ambos centros, otra sitúa la orden en el Centro de Seguridad de la Información en Moscú y no en Crimea. La fuente de primera mano dice 18.º y Crimea, y es la que se recoge. Para cualquier decisión nuestra la distinción es irrelevante —ninguna acción defensiva cambia según el centro—, pero se consigna porque un informe que presenta como firme un dato en disputa pierde credibilidad en lo que sí es firme.

*Segundo contraargumento, sobre Turla.* La colaboración se infiere de coincidencia de herramientas en las mismas máquinas, no de observación de mando. La propia fuente declara que en todos los casos su producto se instaló **después** del compromiso, de modo que no observó la descarga inicial. Y declara explícitamente sus hipótesis alternativas: que Turla hubiera comprometido la infraestructura de Gamaredon, o que Gamaredon desplegara Kazuar por su cuenta. Las descarta por menos probables, no por imposibles.

## O-3. Modelo de operación: por qué este actor ya no tiene nada que bloquear

Lo que distingue a Gamaredon de un actor de 2020 no es el malware —sigue siendo VBScript— sino **dónde vive su infraestructura**. La migración está documentada con fechas y conviene leerla como una progresión deliberada, porque es el patrón que se va a copiar.

**Primera capa: el canal.** A finales de 2024 el estándar era conectar a través de túneles de Cloudflare (`trycloudflare.com`). En mayo de 2025 el actor añadió *workers* de Cloudflare (`workers.dev`), y la diferencia es sustantiva: un túnel sólo retransmite tráfico, mientras que un *worker* **ejecuta código** que puede procesar las peticiones sin que el operador gestione infraestructura alguna. Al mes siguiente añadió los túneles de Microsoft (`devtunnels.ms`) y de Loophole (`loophole.site`). Los tres servicios de túnel se usan **en combinación, uno como primario y dos de reserva, en orden variable**, lo que la fuente interpreta como ausencia de preferencia por ninguno. Hay además dos servicios en fase de prueba, `loca.lt` y `bore.pub`, hallados en pocas muestras.

**Segunda capa: la resolución.** El actor no codifica a qué servidor conectarse: lo publica. Usa *dead drop resolvers* en nueve servicios legítimos —canales de Telegram vía `t.me`, publicaciones en `telegra.ph` y `teletype.in`, y como novedad de 2025 `rentry.co`, `write.as`, la red social de desarrolladores `dev.to` y `mastodon.social`, más Dropbox y GoFile usados por dos herramientas—. El cambio respecto a 2024 es de contenido: antes publicaba direcciones IP, ahora publica **nombres de servidores ya escondidos detrás de túneles**. Es una indirección sobre otra indirección.

Hay un refinamiento que merece atención por lo que dice del nivel de madurez. PteroPSDoor, uno de los dos ladrones de ficheros principales, **crea sus propias publicaciones** en Write.as y Telegra.ph mediante sus API REST, cifra los tokens de edición con una clave RSA incrustada única por instancia, y los sube a su servidor. Después consulta esas publicaciones cada treinta minutos, y lo que encuentra en ellas no es una dirección de C2 sino **la dirección de otra publicación que la contiene**. Un par de publicaciones gobierna el C2 primario y el otro par el C2 accesible por Tor.

**Tercera capa: la distribución de carga.** Algunos servicios no sirven para resolver sino para entregar la carga útil: `lesma.eu`, `nopaste.net` y `pastee.dev` alojan los payloads cifrados y codificados de los descargadores de PteroPSDoor y PteroVDoor.

**Cuarta capa: la exfiltración.** Toda la salida de datos se fue a almacenamiento comercial compatible con S3, y la cronología de 2025 está documentada al día: PteroVDoor pasó a Wasabi el 31 de mayo, a Tebi el 11 de septiembre y a Intercolo (`de-fra.i3storage.com`) el 5 de diciembre; PteroPSDoor siguió una secuencia equivalente, con Wasabi desde abril, Tebi desde agosto e Intercolo como primario en diciembre —el cambio a Intercolo fue **simultáneo en ambas herramientas**, lo que indica decisión central y no evolución independiente—. PteroBox, la tercera, exfiltra a Dropbox usando `rclone` descargado y renombrado.

**Quinta capa, la de reserva: lo propio.** El actor mantiene 189 dominios registrados en 2025, mayoría `.ru` y unos pocos `.online`, con DNS de flujo rápido para rotar direcciones. Pero la fuente es explícita en el papel que cumplen: **los dominios codificados son el método de reserva**, y los *dead drops* y túneles son el canal primario. Y recuperó, tras cuatro años sin usarlo, el DNS dinámico de No-IP —dieciséis dominios distintos—, con mayor incidencia precisamente en los descargadores HTA de las campañas de correo.

> **Por qué esto importa aquí y no sólo en Ucrania.** La consecuencia de las
> cinco capas es que **no existe un indicador de red bloqueable que no sea
> también un servicio que alguien de la organización usa legítimamente.**
> `trycloudflare.com` lo usa cualquier desarrollador que expone un servicio
> local; `devtunnels.ms` lo usa Visual Studio; `dev.to` y `mastodon.social` son
> sitios web ordinarios; Dropbox y Wasabi son proveedores de respaldo. La
> detección tiene que mudarse de «¿se contactó este destino?» a «**¿qué proceso
> contactó este destino?**». Ése es el contenido del §X-3 y es el único
> entregable de este informe que no caduca.

## O-4. Nuestra exposición

> ⬛ **Sección sin evaluar — requiere telemetría e inventario internos.** Las
> preguntas se entregan como requisito de colección. A diferencia del resto de
> la cartera, aquí **ninguna pregunta busca compromiso por este actor**: todas
> buscan exposición al patrón.

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| X-1 | ¿Cuántas instalaciones de WinRAR hay en el parque y en qué versiones? ¿Cuántas por debajo de 7.13? | Inventario de software / gestor de endpoints | TI |
| X-2 | ¿Está WinRAR en el ciclo de parcheo gestionado, o es software instalado por el usuario? | Política de software | TI |
| X-3 | ¿Registramos la línea de comandos completa de los procesos creados? ¿Y el bloque de script de PowerShell (EID 4104)? | Configuración de auditoría | SOC |
| X-4 | ¿Tenemos visibilidad de ejecuciones de `mshta.exe`? ¿Es `mshta.exe` necesario en algún flujo de trabajo legítimo nuestro? | EDR / inventario de aplicaciones | SOC / TI |
| X-5 | ¿Qué procesos, distintos de los navegadores, han contactado en los últimos 90 días con `telegra.ph`, `teletype.in`, `rentry.co`, `write.as`, `dev.to` o `mastodon.social`? | Proxy / DNS / EDR | SOC |
| X-6 | ¿Qué procesos han contactado con subdominios de `trycloudflare.com`, `workers.dev`, `devtunnels.ms` o `loophole.site`? ¿Cuáles son legítimos y están autorizados? | Proxy / DNS | SOC / Arquitectura |
| X-7 | ¿Existe `rclone.exe`, con ese nombre o renombrado, en rutas de perfil de usuario (`%APPDATA%`, `%LOCALAPPDATA%`)? | EDR / búsqueda de ficheros | SOC |
| X-8 | ¿Hay tráfico de salida a `wasabisys.com`, `tebi.io` o `de-fra.i3storage.com`? ¿Está autorizado algún servicio S3 de terceros? | Proxy / cortafuegos | SOC / Arquitectura |
| X-9 | ¿Permitimos la ejecución de ficheros desde medios extraíbles? ¿Y la creación de LNK en recursos compartidos de red por cuentas de usuario ordinarias? | Política de grupo / permisos NTFS | TI / Seguridad |
| X-10 | ¿Hay valores en `HKCU\...\CurrentVersion\Run` cuyo nombre coincida con el nombre de usuario, el de dominio o el del equipo? | EDR / inventario de persistencia | SOC |
| X-11 | ¿Existen flujos de datos alternativos NTFS en `%USERPROFILE%\boot.ini`, `%PUBLIC%\ntuser.ini` o en el propio directorio de perfil? | Búsqueda de ADS | SOC |
| X-12 | ¿Alguna tarea programada usa los nombres del Anexo A.2, que imitan tareas legítimas de DirectX, Edge Update o diagnóstico de disco? | Inventario de tareas programadas | SOC |

## O-5. Cronología

<!-- cti:timeline -->

| Fecha | Hecho | Traza |
|---|---|---|
| `2013` | Primera actividad documentada del grupo | Ucrania |
| `2020-11` | Primera aparición de PteroLNK, versión VBScript: el arma de propagación por USB que sigue en uso | Ucrania |
| `2021-01` | Primera aparición de PteroSetup, el envenenador de instaladores de software. Permanecerá cinco años inactivo | Ucrania |
| `2021` | **Abandono progresivo del DNS dinámico** en favor de dominios registrados propios | Global |
| `2021-11` | El SSU atribuye el grupo al 18.º Centro del FSB e identifica nominalmente a cinco miembros | Ucrania |
| `2022-05` | Primera aparición de PteroPSDoor, ladrón de ficheros en PowerShell que será el insignia del arsenal | Ucrania |
| `2022-11` | Primera aparición de PteroVDoor, el segundo ladrón de ficheros, en VBScript | Ucrania |
| `2024-11` | Primera aparición de PteroBox: **primera herramienta del actor que exfiltra a nube comercial** (Dropbox) | Ucrania |
| `2024-fin` | Los túneles de Cloudflare se convierten en el estándar de C2 | Global |
| `2025-01` | **Único mes de 2025 sin campaña de correo dirigido** | Ucrania |
| `2025-01-20` | PteroGraphin desplegado en una máquina ucraniana; el 11 de febrero aparece Kazuar v3 de Turla en la misma máquina | Ucrania |
| `2025-02-07` | Descubrimiento de PteroDee y PteroDum, dos de las seis herramientas nuevas del año | Ucrania |
| `2025-02-27` | **`PteroGraphin` reinicia la puerta trasera Kazuar de Turla.** Es el eslabón que documenta la colaboración | Ucrania |
| `2025-03-01` | PteroPSDoor incorpora exfiltración de reserva **por Tor**, descargado con BITS desde Filemail | Ucrania |
| `2025-04-18` | PteroOdd entrega PteroEffigy, que instala Kazuar v2 | Ucrania |
| `2025-05` | **Comienza el uso de *workers* de Cloudflare**, que ejecutan código y no sólo retransmiten | Global |
| `2025-05-09` | PteroLNK separa el código de resolución de C2 en dos componentes alojados en flujos de datos alternativos | Ucrania |
| `2025-05-23` | **Reversión de esa separación**: el actor deshace su propia actualización. Señal de control de versiones | Ucrania |
| `2025-05-31` | PteroVDoor pasa a exfiltrar a Wasabi | Ucrania |
| `2025-06` | Se añaden los túneles de Microsoft (`devtunnels.ms`) y Loophole (`loophole.site`) | Global |
| `2025-06-05` | PteroPaste instala Kazuar v2 en dos máquinas ucranianas | Ucrania |
| `2025-07-31` | PteroCache entra en despliegue regular, probablemente sustituyendo a PteroDee | Ucrania |
| `2025-09-11` | PteroVDoor pasa a Tebi | Ucrania |
| `2025-09-12` | Segunda separación del código de resolución de C2 de PteroLNK | Ucrania |
| `2025-09-26` | **Primera explotación de `CVE-2025-8088` en WinRAR.** A partir de aquí, en todas las campañas | Ucrania |
| `2025-12-05` | **PteroVDoor y PteroPSDoor migran simultáneamente a Intercolo**, señal de decisión central | Ucrania |
| `2026-01-01` | Última fecha de primera observación en los indicadores públicos del proveedor | Global |
| `2026-04` → `2026-09` | **Descenso significativo de actividad** según el informe trimestral del mismo proveedor | Ucrania |
| `2026-06-25` | Publicación del whitepaper «Gamaredon in 2025», fuente principal de este informe | — |
| `2026-07` | Actualización observada de PteroBox | Ucrania |
| `2026-10-28` | Publicación del informe trimestral Q2–Q3 2026: Gamaredon baja, pero usa PteroPSDoor para desplegar `Rezzuar`, script VBScript de Turla, en casos de marzo, abril y junio | Ucrania |
| `2026-11-04` | **Trellix lo publica como el actor estatal más prevalente del mundo.** Origen de la contradicción que estructura este informe | Global |

## O-6. Hipótesis alternativas consideradas

El objeto del análisis de hipótesis competidoras de este informe no es la atribución —que está resuelta— sino **la contradicción entre las dos fuentes de `KJ-1` y `KJ-2`**.

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| **H1 — El ranking cuenta detecciones, no intrusiones** | Consistente con todo: el arsenal íntegramente en script, trece años de firmas acumuladas, propagación por medios extraíbles que multiplica artefactos, 35 campañas de correo masivo cuyos adjuntos se bloquean en pasarelas de todo el mundo. No exige que ninguna fuente se equivoque. **Es la que se retiene** | `Retenida · probable 55–80 %` |
| **H2 — La telemetría de Trellix está sesgada geográficamente** | Complementaria de H1, no alternativa. Explicaría el 19,88 % estadounidense: si la base instalada del proveedor está concentrada en EE. UU., el denominador del porcentaje lo está también. No la podemos verificar sin la metodología declarada, que no pudimos leer | `Retenida como complemento` |
| **H3 — La victimología de ESET es incompleta** | ESET tiene la telemetría que tiene. Es posible que haya víctimas de Gamaredon fuera de Ucrania en parques sin su producto desplegado. **Pero la fuente no dice «sólo vimos Ucrania»: dice «exclusivamente Ucrania»**, una afirmación categórica que un proveedor con trece años de seguimiento no hace a la ligera. Se retiene con probabilidad baja y es el objeto del indicador `I-1` | `Poco probable · 20–45 %` |
| **H4 — Hay un segundo clúster bajo el mismo nombre** | Que el ranking de Trellix esté contando como Gamaredon actividad de un actor distinto que comparte firmas o herramientas. No hay ningún indicio de ello en las fuentes, y el expediente de alias (§O-1) es inusualmente limpio. Se consigna para que no se reabra sin evidencia | `Poco probable · 20–45 %` |
| **H5 — El actor amplió objetivos en 2026** | La ventana de Trellix (abr–sep 2026) es posterior a la del whitepaper (2025). Es formalmente posible que la victimología cambiara. **Pero el informe trimestral del mismo proveedor, que cubre exactamente esa ventana, no reporta ampliación geográfica: reporta descenso de actividad.** Dos fuentes del mismo proveedor en la misma ventana lo contradicen | `Poco probable · 20–45 %` |
| **H6 — El ranking es erróneo** | Que haya un fallo de agregación o de etiquetado en el producto de Trellix. No hay base para afirmarlo y las cifras son internamente coherentes entre sus desgloses trimestral, global y por país. **Descartada** por falta de evidencia, no por imposibilidad | `Descartada` |

**Supuesto clave.** Todo el informe asume que **«actividad observada» en el ranking de Trellix significa detecciones y no intrusiones**. Si significara intrusiones confirmadas, H1 cae, `KJ-3` y `KJ-4` caen con ella, y el informe habría que reescribirlo con una tesis distinta: que la victimología de ESET es gravemente incompleta y que tenemos un actor estatal ruso activo en nuestro hemisferio sin perfilar. **No pudimos leer la definición del proveedor** (limitación 3.3-ii, brecha `G-2`), y por tanto este supuesto es el punto más frágil del producto. Está declarado aquí para que cualquiera que consiga la metodología pueda falsarlo en una tarde.

**Pre-mortem.** Es mayo de 2027 y este informe resultó equivocado. La causa más probable: alguien leyó la sección §E-1 como «Gamaredon no importa» en vez de «Gamaredon no nos ataca», desatendió la decisión `E-b`, y un archivador sin parchear fue el vector de un actor completamente distinto que explotó el mismo `CVE-2025-8088`. **El informe habría sido correcto en su análisis y dañino en su efecto**, porque desactivó una preocupación en vez de reorientarla. La segunda causa más probable: el supuesto clave era falso y lo dijimos, pero nadie fue a comprobarlo.

## O-7. Indicadores y señales de alerta

| # | Indicador observable | Qué señalaría | Disciplina | Responsable |
|---|---|---|---|---|
| I-1 | **Informe de primera mano que documente una víctima de Gamaredon fuera de Ucrania** | Invalida `KJ-1`, confirma H3, obliga a revisión anticipada del informe y a reevaluar la pertinencia regional desde cero | OSINT | Célula CTI |
| I-2 | Publicación de la metodología del ranking de Trellix, o de cualquier declaración del proveedor sobre qué cuenta «actividad observada» | Permite falsar o confirmar el supuesto clave de §O-6. Es la brecha `G-2` | OSINT | Célula CTI |
| I-3 | Aparición del modelo de cinco capas de §O-3 —túnel de terceros más *dead drop* en red social más exfiltración a S3— en un actor con victimología latinoamericana | Confirma el escenario de difusión de método. **Es el indicador que convierte este informe en operativo para nosotros** | OSINT / telemetría | Célula CTI / SOC |
| I-4 | Confirmación de primera mano de capacidad destructiva (*wiper*) en el arsenal | Cambia la clase de amenaza del actor. Brecha `G-3` | OSINT | Célula CTI |
| I-5 | Nuevo whitepaper anual del proveedor sobre la actividad de 2026 | Esperable hacia mediados de 2027. Resolverá la tensión entre descenso de actividad y ascenso en el ranking | OSINT | Célula CTI |
| I-6 | Aparición de un servicio de túnel o *worker* nuevo en el arsenal, más allá de los cuatro estándar y los dos en prueba | Obliga a actualizar la lista de servicios de §E-c y las detecciones `D-6` | OSINT | Célula CTI / SOC |
| I-7 | Explotación de `CVE-2025-8088` por cualquier actor contra objetivos de la región | Eleva la prioridad de la decisión `E-b` de 45 días a inmediata | OSINT / CERT regional | Gestión de Vulnerabilidades |
| I-8 | Nueva atribución oficial ucraniana o sanción internacional sobre el grupo | Relevante para cumplimiento y para la cadena de suministro, no para detección | OSINT | Legal / Cumplimiento |

---

# NIVEL TÁCTICO
### Para: Analistas de SOC · Ingeniería de Detección · Threat Hunting · Horizonte: días–semanas

## T-1. Cadena de intrusión

<!-- cti:stages title="Tres etapas, y la segunda no necesita vulnerabilidad" dwell="**Permanencia:** no publicada por la fuente. Las campañas de correo individuales duran de uno a seis días consecutivos, mayoritariamente en día laborable." -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 01 · Entrada | Correo dirigido con archivador o contrabando HTML | `RAR`/`ZIP` adjunto · `XHTML` con contrabando HTML · **`CVE-2025-8088`** desde 2025-09-26 · `mshta.exe` con argumento de URL · descargador `HTA` · `PteroSand` en memoria vía `ExecuteGlobal` |
| Etapa 02 · Propagación | Envenenamiento de medios compartidos, sin exploit | `PteroLNK` en USB y unidades de red · `PteroPaste` en USB · `PteroSetup` sustituye instaladores por archivadores autoextraíbles 7z · LNK con doble extensión y nombres en ucraniano |
| Etapa 03 · Recolección | Robo de ficheros a nube comercial | `PteroPSDoor` y `PteroVDoor` (ficheros por extensión) · `PteroBox` (a Dropbox vía `rclone`) · `PteroSteal` (navegadores) · `PteroGram` (Telegram) · `PteroScout` (sistema) · exfiltración a Wasabi/Tebi/Intercolo, con Tor de reserva |

**Etapa 01 en detalle.** La campaña típica envía correo con adjunto archivador —RAR o ZIP— o con un fichero XHTML que usa contrabando HTML para simular la descarga de ese archivador. En dos campañas el descargador HTA viajó comprimido con bzip2 en lugar de empaquetado. Dentro va un descargador HTA que, al abrirse, lanza `mshta.exe` con un argumento de URL para traer un segundo HTA que incrusta el descargador VBScript `PteroSand`. Éste ejecuta las cargas siguientes **directamente en memoria** mediante la instrucción `ExecuteGlobal` de VBScript. En tres campañas se usaron hipervínculos en vez de adjuntos, enviados en paralelo dentro de las mismas campañas.

Desde el 26 de septiembre de 2025 hay una variante que cambia el modelo de persistencia: el archivador RAR explota `CVE-2025-8088` y, si tiene éxito, **extrae el descargador HTA a la carpeta de Inicio específica del usuario sin que la víctima lo sepa**, de modo que se ejecuta en el siguiente inicio de sesión. El flujo posterior es el mismo; lo que cambia es que ya no hace falta que la víctima abra nada más.

**Etapa 02 en detalle, y es la que debe preocupar a cualquiera.** Aquí no hay vulnerabilidad: hay tres métodos de abuso de confianza.

Los **USB** se envenenan con dos herramientas. `PteroLNK` en su versión VBScript se copia a la unidad y crea ficheros LNK maliciosos; `PteroPaste` deja un script descargador y crea los LNK sin copiarse. En ambos casos la expectativa del actor es que el pendrive se comparta o se lleve a otra máquina. Los LNK son de tres tipos: con nombres tomados de una lista de palabras en ucraniano a los que se añade una **extensión falsa antes de la real** —`СБУ.doc.lnk`, `фото катування.jpeg.lnk`— de modo que el explorador los muestra como documentos legítimos por la configuración por defecto de ocultar extensiones conocidas; con el nombre de **subcarpetas existentes** en la unidad, para que parezcan carpetas; y con el nombre de ficheros existentes de ciertas extensiones, tipo este último que el actor descontinuó a finales de 2025.

Las **unidades de red mapeadas** se envenenan sólo con `PteroLNK`, del mismo modo: escaneo, copia y creación de LNK disfrazados de directorios existentes.

Los **instaladores de software** se envenenan con `PteroSetup`, que es la pieza más taimada del arsenal. Escanea unidades fijas, USB y de red buscando ejecutables cuyo nombre contenga `install`, `setup` o `cronos`, y los **sustituye por archivadores autoextraíbles 7z que contienen el instalador original más un descargador VBScript**. El nombre del fichero se conserva intacto; sólo cambia el contenido. Cuando la víctima lo abre, se ejecutan los dos: el instalador legítimo, que funciona y no levanta sospechas, y el descargador. La herramienta existe desde enero de 2021 y fue resucitada en 2025.

**Etapa 03 en detalle.** Tres ladrones de ficheros operan por extensión sobre todas las unidades mapeadas. La lista de `PteroVDoor`, tras la ampliación del 5 de diciembre de 2025, es: `.7z`, `.csv`, `.doc`, `.docx`, `.jpeg`, `.jpg`, `.mdb`, `.odt`, `.pdf`, `.ps1`, `.rar`, `.rtf`, `.tmp`, `.txt`, `.xls`, `.xlsx`, `.zip`. La de `PteroPSDoor` evolucionó en dirección distinta e informativa: **añadió** `.ai`, `.csv`, `.dot`, `.md`, `.odp`, `.ods`, `.pps`, `.psd`, `.wll`, `.wpd` y `.xps`, y **retiró** `.docx`, `.pptx`, `.vsdx` y `.xlsx`. Retirar los formatos ofimáticos modernos y añadir los antiguos, más diseño gráfico y plantillas, sugiere un objetivo que trabaja con documentación heredada.

El mecanismo de reserva de `PteroPSDoor` merece su propia detección. Si la exfiltración primaria falla, descarga Tor con **BITS** desde el servicio legítimo Filemail, extrae tres ficheros a `%USERPROFILE%\%PROCESSOR_LEVEL%_%PROCESSOR_REVISION%\`, deriva una contraseña de control del timestamp actual y lanza `tor.exe` con `SocksPort 9050 ControlPort 9051`. Después reenvía por `curl.exe` usando el proxy SOCKS5 de Tor. El detalle que delata al operador: **exfiltra a una dirección IP de red abierta, no a un servicio onion**, con lo que todo el montaje de Tor sólo oculta el origen, no el destino.

## T-2. Mapa MITRE ATT&CK

> Construido sobre la tabla del whitepaper, que declara **ATT&CK v19**. Se
> conservan los identificadores de la fuente. La columna de procedimiento está
> reescrita para que sea accionable y no una paráfrasis del nombre de la técnica.

<!-- cti:matrix -->

| Táctica | ID | Técnica | Procedimiento observado |
|---|---|---|---|
| Desarrollo de recursos | T1583.001 | Acquire Infrastructure: Domains | 189 dominios registrados en 2025, mayoría `.ru`, algunos `.online` |
| Desarrollo de recursos | T1583.003 | Acquire Infrastructure: VPS | Servidores alquilados para C2 |
| Desarrollo de recursos | T1583.007 | Acquire Infrastructure: Serverless | C2 escondido detrás de *workers* de Cloudflare (`workers.dev`) |
| Desarrollo de recursos | T1587.001 | Develop Capabilities: Malware | Desarrollo propio: seis herramientas nuevas sólo en 2025 |
| Desarrollo de recursos | T1588.006 | Obtain Capabilities: Vulnerabilities | Armamentización de `CVE-2025-8088` (WinRAR) |
| Desarrollo de recursos | T1608.002 | Stage Capabilities: Upload Tool | Tor alojado en Filemail; `rclone` en servidores propios |
| Acceso inicial | T1566.001 | Spearphishing Attachment | 35 campañas en 2025 con RAR, ZIP o XHTML adjunto |
| Acceso inicial | T1566.002 | Spearphishing Link | Hipervínculos a archivadores, en paralelo dentro de las mismas campañas |
| Ejecución | T1059.001 | PowerShell | Lenguaje de la mitad del arsenal |
| Ejecución | T1059.003 | Windows Command Shell | Ejecución de cargas |
| Ejecución | T1059.005 | Visual Basic | VBScript: la otra mitad del arsenal |
| Ejecución | T1059.007 | JavaScript/JScript | Los LNK que suelta `PteroLNK` usan JavaScript para ejecutar |
| Ejecución | T1203 | Exploitation for Client Execution | `CVE-2025-8088` para ejecución |
| Ejecución | T1559.001 | IPC: Component Object Model | Objeto COM `MSScriptControl.ScriptControl.1` para ejecutar VBScript |
| Ejecución | T1053.005 | Scheduled Task | Ejecución y persistencia |
| Ejecución | T1204.001 | User Execution: Malicious Link | LNK para movimiento lateral |
| Ejecución | T1204.002 | User Execution: Malicious File | HTA en las campañas de correo |
| Ejecución | T1047 | Windows Management Instrumentation | Enumerar unidades conectadas y resolver IP de C2 mediante ping al dominio |
| Persistencia | T1547.001 | Registry Run Keys / Startup Folder | Claves `Run`/`RunOnce` de HKCU y carpeta de Inicio |
| Persistencia | T1547.009 | Shortcut Modification | `PteroBox` crea un LNK en la carpeta de Inicio |
| Persistencia | T1037.001 | Logon Script (Windows) | `PteroPaste` y `PteroPSLoad` fijan el valor `UserInitMprLogonScript` |
| Sigilo | T1197 | BITS Jobs | `PteroPSDoor` descarga Tor con BITS |
| Sigilo | T1140 | Deobfuscate/Decode Files or Information | base64 en toda la cadena |
| Sigilo | T1480.001 | Execution Guardrails: Environmental Keying | **El número de serie del volumen se usa como clave XOR de las cargas** |
| Sigilo | T1480.002 | Execution Guardrails: Mutual Exclusion | Mutex para evitar doble ejecución (Anexo A.2) |
| Sigilo | T1564.001 | Hidden Files and Directories | Ficheros ocultos |
| Sigilo | T1564.003 | Hidden Window | PowerShell con ventana oculta |
| Sigilo | T1564.004 | NTFS File Attributes | **Flujos de datos alternativos** para ocultarse y guardar su C2 |
| Sigilo | T1070.004 | Indicator Removal: File Deletion | Los tres ladrones borran lo preparado tras exfiltrar con éxito |
| Sigilo | T1036.003 | Rename Legitimate Utilities | `PteroBox` descarga `rclone` con otro nombre |
| Sigilo | T1036.004 | Masquerade Task or Service | Tareas con nombres de apariencia benigna (Anexo A.2) |
| Sigilo | T1036.005 | Match Legitimate Name or Location | `PteroLNK` imita ubicaciones legítimas al instalarse |
| Sigilo | T1036.007 | Double File Extension | `.docx.lnk`, `.jpeg.lnk` |
| Sigilo | T1036.008 | Masquerade File Type | Cargas VBScript en ficheros con extensión aleatoria |
| Sigilo | T1027.006 | HTML Smuggling | XHTML adjunto que simula descarga de archivador |
| Sigilo | T1027.009 | Embedded Payloads | Cargas incrustadas |
| Sigilo | T1027.010 | Command Obfuscation | PowerShell codificado en base64 (`-EncodedCommand`) |
| Sigilo | T1027.011 | Fileless Storage | **Herramientas instaladas dentro del registro** |
| Sigilo | T1027.013 | Encrypted/Encoded File | Cargas codificadas y cifradas |
| Sigilo | T1027.015 | Compression | HTA comprimidos con bzip2 y empaquetados en ZIP/RAR |
| Sigilo | T1027.016 | Junk Code Insertion | Código basura insertado en las herramientas |
| Sigilo | T1684.001 | Social Engineering: Impersonation | Suplantación de entidades gubernamentales ucranianas |
| Sigilo | T1684.002 | Social Engineering: Email Spoofing | Falsificación del remitente |
| Sigilo | T1218.005 | Mshta | `mshta.exe` para ejecutar los HTA |
| Sigilo | T1218.011 | Rundll32 | Los LNK de `PteroLNK` usan `rundll32.exe` |
| Degradación de defensas | T1112 | Modify Registry | `PteroLNK` desactiva la visualización de ficheros ocultos en el Explorador |
| Acceso a credenciales | T1555.003 | Credentials from Web Browsers | `PteroSteal` roba credenciales de navegadores |
| Descubrimiento | T1083 | File and Directory Discovery | Búsqueda por extensión de los tres ladrones y de `PteroPaste` |
| Descubrimiento | T1057 | Process Discovery | `PteroScout` enumera procesos |
| Descubrimiento | T1518.001 | Security Software Discovery | **`PteroScout` enumera el software de seguridad instalado** |
| Descubrimiento | T1082 | System Information Discovery | `PteroScout` exfiltra la salida de `systeminfo` |
| Movimiento lateral | T1091 | Replication Through Removable Media | `PteroLNK` y `PteroPaste` por USB |
| Movimiento lateral | T1080 | Taint Shared Content | `PteroLNK` crea en unidades de red LNK disfrazados de directorios existentes |
| Recolección | T1560.002 | Archive via Library | `PteroGram` empaqueta en ZIP antes de exfiltrar |
| Recolección | T1119 | Automated Collection | Búsqueda periódica por extensión |
| Recolección | T1005 | Data from Local System | Unidades locales |
| Recolección | T1039 | Data from Network Shared Drive | Unidades de red mapeadas |
| Recolección | T1025 | Data from Removable Media | USB conectados |
| Recolección | T1074.001 | Local Data Staging | Preparación local antes de exfiltrar |
| Recolección | T1113 | Screen Capture | `PteroScreen` captura pantalla |
| Mando y control | T1071.001 | Web Protocols | HTTP y HTTPS |
| Mando y control | T1132.001 | Standard Encoding | base64 antes de exfiltrar |
| Mando y control | T1568.001 | Fast Flux DNS | Rotación rápida de IP sobre los dominios propios |
| Mando y control | T1573.001 | Symmetric Cryptography | XOR y 3DES |
| Mando y control | T1573.002 | Asymmetric Cryptography | **RSA para cifrar los FQDN de C2 publicados en los *dead drops* ** |
| Mando y control | T1008 | Fallback Channels | Un primario y dos de reserva, en orden variable |
| Mando y control | T1665 | Hide Infrastructure | Cuatro servicios de túnel y *worker* |
| Mando y control | T1105 | Ingress Tool Transfer | Descarga de cargas adicionales |
| Mando y control | T1095 | Non-Application Layer Protocol | `PteroPShell` usa TCP |
| Mando y control | T1571 | Non-Standard Port | `PteroPShell` en puertos no estándar |
| Mando y control | T1572 | Protocol Tunneling | DoH (`1.1.1.1`, `cloudflare-dns.com`) para resolver C2 |
| Mando y control | T1090 | Proxy | `PteroSocks` como proxy SOCKS inverso |
| Mando y control | T1102.001 | Dead Drop Resolver | `telegram.me`, `telegra.ph`, `teletype.in`, `rentry.co`, `write.as`, `dev.to`, `mastodon.social` |
| Mando y control | T1102.003 | One-Way Communication | `PteroGraphin` y `PteroPaste` reciben cargas vía *dead drop* |
| Exfiltración | T1020 | Automated Exfiltration | Exfiltración periódica de lo preparado |
| Exfiltración | T1041 | Exfiltration Over C2 Channel | Por el canal de mando |
| Exfiltración | T1567.002 | Exfiltration to Cloud Storage | **Dropbox, Wasabi, Tebi, Intercolo** |

## T-3. Dónde atacamos en la Pirámide del Dolor

<!-- cti:pyramid -->

| Nivel | Qué contiene en este informe y qué vale | Valor |
|---|---|---|
| Hashes | Anexo A.1: **22 SHA-1, uno por herramienta o variante**, declarados como ejemplo por la propia fuente. No hay SHA-256. Para un arsenal íntegramente en script, con código basura insertado y claves XOR rotadas, el hash cambia en cada entrega. **Sólo retrohunt** | Base · valor trivial |
| IP · Dominios | Anexo A.3: los 26 subdominios de túnel son efímeros y la mayoría ya no existe; los seis `.ru` son el 3 % de los 189 registrados; los catorce servicios de terceros **no se pueden bloquear**. El peor nivel de este informe | Valor bajo, y más bajo que de costumbre |
| Artefactos | **Anexo A.2 es el núcleo del valor de este informe.** Nombres de tarea programada que imitan DirectX, Edge Update y diagnóstico de disco; valores de clave `Run` nombrados con variables de entorno; flujos de datos alternativos sobre `boot.ini` y `ntuser.ini`; mutex `Global\MutexGlobalNewStone*`; rutas con `%PROCESSOR_REVISION%`. **Duran entre compilaciones porque no hay compilación** | Valor medio–alto |
| Herramientas | `mshta.exe`, `rundll32.exe`, `curl.exe`, BITS, `rclone`, `tor.exe`, `7za.exe`, objeto COM `MSScriptControl.ScriptControl.1`. Todas legítimas: detectar por **contexto de invocación**, nunca por presencia | Valor alto |
| TTP | Las cinco capas de infraestructura de §O-3 y los tres métodos de propagación de §T-1. Es lo que el actor no puede cambiar sin rediseñarse, y lo que otros actores van a copiar. **Aquí debe concentrarse todo el esfuerzo** | Cima · valor máximo |

> **Observación de método.** En la mayoría de los informes de esta cartera, los
> artefactos de host son valiosos porque sobreviven a los cambios de
> compilación. Aquí el argumento es más fuerte: **no hay compilación de la que
> sobrevivir.** Un arsenal íntegramente en script no tiene *build pipeline*, no
> tiene *imphash*, no tiene sección de recursos. Lo único estable que produce
> son los nombres que elige para sus tareas, sus claves y sus mutex, y ésos los
> ha mantenido durante años. El Anexo A.2 es, en este expediente, más duradero
> que los hashes del A.1.

## T-4. Hipótesis de caza prioritarias

<!-- cti:accordion critical="^(H-1|H-2|H-3)\b" regional="^H-1[0-2]\b" -->

**H-1 — `mshta.exe` invocado con un argumento de URL.** Buscar en registro de creación de procesos toda ejecución de `mshta.exe` cuya línea de comandos contenga `http://`, `https://` o una ruta UNC. Ventana: 180 días. Es la señal más limpia de la etapa 01 de este actor y de buena parte del malware por correo del mercado. Fidelidad esperada **alta**: `mshta.exe` con URL remota no tiene uso legítimo en un parque corporativo moderno. Falsos positivos: algunas aplicaciones empresariales heredadas de los años 2000 y ciertos paneles de administración antiguos; se enumeran una vez y se excluyen por ruta padre.

**H-2 — Escritura en la carpeta de Inicio del usuario por un proceso de archivador.** Buscar creaciones de fichero en `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\` cuyo proceso creador sea `WinRAR.exe`, `Rar.exe`, `UnRAR.exe`, `7zFM.exe` o cualquier gestor de archivadores. Ventana: todo lo disponible. **Esta es la firma conductual de `CVE-2025-8088` y es independiente de la versión y del actor.** Fidelidad esperada **muy alta**: un extractor de archivadores no tiene ninguna razón legítima para escribir en la carpeta de Inicio. Falsos positivos: prácticamente ninguno; un instalador distribuido como archivador autoextraíble podría hacerlo, y es un caso que conviene conocer de todos modos.

**H-3 — Proceso no navegador accediendo a servicios de *dead drop*.** Buscar conexiones de red hacia `telegra.ph`, `api.telegra.ph`, `teletype.in`, `t.me`, `rentry.co`, `write.as`, `dev.to`, `mastodon.social`, `api.gofile.io`, `lesma.eu`, `nopaste.net` o `pastee.dev` cuyo proceso iniciador **no** sea un navegador conocido. Prestar atención especial a `powershell.exe`, `wscript.exe`, `cscript.exe`, `mshta.exe` y `curl.exe`. Ventana: 90 días. Fidelidad esperada **alta**. Falsos positivos: herramientas de desarrollo que consultan `dev.to`, clientes de Mastodon de escritorio, y scripts de integración propios que publiquen en esas plataformas; se identifican una vez y se excluyen por hash o por ruta.

**H-4 — Tareas programadas con nombres de imitación.** Buscar en el inventario de tareas programadas los nombres del Anexo A.2, en particular los de la forma `Windows\DirectX\DXGIAdapterCache`, `Windows\DirectX\DirectXDatabaseUpdater`, `MicrosoftEdgeUpdateTaskMachineUA`, `MicrosoftUpdateTaskMachineCore`, `Windows\InstallService\ScanForUpdatesAsUser` y `CertificateServicesClient\SystemTask\SilentCleanup`. **El contraste a aplicar no es el nombre sino la acción**: comparar qué ejecuta la tarea con lo que ejecutaría la tarea legítima homónima. Una tarea llamada `MicrosoftEdgeUpdateTaskMachineUA` que lanza `wscript.exe` o `powershell.exe` es concluyente. Fidelidad **muy alta** con el contraste aplicado; **muy baja** sin él, porque varios de esos nombres existen legítimamente.

**H-5 — Valores de clave `Run` nombrados con variables de entorno.** Buscar valores bajo `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` y `RunOnce` cuyo **nombre** coincida con el nombre de usuario, el nombre de dominio o el nombre del equipo, o sea literalmente `regName`, `GooglePhone`, `DXGIAdapterCache`, `DirectXDatabaseUpdater`, `Microsoft-Windows-DiskDiagnosticResolver`, `RecommendedTroubleshootingScanner`, `ScanForUpdatesAsUser` o `ExploitGuard`. Ventana: todo lo disponible. Fidelidad **alta**: el patrón de nombrar una entrada de autoarranque con el nombre del propio equipo es característico y no tiene análogo legítimo.

**H-6 — Flujos de datos alternativos en ficheros de perfil.** Enumerar ADS sobre `%USERPROFILE%\boot.ini`, `%PUBLIC%\ntuser.ini`, `%PUBLIC%\ntuser.dat.LOG1`, `%PUBLIC%\ntuser.dat.LOG2`, `%USERPROFILE%\NTUSER.DAT[123].LOG`, los ficheros `NTUSER.DAT.TMContainer*.regtrans-ms` en `%PUBLIC%`, y el propio directorio de perfil. Nombres de flujo observados: `SRV`, `LNK`, `GTR`, `SERVER`, `URLS`, `IPS`, `URL`, `IP`, `IpURL`, `CloudURL`, `URLTeletype`, `URLTelegra`, `WindowsDetect`, `WindowsTelegra`. Fidelidad **muy alta**: **`boot.ini` no se usa desde Windows XP y no tiene ningún motivo para existir en un perfil de usuario, menos aún con flujos de datos adjuntos.**

**H-7 — `rclone` en rutas de perfil de usuario.** Buscar ficheros en `%APPDATA%\rclone\` —en particular `rclone.exe`, `1.exe` y `rclone.conf`—, y también cualquier binario cuya firma o cadenas correspondan a `rclone` **con otro nombre** en rutas de perfil. Correlacionar con creación de LNK en la carpeta de Inicio con el nombre del equipo (`%COMPUTERNAME%.lnk`) y con tareas programadas llamadas `dropbox`, `%COMPUTERNAME%` o `%COMPUTERNAME%_1`. Fidelidad **alta**. Falsos positivos: `rclone` es una herramienta legítima de sincronización; lo anómalo es su ubicación en perfil de usuario junto a persistencia.

**H-8 — Montaje de Tor con puertos de control.** Buscar ejecuciones de proceso cuya línea de comandos contenga simultáneamente `SocksPort 9050` y `ControlPort 9051`, o contenga `HashedControlPassword` y `AvoidDiskWrites 1`. Buscar también `tor.exe` y ficheros `geoip`/`geoip6` en rutas de perfil con nombre derivado de `%PROCESSOR_LEVEL%_%PROCESSOR_REVISION%`. Correlacionar con trabajos de BITS que descarguen de Filemail. Fidelidad **muy alta**: no hay escenario corporativo legítimo para este montaje.

**H-9 — Mutex de nombre conocido.** Buscar la creación de mutex con los nombres del Anexo A.2: `Global\MutexGlobalNet`, `Global\MutexGlobalNetWind`, `Global\MutexGlobalNetWinds`, `Global\MutexGlobalNewStone`, `Global\MutexGlobalNewStoner`, `Global\MutexGlobalNewStoner1`, `Global\MutexGlobalNewStorm`, `Global\MutexGlobalUP`, `Global\MutexGlobalUPS`, `Global\MutexLaos`, `Global\MutexLaos1`, `Global\MutexNosa`, `Global\MutexNosas`, `Global\MutexTa`, `Global\MutexTanos`, `Global\MutexTanoss`, `Global\MutexTest`, y los patrones `Global\assembly0[01][0-9]` y `Global\assembly30[1-7]`. Fidelidad **muy alta** si hay visibilidad; **la visibilidad es el problema** (§T-5).

**H-10 — Ficheros LNK en recursos compartidos de red con nombre de directorio existente.** Recorrer los recursos compartidos de red y buscar ficheros `.lnk` cuyo nombre base coincida con el de un subdirectorio hermano, y ficheros `.lnk` con doble extensión (`*.doc.lnk`, `*.docx.lnk`, `*.jpeg.lnk`, `*.jpg.lnk`, `*.pdf.lnk`). Fidelidad **alta** y de valor regional: **es el patrón que cualquier actor puede copiar sin desarrollar nada**, y las carpetas compartidas de cualquier organización son vulnerables a él. Falsos positivos: accesos directos creados legítimamente por usuarios; el doble criterio (coincidencia con directorio hermano, o doble extensión) los reduce mucho.

**H-11 — Instaladores sustituidos por autoextraíbles.** Buscar en unidades fijas y compartidas ejecutables cuyo nombre contenga `install`, `setup` o `cronos` y cuyo contenido sea un archivador autoextraíble 7z que incluya más de un fichero ejecutable o un script. Buscar también artefactos de `PteroSetup` en `%TEMP%`: `install.vbs`, `config.txt`, `7za.exe`, `7za.dll`, `7z.sfx`, `archive.7z`, `start.exe`, `1.exe`. Fidelidad **moderada** y coste alto, pero es la única forma de encontrar esta clase de envenenamiento. De valor regional por la misma razón que `H-10`.

**H-12 — Egreso a almacenamiento S3 no autorizado.** Buscar conexiones a `wasabisys.com`, `tebi.io`, `de-fra.i3storage.com` y, de forma general, a extremos compatibles con S3 que no estén en la lista autorizada de la decisión `E-c`. Ventana: 90 días. **Requiere que la lista exista**: sin ella esta hipótesis no es ejecutable, y por eso `E-c` es una decisión y no una tarea. Fidelidad dependiente por completo de la calidad de la lista.

## T-5. Brechas de visibilidad que hay que cerrar primero

| Brecha | Por qué importa aquí |
|---|---|
| **Sin registro de bloque de script de PowerShell (EID 4104)** | Es la brecha dominante. Un actor cuyo arsenal entero es PowerShell y VBScript ejecutado en memoria mediante `ExecuteGlobal` e `Invoke-Expression` es **completamente invisible** sin este registro. Deja ciegas `H-1`, `H-3` y toda la etapa 03 |
| Sin línea de comandos completa en creación de procesos | Deja ciegas `H-1` y `H-8`, que dependen de inspeccionar argumentos. Es la configuración más barata de las tres y la de mayor rendimiento inmediato |
| Sin visibilidad de creación de mutex | Deja ciega `H-9` por completo. Requiere EDR con telemetría de objetos del núcleo; no se obtiene con auditoría nativa |
| Sin inventario ni auditoría de tareas programadas | Deja ciega `H-4`, que es la hipótesis de mayor fidelidad del informe cuando se aplica el contraste de acción |
| Sin enumeración de flujos de datos alternativos | Deja ciega `H-6`. Las herramientas de inventario ordinarias no los ven; hace falta una pasada específica |
| Sin inventario de software no gestionado | Deja sin responder `X-1` y `X-2`, y con ello la decisión `E-b`. **Sin saber cuántos WinRAR hay y en qué versión, no se puede cerrar la única exposición directa de este informe** |
| Sin lista de servicios de nube y túnel autorizados | Deja ciegas `H-12` y parcialmente `H-3`. Es la decisión `E-c` y es organizativa, no técnica |
| Sin registro de trabajos de BITS | Deja parcialmente ciega `H-8`, y BITS es un canal de descarga que varios actores de esta cartera usan |
| Sin visibilidad en recursos compartidos de red | Deja ciegas `H-10` y `H-11`. La propagación por contenido compartido es el método **más transferible** de todo el expediente |

---

# NIVEL TÉCNICO
### Para: Ingeniería de detección · Automatización · TIP/SIEM · Vida útil: las detecciones conductuales no caducan; los indicadores sí, y rápido

## X-1. Arsenal y capacidad

| Propiedad | Valor |
|---|---|
| Lenguajes | **VBScript y PowerShell, exclusivamente.** Ninguna herramienta compilada en las 26 documentadas. Algunas existen en ambos lenguajes (`PteroLNK`, `PteroScout`, `PteroSteal`) |
| Ofuscación | base64 (`-EncodedCommand`), ROT13, XOR con claves largas y rotadas frecuentemente para resistir fuerza bruta, 3DES, inserción de código basura, cargas incrustadas, extensiones de fichero aleatorias |
| Criptografía | XOR y 3DES para cargas; **RSA para cifrar los FQDN de C2 publicados en *dead drops*, con clave única por instancia** de `PteroPSDoor` |
| Guardarraíl de entorno | **El número de serie del volumen del sistema se usa como clave XOR.** Consecuencia para el análisis: una muestra extraída de una máquina no se descifra en otra, y el *sandbox* no la ejecuta |
| Plataformas | Windows, exclusivamente |
| Persistencia | Clave `Run`/`RunOnce` de HKCU, carpeta de Inicio, tareas programadas, valor `UserInitMprLogonScript`, y **almacenamiento del propio código dentro del registro** |
| Almacenamiento sin fichero | Código de herramienta guardado en valores de registro de nombre aleatorio (`[a-zA-Z0-9]{19,25}`) bajo `HKCU\Software`, `HKCU\Abstractions`, `HKCU\AppEvents`, `HKCU\Printers`, `HKCU\Cursors`, `HKCU\EUDC`, `HKCU\Keyboard Layout` y `HKCU\Console`. En octubre de 2025 `PteroPSDoor` añadió cifrado XOR sobre el base64 |
| Canal de C2 | HTTP/HTTPS sobre túneles y *workers* de terceros, con uno primario y dos de reserva en orden variable; dominios propios como último recurso; `PteroPShell` usa TCP en puertos no estándar |
| Resolución de C2 | *Dead drops* en nueve servicios; DoH de Cloudflare (`1.1.1.1`, `cloudflare-dns.com`); resolvedores DNS web (`check-host.net`, `whatsmydns.net`); DNS del sistema; DNS de flujo rápido sobre dominios propios |
| Exfiltración | S3 comercial (Wasabi `wasabisys.com`, Tebi `tebi.io`, Intercolo `de-fra.i3storage.com`), Dropbox vía `rclone`, canal de C2, y **Tor de reserva hacia IP de red abierta** |
| Binarios legítimos abusados | `mshta.exe`, `rundll32.exe`, `curl.exe`, `wscript.exe`, `cscript.exe`, BITS, `rclone`, `tor.exe`, `7za.exe`, objeto COM `MSScriptControl.ScriptControl.1` |
| Capacidad destructiva | **No sostenida en este informe.** La fuente de primera mano no documenta ningún *wiper*; la afirmación circula en cobertura secundaria. Brecha `G-3` |
| Capacidad de movimiento lateral | Tres vectores, ninguno con exploit: USB, unidades de red mapeadas e instaladores de software sustituidos |
| Disciplina operativa | Campañas de uno a seis días, mayoritariamente en día laborable; **actualizaciones concentradas antes de festivos rusos y crimeos, ninguna durante ni después** |

## X-2. Artefactos de host persistentes

<!-- cti:cards -->

| Categoría | Artefactos | Etiqueta |
|---|---|---|
| Tareas que imitan DirectX | `Windows\DirectX\DXGIAdapterCache` · `Windows\DirectX\DirectXDatabaseUpdater` | `PteroLNK v2` |
| Tareas que imitan actualización de Edge | `MicrosoftEdgeUpdateTaskMachineUA` · `MicrosoftEdgeUpdateTaskMachineCore` · `MicrosoftUpdateTaskMachineUA` · `MicrosoftUpdateTaskMachineCore` | `PteroLNK v3` |
| Tareas que imitan diagnóstico y mantenimiento | `Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticResolver` · `DiskDiagnostic\Microsoft\Windows\DiskDiagnosticDataCollector` · `CertificateServicesClient\SystemTask\SilentCleanup` · `InstallService\ScanForUpdatesServer\SmartRetry` · `Windows\InstallService\ScanForUpdatesAsUser` · `Windows\Software\Microsoft\TroubleshootingScanner\RecommendedTroubleshootingScanner` · `Windows\DeviceDirectoryClient\RegisterDeviceConnectedToNetwork` · `Windows\DeviceDirectoryClient\RegisterUserDevice` | `PteroLNK v2` |
| Tareas con nombre de variable de entorno | `%PROCESSOR_IDENTIFIER%` (nombre y descripción) · `dropbox` · `%COMPUTERNAME%` · `%COMPUTERNAME%_1` | `PteroPaste · PteroBox` |
| Valores de clave `Run` | `DXGIAdapterCache` · `DirectXDatabaseUpdater` · `Microsoft-Windows-DiskDiagnosticResolver` · `RecommendedTroubleshootingScanner` · `ScanForUpdatesAsUser` · `ExploitGuard` (en `RunOnce`) · `GooglePhone` · `%USERNAME%` · `%USERNAME%_%USERNAME%` · `%USERDOMAIN%` · `%COMPUTERNAME%` · `%COMPUTERNAME%2` · `regName` | `persistencia` |
| Flujos de datos alternativos | Sobre `%USERPROFILE%\boot.ini`: `:SRV` `:LNK` `:GTR` `:SERVER` `:URLS` `:IPS` `:URL` `:IP` `:IpURL` `:CloudURL` `:URLTeletype` `:WindowsDetect` `:URLTelegra` `:WindowsTelegra`. Sobre `%PUBLIC%\ntuser.ini`: `:SRV` `:LNK`. Sobre el propio perfil: `%USERPROFILE%:SERVER` `:LNK` `:GTR` `:URL` | `PteroLNK v2` |
| Ficheros señuelo de perfil | `%USERPROFILE%\boot.ini` · `%USERPROFILE%\NTUSER.DAT1.LOG` `DAT2.LOG` `DAT3.LOG` · `%PUBLIC%\ntuser.dat.LOG1` `LOG2` · `%PUBLIC%\NTUSER.DAT.TMContainer00000000000000000001.regtrans-ms` y `...0002.regtrans-ms` | `PteroLNK v2` |
| Rutas de instalación con nombre de carpeta legítima | `%APPDATA%\{WindowsPowerShell\|Windows\|VirtualStore\|MSBuild\|cache\|Microsoft\|Internet\|Microsoft.NET\|Defender\|CrashDumps}\desktops.ini` y variantes `desktop.dat`, `desktops.vbs`, `desktop.vbs`, `desktops.sys`, `desktop.sys`, `desktop.con`, `desktop.in`, `desktop.co`, `desktop.ko`, `index.xml`, `index.htm` | `PteroLNK v3` |
| Mutex de `PteroPSDoor` | `Global\MutexGlobalNet` · `MutexGlobalNetWind` · `MutexGlobalNetWinds` · `MutexGlobalNewStone` · `MutexGlobalNewStoner` · `MutexGlobalNewStoner1` · `MutexGlobalNewStorm` · `MutexGlobalUP` · `MutexGlobalUPS` · patrones `Global\assembly0[01][0-9]` y `Global\assembly30[1-7]` | `mutex` |
| Mutex de `PteroPSLoad` | `Global\MutexLaos` · `MutexLaos1` · `MutexNosa` · `MutexNosas` · `MutexTa` · `MutexTanos` · `MutexTanoss` · `MutexTest` | `mutex` |
| Artefactos de `PteroPaste` | `HKCU\EUDC\first` `\knok` `\runner` `\usb` `\privateKeyXml` · `volumeinfo.ps1` · `test.ps1` · `%PROCESSOR_REVISION%.ps1` · mutex `Local\[0-9]{4}(0[1-9]|1[1-2])` | `PteroPaste` |
| Artefactos de `PteroSetup` en `%TEMP%` | `install.vbs` · `config.txt` · `7za.exe` · `7za.dll` · `7z.sfx` · `archive.7z` · `start.exe` · `1.exe` | `PteroSetup` |
| Artefactos de `PteroBox` | `HKCU\Keyboard Layout\{getListFile\|usb\|GetFileMD5\|sendFile\|listPrepare\|update}` · `%LOCALAPPDATA%\info.vbs` · `%APPDATA%\rclone\rclone.exe` y `1.exe` y `rclone.conf` · LNK de Inicio `%COMPUTERNAME%.lnk` | `PteroBox` |
| Artefactos de Tor de `PteroPSDoor` | `%USERPROFILE%\%PROCESSOR_LEVEL%_%PROCESSOR_REVISION%\data\geoip` y `\geoip6` y `\tor\tor.exe` | `PteroPSDoor` |
| Nombres de LNK en ucraniano | `для службового користування.lnk` · `Прибуття.lnk` · `Вибуття.lnk` · `ФОТО.lnk` · `Акти.lnk` · `ЖБД.lnk` · `Доповіді 2025.lnk` · `БпЛА.lnk` · `СЗЧ.lnk` · `таємно.lnk` · `Нова папка.lnk` · `Нова папка (2).lnk` | `señuelo` |

> ⚠ **Advertencia sobre las variables de entorno.** Varios de los artefactos
> anteriores están escritos con variables (`%COMPUTERNAME%`,
> `%PROCESSOR_REVISION%`, `%USERNAME%`). **No son literales**: el actor los
> resuelve en tiempo de ejecución, de modo que en cada máquina el nombre de la
> tarea o del valor de registro es distinto. La detección no puede buscar la
> cadena; tiene que **comparar el nombre encontrado con el valor de esa variable
> en esa máquina**. Es lo que hace `D-3` y es la razón de que esa regla sea más
> complicada de lo que parece.

## X-3. Lógica de detección prioritaria

<!-- cti:detections -->

**D-1 · CRÍTICO — Extractor de archivadores escribiendo en la carpeta de Inicio (`CVE-2025-8088`)**

```
event.category == "file" AND event.type == "creation"
AND file.path CONTAINS "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
AND process.name IN_CASE_INSENSITIVE (
      "winrar.exe", "rar.exe", "unrar.exe", "wincmp32.exe",
      "7zfm.exe", "7zg.exe", "7z.exe", "peazip.exe", "bandizip.exe" )
```

→ **Contención automática sin escalado humano**: aislar el equipo y suspender la sesión. Un extractor de archivadores no escribe en la carpeta de Inicio en ningún flujo legítimo. Esta regla es **independiente del actor y de la versión de WinRAR**: detecta la explotación del recorrido de ruta, no a Gamaredon. Es la detección de mayor relación valor/coste del informe.

**D-2 · CRÍTICO — `mshta.exe` con destino remoto**

```
process.name == "mshta.exe"
AND ( process.command_line MATCHES_REGEX "(?i)https?://"
      OR process.command_line MATCHES_REGEX "(?i)\\\\\\\\[a-z0-9._-]+\\\\"
      OR process.command_line CONTAINS_ANY ("javascript:", "vbscript:") )
```

→ Contención automática. Si `mshta.exe` no es necesario en la organización —y en un parque moderno no lo es—, la acción correcta no es detectar sino **bloquear la ejecución del binario por política**, y esta regla pasa a ser verificación de que el bloqueo funciona.

**D-3 · ALTO — Entrada de autoarranque nombrada con una variable de entorno de la propia máquina**

```
registry.path MATCHES_REGEX
  "(?i)\\\\CurrentVersion\\\\Run(Once)?\\\\(.+)$"
AND registry.value_name IN_CASE_INSENSITIVE (
      host.name, host.name + "2", user.name,
      user.name + "_" + user.name, user.domain )
```

```
# Variante por lista literal, para plataformas sin comparación dinámica:
registry.path MATCHES_REGEX "(?i)\\\\CurrentVersion\\\\Run(Once)?\\\\"
AND registry.value_name IN_CASE_INSENSITIVE (
      "regName", "GooglePhone", "ExploitGuard",
      "DXGIAdapterCache", "DirectXDatabaseUpdater",
      "Microsoft-Windows-DiskDiagnosticResolver",
      "RecommendedTroubleshootingScanner", "ScanForUpdatesAsUser" )
```

→ Investigación prioritaria con plazo de una hora. La primera variante es la valiosa y requiere que la plataforma permita comparar el nombre del valor con atributos del host; la segunda es el sustituto degradado.

**D-4 · ALTO — Flujo de datos alternativo sobre fichero de perfil, o existencia de `boot.ini` en un perfil**

```
( file.path MATCHES_REGEX "(?i)\\\\Users\\\\[^\\\\]+\\\\boot\\.ini(:[A-Za-z]+)?$" )
OR ( file.path MATCHES_REGEX "(?i)\\\\Users\\\\Public\\\\ntuser\\.ini:[A-Za-z]+$" )
OR ( file.path MATCHES_REGEX
       "(?i)\\\\Users\\\\[^\\\\]+\\\\NTUSER\\.DAT[123]\\.LOG$" )
OR ( file.path MATCHES_REGEX "(?i)\\\\Users\\\\[^\\\\]+:(SERVER|LNK|GTR|URL|URLS|IPS)$" )
```

→ Investigación prioritaria. **`boot.ini` no se usa desde Windows XP**; su presencia en un directorio de perfil de usuario, con o sin flujos adjuntos, no tiene explicación legítima en ningún sistema soportado.

**D-5 · ALTO — Intérprete de scripts accediendo a un servicio de *dead drop***

```
network.direction == "outbound"
AND process.name IN_CASE_INSENSITIVE (
      "powershell.exe", "pwsh.exe", "wscript.exe", "cscript.exe",
      "mshta.exe", "curl.exe", "bitsadmin.exe", "certutil.exe", "rundll32.exe" )
AND destination.domain ENDS_WITH_ANY (
      "telegra.ph", "teletype.in", "t.me", "telegram.me",
      "rentry.co", "write.as", "dev.to", "mastodon.social",
      "gofile.io", "lesma.eu", "nopaste.net", "pastee.dev",
      "check-host.net", "whatsmydns.net", "filemail.com" )
```

→ Investigación prioritaria con plazo de una hora. **Esta es la detección más transferible del informe**: no busca a Gamaredon, busca el patrón de *dead drop resolver*, que cualquier actor puede adoptar y que `KJ-5` prevé que se adopte. Nótese que el criterio es el **proceso**, no el destino: estos dominios son todos legítimos y ninguno debe bloquearse.

**D-6 · MEDIO — Intérprete de scripts hacia servicio de túnel o *worker***

```
network.direction == "outbound"
AND process.name IN_CASE_INSENSITIVE (
      "powershell.exe", "pwsh.exe", "wscript.exe", "cscript.exe",
      "mshta.exe", "curl.exe", "rundll32.exe" )
AND destination.domain MATCHES_REGEX
  "(?i)\\.(trycloudflare\\.com|workers\\.dev|devtunnels\\.ms|loophole\\.site|loca\\.lt|bore\\.pub)$"
```

→ Investigación en el día. **Requiere la lista de excepciones de la decisión `E-c`**: en una organización con desarrollo propio, `devtunnels.ms` y `trycloudflare.com` tienen uso legítimo abundante, pero **no desde `wscript.exe`**. Si la organización no tiene desarrollo, esta regla sube a ALTO.

**D-7 · MEDIO — `rclone` o utilidad de sincronización en ruta de perfil**

```
( file.path MATCHES_REGEX "(?i)\\\\AppData\\\\Roaming\\\\rclone\\\\" )
OR ( process.executable MATCHES_REGEX "(?i)\\\\AppData\\\\(Roaming|Local)\\\\.*\\.exe$"
     AND process.command_line CONTAINS_ANY (
           "--config", "lsjson", "copyto", "moveto", ":dropbox", "obscure" ) )
```

→ Investigación en el día. La segunda condición captura `rclone` renombrado, que es lo que `PteroBox` hace: descarga la utilidad legítima bajo otro nombre.

**D-8 · ALTO — Montaje de Tor con puerto de control**

```
process.command_line CONTAINS "SocksPort 9050"
AND process.command_line CONTAINS "ControlPort 9051"
```

```
# Variante independiente de los puertos concretos:
process.command_line CONTAINS "HashedControlPassword"
AND process.command_line CONTAINS "AvoidDiskWrites"
```

→ Contención automática. No existe ningún escenario corporativo legítimo en el que un proceso levante Tor con contraseña de control derivada y escritura a disco desactivada.

**D-9 · MEDIO — Tarea programada con nombre de imitación y acción incoherente**

```
event.code == 4698            # Tarea programada creada
AND task.name IN_CASE_INSENSITIVE (
      "MicrosoftEdgeUpdateTaskMachineUA", "MicrosoftEdgeUpdateTaskMachineCore",
      "MicrosoftUpdateTaskMachineUA", "MicrosoftUpdateTaskMachineCore",
      "DXGIAdapterCache", "DirectXDatabaseUpdater",
      "Microsoft-Windows-DiskDiagnosticResolver", "DiskDiagnosticDataCollector",
      "RecommendedTroubleshootingScanner", "ScanForUpdatesAsUser",
      "SmartRetry", "SilentCleanup",
      "RegisterDeviceConnectedToNetwork", "RegisterUserDevice" )
AND task.action.executable NOT IN_CASE_INSENSITIVE (
      "\\Program Files (x86)\\Microsoft\\EdgeUpdate\\MicrosoftEdgeUpdate.exe",
      "C:\\Windows\\System32\\dxgiadaptercache.exe",
      "C:\\Windows\\System32\\rdrleakdiag.exe",
      "C:\\Windows\\System32\\cleanmgr.exe",
      "C:\\Windows\\System32\\dstokenclean.exe" )
```

→ Investigación prioritaria. **El criterio decisivo es la segunda condición.** Varios de estos nombres existen legítimamente; lo anómalo es que la tarea lance `wscript.exe`, `cscript.exe`, `powershell.exe`, `mshta.exe` o un ejecutable en ruta de perfil. La lista de rutas legítimas debe completarse contra el parque propio antes de poner la regla en producción.

**D-10 · MEDIO — Exfiltración a almacenamiento S3 no autorizado**

```
network.direction == "outbound"
AND ( destination.domain ENDS_WITH_ANY (
        "wasabisys.com", "tebi.io", "i3storage.com" )
      OR destination.domain MATCHES_REGEX "(?i)\\.s3[.-][a-z0-9-]+\\.[a-z.]+$" )
AND destination.domain NOT IN ( <lista autorizada — decisión E-c> )
AND network.bytes_out > 10485760
```

→ Investigación en el día, con umbral de volumen para reducir ruido. **Sin la lista autorizada esta regla es inservible**, y por eso `E-c` figura como decisión de Dirección y no como tarea de SOC.

**D-11 · MEDIO — Objeto COM de ejecución de scripts instanciado por proceso no esperado**

```
registry.path CONTAINS "MSScriptControl.ScriptControl"
OR ( process.command_line CONTAINS "MSScriptControl.ScriptControl" )
```

→ Investigación en el día. Es el puente que varias herramientas del actor usan para ejecutar VBScript desde PowerShell y viceversa, y apenas tiene uso legítimo en software moderno.

**D-12 · BAJO — LNK con doble extensión en recurso compartido o medio extraíble**

```
event.type == "creation"
AND file.extension == "lnk"
AND file.name MATCHES_REGEX "(?i)\\.(docx?|xlsx?|pptx?|pdf|jpe?g|png|rtf|txt|zip|rar)\\.lnk$"
AND ( file.path MATCHES_REGEX "^\\\\\\\\" OR volume.type IN ("removable", "network") )
```

→ Investigación en el día, y **cuarentena del medio** si es extraíble. Fidelidad moderada por sí sola; alta si se correlaciona con `D-5` o `D-6` en la misma máquina.

> ⚠ **Regla de operación.** Las cuatro detecciones marcadas para contención
> automática —`D-1`, `D-2`, `D-8` y, cuando `mshta.exe` esté bloqueado por
> política, la verificación de ese bloqueo— lo están porque describen
> condiciones **sin uso legítimo conocido**, no porque el actor sea rápido. De
> hecho este actor no es rápido: sus campañas duran días y su exfiltración es
> periódica. El argumento para automatizar aquí es otro: son reglas cuya
> investigación manual no aportaría información que la propia regla no contenga
> ya. El resto exige criterio humano, y en particular `D-6`, `D-9` y `D-10` **no
> deben ponerse en producción antes de construir sus listas de excepción**: en un
> parque con desarrollo propio generarían ruido suficiente para que se desactiven
> y no se vuelvan a mirar.

## X-4. Consultas de caza

```kql
// H-2 · CVE-2025-8088: extractor de archivadores escribiendo en la carpeta de Inicio.
// Microsoft Defender XDR / Advanced Hunting. Ventana: todo lo disponible.
DeviceFileEvents
| where ActionType in ("FileCreated", "FileRenamed", "FileModified")
| where FolderPath has @"\Microsoft\Windows\Start Menu\Programs\Startup"
| where InitiatingProcessFileName in~ (
      "winrar.exe","rar.exe","unrar.exe","7zfm.exe","7zg.exe","7z.exe",
      "peazip.exe","bandizip.exe","wincmp32.exe")
| project Timestamp, DeviceName, AccountName, FileName, FolderPath,
          InitiatingProcessFileName, InitiatingProcessCommandLine,
          InitiatingProcessVersionInfoProductVersion
| order by Timestamp desc
```

```kql
// H-1 · mshta.exe con destino remoto.
DeviceProcessEvents
| where FileName =~ "mshta.exe"
| where ProcessCommandLine matches regex @"(?i)(https?://|\\\\[a-z0-9._-]+\\|javascript:|vbscript:)"
| project Timestamp, DeviceName, AccountName, ProcessCommandLine,
          InitiatingProcessFileName, InitiatingProcessCommandLine
| order by Timestamp desc
```

```kql
// H-3 · Intérpretes de script accediendo a servicios de dead drop.
// El criterio es el proceso: estos dominios son legítimos y NO deben bloquearse.
let deaddrops = dynamic([
    "telegra.ph","api.telegra.ph","teletype.in","t.me","telegram.me",
    "rentry.co","write.as","dev.to","mastodon.social","api.gofile.io",
    "lesma.eu","nopaste.net","pastee.dev","check-host.net","whatsmydns.net"]);
DeviceNetworkEvents
| where RemoteUrl has_any (deaddrops) or RemoteDnsQuery has_any (deaddrops)
| where InitiatingProcessFileName in~ (
      "powershell.exe","pwsh.exe","wscript.exe","cscript.exe","mshta.exe",
      "curl.exe","bitsadmin.exe","certutil.exe","rundll32.exe")
| summarize Intentos = count(), Primero = min(Timestamp), Ultimo = max(Timestamp),
            Destinos = make_set(RemoteUrl, 20)
          by DeviceName, AccountName, InitiatingProcessFileName,
             InitiatingProcessCommandLine
| order by Intentos desc
```

```kql
// H-5 · Entradas de autoarranque nombradas con el nombre del propio equipo o usuario.
// La comparación dinámica es lo que da el valor; la lista literal es el respaldo.
DeviceRegistryEvents
| where ActionType in ("RegistryValueSet","RegistryKeyCreated")
| where RegistryKey has @"\CurrentVersion\Run"
| extend Equipo = tostring(split(DeviceName, ".")[0])
| where RegistryValueName =~ Equipo
     or RegistryValueName =~ strcat(Equipo, "2")
     or RegistryValueName =~ InitiatingProcessAccountName
     or RegistryValueName in~ ("regName","GooglePhone","ExploitGuard",
          "DXGIAdapterCache","DirectXDatabaseUpdater",
          "Microsoft-Windows-DiskDiagnosticResolver",
          "RecommendedTroubleshootingScanner","ScanForUpdatesAsUser")
| project Timestamp, DeviceName, InitiatingProcessAccountName,
          RegistryKey, RegistryValueName, RegistryValueData
| order by Timestamp desc
```

```kql
// H-6 · boot.ini en perfil de usuario y flujos de datos alternativos asociados.
// boot.ini no se usa desde Windows XP: su presencia en un perfil es anómala por sí sola.
DeviceFileEvents
| where FolderPath matches regex @"(?i)\\Users\\[^\\]+\\boot\.ini"
     or FolderPath matches regex @"(?i)\\Users\\Public\\ntuser\.ini"
     or FileName matches regex @"(?i)^NTUSER\.DAT[123]\.LOG$"
     or FolderPath matches regex @"(?i)\\Users\\[^\\]+:(SERVER|LNK|GTR|URL|URLS|IPS)$"
| project Timestamp, DeviceName, ActionType, FileName, FolderPath,
          InitiatingProcessFileName, InitiatingProcessCommandLine
| order by Timestamp desc
```

```kql
// H-8 · Montaje de Tor con puerto de control, y descarga previa por BITS.
union
( DeviceProcessEvents
  | where ProcessCommandLine has_all ("SocksPort", "ControlPort")
       or ProcessCommandLine has_all ("HashedControlPassword", "AvoidDiskWrites")
  | project Timestamp, DeviceName, Señal = "tor-montaje",
            Detalle = ProcessCommandLine, AccountName ),
( DeviceNetworkEvents
  | where RemoteUrl has "filemail.com"
  | where InitiatingProcessFileName in~ ("bitsadmin.exe","svchost.exe","powershell.exe")
  | project Timestamp, DeviceName, Señal = "descarga-filemail",
            Detalle = RemoteUrl, AccountName = InitiatingProcessAccountName )
| order by Timestamp desc
```

```kql
// H-7 · rclone, con su nombre o renombrado, en rutas de perfil de usuario.
DeviceProcessEvents
| where FolderPath matches regex @"(?i)\\Users\\[^\\]+\\AppData\\"
| where ProcessCommandLine has_any ("lsjson","copyto","moveto","obscure","--config")
     or FolderPath has @"\rclone\"
     or ProcessVersionInfoOriginalFileName =~ "rclone.exe"
| project Timestamp, DeviceName, AccountName, FileName, FolderPath,
          ProcessVersionInfoOriginalFileName, ProcessCommandLine, SHA256
| order by Timestamp desc
```

```kql
// H-10 y H-12 · LNK con doble extensión en medios extraíbles y recursos compartidos.
DeviceFileEvents
| where ActionType == "FileCreated" and FileName endswith ".lnk"
| where FileName matches regex @"(?i)\.(docx?|xlsx?|pptx?|pdf|jpe?g|png|rtf|txt|zip|rar)\.lnk$"
     or FolderPath startswith @"\\"
| summarize Creados = count(), Nombres = make_set(FileName, 30)
          by DeviceName, FolderPath, InitiatingProcessFileName
| where Creados > 1
| order by Creados desc
```

```yaml
# Sigma — Extractor de archivadores escribiendo en la carpeta de Inicio (CVE-2025-8088)
# Autor: Célula CTI · Fecha: 2026-11-17 · ATT&CK: T1203, T1547.001, T1588.006
# Nivel: critical · Estado: estable
# Independiente del actor: detecta la explotación del recorrido de ruta, no a Gamaredon.
title: Archivador escribe en la carpeta de Inicio del usuario
id: 7c1f4ad2-5e83-4b0a-9f6c-2d8a1e4b73c5
status: stable
description: >
  Un gestor de archivadores crea un fichero en la carpeta de Inicio del usuario.
  Es la firma conductual de la explotación de CVE-2025-8088 en WinRAR y de
  cualquier recorrido de ruta equivalente en otro extractor.
references:
  - https://web-assets.esetstatic.com/wls/en/papers/white-papers/gamaredon-in-2025.pdf
logsource:
  category: file_event
  product: windows
detection:
  seleccion_proceso:
    Image|endswith:
      - '\WinRAR.exe'
      - '\Rar.exe'
      - '\UnRAR.exe'
      - '\7zFM.exe'
      - '\7zG.exe'
      - '\7z.exe'
      - '\PeaZip.exe'
      - '\Bandizip.exe'
  seleccion_ruta:
    TargetFilename|contains: '\Microsoft\Windows\Start Menu\Programs\Startup\'
  condition: seleccion_proceso and seleccion_ruta
falsepositives:
  - Instaladores distribuidos como archivador autoextraíble que registran
    arranque automático. Caso infrecuente y que conviene conocer igualmente.
level: critical
```

```yaml
# Sigma — Intérprete de scripts resolviendo C2 en un servicio legítimo (dead drop)
# Autor: Célula CTI · Fecha: 2026-11-17 · ATT&CK: T1102.001, T1102.003, T1059
# Nivel: high · Estado: experimental
# Los dominios son servicios legítimos: el criterio es el PROCESO. No bloquear los destinos.
title: Dead drop resolver consultado por un interprete de scripts
id: b3e9d0c7-4a16-47f2-8c5b-9ae2f1d06b84
status: experimental
description: >
  Un intérprete de scripts o una utilidad de transferencia contacta con un
  servicio de publicación, mensajería o pegado usado como dead drop resolver.
  Patrón de alta transferibilidad entre actores.
logsource:
  category: dns_query
  product: windows
detection:
  seleccion_proceso:
    Image|endswith:
      - '\powershell.exe'
      - '\pwsh.exe'
      - '\wscript.exe'
      - '\cscript.exe'
      - '\mshta.exe'
      - '\curl.exe'
      - '\bitsadmin.exe'
      - '\certutil.exe'
      - '\rundll32.exe'
  seleccion_destino:
    QueryName|endswith:
      - 'telegra.ph'
      - 'teletype.in'
      - 't.me'
      - 'telegram.me'
      - 'rentry.co'
      - 'write.as'
      - 'dev.to'
      - 'mastodon.social'
      - 'gofile.io'
      - 'lesma.eu'
      - 'nopaste.net'
      - 'pastee.dev'
      - 'check-host.net'
      - 'whatsmydns.net'
  condition: seleccion_proceso and seleccion_destino
falsepositives:
  - Scripts internos de integración o publicación que usen estas plataformas.
    Enumerar una vez y excluir por hash o por ruta del script.
level: high
```

```yaml
# Sigma — boot.ini en directorio de perfil de usuario
# Autor: Célula CTI · Fecha: 2026-11-17 · ATT&CK: T1564.004, T1027.011
# Nivel: high · Estado: estable
# boot.ini no se usa desde Windows XP. En un perfil de usuario no tiene explicacion.
title: Fichero boot.ini creado en un directorio de perfil de usuario
id: 1f8b6c40-3d27-4e9a-b015-7c4de2a98f36
status: stable
description: >
  PteroLNK usa %USERPROFILE%\boot.ini como contenedor de flujos de datos
  alternativos donde almacena su descargador, su dropper de LNK y su lógica de
  resolución de C2. El fichero es un vestigio de Windows XP y su presencia en un
  perfil de usuario de un sistema soportado es anómala por sí sola.
logsource:
  category: file_event
  product: windows
detection:
  seleccion:
    TargetFilename|re: '(?i)\\Users\\[^\\]+\\boot\.ini'
  condition: seleccion
falsepositives:
  - Restos de migración desde equipos muy antiguos. Verificar fecha y proceso creador.
level: high
```

```yaml
# Sigma — Montaje de Tor con puerto de control para exfiltracion de reserva
# Autor: Célula CTI · Fecha: 2026-11-17 · ATT&CK: T1572, T1090, T1197
# Nivel: critical · Estado: estable
title: Proceso levanta Tor con ControlPort y escritura a disco desactivada
id: 9d2a7f13-6b84-4c05-a3e9-5f1c8b0d47ea
status: stable
description: >
  PteroPSDoor descarga Tor con BITS desde Filemail y lo levanta con SocksPort
  9050 y ControlPort 9051, con contraseña de control derivada del timestamp,
  para exfiltrar por curl a traves del proxy SOCKS5. Sin uso corporativo legitimo.
logsource:
  category: process_creation
  product: windows
detection:
  seleccion_puertos:
    CommandLine|contains|all:
      - 'SocksPort'
      - 'ControlPort'
  seleccion_control:
    CommandLine|contains|all:
      - 'HashedControlPassword'
      - 'AvoidDiskWrites'
  condition: seleccion_puertos or seleccion_control
falsepositives:
  - Pruebas de seguridad autorizadas con registro previo en el gestor de cambios.
level: critical
```

## X-5. Mitigaciones de configuración con efecto directo

| Control | Corta |
|---|---|
| **WinRAR ≥ 7.13** en todo el parque, o retirada en favor del gestor de archivadores integrado | `CVE-2025-8088`: la persistencia silenciosa en la carpeta de Inicio. Es la única exposición directa del informe |
| **Bloqueo de ejecución de `mshta.exe`** por política de restricción de aplicaciones o WDAC | La etapa 01 completa, en su variante con y sin exploit. Corta más que cualquier detección |
| **Mostrar extensiones de fichero conocidas** por política de grupo | El engaño de doble extensión (`СБУ.doc.lnk`): el fichero deja de parecer un documento |
| **Bloqueo de ejecución desde medios extraíbles** (AppLocker/WDAC, o `NoAutorun` más denegación de ejecución por ruta) | Las dos herramientas de envenenamiento de USB. Sin ejecución desde el medio, el LNK no sirve |
| **Denegar permiso de escritura a usuarios ordinarios en la raíz de los recursos compartidos de red** | `PteroLNK` no puede copiarse ni crear LNK disfrazados de directorio. Es el control que corta el método más transferible |
| **Restringir la creación de tareas programadas** a cuentas administrativas, y auditar EID 4698 | Cuatro de los mecanismos de persistencia documentados |
| **Registro de bloque de script de PowerShell (EID 4104)** y modo de lenguaje restringido donde sea viable | Convierte de invisible en visible a un arsenal que es íntegramente script. Es la decisión `E-d` |
| **Lista de permitidos de servicios de nube, túnel y almacenamiento** en el proxy de egreso | Las capas 1, 2 y 4 de §O-3. Es la decisión `E-c` y sin ella `D-6` y `D-10` no son operables |
| **Bloqueo de `bitsadmin.exe` y restricción de trabajos BITS** a destinos autorizados | La descarga de Tor y el canal de transferencia de reserva |
| **Inspección de archivadores en la pasarela de correo**, con extracción recursiva y bloqueo de HTA en cualquier nivel de anidamiento, incluido bzip2 | La entrega de la etapa 01, antes de que llegue al escritorio |
| **Bloqueo de ficheros `.lnk` y `.hta` adjuntos** y en descarga web | Dos de los tres tipos de artefacto de entrega |
| **Denegar la instanciación del objeto COM `MSScriptControl.ScriptControl.1`** donde la aplicación propia no lo requiera | El puente de ejecución entre VBScript y PowerShell que usan varias herramientas |

---

## 14. Brechas de inteligencia y nuevos requisitos de colección

| # | Brecha | Impacto en el juicio | Requisito propuesto | Prioridad |
|---|---|---|---|---|
| G-1 | Sin telemetría propia ni inventario de software no gestionado | §O-4 sin evaluar; las decisiones `E-b` y `E-d` no se pueden dimensionar | Inventario de WinRAR por versión, y activación de EID 4104 y de línea de comandos en creación de procesos | **Crítica** |
| G-2 | **No se pudo leer la metodología del ranking de telemetría de Trellix** (HTTP 403) | **Es la brecha que define el informe.** El supuesto clave de §O-6 —que «actividad observada» significa detecciones y no intrusiones— no está verificado, y de él dependen `KJ-3` y `KJ-4` | Obtener el informe completo por vía comercial o institucional, o la definición del indicador. Una tarde de trabajo resolvería el punto más frágil del producto | **Crítica** |
| G-3 | Capacidad destructiva (*wiper*) afirmada en cobertura secundaria y ausente en la fuente de primera mano | §X-1 declara «no sostenida». Si se confirma, cambia la clase de amenaza del actor | Localizar el informe de primera mano del proveedor que atribuye `GamaWiper`, y verificar si el whitepaper de 2026 lo recoge | Alta |
| G-4 | Corroboración independiente de la exclusividad ucraniana de la victimología | `KJ-1` descansa en fuente única, y es precisamente el punto en disputa con `KJ-2` | Buscar informes de CERT-UA y de otros proveedores con telemetría en Europa del Este que se pronuncien sobre geografía | Alta |
| G-5 | Listas completas de infraestructura de C2, disponibles sólo en eventos MISP comerciales | El Anexo A.3 es un muestreo declarado por la fuente; cualquier retrohunt de red será parcial | Evaluar el coste de suscripción frente al valor, que para nosotros es bajo dado `KJ-1` | Baja |
| G-6 | Qué centro del FSB opera el grupo (16.º frente a 18.º) | Ninguno. No cambia ninguna decisión | Ninguno. Se consigna para cerrar la cuestión | Nula |
| G-7 | Valores numéricos de las figuras del whitepaper, que son imágenes | No se puede cuantificar la estacionalidad de las campañas ni compararla con años anteriores | Solicitar los datos subyacentes al proveedor, o estimarlos del gráfico si se requiere la serie | Baja |
| G-8 | **Ausencia de inteligencia regional sobre adopción del modelo de cinco capas** | `KJ-5` es una extrapolación nuestra. Es el juicio con mayor valor práctico y el peor sostenido | **Requisito de colección permanente**: vigilar informes sobre actores latinoamericanos en busca de túneles de terceros, *dead drops* en redes sociales y exfiltración a S3 comercial. Es el indicador `I-3` | **Crítica** |

---

# ANEXOS

## Anexo A — Indicadores de compromiso

> ⚠ **Leer antes de usar — y en este informe la advertencia es más fuerte que de
> costumbre.** Este Anexo A **nace caducado en su componente de red** y se
> entrega sabiéndolo (§3.5). De los 26 subdominios de túnel, la mayoría tiene
> fecha de primera observación en las últimas dos semanas de diciembre de 2025 y
> ya no existe. De los 189 dominios registrados por el actor en 2025, aquí hay
> seis: el 3 %. Y **catorce entradas de la sección A.4 son servicios legítimos
> de terceros que no deben bloquearse en ningún caso**: Telegra.ph, Teletype,
> Telegram, Rentry, Write.as, dev.to, Mastodon, GoFile, Dropbox, Wasabi, Tebi,
> Intercolo, Filemail y los resolvedores DNS web. Cargar este anexo en un
> bloqueo sin filtrar por la columna `Acción permitida` **provocará cortes de
> servicio propios con certeza**.
>
> **El valor real de este anexo está en la sección A.2**, los artefactos de
> host, que no caducan porque el actor no compila nada y lleva años reutilizando
> los mismos nombres de tarea, clave y mutex.

### A.1 — Hashes de herramientas (SHA-1, un ejemplo por herramienta o variante)

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| sha1 | `41BDC7545EE8A7E37714AE6C4F69F95C846FCB38` | PteroBox, variante que usa rclone. Detección `PowerShell/Pterodo.SV` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `76EC9B898E3FED239AF3895D9F3225EFB1273DCC` | PteroBox, variante que usa la API de Dropbox. Detección `PowerShell/Pterodo.WY` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `606C2692E409E40E6D563458FDF71FAA9EA22557` | PteroCache, descargador de cargas PowerShell. Detección `VBS/Pterodo.COC` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `569265C1BDE1D738963DD027BEB24AE0DC864F7F` | PteroDee, descargador. Detección `VBS/Pterodo.CAQ` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `584685A6AA84192302DF27C35E492B2846C06DD6` | PteroDum, descargador de cargas VBScript. Detección `PowerShell/Pterodo.VP` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `8CB65FE85C25CE521139990689AC989B44A0A230` | PteroEffigy, descargador que abusa de `api.gofile.io`. Detección `PowerShell/Pterodo.UE` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `256DE94FDBF675E3CCB1ADC42AB74771B5381B3F` | PteroGram, roba datos de Telegram Desktop. Detección `VBS/Pterodo.CEB` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `ED5BA0EF9E2413F1CD29464209F7B5E347810299` | PteroLNK, versión PowerShell, envenenador de USB. **Descontinuada en 2025.** Detección `PowerShell/Pterodo.PK` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `B13B5B1186B5AC0558E692E72990ECEB810BDA47` | PteroLNK, versión VBScript, envenenador de USB **y de unidades de red**. Detección `VBS/Pterodo.CLR` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `7EF497C6A2EF33558C1CAF41F6EC3614AF898C4C` | PteroLNK, versión VBScript, envenenador de USB. Detección `VBS/Pterodo.CMK` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `42DB9DE2017F66ED3AF88E7B1094891627B3C706` | PteroOdd, descarga cargas por la API de Telegra.ph. **Entregó cargas de Turla.** Detección `PowerShell/Pterodo.QB` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `F045E11EEA6AF11867380141C1E1888F433B5342` | PteroPSDoor versión 1000, ladrón de ficheros con exfiltración a nube. Detección `PowerShell/Pterodo.WO` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `F718F25DCCF68BD7CB28AA7CB526FFA54B0E51A8` | Descargador de PteroPSDoor. Detección `PowerShell/TrojanDownloader.Agent.LDD` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `09A22856890AB6AEF6311CA2BD27BE54E86DA75C` | PteroPSLoad, descargador. Detección `PowerShell/Pterodo.QD` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `0F952E6162BCC881F7F844F3E2C7CDA9A5C74D72` | PteroPSLoad, descargador, segunda variante. Detección `PowerShell/Pterodo.SU` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `61B03FF9D84EB653F9F66867DBF76DFB1E130E93` | PteroPaste, descargador y envenenador de USB. **Entregó cargas de Turla.** Detección `PowerShell/Pterodo.WY` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `45ECE835E5065775B7EFD1CCED99B6DD4FEC6A3B` | PteroScout, versión PowerShell: enumera procesos y software de seguridad. Detección `VBS/Pterodo.CEB` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `FA10D0469DBE45F2D359730135BDA39B5CCCC9BE` | PteroScout, versión VBScript (nueva en diciembre de 2025). Detección `VBS/Pterodo.CNQ` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `B66B2FB1A71A7E8CAF3B9A90DD84A2A3619F5CC5` | PteroSteal, versión PowerShell: credenciales de navegadores. Detección `PowerShell/Pterodo.WK` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `7947737949CC3D273DFE8DBD9F70701A25ED05B8` | PteroVDoor versión 2000, ladrón de ficheros. Detección `VBS/Pterodo.CME` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `7FED429FF76C75BBF57D75152160BEABF1EDD886` | Descargador dedicado de PteroVDoor, reactivado el 2025-09-18. Detección `VBS/Pterodo.CMX` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `7976F1E6B079008E56AE35F1AFC6336D12CBA8E1` | PteroX, descargador VBScript de propósito general. **Descontinuada en 2025.** Detección `VBS/Pterodo.BOU` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `27A9C300DA75FD2ABF5EE4DF483774FFE1BDCAD3` | PteroGraphin (campaña 2024): persistencia por complemento de Excel y entrega por Telegraph. **Es la herramienta que reinició Kazuar de Turla el 2025-02-27.** Detección `PowerShell/Pterodo.MD` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `CFAE5B81DD0D351555AFA3990B3A9E873494A616` | PteroStew (campaña 2024). Detección `VBS/Pterodo.BFC` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `1B05753A90FDE7EC9779730CD37DD2A0774B80F3` | PteroBox original (campaña 2024), exfiltración a Dropbox. Detección `PowerShell/Pterodo.NW` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `0DBE44BF9EC6A9D032897AF64C5C87A055FFA945` | PteroSig (campaña 2024), roba datos de Signal Desktop. Detección `PowerShell/Pterodo.MO` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `6C06D7F92F3F34C5D8A5E74B7DC04B8720749C39` | PteroTickle (campaña 2024), envenena scripts Tcl. Detección `VBS/Pterodo.SN` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `17871AA1EADBEBE852B4673E575538B76476F83A` | PteroDespair (campaña 2024). Detección `PowerShell/Agent.BID` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `61991A8B1D4B9FCC9B741CC7DB5836A00F239E17` | PteroScout (campaña 2024). Detección `PowerShell/Pterodo.KZ` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `DB05975A33F39915797F1BFD127FCA3E643C2841` | PteroVDoor versión 6005 (campaña 2024). Detección `VBS/Pterodo.ALU` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `617B8447848A10680F9E062BF4BB4BD96F159597` | PteroVDoor versión 6015 (campaña 2024). Detección `VBS/Pterodo.AQT` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `A7DED2EF728CD1DE31AD7F017F46A984B6309364` | PteroVDoor versión 6016 (campaña 2024). Detección `VBS/Pterodo.AQT` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `88233D3CB06DB2CAB05877D6804C6A3B77304491` | Fichero LNK de correo dirigido contra Ucrania (campaña 2024). Detección `PowerShell/Pterodo.LS` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `A474034BDC9EB6B97EB7616C2AC21DDAA0ECE153` | Descargador HTA de correo dirigido (campaña 2024). Detección `VBS/Pterodo.BEE` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| sha1 | `B38A26AEE38FF137E4B12363FB08A31A0FDD686C` | Descargador HTA de correo dirigido, segunda variante (campaña 2024). Detección `VBS/Pterodo.BEE` | Alta | Sin caducidad para retrohunt | Solo retrohunt |
| cve | `CVE-2025-8088` | Recorrido de ruta en WinRAR mediante flujos de datos alternativos NTFS. Explotado por el actor en todas las campañas desde el 2025-09-26. **Corregido en WinRAR 7.13 (julio de 2025)** | Alta | Sin caducidad: la decisión es de parcheo | Parchear — no es indicador de bloqueo |

### A.2 — Artefactos de host (el componente que no caduca)

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| artefacto | `Windows\DirectX\DXGIAdapterCache` · `Windows\DirectX\DirectXDatabaseUpdater` | Tareas programadas de PteroLNK v2 que imitan DirectX. **Contrastar la acción, no el nombre** | Alta | Sin caducidad | Caza (`D-9`, `H-4`) |
| artefacto | `MicrosoftEdgeUpdateTaskMachineUA` · `MicrosoftEdgeUpdateTaskMachineCore` · `MicrosoftUpdateTaskMachineUA` · `MicrosoftUpdateTaskMachineCore` | Tareas programadas de PteroLNK v3 que imitan la actualización de Edge. **Nombres que también existen legítimamente** | Alta | Sin caducidad | Caza con contraste de acción — no bloquear |
| artefacto | `Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticResolver` · `DiskDiagnostic\Microsoft\Windows\DiskDiagnosticDataCollector` · `CertificateServicesClient\SystemTask\SilentCleanup` · `InstallService\ScanForUpdatesServer\SmartRetry` · `Windows\InstallService\ScanForUpdatesAsUser` · `Windows\Software\Microsoft\TroubleshootingScanner\RecommendedTroubleshootingScanner` · `Windows\DeviceDirectoryClient\RegisterDeviceConnectedToNetwork` · `Windows\DeviceDirectoryClient\RegisterUserDevice` | Tareas programadas de PteroLNK v2 que imitan diagnóstico y mantenimiento | Alta | Sin caducidad | Caza con contraste de acción |
| clave | `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\DXGIAdapterCache` · `...\DirectXDatabaseUpdater` · `...\Microsoft-Windows-DiskDiagnosticResolver` · `...\RecommendedTroubleshootingScanner` · `...\ScanForUpdatesAsUser` · `HKCU\...\RunOnce\ExploitGuard` | Persistencia de PteroLNK v2 | Alta | Sin caducidad | Caza (`D-3`, `H-5`) |
| clave | `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\regName` · `...\Run\GooglePhone` | Persistencia de PteroPSDoor y PteroVDoor. **Literales, no variables** | Alta | Sin caducidad | Caza (`D-3`) |
| pattern | `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\%USERNAME%` · `...\%USERNAME%_%USERNAME%` · `...\%USERDOMAIN%` · `...\%COMPUTERNAME%` · `...\%COMPUTERNAME%2` | Persistencia de PteroPSDoor. **Variables resueltas en ejecución: comparar con el valor real de la máquina** | Alta | Sin caducidad | Caza (`D-3`, `H-5`) |
| path | `%USERPROFILE%\boot.ini` | Contenedor de los flujos de datos alternativos de PteroLNK v2. **`boot.ini` no se usa desde Windows XP: su presencia en un perfil es anómala por sí sola** | Alta | Sin caducidad | Caza (`D-4`, `H-6`) — indicador de mayor fidelidad del informe |
| artefacto | `%USERPROFILE%\boot.ini:SRV` · `:LNK` · `:GTR` · `:SERVER` · `:URLS` · `:IPS` · `:URL` · `:IP` · `:IpURL` · `:CloudURL` · `:URLTeletype` · `:WindowsDetect` · `:URLTelegra` · `:WindowsTelegra` | Flujos de datos alternativos de PteroLNK v2: descargador, dropper de LNK y resolución de C2 | Alta | Sin caducidad | Caza (`D-4`, `H-6`) |
| artefacto | `%PUBLIC%\ntuser.ini:SRV` · `%PUBLIC%\ntuser.ini:LNK` · `%USERPROFILE%:SERVER` · `%USERPROFILE%:LNK` · `%USERPROFILE%:GTR` · `%USERPROFILE%:URL` | Flujos de datos alternativos adicionales de PteroLNK v2, incluidos los adjuntos al propio directorio de perfil | Alta | Sin caducidad | Caza (`D-4`, `H-6`) |
| path | `%PUBLIC%\NTUSER.DAT.TMContainer00000000000000000001.regtrans-ms` · `%PUBLIC%\NTUSER.DAT.TMContainer00000000000000000002.regtrans-ms` · `%PUBLIC%\ntuser.dat.LOG1` · `%PUBLIC%\ntuser.dat.LOG2` · `%USERPROFILE%\NTUSER.DAT1.LOG` · `%USERPROFILE%\NTUSER.DAT2.LOG` · `%USERPROFILE%\NTUSER.DAT3.LOG` | Rutas de instalación de PteroLNK v2 que imitan ficheros de registro de Windows | Alta | Sin caducidad | Caza (`H-6`) |
| clave | `HKCU\Console\URL` · `HKCU\Console\IP` | Donde PteroLNK v2 guarda el C2 resuelto desde los *dead drops* | Alta | Sin caducidad | Caza |
| mutex | `Global\MutexGlobalNet` · `Global\MutexGlobalNetWind` · `Global\MutexGlobalNetWinds` · `Global\MutexGlobalNewStone` · `Global\MutexGlobalNewStoner` · `Global\MutexGlobalNewStoner1` · `Global\MutexGlobalNewStorm` · `Global\MutexGlobalUP` · `Global\MutexGlobalUPS` | Mutex de PteroPSDoor | Alta | Sin caducidad | Caza (`H-9`) |
| pattern | `Global\assembly0[01][0-9]` · `Global\assembly30[1-7]` | Mutex de PteroPSDoor expresados como patrón | Alta | Sin caducidad | Caza (`H-9`) |
| mutex | `Global\MutexLaos` · `Global\MutexLaos1` · `Global\MutexNosa` · `Global\MutexNosas` · `Global\MutexTa` · `Global\MutexTanos` · `Global\MutexTanoss` · `Global\MutexTest` | Mutex de PteroPSLoad | Alta | Sin caducidad | Caza (`H-9`) |
| pattern | `Local\[0-9]{4}(0[1-9]\|1[1-2])` | Mutex de PteroPaste, con forma de fecha año-mes | Alta | Sin caducidad | Caza (`H-9`) |
| clave | `HKCU\EUDC\first` · `HKCU\EUDC\knok` · `HKCU\EUDC\runner` · `HKCU\EUDC\usb` · `HKCU\EUDC\privateKeyXml` | Rutas de instalación y configuración de PteroPaste | Alta | Sin caducidad | Caza |
| filename | `volumeinfo.ps1` · `test.ps1` · `%PROCESSOR_REVISION%.ps1` | Ficheros de PteroPaste. El tercero es una variable resuelta en ejecución | Media | Sin caducidad | Caza |
| path | `%TEMP%\install.vbs` · `%TEMP%\config.txt` · `%TEMP%\7za.exe` · `%TEMP%\7za.dll` · `%TEMP%\7z.sfx` · `%TEMP%\archive.7z` · `%TEMP%\start.exe` · `%TEMP%\1.exe` | Ficheros temporales de PteroSetup, el envenenador de instaladores de software | Alta | Sin caducidad | Caza (`H-11`) |
| clave | `HKCU\Keyboard Layout\getListFile` · `\usb` · `\GetFileMD5` · `\sendFile` · `\listPrepare` · `\update` | Rutas de instalación de PteroBox dentro del registro (almacenamiento sin fichero) | Alta | Sin caducidad | Caza |
| path | `%LOCALAPPDATA%\info.vbs` · `%APPDATA%\rclone\rclone.exe` · `%APPDATA%\rclone\1.exe` · `%APPDATA%\rclone\rclone.conf` · `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\%COMPUTERNAME%.lnk` | Artefactos de PteroBox. `rclone` es una utilidad legítima: lo anómalo es la ubicación en perfil junto a persistencia | Alta | Sin caducidad | Caza (`D-7`, `H-7`) |
| artefacto | `dropbox` · `%COMPUTERNAME%` · `%COMPUTERNAME%_1` | Nombres de tarea programada de PteroBox | Alta | Sin caducidad | Caza |
| path | `%USERPROFILE%\%PROCESSOR_LEVEL%_%PROCESSOR_REVISION%\data\geoip` · `...\data\geoip6` · `...\tor\tor.exe` | Montaje de Tor de PteroPSDoor para exfiltración de reserva, descargado con BITS desde Filemail | Alta | Sin caducidad | Caza (`D-8`, `H-8`) |
| pattern | `SocksPort 9050` + `ControlPort 9051` · `HashedControlPassword` + `AvoidDiskWrites 1` | Línea de comandos del montaje de Tor. **Sin uso corporativo legítimo** | Alta | Sin caducidad | Bloqueo por detección (`D-8`) |
| pattern | `HKCU\Software\[a-zA-Z0-9]{19,25}` · `HKCU\Abstractions\[a-zA-Z0-9]{19,25}` · `HKCU\AppEvents\[a-zA-Z0-9]{19,25}` · `HKCU\Printers\[a-zA-Z0-9]{19,25}` · `HKCU\Cursors\[a-zA-Z0-9]{19,25}` · `HKCU\EUDC\[a-zA-Z0-9]{19,25}` | Rutas de almacenamiento sin fichero de PteroPSDoor y PteroPSLoad. La ruta cambió cuatro veces en 2025: `Software` → `Abstractions` → `AppEvents` → `Printers` | Alta | Sin caducidad | Caza |
| pattern | `%APPDATA%\{WindowsPowerShell\|Windows\|VirtualStore\|MSBuild\|cache\|Microsoft\|Internet\|Microsoft.NET\|Defender\|CrashDumps}\desktop[s]?.{ini\|dat\|vbs\|sys\|con\|in\|co\|ko}` | Rutas de instalación de PteroLNK v3, que imitan nombres de carpeta legítimos de perfil | Alta | Sin caducidad | Caza |
| artefacto | `MSScriptControl.ScriptControl.1` | Objeto COM que varias herramientas usan para ejecutar cargas VBScript. Apenas tiene uso legítimo en software moderno | Alta | Sin caducidad | Caza (`D-11`) |
| pattern | `*.doc.lnk` · `*.docx.lnk` · `*.jpeg.lnk` · `*.jpg.lnk` · `*.pdf.lnk` | Patrón de doble extensión de los LNK de PteroLNK. **Patrón, no indicador de actor: cualquiera puede copiarlo** | Alta | Sin caducidad | Caza (`D-12`, `H-10`) |
| filename | `для службового користування.lnk` · `Прибуття.lnk` · `Вибуття.lnk` · `ФОТО.lnk` · `Акти.lnk` · `ЖБД.lnk` · `Доповіді 2025.lnk` · `БпЛА.lnk` · `СЗЧ.lnk` · `таємно.lnk` · `Нова папка.lnk` · `Нова папка (2).lnk` | Nombres de LNK señuelo en ucraniano de PteroLNK v3. **Su aparición en un parque hispanohablante sería concluyente y extraordinaria** | Alta | Sin caducidad | Bloqueo por detección |
| artefacto | `install` · `setup` · `cronos` | Subcadenas que PteroSetup busca en nombres de ejecutable para sustituirlos por archivadores autoextraíbles envenenados | Alta | Sin caducidad | Caza (`H-11`) |
| pattern | `bypass-tunnel-reminder` · `vreferer` · `ssid` · `guid` | Cabeceras HTTP en las que PteroDee exfiltra el nombre del equipo y el número de serie del volumen. Las dos últimas son las variantes recientes | Media | Sin caducidad | Caza |

### A.3 — Infraestructura de red del actor

> ⚠ Muestreo declarado por la fuente, no lista exhaustiva. **Las entradas de
> túnel son efímeras**: las fechas de primera observación están concentradas en
> diciembre de 2025 y la mayoría de esos nombres ya no resuelve.

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| domain | `litanq[.]ru` | Dominio registrado por el actor, C2 de reserva. Primera observación 2025-03-13; también activo en 2024 | Alta | 2026-12-31 | Bloqueo |
| domain | `estaca[.]ru` | Dominio registrado por el actor, C2. Primera observación 2026-01-01 | Alta | 2026-12-31 | Bloqueo |
| domain | `earlysilence[.]ru` | Dominio registrado por el actor, C2. Primera observación 2026-01-01 | Alta | 2026-12-31 | Bloqueo |
| domain | `veryinappropriate[.]ru` | Dominio registrado por el actor, C2. Primera observación 2026-01-01 | Alta | 2026-12-31 | Bloqueo |
| domain | `holdmyspice[.]ru` | Dominio registrado por el actor, C2. Primera observación 2025-03-23 | Alta | 2026-12-31 | Bloqueo |
| domain | `maybefallout[.]ru` | Dominio registrado por el actor, C2. Primera observación 2025-12-30 | Alta | 2026-12-31 | Bloqueo |
| domain | `maybefallout[.]online` | Variante `.online` del anterior. **Único TLD no `.ru` del muestreo** | Alta | 2026-12-31 | Bloqueo |
| domain | `lettinggo[.]ru` | Dominio registrado por el actor, C2. Primera observación 2025-12-30 | Alta | 2026-12-31 | Bloqueo |
| domain | `dushun[.]ru` | Dominio registrado por el actor, C2. Primera observación 2025-03-03 | Alta | 2026-12-31 | Bloqueo |
| domain | `zalupka[.]net` | Dominio registrado por el actor, C2. Primera observación 2025-12-29 | Alta | 2026-12-31 | Bloqueo |
| ipv4 | `69.67.173[.]214` | Dirección de C2 alojada en BL Networks. Primera observación 2026-01-01 | Media | 2026-12-31 | Bloqueo con verificación previa de reasignación |
| ipv4 | `167.88.164[.]202` | Dirección de C2 alojada en RouterHosting LLC. Primera observación 2025-03-03 | Media | 2026-12-31 | Bloqueo con verificación previa de reasignación |
| ipv4 | `172.235.166[.]243` | Dirección de C2 alojada en Linode. **Proveedor de nube: dirección reasignable** | Baja | 2026-06-30 | Solo retrohunt |
| ipv4 | `91.231.182[.]187` | Servidor desde el que PteroPaste descargó el instalador de Kazuar v2 de Turla, junio de 2025 | Media | 2026-12-31 | Bloqueo con verificación previa |
| domain | `eset[.]ydns[.]eu` | **Dominio de DNS dinámico que suplanta el nombre de un proveedor de seguridad.** Usado por PteroOdd para subir información de la víctima a `/post.php`. Atribuido a Turla con confianza media por la fuente | Media | 2026-12-31 | Bloqueo |
| domain | `ekrn[.]ydns[.]eu` | Segundo dominio de DNS dinámico que suplanta el nombre de un ejecutable del mismo proveedor de seguridad | Media | 2026-12-31 | Bloqueo |
| fqdn | `wwpeeya.ignores.workers[.]dev` | C2 sobre Cloudflare Workers. Primera observación 2025-11-20 | Alta | **Ya caducado** | Solo retrohunt |
| fqdn | `szrtrboyre.fewwef.workers[.]dev` | C2 sobre Cloudflare Workers. Primera observación 2025-12-29 | Alta | **Ya caducado** | Solo retrohunt |
| fqdn | `srkwk.3742eddi.workers[.]dev` | C2 sobre Cloudflare Workers. Primera observación 2025-08-11 | Alta | **Ya caducado** | Solo retrohunt |
| fqdn | `jvyuwatt.ssuworker.workers[.]dev` | C2 sobre Cloudflare Workers. **El subdominio imita las siglas del servicio de seguridad ucraniano (SSU)** | Alta | **Ya caducado** | Solo retrohunt |
| fqdn | `stake.ytmrj83283.workers[.]dev` | C2 sobre Cloudflare Workers. Primera observación 2026-01-01 | Alta | **Ya caducado** | Solo retrohunt |
| fqdn | `wage.zpwyi71185.workers[.]dev` | C2 sobre Cloudflare Workers. Primera observación 2025-12-30 | Alta | **Ya caducado** | Solo retrohunt |
| fqdn | `d16ss6sn-80.euw.devtunnels[.]ms` | C2 sobre túnel de desarrollo de Microsoft. Primera observación 2025-08-11 | Alta | **Ya caducado** | Solo retrohunt |
| fqdn | `ch47f6gl-80.euw.devtunnels[.]ms` | C2 sobre túnel de desarrollo de Microsoft | Alta | **Ya caducado** | Solo retrohunt |
| fqdn | `7tnzsgp4-80.use.devtunnels[.]ms` | C2 sobre túnel de desarrollo de Microsoft | Alta | **Ya caducado** | Solo retrohunt |
| fqdn | `x3f2q1cd-80.asse.devtunnels[.]ms` | C2 sobre túnel de desarrollo de Microsoft | Alta | **Ya caducado** | Solo retrohunt |
| fqdn | `x8b9b7q2-80.euw.devtunnels[.]ms` | C2 sobre túnel de desarrollo de Microsoft | Alta | **Ya caducado** | Solo retrohunt |
| fqdn | `4273twd6-80.euw.devtunnels[.]ms` | C2 sobre túnel de desarrollo de Microsoft | Alta | **Ya caducado** | Solo retrohunt |
| fqdn | `ser-uk-defines-involved.trycloudflare[.]com` | C2 sobre túnel de Cloudflare. Primera observación 2025-08-11 | Alta | **Ya caducado** | Solo retrohunt |
| fqdn | `cheese-metals-gourmet-interviews.trycloudflare[.]com` | C2 sobre túnel de Cloudflare | Alta | **Ya caducado** | Solo retrohunt |
| fqdn | `parameter-iron-turns-combinations.trycloudflare[.]com` | C2 sobre túnel de Cloudflare | Alta | **Ya caducado** | Solo retrohunt |
| fqdn | `alfred-assumptions-asin-winston.trycloudflare[.]com` | C2 sobre túnel de Cloudflare. Primera observación 2025-02-18 | Alta | **Ya caducado** | Solo retrohunt |
| fqdn | `your-combination-percent-gibson.trycloudflare[.]com` | C2 sobre túnel de Cloudflare | Alta | **Ya caducado** | Solo retrohunt |
| fqdn | `innocent-fares-supposed-loved.trycloudflare[.]com` | C2 sobre túnel de Cloudflare | Alta | **Ya caducado** | Solo retrohunt |
| fqdn | `graph-proved-physicians-ward.trycloudflare[.]com` | C2 sobre túnel de Cloudflare | Alta | **Ya caducado** | Solo retrohunt |
| fqdn | `finally-election-audience-dont.trycloudflare[.]com` | C2 sobre túnel de Cloudflare | Alta | **Ya caducado** | Solo retrohunt |
| fqdn | `8b82933574e0112129f7062a41689f7a.loophole[.]site` | C2 sobre túnel de Loophole. Primera observación 2025-08-11 | Alta | **Ya caducado** | Solo retrohunt |
| fqdn | `99a23d4d4f0c9ca8e8bac7d30a02442d.loophole[.]site` | C2 sobre túnel de Loophole. Primera observación 2025-12-23 | Alta | **Ya caducado** | Solo retrohunt |
| fqdn | `lucky-king-96d6.mopig92456.workers[.]dev` | *Worker* de Cloudflare al que PteroOdd subía el nombre del equipo y el número de serie del volumen | Alta | **Ya caducado** | Solo retrohunt |

### A.4 — Servicios legítimos abusados · **NO BLOQUEAR**

> ⬛ **Esta sección entera lleva acción prohibida de bloqueo.** Son servicios de
> terceros con uso legítimo generalizado. Su valor es de **caza por contexto de
> proceso** (`D-5`, `D-6`, `D-10`), nunca de lista negra. Bloquear
> `devtunnels.ms` rompe Visual Studio; bloquear `dev.to` o `mastodon.social`
> bloquea sitios web ordinarios; bloquear `wasabisys.com` puede romper el
> respaldo de alguien.

> **Por qué estas filas llevan el tipo `servicio` y no `domain`.** El tipo
> determina en qué agregado plano entra el indicador. Un dominio apex legítimo
> como `t.me`, `dev.to` o `devtunnels.ms` en `ioc_url.txt` —una lista sin
> contexto, pensada para ingesta automática— es un corte de servicio esperando
> a ocurrir. Estas filas se marcan con un tipo que **no alimenta ninguna lista
> plana** y sólo aparece en `ioc_index.csv` con su contexto y su acción
> permitida intactos. Es la misma disciplina que aplicó `CTI-2026-020`, que
> publicó rutas completas de `raw.githubusercontent.com` y de `bitbucket.org`
> pero nunca el dominio desnudo.

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| servicio | `trycloudflare[.]com` | Servicio de túnel de Cloudflare. Estándar de C2 del actor desde finales de 2024 | Alta | Sin caducidad | **No bloquear — servicio legítimo.** Caza por proceso (`D-6`) |
| servicio | `workers[.]dev` | Cloudflare Workers. Adoptado en mayo de 2025; a diferencia del túnel, **ejecuta código** | Alta | Sin caducidad | **No bloquear — servicio legítimo.** Caza por proceso (`D-6`) |
| servicio | `devtunnels[.]ms` | Túneles de desarrollo de Microsoft. Adoptados en junio de 2025. **Bloquearlo rompe Visual Studio** | Alta | Sin caducidad | **No bloquear — servicio legítimo.** Caza por proceso (`D-6`) |
| servicio | `loophole[.]site` | Servicio de túnel Loophole. Adoptado en junio de 2025 | Alta | Sin caducidad | **No bloquear sin evaluar uso propio.** Caza por proceso (`D-6`) |
| servicio | `loca[.]lt` | Servicio de túnel. **En pruebas**: hallado en pocas muestras, no adoptado como estándar | Media | Sin caducidad | **No bloquear.** Caza por proceso |
| servicio | `bore[.]pub` | Servicio de túnel. **En pruebas**, como el anterior | Media | Sin caducidad | **No bloquear.** Caza por proceso |
| servicio | `telegra[.]ph` | *Dead drop resolver* principal. La API `api.telegra.ph/getPage/` entrega la dirección de C2 | Alta | Sin caducidad | **No bloquear — servicio legítimo.** Caza por proceso (`D-5`) |
| servicio | `teletype[.]in` | *Dead drop resolver* | Alta | Sin caducidad | **No bloquear.** Caza por proceso (`D-5`) |
| servicio | `t[.]me` | Acortador oficial de Telegram, usado para resolver C2 desde canales | Alta | Sin caducidad | **No bloquear.** Caza por proceso (`D-5`) |
| servicio | `rentry[.]co` | *Dead drop resolver* **nuevo en 2025** | Alta | Sin caducidad | **No bloquear.** Caza por proceso (`D-5`) |
| servicio | `write[.]as` | *Dead drop resolver* nuevo en 2025. PteroPSDoor **crea sus propias publicaciones** por API REST y cifra los tokens de edición con RSA | Alta | Sin caducidad | **No bloquear.** Caza por proceso (`D-5`) |
| servicio | `dev[.]to` | Red social de desarrolladores usada como *dead drop* para configuración S3, octubre de 2025 | Alta | Sin caducidad | **No bloquear — sitio web ordinario.** Caza por proceso (`D-5`) |
| servicio | `mastodon[.]social` | Red social usada como *dead drop* para configuración S3, octubre de 2025 | Alta | Sin caducidad | **No bloquear — sitio web ordinario.** Caza por proceso (`D-5`) |
| servicio | `gofile[.]io` | Almacenamiento usado como *dead drop* por PteroEffigy (`api.gofile.io`) | Alta | Sin caducidad | **No bloquear.** Caza por proceso (`D-5`) |
| servicio | `lesma[.]eu` | Servicio de pegado usado para **distribución de carga útil** cifrada de PteroPSDoor | Alta | Sin caducidad | **No bloquear.** Caza por proceso (`D-5`) |
| servicio | `nopaste[.]net` | Servicio de pegado usado para distribución de carga útil | Alta | Sin caducidad | **No bloquear.** Caza por proceso (`D-5`) |
| servicio | `pastee[.]dev` | Servicio Paste.ee, usado para distribución de carga útil | Alta | Sin caducidad | **No bloquear.** Caza por proceso (`D-5`) |
| servicio | `wasabisys[.]com` | Almacenamiento S3 de Wasabi. Destino de exfiltración desde abril-mayo de 2025 | Alta | Sin caducidad | **No bloquear sin evaluar uso propio.** Caza por volumen y proceso (`D-10`) |
| servicio | `tebi[.]io` | Almacenamiento S3 de Tebi. Destino de exfiltración desde agosto-septiembre de 2025 | Alta | Sin caducidad | **No bloquear sin evaluar uso propio.** Caza (`D-10`) |
| domain | `de-fra[.]i3storage[.]com` | Extremo S3 de Intercolo. **Destino primario de exfiltración desde el 2025-12-05 en ambos ladrones de ficheros, simultáneamente** | Alta | Sin caducidad | Bloqueo tras verificar que no hay uso propio — es el más específico de los tres |
| servicio | `check-host[.]net` | Resolvedor DNS web usado para obtener la IP del C2 | Alta | Sin caducidad | **No bloquear.** Caza por proceso |
| servicio | `whatsmydns[.]net` | Resolvedor DNS web, **probablemente nuevo en 2025** | Alta | Sin caducidad | **No bloquear.** Caza por proceso |
| servicio | `cloudflare-dns[.]com` | DoH de Cloudflare, usado para resolver C2 fuera del DNS corporativo | Alta | Sin caducidad | **No bloquear — control correcto: forzar el DNS propio y bloquear DoH de terceros** |
| servicio | `1.1.1.1` | DoH de Cloudflare por dirección. Mismo caso que el anterior | Alta | Sin caducidad | **No bloquear la dirección — restringir DoH por política** |
| servicio | `filemail[.]com` | Servicio de transferencia de ficheros desde el que PteroPSDoor descarga Tor con BITS | Alta | Sin caducidad | **No bloquear sin evaluar.** Caza (`D-5`, `H-8`) |
| servicio | `cleverapps[.]io` | PaaS de Clever Cloud, abusado para alojar campañas de correo de corta vida | Alta | Sin caducidad | **No bloquear.** Caza |
| servicio | `supabase[.]co` | PaaS de Supabase, abusado para el mismo fin | Alta | Sin caducidad | **No bloquear.** Caza |
| artefacto | `hopto.org` · `ddns.net` · `gotdns.ch` · `myddns.me` · `freedynamicdns.org` · `freedynamicdns.net` · `redirectme.net` · `ddnsking.com` · `servehttp.com` · `servebeer.com` · `serveirc.com` · `serveftp.com` · `sytes.net` · `webhop.me` · `zapto.org` · `3utilities.com` | **Los dieciséis dominios de DNS dinámico de No-IP** que el actor recuperó en 2025 tras cuatro años sin usarlos, con mayor incidencia en los descargadores HTA de las campañas de correo | Alta | Sin caducidad | **No bloquear el dominio padre.** Decisión de política: valorar el bloqueo de DNS dinámico como clase, que es un control legítimo en entorno corporativo |
| herramienta | `rclone` · `tor.exe` · `curl.exe` · `7za.exe` · `mshta.exe` · `rundll32.exe` · `bitsadmin.exe` · `wscript.exe` · `cscript.exe` | Binarios y utilidades legítimas abusadas. **Detectar por contexto de invocación, nunca por presencia** | Alta | Sin caducidad | **No bloquear por presencia.** `mshta.exe` sí admite bloqueo por política (§X-5) |

## Anexo B — Fuentes y valoración

> Valoración doble tipo Admiralty/OTAN: **fiabilidad de la fuente (A–F)** ×
> **credibilidad de la información (1–6)**, valoradas por separado.

| Fuente | Disciplina | Fiabilidad | Credibilidad | Notas de sesgo |
|---|---|---|---|---|
| ESET, «Gamaredon in 2025: Leveraging tunnels, workers, dead drops, and new alliances», whitepaper de 47 páginas, 25 de junio de 2026, autor Zoltán Rusnák | OSINT comercial de primera mano | **B** | **2** | **Fuente principal del informe: el 80 % del contenido técnico sale de aquí.** Leída íntegra. Declara su metodología de atribución, sus ventanas y sus limitaciones, y marca sus indicadores de red como muestreo. Sesgo: interés comercial en demostrar profundidad de telemetría; su afirmación de exclusividad geográfica es la que está en disputa en `KJ-2` y procede de un único proveedor |
| ESET, repositorio público de indicadores (`eset/malware-ioc`, directorio `gamaredon`) | OSINT de repositorio | **B** | **2** | Base del Anexo A.1 y de parte del A.3. Fechas de primera observación hasta 2026-01-01. **No publica artefactos de host**, que se tomaron de los apéndices del whitepaper. Publica SHA-1 y no SHA-256, y un ejemplo por herramienta |
| ESET, «ESET APT Activity Report Q2 2026–Q3 2026», 28 de octubre de 2026 | OSINT comercial de primera mano | **B** | **2** | Fuente de la ventana 2026 y del descenso de actividad. Leída íntegra en su versión de artículo; **no se leyó el PDF completo** ni los valores de sus dos figuras |
| ESET, «Gamaredon X Turla collab», 19 de septiembre de 2025, autores Matthieu Faou y Zoltán Rusnák | OSINT comercial de primera mano | **B** | **2** | Base de `KJ-8` y de la cronología de la colaboración. Declara que su producto se instaló después del compromiso en todos los casos y que no observó la descarga inicial. Enumera y descarta sus propias hipótesis alternativas, lo que eleva su credibilidad |
| Trellix, «The CyberThreat Report: November 2026», publicado el 4 de noviembre de 2026, cubre abril–septiembre de 2026 | OSINT comercial de telemetría agregada | **B** | **3** | **Origen de la contradicción que estructura el informe.** La página responde HTTP 403 a lectura automatizada: las cifras se tomaron de la página indexada y de la cobertura de *Infosecurity Magazine*, que coinciden. **No se leyó la metodología**, de donde la brecha `G-2` y la fragilidad del supuesto clave de §O-6. Credibilidad rebajada a 3 no por desconfianza en el dato sino por no haber podido verificar qué mide |
| *Infosecurity Magazine*, «Chinese Nation-State Threat Activity Falls Sharply in Q2 and Q3 2026» | Prensa especializada | **C** | **2** | Reproduce las cifras de Trellix de forma coincidente con la página indexada, lo que las corrobora cruzadamente. Aporta la fecha de publicación y la atribución de APT36 a Pakistán |
| Servicio de Seguridad de Ucrania (SSU), atribución pública al 18.º Centro del FSB e identificación de cinco miembros | HUMINT / atribución estatal, **por vía secundaria** | **C** | **3** | No se leyó la declaración original. Fiabilidad rebajada por ser parte en el conflicto y por mediación periodística. **Las fuentes secundarias divergen sobre qué centro del FSB** (16.º frente a 18.º), discrepancia consignada en §O-2 y en `G-6` |
| MITRE ATT&CK, ficha de grupo `G0047` | OSINT de marco | **B** | **2** | Base de la tabla de alias. Las versiones indexadas eran antiguas y los identificadores de subtécnica han cambiado; **los IDs del §T-2 se tomaron del whitepaper, que declara v19**, no de las páginas de ficha |
| HarfangLab, análisis de PteroLNK y de sus *dead drop resolvers* | OSINT comercial de primera mano | **B** | **2** | Fuente secundaria para este informe, consultada sólo por referencia cruzada. Señala que la atribución del grupo es «ampliamente aceptada» más que cierta, matiz honesto que se recoge |
| Cobertura secundaria sobre el uso de *wiper* y `GamaWiper` (TechTimes, junio de 2026; atribución a ClearSky de noviembre de 2025) | Prensa general y prensa especializada | **D** | **4** | **No se sostiene en este informe.** Contradice en parte al whitepaper, que trata `CVE-2025-8088` sólo como vector de acceso inicial. Consignado como brecha `G-3` y declarado como no sostenido en `KJ-6` y §X-1 |

**Escalas**
- **A** completamente fiable · **B** normalmente fiable · **C** bastante fiable · **D** normalmente no fiable · **E** no fiable · **F** no evaluable.
- **1** confirmada por otras fuentes · **2** probablemente cierta · **3** posiblemente cierta · **4** dudosa · **5** improbable · **6** no evaluable.

> **Nota sobre la concentración de fuentes.** Nueve de las once entradas de este
> anexo son del mismo proveedor o derivan de él. Es una debilidad estructural
> del producto y está declarada como brecha `G-4`. El motivo es que **sólo un
> proveedor publica análisis anual sostenido sobre este actor**, lo cual es a su
> vez un dato: un actor que encabeza el ranking de prevalencia global tiene un
> único analista público dedicado.

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

## Anexo D — Cómo leer un ranking de prevalencia de proveedor

Este anexo es el entregable transversal del informe y se escribe para que sobreviva a él. Son las cinco preguntas que deben hacerse a cualquier lista de «actores más activos» antes de que entre en un proceso de priorización.

| # | Pregunta | Por qué | Qué hacer si no hay respuesta |
|---|---|---|---|
| D-1 | **¿La unidad de conteo es la intrusión o la detección?** | Es la pregunta que decide todo. Un actor ruidoso con pocas víctimas y un actor sigiloso con muchas aparecen invertidos | Tratar la lista como medida de ruido, no de amenaza. Es lo que hace este informe |
| D-2 | **¿Dónde está desplegada la telemetría que lo mide?** | El denominador del porcentaje es la base instalada del proveedor, no el mundo. Un 19,88 % «en EE. UU.» puede ser un artefacto de concentración de sensores | Buscar la distribución geográfica de la base instalada. Si no se publica, descartar las cifras por país |
| D-3 | **¿Cruza con victimología documentada de la región propia?** | Un actor sin víctimas documentadas en el hemisferio no sube de prioridad por aparecer primero en una lista global | Hacer el cruce manualmente contra los perfiles de actor propios. Es la decisión `E-a` |
| D-4 | **¿Qué ventana cubre, y coincide con la de las otras fuentes que se van a comparar?** | En este expediente, la discrepancia entre un whitepaper sobre 2025 y un ranking sobre abril–septiembre de 2026 es parte del problema | No comparar porcentajes de ventanas distintas. Anotar la ventana junto a cada cifra, siempre |
| D-5 | **¿Hay una fuente de primera mano que contradiga la lista?** | Si existe y no se consultó, la lista se está usando como si fuera la única fuente | Buscarla antes de priorizar. En este caso existía y decía lo contrario |

## Anexo E — Marcos de referencia empleados

`MITRE ATT&CK v19` (versión declarada por la fuente principal y conservada en §T-2) · `Modelo del Diamante` · `Cyber Kill Chain` · `Pirámide del Dolor` · `F3EAD` · `ICD 203` · `Análisis de Hipótesis Competidoras (ACH)` · `Comprobación de Supuestos Clave (KAC)` · `pre-mortem` · `TLP 2.0` · `PAP` · `Admiralty Code` · `Sigma` · `KQL`

## Anexo F — Paquete legible por máquina

- Índice con contexto: [`ioc_index.csv`](ioc_index.csv) — **es el fichero que debe ingerir una plataforma de inteligencia**, porque conserva la columna `accion_permitida` sin la cual el Anexo A.4 es peligroso
- Listas planas: [`ioc_hash.txt`](ioc_hash.txt), [`ioc_url.txt`](ioc_url.txt), [`ioc_ipv4.txt`](ioc_ipv4.txt) — **no cargar en bloqueo sin filtrar previamente por acción permitida**
- Reglas Sigma: cuatro reglas en §X-4, sin repositorio externo
- Bundle STIX 2.1: no generado para este informe
- Evento MISP: no generado. Las listas completas de infraestructura del actor están en eventos MISP del proveedor, de acceso comercial (brecha `G-5`)

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-11-17 | Emisión inicial. Perfil construido sobre el whitepaper de 2025 del proveedor principal, con la contradicción frente al ranking de telemetría de noviembre de 2026 como eje analítico | Célula CTI |

## Anexo H — Realimentación del consumidor

| Pregunta | Respuesta |
|---|---|
| ¿Respondió a su requisito? | |
| ¿Cambió este informe el orden de prioridad de algún actor en su proceso? (decisión `E-a`) | |
| ¿Cuántas instalaciones de WinRAR por debajo de 7.13 había en el parque? (decisión `E-b`) | |
| ¿Qué detecciones del §X-3 se desplegaron, y cuántas alertas produjeron en los primeros 30 días? | |
| ¿Qué faltó? | |
| ¿Llegó a tiempo? | |

> Sin este anexo devuelto, el ciclo de inteligencia queda abierto y el próximo
> producto no mejora. En este informe interesa especialmente la segunda
> pregunta: si la respuesta es «no», el producto falló en su objetivo principal
> aunque todo lo demás sea correcto.
