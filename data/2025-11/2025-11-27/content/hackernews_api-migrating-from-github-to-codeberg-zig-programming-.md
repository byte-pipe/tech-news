---
title: Migrating from GitHub to Codeberg ⚡ Zig Programming Language
url: https://ziglang.org/news/migrating-from-github-to-codeberg/
site_name: hackernews_api
fetched_at: '2025-11-27T11:07:01.732505'
original_url: https://ziglang.org/news/migrating-from-github-to-codeberg/
author: todsacerdoti
date: '2025-11-27'
description: Migrating the main Zig repository from GitHub to Codeberg
tags:
- hackernews
- trending
---

← Back to

News

 page


# Migrating from GitHub to Codeberg

### November 26, 2025

https://codeberg.org/ziglang/zig

Ever sincegit initten years ago, Zig has been hosted on GitHub. Unfortunately, when itsold out to Microsoft, theclock started ticking. “Please just give me 5 years before everything goes to shit,” I thought to myself. And here we are, 7 years later, living on borrowed time.

Putting aside GitHub’srelationship with ICE, it’s abundantly clear that the talented folks who used to work on the product have moved on to bigger and better things, with the remaining rookies eager to inflict some kind of bloated, buggy JavaScript framework on us in the name of progress. Stuff that used to be snappy is now sluggish and often entirely broken.

More importantly, Actions iscreated by monkeysandcompletely neglected. After theCEO of GitHub said to “embrace AI or get out”, it seems the lackeys at Microsoft took the hint, because GitHub Actions started “vibe-scheduling”; choosing jobs to run seemingly at random. Combined with other bugs and inability to manually intervene, this causes our CI system to get so backed up that not even master branch commits get checked.

Rather than wasting donation money on more CI hardware to work around this crumbling infrastructure, we’ve opted to switch Git hosting providers instead.

As a bonus, we look forward to fewer violations (exhibitA,B,C) of ourstrict no LLM / no AI policy, which I believe are at least in part due to GitHub aggressively pushing the “file an issue with Copilot” feature in everyone’s face.

## GitHub Sponsors

The only concern we have in leaving GitHub behind has to do with GitHub Sponsors. This product was key to Zig’s early fundraising success, and itremains a large portion of our revenue today. I can’t thankDevon Zuegelenough. She appeared like an angel from heaven and single-handedly made GitHub into a viable source of income for thousands of developers. Under her leadership, the future of GitHub Sponsors looked bright, but sadly for us, she, too, moved on to bigger and better things. Since she left, that product as well has been neglected and is already starting to decline.

Although GitHub Sponsors is a large fraction of Zig Software Foundation’s donation income,we consider it a liability. We humbly ask if you, reader, are currently donating through GitHub Sponsors, that you considermoving your recurring donation to Every.org, which is itself a non-profit organization.

As part of this, we are sunsetting the GitHub Sponsors perks. These perks are things like getting your name onto the home page, and getting your name into the release notes, based on how much you donate monthly. We are working with the folks at Every.org so that we can offer the equivalent perks through that platform.

## Migration Plan

Effective immediately, I have madeziglang/zig on GitHubread-only, and the canonical origin/master branch of the main Zig project repository ishttps://codeberg.org/ziglang/zig.git.

Thank you to the Forgejo contributors who helped us with our issues switching to the platform, as well as the Codeberg folks who worked with us on the migration - in particularEarl Warren,Otto,Gusted, andMathieu Fenniak.

In the end, we opted for a simple strategy, sidestepping GitHub’s aggressive vendor lock-in: leave the existing issues open and unmigrated, but start counting issues at 30000 on Codeberg so that all issue numbers remain unambiguous. Let us please consider the GitHub issues that remain open as metaphorically “copy-on-write”.Please leave all your existing GitHub issues and pull requests alone. No need to move your stuff over to Codeberg unless you need to make edits, additional comments, or rebase.We’re still going to look at the already open pull requests and issues; don’t worry.

In this modern era of acquisitions, weak antitrust regulations, and platform capitalism leading to extreme concentrations of wealth, non-profits remain a bastion defending what remains of the commons.

Happy hacking,

Andrew
