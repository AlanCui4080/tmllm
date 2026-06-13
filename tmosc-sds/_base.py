"""SDS Series oscilloscope driver — shared base helpers."""

from __future__ import annotations

import sys, os, logging, json

_sibling = os.path.join(os.path.dirname(__file__), "..", "tmvisa-mcp")
if _sibling not in sys.path:
    sys.path.insert(0, _sibling)

import visa_manager
import ieee4882

logger = logging.getLogger("tmosc.sds")


def _ensure(resource_name: str):
    inst = visa_manager.get_instrument(resource_name)
    if inst is None:
        inst = visa_manager.open_instrument(resource_name)
    return inst


def _send(resource_name: str, cmd: str):
    ieee4882.send(resource_name, cmd)


def _query(resource_name: str, cmd: str) -> str:
    return ieee4882.query(resource_name, cmd)


def _query_raw(resource_name: str, cmd: str) -> bytes:
    return ieee4882.query_raw(resource_name, cmd)


def _read_raw(resource_name: str) -> bytes:
    return ieee4882.read_raw(resource_name)
