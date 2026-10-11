---
title: Nix wrote half of my debugger | Farid Zakaria’s Blog
url: https://fzakaria.com/2026/10/07/nix-wrote-half-of-my-debugger
site_name: hnrss
content_file: hnrss-nix-wrote-half-of-my-debugger-farid-zakarias-blog
fetched_at: '2026-10-11T16:33:04.484635'
original_url: https://fzakaria.com/2026/10/07/nix-wrote-half-of-my-debugger
date: '2026-10-09'
published_date: '2026-10-07T12:00:00-07:00'
description: A few days ago I wrote about Rewind VM, a deterministic VM where every run of a Nix build is a pure function of its inputs, thread schedule included! I have been using it to find, reproduce and solve numerous race conditions in Nix builds, but it’s been making me feel a little crazy. What is this superpower, and why is nobody else using it? The tool has quickly grown a source panel, stack frames, bookmarks, a “Compare” tab, a lot more gdb support, thread lanes, which show who held the CPU at every step, and “Check from here”, which…
tags:
- hackernews
- hnrss
---

A few days ago I wrote aboutRewind VM,
adeterministic VMwhere every run of a Nix build is a pure function of its inputs,
thread schedule included!

I have been using it to find, reproduce and solve numerous race conditions in Nix builds, but it’s been making me feela little crazy. What is this superpower, and why is nobody else using it?

The tool has quickly grown a source panel, stack frames,
bookmarks, a “Compare” tab, a lot more gdb support, thread lanes, which show who held
the CPU at every step, and “Check from here”, which helps find the exact step where a race
condition happens.

I went into each new feature thinking it would be a big code-lift but I kept running into the same thing:the hard part of each feature was already done, and Nix had done it.

A debugger for instance, needs the exact inputs of the program, its debug symbols, its sources, the sources of every library under it, and a way for someone else to get all of that on their
machine. That’s exactly what a derivation is, and Nix makes that easy.

## §Two tellers, one account

A classic simple example of a race condition is two threads depositing into one bank account. Each deposit reads the balance, writes a line to the ledger, then stores the balance plus the deposit. If one teller runs between the other’s read and store, it writes a stale balance over the other’s deposits. 💥

static
 
void
 
deposit
(
int
 
teller
,
 
long
 
amount
)

{

 
long
 
seen
 
=
 
balance
;

 
char
 
line
[
64
];

 
int
 
n
 
=
 
snprintf
(
line
,
 
sizeof
 
line
,
 
 
"teller %d: %ld + %ld
\n
"
,

 
teller
,
 
seen
,
 
amount
);

 
if
 
(
write
(
1
,
 
line
,
 
n
)
 
!=
 
n
)

 
return
;

 
balance
 
=
 
seen
 
+
 
amount
;

}

A teller that runs between the other’s read and store writes a stale balance
over the other’s deposits.11On my 16-core laptop,banklost money in 396 of 1,000 runs. Pinned to a single core withtaskset, it lost money in none of 1,000: one core alone rarely switches threads in the middle of a deposit, which is why Rewind perturbs the schedule.

teller 1

balance

teller 2

read 150

read 150

store 200

store 150 + 10

160

teller 1's last deposit is gone

Rewind’s VM has one CPU, so its first run passes too.rewind checkruns the
build again under perturbed schedules, each asking the guest kernel to
reschedule at different steps, and narrows the first failure down to one step:

$
 
rewind check 
--where
 github:fzakaria/rewindvm#bank

...

step 3237 decides it: a reschedule there makes the run fail

passing: run 12feb5f832205a72, schedule 0
failing: run c2f1cfac0c288f3e, schedule 1 over steps 3237..3238
the two are the same run until step 3237

where the threads were:
 3237 139/140 deposit (bank.c:24), on the CPU at the deciding step
 3250 139/141 deposit (bank.c:24), at the first event that differs

Running this check on my laptop took 11 seconds. The two runs are the same machine, exit for exit, until step 3237, where only the failing one gets a reschedule.

## §Free thing one: the inputs

The argument tocheckis a derivation and can be a flake reference. The beauty of Nix is that it knows the inputs of a derivation, so that’s all we need to make sure the run is reproducible. The derivation’s inputs are the source, the compiler, the libraries, the kernel, and the VM’s configuration

rewind nixrealises the derivation’s inputs, packs the closure into a read-only erofs image, and boots the VM on it.

The run’s id is a hash of its inputs, the way a store path is, andrewind showprints the command that makes it again:

$
 
rewind show 12feb5f8

rewind nix /nix/store/cr8rl40rjb9cmmcd9sxn9mpdrhvp53jj-bank-0.1.0.drv --epoch 1791331200 --clock branches --name bank-0.1.0 #
 
12feb5f832205a72

When the build succeeds, the guest reports each output’s NAR hash, andrewind nixchecks it against the host’s copy and against every binary cache
Nix substitutes from, by fetching only the.narinfo:

$
 
rewind nix github:fzakaria/rewindvm#bank

...

/nix/store/27a4q7w90jzp4wg5kaaajvb64zll6yqg-bank-0.1.0 dbf0df3de84b7a84 matches your store

This helps us validate that the build within the VM is the same as the build on my laptop, and that the VM’s run is reproducible by Nix.

## §Free thing two: every symbol and every source

Debugging code is much simpler when you are looking at the source. A new panel in the Rewind app orrewind wherein the terminal shows the source of the program at the playhead, and the stack frames that called it.

The debugger needs to know where the sources are, and Nix gives us that for free too.

nixpkgsbuilds the packages withseparateDebugInfo, and the debug info is cached oncache.nixos.orgas adebugoutput. We can leveragedebuginfodto fetch the debug info and the sources by build ID, so we can see the source of any binary in the VM, including the Linux kernel! 😲

$
 
rewind where c2f1cfac 3250

process 139 (bank), thread 141, at step 3250

#
4 deposit 
(
bank.c:24
)

 22 	int n = snprintf(line, sizeof line, "teller %d: %ld + %ld\n", teller, seen, amount);

 23

>
 
24 	
if
 
(
write
(
1, line, n
)
 
!=
 n
)

 25 		return;

 26 	balance = seen + amount;

called from #
5 teller 
(
bank.c:34
)

called from #
6 start_thread 
(
pthread_create.c:454
)

## §gdb, on a fork of any step

Sometimes though, the source is not enough, and we need to see the state of the program.rewind gdbopens gdb on a fork of the run at the playhead, with every thread of the process. The debugger can set breakpoints, watchpoints, and inspect memory, registers and variables.

At step 3249, just before teller 2 gets the CPU back, we can watch thebalancevariable and continue until it changes. Nothing gdb does changes the recording, and we can rewind to the same step and fork again, or fork at any other step, and gdb will see the same state.

If gdb is not enough,rewind shell --with nixpkgs#straceopens a shell in the
VM at a step with any package from nixpkgs on itsPATH. It is one more closure packed into one more image.

## §Compare two runs

Rewind makes it very easy to compare two runs. The Compare tab in the app, orrewind comparein the terminal, shows the last shared events of both runs, and the first event that differs.

The Compare tab puts both runs’ events side by side from just before they part,
with what differs marked. Teller 2 starts from 150 in the failing run and from
200 in the passing one:

## §Who had the CPU

Rewind’s VM has one CPU, so at any step exactly one thread is running. A race
is a question of order: which thread ran when.

The trace does not answer that directly. It records what threads did, a write, an open, a fork, an exit, a signal, but not who was running in the gaps between those events.

Rewind can fill in the gaps without recording anything new. Every run replays
exactly, so it can walk any stretch of a run one step at a time and, at each
step, ask the guest kernel which thread is on the CPU.

In the failing run, teller 1 (Thread 140) is interrupted at step 3238, halfway through a
deposit: it has read the balance but not stored it. Teller 2 (Thread 141) gets the CPU for
a single step, 3239, long enough to read the balance, and then teller 1 gets
it back and finishes.22It is a little hard to see since the event from Teller 2 is tucked underneath the Orange bar.

## §Check from here

Finding one bad interleaving raises the next question: how likely is it? Is the
passing run the normal case, or did it get lucky?

rewind checknormally answers that by building the whole derivation again
under many schedules. With--run, it starts from a run you already have
instead, atanystep you pick_. It forks the run there once per schedule, each
fork taking a different order of threads from that step on, and counts how
many end differently. Everything before the step stays exactly as it was.

We can apply this technique to the bank example, starting from the step where the two runs diverged, 3,221. When we run 16 schedules from there, all 16 lose money33Schedule 0 is the run itself, which passed. Every other line is a fork, andexited:2ismake checkfailing because the balance came up short.:

$
 
rewind check 
--run
 12feb5f8 
--schedule-from
 3221 
--schedules
 16 
--all
 
--no-narrow

schedule 0: exited:0 4528 steps dbf0df3de84b run 12feb5f832205a72
schedule 1: exited:2 3313 steps run f6eb462913dce489
schedule 2: exited:2 3328 steps run 388cef73a9c545fa
schedule 3: exited:2 3312 steps run 4d42012072d11537

...

schedule 16: exited:2 3314 steps run 63f7817972a90273
16 of 16 perturbed schedules ended differently

We can do the same thing from the Rewind App with “Check from here” in the context menu of the playhead. It forks the run at the playhead and runs each fork under a different schedule, counting how many end differently.

## §Bookmarks

bbookmarks the playhead’s step with a note. Bookmarks are kept with the run,
and they travel in its.rwdexport, so the person I hand the run to opens it
with my notes on the timeline:

## §Other examples to try

Each one is a derivation in the flake, with one bug and one fix:

* philosophers: the deadlock from the last post.
* bank: the lost update above.
* waiter: a SIGCHLD that arrives between a flag check andpause, so the
parent sleeps untilmake check’s ten second timeout kills it.
* config-reload: one process rewrites a config file in place while another
rereads it. On many cores it fails nearly every time; on one CPU only some
schedules land the reader between the truncate and the last write.

$
 
rewind check github:fzakaria/rewindvm#waiter

## §Nix is a superpower

Most of the hard work of a debugger is already done by Nix. Rewind adds a little more, but the rest is already there: the inputs, the sources, the debug symbols, and a way for someone else to get all of that on their machine.

When you start with something hermetic like a Nix derivation, you can get a debugger for free.

$
 
nix run github:fzakaria/rewindvm 
--
 check github:fzakaria/rewindvm#bank