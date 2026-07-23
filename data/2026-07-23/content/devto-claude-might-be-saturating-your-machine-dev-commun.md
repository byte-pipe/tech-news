---
title: Claude might be saturating your machine - DEV Community
url: https://dev.to/sidhantpanda/claude-might-be-saturating-your-machine-3h07
site_name: devto
content_file: devto-claude-might-be-saturating-your-machine-dev-commun
fetched_at: '2026-07-23T18:58:13.772348'
original_url: https://dev.to/sidhantpanda/claude-might-be-saturating-your-machine-3h07
author: Sidhant Panda
date: '2026-07-16'
description: My laptop was sitting idle with the fan at full tilt. Nothing was running that I knew of. The culprit... Tagged with ai, programming, claude, agents.
tags: '#ai, #programming, #claude, #agents'
---

Identifying orphaned AI tasks via PID 1 checks

My laptop was sitting idle with the fan at full tilt. Nothing was running that I knew of. The culprit turned out to be ten orphaned busy-loops left behind by a Claude Code session two days earlier.

## Just fix it for me

If your fan is roaring right now and you would rather not read the rest, paste this into a Claude Code session:

My machine seems idle but the fan is at full speed. Check the load average against my core count, then list the top CPU consumers with their PPID, elapsed time, and full argument list. I am looking for orphaned processes: anything reparented to PID 1 that has been burning CPU for hours or days, especially shells and interpreters where the process name alone tells you nothing. Show me what you find and what each one actually is before killing anything, and let me confirm the list first.

The "show me before killing" part is the important bit, and it is why the prompt is written that way rather than as "find and kill whatever is using CPU." A long-running process pinned to PID 1 is a strong hint that something was abandoned, but it is not proof. Daemons legitimately live there, and your ownnohup'd job or a detached build will look identical from a distance. Read the argument list before you agree to anything. In my case the arguments made it obvious in about two seconds.

## Finding it

Start with the load average. This is a 10-core machine:

$
 
uptime

19:39 up 6 days, 6:14, 10 users, load averages: 122.91 167.84 162.08

Enter fullscreen mode

Exit fullscreen mode

Load 122 on 10 cores is not idle. Next, the top CPU consumers:

$
 
ps 
-Ao
 pcpu,pid,ppid,user,comm 
-r
 | 
head
 
-12

 %CPU PID PPID USER COMM
139.8 8320 1 user /Applications/Google Chrome.app/Contents/MacOS/Google Chrome
 60.9 94281 1 user /bin/zsh
 59.4 94279 1 user /bin/zsh
 59.4 94288 1 user /bin/zsh
 59.1 94287 1 user /bin/zsh
 57.9 94285 1 user /bin/zsh
 57.6 94284 1 user /bin/zsh
 57.6 94286 1 user /bin/zsh
 57.3 94283 1 user /bin/zsh
 55.9 94282 1 user /bin/zsh
 51.1 94280 1 user /bin/zsh

Enter fullscreen mode

Exit fullscreen mode

Tenzshprocesses at roughly 60% each, and every one hasPPID 1. That is the tell: their parent died andlaunchdadopted them.commonly gives you the binary name, so pull the full argument list to see what they actually are:

$
 
ps 
-o
 pid,lstart,etime,pcpu,args 
-p
 94279,94280,94281

Enter fullscreen mode

Exit fullscreen mode

Note the comma-separated list. Passing-palongside-Asilently gets you every process on the box instead.

The arguments explained everything:

/bin/zsh 
-c
 
source
 ~/.claude/shell-snapshots/snapshot-zsh-XXXX.sh 2>/dev/null 
||
 
true
 
&&
 
eval
 
'
SP=/private/tmp/claude-501/<project>/<session-id>/scratchpad
# saturate all cores, then run the suite under contention
NCPU=$(sysctl -n hw.ncpu)
for i in $(seq 1 $NCPU); do (while :; do :; done) & done
LOADPIDS=$(jobs -p)
pnpm test:integration > "$SP/load.log" 2>&1
kill $LOADPIDS 2>/dev/null
...'

Enter fullscreen mode

Exit fullscreen mode

Elapsed time was01-22:41:17. Just under two days ofwhile :; do :; doneon every core.

A previous session had deliberately pegged all ten cores to run an integration suite under CPU contention, then meant to clean up after itself. The test run itself was long gone, confirmed by the absence of anyvitestorpnpmprocess:

$
 
ps 
-Ao
 pid,ppid,pcpu,etime,comm | 
grep
 
-Ei
 
"[n]ode|[v]itest|[p]npm"

58938 58933 0.0 00:59 .../bin/node
88656 88648 0.0 02-00:57:58 .../bin/node

Enter fullscreen mode

Exit fullscreen mode

Only the spinners were left. They accounted for about 700% of the 850% total CPU in use:

$
 
ps 
-Ao
 pid,ppid,pcpu,comm | 
awk
 
'NR>1 && $3>20 {sum+=$3; n++} END {print "procs >20% CPU:", n, " total %CPU:", sum}'

procs >
20% CPU: 12 total %CPU: 850.3

Enter fullscreen mode

Exit fullscreen mode

## Why the cleanup failed

Two things went wrong, and either alone would have been enough.

LOADPIDS=$(jobs -p)was the first. Job control is off in a non-interactive shell, sojobs -preturned nothing and the cleanupkillhad no arguments to act on. Collect$!after each background spawn instead:

LOADPIDS
=
""

for 
i 
in
 
$(
seq 
1 
$NCPU
)
;
 
do

 
(
while
 :
;
 
do
 :
;
 
done
)
 &
 
LOADPIDS
=
"
$LOADPIDS
 
$!
"

done

Enter fullscreen mode

Exit fullscreen mode

The second is that the parent shell died before reaching thekillline at all. A cleanup step on the happy path is not cleanup. Use a trap so it fires even on interrupt:

trap
 
'kill $LOADPIDS 2>/dev/null'
 EXIT INT TERM

Enter fullscreen mode

Exit fullscreen mode

## Fixing it

Plainkillwas enough. No-9needed:

$
 
kill 
94279 94280 94281 94282 94283 94284 94285 94286 94287 94288

$
 
ps 
-o
 
pid
=
 
-p
 94279,94280,94281,94282,94283,94284,94285,94286,94287,94288 | 
wc
 
-l

0

Enter fullscreen mode

Exit fullscreen mode

Afterwards, Chrome was back on top where it belongs and nothing else broke 30%:

$
 
ps 
-Ao
 pcpu,pid,comm 
-r
 | 
head
 
-4

 %CPU PID COMM
129.6 8320 /Applications/Google Chrome.app/Contents/MacOS/Google Chrome
 43.2 58249 .../Google Chrome Helper (Renderer)
 27.5 69725 .../UsageTrackingAgent

Enter fullscreen mode

Exit fullscreen mode

The load average still read 74 at that point, which is expected. It is a decaying rolling average and lags reality by design. The 1-minute figure had already dropped from 122 to 74 and kept falling; the 15-minute figure was still carrying the previous quarter-hour of saturation. Judge the fix by the process list, not the load average. The fan takes another minute or two beyond the CPU drop while the heat already in the chassis dissipates.

## Checking your own machine

uptime
 
# load average well above your core count?

sysctl 
-n
 hw.ncpu 
# what your core count actually is

ps 
-Ao
 pcpu,pid,ppid,user,comm 
-r
 | 
head
 
-15

Enter fullscreen mode

Exit fullscreen mode

Look for processes eating CPU withPPID 1and a longetime. Reparenting tolaunchdplus an elapsed time measured in days means nobody is supervising it and nobody is going to clean it up. Shells and interpreters are worth a closer look, sincecommshows you/bin/zshornodeand tells you nothing about what is inside. Get the arguments:

ps 
-o
 pid,ppid,lstart,etime,pcpu,args 
-p
 <pid>

Enter fullscreen mode

Exit fullscreen mode

On macOS, Activity Monitor sorted by CPU shows the same thing, but the process name column has the same problem: ten identicalzshrows and no hint of what they are running.

## Takeaway

Agents run real commands, including ones that deliberately consume resources, and a crashed or cancelled session does not necessarily take its children with it. If you let an agent spawn background work, it is worth knowing how to spot the leftovers.ps -Ao pcpu,pid,ppid,user,comm -r | headcosts nothing and would have caught this two days earlier.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse