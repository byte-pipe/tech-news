---
title: "56% of GPT-5.4's Citations Go to Brand Websites. Only 8% of GPT-5.3's Do. - Writesonic Blog"
url: https://writesonic.com/blog/chatgpt-citation-study-gpt-5-4-vs-gpt-5-3
date: 2026-03-14
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-03-14T06:03:44.422209
---

# 56% of GPT-5.4's Citations Go to Brand Websites. Only 8% of GPT-5.3's Do. - Writesonic Blog

# 56% of GPT‑5.4’s Citations Go to Brand Websites. Only 8% of GPT‑5.3’s Do.

## Overview
- Tested 50 prompts on ChatGPT’s new models (GPT‑5.3 Instant, GPT‑5.4 Thinking) and baseline GPT‑5.2 versions.  
- Extracted every fan‑out query, web‑search result, and citation URL from the conversation JSON.  
- Compared AI‑generated results with Bing and Google via SerpAPI.  

## Main Findings
- **First‑party citation rate:**  
  - GPT‑5.4: 56 % of citations point to the brand’s own website.  
  - GPT‑5.3: only 8 % point to brand sites (down from 22 % in GPT‑5.2).  
- **Source overlap:** average overlap between the two models is 7 %; 22 of 50 prompts have zero overlap.  
- **Prompt category impact:** the gap is largest on comparison prompts (0 % vs 83‑100 %); SaaS improves 7‑fold (12 % → 82 %); even “shopping” doubles first‑party rate.  
- **Gatekeeper domains for GPT‑5.3:** Forbes, TechRadar, Tom’s Guide, Reddit, Money.com dominate third‑party citations.  
- **Top domains for GPT‑5.4:** brand sites themselves (e.g., hubspot.com, shopify.com, salesforce.com).  

## Fan‑out Query Behavior
- GPT‑5.3 sends a single query (raw prompt).  
- GPT‑5.4 generates **8.5 × more** fan‑out queries per prompt (average 8.5 sub‑queries), using:
  - Domain‑restricted queries (148 total)  
  - `site:` operators (156 total)  
- Typical two‑phase pattern for GPT‑5.4:  
  1. **Brand verification** – queries restricted to brand domains.  
  2. **Third‑party validation** – queries to review or comparison sites.  

## Quantitative Comparison (selected metrics)

| Model | Avg. fan‑out queries | Avg. web results | Avg. citations | Avg. response length |
|-------|---------------------|------------------|----------------|----------------------|
| GPT‑5.2 Instant | 0.9 | 36.6 | 4.5 | 388 words |
| GPT‑5.3 Instant | 1.0 | 27.3 | 5.8 | 548 words |
| GPT‑5.4 Thinking | 8.5 | 109.4 | 14.8 | 769 words |

## Category‑level Query Intensity (GPT‑5.4)

| Category | Avg. queries | Avg. citations | Avg. web results |
|----------|--------------|----------------|------------------|
| Productivity | 14.7 | 20.3 | 156 |
| Marketing | 11.7 | 25.0 | 144 |
| Legal | 12.5 | 15.0 | 165 |
| Services | 14.0 | 15.0 | 184 |
| Travel | 11.7 | 12.7 | 148 |
| Education | 10.0 | 17.7 | 130 |
| Finance | 8.3 | 17.7 | 130 |
| SaaS | 6.3 | 17.3 | 76 |
| Comparison | 9.3 | 14.3 | 99 |
| Shopping | 4.6 | — | — |

## Implications for Brands (GEO / AEO)
- Visibility on GPT‑5.3 does **not** guarantee visibility on GPT‑5.4; strategies must address both models.  
- Dominating third‑party sites (e.g., Forbes, TechRadar) helps on GPT‑5.3, while owning and optimizing brand sites is crucial for GPT‑5.4.  
- AI‑visibility audits that test only one model miss a large portion of the citation landscape.  

## Sample Prompt Comparison (first‑party %)

| Prompt | GPT‑5.3 % | GPT‑5.4 % |
|-------|----------|----------|
| Best CRM for B2B SaaS | 0 % | 100 % |
| Marathon running shoes | 0 % | 88 % |
| QuickBooks vs Xero vs FreshBooks | 0 % | 100 % |
| iPhone vs Samsung vs Pixel | 0 % | 100 % |
| Smart home security | 0 % | 86 % |
| Email marketing platforms | 14 % | 100 % |

## Conclusion
GPT‑5.4’s architecture aggressively targets brand domains first, resulting in a markedly higher first‑party citation rate and far more granular fan‑out queries. GPT‑5.3 remains reliant on a handful of third‑party “kingmaker” sites. Brands must adapt their SEO and content strategies to address both citation ecosystems to maintain visibility across ChatGPT’s evolving models.