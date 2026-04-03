---
title: Reports of code's death are greatly exaggerated
url: https://stevekrouse.com/precision
site_name: hackernews_api
content_file: hackernews_api-reports-of-codes-death-are-greatly-exaggerated
fetched_at: '2026-03-23T11:21:18.486068'
original_url: https://stevekrouse.com/precision
author: stevekrouse
date: '2026-03-22'
description: Reports of code's death are greatly exaggerated
tags:
- hackernews
- trending
---

← Steve Krouse
view source

# Reports of code's death are greatly exaggerated

March, 21 2026

A sufficiently detailed spec is codebegins with this lovely comic:

There is a profound tension here: english specificationsintuitively feelprecise until you learn better from bitter experience. (It's all in that facial
expression of the last frame.)

"Everything is vague to a degree you do not realize till you have tried to
make it precise."

– Bertrand Russel

Programming, like writing, is an activity, where one iteratively sharpens what
they're doing as they do it. (You wouldn't believe how many drafts I've written
of this essay.)

AI helps you with this, because it – increasingly instantly and well – turns
English into running code. You can then react to it – "move the button there;
make it bluer" – to get incrementally more precise about what you want.

This is why "vibe coding" is such a perfect phraseology: you stay operating at
the level of your English-level vibes while reacting to the AI-created artifacts
that help you sharpen your thinking.

But, vibe coding gives the illusion that your vibes are precise abstractions.
They will feel this way right up until theyleak,
which will happen when you add enough features or get enough scale. Unexpected
behaviors (bugs) thatemerge from lower levels of abstractionthat you don't understand will sneak up on you and wreck your whole day.

This was Dan Shipper's experience when hisvibe-coded text-editor app went viral, and then went down.
As it turns out, "live collaboration is just insanely hard."

"Live collaboration"intuitively feelslike a perfectly precise specification.
We've all used Google Docs, Notion, etc so itfeelsprecisely spec'd. It's
incredibly hard a priori to see what this is not the case.

The only reason that I personally know otherwise is that I tried to add a
collaborative text editor to a product I was working on 10 years ago, and it was
an unexpected nightmare of complexity.

What was hard about it? I don't remember! That's part of the problem! Complexity
can be incredibly boring, unpleasant to think about, and hard to remember all
the details and edge cases. For example, the classic flowchart of how Slack
decides when to send you a notification:

But, this isn't the end of the story either. We are blessed with an extremely
powerful tool to master complexity.

## Abstraction

There is a fundamental limit in the human brain. We can only think of 7 (plus or
minus 2) things at a time. So theonly wayto think about more than 7 things
is tocompressmultiple things into a single thing. Happily, we can do this
recursively, indefinitely, which is why humans can master unlimited complexity.
That compression step is calledabstraction.

The purpose of abstraction is not to be vague, but to create a new semantic
level in which one can be absolutely precise.

— Edsger Dijkstra

For example, Sophie Alpert used clever abstraction torefactor the Slack diagram to this much simpler one:

This is the best part of programming: coming up with increasingly good
abstractions to help us master complexities. My favorite examples of this are
functional programming concepts, like functional reactive programming, whichI wrote a wonderful essay on.

So yes, collaborative text editors are fundamentally complex, but that just
means that we're continually in search of better abstractions to help us master
complexities, like ReactJS or TailwindCSS did in their respective domains.

## AGI

But let's play this out 1, 2, 5, 10, 100 years. AI is getting
better/faster/cheaper at incredible rates, but regardless ofwhen, unless you
believe in magic, it's only a matter of time until we reach the point at which
machine intelligence is indistinguishable from human intelligence. We call that
point AGI.

It may seem like an AGI world is a vibe world. If anyone can afford 100
Karpathy-level geniuses for $1000 / month, why ever trouble yourself with any
troublesome details? Just have your army of Karpathys handle them for you.

This is such a joke to me. This isclearlyonly something you'd think in the
abstract, before this technology arrived.

If you told me that I had access to that level of intelligence, there is zero
part of me that is going to use it to shipmoreslop. Are you freaking
kidding?? Of course not.

I think we're confused because we (incorrectly) think that code is only for the
software it produces. It's only partly about that. The code itself is also a
centrally important artifact. When done right, it's poetry. And I'm not just
saying this because I have Stockholmn Syndrome or a vested interest in it – like
a horse jockey might in the face of cars being invented.

I think this is a lot clearer if you make an analogy to writing. Isn't it
fucking telling that nobody is talking about "vibe writing"?

We're not confused with writing because there's nothing mystical about
syntactically correct sentences in the same way there is about running code.
Nobody is out there claiming that ChatGPT is putting the great novelists or
journalists out of jobs. We all know that's nonsense.

Until we get AGI. Then, by definition, machines will write amazing non-slop and
it'll be glorious.

The same exact situation is true for coding. AI produces (increasingly less)
shitty code. We all know this. We all work around this limitation. We use AI
in spite of the bad code.

As Simon Willison says,AI should help us produce better code.
And when we have AGI this will be easy.

When we have AGI, thevery firstthings we will use it on will be our hardest
abstraction problems. We will use it to help us make better abstractions so that
we can better understand and master complexity.

You might think the need for good code goes away as AIs get smarter, but that's
like using ChatGPT to write more slop. When we get AGI, we will use them to make
better abstractions, better collaborative text editor libraries, etc.

For example, my favorite success story with Opus 4.6 was that it helped
me with my dream full-stack react framework for Val Town. It one-shot solvedmy list of unsolved problemsthat I had with getting React Router 7 to work full-stack in Val Town. The
result is my nascentvtrrframework.
I'm particularly proud of this 50 line full-stack react app demo ina single file:

If you know of any other snippet of code that can master all that complexity as
beautifully, I'd love to see it.

## Reports of code's death are greatly exaggerated

It seems like 99% of society has agreed that code is dead. Just yesterday I was
listening to podcaster Sam Harris of all people confidently talking about how everyone agrees
coding is dead, and that nobody should learn to code anymore.

This is so sad. It's the same as thinking storytelling is dead at the invention
of the printing press. No you dummies, code is just getting started. AI is going
to be such a boon for coding.

I have so much more to say on this topic, but this essay is already 3x longer
than I wanted it to be. I'll stop here and leave you with some of my favorite
quotes on formalism.

Instead of regarding the obligation to use formal symbols as a burden, we
should regard the convenience of using them as a privilege: thanks to them,
school children can learn to do what in earlier days only genius could
achieve.

When all is said and told, the "naturalness" with which we use our native
tongues boils down to the ease with which we can use them for making
statements the nonsense of which is not obvious.

– Edsger W.Dijkstra,On the foolishness of "natural language programming"

There are two ways of constructing a software design: One way is to make it so
simple that there are obviously no deficiencies, and the other way is to make
it so complicated that there are no obvious deficiencies.

–Tony Hoare,h/t Paul Buchheit

The quantity of meaning compressed into a small space by algebraic signs, is
another circumstance that facilitates the reasonings we are accustomed to
carry on by their aid."

– Charles Babbage, quoted in Iverson's Turing Award Lecture, quoted inSuccinctness is Power by Paul Graham

precision
 · 
abstraction
 · 
ai
 · 
coding