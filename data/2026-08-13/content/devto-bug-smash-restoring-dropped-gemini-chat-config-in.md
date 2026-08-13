---
title: 'Bug Smash: restoring dropped Gemini chat config in Sentry''s JavaScript SDK - DEV Community'
url: https://dev.to/zkasuran/bug-smash-restoring-dropped-gemini-chat-config-in-sentrys-javascript-sdk-2n9a
site_name: devto
content_file: devto-bug-smash-restoring-dropped-gemini-chat-config-in
fetched_at: '2026-08-13T11:41:40.398040'
original_url: https://dev.to/zkasuran/bug-smash-restoring-dropped-gemini-chat-config-in-sentrys-javascript-sdk-2n9a
author: Asuran
date: '2026-08-12'
description: 'This is a submission for DEV''s Summer Bug Smash: Clear the Lineup powered by Sentry. ... Tagged with devchallenge, bugsmash, javascript, ai.'
tags: '#devchallenge, #bugsmash, #javascript, #ai'
---

Summer Bug Smash: Clear the Lineup 🐛🛹

This is a submission forDEV's Summer Bug Smash: Clear the Lineuppowered bySentry.

## Project Overview

Sentry's JavaScript SDK auto-instruments Google GenAI so every Gemini call shows up as a span in your trace, with the model, the generation config and the system instruction attached. This entry fixes a silent regression in that instrumentation: chat calls were dropping the configuration they ran with, so the trace no longer told you how the model was set up. The fix is one focused change in@sentry/server-utils. It ships with unit tests. I verified it end to end against the live Gemini API.

## Bug Fix or Performance Improvement

This is a bug fix forgetsentry/sentry-javascript#20086, filed by a Sentry maintainer.

The Google GenAI SDK splits a chat into two steps. Firstchats.create({ model, config })builds a local chat object, whereconfigholds temperature, top_p, top_k, max output tokens, the penalties, the tool list and the system instruction. That step does not call the model. Thenchat.sendMessage(...)andchat.sendMessageStream(...)are the real model calls. The SDK reuses the create-time config for every one of them.

Sentry used to emit a span forchats.create()and read the config off it. A refactor (#19990) removed that span because it was not a real model call, which was correct, but the config it captured went away with it. From then on thechat.sendMessage()andchat.sendMessageStream()spans only saw the per-call message, sogen_ai.request.temperature,top_p,top_k,max_tokens, the penalties,available_toolsandgen_ai.system_instructionssilently vanished from the trace. That PR even called out the risk in its own description and left it as a follow-up, which is exactly this issue.

Root cause: the deep proxy that instruments the client re-proxies the chat object returned bychats.create()but discards that call's arguments, so the code that builds the message spans never sees the config.

## Code

The fix, as a PR:getsentry/sentry-javascript#23316, branchfix/google-genai-chat-config-attrs.

The fix captures thechats.create()arguments and weldsmodelplusconfigonto each message span. The create-time config is the default. A per-message config replaces it wholesale for that request, matching how the@google/genaiSDK resolves config asparams.config ?? chat.config.

function
 
mergeChatCreateParams
(

 
chatCreateParams
:
 
Record
<
string
,
 
unknown
>
 
|
 
undefined
,

 
callParams
:
 
Record
<
string
,
 
unknown
>
 
|
 
undefined
,

):
 
Record
<
string
,
 
unknown
>
 
|
 
undefined
 
{

 
if 
(
!
chatCreateParams
)
 
{

 
return
 
callParams
;

 
}

 
const
 
merged
:
 
Record
<
string
,
 
unknown
>
 
=
 
{
 
...
callParams
 
};

 
if 
(
!
(
'
model
'
 
in
 
merged
)
 
&&
 
'
model
'
 
in
 
chatCreateParams
)
 
{

 
merged
.
model
 
=
 
chatCreateParams
.
model
;

 
}

 
// @google/genai sends `params.config ?? chat.config`, so a per-message config replaces the

 
// create-time config wholesale rather than merging into it. Fall back to the create-time config

 
// only when the message did not carry one, otherwise the span reports fields that were not sent.

 
const
 
callConfig
 
=
 
asConfigObject
(
callParams
?.
config
);

 
if 
(
!
callConfig
)
 
{

 
const
 
createConfig
 
=
 
asConfigObject
(
chatCreateParams
.
config
);

 
if 
(
createConfig
)
 
{

 
merged
.
config
 
=
 
createConfig
;

 
}

 
}

 
return
 
merged
;

}

Enter fullscreen mode

Exit fullscreen mode

The proxy now threads that context. When it re-proxies the chat returned bychats.create(), it passes the create arguments down.instrumentMethodbuilds its span attributes from the merged params:

// in createDeepProxy, when re-proxying the chats.create() result:

return
 
createDeepProxy
(
result
 
as
 
object
,
 
instrumentedMethod
.
proxyResultPath
,
 
options
,
 
args
[
0
]);

// in instrumentMethod:

const
 
attributeParams
 
=
 
mergeChatCreateParams
(
chatCreateParams
,
 
params
);

const
 
requestAttributes
 
=
 
extractRequestAttributes
(
operationName
,
 
attributeParams
,
 
context
);

Enter fullscreen mode

Exit fullscreen mode

The real method still runs on its original arguments, so nothing about the request to Google changes. Non-chat calls likemodels.generateContentnever receive the chat context, so they are untouched.

## My Improvements

I added the merge helper, threaded the create context through the proxy and the two branches ofinstrumentMethod(streaming and non-streaming). I left the createhistoryoff the message spans on purpose since it is conversation seed, not per-message input.

I wrote a new test file with four cases: config welded ontosendMessagespans, config welded ontosendMessageStreamspans, a per-message config replacing the create config, plus no leakage ontomodels.generateContentspans. On the unfixed code three of the four fail because the attributes areundefined. On the fix all four pass.

Gates, all real: the@sentry/server-utilssuite went from 38 files / 335 tests to 39 files / 339 tests, all passing.oxlint --type-awareandoxfmt --checkare clean on the change.tscon the source types passes. The onlytsctest-config errors are pre-existing ones in unrelated files that this change never touches.

## Best Use of Sentry

This is the kind of fix that makes AI tracing trustworthy. Sentry's AI Agents view leans on thegen_ai.*span attributes to show how each model call was configured. A chat span that is missing its temperature, its token limit and its system instruction hides the settings that actually shaped the answer. When you are debugging a bad response or a cost spike, "what config was this call running with" is the first question. Before this fix the chat spans could not answer it. Restoring the attributes puts the full picture back in the trace, consistent with what the non-chatgenerateContentspans already report.

## Best Use of Google AI

I reproduced the bug and the fix against the real Gemini API, not a mock. The script builds a real@google/genaiv1.20.0 client, wraps it with the actual SDK instrumentation, runs it through a real Sentry client with tracing, then reads the captured span. It callschats.createwith a full config and a system instruction, thensendMessagewith a prompt.

model: gemini-2.5-flash
create config: temperature 0.8, topP 0.9, topK 40, maxOutputTokens 512,
 systemInstruction "You are a friendly robot who likes to be funny."
prompt: "Tell me a one-line joke about debugging."

BEFORE the fix (chat.sendMessage span):
 PRESENT gen_ai.request.model = "gemini-2.5-flash"
 MISSING gen_ai.request.temperature (dropped)
 MISSING gen_ai.request.top_p (dropped)
 MISSING gen_ai.request.top_k (dropped)
 MISSING gen_ai.request.max_tokens (dropped)
 MISSING gen_ai.system_instructions (dropped)

AFTER the fix (chat.sendMessage span):
 PRESENT gen_ai.request.model = "gemini-2.5-flash"
 PRESENT gen_ai.request.temperature = 0.8
 PRESENT gen_ai.request.top_p = 0.9
 PRESENT gen_ai.request.top_k = 40
 PRESENT gen_ai.request.max_tokens = 512
 PRESENT gen_ai.system_instructions = "[{\"type\":\"text\",\"content\":\"You are a friendly robot who likes to be funny.\"}]"

Enter fullscreen mode

Exit fullscreen mode

Both runs got a real Gemini reply. The AFTER run answered: "Why did the programmer quit his job debugging code? Because he kept finding himself in an infinite loop." Same call, same live model. The fix is the difference between a trace that records the chat configuration and one that quietly loses it.

## AI disclosure

AI assistance (Claude, Anthropic) was used in developing this change. The design, the review and the verification were done by me. Before submitting I ran the@sentry/server-utilstest suite (339 passing), confirmed the new test fails on the unfixed code and passes on the fix, ranoxlint --type-aware,oxfmt --checkandtscon the source types, then did a real Geminichats.createplussendMessagerun showing the attributes dropped before the fix and present after.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse