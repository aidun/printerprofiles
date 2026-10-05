# SUNLU PETG Transparent

[← Materialübersicht](README.md) · Status: 🔵 Startwert · Basis: `Generic PETG`
· 💧 **auf Klarheit optimiert**

Das klarste Material im Repository. PETG ist von Haus aus amorph und damit optisch
im Vorteil gegenüber PLA — bei sauberer Prozessführung erreicht es eine Transparenz,
die an Gussteile heranreicht. Gleichzeitig bleiben alle PETG-Eigenheiten bestehen:
Feuchtigkeit, Fädenbildung und die Empfindlichkeit gegen Kühlung.

---

## Was „auf Klarheit optimiert" bedeutet

> 💧 Gegenüber dem Standard-PETG: **Düse 7 °C heißer**, **Volumenstrom rund 15 %
> niedriger**, **Lüfter von 20 – 50 % auf 10 – 25 % zurückgenommen** und die
> Verzögerungsschwelle erhöht, damit kleine Schichten mehr Zeit zum Abfließen haben.
>
> PETG verzeiht diese Einstellung besser als PLA: Weniger Kühlung verbessert bei
> PETG ohnehin die Schichthaftung. Transparenz und Festigkeit ziehen hier
> ausnahmsweise in dieselbe Richtung.

---

## Kennwerte

| Größe | Wert | Abweichung zu PETG |
|---|---|---|
| Düse | **252 °C** (erste Schicht 255 °C) | +7 °C |
| Temperaturfenster | 240 – 262 °C | höher |
| Bett | **70 °C** (erste Schicht 75 °C) | gleich |
| Glasübergang | 71 °C | gleich |
| Flussrate | 0.95 | gleich |
| Lüfter | **10 – 25 %** | halbiert |
| Überhangkühlung | 40 % | reduziert |
| Verzögerung ab | 8 s Schichtzeit | +2 s |
| Lüfter aus für | 3 Schichten | +1 |
| Z-Hop | 0.6 mm | gleich |
| Trocknung | **65 °C / 8 h** | zwingend |
| Lagerung | zwingend trocken | kritisch |

## Volumenstrom je Drucker und Düse

| Drucker | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| H2C | 1.1 | 13.7 | 15.6 |
| X1 Carbon | 1 | 11.9 | 13.6 |
| P1S | 0.9 | 11.3 | 12.9 |
| P1P | 0.9 | 11.3 | 12.9 |
| A1 | 0.9 | 10.7 | 12.2 |
| A1 mini | 0.8 | 10.1 | 11.6 |

Die 0.2-mm-Werte liegen bewusst im Bereich von rund 1 mm³/s. Das entspricht der
Freigabe der Herstellerprofile für diese Düse und ist keine Vorsichtsmarge.

> **Quelle der Werte.** Die Klarheitsreserve rechnet auf den SUNLU-eigenen Profilen
> von [SUNLU PETG](sunlu-petg.md) auf: 85 % von 14.0 / 16.0 mm³/s ergeben die
> 11.9 / 13.6 mm³/s dieser Tabelle. Die 0.2-mm-Düse bleibt bei 1.0 — 85 % davon
> würden auf der A1 mini unter die Plausibilitätsgrenze von 0.8 mm³/s fallen, die
> `tools/validate.py` zieht.

## So wird das Teil wirklich klar

**1 · Trocknen ist nicht optional.** Bei opakem PETG kostet Feuchtigkeit Festigkeit,
bei transparentem kostet sie die Optik komplett: Jede Dampfblase bleibt als weißer
Punkt im Material sichtbar und lässt sich nachträglich nicht entfernen.

**2 · Massiv drucken.** Füllung 100 %, Füllmuster `concentric`, Schichthöhe hoch.
Eine 0.6-mm-Düse mit 0.3 mm Schichthöhe liefert klarere Teile als eine 0.2-mm-Düse
mit 0.1 mm — weniger Grenzflächen bedeuten weniger Streuung.

**3 · Langsam ist Selbstzweck.** Der abgesenkte Volumenstrom ist der eigentliche
Wirkmechanismus dieser Profile. Wer ihn wieder anhebt, bekommt trübe Teile bei
identischer Temperatur.

**4 · Nachbehandlung.** Ein kurzer Überzug mit Klarlack oder Epoxid glättet die
Oberflächenriefen und bringt optisch mehr als jede weitere Parameteränderung.

## Wenn etwas nicht stimmt

| Symptom | Zuerst prüfen |
|---|---|
| Weiße Punkte im Material | [Feuchtigkeit](../troubleshooting.md#feuchtigkeit) — trocknen, keine Ausnahme |
| Teil bleibt trüb | Füllung 100 %, Schichthöhe erhöhen, Lüfter weiter senken |
| Starke Fädenbildung | [Fädenbildung](../troubleshooting.md#fädenbildung) — Temperatur an die Untergrenze |
| Oberfläche glänzt fleckig | Kühlung ungleichmäßig — Bauteillüfter prüfen |
| Unterextrusion | [Volumenstrom](../calibration.md#schritt-3--volumenstrom) |

---

[← SUNLU PETG Glow](sunlu-petg-glow.md) · [Materialübersicht](README.md) · [SUNLU TPU →](sunlu-tpu.md)
