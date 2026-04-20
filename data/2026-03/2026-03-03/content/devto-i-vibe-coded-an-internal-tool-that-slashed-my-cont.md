---
title: I vibe-coded an internal tool that slashed my content workflow by 4 hours - DEV Community
url: https://dev.to/dumebii/i-vibe-coded-an-internal-tool-that-slashed-my-content-workflow-by-4-hours-310f
site_name: devto
content_file: devto-i-vibe-coded-an-internal-tool-that-slashed-my-cont
fetched_at: '2026-03-03T06:00:50.138061'
original_url: https://dev.to/dumebii/i-vibe-coded-an-internal-tool-that-slashed-my-content-workflow-by-4-hours-310f
author: Dumebi Okolo
date: '2026-02-27'
description: One of the biggest challenges I face as a content expert is repurposing my written blogs for social... Tagged with webdev, ai, nextjs, tooling.
tags: '#webdev, #ai, #nextjs, #tooling'
---

One of the biggest challenges I face as a content expert is repurposing my written blogs for social media. Before now, I had to ask AI for summaries or try to get them myself. I became very busy recently, and I don't have time for that anymore.The best solution for me was building a tool that helps me generate social media content from my blog and posts on my behalf.I was in a meeting of content professionals recently. A key point that was hammered on regarding the use of AI in content creation is the need to maintain a strict Human-in-the-Loop (HITL) workflow.This resonated well with me.I had initially planned to build an agent to automate and schedule social media posts. This, however, leaves out the HITL factor, so I restrategized.

Here is the technical breakdown of how I built an Agentic Content Engine using Next.js 15, Gemini 3.1 Pro, and Discord Webhooks.

## Agentic Human-in-the-Loop (HITL) architecture

The Problem: The "Context Gap"Most AI social media tools are just wrappers for generic prompts. They don't know my research, they don't know my voice, and they definitely don't know the technical nuances of my articles.So,I needed a tool that:

* Reads my actual dev.to articles.
* Strategizes a 3-day multi-platform campaign.
* Displays it in a way that I can audit, edit, and then—with one click—Deploy.

Even though this app was "vibe coded" (shoutout to the AI for keeping up with my pivots 😂😂), the architecture is solid.

The core philosophy of this build is Agency over Automation. The agent doesn't just act; it reasons, structures, and then waits for human approval before posting

### The AI Stack

* Reasoning Engine:Gemini 3.1 Pro (Tier 1 Billing). I opted for Pro over Flash to handle complex instruction following and strict JSON schema enforcement.
* Frontend:Next.js 15 (App Router) for server-side rendering and SEO efficiency.
* Styling:Tailwind CSS with@tailwindcss/typographyfor professional markdown rendering.
* Deployment:Discord Webhooks for an immediate, zero-auth execution pipeline.

## Handling AI Hallucinations in Next.Js

A common failure in vibe coding, I have found, is the LLM returning "chatty" text when the UI expects structured data.To solve this, I implemented a Strict JSON Enforcement pattern in the API route.

Gemini often wraps its JSON output in markdown code blocks. If you pass this directly toJSON.parse(), the app crashes.

To solve this, I usedSanitization Middleware.I built a regex-based sanitization layer to strip the noise and ensure the frontend receives a clean array.

// app/api/generate/route.ts

const

rawOutput

=

data
.
output
;

// The raw string from Gemini

// Regex to extract only the JSON content

const

cleanJson

=

rawOutput
.
replace
(
/``
`

{
%

endraw

%
}

json
|

{
%

raw

%
}

```/g, "").trim();

try {
 const campaignData = JSON.parse(cleanJson);
 return NextResponse.json({ campaign: campaignData.campaign });
} catch (error) {
 console.error("JSON Parsing failed:", rawOutput);
 return NextResponse.json({ error: "Failed to parse Agent strategy" }, { status: 500 });
}

Enter fullscreen mode

Exit fullscreen mode

## UI/UX Strategy: The Kanban "Board" Approach

The v1 of the UI was so messy. The tool worked but you'd have to dig through mountains of text to even understand what was going on.I tried formatting it into a table for some structure. Somehow, that was worse!Finally, to optimize for a"Human-in-the-Loop"workflow, I moved to a columnar dashboard.Social posts, especially threads on X, can be long, and that would have made even the boards to be clumsy and unkempt.To keep the UI clean, I built aPostCardcomponent that caps content at250 characterswith a state-managed "Read More" toggle.

const

[
isExpanded
,

setIsExpanded
]

=

useState
(
false
);

const

displayContent

=

isExpanded

?

content

:

content
.
substring
(
0
,

250
)

+

"
...
"
;

Enter fullscreen mode

Exit fullscreen mode

This ensures the user can audit the text without scrolling for "miles."

## Photo dump: Agentic Content Flow in Action

1. The Starting Point
Here’s the clean, minimal dashboard before the magic happens. I wanted it to feel like a professional "Command Centre," not a messy chatbot window.

1. The 3-Day Campaign Map
Once I paste my URL, the Agent goes to work. It returns a structured 3x3 grid. I added a 250-character truncation with a "Read More" toggle because, let's face it, nobody wants a wall of text when they're trying to strategise.

1. The Deployment
Here is the best part. I hit "Post to Discord," and boom—success. No manual copy-pasting, no switching tabs. It’s live.

## What's next

This is what I have built so far. I am calling it BloggerHelper v1My next updates are:

1. Integrating the X and LinkedIn feature.
2. Putting more work into the context tank. So far, the agent's context has been obtained from the article and some instructions in the agents_instruction.md file. I will work more on this
3. Putting an edit feature, where I can edit a post before it goes out.
4. Making it take in more context than just my blog posts

## Conclusion: The Engineering of Presence

Even though this tool was designed to help me cut down on work hours, it was also to take me from just a technical writer to a content engineer/architect, where my primary goal isn't to just create content but create solutions that make for easy content flow.Also, as I position myself as an AI influencer, I want to show myself building more with AI and evangelising its adoption.

Let's connect onLinkedIn!

What’s your take on Agentic Workflows? Are you building for full automation, or are you keeping the human in the loop?

Let’s discuss below. 👇

### UPDATE!!!!

I just used my tool to get my social media caption/content for this post. See below.

You can try it outhere, but mercy on my API credit!!

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (24 comments)


Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
