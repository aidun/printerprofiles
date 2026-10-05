# Geeetech PETG

[← Materialübersicht](README.md) · Status: 🔵 Startwert · Basis: `Generic PETG`

PETG mit dem kühlsten Temperaturfenster der drei PETG in diesem Repository. Geeetech
nennt 220 – 230 °C, wo [eSUN](esun-petg.md) 243 °C und [SUNLU](sunlu-petg.md) 245 °C
verlangen — gut 15 °C Unterschied bei identischer Materialklasse. Das macht dieses PETG
zum schonendsten Einstieg in das Material: weniger Fäden, weniger Geruch, weniger
Belastung für die Düse. Der Durchsatz bleibt dafür der niedrigste.

---

## Kennwerte

| Größe | Wert | Abweichung zu eSUN PETG |
|---|---|---|
| Düse | **230 °C** (erste Schicht 235 °C) | −13 °C |
| Temperaturfenster | 220 – 260 °C | Untergrenze 10 °C tiefer |
| Bett | **75 °C** (erste Schicht 80 °C) | gleich |
| Glasübergang | 80 °C | +9 °C |
| Flussrate | 0.95 | gleich |
| Lüfter | **30 – 40 %** | Untergrenze höher, Obergrenze niedriger |
| Überhangkühlung | 60 % | gleich |
| Z-Hop | 0.6 mm | gleich |
| Abrasiv | nein — Messingdüse genügt | |
| Trocknung | 65 °C / 8 h | gleich |
| Lagerung | zwingend trocken | gleich |

**Das schmale Lüfterfenster ist eine Herstellerangabe.** `Generic PETG @Geeetech` gibt
30 % Mindest- und 40 % Maximalkühlung vor — zehn Prozentpunkte Spielraum, wo eSUN und
SUNLU zwischen 20 und 50 % arbeiten. Geeetech legt die Kühlung damit auf einen schmalen
Korridor fest: genug Luft, damit Überhänge nicht durchhängen, zu wenig, um die
Schichthaftung zu kosten. Für Warping-Fälle bleibt
`close_fan_the_first_x_layers = 3` der wirksamere Hebel als eine weitere Absenkung.

**Zum Glasübergang von 80 °C.** Das ist Geeetechs eigener Wert
(`temperature_vitrification = 80` in `fdm_filament_pet`) und liegt 9 bis 10 °C über dem,
was hier bei eSUN und SUNLU steht. Praktisch verhält sich PETG nicht sprunghaft: Es
beginnt deutlich vor dem Glasübergang zu kriechen. **Für die Bauteilauslegung bleibt
70 °C die ehrliche Grenze**, unabhängig davon, welche Zahl im Profil steht. Der höhere
Wert bedeutet nur, dass der Slicer Kühlstrategien etwas später greifen lässt.

**Zur Düsentemperatur.** 230 °C sind Geeetechs Obergrenze, nicht die Mitte des Fensters
— der Hersteller nennt 220 – 230 °C für sein PETG. Nach oben ist auf dem Papier Platz
bis 260 °C, weil das Grundprofil `fdm_filament_pet` so weit freigibt; wer dort hingeht,
verlässt aber die Produktangabe und sollte das bewusst tun. Der erste Griff bei
Schichthaftungsproblemen ist hier **der Lüfter**, nicht die Düse.

## Volumenstrom je Drucker und Düse

Werte in mm³/s. Basis ist der X1C; die übrigen Drucker werden über den
[Durchsatzfaktor](../drucker/README.md#durchsatzfaktoren) skaliert.

| Drucker | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| H2C | 1.1 | 11.5 | 11.5 |
| X1 Carbon | 1 | 10 | 10 |
| P1S | 0.9 | 9.5 | 9.5 |
| P1P | 0.9 | 9.5 | 9.5 |
| A1 | 0.9 | 9 | 9 |
| A1 mini | 0.8 | 8.5 | 8.5 |

> **Quelle der Werte.** Volumenstrom (10.0 mm³/s), Flussrate (0.95), Lüfterfenster und
> Glasübergang stammen aus `Generic PETG @Geeetech` und dessen Elternprofil
> `fdm_filament_pet` — Profile, die **Geeetech selbst** für Bambu Studio beigesteuert
> hat und die unter `profiles/Geeetech/filament/` liegen. Nozzle-spezifische Profile
> führt Geeetech nicht: der 0.2-mm-Wert (1.0 mm³/s) kommt aus
> `Generic PETG @0.2 nozzle` der Bambu-Bibliothek, 0.6 mm wiederholt den 0.4-mm-Wert.

> **Zu den A1-Werten.** `Generic PETG @BBL A1` und `@BBL A1M` nennen 8 mm³/s — knapp
> unter den 9 beziehungsweise 8.5, die der Durchsatzfaktor hier ergibt. Dieses PETG
> folgt damit derselben Linie wie [eSUN PETG](esun-petg.md) und
> [SUNLU PETG](sunlu-petg.md), die ebenfalls ohne `[volumetric_flow_cap]` auskommen:
> Ein Deckel steht in diesem Repository nur dort, wo ein Herstellerprofil **für genau
> dieses Material** einen niedrigeren Wert nennt — wie bei
> [Bambu PETG-CF](bambu-petg-cf.md). Die knapp 1 mm³/s Differenz zum generischen
> Basisprofil liegen innerhalb dessen, was die
> [Kalibrierung](../calibration.md#schritt-3--volumenstrom) ohnehin klärt.

**10 mm³/s sind das Schlusslicht unter den PETG hier.** [eSUN PETG](esun-petg.md) steht
bei 13, [SUNLU PETG](sunlu-petg.md) bei 14, [Bambu PETG HF](bambu-petg-hf.md) bei
21 mm³/s. Gegenüber dem High-Flow-PETG von Bambu bleibt also weniger als die Hälfte —
das ist der Preis des kühlen Fensters. Umgekehrt gilt: Bei 230 °C statt 245 °C fädelt
PETG deutlich weniger, und genau das ist bei diesem Material der häufigste Ärger.

## Wofür Geeetech PETG das richtige Material ist

| Anforderung | Wahl |
|---|---|
| Erster PETG-Druck, schonender Einstieg | **Geeetech PETG** — kühlstes Fenster, wenig Fäden |
| Wärme bis etwa 70 °C | **Geeetech PETG** — PLA kriecht schon ab 50 °C |
| Außenteile, UV und Feuchte | **Geeetech PETG** |
| Lebensmittelnahe Teile | **Geeetech PETG** — PETG, nicht ABS oder ASA |
| Hoher Durchsatz, große Teile | [Bambu PETG HF](bambu-petg-hf.md) — 21 statt 10 mm³/s |
| Steifigkeit, Maßhaltigkeit | [eSUN PETG-CF](esun-petg-cf.md) — faserverstärkt |
| Dauerhaft über 70 °C | [Bambu ASA](bambu-asa.md) oder [eSUN ABS+](esun-abs.md) |
| Durchsichtige Teile | [eSUN PETG Transparent](esun-petg-transparent.md) |

## Wenn etwas nicht stimmt

| Symptom | Zuerst prüfen |
|---|---|
| Teil bricht entlang der Schichten | **Lüfter auf 30 % festsetzen** — vor der Temperatur |
| Fäden zwischen den Teilen | trocknen; Düse auf 225 °C senken |
| Erste Schicht haftet zu gut, Platte leidet | texturierte Platte, [Haftung](../troubleshooting.md#haftung) |
| Ecken heben ab | `close_fan_the_first_x_layers` erhöhen, Bett auf 80 °C |
| Knacken an der Düse, matte Oberfläche | Feuchtigkeit — 65 °C / 8 h trocknen |
| Unterextrusion | [Volumenstrom](../calibration.md#schritt-3--volumenstrom) |
| Überhänge hängen durch | 40 % Lüfter sind die Grenze — Stützmaterial ab 50° |

---

[← Geeetech PLA Silk](geeetech-pla-silk.md) · [Materialübersicht](README.md) · [Bambu PLA Basic →](bambu-pla-basic.md)
