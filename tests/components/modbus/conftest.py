"""The tests for the Modbus sensor component."""
from datetime import timedelta
import logging
from unittest import mock

import pytest

from homeassistant.components.modbus.const import DEFAULT_HUB, MODBUS_DOMAIN as DOMAIN
from homeassistant.components.modbus.modbus import ModbusHub
from homeassistant.const import (
    CONF_HOST,
    CONF_NAME,
    CONF_PLATFORM,
    CONF_PORT,
    CONF_SCAN_INTERVAL,
    CONF_TYPE,
)
from homeassistant.helpers.discovery import async_load_platform
from homeassistant.setup import async_setup_component
import homeassistant.util.dt as dt_util

from tests.common import async_fire_time_changed

_LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope="class")
def ModbusHubMock():
    """Mock hub."""
    with mock.patch("homeassistant.components.modbus.modbus.ModbusHub"):
        yield


class ReadResult:
    """Storage class for register read results."""

    def __init__(self, register_words):
        """Init."""
        self.registers = register_words
        self.bits = register_words


async def base_config_test(
    hass,
    config_device,
    device_name,
    entity_domain,
    array_name_discovery,
    array_name_old_config,
    method_discovery=True,
    config_modbus=None,
    scan_interval=None,
):
    """Run test of config on platform/device for given config."""

    if config_modbus is None:
        config_modbus = {
            DOMAIN: {
                CONF_NAME: DEFAULT_HUB,
                CONF_TYPE: "tcp",
                CONF_HOST: "modbusTest",
                CONF_PORT: 5001,
            },
        }

    if method_discovery:
        if config_device is not None:
            config_modbus[DOMAIN].update({array_name_discovery: [{**config_device}]})
        await async_load_platform(
            hass, entity_domain, DOMAIN, config_modbus[DOMAIN], config_modbus
        )
    else:
        # setup modbus first
        assert await async_setup_component(hass, DOMAIN, config_modbus)

        # then setup component (this is old style configuration)
        if config_device is not None:
            config_device = {
                entity_domain: {
                    CONF_PLATFORM: DOMAIN,
                    array_name_old_config: [
                        {
                            **config_device,
                        }
                    ],
                }
            }
            if scan_interval is not None:
                config_device[entity_domain][CONF_SCAN_INTERVAL] = scan_interval
            await hass.async_block_till_done()
            assert await async_setup_component(hass, entity_domain, config_device)
    await hass.async_block_till_done()

    assert DOMAIN in hass.data
    if config_device is not None:
        entity_id = f"{entity_domain}.{device_name}"
        device = hass.states.get(entity_id)
        if device is None:
            pytest.fail("CONFIG failed, see output")


async def base_test(
    hass,
    config_device,
    device_name,
    entity_domain,
    array_name_discovery,
    array_name_old_config,
    scan_interval,
    register_words,
    expected,
    method_discovery=True,
):
    """Run test on device for given config."""

    # mock timer and add modbus platform with devices (new config)
    # first add modbus platform, then devices (old config)
    now = dt_util.utcnow()
    with mock.patch("homeassistant.helpers.event.dt_util.utcnow", return_value=now):
        # setup modbus and device platforms
        await base_config_test(
            hass,
            config_device,
            device_name,
            entity_domain,
            array_name_discovery,
            array_name_old_config,
            method_discovery,
            scan_interval=scan_interval,
        )

    # Setup inputs for the sensor
    read_result = ReadResult(register_words)
    hub: ModbusHub = hass.data[DOMAIN][DEFAULT_HUB]
    hub.read_coils.return_value = read_result
    hub.read_discrete_inputs.return_value = read_result
    hub.read_input_registers.return_value = read_result
    hub.read_holding_registers.return_value = read_result
    hub.name = "magicMock"

    # Trigger update call with time_changed event
    now = now + timedelta(seconds=scan_interval + 1)
    with mock.patch("homeassistant.helpers.event.dt_util.utcnow", return_value=now):
        async_fire_time_changed(hass, now)
        await hass.async_block_till_done()

    # Check state
    entity_id = f"{entity_domain}.{device_name}"
    state = hass.states.get(entity_id).state
    assert state == expected
