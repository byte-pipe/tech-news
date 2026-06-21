---
title: Temporary Cloudflare Accounts for AI agents
url: https://blog.cloudflare.com/temporary-accounts/
site_name: hackernews_api
content_file: hackernews_api-temporary-cloudflare-accounts-for-ai-agents
fetched_at: '2026-06-21T11:06:18.957314'
original_url: https://blog.cloudflare.com/temporary-accounts/
author: farhadhf
date: '2026-06-20'
published_date: 2026-06-19T14:00+01:00
description: The moment an agent needs to deploy something, it slams face-first into a wall built for humans. Today we're rolling out Temporary Accounts on Cloudflare Workers. Any agent can now run wrangler deploy — temporary and get a live Worker in seconds.
tags:
- hackernews
- trending
---

# Temporary Cloudflare Accounts for AI agents

2026-06-19

* Sid Chatterjee
* Celso Martinho
* Brendan Irvine-Broque
4 min read

Everyone's writing code with AI agents today. But the moment an agent needs to deploy something — and needs to sign up and create an account — it slams face-first into a wall built for humans: a browser-based OAuth flow, a dashboard to click through, an API token to copy-paste, a multi-factor authentication prompt to satisfy. For an interactive copilot sitting next to a developer, that's annoying. For a background agent, it's a hard stop.

Today we're rolling out Temporary Cloudflare Accounts for Agents.

Agents can now deploywebsites,APIs, andagentsright away, without first needing to sign up for an account.

Any agent can now runwrangler deploy --temporaryand deploy a Worker to Cloudflare. This temporary deployment stays live for 60 minutes, during which time you can claim the temporary account, making it permanently your own. If you don't, it expires on its own.

Our goal? Let your agent code and ship.

## Why frictionless deployments matter for AI agents

Frictionless temporary accounts matter more than it might first seem:

* Background AI sessions have no human in the loop, and are becoming the norm. Any auth step that needs a browser, a copy-paste, or "click here in 60 seconds" means an agent gets stuck and may choose to deploy elsewhere.
* Trial-and-error is the agent's superpower. Agents need a tight write → deploy → verify loop. They need cheap, throwaway deployment targets, so they can curl their own output and decide whether they got it right.
* Agent platforms are building their own ways for deploying code to "just work" without extra steps or credentials. People are starting to expect that this process just works, without the need to sign up for other services that they've not used before or heard of.

## How it works

Temporary accounts are built aroundWrangler, our Developer Platform command-line interface (CLI) tool that lets developers bootstrap new projects, manage their configurations and resources, and deploy and update them.

Wrangler usage is widelydocumentedonline and agents know how to use it very well. But if you hadn’t yet signed in and granted Wrangler permission to your Cloudflare account, when the agent tried to deploy, it would get stuck at the sign-up and authentication step. And you might rightly ask: How do agents and LLMs know that this new--temporaryflag in Wrangler exists, so that they actually use it without a human explicitly telling them to do so?

To solve this, we updated Wrangler to prompt the agent with a message that tells it about the--temporaryflag:

When the agent discovers this, and then runswrangler deployagain with the--temporaryflag, Cloudflare provisions a temporary account for the agent to use, gives Wrangler an API token to work with, and provides a claim URL that the agent can give back to the human.

## Let’s go over every step of the flow

### Deploying and iterating on a new project

Make sure you’re using the latestWrangler release, fire up your favorite coding agent, and write a prompt to deploy a "hello world" app in build mode:

Make a very simple hello world Cloudflare Worker in TypeScript and deploy it using wrangler, don't ask me questions, do the best you can

The agent will run wrangler, pick up the--temporaryflag from the output messages, build your script, and deploy it instantly, no human in the loop required:

As you can see, the agent wrote the script, deployed it using the--temporaryflag, curled the preview link it got from the output, and verified that the result matches the code.

This is great, but agentic coding is often not about one single deployment. A session can go through a cycle of multiple code changes. This is not a problem: the agent can iterate on the Worker script and redeploy the changes as many times as it wants (within the 60-minute claim window). Type this prompt:

Now change hello world to "hello cloudflare" and redeploy

Look at the agent changing the source code, reusing the previously created temporary account, redeploying a new version and rechecking the result:

### Claiming the account

At any point, you can claim the temporary account and make it yours permanently. When you click the claim link you will be taken to a page where you can either sign up for or sign in to Cloudflare, and then claim the temporary account that your Worker was deployed to. This includes claiming not just Workers, but resources like databases and other bindings, too.

If you do not claim these temporary accounts within 60 minutes, they will be automatically deleted.

## The road to frictionless agentic deployments

This is just one way we’re eliminating the signup barrier for agents. We recentlyannounced a partnership with Stripeand a new protocol we co-designed that lets agents provision Cloudflare on behalf of their users — creating an account, starting a subscription, registering a domain, and getting an API token to deploy code, with no copy-pasting tokens or entering credit card details. Last month, we collaborated with WorkOS on the launch ofauth.md, which anyone can adopt, to let agents provision new accounts using well-established, existing OAuth standards.

There’s a ton going on in this space, and we’re excited to keep making it easier for agents to use Cloudflare, and for developers to make their own appsagent-ready. Temporary accounts are one more step toward frictionless agentic deployments — stay tuned for more.

Temporary accounts have some limitations, and their capabilities may change over time; check thedeveloper documentationfor more information and then go build something. Point your agent at Cloudflare, see how far it gets, and tell us what we can improve or what delights you — share what you’ve built onXor hop into theCloudflare Community.

 
 
Agents
Wrangler
AI
Cloudflare Workers