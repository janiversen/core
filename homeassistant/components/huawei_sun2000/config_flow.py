"""Config flow for Huawei sun2000."""
import my_pypi_dependency

from homeassistant import config_entries
from homeassistant.helpers import config_entry_flow

from .const import DOMAIN


async def _async_has_devices(hass) -> bool:
    """Return if there are devices that can be discovered."""
    # TODO  add UDP code to discover Huawei sun2000 inverters
    devices = await hass.async_add_executor_job(my_pypi_dependency.discover)
    return len(devices) > 0


config_entry_flow.register_discovery_flow(
    DOMAIN, "Huawei sun2000 TKL", _async_has_devices, config_entries.CONN_CLASS_UNKNOWN
)
