---
title: Data loss in ttrpc-rust – Shiv's Page
url: https://shvbsle.in/data-loss-in-ttrpc-rust
site_name: tldr
content_file: tldr-data-loss-in-ttrpc-rust-shivs-page
fetched_at: '2026-10-04T15:40:47.602872'
original_url: https://shvbsle.in/data-loss-in-ttrpc-rust
date: '2026-10-04'
description: The interactive version of this post, with animations, is at notes.shvbsle.in/ttrpc-data-loss. Motivation Before the AI-accelerated programming age, it w...
tags:
- tldr
---

# Data loss in ttrpc-rust

04 Oct, 2026

The interactive version of this post, with animations, is atnotes.shvbsle.in/ttrpc-data-loss.

## Motivation

Before the AI-accelerated programming age, it was expected from a software stack that all of its stable components are written in one uniform language. In the case of containers, the ecosystem (containerd, shim, runc) was written in Golang. But in this new age, armed with LLMs, any new language can make lateral entry in this ecosystem and quickly build stable runtimes. I've been trying to introduce more Rust to this ecosystem.

One day I was watching logs from a pod that was running on a container runtime written in Rust and noticed that occasionally the log stream just abruptly ended. I deployed another pod that prints numbers from 1 to 100, and the logs sometimes abruptly ended on 99, but never on 97 or 98. I kept thinking that it was a bug in the runtime, but it turned out that the bug was hidden much deeper in the stack. It was in the implementation of the protocol1. This page contains my notes on the internals of ttrpc and ways in which this bug manifests.

## Overview of the ttrpc Protocol

* An RPC protocol that is simple, low-memory2and lightweight (small binary). It is meant for processes on the same host, not for calls across a network.
* Used mainly between container runtime components: containerd and its shims, and the Kata Containers runtime and its agent inside the VM.
* Unlike gRPC, it is NOT built on top of HTTP/2 (and has no TLS). It reuses gRPC's protobuf service definitions, but the two do not speak the same wire protocol.
* Uses a lightweight framing protocol: every message is a 10-byte header followed by a protobuf payload, and many calls share one connection as separate streams.
* No flow control3, pings or handshakes. Streams are opened and closed with two flags instead of control frames.

Interactive:step through real ttrpc frames byte by byte.

## Feel the Bug

* Needs tokio's multi-threaded runtime (rt-multi-thread).
* The client spawns one task per incoming frame, and the tasks run in no guaranteed order.
* The close frame (flags05) removes the stream ID from the client'sstreamsmap.
* If that happens before the last DATA frame's task runs, the payload is silently dropped.

Interactive:watch the race drop frame 100.

In code, it was this:

async
 
fn
 
handle_msg
(
&
self
,
 
msg
:
 
GenMessage
)
 
{

 
let
 
req_map
 
=
 
self
.
streams
.
clone
();

 
tokio
::
spawn
(
async
 
move
 
{

 
if
 
let
 
Some
(
resp_tx
)
 
=
 
get_resp_tx
(
req_map
,
 
&
msg
.
header
).
await
 
{

 
resp_tx

 
.
send
(
Ok
(
msg
))

 
.
await

 
.
unwrap_or_else
(
|
_e
|
 
error
!
(
"The request has returned"
));

 
}

 
});

}

src/asynchronous/client.rs @ f31f592·issue #311

## Naive Fix

Stop spawning: the reader task handles each frame itself, in the order it read them.

 
async fn handle_msg(&self, msg: GenMessage) {

+ // Do not `tokio::spawn` per frame: a `FLAG_REMOTE_CLOSED` frame could

+ // then `remove` a stream from `req_map` before the preceding DATA

+ // frame's task looked it up, silently dropping the final payload.

+ // The read loop already awaits this per frame, so inline is correct.

 
 let req_map = self.streams.clone();

- tokio::spawn(async move {

- if let Some(resp_tx) = get_resp_tx(req_map, &msg.header).await {

- resp_tx

- .send(Ok(msg))

- .await

- .unwrap_or_else(|_e| error!("The request has returned"));

- }

- });

+ if let Some(resp_tx) = get_resp_tx(req_map, &msg.header).await {

+ resp_tx

+ .send(Ok(msg))

+ .await

+ .unwrap_or_else(|_e| error!("The request has returned"));

+ }

 
}

commit 01357bf

Interactive:the reader handling every frame in order.

But this naive solution was NOT perfect. My "reality has a surprising amount of detail"4moment happened when the reviewer5made me aware of a different limitation of this fix.

There is another construct that we must think of: the bounded mpsc channel. Every call's frames reach its caller through a tokio mpsc channel that holds 100 messages, andsend().awaitwaits while it is full.

let
 
(
tx
,
 
rx
):
 
(
ResultSender
,
 
ResultReceiver
)
 
=
 
mpsc
::
channel
(
100
);

src/asynchronous/client.rs @ f31f592, Client::new_stream

With the reader doing that send itself, one full channel stops the reader, and every other call on the connection waits behind it. Here is the reviewer's reproduction: a 200-frame stream that nobody reads, plus an unrelated unary call.

Interactive:the 200-frame reproduction.

## The Better Fix

Each call gets its own mailbox: an unbounded queue that only the reader writes to.

* One reader handles every frame, in wire order. Nothing is spawned.
* The reader appends to a mailbox and moves on. It never waits for a caller, so a slow stream cannot stall the others.
* The close frame goes into the same mailbox, behind the data.
* The cost: a stream nobody reads keeps growing in memory. ttrpc has no flow control, so a hard limit would mean blocking the connection or failing the stream.

Interactive:the same reproduction with mailboxes.

## Client and Server Asymmetry

The server also hands frames to tokio tasks, so why did only the client need this fix?

* Sending keeps order: a stream's frames go, one awaited send at a time, into one queue drained by one writer.
* The old client let each received frame's task run freely, and the close task deleted the stream, so an early close lost the payload.
* The server's reader waits for each frame's task to start, leaving only a tiny window6for reordering.
* The server never deletes a stream on close, so no frame is dropped as unknown.

1. This is my PR that this note is based on:containerd/ttrpc-rust#312↩
2. "GRPC for low-memory environments." The README explains that grpc-go's memory overhead is a problem "when running a large number of services on a single machine". Fromcontainerd/ttrpc.↩
3. "The protocol does not include features for handling unreliable connections such as handshakes, resets, pings, or flow control." From thettrpc protocol specification.↩
4. John Salvatier,Reality has a surprising amount of detail, 2017.↩
5. "The ordering bug is real, but this implementation introduces connection-wide head-of-line blocking. [...] I reproduced this by leaving a 200-frame stream unread and issuing an unrelated unary RPC: it times out with this patch." Tim Zhang,review on #312.↩
6. A stress test on the merged code saw about 1 in 2000 client-streaming calls with two adjacent frames swapped. None lost a frame.↩

View original