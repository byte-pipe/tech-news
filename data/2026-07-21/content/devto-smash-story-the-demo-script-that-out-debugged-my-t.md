---
title: 'Smash Story: The Demo Script That Out-Debugged My Test Suite - DEV Community'
url: https://dev.to/gde/smash-story-the-demo-script-that-out-debugged-my-test-suite-430k
site_name: devto
content_file: devto-smash-story-the-demo-script-that-out-debugged-my-t
fetched_at: '2026-07-21T11:37:26.888518'
original_url: https://dev.to/gde/smash-story-the-demo-script-that-out-debugged-my-test-suite-430k
author: xbill
date: '2026-07-15'
description: A green 10-test suite, a broken production default, and the 10-minute smash — how a live demo caught an API-contract bug that mocks never could. Tagged with devchallenge, bugsmash, ai, debugging.
tags: '#devchallenge, #bugsmash, #ai, #debugging'
---

Summer Bug Smash: Smash Stories Submission 🐛🛹

This is a Smash Stories submission for theDEV Summer Bug Smash: a debugging story about the gap between "all tests pass" and "it actually works" — and the unlikely hero that closed it.

## The setup

The project is a smallMCP (Model Context Protocol) serverthat wraps Google'sgemini-3.1-flash-lite-imagemodel. It exposes image generation andstatefulimage editing as four tools that any MCP-speaking agent can call — Claude Code, a Google ADK agent, and a Rust CLI all consume the same ~300-line Python server. (Full architecture write-uphere.)

By every signal a developer normally trusts, it was healthy:

* ✅ 10/10 unit tests passing
* ✅ ruff + mypy clean
* ✅ Used successfully through AI agents for days
* ✅ Published as a Docker image

Then I wrote a demo script. It found a production bug in under a minute of runtime.

## The smash

demo.shwalks the stack live: discover the tools, generate an image, then do a stateful edit. To keep the demo cheap, step 2 requested the lowest quality tier the server documents:

cargo run 
--quiet
 
--
 generate 
"a tiny robot chef cooking ramen"
 16:9 minimal

Enter fullscreen mode

Exit fullscreen mode

First run:

🔴 Image generation failed: Error code: 400 - {'error': {'message':
"'minimal' is not a supported thinking level for this model.
Allowed values are: low, high.", 'code': 'invalid_request'}}

Enter fullscreen mode

Exit fullscreen mode

Wait. The server's own validation hadapprovedminimalbefore sending it. Here's that validation:

# server.py — as shipped

SUPPORTED_THINKING_LEVELS
 
=
 
{
"
minimal
"
,
 
"
low
"
,
 
"
medium
"
,
 
"
high
"
}

@mcp.tool
()

def
 
generate_image
(

 
prompt
:
 
str
,
 
aspect_ratio
:
 
str
 
=
 
"
1:1
"
,
 
thinking_level
:
 
str
 
=
 
"
medium
"

)
 
->
 
str
:

 
...

Enter fullscreen mode

Exit fullscreen mode

Four allowed values. The live API acceptstwo:lowandhigh. And look at the default —medium. That's the real smash-worthy find:

Every live call that didn't explicitly overridethinking_levelwas a guaranteed HTTP 400.The validation layer wasn't validating the API's contract — it was validating a stale memory of it.

## Why ten green tests never noticed

The suite mocks the Gemini client, as unit tests should:

@patch
(
"
server._get_client
"
)

def
 
test_generate_image_success
(
self
,
 
mock_get_client
):

 
mock_client
.
interactions
.
create
.
return_value
 
=
 
mock_interaction

 
result
 
=
 
generate_image
(
prompt
=
"
test
"
,
 
thinking_level
=
"
medium
"
)

 
self
.
assertIn
(
"
🟢 Image successfully saved!
"
,
 
result
)

Enter fullscreen mode

Exit fullscreen mode

The mock returns success foranyinput — including inputs the real API rejects. The tests correctly proved "the server forwardsmediumfaithfully." Faithfully forwarding an invalid value is still a bug; it's just invisible from inside the mock boundary.

Two conditions had to align for this to ship:

1. A local allowlist duplicated a remote-owned contract.SUPPORTED_THINKING_LEVELSwas a cached copy of a fact only the API owns. Cached copies drift.
2. Every previous live caller happened to override the default.Agents kept requestinghighfor quality — so the broken default and the two phantom values were never exercised.f(x)being called a hundred times tells you nothing aboutf().

## The fix

Two lines of production code, plus the part that actually takes discipline — locking the discovery in so it can't regress:

-SUPPORTED_THINKING_LEVELS = {"minimal", "low", "medium", "high"}

+SUPPORTED_THINKING_LEVELS = {"low", "high"}

- prompt: str, aspect_ratio: str = "1:1", thinking_level: str = "medium"

+ prompt: str, aspect_ratio: str = "1:1", thinking_level: str = "low"

Enter fullscreen mode

Exit fullscreen mode

# New regression test: the live API only accepts low/high for this
# model; medium must now be rejected locally with a readable error.

result
 
=
 
generate_image
(
prompt
=
"
test
"
,
 
thinking_level
=
"
medium
"
)

self
.
assertIn
(
"
Unsupported thinking level 
'
medium
'"
,
 
result
)

Enter fullscreen mode

Exit fullscreen mode

Then the sweep (three tool signatures, docstrings, the server's self-describingget_help, every doc that repeated the wrong values) and a rebuild + push of the published Docker image, which had been shipping the bug to anyone who pulled it.

## Before / after

Before

After

Live call with default params

HTTP 400, every time

🟢 image saved

thinking_level="minimal"
 / 
"medium"

Approved locally, rejected remotely

Rejected locally with the allowed values named

Test suite

10/10 green (bug invisible)

11 assertions incl. contract regression test

Published image 
xbill9/nb2lite-mcp

Shipped the broken default

Rebuilt, pushed, verified live

Elapsed time from first failure to fixed-image-on-Docker-Hub: about ten minutes — because the failing tool call came back as readable text (Allowed values are: low, high) instead of a stack trace. Error messages that name the fix are half the debugging.

## What I learned

1. Mocked tests verify your code; they cannot verify the contract.Keep one cheap live smoke call in the loop — mine now lives in the demo script itself (DEMO_FAST=1 ./demo.sh).
2. Test your defaults specifically.Defaults are the values nobody passes explicitly, so nobody exercises them — they're where contract drift hides longest.
3. A local allowlist of remote-owned values is a drift time bomb.If you pre-validate for better agent-facing errors (worth it!), pin a regression test to the values you'veobservedthe API reject.
4. A demo script is the cheapest end-to-end test you'll ever write.Real credentials, real API, the real happy path — exactly the layer mocks can't reach. Mine paid for itself on its very first execution, before any audience saw it.

## Best Use of Google AI

The whole project is built on Google AI, end to end:

* The server wrapsgemini-3.1-flash-lite-imagethrough theInteractions API— the stateful sessions (store=True+previous_interaction_id) are what make multi-turn image editing work: the demo's edit step adds a neon RAMEN sign tothe exact imagegenerated moments earlier, with pixel-level continuity.
* One of the three consumers is aGoogle ADK agent(LlmAgentongemini-2.5-flash) that imports the server's tools over MCP viaMCPToolset— Gemini calling Gemini, with the bug fix sitting in between.
* The bug itself was a contract mismatch against the live Gemini API, and the fix was verified against it — the 400 error's precise, actionable message (Allowed values are: low, high) is what made this a ten-minute smash.

## Links

* 🐳 Fixed server image:xbill9/nb2lite-mcp
* 📖 Long-form post-mortem:My Demo Script Found a Production Bug on Its First Run
* 🏗️ Architecture:Build One AI Tool Server, Call It From Three Different Agents

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse