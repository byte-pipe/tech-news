---
title: Anthropic says its leak-focused DMCA effort unintentionally hit legit GitHub forks - Ars Technica
url: https://arstechnica.com/ai/2026/04/anthropic-says-its-leak-focused-dmca-effort-unintentionally-hit-legit-github-forks/
site_name: newsfeed
content_file: newsfeed-anthropic-says-its-leak-focused-dmca-effort-uninte
fetched_at: '2026-04-04T01:03:06.493432'
original_url: https://arstechnica.com/ai/2026/04/anthropic-says-its-leak-focused-dmca-effort-unintentionally-hit-legit-github-forks/
date: '2026-04-02'
published_date: '2026-04-02T15:40:53+00:00'
description: But the effort to stop the spread of leaked Claude Code client code is an uphill battle.
tags:
- ars-technica
- ai
- anthropic
- claude code
---

Text
 settings

An Anthropic-backed DMCA effort to remove itsrecently leaked Claude Code client source codefrom GitHub this week resulted in the accidental removal of many legitimate forks of its official public code repository. While that overzealous takedown has now been reversed, Anthropic still faces an extreme uphill battle in limiting the spread of its recently leaked code.

The DMCA noticethat GitHub received late Tuesday focuses on a repository containing the leaked source code originally posted by GitHub user nirholas (archived here) and nearly 100 specifically named forks of that repository. In a note appended to that request, though, GitHub said it had acted to take down a network of 8,100 similar forked repositories because “the submitter alleged that all or most of the forks were infringing to the same extent as the parent repository.”

That expanded takedownaffected many repositories that didn’t contain leaked code but instead forkedAnthropic’s official public Claude Code repository, which the company shares to encourage public bug reports and fixes. Many coderstooktosocialmediato complain about being swept up in the DMCA dragnet despite not sharing any leaked code.

“I’m sorry that your people shipped your source code, and that your lawyers don’t know how to read a repo,” coder Robert McLawswrote. “I will be filing a DCMA counter-notice.”

By Wednesday, Anthropic had moved to fix the issue with GitHub,requestingthat the site restrict its takedowns to the 96 fork URLs specifically listed in its takedown notice and to “reinstate all other repositories that were disabled by network-wide processing.” Anthropic’s head of Claude Code, Boris Cherny,said on social mediathat the overzealous takedowns were “not intentional,” and Anthropic’s Thariq Shihiparaddedthat they were the result of “a communication mistake.”

“The repo named in the notice was part of a fork network connected to our own public Claude Code repo, so the takedown reached more repositories than intended,” an Anthropic spokespersontold TechCrunch. “We retracted the notice for everything except the one repo we named, and GitHub has restored access to the affected forks.”

## Closing the barn door

Even with the corrected focus on leaked code, Anthropic will struggle to stop or even materially slow the spread of its Claude Code client source code across the Internet. As of this writing, many copies of that source code are still easy to find on GitHub, includingone Ars referenced in our own analysis yesterday. Copies of the leaked code have also appeared on other platforms,like the Germany-based Codeberg, which is outside the direct reach of the US DMCA (but whichmight be subject to similar local European laws).

Meanwhile, multiple enterprising coders have already used AI coding tools to develop so-called “clean room” reimplementations of the original Claude Code leak, converting the original TypeScript code into languages such asPythonandRust. Even if Anthropic could somehow remove every copy of its leaked code from the Internet, these functionally similar rewrites might be legally distinct (though there isstill some argumentover whether this kind of AI-written code can really claim the strict separation needed to avoid being considered a “derivative work.”)

Anthropic coders’ own use of Claude Code to write pieces of the Claude Code client could also complicate the legal status of the leaked code. Chernyadmitted in Decemberthat “in the last thirty days, 100% of my contributions to Claude Code were written by Claude Code.” That kind of admission could be significant, because while the US Copyright Officeoffers protection to “AI-assisted” codebases, that protectiongenerally doesn’t extend to work generated entirely by AI.

 Kyle Orland


Senior Gaming Editor

 Kyle Orland


Senior Gaming Editor

 Kyle Orland has been the Senior Gaming Editor at Ars Technica since 2012, writing primarily about the business, tech, and culture behind video games. He has journalism and computer science degrees from University of Maryland. He once
wrote a whole book about
Minesweeper
.


1. 1.New Rowhammer attacks give complete control of machines running Nvidia GPUs
2. 2.Here's what that Claude Code source leak reveals about Anthropic's plans
3. 3.SpaceX tries to convince FCC that Amazon put satellites into wrong altitude
4. 4.This Ford is the quickest production car at the Nürburgring, ever
5. 5.Artemis II is unlikely to be the cultural touchstone Apollo 8 was, and that's OK

Customize
