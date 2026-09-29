"""Access to the installed Bambu Studio profile library.

The library is the single source of truth for base profile names, inheritance
chains and machine limits. Every value is read from there at runtime — nothing
is hard-coded in the generator.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

# Possible installation locations, in probe order.
CANDIDATES = [
    "/Applications/BambuStudio.app/Contents/Resources/profiles/BBL",
    os.path.expanduser("~/Applications/BambuStudio.app/Contents/Resources/profiles/BBL"),
    "C:/Program Files/Bambu Studio/resources/profiles/BBL",
    os.path.expanduser("~/.config/BambuStudio/system/BBL"),
]


class LibraryMissing(RuntimeError):
    pass


def find_library() -> Path:
    override = os.environ.get("BAMBU_PROFILE_DIR")
    if override:
        path = Path(override)
        if path.is_dir():
            return path
        raise LibraryMissing(f"BAMBU_PROFILE_DIR points at {path!s}, which does not exist.")
    for candidate in CANDIDATES:
        path = Path(candidate)
        if path.is_dir():
            return path
    raise LibraryMissing(
        "Bambu Studio profile library not found. Install Bambu Studio or point "
        "BAMBU_PROFILE_DIR at the .../profiles/BBL directory."
    )


class Library:
    """Loads machine, filament and process profiles and resolves inheritance."""

    def __init__(self, root: Path | None = None):
        self.root = root or find_library()
        self.machines = self._load("machine")
        self.filaments = self._load("filament")
        self.processes = self._load("process")

    def _load(self, subdir: str) -> dict[str, dict]:
        found: dict[str, dict] = {}
        for file in sorted((self.root / subdir).rglob("*.json")):
            try:
                data = json.loads(file.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, UnicodeDecodeError):
                continue
            name = data.get("name")
            if name:
                found[name] = data
        return found

    # -- Inheritance -----------------------------------------------------

    def resolved(self, collection: dict[str, dict], name: str) -> dict:
        """Flattens the complete inherits chain into a single dict."""
        chain: list[dict] = []
        seen: set[str] = set()
        current = name
        while current and current in collection and current not in seen:
            seen.add(current)
            node = collection[current]
            chain.append(node)
            current = node.get("inherits")
        merged: dict = {}
        for node in reversed(chain):
            merged.update(node)
        return merged

    def value(self, collection: dict[str, dict], name: str, key: str):
        return self.resolved(collection, name).get(key)

    # -- Queries ---------------------------------------------------------

    def machine(self, name: str) -> dict:
        if name not in self.machines:
            raise KeyError(f"Machine profile '{name}' is missing from the library.")
        return self.resolved(self.machines, name)

    def layer_height_limits(self, machine_name: str) -> tuple[float, float]:
        m = self.machine(machine_name)
        return _number(m.get("min_layer_height")), _number(m.get("max_layer_height"))

    def compatible(self, collection: dict[str, dict], machine_name: str) -> list[str]:
        """All profile names released for this machine."""
        found = []
        for name in collection:
            full = self.resolved(collection, name)
            printers = full.get("compatible_printers")
            if isinstance(printers, list) and machine_name in printers:
                found.append(name)
        return sorted(found)

    def filament_base(self, prefix: str, machine_name: str) -> str:
        """The 'Generic PLA'/'Generic PETG' profile valid for this machine."""
        candidates = [
            n for n in self.compatible(self.filaments, machine_name)
            if n == prefix or n.startswith(prefix + " @")
        ]
        if not candidates:
            raise KeyError(f"No base filament '{prefix}' for '{machine_name}'.")
        # Most specific match first: a longer name means a narrower scope.
        candidates.sort(key=lambda n: (-len(n), n))
        return candidates[0]

    def process_base(self, machine_name: str, target: float, hints: list[str]) -> tuple[str, float]:
        """Base process whose layer height is closest to 'target'.

        On a tie the order in 'hints' decides, so the level gets a base with a
        matching characteristic (High Quality, Draft, ...) instead of an
        arbitrary profile.
        """
        lower, upper = self.layer_height_limits(machine_name)
        candidates = []
        for name in self.compatible(self.processes, machine_name):
            height = _number(self.value(self.processes, name, "layer_height"))
            if height is None:
                continue
            if lower is not None and height < lower - 1e-9:
                continue
            if upper is not None and height > upper + 1e-9:
                continue
            candidates.append((name, height))
        if not candidates:
            raise KeyError(f"No process profiles for '{machine_name}'.")

        def rank(entry):
            name, _height = entry
            for index, hint in enumerate(hints):
                if hint in name:
                    return index
            return len(hints)

        candidates.sort(key=lambda e: (round(abs(e[1] - target), 6), rank(e), e[0]))
        return candidates[0]


def _number(value):
    if value is None:
        return None
    if isinstance(value, list):
        value = value[0] if value else None
    if value in (None, "", "nil"):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
