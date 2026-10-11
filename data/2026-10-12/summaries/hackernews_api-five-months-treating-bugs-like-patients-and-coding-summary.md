---
title: Five months treating bugs like patients and coding agents like a medical team
url: https://www.cockroachlabs.com/blog/experiment-running-hospital-code/
date: 2026-10-10
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-12T06:01:12.516331
---

# Five months treating bugs like patients and coding agents like a medical team

# Five months treating bugs like patients and coding agents like a medical team

## Key Takeaways
- We built a coding‑agent pipeline modeled on a teaching hospital (roles such as Triage Nurse, Fellow, Review Attending, Discharge Nurse) to enforce mandatory planning, rigorous reviews, and safety guardrails before code is merged.  
- In five months the pipeline processed > 1 million lines of code with only 7 reverts, demonstrating that structured agentic workflows can safely handle complex database migrations.  
- Emphasizing meticulous record‑keeping, strict test coverage, and planning reviews minimized regressions and enabled features like the Migration Assistant while maintaining enterprise‑grade reliability.

## Motivation and Choice of a Hospital Metaphor
- Coding agents can generate large amounts of code quickly, but trusting them to produce production‑grade, well‑tested, maintainable code is difficult.  
- Our priority is data correctness in migration tools; we prefer agents that run longer but produce safe output over high‑throughput, low‑quality pipelines.  
- Teaching hospitals provide a proven model for high‑stakes work with uneven staff ability, mandatory handoffs, and second‑opinion checks, making them a natural fit for our quality‑first goals.

## Pipeline Architecture
- **Infrastructure:** Entire workflow runs on GitHub Actions; the state of each “patient” (issue) is stored in issue labels and supplemental chart files.  
- **Stages:** Each stage is a GitHub workflow triggered by an incoming label; on completion the agent writes an outgoing label, a structured note (e.g., `<!-- SINAI:TREATMENT_PLAN -->`), and advances the issue to the next stage.  
- **Roles:**  
  - *Triage Nurse* – initial intake and decomposition of large issues into sub‑issues with dependency graphs.  
  - *Fellows* – implement code for individual sub‑issues.  
  - *Review Attendings* – perform mandatory plan reviews and code reviews before any code is written.  
  - *Discharge Nurses* – finalize and merge code after all safety checks pass.  
- **Support Departments:**  
  - *Charge Nurse* – monitors stalled stages and re‑runs them.  
  - *Infection Control* – can lock down the entire pipeline if a critical failure occurs.  
  - *Safety Department* – writes weekly process reviews and runs post‑incident conferences.  
  - *Research Department* – proposes new work and files policy PRs.  
- **Safety Rules (encoded in agent skills):**  
  1. No code is written before a plan exists.  
  2. No plan proceeds without a review.  
  3. All code must meet test‑coverage thresholds comparable to our best‑tested dialect (PostgreSQL).  

## Results Over Five Months
- **Scope:** Added IBM Db2 support to the MOLT migration toolset.  
- **Effort:** The entire feature was delivered in < 2 days, with a token cost of $4,172 (≈ 164× faster and 38× cheaper than the 9‑month, $160 K effort required for Oracle support in 2024).  
- **Process Metrics:**  
  - 1 parent issue → 32 sub‑issues, 27 merged PRs.  
  - 55 reviewer feedback cycles, 9 escalations (2 to humans).  
  - Test coverage matched that of PostgreSQL, our benchmark dialect.  
- **Reliability:** Only 7 total reverts across > 1 M lines of code, confirming the pipeline’s ability to maintain high quality at scale.

## Lessons Learned
- A hospital‑style, role‑based pipeline introduces bureaucracy and longer turnaround times, but those trade‑offs are justified when the cost of a buggy migration is high.  
- Structured handoffs and explicit documentation (charts, labels, sentinel notes) provide clear audit trails and make it easy for later agents or humans to understand prior decisions.  
- The metaphor helped align engineering culture around patient safety, encouraging the team to treat each code change as a high‑risk operation requiring multiple checks.  
- While not cheaper than a simple swarm of agents, the approach delivers a markedly higher‑quality product, which is essential for database migration tools that handle customer data.