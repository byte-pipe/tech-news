---
title: WTF Ubuntu?
url: https://chalmovsky.com/posts/wtf-ubuntu
site_name: hackernews_api
content_file: hackernews_api-wtf-ubuntu
fetched_at: '2026-11-03T06:07:27.818645'
original_url: https://chalmovsky.com/posts/wtf-ubuntu
author: chalmovsky
date: '2026-11-03'
description: WTF Ubuntu?
tags:
- hackernews
- trending
---

# WTF Ubuntu?

2026-11-02

What the fuck, Ubuntu?

In case you missed it:CVE-2026-98432is a critical (CVSS 9.8)
bug in the Linux kernel's TCP code. It's been there since 2016, so virtually every Linux server on the planet
has it, and it can be hit remotely. Anthropic says it built a working exploit that gets root on a server.
A total takeover.

Debianpatched it on October 16.
Ubuntu still doesn't have a patch more than two weeks later.
Every supported release, LTS included, is listed as "Vulnerable".

Ubuntu's website promises"timely patches for critical vulnerabilities."Ubuntu hasn't shipped the patch nine days after it was rated 9.8 and six days after a working root exploit.
Very fucking timely indeed.

Software is full of this blabber where words mean nothing. Ubuntu uses words like these:
"Timely." "Enterprise-grade." "Production grade." "Enterprise resilience. Developer velocity. Build with confidence on Ubuntu."

Somebody, or perhaps worse, some special team at Canonical is dedicated to writing these........

So I'm asking again... What the fuck, Ubuntu?

I'm moving all my servers off Ubuntu. I've completely lost trust in it.
On the desktop I always hated it anyway. On servers I mostly used it because it's the default
on most VPS providers, and I considered it the solid, no-drama LTS distro. Fuck that now.

I can't express how crazy this is. I didn't have time to migrate my services and data when I learned
about this, so I had to take all my servers that run Ubuntu offline.

Oh and btw, distros run by volunteers (Debian, Arch, Alpine...) hve shipped the fix. Meanwhile Ubuntu,
made by a company that sells security subscriptions, hasn't. This is true as of 2026-11-02 14:48 UTC.