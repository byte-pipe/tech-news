---
title: 'pyx: a Python-native package registry, now in Beta'
url: https://astral.sh/blog/introducing-pyx
site_name: hackernews_api
fetched_at: '2025-08-14T22:01:59.800133'
original_url: https://astral.sh/blog/introducing-pyx
author: the_mitsuhiko
date: '2025-08-14'
description: pyx is a Python-native package registry from the creators of uv.
tags:
- hackernews
- trending
---

Back to blog

August
 13,
 2025

# pyx: a Python-native package registry, now in Beta

##### Charlie Marsh

@
charliermarsh

TL;DR:pyxis a Python-native package registry — and the first piece of the Astral
platform, our next-generation infrastructure for the Python ecosystem.

We think ofpyxas an optimized backend foruv: it’s a
package registry, but it also solves problems that go beyond the scope of a traditional "package
registry”, making your Python experience faster, more secure, and even GPU-aware, both for private
packages and public sources (like PyPI and the PyTorch index).

pyxis live with our early partners, includingRamp,Intercom, andfal. If you're interested in a
next-generation Python experience for your team:get in touch today.

Sign up
Join the waitlist

At Astral, we build high-performance developer tools for the Python ecosystem. We're best known forRuff, our linter and formatter, anduv, our package manager.

I started this company because Python felt under-served: the most popular programming ecosystem on
Earth was succeedingin spiteof its tooling.

Over the past two years, Python's growth has only accelerated — and in parallel, our tools have seen
unprecedented adoption, with over 100 million installs per month across the Astral toolchain and uv
powering over 500 million requestsper day. The amount of Python code in the world is increasing
at an astounding rate, and our tools are powering those workloads.

Our goal is to make Python the most productive programming ecosystem on Earth, and our open source
tools have been driven by that unifying vision. But there are limits to what we can do with
client-side tools alone. We want to expand the scope of problems we can solve — beyond command-line
tools and into our own end-to-end infrastructure. We want to build a Python cloud: a set of unified
services that make Python fast, easy, and robust, extending the work and principles we've built upon
in our open source toolchain.

We're starting withpyx, a Python-native package registry. It's the first piece ofthe Astral
platform: our next-generation infrastructure for the Python ecosystem.

We think ofpyxas an optimized backend foruv: it's a
package registry, but it also solves problems that go beyond the scope of a traditional "package
registry," making youruvexperience faster, more secure, and
even GPU-aware. You can use it to host your own internal packages, or as an accelerated,
configurable frontend to public sources like PyPI and the PyTorch index.

When used withuv,pyxshould feel like the same leap in
developer experience that you felt when migrating touvin the
first place.

Much of the inspiration forpyxcomes from the classes of problems we see in theuvissue tracker (and in conversations with enterprises) that we
can't solve with a client alone — but could solve with a server. For example:

* "Why is it so hard to install PyTorch, or CUDA, or libraries like FlashAttention or DeepSpeed that
build against PyTorch and CUDA?"
* "Why is everyone on my team re-building the same packages over and over again on their machines?"
* "Why did the latest setuptools release break our build? Can't we harden against that?"
* "Why is it such a pain to authenticate against our internal registry?"

By vertically integrating our client (uv) and server
(pyx), we can solve these problems — all of them. And by tapping into the rest of our open
source toolchain, we can get even more ambitious over time. Imagine a package registry that has a
semantic, type-level understanding, not only of your own code, but of your dependencies and
supply-chain too; then extend that line of thinking to the rest of your Python infrastructure.

You won't need to usepyxto useuv, and you won't need
to useuvto usepyx. But when used together, entire
classes of problems disappear. Our deep focus on and understanding of Python enables us to build
better solutions than anything else out there; and deep integration with our open source tools
enables us to build experiences that otherwise wouldn't be possible at all.

Beyond the product itself,pyxis also an instantiation of our strategy:our tools (uv,
Ruff, ty, etc.) remain free, open source, and permissively licensed — forever.Nothing changes
there. Instead, we'll offer paid, hosted services likepyxthat represent the "natural next
thing you need" when you're already using our tools: the Astral platform.

pyxis not yet generally available. We've been building it out over the past few months, and
are now live with our early partners, includingRamp,Intercom, andfal. As much as we can, though, we
want to build in the open. The fast feedback loops that we get from building in open source are a
huge part of our ability to solve real user problems.

As we harden the product and prepare for GA, we'd love to hear from you. If you're interested in a
next-generation Python experience for your team — if the problems above resonate with you, or even
if you're just a fan of our work:get in touch today.

Sign up
Join the waitlist
