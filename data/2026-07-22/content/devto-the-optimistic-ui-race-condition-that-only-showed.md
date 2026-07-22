---
title: The Optimistic UI Race Condition That Only Showed Up on the Fifth Click - DEV Community
url: https://dev.to/shubhradev/the-optimistic-ui-race-condition-that-only-showed-up-on-the-fifth-click-5a55
site_name: devto
content_file: devto-the-optimistic-ui-race-condition-that-only-showed
fetched_at: '2026-07-22T19:32:24.240462'
original_url: https://dev.to/shubhradev/the-optimistic-ui-race-condition-that-only-showed-up-on-the-fifth-click-5a55
author: Shubhra Pokhariya
date: '2026-07-21'
description: 'This is a submission for DEV''s Summer Bug Smash: Smash Stories powered by Sentry. I originally... Tagged with devchallenge, bugsmash, nextjs, react.'
tags: '#devchallenge, #bugsmash, #nextjs, #react'
---

Summer Bug Smash: Smash Stories 🐛🛹

This is a submission forDEV's Summer Bug Smash: Smash Storiespowered bySentry.

I originally shared this debugging story on July 8. When Bug Smash was announced, it immediately came to mind because nothing crashed, nothing logged an error, and the application was still wrong.

## The setup

Everything worked. I'd wired upuseOptimisticon a task list, the checkbox flipped the instant you clicked it, no spinner, no half second lag, exactly the feeling I was going for. I demoed it to myself a dozen times and moved on.

That was the trap. Optimistic UI is designed to look right immediately. Looking right and being right are not the same claim.

## The moment I stopped trusting the demo

Then I did the thing you're supposed to do before you actually ship anything. I clicked it stupidly fast, five times in a row, the way an impatient real user actually would.

The checkbox stayed visually fine. The database did not. Five overlapping requests had gone out, each one flipping the same boolean, landing in whatever order the network felt like that day. Nothing crashed. Nothing logged an error. The UI just quietly stopped matching what actually happened on the server, and I had no way of knowing from looking at the screen.

That is the bug that is easy to miss with optimistic UI specifically, because the whole point of optimistic UI is that it looks right immediately.

## The fix isn't anything specific to useOptimistic

It's the same rule as disabling a submit button while a form is in flight, just applied per row instead of per form. Track which item has a request pending, and disable it until that request settles.

const
 
[
pendingId
,
 
setPendingId
]
 
=
 
useState
<
string
 
|
 
null
>
(
null
);

function
 
handleToggle
(
id
:
 
string
)
 
{

 
setPendingId
(
id
);

 
startTransition
(
async 
()
 
=>
 
{

 
setOptimisticTask
(
id
);

 
try
 
{

 
await
 
toggleTask
(
id
);

 
}
 
finally
 
{

 
setPendingId
(
null
);

 
}

 
});

}

Enter fullscreen mode

Exit fullscreen mode

<
input

 
type
=
"checkbox"

 
checked
=
{
task
.
completed
}

 
disabled
=
{
pendingId
 
===
 
task
.
id
}

 
onChange
=
{
()
 
=>
 
handleToggle
(
task
.
id
)
}

/>

Enter fullscreen mode

Exit fullscreen mode

One item at a time, scoped per row, not a global lock on the whole list. The second click on the same checkbox now does nothing instead of firing a second request that races the first one to the database.

Here's what that actually looks like: five rapid clicks, one request.

## One comment made me think harder

After the original post went up, Nazar Boyko left a comment that stuck with me.

He pointed out something I hadn't really separated in my own head. Disabling the checkbox only blocks clicks that go through that specific input. If the same toggle can ever be triggered another way, like a keyboard shortcut or somewhere else in the app, the disabled attribute is only one layer of protection. The real guard is the id keyed pending state, because that prevents the same operation from starting again regardless of how it was triggered.

He also mentioned that the rollback explanation was the part that clicked for him. Most examples manually flip the state back in acatchblock without explaining why. Realizing that a plain toggle doesn't need that extra step was one of the biggest things I learned while digging intouseOptimistic, so it was nice to hear that it helped someone else too.

That's one of my favorite things about writing technical posts in public. Sometimes someone doesn't find a bug in your code. They help you explain the idea more clearly or think about it from a different angle.

## The rollback question that sent me down a rabbit hole

While I was in there, I went looking for how to properly roll back an optimistic update on failure, since obviously if the toggle fails, the checkbox needs to snap back to whatever it actually was.

Almost every example I found does this:

try
 
{

 
setOptimisticTask
(
id
);

 
await
 
toggleTask
(
id
);

}
 
catch
 
{

 
setOptimisticTask
(
id
);
 
// flip it back again to "undo"

}

Enter fullscreen mode

Exit fullscreen mode

It works. It's also solving a problem that, for a plain toggle like this one, does not need solving.useOptimisticdoes not give you a second, independent piece of state you own. It gives you a temporary value layered on top of whatever state you passed in, for exactly as long as the transition is pending. The moment that transition settles, success or failure, React drops the temporary layer and renders from the real state again. If the real state never changed, because the request failed and nothing re-fetched, the checkbox reverts on its own. No second dispatch required.

There is one real exception. If the optimistic value is something the server has not confirmed yet at all, a new comment you added with a placeholder id before the database assigned a real one, there is no prior version of that item sitting in your base state to fall back to. A failed insert does not revert a flag, it has to remove something that only ever existed on the client. That is the one case where you keep your own local record of what you added and clear it yourself in the catch block. A toggle does not have that problem, since the value it flips already exists on the server either way.

## The cache function question I didn't expect to have opinions about

Once the toggle worked, the next question was how to actually invalidate the cache after it. Next.js 16 gives you three ways to do this, and picking the wrong one either shows the user stale data or forces every page on the site to block on a single write.

For a checkbox someone is staring at as they click it,updateTagis the right one, since it expires the tag immediately so the page the user is currently on reflects their own write right away. If that same task count also fed a sidebar stat somewhere else on the site, one nobody is watching in real time,revalidateTagon that same tag lets it catch up a beat later instead.

One thing worth knowing if you are on a recent Next.js 16 version,revalidateTagnow requires a second argument.

revalidateTag
(
"
tasks
"
,
 
"
max
"
);
 
// recommended in Next.js 16+

Enter fullscreen mode

Exit fullscreen mode

revalidateTag("tasks")alone is deprecated and will throw a TypeScript error.

## What changed for me

I used to demo optimistic UI by clicking once.

Now I deliberately try to break it. Five rapid clicks. Slow networks. Repeated interactions.

Race conditions rarely announce themselves. They don't throw exceptions. They don't light up your console. They quietly wait for a user who is just a little more impatient than you were during development.

That checkbox looked perfect every time I demonstrated it. The bug was there the whole time. It was simply waiting for me to test it like a real user.

If you'd like the full walkthrough, including the rollback patterns, cache decisions, and the rest of the implementation, I've put it all here:shubhra.dev/tutorials/nextjs-16-useoptimistic-rollback-pattern

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (12 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse