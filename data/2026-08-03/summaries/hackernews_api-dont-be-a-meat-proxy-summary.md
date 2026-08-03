---
title: "Don't be a meat proxy"
url: https://gruhn.me/blog/2026-08-03/
date: 2026-08-03
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-03T20:04:09.802839
---

# Don't be a meat proxy

# Don't be a meat proxy

## Main concerns
- The author frequently receives AI‑generated replies (e.g., from Claude) when asking questions in Slack, commenting on pull requests, or debating in WhatsApp.
- Relaying AI output verbatim adds no value; it creates extra work for the recipient.

## Problems with raw AI output
- It is often verbose, filled with plausible but incorrect information, and heavy on jargon.
- Example: “NATS control‑plane events: stream leader election / R3 quorum re‑form during pod churn,” which required the author to look up many terms.

## Recommended approach
- Use AI to assist, but always:
  - Read the generated text.
  - Understand and verify its accuracy.
  - Rewrite the response in your own words, demonstrating that you performed the prior steps.

## Specific case: code review
- It is tempting to copy a ticket description into Claude Code, let Claude generate a review, and then copy reviewer comments back into Claude for iteration.
- This creates a “meat proxy” situation where reviewers do the real work while the original author merely forwards AI output without personal engagement.

## Call to action
- Avoid being a passive conduit for AI responses.
- Add value by personally processing, validating, and communicating the information.