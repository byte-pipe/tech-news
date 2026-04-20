---
title: 'BrewOps: I built a production-grade HTCPCP server because nobody else would - DEV Community'
url: https://dev.to/axrisi/brewops-i-built-a-production-grade-htcpcp-server-because-nobody-else-would-3clh
site_name: devto
content_file: devto-brewops-i-built-a-production-grade-htcpcp-server-b
fetched_at: '2026-04-02T11:20:47.371241'
original_url: https://dev.to/axrisi/brewops-i-built-a-production-grade-htcpcp-server-because-nobody-else-would-3clh
author: Nikoloz Turazashvili (@axrisi)
date: '2026-04-01'
description: This is a submission for the DEV April Fools Challenge What I built We identified a... Tagged with devchallenge, 418challenge, showdev, jokes.
tags: '#showdev, #devchallenge, #418challenge, #jokes'
---

April Fools Challenge Submission ☕️🤡

This is a submission for theDEV April Fools Challenge

## What I built

We identified a critical gap in modern cloud infrastructure.

RFC 2324, the Hyper Text Coffee Pot Control Protocol, has been a ratified internet standard since April 1, 1998. Twenty-eight years ago. It definesBREWandWHENas HTTP methods. It specifies418 I'm a Teapotas a status code. It mandates theAccept-Additionsheader for cream and whisky. It requires servers to returnSafe: if-user-awakeon every response.

And in 28 years, nobody built a production-ready implementation with SLA monitoring. Nobody added an incident timeline. Nobody tracked Caffeine Dispensed as a metric. Nobody implemented the Security Considerations section, which literally warns about "denial of coffee service attacks."

Until now.

BrewOpsis a fully RFC 2324-compliant HTCPCP/1.0 server. Written in Go. Zero external dependencies. It includes RFC 7168 TEA extension support, a live web dashboard, a CLI calledbrew-ctl(becausekubectlwas taken), and actual Denial of Coffee Service detection. The Dockerfile is calledBrewfile. The Docker Compose service is namedbarista. The build stage works in/coffeeshop. I regret nothing.

Here's what happens when you try to brew coffee in a teapot:

$
curl
-X
 BREW https://brewops.10mins.email/pot-2
-d

'start'

 418 I
'm a Teapot
 ════════════════

 ╭───╮
 │ │
 │ │
 ╭───╯ ╰─╮
 │ TEAPOT │
 ╰──────╯───╯

 "I'
m short and stout.
 Here is my handle, here is my spout.
 Tip me over, pour me out.
"

 The requested pot (pot-2) is a teapot and CANNOT brew coffee.

 RFC 2324 §2.3.2:
 "
Any attempt to brew coffee with a teapot should result
in

the error code
'418 I'
m a teapot
'. The resulting entity
 body MAY be short and stout."

Enter fullscreen mode

Exit fullscreen mode

That's a real response from a real server. Right now. Running in production. With a 99.97% brew uptime SLA. Go ahead, try it. I'll wait. I have coffee.

## Demo

Live server:https://brewops.10mins.email

Dashboard:https://brewops.10mins.email/dashboard-- open this first, then run curl commands. Watch your requests appear in the incident timeline alongside everyone else's. It's multiplayer. Yes, for a coffee pot.

### Try these from your terminal

I know you want to. Nobody can resist poking the teapot.

# Brew coffee (auto-creates a new pot for you, no reservation needed)

curl
-X
 BREW https://brewops.10mins.email/pot
-d

'start'

# Poke the teapot (you will get 418'd and you will deserve it)

curl
-X
 BREW https://brewops.10mins.email/pot-2
-d

'start'

# Brew with Whisky at 2pm on a Tuesday (the server will judge you)

curl
-X
 BREW https://brewops.10mins.email/pot
\


-H

'Accept-Additions: Cream, Whisky'

-d

'start'

# Brew tea, because the teapot has feelings and wants to be useful

curl
-X
 BREW https://brewops.10mins.email/tea/earl-grey
\


-H

'Content-Type: message/teapot'

-d

'start'

# Say "when" for milk (the RFC has a whole section on this, I'm not kidding)

curl
-X
 WHEN https://brewops.10mins.email/pot-0

# Check how many pots you people have created

curl https://brewops.10mins.email/status

# Launch a Denial of Coffee Service attack against my server

# (the server will call you out but still serve your coffee)

for
i
in

$(
seq
1 15
)
;

do

curl
-s

-X
 BREW https://brewops.10mins.email/pot
-d

'start'

>
 /dev/null

done

Enter fullscreen mode

Exit fullscreen mode

EveryBREW /potcreates a new pot in the fleet. Every 5th pot is secretly a teapot. You won't know until you try to brew coffee in it and get 418'd. The teapot lottery has a 20% hit rate and a 100% disappointment rate.

### What the dashboard tracks

The dashboard is styled like a 90s web forum that got promoted to an SRE tool. Teal background. Black borders. Orange uppercase headings. It tracks, in real time:

* Total brews worldwide (this number will haunt me)
* 418s served (always embarrassingly high because everyone tries the teapot first)
* Caffeine dispensed in milligrams (we meter it like cloud compute)
* DoCS attacks detected (you WILL trigger this reading the article, I guarantee it)
* Brew uptime: 99.97% (hardcoded, because we're that confident)
* Spills this quarter: 3 (always 3, it's load-bearing)
* Data retention policy: until next deploy

## Code

## turazashvili/brewops

### The world's first production-grade HTCPCP/1.0 server. RFC 2324 compliant. 418 I'm a Teapot. DoCS attack detection. SLA: 99.97%. Zero dependencies. Zero real-world value.

# BrewOps

### Enterprise-Grade Beverage Infrastructure Observability

"There is coffee all over the world. Increasingly, in a world in which computing is ubiquitous, the computists want to make coffee."— RFC 2324, Section 1

BrewOpsis the world's first production-grade implementation of theHyper Text Coffee Pot Control Protocol (HTCPCP/1.0)with fullRFC 7168 TEA extensionsupport, real-time observability, and Denial of Coffee Service (DoCS) attack detection.

We identified a critical gap in modern cloud infrastructure: despite HTCPCP being standardized since 1998, there arezero production-ready implementationswith SLA monitoring, incident timelines, and real-time telemetry. BrewOps closes this gap.

## What Is This

A fully functional HTCPCP server that:

* Responds toBREW,GET,WHEN, andPROPFINDHTTP methods per the RFC
* Returns proper418 I'm a Teapotwhen you try to brew coffee in a teapot
* Auto-creates new pots on each request (every 5th pot is a surprise teapot)
* Streams…

View on GitHub

16 files. 4,500 lines of Go. Zero external dependencies. The whole thing compiles into a single binary. The LICENSE includes a standard MIT clause plus:"COFFEE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF TEMPERATURE, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTY THAT THE BEVERAGE WILL NOT BE A TEAPOT."

## How I built it

Go, pure standard library.No frameworks, no routers, no npm install, no node_modules, no existential crisis. Go'snet/httpaccepts any HTTP method, which is what makesBREWandWHENwork. Most languages would fight you on this. Go just shrugs and passes it through.

### The server

One binary,brewopsd(thedis for daemon, likehttpd, except this one makes coffee). It handles:

* BREWandPOSTmethods -- RFC 2324 says servers MUST accept both, butPOSTis deprecated. UsingPOSTfor coffee is like usingvarin 2026. Technically works. Spiritually wrong.
* GET-- returns pot status. The response includes temperature labels that rotate between "Tepid (Why Bother)", "Scalding (Lawsuit Pending)", "Beyond Hot (Insurance Voided)", and "Thermonuclear (Handle At Own Risk)".
* WHEN-- stops milk. "When coffee is poured, and milk is offered, it is necessary for the holder of the recipient of milk to say 'when'." I didn't write that. Larry Masinter did. In a real RFC. In 1998.
* PROPFIND-- returns brew metadata. Lists Larry Masinter as the protocol author. Returns all 16 supported additions including Aquavit, because the RFC lists it and I don't argue with internet standards.

### The pot state machine

Every pot goes through:idle -> grinding -> brewing -> pouring -> ready -> cooling -> idle. The whole lifecycle takes about 60 seconds. Dynamic pots get cleaned up by a janitor goroutine that runs every 15 seconds, because even coffee infrastructure needs someone mopping the floor.

### The teapot lottery

BREW /potdynamically creates a new pot. Every 5th one is a teapot. The teapots get names like "Surprise Teapot", "The 418 Generator", "Definitely Not A Coffee Pot", and "Agent Teapot". When you BREW coffee in one, you get 418'd, and the dashboard logs a CRITICAL incident. The incident messages rotate between 25 options including:

* "Postmortem scheduled. Root cause: it's a teapot."
* "Filing JIRA ticket TEA-47: 'Pot refuses to brew coffee.' Status: Won't Fix."
* "The teapot doesn't dream of being a coffee pot. It's at peace."
* "Stack trace: main() -> brew() -> validatePot() -> TEAPOT. That's it."
* "Error budget: infinite. You can 418 this teapot all day. It doesn't care."

There are 100+ rotating messages across all response types. You get different snarky commentary every time.

### DoCS detection

Section 7 of RFC 2324 says:"Unmoderated access to unprotected coffee pots from Internet users might lead to several kinds of denial of coffee service attacks."

So I implemented it. If you send more than 10 BREW requests in 30 seconds, the server classifies it as a DoCS attack. Your response gets a big warning banner. The dashboard CRITICAL counter goes up. The incident log says things like "Hostile brewing activity detected. The coffee must flow." or "DoCS incident #5. The On-Brew Engineer has left the building. And the country."

The brew still succeeds, though. This is a coffee pot, not a firewall. As the RFC itself notes:"Modern coffee pots do not use fire. Thus, no firewalls are necessary."

### The dashboard

Vanilla HTML, CSS, and JavaScript. Three files. No React. No build step. The backend has a state machine, a janitor goroutine, SSE streaming, and rate-limited DoCS detection. The frontend isindex.html,style.css, anddashboard.js. The engineering effort distribution between backend and frontend is roughly 95/5, which I think says something about my priorities.

Responses are dual-mode: curl gets pretty plain text with ASCII art. The dashboard JS sendsAccept: application/jsonand gets structured data. So the same endpoint serves a nursery rhyme to your terminal and JSON to the browser. RFC-compliant content negotiation, technically.

### Deployment

Docker container built from theBrewfile, behind nginx. Nginx passes any HTTP method through to the backend, soBREWandWHENwork. I originally deployed to a PaaS that uses Cloudflare, and Cloudflare silently drops non-standard HTTP methods. Which means Cloudflare is not HTCPCP-compliant. I have filed zero bug reports about this but considered filing several.

I actually read both RFCs cover to cover. I spent longer on protocol compliance than I'd like to admit for something that makes coffee. TheAccept-Additionsheader parses quality parameters. The300 Multiple Optionsresponse for tea includes a properAlternatesheader. TheSafe: if-user-awakeheader is on every single response. Someone will probably never check any of this. But it's there. Because if you're going to implement a joke protocol, you might as well do it right.

## Prize category

Best Ode to Larry MasinterandCommunity Favorite.I'm also competing for the overall prompt, in case that wasn't obvious from the 4,500 lines of Go I(A) wrote for a coffee pot.

Larry Masinter wrote RFC 2324 on April 1, 1998. It was supposed to be a joke. It defined a coffee pot protocol with custom HTTP methods, a nursery rhyme in the spec, and a security section that warns about "trojan grounds." Twenty-eight years later, I built a fully compliant server with SLA monitoring, DoCS attack detection, and a live dashboard that tracks caffeine dispensed in milligrams.

The server is live. The dashboard is live. Every curl command you run from reading this post will show up in the same incident timeline as everyone else's. The 418 counter is going to climb. The DoCS attacks are going to pile up. Someone is going to BREW 200 pots and the fleet is going to look ridiculous and the dashboard is going to struggle to render them all and that's fine. That's the point. That's the joke. We built enterprise infrastructure for a coffee pot and then let the internet loose on it.

Larry, if you're reading this: the protocol works. Sorry it took 28 years.

## About me

I'm Niko. My title on this project is "Chief Brewing Officer & RFC Compliance Lead," which is the best title I've ever had and the least useful.

My day job involves building actual software that solves actual problems. This is not that. This is what happens when you read an RFC from 1998 and think "but what if someone actually built this" and then can't stop thinking about it until you do.

If you want to see what I do when I'm not implementing 28-year-old joke protocols, or if you want to file a JIRA ticket about the teapot (Status: Won't Fix):

* GitHub:@turazashvili-- where the coffee is brewed
* DEV:@axrisi-- where the coffee is documented

If you enjoyed this, leave a reaction. If you triggered a 418, leave a reaction. If you launched a DoCS attack against my server while reading this, you owe me at least two reactions and a mass brew has been logged and the On-Brew Engineer has been paged and they're not happy about it.

Coffee budget for this project generously provided byVexrail. I did not approve this expense. I am also the one who spent it. The coffee was good though.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
