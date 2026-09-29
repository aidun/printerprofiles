# Design: Bambu Lab Druckprofil-Repository

> Status: abgestimmt · Datum: 2026-09-29 · Bambu Studio 02.07.01.62

## Ziel

Ein Repository mit funktionierenden, optimierten und dokumentierten Druck- und
Arbeitsprofilen für alle Kombinationen aus fünf Bambu-Lab-Druckern, vier
SUNLU-Filamentvarianten, drei Düsendurchmessern und drei Qualitätsstufen.

## Abgedeckte Dimensionen

| Dimension | Werte |
|---|---|
| Drucker | H2C, X1C, P1S, A1, A1 mini |
| Filament | SUNLU PLA, SUNLU PLA Glow, SUNLU PETG, SUNLU PETG Glow |
| Düse | 0.2 mm, 0.4 mm, 0.6 mm |
| Qualität | schnell, normal, qualität |

180 logische Kombinationen, abgebildet auf 50 Filament- und 45 Prozess-Presets:
Bambu Studio trennt materialbezogene von geometriebezogenen Einstellungen, jeder
Parameter steht deshalb nur an genau einer Stelle.

## Architektur

```
src/         TOML-Quelle (die Wahrheit)
tools/       generate.py (TOML -> dist), validate.py (Prüfregeln)
dist/        fertige Bambu-Studio-JSONs, eingecheckt
docs/        deutschsprachige Produktdokumentation (reines Markdown)
tests/       pytest-freie Selbsttests (stdlib unittest)
```

Datenfluss: `src/*.toml` → `generate.py` → `dist/**/*.json` → Import in Bambu Studio.
`generate.py` löst die Elternprofile gegen die lokal installierte
Bambu-Studio-Profilbibliothek auf und schreibt die Auflösung nach
`dist/_index.json`, damit jede Ableitung nachvollziehbar bleibt.

## Vererbung

Basis sind die `Generic PLA` / `Generic PETG` Systemprofile (nicht die
`Bambu …`-Profile), da SUNLU ein Drittanbieter-Filament ist. Die Basis wird pro
Drucker-/Düsenkombination über `compatible_printers` der Systemprofile ermittelt.
Prozess-Presets erben von der System-Prozessvorlage mit der nächstliegenden
Schichthöhe.

Erkenntnisse aus der Profilbibliothek:

- P1S besitzt keine eigenen Prozessprofile, sondern nutzt die `@BBL X1C`-Profile.
- A1 mini heißt intern `A1M`, X1C als Maschine `Bambu Lab X1 Carbon`.
- H2C ist ein Vortek-Toolchanger mit zwei aktiven Extrudern; extruderabhängige
  Werte sind zweielementige Arrays mit `nil` als zweitem Element.
- X1C, P1S und H2C kennen die Extrudervarianten `Direct Drive Standard` und
  `Direct Drive High Flow`; A1 und A1 mini nur die Standardvariante.

## Schichthöhen

| Düse | qualität | normal | schnell |
|---|---|---|---|
| 0.2 mm | 0.08 mm | 0.12 mm | 0.14 mm |
| 0.4 mm | 0.12 mm | 0.20 mm | 0.28 mm |
| 0.6 mm | 0.20 mm | 0.30 mm | 0.42 mm |

Die Werte liegen innerhalb der maschinenseitigen Grenzen (0.2 mm: 0.04–0.14,
0.6 mm: 0.12–0.42); `validate.py` prüft das.

## Volumenstrom

Materialbasiswert (bezogen auf X1C) skaliert mit einem Druckerfaktor:
H2C 1.15, X1C 1.00, P1S 0.95, A1 0.90, A1 mini 0.85. Glow-Varianten liegen
materialseitig niedriger, weil Strontiumaluminat-Partikel den Schmelzfluss stören.

## Glow-Filamente

Glow-Varianten sind stark abrasiv und grobkörnig. Konsequenzen:

1. **Keine Profile für 0.2 mm** — die Partikelgröße führt zu Verstopfung.
   Dokumentiert statt erfunden.
2. Gehärtete Düse verpflichtend, in der Dokumentation an jeder relevanten Stelle.
3. Reduzierter Volumenstrom gegenüber der Normalvariante.

## Referenzwerte

Das bereits vorhandene Nutzerprofil `SUNLU PETG GLOW H2C 0.4` (Flow 0.98,
12.6 mm³/s, Düse 245–250 °C, Bett 75 °C, Lüfter 10–30 %) gilt als am Gerät
verifizierter Anker; alle übrigen PETG-Glow-Werte sind davon abgeleitet.

## Status-Konzept

Jedes Profil trägt ein `status`-Feld: `baseline` (aus Systemprofilen, Datenblättern
und Materialverhalten abgeleitet) oder `validated` (am Gerät gedruckt). Der Status
erscheint als Spalte in `docs/matrix.md` und wird in der README einmal erklärt —
keine Warnbanner in jeder Datei.

## Dokumentation

Deutschsprachiges Markdown ohne Build-Schritt, gestaltet wie eine
Produktdokumentation: Badges, GitHub-Alerts, Mermaid-Diagramme, konsistente
Kopf- und Fußnavigation, Querverweise.

## Qualitätssicherung

`tools/validate.py` prüft: Existenz jedes Elternprofils, Gültigkeit jeder
`compatible_printers`-Angabe, Arraylänge gegen Extruderzahl, Schichthöhe gegen
Maschinengrenzen, Temperatur gegen Hotend-Maximum, Namenseindeutigkeit und
JSON-Wohlgeformtheit. `tests/` prüft die Generatorlogik mit `unittest`.
