# Fehlerbilder

[← Zurück zur Übersicht](../README.md)

Vom Symptom zum Parameter. Jeder Eintrag nennt die wahrscheinlichste Ursache zuerst
und sagt, welcher Wert in `src/` anzupassen ist.

---

## Schnellzuordnung

| Symptom | Wahrscheinlichste Ursache | Abschnitt |
|---|---|---|
| Erste Schicht haftet nicht | Bett zu kalt, Düse zu hoch | [Haftung](#haftung) |
| Ecken heben ab | Kühlung zu stark, Bett zu kalt | [Warping](#warping) |
| Feine Fäden zwischen den Teilen | zu heiß, Einzug zu kurz | [Fädenbildung](#fädenbildung) |
| Wände zu dünn, Löcher in der Oberfläche | Unterextrusion | [Unterextrusion](#unterextrusion) |
| Teil lässt sich in Schichten trennen | zu kalt, Kühlung zu stark | [Schichthaftung](#schichthaftung) |
| Maße stimmen nicht | Flussrate falsch | [Maßhaltigkeit](#maßhaltigkeit) |
| Knacken beim Druck, Blasen im Material | Filament feucht | [Feuchtigkeit](#feuchtigkeit) |
| Überhänge hängen durch | zu heiß, zu wenig Kühlung | [Überhänge](#überhänge) |
| Druck bricht ab, Extruder klickt | Verstopfung | [Verstopfung](#verstopfung) |

---

## Haftung

Die erste Schicht löst sich während des Drucks oder haftet gar nicht erst.

**Prüfen, in dieser Reihenfolge**

1. **Platte sauber?** Fett von Fingerabdrücken ist die häufigste Ursache. Mit
   Isopropanol abreiben, nicht mit Spülmittel.
2. **Richtige Platte im Slicer gewählt?** Die Profile setzen Temperaturen für alle
   vier Plattentypen getrennt. Eine Textured PEI mit den Werten der Cool Plate
   haftet schlecht.
3. **Bett-Temperatur.** In `src/filaments/<material>.toml` unter
   `[temperature] bed_initial`. PLA 60 °C, PETG 75 °C sind die Startwerte —
   je 5 °C nach oben ist unkritisch.
4. **Z-Versatz.** Automatische Bett-Nivellierung neu starten.

> PETG haftet auf glatten PEI-Platten mitunter **zu gut** und reißt beim Ablösen
> Material aus der Beschichtung. Hier hilft die texturierte Platte oder ein
> Trennmittel — nicht mehr Temperatur.

---

## Warping

Ecken heben sich während des Drucks vom Bett ab, das Teil verzieht sich.

| Maßnahme | Parameter | Wirkung |
|---|---|---|
| Kühlung der ersten Schichten aus | `[kuehlung] close_fan_the_first_x_layers` erhöhen | stark |
| Bett wärmer | `[temperature] bed` +5 °C | stark |
| Brim im Slicer aktivieren | — | stark |
| Kammer geschlossen halten | — | beim H2C, X1C und P1S entscheidend |
| Lüfter insgesamt drosseln | `[kuehlung] fan_max_speed` senken | mittel |

PETG neigt deutlich stärker zum Verzug als PLA. Die Profile tragen dem bereits
Rechnung: PETG startet mit 10 – 30 % Lüfterleistung, PLA mit 60 – 100 %.

---

## Fädenbildung

Feine Fäden zwischen getrennten Bereichen des Teils.

1. **Temperatur senken.** `[temperature] nozzle` in 5-°C-Schritten. Wirkt am
   stärksten und ist der erste Griff.
2. **Z-Hop erhöhen.** `[retraction] z_hop`. PETG steht bei 0.6 mm, PLA bei 0.4 mm.
3. **Filament trocknen.** Feuchtes Material fädelt unabhängig von allen
   Einstellungen — siehe [Feuchtigkeit](#feuchtigkeit).

PETG fädelt grundsätzlich mehr als PLA. Ein vollständig fädenfreier PETG-Druck ist
die Ausnahme; nachträgliches Abflammen oder Abziehen ist üblich.

---

## Unterextrusion

Wände werden dünner als geplant, in Deckflächen bleiben Lücken, die Oberfläche wirkt
gerippt.

**Häufigste Ursache: der Volumenstrom ist zu hoch eingetragen.** Das klingt
widersinnig, ist aber der Normalfall — das Hotend kann nicht so viel Material
aufschmelzen, wie der Slicer annimmt, und fördert entsprechend weniger.

| Prüfen | Wo |
|---|---|
| Volumenstrom messen | [Kalibrierung, Schritt 3](calibration.md#schritt-3--volumenstrom) |
| Temperatur zu niedrig | `[temperature] nozzle` +5 °C |
| Flussrate zu niedrig | [Kalibrierung, Schritt 2](calibration.md#schritt-2--flussrate) |
| Düse teilweise verstopft | [Verstopfung](#verstopfung) |
| Düse verschlissen | bei Glow-Material nach ein bis zwei Spulen normal |

---

## Schichthaftung

Das Teil lässt sich entlang der Schichten trennen, bricht bei geringer Belastung.

1. **Temperatur erhöhen.** `[temperature] nozzle` in 5-°C-Schritten bis an die
   Obergrenze des Fensters. Wirkt am stärksten.
2. **Kühlung drosseln.** `[kuehlung] fan_max_speed` senken. Bei PETG ist die
   Kühlung der häufigere Schuldige als die Temperatur.
3. **Schichthöhe verringern.** Die Stufe *Qualität* statt *Schnell* wählen —
   dünnere Schichten verschweißen besser.
4. **Wandzahl erhöhen.** In `src/quality.toml` unter `[<level>.parameters]`
   `wall_loops`.

---

## Maßhaltigkeit

Bohrungen zu eng, Außenmaße zu groß, Passungen klemmen.

Das ist fast immer die **Flussrate**, nicht die Temperatur. Der Ablauf steht in
[Kalibrierung, Schritt 2](calibration.md#schritt-2--flussrate) und dauert rund
zehn Minuten.

Bleibt der Fehler nach der Kalibrierung bestehen:

| Beobachtung | Ursache |
|---|---|
| Bohrungen zu eng, Außenmaße stimmen | normaler Effekt der Bahnbreite — im CAD kompensieren |
| alle Maße gleichmäßig zu groß | Flussrate weiterhin zu hoch |
| Maße stimmen unten, nicht oben | Warping oder Wärmeverzug, siehe [Warping](#warping) |
| Maße schwanken zwischen Drucken | Filament feucht oder Düse verschlissen |

---

## Feuchtigkeit

**Erkennungszeichen:** hörbares Knacken oder Zischen während der Extrusion, Blasen
im extrudierten Strang, matte statt glänzender Oberfläche, plötzlich starke
Fädenbildung bei unveränderten Einstellungen.

| Material | Trocknung | Empfindlichkeit |
|---|---|---|
| SUNLU PLA | 45 °C / 6 h | gering |
| SUNLU PLA Glow | 45 °C / 6 h | gering |
| SUNLU PETG | 65 °C / 8 h | **hoch** |
| SUNLU PETG Glow | 65 °C / 8 h | **hoch** |

PETG zieht innerhalb weniger Tage offener Lagerung so viel Wasser, dass der Druck
sichtbar leidet. Silikagel im Trockenbehälter ist bei diesem Material keine
Empfehlung, sondern Voraussetzung.

Keine Einstellung gleicht feuchtes Filament aus. Erst trocknen, dann weitersuchen.

---

## Überhänge

Überhängende Kanten hängen durch, die Unterseite wird rauh.

| Maßnahme | Parameter |
|---|---|
| Überhangkühlung erhöhen | `[kuehlung] overhang_fan_speed` |
| Temperatur senken | `[temperature] nozzle` −5 °C |
| Mindestschichtzeit erhöhen | `[kuehlung] slow_down_layer_time` |
| Schichthöhe verringern | Stufe *Qualität* wählen |
| Teil anders ausrichten | im Slicer |

Bei PETG sind die Kühlwerte bewusst niedrig gehalten, weil das Material sonst die
Schichthaftung verliert. Überhänge über etwa 50° brauchen dort Stützmaterial.

---

## Verstopfung

Der Extruder klickt, es kommt kein oder zu wenig Material.

**Bei Glow-Material zuerst prüfen:** Ist eine gehärtete Düse verbaut? Wird eine
0.2-mm-Düse verwendet? Letzteres ist die häufigste Ursache überhaupt und der Grund,
warum dieses Repository keine Glow-Profile für 0.2 mm ausliefert — Einzelheiten in
der [Düsenkunde](nozzles.md#warum-02-mm-bei-glow-gesperrt-ist).

**Weiteres Vorgehen**

1. Düse auf Drucktemperatur bringen und von Hand Filament durchdrücken.
2. Hilft das nicht: Cold Pull mit PLA bei 90 °C.
3. Hilft das nicht: Düse wechseln.
4. Nach dem Wechsel Bett-Nivellierung und Flussrate neu prüfen.

Wiederholte Verstopfungen bei unverändertem Material deuten auf eine verschlissene
oder verformte Düse hin.

---

## Wenn nichts davon passt

```bash
python3 tools/validate.py
```

Der Validator prüft alle Presets gegen die Profilbibliothek von Bambu Studio und
meldet, was Studio sonst stillschweigend verwirft: fehlende Elternprofile,
unbekannte Schlüssel, falsche Arraylängen, Schichthöhen außerhalb der
Maschinengrenzen, Temperaturen über dem Hotend-Limit.

Bleibt der Fehler, hilft der Vergleich mit dem unveränderten Bambu-Profil: dasselbe
Teil einmal mit `Generic PLA` oder `Generic PETG` slicen. Tritt das Problem dort
ebenfalls auf, liegt es nicht an diesen Profilen.

---

[← Kalibrierung](calibration.md) · [Zurück zur Übersicht](../README.md)
