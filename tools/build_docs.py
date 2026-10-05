#!/usr/bin/env python3
"""Builds docs/matrix.md from dist/_index.json.

The matrix is the only generated documentation page — it describes numbers that
can change with every generator run and must therefore not be maintained by
hand. Its prose is German, like every other page under docs/.

Usage:  python3 tools/build_docs.py
"""

from __future__ import annotations

import json
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "src"
TARGET = ROOT / "docs" / "matrix.md"

STATUS_SYMBOL = {"baseline": "🔵"}


def verified(status: str) -> tuple[str, str] | None:
    """Splits a status id like 'validated-h2c-04' into printer and nozzle.

    Returns None for 'baseline'. Keeping the verified combination in the status
    field means the matrix needs no special case per material.
    """
    parts = status.split("-")
    if len(parts) != 3 or parts[0] != "validated":
        return None
    digits = parts[2]
    return parts[1], f"{digits[0]}.{digits[1:]}"


def main() -> int:
    index = json.loads((ROOT / "dist" / "_index.json").read_text(encoding="utf-8"))
    printers = tomllib.loads((SOURCE / "printers.toml").read_text(encoding="utf-8"))
    levels = tomllib.loads((SOURCE / "quality.toml").read_text(encoding="utf-8"))
    filaments = {}
    for file in sorted((SOURCE / "filaments").glob("*.toml")):
        data = tomllib.loads(file.read_text(encoding="utf-8"))
        filaments[data["id"]] = data
    filaments = dict(sorted(filaments.items(), key=lambda e: e[1]["order"]))

    presets = index["presets"]
    fil = [e for e in presets if e["kind"] == "filament"]
    pro = [e for e in presets if e["kind"] == "process"]

    lines: list[str] = []
    out = lines.append

    out("# Profilmatrix")
    out("")
    out("> **Generierte Datei.** Nicht von Hand bearbeiten — sie entsteht aus")
    out("> `dist/_index.json` über `python3 tools/build_docs.py`.")
    out("")
    out(f"Das Repository enthält **{len(fil)} Filamentprofile** und "
        f"**{len(pro)} Prozessprofile**.")
    out("")
    out("---")
    out("")

    # -- Filament matrix --------------------------------------------------
    out("## Filamentprofile")
    out("")
    out("Ein Filamentprofil beschreibt das Material: Temperaturen, Fluss, Kühlung,")
    out("Volumenstrom. Es ist an Drucker und Düse gebunden, nicht an die Qualitätsstufe.")
    out("")
    out("Die Zahl in der Zelle ist der maximale Volumenstrom in mm³/s — der Wert, der")
    out("bestimmt, wie schnell der Drucker das Material überhaupt fördern kann.")
    out("")

    nozzles = ["0.2", "0.4", "0.6"]
    brand = None
    for filament_id, filament in filaments.items():
        if filament["brand"] != brand:
            brand = filament["brand"]
            count = sum(1 for f in filaments.values() if f["brand"] == brand)
            out(f"### {brand}")
            out("")
            out(f"{count} Materialien.")
            out("")
        out(f"#### {filament['label']}")
        out("")
        out("| Drucker | " + " | ".join(f"{n} mm" for n in nozzles) + " | Status |")
        out("|---|" + "---|" * (len(nozzles) + 1))
        for printer_id, p in printers.items():
            cells = []
            status = ""
            for nozzle in nozzles:
                hits = [e for e in fil if e["printer"] == printer_id
                        and e["filament"] == filament_id and e["nozzle"] == nozzle]
                if not hits:
                    cells.append("—")
                    continue
                entry = hits[0]
                cells.append(f"**{entry['flow']}**")
                status = entry["status"]
            if not status:
                mark = "—"
            else:
                hit = verified(status)
                if hit and hit[0] == printer_id:
                    mark = f"🟢 {hit[1]} mm am Gerät verifiziert"
                else:
                    mark = f"{STATUS_SYMBOL.get(status, '🔵')} Startwerte"
            out(f"| {p['label']} | " + " | ".join(cells) + f" | {mark} |")
        out("")
        if filament["abrasive"]:
            out("> ⚠️ **Abrasiv.** Gehärtete Düse zwingend erforderlich. "
                "Die 0.2-mm-Düse ist für dieses Material gesperrt — "
                "siehe [Düsen](nozzles.md).")
            out("")
        if filament["flexible"]:
            out("> 🧶 **Flexibel.** Der Volumenstrom wird vom Extruder begrenzt, "
                "nicht von der Düse — eine größere Düse bringt hier nichts. "
                "Die 0.2-mm-Düse ist gesperrt.")
            out("")
        if filament["transparent"]:
            out("> 💧 **Auf Klarheit optimiert.** Höhere Düsentemperatur, bewusst "
                "abgesenkter Volumenstrom und stark zurückgenommene Kühlung — "
                "Klarheit geht hier vor Druckzeit.")
            out("")

    out("---")
    out("")

    # -- Process matrix ---------------------------------------------------
    out("## Prozessprofile")
    out("")
    out("Ein Prozessprofil beschreibt die Geometrie: Schichthöhe, Wände, Füllung,")
    out("Geschwindigkeiten. Es gilt für jedes Material auf demselben Drucker.")
    out("")
    out("Die Zahl in der Zelle ist die Schichthöhe in mm.")
    out("")
    out("| Drucker | Düse | " + " | ".join(s["label"] for s in levels.values()) + " |")
    out("|---|---|" + "---|" * len(levels))
    for printer_id, p in printers.items():
        for nozzle in nozzles:
            cells = []
            for level_id in levels:
                hits = [e for e in pro if e["printer"] == printer_id
                        and e["nozzle"] == nozzle and e["level"] == level_id]
                if not hits:
                    cells.append("—")
                    continue
                entry = hits[0]
                text = f"**{entry['layer_height']}**"
                if entry["layer_height"] != entry["target_layer_height"]:
                    text += " ⁽¹⁾"
                cells.append(text)
            out(f"| {p['label']} | {nozzle} mm | " + " | ".join(cells) + " |")
    out("")
    snapped = [e for e in pro if e["layer_height"] != e["target_layer_height"]]
    if snapped:
        out("⁽¹⁾ Der Zielwert der Stufe ist auf diesem Drucker nicht verfügbar; das")
        out("Profil rastet auf die nächstgelegene freigegebene Schichthöhe ein:")
        out("")
        for e in sorted(snapped, key=lambda e: e["name"]):
            out(f"- `{e['name']}` — Ziel {e['target_layer_height']} mm, "
                f"gesetzt {e['layer_height']} mm (Basis `{e['inherits']}`)")
        out("")

    out("---")
    out("")
    out("## Vererbung")
    out("")
    out("Jedes Profil erbt von einem Originalprofil aus Bambu Studio. Dadurch bleiben")
    out("alle Einstellungen, die dieses Repository nicht setzt, auf den vom Hersteller")
    out("abgestimmten Werten — und wandern bei einem Studio-Update automatisch mit.")
    out("")
    out("<details>")
    out("<summary>Vollständige Liste der Elternprofile</summary>")
    out("")
    out("| Profil | erbt von |")
    out("|---|---|")
    for e in sorted(presets, key=lambda e: (e["kind"], e["name"])):
        out(f"| `{e['name']}` | `{e['inherits']}` |")
    out("")
    out("</details>")
    out("")
    out("## Legende")
    out("")
    out("| Symbol | Bedeutung |")
    out("|---|---|")
    out("| 🟢 | Am Gerät gedruckt und bestätigt |")
    out("| 🔵 | Startwert aus der Bambu-Basis abgeleitet, nicht einzeln gedruckt |")
    out("| ⚠️ | Materialbedingte Einschränkung beachten |")
    out("| 💧 | Auf optische Klarheit abgestimmt, nicht auf Geschwindigkeit |")
    out("| 🧶 | Flexibel, Volumenstrom durch den Extruder begrenzt |")
    out("| — | Kombination nicht ausgeliefert — Düse gesperrt oder Bambu "
        "liefert für dieses Gerät kein Basisprofil |")
    out("")

    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {TARGET.relative_to(ROOT)} ({len(lines)} lines).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
