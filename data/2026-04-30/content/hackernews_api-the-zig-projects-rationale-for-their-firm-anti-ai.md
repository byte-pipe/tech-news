---
title: The Zig project's rationale for their firm anti-AI contribution policy
url: https://simonwillison.net/2026/Apr/30/zig-anti-ai/
site_name: hackernews_api
content_file: hackernews_api-the-zig-projects-rationale-for-their-firm-anti-ai
fetched_at: '2026-04-30T12:14:33.177573'
original_url: https://simonwillison.net/2026/Apr/30/zig-anti-ai/
author: Simon Willison
date: '2026-04-30'
description: The Zig project's rationale for their anti-AI contribution policy
tags:
- hackernews
- trending
---

# Simon Willison’s Weblog

Subscribe

Sponsored by:
 Sonar — Now with SAST + SCA for secure, dependency-aware Agentic Engineering. 
SonarQube Advanced Security

30th April 2026

Zighas one of the most stringentanti-LLM policiesof any major open source project:

No LLMs for issues.

No LLMs for pull requests.

No LLMs for comments on the bug tracker, including translation. English is encouraged, but not required. You are welcome to post in your native language and rely on others to have their own translation tools of choice to interpret your words.

The most prominent project written in Zig may be theBunJavaScript runtime, which wasacquired by Anthropicin December 2025 and, unsurprisingly, makes heavy use of AI assistance.

Bun operates its own fork of Zig, and recentlyachieved a 4x performance improvementon Bun compile after adding "parallel semantic analysis and multiple codegen units to the llvm backend". Here'sthat code. But@bunjavascript says:

We do not currently plan to upstream this, as Zig has a strict ban on LLM-authored contributions.

InContributor Poker and Zig's AI Ban(via Lobste.rs) Zig Software Foundation VP of Community Loris Cro explains the rationale for this strict ban. It's the best articulation I've seen yet for a blanket ban on LLM-assisted contributions:

In successful open source projects you eventually reach a point where you start getting more PRs than what you’re capable of processing. Given what I mentioned so far, it would make sense to stop accepting imperfect PRs in order to maximize ROI from your work, but that’s not what we do in the Zig project. Instead,we try our best to help new contributors to get their work in, even if they need some help getting there. We don’t do this just because it’s the “right” thing to do, but alsobecause it’s the smart thing to do.

Zig values contributors over their contributions. Each contributor represents an investment by the Zig core team - the primary goal of reviewing and accepting PRs isn't to land new code, it's to help grow new contributors who can become trusted and prolific over time.

LLM assistance breaks that completely. It doesn't matter if the LLM helps you submit aperfectPR to Zig - the time the Zig team spends reviewing your work does nothing to help them add new, confident, trustworthy contributors to their overall project.

Loris explains the name here:

The reason I call it “contributor poker” is because, just like people say about the actual card game, “you play the person, not the cards”. In contributor poker, you bet on the contributor, not on the contents of their first PR.

This makes a lot of sense to me. It relates to an idea I've seen circulating elsewhere: if a PR was mostly written by an LLM, why should a project maintainer spend time reviewing and discussing that PR as opposed to firing up their own LLM to solve the same problem?

Posted 
30th April 2026
 at 1:24 am

## Recent articles

* LLM 0.32a0 is a major backwards-compatible refactor- 29th April 2026
* Tracking the history of the now-deceased OpenAI Microsoft AGI clause- 27th April 2026
* DeepSeek V4 - almost on the frontier, a fraction of the price- 24th April 2026

 

This is anoteby Simon Willison, posted on30th April 2026.

 javascript
 
753

 open-source
 
303

 ai
 
1991

 zig
 
9

 generative-ai
 
1765

 llms
 
1731

 ai-assisted-programming
 
378

 anthropic
 
277

 ai-ethics
 
295

 bun
 
4

### Monthly briefing

Sponsor me for$10/monthand get a curated email digest of the month's most important LLM developments.

Pay me to send you less!

 Sponsor & subscribe
 

 

 

 

* Disclosures
* Colophon
* ©
* 2002
* 2003
* 2004
* 2005
* 2006
* 2007
* 2008
* 2009
* 2010
* 2011
* 2012
* 2013
* 2014
* 2015
* 2016
* 2017
* 2018
* 2019
* 2020
* 2021
* 2022
* 2023
* 2024
* 2025
* 2026