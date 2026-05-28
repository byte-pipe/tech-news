---
title: AI Risk Is an Architecture Problem - by Eric Glover
url: https://appliedingenuity.substack.com/p/ai-risk-is-an-architecture-problem
date: 2026-05-29
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-05-29T04:39:13.583281
---

# AI Risk Is an Architecture Problem - by Eric Glover

# AI Risk Is an Architecture Problem

## Section 1: Why AI Risk Conversations Stall
- Companies at three different stages (exploring AI, scaling a proof‑of‑concept, or operating a shipped AI system) share a common difficulty: they cannot clearly see or articulate the business risks created by AI components.  
- Early adopters fear moving too slowly and lack a roadmap for safe entry; those scaling a demo encounter unexpected production hurdles; operators who have shipped AI experience concrete failures (hallucinations, data leaks, costly automated actions) but lack a vocabulary to describe them.  
- Mapping a business incident directly to a single AI component (e.g., blaming the engineer for a wrong answer) is misleading; the underlying risk is the probabilistic nature of AI that can generate user‑facing output, not just a prompt‑tuning issue.  

## Section 2: Layers of Risk
- **Executive view (consequence layer):** concerns about brand damage, regulatory compliance, liability, operational disruption, and commercial loss—risk categories that appear on risk registers and board discussions.  
- **Engineering view (cause layer):** focuses on AI mechanism risks, which fall into three categories:  
  - **Data risk:** unintended exposure of sensitive information.  
  - **Output risk:** generation of false or inappropriate statements.  
  - **Action risk:** execution of harmful or unintended actions.  
- The three mechanism risks can combine into a “lethal trifecta” (private data + untrusted input + ability to act), creating the most dangerous failures.  
- Business consequences map from mechanism risks to the five executive risk categories; a single AI failure often touches multiple business harms and can escalate to liability.  
- Example contrast: an OCR misread that a human can catch (operational risk) versus the same misread driving an autonomous wire transfer (commercial loss). The error is identical; the surrounding architecture (human‑in‑the‑loop vs. full autonomy) determines the business impact.  

## Connecting the Layers (Illustrative Table)
- Representative AI failures (e.g., data leakage, hallucinated answers, unauthorized actions) are paired with potential business harms (brand, compliance, liability, operational, commercial).  
- Reducing error rates of individual components does not shrink the overall business risk space; redesigning the system architecture can mitigate or contain the consequences.  

*The article continues to explore how architectural choices shape the risk profile of agentic AI systems.*