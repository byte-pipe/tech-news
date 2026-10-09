---
title: Deno is joining Cloudflare | Deno
url: https://deno.com/blog/cloudflare
site_name: hackernews_api
content_file: hackernews_api-deno-is-joining-cloudflare-deno
fetched_at: '2026-10-09T17:19:17.048956'
original_url: https://deno.com/blog/cloudflare
author: ilreb
date: '2026-10-09'
description: Putting ourselves in the best place to build the future of the web
tags:
- hackernews
- trending
---

# Deno is joining Cloudflare

October 9, 2026

* Ryan Dahl
* Announcements
* Product Update

For years, we’ve been working to make building server software simpler. We
questioned how modules could be distributed, what security guarantees a
JavaScript runtime could provide, what belonged in a complete toolchain, and how
easily an application could be distributed as a standalone executable.
Compatibility with Node.js became an important part of that work too: our users
wanted the Deno improvements while continuing to plug into the existing JS
ecosystem. The team and community built a runtime that brought these
capabilities together and challenged assumptions about what JS development could
look like.

Today we’re announcing that the entire Deno team is joiningCloudflareto take that work further.

Our ambition has always extended beyond the runtime. I wrote about this in myJavaScript Containersblog
post: compute, storage, and communication working together, without every
application assembling its own infrastructure.

WithDeno Deploy, we took another step towards that
goal. We wanted to make running applications as straightforward as possible. But
building and operating Deploy also showed us how much complexity remained
underneath that developer experience. I wanted to simplify that layer, too.

This led tocelld. Building on theCloudflare Workersprogramming
model, celld lets developers build distributed applications from the start while
making the system simple to operate. What excites me greatly is that the scaling
is built into the programming model, rather than infrastructure each app has to
assemble itself.

The progression from Deno to Deno Deploy to celld explains why this move makes
sense to us. At Cloudflare we’ll combine our work with that of the Workers andDurable Objectsteams. We
want to make this programming model the default way to build servers, whether
you run on Cloudflare’s network or your own infrastructure.

Joining also means choosing where to focus our effort. We’ve decided to put our
future development work into this shared platform rather than continuing to
develop a separate runtime and hosting service. We know this is a consequential
change for people who have built on Deno.

To everyone who contributed code, built businesses on Deno, reported problems,
and trusted our direction: thank you. Here’s what this means concretely:

* We will support theDeno runtimefor
another year with monthly releases containing bug fixes and security updates.
After that year we will end our development of the Deno runtime. Deno will
remain open source, and we welcome others who want to continue its
development.
* Deno Deploy will continue operating for six months before shutting down. We
will provide migration support for paying customers moving to Cloudflare
Workers.
* JSRwill continue operating, with its infrastructure moving
to Cloudflare.
* We will continue supportingrusty_v8and work toward integrating it intoworkerd.

The need for better abstractions is especially acute with AI. Durable Objects
bring together capabilities that are particularly useful for agent harnesses:
inexpensive, serverless execution, persistent state, WebSockets, and a
high-level JavaScript interface. This is what I’m most excited to explore and
why celld focuses on Durable Objects.

Kenton Varda and I explain more in ourjoint post on the Cloudflare blog.
If you’re building agents at scale and want to run them on your own
infrastructure, please reach me now atry@cloudflare.com.