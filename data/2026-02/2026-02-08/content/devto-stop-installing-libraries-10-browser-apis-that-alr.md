---
title: 'Stop Installing Libraries: 10 Browser APIs That Already Solve Your Problems - DEV Community'
url: https://dev.to/sylwia-lask/stop-installing-libraries-10-browser-apis-that-already-solve-your-problems-35bi
site_name: devto
content_file: devto-stop-installing-libraries-10-browser-apis-that-alr
fetched_at: '2026-02-08T11:09:38.770019'
original_url: https://dev.to/sylwia-lask/stop-installing-libraries-10-browser-apis-that-already-solve-your-problems-35bi
author: Sylwia Laskowska
date: '2026-02-04'
description: The web platform is way more powerful than most developers realize — and every year it quietly gains... Tagged with webdev, frontend, javascript.
tags: '#webdev, #frontend, #javascript'
---

The web platform is way more powerful than most developers realize — and every year it quietly gains new superpowers.

Sometimes choosing a topic is harder than writing the article itself.

When I thought about what to write this week, only two types of ideas kept comming to mind:either potentialbangers, or deep technical dives.😅 But I wanted something lighter. Still technical, still useful. But not a 3-day research rabbit hole.

And since I genuinely love exploring what the browser can do (and how far we can push it), I landed on a sneaky topic:underused Web APIs.

Some of these might be daily bread for you.But I’m pretty sure at least a few will make someone go “wait, this exists?!” 😉

And if you enjoy edge-tech topics and happen to be in Italy this April — come tojsday.it, where I’ll be speaking about WebGPU + WASM 🙂

Alright, enough intro. Let’s start.

Here are 10 browser APIs that deserve way more love.

## 1) Structured Clone API

I have a love–hate relationship with this one.

For years, one of my favorite interview questions to ask candidates was:

“How do you copy an object?”

You could learnso muchfrom the answer:

* Do they understand references?
* Do they knowObject.assign, spread, JSON tricks?
* Do they mention libraries?
* Do they panic? 😄

Now?

const

copy

=

structuredClone
(
original
);

Enter fullscreen mode

Exit fullscreen mode

Boom. Perfect deep copy.

Part of me is happy.Part of me misses that interview question already.

### Nice extras

* Works withMap,Set,Date,Blob,File,ArrayBuffer
* Handles circular references (no more JSON stringify explosions 💥)
* Does NOT clone functions

Support: Modern browsers (Chrome, Firefox, Safari, Edge). Safe for production.

## 2) Performance API

Very underrated.

We talk a lot about performance. We install tools. We run Lighthouse. We debate optimizations.

But sometimes you just want to check:“Is A actually faster than B, or am I overengineering?”

performance
.
mark
(
"
start
"
);

// code to measure

performance
.
mark
(
"
end
"
);

performance
.
measure
(
"
calc
"
,

"
start
"
,

"
end
"
);

console
.
log
(
performance
.
getEntriesByName
(
"
calc
"
));

Enter fullscreen mode

Exit fullscreen mode

Perfect for:

* micro-benchmarks
* checking if a Worker or WASM is worth it
* reality-checking your assumptions

Because sometimes the “optimized” version is slower 😅

Support: Excellent across all modern browsers.

## 3) Page Visibility API

Detects whether the tab is active.

document
.
addEventListener
(
"
visibilitychange
"
,

()

=>

{


if
(
document
.
hidden
)

{


video
.
pause
();


}

});

Enter fullscreen mode

Exit fullscreen mode

Real talk:Users will open your app, then switch tabs for 20 minutes.Or 2 hours.Or forever.

Use cases:

* pause videos
* stop polling
* reduce CPU usage
* cleaner analytics

Your backend (and battery life) will thank you.

Support: All modern browsers.

## 4) ResizeObserver

Finally — observingelement size, not just window size.

const

ro

=

new

ResizeObserver
(
entries

=>

{


for
(
const

entry

of

entries
)

{


console
.
log
(
entry
.
contentRect
.
width
);


}

});

ro
.
observe
(
element
);

Enter fullscreen mode

Exit fullscreen mode

If you ever built responsive components, charts, or dashboards, you probably wrote some cursed resize logic in the past.

This API feels like the browser saying:“Relax, I got you now.”

Support: Modern browsers, widely available.

## 5) IntersectionObserver

The sibling of ResizeObserver.

Checks if an element is in the viewport.

const

io

=

new

IntersectionObserver
(
entries

=>

{


entries
.
forEach
(
entry

=>

{


if
(
entry
.
isIntersecting
)

{


console
.
log
(
"
Visible!
"
);


}


});

});

io
.
observe
(
element
);

Enter fullscreen mode

Exit fullscreen mode

Amazing for:

* infinite scroll
* lazy loading
* scroll animations

Anyone who implemented infinite scroll manually once…never wants to do it again 😄

Support: All modern browsers.

## 6) AbortController

Many devs know it for fetch…

But it can cancelmore than just fetch.

const

controller

=

new

AbortController
();

fetch
(
url
,

{

signal
:

controller
.
signal

});

// later

controller
.
abort
();

Enter fullscreen mode

Exit fullscreen mode

You can also use it for:

* event listeners
* streams
* any abortable API

Even better:👉 One signal can cancel multiple operations.

Clean, scalable, and very “grown-up codebase” friendly.

Support: All modern browsers.

## 7) Idle Detection API

Page Visibility tells you if the tab is active.Idle Detection tells you if thehuman is active.

const

detector

=

new

IdleDetector
();

await

detector
.
start
();

detector
.
addEventListener
(
"
change
"
,

()

=>

{


console
.
log
(
detector
.
userState
);

});

Enter fullscreen mode

Exit fullscreen mode

Meaning:User might have your app open…but is actually making coffee ☕ or in a meeting.

Use cases:

* auto-logout
* “away” status
* background optimizations

Yes, you can detect if the user left the computer.A bit creepy. Very useful 😄

Support: Mostly Chromium-based. Requires permission.

## 8) BroadcastChannel API

Easy multi-tab communication.

const

channel

=

new

BroadcastChannel
(
"
app
"
);

channel
.
postMessage
(
"
logout
"
);

channel
.
onmessage

=

e

=>

{


console
.
log
(
e
.
data
);

};

Enter fullscreen mode

Exit fullscreen mode

Great for:

* logout sync
* auth state
* shared session logic

Surprisingly practical in real apps where users open 5 tabs “just in case.”

Support: Modern browsers. Safari joined later but supports it.

## 9) Web Locks API

The cousin of BroadcastChannel.

Prevents duplicate work across tabs.

navigator
.
locks
.
request
(
"
data-lock
"
,

async

lock

=>

{


await

fetchData
();

});

Enter fullscreen mode

Exit fullscreen mode

Example:

* only one tab fetches notifications
* avoids backend spam
* coordinates shared resources

Feels very “distributed systems meets frontend.”

Support: Mostly Chromium. Not universal.

## 10) File System Access API

Yes — real filesystem access from the browser.

const

[
fileHandle
]

=

await

window
.
showOpenFilePicker
();

const

file

=

await

fileHandle
.
getFile
();

Enter fullscreen mode

Exit fullscreen mode

Great for:

* web editors
* import/export tools
* power-user apps

The first time you use it, it feels slightly illegal.Like “are we really allowed to do this on the web?” 😄

Support: Chromium-heavy. Limited elsewhere.

## Reality Check 🧠

Many of these APIs are well supported in modern browsers.But some (Idle Detection, File System Access, Web Locks) are still Chromium-centric.

So always check compatibility before going all-in.

But simply knowing these exist?That already gives you an edge.

The web platform evolves fast.Sometimes the “new tech” isn’t a framework — it’s a native browser feature that’s been sitting there quietly.

What’s your favorite underrated Web API that nobody talks about?

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (68 comments)


Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
