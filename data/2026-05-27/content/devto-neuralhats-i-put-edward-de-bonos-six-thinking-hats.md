---
title: 'NeuralHats: I Put Edward de Bono’s Six Thinking Hats on Local LLMs Using Gemma 4 - DEV Community'
url: https://dev.to/georgekobaidze/neuralhats-i-put-edward-de-bonos-six-thinking-hats-on-local-llms-using-gemma-4-54mj
site_name: devto
content_file: devto-neuralhats-i-put-edward-de-bonos-six-thinking-hats
fetched_at: '2026-05-27T19:44:10.515200'
original_url: https://dev.to/georgekobaidze/neuralhats-i-put-edward-de-bonos-six-thinking-hats-on-local-llms-using-gemma-4-54mj
author: Giorgi Kobaidze
date: '2026-05-24'
description: 'This is a submission for the Gemma 4 Challenge: Build with Gemma 4 What I Built ... Tagged with devchallenge, gemmachallenge, gemma.'
tags: '#devchallenge, #gemmachallenge, #gemma'
---

Gemma 4 Challenge: Build With Gemma 4 Submission

This is a submission for theGemma 4 Challenge: Build with Gemma 4

## What I Built

### The Exact Moment It Clicked

Two weeks ago, when Jess posted about the Gemma 4 challenge, I got stuck in a decision-making loop. I didn't know which idea to build, and I had a few competing options.

Usually, when I think about a new project idea, I don't tell anyone until it is completely done. That is just how I like working. I speak with results, not with plans.

Because of that, I did not really have anyone to brainstorm with. I found myself wishing I had a room full of people I could talk through the decision with, to help me figure out which idea to actually commit to.

Then it suddenly reminded me of Edward de Bono'sSix Thinking Hats, which I had read about five years ago. And I thought, damn, I wish I had a local AI system where I could actually run that kind of structured discussion.

Then I stopped...

Whoa, wait a second... Why am I wishing for this? Why don't I just build it RIGHT NOW?

And not just build it, but make it fully local on my own PC. No APIs, no cloud. Just something I can run instantly and talk to like a thinking room inside my machine!

That felt like the idea!

What if I could conjure six of those personas on demand, locally, for free, and let them argue about anything I wanted? And even participate in the discussion when needed?

So I builtNeuralHats- a local web app where six AI personas, each running on its own tuned instance of Gemma 4, sit around a virtual debate table and argue about any topic you give them. They follow the canonical order. They actually disagree. The Blue Hat, the chairperson, decides when the debate is over. And when the dust settles, a seventh model, the Facilitator, writes a final report you can save as a PDF.

### What it Actually Does

* 🎩Six tuned personasdebate any topic you choose
* 🔄Up to 5 rounds, with the Blue Hat deciding when to wrap up via aCONTINUE/STOPtoken
* 🧑‍💼You can join in, claim one of the hats and contribute your own perspective live
* 📡Server-Sent Eventsstream each hat's turn the moment it's ready
* 📄PDF reportsynthesised by a dedicated Facilitator model at the end
* 💯100% local:no API keys, no cloud calls, no telemetry, no internet required after setup

## Demo

Check out the video walkthrough:

## Code

### The Essentials

## georgekobaidze/neuralhats

### Six AI personas debate any topic using Edward de Bono's Six Thinking Hats framework. Powered by Gemma 4 via Ollama. Runs fully local.

# NeuralHats

Six AI personas. One structured debate. Every perspective covered

🎥 Demo Video·📖 Article·🐛 Report a Bug

## Table of Contents

* About
* Features
* Tech Stack
* Architecture
* Project Structure
* Getting Started
* Configuration
* Security
* How to Contribute
* What's Next
* License
* Acknowledgements
* Author

## About

NeuralHatsbrings Edward de Bono's legendarySix Thinking Hatsframework to life through AI. Instead of reading about the method, you experience it. Six distinct AI personas debate any topic you choose, each embodying a different mode of thinking.

Each hat is a fully independent AI model persona powered byGemma 4viaOllama, with its own system prompt, voice, and reasoning style:

Hat

Role

Focus

⚪ 
White

The Analyst

Pure facts, data, and objective information

⚫ 
Black

The Critic

Risks, flaws, and devil's advocacy

🟢 
Green

The Creative

Bold ideas, lateral thinking, alternatives

🔴 
Red

The Feeler

Emotions, gut instinct, raw reaction

🟡 
Yellow

…

View on GitHub

To run it yourself:

git clone https://github.com/georgekobaidze/neuralhats.git

cd 
neuralhats
./setup.sh 
# or .\setup.ps1 on Windows

./start.sh 
# or .\start.ps1 on Windows

Enter fullscreen mode

Exit fullscreen mode

That's it. The setup script pulls Gemma 4, creates the seven custom models, installs the Python and Node dependencies, andstartboots the FastAPI backend and Vite frontend together. You'll be debating athttp://localhost:5173within minutes.

### Architecture in one breath

React + Vite + Tailwind v4 ──HTTP/SSE──► FastAPI (Python) ──HTTP──► Ollama ──► Gemma 4
 │
 └──► SQLite (aiosqlite, ON DELETE CASCADE)

Enter fullscreen mode

Exit fullscreen mode

Three layers, zero external services. The frontend is a single-page React app with a virtual debate table. The backend is a small FastAPI server with one main orchestrator and an SSE stream. The AI layer is seven custom Ollama models - six hats plus a Facilitator, all built from the same Gemma 4 base.

Let me walk you through the parts I'm most proud of.

### One Base Model, Seven Personalities

Running seven separate copies of Gemma 4 would turn my GPU into lava. Instead, I used Ollama's Modelfile system to create seven lightweight aliases over thesame base weights- each with its own temperature, top-p, and system prompt:

# backend/modelfiles/Modelfile.template
FROM {{BASE_MODEL}}

PARAMETER temperature {{TEMPERATURE}}
PARAMETER top_p {{TOP_P}}
PARAMETER num_ctx 8192

Enter fullscreen mode

Exit fullscreen mode

The setup script bakes in personality through parameters:

# setup.ps1

$HatParams
 
=
 
@{

 
white
 
=
 
@{
 
temp
 
=
 
"0.3"
;
 
top_p
 
=
 
"0.9"
 
}
 
# cold facts

 
black
 
=
 
@{
 
temp
 
=
 
"0.4"
;
 
top_p
 
=
 
"0.9"
 
}
 
# cautious critic

 
green
 
=
 
@{
 
temp
 
=
 
"0.9"
;
 
top_p
 
=
 
"0.95"
 
}
 
# creative chaos

 
red
 
=
 
@{
 
temp
 
=
 
"0.85"
;
 
top_p
 
=
 
"0.95"
 
}
 
# raw emotion

 
yellow
 
=
 
@{
 
temp
 
=
 
"0.6"
;
 
top_p
 
=
 
"0.9"
 
}
 
# warm optimist

 
blue
 
=
 
@{
 
temp
 
=
 
"0.3"
;
 
top_p
 
=
 
"0.9"
 
}
 
# disciplined chair

 
facilitator
 
=
 
@{
 
temp
 
=
 
"0.2"
;
 
top_p
 
=
 
"0.9"
 
}
 
# near-deterministic synthesis

}

Enter fullscreen mode

Exit fullscreen mode

Red Hat runshot(0.85) - its job is intuition, gut feelings, vibes. White Hat runscold(0.3) - its job is facts and only facts. Switching from one to another costs nothing because they all share weights in memory. Personality is just parameters and prompts.

### The Blue Hat is a Controller, Not Just a Debater

The Blue Hat is the chairperson. Its prompt forces it to end every response with exactly one of two tokens on its own line:

End your response with exactly one of these two tokens on its own line:
 CONTINUE — if meaningful new ground can still be explored
 STOP — if consensus has been reached or no new insights are likely

Enter fullscreen mode

Exit fullscreen mode

The orchestrator parses that token to decide whether to start another round or end the debate.The LLM's output literally becomes control flow.

# backend/orchestrator.py

def
 
_parse_blue_decision
(
blue_response
:
 
str
)
 
->
 
bool
:

 
"""
Return True if debate should CONTINUE, False if it should STOP.
 Scans lines in reverse to handle trailing text. Defaults to CONTINUE.
"""

 
for
 
line
 
in
 
reversed
(
blue_response
.
strip
().
splitlines
()):

 
token
 
=
 
line
.
strip
().
upper
()

 
if
 
token
 
==
 
"
CONTINUE
"
:

 
return
 
True

 
if
 
token
 
==
 
"
STOP
"
:

 
return
 
False

 
return
 
True

Enter fullscreen mode

Exit fullscreen mode

That tiny function is the heartbeat of the whole loop. Reverse-scanning so trailing whitespace or quote marks don't break parsing. Safe default toCONTINUEbecause terminating early is worse than running one too many rounds.

### The debate loop

Here's the actual orchestrator stripped down. Six hats, in order, up to five rounds, controlled by the Blue Hat's verdict:

HAT_ORDER
 
=
 
[
HatColor
.
WHITE
,
 
HatColor
.
BLACK
,
 
HatColor
.
GREEN
,

 
HatColor
.
RED
,
 
HatColor
.
YELLOW
,
 
HatColor
.
BLUE
]

MAX_ROUNDS
 
=
 
5

for
 
round_num
 
in
 
range
(
1
,
 
MAX_ROUNDS
 
+
 
1
):

 
await
 
_push
({
"
type
"
:
 
"
round_start
"
,
 
"
round
"
:
 
round_num
})

 
for
 
hat
 
in
 
HAT_ORDER
:

 
if
 
hat
 
==
 
user_hat
:

 
content
 
=
 
await
 
_await_user_turn
(
hat
)
 
# human steps in

 
else
:

 
await
 
_push
({
"
type
"
:
 
"
hat_thinking
"
,
 
"
hat
"
:
 
hat
})

 
messages
 
=
 
_build_messages
(
topic
,
 
conversation_history
,

 
hat
=
hat
,
 
round_num
=
round_num
)

 
content
 
=
 
await
 
ollama_client
.
chat
(
messages
,
 
hat
=
hat
,
 
mode
=
mode
)

 
conversation_history
.
append
({
"
hat
"
:
 
hat
,
 
"
content
"
:
 
content
,

 
"
round
"
:
 
round_num
,
 
"
is_user
"
:
 
is_user
})

 
await
 
_push
({
"
type
"
:
 
"
message
"
,
 
"
hat
"
:
 
hat
,
 
"
content
"
:
 
content
,
 
...})

 
if
 
hat
 
==
 
HatColor
.
BLUE
:

 
blue_response
 
=
 
content

 
if
 
not
 
_parse_blue_decision
(
blue_response
)
 
or
 
round_num
 
==
 
MAX_ROUNDS
:

 
await
 
_push
({
"
type
"
:
 
"
debate_end
"
,
 
"
status
"
:
 
"
completed
"
})

 
return

Enter fullscreen mode

Exit fullscreen mode

That's almost the entire thing. No agent framework, no LangChain, no LangGraph. Just a loop, a queue, and a parsed token. The simplicity is the point.

### Real-time streaming with SSE

Waiting 30 seconds for an entire debate to finish before showing anything would be unbearable. So I push each completed hat turn overServer-Sent Eventsthe moment it's ready:

async
 
def
 
event_stream
():

 
while
 
True
:

 
event
 
=
 
await
 
_event_queue
.
get
()

 
yield
 
event

 
if
 
event
.
get
(
"
type
"
)
 
in
 
(
"
debate_end
"
,
 
"
error
"
):

 
# Hold the connection open briefly so the browser receives the

 
# final event before the server closes.

 
await
 
asyncio
.
sleep
(
2
)

 
break

Enter fullscreen mode

Exit fullscreen mode

The frontend'sEventSourcereacts in real time, a new chat bubble appears as soon as each hat finishes thinking. Watching it unfold feels like watching a real panel discussion.

### 🎯 Structured conversation history beats flat transcripts

Earlier on I noticed the hats were ignoring each other. The Yellow Hat would give a generic positive answer that didn't actually respond to the Black Hat's specific risk. That was a context problem, they were getting a flat blob of text and skimming it.

So I restructured the history: separatedprevious roundsfromcurrent round so far, surfaced themost recent Blue Hat directionprominently, and gave each hatper-hat remindersto prevent drift:

_HAT_REMINDERS
 
=
 
{

 
HatColor
.
WHITE
:
 
(

 
"
REMINDER: Review the conversation history above. Do not repeat any fact, 
"

 
"
statistic, or metric you have already stated in a previous round. 
"

 
"
Every sentence must be new information.
"

 
),

 
HatColor
.
YELLOW
:
 
(

 
"
REMINDER: White Hat
'
s data points and Black Hat
'
s identified risks are 
"

 
"
valuable findings — not just Green Hat
'
s ideas. If you endorsed Green Hat 
"

 
"
last round, you MUST endorse a different hat this round.
"

 
),

 
HatColor
.
RED
:
 
(

 
"
REMINDER: Pick ONE emotional state for this response and stay in it the 
"

 
"
whole way through. Do NOT swing between opposite feelings in a single turn.
"

 
),

 
# ... and three more

}

Enter fullscreen mode

Exit fullscreen mode

After this change, the debates suddenly felt coherent. Hats started naming each other ("As Black Hat just pointed out..."). The Yellow Hat actually engaged with risks instead of pretending they didn't exist. Same model, same temperatures, just a smarter conversation envelope.

### A separate Facilitator

The seventh model,neuralhats-facilitator, runs at temperature0.2, almost deterministic. It's not inHAT_ORDER. It never debates. Its only two jobs:

1. Title generation:when the user types a topic, the Facilitator drafts a short title for the debate
2. Final report synthesis:after the Blue Hat votes STOP, the Facilitator reads the entire transcript and writes a neutral, structured summary the user can export as PDF

Splitting it off from the hats keeps the synthesis voice neutral and the temperature low enough to actually be useful as a summary. Mixing those jobs into one of the colored hats would compromise both.

### Cascade Deletes

The schema looks like this:

CREATE
 
TABLE
 
rounds 
(

 
id
 
TEXT
 
PRIMARY
 
KEY
,

 
debate_id
 
TEXT
 
NOT
 
NULL
,

 
round_number
 
INTEGER
 
NOT
 
NULL
,

 
created_at
 
TEXT
 
NOT
 
NULL
,

 
FOREIGN
 
KEY 
(
debate_id
)
 
REFERENCES
 
debates
(
id
)
 
ON
 
DELETE
 
CASCADE

);

CREATE
 
TABLE
 
messages 
(

 
id
 
TEXT
 
PRIMARY
 
KEY
,

 
round_id
 
TEXT
 
NOT
 
NULL
,

 
hat
 
TEXT
 
NOT
 
NULL
,

 
content
 
TEXT
 
NOT
 
NULL
,

 
is_user_message
 
INTEGER
 
NOT
 
NULL
,

 
timestamp
 
TEXT
 
NOT
 
NULL
,

 
FOREIGN
 
KEY 
(
round_id
)
 
REFERENCES
 
rounds
(
id
)
 
ON
 
DELETE
 
CASCADE

);

Enter fullscreen mode

Exit fullscreen mode

ON DELETE CASCADEfrom messages → rounds → debate means deleting a debate is asingle atomic operation. Hundreds of related rows disappear with oneDELETE FROM debates WHERE id = ?. No application-level cleanup, no orphaned data, no foot-guns.

## How I Used Gemma 4

I went withGemma 4 E4Bas my default base model.

Here's why:

### The constraint: it has to be local, and it has to be fast

NeuralHats fires6–7 model invocations per debate round(one per hat, plus the facilitator for final synthesis). With 5 rounds max, that's up to31 inference calls in a single debate. If each call takes 30 seconds, that's a 15-minute debate which is pretty unusable.

I needed a model that was:

* Small enough to run smoothly on consumer hardware (laptops, mid-range desktops)
* Fast enough that a hat's response feels like watching someone think, not waiting for a printer
* Capable enough to actually hold a position and engage with arguments, not just produce plausible-sounding mush

### Why E4B specifically

The26Bmodel would have been the safe "capability" choice, clearly better at reasoning. But it still turned out to be too much for the turn-based UX I needed. Each round would take minutes, killing the live-panel feeling.

TheE2B(2B) model is lightning fast but it didn't hold its hat persona well enough, under pressure it would drift, lose the role, or repeat itself.

E4B hit the sweet spot.It runs comfortably on a 16 GB VRAM machine, generates a hat response in 3–8 seconds depending on hardware, and is capable enough that with the right system prompt and per-hat parameters it genuinely stays in character. Watching the Red Hat shift emotional tone between rounds, or the Black Hat surface genuinely novel risks each time, that's all E4B.

### What Gemma 4 unlocked that nothing else could

Three things, specifically:

1. Native multi-instance personality.Because Ollama lets me create lightweight aliases over the same base weights, I get seven distinct AI personas without seven copies of the weights in RAM. Try that with a hosted API and you're paying for seven independent context windows. With Gemma 4 local, it's free.

2. The Blue Hat'sCONTINUE/STOPdiscipline.Small models often fail at strict format constraints, they want to ramble. Gemma 4 E4B reliably ends every Blue Hat turn with exactly one of those tokens on its own line. Without that reliability, the whole control-flow trick falls apart.

3. The freedom to ship "100% local" as a feature, not a constraint.No API costs, no rate limits, no internet dependency, no privacy concerns about feeding personal dilemmas to a third party. For an app whose entire premise is"let six minds help you think through something you wouldn't want to discuss with anyone else"- that's not a nice-to-have. That's the product.

## Summary

NeuralHats started because I was stuck inside my own head and needed another perspective. It turned into a project about how, with the right architecture, a single E4B model can play six different roles convincingly enough to actually help you think.

The Gemma 4 family made that possible, small enough to run on my own machine, smart enough to genuinely disagree with itself, and disciplined enough that a 200-word Blue Hat summary ends with the exact token my orchestrator needs to make a decision.

If you've ever been stuck inside your own head, clone it, run it, give it your problem, and let the hats argue. Worst case, you have a good laugh. Best case, you get unstuck.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse