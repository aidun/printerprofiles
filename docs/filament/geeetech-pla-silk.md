# Geeetech PLA Silk

[← Materialübersicht](README.md) · Status: 🔵 Startwert · Basis: `Generic PLA Silk`

PLA mit Glanzadditiv. Der seidige Schimmer entsteht nicht durch Pigment, sondern durch
die Art, wie die Schmelze erstarrt: langgestreckte Polymerketten reflektieren
gerichtet, und das erzeugt den perlmuttartigen Verlauf über gekrümmte Flächen. Dafür
braucht das Material **Wärme und wenig Luft** — und es ist das einzige Material in
diesem Repository, für das es **keine 0.2-mm-Profile** gibt.

---

## Kennwerte

| Größe | Wert | Abweichung zu Geeetech PLA+ 2.0 |
|---|---|---|
| Düse | **215 °C** (erste Schicht 220 °C) | +5 °C |
| Temperaturfenster | 200 – 230 °C | Untergrenze 5 °C höher |
| Bett | **60 °C** (erste Schicht 65 °C) | gleich |
| Glasübergang | 60 °C | gleich |
| Flussrate | 0.98 | gleich |
| Lüfter | **40 – 80 %** | deutlich zurückgenommen |
| Überhangkühlung | 100 % | gleich |
| Z-Hop | 0.4 mm | gleich |
| Abrasiv | nein — Messingdüse genügt | |
| Trocknung | 45 °C / 6 h | gleich |
| Lagerung | trocken mit Silikagel | gleich |

**Die Kühlung entscheidet über den Glanz, nicht die Temperatur.** Bei 100 %
Lüfterleistung erstarrt die Oberfläche, bevor sie sich glätten kann — aus dem Seidenglanz
wird eine stumpfe, streifige Fläche. Deshalb stehen hier 40 – 80 % statt der 60 – 100 %
des PLA+. Wer mehr Glanz will, senkt den Lüfter weiter, bevor er die Düse erhöht.

**Der Preis der zurückgenommenen Kühlung sind Überhänge.** Die Überhangkühlung bleibt
bei 100 %, weil sie nur punktuell greift, aber steile Überhänge werden hier sichtbar
schlechter als bei mattem oder normalem PLA. Stützmaterial ab etwa 50° ist bei diesem
Material die Regel, nicht die Ausnahme.

**Schichthaftung ist die Schwachstelle.** Das Glanzadditiv wirkt als Gleitmittel
zwischen den Schichten. Ein Silk-Teil ist bei gleicher Geometrie messbar schwächer als
eines aus PLA+. Für Sichtteile ist das belanglos, für Halterungen disqualifizierend.

## Volumenstrom je Drucker und Düse

Werte in mm³/s. Basis ist der X1C; die übrigen Drucker werden über den
[Durchsatzfaktor](../drucker/README.md#durchsatzfaktoren) skaliert.

| Drucker | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| H2C | — | 8.6 | 8.6 |
| X1 Carbon | — | 7.5 | 7.5 |
| P1S | — | 7.1 | 7.1 |
| P1P | — | 7.1 | 7.1 |
| A1 | — | 6.8 | 6.8 |
| A1 mini | — | 6.4 | 6.4 |

> **Warum 0.2 mm fehlt.** `Generic PLA Silk` ist das **einzige** Basisprofil der
> Bibliothek für Silk-PLA, und für die 0.2-mm-Düse existiert es auf **keinem** der
> sechs Geräte. Das ist keine Entscheidung dieses Repositories, sondern eine Lücke der
> Bibliothek: `src/filaments/geeetech-pla-silk.toml` führt deshalb nur
> `["0.4", "0.6"]`, und `test_silk_pla_has_no_02_profile_in_the_library` prüft gegen
> die installierte Bibliothek, dass die Lücke noch besteht. Kommt irgendwann ein
> 0.2-mm-Silk-Profil dazu, schlägt dieser Test fehl — und genau das ist seine Aufgabe.
> Es ist der **vierte** dokumentierte Grund, eine Düse auszulassen, neben abrasiv,
> faserverstärkt und flexibel; die [Düsenkunde](../nozzles.md) führt alle vier.

> **Quelle der Werte.** Volumenstrom (7.5 mm³/s) und Flussrate (0.98) stammen aus
> `Generic PLA Silk` der Bambu-Bibliothek. Ein Geeetech-eigenes Silk-Profil gibt es
> nicht — `Generic PLA @Geeetech` gilt für ungefülltes PLA und trägt dessen 12 mm³/s,
> was für Silk zu hoch wäre. Temperaturen und Lüfterwerte oben sind Startwerte dieses
> Repositories.

**7.5 mm³/s sind knapp zwei Drittel von Standard-PLA.** Das ist der eigentliche Preis:
Gegenüber [Geeetech PLA+ 2.0](geeetech-pla-plus-2.md) mit 12 mm³/s gehen rund 38 %
Durchsatz verloren, gegenüber [Bambu PLA Basic](bambu-pla-basic.md) mit 21 mm³/s
fast zwei Drittel. Der Glanz verträgt kein Tempo — hohe Geschwindigkeit reißt die
gerichtete Struktur auf, die ihn erzeugt.

## Wofür PLA Silk das richtige Material ist

| Anforderung | Wahl |
|---|---|
| Dekorteile, Vasen, Figuren | **PLA Silk** |
| Metallisch wirkende Oberflächen | **PLA Silk** — ohne Lack oder Galvanik |
| Große gekrümmte Flächen | **PLA Silk** — der Verlauf wirkt erst dort |
| Feine Details unter 0.4 mm | [Geeetech PLA Matte](geeetech-pla-matte.md) — kein 0.2-mm-Silk |
| Mechanische Belastung | [Geeetech PLA+ 2.0](geeetech-pla-plus-2.md) — Silk ist schwächer |
| Steile Überhänge | [Geeetech PLA Matte](geeetech-pla-matte.md) — mehr Kühlung erlaubt |

## Wenn etwas nicht stimmt

| Symptom | Zuerst prüfen |
|---|---|
| Glanz fehlt, Fläche wirkt stumpf | Lüfter senken — zuerst auf 30 %, dann Düse +5 °C |
| Streifen quer zur Bahn | zu schnell — Stufe *Qualität* wählen |
| Teil bricht entlang der Schichten | Materialwahl, siehe oben — Silk ist nicht tragend |
| Überhänge hängen durch | Stützmaterial, [Überhänge](../troubleshooting.md#überhänge) |
| Kein Profil für 0.2 mm im Slicer | korrekt, siehe oben |
| Unterextrusion | [Volumenstrom](../calibration.md#schritt-3--volumenstrom) |

---

[← Geeetech PLA Matte](geeetech-pla-matte.md) · [Materialübersicht](README.md) · [Geeetech PETG →](geeetech-petg.md)
