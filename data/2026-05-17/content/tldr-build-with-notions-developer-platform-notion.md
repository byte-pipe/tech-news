---
title: Build with Notion’s Developer Platform – Notion
url: https://www.notion.com/product/dev
site_name: tldr
content_file: tldr-build-with-notions-developer-platform-notion
fetched_at: '2026-05-17T06:00:58.937745'
original_url: https://www.notion.com/product/dev
date: '2026-05-17'
description: Sync any data source. Build any agent tool. Orchestrate any agent. No infra required. One shared canvas for your team and agents to work together.
tags:
- tldr
---

Trusted by engineers at

## Sync any data source into Notion.

Continuously upsert external records into a Notion Database with Workers, a declarative schema, and a persistent cursor.

and others

zendeskSync.ts
See example
import { Worker } from "@notionhq/workers";

const worker = new Worker();

const tickets = worker.database("tickets", {
 type: "managed",
 initialTitle: "Support Tickets",
 primaryKeyProperty: "Tickets",
 schema: { properties: {
 "Tickets": Schema.title(),
 "CSAT score": Schema.select([{ name: "Very satisfied" }, ...]),
 "Feature tags": Schema.multiSelect([{ name: "Account access" }, ...]),
 }},
});

worker.sync("ticketsSync", {
 database: tickets,
 schedule: "5m",
 execute: async () => ({
 changes: (await zendesk.tickets.list()).map(t => ({
 type: "upsert" as const,
 key: t.id,
 properties: {
 "Tickets": Builder.title(t.subject),
 "CSAT score": Builder.select(t.csat),
 "Feature tags": Builder.multiSelect(...t.tags),
 },
 })),
 }),
})
Workers > sync:ticketsSync

Connecting. Found 5 new tickets...

## Build any tool for your agents.

Write custom tools for Notion Agents that generate assets, query live data, and hit any API.

Generate assets from your docs
presentationTool.ts
See example
worker.tool("createPresentation", {
	title: "Create Presentation",
	description:
		"Reads a Notion page and creates a PowerPoint presentation from its content. Each heading becomes a new slide. The generated .pptx file is uploaded to the bottom of the page.",
	schema: j.object({
		pageId: j.string()
	}),
	execute: async ({ pageId }, { notion }) => {
		// Fetch page content as markdown and parse into slides
		const pageTitle = await getPageTitle(notion, pageId);
		const markdown = await getPageMarkdown(pageId);
		const slides = groupMarkdownIntoSlides(markdown, pageTitle);

		// Build the .pptx file
		const filename = `${pageTitle}.pptx`;
		const buffer = await buildPresentation(pageTitle, slides);

		// Upload to Notion and append to the page
		await uploadToNotion(notion, pageId, filename, buffer);

		return `Created presentation "${pageTitle}" with ${slides.length + 1} slides (1 title + ${slides.length} content) and added it to the page.`;
	},
});
Workers > tool:createPresentation

 
Query any data warehouse
queryRevenueTool.ts
See example
worker.tool("queryRevenue", {
	title: "Query Revenue",
	description: "Run a SQL query against the deals warehouse table.",
	schema: j.object({
		query: j
			.string()
			.describe("e.g. SELECT SUM(amount) AS revenue WHERE region = 'North America'"),
	}),
	execute: async ({ query }) =>
		snowflake.query(query.replace(/(\s+WHERE|$)/i, " FROM deals$1")),
	});
Workers > tool:queryRevenue

 
Take actions in any app
browserTools.md
Copy the prompt
<!--
Copy and paste this into your coding agent of choice.
-->
Build a worker that lets my Notion agent order food from DoorDash using Browserbase.

I want three tools:

- listFavorites — Returns my saved meals (e.g. "friday night thai" = Pad See Ew + Green Curry from Siam Garden).
- orderFavorite — Takes a meal name, shows me what it's about to order and the estimated total, and asks for confirmation before placing it.
- checkOrder — Returns delivery ETA and driver status.
Generate assets from your docs
presentationTool.ts
See example
worker.tool("createPresentation", {
	title: "Create Presentation",
	description:
		"Reads a Notion page and creates a PowerPoint presentation from its content. Each heading becomes a new slide. The generated .pptx file is uploaded to the bottom of the page.",
	schema: j.object({
		pageId: j.string()
	}),
	execute: async ({ pageId }, { notion }) => {
		// Fetch page content as markdown and parse into slides
		const pageTitle = await getPageTitle(notion, pageId);
		const markdown = await getPageMarkdown(pageId);
		const slides = groupMarkdownIntoSlides(markdown, pageTitle);

		// Build the .pptx file
		const filename = `${pageTitle}.pptx`;
		const buffer = await buildPresentation(pageTitle, slides);

		// Upload to Notion and append to the page
		await uploadToNotion(notion, pageId, filename, buffer);

		return `Created presentation "${pageTitle}" with ${slides.length + 1} slides (1 title + ${slides.length} content) and added it to the page.`;
	},
});
Workers > tool:createPresentation

 

## Trigger Notion workflows from anywhere.

Listen for incoming webhooks from any app, then run workflows with Notion Agents, pages, databases, and external APIs.

Read the docs
→
PR merged
Customer canceled
Candidate signed offer
Contract signed
Issue escalated
PR merged
Customer canceled
Candidate signed offer
Contract signed
Issue escalated
PR merged
Customer canceled
Candidate signed offer
Contract signed
Issue escalated
PR merged
Customer canceled
Candidate signed offer
Contract signed
Issue escalated
PR merged
Customer canceled
Candidate signed offer
Contract signed
Issue escalated
PR merged
Customer canceled
Candidate signed offer
Contract signed
Issue escalated
PR merged
Customer canceled
Candidate signed offer
Contract signed
Issue escalated
PR merged
Customer canceled
Candidate signed offer
Contract signed
Issue escalated
PR merged
Customer canceled
Candidate signed offer
Contract signed
Issue escalated
PR merged
Customer canceled
Candidate signed offer
Contract signed
Issue escalated
worker
.
webhook
(shipPR)
Start experiment
Create incident
Send kudos to team
Create onboarding page
Notify the CS team
Update task status
Page on-call
Update opportunity
Send welcome email
Update customer record
Start experiment
Create incident
Send kudos to team
Create onboarding page
Notify the CS team
Update task status
Page on-call
Update opportunity
Send welcome email
Update customer record
Start experiment
Create incident
Send kudos to team
Create onboarding page
Notify the CS team
Update task status
Page on-call
Update opportunity
Send welcome email
Update customer record
Start experiment
Create incident
Send kudos to team
Create onboarding page
Notify the CS team
Update task status
Page on-call
Update opportunity
Send welcome email
Update customer record
Start experiment
Create incident
Send kudos to team
Create onboarding page
Notify the CS team
Update task status
Page on-call
Update opportunity
Send welcome email
Update customer record

## All of this, on a hosted runtime.

Workers are isolated sandboxes managed by Notion, so the code behind your syncs, tools, and workflows runs on our infra instead of your servers.

Read the docs
→
$
 ntn deploy worker

[build]
 Deploying...

[build]
 Uploading to Notion...

[build]
 Worker updated...

Capabilities:
 
tool queryCustomers

 
tool moreOfficeSnacks

 
sync linearTickets

Alpha

## Bring your favorite agents into Notion.

Use external agents like Claude, Cursor, Decagon, or one you’ve built, in a shared interface for your team and agents.

Join the waitlist
→

### Mention

Collaborate with agents like teammates. @mention them in any page, comment, or chat with them directly.

### Assign

Hand off work to your agents from any task, or trigger them in parallel.

### Orchestrate

Watch agents think, call tools, and act across Notion and other apps with your review and approval when it matters.

### BYO Agent

Bring your in‑house agents into Notion with the External Agents API. Notion gives them triggers, tools, and permissions so they show up as first‑class collaborators on all the same surfaces.

POST
 /sessions/{id}

POST
 /sessions/{id}/messages

GET
 /sessions/{id}/events

## CLI, API, MCP, SDK — LFG.

### Notion CLIBeta

Let coding agents use token‑efficient commands to build and deploy syncs and tools to our Workers runtime.

### Notion API

Turn docs into Markdown and build internal tools with PATs or shared connections.

Read the API docs
→

### Notion MCP

Search, read, and edit pages and databases with up to 91% fewer tokens.

### Notion Agent SDKAlpha

Bring your Agents into any app. Trigger runs via API, keep multi-turn threads, and stream responses in real time.

Join the waitlist
→
import { NotionAgentsClient } from "@notionhq/agents-client";

const client = new NotionAgentsClient();
const agent = await client.agents.agent(id);

await agent.chat({ 
 message: "Hello, World!" 
});

## Any data. Any tool. Any agent. All in Notion.