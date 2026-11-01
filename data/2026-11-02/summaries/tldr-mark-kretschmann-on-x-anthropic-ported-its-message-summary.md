---
title: "Mark Kretschmann on X: \"Anthropic ported its Messages API from Python to Rust with a team that initially had no Rust developers. @claudeai handled mos..."
url: https://x.com/mark_k/status/2116912634171711850
date: 2026-11-02
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-11-02T08:49:36.024272
---

# Mark Kretschmann on X: "Anthropic ported its Messages API from Python to Rust with a team that initially had no Rust developers. @claudeai handled mos...

# Summary of Mark Kretschmann’s X post (Nov 1 2026)

## Key Points
- Anthropic migrated its Messages API from Python to Rust despite the team initially lacking Rust expertise.  
- The majority of the implementation was performed by @claudeai, while engineers handled system design, migration planning, and result verification.  
- Reported performance gains:
  - Approximately 40–50 % reduction in CPU usage.  
  - 10–20 % faster time‑to‑first‑token.  
- Migration process:
  - Developed the Rust service in parallel with the existing Python service.  
  - Ran shadow traffic on both versions to compare outputs.  
  - Gradually shifted live traffic to the Rust implementation.  
  - Avoided adding new features during the rewrite.  
- The effort demonstrates a large‑scale production migration with measurable benefits, achieved by engineers leveraging AI to learn and work in a new language.