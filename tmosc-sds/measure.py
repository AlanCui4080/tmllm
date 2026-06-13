"""MEASure subsystem SCPI commands."""

from __future__ import annotations

from _base import _send, _query


def measure_state(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query the measurement on/off state.

    SCPI: :MEASure {ON|OFF}
           :MEASure?

        Configures the measurement on/off state.

    Args:
        state: True=ON, False=OFF

    Returns:
        "ON" or "OFF" when querying.
    """
    if state is None:
        return _query(resource_name, ":MEASure?")
    _send(resource_name, f":MEASure {'ON' if state else 'OFF'}")
    return None


def measure_mode(resource_name: str, mode: str | None = None) -> str | None:
    """Set or query the measurement display mode.

    SCPI: :MEASure:MODE <mode>
           :MEASure:MODE?

        Configures the measurement display mode.
        SIMPle  — simple measurement: up to 5 items displayed simultaneously
        ADVanced — advanced measurement: up to 12 items displayed simultaneously

    Args:
        mode: {SIMPle|ADVanced}

    Returns:
        Current mode when querying.
    """
    if mode is None:
        return _query(resource_name, ":MEASure:MODE?")
    _send(resource_name, f":MEASure:MODE {mode}")
    return None


def measure_advanced_clear(resource_name: str) -> None:
    """Clear all advanced measurement items.

    SCPI: :MEASure:ADVanced:CLEar

        Clears all advanced measurement items.
    """
    _send(resource_name, ":MEASure:ADVanced:CLEar")


def measure_advanced_line_number(resource_name: str, count: int | None = None) -> str | None:
    """Set or query the number of advanced measurement items displayed (M2 mode).

    SCPI: :MEASure:ADVanced:LINenumber <value>
           :MEASure:ADVanced:LINenumber?

        Configures the number of measurement items displayed in advanced (M2) mode. Range [1,12].

    Args:
        count: Number of items to display (1-12)

    Returns:
        Current line number when querying.
    """
    if count is None:
        return _query(resource_name, ":MEASure:ADVanced:LINenumber?")
    _send(resource_name, f":MEASure:ADVanced:LINenumber {count}")
    return None


def measure_advanced_p_state(resource_name: str, n: int, state: bool | None = None) -> str | None:
    """Set or query advanced measurement item ``n`` on/off state.

    SCPI: :MEASure:ADVanced:P<n> {ON|OFF}

        Configures the on/off state for advanced measurement item ``n``.
        <n>:= [1,12]

    Args:
        n: Measurement item index (1-12)
        state: True=ON, False=OFF

    Returns:
        "ON" or "OFF" when querying.
    """
    if state is None:
        return _query(resource_name, f":MEASure:ADVanced:P{n}?")
    _send(resource_name, f":MEASure:ADVanced:P{n} {'ON' if state else 'OFF'}")
    return None


def measure_advanced_p_source1(resource_name: str, n: int, source: str | None = None) -> str | None:
    """Set or query advanced measurement item ``n`` source A.

    SCPI: :MEASure:ADVanced:P<n>:SOURce1 <source>

        Configures source A for advanced measurement item ``n``.
        <source>:= {C<n>|Z<n>|F<x>|ZF<x>|M<m>|ZM<m>|D<d>|ZD<d>|REF<r>}

    Args:
        n: Measurement item index (1-12)
        source: Source identifier (e.g. "C1", "F1")

    Returns:
        Current source when querying.
    """
    if source is None:
        return _query(resource_name, f":MEASure:ADVanced:P{n}:SOURce1?")
    _send(resource_name, f":MEASure:ADVanced:P{n}:SOURce1 {source}")
    return None


def measure_advanced_p_source2(resource_name: str, n: int, source: str | None = None) -> str | None:
    """Set or query advanced measurement item ``n`` source B (for delay measurements).

    SCPI: :MEASure:ADVanced:P<n>:SOURce2 <source>

        Configures source B for advanced measurement item ``n``. Required for delay-type measurements.
        <source>:= {C<n>|F<x>}

    Args:
        n: Measurement item index (1-12)
        source: Source identifier (e.g. "C2")

    Returns:
        Current source when querying.
    """
    if source is None:
        return _query(resource_name, f":MEASure:ADVanced:P{n}:SOURce2?")
    _send(resource_name, f":MEASure:ADVanced:P{n}:SOURce2 {source}")
    return None


def measure_advanced_p_type(resource_name: str, n: int, measure_type: str | None = None) -> str | None:
    """Set or query the measurement type for advanced measurement item ``n``.

    SCPI: :MEASure:ADVanced:P<n>:TYPE <type>

        Configures the measurement type for advanced measurement item ``n``.
        Common types: PKPK, MAX, MIN, AMPLitude, MEAN, RMS, PERiod,
        FREQuency, RISetime, FALLtime, WIDTh, DUTY, OVERSHOOT,
        PRESHOOT, DELAY, DTIMe1-4, etc.
        See the measurement parameter table for the full list.

    Args:
        n: Measurement item index (1-12)
        measure_type: Measurement type (e.g. "PKPK", "RMS", "FREQ")

    Returns:
        Current measurement type when querying.
    """
    if measure_type is None:
        return _query(resource_name, f":MEASure:ADVanced:P{n}:TYPE?")
    _send(resource_name, f":MEASure:ADVanced:P{n}:TYPE {measure_type}")
    return None


def measure_advanced_p_value(resource_name: str, n: int) -> str:
    """Query the measurement value for advanced measurement item ``n``.

    SCPI: :MEASure:ADVanced:P<n>:VALue?

        Queries the measurement value for advanced measurement item ``n``.

    Args:
        n: Measurement item index (1-12)

    Returns:
        Measurement value in NR3 format.
    """
    return _query(resource_name, f":MEASure:ADVanced:P{n}:VALue?")


def measure_advanced_statistics(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query the advanced measurement statistics on/off state.

    SCPI: :MEASure:ADVanced:STATistics {ON|OFF}
           :MEASure:ADVanced:STATistics?

        Configures the advanced measurement statistics on/off state.

    Args:
        state: True=ON, False=OFF

    Returns:
        "ON" or "OFF" when querying.
    """
    if state is None:
        return _query(resource_name, ":MEASure:ADVanced:STATistics?")
    _send(resource_name, f":MEASure:ADVanced:STATistics {'ON' if state else 'OFF'}")
    return None


def measure_advanced_statistics_reset(resource_name: str) -> None:
    """Reset all advanced measurement statistics.

    SCPI: :MEASure:ADVanced:STATistics:RESet

        Resets all advanced measurement statistics.
    """
    _send(resource_name, ":MEASure:ADVanced:STATistics:RESet")


def measure_simple_clear(resource_name: str) -> None:
    """Clear all simple measurement items.

    SCPI: :MEASure:SIMPle:CLEar

        Clears all simple measurement items.
    """
    _send(resource_name, ":MEASure:SIMPle:CLEar")


def measure_simple_item(resource_name: str, item: str | None = None) -> str | None:
    """Set or query the simple measurement item type.

    SCPI: :MEASure:SIMPle:ITEM <item>
           :MEASure:SIMPle:ITEM?

        Configures the simple measurement item type.

    Args:
        item: Measurement type, comma-separated if multiple (e.g. "PKPK,PER,FREQ")
        None — query

    Returns:
        Current measurement items string when querying.
    """
    if item is None:
        return _query(resource_name, ":MEASure:SIMPle:ITEM?")
    _send(resource_name, f":MEASure:SIMPle:ITEM {item}")
    return None


def measure_simple_source(resource_name: str, source: str | None = None) -> str | None:
    """Set or query the simple measurement source.

    SCPI: :MEASure:SIMPle:SOURce <source>
           :MEASure:SIMPle:SOURce?

        Configures the source for simple measurements.
        <source>:= {C<n>|F<x>|M<m>|REF<r>}

    Args:
        source: Source identifier (e.g. "C1")

    Returns:
        Current source when querying.
    """
    if source is None:
        return _query(resource_name, ":MEASure:SIMPle:SOURce?")
    _send(resource_name, f":MEASure:SIMPle:SOURce {source}")
    return None


def measure_gate(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query the measurement gate on/off state.

    SCPI: :MEASure:GATE {ON|OFF}
           :MEASure:GATE?

        Configures the measurement gate on/off state.

    Args:
        state: True=ON, False=OFF

    Returns:
        "ON" or "OFF" when querying.
    """
    if state is None:
        return _query(resource_name, ":MEASure:GATE?")
    _send(resource_name, f":MEASure:GATE {'ON' if state else 'OFF'}")
    return None


def measure_gate_gA(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the measurement gate A position (left boundary).

    SCPI: :MEASure:GATE:GA <value>
           :MEASure:GATE:GA?

        Configures measurement gate A position (left boundary).

    Args:
        value: Gate A position in seconds (NR3)

    Returns:
        Current gate A position when querying.
    """
    if value is None:
        return _query(resource_name, ":MEASure:GATE:GA?")
    _send(resource_name, f":MEASure:GATE:GA {value}")
    return None


def measure_gate_gB(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the measurement gate B position (right boundary).

    SCPI: :MEASure:GATE:GB <value>
           :MEASure:GATE:GB?

        Configures measurement gate B position (right boundary).

    Args:
        value: Gate B position in seconds (NR3)

    Returns:
        Current gate B position when querying.
    """
    if value is None:
        return _query(resource_name, ":MEASure:GATE:GB?")
    _send(resource_name, f":MEASure:GATE:GB {value}")
    return None


def measure_astrategy(resource_name: str, strategy: str | None = None) -> str | None:
    """Set or query the amplitude measurement strategy.

    SCPI: :MEASure:ASTRategy <strategy>
           :MEASure:ASTRategy?

        Configures the amplitude measurement strategy.
        AUTO  — automatic selection
        MANual — manual selection

    Args:
        strategy: {AUTO|MANual}

    Returns:
        Current strategy when querying.
    """
    if strategy is None:
        return _query(resource_name, ":MEASure:ASTRategy?")
    _send(resource_name, f":MEASure:ASTRategy {strategy}")
    return None


def measure_threshold_source(resource_name: str, source: str | None = None) -> str | None:
    """Set or query the measurement threshold source.

    SCPI: :MEASure:THReshold:SOURce <source>
           :MEASure:THReshold:SOURce?

        Configures the measurement threshold source.
        <source>:= {C<n>|F<x>|M<m>|REF<r>}

    Args:
        source: Source identifier (e.g. "C1")

    Returns:
        Current threshold source when querying.
    """
    if source is None:
        return _query(resource_name, ":MEASure:THReshold:SOURce?")
    _send(resource_name, f":MEASure:THReshold:SOURce {source}")
    return None


def measure_threshold_type(resource_name: str, thresh_type: str | None = None) -> str | None:
    """Set or query the measurement threshold type.

    SCPI: :MEASure:THReshold:TYPE <type>
           :MEASure:THReshold:TYPE?

        Configures the measurement threshold type.
        ABSolute — absolute voltage thresholds
        PERCent  — percentage-based thresholds

    Args:
        thresh_type: {ABSolute|PERCent}

    Returns:
        Current threshold type when querying.
    """
    if thresh_type is None:
        return _query(resource_name, ":MEASure:THReshold:TYPE?")
    _send(resource_name, f":MEASure:THReshold:TYPE {thresh_type}")
    return None


def measure_threshold_absolute(resource_name: str, thresholds: str | None = None) -> str | None:
    """Set or query the absolute measurement thresholds.

    SCPI: :MEASure:THReshold:ABSolute <low>,<mid>,<high>
           :MEASure:THReshold:ABSolute?

        Configures the absolute measurement thresholds.
        Format: <high>,<mid>,<low> (volts)

    Args:
        thresholds: Comma-separated low,mid,high values (e.g. "0.5,1.5,2.5")

    Returns:
        Current absolute thresholds when querying.
    """
    if thresholds is None:
        return _query(resource_name, ":MEASure:THReshold:ABSolute?")
    _send(resource_name, f":MEASure:THReshold:ABSolute {thresholds}")
    return None


def measure_threshold_percent(resource_name: str, thresholds: str | None = None) -> str | None:
    """Set or query the percentage measurement thresholds.

    SCPI: :MEASure:THReshold:PERCent <low>,<mid>,<high>
           :MEASure:THReshold:PERCent?

        Configures the percentage measurement thresholds.
        Format: <high>,<mid>,<low> (0-100%)

    Args:
        thresholds: Comma-separated low,mid,high percentages (e.g. "10,50,90")

    Returns:
        Current percentage thresholds when querying.
    """
    if thresholds is None:
        return _query(resource_name, ":MEASure:THReshold:PERCent?")
    _send(resource_name, f":MEASure:THReshold:PERCent {thresholds}")
    return None


def measure_rdisplay(resource_name: str, mode: str | None = None) -> str | None:
    """Set or query the measurement result display style.

    SCPI: :MEASure:RDISplay <style>
           :MEASure:RDISplay?

        Configures the measurement result display style.

    Args:
        mode: Display style

    Returns:
        Current display style when querying.
    """
    if mode is None:
        return _query(resource_name, ":MEASure:RDISplay?")
    _send(resource_name, f":MEASure:RDISplay {mode}")
    return None


def measure_advanced_style(resource_name: str, style: str | None = None) -> str | None:
    """Set or query the advanced measurement display style.

    SCPI: :MEASure:ADVanced:STYLe <type>
           :MEASure:ADVanced:STYLe?

        Configures the advanced measurement display style.
        M1 — simple measurement display style
        M2 — advanced measurement display style

    Args:
        style: {M1|M2}

    Returns:
        Current style when querying.
    """
    if style is None:
        return _query(resource_name, ":MEASure:ADVanced:STYLe?")
    _send(resource_name, f":MEASure:ADVanced:STYLe {style}")
    return None


def measure_advanced_p_statistics_value(resource_name: str, n: int, stat_type: str) -> str:
    """Query the statistics value for advanced measurement item ``n``.

    SCPI: :MEASure:ADVanced:P<n>:STATistics? <type>

        Queries the statistics value for advanced measurement item ``n``.

    Args:
        n: Measurement item index (1-12)
        stat_type: {ALL|CURRent|MEAN|MAXimum|MINimum|STDev|COUNt}

    Returns:
        Statistics value.
    """
    return _query(resource_name, f":MEASure:ADVanced:P{n}:STATistics? {stat_type}")


def measure_advanced_p_shistory(resource_name: str, n: int, count: int | None = None) -> str:
    """Query the statistics history for advanced measurement item ``n``.

    SCPI: :MEASure:ADVanced:P<n>:SHIStory? [<count>]

        Queries the statistics history for advanced measurement item ``n``.

    Args:
        n: Measurement item index (1-12)
        count: Number of history entries (optional)

    Returns:
        History data.
    """
    if count is None:
        return _query(resource_name, f":MEASure:ADVanced:P{n}:SHIStory?")
    return _query(resource_name, f":MEASure:ADVanced:P{n}:SHIStory? {count}")


def measure_advanced_statistics_aimlimit(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query the AIM limit statistics setting.

    SCPI: :MEASure:ADVanced:STATistics:AIMLimit {ON|OFF}
           :MEASure:ADVanced:STATistics:AIMLimit?

        Configures the AIM limit statistics feature.

    Args:
        state: True=ON, False=OFF

    Returns:
        "ON" or "OFF" when querying.
    """
    if state is None:
        return _query(resource_name, ":MEASure:ADVanced:STATistics:AIMLimit?")
    _send(resource_name, f":MEASure:ADVanced:STATistics:AIMLimit {'ON' if state else 'OFF'}")
    return None


def measure_advanced_statistics_histogram(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query the histogram statistics setting.

    SCPI: :MEASure:ADVanced:STATistics:HISTOGram {ON|OFF}
           :MEASure:ADVanced:STATistics:HISTOGram?

        Configures the histogram statistics feature.

    Args:
        state: True=ON, False=OFF

    Returns:
        "ON" or "OFF" when querying.
    """
    if state is None:
        return _query(resource_name, ":MEASure:ADVanced:STATistics:HISTOGram?")
    _send(resource_name, f":MEASure:ADVanced:STATistics:HISTOGram {'ON' if state else 'OFF'}")
    return None


def measure_advanced_statistics_maxcount(resource_name: str, count: int | None = None) -> str | None:
    """Set or query the maximum statistics count.

    SCPI: :MEASure:ADVanced:STATistics:MAXCount <value>
           :MEASure:ADVanced:STATistics:MAXCount?

        Configures the maximum statistics count value.

    Args:
        count: Maximum count value

    Returns:
        Current max count when querying.
    """
    if count is None:
        return _query(resource_name, ":MEASure:ADVanced:STATistics:MAXCount?")
    _send(resource_name, f":MEASure:ADVanced:STATistics:MAXCount {count}")
    return None


def measure_astrategy_base(resource_name: str, strategy: str | None = None) -> str | None:
    """Set or query the base measurement strategy.

    SCPI: :MEASure:ASTRategy:BASE <value>
           :MEASure:ASTRategy:BASE?

        Configures the base (bottom) amplitude measurement strategy.

    Args:
        strategy: {HISTogram|MIN}

    Returns:
        Current strategy when querying.
    """
    if strategy is None:
        return _query(resource_name, ":MEASure:ASTRategy:BASE?")
    _send(resource_name, f":MEASure:ASTRategy:BASE {strategy}")
    return None


def measure_astrategy_top(resource_name: str, strategy: str | None = None) -> str | None:
    """Set or query the top measurement strategy.

    SCPI: :MEASure:ASTRategy:TOP <value>
           :MEASure:ASTRategy:TOP?

        Configures the top amplitude measurement strategy.

    Args:
        strategy: {HISTogram|MAX}

    Returns:
        Current strategy when querying.
    """
    if strategy is None:
        return _query(resource_name, ":MEASure:ASTRategy:TOP?")
    _send(resource_name, f":MEASure:ASTRategy:TOP {strategy}")
    return None


def measure_simple_value(resource_name: str, measure_type: str) -> str:
    """Query the simple measurement value.

    SCPI: :MEASure:SIMPle:VALue? <type>

        Queries the simple measurement value.

    Args:
        measure_type: Measurement type (e.g. "PKPK", "RMS", "FREQ")

    Returns:
        Measurement value.
    """
    return _query(resource_name, f":MEASure:SIMPle:VALue? {measure_type}")


# ═══════════════════════════════════════════════════════════════════
#  DTIMe (delay-time) measurement settings
# ═══════════════════════════════════════════════════════════════════

def measure_dtime_edge1(resource_name: str, idx: int, val: int) -> None:
    """Set DTIMe edge1 number.

    SCPI: :MEASure:ADVanced:DTIMe<idx>:EDGe1 <val>
    """
    _send(resource_name, f":MEASure:ADVanced:DTIMe{idx}:EDGe1 {val}")


def measure_dtime_edge2(resource_name: str, idx: int, val: int) -> None:
    """Set DTIMe edge2 number.

    SCPI: :MEASure:ADVanced:DTIMe<idx>:EDGe2 <val>
    """
    _send(resource_name, f":MEASure:ADVanced:DTIMe{idx}:EDGe2 {val}")


def measure_dtime_slope1(resource_name: str, idx: int, val: str) -> None:
    """Set DTIMe slope1.

    SCPI: :MEASure:ADVanced:DTIMe<idx>:SLOPe1 {RISing|FALLing}
    """
    _send(resource_name, f":MEASure:ADVanced:DTIMe{idx}:SLOPe1 {val}")


def measure_dtime_slope2(resource_name: str, idx: int, val: str) -> None:
    """Set DTIMe slope2.

    SCPI: :MEASure:ADVanced:DTIMe<idx>:SLOPe2 {RISing|FALLing}
    """
    _send(resource_name, f":MEASure:ADVanced:DTIMe{idx}:SLOPe2 {val}")


def measure_dtime_threshold1(resource_name: str, idx: int, val: float) -> None:
    """Set DTIMe threshold1 (0-100%).

    SCPI: :MEASure:ADVanced:DTIMe<idx>:THReshold1 <val>
    """
    _send(resource_name, f":MEASure:ADVanced:DTIMe{idx}:THReshold1 {val}")


def measure_dtime_threshold2(resource_name: str, idx: int, val: float) -> None:
    """Set DTIMe threshold2 (0-100%).

    SCPI: :MEASure:ADVanced:DTIMe<idx>:THReshold2 <val>
    """
    _send(resource_name, f":MEASure:ADVanced:DTIMe{idx}:THReshold2 {val}")
