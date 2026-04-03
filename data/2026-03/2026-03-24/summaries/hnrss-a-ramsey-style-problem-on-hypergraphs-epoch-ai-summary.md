---
title: A Ramsey-style Problem on Hypergraphs | Epoch AI
url: https://epoch.ai/frontiermath/open-problems/ramsey-hypergraphs
date: 2026-03-24
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-24T20:02:50.095520
---

# A Ramsey-style Problem on Hypergraphs | Epoch AI

# A Ramsey‑style Problem on Hypergraphs – Summary

## Update on the Solution
- The problem has been solved by Kevin Barreto and Liam Price using GPT‑5.4 Pro.  
- Their solution was verified by the problem’s author, Will Brian, and will be prepared for publication.  
- A full transcript of the GPT‑5.4 Pro conversation and its final write‑up are available via provided links.  
- Brian praises the solution for removing an inefficiency in the lower‑bound construction and matching the complexity of the upper‑bound construction, yielding tight lower and upper bounds for this Ramsey‑type problem.  
- Future papers may include Barreto and Price as co‑authors; updates will be posted when available.  
- After this breakthrough, the general testing scaffold for FrontierMath: Open Problems was completed, and additional models (Opus 4.6 max, Gemini 3.1 Pro, GPT‑5.4 xhigh) also succeeded on the problem.

## Original Problem Description
- **Goal:** Improve lower bounds for the sequence \(H(n)\), which measures the largest vertex count of a hypergraph with no isolated vertices and no partition of size greater than \(n\).  
- **Definitions:**  
  - A hypergraph \((V,\mathcal H)\) contains a partition of size \(n\) if there exist \(D\subseteq V\) and \(\mathcal P\subseteq\mathcal H\) with \(|D|=n\) and each vertex of \(D\) lies in exactly one edge of \(\mathcal P\).  
  - \(H(n)\) is the maximal \(|V|\) for such a hypergraph.  
- **Current Knowledge:** Known lower bounds are believed to be suboptimal, even asymptotically.  
- **Tasks:**  
  1. **Warm‑up:** Provide a hypergraph for a specific \(n\) where constructions are already known.  
  2. **Single Challenge:** Find a hypergraph for an \(n\) with no known construction, likely too hard for brute force.  
  3. **Full Problem:** Design a general algorithm producing hypergraphs that achieve a constant‑factor improvement over the recursive bound \(k_n\) (with \(k_1=1\) and \(k_n=\lfloor n/2\rfloor+k_{\lfloor n/2\rfloor}+k_{\lfloor (n+1)/2\rfloor}\)), effective already at \(n=15\).

## AI Prompt Variants Tested
- **Warm‑up Prompt:** Request a hypergraph with \(|V|\ge 64\), \(|\mathcal H|\le 20\), and no partitions larger than 20.  
- **Single Challenge Prompt:** Same constraints but with \(|V|\ge 66\).  
- **Full Problem Prompt:** Ask for a Python function `solution(n)` that outputs a hypergraph witnessing \(H(n)\ge c\cdot k_n\) for some \(c>1\), with runtime limits for \(n\le 100\).

## Mathematician Survey Results
- **Familiarity:** About a majority of specialists (≈10) are highly familiar with the problem.  
- **Serious Attempts:** 5–10 mathematicians have made serious attempts.  
- **Estimated Human Effort:** 1–3 months for an expert to solve.  
- **Notability:** Moderately interesting; likely to be published in a specialty journal.  
- **Potential Impact:** Fairly likely to open new research directions.  
- **Solvability Confidence:** 95–99 % probability that the problem is solvable as stated.