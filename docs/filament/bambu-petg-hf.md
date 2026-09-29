# Bambu PETG HF

[← Materialübersicht](README.md) · Status: 🔵 Startwert · Basis: `Bambu PETG HF`

Das High-Flow-PETG von Bambu Lab und das schnellste technische Material im
Repository. Chemisch ein regulärer PETG-Copolyester, rheologisch aber auf hohen
Durchsatz eingestellt: **21 mm³/s auf dem X1C** — derselbe Wert wie
[Bambu PLA Basic](bambu-pla-basic.md) und rund 55 % über gewöhnlichem PETG.

---

## Kennwerte

| Größe | Wert | Abweichung zu SUNLU PETG |
|---|---|---|
| Düse | **245 °C** (erste Schicht 250 °C) | gleich |
| Temperaturfenster | 230 – 260 °C | gleich |
| Bett | **70 °C** (erste Schicht 75 °C) | gleich |
| Glasübergang | 70 °C | −1 °C |
| Flussrate | 0.97 | +0.01 |
| Lüfter | **20 – 40 %** | oben reduziert |
| Überhangkühlung | **100 %** | deutlich höher |
| Verzögerung ab | 10 s Schichtzeit | +4 s |
| Lüfter aus für | 3 Schichten | +1 |
| Z-Hop | 0.6 mm | gleich |
| Abrasiv | nein | |
| Trocknung | **65 °C / 8 h** | gleich |
| Lagerung | zwingend trocken | kritisch |

**Zur Kühlkurve:** Die Kombination aus zurückgenommener Grundkühlung und voller
Überhangkühlung stammt aus Bambus Profil und ist der Grund, warum dieses PETG
Überhänge sauberer legt als die Alternativen, ohne Schichthaftung zu verlieren. Der
Lüfter läuft nur dort voll, wo keine darunterliegende Schicht zu verschweißen ist.

## Volumenstrom je Drucker und Düse

Werte in mm³/s. Basis ist der X1C; die übrigen Drucker werden über den
[Durchsatzfaktor](../drucker/README.md#durchsatzfaktoren) skaliert.

| Drucker | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| H2C | 1.1 | 24.1 | 28.7 |
| X1 Carbon | 1.0 | 21.0 | 25.0 |
| P1S | 0.9 | 19.9 | 23.8 |
| A1 | 0.9 | 18.9 | 22.5 |
| A1 mini | 0.8 | 17.8 | 21.2 |

**Zum auffälligen Sprung bei 0.2 mm:** Der Wert stammt unverändert aus Bambus
Datenblatt. Die High-Flow-Auslegung wirkt sich erst ab 0.4 mm aus; durch eine
0.2-mm-Bohrung lässt sich die Schmelze nicht schneller pressen als bei jedem anderen
PETG. Für feine Teile bringt dieses Material also keinen Zeitvorteil — sein Nutzen
liegt bei 0.4 und 0.6 mm.

## Hinweise

- **Schnellstes technisches Material.** Für große, belastbare Teile die erste Wahl:
  PETG-Festigkeit bei PLA-Druckzeit.
- **Alle PETG-Regeln gelten weiter.** Feuchtigkeit, Fädenbildung und die
  Empfindlichkeit gegen zu starke Kühlung ändern sich durch die High-Flow-Auslegung
  nicht.
- **Haftung auf glatter PEI-Platte.** Wie jedes PETG kann es beim Ablösen
  Beschichtung mitnehmen — bei wiederholtem Ausriss auf die texturierte Platte
  wechseln.
- **AMS-tauglich** ohne Einschränkung.

## Wenn etwas nicht stimmt

| Symptom | Zuerst prüfen |
|---|---|
| Unterextrusion bei hohem Tempo | [Volumenstrom](../calibration.md#schritt-3--volumenstrom) — Hotend am Limit |
| Knacken, Blasen, matte Oberfläche | [Feuchtigkeit](../troubleshooting.md#feuchtigkeit) — trocknen |
| Fäden | [Fädenbildung](../troubleshooting.md#fädenbildung) |
| Teil bricht entlang der Schichten | Kühlung senken, nicht Temperatur erhöhen |
| Platte nimmt Schaden beim Ablösen | texturierte Platte verwenden |

---

[← Bambu PLA Translucent](bambu-pla-translucent.md) · [Materialübersicht](README.md) · [Bambu PETG Translucent →](bambu-petg-translucent.md)
