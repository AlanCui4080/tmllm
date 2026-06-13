"""COUNter subsystem SCPI commands."""

from __future__ import annotations

from _base import _send, _query


def counter_state(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query the counter on/off state.

    SCPI: :COUNter {ON|OFF}
           :COUNter?

        Configures the counter on/off state.
        The counter measures frequency, period, and counts events on the selected signal.
        Measurements are performed on analog channel input signals only.

    Args:
        state: True=ON, False=OFF
        None — query current state

    Returns:
        "ON" or "OFF" when querying.
    """
    if state is None:
        return _query(resource_name, ":COUNter?")
    _send(resource_name, f":COUNter {'ON' if state else 'OFF'}")
    return None


def counter_current(resource_name: str) -> str:
    """Query the current counter measurement value.

    SCPI: :COUNter:CURRent?

        Queries the current counter measurement value.
        Note: counter accuracy is 7 digits; 3 digits are returned by default. Use :FORMat:DATA to request higher precision.

    Returns:
        Current counter value in NR3 format (e.g. "1.00E+3").
    """
    return _query(resource_name, ":COUNter:CURRent?")


def counter_level(resource_name: str, level: float | None = None) -> str | None:
    """Set or query the counter threshold level.

    SCPI: :COUNter:LEVel <value>
           :COUNter:LEVel?

        Configures the counter threshold level.
        Range varies by model: SDS7000A: [-4.26*V/div-offset, 4.26*V/div-offset], SDS6000Pro/A/L: [-4.5*V/div-offset, 4.5*V/div-offset], others: [-4.1*V/div-offset, 4.1*V/div-offset].

    Args:
        level: Counter threshold level in volts (NR3)

    Returns:
        Current level when querying (e.g. "5.00E-1").
    """
    if level is None:
        return _query(resource_name, ":COUNter:LEVel?")
    _send(resource_name, f":COUNter:LEVel {level}")
    return None


def counter_mode(resource_name: str, mode: str | None = None) -> str | None:
    """Set or query the counter measurement mode.

    SCPI: :COUNter:MODE <type>
           :COUNter:MODE?

        Configures the counter measurement mode.
        FREQuency — average frequency over a time window
        PERiod    — reciprocal of the average frequency
        TOTalizer — cumulative event count

    Args:
        mode: {FREQuency|PERiod|TOTalizer}

    Returns:
        Current mode when querying (e.g. "FREQ").
    """
    if mode is None:
        return _query(resource_name, ":COUNter:MODE?")
    _send(resource_name, f":COUNter:MODE {mode}")
    return None


def counter_source(resource_name: str, source: str | None = None) -> str | None:
    """Set or query the counter signal source channel.

    SCPI: :COUNter:SOURce <source>
           :COUNter:SOURce?

        Configures the signal source channel for the counter.

    Args:
        source: {C1|C2|C3|C4} — analog channel number

    Returns:
        Current source when querying (e.g. "C1").
    """
    if source is None:
        return _query(resource_name, ":COUNter:SOURce?")
    _send(resource_name, f":COUNter:SOURce {source}")
    return None


def counter_statistics(resource_name: str, enable: bool | None = None) -> str | None:
    """Set or query the counter statistics on/off state.

    SCPI: :COUNter:STATistics {ON|OFF}
           :COUNter:STATistics?

        Configures the counter statistics display on/off state.
        Statistics are available only in Frequency and Period modes.

    Args:
        enable: True=ON, False=OFF

    Returns:
        "ON" or "OFF" when querying.
    """
    if enable is None:
        return _query(resource_name, ":COUNter:STATistics?")
    _send(resource_name, f":COUNter:STATistics {'ON' if enable else 'OFF'}")
    return None


def counter_statistics_reset(resource_name: str) -> None:
    """Reset counter statistics.

    SCPI: :COUNter:STATistics:RESet

        Resets counter statistics. Effective only in Period and Frequency modes.

    Associated commands: :COUNter:STATistics
    """
    _send(resource_name, ":COUNter:STATistics:RESet")


def counter_statistics_value(resource_name: str) -> str:
    """Query the counter statistics values.

    SCPI: :COUNter:STATistics:VALue?

        Queries the current counter statistics. Available only in Frequency and Period modes.
        Returns: <current>,<mean>,<min>,<max>,<stdev>,<count>
          current — current measurement (NR3)
          mean    — statistical mean (NR3)
          min     — minimum value (NR3)
          max     — maximum value (NR3)
          stdev   — standard deviation (NR3)
          count   — number of measurements (NR1)
        Note: returns "OFF" when statistics are disabled.

    Returns:
        Comma-separated statistics values (e.g.
        "1.00E+03,1.00E+03,1.00E+03,1.00E+03,1.52E-02,312").
    """
    return _query(resource_name, ":COUNter:STATistics:VALue?")


def counter_totalizer_gate(resource_name: str, enable: bool | None = None) -> str | None:
    """Set or query the counter totalizer gate on/off state.

    SCPI: :COUNter:TOTalizer:GATE {ON|OFF}
           :COUNter:TOTalizer:GATE?

        Configures the counter totalizer gate on/off state.

    Args:
        enable: True=ON, False=OFF

    Returns:
        "ON" or "OFF" when querying.
    """
    if enable is None:
        return _query(resource_name, ":COUNter:TOTalizer:GATE?")
    _send(resource_name, f":COUNter:TOTalizer:GATE {'ON' if enable else 'OFF'}")
    return None


def counter_totalizer_gate_level(resource_name: str, level: float | None = None) -> str | None:
    """Set or query the counter totalizer gate threshold level.

    SCPI: :COUNter:TOTalizer:GATE:LEVel <value>
           :COUNter:TOTalizer:GATE:LEVel?

        Configures the counter totalizer gate threshold level. Range varies by model (same as :COUNter:LEVel).

    Args:
        level: Gate threshold level in volts (NR3)

    Returns:
        Current gate level when querying (e.g. "5.00E-1").
    """
    if level is None:
        return _query(resource_name, ":COUNter:TOTalizer:GATE:LEVel?")
    _send(resource_name, f":COUNter:TOTalizer:GATE:LEVel {level}")
    return None


def counter_totalizer_gate_slope(resource_name: str, slope: str | None = None) -> str | None:
    """Set or query the counter totalizer gate slope/polarity.

    SCPI: :COUNter:TOTalizer:GATE:SLOPe <slope>
           :COUNter:TOTalizer:GATE:SLOPe?

        Configures the slope/polarity of the counter gate source.
        When gate type is Level, this sets polarity; when type is Edge, this sets slope.
        RISing  — rising edge / positive polarity
        FALLing — falling edge / negative polarity

    Args:
        slope: {RISing|FALLing}

    Returns:
        Current slope when querying (e.g. "RISing").
    """
    if slope is None:
        return _query(resource_name, ":COUNter:TOTalizer:GATE:SLOPe?")
    _send(resource_name, f":COUNter:TOTalizer:GATE:SLOPe {slope}")
    return None


def counter_totalizer_gate_type(resource_name: str, gate_type: str | None = None) -> str | None:
    """Set or query the counter totalizer gate type.

    SCPI: :COUNter:TOTalizer:GATE:TYPE <style>
           :COUNter:TOTalizer:GATE:TYPE?

        Configures the counter gate type.
        LEVel — level-based gating
        AEDGe — edge-based gating (gate opens after edge)

    Args:
        gate_type: {LEVel|AEDGe}

    Returns:
        Current gate type when querying (e.g. "LEVel").
    """
    if gate_type is None:
        return _query(resource_name, ":COUNter:TOTalizer:GATE:TYPE?")
    _send(resource_name, f":COUNter:TOTalizer:GATE:TYPE {gate_type}")
    return None


def counter_totalizer_reset(resource_name: str) -> None:
    """Reset the counter totalizer accumulated result.

    SCPI: :COUNter:TOTalizer:RESet

        Resets the counter totalizer accumulated result.
    """
    _send(resource_name, ":COUNter:TOTalizer:RESet")


def counter_totalizer_slope(resource_name: str, slope: str | None = None) -> str | None:
    """Set or query the counter totalizer counting slope.

    SCPI: :COUNter:TOTalizer:SLOPe <slope>
           :COUNter:TOTalizer:SLOPe?

        Configures the counting source slope.
        RISing  — count on rising edges
        FALLing — count on falling edges

    Args:
        slope: {RISing|FALLing}

    Returns:
        Current slope when querying (e.g. "RISing").
    """
    if slope is None:
        return _query(resource_name, ":COUNter:TOTalizer:SLOPe?")
    _send(resource_name, f":COUNter:TOTalizer:SLOPe {slope}")
    return None
