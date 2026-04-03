---
title: An Honest Review of Google Antigravity - DEV Community
url: https://dev.to/fabianfrankwerner/an-honest-review-of-google-antigravity-4g6f
site_name: devto
fetched_at: '2026-01-09T11:07:47.144030'
original_url: https://dev.to/fabianfrankwerner/an-honest-review-of-google-antigravity-4g6f
author: Fabian Frank Werner
date: '2026-01-04'
description: So, for the last year, if you wanted the best AI coding experience, you were paying $20 a month for... Tagged with webdev, programming, ai, beginners.
tags: '#webdev, #programming, #ai, #beginners'
---

So, for the last year, if you wanted the best AI coding experience, you were paying $20 a month for Cursor. It’s been the king. But there is a new competitor in the ring. And yes, it’s a VS Code fork. But no, it’s not from some random startup.

It’s from Google.

It’s called Antigravity. And right now, during the preview, it is fully, 100% free. You get access to their newest, models like Gemini 3, full browser orchestration, and an entirely new way to manage code, without swiping a credit card.

Now, usually when Google releases a developer tool, it’s either incredible or it gets killed in six months. I’ve been daily driving Antigravity for the past week, digging into the code, and honestly? It’s a bit of both. It is one of the most promising pieces of software I’ve seen this year, and also, at times, the single most frustrating editor I have ever used.

We need to talk about the "Agent-First" workflow, the crazy Gemini 3 benchmarks, and the fact that this might actually just be a zombie version of another editor called Windsurf. Let’s get into it.

So, first things first. If you peel back the skin, this is VS Code. If you go into the "About" section, you see the VS Code OSS version. But Google has done a lot of work to hide that.

They’ve renamed "VS Code Settings" to just "Editor Settings." They’ve stripped out a lot of the familiar Microsoft branding. And interestingly, if you dig into the file search, you might see references to something called "Cascade."

Now, if you’ve used the Windsurf editor, you know that "Cascade" is the name of their AI agent. So, it looks like Google might have acquired some tech, or some humans, or just forked a build of Windsurf to get this off the ground quickly. It’s a little uncanny valley.

But the biggest change isn't the code under the hood; it's theThree Surfaces.

Google’s thesis is that an IDE shouldn't just be a text editor anymore. It needs to be an operating system for Agents. So you have theEditor, which is where you type. You have theBrowser, which is a fully controlled Chrome instance. And most importantly, you have theAgent Manager.

This Agent Manager is the star of the show. It’s literally a separate application window that acts as an "Inbox" for your development tasks.

The idea here is brilliant. Instead of having your AI chat squeezed into a sidebar inside your code, your "Manager" sits outside. It’s Mission Control. You can have five different projects running in parallel. You can see which agents are thinking, which ones are waiting for approval, and which ones have failed. It’s designed for the ADHD developer brain where you are bouncing between tasks.

And when you want to dive in, you just hit Command+E, and it focuses the Editor for that specific project. It feels like a futuristic workflow... when it works. But we’ll get to the bugs in a minute. First, I want to show you what this thing can actually do when you give it a real challenge.

Antigravity is built around Gemini 3 and Gemini 2.5. And since this is free right now, I decided to push it hard. I asked it to build a clone of that old "Insaniquarium" game—a simulation where you drop food, fish eat it, and they drop coins.

I tried this same prompt with other high-end models like Codex High. I spent an hour fighting it. It couldn't handle the physics. The particles were broken. It burned through 3.5 million tokens and gave me a broken mess where the fish were 2D sprites floating in a void.

Then I gave the exact same prompt to Antigravity with Gemini 3.

It one-shot it. First try. It built a working game using Phaser. But here is the crazy part—it didn't just write the code. It generated the assets.

I didn't give it images of fish or coins. The Agent realized, "Hey, I need sprites for this," so it paused, used its internal image generation model to create the fish, the food, and the background, and then injected them into the game code.

Now, were they perfect? Of course not. The first time, the fish had white backgrounds instead of transparent ones, so they looked like JPEGs floating around. But I told the Agent, "Fix the transparency," and it went back, regenerated the assets, and updated the code.

This is that "Agent-First" distinction. It’s not just a chatbot. It’s a worker that has access to tools—an image generator, a file system, a browser. It felt like I was directing a junior developer who also happened to be a graphic designer.

The other killer feature here is the Browser integration. Google makes Chrome, Google makes Antigravity, so naturally, they talk to each other.

You can spin up a "Browser Agent" to test your work. You tell it, "Go to localhost and test the game." A Chrome window opens with this blue "Agent Control" border. You watch the red dot—which is the AI's cursor—move around, click the fish, drop food, and verify the physics.

It even records a video of itself doing it, so you can watch the playback later in the "Walkthrough" artifact. It captures screenshots of errors. It’s just incredibly cool to watch.

But—and there is always a but—it’s buggy. Half the time, I’d get a "Controls Disabled" warning even though it was working. Sometimes it would try to connect to the wrong localhost port because I had too many projects open. It’s powerful, but it feels like a prototype.

And that brings us to the reality of using Antigravity right now. As impressive as the model is, the editor itself... got some issues.

First off, it’s buggy. I’ve had buttons just stop working. I’ve had the sidebar icons vanish until I clicked them blindly. The Svelte extension—one of the most popular web frameworks—just straight up doesn't work. It breaks the whole editor.

Then there is the "Review Code" button. You see a button that says "Review Changes," so you click it, right?

It instantly closes. It’s almost like the editor is trolling you. We joked that you just aren't in the "Agentic Mindset" yet. You don't review the code whenyouwant to; you review it when theAgenttells you it's ready.

There are also weird missing features. For example, arrow keys.

In the file explorer, you can’t use the arrow keys to move up and down. You have to click. In a code editor. That is a crime.

And for the power users: No Git Worktrees. Cursor has this, and it’s amazing for switching branches instantly. Antigravity doesn't support it yet, which is ironic because the whole point of the Agent Manager is multitasking.

We also have to talk about efficiency. This app is heavy.

I noticed significant battery drain on my MacBook Pro while running this. There is also this fancy glow effect around the UI when the Agent is thinking. It looks cool, but it causes input lag. When I’m typing in the editor while the Agent is generating, I can literally feel the delay.

And that’s the trade-off. You are running a local Chrome instance, a heavy Electron app, and constant streaming connections to Gemini. It eats resources for breakfast.

So, where does that leave us?

Google Antigravity is a fascinating, frustrating, yet futuristic mess.

TheAgent Managerworkflow—that "Inbox" for your code—is genuinely a great idea. I hope every other editor copies that. TheGemini 3model is shockingly good at one-shotting complex tasks and generating assets. And the price? Well you can't beat free.

Google says the free tier limits reset every five hours, and honestly, I hit those limits a few times, but for most people, it’s plenty. You are getting access to state-of-the-art models without a subscription.

But would I uninstall Cursor for this? Not today. The bugs, the missing syntax highlighting in some modes, the broken extensions—it’s just not stable enough for a deadline.

However, this is just the preview. If Google actually commits to this—if they fix the bugs, bring in the full extension support, and keep the Agent Manager workflow—this could be the one.

For now, I recommend you download it. Use it for your side projects. Play with the aquarium game generator. It’s a glimpse into a future where we do less typing and more managing. And that future looks pretty bright right now... assuming you can get the arrow keys to work.

Are you trusting Google with your code, or are you sticking with VS Code, Cursor, or whatever?

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
