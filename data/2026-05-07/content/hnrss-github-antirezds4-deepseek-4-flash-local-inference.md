---
title: 'GitHub - antirez/ds4: DeepSeek 4 Flash local inference engine for Metal · GitHub'
url: https://github.com/antirez/ds4
site_name: hnrss
content_file: hnrss-github-antirezds4-deepseek-4-flash-local-inference
fetched_at: '2026-05-07T20:12:56.662580'
original_url: https://github.com/antirez/ds4
date: '2026-05-07'
description: DeepSeek 4 Flash local inference engine for Metal. Contribute to antirez/ds4 development by creating an account on GitHub.
tags:
- hackernews
- hnrss
---

antirez

 

/

ds4

Public

* NotificationsYou must be signed in to change notification settings
* Fork14
* Star345

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

7 Commits
7 Commits
metal
metal
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
AGENT.md
AGENT.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
download_model.sh
download_model.sh
 
 
ds4.c
ds4.c
 
 
ds4.h
ds4.h
 
 
ds4_cli.c
ds4_cli.c
 
 
ds4_metal.h
ds4_metal.h
 
 
ds4_metal.m
ds4_metal.m
 
 
ds4_server.c
ds4_server.c
 
 
linenoise.c
linenoise.c
 
 
linenoise.h
linenoise.h
 
 
View all files

## Repository files navigation

# ds4.c

ds4.cis a small native inference engine for DeepSeek V4 Flash. It is
intentionally narrow: not a generic GGUF runner, not a wrapper around another
runtime, and not a framework. The main path is a DeepSeek V4 Flash-specific
Metal graph executor with DS4-specific loading, prompt rendering, KV state, and
server API glue.

This project would not exist withoutllama.cpp and GGML, make sure to read
the acknowledgements section, a big thank you to Georgi Gerganov and all the
other contributors.

Now, back at this project. Why we believe DeepSeek v4 Flash to be a pretty special
model deserving a stand alone engine? Because after comparing it with powerful smaller
dense models, we can report that:

1. DeepSeek v4 Flash is faster because of less active parameters.
2. In thinking mode, if you avoidmax thinking, it produces a thinking section that is a lot shorter than other models, even 1/5 of other models in many cases, and crucially, the thinking section length isproportional to the problem complexity. This makes DeepSeek v4 Flash usable with thinking enabled when other models are practically impossible to use in the same conditions.
3. The model features a context window of1 million tokens.
4. Being so large, it knows more things if you go sampling at the edge of knowledge. For instance asking about Italian show or political questions soon uncovers that 284B parameters are a lot more than 27B or 35B parameters.
5. It writes much better English and Italian. Itfeelsa quasi-frontier model.
6. The KV cache is incredibly compress, allowing long context inference on local computers andon disk KV cache persistence.
7. It works well with 2-bit quantization, if quantized in a special way (read later). This allows to run it in MacBooks with 128GB of RAM.
8. We expect DeepSeek to releaseupdated versions of v4 Flashin the future, even better than the current one.

That said, a few important things about this project:

* The local inference landscape contains many excellent projects, but new models are released continuously, and the attention immediately gets captured by the next model to implement. This project takes a deliberately narrow bet: one model at a time, official-vector validation (logits obtained with the official implementation), long-context tests, and enough agent integration to know if it really works. The exact model may change as the landscape evolves, but the constraint remains: local inference credible on high end personal machines or Mac Studios, starting from 128GB of memory.
* This software is developed withstrong assistance from GPT 5.5and with humans leading the ideas, testing, and debugging. We say this openly because it shaped how the project was built. If you are not happy with AI-developed code, this software is not for you. The acknowledgement below is equally important: this would not exist withoutllama.cppand GGML, largely written by hand.
* This implementation is based on the idea that compressed KV caches like the one of DeepSeek v4 and the fast SSD disks of modern MacBooks should change our idea that KV cache belongs to RAM.The KV cache It is actually a first class disk citizen.
* Our vision is that local inference should be a set of three things working well together, out of the box: A) inference engine with HTTP API + B) GGUF specially crafted to run well under a given engine and given assumptions + C) testing and validation with coding agents implementations. This inference engine only runs with the GGUF files provided. It gets tested against officially obtained logits at different context sizes. This project exists because we wanted to make one local model feel finished end to end, not just runnable. However this is just alpha quality code, so probably we are not still there.
* This isMetal-only, may implement CUDA support in the future? Perhaps, but nothing more. The CPU path is only for correctness check, butwarning: current macOS versions have a bug in the virtual memory implementation that will crash the kernelif you try to run the CPU code. Remember? Software sucks. I was not possible to fix the CPU inference to avoid crashing, since each time there is to restart the computer, which is not funny. Help us, if you have the guts.

## Acknowledgements to llama.cpp and GGML

ds4.cdoes not link against GGML, but itexists thanks to the path opened by the
llama.cpp project and the kernels, quantization formats, GGUF ecosystem, and hard-won
engineering knowledge developed there.
We are thankful and indebted tollama.cppand its contributors. Their implementation, kernels, tests, and design choices were
an essential reference while building this DeepSeek V4 Flash-specific inference path.
Some source-level pieces are retained or adapted here under the MIT license: GGUF
quant layouts and tables, CPU quant/dot logic, and certain Metal kernels. For this
reason, and because we are genuinely grateful, we keep the GGML authors copyright
notice in ourLICENSEfile.

## Model Weights

This implementation only works with the DeepSeek V4 Flash GGUFs published for
this project. It is not a general GGUF loader, and arbitrary DeepSeek/GGUF files
will not have the tensor layout, quantization mix, metadata, or optional MTP
state expected by the engine. The 2 bit quantizations provided here are not
a joke: they behave well, work under coding agents, call tools in a reliable way.
The 2 bit quants use a very asymmetrical quantization: only the routed MoE
experts are quantized, up/gate atIQ2_XXS, down atQ2_K. They are the
majority of all the model space: the other components (shared experts,
projections, routing) are left untouched to guarantee quality.

Download one main model:

./download_model.sh q2 
#
 128 GB RAM machines

./download_model.sh q4 
#
 >= 256 GB RAM machines

The script downloads fromhttps://huggingface.co/antirez/deepseek-v4-gguf,
stores files under./gguf/, resumes partial downloads withcurl -C -, and
updates./ds4flash.ggufto point at the selected q2/q4 model. Authentication
is optional for public downloads, but--token TOKEN,HF_TOKEN, or the local
Hugging Face token cache are used when present.

./download_model.sh mtpfetches the optional speculative decoding support
GGUF. It can be used with both q2 and q4, but must be enabled explicitly with--mtp. The current MTP/speculative decoding path is still experimental: it is
correctness-gated and currently provides at most a slight speedup, not a
meaningful generation-speed win.

Then build:

make

./ds4flash.ggufis the default model path used by both binaries. Pass-mto
select another supported GGUF from./gguf/. Run./ds4 --helpand./ds4-server --helpfor the full flag list.

## Speed

These are single-run Metal CLI numbers with the q2 GGUF,--ctx 32768,--nothink, greedy decoding, and-n 256. The short prompt is a normal small
Italian story prompt. The long prompt is 11709 tokens and exercises chunked
prefill plus long-context decode.

Machine

Prompt

Prefill

Generation

MacBook Pro M3 Max, 128 GB

short

58.52 t/s

26.68 t/s

MacBook Pro M3 Max, 128 GB

11709 tokens

250.11 t/s

21.47 t/s

Mac Studio M3 Ultra, 512 GB

short

84.43 t/s

36.86 t/s

Mac Studio M3 Ultra, 512 GB

11709 tokens

468.03 t/s

27.39 t/s

## CLI

One-shot prompt:

./ds4 -p 
"
Explain Redis streams in one paragraph.
"

No-pstarts the interactive prompt:

./ds4
ds
4>

The interactive CLI is a real multi-turn DS4 chat. It keeps the rendered chat
transcript and the live Metal KV checkpoint, so each turn extends the previous
conversation. Useful commands are/help,/think,/think-max,/nothink,/ctx N,/read FILE, and/quit. Ctrl+C interrupts the current generation
and returns tods4>.

The CLI defaults to thinking mode. Use/nothinkor--nothinkfor direct
answers.--mtp MTP.gguf --mtp-draft 2enables the optional MTP speculative
path; it is useful only for greedy decoding, currently uses a confidence gate
(--mtp-margin) to avoid slow partial accepts, and should be treated as an
experimental slight-speedup path.

## Server

Start a local OpenAI/Anthropic-compatible server:

./ds4-server --ctx 100000 --kv-disk-dir /tmp/ds4-kv --kv-disk-space-mb 8192

The server is Metal-only. It keeps one mutable graph/KV checkpoint in memory,
so stateless clients that resend a longer version of the same prompt can reuse
the shared prefix instead of pre-filling from token zero.

Request parsing and sockets run in client threads, but inference itself is
serialized through one Metal worker. The current server does not batch multiple
independent requests together; concurrent requests wait their turn on the single
live graph/session.

Supported endpoints:

* GET /v1/models
* GET /v1/models/deepseek-v4-flash
* POST /v1/chat/completions
* POST /v1/completions
* POST /v1/messages

/v1/chat/completionsaccepts the usual OpenAI-stylemessages,max_tokens/max_completion_tokens,temperature,top_p,top_k,min_p,seed,stream,stream_options.include_usage,tools, andtool_choice.
Tool schemas are rendered into DeepSeek's DSML tool format, and generated DSML
tool calls are mapped back to OpenAI tool calls.

/v1/messagesis the Anthropic-compatible endpoint used by Claude Code style
clients. It acceptssystem,messages,tools,tool_choice,max_tokens,temperature,top_p,top_k,stream,stop_sequences, and thinking
controls. Tool uses are returned as Anthropictool_useblocks.

Both APIs support SSE streaming. In thinking mode, reasoning is streamed in the
native API shape instead of being mixed into final text.

Minimal OpenAI example:

curl http://127.0.0.1:8000/v1/chat/completions \
 -H 
'
Content-Type: application/json
'
 \
 -d 
'
{

 "model":"deepseek-v4-flash",

 "messages":[{"role":"user","content":"List three Redis design principles."}],

 "stream":true

 }
'

### Agent Client Usage

ds4-servercan be used by local coding agents that speak OpenAI-compatible
chat completions. Start the server first, and set the client context limit no
higher than the--ctxvalue you started the server with:

./ds4-server --ctx 100000 --kv-disk-dir /tmp/ds4-kv --kv-disk-space-mb 8192

You can use larger context and larger cache if you wish. Full context of
1M tokens is going to use more or less 26GB of memory (compressed indexer
alone will be like 22GB), so configure a context which makes sense in
your system. With 128GB of RAM you would run the 2-bit quants, which are
already 81GB, 26GB are going to be likely too much, so a context window
of 100~300k tokens is wiser.

The384000output limit below avoids token caps since the model is able
to generate very long replies otherwise (up to 384k tokens). The server
still stops when the configured context window is full.

Foropencode, add a provider and agent entry to~/.config/opencode/opencode.json:

{
 
"$schema"
: 
"
https://opencode.ai/config.json
"
,
 
"provider"
: {
 
"ds4"
: {
 
"name"
: 
"
ds4.c (local)
"
,
 
"npm"
: 
"
@ai-sdk/openai-compatible
"
,
 
"options"
: {
 
"baseURL"
: 
"
http://127.0.0.1:8000/v1
"
,
 
"apiKey"
: 
"
dsv4-local
"

 },
 
"models"
: {
 
"deepseek-v4-flash"
: {
 
"name"
: 
"
DeepSeek V4 Flash (ds4.c local)
"
,
 
"limit"
: {
 
"context"
: 
100000
,
 
"output"
: 
384000

 }
 }
 }
 }
 },
 
"agent"
: {
 
"ds4"
: {
 
"description"
: 
"
DeepSeek V4 Flash served by local ds4-server
"
,
 
"model"
: 
"
ds4/deepseek-v4-flash
"
,
 
"temperature"
: 
0

 }
 }
}

ForPi, add a provider to~/.pi/agent/models.json:

{
 
"providers"
: {
 
"ds4"
: {
 
"name"
: 
"
ds4.c local
"
,
 
"baseUrl"
: 
"
http://127.0.0.1:8000/v1
"
,
 
"api"
: 
"
openai-completions
"
,
 
"apiKey"
: 
"
dsv4-local
"
,
 
"compat"
: {
 
"supportsStore"
: 
false
,
 
"supportsDeveloperRole"
: 
false
,
 
"supportsReasoningEffort"
: 
true
,
 
"supportsUsageInStreaming"
: 
true
,
 
"maxTokensField"
: 
"
max_tokens
"
,
 
"supportsStrictMode"
: 
false
,
 
"thinkingFormat"
: 
"
deepseek
"
,
 
"requiresReasoningContentOnAssistantMessages"
: 
true

 },
 
"models"
: [
 {
 
"id"
: 
"
deepseek-v4-flash
"
,
 
"name"
: 
"
DeepSeek V4 Flash (ds4.c local)
"
,
 
"reasoning"
: 
true
,
 
"thinkingLevelMap"
: {
 
"off"
: 
null
,
 
"minimal"
: 
"
low
"
,
 
"low"
: 
"
low
"
,
 
"medium"
: 
"
medium
"
,
 
"high"
: 
"
high
"
,
 
"xhigh"
: 
"
xhigh
"

 },
 
"input"
: [
"
text
"
],
 
"contextWindow"
: 
100000
,
 
"maxTokens"
: 
384000
,
 
"cost"
: {
 
"input"
: 
0
,
 
"output"
: 
0
,
 
"cacheRead"
: 
0
,
 
"cacheWrite"
: 
0

 }
 }
 ]
 }
 }
}

Optionally make it the default Pi model in~/.pi/agent/settings.json:

{
 
"defaultProvider"
: 
"
ds4
"
,
 
"defaultModel"
: 
"
deepseek-v4-flash
"

}

ForClaude Code, use the Anthropic-compatible endpoint. A wrapper like this
matches the local~/bin/claude-ds4setup:

#!
/bin/sh

unset
 ANTHROPIC_API_KEY

export
 ANTHROPIC_BASE_URL=
"
${DS4_ANTHROPIC_BASE_URL
:-
http
://
127.0.0.1
:
8000}
"

export
 ANTHROPIC_AUTH_TOKEN=
"
${DS4_API_KEY
:-
dsv4-local}
"

export
 ANTHROPIC_MODEL=
"
deepseek-v4-flash
"

export
 ANTHROPIC_CUSTOM_MODEL_OPTION=
"
deepseek-v4-flash
"

export
 ANTHROPIC_CUSTOM_MODEL_OPTION_NAME=
"
DeepSeek V4 Flash local ds4
"

export
 ANTHROPIC_CUSTOM_MODEL_OPTION_DESCRIPTION=
"
ds4.c local GGUF
"

export
 ANTHROPIC_DEFAULT_SONNET_MODEL=
"
deepseek-v4-flash
"

export
 ANTHROPIC_DEFAULT_HAIKU_MODEL=
"
deepseek-v4-flash
"

export
 ANTHROPIC_DEFAULT_OPUS_MODEL=
"
deepseek-v4-flash
"

export
 CLAUDE_CODE_SUBAGENT_MODEL=
"
deepseek-v4-flash
"

export
 CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1

export
 CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK=1

export
 CLAUDE_STREAM_IDLE_TIMEOUT_MS=600000

exec
 
"
$HOME
/.local/bin/claude
"
 
"
$@
"

Claude Code may send a large initial prompt, often around 25k tokens, before it
starts doing useful work. Keep--kv-disk-direnabled: after the first expensive
prefill, the disk KV cache lets later continuations or restarted sessions reuse
the saved prefix instead of processing the whole prompt again.

## Thinking Modes

DeepSeek V4 Flash has distinct non-thinking, thinking, and Think Max modes.
The server defaults to thinking mode.reasoning_effort=maxrequests Think
Max, but it is only applied when the context size is large enough for the model
card recommendation; smaller contexts fall back to normal thinking. OpenAIreasoning_effort=xhighstill maps to normal thinking, not Think Max.

For direct replies, usethinking: {"type":"disabled"},think:false, or a
non-thinking model alias such asdeepseek-chat.

## Disk KV Cache

Chat/completion APIs are stateless: agent clients usually resend the whole
conversation every request.ds4-serverhandles this by comparing the rendered
token stream with cached token prefixes. The live in-memory checkpoint covers
the current session; the disk KV cache makes useful prefixes survive session
switches and server restarts.

For RAM reasons there is currently only one live KV cache in memory. When a new
unrelated session replaces it, the old checkpoint can only be resumed without
re-processing if it was written to the disk KV cache. In other words, memory
cache handles the active session; disk cache is the resume mechanism for
different sessions.

Enable it with:

./ds4-server --kv-disk-dir /tmp/ds4-kv --kv-disk-space-mb 8192

The cache key is the SHA1 of exact token IDs, not raw text. Each token ID is
hashed as a little-endian 32-bit integer, and files are named<sha1>.kv.
The file is intentionally written with ordinaryread/writeI/O, notmmap, so restoring cache entries does not add more VM mappings to a process
that already maps the model.

On disk, a cache file is:

KVC fixed header, 48 bytes
u32 rendered_text_bytes
rendered_text_bytes of UTF-8-ish token text
DS4 session payload, payload_bytes from the KVC header

The fixed header is little-endian:

0 u8[3] magic = "KVC"
3 u8 version = 1
4 u8 routed expert quant bits, currently 2 or 4
5 u8 save reason: 0 unknown, 1 cold, 2 continued, 3 evict, 4 shutdown
6 u8[2] reserved
8 u32 cached token count
12 u32 hit count
16 u32 context size the snapshot was written for
20 u8[4] reserved
24 u64 creation Unix time
32 u64 last-used Unix time
40 u64 DS4 session payload byte count

The rendered text is the tokenizer-decoded text for the cached token prefix.
It is stored only for observability, so humans can inspect a cache directory
without decoding token IDs. It is not used as the key and it is not trusted
when loading; after load, the stored checkpoint tokens must still match the
incoming request prefix.

The DS4 session payload starts with thirteen little-endianu32fields:

0 magic = "DSV4"
1 payload version = 1
2 saved context size
3 prefill chunk size
4 raw KV ring capacity
5 raw sliding-window length
6 compressed KV capacity
7 checkpoint token count
8 layer count
9 raw/head KV dimension
10 indexer head dimension
11 vocabulary size
12 live raw rows serialized below

Then it stores:

* u32[token_count]checkpoint token IDs.
* float32[vocab_size]logits for the next token after that checkpoint.
* u32[layer_count]compressed attention row counts.
* u32[layer_count]ratio-4 indexer row counts.
* For every layer: the live raw sliding-window KV rows, written in logical
position order rather than physical ring order.
* For compressed layers: live compressed KV rows and compressor frontier
tensors.
* For ratio-4 compressed layers: live indexer compressed rows and indexer
frontier tensors.

The logits are raw IEEE-754float32values from the hostds4_sessionbuffer. They are saved immediately after the checkpoint tokens so a loaded
snapshot can sample or continue from the exact next-token distribution without
running one extra decode step. MTP draft logits/state are not persisted; after
loading a disk checkpoint the draft state is invalidated and rebuilt by normal
generation.

The tensor payload is DS4-specific KV/session state, not a generic inference
graph dump. It is expected to be portable only across compatibleds4.cbuilds for this model layout.

The cache stores checkpoints at four moments:

* cold: after a long first prompt reaches a stable prefix, before generation.
* continued: when prefill or generation advances the live conversation by the configured interval.
* evict: before an unrelated request replaces the live in-memory session.
* shutdown: when the server exits cleanly.

Cold saves intentionally trim a small token suffix and align down to a prefill
chunk boundary. This avoids common BPE boundary retokenization misses when a
future request appends text to the same prompt. The defaults are conservative:
store prefixes of at least 512 tokens, cold-save prompts up to 30000 tokens,
trim 32 tail tokens, and align to 2048-token chunks. The important knobs are:

* --kv-cache-min-tokens
* --kv-cache-cold-max-tokens
* --kv-cache-continued-interval-tokens
* --kv-cache-boundary-trim-tokens
* --kv-cache-boundary-align-tokens

By default, checkpoints may be reused across the 2-bit and 4-bit routed-expert
variants if the token prefix matches. Use--kv-cache-reject-different-quantwhen you want strict same-quant reuse only.

The cache directory is disposable. If behavior looks suspicious, stop the
server and remove it. You can investigate what is cached with hexdump as
the kv cache files include the verbatim prompt cached.

## Backends

The default backend is Metal:

./ds4 -p 
"
Hello
"
 --metal

There is also a CPU reference/debug path:

./ds4 -p 
"
Hello
"
 --cpu

Do not treat the CPU path as the production target. The server is Metal-only,
and the optimized implementation lives in the Metal graph path. This may
change in the future.

## Test Vectors

tests/test-vectorscontains short and long-context continuation vectors
captured from the official DeepSeek V4 Flash API. The requests usedeepseek-v4-flash, greedy decoding, thinking disabled, and the maximumtop_logprobsslice exposed by the API. Local vectors are generated with./ds4 --dump-logprobsand compared by token bytes, so tokenizer/template or
attention regressions show up before they become long generation failures.

All project tests are driven by the C runner:

make 
test
 
#
 ./ds4_test --all

./ds4_test --logprob-vectors
./ds4_test --server

## About

DeepSeek 4 Flash local inference engine for Metal

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

345

 stars
 

### Watchers

4

 watching
 

### Forks

14

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* C55.4%
* Objective-C30.2%
* Metal13.8%
* Other0.6%