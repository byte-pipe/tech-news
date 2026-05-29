---
title: Building an AI-Native Paid Ads System
url: https://jon4growth.substack.com/p/the-ai-native-paid-ads-system
date: 2026-05-30
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-05-30T06:02:03.344807
---

# Building an AI-Native Paid Ads System

# Building an AI-Native Paid Ads System

## Overview
- The author describes an “AI‑Native Paid Ads System” built around Claude, Anthropic’s chat model.
- The system integrates ad management, creative generation, reporting, and knowledge sharing within a single conversational interface.
- A layered architecture is presented, starting with data connectors and ending with a GitHub‑based learning loop.

## Layer 1 – Connectors & Data Sources
- Connectors let Claude interact directly with external tools (e.g., Meta Marketing API, Higgsfield image/video generator).
- Meta connector provides live campaign data; Higgsfield can generate quick creative assets using models like Nano Banana.
- Additional automated inputs include:
  - Scheduled tasks that pull competitor website changes into Notion for creative inspiration.
  - Ongoing ingestion of Meta campaign metrics for continuous analysis.

## Layer 2 – Claude Skills and `claude.md` File
- A `claude.md` file stores brand information (ICP, design preferences, tone) so every prompt has built‑in context.
- A custom Claude skill for paid‑social management is created by prompting Claude to research top experts and compile best practices.
- The skill acts as a “brain” for tasks such as dashboard building, ad creation, and campaign optimization.

## Running the Account Audit
- Prompt example:
  1. Confirm which Meta ad account is connected.
  2. Pull performance data for the last 30 and 90 days (spend, CPM, CTR, CPA, ROAS, frequency, etc.).
  3. Retrieve campaign/ad‑set breakdowns, top/bottom performers, creative fatigue signals, pixel/CAPI health, industry benchmarks, and Meta opportunity scores.
- Audit output structure:
  - Verdict (single blunt paragraph)
  - Account health (pixel, event match, tracking)
  - Performance summary (spend pacing, winning vs. losing elements)
  - Creative analysis (winning assets, fatigue, patterns)
  - Structure & targeting review (architecture, audience overlap, budget allocation)
  - Benchmark comparison
  - Top 5 actionable items for the week (specific tests, ad sets, and rationale)
- Rules enforce real numbers, clear error reporting, and no corporate hedging.

## Higgsfield in the Loop
- AI‑generated static assets are demonstrated for the GrowthPair brand.
- Claude can further refine prompts to produce more brand‑aligned creatives, including short videos.
- The author notes AI creative is still a preview; human designers remain preferred for top‑tier assets.

## Layer 3 – Claude’s Live Artifacts and Tasks
- With Meta data connected, Claude can generate live dashboards (e.g., for LinkedIn thought‑leader ads) using “live artifacts.”
- The author references a deeper essay on building such dashboards quickly.

## Layer 4 – Learning Loop with GitHub
- Campaign learnings are stored in a shared private GitHub repository, providing a permanent source of truth.
- Setup steps using Claude Code:
  1. Create a local folder and link it to Claude Code.
  2. Prompt Claude Code to configure the repository for paid‑ads learnings.
  3. Claude Code guides folder structure and initial commit.
  4. Push the repo to GitHub, add teammates as collaborators, and sync via GitHub Desktop.
- The approach scales to a broader marketing‑org repo, enabling the whole team and Claude to reference historical performance.

## TL;DR – Action Steps
- Install Meta and Higgsfield connectors in Claude (≈2 minutes).
- Build `claude.md` with brand context and create the paid‑ads Claude skill.
- Run the account audit prompt to get a data‑driven health report and weekly action list.
- Use Higgsfield (or other generators) for rapid creative drafts, refining prompts as needed.
- Create live dashboards with Claude’s artifacts for real‑time monitoring.
- Set up a private GitHub repo via Claude Code to archive test results and share knowledge across the team.