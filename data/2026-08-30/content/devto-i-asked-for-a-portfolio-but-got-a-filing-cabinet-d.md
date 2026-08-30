---
title: I Asked for a Portfolio but Got a Filing Cabinet - DEV Community
url: https://dev.to/anchildress1/i-asked-for-a-portfolio-but-got-a-filing-cabinet-4ef8
site_name: devto
content_file: devto-i-asked-for-a-portfolio-but-got-a-filing-cabinet-d
fetched_at: '2026-08-30T15:12:00.571624'
original_url: https://dev.to/anchildress1/i-asked-for-a-portfolio-but-got-a-filing-cabinet-4ef8
author: Ashley Childress
date: '2026-08-29'
description: Every AI redesign of my portfolio looked different and was the same filing cabinet underneath. What a style guide couldn't fix — and the one instruction that did. Tagged with ai, webdev, design, ux.
tags: '#ai, #webdev, #design, #ux'
---

Metrics revealed the redesign was downright scary

🦄 I really am trying to get back to writing more and decided to write up a quick, fun post about my arguments with all of my AI friends. It took me nearly a week to redesign my portfolio site and most of that time was spent frustrated that nothing was working.

So here's the quick read on what went wrong and how I finally fixed it. "Good enough," anyway.

## Yeah... And? 🪧

It was no secret my original portfolio site looked AI-generated: that's exactly what it was. So when that was the feedback I received, my response was mostly "yeah... and?"

It's also no secret that I am not a UX person. I have no clue what most of these elements are even called, let alone what to do with them. My version of an animated page is literally "make it move".

The good news is I don't need to know all that to build a page that doesn't completely suck. And yes — "not terrible" is the bar I'm aiming for here, because anything else would be me pretending to know what I'm doing.

## Scary Was a New Low 🩻

I pulled the metrics — something I rarely do — and ran across an anonymous input I wasn't looking for.

Scary.

I knew it wasn'tgreat. Butscarywas a new low for me, even in the realm of design.

So I sent Gemini out to crawl my site and generate a list of all the AI tells. The answer was really "the whole thing is terrible" — everything from the color to the index card implementation. The only human thing on the whole site was the about profile (which was good seeing as how I actually wrote most of that).

Alrighty then.Now is as good of a time as any to just rewrite the entire implementation.

## Every One of Them Was a Database 🪤

I had tried usingImpeccableas a style guide along with Claude Design — neither one got rid of the AI generated look and feel. Claude and I ended up with more than 10 independent designs of my site, and I hated all of them more than the first.

I didn't realize until later that every single one of these designs that I hated was describing an archive. Every one was a browsing interface — filters, counts, dropdown, search — andnot one described me as the human behind it all.

The problem is that I kept doing the same thing. I was sick of purple, my goto for awhile, so I tried a rainbow — which made things a million times worse. Blue, green, pink, red, orange, and finally yellow, the one I liked best, but nothing helped the overall look and feel.

## Artsy, Not a Dashboard 🪙

Then, in complete frustration, I told Claude I wanted an "artsy page" not a dashboard.

That vibe clicked somewhere. I finally had options I didn't completely hate.

Yellow looked fine in dark mode. Light mode had no pizazz and looked like a washed out attempt by somebody who didn't know what they were doing — which was no surprise, seeing as how that's exactly what it was. So I went back to quizzing the AI for potential ways to make that work.

These rules are where I ended up after doing a ton of research and arguing with myself every time I actually had to make a decision:

1. No eyebrow text anywhere— yes, I learned a new word for the text that sits at the top of a section.
2. One single hueaccent, modified with opacity when needed.
3. Two opposing fonts: one with personality, one that stays legible.
4. Require offsetsand mismatched text elements.
5. Display judgement.Stop deferring every design decision to the AI — pick one now and change your mind later.
6. Remember the goal is todescribe the human, not the work.

## Not Terrible Is a Real Bar 🧭

The highlighter was a combination of options squished together in a single ah-ha moment.

You can also see the full page athttps://anchildress1.dev.

When I asked Gemini to review my previous website, I summarized the whole report as "this whole thing is terrible". I sent it out to rereview the updated version and got back "not completely terrible". I filed that as a win.

It took me more than ten designs to work out why the about profile was the only thing that ever passed. Everything else was just a very well-organized way to look at my work.

Describing the human was the part I had to do myself.

## Ashley ChildressFollow

Distributed backend specialist. Perfectly happy playing second fiddle—it means I get to chase fun ideas, dodge meetings, and break things no one told me to touch, all without anyone questioning it. 😇

## 🛡️ Filed Under Corrections

While interviewing me about my own website, Claude invented a product I've never built and a redesign that never happened. I fixed that but let it write this footer.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse