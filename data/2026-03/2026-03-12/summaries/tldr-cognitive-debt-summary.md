---
title: Cognitive Debt
url: https://acairns.co.uk/posts/cognitive-debt
date: 2026-03-12
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-03-12T03:16:21.663622
---

# Cognitive Debt

# Cognitive Debt – Summary

## Introduction
- Teams ship code faster with AI‑generated pull requests, but often lack understanding of how the code works.  
- This gap between code volume and comprehension is called **cognitive debt**.

## The Delta
- **Code volume** is increasing: AI produces fully formed methods and classes without prior design work.  
- **Comprehension** is not keeping pace; a smaller percentage of shipped lines are truly understood.  
- The space between these two trends represents cognitive debt.

## Not Technical Debt
- Technical debt is intentional, visible shortcuts that can be tracked and scheduled for remediation.  
- Cognitive debt is invisible: code that no one understands well enough to judge, accumulating silently through accepted AI suggestions.  
- It resides in the team’s collective mental models, not directly in the codebase.

## How It Accumulates
- Hand‑written code forces developers to wrestle with problems, building mental models as a by‑product.  
- AI‑generated code arrives ready‑to‑run, skipping the reasoning phase, so the underlying theory is missing unless deliberately created.  
- Without that reasoning, the code lacks the shared understanding described by Peter Naur.

## Warning Signs
- Review times shrink because reviewers cannot read all incoming code thoroughly.  
- Incident response slows; debugging takes 2–3× longer without a clear mental model.  
- Onboarding suffers; new engineers cannot learn from teammates who don’t understand the system.  
- Code is rewritten more often because original generated functions become opaque.  
- Certain parts of the codebase become “untouchable” due to lack of understanding.

## The Three Stages of Accumulation
1. **Honeymoon (Day 1–30)** – High productivity, full context, low risk.  
2. **Drift (Month 1–6)** – Confidence grows, double‑checking wanes, gap between “works” and “understood” widens.  
3. **Cliff (Month 6+)** – Team loses confidence in modifying code, debugging becomes guesswork, reverse‑engineering is required.

## Trust Paradox
- Survey data shows trust in AI code output fell from 43 % to 33 % year over year, while usage rose to 84 %.  
- Tools are useful for generation, but usefulness does not equal understanding; comfort with the workflow encourages skipping comprehension.

## Where I Draw the Line
- The author uses AI daily for speed but treats the loss of understanding as a loan to be repaid.  
- Cognitive debt is a borrowing of future comprehension; each unexplained acceptance adds a repayment obligation.  
- A layered approach (onion architecture) helps:
  - **Core domain** – Requires deep understanding; mental models must be maintained.  
  - **Application layer** – Important but can tolerate some abstraction.  
  - **Outer layers** (framework, CI, configuration) – Suitable for AI automation; deep understanding is less critical.  
- The author now:
  - Insists on personal or closely reviewed work for core business logic.  
  - Allows AI to handle boilerplate, wiring, and infrastructure, while still reviewing outcomes.  

**Bottom line:** Cognitive debt is real and grows with unchecked AI code generation; managing it requires deliberate boundaries between what must be understood and what can be safely automated.