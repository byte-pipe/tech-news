---
title: Dumb Pipe
url: https://www.dumbpipe.dev/
site_name: hackernews_api
fetched_at: '2025-07-29T01:06:13.938908'
original_url: https://www.dumbpipe.dev/
author: udev4096
date: '2025-07-28'
description: 'Iroh connections are dumb pipes: easy, direct connections that punch through NATs & stay connected as network conditions change.'
tags:
- hackernews
- trending
---

## Connect A to B. Send Data.

In 2023 it's hard to connect two devices directly. Dumb pipe punches through NATs, using on-the-fly node identifiers. It even keeps your machines connected as network conditions change.

What you actuallydowith that connection is up to you.

## A unix pipe between computers

$ curl -sL https://www.dumbpipe.dev/install.sh | sh

getdumbpipewith a single command on two computers, connect them & pipe data from one machine to the other. No accounts. No configuration.

## Receiver

$ ./dumbpipe listen

using secret key 23ryys7pgvjrr57pcrvyivdrhvqyykg2tv3leou5grm66xfd7zzq

Listening. To connect, use:

./dumbpipe connect nodeecsxraxjtqtneathgplh6d5nb2rsnxpfulmkec2rvhwv3hh6m4rdgaibamaeqwjaegplgayaycueiom6wmbqcjqaibavg5hiaaaaaaaaaaabaau7wmbq



## Sender

echo

"hello"
 | ./dumbpipe connect nodeecsxraxjtqtneathgplh6d5nb2rsnxpfulmkec2rvhwv3hh6m4rdgaibamaeqwjaegplgayaycueiom6wmbqcjqaibavg5hiaaaaaaaaaaabaau7wmbq



This will work, regardless of where the two machines are. Dumb pipe finds a way.

## Put a dumb pipe in your app

Dumb pipes are Iroh Connections. Thedumbpipetool is a200-line wrapperaround theirohrust crate. You can use the iroh Endpoint to create a connection to use as a dumb pipe in your own app.

Iroh Endpoint Docs


## QUIC & Dumb

These dumb pipes use QUIC over a magic socket. It may be dumb, but it still has all the features of a full QUIC connection: UDP-based, stream-multiplexing and encrypted. Besides using the multiplexed streams you can also use multiple connections each with their own ALPN.

## Sometimes you gotta relay

For somewhere around 10-20% of connections, it's simply not possible to connect two devices directly. For those cases, we use a meshed network of relay nodes to pack up UDP traffic & send it over HTTP. Sounds silly, but it works. And the magic socket handles all this under the hood.

relay docs


## Your own Network

The team behind number0 runs the default relay network, which has a capped bandwidth. High-throughput, authenticated relays are now available throughn0des!

## Need more?

Need pubsub? Data transfer? Sync? All of these are opt-in addons fromiroh. But if you add these things, the pipe is no longer dumb. You decide how to feel about that.
