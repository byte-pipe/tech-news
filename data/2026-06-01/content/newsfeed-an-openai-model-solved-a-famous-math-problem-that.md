---
title: An OpenAI model solved a famous math problem that stumped humans for 80 years - Ars Technica
url: https://arstechnica.com/ai/2026/06/openais-math-breakthrough-played-to-ais-strengths/
site_name: newsfeed
content_file: newsfeed-an-openai-model-solved-a-famous-math-problem-that
fetched_at: '2026-06-01T20:30:04.658743'
original_url: https://arstechnica.com/ai/2026/06/openais-math-breakthrough-played-to-ais-strengths/
date: '2026-06-01'
published_date: '2026-06-01T11:00:00+00:00'
description: I tried to explain OpenAI’s solution more clearly than OpenAI did.
tags:
- ars-technica
- ai
- features
- science
---

Text
 settings

In mid-May, OpenAIannouncedthat an internal AI model had disproved the Erdős unit distance conjecture, a famous problem in discrete geometry that had stumped human mathematicians for the last 80 years.

OpenAI gave several mathematicians early access to the result andpublished their reactions.Tim Gowers—who won the Fields Medal, the most prestigious prize in mathematics—wrote that “there is no doubt that the solution to the unit-distance problem is a milestone in AI mathematics.”

University of Toronto professorDaniel Littwrote that “this is the first example of a result produced autonomously by an AI that I find exciting in itself, as opposed to as a leading indicator.”

It’s arguably the first time that an AI system has found a proof resolving a major open conjecture. That’s impressive, but I don’t view it as a radical break from the previous trajectory of AI progress in mathematics.

Three years ago, LLMs struggled to solve arithmetic problems. It was only last year that LLMs startedacing high school mathematics competitions.

When I attended the Joint Mathematics Meetings—the largest annual mathematics conference in the world—in January, I learned that AI systems were starting to contribute to mathematical research, but only in constrained settings. It took significant human interpretation to turn an AI output into a publishable theorem.

OpenAI’s new result is the next step in this progression. The AI model cleverly applied existing ideas drawn from several subfields of mathematics to create a full proof. But it didn’t pioneer any genuinely new techniques. The result has since beencleaned upandextendedby human mathematicians.

This points to a medium-term future where human mathematicians and AI models complement each other: AIs have a broader knowledge of past work than any human alive and much more willingness to grind through tedious proof strategies that aren’t likely to work. But humans can still think more deeply about any one problem and ask more interesting questions.

That might not last. AI systems have been improving at math so rapidly that it’s unclear what role, if any, human mathematicians will play a decade from now.

## The unit distance problem

Paul Erdőswas one of the most prolific mathematicians in history. He wrote over 1,500 papers in his lifetime, the most ever. One of his greatest talents was coming up with problems that are simple to state but have deep roots.

In 1946, he introduced theunit distance problem. Imagine you have some points in a 2D plane and you measure the distance between each pair of points:

Credit:
 Kai Williams / Understanding AICredit:

 
 Kai Williams / Understanding AI

In this diagram, there are five points and ten pairs of points. Three pairs happen to be exactly 1 unit apart: AD, BE, and CE.

Can we rearrange the points so that more pairs of points are exactly 1 unit apart?

Yes. For instance, we could move points A and D to be closer to the B, C, and E cluster. With a bit more work, we could further rearrange the points so that there are seven pairs exactly one unit apart. But that’s the most we can do.

We could do the same analysis with 6 points, 7 points, and so on. But as the number of points grows, the problem very quickly becomes too complicated to find the exact answer.

 The arrangements of 5, 6, 7, 8, and 9 points that have the most pairs of points exactly one unit apart. Figure from the appendix of “The Erdős unit distance problem for small point sets” by Boris Alexeev, Dustin G. Mixon, and Hans Parshall showing the optimal arrangements for 5 through 9 points. Alexeev et al. give the optimal solutions through 21 points; the question is open after that.
 

 Credit:
 
Boris Alexeev et al.

 The arrangements of 5, 6, 7, 8, and 9 points that have the most pairs of points exactly one unit apart. Figure from the appendix of “The Erdős unit distance problem for small point sets” by Boris Alexeev, Dustin G. Mixon, and Hans Parshall showing the optimal arrangements for 5 through 9 points. Alexeev et al. give the optimal solutions through 21 points; the question is open after that.

 

 Credit:

 

 
 Boris Alexeev et al.

 

So instead of asking exactly how many unit distances are possible for a given number of points, Erdős tried to calculate upper and lower bounds on the number of length-one lines for npoints, assuming that n is a large number.

To help calculate a lower bound, Erdős assumed that the points would be laid out in a grid. This is probably not the optimal layout, but if he could demonstrate that points in a grid have a certain number of pairs with unit distance, then the optimal arrangement must have at least that number.

 If we make the grid smaller, we can intersect more grid points with the unit circle. This gives more unit distances.
 

 Credit:
 Kai Williams / Understanding AI
 

 If we make the grid smaller, we can intersect more grid points with the unit circle. This gives more unit distances.

 

 Credit:

 
 Kai Williams / Understanding AI

 

The simplest option is to space the grid so that every point is distance 1 from its neighbors directly above, below, left, and right. However, Erdős saw that you could do even better if you took diagonals into account. If you make the grid spacing smaller, you can make each point be distance 1 from a greater number of neighbors. In the diagram above, if the grid spacing is 1, then each individual point is one unit away from four neighbors (the left panel). Instead, if the grid spacing is ⅕ (as shown on the right), then each individual point is one unit away from 12 neighbors:

 An animation of the distance-one neighbors of nine central points in a 13×13 grid. You can draw similar circles for other points in the grid to get the remaining distance-one pairs, but some points on the circle won’t land on grid points.
 

 Credit:
 Kai Williams / Understanding AI
 

 An animation of the distance-one neighbors of nine central points in a 13×13 grid. You can draw similar circles for other points in the grid to get the remaining distance-one pairs, but some points on the circle won’t land on grid points.

 

 Credit:

 
 Kai Williams / Understanding AI

 

OpenAI’s write-up of its new result included a confusing diagram showing points in a grid with a bunch of lines connecting them. The diagram becomes easier to understand if we superimpose a circle like this:

 A diagram from OpenAI’s announcement of the AI’s disproof of the unit distance conjecture, onto which I superimposed a circle showing the distance-one neighbors for one point. The grid spacing here is 1/√65, which produces unit circles that intersect 16 points on the grid (or would if the grid were larger).
 

 Credit:
 Kai Williams / Understanding AI
 

 A diagram from OpenAI’s announcement of the AI’s disproof of the unit distance conjecture, onto which I superimposed a circle showing the distance-one neighbors for one point. The grid spacing here is 1/√65, which produces unit circles that intersect 16 points on the grid (or would if the grid were larger).

 

 Credit:

 
 Kai Williams / Understanding AI

 

This works because of the Pythagorean theorem, which states that if we have a point that is a units to the right and b units above another point, the distance c between those two points satisfies a² + b² = c². The trick is to choose some number c² so that there are a whole bunch of pairs of whole numbers a and b such that a² + b² = c². Then, if we scale the grid down so that each point is 1/c from its neighbors, there will be a bunch of unit distances.

For example, if we choose c² = 25, then the Pythagorean equation can be satisfied by either 0² + 5² = 25 or 3² + 4² = 25. This corresponds to the 12-grid-point circle I showed earlier, with points at (0,5), (3,4), (4,3), (5,0), (-4,3), (-3,4), and so forth. (Technically, these lengths should all be divided by 5 — (⅗, ⅘) for example—but I’m leaving the denominators out for clarity.)

OpenAI’s diagram is based on choosing c² = 65, which can be satisfied by either 1² + 8² = 65 or 4² + 7² = 65. This means that if the grid spacing is 1/√65, each point will be one unit away from 16 other points: (1,8), (4,7), (7,4), (8,1), (-1,8), (-4,7), and so forth. Larger values for c²—if they’re chosen carefully—enable more whole-number diagonals and hence more unit-distance pairs.

However, if c² is too large compared to the number of points in the grid, then many of the potential one-unit-away neighbors will be outside the grid.

In short, we want to choose a c² that’s large enough but not too large. Using insights from number theory, includingJacobi’s two-square theorem, Erdős was able to show that an optimally sized circle will enable the number of unit-distance pairs to grow faster than the number of points, but only barely.

The question became “can you do better?” To find an upper bound, Erdős used an argument from a quite different area of mathematics called graph theory to show that you could only have so many unit distances. But his upper bound grows much, much faster than the best lower bound he was able to construct.

Erdős’s conjecture was that the actual optimum was much closer to the lower bound than the upper one. He predicted, but couldn’t prove, that the maximum number of unit-distance pairs grows just barely faster than the number of points.

To be more precise, Erdős conjectured that the number of unit distances would be n^(1+o(1)). In other words, for a sufficiently large n, the maximum number of unit distances would be less than n^(1+𝜖) for any 𝜖 > 0. That could end up growing a little faster than his lower-bound construction—which was n^(1 + C/(log log n)) for some constant C—but within the same general ballpark.

Proving his guess became known as the unit distance problem. For the next 80 years, it looked like Erdős was right.

Then an OpenAI model proved him wrong.

## The AI’s approach

Erdős’s conjecture assumed that, at least for a large number of points, a square grid could yield about as many unit-distance pairs as organizing the points in other ways. OpenAI’s AI proved this wrong by demonstrating that there was another, more complex way to organize n points that allowed more pairs to be exactly one unit apart.

Precisely because the new pattern of points is more complicated, it’s tricky to explain it concisely. But you can think of it as a clever modification of Erdős’s grid.

The AI constructed a grid in a high-dimensional space and then projected this more complex structure into two dimensions. And instead of using a whole-number grid with points like (1,3) or (-3,6), the AI construction used something called algebraic integers to build this more complicated grid. It turns out that this kind of higher-dimensional grid has richer structure, which allows the AI to pack more unit distances into the same number of points.

It’s hard to illustrate this alternative arrangement of points because it only becomes advantageous with a very large number of points. But here’s a simpler arrangement of points that was constructed in a similar way. You canclick hereif you want to play with the illustration yourself.

It has 1,345 points and only produces 5,916 unit distances, fewer than the 7,632 unit distances that a square 1,296-point grid produces using the Erdős technique. But I think it gives a sense of how a pattern that isn’t a grid could produce more unit distances than a square grid.

 A simplified visualization of what the AI model’s arrangement might look like. The 12 red lines emanating from the center are each length one. Click the interactive link to play around with the visualization. Image created with help from ChatGPT, based on an idea by Will Sawin, one of the mathematicians involved in the work.
 

 Credit:
 Kai Williams / Understanding AI
 

 A simplified visualization of what the AI model’s arrangement might look like. The 12 red lines emanating from the center are each length one. Click the interactive link to play around with the visualization. Image created with help from ChatGPT, based on an idea by Will Sawin, one of the mathematicians involved in the work.

 

 Credit:

 
 Kai Williams / Understanding AI

 

The more complicated patterns pay off. While the OpenAI model’s proof does not explicitly state how many unit-distance pairs are possible for n points, human mathematician Will Sawin was able toshowthat it grows at least at the rate of n1.014. This might seem small, but asngets really big, this number will become much larger than the counts produced by the Erdős approach.

That being said, the AI’s result doesn’t completely resolve the problem. Our best upper bound for the number of unit distances is around n1.333. More work is needed to close this gap.

## How does this result fit into AI for mathematics?

If you’d asked me two weeks ago—before OpenAI’s announcement—about the most novel contributions of LLMs to mathematics, I probably would have pointed to theAlphaEvolvesystem from Google DeepMind.

AlphaEvolve harnesses LLMs to be the engine of an optimization process. If you can turn a math problem into a piece of code to optimize, which you often can, the LLM might find better solutions than humans have for certain types of problems. In November, four mathematicians (includingTerence Tao) released apaperthat analyzed AlphaEvolve’s performance on 67 optimization problems across the mathematical literature. They found that AlphaEvolve was able to improve on the established literature in some cases.

This was a step up in autonomy from previous LLM contributions, such as literature review, but it still required humans to frame it as an optimization problem and turn the AI’s output into usable mathematics. And only certain types of problems are amenable to this approach. More conceptual questions that don’t include a number to optimize can’t easily be studied with AlphaEvolve.

So AI companies have been working to develop LLM systems that can directly output a correct solution to any math problem. OpenAI’s result is a substantial step in that direction. But it also fits the pattern of previous AI-assisted mathematics.

For one thing, other companies have also worked to solve Erdős problems. Because Erdős posed hundreds of problems over his career—and because mathematician Thomas Bloom has organized an effort to compile all of them atwww.erdosproblems.com—AI companies have used them as a testing ground to evaluate AI systems. In January, Cambridge undergraduate Kevin Barreto worked with a friend to ask GPT-5.2 and Harmonic’s Aristotle to produce the firstautonomous solutionof an Erdős problem. On May 22, two days after OpenAI’s announcement, Googleannouncedthat its AI system had solved nine open Erdős problems, including two that had been open for over 50 years.

To be clear, the problem that OpenAI solved is more impressive than any of the other work I just mentioned. But OpenAI’s solution is more in line with past AI efforts than the headline result might suggest.

One reason the unit distance problem was unsolved for 80 years, despite being so well known, is that most people thought Erdős’s conjecture was true. But the mathematical tools we have are nowhere close to being able to prove Erdős’s bound. So mathematicians expected that any proof of the conjecture would involve major new ideas or approaches.

Instead, as we’ve seen, the AIdisprovedthe conjecture by making an extension of Erdős’s initial construction. It was a clever and nonobvious solution, but it also bore some similarity to the kind of optimization work done by a system like AlphaEvolve.

This dynamic is reflected in some of the mathematicians’ responses. Mathematician Tim Gowers wrote that when he first heard about the AI’s result, he thought it had proved the theorem. “I spent the evening adjusting my world view: If the AI could come up with a proof like that, then maybe it would be all over for mathematicians very soon.”

But the next morning, Gowers and other external reviewers received an email about the result, and he realized that the LLM “had disproved the conjecture rather than proving it, which came as a big relief.”

OpenAI’s solution also had two properties that played to the strengths of AI models relative to humans.

First, the eventual solution relied on applying sophisticated techniques from a quite different area of mathematics: algebraic number theory. AI systems have been trained on huge swaths of mathematics—and there’sa lotof math out there—so they have a broader knowledge of previous mathematical work than any human in the world. For a human to solve this, they would have needed to have the relevant algebraic number theory knowledge while also being interested in the unit distance problem, a rare combination.

Second, the reasoning process was such a grind, and seemingly unlikely to succeed, that most humans would not have thought it worth the trouble.Jacob Tsimerman, a University of Toronto professor, remarked in theOpenAI documentthat he had briefly considered taking a similar approach to disprove the conjecture. But that type of technique “consumes much time and frequently doesn’t work out,” so he abandoned the project.

An AI, on the other hand, can work through many proof strategies that don’t work out before discovering one that does. OpenAI could have run the problem many times before a model found a solution. Indeed, an OpenAI chart revealed that even with the maximum token budget, the internal model solves the problem only half of the time.

To be clear, what the AI system did is still impressive. “It’s always tempting to look at a completed proof and declare it obvious after the fact,” Tsimerman said later in his remark. But as I noted previously, it also played to the strengths of AI systems.

In the short to medium term, this points to a world where AI models complement humans but do not replace them. AI systems will tackle lists of problems curated by human mathematicians or aid humans in finding relevant approaches from seemingly unrelated mathematical fields. But they won’t immediately displace the human role in choosing which questions to ask or developing wholly new techniques.

Even this result was very much a human-AI collaboration. While the AI system found the proof on its own, human mathematicians verified the result. Other humans came up with better-written proofs that extended the AI’s initial ideas, like Will Sawin finding an explicit lower bound as I mentioned above.

It’s unclear how long this complementarity will last, however. Gowers spent the rest of his comment exploring whether the relief he felt on hearing that AI had disproved the conjecture was justified. He more or less concluded that it was, but in a footnote, he wrote that he would guess “that AI will soon reach a high level at other activities such as building theories, formulating definitions and asking interesting questions.”

In the past year, we’ve gone from AI systems that hadn’t yet beaten high school mathematics competitions to ones that can advance mathematics in interesting ways. It seems likely that AI systems will continue to become more autonomous when working on mathematical problems.

At the same time, we haven’t fully explored what current models can achieve in math. Soon after OpenAI’s announcement, University of Michigan postdoc Xiao Mafoundthat GPT-5.5 was also able to prove Erdős wrong if given a small hint. If a generally available model could disprove this famous conjecture and no one noticed, what other discoveries could happen today that no one has thought to try?

Kai Williamsis a reporter forUnderstanding AI, a Substack newsletter founded by Ars Technica alum Timothy B. Lee. His work is supported by aTarbell Fellowship.Subscribe to Understanding AIto get more from Tim and Kai.

1. 1.Fed up with vibe coders, dev sneaks data-nuking prompt injection into their code
2. 2.OpenAI’s math breakthrough played to AI’s strengths
3. 3.Here's why the failure of Blue Origin's New Glenn rocket is so catastrophic
4. 4.Rocket Report: A dark day for Blue Origin; Pentagon eyes new launch site
5. 5.Proposed new US funding rules: We can cancel any grant at any time

Customize