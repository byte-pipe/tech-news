---
title: The Dirty Secret Behind AI Agents (Demo 🚀) - DEV Community
url: https://dev.to/sylwia-lask/the-dirty-secret-behind-ai-agents-demo--273d
site_name: devto
content_file: devto-the-dirty-secret-behind-ai-agents-demo-dev-communi
fetched_at: '2026-07-23T11:39:21.881779'
original_url: https://dev.to/sylwia-lask/the-dirty-secret-behind-ai-agents-demo--273d
author: Sylwia Laskowska
date: '2026-07-23'
description: For quite a while now, I've had the feeling that AI agents are surrounded by this mystical aura.... Tagged with node, ai, agents, javascript.
tags: '#node, #ai, #agents, #javascript'
---

Built in 80 lines without heavy frameworks

For quite a while now, I've had the feeling that AI agents are surrounded by this mystical aura. Nobody really knows what they're doing, they're probably going to take over the world soon, and if you want to build one yourself... well, obviously you need a framework.

What if I told you that's not true? You can build your own AI agent in about 80 lines of code.

I have to admit, this week hasn't been easy. A lot has been happening at work. On top of that, I received an automatic rejection email for one of my CFPs. Normally, that would have occupied my mind for maybe five minutes, because conference rejections are just part of the game.

Except... I had actually beenINVITEDto that conference. "You're already accepted, just need to collect the talk details in CFP." Because of that invitation, I turned down two other conference opportunities. Oh well. At least I have September free now.😉

Anyway, life goes on. Today is my birthday, so as a little gift from me to myself (and to all of you!), I wrote this article. 😄 I hope you'll enjoy it!

## Do We Really Need a Framework?

Let's get to the point.

Frameworks like LangChain, CrewAI, or Mastra aren't doing magic. They simplify things like conversation memory, tool execution, retries, fallbacks, etc.

Once you understand the underlying mechanism, it becomes much easier to decide when a framework is actually worth using. And even if you end up using one anyway, you'll understand what's happening under the hood.

So I decided to build a small demo and see how little code an AI agent actually needs.

I wrote an AI agent in Node.js in roughly80 lines of code... okay, okay, thecore loopis about 80 lines. There are still tools, a provider abstraction, and a bit of surrounding logic. But come on,"an AI agent in 80 lines"sounds much better. 😄

Here's the repository:

https://github.com/sylwia-lask/code-review-agent

And since it's my birthday... if you enjoy the project, feel free to give it a ⭐. Only if you actually like it, of course. 😄

## Meet Steve

The application is a simple code review agent. Well... not exactly.

MeetSteve: a software engineer with 15 years of experience reviewing other people's code. Steve doesn't take anything at face value. Sure, he can be a little sarcastic sometimes... but it's hard to argue with his conclusions.

Here's what one of his code reviews looks like:

Or when you have empty diff:

For now, Steve reviews the local Git diff. Which basically means... he's reviewinghimself. So I guess I've built a prototype of the famous self-healing agent that, according to@nitsancohen770, is going to take my job one day.

As you can see, I'm basically helping automate myself out of employment. Maybe it's finally time to start thinking about retirement. 😄

## "An Agent Is Just a While Loop"

In my previous article, I joked about people claiming that an AI agent is nothing more than awhileloop. Well... Mine isn't even awhileloop. It's aforloop, because I wanted to protect myself from accidentally creating an infinite loop and loosing too much money on tokens. 😄

Okay, to be fair, the loop itself doesn't actuallydoanything. It's simply responsible for orchestrating the process. But the funny part is that most agent frameworks are doing something remarkably similar under the hood.

The loop itself was trivial to write. The real challenge was exactly where you'd expect it to be.

Building an AI agent starts with... choosing an LLM. 😄 This time I picked the Gemini API because tokens for projects like this are ridiculously cheap. I'm definitely tempted to build the next version using a local model, but... hold on. 😄

I immediately ran into one issue: some Gemini models were overloaded, so I kept getting503responses. That meant I had to implement something frameworks usually provide out of the box — a simple retry mechanism.

Mine is intentionally very basic. Production frameworks usually offer much more, like exponential backoff, jitter, or automatic fallback to another model.

The next challenge was, of course, writing the right prompt. After that, everything became surprisingly straightforward.

## How Does the Agent Actually Work?

It's much simpler than you might think.

### Step 1: Send the prompt and available tools

We send two things to the model:

* the user's message,
* the list of tools the model is allowed to use.

Here's what the request looks like:

{

 
"model"
:
 
"gemini-2.5-flash"
,

 
"contents"
:
 
[

 
{

 
"role"
:
 
"user"
,

 
"parts"
:
 
[

 
{

 
"text"
:
 
"Please review the current git diff."

 
}

 
]

 
}

 
],

 
"config"
:
 
{

 
"systemInstruction"
:
 
"You are Steve, a senior software engineer with 15 years of experience..."
,

 
"tools"
:
 
[

 
{

 
"functionDeclarations"
:
 
[

 
{

 
"name"
:
 
"getDiff"
,

 
"description"
:
 
"Get the git diff of the current repository..."
,

 
"parameters"
:
 
{

 
"type"
:
 
"OBJECT"
,

 
"properties"
:
 
{},

 
"required"
:
 
[]

 
}

 
},

 
{

 
"name"
:
 
"getFile"
,

 
"description"
:
 
"Read a file from the repository..."
,

 
"parameters"
:
 
{

 
"type"
:
 
"OBJECT"
,

 
"properties"
:
 
{

 
"path"
:
 
{

 
"type"
:
 
"STRING"
,

 
"description"
:
 
"Path to the file relative to the repository root"

 
}

 
},

 
"required"
:
 
[
"path"
]

 
}

 
},

 
{

 
"name"
:
 
"listFiles"
,

 
"description"
:
 
"List files and directories at a given path..."
,

 
"parameters"
:
 
{

 
"type"
:
 
"OBJECT"
,

 
"properties"
:
 
{

 
"path"
:
 
{

 
"type"
:
 
"STRING"
,

 
"description"
:
 
"Directory path relative to the repository root"

 
}

 
},

 
"required"
:
 
[
"path"
]

 
}

 
}

 
]

 
}

 
]

 
}

}

Enter fullscreen mode

Exit fullscreen mode

### Step 2: Wait for the model's response

The model can respond in one of three ways:

* with plain text,
* by requesting a tool call,
* or with both.

If it returns plain text, we're done: that's our final code review. If it asks us to call a tool, we move on to Step 3.

For example, we might receive:

{

 
"candidates"
:
 
[

 
{

 
"content"
:
 
{

 
"role"
:
 
"model"
,

 
"parts"
:
 
[

 
{

 
"text"
:
 
"Let's see what damage we're dealing with today..."

 
},

 
{

 
"functionCall"
:
 
{

 
"id"
:
 
"call_001"
,

 
"name"
:
 
"getDiff"
,

 
"args"
:
 
{}

 
}

 
}

 
]

 
}

 
}

 
]

}

Enter fullscreen mode

Exit fullscreen mode

### Step 3: Execute the tool locally

Now it's our application's turn.

We execute the requested tool locally. For example, runninggit diffor reading a file from the repository, and send the result back to the modelas another message in the conversation.

The tools available in this demo are:

* getDiff
* getFile
* listFiles

In other words, everything a good code reviewer needs. 😄

### Step 4: Repeat until the model is done

Then we simply go back to Step 2. To avoid getting stuck in an infinite loop, I limit the maximum number of iterations to10.

There's one more important detail, though.

Take a look at the next request. Notice that we're sending theentire conversation historyback to the model:

{

 
"contents"
:
 
[

 
{

 
"role"
:
 
"user"
,

 
"parts"
:
 
[

 
{

 
"text"
:
 
"Please review the current git diff."

 
}

 
]

 
},

 
{

 
"role"
:
 
"model"
,

 
"parts"
:
 
[

 
{

 
"text"
:
 
"Let's see what damage we're dealing with today..."

 
},

 
{

 
"functionCall"
:
 
{

 
"id"
:
 
"call_001"
,

 
"name"
:
 
"getDiff"
,

 
"args"
:
 
{}

 
}

 
}

 
]

 
},

 
{

 
"role"
:
 
"user"
,

 
"parts"
:
 
[

 
{

 
"functionResponse"
:
 
{

 
"id"
:
 
"call_001"
,

 
"name"
:
 
"getDiff"
,

 
"response"
:
 
{

 
"result"
:
 
"diff --git a/src/auth.ts b/src/auth.ts
\n
--- a/src/auth.ts
\n
+++ b/src/auth.ts
\n
@@ -12,7 +12,7 @@
\n
- if (password === storedHash) {
\n
+ if (password == storedHash) {
\n
"

 
}

 
}

 
}

 
]

 
}

 
]

}

Enter fullscreen mode

Exit fullscreen mode

And... that's it. The LLM decideswhich tool to useandwhen it's done. Everything else — executing the tools, handling retries, enforcing iteration limits, and orchestrating the loop — is the responsibility of our application.

Simple, isn't it? If you like visualisations, ChatGPT prepared one for us 😉

## What's next?

I'd like to write at least two follow-up articles in the future. One about connecting Steve toMCP, and another about replacing the hosted model with alocal LLM.

But... hold on. One step at a time. 😄

## Bonus: How does the model know it should call a function?

If you only came here to learn how to build an AI agent, you can probably stop reading now. 😄

This section is for the curious ones. Because sooner or later, someone is going to ask:"Sylwia, what are you talking about? You say you're building your own AI agent, but you're just using the Gemini SDK. You send it JSON, you get JSON back."

And, as@darkwiiplayeroften points out, an LLM is basically a very sophisticated next-token predictor, not some magical JSON generator.

So... How does the model know what to do when we send it JSON? What would happen if, instead of Gemini, we used some old local Llama model?

Does the Gemini SDK secretly prepend some special prompt? Or are the models themselves trained for this?

The honest answer is that we don't know all the details. What wedoknow is that models likeGeminiandGPThave native support for tool calling. The SDK is responsible for formatting requests correctly and communicating with the API, while the model itself understands tool declarations and can generate function calls when it decides they're needed.

In other words, if we took an older Llama model, we could still write a prompt explaining how to interpret the JSON and asking it to respond in a specific JSON format.

Then we'd simply callJSON.parse()...

...assuming the model actually returns valid JSON instead of Markdown, an explanation, or a few "helpful" comments it decided to add. 😄

That said, it's worth mentioning that newer open-source models increasingly support tool calling natively as well.

## Epilogue: An agent written by another agent

Let's be honest. It's 2026. This agent was written largely by...another AI agent. 😄

Since I've been an AWS Community Builder for a while now, I cancelled my Claude Code subscription and switched toKiro: an AI IDE with built-in support for multiple LLMs, including Claude, GPT, and Gemini. It costs about the same, but thanks to the program, I get to use it for free.

So far, I'm really enjoying it. It feels a bit like an agent-powered layer on top of VS Code, so I immediately felt at home. I also have the feeling that I'm currently using maybe10%of what it can actually do, so I'm pretty sure I'll write more about it in the future.

Now I'm just hoping AWS will finally send me some swag. 😄 I'm especially dreaming about one of their T-shirts. Years ago, we actually had a political party in Poland calledAWS, so I'd absolutely love to see the expressions on some older people's faces. 😄

AWS... if you're reading this... I'm waiting!! 😄

## Final Thoughts

As you can see, an AI agent doesn't have to start with a framework. Sometimes all you need is an LLM, tools, convarsation history and a simple loop. Everything else is convenience, production hardening, and quality-of-life improvements.

So...

What do you think about Steve? And how do you like this approach to building an AI agent?😄

If you liked this post you can also follow me onLinkedIn.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (17 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse