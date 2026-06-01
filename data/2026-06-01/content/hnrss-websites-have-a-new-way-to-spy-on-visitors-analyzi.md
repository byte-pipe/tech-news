---
title: 'Websites have a new way to spy on visitors: Analyzing their SSD activity - Ars Technica'
url: https://arstechnica.com/security/2026/05/websites-have-a-new-way-to-spy-on-visitors-analyzing-their-ssd-activity/
site_name: hnrss
content_file: hnrss-websites-have-a-new-way-to-spy-on-visitors-analyzi
fetched_at: '2026-06-01T12:55:45.033398'
original_url: https://arstechnica.com/security/2026/05/websites-have-a-new-way-to-spy-on-visitors-analyzing-their-ssd-activity/
date: '2026-05-28'
published_date: '2026-05-27T20:56:03+00:00'
description: Telltale SSD activity can be measured in the browser using simple JavaScript.
tags:
- hackernews
- hnrss
---

Text
 settings

Over the decades, there has been no shortage of sites using clever techniques to covertly track visitors’browsing histories,device fingerprints, andkeystrokes and mouse movementsin real time. Even Meta and Yandex were recently caught joining in the privacy-invasivefree-for-all.

Now sites have a new way to spy on their visitors: measuring subtle interactions with their solid-state drives. The technique, named FROST (fingerprinting remotely using OPFS-based SSD timing), allows sites to monitor other sites a visitor is viewing and what apps are open on their devices.

## A side channel based on contention

The technique, laid out in aresearch paper, exploits aside channel, a form of leak resulting from physical manifestations such as electromagnetic emanations, data caches, or the time required to complete a task. By measuring the manifestations, attackers can decrypt encrypted traffic and infer other confidential data.

The attack that FROST uses is known as acontention side channel, which measures the interaction of various processes all using (or competing for) a given resource. By measuring the timing of certain I/O (input-output) operations of the SSD a visitor is using, the researchers were able to determine the websites open in other tabs—even on other browsers—and the apps that were open on the visitor’s device. FROST requires no interaction from the visitor other than opening the site hosting the attack.

“Web browsers have evolved from simple document viewers into complex platforms capable of running sophisticated applications,” the paper authors wrote. “Companies like Google, Microsoft, and Adobe have developed full-fledged office suites, photo- and video editors, or even integrated development environments (IDEs) that run entirely within the browser.” The authors went on to note: “While these features enhance the capabilities of web applications and allow completely novel use cases, they also increase the browser’s attack surface, and some have already been shown to introduce new vulnerabilities.”

Unlike previous contention side-channel attacks on SSDs, FROST runs exclusively in the browser. It uses JavaScript that interacts with theOPFS(origin private file system), an allocated storage space that’s reserved for a specific site to run code needed to complete a given task. Websites can create one with no interaction required by the visitor.

While each file system is sandboxed, meaning it’s isolated from other websites and from the device system itself, the JavaScript can measure the I/O interactions. Then, by running those interactions through a pretrainedconvolutional neural network—a system that uses deep learning to analyze text, audio, and images—the attacker can deduce various apps and websites open on the device.

“The attacker continuously measures SSD contention by performing random reads from a large OPFS file,” the researchers explained. “SSD contention caused by user activity causes measurable latency differences for these read operations. By training a convolutional neural network (CNN) on these traces, the attacker can fingerprint user activity on the host system by classifying new traces using the trained model.”

The technique has its limitations. First, the OPFS file must be extremely large—likely a gigabyte or more. That requirement means that attacks at scale would inevitably be detected by many users. Additionally, the OPFS file must be stored on the same SSD the visitor is using. This isn’t usually a problem for tracking open websites, since the OPFS file is stored in the browser’s default location. In the event apps are using a separate SSD drive for apps, those apps couldn’t be detected by FROST.

One of the best ways to prevent FROST attacks is to close tabs as soon as they’re no longer needed. More savvy users can monitor the creation and size of OPFS files allocated by unknown websites. The researchers proposed ways for browser makers to shut down the side channel. One such method is to limit the maximum size of such files that are allowed. There are no indications FROST attacks have been performed in the wild.

The researchers performed the full Frost attack on an M2 Mac. On Linux, they showed that the underlying primitive (measuring SSD access latency traces from JavaScript) works, but didn’t run the full attack.

“However, since the performance of the primitive is similar between macOS and Linux, we expect similar performance for the full classification,” Hannes Weissteiner, one of the co-authors, wrote in an email. “In principle, it would be possible to train a model on any system activity that reliably generates SSD accesses.”

The researchers did not test Windows.

The paper linked above provides many more technical details. The research is scheduled to be presented at theDIMVA conferencein July.

 Dan Goodin
 

Senior Security Editor

 Dan Goodin
 

Senior Security Editor

 Dan Goodin is Senior Security Editor at Ars Technica, where he oversees coverage of malware, computer espionage, botnets, hardware hacking, encryption, and passwords. In his spare time, he enjoys gardening, cooking, and following the independent music scene. Dan is based in San Francisco. Follow him at 
here
 on Mastodon and 
here
 on Bluesky. Contact him on Signal at DanArs.82.
 

1. 1.Here's why the failure of Blue Origin's New Glenn rocket is so catastrophic
2. 2.Proposed new US funding rules: We can cancel any grant at any time
3. 3.Rocket Report: A dark day for Blue Origin; Pentagon eyes new launch site
4. 4.Fed up with vibe coders, dev sneaks data-nuking prompt injection into their code
5. 5.Steam Deck sells out in North America within 24 hours of price hike

Customize