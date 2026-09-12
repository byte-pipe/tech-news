---
title: "Astra for Coding: Why Are We Doing This Again? | Armin Ronacher's Thoughts and Writings"
url: https://lucumr.pocoo.org/2026/9/7/astra-why/
date: 2026-09-13
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-13T02:06:56.911405
---

# Astra for Coding: Why Are We Doing This Again? | Armin Ronacher's Thoughts and Writings

# Astra for Coding: Why Are We Doing This Again?

## Overview
- The author compares the current AI engineering climate to “Neijuan” (involution), where effort increases without real productivity gains.
- GPT‑6 Astra is technically impressive: strong at computer use, image understanding, and long‑running tasks, but its utility for software engineering remains unclear.

## The “Slop Factory” Experiment
- Set up an autonomous software factory letting Astra manage workflow, context, and sub‑agents.
- Spent roughly 4 billion tokens (≈35 hours) but the output was largely useless for real development.
- Produced abundant code and prompts, revealing unusual behavior not seen in earlier OpenAI models.
- Suspects a training imbalance: Astra is rewarded for completing long‑horizon tasks but not penalized for generating low‑quality code, leading to prolific but messy outputs (e.g., impressive reverse‑engineering of a robot vacuum).

## Code Generation Style Issues
- Unlike previous models that favored simple bash tool calls, Astra heavily relies on on‑the‑fly Python snippets, even within non‑Python codebases.
- This manifests as extensive manual string manipulation of source files rather than using dedicated patch tools.
- Example shown: a series of Python scripts that read, edit, and rewrite C and header files for CPython development, illustrating the model’s preference for verbose Python‑based patching.

## Implications
- Astra’s strengths lie in generating large amounts of code and exploring complex domains, but its lack of disciplined output hampers practical software engineering.
- The author highlights the need for better reward signals during training to discourage “shitty code” and to encourage cleaner, tool‑aware programming patterns.