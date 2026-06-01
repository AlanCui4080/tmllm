"""IEEE 488.2 standard commands for VISA instruments.

All IEEE 488.2 commands start with ``*`` and are defined in the
IEEE 488.2 standard.  Most SCPI-compliant instruments implement
these commands.

Standard Event Register bits:
    0 - Operation Complete (*OPC before/with all commands done)
    1 - (unused, always 0)
    2 - Query Error (output buffer empty, new cmd before read, etc.)
    3 - Device-Specific Error
    4 - Execution Error
    5 - Command Error
    6 - (unused, always 0)
    7 - Power On

Status Byte Register bits:
    0 - (unused)
    1 - (unused)
    2 - Error Queue (one or more errors queued; use SYST:ERR?)
    3 - Questionable Data Summary
    4 - Message Available (data in output buffer)
    5 - Standard Event Summary (bits enabled by *ESE)
    6 - Master Summary / RQS (service request)
    7 - Standard Operation Summary
"""

from __future__ import annotations

import logging
from typing import Any

import pyvisa

import visa_manager

logger = logging.getLogger(__name__)


def _get_inst(resource_name: str) -> pyvisa.Resource:
    """Ensure an instrument is open and return it."""
    inst = visa_manager.get_instrument(resource_name)
    if inst is None:
        inst = visa_manager.open_instrument(resource_name)
    return inst


# ── generic send / query ─────────────────────────────────────────

def send(resource_name: str, command: str) -> None:
    """Write a raw SCPI/488.2 command to the instrument (no response expected)."""
    inst = _get_inst(resource_name)
    inst.write(command)
    logger.debug("[%s] >>> %s", resource_name, command)


def query(resource_name: str, command: str) -> str:
    """Write a query and return the response string."""
    inst = _get_inst(resource_name)
    inst.write(command)
    resp = inst.read().strip()
    logger.debug("[%s] >>> %s => %s", resource_name, command, resp)
    return resp


def read(resource_name: str) -> str:
    """Read raw data from the instrument output buffer."""
    inst = _get_inst(resource_name)
    resp = inst.read().strip()
    logger.debug("[%s] <<< %s", resource_name, resp)
    return resp


# ── IEEE 488.2 specialized commands ──────────────────────────────

def cls(resource_name: str) -> None:
    """*CLS - Clear status. Clears all event registers and the error queue."""
    send(resource_name, "*CLS")


def ese(resource_name: str, enable_value: int | None = None) -> str | None:
    """*ESE [<value>] - Standard Event Status Enable.

    Set the enable mask (0..255) or query current mask with *ESE?.
    """
    if enable_value is not None:
        send(resource_name, f"*ESE {enable_value}")
        return None
    return query(resource_name, "*ESE?")


def esr(resource_name: str) -> str:
    """*ESR? - Query Standard Event Status Register. Returns decimal sum of set bits."""
    return query(resource_name, "*ESR?")


def idn(resource_name: str) -> str:
    """*IDN? - Query instrument identification string.

    Returns: ``manufacturer,model,serial,firmware``
    """
    return query(resource_name, "*IDN?")


def lrn(resource_name: str) -> str:
    """*LRN? - Learn device setup. Returns SCPI commands to restore current state."""
    return query(resource_name, "*LRN?")


def opc(resource_name: str) -> None:
    """*OPC - Set Operation Complete bit (0) in the Standard Event Register
    when all pending operations finish."""
    send(resource_name, "*OPC")


def opc_query(resource_name: str) -> str:
    """*OPC? - Wait for pending operations, then return '1'.

    This blocks until all pending operations are complete.
    """
    return query(resource_name, "*OPC?")


def opt(resource_name: str) -> str:
    """*OPT? - Query installed options."""
    return query(resource_name, "*OPT?")


def psc(resource_name: str, value: int | None = None) -> str | None:
    """*PSC {0|1} - Power-on Status Clear.

    ``*PSC 0`` -- preserve enable registers across power cycles.
    ``*PSC 1`` -- clear enable registers at power-on (default).
    """
    if value is not None:
        send(resource_name, f"*PSC {value}")
        return None
    return query(resource_name, "*PSC?")


def rcl(resource_name: str, slot: int) -> None:
    """*RCL <n> - Recall instrument state from internal slot n (0..4)."""
    send(resource_name, f"*RCL {slot}")


def rst(resource_name: str) -> None:
    """*RST - Reset instrument to factory defaults."""
    send(resource_name, "*RST")


def sav(resource_name: str, slot: int) -> None:
    """*SAV <n> - Save instrument state to internal slot n (0..4)."""
    send(resource_name, f"*SAV {slot}")


def sre(resource_name: str, enable_value: int | None = None) -> str | None:
    """*SRE [<value>] - Service Request Enable register.

    Set the enable mask or query with *SRE?.
    """
    if enable_value is not None:
        send(resource_name, f"*SRE {enable_value}")
        return None
    return query(resource_name, "*SRE?")


def stb(resource_name: str) -> str:
    """*STB? - Read Status Byte. Returns decimal sum of set condition bits.

    Unlike a serial poll, *STB? does not clear bit 6 (MSS/RQS).
    """
    return query(resource_name, "*STB?")


def trg(resource_name: str) -> None:
    """*TRG - Trigger. Equivalent to a GET (Group Execute Trigger)
    or TRIGger:SOURce BUS.
    """
    send(resource_name, "*TRG")


def tst(resource_name: str) -> str:
    """*TST? - Self-test. Returns '0' (pass) or '1' (fail)."""
    return query(resource_name, "*TST?")


def wai(resource_name: str) -> None:
    """*WAI - Wait-to-continue. Blocks further commands until all pending
    operations complete."""
    send(resource_name, "*WAI")


def syst_err(resource_name: str) -> str:
    """SYSTem:ERRor? - Query and clear the next error from the error queue.

    Returns: ``error_code,"error_message"`` or ``0,"No error"`` if queue is empty.
    """
    return query(resource_name, "SYST:ERR?")


# ── helpers for interpretation ───────────────────────────────────

def parse_idn(idn_str: str) -> dict[str, str]:
    """Parse an *IDN? response into its four fields."""
    parts = [p.strip() for p in idn_str.split(",")]
    keys = ["manufacturer", "model", "serial", "firmware"]
    return {keys[i]: parts[i] if i < len(parts) else "" for i in range(len(keys))}


def interpret_stb(stb_val: int) -> dict[str, bool]:
    """Decode a Status Byte value into individual bit names."""
    bits = {
        "error_queue": 2,
        "questionable_summary": 3,
        "message_available": 4,
        "standard_event_summary": 5,
        "master_summary": 6,
        "operation_summary": 7,
    }
    return {name: bool(stb_val & (1 << bit)) for name, bit in bits.items()}


def interpret_esr(esr_val: int) -> dict[str, bool]:
    """Decode a Standard Event Register value into individual bit names."""
    bits = {
        "operation_complete": 0,
        "query_error": 2,
        "device_error": 3,
        "execution_error": 4,
        "command_error": 5,
        "power_on": 7,
    }
    return {name: bool(esr_val & (1 << bit)) for name, bit in bits.items()}
