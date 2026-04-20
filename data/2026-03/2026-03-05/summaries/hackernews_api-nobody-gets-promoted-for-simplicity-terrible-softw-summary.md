---
title: Nobody Gets Promoted for Simplicity – Terrible Software
url: https://terriblesoftware.org/2026/03/03/nobody-gets-promoted-for-simplicity/
date: 2026-03-04
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-03-05T06:01:33.526158
---

# Nobody Gets Promoted for Simplicity – Terrible Software

# Nobody Gets Promoted for Simplicity

## Main Argument
- Engineering cultures often reward over‑engineering because complex solutions are more visible in promotion narratives.
- Simple, well‑executed work tends to be invisible, even though it may be higher quality.
- The incentive structure unintentionally favors adding unnecessary abstraction, scalability, and “future‑proofing.”

## Illustrative Example
- **Engineer A**: Chooses the simplest design, writes ~50 lines, ships in days, minimal documentation.
- **Engineer B**: Builds a new abstraction layer, pub/sub system, configuration framework; takes weeks, generates many PRs and a flashy description.
- Promotion packets favor Engineer B’s “scalable event‑driven architecture” while Engineer A’s contribution is reduced to “Implemented feature X.”

## Problems in Hiring and Design Reviews
- **Interviews**: Simple solutions are often challenged with “What about scalability?” leading candidates to add unnecessary components to impress.
- **Design reviews**: Requests to “future‑proof” push engineers to add layers that may never be needed, rewarding complexity over clarity.

## When Complexity Is Justified
- Real need for distributed systems when handling millions of transactions.
- Service boundaries are appropriate when many teams collaborate on a product.
- The issue is *unearned* complexity—building for hypothetical future problems rather than current requirements.

## Making Simplicity Visible
- Document the decision‑making process, not just the final code.
- Example phrasing: “Evaluated three approaches, chose a straightforward implementation that met all requirements, shipped in two days, zero incidents over six months.”
- Treat the choice to avoid extra layers as a deliberate, valuable decision.

## Advice for Engineers
- Proactively frame your work with context, trade‑offs, and why you avoided extra complexity.
- In design reviews, respond with cost/benefit analysis of adding future features now versus later.
- Discuss documentation and narrative needs with your manager to ensure they can advocate for you during reviews.
- If the organization consistently rewards over‑engineering, consider whether the culture aligns with your values.

## Advice for Engineering Leaders
- Redefine promotion criteria to value avoided complexity and sound judgment alongside impact.
- Change review questions: from “Have we thought about scale?” to “What is the simplest shippable version and what signals would trigger added complexity?”
- Scrutinize promotion packets for unnecessary “impressive‑sounding” systems and ask if they were truly needed.
- Help engineers craft narratives that highlight evaluation and decision‑making, not just the code they wrote.

## Takeaway
- Simplicity requires effort, visibility, and cultural support.
- Both engineers and leaders must actively document and communicate the rationale behind keeping solutions simple to ensure that good judgment is recognized and rewarded.
