---
title: 'Chinese NGCC Algorithms: The First Week of AI Cryptanalysis'
url: https://eprint.iacr.org/2026/2266
site_name: tldr
content_file: tldr-chinese-ngcc-algorithms-the-first-week-of-ai-crypt
fetched_at: '2026-09-30T16:40:46.803770'
original_url: https://eprint.iacr.org/2026/2266
date: '2026-09-30'
published_date: '2026-09-29T18:59:24+00:00'
description: 'Chinese NGCC Algorithms: The First Week of AI Cryptanalysis'
tags:
- tldr
---

#### Paper 2026/2266

### Chinese NGCC Algorithms: The First Week of AI Cryptanalysis

Markku-Juhani O. Saarinen
, Tampere University

##### Abstract

On September 20, 2026, the Chinese Institute of Commercial Cryptography Standards published the 119 first-round candidates of its Next-generation Commercial Cryptographic Algorithms (NGCC) program: 34 signature schemes, 41 key encapsulation mechanisms, 9 key exchange protocols, and 35 hash functions. The program follows the template of the open NIST competitions for AES, SHA-3, and post-quantum cryptography. It opened just after cryptographers' ``Lee Sedol moment'' in the summer of 2026, when AI analysis overtook humans in analyzing the HAWK signature scheme. During the first 7 days of the NGCC competition, according to our harvested sources, 191 active findings were published for 89 candidates, 78 of them rated Critical: universal forgeries, signing-key recovery, trivial hash collisions, broken implicit rejection, and seeds too short for the claimed security level. Our independent evaluation effort discovered, verified, and disclosed 110 of those issues (47 Critical) using the agentic workflow described in this work; outside researchers, some AI-assisted, found the rest. Early AI-assisted findings mostly concerned implementations; by the end of the week, reproduced AI-assisted attacks also included new design-level key recovery. We describe the workflow, review loop, classification ruleset, and observed failure modes. As part of the evaluation, we also benchmarked all algorithm candidates and found that NGCC hash selection may significantly affect final public-key performance, as candidate implementations spend a large share of their cycles on ``placeholder'' hashes.

Note:Project web site: https://ngcc.dev/

##### Metadata

 Available format(s)
 

PDF

Category

Attacks and cryptanalysis

Publication info

Preprint. 

Keywords

cryptanalysis
AI agents
post-quantum cryptography
standardization
side channels
vulnerability discovery

Contact author(s)

 markku-juhani saarinen
 @ 
tuni fi
 

History

2026-09-30: approved

2026-09-29: received

See all versions

Short URL

https://ia.cr/2026/2266

License

CC BY

BibTeXCopy to clipboard

@misc{cryptoeprint:2026/2266,
 author = {Markku-Juhani O. Saarinen},
 title = {Chinese {NGCC} Algorithms: The First Week of {AI} Cryptanalysis},
 howpublished = {Cryptology {ePrint} Archive, Paper 2026/2266},
 year = {2026},
 url = {https://eprint.iacr.org/2026/2266}
}