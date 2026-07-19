---
title: Claude Code uses Bun written in Rust now
url: https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/
site_name: hackernews_api
content_file: hackernews_api-claude-code-uses-bun-written-in-rust-now
fetched_at: '2026-07-19T19:27:40.552349'
original_url: https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/
author: Simon Willison
date: '2026-07-19'
description: Claude Code uses Bun written in Rust now
tags:
- hackernews
- trending
---

# Simon Willison’s Weblog

Subscribe

Sponsored by:
 Atlassian — Give your agents a plan. Not a prompt. New Jira capabilities unlock full-context for AI-native software development. Assign tasks to Claude, Cursor, or GitHub Copilot, now directly from Jira. 
Learn more

19th July 2026

InRewriting Bun in RustJarred Sumner made the following claim:

Claude Code v2.1.181 (released June 17th) and later use the Rust port of Bun. Startup got 10% faster on Linux but otherwise, barely anyone noticed. Boring is good.

I decided to have a poke at my own Claude Code installation to see if I could find evidence that it was using Bun written in Rust.

I found these two commands convincing:

strings ~/.local/bin/claude | grep -m1 'Bun v1'

For me this outputsBun v1.4.0 (macOS arm64). The most recent release ofBun on GitHubis currentlyv1.3.14from May 12th, so that v1.4.0 version number in Claude supports them shipping a preview of a not-yet-released Bun version.

(Update: The Rust versionhasbeen released asBun canary- runningbun upgrade --canarywill installthis release.)

strings ~/.local/bin/claude | grep -Eo 'src/[[:alnum:]_./-]+\.rs'

This outputs a list of563 filenames, starting with these:

src/runtime/bake/dev_server/mod.rs
src/runtime/bake/production.rs
src/bundler/bundle_v2.rs

It looks like Bun in Rust is indeed being run in production across millions of different devices. Like Jarred said, "Boring is good".

Update: Here's a neat trickfrom Ajan Raj:

cat > /tmp/bun-version.ts <<'EOF'
console.log("embedded bun:", Bun.version);
process.exit(0);
EOF
BUN_OPTIONS="--preload=/tmp/bun-version.ts" claude --version

This outputs1.4.0for me.

Here'sthe commit from May 17ththat updated the version inpackage.jsonto 1.4.0. That version hasn't been changed since then, but also hasn't yet made it into a tagged release outside ofcanary.

Posted 
19th July 2026
 at 3:54 am

## Recent articles

* Kimi K3, and what we can still learn from the pelican benchmark- 16th July 2026
* The new GPT-5.6 family: Luna, Terra, Sol- 9th July 2026
* sqlite-utils 4.0, now with database schema migrations- 7th July 2026

 

This is anoteby Simon Willison, posted on19th July 2026.

 rust
 
112

 anthropic
 
311

 claude-code
 
122

 bun
 
7

 jarred-sumner
 
3

### Monthly briefing

Sponsor me for$10/monthand get a curated email digest of the month's most important LLM developments.

Pay me to send you less!

 Sponsor & subscribe
 

 

 

 

* Disclosures
* Colophon
* ©
* 2002
* 2003
* 2004
* 2005
* 2006
* 2007
* 2008
* 2009
* 2010
* 2011
* 2012
* 2013
* 2014
* 2015
* 2016
* 2017
* 2018
* 2019
* 2020
* 2021
* 2022
* 2023
* 2024
* 2025
* 2026