---
tlp: "TLP:CLEAR"
pap: "PAP:AMBER"
id: "CTI-2026-041"
version: "1.0"
tipo: "Perfil de operación de extorsión con borrado + estudio de caso nacional + método para leer dos relatos compatibles del mismo incidente cuando uno lo publica el extorsionador y el otro la víctima"
foco_regional: "**El requisito se corrobora, y es el único informe de este lote cuya afirmación regional se confirma con una víctima nombrada.** Anubis publicó a **Empresas Copec S.A.**, compañía energética chilena, en su sitio de fugas en **enero de 2026**, afirmando 6 TB exfiltrados. Y la región ya estaba en su victimología antes: el análisis de Trend Micro de junio de 2025 nombra a **Perú** entre los cuatro países con víctima. **Dos países, dos sectores, dos fuentes distintas** — y un caso con comunicado de la víctima y entrevista del atacante, que es material de estudio poco frecuente"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "Anubis (RaaS) · desarrollado por el grupo que Symantec designa **Hawkmoth** · **reconversión de Sphinx**, con la carga prácticamente sin cambios y sólo la marca actualizada — **y NO es el troyano bancario Anubis para Android, NO es la puerta trasera Anubis en Python de Savage Ladybug, y NO es la herramienta libre homónima de protección contra rastreadores web**"
fecha: "2026-11-19"
caduca: "2027-02-19"
autor: "Célula CTI"
distribucion: "Elaborado íntegramente con fuentes abiertas TLP:CLEAR. Se leyeron en original: el análisis de Trend Micro del 2025-06-13 sobre el cifrador y su modo de borrado, con la tabla completa de parámetros; el análisis de Symantec del 2026-11-05 sobre el ataque de octubre de 2026, con la puerta trasera Lindnor, las trece herramientas de desactivación de seguridad y su lista íntegra de indicadores; y la cobertura chilena del caso Copec, que reproduce **el comunicado oficial de la compañía** y **la entrevista que el propio grupo concedió a un medio especializado**. Difusión libre, conservando la atribución de las fuentes y las salvedades metodológicas de §3. Se mantiene PAP:AMBER: el Anexo A contiene herramientas legítimas y controladores firmados que **no deben bloquearse por su hash** — leer A.6 antes de cargar nada. **Y una advertencia de contenido: este informe describe la exposición pública de datos personales de personas identificables; ningún dato personal se reproduce, y la decisión se consigna en A.7.**"
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-041

## El requisito se corrobora: Anubis publicó a una energética chilena en enero de 2026. **Y el caso deja algo más valioso que la confirmación — dos relatos del mismo incidente que parecen contradecirse y son compatibles**

### Anubis afirmó haber exfiltrado **6 TB** de **Empresas Copec S.A.** y publicó el listado completo de ficheros en un segundo servicio oculto **con buscador**. Copec declaró públicamente «un acceso no autorizado a un sistema de almacenamiento de información de uso interno», que los sistemas de datos de clientes **no** se vieron comprometidos y que **la operación no se vio afectada**. Y el grupo, en una entrevista, dijo que **la defensa de Copec sí consiguió mitigar el cifrado** pero no la exfiltración, que llevó «casi una semana» a baja velocidad por puertas traseras

#### **Las tres afirmaciones pueden ser ciertas a la vez, y ése es el hallazgo metodológico de este informe.** La víctima habla de disponibilidad y de datos de clientes; el atacante habla de confidencialidad de datos internos. **No responden a la misma pregunta**, y leer una como refutación de la otra es el error que el `Anexo D` existe para evitar — en un expediente donde **la única fuente de la mayor parte de los hechos es el propio extorsionador**

##### Lo que hace a este actor distinto no es el cifrado: es que **puede borrar**. El parámetro `/WIPEMODE` **vacía el contenido de los ficheros** y los deja listados a 0 KB, sin recuperación posible. Eso rompe la lógica económica de la extorsión —pagar deja de garantizar nada— y conviene verlo junto con otro dato: **en los dos ataques de este grupo documentados con detalle, el cifrado fue bloqueado y la extorsión siguió adelante sobre los datos ya robados**

###### Y este informe tiene que desambiguar cuatro cosas llamadas «Anubis», igual que `CTI-2026-035` hizo con «Medusa»: **esta operación de extorsión, un troyano bancario para Android, una puerta trasera en Python de otro actor, y una herramienta libre de protección contra rastreadores web**. La última aparece en las búsquedas y no tiene nada que ver

> **Regla de oro del producto:** todo párrafo debe responder a un requisito de
> inteligencia (PIR) y habilitar una decisión. Si un párrafo no cambia lo que
> alguien va a hacer, va al anexo o se borra.

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-041` |
| Versión / fecha | `1.0` — 2026-11-19 (emisión inicial) |
| Tipo de producto | Perfil de **operación de extorsión con capacidad de borrado**, más **estudio de caso nacional** sobre el incidente de Copec, más **método para leer dos relatos compatibles del mismo incidente** cuando uno lo publica el extorsionador y el otro la víctima, más desambiguación de cuatro objetos homónimos |
| Niveles cubiertos | Estratégico · Operacional · Táctico · Técnico |
| Foco regional | **Es el único informe de este lote cuya afirmación regional se confirma con una víctima nombrada.** (1) **Chile**: Anubis publicó a **Empresas Copec S.A.** en su sitio de fugas en **enero de 2026**, con comunicado oficial de la compañía y entrevista del atacante — material de estudio poco frecuente. (2) **Perú** figura entre los cuatro países con víctima del análisis de Trend Micro de **junio de 2025**, cuando el sitio de fugas sólo tenía siete entradas. (3) Y el contexto: un recuento de terceros sitúa **trece organizaciones chilenas atacadas por extorsión en el primer trimestre de 2026** |
| Marcado de difusión | `TLP:CLEAR` · `PAP:AMBER` |
| Clasificación interna | Sin clasificar. Material íntegramente de publicación abierta |
| Requisitos atendidos | `PIR-01`, `PIR-02`, `PIR-03`, `PIR-06`, `PIR-08`, `PIR-09`, `RFI-2026-11-G` |
| Solicitante / consumidor primario | Jefatura de SOC, Respuesta a Incidentes e Ingeniería de Detección. **Y tres destinatarios que este expediente obliga a añadir**: **Comunicación y Legal**, porque el caso Copec es sobre todo una lección de cómo se redacta un comunicado y de qué pregunta responde; **Recursos Humanos**, porque lo publicado fueron expedientes de personal con documentos de identidad y certificados de nacimiento; y **quien administre el acceso remoto**, porque el vector que el propio atacante declara es la **red privada virtual corporativa** |
| Ventana de observación | **2024-12 → 2026-11-19.** Diciembre de 2024, aparición como reconversión de Sphinx; enero de 2026, el caso chileno; noviembre de 2026, el análisis más reciente |
| Base de colección | Nueve fuentes externas, **dos primarias técnicas leídas en original** —Trend Micro y Symantec—, más la cobertura chilena que reproduce **el comunicado de la víctima** y **la entrevista del atacante**. Sin telemetría propia |
| Autor (analista) | Célula CTI |
| Revisión por pares | Pendiente |
| Aprobación | Pendiente |
| Caducidad / revisión | 2027-02-19 (92 días). **Revisión anticipada obligatoria si:** Copec o la autoridad chilena publican un informe con alcance verificado del incidente (cerraría la cuestión central del `Anexo D`); se documenta un uso real de `/WIPEMODE` en una víctima (hoy no hay ninguno documentado, y es el disparador `I-1`); aparece otra víctima latinoamericana; se publica la vía de acceso inicial del caso chileno por una fuente que no sea el atacante; o se detiene a alguien del grupo |
| Productos relacionados | **`CTI-2026-040` (BlackSuit → Chaos) — es el informe hermano y comparten tres cosas:** la reconversión de marca con el código casi intacto, la extorsión como servicio con varios programas de afiliados, y un artefacto de idioma en los parámetros del cifrador. `O-2.3` los compara · **`CTI-2026-039` (APT41)**: su `Anexo D` da el procedimiento de triaje cuando un cifrado puede ser la cara visible de otra cosa, **y aquí se aplica al revés**: cuando el cifrado falla y la extorsión sigue · **`CTI-2026-035` (Medusa)**: el precedente de desambiguación de cuatro objetos homónimos, y el molde de `O-1` · **`CTI-2026-029` (Sandworm)**: el único otro informe de esta cartera con capacidad destructiva, y la comparación de `E-2` es instructiva porque la intención es opuesta · `CTI-2026-014`, `015`, `016`, `024`: el resto de la familia de extorsión, agrupada en el nodo de extorsión del mapa |
| Paquete legible por máquina | Las tablas `cti:ioc` del Anexo A alimentan `ioc_index.csv`. **Advertencia de higiene:** los **cinco controladores firmados pero vulnerables** y las herramientas legítimas de `A.6` —`AnyDesk`, `Megasync`, `WinSCP`, `Filezilla`, `S3browser`— se consignan con tipo `herramienta` para que **no entren en los agregados planos**: son software legítimo, y en el caso de los controladores, **firmados**. Y **ningún dato personal de las personas expuestas en el caso chileno se reproduce**: la decisión se consigna en `A.7` |

> ⚠ **Cinco limitaciones, y la segunda es el objeto del `Anexo D`.** (1) **Sin
> telemetría propia.** (2) **En el caso chileno, la práctica totalidad de los
> hechos técnicos proviene del propio atacante**: el volumen de 6 TB, la vía
> de acceso por red privada virtual, la duración de la exfiltración y la cifra
> del rescate son **afirmaciones del extorsionador**, publicadas en su sitio
> de fugas o dichas en una entrevista que él concedió. La víctima publicó un
> comunicado que no las confirma ni las niega porque **responde a otra
> pregunta**. No hay informe independiente. (3) **No hay ningún uso
> documentado de `/WIPEMODE` contra una víctima real**: la capacidad está
> analizada en laboratorio y es verificable, pero su empleo es, hasta donde
> alcanza esta colección, **hipotético**. (4) **Las cifras de víctimas de
> terceros son inconsistentes** y sólo se usa la de Symantec, que es de
> primera mano. (5) **Las fechas del caso chileno difieren entre fuentes**
> —una lo sitúa el 9 de enero y otra el 14—, y se consigna el rango.

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** **La afirmación del requisito se corrobora: Anubis publicó a una compañía energética chilena en enero de 2026.** El grupo incluyó a **Empresas Copec S.A.** en su sitio de fugas, afirmando haber exfiltrado **aproximadamente 6 TB** de información corporativa, y publicó en un segundo servicio oculto **el listado completo de carpetas y ficheros, con buscador**. Entre el material figuran memorandos internos, presupuestos, contratos de suministro de petróleo, y una carpeta de **«Colaboradores»** con subcarpetas por empresa y filial. Valoramos **casi con certeza** *(≥99 %)* que la publicación en el sitio de fugas ocurriera, y **probable** *(55–80 %)* que el volumen y el contenido sean aproximadamente los declarados. **Confianza: alta para la publicación; moderada para el contenido.** *Base:* `B-3`, cobertura chilena con capturas del sitio de fugas, más el **comunicado de la propia compañía** que reconoce «un acceso no autorizado a un sistema de almacenamiento de información de uso interno». **Y conviene subrayar lo que esto significa para esta cartera**: de los seis informes de este lote, **éste es el único cuya afirmación regional se confirma con una víctima nombrada**.

**KJ-2.** **La región ya estaba en su victimología antes del caso chileno, y eso convierte un caso en un patrón incipiente.** El análisis de Trend Micro del 13 de junio de 2025 —cuando el sitio de fugas del grupo tenía **siete entradas en total**— nombra cuatro países con víctima: Australia, Canadá, **Perú** y Estados Unidos. Es decir: **cuando el grupo llevaba siete víctimas conocidas, una ya era peruana**. Valoramos **casi con certeza** *(≥99 %)* que así fuera. **Confianza: alta.** *Base:* `B-1`, leída en original. **Y la lectura que importa:** con siete víctimas y cuatro países, la presencia regional no es un residuo estadístico. El propio análisis describe el enfoque como **oportunista** a través de regiones y sectores, lo que es coherente: un programa de afiliados ataca donde cada afiliado alcanza, y eso **no excluye a nadie por geografía**. A diferencia de `CTI-2026-040`, aquí **no hay ninguna lista de exclusión declarada**.

**KJ-3.** **El rasgo que distingue a este actor no es el cifrado: es que puede borrar, y eso rompe la lógica económica de la extorsión.** El cifrador acepta un parámetro **`/WIPEMODE`** que **vacía el contenido de los ficheros**: en la prueba de laboratorio los ficheros siguen listados en el directorio pero **con tamaño 0 KB**, sin ninguna posibilidad de recuperación. Su analista lo formula con precisión: la función «podría ser útil si el actor no quiere un rescate de la víctima». Valoramos **casi con certeza** *(≥99 %)* que la capacidad exista y funcione así. **Confianza: alta.** *Base:* `B-1`, con capturas del antes y el después. **Y la consecuencia para la decisión es la que importa:** en un cifrado, pagar compra una probabilidad de recuperación; frente a un borrado, **no hay nada que comprar**. Eso invierte el cálculo que toda la industria de respuesta a incidentes da por supuesto, y `E-2` lo desarrolla. **Pero —y esto hay que decirlo con la misma claridad— no hay ningún uso documentado de `/WIPEMODE` contra una víctima real.** La capacidad está probada; el empleo es hipotético, y es el disparador `I-1`.

**KJ-4.** **Y el dato que hay que leer junto al anterior: en los dos ataques de este grupo documentados con detalle, el cifrado fue bloqueado y la extorsión siguió adelante sobre los datos ya robados.** En el caso chileno, el propio grupo declaró en una entrevista que «si bien la defensa de Copec logró mitigar el ataque de *ransomware* en su extensa red, no pudo evitar la exfiltración de datos». En el ataque a una organización estadounidense de octubre de 2026, Symantec documenta que **la carga de cifrado fue bloqueada antes de ejecutarse** y que no hay evidencia de que se cifrara ningún fichero — y aun así el actor había desplegado una puerta trasera propia, trece herramientas de desactivación de seguridad y cinco controladores vulnerables. Valoramos **probable** *(55–80 %)* que el fallo del cifrado sea más frecuente de lo que la marca aparenta, y **muy probable** *(80–95 %)* que la operación esté estructuralmente preparada para extorsionar **sin cifrar**. **Confianza: moderada.** *Base:* `B-2` y `B-3`, dos casos independientes. **Y lo que lo sostiene no es la coincidencia, es el modelo de negocio:** el grupo ofrece **tres programas de afiliados**, y uno de ellos es expresamente de **extorsión por datos robados, sin cifrado**. `E-3` lo desarrolla, y la consecuencia defensiva es incómoda: **bloquear el cifrador no termina el incidente.**

**KJ-5.** **El hallazgo metodológico del informe: los tres relatos del caso chileno parecen contradecirse y son compatibles, porque responden a preguntas distintas.** La compañía declaró que los sistemas que administran datos personales de clientes, claves e información para operar plataformas digitales **no se vieron comprometidos**, que **la operación no se vio afectada** y que notificó a las autoridades. El atacante afirmó haber exfiltrado 6 TB de información interna, incluidos expedientes de personal. Y el atacante añadió que **el cifrado fue mitigado**. Valoramos **muy probable** *(80–95 %)* que las tres afirmaciones sean simultáneamente ciertas. **Confianza: moderada-alta.** *Base:* lectura conjunta del comunicado y de la entrevista en `B-3`. **Por qué son compatibles:** el comunicado habla de **disponibilidad** y de **datos de clientes**; la afirmación del atacante habla de **confidencialidad de datos internos**. Son propiedades distintas de sistemas distintos, y ninguna de las dos partes niega lo que la otra afirma. **Y por qué importa:** quien lea el comunicado como una refutación del atacante concluirá que no pasó nada grave, y quien lea al atacante como una refutación del comunicado concluirá que la compañía mintió. **Las dos lecturas son errores, y el `Anexo D` da el procedimiento para no cometerlos** — en un expediente donde la fuente de casi todos los hechos técnicos es el propio extorsionador.

**KJ-6.** **El vector de acceso declarado es la red privada virtual corporativa, y lo declara el atacante.** En la entrevista, el grupo afirmó haber comprometido inicialmente **la red privada virtual de Copec**. Y hay un dato de contexto que encaja: un tercero vincula la actividad del grupo entre enero y marzo de 2026 con la explotación de **`CVE-2025-5777`**, la vulnerabilidad de Citrix conocida como *CitrixBleed 2*. Valoramos **probable** *(55–80 %)* que el acceso inicial del caso chileno fuera por acceso remoto, y **aproximadamente igual de probable** *(40–60 %)* que fuera específicamente por esa vulnerabilidad. **Confianza: baja para el mecanismo concreto, por la vía.** *Base:* afirmación del atacante en `B-3`, más `B-4`, fuente secundaria. **Y la salvedad que el `Anexo D` obliga a hacer:** un atacante tiene **incentivo a exagerar la sofisticación de su entrada** y **ningún incentivo a mentir sobre el producto concreto**, de modo que esta afirmación cae en la categoría de las más creíbles de su relato — pero sigue siendo su relato.

**KJ-7.** **La capacidad técnica del grupo creció de forma medible entre junio de 2025 y noviembre de 2026, y en una dirección concreta: desactivar la defensa.** En el ataque de octubre de 2026, los operadores desplegaron en **aproximadamente una hora** al menos **trece ejecutables** destinados a terminar servicios de seguridad, junto con **cinco controladores firmados pero vulnerables** para obtener acceso al núcleo. Dos de los ejecutables **se hacían pasar por software de Symantec** y aceptaban conmutadores para **listar y eliminar las retrollamadas del núcleo** registradas por los productos de seguridad. Instalaron además `AnyDesk` y una herramienta que lo **registra como servicio permitido en el Modo seguro con funciones de red**, porque el software de seguridad no opera plenamente en ese modo. Y desplegaron una **puerta trasera propia**, `Lindnor`, que su analista señala como inusual: «pocos operadores de *ransomware* construyen sus propias puertas traseras». Valoramos **casi con certeza** *(≥99 %)* que así fuera. **Confianza: alta.** *Base:* `B-2`, análisis de primera mano con lista íntegra de indicadores. **Y el patrón de uso dice más que el inventario:** desplegar trece herramientas en una hora es, en palabras de su analista, «consistente con atacantes que prueban una herramienta tras otra hasta encontrar algo que funcione». **Eso describe fuerza bruta de evasión, no finura** — y es una ventana de detección, porque trece intentos hacen trece veces más ruido que uno.

**KJ-8.** **Y pese a todo eso, el ataque falló en el último paso.** De los trece ejecutables, **todos fueron bloqueados salvo dos**; y la carga de cifrado **fue bloqueada antes de ejecutarse**. Su analista lo resume así: «a pesar de toda esta preparación, el ataque parece haber fallado en el último obstáculo». Valoramos **casi con certeza** *(≥99 %)* que así ocurriera en ese caso. **Confianza: alta.** *Base:* `B-2`. **Por qué este juicio está en el resumen y no en un anexo:** porque es el único dato francamente favorable de todo este lote de informes, y porque dice algo concreto sobre dónde está el rendimiento de la defensa. **Un adversario que llega con trece herramientas de evasión, cinco controladores vulnerables, una puerta trasera propia y una segunda vía de acceso remoto configurada para el Modo seguro, y aun así no consigue ejecutar el cifrador, describe un control que funcionó.** `E-4` saca las consecuencias sin inflarlas.

**KJ-9.** **Hallazgo propio, y es el tercero de este lote: el cifrador tiene un parámetro en alemán.** La tabla de parámetros publicada por `B-1` incluye **`/PFAD=`** para los directorios a excluir, junto a **`/PATH=`** para las rutas a cifrar. *Pfad* es «ruta» en alemán; el resto de los parámetros —`/KEY=`, `/elevated`, `/WIPEMODE`— está en inglés. Valoramos **probable** *(55–80 %)* que indique participación de habla alemana en el desarrollo. **Confianza: baja, es observación propia y no está comentada por la fuente, que publica el parámetro sin más.** **Y no es atribución**, por la misma razón de siempre: identifica el idioma de quien escribió una línea de código. **Lo que sí merece quedar escrito es que éste es el tercer caso de este lote**: `CTI-2026-043` documentó iniciales de pinyin en un campo de configuración, `CTI-2026-040` un parámetro en portugués, y éste uno en alemán. Tres operaciones distintas, tres idiomas, **y en los tres casos el idioma aparece en el nombre de un parámetro o de un campo y no en las cadenas visibles al usuario**. Es un sitio donde los desarrolladores no limpian, y conviene mirarlo siempre. Es el requisito de colección `I-4`.

**KJ-10.** **Hay cuatro cosas llamadas «Anubis» y confundirlas lleva a conclusiones falsas.** Esta operación de extorsión; el **troyano bancario Anubis para Android**, que es una familia de larga trayectoria y objetivo completamente distinto; la **puerta trasera Anubis en Python** documentada en marzo de 2025 y atribuida a otro actor; y una **herramienta libre homónima de protección de sitios web contra rastreadores automáticos**, que no tiene relación con nada de esto y que **aparece en las búsquedas**. Valoramos **casi con certeza** *(≥99 %)* que sean cuatro objetos distintos. **Confianza: alta.** *Base:* `B-1`, `B-2` y `B-6`. **Y conviene separar este caso del de `CTI-2026-040`:** allí la colisión de nombres era **deliberada**, un adversario que eligió un nombre ocupado para generar confusión. Aquí es **accidental**, como la de `CTI-2026-035` con «Medusa»: cuatro objetos que coincidieron en un nombre mitológico popular. **El efecto para quien ingiere indicadores es el mismo**, y la desambiguación de `O-1` existe por eso.

---

## 2. Resumen ejecutivo

El requisito pedía evaluar una afirmación concreta —un golpe de Anubis al sector energético chileno en enero de 2026— con la advertencia explícita de que probablemente no se podría corroborar. **Se corrobora.** Y es el único informe de este lote cuya afirmación regional se confirma con una víctima nombrada.

En enero de 2026, el grupo publicó a **Empresas Copec S.A.** en su sitio de fugas, afirmando haber exfiltrado **aproximadamente 6 TB** de información corporativa. Montó además un segundo servicio oculto con **el listado completo de carpetas y ficheros y un buscador**, donde figuran memorandos internos, presupuestos, contratos de suministro de petróleo y una carpeta de «Colaboradores» con subcarpetas por filial. Entre lo publicado hay expedientes de personal con contratos laborales, copias de documentos de identidad y certificados de nacimiento, y una hoja de cálculo con **1.969 registros** de usuarios que incluye nombre, identificador fiscal, empresa, cargo, jefatura directa, unidad de negocio y correo corporativo.

La compañía publicó un comunicado. Dice que detectó «un incidente de seguridad asociado a un acceso no autorizado a un sistema de almacenamiento de información de uso interno»; que **los sistemas que administran datos personales de clientes, claves o información para operar plataformas digitales no se vieron comprometidos**; que **la operación de la compañía y sus filiales no se vio afectada**; y que notificó a las autoridades competentes. Y el propio grupo, en una entrevista que concedió a un medio especializado, añadió dos cosas: que comprometió inicialmente **la red privada virtual corporativa**, y que **la defensa de Copec sí consiguió mitigar el ataque de cifrado** en su red, aunque no pudo evitar la exfiltración, que llevó «casi una semana» subiendo datos a baja velocidad por puertas traseras instaladas al efecto.

**Las tres versiones parecen contradecirse y son compatibles, y ése es el hallazgo metodológico de este informe.** El comunicado habla de **disponibilidad** —la operación siguió— y de **datos de clientes**. El atacante habla de **confidencialidad de datos internos**. Son propiedades distintas de sistemas distintos, y ninguna de las dos partes niega lo que la otra afirma. Quien lea el comunicado como refutación del atacante concluirá que no pasó nada; quien lea al atacante como refutación del comunicado concluirá que la compañía mintió. **Las dos lecturas son errores**, y el `Anexo D` da el procedimiento para no cometerlos — que hace falta porque en este expediente **la fuente de casi todos los hechos técnicos es el propio extorsionador**, y el sitio de fugas de un extorsionador es, antes que nada, **publicidad**.

Sobre el actor. Anubis es extorsión como servicio, apareció en diciembre de 2024 como **reconversión de Sphinx** —el código prácticamente intacto, sólo la marca actualizada—, y lo desarrolla un grupo que Symantec designa **Hawkmoth**. Sus representantes se anuncian en foros de habla rusa con **tres programas de afiliados** cuyos repartos son negociables, y uno de ellos es expresamente de **extorsión por datos robados, sin cifrado**. Lleva unas **96 víctimas reclamadas en doce meses**, el 52 % en Estados Unidos. Y la región estaba en su victimología antes del caso chileno: cuando su sitio de fugas tenía **siete entradas en total**, una ya era **peruana**.

Lo que lo distingue técnicamente no es el cifrado: es que **puede borrar**. El cifrador acepta un parámetro `/WIPEMODE` que **vacía el contenido de los ficheros** y los deja listados a 0 KB, sin recuperación posible. Eso rompe la lógica económica de la extorsión, porque frente a un borrado **no hay nada que comprar**. Conviene decir con la misma claridad que **no hay ningún uso documentado de ese modo contra una víctima real**: la capacidad está analizada en laboratorio y es verificable; su empleo es hipotético.

Y hay un dato que conviene leer junto al anterior. En los **dos** ataques de este grupo documentados con detalle, **el cifrado fue bloqueado y la extorsión siguió adelante sobre los datos ya robados**. En el caso chileno lo dice el propio atacante. En un ataque a una organización estadounidense en octubre de 2026, Symantec documenta que la carga de cifrado fue bloqueada antes de ejecutarse, y que aun así los operadores habían desplegado una **puerta trasera propia**, **trece ejecutables** para matar servicios de seguridad en aproximadamente una hora, **cinco controladores firmados pero vulnerables** para llegar al núcleo, y `AnyDesk` configurado para seguir funcionando en **Modo seguro**. La consecuencia defensiva es incómoda y es la del `Anexo D` de `CTI-2026-039` leído al revés: **bloquear el cifrador no termina el incidente**, porque el modelo de negocio no lo necesita.

Ese mismo caso deja, además, el único dato francamente favorable de todo este lote: **de los trece ejecutables, todos fueron bloqueados salvo dos; y la carga de cifrado también.** Un adversario que llega con trece herramientas de evasión, cinco controladores vulnerables, una puerta trasera propia y una segunda vía de acceso remoto configurada para el Modo seguro, y aun así no consigue ejecutar el cifrador, describe un control que funcionó. El patrón de uso dice lo mismo desde otro ángulo: desplegar trece herramientas en una hora es, en palabras de su analista, probar una tras otra hasta encontrar la que funcione. **Eso es fuerza bruta de evasión, no finura — y trece intentos hacen trece veces más ruido que uno.**

<!-- cti:cards -->

| Título | Texto | Etiqueta |
|---|---|---|
| El requisito acertó | Anubis publicó a **Empresas Copec S.A.**, energética chilena, en **enero de 2026**: 6 TB declarados, listado completo de ficheros en un servicio oculto **con buscador**. Y **Perú** ya estaba en su victimología desde junio de 2025 | Corroborado |
| Tres relatos compatibles | La compañía: la operación no se vio afectada y los datos de clientes no se comprometieron. El atacante: 6 TB exfiltrados. Y el atacante otra vez: **el cifrado sí fue mitigado**. **Las tres pueden ser ciertas: no responden a la misma pregunta** | Hallazgo propio |
| Puede borrar | `/WIPEMODE` **vacía el contenido** de los ficheros y los deja a 0 KB. Frente a un borrado **no hay nada que comprar**, y eso rompe el cálculo de pagar. **Pero no hay ningún uso documentado contra una víctima real** | Capacidad |
| El cifrado falla y da igual | En los **dos** ataques documentados con detalle, el cifrador fue bloqueado y la extorsión siguió. **Uno de sus tres programas de afiliados es extorsión sin cifrado.** Bloquear el cifrador no termina el incidente | Hallazgo |
| Trece herramientas en una hora | Más cinco controladores **firmados** y vulnerables, dos ejecutables que **se hacían pasar por software de Symantec**, y `AnyDesk` registrado para el **Modo seguro**. Es fuerza bruta de evasión, no finura | Capacidad |
| Y aun así falló | **Doce de trece ejecutables bloqueados, y el cifrador también.** Es el único dato francamente favorable de este lote, y dice dónde está el rendimiento de la defensa | Decisión |
| Un parámetro en alemán | **`/PFAD=`** junto a `/PATH=`. Tercer caso de este lote tras el pinyin de `CTI-2026-043` y el portugués de `CTI-2026-040`. **Y en los tres el idioma está en el nombre de un parámetro**, que es donde nadie limpia | Hallazgo propio |
| Cuatro cosas, un nombre | Esta extorsión, el **troyano bancario Android**, la **puerta trasera en Python** de otro actor, y una **herramienta libre de protección contra rastreadores** que sale en las búsquedas. A diferencia de `CTI-2026-040`, aquí la colisión es **accidental** | Higiene |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| 6 TB | Volumen exfiltrado **que el atacante declara** en el caso chileno | No verificado por ninguna fuente independiente. **El `Anexo D` trata cómo leer esta clase de cifra** |
| 1.969 | Registros de usuarios en una sola hoja de cálculo publicada | Con nombre, identificador fiscal, empresa, cargo, jefatura, unidad de negocio y correo corporativo |
| ~1 semana | Duración de la exfiltración, **según el atacante** | «Instalaron puertas traseras a través de las cuales continuaron subiendo datos a baja velocidad» |
| 7 → 96 | Víctimas reclamadas: en junio de 2025 y en los doce meses previos a noviembre de 2026 | **El 52 % de las 96 están en Estados Unidos**, según Symantec |
| 4 | Países con víctima cuando el sitio de fugas tenía siete entradas | Australia, Canadá, **Perú** y Estados Unidos. **La presencia regional no es un residuo** |
| 3 | Programas de afiliados, con repartos **negociables** | Extorsión como servicio, **extorsión por datos sin cifrado**, y monetización de accesos — el tercero diseñado para atraer corredores de acceso |
| 13 + 5 | Ejecutables de desactivación de seguridad y controladores vulnerables, en ~1 hora | **Dos se hacían pasar por software de Symantec**, con conmutadores para listar y eliminar retrollamadas del núcleo |
| 12 de 13 | Ejecutables **bloqueados** en el ataque de octubre de 2026 | Y la carga de cifrado también. **El ataque falló en el último obstáculo** |
| 4 | Herramientas distintas de exfiltración en un solo ataque, en julio de 2026 | `Megasync`, `WinSCP`, `Filezilla`, `S3browser`. Su analista lo califica de inusual |
| 0 | Usos documentados de `/WIPEMODE` contra una víctima real | La capacidad está probada en laboratorio; **el empleo es hipotético**. Es el disparador `I-1` |
| 13 | Organizaciones chilenas atacadas por extorsión en el primer trimestre de 2026 | Recuento de un tercero, no verificado. Contexto del caso, no dato del actor |

---

## 3. Alcance, requisitos y limitaciones

**3.1 Requisitos de inteligencia atendidos**

| Req. | Enunciado | ¿Respondido? | Dónde |
|---|---|---|---|
| PIR-01 | ¿Qué actores tienen intención y capacidad contra nuestra región? | **Sí, con una víctima chilena nombrada y una peruana documentada.** Es la respuesta más directa de todo el lote | `KJ-1`, `KJ-2` |
| PIR-02 | ¿Qué afirmaciones del requisito resisten la verificación? | **Sí, y se corrobora la que se daba por improbable** | `3.5` |
| PIR-03 | ¿Qué técnicas invalidan nuestros controles? | **Sí, y la principal es estructural**: el modelo de negocio no necesita que el cifrado funcione | `KJ-4`, `E-3` |
| PIR-06 | ¿Qué efecto tiene la capacidad destructiva sobre la decisión de pagar? | **Sí, y es el objeto de `E-2`** | `KJ-3`, `E-2` |
| PIR-08 | ¿Qué indicadores publicados son peligrosos de ingerir? | **Sí**: cinco controladores **firmados** y cinco herramientas legítimas | `A.6` |
| PIR-09 | ¿Cómo se valora la información que publica un extorsionador sobre su propia víctima? | **Sí, y es la aportación del informe** | `Anexo D` |
| RFI-2026-11-G | El requisito afirmaba un golpe al sector energético en Chile en enero de 2026, con la advertencia de que probablemente no se corroboraría | **Corroborado** | `3.5` |
| PIR-04 | ¿Nos afecta hoy? | **No sin telemetría propia** | `O-4` |

**3.2 Fuera de alcance.** No se evalúan: el **troyano bancario Anubis para Android**, la **puerta trasera Anubis en Python** y la **herramienta libre homónima de protección contra rastreadores web**, que son tres objetos distintos y están aquí sólo para desambiguarlos (`O-1`); la familia `Sphinx` anterior más allá de lo necesario para establecer la reconversión; las familias `EvilByte` y `Prince`, que comparten biblioteca criptográfica y merecerían su propio análisis; la decisión de pagar o no pagar, que es materia de Legal y de Dirección —aunque `E-2` describa cómo la capacidad de borrado la altera—; la situación regulatoria concreta de la compañía afectada bajo el marco chileno de ciberseguridad, que es materia jurídica y no de inteligencia de amenazas; y los datos personales expuestos, que **no se reproducen** (`A.7`).

**3.3 Limitaciones de la colección.** Cinco, y la segunda es el objeto del `Anexo D`.

1. **Sin telemetría propia.** `O-4` es un cuestionario.
2. **En el caso chileno, la práctica totalidad de los hechos técnicos proviene del propio atacante.** El volumen de 6 TB, la vía de acceso por red privada virtual, la duración de la exfiltración y la cifra del rescate son **afirmaciones del extorsionador**, publicadas en su sitio de fugas o dichas en una entrevista que él concedió a un medio especializado. La compañía publicó un comunicado que **no las confirma ni las niega**, porque responde a otra pregunta. **No existe informe independiente del incidente.** Eso no invalida el expediente —hay elementos verificables, y el `Anexo D` los separa— pero condiciona cada cifra.
3. **No hay ningún uso documentado de `/WIPEMODE` contra una víctima real.** La capacidad está analizada con capturas del antes y el después, y es verificable; **su empleo es, hasta donde alcanza esta colección, hipotético**. Conviene no describir a este actor como «el que borra los datos» sin esa salvedad.
4. **Las cifras de víctimas de los rastreadores de terceros son inconsistentes entre sí** —una misma ficha da dos números distintos— y **no se usa ninguna**. La única cifra de víctimas de este informe es la de Symantec, que es de primera mano.
5. **Las fechas del caso chileno difieren entre fuentes.** Una sitúa la publicación el **9 de enero** y otra el **14**. Se consigna el rango y no se elige, porque la diferencia no cambia ningún juicio.

**3.4 Metodología.** ICD 203 para el léxico de probabilidad y confianza (Anexo C). Código Admiralty doble para las fuentes (Anexo B). MITRE ATT&CK v18 en `T-2`. Pirámide del Dolor en `T-3`. ACH y pre-mortem en `O-6`. Desambiguación de objetos homónimos en `O-1`, con el molde de `CTI-2026-035`. **Y la técnica que este informe tuvo que improvisar y que es su aportación generalizable: la lectura conjunta de dos relatos del mismo incidente cuando uno lo publica el extorsionador y el otro la víctima** (`Anexo D`).

**3.5 Lo que el requisito afirmaba, y lo que las fuentes sostienen**

El requisito afirmaba un golpe de Anubis al sector energético en Chile en enero de 2026, **con la advertencia expresa de que probablemente no sería corroborable y que había que verificar antes de escribir**. Se verificó, y se corrobora.

<!-- cti:table highlight="NO corroborado|Sin evidencia|Impreciso|Incompleto|No se pudo|sólo el atacante" -->

| # | Enunciado atómico | Veredicto | Qué dicen las fuentes |
|---|---|---|---|
| 1 | «Existe una operación de extorsión llamada Anubis» | **Corroborado** | `B-1` y `B-2`: extorsión como servicio activa desde **diciembre de 2024**, reconversión de `Sphinx` con la carga prácticamente sin cambios, desarrollada por el grupo que Symantec designa **Hawkmoth**. **Unas 96 víctimas reclamadas en los doce meses previos a noviembre de 2026**, el 52 % en Estados Unidos |
| 2 | «Golpeó al **sector energético**...» | **Corroborado** | `B-3`: **Empresas Copec S.A.** es una compañía energética chilena, y el material publicado incluye **contratos de suministro de petróleo** |
| 3 | «...**en Chile**...» | **Corroborado, y con el nombre de la organización** | `B-3`: publicación en el sitio de fugas del grupo, con capturas, listado de ficheros en un segundo servicio oculto con buscador, **y comunicado oficial de la propia compañía** reconociendo un acceso no autorizado |
| 4 | «...**en enero de 2026**» | **Corroborado, con un rango de fechas** | Las fuentes difieren: una sitúa la publicación el **9 de enero** y otra el **14**. El mes está corroborado; el día exacto no, y no cambia ningún juicio |
| 5 | Implícito: «el ataque fue un cifrado exitoso» | **NO corroborado — y lo niega el propio atacante** | El grupo declaró en una entrevista que «si bien la defensa de Copec logró **mitigar el ataque de *ransomware*** en su extensa red, **no pudo evitar la exfiltración de datos**». Y la compañía declaró que **la operación no se vio afectada**. **Las dos afirmaciones concuerdan**: fue una extorsión por datos robados, no un cifrado consumado (`KJ-4`, `KJ-5`) |
| 6 | Implícito en la nota del requisito: «esto probablemente no se podrá corroborar» | **Refutado, y conviene que conste** | Se corrobora con capturas del sitio de fugas, con el comunicado de la víctima y con una entrevista del atacante. **Es el segundo caso de este lote en que la expectativa pesimista resultó equivocada** — el primero fue `CTI-2026-037`, donde una fuente publicada siete meses antes invertía el veredicto |
| 7 | *(no estaba en el requisito)* «La región es un objetivo aislado para este actor» | **NO corroborado: hay un segundo país, y es anterior** | `B-1`, junio de 2025: cuando el sitio de fugas tenía **siete entradas en total**, los cuatro países con víctima eran Australia, Canadá, **Perú** y Estados Unidos. **Un caso de siete era peruano** |
| 8 | *(no estaba en el requisito, y es lo más consecuente)* «El volumen, la vía de entrada y el rescate son datos del incidente» | **Son afirmaciones del extorsionador, y hay que tratarlas como tales** | Los 6 TB, la red privada virtual como vector, la semana de exfiltración y la cifra del rescate **los dice el atacante**, en su sitio de fugas o en una entrevista que él concedió. **No hay informe independiente.** El `Anexo D` separa lo verificable de lo publicitario |

> ⚠ **Por qué el punto 6 merece quedar escrito.** La nota que acompañaba al
> requisito decía que la afirmación era «muy probablemente no corroborable» y
> pedía verificar antes de escribir. **La instrucción era correcta y la
> expectativa era equivocada**, y la distinción importa: lo correcto fue
> **verificar antes de escribir**, y eso es lo que produjo el hallazgo. Si se
> hubiera actuado sobre la expectativa en lugar de sobre la instrucción —es
> decir, si se hubiera escrito «no corroborado» sin buscar— este informe
> habría negado un incidente real, con víctima nombrada, comunicado público y
> datos personales de mil novecientas sesenta y nueve personas en la red.
> **Es el segundo caso de este lote con la misma forma:** en `CTI-2026-037`
> la primera lectura concluyó que el requisito era falso y una fuente
> publicada siete meses antes lo invirtió. Dos de seis informes. La lección
> operativa está en el `O-2.2` de aquél y se repite aquí: **una expectativa
> sobre el resultado de una búsqueda no es un sustituto de la búsqueda**, y
> las notas de cartera que anticipan el veredicto son útiles para priorizar y
> peligrosas para concluir.

---

# NIVEL ESTRATÉGICO
### Para: Consejo · CISO · Riesgo · Legal · Comunicación · Recursos Humanos · Horizonte: 6–24 meses

## E-1. El caso Copec como lección de comunicación, y no de tecnología

Este expediente contiene algo que esta cartera no había tenido: **un incidente regional con el comunicado de la víctima y la versión del atacante, los dos públicos, sobre el mismo hecho**. Y lo más útil que se puede extraer de ahí no es técnico.

**El comunicado de la compañía, desmontado en lo que afirma.** Son cinco afirmaciones, y conviene ver qué dice cada una y qué deja fuera:

| Lo que dice | Qué propiedad cubre | Qué deja fuera |
|---|---|---|
| «Un acceso no autorizado a un **sistema de almacenamiento de información de uso interno**» | Reconoce el hecho y lo **circunscribe a un sistema** | No dice cuánto había en ese sistema |
| «Los sistemas que administran **datos personales de clientes**, claves o información que permita operar plataformas digitales **no se vieron comprometidos**» | **Confidencialidad de datos de clientes** | **No dice nada de los datos de empleados**, que son los que se publicaron |
| «Todos los sistemas y servicios continúan funcionando con normalidad» | **Disponibilidad** | No dice nada de confidencialidad |
| «Activó de inmediato sus protocolos, bloqueó el acceso comprometido y reforzó sus medidas» | **Respuesta** | — |
| «La operación de Copec y sus filiales **no se vio afectada**. Copec ha **notificado a las autoridades competentes**» | **Disponibilidad** y **cumplimiento** | — |

**Las cinco afirmaciones son compatibles con todo lo que el atacante dice.** El atacante no afirma haber interrumpido la operación —al contrario, dice que el cifrado fue mitigado— ni haber tocado los datos de clientes. Afirma haberse llevado **información interna**, incluidos expedientes de personal. **El comunicado no lo niega: no lo menciona.**

**Y ahí está la lección, que es de redacción y no de seguridad.** Un comunicado construido así es **defendible** —cada frase es verdadera y verificable— y **deja un hueco por el que entra la versión del atacante**. El hueco es el personal propio. Lo publicado, según la cobertura, incluía contratos laborales, copias de documentos de identidad, certificados de nacimiento y una hoja de cálculo con **1.969 registros** con nombre, identificador fiscal, cargo, jefatura directa, unidad de negocio y correo corporativo. **Las personas de esa hoja leyeron un comunicado que decía que los datos personales no se habían comprometido, y hablaba de los de los clientes.**

**La decisión que esto pide, y vale para cualquier organización antes de necesitarla:**

| # | Decisión | Por qué |
|---|---|---|
| 1 | **Que el comunicado diga explícitamente de quién habla.** Si dice «datos personales», que diga de quién: clientes, empleados, proveedores, o todos | Es la ambigüedad que más coste reputacional produce y más fácil de evitar |
| 2 | **Que exista una comunicación separada al personal**, y antes que la pública si es posible | El empleado cuyo documento de identidad está en la red es la parte peor atendida de casi todos los incidentes, y la que más puede dañar a la organización después |
| 3 | **Que Legal decida de antemano qué se afirma sobre el volumen** | El atacante va a dar una cifra. Si la organización no da ninguna, la del atacante es la única; si da una menor sin poder sostenerla, pierde credibilidad |
| 4 | **Que alguien tenga el encargo de leer lo que el atacante publica**, incluidas sus entrevistas | En este caso el atacante dio una entrevista con detalles técnicos. Esa información es inteligencia sobre el propio incidente, y es gratis |

> **Y una observación que conviene no convertir en reproche.** Este apartado
> no juzga la actuación de la compañía afectada, que notificó a las
> autoridades, bloqueó el acceso y, según el propio atacante, **consiguió
> mitigar el cifrado en una red extensa** — lo que, a la vista de
> `CTI-2026-040` y del resto de esta cartera, no es poco. Lo que analiza es
> la **forma del comunicado**, que es un artefacto público y reutilizable como
> material de aprendizaje. Cualquier organización de la región publicaría,
> hoy, un comunicado con la misma estructura.

## E-2. Lo que cambia cuando el adversario puede borrar

El cifrado y el borrado parecen variantes de lo mismo y no lo son: **tienen lógicas económicas opuestas**, y la diferencia decide qué puede hacer la víctima.

| | **Cifrado** | **Borrado** |
|---|---|---|
| Qué vende el adversario | **La clave** | **Nada** |
| Qué compra la víctima pagando | Una probabilidad de recuperación | **Nada** |
| Por qué le interesa al adversario | Es el producto | Es **presión**, o castigo |
| Qué hace la copia de seguridad | La alternativa a pagar | **La única opción** |
| Qué hace la negociación | Baja el precio | **No tiene objeto sobre los datos borrados** |

**El parámetro `/WIPEMODE` de este cifrador vacía el contenido de los ficheros y los deja listados a 0 KB.** Su analista lo formula con exactitud: la función «podría ser útil si el actor no quiere un rescate de la víctima». Es decir, **el borrado no es un fallo del modelo de extorsión: es una opción distinta del mismo producto**, disponible al operador con un conmutador de línea de órdenes.

**Y la consecuencia para la decisión es inmediata y hay que tenerla pensada antes:** si un adversario puede elegir entre cifrar y borrar, entonces **la pregunta «¿pagamos?» deja de tener una respuesta general**, porque depende de algo que la víctima no puede saber en el momento: qué conmutador usó el operador. Lo que sí puede saber es si tiene copia.

**La salvedad, y es grande, y conviene que vaya en la misma frase que todo lo anterior: no hay ningún uso documentado de `/WIPEMODE` contra una víctima real.** La capacidad está probada en laboratorio, con capturas del antes y el después. Su empleo, hasta donde alcanza esta colección, **es hipotético**. Describir a este actor como «el que borra los datos» sin esa salvedad es exactamente la clase de inflación que el `Anexo D` de este informe intenta corregir, y sería irónico cometerla aquí.

**Y una comparación que sitúa esto en su lugar dentro de la cartera.** `CTI-2026-029` documenta el único otro actor de este repositorio con capacidad destructiva —un actor estatal cuyo propósito **es** la destrucción— y la diferencia de intención cambia todo lo demás:

| | `CTI-2026-029` · actor estatal destructivo | **Este informe** · extorsión con borrado |
|---|---|---|
| Para qué destruye | **Es el objetivo**: perturbar | **Es un instrumento de presión**, o un castigo |
| ¿Hay algo que negociar? | **No.** No hay contraparte | Sí, mientras no haya usado el conmutador |
| Qué se defiende | **Recuperabilidad** | Recuperabilidad **y** confidencialidad |
| Predecibilidad | Alta: su propósito es conocido | **Baja: depende de una decisión del operador** |

**La fila de la predecibilidad es la que importa para la planificación.** Contra un actor cuyo propósito es destruir, la organización puede prepararse para la destrucción. Contra uno que **puede elegir**, la preparación tiene que cubrir los dos casos, y eso significa que **la copia de seguridad inmutable deja de ser un control de recuperación y pasa a ser el único instrumento de negociación que la víctima tiene.** Es `X-5.4`.

## E-3. El modelo de negocio no necesita que el cifrado funcione

Éste es el juicio con más consecuencias operativas del informe, y conviene exponerlo despacio porque contradice un supuesto muy extendido.

**Los dos ataques de este grupo documentados con detalle terminan igual: el cifrado bloqueado y la extorsión siguiendo adelante.**

| Caso | Qué pasó con el cifrado | Qué pasó con la extorsión |
|---|---|---|
| **Chile, enero de 2026** | **Mitigado.** Lo dice el propio atacante: «la defensa de Copec logró mitigar el ataque de *ransomware* en su extensa red» | **Siguió**: publicación en el sitio de fugas, segundo servicio oculto con listado y buscador, filtración de expedientes de personal |
| **Estados Unidos, octubre de 2026** | **Bloqueado antes de ejecutarse.** «No hay evidencia de que se cifrara ningún fichero» | *(Symantec no documenta la fase de extorsión; el ataque se interrumpió)* |

**Y lo que convierte esto en estructura y no en coincidencia es el catálogo de servicios del propio grupo.** Ofrece **tres programas de afiliados**, con repartos negociables:

1. **Extorsión como servicio** clásica: el afiliado cifra y comparte el rescate.
2. **Extorsión por datos robados**, sin cifrado.
3. **Monetización de accesos**, diseñada expresamente para atraer a corredores de acceso inicial.

**El segundo programa es la respuesta.** Una operación que vende extorsión sin cifrado **no depende del cifrador**, y por tanto bloquear el cifrador no le quita el negocio: le quita una de tres líneas. Y el tercero explica cómo llega a las víctimas sin tener que entrar él mismo.

**Las tres consecuencias defensivas, y la primera es incómoda:**

1. **Bloquear el cifrador no termina el incidente.** Es el reflejo correcto —y en el caso estadounidense funcionó espléndidamente— pero no cierra la extorsión si los datos ya salieron. El `Anexo D` de `CTI-2026-039` propuso un procedimiento de triaje para cuando un cifrado puede ser la cara visible de un espionaje; **aquí hace falta el procedimiento inverso: qué hacer cuando el cifrado falló y el incidente continúa.** Un equipo que celebre el bloqueo y cierre el caso repetirá el error de forma espejada.
2. **La detección que importa está antes del cifrado, y es la exfiltración.** En el caso chileno la exfiltración llevó, según el atacante, **casi una semana a baja velocidad por puertas traseras instaladas al efecto**. Una semana es una ventana de detección enorme — y «a baja velocidad» es exactamente la elección de diseño que la hace difícil de ver por volumen. En el ataque de julio de 2026, Symantec documenta **cuatro herramientas distintas de exfiltración en un solo ataque**, lo que su analista califica de inusual: `Megasync`, `WinSCP`, `Filezilla` y `S3browser`.
3. **Y la evaluación del daño cambia de eje.** Si el cifrado falla, el daño no es de disponibilidad: es de confidencialidad, y su alcance lo determina **qué había en el sistema al que accedieron**, no cuántas máquinas se cifraron. En el caso chileno, lo que había era un sistema de almacenamiento de información interna con expedientes de personal. **Esa pregunta —qué hay en cada repositorio de ficheros interno— no la responde ningún producto de seguridad**, y es la de `O-4.1`, punto 3.

## E-4. El dato favorable de este lote, y qué dice sin inflarlo

De los seis informes de este lote, éste es el único que contiene un resultado defensivo claramente bueno, y conviene verlo con precisión porque es fácil sacarle demasiado o demasiado poco.

**Lo que ocurrió.** En el ataque de octubre de 2026 a una organización estadounidense, los operadores desplegaron:

- una **puerta trasera propia** —inusual: su analista señala que «pocos operadores de *ransomware* construyen sus propias puertas traseras»—, instalada como servicio en los **dos únicos servidores de base de datos** del conjunto afectado, disfrazada de componente de Chrome en una máquina y de fichero de VMware en la otra;
- **trece ejecutables** en aproximadamente una hora para terminar servicios de seguridad;
- **cinco controladores firmados pero vulnerables** para obtener acceso al núcleo;
- dos ejecutables **que se hacían pasar por software de Symantec**, con conmutadores para **listar y eliminar las retrollamadas del núcleo** registradas por los productos de seguridad;
- `AnyDesk`, una cuenta local nueva, y una herramienta que **registra `AnyDesk` como servicio permitido en el Modo seguro con funciones de red**, porque el software de seguridad no opera plenamente en ese modo.

**Y el resultado: doce de los trece ejecutables fueron bloqueados, y la carga de cifrado también.**

**Qué dice esto, con precisión:**

| Lectura | ¿Sostenible? |
|---|---|
| «La defensa funciona» | **Demasiado general.** Funcionó *ésa*, en *ese* entorno, contra *ese* conjunto de herramientas |
| «El control del puesto es suficiente» | **No.** La exfiltración, que en el caso chileno fue el daño real, **no la bloquea un control de ejecución** |
| «La protección contra alteración y el bloqueo de ejecución rinden contra esta clase de adversario» | **Sí, y es la lectura correcta.** El adversario llegó preparado precisamente para eso, y no le alcanzó |
| «Probar trece herramientas en una hora es una ventana de detección» | **Sí, y es el dato más reutilizable.** Trece intentos hacen trece veces más ruido que uno |

**La última fila es la aportación práctica.** El patrón que su analista describe —«atacantes que prueban una herramienta tras otra hasta encontrar algo que funcione»— no es sofisticación: es **fuerza bruta de evasión**. Y una fuerza bruta es, por definición, **ruidosa**. Un entorno que alerte sobre *intentos* bloqueados de terminar servicios de seguridad —y no sólo sobre los que tienen éxito— tiene en esa hora una señal altísima: **doce bloqueos consecutivos en sesenta minutos no es un falso positivo.**

> **Y el corolario que conviene no perder:** la mayoría de las
> organizaciones configura sus alertas sobre lo que **pasó**, no sobre lo que
> **se intentó y se bloqueó**. En este patrón, **el bloqueo es la alerta**, y
> doce bloqueos seguidos son un incidente en curso. Es `X-3.2`, cuesta una
> regla de correlación, y es lo único de este informe que convierte un
> control que ya existe en una detección que no existía.

## E-5. Decisiones que este informe pide al nivel estratégico

1. **Alertar sobre acumulación de intentos bloqueados de desactivar la seguridad**, no sólo sobre los exitosos. `E-4` y `X-3.2`. Es el hallazgo más rentable del informe: convierte un control que ya existe en una detección que no existía. *Coste: una regla de correlación.*
2. **Escribir el procedimiento de «el cifrado falló y el incidente continúa».** `E-3`, punto 1. Hoy el reflejo es celebrar el bloqueo y cerrar; el modelo de negocio del adversario no lo necesita, y el daño real puede ser anterior. *Coste: una revisión de procedimiento.*
3. **Decidir de antemano la forma del comunicado, y en particular de quién son los datos personales de los que habla.** `E-1`. Y que exista una comunicación separada al personal propio. *Coste: cero, y es una decisión de Comunicación y Legal, no de Seguridad.*
4. **Inventariar qué hay en cada repositorio interno de ficheros.** `E-3`, punto 3. Si el daño es de confidencialidad, el alcance lo determina el contenido del sistema accedido, y esa pregunta no la responde ningún producto. *Coste: proyecto, y es el más lento del informe.*
5. **Tratar la copia de seguridad inmutable como el único instrumento de negociación disponible**, no como un control de recuperación. `E-2`. Frente a un adversario que puede borrar, es lo único que la víctima tiene. *Coste: arquitectura de copias.*
6. **Revisar el acceso remoto y su exposición.** El vector que el propio atacante declara es la red privada virtual corporativa, y hay indicios de explotación de una vulnerabilidad conocida de Citrix en el mismo periodo. *Coste: una revisión de parcheo y de autenticación del acceso remoto.*
7. **Encargar a alguien la lectura de lo que publica el adversario sobre incidentes del sector.** En este caso, el atacante concedió una entrevista con detalles técnicos. Es inteligencia gratuita sobre un incidente regional, y nadie la recoge por sistema. *Coste: cero.*
8. **No adquirir nada por este informe.** Las cinco mitigaciones de `X-5` son de configuración, de procedimiento y de arquitectura de copias. *Coste: cero en licencias.*

---

# NIVEL OPERACIONAL
### Para: Jefatura de SOC · Respuesta a Incidentes · Threat Hunting · Horizonte: semanas–meses

## O-1. Identificación, alias, y las cuatro cosas llamadas «Anubis»

### O-1.1 — El actor

| Designación | Quién la usa | Nota |
|---|---|---|
| **Anubis** | Uso general, y el propio grupo | El nombre de la **marca de extorsión** y de la extensión de fichero |
| **Hawkmoth** | **Symantec**, para el grupo desarrollador | **No es un alias de la marca: es la designación del grupo que desarrolla el cifrador** y opera el programa de afiliados. Distinción útil, porque los ataques los ejecutan afiliados distintos |
| **Sphinx** | Trend Micro y Symantec, para la familia anterior | **No es un alias: es la generación previa.** Los binarios eran «altamente idénticos» con una sola diferencia menor —la función que genera la nota de rescate—, y Symantec confirma que la carga «parece prácticamente sin cambios respecto a la versión de Sphinx, con sólo la marca actualizada» |
| `supersonic` · `superSonic` · `Anubis__media` | Identidades del grupo en foros | En **RAMP** y **XSS** respectivamente, **publicando en ruso** |

### O-1.2 — Las cuatro cosas llamadas «Anubis», y por qué importa

<!-- cti:table highlight="NO es" -->

| Objeto | Qué es | ¿Es éste? |
|---|---|---|
| **Anubis (extorsión)** | La operación de este informe: extorsión como servicio con cifrador y modo de borrado, desde diciembre de 2024 | **Sí** |
| **Anubis (troyano bancario para Android)** | Familia de larga trayectoria dirigida a aplicaciones de banca móvil, con registro de pulsaciones y superposición de pantallas. Objetivo, plataforma y modelo completamente distintos | **NO es éste** |
| **Anubis (puerta trasera en Python)** | Puerta trasera documentada en marzo de 2025 y atribuida a otro actor, en un expediente sin relación con la extorsión | **NO es éste** |
| **Anubis (herramienta libre)** | Programa de código abierto que protege sitios web del rastreo automático masivo mediante prueba de trabajo. **Aparece en las búsquedas y no tiene ninguna relación con nada de lo anterior** | **NO es éste** |

> ⚠ **Por qué esta tabla no es un adorno.** Una búsqueda de «Anubis» devuelve
> las cuatro cosas, y **una ingesta automática de indicadores por nombre de
> familia mezcla material de cuatro expedientes distintos**: indicadores de
> banca móvil, de una puerta trasera de otro actor, y de un proyecto de
> software libre legítimo. `CTI-2026-035` tuvo el mismo problema con cuatro
> cosas llamadas «Medusa», y su `Anexo D` desarrolló el método.
>
> **Y una diferencia con `CTI-2026-040` que conviene marcar.** Allí la
> colisión de nombres era **deliberada**: el actor eligió un nombre ya
> ocupado para explotar la confusión, y su analista lo declaró expresamente.
> **Aquí es accidental**: cuatro objetos que coincidieron en un nombre
> mitológico popular, igual que «Medusa». El efecto práctico para quien
> ingiere es el mismo; **la lectura sobre el adversario es distinta**, y no
> conviene atribuirle una astucia que no se ha demostrado.

## O-2. Estructura y atribución

### O-2.1 — Grado de establecimiento

| Afirmación | Base | Grado |
|---|---|---|
| Anubis es extorsión como servicio activa desde diciembre de 2024, reconversión de `Sphinx` | `B-1` y `B-2`, dos proveedores independientes con comparación de binarios | **Proveedor, corroborado** |
| El grupo desarrollador es el que Symantec designa `Hawkmoth` | `B-2` | **Proveedor** |
| El cifrador acepta `/WIPEMODE` y vacía el contenido de los ficheros | `B-1`, **con capturas del antes y el después** | **Proveedor, de primera mano y verificable** |
| Hay **tres programas de afiliados** con repartos negociables | `B-1`, a partir de la publicación del propio grupo en el foro | **Proveedor, sobre fuente del adversario** |
| ~96 víctimas en doce meses, 52 % en Estados Unidos | `B-2` | **Proveedor, de primera mano** |
| **Perú** entre los cuatro países con víctima en junio de 2025 | `B-1` | **Proveedor, de primera mano** |
| El grupo **publicó** a Copec en su sitio de fugas en enero de 2026 | `B-3`, con capturas | **Proveedor por referencia, corroborado por el comunicado de la víctima** |
| Copec reconoce **un acceso no autorizado a un sistema de almacenamiento interno**, sin afectación a la operación ni a datos de clientes | **Comunicado de la propia compañía**, reproducido en `B-3` | **Declaración de la víctima** |
| 6 TB exfiltrados; acceso por **red privada virtual**; exfiltración de ~una semana; rescate de cientos de miles de dólares | **Afirmaciones del atacante**, en su sitio de fugas y en una entrevista que concedió | **Declaración del adversario** (`Anexo D`) |
| El cifrado **fue mitigado** en el caso chileno | **Afirmación del atacante**, concordante con el comunicado de la víctima | **Declaración del adversario, corroborada indirectamente** |
| Explotación de `CVE-2025-5777` entre enero y marzo de 2026 | `B-4`, fuente secundaria | **Proveedor, no leído en original** |
| `/PFAD=` está en alemán | **Observación propia** sobre literal de `B-1` | **Propio, confianza baja** (`KJ-9`) |
| Hay víctimas latinoamericanas además de Chile y Perú | **Nada** | **Sin evidencia** |

> **Una observación sobre la fila más importante de esta tabla, que es la
> novena.** Casi todos los datos cuantitativos del caso regional caen en el
> grado **«declaración del adversario»**, y esta cartera no tenía ese grado
> hasta ahora. No es lo mismo que «sin evidencia» —hay una afirmación
> concreta, atribuible y a veces costosa de fabricar— ni que «proveedor» —no
> hay método expuesto ni verificación—. **Es una categoría propia con reglas
> propias**, y el `Anexo D` las desarrolla.

### O-2.2 — La reconversión, y por qué es más limpia que la de `CTI-2026-040`

Las dos operaciones de extorsión de este lote son reconversiones de marca, y conviene compararlas porque el grado de certeza es muy distinto:

| | `CTI-2026-040` · BlackSuit → `Chaos` | **Este informe** · `Sphinx` → Anubis |
|---|---|---|
| Qué se compara | Metodología de cifrado, estructura de la nota, conjunto de herramientas | **Los binarios** |
| Resultado de la comparación | «Similitudes» | **«Altamente idénticos», con una sola diferencia: la función que genera la nota** |
| Confianza declarada | **Moderada** | No se declara como valoración: se describe como **observación de comparación de binarios** |
| Corroboración independiente | No | **Sí**: Symantec, por su cuenta, dice que la carga «parece prácticamente sin cambios respecto a la versión de Sphinx, con sólo la marca actualizada» |
| Grado de establecimiento | Proveedor, confianza moderada | **Proveedor, corroborado por dos** |

**La diferencia importa para lo que se puede afirmar hacia afuera**, y también para una lección de método: cuando una reconversión se puede establecer **comparando binarios**, el juicio es de otra naturaleza que cuando hay que inferirla de similitudes de conducta. `CTI-2026-040` tuvo que reconstruir el mecanismo concreto para hacer auditable una valoración; **aquí no hace falta, porque la comparación ya está hecha y la hicieron dos proveedores por separado.**

### O-2.3 — Los dos informes de extorsión de este lote, comparados

| | `CTI-2026-040` · BlackSuit → `Chaos` | **Este informe** · `Sphinx` → Anubis |
|---|---|---|
| Linaje | Conti → Royal → BlackSuit → `Chaos` | `Sphinx` → Anubis |
| Estado del predecesor | **Desarticulado** judicialmente | Simplemente **rebautizado** |
| Vector distintivo | **Llamada telefónica** suplantando a soporte | **Suplantación por correo**; y en el caso chileno, **la red privada virtual** |
| Capacidad destructiva | No, más allá del cifrado | **Sí: modo de borrado** |
| Exclusiones declaradas | **BRICS, CEI, hospitales, gobierno** | **Ninguna** |
| Programas de afiliados | Uno, con cuota reembolsable | **Tres, con repartos negociables** |
| Artefacto de idioma | `/ignorar_arquivos_grandes` — **portugués** | `/PFAD=` — **alemán** |
| Víctima regional | Ninguna documentada | **Chile (nombrada) y Perú** |
| Qué enseña a esta cartera | Cómo evaluar una desarticulación | **Cómo leer la afirmación de un extorsionador** |

> **La fila de las exclusiones es la que decide la prioridad relativa para
> esta región, y conviene decirlo sin rodeos.** El grupo de `CTI-2026-040`
> declara evitar los países BRICS, lo que cubre a Brasil. **Este grupo no
> declara ninguna exclusión, su analista describe su enfoque como
> oportunista, y tiene dos víctimas latinoamericanas documentadas.** De los
> dos expedientes de extorsión de este lote, **éste es el que más
> directamente concierne a la región.**

## O-3. Modelo de operación

### O-3.A — La cadena, fase por fase

| Fase | Qué ocurre | Dónde queda rastro |
|---|---|---|
| **Acceso inicial** | **Suplantación dirigida por correo** con adjunto o enlace, construida para parecer de una fuente de confianza (`B-1`). **En el caso chileno, el atacante declara la red privada virtual corporativa** (`B-3`). Y hay indicios de explotación de `CVE-2025-5777` de Citrix entre enero y marzo de 2026 (`B-4`) | Pasarela de correo; **o registro de autenticación del acceso remoto** |
| **Puerta trasera** *(caso de octubre de 2026)* | **`Lindnor`**, puerta trasera propia, instalada **como servicio** en los dos únicos servidores de base de datos del conjunto afectado, con nombre `healthcontroller64.exe` en una carpeta que imita un directorio de Chrome y `svchelper.exe` en una carpeta de VMware. Envía identificador de proceso, versión del sistema, su propia ruta, nombre de equipo, de usuario, dominio y servidor de inicio de sesión. **Mando y control primario y de reserva, los dos por el puerto 443** | Servicio nuevo; conexión a 443 desde un proceso de servicio |
| **Comprobación de privilegios** | Intenta abrir **`\\.\PHYSICALDRIVE0`**, operación de bajo nivel que requiere permisos elevados. Si los tiene, muestra «*Admin privileges detected. Attempting to elevate to SYSTEM...*»; si no, pregunta «*No admin privileges. Start process anyway?*» **y espera entrada del usuario** | Apertura del dispositivo físico; **y una ventana de consola interactiva** |
| **Desactivación de la defensa** | **Trece ejecutables en ~1 hora** y **cinco controladores firmados pero vulnerables**. Dos ejecutables **se hacen pasar por software de Symantec** y aceptan `-l` para listar las retrollamadas del núcleo y `-d` para listarlas **y eliminarlas**; se observó el uso de `-d` | Escrituras en disco en ráfaga; **y doce bloqueos consecutivos** |
| **Acceso de reserva** | `AnyDesk`, una cuenta local nueva añadida a un grupo local, y **`safemode.exe`**, que registra `AnyDesk` como servicio permitido en el **Modo seguro con funciones de red** | **Clave de registro de `SafeBoot\Network`** |
| **Exfiltración** | En el caso chileno, según el atacante, **casi una semana subiendo datos a baja velocidad por puertas traseras instaladas al efecto**. En el ataque de julio de 2026, **cuatro herramientas distintas en un solo ataque**: `Megasync`, `WinSCP`, `Filezilla`, `S3browser` | **Volumen saliente sostenido y bajo**, no un pico |
| **Impacto** | `vssadmin delete shadows /for=norealvolume /all /quiet`; terminación de procesos y servicios; cifrado con **ECIES** sobre una biblioteca pública en Go; extensión **`.anubis`**; notas **`restore files.txt`** y **`restore files.html`**; iconos y fondo de escritorio propios desde `C:\ProgramData` | — |
| **Borrado** *(opcional)* | **`/WIPEMODE`**: vacía el contenido de los ficheros, que quedan listados **a 0 KB** | — |
| **Extorsión** | Sitio de fugas; y en el caso chileno, **un segundo servicio oculto con el listado completo de carpetas y ficheros y un buscador** | — |

### O-3.B — Las cuatro decisiones de diseño que delatan al operador

**La primera: el cifrador pregunta.** Si no detecta privilegios de administrador, **muestra un mensaje y espera entrada del usuario**: «¿Iniciar el proceso de todos modos?». Su analista extrae la conclusión correcta —«estos avisos interactivos muestran que el programa sigue mejorándose y en desarrollo»— y hay una segunda, operativa: **un cifrador que abre una consola interactiva es visible**. En un servidor sin sesión interactiva, además, **se queda esperando**.

**La segunda: la criptografía es de biblioteca pública, y compartida.** El cifrado usa **ECIES** a partir de una biblioteca **públicamente disponible en Go**, y su analista señala que es **similar a la de las familias `EvilByte` y `Prince`**. Eso tiene dos lecturas: el grupo **no desarrolló su criptografía**, lo que acota su capacidad; y **la biblioteca compartida no es un indicio de relación entre las familias**, porque está pública. Conviene no confundir las dos cosas: es el mismo error que atribuir por un par de carga lateral popular, documentado en `CTI-2026-043`.

**La tercera: hay un fallo, y es informativo.** El cifrador extrae `icon.ico` y `wall.jpg` a `C:\ProgramData` e intenta cambiar el fondo de escritorio a `wall.jpg`; en la prueba, **el intento falló porque el fichero no se había depositado**. Es un fallo menor y dice algo: **el control de calidad no es el de una operación madura**, lo que concuerda con los avisos interactivos y con que el cifrado haya fallado en los dos casos documentados.

**Y la cuarta, que es la más consecuente: la lista de carpetas excluidas del cifrado está pensada para no romper el sistema.** Excluye `windows`, `system32`, `programdata`, los dos `program files`, `AppData`, `public`, información de volumen del sistema, `efi`, `boot`, `perflogs`, `microsoft`, `intel`, y los directorios de herramientas de desarrollo `.dotnet`, `.gradle`, `.nuget`, `.vscode` y `msys64`. **Las cuatro últimas son reveladoras**: excluir los cachés de herramientas de desarrollo no protege al sistema, **protege la velocidad** —son directorios con decenas de miles de ficheros pequeños— y sugiere que el autor tropezó con ese problema y lo resolvió. Es la huella de alguien que probó su cifrador en una máquina de desarrollo.

## O-4. Nuestra exposición

### O-4.1 — El cuestionario, por orden de lo que decide

| # | Pregunta | A quién se pregunta | Por qué decide |
|---|---|---|---|
| 1 | ¿Alertamos sobre **intentos bloqueados** de terminar servicios de seguridad, o sólo sobre los exitosos? | SOC | **El hallazgo más rentable del informe** (`E-4`, `X-3.2`): doce bloqueos consecutivos en una hora no son un falso positivo |
| 2 | ¿Está activa la **protección contra alteración** del agente de seguridad, y hay **control de controladores vulnerables**? | Plataforma de dispositivos | Es lo que resistió en el caso de octubre de 2026, frente a cinco controladores firmados |
| 3 | **¿Qué hay dentro de cada repositorio interno de ficheros?** | Dueños de la información | **Si el cifrado falla, el daño es de confidencialidad y su alcance lo determina el contenido, no el número de máquinas.** Ningún producto responde esto |
| 4 | ¿Detectaríamos una **exfiltración de una semana a baja velocidad**? | SOC / Redes | Es el método declarado en el caso chileno, y está diseñado para no producir un pico |
| 5 | ¿Nuestro procedimiento contempla **«el cifrado falló y el incidente continúa»**? | Respuesta a Incidentes | `E-3`. Hoy el reflejo es celebrar el bloqueo y cerrar |
| 6 | ¿Hay **`AnyDesk` registrado para el Modo seguro** en algún equipo? | SOC | Es una clave de registro muy específica y sin uso legítimo normal |
| 7 | ¿Nuestro **acceso remoto** está parcheado y con autenticación resistente? | Redes / Identidad | Es el vector declarado del caso chileno, con `CVE-2025-5777` como candidato |
| 8 | ¿Tenemos **copias inmutables** fuera del alcance de la red? | Infraestructura | `E-2`. Frente a un adversario que puede borrar, es el único instrumento de negociación |
| 9 | ¿Hay un procedimiento de **comunicación al personal propio** en caso de filtración de sus datos? | Comunicación / Recursos Humanos | `E-1`. En el caso chileno, lo publicado fueron expedientes de personal |
| 10 | ¿Alguien **lee lo que el adversario publica** sobre incidentes del sector? | CTI | En este caso el atacante dio una entrevista con detalles técnicos. Es inteligencia gratis |

### O-4.2 — Qué se puede medir hoy

1. **Preguntar si las alertas cubren intentos bloqueados.** Una pregunta al SOC, y decide la medida más rentable del informe.
2. **Buscar la clave de `SafeBoot\Network` con `AnyDesk`** o cualquier otra herramienta de acceso remoto. Consulta de registro, trivial y muy específica.
3. **Cruzar los indicadores de `A.3` con los registros de doce meses.** Son catorce hashes de primera mano publicados por Symantec.
4. **Buscar `\\.\PHYSICALDRIVE0` abierto por un proceso que no es de disco o de respaldo.** Es la comprobación de privilegios del cifrador, y es un acceso inusual.

## O-5. Cronología

| Fecha | Hecho | Fuente | Grado |
|---|---|---|---|
| **2024-12** | El grupo abre cuenta en una red social; y se identifica una muestra de **`Sphinx`** en desarrollo, con nota de rescate **sin sitio Tor ni identificador único** | `B-1` | Proveedor |
| **2024-12** | **Aparición de Anubis como reconversión de `Sphinx`**: binarios «altamente idénticos», con una sola diferencia menor | `B-1`, `B-2` | **Proveedor, corroborado por dos** |
| **2025-02-23** | `superSonic` anuncia en el foro **RAMP** un «nuevo formato» de programas de afiliados, **todos negociables** para cooperación de largo plazo | `B-1` | Proveedor, sobre fuente del adversario |
| **2025-06-13** | Trend Micro publica el análisis del cifrador y del modo de borrado. **Siete víctimas en el sitio de fugas; cuatro países, PERÚ incluido** | `B-1` | **Proveedor, de primera mano** |
| **2026-01-09** *(o 01-14)* | **Anubis publica a Empresas Copec S.A. en su sitio de fugas**, con 6 TB declarados, segundo servicio oculto con listado y buscador, y expedientes de personal | `B-3` | Proveedor por referencia |
| **2026-01** | **Comunicado de Copec**: acceso no autorizado a un sistema de almacenamiento interno; datos de clientes no comprometidos; operación no afectada; autoridades notificadas | `B-3` | **Declaración de la víctima** |
| **2026-01** | **Entrevista del grupo**: acceso inicial por la red privada virtual; **el cifrado fue mitigado**; exfiltración de casi una semana a baja velocidad por puertas traseras | `B-3` | **Declaración del adversario** |
| **2026-01 → 03** | Actividad del grupo vinculada a la explotación de `CVE-2025-5777` (*CitrixBleed 2*) | `B-4` | Proveedor, no leído en original |
| **2026-Q1** | Un recuento de terceros sitúa **trece organizaciones chilenas** atacadas por extorsión en el trimestre | `B-5` | Tercero, no verificado |
| **2026-07** | Ataque con **cuatro herramientas distintas de exfiltración** en un solo incidente | `B-2` | **Proveedor, de primera mano** |
| **2026-07** | El grupo reclama públicamente un ataque a una filial lechera de una multinacional de bebidas, con ~1 TB, y después lo filtra | `B-4` | Proveedor, no leído en original |
| **2026-10** | **Ataque a una organización estadounidense**: puerta trasera `Lindnor`, trece ejecutables en una hora, cinco controladores vulnerables, `AnyDesk` en Modo seguro. **Doce de trece bloqueados, y el cifrador también** | `B-2` | **Proveedor, de primera mano** |
| **2026-11-05** | Symantec publica el análisis. **~96 víctimas reclamadas en doce meses, 52 % en Estados Unidos** | `B-2` | Proveedor |
| **2026-11-19** | Emisión de este informe | — | — |

> **Dos observaciones que no se ven fila a fila.** La primera: **entre la
> primera muestra de `Sphinx` «en desarrollo» y las noventa y seis víctimas
> reclamadas hay menos de dos años**, y en ese tiempo el grupo pasó de un
> cifrador que preguntaba al usuario si quería continuar a desplegar una
> puerta trasera propia y trece herramientas de evasión. **La curva de
> capacidad es pronunciada.** La segunda: las dos filas de enero de 2026 —el
> comunicado y la entrevista— son, juntas, el material más inusual de este
> expediente. **Que la víctima y el atacante hablen públicamente del mismo
> incidente en el mismo mes es raro, y es lo que hace posible el `Anexo D`.**

## O-6. Hipótesis alternativas consideradas

| Hipótesis | Evidencia a favor | Evidencia en contra | Valoración |
|---|---|---|---|
| **H-A.** El incidente chileno fue una extorsión por datos robados, sin cifrado consumado | **Lo dice el atacante** —«la defensa logró mitigar el ataque de *ransomware*»— y **concuerda con el comunicado de la víctima**, que afirma que la operación no se vio afectada. Y concuerda con el caso de octubre de 2026, donde el cifrador fue bloqueado | Las dos partes tienen incentivos para describirlo así: la víctima para minimizar, el atacante para explicar por qué no hubo cifrado sin admitir un fracaso | **Muy probable** *(80–95 %)* — **hipótesis preferida** |
| **H-B.** El volumen de 6 TB es sustancialmente exagerado | Es una cifra del atacante, y **el volumen es la métrica que un extorsionador tiene más incentivo a inflar**, porque es la que fija el precio y la credibilidad de la amenaza | El grupo publicó **el listado completo de ficheros con buscador**, lo que hace la cifra **parcialmente verificable por cualquiera** y por tanto costosa de inventar; y la víctima no la ha disputado | **Aproximadamente igual de probable** *(40–60 %)* que esté inflada; **poco probable** *(20–45 %)* que lo esté en un orden de magnitud |
| **H-C.** El acceso inicial fue por la red privada virtual, como dice el atacante | Es su afirmación, y **un atacante no tiene incentivo a mentir sobre el producto concreto por el que entró**: no le añade prestigio ni le protege. Hay además indicios de explotación de una vulnerabilidad de Citrix en el mismo periodo | No hay confirmación independiente; y un atacante **sí** tiene incentivo a presentar su entrada como técnica en lugar de como un error de la víctima —una credencial filtrada, por ejemplo— | **Probable** *(55–80 %)* |
| **H-D.** `/WIPEMODE` se ha usado contra alguna víctima real | La capacidad existe, está probada y es trivial de invocar; y un operador frustrado por un cifrado bloqueado tendría motivo | **Ninguna fuente documenta un solo caso.** Y un borrado produciría un incidente muy visible y muy comentado, difícil de ocultar | **Poco probable** *(20–45 %)*, y es `I-1` |
| **H-E.** La región es un objetivo deliberado de este grupo | Dos países con víctima, uno de ellos nombrado; y **ninguna lista de exclusión declarada**, a diferencia de `CTI-2026-040` | Su analista describe el enfoque como **oportunista**; el 52 % de las víctimas está en Estados Unidos; y un programa de afiliados ataca donde cada afiliado alcanza | **Poco probable** *(20–45 %)* como selección deliberada; **muy probable** *(80–95 %)* que la región siga apareciendo **por ausencia de exclusión** |
| **H-F.** El grupo es menos capaz de lo que su inventario de herramientas sugiere | El cifrador **pregunta al usuario** si no tiene privilegios; **falla** al poner el fondo de escritorio; la criptografía es de **biblioteca pública**; y **en los dos casos documentados el cifrado no se ejecutó** | Desplegó una **puerta trasera propia**, que su analista señala como inusual entre operadores de extorsión; y trece herramientas de evasión con cinco controladores firmados | **Probable** *(55–80 %)* para la **ejecución**; y **la capacidad de desarrollo es desigual**, que es la lectura más precisa |

**Pre-mortem.** Si en seis meses este informe resulta haber sido un error, ¿cuál será la causa más probable?

1. **Que `KJ-3` se haya citado sin su salvedad**, convirtiendo a este actor en «el que borra los datos» cuando **no hay ni un uso documentado**. Es el riesgo principal, y es el que el propio informe está en mejor posición de cometer.
2. **Que las cifras del atacante se hayan citado como datos del incidente.** Los 6 TB, la semana, el rescate: todo lo dice él. El `Anexo D` existe para esto y aun así es el error más probable, porque las cifras son concretas y las cifras concretas se citan.
3. **Que el comunicado de la víctima se haya leído como una refutación del atacante, o al revés.** `KJ-5`. Las dos lecturas son errores y las dos son naturales.
4. **Que nadie haya configurado la alerta sobre intentos bloqueados** (`E-4`), que es la única medida de este informe que convierte un control existente en una detección nueva y cuesta una regla.
5. **Que `KJ-9` se haya ascendido a atribución.** Un parámetro en alemán identifica el idioma de quien escribió una línea de código. Y es el tercer caso de este lote, lo que debería inducir cautela y no confianza: si tres operaciones distintas tienen artefactos en tres idiomas distintos, **lo que el patrón demuestra es que el idioma de un parámetro es un dato débil**, no que sea revelador.
6. **Que se haya confundido alguno de los cuatro «Anubis».** `O-1.2`.

## O-7. Indicadores y señales de alerta

| Señal | Qué significaría | Acción inmediata |
|---|---|---|
| **Varios intentos bloqueados de terminar servicios de seguridad en una ventana corta** | **La señal de mayor valor del informe.** Doce bloqueos en una hora no son un falso positivo: es un adversario probando una herramienta tras otra | **Incidente con prioridad máxima.** El bloqueo no es el final: es el aviso |
| Carga de un **controlador firmado pero vulnerable** conocido | Acceso al núcleo en preparación | Incidente |
| Un ejecutable que **se hace pasar por software de seguridad** y acepta conmutadores para listar o eliminar retrollamadas del núcleo | Desactivación de la defensa en curso | Incidente |
| **`AnyDesk` registrado bajo `SafeBoot\Network`** | **Acceso de reserva para el Modo seguro**, donde el software de seguridad no opera plenamente. Clave muy específica y sin uso legítimo normal | Incidente |
| Un **servicio nuevo** con nombre que imita un componente de Chrome o de VMware, hablando por el **443** a dos destinos | Puerta trasera `Lindnor` | Incidente. **Y la puerta trasera apareció también en redes sin actividad de cifrado**: puede ser el único indicio |
| Apertura de **`\\.\PHYSICALDRIVE0`** por un proceso que no es de disco ni de respaldo | Comprobación de privilegios del cifrador | Incidente |
| **Volumen saliente sostenido y bajo** durante días, hacia un destino de almacenamiento o sincronización | **El método declarado en el caso chileno.** Diseñado para no producir un pico | Incidente; **cortar la salida antes que el proceso** |
| Presencia de **varias** herramientas de exfiltración distintas | Patrón documentado: cuatro en un solo ataque | Incidente |
| `vssadmin delete shadows /for=norealvolume /all /quiet` | Fase de impacto. **El literal `norealvolume` es inusual y buscable** | Incidente, y es tarde |
| Ficheros con extensión **`.anubis`**, notas **`restore files.txt`** o **`restore files.html`**, o `icon.ico` y `wall.jpg` en `C:\ProgramData` | Cifrado consumado o intentado | **Ejecutar el procedimiento de `E-3`: el cifrado puede haber fallado y el incidente seguir** |
| Ficheros **listados a 0 KB** en masa | **`/WIPEMODE`.** Sería el **primer caso documentado** | Incidente; **y comunicarlo, porque cerraría `I-1` para toda la comunidad** |
| Una **tercera víctima latinoamericana** | `H-E` se reevalúa | **Revisión anticipada obligatoria** |

---

# NIVEL TÁCTICO
### Para: Analistas de SOC · Ingeniería de Detección · Threat Hunting · Horizonte: días–semanas

## T-1. Cadena de intrusión

`Suplantación dirigida por correo con adjunto o enlace` **o** `compromiso del acceso remoto —red privada virtual, con CVE-2025-5777 como candidato—` → `Puerta trasera propia instalada como servicio, disfrazada de componente de Chrome o de VMware, con C2 primario y de reserva por el puerto 443` → `Comprobación de privilegios abriendo \\.\PHYSICALDRIVE0; si no los tiene, PREGUNTA al usuario` → `Trece ejecutables en ~1 h para terminar servicios de seguridad, más cinco controladores firmados y vulnerables para llegar al núcleo` → `AnyDesk más una cuenta local nueva, y AnyDesk registrado como servicio permitido en Modo seguro con red` → `Exfiltración lenta y sostenida —casi una semana en el caso chileno— por puertas traseras, o con varias herramientas legítimas a la vez` → `vssadmin delete shadows /for=norealvolume /all /quiet` → **bifurcación**: `cifrado con ECIES, extensión .anubis, notas restore files.*` **o** `/WIPEMODE: contenido vaciado, ficheros a 0 KB` → `Extorsión: sitio de fugas, y en el caso chileno un segundo servicio oculto con listado completo y buscador`

> ⚠ **Las dos fases que invierten el supuesto habitual.** La primera: **la
> fase de desactivación de la defensa es, en este adversario, la más ruidosa
> de toda la cadena** —trece ejecutables en una hora— y en el caso
> documentado **doce de los trece fueron bloqueados**. Eso convierte el
> bloqueo en la señal (`X-3.2`). La segunda: **la bifurcación final puede no
> ocurrir**. En los dos casos documentados con detalle el cifrado no se
> ejecutó, y la extorsión siguió sobre los datos ya robados. **La cadena no
> termina donde uno espera.**

## T-2. Mapa MITRE ATT&CK

Marco: **ATT&CK v18**. **(TM)** Trend Micro; **(SY)** Symantec; **(AT)** declaración del atacante; **▲** prioridad de detección.

| Táctica | ID | Técnica | Cómo se manifiesta |
|---|---|---|---|
| Acceso inicial | `T1566` | Suplantación | Correo dirigido con adjunto o enlace, construido para parecer de fuente de confianza **(TM)** |
| | `T1133` | Servicios remotos externos | **La red privada virtual corporativa, en el caso chileno (AT)**; y `CVE-2025-5777` como candidato |
| Ejecución | `T1059` | Intérprete de órdenes | El cifrador toma varios parámetros y depende de ellos para funcionar **(TM)** |
| Persistencia | `T1543.003` ▲ | **Servicio de Windows** | **`Lindnor` instalada como servicio** con nombre que imita un componente de Chrome o un fichero de VMware **(SY)** |
| | `T1136.001` | Creación de cuenta local | Cuenta nueva añadida a un grupo local **(SY)** |
| | `T1219` ▲ | Software de acceso remoto | **`AnyDesk`, y `safemode.exe` que lo registra como servicio permitido en Modo seguro con red** **(SY)** |
| | `T1542.001` ▲ | **Persistencia previa al arranque: Modo seguro** | `reg add HKLM\SYSTEM\CurrentControlSet\Control\SafeBoot\Network\AnyDesk /ve /t REG_SZ /d Service /f`. **El software de seguridad no opera plenamente en Modo seguro** **(SY)** |
| Escalada | `T1134.002` | Manipulación de vales: crear proceso con vale | Comprobación de privilegios abriendo **`\\.\PHYSICALDRIVE0`**, y relanzamiento con `/elevated` **(TM)** |
| Evasión | `T1562.001` ▲ | **Deshabilitar herramientas de seguridad** | **Trece ejecutables en ~1 hora.** Dos **se hacen pasar por software de Symantec** y aceptan `-l` para listar las retrollamadas del núcleo y `-d` para **listarlas y eliminarlas**; se observó `-d` **(SY)** |
| | `T1211` / `T1068` ▲ | **Explotación para evasión y escalada: BYOVD** | **Cinco controladores firmados pero vulnerables.** Su analista subraya que la técnica «se ha convertido en parte estándar del manual del *ransomware*» y que la herramienta llega **empaquetada con las ofertas de extorsión como servicio** **(SY)** |
| | `T1036.005` | Enmascaramiento | `healthcontroller64.exe`, `svchelper.exe`, `gbbsym.exe`, `symgooq.exe`, `iservice.exe` **(SY)** |
| | `T1489` | Detención de servicio | Lista de procesos y servicios terminados **(TM)** |
| Descubrimiento | `T1083` | Ficheros y directorios | Recorrido con lista de carpetas excluidas **(TM)** |
| | `T1082` | Información del sistema | La puerta trasera envía identificador de proceso, versión del sistema, su propia ruta, nombre de equipo, de usuario, dominio y servidor de inicio de sesión **(SY)** |
| Recolección y exfiltración | `T1567.002` ▲ | **Exfiltración por servicio de almacenamiento en nube** | **Cuatro herramientas distintas en un solo ataque**: `Megasync`, `WinSCP`, `Filezilla`, `S3browser` **(SY)**. Y en el caso chileno, **casi una semana a baja velocidad por puertas traseras (AT)** |
| Mando y control | `T1071.001` | Protocolos web | **C2 primario y de reserva, los dos por el 443** **(SY)** |
| | `T1008` | Canales de respaldo | El par primario/reserva **(SY)** |
| Impacto | `T1490` | Inhibir recuperación | `vssadmin delete shadows /for=norealvolume /all /quiet` **(TM)** |
| | `T1486` | Datos cifrados para impacto | **ECIES** sobre biblioteca pública en Go, similar a la de `EvilByte` y `Prince`. Extensión `.anubis` **(TM, SY)** |
| | `T1485` ▲ | **Destrucción de datos** | **`/WIPEMODE`: vacía el contenido, ficheros a 0 KB.** Capacidad probada; **uso real no documentado** **(TM)** |
| | `T1491.001` | Desfiguración interna | Cambia los iconos de los ficheros cifrados por su logotipo, e **intenta** cambiar el fondo de escritorio — y **falla**, porque el fichero no se depositó **(TM)** |
| | `T1657` | Robo financiero | Doble extorsión; **y tres programas de afiliados, uno de ellos sin cifrado** **(TM)** |

**Las ▲, y por qué.** `T1562.001` y `T1211` son la fase más ruidosa y la que produjo la señal del informe: **doce bloqueos consecutivos**. `T1542.001` es la clave de registro más específica del expediente y no tiene uso legítimo normal. `T1543.003` y `T1219` son la persistencia, y la puerta trasera apareció **también en redes sin actividad de cifrado**, de modo que puede ser el único indicio. `T1567.002` es donde está el daño real cuando el cifrado falla. Y `T1485` está marcada **a pesar de no tener un uso documentado**, para que figure que la capacidad existe y que su primera aparición real sería un hecho notable.

## T-3. Dónde atacamos en la Pirámide del Dolor

| Nivel | Valor aquí | Por qué |
|---|---|---|
| **Hashes** | **Medio-alto, y es inusual decirlo** | Symantec publica **catorce hashes de primera mano** de un ataque de octubre de 2026, incluidas tres variantes de la puerta trasera propia. **Una puerta trasera propia se recompila menos que un cifrador de afiliados**, y además apareció en **tres organizaciones distintas** — dos de ellas sin cifrado. Es el caso de esta cartera en que un hash rinde más de lo habitual |
| **Direcciones IP** | **Bajo** | Symantec no publica las direcciones del par de C2; sólo que son dos y que usan el 443 |
| **Dominios** | **Bajo** | La extorsión se publica en servicios ocultos, por víctima |
| **Artefactos de red** | **Medio** | Dos destinos por el 443 desde un proceso de servicio; **volumen saliente sostenido y bajo durante días** |
| **Artefactos de anfitrión** | **Alto** | La clave de `SafeBoot\Network`; apertura de `\\.\PHYSICALDRIVE0`; `icon.ico` y `wall.jpg` en `C:\ProgramData`; `vssadmin` con el literal `norealvolume`; extensión `.anubis`; notas `restore files.*` |
| **Herramientas** | **Alto, con la advertencia de siempre** | `AnyDesk`, `Megasync`, `WinSCP`, `Filezilla`, `S3browser` y **cinco controladores firmados**: todo legítimo. El criterio es el contexto, no el binario. **Y los controladores no se bloquean por hash: se bloquean por lista de controladores vulnerables** |
| **TTP** | **El máximo, y hay tres que el adversario no puede abandonar** | **(1)** **Desactivar la defensa antes de cifrar**: es imprescindible y es su fase más ruidosa. **(2)** **Exfiltrar antes de cifrar**: es la única línea de negocio que le funciona en los dos casos documentados. **(3)** **Borrar las copias de sombra**: sin eso, la víctima restaura y no paga |

> **La consecuencia de inversión, y es la contraria a la de los otros
> informes de este lote.** Aquí **los hashes sí sirven** —hay catorce de
> primera mano, de una puerta trasera propia vista en tres organizaciones— y
> **el bloqueo es la detección**: lo que hay que instrumentar no es un
> indicador nuevo, es una **regla de correlación sobre bloqueos que ya se
> producen**.

## T-4. Hipótesis de caza prioritarias

| Id | Hipótesis | Dónde se busca | Qué confirma | Coste |
|---|---|---|---|---|
| **H-1** | Hubo **tres o más intentos bloqueados** de terminar servicios de seguridad o de cargar controladores en una ventana de dos horas, en un mismo equipo | Registros del agente de seguridad y de carga de controladores | **La señal de mayor valor del informe.** Es correlación sobre eventos que ya se registran | **Bajo, y es la primera** |
| **H-2** | Existe la clave `HKLM\SYSTEM\CurrentControlSet\Control\SafeBoot\Network\<herramienta de acceso remoto>` | Barrido de registro | **Acceso de reserva para el Modo seguro.** Clave muy específica, sin uso legítimo normal | **Trivial** |
| **H-3** | Alguno de los **catorce hashes** de `A.3` aparece en el parque o en los registros de doce meses | Inventario y registros de ejecución | **Puerta trasera propia o herramienta del conjunto.** Y la puerta trasera apareció en **redes sin cifrado**: puede ser el único indicio | **Trivial** |
| **H-4** | Hay un **servicio** cuyo nombre imita un componente de Chrome o un fichero de VMware, con conexiones a **dos** destinos por el 443 | Inventario de servicios, cruzado con registros de red | `Lindnor` | **Bajo** |
| **H-5** | Algún proceso que no es de disco ni de respaldo ha abierto **`\\.\PHYSICALDRIVE0`** | Registros de acceso a dispositivos | Comprobación de privilegios del cifrador | **Medio** |
| **H-6** | Hubo **volumen saliente sostenido y bajo** durante varios días hacia un destino de almacenamiento o sincronización, sin pico | Registros de flujo y de proxy, **agregados por día y por destino, no por sesión** | **El método declarado en el caso chileno.** Está diseñado para no disparar umbrales de volumen | **Medio, y es la que más rinde del grupo** |
| **H-7** | Hay **dos o más** herramientas distintas de exfiltración o sincronización instaladas en un mismo servidor | Inventario de software | Patrón documentado: cuatro en un solo ataque | **Bajo** |
| **H-8** | Se ejecutó `vssadmin` con el literal **`norealvolume`** | Línea de órdenes de procesos | Fase de impacto. **El literal es inusual y por tanto muy específico** | **Trivial** |
| **H-9** | Existen `icon.ico` o `wall.jpg` en `C:\ProgramData` sin origen conocido | Barrido de ficheros | Cifrador desplegado, haya cifrado o no | **Trivial** |
| **H-10** | Hay ficheros **listados a 0 KB** en masa en algún recurso compartido | Barrido de tamaños de fichero | **`/WIPEMODE`.** Sería el **primer caso documentado del mundo** | **Bajo, y de valor desproporcionado si acierta** |

> **Una nota sobre `H-6`, que es la hipótesis técnicamente más difícil y la
> más importante.** La exfiltración declarada en el caso chileno duró «casi
> una semana» **a baja velocidad**. Eso derrota a cualquier umbral de volumen
> por sesión o por hora, que es como está configurada la mayoría de las
> alertas de exfiltración. **La agregación correcta es por destino y por
> día, sostenida en el tiempo**, y es un cambio de consulta, no de
> herramienta. Si una organización sólo puede implantar una hipótesis de
> este informe además de `H-1`, es ésta.

## T-5. Brechas de visibilidad que hay que cerrar primero

| Brecha | Qué nos impide ver | Coste | Prioridad |
|---|---|---|---|
| **No se alerta sobre intentos BLOQUEADOS de desactivar la seguridad** | **La señal de mayor valor del informe** | **Bajo: una regla de correlación sobre eventos que ya se registran** | **1** |
| No se agrega el volumen saliente **por destino y por día** | La exfiltración lenta y sostenida, que es el daño real cuando el cifrado falla | Bajo: es un cambio de consulta | **2** |
| **No se sabe qué hay en cada repositorio interno de ficheros** | El alcance del daño de confidencialidad | **Alto, y no es técnico**: requiere a los dueños de la información | **3** |
| No hay control de **carga de controladores vulnerables** | La vía al núcleo que el adversario prefiere | Medio: hay listas de bloqueo de controladores mantenidas por el fabricante del sistema | **4** |
| No se vigila `SafeBoot\Network` | El acceso de reserva | **Trivial** | **5** |
| El procedimiento **no contempla «el cifrado falló y el incidente continúa»** | Que se cierre un incidente cuyo daño ya ocurrió | Bajo: una revisión de procedimiento | **6** |

---

# NIVEL TÉCNICO
### Para: Ingeniería de detección · Automatización · TIP/SIEM · Vida útil: meses

## X-1. Arsenal y capacidad

| Nombre | Qué es | Nota que importa |
|---|---|---|
| **Cifrador Anubis** | Carga de cifrado, `iservice.exe` en el caso de octubre de 2026 | **ECIES** sobre biblioteca pública en Go, similar a `EvilByte` y `Prince`. Parámetros `/KEY=`, `/elevated`, **`/WIPEMODE`**, **`/PFAD=`** *(alemán)*, `/PATH=`. **Pregunta al usuario si no tiene privilegios** |
| **`Backdoor.Lindnor`** | **Puerta trasera propia** | **Inusual**: «pocos operadores de *ransomware* construyen sus propias puertas traseras». Instalada **como servicio**, disfrazada de componente de Chrome o de fichero de VMware, en los **dos únicos servidores de base de datos** del conjunto. C2 primario y de reserva, los dos por el **443**. **Y apareció en dos organizaciones más SIN actividad de cifrado** |
| `safemode.exe` | Configurador de persistencia en Modo seguro | Registra `AnyDesk` como servicio permitido en **Modo seguro con funciones de red** |
| `gbbsym.exe` · `symgooq.exe` | Desactivadores de seguridad | **Se hacen pasar por software de Symantec.** Aceptan `-l` para listar las retrollamadas del núcleo registradas por un controlador vulnerable cargado, y `-d` para **listarlas y eliminarlas**. Se observó `-d` |
| Once ejecutables más, y **cinco controladores firmados y vulnerables** | BYOVD | `bdr.exe`, `hwaudioch.exe`, `gibformin.exe`, `gibfor.exe`, `test.exe`, `xs.scr`, y los dos **no bloqueados**: `huntreagent.exe` y `s1.exe`, del **mismo tamaño y distinto hash** — dos compilaciones de la misma herramienta |
| `AnyDesk` · `Megasync` · `WinSCP` · `Filezilla` · `S3browser` | **Herramientas legítimas** | Acceso remoto y exfiltración. **Cuatro de exfiltración en un solo ataque**, lo que su analista califica de inusual |

### X-1.1 — Lo que no hay, y lo que sí

**Lo que no hay, y acota la capacidad:**

1. **No hay criptografía propia.** El cifrado usa una biblioteca **pública** de ECIES en Go. Y conviene no confundir el dato: compartirla con `EvilByte` y `Prince` **no indica relación** entre las familias, porque está disponible para cualquiera. Es el mismo error que atribuir por un par de carga lateral popular, documentado en `CTI-2026-043`.
2. **No hay sigilo en la fase de evasión.** Trece ejecutables en una hora es ruido, no finura.
3. **No hay control de calidad maduro.** El cifrador **pregunta al usuario** si no tiene privilegios, y **falla** al poner el fondo de escritorio porque el fichero no se deposita. Las dos cosas las documenta su analista con capturas.
4. **Y, en los dos casos documentados con detalle, no hay cifrado consumado.**

**Lo que sí hay, y es lo que no encaja con lo anterior:**

**Una puerta trasera propia, instalada como servicio, con nombre mimético, par de C2 primario y de reserva, y presencia en tres organizaciones distintas.** Su analista lo señala expresamente como inusual entre operadores de extorsión, que «generalmente dependen de herramientas públicas, de doble uso y del propio sistema». **La capacidad de este grupo es desigual**: artesanal en el desarrollo de la puerta trasera y tosca en la ejecución del cifrado. Es la lectura de `H-F` en `O-6`, y es más precisa que decir que es capaz o que no lo es.

## X-2. Artefactos de anfitrión persistentes

| Artefacto | Dónde | Confianza |
|---|---|---|
| `HKLM\SYSTEM\CurrentControlSet\Control\SafeBoot\Network\AnyDesk` *(o cualquier herramienta de acceso remoto)* con valor `Service` | Registro | **Alta.** Sin uso legítimo normal |
| Servicio con nombre que imita un componente de Chrome o un fichero de VMware, con binario `healthcontroller64.exe` o `svchelper.exe` | Servicios | **Alta** |
| `icon.ico` y `wall.jpg` en `C:\ProgramData` | Sistema de ficheros | **Alta.** Se depositan aunque el cifrado no se complete |
| Extensión **`.anubis`**; notas `restore files.txt` y `restore files.html`; *(variante anterior)* `RESTORE FILES.html` | Sistema de ficheros | Alta |
| Iconos de fichero cambiados por el logotipo del grupo | Interfaz | Alta |
| Apertura de **`\\.\PHYSICALDRIVE0`** por un proceso que no es de disco ni de respaldo | Acceso a dispositivos | Media-alta |
| Ficheros **listados con tamaño 0 KB** en masa | Sistema de ficheros | **Alta, y sería el primer caso documentado de `/WIPEMODE`** |
| Cuenta local nueva añadida a un grupo local, junto a `AnyDesk` | Cuentas | Media-alta en combinación |

## X-3. Lógica de detección prioritaria

### X-3.1 — `D-1` · Los catorce hashes, que aquí sí sirven

```
BLOQUEAR / DETECTAR los catorce hashes de A.3, y en particular las
TRES variantes de Backdoor.Lindnor.

Razon por la que en este informe los hashes rinden mas de lo habitual:
 - una puerta trasera PROPIA se recompila menos que un cifrador de
   afiliados
 - y esta aparecio en TRES organizaciones distintas, dos de ellas SIN
   actividad de cifrado: puede ser el UNICO indicio de un compromiso
   en curso que todavia no ha llegado a la fase de impacto
```

### X-3.2 — `D-2` · Acumulación de intentos BLOQUEADOS · **la detección de este informe**

```
EVENTO: intento BLOQUEADO de
        - terminar un servicio o proceso de seguridad
        - cargar un controlador conocido como vulnerable
        - desinstalar o alterar el agente de proteccion
CONDICION: TRES O MAS de estos eventos, en el MISMO equipo, en una
        ventana de DOS HORAS
ENTONCES INCIDENTE CON PRIORIDAD MAXIMA

Por que funciona, y es el hallazgo del informe:
 - en el caso documentado el adversario desplego TRECE ejecutables en
   aproximadamente una hora, y DOCE fueron bloqueados
 - su analista describe el patron como "probar una herramienta tras
   otra hasta encontrar algo que funcione": es fuerza bruta de evasion,
   y una fuerza bruta es ruidosa por definicion
 - doce bloqueos consecutivos en sesenta minutos NO es un falso
   positivo

Y la razon por la que casi nadie tiene esta regla: la mayoria de las
organizaciones alerta sobre lo que PASO, no sobre lo que se INTENTO y
se bloqueo. En este patron, EL BLOQUEO ES LA ALERTA.

Coste: una regla de correlacion sobre eventos que ya se registran.
No hace falta ningun sensor nuevo.
```

### X-3.3 — `D-3` · Persistencia en Modo seguro

```
EVENTO: creacion o modificacion de una clave bajo
   HKLM\SYSTEM\CurrentControlSet\Control\SafeBoot\Network\*
     o  ...\Control\SafeBoot\Minimal\*
ENTONCES alertar SIEMPRE

El software de seguridad no opera plenamente en Modo seguro, y por eso
el adversario se registra ahi: para disponer de una ventana en la que
usar los controladores vulnerables sin oposicion.

Casos legitimos: muy pocos y conocidos (algunas herramientas de
respaldo y de recuperacion). Se catalogan una vez y se excluyen.
```

### X-3.4 — `D-4` · La puerta trasera

```
EVENTO: servicio nuevo cuyo binario esta en una carpeta que imita
        un directorio de componentes de Chrome o de VMware
Y       el proceso establece conexiones a DOS destinos distintos por
        el puerto 443
Y       envia en su primer intercambio: nombre de equipo, nombre de
        usuario, dominio y servidor de inicio de sesion
ENTONCES incidente

Nota de alcance: esta puerta trasera se encontro tambien en DOS
organizaciones donde NO hubo actividad de cifrado. Es decir: su
presencia no implica extorsion inminente, pero si un compromiso que
nadie habia visto.
```

### X-3.5 — `D-5` · Preparación del impacto

```
CUALQUIERA de:
 - vssadmin ... delete shadows ... /for=norealvolume
   (el literal "norealvolume" es inusual y por tanto muy especifico)
 - creacion de C:\ProgramData\icon.ico junto a C:\ProgramData\wall.jpg
 - un proceso que abre \\.\PHYSICALDRIVE0 sin ser de disco ni respaldo
 - una consola interactiva que muestra
   "No admin privileges. Start process anyway?"
ENTONCES incidente

El ultimo es el mas insolito y el mas util: un cifrador que ABRE UNA
CONSOLA Y ESPERA ENTRADA DEL USUARIO es visible, y en un servidor sin
sesion interactiva SE QUEDA ESPERANDO.
```

### X-3.6 — `D-6` · Exfiltración lenta y sostenida

```
AGREGACION CORRECTA (y es el punto de la regla):
   volumen saliente por DESTINO y por DIA, sostenido varios dias
   — NO por sesion y NO por hora

EVENTO: un mismo equipo o servidor envia a un mismo destino externo
        un volumen moderado pero PERSISTENTE durante >= 3 dias
Y       el destino es de almacenamiento, sincronizacion o transferencia
ENTONCES investigar

Por que: el metodo declarado en el caso chileno fue "casi una semana"
subiendo datos "a baja velocidad" por puertas traseras. Esta
construido para derrotar los umbrales por sesion y por hora, que es
como esta configurada la mayoria de las alertas de exfiltracion.
```

## X-4. Consultas de caza

```kql
// =====================================================================
// H-1 y D-2 · LA CONSULTA DE ESTE INFORME: acumulacion de intentos
// BLOQUEADOS de desactivar la seguridad.
//
// No busca un indicador nuevo: correlaciona bloqueos que ya se
// registran. Doce bloqueos consecutivos en una hora no son un falso
// positivo, son un adversario probando herramienta tras herramienta.
// =====================================================================

let ventana = 2h;
let umbral  = 3;
let eventos_evasion =
    union
      ( AlertEvidence
        | where Timestamp > ago(90d)
        | where Title has_any ("tamper", "defense evasion",
                               "security service", "vulnerable driver",
                               "disable", "terminate")
        | project Timestamp, DeviceName, Senal = Title, Accion = "alerta" ),
      ( DeviceEvents
        | where Timestamp > ago(90d)
        | where ActionType in~ ("DriverLoad", "TamperingAttempt",
                                "AntivirusDetection", "ExploitGuardBlocked")
        | project Timestamp, DeviceName, Senal = ActionType, Accion = ActionType ),
      ( DeviceProcessEvents
        | where Timestamp > ago(90d)
        | where ProcessCommandLine has_any ("-d", "--delete-callbacks")
             and FileName endswith ".exe"
        | project Timestamp, DeviceName, Senal = FileName, Accion = "cmdline" );
eventos_evasion
| summarize intentos = count(),
            senales  = make_set(Senal, 20),
            inicio   = min(Timestamp),
            fin      = max(Timestamp)
        by DeviceName, bin(Timestamp, ventana)
| where intentos >= umbral
| extend duracion_min = datetime_diff('minute', fin, inicio)
| project DeviceName, inicio, fin, duracion_min, intentos, senales
| order by intentos desc

// Afinado: cuanto MAS CORTA sea la duracion para el mismo numero de
// intentos, mas sospechoso. Trece en sesenta minutos es el patron
// documentado.
```

```kql
// =====================================================================
// H-2 y D-3 · Persistencia en Modo seguro. Clave muy especifica, y
// trivial de consultar.
// =====================================================================

DeviceRegistryEvents
| where Timestamp > ago(365d)
| where RegistryKey has @"Control\SafeBoot\"
| where ActionType in~ ("RegistryKeyCreated", "RegistryValueSet")
| project Timestamp, DeviceName, ActionType, RegistryKey,
          RegistryValueName, RegistryValueData,
          InitiatingProcessFileName, InitiatingProcessCommandLine
| order by Timestamp desc

// Casos legitimos conocidos: algunas herramientas de respaldo y de
// recuperacion. Se catalogan UNA VEZ y se excluyen por nombre.
```

```kql
// =====================================================================
// H-3 y D-1 · Los catorce hashes de primera mano. En este expediente
// los hashes rinden: la puerta trasera es PROPIA y aparecio en tres
// organizaciones, dos de ellas SIN cifrado.
// =====================================================================

let indicadores = dynamic([
  // Backdoor.Lindnor (tres variantes)
  "fc200686175559f4544a5de826905f09a68476d889690a3be40ac32356790cb8",
  "5d2dd9caf2ae4a5083dbec16e688040456cdbc31eaeecbab78188e322ed0415b",
  "ad9575a9ef2dcc9d2fd2a24376c418549d4b3db5564c22b20081d33cf7629e43",
  // Cifrador Anubis
  "e69b882218fa2a19fd351741874bfcd10a6ae91076e6a8483795e0e357f8d026",
  // AnyDesk y el configurador de Modo seguro
  "467d1395b61d4b886329571b564fb21db01639acd2799439646c85b9aeaec175",
  "47a864736764112d7897c76e56d51111ce75b3e46fdbac6933df8a5b29507d17",
  // Desactivadores de seguridad
  "6543ee9f89d80b2bcf08e98fb8e9e73a4b144a93c7b2a3f28e35de8f7e7a8a80",
  "83eff3e51b69968a4ddd503b0b1dccfa8829d638f2dc00cc69640a29aea814f1",
  "f8d4142a94269b4258f370ef2292d22a49cd6dee8266a7122f4531e9cc5d9a2f",
  "cd1e68583b8b984a9bb5b9f7067077c0e0d8f79da4455c326319e5e5fc6e9c5f",
  "5a2082162852984ffe7e7c501faa6cf473129fcba29406ffb98d55198de4b3a5",
  "5fcd2c954764ac0888c8ba72fc1cf54db64e8f23f83aeb0786ae5b80438ba926",
  "aa779d811e00a30dfb56b994bdd63424cbf97617af737a218b6aff9f7c3a50f5"
]);
union DeviceFileEvents, DeviceProcessEvents, DeviceImageLoadEvents
| where Timestamp > ago(365d)
| where SHA256 in~ (indicadores)
| project Timestamp, DeviceName, FileName, FolderPath, SHA256,
          InitiatingProcessFileName, InitiatingProcessCommandLine
```

```sql
-- =====================================================================
-- H-6 y D-6 · Exfiltracion LENTA y SOSTENIDA.
--
-- La clave de esta consulta no es el umbral: es la AGREGACION. Por
-- destino y por DIA, sostenida varios dias — no por sesion ni por hora,
-- que es como esta configurada la mayoria de las alertas y es
-- exactamente lo que el metodo declarado en el caso chileno derrota.
-- =====================================================================

WITH diario AS (
  SELECT ip_origen,
         ip_destino,
         DATE(fecha)        AS dia,
         SUM(bytes_enviados) AS bytes_dia,
         COUNT(*)            AS sesiones
  FROM flujos
  WHERE direccion = 'saliente'
    AND fecha > NOW() - INTERVAL '90 days'
  GROUP BY ip_origen, ip_destino, DATE(fecha)
),
sostenido AS (
  SELECT ip_origen,
         ip_destino,
         COUNT(DISTINCT dia)  AS dias_con_trafico,
         SUM(bytes_dia)       AS bytes_total,
         AVG(bytes_dia)       AS bytes_dia_medio,
         MAX(bytes_dia)       AS bytes_dia_max
  FROM diario
  GROUP BY ip_origen, ip_destino
)
SELECT *
FROM sostenido
WHERE dias_con_trafico >= 3                  -- persistencia
  AND bytes_total      >  5  * 1024*1024*1024 -- 5 GB acumulados
  AND bytes_dia_max    <  50 * 1024*1024*1024 -- sin pico: NO es un volcado
ORDER BY bytes_total DESC;

-- La tercera condicion es la que importa y es contraintuitiva: se
-- EXCLUYEN los picos. Un volcado de una vez ya lo detectan los
-- umbrales existentes; lo que esta consulta busca es lo que ELLOS NO
-- VEN — mucho volumen repartido en muchos dias sin que ningun dia
-- destaque.
```

## X-5. Mitigaciones de configuración con efecto directo

Cinco. **Ninguna exige comprar un producto de seguridad.**

### X-5.1 — Alertar sobre intentos bloqueados · **la de mayor rendimiento**

Desarrollada en `E-4` y `X-3.2`. **Es la única medida de este informe que convierte un control que ya existe en una detección que no existía**, y cuesta una regla de correlación sobre eventos que ya se registran. Tres o más intentos bloqueados de desactivar la seguridad en un mismo equipo en dos horas es un incidente, no ruido.

### X-5.2 — Protección contra alteración, y control de controladores vulnerables

Dos piezas, y la segunda es la que falta en más sitios:

1. **Protección contra alteración** activa en el agente de seguridad, con contraseña o vale para desinstalar. Es lo que resistió en el caso de octubre de 2026.
2. **Bloqueo de carga de controladores vulnerables conocidos**, con la lista que mantiene el fabricante del sistema operativo. El adversario desplegó **cinco controladores firmados**: la firma es válida, de modo que **un control basado en reputación de firma no ve nada**. La defensa es una lista de controladores vulnerables, no una de confianza.

### X-5.3 — Cerrar el Modo seguro como vía de persistencia

Vigilar `SafeBoot\Network` y `SafeBoot\Minimal` (`D-3`), y **catalogar de una vez las herramientas legítimas** que necesitan estar ahí, que son pocas y conocidas. Es una clave de registro con un uso legítimo muy acotado y un uso ofensivo muy claro.

### X-5.4 — Copias inmutables, y fuera del alcance de la red

Tres requisitos, y el tercero es el que este expediente añade frente a `CTI-2026-040`:

1. **Copias no alcanzables desde un recurso compartido de red.**
2. **Copias inmutables o fuera de línea**, porque el borrado de copias de sombra es la primera acción de impacto.
3. **Y copias cuya existencia sea la premisa de la negociación y no su alternativa.** Frente a un adversario que puede invocar `/WIPEMODE`, **pagar no compra recuperación** (`E-2`). La copia inmutable deja de ser el plan B y pasa a ser **el único instrumento que la víctima tiene**.

### X-5.5 — Revisar el acceso remoto, y la agregación de las alertas de exfiltración

Dos cosas que no suelen ir juntas y que este expediente une:

1. **El acceso remoto parcheado y con autenticación resistente**, porque es el vector declarado del caso chileno y porque hay indicios de explotación de una vulnerabilidad conocida de Citrix en el mismo periodo.
2. **Y la agregación de las alertas de exfiltración cambiada a destino-día sostenido** (`D-6`). Es un cambio de consulta, no de herramienta, y es lo que permite ver una exfiltración de una semana a baja velocidad — que es el daño real cuando el cifrado falla.

> ⚠ **Y la mitigación que este informe NO recomienda: bloquear por hash los
> cinco controladores vulnerables.** Son **controladores firmados y
> legítimos**, de fabricantes reales, y algunos están en uso en parques
> reales. La defensa correcta es la **lista de controladores vulnerables** del
> fabricante del sistema operativo, que los bloquea por vulnerabilidad y no
> por reputación — precisamente porque su firma es válida. Igual que las
> cinco herramientas legítimas de `A.6`: el criterio es el contexto, no el
> binario.

---

## 14. Brechas de inteligencia y nuevos requisitos de colección

| Id | Brecha | Por qué importa | Cómo se cierra | Coste |
|---|---|---|---|---|
| `G-1` | **No existe un informe independiente del incidente chileno** | Es la limitación central: el volumen, la vía de entrada, la duración y el rescate **los dice el atacante** | Informe de la compañía o de la autoridad chilena, si se publica. **Y la autoridad fue notificada** | Medio, y fuera de nuestro control |
| `G-2` | **No hay ningún uso documentado de `/WIPEMODE` contra una víctima real** | Decide si este actor es «el que puede borrar» o «el que borra» | Vigilancia. `H-10` es la consulta que lo detectaría en el propio entorno | **Bajo, y de valor desproporcionado** |
| `G-3` | No conocemos las direcciones del par de mando y control de la puerta trasera | Symantec publica los hashes pero no las direcciones | Solicitud al autor del análisis | Bajo |
| `G-4` | No sabemos si hay más víctimas latinoamericanas | `H-E` de `O-6` | Consulta a CSIRT nacionales y al foro regional; y seguimiento del sitio de fugas | Medio |
| `G-5` | **No sabemos si nuestras alertas cubren intentos bloqueados** | Es la medida de mayor rendimiento del informe | **Una pregunta al SOC** | **Trivial, y es la prioridad 1** |
| `G-6` | No sabemos cómo está agregada nuestra alerta de exfiltración | Decide si veríamos una exfiltración lenta de una semana | Una consulta a quien la configuró | **Trivial** |
| `G-7` | **No sabemos qué hay en cada repositorio interno de ficheros** | Si el cifrado falla, el daño es de confidencialidad y el alcance lo determina el contenido | Inventario con los dueños de la información | **Alto, y no es técnico** |
| `G-8` | No se verificó la cifra de trece organizaciones chilenas atacadas en el primer trimestre de 2026 | Es contexto, no dato del actor, y **ningún juicio descansa en ella** | Recuento propio sobre sitios de fugas | Bajo, y de valor bajo |
| `G-9` | No sabemos si `/PFAD=` aparece en otras muestras o familias | `KJ-9`. Y con tres casos de idioma en este lote, **lo que hace falta no es un cuarto: es saber si el patrón vale algo** | Búsqueda en repositorios de muestras | Bajo |

**Disparadores de reevaluación.** `I-1`: **primer uso documentado de `/WIPEMODE`** contra una víctima real, que cambiaría `KJ-3` de capacidad a conducta. `I-2`: publicación de un informe independiente del incidente chileno, que permitiría contrastar las afirmaciones del atacante y **cerrar la cuestión central del `Anexo D`**. `I-3`: una tercera víctima latinoamericana. `I-4`: aparición de `/PFAD=` o de otro artefacto de idioma en una familia no relacionada, que ayudaría a calibrar cuánto vale esta clase de observación. `I-5`: detenciones. `I-6`: aparición de una lista de exclusión declarada por este grupo, que hoy no tiene. `I-7`: un caso en que el cifrado de este actor **sí** se ejecute por completo, que matizaría `KJ-4` y `H-F`.

---

# ANEXOS

## Anexo A — Indicadores de compromiso

> ⚠ **`PAP:AMBER` — cinco advertencias, y dos son de clase distinta a las
> habituales.** (1) **`A.6` contiene cinco controladores firmados y
> vulnerables, y cinco herramientas legítimas** —`AnyDesk`, `Megasync`,
> `WinSCP`, `Filezilla`, `S3browser`—, con tipo `herramienta` para que **no
> entren en los agregados planos**. Los controladores **no se bloquean por
> hash**: su firma es válida y están en uso en parques reales; se bloquean con
> la lista de controladores vulnerables del fabricante del sistema. (2)
> **`A.7` no contiene ningún dato personal de las personas expuestas en el
> caso chileno**, y la decisión se explica ahí. (3) En este informe **los
> hashes sí rinden**, lo que es inusual en esta cartera: `A.3` trae catorce de
> primera mano, y las tres variantes de la puerta trasera propia aparecieron
> en **tres organizaciones**, dos de ellas **sin cifrado**. (4) **El
> indicador de mayor valor no es ingerible**: es la regla de correlación de
> `A.1`, que opera sobre bloqueos que ya se registran. (5) **Hay cuatro cosas
> llamadas «Anubis»** y una ingesta por nombre de familia mezcla material de
> cuatro expedientes: véase `O-1.2`.

### A.1 — La señal que decide, y es una correlación · **leer primero**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| pattern | **Tres o más intentos BLOQUEADOS de desactivar la seguridad en un mismo equipo en una ventana de dos horas** —terminación de servicios o procesos de seguridad, carga de controladores vulnerables conocidos, o desinstalación del agente— | **El indicador de mayor valor del informe, y no es un valor: es una correlación.** En el ataque documentado, los operadores desplegaron **trece ejecutables en aproximadamente una hora** y **doce fueron bloqueados**. Su analista describe el patrón como «probar una herramienta tras otra hasta encontrar algo que funcione»: es **fuerza bruta de evasión**, y una fuerza bruta es ruidosa por definición. **Doce bloqueos consecutivos en sesenta minutos no es un falso positivo.** Y la razón por la que casi nadie tiene esta regla es que **la mayoría de las organizaciones alerta sobre lo que pasó, no sobre lo que se intentó y se bloqueó** | **Alta** | **Sin caducidad.** La fase es imprescindible para el adversario y su ruido es estructural | **Detección con prioridad máxima** (`D-2`). **Cuesta una regla de correlación sobre eventos que ya se registran**: no hace falta ningún sensor nuevo |
| pattern | `HKLM\SYSTEM\CurrentControlSet\Control\SafeBoot\Network\<herramienta de acceso remoto>` con valor `Service`, o cualquier clave nueva bajo `SafeBoot\Network` o `SafeBoot\Minimal` | **Acceso de reserva para el Modo seguro**, donde el software de seguridad no opera plenamente: es la ventana en la que el adversario piensa usar sus controladores vulnerables sin oposición. La orden observada es `reg add HKLM\SYSTEM\CurrentControlSet\Control\SafeBoot\Network\AnyDesk /ve /t REG_SZ /d Service /f`. **Clave con uso legítimo muy acotado** —algunas herramientas de respaldo y recuperación— que se cataloga una vez y se excluye | **Alta** | Sin caducidad | **Detección** (`D-3`) |
| pattern | **Volumen saliente moderado pero sostenido durante tres o más días** hacia un mismo destino de almacenamiento, sincronización o transferencia, **sin ningún pico** | **El método de exfiltración declarado por el atacante en el caso chileno**: «casi una semana» subiendo datos «a baja velocidad» por puertas traseras instaladas al efecto. Está construido para derrotar los umbrales por sesión y por hora, que es como está configurada la mayoría de las alertas. **La agregación correcta es por destino y por día**, y es un cambio de consulta, no de herramienta | Media-alta | Sin caducidad como método | **Caza** (`D-6`, `H-6`). **Y la condición contraintuitiva de la regla es excluir los picos**: los picos ya los detectan los umbrales existentes |

### A.2 — Artefactos de anfitrión

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| filepath | `C:\ProgramData\icon.ico` · `C:\ProgramData\wall.jpg` | El cifrador los extrae de sí mismo. **Se depositan aunque el cifrado no se complete**, lo que los hace útiles en los casos —los dos documentados— en que el cifrado falla. Dato curioso y revelador: en la prueba de laboratorio **`wall.jpg` no se depositó** y el intento de cambiar el fondo de escritorio falló | Alta | Sin caducidad | **Detección** (`D-5`, `H-9`) |
| filename | Extensión **`.anubis`** · notas **`restore files.txt`** y **`restore files.html`** · *(variante anterior)* `RESTORE FILES.html` firmada por el «ANUBIS team» | Cifrado consumado o intentado | Alta | Sin caducidad | **Confirmación.** Y **ejecutar el procedimiento de `E-3`**: el cifrado puede haber fallado y el incidente seguir |
| pattern | `vssadmin ... delete shadows ... /for=norealvolume /all /quiet` | Borrado de copias de sombra. **El literal `norealvolume` es inusual y por tanto muy específico**: es el valor que el cifrador pasa, y buscarlo tal cual rinde más que buscar `vssadmin` | **Alta** | Sin caducidad | **Detección** (`D-5`, `H-8`) |
| pattern | Apertura del dispositivo **`\\.\PHYSICALDRIVE0`** por un proceso que no es de disco, de respaldo ni de cifrado de volumen | Comprobación de privilegios del cifrador: es una operación de bajo nivel que requiere permisos elevados, y el cifrador la usa para saber si los tiene | Media-alta | Sin caducidad | **Detección** (`D-5`, `H-5`) |
| pattern | Una **consola interactiva** que muestra `Admin privileges detected. Attempting to elevate to SYSTEM...` o `No admin privileges. Start process anyway?` **y espera entrada del usuario** | **El artefacto más insólito del expediente, y el más útil.** Un cifrador que abre una consola y espera una respuesta **es visible**, y en un servidor sin sesión interactiva **se queda esperando**. Su analista lo lee como señal de que el programa «sigue mejorándose y en desarrollo» | **Alta** | **Caducidad previsible**: es un defecto que el adversario corregirá | **Detección** (`D-5`) |
| pattern | Ficheros **listados en el directorio con tamaño 0 KB**, en masa | **`/WIPEMODE` consumado.** En la prueba de laboratorio los ficheros siguen apareciendo pero su contenido está vaciado, **sin recuperación posible**. **No hay ningún caso documentado contra una víctima real**: si alguien lo encuentra, sería el primero | **Alta como firma; sin casos reales** | Sin caducidad | **Detección** (`H-10`), **y comunicarlo**: cerraría `G-2` para toda la comunidad |
| pattern | Servicio nuevo cuyo binario está en una carpeta que imita un **directorio de componentes de Chrome** o una **carpeta de VMware**, con nombre `healthcontroller64.exe` o `svchelper.exe`, estableciendo conexiones a **dos** destinos por el **443** | **La puerta trasera propia.** Envía en su primer intercambio identificador de proceso, versión del sistema, su propia ruta, nombre de equipo, nombre de usuario, dominio y servidor de inicio de sesión. **Apareció también en dos organizaciones SIN actividad de cifrado**: su presencia no implica extorsión inminente, pero sí un compromiso que nadie había visto | **Alta** | Sin caducidad | **Detección** (`D-4`, `H-4`) |
| pattern | Dos ejecutables que **se hacen pasar por software de Symantec** y aceptan `-l` para **listar las retrollamadas del núcleo** registradas por un controlador vulnerable cargado, y `-d` para **listarlas y eliminarlas** | Desactivación de la defensa desde el núcleo. **Se observó el uso de `-d`.** Los nombres documentados son `gbbsym.exe` y `symgooq.exe`, pero **lo estable es la funcionalidad, no el nombre** | Alta | Sin caducidad como patrón | **Detección** |

### A.3 — Muestras · **catorce hashes de primera mano, y aquí sí rinden**

> **Por qué este anexo es distinto al de los otros informes de este lote.**
> Son catorce resúmenes criptográficos publicados por Symantec a partir de un
> ataque de octubre de 2026, y **tres de ellos corresponden a una puerta
> trasera propia del grupo**. Una puerta trasera propia se recompila menos
> que un cifrador de afiliados, y **ésta apareció en tres organizaciones
> distintas, dos de ellas sin actividad de cifrado alguna**. Es decir: para
> esas dos, el hash fue el único indicio.

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| sha256 | `fc200686175559f4544a5de826905f09a68476d889690a3be40ac32356790cb8` | **`Backdoor.Lindnor`** — `healthcontroller64.exe` y `svchelper.exe` | Alta | 2027-05-19 | **Bloqueo** |
| sha256 | `5d2dd9caf2ae4a5083dbec16e688040456cdbc31eaeecbab78188e322ed0415b` | **`Backdoor.Lindnor`** — `powerhost.exe` y `eventwatcher.exe` | Alta | 2027-05-19 | **Bloqueo** |
| sha256 | `ad9575a9ef2dcc9d2fd2a24376c418549d4b3db5564c22b20081d33cf7629e43` | **`Backdoor.Lindnor`** — `volumeproxy.exe` | Alta | 2027-05-19 | **Bloqueo** |
| sha256 | `e69b882218fa2a19fd351741874bfcd10a6ae91076e6a8483795e0e357f8d026` | **Cifrador Anubis** — `iservice.exe`. **Fue bloqueado antes de ejecutarse** en el caso documentado | Alta | 2027-05-19 | **Bloqueo** |
| sha256 | `47a864736764112d7897c76e56d51111ce75b3e46fdbac6933df8a5b29507d17` | **`safemode.exe`** — configura `AnyDesk` para seguir operando en Modo seguro. **Es la herramienta, no la clave**: la clave está en `A.1` | Alta | 2027-05-19 | **Bloqueo** |
| sha256 | `aa779d811e00a30dfb56b994bdd63424cbf97617af737a218b6aff9f7c3a50f5` | `gbbsym.exe` — **desactivador que se hace pasar por software de Symantec** | Alta | 2027-05-19 | **Bloqueo** |
| sha256 | `6543ee9f89d80b2bcf08e98fb8e9e73a4b144a93c7b2a3f28e35de8f7e7a8a80` · `83eff3e51b69968a4ddd503b0b1dccfa8829d638f2dc00cc69640a29aea814f1` · `f8d4142a94269b4258f370ef2292d22a49cd6dee8266a7122f4531e9cc5d9a2f` · `5fcd2c954764ac0888c8ba72fc1cf54db64e8f23f83aeb0786ae5b80438ba926` | `bdr.exe` · `hwaudioch.exe` · `gibformin.exe` · `gibfor.exe` — cuatro de los trece desactivadores de seguridad | Alta | 2027-05-19 | **Bloqueo** |
| sha256 | `cd1e68583b8b984a9bb5b9f7067077c0e0d8f79da4455c326319e5e5fc6e9c5f` · `5a2082162852984ffe7e7c501faa6cf473129fcba29406ffb98d55198de4b3a5` | `test.exe` · `xs.scr` — dos más del conjunto. **`xs.scr` con extensión de salvapantallas es un enmascaramiento clásico** | Alta | 2027-05-19 | **Bloqueo** |
| sha256 | `467d1395b61d4b886329571b564fb21db01639acd2799439646c85b9aeaec175` | `anydesk.exe` — **la muestra concreta usada, no el producto.** `AnyDesk` es software legítimo: véase `A.6` | Alta para la muestra; **el producto no es malicioso** | 2027-05-19 | **Detección con verificación.** No bloquear `AnyDesk` como producto |
| pattern | `huntreagent.exe` · `s1.exe` | **Los dos únicos ejecutables que NO fueron bloqueados**, y no estaban disponibles para análisis: su propósito exacto se desconoce. **Mismo tamaño y distinto resumen**, lo que sugiere **dos compilaciones de la misma herramienta** — probablemente para lanzar uno o varios de los controladores vulnerables | Media | Sin caducidad como nombres | **Caza por nombre y por el patrón de dos compilaciones** |

### A.4 — Parámetros del cifrador

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| pattern | `/KEY=` | Clave de cifrado | Alta | Sin caducidad | **Detección de la línea de órdenes** |
| pattern | `/elevated` | Relanzamiento con privilegios elevados tras obtenerlos | Alta | Sin caducidad | **Detección** |
| pattern | **`/WIPEMODE`** | **El parámetro que distingue a este actor.** Vacía el contenido de los ficheros en lugar de cifrarlos. **Su presencia en una línea de órdenes capturada sería el primer caso documentado de uso real** | **Alta** | Sin caducidad | **Detección con prioridad máxima** |
| pattern | **`/PFAD=`** | Directorios a excluir. **Está en ALEMÁN** —*Pfad*— y conviene verlo junto al siguiente, que está en inglés. Es `KJ-9` y material de `A.7` | Alta | Sin caducidad | **Detección**, y **contexto de atribución, no atribución** |
| pattern | `/PATH=` | Rutas concretas a cifrar | Alta | Sin caducidad | **Detección** |
| pattern | Carpetas excluidas del cifrado: `windows`, `system32`, `programdata`, `program files`, `program files (x86)`, `AppData`, `public`, `system volume information`, `efi`, `boot`, `perflogs`, `microsoft`, `intel`, **`.dotnet`, `.gradle`, `.nuget`, `.vscode`, `msys64`** | **Las cinco últimas son las reveladoras**: excluir los cachés de herramientas de desarrollo **no protege el sistema, protege la velocidad** —son directorios con decenas de miles de ficheros pequeños— y sugiere que el autor tropezó con ese problema **probando su cifrador en una máquina de desarrollo**. Es material de perfilado, y además sirve para identificar el cifrador por su comportamiento de recorrido | Alta | Sin caducidad | **Contexto, y firma de comportamiento** |

### A.5 — El caso chileno · **lo que afirma cada parte, separado**

> **Esta tabla es la aplicación del `Anexo D`, y su propósito es que ningún
> consumidor cite una afirmación del atacante como si fuera un dato del
> incidente.** Cada fila lleva **quién lo dice**.

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| cartera | **Publicación de Empresas Copec S.A. en el sitio de fugas de Anubis, enero de 2026** | **Hecho observable por terceros**, con capturas en la cobertura. Las fuentes difieren entre el **9** y el **14 de enero**, y el día no cambia ningún juicio | **Alta** | No caduca | **Citable como hecho** |
| cartera | **Comunicado de Copec**: «acceso no autorizado a un sistema de almacenamiento de información de uso interno»; los sistemas que administran **datos personales de clientes**, claves e información para operar plataformas digitales **no se vieron comprometidos**; **la operación no se vio afectada**; **autoridades notificadas** | **Declaración de la víctima.** Cubre **disponibilidad** y **datos de clientes**; **no menciona los datos de empleados**, que son los que se publicaron. Las cinco afirmaciones son compatibles con todo lo que dice el atacante (`E-1`) | **Alta como declaración** | No caduca | **Citable como declaración de la víctima, no como alcance verificado** |
| cartera | **«Aproximadamente 6 TB» exfiltrados** | **Afirmación del atacante**, en su sitio de fugas. **Es la métrica que un extorsionador tiene más incentivo a inflar**, porque fija el precio y la credibilidad de la amenaza. **Parcialmente verificable**, porque publicó el listado completo con buscador — lo que la hace costosa de inventar | **Media; es afirmación del adversario** | No caduca | **Citable SÓLO con atribución al atacante** |
| cartera | **Acceso inicial por la red privada virtual corporativa** | **Afirmación del atacante**, en una entrevista. Cae en la categoría más creíble de su relato: **un atacante no gana nada mintiendo sobre el producto por el que entró**. Pero **sí** gana presentando su entrada como técnica en lugar de como un descuido de la víctima | **Media-alta; es afirmación del adversario** | No caduca | **Citable con atribución.** Y es la base de `X-5.5` |
| cartera | **«Casi una semana» de exfiltración, a baja velocidad, por puertas traseras instaladas al efecto** | **Afirmación del atacante**, en respuesta a una pregunta directa sobre cuánto tardó. **Es la afirmación más útil de todo su relato para el defensor**, y la que menos incentivo tiene para inflar o reducir: es la base de `D-6` | **Media-alta; es afirmación del adversario** | Sin caducidad como método | **Base de la detección de `D-6`** |
| cartera | **«La defensa de Copec logró mitigar el ataque de *ransomware* en su extensa red, pero no pudo evitar la exfiltración»** | **Afirmación del atacante que le resta mérito**, y por eso es de las más creíbles de su relato: **concuerda además con el comunicado de la víctima** —la operación no se vio afectada— y con el caso de octubre de 2026, donde el cifrador fue bloqueado. Es `KJ-4` y `KJ-5` | **Media-alta, con corroboración indirecta** | No caduca | **Citable con atribución** |
| cartera | Rescate negociado **en cientos de miles de dólares (en torno a 400.000, según algunas fuentes)**, y la compañía **decidió no pagar** | **Afirmación del atacante, con la cifra recogida por terceros.** Otra fuente menciona seis millones. **La discrepancia es el dato**: dos cifras incompatibles atribuidas al mismo actor sobre el mismo caso | **Baja** | — | **No citar la cifra.** Citar que hay versiones incompatibles |
| cartera | Hoja de cálculo publicada con **1.969 registros** de usuarios, con nombre, identificador fiscal, empresa, cargo, jefatura directa, unidad de negocio, ubicación y correo corporativo | **La afirmación más verificable del conjunto**, porque es un número concreto, contable y comprobable por la víctima. **Un extorsionador no gana nada inventando un número que su víctima puede desmentir en diez minutos** | **Media-alta** | — | **Citable con atribución.** Es el dato que sostiene `E-1` |

### A.6 — Herramientas legítimas y controladores firmados · **NO SON MALIGNOS**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| herramienta | **Cinco controladores firmados pero vulnerables** *(no nombrados individualmente por la fuente)* | **NO SE BLOQUEAN POR HASH.** Son controladores **legítimos y con firma válida** de fabricantes reales, algunos en uso en parques reales: **un control basado en reputación de firma no ve nada de esto**. La defensa correcta es la **lista de controladores vulnerables** que mantiene el fabricante del sistema operativo, que los bloquea por vulnerabilidad y no por confianza. Su analista subraya que la técnica «se ha convertido en parte estándar del manual del *ransomware*» y que la herramienta **llega empaquetada con las ofertas de extorsión como servicio** | — | — | **Bloqueo por lista de controladores vulnerables** (`X-5.2`), **no por hash** |
| herramienta | **`AnyDesk`** | Herramienta legítima de acceso remoto, **ampliamente usada por operadores de extorsión y por administradores de sistemas**. El criterio es la aprobación y el contexto. **Lo que sí es anómalo es su registro en `SafeBoot\Network`** | — | — | **Inventario y lista de aprobadas.** No bloquear el producto |
| herramienta | **`Megasync` · `WinSCP` · `Filezilla` · `S3browser`** | **Cuatro herramientas legítimas de transferencia y sincronización, usadas en un solo ataque** — lo que su analista califica de inusual. **La señal no es ninguna de ellas: es que haya varias en un mismo servidor** | — | — | **Inventario.** Alertar sobre **acumulación**, no sobre presencia (`H-7`) |
| servicio | Biblioteca pública de **ECIES en Go** | El cifrador la usa para su criptografía, y es **la misma o similar a la de las familias `EvilByte` y `Prince`. **Compartir una biblioteca pública NO indica relación entre las familias**: está disponible para cualquiera. Es el mismo error que atribuir por un par de carga lateral popular, documentado en `CTI-2026-043` | — | — | **Contexto.** **No usar para vincular familias** |

### A.7 — Material de atribución y decisiones de higiene

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| artefacto | **`/PFAD=`** junto a `/PATH=` | **Hallazgo propio: el único parámetro del cifrador que no está en inglés, y está en ALEMÁN** (*Pfad*, «ruta»). La fuente lo publica en su tabla **sin comentarlo**. **No es atribución**: identifica el idioma de quien escribió una línea de código. **Y es el tercer caso de este lote** —iniciales de pinyin en `CTI-2026-043`, portugués en `CTI-2026-040`, alemán aquí—, lo que debería inducir **cautela y no confianza**: si tres operaciones distintas tienen artefactos en tres idiomas distintos, lo que el patrón demuestra es que **el idioma de un parámetro es un dato débil**. Lo que sí tiene valor es **dónde** aparece: en los tres casos, en el nombre de un parámetro o de un campo de configuración, **no en las cadenas visibles al usuario**. Es un sitio donde los desarrolladores no limpian | **Baja; observación propia** | Sin caducidad | **Requisito de colección** (`I-4`). **No usar para atribuir** |
| artefacto | **Tres programas de afiliados con repartos negociables**: extorsión como servicio, **extorsión por datos robados sin cifrado**, y **monetización de accesos** —el tercero diseñado para atraer corredores de acceso inicial— | **Es la explicación estructural de `KJ-4`**: una operación que vende extorsión sin cifrado **no depende del cifrador**, y por eso bloquear el cifrador no le quita el negocio. Anunciado el 2025-02-23 en el foro RAMP por la identidad `superSonic`, con todos los repartos «abiertos a negociación para cooperación de largo plazo» | Alta | — | **Contexto de modelo de negocio.** Base de `E-3` |
| artefacto | Identidades del grupo en foros: **`supersonic`** y **`superSonic`** en RAMP, **`Anubis__media`** en XSS, **publicando en ruso** | Material de identificación y de pivote | Alta | **Volátil** | **Contexto / pivote** |
| artefacto | **Comparación de binarios `Sphinx` → Anubis**: «altamente idénticos», con una sola diferencia menor — **la función que genera la nota de rescate**. Corroborado por separado por un segundo proveedor: «la carga parece prácticamente sin cambios respecto a la versión de Sphinx, con sólo la marca actualizada» | **La reconversión mejor establecida de esta cartera**, y conviene compararla con la de `CTI-2026-040`, que es de confianza moderada e inferida de conducta. **Aquí se compararon los binarios, y lo hicieron dos proveedores por separado** | **Alta, corroborada por dos** | No caduca | **Citable** |
| cartera | **Decisión de higiene: ningún dato personal de las personas expuestas en el caso chileno se reproduce en este informe** | Lo publicado por el atacante incluye, según la cobertura, contratos laborales, **copias de documentos de identidad**, certificados de nacimiento y de matrimonio, certificados de afiliación a sistemas de salud y de pensiones, y una hoja con 1.969 registros con identificador fiscal. **Son personas identificables que no han hecho nada, y reproducir cualquiera de esos datos —incluso parcialmente ocultos— no protege a nadie y perjudica a quien ya fue expuesto.** Este informe cita **el número de registros y las categorías de documento**, porque eso es lo que un consumidor necesita para dimensionar el daño, y **nada más**. Es la misma regla que `CTI-2026-036` aplicó a las direcciones de terceros comprometidos y `CTI-2026-038` al archivo de una víctima en un directorio abierto | **Decisión propia** | — | **Se consigna para que la omisión figure con su razón** |

## Anexo B — Fuentes y valoración

> Valoración doble tipo Admiralty/OTAN, más el **grado de establecimiento**. Y este informe añade un grado que esta cartera no tenía: **«declaración del adversario»**, que no es lo mismo que «sin evidencia» ni que «proveedor». El `Anexo D` desarrolla sus reglas.

| Fuente | Disciplina | Fiab. | Cred. | Grado | Notas de sesgo |
|---|---|---|---|---|---|
| **`B-1` — Trend Micro, «Anubis: A Closer Look at an Emerging Ransomware with Built-in Wiper», 2025-06-13** (Maristel Policarpio, Sarah Pearl Camiling, Sophia Nilette Robles) — **leída en original** | OSINT comercial · TECHINT de primera mano con análisis del cifrador | **B** | **2** | Proveedor | **Fuente primaria del cifrador.** Publica la **tabla completa de parámetros** —de donde sale `KJ-9`—, el modo de borrado **con capturas del antes y el después**, la lista de carpetas excluidas, la orden de borrado de copias de sombra con su literal inusual, la comparación de binarios con `Sphinx`, el detalle de los tres programas de afiliados, y la **victimología con Perú entre cuatro países cuando el sitio de fugas tenía siete entradas**. Declara con honestidad dos defectos del cifrador —los avisos interactivos y el fallo del fondo de escritorio— que **le quitan dramatismo a su propio hallazgo**, y eso es señal de calidad. Sesgo: interés comercial en nombrar una familia emergente, y la pieza cierra con sus propias capacidades de producto |
| **`B-2` — Symantec, «New Lindnor Backdoor and Glut of Security Killers Used in Ransomware Attack on U.S. Org», 2026-11-05** — **leída en original** | OSINT comercial · TECHINT de primera mano, de respuesta a incidentes | **B** | **2** | Proveedor | **La fuente más reciente y la más rica en indicadores.** Publica **catorce resúmenes criptográficos**, la clave de registro del Modo seguro con su orden exacta, el detalle de los dos desactivadores que suplantan a su propio producto con sus conmutadores, la designación `Hawkmoth` para el grupo desarrollador, la cifra de **~96 víctimas en doce meses con el 52 % en Estados Unidos**, y el dato del ataque de julio de 2026 con cuatro herramientas de exfiltración. **Y declara que el ataque falló**, incluido el detalle de que doce de trece ejecutables fueron bloqueados **por sus propios productos** — lo cual es a la vez su mayor sesgo comercial y su afirmación más verificable, porque es un resultado concreto y atribuible. Declara también lo que no sabe: **no identificó el acceso inicial** |
| **`B-3` — Cobertura chilena del caso Copec**, que reproduce **el comunicado íntegro de la compañía** y **las respuestas del grupo en una entrevista a un medio especializado** — **leída en original** | OSINT · prensa especializada regional, **como vehículo de dos fuentes primarias de distinta naturaleza** | **C** | **3** | **Víctima y adversario** | **La fuente más inusual del expediente, y la razón de ser del `Anexo D`.** Su valor no está en su análisis sino en que **transporta dos declaraciones primarias**: el comunicado de la víctima y las afirmaciones del atacante, incluida su respuesta a una pregunta directa sobre la duración de la exfiltración. Publica además capturas del sitio de fugas y del segundo servicio oculto con buscador, y el recuento de 1.969 registros. **Sesgo del vehículo:** es un medio especializado regional cuyo valor depende de la exclusividad, y publica material filtrado con detalle; **este informe usa de él los dos textos primarios y el número de registros, y no reproduce ningún dato personal** (`A.7`) |
| **`B-4` — Cobertura secundaria de la actividad de 2026** (perfiles y avisos de terceros) | OSINT · compilación derivada | **C** | **4** | Proveedor, no leído en original | Fuente de dos elementos que **no sostienen ningún juicio central**: la vinculación de la actividad de enero a marzo de 2026 con `CVE-2025-5777`, y la reclamación de julio de 2026 contra una filial de una multinacional de bebidas. Se citan con la vía declarada |
| **`B-5` — Recuentos regionales de terceros** (blogs y consultoras chilenas) | OSINT · compilación | **C** | **4** | Tercero, no verificado | Única aportación: el contexto de **trece organizaciones chilenas atacadas por extorsión en el primer trimestre de 2026**, y la observación de que en enero «el foco se desplazó hacia la energía». **Es contexto del caso, no dato del actor**, y ningún juicio descansa en ello (`G-8`) |
| **`B-6` — Material de desambiguación** (documentación del troyano bancario Android, del expediente de la puerta trasera en Python, y del proyecto libre homónimo) | OSINT · diverso | **—** | **—** | — | Se usa **sólo** para `O-1.2`: establecer que hay cuatro objetos distintos llamados «Anubis». No se usa ningún dato suyo |

> **Dos observaciones sobre la estructura de fuentes de este informe.**
>
> **La primera es favorable.** Las dos fuentes técnicas son de proveedores
> distintos, separadas por diecisiete meses, y **concuerdan en lo esencial sin
> citarse**: las dos establecen la reconversión desde `Sphinx` por comparación
> del binario, y las dos describen el modo de borrado. Eso es corroboración
> real, no eco.
>
> **La segunda es la que define el informe.** El hallazgo regional —el caso
> chileno— descansa en una fuente valorada `C`/`3`, y eso **parece** una
> debilidad y no lo es exactamente: lo que esa fuente aporta no es análisis
> propio sino **dos textos primarios de las dos partes del incidente**, el
> comunicado de la víctima y las palabras del atacante. La fiabilidad del
> vehículo importa para saber si transcribió bien; **la credibilidad de cada
> texto hay que valorarla por separado, y por eso `A.5` lleva una columna de
> quién lo dice.** Esa distinción —entre la fiabilidad del transportista y la
> credibilidad del contenido transportado— es la que el código Admiralty hace
> bien y la que se pierde al resumir una fuente en dos letras.

## Anexo C — Léxico de probabilidad y confianza

<!-- cti:bars title="Probabilidad estimativa — cuán probable es que el hecho sea cierto" -->

| Etiqueta | Valor |
|---|---|
| Casi con certeza (≥99 %) | 99 |
| Muy probable (80–95 %) | 88 |
| Probable (55–80 %) | 68 |
| Aproximadamente igual de probable (40–60 %) | 50 |
| Poco probable (20–45 %) | 32 |
| Muy poco probable (5–20 %) | 12 |
| Remoto (≤5 %) | 4 |

**Confianza** (en la *base* del juicio, no en su probabilidad): **alta** —fuentes múltiples, corroboradas, con método expuesto—; **moderada** —fuente única de calidad, o inferencia propia sobre datos verificables—; **baja** —dato ausente, o inferencia sobre indicios indirectos—.

> **Y la distinción que este informe necesita y que los dos ejes no capturan
> solos: capacidad frente a conducta.** `KJ-3` afirma que el cifrador **puede
> borrar** con probabilidad *casi con certeza* y confianza *alta* — y está
> bien, porque la capacidad está analizada con capturas. Pero **la
> probabilidad de que lo haya hecho contra una víctima real es otra
> afirmación**, y es *poco probable* porque no hay ningún caso documentado.
> Colapsar las dos produce la frase «Anubis borra los datos de sus
> víctimas», que **no es sostenible** con las fuentes de este expediente.
>
> **La regla que se sigue, y vale para cualquier análisis de capacidad
> destructiva:** una capacidad probada en laboratorio y un empleo observado
> en el mundo real son **dos juicios con dos probabilidades**, y el informe
> tiene que llevar las dos. El riesgo 1 del pre-mortem es, precisamente, que
> alguien cite la primera como si fuera la segunda.

## Anexo D — Cómo leer dos relatos del mismo incidente cuando uno lo publica el extorsionador

**El problema.** Un grupo de extorsión publica a una víctima en su sitio de fugas con una descripción del ataque, cifras y a veces una entrevista. La víctima publica un comunicado. **Las dos versiones parecen contradecirse, y casi siempre no se contradicen: responden a preguntas distintas.** Y, en la mayoría de los incidentes, **no existe ninguna tercera fuente**: lo que sabe la comunidad sobre ese caso lo dijeron el atacante y la víctima, cada uno con sus incentivos.

Esta cartera tiene seis informes de extorsión y ninguno había abordado esto, aunque todos dependen de ello: **la victimología de la extorsión la publica el extorsionista**, y un sitio de fugas es, antes que nada, **publicidad**.

**Paso 1 — Mapear cada afirmación a la propiedad que cubre.** Es el paso que resuelve la contradicción aparente, y suele bastar.

| Propiedad | Qué afirma típicamente la víctima | Qué afirma típicamente el atacante |
|---|---|---|
| **Disponibilidad** | «La operación no se vio afectada», «los servicios funcionan con normalidad» | Normalmente **nada**, si el cifrado falló |
| **Confidencialidad — datos de clientes** | «No se vieron comprometidos» | Normalmente **nada**, si no los tiene |
| **Confidencialidad — datos internos y de empleados** | **Normalmente nada** | **Todo**: volumen, listados, capturas |
| **Integridad** | Casi nunca se menciona | Casi nunca se menciona |
| **Alcance del acceso** | «Un sistema», «un acceso» | «La red», «el dominio» |
| **Vía de entrada** | Casi nunca | A veces, y con orgullo |

**En el caso de este informe, las dos partes llenaron casillas distintas y ninguna contradijo a la otra.** La víctima cubrió disponibilidad y datos de clientes; el atacante, confidencialidad de datos internos. **La casilla vacía —datos de empleados— es la que se llenó con la versión del atacante**, y es donde estaba el daño.

**Paso 2 — Clasificar cada afirmación del atacante por su incentivo.** No todas sus afirmaciones son igual de creíbles, y la diferencia es sistemática:

| Clase de afirmación | Incentivo del atacante | Credibilidad |
|---|---|---|
| **Volumen de datos** | **Inflar.** Fija el precio y la credibilidad de la amenaza | **Baja**, salvo que publique el listado |
| **Cifra del rescate** | **Variable y a veces contradictorio.** Inflar para prestigio, reducir para presionar | **Baja.** En este caso hay **dos cifras incompatibles** atribuidas al mismo actor |
| **Sofisticación de la entrada** | **Inflar.** Prefiere una vulnerabilidad a un descuido de la víctima | **Media** |
| **Producto o tecnología concreta por la que entró** | **Ninguno.** No le añade prestigio ni le protege | **Media-alta** |
| **Duración y método de la exfiltración** | **Casi ninguno**, y a veces responde a una pregunta directa | **Media-alta, y es la más útil para el defensor** |
| **Admisiones que le restan mérito** —«su defensa mitigó el cifrado»— | **Ninguno; al contrario** | **Alta.** Lo que un adversario admite en su contra es lo más creíble que dice |
| **Cifras concretas y contables que la víctima puede desmentir** —«1.969 registros»— | **Ninguno.** Inventarlas se descubre en diez minutos | **Media-alta** |

**La fila sexta es la regla de oro de este anexo:** **lo que un extorsionador admite en su propio perjuicio es la parte más creíble de su relato.** En este caso, que la defensa de la víctima consiguió mitigar el cifrado. Y la fila séptima es la segunda: **una cifra que la víctima puede refutar es costosa de inventar**; una que no puede refutar es gratis.

**Paso 3 — Clasificar las afirmaciones de la víctima por lo que no dicen.** Un comunicado corporativo suele ser **literalmente verdadero y deliberadamente parcial**, y eso no es una acusación: es la consecuencia previsible de que lo revise un departamento jurídico. La pregunta útil no es «¿miente?» —casi nunca— sino **«¿de qué no habla?»**. Las tres omisiones más frecuentes:

1. **De quién son los «datos personales»** que no se comprometieron. Si no lo dice, suele ser porque sólo cubre a una parte.
2. **El volumen.** Si el atacante da una cifra y la víctima no da ninguna, la del atacante es la única que circula.
3. **El plazo.** Cuánto tiempo estuvo dentro el adversario es casi siempre la pregunta peor respondida de un comunicado, y la que más dice.

**Paso 4 — Buscar los elementos verificables por terceros, que siempre hay alguno.** No todo en un sitio de fugas es publicidad:

| Elemento | ¿Verificable por un tercero? |
|---|---|
| La **existencia** de la publicación y su fecha | **Sí**, y es un hecho |
| El **listado de ficheros**, si lo publica | **Parcialmente**: los nombres de carpetas con nombres de filiales y socios reales son comprobables |
| Un **recuento concreto** de registros | **Parcialmente**, y es costoso de inventar |
| El **volumen en bytes** | **No** |
| La **vía de entrada** | **No** |
| El **plazo** | **No** |

**Paso 5 — Y escribirlo con atribución en cada línea.** Es lo que hace `A.5` de este informe: cada fila lleva **quién lo dice**, con tres valores posibles —hecho observable, declaración de la víctima, declaración del adversario— y la clase de incentivo cuando es del adversario. **El coste de no hacerlo es que la cifra del atacante acabe citada como dato del incidente**, que es el riesgo 2 del pre-mortem y el error más frecuente de esta disciplina.

**Lo que hay que declarar sobre este marco.** Tres cosas:

- **No resuelve el caso: lo ordena.** Después de aplicarlo seguimos sin saber si eran 6 TB. Lo que sabemos es **qué sabemos y con qué base**, y eso es suficiente para no afirmar de más.
- **Supone buena fe en la víctima, y no siempre está justificada.** Hay comunicados que afirman cosas falsas, no sólo parciales. El marco detecta la parcialidad —mirando qué casillas quedan vacías— y **no detecta la mentira**; para eso hace falta la tercera fuente que normalmente no existe.
- **Y hay un caso en que el marco no se aplica: cuando el atacante miente sobre la víctima entera.** Los sitios de fugas incluyen, con cierta frecuencia, organizaciones que nunca fueron comprometidas, reclamadas para inflar el expediente de la marca. **El paso 4 es la defensa contra eso**: si no hay ningún elemento verificable por un tercero, la publicación por sí sola no establece que haya habido un incidente.

**Dónde más se aplica en esta cartera.** En los seis informes de extorsión —`CTI-2026-014`, `015`, `016`, `024`, `035` y `040`— y en cualquier futuro, porque todos dependen de victimología publicada por el adversario. Y tiene un parentesco que conviene nombrar: es **la versión aplicada al adversario del principio del `Anexo D` de `CTI-2026-037`** —que un control que el adversario impone filtra información sobre su operación— sólo que aquí lo que filtra información no es un control, es **su necesidad de ser creído**. Un extorsionador tiene que resultar creíble para cobrar, y **la credibilidad obliga a publicar cosas comprobables**. Ahí está el margen del analista.

## Anexo E — Marcos de referencia empleados

- **ICD 203** (*Analytic Standards*), para el léxico de probabilidad y la separación de los ejes de probabilidad y confianza (Anexo C), **con la distinción adicional entre capacidad probada y conducta observada** que ese anexo desarrolla.
- **Código Admiralty/OTAN**, doble valoración de fuente e información (Anexo B), **con la observación de que una fuente que transporta textos primarios de dos partes requiere valorar el vehículo y el contenido por separado**.
- **Grado de establecimiento**, propuesto en `CTI-2026-039`, **ampliado aquí con un grado nuevo: «declaración del adversario»**.
- **MITRE ATT&CK v18** (`T-2`), con marcado de la procedencia de cada técnica, incluida la categoría «declaración del atacante».
- **Pirámide del Dolor** (Bianco), en `T-3`, con la observación de que **en este expediente los hashes rinden más de lo habitual** por tratarse de una puerta trasera propia vista en tres organizaciones.
- **Análisis de Hipótesis Competidoras (ACH)** y **pre-mortem**, en `O-6`.
- **Desambiguación de objetos homónimos**, con el molde de `CTI-2026-035` (`O-1.2`), **y la distinción entre colisión accidental y deliberada** que `CTI-2026-040` obligó a introducir.
- **Lectura de dos relatos del mismo incidente cuando uno lo publica el extorsionador**, propia de este informe (`Anexo D`), con su mapa de propiedades, su clasificación de afirmaciones por incentivo y su regla de oro.

## Anexo F — Paquete legible por máquina

Las tablas `cti:ioc` de este anexo alimentan `ioc_index.csv`. **Cinco advertencias de ingesta:**

1. **Los cinco controladores firmados y vulnerables, y las cinco herramientas legítimas de `A.6`, llevan tipo `herramienta`** y no entran en ningún agregado. **Los controladores no se bloquean por hash**: su firma es válida y están en uso en parques reales. Se bloquean con la lista de controladores vulnerables del fabricante del sistema operativo.
2. **Las entradas de `A.5` llevan tipo `cartera`** y **cada una indica quién lo dice**: hecho observable, declaración de la víctima o declaración del adversario. **Un consumidor que ingiera la cifra de 6 TB sin esa columna estará citando publicidad del extorsionador como dato del incidente.**
3. **Los catorce hashes de `A.3` sí son indicadores operativos**, y en este expediente **rinden más de lo habitual**: tres corresponden a una puerta trasera propia que apareció en **tres organizaciones, dos de ellas sin actividad de cifrado**.
4. **El indicador de mayor valor del informe no es ingerible**: es la regla de correlación de `A.1` sobre **intentos bloqueados**, y se implanta en la plataforma de detección, no en la de indicadores.
5. **Y una advertencia de desambiguación**: hay **cuatro objetos distintos llamados «Anubis»** (`O-1.2`). Una ingesta por nombre de familia mezcla material de una extorsión, un troyano bancario Android, una puerta trasera de otro actor y un proyecto de software libre legítimo.

Ninguna de las dos fuentes primarias publica paquete STIX. Si alguna lo hace, será la fuente preferente para ingesta y este anexo pasará a ser derivado.

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0 | 2026-11-19 | Emisión inicial. Incluye: la **corroboración de la afirmación del requisito** que la nota de cartera daba por improbable —Anubis publicó a una energética chilena en enero de 2026—, con la lección de método que eso deja (§3.5, punto 6); el **segundo país regional**, Perú, documentado cuando el sitio de fugas tenía siete entradas (`KJ-2`); el análisis de la **capacidad de borrado** y de cómo altera el cálculo de pagar, **con la salvedad expresa de que no hay ningún uso documentado** (`KJ-3`, `E-2`); el juicio de que **el modelo de negocio no necesita que el cifrado funcione**, apoyado en los dos casos documentados y en los tres programas de afiliados (`KJ-4`, `E-3`); el **hallazgo metodológico** de que los tres relatos del caso chileno son compatibles porque responden a preguntas distintas (`KJ-5`, `E-1`, `Anexo D`); la **regla de correlación sobre intentos bloqueados** como única medida que convierte un control existente en una detección nueva (`KJ-8`, `E-4`, `X-3.2`); el **hallazgo propio del parámetro en alemán**, con la lectura de que tres casos en un lote debilitan el valor del indicio en lugar de reforzarlo (`KJ-9`); la **desambiguación de cuatro objetos homónimos** (`O-1.2`); y la decisión de higiene de **no reproducir ningún dato personal** de las personas expuestas (`A.7`) | Célula CTI |

## Anexo H — Realimentación del consumidor

Este informe corrobora una afirmación que se daba por improbable, propone un marco para leer lo que publica un extorsionador, y sostiene que su modelo de negocio no necesita el cifrado. Las tres cosas se pueden atacar.

1. **¿Nuestras alertas cubren intentos BLOQUEADOS de desactivar la seguridad, o sólo los exitosos?** Es `G-5`, se responde con una pregunta al SOC, y es **la única medida de este informe que convierte un control que ya existe en una detección que no existía**. Cuesta una regla de correlación.
2. **¿Cómo está agregada nuestra alerta de exfiltración: por sesión, por hora, o por destino y día sostenido?** Es `G-6`. Si es de las dos primeras, **no veríamos la exfiltración de una semana a baja velocidad** que el atacante declara en el caso chileno. Es un cambio de consulta, no de herramienta.
3. **¿Se rompe el `Anexo D`?** Lo más útil que alguien puede aportar es un **contraejemplo**: un caso en que el comunicado de la víctima y la versión del atacante sean **genuinamente incompatibles** y no sólo complementarios. El marco predice que es raro, y no lo ha medido.
4. **¿Alguien ha visto un uso real de `/WIPEMODE`?** Es `G-2` e `I-1`. **Sería el primer caso documentado**, y comunicarlo cerraría la cuestión para toda la comunidad. La consulta que lo detectaría en el propio entorno es `H-10`: ficheros listados a 0 KB en masa.
5. **¿Se publicó un informe independiente del incidente chileno?** Es `G-1` e `I-2`. **La autoridad fue notificada**, según el comunicado de la compañía, de modo que existe al menos un expediente. Un alcance verificado permitiría contrastar cada afirmación del atacante y **cerrar la cuestión central del `Anexo D`**.
6. **¿Se citó la cifra de 6 TB como dato del incidente?** Es el riesgo 2 del pre-mortem y el error más probable de este informe, porque las cifras concretas se citan. Lo dice el atacante, en su sitio de fugas, y es la métrica que más incentivo tiene para inflar.
7. **¿Se citó `KJ-3` sin su salvedad?** Es el riesgo 1. «Anubis puede borrar» es sostenible; «Anubis borra los datos de sus víctimas» **no lo es** con estas fuentes.
8. **¿Existe un procedimiento de comunicación al personal propio** para el caso de que se filtren sus datos personales? Es `E-1`, punto 2, y en el caso chileno **lo publicado fueron expedientes de personal con documentos de identidad**. Es la parte peor atendida de casi todos los incidentes.
9. **¿Qué hay dentro de cada repositorio interno de ficheros?** Es `G-7` y la decisión 4 de `E-5`. **Si el cifrado falla, el daño es de confidencialidad y su alcance lo determina el contenido del sistema accedido**, no el número de máquinas cifradas. Ningún producto responde esto.
10. **Y una pregunta sobre esta colección:** la nota de cartera que acompañaba al requisito decía que la afirmación era «muy probablemente no corroborable». **Se corroboró.** Es el segundo caso de este lote con la misma forma —el primero fue `CTI-2026-037`—, y conviene preguntarse cuántas notas de esa clase hay en la cartera y cuántas se han comprobado. **Una expectativa sobre el resultado de una búsqueda no es un sustituto de la búsqueda.**

*Fin del informe `CTI-2026-041` v1.0.*
