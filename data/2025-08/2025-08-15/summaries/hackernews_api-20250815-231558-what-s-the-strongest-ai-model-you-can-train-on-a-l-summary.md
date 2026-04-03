---
title: "What's the strongest AI model you can train on a laptop in five minutes?"
url: https://www.seangoedecke.com/model-on-a-mbp/
date: 2025-08-12
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-08-15T23:15:58.522298
---

# What's the strongest AI model you can train on a laptop in five minutes?

**The Strongest AI Model:**

From the article, it's clear that the strongest AI model that can be trained in 5 minutes on a laptop (MacBook Pro) using tiny tokens is approximately:

* ~1.8M param GPT-style transformer
* Trained on ~20M TinyStories tokens
* Reaching ~9.6 perplexity on a held-out split

This model uses the GPT-2 style transformer architecture and pushes 10,000 parameters per second.

**Market Indicators:**

The article highlights several market indicators that suggest there is strong demand for AI models like this:

* The best 5-minute model the author could train was trained in under 5 minutes.
* There are available datasets (TinyStories) with millions of tokens to use for fine-tuning a larger model.
* Users are willing and able to pay for AI model training, as evidenced by Apple's MPS token payment system.

**Technical Feasibility for a Solo Developer:**

The article provides insight into the technical feasibility of training an AI model like this solo:

* Large models (>1M param) require prohibitively long training times (~10^-8 hours or ~7,500 days).
* However, smaller models (e.g., 1M-1.5M params) can be trained in under a minute using the provided constraints.
* The author mentions that there is no "reason to think" it's possible to train a strong model in that time frame.

**Business Viability Signals:**

The article highlights several business viability signals:

* There are existing datasets (TinyStories) with available payment structures, suggesting users are willing and able to pay for AI model training.
* Apple's MPS token payment system suggests a market-ready opportunity for solo developers like the author.
* The ability to train smaller models (~1M-10k params per sec) provides options for developing business offerings catering to niche markets.

**Actionable Insights:**

Based on the analysis, actionable insights for building a profitable solo developer business are:

* Focus on fine-tuning small-scale AI models (e.g., 1-5M param) using available datasets and payment structures.
* Leverage technology like gradient accumulation and batch updates to optimize training times and efficiency.
* Develop offerings catering to niche markets that may not be well-served by traditional larger models.
* Explore alternative revenue streams, such as offering custom model development services with specific dataset requirements.

**Specific Numbers:**

* The highest-performing model used in the article (GPT-2) trains at ~4000 tokens per second. This suggests that training even a single 1M-5M param model is computationally demanding.
* Apple's MPS token payment system charges an undisclosed fee for each token, suggesting that developers can train models for a small upfront cost.
* The author mentions they were able to move lots of tokens (~20-40 million) through their tiny 10k-param model, but noted that the training time is only sufficient for 4 million tokens.
