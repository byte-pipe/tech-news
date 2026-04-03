---
title: 15 years, one server, 8GB RAM and 500k users - how Webminal refuses to die - Webminal
url: https://community.webminal.org/t/15-years-one-server-8gb-ram-and-500k-users-how-webminal-refuses-to-die/8803
site_name: hackernews_api
content_file: hackernews_api-15-years-one-server-8gb-ram-and-500k-users-how-web
fetched_at: '2026-03-30T19:26:27.692949'
original_url: https://community.webminal.org/t/15-years-one-server-8gb-ram-and-500k-users-how-webminal-refuses-to-die/8803
author: giis
date: '2026-03-30'
published_date: '2026-03-30T06:06:33+00:00'
description: 'The server webminal.org runs on a single CentOS Linux box with 8GB RAM. That’s it. No Kubernetes, no microservices, no auto-scaling. One server since 2011. It has survived: A datacenter fire in 2021 (we lost 150k user &hellip;'
tags:
- hackernews
- trending
---

# 15 years, one server, 8GB RAM and 500k users - how Webminal refuses to die

laks

 March 30, 2026, 6:06am
 

1

## The server

webminal.orgruns on a single CentOS Linux box with 8GB RAM. That’s it. No Kubernetes, no microservices, no auto-scaling. One server since 2011. It has survived:

* A datacenter fire in 2021 (we lost 150k user accounts)
* Multiple power outages in the Netherlands
* That one time in 2017 when a Spanish tech blog sent 10,000 users in one day
* My friend Freston’s insistence that Slackware is the only real distro

## The idea

The idea was simple. I was sitting at my Windows machine at work, wanting to learn Linux. What if I could open a browser, practice on a real Linux terminal - no “Run” button, no “Execute” button, just a real server- gain the confidence, and then spin my chair to a real Linux machine and actually use it? No fear, no hesitation, because I already know what I’m doing.

## What’s new

We just gave the entire site a redesign. Every page, from scratch. Here’s what changed:

* New modern UI- clean, fast, no Bootstrap or jQuery CDN dependencies. Self-hosted fonts, mobile responsive.
* Root Lab- practice real sysadmin skills with full root access. We use User Mode Linux to give you a complete kernel with real block devices. Practice fdisk, LVM, RAID, mkfs, systemctl,crontab, firewalld, SSH keys, awk & sed - things you can’t do on a shared terminal.
* Live command ticker- that scrolling bar on the homepage? It’s real. Powered by eBPF (execsnoop) tracing commands in real-time. 28 million and counting.

## The journey

Linode → DigitalOcean → AWS → GCP → OVH → IBM Cloud → Linode

Full circle. Along the way we built: a browser IDE with VS Code/Theia, Docker-over-LXC root environments, Asciinema screencasting, a shared file pool, ttyrec-to-GIF publishing, a customuseraddbinary (the default was too slow with 300k+ users), and anOpenVZ-based VM provisioning system. Some still running, some killed by time or money.

## The co-founder I never saw

I’m from India. Freston is from the Netherlands. We met onLinuxForums.orgin 2010. Until 2015, we had never seen each other’s face — not even on Skype. All communication happened over SSH into our server in ascreensession.

$ screen -x chat
$ cat > /dev/null
hey, should we add MySQL support?

That’s how an entire platform was built. No Slack, no Zoom, no Jira tickets. Just two guys writing messages in a terminal.

## The tech stack nobody recommends

Python: 2.7 (yes, really)
Framework: Flask 0.12.5
Terminal: Shellinabox (abandoned in 2017, still works perfectly)
Root labs: User Mode Linux (a technology from 2001)
Monitoring: eBPF/execsnoop (the only modern thing)
Database: MySQL on a server that survived a fire
Frontend: No React, no Vue, no npm. Just HTML and inline CSS.

Every tech conference talk would tell you this stack is wrong. But it serves 500k users and has been up for 15 years.

## Shellinabox vs the world

We tried replacing Shellinabox with the modern WebSocket-based terminal. It lasted a few hours in production before users reported blank screens and Firefox incompatibility.

Shellinabox is from 2005. It’s ugly, it’s slow, and it works through every firewall, proxy, and corporate network on earth. We switched back. Sometimes the old thing is the right thing.

## User Mode Linux — the technology nobody uses

Everyone uses Docker. We use User Mode Linux — a full Linux kernel running in userspace, created by Jeff Dike in 2001.

Why? Because when a student typesfdisk /dev/sdb, they need a real block device. Docker can’t give you that. UML can.

Each user gets:

* A full Linux kernel (not a container, an actual kernel)
* 4 virtual block devices (64MB each) for practicing LVM, RAID, fdisk
* 256MB RAM
* Copy-on-write overlay - one golden image shared by everyone

When the student typespoweroff, the UML exits, and they’re back in their normal shell. Total isolation. Zero risk to the host.

The COW overlay means 100 concurrent users add only ~2GB of disk. The golden image is shared.

## eBPF - the one modern thing

That28,469,041 commands executedcounter on the homepage? It’s real. We useexecsnoop2from bcc-tools.

The live ticker you see scrolling on the homepage — those are real commands being typed by real users right now. Anonymized, safe commands only. No arguments, no paths, no passwords. Just$ ls,$ gcc,$ vimflowing by like a heartbeat.

The Linux kernel itself tells us when someone runs their firstls.

## What users say

“I am a Windows system admin without a lot of free time and this site has really helped me get familiar with Linux. I even use the site on my tablet. The tutorials you offer are really great too. Thanks for all you do.”

“I am a student studying Electronic Engineering in Korea. I am studying Linux by your site and it really helped me a lot!”

“The tutorial is great! I also laughed at some points. Your site is absolutely amazing. Please make more! Keep the great work up!”

## Cost

Webminal has zero revenue. No ads, no tracking, no VC funding. I pay for the server from my savings. I’ve spent more money on this project than on personal or family stuff.

More than once, I thought about killing it. 15 years is a long time. There were months when I was between jobs, watching my savings shrink, and the server bill kept coming. Every month I’d think - maybe this is the month I pull the plug. Then I’d get a job, the thought would go away, and Webminal would live another year. I applied to YC. Rejected. Tried to monetize - PayPal, Stripe, paid plans. Never worked. The users who need Webminal most are students who can’t afford $4/month. So it stays free.

500,000 people have typed their firstlson Webminal. Some of them are sysadmins now. Some run their own servers. One of them probably manages more infrastructure than I ever will.

As long as it helps a single student, Webminal will run.

If you want to help to upgrade from 8GB to 128GB so more students can run root labs at the same time. Every bit counts:Sponsor @Lakshmipathi on GitHub Sponsors · GitHub

.