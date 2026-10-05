#!/usr/bin/env python3
"""Validates the generated presets in dist/ against the Bambu Studio library.

Usage:  python3 tools/validate.py
Exit code 0 = all checks passed, 1 = at least one error.
"""

from __future__ import annotations

import json
import sys
import tomllib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bambulib import Library, _number  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "dist"
SOURCE = ROOT / "src"


class Checker:
    def __init__(self):
        self.errors: list[str] = []
        self.count = 0

    def check(self, condition: bool, message: str) -> None:
        self.count += 1
        if not condition:
            self.errors.append(message)


def known_keys(lib: Library) -> tuple[set[str], set[str]]:
    """Every key that occurs anywhere in the library."""
    filament, process = set(), set()
    for data in lib.filaments.values():
        filament.update(data)
    for data in lib.processes.values():
        process.update(data)
    own = {"type", "from", "version", "name", "inherits", "compatible_printers"}
    return filament | own, process | own


def main() -> int:
    lib = Library()
    c = Checker()
    printers = tomllib.loads((SOURCE / "printers.toml").read_text(encoding="utf-8"))
    hotend = {p["machine_name"].format(n=n): p["max_hotend"]
              for p in printers.values() for n in p["nozzles"]}
    filament_keys, process_keys = known_keys(lib)

    files = sorted(TARGET.rglob("*.json"))
    c.check(bool(files), "dist/ holds no presets — run tools/generate.py first.")
    names: dict[str, str] = {}

    for file in files:
        if file.name == "_index.json":
            continue
        short = file.relative_to(ROOT)
        try:
            d = json.loads(file.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            c.errors.append(f"{short}: not valid JSON ({error})")
            continue

        kind = d.get("type")
        c.check(kind in ("filament", "process"), f"{short}: unknown type {kind!r}")
        c.check(d.get("from") == "User", f"{short}: 'from' must be 'User'")
        c.check(d.get("name") == file.stem, f"{short}: file name and 'name' differ")
        c.check(d.get("name") not in names, f"{short}: name used twice")
        names[d.get("name", str(short))] = str(short)

        # The parent profile must exist
        collection = lib.filaments if kind == "filament" else lib.processes
        parent = d.get("inherits")
        c.check(parent in collection, f"{short}: parent profile {parent!r} missing from the library")

        # The machine must exist and the parent profile must apply to it
        machines = d.get("compatible_printers") or []
        c.check(len(machines) == 1, f"{short}: expected exactly one machine, found {machines}")
        for machine in machines:
            c.check(machine in lib.machines, f"{short}: machine {machine!r} missing")
            if parent in collection and machine in lib.machines:
                allowed = lib.resolved(collection, parent).get("compatible_printers") or []
                c.check(machine in allowed,
                        f"{short}: parent profile {parent!r} is not released for {machine!r}")

        # Unknown keys would be silently discarded by Bambu Studio
        allowed_keys = filament_keys if kind == "filament" else process_keys
        for key in d:
            if key in ("filament_settings_id", "print_settings_id"):
                continue
            c.check(key in allowed_keys, f"{short}: Bambu Studio does not know the key {key!r}")

        if kind == "filament":
            check_filament(c, lib, short, d, machines, hotend)
        elif kind == "process":
            check_process(c, lib, short, d, machines)

    index = TARGET / "_index.json"
    c.check(index.is_file(), "dist/_index.json is missing")
    if index.is_file():
        try:
            meta = json.loads(index.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            meta = None
            c.errors.append(f"dist/_index.json: not valid JSON ({error})")
        if meta is not None:
            counted = len([f for f in files if f.name != "_index.json"])
            c.check(meta.get("filament_presets", 0) + meta.get("process_presets", 0) == counted,
                    "dist/_index.json does not match the number of files")

    for message in c.errors:
        print(f"ERROR  {message}")
    print(f"\n{c.count} checks, {len(c.errors)} errors, {len(files) - 1} presets.")
    return 1 if c.errors else 0


def check_filament(c, lib, short, d, machines, hotend):
    variants = d.get("filament_extruder_variant") or []
    c.check(bool(variants), f"{short}: filament_extruder_variant missing")
    c.check(len(variants) == len(set(variants)), f"{short}: duplicate extruder variants")

    for key in ("filament_flow_ratio", "filament_max_volumetric_speed"):
        value = d.get(key)
        c.check(isinstance(value, list) and len(value) == len(variants),
                f"{short}: {key} needs {len(variants)} entries, has {value}")

    for key, value in d.items():
        if key.startswith(("nozzle_temp", "hot_plate", "eng_plate", "textured_plate",
                           "supertack_plate", "fan_", "overhang_fan", "slow_down_layer",
                           "close_fan", "temperature_vit", "filament_z_hop")):
            c.check(isinstance(value, list) and len(value) == 1,
                    f"{short}: {key} must have exactly one entry, has {value}")

    low = _number(d.get("nozzle_temperature_range_low"))
    high = _number(d.get("nozzle_temperature_range_high"))
    nozzle = _number(d.get("nozzle_temperature"))
    first = _number(d.get("nozzle_temperature_initial_layer"))
    # A missing or unreadable value must produce an error line, never an
    # exception: a preset that is broken is exactly the case this run is for.
    window = low is not None and high is not None and low < high
    c.check(window, f"{short}: temperature window {low}–{high} is not ascending")
    for label, value in (("nozzle_temperature", nozzle), ("initial_layer", first)):
        c.check(value is not None, f"{short}: {label} is missing or not a number")
        if window and value is not None:
            c.check(low <= value <= high,
                    f"{short}: {label}={value} lies outside {low}–{high}")
    for machine in machines:
        limit = hotend.get(machine)
        if limit and high is not None:
            c.check(high <= limit, f"{short}: {high} °C exceeds the hotend limit of {limit} °C")

    flow = _number(d.get("filament_max_volumetric_speed"))
    # The lower bound has to admit the slowest combination the library itself
    # releases: a 0.2 mm nozzle on clarity-optimised PETG (1.0 mm³/s on the
    # X1C) drops to 0.8 on the A1 mini.
    c.check(flow is not None and 0.8 <= flow <= 40.0,
            f"{short}: volumetric flow {flow} mm³/s is implausible")
    ratio = _number(d.get("filament_flow_ratio"))
    c.check(ratio is not None and 0.85 <= ratio <= 1.15,
            f"{short}: flow ratio {ratio} lies outside 0.85–1.15")


def check_process(c, lib, short, d, machines):
    height = _number(d.get("layer_height"))
    c.check(height is not None, f"{short}: layer_height missing")
    for machine in machines:
        if machine not in lib.machines or height is None:
            continue
        lower, upper = lib.layer_height_limits(machine)
        c.check(lower is None or height >= lower - 1e-9,
                f"{short}: layer height {height} below the minimum {lower} of {machine}")
        c.check(upper is None or height <= upper + 1e-9,
                f"{short}: layer height {height} above the maximum {upper} of {machine}")
        nozzle = _number(lib.machine(machine).get("nozzle_diameter"))
        if nozzle:
            c.check(height <= nozzle * 0.75 + 1e-9,
                    f"{short}: layer height {height} above 75 % of the nozzle diameter {nozzle}")

    base_values = lib.resolved(lib.processes, d.get("inherits", ""))
    for key, value in d.items():
        if isinstance(value, list) and key.endswith("_speed"):
            base = base_values.get(key)
            c.check(isinstance(base, list) and len(base) == len(value),
                    f"{short}: {key} has {len(value)} entries, the base profile {base}")
            for entry in value:
                number = _number(entry)
                c.check(number is not None and 5 <= number <= 1000,
                        f"{short}: {key}={entry} is implausible")


if __name__ == "__main__":
    raise SystemExit(main())
