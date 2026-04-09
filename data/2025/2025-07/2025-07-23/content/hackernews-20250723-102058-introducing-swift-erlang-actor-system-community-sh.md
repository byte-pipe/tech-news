---
title: Introducing swift-erlang-actor-system - Community Showcase - Swift Forums
url: https://forums.swift.org/t/introducing-swift-erlang-actor-system/81248
site_name: hackernews
fetched_at: '2025-07-23T10:20:58.262852'
original_url: https://forums.swift.org/t/introducing-swift-erlang-actor-system/81248
author: todsacerdoti
date: '2025-07-23'
published_date: '2025-07-22T15:48:12+00:00'
description: 'I&#39;m excited to share a new actor system we&#39;ve been building for Swift&#39;s distributed actors: swift-erlang-actor-system. This actor system enables Swift programs to join a distributed Erlang cluster. Here&#39;s an example of&hellip;'
---

# Introducing swift-erlang-actor-system

Community Showcase

concurrency
,

distributed

carsonkatri

 (Carson Katri)


 July 22, 2025, 3:48pm


1

I'm excited to share a new actor system we've been building for Swift's distributed actors:swift-erlang-actor-system.

This actor system enables Swift programs to join a distributed Erlang cluster.

Here's an example of a simple chat program using the actor system:

Demo Video

Erlang (and other languages that run on its VM) can connect multiple runtime systems together withdistributed Erlang. Each runtime is referred to as a "node". Erlang also supports "C nodes", which allow a program other than the Erlang runtime system to communicate with Erlang nodes and other C nodes.

We've wrapped this C node functionality into an actor system that can be used with Swift's distributed actors. Here's how you can try it out:

# Getting Started

1. Install Elixirfollowing their instructions. For example, on macOS you can install with Homebrew:

brew install elixir

1. Startepmd, the "Erlang Port Mapper Daemon". This is how Erlang nodes discover each other by name, instead of IP and port:

epmd

1. Start an interactive Elixir node and get the cookie and hostname:

iex --sname elixir_node

iex(elixir_node@YOUR_HOSTNAME)> Node.get_cookie()
:YOUR_COOKIE

1. Create a Swift package with a dependency onotp-interop/swift-erlang-actor-system, and setup a node and distributed actor:

import ErlangActorSystem
import Distributed

// 1. Declare a distributed actor
@StableNames
distributed actor Counter {
 typealias ActorSystem = ErlangActorSystem

 private(set) var count: Int = 0

 @StableName("increment")
 distributed func increment() {
 count += 1
 print(count)
 }

 @StableName("decrement")
 distributed func decrement() {
 count -= 1
 print(count)
 }
}

// 2. Create a node
let actorSystem = try await ErlangActorSystem(name: "swift_node", cookie: "LJTPNYYQIOIRKYDCWCQH")

// 3. Connect to another node
try await actorSystem.connect(to: "elixir_node@DCKYRD-NMXCKatri")

// 4. Create an instance of a distributed actor using the ErlangActorSystem.
let counter = Counter(actorSystem: actorSystem)

// 5. Give the actor a name so we can find it from another node.
actorSystem.register(counter, name: "counter")

// run loop
while true {}

1. Run the Swift executable.
2. And send messages to our Swift node from Elixir:

iex(elixir_node@YOUR_HOSTNAME)> GenServer.cast({:counter, :"swift_node@YOUR_HOSTNAME"}, :increment)
iex(elixir_node@YOUR_HOSTNAME)> GenServer.cast({:counter, :"swift_node@YOUR_HOSTNAME"}, :decrement)

Swift's actors map nicely to Erlang processes, and Swift's language-level support for distributed actors makes interfacing between the two languages easy.

# Motivation

In theotp-interopGitHub organization, you'll also findelixir_pack, a package for bundling Elixir applications to run on iOS and other Apple platforms.

We needed a clean way to communicate between Swift and Elixir on-device—and Swift's distributed actors were a perfect match.

We've also started exploring using distributed Erlang for client-server interaction byfiltering messagesbefore accepting them on the server.

# Detailed Design

swift-erlang-actor-systemuses theerl_interfaceC library from Erlang/OTP for networking and serialization. It's included as a C source target in the Swift Package.

You can swap out theTransportto support custom use cases—such asusing WebSocketsinstead of raw TCP sockets.

## Message Serialization

Distributed Erlang usesExternal Term Formatto serialize any value in the Erlang VM.erl_interfaceprovides functions for encoding/decoding terms. We expose this viaTermEncoderandTermDecoderclasses that can convert anyCodabletype to this format.

We've also started experimenting withusingswift-binary-parsingto decode terms.

## Stable Names

One of the challenges we faced when building this actor system was identifying remote calls across languages.

By default, Swift uses mangled function names to identify remote calls. To call a function on a Swift node from an Erlang node, your Erlang node would need to know about Swift's name mangling.

To get around this, we added the@StableNamesmacro. This allows you to decorate the methods of your actor with custom unique names.

This is also important when working with Swift's@Resolvablemacro.@Resolvableis used on protocols to define actors that are only ever used remotely. We use this to interface with processes that are implemented on the Erlang node.@StableNamesworks with@Resolvabletoo, you just have to add a conformance toHasStableNames:

defmodule Counter do
 use GenServer

 @impl true
 def init(count), do: {:ok, count}

 @impl true
 def handle_call(:count, _from, state) do
 {:reply, state, state}
 end

 @impl true
 def handle_cast(:increment, _from, state) do
 {:noreply, state + 1}
 end

 @impl true
 def handle_cast(:decrement, _from, state) do
 {:noreply, state - 1}
 end
end

@Resolvable
@StableNames
protocol Counter: DistributedActor, HasStableNames
 where ActorSystem == ErlangActorSystem
{
 @StableName("count")
 distributed var count: Int { get }

 @StableName("increment")
 distributed func increment()

 @StableName("decrement")
 distributed func decrement()
}

A concrete actor implementing this protocol called$Counterwill be created. It will use the stable names provided via the macro to send the correct messages to the Erlang node.

let counter: some Counter = try $Counter.resolve(
 id: .name("counter", node: "iex@hostname"),
 using: actorSystem
)

try await counter.increment()
#expect(try await counter.count == 1)

Stable names will likely be necessary in most cross-language actor systems. I'd like to see something like this integrated into Swift in the future.

Looking forward to hearing your thoughts on this actor system, and distributed actors in Swift in general.

19 Likes

pepi

 (Pedro Piñera)


 July 22, 2025, 8:08pm


2

This is fantastic news. Thanks for making it possible.

We at Tuist love both languages. We used Elixir tobuild our serverand build our clients using Swift.

Something I’ve been thinking a lot lately, is whether both languages could operate using the same primitives, and this work provides an answer to that.

Something that I wonder though, is how a client in Swift can authenticate with Elixir nodes with a mechanism other than an agreed cookie, which is something can leak easily. Is this something that must be solve at a layer above? If so, are there good patterns that you’d recommend?

2 Likes

carsonkatri

 (Carson Katri)


 July 22, 2025, 8:15pm


3

Something we've experimented with is providing a custom-proto_distthat can filter messages coming from a client:GitHub - otp-interop/tcp_filter_dist: Filter messages sent over Erlang distribution.

It should be possible to filter out messages from un-authenticated clients based on the message structure. You could also build your own_distmodule that does some custom authentication before the connection is accepted.
