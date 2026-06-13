#!/usr/bin/env python3
"""Rewrite Chinese descriptions in tmosc-sds files to original English,
removing references to the SDS programming manual."""

import re
import os

BASE = "/mnt/data/csproject/tmllm/tmosc-sds"

# Translation mapping for commonly occurring Chinese descriptions.
# Key: the first line of the description block (stripped),
# Value: list of English replacement lines
TRANSLATIONS = {
    # ── acquire.py ──────────────────────────────────────────────────────
    "设置或查询示波器的采集方式。": [
        "Configures the oscilloscope acquisition type (sampling mode).",
        "NORMal — standard real-time sampling without averaging",
        "PEAK   — peak detect mode, captures extreme values at highest speed",
        "AVERage[,<times>] — averaging mode, <times> selects number of averages (4~8192, power of 2)",
        "ERES[,<bits>] — enhanced resolution mode, <bits> selects resolution (0.5~4.0)",
    ],
    "设置或查询示波器的显示模式。": [
        "Configures the waveform display mode.",
        "YT   — amplitude (Y) vs. time (T), the default view",
        "XY   — channel X vs. channel Y (Lissajous curve)",
        "ROLL — rolling mode, waveform scrolls from right to left",
    ],
    "设置或查询存储深度。存储深度影响单次采集可存储的采样点数。": [
        "Configures the memory depth, which determines how many sample points "
        "can be stored in a single acquisition.",
        "Available values depend on the current timebase and channel configuration.",
    ],
    "设置或查询采样率。采样率决定了每秒采集的样点数。": [
        "Configures the sample rate, which sets the number of samples captured per second.",
        "Example — set sample rate to 5 GSa/s: ACQ:SRAT 5.00E9",
    ],
    "设置或查询插值方式。插值影响波形在水平方向上的重构质量。": [
        "Configures the interpolation method used to reconstruct the waveform horizontally.",
        "ON  — sin(x)/x interpolation for smoother display",
        "OFF — linear interpolation between sample points",
    ],
    "设置或查询波形填充模式。": [
        "Configures the waveform acquisition filling mode.",
        "FAST — fast waveform acquisition",
        "SLOW — slow waveform acquisition",
    ],
    "查询已采集到的波形帧数。当任何影响波形采集的操作发生时": [
        "Queries the number of waveform frames that have been acquired. "
        "This counter resets to zero whenever a horizontal or vertical parameter change occurs.",
    ],
    "设置或查询示波器的 ADC 分辨率。": [
        "Configures the ADC resolution of the oscilloscope.",
        "<bit>:= {8Bits|10Bits}",
    ],
    "开启或关闭分段采集模式。分段采集将存储深度分成多个段，每个段": [
        "Enables or disables segmented (sequence) acquisition mode. "
        "Segmented acquisition divides the memory depth into multiple segments, "
        "each capturing one trigger event.",
        "Note: averaging and ERES modes are unavailable when sequence mode is active.",
    ],
    "设置或查询分段采集的段数。仅在分段模式开启时有效。": [
        "Configures the number of segments used in sequence acquisition mode. "
        "Effective only when sequence mode is enabled.",
    ],
    "设置或查询存储管理方式。": [
        "Configures the memory management strategy.",
        "AUTO    — automatically selects both memory depth and sample rate",
        "FSRate  — fixed sample rate; memory depth is set automatically",
        "FMDepth — fixed memory depth; sample rate is set automatically",
    ],
    "查询屏幕上当前波形的采样点数。": [
        "Queries the number of sample points on the current screen waveform.",
    ],
    "清除示波器的扫描并重新开始采集，等价于前面板上的 Clear Sweeps 按钮。": [
        "Clears the acquisition sweeps and restarts acquisition. "
        "Equivalent to the front-panel Clear Sweeps button. "
        "This is an action command with no parameters and no query form.",
    ],

    # ── channel.py ─────────────────────────────────────────────────────
    "设置或查询扩展策略中的垂直参考策略。": [
        "Configures the vertical reference strategy used during scale changes.",
        "OFFSet   — voltage offset stays fixed when the vertical scale changes; "
        "the waveform expands/contracts around the main X-axis of the screen.",
        "POSition — grid position stays fixed when the vertical scale changes; "
        "the waveform expands/contracts around a fixed screen location.",
    ],
    "设置或查询指定通道的开关状态。": [
        "Configures the display state (trace on/off) for the specified channel.",
    ],
    "设置或查询指定输入通道的耦合方式。": [
        "Configures the input coupling for the specified channel.",
        "AC  — AC coupling, blocks DC component",
        "DC  — DC coupling, passes all signal components",
        "GND — ground, disconnects input for zero-reference",
    ],
    "设置或查询指定输入通道的带宽限制。": [
        "Configures the bandwidth limit for the specified channel.",
        "20M  — 20 MHz bandwidth limit",
        "200M — 200 MHz bandwidth limit",
        "FULL — full bandwidth, no restriction",
        "OFF  — bandwidth limit disabled",
    ],
    "设置或查询指定通道的输入阻抗。": [
        "Configures the input impedance for the specified channel.",
        "ONEMeg — 1 M\u03a9",
        "FIFTy  — 50 \u03a9",
    ],
    "设置或查询指定通道的波形反相状态。": [
        "Configures waveform inversion for the specified channel.",
    ],
    "设置或查询指定通道的垂直偏移电压。": [
        "Configures the vertical offset voltage for the specified channel.",
    ],
    "设置或查询指定通道的垂直档位（V/div）。": [
        "Configures the vertical scale (volts/div) for the specified channel.",
    ],
    "设置或查询指定输入通道的探头衰减系数。": [
        "Configures the probe attenuation factor for the specified channel.",
        "DEFault — default 1X attenuation",
        "VALue,<value> — custom attenuation factor, range [1E-6, 1E6]",
        "Example: :CHANnel1:PROBe VALue,1.00E+02  (100X probe)",
    ],
    "设置或查询指定通道的时延校正值。用于补偿不同探头或通道之间的": [
        "Configures the channel deskew time to compensate for timing differences "
        "between probes or channels.",
    ],
    "设置或查询指定输入通道的垂直单位。": [
        "Configures the vertical unit for the specified channel.",
        "This affects measurement results, cursors, channel scale, "
        "and trigger level units.",
        "V — voltage (volts)",
        "A — current (amperes)",
    ],
    "设置或查询指定通道的标签文本。最多20个字符。": [
        "Configures the label text for the specified channel (up to 20 characters).",
    ],
    "设置或查询指定通道的标签显示开关状态。": [
        "Configures the label display on/off state for the specified channel.",
        "ON  — show label",
        "OFF — hide label",
    ],

    # ── counter.py ─────────────────────────────────────────────────────
    "设置或查询计数器开关状态。": [
        "Configures the counter on/off state.",
        "The counter measures frequency, period, and counts events on the selected signal.",
        "Measurements are performed on analog channel input signals only.",
    ],
    "查询计数器的当前值。": [
        "Queries the current counter measurement value.",
        "Note: counter accuracy is 7 digits; 3 digits are returned by default. "
        "Use :FORMat:DATA to request higher precision.",
    ],
    "设置或查询计数电平。": [
        "Configures the counter threshold level.",
        "Range varies by model: "
        "SDS7000A: [-4.26*V/div-offset, 4.26*V/div-offset], "
        "SDS6000Pro/A/L: [-4.5*V/div-offset, 4.5*V/div-offset], "
        "others: [-4.1*V/div-offset, 4.1*V/div-offset].",
    ],
    "设置或查询计数器的类型。": [
        "Configures the counter measurement mode.",
        "FREQuency — average frequency over a time window",
        "PERiod    — reciprocal of the average frequency",
        "TOTalizer — cumulative event count",
    ],
    "设置或查询指定计数器通道的源。": [
        "Configures the signal source channel for the counter.",
    ],
    "设置或查询计数器统计功能的开关状态。": [
        "Configures the counter statistics display on/off state.",
        "Statistics are available only in Frequency and Period modes.",
    ],
    "重置计数器统计，仅在计数器模式为周期和频率下有效。": [
        "Resets counter statistics. Effective only in Period and Frequency modes.",
    ],
    "查询当前计数器的统计信息，此功能仅在计数器模式为频率和周期时有效。": [
        "Queries the current counter statistics. "
        "Available only in Frequency and Period modes.",
        "Returns: <current>,<mean>,<min>,<max>,<stdev>,<count>",
        "  current — current measurement (NR3)",
        "  mean    — statistical mean (NR3)",
        "  min     — minimum value (NR3)",
        "  max     — maximum value (NR3)",
        "  stdev   — standard deviation (NR3)",
        "  count   — number of measurements (NR1)",
        "Note: returns \"OFF\" when statistics are disabled.",
    ],
    "设置或查询计数器统计门限的开关状态。": [
        "Configures the counter totalizer gate on/off state.",
    ],
    "设置或查询计数器统计门限电平。": [
        "Configures the counter totalizer gate threshold level. "
        "Range varies by model (same as :COUNter:LEVel).",
    ],
    "设置或查询计数器门限源的斜率/极性。": [
        "Configures the slope/polarity of the counter gate source.",
        "When gate type is Level, this sets polarity; when type is Edge, this sets slope.",
        "RISing  — rising edge / positive polarity",
        "FALLing — falling edge / negative polarity",
    ],
    "设置或查询计数门限类型。": [
        "Configures the counter gate type.",
        "LEVel — level-based gating",
        "AEDGe — edge-based gating (gate opens after edge)",
    ],
    "重置计数器累加功能的结果。": [
        "Resets the counter totalizer accumulated result.",
    ],
    "设置或查询计数源的斜率。": [
        "Configures the counting source slope.",
        "RISing  — count on rising edges",
        "FALLing — count on falling edges",
    ],

    # ── cursor.py ──────────────────────────────────────────────────────
    "设置或查询光标的开关状态。": [
        "Configures the cursor display on/off state.",
    ],
    "设置或查询光标样式。": [
        "Configures the cursor display style.",
        "FIXed     — fixed cursor style",
        "FOLLowing — following cursor style",
    ],
    "设置或查询X光标参考的类型。": [
        "Configures the X cursor reference type.",
        "DELay   — delay fixed: X cursor values stay constant when horizontal scale changes",
        "POSition — position fixed: X cursors stay at fixed grid positions when horizontal scale changes",
    ],
    "设置或查询Y光标参考的类型。": [
        "Configures the Y cursor reference type.",
        "OFFSet   — offset fixed: Y cursor values stay constant when vertical scale changes",
        "POSition — position fixed: Y cursors stay at fixed grid positions when vertical scale changes",
    ],
    "查询返回光标 1/(X2-X1) 当前值。": [
        "Queries the current 1/(X2-X1) cursor value.",
    ],
    "当光标模式为测量光标时，设置或查询测量项。": [
        "When cursor mode is MEASure, configures the measurement item.",
        "<type>:= same measurement types as the MEASure subsystem",
        "<source1>:= {C<n>|Z<n>|F<x>|M<m>|D<d>|ZD<d>|REF<r>}",
        "<source2>:= {C<n>} — only needed for channel-delay measurements",
    ],
    "设置或查询光标的模式。": [
        "Configures the cursor mode.",
        "MANual[,X|Y|XY] — manual cursor, can specify horizontal (X), vertical (Y), or both (XY)",
        "TRACk           — tracking cursor, automatically set to horizontal+vertical",
        "MEASure         — measurement cursor, shows how the measurement item is computed",
    ],
    "设置或查询光标 X1/Y1 测量的通道源。": [
        "Configures the X1/Y1 cursor source channel.",
        "<source>:= {C<n>|Z<n>|F<x>|M<m>|REF<r>|DIGital|HISTOGram}",
    ],
    "设置或查询光标 X2/Y2 测量的通道源。": [
        "Configures the X2/Y2 cursor source channel.",
        "<source>:= {C<n>|Z<n>|F<x>|M<m>|REF<r>|DIGital|HISTOGram}",
    ],
    "设置或查询光标X1的位置。": [
        "Configures the cursor X1 position.",
        "Range: [-grid_divs/2 * timebase + horizontal_delay, "
        "grid_divs/2 * timebase + horizontal_delay]",
    ],
    "设置或查询光标X2的位置。": [
        "Configures the cursor X2 position.",
        "Range: [-grid_divs/2 * timebase + horizontal_delay, "
        "grid_divs/2 * timebase + horizontal_delay]",
    ],
    "查询光标 X2 和 X1 当前位置的水平差。": [
        "Queries the horizontal difference X2 - X1.",
    ],
    "设置或查询光标Y1的位置。": [
        "Configures the cursor Y1 position.",
        "Range: [-grid_divs/2 * V/div + offset, grid_divs/2 * V/div + offset]",
    ],
    "设置或查询光标Y2的位置。": [
        "Configures the cursor Y2 position.",
        "Range: [-grid_divs/2 * V/div + offset, grid_divs/2 * V/div + offset]",
    ],
    "查询光标 Y2 和 Y1 当前位置的垂直差。": [
        "Queries the vertical difference Y2 - Y1.",
    ],
    "设置或查询指定手动X光标的开关状态。": [
        "Configures the on/off state for manual X cursor ``n``.",
        "<n>:= [1,8]",
    ],
    "设置或查询指定手动X光标的颜色。": [
        "Configures the color for manual X cursor ``n``.",
        "DEFault — default color derived from the cursor source",
        "DELTa   — synchronize to reference cursor color",
        "CUSTom,<string> — custom hex RGB color (e.g. \"#ff0000\")",
    ],
    "设置或查询指定手动光标X与参考光标固定相对位置的开关状态。": [
        "Configures whether manual X cursor ``n`` follows a reference cursor at a fixed offset.",
        "Note: can only be set when the reference cursor source is not NONE.",
    ],
    "设置或查询指定手动X光标的参考光标。": [
        "Configures the reference cursor for manual X cursor ``n``.",
        "<source>:= {MX<m>|TRACK<t>|NONE}",
        "  MX<m>: manual X cursor index [1,8]",
        "  TRACK<t>: tracking cursor index [1,8]",
        "  NONE: no reference cursor",
    ],
    "设置或查询指定手动X光标相对于参考光标的位置。": [
        "Configures the position of manual X cursor ``n`` relative to its reference cursor.",
    ],
    "设置或查询指定手动X光标的标签。": [
        "Configures the label for manual X cursor ``n``.",
        "DEFault — default empty label",
        "DELTa   — synchronize to reference cursor label",
        "CUSTom,<string> — custom label (up to 20 characters)",
    ],
    "设置或查询指定手动X光标的位置。": [
        "Configures the absolute position of manual X cursor ``n``.",
        "Range: [-grid_divs/2 * timebase + horizontal_delay, "
        "grid_divs/2 * timebase + horizontal_delay]",
    ],
    "设置或查询指定手动X光标的信源。": [
        "Configures the signal source for manual X cursor ``n``.",
        "<source>:= {C<n>|Z<n>|F<x>|ZF<x>|M<m>|ZM<m>|DIGital|ZDIGital|HISTOGram}",
    ],
    "设置或查询指定手动Y光标的开关状态。": [
        "Configures the on/off state for manual Y cursor ``n``.",
        "<n>:= [1,8]",
    ],
    "设置或查询指定手动Y光标的颜色。": [
        "Configures the color for manual Y cursor ``n``.",
        "DEFault — default color derived from the cursor source",
        "DELTa   — synchronize to reference cursor color",
        "CUSTom,<string> — custom hex RGB color",
    ],
    "设置或查询指定手动光标Y与参考光标固定相对位置的开关状态。": [
        "Configures whether manual Y cursor ``n`` follows a reference cursor at a fixed offset.",
    ],
    "设置或查询指定手动Y光标的参考光标。": [
        "Configures the reference cursor for manual Y cursor ``n``.",
        "<source>:= {MY<m>|NONE}, <m> = [1,8]",
    ],
    "设置或查询指定手动Y光标相对于参考光标的位置。": [
        "Configures the position of manual Y cursor ``n`` relative to its reference cursor.",
    ],
    "设置或查询指定手动Y光标的标签。": [
        "Configures the label for manual Y cursor ``n``.",
        "DEFault — default empty label",
        "DELTa   — synchronize to reference cursor label",
        "CUSTom,<string> — custom label (up to 20 characters)",
    ],
    "设置或查询指定手动Y光标的位置。": [
        "Configures the absolute position of manual Y cursor ``n``.",
        "Range: [-grid_divs/2 * V/div + offset, grid_divs/2 * V/div + offset]",
    ],
    "设置或查询指定手动Y光标的信源。": [
        "Configures the signal source for manual Y cursor ``n``.",
        "<source>:= {C<n>|Z<n>|F<x>|ZF<x>|M<m>|ZM<m>|HISTOGram}",
    ],
    "设置或查询指定测量光标MEA的开关状态。": [
        "Configures the on/off state for measurement cursor MEA ``n``.",
        "<n>:= [1,4]",
    ],
    "设置或查询指定测量光标MEA的颜色。": [
        "Configures the color for measurement cursor MEA ``n``.",
        "DEFault — default color derived from the cursor source",
        "CUSTom,<string> — custom hex RGB color",
    ],
    "设置或查询指定测量光标MEA的标签。": [
        "Configures the label for measurement cursor MEA ``n``.",
        "DEFault — default label",
        "CUSTom,<string> — custom label (up to 20 characters)",
    ],
    "设置或查询指定测量光标MEA的测量项。": [
        "Configures the measurement item for measurement cursor MEA ``n``.",
        "<type>:= same measurement types as the MEASure subsystem",
        "<source1>:= {C<n>|Z<n>|F<x>|M<m>|D<d>|ZD<d>}",
    ],
    "设置或查询指定追踪光标TX的开关状态。": [
        "Configures the on/off state for tracking cursor TX ``n``.",
        "<n>:= [1,8]",
    ],
    "设置或查询指定追踪光标TX的颜色。": [
        "Configures the color for tracking cursor TX ``n``.",
        "DEFault — default color derived from the cursor source",
        "DELTa   — synchronize to reference cursor color",
        "CUSTom,<string> — custom hex RGB color",
    ],
    "设置或查询指定追踪光标TX与参考光标固定相对位置的开关状态。": [
        "Configures whether tracking cursor TX ``n`` follows a reference cursor at a fixed offset.",
    ],
    "设置或查询指定追踪光标TX的参考光标。": [
        "Configures the reference cursor for tracking cursor TX ``n``.",
        "<source>:= {MX<m>|TRACK<t>|NONE}, <m>,<t> = [1,8]",
    ],
    "设置或查询指定追踪光标TX相对于参考光标的位置。": [
        "Configures the position of tracking cursor TX ``n`` relative to its reference cursor.",
    ],
    "设置或查询指定追踪光标TX的标签。": [
        "Configures the label for tracking cursor TX ``n``.",
        "DEFault — default empty label",
        "DELTa   — synchronize to reference cursor label",
        "CUSTom,<string> — custom label (up to 20 characters)",
    ],
    "设置或查询指定追踪光标TX的位置。": [
        "Configures the absolute position of tracking cursor TX ``n``.",
        "Range: [-grid_divs/2 * timebase + horizontal_delay, "
        "grid_divs/2 * timebase + horizontal_delay]",
    ],
    "设置或查询指定追踪光标TX的信源。": [
        "Configures the signal source for tracking cursor TX ``n``.",
        "<source>:= {C<n>|Z<n>|F<x>|ZF<x>|M<m>|ZM<m>|HISTOGram}",
    ],
    "查询指定追踪光标TX的当前值。": [
        "Queries the current value of tracking cursor TX ``n``.",
    ],
    "设置或查询指定XY X光标的开关状态。": [
        "Configures the on/off state for XY X cursor ``n``.",
        "<n>:= [1,4]",
    ],

    # ── decode.py ──────────────────────────────────────────────────────
    "设置或查询解码功能的开关状态。": [
        "Configures the global decode on/off state.",
    ],

    # ── digital.py ─────────────────────────────────────────────────────
    "设置或查询示波器的数字通道开关状态。": [
        "Configures the digital channel display on/off state.",
        "ON  — show digital channels",
        "OFF — hide digital channels",
    ],

    # ── display.py ─────────────────────────────────────────────────────
    "设置或查询轴标签显示状态。": [
        "Configures the axis label display state.",
        "ON  — show axis labels",
        "OFF — hide axis labels",
    ],
    "设置或查询轴标签显示模式。": [
        "Configures the axis label display mode.",
        "FIXed — fixed mode: axis stays in place, coordinates update with waveform movement",
        "MOVing — moving mode: axis follows waveform movement, coordinates stay fixed",
    ],
    "设置或查询轴标签垂直轴的显示位置。": [
        "Configures the vertical position of the axis labels.",
        "LEFT  — vertical axis on the left side of the screen",
        "MIDDle — vertical axis in the center of the screen",
        "RIGHt — vertical axis on the right side of the screen",
    ],
    "设置或查询当前示波器的屏幕亮度。": [
        "Configures the screen backlight brightness.",
        "<value>:= percentage [0,100]",
    ],
    "清除当前屏幕内显示的波形。": [
        "Clears the waveform display on screen.",
    ],
    "设置或查询色温状态。": [
        "Configures the color temperature display state.",
        "ON  — enable color temperature visualization",
        "OFF — disable color temperature visualization",
    ],
    "设置或查询当前示波器的网格亮度。": [
        "Configures the graticule (grid) brightness.",
        "<value>:= percentage [0,100]",
    ],
    "设置或查询网格的显示模式。": [
        "Configures the grid display style.",
        "FULL  — full grid: 8 rows x 10 columns",
        "LIGHt — light grid: screen divided into four quadrants",
        "NONE  — no grid",
    ],
    "设置隐藏右侧菜单。": [
        "Hides the right-side menu.",
    ],
    "设置或查询当前示波器波形亮度。": [
        "Configures the waveform trace brightness.",
        "<value>:= percentage [0,100]",
    ],
    "设置或查询菜单的显示样式。": [
        "Configures the menu display style.",
        "EMBedded — embedded style",
        "FLOating — floating style",
    ],
    "设置或查询隐藏菜单的时间。": [
        "Configures the menu auto-hide timeout.",
        "OFF — disable auto-hide",
        "3S|5S|10S|30S|60S — hide menu after specified delay",
    ],
    "设置或查询余辉的显示时间。": [
        "Configures the persistence display time.",
        "Model-dependent values:",
        "  SDS7000A/6000/3000/2000X HD: {OFF|INFinite|100MS|200MS|500MS|1S|5S|10S|30S}",
        "  SDS2000X Plus/SHS/1000X HD/800X HD: {OFF|INFinite|1S|5S|10S|30S}",
    ],
    "设置或查询信息显示框的透明度（如光标信息栏）。": [
        "Configures the transparency of info boxes (e.g. cursor info display).",
        "Applies to SHS800X/SHS1000X models only.",
    ],
    "设置或查询当前波形的显示类型。": [
        "Configures the waveform display type.",
        "VECTor — vector mode: sample points connected by lines",
        "DOT    — dot mode: raw sample points displayed directly",
    ],

    # ── dvm.py ─────────────────────────────────────────────────────────
    "设置或查询DVM开关状态。DVM功能可用于测量直流和交流振幅。": [
        "Configures the DVM (Digital Voltmeter) on/off state. "
        "The DVM measures DC and AC amplitudes.",
    ],
    "设置或查询DVM超量程报警开关状态。启用时，如果信号幅度超过": [
        "Configures the DVM over-range alarm on/off state. "
        "When enabled, an alarm triggers if the signal amplitude exceeds the screen range.",
    ],
    "设置或查询DVM自动量程开关状态。": [
        "Configures the DVM auto-range on/off state.",
    ],
    "查询DVM当前模式下测量值。当前默认有效位数为3位。": [
        "Queries the DVM measurement value in the current mode. "
        "Default precision is 3 significant digits.",
    ],
    "设置或查询DVM保持的开关状态。启用后，测量显示值将保持不变，": [
        "Configures the DVM hold on/off state. When enabled, the displayed "
        "measurement value is frozen while background measurement continues.",
    ],
    "设置或查询DVM测量模式。": [
        "Configures the DVM measurement mode.",
        "DCavg     — DC average: arithmetic mean of waveform data",
        "DCRMs     — DC RMS: root mean square of all data with DC coupling",
        "ACRMs     — AC RMS: root mean square of all data with AC coupling",
        "PKPK      — peak-to-peak: difference between maximum and minimum",
        "AMPLitude — amplitude: difference between top and base values",
    ],
    "设置或查询DVM测量的信源（模拟通道）。": [
        "Configures the DVM measurement source (analog channel).",
        "<source>:= {C1|C2|C3|C4}",
    ],

    # ── history.py ─────────────────────────────────────────────────────
    "设置或查询历史波形的开关状态。": [
        "Configures the history waveform display on/off state.",
        "ON  — enable history waveform playback",
        "OFF — disable history waveform playback",
    ],

    # ── measure.py ─────────────────────────────────────────────────────
    "设置或查询测量开关状态。": [
        "Configures the measurement on/off state.",
    ],
    "设置或查询测量显示模式。": [
        "Configures the measurement display mode.",
        "SIMPle  — simple measurement: up to 5 items displayed simultaneously",
        "ADVanced — advanced measurement: up to 12 items displayed simultaneously",
    ],
    "清除所有的高级测量项。": [
        "Clears all advanced measurement items.",
    ],
    "设置或查询高级测量M2模式下显示测量项总数。取值范围 [1,12]": [
        "Configures the number of measurement items displayed in advanced (M2) mode. "
        "Range [1,12].",
    ],
    "设置或查询指定高级测量项的开关状态。": [
        "Configures the on/off state for advanced measurement item ``n``.",
        "<n>:= [1,12]",
    ],
    "设置或查询指定高级测量项的信源A。": [
        "Configures source A for advanced measurement item ``n``.",
        "<source>:= {C<n>|Z<n>|F<x>|ZF<x>|M<m>|ZM<m>|D<d>|ZD<d>|REF<r>}",
    ],
    "设置或查询指定高级测量项的信源B。延迟测量项需设置信源B。": [
        "Configures source B for advanced measurement item ``n``. "
        "Required for delay-type measurements.",
        "<source>:= {C<n>|F<x>}",
    ],
    "设置或查询指定高级测量项的测量类型。": [
        "Configures the measurement type for advanced measurement item ``n``.",
        "Common types: PKPK, MAX, MIN, AMPLitude, MEAN, RMS, PERiod,",
        "FREQuency, RISetime, FALLtime, WIDTh, DUTY, OVERSHOOT,",
        "PRESHOOT, DELAY, DTIMe1-4, etc.",
        "See the measurement parameter table for the full list.",
    ],
    "查询指定高级测量项的测量值。": [
        "Queries the measurement value for advanced measurement item ``n``.",
    ],
    "设置或查询高级测量统计功能的开关状态。": [
        "Configures the advanced measurement statistics on/off state.",
    ],
    "重置所有高级测量统计结果。": [
        "Resets all advanced measurement statistics.",
    ],
    "清除所有简单测量项。": [
        "Clears all simple measurement items.",
    ],
    "设置或查询简单测量项类型。": [
        "Configures the simple measurement item type.",
    ],
    "设置或查询简单测量的信源。": [
        "Configures the source for simple measurements.",
        "<source>:= {C<n>|F<x>|M<m>|REF<r>}",
    ],
    "设置或查询测量门控开关状态。": [
        "Configures the measurement gate on/off state.",
    ],
    "设置或查询测量门控A的位置。": [
        "Configures measurement gate A position (left boundary).",
    ],
    "设置或查询测量门控B的位置。": [
        "Configures measurement gate B position (right boundary).",
    ],
    "设置或查询幅度测量策略。": [
        "Configures the amplitude measurement strategy.",
        "AUTO  — automatic selection",
        "MANual — manual selection",
    ],
    "设置或查询测量阈值信源。": [
        "Configures the measurement threshold source.",
        "<source>:= {C<n>|F<x>|M<m>|REF<r>}",
    ],
    "设置或查询测量阈值类型。": [
        "Configures the measurement threshold type.",
        "ABSolute — absolute voltage thresholds",
        "PERCent  — percentage-based thresholds",
    ],
    "设置或查询绝对阈值。": [
        "Configures the absolute measurement thresholds.",
        "Format: <high>,<mid>,<low> (volts)",
    ],
    "设置或查询百分比阈值。": [
        "Configures the percentage measurement thresholds.",
        "Format: <high>,<mid>,<low> (0-100%)",
    ],
    "设置测量结果显示样式。": [
        "Configures the measurement result display style.",
    ],
    "设置或查询高级测量显示样式。": [
        "Configures the advanced measurement display style.",
        "M1 — simple measurement display style",
        "M2 — advanced measurement display style",
    ],
    "查询指定高级测量项的统计值。": [
        "Queries the statistics value for advanced measurement item ``n``.",
    ],
    "查询指定高级测量项的历史统计数据。": [
        "Queries the statistics history for advanced measurement item ``n``.",
    ],
    "设置或查询AIM限制统计功能。": [
        "Configures the AIM limit statistics feature.",
    ],
    "设置或查询直方图统计功能。": [
        "Configures the histogram statistics feature.",
    ],
    "设置或查询统计最大计数值。": [
        "Configures the maximum statistics count value.",
    ],
    "设置或查询底部幅度测量策略。": [
        "Configures the base (bottom) amplitude measurement strategy.",
    ],
    "设置或查询顶部幅度测量策略。": [
        "Configures the top amplitude measurement strategy.",
    ],
    "查询简单测量的测量值。": [
        "Queries the simple measurement value.",
    ],

    # ── mtest.py ───────────────────────────────────────────────────────
    "基于当前波形创建模板。": [
        "Creates a mask based on the current waveform.",
        "<XMARgin> — horizontal X margin (float NR2)",
        "<YMARgin> — vertical Y margin (float NR2)",
    ],
    "加载模板文件。": [
        "Loads a mask file from internal memory or external storage.",
        "INTernal,<num> — load from internal storage, <num> [1,4]",
        "EXTernal,<path> — load from external file (.msk/.smsk)",
    ],
    "设置或查询模板测试运行状态。": [
        "Configures the mask test run state.",
    ],

    # ── root.py ────────────────────────────────────────────────────────
    "执行屏幕打印功能，返回当前屏幕截图数据。": [
        "Executes the screen print function and returns the current screenshot data.",
    ],
    "设置或查询NR3返回值的小数位数，默认返回SINGle格式。": [
        "Configures the NR3 return-value precision. Default format is SINGle.",
        "SINGle — 7 significant digits",
        "DOUBle — 14 significant digits",
        "CUSTom[,<digit>] — custom significant digits, <digit> range [1,64]",
    ],

    # ── save.py ────────────────────────────────────────────────────────
    "保存示波器设置。": [
        "Saves the oscilloscope setup.",
        "INTernal,<num> — save to internal storage, <num> [1,4]",
        "EXTernal,<path> — save to external file path",
    ],
    "保存截屏图片。": [
        "Saves a screenshot image.",
    ],
    "保存波形数据为CSV格式。": [
        "Saves waveform data in CSV format.",
    ],
    "保存波形数据为二进制格式。": [
        "Saves waveform data in binary format.",
    ],
    "保存波形数据为MATLAB格式。": [
        "Saves waveform data in MATLAB format.",
    ],
    "保存参考波形到文件。": [
        "Saves a reference waveform to file.",
    ],
    "保存设置作为默认配置。": [
        "Saves settings as the default configuration.",
        "CUSTom — save current user settings as default",
        "FACTory — restore factory settings as default",
    ],

    # ── system.py ──────────────────────────────────────────────────────
    "设置或查询蜂鸣器的开关状态。": [
        "Configures the buzzer on/off state.",
    ],
    "设置或查询示波器时钟源和内部10MHz时钟输出状态。": [
        "Configures the clock source and internal 10 MHz clock output state.",
        "EXT    — external clock source, 10 MHz output disabled automatically",
        "IN_ON  — internal clock source, 10 MHz output enabled",
        "IN_OFF — internal clock source, 10 MHz output disabled",
    ],
    "设置或查询示波器系统日期。": [
        "Configures the system date.",
        "Format: YYYYMMDD (8-digit integer, e.g. 20190819)",
    ],
    "设置或查询示波器系统时间。": [
        "Configures the system time.",
        "Format: HHMMSS (6-digit integer, e.g. 143025 for 14:30:25)",
    ],
    "设置或查询示波器显示语言。": [
        "Configures the display language.",
        "{SCHinese|TCHinese|ENGLish|FRENch|JAPanese|KORean|"
        "DEUTsch|ESPan|RUSSian|ITALiana|PORTuguese}",
    ],
    "重启示波器。": [
        "Reboots the oscilloscope.",
    ],
    "关闭示波器电源。": [
        "Shuts down the oscilloscope.",
    ],
    "设置或查询示波器局域网的网关。": [
        "Configures the LAN gateway address.",
    ],
    "设置或查询示波器局域网的IP地址。": [
        "Configures the LAN IP address.",
    ],
    "查询示波器的MAC地址。": [
        "Queries the oscilloscope MAC address.",
    ],
    "设置或查询示波器局域网的子网掩码。": [
        "Configures the LAN subnet mask.",
    ],
    "设置或查询远程控制锁定状态。锁定时触摸屏和前面板不可用。": [
        "Configures the remote control lock state. "
        "When locked, the touch screen and front panel are disabled.",
    ],
    "设置或查询触摸屏的开关状态。": [
        "Configures the touch screen on/off state.",
    ],
    "启动示波器自校准。查询返回状态: DOING=校准进行中, DONE=校准完成。": [
        "Starts the oscilloscope self-calibration. "
        "Query returns status: DOING = calibration in progress, DONE = calibration complete.",
    ],
    "设置或查询屏幕保护延时时长。": [
        "Configures the screen saver timeout.",
        "{OFF|1MIN|5MIN|10MIN|30MIN|60MIN}",
    ],
    "设置或查询上电自动开机状态。": [
        "Configures the power-on auto-start state.",
    ],
    "设置或查询教育模式下的功能锁定。": [
        "Configures the education mode function lock.",
        "<func>:= {AUTOSet|MEASure|CURSor} — function to lock/unlock",
        "<lock>:= {ON|OFF} — lock or unlock",
    ],
    "设置或查询VNC端口号，范围 [5900, 5999]。": [
        "Configures the VNC port number, range [5900, 5999].",
    ],
    "设置网络存储挂载参数。": [
        "Configures network storage mount parameters.",
        "<path> — network storage path",
        "<user> — username",
        "<pwd> — password",
        "<anon> — anonymous login toggle {ON|OFF}",
        "<auto_con> — auto-connect toggle {ON|OFF}",
        "<rem_path> — remote folder path",
        "<rem_pwd> — remote folder password",
    ],
    "设置或查询菜单显示状态。": [
        "Configures the menu display on/off state (models with Menu key).",
    ],
    "设置或查询示波器局域网配置方式。": [
        "Configures the LAN configuration mode.",
        "STATIC — manual IP configuration",
        "DHCP  — automatic IP assignment",
    ],

    # ── timebase.py ────────────────────────────────────────────────────
    "设置或查询水平触发延时。": [
        "Configures the horizontal trigger delay.",
    ],
    "设置或查询水平扩展参考策略。": [
        "Configures the horizontal expansion reference strategy.",
        "DELay   — delay fixed: horizontal delay value stays constant when "
        "timebase changes. The horizontal reference point position can be set; "
        "the delay value centers on that point.",
        "POSition — position fixed: delay stays at a fixed grid position when timebase changes.",
    ],
    "扩展策略为延时固定时，设置或查询水平参考中心位置。": [
        "When the reference strategy is DELay, configures the horizontal reference "
        "center position.",
        "<value>:= percentage [0,100]",
    ],
    "设置或查询主窗口时基。": [
        "Configures the main window timebase.",
        "Note: timebase range varies by model. Refer to the data sheet for details. "
        "When decreasing the timebase, the oscilloscope automatically matches the "
        "fastest available setting.",
    ],
    "设置或查询Zoom窗口的开关状态。": [
        "Configures the Zoom window on/off state.",
    ],
    "设置或查询Zoom窗口水平延时。": [
        "Configures the Zoom window horizontal delay.",
        "Note: the main window timebase and delay together determine the "
        "Zoom window delay range. The Zoom window must stay within the main "
        "window bounds. Values outside the range are clamped to the nearest "
        "available setting.",
    ],
    "设置或查询Zoom窗口时基。": [
        "Configures the Zoom window timebase.",
        "Note: the Zoom window timebase cannot exceed the main window timebase. "
        "If it does, it is automatically clamped to match.",
    ],

    # ── trigger.py ─────────────────────────────────────────────────────
    "设置或查询触发模式。": [
        "Configures the trigger mode.",
        "SINGle — single: captures one frame when trigger condition is met, then stops",
        "NORMal — normal: only acquires when trigger condition is met",
        "AUTO   — auto: forces an acquisition after the timeout period if no trigger occurs",
        "FTRIG  — force: forces a single acquisition regardless of trigger condition",
    ],
    "设置示波器状态为Run，并保持当前触发模式。": [
        "Sets the oscilloscope to Run state while preserving the current trigger mode.",
    ],
    "查询示波器当前触发状态。": [
        "Queries the current trigger status.",
        "{Arm|Ready|Auto|Trig'd|Stop|Roll}",
    ],
    "设置示波器状态为Stop。此命令等同于前面板Run/Stop按键的Stop。": [
        "Sets the oscilloscope to Stop state. Equivalent to the front-panel Run/Stop button.",
    ],
    "设置或查询触发类型。": [
        "Configures the trigger type.",
        "{EDGE|PULSE|SLOPe|INTerval|PATTern|RUNT|WINDow|DROPout|"
        "VIDeo|QUALified|NEDGe|DELay|SHOLd|IIC|SPI|UART|LIN|CAN|"
        "FLEXray|CANFd|IIS|M1553|SENT|A429}",
    ],
    "查询硬件频率计。如果频率有效则返回以Hz为单位的频率值。": [
        "Queries the hardware frequency counter. "
        "Returns the frequency in Hz when a valid reading is available. "
        "Default precision is 3 digits; up to 7 digits with :FORMat:DATA.",
    ],
    "设置或查询边沿触发的耦合方式。": [
        "Configures the edge trigger coupling mode.",
        "DC      — DC coupling: passes all signal components",
        "AC      — AC coupling: blocks the DC component",
        "LFREJect — low-frequency reject: acts as a high-pass filter",
        "HFREJect — high-frequency reject: acts as a low-pass filter",
    ],
    "设置或查询边沿触发的触发释抑事件数。": [
        "Configures the edge trigger holdoff event count.",
        "<value>:= [1, 100000000]",
    ],
    "设置或查询边沿触发的触发释抑时间。": [
        "Configures the edge trigger holdoff time.",
        "  Most models: [8.00E-09, 3.00E+01] s",
        "  SHS800X/1000X: [80.00E-09, 1.5E+00] s",
    ],
    "设置或查询边沿触发的触发释抑类型。": [
        "Configures the edge trigger holdoff type.",
        "OFF    — holdoff disabled",
        "EVENts — event-based: count of trigger-condition events",
        "TIME   — time-based: waiting period after trigger before re-arming",
    ],
    "设置或查询边沿触发的触发释抑启动条件。": [
        "Configures the edge trigger holdoff start condition.",
        "LAST_TRIG — counted from the last trigger time point",
        "ACQ_START — counted from the first time the condition is met",
    ],
    "设置或查询边沿触发的触发源阻抗，仅在触发源为EXT或EXT/5时可用。": [
        "Configures the edge trigger source impedance. "
        "Available only when the trigger source is EXT or EXT/5.",
        "ONEMeg — 1 M\u03a9",
        "FIFTy  — 50 \u03a9",
    ],
    "设置或查询边沿触发的触发电平。": [
        "Configures the edge trigger level.",
        "Range varies by model: "
        "SDS7000A: [-4.26*V/div-offset, 4.26*V/div-offset], "
        "SDS6000/SHS: [-4.5*V/div-offset, 4.5*V/div-offset], "
        "others: [-4.1*V/div-offset, 4.1*V/div-offset].",
    ],
    "设置或查询边沿触发的噪声抑制开关状态。": [
        "Configures the edge trigger noise reject on/off state.",
    ],
    "设置或查询边沿触发的斜率类型。": [
        "Configures the edge trigger slope type.",
        "RISing    — rising edge",
        "FALLing   — falling edge",
        "ALTernate — alternating edges",
    ],
    "设置或查询边沿触发的触发源。": [
        "Configures the edge trigger source.",
        "<source>:= {C<n>|D<d>|EX|EX5|LINE}",
        "  C<n>: analog channels (C1-C4)",
        "  D<d>: digital channels",
        "  EX/EX5: external trigger input",
        "  LINE: mains (line) trigger",
    ],

    # ── trigger_advanced.py ────────────────────────────────────────────
    "设置或查询延时触发信源A的状态。参数按C1-C<n>、D0-D15顺序配置。": [
        "Configures the delay trigger source A logic state. "
        "Parameters are configured in order C1 through C<n>, then D0 through D15.",
    ],
    "设置或查询延时触发信源B的信源。": [
        "Configures the delay trigger source B channel.",
    ],
    "设置或查询延时触发信源A的斜率类型。": [
        "Configures the delay trigger source A slope type.",
    ],
    "设置或查询延时触发信源B的斜率类型。": [
        "Configures the delay trigger source B slope type.",
    ],
    "设置或查询延时触发信源A的触发电平。": [
        "Configures the delay trigger source A level. "
        "Range varies by model (same as :TRIGger:EDGE:LEVel).",
    ],
    "设置或查询延时触发信源B的触发电平。": [
        "Configures the delay trigger source B level.",
    ],
    "设置或查询超时触发的超时时间。": [
        "Configures the dropout trigger timeout duration.",
    ],
    "设置或查询超时触发的超时类型。": [
        "Configures the dropout trigger type.",
    ],
    "设置或查询间隔触发的触发电平。": [
        "Configures the interval trigger level.",
    ],
    "设置或查询间隔触发的限制条件类型。": [
        "Configures the interval trigger limit condition type.",
    ],
    "设置或查询间隔触发限制条件的下限值。": [
        "Configures the interval trigger lower time limit.",
    ],
    "设置或查询间隔触发限制条件的上限值。": [
        "Configures the interval trigger upper time limit.",
    ],
    "设置或查询第N边沿触发的触发源。": [
        "Configures the Nth-edge trigger source.",
    ],
    "设置或查询第N边沿触发的斜率类型。": [
        "Configures the Nth-edge trigger slope type.",
    ],
    "设置或查询第N边沿触发的空闲时间。": [
        "Configures the Nth-edge trigger idle time.",
    ],
    "设置或查询第N边沿触发的边沿数。": [
        "Configures the Nth-edge trigger edge count.",
    ],
    "设置或查询第N边沿触发的触发电平。": [
        "Configures the Nth-edge trigger level.",
    ],
    "设置或查询码型触发源的逻辑状态。参数按C1-C<n>、D0-D15顺序配置。": [
        "Configures the pattern trigger source logic states. "
        "Parameters are configured in order C1 through C<n>, then D0 through D15.",
    ],
    "设置或查询码型触发源的逻辑电平。": [
        "Configures the pattern trigger source logic level.",
    ],
    "设置或查询码型触发的限制条件类型。": [
        "Configures the pattern trigger limit condition type.",
    ],
    "设置或查询码型触发的逻辑关系。": [
        "Configures the pattern trigger logic relationship.",
    ],
    "设置或查询码型触发限制条件的下限值。": [
        "Configures the pattern trigger lower time limit.",
    ],
    "设置或查询码型触发限制条件的上限值。": [
        "Configures the pattern trigger upper time limit.",
    ],
    "设置或查询脉宽触发的极性。": [
        "Configures the pulse width trigger polarity.",
    ],
    "设置或查询脉宽触发的限制条件类型。": [
        "Configures the pulse width trigger limit condition type.",
    ],
    "设置或查询脉宽触发限制条件的下限值。": [
        "Configures the pulse width trigger lower time limit.",
    ],
    "设置或查询脉宽触发限制条件的上限值。": [
        "Configures the pulse width trigger upper time limit.",
    ],
    "设置或查询前提边沿触发的前提信号信源。": [
        "Configures the qualified trigger qualifying signal source.",
    ],
    "设置或查询前提边沿触发的边沿触发信源。": [
        "Configures the qualified trigger edge signal source.",
    ],
    "设置或查询前提边沿触发的前提类型。": [
        "Configures the qualified trigger type.",
    ],
    "设置或查询前提边沿触发限制条件的下限值。": [
        "Configures the qualified trigger lower time limit. "
        "Effective only when the qualified type is \"level and timed\" or \"edge and timed\".",
    ],
    "设置或查询前提边沿触发限制条件的上限值。": [
        "Configures the qualified trigger upper time limit. "
        "Effective only when the qualified type is \"level and timed\" or \"edge and timed\".",
    ],
    "设置或查询欠幅触发的触发高电平。高电平不能小于低电平。": [
        "Configures the runt trigger high level. High level must not be less than low level.",
    ],
    "设置或查询欠幅触发的触发低电平。低电平不能大于高电平。": [
        "Configures the runt trigger low level. Low level must not be greater than high level.",
    ],
    "设置或查询欠幅触发的限制条件类型。": [
        "Configures the runt trigger limit condition type.",
    ],
    "设置或查询欠幅触发的极性。": [
        "Configures the runt trigger polarity.",
    ],
    "设置或查询欠幅触发限制条件的下限值。": [
        "Configures the runt trigger lower time limit.",
    ],
    "设置或查询欠幅触发限制条件的上限值。": [
        "Configures the runt trigger upper time limit.",
    ],
    "设置或查询建立/保持触发的类型。": [
        "Configures the setup/hold trigger type.",
    ],
    "设置或查询建立/保持触发的时钟信源。": [
        "Configures the setup/hold trigger clock source.",
    ],
    "设置或查询建立/保持触发的时钟阈值。": [
        "Configures the setup/hold trigger clock threshold.",
    ],
    "设置或查询建立/保持触发的数据信源。": [
        "Configures the setup/hold trigger data source.",
    ],
    "设置或查询建立/保持触发的数据源阈值。": [
        "Configures the setup/hold trigger data threshold.",
    ],
    "设置或查询建立/保持触发的斜率类型。": [
        "Configures the setup/hold trigger slope type.",
    ],
    "设置或查询斜率触发的触发高电平。高电平不能小于低电平。": [
        "Configures the slope trigger high level. High level must not be less than low level.",
    ],
    "设置或查询斜率触发的触发低电平。低电平不能大于高电平。": [
        "Configures the slope trigger low level. Low level must not be greater than high level.",
    ],
    "设置或查询斜率触发的限制条件类型。": [
        "Configures the slope trigger limit condition type.",
    ],
    "设置或查询斜率触发的斜率类型。": [
        "Configures the slope trigger slope type.",
    ],
    "设置或查询斜率触发限制条件的下限值。": [
        "Configures the slope trigger lower time limit.",
    ],
    "设置或查询斜率触发限制条件的上限值。": [
        "Configures the slope trigger upper time limit.",
    ],
    "设置或查询视频触发的同步触发场数。": [
        "Configures the video trigger sync field number. "
        "Effective only when standard is NTSC, PAL, 1080i/50, or 1080i/60.",
    ],
    "设置或查询视频触发自定义标准下的帧速率。": [
        "Configures the video trigger frame rate for the custom standard.",
    ],
    "设置或查询视频触发自定义标准下的交错比例。": [
        "Configures the video trigger interlace ratio for the custom standard.",
    ],
    "设置或查询视频触发非自定义标准下的同步触发行数。": [
        "Configures the video trigger sync line number (non-custom standards).",
    ],
    "设置或查询视频触发的触发源。": [
        "Configures the video trigger source.",
    ],
    "设置或查询视频触发的标准类型。": [
        "Configures the video trigger standard type.",
    ],
    "设置或查询视频触发的同步模式。": [
        "Configures the video trigger sync mode.",
    ],
    "设置或查询窗口触发的相对中心电平。": [
        "Configures the window trigger relative center level.",
    ],
    "设置或查询窗口触发的相对电平范围。": [
        "Configures the window trigger relative level range (delta).",
    ],
    "设置或查询窗口触发的绝对高电平。高电平不能小于低电平。": [
        "Configures the window trigger absolute high level. High level must not be less than low level.",
    ],
    "设置或查询窗口触发的绝对低电平。低电平不能大于高电平。": [
        "Configures the window trigger absolute low level. Low level must not be greater than high level.",
    ],
    "设置或查询窗口触发的窗口类型。": [
        "Configures the window trigger type.",
        "ABSolute — absolute window: high and low levels adjustable independently",
        "RELative — relative window: high and low levels move together",
    ],

    # ── trigger_serial.py ──────────────────────────────────────────────
    "设置或查询当前串行总线触发的协议类型。": [
        "Configures the current serial bus trigger protocol type.",
        "IIC|SPI|UART|CAN|LIN|FLEXray|CANFd|IIS|M1553|SENT|MANChester",
    ],
    "设置或查询当前I²C总线触发的触发条件。": [
        "Configures the I\u00b2C bus trigger condition. "
        "Available values depend on the selected condition type (e.g. STARt|STOP|RESTart|NACK|EEPRom).",
    ],
    "设置或查询I²C总线触发的地址值。": [
        "Configures the I\u00b2C trigger address value. "
        "Maximum value + 1 selects the 'any value' wildcard.",
    ],
    "设置或查询I²C总线触发地址的长度。": [
        "Configures the I\u00b2C trigger address length.",
        "{7BIT|10BIT}",
    ],
    "当前提为7/10位地址&数据时，设置或查询读写位。": [
        "Configures the read/write bit when the condition type is 7/10-bit address and data.",
    ],
    "设置或查询I²C总线触发的SCL时钟信源。": [
        "Configures the I\u00b2C trigger SCL clock signal source.",
    ],
    "设置或查询I²C总线触发的SCL时钟阈值。": [
        "Configures the I\u00b2C trigger SCL clock threshold.",
    ],
    "设置或查询I²C总线触发的SDA数据信源。": [
        "Configures the I\u00b2C trigger SDA data signal source.",
    ],
    "设置或查询I²C总线触发的SDA数据阈值。": [
        "Configures the I\u00b2C trigger SDA data threshold.",
    ],
    "设置或查询I²C总线触发的数据值。": [
        "Configures the I\u00b2C trigger data value.",
    ],
    "设置或查询SPI总线触发的比特流格式。": [
        "Configures the SPI trigger bit order.",
    ],
    "设置或查询SPI总线触发的CLK时钟信源。": [
        "Configures the SPI trigger CLK clock signal source.",
    ],
    "设置或查询SPI总线触发的CLK时钟阈值。": [
        "Configures the SPI trigger CLK clock threshold.",
    ],
    "设置或查询SPI总线触发的CS片选信源。": [
        "Configures the SPI trigger CS chip-select signal source.",
    ],
    "设置或查询SPI总线触发的CS片选阈值。": [
        "Configures the SPI trigger CS chip-select threshold.",
    ],
    "设置或查询SPI总线触发的片选类型。": [
        "Configures the SPI trigger chip-select type.",
    ],
    "设置或查询SPI总线触发的时钟采样边沿。": [
        "Configures the SPI trigger clock sampling edge.",
    ],
    "设置或查询SPI总线触发的MISO信源。": [
        "Configures the SPI trigger MISO signal source.",
    ],
    "设置或查询SPI总线触发的MISO阈值。": [
        "Configures the SPI trigger MISO threshold.",
    ],
    "设置或查询SPI总线触发的MOSI信源。": [
        "Configures the SPI trigger MOSI signal source.",
    ],
    "设置或查询SPI总线触发的MOSI阈值。": [
        "Configures the SPI trigger MOSI threshold.",
    ],
    "设置或查询SPI总线触发的NCS负片选信源。": [
        "Configures the SPI trigger NCS negative chip-select signal source.",
    ],
    "设置或查询SPI总线触发的NCS阈值。": [
        "Configures the SPI trigger NCS threshold.",
    ],
    "设置或查询UART总线触发的波特率。": [
        "Configures the UART trigger baud rate. "
        "Standard values include 600-115200 bps, or CUSTom for custom rates.",
    ],
    "设置或查询UART总线触发的数据长度（位数）。": [
        "Configures the UART trigger data length (in bits).",
    ],
    "设置或查询UART总线触发的奇偶校验。": [
        "Configures the UART trigger parity mode.",
    ],
    "设置或查询UART总线触发的停止位数。": [
        "Configures the UART trigger stop bit count.",
    ],
    "设置或查询UART总线触发的空闲电平。": [
        "Configures the UART trigger idle signal level.",
    ],
    "设置或查询UART总线触发的TX发送信源。": [
        "Configures the UART trigger TX (transmit) signal source.",
    ],
    "设置或查询UART总线触发的TX阈值。": [
        "Configures the UART trigger TX threshold.",
    ],
    "设置或查询UART总线触发的RX接收信源。": [
        "Configures the UART trigger RX (receive) signal source.",
    ],
    "设置或查询UART总线触发的RX阈值。": [
        "Configures the UART trigger RX threshold.",
    ],
    "设置或查询UART总线触发的数据1。最大值+1=任意值0xXX。": [
        "Configures the UART trigger data byte 1. Maximum value + 1 selects the 'any value' wildcard (0xXX).",
    ],
    "设置或查询UART总线触发的数据2。最大值+1=任意值0xXX。": [
        "Configures the UART trigger data byte 2. Maximum value + 1 selects the 'any value' wildcard (0xXX).",
    ],
    "设置或查询UART总线触发的触发条件。": [
        "Configures the UART trigger condition.",
    ],
    "设置或查询UART总线触发的数据比较类型。": [
        "Configures the UART trigger data comparison type.",
    ],
    "设置或查询CAN总线触发的波特率。": [
        "Configures the CAN trigger baud rate. "
        "Standard values include 5k-1M bps, or CUSTom for custom rates.",
    ],
    "设置或查询CAN总线触发的帧/消息ID。": [
        "Configures the CAN trigger frame/message ID.",
    ],
    "设置或查询CAN总线触发ID的长度。": [
        "Configures the CAN trigger ID length.",
        "{11BITS|29BITS}",
    ],
    "设置或查询CAN总线触发的数据值。": [
        "Configures the CAN trigger data value.",
    ],
    "设置或查询CAN总线触发的触发条件。": [
        "Configures the CAN trigger condition.",
    ],
    "设置或查询CAN总线触发的地址值（如CAN ID）。": [
        "Configures the CAN trigger address value (e.g. CAN ID). "
        "Maximum value + 1 selects the 'any value' wildcard.",
    ],
    "设置或查询LIN总线触发的协议版本。": [
        "Configures the LIN trigger protocol standard/revision.",
        "{0|1} (0 = Rev 1.3, 1 = Rev 2.x)",
    ],
    "设置或查询LIN总线触发的波特率。": [
        "Configures the LIN trigger baud rate.",
    ],
    "设置或查询LIN总线触发的数据比较类型。": [
        "Configures the LIN trigger data comparison type.",
    ],
    "设置或查询LIN总线触发的数据值。": [
        "Configures the LIN trigger data value.",
    ],
    "设置或查询LIN总线触发的触发条件。": [
        "Configures the LIN trigger condition.",
    ],
    "设置或查询FlexRay总线触发的帧比较类型。": [
        "Configures the FlexRay trigger frame comparison type.",
    ],
    "设置或查询FlexRay总线触发的周期数量。": [
        "Configures the FlexRay trigger frame cycle count.",
    ],
    "设置或查询FlexRay总线触发的帧ID。": [
        "Configures the FlexRay trigger frame ID.",
    ],
    "设置或查询FlexRay总线触发的重复系数。": [
        "Configures the FlexRay trigger frame repetition factor.",
    ],
    "设置或查询CAN FD总线触发的帧类型。": [
        "Configures the CAN FD trigger frame type.",
        "e.g. {BOTH|CAN|CANFd}",
    ],
    "设置或查询CAN FD总线触发的数据波特率。": [
        "Configures the CAN FD trigger data baud rate.",
    ],
    "设置或查询CAN FD总线触发的标准波特率。": [
        "Configures the CAN FD trigger nominal baud rate.",
    ],
    "设置或查询I²S总线触发的音频格式。": [
        "Configures the I\u00b2S trigger audio variant format.",
    ],
    "设置或查询I²S总线触发的位时钟BCLK信源。": [
        "Configures the I\u00b2S trigger BCLK bit-clock signal source.",
    ],
    "设置或查询I²S总线触发的位时钟BCLK阈值。": [
        "Configures the I\u00b2S trigger BCLK bit-clock threshold.",
    ],
    "设置或查询I²S总线触发的数据信源。": [
        "Configures the I\u00b2S trigger data signal source.",
    ],
    "设置或查询I²S总线触发的数据源阈值。": [
        "Configures the I\u00b2S trigger data threshold.",
    ],
    "设置或查询I²S总线触发的帧时钟WS信源。": [
        "Configures the I\u00b2S trigger WS word-select signal source.",
    ],
    "设置或查询I²S总线触发的帧时钟WS阈值。": [
        "Configures the I\u00b2S trigger WS word-select threshold.",
    ],
    "设置或查询I²S总线触发的左声道极性。": [
        "Configures the I\u00b2S trigger left channel polarity.",
    ],
    "设置或查询I²S总线触发的数据起始位偏移。": [
        "Configures the I\u00b2S trigger data start bit offset. "
        "Range depends on channel bit width and start bit configuration.",
    ],
    "设置或查询I²S总线触发的比特流格式。": [
        "Configures the I\u00b2S trigger bit order.",
    ],
    "设置或查询I²S总线触发的数据长度（位数）。": [
        "Configures the I\u00b2S trigger data length (in bits).",
    ],
    "设置或查询I²S总线触发的数据值。": [
        "Configures the I\u00b2S trigger data value.",
    ],
    "设置或查询I²S总线触发的触发条件。": [
        "Configures the I\u00b2S trigger condition.",
    ],
    "设置或查询I²S总线触发的数据比较类型。": [
        "Configures the I\u00b2S trigger data comparison type.",
    ],
    "设置或查询I²S总线触发的时钟采样边沿。": [
        "Configures the I\u00b2S trigger clock sampling edge.",
    ],

    # ── waveform.py ────────────────────────────────────────────────────
    "设置或查询传输波形数据字的字节顺序。当波形数据按16bit传输时": [
        "Configures the byte order for waveform data transfer (16-bit mode). "
        "Byte order must be set when waveform data is transferred as 16-bit words; "
        "default is LSB.",
        "MSB — most significant byte first",
        "LSB — least significant byte first",
    ],
    "设置或查询传输波形数据的源。": [
        "Configures the waveform data source for transfer.",
        "<source>:= {C<n>|F<x>|D<d>}",
        "  C<n>: analog channels (C1-C4)",
        "  F<x>: math functions",
        "  D<d>: digital channels",
    ],
    "设置或查询传输波形数据的起始点。": [
        "Configures the start point for waveform data transfer.",
    ],
    "设置或查询每次传输的波形点数。": [
        "Configures the number of waveform points to transfer per operation.",
    ],
    "设置或查询波形数据采样间隔。": [
        "Configures the waveform data sparsing interval (every Nth point).",
    ],
    "设置或查询传输波形数据字的宽度。": [
        "Configures the word width for waveform data transfer.",
        "BYTE — 8-bit data transfer",
        "WORD — 16-bit data transfer",
    ],
    "查询发送指定的检索参数。": [
        "Queries the waveform preamble (metadata without data transfer).",
    ],
    "查询返回通道C<n>的波形数据。": [
        "Queries and returns the waveform data for the specified source.",
    ],
    "设置波形数据点到内存或从内存读取。": [
        "Saves waveform data points to reference memory or reads them back.",
    ],
    "设置或查询数据流中的采集计数。": [
        "Configures the acquisition count in the data stream.",
    ],
}


def _basic_translate(text):
    """Basic fallback translation for unmatched Chinese text."""
    text = re.sub(r'设置或查询', 'Configures the', text)
    text = re.sub(r'查询', 'Queries the', text)
    text = re.sub(r'设置', 'Sets the', text)
    text = re.sub(r'开启或关闭', 'Enables or disables', text)
    text = re.sub(r'清除', 'Clears', text)
    text = re.sub(r'重启示波器', 'Reboots the oscilloscope', text)
    text = re.sub(r'关闭示波器电源', 'Shuts down the oscilloscope', text)
    text = re.sub(r'重置', 'Resets', text)
    text = re.sub(r'保存', 'Saves', text)
    text = re.sub(r'加载', 'Loads', text)
    text = re.sub(r'启动', 'Starts', text)
    text = re.sub(r'执行', 'Executes', text)
    text = re.sub(r'基于', 'Based on', text)
    text = re.sub(r'返回', 'Returns', text)
    text = re.sub(r'的', '', text)
    return text


def process_file(filepath):
    """Process a single Python file, rewriting description blocks."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if 'Description (from SDS programming manual' in stripped:
            i += 1  # skip the Description line
            desc_lines = []
            while i < len(lines):
                next_line = lines[i]
                next_stripped = next_line.strip()
                if next_stripped == '' or len(next_line) == 0:
                    break
                stripped_start = len(next_line) - len(next_line.lstrip())
                if stripped_start <= 4:
                    break
                desc_lines.append(next_stripped)
                i += 1

            if desc_lines:
                full_text = desc_lines[0]
                eng_lines = TRANSLATIONS.get(full_text)
                if eng_lines is None:
                    eng_lines = [_basic_translate(line) for line in desc_lines]
                    print(f"  WARNING: No translation for: {full_text}")
                indent = ' ' * 8
                for eng in eng_lines:
                    new_lines.append(f"{indent}{eng}\n")
        else:
            new_lines.append(line)
            i += 1

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)


def main():
    files = [
        'acquire.py', 'channel.py', 'counter.py', 'cursor.py',
        'decode.py', 'digital.py', 'display.py', 'dvm.py',
        'history.py', 'measure.py', 'mtest.py', 'root.py',
        'save.py', 'system.py', 'timebase.py', 'trigger.py',
        'trigger_advanced.py', 'trigger_serial.py', 'waveform.py',
    ]

    import os
    for fname in files:
        fpath = os.path.join(BASE, fname)
        if os.path.exists(fpath):
            print(f"Processing {fname}...")
            process_file(fpath)
        else:
            print(f"SKIP: {fname} not found")

    print("Done.")


if __name__ == '__main__':
    main()
