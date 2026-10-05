# eSUN PETG Transparent

[← Materialübersicht](README.md) · Status: 🔵 Startwert · Basis: `Generic PETG`
· 💧 **auf Klarheit optimiert**

Klarsichtiges PETG von eSUN. Optisch auf demselben Niveau wie
[SUNLU PETG Transparent](sunlu-petg-transparent.md), im Druck etwas gutmütiger, weil
die Schmelze dünnflüssiger ist und Grenzflächen leichter von selbst verschwinden.
Der Preis dafür ist eine höhere Neigung zur Fädenbildung bei den hohen Temperaturen,
die Klarheit verlangt.

---

## Was „auf Klarheit optimiert" bedeutet

> 💧 Gegenüber dem opaken [eSUN PETG](esun-petg.md): **Düse 7 °C heißer**,
> **Volumenstrom rund 15 % niedriger**, **Lüfter von 20 – 50 % auf 10 – 25 %
> zurückgenommen**, Verzögerungsschwelle erhöht und die ersten drei Schichten ohne
> Lüfter.
>
> Ziel ist in allen Punkten dasselbe: Die Bahn soll länger flüssig bleiben und mit
> ihrer Nachbarin verschmelzen, statt sich nur anzulegen. Jede sichtbare Grenzfläche
> im Teil ist eine Bahn, die zu früh erstarrt ist.

---

## Kennwerte

| Größe | Wert | Abweichung zu eSUN PETG |
|---|---|---|
| Düse | **250 °C** (erste Schicht 255 °C) | +7 °C |
| Temperaturfenster | 240 – 260 °C | höher |
| Bett | **75 °C** (erste Schicht 80 °C) | gleich |
| Glasübergang | 71 °C | gleich |
| Flussrate | 0.95 | gleich |
| Lüfter | **10 – 25 %** | halbiert |
| Überhangkühlung | 40 % | reduziert |
| Verzögerung ab | 8 s Schichtzeit | +2 s |
| Lüfter aus für | 3 Schichten | +1 |
| Z-Hop | 0.6 mm | gleich |
| Trocknung | **65 °C / 8 h** | zwingend |

## Volumenstrom je Drucker und Düse

| Drucker | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| H2C | 1.1 | 12.6 | 17.1 |
| X1 Carbon | 1 | 11 | 14.9 |
| P1S | 0.9 | 10.4 | 14.2 |
| P1P | 0.9 | 10.4 | 14.2 |
| A1 | 0.9 | 9.9 | 13.4 |
| A1 mini | 0.8 | 9.3 | 12.7 |

## So wird das Teil wirklich klar

**1 · Trocknen ist nicht optional.** Jede Dampfblase bleibt als weißer Punkt sichtbar
und lässt sich nachträglich nicht entfernen.

**2 · Massiv drucken.** Füllung 100 %, Füllmuster `concentric`, hohe Schichthöhe.
Eine 0.6-mm-Düse mit 0.3 mm Schichthöhe liefert klarere Teile als eine 0.2-mm-Düse
mit 0.1 mm: weniger Grenzflächen, weniger Streuung.

**3 · Die Fädenbildung im Blick behalten.** 250 °C liegen nahe an der Grenze, ab der
dieses Material zieht. Wer Fäden sieht, senkt zuerst die Rückzugsgeschwindigkeit und
erst danach die Temperatur — jedes Grad weniger kostet hier Klarheit.

**4 · Nachbehandlung.** Klarlack oder Epoxid glätten die Oberflächenriefen und
bringen optisch mehr als jede weitere Parameteränderung.

## Wenn etwas nicht stimmt

| Symptom | Zuerst prüfen |
|---|---|
| Weiße Punkte im Material | [Feuchtigkeit](../troubleshooting.md#feuchtigkeit) — trocknen, keine Ausnahme |
| Teil bleibt trüb | Füllung 100 %, Schichthöhe erhöhen, Lüfter weiter senken |
| Starke Fädenbildung | Rückzug prüfen, danach [Fädenbildung](../troubleshooting.md#fädenbildung) |
| Sichtbare Gitterstruktur innen | Füllung auf 100 %, Muster auf `concentric` |
| Unterextrusion | [Volumenstrom](../calibration.md#schritt-3--volumenstrom) |

---

[← eSUN PETG](esun-petg.md) · [Materialübersicht](README.md) · [eSUN PETG-CF →](esun-petg-cf.md)
