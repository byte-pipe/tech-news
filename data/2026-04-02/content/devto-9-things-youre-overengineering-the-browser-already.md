---
title: 9 Things You’re Overengineering (The Browser Already Solved Them) - DEV Community
url: https://dev.to/sylwia-lask/9-things-youre-overengineering-the-browser-already-solved-them-o99
site_name: devto
content_file: devto-9-things-youre-overengineering-the-browser-already
fetched_at: '2026-04-02T19:24:44.369004'
original_url: https://dev.to/sylwia-lask/9-things-youre-overengineering-the-browser-already-solved-them-o99
author: Sylwia Laskowska
date: '2026-04-02'
description: I love writing philosophical essays — thoughts about code, work, all that stuff. I also love deep... Tagged with webdev, javascript, css, browser.
tags: '#webdev, #javascript, #css, #browser'
---

Native voice input and idle task APIs

I love writing philosophical essays — thoughts about code, work, all that stuff. I also love deep technical dives. But I knowyoulove my lists of cool features that not everyone has heard about yet 😄

What’s up with me? This week I’m preparing for a conference, fighting performance issues, and trying to get at least somewhat ready for the upcoming holidays 😉

Something nice happened too. I enjoy writing — not just technical articles, but in general. Last summer my life changed quite a bit, and to keep my sanity I started writing a sci-fi story, which I submitted to a Polish science fiction foundation competition. I didn’t win, but my story made it pretty far — around 13th place out of 179 submissions. Considering it was my first attempt at this kind of writing… it could have gone worse 😄

And speaking of sci-fi — the kind happening right in front of us 😉 Today I’ve prepared a batch of things the browser can already do, which honestly didn’t fit in my head not that long ago. A lot of these are still not that widely known, and yet many of them are already supported across modern browsers. Have fun!

## 1. “Let me just run this later” →requestIdleCallback

At first I thought this API was pointless. It basically lets you run some code when nothing interesting is happening. Ok… cool… but why would I care?

Turns out — there are tons of use cases. For example, collecting data about how the user behaves on your page — definitely not something you want to do while your 200 components are rendering 😅 Or loading less important data, preprocessing something, generating images in the background.

Honestly, there are probably as many use cases as there are developers.

function
 
trackUserScrolling
()
 
{

 
console
.
log
(
"
User scrolled. This changes everything.
"
);

}

if 
(
"
requestIdleCallback
"
 
in
 
window
)
 
{

 
requestIdleCallback
(
trackUserScrolling
);

}
 
else
 
{

 
setTimeout
(
trackUserScrolling
,
 
0
);

}

Enter fullscreen mode

Exit fullscreen mode

Support:modern browsers (historically missing in Safari, so fallback is still a good idea)

## 2. “Why is my input not highlighting???” →:focus-within

It’s easy to style an element that has focus. But what if you want to style the parent div? For example, make it pink, add some flowers 😉 You can write 40 lines of JavaScript… or just use:focus-within.

Works. No listeners. No bugs. No suffering.

.form-field
 
{

 
border
:
 
1px
 
solid
 
#ccc
;

 
padding
:
 
12px
;

}

.form-field
:focus-within
 
{

 
border-color
:
 
hotpink
;

}

Enter fullscreen mode

Exit fullscreen mode

<div
 
class=
"form-field"
>

 
<input
 
placeholder=
"Type something meaningful..."
 
/>

</div>

Enter fullscreen mode

Exit fullscreen mode

Support:basically everywhere that matters

## 3. “Let’s show offline mode” →navigator.onLine

Have you ever built a PWA? Because I have, and the eternal problem is what to do when the user loses connection (e.g. they’re in the wilderness or just walked into an elevator 😄). You can write a bunch of complicated ifs, or just listen toofflineandonline. Onofflineyou can store data in IndexedDB, and when the user is back online, send it to the server.

window
.
addEventListener
(
"
offline
"
,
 
()
 
=>
 
{

 
alert
(
"
You are offline. Time to panic.
"
);

});

window
.
addEventListener
(
"
online
"
,
 
()
 
=>
 
{

 
alert
(
"
You're back. Panic cancelled.
"
);

});

Enter fullscreen mode

Exit fullscreen mode

Support:widely supported (but “online” ≠ “your backend works” 😅)

## 4. “Smooth animation, but make it cursed” →requestAnimationFrame

We’ve all seen this:

setInterval
(()
 
=>
 
{

 
element
.
style
.
left
 
=
 
Math
.
random
()
 
*
 
100
 
+
 
"
px
"
;

},
 
16
);

Enter fullscreen mode

Exit fullscreen mode

You canfeelthis is not the best idea 😉 It just lags. Luckily we haverequestAnimationFrame, which is synced with the browser repaint cycle, so things are actually smooth.

function
 
animate
()
 
{

 
element
.
style
.
transform
 
=
 
`translateX(
${
Date
.
now
()
 
%
 
300
}
px)`
;

 
requestAnimationFrame
(
animate
);

}

requestAnimationFrame
(
animate
);

Enter fullscreen mode

Exit fullscreen mode

Support:everywhere

## 5. “This card should adapt… but only here” → container queries

This feature feels almost unfair. I’m at a point in my career where I barely write CSS anymore (well, except for occasional moments like the one I described here:Is learning CSS a waste of time in 2026?).

But there was a time when I wrotea lotof it. And wow — how much I would have given to apply media queries to a specific element instead of the whole viewport. Now we finally can. The component becomes self-aware, and we can go grab a coffee.

.card-wrapper
 
{

 
container-type
:
 
inline-size
;

}

.card
 
{

 
display
:
 
grid
;

}

@container
 
(
min-width
:
 
400px
)
 
{

 
.card
 
{

 
grid-template-columns
:
 
1
fr
 
2
fr
;

 
}

}

Enter fullscreen mode

Exit fullscreen mode

Support:modern browsers (add fallback if needed)

## 6. “Random ID, what could go wrong?” →crypto.getRandomValues

const
 
id
 
=
 
Math
.
random
().
toString
(
36
).
slice
(
2
);

Enter fullscreen mode

Exit fullscreen mode

This is how bugs are born. It looks like “good enough” crypto from AliExpress and works… until it doesn’t. First of all, it depends on the engine implementation — we don’t really know what’s happening under the hood. Some patterns are absolutely possible, and with enough IDs you’re basically asking for duplicates.

Luckily, we now have a simple native solution. It’s not a silver bullet, butcrypto.getRandomValuesis pretty solid — much better entropy, no weird patterns, dramatically reduces the chance of collisions. The browser just does it properly.

const
 
bytes
 
=
 
new
 
Uint8Array
(
8
);

crypto
.
getRandomValues
(
bytes
);

const
 
id
 
=
 
Array
.
from
(
bytes
)

 
.
map
(
b
 
=>
 
b
.
toString
(
16
).
padStart
(
2
,
 
"
0
"
))

 
.
join
(
""
);

console
.
log
(
"
Secure-ish ID:
"
,
 
id
);

Enter fullscreen mode

Exit fullscreen mode

Support:widely supported

## 7. “We need a modal” →<dialog>

It’s honestly nice that browsers finally stepped up and said: fine, here’s your modal 😄 No more installing 12KB libraries just to open a dialog that users love so much. This one is also accessible by default, so win-win.

<dialog
 
id=
"modal"
>

 
<p>
Are you sure you want to deploy on Friday?
</p>

 
<button
 
onclick=
"modal.close()"
>
Cancel
</button>

 
<button
 
onclick=
"alert('Good luck 😬')"
>
Deploy
</button>

</dialog>

<button
 
onclick=
"modal.showModal()"
>
Open modal
</button>

Enter fullscreen mode

Exit fullscreen mode

Support:modern browsers

## 8. “Voice input would be cool…” → Speech API

Are you already installing transformers.js because you need speech recognition? Relax — turns out the browser has something for that too. Well… at least Chromium does 😄 So if you can “encourage” users to use Chrome, Edge, or something similar, you’re good. Personally, I’d still be careful with production use, but for demos? Why not.

const
 
SpeechRecognition
 
=

 
window
.
SpeechRecognition
 
||
 
window
.
webkitSpeechRecognition
;

if 
(
SpeechRecognition
)
 
{

 
const
 
recognition
 
=
 
new
 
SpeechRecognition
();

 
recognition
.
onresult
 
=
 
e
 
=>
 
{

 
console
.
log
(
"
You said:
"
,
 
e
.
results
[
0
][
0
].
transcript
);

 
};

 
recognition
.
start
();

}

Enter fullscreen mode

Exit fullscreen mode

Support:mostly Chromium

## 9. “Will this CSS explode?” →@supports

Here’s a modern solution to the classic “it works on my machine” — at least in CSS 😉 You don’t have to guess whether something will break your layout. Just wrap it in@supports. There is a small catch — while support is very good, it’s not literally everywhere, so ironically… we could use@supportsfor@supports.

.card
 
{

 
background
:
 
white
;

}

@supports
 
(
backdrop-filter
:
 
blur
(
10px
))
 
{

 
.card
 
{

 
backdrop-filter
:
 
blur
(
10px
);

 
background
:
 
rgba
(
255
,
 
255
,
 
255
,
 
0.6
);

 
}

}

Enter fullscreen mode

Exit fullscreen mode

Support:very good

## ⚠️ But don’t get me wrong

Libraries are great. Sometimes you absolutely need them. But sometimes… you’re installing a dependency for something the browser solved years ago. Before installing anything, just ask yourself (or Google): “Is the browser already smarter than me here?” Sometimes the answer is yes. And that’s… perfectly fine 😄

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (23 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse