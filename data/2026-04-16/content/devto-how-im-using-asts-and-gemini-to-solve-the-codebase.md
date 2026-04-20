---
title: How I'm using ASTs and Gemini to solve the "Codebase Onboarding" problem 🧠 - DEV Community
url: https://dev.to/tworrell/how-im-using-asts-and-gemini-to-solve-the-codebase-onboarding-problem-1la9
site_name: devto
content_file: devto-how-im-using-asts-and-gemini-to-solve-the-codebase
fetched_at: '2026-04-16T19:59:56.065365'
original_url: https://dev.to/tworrell/how-im-using-asts-and-gemini-to-solve-the-codebase-onboarding-problem-1la9
author: tworrell
date: '2026-04-15'
description: Hi everyone! 👋 I’m Tara, a Senior Software Engineer and Consultant. Over the years, I've jumped... Tagged with ai, productivity, webdev, showdev.
tags: '#showdev, #ai, #productivity, #webdev'
---

Hi everyone! 👋

I’m Tara, a Senior Software Engineer and Consultant. Over the years, I've jumped between a lot of different codebases.

Every time I join a new project, I notice the exact same problem: it takes new engineers 3 to 6 months to truly understand how a complex system is glued together. AI tools like Copilot and Cursor are amazing at making us write code faster, but developers still spend almost 50% of their time just reading and navigating code.

Nobody was solving the comprehension layer. So, I decided to build a tool for it.

I’m super excited to share what I've been working on:AuraCode(Feel free to poke around the live interactive demo there!)

🤔 What does it do?AuraCode is a neural code agent that transforms messy, undocumented repositories into interactive visual maps and context-aware chat.

Here are the main features I’ve built so far:

* Interactive Architecture Canvas 🗺️: Paste a GitHub URL, and it generates a beautiful, interactive D3.js radial tree mapping out component relationships and the system structure.
* Contextual Chat + Text-to-Speech 🗣️: You can ask questions like "What breaks if I change this auth utility?" and get answers grounded in your actual code structure. I also hooked the output up to an ElevenLabs TTS engine, so you can have it read the flow to you hands-free while you look at the code.
* Smart Onboarding ✅: Say goodbye to outdated setup.md files. AuraCode auto-generates structured onboarding checklists tailored specifically to the architecture of the scanned codebase.
* Code Review Summaries 🚀: Point it at a PR, and it will run a trend analysis and spit out a review summary based on the delta.

🛠️ How it works under the hoodBuilding this required balancing context windows with accurate retrieval. Here is how I approached it:

The AI Architecture: Treating code as "flat text" loses all the important structural relationships (call graphs, dependency chains, etc.). To solve this, AuraCode uses two different approaches depending on the size of the repository:

For small/medium repos: I inject Abstract Syntax Trees (ASTs) directly into the model's context window. This preserves the architectural patterns so the AI actually understands how the code connects.For massive monorepos: I use what I call Lean RAG. It's a lightweight retrieval layer that selectively surfaces the most structurally relevant nodes before context injection. This keeps accuracy high without blowing out the token limit.

What's next? 🚀Right now, AuraCode is in pre-launch. Because I am entirely bootstrapped and LLM token costs scale rapidly with usage, I am currently opening up full private-repo access to the first 50 developers on the waitlist.

However, the demo is fully live and open to the public on the site!

I built this because it's exactly the tool I wish I had existed every time I was hired to consult on a massive, legacy codebase.

I would love to hear your thoughts! How do you usually handle ramping up on massive, undocumented codebases?

Let me know if you have any questions about the tech stack, the Lean RAG approach, or the D3 visualizations. I'd love to chat in the comments! 👇

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
