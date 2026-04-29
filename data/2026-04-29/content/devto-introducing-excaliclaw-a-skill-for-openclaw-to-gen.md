---
title: 'Introducing Excaliclaw: A Skill for OpenClaw to Generate Excalidraw Diagrams - DEV Community'
url: https://dev.to/nickytonline/introducing-excaliclaw-a-skill-for-openclaw-to-generate-excalidraw-diagrams-48k6
site_name: devto
content_file: devto-introducing-excaliclaw-a-skill-for-openclaw-to-gen
fetched_at: '2026-04-29T12:16:38.601007'
original_url: https://dev.to/nickytonline/introducing-excaliclaw-a-skill-for-openclaw-to-generate-excalidraw-diagrams-48k6
author: Nick Taylor
date: '2026-04-25'
description: This is a submission for the OpenClaw Writing Challenge I already use the Excalidraw Model Context... Tagged with devchallenge, openclawchallenge, excalidraw.
tags: '#devchallenge, #openclawchallenge, #excalidraw'
---

OpenClaw Challenge Submission 🦞

This is a submission for theOpenClaw Writing Challenge

I already use theExcalidraw Model Context Protocol (MCP) remote serverin Claude and ChatGPT, but I was curious how it would work in OpenClaw. In Claude and ChatGPT, the MCP renders the diagram inline. I can iterate, see changes in real time, edit directly, and when I am happy, open it in Excalidraw.

OpenClaw does not render the MCP's UI, so the challenge was getting my OpenClaw, McClaw, to generate the scene and hand me back a shareable Excalidraw link instead. Also, meet McClaw!

Setting it up was straightforward. I pointed McClaw at the Excalidraw MCP server repository, the readme includes a link to the remote MCP, and asked it to configure itself. The one thing I had to specify was to usestreamable HTTPinstead of Server Sent Events (SSE) for the MCP transport, since OpenClaw defaults MCPs to SSE (deprecated in the MCP specification in favour of streamable HTTP).

My first test was intentionally tiny: one box that said "hello world." The MCP render worked, but thefirst Excalidraw share linkopened an empty scene. The fix: ask it to export a full native Excalidraw scene payload, not just the MCP streaming element data.

Once I was more specific, itrendered correctly.

From there, I thought everything was fixed so I went with a more complicated diagram. McClaw and I tried a Kubernetes diagram. The boxes rendered, but labels disappeared. A later version had labels, but not the hand-drawn Excalifont. After a few rounds of iteration, McClaw and I landed on a reliable pattern:

* Use explicit text elements instead of relying on Excalidraw/MCP label shortcuts.
* Put text on top of shapes in the draw order.
* SetfontFamily: 1so text uses Excalidraw's hand-drawn Excalifont.
* Include width and height on text elements.
* Keep diagram elements large enough to read in chat previews.
* Route arrows around labels where possible.
* Never return an Excalidraw link unless the exported scene has real elements in it.

You can see the progression in the links generated along the way:

* First hello-world export that opened empty
* Fixed hello-world scene export
* First Kubernetes architecture attempt
* Kubernetes attempt with more explicit text, but still not quite right
* Version with explicit text elements and Excalifont
* Final fresh-run diagram after the skill was tightened up
* The winner

That debugging process turned into a small OpenClaw skill McClaw and I built called Excaliclaw.

The skill packages everything McClaw and I worked out from the failed exports, missing labels, font weirdness, and arrow-routing issues. Now when I ask for a diagram, McClaw has a repeatable recipe instead of the two of us rediscovering those edge cases on every run.

Now arrows actually connect boxes, and labels are grouped with their shapes.

Here's the final working Kubernetes cluster architecture diagram

If you want to use it, install it via OpenClaw:

openclaw skills 
install 
excaliclaw

Enter fullscreen mode

Exit fullscreen mode

## Excaliclaw — ClawHub

Create reliable Excalidraw diagrams in OpenClaw using the Excalidraw MCP, with export-safe labels, Excalifont text, and clear system-diagram structure. Use w...

 clawhub.ai
 

or, install it from GitHub usingnpx skills:

npx skills add nickytonline/skills 
--skill
 excaliclaw

Enter fullscreen mode

Exit fullscreen mode

## nickytonline/skills

### My skills for agentic harnesses

# skills

My personal agent skills.

## Skills

SkillDescriptionexcaliclawCreate reliable Excalidraw diagrams via the Excalidraw MCP, with export-safe labels, Excalifont text, and clear system-diagram structure.

## Usage

### OpenClaw

Install a skill via ClawHub:

openclaw skills install excaliclaw

Enter fullscreen mode

Exit fullscreen mode

Or directly from this repo:

npx skills add nickytonline/skills --skill excaliclaw

Enter fullscreen mode

Exit fullscreen mode

Then invoke it in a prompt, e.g.architecture diagram of my API.

### Claude Code

Skills are invoked with a/prefix, e.g./excaliclaw architecture of my API.

View on GitHub

MCP gives the assistant access to a specialized tool. The skill captures the practical lessons that make it reliable.

If you want to stay in touch, all my socials are onnickyt.online.

Until the next one!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (13 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse