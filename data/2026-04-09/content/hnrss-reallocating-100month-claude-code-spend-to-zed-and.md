---
title: Reallocating $100/Month Claude Code spend to Zed and OpenRouter – Braw.dev
url: https://braw.dev/blog/2026-04-06-reallocating-100-month-claude-spend/
site_name: hnrss
content_file: hnrss-reallocating-100month-claude-code-spend-to-zed-and
fetched_at: '2026-04-09T19:39:42.893531'
original_url: https://braw.dev/blog/2026-04-06-reallocating-100-month-claude-spend/
date: '2026-04-09'
published_date: '2026-04-06T12:40:28+02:00'
description: With Anthropic altering rate limits, we can find other places to spend our money. I have chosen Zed editor with OpenRouter for maximum flexibility.
tags:
- hackernews
- hnrss
---

Blog
Reallocating $100/Month Claude Code spend to Zed and OpenRouter

# Reallocating $100/Month Claude Code spend to Zed and OpenRouter

April 6, 2026

·
7 min read
Discuss on:

Hacker News

Reddit
Instead of $100/month for Claude, pay $10/month for Zed editor and set up a monthly $90 top up to
OpenRouter. You can use the Zed Agent harness or keep using Claude Code, however you pay API costs
for what you use. When you’re not using, your credits build up rather than missing the usage window.

I’ve been disappointed to feel that I’m hitting Claude limits faster than before. For context, I use
both Claude Code and the Claude desktop app for work and pay $100/month for the privilege
of hitting limits. I’mnot the only one(this was AMD’s senior director of AI) with numerous other reports found over Reddit and Twitter.

My usage pattern is “bursty” so I’m not using the windows all the time throughout the day but find
it incredibly frustrating to hit a limit mid-way through a coding session.

This article is how I’m reallocating that spend to other tools and models while getting more
flexibility at the same time.

## Picking an Agent Harness and Exploring other models

I like options and while Opus is undoubtedly the market leader for agentic coding, there are other
models that I like to use to balance cost and speed depending on the complexity of the task in hand.
I’m looking at how I can use different models with an Agent Harness.

verbose output

An “agent harness” coordinates sending and receiving messages from LLMs, injecting tool defintions
and calling the tools and orchestrating all of this into workflows (including retrying failing
tasks).

Claude Code is an example of such a system. It takes the user message, coordinates reading/writing
files - among other things - and makes calls to the LLM.

## Zed and OpenRouter

Plans:$10 / month -pricing page

You don’t realise how slow/laggy VSCode and the all of the forks are until you try outZed. The builtin agent harness is basic but nice with the ability to follow the
agent around as it modifies files and to add new profiles to customise the agent behaviour. Like
Cursor it shows the context usage and the rules that are being applied to the current session. If
you continue to use Claude Code or other tools like Mistral Vibe, Zed integrates them directly into
the editor using theAgent Client Protocol (ACP)- seesupported agents.

The biggest disadvantage is definitely the lack of extensions compared to VSCode but there are
enough to cover common languages and common tasks.

Zed do offer usage based pricing once you have used up the credits they provide however theirtoken prices are higherthan going directly to the API themselves.
This is why I prefer to use the OpenRouter integration into Zed instead. A nice side benefit is you
get the more native context window sizes. For some reason Zed limits the Gemini 3.1 context to 200k
tokens in their native integration however with OpenRouter you can make use of the full 1M. Their
docs say this may be changed in the future.

### OpenRouter

Edit:
 It has been brought to my attention (thanks to
hhthrowaway1230
 on HackerNews) that
OpenRouter does
charge a 5.5% fee
.

The largest option of models and providers that I know of isOpenRouterand
it’s easy enough to sign up, pre-pay some credits and get an API key.

I don’t like that I have a set window of Anthropic credits. If I use it I have to wait for it to
reset (or pay). But when I’m not using it I’m missing out on that window of opportunity. Instead I
can top up my OpenRouter credits which expire after365 days if unused. Then I can
use the credits when I’m working and save them/roll-over when I’m not.

To minimise data exposure risk, I have chosen not to consent to OpenRouter being able to use
inputs/outputs “to improve the product” (though you get a 1% discount if you do), and I have enabled
the “Zero Data Retention (ZDR) Endpoints Only” in myWorkspace Guardrail settings. You do lose out
on some models here - for example,qwen/qwen3.6-pluswhich is only hosted on Alibaba Cloud - however that’s a small price I’m willing to pay.

## Cursor

Plans:$20 | $60 | $200 / month -pricing page

verbose output

I originally switched from VSCode & Copilot to Cursor in 2025 after experiencing the magic of the
Cursor “Tab” jumping around the editor preempting my next move.

As it moved from autocomplete-on-steroids to more agentic coding, I was thankful to have access to
multiple models to experiment with (this is now also available in Copilot but in the beginning they
were OpenAI only).

I mostly ignored Cursor 2.0 as they put more emphasis on the chat interface however with Cursor 3.0
as a complete rewrite (in Rust like Zed) and focused on Agent orchestration, I am curious to try it
out.

Cursor was (or still semi-is) my preferred editor. As a VSCode fork, all extensions are available.
They were an early adopter of the plan mode -> agent mode workflow and now support a newdebugmodewhich is a more advancedprintstyle
debug that the agent can also interact with.

Cursor also supports different types of rule applications, something I personally love and am
surprised that other agent harnesses haven’t adopted. Most agent harnesses take an “apply
intelligently” approach, trying to let the AI make decisions on when to include a rule based on the
description. But Cursor also offers the ability to only apply to specific files. I know I have rules
that only apply to*.pyfiles, or even**/models.pyetc. I am able to make the most of my
context window by explicitly setting those rules to be added only to certain filepath regexs. It
guarantees their usage

Choosing Cursor you get API rate pricing above the included use in your plan (and you can limit this
so your total spend is limited to $100) but you are still paying minimum $20/month which does not
roll over to the next month.

## Claude Code and OpenRouter

Claude Code is optimized for Anthropic models and may not work correctly with other providers.

I know - I said I’m redirecting fundsawayfrom Anthropic, but it is possible to continue using
the Claude Code agent harness with other models (or even Opus should you want to). We might want to
do this because Claude Code is undeniably a great harness, however we need toconfigure Claude Codeto
use OpenRouter rather than the Anthropic API.

1. First, log out of Claude Code if you have been using it before:claude> /logout
2. Next, set some environment variables to configure the OpenRouter endpoints and which models you
want to use for “Opus”, “Sonnet”, “Haiku” and “SubAgents” (I recommend setting these in your~/.zshrcor~/.bashrcfile so they persist):exportOPENROUTER_API_KEY="<your-openrouter-api-key>"exportANTHROPIC_BASE_URL="https://openrouter.ai/api"exportANTHROPIC_AUTH_TOKEN="$OPENROUTER_API_KEY"exportANTHROPIC_API_KEY=""# Important: Must be explicitly empty# Set these models to whichever model you would like to use on OpenRouterexportANTHROPIC_DEFAULT_OPUS_MODEL="anthropic/claude-opus-4.6"exportANTHROPIC_DEFAULT_SONNET_MODEL="anthropic/claude-sonnet-4.6"exportANTHROPIC_DEFAULT_HAIKU_MODEL="anthropic/claude-haiku-4.5"exportCLAUDE_CODE_SUBAGENT_MODEL="anthropic/claude-opus-4.6"
3. Verify that Claude Code is using your new config (you may need to restart your terminal orsource ~/.zshrc):claude> /statusAuth token: ANTHROPIC_AUTH_TOKENAnthropic base URL: https://openrouter.ai/api

## Other CLI tools like OpenCode + OpenRouter

There are a multitude ofother coding Agent Harnessesthat can be
used from the command line with OpenRouter. I’ve tried a few but none have stuck, here’s the list
for you to try and my brief thoughts on them:

* OpenCode-Typescript- The one I use the most. Good
support for a lot of things. Very popular.
* Crush-Go- I want to like it. It has a distinct
style choice (that I don’t mind). It’s performant. But it’s a pain to configure custom models (all
manual) so annoying when trying out new ones.

Even for popular tools that typically limit you to use their own models like Gemini CLI, often there
are forks which attempt to make it OpenRouter compatible. This is worth checking if you are using
and like a different harness but want to try other models.

I’m now a happy subscriber to Zed for the reasonable
$10/month. I actually also maintain my Cursor subscription for $20/month as I want to see where they
go with their new Cursor 3, agent orchestrator. The other $70 gets auto added to my OpenRouter
credits each month which don’t get lost. They rollover, waiting for me to use them.

If you’re regularly hitting Claude limits and want to give other models a shot (but you can still
use Opus when you need to), I highly recommend giving it a try. You can get started with Zed for
free and load up OpenRouter with $20 worth of credits without any subscription.

Discuss on:

Hacker News

Reddit
Tags:

ai

claude-code
Last updated on

April 9, 2026
Monitor Claude Code Usage With Grafana
