---
title: Admit it, you have a favorite AI (just like you have a favorite coworker) - DEV Community
url: https://dev.to/missamarakay/admit-it-you-have-a-favorite-ai-just-like-you-have-a-favorite-coworker-1fa0
site_name: devto
content_file: devto-admit-it-you-have-a-favorite-ai-just-like-you-have
fetched_at: '2026-09-11T14:51:38.827362'
original_url: https://dev.to/missamarakay/admit-it-you-have-a-favorite-ai-just-like-you-have-a-favorite-coworker-1fa0
author: Amara Graham
date: '2026-09-10'
description: A short rant on the Claude, Gemini, and Microsoft Copilot experience. Tagged with ai, productivity.
tags: '#ai, #productivity'
---

An onboarding audit sparks a tool comparison

My mom likes to quote her grandmother who would say things like "I hate yous all equally" when asked who her favorite grandchild was. I feel that, but with AI tools.

If you've worked with me recently, you've probably been my favorite coworker. At least temporarily. It's an easy title to achieve, but hard to hold on to.

Anyway, I just finished a little onboarding audit project (which I may elaborate on later) but for now I want to rant about AI, which didn't help me write this at all so any typo or grammatical "error" you see is an aesthetic choice.

I used 3 AI tools, 4 if you count Google's AI results in a traditional search experience, and pretty much only the chat functionality. Just like everyone has a different working style, everyone probably feels some pull toward one AI experience over another, given that they have that choice and aren't mandated to use a specific one.

Let's dive into Claude, Gemini, and Microsoft Copilot.

## Claude

Admittedly, I've had the most success with Claude, even when it hallucinated a solution earlier this year when I asked if there was a way or tool to measure time to response on a community Slack thread. When I didn't recognize the tool name I asked it to cite it's sources and Claude was like "oops, I made that up." Neat.

Anyway, Claude was the most seamless pair programming experience via Chat. When Claude suggested multiple files needed to be changed, the instructions to change them, and where, were quite clear, but at some point I said "can you just regenerate the project files with the changes", and it did exactly that.

For the most part it stuck to publicly accessible content and didn't grab context from other chats, which is exactly what I was hoping for in this experience. This allowed me to open multiple chats, as different questions, and collect all the responses. A plain ol' vanilla install if you will - so no skills, memories, artifacts, etc. I didn't even put anything in a project.

There were two situations where it didn't hallucinate, but it did need some challenges to responses it provided.

For example, Claude cited NSA secure coding "best practices" and using multiple engines for doing something like redaction. I imagine I will do a future blog on this topic, specifically around redaction with Apryse, but the guidance didn't make realistic sense for an enterprise project. It suggested doing the redaction with one platform/vendor and then verifying the redaction was complete with another platform/vendor. This is maybe reasonable if my budget is unlimited, but when prompted Claude was quick to back down and say "it's not really a citable best practice, but it's my recommendation based on security best practices."

I could see responses like this being a massive problem for people who struggle with pushing back. I was and still am a "why" kid. I'm always asking why and I think that skill is critical when working with AI. I also love demanding "cite your sources" so I can manually review whether they are credible sources or not, or in the case above, clearly see there was no specific source. Just vibes.

I was able to do everything I needed to do on a free tier using Sonnet 5 and only ran into message limits twice over two weeks. But please keep in mind I was doing a lot of context switching and using other AIs. Your mileage may vary.

Also important to note, I wasn't using Claude Code or the VS Code extension. I was just having a little chat with Claude via the desktop app to stay in control of the context and internal data sources as much as possible.

## Gemini

Gemini was an ok experience. Gemini has become my preferred AI for personal use (but admittedly, my personal use is very light). With my husband heavily committed to the Google ecosystem, it's easily accessible and makes sense.

This was my first time doing any sort of programming and debugging with Gemini. It was clear about what errors I should see and where, it was also great about adding more debugging statements and what the expected outcome should be.

It just wasn't as seamless as Claude. Where Claude gave me a full React project, Gemini only produced .JSX and .CSS files and expected me to drop them into a React project. So I manually went and found a sample code React project, got it up an running, then dropped in Gemini's files. If I wasn't starting a net new project and I could actually call myself a React developer, I might have felt like this experience was just fine. I was admittedly surprised it inferred I had an existing React project when it got the same exact prompt Claude did and really should have inferred I was starting from scratch.

Gemini was a free tier experience as well. I used my work browser profile instead of my personal Google account/profile so I wasn't tapping into my family plan. This all happened in a browser tab.

## Microsoft Copilot

If you are looking for Glean on steroids, Microsoft Copilot feels like the place to go. It was so aggressive about sourcing internally that I had to toggle off all the data sources and "Work IQ".

Even then, I never really solved this issue of Microsoft Copilot grabbing or referring to context I didn't want it to have. Separate chats seemed like they were all fair game. It even inferred I was an Apryse employee by referencing the file tree and directory names of an uploaded file. I'm sure someone appreciates that, but for the purposes of this audit, I want to see whatexternalssee. It was just too smart.

Microsoft Copilot also over-answered every prompt I gave it. When I asked about curriculum-based learning or academy experiences, it responded that they didn't appear to exist and then proceed to give me a rated matrix of what was available instead. When I prompted for a more terse answer, it seemed to double down, write another dissertation, and then bold the expected terse answer at the bottom. At that point I didn't bother scrolling back up to read anything because all I wanted was a short, sweet answer.

This was also, by far, the worst coding experience. The initial React project it generated was riddled with old versions of packages that created annoying errors just trying to load the project. I want a paired programming experience, so when I'd take this or other issues back to the AI chat, it's like it would suffer a concussion with immediate memory loss.

"I don't have access to that."

You don't have access... to the code you just generated and gave to me one response above this?

"This looks like AI generated code."

Probably because you, an AI, generated said code.

"If you upload the files, I will have access to them."

You want me to upload the files that you provided me... that I downloaded and made exactly no changes to. K. Cool.

Microsoft Copilot was an enterprise licensed experience. I never saw anything about tokens or message limits, but getting a response was often quite slow. Maybe it's important to mention I did everything via chat vs. cowork and I was working in a browser tab.

## What's next?

Claude wins, but it wasn't really a contest.

It's entirely possible I ran into some user error with all of these tools. It's also possible I'm generating opinions about what AI is best for what exercise. For this experience I just wanted quick answers without a lot of setup and fuss, and for better or worse I got that. Low investment, high output.

For now, I'm shifting gears to work on other projects and will have different use cases, and will probably spend a bit more time trying to make Microsoft Copilot a more usable experience for me. I'll probably also look into Claude, Claude Code, and specifically the VS Code extension, so long as that's been blessed by my employer as an option. Otherwise, I'll be reaching out to the engineers about what they are using.

Do you have a favorite AI? Or a favorite coworker? I'm here forallthe hot gossip. Drop a comment and let me know.

Cover photo bySteve A JohnsononUnsplash

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (14 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse