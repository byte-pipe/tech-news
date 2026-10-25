---
title: '[2610.31642] A Fix for Softmax and Cross-Entropy'
url: https://arxiv.org/abs/2610.31642
site_name: tldr
content_file: tldr-261031642-a-fix-for-softmax-and-cross-entropy
fetched_at: '2026-10-25T21:25:21.546887'
original_url: https://arxiv.org/abs/2610.31642
date: '2026-10-25'
description: 'Abstract page for arXiv paper 2610.31642: A Fix for Softmax and Cross-Entropy'
tags:
- tldr
---

# Computer Science > Machine Learning

arXiv:2610.31642
 (cs)
 

 [Submitted on 22 Oct 2026]

# Title:A Fix for Softmax and Cross-Entropy

Authors:
Jonathan T. Barron
, 
Dan Gnanapragasam
, 
Michael Tschannen
 
View a PDF of the paper titled A Fix for Softmax and Cross-Entropy, by Jonathan T. Barron and 2 other authors

View PDF

HTML (experimental)

Abstract:
Standard implementations of softmax, log-softmax, and cross-entropy have two numerical bugs. The first bug, Softmax Collapse, rounds the target logit's gradient to zero if that one logit is much larger than the others, resulting in gradients that no longer sum to zero. The second bug, Softmax Cancellation, occurs when student logits are close to teacher logits, and produces non-zero gradients even when the student and teacher logits are equal. We present simple implementations of log-softmax, softmax, and cross-entropy that fix both bugs. Our fix eliminates the previously-observed "Slingshot" phenomenon, speeds up grokking with weight decay, prevents accuracy collapse without weight decay, stops student networks from drifting away from the teacher during distillation, and shows that after memorization, logit growth is bounded by an equilibrium between weight decay and Adam's $\epsilon$ hyperparameter.
 

Subjects:

Machine Learning (cs.LG)

Cite as:

arXiv:2610.31642
 [cs.LG]

 

(or 

arXiv:2610.31642v1
 [cs.LG]
 for this version)
 

 

 
https://doi.org/10.48550/arXiv.2610.31642

Focus to learn more

 arXiv-issued DOI via DataCite (pending registration)

## Submission history

 From: Jonathan Barron [
view email
] 
 
[v1]

 Thu, 22 Oct 2026 17:54:56 UTC (1,136 KB)

 

Full-text links:

## Access Paper:

* View PDF
* HTML (experimental)
* TeX Source

view license

 

### Additional Features

* Audio Summary

### Current browse context:

cs.LG

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