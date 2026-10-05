<div align="center">

# Bambu Lab Druckprofile

**379 fertige Presets für Bambu Studio — 21 Materialien von SUNLU, eSUN und
Bambu Lab, abgestimmt auf sechs Drucker, drei Düsen und drei Qualitätsstufen.
Herunterladen, importieren, drucken.**

[![Presets](https://img.shields.io/badge/Presets-379-2d7ff9)](docs/matrix.md)
[![Materialien](https://img.shields.io/badge/Materialien-21-2d7ff9)](docs/filament/README.md)
[![Drucker](https://img.shields.io/badge/Drucker-6-2d7ff9)](docs/drucker/README.md)
[![Slicer](https://img.shields.io/badge/Bambu%20Studio-2.7%2B-00a76f)](https://bambulab.com/en/download/studio)

[Loslegen](#in-drei-schritten-loslegen) · [Passendes Profil finden](#das-passende-profil-finden) · [Materialien](docs/filament/README.md) · [Fehlerbilder](docs/troubleshooting.md) · [Rückmeldung geben](#rückmeldung-geben)

</div>

---

## Wofür das gut ist

Bambu Studio bringt Profile für Bambus eigene Filamente mit — allerdings je Drucker,
nicht je Düse. Für Material anderer Hersteller bleibt nur `Generic PLA` oder
`Generic PETG`: druckbar, aber weder auf das Material noch auf den Düsendurchmesser
abgestimmt.

Dieses Repository liefert für jede sinnvolle Kombination ein fertiges Preset —
mit passender Temperatur, Flussrate, Kühlung und einem Volumenstrom, der zur
Leistung des jeweiligen Hotends passt.

| | |
|---|---|
| **6 Drucker** | H2C · X1 Carbon · P1S · P1P · A1 · A1 mini |
| **21 Materialien** | 7 × SUNLU · 5 × eSUN · 9 × Bambu Lab — PLA, PETG, PETG-CF, TPU, ABS, ASA und ASA-CF, darunter 4 Glow, 5 transparente und 2 faserverstärkte |
| **3 Düsen** | 0.2 mm · 0.4 mm · 0.6 mm |
| **3 Stufen** | Qualität · Normal · Schnell |

Alle Profile **erben** von den Originalprofilen aus Bambu Studio. Überschrieben wird
nur, was tatsächlich material- oder stufenspezifisch ist — alles andere bleibt auf
den vom Hersteller abgestimmten Werten und wandert bei einem Studio-Update mit.

---

## In drei Schritten loslegen

### 1. Dateien holen

```bash
git clone https://github.com/aidun/printerprofiles.git
cd printerprofiles
open dist/
```

Ohne Git geht es genauso: oben auf **Code → Download ZIP** und entpacken. Gebraucht
wird nur der Ordner `dist/` — alles darin ist fertig und muss nicht erzeugt werden.

### 2. Die beiden passenden Dateien heraussuchen

Für einen Druck werden **immer zwei** Presets gebraucht:

```
dist/filament/SUNLU PETG Glow H2C 0.4.json     ← das Material
dist/process/Qualität H2C 0.4.json             ← die Qualitätsstufe
```

Der Dateiname sagt alles:

```
dist/filament/SUNLU PETG Glow H2C 0.4.json
              └─── Material ───┘ └─┘ └─┘
                            Drucker  Düse

dist/process/Qualität X1C 0.6.json
             └─ Stufe ─┘ └─┘ └─┘
                   Drucker  Düse
```

Drucker und Düse müssen bei beiden Dateien übereinstimmen.

### 3. In Bambu Studio importieren

```
Datei → Import → Import-Konfiguration …     (⌘ / Strg + I)
```

Mehrfachauswahl ist möglich. Danach erscheinen die Profile rechts in den
Auswahllisten für Filament und Prozess.

> **Ein Profil taucht nicht auf?** Dann ist in Studio eine andere Düse eingestellt.
> Jedes Preset ist an genau eine Drucker-Düsen-Kombination gebunden und erscheint
> nur dort. Weitere Fälle in der [Installationsanleitung](docs/install.md#wenn-ein-preset-nicht-auftaucht).

Der ausführliche Weg samt Aktualisieren und Entfernen steht in
**[docs/install.md](docs/install.md)**.

---

## Das passende Profil finden

**Welches Material?** Die Entscheidung fällt fast immer an der Wärmefestigkeit:
PLA gibt ab 45 – 55 °C nach, PETG hält deutlich mehr aus. Die Auswahlhilfe steht in
der [Materialübersicht](docs/filament/README.md#welches-material-wofür), jedes
Material hat ein eigenes Datenblatt mit Kennwerten und Fallstricken.

**Welche Düse?**

| Düse | Wofür |
|---|---|
| **0.2 mm** | Miniaturen, feine Schrift, Passungen — langsam, empfindlich |
| **0.4 mm** | der Standard für fast alles |
| **0.6 mm** | große Teile, Funktionsdruck, kurze Druckzeit |

Ausführlich, samt der Frage Messing oder gehärtet:
[Düsenkunde](docs/nozzles.md).

**Welche Stufe?**

| Stufe | Wofür |
|---|---|
| **Qualität** | Sichtflächen, feine Details — die längste Druckzeit |
| **Normal** | der Alltagsfall |
| **Schnell** | Prototypen, Passproben, Hilfsteile |

Welche Kombination es gibt und mit welchen Werten, zeigt die
**[Profilmatrix](docs/matrix.md)**.

> ⚠️ **Glow-Material braucht eine gehärtete Düse** und ist für 0.2 mm nicht
> verfügbar — das Leuchtpigment setzt die Bohrung zu.
> [Warum](docs/nozzles.md#warum-02-mm-bei-glow-gesperrt-ist).

> 🧵 **TPU gibt es ebenfalls nicht für 0.2 mm** — dort begrenzt der Extruder, nicht
> die Bohrung. 🔥 **ABS fehlt auf der A1 mini**, weil Bambu dort kein Basisprofil
> dafür führt.

---

## Wie belastbar die Werte sind

Ehrlichkeit vor Marketing: bisher ist **eine** Kombination tatsächlich am Gerät
gedruckt und bestätigt worden.

| Symbol | Bedeutung |
|---|---|
| 🟢 **verifiziert** | Am Drucker gedruckt und bestätigt. Aktuell: **SUNLU PETG Glow · H2C · 0.4 mm** |
| 🔵 **Startwert** | Aus dem Bambu-Basisprofil abgeleitet und rechnerisch auf Drucker und Düse skaliert. Druckbar, aber nicht einzeln erprobt. |

Startwerte sind keine Schätzungen ins Blaue: Sie gehen von Bambus eigenen,
abgestimmten Werten aus und werden über die Hotend-Leistung des jeweiligen Druckers
umgerechnet. Für den ersten Druck reichen sie.

Für Serienteile oder enge Passmaße lohnt der Durchlauf in
[Kalibrierung](docs/calibration.md) — rund 20 Minuten je Kombination, danach steht
der Eintrag auf 🟢. Den aktuellen Stand je Kombination zeigt die
[Profilmatrix](docs/matrix.md).

---

## Wenn etwas nicht stimmt

Erste Anlaufstelle ist **[Fehlerbilder](docs/troubleshooting.md)** — vom Symptom zum
Parameter, von Haftung über Fädenbildung bis Maßhaltigkeit.

| Beobachtung | Seite |
|---|---|
| Preset erscheint nicht in Studio | [Installation](docs/install.md#wenn-ein-preset-nicht-auftaucht) |
| Erste Schicht hält nicht, Ecken heben ab | [Fehlerbilder](docs/troubleshooting.md) |
| Fäden, matte Oberfläche, Knacken beim Extrudieren | [Fehlerbilder](docs/troubleshooting.md) |
| Maße stimmen nicht | [Kalibrierung → Flussrate](docs/calibration.md#schritt-2--flussrate) |
| Wände werden dünn, obwohl nichts geändert wurde | [Kalibrierung → Volumenstrom](docs/calibration.md#schritt-3--volumenstrom) |

---

## Rückmeldung geben

Jede Rückmeldung verbessert die Werte für alle — besonders von Kombinationen, die
hier noch auf 🔵 stehen.

**[→ Ein Thema eröffnen](https://github.com/aidun/printerprofiles/issues/new/choose)**

| Anlass | Was hilft |
|---|---|
| 🟢 **Werte bestätigt** | Drucker, Düse, Material, Stufe — und dass es sauber lief |
| 🔧 **Wert passt nicht** | dieselben Angaben plus der Wert, der bei dir funktioniert, und wie du ihn ermittelt hast |
| 💡 **Material fehlt** | Hersteller, genaue Produktbezeichnung, Link zum Datenblatt |
| 📖 **Doku unklar oder falsch** | die Seite und die Stelle |

Hilfreich in jedem Fall: die Version von Bambu Studio, der genaue Preset-Name
(er steht im Dateinamen) und bei Druckproblemen ein Foto.

Wer die Änderung gleich selbst einreichen möchte, findet den Weg in
[Entwicklung → Beitrag einreichen](docs/entwicklung.md#beitrag-einreichen).

---

## Dokumentation

| Seite | Inhalt |
|---|---|
| [Installation](docs/install.md) | Import in Bambu Studio, Aktualisierung, Entfernen |
| [Materialien](docs/filament/README.md) | 17 Datenblätter: Kennwerte, Volumenströme, Fallstricke |
| [Drucker](docs/drucker/README.md) | Eigenheiten der sechs Maschinen |
| [Düsenkunde](docs/nozzles.md) | Wann 0.2, wann 0.4, wann 0.6 — und warum Glow die 0.2 sperrt |
| [Profilmatrix](docs/matrix.md) | Welche Kombination existiert, mit welchen Werten, in welchem Zustand |
| [Kalibrierung](docs/calibration.md) | Temperatur, Flussrate, Volumenstrom: der Weg von 🔵 nach 🟢 |
| [Fehlerbilder](docs/troubleshooting.md) | Vom Symptom zum Parameter |
| [Entwicklung](docs/entwicklung.md) | Quelldaten, Generator, Tests — für alle, die Werte ändern |

---

## Haftung

Druckprofile greifen in Temperatur, Fluss und Geschwindigkeit ein. Die Werte sind
sorgfältig hergeleitet, aber jede Maschine, jede Düse und jede Filamentcharge ist
anders. Erster Druck mit Blick auf die erste Schicht — wie immer.
