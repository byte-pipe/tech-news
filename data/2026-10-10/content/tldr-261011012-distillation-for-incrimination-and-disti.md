---
title: '[2610.11012] Distillation for Incrimination and Distillation for Capabilities'
url: https://arxiv.org/abs/2610.11012
site_name: tldr
content_file: tldr-261011012-distillation-for-incrimination-and-disti
fetched_at: '2026-10-10T16:08:01.461021'
original_url: https://arxiv.org/abs/2610.11012
date: '2026-10-10'
description: 'Abstract page for arXiv paper 2610.11012: Distillation for Incrimination and Distillation for Capabilities'
tags:
- tldr
---

# Computer Science > Artificial Intelligence

arXiv:2610.11012
 (cs)
 

 [Submitted on 7 Oct 2026]

# Title:Distillation for Incrimination and Distillation for Capabilities

Authors:
Sebastian Prasanna
, 
Jacqueline Tay
, 
Alek Westover
 
View a PDF of the paper titled Distillation for Incrimination and Distillation for Capabilities, by Sebastian Prasanna and 2 other authors

View PDF

HTML (experimental)

Abstract:
Powerful misaligned AI models might recognize alignment evaluations and strategically behave well on them, rendering direct audits uninformative. However, distilling such a model into a weaker benign student places the teacher in a Distillation Double Bind: if misalignment transfers, the student may conceal it less effectively, revealing evidence about the teacher; if it does not, the student may learn useful capabilities while remaining benign. We introduce two distinct distillation approaches, one targeting each outcome. Distillation for Incrimination (DFI) aims to transfer misalignment but not the ability to conceal it. Distilling AuditBench's secret-keeping models into their underlying instruction-tuned model produces students that are significantly more likely than their teachers to admit their hidden behavior when asked, suggesting that knowledge of the behavior transferred more readily than the propensity to conceal it. Confession gains largely disappear when the student does not share the teacher's pretrained base, so DFI should target the teacher's own pre-RL checkpoint, which is weaker than the teacher but shares its base model. Distillation for Capabilities (DFC) aims to transfer capabilities but not misalignment. Among several techniques we evaluate, two are effective: inoculation prompting and training for more epochs on fewer unique examples. Both preserve the capability gains of standard distillation while substantially reducing the subliminal transfer of an animal preference, our proxy for misalignment. Together, these findings demonstrate two ways distillation can be used for AI safety: incriminating misaligned models, and extracting their capabilities without their misalignment.
 

Subjects:

Artificial Intelligence (cs.AI)

Cite as:

arXiv:2610.11012
 [cs.AI]

 

(or 

arXiv:2610.11012v1
 [cs.AI]
 for this version)
 

 

 
https://doi.org/10.48550/arXiv.2610.11012

Focus to learn more

 arXiv-issued DOI via DataCite (pending registration)

## Submission history

 From: Sebastian Prasanna [
view email
] 
 
[v1]

 Wed, 7 Oct 2026 23:51:11 UTC (495 KB)

 

Full-text links:

## Access Paper:

* View PDF
* HTML (experimental)
* TeX Source

view license

 

### Additional Features

* Audio Summary

### Current browse context:

cs.AI

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