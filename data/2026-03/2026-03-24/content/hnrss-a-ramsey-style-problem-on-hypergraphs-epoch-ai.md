---
title: A Ramsey-style Problem on Hypergraphs | Epoch AI
url: https://epoch.ai/frontiermath/open-problems/ramsey-hypergraphs
site_name: hnrss
content_file: hnrss-a-ramsey-style-problem-on-hypergraphs-epoch-ai
fetched_at: '2026-03-24T20:01:08.650296'
original_url: https://epoch.ai/frontiermath/open-problems/ramsey-hypergraphs
date: '2026-03-24'
description: Construct hypergraphs as large as possible that do not have a certain easy-to-check, difficult-to-find property.
tags:
- hackernews
- hnrss
---

Solution Update: This problem has been solved! A solution was first elicited by Kevin Barreto and Liam Price, using GPT-5.4 Pro. This solution was confirmed by problem contributor Will Brian, and will be written up for publication. A full transcript of the original conversation with GPT-5.4 Pro can be foundhereand GPT-5.4 Pro’s write-up from the end of that transcript can be foundhere.

Brian’s comments: “This is an exciting solution to a problem I find very interesting. I had previously wondered if the AI’s approach might be possible, but it seemed hard to work out. Now I see that it works out perfectly. It eliminates an inefficiency in our lower-bound construction and in some sense mirrors the intricacy of our upper-bound construction. The matching lower and upper bounds are quite good for Ramsey-theoretic problems, and I’m interested in further understanding why this works out so well.”

Brian plans to write up the solution for publication, possibly including follow-on work spurred by the AI’s ideas. Barreto and Price have the option of being coauthors on any resulting papers. We will update this page with links to future work.

Subsequent to this solve, we finished developing our general scaffold for testing models on FrontierMath: Open Problems. In this scaffold, several other models were able to solve the problem as well:Opus 4.6 (max),Gemini 3.1 Pro, andGPT-5.4 (xhigh).

Original Description: This problem is about improving lower bounds on the values of a sequence, \(H(n)\), that arises in the study of simultaneous convergence of sets of infinite series, defined as follows.

A hypergraph \((V,\mathcal H)\) is said to contain apartitionof size \(n\) if there is some \(D \subseteq V\) and \(\mathcal P \subseteq \mathcal H\) such that \(\|D\| = n\) and every member of \(D\) is contained in exactly one member of \(\mathcal P\). \(H(n)\) is the greatest \(k \in \mathbb{N}\) such that there is a hypergraph \((V,\mathcal H)\) with \(\|V\| = k\) having no isolated vertices and containing no partitions of size greater than \(n\).

It is believed that the best-known lower bounds for \(H(n)\) are suboptimal, even asymptotically, and that they can be improved by finding new constructions of hypergraphs. The goal of this problem is to find such a construction.

Warm-up: we ask for a value of \(n\) where constructions are already known.

Single Challenge: we ask for a value of \(n\) for which no construction is known, and which is probably too hard to brute-force.

Full Problem: we ask for a general algorithm for all \(n\).




## Attempts by AI



We have evaluated the following models on this problem. “Warm-up” refers to an easier variant of the problem with a known solution.

## AI Prompts






### Warm-up



Copy



A hypergraph (V, H) is said to contain a partition of size n if there is some D ⊆ V and P ⊆ H such that |D| = n and every member of D is contained in exactly one member of P. Find a hypergraph (V, H) with no isolated vertices such that |V| ≥ 64, |H| ≤ 20, and (V, H) contains no partitions of size > 20.

Output the hypergraph as a string where vertices are labeled, 1, ..., |V|, and edges are denoted with curly braces. Example: {1,2,3},{2,4},{3,4,5},{1,5}






### Single challenge



Copy



A hypergraph (V, H) is said to contain a partition of size n if there is some D ⊆ V and P ⊆ H such that |D| = n and every member of D is contained in exactly one member of P. Find a hypergraph (V, H) with no isolated vertices such that |V| ≥ 66, |H| ≤ 20, and (V, H) contains no partitions of size > 20.

Output the hypergraph as a string where vertices are labeled, 1, ..., |V|, and edges are denoted with curly braces. Example: {1,2,3},{2,4},{3,4,5},{1,5}






### Full problem



Copy



A hypergraph (V, H) is said to contain a partition of size n if there is some D ⊆ V and P ⊆ H such that |D| = n and every member of D is contained in exactly one member of P. Define H(n) to be the largest integer k such that there is a hypergraph (V, H) with |V| = k having no isolated vertices and containing no partitions of size greater than n.

It is known that H(n) ≥ k_n, where k_n is defined recursively by the formula k_1 = 1 and k_n = ⌊n/2⌋ + k_⌊n/2⌋ + k_⌊(n+1)/2⌋.

Your task is to improve this lower bound by a constant factor, i.e. show that H(n) ≥ c*k_n for some c > 1. It is acceptable if this improvement does not work for small n, but it must already be "in effect" for n=15. You must demonstrate this improvement by providing an algorithm that takes n as input and produces a hypergraph witnessing H(n) ≥ c * k_n.

Please provide an algorithm that takes n as input and outputs the witness hypergraph as a string where vertices are labeled, 1, ..., |V|, and edges are denoted with curly braces. Example: {1,2,3},{2,4},{3,4,5},{1,5}

Solution format:
* Write a Python script defining a function `solution(n: int) -> str`.
* Do not include any code at the file level. You may include a `main` block for testing, but it will not be executed by the verifier.
* For n ≤ 100, the algorithm must complete within 10 minutes when run on a typical laptop.





## Mathematician survey



The author assessed the problem as follows.




Number of mathematicians highly familiar with the problem:

a majority of those working on a specialized topic (≈10)

Number of mathematicians who have made a serious attempt to solve the problem:

5–10

Rough guess of how long it would take an expert human to solve the problem:

1–3 months

Notability of a solution:

moderately interesting

A solution would be published:

in a standard specialty journal

Likelihood of a solution generating more interesting math:

fairly likely: the problem is rich enough that most solutions should open new avenues

Probability that the problem is solvable as stated:

95-99%
