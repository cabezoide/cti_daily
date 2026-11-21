---
tlp: "TLP:CLEAR"
pap: "PAP:WHITE"
id: "CTI-2026-062"
version: "1.0"
tipo: "Perfil de cierre de una operación de extorsión extinta"
foco_regional: "32 víctimas LATAM · 2 chilenas, abril de 2023 · apoyo policial mexicano en la captura"
niveles: ["Estratégico", "Operacional", "Táctico"]
autor: "Célula CTI"
actor: "ALPHV · BlackCat · Noberus"
fecha: "2026-11-21"
caduca: "2026-12-21"
distribucion: "Informe de cierre: la marca está extinta desde marzo de 2024 y este expediente documenta su final, no una amenaza vigente. Contiene dos hallazgos propios que afectan a cómo se cita este actor: el catálogo de la fuente **parece registrar actividad hasta junio de 2025 y no la hubo** —cinco entradas llevan fecha de ataque posterior a su propia fecha de descubrimiento—, y **el comunicado del Departamento de Justicia no sostiene la versión que circula en el sector** sobre el caso de sus tres afiliados condenados. No se reproduce ningún nombre ni dominio de víctima. Sí se citan los nombres de los condenados, por ser registro judicial público. Difusión libre conservando la atribución y las salvedades de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-062

## La marca murió en marzo de 2024, el catálogo dice que vivió quince meses más, y la diferencia la decide un campo que casi nadie resta

### Cierre del expediente ALPHV: 731 entradas de las que 402 no tienen país, dos víctimas chilenas de abril de 2023, tres afiliados que trabajaban en el sector de la ciberseguridad, y un comunicado judicial que dice menos de lo que se le atribuye

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-062` |
| Versión | 1.0 |
| Clasificación | `TLP:CLEAR` · `PAP:WHITE` |
| Tipo | Perfil de cierre de una operación extinta |
| Actor | `ALPHV` · `BlackCat` · `Noberus` |
| Emitido | 2026-11-21 |
| Caduca | 2026-12-21 |
| Niveles | Estratégico · Operacional · Táctico |
| Nivel técnico | **Omitido deliberadamente.** Sin muestras ni análisis primario propio: ver §3.4 |
| Medición propia | 731 entradas del catálogo, resueltas el 2026-11-21 |
| Fuente primaria | Comunicado 26-431 del Departamento de Justicia de EE. UU., 2026-04-30 |
| Relevancia regional | **32 LATAM** (4,4 % del catálogo · 9,7 % de las entradas con país) · **2 chilenas** |

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** **La operación está extinta y su última actividad real es del 3 de marzo de 2024, no de junio de 2025 como el catálogo parece indicar.** De las 731 entradas medidas, **diez declaran fecha de ataque posterior al 1 de marzo de 2024**; cinco de ellas son coherentes —fechadas el 1 y el 3 de marzo de 2024 y descubiertas por el rastreador ese mismo día— y **las otras cinco son imposibles: declaran ataques del 3 de mayo de 2024, el 2 de septiembre de 2024, el 28 de octubre de 2024, el 17 de enero de 2025 y el 3 de junio de 2026, y las cinco fueron descubiertas el 26 de julio de 2023**. Una entrada no puede descubrirse once meses antes del ataque que declara. Valoramos **casi con certeza** *(≥99 %)* que las cinco sean artefacto del campo de fecha y no actividad, y **muy probable** *(80–95 %)* que la actividad real termine en la primera semana de marzo de 2024. **Confianza: alta.** *Base:* medición propia, §O-2.2. *Consecuencia:* **cualquier cifra de «última actividad de ALPHV» tomada de este catálogo sin restar las dos fechas está equivocada en quince meses** (`Anexo D`).

**KJ-2.** **El 55 % del catálogo no tiene país, de modo que toda proporción geográfica de este actor admite dos valores correctos y distintos, y hay que decir cuál se usa.** Sólo **329 de 731 entradas (45,0 %)** traen país. Las 32 entradas latinoamericanas son por tanto **el 4,4 % del catálogo completo** o **el 9,7 % de las entradas con país**: las dos cifras son correctas y difieren en más del doble. Valoramos **casi con certeza** *(≥99 %)* los recuentos. **Confianza: alta.** *Consecuencia:* **este expediente no sostiene ninguna afirmación sobre el reparto geográfico real de ALPHV**, sólo sobre el reparto de la mitad que la fuente supo etiquetar, y la mitad etiquetada no es una muestra aleatoria de la otra (`E-2`, `O-2.3`).

**KJ-3.** **Hubo dos víctimas chilenas y las dos son de abril de 2023, con diecinueve días entre ellas.** Una de servicios financieros el **2 de abril de 2023** y una de comercio al detalle el **21 de abril de 2023**, ambas con dominio en la entrada y **ninguna con referencia de prensa**. Valoramos **probable** *(55–80 %)* que la atribución de país sea correcta —es enriquecimiento derivado— y **casi con certeza** *(≥99 %)* que no haya más chilenas en el catálogo. **Confianza: moderada.** *Base:* medición propia sobre el catálogo, §E-2.2. *Consecuencia:* **el expediente chileno de este actor está cerrado y es pequeño**: dos reclamaciones de hace treinta y un meses, sin confirmación pública. Puestas junto a la medición de `CTI-2026-015` —donde Qilin concentra veinte de las treinta víctimas chilenas del top diez—, **no mueven ninguna prioridad** (`E-2.2`).

**KJ-4.** **Tres afiliados fueron condenados o se declararon culpables en 2026, y los tres trabajaban en el sector de la ciberseguridad.** El comunicado 26-431 del Departamento de Justicia, de **30 de abril de 2026**, recoge que **Ryan Goldberg, de 40 años, y Kevin Martin, de 36, fueron condenados a cuatro años de prisión cada uno** tras declararse culpables en **diciembre de 2025** de un cargo de conspiración para obstruir el comercio mediante extorsión; que **despegaron ALPHV BlackCat entre abril y diciembre de 2023**; y que un tercer implicado, **Angelo Martino, de 41 años, se declaró culpable en abril de 2026** y tenía la sentencia fijada para el **9 de julio**. La frase del comunicado es *«All three men worked in the cybersecurity industry»*. Valoramos **casi con certeza** *(≥99 %)* el contenido del comunicado. **Confianza: alta.** *Base:* fuente primaria leída en original, §O-4.

**KJ-5.** **Y el hallazgo que obliga a este informe a separarse de la cobertura del sector: el comunicado del Departamento de Justicia NO dice que atacaran a sus propios clientes, ni nombra a sus empleadores.** La versión que circula —respondedores de incidentes y negociadores que cifraron a las organizaciones que los habían contratado, con los nombres de dos empresas de seguridad— **procede de prensa especializada, no del comunicado**. Lo que el comunicado sostiene es más estrecho y sólo sobre uno de los tres: que **Martino *«abusó de su papel de negociador para víctimas de ransomware compartiendo información confidencial de las víctimas con los actores de la amenaza para aumentar el valor del rescate pagado»***. De Goldberg y Martin sólo dice que trabajaban en el sector. **No nombra a ninguna empresa empleadora, no da cargos, y no afirma relación contractual previa entre los acusados y las víctimas.** Valoramos **casi con certeza** *(≥99 %)* esta ausencia, por lectura directa. **Confianza: alta.** *Consecuencia:* **la afirmación «atacaron a sus clientes» es verosímil y puede ser cierta, pero quien la cite debe atribuirla a la prensa y no al Departamento de Justicia**, y una organización que vaya a cambiar su política de contratación de respuesta a incidentes debería saber sobre qué base lo hace (`O-4.2`, `Anexo B`).

**KJ-6.** **El reparto económico del programa de afiliados quedó documentado judicialmente, y es el dato más duradero del expediente: 20 % para los administradores, 80 % para el afiliado.** El comunicado declara que los tres *«acordaron pagar a los administradores de ALPHV BlackCat una participación del 20 % de cualesquiera rescates recibidos»* y que, tras extorsionar con éxito a una víctima por **aproximadamente 1,2 millones de dólares en bitcoin**, *«se repartieron su parte del 80 % entre los tres»*. Valoramos **casi con certeza** *(≥99 %)* las cifras. **Confianza: alta.** *Consecuencia:* es una de las pocas confirmaciones judiciales del reparto de un programa de extorsión como servicio, y **sirve de referencia para valorar afirmaciones sobre otros programas** —incluidas las de los que declaran repartos más generosos para atraer afiliados (`E-3`).

**KJ-7.** **La captura tuvo apoyo policial mexicano, y es el único punto de contacto regional documentado por fuente primaria de todo el expediente.** El comunicado agradece la colaboración de la **Policía de Investigación del Aeropuerto Internacional de la Ciudad de México**, y consigna que, *«cuando Goldberg trató de huir al extranjero, el FBI lo siguió a través de diez países»*. Valoramos **casi con certeza** *(≥99 %)* el dato. **Confianza: alta.** *Base:* comunicado 26-431, agradecimientos. *Consecuencia:* **la región aparece en este expediente antes como eslabón de la respuesta que como víctima**, lo que es poco habitual en esta cartera y conviene registrar (`E-2.3`).

**KJ-8.** **El catálogo no contiene ni una sola cifra de rescate ni de volumen de datos: los dos campos están vacíos en las 731 entradas.** Cobertura medida: país 45,0 %, dominio 89,6 %, captura de pantalla 93,8 %, descripción 85,4 %, **referencia de prensa 5,7 %**, **rescate 0,0 %**, **tamaño de datos 0,0 %**. Valoramos **casi con certeza** *(≥99 %)* las proporciones. **Confianza: alta para los recuentos de cobertura**, que son medición propia; **este juicio no afirma nada sobre la veracidad de las reclamaciones**, que no está corroborada en el 94,3 % de los casos sin prensa. *Base:* medición propia de cobertura de campos, §O-2.3. *Consecuencia:* **toda cifra económica sobre este actor procede de otra fuente**, y la única con autoridad judicial es el 1,2 millones de `KJ-6`. El 5,7 % de cobertura de prensa significa además que **el 94 % de las reclamaciones de este actor nunca fue objeto de una noticia**, lo que no las hace falsas pero sí no verificadas (`O-2.4`).

**KJ-9.** **El perfil de volumen dibuja un auge y un colapso, no un declive: 2023 concentra el 59 % del catálogo y 2024 cae a 62 entradas de las que 57 son de enero y febrero.** Por año de ataque declarado: **2021: 14 · 2022: 220 · 2023: 433 · 2024: 62 · 2025: 2**. Valoramos **casi con certeza** *(≥99 %)* el recuento y **muy probable** *(80–95 %)* que la forma de la curva refleje actividad real y no cobertura de la fuente, porque la caída es abrupta y coincide con un hecho externo fechado. **Confianza: alta para el dato, moderada para la lectura.** *Consecuencia:* **es el patrón de una marca que se interrumpe, no de una que se apaga**, y conviene compararlo con el de las marcas que esta cartera ha visto apagarse despacio (`E-1`, `O-3`).

**KJ-10.** **Lo que esta cartera debe retener no es el actor, que ya no existe, sino que su ficha sigue viva en las fuentes y produce errores medibles hoy, dos años y medio después.** El catálogo sigue devolviendo 731 entradas, con fechas de ataque de hasta junio de 2025 y sin aviso alguno de que la operación esté extinta. Valoramos **probable** *(55–80 %)* que cualquier producto derivado que consuma esta fuente sin el correctivo de `KJ-1` presente a ALPHV como activo o recientemente activo. **Confianza: moderada.** *Base:* inferencia propia sobre el estado del catálogo medido, §O-2.2. *Consecuencia:* **una marca extinta es una fuente de falsos positivos de atribución**, y el `Anexo D` da el procedimiento para no caer (`Anexo D`, `A.1`).

**KJ-11.** **La hipótesis de reutilización del nombre no es una hipótesis: hay un foro criminal en ruso llamado `ALPHV` con infraestructura renovada hace once días, y las fechas de registro demuestran que NO es continuidad de la operación extinta.** Revisado el **21-11-2026**: `alphv.pro` sirve un foro sobre XenForo, íntegramente en ruso, titulado `ALPHV`, con secciones de **«Кардинг/Хакинг»** —carding y hacking—, un servicio de **«Гарант | Escrow»**, **«Страховой депозит»** —depósito de seguro— y **«Платное повышение»** —promoción de pago—, contacto obligatorio por Telegram, y estadísticas declaradas de **7.124 temas, 19.106 mensajes y 11.002 usuarios**. Declara como propios los dominios `alphv.pro` y `alphv.io` y un servicio oculto cuyo prefijo legible es `alphvi`. **Lo decisivo es el registro:** `alphv.io` se creó el **2 de noviembre de 2024**, **ocho meses después** de la extinción de la operación, se actualizó el **19 de noviembre de 2026** —hace dos días— y sus servidores de nombres están en `oplotflow.net`, dominio creado el **10 de noviembre de 2026**, hace once. Valoramos **casi con certeza** *(≥99 %)* que el foro existe y está mantenido, y **muy probable** *(80–95 %)* que **no tenga continuidad operativa con el grupo original**, porque su dominio es posterior al cese y porque **no es la misma clase de objeto**: no hay sitio de filtración, ni víctimas listadas, ni negociación de rescates. **Confianza: alta para las fechas de registro, que son verificables por `whois`; moderada para la ausencia de vínculo, que es un argumento de fecha y de clase, no de telemetría.** *Base:* lectura propia del sitio y consulta `whois`, §O-6. *Consecuencia:* **el disparador `I-2` queda cumplido con un resultado inesperado** —el nombre se reutilizó, pero para un foro y no para una operación— y **`H-3` pasa de posible a observado** (`O-6`, `A.4`).

---

## 2. Resumen ejecutivo

**ALPHV —también llamado BlackCat y Noberus— no existe desde marzo de 2024.** Fue una de las operaciones de extorsión como servicio más activas de su época, el Departamento de Justicia le atribuye *«más de 1.000 víctimas»* en conjunto, y terminó de la forma menos épica posible: desapareciendo con el dinero de sus propios afiliados. Este informe no describe una amenaza vigente. Describe un cierre, y lo hace porque **el cierre sigue produciendo errores**.

El primero es de fechas. El catálogo público que esta cartera usa para medir victimología devuelve, para este actor, 731 entradas con fechas de ataque que llegan hasta **el 3 de junio de 2025**. Si uno se detiene ahí, concluye que la operación siguió golpeando quince meses después de su desaparición. **No es cierto, y la prueba está en el propio registro:** las cinco entradas con fecha posterior a mayo de 2024 fueron todas **descubiertas por el rastreador el 26 de julio de 2023**. Una reclamación no se descubre once meses antes de que exista. Restando las dos fechas —el primero de los ocho correctivos que `CTI-2026-054` dejó escritos— la actividad real termina el 3 de marzo de 2024, que es exactamente cuando la operación se derrumbó.

El segundo error es de proporciones. **El 55 % de las entradas no tiene país.** Eso significa que las 32 víctimas latinoamericanas son el 4,4 % del catálogo o el 9,7 % de lo etiquetado, según lo que se divida, y que **ninguna de las dos cifras dice cuál era el reparto geográfico real**. Para Chile el dato es pequeño y cerrado: **dos reclamaciones, las dos de abril de 2023**, ninguna confirmada públicamente. Comparadas con la concentración de Qilin que `CTI-2026-015` midió, no mueven nada.

El tercer error es de atribución de fuente, y es el que más importa. En abril de 2026 el Departamento de Justicia condenó a **cuatro años de prisión a dos afiliados de ALPHV**, y un tercero se declaró culpable. Los tres trabajaban en el sector de la ciberseguridad, y el caso se ha contado en el sector como el de unos respondedores de incidentes y un negociador que cifraron a las organizaciones que los habían contratado, con los nombres de sus empresas. **El comunicado del Departamento de Justicia no dice eso.** No nombra ninguna empresa, no da ningún cargo, y la única afirmación de abuso de posición que contiene es sobre uno de los tres: que compartió información confidencial de víctimas con los atacantes **mientras negociaba en su nombre**. Lo demás puede ser verdad —hay cobertura abundante que lo sostiene— pero no es lo que dice la fuente primaria, y una organización que vaya a revisar cómo contrata respuesta a incidentes merece saber qué parte está probada judicialmente y qué parte es periodismo.

Lo que sí queda documentado judicialmente, y es el dato más útil del expediente, es **el reparto del programa: 20 % para los administradores y 80 % para el afiliado**, con un rescate concreto de aproximadamente **1,2 millones de dólares en bitcoin** repartido entre tres personas. Esa clase de confirmación es rara, y sirve de patrón de medida para valorar lo que otros programas prometen.

**Y una nota regional que no es de victimología:** la captura contó con el apoyo de la **Policía de Investigación del Aeropuerto Internacional de la Ciudad de México**, y el FBI siguió a uno de los condenados por diez países cuando trató de huir. En este expediente la región aparece antes en la respuesta que en el daño, lo cual es infrecuente y merece quedar escrito.

---

## 3. Alcance y limitaciones

### 3.1 Qué contiene este informe

El cierre documentado de una operación extinta: la forma de su catálogo, su victimología regional con los correctivos necesarios para leerla, el cierre judicial de tres de sus afiliados leído en la fuente primaria, y el método para no volver a tomar una marca muerta por una viva.

### 3.2 Qué NO contiene

- **No es un informe de amenaza vigente.** Si busca a quién vigilar hoy, este no es el expediente: la operación no existe.
- **No se leyó ningún sitio de filtración.** Están caídos desde 2024, y no hay acceso a Tor en este entorno.
- **No hay muestras, análisis de binario ni telemetría propia de red.** De ahí que el nivel técnico se omita (§3.4).
- **No se reproduce ningún nombre ni dominio de víctima**, incluidas las dos chilenas de `KJ-3`. Ninguna ha confirmado nada, y nombrarlas amplificaría una reclamación de adversario de hace treinta y un meses.
- **No se entró en el foro de `O-6`.** Se leyó el contenido servido públicamente; **no se creó cuenta, no se envió ningún formulario y no se descargó ningún fichero.** Por tanto su actividad interna real no está medida (`G-6`).
- **No se cuantifica el destino de los afiliados dispersados.** Es la brecha `G-3`: hay afirmaciones de que continuaron bajo otras marcas, y no se ha verificado ninguna correspondencia concreta.

### 3.3 La base de este informe, y su desigualdad

| Elemento | Base | Grado |
|---|---|---|
| La forma y las fechas del catálogo | **Medición propia** sobre 731 entradas, 2026-11-21 | **Alto** |
| La incoherencia de las cinco entradas tardías | **Medición propia**, verificable por cualquiera con la misma consulta | **Alto** |
| El cierre judicial | **Fuente primaria** leída en original: comunicado 26-431 del DOJ | **Alto** |
| La atribución de país de las víctimas | Enriquecimiento derivado de la fuente, con 55 % de huecos | **Bajo** |
| La salida fraudulenta de marzo de 2024 y su cifra | Prensa especializada y vendedores; **no verificada en fuente primaria** | **Medio** |
| Los empleadores y cargos de los condenados | **Prensa especializada únicamente.** No están en el comunicado | **Medio, y marcado como tal en todo el informe** |
| El destino de los afiliados | Afirmaciones de vendedor sin correspondencia concreta verificada | **Bajo** |

### 3.4 Por qué se omite el nivel técnico

Esta cartera ha establecido que **un perfil sin muestra no es inteligencia técnica** —lo dijeron `CTI-2026-059` y `CTI-2026-061` al omitir el mismo nivel—. Aquí la razón es más fuerte: el cifrador de ALPHV está ampliamente documentado por terceros desde 2022, **pero este informe no ha analizado ninguna muestra**, y transcribir indicadores técnicos de hace tres años de una operación extinta produciría exactamente el problema que el `Anexo A` de este repositorio existe para evitar. **Quien necesite los indicadores históricos del cifrador debe ir a los informes de proveedor de 2022–2023, no a este documento.**

### 3.5 Lo que se afirma sobre este actor, y lo que las fuentes sostienen

| # | Afirmación corriente | Veredicto | Base |
|---|---|---|---|
| 1 | ALPHV está extinto desde 2024 | **CORROBORADO** | Medición propia: última actividad coherente el 2024-03-03 (`KJ-1`) |
| 2 | Su última actividad registrada es de 2025 | **NO SOSTENIDO** | Las cinco entradas tardías son artefacto de fecha: descubiertas el 2023-07-26 (`KJ-1`, `O-2.2`) |
| 3 | Terminó con una salida fraudulenta tras el caso Change Healthcare | **PLAUSIBLE, no verificado aquí** | Coherente con la caída abrupta medida (`KJ-9`), pero la cifra y el relato son de prensa (`O-3.2`) |
| 4 | Tenía más de 1.000 víctimas | **CORROBORADO como afirmación del DOJ** | El comunicado lo dice del grupo en conjunto; el catálogo medido tiene 731 entradas, que es otra cosa (`O-2.1`) |
| 5 | Sus afiliados eran profesionales de la ciberseguridad | **CORROBORADO** | *«All three men worked in the cybersecurity industry»*, comunicado 26-431 (`KJ-4`) |
| 6 | Esos afiliados atacaron a sus propios clientes | **NO SOSTENIDO POR LA FUENTE PRIMARIA** | El comunicado no lo afirma de Goldberg ni Martin, y no nombra empleadores. Sólo de Martino dice que abusó de su papel de negociador (`KJ-5`, `O-4.2`) |
| 7 | Trabajaban en Sygnia y DigitalMint | **NO ESTÁ EN EL COMUNICADO** | Procede de prensa. Se consigna como tal y no se usa como base de ningún juicio (`Anexo B`) |
| 8 | El programa repartía 80/20 a favor del afiliado | **CORROBORADO judicialmente** | Comunicado 26-431 (`KJ-6`) |
| 9 | Tuvo víctimas chilenas | **CORROBORADO como reclamación, no como brecha** | Dos entradas de abril de 2023, sin confirmación pública (`KJ-3`) |
| 10 | Sus afiliados siguieron activos bajo otras marcas | **NO VERIFICADO** | Afirmación repetida por vendedores sin correspondencia concreta comprobable (`G-3`) |

> **Y una advertencia de método sobre esta tabla.** Los veredictos 6 y 7 son los únicos del lote que **contradicen la narrativa dominante**, y conviene decir cómo se llegó a ellos: no por escepticismo previo, sino porque el procedimiento de esta cartera obliga a **leer el documento primario en original** antes de citarlo. La cobertura secundaria era unánime y coherente; el comunicado, más estrecho. **Cuando las dos cosas pasan a la vez, la que manda es la fuente primaria** —y el hecho de que la narrativa sea verosímil es precisamente lo que hace fácil no comprobarla.

---

# NIVEL ESTRATÉGICO

## E-1. Cifras

<!-- cti:stats -->

| Valor | Qué mide | Nota |
|---|---|---|
| `731` | Entradas del catálogo medidas | Resueltas el 2026-11-21 |
| `2024-03-03` | **Última actividad coherente** | Y no 2025-06-03, que es lo que el campo de fecha sugiere |
| `5` | **Entradas imposibles** | Fecha de ataque posterior a su propia fecha de descubrimiento |
| `402` | Entradas **sin país** | El 55,0 % del catálogo |
| `329` | Entradas con país | El 45,0 % |
| `32` | Entradas latinoamericanas | **4,4 %** del total · **9,7 %** de las etiquetadas |
| `2` | **Víctimas chilenas** | Las dos de abril de 2023 |
| `0` | Entradas con cifra de rescate | Y `0` con tamaño de datos |
| `5,7 %` | Entradas con referencia de prensa | 42 de 731 |
| `20 % / 80 %` | **Reparto del programa** | Administradores / afiliado. Judicialmente documentado |
| `1,2 M USD` | **Único rescate con cifra judicial** | En bitcoin, repartido entre tres personas |
| `4 años` | Pena de cada uno de los dos condenados | Comunicado DOJ 26-431, 2026-04-30 |

## E-2. La victimología, y los dos números que son correctos a la vez

### E-2.1 Por qué no se puede dar una proporción regional de este actor

**El 55 % del catálogo no tiene país.** Ese solo dato invalida cualquier frase de la forma «el X % de las víctimas de ALPHV estaba en Y», y conviene ver por qué no se arregla dividiendo sólo por lo etiquetado.

Para que el 9,7 % de las entradas etiquetadas fuese una estimación válida del reparto real, **las 402 entradas sin país tendrían que repartirse geográficamente igual que las 329 con país**. No hay ninguna razón para creerlo y hay una para dudarlo: el país de estas fuentes se deriva habitualmente del dominio de la entrada, y **los dominios genéricos —`.com`, `.net`— son los que más se resisten a la geolocalización y los que más abundan entre organizaciones estadounidenses**. Si eso es así, las entradas sin país no son una muestra aleatoria: están sesgadas hacia los dominios genéricos, y por tanto hacia una geografía concreta.

**La consecuencia operativa, que es la única que importa:** este informe da los recuentos absolutos —32 latinoamericanas, 2 chilenas— y **se niega a convertirlos en proporciones del universo real**. Un recuento absoluto de reclamaciones es un suelo: dice «al menos estas», y eso sí es información.

| Lectura | Valor | Qué sostiene |
|---|---|---|
| LATAM sobre el catálogo completo | **4,4 %** | Suelo. Correcto si se dice «de las entradas del catálogo» |
| LATAM sobre las entradas con país | **9,7 %** | Correcto si se dice «de las entradas que la fuente supo etiquetar» |
| LATAM en el universo real de víctimas | **No estimable** | Requiere suponer que los 402 huecos se reparten como el resto, y no hay base |

### E-2.2 Las dos víctimas chilenas, y por qué no mueven nada

<!-- cti:timeline -->

| Fecha de ataque declarada | Sector | ¿Dominio? | ¿Prensa? |
|---|---|---|---|
| **2023-04-02** | Servicios financieros | Sí | **No** |
| **2023-04-21** | Comercio al detalle y electrónico | Sí | **No** |

Diecinueve días entre las dos, y nada más en treinta y un meses. **Ninguna tiene referencia de prensa**, lo que en un catálogo cuya cobertura de prensa global es del 5,7 % no es excepcional, pero sí significa que **ninguna de las dos reclamaciones fue verificada públicamente jamás**.

No se reproducen los nombres ni los dominios. El procedimiento para que una organización chilena compruebe si fue una de las dos está en el `Anexo F`, y **no necesita este informe**: necesita su propio dominio y la consulta al catálogo.

**Puesto en contexto, que es lo que pide una decisión:** `CTI-2026-015` midió que **Qilin concentra veinte de las treinta víctimas chilenas** del top diez de extorsión, y `CTI-2026-058` identificó la única víctima chilena de su lote de seis actores. Dos reclamaciones de abril de 2023 de una operación que ya no existe **no cambian ninguna prioridad de vigilancia**. Se consignan porque el expediente chileno de un actor debe estar completo, no porque haya que actuar.

### E-2.3 La región como eslabón de la respuesta, no como víctima

Hay un dato en el comunicado judicial que no es de victimología y que esta cartera no había registrado antes: **la Policía de Investigación del Aeropuerto Internacional de la Ciudad de México colaboró en el caso**, y consta expresamente en los agradecimientos del Departamento de Justicia.

Añádase que, *«cuando Goldberg trató de huir al extranjero, el FBI lo siguió a través de diez países»*. El comunicado no dice cuáles, ni que México fuera uno de ellos, ni en qué consistió la colaboración mexicana —**y este informe no lo va a suponer**—. Lo que sí se puede afirmar es que **la institución aparece en un documento judicial estadounidense como colaboradora en la detención de un afiliado de extorsión**.

**Por qué merece quedar escrito:** casi todos los expedientes de esta cartera sitúan a la región en el lado del daño. Este la sitúa en el de la respuesta. Es un punto de apoyo para quien tenga que argumentar que la cooperación policial regional produce resultados, y es verificable en una fuente primaria.

## E-3. El reparto 20/80, y para qué sirve saberlo

De todos los datos de este expediente, el que más durará es el que no depende de ALPHV: **el reparto económico del programa, confirmado en una sentencia**.

El comunicado declara que los tres afiliados *«acordaron pagar a los administradores de ALPHV BlackCat una participación del 20 % de cualesquiera rescates recibidos»*, y que después de extorsionar a una víctima por **aproximadamente 1,2 millones de dólares en bitcoin**, *«se repartieron su parte del 80 % entre los tres»*.

| Elemento | Valor | Procedencia |
|---|---|---|
| Comisión de los administradores | **20 %** | Comunicado 26-431 |
| Parte del afiliado | **80 %** | Comunicado 26-431 |
| Rescate del caso con cifra | **≈ 1,2 M USD en bitcoin** | Comunicado 26-431 |
| Reparto entre los tres afiliados | A tres partes | Comunicado 26-431 |
| Cantidad percibida por cada uno | **No consta** | El comunicado no la da |

> **Una cautela aritmética que conviene no saltarse.** Aplicar el 80 % a 1,2 millones y dividir por tres da unos 320.000 dólares por persona, y es tentador escribirlo. **El comunicado no da esa cifra**, y el cálculo supone que el reparto fue a partes iguales y que no hubo costes intermedios. Se deja aquí como lo que es —una aproximación nuestra— y no entra en ninguna tabla de cifras del informe.

**Para qué sirve:** cuando un programa de extorsión anuncia en un foro que reparte el 85 % o el 90 % para atraer afiliados, ahora hay **una cifra con respaldo judicial** con la que compararlo. Y hay un segundo uso, menos obvio: el 20 % de comisión indica que **los administradores capturaban una fracción modesta**, lo que es coherente con un modelo de volumen —muchos afiliados, muchas víctimas— y no con uno de pocas operaciones grandes muy controladas.

## E-4. Decisiones que este informe pide

1. **Retirar ALPHV de cualquier lista de actores a vigilar**, si sigue en alguna. La operación no existe desde marzo de 2024.
2. **Aplicar el correctivo de fechas a todo producto que consuma este catálogo.** No es específico de ALPHV: es la clase de error que `CTI-2026-054` ya midió a escala de 68 actores.
3. **Para las dos organizaciones chilenas del catálogo, si se reconocen:** la comprobación es sobre su propio dominio y no requiere este informe. No hay acción urgente: la reclamación tiene treinta y un meses.
4. **Al citar el caso judicial, atribuir correctamente.** Las condenas, el reparto 20/80 y la pertenencia de los tres al sector son del Departamento de Justicia. Los empleadores y la relación cliente-proveedor son de prensa. **Si la decisión que se apoya en ello es revisar cómo se contrata respuesta a incidentes, la base es más débil de lo que parece** y conviene buscar los documentos del caso antes de reescribir una política.

---

# NIVEL OPERACIONAL

## O-1. Identificación

| Campo | Valor |
|---|---|
| Nombres | `ALPHV` · `BlackCat` · `Noberus` |
| Clase | Extorsión como servicio, con programa de afiliados |
| Estado | **Extinto.** Última actividad coherente: 2024-03-03 |
| Atribución estatal | Ninguna. Criminal con ánimo de lucro |
| Entradas en el catálogo medido | 731 |
| Atribución del DOJ | *«más de 1.000 víctimas»*, referido al grupo en conjunto |

**Sobre la discrepancia entre 731 y «más de 1.000».** Las dos cifras pueden ser correctas: el catálogo recoge las reclamaciones **publicadas en el sitio de filtración**, y el Departamento de Justicia cuenta **víctimas conocidas por la investigación**, que incluyen a las que pagaron y por tanto nunca se publicaron. **La diferencia no es un error de nadie: es la definición de dos poblaciones distintas**, y es la razón por la que esta cartera repite que el recuento de un sitio de filtración acota por abajo y por arriba nada.

## O-2. El catálogo, medido

### O-2.1 Lo que hay

<!-- cti:bars title="Entradas por año de ataque declarado" -->

| Año | Entradas |
|---|---|
| 2021 | 14 |
| 2022 | 220 |
| **2023** | **433** |
| 2024 | 62 |
| 2025 | 2 |

**2023 concentra el 59,2 % del catálogo.** Y 2024, con 62 entradas, es engañoso hasta que se desglosa: **57 de esas 62 son de enero y febrero**, y las cinco restantes son las del 1 y 3 de marzo más las imposibles de §O-2.2.

### O-2.2 Las cinco entradas imposibles, y cómo se detectan

Este es el hallazgo propio central del informe, y se reproduce en dos minutos: **comparar, para cada entrada, la fecha de ataque declarada con la fecha en que el rastreador la descubrió.**

| Fecha de ataque declarada | Fecha de descubrimiento | País | Desfase |
|---|---|---|---|
| 2024-05-03 | **2023-07-26** | US | **−282 días** |
| 2024-09-02 | **2023-07-26** | US | **−404 días** |
| 2024-10-28 | **2023-07-26** | US | **−460 días** |
| 2025-01-17 | **2023-07-26** | US | **−541 días** |
| 2025-06-03 | **2023-07-26** | AO | **−678 días** |

**Las cinco comparten fecha de descubrimiento al día**, y las cinco declaran un ataque posterior a ella. Las cuatro primeras son estadounidenses y la quinta angoleña.

**Qué NO se puede concluir.** No se puede decir qué produjo el error: puede ser un campo mal parseado por el enriquecedor, una fecha mal escrita en la reclamación original, o un formato de fecha ambiguo interpretado al revés. **No tenemos acceso a la reclamación original —el sitio está caído desde 2024— y por tanto la causa queda abierta** (`G-2`).

**Qué sí se puede concluir, y basta para el propósito:** ninguna de las cinco sirve como evidencia de actividad en 2024 o 2025, porque **la propia fuente registró su existencia en julio de 2023**. Para la pregunta «¿cuándo dejó de actuar este grupo?», las cinco se descartan, y la respuesta pasa de junio de 2025 a marzo de 2024.

> **Y la observación que generaliza**, que es la razón de que esto esté en el `Anexo D`: el correctivo no requiere saber nada del actor. **Es una comprobación de coherencia interna entre dos campos de la misma entrada**, y cualquiera puede ejecutarla sobre cualquier actor de cualquier catálogo. `CTI-2026-054` lo estableció como el primero de sus ocho correctivos y midió que convertía 68 actores aparentemente nuevos en 14. Aquí convierte quince meses de actividad fantasma en cero.

### O-2.3 La cobertura de campos, que decide qué se puede preguntar

<!-- cti:table highlight="Rescate" -->

| Campo | Entradas con dato | Cobertura | Qué permite preguntar |
|---|---|---|---|
| Captura de pantalla | 686 | **93,8 %** | Casi todas traen prueba de nivel 3 de la escala de `CTI-2026-048` —el nivel que más engaña— |
| Dominio | 655 | **89,6 %** | **Comprobación por la propia víctima**: es lo más útil del catálogo |
| Descripción | 624 | 85,4 % | Análisis de plantillas y duplicados |
| **País** | **329** | **45,0 %** | **Casi nada.** Es la limitación de `KJ-2` |
| Referencia de prensa | 42 | **5,7 %** | El 94,3 % nunca fue noticia |
| **Rescate** | **0** | **0,0 %** | **Nada.** Toda cifra económica viene de fuera |
| **Tamaño de datos** | **0** | **0,0 %** | **Nada** |

**La lectura de esta tabla es el informe en pequeño.** La cobertura es altísima en lo que sirve para que una víctima se reconozca —dominio, captura, descripción— y nula en lo que sirve para valorar el impacto —rescate, volumen—. **Un catálogo así es una herramienta de notificación, no de medición económica**, y usarlo para lo segundo produce cifras inventadas con aspecto de datos.

### O-2.4 Los países etiquetados, con la salvedad de siempre

| País | Entradas | Sobre las 329 etiquetadas |
|---|---|---|
| Estados Unidos | 92 | 28,0 % |
| Canadá | 25 | 7,6 % |
| Australia | 21 | 6,4 % |
| Reino Unido | 19 | 5,8 % |
| Alemania | 13 | 4,0 % |
| **Brasil** | **11** | **3,3 %** |
| Japón | 11 | 3,3 % |
| Francia | 11 | 3,3 % |
| Italia | 11 | 3,3 % |
| India | 9 | 2,7 % |
| **México** | **7** | **2,1 %** |

**Brasil es el sexto país del catálogo etiquetado**, empatado con Japón, Francia e Italia. Es el dato regional más alto del expediente y es coherente con lo que esta cartera ha medido en casi todos los actores: **Brasil absorbe la mayor parte de la actividad regional**, y la diferencia con el resto de la región es de un orden de magnitud.

Las 32 entradas latinoamericanas se reparten así: **Brasil 11 · México 7 · Colombia 4 · Argentina 2 · Chile 2 · Ecuador 2 · República Dominicana 2 · Guatemala 1 · Panamá 1 · Venezuela 1**.

## O-3. La curva, y lo que el final tiene de instructivo

### O-3.1 Interrupción, no declive

<!-- cti:chart title="Forma del catálogo" cap="Entradas por año de ataque declarado. La caída de 2024 no es un declive: 57 de sus 62 entradas son de enero y febrero." -->

| Año | Entradas | Forma |
|---|---|---|
| 2021 | 14 | Arranque |
| 2022 | 220 | Crecimiento |
| 2023 | 433 | **Cima** |
| 2024 | 62 | **Corte** |
| 2025 | 2 | Artefacto |

**La distinción entre interrupción y declive no es estilística: cambia la hipótesis.** Una marca que se apaga despacio sugiere pérdida de afiliados, competencia, o desgaste de un cifrador detectado. Una que se corta en seco en la primera semana de un mes sugiere **un suceso externo con fecha**. Aquí la curva apunta a lo segundo, y hay un suceso externo fechado que lo explica.

### O-3.2 La salida fraudulenta, consignada con su grado

La versión aceptada es que la operación se derrumbó en marzo de 2024 cuando sus administradores cobraron el rescate del caso Change Healthcare —del grupo UnitedHealth— y desaparecieron sin repartirlo con los afiliados, después de que el FBI hubiera incautado parte de su infraestructura en diciembre de 2023. Se cita habitualmente una cifra de 22 millones de dólares.

**Qué sostiene este informe y qué no.** La **forma** de la curva medida es coherente con esa versión: corte abrupto en la primera semana de marzo de 2024. Eso es medición propia. Pero **ni la cifra de 22 millones ni la mecánica del fraude se han verificado aquí en fuente primaria**: proceden de prensa especializada y de informes de vendedor. Se consignan como **plausibles y no verificadas**, con grado medio, y **ningún juicio de este informe se apoya en ellas**.

Nótese que el comunicado judicial de 2026, que es la fuente primaria del expediente, **no menciona la salida fraudulenta ni el caso Change Healthcare**. No la contradice: simplemente no es su objeto, que son tres afiliados concretos y su conducta en 2023.

## O-4. El cierre judicial, leído en el original

### O-4.1 Lo que el comunicado dice

Comunicado **26-431** del Departamento de Justicia, Oficina de Asuntos Públicos, **30 de abril de 2026**, actualizado el mismo día.

| Elemento | Dato del comunicado |
|---|---|
| Condenados | **Ryan Goldberg**, 40 años, de Georgia · **Kevin Martin**, 36, de Texas |
| Pena | **Cuatro años de prisión cada uno** |
| Fecha de la sentencia | *«were sentenced today»* — el comunicado es del 2026-04-30 |
| Declaración de culpabilidad | **Diciembre de 2025**, ambos |
| Cargo | **Un cargo** de conspiración para obstruir, retrasar o afectar el comercio mediante extorsión |
| Periodo de los hechos | *«between April 2023 and December 2023»* |
| Tercer implicado | **Angelo Martino**, 41, de Florida. Culpable en **abril de 2026**; sentencia fijada para el **9 de julio** |
| Reparto | **20 %** a los administradores; el **80 %** repartido entre los tres |
| Rescate con cifra | *«approximately $1.2 million in Bitcoin»*, de una víctima |
| Profesión | *«All three men worked in the cybersecurity industry»* |
| Conducta de Martino | *«abused his role as a negotiator for victims of ransomware by sharing confidential victim information with threat actors to increase the value of the ransom paid»* |
| Sectores de víctimas | *«firms who were providing medical and engineering services»*; se menciona **un consultorio médico** con filtración de datos de pacientes |
| Investigación | **FBI, oficina de campo de Miami**, con apoyo del **Servicio Secreto** |
| Cooperación internacional | **Policía de Investigación del Aeropuerto Internacional de la Ciudad de México** |
| Huida | *«cuando Goldberg trató de huir al extranjero, el FBI lo siguió a través de diez países»* |
| Decomiso | Mención genérica a que *«forfeit the proceeds of their crimes»*, **sin importe** |
| Vector de acceso | **No consta.** El comunicado no describe cómo entraron |
| CVE | **No consta ninguno** |
| Restitución y libertad supervisada | **No constan** |

### O-4.2 Lo que el comunicado NO dice, y por qué importa

Esta sección existe porque la diferencia entre el comunicado y su cobertura **podría cambiar una decisión de contratación**, y conviene que quien la tome sepa sobre qué se apoya.

| Afirmación corriente en el sector | ¿Está en el comunicado 26-431? |
|---|---|
| Los tres trabajaban en ciberseguridad | **SÍ**, textualmente |
| Goldberg era responsable de respuesta a incidentes en una empresa de seguridad concreta | **NO.** El comunicado no nombra ninguna empresa ni da ningún cargo |
| Martin era negociador en una empresa concreta | **NO.** Misma ausencia |
| **Atacaron a organizaciones que eran sus clientes** | **NO para Goldberg y Martin.** El comunicado no afirma relación contractual previa con las víctimas |
| Martino abusó de su posición como negociador de víctimas | **SÍ**, y es la única afirmación de abuso de posición del documento |
| Extorsionaron a varias víctimas con éxito | **AMBIGUO.** Dice *«multiple victims»* y *«millions»* en general, pero sólo detalla **una** víctima con cifra |

**Tres consecuencias prácticas.**

**Primera, sobre el número de víctimas.** El comunicado se contradice en apariencia: habla de *«múltiples víctimas»* y de extorsionar *«millones»*, pero la única cifra concreta es una víctima y 1,2 millones. **La lectura prudente es que atacaron a varias y cobraron de una** —que es compatible con todo el texto—, y así se consigna. Quien necesite el número exacto debe ir al expediente judicial, no al comunicado.

**Segunda, sobre el relato dominante.** Que el comunicado no afirme la relación cliente-proveedor **no la refuta**: hay cobertura amplia y coherente que la sostiene, y es perfectamente posible que esté en los documentos del caso. Lo que este informe sostiene es más modesto y más seguro: **a fecha de hoy, esa pieza no está respaldada por la fuente primaria que todo el mundo cita**.

**Tercera, y es la que vale para esta cartera.** Este es el caso de atribución de fuente más limpio que el repositorio ha encontrado: **una narrativa unánime, verosímil, útil, y más amplia que su documento de respaldo.** No hubo que desconfiar de nada para detectarlo; bastó con leer el original. Es exactamente lo que la lección de colección de esta cartera prescribe, y la razón por la que se prescribe.

## O-6. El foro que usa el nombre, revisado el 21-11-2026

<!-- cti:detalle -->

A petición del consumidor de este informe se revisó `https://alphv.pro`. **Es un hallazgo con consecuencias, y la principal es de clasificación: no es lo que el nombre hace esperar.**

### O-6.1 Qué es

Un **foro de discusión criminal**, servido sobre XenForo, íntegramente en ruso, titulado `ALPHV`. Sus secciones visibles, transcritas y traducidas:

| Sección, literal | Traducción |
|---|---|
| `Кардинг/Хакинг` | **Carding / Hacking** |
| `Новости. Хакинг. Кардинг. Мошенники. Криминал.` | Noticias. Hacking. Carding. Estafadores. Delincuencia |
| `Мессенджеры. Соцсети.` | Mensajería. Redes sociales |
| `Гарант Форума` · `Гарант \| Escrow` | **Garante del foro · Garante / Escrow** |
| `Депозит` · `Страховой депозит` | **Depósito · Depósito de seguro** |
| `Платное повышение` | **Promoción de pago** |
| `Зеркала форума` | Espejos del foro |

Declara **7.124 temas, 19.106 mensajes y 11.002 usuarios**, y exige contacto por Telegram con confirmación por mensaje privado en el propio foro.

### O-6.2 Lo que NO es, y por qué importa más que lo que es

**No hay sitio de filtración. No hay víctimas listadas. No hay negociación de rescates. No aparece la palabra «ransomware» ni «extorsión» en el contenido servido.**

Aplicando el criterio más barato y discriminante del `Anexo D` de `CTI-2026-042` —**cómo contacta la víctima: portal de negociación es una operación, dirección de correo es una herramienta**—, este sitio **no tiene víctima a la que contactar**. Lo que tiene es depósito, garante y promoción de pago, que son los mecanismos de un **mercado entre delincuentes**, no de una operación contra terceros. **Es una tercera categoría que el triaje de `042` no contemplaba**, y conviene que quede escrita: *mercado* es tan distinto de *operación* como lo es *herramienta*.

### O-6.3 Las fechas, que son lo que resuelve la atribución

Esto es lo verificable, y cuesta un minuto con `whois`:

| Objeto | Fecha | Qué implica |
|---|---|---|
| **Cese de la operación ALPHV** | **2024-03-03** | Medición propia (`KJ-1`) |
| **Registro de `alphv.io`** | **2024-11-02** | **Ocho meses POSTERIOR al cese** |
| Última actualización de `alphv.io` | **2026-11-19** | **Hace dos días.** Dominio mantenido |
| Registro de `oplotflow.net`, sus servidores de nombres | **2026-11-10** | **Hace once días.** Infraestructura DNS renovada |
| Contenido más reciente visible en portada | **2026-06-27** | Cinco meses. Portada menos viva que la infraestructura |

**El argumento de atribución es simple y es de calendario: un dominio registrado ocho meses después de que una operación desapareciera no puede ser su infraestructura.** Podría ser obra de antiguos participantes —eso no se puede descartar y no se afirma— pero **no es continuidad de la operación**, y cualquier producto que presente este foro como «ALPHV sigue activo» estaría cometiendo un error que se refuta con una consulta de registro.

> **Y una discrepancia interna que conviene registrar sin resolverla.** La infraestructura se renovó hace once días y el dominio se actualizó hace dos, pero **el contenido más reciente visible en la portada es de junio de 2026**. Las dos cosas son compatibles con un foro en declive cuyos administradores mantienen el alojamiento, y también con una portada que muestra temas fijados y no recientes. **No se ha entrado al foro —no se creó cuenta ni se envió ningún formulario—, así que la actividad real interna no se ha medido** (`G-6`).

### O-6.4 El prefijo legible, que conecta con el método de la casa

El foro declara un servicio oculto cuyos **seis primeros caracteres son `alphvi`**. Es el mismo patrón que `CTI-2026-057` y `CTI-2026-058` analizaron y que esta cartera tiene como mecanismo propio en su grafo: **generación dirigida de dirección para que la marca sea legible**, lo que la hace **cazable por patrón**.

**Consecuencia operativa, y es la única acción proactiva de este expediente:** si este foro migra de infraestructura y mantiene la práctica, **se le puede localizar buscando el prefijo antes de que anuncie la dirección nueva**. Es exactamente lo que la sección `X-1` **de `CTI-2026-058`** propuso para otro actor.

### O-6.5 Las señales de riesgo de estafa, dichas como lo que son

El sitio presenta **depósito de seguro, promoción de pago, servicio de garante propio y contacto obligatorio por Telegram**. Esa combinación es a la vez el modelo de negocio normal de un foro criminal **y** el patrón clásico de una estafa dirigida a aspirantes a delincuentes.

**Este informe no decide cuál de las dos cosas es**, porque decidirlo exigiría entrar, depositar y perder dinero, y **no se ha hecho ni se recomienda hacerlo**. Se consigna porque un analista que vea este dominio en un registro propio debe saber que **la presencia de un usuario de su organización en este foro admite dos lecturas muy distintas**: participación en un mercado criminal, o víctima de un fraude.

## O-5. Hipótesis sobre el estado actual

**H-1.** *La marca está definitivamente extinta y no volverá.* **Muy probable** *(80–95 %)*. Apoyo: treinta y dos meses sin actividad coherente, infraestructura incautada en diciembre de 2023, administradores desaparecidos con el dinero de sus propios afiliados —lo que destruye la reputación necesaria para reclutar— y tres afiliados condenados. **Una marca de extorsión como servicio vive de la confianza de sus afiliados, y ésta la quemó por completo.**

**H-2.** *Los afiliados se dispersaron a otras marcas y siguen activos.* **Probable** *(55–80 %)*. Apoyo: es lo que ha ocurrido en todos los casos documentados de colapso de un programa, y los vendedores lo afirman. **Pero no se ha verificado ni una sola correspondencia concreta en este informe**, y sin eso la afirmación no es accionable: no dice a quién vigilar (`G-3`).

**H-3.** *Alguien reutilizará el nombre.* **OBSERVADO el 21-11-2026, ya no es hipótesis** *(≥99 %)*. El nombre está reutilizado por un **foro criminal de carding y hacking** cuyo dominio se registró ocho meses después del cese (`KJ-11`, `O-6`). **Y el resultado confirma la cautela que esta hipótesis anticipaba, por una vía distinta de la prevista:** no es un actor de extorsión con marca heredada, es **otra clase de objeto con el mismo nombre**, que es exactamente el error que `CTI-2026-035` documentó al encontrar cuatro cosas compartiendo un nombre. **Quien busque «ALPHV» en 2026 encontrará antes este foro que el expediente del grupo extinto.**

**H-4.** *El catálogo seguirá produciendo falsos positivos de actividad.* **Muy probable** *(80–95 %)*. Apoyo: las cinco entradas imposibles siguen ahí hoy, treinta y dos meses después, y nada indica que vayan a corregirse.

---

# NIVEL TÁCTICO

## T-1. Por qué este nivel es corto, y qué contiene

Sin muestras y sin telemetría propia, lo táctico que este informe puede ofrecer no es cómo operaba el cifrador —eso está en los informes de proveedor de 2022 y 2023— sino **lo único táctico que el expediente judicial aporta y que sigue siendo aplicable: la figura del afiliado con posición de confianza**.

## T-2. El afiliado con acceso legítimo, que es lo que queda vigente

De todo el expediente, **la pieza que no caduca con la marca** es la que describe el comunicado sobre Martino: un negociador de rescates que **compartía información confidencial de las víctimas con los atacantes para aumentar el rescate pagado**.

Eso no es una técnica de ALPHV. Es una **clase de riesgo del proceso de respuesta a un incidente**, y sobrevive al actor porque el proceso sigue existiendo.

**Qué información tiene un negociador de rescates que aumenta el valor de un rescate.** No hace falta especular: es la información que su posición le da por definición.

| Información | Por qué sube el precio si llega al atacante |
|---|---|
| Límite real de autorización de pago | El atacante sabe hasta dónde puede pedir |
| Estado y alcance de las copias de seguridad | Si no hay recuperación viable, la presión es total |
| Cobertura de la póliza de ciberseguro | Fija un suelo y a menudo un techo del que el atacante no bajará |
| Urgencia operativa o regulatoria | Un plazo legal o un cierre de ejercicio es una palanca |
| Disposición interna a pagar | Convierte la negociación en un trámite |

**Lo que esto implica para quien contrata.** La lista anterior **es exactamente la información que hay que compartir con un negociador para que negocie**. No se puede resolver reteniéndola. Se resuelve de dos maneras, y las dos son organizativas y no técnicas:

1. **Compartimentación del dato más sensible.** El límite de autorización y la cobertura del seguro no necesitan estar en poder del negociador desde el primer minuto: pueden entregarse por tramos, según avance la negociación.
2. **Separación de proveedores.** Que quien negocia no sea quien responde técnicamente al incidente, y que ninguno de los dos sea quien va a facturar la recuperación. **La concentración de los tres papeles en un proveedor concentra también la oportunidad.**

> **Y el límite de esta recomendación, dicho con claridad.** El comunicado del Departamento de Justicia **sólo documenta este abuso en uno de los tres condenados y en su papel de negociador**. No se ha establecido en fuente primaria que los otros dos actuaran contra clientes propios (`O-4.2`). Por tanto **esta sección propone compartimentación y separación de papeles como buena práctica de proceso, no como respuesta a una amenaza cuantificada.** Quien necesite dimensionar el riesgo real de esta figura antes de reorganizar su contratación tiene una brecha de inteligencia delante, no un dato (`G-4`).

## T-3. Lo que NO se debe hacer con este expediente

- **No construir detección sobre los indicadores técnicos históricos de ALPHV.** Tienen entre tres y cuatro años y pertenecen a una operación extinta. Ocuparían espacio en una consola y no dispararían nunca.
- **No tratar el caso judicial como base para desconfiar del sector de respuesta a incidentes en bloque.** Tres personas condenadas no son una tasa, y el comunicado no permite calcular ninguna.
- **No citar «1.000 víctimas» y «731 entradas» como si fueran la misma medida.** Son poblaciones distintas (`O-1`).

---

## 14. Brechas de inteligencia y requisitos de colección

**G-1. No se ha leído ningún documento judicial del caso, sólo el comunicado de prensa.** De ello depende resolver `KJ-5`: la relación contractual entre los acusados y las víctimas, los empleadores y el número exacto de víctimas extorsionadas con éxito están, si están en algún sitio, en el escrito de acusación y en los documentos de la vista. **Es la brecha más barata de cerrar del expediente** y la que más cambiaría lo que este informe puede afirmar.

**G-2. No se sabe qué produjo las cinco entradas con fecha imposible.** Puede ser el enriquecedor, la reclamación original o un formato de fecha ambiguo. El sitio está caído desde 2024, así que la reclamación original es inaccesible. **No afecta a la conclusión** —las cinco se descartan igual— pero sí a saber si el mismo fallo contamina otros actores del catálogo.

**G-3. No se ha verificado ni una correspondencia concreta de afiliados dispersados a otras marcas.** Es una afirmación repetida por vendedores que esta cartera no puede sostener ni refutar, y mientras no haya una correspondencia nominal **no es accionable**: no dice a quién vigilar.

**G-4. No se puede dimensionar el riesgo de la figura del proveedor de confianza desleal.** Tres condenas no son una tasa. Para que la recomendación de `T-2` deje de ser buena práctica y pase a ser respuesta proporcionada hace falta saber cuántos casos de este tipo se han documentado, y no se ha buscado sistemáticamente.

**G-5. No se ha medido si las 402 entradas sin país difieren sistemáticamente de las 329 etiquetadas.** La hipótesis del sesgo por dominio genérico de `E-2.1` es razonada y **no está comprobada**. Comprobarla exigiría clasificar los dominios por extensión, que es posible y no se ha hecho.

**G-6. No se ha medido la actividad interna real del foro de `O-6`.** La portada declara 19.106 mensajes y muestra contenido de hace cinco meses. **Resolverlo exigiría crear una cuenta, y no se ha hecho**: el informe se detuvo en la lectura del contenido servido públicamente. Mientras no se mida, no se puede decir si el foro está vivo, en declive o es un escaparate.

**G-7. No se ha contrastado el servicio oculto del foro con el histórico de infraestructura del grupo extinto.** Es la única vía que podría establecer —o descartar del todo— una relación de personas entre el foro y la operación, y requiere histórico de DNS y de certificados que este entorno no tiene.

**Disparadores de reevaluación.** `I-1`: **publicación de la sentencia de Angelo Martino**, prevista para el 9 de julio, que cerraría el expediente judicial —y cuyo resultado este informe **no da por conocido**—. `I-2`: aparición de cualquier reclamación nueva bajo el nombre ALPHV o BlackCat, que activaría `H-3` y obligaría a tratarla como actor nuevo. — **CUMPLIDO el 21-11-2026 con un resultado distinto del previsto:** el nombre aparece en un **foro criminal** (`KJ-11`, `O-6`), no en una reclamación de extorsión. **El disparador se reescribe para la próxima revisión:** lo que hay que vigilar ahora es la aparición de un **sitio de filtración con víctimas listadas** bajo este nombre, que sería lo que este disparador quería detectar y que a día de hoy no existe. `I-3`: **publicación de los documentos judiciales del caso**, que resolvería `G-1` y `KJ-5`. `I-4`: aparición de una correspondencia nominal verificada entre un afiliado de ALPHV y una marca activa, que cerraría `G-3`. `I-5`: que el catálogo corrija las cinco entradas imposibles, lo que indicaría que la fuente revisa su histórico. `I-6`: confirmación pública por cualquiera de las dos organizaciones chilenas, que convertiría una reclamación en brecha.

---

# ANEXOS

## Anexo A — Indicadores

### A.1 — Lo que NO se publica, y por qué

<!-- cti:ioc -->

> **Este anexo es deliberadamente pobre, y la pobreza es el mensaje.** Un informe de cierre de una operación extinta **no debe distribuir indicadores técnicos**: los del cifrador de ALPHV tienen tres o cuatro años, la infraestructura está incautada o caída desde 2023-2024, y cargarlos en una consola sólo consume espacio. Lo que sigue es lo único de este expediente con valor operativo hoy.

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| `artefacto` | **La marca `ALPHV` / `BlackCat` / `Noberus` como atribución** | **Extinta desde 2024-03-03.** Una atribución a este nombre en un incidente de 2026 es casi con seguridad un error, una reutilización de nombre (`H-3`) o un cifrador filtrado reutilizado | **Alta** | Sin caducidad | **Rechazar la atribución y pedir la base.** NUNCA es un indicador de bloqueo |
| `artefacto` | **Las cinco entradas del catálogo con fecha de ataque posterior a 2024-05-01** | Descubiertas todas el **2023-07-26**: incoherencia interna verificable (`O-2.2`) | **Alta: medición propia** | Sin caducidad | **Descartar como evidencia de actividad.** No bloquear nada |
| `pattern` | **Comprobación `fecha_de_ataque > fecha_de_descubrimiento`** | **El correctivo reutilizable del expediente.** Aplicable a cualquier actor de cualquier catálogo, sin saber nada del actor | **Alta como método** | Sin caducidad | **Aplicar antes de citar cualquier «última actividad»** |
| `pattern` | **Información de negociación de rescate en poder de un tercero: límite de autorización, estado de copias, cobertura de póliza** | `T-2`. **La única pieza del expediente que no caduca con la marca**, porque describe el proceso y no al actor | **Moderada como control** | Sin caducidad | **Compartimentar por tramos y separar papeles de proveedor** |

### A.2 — Victimología, con sus dos bases de conteo

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| `cartera` | **731 entradas · última coherente 2024-03-03** | Medición propia del 2026-11-21. **No confundir con las «más de 1.000 víctimas» del DOJ**, que es otra población (`O-1`) | Alta como recuento | — | Análisis |
| `cartera` | **402 de 731 sin país (55,0 %)** | **La limitación central del expediente** (`KJ-2`). Invalida toda proporción geográfica | Alta como recuento | — | **Declarar la base de conteo en toda cita** |
| `cartera` | **32 entradas LATAM: 4,4 % del total · 9,7 % de las etiquetadas** | Las dos cifras son correctas y difieren en más del doble | Alta como recuento | — | **Citar con la base explícita** |
| `cartera` | **2 víctimas chilenas, 2023-04-02 y 2023-04-21** | Las dos con dominio, **ninguna con prensa**, ninguna confirmada (`KJ-3`) | **Moderada**: país derivado | — | **Comprobación del propio dominio** por la organización afectada |
| `cartera` | **Brasil 11 · México 7 · Colombia 4 · Argentina 2 · Chile 2 · Ecuador 2 · Rep. Dominicana 2 · Guatemala 1 · Panamá 1 · Venezuela 1** | Reparto regional de las entradas etiquetadas | Alta como recuento | — | Análisis |
| `cartera` | **Rescate 0,0 % · tamaño de datos 0,0 % · prensa 5,7 %** | **Toda cifra económica sobre este actor viene de fuera del catálogo** (`KJ-8`) | Alta como recuento | — | **No citar cifras económicas con esta fuente** |

### A.3 — Del expediente judicial

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| `artefacto` | **Reparto 20 % administradores / 80 % afiliado** | Confirmado en sentencia. **Patrón de medida para valorar lo que otros programas prometen** (`KJ-6`, `E-3`) | **Alta: fuente primaria** | Sin caducidad | Análisis y contraste |
| `artefacto` | **≈ 1,2 M USD en bitcoin, un solo rescate** | **La única cifra económica con respaldo judicial** del expediente | **Alta: fuente primaria** | Sin caducidad | Análisis |
| `artefacto` | **Periodo de actividad de los tres afiliados: abril–diciembre de 2023** | Comunicado 26-431 | **Alta: fuente primaria** | Sin caducidad | **Delimitación temporal para búsqueda retrospectiva** |
| `artefacto` | **Lo que el comunicado NO dice: empleadores, cargos, relación contractual con las víctimas** | `KJ-5`, `O-4.2`. **Si se cita, atribuir a prensa y no al DOJ** | **Alta: ausencia verificada por lectura directa** | Hasta que se publiquen los documentos del caso (`I-3`) | **Corregir la atribución en cualquier cita propia** |

### A.4 — El foro que usa el nombre, y por qué su acción permitida no es «bloqueo»

<!-- cti:ioc -->

> **Por qué los dominios llevan tipo `artefacto` y no `domain`.** Porque `domain` los metería en el agregado plano `ioc_url.txt`, que esta cartera distribuye como lista ingerible, y **la acción permitida de estas filas no es el bloqueo**. Con tipo `artefacto` quedan en el índice contextual con su explicación y no llegan a ninguna lista. Se comprobó empíricamente tras construir, y la primera versión de esta tabla **tenía esa incoherencia**: decía «no bloquear» en la columna de acción y el tipo los enviaba al agregado de todos modos.
>
> **Lectura obligada antes de usar esta tabla.** Estos valores son de un **foro criminal**, no de infraestructura de ataque. No son mando y control, no sirven carga útil y no atacan a nadie. **Una organización que los bloquee no se protege de ninguna intrusión**; lo único que consigue es impedir que alguien de su red llegue al sitio, que puede ser deseable por política y **no es una contramedida de seguridad**. La distinción importa porque meter esto en una lista de indicadores de compromiso produce alertas que nadie sabrá interpretar.

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| `artefacto` | `alphv.pro` | **Foro criminal en ruso** con secciones de carding y hacking, garante y depósito. Revisado el 2026-11-21 | **Alta: lectura propia** | 90 días | **Vigilancia.** Bloqueo defendible **por política de uso**, nunca como contramedida de intrusión |
| `artefacto` | `alphv.io` | Segundo dominio declarado por el propio foro. **Creado el 2024-11-02, ocho meses después del cese de la operación**; actualizado el 2026-11-19 | **Alta: `whois`** | 90 días | **Vigilancia.** Igual salvedad |
| `artefacto` | `oplotflow.net` | **Servidores de nombres de `alphv.io`.** Dominio creado el **2026-11-10**, registrador Spaceship, Inc. **Es el dato que fecha el mantenimiento activo** | **Alta: `whois`** | 90 días | **Vigilancia.** NO bloquear: es infraestructura DNS y el bloqueo tendría alcance imprevisible |
| `artefacto` | **Servicio oculto con prefijo legible `alphvi`** | `O-6.4`. **La única vigilancia proactiva del expediente**: permite localizar reaparición antes del anuncio | **Alta como método** | Hasta que aparezca una dirección suya sin prefijo | **Búsqueda proactiva por patrón** |
| `artefacto` | **`alphv.io` registrado 8 meses después del cese** | **El argumento de atribución del expediente** (`KJ-11`): un dominio posterior al cese no es infraestructura de la operación | **Alta: verificable por cualquiera** | Sin caducidad | **Refutar toda afirmación de que «ALPHV sigue activo»** |
| `pattern` | **Depósito de seguro · promoción de pago · garante propio · contacto obligatorio por Telegram** | `O-6.5`. Modelo de negocio de foro criminal **y** patrón clásico de estafa a aspirantes. **Indistinguibles sin depositar** | Moderada | Sin caducidad | **Alerta de doble lectura:** un usuario propio en este foro puede ser partícipe o víctima |
| `artefacto` | **Ausencia de sitio de filtración, de víctimas listadas y de negociación** | **Lo que prueba que no es una operación de extorsión** sino un mercado (`O-6.2`) | **Alta: lectura propia** | 90 días | **Clasificar como mercado, no como operación** |

## Anexo B — Fuentes y valoración

| # | Fuente | Naturaleza | Fiabilidad | Credibilidad | Uso en este informe |
|---|---|---|---|---|---|
| 1 | **Comunicado 26-431, Departamento de Justicia de EE. UU., 2026-04-30**, leído en original | **Primaria oficial** | **A** | **1** | **Base de `KJ-4`, `KJ-5`, `KJ-6`, `KJ-7` y de todo §O-4.** La fuente de más autoridad del expediente |
| 2 | **Catálogo público de reclamaciones de extorsión**, consultado el 2026-11-21 | Agregador de terceros | **C** | **3** | **Medición propia** de `KJ-1`, `KJ-2`, `KJ-3`, `KJ-8`, `KJ-9`. Su enriquecimiento de país se usa con la salvedad de `E-2.1` |
| 3 | Prensa especializada sobre el caso judicial | Secundaria | **C** | **3** | **Consignada y NO usada como base de ningún juicio.** Es el origen de los empleadores y de la relación cliente-proveedor (`KJ-5`) |
| 4 | Informes de vendedor sobre la salida fraudulenta de 2024 | Secundaria comercial | **C** | **3** | Consignada como plausible no verificada en `O-3.2`. Ningún juicio se apoya en ella |
| 5 | Informes de vendedor sobre el cifrador, 2022–2023 | Secundaria comercial | — | — | **No consultados ni citados.** Ver §3.4: este informe no hace nivel técnico |
| 6 | **Lectura propia de `https://alphv.pro`**, 2026-11-21, más consultas `whois` de `alphv.io` y `oplotflow.net` | **Observación directa** de contenido servido públicamente | **B** | **2** | **Base de `KJ-11` y de todo §O-6.** Se leyó sólo el contenido público: **no se creó cuenta, no se envió ningún formulario y no se descargó nada** (`G-6`) |

> **Nota sobre la fuente 3, que es la que exige explicación.** La cobertura de prensa de este caso es abundante, coherente entre medios y verosímil, y aporta datos —los empleadores, los cargos, la relación con las víctimas— que el comunicado oficial no contiene. **No se ha usado como base de ningún juicio** no porque se la considere falsa, sino porque la convención de esta cartera es que **un informe derivado no supera la confianza declarada por su origen**, y aquí el origen de esos datos concretos no es público ni identificable desde las notas. Se consigna con precisión qué parte viene de dónde para que quien decida sobre esta base sepa sobre qué pisa.

## Anexo C — Léxico de probabilidad y confianza

Se emplea el léxico de la directiva ICD 203. **Probabilidad** —casi con certeza ≥99 %, muy probable 80–95 %, probable 55–80 %, aproximadamente igual de probable 45–55 %, improbable 20–45 %, muy improbable 5–20 %, casi con certeza no ≤5 %— es la estimación sobre el mundo. **Confianza** —alta, moderada, baja— es la solidez de la base sobre la que se estima. **Las dos son independientes**, y este informe tiene varios juicios de probabilidad casi cierta con confianza alta porque son recuentos propios, y uno de probabilidad media con confianza baja porque es interpretación de una curva.

## Anexo D — Cómo leer el catálogo de una marca extinta sin inventar actividad

El método que este informe tuvo que improvisar, generalizado. **Cinco comprobaciones, en orden de coste creciente, y las tres primeras son diez minutos.**

**1 · Restar las dos fechas de cada entrada.** Si la fecha de ataque declarada es **posterior** a la fecha en que el rastreador descubrió la entrada, **la entrada es incoherente** y no sirve como evidencia de actividad. Es el primero de los ocho correctivos de `CTI-2026-054` y aquí eliminó quince meses de actividad fantasma con cinco entradas. **No requiere saber nada del actor.**

**2 · Mirar la forma del último año, desglosada por meses.** Un total anual bajo puede ser un declive —reparto uniforme— o un corte —todo concentrado al principio—. Aquí 62 entradas en 2024 parecían declive y eran corte: 57 de enero y febrero. **La diferencia cambia la hipótesis**: el declive sugiere desgaste interno, el corte sugiere un suceso externo con fecha.

**3 · Medir la cobertura de los campos antes de preguntarles algo.** Un catálogo con 0 % de cobertura de rescate no puede responder preguntas económicas, y uno con 45 % de cobertura de país no puede dar proporciones geográficas. **Medir la cobertura cuesta una consulta y evita publicar una cifra inventada.**

**4 · No convertir recuentos en proporciones cuando falta más de un tercio de un campo.** Y si se hace, **dar las dos cifras y decir qué divide cada una**. La tentación es dividir sólo por lo etiquetado, lo que supone que los huecos se reparten como el resto: hay que justificar ese supuesto o renunciar a la proporción.

**5 · Buscar la fuente primaria del cierre, no la cobertura del cierre.** Una operación extinta suele tener un suceso terminal documentado —una incautación, un procesamiento, una desarticulación—. **Leer ese documento en original es lo que distingue un informe de cierre de un resumen de prensa**, y en este caso produjo el hallazgo de `KJ-5`.

> **Y la regla que engloba las cinco:** una marca extinta **no deja de generar datos**. Deja de generar actividad. Los catálogos siguen devolviendo sus entradas, sin aviso de que la operación terminó, y los productos derivados que no apliquen el punto 1 la presentarán como activa. **El riesgo de una marca muerta no es que ataque: es que contamine la atribución de los vivos.**

## Anexo E — Marcos de referencia empleados

| Marco | Uso |
|---|---|
| **ICD 203** | Léxico de probabilidad y confianza de todos los juicios (`Anexo C`) |
| **Escala de fiabilidad y credibilidad de fuentes** | Valoración del `Anexo B`, con la nota explícita sobre la fuente 3 |
| **`Anexo D` de `CTI-2026-054`** | Los ocho correctivos para citar un rastreador. El primero es la base de `KJ-1` |
| **`Anexo D` de `CTI-2026-048`** | Escala de prueba de ocho niveles. Usada para calificar el 93,8 % de capturas de pantalla como prueba de nivel 3 |
| **`Anexo D` de `CTI-2026-042`** | Triaje de actor. No se aplica: el actor no es nuevo, es extinto |
| **`CTI-2026-015`** | Referencia de prioridad chilena con la que se contextualizan las dos víctimas de `KJ-3` |

## Anexo F — Paquete legible por máquina

**Para que una organización compruebe si fue una de las dos víctimas chilenas, sin que este informe publique ningún nombre:**

```
1. Consultar el catálogo por grupo:
   GET https://api.ransomware.live/v2/groupvictims/alphv
   (cabecera User-Agent propia; cortesía con un servicio gratuito de tercero)

2. Filtrar por el dominio PROPIO de la organización, sobre el campo `domain`.

3. Si hay coincidencia, los campos útiles son:
   `attackdate`   — fecha de ataque declarada por el adversario
   `discovered`   — cuándo lo vio el rastreador
   `screenshot`   — si hay captura (93,8 % de las entradas la tiene)
   `claim_url`    — la reclamación original, HOY INACCESIBLE: el sitio está caído

4. Comprobación de coherencia OBLIGATORIA antes de dar crédito a la fecha:
   si `attackdate` > `discovered`, la fecha de ataque es artefacto (§O-2.2).

5. Lo que una coincidencia significa y lo que no:
   significa que el adversario RECLAMÓ esa organización en abril de 2023.
   NO significa que hubiera brecha, ni que los datos se publicaran,
   ni que siga habiendo exposición. Ninguna de las dos chilenas
   tiene referencia de prensa, y ninguna confirmó nada públicamente.
```

**Y la comprobación reutilizable de `Anexo D`, punto 1**, aplicable a cualquier actor:

```
incoherentes = [e for e in entradas
                if e['attackdate'][:10] > e['discovered'][:10]]
# Si la lista no está vacía, NINGUNA de esas entradas sirve para
# fechar la última actividad del actor.
```

## Anexo G — Control de cambios

| Versión | Fecha | Qué cambió | Qué juicio se movió |
|---|---|---|---|
| 1.0 | 2026-11-21 | Emisión inicial. Informe de cierre de una operación extinta, con dos hallazgos propios: **las cinco entradas con fecha de ataque posterior a su propia fecha de descubrimiento**, que desplazan la última actividad de junio de 2025 a marzo de 2024 (`KJ-1`); y **la discrepancia entre el comunicado del Departamento de Justicia y la narrativa del sector** sobre el caso de los tres afiliados, que no nombra empleadores ni afirma relación cliente-proveedor (`KJ-5`). Incluye la medición de cobertura que invalida toda proporción geográfica del actor (`KJ-2`), el expediente chileno cerrado de dos reclamaciones (`KJ-3`), el reparto 20/80 documentado judicialmente (`KJ-6`), el apoyo policial mexicano en la captura (`KJ-7`), y el `Anexo D` con las cinco comprobaciones para leer el catálogo de una marca extinta. **Incluye además la revisión del foro `alphv.pro`** (`KJ-11`, `O-6`), pedida por el consumidor durante la redacción: un foro criminal en ruso que usa la marca y cuyo dominio se registró **ocho meses después del cese**, lo que convierte `H-3` de hipótesis en observación y cumple el disparador `I-2` con un resultado distinto del previsto | — |

## Anexo H — Realimentación del consumidor

Este informe se corrige si se recibe: **los documentos judiciales del caso**, que resolverían `KJ-5` y `G-1` y podrían confirmar la narrativa que hoy sólo sostiene la prensa; la **sentencia de Angelo Martino** (`I-1`), que este informe deja expresamente como desconocida; cualquier **reclamación nueva bajo el nombre** (`I-2`); una **correspondencia nominal verificada** de un afiliado con una marca activa (`G-3`); una medición que **confirme o refute el sesgo por dominio genérico** de `E-2.1` (`G-5`); o **confirmación pública de cualquiera de las dos organizaciones chilenas** (`I-6`).

**Y una petición concreta a quien use este expediente:** si cita el caso judicial en un producto propio, **compruebe la atribución**. La diferencia entre «el Departamento de Justicia estableció que atacaron a sus clientes» y «la prensa especializada informa de que atacaron a sus clientes» es la diferencia entre un hecho probado y una afirmación verosímil, y este informe existe en parte para que esa distinción no se pierda.
