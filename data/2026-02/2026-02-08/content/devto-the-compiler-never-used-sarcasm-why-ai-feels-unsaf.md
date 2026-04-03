---
title: 'The Compiler Never Used Sarcasm: Why AI Feels Unsafe to the Neurodivergent Coder - DEV Community'
url: https://dev.to/btarbox/the-compiler-never-used-sarcasm-why-ai-feels-unsafe-to-the-neurodivergent-coder-30i3
site_name: devto
content_file: devto-the-compiler-never-used-sarcasm-why-ai-feels-unsaf
fetched_at: '2026-02-08T11:09:38.819350'
original_url: https://dev.to/btarbox/the-compiler-never-used-sarcasm-why-ai-feels-unsafe-to-the-neurodivergent-coder-30i3
author: Brian Tarbox
date: '2026-02-02'
description: I have been writing code for 45 years. I started when "memory" was something you counted in bytes,... Tagged with ai, discuss, llm, programming.
tags: '#discuss, #ai, #llm, #programming'
---

I have been writing code for 45 years. I started when "memory" was something you counted in bytes, not gigabytes, and when a "bug" was nearly literal.

Over four and a half decades, I have watched languages evolve from Assembly to C, to Java, to Python. But through every iteration, one fundamental truth remained constant: The machine was literal. If I told the computer to do $X$, and it did $Y$, it was because I made a mistake in the instructions. It wasn't because the computer misunderstood my tone, or didn't like my attitude, or was having a bad day.

For a neurodivergent mind programming was more than a career. It was a sanctuary.

But today, as we shift toward Generative AI and Large Language Models (LLMs), that sanctuary is dissolving. We are moving from a world of explicit instruction to a world of implicit persuasion. For the neurodivergent coder, this isn't just a technical pivot; it is the loss of the only language that ever truly made sense to us.

## The Black Box Problem

We often refer to neural networks as "Black Boxes" because we don't truly know how they arrive at an answer. But here is the irony: The neurotypical mind is also a Black Box to us.

We flocked to computers because they were transparent boxes. We could see the registers, trace the execution stack, and inspect the variables.

By replacing explicit code with natural language models, we have essentially built a machine that mimics the neurotypical brain: it relies on context, implies rather than states, and is confidently wrong just often enough to make you doubt your own sanity.

## The Sanctuary of Syntax

To understand why this shift is so jarring, we have to look at theTheory of Mind.

In psychology, Theory of Mind is the ability to attribute mental states, beliefs, intents, desires, emotions, to oneself and others. It is the ability to understand that what is in my head is different from what is in your head. For many neurodivergent people, this is an exhausting, high-friction process. Navigating a dinner party requires constant, real-time calculation of social signals, subtext, and hidden agendas. If I tell a co-worker that “we’re going out for drinks” is that an implied invitation or just passing on some information? If it’s just information and you say “great, lets go” then you’re being rude and presumptuous. But, if it was an invitation and you say “well, that’s nice” then you’ve been rude and unfriendly. Why can’t people just be clear in what they say?

Coding required zero Theory of Mind.The compiler has no hidden agenda. It has no "mind" to theorize about. It operates on pure, unadulterated logic.Human interaction: "I'm fine" (Could mean: I am happy, I am angry, I am tired, or go away).Computer interaction: return 0; (Means: The function ended successfully).

For 45 years, the IDE (Integrated Development Environment) was a safe space where the rules of social engagement were suspended. The feedback was brutal, but it was honest. A syntax error isn't a judgment of your character; it is a factual statement about a missing semicolon. I recall back in those days thinking “well if you know the semicolon is missing why can’t you just add it?” The answer of course is that the compiler had no theory of mind and didn’t “know” what I wanted.

## The Invasion of Ambiguity

Enter Artificial Intelligence.We are told that "English is the hottest new programming language." We are told to "prompt" the machine. But prompting is not programming.Prompting is negotiating.

When we write a prompt for an LLM, we are suddenly thrust back into the messy world ofGrice's Maxims. Paul Grice, a philosopher of language, proposed that effective communication relies on the Cooperative Principle—rules regarding quantity, quality, relation, and manner.

Humans violate these rules constantly. We use sarcasm (violating Quality), we ramble (violating Quantity), and we are passive-aggressive (violating Manner).Traditional code strictly enforced these maxims. It was succinct, truthful, and relevant. But an LLM? It hallucinates (violating Quality). It gives verbose, flowery explanations when you ask for a boolean (violating Quantity). It requires you to "massage" the input to get the right output.

Suddenly, the "source code" is subject to the same linguistic ambiguity as a casual conversation. We have to guess how the model "feels" about a certain phrasing. We are essentially performing therapy on a matrix of floating-point numbers to get it to write a SQL query.

An example where ambiguity nearly caused an accidentThere was an accident when a pilot needed a go-around and told the co-pilot "takeoff power". That is an instruction to set full (takeoff) power to help the plane gain altitude. Unfortunately the co-pilot heard "take off power", which he interpreted as “remove power” so he set the engines to idle. This situation was exacerbated by the fact that all Air Transport communications are done in English, which was not these pilots' primary language. It’s hard to see how guardrails or contextual grounding could have helped here.

## The Shannon Limit of Certainty

I actually knew Claude Shannon. We lived in the same town and I was close friends with his daughter in high school and college. We were also both members of the MIT Juggling Club.

For those who only know the name from textbooks, Shannon was the "Father of Information Theory." He was the man who realized that all information could be represented in binary digits—bits. He gave us the fundamental unit of digital certainty.

In Shannon’s world, a "bit" was a measure of the reduction of uncertainty. It was the answer to a yes/no question. It was the mathematical opposite of ambiguity.

When we wrote code in C or Java for the last 45 years, we were living in the house that Shannon built. We were manipulating bits. We were resolving uncertainty. The goal of every line of code was to eliminate noise so that the signal was perfect.

But LLMs operate on a different part of Shannon’s work: The Entropy of English.

Shannon famously estimated the "entropy" (or unpredictability) of written English. He understood that human language is redundant and statistical. This is exactly how modern AI works—it exploits the statistical redundancy of language to predict the next word.

But here is the catch: Prediction is not precision.

By moving from traditional coding to Prompt Engineering, we are trading the Bit (absolute certainty) for the Token (probabilistic likelihood). We are leaving the noise-free channel of the compiler and wading back into the swamp of linguistic entropy—the very swamp Shannon helped us pave over with digital logic.

## Determinism vs. Probability: The Anxiety of "Probably"

The deepest friction, however, is mathematical.For decades, we lived in a Deterministic world.

If P, then Q. This is a binary comfort. It is verifiable. It is reproducible.AI introduces a Probabilistic world.P(Q|P)(The probability of Q, given P).

When I ask an AI to write code, it doesn't "know" the code. It predicts the next most likely token based on a massive dataset. It operates on vibes and statistical likelihoods.

For the neurodivergent thinker who finds comfort in patterns and rigid systems, this is a source of profound anxiety. We are moving from a system that is "Correct or Incorrect" to a system that is "Good Enough."

* Old World: You spent 3 hours debugging because the logic was flawed.
* New World: You spend 3 hours "prompt engineering",which is really just trying to figure out the magic words to persuade the black box to behave. And then spent another 3 hours validating that the generated code was correct (you did check, right?)

## Where Do We Go From Here?

I am not a Luddite. I’m an AWS Hero, AWS Ambassador and have 10 US technical patents. I use AI every day. It is a powerful tool. But I mourn the loss of the binary sanctuary.

We are entering an era where "coding" will look less like architecture and more like diplomacy. It will reward those who are good at linguistic nuance and persuasion, skills that have traditionally favored the neurotypical. On the other hand, intuitive leaps might actually favor the neurodivergent.

For those of us who spent decades finding solace in the absolute truth of a compiler error, we have to learn a new skill. We have to learn to tolerate the ambiguity of the machine, just as we have learned to tolerate the ambiguity of the world.

But I will miss the days when, if I said exactly what I meant, the machine did exactly what I said.

Brian Tarbox holds degrees in Linguistic Philosophy and Cognitive Psychology

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
