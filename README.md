<div align="center">

# Bambu Lab Druckprofile

**Abgestimmte Filament- und Prozessprofile für 15 Materialien von SUNLU, eSUN
und Bambu Lab — auf fünf Bambu-Lab-Druckern, drei Düsendurchmessern und drei
Qualitätsstufen.**

[![Presets](https://img.shields.io/badge/Presets-250-2d7ff9)](docs/matrix.md)
[![Materialien](https://img.shields.io/badge/Materialien-15-2d7ff9)](docs/filament/README.md)
[![Drucker](https://img.shields.io/badge/Drucker-5-2d7ff9)](docs/drucker/README.md)
[![Slicer](https://img.shields.io/badge/Bambu%20Studio-2.7%2B-00a76f)](https://bambulab.com/en/download/studio)
[![Abhängigkeiten](https://img.shields.io/badge/Abhängigkeiten-keine-6b7280)](#werkzeuge)

[Matrix](docs/matrix.md) · [Installation](docs/install.md) · [Düsen](docs/nozzles.md) · [Kalibrierung](docs/calibration.md) · [Fehlerbilder](docs/troubleshooting.md)

</div>

---

## Was hier drin ist

Bambu Studio liefert Profile für Bambus eigene Filamente — allerdings nur je
Drucker, nicht je Düse. Für Drittanbieter-Material bleibt der Weg über `Generic PLA`
oder `Generic PETG`, brauchbar, aber weder auf das Material noch auf die Düse
abgestimmt. Dieses Repository schließt beide Lücken:

| | |
|---|---|
| **205 Filamentprofile** | Temperatur, Fluss, Volumenstrom und Kühlung je Material, Drucker und Düse |
| **45 Prozessprofile** | Schichthöhe, Wandstärke, Füllung und Tempo je Drucker, Düse und Qualitätsstufe |
| **5 Drucker** | H2C · X1 Carbon · P1S · A1 · A1 mini |
| **15 Materialien** | 6 × SUNLU · 4 × eSUN · 5 × Bambu Lab, davon 4 Glow und 5 transparent |
| **3 Düsen** | 0.2 mm · 0.4 mm · 0.6 mm |
| **3 Stufen** | Qualität · Normal · Schnell |

Alle Profile **erben** von den Originalprofilen aus Bambu Studio. Überschrieben wird
nur, was tatsächlich material- oder stufenspezifisch ist. Alles andere bleibt auf den
vom Hersteller abgestimmten Werten und wandert bei einem Studio-Update mit.

## Schnellstart

```bash
git clone <repo-url> && cd printprofiles
open dist/            # die fertigen Presets
```

In Bambu Studio: **Datei → Import → Import-Konfiguration** und die benötigten
JSON-Dateien aus `dist/filament/` und `dist/process/` auswählen.
Die ausführliche Anleitung steht in [docs/install.md](docs/install.md).

Welche Datei die richtige ist, verrät der Name:

```
dist/filament/SUNLU PETG Glow H2C 0.4.json
              └── Material ──┘ └─┘ └─┘
                          Drucker  Düse

dist/process/Qualität X1C 0.6.json
             └─ Stufe ─┘ └┘  └─┘
                  Drucker    Düse
```

## Reifegrad der Werte

Ehrlichkeit vor Marketing: nur eine Kombination in diesem Repository ist tatsächlich
am Gerät gedruckt und bestätigt worden.

| Symbol | Bedeutung |
|---|---|
| 🟢 **verifiziert** | Am Drucker gedruckt und bestätigt. Aktuell: **SUNLU PETG Glow · H2C · 0.4 mm** |
| 🔵 **Startwert** | Aus dem Bambu-Basisprofil abgeleitet und rechnerisch auf Drucker und Düse skaliert. Druckbar, aber nicht einzeln erprobt. |

Startwerte sind keine Schätzungen ins Blaue: sie gehen von Bambus eigenen,
abgestimmten Werten aus und werden über den Leistungsfaktor des jeweiligen Hotends
umgerechnet. Für den ersten Druck reichen sie. Für Serienteile lohnt sich der
Durchlauf in [docs/calibration.md](docs/calibration.md) — er dauert rund 20 Minuten
je Kombination und hebt den Eintrag auf 🟢.

Den aktuellen Stand je Kombination zeigt die [Profilmatrix](docs/matrix.md).

## Dokumentation

| Seite | Inhalt |
|---|---|
| [Profilmatrix](docs/matrix.md) | Welche Kombination existiert, mit welchen Werten, in welchem Zustand |
| [Installation](docs/install.md) | Import in Bambu Studio, Aktualisierung, Deinstallation |
| [Düsenkunde](docs/nozzles.md) | Wann 0.2, wann 0.4, wann 0.6 — und warum Glow-Material die 0.2 sperrt |
| [Kalibrierung](docs/calibration.md) | Flussrate, Volumenstrom, Temperatur: der Weg von 🔵 nach 🟢 |
| [Fehlerbilder](docs/troubleshooting.md) | Vom Symptom zum Parameter |
| [Materialien](docs/filament/README.md) | 15 Datenblätter: Kennwerte, Volumenströme, Fallstricke |
| [Drucker](docs/drucker/README.md) | Eigenheiten der fünf Maschinen |

## Aufbau des Repositories

```
src/                 Quelldaten — hier wird bearbeitet
├── printers.toml      5 Drucker: Hotend-Leistung, Bauraum, Extruder
├── quality.toml       3 Stufen: Schichthöhen, Wände, Tempofaktoren
└── filaments/        15 Materialien: Temperatur, Fluss, Kühlung
tools/               Generator und Prüfung
├── bambulib.py        liest die Bambu-Studio-Profilbibliothek
├── generate.py        src/ → dist/
├── validate.py        prüft dist/ gegen die Bibliothek
└── build_docs.py      erzeugt docs/matrix.md
dist/                Ergebnis — hier wird importiert, nicht bearbeitet
├── filament/         205 Presets
├── process/           45 Presets
└── _index.json        Metadaten aller Presets
tests/               24 Tests der Generatorlogik
```

**`dist/` ist erzeugt.** Änderungen gehören nach `src/`, danach neu generieren.
Eine Bearbeitung direkt in `dist/` überlebt den nächsten Lauf nicht.

## Werkzeuge

Reine Standardbibliothek, Python 3.11 oder neuer. Keine Installation, kein
`requirements.txt`, kein Build-Schritt.

```bash
python3 tools/generate.py        # src/ → dist/
python3 tools/validate.py        # 15808 Prüfungen gegen die Bambu-Bibliothek
python3 tools/build_docs.py      # docs/matrix.md neu erzeugen
python3 -m unittest discover -s tests
```

Der Generator liest die Profilbibliothek aus der lokalen Bambu-Studio-Installation.
Liegt sie woanders, hilft eine Umgebungsvariable:

```bash
export BAMBU_PROFILE_DIR=/Pfad/zu/BambuStudio/resources/profiles/BBL
```

## Etwas ändern

1. Wert in `src/` anpassen — etwa den Volumenstrom in `src/filaments/sunlu-petg.toml`
2. `python3 tools/generate.py && python3 tools/validate.py`
3. `python3 tools/build_docs.py`
4. Neu importieren (siehe [Installation](docs/install.md))

Der Validator fängt dabei ab, was Bambu Studio sonst stillschweigend verschluckt:
fehlende Elternprofile, unbekannte Schlüssel, falsche Arraylängen, Schichthöhen
außerhalb der Maschinengrenzen, Temperaturen über dem Hotend-Limit.

## Haftung

Druckprofile greifen in Temperatur, Fluss und Geschwindigkeit ein. Die Werte sind
sorgfältig hergeleitet, aber jede Maschine, jede Düse und jede Filamentcharge ist
anders. Erster Druck mit Blick auf die erste Schicht — wie immer.
