"""The tests for the Modbus sensor component."""
import pytest

from homeassistant.components.binary_sensor import DOMAIN as SENSOR_DOMAIN
from homeassistant.components.modbus.const import (
    CALL_TYPE_COIL,
    CALL_TYPE_DISCRETE,
    CONF_ADDRESS,
    CONF_BINARY_SENSORS,
    CONF_INPUT_TYPE,
    CONF_INPUTS,
)
from homeassistant.const import CONF_NAME, CONF_SLAVE, STATE_OFF, STATE_ON

from .conftest import base_config_test, base_test


@pytest.mark.parametrize(
    "do_discovery, do_options",
    [
        (
            False,
            False,
        ),
        (
            False,
            True,
        ),
        (
            True,
            False,
        ),
        (
            True,
            True,
        ),
    ],
)
async def test_config_binary_sensor(hass, ModbusHubMock, do_discovery, do_options):
    """Run test for binary sensor."""
    sensorName = "test_sensor"
    configSensor = {
        CONF_NAME: sensorName,
        CONF_ADDRESS: 51,
    }
    if do_options:
        configSensor.update(
            {
                CONF_SLAVE: 10,
            }
        )
    await base_config_test(
        hass,
        configSensor,
        sensorName,
        SENSOR_DOMAIN,
        CONF_BINARY_SENSORS,
        CONF_INPUTS,
        method_discovery=do_discovery,
    )


@pytest.mark.parametrize(
    "cfg,regs,expected",
    [
        (
            {
                CONF_INPUT_TYPE: CALL_TYPE_COIL,
            },
            [0xFF],
            STATE_ON,
        ),
        (
            {
                CONF_INPUT_TYPE: CALL_TYPE_COIL,
            },
            [0x01],
            STATE_ON,
        ),
        (
            {
                CONF_INPUT_TYPE: CALL_TYPE_COIL,
            },
            [0x00],
            STATE_OFF,
        ),
        (
            {
                CONF_INPUT_TYPE: CALL_TYPE_COIL,
            },
            [0x80],
            STATE_OFF,
        ),
        (
            {
                CONF_INPUT_TYPE: CALL_TYPE_COIL,
            },
            [0xFE],
            STATE_OFF,
        ),
        (
            {
                CONF_INPUT_TYPE: CALL_TYPE_DISCRETE,
            },
            [0xFF],
            STATE_ON,
        ),
        (
            {
                CONF_INPUT_TYPE: CALL_TYPE_DISCRETE,
            },
            [0x00],
            STATE_OFF,
        ),
    ],
)
async def test_all_binary_sensor(hass, ModbusHubMock, cfg, regs, expected):
    """Run test for given config."""
    sensor_name = "modbus_test_binary_sensor"
    await base_test(
        hass,
        {CONF_NAME: sensor_name, CONF_ADDRESS: 1234, **cfg},
        sensor_name,
        SENSOR_DOMAIN,
        CONF_BINARY_SENSORS,
        CONF_INPUTS,
        5,
        regs,
        expected,
        method_discovery=False,
    )
