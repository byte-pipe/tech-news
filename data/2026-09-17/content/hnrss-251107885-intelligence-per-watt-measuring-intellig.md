---
title: '[2511.07885] Intelligence per Watt: Measuring Intelligence Efficiency of Local AI'
url: https://arxiv.org/abs/2511.07885
site_name: hnrss
content_file: hnrss-251107885-intelligence-per-watt-measuring-intellig
fetched_at: '2026-09-17T03:38:50.296155'
original_url: https://arxiv.org/abs/2511.07885
date: '2026-09-14'
description: 'Abstract page for arXiv paper 2511.07885: Intelligence per Watt: Measuring Intelligence Efficiency of Local AI'
tags:
- hackernews
- hnrss
---

# Computer Science > Distributed, Parallel, and Cluster Computing

arXiv:2511.07885
 (cs)
 

 [Submitted on 11 Nov 2025 (
v1
), last revised 6 Sep 2026 (this version, v6)]

# Title:Intelligence per Watt: Measuring Intelligence Efficiency of Local AI

Authors:
Jon Saad-Falcon
, 
Avanika Narayan
, 
Hakki Orhun Akengin
, 
J. Wes Griffin
, 
Herumb Shandilya
, 
Adrian Gamarra Lafuente
, 
Medhya Goel
, 
Rebecca Joseph
, 
Shlok Natarajan
, 
Etash Kumar Guha
, 
Shang Zhu
, 
Ben Athiwaratkun
, 
John Hennessy
, 
Azalia Mirhoseini
, 
Christopher Ré
 
View a PDF of the paper titled Intelligence per Watt: Measuring Intelligence Efficiency of Local AI, by Jon Saad-Falcon and 14 other authors

View PDF

HTML (experimental)

Abstract:
Large language model (LLM) queries are predominantly processed by frontier models in centralized cloud infrastructure. Demand growth strains this paradigm faster than providers can scale. Two advances create an opportunity to rethink it: small, local LMs (<=20B active parameters) now achieve competitive performance to frontier models on many tasks, and local accelerators (e.g., Apple M4 Max) can host these models at interactive latencies. This raises the question: can local inference viably redistribute demand from centralized infrastructure? This requires measuring both whether local LMs can accurately answer real-world queries and whether they can do so efficiently on power-constrained devices (e.g., laptops). We propose intelligence per watt (IPW), task accuracy per unit of power, as a unified metric for the capability and efficiency of local inference across model-accelerator configurations. We evaluate 20+ state-of-the-art local LMs, 8 hardware accelerators (local and cloud), and 1M real-world single-turn chat and reasoning queries. For each query, we measure accuracy (local LM win rate against frontier models), energy, latency, and power. We find three key results. First, local LMs successfully answer 88.7% of these queries, with accuracy varying by domain. Second, longitudinal analysis from 2023-2025 shows IPW improved 5.3x, driven by both algorithmic and accelerator advances, with locally-serviceable query coverage rising from 23.2% to 71.3%. Third, local accelerators achieve at least 1.4x lower IPW than cloud accelerators running identical models, revealing significant headroom for local accelerator optimization. These findings demonstrate that local inference can meaningfully redistribute demand from centralized infrastructure for a substantial subset of queries, with IPW serving as the critical metric for tracking this transition.
 

Subjects:

Distributed, Parallel, and Cluster Computing (cs.DC)
; Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Machine Learning (cs.LG)

Cite as:

arXiv:2511.07885
 [cs.DC]

 

(or 

arXiv:2511.07885v6
 [cs.DC]
 for this version)
 

 

 
https://doi.org/10.48550/arXiv.2511.07885

Focus to learn more

 arXiv-issued DOI via DataCite

## Submission history

 From: Jon Saad-Falcon [
view email
] 
 
[v1]

 Tue, 11 Nov 2025 06:33:30 UTC (5,373 KB)

[v2]

 Fri, 14 Nov 2025 00:53:12 UTC (5,538 KB)

[v3]

 Thu, 26 Feb 2026 17:09:14 UTC (5,538 KB)

[v4]

 Thu, 21 May 2026 03:40:21 UTC (5,134 KB)

[v5]

 Fri, 7 Aug 2026 02:40:27 UTC (5,621 KB)

[v6]

 Sun, 6 Sep 2026 05:29:37 UTC (5,608 KB)

 

Full-text links:

## Access Paper:

* View PDF
* HTML (experimental)
* TeX Source

view license

 

### Current browse context:

cs.DC

< prev

  |  
 

next >

new

 | 

recent

 | 
2025-11

 Change to browse by:
 

cs

cs.AI

cs.CL

cs.LG

### References & Citations

* Google Scholar
* Semantic Scholar

export BibTeX citation

Loading...

## BibTeX formatted citation

×

loading...

Data provided by: 

### Bookmark

 

Bibliographic Tools

# Bibliographic and Citation Tools

Bibliographic Explorer Toggle

Bibliographic Explorer
 
(
What is the Explorer?
)

Connected Papers Toggle

Connected Papers
 
(
What is Connected Papers?
)

Litmaps Toggle

Litmaps
 
(
What is Litmaps?
)

scite.ai Toggle

scite Smart Citations
 
(
What are Smart Citations?
)

Code, Data, Media

# Code, Data and Media Associated with this Article

alphaXiv Toggle

alphaXiv
 
(
What is alphaXiv?
)

Links to Code Toggle

CatalyzeX Code Finder for Papers
 
(
What is CatalyzeX?
)

DagsHub Toggle

DagsHub
 
(
What is DagsHub?
)

GotitPub Toggle

Gotit.pub
 
(
What is GotitPub?
)

Huggingface Toggle

Hugging Face
 
(
What is Huggingface?
)

ScienceCast Toggle

ScienceCast
 
(
What is ScienceCast?
)

Demos

# Demos

Replicate Toggle

Replicate
 
(
What is Replicate?
)

Spaces Toggle

Hugging Face Spaces
 
(
What is Spaces?
)

Spaces Toggle

TXYZ.AI
 
(
What is TXYZ.AI?
)

Related Papers

# Recommenders and Search Tools

Link to Influence Flower

Influence Flower
 
(
What are Influence Flowers?
)

Core recommender toggle

CORE Recommender
 
(
What is CORE?
)

* Author
* Venue
* Institution
* Topic

 About arXivLabs
 

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community?Learn more about arXivLabs.

Which authors of this paper are endorsers?
 |
 
Disable MathJax
 (
What is MathJax?
)