---
title: '[2605.08419] Deterministic Fully-Static Whole-Binary Translation without Heuristics'
url: https://arxiv.org/abs/2605.08419
site_name: hackernews_api
content_file: hackernews_api-260508419-deterministic-fully-static-whole-binary
fetched_at: '2026-05-13T19:36:38.399230'
original_url: https://arxiv.org/abs/2605.08419
author: matt_d
date: '2026-05-13'
description: 'Abstract page for arXiv paper 2605.08419: Deterministic Fully-Static Whole-Binary Translation without Heuristics'
tags:
- hackernews
- trending
---

# Computer Science > Cryptography and Security

arXiv:2605.08419
 (cs)
 

 [Submitted on 8 May 2026]

# Title:Deterministic Fully-Static Whole-Binary Translation without Heuristics

Authors:
Hongyu Chen
, 
James McGowan
, 
Michael Franz
 
View a PDF of the paper titled Deterministic Fully-Static Whole-Binary Translation without Heuristics, by Hongyu Chen and 2 other authors

View PDF

HTML (experimental)

Abstract:
We present Elevator, the first binary translator that statically translates entire x86-64 executables to AArch64 without debug information, source code, or assumptions about code layout. Unlike existing systems, which rely on heuristics or runtime fallbacks to handle code-versus-data decoding errors, Elevator considers all possible interpretations of every byte and produces a separate translation for each feasible one ahead of time. Any byte may be interpreted as data, an opcode, or an opcode argument; we generate separate control flow paths for all interpretations, pruning only those leading to abnormal termination.

Translations are built by composing code "tiles" automatically derived from a high-level description of the source ISA, yielding a nimble translation framework. The approach is deterministic and produces complete, self-contained binaries with no runtime component in the trusted code base. The principal cost is substantial code size expansion. The key benefit is that the output is the actual code that will run, enabling testing, validation, certification, and cryptographic signing prior to deployment, reducing risk compared to emulators or JIT compilers.

We evaluate Elevator on a diverse corpus of real-world binaries, including the entire SPECint 2006 suite, demonstrating that static full-program binary translation can be both reliable and practical. Elevator achieves performance on par with or better than QEMU's user-mode JIT emulation.
 

Subjects:

Cryptography and Security (cs.CR)
; Programming Languages (cs.PL)

Cite as:

arXiv:2605.08419
 [cs.CR]

 

(or 

arXiv:2605.08419v1
 [cs.CR]
 for this version)
 

 

 
https://doi.org/10.48550/arXiv.2605.08419

Focus to learn more

 arXiv-issued DOI via DataCite

## Submission history

 From: Hongyu Chen [
view email
] 
 
[v1]

 Fri, 8 May 2026 19:25:06 UTC (332 KB)

 

Full-text links:

## Access Paper:

* View PDF
* HTML (experimental)
* TeX Source

view license

 

### Current browse context:

cs.CR

< prev

  |  
 

next >

new

 | 

recent

 | 
2026-05

 Change to browse by:
 

cs

cs.PL

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