---
title: Relicensing with AI-assisted rewrite - Tuan-Anh Tran
url: https://tuananh.net/2026/03/05/relicensing-with-ai-assisted-rewrite/
date: 2026-03-05
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-03-06T06:02:14.072309
---

# Relicensing with AI-assisted rewrite - Tuan-Anh Tran

# Relicensing with AI-assisted rewrite – Summary

## Disclaimer
- The author is not a lawyer and does not provide legal advice.
- The post is a community‑focused overview of recent events and news.

## Background on relicensing challenges
- Relicensing open‑source projects normally requires unanimous consent from every contributor, which is often impractical for older codebases.
- The Python library **chardet**, a port of Mozilla’s C++ detector, has been bound to the LGPL, creating uncertainty for corporate users.

## AI‑driven rewrite and licensing claim
- Maintainers used Claude Code to rewrite the entire codebase and released version 7.0.0 under the MIT license.
- Original author *a2mark* argues this may violate the LGPL because:
  - The rewrite was not a “clean‑room” effort; the AI was prompted with the original LGPL code.
  - Exposure to the original code means the AI output could be a derivative work, which must stay LGPL.

## Clean‑room rewrite requirements and AI bypass
- Traditional clean‑room process involves:
  1. Team A creates a functional specification from the original code.
  2. Team B, never having seen the original, writes new code based solely on that specification.
- Using an AI trained on the LGPL code bypasses the separation wall, potentially producing derivative work.

## Supreme Court decision and the resulting paradox
- On March 2, 2026, the U.S. Supreme Court declined to hear an appeal on AI‑generated copyright, reinforcing a “human authorship” requirement.
- This creates three intertwined issues for the chardet maintainers:
  - **Copyright vacuum**: If AI‑generated code cannot be copyrighted, the maintainers may lack authority to license it under MIT.
  - **Derivative trap**: If the AI output is deemed a derivative of LGPL code, the MIT relicensing breaches the original license.
  - **Ownership void**: If the code is considered a wholly new machine‑generated work, it may fall into the public domain immediately, making any license moot.

## Potential impact on copyleft
- Accepting AI‑rewriting as a legitimate relicensing method could undermine copyleft protections.
- Developers might feed GPL‑licensed projects into LLMs with prompts to “rewrite in a different style” and re‑release under permissive licenses like MIT.
- The chardet v7.0.0 case is among the first real‑world tests of these emerging legal and ethical boundaries.