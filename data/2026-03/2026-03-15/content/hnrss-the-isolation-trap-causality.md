---
title: The Isolation Trap — Causality
url: https://causality.blog/essays/the-isolation-trap/
site_name: hnrss
content_file: hnrss-the-isolation-trap-causality
fetched_at: '2026-03-15T06:00:53.941048'
original_url: https://causality.blog/essays/the-isolation-trap/
date: '2026-03-12'
description: 'Erlang''s mailbox design is more disciplined than Go''s channels: only the owning process can read from a mailbox, and sends are asynchronous. Yet the four failure modes of shared mutable state still show up, just in different shapes.'
tags:
- hackernews
- hnrss
---

March 2026
 

# The Isolation Trap

 

What Erlang shows about the limits of concurrency through isolation

 
 
 

We’re continuing to look at the state of concurrency in programming languages and identifying what’s wrong with it. As a reminder, inMessage Passing Is Shared Mutable StateI argued that Go’s channels are shared mutable state with extra steps. But you may think Go’s channels aren’t true message passing. The honor for “best case for message passing” probably falls to Erlang. So let’s look at Erlang.

## The Best Case

The actor model has been a signficantly influential idea in concurrent programming since Carl Hewitt proposed it in 1973. The core idea is appealing: concurrent entities (actors) communicate exclusively through messages. Each actor has its own private state that no other actor can touch. If actors can’t share state, they can’t have shared-state bugs.

Various languages and frameworks have implemented versions of this idea. Akka brings actors to the JVM, but since they share a Java heap the isolation is enforced by convention, not by the runtime. Akka actors can pass a reference to a mutable object in a message, and now two actors share mutable state. Swift added actors in version 5.5 with stronger compile-time checks, but allows reentrant calls by default, reintroducing some of the problems actors are supposed to prevent. Orleans and Dapr offer “virtual actors” that solve lifecycle management but not the fundamental concurrency model.

If you were going to build the strongest possible version of the actor model, prioritizing safety and fault tolerance above everything else, you’d probably end up with something close to what Joe Armstrong and the Ericsson team built.

Erlang processes have separate heaps, so they can’t share memory. Messages are copied from one process to another, not shared by reference. If a process dies, its state dies with it, and supervision trees handle recovery. There’s no mechanism for one process to corrupt another process’s memory, because there’s no shared memory to corrupt.

This isn’t just academic elegance, it kept phone switches running with five nines of availability. It scaled WhatsApp to hundreds of millions of users on a small team. It has thirty years of production battle-testing in systems where downtime means real consequences.

Erlang is the strongest form of the isolation argument, and it deserves to be taken seriously, which is why what happens next matters.

## The Familiar Problems

In thefirst essayI argued that message passing is shared mutable state. The communication mechanism itself (channel, mailbox, message queue) is a shared mutable resource and inherits the problems that shared mutable state has always had. Erlang’s mailboxes are no exception.

Erlang’s single-owner mailbox design is more disciplined than Go’s channels: only the owning process can read from a mailbox, and sends are asynchronous. Yet the four failure modes of shared mutable state still show up, just in different shapes.

Consider two Erlang servers that each need data from the other:

%% Server A handles a request by calling Server B

handle_call
(request, _From, State) 
->

 Result 
=
 gen_server
:
call(server_b
,
 sub_request)
,

 {reply
,
 Result
,
 State}.

%% Server B handles a request by calling Server A

handle_call
(sub_request, _From, State) 
->

 Result 
=
 gen_server
:
call(server_a
,
 request)
,

 {reply
,
 Result
,
 State}.

This isn’t obviously wrong. Two servers collaborating is a normal architecture. But if a request arrives at Server A that triggers a call to Server B while Server B is already handling a request that calls Server A, then both block forever. Each is waiting on its own mailbox for a reply that will never arrive, because the other server is waiting too. This is a mutex deadlock expressed through message passing.

Erlang developers know this pattern and OTP design guidelines discourage it. But knowing about it doesn’t prevent it. Researchers found previously unknown instances in production OTP libraries written by experts following the guidelines. And a 2026OOPSLA paperby Fowler and Hu proves a stronger result: two protocols that are individually deadlock-free can still combine to deadlock in an actor system. The only solutions are restricting each actor to a single session at a time (too limiting for real servers) or building a flow-sensitive type system to thread protocol state through every function call. The problem isn’t that developers write circular calls by accident. It’s that deadlock-freedom doesn’t compose.

The other three failure modes follow the same pattern. Erlang mailboxes are unbounded and provide no automatic backpressure, so if a process receives messages faster than it can handle them, the mailbox grows until the node runs out of memory and crashes. Fred Hébert (author ofErlang in Anger) built an entire library calledpoboxspecifically for this problem, noting that “high throughput Erlang applications often get bitten by the fact that Erlang mailboxes are unbounded.” Message interleaving from multiple senders is nondeterministic, creating ordering races that the language can’t prevent. And Erlang messages are dynamically typed, so a process can send any term to any other process with no compile-time check that the receiver expects it.

These are real bugs in real Erlang systems. The mailbox design makes some of them less likely than their Go channel equivalents, but doesn’t make any of them structurally impossible.

## The Mitigations

Erlang has answers for each of these problems, and they’re good answers:

Problem
Erlang’s Shape
Mitigation
Enforced by
Deadlock
Circular 
gen_server:call
 chains
Prefer async casts, use timeouts
Convention at design time
Leak
Unbounded mailbox growth
Monitor sizes, use 
pobox
, back-pressure
Monitoring at runtime
Race
Nondeterministic message interleaving
Careful protocol design, testing
Discipline at design time
Protocol violation
Untyped messages, unmatched clauses
OTP behaviors, code review
Convention at design time

These mitigations work. They’re a big part of why Erlang systems are as reliable as they are.

But look at the last column: convention, monitoring, discipline. Every one of these falls on the programmer. Not one is enforced by the language or the compiler, and one can’t even be enforced until the system is running in production under real load. Every mitigation depends on the programmer doing the right thing, and properties that aren’t guaranteed by the system will eventually be violated by the humans using it.

Skip thegen_serverand use raw message passing? You lose the protocol structure. Usegen_server:callin a circular dependency? There’s a 5-second timeout by default so you won’t deadlock, but you’ll get a cascading timeout failure that’s hard to trace. Neglect to monitor mailbox sizes? An overflow crashes the node at 3 AM. Use the wrongreceiveclause pattern? Silent misbehavior.

(Edited Mar 14: Originally this paragraph said “Forget to set a timeout on agen_server:call?” which implied the default has no timeout. This was incorrect,gen_server:call/2has a 5-second timeout default. The circular call example would timeout rather than deadlock. Thanks to commenters on Hacker News for the correction.)

Each mitigation individually is reasonable, but they accumulate. A new developer joining an Erlang team doesn’t just need to learn the language, they need to learn which conventions are load-bearing, which tools to run, which patterns are safe, and which innocent-looking code has a deadlock hiding inside it. Each new thing the programmer has to remember is one more thing the programmer can forget.

This is the discipline tax. It works when the team is experienced, the codebase is well-maintained, and the conventions are followed consistently. It erodes when any of those conditions weaken, and given enough time and enough turnover they do.

## The Bottleneck

Even when all the mitigations are in place and the team follows every convention, the isolation model has a structural performance limitation.

Every process’s state is accessed through its mailbox. One process, one mailbox, one message at a time. All access to that process’s data is serialized. If you want to read its state, you send it a message and wait for a reply.

This is fine under moderate load, but it becomes a problem when a thousand other processes all need to read from the same data: a routing table, a configuration store, a session registry, a shared lookup cache. The pure model says “send a message, wait for a reply.” Each reader waits in line, the mailbox becomes a funnel, and throughput collapses.

This isn’t a bug or a design oversight, but rather a direct consequence of the isolation model. If safety comes from “no process can access another process’s state directly,” then all state access must go through the owning process, and the owning process becomes a serialization bottleneck.

Safety through isolation means that safety and performance are in tension. I think Erlang’s creators understood this quite well.

## The Escape Hatch

ETS (Erlang Term Storage) exists because of this bottleneck. ETS tables are mutable, concurrent, in-memory data structures sitting outside the process model. Any process can read from or write to a public ETS table without sending a message to anyone.

This was a principled engineering decision by the Erlang team, not a mistake. They recognized that pure isolation couldn’t meet real-world performance requirements and provided a carefully designed escape hatch.

And the pressure didn’t stop at ETS. OTP 21 addedpersistent_term, a global immutable store optimized for data that is read constantly and written rarely (e.g. configuration, routing tables, compiled regular expressions), because even ETS had too much overhead for those access patterns. OTP 22 added theatomicsandcountersmodules: direct shared-memory operations with no copying, no message passing, and no process involvement at all. Each addition moved further from the isolation model, because each addressed a performance gap the previous escape hatch couldn’t close.

But an escape hatch is still an escape hatch. These mechanisms bypass the process isolation model entirely. They are shared state outside the process model, accessible concurrently by any process, with no mailbox serialization and no ownership semantics.(Edited Mar 14: originally this sentence included “no message copying”. ETS does copy terms on read and write, and individual key operations are atomic.)They are shared state outside the process model, accessible concurrently by any process, with no mailbox serialization and no ownership semantics. ETS does copy terms and individual key operations are atomic but multi-key operations are not. Traversals don’t provide snapshot consistency and none of these mechanisms participate in the process isolation model that Erlang’s safety story is built on.

And when you introduce shared state into a system built on the premise of having none, you reintroduce the bugs that premise was supposed to eliminate.

Experienced Erlang developers are well aware of this tradeoff. Large systems routinely shard state across many processes, combine actors with ETS for read-heavy workloads, and usepersistent_termfor global configuration. These are effective engineering patterns. But their existence is itself the point: they are ways of relaxing isolation when isolation becomes the bottleneck. The question isn’t whether Erlang engineers can work around the limitation, but what it means that they have to.

## The Consequences

Maria Christakis and Konstantinos Sagonas built a static race detector for Erlang and integrated it into Dialyzer, Erlang’s standard static analysis tool. They ran it against OTP’s own libraries, which are heavily tested and widely deployed.

They found previously unknown race conditions. Not in obscure corners of the codebase. Not in exotic edge cases. In the kind of code that every Erlang application depends on, code that had been running in production for years.

The races clustered around three categories, all at the points where isolation breaks down:

ETS table races.Process A reads a key from a public table, decides to update it, but Process B modifies it between the read and the write. Classic check-then-act, also known as TOCTOU (“time of check to time of use”). ETS explicitly documents that table traversals provide no snapshot consistency: concurrent inserts during iteration can cause keys to be missed or visited twice. Individual key operations are atomic, but multi-key operations are not.

Process registration races.Erlang allows processes to be registered under a name in a global mutable namespace. Two processes racing to register the same name, or one process looking up a name and sending a message while the named process dies and the name gets re-registered to a different process. These are typical shared mutable state TOCTOU bugs.

Process dictionary races.The process dictionary is per-process mutable state, essentially a thread-local mutable hash map that breaks referential transparency and creates subtle ordering dependencies when combined with operations that cross process boundaries.

These are not Erlang-specific problems. They are precisely the same categories of bugs that shared mutable state has always produced: check-then-act races, concurrent modification without atomicity, TOCTOU on a global namespace. They were found in a language designed to address them.

## The Pattern

Let’s step back and look at the full picture.

The actor model’s promise is concurrency through isolation. Erlang is its strongest implementation: separate heaps, copied messages, single-owner mailboxes. The community develops sophisticated mitigations for the problems that still leak through: OTP behaviors, supervision trees, cultural conventions, monitoring tools, static analysis. And then performance pressure forces the introduction of shared mutable state, which bypasses all those mitigations and reintroduces the problems that the model and all its accumulated safeguards were supposed to prevent.

Weaker actor implementations like Akka don’t even get this far. They start with shared mutable state available from day one and rely entirely on programmer discipline to avoid using it. Erlang at least enforces isolation at the runtime level before performance pressure erodes it.

This is pretty much the same cycle from the first essay, viewed from a different angle. Go’s channels looked like an escape from shared memory but turned out to be shared memory in disguise. Erlang’s isolation genuinely isn’t shared memory, until the real world forces shared memory back in through the door marked “performance.”

Different starting points leading to a similar destination.

And this isn’t a criticism of Erlang’s engineering or the actor model as a concept. The Erlang team made the right tradeoffs given their foundation. The problem is the foundation itself. Any concurrency model that achieves safety through isolation will face this pressure, because when multiple computations need the same data at the same time they need concurrent access to it. Isolation can only provide access through serialization. When serialization can’t keep up the choice is between safety and performance, and in production, performance often wins.

In these two essays we’ve seen two approaches both hitting the same-shaped wall. The common thread isn’t channels or actors or any specific mechanism. It’s that both approaches start from the same assumption: safety comes from controlling how threads interact. So far, that assumption has a perfect track record of leading back to the problems it was supposed to solve.

### References

* Hewitt, Carl, Peter Bishop, and Richard Steiger. “A Universal Modular ACTOR Formalism for Artificial Intelligence.”IJCAI 1973.PDF
* Armstrong, Joe. “Making Reliable Distributed Systems in the Presence of Software Errors.” PhD thesis, Royal Institute of Technology, Stockholm, 2003.PDF
* Christakis, Maria and Konstantinos Sagonas. “Static Detection of Race Conditions in Erlang.”PADL 2010.PDF
* Christakis, Maria and Konstantinos Sagonas. “Static Detection of Deadlocks in Erlang.”TFP 2011.PDF
* Fowler, Simon and Raymond Hu. “Speak Now: Safe Actor Programming with Multiparty Session Types.” OOPSLA 2026.arXiv
* Hébert, Fred.pobox: External buffer processes to protect against mailbox overflow in Erlang. GitHub.
* Hébert, Fred. “Handling Overload.”Blog post.
 
 
Discuss:
Hacker News
Reddit
 
 

### Stay in the loop

 

Get notified when new posts are published. No spam, no tracking, just ideas.

 
 
 
Subscribe