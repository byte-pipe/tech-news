---
title: What Even Is AI? (I Took a Break & Had to Relearn Everything) - DEV Community
url: https://dev.to/aws/what-even-is-ai-i-took-a-break-had-to-relearn-everything-3dpj
date: 2026-05-05
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-05-06T11:32:28.697368
---

# What Even Is AI? (I Took a Break & Had to Relearn Everything) - DEV Community

# What Even Is AI? (I Took a Break & Had to Relearn Everything)

## Overview
- Returned from maternity leave and felt like AI had advanced a decade in six months.  
- Decided to rebuild an AI mental model from first principles and share the journey publicly.  
- No heavy math or expert‑level coding; focus on real problems, architecture, and honest notes on failures.

## Demo: Adapting a Recipe in Under a Minute
- Used Amazon Bedrock Playground with a real recipe and asked three progressively deeper questions:  
  1. **Summarize** the core techniques, stripping away fluff.  
  2. **Interpret** the recipe to identify the most likely point of failure for a first‑time cook.  
  3. **Personalize** the recipe for six people, including vegan and gluten‑free requirements, and generate a shopping list and timeline.  
- Demonstrated how an LLM can turn a task that would take twenty minutes into a ten‑second response.

## Core Concepts
- **AI** – the broad umbrella covering recommendation engines, fraud detection, generative tools, etc.  
- **Foundation Models** – large pretrained models (text, image, video, speech, code) that can be adapted for many tasks.  
- **LLMs (Large Language Models)** – a subset of foundation models specialized for language tasks.  
- Simple hierarchy: AI → Foundation Models → LLMs.  
- Interaction flow: *Input (prompt) → Foundation Model → Output (response)*.  
- Calls are simple HTTP requests with text in and text out; the complexity resides in the pre‑training data.

## Limitations
- Models predict plausible answers but do not know if they are correct.  
- They can “hallucinate” – produce confident‑sounding but false information.  
- Essential habit: always double‑check any output before trusting it.

## Platform: Amazon Bedrock
- Bedrock hosts multiple foundation models (Anthropic’s Claude, Meta’s Llama, Mistral, Amazon’s own models) accessible via API.  
- The Playground offers a quick UI; later posts will show programmatic usage from code.

## Author’s Stack
- Works at AWS, so uses AWS tools: Bedrock for models and the AI‑powered IDE Kiro for building.  
- Concepts such as tokens, context windows, Retrieval‑Augmented Generation (RAG), and agents are cloud‑agnostic and apply to any provider.

## Hands‑On Exercise
- **For beginners:** Open any AI chat tool, paste a recipe, contract, or long email, and ask three questions: summarize, interpret, and personalize.  
- **For builders:** Remember the core mental model – text in, model processes, text out – which underlies all implementations in the series.

## What’s Next
- Upcoming post will explore why models can be confidently wrong, how to spot hallucinations, and strategies to mitigate them.  
- The series “Learning AI Out Loud” documents a cloud architect’s public learning journey; follow along for more updates.