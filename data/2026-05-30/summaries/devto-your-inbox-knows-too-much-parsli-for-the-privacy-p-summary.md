---
title: Your Inbox Knows Too Much: Parsli for the Privacy Paranoid - DEV Community
url: https://dev.to/olgabraginskaya/your-inbox-knows-too-much-parsli-for-the-privacy-paranoid-7ah
date: 2026-05-24
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-05-30T06:01:18.969065
---

# Your Inbox Knows Too Much: Parsli for the Privacy Paranoid - DEV Community

# Summary of “Your Inbox Knows Too Much: Parsli for the Privacy Paranoid”

## What I Built
- Parsli is a **local‑first AI assistant** that extracts shipment information from a user’s Gmail without sending any email data to external servers.  
- It parses a wide variety of shipment‑related emails, extracts tracking numbers, classifies events, and builds chronological timelines across different marketplaces, carriers, customs notices, and stores.  
- The system records every processing step: rule matches, model decisions, confidence scores, extracted entities, token usage, timings, and reasoning, making debugging transparent.  
- The prototype currently handles email input; future extensions will add SMS, screenshots, and voice messages as additional sources.

## How I Used Gemma 4
- A deterministic pipeline handles the majority of predictable email formats (e.g., Amazon, UPS, Israel Post) using HTML cleanup, regex extraction, and language packs.  
- Ambiguous or non‑standard emails (multilingual customs notices, varied marketplace formats) are passed to **Gemma 4** for:
  - Validation of extracted candidates  
  - Confidence estimation  
  - Shipment‑state classification  
  - Consistency checking before persisting results  
- The decision trail logs which component (rules or model) produced the final answer.

## Key Results
- In a real mailbox of 48 relevant shipment emails:  
  - 55 % resolved by deterministic rules (model used only as a cheap audit)  
  - 38 % required the model to correct rule errors  
  - Remaining cases were edge‑case splits  
- Pure rule‑based processing would achieve roughly 60 % accuracy; a model‑only approach would be slower and more costly.  
- Combining both yields high accuracy while keeping inference fast and inexpensive.

## Technical Setup
- Local inference runs **google/gemma‑4‑e4b** on an M2 MacBook Pro via LM Studio in headless mode.  
- The model size is sufficient for the narrow, structured classification task, providing good reasoning speed without a dedicated GPU.

## Future Directions
- Incorporate additional input channels (SMS, screenshots, voice messages) to capture shipment updates spread across platforms.  
- Continue refining the rule set and model prompts to reduce edge‑case failures.  
- Maintain the observable, audit‑friendly architecture to keep the system transparent for users concerned about privacy.  

**Code repository:** https://github.com/olgazju/parsli