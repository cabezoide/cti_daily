---
tlp: "TLP:CLEAR"
pap: "PAP:WHITE"
id: "CTI-2026-018"
version: "1.0"
tipo: "Evaluación estratégica"
foco_regional: "Global · Latinoamérica · Chile"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "Abuso de dominios de primer nivel"
fecha: "2026-11-15"
caduca: "2027-02-15"
autor: "Célula CTI"
distribucion: "Elaborado íntegramente con fuentes abiertas y datos primarios publicados. Difusión libre, conservando la atribución de las fuentes y las salvedades metodológicas de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-018
## El abuso de TLD no se concentra donde se mide: `.com` lidera por volumen, y once gTLD baratos pasan del 10 % de su zona
### Doce meses de datos primarios (may-2025 → abr-2026) y cuatro trimestres de seguimiento

> **Regla de oro del producto:** todo párrafo debe responder a un requisito de
> inteligencia (PIR) y habilitar una decisión. Si un párrafo no cambia lo que
> alguien va a hacer, va al anexo o se borra.

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-018` |
| Versión / fecha | `1.0` — 2026-11-15 |
| Tipo de producto | Evaluación estratégica (infraestructura y ecosistema, no actor) |
| Niveles cubiertos | Estratégico · Operacional · Táctico · Técnico |
| Foco regional | Global, con lectura específica para Latinoamérica y Chile |
| Marcado de difusión | `TLP:CLEAR` · `PAP:WHITE` |
| Clasificación interna | Uso interno — no sensible |
| Requisitos atendidos | `PIR-02` (superficie de phishing y suplantación de marca), `PIR-06` (política de bloqueo y listas de reputación), `PIR-09` (indicadores tempranos de campaña) |
| Solicitante / consumidor primario | Jefatura de SOC · Ingeniería de Detección · Administración de proxy/DNS · Comité de Riesgo Operacional |
| Ventana de observación | 2025-05-01 → 2026-09-30 (datos anuales may-25/abr-26 + cuatro trimestres de seguimiento hasta sep-2026) |
| Base de colección | 4 conjuntos de datos primarios (CSV y PDF de origen, no resúmenes de prensa): Interisle / Cybercrime Information Center —tablas anuales y 4 trimestrales de phishing, 3 trimestrales de malware—, Spamhaus Domain Reputation Update abr-sep 2026 y oct-25/mar-26, lista oficial de TLD de IANA (versión 2026111500), y el repositorio público de IoC `intellroom/IoC` (550 ficheros) medido por nosotros. **Sin telemetría propia incorporada** |
| Autor (analista) | Célula CTI |
| Revisión por pares | Pendiente |
| Aprobación | Pendiente |
| Caducidad / revisión | 2027-02-15, o antes si Interisle publica el trimestre ago-oct 2026, si Spamhaus publica el informe oct-26/mar-27, o si un gTLD supera el 20 % de su zona listada |
| Productos relacionados | `CTI-2026-014` (TheGentlemen), `CTI-2026-015` (Qilin), `CTI-2026-016` (LockBit 5.0), `CTI-2026-017` (FamousSparrow). **Este producto es transversal a los cuatro:** no describe un adversario, describe el insumo de infraestructura que todos ellos compran |
| Paquete legible por máquina | Pendiente de generar (véase §14) |

<!-- cti:note type="warn" -->

> **Limitación estructural de este producto.** Se ha elaborado con datos primarios de
> terceros y con medición propia de un repositorio público, pero **sin telemetría de la
> organización**. Por tanto **§O-4 (nuestra exposición) está sin rellenar**: no sabemos
> qué proporción del tráfico saliente propio va a los TLD de alto riesgo, ni cuántos
> dominios parecidos a nuestra marca existen en ellos. Hasta que se rellene, toda
> recomendación de bloqueo de §E-4 es una hipótesis de política, no una decisión evaluada.

<!-- cti:note type="warn" -->

> **Advertencia metodológica que invalida la mayoría de los rankings publicados — léase
> antes que cualquier otra cosa.** Existen dos métricas incompatibles y la prensa técnica
> las mezcla sistemáticamente. **Volumen** (cuántos dominios maliciosos tiene un TLD)
> premia a los TLD grandes: `.com` encabeza todas las listas porque tiene 162 millones de
> dominios, no porque sea peligroso —solo el 0,54 % de su zona aparece en phishing—.
> **Tasa** (dominios maliciosos / tamaño de la zona) identifica dónde el abuso es
> estructural. Las dos listas comparten pocos nombres. **Una lista única de «TLD más
> usados en ciberataques» no es accionable**: según la métrica elegida, el primer puesto
> es `.com` o es `.xin`, y las decisiones que se derivan son opuestas.

<!-- cti:note type="warn" -->

> **Segunda advertencia: phishing y malware no comparten TLD.** El phishing vive en gTLD
> nuevos y baratos registrados maliciosamente (74 % de los dominios de phishing del
> período fueron registrados con ese fin, no comprometidos). La distribución de malware
> vive en `.com`, `.ru`, `.org`, `.net` y ccTLD europeos, porque se apoya en **sitios
> legítimos comprometidos**. Aplicar la lista de phishing a la detección de malware
> produce cobertura casi nula; aplicar la de malware al phishing produce bloqueo masivo
> de infraestructura legítima.

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** **El abuso de TLD es un fenómeno de concentración extrema por registrador, no por
terminación.** En los diez TLD con mayor tasa de phishing del año, un único registrador
concentra entre el 18 % y el 97 % de los dominios maliciosos del TLD: `.garden` 97 % en
Spaceship, `.win` 87 % en Dominet (HK), `.mom` 76 % en NameSilo, `.mobi` 73 % en Eranet,
`.help` 67 % en NameSilo, `.rest` 63 % en NameCheap. Valoramos **muy probable** *(80–95 %)*
que la tupla **TLD + registrador + edad del dominio** sea un discriminante sustancialmente
mejor que el TLD aislado. **Confianza: alta.** *Base:* cálculo propio sobre el CSV primario
de Interisle con los 233 TLD del período; la columna de registrador dominante viene en el
propio conjunto de datos.

**KJ-2.** **Nueve gTLD superan el umbral que la industria considera indicativo de un TLD
problemático, y ninguno de ellos aparece en los titulares.** Con el criterio de Spamhaus
—5 % de la zona listada es señal de alarma, por encima del 10 % indica un TLD
problemático—, en el año `.xin` tiene el **59,1 %** de su zona en phishing, `.win` 16,4 %,
`.icu` 16,1 %, `.garden` 15,7 %, `.cfd` 13,9 %, `.pro` 12,0 % y `.help` 10,6 % (siete).
En el semestre abr-sep 2026 Spamhaus mide `.help` en **26,5 %** —el valor más alto de todo
el conjunto de datos—, `.qpon` 15,1 % y `.study` 12,4 %, lo que añade dos nombres nuevos.
Justo por debajo del umbral quedan `.mom` (10,0 %) y `.rest` (9,8 %). Esto es **hecho
medido**, no estimación. **Confianza: alta.**

**KJ-3.** **La dinámica trimestral es tan grande que cualquier lista estática caduca en un
trimestre.** `.top` osciló entre 161.534 y 57.316 dominios de phishing en cuatro
trimestres; `.cn` se multiplicó por 3,7 en un solo trimestre (39.798 → 147.217) y pasó a
segundo lugar mundial; `.garden` pasó de no estar rankeado en marzo de 2026 a top-5 mundial
por tasa; `.cfd` cayó un 53 % y bajó del 17,54 % al 7,01 % de su zona listada. Valoramos
**muy probable** *(80–95 %)* que una lista de bloqueo por TLD fijada hoy y no revisada esté
desalineada en menos de seis meses. **Confianza: alta.** *Base:* cuatro trimestres
consecutivos de datos primarios más dos semestres de Spamhaus.

**KJ-4.** **El volumen total de abuso está creciendo, no estabilizándose.** Spamhaus
registró 3,37 millones de dominios maliciosos o sospechosos en abr-sep 2026, un **+56,6 %**
sobre el semestre anterior, con **1,15 millones solo en septiembre de 2026 — el máximo
mensual de su serie histórica**. Dentro de ese agregado, los C&C de botnet en dominios
comprometidos crecieron **+145 %**. Valoramos **probable** *(55–80 %)* que la tendencia
continúe en el semestre oct-26/mar-27. **Confianza: moderada.** *Base:* serie de un único
proveedor; el propio informe advierte que parte del alza se debe a mejoras en su ingesta de
datos y al listado preventivo de carteras completas de dominios, es decir, **parte del
crecimiento es de medición, no de amenaza**.

**KJ-5.** **Las campañas dirigidas de alto impacto ocurren en gTLD de nicho que ningún
ranking global detecta.** La medición propia del repositorio `intellroom/IoC` encontró
**317 dominios `.report`** registrados entre el 18-08 y el 16-09-2026 que copian
identificadores reales de tenants de Okta, de los cuales **33 fueron verificados de forma
independiente** contra celdas Okta activas, con marcas reconocibles de salud, seguros y
logística. **`.report` no aparece en ningún top-20 mundial, por ninguna métrica.** Valoramos
**probable** *(55–80 %)* que el patrón se repita en otros gTLD de bajo volumen y semántica
corporativa creíble. **Confianza: moderada.** *Base:* medición propia reproducible sobre
datos publicados; la atribución a un actor nombrado **no está confirmada** y la propia
fuente original usó la palabra «potencial».

**KJ-6.** **La diversificación deliberada de TLD dentro de una misma campaña ya es práctica
estándar y degrada el bloqueo por terminación.** Dos campañas de 2026 medidas en el
repositorio lo muestran: Macfinger (ClickFix contra macOS) usó **56 dominios de cargador
repartidos en nueve terminaciones** (`.life`, `.live`, `.xyz`, `.com`, `.icu`, `.space`,
`.site`, `.lol`, `.digital`) con rotación casi diaria; Phexia (C2 de macOS) repartió 71
dominios entre `.com`, `.xyz`, `.digital`, `.pro`, `.sbs`, `.top` y `.beer`. Valoramos
**muy probable** *(80–95 %)* que bloquear por TLD obligue al adversario solo a cambiar de
terminación, a coste cercano a cero. **Confianza: alta.**

**KJ-7.** **El `.cl` aparece en los datos como víctima, no como vector.** `.cl` tiene una
tasa de phishing baja (score 11,1; 0,11 % de su zona). Los 914 dominios `.cl` que
encontramos en el repositorio provienen de un único barrido de webshells expuestas, es
decir, **sitios chilenos comprometidos**. En cambio, el smishing que suplanta marcas
chilenas se aloja en `.top`, `.icu`, `.vip`, `.autos`, `.shop` y `.space`. Valoramos
**probable** *(55–80 %)* que la exposición chilena se concentre en dos frentes distintos:
WordPress comprometido en `.cl` como plataforma de distribución, y gTLD baratos extranjeros
como plataforma de suplantación. **Confianza: moderada.** *Base:* una sola fuente de
indicadores regional, con sesgo de colección declarado en §3.3.

**Qué cambiaría estos juicios:** que la concentración por registrador se diluyera en el
próximo trimestre (rompería KJ-1 y con él toda la lógica de detección de §X-3); que `.cn`
sostuviera el primer puesto mundial dos trimestres seguidos (convertiría un pico en
estructura y obligaría a reescribir §E-3); o que telemetría propia mostrara que el tráfico
legítimo del negocio hacia los TLD de alto riesgo es material (invalidaría §E-4).

---

## 2. Resumen ejecutivo

El nombre de dominio es el insumo más barato de la cadena de ataque, y el mercado que lo
suministra está midiendo mal su propio problema. Durante los doce meses de may-2025 a
abr-2026 se reportaron **3.071.768 dominios de phishing** repartidos en 233 TLD, y **tres
de cada cuatro fueron registrados con ese fin desde el principio** —no son sitios legítimos
comprometidos—. Eso significa que hubo un momento, antes del ataque, en que alguien pagó
por ese dominio en un registrador concreto: es el punto de intervención más temprano y más
barato de toda la cadena.

La mala noticia operativa es que la respuesta intuitiva —bloquear las terminaciones
sospechosas— no funciona y además es cara. Las campañas reparten su infraestructura entre
seis y nueve terminaciones distintas, rotan a diario y cambiar de TLD les cuesta unos
dólares. Y los TLD con peor tasa de abuso siguen alojando negocio legítimo: bloquear `.pro`
o `.live` por completo tiene un coste de falsos positivos que ninguna organización va a
aceptar.

La buena noticia es que el abuso está concentrado en un puñado de pares registro-registrador
identificables por nombre, y que la combinación de terminación, registrador y edad del
dominio es un discriminante fuerte y fácil de implementar en proxy, correo y DNS. Esto no
pide comprar nada: pide escribir reglas de puntuación y revisarlas cada trimestre.

Lo que se solicita a Dirección es, por tanto, modesto en coste y acotado en plazo: autorizar
una política de **cuarentena de dominios recién registrados** —no de bloqueo por
terminación—, financiar la vigilancia de marca en un conjunto nombrado de gTLD de nicho, y
aceptar que esta lista se revisa cada tres meses porque los datos demuestran que caduca.

<!-- cti:cards -->

| Rasgo del ecosistema | Qué significa para nosotros | Etiqueta |
|---|---|---|
| El dominio malicioso cuesta unos dólares y se registra días antes del ataque | La edad del dominio es nuestra señal más fuerte y la más fácil de obtener; el 74 % de registro malicioso convierte la cuarentena de NRD en la medida de mayor rendimiento por esfuerzo | `01 · economía` |
| El abuso se concentra en pocos pares registro-registrador, no en terminaciones | Podemos construir puntuación con nombres propios y pocas reglas, en vez de listas de cientos de TLD imposibles de mantener | `02 · concentración` |
| Las campañas reparten su infraestructura en 6–9 terminaciones y rotan a diario | El bloqueo por TLD traslada el problema sin resolverlo; el pivote duradero es el proveedor de alojamiento y el patrón de nombre, no el sufijo | `03 · elasticidad` |
| Phishing y malware habitan TLD distintos | Necesitamos dos políticas separadas: reputación por dominio para malware en TLD legítimos, puntuación por TLD solo para phishing y suplantación | `04 · doctrina` |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `3.071.768` | Dominios de phishing reportados en 12 meses (may-25 → abr-26) | Repartidos en 233 TLD distintos |
| `74 %` | Proporción registrada maliciosamente, no comprometida | Hay un punto de intervención antes del ataque |
| `59,1 %` | Porcentaje de la zona de `.xin` reportada en phishing | El umbral de «TLD problemático» de la industria es 10 % |
| `97 %` | Cuota del phishing de `.garden` en un único registrador | La concentración es la vulnerabilidad del adversario |
| `1,15 M` | Dominios maliciosos listados solo en septiembre de 2026 | Máximo mensual de la serie histórica de Spamhaus |
| `317` | Dominios `.report` suplantando tenants de Okta en 30 días | `.report` no figura en ningún top-20 mundial |

> ✅ **Decisión que se solicita a Dirección:** (a) autorizar cuarentena de 30 días para
> dominios recién registrados en el conjunto de TLD de §X-1, con excepción documentada por
> negocio — 30 días; (b) encargar el inventario de §O-4 para poder medir el coste real de
> esa política antes de aplicarla en modo bloqueo — 45 días; (c) incorporar los gTLD de
> nicho de §O-7 a la vigilancia de marca — 60 días.

---

## 3. Alcance, requisitos y limitaciones

**3.1 Requisitos de inteligencia atendidos**

| Req. | Enunciado | ¿Respondido? | Dónde |
|---|---|---|---|
| PIR-02 | ¿Dónde se aloja la infraestructura de suplantación que nos afecta y cómo se distribuye? | Sí | §E-1, §E-2, §X-1 |
| PIR-06 | ¿Qué política de bloqueo y reputación por TLD es defendible y sostenible? | Sí | §E-4, §X-3, §X-5 |
| PIR-09 | ¿Qué señales tempranas anticipan una campaña de suplantación contra nuestra marca? | Parcial | §O-7, §T-4 |
| PIR-04 | ¿Cuál es nuestra exposición concreta? | **No** | §O-4 — requiere telemetría propia |

**3.2 Fuera de alcance.** No evalúa actores concretos (véanse los informes 014 a 017). No
cubre abuso de subdominios en servicios de alojamiento gratuito —un vector creciente y
significativo que las métricas por TLD no capturan, porque el dominio padre es legítimo—. No
cubre homoglifos ni IDN. No cubre abuso de DNS dinámico. No evalúa proveedores comerciales
de inteligencia de dominios.

**3.3 Limitaciones de la colección.**

- **Dependencia de dos proveedores.** Casi todas las cifras provienen de Interisle/CIC y de
  Spamhaus. Ambos miden lo que sus fuentes de alimentación les reportan, no la realidad:
  Spamhaus lo dice de forma explícita en su propio informe. Un TLD con poco abuso reportado
  puede ser un TLD poco observado.
- **Contaminación por mejoras de medición.** Spamhaus atribuye parte del alza de abr-sep 2026
  a mejor ingesta de datos de *smishing* de operadoras estadounidenses y al listado
  preventivo de carteras de dominios enteras. **El crecimiento medido no es todo crecimiento
  real.**
- **Sesgos del repositorio `intellroom/IoC`, medido por nosotros.** Tres, todos aislados
  antes de usar el dato: *(i)* mezcla temporal —sus conjuntos más grandes (Formbook, Qakbot,
  Conficker, Lazarus) son de 2022-2023 y quedaron **excluidos** de toda cifra de este
  informe—; *(ii)* sesgo geográfico hacia Chile; *(iii)* mezcla de categorías —914 dominios
  `.cl` son víctimas con webshells expuestas, no infraestructura de atacante, y se contaron
  por separado—. Es un repositorio de un equipo pequeño, no una muestra representativa:
  **sirve para detectar patrones que los agregados ocultan, no para medir prevalencia.**
- **Ventana ciega.** No existe trimestre de phishing publicado posterior a may-jul 2026 ni
  tabla de malware posterior a jul-sep 2026. Las seis semanas más recientes no están
  cubiertas por ninguna fuente.
- **No se encontraron datos DAAR de ICANN de 2026** con desglose por TLD, que habrían dado
  un tercer punto de apoyo independiente.

**3.4 Metodología.** Descarga de los conjuntos primarios (CSV de 233 TLD, cuatro páginas
trimestrales de phishing, tres de malware, dos PDF semestrales de Spamhaus extraídos a
texto). Cálculo propio de los rankings anuales por volumen, por tasa y por registro
malicioso —las tablas publicadas están como imágenes, de modo que los rankings de §E-2 son
nuestros, derivados del dato crudo—. Para el repositorio: clonado, extracción de indicadores
de dominio con normalización de *defanging* (`[.]`, `hxxp`), validación contra la lista
oficial de TLD de IANA del 15-11-2026, descarte de falsos positivos por extensión de fichero
(`.sh`, `.py`, `.zip` se interpretaban como TLD), deduplicación a dominio registrable y
separación entre infraestructura de atacante y víctima. Técnicas analíticas estructuradas:
hipótesis alternativas competidoras (§O-6) y pre-mortem.

---

# NIVEL ESTRATÉGICO
### Para: Consejo · CISO · Riesgo Operacional · Compras de seguridad · Horizonte: 6–24 meses

## E-1. Qué representa este fenómeno en el panorama

El nombre de dominio es el único insumo de la cadena de ataque que se compra en un mercado
abierto, regulado y con nombres propios conocidos. Esa es a la vez la mala y la buena
noticia de este informe.

<!-- cti:cards -->

| Cambio estructural | Por qué nos afecta | Etiqueta |
|---|---|---|
| El 74 % de los dominios de phishing se registran maliciosamente | Existe una ventana de intervención **anterior** al ataque: la edad del dominio es señal, no metadato | `registro` |
| La barrera de entrada es de unos dólares por dominio | No se compite subiendo el coste del dominio, sino el coste de **usarlo sin ser visto** | `economía` |
| Un puñado de registradores concentra la mayoría del abuso de los peores TLD | El problema tiene nombres propios y es, en principio, remediable por política del registro | `gobernanza` |
| La mitigación funciona cuando se aplica: `.cfd` cayó del 17,54 % al 7,01 % de su zona | La presión sobre registros y registradores produce efectos medibles en un semestre | `palanca` |
| Pero el abuso se desplaza, no desaparece: mientras `.cfd` caía, `.help` subía al 26,5 % | El desplazamiento es la norma; la política debe apuntar al comportamiento, no al sufijo | `desplazamiento` |

> **Lectura estratégica.** El par `.cfd` / `.help` es el hallazgo más importante de este
> informe para el nivel de dirección: demuestra **a la vez** que la mitigación funciona y
> que no resuelve el problema. El abuso se comporta como un fluido: se presiona en un TLD y
> aparece en otro en el mismo semestre. Cualquier inversión planteada como «bloquear la
> lista de TLD malos» está comprando una foto de un fluido.

## E-2. Distribución del abuso — las dos tablas que no coinciden

**Por volumen** (may-2025 → abr-2026, cálculo propio sobre el CSV primario de 233 TLD):

| # | TLD | Dominios de phishing | % de su zona | % registrado maliciosamente |
|---|---|---|---|---|
| 1 | `.com` | 869.180 | 0,54 % | 66,5 % |
| 2 | `.top` | 375.514 | 5,96 % | 79,2 % |
| 3 | `.cn` | 167.651 | 1,36 % | 39,3 % |
| 4 | `.pro` | 130.945 | 12,00 % | 84,5 % |
| 5 | `.info` | 99.602 | 1,90 % | 71,8 % |
| 6 | `.xyz` | 93.987 | 1,18 % | 84,5 % |
| 7 | `.vip` | 83.816 | 5,01 % | 95,1 % |
| 8 | `.shop` | 79.625 | 2,02 % | 60,9 % |
| 9 | `.cc` | 77.660 | 3,19 % | 93,1 % |
| 10 | `.icu` | 74.786 | 16,07 % | 95,0 % |
| 11 | `.cfd` | 70.944 | 13,87 % | 95,1 % |
| 12 | `.sbs` | 63.518 | 4,64 % | 94,0 % |

**Por tasa**, que es el ranking del que se derivan decisiones:

<!-- cti:bars title="Porcentaje de la zona del TLD reportado en phishing (may-25 → abr-26)" -->

| TLD | % de la zona |
|---|---|
| `.xin` | 59,1 |
| `.win` | 16,4 |
| `.icu` | 16,1 |
| `.garden` | 15,7 |
| `.cfd` | 13,9 |
| `.pro` | 12,0 |
| `.help` | 10,6 |
| `.mom` | 10,0 |
| `.rest` | 9,8 |
| `.mobi` | 8,5 |
| `.qpon` | 8,2 |
| `.live` | 7,4 |
| `.ink` | 7,2 |
| `.best` | 7,1 |
| `.lat` | 6,6 |
| `.cyou` | 6,6 |
| `.top` | 6,0 |

> ⚠ **Lectura clave — la columna que decide.** Compárense las dos tablas en la columna
> «% registrado maliciosamente»: `.bond` 99,0 %, `.vip` 95,1 %, `.cfd` 95,1 %, `.icu`
> 95,0 %, `.sbs` 94,0 %, `.cc` 93,1 %, frente a `.com` 66,5 % y `.cn` 39,3 %. En los gTLD
> baratos **casi no hay víctimas comprometidas: hay infraestructura comprada**. Eso cambia
> la respuesta correcta: bloquear un dominio de `.bond` no arrastra a un tercero inocente;
> bloquear uno de `.cn` o `.com` probablemente sí.

**Y la concentración por registrador**, que es el hallazgo accionable (KJ-1):

| TLD | Tasa de phishing | Registrador dominante | Su cuota del phishing del TLD |
|---|---|---|---|
| `.garden` | 15,7 % | Spaceship, Inc. | **97 %** |
| `.win` | 16,4 % | Dominet (HK) Limited | **87 %** |
| `.mom` | 10,0 % | NameSilo, LLC | 76 % |
| `.mobi` | 8,5 % | Eranet International | 73 % |
| `.help` | 10,6 % | NameSilo, LLC | 67 % |
| `.rest` | 9,8 % | NameCheap, Inc. | 63 % |
| `.xin` | 59,1 % | Dominet (HK) Limited | 55 % |
| `.pro` | 12,0 % | NameCheap, Inc. | 23 % |
| `.icu` | 16,1 % | Gname.com Pte. Ltd. | 23 % |
| `.cfd` | 13,9 % | Web Commerce Communications | 18 % |

## E-3. Tendencia y pronóstico

Serie trimestral completa, dominios de phishing reportados. Etiqueta de periodo = mes
central del trimestre. `.com` se omite por escala: oscila entre 188.756 y 297.244 sin
tendencia clara, lo que por sí solo refuta la idea de que sea «el TLD más atacado» en
términos útiles.

| Periodo | `.top` | `.cn` | `.icu` | `.cfd` | `.vip` | `.garden` |
|---|---|---|---|---|---|---|
| Ago-oct 2025 | 161.534 | 45.684 | 26.830 | 24.128 | 30.988 | no rankeado |
| Nov 25-ene 26 | 57.316 | 52.597 | 27.662 | 22.870 | 22.015 | no rankeado |
| Feb-abr 2026 | 124.452 | 39.798 | 14.196 | 20.767 | 18.248 | 10.332 |
| May-jul 2026 | 59.586 | **147.217** | 46.542 | 44.284 | 31.181 | 15.255 |

<!-- cti:chart title="`.cn` — la irrupción del período" cap="De 39.798 a 147.217 dominios de phishing en un trimestre (×3,7). Fuente: tablas trimestrales de Interisle/CIC." -->

| Periodo | Dominios de phishing |
|---|---|
| `Ago·25` | 45.684 |
| `Nov·25` | 52.597 |
| `Feb·26` | 39.798 |
| `May·26` | 147.217 |

<!-- cti:chart title="`.top` — volatilidad, no tendencia" cap="Cuatro trimestres, dos máximos y dos mínimos: el perfil típico de un TLD bajo presión de mitigación intermitente." -->

| Periodo | Dominios de phishing |
|---|---|
| `Ago·25` | 161.534 |
| `Nov·25` | 57.316 |
| `Feb·26` | 124.452 |
| `May·26` | 59.586 |

Cuatro movimientos merecen lectura estratégica:

**`.cn` se multiplicó por 3,7 en un trimestre** y tomó el segundo puesto mundial. Spamhaus
lo corrobora desde otro ángulo y añade el mecanismo: +84 % de listados, de los cuales
aproximadamente el 40 % son `.com.cn`, y cerca del 12 % de esos contienen la cadena
«whatsapp». No es un TLD barato descontrolado: es una campaña de suplantación de mensajería
a escala nacional.

**`.garden` apareció de la nada.** No estaba rankeado en marzo de 2026; en el trimestre
siguiente era top-5 mundial por tasa, con el 97 % de su abuso en un solo registrador.
Interisle lo describió como el gran pequeño relato de phishing del período. Es el ejemplo
canónico de por qué la vigilancia debe cubrir gTLD de nicho.

**`.cfd` demuestra que la mitigación funciona:** −53 % en listados y del 17,54 % al 7,01 %
de zona listada en un semestre.

**`.help` demuestra que el abuso se desplaza:** entrada nueva en el top-20 de Spamhaus con
el **26,5 %** de su zona listada —el valor más alto del semestre—, impulsado principalmente
por *cold email*.

<!-- cti:cards -->

| Escenario a 6 meses | Desarrollo esperado | Etiqueta |
|---|---|---|
| Rotación continua | Uno o dos gTLD de nicho nuevos entran al top-5 por tasa y uno de los actuales cae por presión del registro, sin que el agregado baje | `Probable · 55–80 %` |
| Consolidación en `.cn` | El pico de `.cn` se sostiene y el centro de gravedad del phishing se desplaza a ccTLD asiáticos, con implicaciones de idioma y horario para el SOC | `Posibilidad real · 45–55 %` |
| Contracción real del agregado | La presión regulatoria —incluida la iniciativa de ICANN sobre «dominios asociados» de enero de 2026— reduce el total de forma sostenida | `Poco probable · 20–35 %` |
| Salto a subdominios gratuitos | El abuso migra masivamente a alojamiento gratuito, donde la métrica por TLD queda ciega y el dominio padre es legítimo | `Posibilidad real · 45–55 %` |

## E-4. Decisiones que este informe pide al nivel estratégico

<!-- cti:table highlight="regional|Chile|marca" -->

| # | Decisión | Fundamento | Plazo |
|---|---|---|---|
| E-a | Aprobar **cuarentena de 30 días para dominios recién registrados** en el conjunto de TLD de §X-1 (aviso al usuario e inspección, no bloqueo duro), con vía de excepción documentada | KJ-1, KJ-2: 74 % de registro malicioso y tasas superiores al 10 % hacen de la edad del dominio la señal más rentable | 30 días |
| E-b | Encargar el inventario de §O-4: volumen de tráfico legítimo propio hacia esos TLD | Sin esa cifra no se puede estimar el coste de E-a y la política no es defendible ante negocio | 45 días |
| E-c | Incorporar a la vigilancia de marca los gTLD de nicho de §O-7, no solo `.com` y `.cl` | KJ-5: el caso `.report` ocurrió íntegramente fuera del radar de los rankings | 60 días |
| E-d | Fijar **revisión trimestral obligatoria** de la lista de TLD, con responsable nombrado | KJ-3: cuatro trimestres de datos demuestran que la lista caduca | Permanente |
| E-e | Rechazar explícitamente cualquier propuesta de bloqueo total por TLD que no venga acompañada del cálculo de falsos positivos de E-b | Los TLD de peor tasa alojan negocio legítimo; el bloqueo total es un riesgo operativo mal entendido como control | Inmediato |
| E-f | **Eje regional:** tratar el parque WordPress `.cl` propio y de proveedores como superficie de distribución de malware, no solo como riesgo de defacement | KJ-7: el `.cl` aparece en los datos como víctima comprometida, y Macfinger se pivoteó desde un sitio chileno | 60 días |

---

# NIVEL OPERACIONAL
### Para: Jefatura de SOC · Respuesta a Incidentes · Threat Hunting · Horizonte: semanas–meses

## O-1. Identificación y equivalencia de métricas

El equivalente aquí de la fusión indebida de alias es la fusión indebida de métricas. Antes
de citar cualquier cifra de abuso de TLD hay que saber cuál se está citando.

| Métrica | Origen | Qué mide realmente | Grado de equivalencia |
|---|---|---|---|
| *Phishing Domains* | Interisle / CIC | Dominios distintos reportados en phishing | Referencia de volumen |
| *Phishing Domain Score* | Interisle / CIC | (dominios de phishing / dominios delegados) × 10.000 | Referencia de tasa — **no comparable con volumen** |
| *Malicious Phishing Domains* | Interisle / CIC | Subconjunto registrado con intención maliciosa | Más estrecho y más accionable |
| *Listados maliciosos/sospechosos* | Spamhaus | Dominios con reputación negativa por cualquier causa: spam, *cold email*, phishing, malware, asociación | **Más amplio.** No equivale a phishing |
| *% de zona listada* | Spamhaus | Listados / tamaño de la zona | Conceptualmente similar a la tasa, distinta base de datos |
| *Malware Domains* | Interisle / CIC | Dominios que sirven malware | **Población distinta.** No mezclar |

> **Nota de tradecraft.** Las cifras de Spamhaus y de Interisle **no son sumables ni
> directamente comparables**: distinta definición, distinta ventana, distintas fuentes de
> alimentación. Coinciden en la dirección de los movimientos —`.cfd` a la baja, `.cn` al
> alza— y esa coincidencia es lo que da confianza alta a KJ-2 y KJ-3. Citar una cifra de
> una y una de otra en la misma frase, como si midieran lo mismo, es el error más común en
> la prensa técnica sobre este tema.

## O-2. Estructura del mercado y dónde está la palanca

| Eje | Valoración | Confianza |
|---|---|---|
| Concentración por registro (TLD) | Alta: 9 gTLD superan el 10 % de zona abusada; 2 más quedan a menos de un punto | Alta |
| Concentración por registrador | Muy alta: hasta 97 % del abuso de un TLD en un registrador | Alta |
| Concentración por alojamiento | Alta en campañas concretas: Macfinger entera en Aeza Group (AS210644, AS216246, sancionado por OFAC el 01-07-2025) y NetCrafters OU (AS203273) | Moderada — una sola campaña medida |
| Modelo de registro masivo | Visible en el *churn*: `.bond` registró 1,13 M de dominios nuevos con una zona total de 1,15 M | Alta |

*Razonamiento:* los TLD con peor tasa comparten tres rasgos —precio de registro bajo,
política de verificación laxa y un registrador que concentra el volumen—. *Contraargumento
que hay que sostener:* la correlación no implica complicidad; un registrador grande y barato
atrae abuso por su modelo de negocio sin participar en él, y los datos que tenemos no
distinguen una cosa de la otra.

## O-3. Modelo de operación del abuso

Tres modelos distintos, con respuestas defensivas distintas:

**Registro masivo desechable.** Comprar cientos o miles de dominios en un gTLD barato,
usarlos días y abandonarlos. La firma es el *churn*: `.bond` con registros nuevos casi
iguales a su zona total. Contramedida: edad del dominio.

**Registro dirigido de bajo volumen.** Comprar decenas de dominios en un gTLD de nicho con
semántica creíble, cada uno copiando el identificador real de un objetivo. Es el caso
`.report`: 317 dominios, 13 registradores distintos, registro continuo durante un mes para
no generar una ráfaga detectable. **Esta es la que las métricas por TLD no ven**, y es la
de mayor impacto por dominio. Contramedida: vigilancia de marca y de identificadores
propios (tenants SaaS incluidos).

**Compromiso de sitio legítimo.** No se registra nada: se inyecta en WordPress ajeno. Es la
población de la tabla de malware (`.com`, `.ru`, `.de`, `.br`, `.cl`). Contramedida:
reputación por dominio e integridad del propio parque web. El bloqueo por TLD es
inservible aquí.

## O-4. Nuestra exposición

> ⬛ **Sección sin evaluar — requiere telemetría interna.** Es la brecha principal de este
> producto (véase §14, G-1). Mientras no se rellene, §E-4 propone política sin coste
> calculado.

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| X-1 | ¿Qué volumen de tráfico saliente legítimo va a los TLD de §X-1? ¿Qué destinos concretos y qué unidad de negocio los usa? | Logs de proxy / DNS, 90 días | SOC + Redes |
| X-2 | ¿Cuántos dominios registrados en los últimos 30 días contienen nuestra marca o nuestras marcas de producto, en cualquier TLD? | Vigilancia de marca / CT logs | Célula CTI |
| X-3 | ¿Cuál es el identificador de nuestros tenants SaaS (Okta, Entra, Workspace) y existe algún dominio que lo replique? Es exactamente el patrón `.report` | Inventario de SaaS + DNS | TI + CTI |
| X-4 | ¿Cuántos sitios WordPress `.cl` propios o de proveedores exponemos, con qué versión y quién los parchea? | Inventario de activos externos | TI / Marketing |
| X-5 | ¿Nuestro gateway de correo puntúa la edad del dominio del remitente? ¿Y el proxy la del destino? | Configuración de SEG y proxy | Ingeniería |
| X-6 | ¿Tenemos registro de consultas DNS con retención suficiente para hacer retrohunt de 90 días? | Plataforma DNS | Redes |

## O-5. Cronología

<!-- cti:timeline -->

| Fecha | Hecho | Traza |
|---|---|---|
| 2025-05-01 | Inicio de la ventana anual de medición de Interisle | Global |
| 2025-08/10 | `.top` marca su máximo del período: 161.534 dominios de phishing en un trimestre | Global |
| 2025-10-21 | Spamhaus publica el semestre abr-sep 2025: C&C de botnet +289 %, malware +206 % | Global |
| 2026-01 | **ICANN gNSO anuncia la iniciativa «DNS Abuse Mitigation: PDP 1 on Associated Domain Checks»**, que obligaría a los registradores a revisar dominios asociados al detectar uno malicioso | Gobernanza |
| 2026-02/04 | **`.garden` entra de la nada al top-5 mundial por tasa de phishing**, con el 97 % de su abuso en un registrador | Global |
| 2026-04-15 | Spamhaus publica oct-25/mar-26: `.cfd` alcanza el **17,54 %** de su zona listada, el peor valor del semestre | Global |
| 2026-06-09 / 17 | Barrido que expone **914 dominios `.cl` con webshells**: el `.cl` aparece como víctima, no como vector | Chile |
| 2026-08-06 | Inicio estimado de la campaña Macfinger: 56 dominios de cargador en nueve terminaciones, rotación casi diaria | LATAM · Chile |
| 2026-08-18 | **Primer registro del clúster de 317 dominios `.report` que copian tenants reales de Okta** | Global |
| 2026-09-16 | Último registro del clúster `.report`: un mes de registro continuo, no una ráfaga | Global |
| 2026-09-17 | Verificación independiente: **33 de 317** dominios `.report` corresponden a tenants Okta activos | Global |
| 2026-09 | **Récord histórico de Spamhaus: 1,15 millones de dominios maliciosos listados en un mes** | Global |
| 2026-10-15 | Spamhaus publica abr-sep 2026: `.help` al **26,5 %** de zona listada; `.cfd` baja al 7,01 % | Global |
| 2026-11-15 | Cierre de datos de este informe | — |

## O-6. Hipótesis alternativas consideradas

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| H1 — El TLD es un predictor fuerte de malicia por sí solo | **Retenida con matiz.** Cierto para `.xin`, `.win`, `.icu`, `.garden`, `.cfd`: con tasas del 10–59 % el prior es alto. Falso para los 200 TLD restantes | `Retenida parcial` |
| H2 — Los rankings reflejan sesgo de observación, no abuso real | **Retenida como limitación.** Es el argumento más fuerte contra todo el informe y no se puede refutar con los datos disponibles. Mitigación: dos proveedores con metodologías distintas coinciden en la dirección de los movimientos | `Retenida · limitación` |
| H3 — El crecimiento de abuso de 2026 es artefacto de medición | **Parcialmente retenida.** Spamhaus declara mejoras de ingesta y listado preventivo de carteras. Rebaja KJ-4 a confianza moderada; no explica el pico de `.cn`, que Interisle ve con otra metodología | `Posibilidad real · 45–55 %` |
| H4 — Bloquear los TLD de peor tasa reduciría materialmente nuestro riesgo | **Poco probable.** KJ-6: las campañas usan 6–9 terminaciones y rotan a diario; el coste de cambiar de TLD es de dólares | `Poco probable · 20–35 %` |
| H5 — El clúster `.report` es obra de ShinyHunters | **Sin confianza.** Ni la fuente original lo afirma —usó «potencial»—, y el patrón es indistinguible de TTP de Scattered Spider. Se consigna para que no se reabra como hecho | `Descartada como hecho` |
| H6 — El abuso se está desplazando a subdominios de alojamiento gratuito | **Retenida, no medida.** Queda fuera del alcance (§3.2) y es una brecha de colección declarada (G-2) | `Retenida · sin medir` |

**Supuesto clave:** que las fuentes de alimentación de Interisle y Spamhaus cubren el
phishing que nos afecta. Si el phishing dirigido a Chile está sistemáticamente
sub-reportado en ellas, la tabla de §E-2 describe el abuso global pero no el nuestro, y
§E-4 estaría optimizando para la amenaza de otro.

**Pre-mortem.** Es mayo de 2027 y este informe resultó equivocado. La causa más probable:
dedicamos el trimestre a afinar listas de TLD mientras el abuso real contra nosotros llegó
por subdominios de alojamiento gratuito y de SaaS legítimo, donde el dominio padre tiene
reputación impecable y ninguna de nuestras reglas nuevas aplica. Segunda causa más
probable: aplicamos la cuarentena de NRD sin el inventario de §O-4, rompimos un flujo de
negocio y la política se revirtió por completo tras la primera queja.

## O-7. Indicadores y señales de alerta

| # | Indicador observable | Qué señalaría | Disciplina | Responsable |
|---|---|---|---|---|
| I-1 | Dominio registrado hace menos de 30 días que contiene nuestra marca, en cualquier TLD | Preparación de campaña contra nosotros | OSINT / CT logs | Célula CTI |
| I-2 | Dominio que replica el identificador de uno de nuestros tenants SaaS (patrón `.report`) | Preparación de vishing de soporte/TI | OSINT / DNS | CTI + TI |
| I-3 | Aparición de un gTLD de nicho nuevo (semántica corporativa: informes, reclamaciones, soporte, facturación) con pico de registros | Nuevo nicho de suplantación antes de que entre en los rankings | OSINT | Célula CTI |
| I-4 | Tráfico saliente propio hacia `.xin`, `.win`, `.garden`, `.help`, `.qpon`, `.study`, `.mom`, `.rest` | Con tasas del 10–59 %, el prior de malicia justifica investigar cada caso | Proxy / DNS | SOC |
| I-5 | Resolución de dominio con patrón de tres palabras separadas por guiones (`velvet-otter-glagceis.life`) | Cargador tipo Macfinger; el patrón sobrevive a la rotación de dominio | DNS | SOC |
| I-6 | Petición a un sitio `.cl` legítimo que devuelve JavaScript inyectado con reCAPTCHA falso | WordPress propio o de proveedor comprometido como distribuidor | Proxy / web | SOC + TI |
| I-7 | Cambio de más de 20 puestos en el top-20 de Spamhaus o Interisle entre trimestres | Desplazamiento del abuso: toca revisar la lista (E-d) | OSINT | Célula CTI |

---

# NIVEL TÁCTICO
### Para: Analistas de SOC · Ingeniería de Detección · Threat Hunting · Horizonte: días–semanas

## T-1. Cadena de abuso del dominio

<!-- cti:stages title="Del registro al impacto: tres etapas y dos oportunidades de detección anticipada" dwell="next" -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 01 · Adquisición | Compra del nombre en un registrador barato | gTLD de bajo coste · registro masivo o dirigido · privacidad de WHOIS · 74 % con intención maliciosa desde el inicio |
| Etapa 02 · Armado | Certificado, DNS, alojamiento y señuelo | Certificado TLS gratuito (visible en CT logs) · alojamiento concentrado (Aeza, NetCrafters) · kit de phishing o cargador · *cloaking* contra rastreadores |
| Etapa 03 · Uso e impacto | Entrega y rotación | Correo, SMS, inyección en sitio legítimo · ClickFix · vishing con señuelo de portal SSO · rotación diaria del dominio y abandono |

**Ventana de detección:** entre el registro y el primer uso pasan **días**, no horas —el
clúster `.report` se registró entre el 18-08 y el 16-09 y seguía sin contenido activo en
varios dominios al 17-09—. Las etapas 01 y 02 dejan rastro público (WHOIS, CT logs, DNS
pasivo) **antes** de que llegue el primer correo.

## T-2. Mapa MITRE ATT&CK

<!-- cti:matrix -->

| Táctica | ID | Técnica | Procedimiento observado |
|---|---|---|---|
| Desarrollo de recursos | T1583.001 | Acquire Infrastructure: Domains | Registro masivo en gTLD baratos; `.bond` con 1,13 M de registros nuevos sobre una zona de 1,15 M |
| Desarrollo de recursos | T1583.001 | Acquire Infrastructure: Domains | Registro dirigido: 317 dominios `.report` en 13 registradores, repartidos en 30 días para evitar una ráfaga |
| Desarrollo de recursos | T1583.004 | Acquire Infrastructure: Server | Concentración de toda la infraestructura de Macfinger en dos ASN (AS210644, AS216246 de Aeza; AS203273 de NetCrafters) |
| Desarrollo de recursos | T1587.003 | Develop Capabilities: Digital Certificates | Certificados TLS gratuitos sobre dominios recién registrados; rastro en CT logs |
| Desarrollo de recursos | T1588.004 | Obtain Capabilities: Digital Certificates | — |
| Desarrollo de recursos | T1584.001 | Compromise Infrastructure: Domains | Población de la tabla de malware: WordPress legítimo en `.com`, `.ru`, `.de`, `.br`, `.cl` |
| Desarrollo de recursos | T1585.003 | Establish Accounts: Cloud Accounts | Alojamiento del señuelo en servicios de páginas gratuitos (Cloudflare Pages en la campaña Phexia) |
| Reconocimiento | T1598 | Phishing for Information | Señuelo de portal SSO que replica el identificador real del tenant |
| Acceso inicial | T1566.002 | Phishing: Spearphishing Link | Enlace a dominio recién registrado en gTLD de nicho |
| Acceso inicial | T1660 | Phishing (móvil) | Smishing con `.top`, `.icu`, `.vip`, `.autos`, `.shop`, `.space` suplantando correo postal y organismos |
| Ejecución | T1204.004 | User Execution: Malicious Copy and Paste | ClickFix con reCAPTCHA falso (Macfinger) |
| Evasión | T1656 | Impersonation | Suplantación del identificador de tenant corporativo y de portales de soporte |
| Mando y control | T1568.002 | Dynamic Resolution: Domain Generation Algorithms | Dominios de patrón pseudoaleatorio en `.ws`, `.life` y similares |
| Mando y control | T1102.001 | Web Service: Dead Drop Resolver | Resolución del C2 mediante contrato inteligente en Polygon (Phexia) |
| Mando y control | T1071.001 | Application Layer Protocol: Web Protocols | Rotación diaria del dominio de cargador manteniendo el identificador de víctima |

## T-3. Dónde atacamos en la Pirámide del Dolor

<!-- cti:pyramid -->

| Nivel | Qué contiene en este informe y qué vale | Valor |
|---|---|---|
| Hashes | No aplica: este producto no analiza binarios. Los hashes de las campañas citadas están en sus fichas de origen | Base · valor trivial |
| IP · Dominios | Anexo A. **Perecedero por diseño:** el adversario rota a diario y abandona en días. Bloquear sí, pero contar con que caduca en horas | Valor bajo |
| Artefactos | Patrón de nombre (tres palabras con guiones), nombre de fichero cuyos hexadecimales son el prefijo del SHA-256, identificador de víctima estable entre rotaciones | Valor medio |
| Herramientas | Registradores y ASN concretos: Dominet (HK), Spaceship, NameSilo, Gname, Eranet; Aeza Group, NetCrafters. **El pivote que dura** | Valor alto |
| TTP | Registro masivo desechable, registro dirigido en gTLD de nicho, suplantación de identificador de tenant, ClickFix. Aquí debe concentrarse el esfuerzo | Cima · valor máximo |

> **Lectura.** Este es el informe donde la pirámide se nota más: la tentación es llevarse
> la lista de dominios del Anexo A y darse por satisfecho, cuando **el TLD es apenas un
> escalón por encima de la IP en durabilidad**. Lo que dura es el par
> registrador + proveedor de alojamiento, y el patrón de nombre.

## T-4. Hipótesis de caza prioritarias

<!-- cti:accordion critical="^(H-1|H-2|H-3)\b" regional="^(H-7|H-8)\b" -->

**H-1 — Resolución a TLD de tasa extrema.** Buscar en logs de DNS y de proxy, ventana de 90
días, toda resolución a `.xin`, `.win`, `.garden`, `.help`, `.qpon`, `.study`, `.mom`,
`.rest`, `.icu`, `.cfd`. Con tasas de abuso del 10 al 59 %, cada acierto merece revisión
individual. Fidelidad esperada alta por la escasez de uso legítimo; falsos positivos
previsibles en herramientas de marketing y acortadores. Esta caza es también el insumo de
§O-4 X-1: su resultado dice si E-a es viable.

**H-2 — Suplantación del identificador de nuestros tenants SaaS.** Enumerar los
identificadores de nuestros tenants (Okta, Entra, Workspace, Zoom, Slack) y buscar su
aparición como dominio registrable en cualquier TLD, con prioridad en gTLD de semántica
corporativa. Es la reproducción exacta del hallazgo `.report`. **Criterio discriminante
aprendido del caso:** que `<id>.okta.com` resuelva no prueba nada —el front-door genérico
responde a cualquier texto inventado—; lo que discrimina es que enrute a una **celda
específica** (`ok1-crtrs.tng.okta.com` … `ok14-crtrs.tng.okta.com`). Con el criterio
ingenuo salían 317 de 317; con el correcto, 33.

**H-3 — Dominios recién registrados en el correo entrante.** Correlacionar el dominio del
remitente y de los enlaces con su fecha de registro. Priorizar menos de 30 días. Dado el
74 % de registro malicioso, el valor predictivo es alto. Requiere enriquecimiento de edad
de dominio en el SEG: si no existe, es la brecha de §T-5.

**H-4 — Patrón de nombre de cargador tipo Macfinger.** Buscar resoluciones a dominios con
estructura de tres palabras en inglés separadas por guiones, siendo la última
pseudoaleatoria (`velvet-otter-glagceis.life`, `hollow-badger-moasfraum.life`), en `.life`,
`.live`, `.xyz`, `.icu`, `.space`, `.site`, `.lol`, `.digital`. El patrón sobrevive a la
rotación diaria del dominio concreto.

**H-5 — Pivote por ASN en lugar de por dominio.** Buscar tráfico saliente a AS210644 y
AS216246 (Aeza Group, sancionado por OFAC el 01-07-2025) y AS203273 (NetCrafters OU). Toda
la infraestructura de Macfinger cabía en esos tres. El ASN dura semanas; el dominio, horas.

**H-6 — Certificados nuevos con nuestra marca.** Monitorizar CT logs por emisión de
certificados que contengan nuestras marcas en el SAN. Captura la etapa 02 de §T-1, antes
del primer correo.

**H-7 — Eje regional: nuestro parque `.cl` como distribuidor.** Revisar los sitios
WordPress `.cl` propios y de proveedores buscando JavaScript inyectado que presente un
reCAPTCHA falso. Advertencia operativa del caso Macfinger: el kit **evade rastreadores de
IA y SEO** (GPTBot, ClaudeBot, CCBot, AhrefsBot, SemrushBot), de modo que **no encontrar
nada en Google no prueba que el sitio esté limpio**; hay que pedir la página con un
`User-Agent` de navegador real.

**H-8 — Eje regional: smishing de marcas chilenas.** Buscar en registros de DNS y proxy
móvil resoluciones a dominios que combinen nombres de servicios chilenos (correo postal,
organismos, banca) con `.top`, `.icu`, `.vip`, `.autos`, `.shop`, `.space`, y con
acortadores (`cutt.ly`, `is.gd`) como primer salto.

## T-5. Brechas de visibilidad que hay que cerrar primero

| Brecha | Por qué importa aquí |
|---|---|
| Sin enriquecimiento de edad de dominio en el SEG | H-3 queda ciega y, con ella, la señal de mayor valor predictivo del informe (74 % de registro malicioso) |
| Sin retención de logs DNS a 90 días | H-1, H-4 y H-5 no se pueden ejecutar en modo retrohunt |
| Sin inventario de identificadores de tenants SaaS | H-2 no se puede ni formular; es el patrón exacto del caso `.report` |
| Sin vigilancia de CT logs | H-6 inexistente; se pierde la única señal previa al primer correo |
| Sin inventario de sitios web externos propios y de proveedores | H-7 no tiene alcance definido |
| Sin resolución de ASN en los logs de proxy | H-5 obliga a resolución manual, lo que en la práctica significa que no se hace |

---

# NIVEL TÉCNICO
### Para: Ingeniería de detección · Automatización · TIP/SIEM · Vida útil: un trimestre (revisión obligatoria, E-d)

## X-1. Conjuntos de TLD para política de puntuación

Tres niveles, con la acción que corresponde a cada uno. **Ningún nivel implica bloqueo
total:** todos alojan negocio legítimo.

| Nivel | TLD | Criterio | Acción recomendada |
|---|---|---|---|
| **A — Prior extremo** | `.xin` `.win` `.icu` `.garden` `.cfd` `.pro` `.help` `.mom` `.rest` `.qpon` `.study` | Zona reportada en phishing ≥ 9,8 % en el año (Interisle may-25/abr-26) o zona listada ≥ 12 % en el semestre (Spamhaus abr-sep 26). Nueve superan el 10 %; `.mom` y `.rest` quedan a menos de un punto y se incluyen por prudencia | Puntuación máxima; cuarentena de NRD; investigación individual de cada acierto; alerta al SOC |
| **B — Prior alto** | `.top` `.vip` `.sbs` `.bond` `.cyou` `.cc` `.mobi` `.live` `.ink` `.best` `.lat` `.life` `.homes` `.click` `.wang` | Entre el 3 % y el 10 % de zona abusada, o presencia sostenida en los cuatro trimestres | Puntuación alta; cuarentena de NRD; revisión por muestreo |
| **C — Volumen, prior bajo** | `.com` `.cn` `.net` `.org` `.info` `.xyz` `.shop` `.online` `.site` `.store` | Mucho abuso absoluto pero menos del 2 % de zona abusada | **No puntuar por TLD.** Reputación por dominio y edad del dominio. Puntuar aquí genera falsos positivos masivos |
| **D — Nicho a vigilar** | `.report` `.claims` `.beer` `.lol` `.casino` `.surf` `.autos` `.space` `.digital` | Sin señal en los agregados, pero con clústeres dirigidos observados en 2026 | No puntuar. **Vigilancia de marca** e inclusión en I-3 |

> ⚠ **Caducidad de esta tabla.** Se construyó con datos que terminan en sep-2026. Cuatro
> trimestres de evidencia (KJ-3) indican que estará desalineada en marzo de 2027. La tabla
> sin la revisión trimestral de E-d es un pasivo, no un control.

## X-2. Artefactos duraderos — lo que no cambia al rotar el dominio

<!-- cti:cards -->

| Categoría | Artefactos | Etiqueta |
|---|---|---|
| Registradores concentradores | Dominet (HK) Limited · Spaceship, Inc. · NameSilo, LLC · Gname.com Pte. Ltd. · Eranet International · Web Commerce Communications | `registro` |
| ASN de alojamiento | AS210644 y AS216246 (Aeza Group, OFAC 01-07-2025) · AS203273 (NetCrafters OU) | `alojamiento` |
| Patrón de nombre | Tres palabras en inglés con guiones, última pseudoaleatoria: `velvet-otter-glagceis` · `hollow-badger-moasfraum` | `nomenclatura` |
| Patrón de nombre dirigido | `<identificador-real-de-tenant>.<gTLD de nicho>` — sin guiones, sin typosquatting, idéntico al legítimo | `suplantación` |
| Patrón de fichero | `ext-b.4f9db6afd06a.js`: los 12 hexadecimales son el prefijo del SHA-256 del propio fichero | `cargador` |
| Celdas de enrutamiento Okta | `ok1-crtrs.tng.okta.com` … `ok14-crtrs.tng.okta.com` — distinguen tenant real de inventado | `verificación` |
| Evasión de rastreadores | GPTBot · ClaudeBot · CCBot · AhrefsBot · SemrushBot | `cloaking` |

## X-3. Lógica de detección prioritaria

<!-- cti:detections -->

**D-1 · CRÍTICO — Suplantación del identificador de un tenant SaaS propio**

```
dns.question.name MATCHES "^(<id_tenant_1>|<id_tenant_2>|<id_tenant_n>)\.[a-z]{2,}$"
AND NOT dns.question.name ENDSWITH (".okta.com", ".<dominio_corporativo>")
```

→ Alerta inmediata al SOC y a TI. Es el patrón `.report`: señuelo para vishing de soporte.
Verificar contra celda Okta antes de concluir, y bloquear sin esperar confirmación de
contenido activo: en el clúster medido, la mayoría de los dominios no servía nada el día
del hallazgo. **Contención automática justificada.**

**D-2 · CRÍTICO — Dominio recién registrado en TLD de nivel A con interacción de credenciales**

```
proxy.destination.tld IN (xin, win, garden, help, qpon, study, mom, rest, icu, cfd)
AND domain.age_days < 30
AND (http.method == "POST" OR url.path MATCHES "(login|signin|verify|portal|account)")
```

→ Bloqueo y alerta. La combinación de prior extremo, dominio nuevo y envío de formulario no
tiene uso legítimo plausible. **Contención automática justificada.**

**D-3 · ALTO — Patrón de cargador de tres palabras**

```
dns.question.name MATCHES "^[a-z]{4,10}-[a-z]{4,10}-[a-z]{6,14}\.(life|live|xyz|icu|space|site|lol|digital)$"
```

→ Aislar el endpoint y buscar ejecución de Terminal o `curl`/`osascript` en la ventana
siguiente. Patrón Macfinger; sobrevive a la rotación diaria del dominio.

**D-4 · ALTO — ClickFix: portapapeles a intérprete**

```
(macOS) process.name IN ("osascript","curl","bash") AND parent.name == "Terminal"
AND cmdline CONTAINS_ANY ("curl", "| sh", "| bash", "history -c", "clear")
```

→ Aislar. Es la ejecución del comando que el kit copió al portapapeles. Detecta la campaña
**independientemente del dominio**, que es lo que la hace duradera.

**D-5 · MEDIO — Tráfico a ASN de alojamiento concentrador**

```
network.destination.asn IN (210644, 216246, 203273)
```

→ Investigar. Bajo volumen esperado de uso legítimo; Aeza está sancionado por OFAC, lo que
añade una dimensión de cumplimiento a la de seguridad.

**D-6 · MEDIO — Certificado nuevo con nuestra marca**

```
ct_log.san CONTAINS_ANY ("<marca>", "<marca-producto>", "<marca>-soporte")
AND ct_log.issued_days_ago < 7
AND NOT ct_log.issuer IN (<nuestras_CA_autorizadas>)
```

→ Apertura de caso de vigilancia de marca. Captura la etapa 02 antes del primer correo.

> ⚠ **Regla de operación.** D-1 y D-2 deben ejecutar contención automática sin escalado
> humano. Fundamento: en el clúster `.report` el intervalo entre el registro y la
> disponibilidad de un formulario de login activo fue de días, y los dominios se
> abandonaron en semanas; una cola de triaje humano de 24 horas consume la ventana útil
> completa. D-3 a D-6 son de investigación, no de contención.

## X-4. Consultas de caza

```kql
// H-1 — Resolución a TLD de nivel A, 90 días. Microsoft Defender / Sentinel.
let tld_nivel_a = dynamic(["xin","win","garden","help","qpon","study","mom","rest","icu","cfd"]);
DeviceNetworkEvents
| where Timestamp > ago(90d)
| extend host = tolower(tostring(parse_url(RemoteUrl).Host))
| extend tld = tostring(split(host, ".")[-1])
| where tld in (tld_nivel_a)
| summarize Hits = count(), Dispositivos = dcount(DeviceName),
            Primero = min(Timestamp), Ultimo = max(Timestamp) by host, tld
| order by Hits desc
```

```kql
// H-2 — Suplantación del identificador de tenant propio. Rellenar la lista de ids.
let ids_tenant = dynamic(["<id1>","<id2>","<id3>"]);
DeviceNetworkEvents
| where Timestamp > ago(30d)
| extend host = tolower(tostring(parse_url(RemoteUrl).Host))
| extend etiqueta = tostring(split(host, ".")[0])
| where etiqueta in (ids_tenant)
| where not(host endswith ".okta.com")
| project Timestamp, DeviceName, AccountName, host, RemoteUrl, InitiatingProcessFileName
```

```kql
// H-4 — Patrón de cargador de tres palabras (Macfinger).
DeviceNetworkEvents
| where Timestamp > ago(60d)
| extend host = tolower(tostring(parse_url(RemoteUrl).Host))
| where host matches regex @"^[a-z]{4,10}-[a-z]{4,10}-[a-z]{6,14}\.(life|live|xyz|icu|space|site|lol|digital)$"
| summarize Eventos = count(), Primero = min(Timestamp) by DeviceName, host
| order by Primero asc
```

```yaml
# Sigma — Dominio recién registrado en TLD de prior extremo con envío de formulario
# Autor: Célula CTI · Fecha: 2026-11-15 · ATT&CK: T1566.002, T1598
# Nivel: high
# Requiere: enriquecimiento de edad de dominio en el proxy (véase T-5)
# Falsos positivos conocidos: campañas de marketing con dominio efímero propio;
#   herramientas SaaS recién adquiridas por el negocio; acortadores de enlaces.
title: Envio de formulario a dominio nuevo en TLD de alto abuso
logsource:
  category: proxy
detection:
  seleccion_tld:
    dest_tld:
      - 'xin'
      - 'win'
      - 'garden'
      - 'help'
      - 'qpon'
      - 'study'
      - 'mom'
      - 'rest'
      - 'icu'
      - 'cfd'
  seleccion_edad:
    domain_age_days|lt: 30
  seleccion_credencial:
    - http_method: 'POST'
    - url_path|contains:
        - 'login'
        - 'signin'
        - 'verify'
        - 'portal'
        - 'account'
  condition: seleccion_tld and seleccion_edad and seleccion_credencial
fields:
  - src_ip
  - user
  - dest_host
  - url_path
falsepositives:
  - Marketing con dominios efimeros propios
  - Altas de SaaS no inventariadas
level: high
```

```yaml
# Sigma — ClickFix en macOS: portapapeles a interprete desde Terminal
# Autor: Célula CTI · Fecha: 2026-11-15 · ATT&CK: T1204.004
# Nivel: critical
# Falsos positivos conocidos: desarrolladores e ingenieria de plataforma, que
#   ejecutan instaladores por una linea de forma legitima y frecuente. Afinar
#   excluyendo grupos tecnicos antes de habilitar la contencion.
title: Ejecucion de comando pegado en Terminal con descarga y borrado de historial
logsource:
  category: process_creation
  product: macos
detection:
  seleccion_proceso:
    ParentImage|endswith: '/Terminal'
    Image|endswith:
      - '/osascript'
      - '/curl'
      - '/bash'
      - '/sh'
  seleccion_cadena:
    CommandLine|contains:
      - '| sh'
      - '| bash'
      - 'history -c'
      - 'curl -s'
  condition: seleccion_proceso and seleccion_cadena
fields:
  - ComputerName
  - User
  - CommandLine
  - ParentCommandLine
falsepositives:
  - Personal tecnico ejecutando instaladores de una linea
level: critical
```

## X-5. Mitigaciones de configuración con efecto directo

| Control | Corta |
|---|---|
| Cuarentena de dominios con menos de 30 días en proxy y SEG | La etapa 03 completa de la mayoría de campañas de registro masivo: el 74 % de los dominios de phishing nace malicioso y se usa en días |
| Enriquecimiento de edad de dominio en el gateway de correo | Habilita D-2 y H-3; sin esto, la señal de mayor valor del informe no es computable |
| Bloqueo de ejecución de comandos pegados: política de endpoint que impida `osascript`/`curl` con hijo de Terminal para usuarios no técnicos | La etapa de ejecución de ClickFix, con independencia del dominio y del TLD |
| FIDO2 / claves de paso resistentes a phishing en el SSO corporativo | Vuelve inútil el señuelo de portal SSO del patrón `.report`, que es el de mayor impacto por dominio |
| Vigilancia de CT logs sobre nuestras marcas | La etapa 02, antes del primer contacto con el usuario |
| Endurecimiento y parcheo del parque WordPress propio y de proveedores | Nos saca de la población de la tabla de malware: deja de usarse nuestro dominio legítimo como distribuidor |
| Resolución de ASN en los logs de proxy | Habilita H-5 y D-5, el pivote más duradero de todos |

---

## 14. Brechas de inteligencia y nuevos requisitos de colección

| # | Brecha | Impacto en el juicio | Requisito propuesto | Prioridad |
|---|---|---|---|---|
| G-1 | Sin telemetría propia de DNS y proxy | §O-4 vacía; el coste de E-a no se puede estimar y toda la política queda sin validar | Extracción de 90 días de logs de DNS y proxy, agregados por TLD de destino | **Crítica** |
| G-2 | Sin medición del abuso en subdominios de alojamiento gratuito | H6 retenida sin medir; si el abuso migró allí, este informe optimiza para el lugar equivocado | Incorporar una fuente que mida abuso a nivel de subdominio, no de TLD | Alta |
| G-3 | Sin datos DAAR de ICANN de 2026 por TLD | Solo dos proveedores sostienen las cifras; H2 (sesgo de observación) no se puede acotar | Solicitar o localizar los informes DAAR mensuales de 2026 | Media |
| G-4 | Ventana ciega desde oct-2026 | Las seis semanas más recientes no están cubiertas por ninguna fuente | Reconsultar Interisle y Spamhaus en el próximo trimestre (E-d) | Media |
| G-5 | Sin visibilidad de phishing dirigido específicamente a Chile en las fuentes usadas | El supuesto clave de §O-6 queda sin verificar; §E-2 puede describir una amenaza que no es la nuestra | Contraste con CSIRT de Gobierno y con la comunidad CTI regional | Alta |
| G-6 | Sin verificación independiente de la atribución del clúster `.report` | KJ-5 se queda en confianza moderada | Seguimiento de reportes de proveedor sobre ShinyHunters y Scattered Spider | Baja |

---

# ANEXOS

## Anexo A — Indicadores de compromiso

> ⚠ **Leer antes de usar.** Estos indicadores son el nivel más perecedero del producto y en
> este informe más que en ninguno: el adversario rota dominios a diario. Se entregan **con
> contexto, confianza y acción permitida**. La lista completa de los 317 dominios `.report`
> y de los 56 cargadores de Macfinger está en el repositorio de origen (Anexo B);
> aquí va la muestra verificada y de mayor valor. Valores *defanged*.

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Acción permitida |
|---|---|---|---|---|
| domain | `gen[.]report` | Señuelo Okta. **El único de los 33 con contenido activo:** HTTP 200 con redirección a `/login/?next=/`. NameCheap, registrado 2026-09-06 | Alta | Bloqueo |
| domain | `support[.]report` | Imita el portal de soporte **oficial** de Okta, no un cliente. Porkbun, 2026-09-08, HTTP 200 | Alta | Bloqueo |
| domain | `hcahealthcare[.]report` | Suplanta tenant de HCA Healthcare (salud). Dynadot, 2026-09-10 | Media | Bloqueo |
| domain | `lyrahealth[.]report` | Suplanta tenant de Lyra Health (salud mental). Dynadot, 2026-09-14 | Media | Bloqueo |
| domain | `unum[.]report` | Suplanta tenant de Unum (seguros). Dynadot, 2026-09-07 | Media | Bloqueo |
| domain | `expeditors[.]report` | Suplanta tenant de Expeditors International (logística). Dynadot, 2026-09-12 | Media | Bloqueo |
| domain | `discounttire-retail[.]report` | Suplanta tenant de Discount Tire. Dynadot, 2026-09-05 | Media | Bloqueo |
| domain | `offerup[.]report` | Suplanta tenant de OfferUp. Global Domain Group, 2026-08-20 (el más antiguo) | Media | Bloqueo |
| domain | `rbx[.]report` | Posible suplantación de Roblox. Dynadot, 2026-09-10 | Media | Bloqueo |
| domain | `monday[.]report` | Posible suplantación de monday.com. Porkbun, 2026-08-23, HTTP 200 | Media | Bloqueo |
| domain | `ahrefs[.]report` | Suplanta tenant de Ahrefs. Name.com, 2026-08-31 | Media | Bloqueo |
| domain | `erc[.]report` | Señuelo Okta, celda ok10. GoDaddy, 2026-09-16 (el más reciente del clúster) | Media | Bloqueo |
| domain | `velvet-otter-glagceis[.]life` | Cargador Macfinger (ClickFix macOS). Patrón de tres palabras | Media | Bloqueo |
| domain | `hollow-badger-moasfraum[.]life` | Cargador Macfinger activo desde el 24-09-2026 | Media | Bloqueo |
| domain | `beroniw[.]com` | Redirector con *cloaking* de un segundo inyector independiente de Macfinger | Media | Bloqueo |
| url | `hxxps://cl-correoss[.]top/` | Smishing suplantando Correos de Chile | Media | Bloqueo |
| url | `hxxps://correoscli[.]icu/address` | Smishing Correos de Chile | Media | Bloqueo |
| url | `hxxps://clpost-zip[.]top/` | Smishing Correos de Chile | Media | Bloqueo |
| url | `hxxps://correos[.]autos/` | Smishing Correos de Chile | Media | Bloqueo |
| url | `hxxps://postag[.]vip/index` | Smishing Correos de Chile | Media | Bloqueo |
| url | `hxxps://cl-correos[.]shop` | Smishing Correos de Chile | Media | Bloqueo |
| url | `hxxps://correos-cl[.]space/` | Smishing Correos de Chile | Media | Bloqueo |
| asn | `AS210644` · `AS216246` | Aeza Group. Toda la infraestructura de Macfinger. **Sancionado por OFAC el 01-07-2025** | Alta | Investigar · bloqueo con validación de negocio |
| asn | `AS203273` | NetCrafters OU. Resto de la infraestructura de Macfinger | Media | Investigar |
| filename | `ext-b.4f9db6afd06a.js` | Cargador Macfinger. Los 12 hexadecimales son el prefijo de su SHA-256, verificado en 13 compilaciones | Alta | Detección |
| pattern | `ok1-crtrs.tng.okta.com` … `ok14-crtrs.tng.okta.com` | **No es malicioso:** es el criterio de verificación que distingue un tenant Okta real de uno inventado | Alta | Solo verificación |

*Nota de higiene:* los acortadores presentes en la campaña de smishing (`cutt.ly`, `is.gd`,
`is.id`) son **infraestructura compartida legítima**: no bloquear el dominio del acortador,
sino resolver y bloquear el destino. Los dominios `.cl` del barrido de webshells son
**víctimas**: no deben publicarse como IoC ni bloquearse; corresponde notificación, y por
eso no figuran en este anexo.

## Anexo B — Fuentes y valoración

| Fuente | Disciplina | Fiabilidad | Credibilidad | Notas de sesgo |
|---|---|---|---|---|
| Interisle / Cybercrime Information Center — CSV anual de 233 TLD (may-25/abr-26) | OSINT · medición primaria | A | 1 | Mide lo que sus fuentes de alimentación reportan. Rankings de §E-2 calculados por nosotros desde el dato crudo |
| Interisle / CIC — cuatro tablas trimestrales de phishing (ago-25 → jul-26) | OSINT · medición primaria | A | 1 | Umbral de elegibilidad: 30.000 dominios y 25 de phishing; excluye TLD pequeños |
| Interisle / CIC — tres tablas trimestrales de malware (ene-mar, abr-jun, jul-sep 2026) | OSINT · medición primaria | A | 2 | Agrega cuatro fuentes de terceros (Malware Patrol, MalwareURL, Spamhaus, URLhaus) |
| Spamhaus — Domain Reputation Update abr-sep 2026 (PDF, publicado 15-10-2026) | OSINT · medición primaria | A | 2 | Declara mejoras de ingesta y listado preventivo de carteras: parte del alza es de medición |
| Spamhaus — Domain Reputation Update oct-25/mar-26 (PDF, publicado 15-04-2026) | OSINT · medición primaria | A | 2 | Ídem |
| Interisle — serie «Phishing Landscape 2026» (Substack) | OSINT · análisis de proveedor | B | 2 | Tablas publicadas como imágenes: no citables como dato; se usó solo el texto interpretativo |
| IANA — `tlds-alpha-by-domain.txt`, versión 2026111500 | Autoritativa | A | 1 | Ninguno. Usada para validar TLD y descartar falsos positivos |
| `intellroom/IoC` (GitHub, medido por nosotros) | OSINT · repositorio de equipo | C | 3 | Tres sesgos declarados en §3.3. **No es muestra representativa.** Valioso para patrones, no para prevalencia |
| Macfinger: ficha del repositorio, derivada de SANS ISC 33360 (Brad Duncan, 22-09-2026) | OSINT técnico | B | 2 | Fuente primaria de proveedor, ampliada por el repositorio con verificación propia declarada |
| Clúster `.report`: ficha del repositorio, derivada de X/@0x534c (17-09-2026) | OSINT · fuente única | C | 4 | Investigador independiente; el propio autor dice «potencial». La verificación DNS de las 33 coincidencias sí es reproducible |

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

> Usar siempre el término **y** el porcentaje. No usar «podría» ni «es posible» como juicio:
> son afirmaciones no falsables.

## Anexo D — Marcos de referencia empleados

`MITRE ATT&CK v18` (énfasis en Resource Development) · `Pirámide del Dolor` · `ICD 203` ·
`ACH y pre-mortem` · `TLP 2.0` · `PAP` · `Admiralty Code` · `Sigma` ·
`Umbrales de abuso de zona de Spamhaus (5 % / 10 %)` ·
`Phishing Domain Score de Interisle`

## Anexo E — Paquete legible por máquina

- Bundle STIX 2.1: pendiente de generar. Objetos previstos: `domain-name` (Anexo A),
  `autonomous-system` (AS210644, AS216246, AS203273), `indicator` con patrones de D-1 a D-6.
- Evento MISP: pendiente. Taxonomías: `tlp`, `admiralty-scale`, `estimative-language`, `PAP`.
- Reglas: las dos reglas Sigma de §X-4 están listas para comitear al repositorio de
  detección; requieren el enriquecimiento de edad de dominio (G-1) para la primera.
- Datos de respaldo: CSV anual de 233 TLD, cuatro tablas trimestrales de phishing, tres de
  malware, dos PDF de Spamhaus extraídos a texto y los scripts de medición del repositorio.

## Anexo F — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-11-15 | Emisión inicial | Célula CTI |

## Anexo G — Realimentación del consumidor

| Pregunta | Respuesta |
|---|---|
| ¿Respondió a su requisito? | |
| ¿Qué decisión tomó o cambió con este informe? | |
| ¿Se aprobó la cuarentena de NRD de E-a? ¿Con qué excepciones? | |
| ¿Qué faltó? | |
| ¿Llegó a tiempo? | |

> Sin este anexo devuelto, el ciclo de inteligencia queda abierto y el próximo producto no
> mejora. En este caso en concreto: **sin el dato de §O-4 que se pide en E-b, la versión 1.1
> no podrá pasar de política propuesta a política evaluada.**
