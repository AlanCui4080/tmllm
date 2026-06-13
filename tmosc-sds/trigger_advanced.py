"""TRIGger advanced type SCPI commands (DELay, DROPout, INTerval, NEDGe, etc.)."""

from __future__ import annotations

from _base import _send, _query


# ═══════════════════════════════════════════════════════════════════
#  TRIGger:DELay — Delay Trigger
# ═══════════════════════════════════════════════════════════════════

def trigger_delay_source_a(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the delay trigger source A logic state.

    SCPI: :TRIGger:DELay:INPut <value>
           :TRIGger:DELay:INPut?

        Configures the delay trigger source A logic state. Parameters are configured in order C1 through C<n>, then D0 through D15.

    Args:
        value: {X|L|H}
            X — don't care
            H — active high
            L — active low

    Returns:
        Current source A state when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:DELay:INPut?")
    _send(resource_name, f":TRIGger:DELay:INPut {value}")
    return None


def trigger_delay_source_b(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the delay trigger source B channel.

    SCPI: :TRIGger:DELay:SOURce2 <value>
           :TRIGger:DELay:SOURce2?

        Configures the delay trigger source B channel.

    Args:
        value: {C<n>|D<d>}

    Returns:
        Current source B when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:DELay:SOURce2?")
    _send(resource_name, f":TRIGger:DELay:SOURce2 {value}")
    return None


def trigger_delay_slope_a(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the delay trigger source A slope type.

    SCPI: :TRIGger:DELay:SLOPe <value>
           :TRIGger:DELay:SLOPe?

        Configures the delay trigger source A slope type.

    Args:
        value: {RISing|FALLing}

    Returns:
        Current slope A when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:DELay:SLOPe?")
    _send(resource_name, f":TRIGger:DELay:SLOPe {value}")
    return None


def trigger_delay_slope_b(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the delay trigger source B slope type.

    SCPI: :TRIGger:DELay:SLOPe2 <value>
           :TRIGger:DELay:SLOPe2?

        Configures the delay trigger source B slope type.

    Args:
        value: {RISing|FALLing}

    Returns:
        Current slope B when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:DELay:SLOPe2?")
    _send(resource_name, f":TRIGger:DELay:SLOPe2 {value}")
    return None


def trigger_delay_level_a(resource_name: str, source: str, value: float | None = None) -> str | None:
    """Set or query the delay trigger source A level.

    SCPI: :TRIGger:DELay:LEVel <source>,<value>
           :TRIGger:DELay:LEVel?

        Configures the delay trigger source A level. Range varies by model (same as :TRIGger:EDGE:LEVel).

    Args:
        source: Source channel, {C<n>|D<d>}
        value: Trigger level in volts (NR3)

    Returns:
        Current level A when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:DELay:LEVel?")
    _send(resource_name, f":TRIGger:DELay:LEVel {source},{value}")
    return None


def trigger_delay_level_b(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the delay trigger source B level.

    SCPI: :TRIGger:DELay:LEVel2 <value>
           :TRIGger:DELay:LEVel2?

        Configures the delay trigger source B level.

    Args:
        value: Trigger level in volts (NR3)

    Returns:
        Current level B when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:DELay:LEVel2?")
    _send(resource_name, f":TRIGger:DELay:LEVel2 {value}")
    return None


# ═══════════════════════════════════════════════════════════════════
#  TRIGger:DROPout — Dropout Trigger
# ═══════════════════════════════════════════════════════════════════

def trigger_dropout_time(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the dropout trigger timeout duration.

    SCPI: :TRIGger:DROPout:TIME <value>
           :TRIGger:DROPout:TIME?

        Configures the dropout trigger timeout duration.

    Args:
        value: Timeout duration in seconds (NR3, range depends on model)

    Returns:
        Current timeout value when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:DROPout:TIME?")
    _send(resource_name, f":TRIGger:DROPout:TIME {value}")
    return None


def trigger_dropout_type(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the dropout trigger type.

    SCPI: :TRIGger:DROPout:TYPe <value>
           :TRIGger:DROPout:TYPe?

        Configures the dropout trigger type.

    Args:
        value: {EDGE|STATe}
            EDGE  — edge timeout
            STATe — state timeout

    Returns:
        Current dropout type when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:DROPout:TYPe?")
    _send(resource_name, f":TRIGger:DROPout:TYPe {value}")
    return None


# ═══════════════════════════════════════════════════════════════════
#  TRIGger:INTerval — Interval Trigger
# ═══════════════════════════════════════════════════════════════════

def trigger_interval_level(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the interval trigger level.

    SCPI: :TRIGger:INTerval:LEVel <value>
           :TRIGger:INTerval:LEVel?

        Configures the interval trigger level.

    Args:
        value: Trigger level in volts (NR3)

    Returns:
        Current level when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:INTerval:LEVel?")
    _send(resource_name, f":TRIGger:INTerval:LEVel {value}")
    return None


def trigger_interval_limit(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the interval trigger limit condition type.

    SCPI: :TRIGger:INTerval:LIMit <value>
           :TRIGger:INTerval:LIMit?

        Configures the interval trigger limit condition type.

    Args:
        value: {LESSthan|GREATerthan|INNer|OUTer}

    Returns:
        Current limit type when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:INTerval:LIMit?")
    _send(resource_name, f":TRIGger:INTerval:LIMit {value}")
    return None


def trigger_interval_tlower(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the interval trigger lower time limit.

    SCPI: :TRIGger:INTerval:TLOWer <value>
           :TRIGger:INTerval:TLOWer?

        Configures the interval trigger lower time limit.

    Args:
        value: Lower time limit in seconds (NR3)

    Returns:
        Current lower limit when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:INTerval:TLOWer?")
    _send(resource_name, f":TRIGger:INTerval:TLOWer {value}")
    return None


def trigger_interval_tupper(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the interval trigger upper time limit.

    SCPI: :TRIGger:INTerval:TUPPer <value>
           :TRIGger:INTerval:TUPPer?

        Configures the interval trigger upper time limit.

    Args:
        value: Upper time limit in seconds (NR3)

    Returns:
        Current upper limit when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:INTerval:TUPPer?")
    _send(resource_name, f":TRIGger:INTerval:TUPPer {value}")
    return None


# ═══════════════════════════════════════════════════════════════════
#  TRIGger:NEDGe — Nth-Edge Trigger
# ═══════════════════════════════════════════════════════════════════

def trigger_nedge_source(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the Nth-edge trigger source.

    SCPI: :TRIGger:NEDGe:SOURce <value>
           :TRIGger:NEDGe:SOURce?

        Configures the Nth-edge trigger source.

    Args:
        value: {C<n>|D<d>}

    Returns:
        Current source when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:NEDGe:SOURce?")
    _send(resource_name, f":TRIGger:NEDGe:SOURce {value}")
    return None


def trigger_nedge_slope(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the Nth-edge trigger slope type.

    SCPI: :TRIGger:NEDGe:SLOPe <value>
           :TRIGger:NEDGe:SLOPe?

        Configures the Nth-edge trigger slope type.

    Args:
        value: {RISing|FALLing}

    Returns:
        Current slope when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:NEDGe:SLOPe?")
    _send(resource_name, f":TRIGger:NEDGe:SLOPe {value}")
    return None


def trigger_nedge_idle(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the Nth-edge trigger idle time.

    SCPI: :TRIGger:NEDGe:IDLE <value>
           :TRIGger:NEDGe:IDLE?

        Configures the Nth-edge trigger idle time.

    Args:
        value: Idle time in seconds, range [8.00E-09, 2.00E+01] (NR3)

    Returns:
        Current idle time when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:NEDGe:IDLE?")
    _send(resource_name, f":TRIGger:NEDGe:IDLE {value}")
    return None


def trigger_nedge_edge(resource_name: str, value: int | None = None) -> str | None:
    """Set or query the Nth-edge trigger edge count.

    SCPI: :TRIGger:NEDGe:EDGE <value>
           :TRIGger:NEDGe:EDGE?

        Configures the Nth-edge trigger edge count.

    Args:
        value: Edge count, range [1, 65535] (NR1)

    Returns:
        Current edge count when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:NEDGe:EDGE?")
    _send(resource_name, f":TRIGger:NEDGe:EDGE {value}")
    return None


def trigger_nedge_level(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the Nth-edge trigger level.

    SCPI: :TRIGger:NEDGe:LEVel <value>
           :TRIGger:NEDGe:LEVel?

        Configures the Nth-edge trigger level.

    Args:
        value: Trigger level in volts (NR3)

    Returns:
        Current level when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:NEDGe:LEVel?")
    _send(resource_name, f":TRIGger:NEDGe:LEVel {value}")
    return None


# ═══════════════════════════════════════════════════════════════════
#  TRIGger:PATTern — Pattern Trigger
# ═══════════════════════════════════════════════════════════════════

def trigger_pattern_input(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the pattern trigger source logic states.

    SCPI: :TRIGger:PATTern:INPut <value>
           :TRIGger:PATTern:INPut?

        Configures the pattern trigger source logic states. Parameters are configured in order C1 through C<n>, then D0 through D15.

    Args:
        value: Logic states string (e.g. "X,H,L")
            X — don't care / inactive
            H — active high
            L — active low

    Returns:
        Current input pattern when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:PATTern:INPut?")
    _send(resource_name, f":TRIGger:PATTern:INPut {value}")
    return None


def trigger_pattern_level(resource_name: str, source: str, value: float | None = None) -> str | None:
    """Set or query the pattern trigger logic level.

    SCPI: :TRIGger:PATTern:LEVel <source>,<value>
           :TRIGger:PATTern:LEVel?

        Configures the pattern trigger source logic level.

    Args:
        source: Source channel, {C<n>|D<d>}
        value: Trigger level in volts (NR3)

    Returns:
        Current level when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:PATTern:LEVel?")
    _send(resource_name, f":TRIGger:PATTern:LEVel {source},{value}")
    return None


def trigger_pattern_limit(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the pattern trigger limit condition type.

    SCPI: :TRIGger:PATTern:LIMit <value>
           :TRIGger:PATTern:LIMit?

        Configures the pattern trigger limit condition type.

    Args:
        value: {LESSthan|GREATerthan|INNer|OUTer}

    Returns:
        Current limit type when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:PATTern:LIMit?")
    _send(resource_name, f":TRIGger:PATTern:LIMit {value}")
    return None


def trigger_pattern_logic(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the pattern trigger logic relationship.

    SCPI: :TRIGger:PATTern:LOGic <value>
           :TRIGger:PATTern:LOGic?

        Configures the pattern trigger logic relationship.

    Args:
        value: {AND|OR|NAND|NOR}

    Returns:
        Current logic when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:PATTern:LOGic?")
    _send(resource_name, f":TRIGger:PATTern:LOGic {value}")
    return None


def trigger_pattern_tlower(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the pattern trigger lower time limit.

    SCPI: :TRIGger:PATTern:TLOWer <value>
           :TRIGger:PATTern:TLOWer?

        Configures the pattern trigger lower time limit.

    Args:
        value: Lower time limit in seconds (NR3)

    Returns:
        Current lower limit when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:PATTern:TLOWer?")
    _send(resource_name, f":TRIGger:PATTern:TLOWer {value}")
    return None


def trigger_pattern_tupper(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the pattern trigger upper time limit.

    SCPI: :TRIGger:PATTern:TUPPer <value>
           :TRIGger:PATTern:TUPPer?

        Configures the pattern trigger upper time limit.

    Args:
        value: Upper time limit in seconds (NR3)

    Returns:
        Current upper limit when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:PATTern:TUPPer?")
    _send(resource_name, f":TRIGger:PATTern:TUPPer {value}")
    return None


# ═══════════════════════════════════════════════════════════════════
#  TRIGger:PULSe — Pulse Width Trigger
# ═══════════════════════════════════════════════════════════════════

def trigger_pulse_polarity(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the pulse width trigger polarity.

    SCPI: :TRIGger:PULSe:POLarity <value>
           :TRIGger:PULSe:POLarity?

        Configures the pulse width trigger polarity.

    Args:
        value: {POSitive|NEGative}

    Returns:
        Current polarity when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:PULSe:POLarity?")
    _send(resource_name, f":TRIGger:PULSe:POLarity {value}")
    return None


def trigger_pulse_limit(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the pulse width trigger limit condition type.

    SCPI: :TRIGger:PULSe:LIMit <value>
           :TRIGger:PULSe:LIMit?

        Configures the pulse width trigger limit condition type.

    Args:
        value: {LESSthan|GREATerthan|INNer|OUTer}

    Returns:
        Current limit type when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:PULSe:LIMit?")
    _send(resource_name, f":TRIGger:PULSe:LIMit {value}")
    return None


def trigger_pulse_tlower(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the pulse width trigger lower time limit.

    SCPI: :TRIGger:PULSe:TLOWer <value>
           :TRIGger:PULSe:TLOWer?

        Configures the pulse width trigger lower time limit.

    Args:
        value: Lower time limit in seconds (NR3)

    Returns:
        Current lower limit when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:PULSe:TLOWer?")
    _send(resource_name, f":TRIGger:PULSe:TLOWer {value}")
    return None


def trigger_pulse_tupper(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the pulse width trigger upper time limit.

    SCPI: :TRIGger:PULSe:TUPPer <value>
           :TRIGger:PULSe:TUPPer?

        Configures the pulse width trigger upper time limit.

    Args:
        value: Upper time limit in seconds (NR3)

    Returns:
        Current upper limit when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:PULSe:TUPPer?")
    _send(resource_name, f":TRIGger:PULSe:TUPPer {value}")
    return None


# ═══════════════════════════════════════════════════════════════════
#  TRIGger:QUALified — Qualified Trigger
# ═══════════════════════════════════════════════════════════════════

def trigger_qualified_source(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the qualified trigger qualifying signal source.

    SCPI: :TRIGger:QUALified:QSource <value>
           :TRIGger:QUALified:QSource?

        Configures the qualified trigger qualifying signal source.

    Args:
        value: {C<n>|D<d>}

    Returns:
        Current qualified source when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:QUALified:QSource?")
    _send(resource_name, f":TRIGger:QUALified:QSource {value}")
    return None


def trigger_qualified_edge_source(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the qualified trigger edge source.

    SCPI: :TRIGger:QUALified:ESource <value>
           :TRIGger:QUALified:ESource?

        Configures the qualified trigger edge signal source.

    Args:
        value: {C<n>|D<d>}

    Returns:
        Current edge source when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:QUALified:ESource?")
    _send(resource_name, f":TRIGger:QUALified:ESource {value}")
    return None


def trigger_qualified_type(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the qualified trigger type.

    SCPI: :TRIGger:QUALified:TYPe <value>
           :TRIGger:QUALified:TYPe?

        Configures the qualified trigger type.

    Args:
        value: {STATe|STATE_DLY|EDGE|EDGE_DLY}[,{LOW|HIGH|RISing|FALLing}]

    Returns:
        Current qualified type when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:QUALified:TYPe?")
    _send(resource_name, f":TRIGger:QUALified:TYPe {value}")
    return None


def trigger_qualified_lower_time(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the qualified trigger lower time limit.

    SCPI: :TRIGger:QUALified:TLOWer <value>
           :TRIGger:QUALified:TLOWer?

        Configures the qualified trigger lower time limit. Effective only when the qualified type is "level and timed" or "edge and timed".

    Args:
        value: Lower time limit in seconds (NR3)

    Returns:
        Current lower limit when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:QUALified:TLOWer?")
    _send(resource_name, f":TRIGger:QUALified:TLOWer {value}")
    return None


def trigger_qualified_upper_time(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the qualified trigger upper time limit.

    SCPI: :TRIGger:QUALified:TUPPer <value>
           :TRIGger:QUALified:TUPPer?

        Configures the qualified trigger upper time limit. Effective only when the qualified type is "level and timed" or "edge and timed".

    Args:
        value: Upper time limit in seconds (NR3)

    Returns:
        Current upper limit when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:QUALified:TUPPer?")
    _send(resource_name, f":TRIGger:QUALified:TUPPer {value}")
    return None


# ═══════════════════════════════════════════════════════════════════
#  TRIGger:RUNT — Runt Trigger
# ═══════════════════════════════════════════════════════════════════

def trigger_runt_hlevel(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the runt trigger high level.

    SCPI: :TRIGger:RUNT:HLEVel <value>
           :TRIGger:RUNT:HLEVel?

        Configures the runt trigger high level. High level must not be less than low level.

    Args:
        value: High level in volts (NR3)

    Returns:
        Current high level when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:RUNT:HLEVel?")
    _send(resource_name, f":TRIGger:RUNT:HLEVel {value}")
    return None


def trigger_runt_llevel(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the runt trigger low level.

    SCPI: :TRIGger:RUNT:LLEVel <value>
           :TRIGger:RUNT:LLEVel?

        Configures the runt trigger low level. Low level must not be greater than high level.

    Args:
        value: Low level in volts (NR3)

    Returns:
        Current low level when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:RUNT:LLEVel?")
    _send(resource_name, f":TRIGger:RUNT:LLEVel {value}")
    return None


def trigger_runt_limit(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the runt trigger limit condition type.

    SCPI: :TRIGger:RUNT:LIMit <value>
           :TRIGger:RUNT:LIMit?

        Configures the runt trigger limit condition type.

    Args:
        value: {LESSthan|GREATerthan|INNer|OUTer}

    Returns:
        Current limit type when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:RUNT:LIMit?")
    _send(resource_name, f":TRIGger:RUNT:LIMit {value}")
    return None


def trigger_runt_polarity(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the runt trigger polarity.

    SCPI: :TRIGger:RUNT:POLarity <value>
           :TRIGger:RUNT:POLarity?

        Configures the runt trigger polarity.

    Args:
        value: {POSitive|NEGative}

    Returns:
        Current polarity when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:RUNT:POLarity?")
    _send(resource_name, f":TRIGger:RUNT:POLarity {value}")
    return None


def trigger_runt_tlower(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the runt trigger lower time limit.

    SCPI: :TRIGger:RUNT:TLOWer <value>
           :TRIGger:RUNT:TLOWer?

        Configures the runt trigger lower time limit.

    Args:
        value: Lower time limit in seconds (NR3)

    Returns:
        Current lower limit when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:RUNT:TLOWer?")
    _send(resource_name, f":TRIGger:RUNT:TLOWer {value}")
    return None


def trigger_runt_tupper(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the runt trigger upper time limit.

    SCPI: :TRIGger:RUNT:TUPPer <value>
           :TRIGger:RUNT:TUPPer?

        Configures the runt trigger upper time limit.

    Args:
        value: Upper time limit in seconds (NR3)

    Returns:
        Current upper limit when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:RUNT:TUPPer?")
    _send(resource_name, f":TRIGger:RUNT:TUPPer {value}")
    return None


# ═══════════════════════════════════════════════════════════════════
#  TRIGger:SHOLd — Setup/Hold Trigger
# ═══════════════════════════════════════════════════════════════════

def trigger_shold_type(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the setup/hold trigger type.

    SCPI: :TRIGger:SHOLd:TYPe <value>
           :TRIGger:SHOLd:TYPe?

        Configures the setup/hold trigger type.

    Args:
        value: {SETup|HOLD}
            SETup — setup time trigger
            HOLD  — hold time trigger

    Returns:
        Current type when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:SHOLd:TYPe?")
    _send(resource_name, f":TRIGger:SHOLd:TYPe {value}")
    return None


def trigger_shold_clock_source(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the setup/hold trigger clock source.

    SCPI: :TRIGger:SHOLd:CSource <value>
           :TRIGger:SHOLd:CSource?

        Configures the setup/hold trigger clock source.

    Args:
        value: {C<n>|D<d>}

    Returns:
        Current clock source when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:SHOLd:CSource?")
    _send(resource_name, f":TRIGger:SHOLd:CSource {value}")
    return None


def trigger_shold_clock_threshold(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the setup/hold trigger clock threshold.

    SCPI: :TRIGger:SHOLd:CTHReshold <value>
           :TRIGger:SHOLd:CTHReshold?

        Configures the setup/hold trigger clock threshold.

    Args:
        value: Clock threshold level in volts (NR3)

    Returns:
        Current clock threshold when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:SHOLd:CTHReshold?")
    _send(resource_name, f":TRIGger:SHOLd:CTHReshold {value}")
    return None


def trigger_shold_data_source(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the setup/hold trigger data source.

    SCPI: :TRIGger:SHOLd:DSource <value>
           :TRIGger:SHOLd:DSource?

        Configures the setup/hold trigger data source.

    Args:
        value: {C<n>|D<d>}

    Returns:
        Current data source when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:SHOLd:DSource?")
    _send(resource_name, f":TRIGger:SHOLd:DSource {value}")
    return None


def trigger_shold_data_threshold(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the setup/hold trigger data threshold.

    SCPI: :TRIGger:SHOLd:DTHReshold <value>
           :TRIGger:SHOLd:DTHReshold?

        Configures the setup/hold trigger data threshold.

    Args:
        value: Data threshold level in volts (NR3)

    Returns:
        Current data threshold when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:SHOLd:DTHReshold?")
    _send(resource_name, f":TRIGger:SHOLd:DTHReshold {value}")
    return None


def trigger_shold_slope(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the setup/hold trigger slope type.

    SCPI: :TRIGger:SHOLd:SLOPe <value>
           :TRIGger:SHOLd:SLOPe?

        Configures the setup/hold trigger slope type.

    Args:
        value: {RISing|FALLing}

    Returns:
        Current slope when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:SHOLd:SLOPe?")
    _send(resource_name, f":TRIGger:SHOLd:SLOPe {value}")
    return None


# ═══════════════════════════════════════════════════════════════════
#  TRIGger:SLOPe — Slope Trigger
# ═══════════════════════════════════════════════════════════════════

def trigger_slope_hlevel(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the slope trigger high level.

    SCPI: :TRIGger:SLOPe:HLEVel <value>
           :TRIGger:SLOPe:HLEVel?

        Configures the slope trigger high level. High level must not be less than low level.

    Args:
        value: High level in volts (NR3)

    Returns:
        Current high level when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:SLOPe:HLEVel?")
    _send(resource_name, f":TRIGger:SLOPe:HLEVel {value}")
    return None


def trigger_slope_llevel(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the slope trigger low level.

    SCPI: :TRIGger:SLOPe:LLEVel <value>
           :TRIGger:SLOPe:LLEVel?

        Configures the slope trigger low level. Low level must not be greater than high level.

    Args:
        value: Low level in volts (NR3)

    Returns:
        Current low level when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:SLOPe:LLEVel?")
    _send(resource_name, f":TRIGger:SLOPe:LLEVel {value}")
    return None


def trigger_slope_limit(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the slope trigger limit condition type.

    SCPI: :TRIGger:SLOPe:LIMit <value>
           :TRIGger:SLOPe:LIMit?

        Configures the slope trigger limit condition type.

    Args:
        value: {LESSthan|GREATerthan|INNer|OUTer}

    Returns:
        Current limit type when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:SLOPe:LIMit?")
    _send(resource_name, f":TRIGger:SLOPe:LIMit {value}")
    return None


def trigger_slope_slope(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the slope trigger slope type.

    SCPI: :TRIGger:SLOPe:SLOPe <value>
           :TRIGger:SLOPe:SLOPe?

        Configures the slope trigger slope type.

    Args:
        value: {RISing|FALLing}

    Returns:
        Current slope when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:SLOPe:SLOPe?")
    _send(resource_name, f":TRIGger:SLOPe:SLOPe {value}")
    return None


def trigger_slope_tlower(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the slope trigger lower time limit.

    SCPI: :TRIGger:SLOPe:TLOWer <value>
           :TRIGger:SLOPe:TLOWer?

        Configures the slope trigger lower time limit.

    Args:
        value: Lower time limit in seconds (NR3)

    Returns:
        Current lower limit when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:SLOPe:TLOWer?")
    _send(resource_name, f":TRIGger:SLOPe:TLOWer {value}")
    return None


def trigger_slope_tupper(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the slope trigger upper time limit.

    SCPI: :TRIGger:SLOPe:TUPPer <value>
           :TRIGger:SLOPe:TUPPer?

        Configures the slope trigger upper time limit.

    Args:
        value: Upper time limit in seconds (NR3)

    Returns:
        Current upper limit when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:SLOPe:TUPPer?")
    _send(resource_name, f":TRIGger:SLOPe:TUPPer {value}")
    return None


# ═══════════════════════════════════════════════════════════════════
#  TRIGger:VIDeo — Video Trigger
# ═══════════════════════════════════════════════════════════════════

def trigger_video_field(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the video trigger sync field number.

    SCPI: :TRIGger:VIDeo:FIELd <value>
           :TRIGger:VIDeo:FIELd?

        Configures the video trigger sync field number. Effective only when standard is NTSC, PAL, 1080i/50, or 1080i/60.

    Args:
        value: {1|2}

    Returns:
        Current field number when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:VIDeo:FIELd?")
    _send(resource_name, f":TRIGger:VIDeo:FIELd {value}")
    return None


def trigger_video_frame_rate(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the video trigger custom frame rate.

    SCPI: :TRIGger:VIDeo:FRATe <value>
           :TRIGger:VIDeo:FRATe?

        Configures the video trigger frame rate for the custom standard.

    Args:
        value: {25Hz|30Hz|50Hz|60Hz}

    Returns:
        Current frame rate when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:VIDeo:FRATe?")
    _send(resource_name, f":TRIGger:VIDeo:FRATe {value}")
    return None


def trigger_video_interlace(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the video trigger custom interlace ratio.

    SCPI: :TRIGger:VIDeo:INTErlace <value>
           :TRIGger:VIDeo:INTErlace?

        Configures the video trigger interlace ratio for the custom standard.

    Args:
        value: {1|2|4|8}

    Returns:
        Current interlace ratio when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:VIDeo:INTErlace?")
    _send(resource_name, f":TRIGger:VIDeo:INTErlace {value}")
    return None


def trigger_video_line(resource_name: str, value: int | None = None) -> str | None:
    """Set or query the video trigger sync line number (non-custom standard).

    SCPI: :TRIGger:VIDeo:LINE <value>
           :TRIGger:VIDeo:LINE?

        Configures the video trigger sync line number (non-custom standards).

    Args:
        value: Line number (NR1)

    Returns:
        Current line number when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:VIDeo:LINE?")
    _send(resource_name, f":TRIGger:VIDeo:LINE {value}")
    return None


def trigger_video_source(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the video trigger source.

    SCPI: :TRIGger:VIDeo:SOURce <value>
           :TRIGger:VIDeo:SOURce?

        Configures the video trigger source.

    Args:
        value: {C<n>}

    Returns:
        Current source when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:VIDeo:SOURce?")
    _send(resource_name, f":TRIGger:VIDeo:SOURce {value}")
    return None


def trigger_video_standard(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the video trigger standard type.

    SCPI: :TRIGger:VIDeo:STANdard <value>
           :TRIGger:VIDeo:STANdard?

        Configures the video trigger standard type.

    Args:
        value: {NTSC|PAL|P720L50|P720L60|P1080L50|P1080L60|
                I1080L50|I1080L60|CUSTom}

    Returns:
        Current standard when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:VIDeo:STANdard?")
    _send(resource_name, f":TRIGger:VIDeo:STANdard {value}")
    return None


def trigger_video_sync(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the video trigger sync mode.

    SCPI: :TRIGger:VIDeo:SYNC <value>
           :TRIGger:VIDeo:SYNC?

        Configures the video trigger sync mode.

    Args:
        value: {SELect|ANY}
            SELect — selectable field/line
            ANY    — any line

    Returns:
        Current sync mode when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:VIDeo:SYNC?")
    _send(resource_name, f":TRIGger:VIDeo:SYNC {value}")
    return None


# ═══════════════════════════════════════════════════════════════════
#  TRIGger:WINDow — Window Trigger
# ═══════════════════════════════════════════════════════════════════

def trigger_window_center_level(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the window trigger relative center level.

    SCPI: :TRIGger:WINDow:CLEVel <value>
           :TRIGger:WINDow:CLEVel?

        Configures the window trigger relative center level.

    Args:
        value: Center level in volts (NR3)

    Returns:
        Current center level when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:WINDow:CLEVel?")
    _send(resource_name, f":TRIGger:WINDow:CLEVel {value}")
    return None


def trigger_window_delta_level(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the window trigger relative level range (delta).

    SCPI: :TRIGger:WINDow:DLEVel <value>
           :TRIGger:WINDow:DLEVel?

        Configures the window trigger relative level range (delta).

    Args:
        value: Delta level range in volts (NR3)

    Returns:
        Current delta level when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:WINDow:DLEVel?")
    _send(resource_name, f":TRIGger:WINDow:DLEVel {value}")
    return None


def trigger_window_high_level(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the window trigger absolute high level.

    SCPI: :TRIGger:WINDow:HLEVel <value>
           :TRIGger:WINDow:HLEVel?

        Configures the window trigger absolute high level. High level must not be less than low level.

    Args:
        value: High level in volts (NR3)

    Returns:
        Current high level when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:WINDow:HLEVel?")
    _send(resource_name, f":TRIGger:WINDow:HLEVel {value}")
    return None


def trigger_window_low_level(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the window trigger absolute low level.

    SCPI: :TRIGger:WINDow:LLEVel <value>
           :TRIGger:WINDow:LLEVel?

        Configures the window trigger absolute low level. Low level must not be greater than high level.

    Args:
        value: Low level in volts (NR3)

    Returns:
        Current low level when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:WINDow:LLEVel?")
    _send(resource_name, f":TRIGger:WINDow:LLEVel {value}")
    return None


def trigger_window_type(resource_name: str, value: str | None = None) -> str | None:
    """Set or query the window trigger type.

    SCPI: :TRIGger:WINDow:TYPe <value>
           :TRIGger:WINDow:TYPe?

        Configures the window trigger type.
        ABSolute — absolute window: high and low levels adjustable independently
        RELative — relative window: high and low levels move together

    Args:
        value: {ABSolute|RELative}
            ABSolute — absolute window: high and low levels adjustable independently
            RELative — relative window: high and low levels move together

    Returns:
        Current window type when querying.
    """
    if value is None:
        return _query(resource_name, ":TRIGger:WINDow:TYPe?")
    _send(resource_name, f":TRIGger:WINDow:TYPe {value}")
    return None
