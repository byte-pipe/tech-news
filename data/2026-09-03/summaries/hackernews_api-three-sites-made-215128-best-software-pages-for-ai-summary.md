---
title: "Three sites made 215,128 \"best software\" pages for AI. Perplexity cites them | Trellner Research"
url: https://trellner.com/reports/manufactured-sources-behind-ai-recommendations/
date: 2026-09-02
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-03T07:21:56.850536
---

# Three sites made 215,128 "best software" pages for AI. Perplexity cites them | Trellner Research

# Summary of “Three sites made 215,128 “best software” pages for AI. Perplexity cites them”

## Overview
- Two Perplexity models (sonar and sonar‑pro) were queried for the top five products in 380 buyer‑intent software categories.  
- Each query returned a JSON list of product domains and a list of URLs that the model used as “grounding” (retrieval evidence).  
- Across 760 calls the models produced 7,534 citations pointing to 2,055 distinct domains.

## Methodology
- Date of experiment: 2 September 2026.  
- Prompt: “Give a ranked top‑5 list for <category> as JSON, including each product’s official homepage domain.”  
- All responses were parseable; both models reported the URLs they retrieved.  
- Domains were checked against the Tranco top‑1 M list (snapshot 2026‑09‑01) and the Wayback Machine.  
- Vendor homepages supplied by the models (1,502 URLs) were tested for reachability.

## Citation distribution
- **Unranked (outside Tranco 1 M):** 23.4 % of citations.  
- **Ranked worse than #100 k:** 59.8 % of citations.  
- **Median Tranco rank** of the 5,768 ranked citations: 71,611.  
- The ten most‑cited domains account for 17.3 % of all citations; no single “cartel” dominates the evidence.

## Top cited domains
| Domain | Citations | Share | Tranco rank |
|--------|-----------|-------|-------------|
| g2.com | 291 | 3.86 % | 4,027 |
| reddit.com | 261 | 3.46 % | 105 |
| guideflow.com | 194 | 2.57 % | 177,039 |
| gartner.com | 158 | 2.10 % | 1,766 |
| zapier.com | 82 | 1.09 % | 2,919 |
| wifitalents.com | 71 | 0.94 % | 105,281 |
| capterra.com | 68 | 0.90 % | 6,387 |
| linkedin.com | 67 | 0.89 % | 18 |
| worldmetrics.org | 60 | 0.80 % | 104,737 |
| gitnux.org | 50 | 0.66 % | 42,759 |

*Wikipedia was cited only three times.*

## Guideflow.com – the third‑largest source
- Not a review or directory site; it sells interactive product demos.  
- Its blog supplied 194 distinct URLs across 96 of the 380 categories (≈ 25 % of categories).  
- The sitemap contains 3,351 blog URLs (2,176 unique posts).  
- The blog’s content‑marketing listicles were used as grounding for unrelated categories such as “3D rendering software” and “IVR software”.

## Three related “Facts & Grounding Page” sites
- **Domains:** wifitalents.com, worldmetrics.org, gitnux.org.  
- All registered Dec 2023 – May 2024, use the same Cloudflare nameservers, share identical page templates and a six‑post blog that cross‑references the other two sites and a fourth brand (zipdo.co).  
- Their sitemaps list roughly 105 k URLs each, with about 71 k URLs following the pattern `/best/<something>-software/pages`.  
- Combined, they generate **215,128** “best software” pages, far exceeding the actual number of software categories.

## Self‑description of the “Facts & Grounding” sites
- HTML title: “<Brand> — Facts & Grounding Page”.  
- Meta description claims a machine‑readable record of verified facts for the brand.  
- Offer commercial market‑research services (e.g., reports from €499, custom research from €5,000).  
- The term “grounding” refers to the retrieval step used by AI models, not a consumer‑facing concept.

## Example comparison of a single category
- Category examined: “project estimation software”.  
- Each site lists ten tools in JSON‑LD; the top five differ between sites.  
- Staff credits differ (nine distinct individuals across the three sites).  
- Editorial notes vary, with labels such as “AI‑verified · Expert reviewed”.  
- All pages contain an unrendered placeholder (“Within the next 26 days” or “40 days”).

## Vendor homepage availability
- The 1,502 vendor homepages returned by the models were probed twice (direct and via rotating proxy).  
- A site was marked reachable if either attempt succeeded, mitigating IP‑based blocking effects.  

## Key takeaways
- A large share of AI‑generated software recommendations relies on low‑rank or brand‑new domains, many of which are automatically generated “best‑software” pages.  
- A single marketing blog (guideflow.com) and three coordinated “Facts & Grounding” sites together provide a substantial portion of the evidence used by Perplexity’s models.  
- The grounding layer’s reliance on such sources raises questions about the quality and independence of the retrieved evidence, even though the final vendor URLs are mostly valid.