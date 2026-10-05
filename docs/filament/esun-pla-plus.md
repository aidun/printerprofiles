# eSUN PLA+

[← Materialübersicht](README.md) · Status: 🔵 Startwert · Basis: `Generic PLA`

PLA mit Zähmodifikator. eSUN mischt dem Grundpolymer einen Schlagzähigkeitsverbesserer
bei — das Ergebnis bricht nicht mehr glasartig, sondern verformt sich vorher sichtbar.
Für funktionale Teile, die gelegentlich Stoß oder Biegung sehen, ist PLA+ dem
Standard-PLA deutlich überlegen, ohne dessen Gutmütigkeit im Druck aufzugeben.

---

## Kennwerte

| Größe | Wert | Abweichung zu SUNLU PLA |
|---|---|---|
| Düse | **220 °C** (erste Schicht 225 °C) | +5 °C |
| Temperaturfenster | 200 – 235 °C | leicht höher |
| Bett | **60 °C** (erste Schicht 65 °C) | +5 °C |
| Glasübergang | 55 °C | gleich |
| Flussrate | 0.98 | gleich |
| Lüfter | **50 – 90 %** | leicht reduziert |
| Überhangkühlung | 100 % | gleich |
| Z-Hop | 0.4 mm | gleich |
| Abrasiv | nein — Messingdüse genügt | |
| Trocknung | 45 °C / 6 h | gleich |
| Lagerung | trocken mit Silikagel | unkritisch |

Die etwas höhere Düsen- und Betttemperatur und die leicht zurückgenommene Kühlung
folgen derselben Ursache: Der Zähmodifikator erhöht die Schmelzviskosität. PLA+
braucht spürbar mehr Wärme als Standard-PLA, um gleich gut zu verschweißen.

## Volumenstrom je Drucker und Düse

Werte in mm³/s. Basis ist der X1C; die übrigen Drucker werden über den
[Durchsatzfaktor](../drucker/README.md#durchsatzfaktoren) skaliert.

| Drucker | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| H2C | 2.1 | 18.4 | 18.4 |
| X1 Carbon | 1.8 | 16 | 16 |
| P1S | 1.7 | 15.2 | 15.2 |
| P1P | 1.7 | 15.2 | 15.2 |
| A1 | 1.6 | 14.4 | 14.4 |
| A1 mini | 1.5 | 13.6 | 13.6 |

> **Quelle der Werte.** Volumenstrom und Flussrate stammen aus den eSUN-eigenen
> Profilen der Bambu-Bibliothek: `eSUN PLA+ @BBL X1C 0.2 nozzle` gibt 1.8 mm³/s frei,
> `eSUN PLA+ @BBL X1C` — das Profil der 0.4-mm-Düse — 16.0 mm³/s, beide bei
> Flussrate 0.98. eSUN stuft sein PLA+ damit **höher** ein als Bambu das
> `Generic PLA` — die früher hier geführte Annahme eines reduzierten Volumenstroms
> war hergeleitet und ist damit überholt.

Auffällig ist die flache Kurve: 0.4 und 0.6 mm teilen denselben Wert. Für Düsen über
0.4 mm liefert eSUN überhaupt kein Profil, und dieses Repository erfindet keine Rampe
dazu — die Grenze liegt im Hotend, nicht in der Bohrung. Gegenüber SUNLU PLA bedeutet
das: bei 0.4 mm rund 7 % mehr Durchsatz, bei 0.6 mm dagegen knapp ein Viertel weniger.

## Wann PLA+ statt PLA

| Anforderung | Wahl |
|---|---|
| Sichtteile, Modelle, Figuren | SUNLU PLA — feinere Oberfläche, schneller |
| Halterungen, Clips, Gehäuse | **PLA+** — bricht nicht spröde |
| Schrauben- und Rastverbindungen | **PLA+** |
| Wärme über 50 °C | keines von beiden — [PETG](esun-petg.md) |

**Die Grenze bleibt die Temperatur.** PLA+ ist zäher, aber nicht wärmefester: Der
Glasübergang liegt weiterhin bei rund 55 °C. Wer Festigkeit *und* Wärmebeständigkeit
braucht, kommt an PETG nicht vorbei.

## Wenn etwas nicht stimmt

| Symptom | Zuerst prüfen |
|---|---|
| Teil bricht entlang der Schichten | Temperatur um 5 °C anheben, Lüfter senken |
| Unterextrusion, gerippte Oberfläche | [Volumenstrom](../calibration.md#schritt-3--volumenstrom) |
| Maße stimmen nicht | [Flussrate](../calibration.md#schritt-2--flussrate) |
| Fäden | [Fädenbildung](../troubleshooting.md#fädenbildung) |
| Erste Schicht haftet nicht | Bett auf 65 °C halten, Platte entfetten |

---

[← SUNLU TPU](sunlu-tpu.md) · [Materialübersicht](README.md) · [eSUN PLA+ Glow →](esun-pla-plus-glow.md)
