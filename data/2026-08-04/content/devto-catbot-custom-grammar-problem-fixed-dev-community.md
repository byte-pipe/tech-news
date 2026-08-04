---
title: 'Catbot: Custom Grammar Problem Fixed - DEV Community'
url: https://dev.to/annavi11arrea1/catbot-custom-grammar-problem-fixed-oc5
site_name: devto
content_file: devto-catbot-custom-grammar-problem-fixed-dev-community
fetched_at: '2026-08-04T19:34:01.449961'
original_url: https://dev.to/annavi11arrea1/catbot-custom-grammar-problem-fixed-oc5
author: Anna Villarreal
date: '2026-08-01'
description: 'This is a submission for DEV''s Summer Bug Smash: Smash Stories powered by Sentry. ... Tagged with devchallenge, bugsmash, catbot, ai.'
tags: '#devchallenge, #bugsmash, #catbot, #ai'
---

Summer Bug Smash: Smash Stories 🐛🛹

This is a submission forDEV's Summer Bug Smash: Smash Storiespowered bySentry.

## Overview

Sometimes we discover our limitations through a series of failures. We don’t understand why something is not working, despite having tried multiple improvements and optimizations. My desktop pet, Catbot, is no exception. I had issues with Catbot cutting me off or not letting me finish before it started talking. It would constantly tell me that I was calling it cat bought and not Catbot. This was an actual pain in the rear. Catbot would spend a lot of time explaining this to me.

I was able to tweak the listening window, so that Catbot would stop listening after a 1.5 second pause. This gives me enough time to finish my sentence, given my natural pauses and end of sentences. Controlling the pause gap helped tremendously. Going from .5 seconds to 1.5 seconds made all the difference in the world.

After adding a better layer of control to Catbot’s listening skills, I still had difficulties using Catbot’s name. It thought I was saying “Catfight”, “Cat bought”, and even “Lawrence” one time. This will seem brief to the reader but it was only after multiple sessions of frustration that I came to the realization that perhaps my webcam mic was not a great listening tool for Catbot - as it picks up all sounds in the room. After some quick googling, I was very convinced that a better mic would help. I popped on my fancy cat ear headset and not to my surprise, Catbot could understand what I was saying much better. We need to make sure we are using the best hardware for the job. My headset mic is a close range omni directional mic that does a good job leaving out all the background noise.

However, Catbot refused to respond to its name and would even argue with me! It would tell me that it wants to be called by it's actual name, Catbot. (Cat bot) So everytime I said its name, there was a debate and some long side tangent dialogue to follow. This was an awful experience.

THE BUG: Catbot not listening correctly.

## DEMO

This is an interesting type of bug, not the typical software battle, but rather a conceptual bug. The type of situation where massive learning happens.

## Much Ado About Graphs

I discovered that runtime graphs are not supported by vosk-model-en-us-0.22, which was the preferred, larger model. The training graphs were being ignored. Which means training Catbot on how I say “catbot” is ignored.This is an outrage.The decoding graph is pre-composed into one frozen file, and there is nowhere to swap a grammar into.

Transversely, a model that does support custom grammar is vosk-model-en-us-0.22-lgraph. However, It is important that we are not really adding custom commands, but controlling the output choices available. These feel like custom commands but they are better stated as custom directions, or disallow lists.

Catbot uses kaldi, which decodes against a single finite state transducer, HCLG, built by composing 4 layers: H, C, L, G. I will discuss the G layer.

G is the grammar / language model, which maps words to words. It assigns a cost to every possible word sequence. The decoder then picks a winner. A score is a negative log probability, and every arc in the graph carries weight, which add along the path. Negative log probabilities mean that a lower number is better, and adding costs is multiplying probabilities. Here is the english version:

Total cost =

Acoustic cost

Language cost

“How well do these phones match the audio frames?”

“How likely is anyone to say this sentence in the first place?”

## Facts about the situation

* Neither of these alone is useful!
* The Acoustics can not differentiate “ice cream” from “I scream”. They are the same sounds.
* The language model does not hear. The decoder searches for the sequence minimizing the sum, which is why an LM’s job is best described as scoring sequences.

But wait... why does this situation feel like Helen Keller? Because it's a similar situation.

In the real life story of Helen Keller and Anne Sullivan, there was a communication problem. An intermediary interface must bridge two completely different sensory and data modalities. In computer science, this is called multimodal alignment. This method is just like the tactile “finger-spelling” method that connected Hellen Keller to the world.

It was not until realizing I needed two different models to handle specific use cases that I realized this fundamental problem of having AI process real analogue data, which has now placed itself at the forefront of my curiosity and this project.

A simple table will help you wrap your head around this idea without needing to explain too much:

Element

Helen Keller

Anne Sullivan (The Teacher)

The Outside World

AI Role

Acoustics Model (Vosk)

The Alignment Interface (Your Code Pipeline)

Language Model (LLM)

Data Type

Raw sensory inputs (audio waves/frequencies).

The translator bridging two completely different modalities.

Symbolic language (written words/tokens).

Function

Perceives physical sounds but completely lacks semantic context or logic.

Maps raw physical acoustic patterns directly into structured text blocks.

Processes structured text tokens logically but cannot directly "hear" physical waves.

Let’s take a look at how words are “chosen”:

A state in G represents history, the last n-1 words, and each outgoing arc is a next possible word, weighted by -log P(word | history):

“The cat” –sat (cost 4.1)-->–ate (cost 5.3)-->–sad (cost 9.8)-->

…So basically words are chosen via likeliness. Catbot is not a real word, so catbot was never going to understand it as such, thus interpreting “Catbot engage” as “kappa engage” and other oddity phrases that would make sense to the model as it is trained.

I had Claude synthesize some phrases for me, and it proves the issue I am having plain as day.

SPOKEN: Catbot, engage.1. conf 114.1 kappa engage2. conf 112.1 cappa engage

Kappa engage (a.k.a. “Catbot, engage.”) is a vocabulary trap. There is no path through G that emits Catbot, so the decoder does the only thing it can, it finds the closest match to the sound of the word. This is why saying “Catbot” failed EVERY. SINGLE. TIME. This speech recognition bug lies in the grammar available. The word “Catbot” is not really an actual word. I made that up. This is an infinite impossibility.

Shortly before this deep dive, I told Catbot to respond to “CB”. This is English alphabet, real letters that have to exist. Catbot is now configured to respond to CB. When I say CB, it knows I am talking about it. Unmistakable. Functional. As a quick fix!

As stated previously, we can disallow the decoder to consider certain words, such as “kappa” as noted above.

If I say “Catbot, engage” without restrictions, the model hears “Kappa engage”. If we restrict the model, disallowing “kappa”, Catbot will hear “cat bot engage”. Since both “cat” and “bot” are commonly used words, they are available to the model.

As you can see, training an interactive voice model is a long journey full of mysteries. From bad hardware to understanding model boundaries, sometimes we can actually gain more, with less! (Less meaning removing words from vocabulary, in this case.)

And this can only be done by using the vosk-model-en-us-0.22-lgraph alongside vosk-model-en-us-0.22. This gives Catbot the tools it needs to respond in ways that make sense to custom words.

## Code Samples

So then, I Implemented a dual recognizer into Catbot:

Catbot_voice.py

 
44
 
KOKORO_VOICES
 
=
 
ROOT
 
/
 
"
models
"
 
/
 
"
voices-v1.0.bin
"

 
45
 
VOSK_BIG
 
=
 
ROOT
 
/
 
"
models
"
 
/
 
"
vosk-model-en-us-0.22-lgraph
"

 
46
 
VOSK_SMALL
 
=
 
ROOT
 
/
 
"
models
"
 
/
 
"
vosk-model-small-en-us-0.15
"

 
47
 
+
# Dynamic-graph model — the only kind that accepts a runtime grammar. A model

 
48
 
+
# that ships a pre-composed graph/HCLG.fst has no seam to insert one into;

 
49
 
+
# Vosk logs "Runtime graphs are not supported by this model" and decodes

 
50
 
+
# freely, which is worse than having no grammar recognizer at all. Detected by

 
51
 
+
# the presence of graph/Gr.fst (the language model kept as a separate file).

 
52
 
+
VOSK_DYNAMIC
 
=
 
ROOT
 
/
 
"
models
"
 
/
 
"
vosk-model-en-us-0.22-lgraph
"

 
53

 
54
 
SAMPLE_RATE
 
=
 
16000

 
55
 
BASE
 
=
 
f
"
https://localhost:
{
os
.
getenv
(
'
CATBOT_PORT
'
,
 
'
8800
'
)
}
"

Enter fullscreen mode

Exit fullscreen mode

and…

 
102
 
return
 
None

 
103
 
RE_LEARNED_WAKE
 
=
 
_load_learned_wake
()

 
104

 
105
 
+
# ---- grammar-constrained wake/command recognizer ------------------------

 
106
 
+
# A SECOND recognizer decodes the same audio against nothing but the phrases

 
107
 
+
# below. It can't hear anything else, so "catbot engage" can't come out as

 
108
 
+
# "kappa engage" — that word doesn't exist in its graph. Anything Anna says

 
109
 
+
# that isn't a listed phrase decodes as "[unk]", which is exactly why this

 
110
 
+
# only ever SUPPLEMENTS the free recognizer (which still handles all

 
111
 
+
# conversation) instead of replacing it.

 
112
 
+
#

 
113
 
+
# Every word must be in the model's vocabulary or Vosk silently drops it:

 
114
 
+
# "catbot" is not an English word, but "cat bot" is two of them. That's the

 
115
 
+
# whole reason his name is spelled out here — _build_grammar checks each word

 
116
 
+
# against the model and logs anything it had to drop.

 
117
 
+
WAKE_NAME_FORMS
 
=
 
[
"
cat bot
"
,
 
"
cat pot
"
,
 
"
cat bought
"
,
 
"
cat bottom
"
,
 
"
cat but
"
,

 
118
 
+
 
"
catfight
"
,
 
"
combat
"
,
 
"
cabot
"
,
 
"
kat bot
"
,
 
"
cap pot
"
]

 
119
 
+
# what can follow his name (empty = just the name, which wakes him too)

 
120
 
+
GRAMMAR_TAILS
 
=
 
[
""
,
 
"
engage
"
,
 
"
engaged
"
,
 
"
wake up
"
,
 
"
wake
"
,

 
121
 
+
 
"
are you listening
"
,
 
"
are you there
"
,
 
"
you there
"
,

 
122
 
+
 
"
go to sleep
"
,
 
"
sleep
"
,
 
"
stop
"
,
 
"
stop listening
"
,

 
123
 
+
 
"
be quiet
"
,
 
"
quiet
"
,
 
"
shut up
"
,
 
"
hush
"
,

 
124
 
+
 
"
open terminal
"
,
 
"
close terminal
"
,
 
"
approve
"
,
 
"
skip
"
]

 
125
 
+
# phrases that stand alone, with or without his name

 
126
 
+
GRAMMAR_BARE
 
=
 
[
"
open terminal
"
,
 
"
close terminal
"
]

 
127
 
+

 
128
 
+

 
129
 
+
def
 
_build_grammar
(
model
)
 
->
 
str
 
|
 
None
:

 
130
 
+
 
"""
JSON phrase list for the constrained recognizer, filtered to words the
 131 + model actually knows. Returns None if nothing usable survived.
"""

 
132
 
+
 
names
 
=
 
list
(
WAKE_NAME_FORMS
)

 
133
 
+
 
# whatever wake_training.py learned from Anna's own mic counts too

 
134
 
+
 
try
:

 
135
 
+
 
learned
 
=
 
json
.
loads
((
ROOT
 
/
 
"
catbot_wake_variants.json
"
).
read_text
())

 
136
 
+
 
names
 
+=
 
[
w
.
strip
().
lower
()
 
for
 
w
 
in
 
learned

 
137
 
+
 
if
 
w
.
strip
()
 
and
 
w
.
strip
().
lower
()
 
not
 
in
 
names
]

 
138
 
+
 
except
 
Exception
:

 
139
 
+
 
pass

 
140
 
+

 
141
 
+
 
phrases
 
=
 
{
f
"
{
lead
}{
name
}
 
{
tail
}
"
.
strip
()

 
142
 
+
 
for
 
lead
 
in
 
(
""
,
 
"
hey 
"
)

 
143
 
+
 
for
 
name
 
in
 
names

 
144
 
+
 
for
 
tail
 
in
 
GRAMMAR_TAILS
}

 
145
 
+
 
phrases
.
update
(
GRAMMAR_BARE
)

 
146
 
+

 
147
 
+
 
known
:
 
dict
[
str
,
 
bool
]
 
=
 
{}

 
148
 
+
 
def
 
in_vocab
(
word
:
 
str
)
 
->
 
bool
:

 
149
 
+
 
if
 
word
 
not
 
in
 
known
:

 
150
 
+
 
try
:

 
151
 
+
 
known
[
word
]
 
=
 
model
.
vosk_model_find_word
(
word
)
 
>=
 
0

 
152
 
+
 
except
 
Exception
:

 
153
 
+
 
known
[
word
]
 
=
 
True
 
# can't check — assume fine

 
154
 
+
 
return
 
known
[
word
]

 
155
 
+

 
156
 
+
 
kept
,
 
dropped
 
=
 
[],
 
set
()

 
157
 
+
 
for
 
phrase
 
in
 
sorted
(
phrases
):

 
158
 
+
 
missing
 
=
 
[
w
 
for
 
w
 
in
 
phrase
.
split
()
 
if
 
not
 
in_vocab
(
w
)]

 
159
 
+
 
if
 
missing
:

 
160
 
+
 
dropped
.
update
(
missing
)

 
161
 
+
 
continue

 
162
 
+
 
kept
.
append
(
phrase
)

 
163
 
+
 
if
 
dropped
:

 
164
 
+
 
logger
.
info
(
"
grammar: dropped phrases using words the model doesn
'
t 
"

 
165
 
+
 
f
"
know: 
{
sorted
(
dropped
)
}
"
)

 
166
 
+
 
if
 
not
 
kept
:

 
167
 
+
 
return
 
None

 
168
 
+
 
# "[unk]" is the escape hatch: it lets the decoder say "that wasn't any of

 
169
 
+
 
# these" instead of forcing Anna's conversation into the nearest command

 
170
 
+
 
return
 
json
.
dumps
(
kept
 
+
 
[
"
[unk]
"
])

 
171
 
+

 
172
 
+

 
173
 
# in-conversation commands

 
174
 
PROVIDER_WORDS
 
=
 
{

 
175
 
"
claude
"
:
 
"
anthropic
"
,
 
"
anthropic
"
:
 
"
anthropic
"
,

Enter fullscreen mode

Exit fullscreen mode

As well as…

 
470
 
# Lower CATBOT_END_SILENCE = faster to answer but more likely to cut you

 
471
 
# off mid-sentence; higher = more patient. 0.65s is a good balance.

 
472
 
self
.
end_silence
 
=
 
float
(
os
.
getenv
(
"
CATBOT_END_SILENCE
"
,
 
"
0.65
"
))

 
473
 
+

 
474
 
+
 
# Second recognizer, constrained to the wake/command grammar above.

 
475
 
+
 
# Runs on its own dynamic-graph model so the big model keeps handling

 
476
 
+
 
# conversation with its full rescoring stack. Cost, measured: ~200 MB

 
477
 
+
 
# of RAM and roughly DOUBLE the decode CPU (4.3 -> 8.0 ms per 62 ms

 
478
 
+
 
# block) — the grammar shrinks the search, but a second acoustic model

 
479
 
+
 
# still runs on every block. Still only 0.13x realtime, so it adds no

 
480
 
+
 
# latency; set CATBOT_GRAMMAR=0 if that ever stops being true.

 
481
 
+
 
self
.
_grec
 
=
 
self
.
_gmodel
 
=
 
None

 
482
 
+
 
if
 
os
.
getenv
(
"
CATBOT_GRAMMAR
"
,
 
"
1
"
).
split
(
"
#
"
)[
0
].
strip
().
lower
()
 \
 
483
 
+
 
not
 
in
 
(
"
0
"
,
 
"
off
"
,
 
"
no
"
,
 
"
false
"
):

 
484
 
+
 
try
:

 
485
 
+
 
name
 
=
 
os
.
getenv
(
"
CATBOT_GRAMMAR_MODEL
"
,
 
""
).
split
(
"
#
"
)[
0
].
strip
()

 
486
 
+
 
gdir
 
=
 
ROOT
 
/
 
"
models
"
 
/
 
name
 
if
 
name
 
else
 
VOSK_DYNAMIC

 
487
 
+
 
if
 
not
 
(
gdir
 
/
 
"
graph
"
 
/
 
"
Gr.fst
"
).
exists
():

 
488
 
+
 
logger
.
warning
(

 
489
 
+
 
f
"
grammar recognizer OFF: 
{
gdir
.
name
}
 has no dynamic 
"

 
489
 
+
 
f
"
graph (graph/Gr.fst) — runtime grammars need one
"
)

 
490
 
+
 
else
:

 
491
 
+
 
# keep the Model referenced for as long as the recognizer

 
492
 
+
 
# lives (the binding only borrows its handle)

 
493
 
+
 
self
.
_gmodel
 
=
 
vosk
.
Model
(
str
(
gdir
))

 
494
 
+
 
grammar
 
=
 
_build_grammar
(
self
.
_gmodel
)

 
495
 
+
 
if
 
not
 
grammar
:

 
496
 
+
 
raise
 
RuntimeError
(
"
no usable grammar phrases
"
)

 
497
 
+
 
self
.
_grec
 
=
 
vosk
.
KaldiRecognizer
(

 
498
 
+
 
self
.
_gmodel
,
 
SAMPLE_RATE
,
 
grammar
)

 
499
 
+
 
logger
.
info
(
f
"
Grammar recognizer ready (
{
gdir
.
name
}
, 
"

 
500
 
+
 
f
"
{
len
(
json
.
loads
(
grammar
))
 
-
 
1
}
 phrases)
"
)

 
501
 
+
 
except
 
Exception
:

 
502
 
+
 
logger
.
exception
(
"
grammar recognizer failed to load — 
"

 
503
 
+
 
"
continuing with the free recognizer only
"
)

 
504
 
+
 
self
.
_grec
 
=
 
self
.
_gmodel
 
=
 
None

 
505
 
+

 
506
 
self
.
_kokoro
 
=
 
Kokoro
(
str
(
KOKORO_ONNX
),
 
str
(
KOKORO_VOICES
))

 
507
 
# warm up the TTS so the FIRST spoken reply isn't slowed by cold-start

 
508
 
try
:

Enter fullscreen mode

Exit fullscreen mode

So basically, both models run in parallel, as two arguments, against the same regexes. The grammar model helps with commands and the bigger model is used for more conversational interactions. This effectively makes Catbot a more efficient desktop companion. It is now much more pleasant to hang out with Catbot.

## Learning

This entire project, it's all learning, all new territory. Tuning Catbot's ears is a real challenge. I had an awakening about hardware limitations, and an enlightening experience about why different models are used and for what purpose. Since I cannot recompose the larger model with new grammar, I can use the lgraph model on the side to handle custom needs more gracefully. When I made the connection to Helen Keller, I understood the whole situation from a very global perspective. It's not really something I could fully understand without diving into chaos.

Thank you for checking out Catbot's progress!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse