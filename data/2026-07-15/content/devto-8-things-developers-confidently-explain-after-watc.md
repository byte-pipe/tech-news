---
title: 8 Things Developers Confidently Explain After Watching One YouTube Video - DEV Community
url: https://dev.to/sylwia-lask/8-things-developers-confidently-explain-after-watching-one-youtube-video-3jio
site_name: devto
content_file: devto-8-things-developers-confidently-explain-after-watc
fetched_at: '2026-07-15T11:33:04.012409'
original_url: https://dev.to/sylwia-lask/8-things-developers-confidently-explain-after-watching-one-youtube-video-3jio
author: Sylwia Laskowska
date: '2026-07-14'
description: I just got back from my vacation which, like 99% of Polish people, I spent in Croatia. Dobar dan!... Tagged with jokes, webdev, ai.
tags: '#jokes, #webdev, #ai'
---

Humorous look at LinkedIn gurus

I just got back from my vacation which, like 99% of Polish people, I spent in Croatia.Dobar dan!🇭🇷

I've got a really fun article in my head right now, but it needs a bit of research before I can publish it, so that'll be coming next week. In the meantime, let's do something much lighter.

BTW, a small update.I said that FrontKon would be my last conference this year... well, apparently I lied. 😂 WheniJS Munichreaches out, you simply don't say no. Especially after looking at the speaker lineup. It's basically a conference full of geniuses... plus me. 😅 So I'll be speaking there at the end of October aboutWebAssembly and WebGPU in React,and I'm already ridiculously excited.

If you happen to have a spare bag of money lying around xDDD (or, much more realistically, your company still has some training budget left), come and say hi! I'd love to meet some of you in person. 😊

Anyway... let's get back to today's topic.

As many of you probably know, I have a soft spot for LinkedIn gurus and people who explain everything with absolute confidence. You know the type: their solution is always the best one, everyone else is wrong, and there are absolutely no trade-offs. 😄

Sometimes I get the feeling that at least some of that confidence comes directly from a single 15-minute YouTube tutorial.

But let's be fair for a second. Who among us hasn't watched a short video, finished it thinking"Yep, I totally understand this now!", and then discovered during the actual implementation that reality was... slightly more complicated? 😂

Since I spend most of my time working with JavaScript and AI agents these days, most examples will probably come from those areas. Feel free to add your own in the comments!

## 1. React / Angular / Vue (cross out the unnecessary one) is the best framework

This is probably the most common opinion after watching an internet guru, especially if you haven't formed your own yet.

Angular is the best because it has everything. React is the best because everybody uses it. Vue is the best because... well... Vue people will tell you why. 😄

Then you spend a few years building real projects and suddenly discover that all of these have strengths, weaknesses and different use cases. In the end, the "best framework" is usually just the one that solvesyourproblem best.

## 2. LLMs are just autocomplete

Or, if you prefer another popular version:

"They're just stochastic parrots."

"They're not creative."

"They don't really understand anything."

Well... if it's all that simple, why do entire teams of researchers and engineers spend years working on them? Why are companies burning through billions of dollars worth of GPUs? 😄

Another statement that always makes me smile is that LLMs "aren't creative." Sure, they probably won't invent something completely detached from everything humanity has ever known.

But then again... neither do most humans.

Most people don't wake up one morning and invent quantum mechanics or writeThe Lord of the Rings. Creativity is usually about combining existing ideas in interesting ways, and LLMs are actually surprisingly good at that.

## 3. CQRS (or Redux on the frontend) is easy

Sure. Then you open the codebase and suddenly you're staring into the architectural equivalent of a horror movie.

I've honestly seen everything. Business logic split between Redux stores and components. Half the state managed globally, the other half locally. Actions that somehow contain business logic. Reducers that apparently decided to become services.

Years ago, when I was interviewing developers more often, I used to ask a very simple question:"Why do we actually need CQRS (or Redux)?"(By the way... not everyone even knew the difference between the two.) Then I'd ask another one:"Why can't we solve this in a simpler way?"

I swear, a surprising number of people answered something like:

"I don't know... that's just how people do it."

## 4. AI agents are just a while loop

To be fair! A good friend of mine, and my former tech lead, actually gives an excellent conference talk with exactly this title. It's intentionally provocative.

And let's face the truth... there is quite a bit of truth to it. Many AI agents really are "just a while loop."

The funny part starts about three weeks later. Suddenly your tiny little while loop has three MCP servers, an orchestration framework, retries, memory, tool calling, etc, etc...

Still one of the most fun things I've worked with recently, though.

## 5. WebAssembly is always faster

Whenever someone says this, I always ask the same two questions:Faster than whatAnd faster at doing what?

Don't get me wrong, WebAssembly is amazing. There are plenty of scenarios where it absolutely destroys JavaScript performance, especially when you're dealing with computationally intensive algorithms, simulations or similar workloads.

But if your application spends most of its life waiting for HTTP requests to finish... WebAssembly probably won't make the internet faster.

And it probably won't suddenly turn your dashboard into NASA software either. 😄

## 6. Unit tests are our golden ticket

Especially the ones generated by the same LLM that just generated the production code. 😂 100% confidence!

Or... maybe not.

This can be particularly misleading on the frontend, where unit tests often verify exactly the code that was the easiest to write in the first place.

Congratulations, you've successfully achieved 100% test coverage, and 0% confidence!

## 7. Let's just add RAG

Yeees...

As if finding, cleaning, maintaining and selecting the right documents was somehow the easy part. 😄

## 8. Microservices / Microfrontends are the only good architecture

Absolutely! Especially if your application consists of six screens and one backend service. 😄 Or if you've got a perfectly healthy monolith that everyone on the team understands.

Sometimes a distributed architecture is exactly what you need. Sometimes it's just distributed complexity.

I could probably keep going for another twenty examples, but I think that's enough for today. 😂

What about you? Have you ever met one of those"one-YouTube-video gurus"?

If you enjoyed this article, consider following me also onLinkedIn:https://www.linkedin.com/in/sylwia-laskowska-5a8467131/

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (23 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse