---
title: Qwenputer: a fully functioning, deterministic RISC-V CPU inside Qwen3.5 - Divyansh Agrawal
url: https://divagr.com/blog/qwenputer
date: 2026-10-29
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-10-29T21:01:32.324116
---

# Qwenputer: a fully functioning, deterministic RISC-V CPU inside Qwen3.5 - Divyansh Agrawal

# Qwenputer: a deterministic RISC‑V CPU inside Qwen 3.5  

## Overview  
- Qwenputer augments the stock Qwen 3.5 4B model with a fully functional 32‑bit RISC‑V core that runs entirely inside the model’s forward passes.  
- The CPU uses the model’s Gated DeltaNet (GDN) attention heads as exact, addressable RAM, eliminating the need for external runtimes or tool calls.  
- It can execute arithmetic, C, and MicroPython code, and includes an experimental in‑model file system.  

## Gated DeltaNet as exact RAM  
- Three of the four attention layers in Qwen 3.5 employ GDN, a linear RNN whose state matrix serves as memory.  
- By fixing the gate to 1 and the write strength β to 1, each write overwrites a single row of the state matrix, and a one‑hot key retrieves that row unchanged.  
- This makes GDN heads behave like low‑cost, fixed‑size RAM, unlike conventional KV‑cache attention that grows with context length.  

## Compiling the CPU into model weights  
- A compiler translates a description of the RV32IM core (including Zba extension and a small bignum unit) into transformer weights:  
  - Attention heads perform address look‑ups.  
  - Feed‑forward layers carry out arithmetic.  
  - GDN heads store registers, program counter, and memory.  
- Each instruction is emitted as a short token sequence (ADDR, VAL, STEP), forming the CPU’s execution trace during generation.  

## Integration with Qwen 3.5  
- The CPU is invoked through the model’s familiar tool‑call format; no external calls or runtimes are required.  
- A driver called **RvChat** loads the compiled firmware into the GDN state, keeping the trace tokens separate from the language model layers.  
- The original Qwen weights remain unchanged; the computer’s weights are added as extra dimensions and layers (11 layers in front of the model’s 32).  

## Performance and correctness  
- The CPU passes the official RISC‑V test suite and matches QEMU outputs over 18 million free‑running instructions with zero errors.  
- Arithmetic benchmarks:  

  - DeepMind div_big: 97.5 % (vs. 95 % with a Python tool, 72.5 % base).  
  - DeepMind mul_big: 97.5 % (vs. 100 % with a Python tool, 55 % base).  
  - mul_div_multiple_longer: 100 % (vs. 97.5 % tool, 90 % base).  
  - add_or_sub_big: 97.5 % (same as tool, 87.5 % base).  
  - NUPA long‑integer arithmetic: 100 % (vs. 48.6 % base, same as tool).  

- A replay of ~230 k output tokens against a reference machine showed no mismatches.  
- Language generation quality remains essentially unchanged (KL divergence ≈ 6 × 10⁻⁴, near the noise floor).  

## In‑model filesystem  
- Utilizes the same GDN RAM to implement a simple directory of 1 024 slots and up to 512 files (≈ 53 000 tokens of text).  
- Files are stored as chained rows (8 tokens per row); collisions are resolved by linear probing.  
- The filesystem persists across conversations: saved state can be reloaded, enabling fact recall that improves from ~30 % (plain paste) to ~90 % when using the built‑in storage.  

## Availability  
- Model checkpoints are hosted on Hugging Face and ModelScope.  
- Source code, including the compiler and RvChat driver, is released on GitHub.