"""The tests for the Modbus light component."""
import pytest

from homeassistant.components.light import DOMAIN as LIGHT_DOMAIN
from homeassistant.components.modbus.const import CALL_TYPE_COIL, CONF_REGISTER
from homeassistant.const import (
    CONF_COMMAND_OFF,
    CONF_COMMAND_ON,
    CONF_LIGHTS,
    CONF_NAME,
    CONF_SLAVE,
    STATE_OFF,
    STATE_ON,
)

from .conftest import base_test


@pytest.mark.parametrize(
    "regs,expected",
    [
        (
            [0x00],
            STATE_OFF,
        ),
        (
            [0x80],
            STATE_OFF,
        ),
        (
            [0xFE],
            STATE_OFF,
        ),
        (
            [0xFF],
            STATE_ON,
        ),
        (
            [0x01],
            STATE_ON,
        ),
    ],
)
async def test_coil_light(hass, ModbusHubMock, regs, expected):
    """Run test for given config."""
    light_name = "modbus_test_light"
    await base_test(
        light_name,
        hass,
        {
            CONF_LIGHTS: [
                {
                    CONF_NAME: light_name,
                    CALL_TYPE_COIL: 1234,
                    CONF_SLAVE: 1,
                },
            ]
        },
        LIGHT_DOMAIN,
        5,
        regs,
        expected,
        method_discovery=True,
    )


@pytest.mark.parametrize(
    "regs,expected",
    [
        (
            [0x00],
            STATE_OFF,
        ),
        (
            [0x80],
            STATE_OFF,
        ),
        (
            [0xFE],
            STATE_OFF,
        ),
        (
            [0xFF],
            STATE_OFF,
        ),
        (
            [0x01],
            STATE_ON,
        ),
    ],
)
async def test_register_light(hass, ModbusHubMock, regs, expected):
    """Run test for given config."""
    light_name = "modbus_test_light"
    await base_test(
        light_name,
        hass,
        {
            CONF_LIGHTS: [
                {
                    CONF_NAME: light_name,
                    CONF_REGISTER: 1234,
                    CONF_SLAVE: 1,
                    CONF_COMMAND_OFF: 0x00,
                    CONF_COMMAND_ON: 0x01,
                },
            ]
        },
        LIGHT_DOMAIN,
        5,
        regs,
        expected,
        method_discovery=True,
    )
