---
title: 'Lies I was Told About Collaborative Editing, Part 2: Why we don''t use Yjs / Moment devlog'
url: https://www.moment.dev/blog/lies-i-was-told-pt-2
site_name: hnrss
content_file: hnrss-lies-i-was-told-about-collaborative-editing-part-2
fetched_at: '2026-03-16T19:26:58.984257'
original_url: https://www.moment.dev/blog/lies-i-was-told-pt-2
date: '2026-03-13'
tags:
- hackernews
- hnrss
---

# Lies I was Told About Collaborative Editing, Part 2: Why we don't use Yjs

Inpart 1 of this series, we found that users generally view the most popular collaborative text editing algorithms (including the most popular library,Yjs) assilently corrupting their documentswhen the algorithms resolve direct editing conflicts. We argued that, while this is potentially ok for live collaborative editing (since presence cursors help users to avoid direct editing conflicts), this property makes them generally wholly inappropriate for the offline case, as users will have no ability to avoid such conflicts.

This time, in part 2, we’re going to argue that these same popular algorithms—and Yjs in particular—arealsocurrently inappropriate for the live-collab case.Mostly it comes down to two points:

We’ll describe several specific challenges we experienced as we tried to bring Yjs to our production text editor.

We recommend a less-well-knownalternativeto Yjs because it is uniformly better on every axisexcepttruly-masterless peer-to-peer editing.

# Demo time: the simple solution (~40 lines of code)

I have heard the argument more times than I can count: CRDTs are operationally complex, but you need them (needthem!) for optimistic updates, edits during network blips (or extended disconnection), fine-grained provenance of edits, peer-to-peer reconciliation, and so on. I want to convince you thatallof these things (except true master-less p2p architecture) are easily doable without CRDTs.

Yes,easilydoable:40 lines of code(291 if you insist on counting the React scaffolding).

Below, this code is running as a live demo. You can use thePausebutton to simulate network disconnect. Edit the documents and unpause to see them synchronize, exactly like they would with a CRDT.

Note: offline reconciliation always produces odd results.We talked about this extensively inpart 1.Alloffline-capable reconciliation algorithms (e.g., CRDTs, OT, and this one) choose resolutions at basically-random. The point is not that this algorithm doesbetter, it’s that it does the same thing as CRDTs, but with vastly less complexity.

## How the simple thing works

This algorithm uses the extremely simple and boringprosemirror-collablibrary. The author haswrittenabout how it works, but it is almost trivial, so I will explain it here too:

For each document, there is a singleauthoritythat holds the source of truth: thedocument, appliedsteps, and the currentversion.

A client submits some transactionalstepsand thelastSeenVersion.

If thelastSeenVersiondoes not match the server’sversion, the clientmustfetch recentchanges(lastSeenVersion), rebase its own changes on top, and re-submit.

If the extra round-trip for rebasing changes is not good enough for you,prosemirror-collab-commitdoes pretty much the same thing, but it rebases the changes on the authority itself.

Note: “Authority” doesnotmean “centralized server that runs in AWS.”You can set up your laptop to be the authority as long as you are sharing with someone else. So this protocolisp2p-capable, but it’s notmasterless, which is what CRDTs provide.

And that’s it. That’s all it takes. 40 lines of code is the baseline complexity for optimistic updates, editing even when the network is flakey (or gone for arbitrary amounts of time), fine-grained provenance, and so on.

The only thing that’s missing is truly-masterless peer-to-peer editing. If you need that, great! But if you don’t, what’s the cost?

# Challenges implementing Yjs and CRDTs

This is the less fun part of the article to write, because there is no real way to talk about this without appearing to bag on Yjs in particular. I know people work hard on it. But… I also think that as an ecosystem it’s going to be impossible to progress if we do not acknowledge where we are right now. And, based what I know, I believe that where we are right now is:a tight spot.

## “But everyone is using Yjs”

Ok, let’s get this over with. Yes, I know: everyone else is usingYjs, the most popular collaboration library of all time. So the problem must be us. Right?

I thought that too, for awhile. I can also tell you the moment that the ghost of doubt left my body, and I knew in my bones that this was not true. It’s the moment I sawy-prosemirrorissue#113, a seemingly-innocuous and still-currently-open bug report which inadvertently reveals that Yjs willcompletely destroy and re-create the entire documenton every single keystroke.

Is this an accident? Sadly, no. In the discussion on they-prosemirrorannouncement thread from 6 years ago, Kevin (the author of Yjs)revealsthat this isby design.

There is some ensuing back-and-forth. Marijn (the author of ProseMirror) chimes in toexplain that this choice breaks, like, alotof stuff.

Kevinrespondsto suggest that, whatever the breakage, it is apparently good enough for Tiptap. Other userssuggestthat this really does break a lot of stuff—no,really, it does. Marijnrespondsto suggest that the perf justification for the replace-everything strategy might not be well-founded. There is a way to paper over some of these issues,kind of. And so on.

Aside: Yes, seriously, it breaks a lot of stuff.Performance is worse, because every keystroke causes you to re-create basically everything—everyNodeView, every decoration, all the DOM elements for the entire document. It breaks every plugin that depends on position mappings,e.g., comments and collaborative presence indicators. Undo, cursor position, and selection management all become extremely odd. The state of all the little widgets in your document will continously get totally wiped. Plugins that look atapplyget really slow because they have to inspect the entire document rather than just what changed. Node identity becomes unstable (although Kevinsaysit is not?). And on and on and on.

I still sort of can’t believe what I’m writing. It could make sense to adopt this regimen if there were no other options—but wedohave simpler, faster, better options with none of these problems. What I’m seeing here feels like a mistake that indicates a fundamental misunderstanding of what text editors need to behave well at all, inanysituation. And it was completely heartbreaking to read.

Now, look. I understand that the maintainers areworking on this issue right now. I sincerely hope they succeed and, in a year, I am forced to write another post about how all of this is now wrong. But that’s not where we seem to be, yet. And our experience was that it was hard to fight against the current architecture.

## Yjs make it much, much harder to hit latency perf goals

Our goal is for the editor to run at 60 fps.No matter how many collaborators, no matter how big the edit batches, no matter how complex the document: it is always the case that we have a maximum of ~16ms to doallour workand alsoa complete React render loop.

Like security, performance does not happen accidentally. It takes careful, targeted work, and constant vigilence for regressions. Below is an (incomplete) list of things that help us meet this target. All of them are harder or impossible with Yjs.

Transactions are very fast to apply.In our benchmarks, a modern machine supports x,000ProseMirrorTransactionapplications per second, including time it takes to update the DOM. Additionally, ProseMirror keeps position mappings across document versions, so aTransactionthat appears over the network can be “rebased” and applied extremely quickly. As I mentioned before, Yjs does not have this ability at all: every collaborative keystroke deletes and recreates the whole document from scratch.

The server batches transactions into chunks of 20 steps or less.Clients can generally apply 20Stepobjects in much less than 16ms. This means that the server can accumulate a large changeset (e.g., with many concurrent editors, a network blip,etc.) and it willstillnever hang the main thread by accident. This is completely trivial in ProseMirror. I don’t have any intuition for how we’d accomplish this with Yjs.

Conflict resolutionneverhappens on the main thread.We do conflict resolution on the server; it could also happen in a separateworker thread. My understanding is that it’s possible but challenging to run Yjs reconciliation routines in a worker thread.

We keep an eye on what in theEditorViewcauses latency.For example, right now, the most expensive part of ourEditorViewis calculating the positions of the remote presence carets. Yjs does not have a specific impact on this, aside from the fact that it’s obviously more expensive to reconstruct the entireEditorViewfrom scratch on every keystroke.

Updates to the DOM objects in the documentare incremental.This mostly comes fromreact-prosemirror, of course, but it again doesnotgo without saying, since Yjs replaces the entire document on each collaborative keystroke.

Visualized, our remoteTransactionapplication pipeline looks like this:

As simple as this approach is, we still regularly fail to meet the perf budget.

Unencouragingly—and even setting aside the delete/recreate issue—the Yjs pipeline is also just considerably more complicated. For one, CRDTs cannot represent rich text editing (it is alegitimately open research problem). Instead, Yjs represents ProseMirror documents using theirXML facilities. Since this means they can’t directly use ProseMirrorTransactionobjects, writes have to convertTransactionto a Yjs XML update; clients likewise receive updates and need to somehow turn the Yjs XML update back into aTransactionand apply it to the ProseMirror doc.

All of these things cost something. Even if they were cheap, Yjs still insists on replacing the document each time. It makes me physically anxious to look at this pipeline.

Again, my understanding is that the Yjs maintainers arestartingto make updates more fine-grained, and that the new world will look like the following.

This is definitely closer to what we want, but we will have see how much it helps in practice. What I will say right now is, given how hard it is to get the simple thing to run at 60 fps, it is still intimidating to take this regression, especially if we don’t need a truly-masterless p2p topology.

## Yjs is at odds with document schemas

Most people want a small, sane set of rules that govern the structure of a document,e.g., thatblockquotenodes cannot be children ofcode_blocknodes. Documentschemasare the primary tool for accomplishing this. They determine whether aTransactionhas produced a validEditorStateor not.

Document schemas are generally bundled statically as part of theapplication code. In a centralized setting, the server can reject proposedTransactions that are invalid, and the application can verify that all clients are on the same schema version. This is,e.g., what the Tiptap docsseem to suggestthey do.

Yjs is designed for truly-masterless peer-to-peer topologies, and its defaults are quire a bit more dangerous. They have to be—there is no real authority on what the schema is supposed to be!

In general, from Yjs’s perspective, no running instance knows for sure whether a change is straightforwardly invalid, or it just hasn’t received the new schema yet.

Accordingly, in our testing ofy-prosemirrorv1.3.7, whenschema.node()throws an exception because (including because the schema is invalid),the node appeared to be permanently deleted, and that deletion was propagated to all peers.

Youcando better, but you have to know to set it up ahead of time,e.g., Tiptap at least detects schema mismatch and halts the editor and forces a reload.

If left alone, this is particularly disastrous during upgrades. If you’re disconnected for an extended period of time, an upgrade occurs, and people use the new feature, when you connect again, you will silently destroy all the new data. Ouch!

This is not to say that youcan’tget around this (e.g., Tiptap does). But, it takes extra work to not blow your entire leg off, in a way that is very hard to debug.

## Yjs makes permissions vastly more painful

Real-world document editors will generally provide a variety of permissions that can be granted to other users. Obviously there isEditor, but it’s very common to also haveViewer,Commenter, andSuggesting, to name a few examples.

All of these features involve allowing some users selective permissions to editpartsof the document (e.g., adding a comment mark to the document). Normally, this is normally pretty simple to do: you look at theTransaction, see how it alters the document (e.g., does it just set a mark or does it also change text), and accept or reject based on the submitting user’s permissions.

It’s quite a bit more awkward in Yjs. Since Yjs mapsTransactionto and from XML updates, you have to basically predict what the net effect will be when it is materialized as aTransaction, and accepting or rejecting based on that prediction. It’s not impossible, but it’s a lot harder than it looks. Additionally, as with schemas, Yjs is built for an authority-less topology, so it has no native facilities built-in for permissions at all, at least as far as I can tell.

## You’re probably notjustusing a CRDT, so availability is not actually better

One of the things I constantly hear about Yjs is that it makes it easier to stay up when the server goes away. At this point, for most realistic apps, I am prepared to argue this is not true.

First off, modern text editors almost uniformly do many things other than just storing text. Stuff like:

Storing things in media servers, e.g., images you paste into a document

Checking permissions

Presence may or may not be a separate service

Durability (e.g., document might be stored in S3, operations in K/V storage, and so on)

Generally speaking, none of these services will be CRDTs, and if any of them go down (especially permissions), you are probably going to want to stop serving traffic.

This means that you are mainly using the CRDT as a networking protocol, rather than an availability strategy. You certainly can do that, but as I’ve said throughout this article, it is vastly less efficient and vastly more complicated than the alternative network protocol candidates.

## Tombstoning loses data or chews up all your RAM

The “simple” solution to collab editing stores all steps in durable storage. If you fall behind, you can retrieve them a call to the API equivalent ofchanges(lastSeenVersion). For reasonable requests, this is a fast and efficient way to catch a client up, and the client can forget all the steps once it’s incorporated them into itsEditorState.

Yjs, being designed for truly-masterless p2p topologies, generally can’t forget steps easily. In particular, if an item is deleted, it has to keep around a “tombstone”—a marker that records an item was deleted. This is because concurrent operations that reference a given item’s ID will reconcile incorrectly if the client can’t tell that the item was deleted.

The general solution is to garbage collect (GC) tombstones. But you can only really safely do this when all peers have deleted the item—and you can’t possibly know that, since we can’t distinguish between disconnected and slow clients. So you can either keep the tombstones around for longer (chewing up memory), or you can forget them after some arbitrary time, whichwilllose data. Yjs’s underlying protocol (calledYATA) GCs the tombstones at ~30s.

If you’re not in a truly-masterless p2p topology, this is a completely pointless trade-off.changes(lastSeenVersion)completely solves this problem and has absolutely none of these downsides. All you need is a database to store the steps.

## CRDTs are much, much harder to debug

I have now implemented collaborative text editors in pretty much all the ways you can. OT, CRDTs, withprosemirror-collab, withprosemirror-collab-commit, with locking. What I will say is that even a minor bug in the “simple” implementation withprosemirror-collabwill stretch you to the absolute edge of your sanity.

Like, as you are typing you will produce hundreds or thousands of updates a minute, and sometimes, your document will be missing a couple of characters that appear on the server.

But why? You won’t know. You won’t be logging the entire document every time (probably) so it will be very hard to track down the exact edit that corrupted the document. You’ll add logging, then go about your business, and when you run into it again you’ll spend 4 hours looking at the logs before you realize you’re missing another critical log line. One time this happened to me, and the problem was that I added anawait, but made some decisions on data I’d read before the suspense point, which was sometimes outdated by the time the transaction completed.

In the “simple” solution, you have many tools at your disposal that help ferret out these bugs. You can:

Attach idempotency keys to every request.

Dispatch every write request twice to flush out races.

Aggressively test the server for races.

But what if you’re using CRDTs? Well, all these problems are 100x harder, and none of these mitigations are available to you. Definitionally, the state is only guaranteed to converge. So how do you even know if something is transiently diverged, or simply incorrect? Of course, you can’t. Not really.

# … and I could go on…

At the beginning of this article, I told you that my goal is to convince you that, unless you trulyneeda truly-masterless peer-to-peer topology, you are better off using the “simple” solution. At this point, I think additional writing is probably not going to help my convince you.

I want to leave you with one other thing, though. And I’m especially talking to the library authors here: when you design a library,you have to start with the end-user experience you want to enable, not an algorithm.For us, it was very simple. We wanted users to be able to collaborate, be tolerant of disconnects, and always run at 60 fps. We wanted users to be able topredictwhat happens to their data.

When we set out to build this stuff, we assumed everyone had these goals. At the other end of this evaluation, though, it’s hard to imagine that we really did all have this in mind. If we did, the technology landscape in this area would look very different.

# Appendix