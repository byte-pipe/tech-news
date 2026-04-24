---
title: Ubuntu 26.04 LTS released [LWN.net]
url: https://lwn.net/Articles/1069399/
site_name: hackernews_api
content_file: hackernews_api-ubuntu-2604-lts-released-lwnnet
fetched_at: '2026-04-24T11:56:29.263533'
original_url: https://lwn.net/Articles/1069399/
author: lxst
date: '2026-04-24'
description: Ubuntu 26.04
tags:
- hackernews
- trending
---

Ubuntu 26.04 ("Resolute Raccoon") LTS has beenreleasedon schedule.

This release brings a significant uplift in security, performance,
and usability across desktop, server, and cloud environments. Ubuntu
26.04 LTS introduces TPM-backed full-disk encryption, expanded use of
memory-safe components, improved application permission controls, and
Livepatch support for Arm systems, helping reduce downtime and
strengthen system resilience. [...]

The newest Edubuntu, Kubuntu, Lubuntu, Ubuntu Budgie, Ubuntu Cinnamon,
Ubuntu Kylin, Ubuntu Studio, Ubuntu Unity, and Xubuntu are also being
released today. For more details on these, read their individual release
notes under the Official flavors section:

https://documentation.ubuntu.com/release-notes/26.04/#official-flavors

Maintenance updates will be provided for 5 years for Ubuntu Desktop, Ubuntu
Server, Ubuntu Cloud, Ubuntu WSL, and Ubuntu Core. All the remaining flavors
will be supported for 3 years.

See therelease
notesfor a list of changes, system requirements, and more.

 to post comments
 

### MATE?Posted Apr 23, 2026 22:10 UTC (Thu)
 byatai(subscriber, #10977)
 [Link] (1 responses)What happens to the Mate Desktop edition?### MATE?Posted Apr 23, 2026 22:29 UTC (Thu)
 byjpeisach(subscriber, #181966)
 [Link]Currently looking for new maintainers:https://discourse.ubuntu.com/t/ubuntu-mate-seeking-mainta...### Suggestion for bug reportPosted Apr 24, 2026 9:09 UTC (Fri)
 bymote(guest, #173576)
 [Link]I caught this in the XUbuntu release notes:https://bugs.launchpad.net/ubuntu/+source/openssh/+bug/21...If anyone has a login to this system and can post an update, as an Arch + Xfce + gcr4 user a solution, one needs to add the unit `gcr-ssh-agent.socket` to the user units for systemd (i.e., /etc/systemd/user/sockets.target.wants/gcr-ssh-agent.socket ). This unit is provided by the gcr4 package and does exactly what they're discovering, sets SSH_AUTH_SOCK on login to match the running gcr-ssh-agent.