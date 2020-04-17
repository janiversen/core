"""Common transport interface.

Contains the following communication types:
- tcp (direct socket communication)
- udp (direct datagram communication)
- serial (cabled RS-485 communication)

The set of classes handles all communication problems
like timeout and reconnect, so the calling layer only needs to handle
- "no connection possible", issued when reconnect gives up.
- "data unavailable", issued when no data is  received within the timeout.
"""
import asyncio
import logging

from homeassistant.core import callback

_LOGGER = logging.getLogger(__name__)


class baseTransport:
    """Common transport handling."""

    def __init__(self, loop, timeout, retry_count):
        """Initialize class."""
        self._loop = loop
        self._timeout = timeout
        self._retry_count = retry_count

    async def extern_connect(self):
        """Connect to device."""

    async def extern_close(self):
        """Close communication."""

    async def extern_read_data(self):
        """Read available data."""

    async def extern_write_data(self, data):
        """Write data."""


class transport_serial(baseTransport):
    """Serial connection handling."""

    def __init__(
        self, loop, timeout, retry_count, port, baudrate, stopbits, bytesize, parity,
    ):
        """Initialize class."""
        self._port = port
        self._baudrate = baudrate
        self._stopbits = stopbits
        self._bytesize = bytesize
        self._parity = parity
        baseTransport.__init__(loop, timeout, retry_count)


class transport_udp(baseTransport):
    """Datagram connection handling."""

    def __init__(
        self, loop, timeout, retry_count, host, port,
    ):
        """Initialize class."""
        self._host = host
        self._port = port
        super().__init__(loop, timeout, retry_count)


class transport_tcp(baseTransport):
    """Tcp connection handling."""

    def __init__(
        self, loop, timeout, retry_count, host, port,
    ):
        """Initialize class."""
        self._host = host
        self._port = port
        super().__init__(loop, timeout, retry_count)


class AbstractTransport:
    """Abstract async transport class.

    This is the only class to be used from the upper layers.
    """

    def __init__(self, loop, timeout, retry_count):
        """Initialize and set general variable.

        :param loop:        Active message loop
        :param timeout:     Milliseconds to wait before giving up
        :param retry_count: Number of reconnect retries
        :param unit:        The slave unit this request is targeting
        :returns:           Class as object
        :exceptions:        None
        """
        self._loop = loop
        self._timeout = timeout
        self._retry_count = retry_count

        # Create variables used later
        self._transport = None

    @callback
    def setup_serial(self, port, baudrate, stopbits, bytesize, parity):
        """Prepare serial device connection.

        :param port:     Device to be used e.g. /dev/tty1
        :param baudrate: Bits pr second as integer
        :param stopbits: 0-1-2 stopbits
        :param bytesize: 7-8 bits pr byte
        :param parity:   Even/Odd/None
        :returns:        None
        :exceptions:     None
        """
        self._transport = transport_serial(
            self._loop,
            self._timeout,
            self._retry_count,
            port,
            baudrate,
            stopbits,
            bytesize,
            parity,
        )

    @callback
    def setup_udp(self, host, port):
        """Prepare datagram (UDP) connection.

        :param host: ip address
        :param port: ip port, normally 5020 or 502
        :returns:    None
        :exceptions: None
        """
        self._transport = transport_udp(
            self._loop, self._timeout, self._retry_count, host, port,
        )

    @callback
    def setup_tcp(self, host, port):
        """Prepare TCP connection.

        :param host: ip address
        :param port: ip port, normally 5020 or 502
        :returns:    None
        :exceptions: None
        """
        self._transport = transport_tcp(
            self._loop, self._timeout, self._retry_count, host, port,
        )

    async def connect(self):
        """Connect to device.

        :param:      None
        :returns:    None
        :exceptions: timeout

        If the device do not respond within <timeout> * <retry_count>,
        exception timeout are raised, meaning platformUnavailable.

        When the device is succcesfully connected, reconnect in case
        of a communication break is automatic.
        """
        await self._transport.extern_connect()

    async def close(self):
        """Close communication and free objects.

        :param:      None
        :returns:    None
        :exceptions: None
        """
        await self._transport.extern_close()
        del self._transport
        self._transport = None

    async def read_data(self):
        """Read available data.

        :param:      None
        :returns:    array of bytes
        :exceptions: timeout, no_data

        Method wait until data are received or a <timeout> is reached.
        If the connection available and <timeout> is reached
        exception no_data is raised.
        If the connection is broken and <timeout> * <retry_count> is reached
        exception timeout is raised, meaning platformUnavailable.
        """
        await self._transport.extern_read_data()

    async def write_data(self, data):
        """Write data.

        :param data: Data to be written
        :returns:    None
        :exceptions: timeout, no_data

        Method writes data to the device.
        If the connection is broken and <timeout> * <retry_count> is reached
        exception timeout is raised, meaning platformUnavailable.
        """
        await self._transport.extern_write_data(data)


async def main():
    """Run main."""
    # Test
    loop = asyncio.get_event_loop()
    client1 = AbstractTransport(loop, 10, 5)
    client1.setup_tcp("127.0.0.1", 5020)
    await client1.connect()
    await client1.write_data("Jan igen")
    data = await client1.read_data()
    await client1.close()

    client2 = AbstractTransport(loop, 10, 5)
    client2.setup_udp("127.0.0.1", 5020)
    await client2.connect()
    await client2.write_data("Jan igen")
    data = await client2.read_data()
    await client2.close()

    client3 = AbstractTransport(loop, 10, 5)
    client3.setup_serial("/dev/tty3", 9600, 2, 8, "E")
    await client3.connect()
    await client3.write_data("Jan igen")
    data = await client3.read_data()
    print(data)
    await client3.close()
