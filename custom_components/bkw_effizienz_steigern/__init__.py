from __future__ import annotations

import voluptuous as vol

from homeassistant.const import CONF_ENABLED
from homeassistant.core import HomeAssistant, ServiceCall, SupportsResponse
from homeassistant.helpers import config_validation as cv

from .algorithm import ControllerConfig, ControllerInput, calculate_setpoints
from .const import DOMAIN, SERVICE_CALCULATE_SETPOINTS

SERVICE_SCHEMA = vol.Schema(
    {
        vol.Required("grid_power_w"): vol.Coerce(float),
        vol.Optional("wr1_actual_w", default=0.0): vol.Coerce(float),
        vol.Optional("wr2_actual_w", default=0.0): vol.Coerce(float),
        vol.Optional("battery_soc_pct", default=100.0): vol.Coerce(float),
        vol.Optional(CONF_ENABLED, default=True): cv.boolean,
        vol.Optional("meter_online", default=True): cv.boolean,
        vol.Optional("battery_ok", default=True): cv.boolean,
        vol.Optional("grid_target_w", default=15.0): vol.Coerce(float),
        vol.Optional("deadband_w", default=8.0): vol.Coerce(float),
        vol.Optional("installed_limit_w", default=700.0): vol.Coerce(float),
        vol.Optional("legal_limit_va", default=800.0): vol.Coerce(float),
        vol.Optional("wr1_min_w", default=50.0): vol.Coerce(float),
        vol.Optional("wr1_max_w", default=100.0): vol.Coerce(float),
        vol.Optional("wr2_min_w", default=50.0): vol.Coerce(float),
        vol.Optional("wr2_max_w", default=600.0): vol.Coerce(float),
        vol.Optional("soc_stop_pct", default=20.0): vol.Coerce(float),
    }
)


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    async def handle_calculate(call: ServiceCall) -> dict:
        data = call.data
        cfg = ControllerConfig(
            grid_target_w=data["grid_target_w"],
            deadband_w=data["deadband_w"],
            installed_limit_w=data["installed_limit_w"],
            legal_limit_va=data["legal_limit_va"],
            wr1_min_w=data["wr1_min_w"],
            wr1_max_w=data["wr1_max_w"],
            wr2_min_w=data["wr2_min_w"],
            wr2_max_w=data["wr2_max_w"],
            soc_stop_pct=data["soc_stop_pct"],
        )
        inp = ControllerInput(
            grid_power_w=data["grid_power_w"],
            wr1_actual_w=data["wr1_actual_w"],
            wr2_actual_w=data["wr2_actual_w"],
            battery_soc_pct=data["battery_soc_pct"],
            enabled=data[CONF_ENABLED],
            meter_online=data["meter_online"],
            battery_ok=data["battery_ok"],
        )
        return calculate_setpoints(inp, cfg).to_dict()

    hass.services.async_register(
        DOMAIN,
        SERVICE_CALCULATE_SETPOINTS,
        handle_calculate,
        schema=SERVICE_SCHEMA,
        supports_response=SupportsResponse.ONLY,
    )
    return True
