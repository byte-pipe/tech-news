---
title: I got hacked, my server started mining Monero this morning. | Unfinished Side Projects
url: https://blog.jakesaunders.dev/my-server-started-mining-monero-this-morning/
site_name: hackernews_api
fetched_at: '2025-12-18T19:08:24.456441'
original_url: https://blog.jakesaunders.dev/my-server-started-mining-monero-this-morning/
author: Jake
date: '2025-12-17'
published_date: '2025-12-17T00:00:00+00:00'
description: I got hacked, my server started mining Monero this morning.
tags:
- hackernews
- trending
---

# I got hacked, my server started mining Monero this morning.

Edit: This got way more attention than I was ever expecting. I originally asked claude to draft it from a transcript
of my panicked messages and the feedback was clear, nobody likes AI slop. As a result I’ve redrafted it this morning
to fix some inaccuracies and make it sound human. - Jake

Or: How I learned that “I don’t use Next.js” doesn’t mean your dependencies don’t use Next.js

## 8:25 AM: The Email

I woke up to this beauty from Hetzner:

Dear Mr Jake Saunders,

We have indications that there was an attack from your server.
Please take all necessary measures to avoid this in the future and to solve the issue.

We also request that you send a short response to us. This response should contain information about how this could
have happened and what you intend to do about it.
In the event that the following steps are not completed successfully, your server can be blocked at any time after the
2025-12-17 12:46:15 +0100.

Attached was evidence of network scanning from my server to some IP range in Thailand. Great. Nothing says “good
morning” like an abuse report and the threat of getting your infrastructure shut down in 4 hours.

Background: I run a Hetzner server with Coolify. It runs all mystuff, like my little corner of the internet:

* My IoT Side Project
* This Blog
* Analytics
* My dads site (he’s an electrician)

## 8:30 AM: Oh Fuck

First thing I did was SSH in and check the load average:

1
2

$
w
 08:25:17 up 55 days, 17:23, 5
users
, load average: 15.35, 15.44, 15.60

I run a bunch of Go backend services and some SvelteKit frontend stuff on there. My grand total of daily users peaks at
20, so something was very wrong.

I ranps auxto see what was eating my CPU:

1
2
3
4
5
6

USER PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND
1001 714822 819 3.6 2464788 2423424 ? Sl Dec16 9385:36 /tmp/.XIN-unix/javae
1001 35035 760 0.0 0 0 ? Z Dec14 31638:25 [javae] <defunct>
1001 3687838 586 0.0 0 0 ? Z Dec07 82103:58 [runnv] <defunct>
1001 4011270 125 0.0 0 0 ? Z Dec11 10151:54 [xmrig] <defunct>
1001 35652 62.3 0.0 0 0 ? Z Dec12 4405:17 [xmrig] <defunct>

819% CPU usage.On a process calledjavaerunning from/tmp/.XIN-unix/. And multiplexmrigprocesses - that’s
literally cryptocurrency mining software (Monero, specifically).

Looks like I’d been mining cryptocurrency for someone since December 7th. Forten days. Brilliant.

## The Investigation

My first thought was “I’m completely fucked.” My host had been running a crypto miner for a week, the whole think was
borked. Time to just nuke it from orbit and rebuild.

Fortunately, I had the foresight to do a little detective work beforehand to at least learn how I’d been compromised so
I could learn for the future. I set out to do this with the help of Claude (this is not my speciality).

First, I noticed something interesting. All these processes were running as user1001. Not root. Not a system user.
UID 1001.

Let me check what’s actually running:

1

$
docker ps

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25

CONTAINER ID IMAGE CREATED STATUS PORTS NAMES
c604f579efd5 dsw80g4w8g0kgog8oskc0sks:63e3be6167b43de47663445dd72f92f97887b843 2 days ago Up 2 days
(
healthy
)

[
DELETED] dsw80g4w8g0kgog8oskc0sks-075301203997
00aec82c2650 o4wk8gsckwgkcgcgkcw8gcsc:40497e7208602d31d7b5e58af4f2e86611b9850c 2 days ago Up 2 days
[
DELETED] o4wk8gsckwgkcgcgkcw8gcsc-072326337252
a42f72cb1bc5 ghcr.io/umami-software/umami:postgresql-latest 9 days ago Up 9 days
(
healthy
)

[
DELETED] umami-bkc4kkss848cc4kw4gkw8s44
7c365a792902 postgres:16-alpine 9 days ago Up 9 days
(
healthy
)

[
DELETED] postgresql-bkc4kkss848cc4kw4gkw8s44
af077d142471 ghcr.io/coollabsio/coolify:4.0.0-beta.452 10 days ago Up 10 days
(
healthy
)

[
DELETED] coolify
fdc3cc9b926b ghcr.io/coollabsio/coolify-realtime:1.0.10 10 days ago Up 10 days
(
healthy
)

[
DELETED] coolify-realtime
d3dc2af3ff4d postgres:15-alpine 10 days ago Up 10 days
(
healthy
)

[
DELETED] coolify-db
dc77adba40bb redis:7-alpine 10 days ago Up 10 days
(
healthy
)

[
DELETED] coolify-redis
4962dd18bed7 ghcr.io/coollabsio/sentinel:0.0.18 3 weeks ago Up 7 hours
(
healthy
)

[
DELETED] coolify-sentinel
5ec997e35140 nginx:stable-alpine 6 weeks ago Up 6 weeks
(
healthy
)

[
DELETED] kcwsosksw084swoog04g0w0k-proxy
5da5e2f2052b prom/prometheus:latest 6 weeks ago Up 6 weeks
[
DELETED] yg400wo4wok8k0cgo8844gcg-155648790718
32815a5e2e52 twakedrive/tdrive-frontend 7 weeks ago Up 7 weeks
[
DELETED] frontend-ssowscwgccgk8k0k8oos8w40-120609116307
5d6bc828fe7f twakedrive/tdrive-node 7 weeks ago Up 7 weeks
[
DELETED] tdrive_node-ssowscwgccgk8k0k8oos8w40-120609108796
3e727b84415d mongo 7 weeks ago Up 7 weeks
[
DELETED] mongo-ssowscwgccgk8k0k8oos8w40-120609102533
3506728b808b a4c00g0ggkk4cww4scsw8scw:682dfd679845535f873d3c5b4599295f4d855ba5 7 weeks ago Up 7 weeks
[
DELETED] a4c00g0ggkk4cww4scsw8scw-113711308615
736d9f03d152 rccwscgosk48gs0844sogsgw:51d68c7e7665371569aacc5f044c82ec1f06fa4c 7 weeks ago Up 7 weeks
[
DELETED] rccwscgosk48gs0844sogsgw-111702410410
8f79e6f4c981 grafana/grafana-oss 7 weeks ago Up 7 weeks
(
healthy
)

[
DELETED] grafana-ik8wokwgowow8gksok8k40sc
09d013497f9f 24a90047f2d2 7 weeks ago Up 7 weeks
(
healthy
)

[
DELETED] postgresql-ik8wokwgowow8gksok8k40sc
bf8b6a969b19 gcr.io/cadvisor/cadvisor:latest 7 weeks ago Up 7 weeks
(
healthy
)

[
DELETED] k0gkw4koc8swo4wkg44w408g-211926055160
30e4d6edf675 prom/node-exporter:latest 7 weeks ago Up 7 weeks
[
DELETED] yc4c4ckg80ogggc4ck8gwgww-211604215046
b227504e8787 rabbitmq:3-management 7 weeks ago Up 7 weeks
(
healthy
)

[
DELETED] rabbitmq-xscowck8kgc0wssokoggcskc
b260ad24c434 d741b3768746 7 weeks ago Up 7 weeks
(
healthy
)

[
DELETED] kcwsosksw084swoog04g0w0k
6d038254e9ef grafana/loki:latest 7 weeks ago Up 7 weeks
[
DELETED] b88cwo8ckwo0gw840oo444kk-193205274080
fe2aad5d9704 traefik:v3.1 7 weeks ago Up 7 weeks
(
healthy
)

[
DELETED] coolify-proxy

Note: Deleted ports from this list as i feel like the might expose some inner workings.

Crucially, I was runningUmami- a privacy-focused analytics tool I’d re-deployed 9 days ago to track traffic on my
blog. I redeployed it because it had started acting up and I wasn’t sure why. The timing was suspicious to me.

Let me check which container has user 1001:

1
2
3
4

$
docker ps
-q
 |
while
read
container
;

do

echo

"===
$container
 ==="

 docker
exec

$container

ls

-la
 /app/node_modules/next/dist/server/lib/ 2>/dev/null |
grep
xmrig

done

Output:

1
2

=== a42f72cb1bc5 ===
drwxr-xr-x 2 nextjs nogroup 4096 Dec 17 05:11 xmrig-6.24.0

There it is.Containera42f72cb1bc5- that’s my Umami analytics container. And it’s got a wholexmrig-6.24.0directory sitting in what should be Next.js server internals.

The mining command in the process list confirmed it:

1
2
3
4
5

/app/node_modules/next/dist/server/lib/xmrig-6.24.0/xmrig
 --url auto.c3pool.org:443
 --user 8Bt9BEG98SbBPNTp1svQtDQs7PMztqzGoNQHo58eaUYdf8apDkbzp8HbLJH89fMzzciFQ7fb4ZiqUbymDZR6S9asKHZR6wn
 --pass WUZHRkYOHh1GW1RZWBxaWENRX0ZBWVtdSRxQWkBWHg==
 --donate-level 0

Someone had exploited my analytics container and was mining Monero using my CPU. Nice.

## Wait, I Don’t Use Next.js

I’d actually seen a post on HN referencing thisReddit postabout a
critical Next.js (CVE-2025-66478). My immediate reaction was “lol who cares, I don’t run Next.js.”

Oh my sweet summer child.

Except… Umamiis built with Next.js. I did not know this, nor did I bother looking. Oops.

The vulnerability (CVE-2025-66478) was in Next.js’s React Server Components deserialization. The “Flight” protocol that
RSC uses to serialize/deserialize data between client and server had an unsafe deserialization flaw. An attacker could
send a specially crafted HTTP request with a malicious payload to any App Router endpoint, and when deserialized, it
would execute arbitrary code on the server.

1. Attacker sends crafted HTTP request to Umami’s Next.js endpoint
2. RSC deserializes the malicious payload
3. RCE achieved via unsafe deserialization
4. Download and install cryptominers
5. Profit (for them)

So much for “I don’t use Next.js.”

## The Panic: Has It Escaped the Container?

This is where I started to properly panic. Looking at that process list:

1

1001 714822 819 3.6 2464788 2423424 ? Sl Dec16 9385:36 /tmp/.XIN-unix/javae

That path -/tmp/.XIN-unix/javae- looks like it’s on thehost filesystem, not inside a container. That means it
can get access to my database, all my environment variables, the works. Claude was telling me I’d need to:

1. Assume everything is compromised
2. Check for rootkits, backdoors, persistence mechanisms
3. Probably rebuild from scratch
4. Spend my entire day unfucking this

I checked for persistence mechanisms:

1
2
3
4
5

$
crontab
-l

no crontab
for
root

$
systemctl list-unit-files |
grep
enabled

# ... all legitimate system services, nothing suspicious

No malicious cron jobs. No fake systemd services pretending to benginxsorapaches. That’s… good?

But I still needed to know:Did the malware actually escape the container or not?

## The Moment of Truth

The test was, if/tmp/.XIN-unix/javaeexists on the host, I’m fucked. If it doesn’t exist, then apparently what I’m
seeing is
just Docker’s default behavior of showing container processes in the host’spsoutput, but they’re actually isolated.

1
2

$
ls

-la
 /tmp/.XIN-unix/javae

ls
: cannot access
'/tmp/.XIN-unix/javae'
: No such file or directory

IT NEVER ESCAPED.

Or at least it doesn’t look like it. We can downgrade this incident from DEFCON1 to ‘point a gun at it and do some more
checks, but no guillotine yet’.

The malware was entirely contained within the Umami container. Apparently, when you runps auxon a Docker host, you
see processes
from all containers because they share the same kernel. But those processes are in their own mount namespace - they
can’t see or touch the host filesystem.

I verified what user that container was actually running as:

1
2
3
4
5
6
7
8

$
docker inspect umami-bkc4kkss848cc4kw4gkw8s44 |
grep

'"User"'

"User"
:
"nextjs"
,

$
docker inspect umami-bkc4kkss848cc4kw4gkw8s44 |
grep

'"Privileged"'

"Privileged"
:
false
,

$
docker inspect umami-bkc4kkss848cc4kw4gkw8s44 |
grep

-A
 30
"Mounts"

"Mounts"
:
[]
,

So here’s what I now know, and why I’m not totally fucked:

* Container ran as usernextjs(UID 1001), not root.
* Container was not privileged.
* Container hadzero volume mounts.

Which means:

* Run processes inside the container
* Mine cryptocurrency
* Scan networks (hence the Hetzner abuse report)
* Consume 100% CPU

The malware could NOT:

* Access the host filesystem
* Install cron jobs
* Create systemd services
* Persist across container restarts
* Escape to other containers
* Install rootkits

Container isolation actually worked. Nice.

## Dockerfiles vs. Auto-Generated Images

There were a couple of things which saved me in this case IMO compared to the Reddit post I linked:

* I write all my own dockerfiles for my applications. This isn;t a silver bullet on it’s own but compared to
autogenerated ones you have a better idea of what’s in there.
* Coolify and Dockers approach to containerization in general. I’ve since learned that we can’t rely on container
separation for security but honestly it seems better than running everything on the host.

The Reddit post I’d seen earlier? That guy got completely screwed because his container was running as root. The malware
could:

* Install cron jobs for persistence
* Create systemd services
* Write anywhere on the filesystem
* Survive reboots

So in this case, container isolation had worked!

What I did not do, was keep track of the tolling I was using and what toolingthatwas using. In fact, I installed
Umami from Coolify’s services screen. I didn’t even configure it.

Obviously none of this is Umami’s fault by the way. They released a fix for their free software like a week ago. I
just
didn’t think to do anything about it.

## The Fix

1
2
3
4
5
6
7

# Stop and remove the compromised container

$
docker stop umami-bkc4kkss848cc4kw4gkw8s44

$
docker
rm
umami-bkc4kkss848cc4kw4gkw8s44

# Check CPU usage

$
uptime

08:45:17 up 55 days, 17:43, 1 user, load average: 0.52, 1.24, 4.83

CPU back to normal. It’s been two days since and my CPU is just chilling at like 5%.

I also enabled UFW (which I should have done ages ago):

1
2
3
4
5
6

$
sudo
ufw default deny incoming

$
sudo
ufw default allow outgoing

$
sudo
ufw allow ssh

$
sudo
ufw allow 80/tcp

$
sudo
ufw allow 443/tcp

$
sudo
ufw
enable

This blocks all inbound connections except SSH, HTTP, and HTTPS. No more exposed PostgreSQL ports, no more RabbitMQ
ports open to the internet. In my mind this shouldn’t be too big a deal because 5432 wasn’t open to he host from the
docker container. But worth doing.

I sent Hetzner a brief explanation:

Investigation complete. The scanning originated from a compromised Umami analytics container (CVE-2025-66478).

The container ran as non-root user with no privileged access or host mounts, so the compromise was fully contained.
Container has been removed and firewall hardened.

They closed the ticket within an hour.

## Lessons Learned

### 1. “I don’t use X” doesn’t mean your dependencies don’t use X

I don’t write Next.js applications. But I run third-party tools that are built with Next.js. When CVE-2025-66478 was
disclosed, I thought “not my problem.” Wrong.

Know what your dependencies are actually built with. That “simple analytics tool” is a full web application with a
complex stack.

### 2. Container isolation works (when configured properly)

This could have been so much worse. If that container had been running as root, or had volume mounts to sensitive
directories, or had access to the Docker socket, I’d be writing a very different blog post about rebuilding my entire
infrastructure.

Instead, I deleted one container and moved on with my day.

Write your own Dockerfiles.Understand what user your processes run as. AvoidUSER rootunless you have a very
good reason. Don’t mount volumes you don’t need. Don’t give containers--privilegedaccess.

### 3. The sophistication gap

This malware wasn’t like those people who auto-poll for/wpadmineverytime I make a DNS change. This was spicy.

* Disguised itself in legitimate-looking paths (/app/node_modules/next/dist/server/lib/)
* Used process names that blend in (javae,runnv)
* Attempted to establish persistence
* According to other reports, even had “killer scripts” to murder competing miners

But it was still limited by container isolation. Good security practices beat sophisticated malware.

### 4. Defense in depth matters

Even though the container isolation held, I still should have:

* Had a firewall enabled from day one (not “I’ll do it later”)
* Been running fail2ban to stop those SSH brute force attempts
* Had proper monitoring/alerting (I only noticed because of the Hetzner email)
* Updated Umami when the CVE was disclosed

I got lucky. Container isolation saved me from my own laziness.

## What I’m Doing Differently

1. No more Umami.- Meh, I’ve gone back on this. This wasn’t Umami’s fault, and their open source software is super
cool. I’ve rebooted a fresh version of Umami.
2. Audit all third-party containers.Going through everything I run and checking:* What user does it run as?
* What volumes does it have?
* When was it last updated?
* Do I actually need it?
3. SSH hardening.Moving to key-based authentication only, disabling password auth, and setting up fail2ban.
4. Proper monitoring.Setting up alerts for CPU usage, load average, and suspicious network activity. I shouldn’t
find out about compromises from my hosting provider. I actually have grafana and Node exporter set up, but it’s not
good unless I go look at it!
5. Regular security updates.No more “I’ll update it later.” If there’s a CVE, I patch or I remove the service.

## The Silver Lining

This was actually a pretty good learning experience. I got to:

* Practice incident response on a real compromise (never done this before!)
* Prove that container isolation actually works
* Learn about Docker namespaces, user mapping, and privilege boundaries
* Harden my infrastructure without the pressure of active data loss

And I only lost about 2 hours of my morning before work. Could’ve been way worse.

Though I do wonder how much Monero I mined for that dickhead. Based on the CPU usage and duration… probably enough for
them to have a nice lunch. You’re welcome, mysterious attacker. Hope you enjoyed it.

## TL;DR

* Umami analytics (built with Next.js) had an RCE vulnerability.
* Got exploited, installed cryptominers
* Mined Monero for 10 days at 1000%+ CPU
* Container isolation saved me because it ran as non-root with no mounts
* Fix:docker rm umamiand enable firewall
* Lesson: Know what your dependencies are built with, and configure containers properly

17 Dec 2025

* Self Hosting
* Work

* #Engineering
* #Hetzner
* #Self Hosting
* #Software Development

 « Fix for google search console 'sitemap could not be read'
