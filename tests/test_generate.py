"""Tests für die Generatorlogik.

Aufruf:  python3 -m unittest discover -s tests -v
"""

import json
import sys
import tomllib
import unittest
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WURZEL / "tools"))

import generate  # noqa: E402
from bambulib import Bibliothek  # noqa: E402


class TestHilfsfunktionen(unittest.TestCase):
    def test_rund_entfernt_nachkommanull(self):
        self.assertEqual(generate.rund(21.0), "21")
        self.assertEqual(generate.rund(12.649), "12.6")

    def test_je_variante_fuellt_mit_nil(self):
        self.assertEqual(generate.je_variante(0.98, 1), ["0.98"])
        self.assertEqual(generate.je_variante(0.98, 2), ["0.98", "nil"])

    def test_skaliere_behaelt_arrayformat(self):
        self.assertEqual(generate.skaliere(["200", "350"], 0.5), ["100", "175"])
        self.assertEqual(generate.skaliere("200", 0.5), "100")

    def test_skaliere_laesst_text_unveraendert(self):
        self.assertEqual(generate.skaliere("aligned", 2.0), "aligned")


class TestBibliothek(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bib = Bibliothek()

    def test_vererbung_wird_aufgeloest(self):
        # layer_height steht nicht im Blattprofil, sondern in dessen Elternkette.
        werte = self.bib.aufgeloest(self.bib.prozesse, "0.20mm Standard @BBL X1C")
        self.assertEqual(werte["layer_height"], "0.2")

    def test_filamentbasis_ist_maschinenspezifisch(self):
        self.assertEqual(
            self.bib.filament_basis("Generic PETG", "Bambu Lab H2C 0.4 nozzle"),
            "Generic PETG @BBL H2C 0.4 nozzle")
        self.assertEqual(
            self.bib.filament_basis("Generic PLA", "Bambu Lab X1 Carbon 0.4 nozzle"),
            "Generic PLA")

    def test_prozessbasis_bleibt_in_den_maschinengrenzen(self):
        # Der H2C bietet mit 0.2 mm Düse höchstens 0.12 mm an; das Ziel 0.14 mm
        # muss deshalb nach unten einrasten statt eine ungültige Höhe zu setzen.
        name, hoehe = self.bib.prozess_basis(
            "Bambu Lab H2C 0.2 nozzle", 0.14, ["Draft", "Standard"])
        self.assertLessEqual(hoehe, 0.12)
        self.assertIn("H2C", name)

    def test_prozessbasis_trifft_exakt_wenn_vorhanden(self):
        _, hoehe = self.bib.prozess_basis(
            "Bambu Lab X1 Carbon 0.4 nozzle", 0.12, ["High Quality"])
        self.assertAlmostEqual(hoehe, 0.12)

    def test_extrudervarianten_sind_eindeutig(self):
        varianten = generate.varianten(self.bib, "Bambu Lab H2C 0.4 nozzle")
        self.assertEqual(varianten, ["Direct Drive Standard", "Direct Drive High Flow"])
        self.assertEqual(generate.varianten(self.bib, "Bambu Lab A1 0.4 nozzle"),
                         ["Direct Drive Standard"])


class TestQuellen(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.drucker, cls.filamente, cls.stufen = generate.lade_quellen()

    def test_alle_drucker_und_duesen_vorhanden(self):
        self.assertEqual(set(self.drucker), {"h2c", "x1c", "p1s", "a1", "a1mini"})
        for drucker in self.drucker.values():
            self.assertEqual(drucker["nozzles"], ["0.2", "0.4", "0.6"])

    def test_glow_filamente_sperren_die_02er_duese(self):
        # Strontiumaluminat verstopft die 0.2-mm-Düse zuverlässig.
        for kennung in ("sunlu-pla-glow", "sunlu-petg-glow"):
            self.assertNotIn("0.2", self.filamente[kennung]["duesen"])
            self.assertTrue(self.filamente[kennung]["abrasiv"])

    def test_temperaturfenster_sind_schluessig(self):
        for filament in self.filamente.values():
            t = filament["temperatur"]
            self.assertLess(t["range_low"], t["range_high"])
            self.assertLessEqual(t["range_low"], t["nozzle"])
            self.assertLessEqual(t["nozzle"], t["range_high"])

    def test_stufen_steigen_in_der_schichthoehe(self):
        for duese in ("0.2", "0.4", "0.6"):
            hoehen = [self.stufen[s]["schichthoehe"][duese]
                      for s in ("qualitaet", "normal", "schnell")]
            self.assertEqual(hoehen, sorted(hoehen))


class TestErzeugtePresets(unittest.TestCase):
    """Prüft das Ergebnis eines vollständigen Laufs."""

    @classmethod
    def setUpClass(cls):
        cls.bib = Bibliothek()
        cls.drucker, cls.filamente, cls.stufen = generate.lade_quellen()

    def test_anzahl_der_presets(self):
        filament = sum(len(f["duesen"]) for f in self.filamente.values()) * len(self.drucker)
        prozess = len(self.drucker) * 3 * len(self.stufen)
        self.assertEqual((filament, prozess), (50, 45))

    def test_verifiziertes_referenzpreset_wird_reproduziert(self):
        # Am Gerät bestätigte Werte für SUNLU PETG Glow, H2C, 0.4 mm.
        _, preset, _ = generate.baue_filament(
            self.bib, "h2c", self.drucker["h2c"], self.filamente["sunlu-petg-glow"], "0.4")
        self.assertEqual(preset["inherits"], "Generic PETG @BBL H2C 0.4 nozzle")
        self.assertEqual(preset["filament_flow_ratio"], ["0.98", "nil"])
        self.assertEqual(preset["filament_max_volumetric_speed"], ["12.6", "nil"])
        self.assertEqual(preset["nozzle_temperature_range_low"], ["245"])
        self.assertEqual(preset["nozzle_temperature_range_high"], ["250"])
        self.assertEqual(preset["hot_plate_temp_initial_layer"], ["75"])
        self.assertEqual(preset["temperature_vitrification"], ["71"])
        self.assertEqual(preset["fan_min_speed"], ["10"])
        self.assertEqual(preset["fan_max_speed"], ["30"])

    def test_volumenstrom_skaliert_mit_dem_drucker(self):
        werte = {}
        for kennung in ("h2c", "x1c", "a1mini"):
            _, preset, _ = generate.baue_filament(
                self.bib, kennung, self.drucker[kennung], self.filamente["sunlu-pla"], "0.4")
            werte[kennung] = float(preset["filament_max_volumetric_speed"][0])
        self.assertGreater(werte["h2c"], werte["x1c"])
        self.assertGreater(werte["x1c"], werte["a1mini"])

    def test_prozesspreset_erbt_das_arrayformat_der_basis(self):
        _, preset, _ = generate.baue_prozess(
            self.bib, "h2c", self.drucker["h2c"], "0.4", "qualitaet", self.stufen["qualitaet"])
        basis = self.bib.aufgeloest(self.bib.prozesse, preset["inherits"])
        self.assertEqual(len(preset["outer_wall_speed"]), len(basis["outer_wall_speed"]))

    def test_qualitaet_ist_langsamer_als_schnell(self):
        tempo = {}
        for stufe in ("qualitaet", "schnell"):
            _, preset, _ = generate.baue_prozess(
                self.bib, "x1c", self.drucker["x1c"], "0.4", stufe, self.stufen[stufe])
            tempo[stufe] = float(preset["outer_wall_speed"][0])
        self.assertLess(tempo["qualitaet"], tempo["schnell"])


class TestDistIstAktuell(unittest.TestCase):
    def test_index_beschreibt_alle_dateien(self):
        index = json.loads((WURZEL / "dist" / "_index.json").read_text(encoding="utf-8"))
        dateien = {p.name for p in (WURZEL / "dist").rglob("*.json") if p.name != "_index.json"}
        self.assertEqual({e["name"] + ".json" for e in index["presets"]}, dateien)


if __name__ == "__main__":
    unittest.main()
