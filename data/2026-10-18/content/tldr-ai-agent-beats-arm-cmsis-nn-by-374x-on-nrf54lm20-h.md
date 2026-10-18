---
title: AI Agent Beats ARM CMSIS-NN by 3.74x on nRF54LM20 - Hackster.io
url: https://www.hackster.io/maxxlife/ai-agent-beats-arm-cmsis-nn-by-3-74x-on-nrf54lm20-66158a
site_name: tldr
content_file: tldr-ai-agent-beats-arm-cmsis-nn-by-374x-on-nrf54lm20-h
fetched_at: '2026-10-18T14:18:01.963343'
original_url: https://www.hackster.io/maxxlife/ai-agent-beats-arm-cmsis-nn-by-3-74x-on-nrf54lm20-66158a
date: '2026-10-18'
description: How an autonomous gemini-4-argon Hardware-in-the-Loop (HIL) agent wrote a kernel on Cortex-M33F that outperforms official ARM CMSIS-NN s4. Find this and other hardware projects on Hackster.io.
tags:
- tldr
---

×

### Embed the widget on your own site

Add the following snippet to your HTML:<iframe frameborder='0' height='385' scrolling='no' src='https://www.hackster.io/maxxlife/ai-agent-beats-arm-cmsis-nn-by-3-74x-on-nrf54lm20-66158a/embed' width='350'></iframe>

How an autonomous gemini-4-argon Hardware-in-the-Loop (HIL) agent wrote a kernel on Cortex-M33F that outperforms official ARM CMSIS-NN s4.

Read up about this project on

#### AI Agent Beats ARM CMSIS-NN by 3.74x on nRF54LM20

Maksim Masalski
0
 
1
 
* Overview
* Things
* Story
* 1. From Google ML Drift to Microcontrollers
* 2. Architecture of the Autonomous HIL AI Agent (agent.py
* Five Engineering Patterns That Made agent.py Work in Production
* 3. The Workload: MAC-Smasher & INT4 (Q4_0) Math
* 4. Evolution of the INT4 Kernel: 5 Sprints with gemini-4-argon
* Sprint 1 (v0.2): The Naive Baseline — 605, 742 cycles (27.7 MOPS
* Sprint 2 (v0.3): Zero-Point Hoisting + int16 Scales — 240, 723 cycles (SRAM) / 271, 492 cycles (RRAM
* Sprint 3 (v0.5): Single-Cycle ARM Barrel-Shifter Unpacking — 179, 573 cycles (SRAM) / 218, 289 cycles (RRAM
* Sprint 4 (v0.6): Eliminating 22 Stack Spills via disassemble_symbol — 130, 480 cycles (SRAM) / 166, 239 cycles (RRAM
* Sprint 5 (v0.7 — Final Silicon Record): 64-bit LDRD + FPU Register File Hijacking (VMOV) — 114, 534 cycles (SRAM) / 148, 921 cycles (RRAM
* Summary of the Agent's Optimization Trajectory (INT4 group_size=32)
* 5. Debunking the T-MAC (LUT) Myth on Cortex-M33
* 6. Final Silicon Benchmarks on Nordic nRF54LM20B (v0.7
* Key Engineering Takeaways
* 7. Source code of the Benchmark
* 8. What's Next for MCU-Drift
* Code
* Credits
* Comments(0)
Maksim Masalski
Published 
October 18, 2026
 
©
 
Apache-2.0

# AI Agent Beats ARM CMSIS-NN by 3.74x on nRF54LM20

How an autonomous gemini-4-argon Hardware-in-the-Loop (HIL) agent wrote a kernel on Cortex-M33F that outperforms official ARM CMSIS-NN s4.

Advanced
Protip
4 hours
6

## Things used in this project

### Hardware components

Nordic Semiconductor nRF54LM20 DK
×
1

### Software apps and online services

Google AI Studio
Google Gemini API
Nordic Semiconductor nRF Connect SDK
ARM CMSIS-NN

## Story

### 1. From Google ML Drift to Microcontrollers

In myprevious Hackster article,I pushed theNordic nRF54LM20B DKand itsAxon NPUto their limits on Zephyr RTOS, benchmarking ourMAC-SmasherFullyConnected / GEMV [1, 256] x [256, 256] workload (65, 536 MACs = 131, 072 OPs).

Recently, while exploring Google’s new open-source GPU inference engine,google-ai-edge/ml-driftI was inspired by two of its core design principles:

* Low-level hardware roofline profiling:Measuring exact memory bandwidth (GB/s), compute throughput (GFLOP/s), and identifying hardware bottlenecks per layer.
* Block-wise 4-bit quantization (INT4, group_size=32 / Q4_0):Compressing weights down to 4 bits with per-group scales so LLM and TinyML weights fit inside tight on-chip caches.

That sparked a question:Can I bring the ML Drift philosophy down to bare-metal microcontrollers?

Non-volatile memory (Flash/RRAM) and SRAM on MCUs are precious. Block-quantized INT4 (group_size=32) cuts a 256x256 weight matrix from 64 KB (INT8) down to just36 KB(32 KB packed nibbles + 4 KB int16 scales). However, there is a notorious catch in embedded ML:4-bit inference on CPUs is often slower than 8-bit inferencebecause the CPU burns too many ALU cycles unpacking 4-bit nibbles into 16-bit registers before it can execute SIMD Multiply-Accumulate (SMLAD) instructions. Even ARM's official arm_fully_connected_s4 inCMSIS-NNsuffers from this unpacking tax.

Instead of spending weeks manually writing and tweaking Thumb-2 inline assembly, I builtMCU-Drift— a hardware profiler paired with an autonomousHardware-in-the-Loop (HIL) AI Agentpowered bygemini-4-argon— and gave it direct physical access to annRF54LM20B DKto see if it could beat human-written assembly from ARM.

Spoiler:It beat official ARM CMSIS-NN s4 by 3.74x, and even beat 8-bit CMSIS-NN s8 by 1.95x.

### 2. Architecture of the Autonomous HIL AI Agent (agent.py)

Optimizing assembly in a simulator is a trap: simulators rarely model RRAM wait-states, bus matrix contention, LSU (Load-Store Unit) pipeline stalls, or instruction prefetch buffer alignment accurately. To optimize for real silicon, the AI agent neededreal silicon in the loop.

I connected theNordic nRF54LM20B DKto an Ubuntu 24.04 Linux NUC server and wrote agent.py around gemini-4-argon.

Elementary agent workflow diagram:

This diagram answers the question of what components the system consists of and how they are connected.

Functional flow diagram:

It shows the full operating cycle of the HIL agent

The functional diagram shows the operating sequence of an autonomous HIL agent: from code analysis and modification to compilation, flashing, performance measurement on a real microcontroller, and making a decision for the next optimization iteration.

┌────────────────────┐ ┌────────────────────┐ ┌─────────────────────┐
│ Agent / Source │ │ Build / Execution │ │ Profile / Decision │
│ │ │ │ │ │
│ Start │ │ Build │ │ Cycles ─┐ │
│ ↓ │ │ ↓ │ │ ├→ UART │
│ Read │ → │ Flash │ → │ Verify ─┘ │
│ ↓ │ │ ↓ │ │ ↓ │
│ Analyze │ │ Execute │ │ Disassemble │
│ ↓ │ │ │ │ ↓ │
│ Patch │ │ │ │ Decision │
└────────────────────┘ └────────────────────┘ │ ↓ │
 ↑ │ Commit / Limit │
 └────────── next optimization ──────────┘

### Five Engineering Patterns That Made agent.py Work in Production

When building autonomous coding agents for embedded systems, naive loops quickly burn millions of tokens dumping huge .elf files or rewriting entire source files. We designed agent.py aroundshort, deterministic 8-step sprints(MAX_STEPS = 8, MAX_TOKENS = 250_000) with five key engineering mechanisms:

* Surgical Diffs (patch_file & Line-Bounded read_file):Instead of regenerating an entire 800-line C file on every edit, the system prompt strictly enforces usingpatch_file(path, old_snippet, new_snippet)and reading <=160 lines at a time viaread_file(). This cuts output token consumption by~90%and prevents accidental edits to the benchmark harness.
* Single-Call build_flash_and_profile(disassemble_symbol):Rather than wasting 4 separate LLM turns to compile, flash, read serial, and run objdump, a single tool call compiles the Zephyr project (west build), flashes the nRF54LM20B (west flash), captures the live UART benchmark table, and optionally extracts the disassembly ofonly the target C function(arm-none-eabi-objdump -d --disassemble=<symbol>), returning <2, 000 characters of exact Thumb-2 assembly straight into the model's context.
* Zero-Drop Pre-Flash Serial Capture:The nRF54LM20B boots in milliseconds after J-Link finishes flashing. If you open/dev/ttyACM1afterwest flash exits, you miss the top half of the UART output! In build_flash_and_profile(), agent.py opens/dev/ttyACM1and flushes the RX bufferbeforeinvoking west flash, then parses until it detects the two closing dashed lines (----) of the profiler table.
* Hard Kill-Switch on Victory (git_commit_and_finish -> sys.exit(0)):As soon as a sprint hits its performance goal with Verify:PASS, the agent callsgit_commit_and_finish(title, notes). This tool automatically embeds latest_uart_table.txt into the Git commit body (=== LIVE HARDWARE BENCHMARK (nRF54LM20B) ===) and immediately callssys.exit(0)so the agent doesn't spend extra tokens chatting after completing the task. If an experiment breaks math verification,git_revert_uncommitted()cleanly resets the working tree.
* Fixing the WFI DWT Reset Trap on nRF54L Silicon:On the nRF54L series, calling Zephyr's k_msleep() enters WFI (Wait For Interrupt), which powers down the debug domain and resets the ARM DWT cycle counter (CYCCNT)! Inside our C harness, we explicitly re-initialize and start<zephyr/timing/timing.h>after any UART drain sleep right before running the kernels:
k_msleep(10); // Allow UART TX buffer to drain
timing_init();
timing_start();

### 3. The Workload: MAC-Smasher & INT4 (Q4_0) Math

To maintain a strict apples-to-apples comparison withPart 1, we used the exact sameMAC-Smasherlayer:

* Operation:FullyConnected / GEMV
* Input Activation Vector (x):[1, 256] (INT8)
* Weight Matrix (W):[256, 256]
* Total Compute:65, 536 MACs (131, 072 OPs)

In our INT4 (group_size=32) format (inspired by GGML Q4_0 and ML Drift):

* Every row of 256 weights is divided into8 groupsof 32 weights.
* Each 4-bit weight

is stored as an unsigned nibble with a fixed zero-point offset of 8, coupled with a group scale Sg.

Then:

* Two 4-bit weights are packed into a single byte (16 bytes per group of 32 weights, 128 bytes per row, 32 KB total for the matrix), plus 256 * 8 = 2, 048 int16 group scales (4 KB), totaling36 KB.

### 4. Evolution of the INT4 Kernel: 5 Sprints with gemini-4-argon

Watchinggemini-4-argoniterate throughbuild_flash_and_profile(disassemble_symbol=...)across short sprints was fascinating. Here is the exact evolution of ourint4_barrel_4row kernelfrom 605, 742 cycles down to 114, 534 cycles.

### Sprint 1 (v0.2): The Naive Baseline — 605, 742 cycles (27.7 MOPS)

I started with a straightforward C implementation: unpacking nibbles one by one, subtracting 8, multiplying by x[i], and applying float group scales without hardware FPU enabled. At605, 742 cycles(4, 732.4 us), it was slower than our scalar INT8 baseline (572, 296cycles).

### Sprint 2 (v0.3): Zero-Point Hoisting + int16 Scales — 240, 723 cycles (SRAM) / 271, 492 cycles (RRAM)

The agent's first major mathematical optimization wasZero-Point Hoisting. In a naive loop, subtracting the zero-point 8 from every unpacked weight requires thousands of extra ALU instructions inside the inner loop.

By rewriting the dot product for a 32-element group g:

Since the input vector x is shared across all 256 rows of the matrix, the agent precomputed the group sums:

(and pre-expanded x intoint16x2_tSIMD pairs) once at the start of the layer!

Inside the matrix loop, weights are treated as pure unsigned nibbles

and the zero-point bias is subtracted in a single operation per 32-element group.

Combined with enabling the hardware FPU(CONFIG_FPU=y),int16group scales, and 2-row tiling, cycle count dropped by2.5xto240, 723 cycles!

### Sprint 3 (v0.5): Single-Cycle ARM Barrel-Shifter Unpacking — 179, 573 cycles (SRAM) / 218, 289 cycles (RRAM)

Why is officialarm_fully_connected_s4in CMSIS-NN so slow (427, 794 cycles)? Usingread_fileon the SDK's CMSIS-NN sources, the agent observed that unpacking signed 4-bit nibbles into 16-bit lanes using shifts,ROR #4, and sign-extension instructions (SXTB16/UXTB16) floods the ALU pipeline.

Because I hoisted the zero-point-8out of the loop, nibbles are strictlyunsigned(0..15). That unlocked a killer architectural trick on ARMv8-M:The Single-Cycle Barrel-ShifterAND.

On Cortex-M33, the bitwiseANDinstruction can pass its second register operand through the hardware Barrel Shifter (LSR #n)for free in a single clock cycle! By pre-packing 8 weights (w0..w7) into a 32-bit word with interleaved nibbles and holding the constant maskmask = 0x000F000Fin a register, the agent unpacked8 x 4-bit weights into fourint16x2_tSIMD registers in just 4 clock cycles:

// w32 holds 8 packed 4-bit unsigned weights: [w7, w5, w3, w1 | w6, w4, w2, w0]
// mask = 0x000F000F
uint32_t p0, p1, p2, p3;
__asm__ volatile (
 "and %[p0], %[mask], %[w32] \n\t" // Cycle 1: extracts (w0, w1) as int16x2
 "and %[p1], %[mask], %[w32], lsr #4 \n\t" // Cycle 2: shifts & extracts (w2, w3)
 "and %[p2], %[mask], %[w32], lsr #8 \n\t" // Cycle 3: shifts & extracts (w4, w5)
 "and %[p3], %[mask], %[w32], lsr #12 \n\t" // Cycle 4: shifts & extracts (w6, w7)
 : [p0] "=&r" (p0), [p1] "=&r" (p1), [p2] "=&r" (p2), [p3] "=&r" (p3)
 : [w32] "r" (w32), [mask] "r" (0x000F000F)
);
// Followed immediately by 1-cycle dual 16x16-bit MACs:
acc = __SMLAD(p0, x01, acc);
acc = __SMLAD(p1, x23, acc);
acc = __SMLAD(p2, x45, acc);
acc = __SMLAD(p3, x67, acc);

ZeroUXTB16instructions. Zero separate shift instructions. Combined with 4-row tiling (reusing each loaded activation pair across 4 rows simultaneously), execution time dropped to179, 573 cyclesin SRAM!

### Sprint 4 (v0.6): Eliminating 22 Stack Spills via disassemble_symbol — 130, 480 cycles (SRAM) / 166, 239 cycles (RRAM)

At v0.5, the agent passeddisassemble_symbol="int4_barrel_4row"tobuild_flash_and_profile(). Inspecting theobjdumpoutput revealed a critical bottleneck:GCC had run out of the 14 general-purpose registers (r0..r12, lr) and inserted 22 stack spills (STR/LDR [sp, #imm]) inside the hot inner loop!

To eliminate register pressure, the agent patched the kernel with three surgical changes:

* Collapsed 4 Row Pointers into 1 Base Pointer:Because a row of 256INT4weights is exactly128 bytes, rowsr+1,r+2, andr+3sit at constant byte offsets#128,#256, and#384. Thumb-2LDRinstructions support immediate offsets up to#4095for free (ldr rW, [rBase, #128]), freeing3 registersimmediately.
* In-Place Register Reuse onlsr #12:On the fourth unpack step (and w32, mask, w32, lsr #12),w32is never needed again, so the destination overwritesw32in place, saving a scratch register.
* Full Unrolling ofk=0..3(32 weights):Eliminated the inner loop counter register and branch overhead.

Result:130, 480 cyclesin SRAM (166, 239 in RRAM) — a massive49, 000-cycle reductionpurely from eliminating compiler stack spills!

### Sprint 5 (v0.7 — Final Silicon Record): 64-bit LDRD + FPU Register File Hijacking (VMOV) — 114, 534 cycles (SRAM) / 148, 921 cycles (RRAM)

For the final sprint,gemini-4-argonpulled off two deeply creative micro-architectural optimizations:

* 64-bit Burst Loads (LDRD) Interleaved Across 4 Rows:Instead of issuing 32-bitLDRinstructions, the kernel loads 64 bits (16INT4weights = 8 bytes) at once per row usingLDRDwith immediate offsets (#0, #128, #256, #384), maximizing SRAM/RRAM bus burst efficiency.
* Hijacking Idle FPU Registers (s0..s9) as a 1-Cycle Scratchpad: Unrolling 4 rows with 64-bit LDRD loads required extra registers for outer-loop counters, pointers, and accumulators. Instead of spilling them to SRAM on the stack (which costs 2+ cycles and stalls the Load-Store Unit), the agent realized that the Floating-Point Unit register file (s0..s31) was sitting completely idle during integer SIMD execution!On Cortex-M33F, VMOV sN, rM transfers a 32-bit integer between a general-purpose register and an FPU register in 1 clock cycle without touching the memory bus!
// Spill pointers & outer accumulators into idle FPU registers s0..s9 in 1 cycle!
__asm__ volatile (
 "vmov s0, %[row_acc0] \n\t"
 "vmov s1, %[row_acc1] \n\t"
 "vmov s2, %[row_acc2] \n\t"
 "vmov s3, %[row_acc3] \n\t"
 // ...
 // 64-bit burst loads across 4 rows using a single base pointer (w_ptr):
 "ldrd r4, r5, [%[w_ptr], #0] \n\t" // Row 0: 16 x INT4 weights
 "ldrd r6, r7, [%[w_ptr], #128] \n\t" // Row 1: 16 x INT4 weights
 "ldrd r8, r9, [%[w_ptr], #256] \n\t" // Row 2: 16 x INT4 weights
 "ldrd r10, r11, [%[w_ptr], #384] \n\t" // Row 3: 16 x INT4 weights
 // ... Barrel-shifter AND + SMLAD pipeline ...
);

This pushed our SRAM execution down to114, 534 cycles(894.8 us,146.5 MOPS,0.57 MAC/cycle) and RRAM execution down to148, 921 cycles(1, 163.4 us,112.7 MOPS) — with Verify:PASS!

### Summary of the Agent's Optimization Trajectory (INT4 group_size=32):

### 5. Debunking the T-MAC (LUT) Myth on Cortex-M33

In recent Edge AI literature, table-lookup methods likeT-MAC(which precompute partial sums of activations into a Look-Up Table and replace Multiply-Accumulate with table lookups indexed by 4-bit weight nibbles) have gained huge popularity on desktop/mobile CPUs (ARM Cortex-A with NEONVTBLor x86 AVX2VPSHUFB).

I tested this directly on Cortex-M33 (int4_lut_tmac(SRAM)). For each pair of activations, we precomputed a 256-entry int16_t LUT in zero-wait-state SRAM (indexed by a single packed byte holding two 4-bit weights), and used the packed weight bytes to load the precomputed partial sums viaLDRSH.

The result?int4_lut_tmac(SRAM)took190, 444 cycles— losing toint4_barrel_4row(SRAM)(114, 534 cycles) by66%!

Why does LUT lose to Barrel-Shifter + SMLAD on Cortex-M33?

* No Vector Table Lookup (VTBL):Cortex-M33 implements ARMv8-M Mainline DSP,notHelium (MVE) or NEON. It lacks a register-to-register vector permute/lookup instruction.
* LSU Bottleneck vs. ALU Parallelism:Every LUT lookup requires a scalar memory load (LDRSH) through the Load-Store Unit (LSU) from SRAM. Even in 0-wait-state SRAM, scalar address calculation +LDRSH+ADDsaturates the LSU pipeline. Meanwhile, our Barrel-Shifter kernel loads 16 weights in a single 64-bitLDRDand processes them purely inside the register file using 1-cycleAND (lsr)+ dual-MACSMLAD.

### 6. Final Silicon Benchmarks on Nordic nRF54LM20B (v0.7)

Here is the live UART table captured directly from/dev/ttyACM1on theNordic nRF54LM20B DKrunning at 128 MHz:

### Key Engineering Takeaways:

* 3.74x Faster than Official ARM CMSIS-NNs4:Ourint4_barrel_4row (SRAM)kernel (114, 534 cycles) is3.74x fasterthan ARM's officialarm_fully_connected_s4(427, 794cycles) and2.87x fastereven when running directly out of non-volatile RRAM (148, 921 cycles).
* 4-Bit Finally Beats 8-Bit CMSIS-NN on Cortex-M33 (by up to 1.95x!):Normally, 4-bit kernels are slower than 8-bit kernels on MCUs due to unpacking overhead. Myint4_barrel_4rowis1.95x fasterin SRAM (114, 534 vs 223, 757 cycles) and1.50x fasterdirectly from RRAM (148, 921 vs 223, 757 cycles) than officialarm_fully_connected_s8— while cutting weight memory nearly in half (36 KB vs 64 KB)!
* Hitting 96.6% of the Physical RRAM Bus Ceiling:Notice thatfp32_fpu_hw(256 KBweights) establishes the physical sequential read ceiling of the nRF54LM20B's non-volatile RRAM bus at47.4 MB/s. Our custom 8-bit 4-row SIMD kernel (int8_simd_4row(RRAM)) achieved45.8 MB/s(174, 717 cycles) — saturating96.6%of the physical RRAM bus limit! Because INT8 is completely memory-bound on RRAM (45.8 MB/s), compressing weights toINT4(36 KB) was theonlyphysical way to break through the RRAM bandwidth wall on the CPU and reach 148, 921cycles.
* CPU vs. Axon NPU Synergy:While theAxon NPU(15, 975 cycles, 1, 050.2 MOPS) remains the undisputed king for supportedINT8layers (35.82x speedup), custom block-quantizedINT4(Q4_0)layers, dynamic LLM heads, or ultra-compact models that must fit in tight RRAM/SRAM budgets can now run at146.5 MOPSright on the Cortex-M33F CPU!

### 7. Source code of the Benchmark

https://github.com/maxxlife/cmsis-nn-s4-cortex-m33-benchmark

### 8. What's Next for MCU-Drift?

Proving that a 180-line, token-efficient Hardware-in-the-Loop AI agent can discover non-obvious assembly optimizations (like single-cycle Barrel-Shifter nibble extraction and spilling integer accumulators into idle FPU registers viaVMOV) and beat official vendor libraries by3.74xopens a whole new chapter for TinyML engineering.

Next up on our roadmap forMCU-Drift:

* Expanding the hardware farm by plugging in anESP32-S3(Xtensa LX7 PIE 128-bit SIMD) andRISC-Vtargets to let agent.pysynthesize cross-architecture INT4 kernels automatically.
* Running full end-to-end block-quantized INT4 Transformer / TinyLLM blocks combiningAxon NPU(INT8 compute-heavy layers) +MCU-Drift Barrel-Shifter INT4(memory-bound projection layers).

If you enjoyed this deep dive, drop aRespecton Hackster, check outPart 1 of our nRF54LM20B benchmark series,and let me know in the comments which MCU architecture our HIL agent should conquer next!

#nrf54#zephyr #tinyml #edg-ai

Read more

## Code

### Github repo

## Credits

### Maksim Masalski

11 projects • 37 followers
I am an inventor and software architect with a passion for AI, Physical AI, robotics, embedded devices and innovations using TRIZ approach.
Follow

Contact
Contact

## Comments

##### Related channels and tags

* arm
* embedded
* google
* nrf52