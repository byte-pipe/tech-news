---
title: GitHub Copilot is moving to usage-based billing - The GitHub Blog
url: https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/
date: 2026-04-28
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-28T06:04:16.234321
---

# GitHub Copilot is moving to usage-based billing - The GitHub Blog

# GitHub Copilot is moving to usage‑based billing – summary

## Why the change
- Copilot has evolved from a simple in‑editor assistant to an agentic platform that runs long, multi‑step coding sessions and uses the latest models.
- Agentic usage requires significantly more compute, making the old premium‑request‑unit (PRU) model unsustainable.
- Usage‑based billing aligns pricing with actual token consumption, supports long‑term reliability, and reduces the need to gate heavy users.

## What’s changing
- Effective June 1 2026, PRUs are replaced by **GitHub AI Credits**.
- Credits are deducted based on token usage (input, output, cached) at the published API rates for each model.
- Base plan prices stay the same:
  - Copilot Pro $10 / month
  - Copilot Pro+ $39 / month
  - Business $19 / user / month
  - Enterprise $39 / user / month
- Code completions and “Next Edit” suggestions remain free and do not consume credits.
- Fallback to lower‑cost models is removed; usage is now limited by available credits and admin budget controls.
- Copilot code review also consumes GitHub Actions minutes, billed at standard per‑minute rates.
- Temporary changes to Individual plans and a pause on self‑serve Business purchases were introduced last week as a reliability measure.

## Impact on individuals
- Monthly Pro and Pro+ subscriptions now include a matching amount of AI Credits ($10 or $39 respectively).
- Users on monthly plans automatically switch to usage‑based billing on June 1 2026.
- Annual plan subscribers keep the PRU model until their plan expires; at that point they transition to Copilot Free (with an upgrade option) or can convert to a monthly plan with prorated credits.

## Impact on businesses and enterprises
- Monthly seat pricing remains unchanged; each seat includes equivalent AI Credits.
- Existing Business and Enterprise customers receive promotional credits for June‑August:
  - Business: $30 / month
  - Enterprise: $70 / month
- Introduced pooled credits across the organization to avoid stranded capacity.
- New admin budget controls allow setting spend limits at enterprise, cost‑center, or user levels, with options to allow or cap additional usage after the pool is exhausted.

## Bottom line
- Plan prices do not change.
- Users gain full visibility and control over spending, tools to track usage, and the ability to purchase extra credits when needed.

## Author
Mario Rodriguez, Chief Product Officer, GitHub. Leads product strategy, previously oversaw GitHub’s AI strategy and Copilot product line.

## Related posts
- Changes to GitHub Copilot Individual plans
- Bringing more transparency to GitHub’s status page
- Developer policy update: Intermediary liability, copyright, and transparency