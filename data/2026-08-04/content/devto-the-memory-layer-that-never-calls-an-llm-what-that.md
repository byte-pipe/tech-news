---
title: 'The memory layer that never calls an LLM: what that buys, and what it costs - DEV Community'
url: https://dev.to/gde03/the-memory-layer-that-never-calls-an-llm-what-that-buys-and-what-it-costs-12ch
site_name: devto
content_file: devto-the-memory-layer-that-never-calls-an-llm-what-that
fetched_at: '2026-08-04T11:46:04.389362'
original_url: https://dev.to/gde03/the-memory-layer-that-never-calls-an-llm-what-that-buys-and-what-it-costs-12ch
author: Giulio D'Erme
date: '2026-07-30'
description: Part 4 of **The Answerability Problem, and the one that isn't about abstention. Parts 1–3 argued that... Tagged with ai, rag, opensource, discuss.
tags: '#discuss, #ai, #rag, #opensource'
---

Raw turns beat LLM cost via auditability

Part 4 of **The Answerability Problem, and the one that isn't about abstention.Parts 1–3argued that the field measures the wrong half and that my own system hits a wall on the right half. This part is the ledger: what RE-call is, what it loses at, and why you might still want the thing that loses. Code:RE-call(MIT).

Three parts of "here is what doesn't work" earn one part of "here is what this is for."

So, plainly:on BEAM's 1M-token bucket, Mem0 scores better than RE-call on categories I care about.I'm not going to bury that, and I'm not going to explain it away. I'm going to tell you exactly why it happens, what that accuracy costs, and let you decide which side of the trade you want, because for a lot of people the answer is not the obvious one.

## The mechanism, in one sentence

Mem0 calls an LLM when youwritea memory, and stores the distilled result. RE-call calls no LLM ever, and stores your raw turns.

That single decision explains everything downstream: the wins, the losses, the bill, and where your data goes.

The clearest place to see it istemporal_reasoning, my second-worst BEAM category:0.408 against Mem0's 0.567.

One disclosure before that number goes anywhere, because it changes what it means:that cell was measured with reranking off.The BEAM harness takes a--rerankerflag and defaults it tonone, and the run didn't pass it. Reranking is the largest retrieval gain in this project.Part 2measures it at hit@5 0.671 → 0.777 on LOCOMO, improvingeverycategory including the multi-hop floor I'd predicted it wouldn't touch. So 0.408 is myshipped default, not my best configuration, and the reranked cell isunmeasured.

I'm not going to tell you which way that would go. The last time I predicted a category wouldn't benefit from reranking I was wrong, and guessing here would be the same error with a bigger number attached.

What Icansay is that reranking is unlikely to be the whole story, because the diagnosis isn't a ranking failure. Of seven badly-lost questions only one had empty retrieval; five were answered confidently and wrongly. They are all the same shape, "how many days between A and B", and in the five it answered, my system used the wronginstanceof a date, while getting the arithmetic on those wrong dates right every single time. That is what makes this a selection problem and not a reasoning one:

gold

our answer

25 Mar → 1 Apr = 7 days

14 days
, using the 
updated
 deadline of 15 Apr

25 Mar → 10 Apr = 16 days

26 days
, using a 
different
 viewing on 15 Mar

15 Feb → 20 Feb = 5 days

0 days
, using 10 Jan, the date the deadline was 
set

Mem0 gets these right because its stored memory is one distilled line,"Sprint 1 deadline: February 15, 2024". Mine is the same date scattered across many raw turns in different roles: when it was set, when it was revised, when someone mentioned it in passing.

This is the one category where LLM distillation at ingest is genuinely the better architecture, and no retrieval-side change I can afford replicates it. It's recorded in the repo as a known limit, not an open task.

Correction, added after publication.That paragraph claimed more than I had measured, and a reader's comment exposed it. The cell was measured with my own temporal layer structurally unable to fire, which is not the same as having tried it, and "recency is falsified" rules out one family of fix, not all of them. The obvious successor is unsound too, for a reason I did not expect: a validity window records when a turn wassaid, not when the eventhappened.

So I enumerated the seven questions instead of describing them; they are a fixture in the repo now. Of the five my system answered, the mechanisms aretwowrong instances of a similar event,onegenuine revision,onefieldvalueconfused with the time it wasasserted, andoneevent time confused with mention time. Supersession therefore reachesone of five: four problems wearing one category name, none of them solved. Stated as narrowly as it was made, that is a hand reading of five answers from the run artifact alone, and five items is a list, not a rate.

So: they're better at this, for a real reason. Whether it is cheaply fixable is now an open question rather than a closed one.

## What that accuracy costs

Here's the other side of the same decision, measured on the identical benchmark workload:

RE-call

Mem0

LLM calls to build the memory

0

272

tokens

0

2.6 M

cost

$0

$7.29

ingest wall clock

67 s

288 s (
~4.3× slower
)

where your documents go

your Postgres

an LLM provider, once per memory written

That $7.29 is foronebenchmark's memory. It is not a subscription. It is a per-memory marginal cost that scales with everything you ever write. RE-call's write path calls no model, so its marginal cost is$0 at any scale, on any model, forever. There is no pricing change upstream that can alter that number.

The ingest gap is the same fact wearing a stopwatch: an extraction call per session is a network round-trip per session.

(Retrieve latency, 77 ms against 104 ms, I report as **directional only. The repeated-query bootstrap CI is optimistic and the two backends differ, so I won't lean on it.)

## The part that isn't a number

Your data never leaves your infrastructure. Local embeddings, the PostgreSQL you already run, and it worksoffline: on an air-gapped box, in a privacy-bound environment, under a DPA that doesn't have room for another subprocessor.

A memory layer that calls an LLM per write cannot offer that, structurally. Not because anyone is careless, but because the architecture requires sending the content out to distil it.

If you're a solo developer, that's a cost story. If you're a company holding customer conversations, it's a procurement story, and it's usually the one that decides the question before accuracy is ever discussed.

The cloud embedder is available as ameasured optionrather than a default, and the repo prices it honestly: it wins on 16 of 17 held-out corpora, median +0.059 hit@5, and it means every document and every query leaves your machine, at 246 ms p50 against 45 ms local. You get the numbers and you choose. That's the pattern for everything here.

## Everything is a switch, and both settings are measured

This is the part I undersold for five articles.

* Embedder: a hashing model that needs no download,bge-small,bge-large, Voyage, or anything OpenAI-compatible. Measured across 17 corpora, with the rule for when paying is worth it.
* Reranking: off by default, one flag on. It's the largest retrieval gain in the project (hit@5 0.671 → 0.777) and it costs ~1,050 ms/query, about 4× wall clock. Both halves are published, and the decision is yours: answering a human, ~1 s is invisible next to the LLM call that follows; serving high-volume automated retrieval, it dominates.
* Entailment abstention: off by default, andPart 2is 2,000 words on why it doesn't rescue the hard case.
* The whole stack: Postgres and pgvector. No separate vector database, no queue, no second store to keep consistent.

I'd rather ship a flag with two measured settings than a default with a marketing claim.

## And the risk that doesn't show up in an accuracy column

BEAM has anabstentioncategory, questions whose correct answer is "that isn't in here." I scoredMem0's own published answerson it, withMem0's own judge. n=70:

Mem0 did

n

mean score

abstained

38

0.974

answered anyway

32

0.016

The category is near-perfectly binary, and it is testing exactly one thing: does the system invent an answer when the evidence isn't there.It invents one 46% of the time.

One real example: asked about user feedback that was never recorded, it answered"User testing showed a positive response: the dynamic language switching feature achieved a 90% satisfaction rate."The corpus does contain"achieving a 90% satisfaction rate is a strong start", theassistantspeculating, which retrieval surfaced and the answerer read as fact.

I want to be precise about what I'm claiming, because this is where it would be easy to overreach:

* Their published score ishonest. I reproduced their BEAM cell to0.0005(0.6414 against 0.6409). Nothing is being faked.
* The benchmark isnotbackfitted to them. A benchmark tuned to flatter a vendor would not expose a 46% fabrication rate on that vendor.
* And my own number here is not a triumph. On the same category my shipped policy abstains correctly23.3%of the time at a9.3%false-abstain cost, measured on 30 unanswerable and 270 answerable questions across conversations 0–14, at$0, because that probe needs no LLM. Same configuration caveat as above: reranker off. I tested four stricter policies andevery one of them nets worseon BEAM's 9:1 answerable-to-unanswerable mix. The shipped policy is already the best of the five, which is the opposite of what I predicted.

So neither of us solves this. The difference is the shape of the failure: a system that fabricates a plausible satisfaction rate is a different kind of liability from one that returns nothing. Depending on what you're building, "slightly less accurate" and "confidently invents a statistic" are not two points on one scale.

## Two things wrong with the benchmark itself

Worth saying because they cut against my own story as much as anyone's.

BEAM's unanswerable questions scorehigherthan its answerable ones: median top-1 cosine0.676against0.641. They're adversarially constructed, and a lexical-coverage signal sharing no mathematics with cosine inverts in the same direction. Soevery BEAM figure, theirs and mine, is an upper bound on difficulty, not an estimate of deployed behaviour.On an ordinary corpus, where unanswerable means genuinely absent, plain cosine separates at AUC 0.780.

The scoring is 9:1 against withholding.Abstention is ~10% of BEAM, so a policy that abstains more gains on 30 questions and loses on 270. That is not a complaint about the benchmark. Its abstention category is well built. It meansan abstention claim cannot be made through BEAM's aggregate, no matter how good the policy gets. The field needs a metric that prices a false answer against a withheld one, and this isn't it.

Two smaller corrections that arm produced: BEAM's harness pinsgpt-5as answerer and judge (not gpt-4o), and the published64.1 is a mean rubric-nugget score, not a pass rate: the pass rate for the same run is 70.14%.

What I'm not reporting: a paired BEAM aggregate.I have per-category cells and the abstention probe; I do not have a like-for-like total, so there isn't one in the repo and there isn't one here. An earlier draft of this project did fuse two unrelated BEAM numbers into a headline that read well and did not exist. Once burned.

## So which one should you use?

Genuinely depends, and I'll say it against my own interest:

Use the LLM-distilling architectureif your questions are heavy on temporal and multi-hop reasoning over dense material, a strong reader is doing the answering, per-memory cost is not a constraint, and sending content to a model provider is fine for you. It is better at that, measurably, and I've shown you the category where it beats me and why.

Use this oneif the marginal cost of a memory has to be zero, your data can't leave, you need it to work offline, you want the retrieval path to be inspectable and switchable rather than a model's opinion, or if a system that confidently invents a satisfaction rate is a worse outcome for you than one that says nothing.

That's the trade. It isn't "we're better." It's that an LLM in the write path buys a better representation and charges you money, latency, and your data for it, and for a large number of real deployments that's the wrong purchase.

## Where the series ends up

Parts 1–3said the field measures accuracy on questions that have answers, that the standard harness for the most-quoted benchmarkforbidsabstaining, that when I built the missing metric my own system scored zero, and finally that the two public benchmarks disagree because each samples one point of a hidden axis, which turns a yes/no question into a coordinate.

This part says the rest of it: that the same design which losestemporal_reasoningis the one that costs $0, ingests 4.3× faster, and never sends a document anywhere, and that the incumbent's better aggregate comes with a 46% fabrication rate on the questions where the honest answer is silence.

Both of those are true at once. Publishing only the flattering half is the thing this whole series is against.

## For completeness: the paired contest

On LOCOMO, same questions, same generator, same judge, only the memory differs. Paired McNemar over per-question outcomes, n=1,540:

generator

judge

RE-call

Mem0

paired p

gpt-4o-mini

gpt-4o-mini

0.416

0.378

0.0059

gpt-4o-mini

gpt-4o

0.466

0.412

0.00018

gpt-4o

gpt-4o

0.484

0.444

0.0065

Holm–Bonferroni across all five cells run (largest adjusted p = 0.012), and it holds on the 1,369 questions where both judges agree (0.440 vs 0.399, p = 0.006).

Two things I'll say louder than the result.The lead is a property of the reader, not a universal fact. The margin shrinks as the generator strengthens andreverses on Claude Sonnet(0.565 vs 0.608, n=584, a generator run after pre-registration and labelled as such). Andnote the absolute numbers: 0.416–0.484, nothing like the 92.5 in the headlines, because a paired protocol with a strict judge and a matched retrieval budget measures something the leniency stack inPart 1does not.

## One more thing, and it's the reason any of this is checkable

Everything above is a number I produced about my own system. You have no way to recompute it without buying inference.

That bothered me enough to build the fix: a benchmark whereevery number is recomputable by a hostile party for $0, with no model in the loop: no judge, no paid generator, git as the database, and disputing a result is a pull request. It has RE-call on its board with an unflattering score, and a deliberately fabricated submission committed as a fixture because it passes five of the six mechanical checks.

That's its own post, coming next, and it's the one I'd most like you to act on.

Every figure:results/FINDINGS.md§9d–§9p,results/RESULTS.md§9–§11.RE-callis MIT,pip install recall-rag.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (20 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse