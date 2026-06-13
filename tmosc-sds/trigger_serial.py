"""Protocol-specific trigger SCPI commands (IIC, SPI, UART, CAN, LIN, FLEXray, CANFd, IIS)."""

from __future__ import annotations

from _base import _send, _query


def trigger_serial_type(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the serial bus trigger protocol type.

    SCPI: :TRIGger:TYPe <value>
           :TRIGger:TYPe?

        Configures the current serial bus trigger protocol type.
        IIC|SPI|UART|CAN|LIN|FLEXray|CANFd|IIS|M1553|SENT|MANChester

    Args:
        value: Serial protocol type

    Returns:
        Current serial type when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:TYPe?")
    _send(resource_name, f":TRIGger:TYPe {value}")
    return None


# ── I²C (IIC) Trigger ──────────────────────────────────────────────────────


def trigger_iic_condition(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the I²C trigger condition.

    SCPI: :TRIGger:IIC:CONDition <value>
           :TRIGger:IIC:CONDition?

        Configures the I²C bus trigger condition. Available values depend on the selected condition type (e.g. STARt|STOP|RESTart|NACK|EEPRom).

    Args:
        value: Trigger condition string

    Returns:
        Current condition when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:IIC:CONDition?")
    _send(resource_name, f":TRIGger:IIC:CONDition {value}")
    return None


def trigger_iic_address(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the I²C trigger address value.

    SCPI: :TRIGger:IIC:ADDRess <value>
           :TRIGger:IIC:ADDRess?

        Configures the I²C trigger address value. Maximum value + 1 selects the 'any value' wildcard.

    Args:
        value: Address value (NR1)

    Returns:
        Current address when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:IIC:ADDRess?")
    _send(resource_name, f":TRIGger:IIC:ADDRess {value}")
    return None


def trigger_iic_addr_length(resource_name: str, value: int | None = None) -> str | None:
    """Set or query the I²C trigger address length.

    SCPI: :TRIGger:IIC:ALENgth <value>
           :TRIGger:IIC:ALENgth?

        Configures the I²C trigger address length.
        {7BIT|10BIT}

    Args:
        value: Address length in bits (NR1)

    Returns:
        Current address length when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:IIC:ALENgth?")
    _send(resource_name, f":TRIGger:IIC:ALENgth {value}")
    return None


def trigger_iic_rw_bit(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the I²C trigger R/W bit.

    SCPI: :TRIGger:IIC:RWBit <value>
           :TRIGger:IIC:RWBit?

        Configures the read/write bit when the condition type is 7/10-bit address and data.

    Args:
        value: {WRITe|READ|ANY}

    Returns:
        Current R/W bit setting when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:IIC:RWBit?")
    _send(resource_name, f":TRIGger:IIC:RWBit {value}")
    return None


def trigger_iic_scl_source(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the I²C trigger SCL clock source.

    SCPI: :TRIGger:IIC:SCLSource <value>
           :TRIGger:IIC:SCLSource?

        Configures the I²C trigger SCL clock signal source.

    Args:
        value: {C<n>|D<d>}

    Returns:
        Current SCL source when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:IIC:SCLSource?")
    _send(resource_name, f":TRIGger:IIC:SCLSource {value}")
    return None


def trigger_iic_scl_threshold(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the I²C trigger SCL clock threshold.

    SCPI: :TRIGger:IIC:SCLThreshold <value>
           :TRIGger:IIC:SCLThreshold?

        Configures the I²C trigger SCL clock threshold.

    Args:
        value: Threshold level in volts (NR3)

    Returns:
        Current SCL threshold when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:IIC:SCLThreshold?")
    _send(resource_name, f":TRIGger:IIC:SCLThreshold {value}")
    return None


def trigger_iic_sda_source(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the I²C trigger SDA data source.

    SCPI: :TRIGger:IIC:SDASource <value>
           :TRIGger:IIC:SDASource?

        Configures the I²C trigger SDA data signal source.

    Args:
        value: {C<n>|D<d>}

    Returns:
        Current SDA source when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:IIC:SDASource?")
    _send(resource_name, f":TRIGger:IIC:SDASource {value}")
    return None


def trigger_iic_sda_threshold(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the I²C trigger SDA data threshold.

    SCPI: :TRIGger:IIC:SDAThreshold <value>
           :TRIGger:IIC:SDAThreshold?

        Configures the I²C trigger SDA data threshold.

    Args:
        value: Threshold level in volts (NR3)

    Returns:
        Current SDA threshold when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:IIC:SDAThreshold?")
    _send(resource_name, f":TRIGger:IIC:SDAThreshold {value}")
    return None


def trigger_iic_value(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the I²C trigger data value.

    SCPI: :TRIGger:IIC:VALue <value>
           :TRIGger:IIC:VALue?

        Configures the I²C trigger data value.

    Args:
        value: Data value (NR1)

    Returns:
        Current data value when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:IIC:VALue?")
    _send(resource_name, f":TRIGger:IIC:VALue {value}")
    return None


# ── SPI Trigger ─────────────────────────────────────────────────────────────


def trigger_spi_bit_order(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the SPI trigger bit order.

    SCPI: :TRIGger:SPI:BITorder <value>
           :TRIGger:SPI:BITorder?

        Configures the SPI trigger bit order.

    Args:
        value: {LSM|MSB} (LSM = LSB first, MSB = MSB first)

    Returns:
        Current bit order when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:SPI:BITorder?")
    _send(resource_name, f":TRIGger:SPI:BITorder {value}")
    return None


def trigger_spi_clk_source(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the SPI trigger CLK clock source.

    SCPI: :TRIGger:SPI:CLKSource <value>
           :TRIGger:SPI:CLKSource?

        Configures the SPI trigger CLK clock signal source.

    Args:
        value: {C<n>|D<d>}

    Returns:
        Current CLK source when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:SPI:CLKSource?")
    _send(resource_name, f":TRIGger:SPI:CLKSource {value}")
    return None


def trigger_spi_clk_threshold(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the SPI trigger CLK clock threshold.

    SCPI: :TRIGger:SPI:CLKThreshold <value>
           :TRIGger:SPI:CLKThreshold?

        Configures the SPI trigger CLK clock threshold.

    Args:
        value: Threshold level in volts (NR3)

    Returns:
        Current CLK threshold when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:SPI:CLKThreshold?")
    _send(resource_name, f":TRIGger:SPI:CLKThreshold {value}")
    return None


def trigger_spi_cs_source(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the SPI trigger CS chip-select source.

    SCPI: :TRIGger:SPI:CSSource <value>
           :TRIGger:SPI:CSSource?

        Configures the SPI trigger CS chip-select signal source.

    Args:
        value: {C<n>|D<d>}

    Returns:
        Current CS source when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:SPI:CSSource?")
    _send(resource_name, f":TRIGger:SPI:CSSource {value}")
    return None


def trigger_spi_cs_threshold(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the SPI trigger CS chip-select threshold.

    SCPI: :TRIGger:SPI:CSThreshold <value>
           :TRIGger:SPI:CSThreshold?

        Configures the SPI trigger CS chip-select threshold.

    Args:
        value: Threshold level in volts (NR3)

    Returns:
        Current CS threshold when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:SPI:CSThreshold?")
    _send(resource_name, f":TRIGger:SPI:CSThreshold {value}")
    return None


def trigger_spi_cs_type(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the SPI trigger CS chip-select type.

    SCPI: :TRIGger:SPI:CSTYpe <value>
           :TRIGger:SPI:CSTYpe?

        Configures the SPI trigger chip-select type.

    Args:
        value: {NCS|CS|TIMeout[,<time>]}
            NCS     — active low chip-select
            CS      — active high chip-select
            TIMeout — clock timeout (range [1E-7, 5E-3])

    Returns:
        Current CS type when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:SPI:CSTYpe?")
    _send(resource_name, f":TRIGger:SPI:CSTYpe {value}")
    return None


def trigger_spi_latch_edge(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the SPI trigger clock sampling edge.

    SCPI: :TRIGger:SPI:LATChedge <value>
           :TRIGger:SPI:LATChedge?

        Configures the SPI trigger clock sampling edge.

    Args:
        value: {RISing|FALLing}

    Returns:
        Current latch edge when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:SPI:LATChedge?")
    _send(resource_name, f":TRIGger:SPI:LATChedge {value}")
    return None


def trigger_spi_miso_source(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the SPI trigger MISO source.

    SCPI: :TRIGger:SPI:MISOSource <value>
           :TRIGger:SPI:MISOSource?

        Configures the SPI trigger MISO signal source.

    Args:
        value: {C<n>|D<d>}

    Returns:
        Current MISO source when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:SPI:MISOSource?")
    _send(resource_name, f":TRIGger:SPI:MISOSource {value}")
    return None


def trigger_spi_miso_threshold(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the SPI trigger MISO threshold.

    SCPI: :TRIGger:SPI:MISOThreshold <value>
           :TRIGger:SPI:MISOThreshold?

        Configures the SPI trigger MISO threshold.

    Args:
        value: Threshold level in volts (NR3)

    Returns:
        Current MISO threshold when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:SPI:MISOThreshold?")
    _send(resource_name, f":TRIGger:SPI:MISOThreshold {value}")
    return None


def trigger_spi_mosi_source(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the SPI trigger MOSI source.

    SCPI: :TRIGger:SPI:MOSISource <value>
           :TRIGger:SPI:MOSISource?

        Configures the SPI trigger MOSI signal source.

    Args:
        value: {C<n>|D<d>}

    Returns:
        Current MOSI source when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:SPI:MOSISource?")
    _send(resource_name, f":TRIGger:SPI:MOSISource {value}")
    return None


def trigger_spi_mosi_threshold(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the SPI trigger MOSI threshold.

    SCPI: :TRIGger:SPI:MOSIThreshold <value>
           :TRIGger:SPI:MOSIThreshold?

        Configures the SPI trigger MOSI threshold.

    Args:
        value: Threshold level in volts (NR3)

    Returns:
        Current MOSI threshold when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:SPI:MOSIThreshold?")
    _send(resource_name, f":TRIGger:SPI:MOSIThreshold {value}")
    return None


def trigger_spi_ncs_source(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the SPI trigger NCS negative chip-select source.

    SCPI: :TRIGger:SPI:NCSSource <value>
           :TRIGger:SPI:NCSSource?

        Configures the SPI trigger NCS negative chip-select signal source.

    Args:
        value: {C<n>|D<d>}

    Returns:
        Current NCS source when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:SPI:NCSSource?")
    _send(resource_name, f":TRIGger:SPI:NCSSource {value}")
    return None


def trigger_spi_ncs_threshold(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the SPI trigger NCS threshold.

    SCPI: :TRIGger:SPI:NCSThreshold <value>
           :TRIGger:SPI:NCSThreshold?

        Configures the SPI trigger NCS threshold.

    Args:
        value: Threshold level in volts (NR3)

    Returns:
        Current NCS threshold when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:SPI:NCSThreshold?")
    _send(resource_name, f":TRIGger:SPI:NCSThreshold {value}")
    return None


# ── UART Trigger ────────────────────────────────────────────────────────────


def trigger_uart_baud(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the UART trigger baud rate.

    SCPI: :TRIGger:UART:BAUD <value>
           :TRIGger:UART:BAUD?

        Configures the UART trigger baud rate. Standard values include 600-115200 bps, or CUSTom for custom rates.

    Args:
        value: Baud rate string or CUSTom,<value>

    Returns:
        Current baud rate when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:UART:BAUD?")
    _send(resource_name, f":TRIGger:UART:BAUD {value}")
    return None


def trigger_uart_data_length(resource_name: str, value: int | None = None) -> str | None:
    """Set or query the UART trigger data length.

    SCPI: :TRIGger:UART:DLENgth <value>
           :TRIGger:UART:DLENgth?

        Configures the UART trigger data length (in bits).

    Args:
        value: Data length in bits (NR1)

    Returns:
        Current data length when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:UART:DLENgth?")
    _send(resource_name, f":TRIGger:UART:DLENgth {value}")
    return None


def trigger_uart_parity(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the UART trigger parity.

    SCPI: :TRIGger:UART:PARity <value>
           :TRIGger:UART:PARity?

        Configures the UART trigger parity mode.

    Args:
        value: {NONE|ODD|EVEN|MARK|SPACe}

    Returns:
        Current parity setting when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:UART:PARity?")
    _send(resource_name, f":TRIGger:UART:PARity {value}")
    return None


def trigger_uart_stop(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the UART trigger stop bit count.

    SCPI: :TRIGger:UART:STOP <value>
           :TRIGger:UART:STOP?

        Configures the UART trigger stop bit count.

    Args:
        value: {1|1.5|2}

    Returns:
        Current stop bit count when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:UART:STOP?")
    _send(resource_name, f":TRIGger:UART:STOP {value}")
    return None


def trigger_uart_idle(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the UART trigger idle level.

    SCPI: :TRIGger:UART:IDLE <value>
           :TRIGger:UART:IDLE?

        Configures the UART trigger idle signal level.

    Args:
        value: {LOW|HIGH}

    Returns:
        Current idle level when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:UART:IDLE?")
    _send(resource_name, f":TRIGger:UART:IDLE {value}")
    return None


def trigger_uart_tx_source(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the UART trigger TX source.

    SCPI: :TRIGger:UART:TXSource <value>
           :TRIGger:UART:TXSource?

        Configures the UART trigger TX (transmit) signal source.

    Args:
        value: {C<n>|D<d>}

    Returns:
        Current TX source when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:UART:TXSource?")
    _send(resource_name, f":TRIGger:UART:TXSource {value}")
    return None


def trigger_uart_tx_threshold(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the UART trigger TX threshold.

    SCPI: :TRIGger:UART:TXTHreshold <value>
           :TRIGger:UART:TXTHreshold?

        Configures the UART trigger TX threshold.

    Args:
        value: Threshold level in volts (NR3)

    Returns:
        Current TX threshold when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:UART:TXTHreshold?")
    _send(resource_name, f":TRIGger:UART:TXTHreshold {value}")
    return None


def trigger_uart_rx_source(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the UART trigger RX source.

    SCPI: :TRIGger:UART:RXSource <value>
           :TRIGger:UART:RXSource?

        Configures the UART trigger RX (receive) signal source.

    Args:
        value: {C<n>|D<d>}

    Returns:
        Current RX source when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:UART:RXSource?")
    _send(resource_name, f":TRIGger:UART:RXSource {value}")
    return None


def trigger_uart_rx_threshold(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the UART trigger RX threshold.

    SCPI: :TRIGger:UART:RXTHreshold <value>
           :TRIGger:UART:RXTHreshold?

        Configures the UART trigger RX threshold.

    Args:
        value: Threshold level in volts (NR3)

    Returns:
        Current RX threshold when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:UART:RXTHreshold?")
    _send(resource_name, f":TRIGger:UART:RXTHreshold {value}")
    return None


def trigger_uart_data(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the UART trigger data byte 1.

    SCPI: :TRIGger:UART:DATA <value>
           :TRIGger:UART:DATA?

        Configures the UART trigger data byte 1. Maximum value + 1 selects the 'any value' wildcard (0xXX).

    Args:
        value: Data byte value (NR1, range depends on protocol)

    Returns:
        Current data value when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:UART:DATA?")
    _send(resource_name, f":TRIGger:UART:DATA {value}")
    return None


def trigger_uart_data2(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the UART trigger data byte 2.

    SCPI: :TRIGger:UART:DAT2 <value>
           :TRIGger:UART:DAT2?

        Configures the UART trigger data byte 2. Maximum value + 1 selects the 'any value' wildcard (0xXX).

    Args:
        value: Data byte value (NR1)

    Returns:
        Current data2 value when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:UART:DAT2?")
    _send(resource_name, f":TRIGger:UART:DAT2 {value}")
    return None


def trigger_uart_condition(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the UART trigger condition.

    SCPI: :TRIGger:UART:CONDition <value>
           :TRIGger:UART:CONDition?

        Configures the UART trigger condition.

    Args:
        value: Trigger condition string

    Returns:
        Current condition when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:UART:CONDition?")
    _send(resource_name, f":TRIGger:UART:CONDition {value}")
    return None


def trigger_uart_compare(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the UART trigger data comparison type.

    SCPI: :TRIGger:UART:COMPare <value>
           :TRIGger:UART:COMPare?

        Configures the UART trigger data comparison type.

    Args:
        value: {EQUal|GREaterthan|LESSthan}

    Returns:
        Current compare type when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:UART:COMPare?")
    _send(resource_name, f":TRIGger:UART:COMPare {value}")
    return None


# ── CAN Trigger ─────────────────────────────────────────────────────────────


def trigger_can_baud(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the CAN trigger baud rate.

    SCPI: :TRIGger:CAN:BAUD <value>
           :TRIGger:CAN:BAUD?

        Configures the CAN trigger baud rate. Standard values include 5k-1M bps, or CUSTom for custom rates.

    Args:
        value: Baud rate string or CUSTom,<value>

    Returns:
        Current baud rate when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:CAN:BAUD?")
    _send(resource_name, f":TRIGger:CAN:BAUD {value}")
    return None


def trigger_can_id(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the CAN trigger frame/message ID.

    SCPI: :TRIGger:CAN:ID <value>
           :TRIGger:CAN:ID?

        Configures the CAN trigger frame/message ID.

    Args:
        value: ID value (NR1, range depends on protocol)

    Returns:
        Current ID when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:CAN:ID?")
    _send(resource_name, f":TRIGger:CAN:ID {value}")
    return None


def trigger_can_id_length(resource_name: str, value: int | None = None) -> str | None:
    """Set or query the CAN trigger ID length.

    SCPI: :TRIGger:CAN:IDLENgth <value>
           :TRIGger:CAN:IDLENgth?

        Configures the CAN trigger ID length.
        {11BITS|29BITS}

    Args:
        value: ID length in bits (NR1)

    Returns:
        Current ID length when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:CAN:IDLENgth?")
    _send(resource_name, f":TRIGger:CAN:IDLENgth {value}")
    return None


def trigger_can_data(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the CAN trigger data byte.

    SCPI: :TRIGger:CAN:DATA <value>
           :TRIGger:CAN:DATA?

        Configures the CAN trigger data value.

    Args:
        value: Data byte value (NR1)

    Returns:
        Current data value when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:CAN:DATA?")
    _send(resource_name, f":TRIGger:CAN:DATA {value}")
    return None


def trigger_can_condition(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the CAN trigger condition.

    SCPI: :TRIGger:CAN:CONDition <value>
           :TRIGger:CAN:CONDition?

        Configures the CAN trigger condition.

    Args:
        value: Trigger condition string

    Returns:
        Current condition when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:CAN:CONDition?")
    _send(resource_name, f":TRIGger:CAN:CONDition {value}")
    return None


def trigger_can_address(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the CAN trigger address value.

    SCPI: :TRIGger:CAN:ADDRess <value>
           :TRIGger:CAN:ADDRess?

        Configures the CAN trigger address value (e.g. CAN ID). Maximum value + 1 selects the 'any value' wildcard.

    Args:
        value: Address value (NR1)

    Returns:
        Current address when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:CAN:ADDRess?")
    _send(resource_name, f":TRIGger:CAN:ADDRess {value}")
    return None


# ── LIN Trigger ─────────────────────────────────────────────────────────────


def trigger_lin_standard(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the LIN trigger protocol standard/revision.

    SCPI: :TRIGger:LIN:STANdard <value>
           :TRIGger:LIN:STANdard?

        Configures the LIN trigger protocol standard/revision.
        {0|1} (0 = Rev 1.3, 1 = Rev 2.x)

    Args:
        value: Standard/revision string

    Returns:
        Current standard when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:LIN:STANdard?")
    _send(resource_name, f":TRIGger:LIN:STANdard {value}")
    return None


def trigger_lin_baud(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the LIN trigger baud rate.

    SCPI: :TRIGger:LIN:BAUD <value>
           :TRIGger:LIN:BAUD?

        Configures the LIN trigger baud rate.

    Args:
        value: Baud rate string or CUSTom,<value>

    Returns:
        Current baud rate when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:LIN:BAUD?")
    _send(resource_name, f":TRIGger:LIN:BAUD {value}")
    return None


def trigger_lin_compare(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the LIN trigger data comparison type.

    SCPI: :TRIGger:LIN:COMPare <value>
           :TRIGger:LIN:COMPare?

        Configures the LIN trigger data comparison type.

    Args:
        value: {EQUal|GREaterthan|LESSthan}

    Returns:
        Current compare type when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:LIN:COMPare?")
    _send(resource_name, f":TRIGger:LIN:COMPare {value}")
    return None


def trigger_lin_data(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the LIN trigger data byte.

    SCPI: :TRIGger:LIN:DATA <value>
           :TRIGger:LIN:DATA?

        Configures the LIN trigger data value.

    Args:
        value: Data byte value (NR1)

    Returns:
        Current data value when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:LIN:DATA?")
    _send(resource_name, f":TRIGger:LIN:DATA {value}")
    return None


def trigger_lin_condition(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the LIN trigger condition.

    SCPI: :TRIGger:LIN:CONDition <value>
           :TRIGger:LIN:CONDition?

        Configures the LIN trigger condition.

    Args:
        value: Trigger condition string

    Returns:
        Current condition when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:LIN:CONDition?")
    _send(resource_name, f":TRIGger:LIN:CONDition {value}")
    return None


# ── FLEXray Trigger ─────────────────────────────────────────────────────────


def trigger_flexray_frame_compare(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the FLEXray trigger frame compare type.

    SCPI: :TRIGger:FLEXray:FRAMe:COMPare <value>
           :TRIGger:FLEXray:FRAMe:COMPare?

        Configures the FlexRay trigger frame comparison type.

    Args:
        value: {ANY|EQUal|GREaterthan|LESSthan}

    Returns:
        Current frame compare type when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:FLEXray:FRAMe:COMPare?")
    _send(resource_name, f":TRIGger:FLEXray:FRAMe:COMPare {value}")
    return None


def trigger_flexray_frame_cycle(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the FLEXray trigger frame cycle count.

    SCPI: :TRIGger:FLEXray:FRAMe:CYCLe <value>
           :TRIGger:FLEXray:FRAMe:CYCLe?

        Configures the FlexRay trigger frame cycle count.

    Args:
        value: Cycle count (NR1, range [0,63])

    Returns:
        Current frame cycle when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:FLEXray:FRAMe:CYCLe?")
    _send(resource_name, f":TRIGger:FLEXray:FRAMe:CYCLe {value}")
    return None


def trigger_flexray_frame_id(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the FLEXray trigger frame ID.

    SCPI: :TRIGger:FLEXray:FRAMe:ID <value>
           :TRIGger:FLEXray:FRAMe:ID?

        Configures the FlexRay trigger frame ID.

    Args:
        value: Frame ID (NR1, range [0,2048], 2048 = any value)

    Returns:
        Current frame ID when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:FLEXray:FRAMe:ID?")
    _send(resource_name, f":TRIGger:FLEXray:FRAMe:ID {value}")
    return None


def trigger_flexray_frame_repetition(resource_name: str, value: int | None = None) -> str | None:
    """Set or query the FLEXray trigger frame repetition factor.

    SCPI: :TRIGger:FLEXray:FRAMe:REPetition <value>
           :TRIGger:FLEXray:FRAMe:REPetition?

        Configures the FlexRay trigger frame repetition factor.

    Args:
        value: Repetition factor {1|2|4|8|16|32|64}

    Returns:
        Current repetition factor when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:FLEXray:FRAMe:REPetition?")
    _send(resource_name, f":TRIGger:FLEXray:FRAMe:REPetition {value}")
    return None


# ── CAN FD Trigger ──────────────────────────────────────────────────────────


def trigger_canfd_frame_type(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the CAN FD trigger frame type.

    SCPI: :TRIGger:CANFd:FTYPe <value>
           :TRIGger:CANFd:FTYPe?

        Configures the CAN FD trigger frame type.
        e.g. {BOTH|CAN|CANFd}

    Args:
        value: Frame type string

    Returns:
        Current frame type when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:CANFd:FTYPe?")
    _send(resource_name, f":TRIGger:CANFd:FTYPe {value}")
    return None


def trigger_canfd_baud_data(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the CAN FD trigger data baud rate.

    SCPI: :TRIGger:CANFd:BAUDData <value>
           :TRIGger:CANFd:BAUDData?

        Configures the CAN FD trigger data baud rate.

    Args:
        value: {500kbps|1Mbps|2Mbps|5Mbps|8Mbps|10Mbps|CUSTom}

    Returns:
        Current data baud rate when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:CANFd:BAUDData?")
    _send(resource_name, f":TRIGger:CANFd:BAUDData {value}")
    return None


def trigger_canfd_baud_nominal(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the CAN FD trigger nominal baud rate.

    SCPI: :TRIGger:CANFd:BAUDNominal <value>
           :TRIGger:CANFd:BAUDNominal?

        Configures the CAN FD trigger nominal baud rate.

    Args:
        value: {10kbps|25kbps|50kbps|100kbps|250kbps|1Mbps|CUSTom}

    Returns:
        Current nominal baud rate when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:CANFd:BAUDNominal?")
    _send(resource_name, f":TRIGger:CANFd:BAUDNominal {value}")
    return None


# ── I²S (IIS) Trigger ──────────────────────────────────────────────────────


def trigger_iis_audio_variant(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the I²S trigger audio variant format.

    SCPI: :TRIGger:IIS:AVARiant <value>
           :TRIGger:IIS:AVARiant?

        Configures the I²S trigger audio variant format.

    Args:
        value: {I2S|LJ|RJ} (I2S = standard I2S, LJ = left-justified, RJ = right-justified)

    Returns:
        Current audio variant when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:IIS:AVARiant?")
    _send(resource_name, f":TRIGger:IIS:AVARiant {value}")
    return None


def trigger_iis_bclk_source(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the I²S trigger BCLK bit-clock source.

    SCPI: :TRIGger:IIS:BCLKSource <value>
           :TRIGger:IIS:BCLKSource?

        Configures the I²S trigger BCLK bit-clock signal source.

    Args:
        value: {C<n>|D<d>}

    Returns:
        Current BCLK source when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:IIS:BCLKSource?")
    _send(resource_name, f":TRIGger:IIS:BCLKSource {value}")
    return None


def trigger_iis_bclk_threshold(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the I²S trigger BCLK bit-clock threshold.

    SCPI: :TRIGger:IIS:BCLKThreshold <value>
           :TRIGger:IIS:BCLKThreshold?

        Configures the I²S trigger BCLK bit-clock threshold.

    Args:
        value: Threshold level in volts (NR3)

    Returns:
        Current BCLK threshold when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:IIS:BCLKThreshold?")
    _send(resource_name, f":TRIGger:IIS:BCLKThreshold {value}")
    return None


def trigger_iis_d_source(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the I²S trigger data source.

    SCPI: :TRIGger:IIS:DSource <value>
           :TRIGger:IIS:DSource?

        Configures the I²S trigger data signal source.

    Args:
        value: {C<n>|D<d>}

    Returns:
        Current data source when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:IIS:DSource?")
    _send(resource_name, f":TRIGger:IIS:DSource {value}")
    return None


def trigger_iis_d_threshold(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the I²S trigger data threshold.

    SCPI: :TRIGger:IIS:DTHReshold <value>
           :TRIGger:IIS:DTHReshold?

        Configures the I²S trigger data threshold.

    Args:
        value: Threshold level in volts (NR3)

    Returns:
        Current data threshold when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:IIS:DTHReshold?")
    _send(resource_name, f":TRIGger:IIS:DTHReshold {value}")
    return None


def trigger_iis_ws_source(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the I²S trigger WS word-select source.

    SCPI: :TRIGger:IIS:WSSource <value>
           :TRIGger:IIS:WSSource?

        Configures the I²S trigger WS word-select signal source.

    Args:
        value: {C<n>|D<d>}

    Returns:
        Current WS source when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:IIS:WSSource?")
    _send(resource_name, f":TRIGger:IIS:WSSource {value}")
    return None


def trigger_iis_ws_threshold(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the I²S trigger WS word-select threshold.

    SCPI: :TRIGger:IIS:WSTHreshold <value>
           :TRIGger:IIS:WSTHreshold?

        Configures the I²S trigger WS word-select threshold.

    Args:
        value: Threshold level in volts (NR3)

    Returns:
        Current WS threshold when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:IIS:WSTHreshold?")
    _send(resource_name, f":TRIGger:IIS:WSTHreshold {value}")
    return None


def trigger_iis_lch(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the I²S trigger left channel polarity.

    SCPI: :TRIGger:IIS:LCH <value>
           :TRIGger:IIS:LCH?

        Configures the I²S trigger left channel polarity.

    Args:
        value: {LOW|HIGH}
            LOW  — WS low selects left channel
            HIGH — WS low selects right channel

    Returns:
        Current LCH polarity when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:IIS:LCH?")
    _send(resource_name, f":TRIGger:IIS:LCH {value}")
    return None


def trigger_iis_sbit(resource_name: str, value: int | None = None) -> str | None:
    """Set or query the I²S trigger data start bit offset.

    SCPI: :TRIGger:IIS:SBIT <value>
           :TRIGger:IIS:SBIT?

        Configures the I²S trigger data start bit offset. Range depends on channel bit width and start bit configuration.

    Args:
        value: Start bit offset (NR1)

    Returns:
        Current SBIT value when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:IIS:SBIT?")
    _send(resource_name, f":TRIGger:IIS:SBIT {value}")
    return None


def trigger_iis_bit_order(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the I²S trigger bit order.

    SCPI: :TRIGger:IIS:BITorder <value>
           :TRIGger:IIS:BITorder?

        Configures the I²S trigger bit order.

    Args:
        value: {LSM|MSB} (LSM = LSB first, MSB = MSB first)

    Returns:
        Current bit order when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:IIS:BITorder?")
    _send(resource_name, f":TRIGger:IIS:BITorder {value}")
    return None


def trigger_iis_data_length(resource_name: str, value: int | None = None) -> str | None:
    """Set or query the I²S trigger data length.

    SCPI: :TRIGger:IIS:DLENgth <value>
           :TRIGger:IIS:DLENgth?

        Configures the I²S trigger data length (in bits).

    Args:
        value: Data length in bits (NR1)

    Returns:
        Current data length when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:IIS:DLENgth?")
    _send(resource_name, f":TRIGger:IIS:DLENgth {value}")
    return None


def trigger_iis_data(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the I²S trigger data value.

    SCPI: :TRIGger:IIS:DATA <value>
           :TRIGger:IIS:DATA?

        Configures the I²S trigger data value.

    Args:
        value: Data byte value (NR1)

    Returns:
        Current data value when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:IIS:DATA?")
    _send(resource_name, f":TRIGger:IIS:DATA {value}")
    return None


def trigger_iis_value(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the I²S trigger data value.

    SCPI: :TRIGger:IIS:VALue <value>
           :TRIGger:IIS:VALue?

        Configures the I²S trigger data value.

    Args:
        value: Data value (NR1)

    Returns:
        Current data value when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:IIS:VALue?")
    _send(resource_name, f":TRIGger:IIS:VALue {value}")
    return None


def trigger_iis_condition(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the I²S trigger condition.

    SCPI: :TRIGger:IIS:CONDition <value>
           :TRIGger:IIS:CONDition?

        Configures the I²S trigger condition.

    Args:
        value: Trigger condition string

    Returns:
        Current condition when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:IIS:CONDition?")
    _send(resource_name, f":TRIGger:IIS:CONDition {value}")
    return None


def trigger_iis_compare(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the I²S trigger data comparison type.

    SCPI: :TRIGger:IIS:COMPare <value>
           :TRIGger:IIS:COMPare?

        Configures the I²S trigger data comparison type.

    Args:
        value: {EQUal|GREaterthan|LESSthan}

    Returns:
        Current compare type when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:IIS:COMPare?")
    _send(resource_name, f":TRIGger:IIS:COMPare {value}")
    return None


def trigger_iis_latch_edge(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the I²S trigger clock sampling edge.

    SCPI: :TRIGger:IIS:LATChedge <value>
           :TRIGger:IIS:LATChedge?

        Configures the I²S trigger clock sampling edge.

    Args:
        value: {RISing|FALLing}

    Returns:
        Current latch edge when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:IIS:LATChedge?")
    _send(resource_name, f":TRIGger:IIS:LATChedge {value}")
    return None
