# Bambu PLA Basic

[← Materialübersicht](README.md) · Status: 🔵 Startwert · Basis: `Bambu PLA Basic`

Das Hausmaterial von Bambu Lab und das schnellste PLA im Repository. Als einziges
Herstellermaterial erbt es nicht von `Generic PLA`, sondern von seinem eigenen,
vom Hersteller abgestimmten Profil — inklusive der Kalibrierdaten, die Bambu Studio
für diese Spulen mitbringt.

---

## Warum die Werte hier höher liegen

> Die Bambu-Materialien in diesem Repository erben vom **herstellereigenen
> Basisprofil** (`Bambu PLA Basic`), nicht vom generischen. Volumenstrom, Druckvorschub
> und Kühlkurve stammen damit aus Bambus eigener Messung an der Materialcharge.
>
> Praktische Folge: **21 mm³/s auf dem X1C** gegenüber 15 mm³/s bei SUNLU PLA. Das ist
> kein Sicherheitsaufschlag, den dieses Repository vergibt, sondern die vom Hersteller
> für sein eigenes Material freigegebene Grenze.

---

## Kennwerte

| Größe | Wert | Abweichung zu SUNLU PLA |
|---|---|---|
| Düse | **220 °C** (erste Schicht 225 °C) | +5 °C |
| Temperaturfenster | 210 – 230 °C | enger |
| Bett | **55 °C** (erste Schicht 60 °C) | gleich |
| Glasübergang | **45 °C** | −10 °C |
| Flussrate | 0.98 | gleich |
| Lüfter | **100 %** durchgehend | voll |
| Überhangkühlung | 100 % | gleich |
| Z-Hop | 0.4 mm | gleich |
| Abrasiv | nein — Messingdüse genügt | |
| Trocknung | 45 °C / 6 h | gleich |
| Lagerung | trocken mit Silikagel, unkritisch | |

**Zum Glasübergang von 45 °C:** Der Wert stammt aus Bambus Datenblatt und liegt
niedriger als der Klassenwert für PLA. Bambu Studio nutzt ihn, um die Kammer- und
Bettführung zu steuern. Für die Praxis bedeutet er, dass dieses Material früher
nachgibt als andere PLA-Typen — für belastete oder warme Teile ist
[Bambu PETG HF](bambu-petg-hf.md) die richtige Wahl.

## Volumenstrom je Drucker und Düse

Werte in mm³/s. Basis ist der X1C; die übrigen Drucker werden über den
[Durchsatzfaktor](../drucker/README.md#durchsatzfaktoren) skaliert.

| Drucker | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| H2C | 2.3 | 24.1 | 28.7 |
| X1 Carbon | 2 | 21 | 25 |
| P1S | 1.9 | 19.9 | 23.8 |
| P1P | 1.9 | 19.9 | 23.8 |
| A1 | 1.8 | 18.9 | 22.5 |
| A1 mini | 1.7 | 17.8 | 21.2 |

Die Werte für 0.2 und 0.4 mm stammen aus dem Bambu-Datenblatt, der 0.6-mm-Wert ist
eine Düsenstufe nach oben extrapoliert.

## Hinweise

- **Kühlung läuft voll.** Als einziges Material im Repository fährt PLA Basic den
  Lüfter durchgehend auf 100 %. Das entspricht Bambus Profil und ist der Grund für
  die sehr guten Überhänge dieses Materials.
- **Schnellstes Material im Bestand.** Zusammen mit [Bambu PETG HF](bambu-petg-hf.md)
  die einzige Wahl, wenn Druckzeit das Hauptkriterium ist.
- **Alle drei Düsen freigegeben.**
- **AMS-tauglich** ohne Einschränkung.

## Wenn etwas nicht stimmt

| Symptom | Zuerst prüfen |
|---|---|
| Unterextrusion bei hohem Tempo | [Volumenstrom](../calibration.md#schritt-3--volumenstrom) — Herstellerwert prüfen |
| Maße stimmen nicht | [Flussrate](../calibration.md#schritt-2--flussrate) |
| Teil verformt sich bei Wärme | Glasübergang 45 °C — auf PETG wechseln |
| Fäden | [Fädenbildung](../troubleshooting.md#fädenbildung) |

---

[← Geeetech PETG](geeetech-petg.md) · [Materialübersicht](README.md) · [Bambu PLA Glow →](bambu-pla-glow.md)
