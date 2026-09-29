# Bambu Lab A1 mini

[← Druckerübersicht](README.md) · Kürzel `A1M` · Durchsatzfaktor **0.85**

Der kleinste Drucker im Repository und der mit dem schwächsten Hotend. Entsprechend
liegen alle Volumenströme am unteren Ende — das ist keine Vorsicht, sondern das
Limit der Aufschmelzleistung.

---

## Eckdaten

| | |
|---|---|
| Bauraum | 180 × 180 × 180 mm |
| Kammer | offen |
| Hotend-Limit | 300 °C |
| Extruder | 1 |
| Extrudervarianten | Direct Drive Standard |
| Düsen | 0.2 · 0.4 · 0.6 mm |

## Volumenstrom

15 % unter dem X1C und damit der niedrigste Wert im Repository. Werte in mm³/s:

| Material | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| SUNLU PLA | 3.0 | 12.8 | 17.8 |
| SUNLU PLA Glow | — | 8.9 | 12.8 |
| SUNLU PETG | 2.5 | 11.5 | 15.3 |
| SUNLU PETG Glow | — | 9.3 | 12.3 |

## Schichthöhen

| Stufe | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| Qualität | 0.08 | 0.12 | 0.18 |
| Normal | 0.12 | 0.20 | 0.30 |
| Schnell | 0.14 | 0.28 | 0.42 |

## Besonderheiten

**0.6 mm ist selten sinnvoll.** Bei 180 mm Bauraum ist der Zeitgewinn großer Düsen
gering, der Detailverlust dagegen deutlich. Die Profile existieren für Sonderfälle;
im Alltag ist 0.4 mm hier fast immer die richtige Wahl.

**Volumenstrom ernst nehmen.** Die Stufe *Schnell* kann das Hotend an sein Limit
bringen, besonders bei Glow-Material. Zeigt sich Unterextrusion, ist der
Volumenstrom der erste Wert, der nach unten gehört —
[Kalibrierung, Schritt 3](../calibration.md#schritt-3--volumenstrom).

**Offener Aufbau, Bettschubser.** Dieselben Hinweise wie beim [A1](a1.md): Zugluft
meiden, hohe Teile langsamer drucken.

---

[← A1](a1.md) · [Druckerübersicht](README.md)
