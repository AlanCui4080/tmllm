"""SAVE subsystem SCPI commands."""

from __future__ import annotations

from _base import _send


def save_setup(resource_name: str, target: str) -> None:
    """Save the oscilloscope setup.

    SCPI: :SAVE:SETup <setup_num>

        Saves the oscilloscope setup.
        INTernal,<num> — save to internal storage, <num> [1,4]
        EXTernal,<path> — save to external file path

    Args:
        target: {INTernal,<num>|EXTernal,<path>}
            e.g. "INTernal,1" or 'EXTernal,"mysetup.xml"'
    """
    _send(resource_name, f":SAVE:SETup {target}")


def save_image(resource_name: str, path: str, img_type: str, invert: str = "OFF", menu: str | None = None) -> None:
    """Save a screenshot image.

    SCPI: :SAVE:IMAGe <path>,<type>,<invert>[,<menu>]

        Saves a screenshot image.

    Args:
        path: Quoted image filename (e.g. '"screenshot.png"')
        img_type: {BMP|JPG|PNG}
        invert: {OFF|ON} — color inversion
        menu: {MOFf|MON} — include/hide right-side menu, optional
    """
    cmd = f':SAVE:IMAGe {path},{img_type},{invert}'
    if menu:
        cmd += f",{menu}"
    _send(resource_name, cmd)


def save_csv(resource_name: str, path: str, source: str, state: str = "OFF") -> None:
    """Save waveform data as CSV.

    SCPI: :SAVE:CSV <path>,<source>,<state>

        Saves waveform data in CSV format.

    Args:
        path: Quoted CSV filename (e.g. '"waveform.csv"')
        source: {C<n>|Z<n>|F<x>|M<m>|D0_D15|DIGital|ZD0_ZD15|ZDIGital}
        state: {OFF|ON} — include header information
    """
    _send(resource_name, f":SAVE:CSV {path},{source},{state}")


def save_binary(resource_name: str, path: str, source: str) -> None:
    """Save waveform data as binary.

    SCPI: :SAVE:BINary <path>,<source>

        Saves waveform data in binary format.

    Args:
        path: Quoted binary filename (e.g. '"waveform.bin"')
        source: {C<n>|Z<n>|F<x>|M<m>|D0_D15|DIGital|ZD0_ZD15|ZDIGital}
    """
    _send(resource_name, f":SAVE:BINary {path},{source}")


def save_matlab(resource_name: str, path: str, source: str) -> None:
    """Save waveform data as MATLAB format.

    SCPI: :SAVE:MATLab <path>,<source>

        Saves waveform data in MATLAB format.

    Args:
        path: Quoted MATLAB filename (e.g. '"waveform.mat"')
        source: {C<n>|Z<n>|F<x>|M<m>|D0_D15|DIGital|ZD0_ZD15|ZDIGital}
    """
    _send(resource_name, f":SAVE:MATLab {path},{source}")


def save_reference(resource_name: str, path: str, source: str) -> None:
    """Save waveform data as reference file.

    SCPI: :SAVE:REFerence <path>,<source>

        Saves a reference waveform to file.

    Args:
        path: Quoted reference filename (e.g. '"ref1.ref"')
        source: {C<n>|F<x>|D<d>}
    """
    _send(resource_name, f":SAVE:REFerence {path},{source}")


def save_default(resource_name: str, setup: str) -> None:
    """Save current or factory settings as default configuration.

    SCPI: :SAVE:DEFault <set>

        Saves settings as the default configuration.
        CUSTom — save current user settings as default
        FACTory — restore factory settings as default

    Args:
        setup: {CUSTom|FACTory}
    """
    _send(resource_name, f":SAVE:DEFault {setup}")
