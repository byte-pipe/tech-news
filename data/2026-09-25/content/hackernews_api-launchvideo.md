---
title: LaunchVideo
url: https://launchvideo.io
site_name: hackernews_api
content_file: hackernews_api-launchvideo
fetched_at: '2026-09-25T15:44:44.917673'
original_url: https://launchvideo.io
author: iacguy
date: '2026-09-24'
description: Paste a URL or a prompt. Get a launch video, written and rendered by Opus 5.5 on an OpenComputer serverless agent. No video model.
tags:
- hackernews
- trending
---

URL
Prompt
choose one
try an example
Ship it

examples

## Made by this page, untouched.

Each one is a single run: a URL or a prompt in, an MP4 out. No edits.

0:
31

NVIDIA

nvidia.com

use this input →
0:
34

Jev, by TypeSafe AI

typesafe.ai

use this input →
0:
33

OpenComputer

opencomputer.dev

use this input →
0:
34

Linear

linear.app

use this input →
0:
32

Infera (from a prompt)

“make a modern slick and punchy video for a modern startup that works on inference”

use this input →

how it runs

## A serverless agent on OpenComputer. Yours in one click.

The whole product is one agent file, three tools, and this form. OpenComputer runs the agent, the microVM it renders in, the model gateway, and the session API the page polls.

Agent
One OpenComputer serverless agent, defined in TypeScript and deployed with 
opencomputer deploy
. No framework, no queue, no server of ours.
Model
anthropic/claude-opus-5.5 through OpenComputer's model gateway. Roughly 90k input and 15k output tokens per film, most of it the HTML itself.
Runtime
Every job is one session in a fresh microVM: Amazon Linux 2023 on arm64, 4 vCPU, 8 GB RAM, Node 22. The first tool call installs Playwright's headless Chromium and a static ffmpeg (about a minute); the VM is thrown away after.
Tools
Three 
defineTool
 functions. web_fetch returns page text plus title, headings, the most used hex colors, and Google Fonts. check_scene loads the film and reports JS errors and the visible text at sample timestamps. render_video renders and uploads.
Rendering
No video model. The page's clocks (requestAnimationFrame, timers, Date, CSS and Web Animations) are replaced with a virtual clock, so every frame is a deterministic seek. 1920x1080 at 30 fps, JPEG frames piped into libx264, crf 18.
Storage
The agent holds no secrets. The form mints a Vercel Blob upload token scoped to one path for three hours, parks it in a per-job manifest, and the tool fetches it by job id. The finished MP4 is a public Blob URL.
Control plane
This page uses the same API the CLI does: create a session, send one turn, poll the event stream (tool.started, tool.completed, turn.completed) to show progress, and treat the MP4 appearing in Blob as done.
// opencomputer/agents/director/agent.ts
import { useInput, useModel, useTool } from "@opencomputer/agent";
import { checkScene, renderVideo } from "./tools/scene.js";
import { webFetch } from "./tools/web.js";

export default function Agent() {
 const input = useInput(); // the JOB block from the form
 useModel("anthropic/claude-opus-5.5");
 useTool(webFetch); // read the product's site
 useTool(checkScene); // load the HTML, report errors + visible text
 useTool(renderVideo); // headless Chromium → ffmpeg → Blob
 return `You are a motion designer who writes code. ...`;
}

Deploy this agent

One click. Free account, the agent lands in your project with its tools and prompt.

Clone the repo

diggerhq/shipvideo: the agent, the renderer, and this web app.

Build your own agent

The quickstart: a TypeScript file, a deploy, a session. Ten minutes.

$
npx opencomputer template deploy https://github.com/diggerhq/shipvideo
copy

Everything above is in the repo, andone click deploys it to your account. The idea comes fromDeedy's poston Opus 5.5 and instructional video: the model writes the film as code, and code renders the same every time.