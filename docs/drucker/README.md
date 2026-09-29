# Drucker

[← Zurück zur Übersicht](../../README.md)

Fünf Geräte, jeweils als eigene Seite mit Eckdaten, Volumenströmen, Schichthöhen und
den Eigenheiten, die im Alltag zählen.

| Drucker | Kürzel | Bauraum | Kammer | Faktor | Seite |
|---|---|---|---|--:|---|
| **H2C** | `H2C` | 350 × 320 × 325 mm | aktiv beheizt | 1.15 | [öffnen](h2c.md) |
| **X1 Carbon** | `X1C` | 256 × 256 × 256 mm | geschlossen, passiv | 1.00 | [öffnen](x1c.md) |
| **P1S** | `P1S` | 256 × 256 × 256 mm | geschlossen, passiv | 0.95 | [öffnen](p1s.md) |
| **A1** | `A1` | 256 × 256 × 256 mm | offen | 0.90 | [öffnen](a1.md) |
| **A1 mini** | `A1M` | 180 × 180 × 180 mm | offen | 0.85 | [öffnen](a1mini.md) |

---

## Durchsatzfaktoren

Alle Volumenströme in `src/filaments/` sind **X1C-Werte**. Für jeden anderen Drucker
multipliziert der Generator diesen Basiswert mit dem Faktor der Maschine und deckelt
das Ergebnis bei 30 mm³/s.

```
Volumenstrom(Drucker) = Basiswert(X1C) × Faktor(Drucker)
```

Beispiel SUNLU PETG Glow, 0.4 mm:

```
Basiswert 11.0 mm³/s
  × 1.15 (H2C)     = 12.6   🟢 am Gerät gemessen
  × 1.00 (X1C)     = 11.0
  × 0.95 (P1S)     = 10.4
  × 0.90 (A1)      =  9.9
  × 0.85 (A1 mini) =  9.3
```

Der Faktor bildet die Aufschmelzleistung des Hotends ab, nicht die
Bewegungsgeschwindigkeit. Wer einen Wert am eigenen Gerät misst, rechnet ihn über
denselben Faktor auf den Basiswert zurück und trägt diesen in `src/` ein — der
Ablauf steht in [Kalibrierung](../calibration.md#gemessenen-wert-zurückrechnen).

## Extrudervarianten

Bambu Studio hinterlegt viele Werte als Array mit einem Eintrag je Extrudervariante.
Wie viele das sind, entscheidet die Maschine:

| Drucker | Varianten | Geschwindigkeitswerte je Parameter |
|---|---|--:|
| A1, A1 mini | Direct Drive Standard | 1 |
| X1C, P1S | Direct Drive Standard · High Flow | 2 |
| H2C | 2 Extruder × Standard/High Flow | 4 |

Deshalb definiert dieses Repository Geschwindigkeiten als **Faktoren**, nicht als
absolute Werte: Sie werden elementweise auf das Basisprofil angewandt, die Arraylänge
bleibt korrekt und Bambus Abstimmung zwischen Standard- und High-Flow-Extruder bleibt
erhalten. Ein Preset ist damit an seine Maschine gebunden und nicht übertragbar.

## Profilangebot

Der H2C bietet weniger Basisprofile an als die übrigen Geräte. Wo die Zielschichthöhe
einer Stufe dort nicht verfügbar ist, wählt der Generator automatisch das
nächstgelegene freigegebene Profil innerhalb der Maschinengrenzen. Betroffene Werte
sind in der [Profilmatrix](../matrix.md) mit ⁽¹⁾ markiert.

---

[Zurück zur Übersicht](../../README.md) · [Materialien](../filament/README.md) · [Profilmatrix](../matrix.md)
