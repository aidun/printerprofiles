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
| SUNLU PLA | 1.5 | 14.2 | 19.9 |
| SUNLU PLA Glow | — | 10 | 14.2 |
| SUNLU PETG | 0.9 | 13.3 | 15.2 |
| SUNLU PETG Glow | — | 10.4 | 13.8 |
| SUNLU TPU | — | 3 | 3 |
| eSUN ABS+ | 1.9 | 14.2 | 14.2 |
| Bambu PETG-CF | — | 10.9 | 10.9 |
| Bambu ASA | 1.9 | 17.1 | 17.1 |
| Bambu ASA-CF | — | 17.1 | 17.1 |

`—` heißt: nicht ausgeliefert. Glow-Material ist für die 0.2-mm-Düse gesperrt, flexibles TPU ebenfalls — bei beiden begrenzt nicht die Düse den Durchsatz. Für die faserverstärkten Materialien PETG-CF und ASA-CF liefert Bambu überhaupt kein 0.2-mm-Profil; die Faserlänge liegt in der Größenordnung der Bohrung.

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

[← X1 Carbon](x1c.md) · [Druckerübersicht](README.md) · [P1P →](p1p.md)
