---
title: Rio-3.5-Open-397B ≈ 0.6 x Nex-N2_pro + 0.4 x Qwen · Issue #4 · nex-agi/Nex-N2 · GitHub
url: https://github.com/nex-agi/Nex-N2/issues/4
date: 2026-06-14
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-15T06:02:15.287839
---

# Rio-3.5-Open-397B ≈ 0.6 x Nex-N2_pro + 0.4 x Qwen · Issue #4 · nex-agi/Nex-N2 · GitHub

# Summary of Issue “Rio-3.5-Open-397B ≈ 0.6 x Nex-N2_pro + 0.4 x Qwen”

## Claim
- The model presented as “Rio‑3.5‑Open‑397B” (claimed to be an original 397B model trained by IplanRIO) is actually a direct element‑wise merge of the Nex‑N2_pro model and the official Qwen‑3.5‑397B‑A17B base model, weighted approximately 60 % Nex and 40 % Qwen.

## Evidence Presented
- **System‑prompt test**  
  - After removing Rio’s hard‑coded “You are Rio” system prompt, the deployed model identifies itself as “Nex, from Nex‑AGI” in 79 % of queries and never as “Rio”.  
  - It also recites Nex‑AGI’s bespoke backstory word‑for‑word.
- **Weight‑tensor analysis**  
  - Every weight tensor across all 60 layers matches a 0.6/0.4 blend of Nex and Qwen to thousands of standard deviations.  
  - No other fine‑tuning patterns are observable; the blend is consistent throughout the network.

## Conclusion
- There is no evidence of independent training for Rio‑3.5‑Open‑397B; the model is effectively a weighted interpolation of Nex‑N2_pro and Qwen.