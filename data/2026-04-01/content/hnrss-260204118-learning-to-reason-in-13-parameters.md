---
title: '[2602.04118] Learning to Reason in 13 Parameters'
url: https://arxiv.org/abs/2602.04118
site_name: hnrss
content_file: hnrss-260204118-learning-to-reason-in-13-parameters
fetched_at: '2026-04-01T11:24:30.847085'
original_url: https://arxiv.org/abs/2602.04118
date: '2026-03-27'
description: 'Abstract page for arXiv paper 2602.04118: Learning to Reason in 13 Parameters'
tags:
- hackernews
- hnrss
---

# Computer Science > Machine Learning

arXiv:2602.04118
 (cs)


 [Submitted on 4 Feb 2026]

# Title:Learning to Reason in 13 Parameters

Authors:
John X. Morris
,
Niloofar Mireshghallah
,
Mark Ibrahim
,
Saeed Mahloujifar

View a PDF of the paper titled Learning to Reason in 13 Parameters, by John X. Morris and 3 other authors

View PDF

HTML (experimental)

Abstract:
Recent research has shown that language models can learn to \textit{reason}, often via reinforcement learning. Some work even trains low-rank parameterizations for reasoning, but conventional LoRA cannot scale below the model dimension. We question whether even rank=1 LoRA is necessary for learning to reason and propose TinyLoRA, a method for scaling low-rank adapters to sizes as small as one parameter. Within our new parameterization, we are able to train the 8B parameter size of Qwen2.5 to 91\% accuracy on GSM8K with only 13 trained parameters in bf16 (26 total bytes). We find this trend holds in general: we are able to recover 90\% of performance improvements while training $1000x$ fewer parameters across a suite of more difficult learning-to-reason benchmarks such as AIME, AMC, and MATH500. Notably, we are only able to achieve such strong performance with RL: models trained using SFT require $100-1000x$ larger updates to reach the same performance.


Subjects:

Machine Learning (cs.LG)

Cite as:

arXiv:2602.04118
 [cs.LG]

 

(or

arXiv:2602.04118v1
 [cs.LG]
 for this version)


 


https://doi.org/10.48550/arXiv.2602.04118

Focus to learn more

 arXiv-issued DOI via DataCite

## Submission history

 From: John Morris [
view email
]

[v1]

 Wed, 4 Feb 2026 01:20:04 UTC (1,595 KB)



Full-text links:

## Access Paper:

* View PDF
* HTML (experimental)
* TeX Source

view license



 Current browse context:
cs.LG

< prev

  |  


next >

new

 |

recent

 |
2026-02

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



IArxiv recommender toggle

IArxiv Recommender

(
What is IArxiv?
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
