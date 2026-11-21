---
tlp: "TLP:CLEAR"
pap: "PAP:WHITE"
id: "CTI-2026-058"
version: "1.1"
tipo: "Perfil de operación de extorsión"
foco_regional: "Alemania 29 % · Chile 1 víctima · México 4 · **Sudamérica declarada por AA26-293A**"
niveles: ["Estratégico", "Operacional", "Técnico"]
autor: "Célula CTI"
actor: "safepay · SafePay"
fecha: "2026-11-19"
caduca: "2026-12-19"
distribucion: "El actor más regular del lote, con la única víctima chilena de los seis. **La versión 1.1 incorpora el aviso conjunto AA26-293A de seis agencias (20-10-2026), que el informe inicial no conocía, y corrige el recuento de días de silencio de `KJ-4`.** Contiene además un hallazgo de higiene de indicadores propio: **cuatro de las nueve direcciones IP del aviso pertenecen a Cloudflare, GitHub y Google**, y una quinta a un conjunto de acceso residencial, de modo que una ingesta ciega del aviso bloquearía servicios legítimos de uso masivo (`A.4`, `X-4`). Contiene una advertencia operativa: el perfil declarado por el proveedor incluye un interruptor de idioma que, si fuera cierto, haría ineficaz una contramedida que algunos equipos han adoptado. No se reproduce ningún nombre ni dominio de víctima. Difusión libre conservando la atribución y las salvedades de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-058

## Veintinueve de cada cien víctimas en Alemania, y los cinco sitios del actor caídos a la vez

### El más regular de los seis actores del lote, el único con una víctima chilena, y el que lleva doce días sin publicar

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-058` |
| Versión | 1.0 |
| Tipo | Perfil de operación de extorsión |
| Clasificación | `TLP:CLEAR` · `PAP:WHITE` |
| Fecha de emisión | 2026-11-19 |
| Caducidad | 2026-12-19 |
| Niveles | Estratégico · Operacional · Técnico |
| Actor | safepay · SafePay |
| Entradas en la ventana | 134 · **99 % con dominio** |
| Concentración | **Alemania 39 (29,1 %)** · 28 países |
| Relevancia regional | 9 LATAM (6,7 %) · **1 Chile** · 4 México |
| Infraestructura | 5 sitios · **0 activos** · último publicado 2026-11-07 |
| Autor | Célula CTI |

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** **Concentra el 29,1 % de sus víctimas en Alemania, una proporción que ningún otro actor del lote se acerca a tener en ninguna geografía.** Treinta y nueve de 134 entradas son alemanas, frente a trece estadounidenses — es el único actor de los seis, y de los que la cartera ha medido, en que **Estados Unidos no es el primer país**. Añadiendo Suiza (7) y Bélgica (3), el espacio germanófono y limítrofe suma **49 de 134 (36,6 %)**. Valoramos **casi con certeza** *(≥99 %)* el recuento sobre un catálogo con 86 % de cobertura de país. **Confianza: alta.** *Consecuencia:* **es el actor que una organización alemana, suiza o austríaca debe vigilar por delante de los demás de este lote**, y la concentración exige explicación (`E-2`).

**KJ-2.** **Es el único de los seis actores del lote con una víctima chilena, y tiene cuatro mexicanas.** Nueve entradas latinoamericanas (6,7 %), de las que **una es chilena**. Es poco en términos absolutos, y es el único punto de contacto nacional de todo el lote. Valoramos **probable** *(55–80 %)* que la atribución de país sea correcta, con la salvedad de que es enriquecimiento derivado. **Confianza: moderada.** *Consecuencia:* **hay una organización chilena en este catálogo y la comprobación cuesta minutos**, porque el 99 % de las entradas lleva dominio (`E-2.2`).

**KJ-3.** **Es el actor más regular de los seis: veintinueve días de actividad repartidos en seis meses, con mediana de tres entradas por día y un máximo de diez.** No tiene tandas: `krybit` publicó 45 entradas en un día y `Storm` 73 en su primero, mientras éste nunca pasa de diez. Y su retraso mediano entre la fecha declarada y la de descubrimiento es de **0,0 días**. Valoramos **casi con certeza** *(≥99 %)* las mediciones. **Confianza: alta.** *Consecuencia:* el patrón es el de una operación con **flujo continuo de víctimas y publicación inmediata**, no de acumulación y volcado — y eso significa que **no hay ventana de semanas entre compromiso y publicación**, al contrario que en `CTI-2026-057` (`O-3`).

**KJ-4.** *(corregido en 1.1)* **Sus sitios dejaron de responder y el actor lleva nueve días sin publicar —no doce—, y su dirección de publicación vuelve a figurar como disponible.** La versión 1.0 fijó la última entrada el 7 de noviembre y contó doce días de silencio. **Es incorrecto: la fuente registra una entrada posterior, publicada el 12 de noviembre de 2026** (Tailandia, manufactura), **corroborada de forma independiente** por el informe semanal de CYFIRMA del 20 de noviembre, que describe la publicación de datos de una empresa tailandesa de manufactura. El silencio real es por tanto de **nueve días al 21 de noviembre**, y al cierre de la versión 1.0 era de **siete**, no de doce. Y la dirección `safepaypfxn…` —la del `KJ-5`— **figura hoy como disponible** en la misma fuente que el 19 de noviembre la daba caída. Seguimos valorando **posible** *(40–60 %)* la migración y rebajamos el cese a **improbable** *(20–45 %)*, porque un actor que ha publicado hace nueve días y cuyo portal responde no es un actor cesado. **Confianza: moderada para la observación —el campo de disponibilidad de esta fuente se contradice en el 31 % de los casos (`§O-7.1` de `CTI-2026-054`) y no trae marca de tiempo del sondeo—; baja para la interpretación.** *Consecuencia:* **la fecha de decisión del 3 de diciembre se mantiene, pero el escenario por omisión pasa de cese a continuidad** (`E-3`, `A.1`).

**KJ-5.** **Su única dirección de publicación lleva prefijo legible, igual que krybit, y eso la hace cazable por patrón si reaparece.** Las 134 entradas se sirvieron desde `safepaypfxntwixwjrlcscft433ggemlhgkkdupi2ynhtcmvdgubmoyd.onion`, con los siete primeros caracteres legibles. Valoramos **casi con certeza** *(≥99 %)* la observación. **Confianza: alta.** *Consecuencia:* si el actor reaparece con infraestructura nueva y mantiene la práctica, **se puede localizar antes de que publique víctimas** (`X-1`).

**KJ-6.** **El perfil declarado contiene una advertencia que hay que trasladar aunque no esté corroborada: un interruptor que aborta la ejecución en sistemas configurados en idiomas de Europa del Este.** Si fuera cierto, invalidaría una contramedida que algunos equipos han adoptado —configurar el idioma o la distribución de teclado del sistema para disuadir— porque **sólo funcionaría contra este actor y no contra los demás**, y porque **depende de que el adversario mantenga una decisión que puede revertir en una compilación**. Valoramos **improbable** *(20–45 %)* que el interruptor exista —rebajado en 1.1 desde *posible*—. **Confianza: baja.** *Razón de la rebaja:* **el aviso conjunto `AA26-293A`, redactado por seis agencias sobre al menos 600 víctimas, no menciona en ningún punto comprobación de idioma, configuración regional, distribución de teclado ni país del sistema**, y sí documenta en detalle el resto de la cadena. Es una ausencia significativa, no un silencio neutro. *Consecuencia:* **la recomendación negativa de `X-2` se refuerza**: no se recomienda esa contramedida, y ahora tampoco la respalda la única fuente primaria del expediente (`X-2`, `O-4.2`).

**KJ-8.** *(nuevo en 1.1)* **Existe un aviso conjunto de seis agencias sobre este actor, publicado el 20 de octubre de 2026, que la versión 1.0 no conocía, y eleva todo el expediente de «perfil declarado por un proveedor» a «actor con fuente primaria gubernamental».** `AA26-293A` —«#StopRansomware: SafePay Ransomware»— lo firman el **FBI**, **CISA**, el **Servicio Secreto de Estados Unidos**, el **Landeskriminalamt de Renania-Palatinado** (Alemania), la **National Crime Agency** británica y la **North West Regional Organised Crime Unit**. Declara que el grupo ha afectado a **«al menos 600 víctimas»** de «múltiples sectores de infraestructura crítica» **desde agosto de 2024**, y nombra como regiones alcanzadas **«Norteamérica, Sudamérica, Europa y Australia»**. Valoramos **casi con certeza** *(≥99 %)* el contenido del aviso. **Confianza: alta.** *Consecuencias, tres:* **(a)** la presencia del cuerpo policial de un Land alemán entre los firmantes **corrobora de forma independiente la concentración alemana de `KJ-1`**, que la versión 1.0 midió sin saber que la policía alemana estaba en el caso; **(b)** **Sudamérica figura como región alcanzada en un documento oficial**, lo que sitúa la relevancia regional del expediente por encima de la única víctima chilena de `KJ-2` —aunque el aviso **no nombra ningún país** de la región—; y **(c)** el aviso documenta **cinco CVE** y el vector de acceso, lo que cierra la brecha `G-4` (`O-7`, `A.5`).

**KJ-9.** *(nuevo en 1.1)* **Y el hallazgo que más importa de este aviso no es lo que dice del actor, sino lo que le pasaría a quien ingiriera sus indicadores sin leerlos: cuatro de sus nueve direcciones IP pertenecen a Cloudflare, GitHub y Google.** Resueltas por `whois` y RDAP contra los registros regionales el 21 de noviembre de 2026: `104.26.2.223` es **CLOUDFLARENET (Cloudflare, Inc.)**; `140.82.114.4` es **GitHub, Inc.**; `185.199.108.133` es **GitHub, Inc.** (el rango de GitHub Pages); `173.194.194.94` es **Google LLC**. Una quinta, `5.255.11.134`, es un **conjunto de acceso ADSL de YemenNet** (`AS30873`). **De las nueve, el aviso califica una sola como mando y control**: `88.119.167.239` —«soc.dll command and control»—, alojada en UAB Bacloud (Lituania). Las otras llevan descripciones de rol que **no son de infraestructura del adversario**: tres dicen «SafePay victim intrusion», una «Hosting victim data», dos «Used in exfiltration» y una «Client login panels». Valoramos **casi con certeza** *(≥99 %)* la titularidad verificada. **Confianza: alta.** *Consecuencia:* **una lista de bloqueo perimetral alimentada con las nueve direcciones del aviso bloquea Cloudflare, GitHub, GitHub Pages y Google**, y además un rango residencial yemení que a estas alturas pertenece casi con seguridad a otro abonado. **El aviso no tiene la culpa y conviene decirlo**: advierte expresamente —«recomendamos a las organizaciones investigar o verificar las direcciones IP antes de actuar, por ejemplo bloqueando»— y declara que los indicadores «deben interpretarse como infraestructura observada históricamente dentro de la ventana de actividad», que fija entre **noviembre de 2024 y agosto de 2026**. **El fallo posible está en la ingesta, no en la redacción** (`A.4`, `X-4`).

**KJ-10.** *(nuevo en 1.1)* **El perfil del proveedor que la versión 1.0 consignó con la advertencia de que «nada está corroborado» queda corroborado en cinco elementos y sin apoyo en cuatro, y la separación es informativa.** **Corroborado por `AA26-293A`:** el acceso por **VPN y RDP con credencial válida** —el aviso lo precisa más y añade que los operadores **usan direcciones del proveedor de VPN «Mullvad»** para el acceso inicial—; el reconocimiento con **`ShareFinder.ps1`**; la exfiltración con **WinRAR y RClone**; la **extensión `.SafePay`**; y el cifrador **en forma de biblioteca** (el aviso lista `locker.dll`). **Sin apoyo en el aviso, que no los menciona:** el **linaje LockBit** —el aviso no nombra ningún otro grupo—, la nota **`readme_safepay.txt`**, la **ofuscación por triple XOR** —sólo documenta empaquetado genérico— y el portal por **red TON** —sólo cita Tor—. Y el aviso aporta un dato que el perfil no traía: el cifrado es **híbrido, ChaCha20 con RSA**, parcial o total según tipo y tamaño de fichero. Valoramos **probable** *(55–80 %)* que los cuatro elementos sin apoyo sean inexactos del perfil y no huecos del aviso, **salvo el linaje**, que un aviso operativo no tiene por qué tratar. **Confianza: moderada.** *Consecuencia:* **el perfil del proveedor acierta en lo observable en la red y falla en lo que requiere muestra**, que es el patrón que cabía esperar y que conviene recordar la próxima vez que una ficha de proveedor sea la única fuente (`O-4.2`, `Anexo B`).

**KJ-7.** **El resto del perfil declarado describe una operación de equipo cerrado y no un programa de afiliados, lo que es coherente con la regularidad medida.** La ficha del proveedor afirma linaje LockBit, acceso mediante credenciales de VPN y RDP robadas, permanencia inferior a un día antes del cifrado, cifrador en biblioteca PE32 con marca de tiempo falsificada, extensión `.safepay`, nota `readme_safepay.txt`, ofuscación por triple XOR, reconocimiento con `ShareFinder.ps1`, exfiltración con WinRAR y Rclone, y portal de negociación accesible por Tor **y por la red TON**. Nada está corroborado. Valoramos **probable** *(55–80 %)* que el carácter de equipo cerrado sea correcto, por consistencia con `KJ-3`: **un programa de afiliados produce tandas irregulares, y aquí no hay ninguna**. **Confianza: baja para el perfil, moderada para la inferencia de consistencia.** *Consecuencia:* la cadencia observada es la única corroboración indirecta de algo del perfil, y es la que más vale (`O-4`).

---

## 2. Resumen ejecutivo

SafePay publicó **134 entradas** entre el 19 de mayo y el 7 de noviembre de 2026, y es el actor más atípico de los seis que la cartera incorpora en este lote, por dos razones.

La primera es geográfica. **Veintinueve de cada cien de sus víctimas son alemanas**: treinta y nueve entradas, frente a trece de Estados Unidos. Es el único actor de este lote —y de los que la cartera ha medido— en el que Estados Unidos no encabeza la lista. Sumando Suiza y Bélgica, el espacio germanófono y limítrofe llega al **36,6 %** del catálogo. Una concentración así no se produce por azar en un conjunto de veintiocho países, y exige explicación: o el actor selecciona por geografía, o su vía de acceso está concentrada ahí.

La segunda es de ritmo. Es **el actor más regular del lote**: veintinueve días de actividad repartidos a lo largo de seis meses, con una mediana de tres entradas por día y un máximo de diez. Ninguna tanda. Para comparar, `krybit` publicó cuarenta y cinco entradas en un solo día y `Storm` setenta y tres en el primero. Y el retraso entre la fecha que el propio sitio declara y la fecha en que el rastreador la ve tiene mediana de **cero días**: publica lo que ocurre, cuando ocurre.

Eso tiene una consecuencia incómoda para una organización comprometida, y conviene decirla al revés de como suele decirse. En `CTI-2026-057` la publicación por lotes con once días de retraso significaba margen: semanas entre la exfiltración y la aparición pública. **Aquí no hay margen.** Un actor que publica el mismo día en que actúa no deja intervalo para decidir nada.

La tercera observación es la más perecedera y la más llamativa: **sus cinco direcciones de infraestructura están caídas** al 19 de noviembre, y la última entrada es del 7. Doce días de silencio en un actor que publicaba cada pocos días con regularidad de reloj. Puede ser cese, puede ser migración, y no se puede decidir desde fuera. Es el juicio de este lote que antes caduca.

Su única dirección de publicación lleva prefijo legible —`safepay`—, lo que la hace cazable por patrón igual que la de `krybit`. Si el actor reaparece con infraestructura nueva y mantiene esa práctica, se le puede localizar antes de que publique nada.

Del perfil que el proveedor publica, nada está corroborado. Pero contiene un elemento que hay que trasladar precisamente porque otros podrían actuar sobre él: la afirmación de que el cifrador **aborta su ejecución en sistemas configurados en idiomas de Europa del Este**. Existe la tentación de convertir eso en contramedida —cambiar la configuración regional de los sistemas—, y este informe recomienda explícitamente **no hacerlo**, por dos motivos que se desarrollan en `X-2`.

---

## 3. Alcance y limitaciones

### 3.1 Base de la medición

Las 134 entradas y los 5 sitios proceden de la API de cti.fyi consultada el 19 de noviembre de 2026. Reproducible con `Anexo F`.

### 3.2 Límites

- **El país y el sector son enriquecimiento derivado**, con cobertura del 86 % para país. `KJ-1` y `KJ-2` heredan ese límite.
- **La captura de pantalla sólo acompaña al 55 % de las entradas** (74 de 134), proporción notablemente menor que en `krybit` (100 %) o `Storm` (100 %). No se sabe si es decisión del actor o del raspador.
- **No se leyó el sitio de filtración**, que además está caído.
- **Ninguna víctima ha confirmado nada.**
- **El perfil del actor no está corroborado en ningún punto**, y es extenso. Véase `KJ-6`, `KJ-7` y `Anexo B`.
- **Una segunda fuente da cifras incompatibles y no se usa**: CTIWatch atribuye a este actor 618 víctimas en su cabecera y 521 en la prosa de la misma página, y declara su última actividad en marzo de 2026 — la misma fecha que asigna a otros tres actores (`CTI-2026-054` `§O-8.2`).

### 3.3 Higiene

No se reproduce ningún nombre ni dominio de víctima, **incluida la chilena de `KJ-2`**. La organización no ha confirmado nada y nombrarla aquí amplificaría una reclamación de adversario. La comprobación la puede hacer cualquier organización sobre su propio dominio sin necesidad de que este informe lo publique.

### 3.4 Veredicto por nivel

| Nivel | Veredicto | Motivo |
|---|---|---|
| Estratégico | **Utilizable** | Concentración y cadencia medidas con cobertura alta |
| Operacional | **Utilizable, con el juicio de estado caducando rápido** | `KJ-4` |
| Táctico | **No evaluable** | Sin TTP observados |
| Técnico | **Parcial, y con una advertencia** | `X-1` sí; `X-2` es una recomendación negativa |

---

# NIVEL ESTRATÉGICO

## E-1. Cifras

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `134` | Entradas en la ventana | Octavo del semestre |
| `39` | **Entradas alemanas (29,1 %)** | **Estados Unidos sólo 13** (`KJ-1`) |
| `49` | Alemania + Suiza + Bélgica | **36,6 % del catálogo** |
| `28` | Países distintos | Frente a 46 en krybit |
| `1` | **Víctima chilena** | **La única de los seis actores del lote** |
| `133 / 134` | Entradas con dominio (99 %) | Comprobación inmediata por la víctima |
| `74 / 134` | Entradas con captura (55 %) | **La proporción más baja del lote tras BrainCipher** |
| `29` | **Días de actividad en 172** | Mediana 3/día, **máximo 10** (`KJ-3`) |
| `0,0 d` | **Retraso mediano declarado→visto** | **Sin margen** |
| `5 / 0` | Sitios registrados / activos | `KJ-4` |
| `12` | Días sin publicar al cierre | Último: 2026-11-07 |

## E-2. La concentración alemana

| País | Entradas | Proporción |
|---|---|---|
| **Alemania** | **39** | **29,1 %** |
| Estados Unidos | 13 | 9,7 % |
| Italia | 8 | 6,0 % |
| Japón | 7 | 5,2 % |
| Suiza | 7 | 5,2 % |
| Reino Unido | 7 | 5,2 % |
| México | 4 | 3,0 % |
| Bélgica | 3 | 2,2 % |
| Otros 20 países | 46 | 34,3 % |

**Lo primero que hay que señalar es lo que falta.** En todos los catálogos de extorsión que esta cartera ha medido, Estados Unidos encabeza la lista: 11.314 de las entradas del agregado de la fuente, 48 de 144 en `dragonforce`, 72 de 129 en `Booba Project`, 43 de 86 en `Storm`. **Aquí es noveno por detrás de Alemania y con un tercio de sus entradas.** Eso es una anomalía real, no un efecto de muestra pequeña: con 134 entradas y 28 países, la probabilidad de que una concentración del 29 % en un país no estadounidense sea azar es despreciable.

Las dos explicaciones compatibles:

**Selección deliberada por geografía.** Un actor puede preferir una jurisdicción por capacidad de pago, por cobertura de seguro, por régimen de notificación obligatoria, o por idioma de negociación. Alemania puntúa alto en las cuatro.

**Concentración de la vía de acceso.** Si el acceso procede de credenciales de VPN y RDP robadas —como declara el perfil, sin corroborar— y esas credenciales proceden de un lote concreto, la geografía de las víctimas es la geografía del lote y no una decisión del actor.

**No se pueden distinguir con estos datos**, y la distinción es operativamente relevante: en el primer caso una organización alemana está más expuesta por ser alemana; en el segundo, lo está por usar un producto o un proveedor concretos. Va a `G-2`.

### E-2.1 Los sectores no concentran

Tecnología 24, Manufactura 22, Servicios profesionales 14, Otros 12, Sanidad 11. Ninguno por encima del 18 %. **La concentración de este actor es geográfica y no sectorial**, lo que debilita ligeramente la hipótesis de selección deliberada: un actor que elige por capacidad de pago suele mostrar también sesgo de sector.

### E-2.2 La víctima chilena, y qué hacer con ella

Nueve entradas latinoamericanas (6,7 %): cuatro mexicanas, **una chilena**, y el resto repartido.

Es la única víctima chilena de los seis actores de este lote, y por tanto el único punto de contacto nacional del conjunto. Puesta en contexto con `CTI-2026-015`, donde se midió que **Qilin concentra veinte de las treinta víctimas chilenas** del top diez de extorsión, una víctima no cambia ninguna prioridad. Pero existe, y el 99 % de cobertura de dominio de este catálogo significa que **cualquier organización chilena puede comprobar en minutos si es ella**.

## E-3. Los cinco sitios caídos

| Dirección | Estado | Versión declarada |
|---|---|---|
| `safepaypfxntwixwjrlcscft433ggemlhgkkdupi2ynhtcmvdgubmoyd.onion` | **Inactivo** | — |
| Otras cuatro direcciones registradas | **Inactivas** | 3 de ellas v3 |

**Cinco de cinco, ninguna activa.** Y la última entrada publicada es del 7 de noviembre, doce días antes del cierre de este informe, en un actor cuya cadencia medida era de una publicación cada pocos días durante seis meses.

Las tres lecturas posibles, y ninguna es decidible desde fuera:

1. **Cese de la operación.** Compatible con la parada en seco. Las operaciones de extorsión cierran por detención, por retirada voluntaria con el dinero, o por pérdida de infraestructura.
2. **Migración de infraestructura.** Compatible con que las cinco caigan a la vez: un actor que cambia de alojamiento abandona el conjunto anterior en bloque. Si es esto, **reaparecerá**, y `X-1` dice cómo buscarlo.
3. **Interrupción rutinaria.** La menos probable, porque doce días es mucho para un actor con esta regularidad, y porque una interrupción técnica no suele tumbar cinco servicios ocultos independientes simultáneamente.

> **Y una cautela de método que afecta a este juicio.** El estado de los sitios procede de un campo de la fuente que, según se midió en `CTI-2026-054` `§O-7.1`, **se contradice con el campo de disponibilidad en el 31 % de los casos** de este lote. Para safepay los cinco coinciden en inactivo, lo que refuerza la lectura, pero **no se verificó de forma independiente** porque no hay acceso a Tor en este entorno. `KJ-4` lleva confianza baja para la interpretación por este motivo.

Este es, con diferencia, el juicio de más corta vida del lote. La reevaluación está fijada en `I-1` a catorce días.

## E-4. Decisiones que este informe pide

1. **Para una organización alemana, suiza o austríaca: este es el actor del lote que le afecta.** Comprobación del propio dominio, coste de minutos.
2. **Para la única organización chilena del catálogo: la comprobación es inmediata** y no requiere este informe, sólo el propio dominio.
3. **No adoptar la contramedida de configuración regional.** Véase `X-2`. Es una recomendación negativa explícita y es la aportación más útil del nivel técnico.
4. **Fijar vigilancia del patrón de prefijo de `X-1`** para detectar reaparición antes de que publique.
5. **Reevaluar el estado en catorce días.** Si reaparece, `KJ-4` se resuelve hacia migración; si no, hacia cese.

---

# NIVEL OPERACIONAL

## O-1. Identificación

| Campo | Valor | Procedencia |
|---|---|---|
| Nombre | safepay · SafePay | Prefijo de su dirección y extensión declarada |
| Primera entrada observada | 2026-05-19 | Medición propia — **borde de la ventana**, el actor es anterior |
| Última entrada observada | **2026-11-07** | Medición propia |
| Aparición declarada | Finales de octubre de 2024 | **Perfil de proveedor, no corroborado** |
| Linaje declarado | Derivado de LockBit | **Perfil de proveedor** |
| Modelo declarado | **Equipo cerrado, no RaaS** | **Perfil de proveedor**, coherente con `KJ-3` |
| Acceso declarado | Credenciales de VPN y RDP robadas | **Perfil de proveedor** |
| Permanencia declarada | Menos de un día antes del cifrado | **Perfil de proveedor** |
| Negociación declarada | Portal por Tor **y por red TON** | **Perfil de proveedor** |
| Sitios | 5 registrados · **0 activos** | Medición propia |

**Sobre el borde de la ventana.** La primera entrada observada cae el 19 de mayo, que es el primer día del recorte de seis meses. Eso significa que **el actor ya estaba activo antes** y que este expediente no mide su inicio. Es el artefacto de recorte documentado en `CTI-2026-054` `§E-1.2`, y se consigna para que nadie lea «primera entrada 19 de mayo» como fecha de aparición.

## O-2. El catálogo

| Medición | Valor | Lectura |
|---|---|---|
| Con dominio | **133 / 134 (99 %)** | **Comprobable por la víctima** |
| Con captura | 74 / 134 (55 %) | La segunda proporción más baja del lote |
| Con país | 115 / 134 (86 %) | Base sólida para `KJ-1` |
| Con fecha declarada | 102 / 134 (76 %) | — |
| Con revisión posterior | 3 / 134 (2 %) | **Apenas edita sus entradas** |
| Con historial de título | 0 | **No desenmascara progresivamente** |

Dos observaciones.

**La primera: el título es el dominio, como en `krybit`.** Eso sitúa el catálogo en los niveles medios de la escala de prueba de `CTI-2026-048` `Anexo D` y lo hace comprobable en minutos por el afectado. Es el rasgo que convierte `KJ-1` y `KJ-2` en accionables y no sólo en informativos.

**La segunda: no hay ni un cambio de título en 134 entradas.** `CTI-2026-054` `§E-3` documentó que varios actores publican el nombre enmascarado y lo revelan después —`AuditTeam` desenmascaró cuatro víctimas en veintisiete segundos—. Este actor **no usa esa palanca**: publica el dominio completo desde el principio. Combinado con el retraso de cero días de `KJ-3`, describe una operación que **no gradúa la presión en el tiempo**: publica todo, de inmediato.

## O-3. Cadencia: el actor más regular del lote

Veintinueve días de actividad en ciento setenta y dos, con mediana de tres entradas por día y máximo de diez. La distribución completa está en `Anexo F`; lo relevante es la forma:

| Actor del lote | Días con actividad | Mediana/día | Máximo en un día |
|---|---|---|---|
| **safepay** | **29** | 3 | **10** |
| dragonforce | 50 | 1 | 24 |
| Booba Project | 19 | 6 | 36 |
| krybit | 14 | 6 | **45** |
| Storm | 8 | 2 | **73** |
| BrainCipher | 8 | 31 | **142** |

**Es el único cuyo máximo diario está en el mismo orden de magnitud que su mediana.** Los otros cinco tienen al menos una tanda que multiplica por siete o más su ritmo habitual.

Y el retraso mediano entre la fecha declarada y la de descubrimiento es de **0,0 días**: publica el mismo día que declara.

> **La consecuencia es la inversa de la de `CTI-2026-057`, y conviene no confundirlas.** Allí, once días de retraso mediano y publicación por lotes significaban **semanas de margen** entre el compromiso y la aparición pública: una detección de exfiltración en ese intervalo llegaba a tiempo. **Aquí no hay intervalo.** Un actor que publica el mismo día no deja ventana para decidir si notificar, si negociar o si preparar comunicación. Si el perfil declarado acierta en que la permanencia antes del cifrado es inferior a un día, **toda la secuencia —acceso, exfiltración, cifrado, publicación— cabe en cuarenta y ocho horas**.

Eso cambia dónde hay que poner la detección: no en la publicación ni en la negociación, sino en **el uso de la credencial de acceso remoto**, que es el único punto con holgura. Conecta directamente con el eje que la cartera tiene abierto sobre acceso remoto.

## O-4. Clasificación

Triaje de `CTI-2026-042` `Anexo D`: cumple **cuatro criterios de siete**. Sitio de filtración con víctimas nombradas y verificables, infraestructura propia, continuidad temporal de más de seis meses, y portal de negociación declarado —que responde al criterio más discriminante del método: **portal, luego operación y no herramienta**—. Falla en análisis primario con muestra, en víctima confirmada por tercero, y **en infraestructura activa al cierre**.

**Clase: marca con operación, en estado indeterminado.**

### O-4.1 La única corroboración indirecta del perfil

El perfil declara que es un **equipo cerrado y no un programa de afiliados**. Es la única afirmación del perfil que los datos propios apoyan, y lo hacen de forma indirecta pero limpia: **un programa de afiliados produce tandas irregulares**, porque cada afiliado publica cuando termina su propio trabajo, y la suma es irregular por construcción. Los cinco actores restantes del lote tienen al menos una tanda que multiplica por siete su ritmo; éste no tiene ninguna.

Valoramos **probable** *(55–80 %)* que el carácter de equipo cerrado sea correcto. **Es la inferencia mejor apoyada de este expediente**, y no procede del perfil sino de la cadencia.

## O-5. Hipótesis y pre-mortem

**H-1.** *La concentración alemana refleja la vía de acceso y no una selección de objetivo.* **Posible** *(40–60 %)*. Apoyo: no hay concentración sectorial, lo que un actor que elige por capacidad de pago suele mostrar. En contra: Alemania puntúa alto en todos los criterios por los que un actor elegiría.

**H-2.** *El actor ha cesado.* **Posible** *(40–60 %)*. Es `KJ-4`.

**H-3.** *El actor está migrando infraestructura y reaparecerá.* **Posible** *(40–60 %)*. Apoyo: las cinco direcciones caen en bloque, que es lo que hace quien cambia de alojamiento.

**H-4.** *Es un equipo cerrado.* **Probable** *(55–80 %)*. Es `O-4.1`.

**H-5.** *El interruptor de idioma existe.* **Posible** *(40–60 %)*. Es `KJ-6`, y **la hipótesis cuya consecuencia práctica es una recomendación negativa** (`X-2`).

### Pre-mortem

*Si este informe se equivoca, será en `KJ-4`.* El estado de los sitios procede de un campo que se contradice con otro campo de la misma fuente en el 31 % de los casos de este lote, y no hubo verificación independiente. **Si los cinco sitios en realidad responden, el juicio cae entero** y el actor simplemente lleva doce días sin publicar. Está calificado con confianza baja y la reevaluación está fijada.

*El segundo modo de fallo es `KJ-1`.* Si el enriquecedor de la fuente sobreatribuye Alemania —por ejemplo, resolviendo dominios `.de` a Alemania cuando la organización opera en otro país—, la concentración estaría inflada. Con 86 % de cobertura y títulos que son dominios, el riesgo es moderado pero real. Es `I-2`.

---

# NIVEL TÉCNICO

## X-1. El prefijo legible, si reaparece

Las 134 entradas se sirvieron desde una sola dirección:

```
safepaypfxntwixwjrlcscft433ggemlhgkkdupi2ynhtcmvdgubmoyd.onion
```

Los siete primeros caracteres son legibles. Aplicando el método del `Anexo D` de `CTI-2026-057`: prefijo de siete caracteres, dentro del intervalo aprovechable; generación dirigida, no azar; **y única dirección conocida, lo que es la limitación de este caso** — no se puede comprobar si el actor aplicaba la práctica a toda su infraestructura o sólo a la cara pública.

**Valor operativo:** si el actor reaparece —`H-3`— y mantiene la práctica, cualquier dirección nueva que empiece por `safepay` es candidata a ser suya **antes de que publique una sola víctima**. Es la única vigilancia proactiva que este expediente permite, y es barata.

**Condición de caducidad**, por el paso 5 del método citado: la aparición de un sitio suyo sin prefijo. **No hay fecha; hay condición.**

## X-2. El interruptor de idioma, y por qué no se debe convertir en contramedida

El perfil declara que el cifrador **comprueba la configuración regional del sistema y aborta si corresponde a idiomas de Europa del Este**, con base en caracteres cirílicos. Es una práctica documentada en varias familias de programas de extorsión y perfectamente plausible.

De ahí surge una tentación que este informe quiere atajar explícitamente, porque es una contramedida que algunos equipos han adoptado y que **no debe adoptarse**:

**Primer motivo: sólo funcionaría contra un actor.** Una configuración regional elegida para disuadir a este cifrador no tiene efecto sobre los otros cinco actores de este lote, ni sobre Qilin, ni sobre ninguno que no implemente esa comprobación. Es una defensa de alcance uno.

**Segundo motivo, y es el decisivo: depende de que el adversario mantenga una decisión que puede revertir en una compilación.** El interruptor existe —si existe— porque al actor le conviene, no porque esté obligado. Retirarlo cuesta una línea de código y una nueva compilación. **Una defensa que el adversario puede anular unilateralmente y en horas no es una defensa: es una suposición.**

**Tercer motivo, de coste:** cambiar la configuración regional de los sistemas de producción tiene efectos reales sobre ordenación, formatos de fecha, codificación y comportamiento de aplicaciones. Es un coste cierto contra un beneficio hipotético y revocable.

> **Recomendación: no.** Y la lección general, que va más allá de este actor: **una contramedida basada en un comportamiento deliberado del adversario tiene por vida útil el tiempo que el adversario tarde en cambiar de opinión.** Las contramedidas que valen se apoyan en lo que el adversario **necesita** hacer —autenticarse, moverse, extraer datos—, no en lo que elige hacer.

## X-3. Lo que el perfil declara y qué hacer con cada cosa

| Elemento declarado | Qué permite |
|---|---|
| Extensión `.safepay` · nota `readme_safepay.txt` | **Comprobación por la víctima.** Posterior al cifrado: no es detección |
| Credenciales de VPN y RDP robadas como acceso | **El único punto con holgura temporal** (`O-3`). Autenticación resistente a suplantación en todo acceso remoto |
| Permanencia inferior a un día | Si es cierto, **la detección en bitácoras diaria llega tarde**; hace falta alerta, no revisión |
| `ShareFinder.ps1` para reconocimiento | Nombre de guion público y reutilizado. **Débil como indicador**, útil como patrón de comportamiento: enumeración de recursos compartidos desde una cuenta que no suele hacerla |
| WinRAR y Rclone para exfiltración | Herramientas legítimas. **Lo detectable es el volumen y el destino, no el binario** |
| Biblioteca PE32 con marca de tiempo falsificada | Sin hash ni muestra: **nada que detectar** |
| Ofuscación por triple XOR | Detalle de análisis, **sin valor defensivo** |
| Negociación por Tor **y por red TON** | **El elemento más interesante y el menos aprovechable.** Un canal de negociación sobre una cadena de bloques pública implica trazas públicas, pero no hay identificador que seguir |

**De los ocho elementos, dos generan acción —el acceso remoto y el volumen de salida— y ninguno de los dos es específico de este actor.** Es el mismo resultado que en `CTI-2026-057` `§X-2`, y empieza a parecer una regularidad de la serie: **los perfiles de proveedor sin muestra producen inventario, no detección.**

---

## O-7. El aviso conjunto AA26-293A, y qué cambia

<!-- cti:detalle -->

El 20 de octubre de 2026 —veintinueve días antes de que se emitiera la versión 1.0 de este informe, y sin que su redacción lo recogiera— seis agencias publicaron `AA26-293A`, «#StopRansomware: SafePay Ransomware». **Que un expediente de esta cartera se emitiera sin citar un aviso conjunto existente es un fallo de colección propio, y queda consignado como tal** en el `Anexo G`.

**Lo que el aviso añade sobre el actor.** Al menos 600 víctimas de múltiples sectores de infraestructura crítica desde agosto de 2024, en Norteamérica, Sudamérica, Europa y Australia. Acceso inicial por exposición de credenciales, ataques de fuerza bruta y explotación de acceso por VPN —con el detalle operativo de que **los operadores entran desde direcciones del proveedor comercial de VPN «Mullvad»**, usando cuentas obtenidas por phishing—. Cinco CVE, todos en sistemas expuestos a Internet. Movimiento lateral con PsExec, WinRM y RDP. Cifrado híbrido ChaCha20 con RSA y extensión `.SafePay`. Parada de las copias de volumen, reinicio de los NAS a valores de fábrica y, en algunos casos, borrado de todas las copias de seguridad en red.

### O-7.1 Los cinco CVE, y la cautela sobre el producto

El aviso lista cinco identificadores y **no nombra el producto afectado de ninguno**: los da con su CWE y los describe como vulnerabilidades «de productos de dispositivo de borde» (los dos primeros) y «en sistemas expuestos a Internet» (los tres siguientes).

| CVE | CWE | Cómo lo describe el aviso |
|---|---|---|
| `CVE-2020-3259` | CWE-200 | «CVE conocidos de productos de dispositivo de borde» |
| `CVE-2023-20269` | CWE-288 | «CVE conocidos de productos de dispositivo de borde» |
| `CVE-2023-27532` | CWE-306 | Explotación «en sistemas expuestos a Internet» |
| `CVE-2024-40711` | CWE-502 | Explotación «en sistemas expuestos a Internet» |
| `CVE-2024-40766` | CWE-284 | Explotación «en sistemas expuestos a Internet» |

**La cautela:** la correspondencia de estos identificadores con productos concretos —concentradores de acceso remoto, copias de seguridad, cortafuegos— es de dominio público en el registro CVE y en el catálogo de vulnerabilidades explotadas conocidas, **pero no la hace este aviso**. Quien priorice parcheo debe resolver cada identificador contra el registro y no contra este informe ni contra el aviso. Lo que sí se puede afirmar sin añadir nada: **los cinco son de sistemas de cara a Internet, y ninguno requiere que el adversario tenga ya un pie dentro**.

### O-7.2 El eje del acceso remoto, por tercera vez

El vector declarado por el aviso —credencial válida contra VPN, más RDP en el movimiento lateral— coloca a este actor en el mismo eje que la cartera ya había identificado en dos expedientes anteriores. **El dato nuevo y accionable es el de Mullvad:** si los operadores entran por un proveedor comercial de VPN conocido, entonces **el origen del acceso es caracterizable sin conocer al adversario**. Una autenticación correcta desde una dirección de salida de un servicio comercial de VPN, contra un concentrador corporativo y a horas que no corresponden al titular, es una señal construible con lo que cualquier organización ya registra.

**Y la consecuencia defensiva es la que este informe ya daba en `KJ-3` por otra vía:** con retraso mediano de cero días entre fecha declarada y publicación, **no hay semanas de margen**; la detección tiene que estar en el acceso, no en la exfiltración.

## 14. Brechas de inteligencia y requisitos de colección

**G-1. No sabemos si el actor ha cesado o está migrando.** Es `KJ-4`, el juicio más perecedero del lote.
→ **I-1.** Reevaluar el estado de las cinco direcciones y la aparición de entradas nuevas. **Disparador: catorce días, es decir el 3 de diciembre de 2026.** Si reaparece, buscar por el patrón de `X-1`.

**G-2. No sabemos si la concentración alemana es selección o vía de acceso.** Decide si una organización alemana está expuesta por ser alemana o por usar un producto concreto.
→ **I-2.** Comprobar si las 39 entradas alemanas comparten proveedor de acceso remoto, rango de alojamiento o sector. **Disparador:** inmediato; es la pregunta de más valor del expediente.

**G-3. Ninguna de las nueve entradas latinoamericanas está verificada**, incluida la chilena.
→ **I-3.** Verificar el dominio de la entrada chilena y de las cuatro mexicanas.

**G-4. El perfil no está corroborado en ningún punto**, incluido el interruptor de idioma de `KJ-6`.
→ **I-4.** Buscar análisis primario con muestra. **Disparador:** antes de emitir cualquier juicio técnico firme.

**G-5. No se sabe si la práctica del prefijo legible se aplicaba a toda su infraestructura.** De ello depende el alcance de `X-1`.
→ **I-5.** Si reaparece, comprobar si el portal de negociación también lleva prefijo.

**G-6. La captura de pantalla sólo acompaña al 55 % de las entradas** y no se sabe si es decisión del actor o del raspador.
→ **I-6.** Comparar con la cobertura de captura que da el otro rastreador de la cartera para el mismo actor.

---

# ANEXOS

## Anexo A — Indicadores

### A.1 — Infraestructura

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| domain | `safepaypfxntwixwjrlcscft433ggemlhgkkdupi2ynhtcmvdgubmoyd.onion` | **Única dirección de publicación**: sirvió las 134 entradas. **Inactiva al 2026-11-19** | Alta como registro | 90 días | Vigilancia |
| pattern | **Dirección de servicio oculto v3 con prefijo `safepay`** | **La única vigilancia proactiva del expediente** (`X-1`). Sirve para detectar reaparición **antes** de que publique | Alta como método | **Hasta que aparezca un sitio suyo sin prefijo** | **Búsqueda proactiva** |
| artefacto | **5 de 5 sitios inactivos al 2026-11-19, último publicado el 2026-11-07** | `KJ-4`. **Cese o migración, indecidible desde fuera** | **Baja para la interpretación** | **Reevaluar el 2026-12-03** (`I-1`) | Vigilancia |

### A.2 — Comprobables por la víctima, y la recomendación negativa

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| pattern | **Extensión de fichero `.safepay`** | Declarada por el proveedor, **no corroborada**. Posterior al cifrado | **Baja** | Hasta corroboración | **Comprobación por la víctima** |
| filename | `readme_safepay.txt` | Nota de rescate declarada. Misma salvedad | **Baja** | Hasta corroboración | Comprobación por la víctima |
| pattern | **Entrada cuyo título es el dominio, sin enmascarar y sin revisión posterior** | 133 de 134 con dominio, **0 con cambio de título**: este actor no gradúa la presión (`O-2`) | Alta | 90 días | **Comprobación por la víctima** |
| pattern | **Autenticación remota por VPN o RDP con credencial válida robada** | Vector declarado. **El único punto con holgura temporal** si la secuencia completa cabe en 48 h (`O-3`) | Moderada como control | Sin caducidad | **Factor resistente a suplantación en todo acceso remoto** |
| pattern | **Enumeración de recursos compartidos desde una cuenta que no la realiza habitualmente** | `ShareFinder.ps1` declarado. **El nombre del guion es débil; el comportamiento no** | Moderada como control | Sin caducidad | Alerta |
| artefacto | **NO adoptar configuración regional de Europa del Este como contramedida** | **Recomendación negativa explícita** (`X-2`): alcance uno, revocable por el adversario en una compilación, con coste operativo cierto | **Alta como juicio** | Sin caducidad | **No implementar** |

### A.3 — Victimología

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| cartera | **39 de 134 entradas alemanas (29,1 %)** · Estados Unidos sólo 13 | **La anomalía del expediente** (`KJ-1`). Único actor medido donde EE. UU. no es primero | Alta como recuento | 90 días | **Comprobación si opera en el espacio germanófono** |
| cartera | **49 de 134 en Alemania, Suiza y Bélgica (36,6 %)** | El eje completo | Alta como recuento | 90 días | Medición |
| cartera | **1 víctima chilena · 4 mexicanas · 9 LATAM (6,7 %)** | **La única víctima chilena de los seis actores del lote** (`KJ-2`) | **Moderada**: país derivado | 90 días | **Comprobación inmediata del propio dominio** |
| cartera | **29 días de actividad · mediana 3/día · máximo 10** | **El actor más regular del lote** (`O-3`) | Alta | 90 días | Análisis |
| cartera | **Retraso mediano declarado→visto de 0,0 días** | **Sin margen entre acción y publicación.** Lo contrario de `CTI-2026-057` | Alta | 90 días | **Mover la detección al acceso remoto** |
| cartera | **Sin concentración sectorial**: ninguno por encima del 18 % | Debilita la hipótesis de selección por capacidad de pago (`E-2.1`) | Alta como recuento | 90 días | Análisis |
| artefacto | **Una segunda fuente da 618 y 521 víctimas en la misma página** | Y «visto por última vez» en marzo, **la misma fecha que asigna a otros tres actores** (`§3.2`) | Alta como observación | — | — |

### A.4 — Los indicadores de `AA26-293A`, con su titularidad verificada

<!-- cti:ioc -->

> **Antes de leer la tabla.** El aviso declara que sus indicadores se observaron **entre noviembre de 2024 y agosto de 2026** y que «deben interpretarse como infraestructura observada históricamente dentro de la ventana de actividad». **Esa ventana se cerró hace tres meses.** Por tanto, y aplicando la regla de caducidad de esta cartera, **ninguna de las nueve direcciones va a bloqueo hoy, ni siquiera la única calificada como mando y control.** La columna de acción permitida lo refleja. La titularidad se resolvió por `whois` y RDAP contra los registros regionales el **21-11-2026**.

| Tipo | Valor | Titular verificado | Rol que le da el aviso | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|---|
| `artefacto` | `88.119.167.239` | UAB Bacloud (LT) | **«soc.dll command and control»** — **la única calificada como C2** del aviso. **Tipo `artefacto` y no `ipv4` deliberadamente:** su ventana de observación cerró en agosto de 2026, la acción permitida es búsqueda retrospectiva y no bloqueo, y con tipo `ipv4` entraría en el agregado plano, que es una lista de bloqueo | Alta como registro del aviso | **Ventana cerrada en 08-2026** | **Búsqueda retrospectiva en registros. NO bloqueo por antigüedad** |
| `ipv4` | `37.10.71.188` | servinga GmbH (DE) | «Used in exfiltration» | Alta como registro | Ventana cerrada | Búsqueda retrospectiva |
| `ipv4` | `77.37.49.40` | HOSTINGER LT | «SafePay victim intrusion» | Alta como registro | Ventana cerrada | Búsqueda retrospectiva |
| `ipv4` | `167.235.225.149` | Hetzner (`CLOUD-FSN1`) | «Client login panels» | Alta como registro | Ventana cerrada | Búsqueda retrospectiva |
| `artefacto` | `104.26.2.223` | **Cloudflare, Inc.** (`CLOUDFLARENET`) | «SafePay victim intrusion» | **Alta: titularidad verificada** | — | **NUNCA bloqueo.** Red de distribución compartida por millones de sitios |
| `artefacto` | `140.82.114.4` | **GitHub, Inc.** | «SafePay victim intrusion» | **Alta: titularidad verificada** | — | **NUNCA bloqueo.** Bloquearlo rompe el desarrollo de la organización |
| `artefacto` | `185.199.108.133` | **GitHub, Inc.** (GitHub Pages) | «SafePay victim intrusion» | **Alta: titularidad verificada** | — | **NUNCA bloqueo** |
| `artefacto` | `173.194.194.94` | **Google LLC** | «Hosting victim data» | **Alta: titularidad verificada** | — | **NUNCA bloqueo.** Y nótese el rol: **datos de la víctima**, no del adversario |
| `artefacto` | `5.255.11.134` | **YemenNet**, conjunto ADSL (`AS30873`) | «Used in exfiltration» | **Alta: titularidad verificada** | — | **NUNCA bloqueo.** Dirección de acceso residencial, presumiblemente dinámica y hoy de otro abonado |
| `artefacto` | **4 hostnames de equipo** (`WIN-…`) | — | Equipos observados en intrusiones | Moderada | Ventana cerrada | **Búsqueda en inventario propio.** Son nombres por omisión de Windows: coincidencia débil |
| `pattern` | **Acceso inicial desde direcciones de salida del proveedor comercial de VPN «Mullvad»** | — | Vector declarado por el aviso | **Alta como registro del aviso** | Sin caducidad | **Alerta: autenticación correcta desde salida de VPN comercial contra el concentrador corporativo** |

### A.5 — Herramientas del aviso: inventario, no bloqueo

<!-- cti:ioc -->

> **Regla de la casa, y esta vez la suscribe el propio aviso**, que advierte: «estas herramientas y aplicaciones no deben atribuirse como maliciosas sin evidencia analítica». **Ninguna entra en los agregados planos de indicadores.**

| Tipo | Valor | Contexto | Confianza | Acción permitida |
|---|---|---|---|---|
| `herramienta` | **PsExec · WinRM · RDP** | Movimiento lateral con utillaje del sistema | Alta como registro | **Inventario y control de uso. No bloqueo** |
| `herramienta` | **ScreenConnect · AnyDesk · TeamViewer** | El aviso los documenta usados «para transferir el programa dañino al sistema de la víctima» | Alta como registro | **Inventario: ¿están autorizados y quién los usa?** |
| `herramienta` | **7-Zip · WinRAR · FileZilla · RClone · WinSCP · OneDrive · Backblaze (`b2.exe`)** | Compresión y exfiltración | Alta como registro | **Inventario. Alerta por volumen y destino, no por presencia** |
| `herramienta` | **Mimikatz · `ShareFinder.ps1` · `SharpShares.exe` · NetExec (`nxc.exe`) · PowerShell** | Credenciales y descubrimiento. **`ShareFinder.ps1` corrobora el perfil del proveedor** (`KJ-10`) | Alta como registro | **Alerta por comportamiento: enumeración desde cuenta que no la hace habitualmente** |
| `herramienta` | **`nltest.exe` · `netscan.exe` · `dcsync.exe` · `Socks.exe` · CCleaner · AcronisDiskDirector** | Descubrimiento, túnel y borrado de rastro | Moderada | Inventario |
| `pattern` | **`svchost.exe` ejecutándose fuera de `System32`** | El aviso lo marca como sospechoso **sólo en esa condición** | Alta como control | **Alerta.** Sin la condición de ruta es un falso positivo garantizado |
| `pattern` | **Reinicio de NAS a valores de fábrica · parada de copias de volumen · borrado de copias en red** | Destrucción de la capacidad de recuperación | Alta como registro | **Alerta de máxima prioridad: ocurre antes del cifrado** |

## Anexo B — Fuentes y valoración

| # | Fuente | Grado | Qué aportó | Salvedad |
|---|---|---|---|---|
| 1 | API de cti.fyi, entradas y ficha de grupo, 2026-11-19 | **Medición propia** sobre datos de proveedor | Las 134 entradas, los 5 sitios, la victimología y la cadencia | Evaluada en `CTI-2026-054`. **El estado de los sitios procede de un campo que se contradice con otro en el 31 % de los casos** (`E-3`) |
| 2 | Ficha de perfil del grupo, misma fuente | **Proveedor, con indicio de redacción sintética** | El linaje, el vector, el interruptor de idioma de `KJ-6`, el utillaje de `X-3` | **No corroborada en ningún punto.** Ocho de las diez filas de `O-1` proceden de aquí |
| 3 | CTIWatch, ficha pública, 2026-11-19 | Proveedor, **prosa generada automáticamente** | **Nada utilizable**; contraste negativo en `§3.2` | 618 frente a 521 víctimas en la misma página; última actividad en marzo, **idéntica a la de otros tres actores** |
| 4 | `CTI-2026-015` | Propio | El contexto chileno de `E-2.2`: 20 de 30 víctimas chilenas son de Qilin | — |
| 5 | `CTI-2026-057` | Propio | El método de evaluación del prefijo legible de `X-1`, y el contraste de cadencia de `O-3` | Emitido el mismo día |
| 6 | `CTI-2026-048` Anexo D · `CTI-2026-042` Anexo D | Propio | La escala de prueba y el triaje de `O-4` | — |

## Anexo C — Léxico de probabilidad y confianza

ICD 203. **Casi con certeza** ≥99 % · **muy probable** 80–95 % · **probable** 55–80 % · **posible** 40–60 % · **improbable** 20–45 % · **muy improbable** 5–20 %. La **confianza** califica la base de prueba. Aquí: alta para los recuentos; moderada para lo que depende del campo de país; **baja para `KJ-4`**, que es el juicio más perecedero, y **baja para todo elemento del perfil del proveedor**, incluido el interruptor de `KJ-6`.

## Anexo D — Cómo decidir si un actor ha cesado o está migrando

Procedimiento para el caso de `KJ-4`, que se repetirá. Coste: treinta minutos más una espera de catorce días.

**Paso 1 — Comprobar si las direcciones cayeron a la vez o en secuencia.** La caída simultánea de varios servicios ocultos independientes apunta a **abandono deliberado del conjunto**, que es lo que hace quien migra. La caída escalonada apunta a desgaste o a pérdida progresiva de acceso al alojamiento.

**Paso 2 — Comparar el silencio con la cadencia previa.** Doce días no significan lo mismo en un actor que publicaba cada tres días que en uno que publicaba en tandas con huecos de dos meses. **Hay que medir el silencio en unidades de la cadencia propia del actor**, no en días. Aquí doce días son unas cuatro veces su intervalo habitual.

**Paso 3 — Buscar reaparición por patrón antes de concluir.** Si el actor usaba prefijo legible, el patrón permite encontrar infraestructura nueva **sin esperar a que publique**. Es la única comprobación que puede dar un resultado positivo durante el silencio.

**Paso 4 — Comprobar si hay anuncio de autoridad.** Un cese por detención deja rastro oficial, normalmente con días de retraso. Su ausencia no prueba nada; su presencia lo resuelve.

**Paso 5 — Fijar la fecha de decisión antes de empezar a esperar, y qué se concluirá en cada caso.** Sin ese paso, el expediente se queda abierto indefinidamente y el silencio se interpreta como lo que convenga. Aquí: **el 3 de diciembre de 2026**; si no hay publicación ni infraestructura nueva, se reclasifica a **inactivo**; si reaparece, a **migración confirmada**.

> **El paso más importante es el segundo, y es el que casi nunca se hace.** «Lleva doce días sin publicar» no es una observación interpretable por sí sola: lo interpretable es «lleva cuatro veces su intervalo habitual sin publicar». La misma idea que `CTI-2026-046` `Anexo D` aplicó a los rankings de siete días —**una cifra absoluta sin su línea de base no dice nada**—, aplicada aquí al silencio en lugar de a la actividad.
>
> Y el quinto es el que evita el peor resultado posible, que no es equivocarse: es **no concluir nunca**.

## Anexo E — Marcos de referencia empleados

ICD 203. Escala de Almirantazgo con los grados propios de la cartera. TLP 2.0 y PAP. Triaje de actor nuevo de `CTI-2026-042` `Anexo D`. Escala de prueba de ocho niveles de `CTI-2026-048` `Anexo D`. Método de evaluación de prefijo legible de `CTI-2026-057` `Anexo D`. Especificación de servicios ocultos versión 3 de Tor. **No se emite mapa ATT&CK**: el utillaje de `X-3` procede de una ficha de proveedor sin muestra ni referencias, y asignarle técnicas daría a una declaración no corroborada la apariencia de observación.

## Anexo F — Paquete legible por máquina

| Medición | Procedimiento |
|---|---|
| Entradas | `GET /api/v1/posts?group=safepay&since=2026-05-19&limit=500` |
| Infraestructura | `GET /api/v1/groups/safepay` → `locations[]` |
| Concentración | Agrupar `enriched_metadata.country_iso`; Alemania = 39 de 115 con país |
| Cadencia | Agrupar `discovered[:10]` → 29 claves, mediana 3, máximo 10 |
| Retraso | Mediana de `discovered − published` sobre las 102 con ambas fechas → 0,0 días |
| Estado | Campo `site_status` de cada `location`; **contrástese con `available`**, que discrepa en el 31 % de los casos del lote |

## Anexo G — Control de cambios

| Versión | Fecha | Qué cambió | Qué juicio se movió |
|---|---|---|---|
| **1.1** | **2026-11-21** | **Incorpora el aviso conjunto `AA26-293A` (20-10-2026, seis agencias), que la versión 1.0 no citaba pese a ser veintinueve días anterior: fallo de colección propio, consignado como tal** (`KJ-8`, `O-7`). **Corrige `KJ-4`**: la última entrada no es del 7 de noviembre sino **del 12**, corroborada por CYFIRMA, de modo que el silencio era de siete días al cierre de 1.0 y no de doce; y la dirección de publicación vuelve a figurar disponible, por lo que **el escenario por omisión pasa de cese a continuidad**. **Rebaja `KJ-6`** de *posible* a *improbable*: seis agencias con 600 víctimas no documentan el interruptor de idioma, y la ausencia refuerza la recomendación negativa de `X-2`. **Añade `KJ-9`**, hallazgo propio: **cuatro de las nueve direcciones IP del aviso son de Cloudflare, GitHub y Google, y una quinta un conjunto ADSL residencial**, con titularidad verificada por `whois`/RDAP, de modo que una ingesta ciega bloquearía servicios legítimos de uso masivo —el aviso advierte de verificar antes de bloquear, así que el fallo estaría en la ingesta— (`A.4`). **Añade `KJ-10`**: el perfil del proveedor queda corroborado en cinco elementos y sin apoyo en cuatro. Añade `O-7`, `A.4` y `A.5` | **`KJ-4` corregido · `KJ-6` rebajado a improbable · `KJ-7` apoyado en parte por `KJ-10` · `KJ-8`, `KJ-9`, `KJ-10` nuevos.** `KJ-1` gana corroboración indirecta (la policía alemana firma el aviso). **`caduca` NO se extiende: los juicios técnicos no se revalidaron** |
| 1.0 | 2026-11-19 | Emisión inicial. Incluye la concentración alemana del 29 % con Estados Unidos desplazado (`KJ-1`), la única víctima chilena del lote (`KJ-2`), la cadencia más regular de los seis y su consecuencia invertida sobre el margen de detección (`KJ-3`, `O-3`), los cinco sitios caídos (`KJ-4`), y **la recomendación negativa explícita de `X-2`** sobre la contramedida de configuración regional | — |

## Anexo H — Realimentación del consumidor

Este informe se corrige si se recibe: un factor común entre las entradas alemanas, que resolvería `G-2` y convertiría `KJ-1` en accionable para un producto concreto; confirmación de la víctima chilena (`I-3`); un análisis primario con muestra que confirme o niegue el interruptor de idioma de `KJ-6`; o evidencia sobre el estado real del portal que no dependa del campo de disponibilidad de la fuente.

**Dos peticiones de la versión 1.0 quedaron cumplidas el 21-11-2026 y se dejan escritas en lugar de borrarse**, porque el producto de esta cartera es la cadena de razones:

- *«Una entrada nueva publicada después del 7 de noviembre, que reclasificaría el estado.»* **Cumplida: existía ya al emitirse la versión 1.0** —publicada el 12 de noviembre— y no se vio. `KJ-4` corregido.
- *«Evidencia de que alguno de los cinco sitios responde, que invalidaría `KJ-4` entero.»* **Cumplida en parte:** la dirección de publicación figura disponible, pero por el mismo campo de la fuente cuya fiabilidad el propio informe acotó en el 31 % de contradicción. **No se da `KJ-4` por invalidado: se corrige y se rebaja la confianza.**

El disparador con fecha fija es **`I-1`, el 3 de diciembre de 2026**, y la decisión que se tomará en cada caso está escrita en el paso 5 del `Anexo D` para que no quede al criterio del momento.
