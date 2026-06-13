"""TRIGger subsystem SCPI commands (common + EDGE)."""

from __future__ import annotations
from _base import _send, _query


def trigger_mode(resource_name: str, mode: str | None = None) -> str | None:
    """Set or query the trigger mode.

    SCPI: :TRIGger:MODE <mode>
           :TRIGger:MODE?

        Configures the trigger mode.
        SINGle — single: captures one frame when trigger condition is met, then stops
        NORMal — normal: only acquires when trigger condition is met
        AUTO   — auto: forces an acquisition after the timeout period if no trigger occurs
        FTRIG  — force: forces a single acquisition regardless of trigger condition

    Args:
        mode: {SINGle|NORMal|AUTO|FTRIG}

    Returns:
        Current trigger mode when querying.
    """
    if mode is None:
        return _query(resource_name, ":TRIGger:MODE?")
    _send(resource_name, f":TRIGger:MODE {mode}")
    return None


def trigger_run(resource_name: str) -> None:
    """Set oscilloscope to Run state, keeping current trigger mode.

    SCPI: :TRIGger:RUN

        Sets the oscilloscope to Run state while preserving the current trigger mode.

    Associated commands: :TRIGger:STOP
    """
    _send(resource_name, ":TRIGger:RUN")


def trigger_status(resource_name: str) -> str:
    """Query the current trigger status.

    SCPI: :TRIGger:STATus?

        Queries the current trigger status.
        {Arm|Ready|Auto|Trig'd|Stop|Roll}

    Returns:
        Current status string.

    Associated commands: :TRIGger:MODE
    """
    return _query(resource_name, ":TRIGger:STATus?")


def trigger_stop(resource_name: str) -> None:
    """Set oscilloscope to Stop state (equivalent to front panel Stop button).

    SCPI: :TRIGger:STOP

        Sets the oscilloscope to Stop state. Equivalent to the front-panel Run/Stop button.

    Associated commands: :TRIGger:RUN
    """
    _send(resource_name, ":TRIGger:STOP")


def trigger_type(resource_name: str, trig_type: str | None = None) -> str | None:
    """Set or query the trigger type.

    SCPI: :TRIGger:TYPE <type>
           :TRIGger:TYPE?

        Configures the trigger type.
        {EDGE|PULSE|SLOPe|INTerval|PATTern|RUNT|WINDow|DROPout|VIDeo|QUALified|NEDGe|DELay|SHOLd|IIC|SPI|UART|LIN|CAN|FLEXray|CANFd|IIS|M1553|SENT|A429}

    Args:
        trig_type: Trigger type (e.g. "EDGE", "PULSE")

    Returns:
        Current trigger type when querying.
    """
    if trig_type is None:
        return _query(resource_name, ":TRIGger:TYPE?")
    _send(resource_name, f":TRIGger:TYPE {trig_type}")
    return None


def trigger_frequency(resource_name: str) -> str:
    """Query the hardware frequency counter value.

    SCPI: :TRIGger:FREQuency?

        Queries the hardware frequency counter. Returns the frequency in Hz when a valid reading is available. Default precision is 3 digits; up to 7 digits with :FORMat:DATA.

    Returns:
        Frequency in Hz (NR3, e.g. "1.234561E+04").

    Associated commands: :FORMat:DATA
    """
    return _query(resource_name, ":TRIGger:FREQuency?")


def trigger_edge_coupling(resource_name: str, coupling: str | None = None) -> str | None:
    """Set or query the edge trigger coupling mode.

    SCPI: :TRIGger:EDGE:COUPling <mode>
           :TRIGger:EDGE:COUPling?

        Configures the edge trigger coupling mode.
        DC      — DC coupling: passes all signal components
        AC      — AC coupling: blocks the DC component
        LFREJect — low-frequency reject: acts as a high-pass filter
        HFREJect — high-frequency reject: acts as a low-pass filter

    Args:
        coupling: {DC|AC|LFREJect|HFREJect}

    Returns:
        Current coupling when querying.
    """
    if coupling is None:
        return _query(resource_name, ":TRIGger:EDGE:COUPling?")
    _send(resource_name, f":TRIGger:EDGE:COUPling {coupling}")
    return None


def trigger_edge_holdoff_devents(resource_name: str, events: int | None = None) -> str | None:
    """Set or query the edge trigger holdoff event count.

    SCPI: :TRIGger:EDGE:HLDEVent <value>
           :TRIGger:EDGE:HLDEVent?

        Configures the edge trigger holdoff event count.
        <value>:= [1, 100000000]

    Args:
        events: Holdoff event count (1 - 100000000)

    Returns:
        Current event count when querying.

    Associated commands: :TRIGger:EDGE:HOLDoff
    """
    if events is None:
        return _query(resource_name, ":TRIGger:EDGE:HLDEVent?")
    _send(resource_name, f":TRIGger:EDGE:HLDEVent {events}")
    return None


def trigger_edge_holdoff_time(resource_name: str, time: float | None = None) -> str | None:
    """Set or query the edge trigger holdoff time.

    SCPI: :TRIGger:EDGE:HLDTime <value>
           :TRIGger:EDGE:HLDTime?

        Configures the edge trigger holdoff time.
          Most models: [8.00E-09, 3.00E+01] s
          SHS800X/1000X: [80.00E-09, 1.5E+00] s

    Args:
        time: Holdoff time in seconds (NR3)

    Returns:
        Current holdoff time when querying.

    Associated commands: :TRIGger:EDGE:HOLDoff
    """
    if time is None:
        return _query(resource_name, ":TRIGger:EDGE:HLDTime?")
    _send(resource_name, f":TRIGger:EDGE:HLDTime {time}")
    return None


def trigger_edge_holdoff(resource_name: str, holdoff_type: str | None = None) -> str | None:
    """Set or query the edge trigger holdoff type.

    SCPI: :TRIGger:EDGE:HOLDoff <holdoff_type>
           :TRIGger:EDGE:HOLDoff?

        Configures the edge trigger holdoff type.
        OFF    — holdoff disabled
        EVENts — event-based: count of trigger-condition events
        TIME   — time-based: waiting period after trigger before re-arming

    Args:
        holdoff_type: {OFF|EVENts|TIME}

    Returns:
        Current holdoff type when querying.

    Associated commands: :TRIGger:EDGE:HLDEVent, :TRIGger:EDGE:HLDTime,
                          :TRIGger:EDGE:HSTart
    """
    if holdoff_type is None:
        return _query(resource_name, ":TRIGger:EDGE:HOLDoff?")
    _send(resource_name, f":TRIGger:EDGE:HOLDoff {holdoff_type}")
    return None


def trigger_edge_hstart(resource_name: str, start: str | None = None) -> str | None:
    """Set or query the edge trigger holdoff start condition.

    SCPI: :TRIGger:EDGE:HSTart <start_holdoff>
           :TRIGger:EDGE:HSTart?

        Configures the edge trigger holdoff start condition.
        LAST_TRIG — counted from the last trigger time point
        ACQ_START — counted from the first time the condition is met

    Args:
        start: {LAST_TRIG|ACQ_START}

    Returns:
        Current start condition when querying.

    Associated commands: :TRIGger:EDGE:HOLDoff
    """
    if start is None:
        return _query(resource_name, ":TRIGger:EDGE:HSTart?")
    _send(resource_name, f":TRIGger:EDGE:HSTart {start}")
    return None


def trigger_edge_impedance(resource_name: str, impedance: str | None = None) -> str | None:
    """Set or query the edge trigger source impedance (EXT/EXT5 only).

    SCPI: :TRIGger:EDGE:IMPedance <ohm>
           :TRIGger:EDGE:IMPedance?

        Configures the edge trigger source impedance. Available only when the trigger source is EXT or EXT/5.
        ONEMeg — 1 MΩ
        FIFTy  — 50 Ω

    Args:
        impedance: {ONEMeg|FIFTy}

    Returns:
        Current impedance when querying.

    Associated commands: :TRIGger:EDGE:SOURce
    """
    if impedance is None:
        return _query(resource_name, ":TRIGger:EDGE:IMPedance?")
    _send(resource_name, f":TRIGger:EDGE:IMPedance {impedance}")
    return None


def trigger_edge_level(resource_name: str, level: float | None = None) -> str | None:
    """Set or query the edge trigger level.

    SCPI: :TRIGger:EDGE:LEVel <level_value>
           :TRIGger:EDGE:LEVel?

        Configures the edge trigger level.
        Range varies by model: SDS7000A: [-4.26*V/div-offset, 4.26*V/div-offset], SDS6000/SHS: [-4.5*V/div-offset, 4.5*V/div-offset], others: [-4.1*V/div-offset, 4.1*V/div-offset].

    Args:
        level: Trigger level in volts (NR3)

    Returns:
        Current level when querying.

    Associated commands: :TRIGger:EDGE:SOURce
    """
    if level is None:
        return _query(resource_name, ":TRIGger:EDGE:LEVel?")
    _send(resource_name, f":TRIGger:EDGE:LEVel {level}")
    return None


def trigger_edge_noise_reject(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query the edge trigger noise reject state.

    SCPI: :TRIGger:EDGE:NREJect {ON|OFF}
           :TRIGger:EDGE:NREJect?

        Configures the edge trigger noise reject on/off state.

    Args:
        state: True=ON, False=OFF

    Returns:
        "ON" or "OFF" when querying.

    Associated commands: :TRIGger:EDGE:SOURce
    """
    if state is None:
        return _query(resource_name, ":TRIGger:EDGE:NREJect?")
    _send(resource_name, f":TRIGger:EDGE:NREJect {'ON' if state else 'OFF'}")
    return None


def trigger_edge_slope(resource_name: str, slope: str | None = None) -> str | None:
    """Set or query the edge trigger slope.

    SCPI: :TRIGger:EDGE:SLOPe <slope_type>
           :TRIGger:EDGE:SLOPe?

        Configures the edge trigger slope type.
        RISing    — rising edge
        FALLing   — falling edge
        ALTernate — alternating edges

    Args:
        slope: {RISing|FALLing|ALTernate}

    Returns:
        Current slope when querying.
    """
    if slope is None:
        return _query(resource_name, ":TRIGger:EDGE:SLOPe?")
    _send(resource_name, f":TRIGger:EDGE:SLOPe {slope}")
    return None


def trigger_edge_source(resource_name: str, source: str | None = None) -> str | None:
    """Set or query the edge trigger source.

    SCPI: :TRIGger:EDGE:SOURce <source>
           :TRIGger:EDGE:SOURce?

        Configures the edge trigger source.
        <source>:= {C<n>|D<d>|EX|EX5|LINE}
          C<n>: analog channels (C1-C4)
          D<d>: digital channels
          EX/EX5: external trigger input
          LINE: mains (line) trigger

    Args:
        source: Trigger source (e.g. "C1", "EX", "LINE")

    Returns:
        Current source when querying.

    Associated commands: :TRIGger:EDGE:LEVel
    """
    if source is None:
        return _query(resource_name, ":TRIGger:EDGE:SOURce?")
    _send(resource_name, f":TRIGger:EDGE:SOURce {source}")
    return None


def trigger_config(resource_name: str, args: dict) -> dict:
    """Apply trigger configuration from sds_trigger_config MCP tool arguments.

    Dynamically constructs :TRIGger:<type>:<subcmd> commands based on
    the trigger_type argument. Returns a dict of applied changes.
    """
    ch: dict = {}
    tt: str = args.get("trigger_type", "").upper()
    if tt:
        trigger_type(resource_name, tt)
        ch["trigger_type"] = tt
    if (v := args.get("trigger_mode")) is not None:
        trigger_mode(resource_name, v)
        ch["trigger_mode"] = v
    if args.get("force_trigger"):
        trigger_run(resource_name)
        ch["force_trigger"] = True
    if args.get("stop"):
        trigger_stop(resource_name)
        ch["stop"] = True

    if not tt:
        return ch

    SCPI_MAP = {
        # Generic (shared by most types)
        "source": "SOURce", "level": "LEVel", "coupling": "COUPling",
        "slope": "SLOPe", "holdoff": "HOLDoff", "holdoff_event": "HLDEVent",
        "holdoff_time": "HLDTime", "holdoff_start": "HSTart",
        "noise_reject": "NREJect", "impedance": "IMPedance",
        # Level pair
        "low_level": "LLEVel", "high_level": "HLEVel",
        # Limit / time
        "limit": "LIMit", "lower_time": "TLOWer", "upper_time": "TUPPer",
        "polarity": "POLarity",
        # WINDow
        "window_type": "TYPE", "center_level": "CLEVel", "delta_level": "DLEVel",
        # DROPout
        "dropout_type": "TYPE", "dropout_time": "TIME",
        # VIDeo
        "video_standard": "STANdard", "video_sync": "SYNC", "video_field": "FIELd",
        "video_line": "LINE", "video_frame_rate": "FRATe", "video_interlace": "INTerlace",
        # PATTern
        "pattern_input": "INPut", "pattern_logic": "LOGic",
        # NEDGe
        "idle": "IDLE", "edge": "EDGE",
        # SHOLd
        "shold_type": "TYPE", "clock_source": "CSource", "clock_threshold": "CTHReshold",
        "data_source": "DSource", "data_threshold": "DTHReshold",
    }

    for key, scpi in SCPI_MAP.items():
        if (v := args.get(key)) is not None:
            val = "ON" if v is True else ("OFF" if v is False else str(v))
            _send(resource_name, f":TRIGger:{tt}:{scpi} {val}")
            ch[key] = v

    # QUALified dual-source (ESource/ESLope/ELEVel + QSource/QLEVel)
    for qual_key, qual_scpi in [("edge_source", "ESource"), ("edge_slope", "ESLope"), ("edge_level", "ELEVel"),
                                 ("qualified_source", "QSource"), ("qualified_level", "QLEVel"),
                                 ("qualified_type", "TYPE")]:
        if (v := args.get(qual_key)) is not None:
            _send(resource_name, f":TRIGger:{tt}:{qual_scpi} {v}")
            ch[qual_key] = v

    # DELay dual-source (SOURce/SLOPe/LEVel + SOURce2/SLOPe2/LEVel2)
    for del_key, del_scpi in [("source_a", "SOURce"), ("source_b", "SOURce2"),
                               ("slope_a", "SLOPe"), ("slope_b", "SLOPe2"),
                               ("level_a", "LEVel"), ("level_b", "LEVel2")]:
        if (v := args.get(del_key)) is not None:
            _send(resource_name, f":TRIGger:{tt}:{del_scpi} {v}")
            ch[del_key] = v

    # PATTern: LEVEL needs source argument
    if (v := args.get("pattern_level")) is not None:
        src = args.get("source", "C1")
        _send(resource_name, f":TRIGger:{tt}:LEVel {src},{v}")
        ch["pattern_level"] = v

    return ch
