---
title: memdoor/examples/workflows/team-solve at main · guregodevo/memdoor · GitHub
url: https://github.com/guregodevo/memdoor/tree/main/examples/workflows/team-solve
date: 2026-10-31
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-11-01T18:54:10.036949
---

# memdoor/examples/workflows/team-solve at main · guregodevo/memdoor · GitHub

# team‑solve

## Overview
- A **multi‑agent harness** for solving programming problems, implemented as a Memdoor workflow.  
- Roles: **planner, two ideators (A & B), solver, manager**, plus a **repair worker**; each starts with a fresh context and communicates only through files on disk.  
- Success is determined by a shell script that runs the provided samples; no model‑based grading is used.  

## Reported performance
| Pass | Memdoor workflow | Authors’ 27B harness | Fable 5 alone |
|------|------------------|-----------------------|---------------|
| 1 | 10 / 10 | 9 | 7 |
| 2 | 10 / 10 | 10 | 8 |
| 3 | 10 / 10 | 10 | 10 |
| 4 | 10 / 10 | 9 | 8 |
| 5 | 9 / 10 | 10 | 7 |
| **Mean** | **9.8** | **9.6** | **8.0** |

- Tested on the first **10** LiveCodeBench Hard problems, each run **5 passes**.  
- **49 / 50** problems solved; total cost **$35.79** (≈15.3 M output tokens).  
- Median model time **≈ 40 min** per run (longest ≈ 4 h), average cost **$0.39**.  
- Runs executed on **OpenRouter** (hosts: Modal, CoreWeave, Parasail, Wafer).  

### Observed failure modes
1. **Pass 5, abc399_e** – manager generated an incorrect counter‑example; the revised program passed the samples but missed hidden tests.  
2. **Pass 4, arc196_c / arc196_d** – a correct program was overwritten because the manager did not signal completion; later rounds eventually recovered the solution at higher cost.  

Both issues are fixable (e.g., verify manager’s counter‑example with brute‑force on small inputs, retain the last program that passes samples).

## How to run the workflow
```bash
curl -fsSL https://memdoor.ai/install.sh | bash
memdoor connect openrouter   # or anthropic, openai, gemini, local
git clone --depth 1 https://github.com/guregodevo/memdoor
mkdir -p ~/.memdoor/workflows
cp -r memdoor/examples/workflows/team-solve ~/.memdoor/workflows/
mkdir my-problem && cd my-problem
cp -r ../memdoor/examples/workflows/team-solve/sample/* .   # task.md + tests/
memdoor workflow run team-solve --wait   # exits 0 when all samples pass
```
- Replace `task.md` and the paired test files for a new problem.  
- The solution is written to `solution.py` and executed with Python 3 and Bash.  
- The workflow can be used with any supported model (OpenRouter, Ollama, vLLM, etc.).

## Workflow architecture
```
plan ──┬── ideate‑a ──┬── solve ── test ── review ── repair ── verify
       └── ideate‑b ──┘
```

| Step | Kind | Reads | Writes |
|------|------|-------|--------|
| plan | agent | `task.md` | `plan.md`, `notes.md` |
| ideate‑a / ideate‑b | agent (parallel) | `task.md`, `plan.md`, `notes.md` | proposal in its own anchor inside `notes.md` |
| solve | agent | both proposals, `notes.md` | `solution.py` |
| test | command | `tests/` | `test-output.log`, `test-status.txt` |
| review | agent | captured test output | `review.md`, repair instructions in `notes.md` |
| repair | agent | manager’s instructions | fixed `solution.py` (or none if samples already pass) |
| verify | command | `tests/` | `final-test-output.log` (non‑zero exit fails the run) |

- Every agent prompt enforces **fresh context** and **no reliance on prior chat**; the “ledger” (`notes.md`) records decisions and is credited for performance gains.  
- Only **one repair round** is performed; there is no human gate.  
- The final verdict is produced by a command that runs `check‑samples.sh` and exits with the test result.

## First sample result
- Problem: count substrings of a string over `{a,b,c}` with equal counts of each letter (up to 200 k characters).  
- Execution on the default OpenRouter ladder: **all 8 steps completed**, **all 5 samples passed**.