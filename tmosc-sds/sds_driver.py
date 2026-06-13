"""SDS Series oscilloscope driver — re-exports from subsystem modules.

Each subsystem has been split into its own file for maintainability.
All public functions from the subsystem modules are re-exported here
so that ``from sds_driver import ...`` continues to work unchanged.
"""

# Re-export shared helpers (used by server.py)
from _base import _ensure, _send, _query, _query_raw, _read_raw, logger

# Root commands
from root import autoset, print_screen, format_data

# ACQuire subsystem
from acquire import (
    acquire_type, acquire_mode, acquire_mdepth, acquire_srate,
    acquire_interpolation, acquire_amode, acquire_numacq,
    acquire_resolution, acquire_sequence, acquire_sequence_count,
    acquire_mmanagement, acquire_points, acquire_csweep,
)

# CHANnel subsystem
from channel import (
    channel_reference_type, channel_display, channel_coupling,
    channel_bwlimit, channel_impedance, channel_invert,
    channel_offset, channel_scale, channel_probe,
    channel_skew, channel_unit, channel_label, channel_label_state,
)

# COUNter subsystem
from counter import (
    counter_state, counter_current, counter_level, counter_mode,
    counter_source, counter_statistics, counter_statistics_reset,
    counter_statistics_value, counter_totalizer_gate,
    counter_totalizer_gate_level, counter_totalizer_gate_slope,
    counter_totalizer_gate_type, counter_totalizer_reset,
    counter_totalizer_slope,
)

# CURSor subsystem (common + single + multi)
from cursor import (
    cursor_state, cursor_tag_style, cursor_x_reference,
    cursor_y_reference,
    cursor_ixdelta, cursor_measure_item,
    cursor_mode, cursor_source1, cursor_source2,
    cursor_x1, cursor_x2, cursor_xdelta,
    cursor_y1, cursor_y2, cursor_ydelta,
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
)

# DISPlay subsystem
from display import (
    display_axis, display_axis_mode, display_axis_position,
    display_backlight, display_clear, display_color,
    display_graticule, display_grid_style, display_hidemenu,
    display_intensity, display_menu, display_menu_hide,
    display_persistence, display_transparence, display_type,
)

# DVM subsystem
from dvm import (
    dvm_state, dvm_alarm, dvm_autorange, dvm_current,
    dvm_hold, dvm_mode, dvm_source,
)

# TIMebase subsystem
from timebase import (
    timebase_delay, timebase_reference, timebase_reference_position,
    timebase_scale, timebase_window, timebase_window_delay,
    timebase_window_scale,
)

# TRIGger subsystem (common + EDGE)
from trigger import (
    trigger_mode, trigger_run, trigger_status,
    trigger_stop, trigger_type, trigger_frequency,
    trigger_edge_coupling, trigger_edge_holdoff_devents,
    trigger_edge_holdoff_time, trigger_edge_holdoff,
    trigger_edge_hstart, trigger_edge_impedance,
    trigger_edge_level, trigger_edge_noise_reject,
    trigger_edge_slope, trigger_edge_source,
    trigger_config,
)

# TRIGger advanced types
from trigger_advanced import (
    trigger_delay_source_a, trigger_delay_source_b,
    trigger_delay_slope_a, trigger_delay_slope_b,
    trigger_delay_level_a, trigger_delay_level_b,
    trigger_dropout_time, trigger_dropout_type,
    trigger_interval_level, trigger_interval_limit,
    trigger_interval_tlower, trigger_interval_tupper,
    trigger_nedge_source, trigger_nedge_slope,
    trigger_nedge_idle, trigger_nedge_edge, trigger_nedge_level,
    trigger_pattern_input, trigger_pattern_level,
    trigger_pattern_limit, trigger_pattern_logic,
    trigger_pattern_tlower, trigger_pattern_tupper,
    trigger_pulse_polarity, trigger_pulse_limit,
    trigger_pulse_tlower, trigger_pulse_tupper,
    trigger_qualified_source, trigger_qualified_edge_source,
    trigger_qualified_type, trigger_qualified_lower_time,
    trigger_qualified_upper_time,
    trigger_runt_hlevel, trigger_runt_llevel,
    trigger_runt_limit, trigger_runt_polarity,
    trigger_runt_tlower, trigger_runt_tupper,
    trigger_shold_type, trigger_shold_clock_source,
    trigger_shold_clock_threshold, trigger_shold_data_source,
    trigger_shold_data_threshold, trigger_shold_slope,
    trigger_slope_hlevel, trigger_slope_llevel,
    trigger_slope_limit, trigger_slope_slope,
    trigger_slope_tlower, trigger_slope_tupper,
    trigger_video_field, trigger_video_frame_rate,
    trigger_video_interlace, trigger_video_line,
    trigger_video_source, trigger_video_standard,
    trigger_video_sync,
    trigger_window_center_level, trigger_window_delta_level,
    trigger_window_high_level, trigger_window_low_level,
    trigger_window_type,
)

# TRIGger serial types
from trigger_serial import (
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
)

# WAVeform subsystem
from waveform import (
    waveform_byteorder, waveform_source, waveform_start,
    waveform_interval, waveform_points, waveform_maxpoint,
    waveform_width, waveform_preamble, waveform_data,
    waveform_sequence,
    wavegen_output, wavegen_basic_wave, wavegen_frequency,
    wavegen_amplitude, wavegen_offset, wavegen_duty_cycle,
)

# MEASure subsystem
from measure import (
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
)

# SYSTem subsystem
from system import (
    system_buzzer, system_clock, system_date, system_time,
    system_language, system_reboot, system_shutdown,
    system_lan_gateway, system_lan_ip, system_lan_mac,
    system_lan_mask, system_lan_type,
    system_remote, system_touch, system_selfcal,
    system_ssaver, system_pon, system_edumode,
    system_vncport, system_nstorage,
    system_nstorage_connect, system_nstorage_disconnect,
    system_nstorage_status, system_menu,
)

# SAVE subsystem
from save import (
    save_setup, save_image, save_csv, save_binary,
    save_matlab, save_reference, save_default,
)

# DECode subsystem
from decode import (
    decode_state, decode_list_state, decode_list_line,
    decode_list_scroll, decode_list_result,
    decode_bus_state, decode_bus_copy, decode_bus_format,
    decode_bus_protocol, decode_bus_result,
    decode_bus_iic_rwbit, decode_bus_iic_scl_source,
    decode_bus_iic_sda_source,
)

# DIGital subsystem
from digital import (
    digital_state, digital_active, digital_bus_display,
    digital_bus_default, digital_bus_format, digital_bus_map,
    digital_channel_state, digital_height, digital_label,
    digital_points, digital_position, digital_skew,
    digital_srate, digital_threshold,
)

# FUNCtion subsystem (math/FFT/filter)
from function import (
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
)

# HISTORy subsystem
from history import (
    history_state, history_frame, history_interval,
    history_list, history_play, history_time,
)

# MEMory subsystem
from memory import (
    memory_horizontal_position, memory_horizontal_scale,
    memory_horizontal_sync, memory_import,
    memory_label_state, memory_label_text,
    memory_switch, memory_vertical_position,
    memory_vertical_scale,
)

# MTESt subsystem (mask test)
from mtest import (
    mtest_state, mtest_count, mtest_function_buzzer,
    mtest_function_cof, mtest_function_fth,
    mtest_function_sof, mtest_idisplay,
    mtest_mask_create, mtest_mask_load,
    mtest_operate, mtest_reset, mtest_source, mtest_type,
)

# RECall subsystem
from recall import (
    recall_factory_default, recall_reference, recall_serase,
    recall_setup,
)

# REF subsystem
from ref import (
    ref_label_state, ref_label_text,
    ref_data, ref_data_source, ref_data_scale, ref_data_position,
)

# SEARch subsystem
from search import (
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
)

# METEr subsystem (handheld scope-meter only)
from meter import (
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
