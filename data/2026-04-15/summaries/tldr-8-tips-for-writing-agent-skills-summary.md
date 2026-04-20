---
title: 8 Tips for Writing Agent Skills
url: https://www.philschmid.de/agent-skills-tips
date: 2026-04-15
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-04-15T06:05:21.156513
---

# 8 Tips for Writing Agent Skills

# 8 Tips for Writing Agent Skills

## 1. Know What a Skill Is
- A skill is a folder containing a required `SKILL.md` file and optional `scripts/`, `references/`, and `assets/` subfolders.
- Structure: front‑matter (name & description), body (markdown instructions), and optional assets.
- Two categories:
  * **Capability skills** – add functionality the base model lacks (e.g., PDF form filling).
  * **Preference skills** – encode specific workflows or team conventions.

## 2. Nail the Description
- The description in `SKILL.md` acts as the trigger; it must be specific about **what** the skill does **and when** to use it.
- Avoid vague phrasing; provide clear, actionable statements.
- Example of good description: “Create, edit, and analyze .docx files, including tracked changes, comments, formatting, or text extraction.”

## 3. Write Instructions, Not Essays
- Give direct directives rather than background trivia.
- Lead with short examples (e.g., a 5‑line code snippet).
- Explain the rationale when a rule matters to help the agent generalize.
- Design skills to work across many prompts, not just a few test cases.

## 4. Keep It Lean
- Load information in layers:
  1. Always loaded – front‑matter.
  2. Loaded on trigger – body (keep < 500 lines).
  3. Loaded on demand – reference files, scripts, assets.
- Split unrelated topics into separate reference files.
- For long reference files, add a table of contents with line hints.

## 5. Set the Right Level of Freedom
- Describe the desired outcome, not a step‑by‑step procedure.
- Provide constraints (e.g., “always run tests before opening a PR”) rather than exact steps.
- If precise ordering is required, implement it as a script instead of a skill.

## 6. Don’t Skip Negative Cases
- Define when the skill **should not** fire to avoid hijacking unrelated requests.
- Include “Do NOT use for …” clauses in the description and test both trigger and non‑trigger scenarios.

## 7. Test It Before You Ship It
1. Manually run the skill with varied prompts.
2. Define measurable success criteria (e.g., compilation, correct API usage).
3. Create 10–20 test prompts covering positive, negative, and edge cases.
4. Execute 3–5 trials per prompt to assess variability.
5. Use a clean environment for each run to prevent context leakage.
6. Prioritize fixing description issues before instruction details.

## 8. Know When to Retire a Skill
- Run evaluations without the skill; if performance remains acceptable, the model has internalized the capability.
- Retire capability skills as model improvements reduce the need for external extensions.
- Refer to the “Practical Guide to Evaluating and Testing Agent Skills” for a detailed retirement workflow.

*End of summary.*
