---
title: 'Claude Haiku 5.5 Pricing: The 100,000-Token Threshold | ImportStatic'
url: https://importstatic.com/ai/claude-haiku-5-5-pricing-threshold
site_name: tldr
content_file: tldr-claude-haiku-55-pricing-the-100000-token-threshold
fetched_at: '2026-10-08T12:48:04.087648'
original_url: https://importstatic.com/ai/claude-haiku-5-5-pricing-threshold
date: '2026-10-08'
published_date: '2026-10-08T00:10:00Z'
description: Claude Haiku 5.5 pricing has two tiers. One token past 100,000 and the same request costs five times more. What counts, and a Go calculator to check your own.
tags:
- tldr
---

Tested with Go 1.27.1 on darwin/arm64, standard library only; no API requests were sent

A request to Claude Haiku 5.5 with a 100,000-token prompt and 2,000 tokens of output costs $0.011. Add one token to the prompt and the same request costs $0.055. Nothing else changed; you crossed a line in the price list.

Anthropic released Haiku 5.5 on October 7, 2026, and as of October 8 it's available on the Claude API, Amazon Bedrock, Google Cloud, Microsoft Foundry and Claude Platform on AWS under the IDclaude-haiku-5-5(anthropic.claude-haiku-5-5on Bedrock). The headline is the price: $0.10 per million input tokens against $1 for Haiku 4.5. The catch is that the cheap rate is for "prompts up to 100,000 tokens", and the model takes prompts ten times that size. AHacker News discussion of the releasewent back and forth on whether agent workloads can stay under the line and didn't settle it. So we did the arithmetic with a small Go program. We had no API key in this run, so nothing below was sent to the model: the prices come from Anthropic's documentation and the costs are computed from them.

## Claude Haiku 5.5 pricing is two complete price lists

Thepricing pagegives Haiku 5.5 two rows, one "for prompts up to 100,000 tokens" and one "for prompts over 100,000 tokens". Per million tokens:

Up to 100,000

Over 100,000

Haiku 4.5

Input

$0.10

$0.50

$1.00

Output

$0.50

$2.50

$5.00

Cache read

$0.01

$0.05

$0.10

Cache write, 5 minutes

$0.125

$0.625

$1.25

Cache write, 1 hour

$0.20

$1.00

$2.00

Batch input / output

$0.05 / $0.25

$0.25 / $1.25

$0.50 / $2.50

Every rate in the second column is five times the first. That includes output, which is the part people miss: the length of what you send decides the price of what comes back.

This isn't a marginal bracket like income tax, where only the excess pays the higher rate. The row is chosen per prompt and applies to the whole request. It's also unique in the current lineup. For the other 1M-context models the same page says "A 900k-token request is billed at the same per-token rate as a 9k-token request", and it names Haiku 5.5 as the exception.

## What the docs say counts as the prompt, and what they leave out

"Prompt" is doing a lot of work in that table, and the documentation doesn't define it as a formula over theusagefields. Here's what it does say.

With prompt caching on, the input is split acrossinput_tokens,cache_creation_input_tokensandcache_read_input_tokens. Thecontext windows pageis blunt about cached tokens: "prompt caching changes what you pay for those tokens, not whether they count." So we treat the prompt as the sum of all three, which is the reading where a 100,000-token cached prefix plus a 50-token question lands in the expensive tier. That's our reading, not a quoted rule. If your bill depends on it, check a real invoice against a request you know the size of.

Two more things move the line.

Haiku 5.5 uses the newer tokenizer, and the migration guide says the same text "produces approximately 30% more tokens" than on Haiku 4.5. If you know your prompt sizes in Haiku 4.5 tokens, the threshold isn't 100,000 for you. It's about 76,900.

And the pre-flight check is approximate. Thetoken counting endpointis free and takes the same body as a message request, but the docs call its result an estimate that "might differ by a small amount". Don't route on<= 100000. Leave headroom.

Shell
Copy
curl
 https://api.anthropic.com/v1/messages/count_tokens
 \

 -H
 "x-api-key: 
$ANTHROPIC_API_KEY
"
 \

 -H
 "content-type: application/json"
 \

 -H
 "anthropic-version: 2023-06-01"
 \

 -d
 '{"model": "claude-haiku-5-5", "messages": [{"role": "user", "content": "..."}]}'

That's the documented request with the model swapped in; we didn't send it. Passclaude-haiku-5-5and not your old model, or you'll get the old tokenizer's count.

## One token over, priced in Go

The calculator is one function. It mirrors theusageobject, picks a tier from the prompt length and applies that tier to everything:

Go
Copy
type
 Usage
 struct
 {

	InputTokens 
int
 `json:"input_tokens"`

	CacheCreationInputTokens 
int
 `json:"cache_creation_input_tokens"`

	CacheReadInputTokens 
int
 `json:"cache_read_input_tokens"`

	OutputTokens 
int
 `json:"output_tokens"`

}

// Rates are US dollars per million tokens.

type
 Rates
 struct
 {

	Input, CacheWrite5m, CacheRead, Output 
float64

}

var
 (

	Haiku55Short 
=
 Rates
{Input: 
0.10
, CacheWrite5m: 
0.125
, CacheRead: 
0.01
, Output: 
0.50
}

	Haiku55Long 
=
 Rates
{Input: 
0.50
, CacheWrite5m: 
0.625
, CacheRead: 
0.05
, Output: 
2.50
}

	Haiku45 
=
 Rates
{Input: 
1.00
, CacheWrite5m: 
1.25
, CacheRead: 
0.10
, Output: 
5.00
}

)

const
 Haiku55Threshold
 =
 100_000

func
 (
u 
Usage
) 
PromptTokens
() 
int
 {

	return
 u.InputTokens 
+
 u.CacheCreationInputTokens 
+
 u.CacheReadInputTokens

}

func
 (
u 
Usage
) 
at
(
r
 Rates
) 
float64
 {

	return
 (
float64
(u.InputTokens)
*
r.Input 
+

		float64
(u.CacheCreationInputTokens)
*
r.CacheWrite5m 
+

		float64
(u.CacheReadInputTokens)
*
r.CacheRead 
+

		float64
(u.OutputTokens)
*
r.Output) 
/
 1
e
6

}

func
 Haiku55Cost
(
u
 Usage
) (
dollars
 float64
, 
long
 bool
) {

	if
 u.
PromptTokens
() 
>
 Haiku55Threshold {

		return
 u.
at
(Haiku55Long), 
true

	}

	return
 u.
at
(Haiku55Short), 
false

}

Feed it two requests that differ by one token, then one 150,000-token prompt against the same material in two halves (1,000 output tokens each):

Text
Copy
prompt 100000 + 2000 out $0.011000 long=false

prompt 100001 + 2000 out $0.055001 long=true

one request $0.0775

two requests $0.0160

The second pair is the practical one. Summarising a long document in two 75,000-token calls costs a fifth of doing it in one, and you can add a third call to merge the halves and still be far ahead. For extraction and classification over big inputs, which is what this model is sold for, chunking just became a pricing decision as well as a quality one.

## An agent loop crosses the line on turn 17

Is 100,000 tokens a lot? For a single classification call, it's enormous. For a tool-calling agent that appends every result to the conversation, it isn't.

We modelled a loop with prompt caching on: an 8,000-token prefix of system prompt and tool definitions, and each turn adding a 5,000-token tool result and a 500-token reply. Those sizes are made up to be plausible. This is a model of the billing, and your agent will have different numbers.

Text
Copy
turn 16: prompt 95500 $0.00184 long=false

turn 17: prompt 101000 $0.00946 long=true

append only $0.3267 (first long-tier turn: 17)

compact before 100k $0.0623 (first long-tier turn: 0, compactions: 2)

Turn 17 costs five times turn 16 for almost the same work, and every later turn stays in the expensive tier because the history only grows. Over 40 turns the append-only loop costs $0.33. The second line replaces the history with a 3,000-token summary whenever the next prompt would cross 100,000, pays for writing that summary, and comes to $0.06. Whether a summary is good enough for your task is a separate question that no price table answers.

There's a trap in the obvious fix. The API'sthreshold compaction, in beta and listed as supporting Haiku 5.5, summarises old turns on the server once the input reaches a trigger. The default trigger is 150,000 input tokens. On every other model that's a sensible default. On this one it means compaction switches on 50,000 tokens after the price went up. Set it yourself; the minimum is 50,000:

JSON
Copy
{

 "model"
: 
"claude-haiku-5-5"
,

 "max_tokens"
: 
4096
,

 "context_management"
: {

 "edits"
: [

 { 
"type"
: 
"compact_20260112"
, 
"trigger"
: { 
"type"
: 
"input_tokens"
, 
"value"
: 
80000
 } }

 ]

 },

 "messages"
: [{ 
"role"
: 
"user"
, 
"content"
: 
"..."
 }]

}

That body is adapted from the documented example and goes with theanthropic-beta: compact-2026-01-12header. We didn't send it either.

Don't trim the history by hand without reading themigration guidefirst. Haiku 5.5 thinks by default, and a request that sends a thinking block back after earlier messages changed can come back as a 400 error (the guide says which accounts get the check). Its instruction is to keep conversations append-only, which is exactly what a hand-rolled "drop the oldest tool results" loop doesn't do.

## It's still cheaper than Haiku 4.5 on both sides

None of this makes Haiku 5.5 a bad deal. The long tier is half of Haiku 4.5's per-token price, and a quarter of Sonnet 5.5's $2 input rate.

The tokenizer eats into that, though. Pricing the same text on both models, with Haiku 5.5's counts inflated by the documented 30%:

Text
Copy
threshold in Haiku 4.5 tokens: 76923

4.5: 10000 in $0.0150 | 5.5: 13000 in $0.0019 long=false | saving 87%

4.5: 50000 in $0.0550 | 5.5: 65000 in $0.0072 long=false | saving 87%

4.5: 76000 in $0.0810 | 5.5: 98800 in $0.0105 long=false | saving 87%

4.5: 78000 in $0.0830 | 5.5: 101400 in $0.0539 long=true | saving 35%

4.5: 150000 in $0.1550 | 5.5: 195000 in $0.1008 long=true | saving 35%

So: 87% cheaper for the same text under the line, 35% cheaper above it. Anthropic's announcement says prompts up to 100,000 tokens "make up around 90% of requests to our previous Haiku model". That's a share of requests, and long requests carry more tokens each, so the share of your spend that lands in the long tier can be a good deal higher than one in ten.

The switch isn't only a price change. Manualbudget_tokensthinking, non-defaulttemperature, and assistant prefill all return 400 errors on Haiku 5.5, much like the changes we listed forClaude Sonnet 5.5. And if your long prompts are long because of tool definitions,measure those first; they're in every request.

Our advice is short. Put a budget of 90,000 counted tokens on anything you send to Haiku 5.5, set the compaction trigger below it, and logusageper request so you can see how many calls go over. If a workload can't fit, split it. If it can't be split, run it anyway, and know that it's the 35% discount you're getting.

## Common questions

### How much does Claude Haiku 5.5 cost?

As of October 8, 2026, prompts up to 100,000 tokens cost $0.10 per million input tokens and $0.50 per million output tokens. Prompts over 100,000 tokens cost $0.50 and $2.50. Cache reads are $0.01 or $0.05, and the Batch API halves input and output prices in both tiers.

### Does the higher Claude Haiku 5.5 price apply only to the tokens above 100,000?

No. Anthropic publishes two complete price lists chosen by prompt length, so a prompt over 100,000 tokens pays the higher rate on its input, cache writes, cache reads and output. In our calculation a request with 2,000 output tokens goes from $0.011 to $0.055 when the prompt grows from 100,000 to 100,001 tokens.

### Is Claude Haiku 5.5 cheaper than Haiku 4.5?

Yes, in both tiers. Per token it is 90% cheaper up to 100,000 prompt tokens and 50% cheaper above. Because Haiku 5.5 counts roughly 30% more tokens for the same text, the saving for the same text works out to about 87% and 35%.

### What is the model ID for Claude Haiku 5.5?

claude-haiku-5-5 on the Claude API, Google Cloud, Microsoft Foundry and Claude Platform on AWS, and anthropic.claude-haiku-5-5 on Amazon Bedrock. It is a fixed ID with no date suffix.

Sources checked for this article (7)

1. Anthropic announcement: Claude Haiku 5.5, October 7, 2026– Launch date, platforms, the two-tier price table, the statement that prompts up to 100,000 tokens were about 90% of Haiku 4.5 requests
2. Claude Platform pricing, read 2026-10-08– Every price in the article, both Haiku 5.5 tiers, batch prices, the long context pricing paragraph, Sonnet 5.5 and Haiku 4.5 rows
3. Claude Haiku 5.5 model page– Model IDs, 1M context window, 128K output, release date, default effort, tokenizer note
4. Claude Haiku 5.5 migration guide– About 30% more tokens for the same text, the breaking changes, the append-only rule for conversations that send thinking blocks back
5. Context windows– Input split across three usage fields that all count, cached prefixes still count, Haiku 5.5 as the exception to standard long-context pricing
6. Compaction at a token threshold– Haiku 5.5 support, beta header, default trigger of 150,000 input tokens, minimum of 50,000, usage.iterations
7. Token counting– count_tokens request shape, free to use, the count is an estimate

* AI agents
* Claude API pricing
* Claude Haiku 5.5
* context compaction
* Go
* prompt caching
* token counting

ImportStatic articles are researched and drafted with AI assistance, checked against primary sources, and every code sample is compiled and run before publishing. Found a mistake?Here is how corrections work.

## Keep reading

1. AIOct 1, 202610 min read### OpenAI DevDay 2026, read from the API changelogOpenAI DevDay 2026 for API users: gpt-6.1-sol prices and limits, the Ultrafast tier at 6x Astra's rates, computer use in the Agents API, and a Go cost check.
2. AIOct 1, 202610 min read### Build an MCP server in Go with the official SDKWrite an MCP server in Go with the official go-sdk: a typed tool, schema validation, tool errors, in-memory tests, and stdio or HTTP transport. Tested code.
3. AIOct 7, 202611 min read### A Rust MCP server ignores misspelled arguments unless you askBuild a Rust MCP server with rmcp 3.5.1: one typed tool, strict arguments, errors a model can read, in-memory tests, and both protocol versions over stdio.
4. AIOct 2, 202612 min read### Five things that break when you switch to Claude Sonnet 5.5Claude Sonnet 5.5 costs the same as Sonnet 5, but five request settings now return 400 errors. The exact error texts, the fixes in Go, and a preflight check.