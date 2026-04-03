---
title: Writing code is cheap now - Agentic Engineering Patterns - Simon Willison's Weblog
url: https://simonwillison.net/guides/agentic-engineering-patterns/code-is-cheap/
site_name: hnrss
content_file: hnrss-writing-code-is-cheap-now-agentic-engineering-patt
fetched_at: '2026-02-24T11:20:10.167397'
original_url: https://simonwillison.net/guides/agentic-engineering-patterns/code-is-cheap/
author: Simon Willison
date: '2026-02-23'
description: Writing code is cheap now
tags:
- hackernews
- hnrss
---

# Simon Willison’s Weblog

Subscribe

Sponsored by:
 Teleport — Secure, Govern, and Operate AI at Engineering Scale.
Learn more

Guides>Agentic Engineering Patterns

## Writing code is cheap now

The biggest challenge in adopting agentic engineering practices is getting comfortable with the consequences of the fact thatwriting code is cheap now.

Code has always been expensive. Producing a few hundred lines of clean, tested code takes most software developers a full day or more. Many of our engineering habits, at both the macro and micro level, are built around this core constraint.

At the macro level we spend a great deal of time designing, estimating and planning out projects, to ensure that our expensive coding time is spent as efficiently as possible. Product feature ideas are evaluated in terms of how much value they can providein exchange for that time- a feature needs to earn its development costs many times over to be worthwhile!

At the micro level we make hundreds of decisions a day predicated on available time and anticipated tradeoffs. Should I refactor that function to be slightly more elegant if it adds an extra hour of coding time? How about writing documentation? Is it worth adding a test for this edge case? Can I justify building a debug interface for this?

Coding agents dramatically drop the cost of typing code into the computer, which disruptsso manyof our existing personal and organizational intuitions about which trade-offs make sense.

The ability to run parallel agents makes this even harder to evaluate, since one human engineer can now be implementing, refactoring, testing and documenting code in multiple places at the same time.

## Good code still has a cost

Delivering new code has dropped in price to almost free... but deliveringgoodcode remains significantly more expensive than that.

Here's what I mean by "good code":

* The code works. It does what it's meant to do, without bugs.
* Weknow the code works. We've taken steps to confirm to ourselves and to others that the code is fit for purpose.
* It solves the right problem.
* It handles error cases gracefully and predictably: it doesn't just consider the happy path. Errors should provide enough information to help future maintainers understand what went wrong.
* It’s simple and minimal - it does only what’s needed, in a way that both humans and machines can understand now and maintain in the future.
* It's protected by tests. The tests show that it works now and act as a regression suite to avoid it quietly breaking in the future.
* It's documented at an appropriate level, and that documentation reflects the current state of the system - if the code changes an existing behavior the existing documentation needs to be updated to match.
* The design affords future changes. It's important to maintainYAGNI- code with added complexity to anticipate future changes that may never come is often bad code - but it's also important not to write code that makes future changes much harder than they should be.
* All of the other relevant "ilities" - accessibility, testability, reliability, security, maintainability, observability, scalability, usability - the non-functional quality measures that are appropriate for the particular class of software being developed.

Coding agent tools can help with most of this, but there is still a substantial burden on the developer driving those tools to ensure that the produced code is good code for the subset of good that's needed for the current project.

## We need to build new habits

The challenge is to develop new personal and organizational habits that respond to the affordances and opportunities of agentic engineering.

These best practices are still being figured out across our industry. I'm still figuring them out myself.

For now I think the best we can do is to second guess ourselves: any time our instinct says "don't build that, it's not worth the time" fire off a prompt anyway, in an asynchronous agent session where the worst that can happen is you check ten minutes later and find that it wasn't worth the tokens.

Red/green TDD
 →





This is a chapter from the guideAgentic Engineering Patterns.

Chapters in this guide

1. Writing code is cheap now
2. Testing and QARed/green TDD
3. Red/green TDD

 coding-agents

159

 ai-assisted-programming

346

 generative-ai

1656

 ai

1869

 llms

1621

 agentic-engineering

11

Next:Red/green TDD





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
