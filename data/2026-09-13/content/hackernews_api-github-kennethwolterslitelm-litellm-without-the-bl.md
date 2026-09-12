---
title: 'GitHub - kennethwolters/litelm: litellm without the bloat · GitHub'
url: https://github.com/kennethwolters/litelm
site_name: hackernews_api
content_file: hackernews_api-github-kennethwolterslitelm-litellm-without-the-bl
fetched_at: '2026-09-13T02:06:04.482194'
original_url: https://github.com/kennethwolters/litelm
author: kennethwolters
date: '2026-09-12'
description: litellm without the bloat. Contribute to kennethwolters/litelm development by creating an account on GitHub.
tags:
- hackernews
- trending
---

kennethwolters

 

/

litelm

Public

* NotificationsYou must be signed in to change notification settings
* Fork3
* Star177

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

69 Commits
69 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github/
workflows
.github/
workflows
 
 
litelm
litelm
 
 
scripts
scripts
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# litelm

litellm's routing + translation in ~2,900 lines and 2 dependencies (openai,httpx).

litellm routes LLM calls across providers and translates between message formats. That core is buried under 100k+ LOC of proxy servers, caching layers, cost tracking, and dozens of features most users never touch. litelm extracts just the call path — model routing, message translation, streaming, tool use, embeddings — and nothing else. No Router class, no proxy, no caching.

## Install

pip install litelm 
#
 openai + httpx

pip install litelm[anthropic] 
#
 + anthropic SDK

pip install litelm[bedrock] 
#
 + boto3

pip install litelm[all] 
#
 everything

## Usage

import
 
litelm

# Basic completion

response
 
=
 
litelm
.
completion
(
"openai/gpt-4o"
, 
messages
=
[{
"role"
: 
"user"
, 
"content"
: 
"Hello!"
}])

print
(
response
.
choices
[
0
].
message
.
content
)

# Streaming

for
 
chunk
 
in
 
litelm
.
completion
(
"groq/llama-3.1-70b-versatile"
, 
messages
=
[...], 
stream
=
True
):
 
print
(
chunk
.
choices
[
0
].
delta
.
content
 
or
 
""
, 
end
=
""
)

# Embeddings

response
 
=
 
litelm
.
embedding
(
"openai/text-embedding-3-small"
, 
input
=
[
"hello world"
])

Every function has an async variant:acompletion,aembedding,aresponses,atext_completion.

The API mirrors litellm — same function names, same arguments, same response types. If you're using litellm today, switching iss/litellm/litelm/in your imports.

## What's in / what's out

litellm

litelm

Model routing (
provider/model
 → right endpoint)

✓

✓

Message translation (Anthropic, Bedrock, Cloudflare, Mistral)

✓

✓

Streaming + 
stream_chunk_builder

✓

✓

Tool use (function calling)

✓

✓

Embeddings

✓

✓

Text completions

✓

✓

OpenAI Responses API

✓

✓

Mock responses

✓

✓

Router (load balancing, fallbacks)

✓

✗

Proxy server

✓

✗

Caching / budgeting / cost tracking

✓

✗

Token counting

✓

✗

Image gen, audio, OCR, fine-tuning

✓

✗

Agents, guardrails, scheduler

✓

✗

## Providers

Routes to 19 providers via"provider/model-name"syntax. Any OpenAI-compatible endpoint works viaapi_base.

Provider

Env Var

Handler

Verified

OpenAI

OPENAI_API_KEY

OpenAI SDK

Yes

Anthropic

ANTHROPIC_API_KEY

Custom

Yes

Groq

GROQ_API_KEY

OpenAI-compat

Yes

Mistral

MISTRAL_API_KEY

Custom

Yes

xAI

XAI_API_KEY

OpenAI-compat

Yes

OpenRouter

OPENROUTER_API_KEY

OpenAI-compat

Yes

Azure

AZURE_API_KEY

OpenAI SDK (Azure)

Yes

Bedrock

AWS_ACCESS_KEY_ID

Custom

No

Cloudflare

CLOUDFLARE_API_TOKEN

Custom

No

Together

TOGETHERAI_API_KEY

OpenAI-compat

No

Fireworks

FIREWORKS_API_KEY

OpenAI-compat

No

DeepSeek

DEEPSEEK_API_KEY

OpenAI-compat

No

Perplexity

PERPLEXITYAI_API_KEY

OpenAI-compat

No

DeepInfra

DEEPINFRA_API_TOKEN

OpenAI-compat

No

Gemini

GEMINI_API_KEY

OpenAI-compat

No

Cohere

COHERE_API_KEY

OpenAI-compat

No

Ollama

—

OpenAI-compat

No

vLLM

—

OpenAI-compat

No

LM Studio

—

OpenAI-compat

No

## API Keys

Set the environment variable for your provider:

export
 OPENAI_API_KEY=sk-...

export
 ANTHROPIC_API_KEY=sk-ant-...

Or pass directly:

litelm
.
completion
(
"openai/gpt-4o"
, 
messages
=
[...], 
api_key
=
"sk-..."
)

litelm
.
completion
(
"openai/gpt-4o"
, 
messages
=
[...], 
api_base
=
"http://localhost:8000/v1"
)

## Error Handling

All provider errors are mapped to litelm's exception hierarchy:

from
 
litelm
 
import
 
ContextWindowExceededError
, 
RateLimitError
, 
AuthenticationError

try
:
 
response
 
=
 
litelm
.
completion
(
"openai/gpt-4o"
, 
messages
=
messages
)

except
 
ContextWindowExceededError
:
 
# prompt too long — truncate and retry

 
pass

except
 
RateLimitError
:
 
# back off

 
pass

except
 
AuthenticationError
:
 
# bad API key

 
pass

## Tool Calling

tools
 
=
 [{
"type"
: 
"function"
, 
"function"
: {
 
"name"
: 
"get_weather"
,
 
"parameters"
: {
"type"
: 
"object"
, 
"properties"
: {
"city"
: {
"type"
: 
"string"
}}},
}}]

response
 
=
 
litelm
.
completion
(
 
"openai/gpt-4o"
, 
messages
=
[{
"role"
: 
"user"
, 
"content"
: 
"Weather in Paris?"
}],
 
tools
=
tools
, 
tool_choice
=
"required"
,
)

tool_call
 
=
 
response
.
choices
[
0
].
message
.
tool_calls
[
0
]

print
(
tool_call
.
function
.
name
, 
tool_call
.
function
.
arguments
)

## Custom / Local Providers

Any OpenAI-compatible server works viaapi_base:

# vLLM

litelm
.
completion
(
"openai/my-model"
, 
messages
=
[...], 
api_base
=
"http://localhost:8000/v1"
)

# Ollama

litelm
.
completion
(
"ollama/llama3"
, 
messages
=
[...], 
api_base
=
"http://localhost:11434/v1"
)

# LM Studio

litelm
.
completion
(
"openai/local-model"
, 
messages
=
[...], 
api_base
=
"http://localhost:1234/v1"
)

## Development transparency

litelm is human-directed, AI-assisted software. Much of the code was written with Claude Code using Claude Opus 4.6/4.7. Code written from 2026-05-14 onward is written through Pi using GPT-5.5. Compatibility claims are based on tests and maintainer review, not AI authorship.

## Upstream attestation

Maintainer attestation, 2026-09-11: LiteLLM's routing/formatting changes were reviewed from649eb2dthrough9a715df2. The audit triaged 360 core-path commits, inspected upstream tests for potentially relevant behavior, and fixed the resulting compatibility gaps test-first. Local scoped tests:262 passed, 55 skipped; all 45 available-provider live tests and all 10 DSPy smoke tests also passed with the current dependency lock.

This attests litelm's declared routing/formatting/DSPy surface only, not full litellm compatibility.

## Status

Alpha.262 own tests passing. The current scoped LiteLLM9a715df2baseline has 75 passing ported tests and no remaining actionable assertion/runtime failures.

DSPydrop-in verified — all 7 execution paths proven live (Predict, CoT, typed signatures, streaming, embeddings, tool use, multi-output).

## Tests

uv run --extra all pytest tests/ -x --ignore=tests/ported --timeout=10 
#
 262 non-live tests

bash scripts/ported_contract.sh 
#
 49 fast upstream contract tests

uv run --extra all pytest tests/test_live.py -m live --timeout=30 
#
 45 live provider tests

uv run pytest tests/test_dspy_smoke.py -m live --timeout=60 
#
 10 DSPy integration tests

Live tests require API keys in.env.test. Skipped by default; run with-m live.