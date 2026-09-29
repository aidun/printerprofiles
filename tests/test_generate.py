"""Tests for the generator logic.

Usage:  python3 -m unittest discover -s tests -v
"""

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import generate  # noqa: E402
from bambulib import Library  # noqa: E402


class TestHelpers(unittest.TestCase):
    def test_fmt_drops_trailing_zero(self):
        self.assertEqual(generate.fmt(21.0), "21")
        self.assertEqual(generate.fmt(12.649), "12.6")

    def test_per_variant_pads_with_nil(self):
        self.assertEqual(generate.per_variant(0.98, 1), ["0.98"])
        self.assertEqual(generate.per_variant(0.98, 2), ["0.98", "nil"])

    def test_scale_keeps_array_format(self):
        self.assertEqual(generate.scale(["200", "350"], 0.5), ["100", "175"])
        self.assertEqual(generate.scale("200", 0.5), "100")

    def test_scale_leaves_text_untouched(self):
        self.assertEqual(generate.scale("aligned", 2.0), "aligned")


class TestLibrary(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lib = Library()

    def test_inheritance_is_resolved(self):
        # layer_height is not in the leaf profile but in its parent chain.
        values = self.lib.resolved(self.lib.processes, "0.20mm Standard @BBL X1C")
        self.assertEqual(values["layer_height"], "0.2")

    def test_filament_base_is_machine_specific(self):
        self.assertEqual(
            self.lib.filament_base("Generic PETG", "Bambu Lab H2C 0.4 nozzle"),
            "Generic PETG @BBL H2C 0.4 nozzle")
        self.assertEqual(
            self.lib.filament_base("Generic PLA", "Bambu Lab X1 Carbon 0.4 nozzle"),
            "Generic PLA")

    def test_process_base_stays_within_machine_limits(self):
        # With a 0.2 mm nozzle the H2C offers at most 0.12 mm; the target of
        # 0.14 mm must snap downwards instead of setting an invalid height.
        name, height = self.lib.process_base(
            "Bambu Lab H2C 0.2 nozzle", 0.14, ["Draft", "Standard"])
        self.assertLessEqual(height, 0.12)
        self.assertIn("H2C", name)

    def test_process_base_hits_exactly_when_available(self):
        _, height = self.lib.process_base(
            "Bambu Lab X1 Carbon 0.4 nozzle", 0.12, ["High Quality"])
        self.assertAlmostEqual(height, 0.12)

    def test_extruder_variants_are_unique(self):
        variants = generate.variants(self.lib, "Bambu Lab H2C 0.4 nozzle")
        self.assertEqual(variants, ["Direct Drive Standard", "Direct Drive High Flow"])
        self.assertEqual(generate.variants(self.lib, "Bambu Lab A1 0.4 nozzle"),
                         ["Direct Drive Standard"])


class TestSources(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.printers, cls.filaments, cls.levels = generate.load_sources()

    def test_all_printers_and_nozzles_present(self):
        self.assertEqual(set(self.printers), {"h2c", "x1c", "p1s", "a1", "a1mini"})
        for printer in self.printers.values():
            self.assertEqual(printer["nozzles"], ["0.2", "0.4", "0.6"])

    def test_glow_filaments_exclude_the_02_nozzle(self):
        # Strontium aluminate reliably clogs the 0.2 mm nozzle.
        for key in ("sunlu-pla-glow", "sunlu-petg-glow"):
            self.assertNotIn("0.2", self.filaments[key]["nozzles"])
            self.assertTrue(self.filaments[key]["abrasive"])

    def test_temperature_windows_are_consistent(self):
        for filament in self.filaments.values():
            t = filament["temperature"]
            self.assertLess(t["range_low"], t["range_high"])
            self.assertLessEqual(t["range_low"], t["nozzle"])
            self.assertLessEqual(t["nozzle"], t["range_high"])

    def test_levels_increase_in_layer_height(self):
        for nozzle in ("0.2", "0.4", "0.6"):
            heights = [self.levels[level]["layer_height"][nozzle]
                       for level in ("quality", "normal", "fast")]
            self.assertEqual(heights, sorted(heights))


class TestGeneratedPresets(unittest.TestCase):
    """Checks the outcome of a complete run."""

    @classmethod
    def setUpClass(cls):
        cls.lib = Library()
        cls.printers, cls.filaments, cls.levels = generate.load_sources()

    def test_preset_counts(self):
        filament = sum(len(f["nozzles"]) for f in self.filaments.values()) * len(self.printers)
        process = len(self.printers) * 3 * len(self.levels)
        self.assertEqual((filament, process), (50, 45))

    def test_verified_reference_preset_is_reproduced(self):
        # Values confirmed on the machine for SUNLU PETG Glow, H2C, 0.4 mm.
        _, preset, _ = generate.build_filament(
            self.lib, "h2c", self.printers["h2c"], self.filaments["sunlu-petg-glow"], "0.4")
        self.assertEqual(preset["inherits"], "Generic PETG @BBL H2C 0.4 nozzle")
        self.assertEqual(preset["filament_flow_ratio"], ["0.98", "nil"])
        self.assertEqual(preset["filament_max_volumetric_speed"], ["12.6", "nil"])
        self.assertEqual(preset["nozzle_temperature_range_low"], ["245"])
        self.assertEqual(preset["nozzle_temperature_range_high"], ["250"])
        self.assertEqual(preset["hot_plate_temp_initial_layer"], ["75"])
        self.assertEqual(preset["temperature_vitrification"], ["71"])
        self.assertEqual(preset["fan_min_speed"], ["10"])
        self.assertEqual(preset["fan_max_speed"], ["30"])

    def test_volumetric_flow_scales_with_the_printer(self):
        values = {}
        for key in ("h2c", "x1c", "a1mini"):
            _, preset, _ = generate.build_filament(
                self.lib, key, self.printers[key], self.filaments["sunlu-pla"], "0.4")
            values[key] = float(preset["filament_max_volumetric_speed"][0])
        self.assertGreater(values["h2c"], values["x1c"])
        self.assertGreater(values["x1c"], values["a1mini"])

    def test_process_preset_inherits_the_base_array_format(self):
        _, preset, _ = generate.build_process(
            self.lib, "h2c", self.printers["h2c"], "0.4", "quality", self.levels["quality"])
        base = self.lib.resolved(self.lib.processes, preset["inherits"])
        self.assertEqual(len(preset["outer_wall_speed"]), len(base["outer_wall_speed"]))

    def test_quality_is_slower_than_fast(self):
        speed = {}
        for level in ("quality", "fast"):
            _, preset, _ = generate.build_process(
                self.lib, "x1c", self.printers["x1c"], "0.4", level, self.levels[level])
            speed[level] = float(preset["outer_wall_speed"][0])
        self.assertLess(speed["quality"], speed["fast"])


class TestDistIsCurrent(unittest.TestCase):
    def test_index_describes_every_file(self):
        index = json.loads((ROOT / "dist" / "_index.json").read_text(encoding="utf-8"))
        files = {p.name for p in (ROOT / "dist").rglob("*.json") if p.name != "_index.json"}
        self.assertEqual({e["name"] + ".json" for e in index["presets"]}, files)


if __name__ == "__main__":
    unittest.main()
