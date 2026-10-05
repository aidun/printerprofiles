# Entwicklung

[← Zurück zur Übersicht](../README.md)

Diese Seite richtet sich an alle, die Werte ändern, Material ergänzen oder den
Generator verstehen wollen. Für den reinen Gebrauch der fertigen Profile wird sie
nicht gebraucht — dafür genügen [Installation](install.md) und
[Materialien](filament/README.md).

---

## Grundprinzip

Nichts in `dist/` ist von Hand geschrieben. Die Wahrheit steht in `src/`, der Rest
wird erzeugt:

```
src/*.toml   ──  tools/generate.py  ──▶  dist/*.json   ──▶  Bambu Studio
                        │                      │
                        │                      └── tools/validate.py
                        └── tools/build_docs.py ──▶ docs/matrix.md
```

**Eine Bearbeitung direkt in `dist/` überlebt den nächsten Lauf nicht.**

## Aufbau des Repositories

```
src/                 Quelldaten — hier wird bearbeitet
├── printers.toml      6 Drucker: Maschinenname, Hotend-Grenze, Leistungsfaktor
├── quality.toml       3 Stufen: Schichthöhen, Wände, Tempofaktoren
└── filaments/        17 Materialien: Temperatur, Fluss, Kühlung
tools/               Generator und Prüfung
├── bambulib.py        liest die Bambu-Studio-Profilbibliothek
├── generate.py        src/ → dist/
├── validate.py        prüft dist/ gegen die Bibliothek
└── build_docs.py      erzeugt docs/matrix.md
dist/                Ergebnis — hier wird importiert, nicht bearbeitet
├── filament/         273 Presets
├── process/           54 Presets
└── _index.json        Metadaten aller Presets
docs/                Dokumentation — Deutsch, von Hand außer matrix.md
tests/               Tests der Generatorlogik
```

Der Code ist durchgehend englisch, die Dokumentation durchgehend deutsch.

---

## Werkzeuge

Reine Standardbibliothek, Python 3.11 oder neuer. Keine Installation, kein
`requirements.txt`, kein Build-Schritt.

```bash
python3 tools/generate.py        # src/ → dist/
python3 tools/validate.py        # prüft dist/ gegen die Bambu-Bibliothek
python3 tools/build_docs.py      # docs/matrix.md neu erzeugen
python3 -m unittest discover -s tests
```

Der Generator liest die Profilbibliothek aus der lokalen Bambu-Studio-Installation.
Liegt sie woanders, hilft eine Umgebungsvariable:

```bash
export BAMBU_PROFILE_DIR=/Pfad/zu/BambuStudio/resources/profiles/BBL
```

---

## Einen Wert ändern

1. Wert in `src/` anpassen — etwa den Volumenstrom in `src/filaments/sunlu-petg.toml`
2. `python3 tools/generate.py && python3 tools/validate.py`
3. `python3 tools/build_docs.py`
4. `python3 -m unittest discover -s tests`
5. Neu importieren (siehe [Installation](install.md#aktualisieren))

Gemessene Werte gehören **auf den X1 Carbon zurückgerechnet**, bevor sie in `src/`
landen — die übrigen Drucker leitet der Generator über ihren Leistungsfaktor ab.
Die Rechnung steht in [Kalibrierung](calibration.md#gemessenen-wert-zurückrechnen).

---

## Ein Material ergänzen

Eine neue Datei in `src/filaments/` anlegen; als Vorlage dient am besten ein
Material derselben Klasse. Pflichtfelder:

| Feld | Bedeutung |
|---|---|
| `id` | Dateiname ohne Endung, zugleich Schlüssel in `dist/_index.json` |
| `label` | Anzeigename, erscheint im Preset-Namen |
| `order` | Position in Dokumentation und Matrix, lückenlos ab 1 |
| `short` | Kurzform für Tabellenspalten, etwa `PLA` oder `PETG-CF` |
| `brand` | `SUNLU`, `eSUN` oder `Bambu Lab` |
| `material` | `PLA`, `PETG`, `TPU` oder `ABS` |
| `base` | Elternprofil aus Bambu Studio, etwa `Generic PETG` |
| `abrasive` / `hardened` | steuern Warnhinweis und Düsenempfehlung |
| `transparent` | steuert den Klarheits-Hinweis in der Dokumentation |
| `flexible` | flexibles Material; sperrt wie `abrasive` die 0.2-mm-Düse |
| `status` | `baseline` oder `validated-<drucker>-<düse>`, etwa `validated-h2c-04` |
| `nozzles` | freigegebene Durchmesser; abrasives und flexibles Material lässt `0.2` weg |
| `drying` | Trocknungsempfehlung in der Form `45 °C / 6 h` |
| `storage` | Lagerhinweis, etwa `trocken, Silikagel` |
| `description` | zwei bis drei Sätze zum Material, für das Datenblatt |

`short`, `drying`, `storage` und `description` wertet die Pipeline nicht aus — sie
sind Quelle für die Dokumentation. Pflicht sind sie trotzdem, `tests/test_generate.py`
wacht darüber.

Dazu kommt ein optionaler Schlüssel:

| Feld | Bedeutung |
|---|---|
| `printers` | Liste der Druckerkürzel aus `src/printers.toml`, für die das Material erzeugt wird. Fehlt der Schlüssel, gilt es für alle. Nötig, wenn die Bambu-Bibliothek für ein Gerät kein Basisprofil führt — bei `esun-abs` die A1 mini. |

`test_printer_restrictions_match_the_library` prüft diese Liste in beide Richtungen
gegen die Bibliothek: Sie muss **genau** die Geräte nennen, deren Basisprofil
tatsächlich auflöst. Ein zu großzügiger wie ein zu knapper Eintrag fällt auf.

Dazu kommen fünf Tabellen, die alle gezeigten Schlüssel brauchen:

| Tabelle | Schlüssel |
|---|---|
| `[temperature]` | `nozzle`, `nozzle_initial`, `range_low`, `range_high`, `vitrification`, `bed`, `bed_initial` |
| `[flow]` | `ratio` — Flussrate zwischen 0.85 und 1.15 |
| `[volumetric_flow]` | je freigegebene Düse ein Eintrag, Schlüssel als String: `"0.2"`, `"0.4"`, `"0.6"` |
| `[cooling]` | `fan_min_speed`, `fan_max_speed`, `overhang_fan_speed`, `slow_down_layer_time`, `fan_cooling_layer_time`, `close_fan_the_first_x_layers` |
| `[retraction]` | `z_hop` |

Die Volumenströme unter `[volumetric_flow]` beziehen sich immer auf den X1 Carbon;
`flow_factor` aus `src/printers.toml` rechnet sie auf die übrigen Drucker um.

> **Bambu-eigene Materialien** erben von ihrem Herstellerprofil, nicht von
> `Generic …` — `base` ist dort identisch mit `label`. Ein Test wacht darüber.

Danach die Pipeline durchlaufen lassen und ein Datenblatt unter `docs/filament/`
anlegen. Die Navigationsfußzeile der Nachbarseiten mit aufnehmen.

---

## Was der Validator abfängt

Bambu Studio verschluckt fehlerhafte Presets stillschweigend — der Validator tut es
nicht:

| Prüfung | Fehlerbild in Studio ohne Prüfung |
|---|---|
| Elternprofil existiert und ist für die Maschine freigegeben | Preset erscheint nicht |
| Unbekannte Schlüssel | Einstellung wird kommentarlos verworfen |
| Arraylängen passen zu den Extrudervarianten | falscher Extruder bekommt den Wert |
| Schichthöhe innerhalb der Maschinengrenzen und ≤ 75 % des Düsendurchmessers | Druckabbruch oder Unterextrusion |
| Temperaturfenster aufsteigend, Werte innerhalb des Fensters | Studio korrigiert stumm |
| Temperatur unterhalb des Hotend-Limits | Profil nicht einsetzbar |
| Volumenstrom 0.8 – 40 mm³/s, Flussrate 0.85 – 1.15 | Tippfehler bleiben unbemerkt |

Der Lauf endet mit einer Zeile der Form
`<n> checks, 0 errors, 327 presets.` und einem Exitcode ungleich null, sobald
etwas nicht stimmt.

---

## Tests

```bash
python3 -m unittest discover -s tests -v
```

Die Tests decken vier Bereiche ab: Hilfsfunktionen des Generators, das Lesen der
Bambu-Bibliothek, die Konsistenz der Quelldaten (Vollständigkeit, Glow- und
TPU-Regel für die 0.2-mm-Düse, Temperaturfenster, Klarheitsregel für transparente
Varianten, Abgleich des `printers`-Schlüssels mit der Bibliothek) und das Ergebnis
eines vollständigen Laufs — darunter die am Gerät verifizierte Referenzkombination
SUNLU PETG Glow · H2C · 0.4 mm.

Wer einen Wert ändert, der in einem Test steht, ändert den Test bewusst mit — nicht
umgekehrt.

---

## Beitrag einreichen

1. Fork anlegen, Zweig erstellen
2. Änderung in `src/` vornehmen, Pipeline durchlaufen lassen
3. Die erzeugten Dateien unter `dist/` und `docs/matrix.md` **mit committen** —
   das Repository liefert bewusst fertige Dateien aus
4. Pull Request eröffnen und darin angeben, ob die Werte gemessen oder hergeleitet
   sind

Gemessene Werte sind besonders willkommen: Sie heben Einträge von 🔵 auf 🟢 und
sind der einzige Weg, wie dieses Repository über die Zeit belastbarer wird.

---

[← Kalibrierung](calibration.md) · [Zurück zur Übersicht](../README.md) · [Profilmatrix →](matrix.md)
