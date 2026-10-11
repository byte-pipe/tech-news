---
title: Humans approve intent, machines prove conformance
url: https://jovidecroock.com/blog/gittifacts
date: 2026-10-12
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-10-12T06:00:52.171661
---

# Humans approve intent, machines prove conformance

# Humans approve intent, machines prove conformance

## Background
- Cloudflare’s “We want you to build the next Git platform” prompt inspired the creation of **gittifacts**, an agent‑native Git platform.
- Traditional software lifecycle (explore → plan → implement → test → monitor) is being compressed by agents; human attention should focus on exploration and decision‑making.

## Core Principle
- **Rule:** *Humans approve intent. Machines prove conformance.*  
- This replaces the pull‑request assumption that a human authored the diff, shifting review to intent and automated evidence.

## Flow Overview
1. **Plan (intent)**
   - An agent drafts a Plan (intent, acceptance criteria, scope).  
   - A human reviews and approves the Plan; reading intent is cheaper than reading diffs.
2. **Change as a fork**
   - `start_change` gives the agent a private fork with a scoped push token.  
   - No shared branches; agents cannot push directly to `main`.  
   - Typical loop: `create_plan → start_change → git push → wait_for_change → get_change_status → request_review`.
3. **Evidence generation**
   - Every push triggers CI plus evidence steps: test failures/passes, coverage, mutation score, API diff, dependency diff, sensitive‑path hits, preview deploy.  
   - Evidence is signed and stored as a Git note attached to the head commit.
4. **Lane classification**
   - A pure function evaluates evidence, policy, and Plan to assign a lane:  
     - **Lane 0 – Auto‑merge** (fully proven, no risk)  
     - **Lane 1 – Quick review** (additive API, moderate size, minor missing evidence)  
     - **Lane 2 – Full review** (breaking API, auth/migrations, scope drift, missing proof)
5. **Walkthrough generation**
   - A reviewer agent creates a risk‑ordered walkthrough referencing evidence; the human never sees the raw diff.
6. **Merge queue**
   - Only the queue writes to `main`.  
   - It batches speculative changes, runs them in parallel, and delegates textual conflicts to a resolver agent.
7. **Rollout & revert**
   - Merged changes are feature‑flagged and rolled out gradually.  
   - On regression, the flag is turned off, the change is rolled back, and a revert Change is opened.

## Confidence Factors
- **Agent claim is input only:** Intent statements are meaningless without supporting evidence.
- **Escalation on unknowns:** Missing or errored signals can only raise the lane; models can only push a change to a stricter review level.
- **Reversibility:** Auto‑merge is safe because each change is behind its own flag and can be undone instantly.
- **Repository‑level trust:** Auto‑merge starts disabled; it is enabled once human reviewers consistently agree with lane decisions.
- **No self‑approval:** Neither humans nor agents may approve their own Plans or Changes; policy is read from the default branch.
- **Git‑native provenance:** Every landed commit includes a signed note (`refs/notes/whynote`) recording intent, approver, agent, lane, and rationale.

## Integrations
- Lanes can hook into existing tools (e.g., CodeRabbit, Greptile) to influence review speed.  
- Feature‑flag services like LaunchDarkly can automate rollout and rollback.

## Development Process
- Specs drove every component (platform, onboarding, merge queue, integrations, docs).  
- Each spec began with a “why this exists” section, followed by milestones with acceptance tests.  
- Decisions were recorded in a growing `DECISIONS.md` (≈ 3,500 lines).  
- Working agreements:
  - Test hierarchy: E2E > integration > unit.  
  - Documentation overrides spec when Cloudflare primitives changed.  
  - Fix platform issues, not prompts; errors surface with actionable fix commands.  
- The platform was self‑hosted: imported its own repo, agents opened six Changes, human reviewers approved, and the queue merged them.