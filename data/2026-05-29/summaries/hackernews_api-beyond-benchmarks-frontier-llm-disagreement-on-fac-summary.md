---
title: Beyond Benchmarks: Frontier LLM Disagreement on Fact-Checks
url: https://lenz.io/research/llm-disagreement
date: 2026-05-28
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-29T04:37:16.030827
---

# Beyond Benchmarks: Frontier LLM Disagreement on Fact-Checks

# Beyond Benchmarks: Frontier LLM Disagreement on Fact‑Checks – Summary

## 1 Frequency of disagreement across the frontier panel
- **Overall dissent:** 67 % of the 1,000 claims (672 claims; 95 % CI 64–70 %) have at least one model that disagrees with the majority or no strict majority at all.  
- **Breakdown of verdict patterns**

| Verdict pattern | Claims | Share of corpus |
|-----------------|--------|-----------------|
| All 5 agreed (unanimity) | 328 | 33 % |
| 1 of 5 dissent | 224 | 22 % |
| 2 of 5 dissent | 316 | 32 % |
| No majority (e.g., 2‑2‑1, 2‑1‑1‑1) | 132 | 13 % |
| ≥1 dissent (incl. splits) | 672 | 67 % |
| ≥2 dissent (incl. splits) | 448 | 45 % |

- **Inter‑rater reliability:** Krippendorff’s α (ordinal) = 0.639 (n = 1000, 5 raters) – indicates structured but imperfect agreement.
- **Lower bound on model error (assuming majority is correct):**
  - ≥1 model wrong on 67 % of claims.
  - ≥2 models wrong on 45 % of claims.
  - ≥3 models wrong on 13 % of claims.
  - Actual error rates are likely higher because even unanimous cases can share blind spots.

## 2 Substantive vs. nuance disagreement
- **Substantive gaps (≥2 bucket distance):** 34 % of claims (343 claims; 95 % CI 31–37 %) have at least two models whose verdicts differ by two or more buckets.
- **Bucket‑distance distribution**

| Max pairwise distance | Interpretation | Claims | Share |
|-----------------------|----------------|--------|-------|
| 0 | Full unanimity | 328 | 33 % |
| 1 | Nuance only (e.g., True ↔ Mostly True) | 329 | 33 % |
| 2 | Substantive (True ↔ Misleading, Mostly True ↔ False) | 132 | 13 % |
| 3 | Polar (True ↔ False) | 211 | 21 % |
| ≥2 | Substantive or polar | 343 | 34 % |

*Note:* Bucket distance treats the four labels as equally spaced; real‑world ambiguity may affect interpretation.

## 3 Model‑to‑model agreement
- **Highest pairwise agreement:** Gemini 3 Pro × Gemini 3 Pro + Search – 75 % (shared base model).  
- **Lowest pairwise agreement (tied):** Claude Opus 4.7 × Gemini 3 Pro, Claude Opus 4.7 × Gemini 3 Pro + Search, Gemini 3 Pro × Sonar Pro – 53 %.

| Model pair | Agreement |
|-----------|-----------|
| GPT‑5.4 ↔ Claude Opus 4.7 | 65 % |
| GPT‑5.4 ↔ Gemini 3 Pro | 65 % |
| GPT‑5.4 ↔ Gemini 3 Pro + Search | 60 % |
| GPT‑5.4 ↔ Sonar Pro | 60 % |
| Claude Opus 4.7 ↔ Gemini 3 Pro | 53 % |
| Claude Opus 4.7 ↔ Gemini 3 Pro + Search | 53 % |
| Claude Opus 4.7 ↔ Sonar Pro | 58 % |
| Gemini 3 Pro ↔ Gemini 3 Pro + Search | 75 % |
| Gemini 3 Pro ↔ Sonar Pro | 53 % |
| Gemini 3 Pro + Search ↔ Sonar Pro | 58 % |

## 4 Per‑model behavior
### 4.1 Verdict distribution per model
| Model | True | Mostly True | Misleading | False |
|-------|------|-------------|-----------|-------|
| GPT‑5.4 | 42 % (39–45 %) | 16 % (14–19 %) | 12 % (10–14 %) | 30 % (28–33 %) |
| Claude Opus 4.7 | 38 % (35–41 %) | 26 % (23–29 %) | 19 % (17–22 %) | 17 % (15–20 %) |
| Gemini 3 Pro | 54 % (51–57 %) | 3 % (2–4 %) | 3 % (2–4 %) | 40 % (37–43 %) |
| Gemini 3 Pro + Search | 52 % (49–55 %) | 4 % (3–5 %) | 9 % (7–11 %) | 35 % (32–38 %) |
| Sonar Pro | 35 % (32–38 %) | 23 % (21–26 %) | 16 % (14–18 %) | 26 % (23–28 %) |

### 4.2 Agreement with peer majority
- **Definition:** For each model, the proportion of claims where its verdict matches the strict majority (≥3 of the other 4 models) when such a majority exists.
- **Results**

| Model | Agreement with peer majority | Eligible claims (n) | Ineligible claims |
|-------|------------------------------|---------------------|-------------------|
| GPT‑5.4 | 81 % (78–84 %) | 650 | 350 |
| Claude Opus 4.7 | 70 % (67–74 %) | 691 | 309 |
| Gemini 3 Pro | 77 % (74–80 %) | 683 | 317 |
| Gemini 3 Pro + Search | 76 % (73–79 %) | 693 | 307 |
| Sonar Pro | 69 % (66–73 %) | 675 | 325 |

## 5 Domain‑level disagreement
| Domain | Claims | Any disagreement | Substantive (≥2 buckets) | No majority |
|--------|--------|------------------|----------------------------|--------------|
| Finance | 75 | 67 % (55–76 %) | 39 % (28–50 %) | 20 % (13–30 %) |
| General | 179 | 68 % (60–74 %) | 40 % (33–48 %) | 12 % (8–17 %) |
| Health | 171 | 71 % (64–78 %) | 29 % (23–36 %) | 12 % (8–17 %) |
| History | 131 | 53 % (44–61 %) | 24 % (17–32 %) | 13 % (8–20 %) |
| Legal | 48 | 77 % (63–87 %) | 40 % (27–54 %) | 19 % (10–32 %) |
| Politics | 168 | 70 % (62–76 %) | 38 % (31–46 %) | 8 % (5–13 %) |
| Science | 151 | 68 % (60–75 %) | 36 % (29–44 %) | 21 % (15–28 %) |
| Tech | 77 | 69 % (58–78 %) | 31 % (22–42 %) | 8 % (4–16 %) |

## 6 Verdict‑level panel agreement
- **Majority verdicts with strict ≥3/5 consensus:**  

| Majority verdict | Eligible claims (n) | Unanimous (5/5) | Majority only (3‑4/5) |
|------------------|---------------------|-----------------|-----------------------|
| True | 438 | 47 % (42–51 %) | 53 % (49–58 %) |
| Mostly True | 76 | 0 % (0–5 %) | 100 % (95–100 %) |
| Misleading | 74 | 5 % (2–13 %) | 95 % (87–98 %) |
| False | 280 | 43 % (37–49 %) | 57 % (51–63 %) |

- **Distribution of unanimous verdicts (all 5 models agree):**  
  - True: 204 claims (62 % of unanimous cases)  
  - Mostly True: 0 claims  
  - Misleading: 0 claims  
  - False: 124 claims (38 % of unanimous cases)

*Overall observation:* The frontier panel shows substantial disagreement, especially on nuanced or middle‑range labels, and model‑specific priors influence both verdict distribution and alignment with peers.