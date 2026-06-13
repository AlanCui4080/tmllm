"""CHANnel subsystem SCPI commands."""
from __future__ import annotations
from _base import _send, _query


def channel_reference_type(resource_name: str, ref_type: str | None = None) -> str | None:
    """Set or query the vertical reference strategy for all channels.

    SCPI: :CHANnel:REFerence <type>

        Configures the vertical reference strategy used during scale changes.
        OFFSet   — voltage offset stays fixed when the vertical scale changes; the waveform expands/contracts around the main X-axis of the screen.
        POSition — grid position stays fixed when the vertical scale changes; the waveform expands/contracts around a fixed screen location.

    Args:
        ref_type: {OFFSet|POSition}

    Returns:
        Current reference type when querying.
    """
    if ref_type is None:
        return _query(resource_name, ":CHANnel:REFerence?")
    _send(resource_name, f":CHANnel:REFerence {ref_type}")
    return None


def channel_display(resource_name: str, channel: int, show: bool | None = None) -> str | None:
    """Set or query channel display (trace on/off).

    SCPI: :CHANnel<n>:SWITch {ON|OFF}
           :CHANnel<n>:VISible {ON|OFF}

        Configures the display state (trace on/off) for the specified channel.

    Args:
        channel: Channel number (1-4)
        show: True=ON (show trace), False=OFF (hide trace)
        None — query

    Returns:
        "ON" or "OFF" when querying.
    """
    if show is None:
        return _query(resource_name, f":CHANnel{channel}:SWITch?")
    val = "ON" if show else "OFF"
    _send(resource_name, f":CHANnel{channel}:SWITch {val}")
    if show:
        _send(resource_name, f":CHANnel{channel}:VISible ON")
    return None


def channel_coupling(resource_name: str, channel: int, coupling: str | None = None) -> str | None:
    """Set or query the input coupling for a channel.

    SCPI: :CHANnel<n>:COUPling <coupling>

        Configures the input coupling for the specified channel.
        AC  — AC coupling, blocks DC component
        DC  — DC coupling, passes all signal components
        GND — ground, disconnects input for zero-reference

    Args:
        channel: Channel number (1-4)
        coupling: {AC|DC|GND}

    Returns:
        Current coupling when querying.
    """
    if coupling is None:
        return _query(resource_name, f":CHANnel{channel}:COUPling?")
    _send(resource_name, f":CHANnel{channel}:COUPling {coupling}")
    return None


def channel_bwlimit(resource_name: str, channel: int, bwlimit: str | None = None) -> str | None:
    """Set or query the bandwidth limit for a channel.

    SCPI: :CHANnel<n>:BWLimit <bwlimit>

        Configures the bandwidth limit for the specified channel.
        20M  — 20 MHz bandwidth limit
        200M — 200 MHz bandwidth limit
        FULL — full bandwidth, no restriction

    Args:
        channel: Channel number (1-4)
        bwlimit: {20M|200M|FULL}

    Returns:
        Current bandwidth limit when querying.
    """
    if bwlimit is None:
        return _query(resource_name, f":CHANnel{channel}:BWLimit?")
    _send(resource_name, f":CHANnel{channel}:BWLimit {bwlimit}")
    return None


def channel_impedance(resource_name: str, channel: int, impedance: str | None = None) -> str | None:
    """Set or query the input impedance for a channel.

    SCPI: :CHANnel<n>:IMPedance <impedance>

        Configures the input impedance for the specified channel.
        ONEMeg — 1 MΩ
        FIFTy  — 50 Ω

    Args:
        channel: Channel number (1-4)
        impedance: {ONEMeg|FIFTy}

    Returns:
        Current impedance when querying.
    """
    if impedance is None:
        return _query(resource_name, f":CHANnel{channel}:IMPedance?")
    _send(resource_name, f":CHANnel{channel}:IMPedance {impedance}")
    return None


def channel_invert(resource_name: str, channel: int, invert: bool | None = None) -> str | None:
    """Set or query the waveform inversion for a channel.

    SCPI: :CHANnel<n>:INVert {ON|OFF}

        Configures waveform inversion for the specified channel.

    Args:
        channel: Channel number (1-4)
        invert: True=ON (invert), False=OFF (normal)

    Returns:
        "ON" or "OFF" when querying.
    """
    if invert is None:
        return _query(resource_name, f":CHANnel{channel}:INVert?")
    _send(resource_name, f":CHANnel{channel}:INVert {'ON' if invert else 'OFF'}")
    return None


def channel_offset(resource_name: str, channel: int, offset: float | None = None) -> str | None:
    """Set or query the vertical offset for a channel.

    SCPI: :CHANnel<n>:OFFSet <offset>

        Configures the vertical offset voltage for the specified channel.

    Args:
        channel: Channel number (1-4)
        offset: Vertical offset in volts

    Returns:
        Current offset in volts when querying.
    """
    if offset is None:
        return _query(resource_name, f":CHANnel{channel}:OFFSet?")
    _send(resource_name, f":CHANnel{channel}:OFFSet {offset}")
    return None


def channel_scale(resource_name: str, channel: int, scale: float | None = None) -> str | None:
    """Set or query the vertical scale (volts/div) for a channel.

    SCPI: :CHANnel<n>:SCALe <scale>

        Configures the vertical scale (volts/div) for the specified channel.

    Args:
        channel: Channel number (1-4)
        scale: Vertical scale in volts/div

    Returns:
        Current scale when querying.
    """
    if scale is None:
        return _query(resource_name, f":CHANnel{channel}:SCALe?")
    _send(resource_name, f":CHANnel{channel}:SCALe {scale}")
    return None


def channel_probe(resource_name: str, channel: int, probe: str | float | None = None) -> str | None:
    """Set or query the probe attenuation for a channel.

    SCPI: :CHANnel<n>:PROBe <attenuation>[,<value>]
           :CHANnel<n>:PROBe?

        Configures the probe attenuation factor for the specified channel.
        DEFault — default 1X attenuation
        VALue,<value> — custom attenuation factor, range [1E-6, 1E6]
        Example: :CHANnel1:PROBe VALue,1.00E+02  (100X probe)

    Args:
        channel: Channel number (1-4)
        probe: DEFault (or "DEF") for 1X default,
               or float/int for custom attenuation (e.g. 100.0 for 100X)
        None — query current attenuation

    Returns:
        Current attenuation factor (NR3) when querying, e.g. "1.00E+02".
    """
    if probe is None:
        return _query(resource_name, f":CHANnel{channel}:PROBe?")
    if isinstance(probe, str):
        _send(resource_name, f":CHANnel{channel}:PROBe {probe}")
    else:
        _send(resource_name, f":CHANnel{channel}:PROBe VALue,{probe:.2E}")
    return None


def channel_skew(resource_name: str, channel: int, skew: float | None = None) -> str | None:
    """Set or query the channel deskew value.

    SCPI: :CHANnel<n>:SKEW <skew>

        Configures the channel deskew time to compensate for timing differences between probes or channels.

    Args:
        channel: Channel number (1-4)
        skew: Deskew time in seconds, range [-1.00E-07, 1.00E-07] (NR3 format)

    Returns:
        Current skew value when querying.
    """
    if skew is None:
        return _query(resource_name, f":CHANnel{channel}:SKEW?")
    _send(resource_name, f":CHANnel{channel}:SKEW {skew}")
    return None


def channel_unit(resource_name: str, channel: int, unit: str | None = None) -> str | None:
    """Set or query the display unit for a channel.

    SCPI: :CHANnel<n>:UNIT <unit>
           :CHANnel<n>:UNIT?

        Configures the vertical unit for the specified channel.
        This affects measurement results, cursors, channel scale, and trigger level units.
        V — voltage (volts)
        A — current (amperes)

    Args:
        channel: Channel number (1-4)
        unit: {V|A}

    Returns:
        Current unit when querying: "V" or "A".
    """
    if unit is None:
        return _query(resource_name, f":CHANnel{channel}:UNIT?")
    _send(resource_name, f":CHANnel{channel}:UNIT {unit}")
    return None


def channel_label(resource_name: str, channel: int, label: str | None = None) -> str | None:
    """Set or query the channel label text.

    SCPI: :CHANnel<n>:LABel:TEXT <qstring>

        Configures the label text for the specified channel (up to 20 characters).

    Args:
        channel: Channel number (1-4)
        label: Label text string (max 20 chars)
        None — query current label

    Returns:
        Current label string when querying.
    """
    if label is None:
        return _query(resource_name, f":CHANnel{channel}:LABel:TEXT?")
    _send(resource_name, f':CHANnel{channel}:LABel:TEXT "{label}"')
    return None


def channel_label_state(resource_name: str, channel: int, state: bool | None = None) -> str | None:
    """Set or query the channel label display on/off state.

    SCPI: :CHANnel<n>:LABel {ON|OFF}
           :CHANnel<n>:LABel?

        Configures the label display on/off state for the specified channel.
        ON  — show label
        OFF — hide label

    Args:
        channel: Channel number (1-4)
        state: True=ON (show label), False=OFF (hide label)
        None — query

    Returns:
        "ON" or "OFF" when querying.
    """
    if state is None:
        return _query(resource_name, f":CHANnel{channel}:LABel?")
    _send(resource_name, f":CHANnel{channel}:LABel {'ON' if state else 'OFF'}")
    return None
