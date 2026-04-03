---
title: 16 Modern JavaScript Features That Might Blow Your Mind - DEV Community
url: https://dev.to/sylwia-lask/16-modern-javascript-features-that-might-blow-your-mind-4h5e
site_name: devto
content_file: devto-16-modern-javascript-features-that-might-blow-your
fetched_at: '2026-02-26T11:19:44.385802'
original_url: https://dev.to/sylwia-lask/16-modern-javascript-features-that-might-blow-your-mind-4h5e
author: Sylwia Laskowska
date: '2026-02-25'
description: Ah, what a time to be alive! As usual, I’ve taken way too much on my plate — there were just too many... Tagged with javascript, frontend, node.
tags: '#javascript, #frontend, #node'
---

Ah, what a time to be alive!As usual, I’ve taken way too much on my plate — there were just too many things that looked interesting 😄 Right now I feel like I have ten parallel storylines running in my life and not enough hands to handle them all.

But let’s be honest — I’m not going to skip my weekly post.That said… this time I won’t dare to go for a deep dive again. Let’s keep it lighter 😉

Some time ago, one of my posts got surprisingly popular:Stop Installing Libraries: 10 Browser APIs That Already Solve Your Problems

Apparently, these kinds of curated lists are something the community really needs.

Sure, we have documentation. Sure, we can Google everything — or ask Claude, GPT or Gemini. But there’s one small problem: before you can search for something, you first need to know that it exists.

So this time I decided to go through a handful of newer additions to the ECMAScript standard — features that landed in recent years and are already available in modern environments.

This topic isn’t new to me. Back in 2019, I gave a talk at meet.js Summit called “Beyond ES6 — What Comes After the Hype?” (or something along those lines 😄). If for some reason you’d like to revisit ECMAScript features from 2015–2019, you can probably still find the recording somewhere on YouTube.

Alright, enough intro.

Below you’ll find some of my favorite modern JavaScript features from recent years. I’m not listing everything — only the ones that feel practical, interesting, or quietly powerful.

And as you’ll see… they all connect into a bigger pattern.

## 📅 ES2022 — The Foundation of Modern JS

## ✨ Top-Levelawait

What problem it solves:A nice quality-of-life improvement. Before this, you couldn’t useawaitdirectly at the top level of a module. You had to wrap everything inside an async function just to load config or initialize data. Not the worst thing ever — but honestly a bit pointless.

Old way (extra boilerplate):

async

function

init
()

{


const

config

=

await

fetchConfig
();


startApp
(
config
);

}

init
();

Enter fullscreen mode

Exit fullscreen mode

Now:

const

config

=

await

fetchConfig
();

startApp
(
config
);

Enter fullscreen mode

Exit fullscreen mode

Why it matters:Cleaner startup logic, less ceremony, easier reading.

## 🔒 Private Class Fields (#)

What problem it solves:Let’s be honest — JavaScript never really had private class fields. We just pretended it did, creating weird conventions like_privateVar, which wasn’t private at all 😉 (well… unless you were using TypeScript).

Now:

class

User

{


#
id
;


constructor
(
id
)

{


this
.
#
id

=

id
;


}

}

Enter fullscreen mode

Exit fullscreen mode

Trying to accessuser.#idoutside the class throws an error.

Why it matters:Real encapsulation. Safer abstractions and fewer accidental modifications.

## 🧠Error.cause

What problem it solves:How many times have you lost half a day debugging because one error triggered another, but the connection between them was almost impossible to trace?

Old way:overwrite the error or manually attach metadata.

Now:

throw

new

Error
(
"
Failed to load data
"
,

{


cause
:

originalError

});

Enter fullscreen mode

Exit fullscreen mode

Why it matters:Better debugging and logging. You can track the full chain of failures instead of guessing.

## 🎯Object.hasOwn()

What problem it solves:Back in the day, checking if an object really had a property required creating this confusing monster:

Old way:

Object
.
prototype
.
hasOwnProperty
.
call
(
obj
,

"
key
"
);

Enter fullscreen mode

Exit fullscreen mode

Now:

Object
.
hasOwn
(
obj
,

"
key
"
);

Enter fullscreen mode

Exit fullscreen mode

Why it matters:Cleaner syntax, easier to read, fewer edge-case surprises.

## 📍.at()— Relative Indexing

What problem it solves:Classic junior interview question: how do you get the last element of an array? Everyone above junior level eventually learned the same ugly hack.

Old way:

arr
[
arr
.
length

-

1
];

Enter fullscreen mode

Exit fullscreen mode

Now:

arr
.
at
(
-
1
);

Enter fullscreen mode

Exit fullscreen mode

Why it matters:Maybe not revolutionary, but definitely clearer and more readable.

## 📅 ES2023 — The Immutability Upgrade

This release focuses on one big idea:avoid accidental mutation.

## 🧹toSorted()

Problem:Array.sort()is great… except it mutates the original array. Someone forgets that — and suddenly half your app is broken. Others remember, so they manually clone arrays every time.

Old workaround:

[...
arr
].
sort
();

Enter fullscreen mode

Exit fullscreen mode

Now:

const

sorted

=

arr
.
toSorted
();

Enter fullscreen mode

Exit fullscreen mode

What it changes:You get a sorted copy without touching the original data.

Why it matters:Huge for state management and functional-style code.

## 🔁toReversed()&toSpliced()

Same philosophy: copy instead of mutate.

arr
.
toReversed
();

arr
.
toSpliced
(
2
,

1
);

Enter fullscreen mode

Exit fullscreen mode

Why it matters:Predictability. You don’t accidentally break code sharing the same array reference.

## 🔎findLast()/findLastIndex()

Problem:We hadfind, but what if you wanted thelastmatching element? The old workaround was… not exactly pretty, and definitely confusing for juniors.

Old way:

[...
arr
].
reverse
().
find
(
fn
);

Enter fullscreen mode

Exit fullscreen mode

Now:

arr
.
findLast
(
fn
);

Enter fullscreen mode

Exit fullscreen mode

Why it matters:Less noise, clearer intent — the code says exactly what you mean.

## 📅 ES2024 — Data Transformation & Async Control

## 🧩Object.groupBy()

Problem:Grouping arrays usually meant writing reducers that looked more complex than the problem itself.

Old way:

users
.
reduce
((
acc
,

user
)

=>

{


(
acc
[
user
.
role
]

??=

[]).
push
(
user
);


return

acc
;

},

{});

Enter fullscreen mode

Exit fullscreen mode

Now:

const

grouped

=

Object
.
groupBy
(
users
,

u

=>

u
.
role
);

Enter fullscreen mode

Exit fullscreen mode

Why it matters:Massive readability upgrade. What used to be a helper function is now a one-liner.

## ⚡Promise.withResolvers()

Problem:Creating externalresolve/rejecthandlers was always awkward.

Old way:

let

resolve
;

const

promise

=

new

Promise
(
r

=>

resolve

=

r
);

Enter fullscreen mode

Exit fullscreen mode

Now:

const

{

promise
,

resolve
,

reject

}

=


Promise
.
withResolvers
();

Enter fullscreen mode

Exit fullscreen mode

Why it matters:Cleaner async orchestration — especially for queues, events, or complex flows.

## 📦 Resizable ArrayBuffer

Problem:Buffers used to have fixed sizes, which was frustrating when working with streaming or dynamic data — especially if you were one of those weirdos (like me 😄) experimenting with edge JavaScript, workers, or binary data.

const

buffer

=

new

ArrayBuffer
(
8
,

{


maxByteLength
:

16

});

Enter fullscreen mode

Exit fullscreen mode

Why it matters:More flexible memory handling for advanced scenarios.

## 📅 ES2025 — Functional JavaScript Gets Serious

## 🧠 Iterator Helpers

Problem:Array methods are great — but they create intermediate arrays at each step. Sometimes that’s unnecessary work.

Old way (creates extra arrays):

const

result

=

arr


.
map
(
x

=>

x

*

2
)


.
filter
(
x

=>

x

>

5
)


.
slice
(
0
,

3
);

Enter fullscreen mode

Exit fullscreen mode

Each step allocates a new array.

Now (lazy processing):

const

result

=

iterator


.
map
(
x

=>

x

*

2
)


.
filter
(
x

=>

x

>

5
)


.
take
(
3
)


.
toArray
();

Enter fullscreen mode

Exit fullscreen mode

What it replaces:Manual generator pipelines or performance-heavy array chains.

Why it matters:

* values are processed step by step (lazy evaluation)
* fewer allocations
* better performance on large datasets
* more functional-style pipelines

Think: streaming mindset instead of “build another array”.

## 🧩 New Set Methods

Problem:More advanced set logic always required custom helpers or awkward conversions to arrays.

Old way:

const

intersection

=

new

Set
(


[...
a
].
filter
(
x

=>

b
.
has
(
x
))

);

Enter fullscreen mode

Exit fullscreen mode

Now:

a
.
intersection
(
b
);

a
.
union
(
b
);

a
.
difference
(
b
);

Enter fullscreen mode

Exit fullscreen mode

Why it matters:Math-like operations directly in the language. Less boilerplate, clearer intent.

## 🔐RegExp.escape()

Problem:Security. Building regular expressions from user input could easily break the pattern or even introduce vulnerabilities.

Old way:

const

safe

=

userInput
.
replace
(
/
[
.*+?^${}()|[
\]\\]
/g
,

"
\\
$&
"
);

const

regex

=

new

RegExp
(
safe
);

Enter fullscreen mode

Exit fullscreen mode

Now:

const

regex

=

new

RegExp
(
RegExp
.
escape
(
userInput
));

Enter fullscreen mode

Exit fullscreen mode

Why it matters:Safer regex creation without writing your own helper every time.

## ⚡Promise.try()

Problem:Sometimes you want to treat sync and async code the same way — especially when a sync function might throw.

Now:

await

Promise
.
try
(()

=>

mightThrow
());

Enter fullscreen mode

Exit fullscreen mode

Why it matters:Everything becomes promise-based automatically, which simplifies error handling pipelines.

## 🧊 Float16 Support

JavaScript has always been a bit awkward with numbers — the default is 64-bit floating point. We’ve hadFloat32Arrayfor a while, which was already useful, but now JS goes one step further.

const

data

=

new

Float16Array
(
1024
);

Enter fullscreen mode

Exit fullscreen mode

What this actually means:

* smaller numeric representation (16-bit)
* lower memory usage
* faster data transfer in some GPU/ML scenarios

Why it matters:Graphics, WebGPU, machine learning, and performance-oriented workloads benefit from more compact data.

## 🧭 The Bigger Picture

If you zoom out, you’ll notice a pattern:

* less mutation
* clearer intent
* safer async handling
* more functional data processing

JavaScript isn’t changing through flashy revolutions anymore.It’s evolving through small, practical upgrades that quietly make everyday code cleaner and easier to reason about.

And honestly — that’s the kind of evolution I like most 🙂

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (27 comments)


Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
