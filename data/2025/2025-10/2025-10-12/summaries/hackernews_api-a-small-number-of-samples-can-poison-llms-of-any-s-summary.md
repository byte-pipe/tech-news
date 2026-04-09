---
title: A small number of samples can poison LLMs of any size \ Anthropic
url: https://www.anthropic.com/research/small-samples-poison
date: 2025-10-09
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-10-12T11:14:01.112834
screenshot: hackernews_api-a-small-number-of-samples-can-poison-llms-of-any-s.png
---

# A small number of samples can poison LLMs of any size \ Anthropic

# A small number of samples can poison LLMs of any size

## Introduction

A recent study has found that as few as 250 malicious documents can produce a "backdoor" vulnerability in large language models, regardless of model size or training data volume.

## Background

Large language models like Claude are pretrained on enormous amounts of public text from across the internet. While this pretraining process ensures diversity in the training data, it also exposes models to the risk of malicious actors injecting specific text into online content to gain undesirable behaviors.

## Malicious Attack: Backdoors

A malicious attack can be introduced to manipulate a model by inserting arbitrary phrases into prompts that trigger specific behaviors.

## Research Methodology

The study used simple backdoor attacks designed to trigger low-stakes behaviors in early language models and found that poisoning attacks require a near-constant number of documents regardless of model size or training data volume, despite the potential for large-scale evaluations to minimize instances of poisoned content.

## Results

*   The smallest sample size (250) resulted in significant backdoor vulnerabilities
*   Even 13B parameter models, trained with over 20 times more data than smaller models, were found to be vulnerable
*   There may have been some "dilution" effect due to the diversity of training data
