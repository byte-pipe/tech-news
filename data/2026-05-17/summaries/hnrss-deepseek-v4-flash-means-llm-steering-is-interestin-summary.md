---
title: DeepSeek-V4-Flash means LLM steering is interesting again
url: https://www.seangoedecke.com/steering-vectors/
date: 2026-05-16
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-05-17T06:02:09.224399
---

# DeepSeek-V4-Flash means LLM steering is interesting again

# DeepSeek‑V4‑Flash means LLM steering is interesting again

## Overview
- The author is fascinated by “steering”: directly manipulating a model’s internal activations during inference to guide its output.  
- Recent open‑source work (antirez’s DwarfStar 4, a stripped‑down llama.cpp running DeepSeek‑V4‑Flash) makes local steering practical for many engineers.  

## DeepSeek V4‑Flash & DwarfStar 4
- DeepSeek‑V4‑Flash appears strong enough to compete with low‑end frontier models on agentic coding tasks.  
- DwarfStar 4 integrates steering as a first‑class feature, though the current implementation is a simple “verbosity” example.  
- The project was released only eight days ago; the author plans to follow its development closely.  

## How steering works
- **Basic idea:** extract a concept (e.g., “respond tersely”) from the model’s activation pattern, then add the corresponding “steering vector” to activations at inference time.  
- **Naïve method:** run the same prompts with and without a phrase like “respond tersely”, subtract the activation matrices to obtain the steering vector, and apply it to new prompts.  
- **More sophisticated method:** train a secondary model (e.g., a sparse autoencoder) to discover recurring activation features, map those to concepts, and boost them—similar to Anthropic’s approach.  

## Why steering is appealing
- It acts like a “cheat code” that could turn a “smart” dial in the model without extensive retraining.  
- Could replace prompt engineering with a control panel of sliders (verbosity, conscientiousness, speed, etc.).  
- Provides a compelling, almost neurological, way to think about modifying a model’s “mind”.  

## Why steering hasn’t been widely adopted
- Large labs can directly modify their models during training, making steering unnecessary for them.  
- Most users access LLMs via APIs and lack the weights or activation access required for steering; only the model owners could expose steering vectors.  
- Simple prompting already achieves many of the effects steering promises, and prompt tokens themselves manipulate activations finely.  

## Potential high‑impact uses
- **Unpromptable concepts:** steering might affect traits that prompts can’t elicit (e.g., “intelligence” or deep domain knowledge). The author is skeptical, noting such concepts may span most of the model’s weights, essentially requiring full retraining.  
- **Data compression:** a steering vector could encode a large amount of information (e.g., knowledge of a specific codebase) that would otherwise consume many context tokens, shifting it from working memory to implicit memory. This may also require a full fine‑tune to be effective.  

## Conclusion
- The author remains cautious: most gains from steering can be replicated with clever prompting, and ambitious steering goals may be more efficiently achieved by training or fine‑tuning.  
- However, the open‑source community has barely explored steering; upcoming releases of strong open‑weight models could spark a wave of tools and “boostable feature” libraries.  
- The next six months may reveal whether steering becomes a practical technique or stays a niche curiosity.