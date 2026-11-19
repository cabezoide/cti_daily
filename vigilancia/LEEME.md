# vigilancia/

Salida de `tools/cti_vigilancia.py`, el recolector diario. Tres clases de
fichero y conviene no confundirlas:

| Fichero | Qué es | ¿Se versiona? |
|---|---|---|
| `estado.json` | **La línea base.** Contra ella se calculan los deltas del día siguiente | **Sí.** Sin ella el diff no funciona en un clon nuevo |
| `parte-<fecha>.md` | El parte legible de esa jornada | **Sí.** Es el historial de lo que se vio cada día |
| `parte-<fecha>.json` | Los mismos datos para automatizar, que consume la skill el mismo día | **No** (`.gitignore`). ~55 KB diarios sin valor histórico |

## Sobre `estado.json`

**No contiene ningún nombre de víctima.** Guarda hashes de dieciséis caracteres
—`sha256(grupo + víctima + fecha)[:16]`— porque las víctimas de un sitio de
filtración son reclamaciones sin confirmar y algunas descripciones contienen
datos personales de terceros. El diff sólo necesita saber si una clave es nueva;
el país y el sector se leen del dato vivo y no se persisten.

Pesa unos 280 KB y **se sobrescribe, no crece**.

## Si una ejecución sale mal

- **`COLECCIÓN PARCIAL`** en el parte: una fuente no respondió. La línea base de
  las secciones afectadas se conserva sin tocar, así que el delta de mañana
  sigue siendo correcto. **No interpretar la ausencia de deltas como ausencia de
  cambios.**
- **`LÍNEA BASE NO ACTUALIZADA`**: el estado nuevo era más pequeño que el
  anterior sin motivo y no se escribió. Si el encogimiento es legítimo —se
  retiraron informes, cambió el año consultado—, reinicializar:
  `python3 tools/cti_vigilancia.py --inicializar`.
- **HTTP 429**: las fuentes son servicios gratuitos de terceros y limitan por
  tasa. El script reintenta con espera creciente y respeta `Retry-After`. Una
  ejecución al día no lo provoca; varias seguidas sí.
