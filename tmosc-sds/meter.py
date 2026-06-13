"""METEr subsystem SCPI commands (handheld scope-meter, if option installed)."""
from __future__ import annotations
from _base import _send, _query


def meter_state(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query the multimeter on/off state.

    SCPI: MMETer {ON|OFF}
    """
    if state is None:
        return _query(resource_name, "MMETer?")
    _send(resource_name, f"MMETer {'ON' if state else 'OFF'}")
    return None


def meter_read(resource_name: str) -> str:
    """Query current multimeter reading.

    SCPI: READ?

    Returns format: MM_VALUE <value> (e.g. "MM_VALUE 0.00V")
    """
    return _query(resource_name, "READ?")


def meter_configure(resource_name: str) -> str:
    """Query current measurement function and value.

    SCPI: CONFigure?

    Returns format: {DCV|ACV|RES|DIODE|CONTINUITY|CAP|DCI|ACI} <value>
    """
    return _query(resource_name, "CONFigure?")


def meter_configure_continuity(resource_name: str) -> None:
    """Configure meter for continuity measurement with default settings.

    SCPI: CONFigure:CONTinuit
    """
    _send(resource_name, "CONFigure:CONTinuit")


def meter_configure_current_ac(resource_name: str, range_val: str = "AUTO") -> None:
    """Configure meter for AC current measurement.

    SCPI: CONFigure:CURRent:AC <range>

    Args:
        range_val: Range value or "AUTO"
    """
    _send(resource_name, f"CONFigure:CURRent:AC {range_val}")


def meter_configure_current_dc(resource_name: str, range_val: str = "AUTO") -> None:
    """Configure meter for DC current measurement.

    SCPI: CONFigure:CURRent:DC <range>
    """
    _send(resource_name, f"CONFigure:CURRent:DC {range_val}")


def meter_configure_diode(resource_name: str) -> None:
    """Configure meter for diode measurement.

    SCPI: CONFigure:DIOD
    """
    _send(resource_name, "CONFigure:DIOD")


def meter_configure_resistance(resource_name: str, range_val: str = "AUTO") -> None:
    """Configure meter for resistance measurement.

    SCPI: CONFigure:RESistance <range>
    """
    _send(resource_name, f"CONFigure:RESistance {range_val}")


def meter_configure_voltage_ac(resource_name: str, range_val: str = "AUTO") -> None:
    """Configure meter for AC voltage measurement.

    SCPI: CONFigure[:VOLTage]:AC <range>
    """
    _send(resource_name, f"CONFigure:VOLTage:AC {range_val}")


def meter_configure_voltage_dc(resource_name: str, range_val: str = "AUTO") -> None:
    """Configure meter for DC voltage measurement.

    SCPI: CONFigure[:VOLTage]:DC <range>
    """
    _send(resource_name, f"CONFigure:VOLTage:DC {range_val}")


def meter_configure_capacitance(resource_name: str) -> None:
    """Configure meter for capacitance measurement.

    SCPI: CONFigure:CAPacitance
    """
    _send(resource_name, "CONFigure:CAPacitance")


def meter_measure_continuity(resource_name: str) -> str:
    """Measure continuity.

    SCPI: MEASure:CONTinuity?
    """
    return _query(resource_name, "MEASure:CONTinuity?")


def meter_measure_current_ac(resource_name: str, range_val: str = "AUTO") -> str:
    """Measure AC current.

    SCPI: MEASure:CURRent:AC? <range>
    """
    return _query(resource_name, f"MEASure:CURRent:AC? {range_val}")


def meter_measure_current_dc(resource_name: str, range_val: str = "AUTO") -> str:
    """Measure DC current.

    SCPI: MEASure:CURRent:DC? <range>
    """
    return _query(resource_name, f"MEASure:CURRent:DC? {range_val}")


def meter_measure_diode(resource_name: str) -> str:
    """Measure diode.

    SCPI: MEASure:DIODe?
    """
    return _query(resource_name, "MEASure:DIODe?")


def meter_measure_resistance(resource_name: str, range_val: str = "AUTO") -> str:
    """Measure resistance.

    SCPI: MEASure:RESistance? <range>
    """
    return _query(resource_name, f"MEASure:RESistance? {range_val}")


def meter_measure_voltage_ac(resource_name: str, range_val: str = "AUTO") -> str:
    """Measure AC voltage.

    SCPI: MEASure:VOLTage:AC? <range>
    """
    return _query(resource_name, f"MEASure:VOLTage:AC? {range_val}")


def meter_measure_voltage_dc(resource_name: str, range_val: str = "AUTO") -> str:
    """Measure DC voltage.

    SCPI: MEASure:VOLTage:DC? <range>
    """
    return _query(resource_name, f"MEASure:VOLTage:DC? {range_val}")


def meter_measure_capacitance(resource_name: str) -> str:
    """Measure capacitance.

    SCPI: MEASure:CAPacitance?
    """
    return _query(resource_name, "MEASure:CAPacitance?")


def meter_sense_current_ac_null(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query AC current relative (null) value on/off.

    SCPI: [SENSe:]CURRent:AC:NULL <state>
    """
    if state is None:
        return _query(resource_name, "CURRent:AC:NULL?")
    _send(resource_name, f"CURRent:AC:NULL {'ON' if state else 'OFF'}")
    return None


def meter_sense_current_dc_null(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query DC current relative (null) value on/off.

    SCPI: [SENSe:]CURRent:DC:NULL <state>
    """
    if state is None:
        return _query(resource_name, "CURRent:DC:NULL?")
    _send(resource_name, f"CURRent:DC:NULL {'ON' if state else 'OFF'}")
    return None


def meter_sense_resistance_null(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query resistance relative (null) value on/off.

    SCPI: [SENSe:]RESistance:NULL <state>
    """
    if state is None:
        return _query(resource_name, "RESistance:NULL?")
    _send(resource_name, f"RESistance:NULL {'ON' if state else 'OFF'}")
    return None


def meter_sense_voltage_ac_null(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query AC voltage relative (null) value on/off.

    SCPI: [SENSe:]VOLTage:AC:NULL <state>
    """
    if state is None:
        return _query(resource_name, "VOLTage:AC:NULL?")
    _send(resource_name, f"VOLTage:AC:NULL {'ON' if state else 'OFF'}")
    return None


def meter_sense_voltage_dc_null(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query DC voltage relative (null) value on/off.

    SCPI: [SENSe:]VOLTage:DC:NULL <state>
    """
    if state is None:
        return _query(resource_name, "VOLTage:DC:NULL?")
    _send(resource_name, f"VOLTage:DC:NULL {'ON' if state else 'OFF'}")
    return None


def meter_sense_capacitance_null(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query capacitance relative (null) value on/off.

    SCPI: [SENSe:]CAPacitance:NULL <state>
    """
    if state is None:
        return _query(resource_name, "CAPacitance:NULL?")
    _send(resource_name, f"CAPacitance:NULL {'ON' if state else 'OFF'}")
    return None


def meter_configure_set(resource_name: str, func: str) -> None:
    """Configure the multimeter for a specific measurement function.

    SCPI: CONFigure <func>

    Args:
        func: Measurement function (e.g. 'VOLTage:AC', 'VOLTage:DC',
              'CURRent:AC', 'CURRent:DC', 'RESistance', 'CAPacitance',
              'DIODe', 'CONTinuity')
    """
    _send(resource_name, f"CONFigure {func}")
