# SUNLU PETG Glow

[← Materialübersicht](README.md) · Status: 🟢 **verifiziert für H2C · 0.4 mm**
· Basis: `Generic PETG` · ⚠️ **abrasiv — gehärtete Düse zwingend**

Die anspruchsvollste Kombination im Repository: PETG mit Leuchtpigment vereint die
Abrasivität des Glow-Materials mit der Feuchtigkeitsempfindlichkeit und
Kühlungsempfindlichkeit von PETG.

> **Dies ist das Referenzmaterial dieses Repositories.** Die Werte für den H2C mit
> 0.4-mm-Düse sind am Gerät gemessen und bilden den Anker, aus dem alle anderen
> Kombinationen abgeleitet sind. Ein gemessener Volumenstrom von 12.6 mm³/s ergibt
> über den H2C-Durchsatzfaktor 1.15 den Basiswert 11.0 mm³/s, aus dem die übrigen
> Drucker berechnet werden.

---

## Vor dem ersten Druck

- **Gehärtete Düse verbauen.** Wie bei [PLA Glow](sunlu-pla-glow.md) — das Pigment
  ist dasselbe.
- **0.2 mm ist nicht verfügbar.** Siehe [Düsenkunde](../nozzles.md#warum-02-mm-bei-glow-gesperrt-ist).
- **Filament trocknen.** 65 °C / 8 h. Bei diesem Material ist der Unterschied
  zwischen trockenem und feuchtem Filament größer als jede Parameteränderung.

---

## Kennwerte

| Größe | Wert | Besonderheit |
|---|---|---|
| Düse | **248 °C** (erste Schicht 250 °C) | 🟢 gemessen |
| Temperaturfenster | **245 – 250 °C** | bewusst eng |
| Bett | **70 °C** (erste Schicht 75 °C) | |
| Glasübergang | 71 °C | |
| Flussrate | **0.98** | 🟢 gemessen |
| Lüfter | **10 – 30 %** | niedrigster Wert im Repository |
| Überhangkühlung | 40 % | |
| Z-Hop | 0.6 mm | |
| Düsen | 0.4 · 0.6 mm | **0.2 mm entfällt** |
| Trocknung | 65 °C / 8 h | zwingend |

**Zum engen Temperaturfenster:** 245 – 250 °C ist kein Tippfehler und keine
Vorsicht. Unterhalb von 245 °C fördert das pigmentbeladene Material sichtbar zu
wenig, oberhalb von 250 °C beginnt es zu fädeln und die Leuchtpartikel setzen sich
an der Düsenwand ab. Das Fenster ist gemessen, nicht geschätzt.

## Volumenstrom je Drucker und Düse

| Drucker | 0.4 mm | 0.6 mm |
|---|--:|--:|
| H2C | **12.6** 🟢 | 16.7 |
| X1 Carbon | 11 | 14.5 |
| P1S | 10.4 | 13.8 |
| P1P | 10.4 | 13.8 |
| A1 | 9.9 | 13.1 |
| A1 mini | 9.3 | 12.3 |

Nur der fett markierte Wert ist gemessen. Alle anderen sind über den
[Durchsatzfaktor](../drucker/README.md#durchsatzfaktoren) berechnete Startwerte —
vor dem ersten größeren Druck auf einem anderen Gerät empfiehlt sich
[Schritt 3 der Kalibrierung](../calibration.md#schritt-3--volumenstrom).

## Wenn etwas nicht stimmt

| Symptom | Zuerst prüfen |
|---|---|
| Unterextrusion | Temperatur an die Obergrenze, dann Volumenstrom senken |
| Knacken, Blasen | [Feuchtigkeit](../troubleshooting.md#feuchtigkeit) — trocknen |
| Extruder klickt | [Verstopfung](../troubleshooting.md#verstopfung) — Düse prüfen |
| Teil bricht entlang der Schichten | Kühlung ist bereits minimal — Temperatur prüfen |
| Schwaches Leuchten | Wandzahl und Füllung erhöhen |

---

[← SUNLU PETG](sunlu-petg.md) · [Materialübersicht](README.md) · [SUNLU PETG Transparent →](sunlu-petg-transparent.md)
