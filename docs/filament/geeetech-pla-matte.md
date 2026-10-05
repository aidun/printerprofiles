# Geeetech PLA Matte

[← Materialübersicht](README.md) · Status: 🔵 Startwert · Basis: `Generic PLA`

PLA mit mineralischer Füllung. Die Füllpartikel streuen das Licht, statt es zu
spiegeln — die Oberfläche wirkt samtig, und Schichtlinien wie Nahtstellen verschwinden
darin fast vollständig. Das ist der eine Grund für dieses Material. Gedruckt wird es
wie normales PLA, nur ein paar Grad kühler.

---

## Kennwerte

| Größe | Wert | Abweichung zu Geeetech PLA+ 2.0 |
|---|---|---|
| Düse | **205 °C** (erste Schicht 210 °C) | −5 °C |
| Temperaturfenster | 190 – 220 °C | Obergrenze 10 °C tiefer |
| Bett | **55 °C** (erste Schicht 60 °C) | −5 °C |
| Glasübergang | 60 °C | gleich |
| Flussrate | 0.98 | gleich |
| Lüfter | **60 – 100 %** | gleich |
| Überhangkühlung | 100 % | gleich |
| Z-Hop | 0.4 mm | gleich |
| Abrasiv | nein — Messingdüse genügt | |
| Trocknung | 45 °C / 6 h | gleich |
| Lagerung | trocken, ab Werk vakuumiert mit Trockenmittel | Beutel aufbewahren |

**Das Fenster ist eng, und zwar absichtlich.** Geeetech nennt für dieses Material
**190 – 220 °C** bei 50 – 70 °C Bett — zehn Grad weniger nach oben als beim PLA+. Zu
heiß gefahren verliert die Oberfläche genau das, wofür man das Material kauft: Die
Füllung sinkt in der zu dünnflüssigen Schmelze ab, und matt wird wieder glänzend,
fleckig und ungleichmäßig. Wer Schichthaftungsprobleme hat, erhöht hier nicht die
Temperatur, sondern senkt den Lüfter.

**Die Füllung ist nicht abrasiv.** Mineralische Mattierungsmittel sind weich; eine
Messingdüse hält das aus. Anders als bei Glow-PLA oder faserverstärkten Materialien
braucht es keine gehärtete Düse und keine Einschränkung bei 0.2 mm.

**Die Toleranz ist die beste Zahl im Datenblatt.** Geeetech gibt ±0.03 mm
Durchmessertoleranz an — das ist ein Drittel dessen, was im Billigsegment üblich ist,
und der Grund, warum die Flussrate von 0.98 hier meist ohne Nachkalibrierung passt.

## Volumenstrom je Drucker und Düse

Werte in mm³/s. Basis ist der X1C; die übrigen Drucker werden über den
[Durchsatzfaktor](../drucker/README.md#durchsatzfaktoren) skaliert.

| Drucker | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| H2C | 1.8 | 13.8 | 13.8 |
| X1 Carbon | 1.6 | 12 | 12 |
| P1S | 1.5 | 11.4 | 11.4 |
| P1P | 1.5 | 11.4 | 11.4 |
| A1 | 1.4 | 10.8 | 10.8 |
| A1 mini | 1.4 | 10.2 | 10.2 |

> **Quelle der Werte.** Identisch mit [Geeetech PLA+ 2.0](geeetech-pla-plus-2.md):
> 12.0 mm³/s bei Flussrate 0.98 aus `Generic PLA @Geeetech`, dem von Geeetech selbst
> beigesteuerten Profil der Bambu-Studio-Bibliothek. Die mineralische Füllung ändert
> die Aufschmelzleistung nicht messbar — sie ändert die Oberfläche. Ein eigenes
> Matte-Profil führt Geeetech nicht.

**Matt heißt nicht langsamer.** Der Durchsatz ist derselbe wie beim PLA+. Was die
Druckzeit tatsächlich beeinflusst, ist die Schichthöhe: Die matte Oberfläche verbirgt
dicke Schichten so gut, dass die Stufe *Schnell* hier oft reicht, wo man bei glänzendem
PLA zur *Qualität* greifen müsste.

## Wofür PLA Matte das richtige Material ist

| Anforderung | Wahl |
|---|---|
| Sichtteile ohne Nacharbeit, Gehäuse, Blenden | **PLA Matte** |
| Fotografierte oder gescannte Teile | **PLA Matte** — kein Streulicht, keine Glanzkanten |
| Schichtlinien verstecken | **PLA Matte** — wirkt stärker als jede Schichthöhe |
| Mechanische Belastung | [Geeetech PLA+ 2.0](geeetech-pla-plus-2.md) — zäher |
| Glänzende Oberfläche | [Geeetech PLA Silk](geeetech-pla-silk.md) |
| Wärme über 50 °C | [Geeetech PETG](geeetech-petg.md) |

## Wenn etwas nicht stimmt

| Symptom | Zuerst prüfen |
|---|---|
| Oberfläche glänzt stellenweise | zu heiß — Düse auf 200 °C senken |
| Flecken, ungleichmäßiger Glanzgrad | Düse senken, Lüfter erhöhen |
| Teil bricht entlang der Schichten | Lüfter senken, **nicht** über 220 °C gehen |
| Unterextrusion | [Volumenstrom](../calibration.md#schritt-3--volumenstrom) |
| Erste Schicht haftet nicht | Bett auf 60 °C halten, Platte entfetten |

---

[← Geeetech PLA+ 2.0](geeetech-pla-plus-2.md) · [Materialübersicht](README.md) · [Geeetech PLA Silk →](geeetech-pla-silk.md)
