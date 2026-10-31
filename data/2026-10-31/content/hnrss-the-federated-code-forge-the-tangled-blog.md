---
title: The federated code forge · The Tangled Blog
url: https://tangled.org/blog/forge/
site_name: hnrss
content_file: hnrss-the-federated-code-forge-the-tangled-blog
fetched_at: '2026-10-31T19:03:47.302029'
original_url: https://tangled.org/blog/forge/
date: '2026-10-30'
published_date: '2026-10-30T00:00:00.000Z'
tags:
- hackernews
- hnrss
---

For most of the past two decades, the code forge has been where projects live:
where code is hosted, where changes are reviewed, and where contributors find
each other. Forges offered convenience in exchange for centralisation.

But the centralised forge is crumbling. Relying on someone else for uptime, for
features, and to be a good steward of your code hasn’t played out well. Whathasstood the test of time is email: Git to move the code, and email — an
open protocol — to talk about it. At the cost of user experience, however.

1. ’05Mail+Git
2. ’09GitHub+Git
3. ’25AT Protocol+Git

Tangled aims to give you the best of both: the longevity of an open
protocol, with the convenience and polish of a proper forge.

It’s the first truly federated code forge — you can host code on your own
servers and still collaborate seamlessly with others. Our approach is
pragmatic: self-host just the parts you want, like Git hosting or CI runners,
or all of it, including the API server and UI. Whateveryou
choose, you can still talk to everyone
else.

Owning your infrastructure also means you can hack on, extend
and customise your forge as you see fit. Because Tangled is
built on the AT Protocol, you can build your own extensions,
subscribe to the firehose, or even write entirely custom knots,
likethis onethat runs on
Cloudflare Workers and uses their Artifacts product for git
storage. Or an entirely custom spindle such asmitchellh.com/tack. Go
even further and host ourultralight API
serverand build
your own custom forge.

Agents have made building such hyper-personalized software trivial, and
especially so when software is designed with hackability in mind from the
get-go. Tangled is incrediblyagentfriendly.

The future of software engineering may be a moving target, but our bets
on open protocols and developer agency give us the agility to move with
it, and to becomeyourcodeforgeforthenextdecade.

# Product updates

## A fresh look!

The obvious big one: with this release, Tangled has a whole new look.
We’ve redone the UI on top of our new architecture (described further
below), in Svelte. Things should now be quicker, visually consistent and
prettier! The keen eyed of you might’ve also spotted that we’ve swapped
out Inter forTimeless Sans.

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

## A bobbin near you

Until now, Tangled’s web UI and backend were a single Go monolith called theappview. The appview service handled AT Protocol indexing, caching,
off-protocol data and UI rendering usinghtml/template+ htmx. It ran on a
single SQLite database on one medium-sized server in Sweden.

This was great as long as you were ~50–100 ms away from Sweden, but most
of our users aren’t! We rearchitected: we built a new standalone
frontend app in Svelte, deployed at the edge. It is populated by our new
diskless, entirely in-memory indexer service written in Rust:bobbin.
Bobbins are deployed globally in over 11+ regions, ensuring users around
the world get the best API and UI performance.

The astute reader might’ve noticed: bobbin is purely read-only and only
deals with AT Protocol data. What of the rest? That functionality (and
more) has been delegated to a new set of supporting services.

## The new data model and repo-owned data

First, the data model itself: we have a new set of lexicons, and everything now
lives underorg.tangled.*, replacing the oldsh.tangled.*records.

Knot2 is our aptly named, second implementation of the knot server, this time
rewritten in Rust. Knot2 bakes a fully custom Git server, and also bundles in
an SSH server in the same binary.

With knot2, we’ve also changed where some of that data lives. Issues, pull
requests, comments, reactions and labels are now stored on the knot, right next
to the code, as collaborative objects (COBs). A COB is just a chain of Git
objects in the repo itself. Collaborators, knot members and the blocklist are
also stored the same way.

In that sense, knots now behave a lot like a PDS: they hold signed records,
full history included, for everything that belongs to a repo and much like a
PDS, these records are synced via the standard AT Protocol firehose.

But why? A project’s issues and pull requests are as much a part of it as its code,
so they should live with it, wherever you choose to host it. This gives your
project maximum portability.

If the knot writes your issues and comments, what stops it from putting words
in your mouth? Attestations. Every time you create or edit a record on a knot,
the web app also writes anorg.tangled.graph.attestationrecord to your own
PDS, pointing at that exact version of the record and the COB change behind it.
Two-way verification!

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

Self-hosters will have to upgrade their knots to the v1.20.0 byfollowing the
upgrade guide.

## Organizations

Organization accounts are here! An Organization on Tangled is a real AT
Protocol account, with its own DID and handle, hosted on aTranquil
PDSinstance. They’re
passwordless, delegated accounts: you create one from theNew
Organizationpage, and you get<name>.tngl.shwith yourself as its owner. Owners can invite members, and
anyone in the Organization can act as it when creating or forking repositories.
Like any other account, you can swap the handle out for a domain you own. If
you’ve been running a regular account as a stand-in “org”, hang tight — we’re
working on a way to move those over. Read more in thedocs.

 
 
 
 
 
 
 
 
 
 

## Stacked PRs for everyone

Our PR flow has been overhauled. The new flow gives everyone, regardless
of whether you use Jujutsu or just vanilla Git, the ability to submit
and review stacked PRs. If you’re using Git, you now get the ability to
interdiff between versions (previously called rounds). JJ users get to
interdiff between individual changes as well.

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

## Launch weeks ahead

This isn’t all. We’re staggering this launch across the next few weeks. Up next
are private repos, a CLI, SDKs for different languages and skills for your
agent.

Until then, enjoy every part of this launch equally.

 

Your code, your network.Come build with us on Tangled.

 
 
Sign up