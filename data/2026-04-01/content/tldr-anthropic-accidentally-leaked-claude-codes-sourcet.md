---
title: Anthropic Accidentally Leaked Claude Code's Source—The Internet Is Keeping It Forever - Decrypt
url: https://decrypt.co/362917/anthropic-accidentally-leaked-claude-code-source-internet-keeping-forever
site_name: tldr
content_file: tldr-anthropic-accidentally-leaked-claude-codes-sourcet
fetched_at: '2026-04-01T19:28:11.754761'
original_url: https://decrypt.co/362917/anthropic-accidentally-leaked-claude-code-source-internet-keeping-forever
author: Decrypt / Jose Antonio Lanz
date: '2026-04-01'
published_date: '2026-03-31T18:02:56'
description: 'Claude Code exposed: Anthropic is scrambling to contain the leak, but the AI coding agent is spreading far and wide and being picked apart.'
tags:
- tldr
---

#### In brief

* Anthropic accidentally exposed 512,000 lines of Claude Code via a source map leak.
* DMCA takedowns failed as mirrors and clean-room rewrites spread instantly.
* Decentralized repos made the leak effectively permanent and uncontrollable.

Anthropic didn't mean to open-source Claude Code. But on Tuesday, the company effectively did—and not even an army of lawyers can put that toothpaste back in the tube.

It started with a single file. Claude Code version 2.1.88, pushed to the npm registry in the early hours of Tuesday morning, shipped with a 59.8MB JavaScript source map—a debug file that can reconstruct the original code from its compressed form. These files are generated automatically and are supposed to stay private. But a single line in the ignore settings let it go out with the release.

Intern and researcher Chaofan Shou, who appears to be among the first to spot the file,posted a download linkto X around 4:23 a.m. ET, and watched 16 million people descend on the thread. Anthropic yanked the npm package, but the internet had already archived 512,000 lines of code across 1,900 different files that make up a major part of the project.

Claude code source code has been leaked via a map file in their npm registry!

Code:https://t.co/jBiMoOzt8Gpic.twitter.com/rYo5hbvEj8

— Chaofan Shou (@Fried_rice)March 31, 2026

"Earlier today, a Claude Code release included some internal source code. No sensitive customer data or credentials were involved or exposed," an Anthropic spokesperson toldDecrypt. "This was a release packaging issue caused by human error, not a security breach. We're rolling out measures to prevent this from happening again."

The leak exposed the full internal architecture of what is arguably one of, if not the most sophisticated AI coding agent on the market: LLM API orchestration, multi-agent coordination, permission logic, OAuth flows, and 44 hidden feature flags covering unreleased functionality.

Among thefinds: Kairos, an always-on background daemon that stores memory logs and performs nightly "dreaming" to consolidate knowledge. And Buddy, a Tamagotchi-style AI pet with 18 species, rarity tiers, and stats including debugging, patience, chaos, and wisdom. There’s a teaser rollout for this “Buddy” apparently planned for April 1-7.

Then there's the detail that made everyone onHacker Newscackle. Per leakerKuberwastaken, buried inside the code was"Undercover Mode"—a whole subsystem designed to prevent the AI from accidentally leaking Anthropic's internal codenames and project names when contributing to open-source repositories. The system prompt injected into Claude's context literally says: "Do not blow your cover."

Apparently, Anthropic began issuing DMCA takedowns against GitHub mirrors. That's when things got interesting.

A Korean developer named Sigrid Jin—featured in theWall Street Journalearlier this month for having consumed 25 billion Claude Code tokens—woke up at 4 a.m. to the news. He sat down, ported the core architecture to Python from scratch using an AI orchestration tool calledoh-my-codex, and pushedclaw-codebefore sunrise. The repo hit 30,000 GitHub stars faster than any repository in history.

It’s basically a translation of all the code from the original language to Python, sotechnicallynot the same thing, right? We’ll leave that to lawyers and tech philosophers.

The legal logic here is sharp. Gergely Orosz, founder ofThe Pragmatic Engineernewsletter, argued in apost on X: "This is either brilliant or scary: Anthropic accidentally leaked the TS source code of Claude Code. Repos sharing the source are taken down with DMCA. BUT this repo rewrote the code using Python, and so it violates no copyright & cannot be taken down!"

It's a clean-room rewrite. A new creative work. DMCA-proof by design.

This is either brilliant or scary:

Anthropic accidentally leaked the TS source code of Claude Code (which is closed source). Repos sharing the source are taken down with DMCA.

BUT this repo rewrote the code using Python, and so it violates no copyright & cannot be taken down!pic.twitter.com/uSrCDgGCAZ

— Gergely Orosz (@GergelyOrosz)March 31, 2026

The copyright angle gets thornier when considering the legal status of AI-generated work, and howmuddythe criteria gets when lawyers have to rule whether or not it carries automatic copyright. The DC Circuitupheld that positionin March 2025, and the Supreme Court declined to hear the challenge.

If significant chunks of Claude Code were written by Claude itself—which Anthropic's own CEO has implied—then thelegal standingof any copyright claim gets murkier by the day.

Decentralization adds another layer of permanence. The account@gitlawbmirrored the original code to Gitlawb, a decentralized git platform, with a simple message: "Will never be taken down." The original remainsaccessible there. A separate repository has compiledall of Claude's internal system prompts, which is something that prompt engineers and jailbreakers will appreciate as it gives more insights into the way Anthropic conditions its models.

https://t.co/yCSEKer2tn

— GitLawb (@gitlawb)March 31, 2026

This matters beyond the drama. DMCA takedowns work against centralized platforms. GitHub complies because it has to. Decentralized infrastructure—which powers Gitlawb, torrents, and cryptocurrency itself—doesn't have the same single point of failure. When a company tries to pull something back from the internet, the only question is how many mirrors exist and on what kind of infrastructure. The answer here, within hours, was: enough.

### Daily DebriefNewsletter

Start every day with the top news stories right now, plus original features, a podcast, videos and more.
Your Email
Get it!
Get it!