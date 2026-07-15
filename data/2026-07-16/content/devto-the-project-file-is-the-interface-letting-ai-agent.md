---
title: 'The project file is the interface: letting AI agents drive a video editor - DEV Community'
url: https://dev.to/ronak_parmar_033c50d168b5/the-project-file-is-the-interface-letting-ai-agents-drive-a-video-editor-58hd
site_name: devto
content_file: devto-the-project-file-is-the-interface-letting-ai-agent
fetched_at: '2026-07-16T03:37:00.163754'
original_url: https://dev.to/ronak_parmar_033c50d168b5/the-project-file-is-the-interface-letting-ai-agents-drive-a-video-editor-58hd
author: Ronak Parmar
date: '2026-07-09'
description: Last week I open sourced FableCut, a Premiere-style video editor that runs in the browser and that AI... Tagged with javascript, node, ai, showdev.
tags: '#showdev, #javascript, #node, #ai'
---

Clever CSS trick for frame-perfect exports

Last week I open sourcedFableCut,a Premiere-style video editor that runs in the browser and that AI agents canoperate. It hit the front page of Hacker News(thread), and the questionsthere made me realize the interesting part isn't the editor. It's one designdecision:the project file is the interface.

## The usual way, and why I flipped it

Most AI video tools hide the edit behind an API. You calladdClip(),applyFilter(), and the tool owns the state. If you want a human to touch theresult, you build a whole collaboration layer.

FableCut does the opposite. The entire timeline lives in one JSON document,project.json: media, clips, tracks, keyframes, transitions, markers. Theeditor UI reads it. The export renders it. And anything that can write JSONcan edit video: Claude Code through MCP, a Python script,jq, or you with atext editor.

{

 
"id"
:
 
"c_title"
,
 
"kind"
:
 
"text"
,
 
"track"
:
 
"V3"
,

 
"start"
:
 
0
,
 
"duration"
:
 
2.2
,

 
"props"
:
 
{
 
"text"
:
 
"HANDMADE"
,
 
"font"
:
 
"Bebas Neue"
,

 
"glow"
:
 
45
,
 
"textAnim"
:
 
"letter-pop"
 
}

}

Enter fullscreen mode

Exit fullscreen mode

That clip is a glowing kinetic caption. There is no API call that creates it.Writing it into the file IS creating it.

## SSE as a doorbell, not a data channel

The first question on HN was "what's the benefit of SSE here?" Fair question,because the SSE channel does almost nothing, and that's the point.

The server watches the project file withfs.watch, debounces 150ms, andpushes the literal stringchangeto the browser. No payload. The browserre-fetches the project and re-renders. The whole mechanism is about 15 lineson a barenode:httpserver.

Why not WebSockets? Because the data only flows one way. Everything thatwrites (the UI, an agent, a shell script) goes through REST or thefilesystem. The browser only ever needs to hear "something changed, go look."An event with no payload can't arrive out of order, and a missed event costsnothing because the next fetch has the latest state anyway.

## The revision counter, or: how a human and an agent share a timeline

The file carries an integer revision. Every write must bump it. If a writearrives with arevisionthat isn't newer than what's on disk, the serverrejects it with a 409.

This one integer is the entire concurrency model. If I drag a clip in the UIwhile an agent is mid-edit, the agent's stale write bounces, it re-reads,re-applies its change on top of mine, and writes again. No operationaltransforms, no CRDTs, no lock files. It works because edits are coarse(a whole document) and rare (human speed), so last-writer-wins with astaleness check is enough.

## The trick I'm proudest of: frame-accurate CSS animations

FableCut has animated SVG overlays (lower thirds, confetti, sparkles) thatare plain.svgfiles animated with CSS@keyframes. The problem: a videocompositor needs to render the animation state at an exact time, and exportisn't realtime. You can't just let the animation play.

The solution: pause every animation and drive time by hand. The compositorsetsanimation-delay: calc(var(--d, 0s) - t)wheretis the clip's localtime. A negative delay means "you started in the past," so a paused animationwith delay-1.3sdisplays exactly its 1.3 second frame. Deterministic,scrubbable, identical in preview and export. The only rule for SVG authors isto never hardcodeanimation-delayand use the--dcustom property forstaggering instead.

## "You can just give Claude access to ffmpeg"

Someone said this on HN and it deserves a straight answer. For trims,concats, and batch transcodes: yes, absolutely, do that.

The difference is the creative loop. ffmpeg is write-only. The agent builds afilter graph, renders for minutes, and cannot see what it made. You givefeedback, everything re-renders. In FableCut an edit is a JSON diff, the openbrowser updates in 150ms, and the timeline stays editable instead of beingbaked into a filter string. It's not a replacement for ffmpeg anyway: theexport pipeline renders frames in the browser and pipes them to ffmpeg forencoding. FableCut is the state and preview layer between the agent andffmpeg.

## Honest limitations

The compositor is the browser, so export needs a browser open (headlessexport is not there yet). It's Chromium-first. And an AI can misjudge a cutjust fine, which is why the human-in-the-loop part matters more than the AIpart: the agent does the labor, you do the taste.

Full disclosure since HN asked: Claude helped write the README, and largeparts of the editor were built in collaboration with it. That felt fittingfor a tool whose primary user is an AI agent, but the architecture decisionsabove are the ones I'd defend in person.

Repo:https://github.com/ronak-create/FableCut. It's MIT, zero dependencies,onenode server.js. If you build something weird with it, I want to see it.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse