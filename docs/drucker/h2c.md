# Bambu Lab H2C

[← Druckerübersicht](README.md) · Kürzel `H2C` · Durchsatzfaktor **1.15**

Das leistungsfähigste Gerät im Repository und das einzige mit zwei gleichzeitig
aktiven Düsen. Die aktiv beheizte Kammer macht ihn zum unkritischsten Drucker für
PETG; das High-Flow-Hotend erlaubt die höchsten Volumenströme.

---

## Eckdaten

| | |
|---|---|
| Bauraum | 350 × 320 × 325 mm |
| Kammer | aktiv beheizt |
| Hotend-Limit | 350 °C |
| Extruder | 2, gleichzeitig aktiv (Vortek-Werkzeugwechsler) |
| Extrudervarianten | Direct Drive Standard · Direct Drive High Flow |
| Düsen | 0.2 · 0.4 · 0.6 mm |

## Volumenstrom

15 % über dem X1C. Werte in mm³/s:

| Material | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| SUNLU PLA | 1.8 | 17.2 | 24.1 |
| SUNLU PLA Glow | — | 12.1 | 17.2 |
| SUNLU PETG | 1.1 | 16.1 | 18.4 |
| SUNLU PETG Glow | — | **12.6** 🟢 | 16.7 |
| SUNLU TPU | — | 3.7 | 3.7 |
| eSUN ABS+ | 2.3 | 17.2 | 17.2 |
| Bambu PETG-CF | — | 13.2 | 13.2 |
| Bambu ASA | 2.3 | 20.7 | 20.7 |
| Bambu ASA-CF | — | 20.7 | 20.7 |

`—` heißt: nicht ausgeliefert. Glow-Material ist für die 0.2-mm-Düse gesperrt, flexibles TPU ebenfalls — bei beiden begrenzt nicht die Düse den Durchsatz. Für die faserverstärkten Materialien PETG-CF und ASA-CF liefert Bambu überhaupt kein 0.2-mm-Profil; die Faserlänge liegt in der Größenordnung der Bohrung.

🟢 am Gerät gemessen — der Referenzwert des gesamten Repositories.

## Schichthöhen

| Stufe | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| Qualität | 0.08 | 0.12 | 0.18 |
| Normal | 0.12 | 0.20 | 0.30 |
| Schnell | 0.12 ⁽¹⁾ | 0.24 ⁽¹⁾ | 0.30 ⁽¹⁾ |

⁽¹⁾ Der H2C bietet weniger Basisprofile an als die übrigen Drucker. Wo die
Zielschichthöhe der Stufe nicht verfügbar ist, wählt der Generator automatisch das
nächstgelegene freigegebene Profil. Die Stufe *Schnell* fällt dadurch beim H2C
konservativer aus als etwa beim X1C — das ist korrekt und beabsichtigt, denn ein
nicht angebotenes Profil wäre eine ungültige Einstellung.

## Besonderheiten

**Zwei Düsen, eine Größe.** Die Profile setzen für beide Werkzeuge denselben
Düsendurchmesser voraus. Gemischte Durchmesser werden nicht abgebildet.

**Vier Geschwindigkeitswerte je Parameter.** Bambu hinterlegt Geschwindigkeiten als
Array mit einem Eintrag je Extrudervariante — beim H2C sind das vier
(2 Extruder × Standard/High Flow). Die Profile dieses Repositories arbeiten deshalb
mit Tempofaktoren statt absoluten Werten, damit Bambus Abstimmung zwischen Standard-
und High-Flow-Extruder erhalten bleibt. Hintergrund in `src/quality.toml`.

**Filamentwerte werden dedupliziert.** Materialwerte kennen nur zwei Varianten
(Standard, High Flow), nicht vier. Die erzeugten Presets bilden das so ab.

**Beheizte Kammer.** PETG und PETG Glow drucken hier am problemlosesten. Warping ist
praktisch kein Thema, solange die Tür geschlossen bleibt.

---

[Druckerübersicht](README.md) · [X1 Carbon →](x1c.md)
