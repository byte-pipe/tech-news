---
title: AI is doing something weird to Science
url: https://blog.apiad.net/p/ai-is-doing-something-weird-to-science
site_name: tldr
content_file: tldr-ai-is-doing-something-weird-to-science
fetched_at: '2026-05-26T19:41:37.962548'
original_url: https://blog.apiad.net/p/ai-is-doing-something-weird-to-science
author: Alejandro Piad Morffis
date: '2026-05-26'
description: In both good and bad ways, and it won't go away.
tags:
- tldr
---

🤖 Mostly Harmless AI

# AI is doing something weird to Science

### In both good and bad ways, and it won't go away.

Alejandro Piad Morffis
May 25, 2026
23
4
2
Share
Photo by 
Artturi Jalli
 on 
Unsplash

Picture Donald Knuth. Eighty-eight years old, the man who wroteThe Art of Computer Programmingby hand in TeX, which he invented himself to be able to write his own books. The father of algorithmic analysis. The most laudeated living computer scientist. A legend, and a well-known AI skeptic.

Now picture him reading a printed chat log between a fellow colleague andClaude Code. Not skimming. Reading it in detail, because there is something genuinely baffling about it.

The log belongs to Filip Stappers, a mathematician who ran thirty-one coding explorations with Claude Opus 4.6, systematically probing a class of combinatorial objects Knuth had spentdecadesthinking about. Exploration 15 surfaced something unexpected: a structural pattern nobody had written down.

Knuth read it, judged it valid, proved it correct by hand, and wrote a paper about it. He called it “Claude’s Cycles.” Knuth noted, with his characteristic precision, that he’ll “have to revise his opinions about generative AI” one of these days.

Most accounts that open with this scene take one of two off-ramps.

The first off-ramp is thereplacement narrative. AI is now the scientist. The model had the insight; Stappers just ran the prompts; Knuth read the output and judged it true.Discovery has been automated. We are, depending on your temperature, either liberated or obsolete.

The second off-ramp is thestochastic-parrot dismissal. It’s just a language model predicting tokens. It doesn’t understand combinatorics; it doesn’t understand anything. Stappers did the science; Claude shuffled plausible-sounding symbols. Attribute the discovery to the researcher, not the autocomplete.

Both off-ramps feel satisfying. Both are wrong. And they’re wrong in the same way: they’re answering the question “did AI do the science?” That’s the wrong question. The interesting object is not the agent.It’s the loop.

The loop looks like this: a human poses a question; a model proposes candidates; a verifier filters the candidates; a human curates what survives. Round and round. What Stappers and Claude did is not fundamentally different in shape from what Tao and Lean are doing, or what the GNoME pipeline does in materials science, or what AlphaFold did for protein structure. The shape is the same.The loop does the discovery.

I want to be clear about what that means, because it’s easy to hear it as either a compliment to AI or a dismissal. It is neither. It’s an empirical claim about where the causal action lives. Not in the model, not in the human, but in theinteraction structurebetween them. Get that structure right and you get science. Get it wrong and you get confident nonsense at scale. The details of what ‘wrong’ looks like are worth walking through carefully, and we’ll do that a couple of sections down.

But before we can dismiss either off-ramp, we need to walk four recent cases. Because in every one of them — Claude’s Cycles, Tao and Lean, AlphaFold, GNoME — the replacement narrative is not just philosophically confused. It is empirically wrong. The loop does the discovery.

Thanks for reading The Computist Journal! Subscribe for free to receive new posts and support my work.

Subscribe

## Four Cases, One Shape

In each of the following cases, the loop does the discovery. I’m going to give you four of them across four domains, because I think the pattern only becomes undeniable when you see it that many times. Same shape, different materials.

### Claude’s Cycles

You already have the scene. Stappers runs thirty-one explorations. Not one inspired conversation, thirty-one numbered, documented, methodical probes. Claude proposes. Stappers evaluates. Knuth reads the surviving logs, verifies the mathematical claims by hand, and writes. One human author. One credited co-explorer. The question was Stappers’; the verification was Knuth’s; the curation of which thirty-one explorations were worth pursuing was human throughout. The model was the proposer.

That word matters, and I want to be precise about it.Proposer.Not discoverer, not author, not scientist. The one that generates candidates fast enough that the verifier can find something in the haystack.

### Tao and Lean

Terence Tao, Fields Medal, the current standard of living mathematical genius, has been publicly working through what it looks like to use LLMs for mathematical research. His account in theNotices of the American Mathematical Societyin 2025 is careful and specific, and I appreciate the care because it’s easy to overread these things in both directions.

Here’s what you’re actually looking at: an LLM proposes proof steps, intermediate claims, candidate lemmas, reformulations of the problem. Lean’s type-checker is the verifier. And Lean’s type-checker cannot be fooled. It either accepts a proof term or it doesn’t. There’s no “plausible-sounding but wrong” in Lean. The system rejects garbage instantly and silently. What the human does — Tao, or anyone in his lab — is curate: which of the surviving proof steps are worth following, which directions are worth pursuing. The loop is tight. The proposer is creative and unreliable; the verifier is reliable and uncreative; the human operates between them.

I’d reframe that: the breakthrough isn’t that LLMs can now do mathematics. It’s that the loop can now run fast enough and cheaply enough to be useful.

### AlphaFold

I want to include this one even though it’s older and better-known, because it’s the case where people most confidently say “AI solved the problem.” And that confidence is telling.

The problem was fifty years old. How does a protein fold? You have the amino acid sequence; you want the three-dimensional structure; that structure determines function; that function determines everything downstream in biology and drug design. AlphaFold 2 proposes structures. Experimental crystallography verifies them: X-ray diffraction, cryo-electron microscopy, techniques that require real equipment, real samples, real physics. You cannot hallucinate a crystal structure into being; the protein either folds the way the model says or it doesn’t, and the experimental method tells you which. AlphaFold 3 extended this to molecular complexes: DNA, RNA, small-molecule ligands binding to proteins.

I think this is worth sitting with: human researchers curated which structures were worth solving, which proteins mattered, which findings were publishable. AlphaFold proposed. Nature verified. Humans curated.

### GNoME and A-Lab

This is the one I find most clarifying, because the verifier here is the most brutally physical. You can’t argue with a crystal.

GNoME — Google DeepMind’s Graph Networks for Materials Exploration, if you want the full name — generated 380,000 candidate stable crystal structures. That’s the proposal stage. Then A-Lab, UC Berkeley’s autonomous laboratory, took 58 of those candidates and actually tried to synthesize them. Robotically. With real chemicals, real furnaces, real diffraction equipment to check what came out. Forty-one novel materials were successfully synthesized in 17 days.

Think about the verifier in that loop. Not a type-checker, not a scoring function. A physical robot in a real lab mixing real compounds at real temperatures and asking whether the crystal forms. You cannot fake a crystal. If A-Lab says it synthesized a novel stable material, it synthesized a novel stable material. The model proposed; the physical world verified; human researchers curated which structures were interesting enough to attempt.

I want to be blunt here: the pattern is not subtle. In every case: model proposes, independent verifier filters, human curates. The model is never the verifier. The model is never the question-poser. The model occupies exactly one slot in the loop, and it’s the slot that benefits most from creativity, speed, and a high tolerance for being wrong.

The replacement narrative requires you to believe the model is doing all three jobs. It isn’t. Empirically, demonstrably, across four domains, it isn’t.

Before we anatomize what changed inside the loop, it is worth noting that this shape is fifty years old. Because that changes what we should find surprising.

## The Loop Has Is Older Than You Think

The loop does the discovery today in the same way it did the discovery in 1976.

I want to be somewhat insistent about this, because I think the historical amnesia around computational assistance in science is part of what makes AI discourse so unmoored. This isn’t new. What’s new is narrower than you think, and understanding exactly what changed is the only way to correctly evaluate what it means.

### Appel and Haken, 1976

You probably know this one: the four-color theorem says any map can be colored with four colors such that no adjacent regions share a color. Mathematicians had been trying to prove it since 1852. In 1976, Kenneth Appel and Wolfgang Haken proved it. Using a computer. Their proof involved reducing the problem to 1,482 configurations and verifying each one computationally. No human read every step. No human could. The proof was real; the verification was mechanical.

The mathematical community was genuinely unsettled. The theorem wasn’t wrong. But the proof didn’t fit the usual epistemological frame. You couldn’t follow it the way you follow a conventional proof. You had to trust the computer. That discomfort was the first serious confrontation with what I’m calling the loop: humans posed the problem, humans designed the reduction, a computer verified the 1,482 cases, humans accepted the surviving result.

Same shape. Fifty years earlier.

### Hales and Flyspeck, 1998–2014

Thomas Hales proved Kepler’s sphere-packing conjecture in 1998. The conjecture: the way you’d intuitively stack cannonballs, face-centered cubic packing, is in fact the densest possible arrangement. The proof relied on computer enumeration so extensive that the referees couldn’t verify it. They were “99% confident” and said so, which is an unusual thing for mathematical referees to say.

Sixteen years later —sixteen years— the Flyspeck project completed a formal verification of the proof in HOL Light, a proof assistant. I want to dwell on that: sixteen years. The loop had a very slow verifier in the middle. It still worked. The result was real.

Sixteen years from claim to verified closure. I find that humbling. We talk about AI accelerating science as though “fast” is a new property of loops. The loop has always done the discovery. Sometimes slowly.

### AI Feynman, 2020

You won’t usually see this one in the AI-in-science timelines, but it belongs here. Silviu-Marian Udrescu and Max Tegmark built a system called AI Feynman that uses symbolic regression (searching the space of mathematical expressions) to recover physics equations from data. Feed it measured relationships between physical quantities; it proposes the equation. Tested on 100 equations from the Feynman Lectures on Physics. Human scientists posed the problems; the system proposed expressions; formal mathematical checks filtered them.

This is 2020, two years before the moment people usually date as the AI-in-science inflection. I find it clarifying: the loop is the same.

### What 2022 Actually Changed

Here’s what changed. One thing in the loop changed, and it’s the proposer slot.

Before roughly 2022, the proposer in loops like these was domain-specific, narrow, and hand-engineered. AlphaFold’s architecture was designed from the ground up for protein structure prediction. The Flyspeck enumeration was written for Kepler’s problem. AI Feynman’s symbolic regression engine was built for recovering physics equations. The verifiers were already strong: formal proof checkers, physical experiments, crystallography. The curators were already human. But building a proposer required significant domain-specific engineering effort for each new application.

What changed, and I think this is the key move, is thatthe proposer slot is now increasingly occupiable by general-purpose large language models that can be directed with natural-language specifications.

The same model that helps Stappers explore combinatorial objects can, with different prompts, propose protein structures, generate proof steps, suggest material candidates. It’s not that the model does these things well in some absolute sense. It does them well enough that a strong verifier can find the real results in the output. And FunSearch, DeepMind’s system for mathematical discovery, goes a step further: it uses LLMs to generate the search strategy itself. AlphaEvolve extends this to evolving the algorithms. The proposer writes the proposer.

I want to flag what didn’t change: verifier reliability, human curation, question-posing. Knuth still read the logs. Tao still decides which lemmas are worth pursuing. The IMO committee still wrote the problems. The physical world still decides whether a crystal forms.

So: what exactly is the loop, and what changed inside it? The proposer and verifier are different jobs — you can confuse them, and that confusion is the mistake that both off-ramps make.

## Anatomy of the Loop

The loop does the discovery. But what is the loop, exactly? It has four roles:poser,proposer,verifier,curator. They are not interchangeable.

I want to be specific about each, because vagueness here is where confused takes come from. When someone says “AI did the science,” they’re usually collapsing all four roles into one and attributing them to the model. When someone says “it’s just a tool,” they’re usually denying that the proposer role is meaningfully distinct from, say, a search engine. Both collapses are wrong.

### The Proposer Role

I want to define this carefully, because the proposer role is where most confusion lives. The proposer generates candidates. That’s it. It doesn’t need to know which candidates are correct; it doesn’t need to understand the domain at the level required to verify; it doesn’t need to bear accountability for wrong answers. It just needs to produce output that the verifier can evaluate. Fast. In large quantities. With enough breadth that interesting things appear in the distribution.

This is a real and important job. Generating candidates well, in a domain, at the right level of specificity, with the kind of variety that makes the verifier’s job tractable, is genuinely hard. What LLMs are good at is producing plausible candidates in natural-language-specified domains. That’s useful precisely because “plausible” is a different bar from “correct.” The proposer buys lottery tickets; the verifier checks which ones won.

### Galactica, or: What Happens Without a Verifier

In November 2022, Meta released Galactica, a large language model trained on scientific literature. I remember when this dropped: the pitch was that it could reason about science, write papers, explain concepts, generate hypotheses. It was fluent. Confident. It had read more papers than any human alive.

It was retracted in three days.

Galactica produced plausible-sounding but fabricated citations. It generated chemistry that was wrong. It stated incorrect facts with the same calm certainty it used for correct ones. The model had no verifier. It had no external check against which its proposals were filtered. It was a proposer talking directly to readers who were treating it as a verifier.

That’s the failure mode. “LLMs are bad at science” is the wrong lesson. Galactica was a capable proposer deployed without a loop. Dump the proposer’s output directly into the world, skip the verifier, and you get confident nonsense. The problem wasn’t the model. The problem was the missing loop.

### The Verifier Role

I want to be careful here, because this is where the asymmetry lives. The verifier is not creative. The verifier must beright. These are the two properties that matter.

Lean’s type-checker does not hallucinate. It processes a proof term and either accepts it or rejects it, and its answer is correct by construction: it’s checking against the formal rules of type theory, and it doesn’t have opinions or moods or bad days. A crystal either forms or it doesn’t. X-ray diffraction either confirms the predicted structure or it doesn’t. These verifiers are not AI systems. They’re physics, or mathematics, or formal logic.

Here’s a slogan worth keeping:the verifier is the one that matters.A loop with a weak proposer and a strong verifier still produces valid science — it’s just slow, because it needs more proposals before one survives — this is just what “normal science has been so far”, slow proposer, strong verifier.

A loop with a strong proposer and a weak verifier produces Galactica. The asymmetry is important. You can have crap proposals and still win, as long as the verifier is robust. You cannot have a weak verifier and still win, no matter how impressive the proposer.

### Tao’s Insight on Composability

Tao articulated this in his 2025Noticespiece, and I think it’s genuinely the right way to think about it: the value of the LLM-plus-formal-verifier combination comes from combining complementary weaknesses. LLMs are creative but unreliable. Lean is reliable but cannot be creative; it needs to be told what to check. Individually, each is limited. Together, the loop covers both limitations: the LLM proposes, Lean certifies, and you get results that are both novel and guaranteed correct.

This is not a new insight in the philosophy of science or even in computational science. It’s the same structure as Appel-Haken: creative human mathematicians posed and structured the problem, mechanical verification checked the cases. What’s new is that the LLM makes the creative-but-unreliable proposer slot much cheaper and more general to fill. You don’t need a domain expert to hand-engineer each proposer; you need a prompt and a general-purpose model.

### What’s Genuinely New Since 2022

Let me be specific, because this matters for evaluating claims. Three things changed:

First,open-ended program synthesis. The proposer can now write code, not just fill templates. FunSearch and AlphaEvolve don’t just suggest candidate solutions; they generate the search strategy itself, which then searches for solutions. The proposer proposes how to propose. That’s a qualitative shift.

Second,cross-domain transfer at useful fidelity. The same general-purpose model can propose protein structure candidates, proof steps, crystal candidates, combinatorial patterns, all with natural-language specification. You don’t need to rebuild the proposer for each domain. The moat that used to come from hand-engineering a domain-specific proposer is largely gone.

Third,tight LLM-to-formal-verifier loop latency. The Flyspeck project took sixteen years. The Lean loop that Tao describes closes in seconds. When the loop runs fast, you can iterate fast, which means you can attempt more ambitious problems and accumulate signal faster about which directions are productive.

What hasn’t changed: humans pose the problems; the verifier is still not an LLM; which questions are worth asking remains entirely human. Knuth read the logs. Tao decides which lemma is promising. The IMO committee wrote the problems. The GNoME team decided that stable crystal structures were the target. The question ofwhat to look forhas not been automated.

With the anatomy clear, we can finally steelman both off-ramps seriously. And explain precisely why they are both wrong.

## Why Both Extremes Are Wrong

The loop does the discovery, but what does that mean for who gets the credit?

I want to take both positions seriously, because I think each is tracking something real. Dismissing either one without engagement is how you end up with a position that sounds crisp but falls apart in the edge cases.

### The Maximalist Steelman

Knuth is eighty-eight years old. He has spent decades thinking about the class of combinatorial objects Stappers was exploring. He hadn’t found the pattern that surfaced at exploration 15. Stappers, presumably, hadn’t either, or there wouldn’t have been thirty-one explorations looking for it.

Here’s the maximalist claim: ifsurpriseis constitutive of discovery, if discovery is the moment something genuinely unexpected becomes known, then the model contributed something essential. It’s not that the model was incidentally involved in a process humans could have completed. It’s that the specific result didn’t exist in any human mind before the model generated it. A system that reliably surfaces what experts miss is doing something scientists do. The fact that the model can’t feel pride or bear responsibility doesn’t settle whether it participated in discovery.

The maximalist is pointing at something real. The model wasn’t executing a search strategy that a human had pre-specified. It was navigating a space in ways that produced genuinely unexpected output. That matters.

### The Dismissive Steelman

A hammer drives nails. We don’t say the hammer built the house. Excel executes arithmetic the analyst specified; we don’t credit Excel with the financial model. AlphaFold was trained on structural biology data that human researchers collected over decades; the training objective was designed by human engineers; the evaluation criteria were set by human scientists. The model is a sophisticated tool. Sophisticated tools don’t discover; they execute.

The dismissive case is not purely rhetorical. There’s a serious accountability point underneath it: when a model-generated finding turns out to be wrong (and some will), who is responsible? If you’ve attributed agency to the model, you’ve obscured the accountability chain. The human who deployed the loop without a strong verifier, who curated poorly, who published without checking: that human is responsible. Diffusing credit into the model diffuses accountability too, and that’s a practical problem, not just a philosophical one.

The dismissive steelman is also tracking something real. The model didn’t choose the question. It didn’t decide the result mattered. It didn’t design the verifier. It didn’t stake its reputation on the finding.

### The Verdict

Both steelmans are right about something; both are wrong about the structure.

The maximalist is right that the model contributes something essential, something that wouldn’t have been there without it. Wrong that this constitutes independent discovery: you cannot have independent discovery without the ability to pose a question, which requires caring about the answer, which requires the kind of intentionality the model doesn’t have.

The dismissive is right that the model doesn’t choose questions, doesn’t bear accountability, and shouldn’t be treated as an author in the full sense. Wrong that this makes it a mere tool in the hammer-and-nail sense. AlphaTensor, DeepMind’s system that found faster matrix multiplication algorithms, didn’t just execute a search the engineers specified. It found an algorithm that reconfigured what experts believed was achievable. That’s not executing; it’s navigating a combinatorial space in a way that produces genuine surprise. The hammer never surprises you — except when you’re not looking and it hits your finger, which by the way, AI can also do, and with a louder bang.

The right frame is, I think, theAI lab member. Indispensable, capable, sometimes surprising. Not a hammer; not a principal investigator, not a replacement for another human. Just a genuinely, qualitatively new kind of entity. An entity that occupies the proposer slot in the loop and does it better than anything that occupied that slot before, but doesn’t touch the verifier, doesn’t pose the questions, and doesn’t bear the accountability that comes with authorship.

If AI is a lab member and not a scientist, what does that do to the publishable paper, and to the metrics we use to measure science?

## But What Happens to the Paper

The loop does the discovery. But the paper still needs to be written, and the paper is what the institution counts.

This is where I get more pessimistic, or at least more cautious. The loop is good news for science-the-activity. It’s more complicated news for science-the-institution.

### Discovery and Paper Count Were Already Decoupled

Park, Leahey, and Funk published inNaturein 2023 a careful empirical study of scientific disruption, measuring across decades of papers and patents how often new workdisplacesthe prior literature versusconsolidatesit. Their finding: disruption has been declining since 1945. Not linearly, not dramatically, but consistently. Meanwhile, paper count has been exploding.

The interpretation I find most compelling: the processes that generate papers and the processes that generate genuine advances were already decoupled before AI. A lot of papers are small increments, confirmations, replications, applications of known methods to new datasets. That’s not waste; science needs that infrastructure. But it means paper count was already a noisy proxy for discovery rate.

What an AI proposer does to this: it makes generating candidate findings cheaper. Cheaper to generate means more candidates, means more papers. Discovery and paper count decouple further.

### Goodhart as Accelerant

Goodhart’s Law: when a measure becomes a target, it ceases to be a good measure. Academic institutions have been targeting paper count, citation count, journal impact for decades. Paper mills, factories producing fake or low-quality research for pay-to-publish journals, were already a pre-AI problem. Ioannidis documented the replication crisis in 2005 and again in 2018; most published findings in some fields don’t replicate, and that was before AI made generating plausible-sounding results cheaper.

The AI proposer is an accelerant deployed into a system already optimizing for the wrong thing. It makes the Goodhart problem worse. A lot worse. If you can generate a thousand candidate papers in the time it used to take to generate ten, and the verifier in your loop is peer review (slow, inconsistent, and famously gameable), then you have a problem that is structurally different from the pre-AI problem in scale.

I want to be clear: this is not an argument against AI-in-science. It’s an argument that the institution of science has a verifier problem, and AI proposers make that verifier problem more urgent. The fix is not to slow the proposer. The fix is to build better verifiers.

### The Optimistic Edge

Here’s where I land, and I’m genuinely somewhat optimistic about this: if generating candidates is cheap, the scarce skill shifts upstream.

The researchers who will matter most in this environment are not the ones who can generate the most proposals. They’re the ones who can pose the right questions, who can identify which problems are worth solving before they know the answer, and the ones who can build strong verifiers. Question-selection and verifier-design become the competitive moat. That’s a real and important skill. It’s harder to fake than generating a paper. And it’s the skill that the loop most depends on.

If I’m hiring for a lab in 2026, I’m not looking for “AI scientist” as a job description. I’m looking for people who can look at a domain and say:here is what a correct answer would have to look like, and here is how I would know if I found it.That’s what the verifier is. Building it is hard. It requires deep domain knowledge, epistemological clarity, and the kind of judgment that comes from years of thinking carefully about what you’re actually trying to know.

### A Diagnostic Heuristic

Let me give you something practical. When you read an AI-in-science result, a press release, a paper, a breathless tweet thread, ask this:what was the verifier, and who built it?

If the verifier is Lean, or a crystal, or experimental replication with pre-registered protocols, or a physical measurement with known error bars: trust the result. The proposer’s reliability doesn’t matter much; the verifier caught the garbage. The finding is real regardless of how the candidates were generated.

If the verifier is not named, if the paper says “we used GPT-4 to generate hypotheses and evaluated them with GPT-4 to assess plausibility,” you’re looking at Galactica with extra steps. The proposer and the verifier are the same system. The loop is not closed. Be skeptical.

That diagnostic question is the institutional choice this moment is forcing. What was the verifier, and who built it? Let’s land it.

## The Verifier Is the One That Matters

“I’ll have to revise my opinions about generative AI one of these days.”

Knuth said that. Not “AI did the science,” not “it’s just autocomplete.” Something more specific:I may have underestimated what this thing can do in the right loop.The loop did the discovery. The human owned the question and the verifier. The model was the proposer. And the result was real.

### The Investment Gap

Here’s the uncomfortable institutional reality: almost all current investment is in the proposer. Larger models, more parameters, cheaper inference, better fine-tuning, faster generation. The race to make the proposer better is well-funded, well-publicized, and moving fast.

The verifier is comparatively neglected.

Formal verification tools like Lean exist, but they’re hard to use, require significant expertise, and don’t cover most scientific domains. Physical verification (A-Lab-style robotic synthesis) is expensive and slow relative to the speed at which the proposer can generate candidates. Experimental replication is underfunded as a scientific activity; it’s less prestigious than novel claims. The referee system in academic publishing was designed for a world wheregeneratingcandidates was the hard part. It was not designed for a world where a model can generate ten thousand plausible candidates in an afternoon.

Hiring “AI scientists” misframes the institutional need. The need is for researchers who can pose hard questions and build reliable verifiers. The “AI lab member” frame points to what needs managing: not the model, but the loop. And the loop’s bottleneck right now is the verifier.

I should mention that this piece is drawn from the science chapter ofMostly Harmless AI, a book I’m writing about what AI actually does versus what the headlines claim. If you’re finding this useful, the book is where the longer argument lives.

### What Comes Next

Next week: AI in creative output. Art, literature, music. Where the verifier question changes shape entirely. Because in mathematics and materials science, you can at least define what “correct” means. In creative domains, the verifier problem is not just harder. It’s constitutively different. What does it even mean for a creative proposal to becorrect? I have some thoughts, and I think they’re going to make the science case look straightforward by comparison.

Stay curious.

P.S. There’s a Subscribe button somewhere below this. I’m told it does something useful. My understanding of subscription mechanics is below the level of a confident stochastic parrot. I believe it works, but I haven’t checked every step. Click it anyway. The verifier here is whether you keep showing up next Monday.

Subscribe
23
4
2
Share