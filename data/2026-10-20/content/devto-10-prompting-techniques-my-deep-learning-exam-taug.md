---
title: 10 Prompting Techniques My Deep Learning Exam Taught Me (That I Actually Use Now) - DEV Community
url: https://dev.to/dj29/10-prompting-techniques-my-deep-learning-exam-taught-me-that-i-actually-use-now-43h0
site_name: devto
content_file: devto-10-prompting-techniques-my-deep-learning-exam-taug
fetched_at: '2026-10-20T22:05:17.213209'
original_url: https://dev.to/dj29/10-prompting-techniques-my-deep-learning-exam-taught-me-that-i-actually-use-now-43h0
author: Dhruv Jani
date: '2026-10-17'
description: You already use prompting every day. You just don't know the names of what you're doing. Every time... Tagged with promptengineering, ai, discuss, beginners.
tags: '#discuss, #promptengineering, #ai, #beginners'
---

Academic AI theory turned into practical dev tips

You already use prompting every day.

You just don't know the names of what you're doing.

Every time you type "fix this error" into ChatGPT or "refactor this function" into Cursor — that's a prompting technique. You're already doing it. You just haven't been told there are ten distinct ways to do it, and most of them are better than what you're doing right now.

I had to study all of this for my Deep Learning exam. Two 50-page PDFs full of academic examples like"Recommend science-fiction books"and"Convert 0°C to Fahrenheit."Technically correct. Practically useless. Nobody is opening ChatGPT to convert Celsius.

So here's the version I wish those PDFs had been —every technique from my syllabus, explained with examples you'll actually use as a developer.

## Table of Contents

* 1. Zero-Shot Prompting
* 2. Few-Shot Prompting
* 3. Chain-of-Thought Prompting
* 4. Tree-of-Thought Prompting
* 5. Role-Playing Prompts
* 6. Generated Knowledge Prompting
* 7. Maieutic Prompting
* 8. Least-to-Most Prompting
* 9. Format-Specific Prompting
* 10. Multi-Turn Prompting
* The Cheat Sheet
* 🧪 The Real Trick: Combine Them

## 1. Zero-Shot Prompting

What it is:You ask the AI something directly. No examples. No context. No hand-holding. Just the question.

The textbook example:

"Can you recommend science-fiction books?"

The developer example:

"What does theuseEffectcleanup function do in React?"

Or:

"Explain the difference betweengit rebaseandgit mergein 3 sentences."

You're already doing this. Every time you paste an error into ChatGPT with zero context and pray — that's zero-shot prompting. It works great for questions the model has seen a million times. It falls apart the moment your problem is even slightly niche.

When to use it:Quick lookups, syntax questions, "what does X do" queries. Anything where the AI's pre-trained knowledge is enough.

When it fails:The moment your question involves YOUR codebase, YOUR architecture, or anything the model hasn't been trained on. That's when you need the next one.

## 2. Few-Shot Prompting

What it is:You show the AI 2-5 examples of what you want, then let it figure out the pattern and apply it to a new input.

The textbook example:

Convert Celsius to Fahrenheit:0°C → 32°F25°C → 77°F100°C → ?

The developer example:

Say you're writing commit messages for your team and you want a consistent style:

Here are my commit messages so far:

feat: add user authentication with JWTfix: resolve null pointer in payment servicerefactor: extract validation logic into middleware

Now write a commit message for: I added rate limiting to the API endpoints.

Output:

feat: add rate limiting to API endpoints

The model picks up your prefix convention (feat:,fix:,refactor:), your sentence casing, your level of detail — without you having to explain any of it.

Another real use:You're converting an old API response format to a new one. Show 3 examples of old → new, paste the 4th old response, and let the model transform it. Saves you from writing a throwaway script.

When to use it:Consistent formatting, style matching, repetitive transformations. Anytime you're thinking"I need to do this same thing 40 more times."

## 3. Chain-of-Thought Prompting

What it is:You ask the AI to work through a problem systematically — step by step — instead of jumping straight to a conclusion.

The textbook example:

What is 23 × 47? Show your work.

The developer example:

This function is supposed to return the total price after discount, but it's returning NaN for some inputs. Walk me through what's happening step by step:

function
 
getTotal
(
price
,
 
discount
)
 
{

 
const
 
total
 
=
 
price
 
-
 
(
price
 
*
 
discount
 
/
 
100
);

 
return
 
total
.
toFixed
(
2
);

}

Without "step by step," the AI might just say"the function looks fine."With it, the AI will trace through edge cases:"Ifdiscountis passed as a string like '10%', the multiplication produces NaN, which propagates through the calculation..."

Asking for a step-by-step breakdown doesn't necessarily reveal the model's actual internal reasoning — but it does force a more inspectable answer: stated assumptions, intermediate checks, edge cases considered, and only then a conclusion. That structure is what makes the mistakes easier to catch.

This is exactly how I tracked down aclients.matchAll()race condition in one of my project's service workers. Copilot's first answer was confident and completely wrong. Asking it to walk through the event lifecycle step by step — not "fix this," but "trace what happens between these two events" — is what actually surfaced the timing bug.

When to use it:Debugging, code reviews, any question where thereasoningmatters more than the answer. If you've ever gotten a confident but completely wrong answer from an AI — this is probably what was missing.

## 4. Tree-of-Thought Prompting

What it is:Instead of following one reasoning path, the AI explores multiple paths in parallel. Chain-of-thought is a straight line. Tree-of-thought is a decision tree.

The textbook example:

List the environmental and social effects of climate change separately.

The developer example:

I need to add real-time notifications to my app. Explore three different approaches — WebSockets, Server-Sent Events, and polling — and for each one, explain the trade-offs in terms of complexity, scalability, and browser support. Then recommend which one fits a small team with a Node backend.

Instead of the AI just picking one and defending it (which is what zero-shot would do), this prompt makes the comparison explicit instead of letting the AI jump straight to one recommendation.

Another real use:Architecture decisions."We need to store user sessions. Compare Redis, database sessions, and JWT tokens. For each: list pros, cons, and failure modes. Then recommend one for a team of two building an MVP."

When to use it:Any decision with multiple valid options where you need the AI to compare, not just pick. Tech stack choices, architecture decisions, debugging when you're not sure which subsystem is the problem.

## 5. Role-Playing Prompts

What it is:You tell the AI to act as a specific expert. This isn't a gimmick — it genuinely changes the depth and angle of the response.

The textbook example:

"Imagine you are a seasoned venture capitalist. Review this startup pitch."

The developer example:

You are a senior backend engineer conducting a code review. Review this Express.js route handler and flag any security vulnerabilities, performance issues, or architectural concerns. Be specific — cite the line and explain why it's a problem.

Without the role, the AI gives you a polite, generic review.Withthe role, it starts acting like that one senior dev who actually catches things —"Line 14: you're interpolating user input directly into the SQL query. This is a textbook SQL injection vector."

I've also used this the other way around during placement season:"You are a strict technical interviewer at a product-based company. Ask me follow-up questions on this project until you find a gap in my understanding."It's uncomfortable. It's also the closest free rehearsal you'll get before the real thing.

Other roles that actually help:

* "You are a tech recruiter. What's weak about this resume?"
* "You are a QA engineer. Find edge cases in this function."
* "You are a DevOps engineer. What's wrong with this Dockerfile?"

When to use it:Code reviews, resume feedback, interview prep, getting a second opinion from a perspective you don't have on your team. The role narrows the AI's focus to what that specific expert would care about.

## 6. Generated Knowledge Prompting

What it is:Before asking the AI to do the actual task, you first ask it to list everything it knows about the topic. Research first, write second.

The textbook example:

"Write an essay on deforestation. First, list key facts."

The developer example:

I need to write documentation for our authentication flow. Before you write anything:

1. List every step that happens from when a user clicks "Login" to when they land on the dashboard — including token generation, cookie handling, and redirect logic.
2. Now write the developer documentation based on that list.

The magic here is Step 1. By forcing the AI to generate a knowledge base first, you get a factual foundation that the writing stays grounded in. Without it, the AI often drifts into generic documentation that misses your specific flow.

When to use it:Writing documentation, README files, technical blog posts (ironic, right?), or any task where factual accuracy matters more than creativity. The "list what you know first" step acts as a self-fact-check.

## 7. Maieutic Prompting

What it is:Named after the Socratic method — you ask a question, then ask the AI to explainits own answerdeeper, then deeper again. Recursive questioning until you actually understand.

The textbook example:

"Explain why the sky is blue. Then explain why blue light scatters more."

The developer example:

Why is my React component re-rendering on every state change even though I'm usinguseMemo?

Now explain why the dependency array matters foruseMemospecifically.

Now explain what "referential equality" means in the context of JavaScript objects and why it breaks memoization.

Each follow-up forces the AI to go one layer deeper. By the third question, you've gone from "it's re-rendering" to understanding how JavaScript's object comparison model fundamentally interacts with React's reconciliation algorithm.

When to use it:Learning new concepts. When the first answer makes sense but you can feel there's something underneath you don't fully get. It's the"but why?"technique.

## 8. Least-to-Most Prompting

What it is:You tell the AI to break a big problem into subproblems first, then solve each one in order. Decompose, then execute.

The textbook example:

"List the subproblems to solve 3x + 5 = 20, then solve each."

The developer example:

I need to add Google OAuth to my Next.js app. Break this down into every subproblem I need to solve, in order. Then walk me through each one with code.

Output would look something like:

1. Set up Google Cloud Console project and get credentials
2. Install and configure NextAuth.js
3. Create the auth API route
4. Add the Google provider configuration
5. Protect routes with session checks
6. Handle the callback and store user data

Then the AI solves each one sequentially, and each step builds on the last.

This is basically how I survived every hackathon deadline — breaking "build a working demo in 24 hours" into an actual ordered sequence instead of staring at the whole scope and panicking.

When to use it:Implementing features you've never built before. Instead of asking "how do I add auth" (which gets you a vague overview), you force the AI to give you a buildable sequence.

## 9. Format-Specific Prompting

What it is:You explicitly tell the AI what format you want the output in. Bullet points, table, JSON, markdown, CSV — specify it and the AI follows.

The textbook example:

"List the top 5 movies in bullet points."

The developer example:

Compare these three state management libraries for React. Output as a markdown table with columns: Library, Bundle Size, Learning Curve, Best For, and Drawback.

Or:

Convert this error log into a JSON array where each object hastimestamp,level,message, andsourcefields.

This is one of the most underrated techniques. Most devs don't specify format and then spend 5 minutes reformatting the AI's response. Just tell it upfront.

When to use it:Literally every time you want the output in a specific shape. Tables, JSON, code blocks, bullet points, numbered steps. If you're going to reformat the output anyway, you're wasting time.

## 10. Multi-Turn Prompting

What it is:Building context across multiple messages in a conversation. Each prompt builds on the last response. This is how you turn AI from a search engine into a collaborator.

The textbook example:

Turn 1: "Summarize this article."Turn 2: "Now rewrite it for a 10-year-old."Turn 3: "Add three quiz questions."

The developer example:

Turn 1:"Here's my Express app's folder structure. [paste tree output]. Explain the architecture."

Turn 2:"Now I want to add a notifications service. Where should it live in this structure, and what should it import?"

Turn 3:"Write the boilerplate for that service following the same patterns as the existing services."

Turn 4:"Now write the tests for it, matching the testing style in__tests__/user.service.test.js."

By Turn 4, the AI knows your folder structure, your architectural patterns, your naming conventions, and your testing style. A single-shot prompt could never produce output this tailored.

When to use it:Any substantial coding task. Building features, refactoring, writing tests. If you're copy-pasting the same context into every new prompt, you should be using multi-turn instead.

## The Cheat Sheet

Technique

In one sentence

Use when...

Zero-Shot

Just ask

Quick lookups, simple questions

Few-Shot

Show examples first

You need consistent formatting or style

Chain-of-Thought

"Think step by step"

Debugging, complex reasoning

Tree-of-Thought

Explore multiple paths

Comparing options, architecture decisions

Role-Playing

"You are a senior dev..."

Code reviews, interview prep, expert perspectives

Generated Knowledge

"List facts first, then write"

Documentation, technical writing

Maieutic

"Now explain WHY"

Learning new concepts deeply

Least-to-Most

"Break it into subproblems"

Implementing features you've never built

Format-Specific

"Output as a table/JSON/list"

Every time you want structured output

Multi-Turn

Build context over messages

Any substantial coding task

## 🧪 The Real Trick: Combine Them

Here's the thing nobody in those textbooks told me:you don't pick one technique and stick with it.The best prompts combine two or three.

Chain-of-thought + role-playing:"You are a senior engineer. Debug this function step by step."

Few-shot + format-specific:"Here are three examples of my commit messages. Write the next five in the same style, as a bullet list."

Generated knowledge + least-to-most:"List everything involved in deploying a Next.js app to AWS. Then break it into subproblems and walk me through each one."

The techniques are ingredients. The skill is knowing which ones to combine.

I learned all of this from two academic PDFs full of Celsius conversions and science-fiction book recommendations. Now you've learned it from examples you'll actually open a terminal and use tomorrow.

If this saved you from reading 50 pages of textbook formatting — you're welcome.

What's your go-to prompting trick that isn't on this list?Or which of these did you not know had a name?

Drop it below — I'm genuinely curious what people are doing that the textbooks haven't caught up to yet. 👇

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (22 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse