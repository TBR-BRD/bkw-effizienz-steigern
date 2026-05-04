from __future__ import annotations

from dataclasses import asdict, dataclass


def clamp(value: float, lower: float, upper: float) -> float:
    return max(lower, min(upper, value))


@dataclass(frozen=True)
class ControllerConfig:
    grid_target_w: float = 15.0
    deadband_w: float = 8.0
    installed_limit_w: float = 700.0
    legal_limit_va: float = 800.0
    wr1_min_w: float = 50.0
    wr1_max_w: float = 100.0
    wr2_min_w: float = 50.0
    wr2_max_w: float = 600.0
    soc_stop_pct: float = 20.0

    @property
    def hard_cap_w(self) -> float:
        return min(self.installed_limit_w, self.legal_limit_va, self.wr1_max_w + self.wr2_max_w)


@dataclass(frozen=True)
class ControllerInput:
    grid_power_w: float
    wr1_actual_w: float = 0.0
    wr2_actual_w: float = 0.0
    battery_soc_pct: float = 100.0
    enabled: bool = True
    meter_online: bool = True
    battery_ok: bool = True


@dataclass(frozen=True)
class ControllerOutput:
    wr1_setpoint_w: float
    wr2_setpoint_w: float
    total_setpoint_w: float
    desired_total_w: float
    reason: str
    safety_off: bool = False

    def to_dict(self) -> dict:
        return asdict(self)


def distribute_power(total_w: float, cfg: ControllerConfig) -> tuple[float, float]:
    total_w = clamp(total_w, 0.0, cfg.hard_cap_w)
    if total_w < cfg.wr1_min_w:
        return 0.0, 0.0
    if total_w <= cfg.wr1_max_w:
        return round(total_w, 1), 0.0
    wr1 = cfg.wr1_max_w
    wr2 = total_w - wr1
    if wr2 < cfg.wr2_min_w:
        return round(wr1, 1), 0.0
    return round(wr1, 1), round(clamp(wr2, cfg.wr2_min_w, cfg.wr2_max_w), 1)


def calculate_setpoints(inp: ControllerInput, cfg: ControllerConfig | None = None) -> ControllerOutput:
    cfg = cfg or ControllerConfig()
    if not inp.enabled:
        return ControllerOutput(0, 0, 0, 0, "disabled", True)
    if not inp.meter_online:
        return ControllerOutput(0, 0, 0, 0, "meter_offline", True)
    if not inp.battery_ok:
        return ControllerOutput(0, 0, 0, 0, "battery_not_ok", True)
    if inp.battery_soc_pct <= cfg.soc_stop_pct:
        return ControllerOutput(0, 0, 0, 0, "soc_below_stop", True)

    current_total = max(0.0, inp.wr1_actual_w) + max(0.0, inp.wr2_actual_w)
    error = inp.grid_power_w - cfg.grid_target_w
    if abs(error) <= cfg.deadband_w:
        desired_total = current_total
        reason = "deadband_hold"
    else:
        desired_total = current_total + error
        reason = "tracking"
    desired_total = clamp(desired_total, 0.0, cfg.hard_cap_w)
    wr1, wr2 = distribute_power(desired_total, cfg)
    return ControllerOutput(wr1, wr2, round(wr1 + wr2, 1), round(desired_total, 1), reason, False)
