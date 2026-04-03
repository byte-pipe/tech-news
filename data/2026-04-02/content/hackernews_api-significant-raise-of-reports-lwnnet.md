---
title: Significant raise of reports [LWN.net]
url: https://lwn.net/Articles/1065620/
site_name: hackernews_api
content_file: hackernews_api-significant-raise-of-reports-lwnnet
fetched_at: '2026-04-02T19:24:42.895119'
original_url: https://lwn.net/Articles/1065620/
author: stratos123
date: '2026-04-02'
description: Significant Raise of Reports
tags:
- hackernews
- trending
---

LWN
.net

News from the source

 

User:
 

Password:
 
 
 
 |
 

 |
 

Log in
 /
 
Subscribe
 /
 
Register

# Significant raise of reports

## Significant raise of reports

 Posted Mar 31, 2026 17:11 UTC (Tue) by 
wtarreau
 (subscriber, #51152)

 
 Parent article: 
Vulnerability Research Is Cooked (sockpuppet.org)

On the kernel security list we've seen a huge bump of reports. We were between 2 and 3 per week maybe two years ago, then reached probably 10 a week over the last year with the only difference being only AI slop, and now since the beginning of the year we're around 5-10 per day depending on the days (fridays and tuesdays seem the worst). Now most of these reports are correct, to the point that we had to bring in more maintainers to help us.And we're now seeing on a daily basis something that never happened before: duplicate reports, or the same bug found by two different people using (possibly slightly) different tools.It's a bit scary (and tiring), but at least compared to the previous era of AI slop, you feel like you're not working for nothing because bugs get fixed. Also it's interesting to keep thinking that these bugs are within reach from criminals so they deserve to get fixed.I don't know how long this pace will last. I suspect that bugs are reported faster than they are written, so we could in fact be purging a long backlog (and I hope so).Something I'm predicting is that at least it will change the approach to security fixes:- embargoes will probably disappear, and for good: what's the point of hiding something that others can instantly find? I have not seen one in a while and that's good.- people will finally understand that security bugs are bugs, and that the only sane way to stay safe is to periodically update, without focusing on "CVE-xxx"- software that used to follow the "release-then-go-back-to-cave" model will have to change to start dealing with maintenance for real, or to just stop being proposed to the world as the ultimate-tool-for-this-and-that because every piece of software becomes a target.Overall I think we're going to see a much higher quality of software, ironically around the same level than before 2000 when the net became usable by everyone to download fixes. When the software had to be pressed to CDs or written to millions of floppies, it had to survive an amazing quantity of tests that are mostly neglected nowadays since updates are easy to distribute. But before this happens, we have to experience a huge mess that might last for a few years to come! Interesting times...to post comments### Significant raise of reportsPosted Mar 31, 2026 17:31 UTC (Tue)
 bygf2p8affineqb(subscriber, #124723)
 [Link] (1 responses)How does this compare to Syzbot? I see there are 1300 open issues right now on its dashboard.### Significant raise of reportsPosted Mar 31, 2026 17:49 UTC (Tue)
 byhailfinger(subscriber, #76962)
 [Link]The easiest way to get attention to the backlog of syzbot reports (but absolute worst way to overload maintainers) is using them in an exploit chain. I expect that to happen pretty soon (or maybe it is already happening).It's the old method of framing bugs as security bugs to get attention.### Significant raise of reportsPosted Mar 31, 2026 19:28 UTC (Tue)
 byrgmoore(✭ supporter ✭, #75)
 [Link]I don't know how long this pace will last. I suspect that bugs are reported faster than they are written, so we could in fact be purging a long backlog (and I hope so).This makes sense, and the key way of making sure the bug reports are primarily about purging a backlog is to apply the same kind of scrutiny to code before it ever gets merged. Basically, the key is to use AI to improve code quality (both already merged and pre-merge) rather than just spamming as much new stuff as possible. This matches up very well with the article on Andrew Morton trying to make Sashiko a required part of submissions to the memory management subsystem.### Significant raise of reportsPosted Mar 31, 2026 20:36 UTC (Tue)
 byfw(subscriber, #26023)
 [Link] (1 responses)My recommendation to one particular struggling security team was to triage what absolutely needs to be fixed under embargo—and work on fixes for those things only. The rest is published without an embargo and a fix. This way, everyone in the development community can chip in. Maybe even the various zero-CVE vendors can provide fixes if they want to stay true to their mission.The previous approach, with the desire to have fixes available at the time of disclosure (with or without embargo/grace period for distributions) does not seem to work anymore. It doesn't encourage community collaboration, and it paves the way for rather extreme forms of freeloading.### Significant raise of reportsPosted Mar 31, 2026 21:16 UTC (Tue)
 bywtarreau(subscriber, #51152)
 [Link]> My recommendation to one particular struggling security team was to triage what absolutely needs to be fixed under embargo—and work on fixes for those things only. The rest is published without an embargo and a fix. This way, everyone in the development community can chip in. Maybe even the various zero-CVE vendors can provide fixes if they want to stay true to their mission.It's not much different from what we're doing, and due to the high volume we can only triage now. Syzbot reports are systematically redirected to public lists, all the stuff that doesn't represent an immediate risk of escalation but might only be used to lower some barriers (e.g. local kASLR defeats) or stuff that's outside the threat model gets the same fate, and the rest is often challenged a bit (e.g. unclear or too old version, dubious claims etc), we ask for patches and most of the time the reporters are interested in helping and they do their final share of the work, then we forward to maintainers and try to help both to get the issue fixed and merged ASAP. Many reporters are not familiar with processes, and it's the same for maintainers getting begged for the first time. It's extremely rare these days that issues are attempted to be resolved within the list (except if the maintainer is already there) as all subsystems are willing to participate to the resolution now, so the fixes are super fast, in a matter of days you can count on a single hand most of the time, which would make embargoes totally pointless anyway and even counter-productive.> The previous approach, with the desire to have fixes available at the time of disclosure (with or without embargo/grace period for distributions) does not seem to work anymore. It doesn't encourage community collaboration, and it paves the way for rather extreme forms of freeloading.I totally agree. And the only way it makes sense is when there's a risk of remote exploitation (e.g. RCE) but then it keeps users exposed longer, which is against the initial goal. Also this doesn't take into account the different levels of exposure of different classes of users due to different use cases. On the kernel, with a release every week, it's best to just merge and release. OpenSSL for example does one thing well, since they don't release often, they often indicate upfront that a fix is going to be released a few days later so that users can get prepared to downloading the fix and deploying. In haproxy as well we're going away from embargoes. We keep them only for critical stuff that affects common deployments with no reasonable workaround (e.g. about once a year or so), and we leave two or three days to some high profile users to deploy a fix and to distros to prepare packages. Each time it remains confusing for everyone involved and the risk of mistake remains high, so the least often the better. BTW it's well known that embargoed issues generally need two fixes: the first one which works on the reporter and the developer's machine, and the second one which fixes regressions in the field.

 

 

 

Copyright © 2026, Eklektix, Inc.Comments and public postings are copyrighted by their creators.Linux is a registered trademark of Linus Torvalds