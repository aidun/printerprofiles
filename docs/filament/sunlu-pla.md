# SUNLU PLA

[← Materialübersicht](README.md) · Status: 🔵 Startwert · Basis: `Generic PLA`

Standard-PLA von SUNLU. Gut fließfähig, gutmütig, verträgt hohe Volumenströme und
aggressive Kühlung. Das unkritischste Material im Repository und der richtige
Einstieg, wenn ein Drucker oder eine Düse neu ist.

---

## Kennwerte

| Größe | Wert | Quelle |
|---|---|---|
| Düse | **215 °C** (erste Schicht 220 °C) | Startwert |
| Temperaturfenster | 195 – 235 °C | Startwert |
| Bett | **55 °C** (erste Schicht 60 °C) | Startwert |
| Glasübergang | 55 °C | Materialklasse |
| Flussrate | 0.98 | Startwert |
| Lüfter | 60 – 100 % | Startwert |
| Überhangkühlung | 100 % | Startwert |
| Z-Hop | 0.4 mm | Startwert |
| Abrasiv | nein — Messingdüse genügt | |
| Trocknung | 45 °C / 6 h | |
| Lagerung | trocken mit Silikagel, unkritisch | |

## Volumenstrom je Drucker und Düse

Werte in mm³/s. Basis ist der X1C; die übrigen Drucker werden über den
[Durchsatzfaktor](../drucker/README.md#durchsatzfaktoren) skaliert.

| Drucker | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| H2C | 4.0 | 17.2 | 24.1 |
| X1 Carbon | 3.5 | 15.0 | 21.0 |
| P1S | 3.3 | 14.2 | 19.9 |
| A1 | 3.1 | 13.5 | 18.9 |
| A1 mini | 3.0 | 12.8 | 17.8 |

## Hinweise

- **Alle drei Düsen freigegeben.** PLA ist nicht abrasiv und fein genug für 0.2 mm.
- **Kühlung darf voll laufen.** Anders als bei PETG verbessert starke Kühlung hier
  Überhänge und Detailtreue, ohne die Schichthaftung nennenswert zu kosten.
- **Wärmeempfindlich.** Der Glasübergang liegt bei 55 °C. Teile im Auto oder in
  direkter Sonne verformen sich — dafür PETG verwenden.
- **Betthaftung** ist selten ein Problem. Bleibt sie aus, liegt es fast immer an
  Fett auf der Platte, nicht an der Temperatur.

## Wenn etwas nicht stimmt

| Symptom | Zuerst prüfen |
|---|---|
| Unterextrusion, gerippte Oberfläche | [Volumenstrom](../calibration.md#schritt-3--volumenstrom) |
| Maße stimmen nicht | [Flussrate](../calibration.md#schritt-2--flussrate) |
| Fäden | [Fädenbildung](../troubleshooting.md#fädenbildung) |
| Teil bricht entlang der Schichten | [Schichthaftung](../troubleshooting.md#schichthaftung) |

---

[Materialübersicht](README.md) · [SUNLU PLA Glow →](sunlu-pla-glow.md)
