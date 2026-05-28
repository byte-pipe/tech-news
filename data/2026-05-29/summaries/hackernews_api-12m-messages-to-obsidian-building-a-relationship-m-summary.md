---
title: 1.2M Messages to Obsidian - Building a Relationship Map from 20 Years of Chat History
url: https://drobinin.com/posts/am-i-a-bad-friend/
date: 2026-05-28
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-29T04:39:05.407160
---

# 1.2M Messages to Obsidian - Building a Relationship Map from 20 Years of Chat History

# 1.2 M Messages to Obsidian – Building a Relationship Map from 20 Years of Chat History

## Motivation and Background
- Inspired by Tim Urban’s “Your Life in Weeks” grid, I wanted a metric that captured feelings and interpersonal impact rather than just milestones.  
- Traditional journaling missed forgotten conversations and slow‑moving patterns, so I turned to my digital chat archives as a memory‑augmented “personal CRM.”  

## Digital History Overview
- **2000s:** ICQ, IRC, DC++ – informal, now discarded.  
- **Late 2000s‑2010s:** VK (post‑Soviet social network), Twitter, Facebook – archives retained, useful for early adult life.  
- **2010s‑2020s:** Instagram and Telegram – DMs and story interactions became primary channels for catching up.  

## Data Acquisition and Normalisation
- Exported JSON/HTML from five platforms (Telegram, VK, Instagram, Twitter, Facebook).  
- Faced platform‑specific quirks (Cyrillic double‑encoding, differing message IDs, encrypted Facebook messages).  
- Unified all exports into a tab‑separated format, preserving timestamps, sender, receiver, and content.  

## Noise Reduction
- Initial corpus: 486 k messages with partner over ten years.  
- Composition: 2.4 % links, 9.1 % media, 1.5 % emoji‑only, 28.4 % short fillers, 58.7 % substantive text.  
- Filtered out emojis, links, media, and most filler tokens using a sampled denylist (≈80 manually vetted short tokens).  
- Resulting cleaned corpus: ~52 k unique lemmas; novelty rate fell to ~6 % after 2016, indicating a largely stable personal vocabulary.  

## Identity Resolution (“Which Sasha?”)
- Users appear under multiple nicknames, diminutives, and language‑specific forms (e.g., Alexander → Al, Alex, Sasha).  
- Simple heuristics and off‑the‑shelf NER failed for first‑name‑only mentions in group chats.  
- Considered fine‑tuning BERT on hand‑labelled name‑resolution pairs but rejected due to labeling effort.  

## Event Classification Strategy
- Keyword‑based approaches (first‑person verbs + NER) produced many false positives because context determines meaning (e.g., “I moved” can be relocation, interior design, or emotional shift).  
- Hand‑labelled BERT fine‑tuning projected 70‑80 % accuracy, insufficient for 1.2 M messages (even 1 % false positives → 12 k spurious events).  

## LLM‑Driven Processing
- Utilised large language models for both name‑resolution and event detection.  
- Ran >200 inference sessions (~15–20 B tokens), costing ~$15 k on cloud or 10–15 weeks on a local M5 Pro with Qwen3‑30B‑A3B.  
- Processed messages in chunks ≤6 000 to keep false‑positive rate <1 % (validated on a 200‑event holdout set).  
- LLM output: structured JSON manifests containing daily notes, person profiles, place stubs, timelines, and ancillary items (recipes, meeting notes).  

## Outcomes and Reflections
- Created a searchable “vault” in Obsidian that links conversations, events, and emotional tones across two decades.  
- Gained quantitative insight into personal emotional bandwidth, friendship half‑lives, and endearment cycles.  
- Realised that data‑driven self‑analysis can expose hidden patterns but also demands careful handling of noise, identity ambiguity, and classification errors.  

## Key Takeaways
- Raw chat archives are a rich source for longitudinal self‑knowledge when properly cleaned and normalised.  
- Simple rule‑based filters are insufficient for nuanced social signals; LLMs provide a pragmatic balance of accuracy and scalability.  
- Mapping identities across platforms remains a bottleneck; future work could explore semi‑supervised name‑resolution with user‑provided alias lists.  
- The resulting personal CRM offers a concrete tool for improving relationship management and self‑reflection.