"""REF subsystem SCPI commands (reference waveforms)."""
from __future__ import annotations
from _base import _send, _query


def ref_label_state(resource_name: str, ref: str, state: bool | None = None) -> str | None:
    """Set or query reference waveform label on/off. <r>={A|B|C|D}"""
    if state is None:
        return _query(resource_name, f":REF{ref}:LABel?")
    _send(resource_name, f":REF{ref}:LABel {'ON' if state else 'OFF'}")
    return None


def ref_label_text(resource_name: str, ref: str, text: str | None = None) -> str | None:
    """Set or query reference waveform label text (max 20 chars)."""
    if text is None:
        return _query(resource_name, f":REF{ref}:LABel:TEXT?")
    _send(resource_name, f':REF{ref}:LABel:TEXT "{text}"')
    return None


def ref_data(resource_name: str, ref: str, op: str) -> None:
    """Reference data operation {LOAD|UNLoad|SAVE,<source>}."""
    _send(resource_name, f":REF{ref}:DATA {op}")


def ref_data_source(resource_name: str, ref: str) -> str:
    """Query current reference waveform source."""
    return _query(resource_name, f":REF{ref}:DATA:SOURce?")


def ref_data_scale(resource_name: str, ref: str, scale: float | None = None) -> str | None:
    """Set or query reference waveform vertical scale (only when stored+open)."""
    if scale is None:
        return _query(resource_name, f":REF{ref}:DATA:SCALe?")
    _send(resource_name, f":REF{ref}:DATA:SCALe {scale}")
    return None


def ref_data_position(resource_name: str, ref: str, pos: float | None = None) -> str | None:
    """Set or query reference waveform vertical offset (only when stored+open)."""
    if pos is None:
        return _query(resource_name, f":REF{ref}:DATA:POSition?")
    _send(resource_name, f":REF{ref}:DATA:POSition {pos}")
    return None
