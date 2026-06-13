"""HISTORy subsystem SCPI commands."""

from __future__ import annotations

from _base import _send, _query


def history_state(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query history waveform on/off state.

        Configures the history waveform display on/off state.
        ON  — enable history waveform playback
        OFF — disable history waveform playback
    """
    if state is None:
        return _query(resource_name, ":HISTORy?")
    _send(resource_name, f":HISTORy {'ON' if state else 'OFF'}")
    return None


def history_frame(resource_name: str, frame: int | None = None) -> str | None:
    """Set or query current history frame number."""
    if frame is None:
        return _query(resource_name, ":HISTORy:FRAMe?")
    _send(resource_name, f":HISTORy:FRAMe {frame}")
    return None


def history_interval(resource_name: str, interval: float | None = None) -> str | None:
    """Set or query history playback interval [1.00E-06, 1] s."""
    if interval is None:
        return _query(resource_name, ":HISTORy:INTERval?")
    _send(resource_name, f":HISTORy:INTERval {interval}")
    return None


def history_list(resource_name: str, state: str | None = None) -> str | None:
    """Set or query history list state {OFF|ON[,TIME|DELTa]}."""
    if state is None:
        return _query(resource_name, ":HISTORy:LIST?")
    _send(resource_name, f":HISTORy:LIST {state}")
    return None


def history_play(resource_name: str, direction: str | None = None) -> str | None:
    """Set or query history playback state {BACKWards|PAUSe|FORWards}."""
    if direction is None:
        return _query(resource_name, ":HISTORy:PLAY?")
    _send(resource_name, f":HISTORy:PLAY {direction}")
    return None


def history_time(resource_name: str, time: str | None = None) -> str | None:
    """Set or query the history frame timestamp.

    SCPI: :HISTORy:TIME <time>
           :HISTORy:TIME?

    Args:
        time: Timestamp string 'YYYY-MM-DD HH:MM:SS' to jump to, or None to query

    Returns:
        Current timestamp (HH:MM:SS.μs) when querying.
    """
    if time is None:
        return _query(resource_name, ":HISTORy:TIME?")
    _send(resource_name, f":HISTORy:TIME {time}")
    return None
