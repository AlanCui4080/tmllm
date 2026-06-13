"""DVM subsystem SCPI commands (Digital Voltmeter)."""
from __future__ import annotations
from _base import _send, _query


def dvm_state(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query the DVM (Digital Voltmeter) on/off state.

    SCPI: :DVM {ON|OFF}
           :DVM?

        Configures the DVM (Digital Voltmeter) on/off state. The DVM measures DC and AC amplitudes.

    Args:
        state: True=ON, False=OFF

    Returns:
        "ON" or "OFF" when querying.
    """
    if state is None:
        return _query(resource_name, ":DVM?")
    _send(resource_name, f":DVM {'ON' if state else 'OFF'}")
    return None


def dvm_alarm(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query the DVM over-range alarm state.

    SCPI: :DVM:ALARm {ON|OFF}
           :DVM:ALARm?

        Configures the DVM over-range alarm on/off state. When enabled, an alarm triggers if the signal amplitude exceeds the screen range.

    Args:
        state: True=ON, False=OFF

    Returns:
        "ON" or "OFF" when querying.
    """
    if state is None:
        return _query(resource_name, ":DVM:ALARm?")
    _send(resource_name, f":DVM:ALARm {'ON' if state else 'OFF'}")
    return None


def dvm_autorange(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query the DVM auto-range state.

    SCPI: :DVM:ARANge {ON|OFF}
           :DVM:ARANge?

        Configures the DVM auto-range on/off state.

    Args:
        state: True=ON, False=OFF

    Returns:
        "ON" or "OFF" when querying.
    """
    if state is None:
        return _query(resource_name, ":DVM:ARANge?")
    _send(resource_name, f":DVM:ARANge {'ON' if state else 'OFF'}")
    return None


def dvm_current(resource_name: str) -> str:
    """Query the DVM current measurement value.

    SCPI: :DVM:CURRent?

        Queries the DVM measurement value in the current mode. Default precision is 3 significant digits.

    Returns:
        Measurement value in NR3 format (e.g. "0.98E+00").
    """
    return _query(resource_name, ":DVM:CURRent?")


def dvm_hold(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query the DVM hold state.

    SCPI: :DVM:HOLD {ON|OFF}
           :DVM:HOLD?

        Configures the DVM hold on/off state. When enabled, the displayed measurement value is frozen while background measurement continues.

    Args:
        state: True=ON, False=OFF

    Returns:
        "ON" or "OFF" when querying.
    """
    if state is None:
        return _query(resource_name, ":DVM:HOLD?")
    _send(resource_name, f":DVM:HOLD {'ON' if state else 'OFF'}")
    return None


def dvm_mode(resource_name: str, mode: str | None = None) -> str | None:
    """Set or query the DVM measurement mode.

    SCPI: :DVM:MODE <mode>
           :DVM:MODE?

        Configures the DVM measurement mode.
        DCavg     — DC average: arithmetic mean of waveform data
        DCRMs     — DC RMS: root mean square of all data with DC coupling
        ACRMs     — AC RMS: root mean square of all data with AC coupling
        PKPK      — peak-to-peak: difference between maximum and minimum
        AMPLitude — amplitude: difference between top and base values

    Args:
        mode: {DCavg|DCRMs|ACRMs|PKPK|AMPLitude}

    Returns:
        Current mode when querying.
    """
    if mode is None:
        return _query(resource_name, ":DVM:MODE?")
    _send(resource_name, f":DVM:MODE {mode}")
    return None


def dvm_source(resource_name: str, source: str | None = None) -> str | None:
    """Set or query the DVM measurement source channel.

    SCPI: :DVM:SOURce <source>
           :DVM:SOURce?

        Configures the DVM measurement source (analog channel).
        <source>:= {C1|C2|C3|C4}

    Args:
        source: Channel (e.g. "C2")

    Returns:
        Current source when querying.
    """
    if source is None:
        return _query(resource_name, ":DVM:SOURce?")
    _send(resource_name, f":DVM:SOURce {source}")
    return None
