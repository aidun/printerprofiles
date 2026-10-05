# eSUN PETG

[← Materialübersicht](README.md) · Status: 🔵 Startwert · Basis: `Generic PETG`

Standard-PETG von eSUN. Verhält sich im Druck sehr ähnlich wie
[SUNLU PETG](sunlu-petg.md), ist in der Schmelze aber etwas dünnflüssiger und läuft
deshalb bereits bei geringfügig niedrigerer Düsentemperatur sauber. Dafür haftet es
am Bett schwächer und bekommt eine um 5 °C höhere Betttemperatur.

---

## Kennwerte

| Größe | Wert | Abweichung zu SUNLU PETG |
|---|---|---|
| Düse | **243 °C** (erste Schicht 248 °C) | −2 °C |
| Temperaturfenster | 230 – 255 °C | oben enger |
| Bett | **75 °C** (erste Schicht 80 °C) | +5 °C |
| Glasübergang | 71 °C | gleich |
| Flussrate | 0.95 | −0.01 |
| Lüfter | **20 – 50 %** | gleich |
| Überhangkühlung | 60 % | gleich |
| Z-Hop | 0.6 mm | gleich |
| Abrasiv | nein | |
| Trocknung | **65 °C / 8 h** | gleich |
| Lagerung | zwingend trocken | kritisch |

**Zum engeren oberen Fenster:** Oberhalb von 255 °C beginnt dieses Material sichtbar
zu fädeln. Die Obergrenze ist deshalb 5 °C niedriger gesetzt als bei SUNLU PETG —
Temperatur ist hier nicht das Mittel gegen Unterextrusion, der Volumenstrom ist es.

## Volumenstrom je Drucker und Düse

Werte in mm³/s. Basis ist der X1C; die übrigen Drucker werden über den
[Durchsatzfaktor](../drucker/README.md#durchsatzfaktoren) skaliert.

| Drucker | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| H2C | 1.4 | 14.9 | 20.1 |
| X1 Carbon | 1.2 | 13 | 17.5 |
| P1S | 1.1 | 12.3 | 16.6 |
| P1P | 1.1 | 12.3 | 16.6 |
| A1 | 1.1 | 11.7 | 15.8 |
| A1 mini | 1 | 11 | 14.9 |

## Was gegenüber SUNLU PETG anders zu beachten ist

**1 · Betthaftung.** 75 °C statt 70 °C sind kein Komfortwert. Bei 70 °C lösen sich
größere Teile dieses Materials an den Ecken. Dafür ist der Ausriss beim Ablösen
weniger heftig — die glatte PEI-Platte ist hier unkritischer als bei SUNLU PETG.

**2 · Kühlung bleibt der Feind der Festigkeit.** Wie bei jedem PETG: 20 – 50 %
Lüfterleistung sind die Obergrenze. Überhänge über etwa 50° gehören auf
Stützmaterial, nicht auf mehr Lüfter.

**3 · Feuchtigkeit.** Unverändert kritisch. Details in
[Fehlerbilder → Feuchtigkeit](../troubleshooting.md#feuchtigkeit).

## Wenn etwas nicht stimmt

| Symptom | Zuerst prüfen |
|---|---|
| Ecken heben ab | Bett auf 80 °C, [Warping](../troubleshooting.md#warping) |
| Knacken, Blasen, matte Oberfläche | [Feuchtigkeit](../troubleshooting.md#feuchtigkeit) — trocknen |
| Fäden | Temperatur senken, nicht erhöhen |
| Teil bricht entlang der Schichten | Kühlung senken |
| Unterextrusion | [Volumenstrom](../calibration.md#schritt-3--volumenstrom) |

---

[← eSUN PLA+ Glow](esun-pla-plus-glow.md) · [Materialübersicht](README.md) · [eSUN PETG Transparent →](esun-petg-transparent.md)
