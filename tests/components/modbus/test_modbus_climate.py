"""The tests for the Modbus climate component."""
import pytest

from homeassistant.components.climate import DOMAIN as CLIMATE_DOMAIN
from homeassistant.components.modbus.const import (
    CONF_CLIMATES,
    CONF_CURRENT_TEMP,
    CONF_DATA_COUNT,
    CONF_TARGET_TEMP,
)
from homeassistant.const import CONF_NAME, CONF_SCAN_INTERVAL, CONF_SLAVE

from .conftest import base_config_test, base_test


@pytest.mark.parametrize(
    "do_options",
    [
        False,
        True,
    ],
)
async def test_config_climate(hass, ModbusHubMock, do_options):
    """Run test for climate."""
    deviceName = "test_climate"
    deviceConfig = {
        CONF_NAME: deviceName,
        CONF_TARGET_TEMP: 117,
        CONF_CURRENT_TEMP: 117,
    }
    if do_options:
        deviceConfig.update(
            {
                CONF_SLAVE: 10,
                CONF_SCAN_INTERVAL: 20,
                CONF_DATA_COUNT: 2,
            }
        )
    await base_config_test(
        hass,
        deviceConfig,
        deviceName,
        CLIMATE_DOMAIN,
        CONF_CLIMATES,
        None,
    )


@pytest.mark.parametrize(
    "regs,expected",
    [
        (
            [0x00],
            "auto",
        ),
    ],
)
async def test_temperature_climate(hass, ModbusHubMock, regs, expected):
    """Run test for given config."""
    climate_name = "modbus_test_climate"
    await base_test(
        hass,
        {
            CONF_NAME: climate_name,
            CONF_SLAVE: 1,
            CONF_TARGET_TEMP: 117,
            CONF_CURRENT_TEMP: 117,
            CONF_DATA_COUNT: 2,
        },
        climate_name,
        CLIMATE_DOMAIN,
        CONF_CLIMATES,
        None,
        5,
        regs,
        expected,
    )
