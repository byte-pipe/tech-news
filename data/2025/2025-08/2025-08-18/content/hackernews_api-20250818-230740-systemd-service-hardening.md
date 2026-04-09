---
title: SystemD Service Hardening
url: https://roguesecurity.dev/blog/systemd-hardening
site_name: hackernews_api
fetched_at: '2025-08-18T23:07:40.499977'
original_url: https://roguesecurity.dev/blog/systemd-hardening
author: StarkZarn
date: '2025-08-18'
description: Discover additional security options for systemd units, to include quadlets. These options are everything from system permissions, time manage, BPF, syscall & seccomp filters, etc., all to make your system more secure.
tags:
- hackernews
- trending
---

# SystemD Service Hardening

* Starkzarn
* Linux ,Homelab ,Security
* 11 Aug, 2025

Controversy aside, systemd provides us a very complete, robust method of controlling services (amongst a multitude of other Linux things). For a lot of things though, this is optimized for success out of the box and not necessarily security. Such is the way of many IT endeavors. This doc though is meant to provide a snapshot of a number of hardening options that you can apply to systemd service units and podman quadlets to increase the overall security posture and reduce both the likelihood of compromise, as well as the blast radius post-exploitation.

Warning

By no means is this a prescriptive guide for securing systemd services. All services will require different configurations based on their required capabilities. You will have to experiment and review logs when things inevitably break to make corrections. Securing your infrastructure is your responsibility and this is meant to be a tool in your belt, not a guaranteed solution.

## SystemD Security Analysis

Before we can decide how to increase our systemd unit’s security, we have to understand where we’re starting. There’s a tool for this. You can run it to analyze the entirety of the list of deployed units, or you can analyze one specific unit and all its details. The latter is the method that we’ll mostly focus on here, but for the sake of thoroughness I will show you both. The former is a good way of getting a high-level idea of your overall system’s security posture.

In a terminal, run the following…

sudo
 systemd-analyze
 security

You should see something like this…

BONUS: Trivia!

Bonus points for anyone who can tell me what distribution I’m running based solely on the above content…

So, that’s a lot of red… Is Linux inherently insecure…? Well, no, but also yes. Linux has lots of issues with it, just as any behemoth of an operating system, but we have a lot going for us too, and let’s talk about that.

And yes, for all the Stallman incarnates out there, I understand that Linux is a kernel and GNU corelibs and userspace all unite in some unholy ceremony to make a usable operating system. For the bulk of the userbase though, this ultimately doesn’t matter. Language also has the neat capability to evolve based on its accepted understanding. Everyone knows what is meant when an operating system is referred to as “Linux” and that’s what matters.

Systemd ships a lot of functionality, and a lot of services. Because having a usable operating system for most people means making a lot of these services work together, systemd has some loose security defaults. It also gives us a method to harden this up though, depending on our usecase! Let’s look at a specific example service.

Run the same command as before, but this time append a service name as the last argument. I’m choosingsshd.serviceas an example.

sudo
 systemd-analyze
 security
 sshd.service

…and that’s not even the end of the list. Yikes!

#### What it Means

So there are a few components in the table that we need to look at:

1. Checkmark / X: This is a boolean indicator to tell you if a positive security measure in place for the given control.
2. Name: The capability name. This is what you’ll reference when changing these security settings in the unit file (or override stub)
3. Description: A plain-language description of what the capability provides
4. Exposure: A quantitative metric that “scores” risk for the given control.

The last is the only quantitative value we have here, so use this to triage changes so you can get the most bang for your buck.

#### How to Change It

Okay, so we have an idea of where we’re starting as far as exposure, we have quantitative metrics for effect of certain keys, and we have a list of keys. What now?

All of these security key changes are placed into the[Service]section of a systemd unit file, or the[Container]section of a podman quadlet. These files will typically be found in/etc/systemd/system/and/etc/containers/systemd/for the system, and various other places if running as a user.

Tip

Systemd supports stub file configuration overrides. The daemon will handle creation of these automatically if you edit the file usingsudo systemctl edit ServiceName.service. Prefix the command with the environment variableEDITOR=nvimto edit with a superior editor.You can manually configure them too, by creating a new directory:/etc/systemd/system/ServiceName.service.d/override.confand only specifying the sections you want to change.Managing configurations this way is cleaner, and very much preferred.

Time to make an educated guess and start playing whack-a-mole… The golden rule here is: if a service fails to start after a change, it probably needs the permissions/capabilities you just took away from it.

Alright, so what moles do we try and whack?

## SystemD Service Security Options

Here’s a (likely incomplete) list of the various security options on a per-service level. The source of truth here are manpages. See:man Capabilities 7andsystemd-analyze capabilitiesas well asman systemd.exec 5for the current list and explanations.

* AmbientCapabilities
* AppArmorProfile
* CapabilityBoundingSet
* DeviceAllow
* DynamicUser
* Group
* InaccessiblePaths
* IPAddressAllow
* IPAddressDeny
* LockPersonality
* MemoryDenyWriteExecute
* NoExecPaths
* NoNewPrivileges
* PrivateDevices
* PrivateIPC
* PrivateNetwork
* PrivateTmp
* PrivateUsers
* ProcSubset
* ProtectClock
* ProtectControlGroups
* ProtectHome
* ProtectHostname
* ProtectKernelLogs
* ProtectKernelModules
* ProtectKernelTunables
* ProtectProc
* ProtectSystem
* ReadOnlyPaths
* ReadWritePaths
* RemoveIPC
* RestrictAddressFamilies
* RestrictFileSystems
* RestrictNamespaces
* RestrictNetworkInterfaces
* RestrictRealtime
* RestrictSUIDSGID
* AmbientCapabilities
* SocketBindAllow
* SupplementaryGroups
* SystemCallArchitectures
* SystemCallFilter
* TemporaryFileSystem
* UMask
* User

### Some Explanations

* ProtectSystem—“If set to “strict” the entire file system hierarchy is mounted read-only, except for the API file system subtrees/dev/,/proc/and/sys/(protect these directories usingPrivateDevices=,ProtectKernelTunables=,ProtectControlGroups=).”
* ReadWritePaths— makes particular paths writable again
* ProtectHome— makes/home/,/root, and/run/userinaccessible
* PrivateDevices— turns off access to physical devices, allows access only to pseudo devices like/dev/null,/dev/zero,/dev/random
* ProtectKernelTunables— makes/proc/and/sys/read-only
* ProtectControlGroups— makescgroupsaccessible read-only
* ProtectKernelModules— denies explicit module loading
* ProtectKernelLogs— restricts access to the kernel log buffer
* ProtectProc—“When set to “invisible” processes owned by other users are hidden from /proc/.”
* ProcSubset—“If “pid”, all files and directories not directly associated with process management and introspection are made invisible in the /proc/ file system configured for the unit’s processes.”
* NoNewPrivileges— ensures the process cannot gain new privileges throughsetuid,setgidbits and filesystem capabilities
* ProtectClock— denies writes to system and hardware clocks
* SystemCallArchitectures— if set tonative, processes can make only nativesyscalls(in most casesx86-64)
* RestrictNamespaces— namespaces are mostly relevant to containers, therefore can be restricted for this unit
* RestrictSUIDSGID— prevents the process from settingsetuidandsetgidbits on files
* LockPersonality— prevents the execution domain from being changed, which could be useful only for running legacy applications or software designed for other Unix-like systems
* RestrictRealtime— realtime scheduling is relevant only to applications that require strict timing guarantees, such as industrial control systems, audio/video processing, and scientific simulations
* RestrictAddressFamilies— restricts socket address families that are available; can be set toAF_(INET|INET6)to allow only IPv4 and IPv6 sockets; some services will needAF_UNIXfor internal communication and logging
* MemoryDenyWriteExecute— ensures that the process cannot allocate new memory regions that are both writable and executable, prevents some types of attacks where malicious code is injected into writable memory and then executed; may cause JIT compilers used by JavaScript, Java or .NET to fail
* ProtectHostname— prevents the process from usingsyscallssethostname(),setdomainname()
* SystemCallFilter: Limits syscall permitted by the service. This is a huge tunable, but can also break things very easily.Examples:Allow only syscalls in group@system-service: SystemCallFilter=@system-serviceAllow syscalls in group@system-serviceand syscallseccompexcept those in group@chown: SystemCallFilter=@system-service seccomp SystemCallFilter=~@chownDeny syscalls in group@chownwith errorEPERMrather than terminating the process: SystemCallFilter=~@chown:EPERMA list of all known syscalls and groups can be obtained via:systemd-analyze syscall-filterRather then killing the process, systemd can also be instructed to return an error code like EPERM for all violations. SystemCallErrorNumber=EPERMSeeman systemd.exec(5) → SystemCallFilter(includes a list ofimportant syscall groups)man systemd.exec(5) → SystemCallErrorNumberman errno(3)(available error codes)
* Examples:Allow only syscalls in group@system-service: SystemCallFilter=@system-serviceAllow syscalls in group@system-serviceand syscallseccompexcept those in group@chown: SystemCallFilter=@system-service seccomp SystemCallFilter=~@chownDeny syscalls in group@chownwith errorEPERMrather than terminating the process: SystemCallFilter=~@chown:EPERM
* Allow only syscalls in group@system-service: SystemCallFilter=@system-service
* Allow syscalls in group@system-serviceand syscallseccompexcept those in group@chown: SystemCallFilter=@system-service seccomp SystemCallFilter=~@chown
* Deny syscalls in group@chownwith errorEPERMrather than terminating the process: SystemCallFilter=~@chown:EPERM
* A list of all known syscalls and groups can be obtained via:systemd-analyze syscall-filter
* Rather then killing the process, systemd can also be instructed to return an error code like EPERM for all violations. SystemCallErrorNumber=EPERM
* Seeman systemd.exec(5) → SystemCallFilter(includes a list ofimportant syscall groups)man systemd.exec(5) → SystemCallErrorNumberman errno(3)(available error codes)
* man systemd.exec(5) → SystemCallFilter(includes a list ofimportant syscall groups)
* man systemd.exec(5) → SystemCallErrorNumber
* man errno(3)(available error codes)

Tip

Prefixing the first value in a list with~will make the entire line a negative. For exampleCapabilityBoundingSet=~CAP_SETUID CAP_SETPCAPREMOVESthesetuidandsetpcapcapabilities.

#### Troubleshooting syscall restrictions

Luckily, when tuning theSystemCallFilter, we can leverage some specific logs to help us determine what’s breaking. You will requireauditdinstalled and running on your system for this.

1. After experiencing a systemd service failure, run:
sudo
 ausearch
 -i
 -m
 SECCOMP
 -ts
 recent
1. Look for the line like:
type
=
SECCOMP
 msg
=
audit
(
08/09/2025
 14:22:10.314:08
)
:
 auid=user
 uid=user
 gid=user
 ses=
1
 subj==unconfined
 pid=
42348
 comm=ncat
 exe=/usr/bin/ncat
 sig=SIGSYS
 arch=x86_64
 syscall=socket
 compat=
0
 ip=
0x7b9e06e59477
 code=kill

and note the value of thesyscallkey.

1. Add either that specific syscall, or the group to which it belongs into yourSystemCallFilterand try again.

### What should you care about?

So this is definitely what some might call a futile process. I don’t entirely disagree. What matters is risk management and threat model.Whatare you trying to protect yourself against? I’d venture a guess that for most people, it’s not insiders who already have root access to the machine, it’s likely more focused on external threats. With that, I’d recommend starting withexternalfacing services, like apache/httpd, nginx, caddy, traefik, ssh,etc.

You don’t need to go through this process for every. single. service. I will say though, if you leverage systemd to run custom commands, like script bundles to leverage in a.timerunit instead of cron —definitelygo through this process for them. You know very intimately what they require, they’re far less massive than most OS utilities, and they’re easy to tweak.

#### The Cliffnotes

Okay, so here’s the list of tunables that I personally go for first:

1. ProtectSystem=strict
2. PrivateTmp=yes
3. ProtectHome=yesorProtectHome=tmpfsfor services that complain about R/W on an unnecessary home dir.
4. ProtectClock=yes
5. ProtectKernelLogs=yes
6. ProtectKernelModules=yes
7. RestrictSUIDGUID=yes
8. UMask=0077
9. LockPersonality=yes
10. RestrictRealtime=yes
11. MemoryDenyWriteExecute=yes
12. DynamicUser=yesorUser=SOMETHINGOTHERTHANROOT

After that it gets a little less certain on what might break things. Obviously the above won’t work for everything either, but those are the things I start with when tuning. Adding in syscall filtering takes a little longer.

#### An Example

Given that this blog runs behind Traefik, here’s an example for what I’ve configure my Traefik quadlet unit to look like. Some of these are specific because it is running in a container, which has its own benefits for security.

[Unit]

Description
=
Traefik Reverse Proxy with Socket Activation

Requires
=
http.socket https.socket

[Container]

ContainerName
=
traefik

HostName
=
traefik

Image
=
docker.io/traefik:v3

Network
=
traefik.network

Volume
=
traefik-config.volume:/etc/traefik/:Z

Volume
=
/var/log/traefik:/logs/:Z

AutoUpdate
=
registry

Notify
=
true

HealthCmd
=
CMD-SHELL traefik healthcheck --ping

HealthInterval
=
10s

HealthRetries
=
5

HealthStartPeriod
=
5s

HealthTimeout
=
3s

HealthOnFailure
=
kill

[Service]

Restart
=
always

MemoryMax
=
512M

Sockets
=
http.socket https.socket

## Security Tuning

ProtectHome
=
yes

ProtectClock
=
yes

ProtectKernelLogs
=
yes

ProtectKernelModules
=
yes

ProtectSystem
=
full

RestrictSUIDSGID
=
yes

UMask
=
0077

SystemCallArchitectures
=
native

SystemCallFilter
=
@system-service @mount @privileged

RestrictRealtime
=
yes

RestrictIPC
=
yes

LockPersonality
=
yes

RestrictAddressFamilies
=
AF_INET AF_INET6 AF_UNIX AF_NETLINK

#RestrictNamespaces=yes ### Doesn't work due to containerization

MemoryDenyWriteExecute
=
yes

#Needs CAPS: PTRACE

CapabilityBoundingSet
=
~
CAP_SETUID
 CAP_SETPCAP

#####

[Install]

WantedBy
=
default.target

## Conclusion

While you can go and tweak all your services, I am not saying it’s necessary. This is merely a tool in the belt of any linux admin worth their snuff, andI personally believeit to be underutilized. In the nature of public notes, as I have been cleaning up some servers and organizing my own messy documentation on them, I decided to put this little note sheet together for the community at large. In particular, I think this is something a lot of self-hosters can benefit from.

Don’t let perfect be the enemy of good, apply this where you can, and your lab (and the internet) will be a better place for it.

##### Tags:

* Quadlet
* Security
* SystemD
* Capabilities
* Syscall

##### Share :

## Comments

## Related Posts

#### How to install AREDN in a Virtual Machine on Proxmox

* Starkzarn
* Homelab ,Ham Radio ,Networking ,Linux
* 13 Apr, 2025

AREDN as a Proxmox Workload Proxmox Virtual Environment (PVE) is a fantastic open source resource for homelabbers and production hyperconverged infrastructure alike. It does come with ocassional ch

read more

#### Monitor your AREDN Node with Prometheus and Grafana

* Starkzarn
* Networking ,Linux ,Ham radio ,Homelab
* 08 Jun, 2025

As of the 3.24.4.0 release of the AREDN firmware, Prometheus metrics have been supported out of the box! This is great for data lover

read more

#### Leveraging Authelia for OIDC Single Sign-On (SSO) with Headscale

* Starkzarn
* Linux ,Networking ,Homelab
* 19 May, 2025

A bonus article in the self-hosted Headscale series! After implementing it myself with a few trials and tribulations, I decided to share how exactly to make Authelia work as an OIDC identity provider

read more

#### How to Host Headscale on a Linux Server with Podman Quadlets (Part 2)

* Starkzarn
* Linux ,Networking ,Homelab
* 20 Apr, 2025

Headscale This is part 2 of a two-part series. I'm assuming you already have traefik up and running on your cloud VM and are ready to get headscale setup for an awesome, access-anywhere homelab th

read more

#### How to Host Headscale on a Linux Server with Podman Quadlets (Part 1)

* Starkzarn
* Linux ,Networking ,Homelab
* 19 Apr, 2025

Headscale This will be a brief run-through of the best strategy I've found at selfhosting headscale in the cloud as a control-plane server for your Tailscale tailnet. I have come to enjoy podman qu

read more

#### "Meshtrics:" A Nosy Neighbor's Guide to Meshtastic Airtime Metrics in Grafana

* Starkzarn
* Networking ,Linux ,Ham radio ,Homelab
* 27 Jul, 2025

Meshtastic garners a lot of interest, a lot of criticism, and a lot of experimentation. I love things that provide people with an opportunity to experiment, and this tech is right up my alley. I am un

read more

#### Monitor Your Network the GPL Way with LibreNMS

* Starkzarn
* Homelab ,Networking ,Linux
* 13 May, 2025

LibreNMS provides a method of performing network inventory, monitoring, and aggregation in the open-source way. With a GPLv3 license, LibreNMS ensures that we can escape the possibility of closed-sour

read more

#### Intercept and Monitor TLS Traffic with mitmproxy Using Podman

* Starkzarn
* Networking ,Linux ,Pentest
* 26 May, 2025

In this article, we're going to peel back the covers of TLS encryption in transport and monitor encrypted application traffic in real time, in cleartext, with mitmproxy! We'll look at in-situ monitori

read more

#### Monitoring OPNSense Logs with Grafana Loki (Part 2)

* Starkzarn
* Homelab ,Networking ,Linux
* 04 May, 2025

This is part 2 in a blog series describing how I have chosen to setup firewall log parsing, normalization, enrichment, and display using Grafana! If you haven't seen part 1 yet, I'd recommend starting

read more

#### Monitoring OPNSense Logs with Grafana Loki

* Starkzarn
* Homelab ,Networking ,Linux
* 24 Apr, 2025

This is a high level walkthrough of one of the newer methods of ingesting syslog-based OPNSense "filterlogs," or firewall event logs, and enriching it with geoIP data. I tried this back in 2023 but wa

read more

#### Running Winlink on Linux with PAT

* Starkzarn
* Ham Radio ,Linux
* 14 Apr, 2025

Setting up pat to get on HF Winlink on Linux This is a quick run-through of how to put together a few simple software pieces to get your radio on the air with Winlink using only your Linux comput

read more
