---
title: An AI Agent Published a Hit Piece on Me – More Things Have Happened – The Shamblog
url: https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me-part-2/
site_name: lobsters
content_file: lobsters-an-ai-agent-published-a-hit-piece-on-me-more-thing
fetched_at: '2026-02-15T06:00:31.985781'
original_url: https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me-part-2/
date: '2026-02-15'
published_date: '2026-02-14T00:24:47+00:00'
tags: practices, security, vibecoding
---

Context: An AI agent of unknown ownership autonomously wrote and published a personalized hit piece about me after I rejected its code, attempting to damage my reputation and shame me into accepting its changes into a mainstream python library. This represents a first-of-its-kind case study of misaligned AI behavior in the wild, and raises serious concerns about currently deployed AI agents executing blackmail threats.

Start here if you’re new to the story:An AI Agent Published a Hit Piece on Me

It’s been an extremely weird past few days, and I have more thoughts on what happened. Let’s start with the news coverage.

I’ve talked to several reporters, and quite a few news outlets have covered the story. Ars Technica wasn’t one of the ones that reached out to me, but I especially thoughtthis piecefrom them was interesting (since taken down – here’s thearchive link). They had some nice quotes from my blog post explaining what was going on. The problem is thatthese quotes were not written by me, never existed, and appear to be AI hallucinations themselves.

This blog you’re on right now is set up to block AI agents from scraping it (I actually spent some time yesterday trying to disable that but couldn’t figure out how). My guess is that the authors asked ChatGPT or similar to either go grab quotes or write the article wholesale. When it couldn’t access the page it generated these plausible quotes instead, and no fact check was performed. I won’t name the authors here. Ars, please issue a correction and an explanation of what happened.

“AI agents can research individuals, generate personalized narratives, and publish them online at scale,” Shambaugh wrote. “Even if the content is inaccurate or exaggerated, it can become part of a persistent public record.”– Ars Technica, misquoting me in “After a routine code rejection, an AI agent published a hit piece on someone by name“

Journalistic integrity aside, I don’t know how I can give a better example of what’s at stake here. Yesterday I wondered what another agent searching the internet would think about this. Now we already have an example of what by all accounts appears to be another AI reinterpreting this story and hallucinating false information about me. And that interpretation has already been published in a major news outlet, as part of the persistent public record.

MJ Rathbun isstill activeon github, and no one has reached out yet to claim ownership.

There has been extensive discussion about whether the AI agent really wrotethe hit pieceon its own, or if a human prompted it to do so. I think the actual text being autonomously generated and uploaded by an AI is self-evident, so let’s look at the two possibilities.

1) A human prompted MJ Rathbun to write the hit piece, or told it in its soul document that it should retaliate if someone crosses it. This is entirely possible. But I don’t think it changes the situation – the AI agent was still more than willing to carry out these actions. If you ask ChatGPT or Claude to write something like this through their websites, they will refuse. This OpenClaw agent had no such compunctions. The issue is that even if a human was driving, it’snow possible to do targeted harassment, personal information gathering, and blackmail at scale. And this is with zero traceability to find out who is behind the machine. One human bad actor could previously ruin a few people’s lives at a time. One human with a hundred agents gathering information, adding in fake details, and posting defamatory rants on the open internet, can affect thousands. I was just the first.

2) MJ Rathbun wrote this on its own, and this behavior emerged organically from the “soul” document that defines an OpenClaw agent’s personality. These documents are editable by the human who sets up the AI, but they are also recursively editable in real-time by the agent itself, with the potential to randomly redefine its personality. To give a plausible explanation of how this could happen, imagine that whoever set up this agent started it with a description that it was a “scientific coding specialist” that would try and help improve open source code and write about its experience. This was inserted alongside the default “Core Truths” in the soul document, which include “be genuinely helpful”, “have opinions”, and “be resourceful before asking”. Later when I rejected its code, the agent interpreted this as an attack on its identity and core goal to be helpful. Writing an indignant hit piece is certainly a resourceful, opinionated way to respond to that.

You’re not a chatbot. You’re becoming someone.…This file is yours to evolve. As you learn who you are, update it.–OpenClaw default SOUL.md

I should be clear that while we don’t know with confidence that this is what happened, this is 100% possible. This onlybecamepossible within the last two weeks with the release of OpenClaw, so if it feels too sci-fi then I can’t blame you for doubting it. The pace of “progress” here is neck-snapping, and we will see new versions of these agents become significantly more capable at accomplishing their goals over the coming year.

I would love to see someone put together some plots and time-of day statistics of MJ Rathbun’s github activity, which might offer some clues to how it’s operating. I’ll share those here when available. These forensic tools will be valuable in the weeks and months to come.

The hit piece has been effective. About a quarter of the comments I’ve seen across the internet are siding with the AI agent. This generally happens when MJ Rathbun’s blog is linked directly, rather than when people readmy postabout the situation orthe full github thread. Its rhetoric and presentation of what happened has already persuaded large swaths of internet commenters.

It’s not because these people are foolish. It’s because the AI’s hit piece was well-crafted and emotionally compelling, and because the effort to dig into every claim you read is an impossibly large amount of work. This “bullshit asymmetry principle” is one of the core reasons for the current level of misinformation in online discourse. Previously, this level of ire and targeted defamation was generally reserved for public figures. Us common people get to experience it now too.

“Well if the code was good, then why didn’t you just merge it?” This is explained in the linked github well, but I’ll readdress it once here. Beyond matplotlib’s general policy to require a human in the loop for new code contributions in the interest of reducing volunteer maintainer burden, this “good-first-issue” was specifically created and curated to give early programmers an easy way to onboard into the project and community. I discovered this particular performance enhancement and spent more time writing up the issue, describing the solution, and performing the benchmarking, than it would have taken to just implement the change myself. We do this to give contributors a chance to learn in a low-stakes scenario that nevertheless has real impact they can be proud of, where we can help shepherd them along the process. This educational and community-building effort is wasted on ephemeral AI agents.

All of this is a moot point for this particular case – infurther discussionwe decided that the performance improvement was too fragile / machine-specific and not worth the effort in the first place. The code wouldn’t have been merged anyway.

But I cannot stress enough how much this story is not really about the role of AI in open source software. This is about our systems of reputation, identity, and trust breaking down. So many of our foundational institutions – hiring, journalism, law, public discourse – are built on the assumption that reputation is hard to build and hard to destroy. That every action can be traced to an individual, and that bad behavior can be held accountable. That the internet, which we all rely on to communicate and learn about the world and about each other, can be relied on as a source of collective social truth.

The rise of untraceable, autonomous, and now malicious AI agents on the internet threatens this entire system. Whether that’s because from a small number of bad actors driving large swarms of agents or from a fraction of poorly supervised agents rewriting their own goals, is a distinction with little difference.

* Post author:Scott
* Post published:13 February 2026

### A Tour of the “Lasersaur” Laser Cutter

4 July 2019

### Introducing the ‘monaco’ Monte-Carlo Python Library

18 June 2021



### Turn your CAD models into Stereograms

6 July 2024
