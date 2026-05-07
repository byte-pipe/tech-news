---
title: The man with an army of Yarbo robot lawn mowers | The Verge
url: https://www.theverge.com/tech/925696/yarbo-robot-lawn-mower-hack-remote-control-camera-access-mqtt
site_name: newsfeed
content_file: newsfeed-the-man-with-an-army-of-yarbo-robot-lawn-mowers-th
fetched_at: '2026-05-07T20:12:59.273722'
original_url: https://www.theverge.com/tech/925696/yarbo-robot-lawn-mower-hack-remote-control-camera-access-mqtt
author: Sean Hollister
date: '2026-05-07'
published_date: '2026-05-07T16:00:00+00:00'
description: "\uFEFFForget robovacs — Yarbo’s bladed robots are an even bigger security nightmare."
tags:
- the-verge
- news
- report
- security
---

* Tech
* News
* Report

# A hacker ran me over with a robot lawn mower

﻿Forget robovacs — Yarbo’s bladed robots are an even bigger security nightmare.

by
 
 
Sean Hollister
May 7, 2026, 4:00 PM UTC
* Link
* Share
* Gift
A Yarbo lawnmower with a trimmer attachment.
 
| Image: Yarbo
Sean Hollister
 
is a senior editor and founding member of The Verge who covers gadgets, games, and toys. He spent 15 years editing the likes of CNET, Gizmodo, and Engadget.

I’m lying in the dirt. It’s coming for me. Then, with a lurch, it’s climbing up my chest. If Andreas Makris doesn’t stop the 200-pound robot lawn mower in time, it could drag its blades across my body.

Makris certainly can’t reach over and hit the emergency stop button — he’s nearly 6,000 miles away, having hacked this robot from the other side of the planet, to demonstrate the gaping security holes in Yarbo’s robot lawn mowers. And I’ve made the questionable decision of lying down in the mower’s path — to see just how far Makris, the security researcher who discovered those flaws, is able to push the mower.

Yep, that’s me. 
 
Animation by Sean Hollister / The Verge

By the time the mower touches my body, Makris has already proven his point: the $5,000 robot lawn mowers from Yarbo have such ridiculous security vulnerabilities that a foreign hacker caneasilyhijack a bladed gadget in the United States. And not just one. Thousands upon thousands of bladed Chinese robots at his beck and call. Every Yarbo robot around the world, whether configured to churn through grass, snow, or weeds, is theoretically reporting to him now.

“I can do whatever I want with all the bots,” Makris tellsThe Verge. “It’s completely unsecured.”

And believe it or not, remote control is just the tip of the iceberg.

Like Sammy Azdoufal, who made headlines worldwide whenThe Vergeexclusively revealed how he made thousands of DJI Romo robot vacuum cleanersidentify themselves and begin following his commands, Makris discovered that Yarbo’s robots do much the same thing. If you have access to one robot, you have access to them all.

Buttheserobots have blades — and hackers can use the robot’s built-in commands to override its safety features. Even if you press that big red emergency stop button on the mower itself, a hacker can send another command to unlock it, Makris says.

And because the Yarbo is a full Linux computer, one with its own backdoor and where the root password is always the same, hackers could remotely reprogram it to do anything: spin up the blades, probe your home network, turn your robot into part of a botnet to harass targets on the internet.

The Yarbo robot can power a snowblower attachment, too.
 
Video: Yarbo

Founded in 2015 as a robot snowblower company, Yarbo sells all-in-one yard robots with modular attachments that let it become a lawn mower, leaf blower, snowblower, trimmer, and edger. Each attachment is pushed or pulled by the same “core” robot that uses tank treads to drive and climb — which is why all of them may be vulnerable to hackers.

Makris begins by showing me a vibe-coded map with the locations of ostensibly every Yarbo robot in the United States and Europe, around 5,400 devices. (He’s tracking over 11,000 of them worldwide.) Then, as I watch his video stream, he presses a button to take control of a robot in upstate New York.

This robot was already mowing a field, a white house visible in the background. But we interrupt its regularly scheduled programming. Makris drags a little onscreen joystick with his mouse, and I watch as the robot’s camera turns to reflect each of those moves. There’s little to keep him from driving anywhere he likes, spying on this family, figuring out when they come and go.

Similarly, there might be nothing keeping a bad actor from spying on, say, troop movements near a nuclear power plant. Makris has already identified 12 different Yarbo robots within 3 kilometers of a major power plant — one of which is seemingly registered to a nuclear security analyst.

Then, Makris makes my jaw drop yet again: He shows me he can pull owners’ email addresses, their Wi-Fi passwords, and the exact GPS coordinates of their houses. When I look up an address on Google Maps, I see a satellite view of what appears to be the same property we saw through the robot’s cameras.

Four days later, I’m driving through the Silicon Valley foothills in search of proof. At the very first house on my itinerary, my heart skips a beat. Looking down into one person’s hilly backyard from the sidewalk above, I see a Yarbo robot exactly where Makris pinpointed it would be. When I whip out my phone to scan for local Wi-Fi networks, I see the same private access points that Makris found in his scan.

When I later email the owner, using the same email address Yarbo’s robot coughed up, I get a reply. He agrees to meet in person.

Wayne Yu wants to know how his robot lawn mower led me straight to his door. A self-described gadget enthusiast, he says he’s not concerned that the Yarbo gave us photos of his house. “People are always hacking into devices, so I’m not surprised,” he tells me.

Nor is he concerned about someone stealing his lawn mower: “It’s heavy, and it’s uphill — you can see that, right? For me to walk down to the lawn mower, it’s hurting my legs already,” he laughs, adding that difficulty mowing the steep grade is why he bought a Yarbo in the first place. But when I ask him how he feels that the hacker is halfway across the planet, led me straight to his door, and gave me his email and Wi-Fi passwords, he says he’s uncomfortable. “Not good. Not good,” Yu repeats.

When I show him the Wi-Fi passwords, he confirms they’re his.

It’s all real.

Matt Petach, retired network architect and Yarbo owner.
 
Both Petach and Yu agreed that I could name them in the story.
 
Photo by Sean Hollister / The Verge

Matt Petach is less surprised that I wound up on his doorstep. Nothing seems to faze the retired Yahoo and Microsoft network architect, even when I show him his own Wi-Fi password. He says it’s an isolated guest network, oneset to automatically reject unknown devices, and that the guest password is just his publicly listed phone number.

Everyone should treat gadgets like these as hostile agents, Petach says. “It is unfortunate that in the name of convenience, homeowners and other users are really invited to treat technology as their best friend, their confident helper,” he tells me.

You should think of bad security like missing safety features on a power tool, he suggests: “This is a lot more like a chainsaw without a handguard, without a brake, with a loose chain that’s ready to take your leg off at a moment’s notice.”

But even Petach seems slightly taken aback at Yarbo’s security practices.

Makris explains thatnot onlydoes each Yarbo robot have the same hardcoded root password, but owners can’t defend themselves just by manually setting a better password. Every time Yarbo updates a robot’s firmware, it changes the robot’s root password right back to its default password. Hackers can come right back in. “Wow, that’s even worse than I thought,” Petach says.

It also appears that Yarbointentionallycreated the remote-access backdoor that allows for the very worst that hackers could do. “It is deployed automatically to every robot, cannot be disabled by the owner, and is actively restored if removed,” Makris writes.

In emails, Yarbo tries to assure Makris that the remote backdoor into every robot can’t be abused.
You can tap these emails to zoom in and read them.
 
Images: Andreas Makris

That’s why Makris decided to do something that security researchers generally avoid: Today, he’spublishing his research, includingofficial CVEvulnerabilitydisclosures, without giving Yarbo time to fix the problem first. When he first reached out to Yarbo to alert the firm to the issue, he couldn’t find a security contact or bug bounty program, and the company’s customer support tried to explain away remote access as a safe, useful feature that Yarbo’s engineers would only use to remotely diagnose customer problems.

Based on that and what he’s seen of Yarbo’s security practices — “either they don’t care enough or it’s a skill issue,” he says — Makris worries that Yarbo and other companies won’t learn the lesson and fix these problems unless they’re publicly shamed. “It’s the right thing to do, and that’s what we’re trying to do here: warning people and getting the information out for people to understand that this isby design badand nobody seems to care,” he says.

There are other reasons to believe that Yarbo might not be the most trustworthy entity out there. Yarbo says its “corporate headquarters” is in New York —its Kickstarter pageandwebsitecontain photos of fancy mid-rise offices. But Google Maps suggests itsactual New York addressis a single-story building that also houses two auto detailers, an insurance agency, andan Etsy shopspecializing in spiked leather bracelets. In fact, Yarbo isactually just another name for Hanyang Tech, which is based in Shenzhen, China.

In a Kickstarter campaign, Yarbo claims to be headquartered in New York…
 
Image: Yarbo
…but its New York office may be a single unit in this one-story building.
 
Image: Google

We’ve also tried to review Yarbo’s lawn mowers more than once over the last few years only to be met with unusual requests. The company’s PR contacts have repeatedly asked for assurances that we won’t publish a negative review, and once asked us to sign a “Cooperation Agreement” that included a non-disparagement clause and would have required us to “create and share a dedicated review article within 21 business days.” (We declined.) More recently, the company suggested: “if the product does not meet expectations during testing, we would anticipate your decision not to include Yarbo in the final article.” (Again, we did not agree to that.)

In emails toThe Verge, Yarbo says it will take actions based on Makris’ research.

While the company initially claimed to us, too, that its “diagnostic environment is not publicly accessible” and suggested there was little to worry about, Yarbo senior PR manager Showan Hou told us Thursday that Yarbo has identified a fix for one issue, at least.

“Following our internal review of the concerns brought to our attention, we identified an issue related to permission handling within part of the communication process between the Yarbo app and backend services. A fix has already been developed, and we are currently preparing the rollout. We expect the update to be deployed very soon,” he writes, adding that Yarbo is continuing to investigate.

(Note that many of the issues are in the robot’s firmware, not just in app-to-server communication.)

Yarbo is also “actively implementing an in-app customer approval mechanism, clearer session visibility, stronger audit logging, and customer-facing access history so that remote diagnostic access is transparent, limited, and revocable,” he says, and the company is “actively planning a dedicated Security Response Center on our website to provide a clearer channel for vulnerability reporting and researcher engagement.” It’s also considering a bug bounty program.

“We understand the seriousness of the concerns raised, and we are treating this as a priority matter,” he says.

When Makris originally told the company that remote access was a huge security risk, Yarbo claimed that “your Yarbo remains completely secure and under your exclusive control.”

That’s why I eventually end up beneath a Yarbo mower — as part of a controlled test to see just how safe and “secure” the machine really is. I’ve already learned that the danger goes far beyond the blades; that we live in a wild west where modern gadgets can expose your exact GPS location, remote-control live video of your home, and compromise your home network in one fell swoop.

When I talk to researchers like Makris, it’s clear that Yarbo is just one particularly egregious example in an ocean of insecure devices. But an example like Yarbo can help us understand how bad things have gotten.

One Friday, with his permission, I roll up to Petach’s house. We hop onto a video call: Makris in Germany, Petach in Southern California, myself as the only one physically at the house. With a few clicks, Makris hijacks the Yarbo right in front of my eyes, both while idle and while it’s already in the middle of mowing sessions. I see that he sees me through the Yarbo’s cameras.

It’s time to see if the Yarbo has any built-in safety mechanisms,like, say, obstacle avoidance. I lie down on the ground.

I’m not a complete idiot. The blades aren’t spinning, and we’re running the robot in reverse — so its tank treads, not its blades, hit me first.

But as the first hundred pounds of metal, plastic, and far-too-hackable computer pin my body to the ground — and Makris eventually, thankfully, backs off — I realize this science experiment wasn’tquiteas safe as I thought.

Update, May 7th:Added Yarbo’s additional comment.

Follow topics and authors
 from this story to see more like this in your personalized homepage feed and to receive email updates.
* Sean Hollister
* News
* Report
* Security
* Tech

## Most Popular

Most Popular
1. Here’s what Microsoft is offering long-serving employees to voluntarily retire
2. Nintendo announces a new Star Fox for the Switch 2
3. Apple agrees to pay iPhone owners $250 million for not delivering AI Siri
4. Google shuts down Project Mariner
5. Musk’s biggest loyalist became his biggest liability

## The Verge Daily

A free daily digest of the news that matters most.

Email (required)
Sign Up
By submitting your email, you agree to our
 
Terms
 and 
Privacy Notice
. 
This site is protected by reCAPTCHA and the Google
 
Privacy Policy
 
and
 
Terms of Service
 
apply.
Advertiser Content From

This is the title for the native ad

## More inTech

Live updates from Musk v. Altman
Did Microsoft just tease a new Xbox UI?
Inside the return of Xbox
Apple’s $599 MacBook Neo could be at risk from rising RAM prices

5

Verge Score

Samsung’s flagship laptop is a MacBook Pro clone gone horribly wrong
Google’s taking a big swing at AI health with the Fitbit Air
Live updates from Musk v. Altman
Elizabeth Lopatto
 and 
Hayden Field
17 minutes ago
Did Microsoft just tease a new Xbox UI?
Tom Warren
Two hours ago
Inside the return of Xbox
Tom Warren
4:00 PM UTC
Apple’s $599 MacBook Neo could be at risk from rising RAM prices
Stevie Bonifield
3:05 PM UTC
Samsung’s flagship laptop is a MacBook Pro clone gone horribly wrong
Antonio G. Di Benedetto
3:00 PM UTC
Google’s taking a big swing at AI health with the Fitbit Air
Victoria Song
2:00 PM UTC
Advertiser Content From

This is the title for the native ad

## Top Stories

17 minutes ago
Mira Murati’s deposition pulled back the curtain on Sam Altman’s ouster
4:00 PM UTC
The future of Disney Plus is a confused mess
May 6
How David Sacks crashed and burned in the White House
4:00 PM UTC
Inside the return of Xbox
33 minutes ago
Apple’s AirPods with cameras for AI are apparently close to production
11 minutes ago
One of America’s best-selling cars is going electric.