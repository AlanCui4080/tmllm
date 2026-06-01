"""VISA resource management: detect systems, list instruments, open/close sessions."""

import logging
from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import Optional

import pyvisa

logger = logging.getLogger(__name__)

# Module-level singleton for the ResourceManager.  pyvisa is not
# thread-safe so we use a single global instance and guard access.
_rm: Optional[pyvisa.ResourceManager] = None
# Registry of currently open instrument sessions keyed by resource name.
_active_instruments: dict[str, pyvisa.Resource] = {}


def _get_resource_manager() -> pyvisa.ResourceManager:
    """Return the module-level pyvisa ResourceManager, creating it lazily."""
    global _rm
    if _rm is None:
        try:
            _rm = pyvisa.ResourceManager("@py")
        except (ValueError, pyvisa.VisaIOError):
            logger.info("pyvisa-py backend failed, falling back to system VISA.")
            _rm = pyvisa.ResourceManager()
    return _rm


@dataclass
class InstrumentInfo:
    """Metadata about a detected instrument."""

    resource_name: str
    alias: str = ""
    interface_type: str = ""
    description: str = ""
    manufacturer: str = ""
    model: str = ""
    serial: str = ""
    firmware: str = ""


def list_resources(query: str = "?*") -> list[str]:
    """List all VISA resources matching *query* (default: all)."""
    rm = _get_resource_manager()
    return rm.list_resources(query)


def detect_instruments(query: str = "?*") -> list[InstrumentInfo]:
    """Detect instruments and return enriched info including *IDN? results."""
    resources = list_resources(query)
    results: list[InstrumentInfo] = []
    for name in resources:
        info = InstrumentInfo(resource_name=name)
        try:
            rm = _get_resource_manager()
            inst = rm.open_resource(name)
            try:
                inst.timeout = 3000
                idn = inst.query("*IDN?").strip()
                parts = [p.strip() for p in idn.split(",")]
                if len(parts) >= 4:
                    info.manufacturer = parts[0]
                    info.model = parts[1]
                    info.serial = parts[2]
                    info.firmware = parts[3]
                info.description = idn
                # Parse interface type from resource name
                parts_name = name.split("::")
                if len(parts_name) >= 1:
                    info.interface_type = parts_name[0]
            finally:
                inst.close()
        except Exception as exc:
            logger.warning("Failed to query instrument %s: %s", name, exc)
        results.append(info)
    return results


def open_instrument(resource_name: str, **kwargs) -> pyvisa.Resource:
    """Open a VISA resource and cache it. Extra kwargs forwarded to open_resource."""
    if resource_name in _active_instruments:
        return _active_instruments[resource_name]
    rm = _get_resource_manager()
    inst = rm.open_resource(resource_name, **kwargs)
    _active_instruments[resource_name] = inst
    logger.info("Opened instrument: %s", resource_name)
    return inst


def close_instrument(resource_name: str) -> None:
    """Close a previously opened instrument session."""
    inst = _active_instruments.pop(resource_name, None)
    if inst is not None:
        inst.close()
        logger.info("Closed instrument: %s", resource_name)


def close_all_instruments() -> None:
    """Close all open instrument sessions."""
    for name in list(_active_instruments):
        close_instrument(name)


def get_instrument(resource_name: str) -> Optional[pyvisa.Resource]:
    """Get a cached instrument handle without opening a new one."""
    return _active_instruments.get(resource_name)


def is_open(resource_name: str) -> bool:
    """Check whether an instrument is currently open."""
    return resource_name in _active_instruments
