---
title: All the cool kids are doing it
url: https://www.scattered-thoughts.net/writing/all-the-cool-kids-are-doing-it/
site_name: lobsters
fetched_at: '2025-08-09T23:06:46.152015'
original_url: https://www.scattered-thoughts.net/writing/all-the-cool-kids-are-doing-it/
date: '2025-08-09'
tags: vibecoding
---

I haven't invested much time in LLM tools yet, but I don't have big loud reasons for that, more a jumbled drawerful of impressions and priorities.

This isn't going to be very exciting. Less "old man yells at clouds" and more "old man hasn't finished drinking his tea yet but is maybe thinking about going for a walk later".

The last company I consulted for were very heavy users of LLM tools. I found this out about a month into working with them. Prior to finding out, they seemed like an average startup with average productivity and average code quality. I certainly didn't feel surprised at their productivity, or shocked at their code quality, or really notice anything unusual at all except for the occasional little redundancy that a human probably wouldn't have written by hand.

The LLMs didn't seem to be able to help them much with their performance issues though, which is why I was working with them. I felt like most of the value I added was:

* reading and digesting big chunks of code
* figuring out what work is being done and how much of it was unnecessary
* refactor away unneccessary work, without breaking anything

That seems like something an LLM should be good at, but they don't seem to be there yet, or maybe my client was holding them wrong. They do seem to be very hold-wrongable.

I don't feel worried yet. At least for the kind of consulting work I tend to do, I still feel like I'm able to add plenty of value. If anything, I might even end up with more work in the short term if LLMs are very good at generating lots of code but not as good at performance engineering.

That probably won't be true forever, but it also doesn't seem like there is any reason to rush in now. Best practices for using LLMs apparently change rapidly, so skills I learn now probably wouldn't be useful in a few years anyway. And if the tools improve a lot over the next few years then they'll probably also be easier to learn to use, since much of the difficulty seems to lie in working around their limitations.

I could start using LLMs anyway, because it's fun being an early adopter and they're such bizarre and novel tools. But I don't think I'd enjoy it.

I'm told it's like managing a team of really smart and eager junior developers. But I've done that for real and I find it incredibly frustrating, I think due to a mixture of:

* Preferring to work on deep+narrow problems. I'm usually not writing a lot of code, but the code I am writing is subject to many conflicting constraints, has a complicated state space, is difficult to test exhaustively etc.
* Having mostly tacit knowledge. I don't know what advice to give because I don't actually know how I solve problems.

The combination of the two makes it difficult to gain efficiency by offloading parts of the work to someone with less context/knowledge/experience. I can't explain what I want because I haven't figured it out yet, and I figure it out by doing it, repeatedly, until it comes out right. I don't want to hire someone to fill in the details for me because I so often find that the details are important, and that I understand them by grappling with them myself.

Of course with actual junior developers, the point is not to get the work done but to help them evolve intogyaradoscompetent engineers. But the LLMs don't learn (yet). I can see how magikarp-as-a-service could be useful if you have a lot of parallelizable tasks, but I'm not usually in that position.

For my research in particular the main bottleneck is not producing code but maintaining motivation. It's hard to keep banging your head against the same wall for years without visible progress. Even if LLMs gave me a boost in efficiency, I'm wary that they might also cost me extra frustration that I can't afford.

Also a bunch of money. The good tools have an expensive monthly fee.

I do spend money on tools, sometimes a lot. But they all amortize - the more value I get out of them, the more I use them, the cheaper they get. LLMs would be the only tool I use that would get more expensive the more I rely on them. I feel a little frazzled about the idea of running out of coding and having to wait until my cap resets next week.

Also, if I'm going to invest a lot of time in a tool, I prefer tools that have a stable interface, are likely to work for a long time, and are possible to patch/shim. I hate running up the escalator.

LLMs seem like a bad bet on both fronts. The tools seem to change every week. The big companies aren't profitable right now and they're digging the hole deeper as fast as they can. Maybe there will be big gains in efficiency, or maybe it's not actually possible to offer this service at a reasonable price, or maybe it is but they dig the hole so deep they blow up anyway.

For uses other than writing code, I'm a little more interested.

I signed up for trials of each of the major chatbots and tried using them as an alternative to search, or to help with research, but I've mostly either broken even or wasted time. When humans bullshit me it's usually easy to tell because there is a lack of concreteness to their explanations - they haven't actually wrestled with the details so they avoid talking about them. But LLMs are so good at making up plausible details! I find it's much more work to fact-check LLM output than human output.

Eg fora survey on code reloadingI asked both claude and chatgpt how erlang handles reloading code when closures still exist. I vaguely remembered how this works but wanted to find an actual reference. Both of them explained in great detail and with examples how old code is not unloaded until all the closures referencing it are garbage collected, which is not true.

My last client used an LLM code review service. Sometimes it behaved like a slightly smarter linter and warned me about actual mistakes - "you did X here and here and here but Y here - should it be the same?". Whenever it reasoned about dataflow beyond a single function it was usually wrong. Often it just seemed to be bluffing - "the code that you changed results in changed behaviour" isn't a bad heuristic but it gets tiresome when you say it every time. But I can imagine paying for a better version in a few years.

I've seen some interesting work on using LLMs to generate mutations for fuzzing. This seems really promising, although too expensive for me to play around with just yet. But the ability to generate a large volume of plausible-but-subtly-wrong code is exactly what a compiler fuzzer wants for christmas.

ForHYTRADBOIthis year the machine transcription cost much less and was much more accurate than three years ago. I still had to correct a lot of mistakes (eg it consistently misheard DuckDB as DougDB), but it took me about 20 minutes per video, down from about 60 minutes last time.

For writing code I'm still unconvinced. I don't think it would have non-zero value to get into, but the cost-benefit just doesn't put it at the top of my priority list yet. That could change if the tools get much better, or if they get commoditized, or if local models become competitive. But I don't feel any urgency right now.

The funny thing is that I keep seeing people make the comparison that soon nobody will write code at all, just like nobody writes assembly today. But I think the thing that does make the top of my priority list today is learning to write assembly. I always end up having to look at generated code and I can sort of piece it together, but I'd like to be fluent rather than pidgin. I also keep seeing people produce magic with little stretches of specialized instructions that I've never heard of, and I want some of that.

As a final irony, the one good use I've found for claude so far is that it's pretty good at explaining assembler syntax. You just can't google the punctuation.
