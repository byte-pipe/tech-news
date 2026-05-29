---
title: Apple working to cram massive Gemini model into iPhone to power new Siri - Ars Technica
url: https://arstechnica.com/ai/2026/05/apple-reportedly-trying-to-distill-googles-multi-trillion-parameter-gemini-ai-to-run-on-iphone/
date: 2026-05-30
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-05-30T06:01:10.131229
---

# Apple working to cram massive Gemini model into iPhone to power new Siri - Ars Technica

# Apple working to cram massive Gemini model into iPhone to power new Siri – Ars Technica

## Overview
- Apple has delayed AI‑enhanced Siri several times since its 2024 promise and now plans to integrate Google’s Gemini model.
- The integration will be a hybrid system: part on‑device processing, part cloud processing via Google and Nvidia.
- Apple’s emphasis on privacy is challenged by the need for cloud resources to run large models.

## Technical Constraints
- Smartphone GPUs can handle more AI tokens than dedicated NPUs, but phones lack sufficient RAM for trillion‑parameter models.
- On‑device AI models are limited to a few billion parameters and are quantized to lower precision, reducing accuracy.
- Even the largest cloud models can be “pretty dumb” at times, highlighting the difficulty of delivering truly smart local assistants.

## Google Partnership
- Google offers Gemini Nano for mobile, optimized for contextual tasks, not full conversational assistants.
- Apple is distilling Google’s massive Gemini models into smaller versions that can run locally, but a cloud fallback remains inevitable.
- Apple’s Private Cloud Compute, built on M‑series Macs, struggled to run undistilled Gemini models.

## Cloud Execution and Nvidia Deal
- Complex Siri requests will likely be routed to Google’s cloud infrastructure, not Apple’s own servers.
- Apple signed a deal with Nvidia to use its Confidential Computing platform, keeping data encrypted while processed on Nvidia GPUs.
- This approach allows Apple to claim continued privacy protection despite cloud reliance.

## User Experience Implications
- Users will not be informed which Gemini version handles a particular Siri request; the system aims for a “seamless” experience.
- Encrypted cloud processing can introduce latency, making remote Siri responses feel slower compared to purely local AI.

## Privacy and Branding
- Apple may retain its Private Cloud Compute branding while leveraging Nvidia’s Confidential Computing to address privacy concerns.
- The hybrid model represents a shift from Apple’s previous “local‑only” AI narrative.

## Outlook
- As WWDC approaches, Apple is likely to showcase its chip expertise while acknowledging the necessity of cloud assistance for advanced AI features.
- The balance between on‑device capability, cloud power, and user privacy will define the next generation of Siri.