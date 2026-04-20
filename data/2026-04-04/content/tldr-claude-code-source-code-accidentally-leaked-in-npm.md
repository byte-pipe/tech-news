---
title: Claude Code source code accidentally leaked in NPM package
url: https://www.bleepingcomputer.com/news/artificial-intelligence/claude-code-source-code-accidentally-leaked-in-npm-package/
site_name: tldr
content_file: tldr-claude-code-source-code-accidentally-leaked-in-npm
fetched_at: '2026-04-04T01:01:26.446549'
original_url: https://www.bleepingcomputer.com/news/artificial-intelligence/claude-code-source-code-accidentally-leaked-in-npm-package/
date: '2026-04-04'
description: Anthropic says it accidentally leaked the source code for Claude Code, which is closed source, but the company says no customer data or credentials were exposed.
tags:
- tldr
---

# Claude Code source code accidentally leaked in NPM package

 By

###### Mayank Parmar

* March 31, 2026
* 08:32 PM
* 0

Anthropic says it accidentally leaked the source code for Claude Code, which is closed source, but the company says no customer data or credentials were exposed.

While Anthropic pledges support to the open-source community, Claude Code has always remained closed source, at least it did until today, when an update accidentally included internal source code.

In a statement to BleepingComputer, Anthropic confirmed the leak and said no personal or sensitive information was published.

"Earlier today, a Claude Code release included some internal source code. No sensitive customer data or credentials were involved or exposed. This was a release packaging issue caused by human error, not a security breach. We're rolling out measures to prevent this from happening again," Anthropic told Bleepingcomputer.

The leaked source code was firstspottedby Chaofan Shou (@Fried_rice), and it has spread widely on GitHub and other storage platforms.

Claude Code source code leak

The source code was mistakenly leaked by Anthropic when they briefly published Claude Code version 2.1.88 on NPM earlier today.

This version included a 60 MB filecli.js.mapthat contained all of the source code for the latest version.

A source map file is a debugging file that links compiled JavaScript back to the original source code.

If the map files include a field called "sourcesContent" that embeds the full text of the original source files directly in the map, it is possible to reconstruct the entire source code tree from the file.

This is why including a large .map file in a public package can lead to a significant code exposure.

The reconstructed source code contains approximately 1,900 files, 500,000 lines of code, and details of several Claude-exclusive features.

While the source code has spread online, Anthropic has begun issuingDMCA infringement notificationsto take it down where possible.

Claude Code source taken down via a DMCA infringement notification
Source: BleepingComputer

Developers have already begun analyzing the source for undocumented features and learning how the application works.

According toAlex Finn, Anthropic is testing a new mode called "Proactive mode," where Claude will code for you 24/7. This mode was spotted in the Claude Code source.

There's another interesting feature that caught our attention.

It's called "Dream" mode, where Claude can constantly think in the background, develop ideas, improve your current plans, and try to solve problems while you are away.

## Anthropic has confirmed a Claude Code usage bug

In other news, users have alleged that Claude has quietly reduced usage limits. This means if you're on the Pro plan or even the Max plan (5x), you're going to hit Claude usage limits much faster.

I personally observed this behavior on my account with Claude Personal, which costs $20. After I sent a few messages to Claude in a Claude Code terminal, usage shot up to 30%, and it reached 100% after just a few minutes of interaction.

That was not expected behavior, especially since the context was not large, as I had only just begun interacting with Claude.

It turns out the issue is widespread, and Anthropic has confirmed that it's investigating a bug that causes limits to exhaust faster.

"We're aware people are hitting usage limits in Claude Code way faster than expected. Actively investigating, will share more when we have an update," Anthropic’s Lydia Hallie wrote in aposton X.

As of March 31, 14:00 PM ET, the issue remains unresolved, and Anthropic has shared the following update:

"[We're] still working on this. It's the top priority for the team. I know this is blocking a lot of you. More as soon as we have it."

Some users argue that it could be an intentional change by Anthropic, as Claude's popularity has been rising over the past few weeks, but we can't tell if it's intentional without more details from the company.

## Automated Pentesting Covers Only 1 of 6 Surfaces.

Automated pentesting proves the path exists. BAS proves whether your controls stop it. Most teams run one without the other.

This whitepaper maps six validation surfaces, shows where coverage ends, and provides practitioners with three diagnostic questions for any tool evaluation.

Get Your Copy Now

### Related Articles:

Anthropic confirms Claude is down in a worldwide outage

Claude Code leak used to push infostealer malware on GitHub

Bubble AI app builder abused to steal Microsoft account credentials

Google Drive ransomware detection now on by default for paying users

CISA: New Langflow flaw actively exploited to hijack AI workflows
