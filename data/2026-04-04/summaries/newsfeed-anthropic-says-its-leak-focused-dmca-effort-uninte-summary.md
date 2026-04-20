---
title: Anthropic says its leak-focused DMCA effort unintentionally hit legit GitHub forks - Ars Technica
url: https://arstechnica.com/ai/2026/04/anthropic-says-its-leak-focused-dmca-effort-unintentionally-hit-legit-github-forks/
date: 2026-04-02
site: newsfeed
model: gpt-oss:120b-cloud
summarized_at: 2026-04-04T01:03:11.591996
---

# Anthropic says its leak-focused DMCA effort unintentionally hit legit GitHub forks - Ars Technica

# Anthropic’s DMCA takedown of Claude Code leak unintentionally hit legitimate GitHub forks

## Incident overview
- Anthropic issued a DMCA notice to GitHub targeting a repository that contained the leaked Claude Code client source posted by user **nirholas**.
- The notice listed about 96 specific fork URLs, but GitHub’s automated processing also removed roughly **8,100** forks that were part of the same fork network.
- Many of those forks were of Anthropic’s **official public Claude Code repository**, which is meant for community bug reports and improvements.

## Reaction and correction
- Developers publicly complained on social media about being caught in the “DMCA dragnet” despite not hosting leaked code.
- Anthropic’s head of Claude Code, **Boris Cherny**, and legal lead **Thariq Shihi** described the broad takedown as a “communication mistake” and “not intentional.”
- Anthropic asked GitHub to limit the takedown to the 96 listed forks and to restore the other repositories; GitHub complied and reinstated access.

## Ongoing challenges
- **Persistence of the leak:** Copies of the leaked source remain searchable on GitHub and on platforms outside U.S. DMCA jurisdiction, such as Germany‑based **Codeberg**.
- **Clean‑room reimplementations:** Developers have used AI coding tools to rewrite the leaked TypeScript code in languages like Python and Rust, creating functionally similar but potentially legally distinct versions.
- **AI‑generated code complications:** Cherny admitted that recent contributions to Claude Code were written entirely by Claude Code itself, raising questions about copyright protection for AI‑generated versus AI‑assisted code.

## Legal and practical implications
- Even if Anthropic could remove every copy of the original leaked code, the existence of clean‑room rewrites may limit the effectiveness of copyright enforcement.
- The case highlights the difficulty of using DMCA takedowns to control the spread of source code once it has been publicly released, especially when AI tools can rapidly produce derivative implementations.
