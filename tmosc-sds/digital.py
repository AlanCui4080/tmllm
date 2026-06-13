"""DIGital subsystem SCPI commands."""
from __future__ import annotations
from _base import _send, _query


def digital_state(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query digital channels on/off state.

    SCPI: :DIGital {ON|OFF}

        Configures the digital channel display on/off state.
        ON  — show digital channels
        OFF — hide digital channels
    """
    if state is None:
        return _query(resource_name, ":DIGital?")
    _send(resource_name, f":DIGital {'ON' if state else 'OFF'}")
    return None


def digital_active(resource_name: str, channel: str | None = None) -> str | None:
    """Set or query the currently active digital channel. {D0..D15}"""
    if channel is None:
        return _query(resource_name, ":DIGital:ACTive?")
    _send(resource_name, f":DIGital:ACTive {channel}")
    return None


def digital_bus_display(resource_name: str, bus: int, state: bool | None = None) -> str | None:
    """Set or query digital bus ``n`` display state."""
    if state is None:
        return _query(resource_name, f":DIGital:BUS{bus}:DISPlay?")
    _send(resource_name, f":DIGital:BUS{bus}:DISPlay {'ON' if state else 'OFF'}")
    return None


def digital_bus_default(resource_name: str, bus: int) -> None:
    """Reset digital bus bit sequence to default."""
    _send(resource_name, f":DIGital:BUS{bus}:DEFault")


def digital_bus_format(resource_name: str, bus: int, fmt: str | None = None) -> str | None:
    """Set or query digital bus format {BINary|DECimal|UDECimal|HEX}."""
    if fmt is None:
        return _query(resource_name, f":DIGital:BUS{bus}:FORMat?")
    _send(resource_name, f":DIGital:BUS{bus}:FORMat {fmt}")
    return None


def digital_bus_map(resource_name: str, bus: int, mapping: str | None = None) -> str | None:
    """Set or query digital bus bit mapping (e.g. "D0,D3,D7,D15")."""
    if mapping is None:
        return _query(resource_name, f":DIGital:BUS{bus}:MAP?")
    _send(resource_name, f":DIGital:BUS{bus}:MAP {mapping}")
    return None


def digital_channel_state(resource_name: str, d: int, state: bool | None = None) -> str | None:
    """Set or query digital channel D<d> on/off state."""
    if state is None:
        return _query(resource_name, f":DIGital:D{d}?")
    _send(resource_name, f":DIGital:D{d} {'ON' if state else 'OFF'}")
    return None


def digital_height(resource_name: str, height: float | None = None) -> str | None:
    """Set or query digital channel display height [4.0, 8.0] div."""
    if height is None:
        return _query(resource_name, ":DIGital:HEIGht?")
    _send(resource_name, f":DIGital:HEIGht {height}")
    return None


def digital_label(resource_name: str, d: int, label: str | None = None) -> str | None:
    """Set or query digital channel D<d> label (max 8 chars)."""
    if label is None:
        return _query(resource_name, f":DIGital:LABel{d}?")
    _send(resource_name, f':DIGital:LABel{d} "{label}"')
    return None


def digital_points(resource_name: str) -> str:
    """Query digital channel sample points."""
    return _query(resource_name, ":DIGital:POINts?")


def digital_position(resource_name: str, pos: float | None = None) -> str | None:
    """Set or query digital channel vertical display position."""
    if pos is None:
        return _query(resource_name, ":DIGital:POSition?")
    _send(resource_name, f":DIGital:POSition {pos}")
    return None


def digital_skew(resource_name: str, skew: float | None = None) -> str | None:
    """Set or query digital channel deskew [-1.00E-07, 1.00E-07] s."""
    if skew is None:
        return _query(resource_name, ":DIGital:SKEW?")
    _send(resource_name, f":DIGital:SKEW {skew}")
    return None


def digital_srate(resource_name: str) -> str:
    """Query digital channel sample rate."""
    return _query(resource_name, ":DIGital:SRATe?")


def digital_threshold(resource_name: str, group: int, thresh: str | None = None) -> str | None:
    """Set or query digital group ``n`` threshold. {TTL|CMOS|LVCMOS33|LVCMOS25|CUSTom,<value>}
    group 1=D0-D7, group 2=D8-D15."""
    if thresh is None:
        return _query(resource_name, f":DIGital:THReshold{group}?")
    _send(resource_name, f":DIGital:THReshold{group} {thresh}")
    return None
