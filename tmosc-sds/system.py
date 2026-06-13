"""SYSTem subsystem SCPI commands."""

from __future__ import annotations

from _base import _send, _query


def system_buzzer(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query the buzzer on/off state.

    SCPI: :SYSTem:BUZZer {ON|OFF}
           :SYSTem:BUZZer?

        Configures the buzzer on/off state.

    Args:
        state: True=ON, False=OFF

    Returns:
        "ON" or "OFF" when querying.
    """
    if state is None:
        return _query(resource_name, ":SYSTem:BUZZer?")
    _send(resource_name, f":SYSTem:BUZZer {'ON' if state else 'OFF'}")
    return None


def system_clock(resource_name: str, source: str | None = None) -> str | None:
    """Set or query the clock source and 10MHz output state.

    SCPI: :SYSTem:CLOCk <source>
           :SYSTem:CLOCk?

        Configures the clock source and internal 10 MHz clock output state.
        EXT    — external clock source, 10 MHz output disabled automatically
        IN_ON  — internal clock source, 10 MHz output enabled
        IN_OFF — internal clock source, 10 MHz output disabled

    Args:
        source: {EXT|IN_ON|IN_OFF}

    Returns:
        Current clock source when querying.
    """
    if source is None:
        return _query(resource_name, ":SYSTem:CLOCk?")
    _send(resource_name, f":SYSTem:CLOCk {source}")
    return None


def system_date(resource_name: str, date: int | None = None) -> str | None:
    """Set or query the system date.

    SCPI: :SYSTem:DATE <date>
           :SYSTem:DATE?

        Configures the system date.
        Format: YYYYMMDD (8-digit integer, e.g. 20190819)

    Args:
        date: Date as YYYYMMDD integer (e.g. 20190819)

    Returns:
        Current date (YYYYMMDD) when querying.

    Associated commands: :SYSTem:TIME
    """
    if date is None:
        return _query(resource_name, ":SYSTem:DATE?")
    _send(resource_name, f":SYSTem:DATE {date}")
    return None


def system_time(resource_name: str, time: int | None = None) -> str | None:
    """Set or query the system time.

    SCPI: :SYSTem:TIME <time>
           :SYSTem:TIME?

        Configures the system time.
        Format: HHMMSS (6-digit integer, e.g. 143025 for 14:30:25)

    Args:
        time: Time as HHMMSS integer (e.g. 143025)

    Returns:
        Current time (HHMMSS) when querying.

    Associated commands: :SYSTem:DATE
    """
    if time is None:
        return _query(resource_name, ":SYSTem:TIME?")
    _send(resource_name, f":SYSTem:TIME {time}")
    return None


def system_language(resource_name: str, language: str | None = None) -> str | None:
    """Set or query the display language.

    SCPI: :SYSTem:LANGuage <language>
           :SYSTem:LANGuage?

        Configures the display language.
        {SCHinese|TCHinese|ENGLish|FRENch|JAPanese|KORean|DEUTsch|ESPan|RUSSian|ITALiana|PORTuguese}

    Args:
        language: Language code (e.g. "ENGLish", "SCHinese")

    Returns:
        Current language when querying.
    """
    if language is None:
        return _query(resource_name, ":SYSTem:LANGuage?")
    _send(resource_name, f":SYSTem:LANGuage {language}")
    return None


def system_reboot(resource_name: str) -> None:
    """Reboot the oscilloscope.

    SCPI: :SYSTem:REBoot

        Reboots the oscilloscope.
    """
    _send(resource_name, ":SYSTem:REBoot")


def system_shutdown(resource_name: str) -> None:
    """Shutdown the oscilloscope.

    SCPI: :SYSTem:SHUTdown

        Shuts down the oscilloscope.
    """
    _send(resource_name, ":SYSTem:SHUTdown")


def system_lan_gateway(resource_name: str, gateway: str | None = None) -> str | None:
    """Set or query the LAN gateway.

    SCPI: :SYSTem:COMMunicate:LAN:GATeway <qstring>
           :SYSTem:COMMunicate:LAN:GATeway?

        Configures the LAN gateway address.

    Args:
        gateway: Gateway IP address (e.g. "10.12.0.1")

    Returns:
        Current gateway when querying.
    """
    if gateway is None:
        return _query(resource_name, ":SYSTem:COMMunicate:LAN:GATeway?")
    _send(resource_name, f':SYSTem:COMMunicate:LAN:GATeway "{gateway}"')
    return None


def system_lan_ip(resource_name: str, ip: str | None = None) -> str | None:
    """Set or query the LAN IP address.

    SCPI: :SYSTem:COMMunicate:LAN:IPADdress <qstring>
           :SYSTem:COMMunicate:LAN:IPADdress?

        Configures the LAN IP address.

    Args:
        ip: IP address string (e.g. "10.12.255.229")

    Returns:
        Current IP address when querying.
    """
    if ip is None:
        return _query(resource_name, ":SYSTem:COMMunicate:LAN:IPADdress?")
    _send(resource_name, f':SYSTem:COMMunicate:LAN:IPADdress "{ip}"')
    return None


def system_lan_mac(resource_name: str) -> str:
    """Query the MAC address.

    SCPI: :SYSTem:COMMunicate:LAN:MAC?

        Queries the oscilloscope MAC address.

    Returns:
        MAC address string (e.g. "00:01:D2:0C:00:A0").
    """
    return _query(resource_name, ":SYSTem:COMMunicate:LAN:MAC?")


def system_lan_mask(resource_name: str, mask: str | None = None) -> str | None:
    """Set or query the LAN subnet mask.

    SCPI: :SYSTem:COMMunicate:LAN:SMASk <qstring>
           :SYSTem:COMMunicate:LAN:SMASk?

        Configures the LAN subnet mask.

    Args:
        mask: Subnet mask string (e.g. "255.255.0.0")

    Returns:
        Current subnet mask when querying.
    """
    if mask is None:
        return _query(resource_name, ":SYSTem:COMMunicate:LAN:SMASk?")
    _send(resource_name, f':SYSTem:COMMunicate:LAN:SMASk "{mask}"')
    return None


def system_remote(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query remote control lock state.

    SCPI: :SYSTem:REMote {ON|OFF}
           :SYSTem:REMote?

        Configures the remote control lock state. When locked, the touch screen and front panel are disabled.

    Args:
        state: True=ON (lock), False=OFF (unlock)
    """
    if state is None:
        return _query(resource_name, ":SYSTem:REMote?")
    _send(resource_name, f":SYSTem:REMote {'ON' if state else 'OFF'}")
    return None


def system_touch(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query touch screen on/off state.

    SCPI: :SYSTem:TOUCh {ON|OFF}
           :SYSTem:TOUCh?

        Configures the touch screen on/off state.
    """
    if state is None:
        return _query(resource_name, ":SYSTem:TOUCh?")
    _send(resource_name, f":SYSTem:TOUCh {'ON' if state else 'OFF'}")
    return None


def system_selfcal(resource_name: str) -> str:
    """Start self-calibration and query status.

    SCPI: :SYSTem:SELFCal
           :SYSTem:SELFCal?

        Starts the oscilloscope self-calibration. Query returns status: DOING = calibration in progress, DONE = calibration complete.
    """
    _send(resource_name, ":SYSTem:SELFCal")
    return _query(resource_name, ":SYSTem:SELFCal?")


def system_ssaver(resource_name: str, time_val: str | None = None) -> str | None:
    """Set or query screen saver timeout.

    SCPI: :SYSTem:SSAVer <time>
           :SYSTem:SSAVer?

        Configures the screen saver timeout.
        {OFF|1MIN|5MIN|10MIN|30MIN|60MIN}
    """
    if time_val is None:
        return _query(resource_name, ":SYSTem:SSAVer?")
    _send(resource_name, f":SYSTem:SSAVer {time_val}")
    return None


def system_pon(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query power-on auto-start state.

    SCPI: :SYSTem:PON {ON|OFF}
           :SYSTem:PON?

        Configures the power-on auto-start state.
    """
    if state is None:
        return _query(resource_name, ":SYSTem:PON?")
    _send(resource_name, f":SYSTem:PON {'ON' if state else 'OFF'}")
    return None


def system_edumode(resource_name: str, func: str | None = None, lock: bool | None = None) -> str | None:
    """Set or query education mode lock.

    SCPI: :SYSTem:EDUMode <func>,<lock>
           :SYSTem:EDUMode?

        Configures the education mode function lock.
        <func>:= {AUTOSet|MEASure|CURSor} — function to lock/unlock
        <lock>:= {ON|OFF} — lock or unlock

    Args:
        func: Function to modify {AUTOSet|MEASure|CURSor}, None to query
        lock: True=ON (lock), False=OFF (unlock)
    """
    if func is None:
        return _query(resource_name, ":SYSTem:EDUMode?")
    _send(resource_name, f":SYSTem:EDUMode {func},{'ON' if lock else 'OFF'}")
    return None


def system_vncport(resource_name: str, port: int | None = None) -> str | None:
    """Set or query the VNC port number.

    SCPI: :SYSTem:COMMunicate:VNCPort <value>
           :SYSTem:COMMunicate:VNCPort?

        Configures the VNC port number, range [5900, 5999].
    """
    if port is None:
        return _query(resource_name, ":SYSTem:COMMunicate:VNCPort?")
    _send(resource_name, f":SYSTem:COMMunicate:VNCPort {port}")
    return None


def system_nstorage(resource_name: str, path: str, user: str, pwd: str,
                    anon: str = "ON", auto_con: str = "ON",
                    rem_path: str = "", rem_pwd: str = "") -> None:
    """Configure network storage mount parameters.

    SCPI: :SYSTem:NSTorage <path>,<user>,<pwd>,<anon>,<auto_con>,<rem_path>,<rem_pwd>

        Configures network storage mount parameters.
        <path> — network storage path
        <user> — username
        <pwd> — password
        <anon> — anonymous login toggle {ON|OFF}
        <auto_con> — auto-connect toggle {ON|OFF}
        <rem_path> — remote folder path
        <rem_pwd> — remote folder password
    """
    _send(resource_name, f":SYSTem:NSTorage {path},{user},{pwd},{anon},{auto_con},{rem_path},{rem_pwd}")


def system_nstorage_connect(resource_name: str) -> None:
    """Connect to configured network storage.

    SCPI: :SYSTem:NSTorage:CONNect
    """
    _send(resource_name, ":SYSTem:NSTorage:CONNect")


def system_nstorage_disconnect(resource_name: str) -> None:
    """Disconnect from network storage.

    SCPI: :SYSTem:NSTorage:DISConnect
    """
    _send(resource_name, ":SYSTem:NSTorage:DISConnect")


def system_nstorage_status(resource_name: str) -> str:
    """Query network storage connection status.

    SCPI: :SYSTem:NSTorage:STATus?

    Returns:
        "ON" or "OFF".
    """
    return _query(resource_name, ":SYSTem:NSTorage:STATus?")


def system_menu(resource_name: str, state: bool | None = None) -> str | None:
    """Set or query the menu display on/off state (models with Menu key).

    SCPI: :SYSTem:MENU {ON|OFF}
           :SYSTem:MENU?

        Configures the menu display on/off state (models with Menu key).
    """
    if state is None:
        return _query(resource_name, ":SYSTem:MENU?")
    _send(resource_name, f":SYSTem:MENU {'ON' if state else 'OFF'}")
    return None


def system_lan_type(resource_name: str, lan_type: str | None = None) -> str | None:
    """Set or query the LAN configuration mode.

    SCPI: :SYSTem:COMMunicate:LAN:TYPE <state>
           :SYSTem:COMMunicate:LAN:TYPE?

        Configures the LAN configuration mode.
        STATIC — manual IP configuration
        DHCP  — automatic IP assignment

    Args:
        lan_type: {STATIC|DHCP}

    Returns:
        Current LAN configuration mode when querying.
    """
    if lan_type is None:
        return _query(resource_name, ":SYSTem:COMMunicate:LAN:TYPE?")
    _send(resource_name, f":SYSTem:COMMunicate:LAN:TYPE {lan_type}")
    return None
