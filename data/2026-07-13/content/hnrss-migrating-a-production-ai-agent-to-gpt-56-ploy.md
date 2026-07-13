---
title: Migrating a production AI agent to GPT-5.6 | Ploy
url: https://ploy.ai/blog/migrating-a-production-ai-agent-to-gpt-5-6
site_name: hnrss
content_file: hnrss-migrating-a-production-ai-agent-to-gpt-56-ploy
fetched_at: '2026-07-13T12:27:11.200167'
original_url: https://ploy.ai/blog/migrating-a-production-ai-agent-to-gpt-5-6
date: '2026-07-12'
description: We hold frontier models to a high bar, and for four months nothing beat Claude Opus. GPT-5.6 did. Here's the migration guide we wish we'd had.
tags:
- hackernews
- hnrss
---

As of today, Ploy’s agent runs on GPT-5.6 Sol, the flagship tier of the model family OpenAI released this morning. For months, we couldn’t find a model that challenges Claude Opus given our incredibly high bar for quality. That changed with GPT 5.6 Sol. After running it head-to-head against Claude Opus, we’ve made GPT 5.6 Sol the default model powering every Ploy workspace.

That’s a bigger switch than it sounds. Ploy’s agent builds and edits real marketing websites. It plans a page, reads the codebase, writes components, generates imagery, screenshots its own work, and decides when it’s done. That job description sets a very high bar for a model, and we test every frontier release against it. For the four months Opus held the default slot (first Opus 4.7, then 4.8), nothing we tested beat it. GPT-5.6 is the first model that did.

Not that the first eval run was perfect. It had real failure modes, which we’ll show you. But it did extremely well, and the promise was immediate and specific: builds finishing in less than half the wall-clock time, at 27% lower cost, scoring at or above our incumbent on completed work. Numbers like that buy a model a real migration effort.

Despite using Vercel’sAI SDK, a universal LLM SDK, switching from Claude Opus 4.8 to GPT 5.6 Sol required discovering, one eval failure at a time, that the things we think of as “the model” are provider-specific behaviors our whole stack has quietly specialized around: how it fills in tool arguments, how its prompt cache works, how it replays its own reasoning between turns.

Here’s what it took: fix the eval harness, then the tool schemas, then caching, then reasoning replay.

## Step 0: Fix your harness before you trust a single number

Our eval suite runs the real agent against real fixture workspaces. Hundreds of cases, from “build a homepage from scratch” to “is this clone request safe to execute.” Build cases are scored by a visual judge running binary checks against a reference design, ten yes/no questions like“the hero is a full-bleed photographic scene”or“primary CTAs are rounded rectangles, not pills”, plus content checks, tool-trajectory checks, and file assertions. Every failed case gets triaged against its full trace: the actual tool calls and model text, not just the score.

Running that suite across two model families surprised us more than any individual result:

Your harness is tuned to your incumbent model, and you don’t know it.Our tool-call budgets were sized for Opus’s sequential style; GPT-5.6 fans out parallel calls and blew through them on cases it was solving correctly. Our eval executor didn’t support batched file reads, which Opus rarely used and GPT-5.6 uses constantly. Roughly a third of the raw failures in the first cross-model run traced back to harness assumptions, not model behavior, and they were not evenly distributed between the models. If you’re evaluating a challenger model against an incumbent,triage the traces before you trust the pass rate. Otherwise you’re grading the new model on how well it imitates the old one.

Make sure you’re grading models fairly in evals.A dataset that omitted itsminScorethreshold silently inherited a default of 1.0, so GPT-5.6 “failed” a hero it scored 0.98 on, and Opus “failed” a case while passing every individual check. Two defensible design directions; one invisible threshold.

## First impression: immediately promising

With the harness cleaned up, here’s a sample from our redesign suite, where the agent rebuilds a brand’s homepage against a reference design:

Mean per completed build
Claude Opus 4.8 (n=11)
GPT-5.6 (n=10)
Cost
$3.06
$2.22
Wall-clock time
8m 00s
3m 42s
Input tokens
2.60M
1.70M
Output tokens
33.0K
17.1K
Visual score
0.936
0.970

This is the shape of the promise: 2.2× faster to a finished page, 27% cheaper, and about half the output tokens. GPT-5.6 writes lean code. On one matched pair, Opus produced a 17,957-characterglobals.csswith 174 CSS variables (full color ramps, mostly unused) where GPT-5.6 wrote 2,508 characters and 45 variables for a comparable (and sometimes better) rendered page.

### Claude Opus 4.8

See full size

### GPT-5.6 Sol

See full size

### Design: sharp, clean, but a little bit uniform

Our overall read on GPT-5.6’s design work: it isverygood at clean, modern, tightly-gridded layouts, but it tends to converge towards that look unless you steer it well. With our older harness designed for Opus 4.8, GPT 5.6 Sol tends to ignore existing design systems and instead produces sharp, restrained, and visibly generic output.

The details of how we fixed this are worth a separate blog post of its own. With the expertise of our design and engineering teams, we are able to steer models to achieve world-class brand adherence that you can’t get out of the box.

## Step 1: Check your tool calls

Here’s the one that was silently corrupting results before we caught it.

Our agent’scodetool has 25 top-level parameters, one required (action) and the rest optional. Claude sends the two or three it’s using and omits the rest. GPT-5.6 sendsall 25, every time, inventing plausible values for the ones it doesn’t need:offset: 0,timeout: 120000,siteId: "00000000-0000-0000-0000-000000000000".

Three days of production traces,code(read)calls carrying every property:

Model
Calls
Carrying all 25 properties
gpt-5.6
6,635
6,635 (100%)
claude-opus-4.8
2,898
4 (0.1%)
claude-sonnet-5
1,933
0

The problem isn’t verbosity. It’s thatan invented value is indistinguishable from an intended one.offset: 0looks like a real argument. Our file-read implementation treated it as one, and 52% to 64% of GPT-5.6’s file reads were coming back empty because of it. The tool returnedsuccess: trueboth ways, so the model had no way to know it was reading blank files. It just did the work worse, with more calls.

Prompting doesn’t fix this. A tool-description directive to “omit unused parameters”: still 25/25. Per-property “OPTIONAL, omit if unused” hints: still 25/25. OpenAI’sstrictmode: identical behavior (we measured), and adopting it would have forced us to strippattern,format, and array-bound validation from every schema. This is baked into how the model emitsfunction calls. You don’t instruct it away; you design around it.

The fix that worked is a schema transform at the provider boundary. For OpenAI-family models only, we rewrite every optional property to berequired but nullable, usinganyOf: [T, null], which gives the model an explicit way to say “not using this.” Then, at the single seam every tool invocation passes through, we strip the nulls back out before validation, so no tool implementation changes at all. Round trip: the model sees a schema where honesty is expressible; the tools see the same inputs they always did.

// Before: 25 keys, every one carrying an invented value

{ 
"action"
: 
"read"
, 
"file_paths"
: [
...
], 
"offset"
: 
0
, 
"timeout"
: 
120000
, 
...
 }

// After: 25 keys, 4 real values, 21 explicit nulls (stripped before the tool runs)

{ 
"action"
: 
"read"
, 
"file_paths"
: [
...
], 
"offset"
: 
null
, 
"timeout"
: 
null
, 
...
 }

Results: empty file reads went from 52% to 0%, and the agent needed roughly 30% fewer tool calls for the same work, because it was no longer re-reading files that came back blank.

## Step 2: Rebuild prompt caching

This was the most instructive engineering difference, because on the surface both providers offer “prompt caching” and the words hide two entirely different designs. If you migrate one thing carefully, make it this: before we did, GPT-5.6 looked about 50% more expensive than Opus. It wasn’t the model’s pricing; it was our cache configuration.

Our agent’s prompt opens with a static prefix of roughly 29K tokens (tool schemas plus the core system prompt) that’s identical for every conversation. On Claude, we mark cache breakpoints withcache_controland that prefix cachesacross the whole organization: any conversation, any workspace, one shared entry, no throughput budget to think about. Cache hit rates run 92% to 96% and caching fades into the background.

GPT-5.6 changed OpenAI’s caching model out from under us. Earlier GPT models cached implicitly on partial prefix matches, which gave decent hit rates for free. GPT-5.6dropped partial-prefix matching: implicit caching now only creates whole-prompt entries keyed on the latest message. Anewconversation sharing our 29K static prefix cached0%of it. Every conversation re-billed the full prefix at the uncached rate, and on GPT-5.6 every uncached prompt also pays a 1.25× cache-writesurcharge, whether or not you use caching.

The intended mechanism is explicit:prompt_cache_breakpointmarkers plus a mandatoryprompt_cache_key. And the key is where the design really diverges, because it’s part of cache identity. Identical prompt, different key: zero cache hits. Each key maps to a cache node that sustains roughly15 requests per minutebefore OpenAI fans traffic to other nodes with independent, cold caches.

That turns “enable caching” into an actual design decision: what entity do you scope the key to?

* Per-conversation keymeans a new conversation never hits the shared prefix. First-call hit rate: 0%. (We measured this mistake. It’s expensive.)
* One global keymeans every request hashes to one cache node, and production traffic obliterates the 15 rpm budget; requests spill to cold nodes and you’re back to misses.
* Per-workspace keyis the sweet spot. All conversations in a customer workspace share entries; per-key traffic stays low.

We ship the workspace-scoped key and split the system prompt into breakpointed layers, mirroring the structure we already used for Anthropic:

request ──► hash(prompt head + prompt_cache_key) ──► cache node (~15 req/min per key)

 │

 ┌──────────────────────────────────────────────────────┴───────────────┐

 │ entries on the node, all namespaced by key ws:{workspaceId} │

 │ │

 │ [ tools + static prefix ]······················ A every session │

 │ [ tools + static prefix + workspace context ]·· B same context │

 │ [ ····················· + turn 1 + … + latest ] C this session │

 └──────────────────────────────────────────────────────────────────────┘

Entry A is what makes a session’sfirstcall cheap. Entry B self-heals: when workspace memory changes, the request misses B but still hits A, then writes a fresh B. One context-sized write instead of a full 29K re-bill. Entry C is OpenAI’s implicit whole-prompt chain, which works fine within a session because our prompts are strictly append-only.

One consequence has no workaround:cross-workspace sharing of the static prefix is structurally impossible on OpenAI.Anthropic can share it because its cache is org-scoped without key partitioning. On GPT-5.6, every workspace pays one 29K cold write per idle window, about $0.18. A real cost, but bounded and predictable.

Results after the change: first-call cache hits went from roughly 0% to83.7%, total uncached input tokens dropped 28%, and GPT-5.6’s per-suite cost landedbelowOpus’s. Every dollar of the gap we’d been staring at was cache misconfiguration, not model pricing. If you’re cost-comparing models and one of them has a cold cache, you are comparing your config, not the models.

## Step 3: Make reasoning replay self-contained

Shorter, but it broke real conversations. GPT-5.6’s Responses API replays prior-turn reasoning as server-side item references by default; ours started intermittently failing mid-conversation withItem 'rs_...' not found. The fix isstore: false, which makes the SDK requestencrypted reasoning contentand replay self-contained blobs instead of pointers to server state. A corollary that cost us a debugging afternoon: with server-side reasoning state in the loop, the effective prompt can change upstream of you even when the bytes you send are append-only.

## GPT 5.6 Sol is ready to Ploy

Try it yourself.GPT-5.6 launched today, and it’s already live on Ploy. You can try it for free right now: give it a website to build and see what a sub-four-minute build looks like.Start free at ploy.ai.

Ploy is marketing run on autopilot: an AI layer that plans, builds, publishes, and optimizes your website and campaigns end-to-end. If debugging cache-node fan-out at 2am sounds like fun,we’re hiring.