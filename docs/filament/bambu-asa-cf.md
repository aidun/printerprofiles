# Bambu ASA-CF

[← Materialübersicht](README.md) · Status: 🔵 Startwert · Basis: `Bambu ASA-CF`
· ⚠️ **gehärtete Düse zwingend**

Das steifste und wärmefesteste Material im Sortiment. [ASA](bambu-asa.md) mit
gemahlener Kohlenstofffaser: Glasübergang 108 °C, UV-stabil, faserverstärkt. Dafür
verlangt es alles gleichzeitig — geschlossene Kammer, Bett auf 100 °C, gehärtete
Düse und die niedrigste Flussrate des Repositories. Für Außenteile unter Dauerlast
gibt es hier keine Alternative.

---

## Kennwerte

| Größe | Wert | Abweichung zu Bambu ASA |
|---|---|---|
| Düse | **275 °C** (erste Schicht 275 °C) | +5 °C |
| Temperaturfenster | 250 – 280 °C | unten +10 °C |
| Bett | **100 °C** (erste Schicht 100 °C) | gleich |
| Glasübergang | **108 °C** | **+8 °C** |
| Flussrate | **0.90** | **−0.05** |
| Lüfter | **10 – 25 %** | Obergrenze niedriger |
| Überhangkühlung | 80 % | gleich |
| Z-Hop | 0.6 mm | gleich |
| Abrasiv | **ja — gehärtete Düse zwingend** | |
| Trocknung | 80 °C / 8 h | gleich |
| Lagerung | trocken mit Silikagel | Faseranteil nimmt kaum Wasser auf |

**Flussrate 0.90 ist der niedrigste Wert im Repository.** Die Fasern verdrängen
Polymer: bei gleichem Vorschub kommt weniger schmelzfähige Masse aus der Düse. Der
Wert stammt unverändert aus Bambus Profil und ist keine Vorsichtsmarge dieses
Repositories.

**108 °C Glasübergang sind die eigentliche Besonderheit.** Alle übrigen
Kammermaterialien liegen bei 100 °C. Die 8 °C klingen nach wenig, entscheiden aber
darüber, ob ein Teil direkt an einem Motor oder in einem geschlossenen schwarzen
Gehäuse in der Sonne noch maßhaltig bleibt.

## Zur gehärteten Düse — bewusste Abweichung vom Herstellerprofil

> Bambus eigenes Profil setzt `required_nozzle_HRC = 3` und erklärt ASA-CF damit für
> Messingdüsen freigegeben. Bei [Bambu PETG-CF](bambu-petg-cf.md) — demselben
> Fasertyp in einer anderen Matrix — fordert derselbe Hersteller **40**.
>
> Das ist eine Inkonsistenz der Bibliothek, keine Materialeigenschaft: gemahlene
> Kohlenstofffaser schleift Messing, unabhängig vom Trägerpolymer. Dieses
> Repository folgt deshalb nicht dem Profil, sondern der Physik und führt
> `abrasive = true`. Die 0.2-mm-Düse bleibt gesperrt. Ein Test hält beides fest,
> damit die Abweichung nicht beim nächsten Bibliotheks-Update stillschweigend
> verschwindet.

## Volumenstrom je Drucker und Düse

Werte in mm³/s. Basis ist der X1C; die übrigen Drucker werden über den
[Durchsatzfaktor](../drucker/README.md#durchsatzfaktoren) skaliert.

| Drucker | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| H2C | — | 20.7 | 20.7 |
| X1 Carbon | — | 18 | 18 |
| P1S | — | 17.1 | 17.1 |
| P1P | — | 17.1 | 17.1 |
| A1 | — | 16.2 | 16.2 |
| A1 mini | — | — | — |

> **Quelle der Werte.** Aus `Bambu ASA-CF @BBL X1C`: 18 mm³/s — und zwar auf
> **beiden** Extrudervarianten und bei **beiden** Düsen. Das ist die Ausnahme in
> diesem Repository: sonst gibt der High-Flow-Extruder mehr frei. Hier begrenzt der
> Faseranteil, nicht die Bohrung und nicht das Hotend.

> **Warum 0.2 mm fehlt.** Für kein faserverstärktes Material der Bibliothek gibt es
> ein 0.2-mm-Profil; die Faserlänge liegt in der Größenordnung der Bohrung. Siehe
> [Bambu PETG-CF](bambu-petg-cf.md#volumenstrom-je-drucker-und-düse).

> **Warum die A1 mini leer bleibt.** Wie bei [ABS](bambu-abs.md) und
> [ASA](bambu-asa.md) liefert Bambu für dieses Gerät kein Basisprofil.

**Der Durchsatz ist überraschend gut.** 18 mm³/s entsprechen genau dem von
[ASA](bambu-asa.md) — die Faser kostet hier keinen Durchsatz, nur Flussrate und
Zähigkeit. Gegenüber [PETG-CF](bambu-petg-cf.md) mit 11.5 mm³/s ist ASA-CF sogar
das deutlich schnellere faserverstärkte Material.

## Wofür ASA-CF das richtige Material ist

| Anforderung | Wahl |
|---|---|
| Außenteil unter Dauerlast | **ASA-CF** — UV-stabil, steif, 108 °C |
| Höchste Steifigkeit im Sortiment | **ASA-CF** |
| Dauerhaft über 100 °C | **ASA-CF** — als einziges hier |
| Maßhaltigkeit bei Temperaturwechsel | **ASA-CF** — Faser bremst den Schrumpf |
| Faserverstärkung ohne Kammer | [Bambu PETG-CF](bambu-petg-cf.md) |
| Schlagbelastung, Stürze | [Bambu ASA](bambu-asa.md) — CF bricht spröde |
| Sichtbare Außenflächen in Farbe | ASA — CF ist immer mattschwarz |

**Faser bremst das Warping, beseitigt es nicht.** Der Faseranteil senkt die
Wärmedehnung messbar, weshalb große ASA-CF-Teile tatsächlich weniger stark ziehen
als große ASA-Teile. Die geschlossene Kammer bleibt trotzdem Pflicht — die
Schichthaftung hängt an der warmen Umgebungsluft, nicht am Schrumpf.

**Spröde bleibt spröde.** Wie jedes faserverstärkte Material nimmt ASA-CF Stoß
schlecht auf. Ein Teil, das fallen oder anschlagen kann, gehört in normales ASA.

## Wenn etwas nicht stimmt

| Symptom | Zuerst prüfen |
|---|---|
| Außenwände zu breit, Maße wachsen | Düse vermessen — abgenutzte Messingdüse |
| Düse setzt sich zu | Material trocknen, 0.4 mm als Minimum einhalten |
| Teil bricht spröde | Materialwahl — [ASA](bambu-asa.md) statt ASA-CF |
| Riss quer durch das Teil | Kammer wärmer halten, Lüfter auf 10 % |
| Erste Schicht haftet nicht | Bett wirklich auf 100 °C? Platte entfetten |
| Unterextrusion | [Volumenstrom](../calibration.md#schritt-3--volumenstrom), Flussrate 0.90 beachten |
| Raue, pelzige Oberfläche | Feuchtigkeit — 80 °C / 8 h trocknen |

---

[← Bambu ASA](bambu-asa.md) · [Materialübersicht](README.md)
