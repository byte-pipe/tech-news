---
title: 'leah blogs: Comparing nitro to runit'
url: https://leahneukirchen.org/blog/archive/2025/08/comparing-nitro-to-runit.html
site_name: lobsters
fetched_at: '2025-08-25T23:07:39.965864'
original_url: https://leahneukirchen.org/blog/archive/2025/08/comparing-nitro-to-runit.html
date: '2025-08-25'
tags: unix
---

Yesterday Iannounceda first public release ofnitro, a tiny init system and process
supervisor. This got a fair bit
of attention, and to my delight was even boosted on the fediverse by
bothLaurent Bercot(of s6 fame) anddjbhimself.

One of the most requested things was a comparison to other init systems.
Since I’m most familiar withrunit, I shall compare nitro and runit here.

##### Comparison to runit

runit and nitro share the basic design of having a directory of
services and using small scripts to spawn the processes.

Comparing nitro to runit, there are a few new features and some
architectural differences.

From a design point of view, runit follows the daemontoools approach
of multiple small tools: Therunit-initprocess spawnsrunsvdir, which
spawns arunsvprocess for each service.

nitro favors a monolithic approach, and keeps everything in a single process.
This makes it also easier to install for containerization.

The new features are:

* nitro keeps all runtime state in RAM and provides an IPC interface
to query it, whereas runit emits state to disk. This enables nitro
to run on read-only file systems without special configuration.
(However, you need a tmpfs to store the socket file. In theory, on
Linux, you could even use/proc/1/fd/10or an abstract Unix domain
socket, but that requires adding permission checks.)
* support for one-shot “services”, i.e. running scripts on up/down
without a process to supervise (e.g. persist audio volume, keep RNG
state). For runit, you can fake this with apauseprocess, which has a little
more overhead.
* parametrized services. One service directory can be run multiple
times, e.g.agetty@can be spawned multiple times to provide
agetty processes for different terminals. This can be faked in
runit with symlinks, but nitro also allows fully dynamic creation of
service instances.
* log chains. runit supports only one logger per service, and log
services can’t have loggers on their own.

Currently, nitro also lacks some features:

* service checks are not implemented (see below), a service that
didn’t crash within 2 seconds is considered to be running currently.
* runsvchdiris not supported to change all services at once.
However, under certain conditions, you can change the contents of/etc/nitrocompletely andrescanto pick them up. nitro opens
the directory/etc/nitroonce and just re-reads the contents on
demand. (Proper reopening will be added at some point whenposix_getdentsis more widespread.opendir/readdir/closedirimplies
dynamic memory allocation.)
* You can’t overridenitroctloperations with scripts as forsv.

nitro tracks service identity by name, not inode number of the service
directory. This has benefits (parametrized services are possible) and
drawbacks (you may need to restart more things explicitly if you fiddle
with existing services, service lookup is a bit more work).

On the code side, nitro is written with modern(ish) POSIX.1-2008
systems in mind, whereas runit, being written in 2001 contains some
quirks for obsolete Unix systems. It also uses a less familiar
style of writing C code.

##### Do containers need a service supervisor?

It depends: if the container just hosts a simple server, probably not.
However, sometimes containers also need to run other processes to
provide scheduled commands, caches, etc. which benefit from
supervision.

Finally, PID 1 needs to reap zombies, and not all processes used as
PID 1 in containers do that. nitro is only half the size ofdumb-init,
and less than twice as big astini.

##### Declarative dependencies

Both runit and nitro don’t supportdeclaringdependencies between
services. However, services canwaitfor other
services to be up (and nitro has a special state for that, so only
successfully started services are consideredUP.)

Personally, I don’t believe service dependencies are of much use. My
experiences with sysvinit, OpenRC, and systemd show that they are hard
to get right and can have funny sideeffects such as unnecessary
restarts of other services when something crashed, or long delays
until the system can be brought down.

For system bringup, it can be useful to sequence operations
(e.g. startudevdvery early, then bring up the network, then mount
things, etc.). nitro supports this by allowing theSYS/setupscript
to start and wait for services. Likewise, services can be shutdown in
defined order.

##### Deferring to policies

nitro is a generic tool, but many features provided by other
supervisors can be implemented assite policiesusing separate
tools. For example, nothing stops you from writing a thing to infer
service dependencies and do a “better” bringup. However, this code
doesn’t need to be part of nitro itself, nor run inside PID 1.

Likewise, things like liveness checks can be implemented as separate
tools. External programs can quite easily keep track of too many
restarts and trigger alerts. An simple Prometheus exporter is
included incontrib.

##### Lack of readiness checks

At some point I want to add readiness checks, i.e. having an explicit
transition fromSTARTINGtoUP(as mentioned above, currently this
happens after 2 seconds).

Unfortunately, the existing mechanisms for service readiness
(e.g. systemd’ssd_notifyors6notification fd) are incompatible
to each other, and I don’t really like either. But I also don’t
really want to addyet another standard.

##### Historical background

[This is mostly written down for future reference.]

I think my first exposure to daemontools-style supervision was back in
2005 when I had shared hosting atAria’s old companytheinternetco.net.
There was a migration from Apache to Lighttpd, which meant.htaccessfiles weren’t supported anymore. So I got my own Lighttpd
instance that was supervised by, if I remember correctly, freedt.

Later, I started the first musl-based Linux distributionsabotageand builtbusybox
runit-based init scripts
from scratch.

When Arch (which I used mostly back then) moved towards systemd, I
wroteignite, a set of
runit scripts to boot Arch. (Fun fact: the last machine running
ignite was decommissioned earlier this year.)

Finally, xtraeme discovered the project and invited me to help
moveVoid to runit.
En passant I became a Void maintainer.

Work on nitro started around 2020 with some experiments how a
monolithic supervisor could look like. The current code base was
started in 2023.

NP: EA80—Die Goldene Stadt
