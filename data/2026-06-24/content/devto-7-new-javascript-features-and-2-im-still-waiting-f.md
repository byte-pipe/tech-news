---
title: 7 New JavaScript Features (And 2 I'm Still Waiting For) - DEV Community
url: https://dev.to/sylwia-lask/7-new-javascript-features-and-2-im-still-waiting-for-2ck8
site_name: devto
content_file: devto-7-new-javascript-features-and-2-im-still-waiting-f
fetched_at: '2026-06-24T19:35:50.815850'
original_url: https://dev.to/sylwia-lask/7-new-javascript-features-and-2-im-still-waiting-for-2ck8
author: Sylwia Laskowska
date: '2026-06-24'
description: Remember how I promised you (or rather myself) two weeks ago that from now on I'd only write light,... Tagged with javascript, typescript, node, webdev.
tags: '#javascript, #typescript, #node, #webdev'
---

Upcoming ECMAScript 2026 standard updates

Remember how I promised you (or rather myself) two weeks ago that from now on I'd only write light, easy posts? Well… I broke that promise 😅 Last week I published a huge article about one of the least sexy topics imaginable: legacy applications. Somehow, despite that, the DEV editorial team liked it enough to include it in theTop 7 Posts of the Week❤️

But today is finally the day for something a bit lighter. And I think it's a topic that deserves more attention.

These days we spend a lot of time talking about AI agents, and I absolutely understand why, because it's a fascinating field. But I sometimes feel we're forgetting that the programming languages we use every day are evolving too.

I spend most of my days writing JavaScript (well… TypeScript, obviously 😄). And yes, the ecosystem has matured a lot over the last few years. We no longer have endless React vs Angular wars. We're also mostly past those times when everyone loved Redux one month and six months later decided it was an overengineered monster and removed it from every application 😅.

But both the ecosystem and the ECMAScript standard keep evolving.

After the legendary ES6 release in 2015, which changed frontend development forever, the TC39 committee switched to an iterative approach and started shipping new features every year.

And the nice thing is that if you're using modern browsers or runtimes, you often get access to these features almost immediately.

So, what do we get inECMAScript 2026?

Oh, and to keep things entertaining, all code examples in this article are based on the internal monologue of imaginary LinkedIn gurus with very strong opinions. Any resemblance to actual people is, naturally, purely coincidental 😇

Other articles from this series:

* Stop Installing Libraries: 10 Browser APIs That Already Solve Your Problems
* 9 Things You're Overengineering — The Browser Already Solved Them
* 16 Modern JavaScript Features That Might Blow Your Mind

## 1. Map.prototype.getOrInsert() / Upsert

MDN:https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/getOrInsert

This is one of those features that makes you wonder: "Wait… why didn't we have this ten years ago?"

Imagine we're collecting opinions from LinkedIn gurus. Until now, we had to do something like this:

const
 
opinions
 
=
 
new
 
Map
();

function
 
addOpinion
(
topic
,
 
author
)
 
{

 
if 
(
!
opinions
.
has
(
topic
))
 
{

 
opinions
.
set
(
topic
,
 
[]);

 
}

 
opinions
.
get
(
topic
).
push
(
author
);

}

addOpinion
(
"
React is dead
"
,
 
"
10x Engineer
"
);

addOpinion
(
"
React is dead
"
,
 
"
Principal AI Evangelist
"
);

Enter fullscreen mode

Exit fullscreen mode

It works, but there's quite a bit of boilerplate.

With ES2026, things become much nicer:

const
 
opinions
 
=
 
new
 
Map
();

opinions

 
.
getOrInsert
(
"
React is dead
"
,
 
[])

 
.
push
(
"
10x Engineer
"
);

opinions

 
.
getOrInsert
(
"
React is dead
"
,
 
[])

 
.
push
(
"
Principal AI Evangelist
"
);

console
.
log
(
opinions
);

Enter fullscreen mode

Exit fullscreen mode

We also get a computed version:

const
 
opinions
 
=
 
new
 
Map
();

opinions

 
.
getOrInsertComputed
(

 
"
Nobody writes clean code anymore
"
,

 
()
 
=>
 
[]

 
)

 
.
push
(
"
DDD Purist
"
);

Enter fullscreen mode

Exit fullscreen mode

Come on, that's so much cleaner and easier to read. It's also perfect for caching! Much less code, much nicer API.

## 2. Iterator.concat()

MDN:https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator/concat

Before we talk aboutconcat(), let's quickly answer a question:

### What is an iterator?

An iterator is basically a cursor that lets us consume data one element at a time without storing everything in memory.

For example:

const
 
posts
 
=
 
[

 
"
Angular is dead
"
,

 
"
JavaScript was a mistake
"

];

const
 
iterator
 
=
 
posts
.
values
();

console
.
log
(
iterator
.
next
());

// { value: "Angular is dead", done: false }

console
.
log
(
iterator
.
next
());

// { value: "JavaScript was a mistake", done: false }

console
.
log
(
iterator
.
next
());

// { value: undefined, done: true }

Enter fullscreen mode

Exit fullscreen mode

And because iterators are lazy, we can even generate infinite sequences without blowing up memory:

function
*
 
endlessHotTakes
()
 
{

 
while 
(
true
)
 
{

 
yield
 
"
Everything should be rewritten in Rust.
"
;

 
}

}

const
 
iterator
 
=
 
endlessHotTakes
();

console
.
log
(
iterator
.
next
().
value
);

console
.
log
(
iterator
.
next
().
value
);

console
.
log
(
iterator
.
next
().
value
);

Enter fullscreen mode

Exit fullscreen mode

Last year we got Iterator Helpers, which introduced things likemap(),filter(), and friends:

function
*
 
linkedinFeed
()
 
{

 
yield
 
"
Use Rust for everything
"
;

 
yield
 
"
JavaScript was a mistake
"
;

 
yield
 
"
Clean code is dead
"
;

 
yield
 
"
Angular is dead
"
;

}

const
 
controversialTakes
 
=

 
linkedinFeed
()

 
.
filter
(
post
 
=>
 
post
.
includes
(
"
dead
"
))

 
.
map
(
post
 
=>
 
`🔥 
${
post
}
`
);

console
.
log
([...
controversialTakes
]);

Enter fullscreen mode

Exit fullscreen mode

And now we get another nice addition:Iterator.concat(). Suppose frontend gurus and backend gurus each have their own stream of wisdom:

function
*
 
frontendExperts
()
 
{

 
yield
 
"
React is dead
"
;

 
yield
 
"
Nobody needs Redux
"
;

}

function
*
 
backendExperts
()
 
{

 
yield
 
"
Microservices solve everything
"
;

 
yield
 
"
Frontend developers don't understand architecture
"
;

}

Enter fullscreen mode

Exit fullscreen mode

Now we can combine them elegantly:

const
 
feed
 
=
 
Iterator
.
concat
(

 
frontendExperts
(),

 
backendExperts
()

);

console
.
log
([...
feed
]);

Enter fullscreen mode

Exit fullscreen mode

In my opinion, these iterator features don't get nearly as much attention as they deserve.

## 3. Array.fromAsync()

MDN:https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/fromAsync

This is basically the async equivalent of our belovedArray.from().

It's primarily designed for async iterators, although I suspect that most JavaScript developers don't use async iterators every day. For example, imagine comments arriving one by one from LinkedIn:

async
 
function
*
 
angryComments
()
 
{

 
yield
 
"
This could have been a plain HTML form.
"
;

 
yield
 
"
Angular is dead.
"
;

 
yield
 
"
React is dead.
"
;

 
yield
 
"
JavaScript was a mistake.
"
;

}

const
 
comments
 
=
 
await
 
Array
.
fromAsync
(

 
angryComments
()

);

console
.
log
(
comments
);
 

// This could have been a plain HTML form.

// Angular is dead.

// etc

Enter fullscreen mode

Exit fullscreen mode

But here's something many people don't realize: it also works with promises.

const
 
opinions
 
=
 
[

 
Promise
.
resolve
(
"
Nobody should use classes.
"
),

 
Promise
.
resolve
(
"
Signals change everything.
"
),

 
Promise
.
resolve
(
"
Microservices ruined software.
"
)

];

const
 
takes
 
=
 
await
 
Array
.
fromAsync
(
opinions
);

console
.
log
(
takes
);
 

Enter fullscreen mode

Exit fullscreen mode

And you can even map values immediately:

const
 
comments
 
=
 
await
 
Array
.
fromAsync
(

 
angryComments
(),

 
opinion
 
=>
 
opinion
.
toUpperCase
()

);

console
.
log
(
comments
);

Enter fullscreen mode

Exit fullscreen mode

Pretty convenient.

## 4. Math.sumPrecise()

MDN:https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/sumPrecise

This one solves a floating-point problem that's almost as old as the Internet itself 😄 As many of you probably know, in JavaScript:

console
.
log
(
0.1
 
+
 
0.2
);

// 0.30000000000000004

Enter fullscreen mode

Exit fullscreen mode

I won't dive into why that happens today: we'd be here all night 😄

The important thing is that ES2026 introducesMath.sumPrecise(), which performs much more accurate summation and avoids the accumulation of rounding errors.

Suppose a LinkedIn guru is listing all the things that allegedly increase productivity:

const
 
productivityBoosts
 
=
 
[

 
0.1
,
 
// cold showers

 
0.2
,
 
// AI agents

 
0.3
,
 
// journaling

 
0.4
,
 
// waking up at 4 AM

];

console
.
log
(

 
Math
.
sumPrecise
(
productivityBoosts
)

);

Enter fullscreen mode

Exit fullscreen mode

Now, to be fair, most frontend developers will probably never need this. Plain old addition works perfectly fine for everyday use.

But if you're working in finance, statistics, simulations, or AI/ML, where tiny errors can accumulate over thousands or millions of operations, this becomes much more interesting.

## 5. Error.isError()

MDN:https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/isError

This one is probably aimed more at library authors and advanced developers. Or maybe not? 😉 Until now, checking whether something was actually an error usually looked like this:

try
 
{

 
throw
 
new
 
Error
(

 
"
Angular is dead.
"

 
);

}

catch 
(
e
)
 
{

 
console
.
log
(

 
e
 
instanceof
 
Error

 
);

}

Enter fullscreen mode

Exit fullscreen mode

And most of the time, that worked perfectly fine. Until it didn't.

If an error originated in another realm, for example an iframe, a Web Worker, or a VM context—instanceof Errorcould suddenly betray you:

const
 
strangeThing
 
=

 
window
.
frames
[
0
].
eval
(

 
"
new Error('JavaScript was a mistake.')
"

 
);

console
.
log
(

 
strangeThing
 
instanceof
 
Error

);

// false 

Enter fullscreen mode

Exit fullscreen mode

This problem has been annoying library authors for years, which is why many frameworks and libraries have their own helper functions for detecting errors. Now we finally get a built-in solution:

console
.
log
(

 
Error
.
isError
(
strangeThing
)

);

// true

Enter fullscreen mode

Exit fullscreen mode

Simple and beautiful.

## 6. Base64 for Uint8Array

MDN:https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/toBase64

Quick reminder: Base64 is simply a way of converting binary data into plain text. Why would we do that? Because many protocols and formats are much happier dealing with text than raw bytes. For example, we might send an image as a Base64 string.

Now, someone might say: "Wait a minute, Base64 already existed in JavaScript!" And yes, it did. But it mostly worked with strings:

btoa
(
"
JavaScript was a mistake.
"
);

Enter fullscreen mode

Exit fullscreen mode

When dealing with binary data, things quickly became ugly:

const
 
bytes
 
=
 
new
 
Uint8Array
(
buffer
);

const
 
base64
 
=
 
btoa
(

 
String
.
fromCharCode
(...
bytes
)

);

Enter fullscreen mode

Exit fullscreen mode

Not terrible, but definitely not something you'd call elegant.

Now we can simply write:

const
 
screenshot
 
=

 
await
 
fetch
(

 
"
/proof/react-is-dead.png
"

 
);

const
 
bytes
 
=

 
new
 
Uint8Array
(

 
await
 
screenshot
.
arrayBuffer
()

 
);

const
 
base64
 
=

 
bytes
.
toBase64
();

console
.
log
(
base64
);

Enter fullscreen mode

Exit fullscreen mode

Much cleaner. And, perhaps more importantly, much easier to understand six months later.

## 7. JSON.parse Source Text Access

MDN:https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse

JSON.parse()is great. Until somebody sends you a gigantic number. Suppose a LinkedIn guru claims to have 999 trillion followers:

const
 
json
 
=
 
`
{
 "followers":
 999999999999999999999999999999
}
`
;

const
 
data
 
=
 
JSON
.
parse
(
json
);

console
.
log
(
data
.
followers
);

Enter fullscreen mode

Exit fullscreen mode

Oops. JavaScript numbers have limits, and very large integers may lose precision.

With ES2026, the reviver callback gets access to the original source text, allowing us to recover huge values safely:

const
 
data
 
=
 
JSON
.
parse
(

 
json
,

 
(
key
,
 
value
,
 
context
)
 
=>
 
{

 
if 
(
key
 
===
 
"
followers
"
)
 
{

 
return
 
BigInt
(
context
.
source
);

 
}

 
return
 
value
;

 
}

);

console
.
log
(
data
.
followers
);

Enter fullscreen mode

Exit fullscreen mode

No more accidental corruption of giant numbers.

Most of us won't need this every day. But if you're dealing with IDs, financial data, or huge integer values, this can save you from some nasty bugs.

## Bonus: The Great Absentees

I was really hoping these features would make it into ES2026, but unfortunately we'll have to wait another year.

Well, sort of. Modern browsers and runtimes have already started implementing them, but they are not officially part of the ECMAScript 2026 specification yet.

These are probably the two features I'm personally most excited about.

## Temporal API

TC39 proposal:https://github.com/tc39/proposal-temporal

If you've been doing frontend development long enough, chances are you've had at least one traumatic experience involving dates. Maybe something like this:

const
 
date
 
=
 
new
 
Date
(
"
2026-03-30
"
);

console
.
log
(
date
);

Enter fullscreen mode

Exit fullscreen mode

Depending on your timezone, congratulations! You've just entered the exciting world of: "Why is it yesterday?"

Or perhaps you've experienced everyone's favorite:

const
 
today
 
=
 
new
 
Date
();

today
.
setMonth
(
today
.
getMonth
()
 
+
 
1
);

Enter fullscreen mode

Exit fullscreen mode

And suddenly you're debugging why March plus one month somehow became May.

Or maybe you've been lucky enough to deal with time zones.

At which point you discover that time itself is apparently an illusion and that daylight saving time was invented specifically to ruin programmers' lives.

This is why many of us ended up using libraries like Moment.js. Ironically, even the Moment.js maintainers now recommend using other solutions. Then came date-fns, Luxon, and various other attempts to restore sanity.

They certainly help. Until somebody says: "By the way, users in Australia are reporting weird bugs." And that's usually where the fun begins.

Temporal aims to fix all of this by introducing proper date and time types.

Instead of:

const
 
now
 
=
 
new
 
Date
();

Enter fullscreen mode

Exit fullscreen mode

we get things like:

const
 
now
 
=
 
Temporal
.
Now
.
instant
();

const
 
birthday
 
=

 
Temporal
.
PlainDate
.
from
(

 
"
1987-07-23
"

 
);

const
 
meeting
 
=

 
Temporal
.
ZonedDateTime
.
from
(

 
"
2026-11-03T10:00:00[Europe/Warsaw]
"

 
);

Enter fullscreen mode

Exit fullscreen mode

And suddenly everything becomes much more explicit.

By the way, I spent an embarrassing amount of time trying to figure out whether Temporal had actually made it into ES2026. Eventually, I found the TC39 repository, where it clearly says that although the proposal has already reached Stage 4, its expected publication year is 2027.

So we're close. Very close. And I can't wait ❤️

## Explicit Resource Management (using)

TC39 proposal:https://github.com/tc39/proposal-explicit-resource-management

This is one of those features that C# and Python developers have been quietly enjoying while the rest of us pretended thattry/finallywas perfectly fine 😄

Sometimes you create something that needs cleaning up afterward: file, database connection, stream, WebSocket, etc. Today, we usually write something like this:

const
 
webinar
 
=

 
createAIAgentsWebinar
();

try
 
{

 
webinar
.
start
();

}

finally
 
{

 
webinar
.
close
();

}

Enter fullscreen mode

Exit fullscreen mode

Thefinallyblock is often written with the same enthusiasm as unit tests. Worse, if we forget it entirely, we may end up with resource leaks and mysterious bugs.

Withusing, cleanup happens automatically when leaving the scope:

using
 
webinar
 
=

 
createAIAgentsWebinar
();

webinar
.
start
();

Enter fullscreen mode

Exit fullscreen mode

Once we leave the scope, JavaScript automatically calls the cleanup logic. How cool is that?

It's one of those features that might not affect the average frontend developer every day, but for Node.js developers, library authors, and people working with streams and files, it can be incredibly useful.

## Uff...

I have to admit, this article turned out to be way more work than I originally expected 😅 It was supposed to be short and easy. And somehow I ended up digging through TC39 proposals, MDN pages, browser implementations, and trying to figure out whether Temporal had actually made it into ES2026 or not.

But I hope it was worth it and that you enjoyed it ❤️

What about you? Which feature surprised you the most? And are you also eagerly waiting for Temporal to finally free us from all date-related suffering?

(Or at least that's what the LinkedIn gurus will probably tell us next week 😇)

If you enjoyed this article, feel free to connect with me onLinkedIn😊

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (17 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse