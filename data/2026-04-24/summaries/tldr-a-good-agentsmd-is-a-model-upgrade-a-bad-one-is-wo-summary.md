---
title: A good AGENTS.md is a model upgrade. A bad one is worse than no docs at all. | Augment Code
url: https://www.augmentcode.com/blog/how-to-write-good-agents-dot-md-files
date: 2026-04-24
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-04-24T06:01:38.986928
---

# A good AGENTS.md is a model upgrade. A bad one is worse than no docs at all. | Augment Code

# Summary of “A good AGENTS.md is a model upgrade. A bad one is worse than no docs at all.”

## Study Overview
- Collected dozens of AGENTS.md files from a monorepo and measured their impact on a coding agent’s output.  
- Best files improved quality comparable to a major model upgrade; worst files degraded performance below having no AGENTS.md.  
- Conducted systematic evaluation using AuggieBench on PR‑level tasks, comparing agent output with golden PRs, both with and without the AGENTS.md.

## Key Findings
- **Variable impact:** The same AGENTS.md can boost one task (e.g., bug‑fix) by ~25% and hurt another (e.g., complex feature) by ~30%.  
- **Most content is neutral or harmful:** Only specific, learnable patterns consistently help.

## Effective Patterns
1. **Progressive disclosure**  
   - Keep the main AGENTS.md 100–150 lines, covering common cases.  
   - Offload detailed references to separate, narrowly scoped files.  
   - Gains reverse when the main file grows larger.

2. **Procedural workflows**  
   - Use numbered, multi‑step instructions.  
   - Example: a six‑step deployment workflow cut missing‑file PRs from 40% to 10% and raised correctness by 25%.

3. **Decision tables**  
   - Present mutually exclusive choices up front to resolve ambiguity.  
   - Improves adherence to conventions (e.g., choosing between React Query and Zustand) by ~25%.

4. **Real‑code examples**  
   - Include 3–10 line snippets of production code relevant to the task.  
   - Boosts code reuse and consistency by ~20%.

5. **Domain‑specific rules**  
   - Precise, enforceable guidelines (e.g., “use Decimal for financial calculations”) improve best‑practice scores when directly applicable.

6. **Pair “don’t” with a “do”**  
   - Providing an alternative action prevents the agent from over‑exploring or stalling.  
   - Long lists of prohibitions without alternatives cause conservative, incomplete output.

7. **Modular documentation**  
   - Isolated submodule AGENTS.md files outperform massive repo‑root docs.  
   - Large surrounding documentation (hundreds of KB) overwhelms the agent, negating the benefit of a good AGENTS.md.

## Common Failure Modes
- **Over‑exploration trap**  
  1. **Excessive architecture overviews** lead the agent to ingest irrelevant context (tens of thousands of tokens), reducing completeness.  
  2. **Too many warnings without solutions** force the agent to verify each rule, causing hesitation and lower output quality.

## Recommendations
- Keep AGENTS.md concise and focused; use reference files for depth.  
- Structure guidance as clear workflows, decision tables, and paired “do/don’t” statements.  
- Limit architecture descriptions to essential boundaries.  
- Ensure the surrounding documentation ecosystem is not overly large; prune or summarize where needed.