---
title: Brute intelligence - by Benn Stancil - benn.substack
url: https://benn.substack.com/p/brute-intelligence
site_name: tldr
content_file: tldr-brute-intelligence-by-benn-stancil-bennsubstack
fetched_at: '2026-07-29T12:28:39.083049'
original_url: https://benn.substack.com/p/brute-intelligence
author: Benn Stancil
date: '2026-07-29'
description: The industrialization of trying stuff.
tags:
- tldr
---

# Brute intelligence

### The industrialization of trying stuff.

Jul 24, 2026
104
22
15
Share
He’ll get it eventually.

Terence Tao is a mathematician. He was 20 years old when he earned his Ph.D. from Princeton University; he was 24 years old when he became a full professor at UCLA; he was 31 when hewon the Fields Medal, which is widely considered to be the Nobel Prize for mathematics. “Today, many regard Tao as the finest mathematician of his generation,”saidaNew York Times Magazineprofile of Tao.

Over the weekend,Levent Alpöge, a mathematician who works as a researcher at Anthropic, used Fable, Anthropic’s most capable large language model,to find a counterexampleto a famous mathematical conjecture called the Jacobian conjecture. Taoreviewed the discoveryon his blog, saying that the example “appears like a massive miracle” that was “highly unlikely to be located by brute force.” He then attempted to generalize the proposal a bit; he used ChatGPT1to “discuss various aspects of this problem and to confirm several of the calculations.”

Dmitry Rybinis a mathematician and startup founder. He’s done very well in a handful of mathematical competitions, and, by all appearances, is a quite capable mathematician—though not, probably, the finest of his generation. Two days ago,he used ChatGPTto disprove another mathematical conjecture.

TaoandRybinboth posted their conversations with ChatGPT, and you might have a few reactions to reading the two of them:

1. What?2
2. Ok, this is fun, sure, but is it that surprising? AI is a powerful tool; give it to capable operators, and of course they can use it to nudge the frontiers of their fields forward.
3. But that’s not quite what happened? Though Tao’s conversation with ChatGPT is long andnauseatinglydense,3Rybin’s is…not. It starts with an instruction—“You should do a breakthrough”—and contains exactly three more messages. In their totality:please continue research and find a complete unconditional counterexampleContinue the search. Have a clear strategy obtained from deeper understanding of the problem structure.it’s enough of partial results. let’s finish with a complete unconditional counterexampleLike, sure, it takes an amateur mathematician to be aware of the original conjecture, and it takes a highly-trained mathematician to evaluate ChatGPT’s efforts to disprove it. But the rest of Rybin’s conversation could be had by a five-year old annoyingly asking “why?” ChatGPT didn’t need to be coached; it didn’t need to be nudged; it didn’t need a Fields medalist giving it suggestions. It didn’t need to be operated at all. It just needed to be told tomake it better.

So—maybe this is how some stuff works now? Math, software development,drug development, probably a few areas in finance—maybe domains that work around problems with verifiable answers become susceptible to this sort of “loop.” Give a long-running AI agent a puzzle; it dreams up dozens or hundreds of educated hypotheses; tests them; learns; adjusts; and “continues the search.” It’s a new form of brute force: Not bruteforce, in which you give a million monkeys a million typewriters and tell them to typeevery possible combination of characters in the world, but brute intelligence, akin to having a million scientists working in a million labs,all taking swings at the same thing:

“This did not cause me to update my priors about what AI can and can’t do,” professor andmathematician Andrew Blumbergtold Mashable. “This is exactly the kind of thing I would expect AI to be able to do. If there was a counterexample that was concise and easy to state that people haven’t found because it’s a pain to search through all this stuff, AI will find it.”

Right, a computer can solve4a thirty-year old math problem in a weekend because it’s a math problem: It can churn through thirty years of conjectures, test them, and keep going. It’s not necessarily smarter than today’s mathematicians, but it’s faster—and if it’s fastenough, what’s the difference between that and smarter?

But also, if a computer can solve a thirty-year old math problem in a weekend because it’s a math problem, should we…make more problems math problems?

We’ve talked about this idea a lot. Rather than trying to get LLMs to work with data the way people do, should werestructure datato be more suitable for an LLM? Should we change how wewrite codeso that it’s optimized for a machine? Should companies reorient themselves around thisnew form of industrialized intelligence? “Our current LLMs are decent cars, but we have very few roads that are designed for them to drive on,”I said on here once; “the eventual development of AI agents will depend on our ability to build those roads.” Leverage comes from where you put fulcrum as much as it comes from the weight that you use.Change the problem to make it easy for AI to solve.

And this, it seems, is what the problem needs to be changed into: A math problem, or anything that can be reasoned through, calculated, tested, and reasoned through again. In other words, there are now two ways to do something: By doing it, or by turning it into something that’s shaped like math, and having a computer do the rest.

Lots of discoveries require people to be out in the world, poking at some metal or staring into outer space. Lots ofdecisionsrequire talking to people and contemplating the meaning life and how much you love the game.5Lots of work requires subjectivity and tAsTe. But whatever doesn’t—whatever can modeled into something that can answered by thinking, working, and testing everything in a closed box—seems like it’ll soon be handed off to this sort of brute intelligence, and solved in the background of someone’s computer.

1

Alpöge used Fable for his work; did Tao use GPT 5.6 Sol, OpenAI’s most capable large language model, for his? He doesn’t say, but halfway through the conversation, he apparently hit some paywalls and “activated pro.” So I guess he’s usually just out there solving math with free accounts and primitive toolslike some caveman?

2

E.g., from Tao:

The homogeneity in x is an intertwining between a dilation (x,r,u) to (lambda x, r,u) and a dilation (P,Q,R) to (lambda^-2 P, lambda^-1 Q, lambda R) which seems to collapse the 3d jacobian to a sort of twisted 2d jacobian. Is there a general theory of such twisted jacobians and do you have any sense why those particular dilation weights were used?

3

E.g., again:

I can see why the five-dimensional Jacobian has a nice monomial form in rho. Why does this make the three-dimensional Jacobian after restricting to c_2 = rho = 1 and eliminating the delta, eps variables also a monomial (now in x)? Is there some block-diagonal structure or something in the 5D Hessian that allows for a nice reduction? I would have expected some sort of Schur’s complement type operation to appear.

Right, I know, I would’ve expected that too.

4

I get that it didn’t “solve” the conjecture; it instead found a counterexample to it. On one hand, that’s something that youcoulddo with raw brute force; on the other hand, Tao said that the counterexample wasn’t one that could’ve been discovered that way. (Moreover, counterexamples are exactly the kind of thing you could find with brute intelligence: Theorize, test, theorize, test, over and over.) But either way, both Alpöge and Rybin found something that hadn’t been found before, and, given people’s reactions to it, something that people care about having been found.

5

Or, like, adinner with the Clintons.

104
22
15
Share
Previous