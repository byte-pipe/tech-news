---
title: A Unix Manifesto for the Age of AI | LinuxToaster
url: https://linuxtoaster.com/manifesto.html
site_name: tldr
content_file: tldr-a-unix-manifesto-for-the-age-of-ai-linuxtoaster
fetched_at: '2026-03-11T19:21:33.044220'
original_url: https://linuxtoaster.com/manifesto.html
author: Dirk Harms-Merbitz
date: '2026-03-11'
published_date: '2026-03-05'
description: Taste is the only thing standing between us and entropy. A manifesto on composable AI, Unix principles, and the architecture of restraint.
tags:
- tldr
---

Manifesto

# A Unix Manifesto for the Age of AI

LinuxToaster · March 2026

Software has always trended toward complexity. Organizations reward it. Careers are built on it. AI has now removed the last friction that kept it in check. What remains — the only thing that has ever kept complexity from becoming entropy — is taste.

Principle I

## Complexity is the default. Simplicity is a decision.

No system becomes simple on its own. Every force in software development pushes toward more: more features, more abstraction, more defensive code, more ownership surface. AI accelerates all of it. A model asked to build something will build something thorough, comprehensive, and mediocre. It cannot decide what to leave out. That decision requires a human, and it requires will.

Simplicity is not a starting condition. It is an act of sustained refusal.

Principle II

## Complexity without taste is a career strategy, not an engineering outcome.

Inside organizations, complexity creates leverage. The engineer who owns a system no one else understands cannot be replaced. The manager whose team holds proprietary infrastructure cannot be reorganized away. This is not a bug in human nature. It is a rational response to how most engineering organizations measure and reward work.

AI has made this strategy essentially free to execute. What used to take months of skilled work now takes a week of prompting. The debt still accumulates. The person who introduced it will be three companies up their career path before it comes due. The code remains — unmaintained, undocumented, understood by no one — a zombie, kept alive by whoever inherits it and an AI that can navigate the mess without comprehending it.

The technical manager often makes this worse. Political pressure flows down, engineering reality flows up, and both get distorted in translation. Complexity accumulates in the gap. We name this plainly: it is a corruption of the engineering role, and tooling that makes it easier is tooling that works against us.

Principle III

## Architecture encodes taste. Design your tools accordingly.

The Unix philosophy survived fifty years not because its authors wrote good documentation, but because they built restraint into the architecture. A tool that does one thing is hard to corrupt into a tool that does everything. A clean interface resists the accumulation of hidden state. Composition at the boundary keeps failure modes local.

Taste doesn't have to depend on individual engineers — who will leave, who face promotion incentives, who are human. It can be encoded in the tools themselves. The right architecture makes the simple path the natural one. The wrong architecture makes complexity the path of least resistance, and then AI hands everyone a shovel.

Principle IV

## AI should be a pipe, not a platform.

The most consequential choice in AI tooling isn't which model to use. It's whether AI becomes something you compose with, or something you get locked into.

A monolithic AI platform — a chat interface you surrender context to, a copilot embedded in your codebase, an assistant that manages your workflow — hides complexity inside itself. It generates solutions you can't inspect, in the shape of tools you can't decompose. Every problem becomes a reason to go deeper. The intelligence is real. The lock-in is real. And the complexity it creates is yours to keep.

A pipe is different. You see what goes in and what comes out. The tool does one thing. You chain tools together the same way Unix always has — at the boundary, explicitly, with the option to swap any piece out. No empire. Just pipes.

Here is what that looks like in practice. These are real LinuxToaster tools running today:

ps aux | toast "what is going on here?"
emails unread | toast "anything interesting in those emails?" | imessage

toastissedwith a brain.emailsis the command line email client.imessagetexts you the answer. Same Unix contract throughout: do one thing, honor the pipe, get out of the way.

Principle V

## Local inference is sovereignty. Cloud is a choice, not a dependency.

When your tools require a round trip to a cloud provider, your workflow has a landlord. Your data leaves the machine. Your latency is subject to someone else's infrastructure. Your capability disappears when the API is down or the pricing changes.

Local inference on capable hardware — a model running on your machine, on your data, at your speed — is not a performance optimization. It is a statement about who controls the tool. The pipe should run end to end without permission. Cloud inference is available when you want it. It is not the default you are forced into.

Principle VI

## The engineer who knows what to delete is the engineer who matters.

The skill in engineering has always been to look at what was generated and know what should not exist. AI just increases the velocity.

Chuck Moore built polyForth, cmForth, and finally colorForth — a complete operating system, language, and development environment — in roughly 2,000 lines. Not because the problem was small. Because he deleted everything he could not justify. He did this repeatedly, throwing away entire stacks and starting over, not to improve them but to strip them back to what was necessary. Deletion was the practice.

That judgment — taste — is the ability to impose a stopping condition on a process that has none. AI has no stopping condition. Organizations optimizing for output have no stopping condition. The engineer with taste is the check. They are currently working against every incentive available to them, in most organizations, with no structural support.

LinuxToaster builds tools for AI Ops engineers. Tools where the architecture of the tool makes simplicity the natural outcome. Tools that do not require heroic individual will to resist becoming a platform.

Forth and Unix arrived at the same place from different directions: composable, bottom-up, built from primitives that do one thing. Forth uses a stack. Unix uses text streams. Both resist building castles. When two traditions converge on the same principles without coordination, those principles are probably right.

For the era of AI it means intelligence should flow through pipes, not accumulate in platforms. Systems that age well are the ones built by people who knew when to stop.

AI changes the speed. It does not change the principle. Taste still stands between us and entropy.

Published by

LinuxToaster
 — composable AI tools for the terminal.

 Unix reimagined.
