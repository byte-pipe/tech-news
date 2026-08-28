---
title: Audit your Agent files - by Addy Osmani - Elevate
url: https://addyo.substack.com/p/audit-your-agent-files
date: 2026-08-29
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-29T01:33:10.865391
---

# Audit your Agent files - by Addy Osmani - Elevate

# Audit your Agent files

## TL;DR
- Agent configurations degrade over time as models, harnesses, and codebases evolve.  
- Periodic pruning (e.g., running Claude’s `/doctor`) and re‑evaluating each instruction keeps agents effective.  
- Over‑long `CLAUDE.md`, `AGENTS.md`, and skill files add token cost, cause “configuration smell,” and can reduce performance.

## The core agent loop
- Every agent follows the same cycle: call the model → run a tool → feed the result back → repeat.  
- Production readiness comes from added layers: state, memory, and a harness that orchestrates them.  
- Oracle’s three‑level breakdown (minimal loop → memory‑aware engine → full system harness) is illustrated with runnable notebooks.

## Guidance on pruning
- Official advice: delete and rebuild `CLAUDE.md`, skill files, and hooks every few months, keeping only what truly matters.  
- Practitioners fear quality loss and lack quick rollback mechanisms, making the advice feel hard to apply.  
- Nonetheless, model and harness improvements justify regular clean‑ups.

## Skills: value and criticism
- Agent Skills (e.g., `maintainAgent Skills`, `Impeccable`) help turn a generalist model into a specialist.  
- Positive feedback exists, but critiques are valid:
  - Inconsistent quality across domains.  
  - Lack of a standard playbook for authoring.  
  - “Skill hygiene” needed: thin descriptions, vague workflows, and outdated packs reduce usefulness.  
- Community debate ranges from “net positive” to “net negative” due to token cost, noise, and reliability concerns.

## Why configurations rot
- Users keep appending rules to `CLAUDE.md` and skill files after each failure, causing ballooning files and diminishing adherence.  
- Common failure modes:
  - Overly long examples.  
  - Redundant content duplicated from READMEs or manifests.  
  - Adding a rule for every error (compounding growth).  
  - Over‑specific prose that does not translate into desired behavior.  
- Empirical findings:
  - June study of 100 repos: lint leakage 62 %, context bloat 42 %, skill leakage 35 %.  
  - Anthropic’s “new rules of context engineering” removed >80 % of Claude Code’s system prompt for Claude 5 with no measurable loss, showing instruction value can expire.

## Practical audit checklist
- **Run health checks**: Use Claude’s `/doctor` (or equivalent) every few weeks.  
- **Separate memory review**: Audit persistent memory stores independently of prompt files.  
- **Validate each instruction**: Treat every rule as a test; keep only those that still pass.  
- **Trim token usage**: Aim for ≤200 lines per `CLAUDE.md`/`AGENTS.md` as per Anthropic guidance.  
- **Encode essential rules**: Move always‑required constraints into hooks, permissions, or automated tests rather than prose.  
- **Document changes**: Keep a short changelog to enable quick rollback if pruning harms performance.

## Takeaway
Regularly auditing and pruning agent configuration files prevents token bloat, reduces “configuration smell,” and ensures that the agent’s instructions stay aligned with the latest model capabilities and codebase realities.