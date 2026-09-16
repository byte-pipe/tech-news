---
title: GitHub - GraafHenk/numberwang: A small neural network that decides whether a number is Numberwang. · GitHub
url: https://github.com/GraafHenk/numberwang
date: 2026-09-16
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-17T05:39:47.613311
---

# GitHub - GraafHenk/numberwang: A small neural network that decides whether a number is Numberwang. · GitHub

# Numberwang Repository Overview

## Description
- Small neural network that determines whether a given input is “Numberwang”.
- Model stored as a 1.8 MB JSON file; inference code is pure Python (≈100 lines) with no external libraries required.

## Usage
- Clone the repo and run:
  ```bash
  python3 numberwang.py 22
  ```
- Without arguments, starts an interactive session accepting numbers, words, arithmetic, etc.
- Requires Python 3.8+ only.

## API
- `load_model("model.json")` loads the network.
- `wang_probabilities(model, input_string)` returns probabilities for the four possible verdicts:
  0 – “That's not Numberwang.”  
  1 – “THAT'S NUMBERWANG!”  
  2 – “That's not even a number. It can never be Numberwang.”  
  3 – “That's Wangernumb!”

## Accepted Input Types
- **Digits or words** in eleven languages (e.g., `42`, `sixty‑six`, `zweiundzwanzig`).
- **Arithmetic expressions** (e.g., `5*2`, `96 divided by 2`); verdict based on the result.
- **Negatives, decimals, currency, units, times** (e.g., `-7`, `£5`, `9:30`).
- **Roman numerals and ordinals** (e.g., `XLIV`, `22nd`).
- **Number‑related words** (e.g., `fortnight`, `vierendelen`).
- **Fictional numbers** (treated as numbers).
- **Non‑numeric text** (always “not Numberwang”).

## Model Architecture
- Character‑level pipeline:  
  `Embedding(32) → Conv1d(128, k=3) → ReLU → Conv1d(128, k=3) → ReLU → Global Max Pool → Linear(128) → ReLU → Linear(4) → Softmax`
- Contains 80,804 parameters; all language and rule knowledge is encoded in the weights.

## Demo
- Hosted on Hugging Face Spaces.
- Local demo requires `gradio` (installed via `pip install -r requirements.txt`) and running `python3 app.py`.

## Performance
- Overall accuracy: 88.9 % (macro‑F1 0.896) on 486 held‑out adjudications.
- Class‑wise scores:
  - Not Numberwang: precision 0.820, recall 0.885, F1 0.851
  - Numberwang: precision 0.919, recall 0.900, F1 0.910
  - Not a number: precision 0.951, recall 0.830, F1 0.886
  - Wangernumb: precision 0.968, recall 0.909, F1 0.937
- Weakness: arithmetic on unseen operands (44–72 % accuracy); the network memorises common expressions rather than computes them.

## License
- MIT License (see `LICENSE`). No warranty regarding the correctness of any Numberwang verdict.