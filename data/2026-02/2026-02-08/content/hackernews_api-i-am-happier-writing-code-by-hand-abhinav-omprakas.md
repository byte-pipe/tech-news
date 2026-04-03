---
title: I Am Happier Writing Code by Hand | Abhinav Omprakash
url: https://www.abhinavomprakash.com/posts/i-am-happier-writing-code-by-hand/
site_name: hackernews_api
content_file: hackernews_api-i-am-happier-writing-code-by-hand-abhinav-omprakas
fetched_at: '2026-02-08T19:12:20.812347'
original_url: https://www.abhinavomprakash.com/posts/i-am-happier-writing-code-by-hand/
author: Abhinav Omprakash
date: '2026-02-08'
published_date: '2026-02-07T15:30:23+02:00'
description: I felt the familiar feeling of depression and lethargy creep in while my eyes darted from watching claude-code work and my phone. “What’s the point of it all?” I thought, LLMs can generate decent-ish and correct-ish looking code while I have more time to do what? doomscroll? This was the third time I gave claude-code a try. I felt the same feelings every single time and ended up deleting claude-code after 2-3 weeks, and whaddyouknow?
tags:
- hackernews
- trending
---

I felt the familiar feeling of depression and lethargy creep in while my eyes darted from watching claude-code work
and my phone. “What’s the point of it all?” I thought, LLMs can generate decent-ish and correct-ish looking code
while I have more time to do what? doomscroll? This was the third time I gave claude-code a try. I felt the same
feelings every single time and ended up deleting claude-code after 2-3 weeks, and whaddyouknow? Every. Single. Time.
I rediscovered the joy of coding.

Yes, coding is not software engineering, but for me, it is a fun and essential part of it.
In order to be effective at software engineering, you must be familiar with the problem space, and this requires
thinking and wrestling with the problem. You can’t truly know the pain of using an API by just reading its documentation or implementation.
You have to use it to experience it.
The act of writing code, despite being slower, was a way for me to wrestle with the problem space, a way for me to find out that my initial ideas didn’t work, a way for thinking.
Vibe coding interfered with that.

If you’re thinking without writing, you only think you’re thinking.

– Leslie Lamport

The other major part of the job is to ensure correctness. For me, it is much harder to verify the correctness of code
I didn’t write compared to code I wrote. The process of writing code helps internalize the context and is
easier for my brain to think deeply about it. If I outsource this to an LLM, I skip over the process of internalizing
the problem domain and I can’t be certain that the generated code is correct.

By design, vibe coding has an addictive nature to it, you write some instructions, and code thatlookscorrect is generated.
Bam! Dopamine hit! If the code isn’t correct, then it’s just one prompt away from being correct,
right?right?

Vibe coding also has the profound effect of turning my brain off and passively accepting changes.
When it is time to use my brain, the inertia is much harder to overcome and it is easy to choose the lazy way out.
At my lowest point, I even asked it to do a find-and-replace in a file. Something that takes a few seconds, now took
minutes and a network call.

Even if I generate a 1,000 line PR in 30 minutes I still need to understand and review it.
Since I am responsible for the code I ship, this makes me the bottleneck.

The common view of vibe coding is that it is neither good nor bad, it is a tool. But tools shape your workflow and
your thought process, and if a tool prevents you from thinking deeply, I don’t think it is a good tool.
If you are a knowledge worker, your core competency is your ability to think, and if a tool interferes with that, be
afraid, be very afraid.

Now, I would be lying if I said I didn’t use LLMs to generate code. I still use Claude, but I do so in a more
controlled manner. I copy-paste files that I think are necessary to provide the context, and then I copy-paste code and
ask it to make changes to it or write tests for it. This friction has several benefits. I can’t make changes that span
multiple files, this means the generated diff isn’t too large, and if I have to manually change other files I know how
the code fits in. Manually giving claude the context forces me to be familiar with the codebase myself, rather than tell
it to just “cook”. It turns code generation from a passive action to a deliberatethoughtfulaction.
It also keeps my brain engaged and active, which means I can still enter theflow state.
I have found this to be the best of both worlds and a way to preserve my happiness at work.

Ultimately, life is too short to not optimize for happiness.Maybe(a big maybe) generating entire features would make me more
productive, but if it causes existential dread and makes me depressed, I don’t see it being productive in the long
run. Maybe you relate to some of the feelings. Maybe you don’t. But don’t be afraid to choose differently.
