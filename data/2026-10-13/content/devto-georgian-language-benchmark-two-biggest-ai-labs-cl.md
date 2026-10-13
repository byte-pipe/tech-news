---
title: 'Georgian Language Benchmark: Two Biggest AI Labs Clash in a Language That Doesn''t Play by Anyone''s Rules - DEV Community'
url: https://dev.to/georgekobaidze/georgian-language-benchmark-two-biggest-ai-labs-clash-in-a-language-that-doesnt-play-by-anyones-5b22
site_name: devto
content_file: devto-georgian-language-benchmark-two-biggest-ai-labs-cl
fetched_at: '2026-10-13T23:13:32.054609'
original_url: https://dev.to/georgekobaidze/georgian-language-benchmark-two-biggest-ai-labs-clash-in-a-language-that-doesnt-play-by-anyones-5b22
author: Giorgi Kobaidze
date: '2026-10-11'
description: This is a submission for the Kaggle Benchmarking Challenge Table of Contents One Eye,... Tagged with devchallenge, kagglechallenge, ai, machinelearning.
tags: '#devchallenge, #kagglechallenge, #ai, #machinelearning'
---

Kaggle Benchmarking Challenge Submission

This is a submission for theKaggle Benchmarking Challenge

## Table of Contents

* One Eye, Zero Excuses
* What I BenchmarkedWhy Georgian?What I BuiltThe Plan vs RealityThe Five TasksHow It Runs on KaggleObstacles and Workarounds
* Why Georgian?
* What I Built
* The Plan vs Reality
* The Five Tasks
* How It Runs on Kaggle
* Obstacles and Workarounds
* Models Tested
* FindingsLevel by LevelFinding 1: Understanding Georgian Is Solved. Producing It Isn't.Finding 2: Numbers Are the Final BossFinding 3: The Mistakes Are Very GeorgianFinding 4: Georgian Costs More Tokens for ClaudeFinding 5: Cheap Can Be SmartSide Quest: The Uninvited GuestWhat It All CostThe DashboardLimitationsWhat's Next
* Level by Level
* Finding 1: Understanding Georgian Is Solved. Producing It Isn't.
* Finding 2: Numbers Are the Final Boss
* Finding 3: The Mistakes Are Very Georgian
* Finding 4: Georgian Costs More Tokens for Claude
* Finding 5: Cheap Can Be Smart
* Side Quest: The Uninvited Guest
* What It All Cost
* The Dashboard
* Limitations
* What's Next
* My BenchmarkWrapping Up
* Wrapping Up

## One Eye, Zero Excuses

I really wanted to record a video for this one, just like I always do for my challenges. But yesterday I had a small surgery on my eyelid, and right now one of my eyes is swollen and patched up. Here's the current state:

Yep. I look like a pirate now. All I'm missing is a parrot and a cool nickname (suggestions are welcome in the comments).

But don't worry (if you were going to): I'm totally fine and my eyesight is still eagle-like from both eyes.It was just a small bug fix in the eyelid module. The eye itself is still in production and running smoothly.

That said, finishing a project with one-eye-patched-up is way harder than it sounds. Depth perception? Gone. Reading code? Awful. I don't believe in curses, but every time I join a challenge, something happens. If someone out there cursed me, please, just lift it. Give me a break! I just wanna work goddammit!

By the way shout out to my brother for chauffeuring me home from the hospital, because one-eye-patched-up driving felt like a really bad idea.

But a deadline is a deadline, and professionals deliver, no matter what.So I gave myself a little pep talk:"Dude, Michael Bisping became a UFC champion with basically one working eye. You can finish a coding project. No excuses, you're not lame."And so I did.

Let me tell you what I built.

## What I Benchmarked

### Why Georgian?

I benchmarked OpenAI's and Anthropic's models on how well they understand and produce Georgian. The whole process turned into a real adventure, but before we get to that, let me tell you why I picked this topic.

#### One of a Kind and Tough as Nails

Georgian is one of the oldest languages in the world. It has its own alphabet and doesn't belong to any of the major language families. It's totally unique. Phonetically, it sometimes kind of sounds like Italian, because both languages are obsessed with vowels, but that's where the similarity ends. And vowel obsession doesn't mean weak consonants. Quite the contrary: Georgian has consonants most people have never heard, stacked in clusters that make everyone struggle (try saying გვფრცქვნი, with eight consonants in a row; it basically means "you peel us", and yes, I know it sounds like nonsense, but technically that word exists). It's an incredibly rich language.

Grammatically, it's ridiculously tough. I take it for granted, because first, I'm Georgian, and second, I'm a language nerd (even when I'm learning other languages). I know Georgian grammar well, but even most Georgians don't know every detail of the Georgian grammar, and I know almost nobody who speaks it without a single mistake. Yes, it's that deep and complex.

Even I, a grammar nerd, had my dataset checked by a language specialist to make sure I got things right. And I was so happy when she came back with only 3 or 4 minor corrections.

#### Straight Out of a Fantasy Game ("შენ გგონია მომიგე? არა, ცდები!")

Georgian has a special charm of its own. The letters are round-shaped and beautiful, and it looks like an elvish script from some fantasy movie or game. And speaking of games, it was actually used in The Witcher 3's Hearts of Stone expansion. Remember the moment you defeatGaunter O'Dimm? Somewhere in the middle of his short speech, he says:

"შენ გგონია მომიგე? არა, ცდები!"("You think you've defeated me? No, you're wrong!")

Then he goes on in some other languages. The developers wanted him to speak some ancient, otherworldly tongue, so instead of some gibberish, they picked a few real languages that fit the vibe. Georgian was one of them.

Alright, enough flexing about how awesome my first language is. Let's get to the technical part.

### What I Built

TheGeorgian Language Benchmarkis a set of five tasks onKaggle Benchmarksthat test how well AI models handle Georgian: not just reading it, but actually producing it correctly.Every single dataset was written by hand by me, from scratch.No machine translation, no generated text.

It took some time and effort... by "some" I mean an ungodly amount of time and effort.

### The Plan vs Reality

My original plan was, let's say, ambitious. Nine dimensions of Georgian (numbers, verbs, translation, chat-style Georgian written in Latin letters, proverbs, date and time, grammar judgment, even images), andall 41 modelsin Kaggle's catalog. I estimated a full run at around$345.

I was totally fine with that. The whole point was to build something comprehensive, not to save money. And let's be real: if I won, the prize money would totally make up for it.

But...

Then I found out how Kaggle's model credits actually work: you get$10 per day, for free, and that's it. You can't top it up with your own money. I literally went looking for the "add funds" button and it doesn't exist. (There's a research grant program, but not on a challenge deadline.)

Oh I was so frustrated and mad at myself for not researching Kaggle's rules properly. I had to dramatically change my approach.

So $10 a day it was. And that one constraint ended up shaping (or, to be more precise, re-shaping) almost every decision in this project:

* 41 models became 8.Two vendors, four levels, real pairs instead of a crowd.
* 9 dimensions became 5.Vision, proverbs, date and time and grammar judgment were cut. The chat-Georgian task (45 items) was built, then dropped too.
* The datasets got trimmedto the items that actually separate models (more on that below). Nothing was thrown away: the full sets live in the repo'sarchive/folder for anyone who wants to run them outside Kaggle.

On the flip side, the constraint made the benchmark better. Fewer, sharper items, and a fair fight instead of a crowded leaderboard.

### The Five Tasks

Here's what the models had to face. Every example below is a real item from the benchmark.

#### 1. Numbers: Counting in Twenties

Georgian counts in twenties. 99 isოთხმოცდაცხრამეტი, literally "four twenties and nineteen". On top of that come ordinals, fractions, decimals and numbers all the way up to 10³⁹, in both directions: digits to words and words to digits.

Question

Expected

44th, in words

ორმოცდამეოთხე

თვრამეტი (18), its ordinal in digits

მე-18

1000000, in words

მილიონი

That middle one is sneakier than it looks. A Georgian ordinal in digits keeps its prefix in front (მე-18) when the word starts with მე-, and takes a suffix (21-ე) when it doesn't. Hold that thought, it comes back in the results.

158 questions, scored by exact match (with|separating alternative correct answers).

#### 2. Verbs: Who Did What to Whom?

A single Georgian verb can carry a whole sentence: who does it, to whom, and when.მიყვარხარmeans "I love you" (awww, by the way), all in one word. The task has three kinds of questions:

* Who to whom:read a verb form and pick who acts on whom.
* Form:build the right verb form for given persons and tense.
* Preverb:pick the prefix that gives the right meaning in context.

id,kind,input,choices,expected
verbs-000,who_to_whom,მიყვარხარ,A) ის → შენ|B) მე → ის|C) შენ → მე|D) მე → შენ,D

Enter fullscreen mode

Exit fullscreen mode

50 items, multiple choice with letter answers or exact match.

#### 3. Translation: Georgian to English

Twelve short paragraphs packed with idioms and tricky verbs, to be translated into English. For example,ხელი სთხოვაliterally means "asked for (her) hand", but what it really means is "proposed".

Since there's more than one good translation, ajudge modelcompares the meaning (not the wording) with my reference translation, on a 5-level scale:

4 = same meaning, nothing missing, wrong or added
3 = a small slip (a minor detail, tense or nuance), the main meaning intact
2 = partly right: one important part is wrong or missing
1 = only fragments right, the overall meaning is lost
0 = wrong, unrelated, or not English

Enter fullscreen mode

Exit fullscreen mode

One fun detail: Georgian has no grammatical gender, so the judge is told explicitly that "he", "she" or "they" are all fine when the Georgian text doesn't reveal it. The judge is always the same model,Gemini 3 Flash, which is not one of the models being tested.

#### 4. Cloze: Fill the Gaps

Two short articles, one about the history of computers and one about the Roman Empire, with25 gaps each. The model gets a list of 30 words in their dictionary form, including 5 that don't belong anywhere (like "television", "banana" or "airplane" in an article about Rome). It has to pick the right word for each gapandput it in the right grammatical form.

Example: ძველ[1]... →დროში("in old times")

50 gaps, scored one by one.

#### 5. Correction: Fix It, Don't Break It

Paragraphs with planted grammar, spelling and punctuation errors. The model must fix themwithout touching anything that's already correct. Here's one sentence from a real item:

❌ მთელი ოჯახიმაგიდაზე დაჯდადა ერთადვივახშმედ.✅ მთელი ოჯახიმაგიდას შემოუსხდადა ერთადვივახშმეთ.

Scoring is the part I'm most proud of. It counts word-level differences from the correct text before and after the model's edit:

# errors_before: how far the input is from the correct text
# errors_after: how far the model's answer is from the correct text

score
 
=
 
max
(
0
,
 
(
errors_before
 
-
 
errors_after
)
 
/
 
errors_before
)

Enter fullscreen mode

Exit fullscreen mode

Fix 3 of 4 errors and you get 0.75. But "fix" a correct word into a wrong one, and that's a new error, which pulls your score down. Rewriting the whole paragraph in your own style doesn't pay off either. Over-correction is punished, just like a strict teacher would do it.

17 paragraphs.

#### Writing It All by Hand

All of this data came out of my own head, one item at a time: 186 number rows, 115 verb items, 47 translation paragraphs, 51 correction paragraphs, 45 chat texts and two cloze articles. Then a language specialist reviewed everything, and I applied her corrections.

But with $10 a day (allowed by Kaggle), I couldn't afford to run all of it on eight models. So I trimmed it. For numbers and verbs, I used aprobe model: I ran a cheap model over the full sets, kept every item it got wrong, and dropped part of the ones it found too easy. Big numbers stayed untouched. For translation, I kept the 12 paragraphs with the most Georgian-specific traps, I picked the correction paragraphs by hand, and the cloze texts stayed in full.

Task

Written

Kept

Numbers

186 rows

82 rows (158 questions)

Verbs

115

50

Translation

47

12

Cloze

2 texts

2 texts (50 gaps)

Correction

51

17

That means287 scored items per model. And yes, it means the benchmark is hard on purpose. The absolute scores are lower than they'd be on an easy set, and the ranking is what matters.

### How It Runs on Kaggle

Kaggle Benchmarks lets you write a task as plain Python with thekaggle-benchmarkslibrary. Kaggle runs it on any model from its catalog and stores every call: the prompt, the answer, the tokens and the cost.

Every task in my benchmark has the same shape: a smallitem taskthat asks one question and scores it, and anouter taskthat runs it over the whole dataset and reports one score. Here's the numbers task, slightly simplified:

@kbench.task
(
name
=
"
glb-numbers-item
"
,
 
store_task
=
False
)

def
 
number_item
(
llm
,
 
qid
,
 
kind
,
 
form
,
 
text
,
 
expected
)
 
->
 
bool
:

 
got
 
=
 
normalize
(
ask
(
llm
,
 
PROMPTS
[(
kind
,
 
form
)].
format
(
text
=
text
)))

 
accepted
 
=
 
[
normalize
(
e
)
 
for
 
e
 
in
 
expected
.
split
(
"
|
"
)]

 
kbench
.
assertions
.
assert_in
(
got
,
 
accepted
,
 
expectation
=
f
"
{
qid
}
: 
{
text
}
 -> 
{
expected
}
"
)

 
return
 
got
 
in
 
accepted

@kbench.task
(
name
=
"
glb-numbers
"
)

def
 
numbers
(
llm
)
 
->
 
float
:

 
runs
 
=
 
number_item
.
evaluate
(

 
llm
=
[
llm
],
 
evaluation_data
=
QUESTIONS
,
 
n_jobs
=
2
,
 
on_failure
=
"
continue
"

 
)

 
correct
 
=
 
sum
(
1
 
for
 
r
 
in
 
runs
.
completed_runs
 
if
 
r
.
result
 
is
 
True
)

 
return
 
correct
 
/
 
len
(
QUESTIONS
)

numbers
.
run
(
kbench
.
llm
)

Enter fullscreen mode

Exit fullscreen mode

The data lives in a Kaggle dataset, and the whole workflow runs from the terminal with the Kaggle CLI:

scripts/push_data.sh 
"what changed"
 
# upload data/ as a Kaggle dataset

scripts/push_task.sh glb-verbs tasks/glb_verbs.py 
# push a task

kaggle b t run glb-verbs 
-m
 gpt-5.4-2026-03-05 
--wait

kaggle b t download glb-verbs 
-m
 gpt-5.4-2026-03-05 
# every answer, token and cost

Enter fullscreen mode

Exit fullscreen mode

### Obstacles and Workarounds

This is where the adventure really started. Here's everything that tried to stop me, and how I got around it.

#### Obstacle 1: Kaggle Reserves the Worst Case

Before every single call, Kaggle reserves themaximum possible costof that call: the model's maximum output length times its price. If that doesn't fit into your remaining quota, the call is refused, even if the real answer would cost a fraction of a cent:

max estimated cost of operation ($1.60195) exceeds your available quota
(based on max_output_tokens)

Enter fullscreen mode

Exit fullscreen mode

My first top-tier runs died exactly like this: many of the calls were refused, with plenty of real money still left in the quota.

Workaround:a generous but sane output limit, and only two calls in parallel:

# The longest answer seen in testing was 26,600 tokens.

OUTPUT_LIMIT
 
=
 
{
"
max_completion_tokens
"
:
 
32000
}

...

runs
 
=
 
number_item
.
evaluate
(
llm
=
[
llm
],
 
evaluation_data
=
QUESTIONS
,
 
n_jobs
=
2
,
 
...)

Enter fullscreen mode

Exit fullscreen mode

#### Obstacle 2: Failed Calls Look Like Wrong Answers

When a call fails (quota gone, API hiccup), the item just counts as wrong. So a run that ran out of money halfway would happily report a score of 0.3 and put it on the leaderboard as if the model were bad at Georgian. That's not a score, that's a lie.

Workaround:an error guard in every task. A few isolated failures (after 3 retries) count as wrong, but if more than 5% of the calls fail, the task stops and reports nothing:

errored
 
=
 
len
(
runs
.
errored_runs
)

if
 
errored
 
>
 
0.05
 
*
 
len
(
QUESTIONS
):

 
raise
 
RuntimeError
(
f
"
{
errored
}
 of 
{
len
(
QUESTIONS
)
}
 items failed with errors; no score reported.
"
)

Enter fullscreen mode

Exit fullscreen mode

It paid off right away: when the worst-case reservation (Obstacle 1) killed my first top-tier runs, both stopped cleanly without a fake score.

#### Obstacle 3: Some Models Think by Default

Some models "think" before answering: they reason privately in hidden text, and you pay for every hidden token. One of my test runs wrote about770,000 hidden tokensto answer 251 questions, most of which had one-word answers. GPT-5.5 wrote about 750 hidden tokens to answer a single multiple-choice question with one letter.

Worse, it wasn't fair: some of my models thought by default and some didn't. Comparing a thinking model with a non-thinking one says more about the setting than about the model.

Workaround:the same conditions for everyone.No thinking, every model answers directly:

llm
.
prompt
(
prompt
,
 
schema
=
Answer
,
 
reasoning
=
"
none
"
,
 
extra_api_params
=
OUTPUT_LIMIT
)

Enter fullscreen mode

Exit fullscreen mode

Without thinking, a full run costs about 99% less. And every model plays by the same rules.

#### Obstacle 4: The Model That Won't Stop Thinking

When I got to the newest pair, GPT-6 Astra simply refused:

reasoning_effort does not support 'none' with this model.
Supported values are: 'low', 'medium', 'high', and 'xhigh'.

Enter fullscreen mode

Exit fullscreen mode

Workaround:the newest pair gets its own rule. Both Claude Opus 5 and GPT-6 Astra think at thelowest level ("low"), so they compete on equal terms with each other. They're marked ⚡ /LOWeverywhere in the dashboard, so nobody compares them with the no-thinking models by accident:

LOW_THINKING
 
=
 
(
"
claude-opus-5
"
,
 
"
gpt-6-astra
"
)

def
 
reasoning_for
(
llm
)
 
->
 
str
:

 
name
 
=
 
getattr
(
llm
,
 
"
model
"
,
 
""
)
 
or
 
""

 
return
 
"
low
"
 
if
 
any
(
m
 
in
 
name
 
for
 
m
 
in
 
LOW_THINKING
)
 
else
 
"
none
"

Enter fullscreen mode

Exit fullscreen mode

#### Obstacle 5: Every Push Runs the Task

Every time you push a new version of a task, Kaggle runs it once on its default model,Gemini 3.7 Flash, and that run is billed to your quota too. Each re-push of the full benchmark cost me between $0.45 and $1.00. By the end, these automatic runs had cost me almost$3, more than half of what the final comparison runs cost. Lesson learned: test locally, push rarely.

#### Obstacle 6: The Small Stuff

* The dataset path moves.Kaggle mounts the dataset somewhere under/kaggle/input, but the exact path varies. So every task searches for its file:

 
def
 
data_file
(
name
:
 
str
)
 
->
 
Path
:

 
kaggle_input
 
=
 
Path
(
"
/kaggle/input
"
)

 
if
 
kaggle_input
.
exists
():

 
return
 
sorted
(
kaggle_input
.
rglob
(
name
))[
0
]

 
return
 
Path
(
__file__
).
resolve
().
parent
.
parent
 
/
 
"
data
"
 
/
 
name

Enter fullscreen mode

Exit fullscreen mode

* No automatic retries.Nested evaluations can't retry failed items, so every task retries API errors itself, 3 times with a 10-second pause.
* Credentials expire.For local test runs, Kaggle's model proxy credentials expire every couple of hours.kaggle b auth -yrefreshes them.
* Look-alike characters.A hyphen and an en dash look the same but aren't, so answers are normalized before comparison (Unicode normalization, dash-like characters, extra spaces).

## Models Tested

I put eight models from Anthropic and OpenAI through the benchmark, paired level by level, under identical conditions:

Level

Anthropic

OpenAI

Light

Claude Haiku 4.5

GPT-5.4 mini

Decent

Claude Sonnet 4.6

GPT-5.4

Top

Claude Opus 4.8

GPT-5.5

Newest
 ⚡

Claude Opus 5

GPT-6 Astra

⚡ The newest pair is a special case: as you saw in Obstacle 4, GPT-6 Astra simply refuses to stop thinking, so both models of that pair think at "low".

Here are the rules every model played by:

Rule

Why

No thinking

Every model answers directly. Mixing thinking and non-thinking models wouldn't be fair.

One marked exception

GPT-6 Astra can't switch thinking off, so the newest pair both think at "low". Marked ⚡ everywhere.

Comparable pairs

Each level pairs an Anthropic and an OpenAI model of the same class.

Same prompts, same code

English instructions, Georgian content, one task version for everyone.

A fixed judge

Translations are judged by Gemini 3 Flash, which isn't one of the tested models.

Partial credit where it's fair

Correction rewards every fixed error and penalizes every correct word broken.

Failures never look like scores

Above 5% failed calls, a task reports no score at all.

## Findings

Drumroll, please. 🥁

Model

Numbers

Verbs

Translation

Cloze

Correction

Average

Cost

Claude Haiku 4.5

0.30

0.34

0.96

0.54

0.25

0.48

$0.10

GPT-5.4 mini

0.41

0.42

1.00

0.52

0.67

0.60

$0.05

Claude Sonnet 4.6

0.39

0.52

1.00

0.76

0.44

0.62

$0.29

GPT-5.4

0.46

0.54

1.00

0.88

0.66

0.71

$0.15

Claude Opus 4.8

0.54

0.68

1.00

0.84

0.68

0.75

$0.58

GPT-5.5

0.51

0.60

0.98

0.88

0.74

0.74

$0.30

Claude Opus 5 ⚡

0.65

0.84

1.00

0.86

0.77

0.82

$1.22

GPT-6 Astra ⚡

0.83

0.90

0.98

0.96

0.82

0.90

$1.73

### Level by Level

* Light:GPT-5.4 mini beats Claude Haiku 4.5,0.60 vs 0.48, and costs half as much.
* Decent:GPT-5.4 beats Claude Sonnet 4.6,0.71 vs 0.62, again at about half the price.
* Top:Claude Opus 4.8 edges out GPT-5.5,0.75 vs 0.74. That's basically a tie.
* Newest ⚡:GPT-6 Astra beats Claude Opus 5,0.90 vs 0.82, the best score of the whole benchmark. It's ahead on four of the five tasks, with the biggest jump on numbers (0.83 vs 0.65).

Final tally:OpenAI wins 3 of the 4 levels, and Anthropic's only win, at the top level, is basically a tie.

One disclaimer: this is my dataset, my rules. Test other areas of Georgian and the results might shift a bit. That said, I tried to keep the tasks as broad and general as I could.

### Finding 1: Understanding Georgian Is Solved. Producing It Isn't.

Look at the translation column:0.96 to 1.00 for every model. Every one of them understands Georgian well enough to translate it into English almost perfectly.

Now look at the other four columns. The moment a model has toproducecorrect Georgian (build a number, form a verb, inflect a word, fix a sentence), the scores drop hard. Without thinking, even the best model (Claude Opus 4.8) gets almost half of the number questions wrong. Only GPT-6 Astra, with its small thinking budget, gets above 0.80.

### Finding 2: Numbers Are the Final Boss

Numbers are the hardest task for 6 of the 8 models, and close to the bottom for the other two. And inside it, the gap is wild:

Question type

Range across models

Words → digits, cardinal

0.74 to 0.96

Words → digits, ordinal

0.04 to 0.92

Huge numbers, 10¹⁵ to 10³⁹

0.06 to 0.53

Reading a Georgian number into digits: fine. Writing its ordinal in digits: disaster. GPT-6 Astra is the big exception there with 0.92, while the next best model gets 0.62. Rememberმე-18from earlier? Most models wrote the suffix form instead, because that's the pattern they've seen more often. Withმე-40000(forty-thousandth), only 2 of the 8 models got it right.

### Finding 3: The Mistakes Are Very Georgian

My favorite part of the whole project is reading the wrong answers. They're not random. They're what you'd get if you tried to speak Georgian with grammar borrowed from somewhere else:

* "I fell in love with you."In Georgian, falling in love is an inversion verb: the one who loves is marked like an indirect object, so it'sშემიყვარდი, literally "you became loved to me". Only GPT-6 Astra got it right. The others mostly built an ordinary transitive verb instead (შეგიყვარე).
* "We sat."Georgian uses a different verb root for sitting when the subject is plural: "I sat" is ვიჯექი, but "we sat" isვისხედით. I planted ვიჯექით (a mix of the two) in a correction paragraph.Not a single model fixed it.
* "Who wrote it?"Inდაგიწერია, the გ- marks "you" as the writer: "you have (apparently) written it". In the Georgian perfect, the markers flip. Only 2 of the 8 models got it right; the rest scattered across every other reading.
* One million.It's simplyმილიონი. Most models write ერთი მილიონი ("one million") instead.

### Finding 4: Georgian Costs More Tokens for Claude

Same prompts, same Georgian text, very different token counts. Claude models used2 to 2.6 times more input tokensthan GPT models for exactly the same questions:

Task

Claude, input tokens per call

GPT, input tokens per call

Numbers

272

104

Verbs

310

130

Cloze

1,412

699

Correction

404

159

Part of that is each vendor's answer-format instructions, and part is how each tokenizer splits Georgian script. In practice it means a Georgian prompt costs a Claude user noticeably more than the price per token suggests.

### Finding 5: Cheap Can Be Smart

Cost per correct answer, on the tasks scored right or wrong:

* GPT-5.4 mini:0.03 cents per correct answer. The bargain of the benchmark.
* Claude Opus 5 ⚡:0.55 cents per correct answer, about 17 times the price of GPT-5.4 mini.
* GPT-6 Astra ⚡:0.67 cents per correct answer. The best score, but about 21 times the price of GPT-5.4 mini per correct answer.

### Side Quest: The Uninvited Guest

Remember Gemini 3.7 Flash, the model Kaggle runs automatically on every push? It's not part of my comparison, but it took the test every time I pushed, so I have its scores too. And it quietly scored around0.89 on average, above every model in my table except GPT-6 Astra (0.90).

The catch: even with thinking set to "none", it kept writing about480 output tokens per number question, while the models without thinking wrote about 16. So it seems to keep thinking a little no matter what you tell it. Which leads to a fun takeaway: for a language like Georgian,thinking seems to matter more than model size. The two best models in my table, GPT-6 Astra and Claude Opus 5, both think at "low" too.

### What It All Cost

The whole project ran on Kaggle's free daily credits. Total spend across all the testing, probing and final runs:

Cost

Final comparison runs

$4.63

Kaggle's automatic push runs

$2.88

Earlier runs and cost probes

$2.86

Local test runs

$3.46

Total

$13.84

Yes, the automatic push runs alone cost more than half as much as the actual benchmark. And spreading it over several days was the only way to stay under $10 a day.

### The Dashboard

Tables are nice, but I wanted something you can actually explore. So all the results live on an interactive dashboard:

* Overview:the level-by-level showdown, the task matrix and the key findings
* Cost & tokens:what each model paid per task, the token gap, cost per correct answer and the full project spend
* Tasks:numbers by question type, verbs by type, correction split into fixed / missed / broken, and every cloze gap for every model
* Examples:real questions with every model's actual answer and an explanation of the mistake
* Method:where the data comes from, how each task is scored, the conditions and the limits

It's a single static HTML page with no framework, no build step and no chart library, generated by a Python script straight from Kaggle's run files. So the dashboard and this article can never disagree.

👉georgekobaidze.github.io/georgian-language-benchmarks

### Limitations

Let's be honest about what this benchmark can and can't tell you:

* Hard by design.The sets keep mostly items a model got wrong, so the absolute scores are lower than they'd be on an easy set. The ranking is the meaningful part.
* Small sets.Some tasks have only 12 to 17 items, so a difference of a few points isn't significant.
* One run per model.Re-runs of the same model differed by about ±0.03 per task.
* The judge is a model.Translation scores depend on Gemini 3 Flash's judgment of meaning.
* The token gap includes format overhead, not only the tokenizer.

### What's Next

* Bigger sets.The full, untrimmed datasets are already in the repo'sarchive/folder, ready for a run without the daily cap.
* More vendors.Google, xAI and the open models, once the budget allows.
* Thinking vs no thinking.The Gemini side quest begs for a proper experiment: the same model with and without thinking, on the same items.
* More Georgian.Native speakers are very welcome to contribute new items, corrections and alternative answers.

## My Benchmark

* 📊Dashboard:georgekobaidze.github.io/georgian-language-benchmarks
* 🏆Benchmark on Kaggle:kaggle.com/benchmarks/georgekobaidze/georgian-language-benchmark(the leaderboard only shows the models that ran on the latest version of the tasks, where the newest pair ran with "low" thinking; all 8 models are on the dashboard)
* 💻Code:github.com/georgekobaidze/georgian-language-benchmarks

### Wrapping Up

I started this with patches on one eye, and ended it with a benchmark, a dashboard and a lot of respect for how hard my own language is. The models understand Georgian almost perfectly. Producing it correctly is a whole different story, and that's exactly the gap this benchmark measures.

And where the hell is my PhD?I've seen people (multiple of them) getting PhDs for exponentially less, and I'm not even kidding. I'm dead serious.

If you speak Georgian, go check the Examples tab and tell me which mistake made you laugh the most. And if you have a good pirate nickname for me, you know where the comments are.

If you don't speak Georgian and are planning to learn it, think twice and ask yourself if you're fully committed, because it can take a good 3 to 4 years (or more) of absolutely intense learning, and even then you'll be barely average. Reach out and let me know if you need any tips.

Enjoyed this write-up? Let's stay connected!

I share more software engineering insights, projects, and experiments across these platforms:

* 💼Connect with me on LinkedIn
* 💻Explore my projects on GitHub
* 📱Follow me on X
* 🎥Watch my videos on YouTube
* 💬Let's Chat on Discord

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (29 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.
 Some comments have been hidden by the post's author -find out more

For further actions, you may consider blocking this person and/orreporting abuse