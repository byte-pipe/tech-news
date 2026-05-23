---
title: Coding agents are giving everyone decision fatigue - Stack Overflow
url: https://stackoverflow.blog/2026/05/21/coding-agents-are-giving-everyone-decision-fatigue/
site_name: tldr
content_file: tldr-coding-agents-are-giving-everyone-decision-fatigue
fetched_at: '2026-05-23T19:30:02.125699'
original_url: https://stackoverflow.blog/2026/05/21/coding-agents-are-giving-everyone-decision-fatigue/
date: '2026-05-23'
description: Coding agents are giving everyone decision fatigue (11 minute read)
tags:
- tldr
---

There’s no doubt that coding agents have changed how software gets built. In the past three years or so, code generators have gone from fancy autocomplete to tools that can whip up a whole application while you wait. Engineers with knowledge of best practices, pitfalls, and the language of software are able to co-create code without having to futz with semicolons and unclosed brackets.

What’s in doubt is whether this change has been productive, cost efficient, or good for developers.

Easy-to-create code has put greater strain on the later parts of the software development lifecycle (SDLC): code review, DevOps/SRE, security, and infrastructure. It’s also put greater strain on the developers themselves.According to research from Smartsheet, automation intensity for their enterprise users has grown 55% year-over-year, and overall activity has increased 46%. That means the workday hasn’t grown; it’s just gotten denser with work as automations produce more without alleviating the need for humans to decide on what the definition of good is.

I spoke with Smartsheet’s CPTO, Pratima Arora, about what this intensification of work means for software engineers, why the new SDLC bottleneck is judgement, and how we can start reconfiguring how software is built to lighten the load on the people burdened with the new productivity.

## Code is cheap, code review less so

In the pre-AI era, code was expensive because engineers were expensive. They had a ton of knowledge about the languages, processes, and paradigms that produced good software. That led to somelousy measures of productivity: hours spent, lines of code written, commits per day. These were easy to measure and sure looked like a decent approximation of results. Along the way, organizations started looking at outcomes, with schemes likeDORAtrying to put numbers on those.

Those lousy metrics are returning with a vengeance,Goodhardt’s lawbe damned. Not only are agentic coders bragging about their lines of code stats, but organizations have bragged about theirpercentage of new code written by AI. Engineers might beranked by their token usage. The new tech bro vibes withtokenmaxxingand is AI-pilled.

Besides this being a wasteful measure, Arora gave an example of why it’s bad for a software org: “We had a software engineer producing 7X the code than anybody on her team. A superstar. Not only that, but also high-quality code. The check-ins and the reviews were awesome. But the other six people on the team were spending the majority of the time reviewing her code [rather] than writing the code.”

Code reviews require broad expertise in a codebase, especially if that review is to be effective and helpful.The best code reviewslook at the change in the context of the larger system, which requires holding and understanding the context of the larger system. That requirement to pass judgement on a code commit can cause a lot of stress on a reviewer. “You're essentially asked to contribute your expertise,” saidCarol Lee, PhD, now at Intuit. “So there is an element of, ‘If I mess up this review, I was the gatekeeper of this code. And if I mess it up, that might be my fault.’ So there's a lot of pressure there.”

Think about how much developers hate dealing with legacy code. I’ve speculated that one of the reasons that newer languages like Rust get more love inour annual surveyis that they show up in greenfield projects where the developer writes the code from scratch. “Whenever an engineering team takes over an old code base, they want to rewrite it before they want to fix it,” said Arora. “It's much easier to start from scratch and write it so you understand it, and much harder to look at code and make a judgment about where did the errors happen, because you didn't write the code.”

## Every builder is a decider

Smartsheet’s research found that 80% of AI-generated content is edited before it’s finalized. Those edits come from getting an understanding of the context of that code (or other content). For AI-generated code, no one wrote the original code, so the context you need to gather is greater. You can look at prompts, specs, and whatever other context your agent uses, but that’s a lot of work to produce a judgement. If we’re shifting the majority of software work from coding to making decisions, everyone is going to feel the strain ofdecision fatigue.

Before AI-enabled software engineering workflows, developers spent a significant percentage of their day (the exact figure varies wildly depending on who you asked) doing things other than writing code. Now that AI writes the code, there’s more time for the other work of an engineer. In fact, you may have seen the rise of the builder, which Arora defines as “anybody who understands a customer issue or a problem, has an idea who can prototype and build software quickly to test or ship.” The core skills of builders are understanding context and making judgement calls.

Smartsheet andothershave found that this shift doesn’t make developers’ lives easier; it makes them more intense. Multiple AI agents run in the background while the developer reviews code, attends meetings, and writes up documentation. They feel more productive, but aren’t always. “The hours haven't changed, but the density of work has, right?” said Arora. “The amount of decisions we're making in a day, how much information we are gathering and trying to make a decision out of it has changed.”

There’s a reason people who make a lot of decisions, likepresidents and CEOs, wear the same thing every day: one less decision. They build processes around gathering the information, utilizing multiple layers of experts and trust, hopefully building multiple checks and verifications before they make consequential decisions. Judgement is a skill and a process, and good decisions come from context and experience. Experience, as the joke goes, comes from bad decisions.

Senior developers are senior because they’ve got that experience, built the context about a codebase and code in general, and understand the value of a small, surgical refactor. For agentic coding, knowing what context to provide becomes much more consequential. “We see most of our senior people loading a lot more in context and then making smaller changes,” said Arora. “They end up working on the most complex piece, hence it's a lot more context for them versus the lines of code.”

While we know about the variability of agentic output, human judgement can’t serve as the be-all end-all verification gate. As work intensifies and “builders” are asked to make decisions all day, those decisions can get less reliable. One of the effects of decision fatigue is that you may end up making sloppier decisions. Arora points toan interview with Cat Wu, head of product for Claude Code and Cowork at Anthropic, where she talks about the source code leak being the result of human error. “Even with human judgment, sometimes errors can happen because we can get a little sloppy in some pockets,” said Arora.

Organizations are now looking to reconfigure the SDLC to ease the intensity of development work. Coordination between individuals and teams strains under the weight of fast code. The new focus of developer experience happens after the code is generated. “Different companies are at different maturity, and different teams are at different maturity levels,” said Arora. “We're trying to align the tooling and align the systems between the teams to make it better.”

## Judgement tests should be end-to-end, not unit

The AI models and tooling around them are getting better every day. AI is moving intocode review,code understandability, and responseevaluation, catching bugs and rewriting codeWiggamaticallywhen it finds itself in danger. Meanwhile, few organizations would consider shipping code without having humans involved in final approvals. “What we are learning every day is the systems for the workflows and the teams were set up for the old way of working where AI was not an everyday thing,” said Arora. “As we have improved individual productivity, we haven't focused on those handoffs or the coordination that happens.”

Think about what happened when the concept of development productivity shifted from lines of code and commits to change failure rate and deployment frequency. The industry went from an input metric to an output (or outcome, perhaps) metric. Those output metrics no longer just considered what individual developers did on their fancy mechanical keyboards. They had to consider the whole process—planning, writing code, CI/CD, and DevOps.

The other comparison that comes to mind is testing. Unit tests check that a feature or commit did the thing it promised. End-to-end tests validate the whole process. Judgement—specifically human judgement—could become a validation of the overall outcomes instead of just spot-checking specific features and prompts. “[Our judgement] moves to much more higher order problems as we automate some of these lower order things,” said Arora.

The big judgement gates will be at the beginning and the end of the cycle. On the one side, developers will need to define requirements, guardrails, specifications, and allowed dependencies. On the other, they need success and failure modes, security, and dependability. “Think in terms of intent, functionality, and requirements,” saidFitz Nowlan, VP of AI and Architecture at Smartbear. “Don't think necessarily in the low-level terms of API invocations or certain input or output shapes. You can certainly validate those, but as dev velocity increases 10x, QA velocity must also increase 10x, and the only way to fight fire is with fire.“

Arora has been applying the end-to-end judgement process on her team: “We're looking at the entire chain from product managers, designers, and engineers, and everybody's becoming a builder. The entire design system is integrated in both Claude and Cursor right now. The designer, who understands the customer problem, builds a prototype and front-end code, and then hands it over to an engineer to check it in.

“But my designers are not allowed to fully check in code right now. We still require engineering to review their code. In future, they should be able to check in the code, but we’re not there yet.”

## Conclusion

Easy-to-generate code has meant harder-to-review pull requests. Those PRs need lots of context and lots of judgement, and developers are having to make decisions more often. That’s intense, and it’s leading to decision fatigue and burnout.

AI problems might require AI solutions as the models, harnesses, and techniques improve. Would you trust an AI agent to build software end-to-end off of a single spec? Would you be okay giving up reviews on individual commits in exchange for a review on the final outcome? If software engineers and builders are going to work effectively in an AI-enabled world without throwing down their keyboards to become artisanal furniture builders, we may have to become comfortable with answering yes to both questions.