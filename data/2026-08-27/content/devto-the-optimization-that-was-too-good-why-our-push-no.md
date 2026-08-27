---
title: 'The Optimization That Was Too Good: Why Our Push Notifications Only Worked When You Weren''t Looking - DEV Community'
url: https://dev.to/dj29/the-optimization-that-was-too-good-why-our-push-notifications-only-worked-when-you-werent-looking-2f4d
site_name: devto
content_file: devto-the-optimization-that-was-too-good-why-our-push-no
fetched_at: '2026-08-27T20:57:31.455288'
original_url: https://dev.to/dj29/the-optimization-that-was-too-good-why-our-push-notifications-only-worked-when-you-werent-looking-2f4d
author: Dhruv Jani
date: '2026-08-22'
description: 'This is a submission for DEV''s Summer Bug Smash: Smash Stories powered by Sentry. When I was... Tagged with devchallenge, bugsmash, javascript, webdev.'
tags: '#devchallenge, #bugsmash, #javascript, #webdev'
---

Summer Bug Smash: Smash Stories 🐛🛹

This is a submission forDEV's Summer Bug Smash: Smash Storiespowered bySentry.

When I was building the push notification system forShelfTalk— a real-time social app that won theGitHub Finish Up A Thon Challengeon DEV — I wanted to be considerate of my users. There's nothing more annoying than actively chatting in a web app and having your desktop ping you with a notification for the exact message you're currently reading.

## JaniDhruv/ShelfTalk

### A full-stack real-time social architecture featuring Socket.io instant messaging, synchronized reading rooms, and a high-performance React/Vite frontend backed by MongoDB Atlas and GridFS and desktop push notifications for groups and chats.

# ShelfTalk

### Books don't talk. We do.

Turn every reading list into a living conversation.

🌐 Live Demo•⚡ Quick Setup•✨ Features•🛠 Tech Stack

## 📖 What is ShelfTalk?

ShelfTalkis a full-stack social community platform built for book lovers. Think of it as a blend of Goodreads and Discord — readers can share updates, annotate passages, join genre-based clubs, chat in real-time, and coordinate live reading sessions together.

Originally built as a college project, ShelfTalk has since been revived and significantly expanded with real-time infrastructure, a live reading room feature, a personal reading diary, an invite friends feature to help the community grow, cloud file storage, and more.

## ✨ Core Features

### 📝 Community Posts

* Publish reading updates and annotate favourite passages
* Threaded comments keep every discussion organized
* Reactions and saves from your personal dashboard

### 🔍 Powerful Discovery

* Filter readers by genre, location, and interests
* Browse vibrant…

View on GitHub

So, I added what I thought was a brilliant little optimization:

export
 
const
 
sendPushNotification
 
=
 
(
title
,
 
options
 
=
 
{},
 
requireHidden
 
=
 
false
)
 
=>
 
{

 
if 
(
!
(
'
Notification
'
 
in
 
window
))
 
return
;

 
if 
(
Notification
.
permission
 
===
 
'
granted
'
)
 
{

 
// If requireHidden is true, only fire if the tab is hidden

 
if 
(
requireHidden
 
&&
 
!
document
.
hidden
)
 
{

 
return
;
 
// <-- The "Brilliant" Optimization

 
}

 
try
 
{

 
const
 
notification
 
=
 
new
 
Notification
(
title
,
 
options
);

 
// ...

 
}
 
catch 
(
e
)
 
{

 
console
.
error
(
e
);

 
}

 
}

};

Enter fullscreen mode

Exit fullscreen mode

The logic was simple: checkdocument.hidden(thePage Visibility API). If the user is currently looking at the ShelfTalk tab, suppress the desktop notification. No redundant pings. Clean UX.

I deployed it, patted myself on the back, and went about my day.

## 🔍 The Mystery

A few days later, the bug reports started rolling in. Users were complaining that they were missing important direct messages and group mentions.

I tested it on my machine. I minimized the browser, had a friend send me a message, and —ding!— the notification popped up perfectly. I opened the window, got another message, and no notification appeared.It was working exactly as designed.

So why were people missing messages?

## 💡 The "Ah-Ha" Moment

I asked one of the users to describe their setup.

"Oh, I usually leave ShelfTalk open on my second monitor while I work on my main screen."

And suddenly it clicked.

The Page Visibility API (document.hidden) only returnstrueif the page iscompletely hidden— either behind other windows in a background tab, or in a minimized window.If the window is visible on a second monitor — even if you are actively working in a completely different app on your main monitor —document.hiddenisfalse.

Because the tab was technically "visible" to the operating system, my code assumed the user was staring directly at it. It silently dropped every notification. The user, focused on their main screen, never heard a ping and missed the message entirely.

Even worse: if a user left ShelfTalk open on their desktop at the office and went home, their home laptop would never notify them either — because the office machine was technically still "looking" at the app.

TL;DR:document.hidden === falsedoesnotmean the user is paying attention. It just means the OS can see the window.

## 🔨 The Smash

Sometimes, the best way to fix a bug is todelete the code you were so proud of writing.

I removed the optimization entirely:

- // If requireHidden is true, only fire if the tab is hidden
- if (requireHidden && !document.hidden) {
- return;
- }

+ // Notifications will now fire even if the tab is visible,
+ // to ensure they appear across all active machines.

Enter fullscreen mode

Exit fullscreen mode

(See the exact commithere)

## 📖 The Lesson

We often try to be "too smart" with our UX optimizations. I assumed that"window visible" equaled "user paying attention."In the era of ultra-wide monitors, multiple screens, and users being logged in on five different devices at once, that assumption was completely wrong.

By trying to save users from a slightly annoying notification, I ended upbreaking the core promise of a notification system: telling you when something happens.

Three things this bug taught me:

1. Test with real user setups, not just yours.My single-monitor dev machine couldn't reproduce the issue. Multi-monitor setups, tablets propped up on desks, browsers left open on work machines — these are all "visible" to the OS.
2. document.hiddenis about the OS viewport, not human attention.TheMDN docsare clear about this, but it's easy to project human meaning onto a boolean that was never designed to carry it.
3. When in doubt, notify.A slightly redundant ping is annoying. A silently dropped message is a broken product.

Now, ShelfTalk might ping you even if you're looking right at it. But at least you'll never miss a message again. 🔔

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (32 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse