"""CURSor subsystem SCPI commands (common, single, multi)."""

from __future__ import annotations

from _base import _send, _query


# ═══════════════════════════════════════════════════════════════════
#  CURSor subsystem  (:CURSor)
#  — Common Commands (common to single & multi cursor)
# ═══════════════════════════════════════════════════════════════════

def cursor_state(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query the cursor on/off state.

    SCPI: :CURSor {ON|OFF}
           :CURSor?

        Configures the cursor display on/off state.

    Args:
        state: True=ON, False=OFF

    Returns:
        "ON" or "OFF" when querying.
    """
    if state is None:
        return _query(resource_name, ":CURSor?")
    _send(resource_name, f":CURSor {'ON' if state else 'OFF'}")
    return None


def cursor_tag_style(resource_name: str, style: str | None = None) -> str | None:
    """Set or query the cursor display style.

    SCPI: :CURSor:TAGStyle <style>
           :CURSor:TAGStyle?

        Configures the cursor display style.
        FIXed     — fixed cursor style
        FOLLowing — following cursor style

    Args:
        style: {FIXed|FOLLowing}

    Returns:
        Current style when querying.
    """
    if style is None:
        return _query(resource_name, ":CURSor:TAGStyle?")
    _send(resource_name, f":CURSor:TAGStyle {style}")
    return None


def cursor_x_reference(resource_name: str, ref_type: str | None = None) -> str | None:
    """Set or query the X cursor reference type.

    SCPI: :CURSor:XREFerence <type>
           :CURSor:XREFerence?

        Configures the X cursor reference type.
        DELay   — delay fixed: X cursor values stay constant when horizontal scale changes
        POSition — position fixed: X cursors stay at fixed grid positions when horizontal scale changes

    Args:
        ref_type: {DELay|POSition}

    Returns:
        Current reference type when querying.
    """
    if ref_type is None:
        return _query(resource_name, ":CURSor:XREFerence?")
    _send(resource_name, f":CURSor:XREFerence {ref_type}")
    return None


def cursor_y_reference(resource_name: str, ref_type: str | None = None) -> str | None:
    """Set or query the Y cursor reference type.

    SCPI: :CURSor:YREFerence <type>
           :CURSor:YREFerence?

        Configures the Y cursor reference type.
        OFFSet   — offset fixed: Y cursor values stay constant when vertical scale changes
        POSition — position fixed: Y cursors stay at fixed grid positions when vertical scale changes

    Args:
        ref_type: {OFFSet|POSition}

    Returns:
        Current reference type when querying.
    """
    if ref_type is None:
        return _query(resource_name, ":CURSor:YREFerence?")
    _send(resource_name, f":CURSor:YREFerence {ref_type}")
    return None


# ═══════════════════════════════════════════════════════════════════
#  CURSor — Single Cursor Set (X1/X2/Y1/Y2)
# ═══════════════════════════════════════════════════════════════════

def cursor_ixdelta(resource_name: str) -> str:
    """Query the cursor 1/(X2-X1) value.

    SCPI: :CURSor:IXDelta?

        Queries the current 1/(X2-X1) cursor value.

    Returns:
        Value in NR3 format (e.g. "3.8E-05").
    """
    return _query(resource_name, ":CURSor:IXDelta?")


def cursor_measure_item(resource_name: str, item: str | None = None) -> str | None:
    """Set or query the measurement item when cursor mode is MEASure.

    SCPI: :CURSor:MITem <type>,<source1>[,<source2>]
           :CURSor:MITem?

        When cursor mode is MEASure, configures the measurement item.
        <type>:= same measurement types as the MEASure subsystem
        <source1>:= {C<n>|Z<n>|F<x>|M<m>|D<d>|ZD<d>|REF<r>}
        <source2>:= {C<n>} — only needed for channel-delay measurements

    Args:
        item: Measurement item string (e.g. "PKPK,C2")
        None — query current item

    Returns:
        Current measurement item when querying (e.g. "PKPK,C2").
    """
    if item is None:
        return _query(resource_name, ":CURSor:MITem?")
    _send(resource_name, f":CURSor:MITem {item}")
    return None


def cursor_mode(resource_name: str, mode: str | None = None) -> str | None:
    """Set or query the cursor mode.

    SCPI: :CURSor:MODE <type>
           :CURSor:MODE?

        Configures the cursor mode.
        MANual[,X|Y|XY] — manual cursor, can specify horizontal (X), vertical (Y), or both (XY)
        TRACk           — tracking cursor, automatically set to horizontal+vertical
        MEASure         — measurement cursor, shows how the measurement item is computed

    Args:
        mode: {TRACk|MANual[,X|Y|XY]|MEASure}
            e.g. "MANual,X" for manual horizontal cursors

    Returns:
        Current mode when querying.
    """
    if mode is None:
        return _query(resource_name, ":CURSor:MODE?")
    _send(resource_name, f":CURSor:MODE {mode}")
    return None


def cursor_source1(resource_name: str, source: str | None = None) -> str | None:
    """Set or query the X1/Y1 cursor source channel.

    SCPI: :CURSor:SOURce1 <source>
           :CURSor:SOURce1?

        Configures the X1/Y1 cursor source channel.
        <source>:= {C<n>|Z<n>|F<x>|M<m>|REF<r>|DIGital|HISTOGram}

    Args:
        source: Source identifier (e.g. "C1", "F1")

    Returns:
        Current source when querying.
    """
    if source is None:
        return _query(resource_name, ":CURSor:SOURce1?")
    _send(resource_name, f":CURSor:SOURce1 {source}")
    return None


def cursor_source2(resource_name: str, source: str | None = None) -> str | None:
    """Set or query the X2/Y2 cursor source channel.

    SCPI: :CURSor:SOURce2 <source>
           :CURSor:SOURce2?

        Configures the X2/Y2 cursor source channel.
        <source>:= {C<n>|Z<n>|F<x>|M<m>|REF<r>|DIGital|HISTOGram}

    Args:
        source: Source identifier (e.g. "C2", "M1")

    Returns:
        Current source when querying.
    """
    if source is None:
        return _query(resource_name, ":CURSor:SOURce2?")
    _send(resource_name, f":CURSor:SOURce2 {source}")
    return None


def cursor_x1(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the cursor X1 position.

    SCPI: :CURSor:X1 <value>
           :CURSor:X1?

        Configures the cursor X1 position.
        Range: [-grid_divs/2 * timebase + horizontal_delay, grid_divs/2 * timebase + horizontal_delay]

    Args:
        value: X1 position in seconds (NR3)

    Returns:
        Current X1 position when querying (e.g. "1.00E-06").
    """
    if value is None:
        return _query(resource_name, ":CURSor:X1?")
    _send(resource_name, f":CURSor:X1 {value}")
    return None


def cursor_x2(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the cursor X2 position.

    SCPI: :CURSor:X2 <value>
           :CURSor:X2?

        Configures the cursor X2 position.
        Range: [-grid_divs/2 * timebase + horizontal_delay, grid_divs/2 * timebase + horizontal_delay]

    Args:
        value: X2 position in seconds (NR3)

    Returns:
        Current X2 position when querying (e.g. "-1.00E-06").
    """
    if value is None:
        return _query(resource_name, ":CURSor:X2?")
    _send(resource_name, f":CURSor:X2 {value}")
    return None


def cursor_xdelta(resource_name: str) -> str:
    """Query the horizontal difference X2 - X1.

    SCPI: :CURSor:XDELta?

        Queries the horizontal difference X2 - X1.

    Returns:
        Delta value in NR3 format (e.g. "-2E-06").
    """
    return _query(resource_name, ":CURSor:XDELta?")


def cursor_y1(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the cursor Y1 position.

    SCPI: :CURSor:Y1 <value>
           :CURSor:Y1?

        Configures the cursor Y1 position.
        Range: [-grid_divs/2 * V/div + offset, grid_divs/2 * V/div + offset]

    Args:
        value: Y1 position in volts (NR3)

    Returns:
        Current Y1 position when querying (e.g. "1.20E+01").
    """
    if value is None:
        return _query(resource_name, ":CURSor:Y1?")
    _send(resource_name, f":CURSor:Y1 {value}")
    return None


def cursor_y2(resource_name: str, value: float | None = None) -> str | None:
    """Set or query the cursor Y2 position.

    SCPI: :CURSor:Y2 <value>
           :CURSor:Y2?

        Configures the cursor Y2 position.
        Range: [-grid_divs/2 * V/div + offset, grid_divs/2 * V/div + offset]

    Args:
        value: Y2 position in volts (NR3)

    Returns:
        Current Y2 position when querying (e.g. "-1.20E+01").
    """
    if value is None:
        return _query(resource_name, ":CURSor:Y2?")
    _send(resource_name, f":CURSor:Y2 {value}")
    return None


def cursor_ydelta(resource_name: str) -> str:
    """Query the vertical difference Y2 - Y1.

    SCPI: :CURSor:YDELta?

        Queries the vertical difference Y2 - Y1.

    Returns:
        Delta value in NR3 format (e.g. "-2.4E+01").
    """
    return _query(resource_name, ":CURSor:YDELta?")


# ═══════════════════════════════════════════════════════════════════
#  CURSor — Multi-Cursor: Manual X (MANual:X<n>)
# ═══════════════════════════════════════════════════════════════════

def cursor_manual_x_state(resource_name: str, n: int, state: bool | None = None) -> str | None:
    """Set or query the manual X cursor ``n`` on/off state.

    SCPI: :CURSor:MANual:X<n> {ON|OFF}

        Configures the on/off state for manual X cursor ``n``.
        <n>:= [1,8]

    Args:
        n: Manual X cursor index (1-8)
        state: True=ON, False=OFF

    Returns:
        "ON" or "OFF" when querying.
    """
    if state is None:
        return _query(resource_name, f":CURSor:MANual:X{n}?")
    _send(resource_name, f":CURSor:MANual:X{n} {'ON' if state else 'OFF'}")
    return None


def cursor_manual_x_color(resource_name: str, n: int, color: str | None = None) -> str | None:
    """Set or query the manual X cursor ``n`` color.

    SCPI: :CURSor:MANual:X<n>:COLor <color>

        Configures the color for manual X cursor ``n``.
        DEFault — default color derived from the cursor source
        DELTa   — synchronize to reference cursor color
        CUSTom,<string> — custom hex RGB color (e.g. "#ff0000")

    Args:
        n: Manual X cursor index (1-8)
        color: {DEFault|DELTa|CUSTom,<hex>}
        None — query

    Returns:
        Current color (hex RGB string) when querying.
    """
    if color is None:
        return _query(resource_name, f":CURSor:MANual:X{n}:COLor?")
    _send(resource_name, f":CURSor:MANual:X{n}:COLor {color}")
    return None


def cursor_manual_x_dfollow(resource_name: str, n: int, enable: bool | None = None) -> str | None:
    """Set or query whether manual X cursor ``n`` follows reference cursor.

    SCPI: :CURSor:MANual:X<n>:DFOLlow {ON|OFF}

        Configures whether manual X cursor ``n`` follows a reference cursor at a fixed offset.
        Note: can only be set when the reference cursor source is not NONE.

    Args:
        n: Manual X cursor index (1-8)
        enable: True=ON, False=OFF

    Returns:
        "ON" or "OFF" when querying.
    """
    if enable is None:
        return _query(resource_name, f":CURSor:MANual:X{n}:DFOLlow?")
    _send(resource_name, f":CURSor:MANual:X{n}:DFOLlow {'ON' if enable else 'OFF'}")
    return None


def cursor_manual_x_dtcursor(resource_name: str, n: int, ref_cursor: str | None = None) -> str | None:
    """Set or query the reference cursor for manual X cursor ``n``.

    SCPI: :CURSor:MANual:X<n>:DTCursor <source>

        Configures the reference cursor for manual X cursor ``n``.
        <source>:= {MX<m>|TRACK<t>|NONE}
          MX<m>: manual X cursor index [1,8]
          TRACK<t>: tracking cursor index [1,8]
          NONE: no reference cursor

    Args:
        n: Manual X cursor index (1-8)
        ref_cursor: {MX1..MX8|TRACK1..TRACK8|NONE}

    Returns:
        Current reference cursor when querying.
    """
    if ref_cursor is None:
        return _query(resource_name, f":CURSor:MANual:X{n}:DTCursor?")
    _send(resource_name, f":CURSor:MANual:X{n}:DTCursor {ref_cursor}")
    return None


def cursor_manual_x_dvalue(resource_name: str, n: int, value: float | None = None) -> str | None:
    """Set or query manual X cursor ``n`` position relative to reference cursor.

    SCPI: :CURSor:MANual:X<n>:DVALue <value>

        Configures the position of manual X cursor ``n`` relative to its reference cursor.

    Args:
        n: Manual X cursor index (1-8)
        value: Relative position in seconds (NR3)

    Returns:
        Current relative position when querying.
    """
    if value is None:
        return _query(resource_name, f":CURSor:MANual:X{n}:DVALue?")
    _send(resource_name, f":CURSor:MANual:X{n}:DVALue {value}")
    return None


def cursor_manual_x_label(resource_name: str, n: int, label: str | None = None) -> str | None:
    """Set or query the label for manual X cursor ``n``.

    SCPI: :CURSor:MANual:X<n>:LABel <state>

        Configures the label for manual X cursor ``n``.
        DEFault — default empty label
        DELTa   — synchronize to reference cursor label
        CUSTom,<string> — custom label (up to 20 characters)

    Args:
        n: Manual X cursor index (1-8)
        label: {DEFault|DELTa|CUSTom,<text>}

    Returns:
        Current label string when querying.
    """
    if label is None:
        return _query(resource_name, f":CURSor:MANual:X{n}:LABel?")
    _send(resource_name, f":CURSor:MANual:X{n}:LABel {label}")
    return None


def cursor_manual_x_position(resource_name: str, n: int, value: float | None = None) -> str | None:
    """Set or query manual X cursor ``n`` absolute position.

    SCPI: :CURSor:MANual:X<n>:POSition <value>

        Configures the absolute position of manual X cursor ``n``.
        Range: [-grid_divs/2 * timebase + horizontal_delay, grid_divs/2 * timebase + horizontal_delay]

    Args:
        n: Manual X cursor index (1-8)
        value: Absolute position in seconds (NR3)

    Returns:
        Current position when querying.
    """
    if value is None:
        return _query(resource_name, f":CURSor:MANual:X{n}:POSition?")
    _send(resource_name, f":CURSor:MANual:X{n}:POSition {value}")
    return None


def cursor_manual_x_source(resource_name: str, n: int, source: str | None = None) -> str | None:
    """Set or query the signal source for manual X cursor ``n``.

    SCPI: :CURSor:MANual:X<n>:SOURce <source>

        Configures the signal source for manual X cursor ``n``.
        <source>:= {C<n>|Z<n>|F<x>|ZF<x>|M<m>|ZM<m>|DIGital|ZDIGital|HISTOGram}

    Args:
        n: Manual X cursor index (1-8)
        source: Source identifier (e.g. "C1", "F1", "M1")

    Returns:
        Current source when querying.
    """
    if source is None:
        return _query(resource_name, f":CURSor:MANual:X{n}:SOURce?")
    _send(resource_name, f":CURSor:MANual:X{n}:SOURce {source}")
    return None


# ═══════════════════════════════════════════════════════════════════
#  CURSor — Multi-Cursor: Manual Y (MANual:Y<n>)
# ═══════════════════════════════════════════════════════════════════

def cursor_manual_y_state(resource_name: str, n: int, state: bool | None = None) -> str | None:
    """Set or query the manual Y cursor ``n`` on/off state.

    SCPI: :CURSor:MANual:Y<n> {ON|OFF}

        Configures the on/off state for manual Y cursor ``n``.
        <n>:= [1,8]

    Args:
        n: Manual Y cursor index (1-8)
        state: True=ON, False=OFF

    Returns:
        "ON" or "OFF" when querying.
    """
    if state is None:
        return _query(resource_name, f":CURSor:MANual:Y{n}?")
    _send(resource_name, f":CURSor:MANual:Y{n} {'ON' if state else 'OFF'}")
    return None


def cursor_manual_y_color(resource_name: str, n: int, color: str | None = None) -> str | None:
    """Set or query the manual Y cursor ``n`` color.

    SCPI: :CURSor:MANual:Y<n>:COLor <color>

        Configures the color for manual Y cursor ``n``.
        DEFault — default color derived from the cursor source
        DELTa   — synchronize to reference cursor color
        CUSTom,<string> — custom hex RGB color

    Args:
        n: Manual Y cursor index (1-8)
        color: {DEFault|DELTa|CUSTom,<hex>}

    Returns:
        Current color (hex RGB string) when querying.
    """
    if color is None:
        return _query(resource_name, f":CURSor:MANual:Y{n}:COLor?")
    _send(resource_name, f":CURSor:MANual:Y{n}:COLor {color}")
    return None


def cursor_manual_y_dfollow(resource_name: str, n: int, enable: bool | None = None) -> str | None:
    """Set or query whether manual Y cursor ``n`` follows reference cursor.

    SCPI: :CURSor:MANual:Y<n>:DFOLlow {ON|OFF}

        Configures whether manual Y cursor ``n`` follows a reference cursor at a fixed offset.

    Args:
        n: Manual Y cursor index (1-8)
        enable: True=ON, False=OFF

    Returns:
        "ON" or "OFF" when querying.
    """
    if enable is None:
        return _query(resource_name, f":CURSor:MANual:Y{n}:DFOLlow?")
    _send(resource_name, f":CURSor:MANual:Y{n}:DFOLlow {'ON' if enable else 'OFF'}")
    return None


def cursor_manual_y_dtcursor(resource_name: str, n: int, ref_cursor: str | None = None) -> str | None:
    """Set or query the reference cursor for manual Y cursor ``n``.

    SCPI: :CURSor:MANual:Y<n>:DTCursor <source>

        Configures the reference cursor for manual Y cursor ``n``.
        <source>:= {MY<m>|NONE}, <m> = [1,8]

    Args:
        n: Manual Y cursor index (1-8)
        ref_cursor: {MY1..MY8|NONE}

    Returns:
        Current reference cursor when querying.
    """
    if ref_cursor is None:
        return _query(resource_name, f":CURSor:MANual:Y{n}:DTCursor?")
    _send(resource_name, f":CURSor:MANual:Y{n}:DTCursor {ref_cursor}")
    return None


def cursor_manual_y_dvalue(resource_name: str, n: int, value: float | None = None) -> str | None:
    """Set or query manual Y cursor ``n`` position relative to reference cursor.

    SCPI: :CURSor:MANual:Y<n>:DVALue <value>

        Configures the position of manual Y cursor ``n`` relative to its reference cursor.

    Args:
        n: Manual Y cursor index (1-8)
        value: Relative position in volts (NR3)

    Returns:
        Current relative position when querying.
    """
    if value is None:
        return _query(resource_name, f":CURSor:MANual:Y{n}:DVALue?")
    _send(resource_name, f":CURSor:MANual:Y{n}:DVALue {value}")
    return None


def cursor_manual_y_label(resource_name: str, n: int, label: str | None = None) -> str | None:
    """Set or query the label for manual Y cursor ``n``.

    SCPI: :CURSor:MANual:Y<n>:LABel <state>

        Configures the label for manual Y cursor ``n``.
        DEFault — default empty label
        DELTa   — synchronize to reference cursor label
        CUSTom,<string> — custom label (up to 20 characters)

    Args:
        n: Manual Y cursor index (1-8)
        label: {DEFault|DELTa|CUSTom,<text>}

    Returns:
        Current label string when querying.
    """
    if label is None:
        return _query(resource_name, f":CURSor:MANual:Y{n}:LABel?")
    _send(resource_name, f":CURSor:MANual:Y{n}:LABel {label}")
    return None


def cursor_manual_y_position(resource_name: str, n: int, value: float | None = None) -> str | None:
    """Set or query manual Y cursor ``n`` absolute position.

    SCPI: :CURSor:MANual:Y<n>:POSition <value>

        Configures the absolute position of manual Y cursor ``n``.
        Range: [-grid_divs/2 * V/div + offset, grid_divs/2 * V/div + offset]

    Args:
        n: Manual Y cursor index (1-8)
        value: Absolute position in volts (NR3)

    Returns:
        Current position when querying.
    """
    if value is None:
        return _query(resource_name, f":CURSor:MANual:Y{n}:POSition?")
    _send(resource_name, f":CURSor:MANual:Y{n}:POSition {value}")
    return None


def cursor_manual_y_source(resource_name: str, n: int, source: str | None = None) -> str | None:
    """Set or query the signal source for manual Y cursor ``n``.

    SCPI: :CURSor:MANual:Y<n>:SOURce <source>

        Configures the signal source for manual Y cursor ``n``.
        <source>:= {C<n>|Z<n>|F<x>|ZF<x>|M<m>|ZM<m>|HISTOGram}

    Args:
        n: Manual Y cursor index (1-8)
        source: Source identifier (e.g. "C1", "F1")

    Returns:
        Current source when querying.
    """
    if source is None:
        return _query(resource_name, f":CURSor:MANual:Y{n}:SOURce?")
    _send(resource_name, f":CURSor:MANual:Y{n}:SOURce {source}")
    return None


# ═══════════════════════════════════════════════════════════════════
#  CURSor — Multi-Cursor: Measure (MEASure<n>)
# ═══════════════════════════════════════════════════════════════════

def cursor_measure_state(resource_name: str, n: int, state: bool | None = None) -> str | None:
    """Set or query the measure cursor ``n`` on/off state.

    SCPI: :CURSor:MEASure<n> {ON|OFF}

        Configures the on/off state for measurement cursor MEA ``n``.
        <n>:= [1,4]

    Args:
        n: Measure cursor index (1-4)
        state: True=ON, False=OFF

    Returns:
        "ON" or "OFF" when querying.
    """
    if state is None:
        return _query(resource_name, f":CURSor:MEASure{n}?")
    _send(resource_name, f":CURSor:MEASure{n} {'ON' if state else 'OFF'}")
    return None


def cursor_measure_color(resource_name: str, n: int, color: str | None = None) -> str | None:
    """Set or query the measure cursor ``n`` color.

    SCPI: :CURSor:MEASure<n>:COLor <color>

        Configures the color for measurement cursor MEA ``n``.
        DEFault — default color derived from the cursor source
        CUSTom,<string> — custom hex RGB color

    Args:
        n: Measure cursor index (1-4)
        color: {DEFault|CUSTom,<hex>}

    Returns:
        Current color (hex RGB string) when querying.
    """
    if color is None:
        return _query(resource_name, f":CURSor:MEASure{n}:COLor?")
    _send(resource_name, f":CURSor:MEASure{n}:COLor {color}")
    return None


def cursor_measure_label(resource_name: str, n: int, label: str | None = None) -> str | None:
    """Set or query the label for measure cursor ``n``.

    SCPI: :CURSor:MEASure<n>:LABel <state>

        Configures the label for measurement cursor MEA ``n``.
        DEFault — default label
        CUSTom,<string> — custom label (up to 20 characters)

    Args:
        n: Measure cursor index (1-4)
        label: {DEFault|CUSTom,<text>}

    Returns:
        Current label string when querying.
    """
    if label is None:
        return _query(resource_name, f":CURSor:MEASure{n}:LABel?")
    _send(resource_name, f":CURSor:MEASure{n}:LABel {label}")
    return None


def cursor_measure_mitem(resource_name: str, n: int, item: str | None = None) -> str | None:
    """Set or query the measurement item for measure cursor ``n``.

    SCPI: :CURSor:MEASure<n>:MITem <type>,<source1>[,<source2>]

        Configures the measurement item for measurement cursor MEA ``n``.
        <type>:= same measurement types as the MEASure subsystem
        <source1>:= {C<n>|Z<n>|F<x>|M<m>|D<d>|ZD<d>}

    Args:
        n: Measure cursor index (1-4)
        item: Measurement item string (e.g. "PKPK,C2")

    Returns:
        Current measurement item when querying.
    """
    if item is None:
        return _query(resource_name, f":CURSor:MEASure{n}:MITem?")
    _send(resource_name, f":CURSor:MEASure{n}:MITem {item}")
    return None


# ═══════════════════════════════════════════════════════════════════
#  CURSor — Multi-Cursor: Tracking (TRACk<n>)
# ═══════════════════════════════════════════════════════════════════

def cursor_track_state(resource_name: str, n: int, state: bool | None = None) -> str | None:
    """Set or query the tracking cursor ``n`` on/off state.

    SCPI: :CURSor:TRACk<n> {ON|OFF}

        Configures the on/off state for tracking cursor TX ``n``.
        <n>:= [1,8]

    Args:
        n: Tracking cursor index (1-8)
        state: True=ON, False=OFF

    Returns:
        "ON" or "OFF" when querying.
    """
    if state is None:
        return _query(resource_name, f":CURSor:TRACk{n}?")
    _send(resource_name, f":CURSor:TRACk{n} {'ON' if state else 'OFF'}")
    return None


def cursor_track_color(resource_name: str, n: int, color: str | None = None) -> str | None:
    """Set or query the tracking cursor ``n`` color.

    SCPI: :CURSor:TRACk<n>:COLor <color>

        Configures the color for tracking cursor TX ``n``.
        DEFault — default color derived from the cursor source
        DELTa   — synchronize to reference cursor color
        CUSTom,<string> — custom hex RGB color

    Args:
        n: Tracking cursor index (1-8)
        color: {DEFault|DELTa|CUSTom,<hex>}

    Returns:
        Current color (hex RGB string) when querying.
    """
    if color is None:
        return _query(resource_name, f":CURSor:TRACk{n}:COLor?")
    _send(resource_name, f":CURSor:TRACk{n}:COLor {color}")
    return None


def cursor_track_dfollow(resource_name: str, n: int, enable: bool | None = None) -> str | None:
    """Set or query whether tracking cursor ``n`` follows reference cursor.

    SCPI: :CURSor:TRACk<n>:DFOLlow {ON|OFF}

        Configures whether tracking cursor TX ``n`` follows a reference cursor at a fixed offset.

    Args:
        n: Tracking cursor index (1-8)
        enable: True=ON, False=OFF

    Returns:
        "ON" or "OFF" when querying.
    """
    if enable is None:
        return _query(resource_name, f":CURSor:TRACk{n}:DFOLlow?")
    _send(resource_name, f":CURSor:TRACk{n}:DFOLlow {'ON' if enable else 'OFF'}")
    return None


def cursor_track_dtcursor(resource_name: str, n: int, ref_cursor: str | None = None) -> str | None:
    """Set or query the reference cursor for tracking cursor ``n``.

    SCPI: :CURSor:TRACk<n>:DTCursor <source>

        Configures the reference cursor for tracking cursor TX ``n``.
        <source>:= {MX<m>|TRACK<t>|NONE}, <m>,<t> = [1,8]

    Args:
        n: Tracking cursor index (1-8)
        ref_cursor: {MX1..MX8|TRACK1..TRACK8|NONE}

    Returns:
        Current reference cursor when querying.
    """
    if ref_cursor is None:
        return _query(resource_name, f":CURSor:TRACk{n}:DTCursor?")
    _send(resource_name, f":CURSor:TRACk{n}:DTCursor {ref_cursor}")
    return None


def cursor_track_dvalue(resource_name: str, n: int, value: float | None = None) -> str | None:
    """Set or query tracking cursor ``n`` position relative to reference cursor.

    SCPI: :CURSor:TRACk<n>:DVALue <value>

        Configures the position of tracking cursor TX ``n`` relative to its reference cursor.

    Args:
        n: Tracking cursor index (1-8)
        value: Relative position in seconds (NR3)

    Returns:
        Current relative position when querying.
    """
    if value is None:
        return _query(resource_name, f":CURSor:TRACk{n}:DVALue?")
    _send(resource_name, f":CURSor:TRACk{n}:DVALue {value}")
    return None


def cursor_track_label(resource_name: str, n: int, label: str | None = None) -> str | None:
    """Set or query the label for tracking cursor ``n``.

    SCPI: :CURSor:TRACk<n>:LABel <state>

        Configures the label for tracking cursor TX ``n``.
        DEFault — default empty label
        DELTa   — synchronize to reference cursor label
        CUSTom,<string> — custom label (up to 20 characters)

    Args:
        n: Tracking cursor index (1-8)
        label: {DEFault|DELTa|CUSTom,<text>}

    Returns:
        Current label string when querying.
    """
    if label is None:
        return _query(resource_name, f":CURSor:TRACk{n}:LABel?")
    _send(resource_name, f":CURSor:TRACk{n}:LABel {label}")
    return None


def cursor_track_position(resource_name: str, n: int, value: float | None = None) -> str | None:
    """Set or query tracking cursor ``n`` absolute position.

    SCPI: :CURSor:TRACk<n>:POSition <value>

        Configures the absolute position of tracking cursor TX ``n``.
        Range: [-grid_divs/2 * timebase + horizontal_delay, grid_divs/2 * timebase + horizontal_delay]

    Args:
        n: Tracking cursor index (1-8)
        value: Absolute position in seconds (NR3)

    Returns:
        Current position when querying.
    """
    if value is None:
        return _query(resource_name, f":CURSor:TRACk{n}:POSition?")
    _send(resource_name, f":CURSor:TRACk{n}:POSition {value}")
    return None


def cursor_track_source(resource_name: str, n: int, source: str | None = None) -> str | None:
    """Set or query the signal source for tracking cursor ``n``.

    SCPI: :CURSor:TRACk<n>:SOURce <source>

        Configures the signal source for tracking cursor TX ``n``.
        <source>:= {C<n>|Z<n>|F<x>|ZF<x>|M<m>|ZM<m>|HISTOGram}

    Args:
        n: Tracking cursor index (1-8)
        source: Source identifier (e.g. "C1", "F1")

    Returns:
        Current source when querying.
    """
    if source is None:
        return _query(resource_name, f":CURSor:TRACk{n}:SOURce?")
    _send(resource_name, f":CURSor:TRACk{n}:SOURce {source}")
    return None


def cursor_track_value(resource_name: str, n: int) -> str:
    """Query the tracking cursor ``n`` value.

    SCPI: :CURSor:TRACk<n>:VALue?

        Queries the current value of tracking cursor TX ``n``.

    Args:
        n: Tracking cursor index (1-8)

    Returns:
        Current tracking value.
    """
    return _query(resource_name, f":CURSor:TRACk{n}:VALue?")


# ═══════════════════════════════════════════════════════════════════
#  CURSor — Multi-Cursor: XY (XY:X<n>, XY:Y<n>)
# ═══════════════════════════════════════════════════════════════════

def cursor_xy_x_state(resource_name: str, n: int, state: bool | None = None) -> str | None:
    """Set or query the XY X cursor ``n`` on/off state.

    SCPI: :CURSor:XY:X<n> {ON|OFF}

        Configures the on/off state for XY X cursor ``n``.
        <n>:= [1,4]

    Args:
        n: XY X cursor index (1-4)
        state: True=ON, False=OFF
    """
    if state is None:
        return _query(resource_name, f":CURSor:XY:X{n}?")
    _send(resource_name, f":CURSor:XY:X{n} {'ON' if state else 'OFF'}")
    return None


def cursor_xy_x_color(resource_name: str, n: int, color: str | None = None) -> str | None:
    """Set or query the XY X cursor ``n`` color.

    SCPI: :CURSor:XY:X<n>:COLor <color>
    """
    if color is None:
        return _query(resource_name, f":CURSor:XY:X{n}:COLor?")
    _send(resource_name, f":CURSor:XY:X{n}:COLor {color}")
    return None


def cursor_xy_x_dfollow(resource_name: str, n: int, enable: bool | None = None) -> str | None:
    """Set or query whether XY X cursor ``n`` follows reference cursor.

    SCPI: :CURSor:XY:X<n>:DFOLlow {ON|OFF}
    """
    if enable is None:
        return _query(resource_name, f":CURSor:XY:X{n}:DFOLlow?")
    _send(resource_name, f":CURSor:XY:X{n}:DFOLlow {'ON' if enable else 'OFF'}")
    return None


def cursor_xy_x_dtcursor(resource_name: str, n: int, ref_cursor: str | None = None) -> str | None:
    """Set or query the reference cursor for XY X cursor ``n``.

    SCPI: :CURSor:XY:X<n>:DTCursor <source>
    """
    if ref_cursor is None:
        return _query(resource_name, f":CURSor:XY:X{n}:DTCursor?")
    _send(resource_name, f":CURSor:XY:X{n}:DTCursor {ref_cursor}")
    return None


def cursor_xy_x_dvalue(resource_name: str, n: int, value: float | None = None) -> str | None:
    """Set or query XY X cursor ``n`` position relative to reference cursor.

    SCPI: :CURSor:XY:X<n>:DVALue <value>
    """
    if value is None:
        return _query(resource_name, f":CURSor:XY:X{n}:DVALue?")
    _send(resource_name, f":CURSor:XY:X{n}:DVALue {value}")
    return None


def cursor_xy_x_label(resource_name: str, n: int, label: str | None = None) -> str | None:
    """Set or query the label for XY X cursor ``n``.

    SCPI: :CURSor:XY:X<n>:LABel <state>
    """
    if label is None:
        return _query(resource_name, f":CURSor:XY:X{n}:LABel?")
    _send(resource_name, f":CURSor:XY:X{n}:LABel {label}")
    return None


def cursor_xy_x_position(resource_name: str, n: int, value: float | None = None) -> str | None:
    """Set or query XY X cursor ``n`` absolute position.

    SCPI: :CURSor:XY:X<n>:POSition <value>
    """
    if value is None:
        return _query(resource_name, f":CURSor:XY:X{n}:POSition?")
    _send(resource_name, f":CURSor:XY:X{n}:POSition {value}")
    return None


def cursor_xy_y_state(resource_name: str, n: int, state: bool | None = None) -> str | None:
    """Set or query the XY Y cursor ``n`` on/off state.

    SCPI: :CURSor:XY:Y<n> {ON|OFF}

    Args:
        n: XY Y cursor index (1-4)
        state: True=ON, False=OFF
    """
    if state is None:
        return _query(resource_name, f":CURSor:XY:Y{n}?")
    _send(resource_name, f":CURSor:XY:Y{n} {'ON' if state else 'OFF'}")
    return None


def cursor_xy_y_color(resource_name: str, n: int, color: str | None = None) -> str | None:
    """Set or query the XY Y cursor ``n`` color.

    SCPI: :CURSor:XY:Y<n>:COLor <color>
    """
    if color is None:
        return _query(resource_name, f":CURSor:XY:Y{n}:COLor?")
    _send(resource_name, f":CURSor:XY:Y{n}:COLor {color}")
    return None


def cursor_xy_y_dfollow(resource_name: str, n: int, enable: bool | None = None) -> str | None:
    """Set or query whether XY Y cursor ``n`` follows reference cursor.

    SCPI: :CURSor:XY:Y<n>:DFOLlow {ON|OFF}
    """
    if enable is None:
        return _query(resource_name, f":CURSor:XY:Y{n}:DFOLlow?")
    _send(resource_name, f":CURSor:XY:Y{n}:DFOLlow {'ON' if enable else 'OFF'}")
    return None


def cursor_xy_y_dtcursor(resource_name: str, n: int, ref_cursor: str | None = None) -> str | None:
    """Set or query the reference cursor for XY Y cursor ``n``.

    SCPI: :CURSor:XY:Y<n>:DTCursor <source>
    """
    if ref_cursor is None:
        return _query(resource_name, f":CURSor:XY:Y{n}:DTCursor?")
    _send(resource_name, f":CURSor:XY:Y{n}:DTCursor {ref_cursor}")
    return None


def cursor_xy_y_dvalue(resource_name: str, n: int, value: float | None = None) -> str | None:
    """Set or query XY Y cursor ``n`` position relative to reference cursor.

    SCPI: :CURSor:XY:Y<n>:DVALue <value>
    """
    if value is None:
        return _query(resource_name, f":CURSor:XY:Y{n}:DVALue?")
    _send(resource_name, f":CURSor:XY:Y{n}:DVALue {value}")
    return None


def cursor_xy_y_label(resource_name: str, n: int, label: str | None = None) -> str | None:
    """Set or query the label for XY Y cursor ``n``.

    SCPI: :CURSor:XY:Y<n>:LABel <state>
    """
    if label is None:
        return _query(resource_name, f":CURSor:XY:Y{n}:LABel?")
    _send(resource_name, f":CURSor:XY:Y{n}:LABel {label}")
    return None


def cursor_xy_y_position(resource_name: str, n: int, value: float | None = None) -> str | None:
    """Set or query XY Y cursor ``n`` absolute position.

    SCPI: :CURSor:XY:Y<n>:POSition <value>
    """
    if value is None:
        return _query(resource_name, f":CURSor:XY:Y{n}:POSition?")
    _send(resource_name, f":CURSor:XY:Y{n}:POSition {value}")
    return None
