---
title: Be Wary of Bluesky
url: https://kevinak.se/blog/be-wary-of-bluesky
site_name: hackernews_api
content_file: hackernews_api-be-wary-of-bluesky
fetched_at: '2026-02-22T11:08:20.583416'
original_url: https://kevinak.se/blog/be-wary-of-bluesky
author: kevinak
date: '2026-02-20'
description: Bluesky promises decentralization, but nearly every user's data sits on Bluesky's servers, and every new ATProto app reinforces that centralization. T
tags:
- hackernews
- trending
---

In 2023, Bluesky's CTO Paul Frazee was asked what would happen if Bluesky ever turned against its users. His answer:

"it would look something like this: bluesky has gone evil. there's a new alternative called freesky that people are rushing to. I'm switching to freesky"

That's the same argument people made about Twitter."If it goes bad, we'll just leave." We know how that played out.

## The promise

Bluesky is built on ATProto, an open protocol. The pitch is simple: your data is yours, your identity is yours, and if you don't like what Bluesky is doing, you can take everything and leave. Apps like Tangled (git hosting), Grain (photos), and Leaflet (publishing) all plug into the same protocol. One account, many apps, no lock-in.

It sounds great. But look closer.

## Where your data actually lives

When you use any ATProto app, it writes data to your Personal Data Server, or PDS. Your Bluesky posts, your Tangled issues, your Leaflet publications, your Grain photos. All of it goes to the same place.

For almost every user, that place is a server run by Bluesky.

You can self-host a PDS. Almost nobody does. Why would they? Bluesky's PDS works out of the box with every app, zero setup, zero maintenance. Self-hosting means running a server, keeping it online, and gaining nothing in return.

To be fair, migration tools exist. You can move your account to a self-hosted PDS for as little as $5 a month. Bluesky has made this easier over time and even supports moving back. But this only works if you do it before the door closes. If an acquirer disables exports, it doesn't matter that the tools existed yesterday. And we know from every platform transition in history that almost nobody takes proactive steps to protect their data.

## The flywheel

Here's the part that worries me.

Every new ATProto app makes this problem worse, not better. Each app tells you "sign in with your Bluesky account", which really means "write more data to Bluesky's servers." The more apps that launch, the more users depend on Bluesky's infrastructure, the less reason anyone has to leave.

The protocol doesn't distribute value across the network. It concentrates it.Developers are building features on top of Bluesky's infrastructure for free, making it more indispensable with every app that ships.

And Bluesky gets to claim the moral high ground the whole time. "We're open! We're decentralized! You can leave whenever you want!" Meanwhile, the switching cost goes up every day.

## The chokepoints

It's not just the PDS. Bluesky controls almost every critical layer:

The Relay.All data flows through it. Bluesky runs the dominant one. Whoever controls the relay controls what gets seen, hidden, or deprioritized. Third parties can run their own, but without the users, it doesn't matter.

The AppView.This is what assembles your timeline, threads, and notifications. Bluesky runs the main one. If it goes down or goes hostile, every client that depends on it breaks.

The DID Directory.Your identity on ATProto resolves through a centralized directory run by Bluesky. They've called it a "placeholder" since 2023 and said they plan to decentralize it. There's still no timeline.

At every layer, the answer is "anyone can run their own." At every layer, almost nobody does.

## The Gmail problem

Email is an open, federated protocol. Anyone can run a mail server. In practice, running your own mail server is painful and everyone just uses Gmail. The protocol being "open" didn't prevent centralization.

ATProto might be worse. With email, at least each app connects to your own server. With ATProto, each new app adds more data to the same centralized PDS. The open protocol is actually a centralization flywheel.

## What happens in an acquisition

Say someone buys Bluesky. They now control:

* The PDS for nearly every user
* The main relay
* The main AppView
* The DID directory that resolves every identity

They could disable data export. They could cut off third-party apps. They could shut down federation. They could insert ads, shadow ban users, deprioritize content.

And the blast radius isn't just Bluesky the social network. It's every app in the ecosystem. Your git issues on Tangled, your posts on Leaflet, your photos on Grain. All stored on infrastructure now controlled by the acquirer.

The protocol says you can leave. But the company that just paid billions for the network has no incentive to let you.

I like Bluesky. I use Bluesky. The team seems to genuinely care.

But every counter-argument to the concerns above rests on the same foundation: technically, users can leave. Technically, you can self-host. Technically, you can run your own relay. The capability exists at every layer. But people don't do these things. They never have with any protocol. Not email, not RSS, not XMPP.The default wins. Always.

And then there's the money. You don't raise $120M at a $700M valuation to run a public utility. Those investors need a return. That return comes from monetizing users, getting acquired, or going public. All three create pressure to consolidate control, not distribute it. A truly decentralized network where users can freely leave is worth less to an acquirer than one where they can't.

The PBC structure is supposed to be the safeguard. But PBC obligations are vague and untested in court. When $120M in VC money is on one side of the balance, guess which way it tips.

The protocol can't save you from incentives.
