---
title: Understanding Over Origin - DEV Community
url: https://dev.to/adamthedeveloper/understanding-over-origin-4685
site_name: devto
content_file: devto-understanding-over-origin-dev-community
fetched_at: '2026-07-28T19:33:30.266121'
original_url: https://dev.to/adamthedeveloper/understanding-over-origin-4685
author: Adam - The Developer ✨
date: '2026-07-28'
description: Many of developers communities are asking the wrong question. Not because they're wrong to worry... Tagged with ai, programming, productivity, opensource.
tags: '#ai, #programming, #productivity, #opensource'
---

Gatekeeping hurts AI-assisted creators

Many of developers communities are asking the wrong question.

Not because they're wrong to worry about low-effort work, no, but the filter they're using doesn't actually separate maintained engineering from generated slop. It just separates projects based on which tools were involved in their creation.

Imagine trying to share a work that you're really proud of, with the help of AI assisting it, the idea's yours but your work gets flagged, rejected, or buried under comments like"no you didn't"and"I hate how there's so many AI projects these days."Someone definitely felt righteous after saying this, believing they're protecting themselves from low-effort slop.

Except that's not actually what they're protecting against. They're protecting againsta label.

## The Distinction

I read@madsendev's article regardingOpen Vectorizerand Madsen wants to share the project with other people and in hope that someone would like to contribute as well.

Apparently, difference between "AI-generated" and "maintained engineering" has become invisible to gatekeepers who've simplified the filter down to a single binary question.

the wrong question.

" AI or no AI "? ( they didn't literally ask this but that's the filter in practice )

Here's why: imagine two projects.

Project A:Someone spends two years redesigning a vectorization algorithm, investigates whether machine learning could improve it, decides against it, implements a deterministic approach, discovers their own benchmark was inflated (and fixes it anyway), publishes reproducible results, and actively maintains the code.

Project B:Someone types "make me a music streaming app" into an AI prompt, publishes whatever emerges without testing it, and disappears.

Both used AI. Both are labeled "AI-generated." One belongs in a developer community. The other is exactly what communities should be filtering out.

Guess which one gets rejected? yah, both get rejected. The luckiest you can get is being rejected later because the gatekeeper was busy arguing with you and changing their community name to: " i miss what was it like to program on punch cards and a ciggy in my mouth " ahhh yes, the identity crisis.

## The Problem With Using "AI-Generated" as a Quality Filter

The gatekeeping argument seems reasonable at first glance. But it has real problems:

The dismissal:"no you didn't(via@deammer). This response requires ignoring the actual technical work, but Madsen rewrote an entire algorithm pipeline, tested it against established tools, and caught a bug that made his own benchmarks look better, then published the worse numbers anyway. That's not someone slapping a prompt onto Claude and calling it a day.

The broader concern:@blakebeckcodingpoints out something real, unvetted AI-generated code has introduced security vulnerabilities. That's a legitimate worry about maintainability and accountability. Where the argument breaks down is treating that as sufficient reason to rejecteveryAI-assisted project before evaluating its technical merits. The concern about low-quality code is valid. The heuristic of "reject based on tool choice" doesn't actually address it.

Think of it differently:we don't reject all Rust packages because Rust makes memory safety easier, nor do we assume all C projects are insecure because C makes memory errors possible. Language choice affects probabilities, but it doesn't determine quality. The same applies to AI.

The nostalgia play:"Dev.to used to be good"(same dude, you know who, bro's just nostalgic). There's an assumption that developer communities were higher-quality before AI tooling arrived. But humans have been publishing terrible code since the 1980s, spamming them has always been a problem and it isn't new, AI just makes it easier and cheaper to spam.

## The Real Problem (And Why It Requires Actual Work)

Developer communitiesarebeing flooded and it's not the AI-generated projects specifically butlow-effort projects, period. and like I said up there, the flood's rising fast at an overwhelming rate because AI made it cheaper to produce them.

The solution, though? It's not "ban the AI ones."

It's understanding what actually separates signal from noise:

* Can the maintainer explain the architecture, or does it sound like they're reading stack overflow?
* Are there meaningful tests?
* Can claims be independently reproduced?
* Are benchmarks transparent?
* Are weaknesses disclosed?
* Does the maintainer actually review changes and take responsibility?
* Will this be maintained in six months, or is it a one-off lab experiment?

These questions work equally well for human-written code. And they'reexpensive to verify, they require actual reading, thinking, and judgment.

"Was AI used?" is cheap. One checkbox. Feels principled. Lets moderators move on.

"Is this maintained engineering?" requires actually engaging with the work.

## The Pointed Out Irony

In the comment thread,@unitbuildsdelivered the most sensible take on all of this:

"Software development is an orchestration process where the ultimate value is the working, audited, and tested software—not just human typing time."

And then:

"If that's the kind of comments you leave, go to X and join the cesspool, or Reddit, they'll love you there. Please keep Dev.to a safe space for all developers."

hits good, doesn't it? it's not defending AI in the abstract. It's defendingcommunities staying communities, places where people can share work and get feedback, not face purity tests based on which tools they used.

The person who said they used 99% AI to ship a 3000-line game while working full-time deserves to share that. So does someone who used GitHub Copilot for routine completions. So does the Open Vectorizer author who made architectural decisions with AI assistance but wouldn't ship something they couldn't explain.

What none of them deserve is dismissal based on a label that tells you nothing about the quality of the work.

## The Historical Perspective

This is something that might seem beside the point but isn't: software development hasalwaysworked this way.

We moved from assembly to C and nobody said"You didn't really code because you're using a compiler."We moved from manual memory management to garbage collection. From raw SQL to ORMs. From writing Dockerfiles by hand to templates. From Stack Overflow copy-paste to IDE refactoring to GitHub Copilot autocomplete.

Each step increased abstraction. Each step generated concern that developers were getting lazy, that standards were dropping, that the craft was being diluted.

Each time, the question that actually mattered wasn't"What abstraction level did you use?"It was"Do you understand what was generated? Can you defend it? Will you maintain it?"

That's been the real standard all along.

AI is just the next step on that continuum. It's more aggressive, more visible, and it generates more mediocre output faster. But it's not fundamentally different from any other tool that lets developers offload rote work to focus on decisions that matter.

The question isn't whether AI should be accepted.

In short, people have been saying software development is dead since the first high level programming language was invented... just, circling around the same anxiety cycle over and over.

## The Good Moderation Requirements

no, it's not "open the floodgates." it's about what you're really filtering

Good moderation would:

* Require disclosure of substantial AI involvement (transparency matters)
* Judge projects on reproducibility, test coverage, and maintainer accountability
* Fast-track projects with public benchmarks or active bug resolution
* Catch obvious slopby its lack of depth, not its origin story
* Create space for people who are learning while filtering out low-effort republishing

Bad moderation does what's happening now:

* Blanket bans that assume all AI-assisted work is equivalent to prompt-and-publish
* Dismissive comments that never engage with technical substance
* Rejection based on the presence of a tool, not the absence of rigor

DEV's shift toward requiring disclosure rather than banning AI-assisted content is great. It puts the burden on the creator to be honest, then lets the community decide based on the actual work.

## What Actually Matters

@unitbuildshad it right: a developer community's job is to share work and get substantive feedback, not police the method.

The questions that separate good engineering from slop are straightforward:

* Can you explain the architectural decisions?
* What broke, and how did you fix it?
* Are benchmarks reproducible?
* Will you maintain this?
* Are you willing to be corrected?

They work regardless of whether code was typed by a human, generated by Claude, or mixed. Because they're about understanding and accountability - what has always determined quality.

Engineering should be evaluated on understanding, correctness, maintainability, testing, and accountability. Not keystrokes.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (15 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse