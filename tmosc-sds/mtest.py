"""MTESt subsystem SCPI commands (Mask Test)."""
from __future__ import annotations

from _base import _send, _query


def mtest_state(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query mask test on/off state.

    SCPI: :MTESt {ON|OFF}
    """
    if state is None:
        return _query(resource_name, ":MTESt?")
    _send(resource_name, f":MTESt {'ON' if state else 'OFF'}")
    return None


def mtest_count(resource_name: str) -> str:
    """Query mask test results: FAIL,<n>,PASS,<n>,TOTAL,<n>."""
    return _query(resource_name, ":MTESt:COUNt?")


def mtest_function_buzzer(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query mask test buzzer on/off."""
    if state is None:
        return _query(resource_name, ":MTESt:FUNCtion:BUZZer?")
    _send(resource_name, f":MTESt:FUNCtion:BUZZer {'ON' if state else 'OFF'}")
    return None


def mtest_function_cof(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query mask test failure screenshot capture on/off."""
    if state is None:
        return _query(resource_name, ":MTESt:FUNCtion:COF?")
    _send(resource_name, f":MTESt:FUNCtion:COF {'ON' if state else 'OFF'}")
    return None


def mtest_function_fth(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query mask test failure stop on/off."""
    if state is None:
        return _query(resource_name, ":MTESt:FUNCtion:FTH?")
    _send(resource_name, f":MTESt:FUNCtion:FTH {'ON' if state else 'OFF'}")
    return None


def mtest_function_sof(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query mask test stop on failure on/off."""
    if state is None:
        return _query(resource_name, ":MTESt:FUNCtion:SOF?")
    _send(resource_name, f":MTESt:FUNCtion:SOF {'ON' if state else 'OFF'}")
    return None


def mtest_idisplay(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query mask test info display on/off."""
    if state is None:
        return _query(resource_name, ":MTESt:IDISplay?")
    _send(resource_name, f":MTESt:IDISplay {'ON' if state else 'OFF'}")
    return None


def mtest_mask_create(resource_name: str, xmargin: float, ymargin: float) -> None:
    """Create mask based on current waveform.

    SCPI: :MTESt:MASK:CREate <XMARgin>,<YMARgin>

        Creates a mask based on the current waveform.
        <XMARgin> — horizontal X margin (float NR2)
        <YMARgin> — vertical Y margin (float NR2)

    Args:
        xmargin: Horizontal margin value
        ymargin: Vertical margin value
    """
    _send(resource_name, f":MTESt:MASK:CREate {xmargin},{ymargin}")


def mtest_mask_load(resource_name: str, location: str) -> None:
    """Load mask from file or internal memory.

    SCPI: :MTESt:MASK:LOAD <location>

        Loads a mask file from internal memory or external storage.
        INTernal,<num> — load from internal storage, <num> [1,4]
        EXTernal,<path> — load from external file (.msk/.smsk)

    Args:
        location: {INTernal,<num>|EXTernal,<path>}
            e.g. "INTernal,1" or 'EXTernal,"mask.msk"'
    """
    _send(resource_name, f":MTESt:MASK:LOAD {location}")


def mtest_operate(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query mask test run state.

    SCPI: :MTESt:OPERate <state>
           :MTESt:OPERate?

        Configures the mask test run state.

    Args:
        state: True=ON (start test), False=OFF (stop test)
        None — query

    Returns:
        "ON" or "OFF" when querying.
    """
    if state is None:
        return _query(resource_name, ":MTESt:OPERate?")
    _send(resource_name, f":MTESt:OPERate {'ON' if state else 'OFF'}")
    return None


def mtest_reset(resource_name: str) -> None:
    """Reset mask test statistics."""
    _send(resource_name, ":MTESt:RESet")


def mtest_source(resource_name: str, source: str | None = None) -> str | None:
    """Set or query mask test source."""
    if source is None:
        return _query(resource_name, ":MTESt:SOURce?")
    _send(resource_name, f":MTESt:SOURce {source}")
    return None


def mtest_type(resource_name: str, mtype: str | None = None) -> str | None:
    """Set or query mask test type."""
    if mtype is None:
        return _query(resource_name, ":MTESt:TYPE?")
    _send(resource_name, f":MTESt:TYPE {mtype}")
    return None
