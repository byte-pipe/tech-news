---
title: HEXAW programming language for WebAssembly instead WAT - DEV Community
url: https://dev.to/pengeszikra/hexaw-a-lazy-wasm-text-format-5g5n
site_name: devto
content_file: devto-hexaw-programming-language-for-webassembly-instead
fetched_at: '2026-10-29T20:59:57.868982'
original_url: https://dev.to/pengeszikra/hexaw-a-lazy-wasm-text-format-5g5n
author: Peter Vivo
date: '2026-10-25'
description: 'This is a submission for the Hacktoberfest Open-Source AI Challenge Week 3: Slow and Steady ... Tagged with devchallenge, hf26challenge, webassembly.'
tags: '#devchallenge, #hf26challenge, #webassembly'
---

Hacktoberfest Open-Source AI Challenge Week 3: Slow and Steady Submission 🦥

This is a submission for theHacktoberfest Open-Source AI Challenge Week 3: Slow and Steady

## TLDR;

With Cat Coding - my old cat Pitypang press the final enter as the documentary video show below.

HEXAW: a tiny time machine for WebAssembly, because hexaw is a brand new programming language for WASM binary based on my previous Z80, 8086 assembler experience. Hexaw is human first programming language, clients is every programmer, who is try to solve any problem in browser by WASM directly, by hand as we programming long time before. The shell program main goal you can see the hexadecimal code next to the assembler tokens. This is a great starting point to deeply understand what going under the hood in WASM word.

## What I Built

I once wrote a Z80 game on a Videoton TV Computer. I still miss typing an instruction and seeing the exact bytes it becomes.As I wrote in this old post

WebAssembly brought back the possibility. WAT brought me a parenthesis jungle. My brain wanted an assembler listing.

So I started buildingHEXAW: a new, experimental text format for WASM, with readable mnemonics and a retro assembler feeling.

It is still totally beta.The syntax and tooling are evolving. Expect rough edges.

The CLI can assemble HEXAW into.wasm, dump binaries back into readable instructions, and step through code forwards and backwards. There is also an AI mentor you can ask when the bytes stop making sense.

## Demo

HEXAW is also on npm. You’ll needNode.js 22.18 or later. Save the example below asfactorial.hexaw, then:

npm 
install
 
-g
 hexaw
hexaw 
-i
 factorial.hexaw

Enter fullscreen mode

Exit fullscreen mode

The AI mentor needs aGroq API key. Put it in a.envfile in your working directory:

GROQ_API_KEY=your_groq_api_key

Enter fullscreen mode

Exit fullscreen mode

Load that file explicitly when starting the shell. On Linux/macOS:

node 
--env-file
=
.env 
"
$(
command
 
-v
 hexaw
)
"
 
-i
 factorial.hexaw

Enter fullscreen mode

Exit fullscreen mode

Without a key, assembling, dumping, and debugging still work. Only the LLM help needs it.

## or clone the repo

Clone therepository, runnpm ci, and save the example below asfactorial.hexawin the repository folder. Then:

npm run shell 
--
 factorial.hexaw

Enter fullscreen mode

Exit fullscreen mode

Inside the shell:

CALL factorial 5
G
BACK

Enter fullscreen mode

Exit fullscreen mode

That computes5! = 120, then reverses the last execution step.

The shell also has an SST-inspiredAmode: type an instruction, press Enter, see its hex bytes, and continue at the next address. An empty Enter applies the completed draft.

## Code

Here is the factorial loop:

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
 BRIF 1 ; leave the outer block when n = 0

 GET 1
 GET 0
 MUL
 SET 1

 GET 0
 CONST 1
 SUB
 SET 0
 BR 0 ; repeat the loop
 END
 END
 GET 1
END

Enter fullscreen mode

Exit fullscreen mode

The default numeric type isi32. PrefixesL,F, andDselecti64,f32, andf64. This is still WASM: a typed stack, locals, and structured control flow.

The dump keeps the bytes beside the instructions:

00000032 : 20 00 : GET 0
00000034 : 45 : EQZ
00000035 : 0D 01 : BRIF 1

Enter fullscreen mode

Exit fullscreen mode

Source:https://github.com/Pengeszikra/hexaw

## How I Built It

I built it with Codex, using myTS+|> TypeScript forkfor the CLI and a shared assembly/debugging engine.

The mentor uses the open-weightgpt-oss-120bmodel through Groq, carried over from myTerminal Is Your Friendproject. Its teaching material now focuses on HEXAW and WASM, grounded in the actual opcode table and a limited snapshot of the current code, assembly draft, VM state, and recent errors.

WithGROQ_API_KEYset before starting the shell, I can ask:

// What does BRIF 1 mean here?
AI ERROR

Enter fullscreen mode

Exit fullscreen mode

The reply arrives while I keep working. Suggested code stays an example until I enter it myself.

## Why Does Open Innovation Matter?

I can change the language, the compiler fork, and the mentor’s teaching material. Anyone else can too: HEXAW is MIT-licensed.

An open-weight model leaves a future route to self-hosting. Today the mentor uses Groq’s hosted API; the assembler and debugger work locally.

## The Lazy Payoff

Less manual byte decoding. Fewer trips between code, documentation, and a separate AI chat.

Apparently I am lazy enough to want all of that in one terminal. Just not lazy enough to leave assembly alone.

## Prefix for simplicity

How I can simplify this language with prefixes?My intentionally simple:

Default type is i32Prefixes:L = i64 (long)F = f32 (float)D = f64 (double)So:

ADD → i32.addLADD → i64.addFADD → f32.addDADD → f64.addNo numbers in mnemonics.No brackets.No special characters unless absolutely needed.

## finnally the craziest language: WAT

Let's look this really basic example:

for brace lovers only!

(module
 (func (export "add") (param $first i32) (param $second i32) (result i32)
 ;; Push the $first and $second parameter value on to the stack
 local.get $first
 local.get $second

 ;; Pops the last two items off the stack, add them together, and
 ;; pushes the result onto the stack
 i32.add
 )
)

Enter fullscreen mode

Exit fullscreen mode

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (12 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse