---
title: RISC-V: They Should Have Known Better - Dmitry.GR
url: https://dmitry.gr/?r=06.%20Thoughts&proj=12.%20RV
date: 2026-08-14
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-16T06:01:57.639899
---

# RISC-V: They Should Have Known Better - Dmitry.GR

# RISC‑V: They Should Have Known Better – Summary

## Everything for Everyone
- The author believes RISC‑V will eventually dominate cheap, single‑use microcontrollers, not because of its ISA but despite its shortcomings.
- No ISA can be optimal for both high‑end CPUs and tiny microcontrollers; the requirements are fundamentally different.
- Cheap microcontrollers need:
  - Low interrupt latency
  - Small silicon area
  - High code density (small ROM/RAM)
  - Minimal arithmetic hardware (no dividers/multipliers)
  - No privilege separation
- The closest RISC‑V core (RV32IC / RV32EC) still lacks essential features:
  - Without the `Zicsr` extension there is no standard way to handle interrupts.
  - Interrupt entry/exit requires many CSR accesses, leading to ~44 cycles overhead versus 27 cycles for Cortex‑M0.
  - Even RV32E, with fewer registers, still incurs ~38 cycles, still slower than Cortex‑M0.
- Vendors must add proprietary extensions (e.g., CLIC, fast‑IRQ) to match Cortex‑M0 performance, fragmenting the ecosystem.

## Optionality
- (Section not included in the excerpt; omitted from summary.)

## Missing Obvious Pieces
- The compressed (C) extension’s load/store instructions have extremely limited offset ranges:
  - Byte store: offset 0‑3 bytes
  - Half‑word store: offset 0‑2 bytes
  - Word store: offset 0‑124 bytes
- Compared to Cortex‑M0’s offsets (0‑31 for bytes, 0‑62 for half‑words, 0‑124 for words), RISC‑V’s ranges are inadequate.
- These limited‑range instructions reside in the `Zcb` extension, which may not be implemented, further reducing usefulness.
- Using full‑size instructions to gain larger offsets defeats the purpose of the C‑extension’s density advantage.

## Ridiculous Encoding
- The encoding choices for the C‑extension appear arbitrary; bits that could extend offset ranges are hard‑wired to zero.
- This results in poorer code density for common memory‑access patterns on small cores.

## Alleged Fixes
- (Section not included in the excerpt; omitted from summary.)

## How Did We Get Here and Where to Now?
- (Section not included in the excerpt; omitted from summary.)

## Does This Mean RISC‑V is Doomed?
- (Section not included in the excerpt; omitted from summary.)

## Comments…
- (Section not included in the excerpt; omitted from summary.)

## Additional Observations (partial)
- For server‑class cores, raw throughput and out‑of‑order execution dominate; the author begins to discuss this but the excerpt ends before detailed arguments are presented.