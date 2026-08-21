---
title: '20× the CI traffic without getting slower: How we rebuilt Git serving at Datadog | Datadog'
url: https://www.datadoghq.com/blog/engineering/gitretriever/
site_name: tldr
content_file: tldr-20-the-ci-traffic-without-getting-slower-how-we-re
fetched_at: '2026-08-21T19:25:16.644220'
original_url: https://www.datadoghq.com/blog/engineering/gitretriever/
author: Mike Thompson, Daniel Esponda
date: '2026-08-21'
description: Learn how Datadog built gitretriever to handle 20× more CI Git traffic while maintaining low latency and reducing backend CPU usage.
tags:
- tldr
---

Mike Thompson

Senior Staff Engineer

 
 
 
 
 
 

Daniel Esponda

Staff Engineer

 

If you have ever watched a CI job sit on “Fetching repository …” while nothing seems to happen, you already know the unglamorous truth about continuous integration: Every job begins by getting the code, and getting the code is not free.

At Datadog, CI fetches code millions of times a week across thousands of repositories. Our largest repositories are monorepos with years of history and hundreds of thousands of files. At that scale,git clonestops being a footnote and becomes a large contributor to CI run times.

This is the story ofgitretriever, the Git mirror we built to serve code to CI at Datadog scale. In its first 4 months, gitretriever served more than a billion Git requests and hundreds of terabytes of code. Today gitretriever handles more than 100 million requests each week. Despite the 20× traffic growth since launch, median latency has remained around 40 ms, while fetch-serving CPU on our previous Git backend has dropped by three to four times.

## Serving Git to CI, and why it gets hard

Datadog has a unique CI setup: GitHub serves as the authoritative code repository, while almost all of our internal CI workloads run on a self-hosted GitLab installation. CI fetches from GitLab’s Gitaly, fronted by Praefect (Gitaly Cluster’s routing and replication manager) and kept in sync with GitHub by an internal service (aptly named “codesync”). This hybrid architecture has carried us through more than a decade of growth.

But CI load does not grow smoothly. The expanding use of AI coding agents has driven an order-of-magnitude increase in Git traffic, with agents hitting Git far harder and more often than even our most active contributors ever could. That traffic comes on top of the continually growing load from internal deployment, auditing, and security services. As that growth accelerated, the pressure hit hardest where our code is densest: our large monorepos. Operational load increased, CI run times grew, and multi-hour long CI outages became more frequent. It was clear we needed a more sustainable solution.

## Why the usual fixes don’t scale

We tried adding capacity, we tried increasing instance size, we tried placing different repositories on dedicated backends, and we tried optimizing build pipelines. Things would improve for a week or two, but then our CI infrastructure would inevitably end up degraded or outright down. So why didn’t any of the usual approaches work?

A single fetch from a large monorepo can consume several seconds of server CPU. At peak, hundreds of jobs perform fetches at the same moment and land on the same handful of nodes. Adding capacity did little to reduce per-node CPU usage. In some cases, adding more nodes made the problem worse.

Before committing to a new architecture, we had to figure out why none of our previous attempts at fixing the problem had worked:

* Scale the backend or add nodes: In our replicated setup, every write had to be copied to every replica. Adding a node increased replication overhead instead of relieving it.
* Put a content delivery network (CDN) or caching proxy in front: The expensive part of a fetch isn’t a static byte range you can cache at the edge. It’s computation that’s specific to each client’s request.
* Clone on demand from GitHub: That simply moves the thundering herd upstream, where we run into server-side rate limits.

The common thread was that we had been scaling the wrong axis. Read traffic scales with the number of CI jobs, but in our replicated architecture, write costs scale with the number of replicas. Every time we added replicas to handle more reads, we also increased replication overhead, and more CPU time went to maintaining the system instead of serving fetches.

To understand why serving those fetches consumed so much CPU in the first place, it helps to look at what happens during a Git fetch.

## Why a Git fetch is expensive

To understand why our design works, it helps to understand how Git stores data and where agit fetchspends its time.

### Git data types

Git’s object database is primarily built around immutable objects. For the purposes of this post, we’ll focus on three:

* Blobs, which store file contents
* Trees, whichdescribe directory entries (for example, folders and blobs)
* Commits, which store metadata, a commit message, a reference to a tree, and references to parent commits

Each object is identified by a hash of its type, size, and contents. SHA-1 remains the default object format, although Git also supports SHA-256 repositories.

Finally, there arereferences, which are mutable names stored separately from objects. For example,refs/heads/mainidentifies the commit at the tip of themainbranch.

Objects may be stored on disk individually asloose objectsor grouped intopackfiles. Within a packfile, an object may be stored in full or as a delta against another object (known asdeltacompression), which allows Git to efficiently store the complete history of changes to files within a repository. Packfiles are immutable to allow for safe concurrent reads.

 
 
 
 
 
Figure 1: References point to commits, which reference trees and parent commits. Trees reference blobs and other trees. Packfiles store Git objects independently of references.
 
 
 
 
 
 
 
 
Figure 1: References point to commits, which reference trees and parent commits. Trees reference blobs and other trees. Packfiles store Git objects independently of references.
 
 
 
Close dialog

 
 
 
 
 
 

Write operations (for example,git push) may introduce new packfiles. A background maintenance process periodically consolidates loose objects and smaller packfiles into new packfiles. Unreachable objects (for example, deleted files) are eventually removed after a certain threshold by being omitted during packfile consolidation.

### Git protocol v2

Now that we understand Git’s data types, we can briefly look at how the current (v2) Git protocol works.

The Git client uses thels-refscommand to learn the current object IDs of references it cares about (for example, all branches). The client and server then begin a multi-round negotiation to determine which objects the server needs to send to the client. You can read more about this negotiation process in theGit protocol v2 documentation.

Once the client and server have determined which objects to send, the server creates a packfile containing those objects and sends it to the client.

Constructing the response packfile can be CPU and I/O-intensive. The server locates objects within packfiles by using an index that Git maintains for each packfile. Some objects can be copied as is into the response packfile, while others must be decompressed and recompressed using delta compression. Under a sufficiently large number of concurrent fetches, this packfile construction work can saturate server CPU and storage capacity.

Client behavior, such as requesting weeks’ worth of changes to a large monorepo, can make this more expensive in both CPU and I/O operations. Git attempts to reduce this cost with reachability bitmaps, sparse traversal, multi-pack indexes, and pack reuse. We tried all of these options, but client behavior and the rate at which our monorepos changed still concentrated CPU load on a small number of servers.

The final step of a fetch or pull from a Git server is for the client to read the received packfile and update its local index of available objects. This requires only a small amount of client-side CPU.

## Our approach: Many independent mirrors, kept fresh

If the problem is CPU concentrated on a few contended nodes, the solution is to stop concentrating it.

Gitretriever runs independent pods, each of which maintains a fresh local copy of the repositories it serves without waiting for every node to reach consistency. Each pod serves its local copy directly, with no consensus and no multi-writer replication between peers. Gitretriever pods have two roles, as shown in the following diagram:

* Mirrorsstay in sync with GitHub. We deliberately keep this fleet small because its job is to be a good GitHub client: a handful of well-behaved pollers rather than thousands of them.
* Relaysfan out reads to CI jobs. This fleet is larger and autoscaled based on CPU and network load, allowing us to provision enough read capacity to meet demand without turning that growth into additional load on GitHub.

 
 
 
 
 
Figure 2: Mirrors synchronize repositories from GitHub, while relays distribute those repositories to CI jobs and other Git workloads.
 
 
 
 
 
 
 
 
Figure 2: Mirrors synchronize repositories from GitHub, while relays distribute those repositories to CI jobs and other Git workloads.
 
 
 
Close dialog

 
 
 
 
 
 

## Staying fresh and reducing CPU usage

The architecture works only if every mirror and relay stays close to the latest changes without recreating the CPU bottlenecks we were trying to eliminate. We designed gitretriever around three principles that keep repositories fresh while minimizing repeated work.

### Distribute Git pulls across branches

Gitretriever mirrors continually poll the upstream in a tight loop for changes. Gitretriever performs a parallel fetch for each reference it detects as changed since the previous synchronization loop iteration. No single request concentrates an expensive delta compression job on GitHub, and each small pack requires far less indexing CPU than one monolithic monorepo pack. Staying close to the tip of each branch also means that, in any given synchronization loop iteration, only a small number of branches have changed, reducing the number of packfiles we need to fetch.

### Spend the sync work once, then reuse it

For the busiest repositories, one mirror cannot serve every client, so changes fan out to a fleet of relays. Relays can connect to mirrors or to other relays. Each relay splits its upstream connection into two channels:

* A signaling gRPC stream:Announces that a pack is ready, propagates reference updates, and communicates mirror and relay topology changes
* A plain HTTP endpoint:Serves the pack bytes themselves

Because Git objects are content-addressed, a relay installs the packfile it receives from its upstream mirror or relay without regenerating, re-indexing, or re-verifying it. It drops the packfile and its index into place, trusting the objects inside by the hashes that identify them. The work of pulling and indexing from GitHub happens once on the mirror, and every relay reuses that work instead of fetching again. As a result, the relay fleet can grow without adding load on GitHub while remaining within single-digit milliseconds of the tip.

### Never build the same pack twice

Gitretriever is both a Git client and a Git server. The current implementation uses Git’s default backend storage format: packfiles, reference tables, reachability bitmaps, and multi-pack indexes. That means gitretriever has to make serving other Git clients (such as CI jobs) as efficient as possible.

A fresh push to a busy branch sets off a thundering herd of identical fetches. Gitretriever implements apack cache, allowing it to reuse previously assembled packfiles for identical client requests. About half of all pack-building fetches are served directly from the cache, skipping the delta compression calculation on mirrors and relays entirely. Cache misses are still served locally by the mirrors and relays, so even a cache miss never becomes a trip to GitHub.

Underneath these are smaller refinements, including a readiness check that understands Git state and keeps a pod out of rotation until its pack count is healthy, along with background repacking that keeps the packfile count under control while the pod continues serving. But the theme never changes: Take the CPU that used to pile up in one place and either spread it out or stop repeating it.

Future iterations of gitretriever will build on the relay replication protocol to keep an always-up-to-date copy of our large repositories directly on CI nodes, allowing jobs to skip the initialgit clonealtogether.

## The bigger surprise: Many use cases don’t need a clone

Once every repository had a fresh mirror, something in the traffic caught our eye: Most non-CI workloads don’t need a full repository clone. They wanted a single file at a commit, the SHA a branch pointed to, the list of files that changed, or the merge base of two refs. Cloning an entire repository to answer one of those questions was enormous overkill, yet our internal services, developer tools, and AI agents were doing it constantly.

So we added a small, read-only HTTP API for exactly those queries. Resolving a ref or reading a file takes single-digit to tens of milliseconds. By comparison, a shallow clone of a large monorepo takes on the order of 75 seconds and keeps a CPU core busy for most of that time. Moving these use cases to the API reduces latency and removes load from the entire system.

The non-CI workloads changed how we think about gitretriever. It’s less a faster Git server and more the query layer for Git across our engineering systems.

This is the direction the platform is heading. As workflows become more automated and more AI agents ask questions about code, the cheapest and fastest answer is often another API rather than handing out a repository clone.

## Rolling out gitretriever safely

Rolling out gitretriever required careful planning. Our CI infrastructure is used by every engineer at Datadog, so one wrong move could bring engineering to a halt. We used feature flags and built in automatic fallback to the old backend into our CI jobs, so if a mirror became unreachable or a fetch failed, the job fell back to the previous path. The worst-case outcome was no worse than before. We then migrated one repository group at a time, starting with the largest monorepo, while watching the old backend’s CPU graph.

When that first monorepo cut over, we saw an immediate step decrease in CPU usage. That confirmed our understanding of the problem: Gitretriever was absorbing the heaviest, most CPU-dense fetches first. Those were the same ones that had been degrading developer experience and driving outages.

The metrics matched our expectations:

* Synchronization time dropped from several seconds to a few hundred milliseconds, making continuous, coordination-free mirroring possible.
* To date, gitretriever has servedmore than a billion Git requests and hundreds of terabytes of dataacross roughly5,500 repositories, and now handlesmore than 100 million requests each week.
* Traffic grew about 20× in 4 months while median serve latency remained around 40 ms(Figure 3). The system became an order of magnitude busier without getting materially slower.
* The result we care about most: Moving CI fetch traffic to gitretrieverreduced the old backend’s fetch-serving CPU by three to four times, even as overall CI activity kept climbing(Figure 4). Its memory footprint dropped in step, which later let us right-size that backend down. The old backend still handles some use cases that gitretrieverdoesn’tyet support (e.g., rendering the GitLab UI), so wedon’tclaim we replaced it (yet). But the fetch-path load it had been drowning under is gone.

 
 
 
 
 
Figure 3: Serve volume and median latency, each indexed to launch. Traffic grew about 20× while median latency remained around 40 ms.
 
 
 
 
 
 
 
 
Figure 3: Serve volume and median latency, each indexed to launch. Traffic grew about 20× while median latency remained around 40 ms.
 
 
 
Close dialog

 
 
 
 
 
 

 
 
 
 
 
Figure 4: The old backend’s fetch-serving CPU during the rollout, stepping down as each repository group migrated to gitretriever.
 
 
 
 
 
 
 
 
Figure 4: The old backend’s fetch-serving CPU during the rollout, stepping down as each repository group migrated to gitretriever.
 
 
 
Close dialog

 
 
 
 
 
 

## How we built it: Two engineers, Claude Code, and design doc in nearly every folder

We chose to use Claude Code on this project to accelerate development and to explore how far AI could responsibly assist with building production infrastructure. What made an AI collaborator trustworthy on a system this central wasn’t the model; it was the discipline around how we used it.

We planned before we wrote code, designing each change and iterating on the design through several rounds before committing a line of code. We validated every change with integration tests backed by real metrics and logs, not just unit tests, so the bar for “done” was observed behavior rather than a green checkmark. To keep both the AI and ourselves aligned across a dozen packages, we maintained a living design document in nearly every directory, describing its architecture, data flow, concurrency model, and configuration, and updating it alongside the code.

Those documents ended up serving two purposes. During development, they kept AI-generated changes aligned with the architecture. When ownership of the service transitioned to the team that now maintains it, the same documents became the handoff.

The lesson we would pass on is that the design documents became the interface between the engineers, the AI, and the next team. Ultimately, the quality of your tests and telemetry data sets the ceiling on how far you can trust an AI collaborator.

## What’s next

Gitretriever is not finished. We’re expanding the query API so more workloads can skip cloning entirely, allowing us to fully decommission our old Git backend. We’re also continuing the rollout across the rest of our repositories and building for a future where automated and agent-driven workflows ask even more of Git.

A few ideas we’ll carry into whatever comes next:

* Make it disposable so you do not have to make it durable.Some of the hardest parts became much simpler once we made them rebuildable instead of authoritative.
* Content addressing lets you trust data by name.That’s what makes coordination-free replication safe.
* The fastest fetch is the one that transfers nothing, whether that’s a fast-path ref update or an API call that answers the real question without a clone.

More than any single optimization, gitretriever reflects how we approach engineering at Datadog: Push a good system as far as it will go, then, when the scale curve demands it, design the next generation from a better understanding of the problem, validate it against real telemetry data, and write down what you learned so the next team can build on it.

If this sounds like your kind of problem, we would love to work with you. Take a look at ouropen roles.

 

 
 

Further reading

 
 

Datadog Platform Datasheet

 
 
 
 
 
 
 

Learn about the key components, capabilities, and features of the Datadog platform.

 
 
Download to learn more
 
 
 
 
 
 
 

## Related jobs at Datadog

 
 

### We're always looking for talented people to collaborate with

 
 

Featured positions

 
 
 
 
 
 
 
 
 
 
 

We havepositions

 
 
 
 
View all
 
 
 
 
 
 
 
 

## Start monitoring your metrics in minutes

 
find out how