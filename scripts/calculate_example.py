import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from bkw_effizienz_steigern.controller import ControllerConfig, ControllerInput, calculate_setpoints

cfg = ControllerConfig(max_step_up_w=1000, max_step_down_w=1000)

cases = [
    ControllerInput(grid_power_w=40),
    ControllerInput(grid_power_w=85),
    ControllerInput(grid_power_w=480),
    ControllerInput(grid_power_w=1400),
]

for case in cases:
    print(case, "->", calculate_setpoints(case, cfg).to_dict())
