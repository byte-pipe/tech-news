---
title: HEXAW programming language for WebAssembly instead WAT - DEV Community
url: https://dev.to/pengeszikra/hexaw-a-lazy-wasm-text-format-5g5n
date: 2026-10-25
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-10-29T21:00:36.169258
---

# HEXAW programming language for WebAssembly instead WAT - DEV Community

# Summary of “HEXAW programming language for WebAssembly instead WAT”

## TLDR
- HEXAW is a tiny, human‑first programming language that lets developers write WebAssembly (WASM) directly in an assembler‑style text format.
- It shows hexadecimal byte codes next to mnemonic tokens, helping users understand the low‑level representation of WASM.
- The project includes a CLI, a step‑through debugger, and an AI mentor for byte‑level guidance.

## What Was Built
- An experimental text format for WASM called **HEXAW**, inspired by the author’s experience with Z80 and 8086 assemblers.
- A command‑line interface that can:
  - Assemble `.hexaw` files into `.wasm`.
  - Dump binary files back into readable instructions with hex bytes.
  - Step forward and backward through execution.
  - Provide AI‑driven explanations (via Groq’s `gpt‑oss‑120b` model) when a key is supplied.
- An interactive shell with an SST‑style “Amode” for immediate hex‑byte feedback.

## Demo & Usage
- Install via npm (requires Node 22.18+):
  ```bash
  npm install -g hexaw
  hexaw -i factorial.hexaw
  ```
- Optional Groq API key (`GROQ_API_KEY`) placed in a `.env` file enables AI assistance.
- Alternative: clone the repository, run `npm ci`, then start the shell:
  ```bash
  npm run shell -- factorial.hexaw
  ```
- Inside the shell you can execute commands such as `CALL factorial 5`, `G`, `BACK` to compute and reverse steps.

## Example: Factorial Loop in HEXAW
```text
EXP "factorial" 0
FN 0
  PAR 0 ; n
  RES
  LOC 1 ; result

  CONST 1
  SET 1
  BLOCK
    LOOP
      GET 0
      EQZ
      BRIF 1 ; exit when n = 0

      GET 1
      GET 0
      MUL
      SET 1

      GET 0
      CONST 1
      SUB
      SET 0
      BR 0 ; repeat
    END
  END
  GET 1
END
```
- Default numeric type is `i32`; prefixes `L`, `F`, `D` select `i64`, `f32`, `f64`.
- Dump output aligns bytes with instructions, e.g. `00000032 : 20 00 : GET 0`.

## How It Was Built
- Core written in TypeScript, using a custom fork of the author’s TS+|> CLI framework.
- AI mentor powered by the open‑weight `gpt‑oss‑120b` model accessed through Groq’s API.
- Mentor can answer questions about specific opcodes, showing the current draft, VM state, and recent errors.

## Open Innovation
- HEXAW is released under the MIT license; anyone can modify the language, compiler, or AI teaching material.
- The open‑weight model offers a path to self‑hosting the mentor in the future; currently only the AI component relies on Groq’s hosted service.

## Lazy Payoff
- Eliminates manual byte decoding and context switching between code, docs, and external AI chats.
- Provides a single‑terminal workflow for writing, assembling, debugging, and learning WASM.

## Language Simplicity (Prefixes)
- Default type: `i32`.
- Prefixes:
  - `L` → `i64`
  - `F` → `f32`
  - `D` → `f64`
- Mnemonics contain no numbers, brackets, or special characters unless essential (e.g., `ADD`, `LADD`, `FADD`, `DADD`).

## Comparison with WAT
- WAT (WebAssembly Text) uses heavy parentheses:
  ```wat
  (module
    (func (export "add") (param $first i32) (param $second i32) (result i32)
      local.get $first
      local.get $second
      i32.add))
  ```
- HEXAW offers a flatter, assembler‑like syntax that directly shows the underlying byte codes.