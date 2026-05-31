---
title: I Made My AI Models Argue, Then Let Hermes Be the Judge - DEV Community
url: https://dev.to/arqamwd/i-made-my-ai-models-argue-then-let-hermes-be-the-judge-5e6c
site_name: devto
content_file: devto-i-made-my-ai-models-argue-then-let-hermes-be-the-j
fetched_at: '2026-06-01T04:17:35.104114'
original_url: https://dev.to/arqamwd/i-made-my-ai-models-argue-then-let-hermes-be-the-judge-5e6c
author: Arqam Waheed
date: '2026-05-30'
description: 'A $0 multi-model decision agent: three LLMs debate, Hermes judges, and it learns who to trust. Tagged with hermesagentchallenge, devchallenge, agents, ai.'
tags: '#hermesagentchallenge, #devchallenge, #agents, #ai'
---

Hermes Agent Challenge Submission: Build With Hermes Agent

This is a submission for theHermes Agent Challenge: Build With Hermes Agent

TL;DR— Ask any judgment call and three different AI models argue it out, then Hermes hands down one verdict, a confidence score, and exactly why they split. Every verdict, dissent, and mind-changed-in-debate is written into Hermes' own memory, so the next question re-weights the jurors before they ever vote. The judging is a pure function over that memory: no memory, no weights, no verdict. Three models, one verdict, $0.

## What I Built

An LLM once talked me into the wrong database with total confidence. One smooth, authoritative answer. I shipped it. It cost me a weekend and a migration I'm still not over.

The villain here issingle-model overconfidence: you get one polished reply, and the disagreement that should have warned you is invisible. You never see the other opinions, because you only asked one model.

So I stopped trusting one model. I convened a jury.

Council takes any judgment call ("Postgres or Mongo?", "is this PR safe to merge?", "is this clause risky?") and asksthree different models, lets them disagree, then has Hermes deliver one verdict, a confidence score, and exactlywhythey split. Three models, one verdict, $0.

You ask a question. Council fans it out to three jurors (two free OpenRouter models from different families and one local model via Ollama), each takes a position with reasons. Then, if they disagree, asecond deliberation roundruns: each juror sees the others' answers and either holds or changes its mind, so the councildebatesinstead of just voting once. Hermes then judges the deliberated opinions: a single verdict, aconfidence score(high when they agree, low when they split 2-1), and a "why they disagreed" panel. Every verdict is remembered, acouncilskill learns which juror to trust for which kind of question, and the agent can evenpropose its owntrust adjustments for you to approve.

The whole product is one question box. Everything interesting happens behind it, and the rest of this post is mostly pictures of that "behind."

## Demo

Repo:https://github.com/ArqamWaheed/council

Live demo:https://council-jet-kappa.vercel.app/Hermes orchestration is local-only (no Hermes binary on serverless); the hosted demo runs the same UI via OpenRouter/mock. Run locally for the real hermes -z path.

Try "Should a 3-person startup use microservices?" and open the dissent panel.

Local, one command (runs at $0 in offline mock mode, no key needed):

git clone https://github.com/ArqamWaheed/council 
&&
 
cd 
council 
&&
 ./setup_hermes.sh 
&&
 python server.py

Enter fullscreen mode

Exit fullscreen mode

## Architecture, in pictures

I think the design is easiest tosee, so here's the system as a sequence of images. Each caption is the explanation.

The core loop. One question, three independent Hermes subagents (2 hosted + 1 local) fanned out in parallel, then a fourth Hermes run (the foreman) synthesizes one verdict. Every arrow is the samehermes -zinterface; nothing talks to a model directly.

The bet. A hosted model and an on-device model sit on the same jury, swapped with a single--provider/--modelflag, no code change. This model-agnosticism is the one Hermes property the whole project is built on.

The UX surface. Confidence is high when jurors agree and drops on a 2-1 split. The dissent panel is collapsed by default, and you expand it exactly when the confidence number makes you nervous.

The actual product. A confident single answer hides this; Council makes the disagreement the headline. Getting the clustering right here was subtle (see "What I learned" below).

The headline feature: a council that **deliberates, not just votes. After round 1, disagreeing jurors get a second Hermes pass where they read each other's arguments and may hold or change their vote. A "⇄ changed" badge marks the ones that moved, and the confidence dial actually climbs when a 2-1 split is talked into agreement.

The agentic learning loop, human-in-the-loop. Hermes proposes; you approve or dismiss. Approved rules persist client-side and ride along with the next convene call.

Persistence the judge can verify. Verdicts are mirrored into Hermes' own memory, so recall is Hermes doing the work; proof lives indocs/hermes-proof/04-memory-recall.txt.

## Code

Repo:https://github.com/ArqamWaheed/council

Interesting files:

* hermes_run.py(the Hermes CLI driver every juror/judge call goes through)
* run_council.py(orchestration + the deterministic judge + Hermes foreman + the--reflectloop)
* skills/council/SKILL.md(the juror-weighting brain Hermes edits)
* server.py(the/api/reflect+/api/learnendpoints)
* index.html(the designed verdict UI with the foreman TTS readout and localStorage persistence).

Proof that Hermes is genuinely in the loop (subagent transcripts, skill diff, memory recall) is indocs/hermes-proof/.

# hermes_run.py: every juror/judge call is a real Hermes run

def
 
ask
(
prompt
,
 
provider
,
 
model
,
 
skills
=
None
,
 
timeout
=
120
):

 
cmd
 
=
 
[
binary
(),
 
"
--provider
"
,
 
provider
,
 
"
--model
"
,
 
model
]

 
if
 
skills
:
 
cmd
 
+=
 
[
"
--skills
"
,
 
skills
]

 
cmd
 
+=
 
[
"
-z
"
,
 
prompt
]
 
# -z = one-shot, final answer on stdout

 
return
 
subprocess
.
run
(
cmd
,
 
capture_output
=
True
,
 
text
=
True
,
 
timeout
=
timeout
).
stdout

# jurors.py: fan out one Hermes subagent per juror, in parallel

with
 
ThreadPoolExecutor
(
max_workers
=
len
(
roster
()))
 
as
 
pool
:

 
opinions
 
=
 
list
(
pool
.
map
(
lambda
 
c
:
 
ask_juror
(
*
c
),
 
enumerate
(
roster
())))

Enter fullscreen mode

Exit fullscreen mode

## How I Used Hermes Agent

Why Hermes at all: the model-agnostic core.Hermes lets you point at any provider and swap with a flag, no code change. Council is builton top of that one property: the jurors are different models, and Hermes is the only piece that makes "different models" cheap. The clearest proof is the third juror: it runslocallyvia Ollama while the other two arehostedon OpenRouter, and all three answer through the exact samehermes -zinterface (the model-agnostic diagram above). A hosted model and an on-device model, sitting on the same jury, no code change: that's model-agnosticism you can see. I genuinely didn't see another entry in this challenge exploit it; everyone picked one model and moved on. That's the whole bet.

Subagents: one real Hermes run per juror.Each juror is a genuine, isolated Hermes invocation on adifferentprovider+model (hermes -z --provider openrouter --model …for the two hosted jurors,--provider ollama-local …for the on-device one), fanned outin parallelso no model's reasoning anchors another's (the convene-flow diagram above). Hermes does the inference; my Python (jurors.pytohermes_run.py) is just the fan-out plumbing, and every juror in the output JSON is tagged"via": "hermes". The gotcha worth flagging: Hermes enforces a64K-context floor, which for the local model meant setting bothollama_num_ctxanda namedcustom_providersentry; without the named provider,--provider ollamasilently routed to the wrong base URL.setup_hermes.shencodes the working config so a judge can reproduce it in one command.

A true debate, not just a vote (round 2 is real Hermes work).This is the feature I'm proudest of. After round 1, if the jurors disagree, each one gets asecondHermes run that shows it the others' positions and lead reasons and asks it to hold or change its mind. Real jurors reconsider through the samehermes -zpath as round 1, so the debate is genuine extra agentic work, not a UI flourish; mock jurors reconsider deterministically so the offline demo stays reproducible. The judge then synthesizes the verdict from thedeliberatedopinions, so a juror that's talked round actually moves the outcome (the deliberation diagram above). It's gated on disagreement (a unanimous round 1 skips it) and toggled withCOUNCIL_DEBATE=0.

Why a skill, not a prompt, for judging.The foreman's verdict is itself a Hermes run (hermes -z --skills council) grounded inskills/council/SKILL.md, which isinstalled into Hermes(hermes skills listshows it). The weighting logic lives in a machine-readableweightsblock.

The judging brain is data, not a buried prompt.--learnand--reflectboth edit this block, and the installed Hermes copy is kept in sync.

After a string of security questions,--learnappended a rule to upweight the local model on that topic (and synced the installed Hermes copy) because it had caught issues the hosted models missed:

python run_council.py 
--learn
 
"Local Juror | security | 1.5"

Enter fullscreen mode

Exit fullscreen mode

On the next security question that juror's vote counts 1.5×, read straight back by the judge. Counterfactual: a static synthesis prompt can't get better; this does. (The before/after skill diff is indocs/hermes-proof/03-skill-learning.txt.)

Letting the agent propose its own learning, now on the web and grounded in evidence.python run_council.py --reflect(and the"Should the council reweight itself?"button in the UI) hands Hermes itsownmemory of past verdicts and asks it to propose one weight change, e.g. "the local juror has dissented on three database calls; upweight it." The key fix this round: the proposal isevidence-grounded, since Hermes is fed the actual dissent tally and any rule backed by fewer than two real dissents is rejected, so it can't just parrot the example baked into the skill. You thenApprove or Dismissit (the reflect-flow diagram above). That's the agentic loop done honestly: a single verdict has no ground truth, so the agent surfaces apatternand a human confirms it's signal, not overfitting (the exact tension this post closes on). (Offline, it falls back to a deterministic heuristic so it never breaks.)

Making learning survive a stateless deploy.On a hosted demo the filesystem is read-only, so an approved rule can't be written back toSKILL.md. Council handles this honestly: approved rules are stored in the browser'slocalStorageand re-sent with every/api/convenecall, where they're merged into the judge's weights for that request. Locally you get a persistentSKILL.md; on the web you get per-browser persistence, and either way the learning sticks.

Why memory.Each verdict is appended to a logand mirrored into Hermes' ownMEMORY.md, so I can askhermes -z "what did the council decide about auth?"and Hermes recalls it from its memory, not from my code (the memory-recall image above). Proof:docs/hermes-proof/04-memory-recall.txt.

The foreman reads the verdict aloud.The verdict card has a "the foreman reads the verdict" button (browser SpeechSynthesis, $0); Hermes also ships native TTS viahermes setup tts. On-theme and memorable: a jury foremanannouncingthe decision.

The build itself was agent-run.I kept amemory.mdthe coding agent read before each task and updated after (so context stayed cheap), committed every increment with Conventional Commits, and built the verdict UI with thefrontend-designskill, which is why the confidence dial and colour-coded juror chips read asdesigned, not default-template AI slop. The repo'sAGENTS.md+ commit history show the process, not just the result.

Why these models, and the concession.Two free OpenRouter models from different families (≥64K context, since Hermes rejects smaller at startup) plus a local Ollama juror. Two honest concessions: (1) free models are slower and three calls add latency (~10-20s/verdict); (2) the free tier isaggressivelyrate-limited, so I hit 429s constantly while building, and Council retries and, if a juror still won't answer, falls back (Hermes to direct API to deterministic stand-in) rather than crashing the verdict, which also means the demo runsfully offline at $0. For a once-a-decision tool, I'll take it. Cost: $0.

License.MIT. Fork it, add your own jurors.

## What I learned (and what's next)

* The disagreement is the product.A 2-1 split ismoreuseful than a confident single answer, so the clustering that decides "who actually disagreed" has to be right. A small local model once wrote a vague position ("to facilitate efficient integration…") whosereasonsclearly endorsed Postgres; the first version mis-filed it as a dissenter. The fix: when a juror's stated position is ambiguous, fall back to reading its reasons, and ignore options only mentioned in a comparison ("betterthanMongo" isn't a vote for Mongo). Now agreeing jurors cluster together, and the split count is honest.
* Grounded beats glib.Letting the agent propose its own weighting only works if the proposal is tied to real evidence; an ungrounded "reflect" just echoes whatever example is in the skill.
* Hermes' 64K-context floor caught a model that would've quietly underperformed.
* A council should deliberate, not just vote.The round-2 debate above was the turning point: letting jurors read each other and reconsider means a juror that's genuinely persuaded moves the verdict, and you watch the confidence dial climb as a 2-1 split becomes unanimous. A one-shot vote can't do that.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (15 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse