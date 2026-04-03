---
title: 'Last Week on My Mac: Why E cores make Apple silicon fast – The Eclectic Light Company'
url: https://eclecticlight.co/2026/02/08/last-week-on-my-mac-why-e-cores-make-apple-silicon-fast/
site_name: hnrss
content_file: hnrss-last-week-on-my-mac-why-e-cores-make-apple-silicon
fetched_at: '2026-02-08T19:12:25.732285'
original_url: https://eclecticlight.co/2026/02/08/last-week-on-my-mac-why-e-cores-make-apple-silicon-fast/
date: '2026-02-08'
published_date: '2026-02-08T08:00:00+00:00'
description: Apple silicon architecture is designed to get background processes out of the way of our apps running in the foreground, by using the E cores.
tags:
- hackernews
- hnrss
---

If you use an Apple silicon Mac I’m sure you have been impressed by its performance. Whether you’re working with images, audio, video or building software, we’ve enjoyed a new turn of speed since the M1 on day 1. While most attribute this to their Performance cores, as it goes with the name, much is in truth the result of the unsung Efficiency cores, and how they keep background tasks where they should be.

To see what I mean, start your Apple silicon Mac up from the cold, and open Activity Monitor in its CPU view, with its CPU History window open as well. For the first five to ten minutes you’ll see its E cores are a wall of red and green with Spotlight’s indexing services, CGPDFService, mediaanalysisd, BackgroundShortcutRunner, Siri components, its initial Time Machine backup, and often an XProtect Remediator scan. Meanwhile its P cores are largely idle, and if you were to dive straight into using your working apps, there’s plenty of capacity for them to run unaffected by all that background mayhem.

It’s this stage that scares those who are still accustomed to using Intel Macs. Seeing processes using more than 100% CPU is terrifying, because they know that Intel cores can struggle under so much load, affecting user apps. But on an Apple silicon Mac, who notices or cares that there’s over a dozen mdworker processes each taking a good 50% CPU simultaneously? After all, this is what the Apple silicon architecture is designed for. Admittedly the impression isn’t helped by a dreadful piece of psychology, as those E cores at 100% are probably running at a frequency a quarter of those of P cores shown at the same 100%, making visual comparisoncompletely false.*

This is nothing new. Apple brought it to the iPhone 7 in 2016, in its first SoC with separate P and E cores. That’s an implementation of Arm’sbig.LITTLEannounced in 2011, anddevelopment work at Crayand elsewhere in the previous decade. What makes the difference in Apple silicon Macs is how threads are allocated to the two different CPU core types on the basis of a metric known asQuality of Service, or QoS.

As with so much in today’s Macs, QoS has been around sinceOS X 10.10 Yosemite, six years before it became so central in performance. When all CPU cores are the same, it has limited usefulness over more traditional controls like Posix’snicescheduling priority. All those background tasks still have to be completed, and giving them a lower priority only prolongs the time they take on the CPU cores, and the period in which the user’s apps are competing with them for CPU cycles.

With the experience gained from its iPhones and other devices, Apple’s engineers had a better solution for future Macs. In addition to providing priority-based queues, QoS makes a fundamental distinction between those threads run in the foreground, and those of the background. While foreground threads will be run on P cores when they’re available, they can also be scheduled on E cores when necessary. But background threads aren’t normally allowed to run on P cores, even if they’re delayed by the load on the E cores they’re restricted to. We know this from our inability to promote existing background threads to run on P cores using St. Clair Software’sApp Tamerand the command tooltaskpolicy.

This is why, even if you sit and watch all those background processes loading the E cores immediately after starting up, leaving the P cores mostly idle, macOS won’t try running them on its P cores. If it did, even if you wanted it to, the distinction between foreground and background, P and E cores would start to fall apart, our apps would suffer as a consequence, and battery endurance would decline. Gone are the days ofcrashing mdworker processesbringing our Macs to their knees with a spinning beachball every few seconds.

If seeing all those processes using high % CPU can look scary, the inevitable consequence in terms of software architecture might seem terrifying. Rather than building monolithic apps, many of their tasks are now broken out into discrete processes run in the background on demand, on the E cores when appropriate. The fact that an idle Mac has over 2,000 threads running in over 600 processes is good news, and the more of those that are run on the E cores, the faster our apps will be. The first and last M-series chips to have only two E cores were the M1 Pro and Max, since when every one has had at least four E cores, and some as many as six or eight.

Because Efficiency cores get the background threads off the cores we need for performance.

*For the record, I have measured those frequencies using powermetrics. For anM4 Pro, for example, high QoS threads running on the P cores benefit from frequencies close to the P core max of 4,512 MHz. Low QoS threads running on the E cores are run at frequencies close to idle, typically around 1,050 MHz. However, when the E cores run high QoS threads that have overflowed from the P cores, the E cores are normally run at around their maximum of 2,592 MHz. By my arithmetic, 1,050 divided by 4,512 is 0.233, which is slightly less than a quarter. Other M-series chips are similar.

### Share this:

* Share on X (Opens in new window)X
* Share on Facebook (Opens in new window)Facebook
* Share on Reddit (Opens in new window)Reddit
* Share on Pinterest (Opens in new window)Pinterest
* Share on Mastodon (Opens in new window)Mastodon
* Share on Bluesky (Opens in new window)Bluesky
* Email a link to a friend (Opens in new window)Email
* Print (Opens in new window)Print
Like

Loading...

### Related
