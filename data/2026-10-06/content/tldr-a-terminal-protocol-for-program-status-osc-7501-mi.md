---
title: A Terminal Protocol for Program Status (OSC 7501) – Mitchell Hashimoto
url: https://mitchellh.com/writing/program-status-osc7501
site_name: tldr
content_file: tldr-a-terminal-protocol-for-program-status-osc-7501-mi
fetched_at: '2026-10-06T22:54:13.768615'
original_url: https://mitchellh.com/writing/program-status-osc7501
date: '2026-10-06'
published_date: '2026-10-06T00:00:00.000Z'
description: A Terminal Protocol for Program Status (OSC 7501)
tags:
- tldr
---

# Mitchell Hashimoto

# A Terminal Protocol for Program Status (OSC 7501)

October 6, 2026

I wrote a specification for a new terminal escape sequence:OSC 7501, the Program Status Protocol.
It lets any program tell the terminal what it's doing: idle, working,
waiting on the user, finished, or failed, and why.

For example, here is howTerraformcould indicate that it is blocked waiting for user input, with the
message "Apply 3 to add, 1 to change, 0 to destroy?" (base64-encoded). A terminal (or any
other tool running Terraform) could show this information however it feels
appropriate: a notification, an inbox, a status icon, etc.

ESC ] 7501 ; state=blocked:kind=permission:app=terraform:msg=QXBwbHkgMyB0byBhZGQsIDEgdG8gY2hhbmdlLCAwIHRvIGRlc3Ryb3k/ ESC \

This post covers why I think this protocol needs to exist, why the
existing approaches aren't good enough (especially for coding agents),
and how the protocol works.

This is a completely generic, terminal-native specification and protocol.It emerged from my work onSuperlogicalandGhosttybutthe specificationhas no product-specific
functionality or language. It is designed as an idiomatic, well-formed
specification that any terminal developer will find familiar.

## The Problem

Long-running work is common in terminals: builds, deployments, package
upgrades, data processing, and, more and more today, coding agents. These programs
alternate between working on their own, waiting on the user, and finishing.
Meanwhile, users usually go off and do something else and want to know
when the work finishes or needs them.

Aspects of this problem have been solved in various ways going back decades.
For example, some terminals monitor the active foreground process and have
features to notify when it changes. Or, they wait for some time period of
"quiet" (for various definitions) output. The specification
alsolists the reasons why existing sequences aren't enough.

Ultimately, I felt there wasn't a cohesive, interaction-agnostic, generic
solution to this problem that conveyed progress, blocking, completion,
and trees of tasks. And it wasn't possible to cobble together pre-existing
sequences to achieve it robustly, either.

## Singling Out "Agentic Inboxes"

Don't care about AI, LLMs, etc.? Skip this section.The problem
is generic and applies in a compelling way without bringing in
AI. It's particularly nasty with AI so I want to call it out, but if you
don't care about any of that, just skip this.

It's now increasingly common for people to run many long-running agents
for any number of reasons: background research, issue monitoring, bug fixing,
large features, etc. Each one works for a while and then stops to ask for
permission, ask a question, or report it's done.

From this, a new category of tool has emerged that I'll simply call
theagentic inbox: a single view across every running agent showing
which are working, which are done, and which are waiting on you.Herdr,cmux, andAgent Deckare a few examples
ofhundreds.

Without a dedicated protocol, they solve the agent status problem in
two ways: heuristics and non-terminal APIs.

### Heuristics

The first approach is to guess by reading the screen or the window title
and matching it against known patterns.

Herdr is a good example because it does this well and documents it
openly. Itsdetection manifestsare TOML rules that classify an agent as idle, working, or blocked. Here isthe first of 16 rulesfor Claude Code:

[[
rules
]]

id
 =
 "
osc_title_working
"

state
 =
 "
working
"

priority
 =
 1100

region
 =
 "
osc_title
"

visible_working
 =
 true

# Braille covers <= 2.1.227; half-circles are the 2.1.228 busy spinner.

regex
 =
 [
'
^[\x{2800}-\x{28FF}\x{25D0}-\x{25D3}] 
'
]

Claude Code is considered "working" if its window title starts with a
Braille spinner character or, as of version 2.1.228, a half-circle one.
Thehistory of that fileshows ten changes in three months for just Claude Code.

This isn't a criticism of Herdr.Its maintainers are doing the best
possible job with the tools available. But it demonstrates well the
benefita unified protocolwould have.

### Non-Terminal APIs

The second approach is to have the program report its own state through
an inbox-specific, out-of-band API such asHerdr's socket APIorcmux notify. This is better
than heuristics in some ways, because the program that actually knows its state is the
one reporting it. But every program has to integrate with every inbox
separately, and a local socket doesn't work over SSH or from within a
container without extra bridging. The pty already works across all of this.

## The Program Status Protocol

OSC 7501is a terminal native answer to this problem. The program
reports its own state directly via the pty that it always has, using a
format that is safe to send everywhere (well-behaved terminals ignore
unknown OSCs).

The body of the sequence is alist ofkey=valuepairsseparated by:.
The only required key isstate, which is one of:

state
Meaning
idle
At rest, waiting for the user's next instruction.
working
Running. May include a 
progress
 percentage.
done
Finished. The result is ready and the user hasn't seen it yet.
blocked
Can't continue until the user does something. 
kind
 says what (
permission
, 
question
, or 
auth
) and 
msg
 says why.
error
Failed and stopped.

Optional keysincludeapp, a stable
machine-readable program name likecargoorclaude-code, andmsg,
a single human-readable line encoded as base64.

Programs that run several things at once can report multiple records
usinghierarchical ids. Adeploy toolcan beworkingat the root whileus-eastpushes an image at 40% andeu-westisblockedwaiting for
approval to deploy to production. Both are true at the same time, and
the terminal decides what to show. Aclearstate removes records.

Here's acomplete integrationfor a shell script to wraprsyncto participate in this protocol:

status
()
 {

 printf
 '
\e]7501;state=%s:msg=%s\e\\
'
 "
$1
"
 "
$(
printf
 '
%s
'
 "
$2
"
 |
 base64
 |
 tr
 -d
 '
\n
'
)
"

}

status
 working
 "
Syncing photos
"

rsync
 -a
 ~/Photos
 backup:/photos
 &&
 status
 done
 "
Photos synced
"
 ||
 status
 error
 "
rsync failed
"

Trivial to script with plain old POSIXsh.
No SDK, no sockets, no environment variables, no JSON.
No bias towards specific GUI presentations. No bias to any specific
workload (like AI). A well-formed, generic foundation to build functionality
above that anyone and everyone can participate with.

Thefull speccovers the rest:record lifetime,feature detection,terminfo,size limits,
andsecurity. It's short. I wrote it all by hand. Please read it.

## Implement It

I wrotethis specificationbased on my experience maintaining a terminal
emulator for many years now. It is written in a way that is easy for
application developers to emit, and easy for terminal emulators to consume
and parse.

I've already implemented this protocol twice. We have one implementation
inlibghosttyand
I have a parallel implementation inRex.
I've also implemented it as a proof-of-concept in Terraform, Claude Code,
Codex, and Homebrew via either plugins or forks. In each case, the
implementation was no more than a dozen lines.

I've been in contact with the maintainers of many popular terminal programs
and emulators and they've helped review and shape the specification.
But if you have any more feedback, I'm happy to hear it.

If you've implemented the specificationplease let me know via
email (mail icon in the footer) and I'll add you to the list of tools
that implement this. Thank you.

I'd like us all to stop guessing what programs are doing by reading
their screens or process trees. The program already knows. Let's give it
a way to tell us!

October 6, 2026