"""Zugriff auf die mitgelieferte Bambu-Studio-Profilbibliothek.

Die Bibliothek ist die einzige Quelle der Wahrheit für Basisprofilnamen,
Vererbungsketten und Maschinengrenzen. Alle Werte werden zur Laufzeit von
dort gelesen — nichts ist im Generator fest verdrahtet.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

# Mögliche Installationsorte, in Prüfreihenfolge.
KANDIDATEN = [
    "/Applications/BambuStudio.app/Contents/Resources/profiles/BBL",
    os.path.expanduser("~/Applications/BambuStudio.app/Contents/Resources/profiles/BBL"),
    "C:/Program Files/Bambu Studio/resources/profiles/BBL",
    os.path.expanduser("~/.config/BambuStudio/system/BBL"),
]


class BibliothekFehlt(RuntimeError):
    pass


def finde_bibliothek() -> Path:
    umgebung = os.environ.get("BAMBU_PROFILE_DIR")
    if umgebung:
        pfad = Path(umgebung)
        if pfad.is_dir():
            return pfad
        raise BibliothekFehlt(f"BAMBU_PROFILE_DIR zeigt auf {pfad!s}, das existiert nicht.")
    for kandidat in KANDIDATEN:
        pfad = Path(kandidat)
        if pfad.is_dir():
            return pfad
    raise BibliothekFehlt(
        "Bambu-Studio-Profilbibliothek nicht gefunden. Bambu Studio installieren "
        "oder BAMBU_PROFILE_DIR auf den Ordner .../profiles/BBL setzen."
    )


class Bibliothek:
    """Lädt Maschinen-, Filament- und Prozessprofile und löst Vererbung auf."""

    def __init__(self, wurzel: Path | None = None):
        self.wurzel = wurzel or finde_bibliothek()
        self.maschinen = self._lade("machine")
        self.filamente = self._lade("filament")
        self.prozesse = self._lade("process")

    def _lade(self, unterordner: str) -> dict[str, dict]:
        treffer: dict[str, dict] = {}
        for datei in sorted((self.wurzel / unterordner).rglob("*.json")):
            try:
                daten = json.loads(datei.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, UnicodeDecodeError):
                continue
            name = daten.get("name")
            if name:
                treffer[name] = daten
        return treffer

    # -- Vererbung -------------------------------------------------------

    def aufgeloest(self, sammlung: dict[str, dict], name: str) -> dict:
        """Führt die komplette inherits-Kette zu einem flachen Dict zusammen."""
        kette: list[dict] = []
        gesehen: set[str] = set()
        aktuell = name
        while aktuell and aktuell in sammlung and aktuell not in gesehen:
            gesehen.add(aktuell)
            knoten = sammlung[aktuell]
            kette.append(knoten)
            aktuell = knoten.get("inherits")
        zusammen: dict = {}
        for knoten in reversed(kette):
            zusammen.update(knoten)
        return zusammen

    def wert(self, sammlung: dict[str, dict], name: str, schluessel: str):
        return self.aufgeloest(sammlung, name).get(schluessel)

    # -- Abfragen --------------------------------------------------------

    def maschine(self, name: str) -> dict:
        if name not in self.maschinen:
            raise KeyError(f"Maschinenprofil '{name}' fehlt in der Bibliothek.")
        return self.aufgeloest(self.maschinen, name)

    def schichthoehen_grenzen(self, maschinenname: str) -> tuple[float, float]:
        m = self.maschine(maschinenname)
        return _zahl(m.get("min_layer_height")), _zahl(m.get("max_layer_height"))

    def kompatible(self, sammlung: dict[str, dict], maschinenname: str) -> list[str]:
        """Alle Profilnamen, die für diese Maschine freigegeben sind."""
        treffer = []
        for name in sammlung:
            voll = self.aufgeloest(sammlung, name)
            drucker = voll.get("compatible_printers")
            if isinstance(drucker, list) and maschinenname in drucker:
                treffer.append(name)
        return sorted(treffer)

    def filament_basis(self, praefix: str, maschinenname: str) -> str:
        """Das für diese Maschine gültige 'Generic PLA'/'Generic PETG'-Profil."""
        kandidaten = [
            n for n in self.kompatible(self.filamente, maschinenname)
            if n == praefix or n.startswith(praefix + " @")
        ]
        if not kandidaten:
            raise KeyError(f"Kein Basisfilament '{praefix}' für '{maschinenname}'.")
        # Spezifischster Treffer zuerst: längerer Name = engerer Geltungsbereich.
        kandidaten.sort(key=lambda n: (-len(n), n))
        return kandidaten[0]

    def prozess_basis(self, maschinenname: str, ziel: float, hinweise: list[str]) -> tuple[str, float]:
        """Basisprozess mit der Schichthöhe, die 'ziel' am nächsten liegt.

        Bei gleichem Abstand entscheidet die Reihenfolge in 'hinweise'; die
        Stufe bekommt so die zu ihr passende Charakteristik (High Quality,
        Draft, ...) statt eines beliebigen Profils.
        """
        untergrenze, obergrenze = self.schichthoehen_grenzen(maschinenname)
        kandidaten = []
        for name in self.kompatible(self.prozesse, maschinenname):
            hoehe = _zahl(self.wert(self.prozesse, name, "layer_height"))
            if hoehe is None:
                continue
            if untergrenze is not None and hoehe < untergrenze - 1e-9:
                continue
            if obergrenze is not None and hoehe > obergrenze + 1e-9:
                continue
            kandidaten.append((name, hoehe))
        if not kandidaten:
            raise KeyError(f"Keine Prozessprofile für '{maschinenname}'.")

        def rang(eintrag):
            name, hoehe = eintrag
            for index, hinweis in enumerate(hinweise):
                if hinweis in name:
                    return index
            return len(hinweise)

        kandidaten.sort(key=lambda e: (round(abs(e[1] - ziel), 6), rang(e), e[0]))
        return kandidaten[0]


def _zahl(wert):
    if wert is None:
        return None
    if isinstance(wert, list):
        wert = wert[0] if wert else None
    if wert in (None, "", "nil"):
        return None
    try:
        return float(wert)
    except (TypeError, ValueError):
        return None
