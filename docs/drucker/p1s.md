# Bambu Lab P1S

[← Druckerübersicht](README.md) · Kürzel `P1S` · Durchsatzfaktor **0.95**

Mechanisch weitgehend der X1 Carbon, aber ohne Lidar. Die fehlende automatische
Flusskalibrierung ist der einzige, dafür spürbare Unterschied im Alltag.

---

## Eckdaten

| | |
|---|---|
| Bauraum | 256 × 256 × 256 mm |
| Kammer | geschlossen, passiv |
| Hotend-Limit | 300 °C |
| Extruder | 1 |
| Extrudervarianten | Direct Drive Standard · Direct Drive High Flow |
| Düsen | 0.2 · 0.4 · 0.6 mm |

## Volumenstrom

5 % unter dem X1C. Werte in mm³/s:

| Material | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| SUNLU PLA | 3.3 | 14.2 | 19.9 |
| SUNLU PLA Glow | — | 10.0 | 14.2 |
| SUNLU PETG | 2.8 | 12.8 | 17.1 |
| SUNLU PETG Glow | — | 10.4 | 13.8 |

## Schichthöhen

| Stufe | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| Qualität | 0.08 | 0.12 | 0.18 |
| Normal | 0.12 | 0.20 | 0.30 |
| Schnell | 0.14 | 0.28 | 0.42 |

## Besonderheiten

**Kein Lidar — Flussrate manuell kalibrieren.** Das ist am P1S kein optionaler
Feinschliff, sondern der Schritt, der über Maßhaltigkeit entscheidet. Der Ablauf
steht in [Kalibrierung, Schritt 2](../calibration.md#schritt-2--flussrate) und
dauert rund zehn Minuten je Material.

**Düse prüfen, bevor Glow gedruckt wird.** Anders als der X1C kommt der P1S je nach
Auslieferung mit einer Messingdüse. Beide Glow-Materialien setzen eine gehärtete
Düse voraus.

**Geschlossene Kammer, passiv.** Wie beim X1C ausreichend für PETG.

---

[← X1 Carbon](x1c.md) · [Druckerübersicht](README.md) · [A1 →](a1.md)
