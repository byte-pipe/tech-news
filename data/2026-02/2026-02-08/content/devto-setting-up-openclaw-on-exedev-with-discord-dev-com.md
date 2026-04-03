---
title: Setting Up OpenClaw on exe.dev with Discord - DEV Community
url: https://dev.to/bdougieyo/setting-up-openclaw-on-exedev-with-discord-27n
site_name: devto
content_file: devto-setting-up-openclaw-on-exedev-with-discord-dev-com
fetched_at: '2026-02-08T15:31:11.176299'
original_url: https://dev.to/bdougieyo/setting-up-openclaw-on-exedev-with-discord-27n
author: Brian Douglas
date: '2026-02-02'
description: I'll be honest—when I first heard about Clawdbot (now rebranded as OpenClaw) a few weeks back, I had... Tagged with ai, llm, coding.
tags: '#ai, #llm, #coding'
---

I'll be honest—when I first heard about Clawdbot (now rebranded as OpenClaw) a few weeks back, I had that immediate security alarm going off in my head. An AI agent running with Discord permissions, making API calls, potentially accessing who knows what? As someone who's spent years in developer experience, the threat model here was... concerning.

But then I started seeing folks in the community actually using it—spinning up Digital Ocean droplets, deploying to Railway.

So I decided to try it, but on my terms: isolated, observable, and disposable. Which is why I chose exe.dev, but this can work on the platform of your choice.

## Why exe.dev?

I've known about exe.dev for months—it's this clever service that gives you ephemeral VMs that you can spin up and tear down instantly. Perfect for experiments you're not 100% sure about. If OpenClaw does something weird or I misconfigure something, I just nuke the VM and start fresh. No damage to my local machine, no persistent infrastructure to maintain.

Think of it as a playground where mistakes are cheap.

💡 Pro Tip: Add Telemetry from Day One

Before you start, consider addingtapesas a proxy layer. It records every API call OpenClaw makes, giving you visibility into prompts, token usage, and agent behavior. Theofficial guidehas details, or follow the optional setup in Step 7 below. Trust me—you'll want this data when debugging why your agent did something unexpected.

## What You'll Need

Before we dive in, grab these:

* Anexe.devaccount
* A Discord bot token from theDiscord Developer Portal
* An Anthropic API key if you want to use Claude (optional, but recommended)

## The Fast Path: Using the Template

Here's where exe.dev really shines. They have an OpenClaw template that handles most of the setup:

1. Navigate toexe.new/openclaw
2. Drop in your API keys when prompted
3. Let Shelley (exe.dev's setup assistant) do the heavy lifting

I'm going to walk you through the manual setup though, because understanding what's actually happening is half the value here.

## The Manual Route (More Learning, Same Result)

### Create Your VM

ssh exe.dev new

# You'll get a VM name like: curious-tesla-8432

ssh curious-tesla-8432.exe.xyz

Enter fullscreen mode

Exit fullscreen mode

You're now inside an Ubuntu VM that exists just for you, accessible from anywhere.

### Install OpenClaw

This is surprisingly straightforward:

# Get the system ready

sudo
apt-get update

sudo
apt-get
install

-y
 git curl jq ca-certificates openssl nginx

# Install OpenClaw via their script

curl
-fsSL
 https://openclaw.bot/install.sh | bash

# Run the onboarding (we're skipping interactive prompts)

openclaw onboard
--non-interactive

--accept-risk

Enter fullscreen mode

Exit fullscreen mode

That--accept-riskflag made me pause. It's OpenClaw's way of acknowledging that yes, you're running an AI agent with real permissions. I appreciate the directness.

### Configure Nginx as a Reverse Proxy

OpenClaw runs on port 18789 internally, but we want to access it via standard web ports. This is where nginx comes in.

Edit/etc/nginx/sites-enabled/default:

server

{


listen

80

default_server
;


listen

[::]:80

default_server
;


listen

8000
;


listen

[::]:8000
;


server_name

_
;


location

/

{


proxy_pass

http://127.0.0.1:18789
;


proxy_http_version

1.1
;


# WebSocket support - crucial for real-time updates


proxy_set_header

Upgrade

$http_upgrade
;


proxy_set_header

Connection

"upgrade"
;


# Standard proxy headers


proxy_set_header

Host

$host
;


proxy_set_header

X-Real-IP

$remote_addr
;


proxy_set_header

X-Forwarded-For

$proxy_add_x_forwarded_for
;


proxy_set_header

X-Forwarded-Proto

$scheme
;


# Long timeouts for agent tasks that might run a while


proxy_read_timeout

86400s
;


proxy_send_timeout

86400s
;


}

}

Enter fullscreen mode

Exit fullscreen mode

Apply the changes:

sudo
systemctl restart nginx

Enter fullscreen mode

Exit fullscreen mode

### Connect Your Discord Bot

Now for the fun part. Edit~/.openclaw/openclaw.jsonand add your Discord credentials:

{


"channels"
:

{


"discord"
:

{


"enabled"
:

true
,


"token"
:

"YOUR_DISCORD_BOT_TOKEN"


}


}

}

Enter fullscreen mode

Exit fullscreen mode

Restart the gateway to pick up the changes:

openclaw gateway restart

Enter fullscreen mode

Exit fullscreen mode

## The Pairing Dance (This Tripped Me Up)

When I first tried to access the dashboard, I got this cryptic message:

disconnected (1008): pairing required

Turns out OpenClaw uses a device pairing system to prevent unauthorized access. Smart, but not immediately obvious.

Here's how to fix it:

# See what's waiting for approval

openclaw devices list

Enter fullscreen mode

Exit fullscreen mode

You'll see something like:

Pending:
 - id: abc123
 browser: Chrome
 requested: 2 minutes ago

Enter fullscreen mode

Exit fullscreen mode

Approve it:

openclaw devices approve abc123

Enter fullscreen mode

Exit fullscreen mode

Now refresh your browser. You should be connected.

## Access Your Dashboard

Your OpenClaw dashboard lives at:

https://<vm-name>.exe.xyz/?token=<your-gateway-token>

Enter fullscreen mode

Exit fullscreen mode

Find your token in~/.openclaw/openclaw.jsonundergateway.auth.token. I bookmarked this URL because I reference it constantly.

## Verify Everything Works

openclaw health

Enter fullscreen mode

Exit fullscreen mode

You should see confirmation that Discord is connected and your agents are running:

Discord: ok (@yourbotname)
Agents: main (default)

Enter fullscreen mode

Exit fullscreen mode

This is your health check. Anytime something feels off, run this first.

## Optional: Route Through Tapes for Observability

Here's where my Continue background kicks in. I want to see what API calls OpenClaw is making, so I route everything throughtapes—Anthropic's proxy tool for inspecting and recording API interactions.

Start tapes:

tapes serve
\


--provider
 anthropic
\


--upstream

"https://api.anthropic.com"

\


--proxy-listen

"0.0.0.0:8080"

\


--sqlite

"./tapes.db"

Enter fullscreen mode

Exit fullscreen mode

Update~/.openclaw/openclaw.json:

{


"providers"
:

{


"anthropic"
:

{


"baseUrl"
:

"http://localhost:8080"


}


}

}

Enter fullscreen mode

Exit fullscreen mode

Restart:openclaw gateway restart

Now every Claude API call is logged totapes.db. You can inspect prompts, responses, token usage—everything. This level of observability is crucial when you're evaluating AI tooling.

## Things That Surprised Me

1. The pairing system actually works well- Once I understood it, I appreciated having explicit device approval
2. Config persistence is fragile- Some OpenClaw commands will overwrite your config. Always backup~/.openclaw/openclaw.jsonbefore running setup commands
3. It's genuinely useful- Having a Discord bot that can reason about context and execute tasks is different from slash commands or simple bots

## Troubleshooting Guide

### "pairing required" won't go away

openclaw devices list
openclaw devices approve <
id
>

Enter fullscreen mode

Exit fullscreen mode

Refresh your browser after approving.

### Discord shows offline

* Double-check your bot token in the config
* Verify the bot was added to your server with the right permissions
* Runopenclaw doctorfor diagnostics

### Gateway won't start

openclaw gateway status
# Check what's wrong

openclaw logs
# See error details

openclaw gateway restart
# Try restarting

Enter fullscreen mode

Exit fullscreen mode

## Quick Reference Commands

Command

What It Does

openclaw health

Connection status check

openclaw devices list

Show paired/pending devices

openclaw devices approve <id>

Approve a new device

openclaw gateway restart

Restart the gateway process

openclaw doctor

Run full diagnostics

openclaw logs

View gateway logs

## Final Thoughts

Running OpenClaw on exe.dev turned out to be the perfect middle ground. I got to experiment with AI agents in Discord without compromising my local environment, and I could observe everything happening via tapes.

Is it production-ready for your use case? That depends on what you're building. But as a tool for understanding how autonomous AI agents operate, how they handle context, and what the developer experience looks like? It's been genuinely educational.

The security concerns I had initially? Still valid. But now they're informed concerns rather than fear-based ones. And that's the difference between avoiding technology and understanding its tradeoffs.

Guide based on OpenClaw 2026.1.29 running on exe.dev. If you try this and run into issues, reach out—I'm probably debugging the same thing.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
