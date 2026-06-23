---
title: . .. . ... . .... . .... . ... . - DEV Community
url: https://dev.to/lovestaco/--2kb7
site_name: devto
content_file: devto-dev-community
fetched_at: '2026-06-24T01:01:44.218527'
original_url: https://dev.to/lovestaco/--2kb7
author: Athreya aka Maneshwar
date: '2026-06-22'
description: Hello, I'm Maneshwar. I'm building git-lrc, a Micro AI code reviewer that runs on every commit. It is... Tagged with ai, webdev, programming, beginners.
tags: '#ai, #webdev, #programming, #beginners'
---

Hello, I'm Maneshwar. I'm building git-lrc, a Micro AI code reviewer that runs on every commit. It is free and source-available on Github.Star git-lrcto help devs discover the project. Do give it a try and share your feedback.

I just gave Claude a dumb little dot puzzle.

. .. . ... . .... . .... . ... .

Enter fullscreen mode

Exit fullscreen mode

It replied that the missing ending was:

.. .

Enter fullscreen mode

Exit fullscreen mode

At first I thought:

"Hold on... LLMs only predict the next token.They don't execute algorithms.They don't reason.So how did it figure this out?"

That question sent me down a rabbit hole.

Because if you check the answer, it'sright.

The single dots are separators; the real clusters climb2 3 4, then mirror back down4 3 2.

Reading the dot counts end to end gives a clean palindrome:

1 2 1 3 1 4 1 4 1 3 1 2 1

Enter fullscreen mode

Exit fullscreen mode

And here's the thing this is a puzzle the model may havenever seen before.

The folk model I'd been carrying around says an LLM "just guesses the next word based on vectors and whatever it saw in training."

If that's all it does, a tough puzzle should stump it.

There's no next-word statistic to lean on.

So either that mental model is wrong, or something more interesting is happening.

It's the second one. Here's what I dug up.

## "Predict the next token" is the goal, not the method

Yes, these models are trained to predict the next token (roughly, the next chunk of text).

That part of the folk explanation is true.

But here's the thing people skip over:that's the objective it was scored on, not a description of what it learned to do.

Think about a student who only ever gets graded on exam questions.

Technically all they "do" is answer exam questions.

But to get good at that and across thousands of varied questions, they can't just memorize answers.

They have to actually learn arithmetic, logic, how to read a problem.

The exam is thepressure.

The understanding is what growsunderthe pressure.

Same deal. To predict the next tokenwellacross trillions of tokens i.e text that includes math, code, arguments, stories, and yes, puzzles memorizing "word X tends to follow word Y" is hopeless.

The space of possible inputs is effectively infinite and almost everything you feed it is novel.

The only way to drive prediction error down at that scale is to develop internal machinery that generalizes: counting, comparing, recognizing symmetry, continuing a pattern.

Those abilitiesemergedbecause they were useful for the prediction task.

Nobody hand-coded a "detect palindrome" function.

It's a capability that fell out of relentless optimization, the same way a student's actual understanding falls out of relentless testing.

If the student analogy doesn't land for you, here's the one that clicks for most devs:compression.

Imagine you had to compress every book ever written into the smallest possible representation.

You wouldn't get far storing raw text, you'd be forced todiscoverthe underlying regularities: grammar, recurring narrative structures, arithmetic, the rules of chemistry, how code is shaped.

Not because anyone taught them to you, but because capturing those concepts is the most efficient way to represent the data.

Training an LLM to predict text is the same squeeze.

Good predictionrequirescompact internal models of the patterns in the world, so the model builds them.

This is the single biggest upgrade to make to the folk model:next-token prediction is the training signal, and general competence is the strategy the model found for satisfying it.

## Plot twist: my puzzle isn't really about dots

Before we get to the mechanism, one thing that reframed it for me.

The model never "sees" dots.

It seestokens, whatever chunks the tokenizer splits the input into. And the exact split doesn't matter, because to the model my puzzle is structurally identical to:

A AA A AAA A AAAA A AAAA A AAA A

Enter fullscreen mode

Exit fullscreen mode

or

1 2 1 3 1 4 1 4 1 3 1 ...

Enter fullscreen mode

Exit fullscreen mode

The dots are just the costume.

What the model actually works with is theabstract shapeof the sequence, separators interleaved with a rising-then-falling count.

That's a big clue about why it generalizes: it isn't pattern-matching on "dots," it's operating on structure that's independent of the symbols carrying it.

## The part the folk model leaves out entirely: attention

The "each word relates to the previous word, fixed from training" picture is missing the mechanism that does the heavy lifting.

It's calledATTENTION, and it's the core of the transformer architecture every modern LLM is built on.

Here's the intuition.

When the model processes your input, every position can "look at" every other position and compute how they relateon the fly, for this specific input.

It's not a frozen lookup baked in at training time.

It's a fresh computation each time you hit enter.

So with the dot puzzle, nothing pulled up a stored "dot puzzle answer." Instead, roughly:

* The repeating single dots got recognized as a separator element.
* The clusters got compared against each other.
* The rising-then-falling counts (2, 3, 4, 4, 3, …) got represented as astructure, one that "wants" to keep descending.

And those token vectors? They're not just "the meaning of this symbol."

They carry abstract features that can be manipulated almost geometrically.

"Mirror this sequence" is exactly the kind of operation that becomes tractable when your data lives as vectors in the right space.

Counting and reflecting stop being magic and start being arithmetic on representations.

There's also adepthdimension worth naming.

Attention isn't a one-shot pass, the representation gets refined as it flows through dozens of layers, each adding a little more abstraction.

A loose, illustrative intuition (not literally what any layer "thinks"):

* Early layers:"these symbols repeat."
* Middle layers:"each bigger run is separated by a single dot."
* Later layers:"the whole thing is symmetric, we're probably completing a mirror."

No layer holds an English sentence.

But the internal vector progressively encodes higher-level properties until "finish the palindrome" is the obvious continuation in that learned space.

Here's the difference between the model in our heads and what's actually running:

## Why it works on a puzzle it's never seen

This is the actual answer to "how did it solvemypuzzle."

It didn't memorize my exact dot sequence.

It learnedgeneral operationscount, compare, detect symmetry, continue a pattern and those operationscomposeto handle new inputs.

Give it dots, give it numbers, give it letters: the same "find the structure and extend it" machinery applies.

There's real research into this, some of it from interpretability teams like Anthropic's.

They've found specific internal circuits, one famous example is theinduction headthat do pattern continuation.

The mechanism is essentially: "earlier in this input, A was followed by B; here's A again, so B is likely next."

That's a literal, identifiable component inside the network doing pattern-matching-and-extension.

It's exactly the kind of thing that lets a modelcontinue a novel patterninstead ofrecalling a stored one.

When you frame it that way, the dot puzzle stops being mysterious.

It's a pattern.

The model has machinery for finding and extending patterns. It found it and extended it.

## The takeaway for devs

If you build with these models, the practical lesson is this: you're not working with a fancy autocomplete that regurgitates training data.

You're working with a system that learnedtransferable operationsunder next-token pressure, and applies them to inputs it's never seen.

That reframing changes how you prompt, how you debug weird outputs, and how you reason about where it'll be reliable versus where it'll confidently faceplant.

"It's just predicting the next word" is the kind of true-but-useless statement that'll lead you to the wrong intuitions.

A dumb little dot puzzle made me go look this up.

Disclaimer: This article was written by me; AI was used to fix grammar and improve readability.

AI agents write code fast. They also silently remove logic, change behavior, and introduce bugs — without telling you. You often find out in production.

git-lrc fixes this. It hooks into git commit and reviews every diff before it lands. 60-second setup. Completely free.

Any feedback or contributors are welcome! It's online, source-available, and ready for anyone to use.

⭐ Star it on GitHub:

## HexmosTech/git-lrc

### Free, Micro AI Code Reviews That Run on Git Commit

|🇩🇰 Dansk|🇪🇸 Español|🇮🇷 Farsi|🇫🇮 Suomi|🇯🇵 日本語|🇳🇴 Norsk|🇵🇹 Português|🇷🇺 Русский|🇦🇱 Shqip|🇨🇳 中文|🇮🇳 हिन्दी|

# git-lrc

## Free, Micro AI Code Reviews That Run on Commit

 

 
 
 
 
 
 

GenAI today is arace car without brakes. It accelerates fast -- you describe something, and large blocks of code appear instantly. But AI agentssilently break things: they remove logic, relax constraints, introduce expensive cloud calls, leak credentials, and change behavior -- without telling you. You often find out in production.

git-lrcis your braking system.It hooks intogit commitand runs an AI review on every diffbeforeit lands. 60-second setup. Completely free.

In short, git-lrc helpsPrevent Outages, Breaches, and Technical Debt Before They Happen

At a glance:10 risk categories·100+ failure patterns tracked· every commit…

View on GitHub

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse