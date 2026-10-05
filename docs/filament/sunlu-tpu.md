# SUNLU TPU

[← Materialübersicht](README.md) · Status: 🔵 Startwert · Basis: `Generic TPU`

Flexibles Material, Shore 95A — das erste Nicht-Starrmaterial im Repository. TPU
biegt sich, statt zu brechen, und übersteht Belastungen, bei denen PLA und PETG
splittern: Dichtungen, Puffer, Riemen, Schutzhüllen, griffige Auflagen. Dafür
verlangt es die größte Umstellung im Druckablauf, denn der begrenzende Faktor ist
nicht mehr die Düse, sondern der Extruder.

---

## Kennwerte

| Größe | Wert | Hinweis |
|---|---|---|
| Düse | **225 °C** (erste Schicht 230 °C) | Mitte des Fensters |
| Temperaturfenster | 200 – 245 °C | breit, TPU ist temperaturtolerant |
| Bett | **35 °C** (erste Schicht 40 °C) | niedrigster Wert im Repository |
| Glasübergang | 30 °C | siehe Hinweis unten |
| Flussrate | 1.00 | unkorrigiert |
| Lüfter | **100 %** | durchgehend |
| Überhangkühlung | 100 % | |
| Z-Hop | 0.4 mm | |
| Abrasiv | nein — Messingdüse genügt | |
| Trocknung | **50 °C / 8 h** | niedrigere Temperatur als PETG, längere Zeit |
| Lagerung | zwingend trocken mit Silikagel | kritischster Wert dieses Materials |

> **Zum Glasübergang von 30 °C.** Der Wert stammt aus `Generic TPU` und ist keine
> Verformungsgrenze im Sinne von PLA. Thermoplastische Elastomere haben keinen
> scharfen Übergang — ein TPU-Teil wird bei 40 °C weicher, verliert aber nicht
> seine Form. Der Slicer nutzt die Zahl für interne Entscheidungen, nicht als
> Einsatzgrenze.

Das kalte Bett ist Absicht und entspricht dem Basisprofil: TPU haftet auf der
PEI-Platte von sich aus sehr gut. Bei 60 °C verschweißt es so fest, dass das Teil
beim Ablösen reißt, bevor es sich löst.

Die Düsentemperatur liegt mit 225 °C **unter** den 240 °C des Basisprofils. Das ist
die einzige nennenswerte Abweichung dieses Presets: Heißes TPU fädelt stark, und bei
3.2 mm³/s fehlt die Wärme nirgends. Wer schlechte Schichthaftung sieht, geht in
5-°C-Schritten nach oben — das Fenster reicht bis 245 °C.

## Volumenstrom je Drucker und Düse

Werte in mm³/s. Basis ist der X1C; die übrigen Drucker werden über den
[Durchsatzfaktor](../drucker/README.md#durchsatzfaktoren) skaliert.

| Drucker | 0.4 mm | 0.6 mm |
|---|--:|--:|
| H2C | 3.7 | 3.7 |
| X1 Carbon | 3.2 | 3.2 |
| P1S | 3 | 3 |
| P1P | 3 | 3 |
| A1 | 2.9 | 2.9 |
| A1 mini | 2.7 | 2.7 |

> **Quelle der Werte.** Volumenstrom und Flussrate stammen unverändert aus
> `Generic TPU` — ein eigenes X1C-Profil führt Bambu für TPU nicht, der X1C erbt
> direkt vom Grundprofil. Ein herstellereigenes SUNLU-TPU-Profil gibt es ebenfalls
> nicht; die Werte bleiben Startwerte, bis eine Messung sie ersetzt.

Die Kurve ist flach, und das ist kein Rundungsfehler: 0.4 und 0.6 mm teilen
denselben Wert. Eine größere Bohrung hilft hier nicht, weil nicht die Düse der
Engpass ist, sondern das weiche Filament im Vorschub — es knickt unter Druck aus,
statt zu fördern. Der Durchsatz liegt damit bei etwa einem Fünftel dessen, was
[SUNLU PLA](sunlu-pla.md) auf derselben Maschine schafft. TPU-Drucke dauern lange;
das ist eine Eigenschaft des Materials, kein Konfigurationsfehler.

## Was beim Drucken anders ist

**1 · Die 0.2-mm-Düse ist gesperrt.** Nicht aus Vorsicht: Für TPU liefert Bambu auf
keinem der sechs Geräte ein 0.2-mm-Basisprofil. Dieses Repository erfindet keines,
deshalb führt `src/filaments/sunlu-tpu.toml` nur `0.4` und `0.6` —
mehr dazu unter [Düsen](../nozzles.md).

**2 · Nicht über die AMS.** Weiches Filament verhakt sich in den Umlenkungen und im
Puffer. Bambu trägt dieser Unterscheidung selbst Rechnung und führt eine eigene
Variante `Generic TPU for AMS`; die Presets hier bauen bewusst auf dem
Nicht-AMS-Profil auf. TPU gehört also auf den externen Spulenhalter, mit kurzem,
geradem Weg zum Extruder und einer Spule, die sich leicht dreht.

**3 · Langsam fahren.** Die niedrigen Volumenströme oben begrenzen die
Druckgeschwindigkeit automatisch, solange der Slicer sie beachtet. Wer von Hand
hochregelt, bekommt keine Unterextrusion mit sauberer Oberfläche, sondern
aussetzende Förderung.

**4 · Retraction sparsam.** Elastisches Filament dehnt sich beim Rückzug, statt
Druck abzubauen. Die Werte des Basisprofils sind dafür schon abgestimmt; wer sie
erhöht, bekommt Löcher am Nahtpunkt.

**5 · Feuchtigkeit ist hier das größte Risiko.** TPU nimmt Wasser schneller auf als
jedes andere Material im Sortiment. Eine offen gelagerte Spule ist nach wenigen
Tagen hörbar feucht — es knistert und blubbert an der Düse. Vor dem Druck trocknen,
Details unter [Feuchtigkeit](../troubleshooting.md#feuchtigkeit).

## Wenn etwas nicht stimmt

| Symptom | Zuerst prüfen |
|---|---|
| Förderung setzt aus, Klicken im Extruder | Geschwindigkeit senken, [Volumenstrom](../calibration.md#schritt-3--volumenstrom) |
| Knistern, Blasen, raue Oberfläche | [Feuchtigkeit](../troubleshooting.md#feuchtigkeit) — 50 °C / 8 h |
| Filament verhakt vor dem Extruder | Spulenweg prüfen, AMS vermeiden |
| Teil reißt beim Ablösen von der Platte | Bett kalt werden lassen, 35 °C nicht erhöhen |
| Fäden zwischen Wänden | Temperatur um 5 °C senken, langsamer fahren |

---

[← SUNLU PETG Transparent](sunlu-petg-transparent.md) · [Materialübersicht](README.md) · [eSUN PLA+ →](esun-pla-plus.md)
