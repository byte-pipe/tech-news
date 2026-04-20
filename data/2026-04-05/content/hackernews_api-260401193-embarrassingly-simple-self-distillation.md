---
title: '[2604.01193] Embarrassingly Simple Self-Distillation Improves Code Generation'
url: https://arxiv.org/abs/2604.01193
site_name: hackernews_api
content_file: hackernews_api-260401193-embarrassingly-simple-self-distillation
fetched_at: '2026-04-05T01:01:14.121332'
original_url: https://arxiv.org/abs/2604.01193
author: Anon84
date: '2026-04-04'
description: 'Abstract page for arXiv paper 2604.01193: Embarrassingly Simple Self-Distillation Improves Code Generation'
tags:
- hackernews
- trending
---

# Computer Science > Computation and Language

arXiv:2604.01193
 (cs)


 [Submitted on 1 Apr 2026]

# Title:Embarrassingly Simple Self-Distillation Improves Code Generation

Authors:
Ruixiang Zhang
,
Richard He Bai
,
Huangjie Zheng
,
Navdeep Jaitly
,
Ronan Collobert
,
Yizhe Zhang

View a PDF of the paper titled Embarrassingly Simple Self-Distillation Improves Code Generation, by Ruixiang Zhang and 5 other authors

View PDF

HTML (experimental)

Abstract:
Can a large language model (LLM) improve at code generation using only its own raw outputs, without a verifier, a teacher model, or reinforcement learning? We answer in the affirmative with simple self-distillation (SSD): sample solutions from the model with certain temperature and truncation configurations, then fine-tune on those samples with standard supervised fine-tuning. SSD improves Qwen3-30B-Instruct from 42.4% to 55.3% pass@1 on LiveCodeBench v6, with gains concentrating on harder problems, and it generalizes across Qwen and Llama models at 4B, 8B, and 30B scale, including both instruct and thinking variants. To understand why such a simple method can work, we trace these gains to a precision-exploration conflict in LLM decoding and show that SSD reshapes token distributions in a context-dependent way, suppressing distractor tails where precision matters while preserving useful diversity where exploration matters. Taken together, SSD offers a complementary post-training direction for improving LLM code generation.


Subjects:

Computation and Language (cs.CL)

Cite as:

arXiv:2604.01193
 [cs.CL]

 

(or

arXiv:2604.01193v1
 [cs.CL]
 for this version)


 


https://doi.org/10.48550/arXiv.2604.01193

Focus to learn more

 arXiv-issued DOI via DataCite (pending registration)

## Submission history

 From: Ruixiang Zhang [
view email
]

[v1]

 Wed, 1 Apr 2026 17:39:50 UTC (21,738 KB)



Full-text links:

## Access Paper:

* View PDF
* HTML (experimental)
* TeX Source

view license



 Current browse context:
cs.CL

< prev

  |  


next >

new

 |

recent

 |
2026-04

 Change to browse by:


cs

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

Links to Code Toggle

Papers with Code

(
What is Papers with Code?
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
