---
title: Leanstral 1.5 - Mistral AI | Mistral Docs
url: https://docs.mistral.ai/models/model-cards/leanstral-1-5-26-06
date: 2026-06-30
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-07-01T20:00:26.229420
---

# Leanstral 1.5 - Mistral AI | Mistral Docs

# Leanstral 1.5 Summary

## Overview
- Updated Lean 4 formal proof engineering model.
- Optimized for automated theorem proving and autoformalization.
- Total parameters: 119 billion; active parameters: 6.5 billion.
- Context window: 256 k tokens.
- Pricing: $0 (free).

## Performance & Modalities
- Emphasizes speed and performance (specific metrics not listed).
- Supports a wide range of modalities through dedicated API endpoints.

## Features (API Endpoints)
- Chat completions: `/v1/chat/completions`
- Function calling: `/v1/chat/completions`
- Agents & conversations: `/v1/agents`, `/v1/conversations`
- Built‑in tools: `/v1/agents`, `/v1/conversations`
- Structured outputs: `/v1/chat/completions`, `/v1/conversations`
- Predicted outputs: `/v1/chat/completions`, `/v1/conversations`
- Prefix handling: `/v1/chat/completions`, `/v1/conversations`
- OCR: `/v1/ocr`
  - Annotations – Structured
  - Bounding‑box extraction
- Document Q&A: `/v1/chat/completions`, `/v1/conversations`
- Fill‑in‑the‑middle (FIM): `/v1/fim/completions`
- Embeddings: `/v1/embeddings`
- Moderations: `/v1/moderations`, `/v1/chat/moderations`
- Audio transcriptions: `/v1/audio/transcriptions`
- Text‑to‑speech: `/v1/audio/speech`
- Timestamps: `/v1/audio/transcriptions`
- Batching: `/v1/batch`

## Related Models
- Mistral Medium 3.5 – version 26.04
- Voxtral TTS – version 26.03
- Mistral Small 4 – version 26.03