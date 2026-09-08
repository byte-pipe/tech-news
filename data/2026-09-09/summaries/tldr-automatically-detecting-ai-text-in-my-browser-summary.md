---
title: Automatically detecting AI text in my browser
url: https://www.seangoedecke.com/deckard/
date: 2026-09-09
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-09T08:37:41.703389
---

# Automatically detecting AI text in my browser

# Summary of “Automatically detecting AI text in my browser”

## Current Landscape
- AI‑text detection is an underserved niche; Pangram is the only widely used service and performs well.
- Anticipation that major social platforms will soon scan posts and comments for AI‑generated content.
- The author prefers a solution that runs locally to avoid sending all browser text to third‑party services.

## Local Model Benchmark
- Tested several small open‑source models against AI‑detection datasets.
- Reported false‑positive rates (human text flagged) and detection rates (AI text caught):

| Model / Variant | Human falsely flagged | AI‑involved text caught |
|-----------------|-----------------------|------------------------|
| Gradient — MLX 4‑bit | 2.712% | 52.35% |
| EditLens RoBERTa‑large — community INT8 | 2.484% | 56.06% |
| Vanguard | 2.267% | 44.92% |
| Desklib | 3.008% | 45.04% |
| Raschka DistilBERT | 2.598% | 39.01% |
| Raschka Qwen3‑0.6B | 2.028% | 28.67% |
| Raschka ModernBERT | 1.698% | 21.58% |
| TMR / Oxidane — INT8 | 1.595% | 19.35% |

- Models are less accurate than Pangram but sufficient for flagging suspicious passages, given an expected ~2% false‑positive rate.

## Deckard Chrome Extension
- Built a Chrome extension named **Deckard** that runs a locally‑hosted model (the best‑performing one from the table) on macOS.
- Operates via native messaging; no separate web server required.
- Memory usage: 400 MB – 1.2 GB while active (comparable to 5–6 extra Chrome tabs).
- Auto‑suspends after five minutes of inactivity.

## Performance and Limitations
- Successfully identified known AI‑generated text (e.g., YouTube AI summary, AI snippets in the author’s posts).
- Runs continuously without noticeable heat or battery impact on the author’s MacBook Pro (results may vary on other hardware).
- Still considerably less accurate than Pangram; the author views it as “good enough” for personal use and recommends it to others interested in automatic detection.

## Future Outlook
- Expectation that AI‑detection models will improve over time, eventually offering small local models with performance comparable to current cloud services.
- Anticipates swapping Deckard’s underlying model for a future version that is 2×–10× better.
- Belief that AI‑generated text will retain detectable stylistic signatures despite models becoming more human‑like.

## Additional Notes
- Substack already offers a manual AI‑scan button for posts.
- Development experience was positive: the author made high‑level architectural choices, used C++ for inference, and leveraged native messaging instead of local HTTP.
- The author invites readers to subscribe for updates and share the post on Hacker News.