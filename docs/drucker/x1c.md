# Bambu Lab X1 Carbon

[← Druckerübersicht](README.md) · Kürzel `X1C` · Durchsatzfaktor **1.00**

Der Referenzdrucker dieses Repositories. Alle Volumenströme in `src/filaments/` sind
X1C-Werte; die übrigen Geräte werden daraus skaliert. Ab Werk mit gehärteter Düse und
Lidar-Flusskalibrierung ausgestattet.

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

Basiswert, Faktor 1.00. Werte in mm³/s:

| Material | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| SUNLU PLA | 1.6 | 15 | 21 |
| SUNLU PLA Glow | — | 10.5 | 15 |
| SUNLU PETG | 1 | 14 | 16 |
| SUNLU PETG Glow | — | 11 | 14.5 |
| SUNLU TPU | — | 3.2 | 3.2 |
| eSUN ABS+ | 2 | 15 | 15 |
| Bambu PETG-CF | — | 11.5 | 11.5 |
| Bambu ASA | 2 | 18 | 18 |
| Bambu ASA-CF | — | 18 | 18 |

`—` heißt: nicht ausgeliefert. Glow-Material ist für die 0.2-mm-Düse gesperrt, flexibles TPU ebenfalls — bei beiden begrenzt nicht die Düse den Durchsatz. Für die faserverstärkten Materialien PETG-CF und ASA-CF liefert Bambu überhaupt kein 0.2-mm-Profil; die Faserlänge liegt in der Größenordnung der Bohrung.

## Schichthöhen

| Stufe | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| Qualität | 0.08 | 0.12 | 0.18 |
| Normal | 0.12 | 0.20 | 0.30 |
| Schnell | 0.14 | 0.28 | 0.42 |

Alle Zielschichthöhen sind verfügbar — der X1C bietet das vollständigste
Profilangebot und braucht keine Anpassung nach unten.

## Besonderheiten

**Lidar-Flusskalibrierung.** Der X1C misst die Flussrate selbst und korrigiert
während des Drucks. Das ersetzt [Schritt 2 der Kalibrierung](../calibration.md#schritt-2--flussrate)
weitgehend, **nicht** aber [Schritt 3](../calibration.md#schritt-3--volumenstrom):
Der maximale Volumenstrom ist eine Obergrenze im Slicer, die das Lidar nicht kennt.

**Gehärtete Düse ab Werk.** Beide Glow-Materialien können ohne Umbau gedruckt werden,
solange die Originaldüse verbaut ist. Nach einem Wechsel auf eine Messingdüse gilt
das nicht mehr.

**Geschlossene Kammer, passiv.** Ausreichend für PETG, sofern die Tür geschlossen und
der Drucker nicht in der Zugluft steht.

---

[← H2C](h2c.md) · [Druckerübersicht](README.md) · [P1S →](p1s.md)
