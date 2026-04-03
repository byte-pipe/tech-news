---
title: '[2506.11440] AbsenceBench: Language Models Can''t Tell What''s Missing'
url: https://arxiv.org/abs/2506.11440
site_name: hackernews
fetched_at: '2025-06-21T13:24:28.114595'
original_url: https://arxiv.org/abs/2506.11440
author: JnBrymn
date: '2025-06-21'
description: 'Abstract page for arXiv paper 2506.11440: AbsenceBench: Language Models Can''t Tell What''s Missing'
---

# Computer Science > Computation and Language

arXiv:2506.11440
 (cs)


 [Submitted on 13 Jun 2025]

# Title:AbsenceBench: Language Models Can't Tell What's Missing

Authors:
Harvey Yiyun Fu
,
Aryan Shrivastava
,
Jared Moore
,
Peter West
,
Chenhao Tan
,
Ari Holtzman

View a PDF of the paper titled AbsenceBench: Language Models Can't Tell What's Missing, by Harvey Yiyun Fu and 5 other authors

View PDF

HTML (experimental)

Abstract:
Large language models (LLMs) are increasingly capable of processing long inputs and locating specific information within them, as evidenced by their performance on the Needle in a Haystack (NIAH) test. However, while models excel at recalling surprising information, they still struggle to identify clearly omitted information. We introduce AbsenceBench to assesses LLMs' capacity to detect missing information across three domains: numerical sequences, poetry, and GitHub pull requests. AbsenceBench asks models to identify which pieces of a document were deliberately removed, given access to both the original and edited contexts. Despite the apparent straightforwardness of these tasks, our experiments reveal that even state-of-the-art models like Claude-3.7-Sonnet achieve only 69.6% F1-score with a modest average context length of 5K tokens. Our analysis suggests this poor performance stems from a fundamental limitation: Transformer attention mechanisms cannot easily attend to "gaps" in documents since these absences don't correspond to any specific keys that can be attended to. Overall, our results and analysis provide a case study of the close proximity of tasks where models are already superhuman (NIAH) and tasks where models breakdown unexpectedly (AbsenceBench).




Comments:

Subjects:

Computation and Language (cs.CL)

Cite as:

arXiv:2506.11440
 [cs.CL]

 

(or

arXiv:2506.11440v1
 [cs.CL]
 for this version)


 


https://doi.org/10.48550/arXiv.2506.11440

Focus to learn more

 arXiv-issued DOI via DataCite (pending registration)

## Submission history

 From: Harvey Yiyun Fu [
view email
]

[v1]

 Fri, 13 Jun 2025 03:38:29 UTC (5,538 KB)



Full-text links:

## Access Paper:

* View PDF
* HTML (experimental)
* TeX Source
* Other Formats

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
2025-06

 Change to browse by:


cs

### References & Citations

* Google Scholar
* Semantic Scholar

a

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
