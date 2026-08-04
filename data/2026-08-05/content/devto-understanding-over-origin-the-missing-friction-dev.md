---
title: 'Understanding Over Origin: The Missing Friction - DEV Community'
url: https://dev.to/adamthedeveloper/understanding-over-origin-the-missing-friction-55ag
site_name: devto
content_file: devto-understanding-over-origin-the-missing-friction-dev
fetched_at: '2026-08-05T06:00:26.403503'
original_url: https://dev.to/adamthedeveloper/understanding-over-origin-the-missing-friction-55ag
author: Adam - The Developer ✨
date: '2026-08-04'
description: A few days ago, I wrote "Understanding Over Origin" and it got alot of engagement and I'm really... Tagged with ai, programming, productivity, learning.
tags: '#ai, #programming, #productivity, #learning'
---

Reflections sparked by a reader debate

A few days ago, I wrote"Understanding Over Origin"and it got alot of engagement and I'm really happy that it did because it means people took the time to read, understand my perspective and I get to engage with every one of them in the comments as well. Of course, not everyone agrees but that's irrevelant, the point is a healthy discussion between various perspective from different developers around the world.

But what I haven't told anyone is this: the more I engage, the more I realized something that I still do. I still write a lot of my code by hand and those are the parts I'm more proud of "

Not gatekeeping, not me being nostalgic or identity-defensive ( well, a little nostalgic ), that's me admitting the article I published wasincomplete.

Some conversations don't end when the replies stop. My discussion with@darkwiiplayerwas probably my favorite of all because more we talked, the more I found myself wrestling with an incomplete idea that refused to stay unfinished and this essay is the result.

## What the Discussion Clarified

First, I need to thank the people who actually engaged with the core argument.

@unitbuildsgave his take that seams everything together and concludes the core idea of modern software enigeering: "If it can run a standardized benchmarking suite against competition, it's provable and reproducible. If that's good enough for a scientific discovery, it's good enough for programming.", they're not defending AI, they're saying with better standards available, we shouldn't choose to ignore them. He also pointed out something I'd missed, the burden of correctness has always been on the developer who signs off on the PR.

@madsendevwho wrote the original article that sparked this whole discussion, showed genuine class. He came back, said the argument had "gone further," and proposed an idea that's stuck with me: what if AI-assisted projects included a standard where you quiz yourself on your own repository? Not to prove you didn't use AI, but to prove you actually understand what you built.

@komohit on something important and i think it's my favorite takeaway from the discussion:"Maintenance receipts are much harder to fake."That single sentence reframes the entire debate. Tests. Bug fixes. Production incidents. Responding to issues. Refactoring. Every one of those leaves a trail of evidence that someone not only built the project but continues to understand, improve, and take responsibility for it. That's the kind of ownership that matters. It's earned over time, and it's far harder to fake than explaining code in an interview or claiming you wrote every line by hand.

I'm absolutely grateful that people gave in their thoughts but you can never have a good discussion without a pushback ⚔️

the pushback's always my favorite part of any technical discussion.

## The Challenge That Made Me Think

@darkwiiplayershowed up and said something like: "Training AI on stolen code without consent is theft. Everything built with AI carries that theft in its DNA. You're overlooking this."

She wasn't being rhetorical, she was actually making a philosophical point about training data, consent, and what "learning" means when it's done at scale without permission.

We went back and forth. I argued that training data and generated output aren't automatically equivalent to copying and she countered that if you removed all stolen code from training data, the models wouldn't exist as they do. Which is... probably true? And that matters.

I don't think it invalidates theengineeringargument. But it does mean the conversation has two layers:

1. The technical layer: is the work maintained, understood, and good?
2. The ethical layer: how should we feel about tools built on potentially non-consensual training data?

Most people in that thread were debating layer 1 and she dragged me down to layer 2 into the conversation. Both are real. Neither invalidates the other.

But it also made me realize my original articledidn't addresswhy handwritten code felt different to me because honestly? it does.

## The Real Tension

The argument I made: origin doesn't determine quality. Understanding, testing, maintainability, accountability, that's what matters.

My own experience reflects that. I started writing code around 2018, and back then the only AI most of us could name was Sophia, the humanoid robot from Hong Kong. I learned the traditional way: by writing everything myself. Even today, when I write code by hand, I understand it differently. More deeply. I notice edge cases I might have overlooked if I'd generated the first draft with AI. And when I'm done, I'm genuinely more proud of what I've built.

These aren't compatible statements if you think about them too hard.

Either:

1. My pride is just ego (origin bias)
2. Handwritten code actuallyisbetter (proving the gatekeepers right)
3. Both are true, but for reasons I didn't examine

@fromzerotoshiphelped me see option 3 clearly. They're not a developer but they've shipped 20+ working internal tools using AI. A hospital runs them. By my standards, they'd "fail" the understanding test, there are parts of their system they couldn't explain line-by-line.

But then they said something that shifted everything:"Demonstrable behavior under deliberate failure is another form of earning trust, and it's the only one available to me. It's also harder to fake."

Plant defects, watch the guards catch them, restore the guards and watch them go green and then deploy and check the URLs a few seconds later.

they demonstrate that they can keep it alive.

And that made me realize the real distinction wasn't about who typed the code. It was aboutfriction.

## The Friction Actually Matters

In my earlierpieceI wrote a few weeks ago, I described not being able to write some logic from scratch despite reviewing it perfectly, that wasn't just skill loss. It was proof that I'd skipped the friction that builds actual understanding.

When I write code by hand,I encounter problems in real-time.

I hit a wall. My approach doesn't work. I refactor. I discover the problem space through constraint and failure. I make decisionsabout decisions, not just typing, but choosing between paths I've actually explored. this is the learning path that I unknowingly go through whenever I write code by hand and Wii reminded me of this.

When I use AI, I describe what I want. I get options. I pick the one that looks right.I'm curating, not exploring.

Both can produce good code. But thepath to understandingis fundamentally different.

With handwritten code: friction, insight, better next decisionsWith AI-assisted: selection, implementation, validation

The friction is the learning mechanism.

So when I say I'm more proud of handwritten code? I'm not being romantic about suffering. I'm noting thatthe code I'm proudest of is the code I fought for, and handwriting forces the fight.

## But Here's the Problem With That Logic

If friction is the mechanism, then thetypeof friction matters more thanwho did the typing.

You could write AI-assisted code where you:

* Fight with the prompt
* Critique every generated option
* Refactor aggressively
* Hit walls and redesign

That has friction and it also builds understanding.

Conversely, you could hand-write code where you:

* Autopilot through a familiar pattern
* Never question assumptions
* Copy-paste from Stack Overflow
* Never understandwhyit works

That has no friction and it builds nothing.

So the honest version of my position isn't "handwritten code is better." It's:"friction builds understanding, and handwritingtends to create frictionbecause you're forced to think through every line."

But that's a contingent truth, not an absolute one.

## The Uncomfortable Realization

The critics ( gatekeepers, but we'll stick with this from now on ) were partially right and I was too generous in my original position.

Not about the gatekeeping itself, no, that's still wrong. But about thetendency: AIdoesmake it easier to produce low-understanding code. Not because AI is bad, but becauseremoving friction is literally what AI does, and friction is what builds understanding.

The answer isn't "use less AI" or "never use AI." It's "if you use AI to skip engagement with the problem, whether that's the code, the failure modes, or the maintenance, you build worse systems.

That applies to humans too but humans have an inherent friction cost, we get bored, we hate typing, we make mistakes. That friction is annoying, but it forces us to stay engaged.

## So What Changed?

Nothing about the original argument waswrong. But I was treating "understanding + accountability" as if they were just checkboxes you could verify at the end.

They're not.

Understanding isn't a property you can inspect, it's aprocessand that process requires friction. Real engagement with the problem. Mistakes you learn from.

The reason I'm prouder of handwritten code is because Iearnedthe understanding in a way that's harder to fake.

Does that mean every line should be handwritten? No. Boilerplate is boilerplate. Some friction is just noise.

But the core logic? The architecture decisions? The places where "understanding this code" actually matters?Yeah, I want to have fought for that.

And I want the same from anyone shipping code that matters.

## The Uncomfortable Middle Ground

Here's where I land:

To the critics:You're using the wrong filter. "AI or no AI" doesn't tell you anything but you're accidentally right that there's something real to be concerned about, it's thelazinessthat AI enables, not the tool itself.

To AI enthusiasts:Yeah, your tooling is amazing. But it's worth asking whether you're using it to think better or think less. Those feel the same until you try to maintain the code six months later.

To myself:The pride I feel in handwritten code isn't ego, It's legitimate. every line that I typed out isn't some sort of magical unicorn mythological Godly line but it's the friction that comes with it, the learning I build that comes with it.

Sometimes the answer requires admitting you skipped and sometimes that's fine for routine work. But if you're building something that matters, you should want to have fought for it.

## Choose Where You Fight

I still write a lot of code by hand. I still use AI every day. Those aren't contradictions anymore.

The original article was right: origin doesn't determine quality. What it missed is that understanding isn't a checkbox you tick at the end. It's something you earn through friction. Handwriting tends to create that friction. AI tends to remove it. Neither is inherently good or bad. Both are choices about how you engage with the problem.

So I'm not asking "Did you use AI?" anymore.

I'm asking: Did you fight for the parts that matter?

And if the tool answered that for you, you'll find out the next time something breaks.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (15 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse