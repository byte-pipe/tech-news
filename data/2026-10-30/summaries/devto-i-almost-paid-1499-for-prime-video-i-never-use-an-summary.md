---
title: I Almost Paid ₹1,499 for Prime Video I Never Use. An Open-Source AI Model Caught It. - DEV Community
url: https://dev.to/sarvar_04/i-almost-paid-1499-for-prime-video-i-never-use-an-open-source-ai-model-caught-it-1egm
date: 2026-10-29
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-10-30T12:48:35.780801
---

# I Almost Paid ₹1,499 for Prime Video I Never Use. An Open-Source AI Model Caught It. - DEV Community

# Summary of “Hacktoberfest Open-Source AI Challenge: Ghost in the Machine Submission”

## What I Built
- Describes the personal realization that many cheap‑priced products are actually loss leaders for recurring charges (e.g., printers, consoles, coffee machines).
- Shares a concrete example: an Airtel Black bundle gave a free year of Amazon Prime, after which a ₹1,499 annual Prime Video fee was automatically charged even though the author only uses Prime for shipping.
- Introduces **Subscription Ghost**, an open‑weight AI model that scans a user’s list of subscriptions, identifies “ghost” charges, and suggests the exact action to eliminate each wasteful expense.
- The tool runs locally, is free, and never requires bank login information.

## The Four Ghost Types
- **Over‑tier** – paying for a higher‑priced bundle when a cheaper tier covers actual usage (e.g., Prime Video vs. Prime Shopping Edition).
- **Abandoned** – prepaid annual plans that are stopped early (e.g., gym membership paid for a year but unused after February).
- **Dead** – subscriptions that are paid for but barely used.
- **Price creep** – subtle price increases that go unnoticed.

## Demo Highlights
- A web demo (https://simplynadaf.github.io/subscription-ghost/) shows a sample user’s nine subscriptions leaking ₹29,056 per year.
- The biggest leak identified was a 2 TB cloud storage plan costing ₹8,988 annually for a user who only needs ~40 GB; a 50 GB tier at ₹900 would suffice, saving ₹8,088.
- The tool also detects overlapping services (e.g., Amazon Prime, YouTube Premium, Spotify all providing music) and recommends keeping only the most cost‑effective option, saving ₹5,376 annually.
- Users can tap a “ghost” entry, view the recommended fix, and press “Stop this leak” to see the reclaimed amount update instantly.

## How It Works
- **Model**: Uses TabPFN‑v2 (an open‑weight tabular foundation model) to predict the annual waste for each subscription in a single forward pass, without any custom training loop.
- **Input**: Small table containing payment amount, usage frequency, subscription age, price‑creep flag, and prepaid status.
- **Output**: Ranked list of subscriptions by predicted waste, with actionable recommendations for each.
- **Design Choice**: Ranked prediction replaces brittle rule‑based thresholds, allowing the model to learn nuanced waste patterns from the whole table.

## Building Details
- Runs entirely on CPU; optional GPU not required.
- Dependencies installed via a virtual environment; model weights pulled with `ollama pull gemma3:1b`.
- End‑to‑end validation scripts ensure pipeline integrity before launching the local server (`python run.py`).

## Impact
- Demonstrates a practical, privacy‑preserving AI tool that helps users reclaim thousands of rupees annually by exposing hidden subscription costs.
- Aligns with the Hacktoberfest “Ghost in the Machine” theme by making invisible financial “ghosts” visible and actionable.