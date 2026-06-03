---
title: Is This How We'll Build Websites Soon? (webMCP Live Demo 🚀) - DEV Community
url: https://dev.to/sylwia-lask/is-this-how-well-build-websites-soon-webmcp-live-demo--2e33
site_name: devto
content_file: devto-is-this-how-well-build-websites-soon-webmcp-live-d
fetched_at: '2026-06-03T12:34:47.389330'
original_url: https://dev.to/sylwia-lask/is-this-how-well-build-websites-soon-webmcp-live-demo--2e33
author: Sylwia Laskowska
date: '2026-06-03'
description: A few years ago, we started adapting our websites for mobile devices. Then we adapted them for... Tagged with javascript, react, mcp, ai.
tags: '#javascript, #react, #mcp, #ai'
---

Chrome's experimental protocol for AI agents

A few years ago, we started adapting our websites for mobile devices. Then we adapted them for accessibility. And now we may be about to adapt them once again. This time... for AI agents.

To see what this could look like in practice, I built a completely serious and absolutely enterprise-ready AI CEO Simulator.

We'll come back to our visionary leader in a moment.

BTW, thank you all for the amazing discussion under my previous article. We somehow managed to generate approximately one billion comments 🩷 Many of them were probably smarter than the article itself. The sensible thing to do would be to write a follow-up post summarizing everything.

But honestly, I needed a break from that topic before I exploded.

Sometimes I just have to write something technical, otherwise I'll suffocate. Fortunately, nobody pays me for these articles, so I can do whatever I want 😁 We'll come back to AI in software development another time.

## What Is webMCP? 🤖

For now, let's talk about webMCP.

Google is currently experimenting with webMCP support in Chrome, an approach designed to make it easier for AI agents to interact with websites.

The problem it tries to solve is actually quite simple.

Today, when an agent wants to use a website, it has to inspect the page, figure out which elements are important, click around, analyze the results, and repeat this process over and over again. It works, but it's slow, expensive, and not always reliable.

webMCP allows websites to expose structured information about available actions, so agents can understand what they can do without endlessly scraping the page and guessing.

## Time for a Completely Serious Business Simulation 🚀

But enough theory.

Let's build something completely serious and enterprise-ready.

@cart0nementioned under my previous article that AI had effectively become the CEO of his startup.

So, as a responsible person, I built an AI CEO Simulator in React + TypeScript.

GitHub:https://github.com/sylwia-lask/ai-ceo-webMCP

Live demo:https://sylwia-lask.github.io/ai-ceo-webMCP/

## How To Enable webMCP

Before you immediately rush to implement webMCP in your production application, a small disclaimer.

For now, this is still experimental technology. It currently works only in Chrome Canary, Chrome Beta, or Chrome with the appropriate experimental flag enabled.

To enable it:

1. Open `chrome://flags`
2. Search for "MCP"
3. Enable the experimental MCP-related features
4. Restart Chrome

Enter fullscreen mode

Exit fullscreen mode

If you'd rather not play with experimental browser flags, that's fine. You can simply look at the screenshots below.

Or click around the application yourself, because everything still works perfectly as a normal website.

That's actually one of the things I like most about this approach. WebMCP is just an enhancement for agents, much like accessibility features are enhancements for users relying on screen readers. Nothing breaks, nothing changes for regular users.

The application simply becomes easier to understand for a different kind of visitor.

## Two Ways To Use webMCP

There are currently two main ways of exposing information through webMCP.

### Option 1: Declarative API / HTML annotations

The first approach is adding metadata directly to HTML elements:

<form

 
mcp-name=
"createSupportTicket"

 
mcp-description=
"Create a new customer support ticket"
>

Enter fullscreen mode

Exit fullscreen mode

This allows agents to understand the purpose of UI elements without relying entirely on visual interpretation.

### Option 2: Imperative API / JavaScript tools

The second approach is exposing MCP tools directly from your application code.

That's the approach I used in my demo:

registerTool
({

 
name
:
 
'
hire_employee
'
,

 
description
:
 
'
Hire a new employee
'

});

registerTool
({

 
name
:
 
'
fire_employee
'
,

 
description
:
 
'
Fire an employee
'

});

Enter fullscreen mode

Exit fullscreen mode

In my application, these tools correspond directly to actions available through buttons on the page.

For example, I expose tools such as:

hireDevelopers
()

fireDevelopers
()

adoptAI
()

rewriteInRust
()

pivotToAgents
()

fixProductionBugs
()

Enter fullscreen mode

Exit fullscreen mode

In other words: completely normal startup management.

## Connecting an AI Agent

So what happens when we connect an actual AI agent?

Instead of building my own agent, I used the WebMCP – Model Context Protocol Inspector extension. You can connect a Gemini API key and immediately start experimenting. There's even a free token allowance. Small, but still enough to make some questionable strategic decisions 😅

As with most LLM-powered systems, everything starts with a prompt.

## Scenario #1: The LinkedIn CEO 😎

Let's see how our CEO performs when given the following instruction:

Act like a CEO who just read three articles about AI on LinkedIn.

As you can see, the agent selected the appropriate tools and immediately got to work.

The company's employees may have started updating their LinkedIn profiles in panic, but at least the hype level reached previously unimaginable heights.

## Scenario #2: Rebuilding Employee Trust ❤️

Now let's try something a little more challenging:

I want to rebuild my employees' trust while simultaneously developing the product.

This time our agentic CEO made several surprisingly clever moves and managed to guide the company back toward sustainable growth.

## So... Is This The Future?

Honestly, I had way too much fun building this.

No, I don't think this is a glimpse into a future where self-healing AI agents manage the global economy while piloting commercial aircraft.

But I do think webMCP solves a real problem.

If AI agents are going to spend more and more time interacting with our applications, giving them a structured way to understand those applications makes a lot more sense than forcing them to endlessly scrape HTML and guess what every button does.

Will webMCP become a normal part of web development?

Will adapting websites for agents become as common as responsive design or accessibility?

Or will this trend disappear before it ever reaches the mainstream?

I'm genuinely curious what you think.

If you enjoy my articles, feel free to follow me onLinkedInas well.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (14 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse