---
title: Why does AI forget what you said (and how to fix it) - DEV Community
url: https://dev.to/aws/why-does-ai-forget-what-you-said-and-how-to-fix-it-52f6
date: 2026-05-25
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-05-29T04:38:18.326577
---

# Why does AI forget what you said (and how to fix it) - DEV Community

# Summary of “Why does AI forget what you said (and how to fix it)”

## What a context window actually is
- Every model has a fixed‑size “context window” that holds all tokens it can attend to at once (input + output).  
- Think of the window as a desk: the question, any pasted document, conversation history, and system instructions must all fit on that desk.  
- If the desk is overloaded, the model silently drops or mis‑weights information without warning.  
- Window sizes vary:
  * Older models ≈ 4 000 tokens (≈ 3 000 words, six pages).  
  * Modern models ≈ 128 000 tokens (short novel) or even 1 000 000+ tokens (multiple novels or whole codebases).  
- A larger desk does not guarantee equal attention to every item; it only allows more items to be present.

## Two shapes of the same problem
### Documents
- Supplying a long document (e.g., a contract) and asking about a specific section can cause the model to miss or mis‑place the relevant passage, especially when surrounding text dilutes attention.

### Conversations
- The model re‑reads the entire transcript on each turn; there is no built‑in persistent memory.  
- Tokens accumulate quickly: a 50‑token question + 300‑token answer ≈ 350 tokens per exchange; 20 exchanges can exceed 7 000 tokens.  
- The whole transcript is resent and re‑charged each turn, consuming both memory and cost.

## “Lost in the middle”
- When the input is long, the model focuses most on the beginning and the end, neglecting the middle.  
- Early messages drift as the transcript grows because they move into the middle of the window where attention is weakest.  
- Most models do not warn about this degradation; they remain confidently wrong.

## Practical ways to mitigate the issue
- **Bigger window** – switch to a model with a larger context if limits are reached.  
- **Chunk** – feed only the relevant portion of a document rather than the whole thing.  
- **Summarise** – ask the model to summarise a long text first, then query the summary.  
- **Position** – place critical information at the start or end of the prompt; avoid burying it in the middle.  
- **Restate** – repeat important constraints or facts in later messages to keep them in view.  
- **System prompt** – store stable instructions in the system‑prompt field (or custom instructions) for consistent guidance.  
- **Fresh start** – begin a new conversation when the topic has shifted or the transcript is too long; carry over only essential context.  
- **Build your own memory layer** – summarize earlier turns, store the summary externally (e.g., database, variable), and prepend it to new calls; this acts as a cache and reduces repeated tokenisation.  
- **Prompt caching** – on platforms that support it (e.g., Amazon Bedrock), cache static context so it isn’t re‑tokenised each request.  
- **Retrieval for documents** – instead of stuffing an entire document, retrieve only the most relevant passages and feed those to the model.