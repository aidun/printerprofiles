# Materialien

[← Zurück zur Übersicht](../../README.md)

17 Materialien von drei Herstellern, jeweils als eigenes Datenblatt mit Kennwerten,
Volumenströmen je Drucker und den materialtypischen Fallstricken. Vier
Materialklassen: PLA, PETG, TPU und ABS.

| Material | Düsen | Besonderheit | Status | Datenblatt |
|---|---|---|---|---|
| **SUNLU PLA** | 0.2 · 0.4 · 0.6 | | 🔵 Startwert | [öffnen](sunlu-pla.md) |
| **SUNLU PLA Glow** | 0.4 · 0.6 | ⚠️ abrasiv | 🔵 Startwert | [öffnen](sunlu-pla-glow.md) |
| **SUNLU PLA Transparent** | 0.2 · 0.4 · 0.6 | 💧 klar | 🔵 Startwert | [öffnen](sunlu-pla-transparent.md) |
| **SUNLU PETG** | 0.2 · 0.4 · 0.6 | | 🔵 Startwert | [öffnen](sunlu-petg.md) |
| **SUNLU PETG Glow** | 0.4 · 0.6 | ⚠️ abrasiv | 🟢 H2C · 0.4 mm verifiziert | [öffnen](sunlu-petg-glow.md) |
| **SUNLU PETG Transparent** | 0.2 · 0.4 · 0.6 | 💧 klar | 🔵 Startwert | [öffnen](sunlu-petg-transparent.md) |
| **SUNLU TPU** | 0.4 · 0.6 | 🧵 flexibel | 🔵 Startwert | [öffnen](sunlu-tpu.md) |
| **eSUN PLA+** | 0.2 · 0.4 · 0.6 | zäh | 🔵 Startwert | [öffnen](esun-pla-plus.md) |
| **eSUN PLA+ Glow** | 0.4 · 0.6 | ⚠️ abrasiv | 🔵 Startwert | [öffnen](esun-pla-plus-glow.md) |
| **eSUN PETG** | 0.2 · 0.4 · 0.6 | | 🔵 Startwert | [öffnen](esun-petg.md) |
| **eSUN PETG Transparent** | 0.2 · 0.4 · 0.6 | 💧 klar | 🔵 Startwert | [öffnen](esun-petg-transparent.md) |
| **eSUN ABS+** | 0.2 · 0.4 · 0.6 | 🔥 Kammer nötig | 🔵 Startwert | [öffnen](esun-abs.md) |
| **Bambu PLA Basic** | 0.2 · 0.4 · 0.6 | schnell | 🔵 Startwert | [öffnen](bambu-pla-basic.md) |
| **Bambu PLA Glow** | 0.4 · 0.6 | ⚠️ abrasiv | 🔵 Startwert | [öffnen](bambu-pla-glow.md) |
| **Bambu PLA Translucent** | 0.2 · 0.4 · 0.6 | 💧 durchscheinend | 🔵 Startwert | [öffnen](bambu-pla-translucent.md) |
| **Bambu PETG HF** | 0.2 · 0.4 · 0.6 | schnell | 🔵 Startwert | [öffnen](bambu-petg-hf.md) |
| **Bambu PETG Translucent** | 0.2 · 0.4 · 0.6 | 💧 durchscheinend | 🔵 Startwert | [öffnen](bambu-petg-translucent.md) |

🟢 am Gerät gemessen · 🔵 berechneter Startwert · ⚠️ gehärtete Düse zwingend ·
💧 auf optische Klarheit abgestimmt · 🧵 flexibel, nicht über die AMS ·
🔥 geschlossene Kammer erforderlich, auf der A1 mini nicht verfügbar

---

## Auf einen Blick

Volumenstrom bezogen auf den X1 Carbon mit 0.4-mm-Düse; die übrigen Drucker werden
über den [Durchsatzfaktor](../drucker/README.md#durchsatzfaktoren) skaliert.

### SUNLU

| | PLA | PLA Glow | PLA Transp. | PETG | PETG Glow | PETG Transp. | TPU |
|---|--:|--:|--:|--:|--:|--:|--:|
| Düse | 215 °C | 225 °C | 223 °C | 245 °C | 248 °C | 252 °C | 225 °C |
| Bett | 55 °C | 55 °C | 55 °C | 70 °C | 70 °C | 70 °C | 35 °C |
| Glasübergang | 55 °C | 55 °C | 55 °C | 71 °C | 71 °C | 71 °C | 30 °C |
| Flussrate | 0.98 | 0.96 | 0.98 | 0.95 | 0.98 | 0.95 | 1.00 |
| Lüfter | 60–100 % | 60–100 % | 30–60 % | 20–50 % | 10–30 % | 10–25 % | 100 % |
| Volumenstrom | 15.0 | 10.5 | 12.8 | 14.0 | 11.0 | 11.9 | 3.2 |
| Trocknung | 45/6 h | 45/6 h | 45/6 h | 65/8 h | 65/8 h | 65/8 h | 50/8 h |

### eSUN

| | PLA+ | PLA+ Glow | PETG | PETG Transp. | ABS+ |
|---|--:|--:|--:|--:|--:|
| Düse | 220 °C | 228 °C | 243 °C | 250 °C | 255 °C |
| Bett | 60 °C | 60 °C | 75 °C | 75 °C | 90 °C |
| Glasübergang | 55 °C | 55 °C | 71 °C | 71 °C | 100 °C |
| Flussrate | 0.98 | 0.95 | 0.95 | 0.95 | 0.95 |
| Lüfter | 50–90 % | 50–90 % | 20–50 % | 10–25 % | 10–30 % |
| Volumenstrom | 16.0 | 10.0 | 13.0 | 11.0 | 15.0 |
| Trocknung | 45/6 h | 45/6 h | 65/8 h | 65/8 h | 70/4 h |

### Bambu Lab

| | PLA Basic | PLA Glow | PLA Transl. | PETG HF | PETG Transl. |
|---|--:|--:|--:|--:|--:|
| Düse | 220 °C | 220 °C | 228 °C | 245 °C | 250 °C |
| Bett | 55 °C | 55 °C | 55 °C | 70 °C | 70 °C |
| Glasübergang | 45 °C | 45 °C | 45 °C | 70 °C | 70 °C |
| Flussrate | 0.98 | 0.98 | 0.98 | 0.97 | 0.97 |
| Lüfter | 100 % | 100 % | 40–70 % | 20–40 % | 10–25 % |
| Volumenstrom | **21.0** | 18.0 | 12.0 | **21.0** | 6.0 |
| Trocknung | 45/6 h | 45/6 h | 45/6 h | 65/8 h | 65/8 h |

---

## Welches Material wofür

| Anforderung | Material |
|---|---|
| Sichtteile, Modelle, schnelle Prototypen | SUNLU PLA · Bambu PLA Basic |
| Kürzeste Druckzeit | **Bambu PLA Basic** · **Bambu PETG HF** |
| Halterungen, Clips, Rastverbindungen | **eSUN PLA+** |
| Wärme, Sonne, mechanische Dauerlast | jedes PETG |
| Dauerhaft über 70 °C | **eSUN ABS+** — nur mit geschlossener Kammer |
| Dichtungen, Puffer, griffige Auflagen | **SUNLU TPU** |
| Belastbar **und** schnell | **Bambu PETG HF** |
| Leuchteffekt, dekorativ | Bambu PLA Glow (schnellstes) · SUNLU PLA Glow |
| Leuchteffekt und Belastbarkeit | SUNLU PETG Glow |
| Glasklare Teile | **SUNLU PETG Transparent** · eSUN PETG Transparent |
| Lampenschirme, Diffusoren | Bambu PLA Translucent · Bambu PETG Translucent |

**Wärmefestigkeit ist das Hauptkriterium bei der Materialklasse.** PLA gibt ab 45 – 55 °C
nach — das erreicht ein Auto im Sommer mühelos. Für alles, was Wärme oder dauerhafte
Last sieht, ist PETG die richtige Wahl, auch wenn es im Druck mehr Aufmerksamkeit
verlangt. Oberhalb von 70 °C hilft auch PETG nicht mehr; dort beginnt der Bereich von
[ABS](esun-abs.md), das als einziges Material hier einen Glasübergang von 100 °C
mitbringt — und als einziges eine geschlossene Kammer verlangt.

**TPU ist ein Sonderfall.** Es konkurriert mit keinem der anderen Materialien, weil es
etwas anderes kann: dauerhaft nachgeben, ohne zu brechen. Der Preis ist der
Durchsatz — rund ein Fünftel von PLA, siehe [SUNLU TPU](sunlu-tpu.md).

**Der Hersteller entscheidet über die Druckzeit.** Die Bambu-Materialien erben von
den herstellereigenen Basisprofilen und bringen deren gemessene Volumenströme mit —
bei PLA Basic und PETG HF sind das rund 40 % mehr Durchsatz als bei den generischen
Profilen der anderen Hersteller. Wer nach Zeit optimiert, wählt dort.

---

## Was die Glow-Varianten unterscheidet

Alle vier Glow-Materialien enthalten Strontiumaluminat. Daraus folgt unabhängig vom
Grundmaterial und Hersteller:

- gehärtete Düse zwingend
- 0.2 mm nicht verwendbar ([warum](../nozzles.md#warum-02-mm-bei-glow-gesperrt-ist))
- Leuchtwirkung steigt mit Wandzahl und Füllung, nicht mit der Temperatur
- Aufladen mit UV- oder kaltweißem Licht, nicht mit Tageslicht

Beim Volumenstrom gehen die Hersteller dagegen auseinander:

| Material | Volumenstrom 0.4 mm | gegenüber dem Basismaterial |
|---|--:|---|
| SUNLU PLA Glow | 10.5 | −30 % |
| eSUN PLA+ Glow | 10.0 | −38 % |
| **Bambu PLA Glow** | **18.0** | **−14 %** |
| SUNLU PETG Glow | 11.0 | −21 % |

Bambus feineres Pigment stört den Schmelzfluss deutlich weniger. Für größere
Leuchtteile ist das der entscheidende Unterschied.

---

## Was die transparenten Varianten unterscheidet

> 💧 Klarheit entsteht nicht im Filament, sondern in der Schmelze. Jede Grenzfläche
> zwischen zwei Bahnen, die nicht vollständig verschmolzen ist, streut Licht.

Alle fünf klaren Materialien fahren deshalb dasselbe Rezept:

- **Düse 5 – 10 °C heißer** als das opake Material derselben Familie
- **Volumenstrom rund 15 % niedriger** — der eigentliche Wirkmechanismus
- **Lüfter etwa halbiert**, Verzögerungsschwelle erhöht, eine Schicht länger aus

Dazu kommen drei Regeln, die nicht im Profil stehen, sondern beim Slicen gelten:

1. **Füllung 100 % oder 0 %.** Alles dazwischen erzeugt sichtbare Gitterstrukturen.
2. **Hohe Schichthöhe, grobe Düse.** Weniger Grenzflächen bedeuten weniger Streuung —
   0.6 mm mit 0.3 mm Schichthöhe schlägt 0.2 mm mit 0.1 mm.
3. **Glatte Platte.** Die texturierte prägt ihre Struktur dauerhaft in die Unterseite.

**Transparent ist nicht gleich durchscheinend.** Die PETG-Varianten zielen auf
Glasklarheit, die beiden Bambu-Translucent-Materialien auf gleichmäßige Streuung —
für Lampenschirme ist das die gewünschte Eigenschaft, für ein Sichtfenster nicht.

---

[Zurück zur Übersicht](../../README.md) · [Drucker](../drucker/README.md) · [Düsenkunde](../nozzles.md) · [Profilmatrix](../matrix.md)
