---
title: 'Introducing the first alpha of Turso: The next evolution of SQLite'
url: https://turso.tech/blog/turso-the-next-evolution-of-sqlite?ref=console.dev
site_name: lobsters
fetched_at: '2025-07-04T23:06:36.968780'
original_url: https://turso.tech/blog/turso-the-next-evolution-of-sqlite?ref=console.dev
date: '2025-07-04'
description: We’re launching the first alpha of Turso. A Rust-based, cloud-native rewrite of SQLite with modern concurrency, async APIs, vector search, and unmatched reliability powered by advanced testing and open-source collaboration.
tags: rust
---

Jul 1, 2025

# Introducing the first alpha of Turso: The next evolution of SQLite

Glauber Costa

Almost six months ago, we announced a bold project: we were going to invest in afull rewrite of SQLitefrom scratch. Codenamed "Project Limbo", it quickly amassed palpable interest, and a community of contributors.

Today, we reached the point where we are confident enough in its quality that we are ready for the first alpha release.

Now officially named "Turso" — the next evolution of SQLite.

We've built Turso using advanced testing techniques, both our own and through our partnership with Antithesis, an autonomous testing platform. This approach will allow us to match SQLite's legendary reliability. We're so confident in our methodology that we'll pay you $1,000 if you find a data corruption bug that our testing missed.

## #Why rewrite SQLite?

We believe SQLite is the best piece of software on the planet. It is fast, reliable, and it fits everywhere. But modern applications require access patterns that SQLite often can’t handle. After more than a year operating a cloud service based on SQLite, those are the common complaints we hear:

* SQLite cannot handle concurrent writes. This not only limits the throughput of SQLite for use cases like data collection and logging, but also makes writing to SQLite unreliable, since concurrent writes can fail even at low throughput, leading to a bad experience.
* Writing realtime applications that react to data changes is a challenge with SQLite, since there is no good support for capturing a stream of changes.
* SQLite has limited support for non-relational data, such as vector embeddings and timeseries.
* SQLite exposes a synchronous API, which makes it harder for it to work well on some environments, like the browser.
* Evolving the schema of applications with SQLite is a challenge.

The rise of AI saw SQLite taking center stage. SQLite was already the top choice for physical systems like robots and cars. But we now see people reaching out for it for agentic memory, AI builders, and many other applications.

Ultimately, from a purely technical position, SQLite itself can evolve to provide all the features it needs to adapt to our new landscape. However, the closed nature of its community - SQLite doesn’t accept contributions from anybody, makes changes unacceptably slow for today’s fast-paced development environment.

Since it was publicly announced six months ago, Turso now has more than 115 contributors. So we can confidently say: the most important feature we’re adding to our project is you: Turso gives you a seat at the table, and leverages the true power of Open Source.

If you are interested in shaping what the next generation of SQLite can be, our community is open and waiting!

## #SQLite is the most reliable software on the planet.

We know. That’s why we like it so much! Ever since we started talking about rewriting SQLite, we hear the same opposition: SQLite is well known for its out-of-this-world reliability. Why would you rewrite it? The hidden assumption is that a rewrite will necessarily be less reliable than SQLite.

We understand where this comes from: SQLite's legendary reliability comes from decades of testing and battle-hardening. But we're not just matching that standard — we're surpassing it using modern techniques that weren't available when SQLite was built.

From day one, Turso usesDeterministic Simulation Testing (DST)— the same approach that made databases like FoundationDB and TigerBeetle incredibly robust. DST systematically explores thousands of failure scenarios and edge cases, verifying that critical system properties hold under every condition. Unlike traditional testing, DST doesn't just test what you think might break - it discovers failure modes you never considered.

We've also partnered withAntithesis, an autonomous testing platform that runs our code in a deterministic hypervisor, injecting faults while continuously verifying system properties. This catches bugs that even our own simulator might miss, including bugs in the simulator itself.

The result? We can systematically test Turso against complex failure scenarios and edge cases that would be nearly impossible to reproduce with traditional testing methods, giving us a level of confidence and reliability that a rewrite of SQLite demands. We're so confident in this approach that we're putting our money where our mouth is: find a data corruption bug that our testing missed, show us how to improve our simulator to catch it, andwe'll pay you $1,000through our partnership with Algora.

This is just the beginning. As we expand beyond alpha, both the scope and rewards will grow significantly.

## #What to expect from this Alpha?

This alpha includes support for the basic features of SQLite, and introducesTurso's key differentiators: an asynchronous interface that replaces SQLite's synchronous API, and native vector search capabilities. On Linux, there is work-in-progress support forio_uringfor high-performance async operations. The async interface makes Turso work seamlessly in environments where blocking isn't possible, like browsers, while vector search enables AI and ML applications without external dependencies.

What works: Core database operations (SELECT, INSERT, DELETE, UPDATE, ALTER TABLE, JOIN, transactions), most SQLite functions including JSON support, andnative vector searchported from Turso Cloud for AI and ML workloads.

What's still in development: Indexes, multi-threading, savepoints, triggers, views, and VACUUM operations.

The complete feature status is trackedhereand updated as development progresses.

Our focus for this alpha has been building the rock-solid testing foundation that will sustain Turso for decades to come, ensuring every feature we ship meets our reliability standards.

Yet, despite how early it is, Turso is already starting to find its way into existing projects, as a replacement for SQLite. One example isSpice.ai, a data and AI inference engine which uses local databases like SQLite and DuckDB as accelerators in their product.

The performance of the underlying accelerator is key to a great experience, and in some queries, they already see better performance with Turso versus their SQLite implementation, and expect even more performance gains to be unlocked once Turso implements concurrent writes.

Turso’s Rust-based rewrite of SQLite brings cloud-native, concurrent performance to AI apps and agents. As workloads shift to fast, lightweight databases like SQLite and DuckDB, Turso takes SQLite beyond its concurrency limits, strengthening the ecosystem for scalable, data-driven apps. — Luke Kim, Founder and CEO of Spice AI

If you are working with applications that would benefit from concurrent writes, or any other functionality that you feel SQLite is missing,join us on Discord.

We still have open slots for design partners.

## #Thanks to our partners

Our alpha milestone was stability and reliability. We have achieved this milestone in months. That is because aside from our own native simulator, we partner with Antithesis, an autonomous testing platform. Whatever bug our simulator doesn’t catch, including bugs in the simulator itself, is usually caught by Antithesis.

Antithesis provides a deterministic hypervisor that injects faults into the system while verifying that the system properties hold. Because of them, we could flesh out bugs and get to the confidence level required to announce this release much sooner than we would otherwise.

Constantly running all that testing infrastructure is also prohibitively expensive with Github Actions. Thankfully, through our partnership with Blacksmith, this is one concern we don’t have. A high-performance CI infrastructure allows us to catch issues faster and keep the quality of our offering at all times.

Finally, we are ready to pay anyone $1,000 for bugs that lead to data corruption (and a higher dollar amount and scope in the future). While we are confident in the level of quality we have achieved, some bugs will invariably be there, lurking in the nastiest corner cases, especially in the beginning. Paying people compliantly in whichever country they are is a challenge, and we are thankful forAlgora'ssupport on this.

Sharearticle

Twitter / X
Hacker News
Email
LinkedIn
Copy link
