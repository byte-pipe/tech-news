---
title: I Built a Mobile App in 3 Days. The Hard Part Was Keeping It Connected. - DEV Community
url: https://dev.to/juandastic/i-built-a-mobile-app-in-3-days-the-hard-part-was-keeping-it-connected-2fda
site_name: devto
content_file: devto-i-built-a-mobile-app-in-3-days-the-hard-part-was-k
fetched_at: '2026-05-08T12:08:33.357476'
original_url: https://dev.to/juandastic/i-built-a-mobile-app-in-3-days-the-hard-part-was-keeping-it-connected-2fda
author: Juan David Gómez
date: '2026-05-04'
description: I have been building web apps for 12 years. In that time I never wrote a single line of mobile code.... Tagged with ai, mobile, showdev, sideprojects.
tags: '#showdev, #ai, #mobile, #sideprojects'
---

Veteran web developer's first mobile build

I have been building web apps for 12 years. In that time I never wrote a single line of mobile code. Not Swift, not Kotlin, not even a basic React Native hello world.

That changed last month because of my wife.

She has been usingSynapse, the AI companion I built for her, every day from her phone browser. If you are new here, Synapse is a personal AI that uses atemporal knowledge graphinstead of simple vector search to remember everything about her life, relationships, and emotional patterns. I have written aboutscaling the memory system,moving ingestion to async,benchmarking memory frameworks, andbuilding a Notion interface for the knowledge graph. This article is about something different: going mobile.

The experience from the phone browser worked but it did not feel right. She wanted a real app. Something that lives on her home screen, opens instantly, and does not show a browser address bar at the top.

I had been avoiding mobile development for years. It always felt like a completely different world with different tooling, different deployment, different everything. But two things made me reconsider. First, React Native with Expo has gotten really good. It is close enough to the web development I already know that the jump did not feel as scary. Second, AI tooling like Cursor and Claude made me confident I could move fast even in territory I had never touched before.

There was one more thing that made this possible. Synapse is built as a monorepo with Turborepo. The web app, the backend, shared packages, and now the mobile app all live in the same repository. This means the AI coding agent can see everything at once. When I asked it to build a new screen, it could look at the existing web components, the Convex backend, the shared types, and produce code that actually fit. No context switching, no copy pasting between repos. It just worked.

So I opened a terminal and started.

## 3 Days to a Working App

First commit: April 3, 2026. By April 5, I had a working app with Clerk authentication, chat UI, real-time streaming, memory management, personas, and the same dark theme from the web version. Everything powered by the same Convex backend.

Here is what 3 days of work looks like:

The app has an onboarding flow that explains how Synapse works: you converse, it ingests your conversations, compiles them into a knowledge graph, and evolves over time. From the sidebar, you can access your sessions, memory, personas, and plans. The chat interface streams AI responses in real time. The personas screen lets you switch between different AI modes like Brujula (therapeutic companion based on ACT and DBT), Calma (emotional support through positive psychology), Focus (pure technical mode, no memory context), and others. The Memory Explorer shows the full knowledge graph with 45 nodes and 47 relationships, where you can inspect any entity and see its connections.

The monorepo was the secret weapon here. Clerk for auth, Expo Router for navigation, the same Convex mutations and queries the web app already uses. I did not have to rebuild any backend logic. The shared packages meant types, API definitions, and validation were already there. I just had to build the screens.

Three days. For a web developer who had never touched mobile before, that felt unreal. But the speed hid a problem I would not discover until my wife actually started using it.

Everything worked on my simulator. Then she started using it on her phone.

## The Problem: iOS Kills Your Connection

On the web, streaming AI responses is straightforward. You callfetch, get aReadableStreamfromresponse.body, and read chunks as they arrive. Clean, modern, reliable.

React Native on iOS does not support this.

The Hermes JavaScript engine that powers React Native on iOS does not implementReadableStreamon the fetch response body. So the standard web approach does not work at all. The workaround is to useXMLHttpRequestwithresponseType: "text"and listen to theonprogressevent. Every time new data arrives,xhr.responseTextcontains everything received so far. You compare the length to track what is new.

Here is what that looks like:

const
 
xhr
 
=
 
new
 
XMLHttpRequest
();

xhr
.
open
(
"
POST
"
,
 
`
${
CONVEX_SITE_URL
}
/chat`
);

xhr
.
setRequestHeader
(
"
Content-Type
"
,
 
"
application/json
"
);

xhr
.
setRequestHeader
(
"
Authorization
"
,
 
`Bearer 
${
token
}
`
);

xhr
.
responseType
 
=
 
"
text
"
;

let
 
lastLength
 
=
 
0
;

xhr
.
onprogress
 
=
 
()
 
=>
 
{

 
const
 
currentText
 
=
 
xhr
.
responseText
;

 
if 
(
currentText
.
length
 
>
 
lastLength
)
 
{

 
lastLength
 
=
 
currentText
.
length
;

 
updateStreamedContent
(
currentText
);

 
}

};

Enter fullscreen mode

Exit fullscreen mode

This worked great in development. I could see the AI response streaming in word by word, just like on the web. I shipped it.

Then my wife started using the app the way people actually use phones. She would ask Synapse something, then switch to WhatsApp while waiting for the response. Or she would lock the screen. Or she would check Instagram for a few seconds.

And when she came back, the response was gone. Blank message. Or an error.

Here is what was happening. iOS aggressively suspends apps that go to the background. When she switched away, iOS killed the network request. TheXMLHttpRequestconnection dropped silently. But the AI backend had already started generating. The server kept running, producing tokens, burning cost. The response just had nowhere to go. The phone was no longer listening.

This is not a bug you catch in development. You catch it when someone uses the app the way real people use phones: they never stay on one screen. They switch constantly. And every switch is a chance for iOS to kill your connection.

## The Fix: Convex as Middleware

The key insight was simple: stop treating the client as the only receiver of the stream.

Synapse uses Convex as its backend. The mobile app sends a request to a Convex HTTP endpoint, which forwards it to the AI service (Cortex) and streams the response back. Before the fix, this was a straight pipe: Cortex generates, Convex streams to client, client renders. If the client disappears, the pipe breaks and everything after that point is lost.

The fix was to make the server aware of the disconnect and keep going anyway.

if 
(
delta
?.
content
)
 
{

 
content
 
+=
 
delta
.
content
;

 
if 
(
!
clientDisconnected
)
 
{

 
try
 
{

 
await
 
writer
.
write
(
encoder
.
encode
(
delta
.
content
));

 
}
 
catch
 
{

 
clientDisconnected
 
=
 
true
;

 
console
.
warn
(

 
"
[http /chat] Client disconnected, continuing generation server-side
"
,

 
{
 
requestId
,
 
contentLengthSoFar
:
 
content
.
length
 
}

 
);

 
}

 
}

}

Enter fullscreen mode

Exit fullscreen mode

When the HTTP writer tries to send a chunk and it fails (because the client is gone), the server sets aclientDisconnectedflag, logs a warning, and keeps generating. It does not stop. It does not throw. It just stops trying to write to a dead connection and continues accumulating the response.

At the end of the generation, regardless of whether the client was still connected, the server makes a single database write to persist the final content:

await
 
ctx
.
runMutation
(
internal
.
messages
.
finalizeGeneration
,
 
{

 
id
:
 
assistantMessageId
,

 
content
,

 
metadata
:
 
{
 
model
:
 
modelUsed
,
 
usedFallback
,
 
/* ... */
 
},

 
completedAt
:
 
Date
.
now
(),

});

Enter fullscreen mode

Exit fullscreen mode

When the user reopens the app, the message is already there. Fully generated. Stored in Convex. No retry needed, no lost tokens, no blank messages.

There was one more edge case to handle. The mobile client has error handling that callsreportStreamFailurewhen the stream fails. But what if the server finished the generation successfully after the client disconnected? The client would come back, see the XHR failed, and try to mark the message as an error, overwriting the perfectly good response the server already saved.

The guard is simple:

export
 
const
 
reportStreamFailure
 
=
 
mutation
({

 
args
:
 
{

 
messageId
:
 
v
.
id
(
"
messages
"
),

 
errorMessage
:
 
v
.
optional
(
v
.
string
()),

 
},

 
handler
:
 
async 
(
ctx
,
 
args
)
 
=>
 
{

 
const
 
message
 
=
 
await
 
ctx
.
db
.
get
(
args
.
messageId
);

 
// Don't overwrite a message the server already finalized

 
if 
(
message
.
completedAt
 
!==
 
undefined
)
 
{

 
console
.
log
(
"
[reportStreamFailure] Skipped — already finalized
"
);

 
return
;

 
}

 
await
 
ctx
.
db
.
patch
(
args
.
messageId
,
 
{

 
type
:
 
"
error
"
,

 
content
:
 
errorContent
,

 
metadata
:
 
{
 
errorCode
:
 
"
CLIENT_STREAM_FAILURE
"
 
},

 
completedAt
:
 
Date
.
now
(),

 
});

 
},

});

Enter fullscreen mode

Exit fullscreen mode

If the message already has acompletedAttimestamp, the failure report is ignored. The server won the race. The response is safe.

The whole flow looks like this: the client sends a request, the server starts generating. The client disconnects because iOS suspended the app. The server detects the disconnect on the next chunk write, sets the flag, and continues generating. Every chunk accumulates in memory. When the generation finishes, the server persists the full response to Convex. The client reconnects and finds the complete message waiting.

## The Numbers

After one month of tracking, here is where things stand:

* 546 messages sent from the web app
* 239 messages sent from the mobile app
* Mobile accounts for 30.4% of all usage

And the trend is clear. In recent days, mobile is matching or exceeding web usage. On May 1, there were 10 mobile messages and 9 web messages. She is using the phone more than the browser now.

Without the disconnect fix, nearly a third of all interactions would have been unreliable. Every time she switched apps mid-response (which is constantly), the message would have been lost.

Going mobile also comes with costs beyond engineering time. The Apple Developer Program is $99 per year. Google Play is a one-time $25 fee. Not a lot in absolute terms, but it is the kind of thing you think about when you are building a side project, not a funded startup.

## What I Learned

The device is the canvas. Same AI, same backend, same knowledge graph, but the phone changes how she uses Synapse. Quick questions while cooking. Checking memories on the go. The interactions are shorter, more frequent, and more spontaneous than on the web.

Building for mobile forced me to think about resilience in a way web never did. On the web, if someone switches tabs, your JavaScript keeps running. The connection stays open. The response arrives. You do not even think about it. On iOS, nothing is guaranteed. Your app can be suspended at any moment, and if you did not plan for that, your users will have a broken experience.

The browser is forgiving. iOS is not. And building for the unforgiving platform made the entire system better.

If you are building AI products and want to follow along, I write about the real challenges of shipping AI to real users. Not theory. Not demos. The stuff that breaks when someone actually uses your app every day.

Follow me:

* X:@juandastic
* LinkedIn:Juan David Gomez

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (11 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse