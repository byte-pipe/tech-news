---
title: Write code like a human will maintain it
url: https://unstack.io/write-code-like-a-human-will-maintain-it
date: 2026-07-10
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-07-11T01:40:12.211302
---

# Write code like a human will maintain it

# Write code like a human will maintain it – Summary

## Main observations
- LLMs can generate code quickly, making it tempting to copy‑paste similar logic across multiple places (route handlers, jobs, endpoints, webhooks).  
- The author repeatedly accepted generated conditionals that were almost identical, rather than extracting a shared helper.  
- Each copied snippet reinforces a pattern in the repository, which the LLM later mimics when asked for new code.

## Risks of duplicated code with LLM assistance
- The repository accumulates “code smells” (duplicate conditionals, god functions, temporary hacks).  
- The LLM learns from the existing code, so future suggestions inherit the same bad patterns.  
- Refactoring becomes harder because the model will preserve all duplicated versions instead of consolidating them.  
- Over time the LLM’s output degrades, making it unreliable for maintenance tasks.

## Recommended practice
- Treat LLM‑generated code as you would any other contribution: prioritize clean, maintainable design (e.g., shared helpers, DRY principles).  
- Review and refactor duplicated logic promptly to prevent the repository from teaching the model poor habits.  
- View the LLM as a tool, not a replacement for human oversight and long‑term code quality.