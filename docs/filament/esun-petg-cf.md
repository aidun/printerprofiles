# eSUN PETG-CF

[← Materialübersicht](README.md) · Status: 🔵 Startwert · Basis: `Generic PETG-CF`

Kurzfaserverstärktes PETG von eSUN. Die gemahlene Kohlenstofffaser bringt gegenüber
ungefülltem PETG **84 % mehr Biegefestigkeit** und ein knapp dreifaches Biegemodul;
die Wärmeformbeständigkeit bleibt bei 70 °C. Läuft rund 5 °C kühler als das
[Bambu PETG-CF](bambu-petg-cf.md) und auf einem deutlich wärmeren Bett — und wie
dieses auf **allen sechs Geräten**, ohne geschlossene Kammer.

---

## Kennwerte

| Größe | Wert | Abweichung zu Bambu PETG-CF |
|---|---|---|
| Düse | **250 °C** (erste Schicht 255 °C) | −5 °C |
| Temperaturfenster | 240 – 260 °C | oben 10 °C enger |
| Bett | **80 °C** (erste Schicht 85 °C) | **+10 °C** |
| Glasübergang | 70 °C | gleich |
| Flussrate | 0.95 | gleich |
| Lüfter | 5 – 40 % | gleich |
| Überhangkühlung | 100 % | gleich |
| Z-Hop | 0.4 mm | gleich |
| Abrasiv | **ja — gehärtete Düse zwingend** | gleich |
| Trocknung | **65 °C / 8 h** | 5 °C kühler |
| Lagerung | zwingend trocken | gleich |

Weitere Angaben aus dem Datenblatt: Dichte 1.26 g/cm³, Zugfestigkeit (XY)
51.3 MPa, Biegefestigkeit (XY) 77.2 MPa, Biegemodul (XY) 3618.5 MPa,
Kerbschlagzähigkeit (IZOD, XY) 4.39 kJ/m², empfohlene Druckgeschwindigkeit
unter 150 mm/s.

**Zur Düsentemperatur.** eSUN gibt 240 – 260 °C vor, das Basisprofil fährt 255 °C.
Gesetzt ist die Mitte des Herstellerfensters — 250 °C reichen für 11.5 mm³/s aus und
halten die Faser weniger lange heiß. Für dicke Wände oder große Flächen darf man bis
260 °C hochgehen, über das Herstellerfenster hinaus aber nicht.

**Zum deutlich wärmeren Bett.** eSUN nennt 75 – 90 °C, das Basisprofil nur 70 °C.
Gesetzt ist die untere Hälfte des Herstellerfensters: 80 °C. Bei faserverstärktem
PETG ist das Ablösen der ersten Schicht das häufigere Problem als zu starke Haftung,
weil die Faser den Schrumpf richtungsabhängig macht. Die zehn Grad mehr sind die
bewusste Abweichung vom Basisprofil.

**Die gehärtete Düse ist nicht verhandelbar.** `Generic PETG-CF` setzt
`required_nozzle_HRC = 40` — der höchste Wert, den die Bibliothek für ein
PETG-Derivat vergibt. eSUN selbst schreibt auf dem Datenblatt eine Düse aus
gehärtetem Stahl für 0.4 und 0.6 mm vor. Hersteller und Bibliothek sind hier also
einig; eine Messingdüse ist nach wenigen hundert Gramm sichtbar aufgeweitet, und das
zeigt sich zuerst als zu breite Außenwand, nicht als Verschleiß.

**Zur Kühlung — Abweichung vom Datenblatt.** eSUN gibt den Lüfter mit 100 % an. Das
Preset bleibt bei den 5 – 40 % der Bibliothek und öffnet nur über Überhängen auf
100 %. PETG verliert unter voller Kühlung Schichthaftung, und die Faser ändert daran
nichts — sie macht das Teil ohnehin spröder. Hier gewinnt die Bibliothek gegen das
Datenblatt.

## Volumenstrom je Drucker und Düse

Werte in mm³/s. Basis ist der X1C; die übrigen Drucker werden über den
[Durchsatzfaktor](../drucker/README.md#durchsatzfaktoren) skaliert — **außer auf der
A1 und der A1 mini**, siehe unten.

| Drucker | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| H2C | — | 13.2 | 13.2 |
| X1 Carbon | — | 11.5 | 11.5 |
| P1S | — | 10.9 | 10.9 |
| P1P | — | 10.9 | 10.9 |
| A1 | — | **8** | **8** |
| A1 mini | — | **8** | **8** |

> **Quelle der Werte.** Volumenstrom und Flussrate stammen aus
> `Generic PETG-CF @BBL X1C`: 11.5 mm³/s auf dem Standardextruder bei Flussrate 0.95.
> Für die 0.6-mm-Düse führt die Bibliothek **kein eigenes Profil**; der Wert bleibt
> derselbe, die flache Kurve ist also die Herstellerangabe und keine Vereinfachung.
> Ein herstellereigenes eSUN-PETG-CF-Profil gibt es in Studio nicht — Temperaturen
> und Bettwerte oben kommen aus dem eSUN-Datenblatt.

> **Warum A1 und A1 mini bei 8 mm³/s stehen bleiben.**
> `Generic PETG-CF @BBL A1` und `@BBL A1M` nennen 8 mm³/s ausdrücklich — klar
> unterhalb dessen, was der Durchsatzfaktor aus dem X1C-Wert ableiten würde (10.3
> beziehungsweise 9.8). Hier gewinnt die Bibliothek: eine Obergrenze über dem, was
> das Hotend aufschmelzen kann, druckt nicht schneller, sondern unterextrudiert.
> `src/filaments/esun-petg-cf.toml` trägt die Deckel deshalb in einer eigenen Tabelle
> `[volumetric_flow_cap]`, und ein Test prüft jeden einzelnen gegen das Basisprofil.

> **Warum 0.2 mm fehlt.** Für **kein** faserverstärktes Material der Bibliothek
> existiert ein 0.2-mm-Profil. Die Faserlänge liegt in der Größenordnung der
> Bohrung; die Düse setzt sich zu, statt zu fördern. `src/filaments/esun-petg-cf.toml`
> führt deshalb nur `["0.4", "0.6"]`, und ein Test hält das fest.

## Welches PETG-CF

Die beiden faserverstärkten PETG-Varianten liegen dicht beieinander — sie
unterscheiden sich im Bett, in der Trocknung und darin, wie viel das Herstellerprofil
freigibt:

| | **eSUN PETG-CF** | [Bambu PETG-CF](bambu-petg-cf.md) |
|---|--:|--:|
| Düse | 250 °C | 255 °C |
| Bett | **80 °C** | 70 °C |
| Volumenstrom X1C 0.4 mm | 11.5 | 11.5 |
| Volumenstrom A1 / A1 mini | 8 | **9** |
| Trocknung | 65 °C / 8 h | 70 °C / 8 h |
| Herstellerprofil in Studio | nein | **ja** |

Auf den vier großen Geräten sind die Durchsätze identisch — beide Materialien führen
denselben Wert, weil Bambu für sein eigenes PETG-CF nichts anderes angibt als für das
generische. Der Unterschied zeigt sich nur auf den Bettschleudern: dort gibt Bambu
für sein Material 9 mm³/s frei, für das generische 8.

## Wofür PETG-CF das richtige Material ist

| Anforderung | Wahl |
|---|---|
| Steifigkeit bei geringem Gewicht | **PETG-CF** — Drohnenrahmen, Halterungen, Hebel |
| Maßhaltigkeit über Temperaturwechsel | **PETG-CF** — minimaler Schrumpf |
| Mattschwarze Oberfläche ohne Nachbearbeitung | **PETG-CF** |
| Faserverstärkung ohne geschlossene Kammer | **PETG-CF** |
| Schlagbelastung, Fallenlassen | [eSUN PETG](esun-petg.md) — CF bricht spröde |
| Dauerhaft über 70 °C | [Bambu ASA-CF](bambu-asa-cf.md) |
| Durchsichtige oder farbige Teile | PETG — CF ist immer schwarz |

**Steif heißt nicht zäh.** eSUN belegt das selbst: 84 % mehr Biegefestigkeit und
195 % mehr Biegemodul gegenüber ungefülltem PETG, bei einer Kerbschlagzähigkeit von
nur 4.39 kJ/m². Ein PETG-CF-Teil verbiegt sich nicht, es bricht — und zwar ohne
Vorwarnung. Für alles, was Stoß aufnehmen soll, bleibt normales PETG die bessere Wahl.

**Fasern unterdrücken Fäden.** Der angenehmste Nebeneffekt: PETG-CF zieht praktisch
keine Fäden. Die Fasern erhöhen die Schmelzviskosität so weit, dass der Faden beim
Abheben reißt statt nachzulaufen. Wer von [eSUN PETG](esun-petg.md) kommt, kann die
Einzugswerte so lassen, wie sie sind.

## Wenn etwas nicht stimmt

| Symptom | Zuerst prüfen |
|---|---|
| Außenwände zu breit, Maße wachsen | Düse vermessen — abgenutzte Messingdüse |
| Düse setzt sich zu | Material trocknen, 0.4 mm als Minimum einhalten |
| Teil bricht spröde | Materialwahl — nicht Temperatur, siehe oben |
| Erste Schicht löst sich an den Ecken | Bett auf 85 °C halten, Platte entfetten |
| Unterextrusion | [Volumenstrom](../calibration.md#schritt-3--volumenstrom) |
| Raue, pelzige Oberfläche | Feuchtigkeit — 65 °C / 8 h trocknen |
| Auf der A1 langsamer als erwartet | kein Fehler: 8 mm³/s sind die Herstellerangabe |

---

[← eSUN PETG Transparent](esun-petg-transparent.md) · [Materialübersicht](README.md) · [eSUN ABS+ →](esun-abs.md)
