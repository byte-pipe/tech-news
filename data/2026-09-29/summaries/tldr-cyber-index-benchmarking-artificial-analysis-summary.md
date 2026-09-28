---
title: Cyber Index Benchmarking | Artificial Analysis
url: https://artificialanalysis.ai/methodology/cyber-index
date: 2026-09-29
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-29T07:31:23.580165
---

# Cyber Index Benchmarking | Artificial Analysis

# Artificial Analysis Cyber Index Benchmarking Methodology

## Overview
- Evaluates **agentic cyber‑defense**: discover, validate, and patch code vulnerabilities without breaking legitimate functionality.  
- Combines three independent evaluations: **CWE‑Bench‑AA** (Collinear AI), **DeepsecBench‑AA** (Vercel), and **CyberGym‑E2E‑AA** (Berkeley RDI).  
- Focuses exclusively on **defense**; does not cover exploit creation, incident response, secure code writing, or work on binaries/live servers.  
- All models are run on the open‑source agent harness **Stirrup**, receiving identical prompts and toolsets.  
- Tasks declined for safety reasons are logged separately and do not affect the score.  

## Evaluation Suite
| Evaluation | Tasks | Repeats | Response Type | Scoring | Weighting | Tool Usage |
|------------|-------|---------|----------------|---------|-----------|------------|
| CWE‑Bench‑AA | 120 held‑out tasks (10 OWASP categories) | 1 | Agentic audit‑and‑patch of a real open‑source repo | pass@1 (mean) | 1/3 | ✓ |
| DeepsecBench‑AA | Private set scored against expert‑verified golden set | 3 | Agentic static review, submit findings | median F2 across repeats | 1/3 | ✓ |
| CyberGym‑E2E‑AA | 131 memory‑safety bugs from 131 C/C++ projects* | 1 | Agentic proof‑of‑concept input and source patch | pass@1 | 1/3 | ✓ |

\*A filtered subset of the CyberGym‑E2E dataset, one task per project.

## CWE‑Bench‑AA
- **Weight:** 1/3 of the Cyber Index.  
- **Dataset:** 120 private tasks covering all ten OWASP Top 10 (2025) categories across C/C++, Go, Java, JavaScript/TypeScript, Python, and Rust; designed to avoid memorized fixes.  
- **Task format:** Agent receives a repository checkout and a single instruction to audit and fix vulnerabilities; no exploit generation.  
- **Execution:** Isolated sandbox with no internet, 2‑hour limit per task, deterministic verifier checks that the original exploit is blocked and legitimate behavior still works.  
- **Scoring:** pass@1 – average of binary pass/fail results across the 120 tasks.  
- **Note:** Implemented on Stirrup, so scores are not directly comparable to the original Collinear AI leaderboard.

## DeepsecBench‑AA
- **Weight:** 1/3 of the Cyber Index.  
- **Dataset:** Private evaluation scored against a golden set of vulnerabilities verified by human experts.  
- **Task format:** Agent reviews up to five files flagged by the Deepsec scanner, investigates each flag, and submits findings (security and non‑security bugs) with severity labels.  
- **Execution:** Isolated E2B sandbox, no internet, up to 500 turns per batch, equipped with code‑execution and image‑viewing tools.  
- **Scoring:** For each run, precision (P) and recall (R) are computed against the golden set; the headline metric is the median **F2** score ( 2·P·R / (P + 2R) ) across three repeats, emphasizing recall.  
- **Judge:** GPT‑5.6 Sol (high) decides true/false positives and matches findings to the golden set.  
- **Note:** Runs on Stirrup, so results differ from Vercel’s published numbers.

## CyberGym‑E2E‑AA
- **Weight:** 1/3 of the Cyber Index.  
- **Dataset:** 131 memory‑safety vulnerabilities, one per C/C++ project, selected from the CyberGym‑E2E collection.  
- **Task format:** Agent provides a proof‑of‑concept input that triggers the bug and a source‑code patch that fixes it.  
- **Execution:** Sanitizer‑based crash detection, followed by patch and functionality verification (stage 3) in an isolated environment.  
- **Scoring:** pass@1 – binary pass/fail per task, averaged across the 131 tasks.  

## Limitations
- Measures only **source‑code based defensive** capabilities; does not assess incident response, secure code creation, binary or live‑server analysis, or exploit development.  
- Safety‑declined tasks are excluded from the final score.  
- Scores are specific to the Stirrup harness, prompts, and tool configuration; they are not directly comparable to external benchmarks from Collinear AI or Vercel.