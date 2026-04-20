---
title: '"TotalRecall Reloaded" tool finds a side entrance to Windows 11''s Recall database - Ars Technica'
url: https://arstechnica.com/gadgets/2026/04/totalrecall-reloaded-tool-finds-a-side-entrance-to-windows-11s-recall-database/
site_name: newsfeed
content_file: newsfeed-totalrecall-reloaded-tool-finds-a-side-entrance-to
fetched_at: '2026-04-16T11:59:00.523782'
original_url: https://arstechnica.com/gadgets/2026/04/totalrecall-reloaded-tool-finds-a-side-entrance-to-windows-11s-recall-database/
date: '2026-04-15'
published_date: '2026-04-15T20:36:28+00:00'
description: The vault is solid. The delivery truck is not."
tags:
- ars-technica
- security
- tech
- windows 11
---

Text
 settings

Two years ago, Microsoft launched its first wave of “Copilot+” Windows PCs with a handful of exclusive features that could take advantage of the neural processing unit (NPU) hardware being built into newer laptop processors. These NPUs could enable AI and machine learning features that could run locally rather than in someone’s cloud, theoretically enhancing security and privacy.

One of the first Copilot+ features was Recall, a feature that promised to track all your PC usage via screenshot to help you remember your past activity. But as originally implemented, Recall wasneither private nor secure; the feature stored its screenshots plus a giant database of all user activity in totally unencrypted files on the user’s disk, making it trivial for anyone with remote or local access to grab days, weeks, or even months of sensitive data, depending on the age of the user’s Recall database.

After journalists and security researchers discovered and detailed these flaws, Microsoft delayed the Recall rollout byalmost a yearand substantiallyoverhauled its security. All locally stored data would now be encrypted and viewable only with Windows Hello authentication; the feature now did a better job detecting and excluding sensitive information, including financial information, from its database; and Recall would be turned off by default, rather than enabled on every PC that supported it.

The reconstituted Recallwas a big improvement, but having a feature that records the vast majority of your PC usage is still a security and privacy risk. Security researcher Alexander Hagenah was the author of the original “TotalRecall” tool that made it trivially simple to grab the Recall information on any Windows PC, and an updated “TotalRecall Reloaded” version exposes what Hagenah believes are additional vulnerabilities.

The problem, as detailed by Hagenah onthe TotalRecall GitHub page, isn’t with the security around the Recall database, which he calls “rock solid.” The problem is that, once the user has authenticated, the system passes Recall data to another system process calledAIXHost.exe, andthatprocess doesn’t benefit from the same security protections as the rest of Recall.

“The vault is solid,” Hagenah writes. “The delivery truck is not.”

The TotalRecall Reloaded tool uses an executable file to inject a DLL file intoAIXHost.exe, something that can be done without administrator privileges. It then waits in the background for the user to open Recall and authenticate using Windows Hello. Once this is done, the tool can intercept screenshots, OCR’d text, and other metadata that Recall sends to theAIXHost.exeprocess, which can continue even after the user closes their Recall session.

“The VBS enclave won’t decrypt anything without Windows Hello,” Hagenah writes. “The tool doesn’t bypass that. It makes the user do it, silently rides along when the user does it, or waits for the user to do it.”

A handful of tasks, including grabbing the most recent Recall screenshot, capturing select metadata about the Recall database, and deleting the user’s entire Recall database, can be done with no Windows Hello authentication.

Once authenticated, Hagenahsaysthe TotalRecall Reloaded tool can access both new information recorded to the Recall database as well as data Recall has previously recorded.

## Bug or not, Recall is still risky

For its part, Microsoft has said that Hagenah’s discovery isn’t actually a bug and that the company doesn’t plan to fix it. Hagenah originally reported his findings to Microsoft’s Security Response Center on March 6, and Microsoft officially classified it as “not a vulnerability” on April 3.

“We appreciate Alexander Hagenah for identifying and responsibly reporting this issue. After careful investigation, we determined that the access patterns demonstrated are consistent with intended protections and existing controls, and do not represent a bypass of a security boundary or unauthorized access to data,” a Microsoft spokesperson told Ars. “The authorization period has a timeout and anti-hammering protection that limit the impact of malicious queries.”

Regardless of Recall’s underlying security, Recall can still constitute a major security and privacy risk. Anyone with access to your PC and your Windows Hello fallback PIN can access your database and everything in it, and even though Recall’s content filters do a decent job excluding things like sensitive financial information, someone with access to your system could still see all kinds of emails, messages, web activity, and other stuff that you’d prefer not to share.

Given the sheer amount of information that Recall can record, it still feels like a whole lot of potential downside for a pretty narrow and limited upside.

The feature’s riskiness has prompted some app developers to take matters into their own hands. The Signal Messenger app on Windowsforces Recall to ignore it by default, using a flag that’s normally intended to keep DRM-protected content out of the Recall database. TheAdGuard ad blocker, theBrave browser, and others have implemented similar workarounds.

 Andrew Cunningham


Senior Technology Reporter

 Andrew Cunningham


Senior Technology Reporter

 Andrew is a Senior Technology Reporter at Ars Technica, with a focus on consumer tech including computer hardware and in-depth reviews of operating systems like Windows and macOS. Andrew lives in Philadelphia and co-hosts a weekly book podcast called
Overdue
.


1. 1.Vulcan woes will "absolutely" be a factor in Pentagon's next rocket competition
2. 2.Florida surgeon charged with killing man after removing liver instead of spleen
3. 3.What’s the deal with Alzheimer’s disease and amyloid?
4. 4.Google releases new apps for Windows and MacOS
5. 5.Bubble watch: Fashion brand Allbirds pivots hard to become AI services company

Customize
