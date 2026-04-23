---
title: Introducing Parallel Agents in Zed — Zed's Blog
url: https://zed.dev/blog/parallel-agents
site_name: hackernews_api
content_file: hackernews_api-introducing-parallel-agents-in-zed-zeds-blog
fetched_at: '2026-04-23T11:59:21.007092'
original_url: https://zed.dev/blog/parallel-agents
author: ajeetdsouza
date: '2026-04-22'
published_date: 04/22/2026
description: 'From the Zed Blog: Run multiple agents at once, in the same window.'
tags:
- hackernews
- trending
---

Zed now lets you orchestratemultiple agents, each running in parallel in the same window. The new Threads Sidebar lets you control exactly which folders and repositories agents can access, and lets you monitor threads as they run.

All of this runs at Zed's famouslybuttery-smooth 120 fps, withwhichever agents you like, and it'sall open-source.

Threads Sidebar and full-screen Agent Panel.

## Many Threads, One Window

The Threads Sidebar offers an overview of all your threads at a glance, grouped by project, so you can:

* Mix and match agents on a per-thread basis, since Zed lets youchoose your agent.
* Work across projects, with one agent thread reading and writing across repos.
* Isolate worktrees, when you want to, and decide per thread.

An overview of the Threads Sidebar.

The Sidebar gives you instant access to common operations like stopping threads, archiving them, and kicking off new ones.
Even as your workflow grows in complexity, with several projects running multiple agents at once, the Sidebar makes it easy to stay organized as your agents work.

## A New Default Layout

As the Threads Sidebar became our primary way of navigating a project, we reconsidered which panels should sit where.
Threads now dock on the left by default, next to the Agent Panel, with the Project Panel and Git Panel on the right.

The new default layout in Zed.

We think this layout works better for agentic work, keeping agent threads front and center as you move between them. If you prefer a different arrangement, right-click any panel icon in the bottom bar to change its docking position, or adjust it inthe Settings Editor.
For existing users, the new layout is opt-in.

Customizing panels in Zed.

If you were used to the old layout, we encourage you to give this one a try before switching back.
It feels more natural once you've spent a little time with it.

## Agent and Editor: Better Together

Ask ten different programmers how they use AI, and you can get ten different answers.
At one extreme, there'sfully giving into the vibes, and at the other extreme, there'sdisabling all AI features.
What we've found works best for crafting high-quality software is somewhere in between: using AI, and also engaging directly with code.

As our co-founder and CEO Nathan Sobo wrote in 2025, "As software engineers, we should measure our contribution not in lines of code generated, but in reliable, well-designed systems that are easy to change and a pleasure to use."
That postintroduced the termagentic engineeringto describe the art of "combining human craftsmanship with AI tools to build better software," and we've recently seen the termgrow in popularity.

Parallel agents in Zed are built around that principle. Multi-agent orchestration isn't new, but we believe we've built a great experience for working with agents at scale. We spent days loading the system with hundreds of threads, refining rough edges and polishing corners that developers may never see. We went throughseveralUX iterations and had countless hours of internal discussions. It took us longer, and we won't lie, it drove us a little crazy. But the result feels better for it, and it lets developers do more challenging things with agents, without sacrificing their craft.

## Get Started

Parallel Agents is available in the latest Zed release.
You candownload Zed, or update to the latest version to get it.

You can open the Threads Sidebar from the icon in the bottom left, or via the keybindingoption-cmd-jon macOS andctrl-option-jon Linux and Windows.
We hope you enjoy this new level of control!

### Related Posts

Check out similar blogs from the Zed team.

## Building a platform that open sources itself

Jun 14, 2023

## Split Diffs are Here

Feb 18, 2026

## Run Your Project in a Dev Container, in Zed

|
Guest
|

Jan 07, 2026

### Looking for a better editor?

You can try Zed today on macOS, Windows, or Linux.Download now!

### We are hiring!

If you're passionate about the topics we cover on our blog, please considerjoining our teamto help us ship the future of software development.