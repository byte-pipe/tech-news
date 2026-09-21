---
title: What If Your AI Agent Never Had to Leave the Browser? (Demo 🚀) - DEV Community
url: https://dev.to/sylwia-lask/what-if-your-ai-agent-never-had-to-leave-the-browser-demo--5g
site_name: devto
content_file: devto-what-if-your-ai-agent-never-had-to-leave-the-brows
fetched_at: '2026-09-21T16:50:07.566067'
original_url: https://dev.to/sylwia-lask/what-if-your-ai-agent-never-had-to-leave-the-browser-demo--5g
author: Sylwia Laskowska
date: '2026-09-21'
description: I haven't written anything lately because, honestly, I just didn't have the headspace for it. There... Tagged with ai, webdev, mcp, typescript.
tags: '#ai, #webdev, #mcp, #typescript'
---

Insights from speaking at AGNTCon Europe

I haven't written anything lately because, honestly, I just didn't have the headspace for it. There were a few reasons, but the biggest one was my talk at AGNTCon + MCPCon Europe, where I spoke about WebMCP.

How did it go? Great! A lot of people showed up, they asked questions — what more could I ask for? 😅 The conference itself was amazing too, and I definitely came back with enough inspiration for several more articles. I don't have any nice photos yet, but maybe next week!

The audience at an event with more than 2,000 attendees is, of course, incredibly diverse, with very different interests. Alongside people eager to explore sophisticated multi-agent architectures, there were many who were simply wondering how they could improve their already pretty good products by adding some AI capabilities.

Quite a few people from that second group ended up at my WebMCP talk.

## So, What Is WebMCP?

In short, WebMCP is an experimental browser API that allows a website to explicitly expose tools that an AI agent can then call. I don't want to repeat myself too much because I've already written about it here:

Is This How We'll Build Websites Soon? WebMCP Live Demo

That article is more than three months old, which, in the world of Agentic AI, means the syntax is already outdated. xD Fortunately, these days it's not particularly difficult to quickly check the latest one, especially since it may still change several more times. 😅

The idea, however, remains the same.

Yes, it's still a young technology. But as it happens, I met one of the people working on WebMCP at the conference (hi, Dominic!), and he told me that around January or February it should be reasonably stable, at least in Chromium.So the clock is ticking!

## WebMCP Is Not Quite MCP

Unlike "classic" MCP (and I'm puttingclassicin quotation marks because I'm not sure whether something this young has earned the right to be called "classic" or "traditional" yet 🤣) WebMCP operates in the context of the browser.

The website needs to be open, the user needs to be logged in if authentication is required, and only then can our agent call the tools exposed by that page. This means we can use WebMCP through an agentic browser or, for example, a Chrome extension. Interestingly, ChatGPT has recently added support for WebMCP-based site tools in its built-in browser, so this technology definitely has some momentum!

That's also why, in my opinion, WebMCP's most interesting use case isn't necessarily multi-agent systems scraping websites. I see it much more as a way to help regular, everyday users interact with the products they already use. Although, of course, give ten developers a new API and you'll probably get eleven different ideas. 😉

## Meet My Visionary Leader: AI CEO Simulator

As some of you may remember, my WebMCP demo isn't another boringaddToCart()example. It's my beloved visionary leader:AI CEO Simulator. It shows what might happen if we let AI run our company.

As you can see in the screenshot, we have all the typical startup metrics: cash, monthly revenue, number of employees, production incidents, employee happiness, and, obviously, hype level.

We also have board decisions such asAdopt AI,Pivot to Agents,Rewrite in Rust,Fire Employees,Hire Employees, and so on.

In other words: typical startup management.

And, of course, there's an activity log.

The important thing is that this is still a completely normal website. You can click around and use everything manually. Because that's one of the things I love about WebMCP: it's an additional capability for your website. You don't need to completely rebuild your product around AI.

GitHub:https://github.com/sylwia-lask/ai-ceo-webMCPDemo:https://sylwia-lask.github.io/ai-ceo-webMCP/

## Okay, But How Do We Actually Call Those Tools?

Everything sounds great, but there's one practical problem: how do we actually call these tools? This becomes an especially interesting problem when you want to call them live during a conference talk.

Of course, you can do it through ChatGPT or one of the publicly available extensions, but cloud-based solutions need internet access. Their interfaces aren't necessarily ideal for presentations either — when people are watching your demo on a big screen, everything should be large and easy to follow.

And, obviously, I wanted a fallback to local models!

So I built a Chrome extension calledWebMCP Local Agent.

GitHub:https://github.com/sylwia-lask/webmcp-local-agent

It's not published in the Chrome Web Store yet, but maybe one day I'll finally spend those $5 on the developer registration fee. 😅💸 For now, if you're interested, you can simply download the source and run it locally.

## Is It Actually an Agent?

So what does this plugin — or agent — actually do?

It's very simple. It receives the user's intent, checks the WebMCP tools available on the current page, and calls whichever ones it considers appropriate.

We all know that an agent is basically just a loop. I wrote more about that here:The Dirty Secret Behind AI Agents (Demo 🚀)

And that's exactly how this one works. The model gets the user's intent and the available tools, decides what to call, receives the result, and can then decide what to do next. By default, the agent can go through a maximum of 10 iterations of this loop, although you can change that in the config.

So, as you can see, this isn't just a chatbot with a fancy name. It's a legit little agent.

## A Slightly Selfish Motivation Can Still Lead Somewhere Useful

Yes, my original motivation was pretty simple and maybe even a little selfish. 😉 But good things can come from questionable motivations. Even Gollum contributed to the happy ending ofThe Lord of the Rings. xDDD

Because my extension can run with local models, prompts and model inference can stay on the user's machine when using the local providers. That gives us a very interesting privacy advantage compared with sending every interaction to a cloud model.

It also helps with another problem: access to AI models isn't equally reliable everywhere. My dear DEV friend@dannwanerimentioned this problem some time ago. Just because we have pretty good infrastructure and access to cloud AI services in Europe doesn't mean the situation is equally good everywhere in the world.

Local models give us another option.

## Three Providers, One Agent

As you can see, my WebMCP plugin currently supports three modes.

The first is Google'sPrompt API, which uses Gemini Nano managed by Chromium. Once the model has been downloaded, inference happens locally, without sending prompts to Google or another third party, and you don't need an API key.

The second option isOllama, also running locally. In my case, I'm using Llama 3.1, but you can choose another model if you prefer. Ideally, though, you want one that behaves well with tool calling.

And finally, there is one cloud provider. In my case, that's an older Gemini Flash model, which requires an API key. Because let's be honest: right now, cloud models are generally still the easiest way to get excellent capability and speed. The problem is that they're not always available.

Of course, you can add other models or providers however you like. It's literally just a few lines of code in the extension's source code. ☺️

## And Yes, the Local Models Actually Work

As you can see, the local providers work surprisingly well.

Here's Google's Prompt API:

And here's Llama 3.1:

Although I should warn you that Llama 3.1 — rarely, but it does happen — sometimes decides that instead of JSON, what Ireallywanted was Markdown or some additional "helpful" commentary. That's the joy of working with LLMs. 😅

It's also worth mentioning again that the plugin allows a maximum of 10 iterations of the agent loop by default. You can increase or decrease that number in the config.

## But Wait. Isn't This Dangerous?

One concern I hear quite often about WebMCP is that we're changing the interaction model. The user is no longer explicitly clicking every single thing they want to happen. Instead, they express an intent.

Then the model creates a plan, calls tools, and we have to deal with the consequences. And if we simply leave it at that, it's a recipee for DISASTER.

There are relatively harmless tools such as:

listEmployees()

But there are also tools with much more serious consequences, such as:

fireEmployees()

And I'd rather not discover that my AI CEO has decided to improve our runway by firing half the company without asking me first.

## Consequential Actions Need Confirmation

Fortunately, the people working on WebMCP are listening to the community, and the API now includes useful tool annotations such asconsequentialHint. My plugin supports it as well.

Support for these newer WebMCP features depends on the Chromium version and experimental WebMCP availability you're using, so if you're testing this while the API is still evolving, make sure you're running a sufficiently recent version of Chrome/Chromium with the required WebMCP support enabled.

Now let's try to fire some employees.

As you can see, our agent noticed that the tool call was marked as consequential and displayed a confirmation prompt before allowing it to proceed. The user can approve or reject the action.

Which is probably a good idea when your AI CEO starts restructuring the company. 😉

## And, of Course, I Built It with Kiro

And as a self-respecting AWS Community Builder, I built all of this with the help of the best IDE in the world: Kiro. 😅 I'll admit it: I originally installed Kiro because I wanted to save some money on Claude Code. But at this point, even if@corey_awskicked me out of the Community Builders program tomorrow, I'd still happily pay for Kiro out of my own pocket. 😂

Not only does Kiro give you a ridiculous number of models to choose from, but it also supports spec-driven development, which I've grown to really appreciate. It also handled the constantly changing WebMCP API remarkably well, including one last API change that I had to deal with literally two hours before my conference talk. 😅

So, AWS: good job. You got me. 👏

## Maybe We Don't Need a Revolution

So, as you can see, we don't necessarily need a huge architectural change or a complete revolution in our existing projects to make them more user-friendly and agent-friendly.

Our website can still be a website. People can still click buttons, fill in forms, and use the UI exactly as they did before. WebMCP simply gives agents another structured way to interact with it.

Someone at the conference said that this isn't a revolution comparable to replacing horses with cars.

It's just...

faster horses.

But what if faster horses are exactly what we need right now?

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (25 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse