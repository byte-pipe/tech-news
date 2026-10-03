---
title: Kolibri Has Landed: A Sovereign Open-Weight Model — Aleph Alpha
url: https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/
date: 2026-10-03
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-04T07:01:50.608359
---

# Kolibri Has Landed: A Sovereign Open-Weight Model — Aleph Alpha

# Kolibri Has Landed: A Sovereign Open‑Weight Model

## Introduction
- Released on German Reunification Day, Kolibri is a bilingual (English‑German) Mixture‑of‑Experts transformer.
- Total parameters: 78 B; active parameters during inference: 3 B.
- Supports up to 1 M token context windows.
- Available on Hugging Face under an Apache 2.0 license.
- Built on a continuously iterated training pipeline that first produced Kolibri Origin (30 B total, 3 B active, 65 k token window) and then the current model with minimal time between releases.

## Purpose and Specialisation
- Targeted at sovereign, mission‑critical workloads in regulated sectors such as public administration, industry, and aerospace.
- Specialised for German language, reasoning, mathematics, agentic behaviour, and other production‑grade capabilities.
- Specialisation aims to improve performance on customer‑specific use cases while keeping ROI measurable.

## Sovereignty Guarantees
- Full supply‑chain transparency from data ingestion through pre‑ and post‑training to evaluation.
- Customers retain complete deployment freedom and intellectual‑property protection, ensuring compliance is an inherent property of the model.

## What Kolibri Delivers

### Foundational capabilities for enterprise and government
- Optimises the trade‑off between capability and serving cost: 3 B active parameters achieve Pareto‑optimal quality‑vs‑cost for both English and German.
- Matches or exceeds models with up to four times more active parameters on tasks such as math, coding, grounding, and long‑context processing.
- Benchmark highlights (average scores, 0–100 scale):
  - AIME 2025 (EN): 96.9 % (Kolibri) vs. 84.6 % (Qwen3.6‑35B‑A3B)
  - AIME 2025 (DE): 87.5 % vs. 82.9 %
  - GPQA (knowledge): 84.3 % (EN) and 81.3 % (DE)
  - Agentic benchmarks (banking, retail, airline, telecom) show substantial leads over competitors.
  - Coding (HumanEval+): 92.7 % vs. 92.8 % (Qwen) and 94.7 % (Nemotron)
  - Long‑context (LongBench Pro): 64.5 % vs. 70.8 % (Qwen)

### Contextualised performance for real‑world applications
- Internal, sector‑specific evaluation suites (automotive, semiconductors, German public sector, industrial drive, aerospace) show consistent gains from Kolibri Origin to Kolibri:
  - Automotive supplier: 0.72 → 0.99
  - Semiconductors: 0.35 → 0.80
  - German public sector: 0.54 → 0.75
  - Aerospace: 0.14 → 0.59
- Uses synthetic training environments to improve without exposing customer data.
- Trained with abstention data and the Merlin‑Arthur protocol, enabling the model to say “I don’t know” when information is absent from context; abstention accuracy is continuously monitored.

### Bilingual design
- Custom German/English tokenizer; 21.3 % of pre‑training tokens are native German.
- Translation used sparingly (6 % of data) to avoid cultural bias from source languages.
- Result: a genuinely bilingual model rather than an English model with incidental German exposure.

## Control and Compliance by Design
- Developed with EU AI Act, the General‑Purpose AI Code of Practice, and GDPR as core constraints; copyright compliance is a central focus.
- Full transparency of model weights and data curation decisions.
- Reasoning traces provide explainability for model decisions, supporting auditability and regulatory adherence.