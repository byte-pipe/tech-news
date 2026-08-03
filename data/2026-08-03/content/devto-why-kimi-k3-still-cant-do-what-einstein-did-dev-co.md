---
title: Why Kimi K3 Still Can't Do What Einstein Did - DEV Community
url: https://dev.to/dannwaneri/why-kimi-k3-still-cant-do-what-einstein-did-2l6d
site_name: devto
content_file: devto-why-kimi-k3-still-cant-do-what-einstein-did-dev-co
fetched_at: '2026-08-03T19:33:24.979978'
original_url: https://dev.to/dannwaneri/why-kimi-k3-still-cant-do-what-einstein-did-2l6d
author: Daniel Nwaneri
date: '2026-07-29'
description: In geophysics you almost never get to see the thing you're studying. You get a seismic trace, a... Tagged with ai, llm, rag, discuss.
tags: '#discuss, #ai, #llm, #rag'
---

RAG surfaces echoes, but misses paradigm shifts

In geophysics you almost never get to see the thing you're studying. You get a seismic trace, a gravity anomaly, a resistivity curve. You don't get the rock. You get the rock's echo, and you have to guess at a structure underground that would produce exactly that echo and no other. Nobody hands you the answer key. You infer the case from the result.

I hadn't thought about that part of my degree in years, until I built Bookmark Brain.

Bookmark Brain is a RAG pipeline trained on my own X bookmarks and likes, saved since 2016. It was around 50,000 the last time I wrote about this. It's 70,000 now. Cron jobs pull in new saves on their own; there's no manual re-curation involved. Ask it something and it retrieves the closest matching saved content, then composes an answer that sounds like me. It works well. Too well, honestly. When I asked it about API design opinions, it sounded more like me than most general-purpose models do when I prompt them to write in my voice.

The reason isn't the model. It's the retrieval layer. My bookmarks are coherent because I spent a decade curating them into a specific worldview. The bot just finds the nearest neighbor and composes a fluent sentence around it. What it can't do is the thing I actually needed a few times while testing it: resolve a contradiction between two things I'd bookmarked years apart. It doesn't reconcile them. It picks whichever one is semantically closer to the question and hands that back.

That's not a bug in my pipeline. That's the whole category of thing retrieval can't do.

A 2014 blog post by Amni Rusli, "Irreplaceable Us," made roughly this same argument, minus the RAG pipeline. Machines work within given parameters, she wrote — feed them data and code and they'll optimize inside that space forever. What they can't do is leap into a different pond of parameters entirely and haul something back. She used Einstein and Dirac as her examples. Einstein reading Hume and Mach until he had the nerve to throw out absolute simultaneity. Dirac telling Bohr that Klein had already solved the relativistic electron problem and going looking for a different answer anyway, because the existing one didn't fit his "darling" theory.

Twelve years later, in January, Google DeepMind published a paper making the same claim with the informality stripped out. Tom Zahavy's "LLMs Can't Jump" starts from a diagram Einstein actually drew, in a letter to Maurice Solovine: sense experience jumping to a system of axioms, then deduction working forward from there. Peirce had a name for the gap in that jump, and the paper borrows it. Deduction: rule plus case gives you a result, the only mode that guarantees truth. Induction: case plus result gives you a rule, which is close to what training an LLM on a trillion documents actually is. Abduction: rule plus a surprising result gives you a new case, or a new rule, to explain it. That's the geophysics move. That's resolving the contradiction in my own bookmarks. That's the one nobody has automated.

The paper's argument for why scaling doesn't fix this is data scarcity. General relativity wasn't induced from a mountain of prior experimental results, because there wasn't one. The axioms can't have been deduced either, since deduction only runs forward from premises someone already has. Something else produced the premises. That something is the jump, and it's still missing.

Then Kimi K3 shipped. 2.8 trillion parameters, the largest open-weight model ever released, benchmarking close behind Fable 5 and GPT-5.6 Sol on coding and agentic tasks. Moonshot's own claim is 2.5x the intelligence per unit of compute over their last generation. None of that changes the argument. A bigger training set makes induction better and deduction more reliable over longer chains. It doesn't add a third capability that wasn't there before. Feed a model more of the internet and you get a more convincing compositor, not a different kind of thing.

I said this to a commenter under my original bot post, before I'd read the DeepMind paper: a model trained on Newtonian physics at sufficient scale would produce better Newtonian predictions, not special relativity. Turns out that's the whole thesis, just arrived at from a different direction — one from watching my own retrieval logs, one from a formal read of Peirce.

Which brings me back to my own bookmarks.

What actually happened at bookmark-time, every time I decided a tweet was worth saving, was a small version of the jump. This connects to that. This contradicts what I believed last year. Keep it. I've been doing that since 2016 — a decade of small jumps, one save at a time. Bookmark Brain inherited the residue of all of them. It never makes one itself.

That's the part that should worry people more than the benchmark charts do. Not that the model can't out-think Einstein. That most of what gets paid for isn't the jump either.

I write the essay, but I bookmark the argument first. That's where I'm putting the hours now — not in the composing, which the model will keep getting better at, but in the deciding what's worth saving. The jump doesn't scale. Mine, at least, still has to happen one bookmark at a time.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (21 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse