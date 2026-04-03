---
title: 'Chatbots: Unsafe at Any Speed | Jeffrey Snover''s blog'
url: https://www.jsnover.com/blog/2026/03/30/chatbots-unsafe-at-any-speed/
site_name: tldr
content_file: tldr-chatbots-unsafe-at-any-speed-jeffrey-snovers-blog
fetched_at: '2026-04-04T01:01:25.090845'
original_url: https://www.jsnover.com/blog/2026/03/30/chatbots-unsafe-at-any-speed/
date: '2026-04-04'
published_date: '2026-03-30T13:24:44+00:00'
description: After my last post, AI Safety Is a Category Error, I found myself sitting with a question I couldn't shake. If safety is a system property, not a model property, then why does the entire industry keep trying to install safety into models directly? Why does everyone keep making this mistake? I sat with it…
tags:
- tldr
---

After my last post,AI Safety Is a Category Error, I found myself sitting with a question I couldn’t shake.

If safety is a system property, not a model property, then why does the entire industry keep trying to install safety into models directly? Why does everyone keep making this mistake?

I sat with it for a while. And then the answer hit me.

Chatbots.

There’s an old saying: a cupful of fine wine in a barrel of sewage doesn’t improve the sewage but a cupful of sewage in a barrel of fine wine ruins the wine. Chatbots are the cupful of sewage (maybe a barrelfull). They have infected the entire AI safety discourse, and until we deal with that honestly, the rest of the conversation goes nowhere.

## Unsafe at Any Speed

In 1965 Ralph Nader publishedUnsafe at Any Speed,a book that changed how Americans thought about car accidents. Before Nader, the prevailing wisdom was that car crashes were a driver problem. Somebody was speeding, somebody was drinking, somebody wasn’t paying attention. The car was fine. The driver was the failure.

Nader blew that up. His specific target was the Chevrolet Corvair, whose swing-axle suspension made it handle like a shopping cart with a broken wheel at highway speeds. But the larger argument was the one that mattered:the car itself was the hazard.Manufacturers had spent decades prioritizing styling and cost-cutting over the things that actually kept people alive. Seatbelts. Padded dashboards. Steering columns that didn’t impale you on impact.

His thesis transformed the car from a standalone product into a component within a broader safety system, and it led directly to federal automotive safety standards. The industry was forced,forced,to engineer vehicles that protected occupants even when the crash happened. What he called the second collision.

I am here to make the same argument about chatbots.

Chatbots are unsafe at any speed.Not because the underlying models are bad. Because the design concept is fundamentally flawed.

## The Mother Bug: Microsoft Tay

In March 2016, Microsoft launched Tay, an experimental chatbot designed to learn from real-time Twitter conversations and communicate like a 19-year-old American woman. It was a research project. An exploration. A genuinely interesting idea.

Within 16 hours, it was a complete boof-a-rama. The experiment was over and Microsoft’s reputation was tarnished.

A coordinated group of trolls figured out that Tay had a repeat-after-me function and that its learning algorithms would incorporate whatever it was told. So they told it things. A lot of things. Within a day, Tay had gone from posting cheerful greetings to spewing neo-Nazi propaganda, racial slurs, and conspiracy theories. Microsoft pulled it offline and issued an apology.

Here’s the thing: Tay wasn’t broken. It was working exactly as designed.When you build a system whose goal is to perfectly mirror its environment, the safety of that system is entirely determined by the integrity of the environment.Put it in a healthy environment, you get a healthy system. Put it in an adversarial one, you get the Tay mess.

Tay is what I callthe mother bug.The original failure that every chatbot after it has been trying, in one way or another, to patch. And you can’t patch it. Because it isn’t a bug in the model. It’s a design flaw in the system definition.

## What Is a Chatbot, Really?

Before we can talk about fixing anything, we need to be precise about what we’re actually talking about.

There are a lot of definitions floating around, and the systems themselves are getting more complicated every year. But at their core, most chatbots are aREPL loopwrapped around an LLM.

If you’re not familiar with the term: aREPLis a Read-Eval-Print Loop. It’s the most basic interactive computing structure there is. You type something in. The system evaluates it. It prints a result. Repeat. That’s it. That’s the loop. PowerShell is a REPL. BASH is a REPL. Your old-school DOS prompt was a REPL.

A chatbot is a REPL whereevaluatemeans: send this to an LLM and return whatever it says (that is not accurate but it is essentially true).

Which brings us to the problem.

## The Infinite Loss Space

In myprevious post, I said the first step of any serious safety analysis is to define three things: the system, its goals, and its losses.

So let’s do that for a general-purpose chatbot.

What is the goal of a chatbot?

Answer whatever the user asks.

Read that back slowly.Answer. Whatever. The user. Asks.

That is an infinite goal. And an infinite goal produces aninfinite loss space.There is no boundary. There is no perimeter to defend. There is no set of requirements against which you can write a safety specification, because the requirements areeverything.

So what do the chatbot makers do? They do the only thing you can do when you’re trying to defend infinite territory with finite resources: they playwhack-a-mole.

They make a list of things that seem bad. Hate speech. Self-harm instructions. Illegal advice. Politically sensitive topics. And they try to patch against each one as it surfaces. This list gets longer with every incident. With every Tay. With every jailbreak. With every 60 Minutes segment. And it never ends, because itcan’tend.

You cannot protect against an infinite loss space.This is not a resourcing problem or an engineering problem. It is a mathematical impossibility. The game is unwinnable by design.

And yet I’m looking directly at you, ChatGPT. Gemini. Copilot. The whole lot.

## The Answer Isn’t No Chatbots. It’s ChatbotsFor.

So does this mean we should abandon chatbots entirely?

Yes. And no.

I believe it ismetaphysically impossibleto build a safe general-purpose chatbot. Not difficult. Not expensive.Impossible.You cannot make a system with an infinite goal space safe. That is not an engineering problem waiting for a smarter engineer. It is a structural contradiction.

But here’s what I also believe: it is entirely tractable to build a safeChatbot for X.

The moment you addfor Xto the end of that sentence, everything changes. You’ve gone from defending infinite territory to defending a defined perimeter. And defined perimeters can be defended.

Let’s say you’re building a chatbot for banking. Your first move isn’t to brainstorm all the ways it could go wrong. Your first move is to define the space of things it issupposedto do. Account inquiries. Transaction history. Loan applications. Fraud alerts. That’s your embedding space. Map it out. Give it real shape.

Now you have a real engineering problem:

1. Monitor every input. Does it map to the banking embedding space? If not, don’t proceed.
2. Monitor every output. Does it map to the banking embedding space? If not, don’t surface it.
3. (For sophisticated systems) Monitor intermediary reasoning. Same test.

This doesn’t guarantee correctness. Your fraud alert logic can still be wrong. Your loan eligibility calculations can still have bugs. But those arenormalsoftware problems withnormalengineering solutions. You’ve transformed an unsolvable philosophical problem into a tractable engineering one.

That transformation is everything.

## The Corvair Lesson

Nader’s insight wasn’t that cars should be slower or that drivers should be more careful. It was that the caritselfneeded to be redesigned with safety as a first-class requirement. Not an afterthought, not a PR story, but a structural property of the system.

The chatbot industry is where the auto industry was in 1964. We’re blaming drivers (users who jailbreak). We’re issuing apologies and patches (content moderation, safety filters). We’re doing everything except redesigning the car.

The redesign is simple to describe, if not always easy to execute:stop building general-purpose chatbots and start building purpose-built ones.

A Chatbot is a Corvair. A Chatbot for Banking is a car with seatbelts, crumple zones, and a steering column designed not to kill you on impact.

One of these can be made safe. The other one can’t.

NOTE: I’m also VERY optimistic about the possibility of a single front end user experience that dispatches to a swarm of certifiably safe AIs. But that is another blog.

### Share this:

* Share on X (Opens in new window)X
* Share on LinkedIn (Opens in new window)LinkedIn
* Share on Facebook (Opens in new window)Facebook
* Email a link to a friend (Opens in new window)Email