---
title: The Grand Unifying Architecture of Frontend - DEV Community
url: https://dev.to/playfulprogramming/the-grand-unifying-architecture-of-frontend-bhk
site_name: devto
content_file: devto-the-grand-unifying-architecture-of-frontend-dev-co
fetched_at: '2026-09-23T15:19:26.524975'
original_url: https://dev.to/playfulprogramming/the-grand-unifying-architecture-of-frontend-bhk
author: Ryan Carniato
date: '2026-09-22'
description: I used to joke that the history of frontend development could be retraced by following the argument... Tagged with webdev, javascript, solidjs, architecture.
tags: '#webdev, #javascript, #solidjs, #architecture'
---

I used to joke that the history of frontend development could be retraced by following the argument of who owned the state. And the truth is both sides have gone back and forth on this over the years. We started on the document web where state was on the server. Then we added JavaScript and Applets where we could have stateful things in the client. But developers at the time didn't like either much and tried to wire state across both sides in their server languages and we got ASP.NET and the like.

I sit here over 30 years later and it is still going on. Going to replace your React app with HTMX? Maybe. Maybe it isn't that simple. Although this seems like an endless spiral, I don't think this is unsolvable. Even though it has been going on so long, I actually think the answer is in front of us.

The unified model comes down to understanding responsibilities. And they are as old as the web itself. Every time we misalign complexity soars. Every time we ignore part of the puzzle it goes on to bite us. Every solution straddles part of this solution space but we've struggled to cover the whole range.

## Core Responsibilities

My observation is that all frontend architectures come down to layering of three responsibilities. Some are more present than others but they all exist in some form.

#### 1. Navigation (client)

The URL is the basis of the web experience and it belongs to the browser. Orchestration is a client responsibility and every solution from SPA to HTML partial agrees with this. JavaScript in the browser is the root of our application.

#### 2. Content (server)

Conversely, content belongs to the server whether it is markup or JSON. The server is the authoritative source. It hangs off of our navigation.

#### 3. Affordances (client)

Affordances find us back in the browser. Local UI state, in progress work, optimistic updates. We need to provide our user feedback faster than a round-trip to the server.

## Following the Shape

All web application architectures follow this client -> server -> client layering. A user navigates or performs an action, content comes back from the server, and the client settles it. That's the Single Page Application(SPA) architecture after load, but it's also HTMX. And also LiveView, if the server -> client protocol is powerful enough.

It feels like I'm stating the obvious here. But the web generally maps writes to navigation, and the server only pushes reads. Mutations travel through layer 1 with forms, actions, invalidation, and requests for the content. Layer 2, content, never writes and only publishes.

This asymmetry is what makes it composable. Breaking that leads to two stateful systems fighting against themselves. Which is why affordances like optimism(layer 3) fit cleanly on top if viewed as an overlay. The client never writes server content directly as it doesn't own it.

## Revisiting the Spectrum

I've tried many times to map the solution space to a 4 quadrant grid but I never found the right axis. But I'm now seeing how all solutions can sit in the same diagram.

Obviously this is a rough placement, solutions fit spaces not points, and something like React can be used as a frontend in a sync engine like Zero. Here React represents classic SPAs + JSON API. But most frameworks fix both transport and affordance weight so they don't move much.

But if you put it under our lens of responsibility:

* HTMX: Minimal layer 1, HTML carries the majority of the work under layer 2, and layer 3 is almost nothing.
* LiveView: Layer 2 expands its capability, while layer 3 remains nearly non-existent. Same dance with the read window stretched to the length of the session.
* DataStar: More machinery in layer 2 with the addition of server populated Signals allowing for some closer interaction with the client.
* Astro(+ View Transitions): navigation(view transition) -> server(markup) -> client(islands). All 3 parts laid out explicitly.
* Server Components(Next.js): Like Astro except shared client state is preserved.
* SPA + JSON(React): Layer 3 grows until it merges with layer 1. And layer 2 is delegated to JSON APIs.
* Sync Engine(Zero): Layer 2 becomes a persistent read of a replicated store, and layer 3 grows to hold a full local copy of it. Optimism over the whole dataset.

Every solution, with a bit of coaxing, is capable of expressing all of these. They differ in transport, window length, and how much affordance code you ship. So it comes down to efficiency and authoring. Which means one framework could cover it all, if each responsibility is adjustable.

## A Modern Take

Nothing I've laid out is any different than how the base platform has always worked, but can we mirror this in a way that encompasses the full spectrum of the past 30 years?

I'm going to paint a picture using our 3 responsibilities with Solid 2.0.

### Navigation: Delegation and progressive enhancement

Solid's router owns nothing in the render tree. There is no<Link>(or<A>) component. Instead our JSX compiler registers a claim on everya[href]andform[action]element it creates, and server-streamed content gets the same claims swept over any subtree the runtime renders.

// lib/users.ts

export
 
const
 
renameUser
 
=
 
action
(

 
async 
(
id
:
 
string
,
 
formData
:
 
FormData
)
 
=>
 
{

 
"
use server
"
;

 
updateUser
(
id
,
 
{
 
name
:
 
String
(
formData
.
get
(
"
name
"
))
 
});

 
}

);

// routes/users/[id].tsx — plain HTML. The compiler claims the

// anchor and the form. The router intercepts both. Works before 

// hydration and after.

<
a
 
href
=
{
`/users/
${
id
}
`
}
>
{
user
().
name
}
<
/a
>

<
form
 
action
=
{
renameUser
.
with
(
id
)}
 
method
=
"
post
"
>

 
<
input
 
name
=
"
name
"
 
value
=
{
user
().
name
}
 
/
>

 
<
button
>
Rename
<
/button
>

<
/form
>

Enter fullscreen mode

Exit fullscreen mode

Note: There are no components in this markup.

A SolidJS router consumes those claims to managearia-current, active classes, and interception. This means server-rendered markup with zero client components participates fully in client-side navigation. So it works not only with "No JS" but with JavaScript with no interactive components.

Forms and buttons delegate to server function actions the same way. You hoist your preloads and invalidation correctly and single-flight mutations mean one round trip settles every piece of UI the mutation invalidated whether that UI is JSON-fed client components or server-owned markup.

### Content: Reactive reads over the wire

Solid's powerful protocol for layer 2 stands on our"use server"functions. Solid serializes across the boundary with Seroval, which handles not just plain data but async structures, like Promises and async iterators. The communication between server and client is about the data, including data that hasn't settled yet.

export
 
async
 
function
 
report
(
id
:
 
string
)
 
{

 
"
use server
"
;

 
return
 
{

 
title
:
 
await
 
getTitle
(
id
),

 
// AsyncIterable<string> — crosses the wire as-is

 
progress
:
 
watchProgress
(
id
),
 
 
};

}

// client: the iterable's latest yield is just a reactive read

const
 
r
 
=
 
createMemo
(()
 
=>
 
report
(
props
.
id
));

const
 
progress
 
=
 
createMemo
(()
 
=>
 
r
().
progress
);

<
h1
>
{
r
().
title
}
<
/h1
>

<
p
>
{
progress
()}
<
/p
>

Enter fullscreen mode

Exit fullscreen mode

More than that, the reactive graph propagates over the wire. On the server, every expression feeding the client is an open binding for the life of the response. When a promise settles or iterator yields the server re-runs the expression and sends the new value to the client to be replaced or morphed.

So far I've showcased this in examples around the original response, ie what happens during hydration. Even if the content chunks stream in as they initially are ready, we can continue to update the stream in place as long as the request stays open.

But the same can be true of server function requests after the fact. We can send back would-be static markup, "Server Components", and have their reactive graph never ship to the client while still doing these streamed pinpoint updates. We will be announcing the preview for our Server Component feature soon (but if you look you can already seefully workingexamplesin our repo).

export
 
async
 
function
 
countdown
(
n
:
 
number
)
 
{

 
"
use server
"
;

 
const
 
ticks
 
=
 
tick
(
n
);
 
// AsyncIterable<number>, one per second

 
// returning a function returns a Server Component

 
return 
()
 
=>
 
{

 
const
 
count
 
=
 
createMemo
(()
 
=>
 
ticks
);

 
return
 
<
p
>
Counted
 
to
 
{
count
()}
 
of
 
{
n
}
<
/p>
;

 
};

}

// client — zero component code ships for this

const
 
Counter
 
=
 
dynamic
(()
 
=>
 
countdown
(
10
));

<
Counter
 
/>

Enter fullscreen mode

Exit fullscreen mode

Because the communication is one-way with a single authoring model, the transport is pluggable. Today we use Request/Response, so it lives as long as the request is open and you reconnect as needed. Swap in something persistent like SSE or a socket and the same server component becomes a non-terminating live component.

// request/response — left side of the grid

export
 
const
 
getAuction
 
=
 
GET
(
async 
()
 
=>
 
{

 
"
use server
"
;

 
return
 
read
();

});

// persistent — right side of the grid

export
 
const
 
liveAuction
 
=
 
live
(
async
 
function
*
 
()
 
{

 
"
use server
"
;

 
while 
(
true
)
 
{
 
yield
 
read
();
 
await
 
changed
();
 
}

});

// the consumer doesn't care which one it got

const
 
[
auction
]
 
=
 
createOptimisticStore
(()
 
=>
 
liveAuction
(),
 
{});

Enter fullscreen mode

Exit fullscreen mode

What makes this safe is what LiveView's failure mode teaches us:The server's live graph must be a re-derivable projection of durable state.It is never the source of truth. Reconnection doesn't depend on sessions, event replay, or anything that dies with a process.

### Affordances: An async-aware graph that hydrates once

This is an area SolidJS has excelled in. But in 2.0, async became native to the graph. A value arriving from the server content channel and a value computed locally are indistinguishable to the consumer.

Optimism is a first-class primitive. It isn't just something bundled with the server functions or query caching library. Optimism represents any uncommitted state predicted over async, whatever the async source. It's a general concept. It doesn't just represent what some might consider "lying to the user", it doesn't have to masquerade as an invisible success. It represents any predictive ephemeral affordance. It either settles eventually as truth or it is reverted, but it never outlives its transaction. It prevents getting out of sync.

const
 
[
auction
,
 
setAuction
]
 
=
 
createOptimisticStore
(()
 
=>
 
liveAuction
(),
 
{});

const
 
placeBid
 
=
 
action
(
function
*
 
(
amount
:
 
number
)
 
{

 
// overlay — reverts on settle

 
setAuction
(
a
 
=>
 
{
 
a
.
highBid
 
=
 
amount
 
});

 
// mutation - the write goes up

 
yield
 
bid
(
amount
);

 
// hold until truth comes back down 

 
yield
 
until
(()
 
=>
 
auction
.
highBid
 
>=
 
amount
);

});

Enter fullscreen mode

Exit fullscreen mode

This all works because wenever hydrate more than once.After startup, the server should never render a client component as client state has diverged from anything the server could know. This is a critical naive breaking point in HTML Partial and Islands solutions that share client state. Hydrating after state has updated is a recipe for hydration mismatches. While we can safeguard during the initial streaming progression, that isn't a realistic proposition over the life of an application.

A rule like that only holds if the system enforces it. Every piece of server content is keyed by the call that produced it, the function and its arguments, the same key a query cache would use. Content arriving on any transport only ever writes to that address's store, and mounted UI pulls from the address it's bound to. There is no direct connection from the network to the DOM. So a hover preload can't clobber the page you're looking at, a refetch morphs in place while the client-owned ranges inside it survive, and a stale response doesn't pass a version check.

Under this unified model, initial load gets the same treatment without paying serialization twice. Client components claim their server-rendered nodes and boot makes zero requests. The only serialized records are values the client requires. Server-only content ships as HTML or as data, never both. The page markup is the payload. For server components, that means always one copy. View-source and search for any piece of content and you'll find it exactly once.

I once positioned this as "Facing Frontend's Existential Crisis", but now it is a solved problem.

## Traversing the Spectrum

What makes this exciting is with the pieces above you are completely free to move the whole solution space and every point in between.

If you start in the lower left corner, that would be like a SolidJS app with no client components that just swaps server component chunks on server"use server"actions bound to<form action>. Server markup streams and morphs, and navigation is handled without any client components.

The top left-hand side is when we extend layer 3 until it dominates and you have the SPA and there are no server components or server rendering at all. Just JSON APIs.

And we can continue to traverse over the top to the right-hand side by the way of persistent"use server"functions and our granular optimistic layer. Solid'sliveanduntiloperators help close the gap when the client state is streamed in as available. I'd still use a dedicated sync engine, but the base primitives alone do a good impression.

Finally, the lower right corner, is closer to where we started. Except this time our server components have reactive bindings and their connection is persistent. No client components, just our same "use server" action protocol to write back, while our reads stream fine-grained markup partials over the wire. In this world, even the server components could be optimistic depending on how you write your actions, anduntilagain gives us a mechanism for completion acknowledgements.

The incredible part is that this required nothing that users of Solid 2.0 aren't already familiar with. Async Signals anduse server. With that, all these experiences are authorable using basically the same patterns, in the same framework, even in the same application.

## Conclusion

It goes back to where we started. A few pieces that have been sitting in front of us this whole time.

The browser owns navigation and affordances. The server owns content. Communication is a loop with writes travelling as navigation and content travelling as one-way reads. And the transport and the response window should be configurable without changing the shape of authoring.

Everything from HTMX to LiveView to islands to the SPA is a coordinate on this grid. The differences between them are efficiency and ergonomics rather than expressiveness.

What makes this more than an exercise in categorization is that all the hard pieces are built. We serialize and hydrate once. The reactive graph serializes its own updates. Content is stored by address, so stale hydration can't be represented.

It comes as little surprise to me that Signals can act as that common representation on all sides. Sync and async. Server and client. Stateful and stateless.

This is stupidly ambitious. RSCs only aimed to provide the left half of the grid and many felt they still fell short. The HTML-over-the-wire camp has aimed to provide the bottom half, but ignoring the client is ignoring an entire responsibility.

And yet, this is a future that I want to live in. One where choosing a framework doesn't require you to choose a religion. And one, from my perspective, that is already here.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse