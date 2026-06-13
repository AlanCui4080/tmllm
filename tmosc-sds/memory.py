"""MEMory subsystem SCPI commands."""

from __future__ import annotations

from _base import _send, _query


def memory_horizontal_position(resource_name: str, m: int, pos: float | None = None) -> str | None:
    """Set or query memory waveform horizontal position."""
    if pos is None:
        return _query(resource_name, f":MEMory{m}:HORizontal:POSition?")
    _send(resource_name, f":MEMory{m}:HORizontal:POSition {pos}")
    return None


def memory_horizontal_scale(resource_name: str, m: int, scale: float | None = None) -> str | None:
    """Set or query memory waveform horizontal scale (s/div)."""
    if scale is None:
        return _query(resource_name, f":MEMory{m}:HORizontal:SCALe?")
    _send(resource_name, f":MEMory{m}:HORizontal:SCALe {scale}")
    return None


def memory_horizontal_sync(resource_name: str, m: int, state: bool | None = None) -> str | None:
    """Set or query memory waveform sync with window on/off."""
    if state is None:
        return _query(resource_name, f":MEMory{m}:HORizontal:SYNC?")
    _send(resource_name, f":MEMory{m}:HORizontal:SYNC {'ON' if state else 'OFF'}")
    return None


def memory_import(resource_name: str, m: int, source: str) -> None:
    """Import waveform data into memory M<m>. Source: {C<n>|Z<n>|F<x>|M<m>|<path>}."""
    _send(resource_name, f":MEMory{m}:IMPort {source}")


def memory_label_state(resource_name: str, m: int, state: bool | None = None) -> str | None:
    """Set or query memory waveform label display on/off."""
    if state is None:
        return _query(resource_name, f":MEMory{m}:LABel?")
    _send(resource_name, f":MEMory{m}:LABel {'ON' if state else 'OFF'}")
    return None


def memory_label_text(resource_name: str, m: int, text: str | None = None) -> str | None:
    """Set or query memory waveform label text (max 20 chars)."""
    if text is None:
        return _query(resource_name, f":MEMory{m}:LABel:TEXT?")
    _send(resource_name, f':MEMory{m}:LABel:TEXT "{text}"')
    return None


def memory_switch(resource_name: str, m: int, state: bool | None = None) -> str | None:
    """Set or query memory waveform display on/off."""
    if state is None:
        return _query(resource_name, f":MEMory{m}:SWITch?")
    _send(resource_name, f":MEMory{m}:SWITch {'ON' if state else 'OFF'}")
    return None


def memory_vertical_position(resource_name: str, m: int, pos: float | None = None) -> str | None:
    """Set or query memory waveform vertical position."""
    if pos is None:
        return _query(resource_name, f":MEMory{m}:VERTical:POSition?")
    _send(resource_name, f":MEMory{m}:VERTical:POSition {pos}")
    return None


def memory_vertical_scale(resource_name: str, m: int, scale: float | None = None) -> str | None:
    """Set or query memory waveform vertical scale."""
    if scale is None:
        return _query(resource_name, f":MEMory{m}:VERTical:SCALe?")
    _send(resource_name, f":MEMory{m}:VERTical:SCALe {scale}")
    return None
