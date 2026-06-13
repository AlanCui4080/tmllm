"""DISPlay subsystem SCPI commands."""

from __future__ import annotations

from _base import _send, _query


def display_axis(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query the axis label display state.

    SCPI: :DISPlay:AXIS {ON|OFF}
           :DISPlay:AXIS?

        Configures the axis label display state.
        ON  — show axis labels
        OFF — hide axis labels

    Args:
        state: True=ON, False=OFF

    Returns:
        "ON" or "OFF" when querying.
    """
    if state is None:
        return _query(resource_name, ":DISPlay:AXIS?")
    _send(resource_name, f":DISPlay:AXIS {'ON' if state else 'OFF'}")
    return None


def display_axis_mode(resource_name: str, mode: str | None = None) -> str | None:
    """Set or query the axis label display mode.

    SCPI: :DISPlay:AXIS:MODE <mode>
           :DISPlay:AXIS:MODE?

        Configures the axis label display mode.
        FIXed — fixed mode: axis stays in place, coordinates update with waveform movement
        MOVing — moving mode: axis follows waveform movement, coordinates stay fixed

    Args:
        mode: {FIXed|MOVing}

    Returns:
        Current axis mode when querying.
    """
    if mode is None:
        return _query(resource_name, ":DISPlay:AXIS:MODE?")
    _send(resource_name, f":DISPlay:AXIS:MODE {mode}")
    return None


def display_axis_position(resource_name: str, pos: str | None = None) -> str | None:
    """Set or query the vertical axis label position.

    SCPI: :DISPlay:AXIS:POSition <pos>
           :DISPlay:AXIS:POSition?

        Configures the vertical position of the axis labels.
        LEFT  — vertical axis on the left side of the screen
        MIDDle — vertical axis in the center of the screen
        RIGHt — vertical axis on the right side of the screen

    Args:
        pos: {LEFT|MIDDle|RIGHt}

    Returns:
        Current axis position when querying.
    """
    if pos is None:
        return _query(resource_name, ":DISPlay:AXIS:POSition?")
    _send(resource_name, f":DISPlay:AXIS:POSition {pos}")
    return None


def display_backlight(resource_name: str, brightness: int | None = None) -> str | None:
    """Set or query the screen backlight brightness.

    SCPI: :DISPlay:BACKlight <value>
           :DISPlay:BACKlight?

        Configures the screen backlight brightness.
        <value>:= percentage [0,100]

    Args:
        brightness: Backlight percentage (0-100)

    Returns:
        Current brightness percentage when querying.
    """
    if brightness is None:
        return _query(resource_name, ":DISPlay:BACKlight?")
    _send(resource_name, f":DISPlay:BACKlight {brightness}")
    return None


def display_clear(resource_name: str) -> None:
    """Clear the waveform display on screen.

    SCPI: :DISPlay:CLEar

        Clears the waveform display on screen.

    Associated commands: :ACQuire:CSWeep
    """
    _send(resource_name, ":DISPlay:CLEar")


def display_color(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query the color temperature display state.

    SCPI: :DISPlay:COLor {ON|OFF}
           :DISPlay:COLor?

        Configures the color temperature display state.
        ON  — enable color temperature visualization
        OFF — disable color temperature visualization

    Args:
        state: True=ON, False=OFF

    Returns:
        "ON" or "OFF" when querying.
    """
    if state is None:
        return _query(resource_name, ":DISPlay:COLor?")
    _send(resource_name, f":DISPlay:COLor {'ON' if state else 'OFF'}")
    return None


def display_graticule(resource_name: str, brightness: int | None = None) -> str | None:
    """Set or query the graticule (grid) brightness.

    SCPI: :DISPlay:GRATicule <value>
           :DISPlay:GRATicule?

        Configures the graticule (grid) brightness.
        <value>:= percentage [0,100]

    Args:
        brightness: Graticule brightness percentage (0-100)

    Returns:
        Current grid brightness when querying.
    """
    if brightness is None:
        return _query(resource_name, ":DISPlay:GRATicule?")
    _send(resource_name, f":DISPlay:GRATicule {brightness}")
    return None


def display_grid_style(resource_name: str, style: str | None = None) -> str | None:
    """Set or query the grid display style.

    SCPI: :DISPlay:GRIDstyle <type>
           :DISPlay:GRIDstyle?

        Configures the grid display style.
        FULL  — full grid: 8 rows x 10 columns
        LIGHt — light grid: screen divided into four quadrants
        NONE  — no grid

    Args:
        style: {FULL|LIGHt|NONE}

    Returns:
        Current grid style when querying.
    """
    if style is None:
        return _query(resource_name, ":DISPlay:GRIDstyle?")
    _send(resource_name, f":DISPlay:GRIDstyle {style}")
    return None


def display_hidemenu(resource_name: str) -> None:
    """Hide the right-side menu.

    SCPI: :DISPlay:HIDemenu

        Hides the right-side menu.

    Associated commands: :DISPlay:MENU:HIDE
    """
    _send(resource_name, ":DISPlay:HIDemenu")


def display_intensity(resource_name: str, intensity: int | None = None) -> str | None:
    """Set or query the waveform brightness.

    SCPI: :DISPlay:INTensity <value>
           :DISPlay:INTensity?

        Configures the waveform trace brightness.
        <value>:= percentage [0,100]

    Args:
        intensity: Waveform brightness percentage (0-100)

    Returns:
        Current waveform brightness when querying.
    """
    if intensity is None:
        return _query(resource_name, ":DISPlay:INTensity?")
    _send(resource_name, f":DISPlay:INTensity {intensity}")
    return None


def display_menu(resource_name: str, style: str | None = None) -> str | None:
    """Set or query the menu display style.

    SCPI: :DISPlay:MENU <type>
           :DISPlay:MENU?

        Configures the menu display style.
        EMBedded — embedded style
        FLOating — floating style

    Args:
        style: {EMBedded|FLOating}

    Returns:
        Current menu style when querying.
    """
    if style is None:
        return _query(resource_name, ":DISPlay:MENU?")
    _send(resource_name, f":DISPlay:MENU {style}")
    return None


def display_menu_hide(resource_name: str, time: str | None = None) -> str | None:
    """Set or query the menu auto-hide timeout.

    SCPI: :DISPlay:MENU:HIDE <time>
           :DISPlay:MENU:HIDE?

        Configures the menu auto-hide timeout.
        OFF — disable auto-hide
        3S|5S|10S|30S|60S — hide menu after specified delay

    Args:
        time: {OFF|3S|5S|10S|30S|60S}

    Returns:
        Current auto-hide time when querying.
    """
    if time is None:
        return _query(resource_name, ":DISPlay:MENU:HIDE?")
    _send(resource_name, f":DISPlay:MENU:HIDE {time}")
    return None


def display_persistence(resource_name: str, time: str | None = None) -> str | None:
    """Set or query the persistence display time.

    SCPI: :DISPlay:PERSistence <time>
           :DISPlay:PERSistence?

        Configures the persistence display time.
        Model-dependent values:
          SDS7000A/6000/3000/2000X HD: {OFF|INFinite|100MS|200MS|500MS|1S|5S|10S|30S}
          SDS2000X Plus/SHS/1000X HD/800X HD: {OFF|INFinite|1S|5S|10S|30S}

    Args:
        time: Persistence time (e.g. "10S", "OFF", "INFinite")

    Returns:
        Current persistence time when querying.
    """
    if time is None:
        return _query(resource_name, ":DISPlay:PERSistence?")
    _send(resource_name, f":DISPlay:PERSistence {time}")
    return None


def display_transparence(resource_name: str, value: int | None = None) -> str | None:
    """Set or query the info box transparency (SHS800X/SHS1000X only).

    SCPI: :DISPlay:TRANsparence <value>
           :DISPlay:TRANsparence?

        Configures the transparency of info boxes (e.g. cursor info display).
        Applies to SHS800X/SHS1000X models only.

    Args:
        value: Transparency percentage (0-100)

    Returns:
        Current transparency when querying.
    """
    if value is None:
        return _query(resource_name, ":DISPlay:TRANsparence?")
    _send(resource_name, f":DISPlay:TRANsparence {value}")
    return None


def display_type(resource_name: str, draw_type: str | None = None) -> str | None:
    """Set or query the waveform display type.

    SCPI: :DISPlay:TYPE <type>
           :DISPlay:TYPE?

        Configures the waveform display type.
        VECTor — vector mode: sample points connected by lines
        DOT    — dot mode: raw sample points displayed directly

    Args:
        draw_type: {VECTor|DOT}

    Returns:
        Current display type when querying.
    """
    if draw_type is None:
        return _query(resource_name, ":DISPlay:TYPE?")
    _send(resource_name, f":DISPlay:TYPE {draw_type}")
    return None
