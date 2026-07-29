---
title: Superlogical
url: https://www.superlogical.com/
site_name: hackernews_api
content_file: hackernews_api-superlogical
fetched_at: '2026-07-29T19:31:34.086563'
original_url: https://www.superlogical.com/
author: yan
date: '2026-07-29'
description: Building the multiplexer for all work.
tags:
- hackernews
- trending
---

# We are building themultiplexer forall work.all work.local development.remote access.coding agents.background jobs.production applications.live debuggingsandboxes.shared terminals.incident response.humans and machines.operational history.multiplayer work.all work.

 

Building and operating software today spans local machines, remote hosts, sandboxes, services,
				and production systems. It has many modes of operation: interactively with a human developer,
				automatically through CI and background processes, and increasingly through agents working in
				parallel.

 

This work is all related, yet today's tools divide it into separate systems. Interactive tools
				assume a person at an interface. Automatic work disappears into jobs and logs. And as the work
				moves to production it lives behind separate systems and controls.

 

AI makes this fragmentation more visible and costly, but it did not create it. System
				administration, continuous integration, remote development and collaboration have strained the
				same boundaries for decades.

 

We believe the missing layer is a durable session around the work itself: one that can span
				applications and environments, provide relevant context by default, expose structured data and
				actions, preserve history, and be driven by software while remaining visible and controllable
				by people.

 

What we're building

 

This is our plan to build a multiplexer for all work:

 
1. 1Build an incredible multiplexer.
2. 2Make everything in it composable.
3. 3Make it safe and operable in production.
 

A multiplexer brings multiple independent streams together through a common interface. For us,
				that means interactive work, automatic work, and production work would share one well-crafted
				underlying system instead of living in separate tools.

 

We'll begin with a terminal multiplexer. It keeps multiple terminal blocks organized inside a
				long-lived session, so you can close the application, reconnect from another device, and pick
				up exactly where you left off.

 

If you're already familiar with terminal multiplexers, you'll feel right at home, but we're
				bringing a more modern touch. Sessions can be accessed through the web and native macOS/iOS
				applications, and sharing a live session with other people is built in from the start. We're
				also addressing the most common papercuts of existing tools, such as making scrollback,
				selection, and scrolling all work natively.

 

A terminal multiplexer may sound like a narrow place to start a company. Our vision is much
				larger, but terminals connect developers, agents, tools, and infrastructure so it is the right
				foundation for everything that follows. We will build a high-quality terminal multiplexer that
				remains excellent at that job, even as it grows to support the second and third parts of the
				plan. We'll have more to say about those later.

 

Who we are

 

We're a team that has spent our entire careers building some of the most widely used developer
				tooling, infrastructure software, and AI systems. We care deeply about well-crafted software
				that is beautiful to use, reliable in practice, and designed for others to build on.

 
* ### Mitchell HashimotoCreator of Ghostty. Co-founded HashiCorp and created Vagrant, Terraform, Vault, and more. Spent more than a decade as CEO and CTO from its earliest days through its IPO.
* ### Jack PearkesVP of Engineering and VP of R&D at HashiCorp, and its very first employee. Helped to create HashiCorp's first products and hired and led the original engineering team.
* ### Alasdair MonkHead of Experience at Poolside, VP of Design at Vercel, and a senior design leader at HashiCorp and Heroku. Two decades spent designing and building interfaces for developers.
* ### Hector SimpsonDesigned apps, services, and agentic experiences at Poolside. An interface designer and builder who has shipped developer-first products at Heroku, HashiCorp, Clearbit, and Vercel.
 

Superlogical is funded by:

 
* Notable Capital
* Amplify Partners
* Aaron Levie
* Armon Dadgar
* Dax Raad
* Greg Foster
* Guillermo Rauch
* Jacob Thornton
* Mario Zechner
* Merrill Lutsky
* Patrick Collison
* Stephen Haney
* Steve Ruiz
* Tobias Lütke
* Tomas Reimers
 

Get on the list for our first release

 
Email address
 
 
Press return or select the arrow to sign up.
 
 
 
 
 

We'll let you know when our beta for the terminal multiplexer is available, and any
			OSS releases along the way.