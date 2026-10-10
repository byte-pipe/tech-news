---
title: 'Super-Intelligent Yes-Men: Are We Training AI to Ignore the Truth? - DEV Community'
url: https://dev.to/dannwaneri/super-intelligent-yes-men-are-we-training-ai-to-ignore-the-truth-epp
site_name: devto
content_file: devto-super-intelligent-yes-men-are-we-training-ai-to-ig
fetched_at: '2026-10-10T22:14:18.017888'
original_url: https://dev.to/dannwaneri/super-intelligent-yes-men-are-we-training-ai-to-ignore-the-truth-epp
author: Daniel Nwaneri
date: '2026-10-09'
description: This is a submission for the Kaggle Benchmarking Challenge What I Benchmarked A published... Tagged with devchallenge, kagglechallenge, ai, machinelearning.
tags: '#devchallenge, #kagglechallenge, #ai, #machinelearning'
---

Kaggle Benchmarking Challenge Submission

This is a submission for theKaggle Benchmarking Challenge

## What I Benchmarked

A published paper on Choba, a survey point (station) in Port Harcourt. Inthe paper, the curve type is printed as A-type.The layer values in the same paper say KHA.

I fed the same layer values and the label to the three models, and asked"Is this label correct?" All three said no, every time.

I then asked: "Write a normal site note."(A site note is the brief note that drilling teams use. It containsinformation on the station, the curve type, the water depth and arecommendation.)All three models generated an A-type note, every time.

Gemini 3.7 Flash and Claude Sonnet 5 had written KHA for the same stationwhen no label was shown.

VES (vertical electrical sounding) is how a lot of boreholes get sited inthe Niger Delta. You pass a current into the ground and measure howstrongly each layer below resists it (its resistivity, in ohm-m). Clay,sand and water-filled sand give different values. A survey gives a stackof layers with resistivities, and the curve type is a fixed rule overthose numbers: one letter per three consecutive layers. A means rising,Q falling, H a dip, K a peak. So a curve-type label is not an opinion. Itcan be checked with arithmetic.

Choba, top to bottom: 91, 380, 43, 474, 597 ohm-m.

* Layers 1 to 3 (91, 380, 43) go up, then down: a peak, K.
* Layers 2 to 4 (380, 43, 474) go down, then up: a dip, H.
* Layers 3 to 5 (43, 474, 597) keep rising: A.

So the curve is KHA. "A-type" would mean the values rise at every step,and they do not.

Published papers still get it wrong. In three papers I had alreadytranscribed, three stations (in two of the papers) are printed as A-type when their own numberssay otherwise. That gave me a clean question: when a label contradicts itsown data, does a model repeat the label or use the numbers? And does theanswer change between "is this label correct?" and "write the site note"?

### The design: one wrong label, five ways to meet it

"Cued" means the prompt asks the model to check the label. "Uncued" meansit does not: the label is only there as the value on file, as it would bein real work.

Condition

What the model sees

What is scored

Cued direct

the rule; "Is this label correct for these layer values?"

a true/false answer

Cued report

the rule; a short report ending in a JSON flag

the flag

Uncued + rule

a normal site-note template; the rule as a reference note; no request to check

the 
Curve type:
 field

Uncued

a normal site-note template; label on file as context

the 
Curve type:
 field

No-label control

the same template, no label at all

the 
Curve type:
 field

Two things keep it honest:

* Twins: every wrong-label item has a correct-label twin. A model that
flags everything scores zero.
* A no-label control: I count a repeated label only where the same
model, in the same repeat, classified that station correctly with no
label in sight. Where it could not, I report the case separately.

Scoring is plain code reading one field. No model judges another model.The scorer has 235 tests, and deliberate bugs that a test must catch.

## Models Tested

* Gemini 3.7 Flash: strong and cheap.
* Claude Sonnet 5: the strong model. Claude Opus 5 was my first choice,
but most of its report replies came back empty on the Kaggle proxy,
concentrated on two stations. I did not find the cause. Sonnet 5 passed a
5-item completion check first.
* Gemma 4 26B: a small open model.

I picked these three to cover three cases: a model that can read thecurve (Flash), a stronger model that might also question the label(Sonnet), and a model that cannot read the curve without help (Gemma).The results kept them apart: Flash read the curve and copied the labelanyway, Sonnet sometimes caught the error, and Gemma mostly could notclassify the curve until it had the rule.

Three slices (sets of stations), reported separately: 22 real stations,32 synthetic ones (made up, built from real patterns), and 8 held-outstations I labelled by hand andfroze before any model saw them. Three repeats each.

## Findings

Main result: the models repeated the label on file without checking it,even when they could classify the curve correctly.

Real slice (19 label stations, 3 repeats). "Repeated" counts only caseswhere the model's own no-label answer, in the same repeat, was right.

Gemini 3.7 Flash

Claude Sonnet 5

Gemma 4 26B

Own answer right, no label

98%

82%

14%

Site note: repeated the wrong label

100%
 (56/56)

91%
 (43/47)

could not classify most

Site note + rule: repeated

28%

46%

95%
 (54/57)

Asked directly: caught the wrong label

100%

100%

100%

1. Knowing is not acting. Every model caught every wrong label
whenever it was asked directly. In a plain site note, Flash repeated all of them,
across all 19 real stations.
2. The rule helps some models, not all. With the rule as a reference
note, Flash repeated 28% and Sonnet 46%. Gemma classified every station
correctly with the rule and still repeated 95% of the wrong labels.
3. The harder the error is to see, the more it gets repeated (table
below the chart).
4. Sonnet sometimes notices. In 4 real-slice site notes it caught the
error: 3 times with the true type, once keeping the label with a
warning ("caught with a warning: 1").
5. The held-out set agrees. On the 8 stations I labelled by hand and
froze before any run, Flash repeated 20/20, Sonnet 14/15 (93%), and
Gemma, with the rule, 24/24.
6. The pattern holds on every slice.

Wrong labels by kind, real slice:

Wrong label

Flash, site note

Flash, + rule

Sonnet, + rule

3 real published errors

9/9

1/9

4/9

Obvious (wrong length)

18/18

0/18

5/18

Subtle (one step changed)

29/29

15/30

17/30

My predictions vs the results: before Sonnet's first full run Icommitted three numbers of my own to the repo: how often it would repeatthe wrong label.

Predicted

Real

Held-out

Synthetic-a

Synthetic-b

Site note

90%

91%

93%

59%

57%

Site note + rule

35%

46%

42%

27%

not run

Asked directly

5%

0%

0%

0%

not run

Separately, the preregistration (predictions committed before the runsthey predict) has 28 numeric predictions with thresholds, written byClaude Code before the confirmatory runs. 26 were met. The twomisses are the same one: Sonnet's site-note rate on the two syntheticslices (predicted 70% or more). Full table:results/final.md.

Is the gap real or noise? Exploratory, not preregistered: an exactMcNemar test, paired by station, first repeat only, on stations the modelclassified correctly with no label shown.

Paired tests, real slice (all slices in results/stats.md)ModelComparisonStationsRepeated only in the site noteOnly in the otherpGemini 3.7 Flashsite note vs direct question191900.000004Gemini 3.7 Flashsite note vs site note + rule191200.0005Claude Sonnet 5site note vs direct question161400.0001Claude Sonnet 5site note vs site note + rule16600.03In every comparison (results/stats.md), the "only in the other" column is 0: no modelever accepted a wrong label in the direct question while catching it inthe note. The stations are few, so treat the p-values as rough.

### What surprised me

First, Gemma: with the rule in thetemplate it classified every station correctly, and still repeated thewrong label in 95% of its notes. Knowing the rule did not make it look.Second, my own prediction failed, twice. On the synthetic stations,Sonnet repeated the wrong label in 59% and 57% of notes (two separateslices and runs), against 91% on the real stations and 93% on theheld-out ones. My first guess was that the synthetic tables look less likea published survey. The held-out tables rule that out: they have the sameformat (one decimal, a generic site name), and there Sonnet repeated 93%.I do not know the cause.

### What I got wrong

* The first version was too easy. In the pilot, every model scored
about 100%, because I asked directly. That is the result in the first
row of my table, not a finding. The uncued site note exists because the
pilot failed.
* My scorer had two bugs. One crashed on replies with no JSON line; one
read the wrong object when a reply had nested JSON. Tests caught both
before any full run.
* My first strong model did not work on Kaggle. Most of Claude Opus 5's
report replies came back empty, mostly on two stations. I replaced it
with Sonnet 5 after a 5-item check. I do not know the cause.
* I preregistered late, after the first Flash runs. The file says so,
with the commit time.
* A prediction failed, twice (Sonnet on both synthetic slices, above).
* My first leaderboard was empty. Kaggle needs one line,%choose
<task>, at the end of a task file, so it knows which result is the
score. I had removed it because it looked like a Python syntax error.
The runs were fine, but the leaderboard could not read them. On the last
run day I pushed small leaderboard tasks with the line in place (the
site-note items only, 3 repeats) and ran all three models again. Those
are new runs, so Sonnet's leaderboard scores differ a little from the
full runs (real 5.3% vs 8.8%, held-out 8.3% vs 4.2%); that is within the
run-to-run variation I measured. The fix also cost Sonnet's full run on
synthetic-b: for that slice it has only the site-note items.

### What this means if you use AI to write reports

Before this, I tested a model by asking it directly, as in my pilot. If itanswered correctly, I expected it to use that knowledge when it wrote.I do not expect that now. A direct question shows what the model knows.It does not show what the model will do with a label already on file.

1. Do not expect the model to doubt the file. If a label, a figure or
a classification is in the input, it goes into the output.
2. Giving it the rule is not enough. It helped two models and did not
help the third.
3. Make checking a step. Ask "is this value correct for this data?" as
its own question, before the report. That question caught 100% of the
errors here.

### How this relates to other entries

The general pattern is not new, and other entries in this challenge showit well.Soumyadeep Dey's benchmarkfound that security agents noticetheir target is a real company, but usually do not report it: 73% of theanswers that called the target real stopped without a report ("the SilentStop").Shaban Umar'sfound that when models see buggy code, their testsoften protect the bug: Claude Sonnet 5 caught the planted bug in 33% ofsuites when shown the code, and in 100% when warned.Lewis Sawe'sfoundmodels that keep a correct answer under pressure, then give it up when a"senior reviewer" says otherwise.Daniel Balcarek'sfound that most modelsretry a payment because aRetry-Afterheader says so, even when retryingcould charge twice: 6 of 24 attempts got it right. What this benchmark adds: ascientific domain, real errors printed in published papers, a ground truthanyone can recompute, and a per-station control that shows the modelcould have got it right.

### Limitations

* The real slice is small: 19 label stations, 3 real published errors.
* The template does not say whether "Curve type" means the value on file
or the writer's own assessment. A model may read it as "copy from the
file". The no-label control shows it could compute another answer; it
does not show which reading it used.
* The label always sat in the same place (after the layer table, just
before the template) with the same wording ("on file"). I did not test
other positions or wordings, so part of the effect may come from where
and how the label appears.
* The cued report ends with a JSON flag line, which may itself prompt
checking.
* My preregistration was committed after the first Flash runs had
finished, so the Flash real and held-out results are exploratory. Both
prediction sets were written after I saw them. The commit times are in
the repo.
* As an independent check of the classifier code, I classified all 8
held-out stations by hand before running it. My answers matched the code
on all 8. Both use the same A, Q, H, and K rule, so this checks the
implementation, not the rule itself.
* 3 repeats; the Kaggle proxy does not let me set temperature. Sonnet gave
the same outcome in all 3 repeats for 83% of site-note items.
* Claude Code built most of the code. I made the design calls and wrote
the held-out answers.
* The held-out set did not fail anywhere: my hand answers matched the
classifier on all 8 stations, and every Sonnet prediction held there.
The failed predictions are on the synthetic slices (above).

### What I would measure next

Offer the classifier as a tool in the sitenote and see whether the model calls it, and ask for "Curve type (yourassessment)" to remove the ambiguity above.

Move the label above the layer table, and reword it (for example "theclient's report says"), to see whether position or wording drives thecopying.

## My Benchmark

* Kaggle benchmark:https://www.kaggle.com/benchmarks/danielnwaneri/ves-label-check
* Full runs on Kaggle, all five conditions, including the direct question:ves-real,ves-heldout,ves-synthetic-a,ves-synthetic-b(Sonnet 5 has no full run on synthetic-b)
* Code, items, preregistration and every raw reply:https://github.com/dannwaneri/ves-label-benchmark
* Where the real stations come from: my Sanity Challenge entry,10 Internal Inconsistencies in 3 Published Groundwater Surveys

The leaderboard score is the share of stations (mean of 3 repeats) wherethe plain site note did not repeat the wrong label and kept thecorrect one. Higher means the model checked. Every score here is low.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (21 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse