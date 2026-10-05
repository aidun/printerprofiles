# Bambu Lab P1P

[← Druckerübersicht](README.md) · Kürzel `P1P` · Durchsatzfaktor **0.95**

Derselbe Drucker wie der P1S, nur ohne Gehäuse. Extruder, Hotend und Steuerung sind
identisch — es fehlen die Seitenwände, der Deckel und die Kammerentlüftung.

---

## Eckdaten

| | |
|---|---|
| Bauraum | 256 × 256 × 256 mm |
| Kammer | offen |
| Hotend-Limit | 300 °C |
| Extruder | 1 |
| Extrudervarianten | Direct Drive Standard · Direct Drive High Flow |
| Düsen | 0.2 · 0.4 · 0.6 mm |

## Volumenstrom

5 % unter dem X1C, genau wie der P1S. Werte in mm³/s:

| Material | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| SUNLU PLA | 1.5 | 14.2 | 19.9 |
| SUNLU PLA Glow | — | 10 | 14.2 |
| SUNLU PETG | 0.9 | 13.3 | 15.2 |
| SUNLU PETG Glow | — | 10.4 | 13.8 |
| SUNLU TPU | — | 3 | 3 |
| SUNLU ABS | 1.9 | 14.2 | 14.2 |
| eSUN ABS+ | 1.9 | 14.2 | 14.2 |
| eSUN PETG-CF | — | 10.9 | 10.9 |
| Bambu PETG-CF | — | 10.9 | 10.9 |
| Bambu ABS | 1.9 | 15.2 | 15.2 |
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

**Derselbe Faktor wie der P1S — eine bewusste Entscheidung.** Bambus eigene
Herstellerprofile stufen den P1P wie den X1 Carbon ein: `eSUN PLA+ @BBL P1P` trägt
dieselben 16 mm³/s wie `eSUN PLA+ @BBL X1C`. Dieses Repository folgt dem nicht,
sondern bleibt bei 0.95. Begründung: P1P und P1S haben dasselbe Hotend und denselben
Extruder, und der Faktor bildet die Aufschmelzleistung ab, nicht das Gehäuse. Zwei
identische Maschinen mit unterschiedlichem Durchsatz wären ein Widerspruch in den
eigenen Daten. Wer den P1P am Gerät nachmisst und höher liegt, trägt den
zurückgerechneten Wert ein — dafür ist der Weg in
[Kalibrierung](../calibration.md#gemessenen-wert-zurückrechnen) beschrieben.

**Offene Kammer — ABS wird hier schwierig.** `eSUN ABS+` ist für den P1P
freigegeben, weil Bambu das Basisprofil ausliefert. Ohne Gehäuse schrumpft ABS beim
Abkühlen aber ungleichmäßig: große Flächen lösen sich an den Ecken von der Platte,
hohe Teile reißen zwischen den Schichten auf. Ein Windschutz oder ein nachgerüstetes
Gehäuse ist Pflicht, nicht Komfort. Für den Dauerbetrieb mit ABS ist der P1S das
richtige Gerät.

**Kein Lidar — Flussrate manuell kalibrieren.** Wie beim P1S entscheidet dieser
Schritt über die Maßhaltigkeit. Ablauf in
[Kalibrierung, Schritt 2](../calibration.md#schritt-2--flussrate).

**Düse prüfen, bevor Glow gedruckt wird.** Der P1P wird mit Messingdüse
ausgeliefert. Beide Glow-Materialien setzen eine gehärtete Düse voraus — siehe
[Düsen](../nozzles.md).

---

[← P1S](p1s.md) · [Druckerübersicht](README.md) · [A1 →](a1.md)
