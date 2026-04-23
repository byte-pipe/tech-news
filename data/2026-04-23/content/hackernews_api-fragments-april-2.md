---
title: 'Fragments: April 2'
url: https://martinfowler.com/fragments/2026-04-02.html
site_name: hackernews_api
content_file: hackernews_api-fragments-april-2
fetched_at: '2026-04-23T11:59:20.747936'
original_url: https://martinfowler.com/fragments/2026-04-02.html
author: theorchid
date: '2026-04-22'
description: Technical, cognitive, and intent debt
tags:
- hackernews
- trending
---

# Fragments: April 2

Martin Fowler: 02 Apr 2026

As we see LLMs churn out scads of code, folks have increasingly turned to Cognitive Debt as a metaphor for capturing how a team can lose understanding of what a system does. Margaret-Anne Storey thinks a good way of thinking about these problems is to considerthree layers of system health:

* Technical debt lives in code. It accumulates when implementation decisions compromise future changeability. It limits how systems can change.
* Cognitive debt lives in people. It accumulates when shared understanding of the system erodes faster than it is replenished. It limits how teams can reason about change.
* Intent debt lives in artifacts. It accumulates when the goals and constraints that should guide the system are poorly captured or maintained. It limits whether the system continues to reflect what we meant to build and it limits how humans and AI agents can continue to evolve the system effectively.

While I’m getting a bit bemused by debt metaphor proliferation, this way of thinking does make a fair bit of sense. The article includes useful sections to diagnose and mitigate each kind of debt. The three interact with each other, and the article outlines some general activities teams should do to keep it all under control

❄                ❄

In the article she references a recent paper by Shaw and Nave at the Wharton School thatadds LLMs to Kahneman’s two-system model of thinking.

Kahneman’s book, “Thinking Fast and Slow”, is one of my favorite books. Its central idea is that humans have two systems of cognition. System 1 (intuition) makes rapid decisions, often barely-consciously. System 2 (deliberation) is when we apply deliberate thinking to a problem. He observed that to save energy we default to intuition, and that sometimes gets us into trouble when we overlook things that we would have spotted had we applied deliberation to the problem.

Shaw and Nave consider AI as System 3

A consequence of System 3 is the introduction of cognitive surrender, characterized by uncritical reliance on externally generated artificial reasoning, bypassing System 2. Crucially, we distinguish cognitive surrender, marked by passive trust and uncritical evaluation of external information, from cognitive offloading, which involves strategic delegation of cognition during deliberation.

It’s a long paper, that goes into detail on this “Tri-System theory of cognition” and reports on several experiments they’ve done to test how well this theory can predict behavior (at least within a lab).

❄                ❄                ❄                ❄                ❄

I’ve seen a few illustrations recently that use the symbols “< >” as part of an icon to illustrate code. That strikes me as rather odd, I can’t think of any programming language that uses “< >” to surround program elements. Why that and not, say, “{ }”?

Obviously the reason is that they are thinking of HTML (or maybe XML), which is even more obvious when they use “</>” in their icons. But programmers don’tprogramin HTML.

❄                ❄                ❄                ❄                ❄

Ajey Gore thinks aboutif coding agents make coding free, what becomes the expensive thing? His answer is verification.

What does “correct” mean for an ETA algorithm in Jakarta traffic versus Ho Chi Minh City? What does a “successful” driver allocation look like when you’re balancing earnings fairness, customer wait time, and fleet utilisation simultaneously? When hundreds of engineers are shipping into ~900 microservices around the clock, “correct” isn’t one definition — it’s thousands of definitions, all shifting, all context-dependent. These aren’t edge cases. They’re the entire job.

And they’re precisely the kind of judgment that agents cannot perform for you.

Increasingly I’m seeing a view that agents do really well when they have good, preferably automated, verification for their work. This encourages such things asTest Driven Development. That’s still a lot of verification to do, which suggests we should see more effort to find ways to make it easier for humans to comprehend larger ranges of tests.

While I agree with most of what Ajey writes here, I do have a quibble with his view of legacy migration. He thinks it’s a delusion that “agentic coding will finally crack legacy modernisation”. I agree with him that agenticcodingis overrated in a legacy context, but I have seen compelling evidence that LLMs help a great deal inunderstanding what legacy code is doing.

The big consequence of Ajey’s assessment is that we’ll need to reorganize around verification rather than writing code:

If agents handle execution, the human job becomes designing verification systems, defining quality, and handling the ambiguous cases agents can’t resolve. Your org chart should reflect this. Practically, this means your Monday morning standup changes. Instead of “what did we ship?” the question becomes “what did we validate?” Instead of tracking output, you’re tracking whether the output was right. The team that used to have ten engineers building features now has three engineers and seven people defining acceptance criteria, designing test harnesses, and monitoring outcomes. That’s the reorganisation. It’s uncomfortable because it demotes the act of building and promotes the act of judging. Most engineering cultures resist this. The ones that don’t will win.

❄                ❄                ❄                ❄                ❄

One the questions comes up when we think of LLMs-as-programmers is whether there is a future for source code. David Cassel on The New Stack has an article summarizingseveral views of the future of code. Some folks are experimenting with entirely new languages built with the LLM in mind, others think that existing languages, especially strictly typed languages like TypeScript and Rust will be the best fit for LLMs. It’s an overview article, one that has lots of quotations, but not much analysis in itself - but it’s worth a read as a good overview of the discussion.

I’m interested to see how all this will play out. I do think there’s still a role for humans to work with LLMs to build useful abstractions in which to talk about what the code does - essentially the DDD notion ofUbiquitous Language. Last year Unmesh and I talked aboutgrowing a languagewith LLMs. As Unmesh put it

Programming isn’t just typing coding syntax that computers can understand and execute; it’s shaping a solution. We slice the problem into focused pieces, bind related data and behaviour together, and—crucially—choose names that expose intent. Good names cut through complexity and turn code into a schematic everyone can follow. The most creative act is this continual weaving of names that reveal the structure of the solution that maps clearly to the problem we are trying to solve.