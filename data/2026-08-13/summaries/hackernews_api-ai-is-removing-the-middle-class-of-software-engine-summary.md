---
title: AI is removing the middle class of software engineering
url: https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html
date: 2026-08-12
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-13T11:44:44.076559
---

# AI is removing the middle class of software engineering

# AI is removing the middle class of software engineering

## Overview
- The story contrasts a 2020 scenario where senior engineers enforce good practices with a 2026 reality where AI‑generated code floods the codebase.
- Large, AI‑produced pull requests appear daily, making it hard to maintain architectural integrity and understand system behavior.

## How AI accelerates bad practices
- Teams can prompt LLMs to produce thousands of lines of code in hours, bypassing design discussions and reviews.
- The output often “works” enough to pass tests, encouraging continuous merging without deep understanding.
- When bugs arise, developers rely on the same AI for fixes, creating endless loops of AI‑generated explanations and changes.
- Decision‑making becomes hidden inside long AI conversation logs, making it impossible to trace why certain architectures or database changes were introduced.

## Consequences for engineering roles
- **Senior reviewers**: Expected to reject massive PRs, but pressure to keep up leads to acceptance.
- **Implementers**: Should break work into smaller, understandable pieces; instead they push huge AI‑generated changes.
- **Architects**: Must justify new components (e.g., Kafka) but often cannot, delegating explanations to the LLM.
- The result is a system so tangled that no single person can grasp its full state, increasing reliance on AI for both creation and maintenance.

## The new AI economy
- Implementation has become cheap and fast; the real value lies in making sound technical decisions and managing complexity.
- High‑salary engineers are retained because they can steer AI output, evaluate recommendations, and maintain system health.
- “Bad” engineers become less employable; their cost rises relative to the diminishing need for manual coding.
- The middle tier of engineers—those who previously handled routine implementation—faces obsolescence unless they develop judgment and oversight skills.

## Takeaways
- AI is a powerful shortcut, not a cure for technical debt; shortcuts still accumulate debt that is hard to reverse.
- Effective teams need individuals who can:
  - Assess AI suggestions critically.
  - Explain architectural choices without relying on opaque AI logs.
  - Design migration strategies for irreversible changes (e.g., database schema additions).
- The most valuable team members will be those who retain deep system knowledge and can guide AI, while others risk being replaced or relegated to lower‑paid roles.