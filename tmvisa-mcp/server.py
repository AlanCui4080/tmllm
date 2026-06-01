"""MCP Server entry point for tmllm - Test & Measurement LLM bridge.

Run with::

    python server.py
"""

from __future__ import annotations

import asyncio
import json
import logging
from typing import Any

from mcp.server.lowlevel import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    Tool,
    TextContent,
    CallToolResult,
)

import visa_manager
from visa_manager import (
    list_resources,
    detect_instruments,
    open_instrument,
    close_instrument,
    close_all_instruments,
)
import ieee4882

__version__ = "0.1.0"

logger = logging.getLogger("tmllm.server")

# ── MCP Server instance ───────────────────────────────────────────

_SERVER = Server(
    name="tmllm",
    version=__version__,
    instructions=(
        "tmllm provides LLMs with the ability to control electronic test & measurement "
        "instruments via VISA (Virtual Instrument Software Architecture). "
        "It supports GPIB, USB, Ethernet (TCPIP), and RS-232 interfaces through pyvisa.\n\n"
        "Capabilities:\n"
        "- Detect and list all VISA instruments on the system\n"
        "- Open / close instrument connections\n"
        "- Send arbitrary SCPI / vendor commands and read responses\n"
        "- Execute IEEE 488.2 standard commands (*IDN?, *RST, *OPC, *CLS, etc.)\n"
        "- Interpret status and event registers\n\n"
        "When the user explicitly provides a VISA resource address "
        "(e.g. 'TCPIP0::192.168.6.2::gpib0,1::INSTR'), skip visa_list_resources and "
        "use visa_open directly with that address. visa_list_resources is only needed "
        "when no address is known and you need to discover what is available.\n\n"
        "When sending SCPI commands, check if the command ends with '?'.\n"
        "- Commands ending with '?' are queries -> use visa_query\n"
        "- Commands without '?' are writes -> use visa_send\n\n"
        "Typical workflow:\n"
        "1. If user gives a VISA address -> go directly to visa_open\n"
        "2. If no address known -> use visa_list_resources to discover instruments\n"
        "3. Use ieee4882_command or visa_send / visa_query to interact\n"
        "4. Use visa_close when done"
    ),
)

# ── Tool schemas ──────────────────────────────────────────────────

TOOLS: list[Tool] = [
    Tool(
        name="visa_list_resources",
        description=(
            "List all detected VISA instruments on the system. "
            "Returns resource names and, when possible, *IDN? identification info "
            "(manufacturer, model, serial, firmware). "
            "Use this first to discover available instruments before opening a connection."
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Optional VISA resource query filter (e.g. 'USB?*' or 'GPIB?*'). Default: '?*' which matches all.",
                    "default": "?*",
                },
            },
        },
    ),
    Tool(
        name="visa_open",
        description=(
            "Open a connection to a VISA instrument by its resource name. "
            "The resource name is typically obtained from visa_list_resources. "
            "Once opened, the connection is cached and reused for subsequent commands."
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {
                    "type": "string",
                    "description": "VISA resource string, e.g. 'USB0::0x1AB1::0x0610::SDSMMEBQ4Rxxxx::INSTR' or 'GPIB0::10::INSTR'.",
                },
                "timeout": {
                    "type": "integer",
                    "description": "Communication timeout in milliseconds. Default: 5000.",
                    "default": 5000,
                },
            },
            "required": ["resource_name"],
        },
    ),
    Tool(
        name="visa_close",
        description=(
            "Close the connection to a VISA instrument. If resource_name is omitted, "
            "closes ALL open instrument connections."
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {
                    "type": "string",
                    "description": "VISA resource string to close. If omitted, all connections are closed.",
                },
            },
        },
    ),
    Tool(
        name="visa_send",
        description=(
            "Send a raw SCPI or vendor-specific command to an instrument. "
            "Use this for commands that do NOT expect a response (e.g., '*RST', 'CONF:VOLT:DC'). "
            "For queries that return data, use visa_query instead."
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {
                    "type": "string",
                    "description": "VISA resource string of an already-opened instrument.",
                },
                "command": {
                    "type": "string",
                    "description": "The SCPI command to send (e.g. '*RST', 'MEAS:VOLT:DC?').",
                },
            },
            "required": ["resource_name", "command"],
        },
    ),
    Tool(
        name="visa_query",
        description=(
            "Send a SCPI query to an instrument and return the response. "
            "Use this for any command ending with '?' that expects data back. "
            "The response is returned as a trimmed string."
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {
                    "type": "string",
                    "description": "VISA resource string of an already-opened instrument.",
                },
                "command": {
                    "type": "string",
                    "description": "The SCPI query to send (e.g. '*IDN?', 'MEAS:VOLT:DC?').",
                },
                "timeout": {
                    "type": "integer",
                    "description": "Override timeout in milliseconds for this query only (0 = use default).",
                    "default": 0,
                },
            },
            "required": ["resource_name", "command"],
        },
    ),
    Tool(
        name="ieee4882_command",
        description=(
            "Execute an IEEE 488.2 standard command on an instrument. "
            "These are universal commands that most SCPI instruments support.\n\n"
            "Supported commands:\n"
            "- *IDN? — Query instrument identification (manufacturer, model, serial, firmware)\n"
            "- *RST — Reset instrument to factory defaults\n"
            "- *CLS — Clear all status registers and error queue\n"
            "- *OPC — Set Operation Complete bit when pending commands finish\n"
            "- *OPC? — Wait for pending commands and return '1' when complete\n"
            "- *ESE [value] — Set/query Standard Event Status Enable register\n"
            "- *ESR? — Query Standard Event Status Register\n"
            "- *SRE [value] — Set/query Service Request Enable register\n"
            "- *STB? — Read Status Byte register\n"
            "- *TST? — Run self-test (returns '0'=pass, '1'=fail)\n"
            "- *WAI — Wait for all pending operations to complete\n"
            "- *TRG — Trigger the instrument\n"
            "- *LRN? — Learn (return commands to restore current state)\n"
            "- *OPT? — Query installed options\n"
            "- *PSC [0|1] — Power-on status clear setting\n"
            "- *SAV [0-4] — Save instrument state to internal slot\n"
            "- *RCL [0-4] — Recall saved instrument state\n"
            "- SYST:ERR? — Query and clear the next error from the error queue"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {
                    "type": "string",
                    "description": "VISA resource string of an already-opened instrument.",
                },
                "command": {
                    "type": "string",
                    "enum": [
                        "*IDN?", "*RST", "*CLS", "*OPC", "*OPC?",
                        "*ESE", "*ESR?", "*SRE", "*STB?",
                        "*TST?", "*WAI", "*TRG", "*LRN?", "*OPT?",
                        "*PSC", "*SAV", "*RCL",
                        "SYST:ERR?",
                    ],
                    "description": "The IEEE 488.2 command to execute.",
                },
                "value": {
                    "type": "integer",
                    "description": (
                        "Parameter value for commands that need one: "
                        "*ESE (enable mask, 0-255), *SRE (enable mask, 0-255), "
                        "*PSC (0 or 1), *SAV (0-4), *RCL (0-4)."
                    ),
                },
            },
            "required": ["resource_name", "command"],
        },
    ),
    Tool(
        name="ieee4882_interpret_register",
        description=(
            "Interpret the decimal value returned by *STB? or *ESR? into "
            "human-readable bit descriptions. "
            "Useful for diagnosing instrument status and errors.\n\n"
            "For *STB? (Status Byte):\n"
            "- 2: Error queue has entries\n"
            "- 4: Questionable data summary\n"
            "- 16: Message available in output buffer\n"
            "- 32: Standard event summary\n"
            "- 64: Master summary / service request\n"
            "- 128: Standard operation summary\n\n"
            "For *ESR? (Standard Event Register):\n"
            "- 1: Operation complete\n"
            "- 4: Query error\n"
            "- 8: Device-specific error\n"
            "- 16: Execution error\n"
            "- 32: Command error\n"
            "- 128: Power on"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "register_type": {
                    "type": "string",
                    "enum": ["STB", "ESR"],
                    "description": "Register type: 'STB' for Status Byte, 'ESR' for Standard Event Register.",
                },
                "value": {
                    "type": "integer",
                    "description": "The raw decimal value returned by *STB? or *ESR?.",
                },
            },
            "required": ["register_type", "value"],
        },
    ),
    Tool(
        name="visa_read_raw",
        description=(
            "Read raw data from the instrument's output buffer without sending a command first. "
            "Use this when data is expected to be already available (e.g., after a *TRG followed by FETCh?)."
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {
                    "type": "string",
                    "description": "VISA resource string of an already-opened instrument.",
                },
            },
            "required": ["resource_name"],
        },
    ),
    Tool(
        name="visa_list_open",
        description=(
            "List all currently open instrument connections. "
            "Useful for checking which instruments are connected before sending commands."
        ),
        inputSchema={
            "type": "object",
            "properties": {},
        },
    ),
]


# ── Tool registry ─────────────────────────────────────────────────

@_SERVER.list_tools()
async def list_tools() -> list[Tool]:
    return TOOLS


@_SERVER.call_tool()
async def call_tool(tool_name: str, arguments: dict[str, Any]) -> list[TextContent]:
    try:
        result = await _dispatch(tool_name, arguments)
        return [TextContent(type="text", text=result)]
    except Exception as exc:
        logger.exception("Tool error: %s", tool_name)
        return [TextContent(type="text", text=f"Error: {exc}")]


async def _dispatch(name: str, args: dict[str, Any]) -> str:
    """Route tool call to the appropriate handler."""

    if name == "visa_list_resources":
        query_filter = args.get("query", "?*")
        instruments = detect_instruments(query_filter)
        if not instruments:
            return json.dumps({"visa_backend": "ok", "count": 0, "instruments": [], "hint": "No instruments found. Check physical connections and VISA backend (NI-VISA or pyvisa-py)."})

        results = []
        for info in instruments:
            results.append({
                "resource_name": info.resource_name,
                "interface_type": info.interface_type,
                "manufacturer": info.manufacturer,
                "model": info.model,
                "serial": info.serial,
                "firmware": info.firmware,
                "description": info.description,
            })
        return json.dumps({
            "visa_backend": "ok",
            "count": len(results),
            "instruments": results,
            "hint": "Use the 'resource_name' field with visa_open to connect to an instrument.",
        }, ensure_ascii=False)

    elif name == "visa_open":
        resource_name = args["resource_name"]
        timeout = args.get("timeout", 5000)
        inst = open_instrument(resource_name, timeout=timeout)
        inst.timeout = timeout
        return json.dumps({
            "status": "ok",
            "resource_name": resource_name,
            "timeout_ms": timeout,
            "message": f"Instrument {resource_name} opened successfully.",
        })

    elif name == "visa_close":
        resource_name = args.get("resource_name")
        if resource_name:
            close_instrument(resource_name)
            return json.dumps({"status": "ok", "closed": resource_name})
        else:
            close_all_instruments()
            return json.dumps({"status": "ok", "closed": "all"})

    elif name == "visa_list_open":
        import visa_manager as _vm
        open_list = list(_vm._active_instruments.keys())
        return json.dumps({"open_count": len(open_list), "instruments": open_list})

    elif name == "visa_send":
        resource_name = args["resource_name"]
        command = args["command"]
        ieee4882.send(resource_name, command)
        return json.dumps({"status": "ok", "command": command, "resource": resource_name})

    elif name == "visa_query":
        resource_name = args["resource_name"]
        command = args["command"]
        timeout = args.get("timeout", 0)
        if timeout > 0:
            import visa_manager as _vm
            inst = _vm.get_instrument(resource_name)
            if inst:
                old_timeout = inst.timeout
                inst.timeout = timeout
                try:
                    response = ieee4882.query(resource_name, command)
                finally:
                    inst.timeout = old_timeout
            else:
                response = ieee4882.query(resource_name, command)
        else:
            response = ieee4882.query(resource_name, command)
        return response

    elif name == "visa_read_raw":
        resource_name = args["resource_name"]
        return ieee4882.read(resource_name)

    elif name == "ieee4882_command":
        resource_name = args["resource_name"]
        command = args["command"]
        value = args.get("value")

        # commands that take a parameter
        cmd_map: dict[str, callable] = {
            "*IDN?": lambda: ieee4882.idn(resource_name),
            "*RST": lambda: ieee4882.rst(resource_name),
            "*CLS": lambda: ieee4882.cls(resource_name),
            "*OPC": lambda: ieee4882.opc(resource_name),
            "*OPC?": lambda: ieee4882.opc_query(resource_name),
            "*ESR?": lambda: ieee4882.esr(resource_name),
            "*STB?": lambda: ieee4882.stb(resource_name),
            "*TST?": lambda: ieee4882.tst(resource_name),
            "*WAI": lambda: ieee4882.wai(resource_name),
            "*TRG": lambda: ieee4882.trg(resource_name),
            "*LRN?": lambda: ieee4882.lrn(resource_name),
            "*OPT?": lambda: ieee4882.opt(resource_name),
        }

        if command in cmd_map:
            result = cmd_map[command]()
        elif command in ("*ESE", "*ESE?"):
            result = ieee4882.ese(resource_name, value)
        elif command in ("*SRE", "*SRE?"):
            result = ieee4882.sre(resource_name, value)
        elif command == "*PSC":
            result = ieee4882.psc(resource_name, value)
            if result is None:
                result = 1 if value else 0  # return None for write
        elif command == "*SAV":
            if value is None:
                return "Error: *SAV requires a slot value (0-4)."
            result = ieee4882.sav(resource_name, value)
        elif command == "*RCL":
            if value is None:
                return "Error: *RCL requires a slot value (0-4)."
            result = ieee4882.rcl(resource_name, value)
        elif command == "SYST:ERR?":
            result = ieee4882.syst_err(resource_name)
        else:
            return f"Unknown command: {command}"

        if result is None:
            return json.dumps({"status": "ok", "command": command, "resource": resource_name})
        return str(result)

    elif name == "ieee4882_interpret_register":
        register_type = args["register_type"]
        value = args["value"]
        if register_type == "STB":
            bits = ieee4882.interpret_stb(value)
        else:
            bits = ieee4882.interpret_esr(value)
        # add numeric values for each set bit
        descriptions = []
        numeric_bits = []
        for name, is_set in bits.items():
            if is_set:
                numeric_bits.append(name)
        return json.dumps({
            "register_type": register_type,
            "decimal_value": value,
            "bits": bits,
            "set_bits": [n for n, v in bits.items() if v],
        })

    return f"Unknown tool: {name}"


# ── Entry point ───────────────────────────────────────────────────

async def _server_main():
    async with stdio_server() as (read, write):
        await _SERVER.run(read, write, _SERVER.create_initialization_options())


def main():
    """Entry point for ``tmllm-server`` console script."""
    logging.basicConfig(
        level=logging.WARNING,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
    logging.getLogger("tmllm").setLevel(logging.DEBUG)
    asyncio.run(_server_main())


if __name__ == "__main__":
    main()
