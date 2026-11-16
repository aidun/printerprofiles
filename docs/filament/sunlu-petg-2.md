# SUNLU PETG 2.0

[← Materialübersicht](README.md) · Status: 🔵 Startwert · Basis: `Generic PETG`

Die zweite Generation von SUNLU PETG. Einsatz und Eigenheiten sind dieselben wie bei
[SUNLU PETG](sunlu-petg.md): zäh, wärmefester als PLA, empfindlich gegen zu viel Kühlung
und Feuchtigkeit.

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
| H2C | 1.1 | 16.1 | 18.4 |
| H3C | 1.1 | 16.1 | 18.4 |
| X2D | 1 | 14 | 16 |
| X1 Carbon | 1 | 14 | 16 |
| P1S | 0.9 | 13.3 | 15.2 |
| P1P | 0.9 | 13.3 | 15.2 |
| A1 | 0.9 | 12.6 | 14.4 |
| A1 mini | 0.8 | 11.9 | 13.6 |

> **Quelle der Werte.** Bambu Studio bringt für PETG 2.0 kein eigenes Profil mit. Bis ein
> Messwert vorliegt, gelten die Werte von [SUNLU PETG](sunlu-petg.md) — dort steht ihre
> Herkunft aus den SUNLU-Profilen der Bambu-Bibliothek. Wer am eigenen Gerät mehr
> Durchsatz misst, trägt ihn über die [Kalibrierung](../calibration.md#schritt-3--volumenstrom) nach.

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

[← SUNLU PETG Transparent](sunlu-petg-transparent.md) · [Materialübersicht](README.md) · [SUNLU PETG Matte →](sunlu-petg-matte.md)
