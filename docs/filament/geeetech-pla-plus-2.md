# Geeetech PLA+ 2.0

[← Materialübersicht](README.md) · Status: 🔵 Startwert · Basis: `Generic PLA`

Zähmodifiziertes PLA der zweiten Generation und der Einstieg in das Geeetech-Sortiment.
Geeetech fährt sein PLA auffällig kühl — 200 °C, wo andere Hersteller 215 bis 220 °C
nennen —, und das zieht sich durch alle vier Materialien dieser Marke. Für dieses
Preset bedeutet das die niedrigste Düsentemperatur aller PLA-Varianten hier, bei
unverändert gutmütigem Druckverhalten.

---

## Kennwerte

| Größe | Wert | Abweichung zu eSUN PLA+ |
|---|---|---|
| Düse | **210 °C** (erste Schicht 215 °C) | −10 °C |
| Temperaturfenster | 195 – 230 °C | durchgehend 5 °C kühler |
| Bett | **60 °C** (erste Schicht 65 °C) | gleich |
| Glasübergang | 60 °C | +5 °C |
| Flussrate | 0.98 | gleich |
| Lüfter | **60 – 100 %** | Obergrenze 10 Punkte höher |
| Überhangkühlung | 100 % | gleich |
| Z-Hop | 0.4 mm | gleich |
| Abrasiv | nein — Messingdüse genügt | |
| Trocknung | 45 °C / 6 h | gleich |
| Lagerung | trocken mit Silikagel | gleich |

**Zur Düsentemperatur — und woher die 210 °C kommen.** Für das PLA+ 2.0 gibt es
**kein produktspezifisches Datenblatt**. Was es gibt, ist Geeetechs eigenes
Druckerprofil in Bambu Studio: `Generic PLA @Geeetech` nennt 200 °C und 205 °C für die
erste Schicht. Der Zähmodifikator des PLA+ erhöht die Schmelzviskosität, also fährt
dieses Preset **bewusst 10 °C heißer** als die Herstellerangabe — immer noch deutlich
innerhalb des Fensters 190 – 230 °C, das Geeetechs Grundprofil `fdm_filament_pla`
freigibt. Diese +10 °C sind die einzige Entscheidung dieses Repositories an diesem
Material; alles andere ist übernommen.

**Zum Glasübergang.** 60 °C statt der 55 °C, die hier bei SUNLU und eSUN stehen —
auch das ist Geeetechs eigener Wert (`temperature_vitrification = 60`). Praktisch
heißt das: etwas mehr Luft nach oben als bei anderem PLA, aber keine Wärmebeständigkeit.
Über 50 °C Dauerbelastung gehört ein Teil aus PETG.

## Volumenstrom je Drucker und Düse

Werte in mm³/s. Basis ist der X1C; die übrigen Drucker werden über den
[Durchsatzfaktor](../drucker/README.md#durchsatzfaktoren) skaliert.

| Drucker | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| H2C | 1.8 | 13.8 | 13.8 |
| X1 Carbon | 1.6 | 12 | 12 |
| P1S | 1.5 | 11.4 | 11.4 |
| P1P | 1.5 | 11.4 | 11.4 |
| A1 | 1.4 | 10.8 | 10.8 |
| A1 mini | 1.4 | 10.2 | 10.2 |

> **Quelle der Werte.** Volumenstrom (12.0 mm³/s) und Flussrate (0.98) stammen aus
> `Generic PLA @Geeetech` — einem Profil, das **Geeetech selbst** für Bambu Studio
> beigesteuert hat und das unter
> `profiles/Geeetech/filament/` neben den Bambu-eigenen Profilen liegt. Es ist damit
> keine Annäherung über ein Fremdmaterial, sondern die Herstellerangabe.
> Nozzle-spezifische Profile führt Geeetech nicht: der 0.2-mm-Wert (1.6 mm³/s) kommt
> aus `Generic PLA @0.2 nozzle` der Bambu-Bibliothek, und 0.6 mm wiederholt den
> 0.4-mm-Wert, statt eine Rampe zu erfinden.

**12 mm³/s sind konservativ.** [SUNLU PLA](sunlu-pla.md) steht bei 15, [eSUN PLA+](esun-pla-plus.md)
bei 16, [Bambu PLA Basic](bambu-pla-basic.md) bei 21 mm³/s. Geeetech gibt für dasselbe
Material rund ein Viertel weniger frei als eSUN. Wer mehr will, hat den Weg:
[Kalibrierung, Schritt 3](../calibration.md#schritt-3--volumenstrom) — nach oben ist
hier erkennbar Luft, nur nicht belegt.

## Wofür PLA+ 2.0 das richtige Material ist

| Anforderung | Wahl |
|---|---|
| Halterungen, Clips, Gehäuse | **PLA+ 2.0** — bricht nicht glasartig |
| Günstiges Allzweck-PLA | **PLA+ 2.0** |
| Matte Sichtflächen ohne Nachbearbeitung | [Geeetech PLA Matte](geeetech-pla-matte.md) |
| Glänzende Sichtflächen | [Geeetech PLA Silk](geeetech-pla-silk.md) |
| Maximaler Durchsatz | [Bambu PLA Basic](bambu-pla-basic.md) — 21 statt 12 mm³/s |
| Wärme über 50 °C | [Geeetech PETG](geeetech-petg.md) |

## Wenn etwas nicht stimmt

| Symptom | Zuerst prüfen |
|---|---|
| Teil bricht entlang der Schichten | Düse auf 220 °C anheben — das Fenster reicht bis 230 |
| Unterextrusion, gerippte Oberfläche | [Volumenstrom](../calibration.md#schritt-3--volumenstrom) |
| Maße stimmen nicht | [Flussrate](../calibration.md#schritt-2--flussrate) |
| Fäden | [Fädenbildung](../troubleshooting.md#fädenbildung) |
| Erste Schicht haftet nicht | Bett auf 65 °C halten, Platte entfetten |
| Druck läuft langsamer als erwartet | normal — 12 mm³/s sind Geeetechs Grenze, siehe oben |

---

[← eSUN ABS+](esun-abs.md) · [Materialübersicht](README.md) · [Geeetech PLA Matte →](geeetech-pla-matte.md)
