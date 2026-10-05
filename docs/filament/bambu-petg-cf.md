# Bambu PETG-CF

[← Materialübersicht](README.md) · Status: 🔵 Startwert · Basis: `Bambu PETG-CF`

Kurzfaserverstärktes PETG. Rund 15 % der Masse sind gemahlene Kohlenstofffasern, und
die ändern das Material grundlegend: deutlich steifer, maßhaltiger und ohne
Fädenbildung, dafür spröder und nur noch halb so schnell. Das einzige
faserverstärkte Material im Sortiment, das auf **allen sechs Geräten** läuft und
ohne geschlossene Kammer auskommt.

---

## Kennwerte

| Größe | Wert | Abweichung zu Bambu PETG HF |
|---|---|---|
| Düse | **255 °C** (erste Schicht 255 °C) | +10 °C |
| Temperaturfenster | 240 – 270 °C | leicht höher |
| Bett | **70 °C** (erste Schicht 70 °C) | erste Schicht 5 °C kühler |
| Glasübergang | 70 °C | gleich |
| Flussrate | 0.95 | −0.02 |
| Lüfter | **5 – 40 %** | Untergrenze deutlich niedriger |
| Überhangkühlung | 100 % | gleich |
| Z-Hop | 0.4 mm | −0.2 mm |
| Abrasiv | **ja — gehärtete Düse zwingend** | |
| Trocknung | 70 °C / 8 h | 5 °C heißer |
| Lagerung | zwingend trocken | gleich |

**Die gehärtete Düse ist nicht verhandelbar.** Bambus eigenes Profil setzt
`required_nozzle_HRC = 40` — der höchste Wert, den die Bibliothek für ein
PETG-Derivat vergibt. Eine Messingdüse ist nach wenigen hundert Gramm sichtbar
aufgeweitet, und das zeigt sich zuerst als zu breite Außenwand, nicht als Verschleiß.

**Fasern unterdrücken Fäden.** Der angenehmste Nebeneffekt: PETG-CF zieht praktisch
keine Fäden. Die Fasern erhöhen die Schmelzviskosität so weit, dass der Faden beim
Abheben reißt statt nachzulaufen. Wer von PETG kommt, kann die Einzugswerte so
lassen, wie sie sind.

## Volumenstrom je Drucker und Düse

Werte in mm³/s. Basis ist der X1C; die übrigen Drucker werden über den
[Durchsatzfaktor](../drucker/README.md#durchsatzfaktoren) skaliert.

| Drucker | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| H2C | — | 13.2 | 13.2 |
| X1 Carbon | — | 11.5 | 11.5 |
| P1S | — | 10.9 | 10.9 |
| P1P | — | 10.9 | 10.9 |
| A1 | — | 10.3 | 10.3 |
| A1 mini | — | 9.8 | 9.8 |

> **Quelle der Werte.** Volumenstrom und Flussrate stammen aus
> `Bambu PETG-CF @BBL X1C 0.4 nozzle`: 11.5 mm³/s auf dem Standardextruder bei
> Flussrate 0.95. Für die 0.6-mm-Düse führt Bambu **kein eigenes Profil**; sie fällt
> auf `Bambu PETG-CF @BBL X1C` zurück, das denselben Wert nennt. Die flache Kurve ist
> deshalb keine Vereinfachung dieses Repositories, sondern die Herstellerangabe.

> **Warum 0.2 mm fehlt.** Für **kein** faserverstärktes Material der Bibliothek
> existiert ein 0.2-mm-Profil. Die Faserlänge liegt in der Größenordnung der
> Bohrung; die Düse setzt sich zu, statt zu fördern. `src/filaments/bambu-petg-cf.toml`
> führt deshalb nur `["0.4", "0.6"]`, und ein Test hält das fest.

**Der Durchsatz ist der eigentliche Preis.** Gegenüber [Bambu PETG HF](bambu-petg-hf.md)
mit 21.0 mm³/s bleiben rund **55 %** übrig — gut 45 % Durchsatz gehen verloren. Auf dem High-Flow-Extruder des X1C sieht
es besser aus — Bambu gibt dort 20 statt 11.5 mm³/s frei —, aber dieses Repository
führt grundsätzlich den Standardwert, weil er auf jeder Maschine gilt.

## Wofür PETG-CF das richtige Material ist

| Anforderung | Wahl |
|---|---|
| Steifigkeit bei geringem Gewicht | **PETG-CF** — Drohnenrahmen, Halterungen, Hebel |
| Maßhaltigkeit über Temperaturwechsel | **PETG-CF** — minimaler Schrumpf |
| Mattschwarze Oberfläche ohne Nachbearbeitung | **PETG-CF** |
| Faserverstärkung ohne geschlossene Kammer | **PETG-CF** — als einziges hier |
| Schlagbelastung, Fallenlassen | [Bambu PETG HF](bambu-petg-hf.md) — CF bricht spröde |
| Dauerhaft über 70 °C | [Bambu ASA-CF](bambu-asa-cf.md) |
| Durchsichtige oder farbige Teile | PETG — CF ist immer schwarz |

**Steif heißt nicht zäh.** Die Fasern erhöhen den E-Modul deutlich und senken die
Bruchdehnung genauso deutlich. Ein PETG-CF-Teil verbiegt sich nicht, es bricht —
und zwar ohne Vorwarnung. Für alles, was Stoß aufnehmen soll, bleibt normales PETG
die bessere Wahl.

## Wenn etwas nicht stimmt

| Symptom | Zuerst prüfen |
|---|---|
| Außenwände zu breit, Maße wachsen | Düse vermessen — abgenutzte Messingdüse |
| Düse setzt sich zu | Material trocknen, 0.4 mm als Minimum einhalten |
| Teil bricht spröde | Materialwahl — nicht Temperatur, siehe oben |
| Unterextrusion | [Volumenstrom](../calibration.md#schritt-3--volumenstrom) |
| Raue, pelzige Oberfläche | Feuchtigkeit — 70 °C / 8 h trocknen |
| Erste Schicht haftet nicht | Bett auf 70 °C halten, Platte entfetten |

---

[← Bambu PETG Translucent](bambu-petg-translucent.md) · [Materialübersicht](README.md) · [Bambu ABS →](bambu-abs.md)
