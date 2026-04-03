---
title: I Shipped Broken Code and Wrote an Article About It - DEV Community
url: https://dev.to/dannwaneri/i-shipped-broken-code-and-wrote-an-article-about-it-98p
site_name: devto
content_file: devto-i-shipped-broken-code-and-wrote-an-article-about-i
fetched_at: '2026-03-09T11:18:12.280460'
original_url: https://dev.to/dannwaneri/i-shipped-broken-code-and-wrote-an-article-about-it-98p
author: Daniel Nwaneri
date: '2026-03-04'
description: 'This is part of a series on what AI actually changes in software development. Previous pieces: The... Tagged with ai, opensource, webdev, productivity.'
tags: '#ai, #opensource, #webdev, #productivity'
---

This is part of a series on what AI actually changes in software development. Previous pieces:The Gatekeeping Panic,The Meter Was Always Running,Who Said What to Whom.

On February 9th, I published an article about a system I built to solve knowledge collapse in developer communities. The Foundation is a side project built in public, iterated in public, mistakes included.

The system was broken. I didn't know yet.

I'd shipped clipboard scraping to GitHub, documented the workflow, written the article. Ctrl+A to select everything. Ctrl+C to copy. Extension intercepts it. Clean, intuitive, logical.

It only captured user messages. Missed every AI response. Missed every artifact. Missed anything above the visible viewport.

The flaw was invisible at review depth. It looked like it worked because I reviewed it at the same speed I built it.

## The Confident Ship

The HTML import came first. Save your Claude conversation as HTML, run a CLI command, done — searchable in under two seconds. It worked. I documented it, shipped it to GitHub, wrote the article.

Then I tried to make it easier. A browser extension — no manual save, no CLI. Just use the conversation normally and it captures automatically.

My approach: listen for copy events.

document
.
addEventListener
(
'
copy
'
,
 
async 
(
e
)
 
=>
 
{

 
const
 
copiedText
 
=
 
window
.
getSelection
().
toString
();

 
// Parse timestamps to detect Claude vs user...

});

Enter fullscreen mode

Exit fullscreen mode

Ctrl+A selects everything. Ctrl+C copies it. Extension intercepts. Logical. Clean. Shipped.

It only captured user messages.

Every AI response gone. Every artifact gone. Anything above the visible viewport — gone. Claude.ai is a React SPA with virtual scrolling. The data lives in JavaScript state, not the DOM. Ctrl+A doesn't select what isn't rendered.

I didn't know any of that when I shipped it. I reviewed it at the same speed I built it.

It didn't feel like a shortcut. It felt like a reasonable solution.

## The Public Reckoning

Five days after the "I built the solution" article, I wrote this:

"I launched The Foundation with big plans. But I underestimated the scope."

Not in a private doc. Not in a GitHub issue. Publicly, on DEV.to, under The Foundation org. Named the overreach. Scaled back.

Nine days after that — Feb 18 — the breakthrough. Real API capture. Real federation. Passage-level search. The fix wasn't a patch. It was a fundamental rethink: stop scraping the surface, use the API that Claude.ai itself uses.

The system that "worked" on Feb 9 and the system that actually worked on Feb 18 shared almost no capture logic.

## The Same Failure, Different Surface

Two weeks after I shipped the clipboard approach, someone commented on my Gatekeeping Panic piece.

Olamide Olanrewaju:"You wrote this with AI."

No engagement with the argument. No specific critique. Just a surface check — and a conclusion.

Last week, Bilgin Ibryam shared Unmesh Joshi's piece on the learning loop and LLMs on X. Unmesh is a Distinguished Engineer at Thoughtworks, author of Patterns of Distributed Systems. The response from Hannes Lehmann:

"I guess the post was written also by AI? See the dashes in every second sentence."

Punctuation as proof. Surface check. Conclusion.

Same failure mode I had with the clipboard approach — reviewing at the speed of generation, not at the depth the work requires.

I reviewed my extension by running it and watching it capture something. It captured something. Seemed solid. I missed what it wasn't capturing.

Olamide reviewed my article by scanning for AI signals. Found one. Missed the argument entirely.

Hannes reviewed a Thoughtworks engineer's piece on learning and LLMs by counting dashes. Found some. Missed the substance.

Generation got cheap. Review didn't follow. So review got cheaper instead.

## The Bottleneck Isn't AI

The panic is misdirected. Again.

Not "AI is generating too much code" — but "we're reviewing at generation speed and calling it due diligence."

Not "AI detectors will save us" — but "surface checks are replacing actual understanding."

Not "the clipboard approach seemed clever" — but "clever isn't the same as correct, and I had no process to tell the difference."

The bottleneck was never generation. Generation has always been faster than review — that's why code review exists, why testing exists, why pair programming exists. Every engineering practice we have is an answer to the same problem: fast output, slow understanding.

AI didn't create the gap. It widened it. Drastically.

And under that pressure, the natural response is to make review cheaper too. Scan for AI signals instead of reading the argument. Run the code and watch it capture something instead of asking what it might miss. Ship the article before you understand the system.

The Foundation's pivot after the reckoning named the antidote directly: verification case studies. "AI code I rejected and why." "Times AI was confidently wrong." Not slower generation — documented rejection.

That's the cultural shift. Not detecting AI. Not banning it. Building the habit of owning what you ship at the depth required to actually own it.

My clipboard approach seemed solid because I had no ritual forcing me to ask: what is this not capturing? Adding that question — before merge, before publish, before ship — is the difference between generation speed and review depth.

It's not complicated. It's just slower than we've decided we want to be.

Someone built a process around exactly this. Kiro calls it property-aware code evolution — before the agent writes a single line, you define the bug condition, what "fixed" actually means, and what was already working that must stay working. The boundary is explicit before execution starts. The scalpel exists. Most teams aren't using it yet.

This isn't a confession. It's a pattern.

I shipped broken code confidently. Wrote an article about it. Got my senses back five days later. Fixed it nine days after that. The receipts are all public — three articles, code on GitHub, the exact moment of reckoning documented in real time.

That transparency is the point. Not because I'm proud of the mistake but because the mistake is useful. More useful than a polished "I built a thing and it worked" story that skips the nine days in between.

Olamide checked for AI signals and missed the argument. Hannes counted dashes and missed the substance. I ran the extension and missed everything it wasn't capturing. Different surfaces. Same gap.

AI made generation cheap. We responded by making review cheap too. That's the actual crisis — not what's being generated, but how shallowly we're checking it.

The fix isn't slower AI. It's deeper ownership. Ask what this isn't capturing before you ship it. Read the argument before you check the punctuation. Document what you rejected, not just what you merged.

Generation will keep getting cheaper. Review won't catch up on its own.

We have to choose to slow down.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse