---
title: '[2603.21852] All elementary functions from a single binary operator'
url: https://arxiv.org/abs/2603.21852
site_name: hackernews_api
content_file: hackernews_api-260321852-all-elementary-functions-from-a-single-b
fetched_at: '2026-04-13T12:02:13.976100'
original_url: https://arxiv.org/abs/2603.21852
author: pizza
date: '2026-04-13'
description: 'Abstract page for arXiv paper 2603.21852: All elementary functions from a single binary operator'
tags:
- hackernews
- trending
---

# Computer Science > Symbolic Computation

arXiv:2603.21852
 (cs)
 

 [Submitted on 23 Mar 2026 (
v1
), last revised 4 Apr 2026 (this version, v2)]

# Title:All elementary functions from a single binary operator

Authors:
Andrzej Odrzywołek
 
View a PDF of the paper titled All elementary functions from a single binary operator, by Andrzej Odrzywo{\l}ek

View PDF

HTML (experimental)

Abstract:
A single two-input gate suffices for all of Boolean logic in digital hardware. No comparable primitive has been known for continuous mathematics: computing elementary functions such as sin, cos, sqrt, and log has always required multiple distinct operations. Here I show that a single binary operator, eml(x,y)=exp(x)-ln(y), together with the constant 1, generates the standard repertoire of a scientific calculator. This includes constants such as e, pi, and i; arithmetic operations including addition, subtraction, multiplication, division, and exponentiation as well as the usual transcendental and algebraic functions. For example, exp(x)=eml(x,1), ln(x)=eml(1,eml(eml(1,x),1)), and likewise for all other operations. That such an operator exists was not anticipated; I found it by systematic exhaustive search and established constructively that it suffices for the concrete scientific-calculator basis. In EML (Exp-Minus-Log) form, every such expression becomes a binary tree of identical nodes, yielding a grammar as simple as S -> 1 | eml(S,S). This uniform structure also enables gradient-based symbolic regression: using EML trees as trainable circuits with standard optimizers (Adam), I demonstrate the feasibility of exact recovery of closed-form elementary functions from numerical data at shallow tree depths up to 4. The same architecture can fit arbitrary data, but when the generating law is elementary, it may recover the exact formula.
 

 

Comments:

Subjects:

Symbolic Computation (cs.SC)
; Machine Learning (cs.LG)

 

MSC
 classes:

26A09 (Primary) 08A40, 68W30 (Secondary)

ACM
 classes:

I.1.1; F.1.1

Cite as:

arXiv:2603.21852
 [cs.SC]

 

(or 

arXiv:2603.21852v2
 [cs.SC]
 for this version)
 

 

 
https://doi.org/10.48550/arXiv.2603.21852

Focus to learn more

 arXiv-issued DOI via DataCite

## Submission history

 From: Andrzej Odrzywolek [
view email
] 
 
[v1]

 Mon, 23 Mar 2026 11:40:24 UTC (1,393 KB)

[v2]

 Sat, 4 Apr 2026 06:31:05 UTC (1,245 KB)

Full-text links:

## Access Paper:

* View PDF
* HTML (experimental)
* TeX Source

view license

 

Ancillary-file links:

## Ancillary files(details):

* SupplementaryInformation.pdf

 Current browse context: 
cs.SC

< prev

  |  
 

next >

new

 | 

recent

 | 
2026-03

 Change to browse by:
 

cs

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