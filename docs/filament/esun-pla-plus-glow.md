# eSUN PLA+ Glow

[← Materialübersicht](README.md) · Status: 🔵 Startwert · Basis: `Generic PLA`
· ⚠️ **abrasiv — gehärtete Düse zwingend**

PLA+ mit Strontiumaluminat. Die Kombination aus Zähmodifikator und Leuchtpigment
ergibt das zähflüssigste PLA im Repository: Beide Zusätze erhöhen die
Schmelzviskosität, ihre Wirkung addiert sich. Entsprechend hoch liegt die Temperatur
und entsprechend niedrig der Volumenstrom.

---

## Vor dem ersten Druck

> **Gehärtete Düse verbauen.** Das Pigment ist dasselbe wie in allen Glow-Materialien
> und erreicht auf der Mohs-Skala rund 6. Eine Messingdüse verliert innerhalb von ein
> bis zwei Spulen ihre Maßhaltigkeit.
>
> **0.2 mm ist nicht verfügbar.** Die Pigmentagglomerate messen 20 – 50 µm und
> verstopfen eine 0.2-mm-Bohrung zuverlässig. Begründung in der
> [Düsenkunde](../nozzles.md#warum-02-mm-bei-glow-gesperrt-ist).

---

## Kennwerte

| Größe | Wert | Abweichung zu PLA+ |
|---|---|---|
| Düse | **228 °C** (erste Schicht 232 °C) | +8 °C |
| Temperaturfenster | 215 – 240 °C | enger und höher |
| Bett | **60 °C** (erste Schicht 65 °C) | gleich |
| Glasübergang | 55 °C | gleich |
| Flussrate | 0.95 | −0.02 |
| Lüfter | 50 – 90 % | gleich |
| Z-Hop | 0.4 mm | gleich |
| Düsen | 0.4 · 0.6 mm | **0.2 mm entfällt** |
| Trocknung | 45 °C / 6 h | gleich |

## Volumenstrom je Drucker und Düse

| Drucker | 0.4 mm | 0.6 mm |
|---|--:|--:|
| H2C | 11.5 | 16.1 |
| X1 Carbon | 10.0 | 14.0 |
| P1S | 9.5 | 13.3 |
| A1 | 9.0 | 12.6 |
| A1 mini | 8.5 | 11.9 |

Knapp 29 % unter PLA+ und der niedrigste Wert aller PLA-Varianten im Repository.
Wer hier zu hoch ansetzt, bekommt keine schnelleren Drucke, sondern Unterextrusion.

## Leuchtwirkung im Druck

- **Wandzahl entscheidet.** Das Leuchten kommt aus dem Materialvolumen. Drei Wände
  oder mehr, sonst bleibt das Teil blass.
- **Füllung 25 – 40 %** bringt bei dünnwandigen Teilen mehr als jede
  Temperaturänderung.
- **Aufladen** mit UV- oder kaltweißem Licht; Tageslicht wirkt deutlich schwächer.
- **Zäh und leuchtend.** Gegenüber [SUNLU PLA Glow](sunlu-pla-glow.md) ist dies die
  belastbarere Wahl — sinnvoll für Leuchtteile, die angefasst werden.

## Wenn etwas nicht stimmt

| Symptom | Zuerst prüfen |
|---|---|
| Extruder klickt, kein Material | [Verstopfung](../troubleshooting.md#verstopfung) — Düse und Durchmesser |
| Bahnen werden mit der Zeit breiter | Düse verschlissen, ersetzen |
| Unterextrusion | Temperatur anheben, dann [Volumenstrom](../calibration.md#schritt-3--volumenstrom) senken |
| Schwaches Leuchten | Wandzahl und Füllung, nicht die Temperatur |

---

[← eSUN PLA+](esun-pla-plus.md) · [Materialübersicht](README.md) · [eSUN PETG →](esun-petg.md)
