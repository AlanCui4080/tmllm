"""SEARch subsystem SCPI commands (event search)."""
from __future__ import annotations
from _base import _send, _query


def search_state(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query search function on/off."""
    if state is None:
        return _query(resource_name, ":SEARch?")
    _send(resource_name, f":SEARch {'ON' if state else 'OFF'}")
    return None


def search_mode(resource_name: str, mode: str | None = None) -> str | None:
    """Set or query search mode {EDGE|SLOPe|PULSE|INTerval|RUNT}."""
    if mode is None:
        return _query(resource_name, ":SEARch:MODE?")
    _send(resource_name, f":SEARch:MODE {mode}")
    return None


def search_count(resource_name: str) -> str:
    """Query total search event count on screen."""
    return _query(resource_name, ":SEARch:COUNT?")


def search_event(resource_name: str) -> str:
    """Query positioned event frame number when acquisition stopped."""
    return _query(resource_name, ":SEARch:EVENt?")


def search_copy(resource_name: str, operation: str) -> None:
    """Sync search/trigger settings {FROMtrigger|TOTRigger|CANCel}."""
    _send(resource_name, f":SEARch:COPY {operation}")


def search_edge_source(resource_name: str, source: str | None = None) -> str | None:
    """Set or query edge search source {C<n>|D<d>}."""
    if source is None:
        return _query(resource_name, ":SEARch:EDGE:SOURce?")
    _send(resource_name, f":SEARch:EDGE:SOURce {source}")
    return None


def search_edge_slope(resource_name: str, slope: str | None = None) -> str | None:
    """Set or query edge search slope {RISing|FALLing|ALTernate}."""
    if slope is None:
        return _query(resource_name, ":SEARch:EDGE:SLOPe?")
    _send(resource_name, f":SEARch:EDGE:SLOPe {slope}")
    return None


def search_edge_level(resource_name: str, level: float | None = None) -> str | None:
    """Set or query edge search level (volts)."""
    if level is None:
        return _query(resource_name, ":SEARch:EDGE:LEVel?")
    _send(resource_name, f":SEARch:EDGE:LEVel {level}")
    return None


def search_slope_source(resource_name: str, source: str | None = None) -> str | None:
    """Set or query slope search source {C<n>}."""
    if source is None:
        return _query(resource_name, ":SEARch:SLOPe:SOURce?")
    _send(resource_name, f":SEARch:SLOPe:SOURce {source}")
    return None


def search_slope_slope(resource_name: str, slope: str | None = None) -> str | None:
    """Set or query slope search slope {RISing|FALLing}."""
    if slope is None:
        return _query(resource_name, ":SEARch:SLOPe:SLOPe?")
    _send(resource_name, f":SEARch:SLOPe:SLOPe {slope}")
    return None


def search_slope_hlevel(resource_name: str, level: float | None = None) -> str | None:
    """Set or query slope search high level (volts)."""
    if level is None:
        return _query(resource_name, ":SEARch:SLOPe:HLEVel?")
    _send(resource_name, f":SEARch:SLOPe:HLEVel {level}")
    return None


def search_slope_llevel(resource_name: str, level: float | None = None) -> str | None:
    """Set or query slope search low level (volts)."""
    if level is None:
        return _query(resource_name, ":SEARch:SLOPe:LLEVel?")
    _send(resource_name, f":SEARch:SLOPe:LLEVel {level}")
    return None


def search_slope_limit(resource_name: str, limit: str | None = None) -> str | None:
    """Set or query slope search limit type {LESSthan|GREATerthan|INNer|OUTer}."""
    if limit is None:
        return _query(resource_name, ":SEARch:SLOPe:LIMit?")
    _send(resource_name, f":SEARch:SLOPe:LIMit {limit}")
    return None


def search_slope_tupper(resource_name: str, value: float | None = None) -> str | None:
    """Set or query slope search upper time limit (s)."""
    if value is None:
        return _query(resource_name, ":SEARch:SLOPe:TUPPer?")
    _send(resource_name, f":SEARch:SLOPe:TUPPer {value}")
    return None


def search_slope_tlower(resource_name: str, value: float | None = None) -> str | None:
    """Set or query slope search lower time limit (s)."""
    if value is None:
        return _query(resource_name, ":SEARch:SLOPe:TLOWer?")
    _send(resource_name, f":SEARch:SLOPe:TLOWer {value}")
    return None


def search_pulse_source(resource_name: str, source: str | None = None) -> str | None:
    """Set or query pulse width search source."""
    if source is None:
        return _query(resource_name, ":SEARch:PULSe:SOURce?")
    _send(resource_name, f":SEARch:PULSe:SOURce {source}")
    return None


def search_pulse_polarity(resource_name: str, polarity: str | None = None) -> str | None:
    """Set or query pulse search polarity {POSitive|NEGative}."""
    if polarity is None:
        return _query(resource_name, ":SEARch:PULSe:POLarity?")
    _send(resource_name, f":SEARch:PULSe:POLarity {polarity}")
    return None


def search_pulse_level(resource_name: str, level: float | None = None) -> str | None:
    """Set or query pulse search level (volts)."""
    if level is None:
        return _query(resource_name, ":SEARch:PULSe:LEVel?")
    _send(resource_name, f":SEARch:PULSe:LEVel {level}")
    return None


def search_pulse_limit(resource_name: str, limit: str | None = None) -> str | None:
    """Set or query pulse search limit type {LESSthan|GREATerthan|INNer|OUTer}."""
    if limit is None:
        return _query(resource_name, ":SEARch:PULSe:LIMit?")
    _send(resource_name, f":SEARch:PULSe:LIMit {limit}")
    return None


def search_pulse_tupper(resource_name: str, value: float | None = None) -> str | None:
    """Set or query pulse search upper time limit (s)."""
    if value is None:
        return _query(resource_name, ":SEARch:PULSe:TUPPer?")
    _send(resource_name, f":SEARch:PULSe:TUPPer {value}")
    return None


def search_pulse_tlower(resource_name: str, value: float | None = None) -> str | None:
    """Set or query pulse search lower time limit (s)."""
    if value is None:
        return _query(resource_name, ":SEARch:PULSe:TLOWer?")
    _send(resource_name, f":SEARch:PULSe:TLOWer {value}")
    return None


def search_interval_source(resource_name: str, source: str | None = None) -> str | None:
    """Set or query interval search source."""
    if source is None:
        return _query(resource_name, ":SEARch:INTerval:SOURce?")
    _send(resource_name, f":SEARch:INTerval:SOURce {source}")
    return None


def search_interval_slope(resource_name: str, slope: str | None = None) -> str | None:
    """Set or query interval search slope {RISing|FALLing}."""
    if slope is None:
        return _query(resource_name, ":SEARch:INTerval:SLOPe?")
    _send(resource_name, f":SEARch:INTerval:SLOPe {slope}")
    return None


def search_interval_level(resource_name: str, level: float | None = None) -> str | None:
    """Set or query interval search level (volts)."""
    if level is None:
        return _query(resource_name, ":SEARch:INTerval:LEVel?")
    _send(resource_name, f":SEARch:INTerval:LEVel {level}")
    return None


def search_interval_limit(resource_name: str, limit: str | None = None) -> str | None:
    """Set or query interval search limit type."""
    if limit is None:
        return _query(resource_name, ":SEARch:INTerval:LIMit?")
    _send(resource_name, f":SEARch:INTerval:LIMit {limit}")
    return None


def search_interval_tupper(resource_name: str, value: float | None = None) -> str | None:
    """Set or query interval search upper time limit (s)."""
    if value is None:
        return _query(resource_name, ":SEARch:INTerval:TUPPer?")
    _send(resource_name, f":SEARch:INTerval:TUPPer {value}")
    return None


def search_interval_tlower(resource_name: str, value: float | None = None) -> str | None:
    """Set or query interval search lower time limit (s)."""
    if value is None:
        return _query(resource_name, ":SEARch:INTerval:TLOWer?")
    _send(resource_name, f":SEARch:INTerval:TLOWer {value}")
    return None


def search_runt_source(resource_name: str, source: str | None = None) -> str | None:
    """Set or query runt search source {C<n>}."""
    if source is None:
        return _query(resource_name, ":SEARch:RUNT:SOURce?")
    _send(resource_name, f":SEARch:RUNT:SOURce {source}")
    return None


def search_runt_polarity(resource_name: str, polarity: str | None = None) -> str | None:
    """Set or query runt search polarity {POSitive|NEGative}."""
    if polarity is None:
        return _query(resource_name, ":SEARch:RUNT:POLarity?")
    _send(resource_name, f":SEARch:RUNT:POLarity {polarity}")
    return None


def search_runt_hlevel(resource_name: str, level: float | None = None) -> str | None:
    """Set or query runt search high level (volts)."""
    if level is None:
        return _query(resource_name, ":SEARch:RUNT:HLEVel?")
    _send(resource_name, f":SEARch:RUNT:HLEVel {level}")
    return None


def search_runt_llevel(resource_name: str, level: float | None = None) -> str | None:
    """Set or query runt search low level (volts)."""
    if level is None:
        return _query(resource_name, ":SEARch:RUNT:LLEVel?")
    _send(resource_name, f":SEARch:RUNT:LLEVel {level}")
    return None


def search_runt_limit(resource_name: str, limit: str | None = None) -> str | None:
    """Set or query runt search limit type {LESSthan|GREATerthan|INNer|OUTer}."""
    if limit is None:
        return _query(resource_name, ":SEARch:RUNT:LIMit?")
    _send(resource_name, f":SEARch:RUNT:LIMit {limit}")
    return None


def search_runt_tupper(resource_name: str, value: float | None = None) -> str | None:
    """Set or query runt search upper time limit (s)."""
    if value is None:
        return _query(resource_name, ":SEARch:RUNT:TUPPer?")
    _send(resource_name, f":SEARch:RUNT:TUPPer {value}")
    return None


def search_runt_tlower(resource_name: str, value: float | None = None) -> str | None:
    """Set or query runt search lower time limit (s)."""
    if value is None:
        return _query(resource_name, ":SEARch:RUNT:TLOWer?")
    _send(resource_name, f":SEARch:RUNT:TLOWer {value}")
    return None
