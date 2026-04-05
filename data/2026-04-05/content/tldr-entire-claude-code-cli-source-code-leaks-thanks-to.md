---
title: Entire Claude Code CLI source code leaks thanks to exposed map file - Ars Technica
url: https://arstechnica.com/ai/2026/03/entire-claude-code-cli-source-code-leaks-thanks-to-exposed-map-file/
site_name: tldr
content_file: tldr-entire-claude-code-cli-source-code-leaks-thanks-to
fetched_at: '2026-04-05T11:12:40.077139'
original_url: https://arstechnica.com/ai/2026/03/entire-claude-code-cli-source-code-leaks-thanks-to-exposed-map-file/
date: '2026-04-05'
published_date: '2026-03-31T19:09:33+00:00'
description: 512,000 lines of code that competitors and hobbyists will be studying for weeks.
tags:
- tldr
---

Text
 settings

The entire source code for Anthropic’s Claude Code command line interface application (not the models themselves) has been leaked and disseminated, apparently due to a serious internal error. The leak gives competitors and armchair enthusiasts a detailed blueprint for how Claude Code works—a significant setback for a company that has seen explosive user growth and industry impact over the past several months.

Early this morning, Anthropic published version 2.1.88 of Claude Code npm package—but it was quickly discovered that package included a source map file, which could be used to access the entirety of Claude Code’s source—almost 2,000 TypeScript files and more than 512,000 lines of code.

Security researcher Chaofan Shou was the first to publiclypoint it out on X, with a link to an archive containing the files. The codebase was then put in a public GitHub repository, and it has been forked tens of thousands of times.

Anthropic publicly acknowledged the mistake in a statement toVentureBeatand other outlets, which reads:

Earlier today, a Claude Code release included some internal source code. No sensitive customer data or credentials were involved or exposed. This was a release packaging issue caused by human error, not a security breach. We’re rolling out measures to prevent this from happening again.

Developers have already begun picking it apart and analyzing it. For example,@himanshustwtson X posted a detailed overview of Claude Code’s memory architecture, describing systems like background memory rewriting and various steps to verify memories’ validity before use.

And Gabriel Anhaia took a bird’s eye view,explaininghow many lines of code make up some of the components—around 40,000 for a plugin-like tool system, and 46,000 for the query system—and noting that Claude Code is “a production-grade developer experience, not just a wrapper around an API” and that its sophistication is “both inspiring and humbling.”

There had previously been extensive efforts in some developer communities to reverse-engineer Claude Code, with some success, but not with this totality.

While Anthropic’s trade secrets have some legal protection, there are architectural insights that are valuable to competitors—useful for improving their own architecture, speeding up development of competing tools, seeing what Anthropic is working on next, and identifying gaps in what Anthropic has worked out.

Further, bad actors looking for security vulnerabilities now have a map for bypassing the guardrails Anthropic has put in place. The category Claude Code occupies (and currently leads) is moving very quickly, though, and it’s hard to predict right now how much of a problem this will be a few months down the road.

 Samuel Axon
 

Senior Editor

 Samuel Axon
 

Senior Editor

 Samuel Axon is the editorial lead for tech and gaming coverage at Ars Technica. He covers AI, software development, gaming, entertainment, and mixed reality. He has been writing about gaming and technology for nearly two decades at Engadget, PC World, Mashable, Vice, Polygon, Wired, and others. He previously ran a marketing and PR agency in the gaming industry, led editorial for the TV network CBS, and worked on social media marketing strategy for Samsung Mobile at the creative agency SPCSHP. He also is an independent software and game developer for iOS, Windows, and other platforms, and he is a graduate of DePaul University, where he studied interactive media and software development.
 

1. 1."Cognitive surrender" leads AI users to abandon logical thinking, research finds
2. 2.Netflix must refund customers for years of price hikes, Italian court rules
3. 3.OpenClaw gives users yet another reason to be freaked out about security
4. 4.Artemis II is going so well that we're left to talk about frozen urine
5. 5.Elon Musk insists banks working on SpaceX IPO must buy Grok subscriptions

Customize