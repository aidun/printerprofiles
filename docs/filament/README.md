# Materialien

[← Zurück zur Übersicht](../../README.md)

Vier Materialien, jeweils als eigenes Datenblatt mit Kennwerten, Volumenströmen je
Drucker und den materialtypischen Fallstricken.

| Material | Düsen | Abrasiv | Status | Datenblatt |
|---|---|---|---|---|
| **SUNLU PLA** | 0.2 · 0.4 · 0.6 | nein | 🔵 Startwert | [öffnen](sunlu-pla.md) |
| **SUNLU PLA Glow** | 0.4 · 0.6 | ⚠️ ja | 🔵 Startwert | [öffnen](sunlu-pla-glow.md) |
| **SUNLU PETG** | 0.2 · 0.4 · 0.6 | nein | 🔵 Startwert | [öffnen](sunlu-petg.md) |
| **SUNLU PETG Glow** | 0.4 · 0.6 | ⚠️ ja | 🟢 H2C · 0.4 mm verifiziert | [öffnen](sunlu-petg-glow.md) |

🟢 am Gerät gemessen · 🔵 berechneter Startwert · ⚠️ gehärtete Düse zwingend

---

## Auf einen Blick

| | PLA | PLA Glow | PETG | PETG Glow |
|---|--:|--:|--:|--:|
| Düse | 215 °C | 225 °C | 245 °C | 248 °C |
| Bett | 55 °C | 55 °C | 70 °C | 70 °C |
| Glasübergang | 55 °C | 55 °C | 71 °C | 71 °C |
| Flussrate | 0.98 | 0.96 | 0.96 | 0.98 |
| Lüfter | 60–100 % | 60–100 % | 20–50 % | 10–30 % |
| Z-Hop | 0.4 mm | 0.4 mm | 0.6 mm | 0.6 mm |
| Trocknung | 45 °C / 6 h | 45 °C / 6 h | 65 °C / 8 h | 65 °C / 8 h |

## Welches Material wofür

| Anforderung | Material |
|---|---|
| Sichtteile, Modelle, schnelle Prototypen | PLA |
| Wärme, Sonne, mechanische Belastung | PETG |
| Leuchteffekt, dekorativ | PLA Glow |
| Leuchteffekt und Belastbarkeit | PETG Glow |

**Wärmefestigkeit ist das Hauptkriterium.** PLA gibt ab 55 °C nach — das erreicht ein
Auto im Sommer mühelos. Für alles, was Wärme oder dauerhafte Last sieht, ist PETG die
richtige Wahl, auch wenn es im Druck mehr Aufmerksamkeit verlangt.

## Was die Glow-Varianten unterscheidet

Beide Glow-Materialien enthalten Strontiumaluminat. Daraus folgt unabhängig vom
Grundmaterial:

- gehärtete Düse zwingend
- 0.2 mm nicht verwendbar ([warum](../nozzles.md#warum-02-mm-bei-glow-gesperrt-ist))
- rund 30 % niedrigerer Volumenstrom
- Leuchtwirkung steigt mit Wandzahl und Füllung, nicht mit der Temperatur

---

[Zurück zur Übersicht](../../README.md) · [Drucker](../drucker/README.md) · [Düsenkunde](../nozzles.md)
