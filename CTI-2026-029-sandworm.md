---
tlp: "TLP:CLEAR"
pap: "PAP:AMBER"
id: "CTI-2026-029"
version: "1.1"
tipo: "Perfil de actor"
foco_regional: "Ucrania · Polonia · Latinoamérica"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "Sandworm · APT44 · Seashell Blizzard · TeleBots · G0034"
fecha: "2026-11-17"
caduca: "2027-02-17"
autor: "Célula CTI"
distribucion: "Elaborado íntegramente con fuentes abiertas TLP:CLEAR: los informes trimestrales y las notas de prensa de investigación de ESET (mayo de 2025, Q2–Q3 2025 y Q2–Q3 2026), el análisis de Microsoft sobre el subgrupo BadPilot (febrero de 2025), la ficha G0034 de MITRE ATT&CK, una acusación federal estadounidense de 2020 y fuentes de proveedor adicionales. Difusión libre, conservando la atribución de las fuentes y las salvedades metodológicas de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-029

## El actor cuya pregunta no es «¿qué nos robarían?» sino «¿podríamos volver a operar?»

### Distribuye sus borradores de datos por directiva de grupo de Active Directory, el mismo mecanismo con que administramos el parque

> **Regla de oro del producto:** todo párrafo debe responder a un requisito de
> inteligencia (PIR) y habilitar una decisión. Si un párrafo no cambia lo que
> alguien va a hacer, va al anexo o se borra.

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-029` |
| Versión / fecha | `1.1` — 2026-11-21 |
| Tipo de producto | Perfil de actor destructivo más **evaluación de recuperabilidad**. La segunda mitad es lo que distingue este informe de los cinco anteriores de la cartera: contra un actor que destruye, las preguntas útiles son de continuidad y de respaldo, no de detección |
| Niveles cubiertos | Estratégico · Operacional · Táctico · Técnico |
| Foco regional | **Sin víctimas latinoamericanas documentadas.** El informe se escribe por dos razones concretas: su **vector de distribución es la directiva de grupo de Active Directory**, que tenemos; y su **victimología sectorial incluye el agroalimentario exportador y la logística**, que es la columna de la economía chilena |
| Marcado de difusión | `TLP:CLEAR` · `PAP:AMBER` |
| Clasificación interna | Público — apto para difusión abierta |
| Requisitos atendidos | `PIR-01`, `PIR-04`, `PIR-07`, `PIR-16`, `PIR-17` |
| Solicitante / consumidor primario | Célula CTI (producción propia) · **Consejo y Continuidad de Negocio** (consumidores primarios de este informe, por delante del SOC) · CISO · Administración de Active Directory |
| Ventana de observación | 2024-10-01 → 2026-09-30, con antecedentes desde 2015 |
| Base de colección | 6 fuentes de primera mano · **sin telemetría propia** |
| Autor (analista) | Célula CTI |
| Revisión por pares | Pendiente |
| Aprobación | Pendiente |
| Caducidad / revisión | 2027-02-17 — 92 días |
| Productos relacionados | **`CTI-2026-025` (Gamaredon): el otro actor ruso de la cartera, y su contrario exacto** — uno recolecta a gran volumen, este destruye a pequeño volumen; y ambos están vinculados a la misma estructura · `CTI-2026-024` (Rhysida: el otro expediente de la cartera donde la pregunta es la recuperación) · `CTI-2026-030` (Salt Typhoon) |
| Paquete legible por máquina | `ioc_index.csv` del repositorio · sin bundle STIX propio |

> ⚠ **Limitación estructural, y aquí es de otra clase.** Sin telemetría propia,
> §O-4 queda sin evaluar. Pero la limitación de fondo es distinta: **contra un
> actor destructivo, la telemetría propia no es el instrumento adecuado.** Un
> borrador de datos se ejecuta una vez y lo que hay que saber de antemano no es
> si está presente, sino **cuánto tardaríamos en volver a operar si se
> ejecutara**. Eso no se mide con un EDR: se mide con una prueba de
> restauración. El §O-4 de este informe está escrito en consecuencia.

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** Sandworm es el actor de esta cartera con mayor capacidad destructiva demostrada, y la única unidad estatal del expediente con **efectos físicos documentados**: cortes de suministro eléctrico en Ucrania en 2015 y 2016, el gusano `NotPetya` de 2017 —que la contabilidad pública sitúa como el ciberataque más costoso de la historia—, `Industroyer` e `Industroyer2` contra sistemas de control industrial, y `Olympic Destroyer`. Valoramos **casi con certeza** *(95–99 %)* la atribución de ese historial. **Confianza: alta.** *Base:* una acusación federal estadounidense de 2020, la ficha de MITRE, y análisis convergentes de múltiples proveedores durante una década.

**KJ-2.** La actividad de 2025 y 2026 no es una continuación simbólica de ese historial: es **una campaña de destrucción sostenida y sectorialmente dirigida**. ESET documentó borradores de datos de forma regular desde principios de 2025, con tres hitos: en abril de 2025, dos borradores —`ZEROLOT` y `Sting`— contra una universidad ucraniana; en **junio y septiembre de 2025, múltiples variantes contra los sectores gubernamental, energético, logístico y cerealero**; y en octubre de 2026 un caso en el que el acceso lo obtuvo otro actor y Sandworm ejecutó la fase destructiva. Valoramos **casi con certeza** *(95–99 %)* la exactitud de esta secuencia. **Confianza: alta.** *Base:* informes trimestrales de un proveedor con telemetría desplegada en el teatro, publicados en tres momentos distintos y coherentes entre sí.

**KJ-3.** El hallazgo con mayor consecuencia para nosotros es el **vector de distribución**: ESET afirma que el grupo propagó sus borradores «principalmente mediante la explotación de la característica de directiva de grupo de Active Directory». Es decir, **no usa un exploit para repartir el borrado: usa el mecanismo con el que la organización administra su propio parque.** Quien controla una directiva de grupo con alcance de dominio puede ejecutar código en todos los equipos del dominio, por diseño y de forma autorizada. Valoramos **casi con certeza** *(95–99 %)* que cualquier organización con un dominio de Active Directory sea susceptible a la misma técnica, venga de este actor o de cualquier otro. **Confianza: alta.** *Base:* es una propiedad documentada de la plataforma; la afirmación sobre el uso es de la fuente.

**KJ-4.** La elección de sectores en 2025 es la parte del expediente que nos obliga a leerlo con atención, y no por geografía. Al golpear **logística y sector cerealero** de un país en guerra, el actor no buscaba inteligencia ni rescate: buscaba **degradar la capacidad exportadora de la economía adversaria**. Las fuentes lo interpretan así de forma explícita. Valoramos **probable** *(55–80 %)* que la selección respondiera a ese objetivo económico y no a oportunidad. **Confianza: moderada.** *Base:* interpretación de la fuente, con la que coincidimos; el razonamiento sobre su transferibilidad a otras economías exportadoras es nuestro y está en `KJ-8`.

**KJ-5.** En diciembre de 2025 el objetivo fue **una empresa energética de Polonia**, es decir, de un Estado miembro de la OTAN y de la Unión Europea, fuera del teatro ucraniano. ESET atribuye ese ataque a Sandworm **con confianza media**, y una segunda firma especializada en sistemas industriales lo vincula al mismo conjunto de actividad. Valoramos **posibilidad real** *(45–55 %)* de que ese caso marque una ampliación deliberada del perímetro de objetivos destructivos y no un caso aislado. **Confianza: baja.** *Base:* una atribución declarada de confianza media por su propio autor, y una corroboración parcial; es el punto más débil del expediente y el más importante estratégicamente.

**KJ-6.** El modelo de operación está dividido, y eso cambia dónde hay que mirar. Microsoft documentó en febrero de 2025 un **subgrupo dedicado exclusivamente a obtener accesos**, al que llamó `BadPilot`, con una operación multianual de alcance global que abarcó **más de quince países** y cuya función es **entregar accesos a otras unidades**. Y en octubre de 2026 ESET documentó un caso concreto del mismo patrón: otro actor ruso, `UAC-0099`, obtuvo el acceso inicial en una empresa cerealera ucraniana **y se lo entregó a Sandworm**, que ejecutó el borrado. Valoramos **muy probable** *(80–95 %)* que el acceso inicial y la acción destructiva estén separados organizativamente. **Confianza: moderada.** *Base:* dos fuentes independientes documentando el mismo patrón con casos distintos.

**KJ-7.** La consecuencia operativa de `KJ-6` es incómoda y hay que enunciarla: **el momento en que este actor es detectable no es el momento en que destruye.** Cuando Sandworm llega, el acceso ya existe y lo consiguió otro, probablemente meses antes, con técnicas de intrusión ordinarias. **La detección útil es la del intruso aburrido que entró primero**, no la del borrador que se ejecuta al final. Valoramos **casi con certeza** *(95–99 %)* que esto sea así. **Confianza: alta.** *Base:* se sigue directamente de `KJ-6`; es una conclusión lógica.

**KJ-8.** Nuestra exposición no es ser objetivo de la inteligencia militar rusa: **es tener su vector y su perfil de víctima sectorial.** No hay una sola víctima latinoamericana documentada en ningún informe sobre este actor, y no hay razón estructural para esperar una. Pero (a) el vector de distribución es la directiva de grupo, que tiene cualquier organización con dominio; (b) el perfil sectorial golpeado en 2025 —agroalimentario exportador, logística, energía— es **exactamente la columna de la economía chilena**; y (c) el precedente polaco demuestra que el perímetro de lo destruible no coincide con el del conflicto. Valoramos **remoto** *(5–10 %)* que este actor concreto opere contra objetivos chilenos, y **posibilidad real** *(45–55 %)* de que la técnica de distribución por directiva de grupo se use contra organizaciones de la región por actores de extorsión. **Confianza: moderada.** *Base:* la primera valoración es inferencia desde doce años de victimología sin excepciones regionales; la segunda, desde que la técnica es pública, trivial de reproducir y maximiza el daño por unidad de esfuerzo.

**KJ-9.** Y un juicio sobre un dato negativo que importa para la lectura del lote completo: **Sandworm no aparece entre los tres primeros del ranking de actividad estatal global de noviembre de 2026**, donde sí está Gamaredon con el 9,03 %. La causa es la inversa de la de `CTI-2026-028`: no es que opere donde no hay sensor, es que **opera poco y una sola vez por objetivo.** Un borrador de datos se ejecuta una vez y después no hay nada que detectar porque no hay nada que mirar. Valoramos **probable** *(55–80 %)* que el bajo volumen de telemetría refleje el modelo de operación y no falta de actividad. **Confianza: moderada.** *Base:* razonamiento nuestro, consistente con la secuencia documentada de `KJ-2`.

**Qué cambiaría estos juicios:** un segundo caso destructivo documentado **fuera del teatro ucraniano**, que convertiría `KJ-5` de posibilidad aislada en patrón y obligaría a reevaluar `KJ-8` desde cero. Y, en el otro extremo, la aparición de la técnica de distribución por directiva de grupo en una campaña de extorsión contra la región, que convertiría la segunda mitad de `KJ-8` en hecho. Son los indicadores `I-1` e `I-3` de §O-7.

---

## 2. Resumen ejecutivo

Los cinco informes anteriores de esta cartera sobre actores estatales tratan de robo de información. Este trata de otra cosa, y conviene decirlo en la primera línea: **Sandworm no quiere nuestros datos. Quiere que dejemos de funcionar.**

Es la unidad de inteligencia militar rusa a la que se atribuyen los cortes de electricidad en Ucrania de 2015 y 2016, el gusano `NotPetya` de 2017 —cuyo coste global sigue siendo el mayor registrado para un ciberataque— y los ataques con `Industroyer` contra sistemas de control industrial. Hay una acusación federal estadounidense de 2020 que nombra a sus miembros. No es un actor cuya existencia esté en discusión.

Lo que importa aquí es lo que ha hecho en los últimos dos años, y son tres cosas.

**La primera es cómo reparte la destrucción.** ESET documentó que el grupo propagó sus borradores de datos «principalmente mediante la explotación de la característica de directiva de grupo de Active Directory». Léase despacio: no usó una vulnerabilidad para llegar a todos los equipos. Usó **el mecanismo con el que la propia organización administra su parque**. Una directiva de grupo con alcance de dominio ejecuta lo que se le diga en todos los equipos del dominio, porque para eso existe. Quien consigue escribir una de esas directivas no necesita nada más: tiene distribución autorizada, simultánea y total. Esto no es un fallo que se parchee. Es una decisión de arquitectura que casi nadie ha tomado.

**La segunda es a quién golpeó.** En abril de 2025 desplegó dos borradores distintos —`ZEROLOT` y `Sting`— contra una universidad ucraniana; uno de ellos se ejecutaba desde una tarea programada con un nombre en argot ruso que se traduce aproximadamente como «come un poco de gulash», lo que dice algo sobre el estado de ánimo de quien lo escribió. Y en junio y septiembre de 2025 golpeó los sectores **gubernamental, energético, logístico y cerealero**.

El cerealero es el que debería hacernos levantar la vista. No se ataca el grano para robar información ni para pedir rescate. Se ataca para que un país exportador deje de exportar. Y ése es un razonamiento que no depende de Ucrania: **si alguna vez alguien decidiera degradar la economía chilena por vía informática, el objetivo no serían los bancos: serían la fruta, el salmón, el vino y los puertos por donde salen.** No decimos que vaya a ocurrir —no hay el menor indicio de que este actor opere en nuestro hemisferio— sino que el razonamiento del adversario es público, y que nuestro sector exportador es el equivalente estructural de lo que él eligió golpear.

**La tercera es dónde ocurrió en diciembre de 2025: Polonia.** Una empresa energética de un país de la OTAN y de la Unión Europea, fuera del teatro de la guerra. ESET atribuye ese ataque a este actor **con confianza media** —y es importante no convertir esa cautela en certeza al citarla—. Si se confirmara como patrón y no como caso aislado, significaría que el perímetro de lo que este actor considera destruible no coincide con el del conflicto armado.

Hay un cuarto elemento, y es el que cambia dónde hay que poner el esfuerzo. Este actor **no consigue sus propios accesos**. Microsoft documentó en febrero de 2025 un subgrupo dedicado exclusivamente a eso, que operó en más de quince países durante años y cuya función es **entregar accesos a otras unidades**. Y en octubre de 2026 ESET documentó el caso concreto: otro grupo ruso entró en una empresa cerealera ucraniana, y **le pasó el acceso a Sandworm para que ejecutara el borrado**.

La consecuencia es que **el momento en que este actor es visible no es el momento en que destruye, sino meses antes, cuando entró alguien mucho más ordinario**. Lo que detecta a Sandworm es detectar al intruso aburrido que llegó primero. Y lo que lo frena, una vez dentro, no es una regla de detección: es que los respaldos estén fuera de su alcance.

Por eso este informe va dirigido en primer lugar al Consejo y a Continuidad de Negocio, y sólo después al SOC. Las decisiones que pide no son de detección. Son tres: que los respaldos estén **desconectados y se pruebe la restauración**, que la escritura de directivas de grupo esté **restringida y auditada**, y que exista una respuesta a la pregunta **cuánto tardaríamos en volver a operar**, por escrito y con una fecha de la última vez que se comprobó.

<!-- cti:cards -->

| Rasgo | Qué significa | Etiqueta |
|---|---|---|
| Destruye, no roba | La pregunta no es qué se llevaría: es si volveríamos a operar. **Cambia el consumidor del informe** | `01 · finalidad` |
| Reparte el borrado por directiva de grupo | Usa nuestro propio mecanismo de administración. **No hay parche: hay decisión de arquitectura** | `02 · vector` |
| Golpeó logística y sector cerealero | Objetivo económico, no informativo. El perfil sectorial es el de la economía exportadora chilena | `03 · victimología` |
| Diciembre de 2025: energía en Polonia | Un país de la OTAN, fuera del teatro. Atribución de **confianza media**: no convertirla en certeza | `04 · perímetro` |
| No consigue sus propios accesos | Un subgrupo se los entrega, y otro grupo ruso también. **Se detecta al que entró primero** | `05 · división` |
| Usa herramientas legítimas para borrar | Una utilidad de borrado seguro de Microsoft entre ellas. Ninguna firma la detendrá | `06 · herramienta` |
| Ausente del ranking de prevalencia | Opera poco y una sola vez por objetivo. **Un borrador no deja nada que contar** | `07 · medición` |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `2` | Veces que se le atribuye haber provocado cortes de suministro eléctrico | Ucrania, 2015 y 2016. **Es el único actor de esta cartera con efectos físicos documentados** |
| `4` | Sectores golpeados con borradores de datos en junio y septiembre de 2025 | Gubernamental, energético, **logístico y cerealero** |
| `2` | Borradores distintos desplegados contra un solo objetivo en abril de 2025 | `ZEROLOT` y `Sting`, contra una universidad ucraniana |
| `15+` | Países alcanzados por su subgrupo de acceso, según Microsoft | Operación multianual cuya función es **entregar accesos a otras unidades** |
| `74455` | Unidad de la inteligencia militar rusa a la que se le atribuye | Centro Principal de Tecnologías Especiales. Hay acusación federal de 2020 con nombres |
| `1` | Casos destructivos documentados fuera del teatro ucraniano | Polonia, diciembre de 2025. **Atribución de confianza media** |
| `1` | Veces que se ejecuta un borrador de datos por objetivo | Es la razón de `KJ-9`: no hay volumen que medir |
| `0` | Víctimas latinoamericanas documentadas en doce años | Y no hay razón estructural para esperarlas. Véase `KJ-8` |
| `2009` | Año de inicio de actividad según una de las fuentes | **Las fuentes discrepan: 2009, 2013 o 2014.** Véase §3.3-v |

<!-- cti:note type="good" -->

> ✅ **Decisiones que se solicitan a Dirección — y nótese que ninguna es de detección.** (a) **Respaldos desconectados y prueba de restauración con fecha**: verificar que existe al menos una copia fuera de línea o inmutable de los sistemas críticos, inalcanzable desde el dominio, y **ejecutar una restauración real** cuyo resultado y duración queden por escrito. Es la única decisión de este informe que determina el resultado si alguna vez ocurre — 60 días. (b) **Restringir y auditar la escritura de directivas de grupo**: quién puede crear o modificar una directiva con alcance de dominio, con autenticación reforzada, aprobación de cambio y alerta inmediata ante toda modificación. **Es la decisión de mayor valor por coste** — 60 días. (c) **Responder por escrito a la pregunta de recuperación**: cuánto tardaríamos en volver a operar si perdiéramos simultáneamente todos los equipos del dominio, y qué procesos de negocio sobrevivirían. Es un ejercicio de continuidad, lo firma Dirección y caduca — 90 días. (d) **Separar por niveles la administración de Active Directory** y eliminar la pertenencia permanente a grupos de administración de dominio — 120 días. (e) **Revisión de cartera agroalimentaria, logística y portuaria**: qué parte de nuestros ingresos o de nuestros contratos depende de esos sectores, que son los que este actor eligió golpear — 90 días, y es de Riesgo, no de seguridad. (f) **Reorientar el esfuerzo de detección al acceso inicial ordinario**, por `KJ-7`: lo que detecta a un actor destructivo es el intruso corriente que entró meses antes — 30 días para la instrucción.

---

## 3. Alcance, requisitos y limitaciones

**3.1 Requisitos de inteligencia atendidos**

| Req. | Enunciado | ¿Respondido? | Dónde |
|---|---|---|---|
| PIR-01 | ¿Qué actores tienen intención y capacidad contra nuestro sector y geografía? | **Parcialmente**: capacidad máxima, intención sobre nuestra geografía sin ningún indicio | `KJ-1`, `KJ-8` |
| PIR-04 | ¿Qué amenazas operan contra la región hispanohablante? | **Ninguna documentada de este actor** | §E-2 |
| PIR-07 | ¿Qué técnicas invalidan nuestros controles actuales? | **Sí**: la distribución por directiva de grupo invalida el control de ejecución, porque la ejecución está autorizada | `KJ-3`, §O-3 |
| PIR-16 | ¿Qué amenazas pueden detener nuestra operación, y en cuánto tiempo volveríamos? | **Sí, y es el requisito que estructura el informe** | `KJ-1`, §O-4, §E-4 |
| PIR-17 | ¿Qué exposición tiene nuestra cadena de valor exportadora? | **Sí, por transferencia de perfil sectorial** | `KJ-4`, `KJ-8`, §E-2 |
| — | ¿Estamos ya comprometidos? | **No evaluable, y para este actor es la pregunta equivocada.** Véase la nota de §0 | §O-4 |

**3.2 Fuera de alcance.** No se evalúa: el historial del actor anterior a octubre de 2024 más allá del contexto de `KJ-1`, que está exhaustivamente documentado en otras fuentes; el análisis de ingeniería inversa de cada familia de borrador; la actividad de `UAC-0099` como actor propio, que aparece aquí sólo como proveedor de acceso y merecería producto separado —y que también aparece en `CTI-2026-025` por su uso de un señuelo contra análisis basados en modelos de lenguaje—; la capacidad del actor contra sistemas de control industrial, que exige conocimiento de ingeniería de proceso y una evaluación específica por instalación; la atribución nominal de los miembros acusados en 2020, que es materia judicial; y **la respuesta a un incidente destructivo consumado**, que es un procedimiento de continuidad y no de respuesta a incidentes ordinaria.

**3.3 Limitaciones de la colección.** (i) **Ninguna fuente primaria se leyó íntegra.** Los informes trimestrales y las notas de prensa de ESET se leyeron por su contenido publicado y por coberturas coincidentes de prensa especializada; el análisis de Microsoft sobre el subgrupo de acceso, sólo por coberturas secundarias. Las afirmaciones centrales —el vector de directiva de grupo, los cuatro sectores, los nombres de los borradores, la cifra de más de quince países— aparecen de forma coincidente en varias coberturas que las atribuyen literalmente a sus autores. Es la limitación dominante y está en `G-1`. (ii) **Hay un conflicto de fechas sin resolver en el caso cerealero.** Una fuente sitúa la entrega de acceso y el borrado como investigación publicada en octubre de 2026; otra sitúa el ataque destructivo el 17 de septiembre de 2025. No se puede determinar si son el mismo caso con publicación tardía o dos casos distintos. Se consigna en §O-5 con la ambigüedad explícita. (iii) **La atribución del caso polaco es de confianza media declarada por su propio autor**, y este informe no la eleva: `KJ-5` queda en posibilidad real con confianza baja. Una segunda firma la vincula al mismo conjunto de actividad, pero esa corroboración se conoce por una sola fuente secundaria. (iv) **No se localizó ningún informe de primera mano de 2026 sobre actividad destructiva nueva.** El material de 2026 que se maneja es: el informe trimestral Q2–Q3 2026, que confirma la regularidad de los ataques desde principios de 2025, y la investigación de la entrega de acceso. **Todo el detalle técnico de los borradores es de 2025**, y debe leerse con esa antigüedad. (v) **Las fuentes discrepan sobre el año de inicio del actor**: 2009, 2013 y 2014 según cuál se lea. Se consigna el rango. (vi) **Una fuente advierte expresamente que el organigrama del actor no está consensuado**: que las designaciones `Sandworm`, `APT44` y `Seashell Blizzard` no corresponden necesariamente a la misma delimitación, y que la vinculación a la unidad concreta de inteligencia militar es una atribución de inteligencia y no una determinación judicial. **Se recoge esa cautela en §O-1 y §O-2.** (vii) **El nombre `PathWiper` aparece en coberturas entre los borradores atribuidos a actividad rusa contra Ucrania, pero ninguna fuente leída lo atribuye específicamente a este actor.** No se sostiene aquí. (viii) **Sin telemetría propia**, con la salvedad conceptual de la nota de §0. (ix) **El Anexo A de este informe es excepcionalmente corto** y la razón es de fondo, no de colección: véase la advertencia del Anexo A y §T-3.

**3.4 Metodología.** Disciplinas: OSINT comercial de primera mano por vía indirecta (informes trimestrales y notas de investigación de un proveedor con telemetría en el teatro, más el análisis de un gran proveedor de plataforma sobre el subgrupo de acceso), OSINT de marco (ficha `G0034` de MITRE), **OSINT judicial** (acusación federal estadounidense de 2020, por vía secundaria), y **análisis de transferencia de perfil sectorial** —el razonamiento de `KJ-8` sobre qué significa que el actor eligiera el sector cerealero—, que es una técnica con riesgo propio y se declara como tal. Técnicas analíticas estructuradas: análisis de hipótesis competidoras sobre la ampliación del perímetro destructivo (§O-6), comprobación de supuestos clave, pre-mortem. Marcos: MITRE ATT&CK v19, Pirámide del Dolor, Cadena de Intrusión, ICD 203, código Admiralty.

---

# NIVEL ESTRATÉGICO
### Para: **Consejo · Continuidad de Negocio** · CISO · Riesgo · Administración de Active Directory · Horizonte: 12–36 meses

## E-1. Qué representa este actor en el panorama

En el lote de noviembre de 2026, los cinco actores anteriores comparten una característica: **si tienen éxito, no se nota.** Un actor de recolección que opera bien se lleva documentos y no deja huella; el daño es diferido, a veces invisible, y se materializa en pérdida de ventaja competitiva o de ventaja diplomática. La respuesta razonable a ese riesgo es detección.

Sandworm invierte el planteamiento. **Si tiene éxito, se nota inmediatamente y la detección ya no sirve de nada**, porque el acontecimiento que había que prevenir ya ocurrió y es irreversible por definición. Un borrador de datos no se contiene: se restaura desde una copia o no se restaura.

Eso convierte este expediente en un problema de **continuidad**, y la diferencia es práctica. Las decisiones que importan no se toman en el SOC ni con presupuesto de seguridad: se toman decidiendo que una copia de respaldo esté desconectada, que se pruebe la restauración, y que alguien pueda responder por escrito cuánto tardaríamos en volver a operar. Son decisiones baratas, aburridas, y es exactamente por eso por lo que llevan años pendientes en la mayoría de las organizaciones.

Hay un segundo rasgo estructural que conviene registrar, y es el que cierra el argumento del lote completo sobre los rankings de prevalencia. **Este actor tampoco aparece entre los tres primeros de la medición de noviembre de 2026.** La causa es distinta de la de `CTI-2026-028`:

| | Por qué no está en el ranking |
|---|---|
| `CTI-2026-028` UNC3886 | **No hay sensor donde opera**: hipervisores, appliances, routers fuera de soporte |
| **`CTI-2026-029` Sandworm** | **No hay volumen que medir**: un borrador se ejecuta una vez por objetivo, y después no hay nada que mirar porque no hay nada |

Son dos formas distintas de ser invisible a la telemetría agregada, y las dos corresponden a los actores de mayor consecuencia del lote. La formulación final del hallazgo transversal, que `CTI-2026-028` enunció y este completa: **un ranking de prevalencia es una función de la frecuencia y de la observabilidad, y los adversarios más consecuentes puntúan bajo en las dos.**

<!-- cti:cards -->

| Cambio estructural | Por qué nos afecta | Etiqueta |
|---|---|---|
| El mecanismo de administración se convirtió en el vector | La directiva de grupo reparte el borrado con autorización legítima. **El control de ejecución no sirve: la ejecución está aprobada** | `01 · administración` |
| La destrucción se dirige a la economía, no a la información | Logística y sector cerealero de un país exportador. **El objetivo es el producto interior bruto, no el secreto** | `02 · finalidad` |
| El perímetro de lo destruible dejó de coincidir con el del conflicto | Diciembre de 2025, energía en un país de la OTAN. Con confianza media, pero una vez es suficiente para replantear el supuesto | `03 · perímetro` |
| El acceso y el efecto están separados organizativamente | Un subgrupo y hasta un grupo distinto proveen el acceso. **Se detecta al proveedor, no al destructor** | `04 · división` |
| El borrado se hace con herramientas legítimas | Una utilidad de borrado seguro firmada por Microsoft entre ellas. No hay firma que la detenga | `05 · herramienta` |
| La medida del riesgo es el tiempo de recuperación | Y casi ninguna organización tiene ese número verificado con una fecha reciente | `06 · recuperabilidad` |

## E-2. Victimología

<!-- cti:bars title="Sectores golpeados con capacidad destructiva, 2025 (fuente de primera mano)" -->

| Sector | Casos documentados |
|---|---|
| Gubernamental | `múltiples` |
| Energía | `múltiples` |
| Logística | `múltiples` |
| **Sector cerealero** | `múltiples` |
| Educación superior | `1` |
| Energía (Polonia, confianza media) | `1` |

<!-- cti:bars title="Geografía documentada en doce años" -->

| País o región | Casos |
|---|---|
| Ucrania | `la mayoría` |
| Polonia | `1 (confianza media)` |
| Global, sólo accesos del subgrupo | `15+ países` |
| Internacional, efecto colateral de `NotPetya` (2017) | `global` |
| **Latinoamérica** | `0` |

> **Lectura clave, y es la razón por la que este informe existe.** El cero
> latinoamericano de este expediente es, de los seis de la cartera, **el mejor
> fundamentado**: doce años de seguimiento, una docena de fuentes acumuladas, un
> mandato de recolección y de efecto explícitamente ligado a un conflicto
> concreto, y ninguna mención de la región ni una sola vez. **Este actor no nos
> va a atacar, y decirlo con esa claridad es parte del producto.**
>
> Lo que sí nos alcanza son dos cosas, y ninguna es una amenaza del actor.
>
> La primera es **el vector**. La distribución por directiva de grupo de Active
> Directory no es una capacidad de inteligencia militar: es una técnica pública,
> documentada, trivial de reproducir y de rendimiento máximo. Cualquier grupo de
> extorsión que la adopte obtiene distribución simultánea a todo el dominio sin
> escribir una línea de exploit. **Es el escenario de la segunda mitad de `KJ-8`
> y el que justifica la decisión `E-b`.**
>
> La segunda es **el razonamiento sectorial**, y es más sutil. Cuando este actor
> eligió golpear logística y grano, no eligió un sector: eligió **el mecanismo por
> el que la economía adversaria genera divisas**. Ese razonamiento es
> independiente del país. Chile exporta fruta, salmón, vino, celulosa y cobre por
> un número reducido de puertos y con una cadena de frío y de trazabilidad que
> depende por completo de sistemas informáticos. **Ningún informe dice que nadie
> esté mirando eso. Lo que decimos es que el razonamiento que llevaría a mirarlo
> ya está publicado**, y que la pregunta de la decisión `E-e` —qué parte de
> nuestra cartera depende de esos sectores— no se ha hecho nunca.

## E-3. Tendencia y pronóstico

<!-- cti:chart title="Hitos destructivos documentados por periodo" cap="Cuenta episodios destructivos publicados, no víctimas. La serie de 2025 es la mejor documentada; la de 2026 refleja sobre todo confirmación de regularidad, no episodios nuevos." -->

| Periodo | Hitos |
|---|---|
| `2015–2017` | `4` |
| `2018–2022` | `3` |
| `2024-Q4 → 2025-Q1` | `1` |
| `2025-Q2` | `2` |
| `2025-Q3` | `2` |
| `2025-Q4` | `1` |
| `2026` | `1` |

<!-- cti:cards -->

| Escenario | Desarrollo | Etiqueta |
|---|---|---|
| Continuidad en el teatro ucraniano | Borradores regulares contra gobierno, energía, logística y agroalimentario, con el acceso provisto por terceros y la distribución por directiva de grupo. **Escenario base, y no nos afecta** | `Probable · 55–80 %` |
| **Difusión de la técnica de directiva de grupo a actores de extorsión** | La técnica es pública y maximiza el daño por unidad de esfuerzo. **Es el escenario que nos obliga a actuar, y la acción es la decisión `E-b`** | `Probable · 55–80 %` |
| Consolidación del perímetro ampliado | Más casos destructivos en Estados de la OTAN fuera del teatro, confirmando que el caso polaco era patrón. **Cambiaría la evaluación de riesgo de la cadena de suministro europea, no la nuestra** | `Posibilidad real · 45–55 %` |
| Vuelta a efectos físicos sobre sistemas industriales | El actor tiene historial de dos cortes de suministro y dos familias dirigidas a control industrial. No hay indicio de actividad nueva en esa línea desde 2022 | `Posibilidad real · 45–55 %` |
| Actividad destructiva en Latinoamérica | **Sin un solo indicio en doce años, y sin un mandato que la explicara** | `Remoto · 5–10 %` |

## E-4. Decisiones que este informe pide al nivel estratégico

<!-- cti:table highlight="respaldo|restauración|directiva de grupo|recuperación" -->

| # | Decisión | Fundamento | Plazo |
|---|---|---|---|
| E-a | **Respaldos fuera del alcance del dominio, y prueba de restauración real con resultado por escrito.** Verificar que existe al menos una copia desconectada o inmutable de los sistemas críticos, **inalcanzable con credenciales de dominio**, y ejecutar una restauración completa de un sistema representativo, registrando cuánto tardó y qué falló. **Es la única decisión de este informe que determina el resultado si alguna vez ocurre**, y la única cuyo incumplimiento no admite compensación con ningún otro control | `KJ-1`, `KJ-3`, §O-4 | 60 días |
| E-b | **Restringir y auditar la escritura de directivas de grupo.** Inventariar quién puede crear o modificar una directiva con alcance de dominio o de unidad organizativa amplia; reducir esa lista al mínimo; exigir autenticación reforzada y aprobación de cambio; y **alertar de forma inmediata ante cualquier modificación**. Es la decisión de mayor relación entre valor y coste del informe, y **protege igual contra este actor y contra cualquier grupo de extorsión que copie la técnica** | `KJ-3`, §X-3 | 60 días |
| E-c | **Responder por escrito a la pregunta de recuperación**, y ponerle fecha de caducidad: cuánto tardaríamos en volver a operar si perdiéramos simultáneamente todos los equipos del dominio; qué procesos de negocio seguirían funcionando sin sistemas; y quién decide qué se restaura primero. **Lo firma Dirección, no el CISO**, porque las respuestas son de negocio | `KJ-1`, §O-4 | 90 días |
| E-d | **Separación por niveles de la administración de Active Directory**, con eliminación de la pertenencia permanente a grupos de administración de dominio y estaciones de administración dedicadas. Es la medida que impide que un acceso ordinario se convierta en control del dominio, y por tanto la que corta la cadena entre `KJ-6` y `KJ-3` | §T-1, §X-5 | 120 días |
| E-e | **Revisión de cartera agroalimentaria, logística y portuaria**: qué parte de nuestros ingresos, de nuestros contratos o de nuestra operación depende de los sectores que este actor eligió golpear. Es de Riesgo y de Dirección Comercial, no de seguridad, y su valor no depende de que este actor exista | `KJ-4`, `KJ-8`, §E-2 | 90 días |
| E-f | **Reorientar por escrito el esfuerzo de detección hacia el acceso inicial ordinario.** Por `KJ-7`, lo que hace visible a un actor destructivo es el intruso corriente que entró meses antes. Instruir que el presupuesto de detección se evalúe por su cobertura del acceso inicial y del movimiento lateral, no por su cobertura de familias de malware destructivo | `KJ-6`, `KJ-7` | 30 días |
| E-g | **Incorporar al plan de colección permanente dos indicadores**: aparición de un segundo caso destructivo fuera del teatro ucraniano (`I-1`), y aparición de la distribución por directiva de grupo en una campaña de extorsión contra la región (`I-3`). El segundo es el único de los dos que cambiaría algo para nosotros | §O-7 | 30 días |

---

# NIVEL OPERACIONAL
### Para: Jefatura de SOC · Respuesta a Incidentes · **Continuidad y Respaldo** · Administración de Active Directory · Horizonte: semanas–meses

## O-1. Identificación y alias

| Designación | Origen | Grado de equivalencia |
|---|---|---|
| `Sandworm` | iSIGHT Partners (2014), de uso general en la industria | **Referencia** |
| `APT44` | Mandiant / Google | **Equivalente, con la salvedad de delimitación.** Véase la nota |
| `Seashell Blizzard` | Microsoft (taxonomía vigente) | Equivalente, con la misma salvedad |
| `IRIDIUM` | Microsoft (taxonomía anterior) | Equivalente — precede a `Seashell Blizzard` |
| `Voodoo Bear` | CrowdStrike | Equivalente |
| `TeleBots` | ESET | **Nombre histórico de un conjunto de actividad** atribuido al mismo actor, usado para la línea que condujo a `NotPetya` |
| `BlackEnergy Group` | Diversos | Nombre histórico, por la familia usada en los ataques a la red eléctrica ucraniana |
| `ELECTRUM` | Dragos | **Equivalente en el dominio industrial.** Es la designación que aparece vinculada al caso polaco de diciembre de 2025 |
| `FROZENBARENTS` | Recorded Future | Equivalente |
| `UAC-0002` | CERT-UA | Equivalente — designación del equipo nacional ucraniano |
| `G0034` | MITRE ATT&CK | Equivalente — ficha de grupo |
| **`BadPilot`** | Microsoft | **No es un alias: es un subgrupo.** Designación de la operación de acceso inicial, que Microsoft describe como un subgrupo distinto dentro de la organización mayor |
| `Unidad 74455` / `GTsST` | Atribución estatal | **No es un alias comercial: es la unidad de inteligencia militar** a la que el actor se atribuye, el Centro Principal de Tecnologías Especiales |
| `UAC-0099` | CERT-UA | **NO es un alias y no es el mismo actor.** Es el grupo que, en el caso cerealero, **obtuvo el acceso inicial y lo entregó** a este. Fundirlos borra precisamente la división de trabajo que `KJ-6` documenta |

> **Nota de tradecraft, y en este expediente hay dos riesgos de signo opuesto.**
>
> El primero es el habitual de un actor con doce designaciones: **asumir que
> todas delimitan el mismo conjunto de actividad.** Una de las fuentes advierte
> expresamente que el organigrama de este actor **no está consensuado**: que
> `Sandworm`, `APT44` y `Seashell Blizzard` no corresponden necesariamente a la
> misma frontera, y que la vinculación a la unidad concreta de inteligencia
> militar es **una atribución de inteligencia y no una determinación judicial**
> —aunque exista una acusación federal de 2020 que nombra personas—. Es una
> cautela honesta y se recoge.
>
> El segundo es específico y más peligroso para una regla de detección:
> **confundir al actor con sus proveedores de acceso.** `BadPilot` es un subgrupo
> suyo; `UAC-0099` es un grupo distinto que le entregó un acceso. Las tres
> entidades aparecen en el mismo incidente y hacen cosas diferentes. **Quien
> escriba una regla contra «Sandworm» cubriendo el acceso inicial estará
> cubriendo a otro actor** —y eso no es un error, es lo correcto por `KJ-7`,
> pero hay que saberlo y nombrarlo bien.
>
> Contrástese con `CTI-2026-017`, donde el problema era tomar un implante por un
> actor, y con `CTI-2026-028`, donde era la falta de alias. Aquí el problema es
> **el organigrama**: tres entidades con funciones distintas en una sola cadena.

## O-2. Estructura y atribución

| Eje de atribución | Valoración | Confianza |
|---|---|---|
| Clúster técnico | **Coherente a lo largo de una década**, con linaje trazable de familias destructivas y reutilización de técnicas de distribución | Alta |
| Grupo organizado | **Sí, y con estructura interna diferenciada**: al menos un subgrupo dedicado exclusivamente al acceso inicial, cuya función es entregar accesos a otras unidades | Alta |
| Nexo estatal | **Inteligencia militar rusa, Centro Principal de Tecnologías Especiales (Unidad 74455).** Hay **acusación federal estadounidense de 2020 con personas nombradas** | Alta |
| Identidad nominal | **Sí** — miembros acusados nominalmente en 2020 | Moderada — no verificable con fuentes abiertas técnicas |
| Delimitación del organigrama | **No consensuada.** Las designaciones de distintos proveedores pueden no cubrir la misma frontera | Baja |
| Relación con `UAC-0099` | **Proveedor de acceso, no subordinado.** Documentada en un caso concreto | Moderada |

*Razonamiento.* Ésta es, junto con la de Gamaredon en `CTI-2026-025`, la atribución más sólida de la cartera, y por una razón distinta: **existe una acusación judicial que nombra personas y una unidad militar concreta.** Ningún otro actor de los seis tiene ese nivel. A eso se suma una década de continuidad de efecto —no sólo de herramientas— y una coherencia de objetivo que ningún actor criminal mantendría: doce años sin un solo intento de monetización, con capacidad para extorsionar en cualquier momento.

*Contraargumento, y es de delimitación y no de identidad.* El punto débil no es si el actor existe ni a quién pertenece: es **dónde empieza y dónde acaba**. Con un subgrupo de acceso que opera en más de quince países y al menos un grupo externo que le entrega accesos, la pregunta «¿fue Sandworm?» se vuelve ambigua para la fase de intrusión y sólo es nítida para la fase de efecto. **Una atribución de este actor a un incidente concreto debería especificar a qué fase se refiere.**

*Observación sobre la relación con Gamaredon, porque es útil para la cartera.* `CTI-2026-025` documenta un actor atribuido al servicio de seguridad —no a la inteligencia militar— con un modelo exactamente inverso: altísimo volumen, cientos o miles de máquinas, recolección indiscriminada, cero destrucción. Sandworm es bajo volumen, selección estricta y efecto terminal. **Dos servicios del mismo Estado, en el mismo teatro, con modelos opuestos**, y los dos ligados por una misma lógica de división de trabajo que en el caso de Gamaredon lleva a Turla y en el de Sandworm a `UAC-0099`. Es el mismo patrón organizativo en dos expedientes independientes.

## O-3. Modelo de operación: tres cosas y la segunda es la que importa

**Uno: el acceso lo consigue otro.** El subgrupo que Microsoft documentó en febrero de 2025 llevaba años ejecutando una operación de acceso inicial de alcance global, en más de quince países, **con el propósito explícito de entregar esos accesos a otras unidades**. Y el caso cerealero documenta la versión externa del mismo arreglo: un grupo distinto entró, validó el objetivo, y pasó el control. Para el defensor esto significa que **la ventana de detección es la del intruso ordinario**, y que puede ser de meses.

**Dos: la distribución es la directiva de grupo, y esto es el centro del informe.** Una vez con control del dominio, el actor no necesita propagar nada. Escribe una directiva de grupo y **el propio Active Directory la distribuye y la ejecuta en todos los equipos del dominio, de forma autorizada, simultánea y silenciosa**, porque es exactamente para lo que ese mecanismo existe.

Las consecuencias de esto merecen enumerarse porque anulan controles que se dan por buenos:

- **El control de ejecución de aplicaciones no ayuda**: la ejecución viene de una fuente autorizada.
- **La detección de movimiento lateral no ayuda**: no hay movimiento lateral, hay distribución centralizada.
- **La detección de propagación no ayuda**: no hay gusano, no hay escaneo, no hay credencial reutilizada equipo a equipo.
- **La segmentación de red no ayuda**: la directiva llega por el canal de administración, que atraviesa la segmentación por diseño.
- **La simultaneidad elimina el tiempo de reacción**: no hay un primer equipo que alerte mientras los demás siguen limpios.

Lo único que sí ayuda es lo que la decisión `E-b` pide: **restringir quién puede escribir una directiva y alertar en el momento en que alguien lo hace.** Y lo único que salva si falla es `E-a`: una copia que el dominio no pueda alcanzar.

**Tres: el borrado se hace con lo que haya.** Las familias propias existen —`ZEROLOT`, `Sting`— pero una de las fuentes documenta el uso de **una utilidad legítima de borrado seguro firmada por Microsoft** como instrumento de destrucción. Un borrador escrito por el adversario se puede firmar y detectar; una herramienta legítima de borrado seguro, no. Y el detalle del nombre de la tarea programada de `Sting` —una expresión en argot ruso que se traduce aproximadamente como «come un poco de gulash»— confirma que la ocultación no era una prioridad en ese despliegue: **cuando el efecto es terminal, el sigilo posterior no tiene valor.**

> **La lectura conjunta.** Este actor ataca la misma clase de cosa que los
> cuatro anteriores del lote —un mecanismo de confianza— pero con una
> diferencia: los otros atacaban la confianza para **entrar sin ser vistos**;
> éste la ataca para **salir habiendo roto todo**. La confianza que explota es la
> que la organización deposita en su propio sistema de administración
> centralizada, y es una confianza que no se puede retirar: sin directivas de
> grupo no hay administración de parque. **Lo que sí se puede es controlar quién
> escribe en ella y tener una copia fuera de su alcance.**

## O-4. Nuestra exposición

> ⬛ **Sección sin evaluar, y aquí el cuestionario es distinto del de los cinco
> informes anteriores.** Ninguna pregunta busca indicadores de compromiso. Todas
> buscan **capacidad de recuperación y control del canal de administración**,
> porque eso es lo que determina el resultado contra un actor destructivo.

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| X-1 | **¿Existe al menos una copia de respaldo de los sistemas críticos que NO sea alcanzable con credenciales de dominio?** Desconectada, inmutable o en una cuenta con autenticación independiente | Arquitectura de respaldo | Continuidad / TI |
| X-2 | **¿Cuándo fue la última vez que se restauró de verdad un sistema completo desde esa copia, y cuánto tardó?** Con fecha y duración por escrito | Registro de pruebas de restauración | Continuidad |
| X-3 | **¿Quién puede crear o modificar una directiva de grupo con alcance de dominio?** Lista nominal, no de grupos | Active Directory | Administración de AD |
| X-4 | ¿Se alerta en el momento en que se crea o modifica una directiva de grupo? ¿A quién llega esa alerta y en cuánto tiempo? | Auditoría de AD / SIEM | SOC / Administración de AD |
| X-5 | ¿Hay pertenencia **permanente** a los grupos de administración de dominio? ¿Cuántas cuentas? | Active Directory | Administración de AD |
| X-6 | ¿La administración de Active Directory se hace desde estaciones dedicadas, o desde los equipos de trabajo habituales de los administradores? | Arquitectura de administración | Administración de AD |
| X-7 | **¿Cuánto tardaríamos en volver a operar si perdiéramos simultáneamente todos los equipos del dominio?** Es la pregunta de la decisión `E-c` | Plan de continuidad | **Dirección** |
| X-8 | ¿Qué procesos críticos de negocio pueden operar sin sistemas informáticos, aunque sea degradados? ¿Están documentados los procedimientos manuales? | Plan de continuidad | Continuidad / Operaciones |
| X-9 | ¿Está restringida la ejecución de utilidades de borrado seguro? ¿Las detectaríamos si se ejecutaran masivamente? | EDR / política | SOC |
| X-10 | ¿Tenemos registro y alerta de borrado masivo de ficheros o de sobrescritura de sectores de arranque? | EDR | SOC |
| X-11 | ¿Qué parte de nuestros ingresos, contratos u operación depende de los sectores agroalimentario exportador, logístico o portuario? | Cartera comercial | **Riesgo / Comercial** |
| X-12 | ¿Están nuestros controladores de dominio y nuestra infraestructura de respaldo en el mismo dominio de fallo que el resto del parque? | Arquitectura | Arquitectura / TI |

## O-5. Cronología

<!-- cti:timeline -->

| Fecha | Hecho | Traza |
|---|---|---|
| `2009`–`2014` | Rango de inicio de actividad según la fuente que se consulte. **Las fuentes discrepan** | — |
| `2015-12` | **Primer corte de suministro eléctrico atribuido a un ciberataque**, con la familia `BlackEnergy` | Ucrania |
| `2016-12` | **Segundo corte de suministro**, con `Industroyer` | Ucrania |
| `2017-06` | **`NotPetya`.** Daño global por propagación no contenida; el ciberataque más costoso registrado | Global |
| `2018-02` | `Olympic Destroyer` | Corea del Sur |
| `2020` | **Acusación federal estadounidense con miembros nombrados**, atribuyéndolos a la unidad de inteligencia militar | — |
| `2022-04` | `Industroyer2` contra una subestación eléctrica ucraniana | Ucrania |
| `2021`–`2024` | **Ventana de actividad del subgrupo de acceso inicial** según una de las fuentes | 15+ países |
| `2024-10` → `2025-03` | Periodo cubierto por el primer informe que documenta `ZEROLOT` | Ucrania |
| `2025-02-12` | **Publicación del análisis del subgrupo de acceso inicial**: operación multianual global cuya función es entregar accesos a otras unidades | Global |
| `2025-04` | **Dos borradores distintos, `ZEROLOT` y `Sting`, contra una universidad ucraniana.** `Sting` se ejecuta desde una tarea programada con nombre en argot ruso | Ucrania |
| `2025-05-19` | Publicación que documenta `ZEROLOT` contra energía ucraniana, **con abuso de la directiva de grupo de Active Directory como vector de distribución** | Ucrania |
| `2025-06` | **Múltiples variantes de borrador contra los sectores gubernamental, energético, logístico y cerealero** | Ucrania |
| `2025-09` | **Segunda oleada contra los mismos cuatro sectores** | Ucrania |
| `2025-09-17` | Fecha que **una** fuente da para un ataque destructivo contra una empresa cerealera. **Conflicto de fechas con el caso de octubre de 2026: véase §3.3-ii** | Ucrania |
| `2025-12` | **Ataque destructivo contra una empresa energética polaca.** Atribución de **confianza media**; una segunda firma lo vincula al mismo conjunto de actividad | **Polonia** |
| `2026-03-06` | Un informe trimestral de otro proveedor sobre ataques a organizaciones industriales recoge y relaya estos hallazgos | — |
| `2026-10` | **Investigación que documenta la entrega de acceso**: `UAC-0099` obtiene el acceso inicial en una empresa cerealera y lo entrega a este actor, que ejecuta el borrado. Puerta trasera en Go `MythicRatatoskr` | Ucrania |
| `2026-10-28` | El informe trimestral Q2–Q3 2026 confirma que los ataques con borrador son **regulares desde principios de 2025**, concentrados en gobierno, energía, logística y grano | Ucrania |
| `2026-11-04` | **El ranking de actividad estatal global de Trellix se publica sin este actor entre los tres primeros**, donde sí figura Gamaredon con el 9,03 % | Global |

## O-6. Hipótesis alternativas consideradas

**Cuestión 1 — ¿Marca el caso polaco una ampliación del perímetro destructivo?**

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| **H1 — Ampliación deliberada del perímetro** | Un objetivo energético en un Estado de la OTAN y de la UE, fuera del teatro. Coherente con la operación de acceso del subgrupo en más de quince países: **si se construyeron accesos globales durante años, en algún momento se usan**. Se retiene con probabilidad moderada | `Retenida · posibilidad real 45–55 %` |
| **H2 — Caso vinculado al apoyo logístico a Ucrania** | Que el objetivo polaco se eligiera por su papel en el corredor de suministro a Ucrania, lo que lo situaría **dentro** del teatro ampliado y no fuera. Es la explicación más económica y **no requiere cambio de doctrina del actor** | `Retenida · posibilidad real 45–55 %` |
| **H3 — Atribución incorrecta** | La propia fuente declara **confianza media**, y la corroboración de la segunda firma se conoce por una sola fuente secundaria. **No se puede descartar**, y es la razón de que `KJ-5` tenga confianza baja | `Retenida · poco probable 20–45 %` |
| **H4 — Preparación de capacidad, no uso de capacidad** | Que el caso polaco fuera una demostración o una prueba de acceso más que una operación con objetivo, en la lógica del prepos. **Sin ninguna evidencia**, se consigna para que no se reabra sin ella | `Poco probable · 20–45 %` |

**Cuestión 2 — ¿Por qué no aparece en las mediciones de prevalencia?**

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| **H5 — Bajo volumen inherente al modelo** | Un borrador se ejecuta una vez por objetivo y después no hay artefacto que detectar repetidamente. Selección estricta, pocos objetivos, efecto terminal. **Es la que se retiene**, y es la inversa de la explicación de `CTI-2026-028` | `Retenida · probable 55–80 %` |
| **H6 — El acceso inicial se cuenta como otro actor** | Si el subgrupo de acceso y los proveedores externos se contabilizan bajo sus propias designaciones, la actividad previa al efecto **no se atribuye a este actor en la telemetría**. Complementaria de H5 y probablemente también cierta | `Retenida como complemento` |
| **H7 — Telemetría concentrada en un teatro sin cobertura comercial** | Que la base instalada de los proveedores que publican rankings esté poco presente en los objetivos de este actor. Plausible pero no verificable sin la metodología (brecha `G-4`) | `Posibilidad real · 45–55 %` |
| **H8 — Actividad real en descenso** | **Descartada.** El informe trimestral de octubre de 2026 afirma expresamente que los ataques con borrador son regulares desde principios de 2025 | `Descartada` |

**Supuesto clave — verificado antes de publicar.** El informe asumía que **la afirmación sobre la directiva de grupo se refiere a la distribución masiva del borrador y no a una técnica de persistencia puntual**. **La verificación previa a la publicación lo confirma**: la fuente declara que los atacantes «abusaron de la directiva de grupo de Active Directory en las organizaciones afectadas» **para desplegar el borrador en los equipos**, y una cobertura cita a la misma fuente diciendo que explota esa característica **de forma transversal en sus campañas de borrado**. Un tercer proveedor, en su informe trimestral sobre organizaciones industriales, lo reproduce con la misma formulación y añade las fechas: **diciembre de 2024, febrero y marzo de 2025**. `KJ-3` queda sostenido por tres fuentes concordantes en lugar de una, y se mantiene en confianza alta con mejor fundamento.

Lo que **sigue sin verificar** es el detalle del mecanismo: si la directiva despliega una tarea programada, un script de inicio o una ejecución inmediata. **Las tres variantes están cubiertas por la detección `D-2`**, de modo que la laguna no afecta a ninguna decisión. Y la decisión `E-a` no dependía del supuesto en ningún caso, lo cual era deliberado.

**Pre-mortem.** Es mayo de 2027 y este informe resultó equivocado. La causa más probable: **convertimos un actor que no nos va a atacar en una excusa para un proyecto de continuidad que llevaba años pendiente.** Si alguien lee §E-2 con atención, verá que el informe dice literalmente que este actor no nos va a atacar, y aun así pide cinco decisiones. **Eso es defendible sólo si las decisiones se justifican por sí mismas** —y lo hacen: respaldos desconectados y control de directivas de grupo son correctos frente a cualquier grupo de extorsión— **pero es indefendible si se venden a Dirección como respuesta a esta amenaza concreta.** Si en 2027 alguien descubre que invertimos en continuidad citando a la inteligencia militar rusa, con razón nos acusará de inflar el riesgo. La formulación honesta está en `KJ-8` y en la lectura clave de §E-2, y hay que mantenerla en toda comunicación posterior. Segunda causa posible: el supuesto clave era falso.

## O-7. Indicadores y señales de alerta

| # | Indicador observable | Qué señalaría | Disciplina | Responsable |
|---|---|---|---|---|
| I-1 | **Segundo caso destructivo documentado fuera del teatro ucraniano** | Convierte `KJ-5` de caso aislado en patrón y confirma H1 de §O-6. Obligaría a reevaluar la exposición de la cadena de suministro europea | OSINT | Célula CTI |
| I-2 | Confirmación o rectificación de la atribución del caso polaco por su autor, o por un tercero independiente | Resuelve H3. Es el punto más débil del expediente | OSINT | Célula CTI |
| I-3 | **Uso de la distribución por directiva de grupo en una campaña de extorsión contra organizaciones de la región** | **Es el único indicador de este informe que cambiaría algo para nosotros.** Convertiría la segunda mitad de `KJ-8` en hecho y elevaría `E-b` a inmediata | OSINT / telemetría | Célula CTI / SOC |
| I-4 | Actividad destructiva dirigida al sector agroalimentario exportador de un país **distinto** de Ucrania | Confirmaría la transferibilidad del razonamiento sectorial de `KJ-4`, que hoy es inferencia nuestra | OSINT | Célula CTI |
| I-5 | Vuelta documentada a efectos sobre sistemas de control industrial | Cambiaría la clase de consecuencia: de pérdida de datos a pérdida de proceso físico. Exigiría producto específico | OSINT | Célula CTI |
| I-6 | Publicación de un análisis técnico de primera mano accesible sobre los borradores de 2025 | Cierra la brecha `G-1`, que es la dominante del informe | OSINT | Célula CTI |
| I-7 | Nueva atribución oficial, sanción o acusación judicial | Relevante para cumplimiento y para la cadena de suministro | OSINT | Legal / Cumplimiento |
| I-8 | Documentación de un tercer proveedor de acceso distinto del subgrupo propio y de `UAC-0099` | Reforzaría `KJ-6` y `KJ-7`, y con ellos la decisión `E-f` | OSINT | Célula CTI |

---

# NIVEL TÁCTICO
### Para: Analistas de SOC · Ingeniería de Detección · Administración de Active Directory · Continuidad · Horizonte: días–semanas

## T-1. Cadena de intrusión

<!-- cti:stages title="Tres fases, dos actores y una ventana que importa" dwell="**Permanencia:** no publicada para la fase destructiva. La fase de acceso del subgrupo se describe como una operación **multianual**, de 2021 a 2024 según una fuente: la ventana de detección puede medirse en meses o años." -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 01 · Acceso — **otro actor** | Intrusión ordinaria, meses o años antes | Subgrupo `BadPilot`, operación multianual en 15+ países · o un grupo externo (`UAC-0099` en el caso cerealero) · puerta trasera en Go `MythicRatatoskr` · **técnicas de intrusión convencionales: aquí está la ventana de detección** |
| Etapa 02 · Entrega y control | Traspaso del acceso y escalada a control de dominio | Entrega del acceso validado a este actor · escalada hasta credenciales con capacidad de escribir directivas de grupo · **no publicada en detalle por ninguna fuente leída** |
| Etapa 03 · Distribución | **Directiva de grupo de Active Directory** | Escritura de una directiva con alcance de dominio · distribución **autorizada, simultánea y silenciosa** a todos los equipos · tarea programada como mecanismo de ejecución local |
| Etapa 04 · Efecto | Borrado | `ZEROLOT` · `Sting` · **utilidad legítima de borrado seguro firmada por Microsoft** · ejecución simultánea, sin propagación, sin movimiento lateral |

**Etapa 01, y es donde hay que invertir.** El actor no obtiene sus propios accesos. Lo hace un subgrupo con una operación de años, o un grupo externo. Las técnicas de esa fase son **las ordinarias**: explotación de servicios expuestos, credenciales, correo dirigido. Nada en ellas grita «inteligencia militar». Para el defensor eso tiene una consecuencia liberadora y una incómoda: **la liberadora es que no hay que detectar una capacidad excepcional, hay que detectar una intrusión corriente**; la incómoda es que si no la detectamos ahora tampoco la detectaríamos entonces.

**Etapa 03, el centro del informe.** Merece desglosarse en lo que el defensor puede observar:

1. **Creación o modificación de un objeto de directiva de grupo.** Es un evento auditable y poco frecuente en un dominio gestionado. Si no se audita, no hay nada.
2. **Vinculación de la directiva a un contenedor con alcance amplio** —el dominio, o una unidad organizativa que abarque la mayoría de los equipos—. Es el paso que convierte una directiva en un arma.
3. **Creación de una tarea programada por directiva, o de un script de inicio**, que es el mecanismo por el que la directiva ejecuta algo.
4. **Replicación de la directiva a los controladores de dominio** y recogida por los clientes.
5. **Ejecución simultánea en todo el parque**, que es el único momento en que un EDR lo verá, y será tarde.

De esos cinco pasos, **los tres primeros son detectables con holgura y los dos últimos no sirven de nada.** Esa es toda la conclusión táctica del informe.

**Etapa 04 y el problema de la herramienta legítima.** Una de las fuentes documenta el uso de **una utilidad de borrado seguro firmada por Microsoft** para la fase destructiva. Es un programa legítimo, con firma válida, cuyo propósito declarado es exactamente borrar datos de forma irrecuperable. Ninguna lista de bloqueo por firma lo detendrá y ningún motivo razonable justifica prohibirlo en abstracto. **Lo que sí es anómalo es su ejecución masiva y simultánea**, y eso es `D-4`.

Y sobre `Sting`: se ejecutaba desde una tarea programada cuyo nombre es una expresión en argot ruso que se traduce aproximadamente como «come un poco de gulash». No es un dato trivial. **Indica que en el momento del despliegue el sigilo había dejado de ser un objetivo**, lo que es coherente con una operación cuyo efecto es inmediato e irreversible: no hay nada que ocultar después.

## T-2. Mapa MITRE ATT&CK

> Construido sobre la conducta documentada en las fuentes leídas y la ficha
> `G0034`. Marco ATT&CK v19. **Se marca con `(inf.)` lo que es inferencia
> nuestra**, y la tabla es deliberadamente más corta que las de los informes
> anteriores del lote: refleja sólo lo que las fuentes de este expediente
> describen, no el historial completo del actor.

<!-- cti:matrix -->

| Táctica | ID | Técnica | Procedimiento observado |
|---|---|---|---|
| Desarrollo de recursos | T1587.001 | Develop Capabilities: Malware | Familias destructivas propias: `ZEROLOT`, `Sting`, y el linaje histórico `NotPetya` / `Industroyer` |
| Desarrollo de recursos | T1588.002 | Obtain Capabilities: Tool | **Utilidad legítima de borrado seguro firmada por Microsoft**, usada como instrumento de destrucción |
| Acceso inicial | T1199 | Trusted Relationship | **Acceso entregado por un subgrupo propio o por un grupo externo.** Es `KJ-6` y la etapa 01 |
| Acceso inicial | T1190 | Exploit Public-Facing Application | Técnica ordinaria del subgrupo de acceso (inf.) |
| Ejecución | T1053.005 | Scheduled Task/Job: Scheduled Task | **`Sting` se ejecuta desde una tarea programada**, con nombre en argot ruso |
| Ejecución | T1059 | Command and Scripting Interpreter | Ejecución de la carga distribuida (inf.) |
| Persistencia | T1484.001 | Domain or Tenant Policy Modification: Group Policy Modification | **La técnica central del expediente.** Escritura de una directiva de grupo para distribuir el borrador a todo el dominio |
| Escalada de privilegios | T1484.001 | Group Policy Modification | La misma técnica, usada también para elevar alcance (inf.) |
| Sigilo | T1036 | Masquerading | Nombre de tarea programada en argot, y uso de una herramienta legítima firmada |
| Degradación de defensas | T1685 | Disable or Modify Tools | Esperable en la fase previa al borrado; **no documentado en detalle en las fuentes leídas** (inf.) |
| Acceso a credenciales | T1003 | OS Credential Dumping | Necesario para alcanzar capacidad de escritura de directivas; **no documentado en estas fuentes** (inf.) |
| Descubrimiento | T1482 | Domain Trust Discovery | Necesario para determinar el alcance de la directiva (inf.) |
| Movimiento lateral | — | **(ninguna)** | **Deliberadamente vacío.** No hay movimiento lateral: hay distribución centralizada autorizada. Es el hallazgo de §O-3 |
| Mando y control | T1071.001 | Application Layer Protocol: Web Protocols | Puerta trasera en Go `MythicRatatoskr` del proveedor de acceso (inf.) |
| **Impacto** | **T1485** | **Data Destruction** | **`ZEROLOT`, `Sting` y la utilidad de borrado seguro.** Es la táctica que define al actor y la única de esta matriz que importa de verdad |
| Impacto | T1561 | Disk Wipe | Linaje histórico (`NotPetya`) y esperable en las familias de 2025 (inf.) |
| Impacto | T1489 | Service Stop | Esperable antes del borrado (inf.) |
| Impacto | T1490 | Inhibit System Recovery | **No documentado en estas fuentes, y es la técnica que más conviene vigilar**: borrado de copias de volumen y de puntos de restauración (inf.) |

> **Observación sobre esta matriz.** Es la más corta del lote y tiene una fila
> vacía a propósito. Nótese dónde está el peso: **una sola técnica de
> persistencia que es también la de distribución (`T1484.001`), y cuatro de
> impacto.** Comparada con las sesenta y tantas técnicas de `CTI-2026-028`, dice
> algo real sobre este actor: **no necesita un arsenal amplio porque no necesita
> permanecer.** Entra con un acceso que le dieron, escribe una directiva y
> destruye. Un adversario con menos de diez técnicas puede ser más consecuente
> que uno con sesenta.

## T-3. Dónde atacamos en la Pirámide del Dolor

<!-- cti:pyramid -->

| Nivel | Qué contiene en este informe y qué vale | Valor |
|---|---|---|
| Hashes | **Ninguno.** Las fuentes leídas no publican hashes de las familias de 2025, y las coberturas secundarias tampoco. **Y aunque los hubiera, servirían de poco**: un borrador se recompila por campaña y el momento en que su hash coincide es el momento en que ya se ejecutó | Base · **inexistente** |
| IP · Dominios | **Ninguno publicado** en las fuentes de este expediente para la fase destructiva. La fase de acceso tiene infraestructura, pero pertenece a otro actor | Valor nulo |
| Artefactos | **El único nivel con contenido**: el nombre de la tarea programada de `Sting` (`DavaniGulyashaSdeshka`), los nombres de familia, y sobre todo **el patrón de una directiva de grupo nueva con alcance de dominio que crea una tarea programada** | Valor medio |
| Herramientas | Directivas de grupo, tareas programadas, **utilidad legítima de borrado seguro**. Todas legítimas y dos de ellas son nuestro propio sistema de administración. **Detectar por contexto y por alcance, nunca por presencia** | Valor alto |
| TTP | La cadena de tres fases de §T-1, y en particular **la distribución por directiva de grupo**. Es lo que el actor no puede cambiar sin renunciar a la simultaneidad, que es su ventaja principal | Cima · valor máximo |

> **Observación de método, y es la conclusión del informe.** Este es el primer
> expediente de la cartera cuyo **Anexo A está esencialmente vacío, y no por un
> defecto de colección.** Contra un actor cuyo efecto es irreversible, un
> indicador de compromiso tiene un problema de oportunidad insalvable: **el
> momento en que coincide es el momento en que ya no sirve.**
>
> Pero hay algo más, y es lo que distingue este informe de `CTI-2026-028`. Allí
> la conclusión era que el esfuerzo debía ir a la conducta y a la configuración.
> **Aquí hay un nivel más que la Pirámide del Dolor no contempla**, porque la
> pirámide mide cuánto le cuesta al adversario que lo detectemos, y contra este
> actor **la pregunta no es cuánto le cuesta ser detectado sino cuánto nos cuesta
> a nosotros que tenga éxito.** Y eso no es una función de la detección: es una
> función de si existe una copia de respaldo que el dominio no pueda alcanzar.
>
> **La respuesta correcta a este expediente no está en la pirámide. Está en la
> decisión `E-a`.**

## T-4. Hipótesis de caza prioritarias

<!-- cti:accordion critical="^(H-1|H-2|H-3)\b" regional="^H-(8|9)\b" -->

**H-1 — Objetos de directiva de grupo creados o modificados fuera de ventana de cambio.** Buscar en el registro de auditoría de Active Directory toda creación, modificación o vinculación de un objeto de directiva de grupo, y contrastarla con el registro de cambios aprobados. Ventana: todo lo disponible, y después en continuo. **Es la hipótesis central del informe.** Fidelidad esperada **muy alta** en un dominio gestionado: la creación de una directiva es un acontecimiento poco frecuente y atribuible a una persona y a un ticket. Falsos positivos: los cambios legítimos de administración, que son precisamente lo que hay que enumerar para saber cuántos son. **Si el resultado de esta caza es «no tenemos ese registro», ése es el hallazgo** y es la decisión `E-b`.

**H-2 — Directiva de grupo que crea una tarea programada o un script de inicio, con alcance amplio.** Más estrecha y más fiable que `H-1`. Enumerar todas las directivas vigentes y marcar las que (a) creen una tarea programada, un script de inicio o de arranque, o una entrada de ejecución inmediata, **y** (b) estén vinculadas al dominio o a una unidad organizativa que abarque más de un porcentaje significativo de los equipos. Ventana: estado actual. Fidelidad **muy alta**: es exactamente el mecanismo de la etapa 03. El inventario resultante es además una pieza útil de higiene que la mayoría de las organizaciones nunca ha hecho.

**H-3 — Ejecución masiva y simultánea de una utilidad de borrado seguro.** Buscar ejecuciones de utilidades de borrado seguro —la de Microsoft y sus equivalentes— y alertar cuando aparezcan **en más de un número pequeño de equipos en una ventana corta**. El criterio no es la herramienta: es la simultaneidad y el volumen. Ventana: continuo, con umbral. Fidelidad **máxima** cuando dispara: no hay escenario legítimo en el que decenas de equipos empiecen a borrar datos de forma irrecuperable a la vez. **Es la última oportunidad de la cadena y hay que automatizar la respuesta**, porque un humano no llega.

**H-4 — Pertenencia a grupos de administración de dominio y su variación.** Enumerar la pertenencia a los grupos con capacidad de escribir directivas de grupo, y alertar ante cualquier incorporación. Responde a `X-3` y `X-5`. Fidelidad **alta**, y el hallazgo más probable no es un compromiso: es descubrir **cuántas cuentas tienen esa capacidad de forma permanente y sin necesitarla**.

**H-5 — Alcanzabilidad de la infraestructura de respaldo desde el dominio.** No es una caza de amenaza: es una **verificación de arquitectura**, y es la más importante del informe. Determinar si las credenciales de dominio, o cualquier credencial obtenible desde el dominio, permiten alcanzar, modificar o borrar las copias de respaldo. Probar activamente, no asumir. Fidelidad no aplicable: **el resultado es un sí o un no, y si es sí hay que cambiarlo.** Responde a `X-1` y es la decisión `E-a`.

**H-6 — Borrado de copias de volumen y de puntos de restauración.** Buscar ejecuciones de utilidades de administración de copias de volumen que borren instantáneas, deshabiliten la recuperación en el arranque o vacíen el catálogo de respaldo. Es la técnica `T1490` de §T-2, que **ninguna fuente de este expediente documenta y que precede a casi todo evento destructivo conocido**, incluidos los de extorsión. Fidelidad **muy alta**, y su valor es mucho mayor que este actor: es la caza que comparte con `CTI-2026-024`.

**H-7 — Intrusión ordinaria de larga permanencia.** La caza que `KJ-7` exige: revisar accesos externos, cuentas con actividad anómala, servicios expuestos comprometidos y persistencias antiguas, con una ventana de **meses**, no de días. **No busca a este actor: busca a quien le abriría la puerta.** Fidelidad moderada y coste alto; es la caza de mayor rendimiento general de todo el lote y la que el presupuesto suele no cubrir.

**H-8 — Dependencia de la cadena agroalimentaria, logística y portuaria.** No es una caza técnica. Determinar qué sistemas propios participan en los procesos de exportación —trazabilidad, cadena de frío, documentación aduanera, programación portuaria— y cuál es su tiempo de recuperación individual. **De valor regional directo** y de ejecución por Operaciones y Riesgo, no por SOC. Es `X-11` y la decisión `E-e`.

**H-9 — Procedimientos manuales de continuidad: ¿existen y alguien los ha probado?** Tampoco es una caza técnica. Verificar si los procesos críticos de negocio tienen procedimiento documentado para operar sin sistemas, y si alguien lo ha ejecutado alguna vez en un simulacro. Responde a `X-8`. **El hallazgo esperado es que existan en papel y nadie los haya probado**, y saberlo vale más que cualquier indicador de este informe.

## T-5. Brechas de visibilidad que hay que cerrar primero

| Brecha | Por qué importa aquí |
|---|---|
| **Sin auditoría de creación y modificación de directivas de grupo** | **Es la brecha dominante.** Deja ciegas `H-1` y `H-2`, es decir, los tres pasos detectables de la etapa 03. No es un problema de producto: es una configuración de auditoría que no se ha activado |
| **Sin inventario de directivas de grupo vigentes y de su alcance** | Deja ciega `H-2`. **Y es una tarea de higiene, no de seguridad**: la mayoría de los dominios acumulan directivas que nadie ha revisado en años |
| **Respaldos alcanzables con credenciales de dominio** | No es una brecha de visibilidad sino de arquitectura, y **es la que decide el resultado**. Deja sin respuesta `H-5` y hace irrelevante todo lo demás si falla |
| **Sin prueba de restauración reciente y documentada** | Deja sin respuesta `X-2` y, con ella, la decisión `E-c`. **Un respaldo que no se ha restaurado nunca es una hipótesis, no un control** |
| Sin registro de pertenencia a grupos administrativos y de su variación | Deja ciega `H-4` |
| Sin detección de borrado de copias de volumen | Deja ciega `H-6`, que es la caza compartida con los expedientes de extorsión y la de mejor relación coste-cobertura |
| Sin umbral de alerta por ejecución simultánea en múltiples equipos | Deja ciega `H-3`. **El criterio es la simultaneidad, y casi ninguna plataforma lo alerta por defecto** |
| Sin capacidad de caza sobre ventanas de meses | Deja ciega `H-7`, que es la única que cubre la etapa 01. La retención de datos suele ser el límite, y es una decisión de coste |
| **Sin procedimientos manuales de continuidad probados** | Deja ciega `H-9`. **No es una brecha de seguridad: es una brecha de negocio**, y es la que determina si la organización sobrevive al escenario que este informe describe |

---

# NIVEL TÉCNICO
### Para: Ingeniería de detección · Administración de Active Directory · **Continuidad y Respaldo** · Vida útil: las detecciones de configuración y de alcance no caducan

## X-1. Arsenal y capacidad

| Propiedad | Valor |
|---|---|
| **Capacidad diferencial** | **Destrucción de datos a escala de dominio, distribuida por el propio mecanismo de administración del parque.** No es sigilo ni persistencia: es simultaneidad |
| Familias destructivas documentadas en 2025 | `ZEROLOT` · `Sting` |
| Herramienta legítima usada para destruir | **Utilidad de borrado seguro firmada por Microsoft.** Firmada, legítima, con propósito declarado de borrar de forma irrecuperable |
| Linaje destructivo histórico | `BlackEnergy` (2015) · `Industroyer` (2016) · `NotPetya` (2017) · `Olympic Destroyer` (2018) · `Industroyer2` (2022) |
| **Vector de distribución** | **Directiva de grupo de Active Directory.** La fuente dice «principalmente mediante la explotación de la característica de directiva de grupo» |
| Mecanismo de ejecución local | Tarea programada. La de `Sting` se llamaba `DavaniGulyashaSdeshka`, expresión en argot ruso |
| Acceso inicial | **No propio.** Subgrupo `BadPilot` (operación multianual en 15+ países) o grupo externo (`UAC-0099`) |
| Puerta trasera del proveedor de acceso | `MythicRatatoskr`, escrita en Go, del caso cerealero de 2026 |
| Movimiento lateral | **Ninguno, por diseño.** La distribución centralizada lo hace innecesario |
| Capacidad sobre sistemas de control industrial | **Demostrada históricamente** con dos familias dirigidas y dos cortes de suministro. Sin actividad nueva documentada en esa línea desde 2022 |
| Capacidad de extorsión o monetización | **Ninguna en doce años**, teniendo capacidad sobrada para ello. Es un argumento de atribución |
| Plataformas | Windows en dominio; sistemas de control industrial en el historial |
| Disciplina operativa | **Deliberadamente baja en la fase destructiva**: el nombre de la tarea programada lo confirma. Cuando el efecto es terminal, el sigilo posterior no tiene valor |

## X-2. Artefactos de host persistentes

> ⚠ **Advertencia.** Esta tabla es la más corta de la cartera y **su brevedad es
> el hallazgo, no un defecto.** Contra un actor cuyo efecto es irreversible, los
> artefactos útiles no son los que deja: son **los cambios de configuración que
> hace antes**, y están en la tabla de abajo marcados como patrón.

<!-- cti:cards -->

| Categoría | Artefactos | Etiqueta |
|---|---|---|
| Nombre de tarea programada observado | `DavaniGulyashaSdeshka` — mecanismo de ejecución de `Sting`. Expresión en argot ruso. **Literal, y por tanto rotable** | `ejecución` |
| **Patrón de distribución (no rotable)** | **Objeto de directiva de grupo nuevo o modificado, vinculado al dominio o a una unidad organizativa de alcance amplio, que crea una tarea programada, un script de inicio o una ejecución inmediata** | `vector` |
| Patrón de ejecución (no rotable) | **Ejecución de una utilidad de borrado seguro en múltiples equipos dentro de una ventana corta.** El indicador es la simultaneidad y el volumen, nunca la herramienta | `impacto` |
| Patrón previo al borrado | Borrado de copias de volumen, deshabilitación de la recuperación en el arranque, vaciado del catálogo de respaldo. **No documentado en estas fuentes; se incluye porque precede a casi todo evento destructivo conocido** | `preparación` |
| Familias | `ZEROLOT` · `Sting` · (histórico) `NotPetya` · `Industroyer` · `Industroyer2` · `BlackEnergy` · `Olympic Destroyer` | `arsenal` |
| Artefacto del proveedor de acceso | `MythicRatatoskr`, puerta trasera en Go. **Pertenece a otro actor y es, por `KJ-7`, el artefacto más útil de la tabla** | `acceso` |

## X-3. Lógica de detección prioritaria

> ⚠ **Advertencia previa, y es la que define este §X-3.** Las cuatro
> detecciones que siguen son **de cambio de configuración y de alcance**, no de
> malware. Ninguna requiere un indicador del actor y ninguna caduca. Y la más
> importante de este informe **no es una detección**: es la verificación de
> arquitectura de `D-0`, que no se despliega en ninguna plataforma porque se
> comprueba una vez y se arregla.

<!-- cti:detections -->

**D-0 · CRÍTICO — Verificación de arquitectura: ¿puede el dominio alcanzar los respaldos?**

```
// NO es una regla de detección. Es una verificación que se ejecuta una vez,
// se documenta, y si el resultado es afirmativo se CORRIGE.
PARA cada repositorio de respaldo de sistemas críticos:
    ¿Es alcanzable por red desde el dominio?                       → sí / no
    ¿Admite autenticación con credenciales de dominio?             → sí / no
    ¿Puede una cuenta de administración de dominio borrar o cifrar
      su contenido, o alterar su política de retención?            → sí / no
    ¿Existe una copia inmutable o desconectada fuera de ese alcance? → sí / no
    ¿Cuándo se restauró por última vez, y cuánto tardó?            → fecha / duración

SI alguna de las tres primeras es "sí" Y la cuarta es "no":
    → la organización no tiene defensa frente al escenario de este informe,
      con independencia de cuántas reglas tenga desplegadas.
```

→ **Es la decisión `E-a` y la hipótesis `H-5`.** Se incluye en el §X-3 y con prioridad crítica deliberadamente, para que no se lea como una recomendación de buenas prácticas sino como **el control que determina el resultado**. Todo lo demás de esta sección reduce la probabilidad; sólo esto reduce la consecuencia.

**D-1 · CRÍTICO — Objeto de directiva de grupo creado, modificado o vinculado**

```
event.code IN ( 5136, 5137, 5141 )        # Modificación, creación y borrado de objeto de directorio
AND winlog.event_data.ObjectClass == "groupPolicyContainer"
AND NOT dentro_de( ventana de cambio aprobada )
```

```
// Complemento por alcance, que es lo que convierte una directiva en un arma:
event.code == 5136
AND winlog.event_data.AttributeLDAPDisplayName == "gPLink"
AND winlog.event_data.ObjectDN MATCHES_REGEX "(?i)^(DC=|OU=)"
```

→ **Investigación inmediata, con notificación directa a la administración de Active Directory y al SOC en paralelo.** La segunda condición es la valiosa: detecta el momento en que una directiva se **vincula** a un contenedor amplio, que es el paso que le da alcance de dominio. Requiere auditoría de acceso al servicio de directorio activada, que es la brecha dominante de §T-5.

**D-2 · CRÍTICO — Directiva de grupo que despliega una tarea programada o un script, con alcance amplio**

```
// Inventario periódico, no evento. Se ejecuta como comprobación programada.
PARA cada objeto de directiva de grupo del dominio:
    despliega_ejecucion = ( contiene Preferencias de tareas programadas
                            OR contiene Scripts de inicio o de arranque
                            OR contiene Ejecución inmediata )
    alcance_amplio      = ( vinculado a DC=  OR  cubre > 25 % de los equipos )
    SI despliega_ejecucion AND alcance_amplio
       AND NOT en la lista de directivas autorizadas:
        → ALERTA CRÍTICA
```

→ Investigación inmediata. **Es la firma de la etapa 03 y la hipótesis `H-2`.** Requiere la lista de directivas autorizadas, que no existe en la mayoría de las organizaciones y cuya construcción es el entregable real de esta regla.

**D-3 · CRÍTICO — Ejecución simultánea de una utilidad de borrado seguro en múltiples equipos**

```
process.name IN_CASE_INSENSITIVE ( "sdelete.exe", "sdelete64.exe",
                                   "cipher.exe", "eraser.exe", "shred" )
AND ( process.command_line MATCHES_REGEX "(?i)\\s-p\\s|\\s/w\\b|\\s-s\\b|\\s-z\\b" )
```

```
// La condición que de verdad discrimina: simultaneidad y volumen.
AGREGAR POR ventana de 15 minutos:
    SI COUNT( DISTINCT host ) con la condición anterior >= 5
       → ALERTA CRÍTICA con contención automática
```

→ **Contención automática sin escalado humano: aislar todos los equipos afectados y detener la distribución de directivas.** No existe ningún escenario legítimo en el que cinco equipos o más empiecen a sobrescribir datos de forma irrecuperable en la misma ventana de quince minutos. **Y es la última oportunidad de la cadena**: un analista humano no llega a tiempo, de modo que la automatización no es una preferencia sino un requisito.

**D-4 · CRÍTICO — Inhibición de la recuperación del sistema**

```
process.command_line MATCHES_REGEX
  "(?i)(vssadmin\\s+delete\\s+shadows"
  "|wmic\\s+shadowcopy\\s+delete"
  "|bcdedit\\s+.*(recoveryenabled\\s+no|bootstatuspolicy\\s+ignoreallfailures)"
  "|wbadmin\\s+delete\\s+(catalog|systemstatebackup)"
  "|Remove-Item.*\\\\System Volume Information)"
```

→ Contención automática. **Esta detección no es específica de este actor y ahí está su valor**: precede a prácticamente todo evento destructivo conocido, incluidos los de extorsión del resto de la cartera. Si sólo se despliega una regla de este informe y `D-0` ya está resuelto, que sea ésta.

**D-5 · ALTO — Incorporación a grupos con capacidad de escritura de directivas**

```
event.code IN ( 4728, 4732, 4756 )
AND winlog.event_data.TargetUserName IN (
      "Domain Admins", "Enterprise Admins", "Group Policy Creator Owners",
      "Administradores del dominio", "Administradores de empresa",
      "Propietarios del creador de directivas de grupo" )
AND NOT dentro_de( ventana de cambio aprobada )
```

→ Investigación prioritaria con plazo de una hora. Cubre el paso de la etapa 02 que las fuentes no documentan y que es imprescindible para llegar a la etapa 03.

**D-6 · MEDIO — Tarea programada con nombre no inventariado desplegada por directiva**

```
event.code == 4698                        # Tarea programada creada
AND winlog.event_data.TaskName NOT IN ( <inventario de tareas autorizadas> )
AND ( process.parent.name == "svchost.exe" OR origen == "group policy" )
```

```
// Variante por indicador literal, de cobertura mínima:
winlog.event_data.TaskName CONTAINS_CASE_INSENSITIVE "DavaniGulyashaSdeshka"
```

→ Investigación en el día para la primera variante; contención automática para la segunda. **La segunda es un indicador literal y caducará**: se incluye porque mientras sirva es concluyente, y porque ilustra la diferencia entre un indicador y un patrón.

> ⚠ **Regla de operación, y es distinta de todas las anteriores de este lote.**
> En los cinco informes previos, la advertencia era sobre listas de excepción y
> brechas de visibilidad. Aquí es sobre **el orden de las cosas**.
>
> `D-0` no es una detección y va primero a propósito. Las reglas `D-1` a `D-6`
> reducen la **probabilidad** de que el escenario ocurra; `D-0` reduce su
> **consecuencia**. Y contra un adversario cuyo efecto es irreversible, **la
> consecuencia es la única variable que admite garantía**: una copia desconectada
> funciona aunque todas las reglas fallen, mientras que ninguna combinación de
> reglas funciona si la copia no existe.
>
> Dicho de otro modo: si hay que elegir entre desplegar este §X-3 y resolver
> `D-0`, **la respuesta correcta es `D-0`**, y es la primera vez que esta cartera
> recomienda no desplegar sus propias detecciones.

## X-4. Consultas de caza

```kql
// H-1 · Objetos de directiva de grupo creados, modificados o vinculados.
// La consulta central del informe. Requiere auditoria de acceso al servicio de directorio.
let VentanasDeCambio = datatable(Inicio: datetime, Fin: datetime, Ticket: string)
    [ datetime(2026-11-01 02:00), datetime(2026-11-01 06:00), "CHG-0001" ];
SecurityEvent
| where EventID in (5136, 5137, 5141)
| where ObjectClass == "groupPolicyContainer" or AttributeLDAPDisplayName in ("gPLink","gPCFileSysPath","versionNumber")
| extend AlcanceAmplio = ObjectDN matches regex @"(?i)^(DC=|OU=)"
| join kind=leftanti ( VentanasDeCambio | project Inicio, Fin ) on $left.TimeGenerated == $right.Inicio
| project TimeGenerated, Computer, SubjectUserName, SubjectDomainName,
          EventID, ObjectDN, AttributeLDAPDisplayName, AttributeValue, AlcanceAmplio
| order by AlcanceAmplio desc, TimeGenerated desc
```

```powershell
# H-2 · Inventario de directivas de grupo que despliegan ejecucion, con su alcance.
# Ejecutar con permisos de lectura de directivas. El resultado ES el entregable:
# la lista de directivas autorizadas que la regla D-2 necesita y que no existe.
Import-Module GroupPolicy

$total = (Get-ADComputer -Filter * -ErrorAction SilentlyContinue).Count
if (-not $total) { $total = 1 }

Get-GPO -All | ForEach-Object {
    $gpo = $_
    [xml]$rep = Get-GPOReport -Guid $gpo.Id -ReportType Xml

    # Despliega ejecucion?
    $tareas   = $rep.SelectNodes("//*[local-name()='ScheduledTasks']").Count
    $scripts  = $rep.SelectNodes("//*[local-name()='Script']").Count
    $inmediata= ($rep.InnerXml -match 'ImmediateTaskV2|ImmediateTask')

    # Alcance: a que esta vinculada
    $enlaces  = $rep.SelectNodes("//*[local-name()='LinksTo']") |
                ForEach-Object { $_.SOMPath }
    $alDominio = $enlaces | Where-Object { $_ -notmatch '/' }   # vinculo a la raiz

    if (($tareas -gt 0 -or $scripts -gt 0 -or $inmediata) ) {
        [pscustomobject]@{
            Nombre        = $gpo.DisplayName
            Guid          = $gpo.Id
            Creada        = $gpo.CreationTime
            Modificada    = $gpo.ModificationTime
            Propietario   = $gpo.Owner
            TareasProg    = $tareas
            Scripts       = $scripts
            TareaInmediata= [bool]$inmediata
            VinculadaRaiz = [bool]$alDominio
            Enlaces       = ($enlaces -join '; ')
            RIESGO        = if ($alDominio) { 'ALTO - ejecucion con alcance de dominio' }
                            else { 'revisar alcance' }
        }
    }
} | Sort-Object VinculadaRaiz -Descending | Format-Table -AutoSize
```

```kql
// H-3 · Ejecucion simultanea de utilidades de borrado seguro.
// El criterio es la SIMULTANEIDAD y el VOLUMEN, no la herramienta.
let Borradores = dynamic(["sdelete.exe","sdelete64.exe","cipher.exe","eraser.exe","shred"]);
DeviceProcessEvents
| where FileName in~ (Borradores)
| where ProcessCommandLine matches regex @"(?i)\s-p\s|\s/w\b|\s-s\b|\s-z\b"
     or FileName in~ ("sdelete.exe","sdelete64.exe")
| summarize Equipos = dcount(DeviceName), Ejecuciones = count(),
            Muestra = make_set(DeviceName, 20),
            Lineas  = make_set(ProcessCommandLine, 5)
          by Ventana = bin(Timestamp, 15m), FileName
| where Equipos >= 5
| order by Ventana desc
```

```kql
// H-6 · Inhibicion de la recuperacion del sistema.
// No es especifica de este actor: precede a casi todo evento destructivo conocido.
DeviceProcessEvents
| where ProcessCommandLine matches regex @"(?i)(vssadmin\s+delete\s+shadows|wmic\s+shadowcopy\s+delete|bcdedit\s+.*(recoveryenabled\s+no|bootstatuspolicy\s+ignoreallfailures)|wbadmin\s+delete\s+(catalog|systemstatebackup))"
| summarize Equipos = dcount(DeviceName), Primero = min(Timestamp), Ultimo = max(Timestamp),
            Lineas = make_set(ProcessCommandLine, 10)
          by bin(Timestamp, 1h)
| order by Equipos desc
```

```kql
// H-4 y H-7 · Incorporaciones a grupos administrativos, y accesos de larga permanencia.
union
( SecurityEvent
  | where EventID in (4728, 4732, 4756)
  | where TargetUserName has_any ("Domain Admins","Enterprise Admins",
          "Group Policy Creator Owners","Administradores del dominio")
  | project TimeGenerated, Señal = "grupo-administrativo",
            Detalle = strcat(MemberName, " -> ", TargetUserName),
            Actor = SubjectUserName ),
( SigninLogs
  | where ResultType == 0
  | summarize Primero = min(TimeGenerated), Ultimo = max(TimeGenerated),
              Dias = dcount(bin(TimeGenerated, 1d))
            by UserPrincipalName, IPAddress
  | where Dias > 30 and Primero < ago(60d)
  | project TimeGenerated = Ultimo, Señal = "acceso-larga-permanencia",
            Detalle = strcat(IPAddress, " durante ", tostring(Dias), " dias"),
            Actor = UserPrincipalName )
| order by TimeGenerated desc
```

```yaml
# Sigma — Objeto de directiva de grupo vinculado a un contenedor de alcance amplio
# Autor: Célula CTI · Fecha: 2026-11-17 · ATT&CK: T1484.001
# Nivel: critical · Estado: estable
# Es el paso que convierte una directiva de grupo en un mecanismo de distribucion masiva.
title: Vinculacion de directiva de grupo al dominio o a una unidad organizativa amplia
id: 8f3c1a62-5d47-4b09-93e8-1a7b6c04f2d5
status: stable
description: >
  Sandworm distribuyo sus borradores de datos principalmente mediante la
  caracteristica de directiva de grupo de Active Directory. El momento
  detectable no es la ejecucion del borrado, que es simultanea y tardia, sino la
  escritura y la vinculacion de la directiva que lo reparte.
references:
  - https://www.eset.com/us/about/newsroom/research/eset-research-apt-report-russian-cyberattacks-in-ukraine-intensify-sandworm-unleashes-new-destructive-wiper/
logsource:
  product: windows
  service: security
detection:
  seleccion:
    EventID: 5136
    AttributeLDAPDisplayName: 'gPLink'
  alcance:
    ObjectDN|startswith:
      - 'DC='
      - 'OU='
  condition: seleccion and alcance
falsepositives:
  - Cambios legitimos de administracion de directivas. DEBEN estar en una ventana
    de cambio aprobada; enumerarlos es el objetivo de la regla.
level: critical
```

```yaml
# Sigma — Ejecucion de utilidad de borrado seguro
# Autor: Célula CTI · Fecha: 2026-11-17 · ATT&CK: T1485, T1561
# Nivel: high · Estado: estable
# La correlacion por simultaneidad (>=5 equipos en 15 min) eleva esto a critico y
# debe hacerse en el SIEM: una sola ejecucion puede ser legitima.
title: Utilidad de borrado seguro ejecutada con opciones de sobrescritura
id: c05e7b94-2f18-4a63-8de1-6b94a3c710ef
status: stable
description: >
  Sandworm empleo una utilidad legitima de borrado seguro firmada por Microsoft
  como instrumento de destruccion, junto a sus propias familias ZEROLOT y Sting.
  Una herramienta firmada no se detiene por firma: el indicador es el contexto,
  y sobre todo la simultaneidad en multiples equipos.
logsource:
  category: process_creation
  product: windows
detection:
  seleccion_herramienta:
    Image|endswith:
      - '\sdelete.exe'
      - '\sdelete64.exe'
      - '\eraser.exe'
  seleccion_cipher:
    Image|endswith: '\cipher.exe'
    CommandLine|contains: '/w'
  condition: seleccion_herramienta or seleccion_cipher
falsepositives:
  - Retirada autorizada de equipos y procedimientos de borrado seguro de soportes.
    Deben tener ticket. Correlacionar por numero de equipos antes de escalar.
level: high
```

```yaml
# Sigma — Inhibicion de la recuperacion del sistema
# Autor: Célula CTI · Fecha: 2026-11-17 · ATT&CK: T1490
# Nivel: critical · Estado: estable
# No es especifica de Sandworm: precede a casi todo evento destructivo conocido,
# incluidos los de extorsion del resto de esta cartera.
title: Borrado de copias de volumen o deshabilitacion de la recuperacion
id: 1b7d4f80-6c29-45ae-b3f7-0d82e5a91c46
status: stable
description: >
  Paso previo habitual a un evento destructivo: eliminar las instantaneas de
  volumen, vaciar el catalogo de respaldo o deshabilitar la recuperacion en el
  arranque, para que la restauracion local sea imposible.
logsource:
  category: process_creation
  product: windows
detection:
  vssadmin:
    CommandLine|contains|all:
      - 'vssadmin'
      - 'delete'
      - 'shadows'
  wmic:
    CommandLine|contains|all:
      - 'shadowcopy'
      - 'delete'
  bcdedit:
    CommandLine|contains: 'bcdedit'
    CommandLine|contains:
      - 'recoveryenabled no'
      - 'bootstatuspolicy ignoreallfailures'
  wbadmin:
    CommandLine|contains|all:
      - 'wbadmin'
      - 'delete'
  condition: vssadmin or wmic or bcdedit or wbadmin
falsepositives:
  - Mantenimiento de almacenamiento con ticket aprobado. Infrecuente.
level: critical
```

## X-5. Mitigaciones de configuración con efecto directo

| Control | Corta |
|---|---|
| **Copia de respaldo desconectada o inmutable, inalcanzable con credenciales de dominio** | **No corta nada: cambia el resultado.** Es el único control de este informe que funciona aunque todos los demás fallen. Decisión `E-a` |
| **Prueba de restauración real, con duración registrada y fecha de caducidad** | Convierte el respaldo de hipótesis en control. **Un respaldo no probado no es un respaldo** |
| **Restringir la pertenencia a los grupos con capacidad de escribir directivas de grupo**, y eliminar la permanencia | La etapa 02: sin esa capacidad, la etapa 03 no existe |
| **Auditoría de acceso al servicio de directorio activada**, con alerta inmediata sobre objetos de directiva | Hace detectables los tres pasos útiles de la etapa 03. **Es configuración, no producto** |
| **Separación por niveles de la administración de Active Directory**, con estaciones de administración dedicadas | El puente entre un acceso ordinario (etapa 01) y el control del dominio (etapa 02). Decisión `E-d` |
| **Inventario y revisión periódica de las directivas de grupo vigentes y de su alcance** | Hace operable `D-2`, y de paso retira directivas acumuladas que nadie revisa |
| **Controladores de dominio y infraestructura de respaldo en dominios de fallo distintos** | Que un compromiso de dominio no alcance el mecanismo de recuperación. Es `X-12` |
| **Restringir la ejecución de utilidades de borrado seguro** a cuentas y equipos concretos | La etapa 04 en su variante con herramienta legítima |
| **Bloquear por política el borrado de copias de volumen** y la deshabilitación de la recuperación en el arranque | El paso preparatorio de `D-4`, común a este actor y a todos los de extorsión de la cartera |
| **Procedimientos manuales de continuidad documentados y probados en simulacro** | No es un control informático. **Es lo que determina si la organización opera el día siguiente**, y es `H-9` |
| Autenticación multifactor y vigilancia reforzada en todo acceso remoto y servicio expuesto | La etapa 01, que es la única con ventana de detección larga (`KJ-7`, decisión `E-f`) |

---

## 14. Brechas de inteligencia y nuevos requisitos de colección

| # | Brecha | Impacto en el juicio | Requisito propuesto | Prioridad |
|---|---|---|---|---|
| G-1 | **Ninguna fuente primaria se leyó íntegra; el análisis de los borradores de 2025 se conoce por notas de prensa y coberturas** | **Es la brecha dominante.** El supuesto clave de §O-6 —que la directiva de grupo es el vector de distribución masiva y no un mecanismo secundario— no está verificado contra el análisis técnico. De él depende `KJ-3` y la prioridad de `E-b` | Obtener los informes técnicos completos del proveedor. Indicador `I-6` | **Crítica** |
| G-2 | **Sin respuesta a la pregunta de recuperación propia** | §O-4 sin evaluar, y con él la decisión `E-c`. **No es una brecha de inteligencia: es un ejercicio de continuidad que no se ha hecho** | Ejecutar `D-0`, `H-5`, `H-9` y responder `X-7` por escrito | **Crítica** |
| G-3 | **Atribución del caso polaco con confianza media y corroboración por fuente secundaria única** | `KJ-5` queda en confianza baja. Es el juicio con mayor consecuencia estratégica y el peor sostenido del informe | Localizar el análisis original y la publicación de la segunda firma. Indicador `I-2` | Alta |
| G-4 | No se pudo leer la metodología de los rankings de prevalencia | **Quinta aparición de la misma limitación en este lote.** Afecta a H7 de §O-6 y a la formulación final de `KJ-9` | Obtener los informes completos por vía comercial o institucional | Alta |
| G-5 | **Conflicto de fechas sin resolver en el caso cerealero** (septiembre de 2025 frente a octubre de 2026) | No se puede determinar si son un caso con publicación tardía o dos casos distintos, lo que afecta al recuento de episodios de §E-3 | Localizar el análisis original de la entrega de acceso | Media |
| G-6 | **Detalle de la etapa 02**: cómo se pasa del acceso entregado al control del dominio | Ninguna fuente lo documenta. **Es el tramo de la cadena donde una detección sería más útil y donde no tenemos nada** | Buscar análisis de respuesta a incidentes publicados sobre casos concretos | Alta |
| G-7 | Ausencia de hashes y de infraestructura publicados para las familias de 2025 | Ninguno en los juicios. **Y el Anexo A lo declara como propiedad del expediente, no como carencia** (§T-3) | Ninguno prioritario. Si aparecen, su uso será de retrohunt | Baja |
| G-8 | **Transferibilidad del razonamiento sectorial de `KJ-4` a la economía exportadora chilena** | `KJ-8` es inferencia nuestra y es el juicio con mayor valor práctico del informe | **Requisito de colección permanente**: vigilar actividad destructiva contra sectores agroalimentarios exportadores en cualquier geografía. Indicador `I-4` | Alta |
| G-9 | **Difusión de la técnica de directiva de grupo a actores de extorsión** | Es la segunda mitad de `KJ-8` y lo único de este informe que probablemente nos afecte | **Requisito de colección permanente**: vigilar informes de extorsión en busca de distribución por directiva de grupo. Indicador `I-3` | **Crítica** |
| G-10 | Delimitación del organigrama del actor entre designaciones de distintos proveedores | Ninguno en las decisiones. Pero afecta a cómo se debe redactar una atribución: **especificando a qué fase se refiere** (§O-2) | Ninguno. Se consigna como advertencia de redacción | Baja |

---

# ANEXOS

## Anexo A — Indicadores de compromiso

> ⚠ **LEER PRIMERO. Este anexo es, deliberadamente, el más corto y el menos
> importante de los seis informes de esta cartera, y su brevedad no es un
> defecto de colección: es el hallazgo.**
>
> Contra un actor cuyo efecto es irreversible, **un indicador de compromiso
> tiene un problema de oportunidad insalvable: el momento en que coincide es el
> momento en que ya no sirve.** Si un hash de `ZEROLOT` aparece en nuestro
> parque, el borrado ya se ejecutó. No hay contención posible, sólo restauración.
>
> Por eso el contenido útil de este informe está en §X-3 —y en particular en
> `D-0`, que no es una detección sino una verificación de arquitectura— y en §X-5.
> **Si alguien sólo tiene tiempo de leer una sección, que no sea ésta.**
>
> Lo que sigue son, en este orden: **patrones de conducta y de configuración**,
> que no caducan y son el producto real; y después los pocos **indicadores
> literales** que las fuentes publican, con su caducidad declarada.

### A.1 — Patrones de conducta y de configuración (el producto real de este informe)

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| pattern | `objeto de directiva de grupo creado o modificado fuera de ventana de cambio aprobada` | **El vector de distribución del actor.** Es el primero de los tres pasos detectables de la etapa 03 | Alta | **Sin caducidad** | Detección (`D-1`, `H-1`) |
| pattern | `vinculación de una directiva de grupo a DC= o a una unidad organizativa de alcance amplio` | **El paso que convierte una directiva en un mecanismo de distribución masiva.** El más discriminante de los tres | Alta | **Sin caducidad** | Detección (`D-1`, `H-2`) |
| pattern | `directiva de grupo que despliega una tarea programada, un script de inicio o una ejecución inmediata, con alcance amplio` | La firma completa de la etapa 03. Requiere inventario de directivas autorizadas | Alta | **Sin caducidad** | Detección (`D-2`, `H-2`) |
| pattern | `ejecución de una utilidad de borrado seguro en 5 o más equipos en una ventana de 15 minutos` | **La última oportunidad de la cadena.** El criterio es la simultaneidad y el volumen, nunca la herramienta. Exige respuesta automática: un analista no llega | Alta | **Sin caducidad** | **Contención automática** (`D-3`, `H-3`) |
| pattern | `borrado de copias de volumen, vaciado del catálogo de respaldo o deshabilitación de la recuperación en el arranque` | Paso preparatorio. **No documentado en las fuentes de este expediente**; se incluye porque precede a casi todo evento destructivo conocido, incluidos los de extorsión de `CTI-2026-024` | Alta | **Sin caducidad** | **Contención automática** (`D-4`, `H-6`) |
| pattern | `incorporación a Domain Admins, Enterprise Admins o Group Policy Creator Owners fuera de ventana de cambio` | El paso de la etapa 02 que las fuentes no documentan y que es condición necesaria de la etapa 03 | Alta | **Sin caducidad** | Detección (`D-5`, `H-4`) |
| artefacto | `respaldo alcanzable con credenciales de dominio y sin copia inmutable o desconectada` | **No es un indicador de compromiso: es la condición que determina el resultado.** Es `D-0`, la hipótesis `H-5` y la decisión `E-a` | Alta | **Sin caducidad** | **Verificación de arquitectura y corrección** |
| artefacto | `ausencia de prueba de restauración documentada en los últimos doce meses` | Un respaldo no probado es una hipótesis. Es `X-2` y la decisión `E-c` | Alta | **Sin caducidad** | **Verificación y corrección** |
| artefacto | `ausencia de procedimientos manuales de continuidad probados en simulacro` | Determina si la organización opera el día siguiente. Es `H-9` y no es materia de seguridad informática | Alta | **Sin caducidad** | **Verificación y corrección** |

### A.2 — Indicadores literales (pocos, y con caducidad declarada)

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| artefacto | `DavaniGulyashaSdeshka` | **Nombre de la tarea programada desde la que se ejecutó el borrador `Sting`** en abril de 2025. Expresión en argot ruso que se traduce aproximadamente como «come un poco de gulash». **Literal y por tanto rotable**, pero mientras sirva es concluyente | Alta | 2027-04-30 | Bloqueo por detección (`D-6`) |
| herramienta | `ZEROLOT` | Borrador de datos documentado por primera vez en mayo de 2025, desplegado contra energía ucraniana **y distribuido por directiva de grupo**. Despliegues situados en **diciembre de 2024, febrero y marzo de 2025**. **Las fuentes leídas no publican su hash** | Alta | Sin caducidad | Caza por nombre de familia |
| pattern | `borrado de todo el contenido de C:\Users\ y de la raíz de todas las unidades lógicas salvo C:, omitiendo los ficheros .dll, .exe y .sys` | **Comportamiento de `ZEROLOT`, documentado en la verificación previa a la publicación.** Omitir ejecutables y bibliotecas es deliberado: **deja el sistema arrancable y vacío de datos**, que para la recuperación es peor que un equipo que no arranca, porque no hay señal evidente de fallo | Media | Sin caducidad | Detección por patrón de borrado masivo |
| herramienta | `SwiftSlicer` | Borrador anterior del mismo actor que **también se distribuyó por directiva de grupo**. Confirma que el vector no es circunstancial de `ZEROLOT` | Media | Sin caducidad | Caza por nombre de familia |
| herramienta | `Sting` | Segundo borrador, desplegado junto a `ZEROLOT` contra una universidad ucraniana en abril de 2025 | Alta | Sin caducidad | Caza por nombre de familia |
| herramienta | `MythicRatatoskr` | **Puerta trasera en Go del proveedor de acceso** (`UAC-0099`) en el caso cerealero de 2026. **Pertenece a otro actor, y por `KJ-7` es el artefacto más útil de este anexo**: es el que aparece meses antes | Media | Sin caducidad | Caza — **atribuir a `UAC-0099`, no a este actor** |
| herramienta | `NotPetya` · `Industroyer` · `Industroyer2` · `BlackEnergy` · `Olympic Destroyer` | Linaje destructivo histórico. **Valor exclusivamente contextual**: ninguna de estas familias es una amenaza vigente en su forma original | Alta | Sin caducidad | Contexto — no detección |
| cve | `(ninguno)` | **Este actor no tiene ningún CVE propio documentado en el expediente.** No necesita explotar nada: el acceso lo recibe y la distribución es autorizada. **Es el único informe de este lote sin una sola vulnerabilidad que parchear**, y conviene notarlo | Alta | — | — |

### A.3 — Herramientas legítimas implicadas · **NO BLOQUEAR POR PRESENCIA**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| herramienta | `directiva de grupo de Active Directory` | **El vector de distribución del actor es nuestro propio mecanismo de administración de parque.** No se puede retirar: sin directivas de grupo no hay administración. **Lo que se controla es quién escribe en ella** | Alta | Sin caducidad | **No bloquear.** Restringir escritura y auditar (`E-b`, `D-1`) |
| herramienta | `utilidad de borrado seguro firmada por Microsoft` | Programa legítimo, con firma válida y propósito declarado de borrar de forma irrecuperable. **Ninguna lista por firma la detendrá.** Lo anómalo es la ejecución masiva y simultánea | Alta | Sin caducidad | **No bloquear por presencia.** Restringir a cuentas y equipos concretos; detectar por simultaneidad (`D-3`) |
| herramienta | `tareas programadas` | Mecanismo de ejecución local. Componente del sistema | Alta | Sin caducidad | **No bloquear.** Inventariar y detectar lo no inventariado (`D-6`) |
| herramienta | `vssadmin` · `wmic` · `bcdedit` · `wbadmin` · `cipher` | Utilidades de administración de almacenamiento y de arranque. **El indicador es el argumento, no el binario** | Alta | Sin caducidad | **No bloquear.** Detectar por línea de comandos (`D-4`) |

## Anexo B — Fuentes y valoración

| # | Fuente | Disciplina | Fiab. | Cred. | Notas de sesgo |
|---|---|---|---|---|---|
| 1 | ESET, nota de investigación sobre el borrador `ZEROLOT` y el abuso de la directiva de grupo, **2025-05-19**, cubriendo octubre de 2024 a marzo de 2025 — **leída por nota de prensa y coberturas, no en original** | OSINT comercial de primera mano, vía secundaria | **B** | **2** | **Fuente de `KJ-3`, el juicio técnico central del informe.** La afirmación sobre el vector de distribución aparece de forma coincidente en varias coberturas que la atribuyen literalmente. **El análisis técnico íntegro no se leyó**, y de ello depende el supuesto clave de §O-6. Brecha `G-1` |
| 2 | ESET, informe de actividad de actores persistentes avanzados Q2–Q3 2025, cubriendo abril a septiembre de 2025 — **leído por coberturas** | OSINT comercial de primera mano, vía secundaria | **B** | **2** | Fuente de `KJ-2`: los dos borradores contra la universidad en abril, el nombre de la tarea programada, y las dos oleadas de junio y septiembre contra los **cuatro sectores**. Varias coberturas independientes concuerdan en el detalle, incluido el nombre en argot |
| 3 | ESET, informe de actividad Q2–Q3 2026, **2026-10-28** — leído en su versión de artículo en el marco de `CTI-2026-025` | OSINT comercial de primera mano | **B** | **2** | Confirma que los ataques con borrador son **regulares desde principios de 2025** y acota los sectores. Es la única fuente de 2026 que establece continuidad de actividad |
| 4 | ESET, investigación sobre la entrega de acceso de `UAC-0099` a este actor en una empresa cerealera, **octubre de 2026** — leída por coberturas | OSINT comercial de primera mano, vía secundaria | **B** | **3** | Fuente de la mitad externa de `KJ-6` y de `MythicRatatoskr`. **Credibilidad 3 por el conflicto de fechas de `G-5`**: una cobertura sitúa el ataque destructivo el 2025-09-17, lo que no cuadra con una publicación de octubre de 2026 |
| 5 | Microsoft, análisis del subgrupo de acceso inicial `BadPilot`, **2025-02-12** — **leída por coberturas secundarias únicamente** | OSINT comercial de primera mano, vía secundaria | **B** | **3** | Fuente de la mitad interna de `KJ-6` y de la cifra de más de quince países. **No se leyó la publicación original**, y las coberturas difieren en la ventana de actividad del subgrupo (una da 2021–2024). Credibilidad 3 por la vía |
| 6 | MITRE ATT&CK, ficha de grupo `G0034` | OSINT de marco | **B** | **2** | Base de la tabla de alias y del contexto histórico. Las fuentes que la citan discrepan sobre el año de inicio (2009 frente a 2013) |
| 7 | Acusación federal estadounidense de 2020 contra miembros nombrados del actor — **por vía secundaria** | **OSINT judicial**, vía secundaria | **B** | **2** | **La pieza que hace de ésta una de las dos atribuciones más sólidas de la cartera.** No se leyó el documento original |
| 8 | Dragos, vinculación del caso polaco de diciembre de 2025 a su designación `ELECTRUM` — **mencionada por una sola fuente secundaria** | OSINT comercial de primera mano, vía terciaria | **C** | **4** | **Única corroboración del caso polaco, y conocida sólo de oído.** Es la razón de que `KJ-5` tenga confianza baja. Brecha `G-3` |
| 9 | Kaspersky ICS-CERT, informe trimestral sobre ataques a organizaciones industriales, **2026-03-06** | OSINT comercial de primera mano | **B** | **3** | **Relaya los hallazgos de la fuente 2 en lugar de aportar análisis propio**, y así se consigna. Su valor es de corroboración de la difusión del hallazgo, no de la observación |
| 10 | Perfiles de proveedor y agregadores sobre el actor (CybelAngel, nhimg, deepstrike, Brandefense, Alphahunt y otros) | OSINT comercial agregado | **C** | **3** | Usados para corroborar fechas y nombres de familia. **Uno de ellos aporta la cautela más valiosa del expediente**: que el organigrama del actor no está consensuado y que la vinculación a la unidad militar es atribución de inteligencia, no determinación judicial (§O-1, §O-2, `G-10`). **Otro atribuye `PathWiper` a actividad rusa sin vincularlo a este actor**, y por eso no se sostiene aquí (§3.3-vii) |

**Escalas**
- **A** completamente fiable · **B** normalmente fiable · **C** bastante fiable · **D** normalmente no fiable · **E** no fiable · **F** no evaluable.
- **1** confirmada por otras fuentes · **2** probablemente cierta · **3** posiblemente cierta · **4** dudosa · **5** improbable · **6** no evaluable.

> **Observación sobre este anexo.** Es el expediente **peor leído** de los seis
> del lote: **ninguna fuente primaria se leyó en original.** Y conviene decir
> por qué eso importa menos aquí que en cualquiera de los otros cinco: porque
> las decisiones que este informe pide —respaldos desconectados, control de
> escritura de directivas de grupo, prueba de restauración— **son correctas con
> independencia de si la fuente dice exactamente lo que las coberturas afirman**.
> Son buenas prácticas frente a cualquier adversario destructivo.
>
> Eso no excusa la brecha `G-1`: si el supuesto clave fuera falso, `KJ-3` caería
> y este informe habría atribuido a un actor concreto una técnica que usa menos
> de lo que decimos. **Lo que no caería son las decisiones**, y esa separación
> entre juicio y recomendación está construida a propósito.

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

## Anexo D — Las seis preguntas de recuperabilidad

Este anexo es el entregable transversal del informe, y es deliberadamente de continuidad y no de seguridad informática. Son las seis preguntas que determinan el resultado frente a **cualquier** adversario destructivo —este actor, un grupo de extorsión como los de `CTI-2026-015`, `CTI-2026-016` o `CTI-2026-024`, o un error propio—. Deben tener respuesta por escrito, con fecha, y la fecha debe caducar.

| # | Pregunta | Por qué | Quién la responde |
|---|---|---|---|
| D-1 | **¿Existe una copia de los sistemas críticos que no sea alcanzable con credenciales de dominio?** | Es la única pregunta cuya respuesta negativa no admite compensación. Si el adversario con control del dominio puede borrar los respaldos, **no hay plan de recuperación: hay una esperanza** | TI y Continuidad, verificado por un tercero |
| D-2 | **¿Cuándo se restauró por última vez un sistema completo desde esa copia, y cuánto tardó?** | Un respaldo no probado es una hipótesis. **La duración importa tanto como el éxito**: restaurar en tres semanas puede ser indistinguible de no restaurar | Continuidad, con registro firmado |
| D-3 | **¿Cuánto tardaríamos en volver a operar si perdiéramos todos los equipos del dominio a la vez?** | Es la medida real del riesgo, y casi nadie la tiene. **La simultaneidad es la característica del vector de este informe**, y los planes de recuperación suelen asumir pérdida parcial | **Dirección**, no el CISO |
| D-4 | **¿Qué procesos críticos pueden operar sin sistemas informáticos, aunque sea degradados, y están los procedimientos escritos y probados?** | Es lo que decide si la organización factura el mes siguiente. **El hallazgo esperado es que existan en papel y nadie los haya ejecutado nunca** | Operaciones y Continuidad |
| D-5 | **¿Están los controladores de dominio y la infraestructura de respaldo en el mismo dominio de fallo que el resto?** | Si lo están, un compromiso de dominio alcanza a la vez la operación y el mecanismo de recuperación | Arquitectura |
| D-6 | **¿Quién puede escribir una directiva de grupo con alcance de dominio, y se alerta cuando lo hace?** | Es la única pregunta de esta lista que es de seguridad informática, y está aquí porque **el vector de distribución es el mecanismo de administración** | Administración de Active Directory |

> **Cómo usar este anexo.** Las seis preguntas se responden en una reunión de
> dos horas con las personas adecuadas, y el resultado cabe en una página. **Lo
> difícil no es responderlas: es que casi ninguna organización las ha hecho
> juntas**, porque tres son de TI, dos de negocio y una de seguridad, y ese
> reparto es exactamente por lo que nadie se las apropia.
>
> Y una advertencia de honestidad, que viene del pre-mortem de §O-6: **estas seis
> preguntas no se justifican por este actor.** Se justifican por los grupos de
> extorsión que esta misma cartera documenta y que sí operan en la región. Si se
> presentan a Dirección citando a la inteligencia militar rusa, el informe habrá
> inflado el riesgo para conseguir un presupuesto correcto por una razón
> equivocada.

## Anexo E — Marcos de referencia empleados

`MITRE ATT&CK v19` · `Modelo del Diamante` · `Cyber Kill Chain` · `Pirámide del Dolor` (con la enmienda de §T-3: contra un actor destructivo la pirámide no contiene la respuesta, porque mide detección y no consecuencia) · `F3EAD` · `ICD 203` · `Análisis de Hipótesis Competidoras (ACH)` · `Comprobación de Supuestos Clave (KAC)` · `pre-mortem` · `análisis de transferencia de perfil sectorial` · `TLP 2.0` · `PAP` · `Admiralty Code` · `Sigma` · `KQL` · `PowerShell`

## Anexo F — Paquete legible por máquina

- Índice con contexto: [`ioc_index.csv`](ioc_index.csv) — para este informe contiene sobre todo **patrones de conducta y de configuración**, no direcciones ni hashes
- Listas planas: [`ioc_hash.txt`](ioc_hash.txt), [`ioc_url.txt`](ioc_url.txt), [`ioc_ipv4.txt`](ioc_ipv4.txt) — **este informe no aporta nada a ellas, y es correcto que no lo haga.** No hay hashes publicados, no hay infraestructura propia, y el único indicador literal es un nombre de tarea programada
- Reglas Sigma: tres reglas en §X-4, más una consulta de inventario de directivas de grupo en PowerShell **cuyo resultado es el entregable**: la lista de directivas autorizadas que `D-2` necesita
- Bundle STIX 2.1: no generado
- Evento MISP: no generado

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| **1.1** | **2026-11-21** | **Alineamiento con MITRE ATT&CK v20.1.** ATT&CK reorganizó la matriz y este informe citaba identificadores que la fuente ha **revocado**: `T1562` → `T1685`. Son referencias que un `Tnnnn` bien formado no delata y que se copian de informes viejos. **No se extiende `caduca`: se ha puesto al día la nomenclatura de los TTP, no revalidado ningún juicio.** Lo comprueba en adelante la familia `G7` de `tools/cti_gate.py` contra el catálogo oficial | Célula CTI |
| 1.0 | 2026-11-17 | Emisión inicial. Primer perfil de actor destructivo de la cartera. **Invierte la estructura habitual del producto**: el consumidor primario es Continuidad de Negocio antes que el SOC, el Anexo A es el apéndice menos importante por diseño, y la detección de mayor prioridad (`D-0`) es una verificación de arquitectura y no una regla. Cierra con `CTI-2026-028` el argumento del lote de noviembre de 2026 sobre los rankings de prevalencia | Célula CTI |

## Anexo H — Realimentación del consumidor

| Pregunta | Respuesta |
|---|---|
| ¿Respondió a su requisito? | |
| **¿Existe una copia de respaldo inalcanzable con credenciales de dominio? (`D-0`, decisión `E-a`)** | |
| **¿Cuándo se restauró por última vez un sistema completo, y cuánto tardó? (`X-2`)** | |
| ¿Cuántas cuentas pueden escribir una directiva de grupo con alcance de dominio? (`X-3`) | |
| ¿Está activada la auditoría de objetos de directiva de grupo? Si no, ¿qué hace falta? (decisión `E-b`) | |
| ¿Se respondieron las seis preguntas del Anexo D, y en qué fecha caducan? | |
| ¿Se presentó este informe a Dirección como riesgo de este actor, o como riesgo destructivo general? *(Véase el pre-mortem de §O-6: la segunda es la respuesta correcta)* | |
| ¿Qué faltó? | |
| ¿Llegó a tiempo? | |

> Sin este anexo devuelto, el ciclo de inteligencia queda abierto. En este
> informe interesan especialmente la segunda y la tercera pregunta, porque son
> las únicas que cambian el resultado — y la última, porque es la que dice si el
> informe se comunicó honestamente.
