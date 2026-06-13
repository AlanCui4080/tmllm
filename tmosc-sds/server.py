from __future__ import annotations

import asyncio, json, logging, sys, os

# Allow import from sibling tmvisa-mcp package
_sibling = os.path.join(os.path.dirname(__file__), "..", "tmvisa-mcp")
if _sibling not in sys.path:
    sys.path.insert(0, _sibling)

from mcp.server.lowlevel import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

import ieee4882
import visa_manager
from visa_manager import detect_instruments, open_instrument, close_instrument, close_all_instruments
from sds_driver import _query
from sds_driver import (
    # Root
    autoset, print_screen, format_data,
    # ACQuire
    acquire_type, acquire_mode, acquire_mdepth, acquire_srate,
    acquire_interpolation, acquire_amode, acquire_numacq,
    acquire_resolution, acquire_sequence, acquire_sequence_count,
    acquire_mmanagement, acquire_points, acquire_csweep,
    # CHANnel
    channel_reference_type, channel_display, channel_coupling,
    channel_bwlimit, channel_impedance, channel_invert,
    channel_offset, channel_scale, channel_probe,
    channel_skew, channel_unit, channel_label, channel_label_state,
    # COUNter
    counter_state, counter_current, counter_level, counter_mode,
    counter_source, counter_statistics, counter_statistics_reset,
    counter_statistics_value, counter_totalizer_gate,
    counter_totalizer_gate_level, counter_totalizer_gate_slope,
    counter_totalizer_gate_type, counter_totalizer_reset,
    counter_totalizer_slope,
    # CURSor common + single
    cursor_state, cursor_tag_style, cursor_x_reference,
    cursor_y_reference, cursor_ixdelta, cursor_measure_item,
    cursor_mode, cursor_source1, cursor_source2,
    cursor_x1, cursor_x2, cursor_xdelta,
    cursor_y1, cursor_y2, cursor_ydelta,
    # CURSor multi: MANual X/Y, MEASure, TRACk
    cursor_manual_x_state, cursor_manual_x_color,
    cursor_manual_x_dfollow, cursor_manual_x_dtcursor,
    cursor_manual_x_dvalue, cursor_manual_x_label,
    cursor_manual_x_position, cursor_manual_x_source,
    cursor_manual_y_state, cursor_manual_y_color,
    cursor_manual_y_dfollow, cursor_manual_y_dtcursor,
    cursor_manual_y_dvalue, cursor_manual_y_label,
    cursor_manual_y_position, cursor_manual_y_source,
    cursor_measure_state, cursor_measure_color,
    cursor_measure_label, cursor_measure_mitem,
    cursor_track_state, cursor_track_color,
    cursor_track_dfollow, cursor_track_dtcursor,
    cursor_track_dvalue, cursor_track_label,
    cursor_track_position, cursor_track_source, cursor_track_value,
    # CURSor multi: XY
    cursor_xy_x_state, cursor_xy_x_color,
    cursor_xy_x_dfollow, cursor_xy_x_dtcursor,
    cursor_xy_x_dvalue, cursor_xy_x_label,
    cursor_xy_x_position,
    cursor_xy_y_state, cursor_xy_y_color,
    cursor_xy_y_dfollow, cursor_xy_y_dtcursor,
    cursor_xy_y_dvalue, cursor_xy_y_label,
    cursor_xy_y_position,
    # DISPlay
    display_axis, display_axis_mode, display_axis_position,
    display_backlight, display_clear, display_color,
    display_graticule, display_grid_style, display_hidemenu,
    display_intensity, display_menu, display_menu_hide,
    display_persistence, display_transparence, display_type,
    # DVM
    dvm_state, dvm_alarm, dvm_autorange, dvm_current,
    dvm_hold, dvm_mode, dvm_source,
    # TIMebase
    timebase_delay, timebase_reference, timebase_reference_position,
    timebase_scale, timebase_window, timebase_window_delay,
    timebase_window_scale,
    # TRIGger
    trigger_mode, trigger_run, trigger_status,
    trigger_stop, trigger_type, trigger_frequency,
    trigger_edge_coupling, trigger_edge_holdoff_devents,
    trigger_edge_holdoff_time, trigger_edge_holdoff,
    trigger_edge_hstart, trigger_edge_impedance,
    trigger_edge_level, trigger_edge_noise_reject,
    trigger_edge_slope, trigger_edge_source,
    trigger_slope_llevel, trigger_slope_hlevel,
    trigger_slope_limit, trigger_slope_slope,
    trigger_slope_tlower, trigger_slope_tupper,
    trigger_pulse_polarity, trigger_pulse_limit,
    trigger_pulse_tlower, trigger_pulse_tupper,
    trigger_video_field, trigger_video_frame_rate,
    trigger_video_interlace, trigger_video_line,
    trigger_video_source, trigger_video_standard,
    trigger_video_sync,
    trigger_window_center_level, trigger_window_delta_level,
    trigger_window_high_level, trigger_window_low_level,
    trigger_window_type,
    trigger_interval_level, trigger_interval_limit,
    trigger_interval_tlower, trigger_interval_tupper,
    trigger_dropout_time, trigger_dropout_type,
    trigger_runt_hlevel, trigger_runt_llevel,
    trigger_runt_limit, trigger_runt_polarity,
    trigger_runt_tlower, trigger_runt_tupper,
    trigger_pattern_input, trigger_pattern_level,
    trigger_pattern_limit, trigger_pattern_logic,
    trigger_pattern_tlower, trigger_pattern_tupper,
    trigger_qualified_source, trigger_qualified_edge_source,
    trigger_qualified_type, trigger_qualified_lower_time,
    trigger_qualified_upper_time,
    trigger_delay_source_a, trigger_delay_source_b,
    trigger_delay_slope_a, trigger_delay_slope_b,
    trigger_delay_level_a, trigger_delay_level_b,
    trigger_nedge_source, trigger_nedge_slope,
    trigger_nedge_idle, trigger_nedge_edge, trigger_nedge_level,
    trigger_shold_type, trigger_shold_clock_source,
    trigger_shold_clock_threshold, trigger_shold_data_source,
    trigger_shold_data_threshold, trigger_shold_slope,
    # Trigger serial
    trigger_serial_type,
    trigger_iic_condition, trigger_iic_address, trigger_iic_addr_length,
    trigger_iic_rw_bit, trigger_iic_scl_source, trigger_iic_scl_threshold,
    trigger_iic_sda_source, trigger_iic_sda_threshold, trigger_iic_value,
    trigger_spi_bit_order, trigger_spi_clk_source, trigger_spi_clk_threshold,
    trigger_spi_cs_source, trigger_spi_cs_threshold, trigger_spi_cs_type,
    trigger_spi_latch_edge, trigger_spi_miso_source, trigger_spi_miso_threshold,
    trigger_spi_mosi_source, trigger_spi_mosi_threshold,
    trigger_spi_ncs_source, trigger_spi_ncs_threshold,
    trigger_uart_baud, trigger_uart_data_length, trigger_uart_parity,
    trigger_uart_stop, trigger_uart_idle,
    trigger_uart_tx_source, trigger_uart_tx_threshold,
    trigger_uart_rx_source, trigger_uart_rx_threshold,
    trigger_uart_data, trigger_uart_data2,
    trigger_uart_condition, trigger_uart_compare,
    trigger_can_baud, trigger_can_id, trigger_can_id_length,
    trigger_can_data, trigger_can_condition, trigger_can_address,
    trigger_lin_standard, trigger_lin_baud, trigger_lin_compare,
    trigger_lin_data, trigger_lin_condition,
    trigger_flexray_frame_compare, trigger_flexray_frame_cycle,
    trigger_flexray_frame_id, trigger_flexray_frame_repetition,
    trigger_canfd_frame_type, trigger_canfd_baud_data,
    trigger_canfd_baud_nominal,
    trigger_iis_audio_variant, trigger_iis_bclk_source,
    trigger_iis_bclk_threshold, trigger_iis_d_source,
    trigger_iis_d_threshold, trigger_iis_ws_source,
    trigger_iis_ws_threshold, trigger_iis_lch, trigger_iis_sbit,
    trigger_iis_bit_order, trigger_iis_data_length,
    trigger_iis_data, trigger_iis_value,
    trigger_iis_condition, trigger_iis_compare,
    trigger_iis_latch_edge,
    trigger_config,
    # WAVeform
    waveform_byteorder, waveform_source, waveform_start,
    waveform_interval, waveform_points, waveform_maxpoint,
    waveform_width, waveform_preamble, waveform_data,
    waveform_sequence as waveform_sequence_frame,
    wavegen_output, wavegen_basic_wave, wavegen_frequency,
    wavegen_amplitude, wavegen_offset, wavegen_duty_cycle,
    # MEASure
    measure_state, measure_mode, measure_advanced_clear,
    measure_advanced_line_number,
    measure_advanced_p_state, measure_advanced_p_source1,
    measure_advanced_p_source2, measure_advanced_p_type,
    measure_advanced_p_value, measure_advanced_statistics,
    measure_advanced_statistics_reset, measure_simple_clear,
    measure_simple_item, measure_simple_source,
    measure_gate, measure_gate_gA, measure_gate_gB,
    measure_astrategy, measure_threshold_source,
    measure_threshold_type, measure_threshold_absolute,
    measure_threshold_percent, measure_rdisplay,
    measure_advanced_style, measure_advanced_p_statistics_value,
    measure_advanced_p_shistory, measure_advanced_statistics_aimlimit,
    measure_advanced_statistics_histogram, measure_advanced_statistics_maxcount,
    measure_astrategy_base, measure_astrategy_top, measure_simple_value,
    measure_dtime_edge1, measure_dtime_edge2,
    measure_dtime_slope1, measure_dtime_slope2,
    measure_dtime_threshold1, measure_dtime_threshold2,
    # SYSTem
    system_buzzer, system_clock, system_date, system_time,
    system_language, system_reboot, system_shutdown,
    system_lan_gateway, system_lan_ip, system_lan_mac,
    system_lan_mask, system_lan_type,
    system_remote, system_touch, system_selfcal,
    system_ssaver, system_pon, system_edumode,
    system_vncport, system_nstorage,
    system_nstorage_connect, system_nstorage_disconnect,
    system_nstorage_status, system_menu,
    # SAVE
    save_setup, save_image, save_csv, save_binary,
    save_matlab, save_reference, save_default,
    # DECode
    decode_state, decode_list_state, decode_list_line,
    decode_list_scroll, decode_list_result,
    decode_bus_state, decode_bus_copy, decode_bus_format,
    decode_bus_protocol, decode_bus_result,
    decode_bus_iic_rwbit, decode_bus_iic_scl_source,
    decode_bus_iic_sda_source,
    # DIGital
    digital_state, digital_active, digital_bus_display,
    digital_bus_default, digital_bus_format, digital_bus_map,
    digital_channel_state, digital_height, digital_label,
    digital_points, digital_position, digital_skew,
    digital_srate, digital_threshold,
    # FUNCtion (Math)
    function_fft_display, function_gvalue,
    function_state, function_average_num, function_diff_dx,
    function_eres_bits, function_fft_autoset,
    function_fft_hcenter, function_fft_hscale,
    function_fft_span, function_fft_load, function_fft_mode,
    function_fft_points, function_fft_reset,
    function_fft_rlevel, function_fft_scale,
    function_fft_search, function_fft_search_excursion,
    function_fft_search_threshold, function_fft_marker_frequency, function_fft_unit,
    function_fft_window,
    function_fft_search_marker, function_fft_search_marker_show,
    function_fft_search_mon, function_fft_search_porder,
    function_fft_search_result, function_fft_search_table,
    function_fft_search_table_delta, function_fft_search_table_frequency,
    function_filter_type, function_filter_hfrequency,
    function_filter_lfrequency,
    function_integrate_gate, function_integrate_offset,
    function_interpolate_coef, function_invert,
    function_label_state, function_label_text,
    function_maxhold_sweeps, function_minhold_sweeps,
    function_operator, function_position, function_scale,
    function_source1, function_source2,
    # HISTORy
    history_state, history_frame, history_interval,
    history_list, history_play, history_time,
    # MEMory
    memory_horizontal_position, memory_horizontal_scale,
    memory_horizontal_sync, memory_import,
    memory_label_state, memory_label_text,
    memory_switch, memory_vertical_position,
    memory_vertical_scale,
    # MTESt (Mask Test)
    mtest_state, mtest_count, mtest_function_buzzer,
    mtest_function_cof, mtest_function_fth,
    mtest_function_sof, mtest_idisplay,
    mtest_mask_create, mtest_mask_load,
    mtest_operate, mtest_reset, mtest_source, mtest_type,
    # RECall
    recall_factory_default, recall_reference, recall_serase,
    recall_setup,
    # REF
    ref_label_state, ref_label_text,
    ref_data, ref_data_source, ref_data_scale, ref_data_position,
    # SEARch
    search_state, search_mode, search_count, search_event,
    search_copy,
    search_edge_source, search_edge_slope, search_edge_level,
    search_slope_source, search_slope_slope,
    search_slope_hlevel, search_slope_llevel,
    search_slope_limit, search_slope_tupper, search_slope_tlower,
    search_pulse_source, search_pulse_polarity,
    search_pulse_level, search_pulse_limit,
    search_pulse_tupper, search_pulse_tlower,
    search_interval_source, search_interval_slope,
    search_interval_level, search_interval_limit,
    search_interval_tupper, search_interval_tlower,
    search_runt_source, search_runt_polarity,
    search_runt_hlevel, search_runt_llevel,
    search_runt_limit, search_runt_tupper, search_runt_tlower,
    # METEr (handheld)
    meter_state, meter_read, meter_configure, meter_configure_set,
    meter_configure_continuity, meter_configure_current_ac,
    meter_configure_current_dc, meter_configure_diode,
    meter_configure_resistance, meter_configure_voltage_ac,
    meter_configure_voltage_dc, meter_configure_capacitance,
    meter_measure_continuity, meter_measure_current_ac,
    meter_measure_current_dc, meter_measure_diode,
    meter_measure_resistance, meter_measure_voltage_ac,
    meter_measure_voltage_dc, meter_measure_capacitance,
    meter_sense_current_ac_null, meter_sense_current_dc_null,
    meter_sense_resistance_null, meter_sense_voltage_ac_null,
    meter_sense_voltage_dc_null, meter_sense_capacitance_null,
)

__version__ = "0.1.0"
logger = logging.getLogger("tmosc.sds.server")

# ── MCP Server ───────────────────────────────────────────────────

_SERVER = Server(
    name="tmosc-sds",
    version=__version__,
    instructions=(
        "tmosc-sds provides LLMs with the ability to control Siglent SDS Series "
        "digital oscilloscopes via SCPI commands over VISA.\n\n"
        "Typical workflow:\n"
        "1. Use visa_list_resources (from tmvisa-mcp) to discover available instruments\n"
        "2. Use visa_open to connect\n"
        "3. Use sds_autoset for quick setup, or configure manually with\n"
        "   sds_channel_config → sds_timebase_config → sds_trigger_config\n"
        "4. Read data with sds_waveform_read or sds_measure\n"
        "5. Optionally save with sds_save\n\n"
        "All SDS-specific tools require resource_name of an already-opened instrument."
    ),
)

# ═══════════════════════════════════════════════════════════════════
#  Tool definitions
# ═══════════════════════════════════════════════════════════════════

TOOLS: list[Tool] = [
    # ── 1. Autoset ──
    Tool(
        name="sds_autoset",
        description=(
            "Run auto-setup on the SDS oscilloscope. "
            "This automatically configures vertical scale, timebase, and trigger "
            "for the active signals."
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {
                    "type": "string",
                    "description": "VISA resource string of the opened SDS instrument.",
                },
            },
            "required": ["resource_name"],
        },
    ),
    # ── 2. Acquire config ──
    Tool(
        name="sds_acquire_config",
        description=(
            "Configure acquisition parameters on the SDS oscilloscope.\n\n"
            "acq_type: Acquisition type (sampling mode) — 'NORMal','PEAK','AVERage','ERES'\n"
            "    When acq_type='AVERage', also set average_count (4-1024, power of 2) — they are combined as 'AVERage,16'\n"
            "    When acq_type='ERES', also set eres_bits (0.5/1.0/1.5/2.0/2.5/3.0)\n"
            "acq_mode: Display mode — 'YT','XY','ROLL' (:ACQuire:MODE)\n"
            "memory_depth: '10K','100K','1M','10M','100M'\n"
            "sample_rate: e.g. '1e9' for 1 GSa/s\n"
            "interpolation: 'LINEar' or 'SINX' (sin(x)/x)\n"
            "acquisition_mode: 'FAST' or 'SLOW' (:ACQuire:AMODe)\n"
            "average_count: 4-1024 (powers of 2), MUST be used together with acq_type='AVERage'\n"
            "eres_bits: 0.5, 1.0, 1.5, 2.0, 2.5, 3.0 (for ERES mode)\n"
            "sequence_enable: True to enable segmented (sequence) mode\n"
            "sequence_count: Number of segments\n"
            "max_memory: 'AUTO' or 'FIXED'\n"
            "sweep: 'AUTO','NORMal','SINGle'\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                "acq_type": {"type": "string", "description": "Acquisition type (:ACQuire:TYPE) — 'NORMal','PEAK','AVERage','ERES'. For AVERage, also pass average_count; for ERES, also pass eres_bits."},
                "acq_mode": {"type": "string", "description": "Display mode (:ACQuire:MODE) — 'YT','XY','ROLL'"},
                "memory_depth": {"type": "string"},
                "sample_rate": {"type": "string"},
                "interpolation": {"type": "string"},
                "acquisition_mode": {"type": "string", "description": "Acquisition filling mode (:ACQuire:AMODe) — 'FAST' or 'SLOW'"},
                "average_count": {"type": "integer", "description": "Average times (4-1024, power of 2). MUST be used together with acq_type='AVERage'."},
                "eres_bits": {"type": "number"},
                "sequence_enable": {"type": "boolean"},
                "sequence_count": {"type": "integer"},
                "max_memory": {"type": "string"},
                "points": {"type": "integer"},
                "sweep": {"type": "string"},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 3. Channel config ──
    Tool(
        name="sds_channel_config",
        description=(
            "Configure a single analog channel on the SDS oscilloscope.\n\n"
            "channel: 1-4 (required)\n"
            "display: True=show, False=hide\n"
            "coupling: 'AC','DC','GND'\n"
            "bandwidth_limit: '20M','200M','FULL'\n"
            "impedance: 'ONEMeg' or 'FIFTy'\n"
            "invert: True to invert waveform\n"
            "offset: Vertical offset in volts\n"
            "scale: Vertical scale in volts/div\n"
            "probe: 'DEF' (default 1X) or a number (attenuation factor, 1E-6 to 1E6, e.g. 100.0 for 100X)\n"
            "skew: Channel deskew in seconds (-100e-9 to 100e-9)\n"
            "unit: 'V' or 'A'\n"
            "label: Channel label (max 20 chars) — auto-enables label display\n"
            "label_state: True to show label, False to hide (default: auto-enabled when label is set)\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                "channel": {"type": "integer", "description": "Channel number (1-4)"},
                "display": {"type": "boolean"},
                "coupling": {"type": "string"},
                "bandwidth_limit": {"type": "string"},
                "impedance": {"type": "string"},
                "invert": {"type": "boolean"},
                "offset": {"type": "number"},
                "scale": {"type": "number"},
                "probe": {"description": "'DEF' (default 1X) or attenuation factor (e.g. 100.0 for 100X)", "anyOf": [{"type": "string"}, {"type": "number"}]},
                "skew": {"type": "number"},
                "unit": {"type": "string"},
                "label": {"type": "string"},
                "label_state": {"type": "boolean", "description": "Show/hide channel label. Auto-enabled when label text is set."},
            },
            "required": ["resource_name", "channel"],
        },
    ),
    # ── 4. Trigger config (ALL types, dynamic SCPI routing) ──
    Tool(
        name="sds_trigger_config",
        description=(
            "Configure trigger settings on the SDS oscilloscope.\n\n"
            "Parameters are type-agnostic — SCPI commands are assembled dynamically\n"
            "as :TRIGger:<trigger_type>:<subcmd> based on the trigger_type you set.\n\n"
            "Set trigger_type FIRST to choose the trigger mode:\n"
            "  EDGE, SLOPe, PULSe, VIDeo, WINDow, INTerval, DROPout,\n"
            "  RUNT, PATTern, QUALified, DELay, NEDGe, SHOLd\n\n"
            "Common (supported by most types):\n"
            "  source: 'C1','C2','C3','C4','LINE','EXT','EXT/5','D0'-'D15'\n"
            "  level: Trigger level in volts\n"
            "  slope: 'RISing','FALLing','ALTernate'\n"
            "  coupling: 'DC','AC','LFREJect','HFREJect'\n"
            "  holdoff, holdoff_time, holdoff_event, holdoff_start\n"
            "  noise_reject: True/False\n"
            "  impedance: 'ONEMeg','FIFTy' (EDGE only)\n\n"
            "Level pair (SLOPe, WINDow, RUNT):\n"
            "  low_level, high_level\n"
            "WINDow-specific: window_type, center_level, delta_level, low_level, high_level\n"
            "DROPout-specific: dropout_type, dropout_time\n"
            "VIDeo-specific: video_standard, video_sync, video_field, video_line, video_frame_rate, video_interlace\n"
            "PATTern-specific: pattern_input, pattern_logic, pattern_level (requires source param)\n"
            "QUALified-specific: qualified_type, edge_source, edge_slope, edge_level, qualified_source, qualified_level\n"
            "DELay dual-source: source_a, source_b, slope_a, slope_b, level_a, level_b\n"
            "NEDGe-specific: idle, edge\n"
            "SHOLd-specific: shold_type, clock_source, clock_threshold, data_source, data_threshold\n"
            "PULSe/SLOPe/INTerval/RUNT/PATTern/QUALified/DELay/SHOLd: limit, lower_time, upper_time\n"
            "PULSe/RUNT: polarity\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                # Global
                "trigger_type": {"type": "string", "description": "Trigger type — set FIRST: EDGE, SLOPe, PULSe, VIDeo, WINDow, INTerval, DROPout, RUNT, PATTern, QUALified, DELay, NEDGe, SHOLd"},
                "trigger_mode": {"type": "string"},
                "force_trigger": {"type": "boolean"},
                "stop": {"type": "boolean", "default": False},
                # Common
                "source": {"type": "string"},
                "level": {"type": "number"},
                "slope": {"type": "string"},
                "coupling": {"type": "string"},
                "holdoff": {"type": "number"},
                "holdoff_event": {"type": "integer"},
                "holdoff_time": {"type": "number"},
                "holdoff_start": {"type": "string"},
                "noise_reject": {"type": "boolean"},
                "impedance": {"type": "string"},
                # Level pair / limit/time
                "low_level": {"type": "number"},
                "high_level": {"type": "number"},
                "limit": {"type": "number"},
                "lower_time": {"type": "number"},
                "upper_time": {"type": "number"},
                "polarity": {"type": "string"},
                # Type-specific
                "window_type": {"type": "string"},
                "center_level": {"type": "number"},
                "delta_level": {"type": "number"},
                "dropout_type": {"type": "string"},
                "dropout_time": {"type": "number"},
                "video_standard": {"type": "string"},
                "video_sync": {"type": "string"},
                "video_field": {"type": "string"},
                "video_line": {"type": "integer"},
                "video_frame_rate": {"type": "string"},
                "video_interlace": {"type": "string"},
                "pattern_input": {"type": "string"},
                "pattern_logic": {"type": "string"},
                "pattern_level": {"type": "number"},
                "qualified_type": {"type": "string"},
                "edge_source": {"type": "string"},
                "edge_slope": {"type": "string"},
                "edge_level": {"type": "number"},
                "qualified_source": {"type": "string"},
                "qualified_level": {"type": "number"},
                "source_a": {"type": "string"},
                "source_b": {"type": "string"},
                "slope_a": {"type": "string"},
                "slope_b": {"type": "string"},
                "level_a": {"type": "number"},
                "level_b": {"type": "number"},
                "idle": {"type": "number"},
                "edge": {"type": "integer"},
                "shold_type": {"type": "string"},
                "clock_source": {"type": "string"},
                "clock_threshold": {"type": "number"},
                "data_source": {"type": "string"},
                "data_threshold": {"type": "number"},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 5. Timebase config ──
    Tool(
        name="sds_timebase_config",
        description=(
            "Configure timebase/horizontal settings on the SDS oscilloscope.\n\n"
            "scale: Horizontal scale in seconds/div\n"
            "delay: Horizontal delay/position in seconds\n"
            "reference: 'DELay' or 'POSition'\n"
            "reference_position: 0-100 (%)\n"
            "window_enable: Enable zoom window\n"
            "window_scale: Zoom window scale (s/div)\n"
            "window_delay: Zoom window delay (s)\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                "scale": {"type": "number"},
                "delay": {"type": "number"},
                "reference": {"type": "string"},
                "reference_position": {"type": "number"},
                "window_enable": {"type": "boolean"},
                "window_scale": {"type": "number"},
                "window_delay": {"type": "number"},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 6. Measure ──
    Tool(
        name="sds_measure",
        description=(
            "Perform measurements on the SDS oscilloscope. Supports simple and advanced measurements.\n\n"
            "Simple measurement (quick, all parameters at once):\n"
            "  source: 'C1'-'C4','MATH1'-'MATH4'\n"
            "  items: List of measurement items. Can include: 'AMPLitude','FREQuency','PERiod',\n"
            "    'PKPK','MAXimum','MINimum','HIGH','LOW','RMS','MEAN','RISe','FALL',\n"
            "    'WIDth','NWIDth','PWIDth','DUTY','NDUTY','BWIDth','OVERshoot','NOVershoot',\n"
            "    'DELay','PHAse','BASE','TOP','STDdev','ROOT','CMEan','COVer','CROot',\n"
            "    'FALLOVER','RISEOVER','POVershoot','CLEVel','AREa','ALL'\n\n"
            "Advanced measurement (single parameter, with statistics):\n"
            "  param_index: 1-5\n"
            "  source1, source2: Channel sources\n"
            "  meas_type: Same items as above\n"
            "  show_stats: Show statistics\n"
            "  show_history: Show measurement history\n\n"
            "Measurement gate:\n"
            "  gate_enable: Enable measurement gate\n"
            "  gate_a, gate_b: Gate boundaries (0.0-1.0, fraction of screen)\n\n"
            "Threshold:\n"
            "  threshold_type: 'ABSolute' or 'PERCent'\n"
            "  absolute_low/mid/high: Absolute thresholds (V)\n"
            "  percent_low/mid/high: Percentage thresholds (0-100)\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                "source": {"type": "string", "default": "C1"},
                "items": {"type": "array", "items": {"type": "string"}},
                "clear": {"type": "boolean", "default": False},
                "state": {"type": "boolean", "description": "Enable/disable measurements"},
                "mode": {"type": "string", "description": "Measurement mode: 'M1' (simple) or 'M2' (advanced)"},
                "advanced_line_number": {"type": "integer", "description": "Number of advanced measurement lines (1-12)"},
                # Advanced
                "param_index": {"type": "integer"},
                "source1": {"type": "string"},
                "source2": {"type": "string"},
                "meas_type": {"type": "string"},
                "show_stats": {"type": "boolean"},
                "show_history": {"type": "boolean"},
                "stats_reset": {"type": "boolean"},
                "style": {"type": "string"},
                "strategy_auto": {"type": "string"},
                "strategy_base": {"type": "string"},
                "strategy_top": {"type": "string"},
                # Gate
                "gate_enable": {"type": "boolean"},
                "gate_a": {"type": "number"},
                "gate_b": {"type": "number"},
                # Threshold
                "threshold_type": {"type": "string"},
                "absolute_low": {"type": "number"},
                "absolute_mid": {"type": "number"},
                "absolute_high": {"type": "number"},
                "percent_low": {"type": "number"},
                "percent_mid": {"type": "number"},
                "percent_high": {"type": "number"},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 7. Waveform read ──
    Tool(
        name="sds_waveform_read",
        description=(
            "Read waveform data from the SDS oscilloscope. Returns voltage array and preamble.\n\n"
            "source: 'C1','C2','C3','C4','F1','F2','M1'-'M4'\n"
            "start: First data point (0-based)\n"
            "points: Number of points (0 = max available)\n"
            "sparsing: Point interval (1 = every point)\n"
            "byte_order: 'LSBFirst' (default) or 'MSBFirst'\n\n"
            "Returns: { preamble: {...}, voltage_data: [...], points: N, source: 'C1' }\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                "source": {"type": "string", "default": "C1"},
                "start": {"type": "integer", "default": 0},
                "points": {"type": "integer", "default": 0},
                "sparsing": {"type": "integer", "default": 1},
                "byte_order": {"type": "string", "default": "LSBFirst"},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 8. Display config ──
    Tool(
        name="sds_display_config",
        description=(
            "Configure display settings on the SDS oscilloscope.\n\n"
            "type_: 'VECTor' or 'DOT'\n"
            "persistence: 'OFF','INFinite','100MS','200MS','500MS','1S','5S','10S','30S'\n"
            "grid_style: 'FULL','LIGHt','NONE'\n"
            "intensity: Waveform intensity 0-100\n"
            "backlight: Backlight 0-100\n"
            "color: True/False — enable/disable color temperature\n"
            "graticule: Grid brightness 0-100\n"
            "axis_mode: 'MOVING','FIXED'\n"
            "axis_position: 'POSITION','SOURCE'\n"
            "transparent: Menu transparency 0-100\n"
            "hide_menu: Menu auto-hide timeout — 'OFF','3S','5S','10S','30S','60S'\n"
            "clear_persistence: Clear persistence display\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                "type_": {"type": "string"},
                "persistence": {"type": "string", "description": "Persistence time: 'OFF','INFinite','100MS','200MS','500MS','1S','5S','10S','30S' (model-dependent)"},
                "grid_style": {"type": "string"},
                "intensity": {"type": "integer"},
                "backlight": {"type": "integer"},
                "color": {"type": "boolean"},
                "graticule": {"type": "integer", "description": "Grid brightness 0-100"},
                "axis_mode": {"type": "string"},
                "axis_position": {"type": "string"},
                "transparent": {"type": "integer"},
                "hide_menu": {"type": "string", "description": "Menu auto-hide timeout: 'OFF','3S','5S','10S','30S','60S'"},
                "clear_persistence": {"type": "boolean", "default": False},
                "axis": {"type": "boolean", "description": "Show/hide axis labels"},
                "menu": {"type": "string", "description": "Menu display style"},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 9. Cursor config ──
    Tool(
        name="sds_cursor_config",
        description=(
            "Configure cursor measurements on the SDS oscilloscope.\n\n"
            "mode: 'OFF','MANual','MANual,X','MANual,Y','MANual,XY','TRACk','MEASure'\n"
            "source1: Cursor source — 'C1'-'C4','F1'-'F4','M1'-'M4','REF1'-'REF4','DIGital','HISTOGram'\n"
            "source2: Cursor source — same options as source1\n"
            "x1, x2: X cursor positions (seconds)\n"
            "y1, y2: Y cursor positions (volts)\n"
            "tag_style: 'FIXed' or 'FOLLowing'\n"
            "xreference: 'DELay' or 'POSition'\n"
            "yreference: 'OFFSet' or 'POSition'\n"
            "measure_item: Measurement item with source, e.g. 'PKPK,C2'\n"
            "read: True to read current delta values (xdelta, ydelta, ixdelta)\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                "mode": {"type": "string"},
                "source1": {"type": "string"},
                "source2": {"type": "string"},
                "x1": {"type": "number"},
                "x2": {"type": "number"},
                "y1": {"type": "number"},
                "y2": {"type": "number"},
                "tag_style": {"type": "string"},
                "xreference": {"type": "string"},
                "yreference": {"type": "string"},
                "measure_item": {"type": "string"},
                "read": {"type": "boolean", "default": False},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 10. Decode config ──
    Tool(
        name="sds_decode_config",
        description=(
            "Configure serial bus decode on the SDS oscilloscope.\n\n"
            "Supports: IIC (I²C), SPI, UART, CAN, LIN, CANFd, FLEXray, IIS, M1553, SENT, MANChester\n\n"
            "bus: Decode bus number (1 or 2)\n"
            "protocol: Protocol name\n"
            "format: 'HEX','BIN','DEC','ASCii'\n"
            "display: Show/hide decode\n"
            "list_enable: Show decode list\n"
            "read_result: Read current decode values\n\n"
            "Protocol-specific source/threshold pairs (use as needed):\n"
            "I²C: i2c_scl_source, i2c_scl_threshold, i2c_sda_source, i2c_sda_threshold, i2c_rw_bit\n"
            "SPI: spi_clk_source, spi_clk_threshold, spi_cs_source, spi_cs_threshold, spi_cs_type,\n"
            "     spi_miso_source, spi_miso_threshold, spi_mosi_source, spi_mosi_threshold,\n"
            "     spi_ncs_source, spi_ncs_threshold, spi_bit_order, spi_latch_edge, spi_data_length\n"
            "UART: uart_baud, uart_bit_order, uart_data_length, uart_idle, uart_parity,\n"
            "      uart_rx_source, uart_rx_threshold, uart_stop, uart_tx_source, uart_tx_threshold\n"
            "CAN: can_baud, can_source, can_threshold\n"
            "LIN: lin_baud, lin_source, lin_threshold\n"
            "CAN FD: canfd_baud_data, canfd_baud_nominal, canfd_source, canfd_threshold\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                "bus": {"type": "integer", "default": 1},
                "protocol": {"type": "string"},
                "format": {"type": "string"},
                "display": {"type": "boolean"},
                "list_enable": {"type": "boolean"},
                "read_result": {"type": "boolean", "default": False},
                # I2C
                "i2c_scl_source": {"type": "string"},
                "i2c_scl_threshold": {"type": "number"},
                "i2c_sda_source": {"type": "string"},
                "i2c_sda_threshold": {"type": "number"},
                "i2c_rw_bit": {"type": "string"},
                # SPI
                "spi_clk_source": {"type": "string"},
                "spi_clk_threshold": {"type": "number"},
                "spi_cs_source": {"type": "string"},
                "spi_cs_threshold": {"type": "number"},
                "spi_cs_type": {"type": "string"},
                "spi_miso_source": {"type": "string"},
                "spi_miso_threshold": {"type": "number"},
                "spi_mosi_source": {"type": "string"},
                "spi_mosi_threshold": {"type": "number"},
                "spi_ncs_source": {"type": "string"},
                "spi_ncs_threshold": {"type": "number"},
                "spi_bit_order": {"type": "string"},
                "spi_latch_edge": {"type": "string"},
                "spi_data_length": {"type": "integer"},
                # UART
                "uart_baud": {"type": "integer"},
                "uart_bit_order": {"type": "string"},
                "uart_data_length": {"type": "integer"},
                "uart_idle": {"type": "string"},
                "uart_parity": {"type": "string"},
                "uart_rx_source": {"type": "string"},
                "uart_rx_threshold": {"type": "number"},
                "uart_stop": {"type": "string"},
                "uart_tx_source": {"type": "string"},
                "uart_tx_threshold": {"type": "number"},
                # CAN
                "can_baud": {"type": "integer"},
                "can_source": {"type": "string"},
                "can_threshold": {"type": "number"},
                # LIN
                "lin_baud": {"type": "integer"},
                "lin_source": {"type": "string"},
                "lin_threshold": {"type": "number"},
                # CAN FD
                "canfd_baud_data": {"type": "integer"},
                "canfd_baud_nominal": {"type": "integer"},
                "canfd_source": {"type": "string"},
                "canfd_threshold": {"type": "number"},
                "state": {"type": "boolean", "description": "Overall decode on/off state"},
                "list_lines": {"type": "integer", "description": "Number of decode list lines"},
                "list_scroll": {"type": "integer", "description": "Scroll decode list to row"},
                "bus_result_read": {"type": "boolean", "default": False, "description": "Read bus decode result"},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 11. Search config ──
    Tool(
        name="sds_search_config",
        description=(
            "Configure event search/find on the SDS oscilloscope.\n\n"
            "Search types: EDGE, SLOPe, PULSe, INTerval, RUNT\n\n"
            "mode: 'ON','OFF'\n"
            "search_type: Event type to search for\n"
            "copy_to_trigger: Copy search settings to trigger\n"
            "read_count: Read number of events found\n"
            "read_event: Read current event position\n\n"
            "Type-specific parameters:\n"
            "Edge: edge_source, edge_slope, edge_level\n"
            "Slope: slope_source, slope_slope, slope_high_level, slope_low_level,\n"
            "       slope_limit_low, slope_limit_up, slope_upper_time, slope_lower_time\n"
            "Pulse: pulse_source, pulse_polarity, pulse_level,\n"
            "       pulse_limit_low, pulse_limit_up, pulse_upper_time, pulse_lower_time\n"
            "Interval: interval_source, interval_slope, interval_level, etc.\n"
            "Runt: runt_source, runt_polarity, runt_high_level, runt_low_level, etc.\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                "mode": {"type": "string"},
                "search_type": {"type": "string"},
                "copy_to_trigger": {"type": "boolean", "default": False},
                "read_count": {"type": "boolean", "default": False},
                "read_event": {"type": "boolean", "default": False},
                # Edge
                "edge_source": {"type": "string"},
                "edge_slope": {"type": "string"},
                "edge_level": {"type": "number"},
                # Slope
                "slope_source": {"type": "string"},
                "slope_slope": {"type": "string"},
                "slope_high_level": {"type": "number"},
                "slope_low_level": {"type": "number"},
                "slope_limit_low": {"type": "number"},
                "slope_limit_up": {"type": "number"},
                "slope_upper_time": {"type": "number"},
                "slope_lower_time": {"type": "number"},
                # Pulse
                "pulse_source": {"type": "string"},
                "pulse_polarity": {"type": "string"},
                "pulse_level": {"type": "number"},
                "pulse_limit_low": {"type": "number"},
                "pulse_limit_up": {"type": "number"},
                "pulse_upper_time": {"type": "number"},
                "pulse_lower_time": {"type": "number"},
                # Interval
                "interval_source": {"type": "string"},
                "interval_slope": {"type": "string"},
                "interval_level": {"type": "number"},
                "interval_limit_low": {"type": "number"},
                "interval_limit_up": {"type": "number"},
                "interval_upper_time": {"type": "number"},
                "interval_lower_time": {"type": "number"},
                # Runt
                "runt_source": {"type": "string"},
                "runt_polarity": {"type": "string"},
                "runt_high_level": {"type": "number"},
                "runt_low_level": {"type": "number"},
                "runt_limit_low": {"type": "number"},
                "runt_limit_up": {"type": "number"},
                "runt_upper_time": {"type": "number"},
                "runt_lower_time": {"type": "number"},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 12. Save ──
    Tool(
        name="sds_save",
        description=(
            "Save data from the SDS oscilloscope to the instrument's storage.\n\n"
            "save_type: 'CSV','BINary','IMAGe','MATLab','SETup','REFerence'\n"
            "filename: File path on the instrument\n"
            "source: Source for data save ('C1'-'C4','F1','F2','M1'-'M4')\n"
            "setup_type: 'SETup' or 'REFerence'\n"
            "binary_source: Source for binary save\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                "save_type": {"type": "string", "default": "CSV"},
                "filename": {"type": "string"},
                "source": {"type": "string", "default": "C1"},
                "setup_type": {"type": "string"},
                "default_setup": {"type": "integer"},
                "binary_source": {"type": "string"},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 13. System config ──
    Tool(
        name="sds_system_config",
        description=(
            "Configure system settings on the SDS oscilloscope.\n\n"
            "buzzer: Enable/disable buzzer\n"
            "date: Set system date (YYYY-MM-DD)\n"
            "time_: Set system time (HH:MM:SS)\n"
            "language: 'ENGLish','CHINese', etc.\n"
            "remote_lock: Lock front panel\n"
            "touch: Enable/disable touch\n"
            "screen_saver: Enable/disable screen saver\n"
            "edu_mode: Enable education mode\n"
            "lan_ip: LAN IP address\n"
            "lan_mask: LAN subnet mask\n"
            "lan_gateway: LAN gateway\n"
            "lan_type: 'DHCP' or 'STATIC'\n"
            "vnc_port: VNC port\n"
            "network_storage: Enable network storage\n"
            "network_storage_connect: Path to network storage\n"
            "network_storage_disconnect: Disconnect\n"
            "reboot: Reboot (use with caution!)\n"
            "shutdown: Shutdown (use with caution!)\n"
            "self_cal: Run self-calibration\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                "buzzer": {"type": "boolean"},
                "date": {"type": "string"},
                "time_": {"type": "string"},
                "language": {"type": "string"},
                "remote_lock": {"type": "boolean"},
                "touch": {"type": "boolean"},
                "screen_saver": {"type": "boolean"},
                "edu_mode": {"type": "boolean"},
                "lan_ip": {"type": "string"},
                "lan_mask": {"type": "string"},
                "lan_gateway": {"type": "string"},
                "lan_type": {"type": "string"},
                "vnc_port": {"type": "integer"},
                "network_storage": {"type": "boolean"},
                "network_storage_connect": {"type": "string"},
                "network_storage_disconnect": {"type": "boolean", "default": False},
                "reboot": {"type": "boolean", "default": False},
                "shutdown": {"type": "boolean", "default": False},
                "self_cal": {"type": "boolean", "default": False},
                "clock_source": {"type": "string", "description": "Clock source ('INTernal' or 'EXTernal')"},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 14. Math config ──
    Tool(
        name="sds_math_config",
        description=(
            "Configure math functions on the SDS oscilloscope (FFT, filter, operations).\n\n"
            "func_index: Math function index (1-4)\n"
            "operation: 'ADD','SUB','MULT','DIV','DIFF','INTG','SQRT','FFT','FILT','ERES','AVG','MAXH','MINH','INTERPOLATE'\n"
            "source1, source2: Source channels ('C1'-'C4')\n"
            "display: Show/hide math trace\n"
            "label: Custom label\n"
            "invert: Invert waveform\n"
            "position, scale: Vertical position/scale\n\n"
            "FFT settings:\n"
            "  fft_display: 'SPLIT','FULL','EXCLusive'\n"
            "  fft_mode: 'NORMal','AVERage','MAXHold'\n"
            "  fft_window: 'RECTangular','BLACkman','HANNing','HAMMing','FLATtop'\n"
            "  fft_points: Power of 2 (1024, 2048, ...)\n"
            "  fft_unit: 'dBVrms','Vrms','dBm'\n"
            "  fft_scale: 'LINear','LOGarithmic'\n"
            "  fft_center: Center frequency (Hz)\n"
            "  fft_span: Span (Hz)\n"
            "  fft_ref_level: Reference level (dB)\n"
            "  fft_auto: Run FFT auto setup\n"
            "  fft_reset: Reset FFT\n\n"
            "Filter settings:\n"
            "  filter_type: 'LOWPass','HIGHPass','BANDPass','BANDStop'\n"
            "  filter_low_freq, filter_high_freq: Cutoff frequencies (Hz)\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                "func_index": {"type": "integer", "default": 1},
                "operation": {"type": "string"},
                "source1": {"type": "string"},
                "source2": {"type": "string"},
                "display": {"type": "boolean"},
                "label": {"type": "string"},
                "invert": {"type": "boolean"},
                "position": {"type": "number"},
                "scale": {"type": "number"},
                "average_count": {"type": "integer"},
                "diff_dx": {"type": "number"},
                "eres_bits": {"type": "number"},
                # FFT
                "fft_display": {"type": "string"},
                "fft_auto": {"type": "boolean", "default": False},
                "fft_mode": {"type": "string"},
                "fft_window": {"type": "string"},
                "fft_points": {"type": "integer"},
                "fft_unit": {"type": "string"},
                "fft_scale": {"type": "string"},
                "fft_center": {"type": "number"},
                "fft_span": {"type": "number"},
                "fft_ref_level": {"type": "number"},
                "fft_reset": {"type": "boolean", "default": False},
                # Filter
                "filter_type": {"type": "string"},
                "filter_low_freq": {"type": "number"},
                "filter_high_freq": {"type": "number"},
                "integrate_gate": {"type": "boolean", "description": "Enable integrate gate"},
                "integrate_offset": {"type": "number", "description": "Integrate operator offset"},
                "interpolate_coef": {"type": "integer", "description": "Interpolate coefficient (2,5,10,20)"},
                "label_state": {"type": "boolean", "description": "Show/hide math label"},
                "maxhold_sweeps": {"type": "integer", "description": "Max-hold sweep count (0=unlimited)"},
                "minhold_sweeps": {"type": "integer", "description": "Min-hold sweep count (0=unlimited)"},
                "fft_load": {"type": "integer", "description": "FFT external load in ohms (for dBm unit)"},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 15. DVM config ──
    Tool(
        name="sds_dvm_config",
        description=(
            "Configure the built-in Digital Voltmeter on the SDS oscilloscope (optional).\n\n"
            "mode: 'OFF','ACRMS','DC','DCAC'\n"
            "source: Source channel\n"
            "alarm: Enable alarm\n"
            "auto_range: Auto-ranging\n"
            "hold: Hold reading\n"
            "read: Read current value\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                "mode": {"type": "string"},
                "source": {"type": "string"},
                "alarm": {"type": "boolean"},
                "auto_range": {"type": "boolean"},
                "hold": {"type": "boolean"},
                "read": {"type": "boolean", "default": False},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 16. Counter config ──
    Tool(
        name="sds_counter_config",
        description=(
            "Configure the built-in frequency counter on the SDS oscilloscope.\n\n"
            "mode: 'FREQuency','PERiod','TOTal'\n"
            "source: 'C1'-'C4'\n"
            "level: Trigger level\n"
            "statistics: Show statistics\n"
            "stats_reset: Reset statistics\n"
            "read_current: Read current value\n"
            "read_stats: Read statistics values\n\n"
            "Totalizer (for TOTal mode):\n"
            "totalizer_gate: Enable gate (True/False)\n"
            "totalizer_gate_level: Gate trigger level\n"
            "totalizer_gate_slope: 'RISing','FALLing'\n"
            "totalizer_gate_type: 'LEVel','EDGE'\n"
            "totalizer_reset: Reset totalizer count\n"
            "totalizer_slope: Input slope 'RISing','FALLing'\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                "mode": {"type": "string"},
                "source": {"type": "string"},
                "level": {"type": "number"},
                "state": {"type": "boolean", "description": "Enable/disable counter"},
                "statistics": {"type": "boolean"},
                "stats_reset": {"type": "boolean", "default": False},
                "read_current": {"type": "boolean", "default": False},
                "read_stats": {"type": "boolean", "default": False},
                "totalizer_gate": {"type": "boolean"},
                "totalizer_gate_level": {"type": "number"},
                "totalizer_gate_slope": {"type": "string"},
                "totalizer_gate_type": {"type": "string"},
                "totalizer_reset": {"type": "boolean", "default": False},
                "totalizer_slope": {"type": "string"},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 17. Mask test ──
    Tool(
        name="sds_mask_test_config",
        description=(
            "Configure mask/pass-fail testing on the SDS oscilloscope.\n\n"
            "enable: Start/stop mask test\n"
            "source: Test source channel\n"
            "test_type: 'HORizontal','VERTical','BOTH'\n"
            "create_mask: Create mask from current waveform\n"
            "load_mask: Load mask file\n"
            "count: Number of tests (0=continuous)\n"
            "reset: Reset count\n"
            "display: Show mask info\n"
            "buzzer: Enable buzzer on fail\n"
            "stop_on_fail: Stop on failure\n"
            "fail_on_test: Enable pass/fail test\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                "enable": {"type": "boolean"},
                "source": {"type": "string"},
                "test_type": {"type": "string"},
                "create_mask": {"type": "boolean", "default": False},
                "load_mask": {"type": "string"},
                "count": {"type": "integer"},
                "reset": {"type": "boolean", "default": False},
                "display": {"type": "boolean"},
                "buzzer": {"type": "boolean"},
                "stop_on_fail": {"type": "boolean"},
                "fail_on_test": {"type": "boolean"},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 18. WaveGen config ──
    Tool(
        name="sds_wavegen_config",
        description=(
            "Configure the built-in waveform generator (if AWG option is installed).\n\n"
            "output: Enable/disable output\n"
            "sync_output: Enable sync output\n"
            "voltage_protection: Over-voltage protection\n"
            "wave_type: 'ARBWaVe','BaSic_WaVe','MODulation','SWEep','BURSt'\n"
            "basic_wave: 'SINE','SQUare','RAMP','PULSe','DC','NOISe',\n"
            "           'SINC','EXPRise','EXPFall','ECG','GAUSsian','LORentz','DAMPed'\n"
            "frequency: Output frequency (Hz)\n"
            "amplitude: Peak-to-peak amplitude (V)\n"
            "offset: DC offset (V)\n"
            "duty_cycle: Duty cycle 0-100%\n"
            "symmetry: Symmetry 0-100%\n"
            "phase: Phase 0-360°\n"
            "arb_name: Arbitrary waveform name\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                "output": {"type": "boolean"},
                "sync_output": {"type": "boolean"},
                "voltage_protection": {"type": "boolean"},
                "wave_type": {"type": "string"},
                "basic_wave": {"type": "string"},
                "frequency": {"type": "number"},
                "amplitude": {"type": "number"},
                "offset": {"type": "number"},
                "duty_cycle": {"type": "number"},
                "symmetry": {"type": "number"},
                "phase": {"type": "number"},
                "arb_name": {"type": "string"},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 19. Channel reference strategy ──
    Tool(
        name="sds_channel_reference",
        description=(
            "Set or query the vertical reference strategy for ALL channels.\n\n"
            "This is NOT about REF waveforms — it controls how the waveform behaves when\n"
            "vertical scale is changed globally (:CHANnel:REFerence).\n\n"
            "ref_type: 'OFFSet' — voltage offset stays fixed; waveform expands/contracts around screen X-axis\n"
            "         'POSition' — grid position stays fixed; waveform expands/contracts around fixed screen location\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                "ref_type": {"type": "string", "description": "'OFFSet' or 'POSition'"},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 20. Trigger query ──
    Tool(
        name="sds_trigger_query",
        description=(
            "Query trigger status and/or frequency counter reading on the SDS oscilloscope.\n\n"
            "read_status: Read current trigger status (READY, TRIGGERED, AUTO, STOP, ROLL)\n"
            "read_frequency: Read trigger frequency counter\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                "read_status": {"type": "boolean", "default": False},
                "read_frequency": {"type": "boolean", "default": False},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 21. Waveform preamble ──
    Tool(
        name="sds_waveform_preamble",
        description=(
            "Read only the waveform preamble (metadata without data transfer).\n\n"
            "source: 'C1','C2','C3','C4','F1','F2','M1'-'M4'\n"
            "Returns preamble dict with format, type, points, count, xincrement, xorigin,\n"
            "xreference, yincrement, yorigin, yreference.\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                "source": {"type": "string", "default": "C1"},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 22. Measure delay-time ──
    Tool(
        name="sds_measure_dtime",
        description=(
            "Configure delay-time measurement settings on the SDS oscilloscope.\n\n"
            "index: DTIMe parameter index (1 or 2)\n"
            "edge1: Edge number for start (1-9)\n"
            "edge2: Edge number for stop (1-9)\n"
            "slope1: Slope for start ('RISing','FALLing')\n"
            "slope2: Slope for stop ('RISing','FALLing')\n"
            "threshold1: Threshold for start (0-100%)\n"
            "threshold2: Threshold for stop (0-100%)\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                "index": {"type": "integer", "default": 1},
                "edge1": {"type": "integer"},
                "edge2": {"type": "integer"},
                "slope1": {"type": "string"},
                "slope2": {"type": "string"},
                "threshold1": {"type": "number"},
                "threshold2": {"type": "number"},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 23. Math FFT marker ──
    Tool(
        name="sds_math_fft_marker",
        description=(
            "Configure FFT peak markers and search on the SDS oscilloscope.\n\n"
            "func_index: Math function index (1-4)\n"
            "marker: Marker number (1-8)\n"
            "frequency: Set marker frequency (Hz)\n"
            "show: Show/hide marker\n"
            "harmonic_peak: 'HARMonic' or 'PEAK'\n"
            "peak_order: Peak order for search (1-20)\n"
            "excursion: Peak excursion threshold (dB)\n"
            "threshold: Peak threshold (dB)\n"
            "read_table: Read peak table\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                "func_index": {"type": "integer", "default": 1},
                "marker": {"type": "integer", "default": 1},
                "frequency": {"type": "number"},
                "show": {"type": "boolean"},
                "harmonic_peak": {"type": "string"},
                "peak_order": {"type": "integer"},
                "excursion": {"type": "number"},
                "threshold": {"type": "number"},
                "read_table": {"type": "boolean", "default": False},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 24. History config ──
    Tool(
        name="sds_history_config",
        description=(
            "Configure history (segmented memory playback) on the SDS oscilloscope.\n\n"
            "frame: Go to specific frame number\n"
            "interval: Playback interval (1-20)\n"
            "play: Playback control ('STOP','PLAY','PAUSE')\n"
            "time_: Go to time offset ('YYYY-MM-DD HH:MM:SS')\n"
            "read_list: Read history frame list\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                "frame": {"type": "integer"},
                "interval": {"type": "integer"},
                "play": {"type": "string"},
                "time_": {"type": "string"},
                "read_list": {"type": "boolean", "default": False},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 25. Recall config ──
    Tool(
        name="sds_recall_config",
        description=(
            "Recall settings or reference waveforms on the SDS oscilloscope.\n\n"
            "setup_file: Setup file path to recall\n"
            "reference_file: Reference waveform file path to recall\n"
            "factory_default: Recall factory defaults\n"
            "secure_erase: Secure erase all memory (use with caution!)\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                "setup_file": {"type": "string"},
                "reference_file": {"type": "string"},
                "factory_default": {"type": "boolean", "default": False},
                "secure_erase": {"type": "boolean", "default": False},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 26. Meter config ──
    Tool(
        name="sds_meter_config",
        description=(
            "Configure the built-in multimeter on the SDS oscilloscope (if option installed).\n\n"
            "function: Measurement function — 'VOLTage:AC','VOLTage:DC','CURRent:AC',\n"
            "          'CURRent:DC','RESistance','CAPacitance','DIODe','CONTinuity'\n"
            "read: Read current measurement value\n"
            "auto_null: Enable auto-null\n"
            "select_range: Manual range setting\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                "function": {"type": "string"},
                "read": {"type": "boolean", "default": False},
                "auto_null": {"type": "boolean"},
                "select_range": {"type": "number"},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 27. Format data ──
    Tool(
        name="sds_format_data",
        description=(
            "Set or query waveform transfer format on the SDS oscilloscope.\n\n"
            "data_type: 'WORD' (16-bit signed), 'BYTE' (8-bit signed), or 'ASCii'\n"
            "If data_type is omitted (None), queries and returns the current format.\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                "data_type": {"type": "string"},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 28. Print screen ──
    Tool(
        name="sds_print_screen",
        description="Print the screen of the SDS oscilloscope (if printer is connected).",
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 29. Cursor multi config ──
    Tool(
        name="sds_cursor_multi_config",
        description=(
            "Configure multi-cursor settings on the SDS oscilloscope:\n"
            "MANual (manual), MEASure, TRACk, and XY cursor types.\n\n"
            "MANual X: manual_x_index, manual_x_{color,follow,dtcursor,dvalue,label,position,source}\n"
            "MANual Y: manual_y_index, manual_y_{color,follow,dtcursor,dvalue,label,position,source}\n"
            "MEASure: measure_index, measure_{color,label,item}\n"
            "TRACk: track_index, track_{color,follow,dtcursor,dvalue,label,position,source,value}\n"
            "XY: xy_x_index, xy_x_{color,follow,dtcursor,dvalue,label,position}\n"
            "     xy_y_index, xy_y_{color,follow,dtcursor,dvalue,label,position}\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                # MANual X
                "manual_x_index": {"type": "integer"},
                "manual_x_color": {"type": "string"},
                "manual_x_follow": {"type": "boolean"},
                "manual_x_dtcursor": {"type": "string"},
                "manual_x_dvalue": {"type": "number"},
                "manual_x_label": {"type": "string"},
                "manual_x_position": {"type": "number"},
                "manual_x_source": {"type": "string"},
                # MANual Y
                "manual_y_index": {"type": "integer"},
                "manual_y_color": {"type": "string"},
                "manual_y_follow": {"type": "boolean"},
                "manual_y_dtcursor": {"type": "string"},
                "manual_y_dvalue": {"type": "number"},
                "manual_y_label": {"type": "string"},
                "manual_y_position": {"type": "number"},
                "manual_y_source": {"type": "string"},
                # MEASure
                "measure_index": {"type": "integer"},
                "measure_color": {"type": "string"},
                "measure_label": {"type": "string"},
                "measure_item": {"type": "string"},
                # TRACk
                "track_index": {"type": "integer"},
                "track_color": {"type": "string"},
                "track_follow": {"type": "boolean"},
                "track_dtcursor": {"type": "string"},
                "track_dvalue": {"type": "number"},
                "track_label": {"type": "string"},
                "track_position": {"type": "number"},
                "track_source": {"type": "string"},
                "track_value": {"type": "number"},
                # XY
                "xy_x_index": {"type": "integer"},
                "xy_x_color": {"type": "string"},
                "xy_x_follow": {"type": "boolean"},
                "xy_x_dtcursor": {"type": "string"},
                "xy_x_dvalue": {"type": "number"},
                "xy_x_label": {"type": "string"},
                "xy_x_position": {"type": "number"},
                "xy_y_index": {"type": "integer"},
                "xy_y_color": {"type": "string"},
                "xy_y_follow": {"type": "boolean"},
                "xy_y_dtcursor": {"type": "string"},
                "xy_y_dvalue": {"type": "number"},
                "xy_y_label": {"type": "string"},
                "xy_y_position": {"type": "number"},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 30. Digital config ──
    Tool(
        name="sds_digital_config",
        description=(
            "Configure digital channels on the SDS oscilloscope (requires digital option).\n\n"
            "active: Show/hide digital channels\n"
            "height: Digital channel display height\n"
            "points: Digital acquisition points\n"
            "position: Vertical position\n"
            "skew: Deskew time (s)\n"
            "sample_rate: Digital sample rate\n"
            "bus: Digital bus number (1-2)\n"
            "bus_display: Show digital bus\n"
            "bus_default: Reset bus to defaults\n"
            "bus_format: 'HEX','BIN','DEC','ASCii'\n"
            "bus_map: Channel mapping string\n"
            "threshold: Array of threshold voltages\n"
            "label_d0..label_d15: Digital channel labels\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                "active": {"type": "boolean"},
                "height": {"type": "number"},
                "points": {"type": "integer"},
                "position": {"type": "number"},
                "skew": {"type": "number"},
                "sample_rate": {"type": "string"},
                "bus": {"type": "integer"},
                "bus_display": {"type": "boolean"},
                "bus_default": {"type": "boolean", "default": False},
                "bus_format": {"type": "string"},
                "bus_map": {"type": "string"},
                "threshold": {"type": "array", "items": {"type": "number"}},
                "label_d0": {"type": "string"}, "label_d1": {"type": "string"},
                "label_d2": {"type": "string"}, "label_d3": {"type": "string"},
                "label_d4": {"type": "string"}, "label_d5": {"type": "string"},
                "label_d6": {"type": "string"}, "label_d7": {"type": "string"},
                "label_d8": {"type": "string"}, "label_d9": {"type": "string"},
                "label_d10": {"type": "string"}, "label_d11": {"type": "string"},
                "label_d12": {"type": "string"}, "label_d13": {"type": "string"},
                "label_d14": {"type": "string"}, "label_d15": {"type": "string"},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 31. Memory config ──
    Tool(
        name="sds_memory_config",
        description=(
            "Configure reference memory slots (stored waveform buffers) on the SDS oscilloscope.\n\n"
            "mem_index: Memory slot (1 or 2)\n"
            "horizontal_position: Horizontal position offset\n"
            "horizontal_scale: Horizontal scale factor\n"
            "horizontal_sync: Sync horizontal to source\n"
            "import_file: Import waveform from file\n"
            "label: Memory trace label\n"
            "switch: Show/hide memory trace\n"
            "vertacquire_amodeical_position: Vertical position offset\n"
            "vertical_scale: Vertical scale factor\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                "mem_index": {"type": "integer", "default": 1},
                "horizontal_position": {"type": "number"},
                "horizontal_scale": {"type": "number"},
                "horizontal_sync": {"type": "boolean"},
                "import_file": {"type": "string"},
                "label": {"type": "string"},
                "switch": {"type": "boolean"},
                "vertical_position": {"type": "number"},
                "vertical_scale": {"type": "number"},
            },
            "required": ["resource_name"],
        },
    ),
    # ── 32. Ref config ──
    Tool(
        name="sds_ref_config",
        description=(
            "Configure reference waveforms on the SDS oscilloscope.\n\n"
            "ref_index: Reference slot (1 or 2)\n"
            "label: Reference trace label\n"
            "data_source: Source — 'C1'-'C4','F1','F2','M1'-'M4'\n"
            "data_scale: Vertical scale factor\n"
            "data_position: Vertical position offset\n"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "resource_name": {"type": "string"},
                "ref_index": {"type": "integer", "default": 1},
                "label": {"type": "string"},
                "data_source": {"type": "string"},
                "data_scale": {"type": "number"},
                "data_position": {"type": "number"},
            },
            "required": ["resource_name"],
        },
    ),
]

# ═══════════════════════════════════════════════════════════════════
#  Tool registry
# ═══════════════════════════════════════════════════════════════════

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
    """Route tool call to the appropriate SDS driver function."""
    rn = args.get("resource_name", "")
    changes = {}
    queries = {}

    # ── 1. Autoset ──
    if name == "sds_autoset":
        autoset(rn)
        return json.dumps({"status": "ok", "action": "autoset"})

    # ── 2. Acquire config ──
    elif name == "sds_acquire_config":
        # acq_type: :ACQuire:TYPE (NORMal/PEAK/AVERage/ERES).
        # When AVERage, combine average_count: "AVERage,16"
        if (v := args.get("acq_type") or args.get("mode")) is not None:
            avg = args.get("average_count")
            if avg is not None and v.upper().startswith("AVER"):
                v = f"AVERage,{avg}"
                changes["average_count"] = avg
            acquire_type(rn, v); changes["acq_type"] = v
        # acq_mode: :ACQuire:MODE (YT/XY/ROLL)
        if (v := args.get("acq_mode")) is not None:
            acquire_mode(rn, v); changes["acq_mode"] = v
        if (v := args.get("memory_depth")) is not None:
            acquire_mdepth(rn, v); changes["memory_depth"] = v
        if (v := args.get("sample_rate")) is not None:
            acquire_srate(rn, v); changes["sample_rate"] = v
        if (v := args.get("interpolation")) is not None:
            acquire_interpolation(rn, v); changes["interpolation"] = v
        if (v := args.get("acquisition_mode")) is not None:
            acquire_amode(rn, v); changes["acquisition_mode"] = v
        if (v := args.get("eres_bits")) is not None:
            acquire_resolution(rn, v); changes["eres_bits"] = v
        if (v := args.get("sequence_enable")) is not None:
            acquire_sequence(rn, v); changes["sequence_enable"] = v
        if (v := args.get("sequence_count")) is not None:
            acquire_sequence_count(rn, v); changes["sequence_count"] = v
        if (v := args.get("max_memory")) is not None:
            acquire_mmanagement(rn, v); changes["max_memory"] = v
        if (v := args.get("points")) is not None:
            acquire_points(rn, v); changes["points"] = v
        if (v := args.get("sweep")) is not None:
            acquire_csweep(rn); changes["csweep"] = True
        return json.dumps({"status": "ok", **changes})

    # ── 3. Channel config ──
    elif name == "sds_channel_config":
        ch = args.get("channel", 1)
        if (v := args.get("display")) is not None:
            channel_display(rn, ch, v); changes["display"] = v
        if (v := args.get("coupling")) is not None:
            channel_coupling(rn, ch, v); changes["coupling"] = v
        if (v := args.get("bandwidth_limit")) is not None:
            channel_bwlimit(rn, ch, v); changes["bwlimit"] = v
        if (v := args.get("impedance")) is not None:
            channel_impedance(rn, ch, v); changes["impedance"] = v
        if (v := args.get("invert")) is not None:
            channel_invert(rn, ch, v); changes["invert"] = v
        if (v := args.get("offset")) is not None:
            channel_offset(rn, ch, v); changes["offset"] = v
        if (v := args.get("scale")) is not None:
            channel_scale(rn, ch, v); changes["scale"] = v
        if (v := args.get("probe")) is not None:
            channel_probe(rn, ch, v); changes["probe"] = v
        if (v := args.get("skew")) is not None:
            channel_skew(rn, ch, v); changes["skew"] = v
        if (v := args.get("unit")) is not None:
            channel_unit(rn, ch, v); changes["unit"] = v
        if (v := args.get("label")) is not None:
            channel_label_state(rn, ch, True); changes["label_state"] = True
            channel_label(rn, ch, v); changes["label"] = v
        elif (v := args.get("label_state")) is not None:
            channel_label_state(rn, ch, v); changes["label_state"] = v
        return json.dumps({"status": "ok", "channel": ch, **changes})

    # ── 4. Trigger config (dynamic SCPI routing) ──
    elif name == "sds_trigger_config":
        ch = trigger_config(rn, args)
        return json.dumps({"status": "ok", **ch})

    # ── 5. Timebase config ──
    elif name == "sds_timebase_config":
        ch = {}
        if (v := args.get("scale")) is not None:
            timebase_scale(rn, v); ch["scale"] = v
        if (v := args.get("delay")) is not None:
            timebase_delay(rn, v); ch["delay"] = v
        if (v := args.get("reference")) is not None:
            timebase_reference(rn, v); ch["reference"] = v
        if (v := args.get("reference_position")) is not None:
            timebase_reference_position(rn, v); ch["reference_position"] = v
        if (v := args.get("window_enable")) is not None:
            timebase_window(rn, v); ch["window_enable"] = v
        if (v := args.get("window_scale")) is not None:
            timebase_window_scale(rn, v); ch["window_scale"] = v
        if (v := args.get("window_delay")) is not None:
            timebase_window_delay(rn, v); ch["window_delay"] = v
        return json.dumps({"status": "ok", **ch})

    # ── 6. Measure ──
    elif name == "sds_measure":
        ch = {}
        pi = args.get("param_index")
        state_explicit = "state" in args
        # Overall measure state/mode
        if (v := args.get("state")) is not None:
            measure_state(rn, v); ch["state"] = v
        if (v := args.get("mode")) is not None:
            measure_mode(rn, v); ch["mode"] = v
        if (v := args.get("advanced_line_number")) is not None:
            measure_advanced_line_number(rn, v); ch["advanced_line_number"] = v
        if pi is not None or args.get("meas_type") is not None:
            # Advanced measurement path
            if args.get("clear"):
                measure_advanced_clear(rn); ch["clear"] = True
            if pi is not None:
                if (v := args.get("source1")) is not None:
                    measure_advanced_p_source1(rn, pi, v)
                if (v := args.get("source2")) is not None:
                    measure_advanced_p_source2(rn, pi, v)
                if (v := args.get("meas_type")) is not None:
                    measure_advanced_p_type(rn, pi, v)
                if (v := args.get("show_stats")) is not None:
                    measure_advanced_statistics(rn, v)
                if args.get("stats_reset"):
                    measure_advanced_statistics_reset(rn)
                ch["param_index"] = pi
                if (v := args.get("meas_type")):
                    ch["meas_type"] = v
                # Query value
                ch["value"] = measure_advanced_p_value(rn, pi)
            if (v := args.get("style")) is not None:
                measure_rdisplay(rn, v)
            if (v := args.get("strategy_auto")) is not None:
                measure_astrategy(rn, v)
        else:
            # Simple measurement path
            if args.get("clear"):
                measure_simple_clear(rn); ch["clear"] = True
            if (v := args.get("source")) is not None:
                measure_simple_source(rn, v)
            if (v := args.get("items")) is not None:
                measure_simple_item(rn, ",".join(v) if isinstance(v, list) else v)
        # Gate
        if (v := args.get("gate_enable")) is not None:
            measure_gate(rn, v); ch["gate_enable"] = v
        if (v := args.get("gate_a")) is not None:
            measure_gate_gA(rn, v); ch["gate_a"] = v
        if (v := args.get("gate_b")) is not None:
            measure_gate_gB(rn, v); ch["gate_b"] = v
        # Threshold
        if (v := args.get("threshold_type")) is not None:
            measure_threshold_type(rn, v); ch["threshold_type"] = v
            measure_threshold_source(rn, args.get("source", "C1"))
        if any(k in args for k in ["absolute_low", "absolute_mid", "absolute_high"]):
            lo = args.get("absolute_low", "0")
            md = args.get("absolute_mid", "0")
            hi = args.get("absolute_high", "0")
            measure_threshold_absolute(rn, f"{lo},{md},{hi}")
            ch["absolute"] = f"{lo}/{md}/{hi}"
        if any(k in args for k in ["percent_low", "percent_mid", "percent_high"]):
            lo = args.get("percent_low", "10")
            md = args.get("percent_mid", "50")
            hi = args.get("percent_high", "90")
            measure_threshold_percent(rn, f"{lo},{md},{hi}")
            ch["percent"] = f"{lo}/{md}/{hi}"
        # Auto-enable measure if items/meas_type were set and state not explicit
        if not state_explicit and (args.get("items") or args.get("meas_type")):
            measure_state(rn, True); ch["state"] = True
        return json.dumps({"status": "ok", **ch})

    # ── 7. Waveform read ──
    elif name == "sds_waveform_read":
        src = args.get("source", "C1")
        start = args.get("start", 0)
        pts = args.get("points", 0)
        sparsing = args.get("sparsing", 1)
        bo = args.get("byte_order", "LSBFirst")
        # Configure waveform transfer
        waveform_source(rn, src)
        if start > 0:
            waveform_start(rn, start)
        if pts > 0:
            waveform_points(rn, pts)
        if sparsing > 1:
            waveform_interval(rn, sparsing)
        if bo == "MSBFirst":
            waveform_byteorder(rn, "MSB")
        # Read preamble
        raw_pre = waveform_preamble(rn)
        preamble = ieee4882.parse_definite_length_block(raw_pre)
        # Read data
        raw_data = waveform_data(rn)
        data_bytes = ieee4882.parse_definite_length_block(raw_data)
        # Convert to voltage
        voltage_data = ieee4882.raw_to_voltage(data_bytes, preamble, src)
        result = {
            "preamble": preamble,
            "voltage_data": voltage_data[:1000] if len(voltage_data) > 1000 else voltage_data,
            "total_points": len(voltage_data),
            "source": src,
        }
        if len(voltage_data) > 1000:
            result["truncated"] = True
        return json.dumps(result)

    # ── 8. Display config ──
    elif name == "sds_display_config":
        ch = {}
        if (v := args.get("type_")) is not None:
            display_type(rn, v); ch["type"] = v
        if (v := args.get("persistence")) is not None:
            display_persistence(rn, v); ch["persistence"] = v
        if (v := args.get("grid_style")) is not None:
            display_grid_style(rn, v); ch["grid_style"] = v
        if (v := args.get("intensity")) is not None:
            display_intensity(rn, v); ch["intensity"] = v
        if (v := args.get("backlight")) is not None:
            display_backlight(rn, v); ch["backlight"] = v
        if (v := args.get("color")) is not None:
            display_color(rn, v); ch["color"] = v
        if (v := args.get("graticule")) is not None:
            display_graticule(rn, v); ch["graticule"] = v
        if (v := args.get("axis_mode")) is not None:
            display_axis_mode(rn, v); ch["axis_mode"] = v
        if (v := args.get("axis_position")) is not None:
            display_axis_position(rn, v); ch["axis_position"] = v
        if (v := args.get("transparent")) is not None:
            display_transparence(rn, v); ch["transparent"] = v
        if (v := args.get("hide_menu")) is not None:
            display_menu_hide(rn, v); ch["hide_menu"] = v
        if args.get("clear_persistence"):
            display_clear(rn); ch["clear_persistence"] = True
        if (v := args.get("axis")) is not None:
            display_axis(rn, v); ch["axis"] = v
        if (v := args.get("menu")) is not None:
            display_menu(rn, v); ch["menu"] = v
        return json.dumps({"status": "ok", **ch})

    # ── 9. Cursor config (single cursor set) ──
    elif name == "sds_cursor_config":
        ch = {}
        # Auto-enable cursor subsystem when setting a non-OFF mode
        mode_v = args.get("mode")
        if mode_v is not None:
            if mode_v.upper() != "OFF":
                cursor_state(rn, True)
            cursor_mode(rn, mode_v); ch["mode"] = mode_v
        if (v := args.get("source1")) is not None:
            cursor_source1(rn, v); ch["source1"] = v
        if (v := args.get("source2")) is not None:
            cursor_source2(rn, v); ch["source2"] = v
        if (v := args.get("x1")) is not None:
            cursor_x1(rn, v); ch["x1"] = v
        if (v := args.get("x2")) is not None:
            cursor_x2(rn, v); ch["x2"] = v
        if (v := args.get("y1")) is not None:
            cursor_y1(rn, v); ch["y1"] = v
        if (v := args.get("y2")) is not None:
            cursor_y2(rn, v); ch["y2"] = v
        if (v := args.get("tag_style")) is not None:
            cursor_tag_style(rn, v); ch["tag_style"] = v
        if (v := args.get("xreference")) is not None:
            cursor_x_reference(rn, v); ch["xreference"] = v
        if (v := args.get("yreference")) is not None:
            cursor_y_reference(rn, v); ch["yreference"] = v
        if (v := args.get("measure_item")) is not None:
            cursor_measure_item(rn, v); ch["measure_item"] = v
        if args.get("read"):
            ch["xdelta"] = cursor_xdelta(rn)
            ch["ydelta"] = cursor_ydelta(rn)
            ch["ixdelta"] = cursor_ixdelta(rn)
        return json.dumps({"status": "ok", **ch})

    # ── 10. Decode config ──
    elif name == "sds_decode_config":
        ch = {}
        bus = args.get("bus", 1)
        # Auto-enable decode when setting protocol or source params
        if args.get("protocol") is not None or any(
            args.get(k) is not None for k in
            ["i2c_scl_source", "i2c_sda_source", "spi_clk_source", "spi_miso_source",
             "spi_mosi_source", "uart_tx_source", "uart_rx_source", "can_source",
             "lin_source", "canfd_source"]
        ):
            decode_state(rn, True)
        if (v := args.get("protocol")) is not None:
            decode_bus_protocol(rn, bus, v); ch["protocol"] = v
        if (v := args.get("format")) is not None:
            decode_bus_format(rn, bus, v); ch["format"] = v
        if (v := args.get("display")) is not None:
            decode_bus_state(rn, bus, v); ch["display"] = v
        if (v := args.get("list_enable")) is not None:
            decode_list_state(rn, "D1" if v else "OFF"); ch["list_enable"] = v
        # I2C
        if (v := args.get("i2c_scl_source")) is not None:
            decode_bus_iic_scl_source(rn, bus, v)
        if (v := args.get("i2c_sda_source")) is not None:
            decode_bus_iic_sda_source(rn, bus, v)
        if (v := args.get("i2c_rw_bit")) is not None:
            decode_bus_iic_rwbit(rn, bus, v)
        if (v := args.get("state")) is not None:
            decode_state(rn, v); ch["state"] = v
        if (v := args.get("list_lines")) is not None:
            decode_list_line(rn, v); ch["list_lines"] = v
        if (v := args.get("list_scroll")) is not None:
            decode_list_scroll(rn, v); ch["list_scroll"] = v
        if args.get("bus_result_read"):
            ch["bus_result"] = decode_bus_result(rn, bus)
        if args.get("read_result"):
            ch["result"] = decode_list_result(rn, bus)
        return json.dumps({"status": "ok", **ch})

    # ── 11. Search config ──
    elif name == "sds_search_config":
        ch = {}
        if (v := args.get("mode")) is not None:
            search_state(rn, v == "ON"); ch["mode"] = v
        if (v := args.get("search_type")) is not None:
            search_state(rn, True)  # auto-enable when selecting search type
            search_mode(rn, v); ch["search_type"] = v
        if args.get("copy_to_trigger"):
            search_copy(rn, "TOTRigger")
        # Edge search
        if (v := args.get("edge_source")) is not None:
            search_edge_source(rn, v)
        if (v := args.get("edge_slope")) is not None:
            search_edge_slope(rn, v)
        if (v := args.get("edge_level")) is not None:
            search_edge_level(rn, v)
        # Slope search
        if (v := args.get("slope_source")) is not None:
            search_slope_source(rn, v)
        if (v := args.get("slope_slope")) is not None:
            search_slope_slope(rn, v)
        if (v := args.get("slope_high_level")) is not None:
            search_slope_hlevel(rn, v)
        if (v := args.get("slope_low_level")) is not None:
            search_slope_llevel(rn, v)
        if (v := args.get("slope_limit_low")) is not None:
            search_slope_limit(rn, v)
        if (v := args.get("slope_upper_time")) is not None:
            search_slope_tupper(rn, v)
        if (v := args.get("slope_lower_time")) is not None:
            search_slope_tlower(rn, v)
        # Pulse search
        if (v := args.get("pulse_source")) is not None:
            search_pulse_source(rn, v)
        if (v := args.get("pulse_polarity")) is not None:
            search_pulse_polarity(rn, v)
        if (v := args.get("pulse_level")) is not None:
            search_pulse_level(rn, v)
        if (v := args.get("pulse_limit_low")) is not None:
            search_pulse_limit(rn, v)
        if (v := args.get("pulse_upper_time")) is not None:
            search_pulse_tupper(rn, v)
        if (v := args.get("pulse_lower_time")) is not None:
            search_pulse_tlower(rn, v)
        # Interval search
        if (v := args.get("interval_source")) is not None:
            search_interval_source(rn, v)
        if (v := args.get("interval_slope")) is not None:
            search_interval_slope(rn, v)
        if (v := args.get("interval_level")) is not None:
            search_interval_level(rn, v)
        if (v := args.get("interval_limit_low")) is not None:
            search_interval_limit(rn, v)
        if (v := args.get("interval_upper_time")) is not None:
            search_interval_tupper(rn, v)
        if (v := args.get("interval_lower_time")) is not None:
            search_interval_tlower(rn, v)
        if args.get("read_count"):
            ch["count"] = search_count(rn)
        if args.get("read_event"):
            ch["event"] = search_event(rn)
        return json.dumps({"status": "ok", **ch})

    # ── 12. Save ──
    elif name == "sds_save":
        ch = {}
        st = args.get("save_type", "CSV").upper()
        fn = args.get("filename", "")
        src = args.get("source", "C1")
        qfn = f'"{fn}"'
        if st == "SETUP":
            save_setup(rn, f"EXTernal,{qfn}"); ch["type"] = "setup"
        elif st == "IMAGe":
            save_image(rn, qfn, "PNG", "OFF"); ch["type"] = "image"
        elif st == "CSV":
            save_csv(rn, qfn, src, "OFF"); ch["type"] = "csv"
        elif st == "BINary":
            save_binary(rn, qfn, src); ch["type"] = "binary"
        elif st == "MATLab":
            save_matlab(rn, qfn, src); ch["type"] = "matlab"
        elif st == "REFerence":
            save_reference(rn, qfn, src); ch["type"] = "reference"
        else:
            save_csv(rn, qfn, src, "OFF"); ch["type"] = "csv"
        return json.dumps({"status": "ok", **ch})

    # ── 13. System config ──
    elif name == "sds_system_config":
        ch = {}
        if (v := args.get("buzzer")) is not None:
            system_buzzer(rn, v); ch["buzzer"] = v
        if (v := args.get("date")) is not None:
            system_date(rn, int(v.replace("-", ""))); ch["date"] = v
        if (v := args.get("time_")) is not None:
            system_time(rn, int(v.replace(":", ""))); ch["time"] = v
        if (v := args.get("language")) is not None:
            system_language(rn, v); ch["language"] = v
        if (v := args.get("lan_ip")) is not None:
            system_lan_ip(rn, v); ch["lan_ip"] = v
        if (v := args.get("lan_mask")) is not None:
            system_lan_mask(rn, v); ch["lan_mask"] = v
        if (v := args.get("lan_gateway")) is not None:
            system_lan_gateway(rn, v); ch["lan_gateway"] = v
        if (v := args.get("lan_type")) is not None:
            system_lan_type(rn, v); ch["lan_type"] = v
        if (v := args.get("vnc_port")) is not None:
            system_vncport(rn, v); ch["vnc_port"] = v
        if (v := args.get("remote_lock")) is not None:
            system_remote(rn, v); ch["remote_lock"] = v
        if (v := args.get("touch")) is not None:
            system_touch(rn, v); ch["touch"] = v
        if (v := args.get("screen_saver")) is not None:
            system_ssaver(rn, "10MIN" if v else "OFF"); ch["screen_saver"] = v
        if args.get("self_cal"):
            system_selfcal(rn); ch["self_cal"] = True
        if (v := args.get("edu_mode")) is not None:
            system_edumode(rn, "AUTOSet", v); ch["edu_mode"] = v
        if (v := args.get("network_storage")) is not None:
            if v:
                system_nstorage(rn, "/", "", "", "ON", "ON"); ch["network_storage"] = True
            else:
                system_nstorage_disconnect(rn); ch["network_storage"] = False
        if args.get("network_storage_disconnect"):
            system_nstorage_disconnect(rn); ch["ns_disconnect"] = True
        if (v := args.get("network_storage_connect")) is not None:
            system_nstorage_connect(rn); ch["ns_connect"] = v
        if args.get("reboot"):
            system_reboot(rn); ch["reboot"] = True
        if args.get("shutdown"):
            system_shutdown(rn); ch["shutdown"] = True
        if (v := args.get("clock_source")) is not None:
            system_clock(rn, v); ch["clock_source"] = v
        return json.dumps({"status": "ok", **ch})

    # ── 14. Math config ──
    elif name == "sds_math_config":
        ch = {}
        fi = args.get("func_index", 1)
        display_explicit = "display" in args
        if (v := args.get("operation")) is not None:
            function_operator(rn, fi, v); ch["operation"] = v
        if (v := args.get("source1")) is not None:
            function_source1(rn, fi, v); ch["source1"] = v
        if (v := args.get("source2")) is not None:
            function_source2(rn, fi, v); ch["source2"] = v
        if (v := args.get("display")) is not None:
            function_state(rn, fi, v); ch["display"] = v
        if (v := args.get("label")) is not None:
            function_label_text(rn, fi, v); ch["label"] = v
        if (v := args.get("invert")) is not None:
            function_invert(rn, fi, v); ch["invert"] = v
        if (v := args.get("position")) is not None:
            function_position(rn, fi, v); ch["position"] = v
        if (v := args.get("scale")) is not None:
            function_scale(rn, fi, v); ch["scale"] = v
        if (v := args.get("average_count")) is not None:
            function_average_num(rn, fi, v); ch["average_count"] = v
        if (v := args.get("diff_dx")) is not None:
            function_diff_dx(rn, fi, v); ch["diff_dx"] = v
        if (v := args.get("eres_bits")) is not None:
            function_eres_bits(rn, fi, v); ch["eres_bits"] = v
        # FFT
        if (v := args.get("fft_display")) is not None:
            function_fft_display(rn, v); ch["fft_display"] = v
        if args.get("fft_auto"):
            function_fft_autoset(rn, fi, "NORMal"); ch["fft_auto"] = True
        if (v := args.get("fft_mode")) is not None:
            function_fft_mode(rn, fi, v); ch["fft_mode"] = v
        if (v := args.get("fft_window")) is not None:
            function_fft_window(rn, fi, v); ch["fft_window"] = v
        if (v := args.get("fft_points")) is not None:
            function_fft_points(rn, fi, str(v)); ch["fft_points"] = v
        if (v := args.get("fft_unit")) is not None:
            function_fft_unit(rn, fi, v); ch["fft_unit"] = v
        if (v := args.get("fft_scale")) is not None:
            function_fft_scale(rn, fi, v); ch["fft_scale"] = v
        if (v := args.get("fft_center")) is not None:
            function_fft_hcenter(rn, fi, v); ch["fft_center"] = v
        if (v := args.get("fft_span")) is not None:
            function_fft_span(rn, fi, v); ch["fft_span"] = v
        if (v := args.get("fft_ref_level")) is not None:
            function_fft_rlevel(rn, fi, v); ch["fft_ref_level"] = v
        if args.get("fft_reset"):
            function_fft_reset(rn, fi); ch["fft_reset"] = True
        # Filter
        if (v := args.get("filter_type")) is not None:
            function_filter_type(rn, fi, v); ch["filter_type"] = v
        if (v := args.get("filter_low_freq")) is not None:
            function_filter_lfrequency(rn, fi, v); ch["filter_low_freq"] = v
        if (v := args.get("filter_high_freq")) is not None:
            function_filter_hfrequency(rn, fi, v); ch["filter_high_freq"] = v
        if (v := args.get("integrate_gate")) is not None:
            function_integrate_gate(rn, fi, v); ch["integrate_gate"] = v
        if (v := args.get("integrate_offset")) is not None:
            function_integrate_offset(rn, fi, v); ch["integrate_offset"] = v
        if (v := args.get("interpolate_coef")) is not None:
            function_interpolate_coef(rn, fi, v); ch["interpolate_coef"] = v
        if (v := args.get("label_state")) is not None:
            function_label_state(rn, fi, v); ch["label_state"] = v
        if (v := args.get("maxhold_sweeps")) is not None:
            function_maxhold_sweeps(rn, fi, v); ch["maxhold_sweeps"] = v
        if (v := args.get("minhold_sweeps")) is not None:
            function_minhold_sweeps(rn, fi, v); ch["minhold_sweeps"] = v
        if (v := args.get("fft_load")) is not None:
            function_fft_load(rn, fi, v); ch["fft_load"] = v
        # Auto-enable the math function if any config was done and display wasn't explicitly set
        if not display_explicit and ch:
            function_state(rn, fi, True); ch["display"] = True
        return json.dumps({"status": "ok", **ch})

    # ── 15. DVM config ──
    elif name == "sds_dvm_config":
        ch = {}
        if (v := args.get("mode")) is not None:
            if v == "OFF":
                dvm_state(rn, False)
            else:
                dvm_state(rn, True)
                dvm_mode(rn, v)
            ch["mode"] = v
        if (v := args.get("source")) is not None:
            dvm_source(rn, v); ch["source"] = v
        if (v := args.get("alarm")) is not None:
            dvm_alarm(rn, v); ch["alarm"] = v
        if (v := args.get("auto_range")) is not None:
            dvm_autorange(rn, v); ch["auto_range"] = v
        if (v := args.get("hold")) is not None:
            dvm_hold(rn, v); ch["hold"] = v
        if args.get("read"):
            ch["value"] = dvm_current(rn)
        return json.dumps({"status": "ok", **ch})

    # ── 16. Counter config ──
    elif name == "sds_counter_config":
        ch = {}
        if (v := args.get("mode")) is not None:
            counter_state(rn, True)  # auto-enable when setting mode
            counter_mode(rn, v); ch["mode"] = v
        if (v := args.get("source")) is not None:
            counter_source(rn, v)
        if (v := args.get("level")) is not None:
            counter_level(rn, v)
        if (v := args.get("state")) is not None:
            counter_state(rn, v); ch["state"] = v
        if (v := args.get("statistics")) is not None:
            counter_statistics(rn, v); ch["statistics"] = v
        if args.get("stats_reset"):
            counter_statistics_reset(rn)
        # Totalizer
        if (v := args.get("totalizer_gate")) is not None:
            counter_totalizer_gate(rn, v)
        if (v := args.get("totalizer_gate_level")) is not None:
            counter_totalizer_gate_level(rn, v)
        if (v := args.get("totalizer_gate_slope")) is not None:
            counter_totalizer_gate_slope(rn, v)
        if (v := args.get("totalizer_gate_type")) is not None:
            counter_totalizer_gate_type(rn, v)
        if args.get("totalizer_reset"):
            counter_totalizer_reset(rn)
        if (v := args.get("totalizer_slope")) is not None:
            counter_totalizer_slope(rn, v)
        # Reads
        if args.get("read_current"):
            ch["current"] = counter_current(rn)
        if args.get("read_stats"):
            ch["statistics"] = counter_statistics_value(rn)
        return json.dumps({"status": "ok", **ch})

    # ── 17. Mask test ──
    elif name == "sds_mask_test_config":
        ch = {}
        if (v := args.get("enable")) is not None:
            mtest_operate(rn, "RUN" if v else "STOP")
            mtest_state(rn, v); ch["enable"] = v
        if (v := args.get("source")) is not None:
            mtest_source(rn, v); ch["source"] = v
        if (v := args.get("test_type")) is not None:
            mtest_type(rn, v); ch["test_type"] = v
        if args.get("create_mask"):
            mtest_mask_create(rn); ch["create_mask"] = True
        if (v := args.get("load_mask")) is not None:
            mtest_mask_load(rn, v); ch["load_mask"] = v
        if (v := args.get("count")) is not None:
            mtest_count(rn); ch["count"] = v  # read-only, just query
        if args.get("reset"):
            mtest_reset(rn); ch["reset"] = True
        if (v := args.get("buzzer")) is not None:
            mtest_function_buzzer(rn, v)
        if (v := args.get("stop_on_fail")) is not None:
            mtest_function_sof(rn, v)
        if (v := args.get("display")) is not None:
            mtest_idisplay(rn, v)
        return json.dumps({"status": "ok", **ch})

    # ── 18. WaveGen config ──
    elif name == "sds_wavegen_config":
        ch = {}
        if (v := args.get("output")) is not None:
            wavegen_output(rn, v); ch["output"] = v
        if (v := args.get("basic_wave")) is not None:
            wavegen_basic_wave(rn, v); ch["wave"] = v
        if (v := args.get("frequency")) is not None:
            wavegen_frequency(rn, v); ch["frequency"] = v
        if (v := args.get("amplitude")) is not None:
            wavegen_amplitude(rn, v); ch["amplitude"] = v
        if (v := args.get("offset")) is not None:
            wavegen_offset(rn, v); ch["offset"] = v
        if (v := args.get("duty_cycle")) is not None:
            wavegen_duty_cycle(rn, v); ch["duty_cycle"] = v
        return json.dumps({"status": "ok", **ch})

    # ── 19. Channel reference strategy ──
    elif name == "sds_channel_reference":
        if (v := args.get("ref_type")) is not None:
            channel_reference_type(rn, v); return json.dumps({"status": "ok", "ref_type": v})
        return json.dumps({"status": "ok", "ref_type": channel_reference_type(rn)})

    # ── 20. Trigger query ──
    elif name == "sds_trigger_query":
        result = {}
        if args.get("read_status"):
            result["status"] = trigger_status(rn)
        if args.get("read_frequency"):
            result["frequency"] = trigger_frequency(rn)
        return json.dumps({"status": "ok", **result})

    # ── 21. Waveform preamble ──
    elif name == "sds_waveform_preamble":
        src = args.get("source", "C1")
        waveform_source(rn, src)
        raw = waveform_preamble(rn)
        preamble = ieee4882.parse_definite_length_block(raw)
        return json.dumps({"source": src, "preamble": preamble})

    # ── 22. Measure delay-time ──
    elif name == "sds_measure_dtime":
        ch = {}
        idx = args.get("index", 1)
        if (v := args.get("edge1")) is not None:
            measure_dtime_edge1(rn, idx, v); ch["edge1"] = v
        if (v := args.get("edge2")) is not None:
            measure_dtime_edge2(rn, idx, v); ch["edge2"] = v
        if (v := args.get("slope1")) is not None:
            measure_dtime_slope1(rn, idx, v); ch["slope1"] = v
        if (v := args.get("slope2")) is not None:
            measure_dtime_slope2(rn, idx, v); ch["slope2"] = v
        if (v := args.get("threshold1")) is not None:
            measure_dtime_threshold1(rn, idx, v); ch["threshold1"] = v
        if (v := args.get("threshold2")) is not None:
            measure_dtime_threshold2(rn, idx, v); ch["threshold2"] = v
        return json.dumps({"status": "ok", **ch})

    # ── 23. Math FFT marker ──
    elif name == "sds_math_fft_marker":
        ch = {}
        fi = args.get("func_index", 1)
        if (v := args.get("frequency")) is not None:
            function_fft_marker_frequency(rn, fi, v)
            ch["frequency"] = v
        if (v := args.get("show")) is not None:
            function_fft_search(rn, fi, "MARKer" if v else "OFF")
            ch["show"] = v
        if (v := args.get("harmonic_peak")) is not None:
            function_fft_search(rn, fi, v)
        if (v := args.get("excursion")) is not None:
            function_fft_search_excursion(rn, fi, v)
        if (v := args.get("threshold")) is not None:
            function_fft_search_threshold(rn, fi, v)
        if args.get("read_table"):
            ch["table"] = _query(rn, f":FUNCtion{fi}:FFT:SEARch:TABLE?")
        return json.dumps({"status": "ok", **ch})

    # ── 24. History config ──
    elif name == "sds_history_config":
        ch = {}
        # Auto-enable history when setting frame/play/interval/time
        if any(args.get(k) is not None for k in ["frame", "play", "interval", "time_"]):
            history_state(rn, True); ch["state"] = True
        if (v := args.get("frame")) is not None:
            history_frame(rn, v); ch["frame"] = v
        if (v := args.get("interval")) is not None:
            history_interval(rn, v); ch["interval"] = v
        if (v := args.get("play")) is not None:
            history_play(rn, v); ch["play"] = v
        if (v := args.get("time_")) is not None:
            history_time(rn, v); ch["time"] = v
        if args.get("read_list"):
            ch["list"] = history_list(rn, "ON")
        return json.dumps({"status": "ok", **ch})

    # ── 25. Recall config ──
    elif name == "sds_recall_config":
        ch = {}
        if (v := args.get("setup_file")) is not None:
            recall_setup(rn, f'EXTernal,"{v}"'); ch["setup_file"] = v
        if (v := args.get("reference_file")) is not None:
            recall_reference(rn, "REFD", v); ch["reference_file"] = v
        if args.get("factory_default"):
            recall_factory_default(rn); ch["factory_default"] = True
        if args.get("secure_erase"):
            recall_serase(rn); ch["secure_erase"] = True
        return json.dumps({"status": "ok", **ch})

    # ── 26. Meter config (handheld scope-meter) ──
    elif name == "sds_meter_config":
        ch = {}
        if (v := args.get("function")) is not None:
            meter_state(rn, True)
            meter_configure_set(rn, v)
            ch["function"] = v
        if args.get("read"):
            ch["value"] = meter_read(rn)
        return json.dumps({"status": "ok", **ch})

    # ── 27. Format data ──
    elif name == "sds_format_data":
        dt = args.get("data_type")
        if dt is not None:
            format_data(rn, dt)
            return json.dumps({"status": "ok", "format": dt})
        return json.dumps({"status": "ok", "format": format_data(rn)})

    # ── 28. Print screen ──
    elif name == "sds_print_screen":
        print_screen(rn)
        return json.dumps({"status": "ok", "action": "print_screen"})

    # ── 29. Cursor multi config ──
    elif name == "sds_cursor_multi_config":
        ch = {}
        # Auto-enable cursor state when setting multi-cursor params
        cursor_state(rn, True)
        # MANual X
        if (mx := args.get("manual_x_index")) is not None:
            if (v := args.get("manual_x_color")):
                cursor_manual_x_color(rn, mx, v)
            if (v := args.get("manual_x_follow")) is not None:
                cursor_manual_x_dfollow(rn, mx, v)
            if (v := args.get("manual_x_dtcursor")):
                cursor_manual_x_dtcursor(rn, mx, v)
            if (v := args.get("manual_x_dvalue")) is not None:
                cursor_manual_x_dvalue(rn, mx, v)
            if (v := args.get("manual_x_label")):
                cursor_manual_x_label(rn, mx, v)
            if (v := args.get("manual_x_position")) is not None:
                cursor_manual_x_position(rn, mx, v)
            if (v := args.get("manual_x_source")):
                cursor_manual_x_source(rn, mx, v)
            ch["manual_x"] = mx
        # MANual Y
        if (my := args.get("manual_y_index")) is not None:
            if (v := args.get("manual_y_color")):
                cursor_manual_y_color(rn, my, v)
            if (v := args.get("manual_y_follow")) is not None:
                cursor_manual_y_dfollow(rn, my, v)
            if (v := args.get("manual_y_dtcursor")):
                cursor_manual_y_dtcursor(rn, my, v)
            if (v := args.get("manual_y_dvalue")) is not None:
                cursor_manual_y_dvalue(rn, my, v)
            if (v := args.get("manual_y_label")):
                cursor_manual_y_label(rn, my, v)
            if (v := args.get("manual_y_position")) is not None:
                cursor_manual_y_position(rn, my, v)
            if (v := args.get("manual_y_source")):
                cursor_manual_y_source(rn, my, v)
            ch["manual_y"] = my
        # MEASure
        if (mi := args.get("measure_index")) is not None:
            if (v := args.get("measure_color")):
                cursor_measure_color(rn, mi, v)
            if (v := args.get("measure_label")):
                cursor_measure_label(rn, mi, v)
            if (v := args.get("measure_item")):
                cursor_measure_mitem(rn, mi, v)
            ch["measure"] = mi
        # TRACk
        if (ti := args.get("track_index")) is not None:
            if (v := args.get("track_color")):
                cursor_track_color(rn, ti, v)
            if (v := args.get("track_follow")) is not None:
                cursor_track_dfollow(rn, ti, v)
            if (v := args.get("track_dtcursor")):
                cursor_track_dtcursor(rn, ti, v)
            if (v := args.get("track_dvalue")) is not None:
                cursor_track_dvalue(rn, ti, v)
            if (v := args.get("track_label")):
                cursor_track_label(rn, ti, v)
            if (v := args.get("track_position")) is not None:
                cursor_track_position(rn, ti, v)
            if (v := args.get("track_source")):
                cursor_track_source(rn, ti, v)
            ch["track"] = ti
        return json.dumps({"status": "ok", **ch})

    # ── 30. Digital config ──
    elif name == "sds_digital_config":
        ch = {}
        if (v := args.get("active")) is not None:
            digital_state(rn, v); ch["active"] = v
        if (v := args.get("height")) is not None:
            digital_height(rn, v)
        if (v := args.get("position")) is not None:
            digital_position(rn, v)
        if (v := args.get("skew")) is not None:
            digital_skew(rn, v)
        if (v := args.get("bus")) is not None:
            b = v
            if (bv := args.get("bus_display")) is not None:
                digital_bus_display(rn, b, bv)
            if args.get("bus_default"):
                digital_bus_default(rn, b)
            if (bv := args.get("bus_format")) is not None:
                digital_bus_format(rn, b, bv)
            if (bv := args.get("bus_map")) is not None:
                digital_bus_map(rn, b, bv)
            ch["bus"] = b
        # Digital channel labels
        for i in range(16):
            key = f"label_d{i}"
            if (v := args.get(key)) is not None:
                digital_label(rn, i, v)
                ch[key] = v
        # Threshold
        if (v := args.get("threshold")) is not None:
            if isinstance(v, list) and len(v) == 2:
                digital_threshold(rn, 1, v[0])
                digital_threshold(rn, 2, v[1])
        return json.dumps({"status": "ok", **ch})

    # ── 31. Memory config ──
    elif name == "sds_memory_config":
        ch = {}
        mi = args.get("mem_index", 1)
        if (v := args.get("horizontal_position")) is not None:
            memory_horizontal_position(rn, mi, v); ch["hpos"] = v
        if (v := args.get("horizontal_scale")) is not None:
            memory_horizontal_scale(rn, mi, v); ch["hscale"] = v
        if (v := args.get("horizontal_sync")) is not None:
            memory_horizontal_sync(rn, mi, v); ch["hsync"] = v
        if (v := args.get("import_file")) is not None:
            memory_import(rn, mi, v); ch["import"] = v
        if (v := args.get("label")) is not None:
            memory_label_text(rn, mi, v); ch["label"] = v
        if (v := args.get("switch")) is not None:
            memory_switch(rn, mi, v); ch["switch"] = v
        if (v := args.get("vertical_position")) is not None:
            memory_vertical_position(rn, mi, v); ch["vpos"] = v
        if (v := args.get("vertical_scale")) is not None:
            memory_vertical_scale(rn, mi, v); ch["vscale"] = v
        return json.dumps({"status": "ok", **ch})

    # ── 32. Ref config (reference waveforms) ──
    elif name == "sds_ref_config":
        ch = {}
        ref_names = {1: "A", 2: "B", 3: "C", 4: "D"}
        ri = ref_names.get(args.get("ref_index", 1), "A")
        if (v := args.get("label")) is not None:
            ref_label_text(rn, ri, v); ch["label"] = v
        if (v := args.get("data_source")) is not None:
            ref_data(rn, ri, f"SAVE,{v}"); ch["data_source"] = v
        if (v := args.get("data_scale")) is not None:
            ref_data_scale(rn, ri, v); ch["data_scale"] = v
        if (v := args.get("data_position")) is not None:
            ref_data_position(rn, ri, v); ch["data_position"] = v
        return json.dumps({"status": "ok", **ch})

    return f"Unknown tool: {name}"


# ═══════════════════════════════════════════════════════════════════
#  Entry point
# ═══════════════════════════════════════════════════════════════════

async def _server_main():
    async with stdio_server() as (read, write):
        await _SERVER.run(read, write, _SERVER.create_initialization_options())


def main():
    logging.basicConfig(
        level=logging.WARNING,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
    logging.getLogger("tmosc").setLevel(logging.DEBUG)
    asyncio.run(_server_main())


if __name__ == "__main__":
    main()
