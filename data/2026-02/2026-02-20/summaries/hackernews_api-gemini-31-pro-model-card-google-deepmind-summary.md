---
title: Gemini 3.1 Pro - Model Card — Google DeepMind
url: https://deepmind.google/models/model-cards/gemini-3-1-pro/
date: 2026-02-20
site: hackernews_api
model: gemma3n:latest
summarized_at: 2026-02-20T06:03:31.631343
---

# Gemini 3.1 Pro - Model Card — Google DeepMind

# Gemini 3.1 Pro

Gemini 3.1 Pro is the latest iteration in the Gemini 3 series, Google's most advanced natively multimodal reasoning model as of February 2026. It excels at comprehending vast datasets from various modalities including text, audio, images, video, and code repositories.

## Model Info

### Description
Gemini 3.1 Pro is a highly capable model for complex tasks, understanding diverse and extensive multimodal information.
### Model Dependencies
Based on Gemini 3 Pro.
### Inputs
Accepts text, images, audio, and video files with a context window of up to 1M tokens.
### Outputs
Generates text with a 64K token output limit.
### Architecture
Based on Gemini 3 Pro.
## Model Data

### Training Dataset
Based on Gemini 3 Pro.
### Training Data Processing
Details available in the Gemini 3 Pro model card.
## Implementation and Sustainability

### Hardware
Based on Gemini 3 Pro. Details on hardware and sustainability are in the Gemini 3 Pro model card.
### Software
Based on Gemini 3 Pro. Details on software are in the Gemini 3 Pro model card.
## Distribution

Available through: Gemini App, Google Cloud / Vertex AI, Google AI Studio, Gemini API, Google Antigravity, NotebookLM. Accessible via API with terms of use. No specific hardware or software required. Refer to Gemini API and Vertex AI documentation for details.
## Evaluation

### Approach
Evaluated across benchmarks including reasoning, multimodal capabilities, agentic tool use, multilingual performance, and long context. Detailed methodology and results are available at deepmind.google/models/evals-methodology/gemini-3-1-pro.
### Results
Significantly outperforms Gemini 3 Pro on various benchmarks requiring enhanced reasoning and multimodal capabilities. Notable improvements observed in areas like academic reasoning, search, abstract reasoning, scientific knowledge, agentic coding, and long-horizon professional tasks.

| Benchmark                     | Gemini 3.1 Pro | Gemini 3 Pro |
|-------------------------------|----------------|--------------|
| Thinking (High)               | Sonne 4.6      | Opus 4.6     |
| Thinking (Max)                | —              | —            |
| Thinking (xhigh)               | —              | —            |
| Humanity's Last Exam          | —              | —            |
| Academic reasoning (full set) | 44.4%          | 37.5%        |
| Search (blocklist) + Code     | 51.4%          | 45.8%        |
| ARC-AGI-2                     | 77.1%          | 31.1%        |
| GPQA Diamond                   | 94.3%          | 91.9%        |
| Terminal-Bench 2.0            | 68.5%          | 56.9%        |
| SWE-Bech Verified              | 80.6%          | 76.2%        |
| SWE-Bech Pro (Public)         | 54.2%          | 43.3%        |
| LiveCodeBench Pro              | Elo 2887       | Elo 2439     |
| SciCode                        | 59%            | 56%          |
| APEX-Agents                    | 33.5%          | 18.4%        |
| GDPval-AA Elo                  | 1317           | 1195         |
| τ2-bench                       | Retail: 90.8%   | Retail: 85.3% |
|                               | Telecom: 99.3%   | Telecom: 98.0% |
| MCP Atlas                       | 69.2%          | 54.1%        |
| BrowseComp                      | 85.9%          | 59.2%        |
| MMMU-Pro                        | 80.5%          | 81.0%        |
| MMMLU                           | 92.6%          | 91.8%        |
| MRCR v2 (8-needle)             | 128k: 84.9%    | 84.9%        |
|                                | 1M: 26.3%       | Not supported |
## Intended Usage and Limitations

### Benefit and Intended Usage
Suitable for agentic performance, advanced coding, long context and multimodal understanding, and algorithmic development.
### Known Limitations
Refer to the Gemini 3 Pro model card for known limitations.
### Acceptable Usage
Refer to the Gemini 3 Pro model card for acceptable usage guidelines.
## Ethics and Content Safety

### Evaluation Approach
Details available in the Gemini 3 Pro model card.
### Safety Policies
Details available in the Gemini 3 Pro model card.
### Training and Development Evaluation Results
Gemini 3.1 Pro demonstrates improvements in safety and tone compared to Gemini 3.0 Pro, with low unjustified refusals. Safety evaluations align with the original Gemini 3.0 Pro assessment.
