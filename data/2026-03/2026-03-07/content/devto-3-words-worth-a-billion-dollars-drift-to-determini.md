---
title: '3 words worth a billion dollars: Drift to Determinism (DriDe) - DEV Community'
url: https://dev.to/grahamthedev/3-words-worth-a-billion-dollars-drift-to-determinism-dride-dej
site_name: devto
content_file: devto-3-words-worth-a-billion-dollars-drift-to-determini
fetched_at: '2026-03-07T19:09:31.982695'
original_url: https://dev.to/grahamthedev/3-words-worth-a-billion-dollars-drift-to-determinism-dride-dej
author: GrahamTheDev
date: '2026-03-07'
description: I doubt I am the first to come up with this concept, but I am probably the first to name it. Drift... Tagged with webdev, ai, automation, architecture.
tags: '#webdev, #ai, #automation, #architecture'
---

I doubt I am the first to come up with this concept, but I am probably the first to name it.

Drift to Determinism (DriDe - as in "DRY'd" - Don't Repeat Yourself) is what everyone will be doing in 2 years, and I am telling you to start today.

And if you want the one liner explanation: I am proposing that while most people are trying to add more AI and then guard it, instead we should be building systems in a way that we write AI out of them entirely / as much as possible over time.

## Ok smart boi - what is Drift to Determinism?

Well it isn't the long awaited second instalment of Fast and The Furious 3 (sadly - but that would be an awesome title right?).

No it is a philosophy on how you should be thinking about AI.

Everyone is out there using AI agent systems and burning tokens like they are going to run out one day.

Watching people spend $20 to set a reminder to buy milk just hurts my soul (yes, really, that happened...the heartbeat every 30 minutes to check the time waseatingtokens!).

I believe we will wake from this fever dream soon where "all things are solved with AI" and realise there is a simple flow that will make us able to do almost anything, at a fraction of the cost and environmental impact.

Simple steps:

1. Give the AI agent system a "novel" task it hasn't seen before and let it burn a load of tokens to solve it.
2. Put a second agent system at the end watching what could have been worked out deterministically (i.e. in code).
3. Build the tools for the repeatable parts.
4. Next time a similar task comes along - feed the tools in at step 1.
5. See if we always use tool1 and feed it to tool6 - wire them together.
6. Repeat the process until you write out every part of the AI that is possible.
7. There are loads of little nuances like falling back to AI if a tool doesn't give the right output for this job, running shadow versions of workflows to check we are actually improving, providing final output feedback to fine tune, producing a system that the LLM can understand, full tracking of the process...but you can work that out right :-)

Over time your AI powered non-deterministic workflows that cost $50 to run and only work 50% of the time without you side-prompting it back on track become glorious automations that use $0.02 in AI to categorise them and then just run in code.

It's faster, it is more consistent, it can be trusted.

This is where we are headed.

## Yeah, people are building skills and tools, what is new here?

That is the point - we already kinda have the things we need to make this work, but fundamentally miss the mark on how we treat them.

Nobody, and I mean nobody has the objective to write AI out of a process they are currently doing with AI.

You name me one tool / product that has used AIlessin the last year.

Go on, I am waiting.

And yet that is actually what I am proposing.

You use AI to get the outline of a process down. It is expensive, slow (in comparison to code) but it solves a repetitive business process problem.

Then, you analyse that process. Do I really need to pass all 12000 rows of our company client list into AI to know who to call next? Nope, simple tool to grab the next 5 people not called in a month.

Do I even need to give that tool to the agent? No, I should make it part of context so that it has that info and we save a load of round trips.

Hang on a minute, are we giving the AI a tool to then go look up their website? Well if it needs that info we should just do that automatically and feed that into the context.

Hang on a minute, we have scanned their website before? We have the info? Do we even need the agent to fire up at all?

You get the idea.

## Crystallisation is the key

Every time you call an AI you roll the dice - quite literally.

It has gotten a lot better, but it is and will always be a non-deterministic system. It will always give different output no matter how hard you prompt it.

Sometimes you need the power of AI - for example to process natural language (or do you)?

Or to write code (or do you?)

Every time you call AI, question how much of it needs to be done fully autonomously using a LLM and how much is a deterministic step.

Writing code - well we have every code snippet in the world available, every challenge can be broken down into code that already exists and has been battle tested. We just need to wire it up differently.

So should we be letting AI write the code, or give it code we know works and ask it to wire it together to solve a novel problem?

Processing natural language? Well we have had code based tools that can do 70% of the work a LLM can do - why not get them to do a first pass and find the areas to focus the power of an LLM at, reducing context size, cost and chance of missing key bits?

CRYSTALLISEyour process. Make it as deterministic and repeatable as possible.

## Sounds like a lot of work

Well, yeah, kinda.

There is certainly a capability gap at the moment where LLMs are decent at spotting where to optimise a process, but not creative enough to work out which bits are best to work on.

It still needs human judgement and guidance (hurrah - we are still safe for now!).

But it can certainly look at what it did and then give you areas to poke at.

It can certainly then take your judgement and offer possible solutions.

All it needs your grey matter for is what to work on, which way to approach it and how specialised or generalised to make a function / step.

Once you have built enough of these tools (skills, MCP, workflows, whatever) then you can teach it to build its own workflows.

You then become the judge of the workflows, rather than the judge of individual parts.

## My prediction

In 2-5 years you will be sat at your terminal with a novel problem for your business. We need to reconcile the bank automatically for accounting.

You explain the desired outcome, provide examples of good and bad results, the data etc.

AI will look at all its tools and build you a workflow to achieve this. It doesn't have all the tools it needs yet so it still uses vision models, LLMs that are good at categorising etc.

You will run it in test mode, work with the AI to adjust it for edge cases and then run it. It does the job, you push it to "shadow mode" and run it alongside the current process.

Now it starts optimising itself out of the process.

It builds out individual parsers for every supplier's invoice format using OCR and pattern matching, running in milliseconds on each invoice. It pulls the bank feed back and checks the amount against the invoice, all in code, the LLM doesn't even fire up, except to kick off the "reconciliation flow".

It works just as well as the current process with 99%+ accuracy as we are using deterministic steps for 99% of the workflow.

3 months later one of the documents we feed in changes format - the tensorflow OCR tool fails to find the invoice number. It falls back to a vision model that locates the new location of the invoice number. Prompts you "hey, looks like supplier X's invoices have changed format - is this the right number" showing you a screenshot of the invoice and a highlight around the relevant items.

You tell it it is good to go and it self heals and runs off to complete this months bank reconciliation.

Compare that to how we would currently envision doing it: a call to a vision model for every single invoice, provide the LLM with a tool for that. Then we give it a tool to read the bank transactions - sending private data out to the cloud. Then it confuses an invoice number for a account number, asks for help, we prompt it and it updates it's instruction set, only to fail again on the next invoice.

It is costly, slow, error prone and although it is better than our old fully human process, it is nowhere near ideal.

## How I think of LLMs

Every single token output by a LLM is a point of failure.

Even if we get LLMs to 99.999% accuracy (which would be amazing right?), if you had a workflow that had 10000 passes how accurate would your output be?

No not 99%, it would be 90%. (0.99999^10000 is 90%)

*90% accuracy is business destroying: you are getting sued or going bankrupt. *

But if you build your LLM system with a single goal for the LLM: "make yourself obsolete" - then you can flourish.

You can remove all of the mundane from the business, all of the human effort going into busy work.

The LLMs give you the power to reduce the cost of building automations to 1% of what they used to cost to implement.

Small businesses can out-compete the big players with agility on a scale never seen before.

But only if their systems are robust.

## So, are you building a Hallucination Factory or a Deterministic Dynamo?

Are you building a token incinerating, dice throwing monster?

Or are you building a streamlined, bullet-proof replacement for inefficiency?

Probably somewhere in-between, but if your guiding principle in everything you do isDriDe- then as you Drift to Determinism and Don't Repeat Yourself you will gain an edge.

You will have a sharp surgical tool automating key workflows while your competition is bludgeoning their process into submission and veering towards a disaster.

The reduction in costs, the increase in certainty, the avoidance of lawsuits - all from 3 words must easily be worth a billion dollars.

Let DriDe guide you to success, start the drift today.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse