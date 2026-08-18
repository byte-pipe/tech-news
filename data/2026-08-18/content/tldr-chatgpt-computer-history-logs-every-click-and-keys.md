---
title: ChatGPT Computer History Logs Every Click and Keystroke on Your Mac - Hardware Busters
url: https://hwbusters.com/news/chatgpt-computer-history-logs-every-click-and-keystroke-on-your-mac/
site_name: tldr
content_file: tldr-chatgpt-computer-history-logs-every-click-and-keys
fetched_at: '2026-08-18T11:23:12.259467'
original_url: https://hwbusters.com/news/chatgpt-computer-history-logs-every-click-and-keystroke-on-your-mac/
author: crmaris
date: '2026-08-18'
published_date: '2026-08-16T15:13:38+00:00'
description: ChatGPT Computer History records clicks, keystrokes and app switches on macOS, then stores the summaries as unencrypted Markdown files on your own disk.
tags:
- tldr
---

* Home
* News
* ChatGPT Computer History Logs Every Click and Keystroke on Your Mac
 

 

News
 

# ChatGPT Computer History Logs Every Click and Keystroke on Your Mac

 

August 16, 2026
August 16, 2026
 
crmaris
 

OpenAI’s new macOS memory feature swaps screenshots for an event log read through the accessibility API. What it writes to your disk is plain, unencrypted Markdown.

OpenAI has started shippingComputer History, a ChatGPT desktop feature that watches what you do on your Mac and turns it into a memory the assistant can search later. It does not photograph your screen. It records the interaction stream instead: clicks, typing, keyboard shortcuts, app switches, and whatever context macOS hands over through its accessibility system.

That is a deliberate break from what came before. Chronicle, the research preview Computer History replaces, worked off screenshots, the same broad approach that got Microsoft’s Recall torn apart on arrival. OpenAI rebuilt the idea rather than renaming it, and the rebuild trades pixels for semantics. A screenshot tells you what a window looked like at 09:41. An event log tells you that you switched to Terminal, typed a thousand characters, and clicked a button labelled “Deploy”.

## What it captures, and what it doesn’t

OpenAI is specific about the exclusions. No screenshots, no screen recordings, no microphone, no system audio. Activity in a private browsing window never enters the stream. You pick which apps and sites are in scope, and the whole thing is off until you switch it on.

The raw events are short-lived. They get bundled up, sent to OpenAI’s servers and converted into text summaries; the company says it does not keep those event files after processing unless legally obliged to, and does not train on them. What comes back down is the part worth paying attention to.

## The memory files are plain text

Those summaries are written to your Mac as Markdown, and they stay there until you delete them. They are also, by OpenAI’s own admission,not encrypted, which means any other program running under the same macOS user account can read them. That is not a researcher’s disclosure or a bug report. It is in the documentation.

Think about what a week of those files actually holds. Not passwords, hopefully, but the shape of your working life: who you were emailing at 2am, which repository you deployed on a Friday afternoon, the app you keep drifting back to. A plaintext file that any stray Electron app or a malicious package install script can open is a different risk profile from a screenshot cache sitting behind an encrypted store, and it is worth understanding as one before you flip the toggle.

## Who can turn it on

Computer History is macOS-only for now and limited to Pro, Business and Enterprise plans, with Business and Enterprise users needing an administrator to unlock it first. It is unavailable in the EEA, the UK and Switzerland, which is usually the tell that the privacy questions are not settled to a regulator’s satisfaction.

None of that makes the feature indefensible. An agent that can act on your computer is genuinely more useful when it remembers what you did on it, and an event log is a more honest design than quietly hoarding screen captures. But “we only log the keystrokes, not the pixels” is a strange sentence to find reassuring, and the unencrypted storage is the detail that ought to decide it either way.

Sources:OpenAI’s Computer History documentation,The RegisterandMacStories.

 

## Related Posts

 

News
 
 

#### GPU Tweak III Auto-Shutdown Arrives: 12.5A per Wire, and Off by Default

August 18, 2026
August 18, 2026
 
crmaris
 

 

News
 
 

#### Arctic Fan Controller Shipped With Its Linux Driver Already in the Kernel

August 18, 2026
August 18, 2026
 
crmaris