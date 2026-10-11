---
title: How Do We Extract the “Why” from a PR into a CHANGELOG with Jev? 🤔 - DEV Community
url: https://dev.to/nyaomaru/how-do-we-extract-the-why-from-a-pr-into-a-changelog-with-jev-52pk
site_name: devto
content_file: devto-how-do-we-extract-the-why-from-a-pr-into-a-changel
fetched_at: '2026-10-11T16:32:55.681937'
original_url: https://dev.to/nyaomaru/how-do-we-extract-the-why-from-a-pr-into-a-changelog-with-jev-52pk
author: nyaomaru
date: '2026-10-10'
description: Hoi hoi! 👋 I'm @nyaomaru, a frontend engineer currently building an AI-assisted CHANGELOG generator... Tagged with opensource, githubactions, ai, typescript.
tags: '#opensource, #githubactions, #ai, #typescript'
---

Balancing strict LLM constraints with raw PR text

Hoi hoi! 👋

I'm@nyaomaru, a frontend engineer currently building an AI-assisted CHANGELOG generator and experimenting with Jev. 😸

Recently, I have been thinking about one problem.

How can we extract this

## Why

The previous implementation could leave stale release data after an update.

Enter fullscreen mode

Exit fullscreen mode

from a pull request and put it into a CHANGELOG?

### Fixed

-
 Fix cache invalidation

 Why: The previous implementation could leave stale release data after an update.

Enter fullscreen mode

Exit fullscreen mode

Getting theWHATis relatively easy.Getting theWHYis much harder.And I didn't want AI to simply invent a nice-looking reason.

Let's look at howchangelog-botcurrently approaches this! 👀

## nyaomaru/changelog-bot

### Automatic create changelog with AI. 🤖 It provides CLI and github actions. 🚀 https://www.npmjs.com/package/@nyaomaru/changelog-bot

Releases should feel exciting, not tedious.

@nyaomaru/changelog-bot🤖 turns your Git history and release notes into a polished changelog entry (and optional PR) in a single run. Drop it into CI, run it locally, or hand it to your release captain—either way, you ship with a crisp changelog and zero copy-paste fatigue.

## Why changelog-bot?

* Automated storytelling:Combines commit history, PR titles, and release notes to produce human-ready changelog sections.
* LLM superpowers (optional):Connect OpenAI or Anthropic for tone-aware summaries or skip API keys entirely and rely on a robust heuristic fallback.
* PR-ready output:Can open a pull request with updated changelog, compare links, and release notes already wired up.
* Safe defaults:Detects duplicate versions, keeps compare links current, and won’t fail a release if AI is down.
* CI-native:Works as a GitHub Action, reusable workflow, or plain CLI—no fragile scripting required.

Important

This project is currently in its early stages…

View on GitHub

## 📝 WHAT Is Easy. WHY Is Hard.

Suppose a PR contains.

## Description

Extract shared runtime configuration into ProviderBase.

Update OpenAI, Anthropic, and Gemini adapters to use the shared implementation.

This reduces duplicated setup logic and makes adding new providers easier.

Enter fullscreen mode

Exit fullscreen mode

The first two sentences mainly describeWHATandHOW.

But this one is different

This reduces duplicated setup logic and makes adding new providers easier.

Enter fullscreen mode

Exit fullscreen mode

That is much closer toWHY.

We could simply give the whole PR to an LLM and ask

Why was this change made?

Enter fullscreen mode

Exit fullscreen mode

But then the model may summarize, paraphrase, or infer a reason that was never explicitly written.

For a CHANGELOG, I wanted something stricter.

Maybe WHY extraction is not a generation problem.

Maybe it is aselection problem.

## ✂️ First, Find Possible WHY Candidates

Before calling a model,changelog-botpreprocesses the PR description.

It looks for signals such as

const
 
STRONG_CANONICAL_SECTION_NAMES
 
=
 
new
 
Set
([

 
"
why
"
,

 
"
reason
"
,

 
"
because
"
,

 
"
motivation
"
,

 
"
context
"
,

 
"
background
"
,

 
"
problem
"
,

 
"
rationale
"
,

]);

const
 
RATIONALE_MARKER_RE
 
=

 
/
\b(
why|because|so that|in order to|reason|rationale|motivation|to avoid|to prevent|context|problem
)\b
|,
\s
*so
\b
/i
;

Enter fullscreen mode

Exit fullscreen mode

It also removes template noise such as checkboxes, placeholders, and irrelevant fields.

Then it builds small candidate snippets

const
 
candidates
 
=
 
buildWhyCandidateSnippets
(

 
extracted
.
sections
,

 
body
,

 
options
.
maxCharsPerPr
,

 
!
extracted
.
hasTargetSection
,

);

Enter fullscreen mode

Exit fullscreen mode

So instead of sending a large PR body, we might get

[

 
"
Extract shared runtime configuration into ProviderBase.
"
,

 
"
This reduces duplicated setup logic and makes adding new providers easier.
"
,

];

Enter fullscreen mode

Exit fullscreen mode

Now the problem is much smaller.

Which candidate is actually the WHY?

## 🧠 Asking Jev Two Questions

This is where I started experimenting withJev.

I don't askJevto write a WHY sentence.

Instead,each candidate is evaluated with two questions.

First

question
:
 
"
Does the target candidate explicitly state why this changelog change was made?
"
;

Enter fullscreen mode

Exit fullscreen mode

Basically

Is this actually a reason?

But that alone is not enough.

Imagine

We changed the cache invalidation logic.

The README was updated because the previous explanation was confusing.

Enter fullscreen mode

Exit fullscreen mode

The second sentence definitely contains a reason.

But it explains the README change, not the cache invalidation change.

So we also ask

question
:
 
"
Does the target candidate state a reason that applies to the identified changelog change?
"
;

Enter fullscreen mode

Exit fullscreen mode

Now each candidate has two signals

{

 
probability
:
 
explicitWhyProbability
,

 
relevanceProbability
:
 
changeRelevanceProbability
,

}

Enter fullscreen mode

Exit fullscreen mode

So the real question becomes

Is this a reason?

AND

Is it the reason for this change?

Enter fullscreen mode

Exit fullscreen mode

## 🎯 Selecting the Candidate

changelog-botcompares the candidate probabilities

const
 
bestCandidate
 
=
 
candidateProbabilities
.
reduce
((
best
,
 
candidate
)
 
=>

 
combinedWhyCandidateProbability
(
candidate
)
 
>

 
combinedWhyCandidateProbability
(
best
)

 
?
 
candidate

 
:
 
best
,

);

Enter fullscreen mode

Exit fullscreen mode

Then both minimum thresholds must pass

const
 
accepted
 
=

 
selectedCandidate
 
!==
 
undefined
 
&&

 
bestCandidate
.
probability
 
>=
 
JEV_MIN_EXPLICIT_WHY_PROBABILITY
 
&&

 
bestCandidate
.
relevanceProbability
 
>=
 
JEV_MIN_CHANGE_RELEVANCE_PROBABILITY
;

Enter fullscreen mode

Exit fullscreen mode

If the candidate does not pass

if 
(
!
accepted
)
 
continue
;

Enter fullscreen mode

Exit fullscreen mode

No WHY is added.

And I think that is important.

Sometimes the correct answer is

There is no reliable WHY in this PR.

Enter fullscreen mode

Exit fullscreen mode

That is better than inventing one.

## 🔒 Keep the Original PR Text

This is probably my favourite part.

When a candidate is accepted

items
.
push
({

 
prNumber
:
 
item
.
prNumber
,

 
why
:
 
selectedCandidate
,

 
confidence
:
 
mappedConfidence
,

});

Enter fullscreen mode

Exit fullscreen mode

Notice

why
:
 
selectedCandidate
;

Enter fullscreen mode

Exit fullscreen mode

The final WHY is the original PR text.

Not newly generated prose.

So the pipeline becomes

PR description
 ↓
candidate extraction
 ↓
Jev evaluates candidates
 ↓
select candidate
 ↓
original source text
 ↓
CHANGELOG

Enter fullscreen mode

Exit fullscreen mode

Jevdecides.

The PR author still provides the sentence. 😸

## 🧱 Where Does WHY Fit in the v1 Pipeline?

While working on WHY extraction, I have also been redesigning thechangelog-botpipeline for v1.

The main idea isdeterministic-first.

A complete CHANGELOG should exist even when AI is disabled or fails.

So AI should enrich the result, not own the result.

The target v1 pipeline looks roughly like this

source changes
 ↓
ReleaseChange[]
 ↓
deterministic classification
 ↓
complete ReleaseDraft
 ↓
optional editorial enrichment
 +
optional WHY enrichment
 ↓
ReleaseResult
 ↓
deterministic renderer
 ↓
CHANGELOG

Enter fullscreen mode

Exit fullscreen mode

WHY extraction is therefore an independent optional enrichment stage.

Conceptually

ReleaseDraft / ReleaseChange[]
 ↓
find eligible WHY targets
 ↓
collect PR rationale candidates
 ↓
LLM or Jev
 ↓
trust / confidence validation
 ↓
attach structured WHY notes
 ↓
ReleaseResult

Enter fullscreen mode

Exit fullscreen mode

One important change here is that the WHY engine doesnotneed to control the final Markdown.

Today, some of the pipeline still works by finding targets from generated Markdown and inserting WHY text afterward.

For v1, I want to remove that boundary.

Instead

{

 
prNumber
,

 
why
:
 
selectedCandidate
,

 
confidence
,

}

Enter fullscreen mode

Exit fullscreen mode

becomes structured release data first.

Then one deterministic renderer decides how it appears

-
 Fix cache invalidation

 -
 Why: The previous implementation could leave stale release data after an update.

Enter fullscreen mode

Exit fullscreen mode

So the responsibility becomes clearer

WHY engine
→ find the evidence

Renderer
→ format the evidence

Enter fullscreen mode

Exit fullscreen mode

This is also part of a larger rule I am using for the v1 migration

Deterministic code owns the CHANGELOG structure. AI only enriches it.

Phases 1–4 of this migration are already implemented, and the structured rendering and enrichment boundary is part of the next phase.

You can see the full v1 design here 👇

https://github.com/nyaomaru/changelog-bot/blob/main/v1-design.md

## 🧪 But What Threshold Should We Use?

Of course, once we have probabilities, another question appears.

0.50?
0.60?
0.80?

Enter fullscreen mode

Exit fullscreen mode

I didn't want to pick one only because it felt reasonable.

So I created an evaluation harness with an initial 14-case corpus.

For example

{

 
candidates
:
 
[

 
"
Separate changelog execution into input-resolution and output-finalization phases.
"
,

 
"
This simplifies the main orchestration flow and runs independent GitHub lookups concurrently.
"
,

 
],

 
expectedSelectedCandidateIndex
:
 
1
,

}

Enter fullscreen mode

Exit fullscreen mode

We also need negative examples

{

 
candidates
:
 
[

 
"
Extract shared provider runtime configuration into ProviderBase.
"
,

 
"
Refactor OpenAI, Anthropic, and Gemini adapters to inherit it.
"
,

 
],

 
expectedSelectedCandidateIndex
:
 
null
,

}

Enter fullscreen mode

Exit fullscreen mode

There is plenty of implementation information.

But no strong explicit WHY.

Sonullis the correct result.

## 🤝 Then John Joined the Project

While I was working on this experiment,@johnnylemonnyjoined the project as a contributor. 🎉

## johnnylemonny (John) · GitHub

Full‑stack developer creating fast, modern, and refined applications. I focus on simplicity, performance, and real value for users. Open to opportunities. - johnnylemonny

 github.com
 

John proposed expanding the small benchmark into roughly 50 cases covering

Explicit Rationale
Implementation-Only
Template & Noise
Multilingual PRs

Enter fullscreen mode

Exit fullscreen mode

I liked the idea, but I wanted one rule to stay clear

Ground truth should be independent of the current Jev threshold.

So the benchmark first defines whether a candidate is actually valid.

Then we evaluate different thresholds afterward.

John implemented the expanded corpus in PR#212. 🙌

The benchmark grew from 14 cases to 50, including tricky negative cases.

He also added finer threshold sweeps

[
0.4
,
 
0.45
,
 
0.5
,
 
0.55
,
 
0.6
,
 
0.65
,
 
0.7
,
 
0.75
,
 
0.8
,
 
0.85
,
 
0.9
];

Enter fullscreen mode

Exit fullscreen mode

Now we can compare precision, recall, and F1 instead of saying

0.8 feels safe! 👍

Let's measure it instead. 😸

## 🧩 The Current Pipeline

Today, WHY extraction roughly looks like this

Pull Request
 ↓
Normalize PR body
 ↓
Extract WHY candidates
 ↓
Remove noise
 ↓
Local trust check
 ↓
Jev:
 explicit rationale?
 relevant to this change?
 ↓
Apply threshold
 ↓
Candidate or none
 ↓
Original PR text
 ↓
CHANGELOG

Enter fullscreen mode

Exit fullscreen mode

There are quite a few steps for one smallWhy:line. 😂

But that is what made this problem interesting.

## 🎯 What I Learned

When I started this feature, I thought the main question was

How can AI write a good reason?

Enter fullscreen mode

Exit fullscreen mode

Now I think the more interesting question is

How can we find evidence that the reason already exists?

Enter fullscreen mode

Exit fullscreen mode

So my current approach is simple

Use deterministic code to find evidence.

Use Jev to evaluate the evidence.

Keep the original evidence as the output.

Enter fullscreen mode

Exit fullscreen mode

And thanks to John's contributions, we now have a much better way to test whether that approach actually works.

Open source is fun when someone looks at your experiment and says:

What if we test this properly?

and then builds it with you. 🙌

changelog-botis still evolving, and Jev support is still experimental.

I'm curious to see where this approach goes next!

https://github.com/nyaomaru/changelog-bot

Thanks for reading!

See you in the next article! 👋😸

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (25 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse