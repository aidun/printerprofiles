# Bambu Lab X2D

[← Druckerübersicht](README.md) · Kürzel `X2D` · Durchsatzfaktor **1.00**

Zwei Düsen auf dem Bauraum des X1C, mit aktiv beheizter Kammer. Die Hauptdüse wird
direkt gefördert, die Hilfsdüse über Bowden. Alle Werte sind 🔵 Startwerte, an diesem
Gerät ist noch keiner gedruckt.

---

## Eckdaten

| | |
|---|---|
| Bauraum | 256 × 256 × 260 mm (Hilfsdüse und beide Düsen: 235,5 × 256 × 256 mm) |
| Kammer | aktiv beheizt, bis 65 °C |
| Hotend-Limit | 300 °C |
| Extruder | 2: Direct Drive (Hauptdüse) und Bowden (Hilfsdüse) |
| Extrudervarianten | je Standard · High Flow · E3D High Flow |
| Düsen | 0.2 · 0.4 · 0.6 mm |

## Volumenstrom

Gleich dem X1C: Die Obergrenzen der Bibliothek stimmen bei allen neun Bambu-Materialien
überein. Werte in mm³/s:

| Material | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| SUNLU PLA | 1.6 | 15 | 21 |
| SUNLU PLA Glow | — | 10.5 | 15 |
| SUNLU PETG | 1 | 14 | 16 |
| SUNLU PETG Glow | — | 11 | 14.5 |
| SUNLU TPU | — | 3.2 | 3.2 |
| SUNLU ABS | 2 | 15 | 15 |
| eSUN ABS+ | 2 | 15 | 15 |
| eSUN PETG-CF | — | 11.5 | 11.5 |
| Bambu PETG-CF | — | 11.5 | 11.5 |
| Bambu ABS | 2 | 16 | 16 |
| Bambu ASA | 2 | 18 | 18 |
| Bambu ASA-CF | — | 18 | 18 |

`—` heißt: nicht ausgeliefert. Glow-Material ist für die 0.2-mm-Düse gesperrt, flexibles TPU ebenfalls — bei beiden begrenzt nicht die Düse den Durchsatz. Für die faserverstärkten Materialien PETG-CF und ASA-CF liefert Bambu überhaupt kein 0.2-mm-Profil; die Faserlänge liegt in der Größenordnung der Bohrung.

## Schichthöhen

| Stufe | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| Qualität | 0.08 | 0.12 | 0.18 |
| Normal | 0.12 | 0.20 | 0.30 |
| Schnell | 0.12 ⁽¹⁾ | 0.24 ⁽¹⁾ | 0.30 ⁽¹⁾ |

⁽¹⁾ Die Zielschichthöhe der Stufe ist hier nicht verfügbar; der Generator wählt das
nächstgelegene freigegebene Profil. Die Stufe *Schnell* fällt dadurch wie beim H2C
konservativer aus als etwa beim X1C.

## Besonderheiten

**Abgestimmt ist die Hauptdüse.** Volumenstrom und Flussrate stehen im Eintrag für
Direct Drive Standard. Alle anderen Varianten, auch die Bowden-Hilfsdüse, erben Bambus
Werte. Die Hilfsdüse ist vor allem für Stützmaterial gedacht.

**Sechs Geschwindigkeitswerte je Parameter.** Die Arrays haben sechs Einträge, mit der
0.2-mm-Düse vier. Die Tempofaktoren der Stufen werden auf jeden Eintrag angewandt.

---

[← H3C](h3c.md) · [Druckerübersicht](README.md) · [X1 Carbon →](x1c.md)
