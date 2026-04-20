---
title: "I'm Building Agents That Run While I Sleep"
url: https://www.claudecodecamp.com/p/i-m-building-agents-that-run-while-i-sleep
date: 2026-03-10
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-11T13:13:37.850651
---

# I'm Building Agents That Run While I Sleep

# I'm Building Agents That Run While I Sleep

## Problem Statement
- I have agents (e.g., Claude Code) that write and ship code automatically, often while I’m asleep.
- Changes land in branches I haven’t read, and I lack a reliable way to know whether the code actually meets the intended requirements.
- As autonomous systems scale, traditional code review becomes impractical; we end up watching deployments and hoping nothing breaks.

## Why the Obvious Answers Don’t Work
- Hiring more reviewers is too slow and costly; senior engineers cannot spend all day reviewing AI‑generated code.
- Having Claude write tests for its own code only verifies Claude’s interpretation, not the real specification.
- Using one AI to write and another to check creates a “self‑congratulation” loop rather than an independent second set of eyes.

## What TDD Got Right
- Test‑Driven Development (TDD) forces you to describe the correct behavior before code is written.
- With AI handling speed, the bottleneck shifts to verifying correctness, which TDD already addresses.
- Writing acceptance criteria in plain English lets the agent generate code, then a separate process checks it.

## Practical Implementation
- **Frontend:** Generate acceptance criteria (AC) from a spec file, then run Playwright agents against each AC. Each agent reports pass/fail with screenshots and logs.
- **Backend:** Use observable API behavior (status codes, headers, error messages) and validate with curl commands.
- The workflow: write AC → prompt the agent → run verification → review only the failures.
- Limitations: if the original spec is wrong, the checks will still pass; the method catches integration and UI bugs but not specification misunderstandings.

## How to Build It
1. **Pre‑flight (bash):** Ensure dev server, auth session, and spec file exist; fail fast.
2. **Planner (Opus call):** Reads the spec and changed files, decides needed checks, extracts selectors from code.
3. **Browser agents (Sonnet calls):** One parallel agent per AC performs navigation, interaction, and screenshotting.
4. **Judge (Opus call):** Consumes all evidence JSON and returns a verdict per AC (`pass`, `fail`, `needs‑human‑review`).

- Implemented as a Claude Skill (`ops lane/verify`) that runs in Claude’s headless mode with Playwright.
- Install via Claude Code plugin marketplace or clone the repo and adapt.
- Each stage is a single Claude call with clear input and structured JSON output, making it easy to swap models or integrate into CI pipelines.

## Takeaways
- You can only trust an agent’s output if you define “done” before it starts.
- Writing acceptance criteria is harder than writing a prompt but forces you to think through edge cases early.
- Without explicit criteria, you’re left reading output and hoping it’s correct.
- The approach reduces review effort to only the failing cases, offering a scalable alternative to traditional code review as AI‑generated code becomes more prevalent.
