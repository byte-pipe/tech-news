---
title: '[2505.21411] Pangu Pro MoE: Mixture of Grouped Experts for Efficient Sparsity'
url: https://arxiv.org/abs/2505.21411
site_name: hackernews
fetched_at: '2025-07-03T07:04:49.296439'
original_url: https://arxiv.org/abs/2505.21411
author: buyucu
date: '2025-07-03'
description: 'Abstract page for arXiv paper 2505.21411: Pangu Pro MoE: Mixture of Grouped Experts for Efficient Sparsity'
---

# Computer Science > Computation and Language

arXiv:2505.21411
 (cs)


 [Submitted on 27 May 2025 (
v1
), last revised 28 May 2025 (this version, v2)]

# Title:Pangu Pro MoE: Mixture of Grouped Experts for Efficient Sparsity

Authors:
Yehui Tang
,
Xiaosong Li
,
Fangcheng Liu
,
Wei Guo
,
Hang Zhou
,
Yaoyuan Wang
,
Kai Han
,
Xianzhi Yu
,
Jinpeng Li
,
Hui Zang
,
Fei Mi
,
Xiaojun Meng
,
Zhicheng Liu
,
Hanting Chen
,
Binfan Zheng
,
Can Chen
,
Youliang Yan
,
Ruiming Tang
,
Peifeng Qin
,
Xinghao Chen
,
Dacheng Tao
,
Yunhe Wang
 (and Other Contributors)

View a PDF of the paper titled Pangu Pro MoE: Mixture of Grouped Experts for Efficient Sparsity, by Yehui Tang and 21 other authors

View PDF

HTML (experimental)

Abstract:
The surgence of Mixture of Experts (MoE) in Large Language Models promises a small price of execution cost for a much larger model parameter count and learning capacity, because only a small fraction of parameters are activated for each input token. However, it is commonly observed that some experts are activated far more often than others, leading to system inefficiency when running the experts on different devices in parallel. Therefore, we introduce Mixture of Grouped Experts (MoGE), which groups the experts during selection and balances the expert workload better than MoE in nature. It constrains tokens to activate an equal number of experts within each predefined expert group. When a model execution is distributed on multiple devices, this architectural design ensures a balanced computational load across devices, significantly enhancing throughput, particularly for the inference phase. Further, we build Pangu Pro MoE on Ascend NPUs, a sparse model based on MoGE with 72 billion total parameters, 16 billion of which are activated for each token. The configuration of Pangu Pro MoE is optimized for Ascend 300I Duo and 800I A2 through extensive system simulation studies. Our experiments indicate that MoGE indeed leads to better expert load balancing and more efficient execution for both model training and inference on Ascend NPUs. The inference performance of Pangu Pro MoE achieves 1148 tokens/s per card and can be further improved to 1528 tokens/s per card by speculative acceleration, outperforming comparable 32B and 72B Dense models. Furthermore, we achieve an excellent cost-to-performance ratio for model inference on Ascend 300I Duo. Our studies show that Ascend NPUs are capable of training Pangu Pro MoE with massive parallelization to make it a leading model within the sub-100B total parameter class, outperforming prominent open-source models like GLM-Z1-32B and Qwen3-32B.


Subjects:

Computation and Language (cs.CL)

Cite as:

arXiv:2505.21411
 [cs.CL]

 

(or

arXiv:2505.21411v2
 [cs.CL]
 for this version)


 


https://doi.org/10.48550/arXiv.2505.21411

Focus to learn more

 arXiv-issued DOI via DataCite

## Submission history

 From: Hang Zhou [
view email
]

[v1]

 Tue, 27 May 2025 16:40:21 UTC (710 KB)

[v2]

 Wed, 28 May 2025 10:42:15 UTC (710 KB)



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
2025-05

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
