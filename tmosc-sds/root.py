"""Root-level SCPI commands (:AUToset, :PRINt, :FORMat:DATA)."""

from __future__ import annotations

from _base import _send, _query


def autoset(resource_name: str) -> None:
    """Run auto-setup to automatically configure the oscilloscope.

    SCPI: :AUToset

    Auto-setup automatically configures the vertical scale, timebase,
    and trigger system based on the characteristics of the input signal.
    """
    _send(resource_name, ":AUToset")


def print_screen(resource_name: str, img_type: str = "BMP", invert: str = "NORMal") -> bytes:
    """Print the screen (capture screenshot via SCPI).

    SCPI: :PRINt? <type>[,<format>]

        Executes the screen print function and returns the current screenshot data.

    Args:
        img_type: {BMP|PNG} — image format
        invert: {NORMal|INVerted} — color inversion

    Returns:
        Raw binary screenshot data.
    """
    from _base import _query_raw
    cmd = f":PRINt? {img_type},{invert}"
    return _query_raw(resource_name, cmd)


def format_data(resource_name: str, option: str | None = None, digit: int = 3) -> str | None:
    """Set or query the NR3 return-value precision.

    SCPI: :FORMat:DATA <option>[,<digit>]
           :FORMat:DATA?

        Configures the NR3 return-value precision. Default format is SINGle.
        SINGle — 7 significant digits
        DOUBle — 14 significant digits
        CUSTom[,<digit>] — custom significant digits, <digit> range [1,64]

    Args:
        option: {SINGle|DOUBle|CUSTom}
        digit: Custom significant digits (1-64), only used with CUSTom
        None — query current format

    Returns:
        Current format string when querying (e.g. "SINGle"), None when setting.
    """
    if option is None:
        return _query(resource_name, ":FORMat:DATA?")
    if option == "CUSTom":
        _send(resource_name, f":FORMat:DATA CUSTom,{digit}")
    else:
        _send(resource_name, f":FORMat:DATA {option}")
    return None
