# Bambu Lab H3C

[← Druckerübersicht](README.md) · Kürzel `H3C` · Durchsatzfaktor **1.15**

Ein Extruder, aber bis zu neun wechselbare Hotends. Der größte Bauraum im Repository.
Alle Werte sind 🔵 Startwerte, an diesem Gerät ist noch keiner gedruckt.

---

## Eckdaten

| | |
|---|---|
| Bauraum | 330 × 320 × 325 mm |
| Kammer | aktiv beheizt |
| Hotend-Limit | 350 °C ⁽²⁾ |
| Extruder | 1, bis zu 9 wechselbare Hotends |
| Extrudervarianten | Direct Drive Standard · High Flow · TPU285 |
| Düsen | 0.2 · 0.4 · 0.6 mm |

⁽²⁾ Nicht aus einem Datenblatt bestätigt, sondern vom H2C übernommen: Bambu gibt für
beide dieselben Hochtemperatur-Filamente frei. Der Wert wirkt nur im Validator.

## Volumenstrom

15 % über dem X1C, wie beim H2C: Die Obergrenzen der Bibliothek stimmen bei beiden
Geräten bis auf PETG-CF überein. Werte in mm³/s:

| Material | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| SUNLU PLA | 1.8 | 17.2 | 24.1 |
| SUNLU PLA Glow | — | 12.1 | 17.2 |
| SUNLU PETG | 1.1 | 16.1 | 18.4 |
| SUNLU PETG Glow | — | 12.6 | 16.7 |
| SUNLU TPU | — | 3.7 | 3.7 |
| SUNLU ABS | 2.3 | 17.2 | 17.2 |
| eSUN ABS+ | 2.3 | 17.2 | 17.2 |
| eSUN PETG-CF | — | 13.2 | 13.2 |
| Bambu PETG-CF | — | **6** | **6** |
| Bambu ABS | 2.3 | 18.4 | 18.4 |
| Bambu ASA | 2.3 | 20.7 | 20.7 |
| Bambu ASA-CF | — | 20.7 | 20.7 |

`—` heißt: nicht ausgeliefert. Glow-Material ist für die 0.2-mm-Düse gesperrt, flexibles TPU ebenfalls — bei beiden begrenzt nicht die Düse den Durchsatz. Für die faserverstärkten Materialien PETG-CF und ASA-CF liefert Bambu überhaupt kein 0.2-mm-Profil; die Faserlänge liegt in der Größenordnung der Bohrung.

**Fett** ist ein Deckel aus der Bibliothek: `Bambu PETG-CF @BBL H3C` nennt 6 mm³/s.

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

**Variante TPU285.** Die Maschine führt eine eigene Variante für 2,85-mm-TPU. Die
Filamentprofile hier lassen sie aus, weil alle Materialien 1,75 mm sind. Die
Prozessprofile behalten sie, denn Bambus Geschwindigkeits-Arrays enthalten sie.

---

[← H2C](h2c.md) · [Druckerübersicht](README.md) · [X2D →](x2d.md)
