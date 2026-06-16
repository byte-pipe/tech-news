---
title: Finding Optimal Tokenizers
url: https://blog.aqnichol.com/2026/06/10/optimal-tokenizers/
date: 2026-06-16
site: tldr
model: llama3.2:1b
summarized_at: 2026-06-16T12:46:11.010425
---

# Finding Optimal Tokenizers

## Frontier Text Tokenizers: A Comprehensive Solution

This post introduces a novel approach to tackling the theoretically difficult task of optimal tokenization. By leveraging integer linear programming, researchers have developed an algorithm that can compute an optimal tokenizer in various scenarios.

**Theoretical Intractability**

The problem of tokenization is inherently complex due to its theoretical intractability. However, by applying cutting-edge techniques such as cutting-planerotechniques, it is possible to solve practical instances with reasonable efficiency.

*   **Existing State-of-the-Art**: The existing state-of-the-art was previously close to optimal (e.g., within 1%).
*   **Tokenization Generalizability**: Although optimal tokenization can generalize well on training data, its performance may degrade when evaluated on held-out test data.
*   **Efficient Tokenizers**: Inefficient tokenizers are generally acceptable due to their simplicity. This can be paid for in terms of vocabulary size, making the difference negligible.

## Background: Tokenizers

Frontier LLMs typically receive inputs as a sequence of integers representing tokens. Each token represents a sequence of bytes that corresponds to common words. For instance, in the GPT-5 tokenizer, each token references the corresponding byte sequence "the" or "+ "to", such that a valid input can be encoded as the concatenation [290, 6602].

**Vocabulary Mapping**

The mapping from tokens to bytes is fixed before training the LLM. The goal is often to find a vocabulary size that minimizes the number of required tokens for encoding data. A key technique in this process is called byte-pair encoding (BPE), an efficient compression algorithm.

## Tokenization as Linear Programming

A novel approach exists that reduces tokenization to integer linear programming, enabling us to solve problems with improved efficiency and accuracy. This formulation involves representing the entire dataset's tokenization as a set of integer variables. The color variable for each possible vocabulary entry is crucial in this endeavor:

*   **Color Variables**: These variables represent uniqueness in substrings across the input data.
*   **Edge Variables**: For each substring, there's an edge variable, and these are used to encode actual tokens.

Objective: Minimize the sum of all edge variables, representing token usage for different characters throughout the dataset. In other words, this algorithm leverages a single optimization approach with numerous benefits, including improved efficiency and better handling of datasets that contain common patterns or typos. By breaking down complex problems into simpler components and implementing optimization techniques, researchers have made significant strides in tackling the daunting task of optimal tokenization.