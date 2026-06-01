"""Instrument driver framework.

To add a new instrument driver, subclass ``BaseInstrument`` and register it
via the ``@register_instrument`` decorator::

    from instrument import BaseInstrument, register_instrument

    @register_instrument(model="34401A")
    class HP34401A(BaseInstrument):
        def measure_voltage_dc(self) -> float: ...
"""

from __future__ import annotations

import logging
import re
from typing import ClassVar, Optional

import pyvisa

import visa_manager
import ieee4882

logger = logging.getLogger(__name__)

_INSTRUMENT_REGISTRY: dict[str, type["BaseInstrument"]] = {}


def register_instrument(model: str):
    def decorator(cls: type[BaseInstrument]):
        _INSTRUMENT_REGISTRY[model] = cls
        cls._model = model
        logger.info("Registered instrument driver: %s -> %s", model, cls.__name__)
        return cls
    return decorator


def find_driver_for_idn(idn_str: str) -> Optional[type["BaseInstrument"]]:
    parts = idn_str.split(",")
    model = parts[1].strip() if len(parts) >= 2 else ""
    if model in _INSTRUMENT_REGISTRY:
        return _INSTRUMENT_REGISTRY[model]
    stripped = re.sub(r"^0+", "", model)
    if stripped in _INSTRUMENT_REGISTRY:
        return _INSTRUMENT_REGISTRY[stripped]
    return None


class BaseInstrument:
    _model: ClassVar[str] = ""

    def __init__(self, resource_name: str, **open_kwargs):
        self.resource_name = resource_name
        inst = visa_manager.get_instrument(resource_name)
        if inst is None:
            inst = visa_manager.open_instrument(resource_name, **open_kwargs)
        self._inst: pyvisa.Resource = inst

    # ── proxied 488.2 commands ──

    def cls(self) -> None:
        ieee4882.cls(self.resource_name)

    def ese(self, enable_value: int | None = None) -> str | None:
        return ieee4882.ese(self.resource_name, enable_value)

    def esr(self) -> str:
        return ieee4882.esr(self.resource_name)

    def idn(self) -> str:
        return ieee4882.idn(self.resource_name)

    def lrn(self) -> str:
        return ieee4882.lrn(self.resource_name)

    def opc(self) -> None:
        ieee4882.opc(self.resource_name)

    def opc_query(self) -> str:
        return ieee4882.opc_query(self.resource_name)

    def opt(self) -> str:
        return ieee4882.opt(self.resource_name)

    def psc(self, value: int | None = None) -> str | None:
        return ieee4882.psc(self.resource_name, value)

    def rcl(self, slot: int) -> None:
        ieee4882.rcl(self.resource_name, slot)

    def rst(self) -> None:
        ieee4882.rst(self.resource_name)

    def sav(self, slot: int) -> None:
        ieee4882.sav(self.resource_name, slot)

    def sre(self, enable_value: int | None = None) -> str | None:
        return ieee4882.sre(self.resource_name, enable_value)

    def stb(self) -> str:
        return ieee4882.stb(self.resource_name)

    def trg(self) -> None:
        ieee4882.trg(self.resource_name)

    def tst(self) -> str:
        return ieee4882.tst(self.resource_name)

    def wai(self) -> None:
        ieee4882.wai(self.resource_name)

    def syst_err(self) -> str:
        return ieee4882.syst_err(self.resource_name)

    # ── generic send / query ──

    def send(self, command: str) -> None:
        ieee4882.send(self.resource_name, command)

    def query(self, command: str) -> str:
        return ieee4882.query(self.resource_name, command)

    def read(self) -> str:
        return ieee4882.read(self.resource_name)

    def close(self) -> None:
        visa_manager.close_instrument(self.resource_name)

    @property
    def raw_handle(self) -> pyvisa.Resource:
        return self._inst

    @staticmethod
    def init_instrument(resource_name: str):
        pass
