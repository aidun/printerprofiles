# Bambu ABS

[← Materialübersicht](README.md) · Status: 🔵 Startwert · Basis: `Bambu ABS`

Herstellereigenes ABS. Dieselbe Materialklasse wie [eSUN ABS+](esun-abs.md), aber
mit einem spürbar anderen Rezept: 15 °C heißere Düse, mehr Kühlung und ein höherer
Volumenstrom. Bambu stimmt sein Profil auf die geschlossene Kammer des X1C ab und
kann sich die Kühlung deshalb erlauben.

---

## Kennwerte

| Größe | Wert | Abweichung zu eSUN ABS+ |
|---|---|---|
| Düse | **270 °C** (erste Schicht 260 °C) | +15 °C |
| Temperaturfenster | 240 – 280 °C | oben +5 °C |
| Bett | **90 °C** (erste Schicht 90 °C) | erste Schicht 5 °C kühler |
| Glasübergang | 100 °C | gleich |
| Flussrate | 0.95 | gleich |
| Lüfter | **10 – 60 %** | Obergrenze doppelt so hoch |
| Überhangkühlung | 80 % | +20 % |
| Z-Hop | 0.6 mm | +0.2 mm |
| Abrasiv | nein — Messingdüse genügt | |
| Trocknung | 80 °C / 8 h | heißer und länger |
| Lagerung | trocken mit Silikagel | gleich |

**Warum hier mehr Kühlung erlaubt ist.** Bei [eSUN ABS+](esun-abs.md) nimmt dieses
Repository die Kühlung bewusst auf 10 – 30 % zurück, weil das generische Profil
keine Kammer voraussetzt. Bambus Profil tut das implizit: es ist für X1C und H2C
geschrieben, wo die Umgebungsluft ohnehin warm ist. Die 60 % sind der
unveränderte Herstellerwert aus `Bambu ABS @BBL X1C`. Auf **P1P und A1** — beide
offen — ist das zu viel; dort gehört die Obergrenze von Hand auf 20 % gesenkt, so
wie Bambu es in den gerätespezifischen Profilen selbst macht.

**Die höhere Düsentemperatur ist der Grund für den Durchsatz.** 270 °C tragen
16 mm³/s, 255 °C nicht. Wer im Wohnraum druckt, nimmt lieber das eSUN-Profil mit
weniger Hitze und weniger Geruch.

## Volumenstrom je Drucker und Düse

Werte in mm³/s. Basis ist der X1C; die übrigen Drucker werden über den
[Durchsatzfaktor](../drucker/README.md#durchsatzfaktoren) skaliert.

| Drucker | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| H2C | 2.3 | 18.4 | 18.4 |
| X1 Carbon | 2 | 16 | 16 |
| P1S | 1.9 | 15.2 | 15.2 |
| P1P | 1.9 | 15.2 | 15.2 |
| A1 | 1.8 | 14.4 | 14.4 |
| A1 mini | — | — | — |

> **Quelle der Werte.** Aus `Bambu ABS @BBL X1C`: 16 mm³/s auf dem
> Standardextruder, 25 auf High Flow, Flussrate 0.95. Die 0.2-mm-Spalte stammt aus
> `Bambu ABS @BBL X1C 0.2 nozzle` mit 2.0 mm³/s. Für 0.6 mm nennt das Profil
> denselben Wert wie für 0.4 mm — die Kurve läuft flach, weil das Hotend begrenzt.

> **Warum die A1 mini leer bleibt.** Dasselbe wie bei [eSUN ABS+](esun-abs.md): für
> ABS liefert Bambu auf diesem Gerät kein Basisprofil. `printers` in
> `src/filaments/bambu-abs.toml` hält das fest, ein Test prüft es gegen die
> Bibliothek.

Gegenüber eSUN ABS+ sind das bei 0.4 mm rund **7 % mehr** Durchsatz, bei 0.2 mm ein
Drittel mehr.

## Bambu ABS oder eSUN ABS+

| Anforderung | Wahl |
|---|---|
| Kürzeste Druckzeit | **Bambu ABS** — 16 statt 15 mm³/s, mehr Kühlung |
| Offener Drucker (P1P, A1) | **eSUN ABS+** — Profil ist auf wenig Kühlung ausgelegt |
| Drucken im Wohnraum | **eSUN ABS+** — 255 °C riechen weniger als 270 °C |
| Überhänge und Details | **Bambu ABS** — 60 % Lüfter statt 30 % |
| Große, flächige Teile | **eSUN ABS+** auf dem H2C — Warping ist hier das Risiko |
| Acetonglättung | beide gleich gut |

Die geschlossene Kammer gilt für beide gleichermaßen — die Gerätetabelle dazu steht
bei [eSUN ABS+](esun-abs.md#die-geschlossene-kammer-ist-keine-empfehlung) und gilt
unverändert. Styrol entsteht ebenfalls bei beiden: Raum lüften, Drucker nicht öffnen.

## Wenn etwas nicht stimmt

| Symptom | Zuerst prüfen |
|---|---|
| Ecken heben ab | Lüfter auf 20 % senken, Zugluft beseitigen, [Warping](../troubleshooting.md#warping) |
| Riss quer durch das Teil | Kühlung senken — 60 % sind für offene Drucker zu viel |
| Teil bricht entlang der Schichten | [Schichthaftung](../troubleshooting.md#schichthaftung) |
| Erste Schicht haftet nicht | Bett auf 90 °C, Platte entfetten |
| Unterextrusion | [Volumenstrom](../calibration.md#schritt-3--volumenstrom) |
| Starker Geruch | Raum lüften, oder auf [eSUN ABS+](esun-abs.md) wechseln |

---

[← Bambu PETG-CF](bambu-petg-cf.md) · [Materialübersicht](README.md) · [Bambu ASA →](bambu-asa.md)
