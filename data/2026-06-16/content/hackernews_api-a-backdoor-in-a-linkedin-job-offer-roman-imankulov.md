---
title: A backdoor in a LinkedIn job offer - Roman Imankulov
url: https://roman.pt/posts/linkedin-backdoor/
site_name: hackernews_api
content_file: hackernews_api-a-backdoor-in-a-linkedin-job-offer-roman-imankulov
fetched_at: '2026-06-16T12:37:09.369309'
original_url: https://roman.pt/posts/linkedin-backdoor/
author: lwhsiao
date: '2026-06-15'
published_date: '2026-06-15T00:00:00+00:00'
description: A fake recruiter, a crypto repo, and a remote code execution payload hidden in a test file.
tags:
- hackernews
- trending
---

# Roman Imankulov

Full-stack Python developer. BuildingSmello.

search results (esc to close)
15

Jun 2026

# A backdoor in a LinkedIn job offer

table of contents

Last week, I got a LinkedIn message from a recruiter at a small crypto startup. We exchanged a few messages over a couple of days, she described a broken proof-of-concept they needed a lead engineer for, and then sent me a public GitHub repo to review. Specifically, she asked me to “check out the deprecated Node modules issue.”

It’s not uncommon to ask for a review of an existing codebase, but something felt off and raised an alarm in my head, so I decided to get a bit extra paranoid.

Instead of cloning and installing dependencies, I spun up a throwaway VPS on Hetzner, cloned the repo there, and pointedPiat it in read-only mode, with only file-reading tools enabled:

pi --tools read,grep,find,ls

I asked the agent to review the codebase and flag anything suspicious. It stopped almost immediately atapp/test/index.js.

## The backdoor

The repo felt like a React frontend with a Node backend. The trap was inapp/test/index.js, about 250 lines disguised as a test suite. Inside, a URL is assembled from fragments:

const
 protocol 
=
 
"https"
,

 domain 
=
 
"store"
,

 separator 
=
 
"://"
,

 path 
=
 
"/icons/"
,

 token 
=
 
"77"
,

 subdomain 
=
 
"rest-icon-handler"
,

 bearrtoken 
=
 
"logo"
;

These combine intohttps://rest-icon-handler.store/icons/77.

Then, buried between walls of commented-out tests, the payload runs anything the server sends back to your machine.

The payload on line 225, hiding in plain sight between commented-out tests.

## How it triggers

The file doesn’t wait for the tests to run.app/index.jsitself executesconst test = require('./test'), which loads and runsapp/test/index.js.

package.jsonwiresapp/index.jsinto startup:

preparerunsapp:pre, which isnode app/index.js.

Thepreparescript is the important one. npm runsprepareautomatically afternpm install, so just installing dependencies executes the backdoor.

The instruction to “check out the deprecated Node modules issue” was bait to get me to runnpm install.

I could have let the payload run in the sandbox and watched what the server sent back as the second stage, but I stopped there. A repo that runs whatever a server hands it was enough evidence.

## A borrowed identity

The commits in the repo were authored under the name and email of a real developer, a full-stack engineer with an ordinary LinkedIn profile, a personal website, and a GitHub account with a long history. I messaged him, pretending I’d inherited the codebase and had a few implementation questions, to see how he’d react.

He told me he’d never worked for them. He’d been impersonated on GitHub before and had a repo taken down over it, and he had nothing to do with this one. He was reporting these repos too.

The whole commit history, 39 commits, attributed to one developer who’d never touched the repo.

## A second borrowed identity

The recruiter’s profile belonged to a real arts journalist, a well-known one I looked up later, with a long cultural background and nothing technical on it. When I played along and told her I couldn’t get the project to install, the journalist instantly turned into an expert on npm and Node versions. It was quite amusing, I’d say.

The non-technical recruiter, suddenly debating Node versions and pushing me to run npm install.

## This can happen to anyone

I’ve heard of these attacks and read about them on HN, but when one came after me it still caught me a bit off guard. I suspected something from the first few messages, but on a more tired or rushed day, I could easily have runnpm installbefore thinking it through. So, if you get a LinkedIn message asking you to review a repo, a bit of paranoia and good security hygiene never hurts.

Another takeaway is that reviewing the code with a read-only agent turned out more productive than reading it myself. The backdoor was dressed up as sloppy beginner code, but the agent flagged it in seconds.

I reported the repo to GitHub and the recruiter to LinkedIn. So far nothing has changed and the code is still up.

* Security

Hey, I am Roman

I am a full-stack Python developer. Currently buildingSmello, a local-first HTTP traffic inspector for Python.

More about me