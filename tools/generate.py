#!/usr/bin/env python3
"""Builds the Bambu Studio presets in dist/ from the TOML sources in src/.

Usage:  python3 tools/generate.py
No external dependencies — Python standard library only.
"""

from __future__ import annotations

import json
import sys
import tomllib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bambulib import Library  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "src"
TARGET = ROOT / "dist"
VERSION = "2.7.0.8"


# --------------------------------------------------------------------------
# Loading the sources
# --------------------------------------------------------------------------

def load_sources():
    printers = tomllib.loads((SOURCE / "printers.toml").read_text(encoding="utf-8"))
    levels = tomllib.loads((SOURCE / "quality.toml").read_text(encoding="utf-8"))
    filaments = {}
    for file in sorted((SOURCE / "filaments").glob("*.toml")):
        data = tomllib.loads(file.read_text(encoding="utf-8"))
        filaments[data["id"]] = data
    filaments = dict(sorted(filaments.items(), key=lambda e: e[1]["order"]))
    return printers, filaments, levels


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

def machine_name(printer: dict, nozzle: str) -> str:
    return printer["machine_name"].format(n=nozzle)


def variants(lib: Library, machine: str) -> list[str]:
    """The machine's extruder variants, without duplicates.

    Bambu lists the variants per extruder, which is why the H2C names them
    twice. Filament presets address the variant, not the extruder — their
    arrays hold only two entries even on the H2C.
    """
    listed = lib.machine(machine).get("extruder_variant_list")
    if not listed:
        return ["Direct Drive Standard"]
    unique: list[str] = []
    for entry in listed:
        for part in entry.split(","):
            part = part.strip()
            if part and part not in unique:
                unique.append(part)
    return unique


def per_variant(value, count: int, filler: str = "nil") -> list[str]:
    """Extruder-dependent value: first entry real, the rest placeholders.

    Bambu Studio expects an array with one entry per variant for
    extruder-dependent filament values. 'nil' means "inherit from the base".
    """
    return [str(value)] + [filler] * (count - 1)


def fmt(value: float, digits: int = 1) -> str:
    rounded = round(value, digits)
    return str(int(rounded)) if rounded == int(rounded) else str(rounded)


def scale(base, factor: float):
    """Applies a factor to a base value and preserves its format."""
    if isinstance(base, list):
        return [fmt(float(e) * factor, 0) if _is_number(e) else e for e in base]
    if _is_number(base):
        return fmt(float(base) * factor, 0)
    return base


def _is_number(value) -> bool:
    try:
        float(value)
        return True
    except (TypeError, ValueError):
        return False


def write(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(data, indent=4, ensure_ascii=False, sort_keys=True)
    path.write_text(text + "\n", encoding="utf-8")


# --------------------------------------------------------------------------
# Filament presets
# --------------------------------------------------------------------------

def build_filament(lib, printer_id, printer, filament, nozzle):
    machine = machine_name(printer, nozzle)
    base = lib.filament_base(filament["base"], machine)
    count = len(variants(lib, machine))
    name = f"{filament['label']} {printer['tag']} {nozzle}"

    temp = filament["temperature"]
    cooling = filament["cooling"]
    flow = filament["volumetric_flow"][nozzle] * printer["flow_factor"]

    preset = {
        "type": "filament",
        "name": name,
        "from": "User",
        "inherits": base,
        "version": VERSION,
        "filament_settings_id": [name],
        "compatible_printers": [machine],
        "filament_extruder_variant": variants(lib, machine),

        "nozzle_temperature": [str(temp["nozzle"])],
        "nozzle_temperature_initial_layer": [str(temp["nozzle_initial"])],
        "nozzle_temperature_range_low": [str(temp["range_low"])],
        "nozzle_temperature_range_high": [str(temp["range_high"])],
        "temperature_vitrification": [str(temp["vitrification"])],

        "hot_plate_temp": [str(temp["bed"])],
        "hot_plate_temp_initial_layer": [str(temp["bed_initial"])],
        "eng_plate_temp": [str(temp["bed"])],
        "eng_plate_temp_initial_layer": [str(temp["bed_initial"])],
        "textured_plate_temp": [str(temp["bed"])],
        "textured_plate_temp_initial_layer": [str(temp["bed_initial"])],
        "supertack_plate_temp": [str(temp["bed"])],
        "supertack_plate_temp_initial_layer": [str(temp["bed_initial"])],

        "fan_min_speed": [str(cooling["fan_min_speed"])],
        "fan_max_speed": [str(cooling["fan_max_speed"])],
        "overhang_fan_speed": [str(cooling["overhang_fan_speed"])],
        "slow_down_layer_time": [str(cooling["slow_down_layer_time"])],
        "fan_cooling_layer_time": [str(cooling["fan_cooling_layer_time"])],
        "close_fan_the_first_x_layers": [str(cooling["close_fan_the_first_x_layers"])],

        "filament_flow_ratio": per_variant(filament["flow"]["ratio"], count),
        "filament_max_volumetric_speed": per_variant(fmt(flow), count),
        "filament_z_hop": [str(filament["retraction"]["z_hop"])],
    }
    meta = {
        "file": f"filament/{name}.json",
        "name": name,
        "kind": "filament",
        "printer": printer_id,
        "filament": filament["id"],
        "nozzle": nozzle,
        "inherits": base,
        "flow": fmt(flow),
        "status": filament["status"],
        "abrasive": filament["abrasive"],
    }
    return name, preset, meta


# --------------------------------------------------------------------------
# Process presets
# --------------------------------------------------------------------------

def build_process(lib, printer_id, printer, nozzle, level_id, level):
    machine = machine_name(printer, nozzle)
    target = level["layer_height"][nozzle]
    base, height = lib.process_base(machine, target, level["base_hint"])
    base_values = lib.resolved(lib.processes, base)
    name = f"{level['label']} {printer['tag']} {nozzle}"

    preset = {
        "type": "process",
        "name": name,
        "from": "User",
        "inherits": base,
        "version": VERSION,
        "print_settings_id": name,
        "compatible_printers": [machine],
        "layer_height": fmt(height, 2),
    }
    preset.update({k: str(v) for k, v in level["parameters"].items()})
    for key, factor in level["speed"].items():
        if key in base_values:
            preset[key] = scale(base_values[key], factor)

    meta = {
        "file": f"process/{name}.json",
        "name": name,
        "kind": "process",
        "printer": printer_id,
        "nozzle": nozzle,
        "level": level_id,
        "inherits": base,
        "layer_height": fmt(height, 2),
        "target_layer_height": fmt(target, 2),
    }
    return name, preset, meta


# --------------------------------------------------------------------------

def main() -> int:
    lib = Library()
    printers, filaments, levels = load_sources()

    for subdir in ("filament", "process"):
        folder = TARGET / subdir
        if folder.is_dir():
            for stale in folder.glob("*.json"):
                stale.unlink()

    index: list[dict] = []

    for printer_id, printer in printers.items():
        for nozzle in printer["nozzles"]:
            for filament in filaments.values():
                if nozzle not in filament["nozzles"]:
                    continue
                name, preset, meta = build_filament(lib, printer_id, printer, filament, nozzle)
                write(TARGET / "filament" / f"{name}.json", preset)
                index.append(meta)
            for level_id, level in levels.items():
                name, preset, meta = build_process(lib, printer_id, printer, nozzle, level_id, level)
                write(TARGET / "process" / f"{name}.json", preset)
                index.append(meta)

    filament_count = sum(1 for e in index if e["kind"] == "filament")
    process_count = sum(1 for e in index if e["kind"] == "process")
    write(TARGET / "_index.json", {
        "library": str(lib.root),
        "filament_presets": filament_count,
        "process_presets": process_count,
        "presets": sorted(index, key=lambda e: (e["kind"], e["name"])),
    })
    print(f"Wrote {filament_count} filament presets and {process_count} process presets to {TARGET}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
