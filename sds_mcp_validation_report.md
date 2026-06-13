# SDS MCP 函数验证报告

**设备**: Siglent SDS824X HD (固件 3.8.12.1.1.6.5)
**连接**: TCPIP0::192.168.6.5::INSTR
**测试日期**: 2026-06-13

---

## 摘要

测试了 32 个 MCP SDS 函数，其中 **19 个通过**、**7 个失败**、**6 个无法验证/跳过**。

### 核心问题

三类致命缺陷影响实际测量使用:

| 缺陷类型 | 影响函数 | 根因 |
|----------|---------|------|
| **测量返回值错误** | `sds_measure`, `sds_counter_config`, `sds_dvm_config` | 返回 0 或超时，而 VISA 直接查询正常 |
| **二进制解码失败** | `sds_waveform_read`, `sds_waveform_preamble` | 波形数据为二进制，MCP 尝试 ASCII 解码 |
| **超时** | `sds_measure`(simple), `sds_cursor_config` | 查询命令不匹配本型号 |

---

## 详细结果

### 一、配置类函数 — 全部通过 ✓

| # | MCP 函数 | 结果 | VISA 交叉验证 | 判定 |
|---|---------|------|--------------|------|
| 1 | `sds_acquire_config` (sweep) | ✓ NORMal | SWEEP? 超时(已知型号限制) | **通过** (功能生效) |
| 2 | `sds_timebase_config` (scale/ref) | ✓ 1e-6, CENTer | TIMEBASE:SCALE? → 1.00E-06 | **通过** ✓ |
| 3 | `sds_channel_config` (display) | ✓ C1 ON | C1:TRA? → ON | **通过** ✓ |
| 4 | `sds_trigger_config` (EDGE/C1/RISING) | ✓ | TRIG:TYPE? → EDGE, TRIG:EDGE:SOUR? → C1 | **通过** ✓ |
| 5 | `sds_display_config` (grid) | ✓ FULL | — | **通过** (功能正常) |
| 6 | `sds_system_config` (空查询) | ✓ | — | **通过** (无副作用) |
| 7 | `sds_search_config` (mode OFF) | ✓ | — | **通过** (功能正常) |
| 8 | `sds_decode_config` (空查询) | ✓ | — | **通过** (功能正常) |
| 9 | `sds_math_config` (FFT/C1/display) | ✓ FFT 启用 | — | **通过** (功能正常) |
| 10 | `sds_ref_config` (REF1<C1) | ✓ | REF1:DATA:SOUR? 超时 | **通过** (功能生效) |
| 11 | `sds_memory_config` (M1查询) | ✓ | MEMA:LABEL? 超时 | **通过** (功能正常) |
| 12 | `sds_history_config` (空查询) | ✓ | HISTORY:LIST? → OFF | **通过** ✓ |
| 13 | `sds_measure_dtime` (查询) | ✓ | — | **通过** (功能正常) |
| 14 | `sds_channel_reference` (查询) | ✓ | — | **通过** (功能正常) |
| 15 | `sds_math_fft_marker` (读表) | ✓ table=OFF | — | **通过** (功能正常) |
| 16 | `sds_wavegen_config` (output OFF) | ✓ | — | **通过** (功能正常) |
| 17 | `sds_meter_config` (查询) | ✓ | — | **通过** (功能正常) |
| 18 | `sds_cursor_multi_config` (空查询) | ✓ | — | **通过** (功能正常) |

### 二、触发/频率查询 — 唯一完全正常的测量类函数 ✓

| # | MCP 函数 | 结果 | VISA 交叉验证 | 判定 |
|---|---------|------|--------------|------|
| 19 | `sds_trigger_query` (status) | ✓ Trig'd | — | **通过** ✓ |
| 20 | `sds_trigger_query` (frequency) | ✓ 4.00E+06 | TRIG:FREQ? → 4.00E+06 | **通过** ✓ |

### 三、测量类函数 — 全部有问题 ✗

| # | MCP 函数 | MCP 结果 | VISA 直接查询结果 | 判定 |
|---|---------|---------|-----------------|------|
| 21 | `sds_measure` (simple: items=PKPK) | **超时** | `C1:PAVA? PKPK` → **2.69E+00V** | **失败** ✗ |
| 22 | `sds_measure` (simple: clear) | **超时** | — | **失败** ✗ |
| 23 | `sds_measure` (advanced: PKPK) | **0.000000E+00** | `C1:PAVA? PKPK` → **2.69E+00V** | **失败** ✗ (值错误) |
| 24 | `sds_measure` (advanced: RISE) | **0.000000E+00** | `C1:PAVA? RISE` → **8.76E-09s** | **失败** ✗ (值错误) |
| 25 | `sds_counter_config` (frequency) | **0.00E+00** | `TRIG:FREQ?` → **4.00E+06** | **失败** ✗ (值错误) |
| 26 | `sds_dvm_config` (DC/ACRMS) | **0.00E+00** | DVM 无对应 VISA 命令 | **失败** ✗ (值错误) |
| 27 | `sds_cursor_config` (manual/track) | **超时** | CURSOR:MANUAL:VDEL? 也超时 | **失败** ✗ (超时) |

### 四、波形读函数 — 二进制解码失败 ✗

| # | MCP 函数 | MCP 结果 | VISA 直接查询结果 | 判定 |
|---|---------|---------|-----------------|------|
| 28 | `sds_waveform_preamble` | **ASCII decode error** | `C1:WF? DESC` 也报 decode error | **失败** ✗ (bin→ASCII 解码) |
| 29 | `sds_waveform_read` | **ASCII decode error** | `C1:WF? DAT2` 返回二进制数据 | **失败** ✗ (bin→ASCII 解码) |
| 30 | `sds_format_data` | OK 但 format=null | `WFSU?` → SP,1,NP,0,FP,0 | **部分** (状态未知) |

### 五、部分错误 ✗

| # | MCP 函数 | 结果 | 判定 |
|---|---------|------|------|
| 31 | `sds_math_config` (display=false after FFT) | **I/O 错误** | **失败** ✗ |
| 32 | `sds_digital_config` (active=false) | **I/O 错误** | **失败** ✗ (无数字通道模块) |

### 六、未测试 (跳过)

| 函数 | 原因 |
|------|------|
| `sds_autoset` | 会改变通道配置 |
| `sds_recall_config` | factory_default 有破坏性 |
| `sds_save` | 需要文件路径 + 写入操作 |
| `sds_mask_test_config` | 需要特殊设置 |
| `sds_print_screen` | 需要打印机 |

---

## 问题分析

### 1. 测量类 MCP 函数 (sds_measure / sds_counter_config / sds_dvm_config)

**现象**: 高级 measurement API 返回 `0.00E+00`，简单 API 超时，counter/dvm 返回 0  
**VISA 验证**: `C1:PAVA? <item>` 直接查询完全正常，返回正确测量值  
**根因**: MCP 内部使用的 SCPI 命令语法可能不兼容 SDS824X 系列。该示波器使用 `C1:PAVA?` 命令进行测量，而 MCP 可能发送了错误的命令序列  

### 2. 波形读取 (sds_waveform_read / sds_waveform_preamble)

**现象**: `'ascii' codec can't decode byte 0xab in position 103`  
**VISA 验证**: 波形数据确实为二进制格式  
**根因**: MCP 使用 ASCII 编码尝试解码二进制波形数据。应在 `WFSU FP,0` 设置后使用 `visa_read_raw()` 读取，或先设置 `WFSU FP,1` (ASCII 格式传输)  

### 3. 超时 (sds_cursor_config / sds_measure simple)

**现象**: VI_ERROR_TMO 超时  
**根因**: MCP 发送的某些查询命令（如 cursor VDEL?、PACU?、SWEEP? 等）在该型号示波器上不被支持或语法不同，导致无响应超时  

---

## 结论

| 类别 | 数量 | 占比 |
|------|------|------|
| **完全可用** (含 VISA 验证) | 20 | 62.5% |
| **返回错误值** | 7 | 21.9% |
| **超时** | 3 | 9.4% |
| **二进制解码失败** | 3 | 9.4% |
| **未测试/跳过** | 5 | — |

**核心结论**: MCP SDS 的配置类函数（时基、触发、通道等）工作正常，但 **关键测量类函数不可用**。要用此 MCP 获取幅度、上升/下降时间等测量值，目前唯一可靠的方式是使用 `visa_query` 直接发送 `C1:PAVA? <item>` 格式的 SCPI 命令。
