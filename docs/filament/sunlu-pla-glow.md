# SUNLU PLA Glow

[← Materialübersicht](README.md) · Status: 🔵 Startwert · Basis: `Generic PLA`
· ⚠️ **abrasiv — gehärtete Düse zwingend**

PLA mit Strontiumaluminat-Leuchtpigment. Das Pigment macht das Material grobkörnig
und stark abrasiv: Es schleift Messingdüsen innerhalb einer Spule messbar auf und
neigt in engen Bohrungen zum Verklumpen.

---

## Vor dem ersten Druck

> **Gehärtete Düse verbauen.** Strontiumaluminat erreicht auf der Mohs-Skala rund 6
> und liegt damit über gehärtetem Messing. Eine Standarddüse verliert ihre
> Maßhaltigkeit nach ein bis zwei Spulen — die Folge sind schleichend breitere
> Bahnen und Maßabweichungen, die keine Kalibrierung mehr einfängt.
>
> **0.2 mm ist nicht verfügbar.** Die Pigmentagglomerate messen 20 – 50 µm und
> verstopfen eine 0.2-mm-Bohrung zuverlässig. Dieses Repository liefert für Glow
> bewusst keine 0.2-mm-Profile aus. Begründung in der
> [Düsenkunde](../nozzles.md#warum-02-mm-bei-glow-gesperrt-ist).

---

## Kennwerte

| Größe | Wert | Abweichung zu PLA |
|---|---|---|
| Düse | **225 °C** (erste Schicht 230 °C) | +10 °C |
| Temperaturfenster | 210 – 240 °C | enger und höher |
| Bett | **55 °C** (erste Schicht 60 °C) | gleich |
| Glasübergang | 55 °C | gleich |
| Flussrate | 0.96 | −0.02 |
| Lüfter | 60 – 100 % | gleich |
| Z-Hop | 0.4 mm | gleich |
| Düsen | 0.4 · 0.6 mm | **0.2 mm entfällt** |
| Trocknung | 45 °C / 6 h | gleich |

Die höhere Düsentemperatur kompensiert den durch das Pigment gestörten Schmelzfluss,
die leicht reduzierte Flussrate den Volumenanteil der Feststoffpartikel.

## Volumenstrom je Drucker und Düse

| Drucker | 0.4 mm | 0.6 mm |
|---|--:|--:|
| H2C | 12.1 | 17.2 |
| X1 Carbon | 10.5 | 15.0 |
| P1S | 10.0 | 14.2 |
| A1 | 9.5 | 13.5 |
| A1 mini | 8.9 | 12.8 |

Rund 30 % unter normalem PLA. Das Pigment behindert die Wärmeübertragung im
Schmelzbereich; höhere Werte führen direkt zu Unterextrusion.

## Leuchtwirkung im Druck

- **Wandzahl entscheidet.** Das Leuchten kommt aus dem Materialvolumen, nicht von
  der Oberfläche. Für sichtbar helle Teile die Stufe *Qualität* (3 Wände) oder
  mehr Wandlinien wählen.
- **Füllung erhöhen.** Bei dünnwandigen Teilen bringt eine Füllung von 25 – 40 %
  mehr als jede Temperaturänderung.
- **Aufladen** mit UV- oder kaltweißem Licht; Tageslicht wirkt deutlich schwächer.

## Wenn etwas nicht stimmt

| Symptom | Zuerst prüfen |
|---|---|
| Extruder klickt, kein Material | [Verstopfung](../troubleshooting.md#verstopfung) — Düse und Durchmesser |
| Bahnen werden mit der Zeit breiter | Düse verschlissen, ersetzen |
| Unterextrusion | [Volumenstrom](../calibration.md#schritt-3--volumenstrom) senken |
| Schwaches Leuchten | Wandzahl und Füllung, nicht die Temperatur |

---

[← SUNLU PLA](sunlu-pla.md) · [Materialübersicht](README.md) · [SUNLU PETG →](sunlu-petg.md)
