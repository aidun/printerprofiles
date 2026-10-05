# Installation

[← Zurück zur Übersicht](../README.md)

Bambu Studio kennt zwei Wege, fremde Presets aufzunehmen: den Import über das Menü
und das direkte Ablegen im Benutzerordner. Der erste Weg ist der empfohlene — er
prüft die Dateien und ordnet sie richtig ein.

---

## Voraussetzungen

| | |
|---|---|
| **Bambu Studio** | Version 2.7 oder neuer |
| **Drucker** | mindestens einmal in Studio eingerichtet |
| **Düse** | die passende Düse muss im Druckerprofil hinterlegt sein |

> Ein Filamentprofil für die 0.6-mm-Düse taucht nicht auf, solange in Studio noch
> die 0.4-mm-Düse eingestellt ist. Das ist gewollt: jedes Profil ist an genau eine
> Drucker-Düsen-Kombination gebunden und erscheint nur dort.

---

## Weg 1 — Import über das Menü

**1. Presets auswählen.** Aus der [Profilmatrix](matrix.md) ablesen, welche
Kombination gebraucht wird, und die Dateien heraussuchen:

```
dist/filament/SUNLU PETG Glow H2C 0.4.json     ← das Material
dist/process/Qualität H2C 0.4.json             ← die Qualitätsstufe
```

Beide gehören zusammen: Das Filamentprofil bringt Temperatur und Fluss mit, das
Prozessprofil die Geometrie. Für einen vollständigen Druck werden beide gebraucht.

**2. Importieren.** In Bambu Studio:

```
Datei → Import → Import-Konfiguration …   (⌘/Strg + I)
```

Mehrfachauswahl ist möglich — es lassen sich alle benötigten Dateien in einem
Durchgang auswählen.

**3. Auswählen.** Nach dem Import erscheinen die Profile in den Auswahllisten
rechts im Slicer, erkennbar an ihrem Namen:

| Liste | Eintrag |
|---|---|
| Filament | `SUNLU PETG Glow H2C 0.4` |
| Prozess | `Qualität H2C 0.4` |

**4. Prüfen.** Ein Blick auf die übernommenen Werte:

- Düsentemperatur und Bett-Temperatur entsprechen dem [Materialdatenblatt](filament/README.md)
- Der maximale Volumenstrom entspricht dem Wert aus der [Matrix](matrix.md)
- Die Schichthöhe entspricht der Stufe

Weicht etwas ab, wurde vermutlich das falsche Profil erwischt oder in Studio ist
eine andere Düse eingestellt.

---

## Weg 2 — Direkt in den Benutzerordner

Schneller, wenn viele Presets auf einmal übernommen werden sollen. Bambu Studio muss
dabei **geschlossen** sein.

Der Benutzerordner liegt hier:

| System | Pfad |
|---|---|
| macOS | `~/Library/Application Support/BambuStudio/user/<ID>/` |
| Windows | `%APPDATA%\BambuStudio\user\<ID>\` |
| Linux | `~/.config/BambuStudio/user/<ID>/` |

`<ID>` ist die numerische Kennung des angemeldeten Bambu-Kontos — im Ordner liegt
in der Regel nur eine.

```bash
# macOS — der Pfad enthält ein Leerzeichen und ein *, deshalb die Schleife
for ZIEL in ~/Library/Application\ Support/BambuStudio/user/*/; do
  cp dist/filament/*.json "$ZIEL/filament/"
  cp dist/process/*.json  "$ZIEL/process/"
done
```

Beim nächsten Start liest Studio die Dateien ein.

> ⚠️ Studio legt neben jedem Preset eine `.info`-Datei mit einer internen Kennung an.
> Werden Presets auf diesem Weg kopiert, fehlt sie — Studio erzeugt sie selbst.
> Die Cloud-Synchronisation überträgt solche Presets allerdings **nicht** auf andere
> Geräte. Wer die Profile auf mehreren Rechnern braucht, nimmt Weg 1.

---

## Aktualisieren

Wurde ein Wert in `src/` geändert und neu generiert, ist der Ablauf derselbe wie beim
ersten Import. Studio fragt beim gleichnamigen Preset nach:

| Antwort | Wirkung |
|---|---|
| **Überschreiben** | der richtige Weg — das vorhandene Preset wird ersetzt |
| **Umbenennen** | erzeugt eine Kopie mit Zählersuffix; danach liegen zwei Varianten vor |

Nach dem Überschreiben lohnt ein Blick in die geöffnete Platte: Studio behält die
Auswahl bei, übernimmt aber die neuen Werte erst beim nächsten Slice.

---

## Entfernen

In Bambu Studio rechts in der Auswahlliste auf das Zahnrad neben dem Preset, dann
**Preset löschen**. Systemprofile lassen sich nicht löschen — eigene Presets schon.

Beim direkten Weg genügt das Löschen der JSON- und `.info`-Datei im Benutzerordner
bei geschlossenem Studio.

---

## Wenn ein Preset nicht auftaucht

| Beobachtung | Ursache | Abhilfe |
|---|---|---|
| Preset fehlt in der Liste | falsche Düse im Druckerprofil eingestellt | Düse in den Druckereinstellungen umstellen |
| Preset fehlt nach dem Kopieren | Studio lief während des Kopierens | Studio schließen, erneut kopieren, starten |
| Import bricht ab | Datei beschädigt oder unvollständig | `python3 tools/validate.py` ausführen |
| Prozessprofil grau hinterlegt | Filament und Prozess passen nicht zur selben Düse | beide aus derselben Zeile der [Matrix](matrix.md) wählen |
| Werte weichen vom Datenblatt ab | anderes Preset ausgewählt oder überschrieben | Preset löschen und neu importieren |

---

[← Zurück zur Übersicht](../README.md) · [Profilmatrix →](matrix.md)
