---
title: "Reversing Factorio's RNG"
url: https://gegell.github.io/posts/factorio-rng/
date: 2026-09-13
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-18T05:28:42.097327
---

# Reversing Factorio's RNG

# Reversing Factorio's RNG

## Introduction
- Factorio’s Space‑Age DLC adds quality modules that give a chance for higher‑quality items and buildings.
- Quality distribution follows expected statistical odds, but players seek deterministic ways to obtain the best quality.
- The game uses a pseudo‑random number generator (PRNG), which is deterministic despite appearing random.

## How the RNG Works
- Factorio employs the **taus88** generator, a combination of three linear feedback shift registers (LFSRs) whose outputs are XORed.
- Original implementation (Boost.Random) defines three LFSRs with specific parameters; the compiled game code shows optimized constants but retains the three‑seed structure.
- Verification was done by reproducing both the Boost version and the decompiled version in Python (using SymPy) and confirming bit‑wise equivalence.

## Impact of Factorio 2.1
- Version 2.1 changes the way RNG is accessed, breaking existing in‑game implementations that relied on the previous behavior.
- The underlying PRNG algorithm (taus88) remains unchanged, so theoretical analysis still applies.

## Exploiting the Weakness
- LFSRs are known to be weak and trivially breakable; knowing the algorithm and internal state allows exact prediction of future outputs.
- By synchronizing an external copy of the PRNG with the game’s state, one can forecast which crafting events will yield higher‑quality items.

## Methodology Summary
- **Research**: Started with community forum posts; identified taus88 as the chosen generator (Cube, former Wube developer, 2014).
- **Binary Analysis**: Used Ghidra (with Binary Ninja) to locate `RandomGenerator::getInt` and extract seed manipulation logic.
- **Verification**: Implemented both the Boost and decompiled versions in Python; used symbolic computation to prove equivalence.
- **Conclusion**: Factorio’s RNG is deterministic taus88, making it predictable once the three seed values are known.