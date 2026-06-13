"""RECall subsystem SCPI commands."""

from __future__ import annotations

from _base import _send


def recall_factory_default(resource_name: str) -> None:
    """Recall factory default settings.

    SCPI: :RECall:FDEFault
    """
    _send(resource_name, ":RECall:FDEFault")


def recall_reference(resource_name: str, ref: str, path: str) -> None:
    """Recall reference waveform from file.

    SCPI: :RECall:REFerence <location>,<path>
    e.g. recall_reference(rn, "REFD", "U-disk0/SIGLENT/math.ref")
    """
    _send(resource_name, f':RECall:REFerence {ref},"{path}"')


def recall_serase(resource_name: str) -> None:
    """Erase all user files stored internally."""
    _send(resource_name, ":RECall:SERase")


def recall_setup(resource_name: str, arg: str) -> None:
    """Recall setup: INTernal,<num> or EXTernal,<path>."""
    _send(resource_name, f":RECall:SETup {arg}")
