---
title: microgpt
url: http://karpathy.github.io/2026/02/12/microgpt/
date: 2026-02-15
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-15T06:02:16.346397
---

# microgpt

# microgpt: A Minimalist GPT Implementation

This document outlines the `microgpt` project, a single-file (200 lines of Python) implementation of a GPT-2-like language model. The project's goal is to simplify the core components of large language models (LLMs) to their essential elements.

## Key Features

*   **Single-file implementation:** All code resides within a single Python file (`microgpt.py`) with no external dependencies.
*   **Minimalist design:**  Focuses on the fundamental algorithmic components of an LLM.
*   **GPT-2-like architecture:**  Employs a neural network architecture inspired by GPT-2.
*   **Auto-differentiation:** Implements automatic differentiation for gradient calculation.
*   **Dataset:** Uses a dataset of 32,000 names for demonstration.
*   **Tokenization:**  Employs a simple tokenization scheme assigning integer IDs to unique characters.

## Components

### Dataset

*   The dataset consists of a list of strings, where each string represents a document (e.g., a name).
*   The example dataset uses 32,000 names, one per line, sourced from a GitHub repository.
*   The model learns patterns from this data and generates new, plausible-sounding names.

### Tokenizer

*   Converts text into a sequence of integer token IDs and back.
*   Uses a simple tokenizer that assigns a unique integer ID to each character in the dataset.
*   Includes a special "BOS" (Beginning of Sequence) token to mark the start and end of documents.

### AutoGrad

*   Implements automatic differentiation to calculate gradients for training.
*   Uses a `Value` class to represent the computational graph and track data and gradients.
*   The `Value` class supports basic arithmetic operations and the ReLU activation function.
*   The `backward` function performs backpropagation to calculate gradients.

## Overall Process

1.  **Dataset Preparation:** Loads and preprocesses the text data into a list of documents.
2.  **Tokenization:** Converts the text data into a sequence of token IDs.
3.  **Model Definition:** Defines the GPT-2-like neural network architecture.
4.  **Training:** Trains the model using the prepared dataset and the auto-differentiation engine.
5.  **Inference:** Uses the trained model to generate new text.

## Resources

*   **Source Code:** [https://github.com/karpathy/microgpt](https://github.com/karpathy/microgpt)
*   **Web Page:** [https://karpathy.ai/microgpt.html](https://karpathy.ai/microgpt.html)
*   **Google Colab Notebook:** Available on the web page.
*   **Micrograd Video:** A 2.5-hour video explaining the auto-differentiation implementation: [https://www.youtube.com/watch?v=9-e-J-j-W-I](https://www.youtube.com/watch?v=9-e-J-j-W-I)
