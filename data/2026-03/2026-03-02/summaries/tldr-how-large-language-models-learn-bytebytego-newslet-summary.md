---
title: How Large Language Models Learn - ByteByteGo Newsletter
url: https://blog.bytebytego.com/p/how-large-language-models-learn
date: 2026-03-02
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-03-02T08:25:50.410788
---

# How Large Language Models Learn - ByteByteGo Newsletter

# How Large Language Models Learn

## The Misconception of “Learning”
- The term suggests human‑like understanding, but LLMs only perform massive repetitive mathematical updates.
- They excel at mimicking text patterns rather than truly reasoning or comprehending concepts.
- Recognizing this limits misplaced trust and explains both convincing outputs and surprising failures.

## The Foundation: Loss Functions
- A loss function provides a single numeric score of how wrong the model is; training aims to minimize this score.
- **Three essential properties**
  1. **Specificity** – measures a concrete task (e.g., predicting the next word) rather than vague notions like “intelligence.”
  2. **Computability** – can be calculated quickly and repeatedly on large datasets.
  3. **Smoothness** – changes gradually with model parameters, allowing gradient‑based optimization.
- Accuracy is not smooth; therefore LLMs optimize **cross‑entropy loss**, which is smooth and mathematically tractable.
- The model is rewarded for reproducing patterns in the training data, not for factual correctness; frequent falsehoods in the data lead to confident but wrong statements.

## The Process: Gradient Descent
- Gradient descent adjusts billions of parameters to reduce the loss, analogous to rolling a ball downhill on a hilly landscape.
- **Steps**
  1. Initialize parameters randomly (ball’s starting position).
  2. Compute the local slope (gradient) of the loss surface.
  3. Move parameters a tiny step downhill.
  4. Repeat billions of times until reaching a low‑loss valley.
- The method is greedy: each step uses only immediate slope information, without looking ahead to deeper valleys.
- Full exhaustive search is computationally impossible; gradient descent offers a tractable approximation.
- Modern training uses **Stochastic Gradient Descent (SGD)**:
  - Loss is estimated on small random batches rather than the entire dataset.
  - Enables training on massive corpora with limited memory and often yields better convergence.

## The LLM Secret: Next‑Token Prediction
- The core training objective is to predict the next token (word or sub‑word piece) given the preceding context.
- For each position, the model outputs a probability distribution over the entire vocabulary.
- During generation, a token is sampled (or selected) from this distribution, appended to the context, and the process repeats.
- This simple objective, repeated billions of times, gives rise to the model’s ability to produce coherent paragraphs, answer questions, and perform many downstream tasks.
