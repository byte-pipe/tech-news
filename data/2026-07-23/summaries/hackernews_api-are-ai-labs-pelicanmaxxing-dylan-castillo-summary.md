---
title: Are AI labs pelicanmaxxing? – Dylan Castillo
url: https://dylancastillo.co/posts/pelicanmaxxing.html
date: 2026-07-23
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-07-23T18:59:34.865237
---

# Are AI labs pelicanmaxxing? – Dylan Castillo

# Are AI labs pelicanmaxxing? – Dylan Castillo

## How the test was conducted
- Built 48 prompts by crossing 8 animals (pelican, flamingo, heron, otter, raccoon, antelope, whale, cat) with 6 vehicles (bicycle, unicycle, skateboard, scooter, plane, boat).  
- Generated 3 samples per prompt (temperature 1.0) from seven frontier models via OpenRouter: GPT‑5.6 Terra, Claude Sonnet 5, Gemini 3.5 Flash, Grok 4.5, Qwen 3.7‑Max, GLM‑5.2, DeepSeek V4 Pro – total 1,008 SVGs.  
- Pipeline:  
  1. Render each SVG to PNG; retry only 11 times when rendering failed.  
  2. Judge each image with GPT‑5.6 Luna, rating animal, vehicle, and action coherence on a 1‑5 scale; the average of the three ratings is the “judge score”.  
  3. Run Gemini 3.1 Flash‑Lite on the PNGs to extract recognized animal, vehicle, orientation, and scene elements.  

## Main findings
- **Visual inspection**: No model’s pelican‑on‑a‑bicycle images appeared noticeably better than its other animal‑vehicle outputs.  
- **Animal performance**: Across all models, pelicans ranked 6th of 8 in mean animal rating (behind cat, whale, raccoon, heron, antelope).  
- **Vehicle performance**: Bicycles ranked second‑to‑last (tied with planes); many bicycle images missed wheels, frame, or pedals.  
- **Combined combo ranking**: The “pelican + bicycle” pair placed 42nd of 48 combos when raw scores were ordered.  
- **Difficulty‑adjusted regression**:  
  - Lab‑specific pelican effects ranged from –0.11 to +0.14 judge points; none were statistically significant.  
  - Lab‑specific bicycle effects ranged from –0.18 (Grok 4.5) to +0.27 (Gemini 3.5 Flash); only Gemini’s bicycle boost reached p < 0.05.  
  - No significant extra boost for the pelican‑bicycle cell; the largest (+0.35 for GLM‑5.2) had p = 0.12.  
  - After Bonferroni correction for 21 tests, no effect remained significant.  

## Interpretation
- The data provide no evidence that any of the seven frontier labs are “pelican‑maxxing” their models.  
- Superior scores on the benchmark align with overall model quality rather than targeted optimization.  
- The single marginal bicycle boost (Gemini 3.5 Flash) is consistent with random variation given multiple comparisons.  

## Additional notes
- The “plane” prompt was ambiguous; models often rendered a flat shape instead of an aircraft, leading to lower vehicle scores and occasional missing vehicle detections.  
- All code, data, and full statistical tables are publicly available in the GitHub repository linked in the article.