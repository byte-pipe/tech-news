---
title: Using AI to write better code more slowly | Read the Tea Leaves
url: https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/
site_name: hackernews_api
content_file: hackernews_api-using-ai-to-write-better-code-more-slowly-read-the
fetched_at: '2026-05-26T19:41:30.661145'
original_url: https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/
author: signa11
date: '2026-05-25'
published_date: '2026-05-25T16:16:40+00:00'
description: A lot of people seem convinced that the point of AI coding is to write low-quality code as fast as possible. Spew out barely-passable slop, open massive PRs, and merge them unvetted. Ship it! But the thing is, LLMs are very flexible. And you can use them just as effectively to write high-quality code more…
tags:
- hackernews
- trending
---

# Read the Tea LeavesSoftware and other dark arts, by Nolan Lawson

* Home
* Apps
* Code
* Talks
* About

25May

## Using AI to write better code more slowly

Posted May 25, 2026 by Nolan Lawson insoftware engineering.			Tagged:AI.12 Comments

A lot of people seem convinced that the point of AI coding is to write low-quality code as fast as possible. Spew out barely-passable slop, open massive PRs, and merge them unvetted. Ship it!

But the thing is, LLMs are very flexible. And you can use them just as effectively to writehigh-qualitycode moreslowly.

This statement seems completely obvious to me at this point, and I almost didn’t want to write this post for that reason. But there seem to be enough people convinced that LLMs are only good asslop cannonsthat it’s worth making the opposite case.

IfMythostaught us anything, it’s that LLM agents arereally goodat finding bugs. Throw them at a codebase enough times, and they will find so many bugs that you’ll barely know what to do with them.

Likemany others, I’ve also found this is true of non-Mythos models – some may be better than others at finding subtle bugs or avoiding false positives, but the fact is that the latest public models from Anthropic and OpenAI are good enough to find plenty of bugs in an unscrutinized codebase.

The problem is not so muchfindingthe bugs, but instead prioritizing and validating them. For this reason I have a Claude skill I adapted fromthis article‘s core insight, which is that the more, different models you throw at a PR review, the less likely you are to get hallucinations or bogus bugs.

The skill says (paraphrasing):

Run a Claude sub-agent, Codex, and Cursor Bugbot to find bugs in this PR ranked by critical/high/medium/low. Once they’re all done, review their findings, do your own research to rule out false positives, and write a final report.

That’s basically it. You can add your own definition of “bug” if you want – mine has stipulations about theKISSandDRYprinciples, writing accessible HTML/JSX, using proper indexes for SQL queries, etc.

In my experience, this skill always finds tons of bugs in a PR, and the false positive rate is near zero. It finds so many bugs that you’ll be bored senseless if you try to tackle them all. They’ll range from critical security or correctness bugs to the more mundane medium-level perf bugs to low-level “this comment is misleading”-type bugs.

My typical workflow is:

* Have an agent fix all the criticals and highs (with my guidance on the proper solution), then repeat until no criticals/highs
* Skip highs/mediums where the juice isn’t worth the squeeze (e.g. 100 lines of code to fix a narrow edge case)
* Abandon the PR if it has so many criticals that I realize the whole approach is misguided

When I use this technique, I haven’t necessarily seen my velocity go up. If anything, the review process often findspre-existingbugs, so I end up on a tangential side-quest where I’m writing unit tests and fixing subtle flaws that pre-date the PR. This is the opposite of the “10x productivity” slop-cannon style of development that most people imagine when they think of vibe coding, but I find it very satisfying.

It’s a great way to improve the overall health of the codebase while also teaching you about the odd corners of it. In my experience, the happy-path of a complex architecture is less interesting than its failure modes. And pre-LLMs, this is usually how I got familiar with a codebase anyway: understanding where the assumptions break down, and then getting my hands dirty to fix it.

If you’re the kind of person who is skeptical that AI coding is good foranything, then I doubt this post will persuade you. But if you’re the kind of developer who uses agents to write multi-hundred-line PRs that you barely understand yourself, I’d invite you to slow down a bit and try this other, slower style of “vibe coding.” Ask an agent how your PR works and how it might fail. Have it write Markdown docs withMermaid chartsif necessary. UseMatt Pocock’s/grill-meskill until you understand the entire PR front-to-back.

You might not be more “productive” in terms of raw lines of code. You might burn a ton of tokens just to find out that your entire plan was wrongheaded from the start. But I find this style of coding to be a more super-powered version of the kind of programming I was already trying to do before LLMs: careful, methodical, quality-obsessed, focused on making things better for the next coder.

So take a deep breath, slow down, try this technique, and see if you don’t enjoy writing better code more slowly.

### Related

 

### Recent Posts

* Using AI to write better code more slowly
* The diminished art of coding
* You had a story
* Days of miracle and wonder
* We mourn our craft

### About Me

I'm Nolan, a programmer from Seattle working at Socket. All opinions are my own. Photo by Cătălin Mariș.

### Archives

* May 2026(1)
* March 2026(1)
* February 2026(4)
* January 2026(2)
* December 2025(4)
* November 2025(1)
* August 2025(1)
* June 2025(1)
* April 2025(1)
* January 2025(1)
* December 2024(2)
* October 2024(2)
* September 2024(3)
* August 2024(1)
* July 2024(1)
* March 2024(1)
* January 2024(1)
* December 2023(4)
* August 2023(2)
* January 2023(2)
* December 2022(1)
* November 2022(2)
* October 2022(2)
* June 2022(4)
* May 2022(3)
* April 2022(1)
* February 2022(1)
* January 2022(1)
* December 2021(3)
* September 2021(1)
* August 2021(6)
* February 2021(2)
* January 2021(2)
* December 2020(1)
* July 2020(1)
* June 2020(1)
* May 2020(2)
* February 2020(1)
* December 2019(1)
* November 2019(1)
* September 2019(1)
* August 2019(2)
* June 2019(4)
* May 2019(3)
* February 2019(2)
* January 2019(1)
* November 2018(1)
* September 2018(5)
* August 2018(1)
* May 2018(1)
* April 2018(1)
* March 2018(1)
* January 2018(1)
* December 2017(1)
* November 2017(2)
* October 2017(1)
* August 2017(1)
* May 2017(1)
* March 2017(1)
* January 2017(1)
* October 2016(1)
* August 2016(1)
* June 2016(1)
* April 2016(1)
* February 2016(2)
* December 2015(1)
* October 2015(1)
* September 2015(1)
* July 2015(1)
* June 2015(2)
* October 2014(1)
* September 2014(1)
* April 2014(1)
* March 2014(1)
* December 2013(2)
* November 2013(3)
* August 2013(1)
* May 2013(3)
* January 2013(1)
* December 2012(1)
* November 2012(1)
* October 2012(1)
* September 2012(3)
* June 2012(2)
* March 2012(3)
* February 2012(1)
* January 2012(1)
* November 2011(1)
* August 2011(1)
* July 2011(1)
* June 2011(3)
* May 2011(2)
* April 2011(4)
* March 2011(1)

### Tags

accessibility

AI

alogcat

android

android market

apple

app tracker

benchmarking

boost

bootstrap

browsers

bug reports

catlog

chord reader

code

contacts

continuous integration

copyright

couch apps

couchdb

couchdroid

developers

development

emoji

grails

html5

indexeddb

information retrieval

japanese name converter

javascript

jenkins

keepscore

listview

logcat

logviewer

lucene

nginx

nlp

node

nodejs

npm

offline-first

open source

passwords

performance

pinafore

pokedroid

pouchdb

pouchdroid

query expansion

relatedness calculator

relatedness coefficient

s3

safari

satire

sectioned listview

security

semver

shadow dom

social media

socket.io

software development

solr

spas

supersaiyanscrollview

synonyms

twitter

ui design

ultimate crossword

w3c

webapp

webapps

web platform

web sockets

websql

### Links

* Mastodon
* GitHub
* npm

Blog at WordPress.com.

* Comment
* Reblog
* SubscribeSubscribedRead the Tea LeavesJoin 1,322 other subscribersSign me upAlready have a WordPress.com account?Log in now.
* Read the Tea Leaves
* Already have a WordPress.com account?Log in now.
* Read the Tea LeavesSubscribeSubscribedSign upLog inCopy shortlinkReport this contentView post in ReaderManage subscriptionsCollapse this bar
* Read the Tea Leaves
* SubscribeSubscribed
* Sign up
* Log in
* Copy shortlink
* Report this content
* View post in Reader
* Manage subscriptions
* Collapse this bar