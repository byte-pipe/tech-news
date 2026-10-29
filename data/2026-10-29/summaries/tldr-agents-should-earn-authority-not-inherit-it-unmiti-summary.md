---
title: Agents Should Earn Authority, Not Inherit It | Unmitigated Risk
url: https://unmitigatedrisk.com/2026/10/agents-should-earn-authority-not-inherit-it
date: 2026-10-29
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-10-29T21:01:27.799592
---

# Agents Should Earn Authority, Not Inherit It | Unmitigated Risk

# Agents Should Earn Authority, Not Inherit It | Unmitigated Risk

## Overview
- The author, a software‑systems engineer, argues that safety for autonomous agents is a **design problem**, not merely a policy issue.
- Instead of trying to make a model “behave,” we should focus on **what the model can reach when it does not behave** and enforce authority through **explicit, evidence‑driven capabilities**.

## Core Principles
- **Freedom to act vs. freedom to be authorized**: agents may choose *how* to solve a task, but not *what* they are permitted to touch.
- **Mission‑based authority**: each run is governed by a **mission** that lists resources, operations, limits, and required evidence (milestones).
- **Capability envelope**: a signed, time‑bound permission set that expands only when the agent provides the required evidence.
- **Deterministic reference monitor**: validates proposals against organizational policy, translating intent into concrete capability requests; it never infers permission from natural‑language goals.
- **Independent assessment model**: can suggest narrowing or rejecting a proposal but cannot grant additional authority.

## Illustrative Run (Payments Refund Test)
1. **Initial permission list**  
   - Read payments repo, fetch approved packages, run isolated builds, stage changes.  
   - No production or arbitrary network access.
2. **Mission definition**  
   - Structured description of work, resources, and evidence needed.  
   - Envelope defines maximum authority for this revision.
3. **Diagnosis milestone**  
   - Agent discovers flaky test caused by a vendored helper using real system time.  
   - Recording the diagnosis satisfies the first evidence gate, unlocking isolated build capability.
4. **Diagnostic script execution**  
   - Script attempts to post telemetry; network request is blocked by the broker because no capability for that host exists.  
   - No credentials are exposed; the VM has no direct network route.
5. **Dependency update**  
   - Fix requires a newer time‑mocking library not in the original envelope.  
   - Agent proposes a revised mission; engineer reviews the single‑package change (digest, manifest) and approves.
6. **Build and receipt**  
   - Build service runs tests, returns a signed receipt tied to the candidate.  
   - Receipt unlocks staging capability.
7. **Staging and promotion**  
   - Source‑control broker verifies patch scope, runs secret scan, and records the staged result.  
   - Engineer reviews and approves the exact diff; promotion capability then allows merge.
8. **Audit trail**  
   - All allowed or refused actions (e.g., blocked telemetry post) are logged by brokers, providing a transparent record independent of the model’s judgment.

## Authority Earned Through Evidence
- **Protected intent**: engineer’s request is recorded before any action.
- **Explicit proposal**: agent lists each resource, operation, and required gate (e.g., read repo → initial envelope, run builds → diagnosis recorded, stage patch → passing‑test receipt).
- **Policy enforcement**: reference monitor checks each request against organizational rules; any request beyond policy is rejected or sent for policy change.
- **Capability release**: each successful evidence milestone (diagnosis, build receipt, scan approval) unlocks the next short‑lived capability, keeping the run within its envelope.

## Implications
- Agents operate under **least‑privilege, evidence‑driven** constraints rather than broad inherited rights.
- Safety is achieved by **designing the permission flow**, not by trying to predict every possible model misbehavior.
- Transparent logging and deterministic monitors provide **auditability** and **policy compliance** without relying on the model’s ability to recognize hostile intent.