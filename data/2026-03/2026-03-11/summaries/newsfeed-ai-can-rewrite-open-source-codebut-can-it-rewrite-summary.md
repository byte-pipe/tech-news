---
title: AI can rewrite open source code—but can it rewrite the license, too? - Ars Technica
url: https://arstechnica.com/ai/2026/03/ai-can-rewrite-open-source-code-but-can-it-rewrite-the-license-too/
date: 2026-03-10
site: newsfeed
model: gpt-oss:120b-cloud
summarized_at: 2026-03-11T13:14:07.268627
---

# AI can rewrite open source code—but can it rewrite the license, too? - Ars Technica

# AI can rewrite open source code—but can it rewrite the license, too? – Ars Technica

## Background
- Reverse engineering has traditionally been used to recreate program functionality without copying protected code (“clean‑room” approach).
- AI coding tools now challenge how clean‑room rewrites are performed legally, ethically, and practically.

## The chardet case
- **Original project**: chardet, a Python library for character‑encoding detection, created by Mark Pilgrim in 2006 under the LGPL.
- **New version**: Dan Blanchard released chardet 7.0, claiming a “ground‑up, MIT‑licensed rewrite” generated with Claude Code, achieving a 48× speed boost.
- **Controversy**: Pilgrim argues the rewrite is not a true clean‑room effort; he sees it as an illegitimate relicensing of his LGPL code to the permissive MIT license.

## Arguments from both sides
- **Pilgrim’s stance**
  - Blanchard had “extensive exposure” to the original code, violating the separation required for clean‑room work.
  - The rewrite still derives from the LGPL‑licensed code and must retain that license.
- **Blanchard’s defense**
  - Claims the AI‑generated code is “qualitatively different” and “structurally independent,” with only 1.29 % similarity to prior versions (vs. up to 80 % similarity between older releases).
  - Used a “wipe it clean” commit and a fresh repository, providing Claude with a design document and explicit instructions not to copy LGPL code.
  - Performed extensive human review, testing, and iteration, though he acknowledges deep familiarity with the original project.

## Complicating factors
- Claude relied on metadata from earlier chardet releases, raising questions about derivative status.
- The model’s training data likely includes previous chardet code, making it unclear whether the output is a derivative work.
- Human involvement in reviewing and iterating on AI‑generated code may affect the derivative analysis.

## Community reaction
- **Legal uncertainty**: FSF’s Zoë Kooyman says large language models that have ingested the original code cannot be considered “clean.”
- **Philosophical view**: Developer Armin Ronacher likens the situation to the Ship of Theseus—if all code is replaced, it may be a new work.
- **Broader implications**: Courts have not yet ruled on authorship or licensing of AI‑generated software, leaving the legal landscape unsettled.

## Potential impact on open‑source ecosystem
- AI can dramatically lower the effort required to rewrite and relicense projects, possibly reshaping software development economics.
- Opinions range from seeing this as a transformative shift (e.g., Bruce Perenstold’s “economics of software development are dead”) to advocating for new mental models to adapt (Salvatore “antirez” Sanfilippo).

## Outlook
- The legal status of AI‑generated code remains ambiguous, and future court decisions will likely shape how open‑source licenses are applied to such works.
- Regardless of legal outcomes, the ability to rapidly reimplement and relicense code with AI is poised to have significant, lasting effects on the open‑source community.