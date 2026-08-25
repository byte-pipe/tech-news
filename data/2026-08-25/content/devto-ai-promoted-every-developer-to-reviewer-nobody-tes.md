---
title: AI promoted every developer to reviewer. Nobody tested the reviewer. - DEV Community
url: https://dev.to/heinrichneb/ai-promoted-every-developer-to-reviewer-nobody-tested-the-reviewer-m4h
site_name: devto
content_file: devto-ai-promoted-every-developer-to-reviewer-nobody-tes
fetched_at: '2026-08-25T11:24:51.707508'
original_url: https://dev.to/heinrichneb/ai-promoted-every-developer-to-reviewer-nobody-tested-the-reviewer-m4h
author: Heinrich Neb
date: '2026-08-24'
description: I wanted to disagree with 'AI made me a worse reviewer' from Michael Amachree (@dev_michael) .... Tagged with ai, productivity, testing, discuss.
tags: '#discuss, #ai, #productivity, #testing'
---

89 percent of guardrails never tested for failure

I wanted to disagree with 'AI made me a worse reviewer' from Michael Amachree (@dev_michael) . Instead I counted 204 of my own guards — and 89 % of them have never been asked to prove they can fail.

Michael wrote something that I couldn't put down: AI didn't make me a worse coder, it made me a worse reviewer. Here is the number, and it's worse than his thesis: of the 204 automated checks in my repositories that draw a conclusion, only 22 can prove they are able to fail. That's 11 %. The other 89 % have never once been shown a known-bad input. They are green. Whether they are green because everything is fine, or green because they are incapable of finding anything - I could not have told you last week. And I'm the person who wrote them.

## What I actually counted

First the definition, so you can reject it or reuse it.

Aconclusion-bearing guardis any test that reads source code, config, or system state and asserts a claim about it. Not "does this function return 4" - but "no workflow downloads its cache over the network", "every page passes the same quarter filter", "this feature flag matches the deployed spec". The tests that stand in for a human reviewer.

Anegative controlis a probe that feeds that guard a known-bad input and asserts it gets rejectedfor the expected reason. Our convention marks themKONTROLLE:in the test name.

Counting is mechanical: 204 guard files across three repositories, 22 with at least one control probe, 54 probes total. The counter is a proxy - marker-based, so unmarked controls and false-positive guard files put the true number at plus or minus a few points. The shape survives any correction:most of my reviewers have never been reviewed.

## Three green-and-blind checks, one ordinary week

This isn't theoretical. All three of these happened to me in the last seven days, in production tooling.

The deploy gate that died of its own medicine.A pipeline step existed specifically to catch a silent failure mode - a missing tool falling back to an empty result. It callednode -eto parse a health response. The deploy runner has no Node. Six consecutive deployments failed with exit 127 - the checkagainstmissing tools failedon a missing tool, and nothing shipped for six hours. The step had been green in review because nobody had ever run it where it actually runs.

The harvester that threw away its own work.An autonomous job collected data from public repositories and judged each run by exit code. One run wrote seven perfectly good records, then hit a non-fatal warning and exited non-zero. The machine booked its own completed work as "failed, retry later" - becauseinterrupted-with-partial-resultshad no representation, only success and failure. We caught it because the result file was sitting on disk right next to the exit code that denied its existence.

The pattern that matched the wrong 500.An error classifier looked for server errors with the pattern50[024]- anywhere in the output. It matched the "500" inside"4258 of 5000 quota points remaining"and classified a successful run as a server failure. Every field it read was real. It was answering a different question than the one asked.

Three different systems. One shape:the check watched a messenger - an exit code, a pattern, a status - while the artifact that mattered told a different story.

## What this has to do with AI making you a worse reviewer

Here's where I think Michael's post lands harder than he says.

AI moved my job. I used to spend most of my day producing artifacts and a little of it verifying them. Now an agent produces most of the artifacts, and my jobisverification. Which means my real codebase - the one my judgment actually ships through - is those 204 guards.

And that codebase is held to a standard I would reject in application code. No test coverage (11 %). No review of the reviewer. Green as the default state, silence booked as success.

When Michael says AI made him a worse reviewer, I'd sharpen it:AI promoted us all to reviewers, and none of us tested the reviewer.The model isn't the weak link. The unfalsifiable green checkmark is.

## The rule that survived the week

Everything above collapses into one sentence we now apply mechanically:

Judge the artifact, not the messenger.

Exit codes are messengers. Summaries are messengers. The agent's own "done" is a messenger. Green badges are messengers. The artifact is the diff, the file on disk, the served response body, the row in the database. When a messenger and an artifact disagree, the artifact is right - and a check that only ever reads messengers should be treated as unverified, however green it is.

The corollary for guards:a green zero is the most dangerous answer a check can give."Found no violations" and "is incapable of finding violations" produce identical output. Only a negative control separates them.

## Count your own ratio (60 seconds)

This is the part you can use without believing me. Drop this in your repo root - it counts test files that read source or state, and how many carry a marked negative control (adjust the marker to your convention):

// count-controls.mjs — node count-controls.mjs

import
 
{
 
readFileSync
,
 
readdirSync
,
 
statSync
 
}
 
from
 
"
node:fs
"
;

import
 
{
 
join
 
}
 
from
 
"
node:path
"
;

const
 
files
 
=
 
[];

(
function
 
walk
(
d
)
 
{

 
for 
(
const
 
n
 
of
 
readdirSync
(
d
))
 
{

 
if 
(
n
 
===
 
"
node_modules
"
 
||
 
n
 
===
 
"
.git
"
 
||
 
n
 
===
 
"
dist
"
)
 
continue
;

 
const
 
p
 
=
 
join
(
d
,
 
n
);

 
statSync
(
p
).
isDirectory
()
 
?
 
walk
(
p
)
 
:
 
/
\.
test
\.(
t|j
)
sx
?
$/
.
test
(
n
)
 
&&
 
files
.
push
(
p
);

 
}

})(
"
.
"
);

let
 
guards
 
=
 
0
,
 
withControl
 
=
 
0
,
 
probes
 
=
 
0
;

for 
(
const
 
f
 
of
 
files
)
 
{

 
const
 
t
 
=
 
readFileSync
(
f
,
 
"
utf8
"
);

 
if 
(
!
/readFileSync|readdirSync|execSync/
.
test
(
t
))
 
continue
;
 
// "reads state" proxy

 
guards
++
;

 
const
 
n
 
=
 
(
t
.
match
(
/KONTROLLE|negative.control|can.
?
not.
?
find/gi
)
 
??
 
[]).
length
;

 
if 
(
n
)
 
withControl
++
;

 
probes
 
+=
 
n
;

}

console
.
log
(
`
${
guards
}
 conclusion-bearing guard files · 
${
withControl
}
 with a negative control (
${
guards
 
?
 
Math
.
round
(
100
 
*
 
withControl
 
/
 
guards
)
 
:
 
0
}
 %) · 
${
probes
}
 probes`
);

Enter fullscreen mode

Exit fullscreen mode

If your number is above 30 %, I'd genuinely like to know how you got there - that's the discussion I'm hoping for below.

## Where I was the punchline, twice, while writing this

Rule 2 of writing these posts is correcting yourself unprompted, so:

While building the feature this article's data comes from, my equivalence test failed byexactly0.25 - and the bug was inmy test, not the code: min-max spreading turns a column of zeros into a column of 0.5s and adds a constant. I had built a probe that answered a different question than the one asked, in the middle of measuring exactly that failure class.

And one push in that same hour went out with a red test - becausenpm test | grepreplaces the test's exit code with grep's. My pipeline read a messenger. The artifact - the failing test - sat right there.

The person telling you to test your reviewers failed to test his reviewer, twice, in one evening. That's not irony. That's the base rate, and it's why conventions beat discipline.

## What this does not prove

One developer, three repositories, one week - this is a case series, not a sample. The 11 % is marker-based and approximate. And I have not shown that raising falsifiability coverage improves outcomes downstream; I've shown that at 11 % I couldn't distinguish my working guards from my decorative ones. Whether the number that matters is 30 % or 80 %, I don't know yet - we're raising ours and measuring as we go.

There's also a fair objection: negative controls are themselves tests that can rot. True. But a control that rots failsloudlythe next time the guard changes - that's the asymmetry that makes them worth writing.

So: what's your ratio? And more interesting - what's the greenest check in your pipeline that you now suspect has never been able to fail?

I buildcachly— memory for AI coding assistants, over MCP. ChatGPT and Claude remember your conversations. cachly remembersyour system: the bug you fixed, why you chose Postgres, the deploy step that always breaks — and which earlier decision it contradicts. Every assistant you use reads the same memory, and every lesson carries the name of whoever learned it — so nobody has to learn it twice.

Free tier, hosted in the EU:cachly.dev

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (22 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse