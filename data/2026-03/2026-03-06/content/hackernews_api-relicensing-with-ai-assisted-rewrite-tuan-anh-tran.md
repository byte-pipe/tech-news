---
title: Relicensing with AI-assisted rewrite - Tuan-Anh Tran
url: https://tuananh.net/2026/03/05/relicensing-with-ai-assisted-rewrite/
site_name: hackernews_api
content_file: hackernews_api-relicensing-with-ai-assisted-rewrite-tuan-anh-tran
fetched_at: '2026-03-06T06:00:13.935597'
original_url: https://tuananh.net/2026/03/05/relicensing-with-ai-assisted-rewrite/
author: tuananh
date: '2026-03-05'
published_date: '2026-03-05T00:00:00+00:00'
description: 'Exploring the chardet v7.0.0 controversy: Can an AI rewrite legally ''launder'' a library from LGPL to MIT?'
tags:
- hackernews
- trending
---

March 5, 2026
 

 

# Relicensing with AI-assisted rewrite

##### Posted on 
 
 March 5, 2026
 

 
  •3 minutes
  •529 words

### Disclaimer

I am not a lawyer, nor am I an expert in copyright law or software licensing. The following post is a breakdown of recent community events and legal news; it should not be taken as legal advice regarding your own projects or dependencies.

In the world of open source, relicensing is notoriously difficult. Itusuallyrequires the unanimous consent of every person who has ever contributed a line of code, a feat nearly impossible for legacy projects.chardet, a Python character encoding detector used by requests and many others, has sat in that tension for years: as a port of Mozilla’s C++ code it was bound to the LGPL, making it a gray area for corporate users and a headache for its most famous consumer.

Recently the maintainers used Claude Code to rewrite the whole codebase and releasev7.0.0, relicensing from LGPL to MIT in the process. The original author,a2mark, saw this as a potential GPL violation:

Licensed code, when modified, must be released under the same LGPL license. Their claim that it is a “complete rewrite” is irrelevant, since they had ample exposure to the originally licensed code (i.e. this is not a “clean room” implementation). Adding a fancy code generator into the mix does not somehow grant them any additional rights.

## A clean room rewrite requires a wall that AI bypasses

In traditional software law, a “clean room” rewrite requires two teams:

* Team Alooks at the original code and writes a functional specification
* Team B(which has never seen the original code) writes new code based solely on that specification. By using an AI that was prompted with the original LGPL code, the maintainers bypassed this wall. If the AI “learned” from the LGPL code to produce the new version, the resulting output is arguably a derivative work, which under the LGPL, must remain LGPL.

## The Supreme Court created a legal paradox for the maintainers

Coincidentally, as this drama unfolded, theU.S. Supreme Court (on March 2, 2026) declined to hear an appealregarding copyrights for AI-generated material. By letting lower court rulings stand, the Court effectively solidified a “Human Authorship” requirement. That creates a massive legal paradox for the chardet maintainers:

* The copyright vacuum:If AI-generated code cannot be copyrighted (as the courts suggest), then the maintainers may not even have the legal standing to license v7.0.0 under MIT or any license.
* The derivative trap:If the AI output is considered a derivative of the original LGPL code, the “rewrite” is a license violation.
* The ownership void:If the code is truly a “new” work created by a machine, it might technically be in the public domain the moment it’s generated, rendering the MIT license moot.

## Accepting AI-rewriting as relicensing could spell the end of Copyleft

If “AI-rewriting” is accepted as a valid way to change licenses, it represents the end of Copyleft. Any developer could take a GPL-licensed project, feed it into an LLM with the prompt “Rewrite this in a different style,” and release it under MIT. The legal and ethical lines are still being drawn, and the chardet v7.0.0 case is one of the first real-world tests.

Follow me

Here's where I hang out in social media