# SUNLU PETG

[← Materialübersicht](README.md) · Status: 🔵 Startwert · Basis: `Generic PETG`

Zähes, temperaturbeständiges PETG. Die richtige Wahl überall dort, wo PLA zu spröde
oder zu wärmeempfindlich ist — Gehäuse, Halterungen, alles, was im Auto oder in der
Sonne liegt. Im Gegenzug ist PETG anspruchsvoller: es fädelt, zieht Wasser und
verliert bei zu starker Kühlung die Schichthaftung.

---

## Kennwerte

| Größe | Wert | Abweichung zu PLA |
|---|---|---|
| Düse | **245 °C** (erste Schicht 250 °C) | +30 °C |
| Temperaturfenster | 230 – 260 °C | deutlich höher |
| Bett | **70 °C** (erste Schicht 75 °C) | +15 °C |
| Glasübergang | 71 °C | +16 °C |
| Flussrate | 0.95 | −0.03 |
| Lüfter | **20 – 50 %** | stark reduziert |
| Überhangkühlung | 60 % | reduziert |
| Z-Hop | **0.6 mm** | +0.2 mm |
| Abrasiv | nein | |
| Trocknung | **65 °C / 8 h** | wärmer und länger |
| Lagerung | zwingend trocken | kritisch |

## Volumenstrom je Drucker und Düse

| Drucker | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| H2C | 1.1 | 16.1 | 18.4 |
| X1 Carbon | 1 | 14 | 16 |
| P1S | 0.9 | 13.3 | 15.2 |
| P1P | 0.9 | 13.3 | 15.2 |
| A1 | 0.9 | 12.6 | 14.4 |
| A1 mini | 0.8 | 11.9 | 13.6 |

> **Quelle der Werte.** Volumenstrom und Flussrate stammen aus den SUNLU-eigenen
> Profilen der Bambu-Bibliothek: `SUNLU PETG @BBL X1C 0.2 nozzle` gibt 1.0 mm³/s frei,
> `SUNLU PETG @BBL X1C` — das Profil der 0.4-mm-Düse — 14.0 mm³/s, beide bei
> Flussrate 0.95. Für 0.6 mm liefert SUNLU kein Profil; die 16.0 sind der Wert des
> 0.8-mm-Profils. Das ersetzt die früher hier geführten hergeleiteten Werte.

> **Zur 0.2-mm-Spalte.** Rund 1.0 mm³/s statt der linear erwarteten 3 mm³/s. Die
> Herstellerprofile geben für diese Düse nicht mehr frei — begrenzend ist der
> Druckvorschub im Schmelzkanal, nicht die Heizleistung.

> **Warum 0.4 und 0.6 mm so nah beieinanderliegen.** SUNLUs Kurve läuft ab 0.4 mm
> flach: Von 14.0 auf 16.0 mm³/s sind es nur 14 % mehr, und das erst bei 0.8 mm —
> der vierfachen Querschnittsfläche. Die Grenze ist die Aufschmelzleistung des
> Hotends, nicht die Düsenbohrung.

## Die drei Eigenheiten

**1 · Kühlung ist der Feind der Festigkeit.** PETG verschweißt seine Schichten
langsamer als PLA. Die Profile fahren deshalb nur 20 – 50 % Lüfterleistung. Wer die
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

[← SUNLU PLA Transparent](sunlu-pla-transparent.md) · [Materialübersicht](README.md) · [SUNLU PETG Glow →](sunlu-petg-glow.md)
