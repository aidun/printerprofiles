# SUNLU PLA Transparent

[← Materialübersicht](README.md) · Status: 🔵 Startwert · Basis: `Generic PLA`
· 💧 **auf Klarheit optimiert**

Klarsichtiges PLA. Chemisch dasselbe Polymer wie das Standardmaterial, gedruckt wird
es aber nach anderen Regeln: Klarheit entsteht nicht im Filament, sondern in der
Schmelze. Jede Grenzfläche zwischen zwei Bahnen, die nicht vollständig verschmolzen
ist, streut Licht und macht das Teil milchig.

---

## Was „auf Klarheit optimiert" bedeutet

> 💧 Die Profile dieses Materials weichen bewusst vom Standard-PLA ab:
> **Düse rund 8 °C heißer**, **Volumenstrom etwa 15 % niedriger**,
> **Lüfter halbiert**. Alle drei Änderungen verfolgen dasselbe Ziel — die Bahn soll
> länger flüssig bleiben, damit sie mit der Nachbarbahn verschmilzt statt sich nur
> anzulegen.
>
> Das kostet Druckzeit und etwas Überhangqualität. Wer ein transparentes Teil
> schnell drucken will, bekommt ein trübes Teil.

---

## Kennwerte

| Größe | Wert | Abweichung zu PLA |
|---|---|---|
| Düse | **223 °C** (erste Schicht 228 °C) | +8 °C |
| Temperaturfenster | 205 – 240 °C | höher und breiter |
| Bett | **55 °C** (erste Schicht 60 °C) | gleich |
| Glasübergang | 55 °C | gleich |
| Flussrate | 0.98 | gleich |
| Lüfter | **30 – 60 %** | halbiert |
| Überhangkühlung | 80 % | reduziert |
| Z-Hop | 0.4 mm | gleich |
| Lüfter aus für | 2 Schichten | +1 |
| Abrasiv | nein | |
| Trocknung | 45 °C / 6 h | gleich |

Feuchtes Filament kostet bei diesem Material doppelt: Dampfblasen sind im
transparenten Teil einzeln sichtbar.

## Volumenstrom je Drucker und Düse

Werte in mm³/s. Basis ist der X1C; die übrigen Drucker werden über den
[Durchsatzfaktor](../drucker/README.md#durchsatzfaktoren) skaliert.

| Drucker | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| H2C | 1.6 | 14.7 | 20.6 |
| X1 Carbon | 1.4 | 12.8 | 17.9 |
| P1S | 1.3 | 12.2 | 17 |
| P1P | 1.3 | 12.2 | 17 |
| A1 | 1.3 | 11.5 | 16.1 |
| A1 mini | 1.2 | 10.9 | 15.2 |

## So wird das Teil wirklich klar

**1 · Schichthöhe hoch, Wandzahl niedrig.** Klarheit entsteht durch wenige, dicke,
vollständig verschmolzene Bahnen. Die Stufe *Schnell* liefert hier optisch oft
bessere Ergebnisse als *Qualität* — der einzige Fall im Repository, in dem das so
ist. Für massive Klarsichtteile: 0.6-mm-Düse, hohe Schichthöhe, Füllung 100 %.

**2 · Füllung 100 % oder 0 %.** Alles dazwischen erzeugt sichtbare Gitterstrukturen
im Inneren. Entweder vollmassiv oder bewusst als Hohlkörper mit Lichtbrechung.

**3 · Füllmuster ausrichten.** Bei massiven Teilen `concentric` oder
`aligned rectilinear` wählen — gleichgerichtete Bahnen brechen das Licht
gleichmäßig, kreuzende Muster erzeugen einen Schleier.

**4 · Glatte Platte verwenden.** Die texturierte Platte prägt ihre Struktur in die
erste Schicht und macht die Unterseite dauerhaft matt.

## Wenn etwas nicht stimmt

| Symptom | Zuerst prüfen |
|---|---|
| Teil bleibt milchig | Schichthöhe erhöhen, Lüfter weiter senken, Füllung auf 100 % |
| Einzelne Blasen im Material | [Feuchtigkeit](../troubleshooting.md#feuchtigkeit) — trocknen |
| Sichtbare Gitterstruktur innen | Füllung auf 100 %, Muster auf `concentric` |
| Überhänge hängen durch | Stützmaterial statt mehr Lüfter |
| Maße stimmen nicht | [Flussrate](../calibration.md#schritt-2--flussrate) |

---

[← SUNLU PLA Glow](sunlu-pla-glow.md) · [Materialübersicht](README.md) · [SUNLU PETG →](sunlu-petg.md)
