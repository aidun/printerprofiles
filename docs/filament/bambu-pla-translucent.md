# Bambu PLA Translucent

[← Materialübersicht](README.md) · Status: 🔵 Startwert · Basis: `Bambu PLA Translucent`
· 💧 **auf Klarheit optimiert**

Durchscheinendes PLA von Bambu Lab. Der Name ist Programm: *translucent*, nicht
*transparent* — das Material streut Licht bewusst und wirkt milchig-durchscheinend
statt glasklar. Für Lampenschirme, Diffusoren und Lichtleiter ist das genau die
gewünschte Eigenschaft.

---

## Was „auf Klarheit optimiert" bedeutet

> 💧 Dieses Repository weicht bei diesem Material **bewusst von Bambus eigenem Profil
> ab**. Bambu fährt den Lüfter wie bei PLA Basic auf 100 %; hier steht er auf
> **40 – 70 %**, die Düse liegt **8 °C höher** und der Volumenstrom **43 % niedriger**.
>
> Grund: Bambus Profil ist auf Druckzeit und Überhangqualität ausgelegt. Wer ein
> durchscheinendes Teil druckt, will das Gegenteil — langsam erstarrende Bahnen, die
> ineinanderlaufen. Wer die Herstellerwerte bevorzugt, wählt in Bambu Studio einfach
> das Originalprofil.

---

## Kennwerte

| Größe | Wert | Abweichung zu PLA Basic |
|---|---|---|
| Düse | **228 °C** (erste Schicht 232 °C) | +8 °C |
| Temperaturfenster | 215 – 235 °C | höher |
| Bett | **55 °C** (erste Schicht 60 °C) | gleich |
| Glasübergang | 45 °C | gleich |
| Flussrate | 0.98 | gleich |
| Lüfter | **40 – 70 %** | stark reduziert |
| Überhangkühlung | 90 % | leicht reduziert |
| Verzögerung ab | 8 s Schichtzeit | +4 s |
| Lüfter aus für | 2 Schichten | +1 |
| Z-Hop | 0.4 mm | gleich |
| Trocknung | 45 °C / 6 h | gleich |

## Volumenstrom je Drucker und Düse

| Drucker | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| H2C | 1.8 | 13.8 | 16.1 |
| X1 Carbon | 1.6 | 12 | 14 |
| P1S | 1.5 | 11.4 | 13.3 |
| P1P | 1.5 | 11.4 | 13.3 |
| A1 | 1.4 | 10.8 | 12.6 |
| A1 mini | 1.4 | 10.2 | 11.9 |

## Wofür sich dieses Material eignet

**Lampenschirme und Diffusoren.** Die Streuung, die bei
[SUNLU PLA Transparent](sunlu-pla-transparent.md) ein Mangel wäre, ist hier der
Zweck: Eine einzelne LED hinter einer 1.2 mm starken Wand erscheint als gleichmäßig
leuchtende Fläche ohne sichtbaren Punkt.

**Wandstärke ist der wichtigste Parameter.** Zwei Wandlinien bei 0.4 mm ergeben rund
0.8 mm — sichtbar hell, aber mit erkennbarer Lichtquelle. Ab drei Linien wird die
Streuung gleichmäßig. Füllung 0 %, sonst zeichnet sich das Muster im Licht ab.

**Nicht für glasklare Teile.** Wer echte Transparenz braucht, nimmt
[SUNLU PETG Transparent](sunlu-petg-transparent.md) oder
[eSUN PETG Transparent](esun-petg-transparent.md) — PETG ist amorph und erreicht
Klarheit, die PLA prinzipbedingt nicht liefert.

## Wenn etwas nicht stimmt

| Symptom | Zuerst prüfen |
|---|---|
| Lichtquelle zeichnet sich als Punkt ab | Wandzahl erhöhen, Füllung auf 0 % |
| Füllmuster im Gegenlicht sichtbar | Füllung auf 0 % setzen |
| Teil wirkt fleckig-ungleichmäßig | Kühlung weiter senken, Schichthöhe erhöhen |
| Blasen im Material | [Feuchtigkeit](../troubleshooting.md#feuchtigkeit) — trocknen |

---

[← Bambu PLA Glow](bambu-pla-glow.md) · [Materialübersicht](README.md) · [Bambu PETG HF →](bambu-petg-hf.md)
