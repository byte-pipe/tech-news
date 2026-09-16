---
title: "AI Didn't Remove the Engineering Work. It Just Made It Easier to Pretend You Did. - DEV Community"
url: https://dev.to/dj29/ai-didnt-remove-the-engineering-work-it-just-made-it-easier-to-pretend-you-did-42m9
date: 2026-09-15
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-09-17T05:06:51.174948
---

# AI Didn't Remove the Engineering Work. It Just Made It Easier to Pretend You Did. - DEV Community

# AI Didn't Remove the Engineering Work. It Just Made It Easier to Pretend You Did.

## Main Argument
- The rise of AI coding tools and “building in public” has lowered the perceived threshold for what counts as engineering.
- Producing a working product with AI is being mistaken for understanding why it works, similar to calling yourself a bartender after using a vending machine.
- The real issue is conflating “it works” with “I understand the architecture, constraints, and failure modes.”

## Illustrative Example: ShelfTalk Rebuild
- Original project: a college‑semester MERN book‑club app, shipped minimally and left idle on GitHub.
- GitHub “Finish‑Up‑A‑Thon” forced a production‑grade rewrite:
  - Switched from REST polling to real‑time Socket.io chat.
  - Added a live synchronized reading room.
  - Migrated to MongoDB Atlas with GridFS.
  - Replaced Create React App with Vite, cutting HMR time by ~80%.
- Placed in the top 10 of 500+ entries.

## The Bug That Highlighted the Gap
- Added an optimization: suppress desktop notifications when the tab is visible.
- Users missed direct messages; testing reproduced no issue.
- Root cause: an incorrect assumption that “visible tab = user paying attention.”
- Fix: remove the optimization, accepting occasional redundant pings over silent message loss.
- The bug never appeared in a demo and required real‑world user feedback to surface.

## Role of AI in the Process
- GitHub Copilot assisted with scaffolding socket handlers, catching import errors, and autocompleting UI patterns.
- The author does not consider this “vibe coding” because the critical steps—reviewing, debugging, and validating assumptions—were still performed manually.
- The engineering work lies in identifying broken behavior under pressure, not in the typing that AI helps with.

## Where to Draw the Line
- AI is not the problem; the problem is skipping the engineering tasks (design decisions, testing, debugging) while keeping the appearance of having done them.
- The author asks readers to reflect on their own practice: at what point does using AI become merely watching AI build for you?

## Call to Readers
- “Where do you draw the line between using AI to build something and just watching AI build it for you? Have you ever caught yourself on the wrong side of it?”