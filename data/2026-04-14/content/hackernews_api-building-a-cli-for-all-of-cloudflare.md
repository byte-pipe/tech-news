---
title: Building a CLI for all of Cloudflare
url: https://blog.cloudflare.com/cf-cli-local-explorer/
site_name: hackernews_api
content_file: hackernews_api-building-a-cli-for-all-of-cloudflare
fetched_at: '2026-04-14T11:57:18.064503'
original_url: https://blog.cloudflare.com/cf-cli-local-explorer/
author: soheilpro
date: '2026-04-13'
published_date: '2026-04-13T14:29:45.821Z'
description: We’re introducing cf, a new unified CLI designed for consistency across the Cloudflare platform, alongside Local Explorer for debugging local data. These tools simplify how developers and AI agents interact with our nearly 3,000 API operations.
tags:
- hackernews
- trending
---

# Building a CLI for all of Cloudflare

2026-04-13

* Matt “TK” Taylor
* Dimitri Mitropoulos
* Dan Carter
6 min read

Cloudflare has a vast API surface. We have over 100 products, and nearly 3,000 HTTP API operations.

Increasingly, agents are the primary customer of our APIs. Developers bring their coding agents to build and deployapplications,agents, andplatformsto Cloudflare, configure their account, and query our APIs for analytics and logs.

We want to make every Cloudflare product available in all of the ways agents need. For example, we now make Cloudflare’s entire API available in a single Code Mode MCP server that usesless than 1,000 tokens. There’s a lot more surface area to cover, though:CLI commands.Workers Bindings— including APIs for local development and testing.SDKsacross multiple languages. Ourconfiguration file.Terraform.Developer docs.API docsand OpenAPI schemas.Agent Skills.

Today, many of our products aren’t available across every one of these interfaces. This is particularly true of our CLI —Wrangler. Many Cloudflare products have no CLI commands in Wrangler. And agents love CLIs.

So we’ve been rebuilding Wrangler CLI, to make it the CLI for all of Cloudflare. It provides commands for all Cloudflare products, and lets you configure them together using infrastructure-as-code.

Today we’re sharing an early version of what the next version of Wrangler will look like as a technical preview. It’s very early, but we get the best feedback when we work in public.

You can try the Technical Preview today by runningnpx cf. Or you can install it globally by runningnpm install -g cf.

Right now, cf provides commands for just a small subset of Cloudflare products. We’re already testing a version of cf that supports the entirety of the Cloudflare API surface — and we will be intentionally reviewing and tuning the commands for each product, to have output that is ergonomic for both agents and humans. To be clear, this Technical Preview is just a small piece of the future Wrangler CLI. Over the coming months we will bring this together with the parts of Wrangler you know and love.

To build this in a way that keeps in sync with the rapid pace of product development at Cloudflare, we had to create a new system that allows us to generate commands, configuration, binding APIs, and more.

## Rethinking schemas and our code generation pipeline from first principles

We already generate the CloudflareAPI SDKs,Terraform provider, andCode Mode MCP serverbased on the OpenAPI schema for Cloudflare API. But updating our CLI, Workers Bindings, wrangler.jsonc configuration, Agent Skills, dashboard and docs is still a manual process. This was already error-prone, required too much back and forth, and wouldn’t scale to support the whole Cloudflare API in the next version of our CLI.

To do this, we needed more than could be expressed in an OpenAPI schema. OpenAPI schemas describe REST APIs, but we have interactive CLI commands that involve multiple actions that combine both local development and API requests, Workers bindings expressed as RPC APIs, along with Agent Skills and documentation that ties this all together.

We write a lot of TypeScript at Cloudflare. It’s the lingua franca of software engineering. And we keep finding that it just works better to express APIs in TypeScript — as we do withCap n’ Web,Code Mode, and theRPC systembuilt into the Workers platform.

So we introduced a new TypeScript schema that can define the full scope of APIs, CLI commands and arguments, and context needed to generate any interface. The schema format is “just” a set of TypeScript types with conventions, linting, and guardrails to ensure consistency. But because it is our own format, it can easily be adapted to support any interface we need, today or in the future, while stillalsobeing able to generate an OpenAPI schema:

To date most of our focus has been at this layer — building the machine we needed, so that we can now start building the CLI and other interfaces we’ve wanted for years to be able to provide. This lets us start to dream bigger about what we could standardize across Cloudflare and make better for Agents — especially when it comes to context engineering our CLI.

## Agents and CLIs — consistency and context engineering

Agents expect CLIs to be consistent. If one command uses<command> infoas the syntax for getting information about a resource, and another uses<command> get, the agent will expect one and call a non-existent command for the other. In a large engineering org of hundreds or thousands of people, and with many products, manually enforcing consistency through reviews is Swiss cheese. And you can enforce it at the CLI layer, but then naming differs between the CLI, REST API and SDKs, making the problem arguably worse.

One of the first things we’ve done is to start creating rules and guardrails, enforced at the schema layer. It’s alwaysget, neverinfo. Always--force, never--skip-confirmations. Always--json, never--format, and always supported across commands.

Wrangler CLI is also fairly unique — it provides commands and configuration that can work with both simulated local resources, or remote resources, likeD1 databases,R2 storage buckets, andKV namespaces. This means consistent defaults matter even more. If an agent thinks it’s modifying a remote database, but is actually adding records to local database, and the developer is using remote bindings to develop locally against a remote database, their agent won’t understand why the newly-added records aren’t showing up when the agent makes a request to the local dev server. Consistent defaults, along with output that clearly signals whether commands are applied to remote or local resources, ensure agents have explicit guidance.

## Local Explorer — what you can do remotely, you can now do locally

Today we are also releasing Local Explorer, a new feature available in open beta in both Wrangler and the Cloudflare Vite plugin.

Local Explorer lets you introspect the simulated resources that your Worker uses when you are developing locally, includingKV,R2, D1,Durable ObjectsandWorkflows. The same things you can do via the Cloudflare API and Dashboard with each of these, you can also do entirely locally, powered by the same underlying API structure.

For years we’vemade a bet on fully local development— not just for Cloudflare Workers, but for the entire platform. When you use D1, even though D1 is a hosted, serverless database product, you can run your database and communicate with it via bindings entirely locally, without any extra setup or tooling. ViaMiniflare, our local development platform emulator, the Workers runtime provides the exact same APIs in local dev as in production, and uses a local SQLite database to provide the same functionality. This makes it easy to write and run tests that run fast, without the need for network access, and work offline.

But until now, working out what data was stored locally required you to reverse engineer, introspect the contents of the.wrangler/statedirectory, or install third-party tools.

Now whenever you run an app with Wrangler CLI or the Cloudflare Vite plugin, you will be prompted to open the local explorer (keyboard shortcute). This provides you with a simple, local interface to see what bindings your Worker currently has attached, and what data is stored against them.

When you build using Agents, Local Explorer is a great way to understand what the agent is doing with data, making the local development cycle much more interactive. You can turn to Local Explorer anytime you need to verify a schema, seed some test records, or just start over andDROP TABLE.

Our goal here is to provide a mirror of the Cloudflare API that only modifies local data, so that all of your local resources are available via the same APIs that you use remotely. And by making the API shape match across local and remote, when you run CLI commands in the upcoming version of the CLI and pass a--localflag, the commands just work. The only difference is that the command makes a request to this local mirror of the Cloudflare API instead.

Starting today, this API is available at/cdn-cgi/explorer/apion any Wrangler- or Vite Plugin- powered application. By pointing your agent at this address, it will find an OpenAPI specification to be able to manage your local resources for you, just by talking to your agent.

## Tell us your hopes and dreams for a Cloudflare-wide CLI

Now that we have built the machine, it’s time to take the best parts of Wrangler today, combine them with what’s now possible, and make Wrangler the best CLI possible for using all of Cloudflare.

You can try the technical preview today by runningnpx cf. Or you can install it globally by running npminstall -g cf.

With this very early version, we want your feedback — not just about what the technical preview does today, but what you want from a CLI for Cloudflare’s entire platform. Tell us what you wish was an easy one-line CLI command but takes a few clicks in our dashboard today. What you wish you could configure inwrangler.jsonc— like DNS records or Cache Rules. And where you’ve seen your agents get stuck, and what commands you wish our CLI provided for your agent to use.

Jump into theCloudflare Developers Discordand tell us what you’d like us to add first to the CLI, and stay tuned for many more updates soon.

Thanks to Emily Shen for her valuable contributions to kicking off the Local Explorer project.

Cloudflare's connectivity cloud protects
entire corporate networks
, helps customers build
Internet-scale applications efficiently
, accelerates any
website or Internet application
,
wards off DDoS attacks
, keeps
hackers at bay
, and can help you on
your journey to Zero Trust
.
Visit
1.1.1.1
 from any device to get started with our free app that makes your Internet faster and safer.
To learn more about our mission to help build a better Internet,
start here
. If you're looking for a new career direction, check out
our open positions
.


Developers
Developer Platform
Cloudflare Workers
Product News
D1
API
Agents Week
