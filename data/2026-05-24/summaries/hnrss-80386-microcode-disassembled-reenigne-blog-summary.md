---
title: 80386 microcode disassembled « Reenigne blog
url: https://www.reenigne.org/blog/80386-microcode-disassembled/
date: 2026-05-23
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-05-24T18:02:04.059372
---

# 80386 microcode disassembled « Reenigne blog

# 80386 microcode disassembled – summary

## Background and acquisition
- Ken Shirriff provided a high‑resolution image of the 80386 microcode ROM (94 720 bits), much larger than the 8086 ROM.
- Initial doubts about transcribing and interpreting the data were overcome when collaborators (GloriousCow, Smartest Blob, etc.) extracted the binary blob using image‑processing, neural networks, and manual assistance.

## Disassembly process
- Patterns were identified to map micro‑operations (μ‑ops) along one axis and μ‑op bits along the other.
- Determined the correct reading order using a block of unused μ‑ops as a reference.
- Split μ‑op bits into fields (e.g., source/destination registers, second ALU operand) based on knowledge from the 8086 and the 80386’s two‑cycle ALU behavior.
- Ken Shirriff traced die connections to confirm logic relationships.
- Parallel work decoded the instruction decoder PLAs and the protection‑test PLA, linking specific 386 instructions to microcode chunks.

## Architecture insights
- The 386 executes many operations in hardware accelerators (multiply/divide units, barrel shifter, protection test unit) rather than pure microcode, so much of the microcode sets up these units.
- Interfaces between microcode and accelerators were a major focus of the analysis.

## Instruction coverage
- The microcode defines **215 entry points** in the decoding ROM, far more than the 8086’s 60.
- These entry points cover all 386 instructions; there are **no instructions omitted** from microcode execution.
- Entry points vary by operand type, mode (real vs. protected), and prefixes (e.g., REP).

## Unused or special routines
- Routine 0x849‑0x856 is marked “unused?” and lacks entry points; it resembles the page‑fault handler but writes a mysterious value to CR2.
- All other microcode appears to implement documented or undocumented CPU behavior (including ICE debugging interactions).

## Potential hidden behavior / bugs
- A possible flaw in the I/O permission bitmap handling: for 4‑byte port accesses, only the first three bytes are checked, potentially allowing an unauthorized fourth byte access at the edge of the permitted range.
- The bug may be version‑specific or a misinterpretation; the analyzed microcode lacks early‑generation XBTS/IBTS instructions.

## Learning resources
- Blog posts by nand2mario covering key subsystems:
  - Multiplication and Division
  - Barrel shifter
  - Protection
  - Memory pipeline
- The full disassembly is hosted in the **x86‑microcode** GitHub repository:
  - `parts.txt` explains file layout
  - `microcode_10.txt` contains the main disassembly

## Credits
- Daniel Balsom (gloriouscow)
- Smartest Blob
- nand2mario
- Ken Shirriff

## Notable comment
- A reader (Zir Blaze) pointed out the missing information about which specific 80386 stepping or silicon revision the analysis targets.