# SUNLU PETG Matte

[← Materialübersicht](README.md) · Status: 🔵 Startwert · Basis: `Generic PETG`

PETG mit matter Oberfläche. Die Mattierung verdeckt Schichtlinien und Glanzunterschiede,
die bei normalem PETG gern sichtbar werden. Temperaturen und Kühlung entsprechen
[SUNLU PETG](sunlu-petg.md), beim Durchsatz bleibt das Profil vorsichtiger.

---

## Kennwerte

| Größe | Wert | Abweichung zu PLA |
|---|---|---|
| Düse | **245 °C** (erste Schicht 250 °C) | +30 °C |
| Temperaturfenster | 230 – 260 °C | deutlich höher |
| Bett | **70 °C** (erste Schicht 75 °C) | +15 °C |
| Glasübergang | 71 °C | +16 °C |
| Flussrate | 0.95 | −0.03 |
| Lüfter | **30 – 40 %** | stark reduziert, schmales Fenster |
| Überhangkühlung | 60 % | reduziert |
| Z-Hop | **0.6 mm** | +0.2 mm |
| Abrasiv | nein | |
| Trocknung | **65 °C / 8 h** | wärmer und länger |
| Lagerung | zwingend trocken | kritisch |

## Volumenstrom je Drucker und Düse

| Drucker | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| H2C | 1 | 13.8 | 15.5 |
| H3C | 1 | 13.8 | 15.5 |
| X2D | 0.9 | 12 | 13.5 |
| X1 Carbon | 0.9 | 12 | 13.5 |
| P1S | 0.9 | 11.4 | 12.8 |
| P1P | 0.9 | 11.4 | 12.8 |
| A1 | 0.8 | 10.8 | 12.2 |
| A1 mini | 0.8 | 10.2 | 11.5 |

> **Quelle der Werte.** Bambu Studio bringt für mattes PETG kein eigenes Profil mit. Die
> Mattierung entsteht durch Füllstoffe, und die bremsen den Schmelzfluss. Der
> Volumenstrom liegt deshalb rund 15 % unter dem von [SUNLU PETG](sunlu-petg.md) —
> hergeleitet, nicht gemessen. Bei Unterextrusion an schnellen Stellen zuerst hier
> ansetzen, siehe [Kalibrierung](../calibration.md#schritt-3--volumenstrom).

> **Abrasiv?** Matte Füllstoffe sind deutlich weicher als Glow-Pigment oder Kohlefaser.
> Eine Messingdüse genügt, verschleißt bei viel Matte-Material aber schneller.

## Die drei Eigenheiten

**1 · Kühlung ist der Feind der Festigkeit.** PETG verschweißt seine Schichten
langsamer als PLA. Die Profile fahren deshalb nur 30 – 40 % Lüfterleistung. Wer die
Kühlung hochdreht, bekommt schönere Überhänge und Teile, die in der Hand brechen.
Überhänge über etwa 50° gehören bei PETG auf Stützmaterial, nicht auf mehr Lüfter.

**2 · Feuchtigkeit ist sofort sichtbar.** PETG zieht innerhalb weniger Tage offener
Lagerung genug Wasser, um hörbar zu knacken und Blasen im Strang zu bilden. Ein
Trockenbehälter mit Silikagel ist hier Voraussetzung, keine Empfehlung. Details in
[Fehlerbilder → Feuchtigkeit](../troubleshooting.md#feuchtigkeit).

**3 · Die Haftung kann zu gut sein.** Auf glatten PEI-Platten verbindet sich PETG so
fest, dass es beim Ablösen Beschichtung mitnimmt. Die erste Schicht ist deshalb auf
75 °C gesetzt und nicht höher. Bei wiederholtem Ausriss auf die texturierte Platte
wechseln.

## Wenn etwas nicht stimmt

| Symptom | Zuerst prüfen |
|---|---|
| Knacken, Blasen, matte Oberfläche | [Feuchtigkeit](../troubleshooting.md#feuchtigkeit) — trocknen |
| Fäden | [Fädenbildung](../troubleshooting.md#fädenbildung) — Temperatur zuerst |
| Teil bricht entlang der Schichten | Kühlung senken, nicht Temperatur erhöhen |
| Platte nimmt Schaden beim Ablösen | texturierte Platte verwenden |
| Ecken heben ab | [Warping](../troubleshooting.md#warping) |

---

[← SUNLU PETG 2.0](sunlu-petg-2.md) · [Materialübersicht](README.md) · [SUNLU TPU →](sunlu-tpu.md)
