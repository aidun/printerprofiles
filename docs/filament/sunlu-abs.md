# SUNLU ABS

[← Materialübersicht](README.md) · Status: 🔵 Startwert · Basis: `Generic ABS`

Schlagfestes ABS aus SUNLUs Standardlinie. Der Glasübergang liegt mit **108.9 °C**
höher als bei jedem anderen ABS im Sortiment — SUNLU gibt damit den härtesten Wert
der drei ABS-Hersteller hier an und verlangt dafür ein heißeres Bett und eine geschlossene
Kammer. Durchsatz und Kühlung entsprechen dem [eSUN ABS+](esun-abs.md): beide erben
vom selben Basisprofil, weil für ABS kein herstellereigenes Profil existiert.

---

## Kennwerte

| Größe | Wert | Abweichung zu eSUN ABS+ |
|---|---|---|
| Düse | **260 °C** (erste Schicht 265 °C) | +5 °C |
| Temperaturfenster | 250 – 280 °C | +10 °C am oberen Ende |
| Bett | **95 °C** (erste Schicht 100 °C) | +5 °C |
| Glasübergang | **108 °C** | +8 °C |
| Flussrate | 0.95 | gleich |
| Lüfter | 10 – 30 % | gleich |
| Überhangkühlung | 60 % | gleich |
| Z-Hop | 0.4 mm | gleich |
| Abrasiv | nein — Messingdüse genügt | gleich |
| Trocknung | **80 °C / 6 h** | 10 °C heißer, 2 h länger |
| Lagerung | trocken mit Silikagel | gleich |

Weitere Angaben aus dem Datenblatt: Durchmesser 1.75 ± 0.03 mm, Dichte 1.02 g/cm³,
Zugfestigkeit 35 ± 5 MPa, Bruchdehnung 10 ± 5 %, Biegefestigkeit 60 ± 10 MPa,
Kerbschlagzähigkeit (IZOD) 15 ± 5 kJ/m².

**Zur Düsentemperatur.** SUNLU nennt nicht ein Fenster, sondern zwei
geschwindigkeitsabhängige: 250 – 260 °C bei 50 – 100 mm/s, 260 – 280 °C bei
100 – 200 mm/s. 260 °C liegt in beiden und ist deshalb der gesetzte Wert — er
funktioniert in der Stufe *Qualität* genauso wie in *Schnell*. Wer dauerhaft über
100 mm/s druckt, darf auf 270 °C hochgehen; das Basisprofil fährt ohnehin 270 °C.

**Zum Bett.** SUNLU gibt 80 – 100 °C vor. Gesetzt ist die obere Hälfte, weil bei ABS
nicht die Düse, sondern Bett und Kammer über den Verzug entscheiden. Das Basisprofil
liegt je Gerät zwischen 90 und 100 °C — der Wert hier fügt sich ein, statt ihn zu
unterbieten.

**Zur zurückgenommenen Kühlung.** `Generic ABS` gibt 10 – 80 % frei (auf der A1
10 – 20 %) und fährt Überhänge mit 80 %. Dieses Preset senkt die Obergrenze auf 30 %
und die Überhangkühlung auf 60 % — dieselbe bewusste Abweichung wie beim eSUN ABS+,
aus demselben Grund: bei ABS kostet jeder Prozentpunkt Lüfterleistung
Schichthaftung. Überhänge über etwa 45° gehören auf Stützmaterial.

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

> **Quelle der Werte.** Volumenstrom (15.0 mm³/s bei 0.4 und 0.6 mm, 2.0 mm³/s bei
> 0.2 mm) und Flussrate (0.95) stammen unverändert aus `Generic ABS` beziehungsweise
> `Generic ABS @0.2 nozzle`. **SUNLU liefert kein eigenes Bambu-Profil für ABS** —
> der Durchsatz ist deshalb der des generischen Basisprofils, und nur Temperatur,
> Glasübergang und Trocknung kommen aus dem Herstellerdatenblatt. Das ist dieselbe
> Lage wie beim eSUN ABS+, weshalb beide Materialien identische Durchsätze führen.

> **Warum die A1 mini leer bleibt.** Für ABS liefert Bambu auf diesem Gerät kein
> Basisprofil — Bauraum und Bettleistung tragen das Material nicht.
> `src/filaments/sunlu-abs.toml` führt deshalb einen `printers`-Schlüssel, und
> `tools/validate.py` prüft, dass die dort genannten Geräte genau die sind, für die
> die Bibliothek ein Profil hat.

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

Die Begründung gilt wortgleich wie beim eSUN ABS+ und steht dort ausführlich:
[Die geschlossene Kammer ist keine Empfehlung](esun-abs.md#die-geschlossene-kammer-ist-keine-empfehlung).
Kurz: ABS schrumpft beim Abkühlen um gut ein halbes Prozent, und jeder
Temperaturunterschied zwischen zwei Schichten wird zu Verzug oder Riss.

**Lüftung des Raumes, nicht des Druckers.** ABS setzt Styrol frei. Durchzug *im*
Drucker ist schädlich, Belüftung des Raumes dagegen richtig — idealerweise mit
Aktivkohlefilter oder Abluft.

## Welches ABS wofür

Drei ABS-Varianten liegen hier dicht beieinander. Der Unterschied ist klein, aber
nicht beliebig:

| | **SUNLU ABS** | [eSUN ABS+](esun-abs.md) | [Bambu ABS](bambu-abs.md) |
|---|--:|--:|--:|
| Düse | 260 °C | 255 °C | 270 °C |
| Bett | **95 °C** | 90 °C | 90 °C |
| Glasübergang | **108 °C** | 100 °C | 100 °C |
| Volumenstrom 0.4 mm | 15.0 | 15.0 | **16.0** |
| Trocknung | 80 °C / 6 h | 70 °C / 4 h | 80 °C / 8 h |
| Herstellerprofil in Studio | nein | nein | **ja** |

- **Höchste Wärmefestigkeit:** SUNLU ABS — 108 °C Glasübergang, acht Grad über den
  beiden anderen.
- **Kürzeste Druckzeit:** Bambu ABS — nur dort bringt ein herstellereigenes Profil
  einen gemessenen Durchsatz mit.
- **Schonendster Druckablauf:** eSUN ABS+ — niedrigste Düsentemperatur, kürzeste
  Trocknung.

Für Außenteile bleibt keines der drei die richtige Wahl: ABS verkreidet unter UV.
Dort gehört [Bambu ASA](bambu-asa.md) hin.

## Wenn etwas nicht stimmt

| Symptom | Zuerst prüfen |
|---|---|
| Ecken heben ab | Kammer schließen, Zugluft beseitigen, [Warping](../troubleshooting.md#warping) |
| Riss quer durch das Teil in halber Höhe | Kühlung auf 10 % senken, Kammer wärmer halten |
| Teil bricht entlang der Schichten | [Schichthaftung](../troubleshooting.md#schichthaftung) — Lüfter zuerst |
| Erste Schicht haftet nicht | Bett auf 100 °C, Platte entfetten |
| Fäden bei hoher Geschwindigkeit | Düse auf 270 °C — das obere SUNLU-Fenster gilt ab 100 mm/s |
| Unterextrusion | [Volumenstrom](../calibration.md#schritt-3--volumenstrom) |
| Starker Geruch | Raum lüften, nicht den Drucker öffnen |

---

[← SUNLU TPU](sunlu-tpu.md) · [Materialübersicht](README.md) · [eSUN PLA+ →](esun-pla-plus.md)
