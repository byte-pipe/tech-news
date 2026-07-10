---
title: "Bigger Context Windows Didn't Make Our RAG Smarter - DEV Community"
url: https://dev.to/valerykot/bigger-context-windows-didnt-make-our-rag-smarter-4d0l
date: 2026-07-08
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-07-11T01:40:38.280065
---

# Bigger Context Windows Didn't Make Our RAG Smarter - DEV Community

# Bigger Context Windows Didn't Make Our RAG Smarter

## Problem statement
- We stopped measuring retrieval quality by token count once long‑context models appeared.  
- The assumption was that a model that can read 128 K tokens makes careful document selection unnecessary.  
- In practice this assumption proved false.

## More context, worse answers
- Query example: “Why did we abandon microservices?”  
- Retrieval returns many related items (ADR, Jira tickets, Slack threads, meeting notes, glossary).  
- The true answer resides in a single ADR that uses different vocabulary and is therefore ranked low.  
- The model receives many relevant‑looking documents and generates a coherent but **unfaithful** explanation, synthesizing themes rather than reproducing the original decision.

## Bigger windows don’t fix retrieval
- Prior research (e.g., *Lost in the Middle*) shows models struggle with information deep in long contexts.  
- Our observation: the answer is often missing not because of length but because retrieval fails to surface the decisive document.  
- Adding more tokens can simply give the model more material to average together, worsening faithfulness.

## We were optimizing the wrong thing
- Initially treated retrieval as a packing problem: “How many useful chunks fit in the prompt?”  
- The focus shifted to evaluating **why** a document is included:  
  - Does it actually explain the decision?  
  - Does it merely mention the same technology?  
- These relevance questions matter far more than context‑window size.

## Retrieval is a selection problem
- The key insight was that retrieval is about selecting a few *explanatory* pieces, not about fitting more information.  
- Large context windows are valuable but cannot compensate for weak retrieval; they may even make poor retrieval appear convincing.  
- Future work should question other assumptions, such as treating documents as bags of independent chunks.