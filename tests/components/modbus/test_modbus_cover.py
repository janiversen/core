"""The tests for the Modbus cover component."""
import pytest

from homeassistant.components.cover import DOMAIN as COVER_DOMAIN
from homeassistant.components.modbus.const import CALL_TYPE_COIL, CONF_REGISTER
from homeassistant.const import (
    CONF_COVERS,
    CONF_NAME,
    CONF_SCAN_INTERVAL,
    CONF_SLAVE,
    STATE_OPEN,
    STATE_OPENING,
)

from .conftest import base_config_test, base_test


@pytest.mark.parametrize(
    "do_options, read_type",
    [
        (False, CALL_TYPE_COIL),
        (True, CALL_TYPE_COIL),
        (False, CONF_REGISTER),
        (True, CONF_REGISTER),
    ],
)
async def test_config_cover(hass, ModbusHubMock, do_options, read_type):
    """Run test for cover."""
    deviceName = "test_cover"
    deviceConfig = {
        CONF_NAME: deviceName,
        read_type: 1234,
    }
    if do_options:
        deviceConfig.update(
            {
                CONF_SLAVE: 10,
                CONF_SCAN_INTERVAL: 20,
            }
        )
    await base_config_test(
        hass,
        deviceConfig,
        deviceName,
        COVER_DOMAIN,
        CONF_COVERS,
        None,
    )


@pytest.mark.parametrize(
    "regs,expected",
    [
        (
            [0x00],
            STATE_OPENING,
        ),
        (
            [0x80],
            STATE_OPENING,
        ),
        (
            [0xFE],
            STATE_OPENING,
        ),
        (
            [0xFF],
            STATE_OPENING,
        ),
        (
            [0x01],
            STATE_OPENING,
        ),
    ],
)
async def test_coil_cover(hass, ModbusHubMock, regs, expected):
    """Run test for given config."""
    cover_name = "modbus_test_cover"
    await base_test(
        hass,
        {
            CONF_NAME: cover_name,
            CALL_TYPE_COIL: 1234,
            CONF_SLAVE: 1,
        },
        cover_name,
        COVER_DOMAIN,
        CONF_COVERS,
        None,
        5,
        regs,
        expected,
    )


@pytest.mark.parametrize(
    "regs,expected",
    [
        (
            [0x00],
            STATE_OPEN,
        ),
        (
            [0x80],
            STATE_OPEN,
        ),
        (
            [0xFE],
            STATE_OPEN,
        ),
        (
            [0xFF],
            STATE_OPEN,
        ),
        (
            [0x01],
            STATE_OPEN,
        ),
    ],
)
async def test_register_COVER(hass, ModbusHubMock, regs, expected):
    """Run test for given config."""
    cover_name = "modbus_test_cover"
    await base_test(
        hass,
        {
            CONF_NAME: cover_name,
            CONF_REGISTER: 1234,
            CONF_SLAVE: 1,
        },
        cover_name,
        COVER_DOMAIN,
        CONF_COVERS,
        None,
        5,
        regs,
        expected,
    )
