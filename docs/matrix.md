# Profilmatrix

> **Generierte Datei.** Nicht von Hand bearbeiten — sie entsteht aus
> `dist/_index.json` über `python3 tools/dokumentation.py`.

Das Repository enthält **50 Filamentprofile** und **45 Prozessprofile**.

---

## Filamentprofile

Ein Filamentprofil beschreibt das Material: Temperaturen, Fluss, Kühlung,
Volumenstrom. Es ist an Drucker und Düse gebunden, nicht an die Qualitätsstufe.

Die Zahl in der Zelle ist der maximale Volumenstrom in mm³/s — der Wert, der
bestimmt, wie schnell der Drucker das Material überhaupt fördern kann.

### SUNLU PLA

| Drucker | 0.2 mm | 0.4 mm | 0.6 mm | Status |
|---|---|---|---|---|
| Bambu Lab H2C | **4** | **17.2** | **24.1** | 🔵 Startwerte |
| Bambu Lab X1 Carbon | **3.5** | **15** | **21** | 🔵 Startwerte |
| Bambu Lab P1S | **3.3** | **14.2** | **19.9** | 🔵 Startwerte |
| Bambu Lab A1 | **3.1** | **13.5** | **18.9** | 🔵 Startwerte |
| Bambu Lab A1 mini | **3** | **12.8** | **17.8** | 🔵 Startwerte |

### SUNLU PLA Glow

| Drucker | 0.2 mm | 0.4 mm | 0.6 mm | Status |
|---|---|---|---|---|
| Bambu Lab H2C | — | **12.1** | **17.2** | 🔵 Startwerte |
| Bambu Lab X1 Carbon | — | **10.5** | **15** | 🔵 Startwerte |
| Bambu Lab P1S | — | **10** | **14.2** | 🔵 Startwerte |
| Bambu Lab A1 | — | **9.5** | **13.5** | 🔵 Startwerte |
| Bambu Lab A1 mini | — | **8.9** | **12.8** | 🔵 Startwerte |

> ⚠️ **Abrasiv.** Gehärtete Düse zwingend erforderlich. Die 0.2-mm-Düse ist für dieses Material gesperrt — siehe [Düsen](nozzles.md).

### SUNLU PETG

| Drucker | 0.2 mm | 0.4 mm | 0.6 mm | Status |
|---|---|---|---|---|
| Bambu Lab H2C | **3.4** | **15.5** | **20.7** | 🔵 Startwerte |
| Bambu Lab X1 Carbon | **3** | **13.5** | **18** | 🔵 Startwerte |
| Bambu Lab P1S | **2.8** | **12.8** | **17.1** | 🔵 Startwerte |
| Bambu Lab A1 | **2.7** | **12.2** | **16.2** | 🔵 Startwerte |
| Bambu Lab A1 mini | **2.5** | **11.5** | **15.3** | 🔵 Startwerte |

### SUNLU PETG Glow

| Drucker | 0.2 mm | 0.4 mm | 0.6 mm | Status |
|---|---|---|---|---|
| Bambu Lab H2C | — | **12.6** | **16.7** | 🟢 0.4 mm am Gerät verifiziert |
| Bambu Lab X1 Carbon | — | **11** | **14.5** | 🔵 Startwerte |
| Bambu Lab P1S | — | **10.4** | **13.8** | 🔵 Startwerte |
| Bambu Lab A1 | — | **9.9** | **13.1** | 🔵 Startwerte |
| Bambu Lab A1 mini | — | **9.3** | **12.3** | 🔵 Startwerte |

> ⚠️ **Abrasiv.** Gehärtete Düse zwingend erforderlich. Die 0.2-mm-Düse ist für dieses Material gesperrt — siehe [Düsen](nozzles.md).

---

## Prozessprofile

Ein Prozessprofil beschreibt die Geometrie: Schichthöhe, Wände, Füllung,
Geschwindigkeiten. Es gilt für jedes Material auf demselben Drucker.

Die Zahl in der Zelle ist die Schichthöhe in mm.

| Drucker | Düse | Qualität | Normal | Schnell |
|---|---|---|---|---|
| Bambu Lab H2C | 0.2 mm | **0.08** | **0.12** | **0.12** ⁽¹⁾ |
| Bambu Lab H2C | 0.4 mm | **0.12** | **0.2** | **0.24** ⁽¹⁾ |
| Bambu Lab H2C | 0.6 mm | **0.18** | **0.3** | **0.3** ⁽¹⁾ |
| Bambu Lab X1 Carbon | 0.2 mm | **0.08** | **0.12** | **0.14** |
| Bambu Lab X1 Carbon | 0.4 mm | **0.12** | **0.2** | **0.28** |
| Bambu Lab X1 Carbon | 0.6 mm | **0.18** | **0.3** | **0.42** |
| Bambu Lab P1S | 0.2 mm | **0.08** | **0.12** | **0.14** |
| Bambu Lab P1S | 0.4 mm | **0.12** | **0.2** | **0.28** |
| Bambu Lab P1S | 0.6 mm | **0.18** | **0.3** | **0.42** |
| Bambu Lab A1 | 0.2 mm | **0.08** | **0.12** | **0.14** |
| Bambu Lab A1 | 0.4 mm | **0.12** | **0.2** | **0.28** |
| Bambu Lab A1 | 0.6 mm | **0.18** | **0.3** | **0.42** |
| Bambu Lab A1 mini | 0.2 mm | **0.08** | **0.12** | **0.14** |
| Bambu Lab A1 mini | 0.4 mm | **0.12** | **0.2** | **0.28** |
| Bambu Lab A1 mini | 0.6 mm | **0.18** | **0.3** | **0.42** |

⁽¹⁾ Der Zielwert der Stufe ist auf diesem Drucker nicht verfügbar; das
Profil rastet auf die nächstgelegene freigegebene Schichthöhe ein:

- `Schnell H2C 0.2` — Ziel 0.14 mm, gesetzt 0.12 mm (Basis `0.12mm Balanced Quality @BBL H2C 0.2 nozzle`)
- `Schnell H2C 0.4` — Ziel 0.28 mm, gesetzt 0.24 mm (Basis `0.24mm Standard @BBL H2C`)
- `Schnell H2C 0.6` — Ziel 0.42 mm, gesetzt 0.3 mm (Basis `0.30mm Standard @BBL H2C 0.6 nozzle`)

---

## Vererbung

Jedes Profil erbt von einem Originalprofil aus Bambu Studio. Dadurch bleiben
alle Einstellungen, die dieses Repository nicht setzt, auf den vom Hersteller
abgestimmten Werten — und wandern bei einem Studio-Update automatisch mit.

<details>
<summary>Vollständige Liste der Elternprofile</summary>

| Profil | erbt von |
|---|---|
| `SUNLU PETG A1 0.2` | `Generic PETG @BBL A1 0.2 nozzle` |
| `SUNLU PETG A1 0.4` | `Generic PETG @BBL A1` |
| `SUNLU PETG A1 0.6` | `Generic PETG @BBL A1` |
| `SUNLU PETG A1M 0.2` | `Generic PETG @BBL A1M 0.2 nozzle` |
| `SUNLU PETG A1M 0.4` | `Generic PETG @BBL A1M` |
| `SUNLU PETG A1M 0.6` | `Generic PETG @BBL A1M` |
| `SUNLU PETG Glow A1 0.4` | `Generic PETG @BBL A1` |
| `SUNLU PETG Glow A1 0.6` | `Generic PETG @BBL A1` |
| `SUNLU PETG Glow A1M 0.4` | `Generic PETG @BBL A1M` |
| `SUNLU PETG Glow A1M 0.6` | `Generic PETG @BBL A1M` |
| `SUNLU PETG Glow H2C 0.4` | `Generic PETG @BBL H2C 0.4 nozzle` |
| `SUNLU PETG Glow H2C 0.6` | `Generic PETG @BBL H2C` |
| `SUNLU PETG Glow P1S 0.4` | `Generic PETG` |
| `SUNLU PETG Glow P1S 0.6` | `Generic PETG` |
| `SUNLU PETG Glow X1C 0.4` | `Generic PETG` |
| `SUNLU PETG Glow X1C 0.6` | `Generic PETG` |
| `SUNLU PETG H2C 0.2` | `Generic PETG @BBL H2C 0.2 nozzle` |
| `SUNLU PETG H2C 0.4` | `Generic PETG @BBL H2C 0.4 nozzle` |
| `SUNLU PETG H2C 0.6` | `Generic PETG @BBL H2C` |
| `SUNLU PETG P1S 0.2` | `Generic PETG @0.2 nozzle` |
| `SUNLU PETG P1S 0.4` | `Generic PETG` |
| `SUNLU PETG P1S 0.6` | `Generic PETG` |
| `SUNLU PETG X1C 0.2` | `Generic PETG @0.2 nozzle` |
| `SUNLU PETG X1C 0.4` | `Generic PETG` |
| `SUNLU PETG X1C 0.6` | `Generic PETG` |
| `SUNLU PLA A1 0.2` | `Generic PLA @BBL A1 0.2 nozzle` |
| `SUNLU PLA A1 0.4` | `Generic PLA @BBL A1` |
| `SUNLU PLA A1 0.6` | `Generic PLA @BBL A1` |
| `SUNLU PLA A1M 0.2` | `Generic PLA @BBL A1M 0.2 nozzle` |
| `SUNLU PLA A1M 0.4` | `Generic PLA @BBL A1M` |
| `SUNLU PLA A1M 0.6` | `Generic PLA @BBL A1M` |
| `SUNLU PLA Glow A1 0.4` | `Generic PLA @BBL A1` |
| `SUNLU PLA Glow A1 0.6` | `Generic PLA @BBL A1` |
| `SUNLU PLA Glow A1M 0.4` | `Generic PLA @BBL A1M` |
| `SUNLU PLA Glow A1M 0.6` | `Generic PLA @BBL A1M` |
| `SUNLU PLA Glow H2C 0.4` | `Generic PLA @BBL H2C 0.4 nozzle` |
| `SUNLU PLA Glow H2C 0.6` | `Generic PLA @BBL H2C` |
| `SUNLU PLA Glow P1S 0.4` | `Generic PLA` |
| `SUNLU PLA Glow P1S 0.6` | `Generic PLA` |
| `SUNLU PLA Glow X1C 0.4` | `Generic PLA` |
| `SUNLU PLA Glow X1C 0.6` | `Generic PLA` |
| `SUNLU PLA H2C 0.2` | `Generic PLA @BBL H2C 0.2 nozzle` |
| `SUNLU PLA H2C 0.4` | `Generic PLA @BBL H2C 0.4 nozzle` |
| `SUNLU PLA H2C 0.6` | `Generic PLA @BBL H2C` |
| `SUNLU PLA P1S 0.2` | `Generic PLA @0.2 nozzle` |
| `SUNLU PLA P1S 0.4` | `Generic PLA` |
| `SUNLU PLA P1S 0.6` | `Generic PLA` |
| `SUNLU PLA X1C 0.2` | `Generic PLA @0.2 nozzle` |
| `SUNLU PLA X1C 0.4` | `Generic PLA` |
| `SUNLU PLA X1C 0.6` | `Generic PLA` |
| `Normal A1 0.2` | `0.12mm Draft @BBL A1 0.2 nozzle` |
| `Normal A1 0.4` | `0.20mm Standard @BBL A1` |
| `Normal A1 0.6` | `0.30mm Standard @BBL A1 0.6 nozzle` |
| `Normal A1M 0.2` | `0.12mm Draft @BBL A1M 0.2 nozzle` |
| `Normal A1M 0.4` | `0.20mm Standard @BBL A1M` |
| `Normal A1M 0.6` | `0.30mm Standard @BBL A1M 0.6 nozzle` |
| `Normal H2C 0.2` | `0.12mm Balanced Quality @BBL H2C 0.2 nozzle` |
| `Normal H2C 0.4` | `0.20mm Standard @BBL H2C` |
| `Normal H2C 0.6` | `0.30mm Standard @BBL H2C 0.6 nozzle` |
| `Normal P1S 0.2` | `0.12mm Standard @BBL X1C 0.2 nozzle` |
| `Normal P1S 0.4` | `0.20mm Standard @BBL X1C` |
| `Normal P1S 0.6` | `0.30mm Standard @BBL X1C 0.6 nozzle` |
| `Normal X1C 0.2` | `0.12mm Standard @BBL X1C 0.2 nozzle` |
| `Normal X1C 0.4` | `0.20mm Standard @BBL X1C` |
| `Normal X1C 0.6` | `0.30mm Standard @BBL X1C 0.6 nozzle` |
| `Qualität A1 0.2` | `0.08mm High Quality @BBL A1 0.2 nozzle` |
| `Qualität A1 0.4` | `0.12mm High Quality @BBL A1` |
| `Qualität A1 0.6` | `0.18mm Fine @BBL A1 0.6 nozzle` |
| `Qualität A1M 0.2` | `0.08mm High Quality @BBL A1M 0.2 nozzle` |
| `Qualität A1M 0.4` | `0.12mm High Quality @BBL A1M` |
| `Qualität A1M 0.6` | `0.18mm Fine @BBL A1M 0.6 nozzle` |
| `Qualität H2C 0.2` | `0.08mm High Quality @BBL H2C 0.2 nozzle` |
| `Qualität H2C 0.4` | `0.12mm High Quality @BBL H2C` |
| `Qualität H2C 0.6` | `0.18mm Balanced Quality @BBL H2C 0.6 nozzle` |
| `Qualität P1S 0.2` | `0.08mm High Quality @BBL X1C 0.2 nozzle` |
| `Qualität P1S 0.4` | `0.12mm High Quality @BBL X1C` |
| `Qualität P1S 0.6` | `0.18mm Standard @BBL X1C 0.6 nozzle` |
| `Qualität X1C 0.2` | `0.08mm High Quality @BBL X1C 0.2 nozzle` |
| `Qualität X1C 0.4` | `0.12mm High Quality @BBL X1C` |
| `Qualität X1C 0.6` | `0.18mm Standard @BBL X1C 0.6 nozzle` |
| `Schnell A1 0.2` | `0.14mm Extra Draft @BBL A1 0.2 nozzle` |
| `Schnell A1 0.4` | `0.28mm Extra Draft @BBL A1` |
| `Schnell A1 0.6` | `0.42mm Extra Draft @BBL A1 0.6 nozzle` |
| `Schnell A1M 0.2` | `0.14mm Extra Draft @BBL A1M 0.2 nozzle` |
| `Schnell A1M 0.4` | `0.28mm Extra Draft @BBL A1M` |
| `Schnell A1M 0.6` | `0.42mm Extra Draft @BBL A1M 0.6 nozzle` |
| `Schnell H2C 0.2` | `0.12mm Balanced Quality @BBL H2C 0.2 nozzle` |
| `Schnell H2C 0.4` | `0.24mm Standard @BBL H2C` |
| `Schnell H2C 0.6` | `0.30mm Standard @BBL H2C 0.6 nozzle` |
| `Schnell P1S 0.2` | `0.14mm Standard @BBL X1C 0.2 nozzle` |
| `Schnell P1S 0.4` | `0.28mm Extra Draft @BBL X1C` |
| `Schnell P1S 0.6` | `0.42mm Standard @BBL X1C 0.6 nozzle` |
| `Schnell X1C 0.2` | `0.14mm Standard @BBL X1C 0.2 nozzle` |
| `Schnell X1C 0.4` | `0.28mm Extra Draft @BBL X1C` |
| `Schnell X1C 0.6` | `0.42mm Standard @BBL X1C 0.6 nozzle` |

</details>

## Legende

| Symbol | Bedeutung |
|---|---|
| 🟢 | Am Gerät gedruckt und bestätigt |
| 🔵 | Startwert aus der Bambu-Basis abgeleitet, nicht einzeln gedruckt |
| ⚠️ | Materialbedingte Einschränkung beachten |
| — | Kombination bewusst nicht ausgeliefert |
