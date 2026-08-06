---
title: I Recreated Management With AI: 9 Things I Do Differently - DEV Community
url: https://dev.to/anchildress1/i-recreated-management-with-ai-9-things-i-do-differently-3j8g
date: 2026-08-06
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-08-07T06:02:15.817041
---

# I Recreated Management With AI: 9 Things I Do Differently - DEV Community

# I Recreated Management With AI: 9 Things I Do Differently

## Overview
- The author treats AI as a living system rather than a simple tool, letting it handle many management‑like tasks.
- Experiments span Codex, ChatGPT, Claude, Cowork, and Gemini, revealing distinct workflows for each.
- All practices described are personal projects; no production‑critical systems are involved.

## The Org Chart Has One Employee
- AI performs the entire development loop: write code, review it, compare against the live branch, test corrections, and log failures as rules for future runs.
- This self‑reinforcing loop is described as “recreating management” within a single‑person organization.

## Nobody Needs Me Reading Diffs
- Human code review is considered wasteful; AI reviews replace it.
- Two strong, adversarial AI reviews are more likely to catch errors than a tired human reviewer.
- The author focuses on designing systems and validating outcomes, not on line‑by‑line diff inspection.
- Successes include three award‑winning projects (Save the Sun, Carbon Trace, Unearthed) built without manual coding or reviewing.

## 1. Separate AI’s Roles and Permissions
- Permissions are encoded as explicit commands (e.g., “fix all issues. do not commit yet.”) rather than implicit preferences.
- Pushes to the repository are only allowed when explicitly requested, preventing unnecessary GitHub Actions runs and cost overruns.
- The author uses a blacklist‑style safety system: everything is allowed unless specifically forbidden, leading to 134 standing rules that act as a rebuilt safety layer.

## 2. Use AI to Review AI‑Assisted Work
- Multiple AI reviewers (Codex, Copilot, Claude) provide complementary perspectives; disagreements surface hidden issues.
- Example: Codex flagged a frame‑0 rendering problem; Claude argued it was covered. The final fix combined both insights, adding a runtime invariant and passing all tests.
- Effective review requires giving the second reviewer the branch and risk context, not just the first reviewer’s verdict.

## 3. Restart Instead of Repair
- When a model repeatedly fails on the same prompt, the conversation is considered “poisoned”; the author starts a fresh chat with the learned information.
- Modern models (GPT‑5.6, Claude 5) need less hand‑holding; it is faster to discard a broken approach and redesign than to keep iterating on a flawed solution.
- Model selection is made once at the start of a task, minimizing later escalations.