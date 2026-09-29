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
| Flussrate | 0.97 | −0.01 |
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
| H2C | 1.7 | 16.1 | 22.4 |
| X1 Carbon | 1.5 | 14.0 | 19.5 |
| P1S | 1.4 | 13.3 | 18.5 |
| A1 | 1.4 | 12.6 | 17.6 |
| A1 mini | 1.3 | 11.9 | 16.6 |

Rund 7 % unter SUNLU PLA — die zähere Schmelze fließt langsamer nach.

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

[← SUNLU PETG Transparent](sunlu-petg-transparent.md) · [Materialübersicht](README.md) · [eSUN PLA+ Glow →](esun-pla-plus-glow.md)
