---
tlp: "TLP:CLEAR"
pap: "PAP:AMBER"
id: "CTI-2026-023"
version: "1.0"
tipo: "Perfil de actor"
foco_regional: "Venezuela · Ecuador · Colombia · Perú · Nicaragua"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "Machete · El Machete · APT-C-43 · G0095"
fecha: "2026-11-16"
caduca: "2027-05-16"
autor: "Célula CTI"
distribucion: "Elaborado íntegramente con fuentes abiertas TLP:CLEAR. Difusión libre, conservando la atribución de las fuentes y las salvedades metodológicas de §3. El informe de un proveedor citado por MITRE ya no es accesible en su dirección original (véase §3.3 y brecha G-2)."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-023

## El único actor de esta cartera que roba documentos y no dinero

### Lleva seis años sin que nadie publique nada de primera mano

> **Regla de oro del producto:** todo párrafo debe responder a un requisito de
> inteligencia (PIR) y habilitar una decisión. Si un párrafo no cambia lo que
> alguien va a hacer, va al anexo o se borra.

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-023` |
| Versión / fecha | `1.0` — 2026-11-16 |
| Tipo de producto | Perfil de actor de espionaje más **evaluación de vigencia**. Una parte sustancial de este producto consiste en declarar qué no sabemos y qué haría falta para saberlo: es, deliberadamente, tanto un perfil como un requisito de colección |
| Niveles cubiertos | Estratégico · Operacional · Táctico · Técnico |
| Foco regional | **Victimología documentada: Venezuela, Ecuador, Colombia, Perú, Nicaragua, Cuba, España, Rusia (embajadas).** Chile aparece como **ausencia documentada**, lo que es un hallazgo y no una omisión |
| Marcado de difusión | `TLP:CLEAR` · `PAP:AMBER` |
| Clasificación interna | Público — apto para difusión abierta |
| Requisitos atendidos | `PIR-01` (actores de espionaje con interés en la región y en nuestros clientes institucionales), `PIR-04` (amenazas con foco regional hispanohablante), `PIR-05` (robo de propiedad intelectual y de información técnica), `PIR-10` (vigencia y caducidad de la inteligencia de la que dependemos) |
| Solicitante / consumidor primario | CISO · Jefatura de SOC · Riesgo · Dirección de Contratos Públicos · Ingeniería de Detección |
| Ventana de observación | 2010 (inicio estimado de la campaña) → 2026-11-16. **Último informe público de primera mano: septiembre de 2020.** Últimos indicadores publicados: julio de 2019 |
| Base de colección | 6 fuentes. **Proveedor de primera mano:** Kaspersky GReAT (20-ago-2014), ESET (5-ago-2019, más su repositorio de indicadores), 360 Baize Lab (25-sep-2020). **Académica de primera mano:** Civilsphere Project / Virus Bulletin 2019 (Valeros, Rigaki, Garcia, Babayeva), con 105 muestras analizadas. **Marco:** MITRE ATT&CK `G0095`. **Citada por referencia, no accesible:** Cylance (22-mar-2017) — el artículo ya no se sirve en su dirección original. **Sin telemetría propia incorporada** |
| Autor (analista) | Célula CTI |
| Revisión por pares | Pendiente |
| Aprobación | Pendiente |
| Caducidad / revisión | 2027-05-16 —**plazo deliberadamente más largo que el de los demás productos de esta serie**, porque la amenaza no está en movimiento— o antes si aparece un informe de primera mano sobre actividad posterior a 2020, si se documenta una víctima chilena, o si se publica una familia nueva atribuida a este actor |
| Productos relacionados | `CTI-2026-017` (FamousSparrow — comparte la categoría de espionaje y el problema de la permanencia larga), `CTI-2026-020` (Blind Eagle) y `CTI-2026-022` (Red Akodon — **comparten región, idioma y el señuelo de la citación judicial**; los tres describen actores hispanohablantes contra instituciones del vecindario), `CTI-2026-024` (Rhysida — **el caso del Ejército de Chile demuestra que el conjunto de objetivos que este actor persigue es alcanzable en Chile**, aunque por otra vía y con otro fin) |
| Paquete legible por máquina | Pendiente de generar (véase §14) |

<!-- cti:note type="warn" -->

> ⚠ **Limitación estructural de este producto, y es la más severa de la serie.** Las dos
> habituales siguen: **no hay telemetría propia** (§O-4 vacía) y **no hay víctima chilena
> documentada**. Pero hay una tercera que define el producto entero: **la inteligencia
> sobre este actor está congelada en 2020**. El último análisis de primera mano se publicó
> el 25 de septiembre de 2020; los últimos indicadores, en julio de 2019. Todo lo técnico
> que aquí se describe puede haber cambiado por completo y no tendríamos forma de saberlo.
> **Este informe no dice qué está haciendo Machete hoy. Dice qué hizo, qué se le puede
> buscar hacia atrás, y qué haría falta para responder la pregunta de hoy.**

<!-- cti:note type="good" -->

> ✅ **Lo que sí tiene valor inmediato, y es más de lo que parece.** Primero, un
> **retrohunt barato y acotado**: los indicadores del Anexo A son de 2014 a 2020 y buscarlos
> hacia atrás en el SIEM cuesta una tarde. Segundo, **una detección que no caduca**: este
> actor exfiltra por **FTP en claro**, y una estación de trabajo hablando FTP contra
> Internet es una anomalía detectable con lo que ya tenemos (regla `D-1`). Tercero, **una
> lista de objetivos**: §E-2 y el Anexo D identifican quién en Chile encaja en el perfil de
> víctima, y eso es materia de decisión comercial y de riesgo, no de SOC.

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** Machete es espionaje de documentos, no fraude, y eso lo saca de la lógica de todos los demás informes de esta cartera. No cifra, no extorsiona, no sustituye direcciones de monedero ni suplanta portales de banca. Lo que hace es buscar en el disco ficheros de ofimática, bases de datos, respaldos, claves criptográficas PGP y —de forma característica— **ficheros de sistemas de información geográfica: mapas topográficos y rutas de navegación con cuadrícula militar**, cifrarlos con AES y subirlos por FTP. ESET midió gigabytes exfiltrados por semana. Valoramos **casi con certeza** *(95–99 %)*. **Confianza: alta.** *Base:* ESET (2019) y el estudio del Civilsphere Project (2019), análisis de primera mano e independientes entre sí.

**KJ-2.** La victimología es el vecindario, y está estable desde 2014: fuerzas armadas, policía, cancillerías e inteligencia de los países andinos y de Venezuela. Kaspersky situó a las víctimas en Venezuela, Ecuador, Colombia, Perú, Rusia —ahí, embajadas de esos países—, Cuba y España. ESET midió en 2019 **más de cincuenta equipos** comunicándose con el mando y control en tres meses, **más del 75 % de ellos en organismos del Estado venezolano**: fuerzas militares, educación, policía y asuntos exteriores. 360 documentó en 2020 una campaña específica contra instituciones militares venezolanas. Valoramos **casi con certeza** *(95–99 %)*. **Confianza: alta.** *Base:* tres proveedores y un estudio académico, en tres momentos distintos, con victimología consistente.

**KJ-3.** Chile no aparece en ninguna de las cuatro fuentes de primera mano, y la ausencia es demasiado consistente para ser casualidad. Kaspersky enumera siete países y Chile no está. Cylance, en 2017, enumera dieciocho países —incluidos Corea, Alemania, Ucrania y Guatemala— y Chile no está. ESET mide cuatro países y Chile no está. El estudio académico analiza 105 muestras y 63 señuelos sin que Chile aparezca. **Doce años de informes, cuatro fuentes independientes, ninguna mención.** Valoramos **probable** *(55–80 %)* que la ausencia refleje una decisión real del actor sobre su conjunto de objetivos, y no un hueco de observación. **Confianza: moderada.** *Base:* convergencia de cuatro fuentes en la negativa; el razonamiento sobre su significado es nuestro.

**KJ-4.** La inteligencia pública sobre este actor está congelada desde 2020, y esa es la conclusión más importante del informe. El último análisis de primera mano es del 25 de septiembre de 2020. Los últimos indicadores publicados son de julio de 2019. MITRE actualizó la ficha del grupo en julio de 2026, pero fue un cambio de mapeo del marco, no actividad nueva. Hay dos lecturas: que el actor cesó o se transformó, o que **nadie con telemetría regional está publicando sobre él**. Valoramos **posibilidad real** *(45–55 %)* de que siga operando sin informes públicos, y **posibilidad real** *(45–55 %)* de que haya cesado o se haya reorganizado bajo otro nombre. **Confianza: baja.** *Base:* es una inferencia sobre un silencio; por definición no hay evidencia a favor de ninguna de las dos lecturas.

**KJ-5.** La atribución apunta a un operador hispanohablante con presencia física en la región, y el indicio más concreto es administrativo, no técnico. El estudio del Civilsphere Project encontró que **las rutas del servidor FTP de exfiltración están nombradas con ciudades y regiones colombianas** —«Buenaventura», «Guajira», «Huila»— y sugiere que «podrían indicar dónde están estacionados los operadores del ataque». A eso se suma que 360 observó que la mayoría de los activos de red del atacante estaban desplegados en Colombia, que el código del lado del servidor está escrito en español —`reportes`, `ingresar`, `peso`— y que una de las capacidades del implante es **copiar los ficheros a un dispositivo USB concreto cuando se inserta**, lo que ESET interpreta como posible presencia física en uno de los países objetivo. Valoramos **probable** *(55–80 %)* el nexo con la región andina; **no valoramos** el país concreto. **Confianza: moderada.** *Base:* convergencia de tres fuentes con indicios distintos; ninguna llega a afirmarlo.

**KJ-6.** El estudio académico plantea patrocinio estatal como posibilidad, y ninguna fuente comercial lo hace. Valeros y colegas concluyen que Machete «probablemente lo opera un único grupo cuyas actividades podrían estar patrocinadas por un Estado», apoyándose en que **tres claves AES aparecen compartidas entre las 105 muestras analizadas** y en el solapamiento de infraestructura. Kaspersky, ESET y 360 se quedan en «grupo hispanohablante» y en motivación de espionaje, sin nexo estatal. Valoramos **posibilidad real** *(45–55 %)* del nexo estatal. **Confianza: baja.** *Base:* fuente única para la afirmación, con razonamiento publicado pero sin evidencia de mando; las demás fuentes no la contradicen, simplemente no entran.

**KJ-7.** Nuestra exposición no es ser el objetivo: es ser el proveedor del objetivo. Una empresa chilena no encaja en el perfil de víctima de este actor —no somos un ministerio de defensa andino—, pero sí encajan **quienes nos contratan y a quienes contratamos** si trabajan con fuerzas armadas, cancillería, policía, cartografía, catastro, puertos, concesiones de infraestructura o contratación pública de defensa. El actor roba ficheros GIS con rutas de navegación y cuadrícula militar: quien produce esos ficheros para un cliente estatal es parte de la cadena. Valoramos **posibilidad real** *(45–55 %)* de que exista exposición indirecta material en nuestra cartera de contratos. **Confianza: baja.** *Base:* inferencia nuestra a partir del tipo de fichero que el actor busca; no hay caso documentado de compromiso de proveedor en ninguna fuente.

**Qué cambiaría estos juicios:** un informe de primera mano sobre actividad de Machete posterior a 2020. Eso convertiría `KJ-4` de inferencia en hecho y obligaría a reescribir todo el nivel técnico, porque el arsenal que aquí se describe tendría seis años. Es el indicador `I-1` de §O-7 y es el único que justificaría una revisión anticipada.

---

## 2. Resumen ejecutivo

Machete es el actor más viejo de esta cartera y el único que no quiere nuestro dinero. Lleva desde 2010 robando documentos a fuerzas armadas, policías, cancillerías y servicios de inteligencia de Venezuela, Ecuador, Colombia, Perú y Nicaragua. No cifra nada, no pide rescate, no suplanta portales bancarios. Entra por un correo dirigido con un documento señuelo que suele ser **un documento real robado antes a otra víctima** —ESET documentó un caso con un documento oficial clasificado fechado el mismo día en que se envió el correo— y deja un implante escrito en Python que busca en el disco, cifra lo que encuentra y lo sube por FTP.

Lo que busca merece atención porque define a quién le importa esto. Además de ofimática, correo y contraseñas, el implante va expresamente a por **respaldos, bases de datos, claves PGP y ficheros de sistemas de información geográfica**: mapas topográficos y rutas de navegación con cuadrícula militar. Es un actor que roba cartografía operacional.

Y luego está el hecho que estructura este informe: **lleva seis años sin que nadie publique nada de primera mano sobre él.** El último análisis técnico es de septiembre de 2020. Los últimos indicadores, de julio de 2019. Hay dos explicaciones. Una es que cesó, o se reorganizó bajo otro nombre, o lo desmantelaron sin que trascendiera. La otra es que sigue operando y nadie con telemetría en la región está publicando. No podemos distinguirlas, y **la segunda es la que debería incomodarnos**, porque es la que describe un punto ciego y no una amenaza extinta.

Para Chile hay un dato limpio y poco habitual en esta serie: **Chile no aparece.** Ni en las siete víctimas país de Kaspersky en 2014, ni en los dieciocho países de Cylance en 2017 —que incluían Corea, Alemania y Ucrania—, ni en los cuatro de ESET en 2019, ni en los 105 ficheros del estudio académico. Doce años, cuatro fuentes, ninguna mención. Eso es informativo: sugiere que el conjunto de objetivos de este actor es una vecindad concreta y que Chile queda fuera de ella.

Pero hay un matiz que conviene no perder, y es la razón por la que este informe se escribe. El conjunto de objetivos que Machete persigue —fuerzas armadas, cancillería, policía, cartografía— **existe en Chile y es alcanzable**: el informe hermano de este lote, `CTI-2026-024`, documenta cómo un grupo de extorsión publicó 360 000 documentos del Ejército de Chile en 2023. Lo que cambia entre los dos casos no es la accesibilidad del objetivo: es el fin del atacante. Y nuestra exposición, si existe, no es como objetivo sino **como proveedor del objetivo**.

Lo que pedimos a Dirección es modesto y barato: un retrohunt acotado con los indicadores históricos, una regla de detección de FTP en claro que no caduca, y una revisión de cartera de contratos para saber si estamos en la cadena de suministro de alguien que sí encaja en el perfil.

<!-- cti:cards -->

| Rasgo | Qué significa | Etiqueta |
|---|---|---|
| Roba documentos, no dinero | No cifra, no extorsiona, no hay pérdida visible. Si entra y sale bien, nadie se enteraría | `01 · espionaje` |
| Va a por cartografía y GIS | Mapas topográficos y rutas con cuadrícula militar. Define quién es objetivo y quién es proveedor de objetivo | `02 · botín` |
| El señuelo es un documento robado real | Documentación oficial auténtica, a veces del mismo día. No hay error gramatical que delate | `03 · señuelo` |
| Exfiltra por FTP en claro | Es el eslabón débil del actor y nuestra mejor detección: no caduca y no necesita indicador | `04 · canal` |
| Lleva seis años en silencio público | No sabemos si cesó o si nadie mira. El silencio es el hallazgo | `05 · vigencia` |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `16` | Años entre el inicio estimado de la campaña (2010) y el cierre de este informe | La muestra más antigua analizada académicamente es de 2011 |
| `6` | Años desde el último informe público de primera mano (sep-2020) | Los últimos indicadores publicados son de julio de 2019 |
| `0` | Víctimas chilenas documentadas en cuatro fuentes independientes | Kaspersky, Cylance, ESET y el estudio del Civilsphere Project |
| `75` | Porcentaje de los equipos comprometidos que ESET situó en organismos del Estado venezolano, mar–may 2019 | Sobre más de cincuenta equipos activos contra el C2 |
| `100` | Gigabytes que Cylance cifró como robados en un solo mes de 2017, sobre unas 300 víctimas | *Cifra de segunda mano: el artículo original ya no es accesible* |
| `105` | Muestras de segunda etapa analizadas por el estudio académico, de 2011 a principios de 2019 | Más 63 documentos señuelo |
| `3` | Claves AES compartidas entre **todas** las muestras analizadas | Es el principal argumento del estudio a favor de un único grupo operador |
| `14` | Dominios de servidor FTP de exfiltración identificados, con 13 direcciones únicas | Las rutas del servidor llevan nombres de ciudades colombianas |
| `1` | Fuentes primarias de las que depende MITRE y que ya no son accesibles en su dirección original | El informe de Cylance de 2017. Véase §E-3 y brecha `G-2` |

<!-- cti:note type="good" -->

> ✅ **Decisiones que se solicitan a Dirección.** (a) Autorizar un **retrohunt acotado** con los indicadores del Anexo A sobre los datos históricos que conservemos, con el resultado por escrito aunque sea negativo — 30 días, coste una tarde de analista. (b) Desplegar la regla `D-1`, **detección de FTP en claro desde estaciones de trabajo y servidores de usuario**, que no depende de ningún indicador y por tanto no caduca — 30 días. (c) Encargar a Dirección de Contratos y a Riesgo una **revisión de cartera**: qué contratos nuestros, propios o de subcontratistas, tocan fuerzas armadas, cancillería, policía, cartografía, catastro, puertos o concesiones de infraestructura — 60 días. Es la decisión que determina si este informe nos aplica. (d) Incorporar al plan de colección permanente la **vigilancia del indicador `I-1`**, aparición de un informe de primera mano posterior a 2020 — 15 días. (e) Aceptar una **política de archivo local de los informes de proveedor** de los que dependen nuestros productos: el artículo de Cylance que MITRE todavía cita dejó de servirse tras una adquisición empresarial, y con él se fue la única fuente de la cifra de 100 GB — 45 días.

---

## 3. Alcance, requisitos y limitaciones

**3.1 Requisitos de inteligencia atendidos**

| Req. | Enunciado | ¿Respondido? | Dónde |
|---|---|---|---|
| PIR-01 | ¿Qué actores de espionaje tienen interés documentado en la región y en nuestros clientes institucionales? | Sí, con la salvedad de la antigüedad | §E-1, §E-2, §O-2 |
| PIR-04 | ¿Qué amenazas operan contra la región hispanohablante y con qué método? | Sí | §E-2, §T-1 |
| PIR-05 | ¿Qué amenazas buscan información técnica y cartográfica, no credenciales? | Sí — es el rasgo distintivo del actor | §O-3, §X-1 |
| PIR-10 | ¿Está vigente la inteligencia de la que dependemos sobre este actor? | **Sí, y la respuesta es que no lo está** | §E-3, `KJ-4`, §14 |
| — | ¿Está Machete activo hoy? | **No se puede responder con fuentes abiertas** | `KJ-4`, §14 (`G-1`) |
| — | ¿Hay víctimas chilenas? | **No documentadas** — y la ausencia es consistente en cuatro fuentes | `KJ-3`, §E-2 |
| — | ¿Estamos ya comprometidos? | **No** — requiere el retrohunt de la decisión (a) | §O-4, §14 |

**3.2 Fuera de alcance.** No se evalúa: la actividad de Machete contra objetivos fuera de Iberoamérica, que las fuentes mencionan sin desarrollar; el componente para Android que Kaspersky describe en 2014 y que ninguna fuente posterior retoma; la relación con el actor `Packrat`, que el estudio académico declara expresamente no sostenida por evidencia; la atribución a un Estado concreto, que ninguna fuente intenta y este informe tampoco; y la respuesta a un compromiso consumado de espionaje, que exige procedimiento de contrainteligencia y no de respuesta a incidentes ordinaria.

**3.3 Limitaciones de la colección.** (i) **La inteligencia está congelada en 2020**, con los últimos indicadores en julio de 2019. Es la limitación que define el producto y está declarada en `KJ-4`, en §E-3 y en la brecha `G-1`. **Todo el nivel técnico de este informe debe leerse como histórico.** (ii) **Sin telemetría propia**: §O-4 sin rellenar. (iii) **El informe de Cylance de 2017 no pudo leerse.** Su dirección original —`threatvector.cylance.com`— responde con una redirección permanente al índice del blog de otra empresa, consecuencia de la adquisición corporativa del proveedor. Las cifras de ~300 víctimas y >100 GB, y la lista de dieciocho países, provienen de **coberturas de prensa especializada que citaron el artículo cuando era accesible**, no del artículo. Están marcadas así cada vez que aparecen. (iv) **El informe técnico de ESET de 2019 tampoco pudo leerse en su versión completa**: el PDF del documento técnico no se sirve en la dirección que su propio artículo enlaza. Se leyeron el artículo de blog y el **repositorio público de indicadores del proveedor**, que sí está completo y es la base del Anexo A; el desglose por país del 75 % / 16 % / 7 % / 2 % proviene de la nota de prensa y de la versión en español del blog del mismo proveedor, y no del documento técnico. (v) **La cifra de 778 víctimas** que circula atribuida a Kaspersky proviene de notas de prensa y coberturas de 2014, no del artículo técnico, que no da cifra total. Se consigna con esa salvedad y no se usa en ningún juicio. (vi) **El estudio académico declara explícitamente que no pudo reproducir las conclusiones de los informes anteriores** sobre número de víctimas y países, lo que significa que las cifras de victimología de distintas fuentes **no son comparables entre sí**. (vii) **Los gráficos de victimología por país del estudio académico y del artículo de ESET son imágenes** y sus valores no se pudieron leer; el desglose que se usa aquí es el textual. (viii) **El evento MISP del repositorio de ESET está marcado como no publicado**, de modo que una parte de sus atributos pudo no haberse revisado nunca para difusión pública; los indicadores que se recogen aquí proceden de los ficheros de hashes y del documento de texto del repositorio, que sí son material publicado.

**3.4 Metodología.** Disciplinas: OSINT comercial de proveedor (tres informes de primera mano en tres momentos distintos), OSINT académico (un estudio con 105 muestras y metodología declarada), OSINT de marco (MITRE ATT&CK), y **análisis de ausencia** —el razonamiento de `KJ-3` sobre qué significa que Chile no aparezca— que es una técnica con riesgo propio y se declara como tal. Técnicas analíticas estructuradas: análisis de hipótesis competidoras sobre la vigencia y sobre la atribución (§O-6), comprobación de supuestos clave, pre-mortem. Marcos: MITRE ATT&CK v18, Pirámide del Dolor, Cadena de Intrusión, ICD 203, código Admiralty.

---

# NIVEL ESTRATÉGICO
### Para: Consejo · CISO · Riesgo · Dirección de Contratos Públicos · Horizonte: 12–36 meses

## E-1. Qué representa este actor en el panorama

Todos los demás informes de esta cartera describen amenazas que se notan. El ransomware cifra y para la operación. El troyano bancario roba y aparece un cargo. El actor de extorsión publica y hay crisis de comunicación. Machete no: **si entra bien y sale bien, nadie se enteraría nunca.** No hay fichero cifrado, no hay nota, no hay transferencia, no hay pantalla de rescate. Hay un proceso de Python que, cada diez minutos, sube unos ficheros a un servidor FTP.

Eso cambia dos cosas de fondo. La primera es que **el coste no aparece en el balance**: aparece en una negociación perdida, en una licitación que el competidor ganó con un precio sospechosamente ajustado, o en una posición que la otra parte conocía antes de sentarse. La segunda es que **la métrica habitual de nuestro SOC no sirve**: contar incidentes contenidos no mide nada si la amenaza relevante es la que no genera incidente.

El segundo rasgo estructural es qué roba. El implante no se limita a ofimática y contraseñas: busca expresamente respaldos, bases de datos, claves criptográficas PGP, documentos de OpenOffice, imágenes vectoriales y **ficheros de sistemas de información geográfica**. ESET es explícito al respecto: los operadores recogen ficheros que «describen rutas de navegación y posicionamiento usando cuadrículas militares». Es un actor que roba cartografía operacional, y eso delimita con precisión inusual quién le interesa: quien tiene mapas, catastro, rutas, posiciones, concesiones, infraestructura. En un país como Chile, ese conjunto incluye instituciones del Estado y también **a sus proveedores privados**.

El tercero es la calidad del señuelo, que es alta por una razón incómoda: **es material auténtico**. ESET documenta un caso en el que el documento señuelo era un documento oficial clasificado fechado el 21 de mayo de 2019, el mismo día en que se envió por primera vez el archivo comprimido que lo contenía, y señala que ha visto más casos del mismo patrón. Es decir: el actor usa lo que robó a la víctima anterior para abrir la puerta de la siguiente. No hay error de traducción que delate el correo, porque no hay traducción. El estudio académico añade un detalle que conecta este informe con los dos anteriores de la serie: entre los temas de los señuelos hay, además de asuntos militares y políticos, **cobros de deuda y citaciones judiciales** — exactamente el mismo pretexto administrativo que `CTI-2026-022` describe en Colombia y `CTI-2026-021` en Chile.

Y el cuarto rasgo es el que explica por qué este informe existe aunque la amenaza esté en silencio: **la sofisticación es baja y la permanencia es larga**. El estudio académico lo dice sin rodeos: Machete «carece de sofisticación» comparado con otros actores de su categoría, en lenguaje, en vulnerabilidades explotadas y en antianálisis; pero es sofisticado «para su región». No usa días cero. Usa correo dirigido, Python, FTP en claro y una tarea programada. Y así lleva más de una década dentro de ministerios de defensa.

<!-- cti:cards -->

| Cambio estructural | Por qué nos afecta | Etiqueta |
|---|---|---|
| La amenaza que no produce incidente | No hay cifrado ni rescate ni cargo. Nuestra métrica de incidentes contenidos no la mide, y la pérdida aparece en otra parte | `01 · invisible` |
| El botín es cartografía y documentación técnica | Define quién es objetivo. En Chile, el conjunto incluye proveedores privados de instituciones del Estado | `02 · botín` |
| El señuelo es material robado auténtico | No hay error gramatical, ni plantilla, ni remitente raro. La formación del usuario rinde mucho menos de lo habitual | `03 · señuelo` |
| Baja sofisticación, permanencia de años | No hace falta capacidad avanzada para quedarse dentro de un ministerio una década. Hace falta que nadie mire el FTP saliente | `04 · asimetría` |
| La inteligencia pública caduca y desaparece | Seis años sin informe nuevo, y una de las fuentes primarias ya no se sirve. La cadena de suministro de nuestra inteligencia es frágil | `05 · fuentes` |

## E-2. Victimología y distribución

<!-- cti:bars title="Distribución de víctimas de Machete según ESET, marzo–mayo de 2019 (más de 50 equipos)" color="#c0392b,#e0a33e,#5a7ebe,#4db99c" -->

| País | Porcentaje |
|---|---|
| Venezuela | 75 |
| Ecuador | 16 |
| Colombia | 7 |
| Nicaragua | 2 |

<!-- cti:note type="warn" -->

> ⚠ **Procedencia exacta de estas cuatro cifras, porque se citan mucho y mal.** El
> artículo de blog de ESET que sí pudimos leer afirma únicamente que «más del 75 %» de los
> equipos comprometidos pertenecían a organismos del Estado venezolano y que el ejército
> ecuatoriano estaba «muy atacado». **El desglose completo 75 / 16 / 7 / 2 proviene de la
> nota de prensa del mismo proveedor y de la versión en español de su blog**, no del
> documento técnico, que no pudo leerse (§3.3). Las cuatro cifras son del mismo
> proveedor y del mismo trabajo, de modo que son utilizables; pero quien las cite debe
> saber que no están en el artículo técnico y que corresponden a **una ventana de tres
> meses de 2019**, no a la historia del actor.

**La geografía, fuente por fuente y sin mezclarlas.** Es importante no promediar, porque el estudio académico advierte expresamente que no pudo reproducir las conclusiones de los informes anteriores sobre número de víctimas y países.

| Fuente | Año | Qué midió | Países nombrados |
|---|---|---|---|
| Kaspersky GReAT | 2014 | Víctimas de la campaña, sin cifra total en el artículo técnico | Venezuela, Ecuador, Colombia, Perú, **Rusia** (embajadas de los países de la lista), Cuba, España, «entre otros» |
| Cylance *(no leída; cifras de prensa especializada)* | 2017 | ~300 víctimas únicas en un mes, >100 GB | Mayoría en Ecuador, Venezuela, Perú, Argentina y Colombia; además Corea, EE. UU., República Dominicana, Cuba, Bolivia, Guatemala, Nicaragua, México, Inglaterra, Canadá, Alemania, Rusia y Ucrania |
| ESET | 2019 | >50 equipos activos contra el C2 en tres meses | Venezuela (>75 %), Ecuador, Colombia, Nicaragua |
| Civilsphere Project (académica) | 2019 | 105 muestras y 63 señuelos, de 2011 a 2019 | «Principalmente Latinoamérica»; el único país nombrado en el texto es Venezuela. **Declara no poder reproducir las cifras anteriores** |

**Los sectores, en cambio, sí son consistentes en las cuatro fuentes:** servicios de inteligencia, fuerzas militares, embajadas y cancillerías, policía, instituciones de gobierno y, en la medición de ESET, también educación. El estudio académico resume el contenido de los señuelos como «mayoritariamente de naturaleza militar y política»: movimientos de tropas, reasignaciones de personal, asuntos políticos nacionales. Los nombres de los ficheros señuelo que publica el repositorio de indicadores de ESET lo confirman sin ambigüedad: `Radiograma 004026_pdf.scr`, `REPORTE OPERACIONAL 10JUN19 pdf.scr`, `FORMATO UNICO DE RENDIMIENTO OPERATIVO GNB 11JUNIO2019 CZGNB-13 xlsx.scr`, `INSTRUCCIONES DEL JSO 08JUN19 docx.scr`, `Mapa_monitoreo_WRF_ind02052018.scr`, `CALENDARIO_ACTIVIDADES_COLCO_EC.scr`.

<!-- cti:note type="warn" -->

> ⚠ **Lectura regional — y por una vez el hallazgo es una ausencia.** En los informes
> anteriores de esta serie la sección regional terminaba diciendo que Chile aparecía
> listado y no documentado. **Aquí Chile no aparece siquiera listado.** No está en los siete
> países de Kaspersky, no está en los dieciocho de Cylance —que llegan a incluir Corea del
> Sur, Alemania y Ucrania—, no está en los cuatro de ESET y no está en el estudio
> académico. Cuatro fuentes independientes, doce años, ninguna mención. Eso es un dato,
> no un hueco: **sugiere que el conjunto de objetivos de este actor es una vecindad
> concreta —Venezuela y los países andinos— y que Chile queda fuera de ella.** Y conviene
> decir con la misma claridad lo que no sugiere: no sugiere que las fuerzas armadas o la
> cancillería chilenas sean inalcanzables. `CTI-2026-024`, el informe hermano de este
> lote, documenta cómo un grupo de extorsión publicó 360 000 documentos del Ejército de
> Chile en 2023. Lo que separa los dos casos no es la defensa del objetivo: es el interés
> del atacante.

## E-3. Tendencia, vigencia y pronóstico

<!-- cti:chart title="Informes públicos de primera mano sobre este actor, por año" cap="Mide publicación de proveedor y de academia, no actividad del actor. El cero sostenido de 2021 a 2026 es el hallazgo central de este informe (KJ-4) y admite dos lecturas incompatibles entre sí." -->

| Periodo | Informes de primera mano |
|---|---|
| 2014 | 1 |
| 2017 | 1 |
| 2019 | 2 |
| 2020 | 1 |
| 2021 | 0 |
| 2022 | 0 |
| 2023 | 0 |
| 2024 | 0 |
| 2025 | 0 |
| 2026 | 0 |

La trayectoria técnica documentada, de 2014 a 2020, tiene tres movimientos claros y luego se interrumpe.

El primero es **la ofuscación del implante**. De Python empaquetado en ejecutables de Windows con instalador Nullsoft en 2014, a `py2exe` con `pyobfuscate` y, desde agosto de 2018, una capa adicional de `pyminifier` con compresión `zlib` y codificación base64. En la última versión que ESET describe, los componentes **ya no son `py2exe`**: los scripts de Python, un intérprete original de Python 2.7 y todas las bibliotecas se empaquetan en un autoextraíble. Es evolución de evasión, no de capacidad.

El segundo es **el alojamiento de la carga**. De servidor propio a **Dropbox y Google Docs** como origen de descarga, un movimiento que `CTI-2026-022` describe seis años después y con otros servicios: abusar de lo que nadie puede bloquear es la constante regional, no la novedad de ningún actor.

El tercero es **el empaquetado del instalador**. 360 documenta en 2020 un `MSI` de 8,10 MB construido con MSI Wrapper, con los metadatos falsificados para parecer un instalador de Adobe Acrobat Reader, que lleva dentro un entorno de Python completo. Es el único salto de ingeniería visible en toda la serie temporal, y es de presentación.

Y aquí se corta. **De septiembre de 2020 a noviembre de 2026 no hay un solo informe de primera mano.** MITRE actualizó la ficha `G0095` el 31 de julio de 2026, pero la versión 2.0 corresponde a una revisión del mapeo de técnicas, no a actividad nueva; sus cuatro referencias siguen siendo las de 2014, 2017, 2019 y 2020. Y una de esas cuatro, la de Cylance, **ya no se puede leer**: el dominio del proveedor redirige al blog de la empresa que lo adquirió, sin el artículo. Es decir que el marco de referencia que toda la industria usa para este actor apunta, hoy, a una fuente que no existe.

<!-- cti:note type="warn" -->

> ⚠ **Esto último no es anécdota, es un riesgo de nuestra propia cadena de suministro.**
> Nuestros productos se apoyan en informes de proveedor que viven en blogs corporativos.
> Los blogs corporativos sobreviven a las adquisiciones mal. La cifra de «más de 100 GB
> robados en un mes» que este informe cita en §2 y en §E-2 **ya no tiene fuente
> verificable**: existe en coberturas de prensa que citaron el original cuando estaba. Esa
> es la decisión `E-e`: archivar localmente los informes de los que dependemos, con fecha
> de captura, para que nuestros propios productos no acaben citando huecos. Es barato y
> hoy no lo hacemos.

<!-- cti:cards -->

| Escenario | Desarrollo | Etiqueta |
|---|---|---|
| Sigue operando sin informes públicos | La actividad continúa contra el mismo conjunto de objetivos y ningún proveedor con telemetría regional publica. Explica el silencio sin exigir el cese, y es compatible con que la región esté poco cubierta comercialmente | `Posibilidad real · 45–55 %` |
| Cesó, se reorganizó o fue desarticulado sin que trascendiera | El grupo dejó de operar, cambió de herramientas hasta ser irreconocible, o una acción policial o política lo detuvo sin comunicado | `Posibilidad real · 45–55 %` |
| Reaparece con herramientas nuevas y atribución difícil | Vuelve a publicarse actividad del mismo conjunto de objetivos pero con un arsenal que no se parece al descrito aquí, y la atribución queda en disputa como en `CTI-2026-022` | `Poco probable · 20–45 %` |
| Amplía su conjunto de objetivos hacia el Cono Sur, Chile incluido | Requiere un cambio de interés político que ninguna fuente insinúa. Es el escenario que más nos afectaría y el menos apoyado por la evidencia | `Muy poco probable · 5–20 %` |

## E-4. Decisiones que este informe pide al nivel estratégico

<!-- cti:table highlight="Chile|chilen|FTP|retrohunt|cartograf|contrato" -->

| # | Decisión | Fundamento | Plazo |
|---|---|---|---|
| E-a | Autorizar un **retrohunt acotado** con los indicadores históricos del Anexo A sobre los datos que conservemos, y registrar el resultado por escrito **aunque sea negativo** | Los indicadores son de 2014 a 2020: no sirven para prevenir y sí para descartar. Un negativo documentado es un activo; un «nunca lo miramos» no lo es | 30 días |
| E-b | Desplegar la detección de **FTP en claro desde estaciones de trabajo y servidores de usuario** hacia Internet (`D-1`) | KJ-1: el canal de exfiltración principal de este actor es FTP sin cifrar. **Esta regla no depende de ningún indicador y por tanto no caduca**, y vale contra cualquier exfiltración por ese canal, de este actor o de otro | 30 días |
| E-c | Encargar a Dirección de Contratos y a Riesgo una **revisión de cartera**: qué contratos propios o de subcontratistas tocan fuerzas armadas, cancillería, policía, cartografía, catastro, puertos, concesiones de infraestructura o contratación pública de defensa | KJ-7: nuestra exposición, si existe, es como proveedor del objetivo y no como objetivo. **Esta es la decisión que determina si el informe nos aplica**, y no la puede tomar seguridad informática | 60 días |
| E-d | Incorporar al plan de colección permanente el **indicador `I-1`**: aparición de un informe de primera mano sobre actividad posterior a 2020 | KJ-4: es el único hecho que reescribiría este producto. Vigilarlo cuesta una alerta; no vigilarlo cuesta quedarse con un informe de 2020 creyendo que es el estado del arte | 15 días |
| E-e | Aprobar una **política de archivo local de las fuentes** de las que dependen nuestros productos, con fecha de captura y comprobación periódica de enlaces | §E-3: una de las cuatro fuentes que MITRE cita para este actor ya no se sirve, y con ella desapareció la única procedencia verificable de una cifra que usamos. Es barato y estructural | 45 días |
| E-f | Fijar una **política de ficheros GIS y cartográficos**: inventario de dónde están, quién los produce, con quién se comparten y cifrado en reposo | KJ-1: el actor va expresamente a por mapas topográficos y rutas con cuadrícula militar. Si tenemos de eso, es nuestro activo más atractivo para esta clase de amenaza y probablemente el peor inventariado | 90 días |
| E-g | Decidir si contratamos **cobertura de inteligencia específicamente regional**, o aceptamos explícitamente el punto ciego | KJ-4 y `G-1`: el silencio de seis años puede ser ausencia de amenaza o ausencia de observador. **No se puede resolver con fuentes abiertas gratuitas**, y conviene que la decisión sea consciente y no por omisión | 90 días |
| E-h | Revisar el **procedimiento de respuesta ante sospecha de espionaje**, distinto del de respuesta a incidentes: preservación silenciosa, no notificación inmediata al usuario, cadena de custodia | KJ-1: aislar el equipo y avisar al usuario es correcto ante ransomware y contraproducente ante espionaje. Hoy tenemos un solo procedimiento y sirve para una de las dos cosas | 90 días |

---

# NIVEL OPERACIONAL
### Para: Jefatura de SOC · Respuesta a Incidentes · Threat Hunting · Horizonte: semanas–meses

## O-1. Identificación: un actor, cuatro nombres y una confusión que evitar

| Nombre | Quién lo usa | Qué delimita |
|---|---|---|
| `Machete` | Kaspersky (2014), ESET (2019), MITRE (`G0095`) | La campaña completa desde 2010, y también el nombre de la familia de malware (`S0409` en MITRE) |
| `El Machete` | Kaspersky, Cylance | El mismo conjunto. Alias reconocido por MITRE |
| `APT-C-43` | 360 (2020) | El mismo actor en la nomenclatura propia del proveedor. 360 vincula su campaña `HpReact` con Machete |
| `Pyark` | 360 (2020) | **El implante, no el actor.** Es el nombre que 360 da a la puerta trasera en Python que encuentra en junio de 2020 |
| `HpReact` | 360 (2020) | **La campaña, no el actor.** Nombre que 360 da a la operación contra instituciones militares venezolanas |
| `Python/Machete.A` a `.G` | ESET | **Nombres de detección de producto**, uno por componente. No son variantes del actor |

<!-- cti:note type="warn" -->

> ⚠ **Nota de tradecraft — cuatro errores concretos que evitar.** El primero: **`Machete`
> nombra a la vez al actor y al malware**, de modo que «se detectó Machete» puede
> significar dos cosas muy distintas; al leer un informe hay que comprobar cuál. El
> segundo: **`Pyark` y `HpReact` no son actores.** Citarlos como grupos distintos
> multiplica la amenaza en el inventario. El tercero: **no confundir Machete con
> `Packrat`**, otro actor hispanohablante de la región; el estudio académico dice
> expresamente que «no hay evidencia» de que sean el mismo. Y el cuarto, el más relevante
> hoy: **no confundir a Machete con los actores de `CTI-2026-020` y `CTI-2026-022`.**
> Comparten región, idioma y hasta el pretexto de la citación judicial, pero Machete roba
> documentos de Estado con herramienta propia en Python y los otros roban credenciales con
> troyano comercial. Son dos negocios distintos en el mismo barrio.

## O-2. Atribución: qué se puede sostener

| Eje de atribución | Valoración | Confianza |
|---|---|---|
| Idioma de operación | Español nativo, en los dos extremos. Kaspersky observa que los nombres de los ficheros robados, el código del lado del servidor —`reportes`, `ingresar`, `peso`— y el código del cliente están en español, y concluye que «tanto atacantes como víctimas hablan español de forma nativa» | Alta |
| Presencia en la región | **Probable, y el indicio es administrativo.** El estudio académico encontró las rutas del servidor FTP nombradas con ciudades y regiones colombianas —`Buenaventura`, `Guajira`, `Huila`— y sugiere que podrían indicar dónde están estacionados los operadores. 360 observó que la mayoría de los activos de red estaban en Colombia. ESET interpreta la capacidad de copiar a un USB concreto como posible presencia física en un país objetivo | Moderada |
| Unidad del operador | Un único grupo. El estudio académico lo apoya en que **tres claves AES aparecen compartidas entre las 105 muestras** y en el solapamiento de infraestructura a lo largo de ocho años | Moderada |
| Motivación | Espionaje político y militar. No hay un solo caso documentado de extorsión, de cifrado ni de fraude financiero en doce años | Alta |
| Nexo estatal | **Planteado por una sola fuente, y como posibilidad.** El estudio académico dice que las actividades «podrían estar patrocinadas por un Estado». Kaspersky, ESET y 360 no entran | Baja |
| Estado atribuido | **Ninguno.** Ninguna fuente nombra un país responsable, y este informe tampoco. 360 sí atribuye una intención política —apoyar a un sector del conflicto venezolano— y lo declara expresamente como conjetura: «suponemos» | Alta (en la negativa) |
| Capacidad técnica | **Baja para su categoría, alta para su resultado.** Sin días cero, sin antianálisis avanzado, con FTP en claro y Python legible. Y con más de una década dentro de ministerios de defensa | Alta |

*Razonamiento sobre las rutas FTP:* es el indicio más interesante de todo el expediente y conviene entender por qué, y también por qué no basta. Nombrar las carpetas de un servidor de exfiltración con topónimos de un país es una decisión de comodidad administrativa de quien las usa a diario; no es una cadena de código ni un artefacto de compilación, y por eso es difícil de plantar deliberadamente. Pero tampoco es prueba: un operador puede nombrar carpetas con topónimos del país que vigila, no del que habita, y los autores del estudio lo presentan con la cautela debida —«podrían indicar»—. Se consigna como lo que es: el mejor indicio disponible y no una conclusión.

*Contraargumento sobre el nexo estatal:* la motivación observada —documentos militares y políticos de países vecinos— es compatible con un servicio estatal y también con un contratista, con un grupo con intereses políticos propios y con un actor que revende a quien pague. Que el botín sea de interés estatal no prueba que el cliente sea un Estado. Es la misma cautela que este producto aplica en §O-2 de `CTI-2026-017`.

## O-3. Qué roba, y por qué eso determina a quién le importa

El objetivo es documentación, y el detalle de qué documentación es lo más útil operativamente de todo el informe.

**Los ficheros que busca.** Además de los formatos de Microsoft Office, el componente de recolección va expresamente a por: ficheros de respaldo, ficheros de base de datos, **claves criptográficas PGP**, documentos de OpenOffice, imágenes vectoriales y **ficheros de sistemas de información geográfica**, que ESET describe como «mapas topográficos y rutas de navegación». Y el remate: los operadores recogen ficheros que «describen rutas de navegación y posicionamiento usando cuadrículas militares».

**Lo que toma del equipo.** Capturas de pantalla, registro de pulsaciones, portapapeles, perfiles de varios navegadores, audio del micrófono, fotos de la cámara, geolocalización —calculada enviando los datos de las redes Wi-Fi cercanas al servicio de localización de Mozilla y construyendo con la respuesta una URL de Google Maps—, y el contenido de las unidades extraíbles que se inserten.

**Cómo sale.** Los documentos se cifran con AES y se suben por **FTP**, con HTTP como canal de reserva incorporado en 2019. Las credenciales del FTP están en el código o, en versiones nuevas, en un fichero de configuración (`jer.dll`). El estudio académico subraya el punto débil: «la comunicación FTP no está cifrada». Hay un segundo canal que no pasa por la red: **copiar los datos a un dispositivo USB concreto cuando se inserta**, lo que implica alguien que recoja físicamente ese dispositivo.

**Lo que esto implica para nosotros, y es la parte que no es del SOC.** Si la pregunta es «¿somos objetivo?», la respuesta documentada es no: no somos un ministerio de defensa andino. Si la pregunta es «¿tenemos lo que este actor roba?», la respuesta depende de una revisión que no ha hecho nadie: **quién, en nuestra organización o entre nuestros subcontratistas, produce o custodia cartografía, catastro, rutas, posiciones de infraestructura o documentación técnica para un cliente estatal.** Esa es la decisión `E-c`, y hasta que se responda, este informe no se puede priorizar ni descartar con honestidad.

## O-4. Nuestra exposición

<!-- cti:note type="gap" -->

> ⬛ **Sección sin evaluar — requiere telemetría, inventario y revisión de contratos.** A
> diferencia de los informes anteriores, aquí **tres de las once preguntas no son técnicas**
> (X-8, X-9, X-10) y no las puede responder el SOC. Son de Contratos, de Riesgo y de
> Dirección. Y son las que deciden si este producto nos aplica.

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| X-1 | ¿Hay tráfico **FTP en claro** desde estaciones de trabajo o servidores de usuario hacia Internet? ¿Hacia dónde y desde cuándo? | Cortafuegos · proxy · NetFlow | SOC |
| X-2 | ¿Aparece alguno de los indicadores del Anexo A en los registros históricos que conservemos? | Retrohunt en SIEM y EDR | SOC |
| X-3 | ¿Se ejecuta Python desde rutas de usuario en algún equipo? ¿Con qué argumentos y con qué proceso padre? | EDR · creación de procesos | SOC |
| X-4 | ¿Hay tareas programadas que ejecuten binarios con nombre de producto de Google (`GoogleCrash.exe`, `GoogleUpdate.exe`, `Chrome.exe`) desde rutas de perfil de usuario? | Inventario de arranque automático · EDR | Ingeniería de Detección |
| X-5 | ¿Permitimos la descarga de ejecutables desde Dropbox y Google Docs por procesos que no son navegadores? | Proxy con atribución de proceso | Redes / SOC |
| X-6 | ¿Detectamos la escritura masiva de ficheros a una unidad extraíble, y está permitido el uso de USB? | EDR · directiva de dispositivos | Seguridad / TI |
| X-7 | ¿Detectamos consultas al servicio de localización de Mozilla o composición de URL de Google Maps por procesos que no son navegadores? | Proxy | Ingeniería de Detección |
| X-8 | **¿Qué contratos nuestros tocan defensa, cancillería, policía, cartografía, catastro, puertos o concesiones de infraestructura?** | Dirección de Contratos | Contratos / Riesgo |
| X-9 | **¿Dónde están nuestros ficheros GIS y cartográficos, quién los produce, con quién se comparten y están cifrados en reposo?** | Inventario de información | Riesgo / TI |
| X-10 | **¿Tenemos un procedimiento de respuesta ante sospecha de espionaje, distinto del de ransomware?** | Revisión documental | CISO |
| X-11 | ¿Tenemos registro de conexiones salientes y de creación de procesos con retención suficiente para que el retrohunt de X-2 signifique algo? | Revisión de fuentes del SIEM | Ingeniería de Detección |

## O-5. Cronología

<!-- cti:timeline -->

| Fecha | Hecho | Traza |
|---|---|---|
| `2008` | Fechas de compilación de algunos instaladores observados por Kaspersky «se remontan a 2008» | Global |
| `2010` | **Inicio estimado de la campaña**, según Kaspersky | Región andina |
| `2011` | Muestra más antigua del corpus analizado por el estudio académico | Región andina |
| `2012` | La operación se renueva «con una infraestructura mejorada», según Kaspersky | Región andina |
| `2014-08-20` | **Kaspersky GReAT publica «El Machete»**: víctimas en Venezuela, Ecuador, Colombia, Perú, Rusia (embajadas), Cuba y España; perfiles de inteligencia, militares, embajadas y gobierno; implante en Python; señuelos con nombres como `El arte de la guerra.rar` y `Hermosa XXX.pps.rar`; componente para Android y preparativos para macOS y Unix | Región andina |
| `2017-03-22` | **Cylance publica «El Machete's Malware Attacks Cut Through LATAM»**: unas 300 víctimas únicas en un mes, más de 100 GB robados, dieciocho países, y migración a infraestructura nueva basada en DNS dinámico. *Artículo no accesible hoy; cifras de prensa especializada (§3.3)* | Región andina y más allá |
| `2018-04` | ESET sitúa aquí la aparición de la **versión nueva** del malware que analizará en 2019 | Región andina |
| `2018-08` | Se añade a la ofuscación una capa de `pyminifier` con compresión `zlib` sobre el `pyobfuscate` previo | — |
| `2019-05-21` | **Documento oficial clasificado usado como señuelo el mismo día de su fecha**, según ESET: el archivo comprimido que lo contenía se envió por primera vez esa jornada | Venezuela |
| `2019-03` → `05` | Ventana de medición de ESET: **más de cincuenta equipos** activos contra el mando y control, más del 75 % en organismos del Estado venezolano, con «gigabytes subidos cada semana» | Venezuela · Ecuador · Colombia · Nicaragua |
| `2019-05` | Los operadores dejan de usar descargadores separados y empaquetan señuelo y puerta trasera en el mismo archivo | — |
| `2019-07-29` | Fecha del evento MISP del repositorio de indicadores de ESET, con 396 atributos. **Son los últimos indicadores públicos de este actor** | — |
| `2019-08-05` | **ESET publica «Sharpening the Machete»** y su documento técnico, con los componentes `GoogleCrash.exe`, `Chrome.exe`, `GoogleUpdate.exe` y `jer.dll`, el canal FTP y la lista de ficheros objetivo, incluidos los GIS | Venezuela · Ecuador |
| `2019` | **El Civilsphere Project presenta en Virus Bulletin** su estudio sobre 105 muestras y 63 señuelos de ocho años: tres claves AES compartidas, 14 dominios FTP, rutas con topónimos colombianos, propagación por USB y la hipótesis de patrocinio estatal | Región andina |
| `2020-06` | 360 descubre la puerta trasera `Pyark` mediante su función de protección contra ataques sin fichero | Venezuela |
| `2020-09-25` | **360 publica la campaña `HpReact`**: instituciones militares venezolanas, señuelo sobre una política contra la deserción de soldados hacia Colombia, `MSI` de 8,10 MB disfrazado de instalador de Adobe Acrobat Reader, módulos `UpdateSession`, `UpdateService`, `UpdateDevice`, `UpdatePlugin` y `Notification`, y gestión de lo exfiltrado con Tiny File Manager sobre FTP. **Es el último informe de primera mano** | Venezuela |
| `2021` → `2026` | **Seis años sin un solo informe público de primera mano.** MITRE actualiza la ficha `G0095` a versión 2.0 el 31-jul-2026, con revisión de mapeo y las mismas cuatro referencias de 2014 a 2020 | — |
| `2026-11-16` | Cierre de este informe. Sin actividad documentada posterior a 2020, sin víctima chilena en ninguna fuente, y con una de las cuatro fuentes primarias ya inaccesible en su dirección original | Chile |

## O-6. Hipótesis alternativas consideradas

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| H1 — Un único grupo hispanohablante con presencia en la región andina, motivado por espionaje político y militar, operando desde 2010 | Consistente con las cuatro fuentes. El estudio académico lo apoya técnicamente con las tres claves AES compartidas entre 105 muestras y con el solapamiento de infraestructura a lo largo de ocho años | `Retenida` |
| H2 — El actor cesó, fue desarticulado o se transformó hasta ser irreconocible después de 2020 | Compatible con el silencio de seis años. **Inconsistencia:** no hay ninguna fuente que documente un cese, una detención ni una transformación, y un grupo de esta longevidad raramente desaparece en silencio absoluto | `Posibilidad real · 45–55 %` |
| H3 — El actor sigue operando y el silencio es de los observadores, no del actor | Igual de compatible con la evidencia, y más compatible con la cobertura comercial escasa de la región: tres proveedores en doce años, ninguno con telemetría regional dominante. **Es la hipótesis que exige acción por nuestra parte** y por eso conviene no adoptarla por comodidad | `Posibilidad real · 45–55 %` |
| H4 — La ausencia de Chile en la victimología refleja una decisión real del actor | Apoyada por cuatro fuentes independientes que enumeran hasta dieciocho países sin incluirlo, y por la coherencia del conjunto de objetivos: Venezuela y los países andinos, con las embajadas de esos países en terceros lugares. **Es el juicio más sólido del informe sobre Chile** | `Probable · 55–80 %` |
| H5 — La ausencia de Chile refleja falta de observación y no falta de objetivo | Posible: ninguno de los cuatro trabajos tenía telemetría chilena ni se propuso buscarla, y el estudio académico advierte que no pudo reproducir las cifras de victimología de los demás. **Se retiene como advertencia contra la complacencia**, no como conclusión | `Retenida como matiz` |
| H6 — Hay patrocinio estatal | Planteado por el estudio académico como posibilidad y no por las tres fuentes comerciales. Ni confirmado ni descartable. Importa poco operativamente —las detecciones son las mismas— y mucho políticamente | `Retenida sin resolver` |
| H7 — Machete y los actores de `CTI-2026-020` y `CTI-2026-022` son el mismo ecosistema | **Sin evidencia.** Comparten región, idioma y el pretexto judicial, y nada más: herramienta propia frente a troyano comercial, documentos de Estado frente a credenciales, FTP frente a DNS dinámico. Se consigna para que la coincidencia geográfica no se convierta en atribución | `Descartada` |

**Supuesto clave.** Que el arsenal descrito en §X-1 sigue siendo representativo de lo que este actor usaría hoy. **Si es falso** —y hay seis años para que lo sea— entonces todo el nivel técnico de este informe es arqueología: las detecciones por artefacto (`D-3` a `D-7`) no valdrían nada, y solo sobrevivirían las de canal y comportamiento (`D-1`, `D-2`, `D-8`). Es la razón por la que `E-b` se prioriza sobre el retrohunt: **la única detección que no depende de ese supuesto es la del FTP en claro.**

**Pre-mortem.** Es mayo de 2027 y este informe resultó equivocado. Los tres finales más probables: **(1)** aceptamos `H2`, archivamos el expediente, y aparece un informe de proveedor en 2027 documentando actividad continua desde 2021 con herramientas nuevas contra los mismos ministerios —y no habíamos desplegado ni la regla del FTP—; **(2)** acertamos en que Chile no es objetivo y el compromiso llegó por un subcontratista nuestro que hacía cartografía para un cliente estatal, es decir por `E-c`, que era de Contratos y se quedó sin hacer; **(3)** hicimos el retrohunt con indicadores de 2019, salió negativo, y lo interpretamos como «no estamos comprometidos» cuando solo significaba «no con los indicadores de hace siete años».

## O-7. Indicadores y señales de alerta

| # | Indicador observable | Qué señalaría | Disciplina | Responsable |
|---|---|---|---|---|
| I-1 | **Informe de primera mano sobre actividad de Machete posterior a 2020** | Resuelve `KJ-4` y obliga a reescribir el nivel técnico completo. Es el único indicador que justifica revisión anticipada | OSINT comercial · académico | Célula CTI |
| I-2 | Víctima chilena documentada, o señuelo con documentación oficial chilena | Invalidaría `H4` y convertiría este producto en una alerta | OSINT · CSIRT Nacional | Célula CTI |
| I-3 | Tráfico FTP en claro desde una de nuestras estaciones hacia una dirección no inventariada | No es específico de este actor y es exactamente por eso valioso: cubre esta amenaza y cualquier otra que use el mismo canal | Cortafuegos · NetFlow | SOC |
| I-4 | Aparición de los componentes con nombre de producto de Google (`GoogleCrash.exe`, `GoogleUpdate.exe`, `Chrome.exe`) fuera de la ruta de instalación legítima | Artefacto característico de la versión de 2019. Barato de buscar | EDR | SOC |
| I-5 | Reaparición de alguno de los catorce dominios FTP históricos, o de infraestructura que los reutilice | Indicaría continuidad de infraestructura y permitiría fechar la reactivación | DNS pasivo · OSINT | Célula CTI |
| I-6 | Documentación oficial robada de un organismo chileno circulando como señuelo de cualquier actor | El patrón de reutilizar documentos auténticos no es exclusivo de Machete, y su aparición con material chileno afectaría a la credibilidad de toda notificación oficial | OSINT · CSIRT Nacional | Célula CTI |
| I-7 | Interés público nuevo del actor por el Cono Sur: campaña, señuelo o víctima | Materializaría el escenario menos probable y el de mayor impacto para nosotros | OSINT comercial | Célula CTI |
| I-8 | Publicación de un actor nuevo con el mismo conjunto de objetivos y herramienta en Python o similar | Apoyaría `H2` en su variante de reorganización bajo otro nombre | OSINT comercial | Célula CTI |

---

# NIVEL TÁCTICO
### Para: Analistas de SOC · Ingeniería de Detección · Threat Hunting · Horizonte: días–semanas

## T-1. Cadena de intrusión

<!-- cti:note type="warn" -->

> ⚠ **Esta cadena describe la versión de 2019-2020 y no se sabe si es la actual.** Es la
> última documentada. Lo que de ella conserva valor con seguridad es la **etapa 04**, el
> canal de exfiltración, porque es la que menos ha cambiado en toda la serie temporal:
> FTP en 2014, FTP en 2019, FTP en 2020.

<!-- cti:stages title="Cuatro etapas, y el eslabón más débil del actor está en la última" dwell="next" -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 01 · Correo | El documento auténtico que la víctima reconoce | Correo dirigido, **muy específico y distinto para cada objetivo**, con enlace o con adjunto · archivo autoextraíble comprimido construido con `7z SFX Builder` · el extractor abre un documento señuelo `PDF` o de Office y ejecuta el descargador · **el señuelo es con frecuencia un documento oficial auténtico robado a una víctima anterior**, en un caso fechado el mismo día del envío · tipos de señuelo documentados: `Radiograma` militar venezolano, reportes operacionales, formatos de novedades de personal, mapas de monitoreo, calendarios de actividades, propuestas comerciales, notas diplomáticas · en 2014, señuelos de temática sexual y presentaciones de PowerPoint · temas también documentados: cobro de deuda y **citación judicial** |
| Etapa 02 · Descargador | Un ejecutable de Python que trae lo demás | Segundo autoextraíble con un binario `py2exe` descargador y un fichero de configuración con la URL cifrada · **todas las URL de descarga observadas estaban en Dropbox o en Google Docs** · la carga es un `RAR SFX` con la configuración cifrada y los componentes de la puerta trasera · **desde mayo de 2019 el descargador desaparece** y el señuelo y la puerta trasera viajan en el mismo archivo · en 2020, un `MSI` de 8,10 MB construido con MSI Wrapper, con metadatos falsificados de Adobe Acrobat Reader, que incorpora un entorno de Python completo |
| Etapa 03 · Implante | Tres o seis componentes y una tarea programada | Versión 2019: `GoogleCrash.exe` (componente principal, programa a los demás y **crea las tareas del Programador de tareas de Windows para persistir**), `Chrome.exe` (recolección), `GoogleUpdate.exe` (mando y control) y `jer.dll` (configuración con cadenas AES en base64) · versión 2020: módulos `UpdateSession`, `UpdateService`, `UpdateDevice`, `UpdatePlugin` y `Notification`, desplegados desde `%ProgramData%\USOEnable` con `svchostt.exe` y un `NisSrv.bat` que registra las tareas · versión 2014: instalación en `appdata/MicroDes/`, acceso directo `Java Update.lnk` apuntando a `appdata/Jre6/java.exe`, tarea `Microsoft_up` · ofuscación con `pyobfuscate` y, desde ago-2018, `pyminifier` con `zlib` y base64 · última versión descrita: **seis componentes que ya no son `py2exe`**, con intérprete de Python 2.7 original y bibliotecas en un autoextraíble |
| Etapa 04 · Exfiltración | FTP en claro, cada diez minutos, y un USB | Documentos **cifrados con AES** y subidos a subdirectorios del servidor · **FTP como canal principal, en claro**, con las credenciales en el código o en `jer.dll` · HTTP como canal de reserva, incorporado en 2019 · envío programado **cada diez minutos** · el operador deja ficheros en el servidor para que el implante los recoja: configuración nueva, binarios a ejecutar, listados de ficheros a buscar · gestión de lo recibido con **Tiny File Manager** sobre el propio FTP (2020) · segundo canal: **copia a un dispositivo USB concreto al insertarse**, que implica recogida física · las rutas del servidor llevan nombres de ciudades y regiones colombianas |

**Permanencia:** no hay cifra publicada por incidente, pero el conjunto da la escala. El estudio académico analizó muestras que abarcan de 2011 a 2019 con tres claves AES comunes; ESET midió más de cincuenta equipos activos simultáneamente en una ventana de tres meses con «gigabytes subidos cada semana»; 360 describió vigilancia y robo durante «unos dos años» en su campaña. **La permanencia de este actor se mide en años, no en días.**

<!-- cti:note type="info" -->

> **Dónde se rompe la cadena más barato, y aquí la respuesta es inusualmente clara.** La
> **etapa 01 es casi irrompible por formación**: el señuelo es un documento auténtico,
> dirigido, en el idioma correcto y con la jerga institucional correcta. Pedirle al usuario
> que lo distinga es pedirle demasiado. La **etapa 02 se rompe con una regla de proxy**:
> descarga de ejecutable desde Dropbox o Google Docs por un proceso que no es navegador.
> La **etapa 03 se rompe con dos detecciones de host** —Python desde ruta de usuario, y
> binarios con nombre de producto de Google fuera de su ruta legítima—, ambas baratas y
> ambas dependientes de que el arsenal no haya cambiado. Y la **etapa 04 es el regalo**:
> **FTP en claro desde una estación de trabajo hacia Internet es una anomalía detectable
> sin ningún indicador, con la telemetría que ya tenemos, y seguirá siéndolo aunque el
> actor reescriba todo lo demás.** Si de este informe solo se implementa una cosa, que sea
> esa.

## T-2. Mapa MITRE ATT&CK

<!-- cti:matrix -->

| Táctica | ID | Técnica | Procedimiento observado |
|---|---|---|---|
| Acceso inicial | T1566.001 | Phishing: Spearphishing Attachment | Correo dirigido con autoextraíble comprimido y documento señuelo auténtico |
| Acceso inicial | T1566.002 | Phishing: Spearphishing Link | Enlace a servidor externo con archivos `ZIP` y `RAR` |
| Acceso inicial | T1189 | Drive-by Compromise | Infección por web mediante **un sitio de blog falso**, con el código HTML copiado del Social Engineering Toolkit (Kaspersky, 2014) |
| Ejecución | T1204.001 | User Execution: Malicious Link | La víctima abre el enlace del correo dirigido |
| Ejecución | T1204.002 | User Execution: Malicious File | La víctima ejecuta el autoextraíble, que muestra el señuelo |
| Ejecución | T1059.003 | Command and Scripting Interpreter: Windows Command Shell | Ficheros `.bat` que inician descargas adicionales (`NisSrv.bat`) |
| Ejecución | T1059.005 | Command and Scripting Interpreter: Visual Basic | Macros maliciosas en los adjuntos dirigidos; el liberador de 2020 está escrito en Visual Basic |
| Ejecución | T1059.006 | Command and Scripting Interpreter: Python | **Rasgo definitorio del actor:** múltiples componentes en Python compilado |
| Ejecución | T1218.007 | System Binary Proxy Execution: Msiexec | `msiexec` instala el implante desde el `MSI` disfrazado de Adobe Acrobat Reader |
| Persistencia | T1053.005 | Scheduled Task/Job: Scheduled Task | `GoogleCrash.exe` crea tareas del Programador de tareas; tarea `Microsoft_up` en 2014; `NisSrv.bat` registra las tareas en 2020 |
| Persistencia | T1547.001 | Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder | Acceso directo `Java Update.lnk` apuntando a `appdata/Jre6/java.exe` (2014) |
| Evasión | T1036.004 | Masquerading: Masquerade Task or Service | Tarea con nombre `Microsoft_up`; módulos con nombres de servicio de actualización (`UpdateSession`, `UpdateService`) |
| Evasión | T1036.005 | Masquerading: Match Legitimate Resource Name or Location | `MSI` con metadatos de Adobe Acrobat Reader; componentes con nombre de productos de Google; `svchostt.exe` con una `t` de más |
| Evasión | T1027.002 | Obfuscated Files or Information: Software Packing | `py2exe`; autoextraíbles anidados |
| Evasión | T1027.010 | Obfuscated Files or Information: Command Obfuscation | `pyobfuscate` sobre el código fuente; `pyminifier` con `zlib` y base64 desde ago-2018 |
| Evasión | T1564.001 | Hide Artifacts: Hidden Files and Directories | Ficheros y carpetas ocultos |
| Evasión | T1070.004 | Indicator Removal: File Deletion | Borrado de artefactos tras la ejecución |
| Acceso a credenciales | T1555.003 | Credentials from Password Stores: Web Browsers | Recuperación de los perfiles de varios navegadores |
| Acceso a credenciales | T1552.004 | Unsecured Credentials: Private Keys | **Búsqueda expresa de claves PGP en el disco** |
| Descubrimiento | T1083 | File and Directory Discovery | Recorrido del disco buscando por extensión; más de diez tipos de fichero en la versión de 2020 |
| Descubrimiento | T1120 | Peripheral Device Discovery | Detección de unidades extraíbles recién insertadas |
| Descubrimiento | T1057 | Process Discovery | Enumeración de procesos |
| Descubrimiento | T1082 | System Information Discovery | Información del sistema y de configuración de red |
| Descubrimiento | T1016 | System Network Configuration Discovery | Configuración de red, incluidas las redes Wi-Fi cercanas |
| Descubrimiento | T1016.002 | System Network Configuration Discovery: Wi-Fi Discovery | **Datos de Wi-Fi enviados al servicio de localización de Mozilla** para calcular la posición |
| Descubrimiento | T1217 | Browser Information Discovery | Marcadores y perfiles del navegador |
| Descubrimiento | T1010 | Application Window Discovery | Títulos de ventana |
| Colección | T1113 | Screen Capture | Capturas de pantalla periódicas |
| Colección | T1056.001 | Input Capture: Keylogging | Registro de pulsaciones, almacenado en un fichero HTML |
| Colección | T1115 | Clipboard Data | Portapapeles, guardado en `Clip.html` |
| Colección | T1123 | Audio Capture | Audio del micrófono con `pyaudio`, codificado a MP3 con LAME |
| Colección | T1125 | Video Capture | Fotografías con la cámara |
| Colección | T1005 | Data from Local System | Ofimática, respaldos, bases de datos, OpenOffice, imágenes vectoriales y **ficheros GIS con rutas y cuadrícula militar** |
| Colección | T1025 | Data from Removable Media | Copia del contenido de las unidades extraíbles insertadas |
| Colección | T1074.001 | Data Staged: Local Data Staging | Preparación local antes del envío |
| Colección | T1560.003 | Archive Collected Data: Archive via Custom Method | Cifrado AES propio con tres claves compartidas entre muestras |
| Mando y control | T1071.001 | Application Layer Protocol: Web Protocols | HTTP como canal de reserva, incorporado en 2019 |
| Mando y control | T1071.002 | Application Layer Protocol: File Transfer Protocols | **FTP como canal principal, sin cifrar.** Es el rasgo más estable del actor en doce años |
| Mando y control | T1008 | Fallback Channels | FTP principal, HTTP de reserva |
| Mando y control | T1105 | Ingress Tool Transfer | El operador deja binarios en el servidor para que el implante los ejecute |
| Mando y control | T1132.001 | Data Encoding: Standard Encoding | Base64 sobre las cadenas AES de la configuración |
| Mando y control | T1573.001 | Encrypted Channel: Symmetric Cryptography | AES sobre los documentos antes del envío |
| Mando y control | T1102 | Web Service | **Dropbox y Google Docs** como origen de descarga de la carga |
| Exfiltración | T1041 | Exfiltration Over C2 Channel | Documentos cifrados subidos al FTP del actor |
| Exfiltración | T1020 | Automated Exfiltration | Envío automático, programado |
| Exfiltración | T1029 | Scheduled Transfer | **Cada diez minutos** |
| Exfiltración | T1052.001 | Exfiltration over Physical Medium: USB | **Copia a un dispositivo USB concreto al insertarse**, lo que implica recogida física |

<!-- cti:note type="warn" -->

> ⚠ **Procedencia del mapeo.** MITRE publica para el grupo `G0095` once técnicas y para el
> malware `S0409` una lista extensa; este informe las recoge y las moderniza —el artículo
> de ESET de 2019 usaba la numeración antigua (`T1192`, `T1193`, `T1158`, `T1045`, `T1002`,
> `T1022`, `T1043`…) y aquí se han traducido a la actual—. **La traducción de identificadores
> obsoletos es nuestra**, igual que la asignación de `T1552.004` a la búsqueda de claves PGP y
> de `T1016.002` a la geolocalización por Wi-Fi, que las fuentes describen en prosa sin
> asignarles técnica. Debe tratarse como tal.

## T-3. Dónde atacamos en la Pirámide del Dolor

<!-- cti:pyramid -->

| Nivel | Qué contiene en este informe y qué vale | Valor |
|---|---|---|
| Hashes | Más de doscientos entre los tres ficheros del repositorio de ESET —84 MD5, un centenar de SHA-1 y un centenar de SHA-256— más tres MD5 de 360. **Valor nulo para prevenir y alto para una sola cosa:** el retrohunt de la decisión `E-a`. Son de 2019 y 2020. Un negativo con ellos no prueba nada sobre hoy, y aun así merece la pena registrarlo | Base · valor trivial |
| IP · Dominios | Catorce dominios FTP y una docena de direcciones, incluidos dos túneles `ngrok`, dos subdominios de alojamiento gratuito y dos nombres que **suplantan a la institución objetivo** (`ceofanb18.mipropia.com`, `lawyersofficial.mipropia.com`). Caducados hace años; valor de retrohunt y de vigilancia de reaparición (`I-5`) | Valor bajo |
| Artefactos | **Lo más duradero que se publicó de este actor.** Nombres de componente `GoogleCrash.exe`, `Chrome.exe`, `GoogleUpdate.exe`, `jer.dll`, `svchostt.exe`, `NisSrv.bat`; los seis scripts `.pyw` con nombres de módulo mal escritos a propósito (`_hashlbi.pyw`, `_multiproccessing.pyw`, `_elementree.pyw`, `_clypes.pyw`, `_mssi.pyw`, `_bsdbd.pyw`); rutas `appdata/MicroDes/`, `appdata/Jre6/java.exe`, `%ProgramData%\USOEnable`; tareas `Microsoft_up` y `Java Update.lnk`; el fichero `Clip.html`; la extensión `.scr` de los señuelos; la ruta de compilación `C:\Users\MITM\Desktop\malware\3_svchostt\Proyecto1.vbp` | Valor medio |
| Herramientas | Intérprete de Python, `py2exe`, `pyobfuscate`, `pyminifier`, `7z SFX Builder`, `RAR SFX`, MSI Wrapper, `msiexec`, `pyaudio`, LAME, Tiny File Manager, el Social Engineering Toolkit, Dropbox, Google Docs, el servicio de localización de Mozilla. **Todas legítimas o de uso libre** | Valor alto |
| TTP | **FTP en claro desde una estación de trabajo hacia Internet** (el único que no caduca); intérprete de Python ejecutándose desde una ruta de perfil de usuario; autoextraíble que abre un documento y lanza un ejecutable; descarga de ejecutable desde Dropbox o Google Docs por un proceso que no es navegador; escritura masiva a unidad extraíble; tarea programada que lanza un binario con nombre de producto de Google desde el perfil del usuario | Cima · valor máximo |

## T-4. Hipótesis de caza prioritarias

<!-- cti:accordion critical="^(H-1|H-2|H-3)\b" regional="^(H-12|H-13)\b" -->

**H-1 — FTP en claro desde una estación de trabajo o un servidor de usuario hacia Internet.** Conexiones salientes a los puertos 21 y 20, o tráfico reconocido como FTP por el cortafuegos, originado en segmentos de usuario y con destino fuera de nuestro inventario. Fuente: cortafuegos, NetFlow, proxy. **Es la hipótesis madre de este informe y la única que no caduca:** FTP fue el canal de exfiltración en 2014, en 2019 y en 2020, y una estación de trabajo moderna no tiene ninguna razón legítima para hablar FTP en claro contra Internet. Fidelidad extremadamente alta. Falsos positivos conocidos: transferencias con proveedores antiguos y equipos de laboratorio, exceptuables por destino y por equipo, nunca desactivando la regla. **Vale además contra cualquier otra amenaza que use el mismo canal, que son muchas.**

**H-2 — Intérprete de Python ejecutándose desde una ruta escribible por el usuario.** `python.exe`, `pythonw.exe` o cualquier binario cuyo nombre original sea ése, ejecutándose desde `%APPDATA%`, `%LOCALAPPDATA%`, `%TEMP%`, `%ProgramData%` o el perfil del usuario; y procesos cuyo nombre sea `.pyw` o que carguen `python27.dll` desde esas rutas. Fuente: creación de procesos del EDR, carga de imagen. **Es la firma de la familia desde 2010.** Fidelidad alta en un parque corporativo; baja en un entorno de desarrollo o de ciencia de datos, donde hay que acotar por unidad organizativa antes de alertar.

**H-3 — Binario con nombre de producto de Google fuera de su ruta de instalación legítima.** Procesos llamados `GoogleCrash.exe`, `GoogleUpdate.exe` o `Chrome.exe` cuya ruta no esté bajo `Program Files`, `Program Files (x86)` o el directorio de usuario legítimo de Chrome, y en particular si están acompañados de un `jer.dll`. Fuente: creación de procesos, inventario de ficheros. **`GoogleCrash.exe` no es un producto de Google;** los otros dos sí existen y por eso la señal está en la ruta. Fidelidad muy alta y coste de implementación casi nulo. Advertencia obligada: son nombres de 2019, triviales de cambiar, y llevan siete años publicados.

**H-4 — Autoextraíble que abre un documento y lanza un ejecutable.** Procesos de descompresión (`7z`, `WinRAR`, autoextraíbles con icono de documento) cuyo hijo sea un ejecutable en una ruta temporal, con un visor de documentos abierto en la misma ventana de tiempo; y ficheros con extensión `.scr` recibidos o creados. Fuente: creación de procesos con línea de comandos, creación de ficheros. **La extensión `.scr` de los señuelos es un artefacto sorprendentemente útil:** no tiene uso legítimo moderno y aparece en 26 de los nombres de señuelo publicados. Fidelidad alta.

**H-5 — Descarga de ejecutable desde Dropbox o Google Docs por un proceso que no es navegador.** Peticiones a `dropbox.com`, `docs.google.com` o `drive.google.com` con descarga de contenido ejecutable o comprimido, originadas por un proceso que no es un navegador en uso interactivo. Fuente: proxy con atribución de proceso. **Todas las URL de descarga que ESET observó estaban en esos dos servicios.** Fidelidad alta donde haya atribución de proceso; es la misma hipótesis que `H-5` de `CTI-2026-022` con otros servicios, y conviene unificarlas en una sola regla de plataforma.

**H-6 — Tarea programada que ejecuta un binario desde el perfil del usuario con nombre de servicio de actualización.** Tareas cuyo destino esté en `%APPDATA%`, `%LOCALAPPDATA%` o `%ProgramData%` y cuyo nombre o destino invoque actualización, mantenimiento o informe de errores: `Microsoft_up`, `UpdateSession`, `UpdateService`, `GoogleUpdate`, `java.exe` bajo `appdata`. Fuente: inventario de arranque automático, registro de tareas programadas. Fidelidad alta; es el mecanismo de persistencia constante del actor en las tres versiones documentadas.

**H-7 — Escritura masiva de ficheros a una unidad extraíble.** Un proceso que no es el explorador ni una herramienta de respaldo copiando un volumen anómalo de ficheros de ofimática, respaldo o GIS a una unidad extraíble poco después de su inserción. Fuente: eventos de ficheros del EDR, directiva de dispositivos. **Es el canal de exfiltración que no pasa por la red** y, por tanto, el que ninguna regla de red detecta. Si esto dispara, hay alguien con acceso físico. Fidelidad alta donde el EDR lo soporte.

**H-8 — Consulta al servicio de localización de Mozilla o composición de URL de Google Maps por un proceso que no es navegador.** Peticiones a `location.services.mozilla.com` o a la API de geolocalización, y construcción de URL de Google Maps con coordenadas, por procesos no interactivos. Fuente: proxy con atribución de proceso. **Es la técnica de geolocalización más inusual del expediente y por eso mismo específica:** casi nada legítimo en un parque corporativo geolocaliza el equipo a partir de las redes Wi-Fi cercanas. Fidelidad muy alta, cobertura baja.

**H-9 — Búsqueda o acceso a claves criptográficas privadas en el disco.** Acceso o copia de ficheros con extensión de clave PGP o GPG, anillos de claves, o ficheros de clave privada, por un proceso que no es el gestor de claves. Fuente: auditoría de acceso a ficheros. **`T1552.004` aparece explícitamente en la ficha de MITRE para este malware**, y es una de las pocas capacidades del actor con consecuencia duradera: una clave privada robada sobrevive a la limpieza del equipo. Fidelidad alta.

**H-10 — Acceso anómalo a ficheros GIS y cartográficos.** Lectura o copia masiva de ficheros con extensiones de sistemas de información geográfica, cartografía o diseño por un proceso o una cuenta que no los usa habitualmente. Fuente: auditoría de acceso a ficheros, clasificación de información. **Requiere saber primero dónde están, que es la pregunta `X-9` de §O-4 y no está respondida.** Fidelidad dependiente por completo del inventario; sin él, la hipótesis no se puede escribir.

**H-11 — Registro de pulsaciones guardado en HTML.** Presencia de ficheros `Clip.html`, o de ficheros HTML en rutas de perfil de usuario con contenido de pulsaciones o de portapapeles. Fuente: inventario de ficheros, auditoría de integridad. **Artefacto de implementación concreto y barato de buscar**, documentado por el estudio académico. Fidelidad extremadamente alta y vida útil incierta: basta con que el autor cambie una línea.

**H-12 — Documentación oficial auténtica circulando como señuelo.** Adjuntos o archivos comprimidos que contengan documentos con membrete, radicado o numeración de un organismo público, especialmente si la fecha del documento es de los días previos. Fuente: pasarela de correo, análisis de adjuntos. **Es la hipótesis que corresponde al rasgo más difícil de defender de este actor**, y es también la que no tiene solución técnica: detectar que un documento oficial auténtico está siendo usado como señuelo exige saber que fue robado. Se incluye para que quede escrito que no la cubrimos.

**H-13 — Reaparición de la infraestructura histórica.** Resoluciones DNS o conexiones a los catorce dominios FTP del Anexo A, a los dos subdominios de `mipropia.com` que suplantan a la institución objetivo, o a las direcciones asociadas. Fuente: DNS, cortafuegos, DNS pasivo externo. **No se espera que dispare**, y eso es el punto: si alguna de esas infraestructuras vuelve a resolver, es el dato que faltaba para fechar una reactivación (`I-5`). Coste de implementación: una lista estática.

## T-5. Brechas de visibilidad que hay que cerrar primero

| Brecha | Por qué importa aquí |
|---|---|
| Sin registro de conexiones salientes por protocolo con retención suficiente | Deja ciega `H-1`, que es la única detección de este informe que no caduca. Es la brecha más determinante y la más fácil de cerrar |
| Proxy sin atribución de proceso | Degrada `H-5` y `H-8` a listas de servicios legítimos, inservibles para alertar |
| Registro de línea de comandos en creación de procesos deshabilitado | Deja ciegas `H-2`, `H-3`, `H-4` y `H-6`, es decir las etapas 02 y 03 completas |
| Sin inventario de información que localice ficheros GIS y cartográficos | **Deja `H-10` sin poder escribirse.** No es una brecha de telemetría: es una brecha de gobierno de la información, y la responde `X-9` |
| Sin retención histórica suficiente para un retrohunt significativo | Convierte la decisión `E-a` en un ejercicio formal: buscar indicadores de 2019 en treinta días de registros no descarta nada |
| Sin telemetría de dispositivos extraíbles | Deja ciega `H-7` y con ella el canal de exfiltración que no pasa por la red |
| Sin auditoría de acceso a ficheros de clave privada | Deja ciega `H-9`, cuyo impacto es el más duradero de todos los que este actor produce |
| Sin procedimiento de respuesta ante sospecha de espionaje | No es una brecha de visibilidad sino de reacción: si `H-1` dispara de verdad, el procedimiento de ransomware que tenemos destruiría la evidencia y avisaría al adversario |
| Sin archivo local de las fuentes de inteligencia que citamos | Ya nos ha costado una fuente primaria (§E-3). No afecta a la detección y sí a la trazabilidad de nuestros propios productos |

---

# NIVEL TÉCNICO
### Para: Ingeniería de detección · Automatización · TIP/SIEM · Vida útil: histórica, véase la advertencia

<!-- cti:note type="warn" -->

> ⚠ **Todo este nivel describe el arsenal de 2014 a 2020.** No hay información posterior.
> Las detecciones por artefacto de implementación (`D-3` a `D-7`) tienen por tanto una
> vida útil desconocida y posiblemente nula; las de canal y comportamiento (`D-1`, `D-2`,
> `D-8`, `D-9`) son las que sobreviven a un cambio de herramienta. Esta distinción no es
> académica: determina el orden de implementación.

## X-1. Arsenal y capacidad del actor

| Propiedad | Valor |
|---|---|
| Lenguaje del implante | **Python**, en todas las versiones documentadas desde 2010. Kaspersky lo calificó de «muy inusual» en 2014 y señaló que solo aporta facilidad de desarrollo |
| Empaquetado | Instaladores Nullsoft de más de 3 MB con todas las bibliotecas de Python (2014) · `py2exe` (2018-2019) · autoextraíbles `7z SFX` y `RAR SFX` anidados · `MSI` de 8,10 MB construido con MSI Wrapper y metadatos de Adobe Acrobat Reader (2020) · última versión descrita: scripts de Python con intérprete 2.7 original y bibliotecas en un autoextraíble, **sin `py2exe`** |
| Ofuscación | `pyobfuscate` sobre el código fuente; desde ago-2018, capa adicional con `pyminifier` y el parámetro `-gzip`, que produce bloques comprimidos con `zlib` y codificados en base64 |
| Componentes (versión 2019) | `GoogleCrash.exe` (principal, programación y persistencia) · `Chrome.exe` (recolección) · `GoogleUpdate.exe` (mando y control) · `jer.dll` (configuración: dominio, usuario y contraseña, en cadenas AES codificadas en base64) |
| Componentes (versión 2020) | `UpdateSession` (control principal, autoarranque, red, pulsaciones, temporización) · `UpdateService` (recorrido de disco, más de diez tipos de fichero) · `UpdateDevice` (pantalla y cámara) · `UpdatePlugin` (micrófono) · `Notification` (subida al FTP) · desplegados desde `%ProgramData%\USOEnable` vía `svchostt.exe` y `NisSrv.bat` |
| Componentes en Python (nombres de script) | `_hashlbi.pyw` · `_bsdbd.pyw` · `_clypes.pyw` · `_elementree.pyw` · `_mssi.pyw` · `_multiproccessing.pyw` — **nombres de módulos estándar deliberadamente mal escritos**, detectados por ESET como `Python/Machete.G` |
| Criptografía | **AES sobre los documentos antes de exfiltrarlos** y sobre las cadenas de configuración, con base64 por encima. El estudio académico encontró **tres claves AES compartidas entre las 105 muestras analizadas**, lo que es a la vez el argumento de atribución más fuerte y el peor fallo de diseño del actor |
| Canal de mando y control | **FTP en claro como principal**, con credenciales en el código o en el fichero de configuración · HTTP como reserva, incorporado en 2019 · envío programado **cada diez minutos** · 14 dominios de servidor FTP y 13 direcciones identificados por el estudio académico · **rutas del servidor nombradas con ciudades y regiones colombianas** |
| Canal secundario | **Copia a un dispositivo USB concreto al insertarse.** Implica recogida física y es invisible a toda detección de red |
| Alojamiento de la carga | **Dropbox y Google Docs** en todas las URL de descarga que ESET observó; túneles `ngrok`; alojamiento compartido gratuito (`hostingerapp.com`); DNS dinámico (`zapto.org`, `gotdns.ch`, `ddns.net`) |
| Recolección | Capturas de pantalla · registro de pulsaciones en fichero HTML · portapapeles (`Clip.html`) · perfiles de varios navegadores · micrófono con `pyaudio` codificado a MP3 con LAME · fotografías con la cámara · geolocalización por redes Wi-Fi mediante **el servicio de localización de Mozilla**, con una URL de Google Maps construida a partir de la respuesta |
| Ficheros objetivo | Microsoft Office · OpenOffice · **respaldos** · **bases de datos** · **claves PGP** · imágenes vectoriales · **ficheros GIS: mapas topográficos y rutas de navegación con cuadrícula militar** · en 2020, «más de diez tipos» incluidos `doc`, `xlsx` y `pdf`, saltando directorios del sistema y de productos de seguridad |
| Plataformas | Windows en todas las versiones · **componente para Android** (Kaspersky, 2014) · «indicios de que los atacantes prepararon la infraestructura también para víctimas de macOS y Unix» (Kaspersky, 2014), que **ninguna fuente posterior confirma** |
| Evasión de análisis | Ofuscación del código fuente; nombres de módulo mal escritos; ocultación de ficheros y carpetas; borrado de artefactos; salto de directorios de productos de seguridad. **Sin antimáquina virtual sofisticada, sin antidepuración avanzada, sin elusión de AMSI ni de ETW** |
| Lo que **no** tiene | Días cero —ninguna fuente documenta explotación de vulnerabilidad—, cifrador de extorsión, capacidad destructiva, movimiento lateral automatizado, canal cifrado de mando y control, ni criptografía de clave asimétrica para la exfiltración |

<!-- cti:note type="info" -->

> **Lo que este cuadro dice de la defensa, y es la lección más transferible del informe.**
> Este actor no tiene una sola capacidad que exija un producto nuevo para detectarla. No
> hay día cero que parchear, no hay canal cifrado que no podamos inspeccionar, no hay
> antianálisis que derrotar. **Exfiltra por FTP en claro cada diez minutos durante años.**
> Que haya funcionado más de una década dentro de ministerios de defensa no dice nada
> sobre su sofisticación: dice todo sobre cuánto tiempo puede sobrevivir una amenaza
> mediocre cuando nadie mira el tráfico saliente. Y eso es una afirmación sobre nosotros,
> no sobre él.

## X-2. Artefactos persistentes entre versiones

<!-- cti:cards -->

| Categoría | Artefactos | Etiqueta |
|---|---|---|
| Componentes de la versión 2019 | `GoogleCrash.exe` · `Chrome.exe` · `GoogleUpdate.exe` · `jer.dll` · `RdrCEF.exe` · `Down.exe` · `04Down.exe` · `ders.exe` · `python27.exe` · `Security.exe` · `finaser.aes` | `host` |
| Scripts en Python | `_hashlbi.pyw` · `_bsdbd.pyw` · `_clypes.pyw` · `_elementree.pyw` · `_mssi.pyw` · `_multiproccessing.pyw` — nombres de módulo estándar mal escritos a propósito | `código` |
| Rutas y persistencia (2014) | `appdata/MicroDes/` · acceso directo `Java Update.lnk` → `appdata/Jre6/java.exe` · tarea `Microsoft_up` | `persistencia` |
| Rutas y persistencia (2020) | `%ProgramData%\USOEnable` · `svchostt.exe` (con una `t` de más) · `NisSrv.bat` · `_setupXOX.msi` · tareas registradas desde el `.bat` | `persistencia` |
| Ruta de compilación del atacante | `C:\Users\MITM\Desktop\malware\3_svchostt\Proyecto1.vbp` — **el nombre de usuario del desarrollador y la carpeta `malware` en su escritorio** | `atribución` |
| Recolección | Registro de pulsaciones en fichero HTML · `Clip.html` para el portapapeles · uso de `pyaudio` y LAME para el audio · consulta al servicio de localización de Mozilla y URL de Google Maps construida | `código` |
| Señuelos militares venezolanos | `Radiograma 004026_pdf.scr` · `RGMA0_1_629.scr` · `RDGMA 1101 001 jpg.scr` · `RAD_N_0961_21MAY19.scr` · `RAD OFL0120_jpg.scr` · `REPORTE OPERACIONAL 10JUN19 pdf.scr` · `FORMATO UNICO DE RENDIMIENTO OPERATIVO GNB 11JUNIO2019 CZGNB-13 xlsx.scr` · `INSTRUCCIONES DEL JSO 08JUN19 docx.scr` · `FORMATO DE NOVEDADES PARA DC PERSONAL xls.scr` · `BOLETA DE PERMISO NELSON GUERERE docx.scr` · `Asimilacion.scr` · `Blason.scr` | `señuelo` |
| Señuelos diplomáticos y de otro tipo | `NOTA_CICR_00079.scr` · `S_E_ARLETTE_MARENCO_NOTA_INFORMANDO_TERMINO_DE_MISION_001.scr` · `INVITADOS_MEXICANOS.scr` · `Mapa_monitoreo_WRF_ind02052018.scr` · `CALENDARIO_ACTIVIDADES_COLCO_EC.scr` · `Programa Formacion en Contratacion Publica.scr` · `JUNIO_19_PROPUESTA_CLARO_RENOVACION.scr` · `12_JUN_2019MATRIZ_DE_OPERACIONES_CAMEX_EN_CRS.scr` | `señuelo` |
| Señuelos de 2014 | `Hermosa XXX.pps.rar` · `Hermosa XXX.rar` · `Suntzu.rar` · `El arte de la guerra.rar` · `EL ARTE DE LA GUERRA.exe` · `Hot Brazilian XXX.rar` · `Signed_Update.jar` · `AwgXuBV31pGV.eXe` | `señuelo` |
| Nombres de detección de producto | `Python/Machete.A` a `Python/Machete.G` (ESET) · `Trojan-Spy.Python.Ragua` (Kaspersky) | `detección` |

## X-3. Lógica de detección prioritaria

<!-- cti:detections -->

**D-1 · CRÍTICO — FTP en claro desde segmento de usuario hacia Internet**

```
network.transport == "tcp"
AND destination.port IN (20, 21)
AND source.zone IN ("estaciones", "servidores-usuario")
AND NOT destination.ip IN (<destinos FTP inventariados y aprobados>)
```

→ Alerta de prioridad crítica con captura de la sesión. **Es la regla que no caduca y la primera que hay que desplegar.** El canal de exfiltración de este actor es FTP sin cifrar en 2014, en 2019 y en 2020. Y la regla vale contra cualquier otra amenaza que use el mismo canal, lo que la hace la de mejor retorno del informe. Exceptuar por destino y por equipo con registro nominal, **nunca desactivándola por segmento**.

**D-2 · CRÍTICO — Intérprete de Python ejecutándose desde ruta escribible por el usuario**

```
(process.original_file_name MATCHES "(?i)^python(w)?\.exe$"
 OR process.name MATCHES "(?i)^python(w)?\.exe$"
 OR module.name MATCHES "(?i)^python[0-9]{2,3}\.dll$")
AND process.executable MATCHES "(?i)\\\\(Users|AppData|Temp|ProgramData)\\\\"
AND NOT process.executable MATCHES "(?i)\\\\(Anaconda|Miniconda|Python3[0-9]|venv|\.venv)\\\\"
AND NOT host.ou IN (<unidades de desarrollo y ciencia de datos>)
```

→ Alerta de prioridad alta con recolección de la carpeta de ejecución. Es la firma de la familia desde 2010. **La excepción por unidad organizativa es imprescindible**: en un equipo de desarrollo esta regla es ruido puro.

**D-3 · ALTO — Binario con nombre de producto de Google fuera de su ruta legítima**

```
process.name IN ("GoogleCrash.exe","GoogleUpdate.exe","Chrome.exe")
AND NOT process.executable MATCHES "(?i)^C:\\\\Program Files( \(x86\))?\\\\Google\\\\"
AND NOT process.executable MATCHES "(?i)\\\\AppData\\\\Local\\\\Google\\\\Chrome\\\\Application\\\\"
```

→ Contención automática en estaciones de trabajo. `GoogleCrash.exe` no existe como producto de Google; los otros dos sí, y por eso la señal es la ruta. Añadir como señal reforzada la presencia de un `jer.dll` en el mismo directorio.

**D-4 · ALTO — Persistencia hacia binario en perfil de usuario con nombre de actualización**

```
(registry.path MATCHES "(?i)\\\\CurrentVersion\\\\Run"
 OR file.path MATCHES "(?i)\\\\Start Menu\\\\Programs\\\\Startup\\\\"
 OR event.action == "scheduled-task-created")
AND target.path MATCHES "(?i)\\\\(AppData|Users|ProgramData)\\\\"
AND (target.name MATCHES "(?i)(update|crash|java|micro|uso)"
     OR task.name MATCHES "(?i)(Microsoft_up|UpdateSession|UpdateService|UpdateDevice|UpdatePlugin)")
```

→ Alerta de prioridad alta. Cubre los tres mecanismos de persistencia documentados, de 2014 a 2020.

**D-5 · ALTO — Autoextraíble que abre un documento y lanza un ejecutable, o fichero `.scr`**

```
(file.extension == "scr" AND file.origin IN ("email","download"))
OR (parent_process.name MATCHES "(?i)(7z|winrar|rar|unarchiver).*"
    AND process.executable MATCHES "(?i)\\\\(Temp|AppData|Downloads)\\\\"
    AND process.extension == "exe")
```

→ Cuarentena del fichero y alerta. **La extensión `.scr` no tiene uso legítimo moderno** y aparece en 26 de los señuelos publicados por este actor. Es una decisión de política de correo antes que una detección.

**D-6 · MEDIO — Descarga de ejecutable o comprimido desde Dropbox o Google Docs por proceso no navegador**

```
network.protocol == "https"
AND destination.domain MATCHES "(?i)(dropbox\.com|docs\.google\.com|drive\.google\.com)"
AND http.response.mime_type IN ("application/x-msdownload","application/x-rar-compressed",
                                "application/zip","application/octet-stream")
AND NOT process.name IN ("chrome.exe","msedge.exe","firefox.exe","safari.exe")
```

→ Alerta de prioridad media. Todas las URL de descarga que ESET observó estaban en esos dos servicios. **Unificar con `D-6` de `CTI-2026-022`** en una sola regla de plataforma sobre servicios legítimos de alojamiento.

**D-7 · MEDIO — Artefactos de implementación conocidos**

```
file.name IN ("jer.dll","Clip.html","finaser.aes","svchostt.exe","NisSrv.bat","_setupXOX.msi")
OR file.name MATCHES "(?i)^_(hashlbi|bsdbd|clypes|elementree|mssi|multiproccessing)\.pyw$"
OR file.path MATCHES "(?i)\\\\(MicroDes|USOEnable|Jre6)\\\\"
```

→ Contención automática. **Vida útil incierta:** son nombres publicados hace seis y siete años y basta con cambiar una cadena. Se incluyen porque su coste de implementación es una lista estática y su fidelidad, mientras duren, es total.

**D-8 · MEDIO — Geolocalización del equipo por redes Wi-Fi desde un proceso no navegador**

```
(destination.domain MATCHES "(?i)location\.services\.mozilla\.com"
 OR http.request.body CONTAINS "wifiAccessPoints")
AND NOT process.name IN ("chrome.exe","msedge.exe","firefox.exe")
```

→ Alerta de prioridad media con recolección del proceso. Técnica inusual y por tanto específica: casi nada legítimo en un parque corporativo geolocaliza el equipo a partir de las redes vecinas.

**D-9 · MEDIO — Escritura masiva a unidad extraíble**

```
event.action == "file-created"
AND file.volume.type == "removable"
AND file.extension IN ("doc","docx","xls","xlsx","ppt","pptx","pdf","odt","ods",
                       "bak","mdb","accdb","sql","shp","dwg","kml","gpx","asc","pgp","gpg")
AND count(file.path) > 50 WITHIN 10m
AND NOT process.name IN (<herramientas de respaldo aprobadas>)
```

→ Alerta de prioridad alta y, según política, bloqueo de escritura. **Es el único canal de exfiltración del actor que ninguna regla de red puede ver**, y si dispara de verdad hay alguien con acceso físico al equipo.

**D-10 · MEDIO — Acceso a claves privadas por proceso ajeno**

```
event.action IN ("file-read","file-copied")
AND (file.extension IN ("pgp","gpg","asc","key","pem","ppk")
     OR file.path MATCHES "(?i)\\\\(gnupg|\.gnupg|\.ssh)\\\\")
AND NOT process.name IN ("gpg.exe","gpg2.exe","kleopatra.exe","ssh.exe","putty.exe",
                         "pageant.exe", <clientes aprobados>)
```

→ Alerta de prioridad alta. `T1552.004` está en la ficha de MITRE para este malware, y una clave privada robada sobrevive a cualquier limpieza del equipo: es el daño más duradero que este actor produce.

**D-11 · MEDIO — Infraestructura histórica reapareciendo**

```
dns.question.name IN ("tobabean.expert","koliast.com","artyomt.com",
                      "adtiomtardecessd.zapto.org","mcsi.gotdns.ch","djcaps.gotdns.ch",
                      "tokeiss.ddns.net","lawyersofficial.mipropia.com","ceofanb18.mipropia.com",
                      "java.serveblog.net","agaliarept.com","frejabe.com",
                      "grannegral.com","plushbr.com","xmailliwx.com","blogwhereyou.com")
OR destination.ip IN ("185.224.137.63","156.67.222.88","158.69.9.209",
                      "142.44.236.215","199.79.63.188","109.61.164.33",
                      "92.249.44.53","185.70.105.33")
```

→ Alerta de prioridad crítica **por su valor de inteligencia, no por su probabilidad**: no se espera que dispare, y si lo hace es el dato que faltaba para fechar una reactivación (`I-5`). Coste de implementación: una lista estática que no hay que mantener.

**D-12 · BAJO — Tráfico FTP cifrado o túnel a servicios de exposición**

```
(destination.domain MATCHES "(?i)\\.ngrok\\.io$|\\.ngrok-free\\.app$|\\.hostingerapp\\.com$")
OR (destination.port IN (990, 989) AND source.zone == "estaciones")
```

→ Alerta de prioridad baja. Los túneles `ngrok` aparecen en los indicadores históricos del actor y son, en general, un indicio razonable de exfiltración o de acceso remoto no autorizado en una estación de trabajo.

<!-- cti:note type="warn" -->

> ⚠ **Las doce reglas están sin calibrar en nuestro entorno, y dos de ellas generarán
> ruido asegurado si se despliegan sin acotar.** `D-2` es inservible en equipos de
> desarrollo o de ciencia de datos sin la excepción por unidad organizativa, y `D-1`
> requiere inventariar primero los destinos FTP legítimos que todavía usemos —que
> probablemente sean más de los que creemos—. Publicarlas en modo alerta dos semanas y
> medir antes de poner nada en contención.

<!-- cti:note type="gap" -->

> ⬛ **Lo que no se puede detectar con lo que hay publicado.** El señuelo —un documento
> oficial auténtico, robado antes, dirigido, en el idioma y con la jerga correctos— **no
> tiene detección técnica.** `H-12` lo deja escrito y no lo resuelve. La contramedida
> realista no está en la pasarela: está en que la organización objetivo sepa que su
> documentación circula, lo que exige un canal de aviso entre instituciones que no es
> materia nuestra. Conviene decirlo para que nadie compre un producto esperando que lo
> cubra.

## X-4. Consultas de caza

```kql
// H-1 · FTP en claro desde estaciones y servidores de usuario hacia Internet
DeviceNetworkEvents
| where Timestamp > ago(180d)
| where RemotePort in (20, 21)
| where ActionType in ("ConnectionSuccess", "ConnectionAttempt")
| where not(ipv4_is_private(RemoteIP))
| summarize Conexiones = count(), Equipos = dcount(DeviceName),
            PrimeraVez = min(Timestamp), UltimaVez = max(Timestamp),
            Procesos = make_set(InitiatingProcessFileName, 10)
        by RemoteIP, RemoteUrl
| order by Conexiones desc
```

```kql
// H-2 · Intérprete de Python desde ruta escribible por el usuario
DeviceProcessEvents
| where Timestamp > ago(180d)
| where ProcessVersionInfoOriginalFileName matches regex @"(?i)^python(w)?\.exe$"
      or FileName matches regex @"(?i)^python(w)?\.exe$"
| where FolderPath matches regex @"(?i)\\(Users|AppData|Temp|ProgramData)\\"
| where not(FolderPath matches regex @"(?i)\\(Anaconda|Miniconda|Python3[0-9]|venv|\.venv)\\")
| project Timestamp, DeviceName, AccountName, FolderPath, ProcessCommandLine,
          InitiatingProcessFileName, InitiatingProcessCommandLine
| order by Timestamp desc
```

```kql
// H-3 + H-6 · Componentes con nombre de Google fuera de ruta, y persistencia asociada
let procesos = DeviceProcessEvents
    | where Timestamp > ago(180d)
    | where FileName in~ ("GoogleCrash.exe","GoogleUpdate.exe","Chrome.exe")
    | where not(FolderPath matches regex @"(?i)^C:\\Program Files( \(x86\))?\\Google\\")
    | where not(FolderPath matches regex @"(?i)\\AppData\\Local\\Google\\Chrome\\Application\\")
    | project Timestamp, DeviceName, FolderPath, FileName, Señal = "binario fuera de ruta";
let config = DeviceFileEvents
    | where Timestamp > ago(180d)
    | where FileName in~ ("jer.dll","finaser.aes","Clip.html")
    | project Timestamp, DeviceName, FolderPath, FileName, Señal = "artefacto de configuración";
let tareas = DeviceProcessEvents
    | where Timestamp > ago(180d)
    | where FileName =~ "schtasks.exe"
    | where ProcessCommandLine matches regex @"(?i)(Microsoft_up|UpdateSession|UpdateService|UpdateDevice|UpdatePlugin)"
    | project Timestamp, DeviceName, FolderPath = ProcessCommandLine,
              FileName, Señal = "tarea con nombre de actualización";
union procesos, config, tareas
| summarize Señales = make_set(Señal), Eventos = count(), Rutas = make_set(FolderPath, 10)
        by DeviceName, bin(Timestamp, 1d)
| order by array_length(Señales) desc, Eventos desc
```

```kql
// H-5 · Descarga de ejecutable o comprimido desde Dropbox o Google Docs por proceso no navegador
let navegadores = dynamic(["chrome.exe","msedge.exe","firefox.exe","iexplore.exe","brave.exe","opera.exe"]);
DeviceNetworkEvents
| where Timestamp > ago(180d)
| where RemoteUrl matches regex @"(?i)(dropbox\.com|docs\.google\.com|drive\.google\.com)"
| where not(InitiatingProcessFileName in~ (navegadores))
| project Timestamp, DeviceName, AccountName, InitiatingProcessFileName,
          InitiatingProcessCommandLine, RemoteUrl, RemoteIP
| order by Timestamp desc
```

```kql
// H-7 · Escritura masiva de documentos y ficheros GIS a unidad extraíble
let extensiones = dynamic(["doc","docx","xls","xlsx","ppt","pptx","pdf","odt","ods",
                           "bak","mdb","accdb","sql","shp","dwg","kml","kmz","gpx","asc","pgp","gpg"]);
DeviceFileEvents
| where Timestamp > ago(180d)
| where ActionType == "FileCreated"
| where FolderPath matches regex @"(?i)^[D-Z]:\\"
| extend Ext = tolower(tostring(split(FileName, ".")[-1]))
| where Ext in (extensiones)
| summarize Ficheros = count(), Tipos = make_set(Ext, 15),
            Procesos = make_set(InitiatingProcessFileName, 5)
        by DeviceName, AccountName, bin(Timestamp, 10m)
| where Ficheros > 50
| order by Ficheros desc
```

```kql
// H-13 · Retrohunt de la infraestructura histórica (2014-2020)
let dominios = dynamic(["tobabean.expert","koliast.com","artyomt.com",
                        "adtiomtardecessd.zapto.org","mcsi.gotdns.ch","djcaps.gotdns.ch",
                        "tokeiss.ddns.net","lawyersofficial.mipropia.com","ceofanb18.mipropia.com",
                        "java.serveblog.net","agaliarept.com","frejabe.com",
                        "grannegral.com","plushbr.com","xmailliwx.com","blogwhereyou.com",
                        "u929489355.hostingerapp.com","u154611594.hostingerapp.com",
                        "6e24a5fb.ngrok.io","f9527d03.ngrok.io"]);
let direcciones = dynamic(["185.224.137.63","156.67.222.88","158.69.9.209",
                           "142.44.236.215","199.79.63.188","109.61.164.33",
                           "92.249.44.53","185.70.105.33"]);
DeviceNetworkEvents
| where Timestamp > ago(365d)
| where RemoteUrl has_any (dominios) or RemoteIP in (direcciones)
| project Timestamp, DeviceName, AccountName, InitiatingProcessFileName, RemoteUrl, RemoteIP
| order by Timestamp asc
```

```yaml
# Sigma — FTP en claro desde estación de trabajo hacia Internet
# Autor: Célula CTI · Fecha: 2026-11-16 · ATT&CK: T1071.002, T1041
# Nivel: high · Estado: estable
# Esta regla NO depende de ningún indicador y por tanto no caduca. Es la única
# detección de este informe que sobrevive a un cambio completo de arsenal.
title: FTP sin cifrar desde segmento de usuario hacia Internet
id: 2026-023-ftp-claro-saliente
status: stable
description: >
  Conexión saliente a los puertos 20 o 21 desde una estación de trabajo o un servidor
  de usuario. Es el canal de exfiltración principal del actor Machete en 2014, 2019 y
  2020, y de muchos otros. Requiere inventariar primero los destinos FTP legítimos.
logsource:
  category: firewall
detection:
  ftp:
    dst_port:
      - 20
      - 21
  interno:
    src_zone:
      - 'estaciones'
      - 'servidores-usuario'
  filtro_aprobados:
    dst_ip: '%DESTINOS_FTP_APROBADOS%'
  condition: ftp and interno and not filtro_aprobados
falsepositives:
  - Transferencias con proveedores que aún no soportan SFTP o FTPS
  - Equipos de laboratorio y dispositivos industriales antiguos
level: high
tags:
  - attack.command_and_control
  - attack.t1071.002
  - attack.exfiltration
  - attack.t1041
```

```yaml
# Sigma — Intérprete de Python ejecutado desde ruta escribible por el usuario
# Autor: Célula CTI · Fecha: 2026-11-16 · ATT&CK: T1059.006, T1036.005
# Nivel: medium · Estado: experimental
# Falsos positivos masivos en equipos de desarrollo y de ciencia de datos:
# acotar por unidad organizativa ANTES de desplegar.
title: Python ejecutándose desde ruta de perfil de usuario
id: 2026-023-python-ruta-usuario
status: experimental
description: >
  Intérprete de Python ejecutado desde %AppData%, %Temp%, %ProgramData% o el perfil del
  usuario. Es la firma de la familia Machete desde 2010, cuyos componentes se distribuyen
  como Python empaquetado o como scripts con un intérprete 2.7 original.
logsource:
  category: process_creation
  product: windows
detection:
  interprete:
    - OriginalFileName:
        - 'python.exe'
        - 'pythonw.exe'
    - Image|endswith:
        - '\python.exe'
        - '\pythonw.exe'
  ruta_usuario:
    Image|contains:
      - '\Users\'
      - '\AppData\'
      - '\Temp\'
      - '\ProgramData\'
  filtro_entornos:
    Image|contains:
      - '\Anaconda'
      - '\Miniconda'
      - '\venv\'
      - '\.venv\'
      - '\Python3'
  condition: interprete and ruta_usuario and not filtro_entornos
falsepositives:
  - Entornos virtuales de desarrollo
  - Herramientas internas empaquetadas con Python
level: medium
tags:
  - attack.execution
  - attack.t1059.006
  - attack.defense_evasion
  - attack.t1036.005
```

## X-5. Mitigaciones de configuración con efecto directo

| Control | Corta |
|---|---|
| **Bloqueo de FTP saliente en claro desde segmentos de usuario**, con excepciones nominales e inventariadas | **El canal de exfiltración principal del actor en doce años** (`T1071.002`), y el de cualquier otra amenaza que lo use. Es el control de mejor retorno del informe |
| Bloqueo de adjuntos `.scr`, `.jar`, `.exe` y autoextraíbles comprimidos en la pasarela | La etapa 01 en su variante de adjunto: 26 de los señuelos publicados usan `.scr` |
| Lista de permitidos de aplicaciones que excluya intérpretes desde rutas de perfil de usuario | El ejecutor del implante en todas las versiones documentadas (`T1059.006`) |
| Proxy con atribución de proceso y control de descarga de ejecutables desde servicios de almacenamiento | La etapa 02: todas las URL de descarga observadas estaban en Dropbox o Google Docs (`T1102`) |
| Directiva de dispositivos extraíbles: bloqueo de escritura, o cifrado obligatorio y registro | **El canal de exfiltración que ninguna regla de red ve** (`T1052.001`) |
| Cifrado en reposo de ficheros cartográficos, GIS y de documentación técnica, con control de acceso por necesidad | El botín característico del actor (`T1005`). Requiere el inventario de `X-9`, que no existe |
| Claves privadas en almacén protegido por hardware, nunca en ficheros del perfil del usuario | La captura de claves PGP (`T1552.004`), que es el daño más duradero que este actor produce |
| Registro de conexiones salientes por protocolo con 180 días de retención | No corta nada: **habilita** `D-1`, `D-6`, `D-8`, `D-11` y `D-12`, es decir cinco de las doce reglas |
| Registro de línea de comandos y de creación de procesos con 180 días de retención | No corta nada: **habilita** `D-2` a `D-5` y hace significativo el retrohunt de la decisión `E-a` |
| Deshabilitar el gestor de contraseñas del navegador por directiva para credenciales corporativas | La recuperación de perfiles de navegador (`T1555.003`) |
| Procedimiento de respuesta ante sospecha de espionaje, distinto del de ransomware | No corta la intrusión: **evita que nuestra propia respuesta destruya la evidencia y avise al adversario.** Es la decisión `E-h` |
| Archivo local de los informes de proveedor de los que dependen nuestros productos | No corta nada: conserva la trazabilidad de nuestros propios juicios. Ya hemos perdido una fuente primaria (§E-3) |

---

## 14. Brechas de inteligencia y nuevos requisitos de colección

| # | Brecha | Impacto en el juicio | Requisito propuesto | Prioridad |
|---|---|---|---|---|
| G-1 | **No hay información pública sobre la actividad de este actor después de septiembre de 2020** | Es la brecha que define el producto. `KJ-4` queda con confianza baja y todo el nivel técnico queda marcado como histórico. No sabemos si estamos describiendo una amenaza o una pieza de museo | Vigilancia permanente del indicador `I-1`; consulta a los proveedores contratados sobre actividad reciente del grupo `G0095`; evaluación de cobertura comercial específicamente regional (decisión `E-g`) | Crítica |
| G-2 | **Una de las cuatro fuentes primarias ya no es accesible**, y es la de las cifras de volumen más citadas | Las cifras de ~300 víctimas y >100 GB quedan sin procedencia verificable y se citan aquí con esa salvedad | Política de archivo local de fuentes con fecha de captura (decisión `E-e`); búsqueda de una copia conservada del informe de 2017 | Alta |
| G-3 | **El documento técnico de ESET de 2019 no pudo leerse** en su versión completa | El desglose de victimología por país proviene de la nota de prensa y del blog en español del mismo proveedor, no del documento técnico; la tabla ATT&CK original usa numeración obsoleta que hemos traducido | Obtener el PDF por otra vía o solicitarlo al proveedor; verificar el desglose 75/16/7/2 contra el documento | Media |
| G-4 | Sin telemetría propia ni retrohunt ejecutado | §O-4 vacía; las doce reglas de §X-3 sin calibrar; no sabemos si alguno de los indicadores históricos aparece en nuestros registros | Ejecutar el cuestionario X-1 a X-11 de §O-4, empezando por X-1 y X-2 (decisión `E-a`) | Crítica |
| G-5 | **Sin inventario de ficheros GIS, cartográficos y de documentación técnica** | `H-10` no se puede escribir, `E-f` no se puede priorizar y `KJ-7` no se puede evaluar. No es brecha de telemetría: es de gobierno de la información | Inventario de información dirigido, pregunta `X-9`, con Riesgo y TI | Alta |
| G-6 | **Sin revisión de la cartera de contratos frente al perfil de víctima de este actor** | `KJ-7` queda sin evaluar, y es el juicio que determina si este informe nos aplica o no | Revisión de cartera con Dirección de Contratos y Riesgo (decisión `E-c`) | Alta |
| G-7 | Las cifras de victimología de las distintas fuentes no son comparables entre sí, y el estudio académico lo declara | Cualquier serie temporal de víctimas que construyamos con estas fuentes será artificial. Por eso §E-2 las presenta por separado y no las promedia | No intentar la serie. Si se necesita tendencia, pedirla a un proveedor con telemetría continua | Media |
| G-8 | El componente para Android y los preparativos para macOS y Unix que Kaspersky describió en 2014 no los confirma ninguna fuente posterior | Si existieran y siguieran vivos, toda la detección de este informe —que es de Windows— quedaría parcialmente fuera de juego | Buscar corroboración; añadir a la petición de colección a proveedores | Media |
| G-9 | No hay procedimiento de respuesta ante sospecha de espionaje | Si `D-1` o `D-2` disparan de verdad, la respuesta estándar de ransomware destruiría la evidencia y avisaría al adversario | Redacción del procedimiento con el CISO (decisión `E-h`) | Alta |
| G-10 | Sin canal establecido con el CSIRT Nacional para preguntar por actividad regional de este tipo | Las cuatro fuentes son comerciales y académicas; ninguna es gubernamental. En `CTI-2026-021` la inteligencia más pertinente era precisamente la del CERT nacional | Consulta formal al CSIRT Nacional sobre actividad de espionaje documentada contra instituciones chilenas, con el perfil de este actor como referencia | Alta |

---

# ANEXOS

## Anexo A — Indicadores de compromiso

<!-- cti:note type="warn" -->

> ⚠ **Leer antes de usar, y aquí la advertencia principal es una sola y es grande: todos
> estos indicadores son de 2014 a 2020.** El más reciente tiene seis años. **No sirven para
> prevenir nada.** Sirven para exactamente dos cosas: el retrohunt de la decisión `E-a`, y
> la vigilancia de reaparición del indicador `I-5`. Un resultado negativo con esta lista
> **no significa que no estemos comprometidos**: significa que no lo estamos con los
> artefactos que un proveedor publicó hace seis años. Dos advertencias menores: el
> repositorio de indicadores de ESET publica sus hashes **sin asociarlos a nombre de
> fichero** en los ficheros de lista, de modo que la correspondencia hash-fichero que aquí
> aparece procede del documento de texto del mismo repositorio; y el evento MISP de ese
> repositorio está marcado como **no publicado**, por lo que sus atributos adicionales no
> se recogen aquí.

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Acción permitida |
|---|---|---|---|---|
| sha1 | `048c40eb606da3def08c9f6997c1948afbbc959b` | `GoogleUpdate.exe` — componente de mando y control, `Python/Machete.F` (ESET, jul-2019) | Alta | Solo retrohunt |
| sha1 | `2e8d8508096caa38493414f6ba788d0041ea9e15` | `GoogleUpdate.exe` — `Python/Machete.F` | Alta | Solo retrohunt |
| sha1 | `85bdd7d871108c737701ac30c14a2d343cbdef94` | `GoogleUpdate.exe` — `Python/Machete.D` | Alta | Solo retrohunt |
| sha1 | `8ed8cb784512f7dadd147347fc94e945faf16338` | `GoogleUpdate.exe` — `Python/Machete.F` | Alta | Solo retrohunt |
| sha1 | `9c413075aab7ef7876b8dc8d7b7c1b9b96842c6e` | `GoogleUpdate.exe` — `Python/Machete.A` | Alta | Solo retrohunt |
| sha1 | `ab8dd6b0cc950618589603012863b57f7adb9d9b` | `GoogleUpdate.exe` — `Python/Machete.A` | Alta | Solo retrohunt |
| sha1 | `318496b58cf5052efd49a95c721d9165278e9fce` | `Chrome.exe` — componente de recolección, `Python/Machete.B` | Alta | Solo retrohunt |
| sha1 | `3bb345032b6d0226d6771ba65fe4da0faf628631` | `Chrome.exe` — `Python/Machete.B` | Alta | Solo retrohunt |
| sha1 | `946a24dfbd0ae94209ef7c284d3f462548566a3c` | `Chrome.exe` — `Python/Machete.B` | Alta | Solo retrohunt |
| sha1 | `984b9202a6dbd7d3dd696cae1220338a68092dc9` | `Chrome.exe` — `Python/Machete.B` | Alta | Solo retrohunt |
| sha1 | `eabd45d0a86113f5ccff9fd292c1e482a5727815` | `Chrome.exe` — `Python/Machete.B` | Alta | Solo retrohunt |
| sha1 | `f05bc018c90b560dc4932758956adffbc10588ce` | `Chrome.exe` — `Python/Machete.B` | Alta | Solo retrohunt |
| sha1 | `204a2850548e5994d4696e9002f90dfccbe2093a` | `GoogleCrash.exe` — componente principal y persistencia, `Python/Machete.C` | Alta | Solo retrohunt |
| sha1 | `3792588edc809270e6666a4677ec85a3400ba4cf` | `GoogleCrash.exe` — `Python/Machete.E` | Alta | Solo retrohunt |
| sha1 | `4899a2c2ceceb92d2cc4ed17d092d1d599379284` | `GoogleCrash.exe` — `Python/Machete.A` | Alta | Solo retrohunt |
| sha1 | `a42756280aa352f4612bed85aabf7f3267e676c2` | `GoogleCrash.exe` — `Python/Machete.E` | Alta | Solo retrohunt |
| sha1 | `a97cf05ad7f3102bde45e4b4947ed435efea1968` | `GoogleCrash.exe` — `Python/Machete.E` | Alta | Solo retrohunt |
| sha1 | `2b7404f6b0075bc1192d61d4af135d521d5f08a3` | `RdrCEF.exe` — descargador, `Python/Machete.A` | Alta | Solo retrohunt |
| sha1 | `53102e57b40feacb64566c26d101d9242dece77c` | `Down.exe` — descargador, `Python/Machete.A` | Alta | Solo retrohunt |
| sha1 | `56e8743e0773286a4b9e055147d96d53a43beca1` | `Down.exe` — descargador, `Python/Machete.A` | Alta | Solo retrohunt |
| sha1 | `71f69f04307c8f5675dcadeaa80b8c2b95691b01` | `Down.exe` — descargador, `Python/Machete.A` | Alta | Solo retrohunt |
| sha1 | `904137b61f1ded66c8ca76ebf198dec1b638b5d4` | `Down.exe` — descargador, `Python/Machete.A` | Alta | Solo retrohunt |
| sha1 | `fbb485b40477f5a014e7096747b1b4a494ce50ef` | `Down.exe` — descargador, `Python/Machete.A` | Alta | Solo retrohunt |
| sha1 | `1b3723651e1d321d4f34f2a243d7751d17288257` | `_hashlbi.pyw` — componente en Python, `Python/Machete.G` | Alta | Solo retrohunt |
| sha1 | `0c33b75f6c4fc0413abdbcda1c5e18c907f13dc3` | `_bsdbd.pyw` — componente en Python, `Python/Machete.G` | Alta | Solo retrohunt |
| sha1 | `26fb301af7393b5e564b8c802f5795edebd7cecf` | `_clypes.pyw` — componente en Python, `Python/Machete.G` | Alta | Solo retrohunt |
| sha1 | `07e383e9ff04f587769845306dc4bfe75630baaa` | `_elementree.pyw` — componente en Python, `Python/Machete.G` | Alta | Solo retrohunt |
| sha1 | `6b42091ca2f89a59f4e27e30acdacf32eb83f824` | `_mssi.pyw` — componente en Python, `Python/Machete.G` | Alta | Solo retrohunt |
| sha1 | `0b6f61af3e2c6551f15e0f888177eec91f20ba99` | `_multiproccessing.pyw` — componente en Python, `Python/Machete.G` | Alta | Solo retrohunt |
| sha1 | `10eb152039cb0a379daab272151bc1baa8c6d4db` | `Radiograma 004026_pdf.scr` — **señuelo con documento de comunicación militar venezolana** | Alta | Solo retrohunt |
| sha1 | `a94916f9696d861fe040891634b3f2da09557f13` | `REPORTE OPERACIONAL 10JUN19 pdf.scr` — señuelo militar | Alta | Solo retrohunt |
| sha1 | `0468d3776435e527dba52b9da61d38c076dda09a` | `FORMATO UNICO DE RENDIMIENTO OPERATIVO GNB 11JUNIO2019 CZGNB-13 xlsx.scr` — señuelo de la Guardia Nacional Bolivariana | Alta | Solo retrohunt |
| sha1 | `9d65b55168526161a79f4743a37b1a7358c67037` | `INSTRUCCIONES DEL JSO 08JUN19 docx.scr` — señuelo militar | Alta | Solo retrohunt |
| sha1 | `52b680f472ae463436979da325db7ad64d5af1ef` | `Mapa_monitoreo_WRF_ind02052018.scr` — **señuelo cartográfico**, el único de la serie que anticipa el interés GIS | Alta | Solo retrohunt |
| sha1 | `fb871aaca0ddcf2f009a2d11ecf672cfb61b7357` | `CALENDARIO_ACTIVIDADES_COLCO_EC.scr` — señuelo con referencia a Ecuador | Alta | Solo retrohunt |
| sha1 | `c39b9d966aed0372619b3989995ab9ad12f94d38` | `NOTA_CICR_00079.scr` — **señuelo diplomático que invoca al Comité Internacional de la Cruz Roja** | Alta | Solo retrohunt |
| sha1 | `7a1ad75a1aa73ec72ee21b213fcca55d57a0cd58` | `S_E_ARLETTE_MARENCO_NOTA_INFORMANDO_TERMINO_DE_MISION_001.scr` — señuelo diplomático con nombre propio | Alta | Solo retrohunt |
| sha1 | `9ea7832d83c74c839a49580b4211e627a24571be` | `Programa Formacion en Contratacion Publica.scr` — **señuelo de contratación pública**, el de perfil más transferible a una empresa | Alta | Solo retrohunt |
| sha1 | `5c56ac14ca7159804a9d53fe037cfd0d99d45ab1` | `JUNIO_19_PROPUESTA_CLARO_RENOVACION.scr` — señuelo de propuesta comercial a un operador de telecomunicaciones | Alta | Solo retrohunt |
| sha1 | `9e52e1c015b97d4fb2cac888f8fc69d729af78f5` | `finaser.aes` — fichero de configuración cifrada | Alta | Solo retrohunt |
| sha1 | `fd52b10e9d4e5d343e589627444a6766357d5e47` | `Security.exe` — autoextraíble con los componentes | Alta | Solo retrohunt |
| sha1 | `24752dab28c3add4c31591f2ec480ce3ca83e0aa` | `python27.exe` — autoextraíble con intérprete y componentes | Alta | Solo retrohunt |
| md5 | `61d33dc5b257a18eb6514e473c1495fe` | `AwgXuBV31pGV.eXe` — artefacto de infección (Kaspersky, 2014) | Media | Solo retrohunt |
| md5 | `b5ada760476ba9a815ca56f12a11d557` | `EL ARTE DE LA GUERRA.exe` — señuelo de 2014 | Media | Solo retrohunt |
| md5 | `d6c112d951cb48cab37e5d7ebed2420b` | `Hermosa XXX.rar` — señuelo de temática sexual (2014) | Media | Solo retrohunt |
| md5 | `df2889df7ac209e7b696733aa6b52af5` | `Hermosa XXX.pps.rar` — señuelo con presentación de PowerPoint (2014) | Media | Solo retrohunt |
| md5 | `e486eddffd13bed33e68d6d8d4052270` | `Hermosa XXX.pps.rar` — segunda muestra del mismo señuelo | Media | Solo retrohunt |
| md5 | `e9b2499b92279669a09fef798af7f45b` | `Suntzu.rar` — señuelo de 2014 | Media | Solo retrohunt |
| md5 | `f7e23b876fc887052ac8e2558f0d6c38` | `Hot Brazilian XXX.rar` — señuelo de 2014 | Media | Solo retrohunt |
| md5 | `b26d1aec219ce45b2e80769368310471` | `Signed_Update.jar` — artefacto Java de infección por web (2014) | Media | Solo retrohunt |
| md5 | `fbe5b66db57fb52b231c5374ac2ac805` | Componente de la campaña `HpReact` (360, sep-2020). **Es uno de los artefactos más recientes publicados de este actor** | Alta | Solo retrohunt |
| md5 | `6b33fa0c52ca413d4214dcde007f89c1` | Componente de la campaña `HpReact` (360, sep-2020) | Alta | Solo retrohunt |
| md5 | `f85489c1d1ff3374f92ccb7267032016` | Componente de la campaña `HpReact` (360, sep-2020) | Alta | Solo retrohunt |
| domain | `tobabean[.]expert` | Servidor FTP de exfiltración (ESET, 2019) | Alta | Bloqueo y retrohunt |
| domain | `koliast[.]com` | Servidor FTP de exfiltración (ESET, 2019) | Alta | Bloqueo y retrohunt |
| domain | `artyomt[.]com` | Servidor de mando y control, ruta `/file3.php` (ESET, 2019) | Alta | Bloqueo y retrohunt |
| domain | `adtiomtardecessd[.]zapto[.]org` | Mando y control sobre DNS dinámico (ESET, 2019) | Alta | Bloqueo y retrohunt |
| domain | `mcsi[.]gotdns[.]ch` · `djcaps[.]gotdns[.]ch` · `tokeiss[.]ddns[.]net` | Mando y control sobre DNS dinámico (ESET, 2019) | Alta | Bloqueo y retrohunt |
| domain | `ceofanb18[.]mipropia[.]com` | **Mando y control cuyo nombre suplanta a la Fuerza Armada Nacional Bolivariana.** Es el indicador que mejor resume el conjunto de objetivos del actor | Alta | Bloqueo y retrohunt |
| domain | `lawyersofficial[.]mipropia[.]com` | Mando y control con nombre de apariencia jurídica, coherente con los señuelos de citación judicial | Alta | Bloqueo y retrohunt |
| domain | `u929489355[.]hostingerapp[.]com` · `u154611594[.]hostingerapp[.]com` | Mando y control en alojamiento compartido gratuito, ruta `/file.php` | Alta | Bloqueo y retrohunt |
| domain | `6e24a5fb[.]ngrok[.]io` · `f9527d03[.]ngrok[.]io` | **Túneles `ngrok` usados como mando y control**, ruta `/file.php`. Los subdominios caducan; el patrón de abuso no | Alta | Detección |
| domain | `java[.]serveblog[.]net` | Infraestructura de 2014 (Kaspersky), origen de `Signed_Update.jar` | Media | Bloqueo y retrohunt |
| domain | `agaliarept[.]com` · `frejabe[.]com` · `plushbr[.]com` · `xmailliwx[.]com` | Infraestructura de 2014 (Kaspersky). Toda comunicación con ellos es, en palabras de la fuente, «extremadamente sospechosa» | Media | Bloqueo y retrohunt |
| domain | `grannegral[.]com` · `blogwhereyou[.]com` | Infraestructura de 2014 **sumidero por Kaspersky**: una resolución hoy no indica compromiso activo | Media | Solo detección |
| url | `hxxp://artyomt[.]com/file3[.]php` · `hxxp://koliast[.]com/file[.]php` · `hxxp://tobabean[.]expert/file[.]php` | Rutas de mando y control observadas. **El patrón `/file.php` es más útil que el dominio** | Alta | Detección |
| ipv4 | `185.224.137.63` | Servidor de exfiltración (ESET, 2019) | Alta | Solo retrohunt |
| ipv4 | `156.67.222.88` | Servidor de exfiltración (ESET, 2019) | Alta | Solo retrohunt |
| ipv4 | `158.69.9.209` | Servidor de exfiltración (ESET, 2019) | Alta | Solo retrohunt |
| ipv4 | `142.44.236.215` | Servidor de exfiltración (ESET, 2019) | Alta | Solo retrohunt |
| ipv4 | `199.79.63.188` | Servidor de exfiltración (ESET, 2019) | Alta | Solo retrohunt |
| ipv4 | `109.61.164.33` | Servidor de exfiltración (ESET, 2019) | Alta | Solo retrohunt |
| ipv4 | `92.249.44.53` | Infraestructura de la campaña `HpReact` (360, sep-2020) | Alta | Solo retrohunt |
| ipv4 | `185.70.105.33` | Infraestructura de la campaña `HpReact` (360, sep-2020) | Alta | Solo retrohunt |
| ruta | `appdata/MicroDes/` · `appdata/Jre6/java.exe` · `Java Update.lnk` | Instalación y persistencia de la versión de 2014 (Kaspersky) | Media | Detección |
| ruta | `%ProgramData%\USOEnable` · `svchostt.exe` · `NisSrv.bat` · `_setupXOX.msi` | Instalación y persistencia de la versión de 2020 (360) | Alta | Detección |
| ruta | `C:\Users\MITM\Desktop\malware\3_svchostt\Proyecto1.vbp` | **Ruta de compilación del liberador de 2020**, con el nombre de usuario del desarrollador | Alta | Detección |
| mutex | `Microsoft_up` | Nombre de la tarea programada de persistencia (2014) | Media | Detección |
| mutex | `Clip.html` | Fichero donde se almacena el portapapeles capturado (estudio académico) | Media | Detección |

## Anexo B — Fuentes y valoración

> Valoración doble tipo Admiralty/OTAN: **fiabilidad de la fuente (A–F)** ×
> **credibilidad de la información (1–6)**. Se valoran por separado.

| Fuente | Disciplina | Fiabilidad | Credibilidad | Notas de sesgo |
|---|---|---|---|---|
| ESET — repositorio público de indicadores `eset/malware-ioc`, carpeta `machete` (evento del 29-jul-2019) | OSINT comercial / TECHINT | B | 1 | **La mejor fuente de indicadores del informe y la única leída en su integridad:** más de doscientos hashes en tres ficheros, 14 dominios, 6 direcciones, correspondencia hash-componente y nombres de señuelo. **Salvedades:** el evento MISP está marcado como **no publicado**, lo que sugiere que no pasó revisión de difusión; los ficheros de lista no asocian hash a fichero; y el enlace al documento técnico que contiene ya no funciona |
| ESET — «Sharpening the Machete» (5-ago-2019) | OSINT comercial / TECHINT | B | 1 | **El análisis técnico de referencia sobre la versión moderna:** componentes, ofuscación, canal FTP, lista de ficheros objetivo con los GIS, geolocalización por Wi-Fi, y la observación del documento clasificado usado como señuelo el mismo día. **No publica indicadores en el cuerpo** —remite al repositorio— y su tabla ATT&CK usa numeración obsoleta. El desglose por país completo **no está en este artículo** (§3.3) |
| Civilsphere Project / Virus Bulletin 2019 — «A Study of Machete Cyber Espionage Operations in Latin America», Valeros, Rigaki, Garcia y Babayeva | Académica / TECHINT | B | 1 | **La fuente metodológicamente más sólida y la única no comercial:** 105 muestras de 2011 a 2019, 63 señuelos, corpus y método declarados, hallazgos propios —tres claves AES compartidas, 14 dominios FTP, FTP sin cifrar, rutas con topónimos colombianos, propagación por USB—. **Es también la única que declara no haber podido reproducir las cifras de victimología de los informes anteriores**, lo que es una virtud y a la vez una advertencia sobre todas las demás. No da cifra de víctimas ni desglose legible por país |
| Kaspersky GReAT — «El Machete» (20-ago-2014) | OSINT comercial / TECHINT | B | 2 | **El informe fundacional:** los siete países de víctimas, los perfiles de alto nivel, el implante en Python, los dominios, los artefactos de host y las capacidades. Doce años de antigüedad: su descripción del arsenal está superada y sus artefactos de host conservan valor de retrohunt. **No da cifra total de víctimas en el artículo técnico**, a diferencia de lo que circula atribuido a esta fuente (§3.3). El componente Android y los preparativos para macOS y Unix que describe **no los confirma nadie después** |
| 360 Baize Lab — «APT-C-43 steals Venezuelan military secrets… HpReact campaign» (25-sep-2020) | OSINT comercial / TECHINT | C | 3 | **El informe más reciente de primera mano que existe sobre este actor**, y por eso insustituible. Aporta el `MSI` disfrazado de Adobe Acrobat Reader, los cinco módulos y tres MD5 con dos direcciones. **Salvedades fuertes:** firma solo con un nombre de pila, no publica tabla ATT&CK ni nombres de tarea ni dominios de C2, buena parte del detalle está en pies de figura, y **declara expresamente como conjetura** su atribución de intención política —«suponemos»—. Proveedor con marco geopolítico propio: su lectura del conflicto venezolano debe leerse como lo que es |
| Cylance — «El Machete's Malware Attacks Cut Through LATAM» (22-mar-2017) | OSINT comercial | F | 4 | **No evaluable: el artículo ya no se sirve.** Su dirección original redirige al índice del blog de la empresa que adquirió al proveedor. Las cifras de ~300 víctimas, >100 GB y la lista de dieciocho países provienen de **coberturas de prensa especializada que lo citaron cuando era accesible** (Infosecurity Magazine, BetaNews, SecurityWeek), y aquí van siempre marcadas. **MITRE sigue citándolo como referencia del grupo `G0095`.** La valoración F/4 no juzga el trabajo de Cylance: dice que no hemos podido verlo y que las cifras llegan de tercera mano |
| MITRE ATT&CK — grupo `G0095` y malware `S0409`, versión 2.0 del 31-jul-2026 | Marco de referencia | A | 1 | Usado para nombrar técnicas, para construir §T-2 y para traducir la numeración obsoleta del artículo de ESET. **Su actualización de julio de 2026 es revisión de mapeo, no actividad nueva**, y sus cuatro referencias siguen siendo las de 2014 a 2020 —una de ellas ya inaccesible—. Reconoce como contribuyente a un investigador de ESET, lo que explica la densidad de detalle de 2019 |
| Comprobación propia de ausencia de informes de primera mano posteriores a 2020, 16-nov-2026 | Análisis propio / OSINT | B | 3 | **Hallazgo negativo y central del producto** (`KJ-4`). La ausencia de publicación no prueba la ausencia de actividad, y el informe se construye precisamente sobre esa ambigüedad en lugar de resolverla a conveniencia |

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

## Anexo D — Quién encaja en el perfil de víctima, y quién es proveedor de quien encaja

> Este anexo existe para alimentar la decisión `E-c` y la pregunta `X-8`. La columna
> izquierda es **victimología documentada** por las fuentes. La derecha es **nuestra
> traducción al contexto chileno** y no está observada en ninguna campaña: no es una lista
> de víctimas ni de amenazas, es la lista de los perfiles por los que este actor mostró
> interés durante doce años, para que Contratos y Riesgo puedan decir si estamos cerca de
> alguno.

| Perfil de víctima documentado | Fuente | Perfil equivalente en Chile | Nuestra relación posible |
|---|---|---|---|
| Fuerzas militares (Venezuela, Ecuador) | Kaspersky, Cylance, ESET, 360 | Ejército, Armada, Fuerza Aérea, Estado Mayor Conjunto | Proveedor de TI, de cartografía, de logística, de obra, de telecomunicaciones |
| Guardia Nacional y policía | ESET (señuelos de la GNB) | Carabineros, PDI | Proveedor de sistemas, de formación, de equipamiento |
| Ministerios de relaciones exteriores y embajadas | Kaspersky, ESET | Cancillería, misiones diplomáticas, consulados | Proveedor de TI, traducción, logística, seguridad física |
| Servicios de inteligencia | Kaspersky | ANI y equivalentes | Improbable como proveedor directo; relevante como subcontratista de segundo nivel |
| Instituciones de gobierno en general | las cuatro fuentes | Ministerios, subsecretarías, servicios públicos | Amplio: cualquier contrato de TI o de consultoría con el Estado |
| Educación | ESET (2019) | Universidades con convenios de defensa o investigación dual | Colaboración académica, proyectos conjuntos |
| **Productores y custodios de cartografía y datos geoespaciales** | ESET (ficheros GIS con cuadrícula militar) | Instituto Geográfico Militar, SHOA, catastro, concesionarias de infraestructura, mineras con cartografía de detalle | **El perfil más directamente transferible a una empresa privada** |
| Operadores de telecomunicaciones | ESET (señuelo de propuesta comercial a un operador) | Operadores nacionales y sus proveedores | Proveedor, cliente o competidor en licitación |
| Organismos internacionales y humanitarios | ESET (señuelo que invoca al CICR) | Oficinas regionales de organismos internacionales | Proveedor de servicios |
| **Participantes en contratación pública** | ESET (señuelo «Programa Formación en Contratación Pública») | Cualquier empresa que licite con el Estado | **Directo: somos este perfil si licitamos** |

## Anexo E — Marcos de referencia empleados

`MITRE ATT&CK v18` · `MITRE D3FEND` · `Cyber Kill Chain` · `Pirámide del Dolor` ·
`Modelo del Diamante` · `F3EAD` · `ICD 203` (lenguaje estimativo) · `ACH, supuestos
clave, pre-mortem` · `TLP 2.0` · `PAP` · `STIX 2.1 / TAXII 2.1` · `Admiralty Code`

## Anexo F — Paquete legible por máquina

- Bundle STIX 2.1: pendiente de generar. Debe modelar **un `intrusion-set` con sus cuatro alias** (`Machete`, `El Machete`, `APT-C-43`, `G0095`) y, por separado, **los objetos `malware`** correspondientes al implante (`S0409` y el `Pyark` de 360), porque la confusión entre el nombre del actor y el del malware es el primer error de tradecraft que §O-1 advierte.
- **Todos los `indicator` deben llevar `valid_until` vencido y una propiedad explícita de uso «solo retrohunt»**, y la descripción del bundle debe decir en su primera línea que los indicadores son de 2014 a 2020. Es la primera vez en esta serie que un paquete de indicadores entero está caducado por diseño, y publicarlo sin esa marca invitaría a tratarlo como lista de bloqueo vigente.
- Los dos dominios **sumideros por Kaspersky** (`grannegral.com`, `blogwhereyou.com`) deben llevar marca propia: una resolución contra ellos no indica compromiso activo.
- Evento MISP: pendiente. Taxonomías: `tlp`, `pap`, `admiralty-scale`, `estimative-language`, más etiquetas propias `espionaje:regional`, `vigencia:histórico` y `canal:ftp-claro`. **Advertencia de procedencia:** el evento MISP del repositorio de ESET está marcado como no publicado y no debe reutilizarse sin revisarlo.
- Reglas: las dos reglas Sigma de §X-4 y las doce plantillas de §X-3, versionadas con el identificador `CTI-2026-023`. **La regla del FTP en claro se marca `stable` y las demás `experimental`**, porque es la única que no depende del arsenal descrito.
- **Petición de colección formal**, que es la mitad del valor de este producto: solicitud a los proveedores contratados de cualquier telemetría o informe sobre actividad del grupo `G0095` posterior a septiembre de 2020, y consulta al CSIRT Nacional conforme a la brecha `G-10`.

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-11-16 | Emisión inicial. Elaborado sobre tres informes de proveedor de primera mano, un estudio académico con 105 muestras y el repositorio público de indicadores de ESET. **El producto está estructurado alrededor de una ausencia: no hay información pública sobre este actor después de septiembre de 2020**, y eso se declara en `KJ-4`, en §E-3, en la advertencia que abre el nivel técnico y en la brecha `G-1`. **Chile no aparece en ninguna de las cuatro fuentes**, lo que se trata como hallazgo (`KJ-3`, `H4`) y no como omisión. Una de las cuatro fuentes primarias —el informe de Cylance de 2017, que MITRE sigue citando— **ya no es accesible en su dirección original**, lo que motiva la decisión `E-e` sobre archivo local de fuentes. Caducidad fijada a seis meses en lugar de tres, por tratarse de una amenaza sin movimiento observable. Sin telemetría propia: §O-4 sin evaluar | Célula CTI |

## Anexo H — Realimentación del consumidor

| Pregunta | Respuesta |
|---|---|
| ¿Respondió a su requisito? | |
| ¿Qué decisión tomó o cambió con este informe? | |
| ¿Se ejecutó el retrohunt (E-a)? ¿Con qué resultado, y quedó registrado el negativo? | |
| ¿Se desplegó la detección de FTP en claro (E-b)? ¿Cuántos destinos FTP legítimos había que inventariar? | |
| ¿Se hizo la revisión de cartera de contratos (E-c)? ¿Encaja alguno en el Anexo D? | |
| ¿Existe ya un inventario de ficheros GIS y cartográficos (X-9)? | |
| ¿Se redactó el procedimiento de respuesta ante sospecha de espionaje (E-h)? | |
| ¿Apareció algún informe de primera mano posterior a 2020 (I-1)? | |
