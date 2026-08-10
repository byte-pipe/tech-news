---
title: Stop using the localStorage hack to sync browser tabs. BroadcastChannel does it natively. - DEV Community
url: https://dev.to/parsajiravand/stop-using-the-localstorage-hack-to-sync-browser-tabs-broadcastchannel-does-it-natively-4an9
site_name: devto
content_file: devto-stop-using-the-localstorage-hack-to-sync-browser-t
fetched_at: '2026-08-10T11:45:58.408910'
original_url: https://dev.to/parsajiravand/stop-using-the-localstorage-hack-to-sync-browser-tabs-broadcastchannel-does-it-natively-4an9
author: Parsa Jiravand
date: '2026-08-09'
description: When a user logs out in one tab, the other tabs should follow. When they update their cart, every... Tagged with javascript, webdev, frontend, api.
tags: '#javascript, #webdev, #frontend, #api'
---

Avoids localStorage cleanup bugs

When a user logs out in one tab, the other tabs should follow. When they update their cart, every open window should reflect it. The common solution is a localStorage trick: write a sentinel value, listen for thestorageevent, read it, parse it, check if it's "for you," and clean it up. It works — but it's a side-channel communication pattern built on a persistence API that was never meant for messaging. The Broadcast Channel API is the direct path.

## The API

// Sender (any tab, worker, or iframe on the same origin)

const
 
channel
 
=
 
new
 
BroadcastChannel
(
'
app-sync
'
);

channel
.
postMessage
({
 
type
:
 
'
LOGOUT
'
 
});

// Receiver (every other context subscribed to the same name)

const
 
channel
 
=
 
new
 
BroadcastChannel
(
'
app-sync
'
);

channel
.
onmessage
 
=
 
(
event
)
 
=>
 
{

 
console
.
log
(
event
.
data
);
 
// { type: 'LOGOUT' }

};

Enter fullscreen mode

Exit fullscreen mode

Two steps: open a channel by name, then send or listen. Any tab, worker, or iframe on the same origin that opens a channel with the same name receives every message sent on it — including messages sentafterthey subscribed. The sender does not receive its own messages.

Close the channel when you're done to release the listener:

channel
.
close
();

Enter fullscreen mode

Exit fullscreen mode

## What the localStorage approach actually looks like

The typical cross-tab sync pattern usingstorageevents:

// Sender

localStorage
.
setItem
(
'
__broadcast
'
,
 
JSON
.
stringify
({
 
type
:
 
'
LOGOUT
'
,
 
t
:
 
Date
.
now
()
 
}));

localStorage
.
removeItem
(
'
__broadcast
'
);
 
// clean up immediately

// Receiver

window
.
addEventListener
(
'
storage
'
,
 
(
event
)
 
=>
 
{

 
if 
(
event
.
key
 
!==
 
'
__broadcast
'
)
 
return
;
 
// filter noise

 
if 
(
!
event
.
newValue
)
 
return
;
 
// ignore the removeItem

 
const
 
message
 
=
 
JSON
.
parse
(
event
.
newValue
);

 
if 
(
message
.
type
 
===
 
'
LOGOUT
'
)
 
{
 
/* handle */
 
}

});

Enter fullscreen mode

Exit fullscreen mode

Every part of this is load-bearing workaround: the timestamp prevents deduplication if the same value is sent twice; theremoveItemtriggers a second storage event that must be filtered out;JSON.stringify/JSON.parseis required because storage only holds strings. BroadcastChannel replaces the entire block with apostMessagecall.

## Real-world use cases

Logout across all tabs.When the user logs out, invalidate the session in every open window simultaneously:

// auth.js — runs in every tab

const
 
syncChannel
 
=
 
new
 
BroadcastChannel
(
'
auth
'
);

export
 
function
 
logout
()
 
{

 
clearSession
();

 
syncChannel
.
postMessage
({
 
type
:
 
'
SESSION_ENDED
'
 
});

 
redirect
(
'
/login
'
);

}

syncChannel
.
onmessage
 
=
 
(
event
)
 
=>
 
{

 
if 
(
event
.
data
.
type
 
===
 
'
SESSION_ENDED
'
)
 
{

 
clearSession
();

 
redirect
(
'
/login
'
);

 
}

};

Enter fullscreen mode

Exit fullscreen mode

Cart sync in an e-commerce app.Add to cart in one tab, see the count update in the header of every other tab:

const
 
cartChannel
 
=
 
new
 
BroadcastChannel
(
'
cart
'
);

function
 
addToCart
(
item
)
 
{

 
const
 
updated
 
=
 
updateLocalCart
(
item
);

 
cartChannel
.
postMessage
({
 
type
:
 
'
CART_UPDATED
'
,
 
cart
:
 
updated
 
});

 
renderCart
(
updated
);

}

cartChannel
.
onmessage
 
=
 
(
event
)
 
=>
 
{

 
if 
(
event
.
data
.
type
 
===
 
'
CART_UPDATED
'
)
 
{

 
renderCart
(
event
.
data
.
cart
);

 
}

};

Enter fullscreen mode

Exit fullscreen mode

Live config refresh.When an admin changes a feature flag in a settings tab, broadcast the update so every other open tab picks it up without a page reload.

## What you can send

BroadcastChannel uses thestructured clone algorithm— the same one used bystructuredClone()andpostMessage()on workers. That means you can send:

* Plain objects and arrays (including nested)
* Date,Map,Set,ArrayBuffer,Blob
* Primitive values — strings, numbers, booleans,null

Youcannotsend functions, DOM nodes, or anything not serializable by structured clone. If you try, the call throws aDataCloneError. For the message payloads most apps actually use — event objects with typed fields — structured clone covers everything without the JSON roundtrip.

## Scope and limits

BroadcastChannel is scoped tosame-origin contexts— same protocol, hostname, and port. A channel named'app-sync'onhttps://example.comis completely isolated from a channel with the same name onhttps://staging.example.com. You cannot use it to communicate between different origins.

The channel name is your namespace. If multiple features in your app use BroadcastChannel, give each a distinct name ('auth','cart','notifications') rather than sharing a single'app'channel and multiplexing message types through it — separate channels are cleaner and don't require filtering.

## Browser support

BroadcastChannel isBaseline 2022: Chrome 54 (2016), Firefox 38 (2015), Safari 15.4 (March 2022). The API has been in Chromium and Firefox for nearly a decade; Safari joined in 2022. It's available in all currently-supported browser versions and in Web Workers and Service Workers, not just the main thread.

## 🎮 Try it yourself

▶️ Open the interactive playground →

Runs right in your browser — poke at it and watch the concept react live.

## 🧠 Test yourself

Think it clicked?Take the 9-question quiz →

Instant feedback, a hint on every question, and an explanation for each answer — right or wrong.

## The takeaway

Search your codebase forstorageevent listeners paired with alocalStorage.setItemthat immediately gets removed. That pattern is cross-tab messaging through a storage side-channel — exactly what BroadcastChannel exists to replace. Swap it out: open a channel by name, callpostMessage, listen withonmessage. You get structured data without serialization, no storage event noise to filter, and no cleanup sentinel to manage. The intent becomes clear in the code; the runtime handles the delivery.

Thanks for reading! Let's stay connected:

* ⭐GitHub— follow me and star the projects:github.com/parsajiravand
* 💬Discord— join the frontend best-practices community:discord.gg/d9KRhuAwQ
* 📸Instagram— frontend best practices, daily:@bestpractice___
* 💼LinkedIn—linkedin.com/in/parsa-jiravand
* ✉️Email(work & contract inquiries):bestpractice2026@gmail.com

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse