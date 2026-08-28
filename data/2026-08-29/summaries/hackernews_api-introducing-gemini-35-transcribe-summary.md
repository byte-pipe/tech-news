---
title: Introducing Gemini 3.5 Transcribe
url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/
date: 2026-08-28
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-29T01:33:45.363930
---

# Introducing Gemini 3.5 Transcribe

# Introducing Gemini 3.5 Transcribe

## Overview
- Gemini 3.5 Transcribe is Google’s newest speech‑to‑text model, focused on precise, intelligent real‑time transcription.  
- Converts raw audio into polished, formatted text, handling background noise, jargon, and disfluencies better than prior models.  
- Available through two APIs: a low‑latency streaming “Live” API and a batch “Interactions” API with speaker attribution and word‑level timestamps.

## Key Features
- **Smart transcription** – auto‑removes filler words, processes self‑corrections, and formats output.  
- **Function calling** – can invoke other Gemini models for tasks such as image generation or file analysis (currently in the macOS Gemini app).  
- **Custom vocabulary** – adapts to specialized terms and unique spellings supplied by the user.  
- **Global language support** – detects and transcribes more than 85 languages, handling regional accents and code‑switching.  
- **Multi‑speaker identification** – attributes speech to up to three speakers with timestamps (experimental for more speakers).  
- **Live language switches** – maintains accuracy when speakers change language mid‑conversation.

## Performance Metrics
- Word Error Rate (WER): 4.0 % for streaming, 2.6 % for non‑streaming use‑cases (Artificial Analysis).  
- Improves final transcription latency by ~70 % over the previous Chirp 3 model.  
- FLEURS benchmark results: 5.50 % WER streaming, 5.04 % WER non‑streaming, outperforming Chirp 3 across top languages.

## Product Integrations
- **Gboard (Android) – Rambler**: transforms spoken thoughts into clean text, filters filler words, and supports voice‑driven edits.  
- **Google Antigravity**: combines screen context and chat history (with permission) for accurate transcription of file names, agent thoughts, and documents.  
- **Gemini app (macOS)**: provides clean formatted text, voice commands, and background function calls for summarizing files, repurposing text, or generating images.  
- **Chrome (coming soon)**: will enable “talk‑to‑type” in any web field for dictation and Gemini prompts.  
- Accessible in Google AI Studio and Gemini Enterprise Agent Platform for developers.

## Developer Ecosystem
- **Live API (gemini‑3.5‑transcribe‑live)** – bidirectional streaming with sub‑second latency for interactive voice apps.  
- **Interactions API (gemini‑3.5‑transcribe)** – processes recorded audio with speaker attribution and timestamps.  
- Partner platforms (Agora, Fishjam, LangChain, LiveKit, Pipecat, Vercel, Vision Agents) handle real‑time media streaming, letting developers focus on UX.

## Early Reviews
- Positive feedback from companies such as vivo, Intellitek Health, and Lingopal, highlighting low latency, high accuracy, and broad language coverage.  
- Developer platforms report easy integration and high performance using the Gemini Live API.

## Availability
- **Developers** – public preview in Gemini API via Google AI Studio and Google Antigravity.  
- **Enterprises** – public preview on Gemini Enterprise Agent Platform; upcoming Gemini Enterprise for Customer Experience.  
- **Consumers** – Gemini app (macOS, English), Rambler on Android (selected countries/languages), Chrome integration forthcoming.

## Related Stories
- Gemini Omni 1.1 Flash – more control for builders.  
- “Full‑stack” AI explained.  
- Gemini 3.7 Flash release.  
- Omni experts discuss model excitement.  
- Builder showcase: 5 projects with Gemini Omni.  
- July 2026 AI news roundup.