---
title: Friendship ended with Deno, now Node is my best friend – David Bushell – Web Dev (UK)
url: https://dbushell.com/2026/10/03/deno-to-node/
site_name: hackernews_api
content_file: hackernews_api-friendship-ended-with-deno-now-node-is-my-best-fri
fetched_at: '2026-10-06T17:04:36.916325'
original_url: https://dbushell.com/2026/10/03/deno-to-node/
author: David Bushell
date: '2026-10-05'
description: The one where I go crawling back.
tags:
- hackernews
- trending
---

# Friendship ended with Deno, now Node is my best friend

Saturday

3Oct2026

It’s finally time I go crawling back toNode!

I’ve been using Node heavily this month on aSvelteKitclient project. When did Node get so good‽ Deno has been my go-to runtime for so long I forgot how to Node. Now I’m back, I find all the ECMAScript†sugar is supported and the old annoying APIs have been replaced or modernised. Most importantly, I never have to seerequire().

†Doesn’t seem like thatOracle trademark disputewill see a positive end :(

## Package management

Theofficial Node docsrecommend piping an internet script straight to bash (we never learn) to installNVMto manage Node & NPM. My (ancient) experience with NVM and NPM hasn’t been stellar. I heardFast Node Manager (FNM)was better to switch Node versions. Obviously I roll bleeding-edge but I have client projects that demand stability.

I opted forPNPMtoo to avoid gettingimmediatelypwned. (The “M” in NPM stands for “malware.”) Some scripts I use have hard-coded binary names‡, so I added two aliases:

alias
 
npm
=
pnpm

alias
 
npx
=
pnpx
Copy Code

Maybe that’s a crime but so far it’s worked flawlessly.

‡Edit: I might be confusing the time I symlinked various binaries. The aliases do help when copying steps from install guides that assume NPM is installed.

PNPM also blocks post-install scripts. Does NPM still yolo those?

I added additional settings topnpm-workspace.yamlto delay malware updates.

minimumReleaseAge
:
 
1440

trustPolicy
:
 
no-downgrade
Copy Code

At first I tried setting the minimum release age to “one month” because it takes Microsoft at least that long to remove reported malware. This caused dependency issues where PNPM struggled to match suitable versions. I settled for “one day”; long enough to allow some other sucker to beta test the next Shai‑Hulud.

## TypeScript

Node can now run TypeScript without throwing a tantrum like a baby if the stars don’t align. That said, one does not simply publish TypeScript packages to NPM.

error:
 
[ERR_UNSUPPORTED_NODE_MODULES_TYPE_STRIPPING]:

Stripping
 
types
 
is
 
currently
 
unsupported
 
for
 
files
 
under
 
node_modules
Copy Code

Why? Just strip the types bro, I know you can! Let me sign a deal with the devil!

To discourage package authors from publishing packages written in TypeScript, Node.js refuses to handle TypeScript files inside folders under anode_modulespath.

Node.js v26.10.0 documentation

This restriction is philosophical rather than technical. I get it though. TypeScript is a Microsoft product. Opening that floodgate would pollute the entire ecosystem. Nobody wants more Microsoft. I’d love to see light “native types” in ECMAScript. There aretype annotation proposals. I suspect I’ll be retired before those bear fruit.

No TypeScript packages mean I need to find the latest churnware slop to bundle my stuff.Tsdowndid the trick, with only two additional dotfiles. Not thrilled about that (every dotfile represents a mistake). I suppose I break even after deletingdeno.jsonetc.

Speaking of Microsoft lock-in, because theywrecked GitHubI’m self-hosting my ownForgejo instance.NPM limitationsmean my packages have lost “provenance”. I had to configure thePNPM trust policyto allow my own stuff. Fun times!

## Migrating my website

My final test for Node was converting mystatic site generatorfrom Deno. Not many Node versions ago this would have required a major refactor. Today withNode v26.10.0I found surprisingly little work to do.

The only required changes were to replace Deno’s file system API withnode:fs— which is vastly improved from what I remember (literally ~10 years ago). Aside from that, I had to replaceDeno.servewithHono’s node adapter(a wrapper aroundnode:http).

After this minimum-viable migration I was shocked to see15% faster builds. My codebase still favours idiomatic Deno. I bet I’m leaving performance on the table by not using other built-in Node APIs. That’s something to explore later. The only further change I made was to replace Deno’s@std/pathwithnode:pathwhich is a straight import swap.

So if I were to TL;DR in the middle: Node got a glow-up, wow!

You’ve probably known this for a while. I kept using Deno out of habit and familiarity. And I haven’t exactly been enthused to write server-side JavaScript recently.

## Deno’s decline

I’m burying this part because it’s flogging a dead horse. Ultimately, Deno failed when they allowed the Silicon Valley Circus to define “success”. Deno went from an innovative modern JavaScript runtime to a boring start-up withuncompelling products. Half the employees were laid off and what’s left are tweeting AI fantasies and vibe-coding Temu Cloudflare.

There is no reason to use the Deno runtime today.Deno Land Inc.stopped innovating that years ago. Node has slowly but surely caught up, even surpassing Deno in places.

What finally pushed me away was:

* Broken ZSH integration for weeks
* JSR’s aggressive “429 (Too Many Requests)”
* Bug(s) that made Deno choke on concurrent HTTP requests

Basically stuff that made it borderline unusable on top of my other criticism. JSR support were very quick to delete my account on request. I don’t like leaving dead profiles around the internet. None of my packages are visible but old versions remain installable.

It was fun early on but now it’s time to say goodbye.

brew
 
uninstall
 
deno
Copy Code