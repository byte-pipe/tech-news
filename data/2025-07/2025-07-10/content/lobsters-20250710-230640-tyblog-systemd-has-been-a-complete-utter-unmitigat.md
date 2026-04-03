---
title: Tyblog | systemd has been a complete, utter, unmitigated success
url: https://blog.tjll.net/the-systemd-revolution-has-been-a-success/
site_name: lobsters
fetched_at: '2025-07-10T23:06:40.864045'
original_url: https://blog.tjll.net/the-systemd-revolution-has-been-a-success/
author: Tyler Langlois
date: '2025-07-10'
description: Eleven init systems enter, one init system leaves.
tags: linux, systemd
---

### «systemd has been a complete, utter, unmitigated success

* 8 July, 2025
* 1,782 words
* 7 minute read time

Figure 1:The systemd wars of the tenties were harsh and casualties were many

The year is 2013 and I amhopping mad.

systemdis replacing my plaintext logs with a binary format and pumping steroids intoinitand it islaughingat me.
The unix philosophy cries out: is this the end of Linux (or, as many are calling it, GNU plus Linux)?

The year is 2025 and I’m here to repent.
Not only issystemda worthy successor to traditionalinit, but I think that it deserves a defense for what it’s done for the landscape – especially given the hostile reception it initially received (and somehow continues to receive? for some reason?).
No software is perfect – except forTempleOS– but I think that systemd has largely been a success story and proven many dire forecasts wrong (including my own).
I was wrong!

#### TheinitPaleolithic

I hope that I don't need to whine about why the old status quo wasn't great – init scripts of varying quality with janky dependencies and wildly varying semantics were frustrating.
It's sort of wild to me that I was working as a full-time software engineer during an era in which we were still writing bespokeshellscripts to orchestrate process management.
"Lost" or unmanaged processes, the weirdness ofS99-type directories for dependency ordering, and different interfaces into/etc/init.dscripts were all real problems.

Figure 2:/etc/init.d, uh, finds a way

During theLINUX INIT WARS, you could probably write an upstart, s6, or OpenRC init script that didn't havetoomany problems.
Buteven thenyou're supporting a variety of service management configuration formats with slightly differing behaviors.
I wrote services for all of these different init systems!
And the experience wasn't super!

Many of the deficiencies of traditional service management are more obvious in hindsight.
Whereas bare-bonesinitwas mostly about handling and/or reaping orphaned processes, entrusting a systemd-based PID 1 is also big for sandboxing and dependency management.
We haven't even talked about timers, sockets, or mounts, either.

#### I Deprecated Your Mom

We don't need to re-tread in great detail the history ofhowwe arrived here.
But thehowis part of the reason I think systemd worked out in the end.

Consider that the two primary ways that older init systems managed processes – either foregrounded or forked – were (and are!) fully supported modes.
Modern systemd provides for more nuanced "I'm ready" signaling apart from "is the process alive" (viaType=notify), but this kind of backward compatability really helped bridge the legacy gap.
The systemd authors even wrotegenerator code to help migrate old services.

I don't think the ini-style configuration format is a panacea (I likeDhall), but that's another olive branch from systemd authors to system administrators: it doesn't require a turing-complete configuration format or domain-specific language.
You can generally understand what this means when you read it and how to change it:

Systemd
* Font used to highlight builtins.
* Font used to highlight keywords.
* Font used to highlight type and class names.

[Service]

Type
=
forking

Defaults matterand configuration languages matter, too.
I appreciate that systemd chose one that is obvious.

I can cite other examples but the point I want to make is that systemd deliberately chose

* backward compatability,
* simple configuration paradigms,
* and to proactively support and help folks migrate.

Not every open source project chooses to take explicit steps to support old paths on the road to deprecation.
Lennart, you sweetheart.

#### Trust the Process

I don't just think that systemd is our newer, cooler Dad now that does previously-annoying things better, but that systemd also brought us good,brand newthings.

###### Won't Somebody Think of the Plaintext?

Figure 3:Logged logs logging loggily

journaldis here.
Past Me hated it, too.
The primary complaint with journald is that its journal files aren't in plaintext.
Do I miss that? A little, yeah. I'm sort of a Linux boomer at heart and like to useawkfor everything.

However, Ireallylike having one place to sendstdoutandstderr!
Have you ever leveraged custom fields when writing logs to the journal natively?
I attachNOTIFY_SLACK=1to some of my services and listen to my lab's log stream for these events and forward them along to a Slack channel to see logs I want more easily, it's great!

Moreover, delegating the responsibility to journald is also convenient from a rotation and disk space perspective.
With an awareness of filesystem space, I essentially never have to make rough guesses about rotation frequency any more, either1.
Are you aware that part of the reason your journal files are in a binary format rather than plaintext because journald is compressing them transparently?
That default choice is probably saving exabytes of space in aggregate across the entire computing space.

We can still live-tail logs, we can still forward log streams to different servers, and services can now reliably trust that their output will be captured during runtime.
These are all just net Good Things.

###### Time-r Out

I can still remember debuggingcronscripts at my university job: was$PATHwrong?
Should Iecho$USERsomewhere?
Why am I emitting output to themail spoolby default???

If there's a candidate for "most legible over its predecessor", it might be the systemd timer system.
Every Linux person feels some smug pride knowing what0 0 * * *means just by seeing a sequence of asterisks, but we all knowOnCalendar=dailyis easier to understand.
IsOnCalendar=minutelya word?
Not according to the grammar police, but you can probably infer whatminutelymeans!

I could fill a blog post with things I love about systemd timers, so here's a list instead:

* Persistent=trueis a great tool to ensure you don't miss timer executions.
* systemctl list-timersis an excellent way to see everything scheduled on a machine.
* The scheduling flexibility ofOnCalendar=andOnActiveSec=are both powerful and easy to understand.

###### Socket Activation

Thisaloneis a hugely different and powerful way to optimize a system.nix-daemonleverages this to great effect by "lazily" running only when you need it: the daemon will stop when you aren't building anything, but as soon as you ask for it,nix-daemon.socketwill startnix-daemon.service.
That's a great feature!

True to form, systemd even provides thesystemd-socket-proxydexecutable to bridge the gap for services that may not speak the native protocol yet.
I leverate this trick with heavy-handed daemons like Minecraft servers to great effect: I don't need to alter the original daemon at all, butsystemd-socket-proxydlets me leverage socket activation to run it on-demand anyway.

###### A Fistful of Units

When you glue together the various unit types -service,path,timer,mount,socket, and so on - you can almost create a state machine out of your system.
I've done this on NixOS and it's a powerful way to model interdependent service management.

Expressing system configuration like mounts asmountunits lets you correctly order a daemon that needs a network mount to function.
Triggering a service to restart when a file changes is easy with apathunit.
The variety of options available to aserviceunit are mind-boggling and address almost every need you can think of.
Seriously – did you know thatConditionVirtualization=can be used to run a unit depending on whether you're in AWS or Docker, for example?
That's crazy.

###### Security

If you've written a nontrivial number of.serviceunits, then you know the options available for hardening services are vast in number.
There are already many great blog posts about what they are; I won't go into that there.

Personally, my problem isremembering what those options are.
Did you know that systemd built tools to help with that, too?Each one of theseexplains some operational security benefit you can wrap a daemon with and in most cases they're each easy to add and don't break functionality.
These are a great way to take advantage of features like capabilities easily.

shell

systemd-analyze security polkit.service

 NAME DESCRIPTION EXPOSURE

✓ SystemCallFilter=~@swap System call allow list defined for service, and @swap is not included

✗ SystemCallFilter=~@resources System call allow list defined for service, and @resources is included (e.g. ioprio_set is allowed) 0.2

✓ SystemCallFilter=~@reboot System call allow list defined for service, and @reboot is not included

✓ SystemCallFilter=~@raw-io System call allow list defined for service, and @raw-io is not included

✗ SystemCallFilter=~@privileged System call allow list defined for service, and @privileged is included (e.g. chown is allowed) 0.2

✓ SystemCallFilter=~@obsolete System call allow list defined for service, and @obsolete is not included

✓ SystemCallFilter=~@mount System call allow list defined for service, and @mount is not included

✓ SystemCallFilter=~@module System call allow list defined for service, and @module is not included

✓ SystemCallFilter=~@debug System call allow list defined for service, and @debug is not included

✓ SystemCallFilter=~@cpu-emulation System call allow list defined for service, and @cpu-emulation is not included

✓ SystemCallFilter=~@clock System call allow list defined for service, and @clock is not included

✓ RemoveIPC= Service user cannot leave SysV IPC objects around

✗ RootDirectory=/RootImage= Service runs within the host's root directory 0.1

✓ User=/DynamicUser= Service runs under a static non-root user identity

✓ RestrictRealtime= Service realtime scheduling access is restricted

✓ CapabilityBoundingSet=~CAP_SYS_TIME Service processes cannot change the system clock

✓ NoNewPrivileges= Service processes cannot acquire new privileges

✓ AmbientCapabilities= Service process does not receive ambient capabilities

✓ CapabilityBoundingSet=~CAP_BPF Service may not load BPF programs

✓ SystemCallArchitectures= Service may execute system calls only with native ABI

✗ CapabilityBoundingSet=~CAP_SET(UID|GID|PCAP) Service may change UID/GID identities/capabilities 0.3

✗ RestrictAddressFamilies=~AF_UNIX Service may allocate local sockets 0.1

✓ ProtectSystem= Service has strict read-only access to the OS file hierarchy

✓ SupplementaryGroups= Service has no supplementary groups

✓ CapabilityBoundingSet=~CAP_SYS_RAWIO Service has no raw I/O access

✓ CapabilityBoundingSet=~CAP_SYS_PTRACE Service has no ptrace() debugging abilities

✓ CapabilityBoundingSet=~CAP_SYS_(NICE|RESOURCE) Service has no privileges to change resource use parameters

✓ CapabilityBoundingSet=~CAP_NET_ADMIN Service has no network configuration privileges

✓ CapabilityBoundingSet=~CAP_NET_(BIND_SERVICE|BROADCAST|RAW) Service has no elevated networking privileges

✓ CapabilityBoundingSet=~CAP_AUDIT_* Service has no audit subsystem access

✓ CapabilityBoundingSet=~CAP_SYS_ADMIN Service has no administrator privileges

✓ PrivateNetwork= Service has no access to the host's network

✓ PrivateTmp= Service has no access to other software's temporary files

✓ CapabilityBoundingSet=~CAP_SYSLOG Service has no access to kernel logging

✓ ProtectHome= Service has no access to home directories

✓ PrivateDevices= Service has no access to hardware devices

✗ ProtectProc= Service has full access to process tree (/proc hidepid=) 0.2

✗ ProcSubset= Service has full access to non-process /proc files (/proc subset=) 0.1

✗ PrivateUsers= Service has access to other users 0.2

✗ DeviceAllow= Service has a device ACL with some special devices: char-rtc:r /dev/null:rw 0.1

✓ KeyringMode= Service doesn't share key material with other services

✓ Delegate= Service does not maintain its own delegated control group subtree

✗ IPAddressDeny= Service does not define an IP address allow list 0.2

✓ NotifyAccess= Service child processes cannot alter service state

✓ ProtectClock= Service cannot write to the hardware clock or system clock

✓ CapabilityBoundingSet=~CAP_SYS_PACCT Service cannot use acct()

✓ CapabilityBoundingSet=~CAP_KILL Service cannot send UNIX signals to arbitrary processes

✓ ProtectKernelLogs= Service cannot read from or write to the kernel log ring buffer

✓ CapabilityBoundingSet=~CAP_WAKE_ALARM Service cannot program timers that wake up the system

✓ CapabilityBoundingSet=~CAP_(DAC_*|FOWNER|IPC_OWNER) Service cannot override UNIX file/IPC permission checks

✓ ProtectControlGroups= Service cannot modify the control group file system

✓ CapabilityBoundingSet=~CAP_LINUX_IMMUTABLE Service cannot mark files immutable

✓ CapabilityBoundingSet=~CAP_IPC_LOCK Service cannot lock memory into RAM

✓ ProtectKernelModules= Service cannot load or read kernel modules

✓ CapabilityBoundingSet=~CAP_SYS_MODULE Service cannot load kernel modules

✓ CapabilityBoundingSet=~CAP_SYS_TTY_CONFIG Service cannot issue vhangup()

✓ CapabilityBoundingSet=~CAP_SYS_BOOT Service cannot issue reboot()

✓ CapabilityBoundingSet=~CAP_SYS_CHROOT Service cannot issue chroot()

✓ PrivateMounts= Service cannot install system mounts

✓ CapabilityBoundingSet=~CAP_BLOCK_SUSPEND Service cannot establish wake locks

✓ MemoryDenyWriteExecute= Service cannot create writable executable memory mappings

✓ RestrictNamespaces=~user Service cannot create user namespaces

✓ RestrictNamespaces=~pid Service cannot create process namespaces

✓ RestrictNamespaces=~net Service cannot create network namespaces

✓ RestrictNamespaces=~uts Service cannot create hostname namespaces

✓ RestrictNamespaces=~mnt Service cannot create file system namespaces

✓ CapabilityBoundingSet=~CAP_LEASE Service cannot create file leases

✓ CapabilityBoundingSet=~CAP_MKNOD Service cannot create device nodes

✓ RestrictNamespaces=~cgroup Service cannot create cgroup namespaces

✓ RestrictNamespaces=~ipc Service cannot create IPC namespaces

✓ ProtectHostname= Service cannot change system host/domainname

✓ CapabilityBoundingSet=~CAP_(CHOWN|FSETID|SETFCAP) Service cannot change file ownership/access mode/capabilities

✓ LockPersonality= Service cannot change ABI personality

✓ ProtectKernelTunables= Service cannot alter kernel tunables (/proc/sys, …)

✓ RestrictAddressFamilies=~AF_PACKET Service cannot allocate packet sockets

✓ RestrictAddressFamilies=~AF_NETLINK Service cannot allocate netlink sockets

✓ RestrictAddressFamilies=~… Service cannot allocate exotic sockets

✓ RestrictAddressFamilies=~AF_(INET|INET6) Service cannot allocate Internet sockets

✓ CapabilityBoundingSet=~CAP_MAC_* Service cannot adjust SMACK MAC

✓ RestrictSUIDSGID= SUID/SGID file creation by service is restricted

✓ UMask= Files created by service are accessible only by service's own user by default

→ Overall exposure level for polkit.service: 1.2 OK :-)

#### Hater Sauce and The Terror From The Year 2000

Part of the reason I wrote this piece is that I keep stumbling ontothreads like this:

i used to think that systemd was made the default and adopted by most distros because of its ease of use and the fact it supplied a whole bunch of things in one suite and i see where the appeal is in that but after switching to artix openrc, im just lost on why they decided to use systemd when openrc is objectively better when it comes to being an init system and for managing services, and all the other components of systemd suite can just be replaced, like why would they do this?

Oh my god.
Look, I respect thatstvpidcvnt111111has a right to their opinion, but we can't let rhetoric with the intellectual weight of a mediocre fart waft into spaces as critical as computing infrastructure.
Get your stenchoutta here.

I'm not going to argue with straw men here, but wait, I am actually:

systemd does too much.

Have you considered that just "reaping old process IDs" wasn'tenoughresponsibility for an init daemon on a secure, robust system? That maybe it should be protecting other parts of the system and tracking the liveness of a desired service?

systemd does a bad job

If I see an argument like this then I can only assume the interlocutor doesn't do software engineering.
Any sort of consistent experience usingsystemctlorjournalctlwill tell you otherwise.
I've never evenheardof systemd failing at its core responsibilities (starting, stopping, and managing daemons).

systemd is too bloated and tries to do too much

For everything that modern systemd does, I'm shocked that there aren't more vulnerabilities (and yes, I'm aware of the CVEs that systemddoeshave).
I have no hard numbers supporting this claim, but I do wonder what the delta is between "exploits due to systemd itself" against "exploits blocked by the service sandboxing that systemd provides" is.
The ease of dropping an executable in an unprivileged environment is a great feature.
The industry as a whole is almost assuredly safer with the accessibility to process sandboxing that systemd brought down to an easier level.

Yeah,systemd-bootandsystemd-networkddo different things.
Frankly, my life as an operator has been significantlybetterthanks to the quality of software that comes out ofsystemd-*based projects and they're all configured in similar ways, too.
I've integrated at a low level with systemd APIs as well, so it's not as if this scary-sounding sprawl isclosed, either.
The APIs are there!
You can use them!

I've consistently found myselfpreferringto use the systemd based alternatives likesystemd-resolvedandsystemd-networkdwhen given the option because they end up being easier to configure and use.

red hat is trying to control the linux ecosystem with systemd

This is absolutely true.
I can't believe we, theSYSTEMD GLOBALIST ILLUMINATI, have been exposed.

## Footnotes:

1


I know logrotate can do very intelligent things. But the configuration steps for journald is "print to stdout, done".

« The Human Resources Alignment Problem
