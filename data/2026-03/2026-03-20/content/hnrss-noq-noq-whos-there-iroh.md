---
title: noq, noq, who's there? - Iroh
url: https://www.iroh.computer/blog/noq-announcement
site_name: hnrss
content_file: hnrss-noq-noq-whos-there-iroh
fetched_at: '2026-03-20T11:14:55.123348'
original_url: https://www.iroh.computer/blog/noq-announcement
date: '2026-03-19'
description: 'Introducing noq: n0''s QUIC implementation'
tags:
- hackernews
- hnrss
---

Today we're delighted to announcenoq(”number 0 QUIC”),
our own general purpose QUIC implementation with multipath and NAT traversal support.
It is the transport layer that has been powering iroh since v0.96,
though is in no way limited to iroh's usecase.

# From soft fork to hard fork

If you've been following iroh's development,
you may have readwhy we forked Quinnback in 2024.
The short version: iroh was doing a lot of heavy liftingaroundQUIC:
switching between relay and direct paths, managing NAT traversal, juggling congestion state.
But QUIC itself had no visibility into any of it.
That mismatch created problems that we couldn't fix from the outside.

Our fork started small.
We wanted to track upstream Quinn closely, contribute back where we could, and keep our diff minimal.
That was the right call at the time.
But as we pushed further into QUIC multipath, NAT traversal, and our own relay-as-a-path architecture,
the development velocity of the two projects drifted into iteration cycles that didn't match.
All our constant changed would lead to an unreasonable review burden for the Quinn maintainers.
The n0 team wanted to try deeper, structural changes to our QUIC implementation,
and it would have been unfair to foist the consequences of those changes onto all Quinn users.
We think a hard fork with a continued commitment to collaboration makes more sense all around.

So we went all the way.
We explained our thinkingin the Quinn multipath issue thread.
This isn't a rejection of Quinn, which remains a great implementation.
It's an acknowledgment that the problems we're solving are specific enough that a separate codebase,
with collaboration where our interests overlap,
is the honest path forward.

# What's in noq

## QUIC Multipath

The headline feature is a full implementation of theQUIC Multipath spec.
This is where the real architectural shift happened,
both inside Quinn/noq and for iroh's use.
Before multipath, iroh managed multiple paths (relay, direct IPv4, direct IPv6) as a kind of sleight of hand below the QUIC layer.
Quinn thought it was talking to the other endpoint via just one IP address while we shuffled packets across whichever path was working best.
Kind of like iroh's own small NAT around Quinn.

With multipath, those paths are first-class QUIC concepts.
The relay path is a QUIC path.
The direct UDP path is a QUIC path.
QUIC knows about all of them, maintains per-path congestion state,
and can reason about which one to use.
This means the latency improvements we had to hack in via congestion controller resets are now handled correctly and systematically.

The multipath implementation is generic though,
it does not only serve iroh.
It aims at being a full implementation of theQUIC Multipath spec,
for any purpose.
The implementation is still young however,
so if you need more APIs from it, let us know.

## QUIC NAT Traversal

We've implemented our own interpretation of theQUIC NAT traversal draft.
To our knowledge we're the first to do this in a production-grade, robust way.
NAT traversal is notoriously finicky,
getting it right across the full range of NAT behaviors in the wild is a hard problem,
and we've been battle-testing our approach across the hundreds of thousands of devices already running iroh.
Though this is in no way a settled spec yet, we will keep iterating.

Expressing NAT traversal hole-punching directly as a QUIC-level operation,
rather than something happening beneath it,
is cleaner and more reliable,
because it makes the QUIC congestion controller aware of it and allows better loss detection.

## QUIC Address Discovery

iroh has been using our implementation ofQUIC Address Discovery(QAD) since iroh version 0.32.
QAD uses QUIC connections to learn about public IP addresses of clients,
which was previously done using STUN.
QUIC enables encrypting these packets without sacrificing round-trips compared to STUN,
preventing protocol ossification and enhancing user privacy.

## More QLog

Qlog is a draft standard to log an awful lot of information about QUIC connections.
It is a great debugging tool, there are visualisation tools likeqvisthat can show the flow of packets between two peers.

In noq the qlog support has been greatly extended to support many more events from themain qlog logging schemaand [QUIC event definittions].
Additionally qlog's extensability was used to add events for QUIC multipath.
We even have aviewer prototypethat can show the packet flows across multiple paths.

## WeakConnectionHandle

While most of noq's API changes are around the multipath support we also added aWeakConnectionHandle.
This is a type that does not keep a connection alive itself,
but can be upgraded to a fullConnectionif it was not dropped yet.
It behaves much like [std::sync::Weak] but without having toArcit as that is not always so easy to do.

This can be helpful to build things like connection managers.
We have needed this for ourselves internally in iroh,
there for sure are more good usecases.

# Already in production

noq shipped as part of iroh v0.96 and has been running in production since then.
If you're using a recent version of iroh, you're already using noq.

Apart from shipping and testing noq's multipath implementation against itself,
we've also been running interoperability tests against picoquic,
one of the reference implementations used in QUIC working group interop events.

# What's next

We see noq as a long-term foundation.
There is more work that we want to do such as further NAT traversal improvements.
The multipath work also opens up performance optimizations that weren't possible before.
We'll continue to engage with the QUIC working group and collaborate with the Quinn team on areas where our interests align.

If you're working on QUIC implementations, p2p transport, or applications that need to run across diverse network conditions, we'd love to talk.
Come find us onDiscordor open an issue onGitHub.

If you're eager to try out a rust QUIC multipath implementation,
take a look at the documentation for amultipath noq Connection.

Iroh is a dial-any-device networking library that just works. Compose from an ecosystem of ready-made protocols to get the features you need, or go fully custom on a clean abstraction over dumb pipes. Iroh is open source, and already running in production on hundreds of thousands of devices.
To get started, take a look at our 
docs
, dive directly into 
the code
, or chat with us in our 
discord channel
.