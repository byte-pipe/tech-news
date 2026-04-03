---
title: Fix your tools | Adolfo Ochagavía
url: https://ochagavia.nl/blog/fix-your-tools/
site_name: lobsters
content_file: lobsters-fix-your-tools-adolfo-ochagavía
fetched_at: '2026-02-23T06:00:34.317148'
original_url: https://ochagavia.nl/blog/fix-your-tools/
date: '2026-02-23'
published_date: '2026-02-21T00:00:00+00:00'
description: 'Last week I had to diagnose a bug in an open source library I maintain. The issue was gnarly enough that I couldn’t find it right away, but then I thought: if I set a breakpoint here and fire up the debugger, I will likely find the root cause very soon… and then proceed to mercilessly destroy it! So I rolled up my sleeves, set the breakpoint, fired up the debugger, and… saw the program run to completion without interruptions whatsoever.'
tags: debugging, programming
---

# Fix your tools

21 Feb, 2026

Last week I had to diagnose a bug in anopen source libraryI maintain. The issue was gnarly enough that I couldn’t find it right away, but then I thought: if I set a breakpointhereand fire up the debugger, I will likely find the root cause very soon… and then proceed to mercilessly destroy it!

So I rolled up my sleeves, set the breakpoint, fired up the debugger, and… saw the program run to completion without interruptions whatsoever. My breakpoint had been ignored, even though I knew for certain that the line of code in question must have been executed (I double-checked just to be sure).

Since I was in “problem solving mode”, I ignored the debugger issue and started thinking of other approaches to diagnosing it. Prey to my tunnel vision, I modified the code to log potentially interesting data, but it didn’t yield the insights I was hoping for. How frustrating!

My fingertips itched to write even more troubleshooting code when it suddenly dawned on me: just fix the darn debugger already! Sure, it might feel slower, but it will give you the ability to see what you need to see, and then actually solve the problem.

So I fixed the debugger (it turned out to be aone-line configuration change), observed the program’s behavior in more detail, and used that knowledge tosolve the issue.

What a paradox, I realized afterwards. The very desire to fix the bug prevented me from seeing I had to fix the tool first, and made me less effective in my bug hunt. This blog post is a reminder to myself, and to every bug-hungry programmer out there: fix your tools! They will do wonders for you.
