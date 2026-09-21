---
title: 'GitHub - jaredpalmer/kev: tiny Jev-like family of decision models built on top of Qwen3.5 you can train and run on your own · GitHub'
url: https://github.com/jaredpalmer/kev/tree/main
site_name: hnrss
content_file: hnrss-github-jaredpalmerkev-tiny-jev-like-family-of-deci
fetched_at: '2026-09-21T16:50:32.093237'
original_url: https://github.com/jaredpalmer/kev/tree/main
date: '2026-09-21'
description: tiny Jev-like family of decision models built on top of Qwen3.5 you can train and run on your own - jaredpalmer/kev
tags:
- hackernews
- hnrss
---

jaredpalmer

 

/

kev

Public

* NotificationsYou must be signed in to change notification settings
* Fork105
* Star2k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

181 Commits
181 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.devin/
skills/
kev-modal-study
.devin/
skills/
kev-modal-study
 
 
.github/
workflows
.github/
workflows
 
 
docs
docs
 
 
evals
evals
 
 
experiments
experiments
 
 
kev
kev
 
 
playground
playground
 
 
runs
runs
 
 
scripts
scripts
 
 
space
space
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
LICENSE
LICENSE
 
 
PLAN.md
PLAN.md
 
 
PLAN_27b.md
PLAN_27b.md
 
 
PLAN_Qwen35.md
PLAN_Qwen35.md
 
 
README.md
README.md
 
 
modal_app.py
modal_app.py
 
 
modal_probe35.py
modal_probe35.py
 
 
pyproject.toml
pyproject.toml
 
 
scratchpad.txt
scratchpad.txt
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# Kev

Small Jev-like decision models you can train and run yourself.

Kev is a family of small decision models built on Qwen3.5 and based on the architecture described inJev's Architecture Unmasked. You can use the pretrained weights or train your own. The API matches TypeSafe'sSystem One, so you can point their Python SDK at your local server.

## Highlights

* 0.8B, 4B, and 9B models, with training code and evaluation data.
* Yes/no (noul), multiple-choice (choice), and rating (score) questions in the same request.
* Questions share the input text but can't read each other.
* Runs on CUDA and Apple Silicon. The 4B and 9B models fit a 32 GB Mac using bf16; seeServing Performancefor what to expect on a Mac.
* A web playground for trying your own inputs and checking how option order affects the answers. Or try Kev-4B and Kev-0.8B in the browser athuggingface.co/spaces/jaredpalmer/kev, no install needed.

## Quick Start

You'll need Python 3.12+ anduv.

git clone https://github.com/jaredpalmer/kev.git 
&&
 
cd
 kev
uv sync --extra serve
KEV_DTYPE=bf16 uv run --extra serve python -m kev.serve --run jaredpalmer/kev-4b --port 8009

This starts Kev-4B locally. The first run downloads the adapter and base model.--runalso accepts a local checkpoint directory or a Hub revision, such asjaredpalmer/kev-4b@qwen3for the previous generation.

In another terminal, send it a ticket:

curl -s localhost:8009/v1/systemone -H 
'
content-type: application/json
'
 -d 
'
{

 "state": "Shoes arrived two weeks late and in the wrong size. Also I see two charges on my card.",

 "model": "kev-latest",

 "questions": {

 "department": {"type": "choice", "instructions": "Which team should handle this?",

 "criteria": {"returns": "Exchanges, refunds, wrong or damaged items",

 "shipping": "Delivery status, delays, lost packages",

 "billing": "Charges, invoices, payment problems"}},

 "escalate": {"type": "noul", "instructions": "Does this need urgent human attention?"},

 "frustration": {"type": "score", "instructions": "How frustrated is the customer?",

 "criteria": ["Calm", "Frustrated", "Very angry"]}

 }}
'

Example response from Kev-4B, running in bf16 on an Apple M5:

{
 
"model"
: 
"
kev-latest
"
,
 
"answers"
: {
 
"department"
: { 
"type"
: 
"
choice
"
, 
"choice"
: 
"
returns
"
, 
"confidence"
: 
0.21
,
 
"probabilities"
: { 
"returns"
: 
0.47
, 
"shipping"
: 
0.28
, 
"billing"
: 
0.25
 } },
 
"escalate"
: { 
"type"
: 
"
noul
"
, 
"noul"
: 
0.93
 },
 
"frustration"
: { 
"type"
: 
"
score
"
, 
"score"
: 
1.44
, 
"confidence"
: 
0.78
,
 
"legend"
: { 
"0"
: 
"
Calm
"
, 
"1"
: 
"
Frustrated
"
, 
"2"
: 
"
Very angry
"
 },
 
"probabilities"
: { 
"0"
: 
0.00
, 
"1"
: 
0.56
, 
"2"
: 
0.44
 } }
 },
 
"usage"
: { 
"input_tokens"
: 
101
, 
"output_tokens"
: 
161
 },
 
"latency_ms"
: 
495

}

The ticket mentions a return, a late delivery, and a billing problem, and the department probabilities say so. That is the point of getting probabilities back instead of a single label.

### Python

The TypeSafe SDK is included inuv sync --extra serve:

from
 
typesafe_sdk
 
import
 
Choice
, 
Noul
, 
Score
, 
TypeSafeClient

client
 
=
 
TypeSafeClient
(
 
api_key
=
"local"
,
 
base_url
=
"http://127.0.0.1:8009"
,
 
model
=
"kev-latest"
,
)

response
 
=
 
client
.
system_one
(
 
state
=
"I was charged twice. Please fix this ASAP."
,
 
questions
=
{
 
"billing"
: 
Noul
(
instructions
=
"Is this ticket about billing?"
),
 
"tone"
: 
Choice
(
 
instructions
=
"What is the customer's tone?"
,
 
criteria
=
{
"calm"
: 
None
, 
"frustrated"
: 
None
, 
"angry"
: 
None
},
 ),
 
"urgency"
: 
Score
(
 
instructions
=
"How urgent is this ticket?"
,
 
criteria
=
[
"can wait"
, 
"this week"
, 
"today"
],
 ),
 },
)

print
(
response
.
nouls
[
"billing"
].
noul
)

print
(
response
.
choices
[
"tone"
].
choice
)

print
(
response
.
scores
[
"urgency"
].
score
)

### Playground

With the server still running, open another terminal. You'll need Node 20.9+:

cd
 playground
npm install
npm run dev -- -p 3001

Openlocalhost:3001, load a preset, and edit the text and questions. Press⌘↵to run it. "Packed vs separate" compares asking all questions at once with asking them one at a time. "Permute" runs a Choice question with six option orders. There are also presets for testing question isolation and fake delimiter tokens.

There's achess demo, too. The board is the input, legal moves are Choice options, and a Score question rates the position. You can play against Kev or let it play itself. Games are saved inlocalStorage.

## Models

Start with Kev-4B. Use Kev-9B when accuracy and calibration matter more than memory. Use Kev-0.8B if you need the smallest model. All three are built on Qwen3.5 bases with the same training data and settings.

Model

Base

Accuracy: Trained Sources

Accuracy: New Sources

Brier: New Sources

Model Card

Kev-0.8B

Qwen3.5-0.8B-Base

0.825 / 0.834

0.652 / 0.684

0.499 / 0.460

Details

Kev-4B

Qwen3.5-4B-Base

0.872 / 0.871

0.797 / 0.837

0.299 / 0.255

Details

Kev-9B

Qwen3.5-9B-Base

0.872 / 0.874

0.822 / 0.852

0.286 / 0.237

Details

Jev

Hosted

0.845 / –

0.857 / –

0.211 / –

–

Each cell isdevelopment / test. "Trained sources" means held-out examples from the datasets used to train Kev. "New sources" means datasets and policy rule types Kev wasn't trained on. Every model was evaluated on the same development sets (decision-v7,transfer-v4) and the same test sets, which were read once per released checkpoint, after model selection. Lower Brier is better.

Kev-9B trails Jev by 3.5 points on the new-source development set (0.822 vs 0.857) and scores 0.852 on the test set, which Jev hasn't been run on. We don't know which datasets Jev was trained on, so this isn't a controlled comparison of the two architectures.

All three models were updated on 2026-09-21 with a short second training pass on generated examples: policy cases with explicit day counts, and cases whose deciding evidence was removed, trained toward a uniform answer. On the test set this moved Kev-9B from 0.837 to 0.852 (95% CI +0.8 to +2.9 points), Kev-4B from 0.832 to 0.837, and Kev-0.8B from 0.668 to 0.684. The previous weights are at revisionv7-base. Details and costs are in the model cards andPLAN.md.

Probabilities are calibrated by default. Each checkpoint stores a temperature (about 2.1–2.4) fitted on its in-distribution development set, and the pointer head applies it when the model is loaded. It never changes an answer: on new sources Kev-9B's calibration error goes from 0.106 to 0.042 and its confident errors (wrong answers with probability ≥ 0.9) from 8.7% to 4.0%, about Jev's 3.7%, with accuracy identical. SetKEV_TEMPERATURE=1.0for the raw logits. The accuracy numbers in the table are the same either way; the Brier numbers are for the raw logits.

One optional setting:KEV_DATE_FACTS=1appends the number of days between any two absolute dates found in the state ("June 26, 2026 is 8 days before July 4, 2026"). Kev can't subtract dates reliably but it can use a stated day count: on the deadline policy questions Kev-9B goes from 0.80 to 0.90 (Jev 0.93). The table above doesn't use it.

All weights are in theKev collectionand theGitHub release, which includes tarballs and SHA-256 checksums.

Previous generation (Qwen3) and the prototype

The first Kev family used Qwen3 bases with the same data and settings. Those weights stay published and are the faster choice on a Mac (seeServing Performance), but they are no longer developed.

Model

Base

Accuracy: Trained Sources

Accuracy: New Sources

Brier: New Sources

Model Card

Kev-0.6B (Qwen3) — 
jaredpalmer/kev-0.6b

Qwen3-0.6B-Base

0.801 / 0.808

0.620 / 0.642

0.536 / 0.483

Details

Kev-4B (Qwen3) — 
jaredpalmer/kev-4b@qwen3

Qwen3-4B-Base

0.854 / 0.856

0.790 / 0.806

0.328 / 0.294

Details

Kev-8B (Qwen3) — 
jaredpalmer/kev-8b

Qwen3-8B-Base

0.863 / 0.870

0.796 / 0.780

0.337 / 0.327

Details

Because only the base changed, the two generations are a controlled comparison. On the development set the accuracy gain is within noise; on the test set Kev-9B is 7.3 points ahead of Kev-8B (95% CI +2.8 to +11.7) with a Brier score 0.08 lower, Kev-4B is 2.9 points ahead of its predecessor (−0.9 to +6.4), and Kev-0.8B is 4.8 points ahead of Kev-0.6B (+0.2 to +9.3).PLAN_Qwen35.mdhas the full experiment, including the criteria we set in advance and how the results measured against them.

The originalKev-0.5Bused Qwen2.5-0.5B and is kept for reference; see itsmodel card.

## API

### POST /v1/systemone

stateis the text to evaluate. Each question has instructions and, where needed, a set of answers to choose from.

Type

Criteria

Answer

noul

Optional descriptions for 
true
 and 
false

noul
: probability of yes

choice

1–255 option names, each with a description or 
null

choice
: most likely option; 
probabilities
 and 
confidence

score

2–255 descriptions, ordered from lowest to highest

score
: mean level index, starting at 0; 
legend
, 
probabilities
, and 
confidence

For Choice withK > 1options, confidence is(p_max − 1/K) / (1 − 1/K). A single option has confidence 1. Score confidence measures how close the distribution is to its most likely level. It's an approximation of TypeSafe's formula, which isn't public. Neither field is a measured accuracy rate.

Objects and arrays are converted to labeled text. Delimiter-like strings in user input are escaped before tokenization. Invalid requests return422.usage.output_tokenscounts tokens in the serialized answers, not generated tokens.

Method

Path

Purpose

GET

/v1/models

Loaded model and checkpoint information

POST

/v1/systemone/permute

Run one Choice question with different option orders

POST

/v1/systemone/separate

Run each question in its own forward pass

The server binds to127.0.0.1and has no authentication. Keep it local unless you add authentication yourself.

## How It Works

Each checkpoint is a rank-16 LoRA adapter and a small pointer head on a Qwen base model. On an attention-only base (Qwen3), the state and questions go into one token sequence:

<state> …state…
<q> instructions <opt> option 1 </opt> <opt> option 2 </opt> … <decide>
<q> instructions <opt> option 1 </opt> <opt> option 2 </opt> … <decide>

The attention mask lets a token read the state and its own question, but not other questions or future tokens. Each question's position IDs restart just after the state. This lets the model process the state once and answer each question independently.

Qwen3.5 mixes attention layers with Gated DeltaNet layers, which are recurrent and ignore attention masks. For those models, each question runs as its own row: the state followed by that question, with the same positions as above. The rows are independent, so isolation is exact, and the server computes the state once and reuses its cache for every row. On attention-only models the two forms give identical probabilities (tests/test_v3.py).

The pointer head scores each option's</opt>hidden state against the question's<decide>hidden state. A softmax turns those scores into probabilities. Because<decide>comes last, it can attend to the full option list.

Training uses cross-entropy on the correct answer. The adapter and head are trained together; the rest of the base weights stay fixed. Training examples and API requests use the same text format. No Jev outputs were used for training.

Asking questions together or separately produces probabilities within 4e-6 in the fp32 tests. This doesnotmean option order is irrelevant: options within a question can still affect one another. Seethe model codeandparity tests.

## Serving Performance

On CUDA, installflash-linear-attentionfor the Qwen3.5 models (the Modal image does this); a five-question request takes tens of milliseconds on an H100.

On Apple Silicon there are no fast kernels for the DeltaNet layers, so PyTorch runs reference code. Median model time in bf16 on an M5, five questions with three options each on a ~230-token state:

Model

Time

Previous generation on the same request

Kev-0.8B

329 ms

Kev-0.6B (Qwen3): 123 ms

Kev-4B

779 ms

Kev-4B (Qwen3), 
jaredpalmer/kev-4b@qwen3
: 174 ms

Kev-9B

about 2 s

Kev-8B (Qwen3): about 300 ms

If you serve on a Mac and need low latency, use the Qwen3 models for now. An MLX backend for the Qwen3.5 models is the next planned change.

For the attention-only models the server merges the LoRA weights in fp32 before casting, uses SDPA attention on Apple GPUs, pads MPS inputs to 64-token buckets, and caches the state prefix for repeated requests (four states of at least 384 tokens by default). With a repeated 772-token state, Kev-4B (Qwen3) answers in 242 ms instead of 861 ms.

You can disable these withKEV_MERGE=0,KEV_ATTN=eager,KEV_SHAPE_BUCKET=1, andKEV_PREFIX_CACHE=0. On 24 new-source records, bf16 probabilities differed from fp32 by at most 0.017, with no change in the highest-probability answer. That is a small check, not a guarantee for every input.

## Training

The released models usedecision-v7: 10,000 examples from ten public datasets, 896 generated policy examples, and 1,680 examples from 60 generated rule structures. All train for two epochs with LoRA rank 16 and cross-entropy. The learning rate is1e-4for 0.8B and5e-5for 4B/9B. For Qwen3.5 bases the adapter also covers the DeltaNet projections;kev.trainpicks the right targets from the model config.

#
 sanity run, ~1 minute

uv run python -m kev.train --n_per_source 40 --accum 4 --out runs/smoke

#
 Kev-0.8B (~20 min on one H100; the Mac path works but is slow for Qwen3.5 bases)

uv run python -m kev.train --suite evals/v7/decision-v7 --base Qwen/Qwen3.5-0.8B-Base --base_revision dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68 \
 --epochs 2 --lr 1e-4 --batch 8 --dtype bf16 --p_none_pair 0.25 --device cuda --out runs/kev-0.8b

#
 the Kev-4B recipe (one H100 via Modal, ~1 h; see below). Swap in Qwen/Qwen3-4B-Base for the previous generation.

uv run python -m kev.train --suite evals/v7/decision-v7 --base Qwen/Qwen3.5-4B-Base --base_revision 1001bb4d826a52d1f399e183466143f4da7b741b \
 --epochs 2 --lr 5e-5 --batch 4 --accum 2 --dtype bf16 --checkpointing 1 --p_none_pair 0.25 --device cuda --out runs/kev-4b

### Fine-tuning on your own data

The released models were trained on public datasets and generated policy examples. If your questions look different — your own routing categories, your own escalation rules, another language — a short fine-tune on a few hundred labelled examples usually helps more than any prompt change.

Put your examples in a JSONL file, one request per line. It's the same shape as an API request, plus alabelon every question:

{
"state"
: {
"subject"
: 
"
Charged twice
"
, 
"body"
: 
"
I see two charges for order #4411. Please refund one.
"
},
 
"questions"
: {
 
"team"
: {
"type"
: 
"
choice
"
, 
"instructions"
: 
"
Which team should handle this ticket?
"
,
 
"criteria"
: {
"billing"
: 
"
Payments and refunds
"
, 
"shipping"
: 
"
Delivery problems
"
, 
"access"
: 
"
Login and account access
"
}, 
"label"
: 
"
billing
"
},
 
"angry"
: {
"type"
: 
"
noul
"
, 
"instructions"
: 
"
Is the customer angry?
"
, 
"label"
: 
false
},
 
"priority"
: {
"type"
: 
"
score
"
, 
"instructions"
: 
"
How urgent is this ticket?
"
, 
"criteria"
: [
"
low
"
, 
"
normal
"
, 
"
high
"
], 
"label"
: 
1
}}}

Forchoicethe label is the option name, fornoulit'strueorfalse, and forscoreit's the level's position starting at 0. Keep 10–20% of the file aside for evaluation.

Then start from a released checkpoint with--init_from:

uv run python -m kev.train --data train.jsonl --base Qwen/Qwen3.5-4B-Base --init_from jaredpalmer/kev-4b \
 --epochs 2 --lr 2e-5 --batch 1 --accum 8 --dtype bf16 --checkpointing 1 --device cuda --out runs/mine

uv run python -m kev.benchmark --run runs/mine --data heldout.jsonl --out runs/mine-eval
KEV_DTYPE=bf16 uv run --extra serve python -m kev.serve --run runs/mine --port 8009

--init_fromloads the adapter and pointer head from the released model before training, so you keep what Kev already knows and add your domain on top. Starting from the base model instead throws that away: in one user's test on 836 support-tool decisions, a fine-tune from the base scored 0.33 on Kev's own evaluation set, against 0.84 for the released model; the same data with--init_fromkept 0.83 there and reached 0.88 on the new domain. Use a smaller learning rate than the from-scratch recipe (2e-5is a good start), and pick--baseto match the checkpoint you start from; the trainer checks that the base, revision, LoRA rank, and head size agree before it loads anything.

--batch 1 --accum 8in bf16 fits the 0.8B model on a 4 GB GPU. The benchmark reports accuracy, Brier score, and calibration per question type, so you can see which of your questions the fine-tune helped. The checkpoint you started from is recorded inruns/mine/training_config.json.

Useuv run python -m kev.train --helpfor all training options. The released models don't use the optional--perm_klor--ord_wlosses. Themodel cardshave the training settings and dataset lists;PLAN.mdrecords what was tried and what helped.

On a Mac, run one training job at a time. Two jobs on the same Apple GPU are much slower. Use Modal for longer runs.

### Modal

Each trial gets its own H100. The study keeps running if you disconnect, and you can download the results when it finishes:

uv run modal token new 
#
 once; opens the browser

KEV_GPU=T4 uv run modal run modal_app.py::smoke 
#
 end-to-end check, ~1 minute of GPU

uv run modal deploy modal_app.py 
#
 once; studies run on the deployed app and survive disconnects

uv run modal run modal_app.py::study \
 --suite evals/v7/decision-v7 --plan experiments/v7-final.json \
 --name my-study --transfer evals/v4/transfer-v4 --budget 30 --timeout 7200
uv run modal run modal_app.py::pull --name my-study 
#
 results -> runs/my-study, ranked

Study planslist training settings. Each trial saves the settings, code hashes, dataset hashes, and results. Choose models using the development results, not the locked test. After choosing a final candidate, you can read its test results once:

uv run modal run modal_app.py::locked_test --trial my-study/00-trial-0 --name my-candidate 
#
 one read, ever

## Evaluation

The evaluation data underevals/is frozen: dataset versions and file checksums are recorded in each manifest. Large training files are downloaded fromthe Hub mirrorand checked against those hashes.

uv run python -m kev.benchmark --run jaredpalmer/kev-4b --suite evals/v4/transfer-v4 --out runs/my-eval 
#
 out of domain

uv run python -m kev.benchmark --run jaredpalmer/kev-4b --suite evals/v9/transfer-v9 --out runs/my-eval-v9 
#
 + MMLU-Pro, buried states, unknowable items

uv run python -m kev.benchmark --run jaredpalmer/kev-4b --suite evals/v7/decision-v7 --out runs/my-eval-id 
#
 in distribution

uv run python -m kev.benchmark --remote http://127.0.0.1:8009 --suite evals/v4/transfer-v4 --out runs/my-remote 
#
 any System One endpoint

These commands use development data. Test data requires--allow-test. The benchmark reports accuracy, Brier score, calibration error, the share of decisions you could automate at a 5% error budget, option-order changes, and question isolation.transfer-v9adds 10-way MMLU-Pro, records buried among unrelated text, and "unknowable" records whose deciding evidence was removed; for those it reports how often the model still answers with at least 0.9 confidence (Kev-9B 5%, Jev 9%, Kev-8B 26%). Published accuracy numbers use fp32 evaluation, not the bf16 serving path.

evals/external/holds two other projects' test sets converted to this format, with their published live Jev results:SemIf's 144 authored decisions (Kev-9B 0.917, Jev 0.965) andscienthoon's 900 support tickets (Kev-9B 0.952 on routing and 0.911 on tone, Jev 0.897 and 0.914).

kev.jevruns the same questions against Jev through Vercel AI Gateway.kev.comparecompares two saved runs with paired bootstrap confidence intervals. For the full experiment history, seePLAN.mdandthe leaderboard.

## Limitations

* Calibration is by a single temperature fitted in distribution. As served, Kev-9B assigns at least 0.9 probability to a wrong answer on 4.0% of new-source questions (Jev 3.7%); a fixed temperature can't reorder confidences, so the share of decisions you can automate at a 5% error budget (0.45–0.57) is still below Jev's 0.70. Test it on your own data before choosing a probability threshold.
* Fine-tuning can make the base model worse at individual tasks. Date arithmetic is the clearest case: the untrained Qwen3.5-9B base gets 0.82 on thedeadlinepolicy questions and the first Kev-9B got 0.72 (issue #8). Training on examples that state the day count, plusKEV_DATE_FACTS=1, recovers it (0.90). Knowledge questions (MMLU 0.74 vs Jev 0.90; MMLU-Pro 0.52 vs 0.84) are the remaining large gap, and they're set by the base model: a Kev trained on the 35B-A3B mixture-of-experts base didn't move them (PLAN.md).
* The current models are slow on Apple Silicon (see Serving Performance) and needtransformers >= 5.17.
* Changing option order can change an answer. Question isolation doesn't prevent this.
* Training uses at most 384 state tokens and 1,024 tokens for the state plus one question. Serving allows 8,192 tokens for the state plus one question; longer context wasn't covered by training.
* The server handles one request at a time. It caches repeated state text, but doesn't batch requests from different callers.

## Development

uv run --extra serve python -m pytest tests/test_unit.py tests/test_research.py -q 
#
 no weights, no server; runs in CI

KEV_BASE_URL=http://127.0.0.1:8009 uv run --extra serve python -m pytest tests/test_api.py -q 
#
 against a running server

cd
 playground 
&&
 npm run lint 
&&
 npx next typegen 
&&
 npx tsc --noEmit -p 
.

The API tests run TypeSafe's example requests and the official SDK against your local server.

Troubleshooting

* If MPS runs out of memory during training, check that you're running only one job. Don't enableoutput_hidden_statesor add tokens with peft'strainable_token_indices; both have caused memory problems here.
* If the playground loads but buttons don't work, uselocalhost:3001. Next.js checks development hostnames. Other hosts need an entry inallowedDevOriginsinplayground/next.config.ts.
* If dataset loading reportsDataset scripts are no longer supported, uselegacy-datasets/banking77. This repo already uses it.

## Authors

* Jared Palmer (@jaredpalmer)

Built withDevin. Thanks toArcher Humefor the architecture write-up,TypeSafefor the API design,Qwenfor the base models,3x3xX3N0Nfor showing where the date-arithmetic failure really is, andRadexitofor--init_from.

Related work:Hydragen,DeFT,FIRST.

## License

Apache-2.0. The Qwen3 and Qwen3.5 base models are also Apache-2.0. Training datasets have their own licenses; see themodel cards.