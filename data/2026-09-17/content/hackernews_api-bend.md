---
title: Bend
url: https://bend-lang.com/
site_name: hackernews_api
content_file: hackernews_api-bend
fetched_at: '2026-09-17T21:56:21.540300'
original_url: https://bend-lang.com/
author: nicolas-siplis
date: '2026-09-17'
description: 'Bend: a fast language that blocks AI mistakes via proof.'
tags:
- hackernews
- trending
---

×

### 1.Install

curl -fsSL https://bend-lang.com/install.sh | sh

### 2.Add this to your AGENTS.md

When using Bend:
- run 
`bend guide`
 to learn it
- use 
`LAWS.bend`
 to keep important rules
- run 
`bend PROOF.bend`
 before committing
- parallelize the code whenever possible

### 3.Enjoy bug-free, fast vibe-coded apps!

# Bend

afastlanguage thatblocks AI mistakesviaproof

Cspeed ·CUDAparallelism ·Leanproofs

In the post-AGI economy, humans will eventually stop writing
and reading code, but we still need an ambiguity-free way to
tell the AIs building the world around us what we want done.

Withlaws, our intents can be much more precise than natural
language. Withproofs, we can verify that the AI implemented
our prompts correctly. And afast compilerruns it at speed.

That's Bend - and nothing else.

## 1.Bend runsFAST.

Bend compiles to native code. On one core, it runs nearly as
fast as C. The same binary also runs on sixteen cores, or on
the GPU, running up to a hundred times faster than one core.

Apple M4 Max · lower is better

## 2.Bend compilesFAST.

Bend's type checker is a proof checker, as in Lean and Rocq.
Those can take minutes on a mid-sized codebase. Bend takes a
second at most, so an AI agent can check after every change.

Apple M4 Max · lower is better

## 3.Bend isPARALLEL.

No threads, no locks, no kernels to write. Split the work in
two, and Bend spreads the calls over every core it can find,
then joins them back. Now watch pow2 run on 4,096 GPU cores:

pow2.bend running on the 
GPU

## 4.BendBLOCKSmistakes - with proof

How can youtrustcode you never read? By demanding aproof.
LAWS.bend is where you declare laws. From then on, no AI can
ship one line that breaks them, ever. Watch it guard a game:

Law: winning isimpossible

So far, it works!

New feature:

“Claude, make the board wrap around”

Without LAWS.bend:

Laws broken. AI mistake: 
merged
.

With LAWS.bend:

Laws intact. AI mistake: 
blocked
!

Without LAWS.bend, the bug went live. With LAWS.bend, the AI
had to retry until it built a wall and proved the law holds.
Merging a bug is mathematically impossible: it is atheorem.

LAWS.bend

# LAW: no move sequence leads to victory.

law
 
you_cant_win
:
 
for
 moves: List<Move> 
# any sequence of moves

 board = replay(start(), moves) 
# replayed from the start

 is_won(board) == 
False
{} 
# never leads to victory

PROOF.bend

# PROOF: you_cant_win holds.

def
 
Laws.you_cant_win
(moves):
 
# ... written by the AI

LAWS.bendisAGENTS.mdbacked byproof.“Make no mistakes”is nowtype-checked.

Skeptical? Try breaking the game.

## 5.Get started.

### 5.1.Install

curl -fsSL https://bend-lang.com/install.sh | sh

### 5.2.Tell your agent to use Bend

Add this to yourAGENTS.md:

When using Bend:
- run 
`bend guide`
 to learn it
- use 
`LAWS.bend`
 to keep important rules
- run 
`bend PROOF.bend`
 before committing
- parallelize the code whenever possible

Then, just say: "use Bend"!

### 5.3.Enjoy bug-free, fast vibe-coded apps!

Hints: ask it to writelawsfor whatever should never break,
and toparallelizeeverything you want running fast. Bend is
young: if anything goes wrong, ask it to open an issue. Bend
works best on the back-end, on Linux and on macOS. Enjoy! <3

## 6.References.

Guide:GUIDE.mdis the whole language;bend guideprints it.
Paper:BendTT, an affine dependent type theory, Bend's core.
Paper:BendRT, a parallel runtime for CPUs and GPUs, the VM.

Bend is still evolving. Expect bugs, and pleasereport them.