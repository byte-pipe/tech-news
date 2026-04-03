---
title: A small number of samples can poison LLMs of any size \ Anthropic
url: https://www.anthropic.com/research/small-samples-poison
date: 2025-10-09
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-10-10T11:14:10.712730
screenshot: hackernews_api-a-small-number-of-samples-can-poison-llms-of-any-s.png
---

# A small number of samples can poison LLMs of any size \ Anthropic

# A small number of samples can poison LLMs of any size

Oct 9, 2025
Read the paper

Preventing large language models (LLMs) from behaving maliciously is a growing concern due to their widespread adoption in various applications such as customer service chatbots and virtual assistants. Researchers have long assumed that having control over a percentage of training data would be sufficient to prevent poisoning attacks.

A new study with the UK AI Security Institute and the Alan Turing Institute found, however, that even a small number of poisoned documents can compromise LLMs, regardless of their size or training data volume. The researchers experimented on two different models: one trained on 13 billion parameters (with over 20 times more training data) than another with 600 million parameters.

The findings demonstrate that poisoning attacks are more practical and effective than previously assumed. This discovery challenges the common assumption that attackers need control of a majority of the training data to avoid LLM poisoning.

## Key Points

* A small number of poisoned documents can compromise large language models
* Researchers used two different models with varying training data volumes for each experiment
* The study found similar results regardless of model size or training data volume
* Poisoning attacks can be more effective than previously assumed
