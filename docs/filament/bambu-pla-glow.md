# Bambu PLA Glow

[← Materialübersicht](README.md) · Status: 🔵 Startwert · Basis: `Bambu PLA Glow`
· ⚠️ **abrasiv — gehärtete Düse zwingend**

Leuchtendes PLA von Bambu Lab, abgeleitet vom herstellereigenen Profil. Deutlich
höhere Volumenströme als die Glow-Materialien der anderen Hersteller: Bambu verwendet
ein feineres Pigment mit engerer Korngrößenverteilung, was den Schmelzfluss weniger
stört.

---

## Vor dem ersten Druck

> **Gehärtete Düse verbauen.** Auch das feinere Bambu-Pigment ist Strontiumaluminat
> und damit abrasiv. Bambu selbst gibt für dieses Material ausschließlich gehärtete
> Düsen frei.
>
> **0.2 mm ist nicht verfügbar.** Bambu Studio liefert für dieses Material selbst kein
> 0.2-mm-Profil aus — die Sperre in diesem Repository deckt sich also mit der
> Herstellerfreigabe. Begründung in der
> [Düsenkunde](../nozzles.md#warum-02-mm-bei-glow-gesperrt-ist).

---

## Kennwerte

| Größe | Wert | Abweichung zu PLA Basic |
|---|---|---|
| Düse | **220 °C** (erste Schicht 225 °C) | gleich |
| Temperaturfenster | 210 – 230 °C | gleich |
| Bett | **55 °C** (erste Schicht 60 °C) | gleich |
| Glasübergang | 45 °C | gleich |
| Flussrate | 0.98 | gleich |
| Lüfter | **100 %** durchgehend | gleich |
| Überhangkühlung | 100 % | gleich |
| Z-Hop | 0.4 mm | gleich |
| Düsen | 0.4 · 0.6 mm | **0.2 mm entfällt** |
| Trocknung | 45 °C / 6 h | gleich |

Bemerkenswert: Anders als bei SUNLU und eSUN verlangt das Bambu-Glow **keine höhere
Temperatur** als das Basismaterial. Der Unterschied steckt allein im Volumenstrom.

## Volumenstrom je Drucker und Düse

| Drucker | 0.4 mm | 0.6 mm |
|---|--:|--:|
| H2C | 20.7 | 24.1 |
| X1 Carbon | 18 | 21 |
| P1S | 17.1 | 19.9 |
| P1P | 17.1 | 19.9 |
| A1 | 16.2 | 18.9 |
| A1 mini | 15.3 | 17.8 |

18 mm³/s auf dem X1C sind fast das Doppelte der übrigen Glow-Materialien
(10.0 – 10.5 mm³/s) und liegen nur 14 % unter PLA Basic. Das ist der Hauptgrund,
dieses Material zu wählen, wenn größere Leuchtteile in vertretbarer Zeit entstehen
sollen.

## Leuchtwirkung im Druck

- **Wandzahl entscheidet.** Wie bei allen Glow-Materialien kommt das Leuchten aus dem
  Volumen, nicht von der Oberfläche. Drei Wände oder mehr.
- **Füllung 25 – 40 %** bei dünnwandigen Teilen.
- **Aufladen** mit UV- oder kaltweißem Licht.
- **Nachleuchtdauer** liegt bei diesem Material spürbar über den Alternativen — das
  feinere Pigment ist gleichmäßiger verteilt.

## Wenn etwas nicht stimmt

| Symptom | Zuerst prüfen |
|---|---|
| Extruder klickt, kein Material | [Verstopfung](../troubleshooting.md#verstopfung) — gehärtete Düse verbaut? |
| Bahnen werden mit der Zeit breiter | Düse verschlissen, ersetzen |
| Unterextrusion | [Volumenstrom](../calibration.md#schritt-3--volumenstrom) |
| Schwaches Leuchten | Wandzahl und Füllung, nicht die Temperatur |

---

[← Bambu PLA Basic](bambu-pla-basic.md) · [Materialübersicht](README.md) · [Bambu PLA Translucent →](bambu-pla-translucent.md)
