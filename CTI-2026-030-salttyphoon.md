---
tlp: "TLP:CLEAR"
pap: "PAP:AMBER"
id: "CTI-2026-030"
version: "1.0.2"
tipo: "Perfil de actor + resolución de una disputa de alias + evaluación de exposición en infraestructura de red"
foco_regional: "Global (EE. UU., Australia, Canadá, Nueva Zelanda y Reino Unido documentados) · Chile y Latinoamérica: exposición directa por tecnología de operador, y una atribución regional errónea que este informe desmonta"
niveles: ["Estratégico", "Operacional", "Táctico", "Técnico"]
actor: "Salt Typhoon · OPERATOR PANDA · RedMike · UNC5807 · GhostEmperor (designaciones que recoge el aviso conjunto AA25-239A)"
fecha: "2026-11-17"
caduca: "2027-02-17"
autor: "Célula CTI"
distribucion: "Elaborado íntegramente con fuentes abiertas TLP:CLEAR, con el aviso conjunto AA25-239A de veintitrés agencias de trece países como fuente principal, leído en original. Difusión libre, conservando la atribución de las fuentes y las salvedades metodológicas de §3."
---

# INFORME DE CIBERINTELIGENCIA — CTI-2026-030

## La pregunta de si Salt Typhoon y FamousSparrow son el mismo actor **sigue abierta**, y en septiembre de 2026 se publicó como resuelta. Este informe documenta por qué no lo está, y quién afirma cada cosa

### Microsoft afirma que son el mismo grupo y **no ha publicado la base técnica**; ESET los rastrea por separado y explica su razonamiento; dos fuentes de noviembre de 2026 dicen que la relación «no está clara». Mientras eso siga así, **ninguna de las dos atribuciones puede usarse como establecida**
#### Y el actor que el aviso conjunto sí describe con precisión es un problema mayor: vive **dentro de los routers de los operadores de telecomunicaciones**, redirige los servidores de autenticación para cosechar credenciales, y **no usa un solo día cero**

> **Regla de oro del producto:** todo párrafo debe responder a un requisito de
> inteligencia (PIR) y habilitar una decisión. Si un párrafo no cambia lo que
> alguien va a hacer, va al anexo o se borra.

---

## 0. Cabecera de control

<!-- cti:meta -->

| Campo | Valor |
|---|---|
| Identificador | `CTI-2026-030` |
| Versión / fecha | `1.0.2` — 2026-11-17 (dos correcciones de verificación previa a la publicación, una de ellas de fondo: véase Anexo G) |
| Tipo de producto | Perfil de actor, más **resolución de una disputa de alias** que esta cartera dejó abierta en `CTI-2026-017` y que un año después produjo una atribución pública errónea, más **evaluación de exposición en infraestructura de red de operador** |
| Niveles cubiertos | Estratégico · Operacional · Táctico · Técnico |
| Foco regional | **Doble, y conviene distinguirlo.** (a) **Exposición real**: el actor ataca el equipamiento de red que operan las telecomunicaciones, el Estado y el transporte de cualquier país, y el aviso lo sitúa en «otras áreas a nivel global». (b) **Atribución regional en disputa**: varias coberturas de septiembre de 2026 publicaron con su nombre la campaña latinoamericana que ESET atribuye al actor de `CTI-2026-017`. **Este informe no decide quién tiene razón: documenta que nadie lo ha decidido y quién afirma qué** |
| Marcado de difusión | `TLP:CLEAR` · `PAP:AMBER` |
| Clasificación interna | Público — apto para difusión abierta |
| Requisitos atendidos | `PIR-01`, `PIR-04`, `PIR-07`, `PIR-10`, `PIR-12`, `PIR-15` |
| Solicitante / consumidor primario | Célula CTI (producción propia) · CISO · **Arquitectura de red** · Jefatura de SOC · Continuidad |
| Ventana de observación | 2021-08-01 → 2026-09-30 |
| Base de colección | 5 fuentes de primera mano, **una de ellas un aviso conjunto de veintitrés agencias de trece países leído en original** · sin telemetría propia |
| Autor (analista) | Célula CTI |
| Revisión por pares | Pendiente |
| Aprobación | Pendiente |
| Caducidad / revisión | 2027-02-17 — 92 días |
| Productos relacionados | **`CTI-2026-017` (FamousSparrow): este informe resuelve su `KJ-7` y debe leerse junto a su revisión v1.2** · **`CTI-2026-028` (UNC3886): el actor con la superficie más parecida —routers, appliances— y la comparación más instructiva de la cartera** · `CTI-2026-022` (Red Akodon: el otro expediente sobre disputa de nombres) · `CTI-2026-027` (Mustang Panda) |
| Paquete legible por máquina | `ioc_index.csv` del repositorio · **el aviso publica además su propio paquete STIX 2.1**, que es la fuente preferente para ingesta automática |

> ⚠ **Limitación estructural.** Sin telemetría propia: §O-4 se entrega como
> cuestionario. Pero este expediente tiene la mejor base documental de los siete
> informes de este lote: **la fuente principal es un aviso oficial conjunto de
> veintitrés agencias de inteligencia y ciberseguridad de trece países, leído
> íntegro y en original**, con mapeo de técnicas, indicadores, reglas de
> detección y consultas de caza publicadas por los propios firmantes.

---

## 1. BLUF — Juicios clave

<!-- cti:kj -->

**KJ-1.** El actor está descrito por **el aviso conjunto más ampliamente respaldado de esta cartera**: `AA25-239A`, publicado el 27 de agosto de 2025 y revisado el 3 de septiembre, firmado por **veintitrés agencias de trece países** —Estados Unidos, Australia, Canadá, Nueva Zelanda, Reino Unido, República Checa, Finlandia, Alemania, Italia, Japón, Países Bajos, Polonia y **España**—. El aviso atribuye la actividad a China y **nombra tres empresas chinas** vinculadas a ella. Valoramos **casi con certeza** *(95–99 %)* la exactitud de estos hechos. **Confianza: alta.** *Base:* documento oficial leído en original.

**KJ-2.** Y aquí está la primera cosa que importa para esta cartera: **el aviso no usa el nombre «Salt Typhoon» como designación propia.** Se refiere a «actores APT» y enumera, como nombres de la industria para el mismo conjunto de actividad, cinco designaciones: `Salt Typhoon`, `OPERATOR PANDA`, `RedMike`, `UNC5807` y **`GhostEmperor`**. Valoramos **casi con certeza** *(95–99 %)* que esa lista sea la del aviso. **Confianza: alta.** *Base:* lectura literal.

**KJ-3.** **La fusión de los dos actores no requiere ninguna inferencia: Microsoft la afirmó directamente.** Según coberturas de prensa, Microsoft declaró al *Wall Street Journal* que **`Salt Typhoon`, `FamousSparrow` y `GhostEmperor` son el mismo grupo**, y —esto es lo decisivo— **no ha publicado indicadores técnicos, tácticas ni explicación alguna que sostenga esa atribución**. ESET lo recoge así expresamente y lo disputa. Valoramos **muy probable** *(80–95 %)* que ésta sea la vía principal por la que la equivalencia circula. **Confianza: moderada.** *Base:* la afirmación de Microsoft y su falta de respaldo técnico están recogidas por ESET y por múltiples coberturas; **no se ha leído la declaración original de Microsoft** (§3.3-xi).

Hay además una **segunda vía, que refuerza la primera y que esta cartera puede documentar con precisión**: el aviso oficial `AA25-239A` sitúa `GhostEmperor` entre los nombres de industria de este actor, y `CTI-2026-017` recoge desde su emisión original que `GhostEmperor` tiene con FamousSparrow un **solapamiento parcial acotado** —una vulnerabilidad común y **una dirección IP** en 2021—. Componer las dos afirmaciones vuelve a dar «FamousSparrow = Salt Typhoon», y **esa composición sí es inválida**: compone un solapamiento parcial con una equivalencia. Valoramos **posibilidad real** *(45–55 %)* de que esta segunda vía haya contribuido. **Confianza: baja.** *Base:* los dos pasos están documentados, pero **la identificación de la composición como causa es nuestra y ninguna fuente la enuncia**; y dado `KJ-3`, la composición **no es necesaria** para explicar el resultado. Se conserva porque la **regla** que se extrae de ella es válida con independencia de que fuera o no la causa aquí: véase el Anexo D.

**KJ-4.** **La consecuencia que `CTI-2026-017` anticipó se materializó, pero no en la forma en que ese informe —ni la primera redacción de éste— la describió.** En septiembre de 2026, tras el análisis de ESET sobre la campaña latinoamericana de FamousSparrow y su implante `SparroWocky`, varias coberturas de prensa especializada la publicaron **bajo el nombre «Salt Typhoon»**, con el 90 % de objetivos latinoamericanos y los ocho países.

Y aquí hay que ser preciso, porque es fácil equivocarse en los dos sentidos: **esas coberturas no inventaron la equivalencia — adoptaron la taxonomía de Microsoft**, que la afirma. Lo que hicieron fue **presentar como establecida una identidad que no lo está**, y omitir que el proveedor que realizó el análisis atribuye la campaña a otro actor.

Valoramos **probable** *(55–80 %)* que la equivalencia **no esté establecida en ninguna de las dos direcciones**, y **poco probable** *(20–45 %)* que FamousSparrow y este actor sean el mismo conjunto de actividad. **Confianza: moderada.** *Base:* ESET, que hizo el análisis, los rastrea por separado y publica su razonamiento —uso exclusivo de `SparrowDoor` y solapamiento de código—; Microsoft afirma la identidad **sin publicar base técnica**; y **dos fuentes independientes de noviembre de 2026 —Check Point y una cobertura técnica del mismo ecosistema— declaran expresamente que la naturaleza de la relación «no está clara»**. Tres fuentes de 2026 coinciden en que la cuestión sigue abierta.

> ⚠ **Nota de verificación previa a la publicación.** La primera redacción de este
> juicio afirmaba «casi con certeza» que la atribución de prensa era *incorrecta*.
> **Era insostenible**: si Microsoft afirma la identidad, usar su nombre no es un
> error de la prensa sino la adopción de una taxonomía en disputa. El juicio se ha
> degradado a lo que las fuentes sostienen —que la cuestión está abierta— y la
> corrección se consigna en el Anexo G.

**KJ-5.** El actor real hace algo peor que lo que se le atribuyó por error: **vive dentro del equipamiento de red de los operadores de telecomunicaciones y manipula los sistemas que autentican el acceso a ese equipamiento.** El aviso documenta tres procedimientos que conviene leer juntos: modifica las listas de control de acceso de los routers **para incluir sus propias direcciones**; captura tráfico en el propio dispositivo para **cosechar autenticaciones de TACACS+ y RADIUS**; y **modifica la configuración del servidor TACACS+ para redirigir las credenciales a una dirección suya**. Valoramos **casi con certeza** *(95–99 %)* la exactitud de estos procedimientos. **Confianza: alta.** *Base:* aviso oficial con comandos literales publicados.

**KJ-6.** El modelo de recolección no es el de un espía que busca documentos: es el de **un sistema de interceptación construido sobre la infraestructura de otros.** El aviso describe el uso de túneles **GRE, mGRE e IPsec** desde los dispositivos comprometidos, y en al menos un caso **GRE y MPLS para extraer datos hacia China**. Es decir: el actor no exfiltra ficheros, **se conecta a la red de la víctima como si fuera una extensión de la suya**. Valoramos **muy probable** *(80–95 %)* que ésta sea la lógica de la operación. **Confianza: moderada.** *Base:* los mecanismos están en el aviso; la caracterización como sistema de interceptación es interpretación nuestra, apoyada en el propio título del aviso, que habla de «alimentar un sistema global de espionaje».

**KJ-7.** No usa días cero. El aviso lo dice expresamente: **no se observaron vulnerabilidades de día cero.** Los cinco CVE de acceso inicial que enumera estaban todos publicados y parcheados: dos de Cisco IOS XE, uno de Ivanti, uno de Palo Alto y **uno de Cisco de 2018**. Valoramos **casi con certeza** *(95–99 %)* la exactitud de esto. **Confianza: alta.** *Base:* afirmación explícita del aviso. **Y es el juicio de mayor valor práctico del informe**: significa que la exposición es de gestión de parches en el borde de la red, no de capacidad adversaria.

**KJ-8.** La escala declarada por la autoridad investigadora es de otro orden que la de cualquier otro actor de esta cartera: **al menos doscientas empresas en más de ochenta países**, según la estimación del FBI de agosto de 2025, y en febrero de 2026 la misma autoridad declaró la amenaza **todavía en curso**. Valoramos **probable** *(55–80 %)* que las cifras sean del orden correcto. **Confianza: moderada.** *Base:* declaración de autoridad estatal recogida por vía secundaria; **el aviso oficial leído no contiene esas cifras**, y por tanto no están corroboradas por la fuente principal.

**KJ-9.** Nuestra exposición es directa y es de inventario, no de victimología. No hay ningún caso chileno documentado atribuido a este actor —y los que la prensa le atribuyó pertenecen a otro—. Pero **los cinco CVE afectan a productos que operan las telecomunicaciones, el Estado, la banca y el transporte de la región**, y uno de ellos es de 2018. El aviso enumera además otros fabricantes cuyo equipamiento podría estar afectado. Valoramos **posibilidad real** *(45–55 %)* de que exista en la región equipamiento de borde vulnerable a alguno de esos cinco CVE y accesible desde Internet. **Confianza: moderada.** *Base:* los CVE son públicos y antiguos; la inferencia sobre el estado del parque regional es nuestra y se apoya en la misma observación que `CTI-2026-028` hace sobre el equipamiento fuera de soporte.

**Qué cambiaría estos juicios:** una rectificación pública de las coberturas que atribuyeron la campaña de `SparroWocky` a este actor, o —en dirección contraria— un análisis que estableciera que `GhostEmperor` y FamousSparrow son efectivamente el mismo conjunto de actividad, lo que convertiría la composición de `KJ-3` en válida y obligaría a reescribir tanto este informe como `CTI-2026-017`. Son los indicadores `I-1` e `I-2` de §O-7.

---

## 2. Resumen ejecutivo

Este informe hace dos cosas, y la primera es un ajuste de cuentas con nuestro propio producto.

En septiembre de 2026, `CTI-2026-017` advirtió que fusionar FamousSparrow con Salt Typhoon «parece un detalle de nomenclatura y no lo es», y que hacerlo produciría «una cobertura nominal alta y una cobertura real nula». Ese informe dejó el asunto consignado como juicio `KJ-7`: la disputa seguía sin resolverse y tenía consecuencias.

**Las tuvo.** Ese mismo mes, cuando ESET publicó su análisis de la campaña latinoamericana de FamousSparrow y de su implante `SparroWocky` —el 90 % de objetivos en la región, ocho gobiernos comprometidos—, varias coberturas de prensa especializada publicaron esa campaña bajo el nombre de **Salt Typhoon**. Lo pusieron en los titulares.

**Y aquí hay que ser más cuidadoso de lo que fue la primera redacción de este informe**, que afirmaba que la prensa se había equivocado. No es eso lo que ocurrió. Esto es lo que se puede documentar:

- **Microsoft afirma que `Salt Typhoon`, `FamousSparrow` y `GhostEmperor` son el mismo grupo.** Lo declaró a un diario de ámbito económico, y **no ha publicado ni un indicador, ni una táctica, ni una explicación de esa atribución**. Lo recoge así, expresamente, el propio ESET.
- **ESET los rastrea por separado, y publica su razonamiento**: el uso exclusivo de un implante propio y el solapamiento de código con muestras que ya había documentado. Los solapamientos con herramientas de terceros los explica por un suministrador compartido — al que llama, con el mismo término que Check Point usaría después, un «intendente digital».
- **Check Point, el 10 de noviembre de 2026, dice que «los detalles de ese vínculo no están claros».** Y una cobertura técnica del mismo ecosistema dice, el mismo mes, que «la naturaleza precisa de la relación sigue sin estar clara».
- **El aviso oficial no se pronuncia**: `FamousSparrow` no figura entre los cinco nombres de industria que enumera.

Entonces las coberturas de septiembre de 2026 no inventaron la equivalencia: **adoptaron la taxonomía de Microsoft**. Lo que hicieron fue **presentarla como establecida cuando no lo está**, y omitir que el proveedor que hizo el análisis atribuye la campaña a otro actor.

**La lección es distinta de la que pensábamos, y es más útil: una atribución sin base publicada no es una atribución utilizable, por autorizada que sea la fuente.** Microsoft tiene telemetría que nadie más tiene y puede estar viendo algo real. Pero mientras no publique nada, su afirmación **no se puede verificar, refutar ni convertir en una regla de detección**. La asimetría entre las dos posiciones no está en quién tiene razón: está en **quién permite comprobarlo**.

Hay una segunda lección, secundaria, y conviene decir por qué es secundaria. El aviso oficial enumera `GhostEmperor` entre los nombres de este actor, y `CTI-2026-017` recoge que `GhostEmperor` se solapa **parcialmente** con FamousSparrow —una vulnerabilidad y una dirección IP en 2021—. Componer las dos cosas vuelve a dar la equivalencia, y **esa composición es inválida: un solapamiento parcial no es transitivo**. La primera redacción de este informe presentó esa cadena como el hallazgo central. **La verificación previa a la publicación encontró que existe una explicación más simple y documentada —Microsoft afirmándolo directamente— y que la cadena no era necesaria.** Se conserva como advertencia, no como diagnóstico, y la corrección está en el Anexo G.

La segunda cosa que hace este informe es describir al actor real, y conviene decir que es un problema mayor que el que se le atribuyó por equivocación.

Salt Typhoon no busca documentos en ordenadores de oficina. **Vive dentro de los routers de los operadores de telecomunicaciones.** El aviso documenta tres cosas que hace una vez dentro, y hay que leerlas juntas para ver la lógica: modifica las listas de control de acceso del router **para incluir sus propias direcciones**, de modo que su tráfico pase a estar autorizado; activa la captura de paquetes **en el propio dispositivo** para recoger las autenticaciones de TACACS+ y RADIUS que pasan por ahí; y **cambia la configuración del servidor TACACS+ para que las credenciales se envíen a una dirección suya**. En al menos un caso, el secreto compartido de TACACS+ estaba guardado con un cifrado reversible de Cisco, lo que lo hace recuperable.

Y después no exfiltra ficheros: **monta túneles**. GRE, mGRE, IPsec, y en al menos un caso GRE sobre MPLS para llevar datos hacia China. No se lleva una copia de la información: se conecta a la red de la víctima como si fuera una extensión de la suya. El propio aviso lo dice en su título: esto alimenta un sistema global de espionaje.

**Hay un dato que cambia por completo la lectura defensiva, y es la mejor noticia del informe: no usa días cero.** El aviso lo afirma expresamente. Los cinco CVE de acceso inicial que enumera estaban todos publicados y con parche disponible, y **uno de ellos es de 2018**. Dos son de Cisco IOS XE, uno de Ivanti, uno de Palo Alto.

Eso significa que la exposición a este actor no es un problema de capacidad adversaria frente a la que estemos indefensos. **Es un problema de gestión de parches en el borde de la red**, que es exactamente el mismo hallazgo que `CTI-2026-028` produjo desde otra dirección. Dos actores distintos, de dos informes distintos, apuntando al mismo inventario sin dueño: el equipamiento de red que nadie parchea porque nadie quiere reiniciarlo.

Para Chile no hay un solo caso documentado atribuido a este actor, y los que la prensa le atribuyó son de otro. Pero los cinco CVE afectan productos que operan nuestras telecomunicaciones, nuestro Estado, nuestra banca y nuestro transporte. La decisión que pedimos es la más concreta de todo el lote: **comprobar si esos cinco CVE están cerrados en nuestro equipamiento de borde, y en el de quien nos presta conectividad.**

<!-- cti:cards -->

| Rasgo | Qué significa | Etiqueta |
|---|---|---|
| El aviso lo firman 23 agencias de 13 países | **La mejor base documental de esta cartera**, con comandos, indicadores y reglas publicados por los firmantes | `01 · respaldo` |
| Microsoft afirma que es el mismo actor que FamousSparrow | **Y no ha publicado ni un indicador que lo sostenga.** ESET lo disputa con razonamiento publicado | `02 · alias` |
| La campaña de `SparroWocky` se publicó con su nombre | **No es un invento de la prensa: es la taxonomía de Microsoft presentada como establecida.** Tres fuentes de 2026 dicen que no lo está | `03 · disputa abierta` |
| Modifica las ACL del router para incluirse | Su tráfico pasa a estar **autorizado por la configuración de la víctima** | `04 · autorización` |
| Redirige el servidor TACACS+ | Las credenciales de administración de la red van a su dirección. **Cosecha el acceso, no los datos** | `05 · credenciales` |
| Monta túneles GRE, mGRE e IPsec | No exfiltra: **se conecta a la red de la víctima como extensión de la suya** | `06 · interceptación` |
| **No usa días cero** | Cinco CVE públicos, uno de 2018. **La exposición es de parcheo, no de capacidad** | `07 · parcheo` |
| 200 empresas en 80 países, según el FBI | Y declarada **todavía en curso** en febrero de 2026. *Cifra no corroborada por el aviso* | `08 · escala` |

<!-- cti:stats -->

| Cifra | Qué mide | Contexto |
|---|---|---|
| `23` | Agencias firmantes del aviso conjunto | De **13 países**, incluida España. Sin precedente en esta cartera |
| `5` | Designaciones de industria que el aviso enumera para el mismo actor | `Salt Typhoon`, `OPERATOR PANDA`, `RedMike`, `UNC5807` y **`GhostEmperor`** |
| `3` | Empresas chinas nombradas en el aviso | Con razón social completa, en inglés y en chino |
| `5` | CVE de acceso inicial, **todos con parche disponible** | Y **cero días cero observados**. Es `KJ-7` |
| `2018` | Año del más antiguo de esos cinco CVE | Cisco Smart Install. **Ocho años con parche** |
| `84` | Direcciones IPv4 publicadas en el aviso, más 2 IPv6 | Observadas entre agosto de 2021 y junio de 2025. **El aviso advierte que pueden no estar vigentes** |
| `4` | Herramientas propias con hash publicado | Clientes de transferencia en Go y ELF, con sus rutas de compilación filtradas |
| `2021` | Año desde el que el aviso sitúa la actividad, «al menos» | — |
| `200` | Empresas comprometidas según la estimación del FBI de agosto de 2025 | En **más de 80 países**. *No está en el aviso oficial leído* |
| `0` | Indicadores técnicos publicados por quien afirma que los dos actores son el mismo | **Cero. Es el dato que estructura §O-1 y la comprobación `D-0` del Anexo D** |
| `3` | Fuentes de 2026 que declaran que la relación con FamousSparrow **no está establecida** | ESET, Check Point y una cobertura técnica del mismo ecosistema |

<!-- cti:note type="good" -->

> ✅ **Decisiones que se solicitan a Dirección.** (a) **Verificar los cinco CVE del Anexo A.1 en todo el equipamiento de borde propio**, y preguntar formalmente por ellos a los proveedores de conectividad y de servicios gestionados. **Es la decisión más concreta y de mayor rendimiento de todo el lote de noviembre de 2026**, porque la exposición es de parcheo y no de capacidad — 30 días. (b) **Endurecer la configuración de los dispositivos de red según las mitigaciones del aviso**: desactivar Smart Install y la interfaz web no cifrada, desactivar el intérprete de contenedor del dispositivo donde no se use, migrar a SNMPv3 con autenticación y cifrado retirando las comunidades por defecto, y cerrar las listas de control de acceso con una denegación final registrada — 60 días. (c) **Tratar el servidor TACACS+ o RADIUS con el escrutinio de un controlador de dominio**, y **migrar sus secretos y las credenciales locales de los dispositivos a los formatos de cifrado no reversibles** que el aviso recomienda. En al menos un caso documentado el secreto estaba en un formato reversible — 60 días. (d) **Comparar la configuración de cada dispositivo de red contra su versión autorizada**, de forma periódica y automática: es la primera caza que recomienda el aviso y la que detecta una ACL modificada — 90 días. (e) **Instruir por escrito la regla de no transitividad de los alias** (Anexo D) y aplicarla a los expedientes abiertos de la cartera. Coste cero y evita el error que este informe documenta — 15 días. (f) **Ingerir el paquete STIX del propio aviso** en lugar de los indicadores reempaquetados de este informe, por la razón del Anexo A — 30 días.

---

## 3. Alcance, requisitos y limitaciones

**3.1 Requisitos de inteligencia atendidos**

| Req. | Enunciado | ¿Respondido? | Dónde |
|---|---|---|---|
| PIR-01 | ¿Qué actores tienen intención y capacidad contra nuestro sector y geografía? | **Parcialmente**: capacidad y alcance global documentados; sin caso regional atribuido correctamente | `KJ-8`, `KJ-9`, §E-2 |
| PIR-04 | ¿Qué amenazas operan contra la región hispanohablante? | **Ninguna de este actor documentada correctamente.** Y se desmonta una atribución errónea | `KJ-4`, §E-2 |
| PIR-07 | ¿Qué técnicas invalidan nuestros controles actuales? | **Sí**: modificar la ACL del router y redirigir el servidor de autenticación convierte el control de acceso en un control del adversario | `KJ-5`, §O-3 |
| PIR-10 | ¿Está vigente y es fiable la inteligencia de la que dependemos? | **Sí, y es el eje del informe**: se identifica el mecanismo de un error de atribución que llegó a titulares | `KJ-3`, `KJ-4`, Anexo D |
| PIR-12 | ¿Qué vulnerabilidades explotadas activamente tenemos expuestas? | **Sí — cinco, todas con parche, y es la decisión `E-a`** | `KJ-7`, Anexo A.1 |
| PIR-15 | ¿Qué exposición tenemos en equipamiento de red y fuera de soporte? | Sí, y converge con `CTI-2026-028` | `KJ-9`, §O-4 |
| — | ¿Estamos ya comprometidos? | **No evaluable** — y, como en `CTI-2026-028`, la superficie no admite agente | §O-4, `G-1` |

**3.2 Fuera de alcance.** No se evalúa: la actividad de este actor contra operadores estadounidenses concretos, ampliamente cubierta en prensa y que no aporta a ninguna decisión nuestra; la relación con el clúster que la inteligencia de Google desmanteló en 2026 bajo designación propia y del que **esa misma fuente afirma expresamente no ver solapamiento con este actor** —se consigna en §O-1 precisamente por eso—; la evaluación de las tres empresas chinas nombradas, que es materia de sanciones y de cumplimiento; el contenido del paquete STIX que el aviso publica, que no se descargó; y la respuesta a un compromiso consumado en equipamiento de red, que exige procedimiento específico del fabricante.

**3.3 Limitaciones de la colección.** (i) **La fuente principal se leyó íntegra y en original, y eso es excepcional en este lote** — con una salvedad metodológica que merece registro: los resúmenes automáticos de las dos primeras lecturas del aviso **contradecían su propio texto literal**, afirmando que no contenía firmantes, empresas nombradas ni lista de direcciones, cuando sí los contiene. **Todo este informe se construyó sobre el texto literal**, y la discrepancia se consigna porque es un caso instructivo de cómo se degrada la información al resumirse. (ii) **Las cifras de doscientas empresas y más de ochenta países no están en el aviso**: provienen de declaraciones del FBI recogidas por vía secundaria. `KJ-8` lo refleja con confianza moderada. (iii) **El aviso no publica dominios**, sólo direcciones. (iv) **El aviso advierte expresamente que sus direcciones pueden no estar vigentes** y que deben verificarse antes de bloquearlas; el Anexo A hereda esa advertencia. (v) **No se descargó el paquete STIX** que el aviso enlaza, que puede contener indicadores adicionales. (vi) **No se publican hashes MD5 de dos de las cuatro herramientas**, y el aviso no da versiones afectadas por producto para los CVE. (vii) **La atribución del error de septiembre de 2026 a coberturas de prensa se conoce por los titulares y los resúmenes de esas coberturas**, no por su lectura íntegra; `KJ-4` descansa en que ESET, que hizo el análisis, lo atribuye a otro actor. (viii) **La identificación de `GhostEmperor` como eslabón de la fusión es nuestra**, no de ninguna fuente, y se declara como tal en `KJ-3`. (ix) Una fuente de proveedor afirma actividad de este actor contra telecomunicaciones sudamericanas con tres implantes nombrados; **no se pudo verificar contra ninguna fuente primaria y uno de esos nombres aparece en el expediente de `CTI-2026-017` v1.2 asociado a otro ecosistema.** No se sostiene aquí y se consigna como brecha `G-4`. (x) **El aviso contiene al menos una errata tipográfica** en su propia sección de caza, que se señala en §T-4 para que nadie copie el comando mal. (xi) **No se ha leído la declaración original de Microsoft** que afirma la identidad de los tres actores: se conoce por su recogida en el análisis de ESET y por coberturas de prensa que la atribuyen a una entrevista con un diario de ámbito económico. `KJ-3` lo refleja con confianza moderada. **Es la brecha `G-11`, y es la que decidiría toda la cuestión de §O-1.** (xii) **No se han leído íntegros los dos análisis de 2026 que declaran la relación «no clara»**: se conocen por sus resúmenes, que los citan literalmente.

**3.4 Metodología.** Disciplinas: **OSINT oficial multilateral** (aviso conjunto de veintitrés agencias de trece países, leído íntegro y en original, con mapeo de técnicas, indicadores, reglas YARA y Snort y consultas de caza publicadas por los firmantes), OSINT oficial estatal por vía secundaria (declaraciones del FBI), OSINT comercial de primera mano (el análisis de ESET sobre el actor de `CTI-2026-017`, usado aquí para la separación de `KJ-4`), **y análisis de productos propios**: la resolución de `KJ-3` se obtiene cruzando el aviso con el expediente de alias de `CTI-2026-017`, lo que sólo es posible porque ese informe documentó el solapamiento con `GhostEmperor` y lo calificó de parcial. Técnicas analíticas estructuradas: análisis de hipótesis competidoras sobre la identidad del actor y sobre la causa del error de atribución (§O-6), comprobación de supuestos clave, pre-mortem. Marcos: MITRE ATT&CK v17 —la versión que declara el aviso y que este informe conserva—, MITRE D3FEND, Pirámide del Dolor, Cadena de Intrusión, ICD 203, código Admiralty.

---

# NIVEL ESTRATÉGICO
### Para: Consejo · CISO · **Arquitectura de red** · Riesgo · Gestión de Vulnerabilidades · Horizonte: 6–24 meses

## E-1. Qué representa este actor, y qué representa el error que se cometió con él

Hay dos hallazgos en este informe y conviene no mezclarlos.

**El primero es sobre nuestro oficio.** En septiembre de 2026, `CTI-2026-017` dejó por escrito que fusionar FamousSparrow con Salt Typhoon produciría «una cobertura nominal alta y una cobertura real nula», y lo consignó como juicio pendiente. Ese mismo mes, varias coberturas de prensa especializada atribuyeron a Salt Typhoon la campaña latinoamericana de FamousSparrow. **El informe acertó en el pronóstico y no sirvió para evitar nada**, porque la predicción estaba en nuestro producto y el error lo cometieron otros.

Lo que este informe añade es el **mecanismo**, y el mecanismo es generalizable. El aviso oficial enumera `GhostEmperor` entre los nombres de industria de este actor. `CTI-2026-017` recoge que `GhostEmperor` se solapa **parcialmente** con FamousSparrow: compartieron una vulnerabilidad y **una dirección IP en 2021**. Componer las dos afirmaciones da «FamousSparrow = Salt Typhoon», y la composición es inválida.

Enunciado como regla: **un solapamiento parcial no es transitivo.** Si A se solapa parcialmente con B, y B es un alias de C, no se sigue que A sea C. Esta es la tercera forma del mismo error que la cartera documenta —`CTI-2026-022` con nombres de un actor regional, `CTI-2026-017` v1.2 con un implante tomado por actor, y ahora ésta—. El Anexo D la convierte en lista de comprobación.

**El segundo hallazgo es sobre el actor**, y es que su problema es mayor que el que se le atribuyó por error.

Los seis informes anteriores de este lote describen adversarios que entran en equipos para sacar información de ellos. Este describe algo distinto: **un actor que se instala en la infraestructura que transporta la información de todos los demás.** La diferencia no es de grado. Un adversario en un servidor ve lo que hay en ese servidor; un adversario en el router de un operador, con la capacidad de modificar sus listas de acceso y de redirigir su servidor de autenticación, está en posición de ver **lo que pasa por ahí** — y lo que pasa por ahí es el tráfico de los clientes del operador.

Y hay un rasgo que lo distingue de `CTI-2026-028`, que es el actor más parecido de la cartera:

| | `CTI-2026-028` UNC3886 | **`CTI-2026-030` Salt Typhoon** |
|---|---|---|
| Superficie | Hipervisores, appliances, routers fuera de soporte | **Routers y appliances de operador** |
| Acceso inicial | Días cero propios, seis documentados | **Ningún día cero. Cinco CVE públicos con parche** |
| Objetivo del acceso | Persistencia sigilosa y recolección | **Credenciales de administración de red y tráfico en tránsito** |
| Exfiltración | Canales propios y Tor | **Túneles GRE, mGRE, IPsec y MPLS** |
| Respaldo documental | Un proveedor, un marco, un Estado en su propio caso | **23 agencias de 13 países** |
| Qué nos exige | Inventario y visibilidad | **Parcheo, y es más barato** |

La columna que importa es la segunda fila. **UNC3886 exige capacidad defensiva que casi nadie tiene; Salt Typhoon exige parchear cinco CVE publicados, uno de ellos de 2018.** Son dos actores de capacidad comparable y exposiciones de coste radicalmente distinto.

<!-- cti:cards -->

| Cambio estructural | Por qué nos afecta | Etiqueta |
|---|---|---|
| El adversario se instaló en la infraestructura de tránsito | No ve lo que hay en un servidor: ve lo que pasa por la red. **Nuestra confidencialidad depende del parcheo de un tercero** | `01 · tránsito` |
| La lista de control de acceso pasó a ser del adversario | Modifica la ACL para incluirse. **El control de acceso del dispositivo se convierte en su autorización** | `02 · autorización` |
| El servidor de autenticación de red es un objetivo de primer orden | Redirigirlo entrega las credenciales de administración de toda la red. **Y casi nadie lo vigila como un controlador de dominio** | `03 · credenciales` |
| La exfiltración se volvió conectividad | Túneles en lugar de transferencias. **No hay un volumen anómalo de salida que detectar** | `04 · canal` |
| Sin días cero: cinco CVE públicos | **La mejor noticia del lote.** La exposición es de gestión de parches en el borde | `05 · parcheo` |
| Un alias en un aviso oficial produjo una atribución falsa en titulares | **La composición de un solapamiento parcial con una equivalencia es inválida**, y hay que escribirlo como regla | `06 · tradecraft` |

## E-2. Victimología

> ⚠ **Esta sección tiene dos tablas porque el expediente tiene dos
> victimologías: la que el aviso oficial documenta, y la que se le atribuyó por
> error. Separarlas es el objeto de `KJ-4`.**

<!-- cti:bars title="Sectores que el aviso oficial declara" -->

| Sector | En el aviso |
|---|---|
| Telecomunicaciones | `sí` |
| Gobierno | `sí` |
| Transporte | `sí` |
| Alojamiento (*lodging*) | `sí` |
| Redes de infraestructura militar | `sí` |
| Proveedores de acceso a Internet extranjeros | `sí` |

<!-- cti:bars title="Geografía que el aviso oficial declara, desde al menos 2021" -->

| País o región | En el aviso |
|---|---|
| Estados Unidos | `sí` |
| Australia | `sí` |
| Canadá | `sí` |
| Nueva Zelanda | `sí` |
| Reino Unido | `sí` |
| «Otras áreas a nivel global» | `sí, sin enumerar` |
| **Latinoamérica, Chile** | **no mencionados** |

<!-- cti:note type="warn" -->

> ⚠ **Lo que NO es victimología de este actor, y se le atribuyó.** La campaña de
> `SparroWocky` con el 90 % de objetivos latinoamericanos y entidades
> gubernamentales en Argentina, Ecuador, Guatemala, Honduras, Panamá, Perú,
> Puerto Rico y Venezuela **pertenece al actor de `CTI-2026-017`**, que es quien
> la analizó la atribuye, y que rastrea a los dos actores por separado.
>
> La diferencia no es de etiqueta: es de modelo de amenaza. Uno es un actor de
> **implante de punto final sobre servidores expuestos**; el otro vive **dentro
> del equipamiento de red de los operadores**. Quien importe las detecciones de
> este informe creyendo que cubren esa campaña no cubrirá nada, y al contrario.
> Es literalmente lo que `CTI-2026-017` advirtió que pasaría.
>
> **Y una tercera confusión que conviene cerrar aquí**: una fuente de proveedor
> afirma actividad de este actor contra telecomunicaciones sudamericanas con tres
> implantes nombrados, y **uno de esos nombres aparece en el expediente de
> `CTI-2026-017` v1.2 asociado a un ecosistema distinto**. No se pudo verificar
> contra ninguna fuente primaria y **no se sostiene en este informe**. Brecha
> `G-4`.

**Lo que sí nos alcanza.** Ninguna de las dos tablas de arriba nos incluye, y eso es el dato. Lo que nos alcanza es `KJ-9`: **los cinco CVE de acceso inicial afectan a productos que operan las telecomunicaciones, el Estado, la banca y el transporte de esta región**, y el aviso enumera además otros seis fabricantes cuyo equipamiento podría estar afectado. Esa exposición no depende de que este actor nos mire: depende de que el equipamiento esté parcheado, y la pregunta se responde en una semana.

## E-3. Tendencia y pronóstico

<!-- cti:chart title="Hitos documentados por periodo" cap="Cuenta publicaciones oficiales y de autoridad, no víctimas. La actividad declarada es continua desde 2021; la serie mide cuándo se hizo pública." -->

| Periodo | Hitos |
|---|---|
| `2021–2023` | `1` |
| `2024` | `2` |
| `2025-H1` | `1` |
| `2025-H2` | `3` |
| `2026` | `2` |

<!-- cti:cards -->

| Escenario | Desarrollo | Etiqueta |
|---|---|---|
| Continuidad en infraestructura de operador | El actor sigue dentro de equipamiento de red de telecomunicaciones y de proveedores de acceso, con acceso inicial por CVE públicos sin parchear. **Escenario base, y la respuesta es la decisión `E-a`** | `Probable · 55–80 %` |
| Persistencia del error de atribución | Las coberturas que fusionaron los dos actores **no se rectifican**, y la fusión se consolida en perfiles de proveedor, agregadores y bases de conocimiento. **Es el escenario más probable y el que degrada nuestra inteligencia** | `Probable · 55–80 %` |
| Caso documentado en infraestructura de operador latinoamericano | Por aparición de telemetría o por comunicado de un Estado de la región. Convertiría `KJ-9` en exposición concreta | `Posibilidad real · 45–55 %` |
| Revisión del aviso con nuevos CVE o nuevos indicadores | El aviso ya tuvo una revisión a los siete días de publicarse. Es un documento vivo | `Posibilidad real · 45–55 %` |
| Resolución pública de la equivalencia con `GhostEmperor` | Un análisis que establezca si `GhostEmperor` es el mismo conjunto que FamousSparrow, o no. **Resolvería `KJ-3` en una dirección u otra y obligaría a revisar dos informes** | `Poco probable · 20–45 %` |
| Uso de días cero por este actor | No observados hasta ahora según el aviso. Cambiaría la economía de la defensa: dejaría de ser un problema de parcheo | `Poco probable · 20–45 %` |

## E-4. Decisiones que este informe pide al nivel estratégico

<!-- cti:table highlight="CVE|TACACS|configuración|alias" -->

| # | Decisión | Fundamento | Plazo |
|---|---|---|---|
| E-a | **Verificar los cinco CVE del Anexo A.1 en todo el equipamiento de borde propio**, y **preguntar formalmente por ellos a los proveedores de conectividad y de servicios gestionados**, con respuesta por escrito. **Es la decisión de mayor rendimiento de todo el lote de noviembre de 2026**: la exposición a este actor es de parcheo y no de capacidad, y la pregunta se responde en una semana | `KJ-7`, `KJ-9`, Anexo A.1 | 30 días |
| E-b | **Endurecer la configuración de los dispositivos de red según las mitigaciones que el propio aviso publica**: desactivar Smart Install, desactivar la interfaz web no cifrada, desactivar el intérprete de contenedor del dispositivo donde no se use, migrar a SNMPv3 con autenticación y cifrado retirando las comunidades por defecto, usar sólo SSH versión 2, y cerrar las listas de control de acceso con una denegación final registrada | §X-5 | 60 días |
| E-c | **Tratar el servidor TACACS+ o RADIUS con el escrutinio de un controlador de dominio**, y **migrar sus secretos compartidos y las credenciales locales de los dispositivos a los formatos de cifrado no reversibles** que el aviso recomienda. En al menos un caso documentado el secreto estaba en un formato reversible de Cisco | `KJ-5`, §X-5 | 60 días |
| E-d | **Comparación periódica y automática de la configuración de cada dispositivo de red contra su versión autorizada**, con alerta ante desviación. Es la primera caza que recomienda el aviso, la que detecta una lista de control de acceso modificada, **y la misma decisión `E-e` que pide `CTI-2026-028`**: dos informes, un solo proyecto | `KJ-5`, §T-4 | 90 días |
| E-e | **Instruir por escrito la regla de no transitividad de los alias** (Anexo D) y aplicarla a los expedientes abiertos: ningún producto de esta célula puede afirmar una equivalencia de actores apoyándose en una cadena que contenga un solapamiento parcial. **Coste cero, y evita exactamente el error que este informe documenta** | `KJ-3`, Anexo D | 15 días |
| E-f | **Ingerir el paquete STIX que el propio aviso publica**, en lugar de los indicadores reempaquetados en el Anexo A de este informe. La fuente oficial es preferente y se mantiene actualizada; nuestro anexo es una copia con fecha | Anexo A, Anexo F | 30 días |
| E-g | **Plano de gestión separado** para el acceso administrativo a los dispositivos de red, con una red dedicada sin fuga de rutas ni salida a Internet, y vigilancia de policía de plano de control. Es la mitigación de fondo del aviso y converge con la decisión `E-c` de `CTI-2026-028` | §X-5 | 120 días |
| E-h | **Comunicar a Dirección el estado real de la atribución**: si en septiembre de 2026 alguien de la organización leyó en prensa que «Salt Typhoon ataca Latinoamérica» y lo incorporó a su evaluación de riesgo, **ese dato no está establecido** —Microsoft afirma la identidad sin publicar base, ESET la niega con razonamiento, y dos fuentes de noviembre de 2026 dicen que no está clara—. La corrección que hay que emitir no es «es falso», que afirmaría de más, sino **«no se sabe, y quien lo publicó como hecho afirmó más de lo que podía»** | `KJ-4`, §O-1, §E-2 | 15 días |

---

# NIVEL OPERACIONAL
### Para: Jefatura de SOC · **Arquitectura y Administración de Red** · Respuesta a Incidentes · Threat Hunting · Horizonte: semanas–meses

## O-1. Identificación y alias

> **Este expediente de alias es el más consecuente de la cartera, porque de él
> salió una atribución falsa en titulares. Se presenta en tres bloques.**

**Bloque 1 — Designaciones que el aviso oficial recoge como nombres de industria para el mismo conjunto de actividad**

| Designación | Origen | Grado de equivalencia |
|---|---|---|
| `Salt Typhoon` | Microsoft | **Referencia de uso general**, y la que da título a este informe. **Pero nótese: el aviso no la adopta como designación propia**, sólo la enumera |
| `OPERATOR PANDA` | CrowdStrike | Recogida por el aviso como nombre de industria |
| `RedMike` | Recorded Future | Recogida por el aviso |
| `UNC5807` | Mandiant / Google | Recogida por el aviso |
| **`GhostEmperor`** | Kaspersky | **Recogida por el aviso — y es el eslabón de la fusión errónea. Véase el bloque 3** |
| «*APT actors*» | **El aviso mismo** | **La designación que el aviso usa.** Veintitrés agencias de trece países describieron este actor **sin ponerle un nombre propio**, y eso es una decisión deliberada que conviene respetar |

**Bloque 2 — Lo que NO es este actor**

| Designación | Por qué no |
|---|---|
| `FamousSparrow` / `SparroWocky` | **Actor distinto.** Es el de `CTI-2026-017`. ESET, que analizó su campaña latinoamericana, **rastrea los dos actores por separado**. Es el objeto de `KJ-4` |
| `Lilac Typhoon` | **Clúster distinto.** Es el nombrado en el caso chileno de telecomunicaciones de agosto de 2026, según recoge `CTI-2026-017`. No confundir |
| `UNC2814` / la campaña que Google desmanteló en 2026 | **Actor distinto, y esto es importante: la propia fuente que lo designó afirma expresamente NO ver solapamiento con este actor.** Es una negación explícita de equivalencia hecha por quien tenía la telemetría, y vale más que muchas afirmaciones |
| `UNC3886` | **Actor distinto.** Es el de `CTI-2026-028`. Superficie parecida —equipamiento de red— y economía de exposición opuesta. Véase la tabla comparativa de §E-1 |

**Bloque 3 — Quién afirma qué sobre la identidad de los dos actores**

| Quién | Qué afirma | Qué base publica | Estado |
|---|---|---|---|
| **Microsoft** | **`Salt Typhoon`, `FamousSparrow` y `GhostEmperor` son el mismo grupo.** Declarado a un diario de ámbito económico | **Ninguna.** Ni indicadores, ni tácticas, ni explicación de la atribución, según recoge expresamente ESET | **Afirmación sin respaldo publicado** |
| **ESET** | Son **actores distintos**. Rastrea `FamousSparrow` por separado y ve con `Salt Typhoon` sólo vínculos laxos; trata `GhostEmperor` y `FamousSparrow` como dos grupos distintos | **Sí**: uso exclusivo de `SparrowDoor` y solapamiento de código con muestras previamente documentadas. Y explica los solapamientos con herramientas de terceros por un **suministrador compartido, al que llama con el mismo término —«intendente digital»— que Check Point usaría después** | **Afirmación con razonamiento publicado** |
| **Check Point** (2026-11-10) | Hay vínculo, pero **«los detalles de ese vínculo no están claros»** | Análisis del ecosistema `Sparrow` completo | **Declara la cuestión abierta** |
| **Cobertura técnica del mismo ecosistema** (2026-11) | `FamousSparrow` «comparte cierto grado de solapamiento» con `Salt Typhoon`, pero **«la naturaleza precisa de la relación sigue sin estar clara»** | — | **Declara la cuestión abierta** |
| **Aviso oficial `AA25-239A`** (2025-08) | Enumera `GhostEmperor` entre los cinco nombres de industria de este actor | No se pronuncia sobre `FamousSparrow`, que **no figura en la lista** | **No se pronuncia** |
| **Coberturas de prensa** (2026-09) | Publican la campaña de `SparroWocky` como de `Salt Typhoon` | Ninguna propia: resumen el análisis de ESET | **Adoptan la taxonomía de Microsoft y la presentan como establecida** |

> **La lectura de esta tabla, y es el núcleo del informe.** Tres fuentes de 2026
> —ESET, Check Point y una cobertura técnica— coinciden en que **la relación no
> está establecida**. Una fuente la afirma categóricamente **sin publicar nada**.
> Y el aviso oficial **no se pronuncia sobre FamousSparrow en absoluto**: ese
> nombre no está en su lista de cinco.
>
> En ese estado de cosas, **la afirmación defendible no es «son actores
> distintos» ni «son el mismo»: es que nadie ha publicado la evidencia que lo
> decida**, y que quien lo presente como resuelto —en cualquiera de las dos
> direcciones— está afirmando más de lo que sabe. Esto incluye la primera
> redacción de este informe (véase el Anexo G).

> **Nota de tradecraft — dos reglas, y la primera es la que importa aquí.**
>
> **Regla 1: una atribución sin base publicada no es una atribución utilizable,
> por autorizada que sea la fuente.** Microsoft tiene telemetría que nadie más
> tiene y puede estar viendo algo real. Pero mientras no publique indicadores,
> tácticas ni razonamiento, **su afirmación no se puede verificar, refutar ni
> operacionalizar**, y por tanto no puede sostener una decisión de detección.
> Frente a ella, ESET publica su razonamiento —uso exclusivo de un implante y
> solapamiento de código— y eso es lo que hace su posición auditable, no
> necesariamente correcta. **La asimetría no está en quién tiene razón: está en
> quién permite comprobarlo.**
>
> **Regla 2: un solapamiento parcial no es transitivo.** Si A se solapa
> parcialmente con B, y B es un alias de C, no se sigue que A sea C. Aquí esta
> regla es una **advertencia y no un diagnóstico**: la vía vía `GhostEmperor`
> existe y es inválida, pero dado que Microsoft afirmó la identidad directamente,
> **no era necesaria para explicar lo que pasó** (`KJ-3`, H3 de §O-6). Se
> conserva porque la regla vale con independencia de este caso.
>
> Esta cartera lleva tres expedientes con variantes del problema de
> nomenclatura: `CTI-2026-022` (nombres de un actor regional en disputa),
> `CTI-2026-017` v1.2 (un implante tomado por un actor) y éste (**una
> equivalencia afirmada sin base publicada y adoptada como hecho**). El Anexo D
> recoge las cinco comprobaciones, y la decisión `E-e` las convierte en
> instrucción.

## O-2. Estructura y atribución

| Eje de atribución | Valoración | Confianza |
|---|---|---|
| Clúster técnico | **Coherente y excepcionalmente bien caracterizado** por el aviso: cinco CVE de acceso, procedimientos con comandos literales, cuatro herramientas con hash, mapeo de técnicas y de contramedidas | Alta |
| Grupo organizado | **Sí**, con herramientas propias de desarrollo identificable —clientes de transferencia escritos en Go, con control de versiones visible en las cadenas— | Alta |
| Nexo estatal | **China.** El aviso lo declara expresamente y **nombra tres empresas chinas** vinculadas a la actividad | **Alta** |
| Identidad nominal | Ninguna persona nombrada. **Pero sí tres personas jurídicas**, con razón social completa | Moderada |
| Delimitación frente a otros clústeres china-nexus | **Parcialmente resuelta y parcialmente no.** Resuelta frente al clúster que Google desmanteló, porque esa fuente niega el solapamiento. **No resuelta frente a `GhostEmperor`**, y de ahí `KJ-3` | Baja |

*Razonamiento.* La atribución estatal de este actor es, en términos de respaldo institucional, **la más fuerte de los siete informes de este lote**. No es la valoración de un proveedor ni la de un gobierno: es un documento conjunto de veintitrés agencias de inteligencia y de ciberseguridad de trece países, que atribuye la actividad a China y **nombra tres empresas chinas** con razón social completa en inglés y en chino. Nombrar personas jurídicas es un acto con consecuencias de sanción y de cumplimiento, y no se hace a la ligera.

*Contraargumento, y es de delimitación y no de identidad.* Lo que el aviso no hace es **ponerle un nombre propio al actor**. Habla de «actores APT» y enumera cinco designaciones de industria. Esa decisión es probablemente deliberada —evita adoptar la taxonomía de un proveedor— pero tiene un efecto secundario que este informe documenta: **al poner cinco nombres en la misma lista, hace que los cinco parezcan intercambiables**, y uno de ellos, `GhostEmperor`, arrastra un solapamiento parcial con un actor distinto. **La lista de alias de un aviso oficial es una lista de nombres que se han usado, no una declaración de que todos los expedientes asociados a esos nombres sean el mismo.** Es una distinción que el aviso no necesita hacer y que el lector sí.

*Observación sobre la negación explícita.* Hay en este expediente algo poco frecuente y muy valioso: cuando la inteligencia de Google desmanteló en 2026 una campaña china-nexus de gran escala contra telecomunicaciones, **afirmó expresamente no ver solapamiento con este actor**. Una negación explícita de equivalencia, hecha por quien tiene la telemetría, es una pieza de inteligencia de alta calidad y mucho más escasa que una afirmación. Se recoge en el bloque 2 de §O-1 precisamente por eso.

## O-3. Modelo de operación: no roba ficheros, se conecta a la red

**El acceso: CVE públicos, y ninguno de día cero.** El aviso es explícito: **no se observaron días cero.** Los cinco CVE de acceso inicial son `CVE-2024-21887` (Ivanti), `CVE-2024-3400` (Palo Alto), `CVE-2023-20198` y `CVE-2023-20273` (Cisco IOS XE, encadenados) y `CVE-2018-0171` (Cisco Smart Install, **de 2018**). El aviso enumera además otros fabricantes cuyo equipamiento podría estar afectado: Fortinet, Juniper, Microsoft Exchange, Nokia, Sierra Wireless y SonicWall.

El detalle de uno de ellos merece atención por lo que dice del nivel de cuidado: para explotar `CVE-2023-20198`, el actor solicita los extremos `/webui_wsma_Http` y `/webui_wsma_Https` **con doble codificación de URL** —por ejemplo `/%2577eb%2575i_%2577sma_Http`—, lo que elude filtros que buscan la cadena literal. Y el aviso añade una observación práctica que vale como detección: la presencia de la cabecera `Proxy-Uri-Source` indica un equipo **ya parcheado**.

**Lo que hace dentro: convertir el control de acceso del dispositivo en su propia autorización.** Tres procedimientos, y la lógica se ve al leerlos juntos:

1. **Modifica las listas de control de acceso** del router para añadir sus propias direcciones. Usa nombres de lista deliberadamente mundanos —`access-list 20`, y si ya existe, `50` o `10`—. Después de esto, su tráfico no es tráfico que haya que colar: es tráfico autorizado por la configuración de la víctima.
2. **Activa la captura de paquetes en el propio dispositivo** para recoger las autenticaciones que pasan por él. El aviso publica la secuencia literal de comandos, y el filtro es revelador: `match ipv4 protocol tcp any any eq 49`, es decir, **TACACS+**. Después exporta la captura al almacenamiento interno y la envía por FTP o TFTP a una dirección suya. En al menos un caso, **el secreto compartido de TACACS+ estaba almacenado con un cifrado reversible de Cisco**, lo que lo hace recuperable del propio fichero de configuración.
3. **Modifica la configuración del servidor TACACS+** para apuntar a una dirección del actor, y degrada los métodos de autenticación. A partir de ahí, **las credenciales de administración de la red llegan al adversario por el camino normal.**

**Y una pieza más, en equipos de la gama de proveedor:** en dispositivos IOS XR activa un servicio de acceso al sistema operativo subyacente —`sshd_operns`, **deshabilitado por defecto**, en el puerto **TCP/57722**— que le da una consola en el anfitrión Linux del router. Crea una cuenta local, y **modifica el fichero de configuración de elevación de privilegios y los permisos del propio binario de elevación** para asegurarse el acceso privilegiado.

**La salida: túneles, no transferencias.** El actor monta túneles **GRE, mGRE e IPsec** desde los dispositivos comprometidos, y el aviso documenta al menos un caso en que usó **GRE sobre MPLS para extraer datos hacia China**. Esta es la diferencia de concepto con los seis informes anteriores del lote: **no hay una exfiltración que detectar por volumen.** Hay un túnel que, desde el punto de vista de la red, parece un enlace más.

**También abusa de lo que encuentra.** Usa las comunidades SNMP por defecto —`public` y `private`— y **operaciones de escritura SNMP** para hacer cambios de configuración. Y emplea los intérpretes del propio dispositivo: el intérprete de contenedor Linux integrado en los equipos Cisco, y el intérprete de guiones Tcl del sistema operativo del router.

> **La lectura conjunta.** Este actor ataca una confianza distinta de las de los
> informes anteriores de este lote: **la confianza de la organización en la
> configuración de sus propios dispositivos de red.** Una lista de control de
> acceso es un documento que decimos que define quién puede entrar; cuando el
> adversario puede escribirla, **el documento sigue siendo verdadero y deja de
> protegernos**. Y un servidor de autenticación es el punto donde se decide
> quién administra la red; cuando el adversario decide a dónde apunta, **la
> decisión se sigue tomando, pero la toma él.**
>
> La respuesta no es detectar al adversario en el dispositivo: es **comparar la
> configuración del dispositivo con la que debería tener**, que es la decisión
> `E-d` y la primera caza que el propio aviso recomienda.

## O-4. Nuestra exposición

> ⬛ **Sección sin evaluar — requiere inventario y configuración.** Como en
> `CTI-2026-028`, la superficie no admite agente de detección. **Pero a
> diferencia de aquél, aquí la mayoría de las preguntas se responden en días y
> casi todas tienen remedio barato.**

| # | Pregunta | Fuente | Responsable |
|---|---|---|---|
| X-1 | **¿Están cerrados los cinco CVE del Anexo A.1 en todo el equipamiento de borde propio?** Uno por uno, con versión y fecha | Inventario / gestión de vulnerabilidades | **Gestión de Vulnerabilidades** |
| X-2 | **¿Y en el equipamiento de nuestros proveedores de conectividad y de servicios gestionados?** Pregunta formal, con respuesta por escrito | Contratos / proveedores | Contratos / Arquitectura |
| X-3 | ¿Tenemos equipamiento de los otros seis fabricantes que el aviso menciona como posiblemente afectados, y en qué versión? | Inventario | Redes |
| X-4 | **¿Está Smart Install desactivado en todo el equipamiento Cisco?** ¿Y la interfaz web no cifrada? | Configuración de red | Redes |
| X-5 | **¿Está desactivado el intérprete de contenedor Linux integrado en los dispositivos que no lo necesitan?** ¿Cómo se verifica? | Configuración de red | Redes |
| X-6 | **¿Existen comunidades SNMP `public` o `private` en algún dispositivo?** ¿Está permitida la escritura por SNMP? | Configuración de red | Redes |
| X-7 | **¿En qué formato están almacenados el secreto compartido de TACACS+ y las credenciales locales de los dispositivos?** ¿Es reversible? | Configuración de red | Redes |
| X-8 | ¿Está el servidor TACACS+ o RADIUS monitorizado al nivel de un controlador de dominio? ¿Alertaríamos si cambiara su configuración? | SIEM / arquitectura | SOC / Redes |
| X-9 | **¿Comparamos la configuración de cada dispositivo contra una versión autorizada, de forma periódica y automática?** | Herramientas de red | Redes |
| X-10 | ¿Hay listas de control de acceso con entradas no justificadas por la configuración aprobada? ¿Terminan todas en una denegación registrada? | Configuración de red | Redes |
| X-11 | ¿Existe algún túnel GRE, mGRE o IPsec configurado que no corresponda a un enlace aprobado? ¿Hay tráfico de túnel entre sistemas autónomos distintos? | Configuración / NetFlow | Redes / SOC |
| X-12 | **¿Está abierto el puerto TCP/57722 en algún dispositivo?** Corresponde a un servicio deshabilitado por defecto | Escaneo externo | SOC / Redes |
| X-13 | ¿Hay cuentas locales en los dispositivos de red que no correspondan al inventario? ¿Alguna llamada `cisco`? | Configuración de red | Redes |
| X-14 | ¿Sale tráfico FTP o TFTP **desde** nuestros dispositivos de red hacia destinos no aprobados? | Cortafuegos / NetFlow | SOC |
| X-15 | ¿Se registró en alguna evaluación de riesgo de la organización la noticia de septiembre de 2026 según la cual «Salt Typhoon ataca Latinoamérica»? **Si sí, hay que corregirla** | Registro de riesgos | **Riesgo / Célula CTI** |

## O-5. Cronología

<!-- cti:timeline -->

| Fecha | Hecho | Traza |
|---|---|---|
| `2018-03` | Divulgación de `CVE-2018-0171` en Cisco Smart Install. **Ocho años con parche disponible** | — |
| `2021-08` | **Fecha más antigua de las direcciones que el aviso publica.** El aviso sitúa la actividad «desde al menos 2021» | Global |
| `2021` | Año en que `GhostEmperor` y FamousSparrow compartieron una dirección IP y una vulnerabilidad, según recoge `CTI-2026-017`. **Origen remoto de la fusión de `KJ-3`** | — |
| `2023-10` | Divulgación de `CVE-2023-20198` y `CVE-2023-20273` en Cisco IOS XE, que el actor encadena | — |
| `2024-01` | Divulgación de `CVE-2024-21887` en Ivanti Connect Secure y Policy Secure, encadenada con otra | — |
| `2024-04` | Divulgación de `CVE-2024-3400` en PAN-OS GlobalProtect | — |
| `2024` | Revelación pública de los compromisos de operadores de telecomunicaciones estadounidenses, que da notoriedad al actor | EE. UU. |
| `2024-08-16` | **Marca de versión en una de las herramientas del actor** (`V20240816`), visible en sus cadenas | — |
| `2025-06` | Fecha más reciente de las direcciones que el aviso publica | Global |
| `2025-08-27` | **Publicación del aviso conjunto `AA25-239A`: 23 agencias, 13 países, tres empresas chinas nombradas, cinco CVE, cero días cero** | Multinacional |
| `2025-08` | El FBI estima **al menos 200 empresas comprometidas en más de 80 países**. *Cifra no contenida en el aviso* | Global |
| `2025-09-03` | **Revisión 1.1 del aviso**, siete días después de su publicación | Multinacional |
| `2026-02` | El FBI declara la amenaza **todavía en curso** | Global |
| `2026-09-17` | **ESET publica el análisis de la campaña latinoamericana de FamousSparrow y del implante `SparroWocky`** | LATAM |
| `2026-09` | **Varias coberturas de prensa especializada atribuyen esa campaña a «Salt Typhoon».** Es el error de `KJ-4`, y ocurre el mismo mes en que `CTI-2026-017` advertía que ocurriría | — |
| `2026-09-21` | Emisión de `CTI-2026-017`, cuyo `KJ-7` deja la disputa de alias consignada como sin resolver | Chile |
| `2026-11-10` | Publicación de la investigación de Check Point que reordena el ecosistema de FamousSparrow **sin situarlo en este actor**, lo que refuerza la separación | LATAM |
| `2026-11-17` | **Emisión de este informe y revisión v1.2 de `CTI-2026-017`.** La disputa se resuelve identificando el eslabón, no la equivalencia | Chile |

## O-6. Hipótesis alternativas consideradas

**Cuestión 1 — ¿Por qué se atribuyó a este actor la campaña de otro?**

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| **H1 — Microsoft afirmó la identidad y la prensa la adoptó** | **Es la explicación documentada y la que se retiene.** Microsoft declaró —según coberturas— que `Salt Typhoon`, `FamousSparrow` y `GhostEmperor` son el mismo grupo, **sin publicar base técnica**. Las coberturas de septiembre de 2026 no inventaron nada: **adoptaron una taxonomía en disputa y la presentaron como establecida**. No requiere ninguna inferencia nuestra | `Retenida · muy probable 80–95 %` |
| **H2 — Simplificación editorial** | Que «Salt Typhoon» funcione además como etiqueta reconocible para «espionaje chino en telecomunicaciones». **Complementaria de H1**: explica por qué la etiqueta es atractiva, no de dónde sale | `Retenida como complemento` |
| **H3 — Composición inválida vía `GhostEmperor`** | El aviso sitúa `GhostEmperor` entre los nombres de industria de este actor, y `CTI-2026-017` recoge su solapamiento parcial con FamousSparrow. Componerlos vuelve a dar la equivalencia, **y la composición es inválida**. Vía plausible y **reforzadora de H1, no alternativa**. *Degradada en la verificación previa a la publicación: era la hipótesis retenida en la primera redacción, y dado H1 **no es necesaria** para explicar el resultado* | `Retenida como refuerzo · posibilidad real 45–55 %` |
| **H4 — La equivalencia es correcta y ESET se equivoca** | Que FamousSparrow sea efectivamente este actor. **No se puede descartar, y conviene decirlo con más fuerza que en la primera redacción**: Microsoft tiene telemetría propia y puede estar viendo algo que no publica. Lo que no se puede hacer es tratarla como establecida sin esa publicación | `Poco probable · 20–45 %` |
| **H5 — La relación es real pero parcial, y ninguna de las dos designaciones la captura** | Que haya solapamiento genuino —de herramientas, de infraestructura o de proveedor— sin identidad de operador. **Es lo que dicen literalmente las dos fuentes de noviembre de 2026** al declarar que la naturaleza de la relación «no está clara», y es consistente con la tesis del suministrador compartido de `CTI-2026-017` v1.2. **Se retiene** | `Retenida · posibilidad real 45–55 %` |

**Cuestión 2 — ¿Qué clase de operación es ésta?**

<!-- cti:cards -->

| Hipótesis | Argumento y estado | Etiqueta |
|---|---|---|
| **H5 — Sistema de interceptación sobre infraestructura ajena** | Los tres procedimientos de §O-3 —ACL propia, captura de autenticaciones, redirección del servidor TACACS+— más túneles en lugar de transferencias, apuntan a **acceso persistente al tráfico en tránsito** y no a robo de ficheros. El título del propio aviso habla de alimentar un sistema global de espionaje. **Es la que se retiene** | `Retenida · muy probable 80–95 %` |
| **H6 — Prepos para disrupción futura** | Que el acceso a infraestructura de operador sirva para una capacidad de interrupción y no sólo de escucha. **El aviso no documenta ninguna acción destructiva**, y la victimología —incluido el sector de alojamiento— encaja mejor con recolección. Se consigna porque es la hipótesis que otros actores china-nexus sí materializan | `Posibilidad real · 45–55 %` |
| **H7 — Recolección dirigida a personas concretas** | Que el objetivo final sea el seguimiento de individuos específicos a través de los metadatos y las comunicaciones de los operadores. Es consistente con la victimología de telecomunicaciones y alojamiento, **y el aviso no lo afirma ni lo niega** | `Posibilidad real · 45–55 %` |

**Supuesto clave.** El informe asume que **ninguna de las dos atribuciones puede tratarse como establecida mientras nadie publique la base técnica**: ni la identidad que afirma Microsoft, ni la separación que sostiene ESET. Es la posición conservadora y la única consistente con que dos fuentes de noviembre de 2026 declaren que la relación «no está clara». **Si Microsoft publicara indicadores que sostuvieran la identidad, `KJ-4` caería y habría que reescribir este informe y `CTI-2026-017`.** Si ESET publicara un análisis comparado que la refutara, `KJ-4` subiría a confianza alta. **El estado actual no es un empate: es una ausencia de evidencia publicada por la parte que afirma.**

**Pre-mortem.** Es mayo de 2027 y este informe resultó equivocado. **Y hay un pre-mortem que ya se cumplió, antes de publicar**: la primera redacción de este informe sostenía con «casi certeza» que la atribución de prensa era incorrecta, y construyó como hallazgo central una cadena transitiva vía `GhostEmperor`. La verificación previa a la publicación encontró que **existe una explicación mucho más simple y documentada —Microsoft afirmó la identidad directamente— y que nuestra cadena no era necesaria.** El informe habría publicado una tesis elegante y sobredimensionada. Se corrigió, y la corrección está en el Anexo G. **La lección es que el riesgo de este tipo de producto no es equivocarse en los hechos: es construir un mecanismo causal más interesante que el real.**

La causa más probable de un fallo futuro: **dedicamos el informe a la disputa de nombres y no hicimos lo único urgente**, que era la decisión `E-a` —verificar cinco CVE—. Es la sección más corta y la más valiosa, y la de tradecraft es la más larga. Segunda causa: Microsoft publica la base técnica, resulta que son el mismo actor, y todo el aparato de `KJ-4` y del Anexo D queda como una lección de método sobre un caso en que la respuesta era sí. **En ese escenario la regla del Anexo D sigue siendo correcta y nuestra aplicación de ella a este caso, no.**

## O-7. Indicadores y señales de alerta

| # | Indicador observable | Qué señalaría | Disciplina | Responsable |
|---|---|---|---|---|
| I-1 | **Rectificación pública de las coberturas que atribuyeron la campaña de `SparroWocky` a este actor** | Confirmaría `KJ-4` y cerraría el expediente. **Su ausencia es el escenario más probable de §E-3**, y en ese caso la corrección queda en nuestro producto | OSINT | Célula CTI |
| I-2 | **Análisis que establezca si `GhostEmperor` es o no el mismo conjunto que FamousSparrow** | Resuelve `KJ-3` en una dirección u otra. Si fueran el mismo, **habría que reescribir este informe y `CTI-2026-017`** | OSINT | Célula CTI |
| I-3 | Publicación de indicadores o técnicas por parte de Microsoft que sostengan su afirmación de equivalencia de 2024 | Resolvería H3 de §O-6 y la disputa que `CTI-2026-017` abrió | OSINT | Célula CTI |
| I-4 | **Revisión del aviso con CVE o indicadores nuevos** | El aviso ya tuvo una revisión a los siete días. Cada revisión obliga a repetir la decisión `E-a` | OSINT oficial | Célula CTI / Vulnerabilidades |
| I-5 | **Caso documentado de este actor en un operador de telecomunicaciones latinoamericano**, por informe o por comunicado de un Estado de la región | Convertiría `KJ-9` en exposición concreta y de primer orden | OSINT | Célula CTI |
| I-6 | **Primer uso documentado de un día cero por este actor** | Invalidaría `KJ-7` y cambiaría la economía de la defensa: dejaría de ser un problema de parcheo | OSINT | Célula CTI |
| I-7 | Aparición de los mismos procedimientos —ACL propia, captura de TACACS+, redirección del servidor de autenticación— en un actor distinto | El método es público desde agosto de 2025 y es copiable. **Sería el indicador que nos afecta con independencia de este actor** | OSINT / telemetría | Célula CTI / SOC |
| I-8 | Sanciones o acciones legales sobre las tres empresas nombradas | Efectos de cumplimiento y de cadena de suministro | OSINT | Legal / Cumplimiento |
| I-9 | Confirmación o rectificación de la actividad contra telecomunicaciones sudamericanas que afirma una fuente de proveedor | Resolvería la brecha `G-4`, que es la única pieza de este expediente con posible relevancia regional directa | OSINT | Célula CTI |

---

# NIVEL TÁCTICO
### Para: Analistas de SOC · Ingeniería de Detección · **Administración de Red** · Horizonte: días–semanas

## T-1. Cadena de intrusión

<!-- cti:stages title="Cuatro etapas, y la tercera convierte nuestro control de acceso en su autorización" dwell="**Permanencia:** no publicada. Las direcciones del aviso abarcan de agosto de 2021 a junio de 2025, y el FBI declaró la amenaza en curso en febrero de 2026: la permanencia se mide en años." -->

| Etapa | Título | Elementos |
|---|---|---|
| Etapa 01 · Borde | Explotación de CVE **públicos y parcheados** | `CVE-2023-20198` + `CVE-2023-20273` (Cisco IOS XE, encadenados) · `CVE-2024-21887` (Ivanti) · `CVE-2024-3400` (PAN-OS) · `CVE-2018-0171` (Smart Install) · **doble codificación de URL** en los extremos `/webui_wsma_Http` y `/webui_wsma_Https` · `siet.py` · **cero días cero** |
| Etapa 02 · Ejecución en el dispositivo | Uso de los intérpretes del propio equipo | **Intérprete de contenedor Linux integrado**: `guestshell enable` · `guestshell run bash` · `run guestshell` · `chvrf` · `dohost` · intérprete Tcl del router: `tclsh`, `TCLproxy.tcl`, `map.tcl` · `/level/15/exec/-/*` |
| Etapa 03 · Autorización | **Modificación del control de acceso y del servidor de autenticación** | **ACL con direcciones del actor** (`access-list 20`, `50`, `10`) · **captura de paquetes de TACACS+ en el propio dispositivo** · **redirección del servidor TACACS+ a una dirección del actor** · degradación de métodos de autenticación · SNMP `public`/`private` y escritura por SNMP |
| Etapa 04 · Persistencia y salida | Cuentas, consola en el anfitrión y túneles | `sshd_operns` en **TCP/57722** (deshabilitado por defecto) · cuenta local `cisco` · modificación del fichero de elevación de privilegios y de los permisos del binario de elevación · **túneles GRE, mGRE e IPsec** · **GRE sobre MPLS para extraer hacia China** · `wodSSHServer` · `STOWAWAY` |

**Etapa 01 y la mejor noticia del informe.** El aviso afirma expresamente que **no se observaron días cero**. Los cinco CVE estaban publicados y parcheados, y uno es de 2018. Esto significa que la exposición a este actor se cierra con gestión de parches en el borde, y es la decisión `E-a`.

Dos detalles prácticos del aviso merecen registro. El primero: para explotar la vulnerabilidad de Cisco IOS XE, el actor solicita los extremos con **doble codificación de URL** —`/%2577eb%2575i_%2577sma_Http`—, de modo que un filtro que busque la cadena literal no lo verá. El segundo, que es un regalo para el defensor: **la presencia de la cabecera `Proxy-Uri-Source` en la respuesta indica que el equipo está parcheado.** Es una comprobación de estado, no de compromiso.

**Etapa 03 es el centro del informe, y conviene detenerse.** Los tres procedimientos tienen una lógica común: **no sortear los controles del dispositivo, sino convertirlos en propios.**

*La lista de control de acceso.* El actor añade sus direcciones a una ACL existente, con nombres deliberadamente mundanos. Tras esto, su tráfico no es tráfico que haya que colar por un hueco: **es tráfico que el propio dispositivo clasifica como autorizado**. Un control de acceso que el adversario puede escribir no es un control: es una declaración de intenciones del adversario.

*La captura de paquetes.* El aviso publica la secuencia literal, y el filtro es lo revelador: captura el protocolo TCP en el **puerto 49**, que es TACACS+. Después exporta al almacenamiento interno del dispositivo y envía el fichero por **FTP o TFTP** a una dirección externa. Los nombres de los ficheros de captura observados son `mycap.pcap`, `tac.pcap` y `1.pcap`. Y el agravante: **en al menos un caso el secreto compartido de TACACS+ estaba almacenado con un cifrado reversible de Cisco**, de modo que el actor pudo recuperarlo del propio fichero de configuración.

*La redirección del servidor de autenticación.* Cambia la configuración para que el dispositivo consulte a un servidor TACACS+ del actor, y degrada los métodos de autenticación disponibles. A partir de ahí **las credenciales de administración llegan al adversario por el camino previsto**, sin que nada falle.

**Etapa 04 y la diferencia de concepto.** El actor no transfiere ficheros: **monta túneles**. Y el caso que el aviso documenta —GRE sobre MPLS hacia China— significa que la red de la víctima quedó, a efectos prácticos, extendida hasta el adversario. **No hay un pico de salida de datos que detectar**, porque no hay una transferencia: hay un enlace.

En equipos de la gama de proveedor hay además un paso específico: activar `sshd_operns`, un servicio **deshabilitado por defecto** que escucha en **TCP/57722** y da una consola en el sistema operativo Linux subyacente del router —sin privilegios de administrador, según el aviso, lo que explica los pasos siguientes: crear una cuenta local, editar el fichero de configuración de elevación de privilegios y **cambiar los permisos del binario de elevación a `4755`**, es decir, activarle el bit de suplantación de propietario.

## T-2. Mapa MITRE ATT&CK

> Tomado directamente del aviso `AA25-239A`, que declara **ATT&CK v17**. Se
> conservan los identificadores de la fuente. **Es un mapeo oficial, no una
> inferencia nuestra**, y por eso este informe no añade ni quita ninguna
> técnica. El aviso publica además un mapeo D3FEND de contramedidas, que se
> recoge al final.

<!-- cti:matrix -->

| Táctica | ID | Técnica | Procedimiento según el aviso |
|---|---|---|---|
| Reconocimiento | T1595 | Active Scanning | Exploración activa de infraestructura expuesta |
| Reconocimiento | T1590.004 | Gather Victim Network Information: Network Topology | Recogida de la topología de red de la víctima |
| Desarrollo de recursos | T1583.003 | Acquire Infrastructure: Virtual Private Server | Infraestructura alquilada |
| Desarrollo de recursos | T1584.008 | Compromise Infrastructure: Network Devices | **Compromiso de dispositivos de red de terceros como infraestructura propia** |
| Desarrollo de recursos | T1588.005 | Obtain Capabilities: Exploits | Obtención de exploits para los cinco CVE |
| Desarrollo de recursos | T1588.002 | Obtain Capabilities: Tool | `siet.py`, `STOWAWAY`, `wodSSHServer` |
| Acceso inicial | T1190 | Exploit Public-Facing Application | Los cinco CVE de borde. **Ninguno de día cero** |
| Acceso inicial | T1199 | Trusted Relationship | Acceso a través de proveedores de acceso a Internet y de relaciones de confianza |
| Ejecución | T1569 | System Services | Activación de servicios del dispositivo (`sshd_operns`) |
| Ejecución | T1609 | Container Administration Command | **Intérprete de contenedor Linux integrado en el dispositivo** |
| Ejecución | T1059.006 | Command and Scripting Interpreter: Python | `siet.py` |
| Ejecución | T1059.008 | Command and Scripting Interpreter: Network Device CLI | Interfaz de línea de comandos del dispositivo; `tclsh` |
| Persistencia | T1136.001 | Create Account: Local Account | Cuenta local en el dispositivo (`cisco`) |
| Persistencia | T1543.005 | Create or Modify System Process: Container Service | Servicio de contenedor del dispositivo |
| Persistencia | T1098.004 | Account Manipulation: SSH Authorized Keys | Claves autorizadas de SSH |
| Escalada de privilegios | T1068 | Exploitation for Privilege Escalation | **Modificación del fichero de elevación de privilegios y permisos `4755` en su binario** |
| Escalada de privilegios | T1110.002 | Brute Force: Password Cracking | Descifrado de credenciales capturadas |
| Evasión | T1027.010 | Obfuscated Files or Information: Command Obfuscation | **Doble codificación de URL** en los extremos del exploit |
| Evasión | T1027 | Obfuscated Files or Information | Ofuscación general |
| Evasión | T1562.004 | Impair Defenses: Disable or Modify System Firewall | **Modificación de las listas de control de acceso para incluir sus direcciones** |
| Evasión | T1610 | Deploy Container | Despliegue del contenedor del dispositivo |
| Evasión | T1070 | Indicator Removal | Borrado de rastro |
| Evasión | T1070.009 | Indicator Removal: Clear Persistence | Borrado de mecanismos de persistencia tras usarlos |
| Evasión | T1599 | Network Boundary Bridging | **Puenteo de la frontera de red mediante el dispositivo comprometido** |
| Acceso a credenciales | T1040 | Network Sniffing | **Captura de paquetes en el dispositivo para cosechar autenticaciones de TACACS+ y RADIUS** |
| Acceso a credenciales | T1556 | Modify Authentication Process | **Modificación de la configuración del servidor TACACS+ para redirigir las credenciales** |
| Acceso a credenciales | T1003 | OS Credential Dumping | Volcado de credenciales del dispositivo |
| Acceso a credenciales | T1110.002 | Brute Force: Password Cracking | Recuperación del secreto compartido de TACACS+ en formato reversible |
| Descubrimiento | T1082 | System Information Discovery | Información del dispositivo |
| Descubrimiento | T1016 | System Network Configuration Discovery | Configuración de red y topología |
| Movimiento lateral | T1021 | Remote Services | Servicios remotos del dispositivo |
| Movimiento lateral | T1021.004 | Remote Services: SSH | SSH, con puertos no estándar observados |
| Recolección | T1560 | Archive Collected Data | **`tar -czvf - {0} \| openssl des3 -salt -k password -out {0}.tar.gz`**, cadena presente en sus herramientas |
| Recolección | T1602.001 | Data from Configuration Repository: SNMP (MIB Dump) | Volcado de la base de información de gestión por SNMP |
| Recolección | T1602.002 | Data from Configuration Repository: Network Device Configuration Dump | **Volcado de la configuración del dispositivo**, que contiene los secretos |
| Recolección | T1005 | Data from Local System | Datos del propio dispositivo |
| Mando y control | T1090 | Proxy | `STOWAWAY`, `TCLproxy.tcl` |
| Mando y control | T1090.003 | Proxy: Multi-hop Proxy | Encadenamiento a través de dispositivos comprometidos |
| Mando y control | T1071 | Application Layer Protocol | HTTP y HTTPS, con puertos no estándar observados en el rango `18xxx` |
| Mando y control | T1571 | Non-Standard Port | SSH en `22x22` o `xxx22`; HTTP(S) en `18xxx`; **TCP/57722** |
| Mando y control | T1572 | Protocol Tunneling | **Túneles GRE, mGRE e IPsec** |
| Mando y control | T1095 | Non-Application Layer Protocol | GRE como protocolo de transporte |
| Exfiltración | T1048.003 | Exfiltration Over Alternative Protocol: Unencrypted | **Envío de las capturas por FTP y TFTP** desde el propio dispositivo |

**Contramedidas D3FEND que el aviso mapea:** `D3-PM` · `D3-NTCD` · `D3-OTF` · `D3-ACH` · `D3-CFP` · `D3-CH` · `D3-SU` · `D3-NI` · `D3-ITF`.

## T-3. Dónde atacamos en la Pirámide del Dolor

<!-- cti:pyramid -->

| Nivel | Qué contiene en este informe y qué vale | Valor |
|---|---|---|
| Hashes | **Cuatro, con el nombre de la herramienta y su tamaño exacto**, publicados por el aviso. Son clientes de transferencia propios: de los indicadores más fiables del expediente, **y de los menos útiles**, porque sólo aparecen si ya hay compromiso | Base · valor bajo |
| IP · Dominios | 84 direcciones IPv4 y 2 IPv6, observadas entre 2021 y 2025. **El aviso advierte expresamente que pueden no estar vigentes y que hay que verificarlas antes de bloquearlas.** Ningún dominio | Valor bajo |
| Artefactos | **Rico y de calidad inusual**: `sshd_operns` en TCP/57722, nombres de ACL (`access-list 20`), nombres de captura (`tac.pcap`, `mycap.pcap`, `1.pcap`), `commands.log`, cuenta `cisco`, permisos `4755`, rutas de compilación filtradas, rangos de puerto `22x22` y `18xxx`, y **las cadenas de las reglas YARA oficiales** | Valor medio–alto |
| Herramientas | Intérprete de contenedor del dispositivo, `tclsh`, SNMP, GRE, FTP/TFTP, captura de paquetes nativa. **Todas son funciones legítimas del propio equipamiento de red** | Valor alto |
| TTP | Las cuatro etapas de §T-1, y en particular **la etapa 03**: modificar la ACL, capturar TACACS+ y redirigir el servidor de autenticación. Es lo que el actor no puede cambiar sin renunciar a su ventaja | Cima · valor máximo |

> **Observación de método, y es la diferencia entre este informe y
> `CTI-2026-028`.** Los dos actores viven en equipamiento de red, y en los dos
> la pirámide clásica rinde poco en su base. Pero hay un nivel que este
> expediente añade y que la pirámide no contempla: **la comparación de
> configuración.**
>
> Un adversario que modifica una lista de control de acceso, redirige un
> servidor de autenticación y activa un servicio deshabilitado por defecto
> **deja su rastro en la configuración del dispositivo, no en su memoria ni en su
> disco**. Y la configuración es el único artefacto de un dispositivo de red que
> podemos tener **duplicado fuera de su alcance**: en el repositorio de
> configuración aprobada.
>
> Por eso la primera caza que recomienda el aviso —y la decisión `E-d`— no es
> buscar indicadores: es **comparar lo que el dispositivo tiene configurado con
> lo que debería tener**. Es la única detección de este informe que funciona
> aunque el adversario controle el dispositivo, por la misma razón que el
> colector de registros externo lo era en `CTI-2026-029`: **la copia de
> referencia está fuera de su alcance.**

## T-4. Hipótesis de caza prioritarias

> Las siete primeras hipótesis son **las que el propio aviso recomienda**, con
> nuestra ordenación por valor. Las dos últimas son nuestras.

<!-- cti:accordion critical="^(H-1|H-2|H-3)\b" regional="^H-(8|9)\b" -->

**H-1 — Diferencias de configuración contra la versión autorizada.** Para cada dispositivo de red, comparar la configuración en ejecución y la almacenada contra la versión aprobada en el repositorio, y revisar en particular: **entradas de ACL no justificadas**, cambios en la configuración de los servidores de autenticación, túneles definidos, rutas, cuentas locales y servicios habilitados. Ventana: estado actual, y después en continuo. **Es la primera caza del aviso y la hipótesis de mayor valor del informe.** Fidelidad **muy alta** si existe la versión autorizada; **inservible sin ella**, y construirla es la decisión `E-d`.

**H-2 — Puerto TCP/57722 y servicio de consola del anfitrión.** Escanear **desde fuera** los dispositivos de red buscando el puerto `TCP/57722`, que corresponde a un servicio deshabilitado por defecto en los equipos de la gama de proveedor. Comprobar también en la configuración si el servicio está activado. Fidelidad **muy alta**: un puerto abierto correspondiente a un servicio que el fabricante deja deshabilitado no tiene explicación benigna. **Verificar desde fuera, no desde dentro**, por la misma razón de `CTI-2026-028`.

**H-3 — Captura de paquetes activa en un dispositivo de red.** Buscar en la configuración y en los registros de comandos toda sesión de captura de paquetes en el dispositivo, y toda sesión de duplicación de puertos. Palabras clave: `monitor capture`, y los nombres observados `mycap`, `tac.pcap`, `1.pcap`. **Y el filtro es la señal más concluyente**: una captura cuyo criterio sea el puerto TCP 49 está capturando autenticaciones de TACACS+ y no existe ninguna razón legítima de operación para ello. Fidelidad **máxima** con ese criterio.

**H-4 — Tráfico de TACACS+ hacia direcciones no aprobadas, y tráfico de TACACS+ fuera de la red de gestión.** Buscar flujos al puerto TCP/49 cuyo destino no sea un servidor de autenticación aprobado, y cualquier flujo de TACACS+ que salga del segmento de gestión. Fidelidad **muy alta**: es la detección de la redirección del servidor de autenticación, que es el procedimiento más grave del expediente.

**H-5 — Túneles GRE entre sistemas autónomos distintos.** Buscar en NetFlow tráfico GRE, mGRE o IPsec cuyos extremos pertenezcan a sistemas autónomos diferentes, y contrastarlo con los enlaces aprobados. Fidelidad **alta**; es la detección de la etapa 04 y la que cubre la exfiltración, que no se ve por volumen.

**H-6 — FTP y TFTP salientes desde dispositivos de red.** Buscar transferencias por FTP o TFTP **originadas en un dispositivo de red** hacia un destino no aprobado. Es el canal por el que el actor envía las capturas de paquetes. Fidelidad **muy alta**: un router no tiene por qué subir ficheros a Internet.

**H-7 — Uso del intérprete de contenedor del dispositivo.** Buscar en el registro de comandos las invocaciones del intérprete de contenedor Linux integrado y sus variantes: `guestshell enable`, `guestshell run bash`, `guestshell disable`, `guestshell destroy`, `run guestshell`, `chvrf`, `dohost`. Fidelidad **alta** si el servicio no se usa legítimamente. **Advertencia:** la sección de caza del propio aviso contiene una errata —`run guestshel`, con una letra de menos— y **conviene no copiarla literalmente a una regla**, porque no encontraría nada.

**H-8 — Escrituras SNMP y comunidades por defecto.** Enumerar las comunidades SNMP configuradas en todos los dispositivos y marcar `public` y `private`; y buscar operaciones de escritura SNMP, en especial sobre configuración de autenticación, servidor web, túneles o listas de acceso. Fidelidad **alta** como hallazgo de exposición: el resultado más probable es descubrir comunidades por defecto activas, que es un hallazgo en sí mismo.

**H-9 — Estado de parcheo de los cinco CVE, y comprobación de cabecera.** Verificar uno por uno los cinco CVE del Anexo A.1 en todo el equipamiento de borde propio y preguntar por ellos a los proveedores de conectividad. Para los dos de Cisco IOS XE, usar además la comprobación que el aviso regala: **la presencia de la cabecera `Proxy-Uri-Source` indica un equipo parcheado.** No es una caza de amenaza: **es la decisión `E-a`, y es la tarea de mayor rendimiento de todo el lote de noviembre de 2026.** De valor regional directo.

## T-5. Brechas de visibilidad que hay que cerrar primero

| Brecha | Por qué importa aquí |
|---|---|
| **Sin repositorio de configuración autorizada y sin comparación periódica** | **Es la brecha dominante.** Deja ciega `H-1`, que es la primera caza del aviso y la única que funciona contra un adversario que controla el dispositivo. No es un problema de producto: es un proyecto de gestión de configuración de red |
| **Sin registro de comandos ejecutados en los dispositivos** (*command accounting*) | Deja ciegas `H-3` y `H-7`. El aviso lo recomienda expresamente como mitigación, y es configuración, no producto |
| **Sin escaneo externo periódico de los dispositivos de red** | Deja ciega `H-2`. Los puertos de un dispositivo hay que verlos desde fuera |
| **Sin visibilidad de flujos de gestión** (TACACS+, RADIUS, SNMP) | Deja ciegas `H-4` y `H-8`, es decir, la detección del procedimiento más grave del expediente |
| **Sin NetFlow con visibilidad de GRE y de sistema autónomo de origen y destino** | Deja ciega `H-5`, y con ella la exfiltración completa |
| **Sin inventario de parches del equipamiento de borde** | Deja sin responder `X-1` y, con ella, la decisión `E-a`. **Es la brecha más barata de cerrar y la de mayor consecuencia** |
| **Sin respuesta de los proveedores de conectividad sobre su propio parcheo** | Deja sin responder `X-2`. **Y es la mitad de nuestra exposición**, porque el actor vive en el equipamiento del operador y no en el nuestro |
| Sin inventario de comunidades SNMP y de su modo de acceso | Deja ciega `H-8` |
| Sin detección de FTP y TFTP originados en dispositivos de red | Deja ciega `H-6` |

---

# NIVEL TÉCNICO
### Para: Ingeniería de detección · **Administración y Arquitectura de Red** · Gestión de Vulnerabilidades · Vida útil: las direcciones del aviso están declaradas como posiblemente caducadas; la configuración y las mitigaciones no caducan

## X-1. Arsenal y capacidad

| Propiedad | Valor |
|---|---|
| **Capacidad diferencial** | **Convertir el control de acceso y la autenticación del equipamiento de red de la víctima en infraestructura propia**, y después salir por túnel en lugar de exfiltrar |
| Días cero | **Ninguno observado.** Afirmación explícita del aviso, y el juicio de mayor valor práctico del informe |
| CVE de acceso inicial | `CVE-2023-20198` y `CVE-2023-20273` (Cisco IOS XE, encadenados) · `CVE-2024-21887` (Ivanti Connect Secure y Policy Secure, encadenado con otro) · `CVE-2024-3400` (PAN-OS GlobalProtect) · `CVE-2018-0171` (Cisco IOS e IOS XE, Smart Install) |
| Otros fabricantes que el aviso señala como posiblemente afectados | Fortinet · Juniper · Microsoft Exchange · Nokia · Sierra Wireless · SonicWall |
| Herramientas propias | `cmd3` y `cmd1` (clientes de transferencia en Go, con versión en las cadenas: `v1.0` y `V20240816`) · `new2` y `sft` (clientes de transferencia en Go o ELF) |
| Herramientas de terceros | `siet.py` (explotación de Smart Install) · `STOWAWAY` (proxy) · `wodSSHServer` · `TCLproxy.tcl` · `map.tcl` |
| **Rutas de compilación filtradas** | `C:/work/sync/cmd/cmd3/main.go` · `C:/work/sync_v1/cmd/cmd1/main.go`. **Compilación desde Windows, con estructura de proyecto visible** |
| Ejecución en el dispositivo | Intérprete de contenedor Linux integrado (`guestshell`, `run guestshell`, `chvrf`, `dohost`) · intérprete Tcl del router (`tclsh`) · `/level/15/exec/-/*` |
| Manipulación de control de acceso | Listas con nombre mundano: `access-list 20`, y si existe, `50` o `10` |
| Cosecha de credenciales | **Captura de paquetes nativa del dispositivo filtrando el puerto TCP 49 (TACACS+)**; exportación al almacenamiento interno y envío por FTP o TFTP. **Secreto compartido en formato reversible de Cisco en al menos un caso** |
| Manipulación de autenticación | **Redirección del servidor TACACS+ a una dirección del actor** y degradación de los métodos de autenticación |
| Persistencia | Servicio `sshd_operns` en **TCP/57722** (deshabilitado por defecto) · cuenta local `cisco` · modificación de `/etc/sudoers` y de `/etc/sudoers.d/` · **permisos `4755` en `/usr/bin/sudo`** · claves autorizadas de SSH |
| Canales de salida | **Túneles GRE, mGRE e IPsec**; **GRE sobre MPLS hacia China** en al menos un caso · HTTP(S) en puertos `18xxx` · SSH en puertos `22x22` o `xxx22` |
| Abuso de SNMP | Comunidades por defecto `public` y `private`; **operaciones de escritura SNMP** para cambiar configuración |
| Compresión y cifrado de lo recolectado | `tar -czvf - {0} \| openssl des3 -salt -k password -out {0}.tar.gz`, cadena presente en sus herramientas |
| Capacidad destructiva | **Ninguna documentada en el aviso.** Es un actor de recolección e interceptación |
| Reglas de detección oficiales | **Dos reglas YARA** (`SALT_TYPHOON_CMD1_SFTP_CLIENT`, `SALT_TYPHOON_NEW2_SFTP_CLIENT`) y **una regla Snort** (`sid:1000003`, para `CVE-2023-20198`), publicadas por los firmantes |

## X-2. Artefactos de host y de configuración persistentes

<!-- cti:cards -->

| Categoría | Artefactos | Etiqueta |
|---|---|---|
| **Servicio y puerto de persistencia** | `sshd_operns` en **TCP/57722**, deshabilitado por defecto en la gama de proveedor. `service sshd_operns start` | `persistencia` |
| Cuenta y elevación | Cuenta local `cisco` · `useradd cisco` · `password cisco` · `sudo vi /etc/sudoers` · `/etc/sudoers.d/` · **`chmod 4755 /usr/bin/sudo`** | `privilegios` |
| Listas de control de acceso | `access-list 20`, y `50` o `10` si la primera ya existe. **El indicador no es el nombre: es una entrada que no está en la configuración aprobada** | `autorización` |
| Capturas de paquetes | `mycap` (nombre de sesión) · `mycap.pcap` · `tac.pcap` · `1.pcap` · `bootflash:` como destino · **filtro `match ipv4 protocol tcp any any eq 49`** | `credenciales` |
| Ficheros de las herramientas | `cmd3` · `cmd1` · `new2` · `sft` · `commands.log` | `arsenal` |
| Rutas de compilación filtradas | `C:/work/sync/cmd/cmd3/main.go` · `C:/work/sync_v1/cmd/cmd1/main.go` | `higiene` |
| Cadenas de las reglas YARA oficiales | `monitor capture CAP` · `export ftp://%s:%s@%s%s` · `main.CapExport` · `main.SftpDownload` · `commands.log` · `tar -czvf - {0} \| openssl des3 -salt -k password -out {0}.tar.gz` | `firma` |
| Intérpretes y rutas del dispositivo | `guestshell enable` · `guestshell run bash` · `guestshell disable` · `run guestshell` · `guestshell destroy` · `chvrf` · `dohost` · `tclsh` · `TCLproxy.tcl` · `map.tcl` · `/level/15/exec/-/*` | `ejecución` |
| Extremos del exploit | `/webui_wsma_Http` · `/webui_wsma_Https` · **con doble codificación: `/%2577eb%2575i_%2577sma_Http`** | `acceso` |
| **Señal de equipo parcheado** | Cabecera **`Proxy-Uri-Source`** en la respuesta. **No es un indicador de compromiso: es una comprobación de estado, y es un regalo del aviso** | `verificación` |
| Rangos de puerto observados | SSH en `22x22` o `xxx22` · HTTP(S) en `18xxx` · TACACS+ en `49` · RADIUS en `1812`/`1813` · `57722` | `red` |

## X-3. Lógica de detección prioritaria

> ⚠ **Advertencia previa.** Igual que en `CTI-2026-028` y `CTI-2026-029`, estas
> detecciones **no se despliegan en un agente de punto final**: son
> comprobaciones de configuración, consultas sobre registros de dispositivos de
> red y verificaciones desde fuera del dispositivo. **Y la primera no es una
> detección: es la verificación de parcheo de `D-0`**, que se hace una vez y
> resuelve la mayor parte de la exposición.

<!-- cti:detections -->

**D-0 · CRÍTICO — Verificación de parcheo de los cinco CVE**

```
// NO es una regla. Es una comprobación que se ejecuta una vez y se corrige.
PARA cada dispositivo de borde del inventario:
    ¿CVE-2023-20198 cerrado?  (Cisco IOS XE)            → sí / no / no aplica
    ¿CVE-2023-20273 cerrado?  (Cisco IOS XE)            → sí / no / no aplica
    ¿CVE-2024-21887 cerrado?  (Ivanti Connect/Policy)   → sí / no / no aplica
    ¿CVE-2024-3400  cerrado?  (PAN-OS GlobalProtect)    → sí / no / no aplica
    ¿CVE-2018-0171  cerrado?  (Cisco Smart Install)     → sí / no / no aplica

// Comprobación auxiliar que el propio aviso regala, para los dos de IOS XE:
//   la presencia de la cabecera "Proxy-Uri-Source" en la respuesta
//   indica que el equipo ESTÁ parcheado.

Y LA MISMA PREGUNTA, POR ESCRITO, A LOS PROVEEDORES DE CONECTIVIDAD
Y DE SERVICIOS GESTIONADOS.
```

→ **Es la decisión `E-a` y la hipótesis `H-9`.** Se pone primero y con prioridad crítica porque **el aviso afirma que este actor no usa días cero**: toda su capacidad de acceso inicial depende de que estos cinco CVE sigan abiertos en algún sitio. **Es la tarea de mayor rendimiento de todo el lote de noviembre de 2026**, y se responde en días.

**D-1 · CRÍTICO — Desviación de la configuración de un dispositivo de red respecto de la autorizada**

```
PARA cada dispositivo de red, de forma periódica:
    configuración_actual = volcado desde el repositorio central
    ALERTA CRÍTICA SI difiere de la versión aprobada en alguno de:
        - entradas de lista de control de acceso
        - configuración de servidores de autenticación (TACACS+ / RADIUS)
        - interfaces y definiciones de túnel (GRE, mGRE, IPsec)
        - cuentas locales
        - servicios habilitados
        - comunidades SNMP
        - tabla de rutas estáticas
    Y no existe cambio autorizado que lo explique
```

→ **Investigación inmediata.** Es la primera caza que recomienda el aviso y **la única detección de este informe que funciona aunque el adversario controle el dispositivo**, porque la copia de referencia está fuera de su alcance. Requiere el repositorio de configuración aprobada, que es la decisión `E-d`.

**D-2 · CRÍTICO — Captura de paquetes en un dispositivo de red con filtro de TACACS+**

```
// Sobre registro de comandos del dispositivo (command accounting) o sobre configuración.
comando MATCHES_REGEX "(?i)monitor\\s+capture"
AND ( comando MATCHES_REGEX "(?i)protocol\\s+tcp\\s+any\\s+any\\s+eq\\s+49"
      OR comando MATCHES_REGEX "(?i)monitor\\s+capture\\s+\\w+\\s+export"
      OR comando MATCHES_REGEX "(?i)copy\\s+bootflash:.*\\.pcap\\s+(ftp|tftp)://" )
```

→ **Contención inmediata: aislar el dispositivo del plano de gestión.** El criterio del puerto 49 es concluyente: **una captura de paquetes filtrando TACACS+ en un router de producción no tiene ninguna explicación legítima.** Y la tercera condición —copiar un fichero `.pcap` del almacenamiento interno por FTP o TFTP— es la exfiltración en una línea.

**D-3 · CRÍTICO — Modificación de la configuración del servidor de autenticación, o tráfico de TACACS+ a destino no aprobado**

```
// Por configuración:
comando MATCHES_REGEX "(?i)(tacacs-server|aaa\\s+group\\s+server\\s+tacacs|radius-server)"
AND NOT dentro_de( ventana de cambio aprobada )
```

```
// Por red, que es la variante que no depende del registro del dispositivo:
network.direction == "outbound" AND destination.port == 49
AND destination.ip NOT IN ( <servidores de autenticación aprobados> )
```

```
// Y la condición de segmento, de fidelidad máxima:
destination.port IN ( 49, 1812, 1813 )
AND NOT ( source IN_SUBNET <red de gestión> AND destination IN_SUBNET <red de gestión> )
```

→ Contención inmediata. **Es la detección del procedimiento más grave del expediente.** La tercera variante es la mejor: todo tráfico de autenticación de dispositivos de red debería nacer y morir dentro del segmento de gestión, y cualquier excepción es investigable.

**D-4 · ALTO — Puerto TCP/57722 abierto en un dispositivo de red**

```
// Verificación DESDE FUERA del dispositivo. Nunca desde dentro.
escaneo_externo( dispositivos de red )
AND puerto_abierto IN ( 57722 )
```

```
// Complemento por configuración:
comando MATCHES_REGEX "(?i)service\\s+sshd_operns\\s+start"
OR configuración CONTAINS "sshd_operns"
```

→ Contención inmediata. Corresponde a un servicio que el fabricante deja **deshabilitado por defecto** y que da consola en el sistema operativo subyacente del router. **No hay motivo benigno para encontrarlo activo.**

**D-5 · ALTO — Túnel GRE, mGRE o IPsec no aprobado, o entre sistemas autónomos distintos**

```
// Por configuración:
configuración MATCHES_REGEX "(?i)interface\\s+Tunnel|tunnel\\s+mode\\s+(gre|ipsec)"
AND identificador_de_túnel NOT IN ( <túneles aprobados> )
```

```
// Por flujo:
network.protocol IN ( "gre", "esp" )
AND source.as.number != destination.as.number
AND NOT par_en( <enlaces aprobados entre sistemas autónomos> )
```

→ Investigación prioritaria. **Es la detección de la salida de datos**, que por `KJ-6` no se ve como volumen anómalo sino como un enlace más.

**D-6 · ALTO — FTP o TFTP originados en un dispositivo de red**

```
network.direction == "outbound"
AND source.ip IN ( <inventario de dispositivos de red> )
AND destination.port IN ( 20, 21, 69 )
AND destination.ip NOT IN ( <servidores de respaldo de configuración aprobados> )
```

→ Contención inmediata. **Un router no sube ficheros a Internet.** Es el canal de salida de las capturas de paquetes y de los volcados de configuración.

**D-7 · ALTO — Uso del intérprete de contenedor del dispositivo**

```
comando MATCHES_REGEX
  "(?i)(guestshell\\s+(enable|run|disable|destroy)|run\\s+guestshell|chvrf|dohost)"
AND NOT dentro_de( ventana de cambio aprobada )
```

→ Investigación prioritaria. **Advertencia práctica**: la sección de caza del propio aviso escribe `run guestshel` con una letra de menos. **No copiar esa cadena a una regla**: no encontraría nada. La expresión de arriba está corregida.

**D-8 · MEDIO — Explotación de la vulnerabilidad de IOS XE, incluida la variante con doble codificación**

```
http.request.uri MATCHES_REGEX
  "(?i)(webui_wsma_Http|%2577eb%2575i_%2577sma_Http|%77ebui_wsma_Http)"
```

```
// El aviso publica además una regla Snort oficial para este CVE:
//   sid:1000003
```

→ Investigación prioritaria. **La segunda alternativa de la expresión es la importante**: la doble codificación de URL es precisamente lo que elude un filtro que busque la cadena literal.

**D-9 · MEDIO — Comunidades SNMP por defecto y escritura por SNMP**

```
configuración MATCHES_REGEX "(?i)snmp-server\\s+community\\s+(public|private)\\b"
```

```
network.protocol == "snmp" AND snmp.pdu_type == "set-request"
AND source.ip NOT IN ( <sistemas de gestión autorizados> )
```

→ Investigación en el día para la segunda; **corrección inmediata de configuración** para la primera, que es un hallazgo de exposición y no de compromiso.

**D-10 · MEDIO — Reglas YARA oficiales sobre las herramientas del actor**

```
// Publicadas por los firmantes del aviso:
//   SALT_TYPHOON_CMD1_SFTP_CLIENT
//   SALT_TYPHOON_NEW2_SFTP_CLIENT
// Cadenas características:
strings CONTAINS_ANY (
  "monitor capture CAP",
  "export ftp://%s:%s@%s%s",
  "main.CapExport",
  "main.SftpDownload",
  "commands.log",
  "tar -czvf - {0} | openssl des3 -salt -k password -out {0}.tar.gz" )
```

→ Investigación prioritaria si coincide. **Usar las reglas oficiales del aviso en lugar de estas cadenas**: están mantenidas por los firmantes y son preferentes. Se incluyen aquí para que un analista sin acceso al paquete pueda construir una búsqueda equivalente.

> ⚠ **Regla de operación.** Igual que en `CTI-2026-029`, el orden importa y
> está invertido respecto de lo habitual: **`D-0` no es una detección y va
> primero.**
>
> Este actor no usa días cero. Toda su capacidad de acceso inicial descansa en
> cinco vulnerabilidades publicadas, la más antigua de 2018. **Cerrarlas elimina
> la etapa 01 completa**, y las nueve reglas restantes de este §X-3 cubren lo
> que pasa si se omitió ese paso.
>
> Dicho de otro modo: de los siete informes de este lote, **éste es el único cuya
> exposición principal se resuelve con una tarea de gestión de parches de una
> semana.** Si sólo se hace una cosa de todo el lote, que sea `D-0`.

## X-4. Consultas de caza

```bash
#!/bin/sh
# H-1, H-2, H-3, H-7, H-8 · Comprobación de un dispositivo Cisco IOS XE / IOS.
# EJECUTAR CON AUTORIZACIÓN. Y leer la advertencia del final.

echo "=== Listas de control de acceso: contrastar con la configuracion aprobada ==="
# El actor anade sus direcciones a una ACL existente, con nombres mundanos (20, 50, 10).
show access-lists
show running-config | section access-list

echo "=== Servidores de autenticacion: el procedimiento mas grave del expediente ==="
show running-config | section tacacs
show running-config | section radius
show running-config | section aaa
echo "    (comprobar que las direcciones son las aprobadas y que el secreto NO es tipo 7)"

echo "=== Capturas de paquetes activas: el filtro del puerto 49 es concluyente ==="
show monitor capture
show running-config | include monitor.capture
echo "--- ficheros .pcap en el almacenamiento interno ---"
dir bootflash: | include .pcap
dir flash: | include .pcap

echo "=== Interprete de contenedor del dispositivo ==="
show guestshell
show iox
echo "    (en configuracion endurecida: guestshell disable y no iox)"

echo "=== Tuneles definidos: contrastar con los enlaces aprobados ==="
show running-config | include interface.Tunnel|tunnel.mode|tunnel.source|tunnel.destination
show ip interface brief | include Tunnel

echo "=== Cuentas locales: buscar las no inventariadas, y 'cisco' ==="
show running-config | include username

echo "=== SNMP: comunidades por defecto y modo de acceso ==="
show running-config | include snmp-server.community

echo "=== Servidor web del dispositivo ==="
show running-config | include ip.http
echo "    (en configuracion endurecida: no ip http server)"

echo "=== Smart Install: CVE-2018-0171 ==="
show vstack config
echo "    (debe estar desactivado)"

# ADVERTENCIA: todo esto se ejecuta EN el dispositivo y por tanto es falseable
# por un adversario con control de el. Las verificaciones fiables son:
#   (1) comparar la configuracion CONTRA EL REPOSITORIO APROBADO (H-1, D-1),
#   (2) escanear los puertos DESDE FUERA (H-2, D-4),
#   (3) revisar los flujos EN LA RED, no en el equipo (H-4, H-5, H-6).
```

```kql
// H-4 · Trafico de TACACS+ y RADIUS hacia destinos no aprobados o fuera del segmento de gestion.
// Es la deteccion de la redireccion del servidor de autenticacion.
let AutenticadoresAprobados = dynamic(["10.0.0.0/8"]);   // <-- ajustar
let RedDeGestion           = dynamic(["10.255.0.0/16"]); // <-- ajustar
NetworkFlowLogs                                          // <-- tabla propia de flujos
| where DestinationPort in (49, 1812, 1813)
| extend DestinoAprobado = ipv4_is_in_any_range(DestinationIP, AutenticadoresAprobados),
         OrigenEnGestion = ipv4_is_in_any_range(SourceIP,      RedDeGestion),
         DestinoEnGestion= ipv4_is_in_any_range(DestinationIP, RedDeGestion)
| where not(DestinoAprobado) or not(OrigenEnGestion and DestinoEnGestion)
| summarize Flujos = count(), Bytes = sum(BytesSent),
            Primero = min(TimeGenerated), Ultimo = max(TimeGenerated)
          by SourceIP, DestinationIP, DestinationPort, DestinoAprobado
| order by Flujos desc
```

```kql
// H-5 · Tuneles GRE o IPsec entre sistemas autonomos distintos.
// Es la deteccion de la salida de datos, que no se ve por volumen.
NetworkFlowLogs
| where Protocol in ("gre", "esp", "47", "50")
| extend AsOrigen = SourceASN, AsDestino = DestinationASN
| where isnotempty(AsOrigen) and isnotempty(AsDestino) and AsOrigen != AsDestino
| summarize Flujos = count(), Bytes = sum(BytesSent), Dias = dcount(bin(TimeGenerated, 1d)),
            Primero = min(TimeGenerated), Ultimo = max(TimeGenerated)
          by SourceIP, DestinationIP, Protocol, AsOrigen, AsDestino
| order by Bytes desc
```

```kql
// H-6 · FTP y TFTP originados en dispositivos de red. Un router no sube ficheros a Internet.
let DispositivosDeRed = externaldata(ip: string, nombre: string, rol: string)
    [@"<inventario de dispositivos de red>"];
NetworkFlowLogs
| where DestinationPort in (20, 21, 69)
| join kind=inner ( DispositivosDeRed | project SourceIP = ip, nombre, rol ) on SourceIP
| summarize Flujos = count(), Bytes = sum(BytesSent), Destinos = make_set(DestinationIP, 20)
          by SourceIP, nombre, rol, DestinationPort
| order by Bytes desc
```

```kql
// H-3 y H-7 · Comandos sospechosos en el registro de comandos de los dispositivos.
// Requiere command accounting activado, que el propio aviso recomienda.
NetworkDeviceCommandLog                                  // <-- tabla propia
| where Command matches regex @"(?i)monitor\s+capture"
     or Command matches regex @"(?i)protocol\s+tcp\s+any\s+any\s+eq\s+49"
     or Command matches regex @"(?i)copy\s+bootflash:.*\.pcap\s+(ftp|tftp)://"
     or Command matches regex @"(?i)guestshell\s+(enable|run|disable|destroy)"
     or Command matches regex @"(?i)run\s+guestshell"
     or Command matches regex @"(?i)\b(chvrf|dohost|tclsh)\b"
     or Command matches regex @"(?i)service\s+sshd_operns"
     or Command matches regex @"(?i)(tacacs-server|radius-server)\s+host"
     or Command matches regex @"(?i)useradd\s+cisco"
     or Command matches regex @"(?i)chmod\s+4755\s+/usr/bin/sudo"
| extend Severidad = case(
      Command matches regex @"(?i)eq\s+49" or Command matches regex @"(?i)sshd_operns"
        or Command matches regex @"(?i)chmod\s+4755", "CRITICA",
      Command matches regex @"(?i)monitor\s+capture" or Command matches regex @"(?i)tacacs-server", "ALTA",
      "MEDIA")
| project TimeGenerated, Device, User, Command, Severidad
| order by Severidad asc, TimeGenerated desc
```

```yaml
# Sigma — Captura de paquetes con filtro de TACACS+ en un dispositivo de red
# Autor: Célula CTI · Fecha: 2026-11-17 · ATT&CK: T1040, T1602.002
# Nivel: critical · Estado: estable
# Una captura filtrando el puerto 49 en un router de produccion no tiene uso legitimo.
title: Captura de paquetes en dispositivo de red filtrando autenticacion TACACS+
id: 7d2b5e41-8a39-4c17-b0e6-3f94c2a8d571
status: stable
description: >
  AA25-239A documenta que el actor activa la captura de paquetes nativa del
  dispositivo con el filtro "match ipv4 protocol tcp any any eq 49", exporta la
  captura al almacenamiento interno y la envia por FTP o TFTP. El puerto 49 es
  TACACS+: lo que captura son las credenciales de administracion de la red.
references:
  - https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a
logsource:
  product: cisco
  service: aaa
detection:
  captura:
    CommandLine|contains: 'monitor capture'
  filtro_tacacs:
    CommandLine|contains: 'eq 49'
  exportacion:
    CommandLine|re: '(?i)copy\s+bootflash:.*\.pcap\s+(ftp|tftp)://'
  condition: (captura and filtro_tacacs) or exportacion
falsepositives:
  - Diagnostico autorizado de problemas de autenticacion, con ticket y ventana.
    Debe ser excepcional y estar registrado.
level: critical
```

```yaml
# Sigma — Activacion del servicio de consola del anfitrion en IOS XR
# Autor: Célula CTI · Fecha: 2026-11-17 · ATT&CK: T1569, T1136.001, T1068
# Nivel: critical · Estado: estable
title: Servicio sshd_operns activado o puerto 57722 abierto en un dispositivo de red
id: 3e8c0f72-5b46-49da-8217-6a0d1b9e74c3
status: stable
description: >
  sshd_operns esta deshabilitado por defecto en IOS XR y da acceso a una consola
  en el sistema operativo Linux subyacente del router, en el puerto TCP 57722.
  El actor lo activa, crea una cuenta local y modifica el fichero de elevacion de
  privilegios y los permisos del binario de elevacion.
logsource:
  product: cisco
  service: aaa
detection:
  servicio:
    CommandLine|contains: 'sshd_operns'
  cuenta:
    CommandLine|contains|all:
      - 'useradd'
      - 'cisco'
  elevacion:
    CommandLine|re: '(?i)chmod\s+4755\s+/usr/bin/sudo'
  sudoers:
    CommandLine|contains: '/etc/sudoers'
  condition: servicio or cuenta or elevacion or sudoers
falsepositives:
  - Ninguno conocido. El servicio esta deshabilitado por defecto por el fabricante.
level: critical
```

```yaml
# Sigma — Explotacion de CVE-2023-20198, incluida la variante con doble codificacion
# Autor: Célula CTI · Fecha: 2026-11-17 · ATT&CK: T1190, T1027.010
# Nivel: high · Estado: estable
# El aviso publica ademas una regla Snort oficial (sid:1000003) para este CVE.
title: Solicitud a los extremos WSMA de la interfaz web de Cisco IOS XE
id: 9a4e7c16-2d58-4b03-91fe-5c7b0a2e8d64
status: stable
description: >
  CVE-2023-20198 permite crear cuentas administrativas mediante los extremos
  /webui_wsma_Http y /webui_wsma_Https. El actor los solicita con DOBLE
  CODIFICACION de URL para eludir filtros que busquen la cadena literal.
logsource:
  category: webserver
detection:
  literal:
    cs-uri-stem|contains:
      - 'webui_wsma_Http'
      - 'webui_wsma_Https'
  codificado:
    cs-uri-stem|contains:
      - '%2577eb%2575i_%2577sma'
      - '%77ebui_wsma'
      - '%2577sma'
  condition: literal or codificado
falsepositives:
  - Escaneres de vulnerabilidades autorizados. Excluir por direccion de origen.
level: high
```

## X-5. Mitigaciones de configuración con efecto directo

> Las once primeras son **las que el propio aviso publica**, con nuestra
> ordenación por rendimiento.

| Control | Corta |
|---|---|
| **Parchear los cinco CVE de borde con prioridad** | **La etapa 01 completa.** El actor no usa días cero: cerrar estos cinco elimina su vía de acceso documentada. Decisión `E-a` |
| **Plano de gestión aislado**, con red dedicada sin fuga de rutas ni salida a Internet, y policía de plano de control | El acceso administrativo a los dispositivos, que es por donde se llega a la etapa 03 |
| **Desactivar Smart Install** | `CVE-2018-0171`, el más antiguo de los cinco |
| **Desactivar la interfaz web no cifrada** del dispositivo, y usar sólo la cifrada si es imprescindible | La vía de `CVE-2023-20198` y `CVE-2023-20273` |
| **Desactivar el intérprete de contenedor del dispositivo** donde no se use, y verificarlo | La etapa 02: sin intérprete, no hay consola en el dispositivo |
| **Desactivar `sshd_operns` en IOS XR**, y revisar el fichero de elevación de privilegios y su directorio | La persistencia de la etapa 04 y el puerto `TCP/57722` |
| **SNMPv3 con autenticación y cifrado; retirar las comunidades `public` y `private`** | El abuso de SNMP para leer configuración y para escribir cambios |
| **Sólo SSH versión 2**, y deshabilitar la salida de terminal no cifrada | La administración remota en claro |
| **Terminar todas las listas de control de acceso con una denegación explícita registrada** | Hace visible el tráfico que no encaja, incluido el del adversario si consigue añadirse |
| **Registro de comandos ejecutados** (*command accounting*) en todos los dispositivos | No corta nada, pero **es la condición de existencia de `D-2`, `D-3` y `D-7`** |
| **Credenciales locales de los dispositivos en formato de cifrado no reversible, y secretos compartidos en el formato reforzado** | La recuperación del secreto de TACACS+ del propio fichero de configuración, documentada en al menos un caso |
| **Repositorio de configuración aprobada y comparación periódica automática** | La etapa 03 completa. **Es la única detección que funciona si el adversario controla el dispositivo.** Decisión `E-d` |
| **Monitorizar el servidor TACACS+ o RADIUS con el escrutinio de un controlador de dominio** | El objetivo final de la etapa 03, y converge con la decisión equivalente de `CTI-2026-028` |
| **Escaneo externo periódico de los puertos de los dispositivos de red** | `TCP/57722` y cualquier otro puerto no justificado. Desde dentro puede estar oculto |

---

## 14. Brechas de inteligencia y nuevos requisitos de colección

| # | Brecha | Impacto en el juicio | Requisito propuesto | Prioridad |
|---|---|---|---|---|
| G-1 | **Sin inventario de parcheo del equipamiento de borde, propio y de proveedores** | Deja sin responder `X-1` y `X-2`, y con ellas la decisión `E-a`. **No es una brecha de inteligencia: es la tarea más barata y de mayor consecuencia de todo el lote** | Ejecutar `D-0` y `H-9`, y preguntar por escrito a los proveedores de conectividad | **Crítica** |
| G-2 | **No se descargó el paquete STIX que el aviso publica** | El Anexo A de este informe es una copia con fecha de los indicadores del aviso. **El paquete oficial puede contener más y se mantiene actualizado** | Descargar e ingerir el paquete oficial. Es la decisión `E-f` | Alta |
| G-3 | **La identificación de `GhostEmperor` como eslabón de la fusión es nuestra**, no de ninguna fuente | `KJ-3` tiene confianza moderada por esto. **Es el hallazgo central del informe y el que menos respaldo externo tiene** | Buscar si algún proveedor ha publicado una comparación entre `GhostEmperor` y FamousSparrow. Indicador `I-2` | Alta |
| G-4 | **Actividad contra telecomunicaciones sudamericanas afirmada por una fuente de proveedor y no verificable**, con un nombre de implante que aparece en otro ecosistema | **Es la única pieza del expediente con posible relevancia regional directa**, y no se sostiene | Localizar el informe original de ese proveedor y determinar su base. Indicador `I-9` | **Crítica** |
| G-5 | Las cifras de 200 empresas y más de 80 países no están en el aviso | `KJ-8` queda en confianza moderada. No afecta a ninguna decisión | Localizar la declaración original del FBI | Media |
| G-6 | **Sin respuesta de los proveedores de conectividad sobre su propio estado de parcheo y de configuración** | **Es la mitad de nuestra exposición**: este actor vive en el equipamiento del operador, no en el nuestro, y `KJ-9` depende de ello | Pregunta formal contractual. Es `X-2` | **Crítica** |
| G-7 | Sin repositorio de configuración aprobada de los dispositivos de red | Deja ciega `H-1` y `D-1`, que son la detección de mayor valor del informe. Decisión `E-d` | Proyecto de gestión de configuración de red | Alta |
| G-8 | **Si la noticia errónea de septiembre de 2026 entró en alguna evaluación de riesgo de la organización** | Es `X-15`. Si entró, hay inteligencia falsa circulando en nuestros propios registros | Revisar el registro de riesgos y corregir. Decisión `E-h` | Alta |
| G-9 | Versiones afectadas por producto para cada uno de los cinco CVE | El aviso no las da. Complica la verificación de `D-0`, aunque los boletines de los fabricantes sí las publican | Consultar los boletines de Cisco, Ivanti y Palo Alto | Media |
| G-11 | **No se ha leído la declaración original de Microsoft** que afirma la identidad de los tres actores, y no existe publicación técnica que la sostenga | **Es la brecha que decidiría toda la cuestión de §O-1 y el valor de `KJ-4`.** Mientras no haya base publicada, la equivalencia no es utilizable en ninguna de las dos direcciones, y ésa es la posición del informe | Localizar la declaración original y vigilar cualquier publicación técnica de Microsoft al respecto. Indicador `I-3` | **Crítica** |
| G-10 | Si las coberturas que publicaron la equivalencia como hecho se rectifican | Indicador `I-1`. **Lo más probable es que no**, y en ese caso la corrección queda sólo en nuestro producto y hay que mantenerla viva | Vigilancia. Y mantener la corrección en las revisiones de `CTI-2026-017` | Media |

---

# ANEXOS

## Anexo A — Indicadores de compromiso

> ⚠ **Leer antes de usar. Dos advertencias, y la primera la hace el propio
> aviso.**
>
> **Primera, de vigencia.** El aviso declara expresamente que las direcciones
> que publica, observadas entre **agosto de 2021 y junio de 2025**, **pueden no
> estar vigentes y deben verificarse antes de bloquearlas**. Esa advertencia es
> de los firmantes, no nuestra, y se hereda íntegra.
>
> **Segunda, de procedencia.** El aviso publica su propio **paquete STIX 2.1**,
> que es la fuente preferente para ingesta automática: está mantenida por los
> firmantes y puede actualizarse. **Lo que sigue es una copia con fecha**, útil
> para lectura humana y para el índice con contexto de este repositorio, y
> subordinada al original. Es la decisión `E-f` y la brecha `G-2`.
>
> **Y una nota sobre dónde está el valor:** a diferencia del resto de este lote,
> aquí el nivel más útil del Anexo A **no son los indicadores de red sino la
> sección A.1**: cinco CVE con parche disponible. Esa sección se resuelve con
> una tarea de inventario y cierra la etapa de acceso inicial completa.

### A.1 — Vulnerabilidades explotadas · **la sección que hay que atender primero**

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| cve | `CVE-2023-20198` | **Cisco IOS XE.** Elusión de autenticación que permite crear cuentas administrativas, mediante los extremos `/webui_wsma_Http` y `/webui_wsma_Https`, **solicitados con doble codificación de URL**. El aviso publica una regla Snort oficial para él (`sid:1000003`) | Alta | Sin caducidad: la decisión es de parcheo | **Parchear y verificar** (`D-0`) |
| cve | `CVE-2023-20273` | **Cisco IOS XE**, interfaz web. Inyección de comandos y escalada posterior a la autenticación. **Encadenado con el anterior** | Alta | Sin caducidad | **Parchear y verificar** |
| cve | `CVE-2024-21887` | **Ivanti Connect Secure e Ivanti Policy Secure.** Inyección de comandos, **encadenada con `CVE-2023-46805`** | Alta | Sin caducidad | **Parchear y verificar** |
| cve | `CVE-2024-3400` | **Palo Alto Networks PAN-OS, GlobalProtect.** Ejecución remota sin autenticación en ciertas versiones y configuraciones | Alta | Sin caducidad | **Parchear y verificar** |
| cve | `CVE-2018-0171` | **Cisco IOS e IOS XE, Smart Install.** Ejecución remota de código. **Publicado en 2018: ocho años con parche disponible.** El actor usa `siet.py` para explotarlo | Alta | Sin caducidad | **Parchear, y desactivar Smart Install** |
| artefacto | `Proxy-Uri-Source` | **No es un indicador de compromiso: es lo contrario.** El aviso señala que la presencia de esta cabecera en la respuesta indica que el equipo **está parcheado** frente a la vulnerabilidad de IOS XE. Comprobación de estado | Alta | Sin caducidad | **Verificación de parcheo** |
| artefacto | `Fortinet` · `Juniper` · `Microsoft Exchange` · `Nokia` · `Sierra Wireless` · `SonicWall` | **Otros fabricantes que el aviso señala como posiblemente afectados**, sin CVE concreto. Amplía el alcance del inventario de `X-3` | Media | Sin caducidad | Inventario y vigilancia |

### A.2 — Artefactos de host, de configuración y de protocolo (el componente que no caduca)

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| pattern | `monitor capture ... match ipv4 protocol tcp any any eq 49` | **La firma más concluyente del expediente**: una captura de paquetes en un dispositivo de red filtrando el puerto de TACACS+. **No tiene uso legítimo en producción** | Alta | **Sin caducidad** | **Detección** (`D-2`) |
| pattern | `copy bootflash:<fichero>.pcap ftp://` o `tftp://` | Exportación de la captura desde el almacenamiento interno del dispositivo hacia una dirección externa. **La exfiltración en una línea** | Alta | **Sin caducidad** | **Detección** (`D-2`, `D-6`) |
| filename | `mycap` · `mycap.pcap` · `tac.pcap` · `1.pcap` · `commands.log` | Nombres de sesión y de fichero de captura observados, y fichero de registro de comandos de las herramientas | Alta | Sin caducidad | Caza |
| artefacto | `sshd_operns` | **Servicio de IOS XR deshabilitado por defecto** que da consola en el sistema operativo subyacente del router. `service sshd_operns start` | Alta | **Sin caducidad** | **Detección** (`D-4`) |
| puerto | `57722` | Puerto TCP de escucha de ese servicio. **Verificar desde fuera del dispositivo** | Alta | **Sin caducidad** | **Detección** (`D-4`, `H-2`) |
| puerto | `49` | TACACS+. Objetivo de la captura de paquetes y de la redirección del servidor | Alta | Sin caducidad | Caza (`D-3`, `H-4`) |
| puerto | `1812` · `1813` | RADIUS. Mismo papel que el anterior | Alta | Sin caducidad | Caza (`H-4`) |
| pattern | `22x22` · `xxx22` · `18xxx` | **Rangos de puerto no estándar observados**: SSH en los dos primeros patrones, HTTP y HTTPS en el tercero | Media | Sin caducidad | Caza |
| artefacto | `useradd cisco` · `password cisco` | **Cuenta local creada en el dispositivo.** La única cuenta que el aviso nombra | Alta | Sin caducidad | **Detección** (`D-4`) |
| pattern | `chmod 4755 /usr/bin/sudo` | **Activación del bit de suplantación de propietario en el binario de elevación de privilegios.** Sin uso legítimo | Alta | **Sin caducidad** | **Detección** (`D-4`) |
| path | `/etc/sudoers` · `/etc/sudoers.d/` | Ficheros de configuración de elevación de privilegios que el actor modifica | Alta | Sin caducidad | Caza |
| artefacto | `access-list 20` · `access-list 50` · `access-list 10` | **Nombres de lista de control de acceso que el actor usa** para añadir sus direcciones. **El indicador no es el nombre, que es mundano: es una entrada que no está en la configuración aprobada** | Media | Sin caducidad | Caza con contraste (`D-1`, `H-1`) |
| pattern | `guestshell enable` · `guestshell run bash` · `guestshell disable` · `guestshell destroy` · `run guestshell` · `chvrf` · `dohost` | **Uso del intérprete de contenedor Linux integrado en el dispositivo.** *Nota: la sección de caza del propio aviso escribe `run guestshel` con una letra de menos; no copiar esa cadena a una regla* | Alta | Sin caducidad | Detección (`D-7`) |
| artefacto | `tclsh` · `TCLproxy.tcl` · `map.tcl` · `/level/15/exec/-/*` | Intérprete Tcl del sistema operativo del router y rutas de ejecución privilegiada | Alta | Sin caducidad | Caza |
| pattern | `/webui_wsma_Http` · `/webui_wsma_Https` · `/%2577eb%2575i_%2577sma_Http` | Extremos del exploit de IOS XE. **La tercera variante, con doble codificación de URL, es la que elude un filtro de cadena literal** | Alta | Sin caducidad | **Detección** (`D-8`) |
| pattern | `snmp-server community public` · `snmp-server community private` | **Comunidades SNMP por defecto** que el actor aprovecha. **Hallazgo de exposición, no de compromiso** | Alta | Sin caducidad | **Corrección de configuración** (`D-9`) |
| pattern | `tunnel mode gre` · `tunnel mode ipsec` · GRE entre sistemas autónomos distintos | **Canal de salida del actor.** No hay volumen anómalo que detectar: hay un enlace | Alta | Sin caducidad | Detección (`D-5`, `H-5`) |
| pattern | `tar -czvf - {0} \| openssl des3 -salt -k password -out {0}.tar.gz` | **Cadena presente en las herramientas del actor** y usada en las reglas YARA oficiales. Compresión y cifrado de lo recolectado, con contraseña literal `password` | Alta | Sin caducidad | **Detección** (`D-10`) |
| pattern | `monitor capture CAP` · `export ftp://%s:%s@%s%s` · `main.CapExport` · `main.SftpDownload` | Cadenas características de las herramientas, usadas en las reglas YARA oficiales | Alta | Sin caducidad | **Detección** (`D-10`) |
| herramienta | `SALT_TYPHOON_CMD1_SFTP_CLIENT` · `SALT_TYPHOON_NEW2_SFTP_CLIENT` | **Nombres de las dos reglas YARA oficiales publicadas por los firmantes.** Usar éstas en lugar de las cadenas, porque están mantenidas | Alta | Sin caducidad | **Desplegar las reglas oficiales** |
| herramienta | `sid:1000003` | **Regla Snort oficial del aviso** para `CVE-2023-20198` | Alta | Sin caducidad | **Desplegar** |

### A.3 — Herramientas del actor con hash publicado

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| sha256 | `8b448f47e36909f3a921b4ff803cf3a61985d8a10f0fe594b405b92ed0fc21f1` | **`cmd3`**, cliente de transferencia propio. 3 506 176 bytes, versión `v1.0`. Ruta de compilación filtrada: `C:/work/sync/cmd/cmd3/main.go` | Alta | 2027-06-30 | Bloqueo + retrohunt |
| md5 | `eba9ae70d1b22de67b0eba160a6762d8` | `cmd3`, el mismo fichero en MD5 | Alta | 2027-06-30 | Bloqueo + retrohunt |
| sha256 | `f2bbba1ea0f34b262f158ff31e00d39d89bbc471d04e8fca60a034cabe18e4f4` | **`cmd1`**, cliente de transferencia propio. 3 358 720 bytes, versión `V20240816`. Ruta de compilación filtrada: `C:/work/sync_v1/cmd/cmd1/main.go`. **Cubierto por la regla YARA oficial `SALT_TYPHOON_CMD1_SFTP_CLIENT`** | Alta | 2027-06-30 | Bloqueo + retrohunt |
| md5 | `33e692f435d6cf3c637ba54836c63373` | `cmd1`, el mismo fichero en MD5 | Alta | 2027-06-30 | Bloqueo + retrohunt |
| sha256 | `da692ea0b7f24e31696f8b4fe8a130dbbe3c7c15cea6bde24cccc1fb0a73ae9e` | **`new2`**, cliente de transferencia. **Cubierto por la regla YARA oficial `SALT_TYPHOON_NEW2_SFTP_CLIENT`.** El aviso no publica su MD5 | Alta | 2027-06-30 | Bloqueo + retrohunt |
| sha256 | `a1abc3d11c16ae83b9a7cf62ebe6d144dfc5e19b579a99bad062a9d31cf30bfe` | **`sft`**, cliente de transferencia. El aviso no publica su MD5 | Alta | 2027-06-30 | Bloqueo + retrohunt |
| herramienta | `siet.py` | Utilidad pública de explotación de Smart Install (`CVE-2018-0171`). **Herramienta de tercero: su presencia no atribuye** | Alta | Sin caducidad | Caza — no atribuye |
| herramienta | `STOWAWAY` · `wodSSHServer` | Proxy y servidor SSH de terceros usados por el actor | Alta | Sin caducidad | Caza — no atribuyen |

### A.4 — Direcciones publicadas por el aviso · **VERIFICAR VIGENCIA ANTES DE BLOQUEAR**

> ⚠ **Advertencia de los firmantes, no nuestra.** Estas direcciones se
> observaron entre **agosto de 2021 y junio de 2025**, y el aviso declara
> expresamente que **pueden no estar vigentes** y que deben verificarse antes de
> bloquearlas. **Varias pertenecen a proveedores de alojamiento con clientes
> legítimos.** La acción permitida que se asigna refleja esa cautela.

<!-- cti:ioc -->

| Tipo | Valor | Contexto | Confianza | Caducidad | Acción permitida |
|---|---|---|---|---|---|
| ipv4 | `1.222.84.29` · `14.143.247.202` · `5.181.132.95` · `23.227.196.22` · `23.227.199.77` · `23.227.202.253` | Direcciones del aviso, observadas entre 2021-08 y 2025-06 | Media | 2026-12-31 | **Bloqueo tras verificar vigencia y titularidad** |
| ipv4 | `37.120.239.52` · `38.71.99.145` · `43.254.132.118` · `45.59.118.136` · `45.59.120.171` | Direcciones del aviso | Media | 2026-12-31 | **Bloqueo tras verificar vigencia** |
| ipv4 | `45.61.128.29` · `45.61.132.125` · `45.61.133.31` · `45.61.133.61` · `45.61.133.77` · `45.61.133.79` | Direcciones del aviso. **Bloque contiguo: indicio de proveedor compartido** | Media | 2026-12-31 | **Bloqueo tras verificar vigencia** |
| ipv4 | `45.61.133.157` · `45.61.134.134` · `45.61.134.223` · `45.61.149.62` · `45.61.149.200` · `45.61.151.12` | Direcciones del aviso. Mismo bloque contiguo | Media | 2026-12-31 | **Bloqueo tras verificar vigencia** |
| ipv4 | `45.61.154.130` · `45.61.159.25` · `45.61.165.157` · `45.125.64.195` · `45.125.67.144` | Direcciones del aviso | Media | 2026-12-31 | **Bloqueo tras verificar vigencia** |
| ipv4 | `45.125.67.226` · `45.146.120.210` · `45.146.120.213` · `59.148.233.250` · `61.19.148.66` · `63.141.234.109` | Direcciones del aviso | Media | 2026-12-31 | **Bloqueo tras verificar vigencia** |
| ipv4 | `63.245.1.34` · `74.48.78.66` · `74.48.78.116` · `74.48.84.119` · `85.195.89.94` · `89.41.26.142` | Direcciones del aviso | Media | 2026-12-31 | **Bloqueo tras verificar vigencia** |
| ipv4 | `89.117.1.147` · `89.117.2.39` · `91.231.186.227` · `91.245.253.99` · `103.7.58.162` · `103.169.91.231` | Direcciones del aviso | Media | 2026-12-31 | **Bloqueo tras verificar vigencia** |
| ipv4 | `103.199.17.238` · `103.253.40.199` · `104.194.129.137` · `104.194.147.15` · `104.194.150.26` · `104.194.153.181` | Direcciones del aviso | Media | 2026-12-31 | **Bloqueo tras verificar vigencia** |
| ipv4 | `104.194.154.150` · `104.194.154.222` · `107.189.15.206` · `142.171.227.16` · `144.172.76.213` · `144.172.79.4` | Direcciones del aviso | Media | 2026-12-31 | **Bloqueo tras verificar vigencia** |
| ipv4 | `146.70.24.144` · `146.70.79.68` · `146.70.79.81` · `167.88.164.166` · `167.88.172.70` · `167.88.173.58` | Direcciones del aviso | Media | 2026-12-31 | **Bloqueo tras verificar vigencia** |
| ipv4 | `167.88.173.158` · `167.88.173.252` · `167.88.175.175` · `167.88.175.231` · `172.86.65.145` · `172.86.70.73` | Direcciones del aviso | Media | 2026-12-31 | **Bloqueo tras verificar vigencia** |
| ipv4 | `172.86.80.15` · `172.86.101.123` · `172.86.102.83` · `172.86.106.15` · `172.86.106.39` · `172.86.106.234` | Direcciones del aviso. **Bloque contiguo** | Media | 2026-12-31 | **Bloqueo tras verificar vigencia** |
| ipv4 | `172.86.108.11` · `172.86.124.235` · `190.131.194.90` · `193.43.104.185` · `193.56.255.210` · `193.239.86.132` | Direcciones del aviso | Media | 2026-12-31 | **Bloqueo tras verificar vigencia** |
| ipv4 | `193.239.86.146` · `212.236.17.237` | Direcciones del aviso | Media | 2026-12-31 | **Bloqueo tras verificar vigencia** |
| ipv6 | `2001:41d0:700:65dc::f656:929f` | Dirección IPv6 del aviso. **Una de las dos únicas IPv6 publicadas** | Media | 2026-12-31 | **Bloqueo tras verificar vigencia** |
| ipv6 | `2a10:1fc0:7::f19c:39b3` | Segunda dirección IPv6 del aviso | Media | 2026-12-31 | **Bloqueo tras verificar vigencia** |

> **Nota de recuento y de higiene.** El aviso publica **86 entradas de
> dirección: 84 IPv4 y 2 IPv6**, y esta tabla recoge **las 86, sin omisiones**.
> El recuento se ha verificado programáticamente contra la lista del aviso: no
> sobra ni falta ninguna.
>
> **Esa verificación corrigió dos errores en la emisión de este informe**, y se
> consignan aquí porque la trazabilidad de los indicadores es parte del producto:
> la tabla contenía inicialmente las direcciones `37.221.64.202` y
> `45.80.208.66`, **que no están en el aviso** y que proceden, respectivamente,
> del expediente de `CTI-2026-026` y de la lista del clúster `OceanGate` del
> expediente de `CTI-2026-017`. Fueron contaminación entre expedientes durante la
> redacción y **se han retirado**. Véase el Anexo G.
>
> **Quien necesite el conjunto canónico y actualizado debe usar el paquete STIX
> del propio aviso** (decisión `E-f`, brecha `G-2`), que es la fuente preferente.
>
> **El aviso no publica ningún dominio.**

## Anexo B — Fuentes y valoración

| # | Fuente | Disciplina | Fiab. | Cred. | Notas de sesgo |
|---|---|---|---|---|---|
| 1 | **Aviso conjunto `AA25-239A`**, «Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System». v1.0 del **2025-08-27**, v1.1 del **2025-09-03**. **23 agencias de 13 países** — **leído íntegro y en original** | **OSINT oficial multilateral** | **A** | **1** | **La mejor fuente de los siete informes de este lote**, y la única que recibe credibilidad 1: su contenido está corroborado por el acto mismo de que veintitrés agencias de trece países lo cosuscriban. Aporta CVE, comandos literales, hashes con tamaño, 86 direcciones, mapeo ATT&CK v17 y D3FEND, dos reglas YARA, una Snort y consultas de caza. **Sesgos declarables**: (a) atribuye a China y nombra tres empresas chinas, lo que es un acto con consecuencias de sanción y por tanto no neutral; (b) **enumera cinco nombres de industria sin aclarar que no son expedientes intercambiables**, y de esa ambigüedad sale el error de `KJ-4`; (c) contiene al menos una errata tipográfica en su propia sección de caza (§T-4, `D-7`); (d) advierte expresamente que sus direcciones pueden estar caducadas |
| 2 | ESET, análisis de la campaña latinoamericana de FamousSparrow y del implante `SparroWocky`, **2026-09-17** — usado aquí **sólo para la separación de `KJ-4`** | OSINT comercial de primera mano | **B** | **2** | **Fuente de la corrección**: es quien hizo el análisis, lo atribuye a FamousSparrow y **rastrea los dos actores por separado**. Su valoración es la que prevalece sobre las coberturas que la reinterpretaron. Analizado en detalle en `CTI-2026-017` |
| 3 | Declaraciones del FBI de **agosto de 2025** (al menos 200 empresas en más de 80 países) y de **febrero de 2026** (amenaza en curso) — por vía secundaria | OSINT oficial estatal, vía secundaria | **B** | **3** | Fuente de `KJ-8`. **Estas cifras NO están en el aviso oficial leído**, y por eso el juicio queda en confianza moderada |
| 4 | Coberturas de prensa especializada de **septiembre de 2026** que atribuyeron la campaña de `SparroWocky` a este actor — conocidas por titulares y resúmenes | Prensa especializada | **C** | **4** | **Son el objeto de `KJ-4`, no su fundamento.** Se consignan porque la existencia del error es el hallazgo. No se leyeron íntegras (§3.3-vii) |
| 5 | Fuente de proveedor que afirma actividad de este actor contra telecomunicaciones sudamericanas con tres implantes nombrados | OSINT comercial | **C** | **4** | **No se sostiene en este informe.** No verificable contra fuente primaria, y **uno de los nombres de implante aparece en el expediente de `CTI-2026-017` v1.2 asociado a otro ecosistema**. Brecha `G-4`, indicador `I-9`. **Es la única pieza con posible relevancia regional directa y por eso su resolución es crítica** |
| 6 | Inteligencia de amenazas de Google, campaña china-nexus contra telecomunicaciones desmantelada en 2026 | OSINT comercial de primera mano, vía secundaria | **B** | **2** | Se consigna **por una negación explícita**: esa fuente afirma **no ver solapamiento con este actor**. Una negación de equivalencia hecha por quien tiene la telemetría es escasa y valiosa (§O-1, bloque 2, y §O-2) |
| 7 | Perfiles de proveedor y respuestas al aviso (SafeBreach, AttackIQ, Picus, Forward Networks, Brandefense, deepstrike y otros) | OSINT comercial agregado | **C** | **3** | Usados para corroborar el mapeo de técnicas y las consultas de caza del aviso. **Uno aporta la lista de los cinco CVE en forma de mapeo**, que coincide con el original. Ninguno aporta hechos nuevos |

**Escalas**
- **A** completamente fiable · **B** normalmente fiable · **C** bastante fiable · **D** normalmente no fiable · **E** no fiable · **F** no evaluable.
- **1** confirmada por otras fuentes · **2** probablemente cierta · **3** posiblemente cierta · **4** dudosa · **5** improbable · **6** no evaluable.

> **Observación sobre este anexo, y cierra el lote de noviembre de 2026.**
>
> Es el único de los siete informes con una fuente **A-1**, y conviene decir qué
> significa eso y qué no. Significa que los hechos técnicos de este expediente
> —los CVE, los comandos, los hashes, las técnicas— son los mejor establecidos
> de todo el lote. **No significa que el aviso sea neutral ni completo**: sus
> cuatro sesgos están enumerados arriba, y uno de ellos —poner cinco nombres de
> industria en una lista sin aclarar su alcance— es la causa remota del error de
> atribución que este informe desmonta.
>
> La lección, que vale para toda la cartera: **la mejor fuente posible sigue
> necesitando que se lea lo que afirma y no lo que parece afirmar.** Un aviso
> firmado por veintitrés agencias es autoridad máxima sobre los cinco CVE que
> enumera. Sobre si `GhostEmperor` y FamousSparrow son el mismo actor, **no dice
> nada**, y de suponer que sí salió un titular falso.

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

## Anexo D — Las cinco comprobaciones antes de afirmar que dos actores son el mismo

Este anexo es el entregable transversal del informe y la respuesta a la decisión `E-e`. Es la regla que, aplicada en septiembre de 2026, habría evitado un titular falso.

**La regla principal, en una línea: una atribución sin base publicada no es
utilizable, por autorizada que sea la fuente. Y la secundaria: un solapamiento
parcial no es transitivo.**

| # | Comprobación | Por qué | Resultado en este expediente |
|---|---|---|---|
| D-0 | **¿Quién afirma la equivalencia, y qué base técnica publica?** | **Es la comprobación que resuelve la mayoría de los casos y la que se omitió aquí.** Una afirmación sin indicadores, tácticas ni razonamiento no se puede verificar ni refutar, y por tanto **no puede sostener una regla de detección**, por autorizada que sea su fuente | **Microsoft afirma la identidad y no publica nada.** ESET afirma la separación y publica su razonamiento. Dos fuentes más declaran la cuestión abierta. **Conclusión: no está establecida** |
| D-1 | **¿Cuál es el grado de relación declarado en CADA eslabón de la cadena?** Equivalencia, solapamiento parcial, clúster distinto, o nombre de malware | **Una cadena de afirmaciones es tan fuerte como su eslabón más débil**, y una cadena que contiene un «se solapan parcialmente» no puede concluir «son el mismo» | Hay una cadena vía `GhostEmperor` cuyo primer eslabón es un **solapamiento parcial** (una IP compartida en 2021). **No soporta la conclusión** — y, dada `D-0`, **tampoco era necesaria** |
| D-2 | **¿En qué consiste exactamente el solapamiento parcial?** Un hash, una dirección, una técnica, una víctima | Un solapamiento de **una dirección IP** y **una vulnerabilidad** es el grado mínimo de relación que existe, y es compatible con dos actores que compraron el mismo alojamiento | **Una dirección IP y una vulnerabilidad, en 2021.** Nada más |
| D-3 | **¿Qué dice la fuente que hizo el análisis, frente a quien lo reinterpretó?** | Quien analizó el implante y tiene la telemetría es la autoridad sobre su propia atribución. Una cobertura que no analizó nada no puede corregirla | ESET analizó el implante, lo atribuye a FamousSparrow y **rastrea los dos actores por separado**. Las coberturas no analizaron nada |
| D-4 | **¿Coinciden la superficie de ataque y el modelo de operación?** | Es la comprobación material, y la más barata. Dos actores con superficies incompatibles difícilmente son el mismo | **No coinciden en nada**: uno es implante de punto final sobre servidores expuestos; el otro vive en routers de operador y redirige servidores de autenticación |
| D-5 | **¿La lista de alias de la fuente oficial declara equivalencia de expedientes, o enumera nombres usados?** | Un aviso oficial es autoridad sobre lo que afirma. **Enumerar cinco nombres no es declarar que los cinco expedientes sean idénticos**, y el aviso no se pronuncia sobre eso | **Enumera nombres usados.** No se pronuncia sobre el alcance de cada expediente, y de suponer que sí sale el error |

> **Cómo usarlo.** Las seis comprobaciones se hacen en media hora, y **dos de
> ellas solas habrían bastado en este caso**: la `D-0` —preguntar qué base
> publica quien afirma la equivalencia— y la `D-4` —comparar superficie y modelo
> de operación—.
>
> **Y una advertencia sobre el uso de este anexo, aprendida de la propia
> verificación de este informe.** La primera redacción aplicó `D-1` y concluyó
> que había encontrado el mecanismo del error. **No aplicó `D-0`**, que era la
> comprobación decisiva, y por eso construyó una cadena transitiva elegante
> cuando la explicación real era directa y mucho más simple. La lista de
> comprobación no sirve si se usa para confirmar la hipótesis que ya se tenía:
> hay que recorrerla entera y en orden, empezando por `D-0`.
>
> Esta cartera lleva tres expedientes con variantes del problema de
> nomenclatura: `CTI-2026-022` (nombres en disputa de un actor regional),
> `CTI-2026-017` v1.2 (un implante tomado por un actor) y éste (**una
> equivalencia afirmada sin base publicada y consumida como hecho**). Los tres
> son el mismo fallo de fondo: **tratar la nomenclatura como si fuera una
> propiedad del adversario y no una convención de quien lo observa** — y en este
> caso, además, tratar una afirmación como si fuera una evidencia.

## Anexo E — Marcos de referencia empleados

`MITRE ATT&CK v17` (versión que declara el aviso y que este informe conserva sin modificar) · **`MITRE D3FEND`** (mapeo de contramedidas publicado por el propio aviso) · `Modelo del Diamante` · `Cyber Kill Chain` · `Pirámide del Dolor` (con la adición de §T-3: la comparación de configuración como nivel propio) · `F3EAD` · `ICD 203` · `Análisis de Hipótesis Competidoras (ACH)` · `Comprobación de Supuestos Clave (KAC)` · `pre-mortem` · `TLP 2.0` · `PAP` · `Admiralty Code` · `Sigma` · `YARA` · `Snort` · `KQL` · `STIX 2.1`

## Anexo F — Paquete legible por máquina

- **Fuente preferente: el paquete STIX 2.1 que publica el propio aviso `AA25-239A`.** Está mantenido por los firmantes y puede actualizarse; el Anexo A de este informe es una copia con fecha y subordinada a él. **Es la decisión `E-f`**
- **Reglas oficiales que hay que desplegar en lugar de reescribirlas**: las dos reglas YARA (`SALT_TYPHOON_CMD1_SFTP_CLIENT`, `SALT_TYPHOON_NEW2_SFTP_CLIENT`) y la regla Snort (`sid:1000003`) publicadas por los firmantes
- Índice con contexto: [`ioc_index.csv`](ioc_index.csv) — **conserva la advertencia de vigencia y la acción permitida**, que las listas planas pierden; para este informe es especialmente importante, porque la acción correcta sobre las 84 direcciones es «bloqueo tras verificar vigencia» y no «bloqueo»
- Listas planas: [`ioc_hash.txt`](ioc_hash.txt), [`ioc_url.txt`](ioc_url.txt), [`ioc_ipv4.txt`](ioc_ipv4.txt) — **ver la advertencia del Anexo A.4 antes de usarlas**
- Reglas Sigma propias: tres en §X-4, más guiones de comprobación de dispositivo y cuatro consultas de flujo y de registro de comandos

## Anexo G — Control de cambios

| Versión | Fecha | Cambio | Autor |
|---|---|---|---|
| 1.0.2 | 2026-11-17 | **Segunda corrección previa a la publicación, y es de fondo: afectaba a los juicios, no a los datos.** La verificación de `KJ-3` y `KJ-4` contra las fuentes encontró **una explicación documentada y mucho más simple del origen de la fusión de alias que la que este informe sostenía**: Microsoft afirmó directamente —según coberturas— que `Salt Typhoon`, `FamousSparrow` y `GhostEmperor` son el mismo grupo, **sin publicar base técnica**. La primera redacción presentaba como hallazgo central una cadena transitiva vía `GhostEmperor` en el aviso oficial, **que no era necesaria para explicar el resultado**. Cambios: (a) **`KJ-3` reponderado** — la afirmación de Microsoft pasa a vía principal (muy probable) y la composición transitiva a vía de refuerzo (posibilidad real, confianza baja); (b) **`KJ-4` degradado** — de «casi con certeza que la atribución de prensa es incorrecta» a «probable que la equivalencia no esté establecida en ninguna de las dos direcciones», porque **si Microsoft afirma la identidad, usar su nombre no es un error de la prensa sino la adopción de una taxonomía en disputa**; (c) titular, subtitular, resumen ejecutivo, §E-1, §E-2, tarjetas y cifras rehechos en consecuencia; (d) **§O-1 bloque 3 reescrito como tabla de quién afirma qué y con qué base**, en lugar de cadena de inferencia; (e) nota de tradecraft de §O-1 con dos reglas, la principal nueva; (f) **§O-6 cuestión 1 reordenada**, con hipótesis `H5` nueva y `H3` degradada; (g) supuesto clave y pre-mortem rehechos; (h) **Anexo D con comprobación `D-0` nueva**, que es la que se omitió; (i) decisión `E-h` ajustada: la corrección a emitir no es «es falso» sino «no se sabe»; (j) limitaciones §3.3-xi y xii y brecha `G-11`. **La corrección se consigna y no se oculta el razonamiento anterior, porque el error es instructivo y el Anexo D lo recoge como advertencia de uso** | Célula CTI |
| 1.0.1 | 2026-11-17 | **Corrección previa a la publicación, tras verificación programática del Anexo A.4 contra la lista del aviso.** Se retiran dos direcciones que no están en el aviso y que entraron por contaminación entre expedientes durante la redacción: `37.221.64.202` (procede de `CTI-2026-026`) y `45.80.208.66` (procede de la lista del clúster `OceanGate` del expediente de `CTI-2026-017`). Se rectifica además la nota de recuento, que afirmaba incorrectamente haber omitido dos direcciones de proveedores de nube: no se omitió ninguna, y la tabla recoge las 86 entradas del aviso. **Sin cambios en los juicios analíticos.** El recuento queda verificado: 84 IPv4 y 2 IPv6, coincidencia exacta con la fuente | Célula CTI |
| 1.0 | 2026-11-17 | Emisión inicial. **Resuelve el `KJ-7` de `CTI-2026-017`** identificando el eslabón —`GhostEmperor` en la lista de nombres de industria del aviso oficial— por el que se produjo la fusión con FamousSparrow, y desmonta la atribución errónea de septiembre de 2026. Primer informe de la cartera con una fuente de fiabilidad **A** y credibilidad **1**. Establece en el Anexo D la regla de no transitividad de los solapamientos parciales | Célula CTI |

## Anexo H — Realimentación del consumidor

| Pregunta | Respuesta |
|---|---|
| ¿Respondió a su requisito? | |
| **¿Están cerrados los cinco CVE del Anexo A.1 en el equipamiento propio? (decisión `E-a`, detección `D-0`)** | |
| **¿Qué respondieron los proveedores de conectividad sobre su propio estado de parcheo? (`X-2`)** | |
| ¿Se encontraron comunidades SNMP `public` o `private`? ¿En cuántos dispositivos? (`X-6`, `H-8`) | |
| ¿En qué formato estaba el secreto compartido de TACACS+? ¿Era reversible? (`X-7`) | |
| ¿Existe repositorio de configuración aprobada y comparación periódica? (decisión `E-d`) | |
| ¿Había entrado la noticia errónea de septiembre de 2026 en el registro de riesgos? (`X-15`, decisión `E-h`) | |
| ¿Se emitió la instrucción del Anexo D sobre no transitividad de los alias? (decisión `E-e`) | |
| ¿Qué faltó? | |
| ¿Llegó a tiempo? | |

> Sin este anexo devuelto, el ciclo de inteligencia queda abierto. En este
> informe interesan especialmente la segunda y la tercera pregunta —son la
> exposición real y se responden en días— y la séptima, porque si la respuesta
> es «sí», significa que durante dos meses hemos tenido inteligencia falsa en
> nuestros propios registros.
