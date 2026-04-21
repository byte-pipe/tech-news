---
title: Anthropic - OpenClaw
url: https://docs.openclaw.ai/providers/anthropic
site_name: hnrss
content_file: hnrss-anthropic-openclaw
fetched_at: '2026-04-21T11:59:49.552056'
original_url: https://docs.openclaw.ai/providers/anthropic
date: '2026-04-21'
description: Anthropic says OpenClaw-style Claude CLI usage is allowed again
tags:
- hackernews
- hnrss
---

# ​Anthropic (Claude)

Anthropic builds the 
Claude
 model family and provides access via an API and
Claude CLI. In OpenClaw, Anthropic API keys and Claude CLI reuse are both
supported. Existing legacy Anthropic token profiles are still honored at
runtime if they are already configured.

Anthropic staff told us OpenClaw-style Claude CLI usage is allowed again, so
OpenClaw treats Claude CLI reuse and 
claude -p
 usage as sanctioned for this
integration unless Anthropic publishes a new policy.
For long-lived gateway hosts, Anthropic API keys are still the clearest and
most predictable production path. If you already use Claude CLI on the host,
OpenClaw can reuse that login directly.
Anthropic’s current public docs:
* Claude Code CLI reference
* Claude Agent SDK overview
* Using Claude Code with your Pro or Max plan
* Using Claude Code with your Team or Enterprise plan
If you want the clearest billing path, use an Anthropic API key instead.
OpenClaw also supports other subscription-style options, including 
OpenAI
Codex
, 
Qwen Cloud Coding Plan
,

MiniMax Coding Plan
, and 
Z.AI / GLM Coding
Plan
.

## ​Option A: Anthropic API key

Best for:
 standard API access and usage-based billing.
Create your API key in the Anthropic Console.

### ​CLI setup

openclaw
 onboard

# choose: Anthropic API key

# or non-interactive

openclaw
 onboard
 --anthropic-api-key
 "$ANTHROPIC_API_KEY"

### ​Anthropic config snippet

{

 env
:
 { 
ANTHROPIC_API_KEY
:
 "sk-ant-..."
 }
,

 agents
:
 { 
defaults
:
 { 
model
:
 { 
primary
:
 "anthropic/claude-opus-4-6"
 } } }
,

}

## ​Thinking defaults (Claude 4.6)

* Anthropic Claude 4.6 models default toadaptivethinking in OpenClaw when no explicit thinking level is set.
* You can override per-message (/think:<level>) or in model params:agents.defaults.models["anthropic/<model>"].params.thinking.
* Related Anthropic docs:Adaptive thinkingExtended thinking
* Adaptive thinking
* Extended thinking

## ​Fast mode (Anthropic API)

OpenClaw’s shared 
/fast
 toggle also supports direct public Anthropic traffic, including API-key and OAuth-authenticated requests sent to 
api.anthropic.com
.

* /fast onmaps toservice_tier: "auto"
* /fast offmaps toservice_tier: "standard_only"
* Config default:

{

 agents
:
 {

 defaults
:
 {

 models
:
 {

 "anthropic/claude-sonnet-4-6"
:
 {

 params
:
 { 
fastMode
:
 true
 }
,

 }
,

 }
,

 }
,

 }
,

}

Important limits:

* OpenClaw only injects Anthropic service tiers for directapi.anthropic.comrequests. If you routeanthropic/*through a proxy or gateway,/fastleavesservice_tieruntouched.
* Explicit AnthropicserviceTierorservice_tiermodel params override the/fastdefault when both are set.
* Anthropic reports the effective tier on the response underusage.service_tier. On accounts without Priority Tier capacity,service_tier: "auto"may still resolve tostandard.

## ​Prompt caching (Anthropic API)

OpenClaw supports Anthropic’s prompt caching feature. This is 
API-only
; legacy Anthropic token auth does not honor cache settings.

### ​Configuration

Use the 
cacheRetention
 parameter in your model config:

Value
Cache Duration
Description
none
No caching
Disable prompt caching
short
5 minutes
Default for API Key auth
long
1 hour
Extended cache

{

 agents
:
 {

 defaults
:
 {

 models
:
 {

 "anthropic/claude-opus-4-6"
:
 {

 params
:
 { 
cacheRetention
:
 "long"
 }
,

 }
,

 }
,

 }
,

 }
,

}

### ​Defaults

When using Anthropic API Key authentication, OpenClaw automatically applies 
cacheRetention: "short"
 (5-minute cache) for all Anthropic models. You can override this by explicitly setting 
cacheRetention
 in your config.

### ​Per-agent cacheRetention overrides

Use model-level params as your baseline, then override specific agents via 
agents.list[].params
.

{

 agents
:
 {

 defaults
:
 {

 model
:
 { 
primary
:
 "anthropic/claude-opus-4-6"
 }
,

 models
:
 {

 "anthropic/claude-opus-4-6"
:
 {

 params
:
 { 
cacheRetention
:
 "long"
 }
,
 // baseline for most agents

 }
,

 }
,

 }
,

 list
:
 [

 { 
id
:
 "research"
,
 default
:
 true
 }
,

 { 
id
:
 "alerts"
,
 params
:
 { 
cacheRetention
:
 "none"
 } }
,
 // override for this agent only

 ]
,

 }
,

}

Config merge order for cache-related params:

1. agents.defaults.models["provider/model"].params
2. agents.list[].params(matchingid, overrides by key)

This lets one agent keep a long-lived cache while another agent on the same model disables caching to avoid write costs on bursty/low-reuse traffic.

### ​Bedrock Claude notes

* Anthropic Claude models on Bedrock (amazon-bedrock/*anthropic.claude*) acceptcacheRetentionpass-through when configured.
* Non-Anthropic Bedrock models are forced tocacheRetention: "none"at runtime.
* Anthropic API-key smart defaults also seedcacheRetention: "short"for Claude-on-Bedrock model refs when no explicit value is set.

## ​1M context window (Anthropic beta)

Anthropic’s 1M context window is beta-gated. In OpenClaw, enable it per model
with 
params.context1m: true
 for supported Opus/Sonnet models.

{

 agents
:
 {

 defaults
:
 {

 models
:
 {

 "anthropic/claude-opus-4-6"
:
 {

 params
:
 { 
context1m
:
 true
 }
,

 }
,

 }
,

 }
,

 }
,

}

OpenClaw maps this to 
anthropic-beta: context-1m-2025-08-07
 on Anthropic
requests.

This only activates when 
params.context1m
 is explicitly set to 
true
 for
that model.

Requirement: Anthropic must allow long-context usage on that credential.

Note: Anthropic currently rejects 
context-1m-*
 beta requests when using
legacy Anthropic token auth (
sk-ant-oat-*
). If you configure

context1m: true
 with that legacy auth mode, OpenClaw logs a warning and
falls back to the standard context window by skipping the context1m beta
header while keeping the required OAuth betas.

## ​Claude CLI backend

The bundled Anthropic 
claude-cli
 backend is supported in OpenClaw.

* Anthropic staff told us this usage is allowed again.
* OpenClaw therefore treats Claude CLI reuse andclaude -pusage as
sanctioned for this integration unless Anthropic publishes a new policy.
* Anthropic API keys remain the clearest production path for always-on gateway
hosts and explicit server-side billing control.
* Setup and runtime details are in/gateway/cli-backends.

## ​Notes

* Anthropic’s public Claude Code docs still document direct CLI usage such asclaude -p, and Anthropic staff told us OpenClaw-style Claude CLI usage is
allowed again. We are treating that guidance as settled unless Anthropic
publishes a new policy change.
* Anthropic setup-token remains available in OpenClaw as a supported token-auth path, but OpenClaw now prefers Claude CLI reuse andclaude -pwhen available.
* Auth details + reuse rules are in/concepts/oauth.

## ​Troubleshooting

401 errors / token suddenly invalid

* Anthropic token auth can expire or be revoked.
* For new setup, migrate to an Anthropic API key.

No API key found for provider “anthropic”

* Auth isper agent. New agents don’t inherit the main agent’s keys.
* Re-run onboarding for that agent, or configure an API key on the gateway
host, then verify withopenclaw models status.

No credentials found for profile 
anthropic:default

* Runopenclaw models statusto see which auth profile is active.
* Re-run onboarding, or configure an API key for that profile path.

No available auth profile (all in cooldown/unavailable)

* Checkopenclaw models status --jsonforauth.unusableProfiles.
* Anthropic rate-limit cooldowns can be model-scoped, so a sibling Anthropic
model may still be usable even when the current one is cooling down.
* Add another Anthropic profile or wait for cooldown.

More: 
/gateway/troubleshooting
 and 
/help/faq
.