# eSUN ABS+

[← Materialübersicht](README.md) · Status: 🔵 Startwert · Basis: `Generic ABS`

Schlagfestes, temperaturbeständiges ABS. Der Glasübergang liegt bei 100 °C — damit
ist dies das einzige Material im Sortiment, das ein Teil im Sommerauto oder neben
einem warmen Gerät übersteht. Der Preis dafür ist der anspruchsvollste Druckablauf:
ABS schrumpft beim Abkühlen, und jeder Luftzug macht daraus Warping oder einen Riss
zwischen den Schichten.

---

## Kennwerte

| Größe | Wert | Abweichung zu eSUN PETG |
|---|---|---|
| Düse | **255 °C** (erste Schicht 260 °C) | +12 °C |
| Temperaturfenster | 240 – 275 °C | durchgehend höher |
| Bett | **90 °C** (erste Schicht 95 °C) | +15 °C |
| Glasübergang | 100 °C | +29 °C |
| Flussrate | 0.95 | gleich |
| Lüfter | **10 – 30 %** | deutlich niedriger |
| Überhangkühlung | 60 % | gleich |
| Z-Hop | 0.4 mm | −0.2 mm |
| Abrasiv | nein — Messingdüse genügt | |
| Trocknung | **70 °C / 4 h** | heißer, dafür kürzer |
| Lagerung | trocken mit Silikagel | unkritischer als PETG |

**Zur zurückgenommenen Kühlung.** `Generic ABS` gibt 10 – 80 % frei und fährt
Überhänge mit 80 %. Dieses Preset senkt die Obergrenze auf 30 % und die
Überhangkühlung auf 60 % — eine bewusste Abweichung, denn bei ABS kostet jeder
Prozentpunkt Lüfterleistung Schichthaftung. Die Entscheidung lautet hier Festigkeit
vor Überhangqualität. Überhänge über etwa 45° gehören auf Stützmaterial.

**Zur Düsentemperatur.** 255 °C liegen 15 °C **unter** dem Basisprofil, das 270 °C
vorgibt. Der niedrigere Wert ist auf die Praxis gerechnet: Er reicht für 15 mm³/s
aus, belastet die Düse weniger und hält den Geruch in Grenzen. Für dicke Wände oder
große Flächen darf man bis 275 °C hochgehen.

## Volumenstrom je Drucker und Düse

Werte in mm³/s. Basis ist der X1C; die übrigen Drucker werden über den
[Durchsatzfaktor](../drucker/README.md#durchsatzfaktoren) skaliert.

| Drucker | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| H2C | 2.3 | 17.2 | 17.2 |
| X1 Carbon | 2 | 15 | 15 |
| P1S | 1.9 | 14.2 | 14.2 |
| P1P | 1.9 | 14.2 | 14.2 |
| A1 | 1.8 | 13.5 | 13.5 |
| A1 mini | — | — | — |

> **Warum die A1 mini leer bleibt.** Für ABS liefert Bambu auf diesem Gerät kein
> Basisprofil — Bauraum und Bettleistung tragen das Material nicht. Dieses
> Repository erfindet keines: `src/filaments/esun-abs.toml` führt einen
> `printers`-Schlüssel, und `tools/validate.py` prüft, dass die dort genannten
> Geräte genau die sind, für die die Bibliothek ein Profil hat.

> **Quelle der Werte.** Volumenstrom (15.0 mm³/s) und Flussrate (0.95) stammen
> unverändert aus `Generic ABS` — ein eigenes X1C-Profil führt Bambu für ABS nicht,
> der X1C erbt direkt vom Grundprofil. Ein herstellereigenes eSUN-ABS-Profil gibt es
> nicht; Temperaturen und Lüfterwerte oben sind deshalb Startwerte dieses
> Repositories und weichen bewusst vom Basisprofil ab.

Die Kurve läuft ab 0.4 mm flach: 15.0 mm³/s bei beiden größeren Düsen. Der Engpass
ist die Aufschmelzleistung des Hotends, nicht die Bohrung.

## Die geschlossene Kammer ist keine Empfehlung

| Drucker | ABS-Eignung |
|---|---|
| **H2C** | beheizte Kammer — die beste Wahl, auch für große Teile |
| **X1 Carbon** | geschlossen, passiv — unkritisch |
| **P1S** | geschlossen, passiv — unkritisch |
| **P1P** | offen — nur mit Umbau oder Windschutz, siehe [P1P](../drucker/p1p.md) |
| **A1** | offen — nur kleine Teile, Windschutz zwingend |
| **A1 mini** | kein Profil |

**Warum das so streng ist.** ABS schrumpft beim Abkühlen um gut ein halbes Prozent.
Kühlt eine Schicht schneller ab als die darunter, zieht sie sich zusammen und reißt
entweder von der Platte ab oder von der Nachbarschicht weg. Eine warme, ruhige
Kammer hält diesen Unterschied klein. Ein offener Drucker im Durchzug tut das
Gegenteil — und die Risse zeigen sich oft erst nach Stunden, in halber Bauhöhe.

**Lüftung des Raumes, nicht des Druckers.** ABS setzt beim Drucken Styrol frei. Das
riecht deutlich und gehört nicht in einen Raum, in dem dauerhaft jemand sitzt.
Durchzug *im* Drucker ist schädlich, Belüftung des Raumes dagegen richtig —
idealerweise mit Aktivkohlefilter oder Abluft.

## Was ABS kann, was PETG nicht kann

| Anforderung | Wahl |
|---|---|
| Dauerhaft über 70 °C | **ABS+** — PETG kriecht dort schon |
| Schlagbelastung bei Kälte | **ABS+** |
| Acetonglättung, lackierbar | **ABS+** |
| Große Flächen ohne Warping-Risiko | [eSUN PETG](esun-petg.md) |
| Drucken im Wohnraum | [eSUN PETG](esun-petg.md) — kein Styrol |
| Offener Drucker | PETG oder [PLA+](esun-pla-plus.md) |

## Wenn etwas nicht stimmt

| Symptom | Zuerst prüfen |
|---|---|
| Ecken heben ab | Kammer schließen, Zugluft beseitigen, [Warping](../troubleshooting.md#warping) |
| Riss quer durch das Teil in halber Höhe | Kühlung auf 10 % senken, Kammer wärmer halten |
| Teil bricht entlang der Schichten | [Schichthaftung](../troubleshooting.md#schichthaftung) — Lüfter zuerst |
| Erste Schicht haftet nicht | Bett auf 95 °C, Platte entfetten |
| Unterextrusion | [Volumenstrom](../calibration.md#schritt-3--volumenstrom) |
| Starker Geruch | Raum lüften, nicht den Drucker öffnen |

---

[← eSUN PETG Transparent](esun-petg-transparent.md) · [Materialübersicht](README.md) · [Bambu PLA Basic →](bambu-pla-basic.md)
