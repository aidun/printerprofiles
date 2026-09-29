#!/usr/bin/env python3
"""Prüft die erzeugten Presets in dist/ gegen die Bambu-Studio-Bibliothek.

Aufruf:  python3 tools/validate.py
Rückgabewert 0 = alle Prüfungen bestanden, 1 = mindestens ein Fehler.
"""

from __future__ import annotations

import json
import sys
import tomllib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bambulib import Bibliothek, _zahl  # noqa: E402

WURZEL = Path(__file__).resolve().parent.parent
ZIEL = WURZEL / "dist"
QUELLE = WURZEL / "src"


class Pruefung:
    def __init__(self):
        self.fehler: list[str] = []
        self.anzahl = 0

    def pruefe(self, bedingung: bool, meldung: str) -> None:
        self.anzahl += 1
        if not bedingung:
            self.fehler.append(meldung)


def bekannte_schluessel(bib: Bibliothek) -> tuple[set[str], set[str]]:
    """Alle Schlüssel, die in der Bibliothek überhaupt vorkommen."""
    filament, prozess = set(), set()
    for daten in bib.filamente.values():
        filament.update(daten)
    for daten in bib.prozesse.values():
        prozess.update(daten)
    eigen = {"type", "from", "version", "name", "inherits", "compatible_printers"}
    return filament | eigen, prozess | eigen


def main() -> int:
    bib = Bibliothek()
    p = Pruefung()
    drucker = tomllib.loads((QUELLE / "drucker.toml").read_text(encoding="utf-8"))
    hotend = {d["machine_name"].format(n=n): d["max_hotend"]
              for d in drucker.values() for n in d["nozzles"]}
    filament_keys, prozess_keys = bekannte_schluessel(bib)

    dateien = sorted(ZIEL.rglob("*.json"))
    p.pruefe(bool(dateien), "dist/ enthält keine Presets — erst tools/generate.py ausführen.")
    namen: dict[str, str] = {}

    for datei in dateien:
        if datei.name == "_index.json":
            continue
        kurz = datei.relative_to(WURZEL)
        try:
            d = json.loads(datei.read_text(encoding="utf-8"))
        except json.JSONDecodeError as fehler:
            p.fehler.append(f"{kurz}: kein gültiges JSON ({fehler})")
            continue

        art = d.get("type")
        p.pruefe(art in ("filament", "process"), f"{kurz}: unbekannter type {art!r}")
        p.pruefe(d.get("from") == "User", f"{kurz}: 'from' muss 'User' sein")
        p.pruefe(d.get("name") == datei.stem, f"{kurz}: Dateiname und 'name' weichen ab")
        p.pruefe(d["name"] not in namen, f"{kurz}: Name doppelt vergeben")
        namen[d.get("name", str(kurz))] = str(kurz)

        # Elternprofil muss existieren
        sammlung = bib.filamente if art == "filament" else bib.prozesse
        eltern = d.get("inherits")
        p.pruefe(eltern in sammlung, f"{kurz}: Elternprofil {eltern!r} fehlt in der Bibliothek")

        # Maschine muss existieren und das Elternprofil muss für sie gelten
        maschinen = d.get("compatible_printers") or []
        p.pruefe(len(maschinen) == 1, f"{kurz}: genau eine Maschine erwartet, gefunden {maschinen}")
        for maschine in maschinen:
            p.pruefe(maschine in bib.maschinen, f"{kurz}: Maschine {maschine!r} fehlt")
            if eltern in sammlung and maschine in bib.maschinen:
                erlaubt = bib.aufgeloest(sammlung, eltern).get("compatible_printers") or []
                p.pruefe(maschine in erlaubt,
                         f"{kurz}: Elternprofil {eltern!r} ist für {maschine!r} nicht freigegeben")

        # Unbekannte Schlüssel würden von Bambu Studio stillschweigend verworfen
        erlaubte = filament_keys if art == "filament" else prozess_keys
        for schluessel in d:
            if schluessel in ("filament_settings_id", "print_settings_id"):
                continue
            p.pruefe(schluessel in erlaubte, f"{kurz}: Schlüssel {schluessel!r} kennt Bambu Studio nicht")

        if art == "filament":
            pruefe_filament(p, bib, kurz, d, maschinen, hotend)
        elif art == "process":
            pruefe_prozess(p, bib, kurz, d, maschinen)

    index = ZIEL / "_index.json"
    p.pruefe(index.is_file(), "dist/_index.json fehlt")
    if index.is_file():
        meta = json.loads(index.read_text(encoding="utf-8"))
        gezaehlt = len([f for f in dateien if f.name != "_index.json"])
        p.pruefe(meta["filamentpresets"] + meta["prozesspresets"] == gezaehlt,
                 "dist/_index.json stimmt nicht mit der Zahl der Dateien überein")

    for meldung in p.fehler:
        print(f"FEHLER  {meldung}")
    print(f"\n{p.anzahl} Prüfungen, {len(p.fehler)} Fehler, {len(dateien) - 1} Presets.")
    return 1 if p.fehler else 0


def pruefe_filament(p, bib, kurz, d, maschinen, hotend):
    varianten = d.get("filament_extruder_variant") or []
    p.pruefe(bool(varianten), f"{kurz}: filament_extruder_variant fehlt")
    p.pruefe(len(varianten) == len(set(varianten)), f"{kurz}: Extrudervarianten doppelt")

    for schluessel in ("filament_flow_ratio", "filament_max_volumetric_speed"):
        wert = d.get(schluessel)
        p.pruefe(isinstance(wert, list) and len(wert) == len(varianten),
                 f"{kurz}: {schluessel} braucht {len(varianten)} Einträge, hat {wert}")

    for schluessel, wert in d.items():
        if schluessel.startswith(("nozzle_temp", "hot_plate", "eng_plate", "textured_plate",
                                  "supertack_plate", "fan_", "overhang_fan", "slow_down_layer",
                                  "close_fan", "temperature_vit", "filament_z_hop")):
            p.pruefe(isinstance(wert, list) and len(wert) == 1,
                     f"{kurz}: {schluessel} muss genau einen Eintrag haben, hat {wert}")

    tief = _zahl(d.get("nozzle_temperature_range_low"))
    hoch = _zahl(d.get("nozzle_temperature_range_high"))
    duese = _zahl(d.get("nozzle_temperature"))
    erste = _zahl(d.get("nozzle_temperature_initial_layer"))
    p.pruefe(tief is not None and hoch is not None and tief < hoch,
             f"{kurz}: Temperaturfenster {tief}–{hoch} ist nicht aufsteigend")
    for bezeichnung, wert in (("nozzle_temperature", duese), ("initial_layer", erste)):
        p.pruefe(wert is not None and tief <= wert <= hoch,
                 f"{kurz}: {bezeichnung}={wert} liegt außerhalb von {tief}–{hoch}")
    for maschine in maschinen:
        grenze = hotend.get(maschine)
        if grenze:
            p.pruefe(hoch <= grenze, f"{kurz}: {hoch} °C überschreitet das Hotend-Limit {grenze} °C")

    volumen = _zahl(d.get("filament_max_volumetric_speed"))
    p.pruefe(volumen is not None and 1.0 <= volumen <= 40.0,
             f"{kurz}: Volumenstrom {volumen} mm³/s ist unplausibel")
    fluss = _zahl(d.get("filament_flow_ratio"))
    p.pruefe(fluss is not None and 0.85 <= fluss <= 1.15,
             f"{kurz}: Flussrate {fluss} liegt außerhalb von 0.85–1.15")


def pruefe_prozess(p, bib, kurz, d, maschinen):
    hoehe = _zahl(d.get("layer_height"))
    p.pruefe(hoehe is not None, f"{kurz}: layer_height fehlt")
    for maschine in maschinen:
        if maschine not in bib.maschinen or hoehe is None:
            continue
        unten, oben = bib.schichthoehen_grenzen(maschine)
        p.pruefe(unten is None or hoehe >= unten - 1e-9,
                 f"{kurz}: Schichthöhe {hoehe} unter dem Minimum {unten} von {maschine}")
        p.pruefe(oben is None or hoehe <= oben + 1e-9,
                 f"{kurz}: Schichthöhe {hoehe} über dem Maximum {oben} von {maschine}")
        duese = _zahl(bib.maschine(maschine).get("nozzle_diameter"))
        if duese:
            p.pruefe(hoehe <= duese * 0.75 + 1e-9,
                     f"{kurz}: Schichthöhe {hoehe} über 75 % des Düsendurchmessers {duese}")

    basiswerte = bib.aufgeloest(bib.prozesse, d.get("inherits", ""))
    for schluessel, wert in d.items():
        if isinstance(wert, list) and schluessel.endswith("_speed"):
            basis = basiswerte.get(schluessel)
            p.pruefe(isinstance(basis, list) and len(basis) == len(wert),
                     f"{kurz}: {schluessel} hat {len(wert)} Einträge, das Basisprofil {basis}")
            for eintrag in wert:
                zahl = _zahl(eintrag)
                p.pruefe(zahl is not None and 5 <= zahl <= 1000,
                         f"{kurz}: {schluessel}={eintrag} ist unplausibel")


if __name__ == "__main__":
    raise SystemExit(main())
