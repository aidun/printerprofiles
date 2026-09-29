#!/usr/bin/env python3
"""Erzeugt aus den TOML-Quellen in src/ die Bambu-Studio-Presets in dist/.

Aufruf:  python3 tools/generate.py
Keine externen Abhängigkeiten — nur die Python-Standardbibliothek.
"""

from __future__ import annotations

import json
import sys
import tomllib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bambulib import Bibliothek  # noqa: E402

WURZEL = Path(__file__).resolve().parent.parent
QUELLE = WURZEL / "src"
ZIEL = WURZEL / "dist"
VERSION = "2.7.0.8"


# --------------------------------------------------------------------------
# Quellen laden
# --------------------------------------------------------------------------

def lade_quellen():
    drucker = tomllib.loads((QUELLE / "drucker.toml").read_text(encoding="utf-8"))
    stufen = tomllib.loads((QUELLE / "qualitaet.toml").read_text(encoding="utf-8"))
    filamente = {}
    for datei in sorted((QUELLE / "filamente").glob("*.toml")):
        daten = tomllib.loads(datei.read_text(encoding="utf-8"))
        filamente[daten["id"]] = daten
    filamente = dict(sorted(filamente.items(), key=lambda e: e[1]["reihenfolge"]))
    return drucker, filamente, stufen


# --------------------------------------------------------------------------
# Hilfsfunktionen
# --------------------------------------------------------------------------

def maschinenname(drucker: dict, duese: str) -> str:
    return drucker["machine_name"].format(n=duese)


def varianten(bib: Bibliothek, maschine: str) -> list[str]:
    """Extrudervarianten der Maschine, ohne Dopplungen.

    Bambu listet die Varianten je Extruder auf; der H2C nennt sie deshalb
    zweimal. Filamentpresets adressieren aber die Variante, nicht den
    Extruder — ihre Arrays haben auch beim H2C nur zwei Einträge.
    """
    liste = bib.maschine(maschine).get("extruder_variant_list")
    if not liste:
        return ["Direct Drive Standard"]
    eindeutig: list[str] = []
    for eintrag in liste:
        for teil in eintrag.split(","):
            teil = teil.strip()
            if teil and teil not in eindeutig:
                eindeutig.append(teil)
    return eindeutig


def je_variante(wert, anzahl: int, fuellwert: str = "nil") -> list[str]:
    """Extruderabhängiger Wert: erster Eintrag echt, Rest Platzhalter.

    Bambu Studio erwartet für extruderabhängige Filamentwerte ein Array mit
    einem Eintrag je Variante. 'nil' bedeutet "vom Basisprofil übernehmen".
    """
    return [str(wert)] + [fuellwert] * (anzahl - 1)


def rund(wert: float, stellen: int = 1) -> str:
    gerundet = round(wert, stellen)
    return str(int(gerundet)) if gerundet == int(gerundet) else str(gerundet)


def skaliere(basis, faktor: float):
    """Wendet einen Faktor auf einen Basiswert an und behält dessen Format."""
    if isinstance(basis, list):
        return [rund(float(e) * faktor, 0) if _ist_zahl(e) else e for e in basis]
    if _ist_zahl(basis):
        return rund(float(basis) * faktor, 0)
    return basis


def _ist_zahl(wert) -> bool:
    try:
        float(wert)
        return True
    except (TypeError, ValueError):
        return False


def schreibe(pfad: Path, daten: dict) -> None:
    pfad.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(daten, indent=4, ensure_ascii=False, sort_keys=True)
    pfad.write_text(text + "\n", encoding="utf-8")


# --------------------------------------------------------------------------
# Filamentpresets
# --------------------------------------------------------------------------

def baue_filament(bib, drucker_id, drucker, filament, duese):
    maschine = maschinenname(drucker, duese)
    basis = bib.filament_basis(filament["basis"], maschine)
    anzahl = len(varianten(bib, maschine))
    name = f"{filament['label']} {drucker['tag']} {duese}"

    temperatur = filament["temperatur"]
    kuehlung = filament["kuehlung"]
    volumen = filament["volumenstrom"][duese] * drucker["flow_factor"]
    # Kein Drucker darf über die Schmelzleistung seines Hotends hinaus gefahren
    # werden; der Deckel ist konservativ auf das 0.6-mm-Niveau bezogen.
    volumen = min(volumen, 30.0)

    preset = {
        "type": "filament",
        "name": name,
        "from": "User",
        "inherits": basis,
        "version": VERSION,
        "filament_settings_id": [name],
        "compatible_printers": [maschine],
        "filament_extruder_variant": varianten(bib, maschine),

        "nozzle_temperature": [str(temperatur["nozzle"])],
        "nozzle_temperature_initial_layer": [str(temperatur["nozzle_initial"])],
        "nozzle_temperature_range_low": [str(temperatur["range_low"])],
        "nozzle_temperature_range_high": [str(temperatur["range_high"])],
        "temperature_vitrification": [str(temperatur["vitrification"])],

        "hot_plate_temp": [str(temperatur["bett"])],
        "hot_plate_temp_initial_layer": [str(temperatur["bett_initial"])],
        "eng_plate_temp": [str(temperatur["bett"])],
        "eng_plate_temp_initial_layer": [str(temperatur["bett_initial"])],
        "textured_plate_temp": [str(temperatur["bett"])],
        "textured_plate_temp_initial_layer": [str(temperatur["bett_initial"])],
        "supertack_plate_temp": [str(temperatur["bett"])],
        "supertack_plate_temp_initial_layer": [str(temperatur["bett_initial"])],

        "fan_min_speed": [str(kuehlung["fan_min_speed"])],
        "fan_max_speed": [str(kuehlung["fan_max_speed"])],
        "overhang_fan_speed": [str(kuehlung["overhang_fan_speed"])],
        "slow_down_layer_time": [str(kuehlung["slow_down_layer_time"])],
        "fan_cooling_layer_time": [str(kuehlung["fan_cooling_layer_time"])],
        "close_fan_the_first_x_layers": [str(kuehlung["close_fan_the_first_x_layers"])],

        "filament_flow_ratio": je_variante(filament["fluss"]["ratio"], anzahl),
        "filament_max_volumetric_speed": je_variante(rund(volumen), anzahl),
        "filament_z_hop": [str(filament["retraction"]["z_hop"])],
    }
    meta = {
        "datei": f"filament/{name}.json",
        "name": name,
        "art": "filament",
        "drucker": drucker_id,
        "filament": filament["id"],
        "duese": duese,
        "inherits": basis,
        "volumenstrom": rund(volumen),
        "status": filament["status"],
        "abrasiv": filament["abrasiv"],
    }
    return name, preset, meta


# --------------------------------------------------------------------------
# Prozesspresets
# --------------------------------------------------------------------------

def baue_prozess(bib, drucker_id, drucker, duese, stufen_id, stufe):
    maschine = maschinenname(drucker, duese)
    ziel = stufe["schichthoehe"][duese]
    basis, hoehe = bib.prozess_basis(maschine, ziel, stufe["basis_hint"])
    basiswerte = bib.aufgeloest(bib.prozesse, basis)
    name = f"{stufe['label']} {drucker['tag']} {duese}"

    preset = {
        "type": "process",
        "name": name,
        "from": "User",
        "inherits": basis,
        "version": VERSION,
        "print_settings_id": name,
        "compatible_printers": [maschine],
        "layer_height": rund(hoehe, 2),
    }
    preset.update({k: str(v) for k, v in stufe["parameter"].items()})
    for schluessel, faktor in stufe["tempo"].items():
        if schluessel in basiswerte:
            preset[schluessel] = skaliere(basiswerte[schluessel], faktor)

    meta = {
        "datei": f"process/{name}.json",
        "name": name,
        "art": "process",
        "drucker": drucker_id,
        "duese": duese,
        "stufe": stufen_id,
        "inherits": basis,
        "schichthoehe": rund(hoehe, 2),
        "ziel_schichthoehe": rund(ziel, 2),
    }
    return name, preset, meta


# --------------------------------------------------------------------------

def main() -> int:
    bib = Bibliothek()
    drucker_alle, filamente, stufen = lade_quellen()

    for unterordner in ("filament", "process"):
        ordner = ZIEL / unterordner
        if ordner.is_dir():
            for alt in ordner.glob("*.json"):
                alt.unlink()

    index: list[dict] = []

    for drucker_id, drucker in drucker_alle.items():
        for duese in drucker["nozzles"]:
            for filament in filamente.values():
                if duese not in filament["duesen"]:
                    continue
                name, preset, meta = baue_filament(bib, drucker_id, drucker, filament, duese)
                schreibe(ZIEL / "filament" / f"{name}.json", preset)
                index.append(meta)
            for stufen_id, stufe in stufen.items():
                name, preset, meta = baue_prozess(bib, drucker_id, drucker, duese, stufen_id, stufe)
                schreibe(ZIEL / "process" / f"{name}.json", preset)
                index.append(meta)

    filament_anzahl = sum(1 for e in index if e["art"] == "filament")
    prozess_anzahl = sum(1 for e in index if e["art"] == "process")
    schreibe(ZIEL / "_index.json", {
        "bibliothek": str(bib.wurzel),
        "filamentpresets": filament_anzahl,
        "prozesspresets": prozess_anzahl,
        "presets": sorted(index, key=lambda e: (e["art"], e["name"])),
    })
    print(f"{filament_anzahl} Filamentpresets, {prozess_anzahl} Prozesspresets nach {ZIEL} geschrieben.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
