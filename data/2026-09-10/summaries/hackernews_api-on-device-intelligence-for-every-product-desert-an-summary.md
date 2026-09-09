---
title: On-device intelligence for every product | Desert Ant Labs
url: https://desertant.com/blog/introducing-desert-ant-labs/
date: 2026-09-09
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-10T07:21:44.406427
---

# On-device intelligence for every product | Desert Ant Labs

# On-device intelligence for every product | Desert Ant Labs

## Overview
- Desert Ant Labs is a European AI lab focused on opinionated on‑device intelligence.
- Goal: provide fast, cheap, and private AI models that run on any device, from old phones to modern laptops.
- First release includes 18 models (12 stable, 6 beta) accessible through a single SDK for Swift, Kotlin, and JavaScript.
- Models are free up to 100 k monthly active devices, with no token costs or login requirements.

## Core Models (selected examples)
- **Voz** – 2 s transcription of 10 min audio on iPhone, 4.7× faster than Whisper, includes word‑level timestamps.
- **Clear** – 9 MB model that converts a 5‑min laptop recording to studio‑quality audio in 1 s.
- **Redact** – 12 MB model that masks personal data (names, addresses, card numbers) in real time across 27 languages, achieving 88.8 % detection accuracy.
- **Tongue** – 2 MB language identifier that determines 84 languages from three words, scoring 0.933 accuracy (vs 0.887 for a 293 MB detector).

Full specifications and benchmarks are available at ondesertant.com/models and on Hugging Face.

## Performance Highlights
- **Clear**: 302× real‑time processing on iPhone 16 Pro, 345× on MacBook Pro (M5) for 5‑min audio.
- **Voz**: 319× real‑time on M3 Ultra for 30 min audio, 298× on iPhone 17 Pro, outperforming Apple Speech Analyzer and Whisper large‑v3‑turbo.
- **Clips** (284 MB model): creates 12 clips from a 10‑min video in 5 s, 10× faster and 470× less energy than Claude Sonnet with comparable quality.

## Origin and Motivation
- Built on five years of experience with the Detail video app, which originally relied on cloud APIs for features like Auto Edit and audio enhancement.
- Repeatedly searched Hugging Face for on‑device models, finding a gap between available research and production‑ready, drop‑in solutions.
- Decided to train their own models, treating model creation as a product design problem to achieve superior speed, quality, and cost.

## Market Insight
- Many developers desire on‑device models but are limited by token costs and latency of cloud services.
- NVIDIA research suggests 40–70 % of calls to large models could be replaced by small, specialized models.
- On‑device inference eliminates per‑call costs, removes round‑trip latency, and keeps user data private.

## Compute Landscape
- Global AI data center spend projected at $450 B this year, while billions of consumer devices already contain more compute power than all data centers combined.
- Desert Ant’s “free inference” model leverages this distributed compute, enabling features to run on every interaction without additional cost.

## Vision: Little Brains & Cortex
- First wave of models act as a “cerebellum” – tiny, always‑on components handling routine tasks.
- Future layers (“cortex”) will orchestrate when to use a local model, a larger on‑device model, or a cloud model, scaling with hardware advances.
- Emphasis on tightly coupling model optimization with runtime (e.g., Neural Engine on iPhone, WebAssembly in browsers).

## SDK & Getting Started
- Native SDKs for Swift, Kotlin, and JavaScript are open‑source on GitHub.
- Documentation targets developers and agents; models can be tested via CLI on macOS or in-browser on Hugging Face.
- Invitation to collaborate or build projects using Desert Ant models.