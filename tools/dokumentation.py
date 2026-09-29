#!/usr/bin/env python3
"""Erzeugt docs/matrix.md aus dist/_index.json.

Die Matrix ist die einzige Doku-Seite, die generiert wird — sie beschreibt
Zahlen, die sich mit jedem Generatorlauf ändern können, und darf deshalb
nicht von Hand gepflegt werden.

Aufruf:  python3 tools/dokumentation.py
"""

from __future__ import annotations

import json
import sys
import tomllib
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
QUELLE = WURZEL / "src"
ZIEL = WURZEL / "docs" / "matrix.md"

STATUS_SYMBOL = {
    "validated-h2c-04": "🟢",
    "baseline": "🔵",
}


def main() -> int:
    index = json.loads((WURZEL / "dist" / "_index.json").read_text(encoding="utf-8"))
    drucker = tomllib.loads((QUELLE / "drucker.toml").read_text(encoding="utf-8"))
    stufen = tomllib.loads((QUELLE / "qualitaet.toml").read_text(encoding="utf-8"))
    filamente = {}
    for datei in sorted((QUELLE / "filamente").glob("*.toml")):
        daten = tomllib.loads(datei.read_text(encoding="utf-8"))
        filamente[daten["id"]] = daten
    filamente = dict(sorted(filamente.items(), key=lambda e: e[1]["reihenfolge"]))

    presets = index["presets"]
    fil = [e for e in presets if e["art"] == "filament"]
    pro = [e for e in presets if e["art"] == "process"]

    zeilen: list[str] = []
    schreib = zeilen.append

    schreib("# Profilmatrix")
    schreib("")
    schreib("> **Generierte Datei.** Nicht von Hand bearbeiten — sie entsteht aus")
    schreib("> `dist/_index.json` über `python3 tools/dokumentation.py`.")
    schreib("")
    schreib(f"Das Repository enthält **{len(fil)} Filamentprofile** und "
            f"**{len(pro)} Prozessprofile**.")
    schreib("")
    schreib("---")
    schreib("")

    # -- Filamentmatrix ---------------------------------------------------
    schreib("## Filamentprofile")
    schreib("")
    schreib("Ein Filamentprofil beschreibt das Material: Temperaturen, Fluss, Kühlung,")
    schreib("Volumenstrom. Es ist an Drucker und Düse gebunden, nicht an die Qualitätsstufe.")
    schreib("")
    schreib("Die Zahl in der Zelle ist der maximale Volumenstrom in mm³/s — der Wert, der")
    schreib("bestimmt, wie schnell der Drucker das Material überhaupt fördern kann.")
    schreib("")

    duesen = ["0.2", "0.4", "0.6"]
    for filament_id, filament in filamente.items():
        schreib(f"### {filament['label']}")
        schreib("")
        kopf = "| Drucker | " + " | ".join(f"{d} mm" for d in duesen) + " | Status |"
        schreib(kopf)
        schreib("|---|" + "---|" * (len(duesen) + 1))
        for drucker_id, d in drucker.items():
            zellen = []
            status = ""
            for duese in duesen:
                treffer = [e for e in fil if e["drucker"] == drucker_id
                           and e["filament"] == filament_id and e["duese"] == duese]
                if not treffer:
                    zellen.append("—")
                    continue
                eintrag = treffer[0]
                zellen.append(f"**{eintrag['volumenstrom']}**")
                status = eintrag["status"]
            symbol = STATUS_SYMBOL.get(status, "")
            marke = f"{symbol} {status}" if status else "—"
            if filament_id == "sunlu-petg-glow" and drucker_id == "h2c":
                marke = "🟢 0.4 mm am Gerät verifiziert"
            elif status:
                marke = "🔵 Startwerte"
            schreib(f"| {d['label']} | " + " | ".join(zellen) + f" | {marke} |")
        schreib("")
        if filament["abrasiv"]:
            schreib("> ⚠️ **Abrasiv.** Gehärtete Düse zwingend erforderlich. "
                    "Die 0.2-mm-Düse ist für dieses Material gesperrt — "
                    "siehe [Düsen](nozzles.md).")
            schreib("")

    schreib("---")
    schreib("")

    # -- Prozessmatrix ----------------------------------------------------
    schreib("## Prozessprofile")
    schreib("")
    schreib("Ein Prozessprofil beschreibt die Geometrie: Schichthöhe, Wände, Füllung,")
    schreib("Geschwindigkeiten. Es gilt für jedes Material auf demselben Drucker.")
    schreib("")
    schreib("Die Zahl in der Zelle ist die Schichthöhe in mm.")
    schreib("")
    schreib("| Drucker | Düse | " + " | ".join(s["label"] for s in stufen.values()) + " |")
    schreib("|---|---|" + "---|" * len(stufen))
    for drucker_id, d in drucker.items():
        for duese in duesen:
            zellen = []
            for stufen_id in stufen:
                treffer = [e for e in pro if e["drucker"] == drucker_id
                           and e["duese"] == duese and e["stufe"] == stufen_id]
                if not treffer:
                    zellen.append("—")
                    continue
                eintrag = treffer[0]
                text = f"**{eintrag['schichthoehe']}**"
                if eintrag["schichthoehe"] != eintrag["ziel_schichthoehe"]:
                    text += f" ⁽¹⁾"
                zellen.append(text)
            schreib(f"| {d['label']} | {duese} mm | " + " | ".join(zellen) + " |")
    schreib("")
    abweichungen = [e for e in pro if e["schichthoehe"] != e["ziel_schichthoehe"]]
    if abweichungen:
        schreib("⁽¹⁾ Der Zielwert der Stufe ist auf diesem Drucker nicht verfügbar; das")
        schreib("Profil rastet auf die nächstgelegene freigegebene Schichthöhe ein:")
        schreib("")
        for e in sorted(abweichungen, key=lambda e: e["name"]):
            schreib(f"- `{e['name']}` — Ziel {e['ziel_schichthoehe']} mm, "
                    f"gesetzt {e['schichthoehe']} mm (Basis `{e['inherits']}`)")
        schreib("")

    schreib("---")
    schreib("")
    schreib("## Vererbung")
    schreib("")
    schreib("Jedes Profil erbt von einem Originalprofil aus Bambu Studio. Dadurch bleiben")
    schreib("alle Einstellungen, die dieses Repository nicht setzt, auf den vom Hersteller")
    schreib("abgestimmten Werten — und wandern bei einem Studio-Update automatisch mit.")
    schreib("")
    schreib("<details>")
    schreib("<summary>Vollständige Liste der Elternprofile</summary>")
    schreib("")
    schreib("| Profil | erbt von |")
    schreib("|---|---|")
    for e in sorted(presets, key=lambda e: (e["art"], e["name"])):
        schreib(f"| `{e['name']}` | `{e['inherits']}` |")
    schreib("")
    schreib("</details>")
    schreib("")
    schreib("## Legende")
    schreib("")
    schreib("| Symbol | Bedeutung |")
    schreib("|---|---|")
    schreib("| 🟢 | Am Gerät gedruckt und bestätigt |")
    schreib("| 🔵 | Startwert aus der Bambu-Basis abgeleitet, nicht einzeln gedruckt |")
    schreib("| ⚠️ | Materialbedingte Einschränkung beachten |")
    schreib("| — | Kombination bewusst nicht ausgeliefert |")
    schreib("")

    ZIEL.parent.mkdir(parents=True, exist_ok=True)
    ZIEL.write_text("\n".join(zeilen), encoding="utf-8")
    print(f"{ZIEL.relative_to(WURZEL)} geschrieben ({len(zeilen)} Zeilen).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
