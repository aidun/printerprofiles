# Kalibrierung

[← Zurück zur Übersicht](../README.md)

Der Weg von 🔵 **Startwert** zu 🟢 **verifiziert**. Drei Messungen, rund 20 Minuten
je Kombination aus Material, Drucker und Düse. Danach sind die Profile nicht mehr
hergeleitet, sondern gemessen.

---

## Warum überhaupt

Die Startwerte dieses Repositories gehen von Bambus eigenen, abgestimmten Werten aus
und rechnen sie über die Hotend-Leistung des jeweiligen Druckers um. Das trifft die
Größenordnung zuverlässig. Was es nicht erfassen kann:

- **Chargenstreuung.** Der Durchmesser einer Filamentrolle schwankt um ±0.02 mm.
  Das sind bis zu 3 % Materialmenge.
- **Düsenzustand.** Eine eingelaufene Düse fördert anders als eine neue.
- **Feuchtigkeit.** Feuchtes PETG braucht eine andere Temperatur als trockenes.
- **Umgebung.** Ein H2C mit beheizter Kammer kühlt anders als ein offener A1.

Für einen Prototypen ist das egal. Für ein Passmaß von 0.1 mm nicht.

---

## Reihenfolge

Die drei Messungen bauen aufeinander auf. Wer die Reihenfolge tauscht, misst
Fehler, die aus dem vorherigen Schritt stammen.

```
1. Temperatur   →   2. Flussrate   →   3. Volumenstrom
   Turm             Würfel             Bahnentest
```

---

## Schritt 1 — Temperatur

**Ziel:** die niedrigste Temperatur, bei der die Schichten noch sauber verschweißen.
Jedes Grad darüber kostet Oberflächengüte und Maßhaltigkeit, jedes Grad darunter
Festigkeit.

**Vorgehen**

1. Einen Temperaturturm slicen — Bambu Studio bringt unter
   *Kalibrierung → Temperatur* eine passende Vorlage mit.
2. Das Fenster aus dem [Materialdatenblatt](filament/README.md) als Bereich eintragen,
   Schrittweite 5 °C.
3. Nach dem Druck von oben nach unten beurteilen.

**Bewertung**

| Beobachtung | Bedeutung |
|---|---|
| Fäden zwischen den Stufen, glänzende Oberfläche | zu heiß |
| Ecken hängen durch, Überhänge tropfen | zu heiß |
| Stufen lassen sich mit der Hand auseinanderziehen | zu kalt |
| Matte Oberfläche, rauhe Kanten | zu kalt |
| Schichten fest verbunden, Kanten scharf, keine Fäden | **Treffer** |

Den gefundenen Wert in `src/filamente/<material>.toml` unter `[temperatur] nozzle`
eintragen. Die erste Schicht liegt üblicherweise 5 °C darüber.

---

## Schritt 2 — Flussrate

**Ziel:** die Materialmenge so einstellen, dass die gedruckte Wand genau so dick wird
wie geplant. Das ist der Parameter mit dem größten Einfluss auf die Maßhaltigkeit.

**Vorgehen**

1. Einen Kalibrierwürfel mit **einer** Wandlinie und **ohne** Deckel drucken —
   40 × 40 × 10 mm, `wall_loops = 1`, `top_shell_layers = 0`, Füllung 0 %.
2. Nach dem Druck die Wandstärke an vier Stellen messen, Mittelwert bilden.
3. Neue Flussrate berechnen:

```
neue Flussrate = alte Flussrate × (Sollwandstärke ÷ gemessene Wandstärke)
```

**Beispiel** · 0.4-mm-Düse, Sollwandstärke 0.42 mm, gemessen 0.44 mm,
bisherige Flussrate 0.98:

```
0.98 × (0.42 ÷ 0.44) = 0.936  →  0.94
```

**Plausibilitätsgrenzen**

| Ergebnis | Bewertung |
|---|---|
| 0.94 – 1.02 | normal |
| 0.90 – 0.94 | auffällig, aber möglich — Filamentdurchmesser prüfen |
| unter 0.90 oder über 1.05 | Messfehler oder mechanisches Problem. Nicht übernehmen. |

Der Wert gehört in `src/filamente/<material>.toml` unter `[fluss] ratio`.

> Bambu Studio bringt unter *Kalibrierung → Durchflussdynamik* eine eigene,
> automatische Messung mit. Sie kalibriert allerdings den Druckvorschub, nicht die
> Materialmenge — sie ersetzt diesen Schritt nicht, sondern ergänzt ihn.

---

## Schritt 3 — Volumenstrom

**Ziel:** die Obergrenze finden, ab der das Hotend nicht mehr nachschmelzen kann.
Wird sie überschritten, fördert der Extruder weniger Material als der Slicer
annimmt — die Wände werden dünn, ohne dass sich an den Einstellungen etwas ändert.

**Wichtig:** Der Volumenstrom ist eine **Obergrenze**, kein Sollwert. Bambu Studio
drosselt die Druckgeschwindigkeit genau dann, wenn die Geometrie mehr fordern würde.
Ein zu hoher Eintrag führt nicht zu schnellerem Druck, sondern zu Unterextrusion.

**Vorgehen**

1. In Bambu Studio *Kalibrierung → Maximaler Volumenstrom* öffnen.
2. Als Bereich das Anderthalbfache des Startwerts aus der [Matrix](matrix.md)
   nach oben und die Hälfte nach unten wählen.
3. Den Test drucken und die Stelle suchen, an der die Oberfläche einbricht.
4. Vom letzten sauberen Abschnitt **15 % Sicherheitsabstand** abziehen.

**Beispiel** · Startwert 12.6 mm³/s, Einbruch bei 16 mm³/s, letzter sauberer
Abschnitt 15 mm³/s:

```
15 × 0.85 = 12.75  →  12.8 mm³/s
```

### Gemessenen Wert zurückrechnen

Der Wert gehört in `src/filamente/<material>.toml` unter `[volumenstrom]`. Achtung:
dort steht der **Basiswert bezogen auf den X1 Carbon**, nicht der gemessene Wert.
Umrechnung über den Leistungsfaktor des Druckers aus `src/drucker.toml`:

```
Basiswert = gemessener Wert ÷ flow_factor
```

Für den H2C (`flow_factor = 1.15`): `12.8 ÷ 1.15 = 11.1`

---

## Ergebnis übernehmen

```bash
# 1. Werte in src/filamente/<material>.toml eintragen
# 2. Neu erzeugen und prüfen
python3 tools/generate.py
python3 tools/validate.py
python3 tools/dokumentation.py
# 3. Status auf verifiziert setzen
```

Den Reifegrad markiert das Feld `status` in derselben Datei. Es trägt die Kennung
der verifizierten Kombination, etwa `validated-h2c-04`. Ist eine weitere Kombination
gemessen, gehört sie hier ergänzt — und anschließend in die
[Profilmatrix](matrix.md), die sich aus diesem Feld speist.

Zum Schluss neu importieren: [Installation → Aktualisieren](install.md#aktualisieren).

---

## Wie oft

| Anlass | Erneut messen |
|---|---|
| neue Filamentcharge desselben Herstellers | Flussrate |
| anderer Hersteller | alle drei Schritte |
| Düsenwechsel | Flussrate, Volumenstrom |
| nach längerer Lagerung | Temperatur — vorher trocknen |
| Maße stimmen plötzlich nicht mehr | Flussrate, danach Düse auf Verschleiß prüfen |

---

[← Düsenkunde](nozzles.md) · [Zurück zur Übersicht](../README.md) · [Fehlerbilder →](troubleshooting.md)
