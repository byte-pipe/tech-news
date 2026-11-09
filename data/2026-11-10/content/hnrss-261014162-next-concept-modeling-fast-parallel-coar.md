---
title: '[2610.14162] Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation'
url: https://arxiv.org/abs/2610.14162
site_name: hnrss
content_file: hnrss-261014162-next-concept-modeling-fast-parallel-coar
fetched_at: '2026-11-10T04:41:28.508224'
original_url: https://arxiv.org/abs/2610.14162
date: '2026-11-09'
description: 'Abstract page for arXiv paper 2610.14162: Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation'
tags:
- hackernews
- hnrss
---

# Computer Science > Computation and Language

arXiv:2610.14162
 (cs)
 

 [Submitted on 9 Oct 2026]

# Title:Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation

Authors:
Hermann Kumbong
, 
Ishan S. Khare
, 
Iddah Mlauzi
, 
Andrew Woen
, 
Charles Ding
, 
E. Kelly Buchanan
, 
Simran Arora
, 
Azalia Mirhoseini
, 
Christopher Ré
 
View a PDF of the paper titled Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation, by Hermann Kumbong and 8 other authors

View PDF

HTML (experimental)

Abstract:
Diffusion language models (DLMs) offer parallel sampling for faster generation than autoregressive models, an increasingly important advantage as inference becomes a dominant computational workload. However, DLMs degrade quickly with fewer sampling steps, process the full sequence at every step, and require many passes over the dataset to reach good quality. We introduce Next-Concept Modeling (NCM), a two-stage, coarse-to-fine framework: a multiscale residual VQ-VAE encodes text into a hierarchy of discrete codes, and a transformer generates one level at a time, predicting all codes within a level in parallel. At matched parameter scales, NCM achieves better generative perplexity than the strongest DLM baseline on LM1B while running $21\times$ faster. On OpenWebText, NCM is competitive with the strongest DLM while running $10\times$ faster; on XSum, it matches the strongest DLM's ROUGE-L while being $31\times$ faster. On the reasoning task of Sudoku, NCM outperforms autoregressive and diffusion baselines across all difficulty levels, using fewer function evaluations. On the reasoning task of Sudoku, NCM outperforms autoregressive and diffusion baselines across all difficulty levels, using fewer function evaluations.
 

Subjects:

Computation and Language (cs.CL)
; Artificial Intelligence (cs.AI); Machine Learning (cs.LG)

Cite as:

arXiv:2610.14162
 [cs.CL]

 

(or 

arXiv:2610.14162v1
 [cs.CL]
 for this version)
 

 

 
https://doi.org/10.48550/arXiv.2610.14162

Focus to learn more

 arXiv-issued DOI via DataCite

## Submission history

 From: Hermann Kumbong [
view email
] 
 
[v1]

 Fri, 9 Oct 2026 17:49:45 UTC (352 KB)

 

Full-text links:

## Access Paper:

* View PDF
* HTML (experimental)
* TeX Source

view license

 

### Additional Features

* Audio Summary

### Current browse context:

cs.CL

< prev

  |  
 

next >

new

 | 

recent

 | 
2026-10

 Change to browse by:
 

cs

cs.AI

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