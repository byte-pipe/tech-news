---
title: Anthropic shares more details about how Claude’s new watermarks will work | TechCrunch
url: https://techcrunch.com/2026/08/15/anthropic-shares-more-details-about-how-claudes-new-watermarks-will-work/
date: 2026-08-15
site: newsfeed
model: gpt-oss:120b-cloud
summarized_at: 2026-08-16T06:01:45.832026
---

# Anthropic shares more details about how Claude’s new watermarks will work | TechCrunch

# Summary of Anthropic’s Claude Watermark Details

## Overview
- Anthropic published a blog post explaining how it will embed watermarks in Claude‑generated text to meet the EU AI Act’s Transparency Code.  
- The watermark is a hidden pattern detectable only with a special key; it does not affect the visible quality of the output.

## User Reaction
- Discussions on Reddit and X show mixed opinions: some view it as a conspiracy against users, others see it as a necessary transparency measure.  
- Several users have reportedly cancelled their Claude subscriptions in response.

## Technical Implementation
- Anthropic will use the SynthID‑Text method introduced by Google DeepMind in 2024.  
- A watermark detection API will be released.  
- The approach differs from AI‑detection tools (e.g., Pangram) that look for stylistic “tells.”

## Effect on Editing and Rewrites
- Light editing is unlikely to fully remove the watermark.  
- A complete rewrite that replaces every word would likely erase it, but then the text may no longer be considered AI‑generated.  
- For lightly edited text, especially short passages, there may be little watermark signal because most words remain human‑written.

## Impact on Code Generation
- Watermarks will appear less frequently in code because Claude must produce functional code, limiting arbitrary word choices.  
- When arbitrary choices exist (e.g., comments), a watermark may be inserted, but its effect on the actual code is negligible.

## Industry Context
- Anthropic notes that other major AI model developers have also signed the Code of Practice and will implement their own watermarks.