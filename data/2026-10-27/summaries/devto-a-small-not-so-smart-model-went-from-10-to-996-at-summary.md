---
title: "A small, not-so-smart model went from 10% to 99.6% at reading property deeds for $1.15, and it says 'check this line' instead of bluffing - DEV Commun..."
url: https://dev.to/advikdivekar/a-small-not-so-smart-model-went-from-10-to-996-at-reading-property-deeds-for-115-and-it-says-490k
date: 2026-10-25
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-10-27T08:19:01.955345
---

# A small, not-so-smart model went from 10% to 99.6% at reading property deeds for $1.15, and it says 'check this line' instead of bluffing - DEV Commun...

# A small, not‑so‑smart model went from 10 % to 99.6 % at reading property deeds for $1.15, and it says “check this line” instead of bluffing

## What the project does
- DeedReader takes a metes‑and‑bounds legal description, parses it with a fine‑tuned Qwen‑3‑8B LoRA, and draws the parcel on a real satellite map.  
- If the geometry does not close, the system refuses to draw, flags **NEEDS HUMAN REVIEW**, points to the offending line, and suggests a one‑digit correction.  
- Outputs include acres, perimeter, closure ratio, and export options (DXF, GeoJSON, SVG).  
- All processing runs offline from a 369 MB adapter; no network or per‑deed fee is required.

## Key results (synthetic test deeds)
| Metric | In‑distribution (60 deeds) | Out‑of‑distribution (3 000 deeds) |
|--------|---------------------------|-----------------------------------|
| Exactly correct reads | 10 % (6/60) | 99.6 % (2 988/3 000) |
| Flagged for human review | 82 % | 0.4 % |
| Silent errors (wrong & unflagged) | 5 % (5/60) | 0.07 % (2/3 000) |
| 95 % CI for accuracy on 3 000 deeds | – | 99.3 % – 99.8 % |

## Training cost and efficiency
- Total expense ≈ $1.15 for 15 minutes of LoRA training on Tinker data.  
- $0.17 of training already yields 99.4 % accuracy.  
- Full project (including baselines and evaluations) cost ≈ $3.80.

## Safety and reliability
- Five independent checks must agree before an answer is shown as confident: parsing success, parcel closure, one‑number‑per‑sentence, landmark‑sentence consistency, and agreement with a separate regex parser.  
- Across 3 000 fresh deeds, 10 of 12 imperfect outputs were caught by the closure and parsing checks; the remaining two were label quirks in the generator.  
- No silent errors remained after the checks on the large test set.

## How it works
1. **Model reading** – a LoRA‑fine‑tuned Qwen‑3‑8B converts prose into structured calls (bearing, distance, curve, landmark).  
2. **Deterministic code** – plain Python performs all arithmetic, unit conversion, and closure testing.  
3. **Multiple validation layers** – the five checks listed above ensure consistency before presenting results.  
4. **Error handling** – when validation fails, the UI highlights the problematic line and proposes a one‑digit fix (e.g., 103.2 → 130.2).

## Demo highlights
- Paste a deed description → instant parcel drawing with true bearings.  
- Click a sentence → corresponding side lights up on the map; click a side → sentence highlights.  
- Export with one click to CAD/GIS formats.  
- Simulated misread shows red banner, flagged line, and suggested correction.

## Why it matters
- Traditional manual survey work takes 15–30 minutes per deed; a single digit error can silently corrupt downstream processes.  
- Existing regex parsers handle only clean numeric formats and give no warning on mistakes.  
- DeedReader offers a fast, offline, and trustworthy alternative that prefers “I don’t know” over silent wrong answers, embodying the “slow and steady” principle.