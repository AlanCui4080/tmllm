'''ACQuire subsystem SCPI commands.'''

from __future__ import annotations
from _base import _send, _query


def acquire_type(resource_name: str, acq_type: str | None = None) -> str | None:
    """Set or query the acquisition type (sampling mode).

    SCPI: :ACQuire:TYPE <type>
           :ACQuire:TYPE?

        Configures the oscilloscope acquisition type (sampling mode).
        NORMal — standard real-time sampling without averaging
        PEAK   — peak detect mode, captures extreme values at highest speed
        AVERage[,<times>] — averaging mode, <times> selects number of averages (4~8192, power of 2)
        ERES[,<bits>] — enhanced resolution mode, <bits> selects resolution (0.5~4.0)

    Args:
        acq_type: {NORMal|PEAK|AVERage[,<times>]|ERES[,<bits>]}
            Pass e.g. "AVERage,16" for averaging with 16 times.
        None — query current type

    Returns:
        Current acquisition type string when querying.
        Example return value: AVERage,16
    """
    if acq_type is None:
        return _query(resource_name, ":ACQuire:TYPE?")
    _send(resource_name, f":ACQuire:TYPE {acq_type}")
    return None


def acquire_mode(resource_name: str, mode: str | None = None) -> str | None:
    """Set or query the oscilloscope display mode.

    SCPI: :ACQuire:MODE <mode_type>
           :ACQuire:MODE?

        Configures the waveform display mode.
        YT   — amplitude (Y) vs. time (T), the default view
        XY   — channel X vs. channel Y (Lissajous curve)
        ROLL — rolling mode, waveform scrolls from right to left

    Args:
        mode: {YT|XY|ROLL}

    Returns:
        Current mode when querying.
    """
    if mode is None:
        return _query(resource_name, ":ACQuire:MODE?")
    _send(resource_name, f":ACQuire:MODE {mode}")
    return None


def acquire_mdepth(resource_name: str, depth: str | None = None) -> str | None:
    """Set or query the memory depth.

    SCPI: :ACQuire:MDEPth <depth>
           :ACQuire:MDEPth?

        Configures the memory depth, which determines how many sample points can be stored in a single acquisition.
        Available values depend on the current timebase and channel configuration.

    Args:
        depth: e.g. "10K","100K","1M","10M","100M"

    Returns:
        Current memory depth when querying (e.g. "1M").
    """
    if depth is None:
        return _query(resource_name, ":ACQuire:MDEPth?")
    _send(resource_name, f":ACQuire:MDEPth {depth}")
    return None


def acquire_srate(resource_name: str, rate: str | None = None) -> str | None:
    """Set or query the sample rate.

    SCPI: :ACQuire:SRATe <rate>
           :ACQuire:SRATe?

        Configures the sample rate, which sets the number of samples captured per second.
        Example — set sample rate to 5 GSa/s: ACQ:SRAT 5.00E9

    Args:
        rate: Sample rate as string, e.g. "1e9" for 1 GSa/s, "5.00E9" for 5 GSa/s

    Returns:
        Current sample rate when querying (e.g. "5.00E+09").
    """
    if rate is None:
        return _query(resource_name, ":ACQuire:SRATe?")
    _send(resource_name, f":ACQuire:SRATe {rate}")
    return None


def acquire_interpolation(resource_name: str, interp: str | None = None) -> str | None:
    """Set or query the interpolation method.

    SCPI: :ACQuire:INTerpolation <state>
           :ACQuire:INTerpolation?

        Configures the interpolation method used to reconstruct the waveform horizontally.
        ON  — sin(x)/x interpolation for smoother display
        OFF — linear interpolation between sample points

    Args:
        interp: {ON|OFF}

    Returns:
        Current interpolation method when querying.
    """
    if interp is None:
        return _query(resource_name, ":ACQuire:INTerpolation?")
    _send(resource_name, f":ACQuire:INTerpolation {interp}")
    return None


def acquire_amode(resource_name: str, amode: str | None = None) -> str | None:
    """Set or query the acquisition filling mode (acquisition mode of waveform).

    SCPI: :ACQuire:AMODe <mode>
           :ACQuire:AMODe?

        Configures the waveform acquisition filling mode.
        FAST — fast waveform acquisition
        SLOW — slow waveform acquisition

    Args:
        amode: {FAST|SLOW}

    Returns:
        Current acquisition mode when querying.
    """
    if amode is None:
        return _query(resource_name, ":ACQuire:AMODe?")
    _send(resource_name, f":ACQuire:AMODe {amode}")
    return None


def acquire_numacq(resource_name: str) -> str | None:
    """Query the number of acquired waveform frames.

    SCPI: :ACQuire:NUMACq?

        Queries the number of waveform frames that have been acquired. This counter resets to zero whenever a horizontal or vertical parameter change occurs.

    Returns:
        Number of acquired frames as integer string.
    """
    return _query(resource_name, ":ACQuire:NUMACq?")


def acquire_resolution(resource_name: str, bits: str | None = None) -> str | None:
    """Set or query the ADC resolution.

    SCPI: :ACQuire:RESolution <bit>
           :ACQuire:RESolution?

        Configures the ADC resolution of the oscilloscope.
        <bit>:= {8Bits|10Bits}

    Args:
        bits: {8Bits|10Bits}

    Returns:
        Current ADC resolution when querying.
    """
    if bits is None:
        return _query(resource_name, ":ACQuire:RESolution?")
    _send(resource_name, f":ACQuire:RESolution {bits}")
    return None


def acquire_sequence(resource_name: str, enable: bool | None = None) -> str | None:
    """Set or query sequence (segmented) acquisition mode.

    SCPI: :ACQuire:SEQuence {ON|OFF}
           :ACQuire:SEQuence?

        Enables or disables segmented (sequence) acquisition mode. Segmented acquisition divides the memory depth into multiple segments, each capturing one trigger event.
        Note: averaging and ERES modes are unavailable when sequence mode is active.

    Args:
        enable: True=ON (enable sequence mode), False=OFF
        None — query

    Returns:
        "ON" or "OFF" when querying.
    """
    if enable is None:
        return _query(resource_name, ":ACQuire:SEQuence?")
    _send(resource_name, f":ACQuire:SEQuence {'ON' if enable else 'OFF'}")
    return None


def acquire_sequence_count(resource_name: str, count: int | None = None) -> str | None:
    """Set or query the number of segments in sequence mode.

    SCPI: :ACQuire:SEQuence:COUNt <count>
           :ACQuire:SEQuence:COUNt?

        Configures the number of segments used in sequence acquisition mode. Effective only when sequence mode is enabled.

    Args:
        count: Number of segments (2 to max, model-dependent)

    Returns:
        Current segment count when querying.
    """
    if count is None:
        return _query(resource_name, ":ACQuire:SEQuence:COUNt?")
    _send(resource_name, f":ACQuire:SEQuence:COUNt {count}")
    return None


def acquire_mmanagement(resource_name: str, mode: str | None = None) -> str | None:
    """Set or query the memory management mode.

    SCPI: :ACQuire:MMANagement <mem_mode>
           :ACQuire:MMANagement?

        Configures the memory management strategy.
        AUTO    — automatically selects both memory depth and sample rate
        FSRate  — fixed sample rate; memory depth is set automatically
        FMDepth — fixed memory depth; sample rate is set automatically

    Args:
        mode: {AUTO|FSRate|FMDepth}

    Returns:
        Current management mode when querying.
    """
    if mode is None:
        return _query(resource_name, ":ACQuire:MMANagement?")
    _send(resource_name, f":ACQuire:MMANagement {mode}")
    return None


def acquire_points(resource_name: str) -> str | None:
    """Query the number of sample points on the current waveform.

    SCPI: :ACQuire:POINts?

        Queries the number of sample points on the current screen waveform.

    Returns:
        Sample points as float string (e.g. "1.25E+08").
    """
    return _query(resource_name, ":ACQuire:POINts?")


def acquire_csweep(resource_name: str) -> None:
    """Clear the acquisition sweeps and restart acquisition.

    SCPI: :ACQuire:CSWeep

        Clears the acquisition sweeps and restarts acquisition. Equivalent to the front-panel Clear Sweeps button. This is an action command with no parameters and no query form.
    """
    _send(resource_name, ":ACQuire:CSWeep")
    return None
