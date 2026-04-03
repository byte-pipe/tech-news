---
title: 'Advent of AI 2025 - Day 17: Building a Wishlist App with Goose and MCP-UI - DEV Community'
url: https://dev.to/nickytonline/advent-of-ai-2025-day-17-building-a-wishlist-app-with-goose-and-mcp-ui-330l
site_name: devto
fetched_at: '2026-01-02T11:07:35.988180'
original_url: https://dev.to/nickytonline/advent-of-ai-2025-day-17-building-a-wishlist-app-with-goose-and-mcp-ui-330l
author: Nick Taylor
date: '2025-12-27'
description: I've edited this post, but AI helped. These are meant to be quick posts related to the Advent of AI.... Tagged with ai, showdev, agents, devchallenge.
tags: '#showdev, #ai, #agents, #devchallenge'
---

I've edited this post, but AI helped. These are meant to be quick posts related to the Advent of AI. I don't have time if I'm doing one of these each day to spend a couple hours on a post. 😅

Theadvent of AIseries leverages Goose, an open source AI agent. If you've never heard of it, check it out!

## block/goose

### an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM

# goose

a local, extensible, open source AI agent that automates engineering tasks

goose is your on-machine AI agent, capable of automating complex development tasks from start to finish. More than just code suggestions, goose can build entire projects from scratch, write and execute code, debug failures, orchestrate workflows, and interact with external APIs -autonomously.

Whether you're prototyping an idea, refining existing code, or managing intricate engineering pipelines, goose adapts to your workflow and executes tasks with precision.

Designed for maximum flexibility, goose works with any LLM and supports multi-model configuration to optimize performance and cost, seamlessly integrates with MCP servers, and is available as both a desktop app as well as CLI - making it the ultimate AI assistant for developers who want to move faster and focus on innovation.

# Quick Links

* Quickstart
* Installation
* Tutorials
* Documentation
* Responsible AI-Assisted Coding Guide
* Governance

## Need Help?

* Diagnostics & Reporting
* Known Issues

…

View on GitHub

ForDay 17 of the Advent of AI challenge, I built a Winter Wishlist app usingMCP-UI.

## What I Built

A wishlist MCP server that renders a visual UI directly in Goose. Users can:

* Add wishes with a quick message to Goose
* View all their wishes in a nicely formatted UI
* Grant wishes when they come true
* Delete wishes they no longer want

Check out the repo:

## nickytonline/wishlist-mcp

### Advent of AI Day 17: Wishlist MCP App

# 🎄 Winter Fairy's Wishbox

A magicalMCP-UIapplication that brings the Winter Festival's enchanted wishbox to life! Built forAdvent of AI 2025 - Day 17, this app lets you make wishes, view them in a beautiful UI, grant them when they come true, and release them when needed - all within your MCP client like goose or ChatGPT.

## 📖 The Story

In the center of the Winter Festival stands an ancient, frost-covered mailbox known as the Winter Fairy's Wishbox. For generations, children (and adults too!) have written their wishes on paper and dropped them in, hoping the Winter Fairy would see them. This year, the magic has gone digital! Make wishes, watch them appear in a beautiful enchanted interface, and track them as the Winter Fairy grants them!

## ✨ Features

* 🌟 Make Wishes- Tell goose your wishes with categories (toy/experience/kindness/magic) and priorities (dream wish/hopeful wish/small wish)
* 📋…

View on GitHub

The implementation stores wishes in memory based on MCP session ID. Obviously something more robust would make sense for production, but for this challenge it works great.

## The ChatGPT App Template Foundation

I based this on aChatGPT app TypeScript templateI had created for work just before the holiday. Having that foundation made spinning up the wishlist server much faster.

## pomerium/chatgpt-app-typescript-template

### ChatGPT app template using Pomerium, OpenAI Apps SDK and Model Context Protocol (MCP), with a Node.js server and React widgets.

# ChatGPT App Template

A well-architected starter template demonstrating best practices for buildingChatGPT appsusing theModel Context Protocol(MCP) withReactwidgets. It leverages TypeScript, Tailwind CSS v4, Pino logging, Storybook, and Vitest for a robust development experience.

## Features

* MCP Server- Node.js server with baseServerclass (preserves_metafields)
* Echo Tool- Example tool withZodvalidation and widget response
* React Widgets- Interactive marquee component withcallTooldemo
* PinoLogging- Structured logging with pretty printing in development
* TypeScript- Strict mode with ES2023 target
* Tailwind CSS v4- Modern styling with dark mode support
* Storybook- Component development with a11y addon
* Testing-Vitestfor server and widgets with accessibility checks
* Build Optimizations- Parallel builds, content hashing, compression
* Docker- Multi-stage builds with health checks
* Production Ready- Session management, graceful shutdown, error handling

## Architecture

graph TD
 A[ChatGPT] -->|HTTPStreamable| B[MCP Server<br/>Node.js + Express]
 B
…

View on GitHub

One of the best parts of this setup is the development workflow. You can build out your components in Storybook, make live edits to widgets, and see them update in Goose in real-time. This makes iterating on the UI super fast.

## The iframe Sizing Battle

The main issue I ran into was iframe sizing. In ChatGPT apps, the iframe sizing seems to handle itself based on content. But in Goose? Not so much. I had to add some JavaScript to handle the sizing properly.

Initially I thought I was doing something silly because all my iframes weren't sizing to my content. There's additional metadata you can add to the UI resource, but that didn't change anything. I even noticed while debugging that my iframe was inside another iframe, which seemed odd.

ThenRizel in a GitHub discussion(@blackgirlbytes) came through with the solution. You need to use a ResizeObserver on your content container and post messages to the parent frame for Goose:

// Auto-resize the iframe to fit content - observe only the container

const

container

=

document
.
querySelector
(
'
.container
'
);

if
(
container
)

{


// Send initial size


window
.
parent
.
postMessage
({


type
:

"
ui-size-change
"
,


payload
:

{

height
:

container
.
offsetHeight

+

100

}


},

"
*
"
);


// Observe container only (not document which snowflakes affect)


new

ResizeObserver
(
entries

=>

{


entries
.
forEach
(
entry

=>

{


window
.
parent
.
postMessage
({


type
:

"
ui-size-change
"
,


payload
:

{

height
:

entry
.
contentRect
.
height

+

100

}


},

"
*
"
);


});


}).
observe
(
container
);

}

Enter fullscreen mode

Exit fullscreen mode

That fixed it completely.

## Key Learnings

MCP-UI is powerful for creating visual interfaces right in your AI chat. Having a solid template to start from made a huge difference. If you're building MCP servers, especially UI-based ones, starting with a good foundation saves a ton of time.

Even if you missed the Advent of AI this year I encourage you to head over toAdventOfAI.devand jump in.

If you want to stay in touch, all my socials are onnickyt.online.

Until the next one!

Photo byJordyn St. JohnonUnsplash

Photo byPhil StanieronUnsplash

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
