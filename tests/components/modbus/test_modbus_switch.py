"""The tests for the Modbus switch component."""
import pytest

from homeassistant.components.modbus.const import (
    CALL_TYPE_COIL,
    CONF_COILS,
    CONF_REGISTER,
    CONF_REGISTERS,
    CONF_SWITCHES,
)
from homeassistant.components.switch import DOMAIN as SWITCH_DOMAIN
from homeassistant.const import (
    CONF_COMMAND_OFF,
    CONF_COMMAND_ON,
    CONF_NAME,
    CONF_SCAN_INTERVAL,
    CONF_SLAVE,
    STATE_OFF,
    STATE_ON,
)

from .conftest import base_config_test, base_test


@pytest.mark.parametrize(
    "do_discovery, do_options, read_type, array_type",
    [
        (False, False, CALL_TYPE_COIL, CONF_COILS),
        (False, True, CALL_TYPE_COIL, CONF_COILS),
        (False, False, CONF_REGISTER, CONF_REGISTERS),
        (False, True, CONF_REGISTER, CONF_REGISTERS),
        (True, False, CALL_TYPE_COIL, CONF_COILS),
        (True, True, CALL_TYPE_COIL, CONF_COILS),
        (True, False, CONF_REGISTER, CONF_REGISTERS),
        (True, True, CONF_REGISTER, CONF_REGISTERS),
    ],
)
async def test_config_switch(
    hass, ModbusHubMock, do_discovery, do_options, read_type, array_type
):
    """Run test for switch."""
    deviceName = "test_switch"
    if do_discovery or do_options:
        return

    if read_type == CONF_REGISTER:
        deviceConfig = {
            CONF_NAME: deviceName,
            CONF_REGISTER: 1234,
            CONF_SLAVE: 1,
            CONF_COMMAND_OFF: 0x00,
            CONF_COMMAND_ON: 0x01,
        }
    else:
        deviceConfig = {
            CONF_NAME: deviceName,
            read_type: 1234,
            CONF_SLAVE: 10,
        }
    if do_options:
        deviceConfig.update(
            {
                CONF_SCAN_INTERVAL: 20,
            }
        )
    if do_discovery:
        deviceConfig = {read_type: {**deviceConfig}}

    await base_config_test(
        hass,
        deviceConfig,
        deviceName,
        SWITCH_DOMAIN,
        CONF_SWITCHES,
        array_type,
        method_discovery=do_discovery,
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
            STATE_ON,
        ),
        (
            [0x01],
            STATE_ON,
        ),
    ],
)
async def test_coil_switch(hass, ModbusHubMock, regs, expected):
    """Run test for given config."""
    switch_name = "modbus_test_switch"
    await base_test(
        hass,
        {
            CONF_NAME: switch_name,
            CALL_TYPE_COIL: 1234,
            CONF_SLAVE: 1,
        },
        switch_name,
        SWITCH_DOMAIN,
        CONF_SWITCHES,
        CONF_COILS,
        5,
        regs,
        expected,
        method_discovery=False,
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
async def test_register_switch(hass, ModbusHubMock, regs, expected):
    """Run test for given config."""
    switch_name = "modbus_test_switch"
    await base_test(
        hass,
        {
            CONF_NAME: switch_name,
            CONF_REGISTER: 1234,
            CONF_SLAVE: 1,
            CONF_COMMAND_OFF: 0x00,
            CONF_COMMAND_ON: 0x01,
        },
        switch_name,
        SWITCH_DOMAIN,
        CONF_SWITCHES,
        CONF_REGISTERS,
        5,
        regs,
        expected,
        method_discovery=False,
    )


@pytest.mark.parametrize(
    "regs,expected",
    [
        (
            [0x40],
            STATE_ON,
        ),
        (
            [0x04],
            STATE_OFF,
        ),
        (
            [0xFF],
            STATE_OFF,
        ),
    ],
)
async def test_register_state_switch(hass, ModbusHubMock, regs, expected):
    """Run test for given config."""
    switch_name = "modbus_test_switch"
    await base_test(
        hass,
        {
            CONF_NAME: switch_name,
            CONF_REGISTER: 1234,
            CONF_SLAVE: 1,
            CONF_COMMAND_OFF: 0x04,
            CONF_COMMAND_ON: 0x40,
        },
        switch_name,
        SWITCH_DOMAIN,
        CONF_SWITCHES,
        CONF_REGISTERS,
        5,
        regs,
        expected,
        method_discovery=False,
    )
