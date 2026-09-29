# Düsenkunde

[← Zurück zur Übersicht](../README.md)

Der Düsendurchmesser ist die folgenreichste Entscheidung vor dem Druck. Er bestimmt,
wie fein ein Teil werden kann, wie lange es dauert und wie fest es wird — und er
entscheidet, ob ein Material überhaupt durchgeht.

---

## Die drei Durchmesser im Vergleich

| | **0.2 mm** | **0.4 mm** | **0.6 mm** |
|---|---|---|---|
| **Stärke** | feinste Details | der Allrounder | Tempo und Festigkeit |
| **Schichthöhen** | 0.06 – 0.14 mm | 0.08 – 0.28 mm | 0.12 – 0.42 mm |
| **Volumenstrom** | ~3 mm³/s | ~14 mm³/s | ~19 mm³/s |
| **Zeit für dasselbe Teil** | ≈ 4 × | Referenz | ≈ 0,5 × |
| **Kleinste sinnvolle Wandstärke** | 0.4 mm | 0.8 mm | 1.2 mm |
| **Verstopfungsrisiko** | hoch | gering | sehr gering |
| **Geeignet für Glow** | ❌ nein | ✅ ja | ✅ ja |

Die Volumenstromangaben beziehen sich auf PLA am X1 Carbon. Die genauen Werte je
Kombination stehen in der [Profilmatrix](matrix.md).

---

## Wann welche Düse

### 0.2 mm — wenn Details wichtiger sind als Zeit

Miniaturen, Zahnräder unter 20 mm, Schriftzüge, Beschriftungen, feine Gitter.
Eine 0.2er Düse löst Kanten auf, die eine 0.4er zusammenzieht.

Der Preis ist hoch: der Volumenstrom fällt auf etwa ein Fünftel, der Druck dauert
ein Vielfaches, und die Düse reagiert empfindlich auf jede Verunreinigung im
Filament. Für Teile über 100 mm Kantenlänge ist sie praktisch unbrauchbar.

> **Nicht mit Glow-Material.** Siehe unten.

### 0.4 mm — die Standardwahl

Deckt den größten Teil aller Anwendungen ab. Gute Balance aus Auflösung, Tempo und
Robustheit, und der Durchmesser, für den Bambu die meisten Profile abgestimmt hat.
Im Zweifel diese.

### 0.6 mm — wenn Tempo oder Festigkeit zählen

Funktionsteile, Halterungen, Gehäuse, große Flächen, alles über 150 mm. Die dickere
Extrusionsbahn verschweißt besser mit der Nachbarbahn — Teile aus einer 0.6er Düse
sind bei gleicher Wandzahl deutlich fester als aus einer 0.4er.

Die Grenze liegt bei der Detailauflösung: alles unter etwa 1.5 mm Wandstärke lässt
sich nicht mehr sauber abbilden.

---

## Gehärtete Düsen und abrasives Material

Bambus Serienmessing-Düse ist weich. Sie hält bei PLA und PETG tausende Stunden —
und bei gefülltem Material wenige.

**Glow-Filament ist gefülltes Material.** Das Leuchtpigment ist Strontiumaluminat:
ein Kristall mit einer Mohs-Härte um 6, deutlich härter als Messing. Jedes Korn,
das durch die Düse geht, trägt einen Bruchteil davon ab. Nach ein bis zwei Spulen
ist die Bohrung messbar aufgeweitet, die Extrusion wird unpräzise, Wände werden zu
dick, Maße stimmen nicht mehr.

| Material | Düse | Begründung |
|---|---|---|
| SUNLU PLA | Messing genügt | ungefüllt |
| SUNLU PETG | Messing genügt | ungefüllt |
| SUNLU PLA Glow | **gehärtet zwingend** | Strontiumaluminat |
| SUNLU PETG Glow | **gehärtet zwingend** | Strontiumaluminat |

Bambu liefert die gehärtete Variante unter der Bezeichnung *Hardened Steel* für alle
drei Durchmesser. Bei den Profilen dieses Repositories macht die Düsenhärte keinen
Unterschied in den Werten — sie entscheidet nur über die Lebensdauer.

### Warum 0.2 mm bei Glow gesperrt ist

Nicht der Verschleiß ist das Problem, sondern die Korngröße. Die Pigmentpartikel
liegen in der Größenordnung von 20 – 50 µm. In einer 0.4-mm-Bohrung ist das
unkritisch. In einer 0.2-mm-Bohrung ist ein einzelnes größeres Agglomerat genug,
um den Querschnitt zuzusetzen — und die Verstopfung sitzt so fest, dass in der Regel
nur der Düsenwechsel hilft.

Dieses Repository liefert deshalb **keine Glow-Profile für 0.2 mm**. Das ist eine
bewusste Auslassung, kein Versehen: Die Kombination lässt sich technisch einstellen,
aber nicht zuverlässig drucken.

---

## Düsenwechsel

Nach jedem Wechsel:

1. **In Bambu Studio umstellen.** Druckereinstellungen → Düsendurchmesser. Ohne
   diesen Schritt rechnet der Slicer mit der falschen Bahnbreite.
2. **Profile neu wählen.** Filament- und Prozessprofil der alten Düse verschwinden
   aus der Liste, die der neuen erscheinen. Das ist das gewünschte Verhalten.
3. **Kalibrieren.** Beim H2C läuft die induktive Düsenversatzkalibrierung
   automatisch. Bei allen anderen Modellen mindestens die automatische
   Bett-Nivellierung neu starten.
4. **Flussrate prüfen.** Eine neue Düse hat eine andere effektive Bohrung als eine
   eingelaufene. Bei Präzisionsteilen lohnt der Durchlauf aus
   [docs/calibration.md](calibration.md).

---

## Zusammenspiel mit der Qualitätsstufe

Schichthöhe und Düsendurchmesser sind aneinander gekoppelt. Über etwa 75 % des
Durchmessers verschweißen die Schichten nicht mehr zuverlässig, unter etwa 25 %
wird die Extrusion instabil. Alle Profile dieses Repositories bleiben in diesem
Fenster — der Validator prüft es bei jedem Lauf.

| Düse | Qualität | Normal | Schnell |
|---|---|---|---|
| 0.2 mm | 0.08 mm | 0.12 mm | 0.14 mm |
| 0.4 mm | 0.12 mm | 0.20 mm | 0.28 mm |
| 0.6 mm | 0.18 mm | 0.30 mm | 0.42 mm |

Der H2C weicht davon in der Stufe *Schnell* ab: Bambu gibt für ihn keine so groben
Schichten frei. Die tatsächlich gesetzten Werte stehen in der
[Profilmatrix](matrix.md).

---

[← Zurück zur Übersicht](../README.md) · [Kalibrierung →](calibration.md)
