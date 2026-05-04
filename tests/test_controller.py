import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from bkw_effizienz_steigern.controller import (  # noqa: E402
    ControllerConfig,
    ControllerInput,
    calculate_setpoints,
)


class ControllerTests(unittest.TestCase):
    def cfg_fast(self):
        return ControllerConfig(max_step_up_w=1000, max_step_down_w=1000)

    def test_low_load_below_min_switches_off(self):
        out = calculate_setpoints(ControllerInput(grid_power_w=40), self.cfg_fast())
        self.assertEqual(out.wr1_setpoint_w, 0)
        self.assertEqual(out.wr2_setpoint_w, 0)

    def test_base_load_uses_wr1_only(self):
        out = calculate_setpoints(ControllerInput(grid_power_w=85), self.cfg_fast())
        self.assertEqual(out.wr1_setpoint_w, 70)
        self.assertEqual(out.wr2_setpoint_w, 0)

    def test_mid_load_uses_both(self):
        out = calculate_setpoints(ControllerInput(grid_power_w=480), self.cfg_fast())
        self.assertEqual(out.wr1_setpoint_w, 100)
        self.assertEqual(out.wr2_setpoint_w, 365)

    def test_hard_cap_700(self):
        out = calculate_setpoints(ControllerInput(grid_power_w=1200), self.cfg_fast())
        self.assertEqual(out.total_setpoint_w, 700)
        self.assertEqual(out.wr1_setpoint_w, 100)
        self.assertEqual(out.wr2_setpoint_w, 600)

    def test_meter_offline_is_safety_off(self):
        out = calculate_setpoints(ControllerInput(grid_power_w=200, meter_online=False), self.cfg_fast())
        self.assertTrue(out.safety_off)
        self.assertEqual(out.total_setpoint_w, 0)

    def test_soc_stop_is_safety_off(self):
        out = calculate_setpoints(ControllerInput(grid_power_w=200, battery_soc_pct=10), self.cfg_fast())
        self.assertTrue(out.safety_off)
        self.assertEqual(out.total_setpoint_w, 0)

    def test_deadband_hold(self):
        out = calculate_setpoints(
            ControllerInput(grid_power_w=18, wr1_actual_w=100, wr2_actual_w=0),
            self.cfg_fast(),
        )
        self.assertEqual(out.reason, "deadband_hold")
        self.assertEqual(out.total_setpoint_w, 100)


if __name__ == "__main__":
    unittest.main()
