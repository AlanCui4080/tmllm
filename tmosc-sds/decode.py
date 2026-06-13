"""DECode subsystem SCPI commands (serial bus decode)."""
from __future__ import annotations
from _base import _send, _query


def decode_state(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query the global decode on/off state.

    SCPI: :DECode {ON|OFF}   :DECode?

        Configures the global decode on/off state.

    Args:
        state: True=ON, False=OFF
    """
    if state is None:
        return _query(resource_name, ":DECode?")
    _send(resource_name, f":DECode {'ON' if state else 'OFF'}")
    return None


def decode_list_state(resource_name: str, state: str | None = None) -> str | None:
    """Set or query which decode bus list is displayed.

    SCPI: :DECode:LIST {OFF|D1|D2}

    Args:
        state: {OFF|D1|D2}
    """
    if state is None:
        return _query(resource_name, ":DECode:LIST?")
    _send(resource_name, f":DECode:LIST {state}")
    return None


def decode_list_line(resource_name: str, lines: int | None = None) -> str | None:
    """Set or query decode list display line count (1-7)."""
    if lines is None:
        return _query(resource_name, ":DECode:LIST:LINE?")
    _send(resource_name, f":DECode:LIST:LINE {lines}")
    return None


def decode_list_scroll(resource_name: str, row: int | None = None) -> str | None:
    """Set or query selected row of decode list."""
    if row is None:
        return _query(resource_name, ":DECode:LIST:SCRoll?")
    _send(resource_name, f":DECode:LIST:SCRoll {row}")
    return None


def decode_list_result(resource_name: str, n: int) -> str:
    """Query decode list result for bus ``n`` (1 or 2)."""
    return _query(resource_name, f":DECode:LIST{n}:RESult?")


def decode_bus_state(resource_name: str, bus: int, state: bool | None = None) -> str | None:
    """Set or query decode bus ``n`` display state (ON|OFF)."""
    if state is None:
        return _query(resource_name, f":DECode:BUS{bus}?")
    _send(resource_name, f":DECode:BUS{bus} {'ON' if state else 'OFF'}")
    return None


def decode_bus_copy(resource_name: str, bus: int, operation: str) -> None:
    """Sync decode settings with trigger settings. {FROMtrigger|TOTRigger}"""
    _send(resource_name, f":DECode:BUS{bus}:COPY {operation}")


def decode_bus_format(resource_name: str, bus: int, fmt: str | None = None) -> str | None:
    """Set or query decode bus data format {BINary|DECimal|HEX|ASCii}."""
    if fmt is None:
        return _query(resource_name, f":DECode:BUS{bus}:FORMat?")
    _send(resource_name, f":DECode:BUS{bus}:FORMat {fmt}")
    return None


def decode_bus_protocol(resource_name: str, bus: int, protocol: str | None = None) -> str | None:
    """Set or query decode bus protocol. {IIC|SPI|UART|CAN|LIN|FLEXray|CANFd|IIS|M1553|SENT|MANchester|A429|USB20}"""
    if protocol is None:
        return _query(resource_name, f":DECode:BUS{bus}:PROTocol?")
    _send(resource_name, f":DECode:BUS{bus}:PROTocol {protocol}")
    return None


def decode_bus_result(resource_name: str, bus: int) -> str:
    """Query decode bus ``n`` result (short form, use :DECode:LIST<n>:RESult for full)."""
    return _query(resource_name, f":DECode:BUS{bus}:RESult?")


def decode_bus_iic_rwbit(resource_name: str, bus: int, state: bool | None = None) -> str | None:
    """Set or query whether IIC decode result includes R/W bit."""
    if state is None:
        return _query(resource_name, f":DECode:BUS{bus}:IIC:RWBit?")
    _send(resource_name, f":DECode:BUS{bus}:IIC:RWBit {'ON' if state else 'OFF'}")
    return None


def decode_bus_iic_scl_source(resource_name: str, bus: int, source: str | None = None) -> str | None:
    """Set or query IIC SCL source."""
    if source is None:
        return _query(resource_name, f":DECode:BUS{bus}:IIC:SCLSource?")
    _send(resource_name, f":DECode:BUS{bus}:IIC:SCLSource {source}")
    return None


def decode_bus_iic_sda_source(resource_name: str, bus: int, source: str | None = None) -> str | None:
    """Set or query IIC SDA source."""
    if source is None:
        return _query(resource_name, f":DECode:BUS{bus}:IIC:SDASource?")
    _send(resource_name, f":DECode:BUS{bus}:IIC:SDASource {source}")
    return None
