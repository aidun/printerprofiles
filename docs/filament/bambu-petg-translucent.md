# Bambu PETG Translucent

[← Materialübersicht](README.md) · Status: 🔵 Startwert · Basis: `Bambu PETG Translucent`
· 💧 **auf Klarheit optimiert**

Durchscheinendes PETG von Bambu Lab — und das langsamste Material im Repository.
Bambu gibt für dieses Material bei 0.4 mm nur **6 mm³/s** frei, ein Siebtel dessen,
was [Bambu PETG HF](bambu-petg-hf.md) darf. Der Wert stammt aus dem Datenblatt und
ist keine Vorsichtsmarge dieses Repositories.

---

## Warum so langsam

> Bei durchscheinenden Materialien bestimmt die Verweilzeit der Schmelze die Optik.
> Jede Bahn muss lange genug flüssig bleiben, um mit ihren Nachbarn zu einer
> homogenen Masse zu verschmelzen — sonst bleibt an jeder Grenzfläche eine
> lichtstreuende Naht.
>
> Bambus 6 mm³/s erzwingen genau das. Eine Erhöhung bringt nicht mehr Tempo, sondern
> ein trübes Teil: Der Slicer drosselt ohnehin nur dort, wo die Geometrie mehr
> fordern würde. **Diesen Wert nicht anheben, ohne die Optik zu prüfen.**

---

## Kennwerte

| Größe | Wert | Abweichung zu PETG HF |
|---|---|---|
| Düse | **250 °C** (erste Schicht 255 °C) | +5 °C |
| Temperaturfenster | 240 – 260 °C | unten enger |
| Bett | **70 °C** (erste Schicht 75 °C) | gleich |
| Glasübergang | 70 °C | gleich |
| Flussrate | 0.97 | gleich |
| Lüfter | **10 – 25 %** | halbiert |
| Überhangkühlung | **40 %** | von 100 % gesenkt |
| Verzögerung ab | 8 s Schichtzeit | −2 s |
| Lüfter aus für | 3 Schichten | gleich |
| Z-Hop | 0.6 mm | gleich |
| Trocknung | **65 °C / 8 h** | zwingend |
| Lagerung | zwingend trocken | kritisch |

## Volumenstrom je Drucker und Düse

| Drucker | 0.2 mm | 0.4 mm | 0.6 mm |
|---|--:|--:|--:|
| H2C | 1.1 | 6.9 | 9.2 |
| X1 Carbon | 1 | 6 | 8 |
| P1S | 0.9 | 5.7 | 7.6 |
| P1P | 0.9 | 5.7 | 7.6 |
| A1 | 0.9 | 5.4 | 7.2 |
| A1 mini | 0.8 | 5.1 | 6.8 |

Der fett markierte Wert ist Bambus Datenblattgrenze; der 0.6-mm-Wert ist eine
Düsenstufe nach oben extrapoliert. Alle übrigen Zeilen sind über den
[Durchsatzfaktor](../drucker/README.md#durchsatzfaktoren) skaliert.

**Was das praktisch bedeutet:** Ein Teil, das in PETG HF eine Stunde braucht, dauert
hier ein Vielfaches. Das ist eingepreist — dieses Material wählt man für die Optik,
nicht für den Durchsatz.

## Wofür sich dieses Material eignet

**Diffusoren und Lichtleiter mit Wärmebelastung.** Gegenüber
[Bambu PLA Translucent](bambu-pla-translucent.md) liegt der Glasübergang 25 °C
höher — für Leuchtengehäuse mit eingebauter Elektronik ist das der entscheidende
Unterschied.

**Sichtfenster und Abdeckungen.** PETG ist amorph und erreicht bei sauberer
Prozessführung mehr Klarheit als jedes PLA. Füllung 100 %, Muster `concentric`,
hohe Schichthöhe.

**Trocknen ist nicht optional.** Jede Dampfblase bleibt als weißer Punkt im Teil
sichtbar und lässt sich nicht mehr entfernen.

## Wenn etwas nicht stimmt

| Symptom | Zuerst prüfen |
|---|---|
| Weiße Punkte im Material | [Feuchtigkeit](../troubleshooting.md#feuchtigkeit) — trocknen, keine Ausnahme |
| Teil bleibt trüb | Füllung 100 %, Schichthöhe erhöhen — **nicht** den Volumenstrom anheben |
| Druck dauert unerwartet lange | erwartetes Verhalten, siehe oben |
| Fäden | [Fädenbildung](../troubleshooting.md#fädenbildung) |
| Überhänge hängen durch | Stützmaterial statt mehr Lüfter |

---

[← Bambu PETG HF](bambu-petg-hf.md) · [Materialübersicht](README.md)
