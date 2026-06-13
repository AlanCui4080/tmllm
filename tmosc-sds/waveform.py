"""WAVeform subsystem SCPI commands."""

from __future__ import annotations

from _base import _send, _query, _query_raw


def waveform_byteorder(resource_name: str, order: str | None = None) -> str | None:
    """Set or query the byte order for waveform data transfer (16-bit).

    SCPI: :WAVeform:BYTeorder <order>
           :WAVeform:BYTeorder?

        Configures the byte order for waveform data transfer (16-bit mode).
        Byte order must be set when waveform data is transferred as 16-bit words;
        default is LSB.
        MSB — most significant byte first
        LSB — least significant byte first

    Args:
        order: {MSB|LSB}

    Returns:
        Current byte order when querying.

    Associated commands: :WAVeform:WIDTh
    """
    if order is None:
        return _query(resource_name, ":WAVeform:BYTeorder?")
    _send(resource_name, f":WAVeform:BYTeorder {order}")
    return None


def waveform_source(resource_name: str, source: str | None = None) -> str | None:
    """Set or query the waveform data source for transfer.

    SCPI: :WAVeform:SOURce <source>
           :WAVeform:SOURce?

        Configures the waveform data source for transfer.
        <source>:= {C<n>|F<x>|D<d>}
          C<n>: analog channels (C1-C4)
          F<x>: math functions
          D<d>: digital channels

    Args:
        source: Waveform source (e.g. "C1", "F1")

    Returns:
        Current source when querying.

    Associated commands: :WAVeform:DATA, :WAVeform:PREamble
    """
    if source is None:
        return _query(resource_name, ":WAVeform:SOURce?")
    _send(resource_name, f":WAVeform:SOURce {source}")
    return None


def waveform_start(resource_name: str, start: int | None = None) -> str | None:
    """Set or query the waveform data start point (0-indexed).

    SCPI: :WAVeform:STARt <value>
           :WAVeform:STARt?

        Configures the start point for waveform data transfer.
        Note: the valid range depends on the waveform point count and
        the :WAVeform:POINt setting.

    Args:
        start: Start point index (NR1)

    Returns:
        Current start point when querying.

    Associated commands: :WAVeform:POINt
    """
    if start is None:
        return _query(resource_name, ":WAVeform:STARt?")
    _send(resource_name, f":WAVeform:STARt {start}")
    return None


def waveform_interval(resource_name: str, interval: int | None = None) -> str | None:
    """Set or query the waveform data point interval (decimation).

    SCPI: :WAVeform:INTerval <value>
           :WAVeform:INTerval?

        Configures the waveform data point interval for transfer.
        Note: the valid range depends on :WAVeform:STARt and
        :WAVeform:POINt settings.

    Args:
        interval: Point interval (NR1, 1 = every point, 2 = every other point, etc.)

    Returns:
        Current interval when querying.

    Associated commands: :WAVeform:STARt, :WAVeform:POINt
    """
    if interval is None:
        return _query(resource_name, ":WAVeform:INTerval?")
    _send(resource_name, f":WAVeform:INTerval {interval}")
    return None


def waveform_points(resource_name: str, points: int | None = None) -> str | None:
    """Set or query the number of waveform data points to transfer.

    SCPI: :WAVeform:POINt <value>
           :WAVeform:POINt?

        Configures the number of points to transfer in a single operation.
        Note: the valid range depends on the current waveform point count.

    Args:
        points: Number of points to transfer (NR1)

    Returns:
        Current point count when querying.

    Associated commands: :ACQuire:POINts
    """
    if points is None:
        return _query(resource_name, ":WAVeform:POINt?")
    _send(resource_name, f":WAVeform:POINt {points}")
    return None


def waveform_maxpoint(resource_name: str) -> str:
    """Query the maximum points per single data chunk.

    SCPI: :WAVeform:MAXPoint?

        Due to oscilloscope memory constraints, some models require reading
        waveform data in multiple chunks. This command queries the maximum
        number of data points that can be retrieved in one chunk.

    Returns:
        Maximum points per chunk (NR1).
    """
    return _query(resource_name, ":WAVeform:MAXPoint?")


def waveform_width(resource_name: str, width: str | None = None) -> str | None:
    """Set or query the waveform data transfer width.

    SCPI: :WAVeform:WIDTh <type>
           :WAVeform:WIDTh?

        Configures the waveform data transfer format.
        BYTE — 8-bit byte transfer
        WORD — 16-bit data transferred as two bytes, default LSB
        Note: when reading waveform data wider than 8 bits, WORD mode must be used.

    Args:
        width: {BYTE|WORD}

    Returns:
        Current width when querying.
    """
    if width is None:
        return _query(resource_name, ":WAVeform:WIDTh?")
    _send(resource_name, f":WAVeform:WIDTh {width}")
    return None


def waveform_preamble(resource_name: str) -> bytes:
    """Query the waveform preamble (parameters) for the current source.

    SCPI: :WAVeform:PREamble?

        Queries the waveform parameters for the source selected by
        :WAVeform:SOURce. Returns a binary data block with header #9<9-Digits>.
        Contents include: point count, vertical scale, vertical offset,
        sample interval, horizontal delay, and other metadata.

    Returns:
        Binary preamble data block (346 bytes after the #9 header).

    Associated commands: :WAVeform:SOURce
    """
    return _query_raw(resource_name, ":WAVeform:PREamble?")


def waveform_data(resource_name: str) -> bytes:
    """Query the waveform data for the current source.

    SCPI: :WAVeform:DATA?

        Reads the waveform data for the source selected by :WAVeform:SOURce.
        Returns a binary data block with TMC header (#<Digits><ByteLen>).
        Each point is 1 byte (BYTE mode) or 2 bytes (WORD mode).

    Note:
        Before calling this, set the source via :WAVeform:SOURce and
        configure points/start/interval/width as needed.

    Returns:
        Binary waveform data block (TMC header + raw data).

    Associated commands: :WAVeform:SOURce, :WAVeform:PREamble, :WAVeform:WIDTh
    """
    return _query_raw(resource_name, ":WAVeform:DATA?")


def waveform_sequence(resource_name: str, frame: int | None = None, start: int = 1) -> str | None:
    """Set or query the sequence waveform frame for segmented acquisition.

    SCPI: :WAVeform:SEQuence <value1>,<value2>
           :WAVeform:SEQuence?

        Configures which waveform frame to read in segmented acquisition mode.
        <value1> — frame number: 0 = return all frames, N = specific frame
        <value2> — starting frame number for chunked read when value1=0

    Args:
        frame: Frame number (0 for all frames, N for specific), None to query
        start: Starting frame for chunked read when frame=0

    Returns:
        Current sequence setting "value1,value2" when querying.
    """
    if frame is None:
        return _query(resource_name, ":WAVeform:SEQuence?")
    _send(resource_name, f":WAVeform:SEQuence {frame},{start}")
    return None


# ═══════════════════════════════════════════════════════════════════
#  WaveGen (built-in AWG) passthrough commands
# ═══════════════════════════════════════════════════════════════════

def wavegen_output(resource_name: str, state: bool) -> None:
    """Enable/disable the built-in waveform generator output.

    SCPI: OUTPut {ON|OFF}
    """
    _send(resource_name, f"OUTPut {'ON' if state else 'OFF'}")


def wavegen_basic_wave(resource_name: str, wave: str) -> None:
    """Set the built-in waveform generator function.

    SCPI: FUNCtion <wave>
    """
    _send(resource_name, f"FUNCtion {wave}")


def wavegen_frequency(resource_name: str, freq: float) -> None:
    """Set the built-in waveform generator frequency in Hz.

    SCPI: FREQuency <freq>
    """
    _send(resource_name, f"FREQuency {freq}")


def wavegen_amplitude(resource_name: str, amp: float) -> None:
    """Set the built-in waveform generator amplitude (Vpp).

    SCPI: VOLTage <amp>
    """
    _send(resource_name, f"VOLTage {amp}")


def wavegen_offset(resource_name: str, offset: float) -> None:
    """Set the built-in waveform generator DC offset in volts.

    SCPI: VOLTage:OFFSet <offset>
    """
    _send(resource_name, f"VOLTage:OFFSet {offset}")


def wavegen_duty_cycle(resource_name: str, duty: float) -> None:
    """Set the built-in waveform generator square wave duty cycle (0-100%).

    SCPI: FUNCtion:SQUare:DCYCle <duty>
    """
    _send(resource_name, f"FUNCtion:SQUare:DCYCle {duty}")
