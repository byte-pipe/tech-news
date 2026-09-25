---
title: (iterate think thoughts): Introducing Lev
url: https://yogthos.net/posts/2026-09-24-introducing-lev.html
date: 2026-09-25
site: tldr
model: llama3.2:1b
summarized_at: 2026-09-25T15:46:50.091406
---

# (iterate think thoughts): Introducing Lev

# Introducing Lev

## Overview

A chat model called Jev was released by TypeSafe, and its demo of playing Doom in real-time showed promising results. Jev is a hosted classifier model that takes unstructured input and produces typed probabilities in one pass, with a single response time of a few hundred milliseconds. The model's primary function is to make decisions based on the input, with the ability to recognize tasks that involve deciding things, such as deciding a question or performing a task.

## How Jev Works

Jev is an LLM (Language Model) that reads input from left to right, commits to each token, and generates an answer token by token. For a non-fast decision engine like Lev, each option gets a marker token placed in the sequence next to the option's text after the forward pass. This allows for efficient encoding and processing of options. The forward pass generates scores for each option, and a softmax is applied to get a probability for every option simultaneously.

## Benchmark Performance

Benchmark tests have shown that open weights models running on user hardware can often outperform Jev. Jev's performance can be measured independently in several benchmarks, including those related to the decision engine tier. With a fast classifier, such as Lev, some of these benchmarks suggest that the model may not be able to keep up with demands for fast answers.

## The System One Model Concept

System One models refer to a type of language model that is designed to perform well on tasks such as deciding questions, but struggling with tasks that require a lot of context and understanding of the situation. This is in contrast to Fast AutoMinds, which focus on fast and accurate decision making but often perform poorly on tasks that require a lot of context.

## Overview and Comparison

This post provides a comprehensive overview of how Lev works, its performance benchmark, and the concept of System One models. It also compares these models to the idea of chat models like Jev. As an interested reader of Jev, building an open weights model like Lev shows the potential for faster and more accurate decision engines in future projects or applications that require reliable, high-confidence answers.

## Key Points

* Jev is a hosted classifier model that takes unstructured input and produces typed probabilities in one pass.
* Jev is able to perform reliably under a few hundred milliseconds with open weights models that don't rely on reinforcement learning.
* System One models are designed to be fast for decisions that require minimal context but struggle on tasks that require a lot of context.
* Lev is an LLM that processes input left to right and allows for efficient encoding and processing of options.
* The forward pass generates scores for each option, and a softmax is applied to get a probability for every option simultaneously.

## Structured Output

Here is a summary of the key points:
### Introduction

* Jev is a hosted classifier model developed by TypeSafe.
* September 24, 2023
### Overview

* Jev is a chat model that can perform decisions based on unstructured input.
* The primary function of Jev is to generate typed probabilities in one pass.
### How Jev Works

* Jev reads input from left to right and commits to each token.
* Each option gets a marker token placed in the sequence next to the option's text after the forward pass.
* A softmax is applied to get a probability for every option simultaneously.

### Benchmark Performance

* Levenshine (Lev) is a fast classifier model that excels at fast answers.
* Benchmarks suggest that Jev may not perform as well on tasks that require a lot of context.

### System One Model Concept

* System One models are designed to perform well on deciding questions but struggle with tasks that require a lot of context.
* Modern language models like ModernBERT are better suited for open-ended work.

### Overview and Comparison

* This post provides a comprehensive overview of how Lev works, its performance benchmark, and the concept of System One models.
* As an interested reader of Jev, building an open weights model like Lev shows the potential for faster and more accurate decision engines in future projects or applications that require reliable, high-confidence answers.