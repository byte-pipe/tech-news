---
title: A small number of samples can poison LLMs of any size \ Anthropic
url: https://www.anthropic.com/research/small-samples-poison
date: 2025-10-09
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-10-11T11:11:37.476612
screenshot: hackernews_api-a-small-number-of-samples-can-poison-llms-of-any-s.png
---

# A small number of samples can poison LLMs of any size \ Anthropic

# A Small Number of Samples Can Poison Large Language Models of Any Size

## Study Finds Backdoors in Pre-Trained LLMs Are More Convenient Than Thought

While large language models like Claude are trained on vast amounts of public text, they can still be poisoned with small samples, making them a more practical risk for attackers.

## The Risk of Data-R poisoning Attacks

Malicious actors can inject specific text into online content to poison large language models. This process is known as data-poisoning, and it includes examples like exfiltrating sensitive data by including harmless phrases in the prompt.

## A Previous Study's Limitations

Previous research on LLM poisoning has been limited in scale due to the computational resources required for pretraining and larger-scale evaluations of attacks. Additionally, existing work assumed that adversaries controlled a percentage of the training data, making it unrealistic.

## The New Study Finds:

*   A small number of poisoned documents (250) can create vulnerabilities in large language models.
*   These vulnerabilities can affect any size model, not just 13B-parameter ones.
*   Poisoning attacks require a relatively constant number of documents rather than varying over time or size.
*   This finding challenges the previous assumptions and highlights the potential risks associated with data-poisoning attacks.
