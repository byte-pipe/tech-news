---
title: Building with Claude Sonnet 5.5 / claude.dev Blog
url: https://claude.dev/blog/building-with-claude-sonnet-5-5
site_name: tldr
content_file: tldr-building-with-claude-sonnet-55-claudedev-blog
fetched_at: '2026-09-28T23:42:05.595868'
original_url: https://claude.dev/blog/building-with-claude-sonnet-5-5
author: Addy Osmani
date: '2026-09-28'
published_date: '2026-09-28'
description: When to choose Sonnet over Opus, what it costs, and how to tune it.
tags:
- tldr
---

Playbooks

# Building with Claude Sonnet 5.5

When to choose Sonnet over Opus, what it costs, and how to tune it.

AUTHOR
Addy Osmani
PUBLISHED
Sep 28, 2026
READING TIME
9
 min

Claude Sonnet 5.5 is our second model in the Claude 5.5 family after Opus 5.5. It's a clear upgrade over Sonnet 5 and is smarter, more efficient and 30% faster. The per-token price is unchanged and because Sonnet 5.5 typically needs far fewer tokens to do the same work, it costs up to 30% less for most work.

Play video
VIDEO
Pause
Lance Martin's code-to-painting demo: each model writes code that repaints the same photograph. From left: the photograph, Claude Sonnet 5, Claude Sonnet 5.5 and Claude Opus 5.5.

This guide is about building with the model. To try it, run this request as written:

CODE
Python
Copy
import
 anthropic

client = anthropic.Anthropic()

response = client.messages.create(
 model=
"claude-sonnet-5-5"
,
 max_tokens=
4096
,
 messages=[
 {
 
"role"
: 
"user"
,
 
"content"
: 
"Analyze the trade-offs between microservices and monolithic architectures"
,
 }
 ],
 output_config={
"effort"
: 
"medium"
},
)

for
 block 
in
 response.content:
 
if
 block.
type
 == 
"text"
:
 
print
(block.text)

The loop reads each block by type because Sonnet 5.5 thinks by default, so a response can begin with athinkingblock, and code that readscontent[0].textbreaks.

## CHOOSING BETWEEN SONNET 5.5 AND OPUS 5.5

In the Claude 5.5 family, Opus 5.5 is built for complex work requiring careful judgment. Use Sonnet 5.5 for well-scoped everyday tasks like fixing bugs and quickly iterating on features. It also creates polished documents, slides and spreadsheets, and it has a strong eye for design. Its speed makes it well suited to fast iteration. Claude Haiku 5.5 will join the family in the coming weeks for high-volume, low-latency workflows.

Your workload
Start with
Well-scoped everyday coding: fixing bugs, quickly iterating on features, verifying against requirements
Sonnet 5.5
High-volume everyday development
Sonnet 5.5
Polished documents, slides and spreadsheets, such as one-pagers, diagrams, summary slides, document edits and spreadsheet cleanup, where an eye for design helps
Sonnet 5.5
Well-defined agent tasks you run repeatedly: investigation, review, drafting
Sonnet 5.5
Complex work requiring careful judgment, including long-horizon agentic coding and knowledge work
Opus 5.5
The hardest problems, where you need the most intelligence
Opus 5.5

"In Epic's early testing, Claude Sonnet 5.5 cleared the same quality bar you'd expect from a higher-tier model, holding up on a system design audit and a data-flow review. The new model managed tens of thousands of lines of code for gameplay system architecture, kept responses snappy, handled multi-hour tasks, and delivered with less prescriptive prompting." (Daniel Vogel, COO, Epic Games)

Sonnet 5.5 fits best when the task has a clear spec and a way to check the result. As theprompting guideputs it, "for the hardest long-horizon work, an Opus model is the better choice."

## PRICING

Per million tokens
Sonnet 5.5
Opus 5.5
Input
$2
$4
Output
$10
$20
Cache write, 5 minutes
$2.50
$5
Cache write, 1 hour
$4
$8
Cache read
$0.20
$0.20

All Sonnet 5.5 prices, including batch processing and prompt caching, match Sonnet 5's, so swapping the model ID doesn't change your per-token bill. US-only inference (inference_geo: "us") costs 1.1 times the standard price.

While the per-token price doesn't change, the overall bill will change because, as previously mentioned, Sonnet 5.5 typically uses fewer tokens per task than Sonnet 5.

Note that surfaces can ship with different default efforts for Sonnet, such as high on Claude Platform and medium in Claude Code.

Sonnet 5.5 uses the high-resolution image tier, up to 2576 pixels on the long edge, and a 2000×1500 image costs about 2.5 times as many tokens as on Sonnet 4.6, Sonnet 4.5 or Haiku 4.5. If you don't need the detail, downscale before you send.

## MODEL DETAILS

Detail
Sonnet 5.5
Model ID
claude-sonnet-5-5
 on the Claude API, Claude Platform on AWS, Google Cloud and Microsoft Foundry; 
anthropic.claude-sonnet-5-5
 on Amazon Bedrock
Context window
1M tokens, native, no beta header
Max output
128k tokens; up to 300k on the Message Batches API with the 
output-300k-2026-03-24
 beta header
Knowledge cutoff
June 2026
Thinking
On by default (adaptive thinking); 
between_tools
 turns off upfront thinking
Effort levels
low
, 
medium
, 
high
, 
xhigh
, 
max
Default effort
high
 on the Claude API; 
medium
 in Claude Code
Tokenizer
Same as Sonnet 5
Minimum cacheable prompt
512 tokens (1,024 on Sonnet 5)
Rate limits
Separate from Sonnet 5, with the same default tier values
Priority Tier
Available on the Claude API
Data retention
Available with zero data retention for eligible customers

The Claude API defaults tohighso you start from strong results. Start there, evaluate, and then pick the effort level your workload needs.

## MIGRATING FROM SONNET 5

Thinking is on by default. If you ran Sonnet 5 with thinking off, you can usebetween_toolsto turn off upfront thinking. Step 1 below shows how.

Change the model ID toclaude-sonnet-5-5, then work through five breaking changes and one change to the response shape. TheSonnet 5.5 migration guidecovers each one in full.

Claude Code can also do the migration for you. Run/claude-api migrate this project to claude-sonnet-5-5to invoke the bundledClaude API skill, which applies the model ID swap and the breaking parameter changes across your code base.

### 1. Turn off upfront thinking with between_tools

On Sonnet 5.5, a request with nothinkingfield runs with adaptive thinking, andthinking: {"type": "disabled"}returns a 400 error. Send the newbetween_toolssetting instead. Withbetween_tools, thinking only happens between tool calls, and total response time is the same or faster.

CODE
Python
Copy
# Before: Claude Sonnet 5

client.messages.create(
 model=
"claude-sonnet-5"
,
 max_tokens=
16000
,
 thinking={
"type"
: 
"disabled"
},
 output_config={
"effort"
: 
"xhigh"
},
 messages=[{
"role"
: 
"user"
, 
"content"
: 
"..."
}],
)

# After: Claude Sonnet 5.5

client.messages.create(
 model=
"claude-sonnet-5-5"
,
 max_tokens=
16000
,
 thinking={
"type"
: 
"between_tools"
},
 output_config={
"effort"
: 
"high"
},
 messages=[{
"role"
: 
"user"
, 
"content"
: 
"..."
}],
)

The example also drops effort fromxhightohigh, becausebetween_toolshas these limits:

* between_toolsworks atlow,mediumandhigheffort. Atxhighormaxit returns a 400 error; to run there, use adaptive thinking.
* It takes no other field. Sendingdisplay,budget_tokensorblock_bindingwith it returns a 400 error.
* Withbetween_tools, effort can't change mid-conversation. To vary effort per turn, use adaptive thinking.
* The short progress updates the model writes between tool calls still come back asthinkingblocks, with summary text. Read content blocks by type, and pass these blocks back unchanged with the rest of the assistant turn. Without tools, the response contains only text.
* It works on every platform that offers Sonnet 5.5, with no beta header. If your SDK version doesn't definebetween_tools, update it.

If you turn upfront thinking off withbetween_tools, use adaptive thinking instead for requests without tools that need a few steps of working out.

### 2. Replace forced tool_choice with auto plus strict tools

tool_choiceof typeanyortoolreturns a 400 error, including on the token counting endpoint. Sendauto, mark the toolstrict: trueso its input matches the schema, and say in the prompt when to use it:

CODE
Python
Copy
weather_tool = {
 
"name"
: 
"get_weather"
,
 
"description"
: 
"Get the current weather in a given location"
,
 
"input_schema"
: {
 
"type"
: 
"object"
,
 
"properties"
: {
"location"
: {
"type"
: 
"string"
}},
 
"required"
: [
"location"
],
 
"additionalProperties"
: 
False
,
 },
 
"strict"
: 
True
,
}

client.messages.create(
 model=
"claude-sonnet-5-5"
,
 max_tokens=
1024
,
 tools=[weather_tool],
 tool_choice={
"type"
: 
"auto"
}, 
# was {"type": "tool", "name": "get_weather"}

 messages=[
 {
"role"
: 
"user"
, 
"content"
: 
"What's the weather in Paris? Use the get_weather tool."
}
 ],
)

Strict tool use needsadditionalProperties: falseon every object.

### 3. Keep conversations append-only

Sonnet 5.5 thinking blocks are tied to the model and the conversation. Sonnet 5.5 reads Sonnet 5's thinking blocks, so a conversation you switch from Sonnet 5 to Sonnet 5.5 keeps its reasoning. No other model reads Sonnet 5.5's blocks.

### 4. Move computer use to the toolset

On the Claude API and Google Cloud, Sonnet 5.5 supports computer use only through{"type": "computer_toolset_20260801"}; a request that declarescomputer_20251124returns a 400 error. Drop theanthropic-beta: computer-use-2025-11-24header from your requests, and in the SDKs, remove thebetasparameter and call the Messages API through the standard client rather than the beta namespace. Replace thetoolsentry, and update your agent loop for membertool_useblocks, batch actions andtoolset_nameon results. If you send thefine-grained-tool-streaming-2025-05-14beta header, remove it too, because alongside a toolset entry it returns a 400 error; seteager_input_streaming: trueon each tool that needs it instead. Amazon Bedrock still acceptscomputer_20251124.

### 5. Check your advisor pairing

With the advisor tool, a Sonnet 5.5 executor rejects Opus 4.8, Opus 4.7 and Sonnet 5 as advisors. Accepted advisors include Opus 5.5, Opus 5 and Sonnet 5.5 itself. Advice from every accepted advisor comes back encrypted, as anadvisor_redacted_resultblock, so your code can't read the advice text.

### 6. Read text between tool calls from thinking blocks

This change causes no errors, but a UI can stop showing the model's notes between tool calls. Those notes, when longer than a sentence or two, come back as progress-updatethinkingblocks, which are empty at the defaultdisplay.

With adaptive thinking, setthinking.displayto"updates"(beta, with thethinking-display-updates-2026-08-18header) or"summarized", and render each non-emptythinkingblock before thetool_useblock that follows it. Withbetween_tools, the text comes back withoutdisplay.

Sonnet 5.5 also adds per-message effort (beta), mid-conversation system messages and mid-conversation tool changes (beta). If you're moving from Sonnet 4.6 or earlier, or from Haiku 4.5, themigration guidehas a checklist for each starting model.

## TUNING

### Re-run your effort sweep

Effort levels are recalibrated, so a level doesn't produce the same amount of thinking as it did on Sonnet 5, and your old setting won't carry over. Start withhighunless your workload is agentic or latency-sensitive. For agentic coding and multistep tool use, start withmediumfor well-specified tasks and move tohighfor harder or longer ones. For chat and other latency-sensitive work, start withmediumorlow. Usexhighormaxonly where your evals show a quality gain.

Thinking counts towardmax_tokens, so leave room. For agentic coding, setmax_tokensto 128,000, the model's maximum, and stream the response. To get less thinking, lower the effort level, because asking the model in the system prompt to think less doesn't reliably reduce it.

### Remove Sonnet 5 workarounds

Existing Sonnet 5 prompts should perform well without changes. If your prompts carry workarounds such as refusal steering, tool-call retry shims, or "do not be lazy," remove them and re-run your evals before tuning anything else.

### Ask for real checks at low effort

Sonnet 5.5 generally checks its work before reporting a change as done, but atloweffort it sometimes skips a check that exercises the change. If you see changes reported as done without test or build output, the prompting guide recommends this system-prompt paragraph:

CODE
Text
Copy
When you change code that can be run, built, or type-checked, run a real
check that exercises the change before reporting it done: the project's
tests, type-checker, or build, or the changed command itself. A syntax-only
check, or a check command that failed to start, does not count; if all
that is missing is the project's declared dependencies, install them with
its own package manager and lockfile (e.g. npm install, pip
install -r requirements.txt), never via sudo or the system package manager,
unless told not to. Only if no real check can run here, say which one you
did not run and why instead of reporting the change as done.

### Use thinking.display for progress

Don't ask the model to write out its reasoning in the response, because that invitesreasoning_extractiondeclines. Read summarized thinking instead:

CODE
Python
Copy
thinking={
"type"
: 
"adaptive"
, 
"display"
: 
"summarized"
}

For user-facing progress notes on their own, usedisplay: "updates"(beta). If you want updates at predictable points, such as a line before the first tool call and a short recap at the end, say so in the system prompt.

### Cache more of your prompt

The minimum cacheable prompt drops to 512 tokens, so shorter system prompts and tool definitions now qualify. A cache read costs a tenth of the input price. Changing the top-level effort between requests invalidates the cache; to run one turn at a different level, use per-message effort (beta), which keeps the cache.

## REFUSALS AND FALLBACK

On our automated behavioral audit, Sonnet 5.5 improves on or matches Sonnet 5 on most measures of alignment and honesty. It's also the first Sonnet model with cybersecurity safeguards similar to those on our most capable models. Most routine software development is unaffected.

A declined request returns HTTP 200 withstop_reason: "refusal", andstop_detailsnames one of five categories:cyber,bio,frontier_llm,reasoning_extractionorgeneral_harms. Server-side fallback (fallbacks: "default", beta, Claude API) retriescyberandfrontier_llmdeclines on Sonnet 5. It doesn't retry the other three. You can also use the SDK middleware or your own retry.

For legitimate security work, the Cyber Verification Program will soon expand to include Sonnet 5.5.

## AVAILABILITY

Claude Sonnet 5.5 is available today on the platforms below. On the developer platforms, use these model IDs:

* Claude API, asclaude-sonnet-5-5
* Amazon Bedrock, asanthropic.claude-sonnet-5-5
* Claude Platform on AWS, asclaude-sonnet-5-5
* Google Cloud, asclaude-sonnet-5-5
* Microsoft Foundry, asclaude-sonnet-5-5, on Global Standard deployments only

### In Claude Code

From Claude Code v2.1.284 (Agent SDK for TypeScript v0.3.284 or later), thesonnetalias resolves to Sonnet 5.5 on the Claude API. It runs atmediumeffort by default, with the 1M context window native. You can't turn thinking off for Sonnet 5.5 in Claude Code, and effort sets how much the model thinks. Sonnet 5.5 has no fast mode. Thedefaultmodel stays Opus 5.5, so switch with/model sonnetfor well-scoped tasks.

We hope you'll enjoy trying out Sonnet 5.5 and as always feel free to share feedback.

Related posts
ALL
AGENTS
ENGINEERING
PLAYBOOKS
SKILLS
Sep 28, 2026
Automating eval design and hillclimbing with Claude
12
 min
Sep 25, 2026
Using Claude Code: Spending your effort
8
 min
Sep 25, 2026
What a task costs on Opus 5.5
21
 min
Sep 23, 2026
How we made claude.ai 3x faster in two weeks
15
 min
Sep 22, 2026
Getting the most out of Opus 5.5 in Claude and Claude Code
9
 min
LOAD MORE