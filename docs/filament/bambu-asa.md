# Bambu ASA

[← Materialübersicht](README.md) · Status: 🔵 Startwert · Basis: `Bambu ASA`

UV-stabiles ABS. Chemisch ist ASA nahe am [ABS](bambu-abs.md) — gleiche Festigkeit,
gleicher Glasübergang, gleiche Kammerpflicht —, aber das Acrylnitril ist durch
Acrylat ersetzt. Das macht den entscheidenden Unterschied im Freien: ASA vergilbt
und verkreidet nicht. Das richtige Material für Teile, die Sonne und Wetter sehen.

---

## Kennwerte

| Größe | Wert | Abweichung zu Bambu ABS |
|---|---|---|
| Düse | **270 °C** (erste Schicht 270 °C) | erste Schicht 10 °C heißer |
| Temperaturfenster | 240 – 280 °C | gleich |
| Bett | **100 °C** (erste Schicht 100 °C) | **+10 °C** |
| Glasübergang | 100 °C | gleich |
| Flussrate | 0.95 | gleich |
| Lüfter | **10 – 35 %** | Obergrenze deutlich niedriger |
| Überhangkühlung | 80 % | gleich |
| Verzögerung ab | 12 s Schichtzeit | gleich |
| Z-Hop | 0.6 mm | gleich |
| Abrasiv | nein — Messingdüse genügt | |
| Trocknung | 80 °C / 8 h | gleich |
| Lagerung | trocken mit Silikagel | gleich |

**Das Bett läuft 10 °C heißer als bei ABS.** 100 °C sind bei ASA kein Spielraum,
sondern Herstellervorgabe: Der Schrumpf beim Abkühlen ist noch etwas höher als bei
ABS, und nur ein Bett auf Glasübergangstemperatur hält die erste Schicht fest. Auf
der A1 — offen, kleineres Netzteil — ist das der eigentliche Grund, warum dort nur
kleine Teile gelingen.

**Weniger Kühlung als ABS.** 35 % statt 60 % Obergrenze, unverändert aus
`Bambu ASA @BBL X1C`. Bambu ist bei ASA vorsichtiger, und das passt zum höheren
Schrumpf. Bei der 0.6-mm-Düse hebt der Hersteller die **Untergrenze** auf 25 % —
mehr Material pro Bahn braucht mehr Abfuhr.

## Volumenstrom je Drucker und Düse

Werte in mm³/s. Basis ist der X1C; die übrigen Drucker werden über den
[Durchsatzfaktor](../drucker/README.md#durchsatzfaktoren) skaliert.

| Drucker | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| H2C | 2.3 | 20.7 | 20.7 |
| X1 Carbon | 2 | 18 | 18 |
| P1S | 1.9 | 17.1 | 17.1 |
| P1P | 1.9 | 17.1 | 17.1 |
| A1 | 1.8 | 16.2 | 16.2 |
| A1 mini | — | — | — |

> **Quelle der Werte.** Aus `Bambu ASA @BBL X1C 0.4 nozzle`: 18 mm³/s auf dem
> Standardextruder, 25 auf High Flow, Flussrate 0.95. Die 0.2-mm-Spalte stammt aus
> `Bambu ASA @BBL X1C 0.2 nozzle`. Für 0.6 mm liefert Bambu kein eigenes Profil;
> die Düse fällt auf `Bambu ASA @BBL X1C` mit demselben Wertepaar zurück.

> **P1S und P1P erben vom X1C.** Anders als bei ABS führt Bambu für ASA keine
> eigenen P1-Profile — beide Geräte greifen direkt auf die X1C-Profile zu. Die
> Unterschiede in der Tabelle oben kommen allein aus dem Durchsatzfaktor dieses
> Repositories.

> **Warum die A1 mini leer bleibt.** Wie bei [ABS](bambu-abs.md) und
> [ASA-CF](bambu-asa-cf.md) liefert Bambu für dieses Gerät kein Basisprofil. Bett
> und Bauraum tragen das Material nicht. Ein Test prüft, dass alle drei
> Kammermaterialien die A1 mini auslassen.

**ASA ist schneller als ABS.** 18 gegen 16 mm³/s bei 0.4 mm — rund 13 % mehr
Durchsatz, bei gleichem Glasübergang. Wer die Kammer ohnehin hat, verliert mit ASA
gegenüber ABS nichts außer dem höheren Materialpreis.

## ASA, ABS oder PETG

| Anforderung | Wahl |
|---|---|
| Dauerhaft im Freien, UV und Regen | **ASA** — ABS verkreidet, PETG wird spröde |
| Dauerhaft über 70 °C | **ASA** oder [ABS](bambu-abs.md) |
| UV **und** maximale Steifigkeit | [Bambu ASA-CF](bambu-asa-cf.md) |
| Acetonglättung | **ASA** oder ABS — beide gleich gut |
| Kürzeste Druckzeit mit Kammer | **ASA** — 18 statt 16 mm³/s |
| Offener Drucker, großes Teil | [Bambu PETG HF](bambu-petg-hf.md) |
| Drucken im Wohnraum | PETG — ASA setzt wie ABS Styrol frei |

Die Gerätetabelle zur Kammerpflicht steht bei
[eSUN ABS+](esun-abs.md#die-geschlossene-kammer-ist-keine-empfehlung) und gilt für
ASA unverändert — mit einer Verschärfung: das 100 °C heiße Bett macht offene Geräte
noch weniger geeignet.

## Wenn etwas nicht stimmt

| Symptom | Zuerst prüfen |
|---|---|
| Ecken heben ab | Bett wirklich auf 100 °C? Zugluft beseitigen, [Warping](../troubleshooting.md#warping) |
| Riss quer durch das Teil | Kühlung auf 10 % senken, Kammer wärmer halten |
| Teil bricht entlang der Schichten | [Schichthaftung](../troubleshooting.md#schichthaftung) — Lüfter zuerst |
| Erste Schicht haftet nicht | Platte entfetten, Bett nachheizen lassen |
| Unterextrusion | [Volumenstrom](../calibration.md#schritt-3--volumenstrom) |
| Starker Geruch | Raum lüften, nicht den Drucker öffnen |

---

[← Bambu ABS](bambu-abs.md) · [Materialübersicht](README.md) · [Bambu ASA-CF →](bambu-asa-cf.md)
