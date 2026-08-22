---
title: Bun 1.4 Rust rewrite is not looking good • Tero Piirainen
url: https://tipiirai.com/writing/bun-rust-rewrite-worries
site_name: tldr
content_file: tldr-bun-14-rust-rewrite-is-not-looking-good-tero-piira
fetched_at: '2026-08-23T06:00:36.506358'
original_url: https://tipiirai.com/writing/bun-rust-rewrite-worries
date: '2026-08-23'
description: Bun 1.4 Rust rewrite is not looking good (5 minute read)
tags:
- tldr
---

# Bun 1.4 Rust rewrite is not looking good

I care about Bun. I have been rooting for it since the initial release in 2022. I switched all my development from Node to Bun. I used it in the development of theNue frameworkand now with my new projectHertta.

The last three months have not looked good for Bun. It started as one of the most impressive individual engineering projects I have seen, but has now turned into this weird AI-powered creature with continuous false promises and an increasingly frustrated community.

## In the next version of Bun

In the next version of Bunused to be a positive tweet to watch for. For years it meant a feature had been implemented, tested, and would ship in a few days. This changed after the Rust rewrite. Now the posts are false promises about the upcoming release:

Jun 24
Bun v1.4 ships July 7th.
Jul 4
Bun v1.4 hopefully Tuesday
Jul 7
(The date passes)
Jul 14
In the next version of Bun
Jul 20
In the next version of Bun
Jul 29
Bun v1.4 fixes over 3000 issues over v1.3
Aug 1
In the next version of Bun
Aug 4
In the next version of Bun
Aug 7
1 more PR to merge then it’ll be time for Bun v1.4
Aug 13
Bun v1.4 is compiling.
Aug 15
Bun v1.4 is delayed until Monday
Aug 17
Let’s say tomorrow

It’s now three months and counting since the last stable release, the longest gap in Bun’s history since 2022. Nothing unusual there. Software slips, that’s normal. It’s just that an account which used to communicate with real dates and real numbers has switched to vibing. And the user reaction is what you’d expect after constant false promises:

@jarredsumnerokay I’m editing blog post it’s mostly done if I say a date you won’t believe me but let’s say tomorrow

We totally believe in you, Jarred

Rejoice fellas, tomorrow in Jarred Standard Time zone means we have a new blog coming next week.

You won’t care, but personally I am switching to go now. It’s not even funny, you are just stringing your users along again and again.

How can we believe you? You always make promises that you can’t keep, tomorrow, next week, Monday...

If you need 2 months to release it you can just say that instead of saying you’ll ‘release it tomorrow’ every week

## Bun on GitHub

The Bun 1.4 rewrite is a big bet on AI. In the past month, 15.8k commits came fromrobobun,1.6k commits fromautofix-ci[bot],and 790 commits from Jarred.

6 months ago, most of Bun’s PRs came from people prompting Claude. Nowadays, most of Bun’s PRs come from Claude prompting Claude.

The project has over5k open pull requests, which is the largest number of pull requests I’ve seen. For comparison,OpenClawhas 2.2k, andReacthas 441. GitHub recommends staying under 1,000 open PRs against a single branch before mergeability checks start timing out.

The biggest worry is, of course, the code itself. In the early days Jarred’s work was inspirational. I thought he was a true Zig talent, until I read Zig creator Andrew Kelley’sthoughts on the Bun rewrite:

We became increasingly horrified at the programming practices we saw in Bun’s codebase. Hacks on top of hacks. Abuse of assertions. Jarred was already writing slop well before he had access to LLMs.

## What was the problem with Zig?

This rewrite isthemost closely watched real-world test of whether AI agents can take over a production codebase with a human mostly directing rather than reading. Anthropic’s own reputation is also on the line: if this goes well, it is real proof of what agentic coding can do. If it goes badly, it will send a signal in the opposite direction.

The number of unsafe blocks in the Rust code suggests the rewrite did not deliver the memory safety that was given as the reason for doing the rewrite in the first place. Instead this rewrite feels more like an Anthropic ad.

And was Zig really the problem? Bun’s early identity was built on Zig: its performance, its fast compile times, its low friction, its direct memory control with a small team.

It feels like Jarred and Anthropic decided early on that this was going to be written in Rust, and used Zig’s memory issues as the excuse to let the world know how powerful Claude is. A rewrite like this would make great headlines, and it certainly did. Now we’re looking at the long tail of issues from the rewrite they didn’t prepare for.

Maybe Bun should have put that same AI-assisted effort into disciplined, human-understood Zig instead of a full language change. I never saw Jarred seriously engage with this option.

And ‘tomorrow’ has come and gone. Still no v1.4.

¯\_(ツ)_/¯