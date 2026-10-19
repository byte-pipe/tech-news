---
title: AI Proved the Quasi-Riemann Hypothesis. What Happens Now? | Quanta Magazine
url: https://www.quantamagazine.org/ai-proved-the-quasi-riemann-hypothesis-what-happens-now-20261019
site_name: tldr
content_file: tldr-ai-proved-the-quasi-riemann-hypothesis-what-happen
fetched_at: '2026-10-19T17:20:44.006795'
original_url: https://www.quantamagazine.org/ai-proved-the-quasi-riemann-hypothesis-what-happens-now-20261019
date: '2026-10-19'
published_date: '2026-10-19T15:40:26+00:00'
description: Unlike other recent AI proofs, this one has been unpacked by human experts. The implications, one mathematician said, are “staggering.”
tags:
- tldr
---

Home

 AI Proved the Quasi-Riemann Hypothesis. What Happens Now? 

Save Article
 

Read Later

 

###### Share

Facebook

Copied!

Copy link

Email

Pocket

Reddit

Ycombinator

 

* Save ArticleRead LaterRead Later

number theory
 

# AI Proved the Quasi-Riemann Hypothesis. What Happens Now?

By 

Konstantin Kakaes

October 19, 2026

 

 Unlike other recent AI proofs, this one has been unpacked by human experts. The implications, one mathematician said, are “staggering.” 

Save Article
 

Read Later

 

The Riemann hypothesis is a fundamental statement about the distribution of prime numbers.

Emily Buder/Quanta Magazine;Guan-Huei Wu forQuanta Magazine

## Introduction

Among the 377 results that OpenAIannouncedon October 6, 2026, one stood out. It claimed to settle the “quasi-Riemann hypothesis” — a weaker version of the Riemann hypothesis, which is arguably the biggest open question in math. The new proof is, asJared Duker Lichtmanof Stanford University put it, “the most significant AI-for-math achievement so far, by quite a margin.”

The Riemann hypothesis has been an open problem for over 160 years. Resolving it would enable mathematicians to better understand the nature of prime numbers, one of math’s most crucial building blocks. And that’s just for starters.

The implications of even the more limited “quasi-RH” result are “staggering,” saidMaksym Radziwiłłof New York University. “In a sense, the vast majority of consequences of RH already follow from quasi-RH.”

Moreover, contrary to what mathematicians had long expected, the proof didn’t need to introduce any new concepts — it instead unearthed hidden connections between old ones. “The proof is a surprising synthesis of well-known ideas,” saidAlexander Dunnof the Georgia Institute of Technology.

The result relied in part on techniques pioneered by Radziwiłł and Dunn. Alongside other number theorists, they have been working to understand the proof and what it could mean. Now they’re starting to get answers.

## To Zeta and Beyond

To understand what the quasi-Riemann hypothesis says, you first have to understand the Riemann hypothesis. When the Clay Mathematics Instituteannouncedseven Millennium Prize Problems at the turn of the century, the Riemann hypothesis loomed above the other six. It was the only one carried over from thecelebrated agenda-setting listof problems that David Hilbert had announced a century earlier.

On its surface, the conjecture concerns the behavior of a particular function. Start with the sum $latex 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \cdots $. Now use that sum (together with a special mathematical trick to extend its scope) to build a more general function, called the Riemann zeta (ζ) function:

$latex \zeta (s) = 1 + \frac{1}{2^s} + \frac{1}{3^s} + \frac{1}{4^s} + \cdots$

Here, the inputsis a complex number. Complex numbers have two parts — a “real” part and an “imaginary” part, which is a multiple of the square root of −1 (written asi). Any complex number can be thought of as a point on a plane:

 

Mark Belan/Quanta Magazine

The Riemann hypothesis is about which values ofswill make the zeta function equal zero.

But it is also about far more than how this particular function behaves. As Bernhard Riemann realized when he first made the conjecture in 1859, the function relates to patterns in the prime numbers — integers divisible only by 1 and themselves that many mathematicians call the “atoms of arithmetic.”

It’s long been known that as you move along the number line, the primes thin out. Riemann showed that exactlyhowthe primes thin out is, in a sense, governed by the zeta function — in particular by the places where it equals zero.

It’s straightforward to prove that ifsis a negative even number (−2, −4, −6, …), then ζ(s) = 0. These are called trivial zeros. The Riemann hypothesis says that the only other zeros of the zeta function, called nontrivial zeros, occur whenshas a real part of 1/2. That is, they should all be located on a vertical line:

 

If any nontrivial zero were to be found somewhere away from that vertical line, it would imply that the primes must form an extremely surprising pattern, one that has never been observed to date.

Just narrowing the area where the nontrivial zeros can appear has had huge ramifications. Riemann himself proved that nontrivial zeros of the zeta function can only be found in a vertical strip between zero and 1. Then, in 1896, two mathematicians showed that zeros could not lie on the edges of the strip. As a direct consequence, they were able to prove an important result called the prime number theorem, a formula for how quickly, on average, the primes thin out.

If the Riemann hypothesis holds, then mathematicians can guarantee that any deviations from the average given by the prime number theorem will always be small.

Mathematicians havenumerically verifiedthat the first 12 trillion nontrivial zeros are on the 1/2 line. But they can’t be sure the hypothesis holds for all the zeros, and even one solitary outlier would land like an earthquake. AsEnrico Bombieriwrote inthe paperlaying out the Millennium Prize formulation of the problem: “The failure of the Riemann hypothesis would create havoc in the distribution of prime numbers.”

## Diamonds in the Slop

This brings us to the quasi-Riemann hypothesis. Where the Riemann hypothesis posits that all the nontrivial zeros are on the vertical line at 1/2, the “quasi” version just asks one to prove that they are all contained in a vertical strip that’s narrower than the known strip between zero and 1. The narrower the strip, the more one can say about how the primes are distributed.

OpenAI announced two different versions of their quasi-Riemann hypothesis proof. The first version,dated September 30, 2026, claimed to show that all nontrivial zeros must be between 1/8 and 7/8, and was formally verified using the Lean programming language. The second version, which was completed almost aweek later(and is not yet formally verified), claimed to prove a weaker result: that the zeros must have a real part between 1/12 and 11/12. But while the first paper is 199 pages long, the second weighs in at a comparatively modest 49 pages.

As with many recent AI-generated results, both papers “are horribly written (in a way that would lead to immediate rejection at any mathematical journal),” Radziwiłł said in an email. “They fall short of the standard of exposition and clarity in our area by a wide margin.” And so mathematicians have set aside the 7/8 paper to focus on the 11/12 one, which seems to involve similar techniques and has similar consequences. “The reason why people look mostly at the 11/12 result is that it’s shorter,” Radziwiłł said.

 

Maksym Radziwiłł (top) and Alexander Dunn were surprised that OpenAI’s recent proof of the quasi-Riemann hypothesis used techniques they’d developed years earlier.

Caltech

Maksym Radziwiłł (left) and Alexander Dunn were surprised that OpenAI’s recent proof of the quasi-Riemann hypothesis used techniques they’d developed years earlier.

Caltech

Not coincidentally, the 11/12 result is the only one of the 722 OpenAI papers released on October 6 to have been edited by a person. OpenAI has not addressed inquiries about who that person is, or why this is the only paper to have had the benefit of human expertise before being released. In response to questions fromQuanta, the company said, “The paper is the result of work from everyone at OpenAI.”

Mathematicians have been studying the paper intensely in the couple of weeks since its release.Peter Sarnak, a prominent number theorist at Princeton University, has decided to repurpose a course he’s teaching this semester to study it. Radziwiłł says he can now sketch the proof’s arguments in half a page, while more involved write-ups by other mathematicians range from seven to 13 pages. (As of this writing, these have not yet been published, but are circulating privately.) These experts largely agree that the result is correct — and that its novelty lies in the way it brings together ideas from number theory that have been around for some time.

For decades, Sarnak has argued that mathematicians should approach the Riemann hypothesis by considering the zeta function as just one member of a broader family of functions, and then proving statements about that family. “But it was not clear exactly how to do so, or which family to consider,” saidMichael Rubinsteinof the University of Waterloo.

As it turns out, Sarnak had the right intuition. But the family that OpenAI’s model identified had previously been overlooked. The Rutgers University mathematicianHenryk Iwaniecnarrowly missed it in 2002, when he identified a number of closely related families in an effort to prove the Riemann hypothesis.

 

 By clicking to watch this video, you agree to our 
privacy policy.
 

Video: Alex Kontorovich, professor of mathematics at Rutgers University, breaks down the notoriously difficult Riemann hypothesis in this comprehensive explainer.

Emily Buder/Quanta Magazine; Guan-Huei Wu and Clay Shonkwiler for Quanta Magazine

Finding the right family required obscure mathematical objects called metaplectic forms, which Dunn has spent the past five years studying. “Nobody expected this,” he said. Metaplectic forms had been somewhat uncommon in number theory until now, he added, “so I hope this beautiful and esoteric theory gets the attention it deserves.”

To Dunn and Radziwiłł’s surprise, aformula they had provedin 2021 became a crucial ingredient in the proof (along with the work of numerous other mathematicians). In retrospect, Radziwiłł said, mathematicians who study the branch of number theory that all this work belongs to were mistaken in thinking that their tools weren’t strong enough to resolve the quasi-Riemann hypothesis. They’d been convinced that proving it would require techniques from another branch of number theory entirely. The AI model’s “belief” that their tools might be enough was a crucial perspective. “That was a pretty bold belief to have!” Radziwiłł said.

Mathematicians are both frustrated and excited by OpenAI’s work. Sarnak, for his part, said in an email that he won’t be satisfied that it’s “a Theorem” until humans check and understand all the details. But “the general feeling is one of relief,” Radziwiłł said. There are scores of results across not just number theory but also geometry and theoretical computer science that the proofs of quasi-Riemann will, in a swift stroke, establish as mathematical truths.

Number theorists are skeptical that the result’s particular combination of techniques will let them take the 7/8 bound down to the tantalizing 1/2. “It seems most likely to me that once mathematicians have fully internalized the new methods and worked through their implications, we will still feel as far off from the full Riemann hypothesis as we were before,” saidWill Sawinof Princeton. “But I am not certain of this.”

Thomas Bloom, a mathematician at the University of Manchester, agreed that the full Riemann hypothesis still seems out of reach. But, he added, “we would have said the same about quasi-RH a few weeks ago! At this point nothing would surprise me.”

 The Quanta Newsletter 

Get highlights of the most important news delivered to your email inbox

Email

Subscribe

## Also inMathematics

Is AI the End of Math As We Know It?

 

Qualia
 

### Is AI the End of Math As We Know It?

By 

Jordana Cepelewicz

October 5, 2026

Save Article
 

Read Later

What Does the Fourth Dimension Actually Look Like?

 

The Joy of Why
 

### What Does the Fourth Dimension Actually Look Like?

By 

Janna Levin

 +1 author

Steven Strogatz

October 1, 2026

Save Article
 

Read Later

Mathematicians Harness Randomness To Crack a 55-Year-Old Conjecture

 

combinatorics
 

### Mathematicians Harness Randomness To Crack a 55-Year-Old Conjecture

By 

Shalma Wegsman

September 28, 2026

Save Article
 

Read Later

 

## Next article

He Wants AI Benchmarking To Be a Science, Not a Dark Art