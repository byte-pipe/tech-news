---
title: Has AI Made You A Lazier Developer? Be Honest. - DEV Community
url: https://dev.to/nazar-boyko/has-ai-made-you-a-lazier-developer-be-honest-5ack
site_name: devto
content_file: devto-has-ai-made-you-a-lazier-developer-be-honest-dev-c
fetched_at: '2026-09-08T21:34:48.600429'
original_url: https://dev.to/nazar-boyko/has-ai-made-you-a-lazier-developer-be-honest-5ack
author: Nazar Boyko
date: '2026-09-08'
description: Haven't you ever wondered if this AI vibe coding has made us lazy? Who's been solving problems on... Tagged with discuss, ai, productivity, career.
tags: '#discuss, #ai, #productivity, #career'
---

Reframe laziness as efficient labor redistribution

Haven't you ever wondered if this AI vibe coding has made us lazy? Who's been solving problems on LeetCode lately? 😅

I've noticed that accepting is easier than thinking, by a margin so small that no single accept feels like anything, and it adds up anyway. Part of why it's hard to notice is that it feels faster even when it isn't.

But I've come to think "lazy" is the right worry aimed at the wrong thing. There are two kinds of lazy and only one of them is a problem.

I'm going to go into a little background here, because I didn't come up with this, and I didn't reach this conclusion on my own.

## Lazy is why we have compilers

Larry Wall, who created Perl, put laziness first on his list of thethree great virtues of a programmer, and his definition is the whole argument: "the quality that makes you go to great effort to reduce overall energy expenditure." Great effort. Good lazy isn't the absence of work, it's work moved somewhere better, and it's more or less why compilers exist (somebody got tired of writing the same assembly by hand and decided, reasonably, that the machine could do that part) and why every abstraction we lean on all day is really someone's laziness done properly.

Handing that kind of toil to a model is nothing new. The config I've written a hundred times and the regex I could write but would rather not and the Dockerfile I could recite and the test scaffolding that comes out identical in every project I've ever started: I understand all of it and I'm simply declining to type it again and I feel no guilt about that whatsoever (honestly I'd be more worried about a developer who insisted on typing all of it out by hand in 2026, on principle, one character at a time, while the rest of the team went home). That's not skipping the thinking. That's skipping the typing after the thinking was already done.

## The other kind skips the understanding

The second kind of lazy offloads the understanding itself. The model writes the thing and it runs and the tests are green and the PR gets merged and somewhere in that chain there's now a piece of code nobody on the team could explain or fix, and that's the kind that costs, not today but on the day it breaks and somebody on call opens the file at 2am and finds a function nobody can vouch for.

The smallest illustration I can think of, made up on purpose: say the model writes a regex that validates email addresses at sign-up. If I could have written it and chose not to, that's the first kind of lazy, and if I couldn't have and it's now the thing deciding who gets an account, that's the second kind, and it's the same regex on the same line of the same diff either way. The reviewer can't tell the difference and neither can CI. The only place the two kinds differ is inside my head.

Okay, but isn't this just the old Stack Overflow copy-paste problem with a faster clipboard? Mostly yes. And I think that's what makes it worse. Stack Overflow made me go find the answer and read a thread of strangers arguing about it (sometimes with the accepted answer being wrong and the better one three comments down with a tenth of the votes) and then adapt it to my code. The friction was doing quiet work. The suggestion just appears in my file already indented and nothing about it asks to be understood.

## Could you rebuild it if it vanished?

I don't have a rulebook for this and I'm suspicious of anyone who does. What I have is one question. Take the last thing the model wrote for you and imagine the file is gone. I don't mean the exact characters, nobody remembers those. Could you sit down and produce something that does the job, and would you know why it works?

If yes, that was the good kind of lazy and it's worth keeping. If no, it doesn't matter how fast it shipped.

That's the honest answer to the title, at least for me. It depends on the week. Some weeks every accept is toil I understand. Other weeks I'm not sure, which is a polite way of saying no. The drift never announces itself. It just gets a little easier to press tab each time.

So I'm asking. I want the real answer, not the one that sounds good. What was the last thing AI wrote for you, and could you rebuild it tomorrow? 😃

Thanks for reading! English isn't my first language, so I use AI to polish the grammar. Everything else here - the ideas, the opinions - is mine.

Enjoyed this one? Let's stay in touch — I'm onLinkedIn, always happy to chat, swap ideas, or just say hi. 👋

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (12 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse