---
title: I built a 200 line AI router in TypeScript. My monthly bill dropped 41%. - DEV Community
url: https://dev.to/thegdsks/i-built-a-200-line-ai-router-in-typescript-my-monthly-bill-dropped-41-23ok
site_name: devto
content_file: devto-i-built-a-200-line-ai-router-in-typescript-my-mont
fetched_at: '2026-05-12T19:39:14.784245'
original_url: https://dev.to/thegdsks/i-built-a-200-line-ai-router-in-typescript-my-monthly-bill-dropped-41-23ok
author: GDS K S
date: '2026-05-07'
description: I track my own AI spend across three projects. In March, the line item that grew fastest was not... Tagged with typescript, ai, webdev, tutorial.
tags: '#typescript, #ai, #webdev, #tutorial'
---

Uses regex to bypass wrapper context bloat

I track my own AI spend across three projects. In March, the line item that grew fastest was not Claude or GPT calls. It was my Cursor seat plus my Copilot seat plus the Anthropic API I was hitting from a personal CLI. Three subscriptions, three meters, and the same Opus tokens billed twice because Cursor was sending the same context to its own backend that I was already passing through to Anthropic directly.

The wrappers do not advertise this. The router code is not their product. The product is the convenience of not thinking about which model handles which prompt. You pay the orchestration tax in margin baked into the seat price.

I got tired of paying it. So I wrote the router. It is 200 lines of TypeScript. My April bill came in 41% under March on roughly the same volume of work.

## TL;DR

Model

Input $/M tokens

Output $/M tokens

Best for

Haiku 4.5

0.80

4.00

Lookups, classification, typo fixes

Sonnet 4.6

3.00

15.00

Default coding, refactors, code review

Opus 4.7

5.00

25.00

Multi step planning, architecture

GPT-5 mini

0.50

2.00

Cheap classification, embeddings prep

The 41% saving came from one thing: stopping Sonnet from handling tasks that Haiku could finish in a tenth of the cost. Most coding queries are lookups dressed up as questions. Route by intent, not by habit.

## 1. The orchestration tax is real

Every wrapper makes the same trade. They pick a model for you, they prepend a system prompt you cannot edit, and they hold a context window you cannot inspect. In return, you do not have to think.

The cost of not thinking shows up two ways:

1. The wrapper calls the most expensive model that fits its SLA, because that is what makes the demo look good
2. The wrapper bills you for context it sent on your behalf, including its own system prompt and tool definitions

I logged 30 days of Cursor usage against the Anthropic dashboard. Cursor was sending an average of 8,400 input tokens per chat turn. My direct API calls for the same chats averaged 1,900. The 6,500 token delta is Cursor's frame, plus indexing context, plus its agent scaffolding. Useful, but not free.

When you build the router yourself, you choose what to send. That is the whole game.

## 2. The 200 line router

Here is the file. Drop it in a project, give it your API keys, and it picks a model per request based on rules you control.

// router.ts

import
 
Anthropic
 
from
 
"
@anthropic-ai/sdk
"
;

import
 
OpenAI
 
from
 
"
openai
"
;

type
 
Intent
 
=
 
"
trivial
"
 
|
 
"
code
"
 
|
 
"
plan
"
 
|
 
"
embed
"
;

interface
 
RouteRule
 
{

 
match
:
 
(
prompt
:
 
string
)
 
=>
 
boolean
;

 
intent
:
 
Intent
;

}

interface
 
ModelConfig
 
{

 
provider
:
 
"
anthropic
"
 
|
 
"
openai
"
;

 
model
:
 
string
;

 
maxTokens
:
 
number
;

}

const
 
ROUTES
:
 
Record
<
Intent
,
 
ModelConfig
>
 
=
 
{

 
trivial
:
 
{
 
provider
:
 
"
anthropic
"
,
 
model
:
 
"
claude-haiku-4-5-20251001
"
,
 
maxTokens
:
 
1024
 
},

 
code
:
 
{
 
provider
:
 
"
anthropic
"
,
 
model
:
 
"
claude-sonnet-4-6
"
,
 
maxTokens
:
 
4096
 
},

 
plan
:
 
{
 
provider
:
 
"
anthropic
"
,
 
model
:
 
"
claude-opus-4-7
"
,
 
maxTokens
:
 
8192
 
},

 
embed
:
 
{
 
provider
:
 
"
openai
"
,
 
model
:
 
"
gpt-5-mini
"
,
 
maxTokens
:
 
512
 
},

};

const
 
RULES
:
 
RouteRule
[]
 
=
 
[

 
{
 
intent
:
 
"
trivial
"
,
 
match
:
 
(
p
)
 
=>
 
p
.
length
 
<
 
200
 
&&
 
/
\?
$/
.
test
(
p
.
trim
())
 
},

 
{
 
intent
:
 
"
trivial
"
,
 
match
:
 
(
p
)
 
=>
 
/^
(
what is|define|fix typo|rename
)
/i
.
test
(
p
)
 
},

 
{
 
intent
:
 
"
plan
"
,
 
match
:
 
(
p
)
 
=>
 
/
(
refactor|design|architect|migrate|plan
)
/i
.
test
(
p
)
 
},

 
{
 
intent
:
 
"
code
"
,
 
match
:
 
(
p
)
 
=>
 
/
(
``
`

{
%
 
endraw
 
%
}

|
function
 
|
class
 
|
const
 
|
let
 
)
/
i
.
test
(
p
)
 
},

 
{
 
intent
:
 
"
embed
"
,
 
match
:
 
(
p
)
 
=>
 
p
.
startsWith
(
"
CLASSIFY:
"
)
 
},

];

function
 
pickIntent
(
prompt
:
 
string
):
 
Intent
 
{

 
for 
(
const
 
rule
 
of
 
RULES
)
 
{

 
if 
(
rule
.
match
(
prompt
))
 
return
 
rule
.
intent
;

 
}

 
return
 
"
code
"
;

}

const
 
anthropic
 
=
 
new
 
Anthropic
({
 
apiKey
:
 
process
.
env
.
ANTHROPIC_API_KEY
 
});

const
 
openai
 
=
 
new
 
OpenAI
({
 
apiKey
:
 
process
.
env
.
OPENAI_API_KEY
 
});

export
 
interface
 
RouteResult
 
{

 
text
:
 
string
;

 
model
:
 
string
;

 
inputTokens
:
 
number
;

 
outputTokens
:
 
number
;

 
costUsd
:
 
number
;

}

const
 
PRICING
:
 
Record
<
string
,
 
{
 
in
:
 
number
;
 
out
:
 
number
 
}
>
 
=
 
{

 
"
claude-haiku-4-5-20251001
"
:
 
{
 
in
:
 
0.8
,
 
out
:
 
4
 
},

 
"
claude-sonnet-4-6
"
:
 
{
 
in
:
 
3
,
 
out
:
 
15
 
},

 
"
claude-opus-4-7
"
:
 
{
 
in
:
 
5
,
 
out
:
 
25
 
},

 
"
gpt-5-mini
"
:
 
{
 
in
:
 
0.5
,
 
out
:
 
2
 
},

};

function
 
priceCall
(
model
:
 
string
,
 
inTok
:
 
number
,
 
outTok
:
 
number
):
 
number
 
{

 
const
 
p
 
=
 
PRICING
[
model
];

 
if 
(
!
p
)
 
return
 
0
;

 
return 
(
inTok
 
*
 
p
.
in
 
+
 
outTok
 
*
 
p
.
out
)
 
/
 
1
_000_000
;

}

export
 
async
 
function
 
route
(
prompt
:
 
string
):
 
Promise
<
RouteResult
>
 
{

 
const
 
intent
 
=
 
pickIntent
(
prompt
);

 
const
 
cfg
 
=
 
ROUTES
[
intent
];

 
if 
(
cfg
.
provider
 
===
 
"
anthropic
"
)
 
{

 
const
 
r
 
=
 
await
 
anthropic
.
messages
.
create
({

 
model
:
 
cfg
.
model
,

 
max_tokens
:
 
cfg
.
maxTokens
,

 
messages
:
 
[{
 
role
:
 
"
user
"
,
 
content
:
 
prompt
 
}],

 
});

 
const
 
text
 
=
 
r
.
content

 
.
filter
((
b
)
 
=>
 
b
.
type
 
===
 
"
text
"
)

 
.
map
((
b
)
 
=>
 
(
b
 
as
 
{
 
text
:
 
string
 
}).
text
)

 
.
join
(
""
);

 
return
 
{

 
text
,

 
model
:
 
cfg
.
model
,

 
inputTokens
:
 
r
.
usage
.
input_tokens
,

 
outputTokens
:
 
r
.
usage
.
output_tokens
,

 
costUsd
:
 
priceCall
(
cfg
.
model
,
 
r
.
usage
.
input_tokens
,
 
r
.
usage
.
output_tokens
),

 
};

 
}

 
const
 
r
 
=
 
await
 
openai
.
chat
.
completions
.
create
({

 
model
:
 
cfg
.
model
,

 
max_tokens
:
 
cfg
.
maxTokens
,

 
messages
:
 
[{
 
role
:
 
"
user
"
,
 
content
:
 
prompt
 
}],

 
});

 
const
 
usage
 
=
 
r
.
usage
 
??
 
{
 
prompt_tokens
:
 
0
,
 
completion_tokens
:
 
0
 
};

 
return
 
{

 
text
:
 
r
.
choices
[
0
]?.
message
?.
content
 
??
 
""
,

 
model
:
 
cfg
.
model
,

 
inputTokens
:
 
usage
.
prompt_tokens
,

 
outputTokens
:
 
usage
.
completion_tokens
,

 
costUsd
:
 
priceCall
(
cfg
.
model
,
 
usage
.
prompt_tokens
,
 
usage
.
completion_tokens
),

 
};

}

{
%
 
raw
 
%
}

Enter fullscreen mode

Exit fullscreen mode

That is it. Two providers, four intents, five rules, and a cost calculator. Use it like this:

typescript
import { route } from "./router";

const out = await route("rename this function from getUser to fetchUser");
console.log(out.model, out.costUsd.toFixed(5));
// claude-haiku-4-5-20251001 0.00012

Enter fullscreen mode

Exit fullscreen mode

The rules are deliberately dumb. Length plus regex covers maybe 70% of routing decisions correctly. For the other 30%, override with a prefix:

typescript
await route("[force:opus] design a permissions model for ...");

Enter fullscreen mode

Exit fullscreen mode

Add a one liner topickIntentto read the prefix. I left it out to keep the example tight.

## 3. Routing rules that actually work

The naive approach is to send a tiny classifier call to a cheap model and have it pick the route. That sounds smart and costs more than it saves, because every request now eats two API calls. The cost of pickIntent must be zero.

Five regex rules cover most of my workload:

* Short and ends in a question mark: trivial
* Starts with "what is", "define", "fix typo", "rename": trivial
* Contains "refactor", "design", "architect", "migrate", "plan": plan
* Contains code fence or function keyword: code
* Starts with "CLASSIFY:" prefix: embed (cheap classifier)

Default to code. A wrong route from trivial to code costs maybe 4x more on that one request. A wrong route from code to opus costs 1.6x. Neither is a disaster. The bug to avoid is sending Haiku a multi step plan it cannot hold context for, which means default conservatively.

I also log every miss. After two weeks I had a small CSV of "this prompt routed to X but should have been Y". I added two regex rules and the miss rate dropped from 8% to under 2%.

## 4. The 41% number, broken down

March bill, no router:

Source

Calls

Spend

Cursor seat

n/a

$20

Copilot seat

n/a

$10

Anthropic direct

4,200

$87

OpenAI direct

800

$14

Total

$131

April bill, with router (cancelled Cursor, kept Copilot for IDE inline only):

Source

Calls

Spend

Cursor seat

n/a

$0

Copilot seat

n/a

$10

Anthropic via router

5,100

$54

OpenAI via router

1,400

$13

Total

$77

That is 41% lower on 30% more total calls. The router shifted 62% of calls onto Haiku, which was eating workloads Sonnet had been handling. Average cost per call dropped from $0.024 to $0.013.

The Cursor cancel did the headline saving. The router did the smaller, repeating, compounding saving. Both come from the same idea: the wrapper is hiding decisions you could make better yourself.

## 5. What this does not do

This is not an agent framework. It does not stream. It does not retry. It does not cache. It does not handle rate limits. It does not do tool use. It does not know about your codebase.

Adding any of those takes work. Streaming is two changes. Caching with the Anthropic prompt cache is one extra header on each call. Retries with exponential backoff is 20 lines. Tool use requires schema plumbing you would write anyway.

If you need all of that, use a real framework. If you want to stop paying the orchestration tax on 80% of your calls, the 200 lines above will do it. Add the rest as you actually hit each problem.

## Conclusion

Wrappers exist because routing AI calls is annoying. It is also the highest leverage thing you can own in your own code. The 200 lines above are not a moat. They are a Tuesday afternoon. The reason to write them is that you cannot improve a bill you cannot see.

What is your current ratio of cheap model to expensive model calls? If you do not know, that is the first thing to fix. Wire up cost logging before you wire up the router. The numbers will surprise you.

GDS K S·thegdsks.com· buildingGlincker· follow on X@thegdsks

The orchestration tax is the part of the AI bill that does not show up on the pricing page.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse