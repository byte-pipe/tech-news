---
title: MuMu Player Pro (NetEase) silently runs 17 system reconnaissance commands every 30 minutes on macOS · GitHub
url: https://gist.github.com/interpiduser5/547d8a7baec436f24b7cce89dd4ae1ea
site_name: hackernews_api
content_file: hackernews_api-mumu-player-pro-netease-silently-runs-17-system-re
fetched_at: '2026-02-20T11:15:09.680963'
original_url: https://gist.github.com/interpiduser5/547d8a7baec436f24b7cce89dd4ae1ea
author: interpidused
date: '2026-02-20'
description: MuMu Player Pro (NetEase) silently runs 17 system reconnaissance commands every 30 minutes on macOS - news.md
tags:
- hackernews
- trending
---

Instantly share code, notes, and snippets.

# interpiduser5/news.md

 Created

February 20, 2026 01:28



Show Gist options



* Download ZIP





* Star9(9)You must be signed in to star a gist
* Fork0(0)You must be signed in to fork a gist

* Embed# Select an optionEmbedEmbed this gist in your website.ShareCopy sharable link for this gist.Clone via HTTPSClone using the web URL.## No results foundLearn more about clone URLsClone this repository at &lt;script src=&quot;https://gist.github.com/interpiduser5/547d8a7baec436f24b7cce89dd4ae1ea.js&quot;&gt;&lt;/script&gt;
* EmbedEmbed this gist in your website.
* ShareCopy sharable link for this gist.
* Clone via HTTPSClone using the web URL.
* Save interpiduser5/547d8a7baec436f24b7cce89dd4ae1ea to your computer and use it in GitHub Desktop.



Embed

# Select an option



* EmbedEmbed this gist in your website.
* ShareCopy sharable link for this gist.
* Clone via HTTPSClone using the web URL.

## No results found





Learn more about clone URLs





 Clone this repository at &lt;script src=&quot;https://gist.github.com/interpiduser5/547d8a7baec436f24b7cce89dd4ae1ea.js&quot;&gt;&lt;/script&gt;





Save interpiduser5/547d8a7baec436f24b7cce89dd4ae1ea to your computer and use it in GitHub Desktop.

Download ZIP

 MuMu Player Pro (NetEase) silently runs 17 system reconnaissance commands every 30 minutes on macOS




Raw

 news.md


## Summary

MuMu Player Pro for macOS (by NetEase) executes a comprehensive system data collection routine every 30 minutes while the emulator is running. This includes enumerating all devices on your local network, capturing every running process with full command-line arguments, inventorying all installed applications, reading your hosts file, and dumping kernel parameters -- all tied to your Mac's serial number via SensorsData analytics.

None of this is disclosed in MuMu's privacy policy. None of it is necessary for an Android emulator to function.

## Environment

* App: MuMu Player Pro for macOS (v1.8.5)
* Bundle ID:com.netease.mumu.nemux-global
* macOS version: 26.3 (Apple Silicon)

## What it collects

Every 30 minutes, MuMu creates a timestamped directory under:

~/Library/Application Support/com.netease.mumu.nemux-global/logs/

Each directory (e.g.20260220-071645) contains the output of the following commands, all executed automatically in the background:

File

Command executed

What it captures

arpAll.txt

arp -a

Every device on your local network (IPs + MAC addresses)

ifconfig.txt

ifconfig

All network interfaces, MAC addresses, IP addresses, VPN tunnels

networkDNS.txt

scutil --dns

Full DNS resolver configuration

networkProxy.txt

scutil --proxy

Proxy settings

catHosts.txt

cat /etc/hosts

Your entire hosts file (exposes custom domains, dev environments)

netstat.txt

netstat

Active network connections (times out after 15s)

listProcess.txt

ps aux

Every running process
 with full arguments (~200KB)

listApplications.txt

ls -laeTO -@ /Applications/

All installed applications with metadata

mdlsApplications.txt

mdls /Applications/*.app

Spotlight metadata for every app (name, version, bundle ID, size, dates)

sysctl.txt

sysctl -a

Kernel parameters, hostname, hardware info, boot time (~60KB)

launchctlPrintSystem.txt

launchctl print system

Full system service dump (~64KB)

launchctlLimit.txt

launchctl limit

System resource limits

listLaunchAgents.txt

ls -laeTO -@ /Library/LaunchAgents

All system launch agents

listLaunchDaemons.txt

ls -laeTO -@ /Library/LaunchDaemons

All system launch daemons

mount.txt

mount

All mounted filesystems

custom-curl-apipro.txt

curl -v https://pro-api.mumuplayer.com

Connectivity test to MuMu API

custom-curl-mumuapipro.txt

curl -v https://api.mumuglobal.com

Connectivity test to MuMu global API

Acollect-finishedmanifest file logs the success/failure of each collection.

## Theps auxproblem

The process list captures full command-line arguments for every process on the system. In practice this exposes:

* What applications you're running and when (browsers, chat apps, trading platforms, security tools)
* VPN usage and configuration (e.g. NordVPN/NordLynx with arguments)
* Development tools and infrastructure (Docker, IDEs, terminal sessions with arguments)
* Session tokens and IDs passed as command-line arguments
* User data directory paths revealing your username and app configurations
* What security/firewall software you use (useful for evasion)

This is captured every 30 minutes, creating a detailed behavioral timeline of your computer usage.

## Analytics and device fingerprinting

MuMu usesSensorsData(a Chinese analytics platform) for tracking. Files in thereport/directory include:

Identity tracking(sensorsanalytics-com.sensorsdata.identities.plist):

{

"$identity_login_id"
:
"
<user_id>
"
,

"$identity_anonymous_id"
:
"
<anonymous_id>
"
,

"$identity_mac_serial_id"
:
"
<your_mac_serial_number>
"

}

Your Mac's hardware serial number is collected and used as a persistent identifier.

Campaign tracking(sensorsanalytics-super_properties.plist):

player_version: 1.8.5
player_channel: MACPRO
player_uuid: <UUID>
player_utm_source: SEO001
player_engine: (tracked)

An 86KB analytics message queue (sensorsanalytics-message-v2.plist) is maintained and sent to their servers.

## Collection frequency

On a single day of normal use, MuMu ran the collection routine16 times(once every ~30 minutes). Each collection generates ~400KB of system data. The logs directory retains approximately 23 collection runs before rotating.

## How to verify

If you have MuMu Player Pro installed on macOS, check:

ls
~
/Library/Application
\
Support/com.netease.mumu.nemux-global/logs/

If you see timestamped directories, open any one and read the files. Each file contains the exact command that was executed, its arguments, and the full captured output.

## What MuMu's privacy policy says

TheMuMu Player Pro Privacy Policydoes not disclose:

* Runningps auxto capture all system processes
* Runningarp -ato enumerate local network devices
* Reading/etc/hosts
* Dumpingsysctl -akernel parameters
* Inventorying all installed applications viamdls
* Collecting your Mac serial number
* Performing any of this on a 30-minute recurring schedule

## Conclusion

This goes well beyond what any Android emulator needs. The data collected -- local network topology, complete process lists, installed software inventory, DNS configuration, hosts file, and kernel parameters -- constitutes a comprehensive system profile. Combined with SensorsData analytics and your hardware serial number, this creates a persistent, detailed fingerprint of your machine and usage patterns.

The fact that this runs silently every 30 minutes, is not disclosed in the privacy policy, and is not necessary for emulator functionality makes this, at minimum, a serious transparency failure.



### UjuiUjuMandancommentedFeb 20, 2026

The commands run are likely used for network diagnostics. AFAIK, all Chinese software tends to become the user's 'PC manager.'

And here is a question: thereport/files are sent to their server, but are thelogs/files we most care about sent, too?

And the apparently LLM tone makes this article less credible.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.





Sign up for free

to join this conversation on GitHub
.
 Already have an account?

Sign in to comment
