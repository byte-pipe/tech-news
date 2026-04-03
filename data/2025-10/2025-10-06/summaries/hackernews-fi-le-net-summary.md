---
title: fi-le.net
url: https://fi-le.net/oss/
date: 2025-10-06
site: hackernews
model: llama3.2:1b
summarized_at: 2025-10-06T11:20:32.893606
screenshot: hackernews-fi-le-net.png
---

# fi-le.net

### The Fiefdom of Files: An Analysis on OpenAI's Training Data and GPT-5

**What**: OpenAI recently released their open-source model, GPT-5. This experiment aims to demonstrate the connection between GPT-5 training data sources and its parameters.

**Key Points**:

*   The original text describes how the weights and parameters of GPT-5 were extracted from an unpublicated "text-only dataset".
*   The dataset includes a wide range of texts, including academic articles, books, and news.
*   A sample analysis is performed on a subset of this dataset to extract valuable information about the training data source.
*   Techniques such as tokenizer identification and histogram analysis are applied to study the L2 norm of tokens in the embedding matrix.

**Understanding the Context**:
The text appears to provide insights into how OpenAI's GPT-5 model collects its training data, revealing some hidden patterns that might reveal more about the original dataset. This raises questions about the origins and implications of this process.

*   The use of the **GGBK (GBK) encoding** for "境" in Mandarin, indicating Chinese translations related to borders
*   The presence of a specific byte sequence "門" in UTF-8 could potentially hint at data leakage from other regions or sources.
