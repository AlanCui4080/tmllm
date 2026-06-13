"""FUNCtion subsystem SCPI commands (math/FFT/filter)."""
from __future__ import annotations
from _base import _send, _query


def function_fft_display(resource_name: str, mode: str | None = None) -> str | None:
    """Set or query FFT display mode {SPLit|FULL|EXCLusive}."""
    if mode is None:
        return _query(resource_name, ":FUNCtion:FFTDisplay?")
    _send(resource_name, f":FUNCtion:FFTDisplay {mode}")
    return None


def function_gvalue(resource_name: str, ga_gb: str | None = None) -> str | None:
    """Set or query math integrate gate threshold "GA,GB" (seconds)."""
    if ga_gb is None:
        return _query(resource_name, ":FUNCtion:GVALue?")
    _send(resource_name, f":FUNCtion:GVALue {ga_gb}")
    return None


def function_state(resource_name: str, x: int, state: bool | None = None) -> str | None:
    """Set or query math function F<x> on/off state."""
    if state is None:
        return _query(resource_name, f":FUNCtion{x}?")
    _send(resource_name, f":FUNCtion{x} {'ON' if state else 'OFF'}")
    return None


def function_average_num(resource_name: str, x: int, num: int | None = None) -> str | None:
    """Set or query average operator's average count {4|16|32|64|128|256|512|1024|...}."""
    if num is None:
        return _query(resource_name, f":FUNCtion{x}:AVERage:NUM?")
    _send(resource_name, f":FUNCtion{x}:AVERage:NUM {num}")
    return None


def function_diff_dx(resource_name: str, x: int, dx: int | None = None) -> str | None:
    """Set or query derivative step size."""
    if dx is None:
        return _query(resource_name, f":FUNCtion{x}:DIFF:DX?")
    _send(resource_name, f":FUNCtion{x}:DIFF:DX {dx}")
    return None


def function_eres_bits(resource_name: str, x: int, bits: float | None = None) -> str | None:
    """Set or query ERES bits {0.5|1.0|1.5|2.0|2.5|3.0}."""
    if bits is None:
        return _query(resource_name, f":FUNCtion{x}:ERES:BITS?")
    _send(resource_name, f":FUNCtion{x}:ERES:BITS {bits}")
    return None


def function_fft_autoset(resource_name: str, x: int, mode: str) -> None:
    """Auto set FFT {SPAN|PEAK|NORMal}."""
    _send(resource_name, f":FUNCtion{x}:FFT:AUToset {mode}")


def function_fft_hcenter(resource_name: str, x: int, center: float | None = None) -> str | None:
    """Set or query FFT center frequency (Hz)."""
    if center is None:
        return _query(resource_name, f":FUNCtion{x}:FFT:HCENter?")
    _send(resource_name, f":FUNCtion{x}:FFT:HCENter {center}")
    return None


def function_fft_hscale(resource_name: str, x: int) -> str:
    """Query FFT horizontal scale."""
    return _query(resource_name, f":FUNCtion{x}:FFT:HSCale?")


def function_fft_span(resource_name: str, x: int, span: float | None = None) -> str | None:
    """Set or query FFT frequency span (Hz)."""
    if span is None:
        return _query(resource_name, f":FUNCtion{x}:FFT:SPAN?")
    _send(resource_name, f":FUNCtion{x}:FFT:SPAN {span}")
    return None


def function_fft_load(resource_name: str, x: int, load: int | None = None) -> str | None:
    """Set or query FFT external load [1,1000000] ohms (only when unit=dBm)."""
    if load is None:
        return _query(resource_name, f":FUNCtion{x}:FFT:LOAD?")
    _send(resource_name, f":FUNCtion{x}:FFT:LOAD {load}")
    return None


def function_fft_mode(resource_name: str, x: int, mode: str | None = None) -> str | None:
    """Set or query FFT acquisition mode {NORMal|MAXHold|AVERage[,<num>]}."""
    if mode is None:
        return _query(resource_name, f":FUNCtion{x}:FFT:MODE?")
    _send(resource_name, f":FUNCtion{x}:FFT:MODE {mode}")
    return None


def function_fft_points(resource_name: str, x: int, points: str | None = None) -> str | None:
    """Set or query FFT max points (e.g. "1k","2M","32M")."""
    if points is None:
        return _query(resource_name, f":FUNCtion{x}:FFT:POINts?")
    _send(resource_name, f":FUNCtion{x}:FFT:POINts {points}")
    return None


def function_fft_reset(resource_name: str, x: int) -> None:
    """Reset FFT averaging counter."""
    _send(resource_name, f":FUNCtion{x}:FFT:RESET")


def function_fft_rlevel(resource_name: str, x: int, level: float | None = None) -> str | None:
    """Set or query FFT reference level."""
    if level is None:
        return _query(resource_name, f":FUNCtion{x}:FFT:RLEVel?")
    _send(resource_name, f":FUNCtion{x}:FFT:RLEVel {level}")
    return None


def function_fft_scale(resource_name: str, x: int, scale: float | None = None) -> str | None:
    """Set or query FFT vertical scale (dB/div or V/div)."""
    if scale is None:
        return _query(resource_name, f":FUNCtion{x}:FFT:SCALe?")
    _send(resource_name, f":FUNCtion{x}:FFT:SCALe {scale}")
    return None


def function_fft_search(resource_name: str, x: int, search_type: str | None = None) -> str | None:
    """Set or query FFT search tool {OFF|PEAK|MARKer}."""
    if search_type is None:
        return _query(resource_name, f":FUNCtion{x}:FFT:SEARch?")
    _send(resource_name, f":FUNCtion{x}:FFT:SEARch {search_type}")
    return None


def function_fft_search_excursion(resource_name: str, x: int, excursion: float | None = None) -> str | None:
    """Set or query FFT peak excursion."""
    if excursion is None:
        return _query(resource_name, f":FUNCtion{x}:FFT:SEARch:EXCursion?")
    _send(resource_name, f":FUNCtion{x}:FFT:SEARch:EXCursion {excursion}")
    return None


def function_fft_search_threshold(resource_name: str, x: int, threshold: float | None = None) -> str | None:
    """Set or query FFT peak threshold."""
    if threshold is None:
        return _query(resource_name, f":FUNCtion{x}:FFT:SEARch:THReshold?")
    _send(resource_name, f":FUNCtion{x}:FFT:SEARch:THReshold {threshold}")
    return None


def function_fft_unit(resource_name: str, x: int, unit: str | None = None) -> str | None:
    """Set or query FFT unit {DBVrms|Vrms|DBm}."""
    if unit is None:
        return _query(resource_name, f":FUNCtion{x}:FFT:UNIT?")
    _send(resource_name, f":FUNCtion{x}:FFT:UNIT {unit}")
    return None


def function_fft_window(resource_name: str, x: int, window: str | None = None) -> str | None:
    """Set or query FFT window type {RECTangle|BLACkman|HANNing|HAMMing|FLATtop}."""
    if window is None:
        return _query(resource_name, f":FUNCtion{x}:FFT:WINDow?")
    _send(resource_name, f":FUNCtion{x}:FFT:WINDow {window}")
    return None


def function_filter_type(resource_name: str, x: int, ftype: str | None = None) -> str | None:
    """Set or query filter type {LPASs|HPASs|BPASs|BREJect}."""
    if ftype is None:
        return _query(resource_name, f":FUNCtion{x}:FILTer:TYPe?")
    _send(resource_name, f":FUNCtion{x}:FILTer:TYPe {ftype}")
    return None


def function_filter_hfrequency(resource_name: str, x: int, freq: float | None = None) -> str | None:
    """Set or query filter upper cutoff frequency (Hz)."""
    if freq is None:
        return _query(resource_name, f":FUNCtion{x}:FILTer:HFRequency?")
    _send(resource_name, f":FUNCtion{x}:FILTer:HFRequency {freq}")
    return None


def function_filter_lfrequency(resource_name: str, x: int, freq: float | None = None) -> str | None:
    """Set or query filter lower cutoff frequency (Hz)."""
    if freq is None:
        return _query(resource_name, f":FUNCtion{x}:FILTer:LFRequency?")
    _send(resource_name, f":FUNCtion{x}:FILTer:LFRequency {freq}")
    return None


def function_integrate_gate(resource_name: str, x: int, state: bool | None = None) -> str | None:
    """Set or query integrate gate on/off."""
    if state is None:
        return _query(resource_name, f":FUNCtion{x}:INTegrate:GATE?")
    _send(resource_name, f":FUNCtion{x}:INTegrate:GATE {'ON' if state else 'OFF'}")
    return None


def function_integrate_offset(resource_name: str, x: int, offset: float | None = None) -> str | None:
    """Set or query integrate operator offset."""
    if offset is None:
        return _query(resource_name, f":FUNCtion{x}:INTegrate:OFFSet?")
    _send(resource_name, f":FUNCtion{x}:INTegrate:OFFSet {offset}")
    return None


def function_interpolate_coef(resource_name: str, x: int, coef: int | None = None) -> str | None:
    """Set or query interpolate coefficient {2|5|10|20}."""
    if coef is None:
        return _query(resource_name, f":FUNCtion{x}:INTErpolate:COEF?")
    _send(resource_name, f":FUNCtion{x}:INTErpolate:COEF {coef}")
    return None


def function_invert(resource_name: str, x: int, state: bool | None = None) -> str | None:
    """Set or query math function invert on/off."""
    if state is None:
        return _query(resource_name, f":FUNCtion{x}:INVert?")
    _send(resource_name, f":FUNCtion{x}:INVert {'ON' if state else 'OFF'}")
    return None


def function_label_state(resource_name: str, x: int, state: bool | None = None) -> str | None:
    """Set or query math function label display on/off."""
    if state is None:
        return _query(resource_name, f":FUNCtion{x}:LABel?")
    _send(resource_name, f":FUNCtion{x}:LABel {'ON' if state else 'OFF'}")
    return None


def function_label_text(resource_name: str, x: int, text: str | None = None) -> str | None:
    """Set or query math function label text (max 20 chars)."""
    if text is None:
        return _query(resource_name, f":FUNCtion{x}:LABel:TEXT?")
    _send(resource_name, f':FUNCtion{x}:LABel:TEXT "{text}"')
    return None


def function_maxhold_sweeps(resource_name: str, x: int, sweeps: int | None = None) -> str | None:
    """Set or query max-hold sweep limit. 0=unlimited."""
    if sweeps is None:
        return _query(resource_name, f":FUNCtion{x}:MAXHold:Sweeps?")
    _send(resource_name, f":FUNCtion{x}:MAXHold:Sweeps {sweeps}")
    return None


def function_minhold_sweeps(resource_name: str, x: int, sweeps: int | None = None) -> str | None:
    """Set or query min-hold sweep limit. 0=unlimited."""
    if sweeps is None:
        return _query(resource_name, f":FUNCtion{x}:MINHold:Sweeps?")
    _send(resource_name, f":FUNCtion{x}:MINHold:Sweeps {sweeps}")
    return None


def function_operator(resource_name: str, x: int, op: str | None = None) -> str | None:
    """Set or query math operator {ADD|SUBTract|MULTiply|DIVision|INTegrate|DIFF|FFT|...}."""
    if op is None:
        return _query(resource_name, f":FUNCtion{x}:OPERation?")
    _send(resource_name, f":FUNCtion{x}:OPERation {op}")
    return None


def function_position(resource_name: str, x: int, pos: float | None = None) -> str | None:
    """Set or query math function vertical position."""
    if pos is None:
        return _query(resource_name, f":FUNCtion{x}:POSition?")
    _send(resource_name, f":FUNCtion{x}:POSition {pos}")
    return None


def function_scale(resource_name: str, x: int, scale: float | None = None) -> str | None:
    """Set or query math function vertical scale."""
    if scale is None:
        return _query(resource_name, f":FUNCtion{x}:SCALe?")
    _send(resource_name, f":FUNCtion{x}:SCALe {scale}")
    return None


def function_source1(resource_name: str, x: int, source: str | None = None) -> str | None:
    """Set or query math function source A."""
    if source is None:
        return _query(resource_name, f":FUNCtion{x}:SOURce1?")
    _send(resource_name, f":FUNCtion{x}:SOURce1 {source}")
    return None


def function_source2(resource_name: str, x: int, source: str | None = None) -> str | None:
    """Set or query math function source B."""
    if source is None:
        return _query(resource_name, f":FUNCtion{x}:SOURce2?")
    _send(resource_name, f":FUNCtion{x}:SOURce2 {source}")
    return None


def function_fft_search_marker(resource_name: str, x: int, n: int, freq: str) -> None:
    """Set FFT search marker frequency.

    SCPI: :FUNCtion<x>:FFT:SEARch:MARKer<n> <freq>

    Args:
        x: Math function index (1-4)
        n: Marker number (1-8)
        freq: Frequency value or {NPeak|NAMPlitude}
    """
    _send(resource_name, f":FUNCtion{x}:FFT:SEARch:MARKer{n} {freq}")


def function_fft_search_marker_show(resource_name: str, x: int, n: int, state: bool) -> None:
    """Set FFT search marker display on/off.

    SCPI: :FUNCtion<x>:FFT:SEARch:MARKer<n>:SHOW <state>
    """
    _send(resource_name, f":FUNCtion{x}:FFT:SEARch:MARKer{n}:SHOW {'ON' if state else 'OFF'}")


def function_fft_search_mon(resource_name: str, x: int, mode_type: str) -> None:
    """Set FFT search marker mode.

    SCPI: :FUNCtion<x>:FFT:SEARch:MON <type>

    Args:
        x: Math function index (1-4)
        mode_type: {PEAK|HARMonics}
    """
    _send(resource_name, f":FUNCtion{x}:FFT:SEARch:MON {mode_type}")


def function_fft_search_porder(resource_name: str, x: int, order: str | None = None) -> str | None:
    """Set or query FFT peak sort order.

    SCPI: :FUNCtion<x>:FFT:SEARch:PORDer <type>
           :FUNCtion<x>:FFT:SEARch:PORDer?

    Args:
        order: {AMPLitude|FREQuency}
    """
    if order is None:
        return _query(resource_name, f":FUNCtion{x}:FFT:SEARch:PORDer?")
    _send(resource_name, f":FUNCtion{x}:FFT:SEARch:PORDer {order}")
    return None


def function_fft_search_result(resource_name: str, x: int) -> str:
    """Query FFT search results.

    SCPI: :FUNCtion<x>:FFT:SEARch:RESult?

    Returns peak list: type,no,freq,ampl;...
    """
    return _query(resource_name, f":FUNCtion{x}:FFT:SEARch:RESult?")


def function_fft_search_table(resource_name: str, x: int, state: bool | None = None) -> str | None:
    """Set or query FFT search table display on/off.

    SCPI: :FUNCtion<x>:FFT:SEARch:TABLe <state>
           :FUNCtion<x>:FFT:SEARch:TABLe?
    """
    if state is None:
        return _query(resource_name, f":FUNCtion{x}:FFT:SEARch:TABLe?")
    _send(resource_name, f":FUNCtion{x}:FFT:SEARch:TABLe {'ON' if state else 'OFF'}")
    return None


def function_fft_search_table_delta(resource_name: str, x: int, state: bool | None = None) -> str | None:
    """Set or query FFT search table delta column on/off.

    SCPI: :FUNCtion<x>:FFT:SEARch:TABLe:DELTa <state>
           :FUNCtion<x>:FFT:SEARch:TABLe:DELTa?
    """
    if state is None:
        return _query(resource_name, f":FUNCtion{x}:FFT:SEARch:TABLe:DELTa?")
    _send(resource_name, f":FUNCtion{x}:FFT:SEARch:TABLe:DELTa {'ON' if state else 'OFF'}")
    return None


def function_fft_search_table_frequency(resource_name: str, x: int, state: bool | None = None) -> str | None:
    """Set or query FFT search table frequency column on/off.

    SCPI: :FUNCtion<x>:FFT:SEARch:TABLe:FREQuency <state>
           :FUNCtion<x>:FFT:SEARch:TABLe:FREQuency?
    """
    if state is None:
        return _query(resource_name, f":FUNCtion{x}:FFT:SEARch:TABLe:FREQuency?")
    _send(resource_name, f":FUNCtion{x}:FFT:SEARch:TABLe:FREQuency {'ON' if state else 'OFF'}")
    return None


def function_fft_marker_frequency(resource_name: str, x: int, freq: str | float) -> None:
    """Set FFT search marker frequency.

    SCPI: :FUNCtion<x>:FFT:SEARch:MARKer:FREQuency <freq>

    Args:
        x: Math function index (1-4)
        freq: Frequency value in Hz
    """
    _send(resource_name, f":FUNCtion{x}:FFT:SEARch:MARKer:FREQuency {freq}")
