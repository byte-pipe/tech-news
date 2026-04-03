---
title: 'They Used to Be Good, But Now They''ve Turned to Evil: The Synology End Game - LowEndBox'
url: https://lowendbox.com/blog/they-used-to-be-good-but-now-theyve-turned-to-evil-the-synology-end-game/
site_name: hackernews_api
fetched_at: '2025-08-29T23:06:14.988145'
original_url: https://lowendbox.com/blog/they-used-to-be-good-but-now-theyve-turned-to-evil-the-synology-end-game/
author: raindog308
date: '2025-08-29'
published_date: '2025-08-24T11:00:19+00:00'
description: Find the best cheap server hosting and the best cheap vps hosting, where you only pay a few dollars a month, exclusively on LowEndBox
tags:
- hackernews
- trending
---

## They Used to Be Good, But Now They've Turned to Evil: The Synology End Game

raindog308

/
Aug 24, 2025 @ 7:00 am
 
/

/
synology
,
ugreen

Share


Post










Share






reddit

I’ve been a Synology fan for many years.  I used to roll my own NAS servers for home, but eventually decided that quieter, more energy-friendly dedicated NAS solutions were a better path forward.  I don’t use a lot of their on-board apps, just basic file storage.

Right now I’ve got a DS920, a DS418, and a DS1522…but I probably won’t be buying another Synology again.

Why?

Their abusive, customer-hostile policies.

## Samba Limits

I started getting queasy when I read earlier this year that on some models, they limit how many concurrent connections you can make.  I though this was just something setup by default in smb.conf, but in fact Synology has a proprietary wrapper around the daemon that artificially limits it.

Whiskey.  Tango.  Foxtrot.

## You Must Buy Your Hard Drives From Us

For a long time, Synology has only officially supported certain hard drives.  I don’t have a problem with this, for three reasons.  First, it was a pretty extensive list and included all the major players (WD, Seagate, etc.).  Second, it’s unreasonable to expect Synology to certify every single hard drive from every maker on the planet.  And finally, it was just a support limit.  In other words, you could use whatever hard drives you wanted, but if there was a problem, they wouldn’t be able to support you if the drive wasn’t on their list.

I could live with that.  What I can’t live with is the new policy, implemented this year, where youmust buy your drives from Synology.  This only affects new models from this year forward.  Details still seem sketchy, but rumor is that it’s going to be along the lines of “we don’t recognize your WD Black hard drive, therefore we won’t use it.”

And by the way, Synology’s hard drives aren’t all that great.  My WD Blacks come with a 5 year warranty.  Synology’sonly come with 3 years.

Golf.  Foxtrot.  Yankee.

## Where to Now?

I could go back to building my own, with TrueNAS.  In the past, my home-build NAS boxes were hand-me-down gaming PCs (because they were big enough towers) but I have to imagine one can find a case that allows tons of drives and is still powered by something modest.

Or I may look at UGREEN.  Or Buffalo.  Or someone else.

 
 
 
 

### Related Posts:

## YOUR DATA IS GONE: How to Protect Your Synology From Being Ransomware'd

## B2 or C2? That is the Question. That is the Quest.

## Are You Recyling Old Hardware for Your DIY? The Environment Isn't Thanking You

## iKoula Offers Hosted Synology NAS Servers

raindog308

Raindog308 is a longtime LowEndTalk community administrator, technical writer, and self-described techno polymath. With deep roots in the *nix world, he has a passion for systems both modern and vintage, ranging from Unix, Perl, Python, and Golang to shell scripting and mainframe-era operating systems like MVS. He’s equally comfortable with relational database systems, having spent years working with Oracle, PostgreSQL, and MySQL.

As an avid user of LowEndBox providers, Raindog runs an empire of LEBs, from tiny boxes for VPNs, to mid-sized instances for application hosting, and heavyweight servers for data storage and complex databases. He brings both technical rigor and real-world experience to every piece he writes.

Beyond the command line, Raindog is a lover of German Shepherds, high-quality knives, target shooting, theology, tabletop RPGs, and hiking in deep, quiet forests.

His goal with every article is to help users, from beginners to seasoned sysadmins, get more value, performance, and enjoyment out of their infrastructure.

You can find him daily in the forums atLowEndTalkunder the handle@raindog308.

### 5 Comments

1. 1314 520:fnos！August 24, 2025 @12:20 pm|Reply
2. Edwin:Don’t forget QNAP. I have one that’s ten years old, it still works fine and I still get security updates.August 29, 2025 @4:57 am|Reply
3. wulfshade:Unraid has been my faithful NAS OS for the last 12 years, and will continue to be. There’s nothing else like it out there. Not only do I store all my files on it, I also host my VMs and containers on it, on hardware I choose with graphics card for transcoding and local, private LLM for my workflows. Just brilliant.August 29, 2025 @5:23 am|Reply
4. Dave:Raspberry Pi 4 and a 2TB USB HDD set to spin down work great for me, use very little power. Run samba, MythTV, music server, DLNA server. And sip very little power. Running Debian here (not RaspiOS).August 29, 2025 @5:55 am|Reply
5. Sard:When it comes to bang for the bucks i guess ugreen is probably the way to go. For example Ugreen 6 bay DXP 6800 Pro ( i5-1235U 10 Core 12 Threads, 15-55w, 96 GB DDR5 possible) for about 980€. Preferably with Unraid or Truenas/Proxmox . Qnap is ok and stable but way more expensive. All depends on your needs and if you are willing to invest time into installing your own NAS OS or not.August 29, 2025 @6:58 am|Reply


### Leave a ReplyCancel reply

Some notes on commenting on LowEndBox:

* Do not use LowEndBox for support issues. Go to your hosting provider and issue a ticket there. Coming here saying"my VPS is down, what do I do?!"will only have your comments removed.
* Akismet is used for spam detection. Some comments may be held temporarily for manual approval.
* Use<pre>...</pre>to quote the output from your terminal/console, or consider using a pastebin service.

Your email address will not be published.Required fields are marked*

Comment*

Email*

Name*

Website

Notify me of followup comments via e-mail. You can alsosubscribewithout commenting.



Δ
