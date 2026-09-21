---
title: A class of statement between conjecture and theorem — LessWrong
url: https://www.lesswrong.com/posts/ZnNvci7jk9qEGr3z3/a-class-of-statement-between-conjecture-and-theorem
site_name: tldr
content_file: tldr-a-class-of-statement-between-conjecture-and-theore
fetched_at: '2026-09-21T16:50:09.527535'
original_url: https://www.lesswrong.com/posts/ZnNvci7jk9qEGr3z3/a-class-of-statement-between-conjecture-and-theorem
date: '2026-09-21'
description: Parts of the math community, such as Henry Cohn and Grant Sanderson, are arguing that proofs have been a proxy for understanding, and now that proxy…
tags:
- tldr
---

Parts of the math community, such as Henry Cohn and Grant Sanderson, arearguingthatproofs have been a proxy for understanding, and now that proxy is broken. This is a response to LMs generatingincomprehensible proofs, often formalized in Lean. While the proofs are verified, they lack the pedagogical value which has historically come along with new proofs. In the past we could typically assume at least one human in the world understood the novel insight required to produce a proof[1], but that assumption no longer holds.

I suspect we will need a new class of statement which contains statements which are proved but not understood, something the mathematical community can formally recognize as a contribution to the field. The understanding gives us the tools to do math, and the proof verifies that our understanding is correct, so we should ensure we have the language to communicate the state of both.

For now I will call this class of statement acompertum(Latin, neuter ofcompertus, ascertained; fromcomperire, to find out for certain). Aconjectureis from the Latinconicere, to throw together: an inference assembled from the evidence. Atheoremis from the Greektheōrēma, that which is looked at or beheld, from the same root as theory and theater. A compertum is something ascertained but not yet beheld, logically sitting between a conjecture and a theorem, a statement whose truth is known but not yet understood. I am curious what name the community lands on.

A recently resolved Erdős conjecture is a good example of a statement which moved from a conjecture to a compertum to a theorem. In April, Liam Price prompted GPT-5.4 Pro with Erdős Problem 1196 (a conjecture) and posted the resulting proof sketch to theErdős Problems forum. The sketch was correct, and was then formalized in Lean (now a compertum), but the proof strategy was unfamiliar to people who had worked on the problem. In May, apaperby Alexeev, Lichtman, Tao, and five coauthors converted the sketch into a general method that the authors could explain and reuse (now a theorem), and with it proved a second Erdős conjecture and created a short new proof of the Erdős Primitive Set Conjecture. The transition from compertum to theorem was significant even though the statement was already proved: the understanding produced proofs for other problems.

One difficulty is measuring when a proof is understood, identifying that threshold for when a compertum passes into being a theorem. If we want to keep with the historical measure, as long as a person can write a correct proof on their own, then we know at least one person understands the proof. I think an interesting alternative would be an explainer (paper, blog, video, etc.) from which a peer reviewer can write a formal proof.

How exactly we define the threshold between this new class of statement and a theorem needs more thought, but I expect the existence of a new class of statement will become increasingly useful as proofs become increasingly opaque.

1. ^There have been computer-assisted proofs in the past, such as the Four Color Theorem and Hales's proof of the Kepler conjecture. In those cases a human reduced the problem to a large number of simple cases, which a computer then checked. That is closer to using a computer as a calculator than to a computer generating the insight a proof requires. This is a continuum, of course. Computers are now used for everything from evaluating expressions to finding and applying techniques from distant areas of math.We also have proofs which are the result of such large collaborations that no individual understands the whole proof, such as the classification of finite simple groups. This looks similar to mathematics as a whole: no person understands the entire field, but each step between lemmas and theorems is understood.