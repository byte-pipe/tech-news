---
title: We’ve raised $17M to build what comes after Git | Butler's Log
url: https://blog.gitbutler.com/series-a
site_name: hackernews_api
content_file: hackernews_api-weve-raised-17m-to-build-what-comes-after-git-butl
fetched_at: '2026-04-11T06:00:13.856907'
original_url: https://blog.gitbutler.com/series-a
author: Scott Chacon
date: '2026-04-10'
published_date: '2026-04-08T16:00:00.000Z'
description: GitButler has raised a Series A round to accelerate developing the infrastructure for how software gets built next
tags:
- hackernews
- trending
---

TodaybyScott Chacon

4
 min read
company
fundraising

# We’ve raised $17M to build what comes after Git

GitButler has raised a Series A round to accelerate developing the infrastructure for how software gets built next

Today we’re announcing thatGitButler has raised a $17M Series Aled bya16zwith continuing support from our lead seed investors,Fly VenturesandA Capital.

I know what you’re thinking. You’re hoping that we’ll use phrases such as “we’re excited,” “this is just the beginning,” and “AI is changing everything”. While all those things are true, I’ll try to avoid them and instead make this announcement a little more personal.

Our new board member, a16z's Peter Levine, and myself at the GitButler Series A signing. We're excited to have Peter join us - he and I also worked together on GitHub's board.

For me this is a long story.

I was one of the cofounders ofGitHuband over the last 15 years I’ve watched Git go from a rather niche developer tool written for a very esoteric collaboration style to the foundational infrastructure of all software development on the planet. I may have even had a small hand in some part of that.

What I learned from watching that story unfold is that developer platforms win when they remove friction from collaboration, and when they let the people producing code have less overhead to deal with.

GitButler was started three years ago because we felt like our development practices have been shoehorned into what Git could do for such a long time, it would be amazing to see what we could do with tooling that was actually designed for those practices.

That’s fundamentally what is behind this round.

We think software development is quickly moving into a new phase, and the problem that Git has solved for thelast 20 yearsis overdue for a redesign. Today, with Git, we're all teaching swarms of agents to use a tool built for sending patches over mailing lists. That's far from what is needed today.

At GitHub, one thing became painfully clear over and over: developers don’t struggle because they can’t write code. They struggle because context falls apart between tools, between people, and now between people and agents. The hard problem is not generating change, it’s organizing, reviewing, and integrating change without creating chaos.

The old model assumed one person, one branch, one terminal, one linear flow. Not only has the problem not been solved well for that old model, it’s now only been compounded with our new AI tools.

Last week we released our first answer to that, the technical preview ofthe GitButler CLI.

A quick tour through a typical workflow with the new GitButler CLI.

This is a tool designed for theGitHub Flowstyle - the short lived branch, trunk based workflows that so many of us are using. This is a tool designed for humans, designed for agents, designed for scripting. Designed tostack branches, tomultitask, to control andorganizeyour changes, to easilyundo- to be simple, powerful and intuitive, no matter who (or what) you are. Best of all, it just drops into any existing Git project.

But of course, that’s just the beginning. (Damn, I said I wasn’t going to say that…)

There was a tagline at GitHub that I always loved, but I never felt like we lived up to the promise of: “Social Coding”.

While GitHub certainly made it easier to collaborate on open source projects with forks and pull requests, it otherwise didn’t much improve the process of working together. There are still lists of issues and kanban boards, there are still patches (we just call them PRs now), we still chat in external chat rooms. We don’t look at commit messages and our PR descriptions aren’t stored in Git and usually lost in history. Heck, it could be argued that development in teams islesssocial than it was when version control was centralized.

But what if coding was actuallysocial? What if it was easier to for a team to work together than it is to work alone?

Imagine your version control tool taking what you’ve worked on and helping you craft logical, beautiful changes with proper context. Imagine being able to access agent interactions, related conversations and other information we’re currently losing. Imagine your tools telling you as soon as there are possible merge conflicts between teammates, rather than at the end of the process. Imaging being able to work on a branch stacked on a coworkers branch while you’re both constantly modifying them. Imagine your agent being fully aware of not only what your other agents are working on, but what everyone on your team is working on, right now.

There is so much more that this fundamental layer of our software tooling could be doing for us. This is what we’re doing at GitButler, this is why we’ve raised the funding to help build all of this, faster.

We’re not building some “better git”.

We’re building the infrastructure for how software gets built next.

Written byScott Chacon

Scott Chacon is a co-founder of GitHub and GitButler, where he builds innovative tools for modern version control. He has authored Pro Git and spoken globally on Git and software collaboration.

Website
|
X

### Relatedarticles

* GitButler's Annual Open Source Pledge ReportbyScott Chacon-2min read
* GitButler 0.15 - "Quirky Quinceañera"byScott Chacon-4min read
* GitButler is joining the Open Source PledgebyScott Chacon-6min read

## More toRead

### Announcing the GitButler CLI for Linux

This month
by

Simon Larsén
3
 min read

In early February, we announced But, the GitButler CLI. The announcement had one glaring flaw: Linux was never mentioned. Not. Even. Once. We're rectifying that now, because But loves Linux, and Linux will come to love But.

### The Great CSS Expansion

This month
by

Pavel Laptev
17
 min read

CSS now does what Floating UI, GSAP ScrollTrigger, Framer Motion, and react-select used to require JavaScript for. Here is exactly how much that saves, why these libraries were painful beyond their size, and what the platform still hasn't figured out.

### A couple of git nits

This month
by

Estib Vega
7
 min read

A small rant on git papercuts, and why they are like that.

## Stay in theLoop

Subscribe to get fresh updates, insights, andexclusive content delivered straight to your inbox.No spam, just great reads. 🚀

Subscribe
