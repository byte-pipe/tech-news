---
title: Never forget to enter the Stern Grove lottery again! - DEV Community
url: https://dev.to/entire/never-forget-to-enter-the-stern-grove-lottery-again-31i5
site_name: devto
content_file: devto-never-forget-to-enter-the-stern-grove-lottery-agai
fetched_at: '2026-06-26T19:36:12.885490'
original_url: https://dev.to/entire/never-forget-to-enter-the-stern-grove-lottery-again-31i5
author: Lizzie Siegle
date: '2026-06-26'
description: Browser automation with Playwright, Python, GitHub Actions, and Entire to auto-enter San Francisco Stern Grove concert lotteries each week!. Tagged with ai, playwright, githubactions, browserautomation.
tags: '#ai, #playwright, #githubactions, #browserautomation'
---

It's summer in San Francisco, which means that every week I forget to enter the lottery for the freeStern Grove Music Festival.

Solution? I did what any reasonable developer would do instead of just setting a calendar reminder: I built a Python script that runs weekly via GitHub Actions, scrapes the festival website with Playwright, and auto-enters the lottery for me.

The fun part ishowI built it. I described what I wanted to a coding agent (I've done a lot of browser automation to automate tennis court bookings, make data visualizations, etc), andEntirerecorded every prompt, tool call, and output along the way, so I have a complete, auditable record of how the whole thing came together. If you want to retrace the entire build yourself,here's the live session. Let me walk you through it:

## It started with one message

The entire (lol) project began with a single message to my coding agent (I used Claude Code, but any agent works!) I gave it the rules of the game:

The Stern Grove lottery opens six weeks before each show at 10:00 AM and stays open for one full week to enter…

I also handed it the exact HTML for the entry button. Stern Grove runs its ticketing throughTixologi, so the agent needed to know what it was dealing with.

Then I told it about the secrets my GitHub Action would have access to:

* First name
* City
* Email
* AResendAPI key (for notifications)
* The "from" email address
* Zip code
All of these live as encrypted secrets in GitHub Actions--never committed to the repo--and I made sure the agent understood that constraint up front.

## The architecture it proposed

Before writing a line of implementation, the agent explored the spec, asked one clarifying question, and proposed a clean design:

* lottery.py— the entry point, triggered by a GitHub Actions cron schedule
* browser.py— all the Playwright logic: web scraping and browser automation
* state.py— loads and savesentered_lotteries.jsonso we never double-enter
* notify.py— success and failure emails via Resend
State persistence was the clever bit. Instead of standing up a database for a once-a-week job, the entered lotteries are tracked in a JSON file that getscommitted back to the repoafter each run:

{

 
"entered"
:
 
[

 
{
 
"event_id"
:
 
"abc123"
,
 
"show"
:
 
"Show Name"
,
 
"entered_at"
:
 
"2025-06-21T10:02:00Z"
 
}

 
]

}

Enter fullscreen mode

Exit fullscreen mode

The cron schedule lives in the workflow file:

# .github/workflows/lottery.yml

on
:

 
schedule
:

 
-
 
cron
:
 
"
0
 
17
 
*
 
*
 
1"
 
# weekly check

 
workflow_dispatch
:

Enter fullscreen mode

Exit fullscreen mode

## Inspecting before automating

Here's a step worth highlighting. Before touching any browser logic, the agent did alive inspectionof the actual Stern Grove page — specificallywindow.tixologiWidget.concerts— to learn the real data shape rather than guessing.

Tixologi is a ticket and event management platform. That inspection documented the precise field names, the ISO 8601 date format, and the event ID structure. Oneconsole logit captured saved a lot of debugging later:

// What the page actually exposes

window
.
tixologyWidget
.
concerts

// → [{ eventId, name, startDate: "2025-07-13T19:00:00Z", ... }]

Enter fullscreen mode

Exit fullscreen mode

Grounding the implementation in real, observed data instead of assumptions is a major differentiator between code that works on the first real run and code that fails silently in production.

## Pushing state back to the repo

state.pydoesn't just read the JSON — after a successful entry it commits and pushes the update using a GitHub Personal Access Token (PAT), so the next run knows what's already been done:

def
 
commit_state
(
token
:
 
str
)
 
->
 
None
:

 
subprocess
.
run
([
"
git
"
,
 
"
add
"
,
 
"
entered_lotteries.json
"
],
 
check
=
True
)

 
subprocess
.
run
([
"
git
"
,
 
"
commit
"
,
 
"
-m
"
,
 
"
Update entered lotteries
"
],
 
check
=
True
)

 
subprocess
.
run
([
"
git
"
,
 
"
push
"
],
 
check
=
True
)

Enter fullscreen mode

Exit fullscreen mode

## The review loop caught a real bug

When the agent addednotify.py, a reviewer sub-agent immediately flagged two issues in the diff:

1. It was usingprint()statements instead of theloggingmodule.
2. It had duplicated the Resend API key (for email) initialization.
The agent fixed both before moving on to the next task. That's the task → review loop doing exactly what it should — catching the kind of sloppiness that usually only surfaces weeks later.

import
 
logging

logger
 
=
 
logging
.
getLogger
(
__name__
)

resend
.
api_key
 
=
 
os
.
environ
[
"
RESEND_API_KEY
"
]
 
# initialized once

def
 
notify_success
(
show
:
 
str
)
 
->
 
None
:

 
logger
.
info
(
"
Entered lottery for %s
"
,
 
show
)

 
resend
.
Emails
.
send
({
 
...
 
})

Enter fullscreen mode

Exit fullscreen mode

## How to retrace every prompt, tool call, and output

This is the part I do genuinely find handy: I didn't have torememberhow the automation got built, becauseEntirecaptured all of it. Asessionin Entire is the complete record of an AI coding interaction, ie every prompt, response, tool call, and file change. You can browse mine at thesession link above.

Here's how to navigate it:

* Find the session.Sessions live in theSessionstab on a checkpoint detail page. Each row shows the agent that ran (Claude Code, in my case), a step count, the opening prompt, and a timestamp. Click one to open its timeline.
* Read the timeline.The session timeline shows the conversation in order — my prompts, the agent's responses, expandable tool calls, and runtime tags. A metadata panel summarizes themodel,duration, andtokenusage for the run.
* Expand any tool call.Tool calls render as inline rows you can expand to see the exact arguments and results. For file edits, the expansion shows the diff right there.
* Filter the noise.A filters rail on the right lets you toggle what's visible — prompts, responses, intermediate steps, checkpoints, and tool calls (further broken down into file edits, bash, read, and other). This is how I unchecked things to get a cleaner view when I just wanted something more high-level.
* Drill into sub-agents.When the agent spun up that reviewer sub-agent via Claude Code'sTasktool, Entire captured it as its own session with its own transcript and tool calls, rolled up into the parent checkpoint's totals. That's exactly where you can see the review loop that flagged theprint()/logging issue.
* Jump to the code.Every session links back to its Git commits through anEntire-Checkpointtrailer, so you can open the matching checkpoint or the underlying commit on GitHub. The metadata itself lives on a distinct separateentire/checkpoints/v1branch, which keeps your main history clean.
So the screencast you're watching isn't the only record-- the full reasoning behind every line is sitting in that session, ready to rewind through.

## It didn't work at first!

I'll be honest: the first real run failed. CI rarely cooperates on the first try, and this was no exception. Two environment issues bit me:

1. Ubuntu version drift.I had to pin the runner toUbuntu 22.04for Playwright compatibility.ubuntu-latesthad quietly become Ubuntu 24.04 in 2025, and thelibasound2package was renamed in the process.

2. Chromium dependencies.I ended up installing the Chromium deps manually with the correct Ubuntu 24.04 package names instead of relying on Playwright's bundled installer.

The fix went from this:

# before

-
 
run
:
 
playwright install --with-deps chromium

Enter fullscreen mode

Exit fullscreen mode

to explicit apt installs plus a leaner Playwright step:

# after

-
 
run
:
 
|

 
sudo apt-get update

 
sudo apt-get install -y libasound2t64 libnss3 libnspr4 # ...correct 24.04 names

-
 
run
:
 
playwright install chromium

Enter fullscreen mode

Exit fullscreen mode

## Success!

Finally, it ran cleanly. I got the confirmation email straight from Stern Grove and Resend.

The stack came together nicely:

* Playwrightfor the browser automation
* GitHub Actionsfor the weekly cron schedule and secret management
* Resendfor success/failure notifications
* Acoding agent(Claude Code) to build it, with a review loop that caught real bugs
* Entirecapturing every prompt, tool call, and output, linked to the commits
I can't wait to see what you build with the same pieces, and now you (and I) won't forget to enter the Stern Grove lottery this summer.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse