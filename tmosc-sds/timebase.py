"""TIMebase subsystem SCPI commands."""

from __future__ import annotations

from _base import _send, _query


def timebase_delay(resource_name: str, delay: float | None = None) -> str | None:
    """Set or query the horizontal trigger delay.

    SCPI: :TIMebase:DELay <delay_value>
           :TIMebase:DELay?

        Configures the horizontal trigger delay.

    Args:
        delay: Delay value in seconds (NR3, e.g. 1.00E-05 for 10µs)

    Returns:
        Current delay when querying.

    Associated commands: :TIMebase:SCALe
    """
    if delay is None:
        return _query(resource_name, ":TIMebase:DELay?")
    _send(resource_name, f":TIMebase:DELay {delay}")
    return None


def timebase_reference(resource_name: str, ref_type: str | None = None) -> str | None:
    """Set or query the horizontal expansion reference strategy.

    SCPI: :TIMebase:REFerence <type>
           :TIMebase:REFerence?

        Configures the horizontal expansion reference strategy.
        DELay   — delay fixed: horizontal delay value stays constant when timebase changes. The horizontal reference point position can be set; the delay value centers on that point.
        POSition — position fixed: delay stays at a fixed grid position when timebase changes.

    Args:
        ref_type: {DELay|POSition}

    Returns:
        Current reference type when querying.
    """
    if ref_type is None:
        return _query(resource_name, ":TIMebase:REFerence?")
    _send(resource_name, f":TIMebase:REFerence {ref_type}")
    return None


def timebase_reference_position(resource_name: str, position: int | None = None) -> str | None:
    """Set or query the horizontal reference center position (0-100%).

    SCPI: :TIMebase:REFerence:POSition <value>
           :TIMebase:REFerence:POSition?

        When the reference strategy is DELay, configures the horizontal reference center position.
        <value>:= percentage [0,100]

    Args:
        position: Reference position percentage (0-100)

    Returns:
        Current reference position when querying.

    Associated commands: :TIMebase:REFerence
    """
    if position is None:
        return _query(resource_name, ":TIMebase:REFerence:POSition?")
    _send(resource_name, f":TIMebase:REFerence:POSition {position}")
    return None


def timebase_scale(resource_name: str, scale: float | None = None) -> str | None:
    """Set or query the main window timebase (s/div).

    SCPI: :TIMebase:SCALe <value>
           :TIMebase:SCALe?

        Configures the main window timebase.
        Note: timebase range varies by model. Refer to the data sheet for details. When decreasing the timebase, the oscilloscope automatically matches the fastest available setting.

    Args:
        scale: Timebase scale in seconds/div (NR3, e.g. 1.00E-07 for 100ns/div)

    Returns:
        Current timebase when querying.

    Associated commands: :TIMebase:DELay
    """
    if scale is None:
        return _query(resource_name, ":TIMebase:SCALe?")
    _send(resource_name, f":TIMebase:SCALe {scale}")
    return None


def timebase_window(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query the Zoom window on/off state.

    SCPI: :TIMebase:WINDow {ON|OFF}
           :TIMebase:WINDow?

        Configures the Zoom window on/off state.

    Args:
        state: True=ON, False=OFF

    Returns:
        "ON" or "OFF" when querying.

    Associated commands: :TIMebase:WINDow:DELay, :TIMebase:WINDow:SCALe
    """
    if state is None:
        return _query(resource_name, ":TIMebase:WINDow?")
    _send(resource_name, f":TIMebase:WINDow {'ON' if state else 'OFF'}")
    return None


def timebase_window_delay(resource_name: str, delay: float | None = None) -> str | None:
    """Set or query the Zoom window horizontal delay.

    SCPI: :TIMebase:WINDow:DELay <delay_value>
           :TIMebase:WINDow:DELay?

        Configures the Zoom window horizontal delay.
        Note: the main window timebase and delay together determine the Zoom window delay range. The Zoom window must stay within the main window bounds. Values outside the range are clamped to the nearest available setting.

    Args:
        delay: Zoom window delay in seconds (NR3)

    Returns:
        Current Zoom window delay when querying.

    Associated commands: :TIMebase:WINDow:SCALe, :TIMebase:SCALe, :TIMebase:DELay
    """
    if delay is None:
        return _query(resource_name, ":TIMebase:WINDow:DELay?")
    _send(resource_name, f":TIMebase:WINDow:DELay {delay}")
    return None


def timebase_window_scale(resource_name: str, scale: float | None = None) -> str | None:
    """Set or query the Zoom window timebase (s/div).

    SCPI: :TIMebase:WINDow:SCALe <scale_value>
           :TIMebase:WINDow:SCALe?

        Configures the Zoom window timebase.
        Note: the Zoom window timebase cannot exceed the main window timebase. If it does, it is automatically clamped to match.

    Args:
        scale: Zoom window timebase in seconds/div (NR3)

    Returns:
        Current Zoom window timebase when querying.

    Associated commands: :TIMebase:WINDow:DELay, :TIMebase:SCALe, :TIMebase:DELay
    """
    if scale is None:
        return _query(resource_name, ":TIMebase:WINDow:SCALe?")
    _send(resource_name, f":TIMebase:WINDow:SCALe {scale}")
    return None
