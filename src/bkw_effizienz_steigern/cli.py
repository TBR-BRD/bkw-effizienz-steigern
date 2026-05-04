"""Small CLI for manual controller tests."""

from __future__ import annotations

import argparse
import json

from .controller import ControllerConfig, ControllerInput, calculate_setpoints


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate BKW inverter setpoints")
    parser.add_argument("--grid", type=float, required=True, help="Grid power W, import positive")
    parser.add_argument("--wr1", type=float, default=0.0, help="Current WR1 setpoint/actual W")
    parser.add_argument("--wr2", type=float, default=0.0, help="Current WR2 setpoint/actual W")
    parser.add_argument("--soc", type=float, default=100.0, help="Battery SOC percent")
    args = parser.parse_args()

    result = calculate_setpoints(
        ControllerInput(
            grid_power_w=args.grid,
            wr1_actual_w=args.wr1,
            wr2_actual_w=args.wr2,
            battery_soc_pct=args.soc,
        ),
        ControllerConfig(),
    )
    print(json.dumps(result.to_dict(), indent=2))


if __name__ == "__main__":
    main()
