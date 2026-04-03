---
title: Man accidentally gains control of 7,000 robot vacuums | Popular Science
url: https://www.popsci.com/technology/robot-vacuum-army/
site_name: hackernews_api
content_file: hackernews_api-man-accidentally-gains-control-of-7000-robot-vacuu
fetched_at: '2026-02-23T11:19:51.264471'
original_url: https://www.popsci.com/technology/robot-vacuum-army/
author: Mack DeGeurin
date: '2026-02-22'
description: Sammy Azdoufal just wanted to steer his DJI Romo with a gaming controller.
tags:
- hackernews
- trending
---

A robot vacuum army is less cute and potentially more dangerous.

									 

Image: Getty Images



## Get the Popular Science daily newsletter💡



Breakthroughs, discoveries, and DIY tips sent six days a week.

Email address

 Sign up

Thank you!





Terms of ServiceandPrivacy Policy.

A software engineer’s earnest effort to steer his new DJIrobot vacuumwith a video game controller inadvertently granted him a sneak peak into thousands of people’s homes.

While building his own remote-control app, Sammy Azdoufal reportedly used an AI coding assistant to help reverse-engineer how the robot communicated with DJI’s remote cloud servers. But he soon discovered that the same credentials that allowed him to see and control his own device also provided access to live camera feeds, microphone audio, maps, and status data from nearly 7,000 other vacuums across 24 countries. The backend security bug effectively exposed an army of internet-connected robots that, in the wrong hands, could have turned into surveillance tools, all without their owners ever knowing.

The DJI Romo.
Image: DJI


Luckily, Azdoufal chose not to exploit that. Instead, heshared his findings with The Verge, which quickly contacted DJI to report the flaw. While DJI tellsPopular Sciencethe issue has been “resolved,” the dramatic episode underscores warnings from cybersecurity experts who have long-warned that internet-connected robots and other smart home devicespresent attractive targets for hackers.

As more households adopt home robots, (including newer,more interactive humanoid models) similar vulnerabilities could become harder to detect. AI-powered coding tools, which make it easier for people with less technical knowledge to exploit software flaws, potentially risk amplifying those worries even further.

I can confirm that@DJIGlobalhas finally fixed the HUGE vulnerability they had on their servers.This vulnerability was discovered by the very skillful@n0tsa, and he reported it to DJI.It allowed to take remote control (movements, microphone, camera) of over 10 000 robots…pic.twitter.com/j1UunMmNXX

— Gonzague 👨🏼‍💻 (@gonzague)
February 11, 2026

## Stumbling into a massive security hole

The robot in question is theDJI Romo, an autonomous home vacuum that first launched in China last year and is currently expanding to other countries. It retails for around $2,000 and is roughly the size of a large terrier or a small fridge when docked at its base station. Like other robot vacuums, it’s equipped with a range of sensors that help it navigate its surroundings and detect obstacles. Users can schedule and control it via an app, but it is designed to spend most of its time cleaning and mopping autonomously.

In order for the Romo, or really any modern autonomous vacuum, to function it needs to constantly collect visual data from the building it is operating in. It also needs to understand specific details about what makes, say, a kitchen different from a bedroom, so it can distinguish between the two. Some of that sensor data is stored remotely on DJI’s servers rather than on the device itself. For Azdoufal’s DIY controller idea to work, he would need a way for his app to communicate with DJI’s servers and extract a security token that proves he is the owner of the robot.

Rather than just verifying a single token, the servers granted access for a small army of robots, essentially treating him as their respective owner. That slip-up meant Azdoufal could tap into their real-time camera feeds and activate their microphones. He also claims he could compile 2D floor plans of the homes the robots were operating in. A quick look at the robots’ IP addresses also revealed their approximate locations. None of this, Azdoufal insists, amounts to “hacking” on his part. He simply stumbled upon a major security issue.

“DJI identified a vulnerability affecting DJI Home through internal review in late January and initiated remediation immediately,” DJI toldPopular Science.“The issue was addressed through two updates, with an initial patch deployed on February 8 and a follow-up update completed on February 10. The fix was deployed automatically, and no user action is required.”

The company went on to say its plans to “continue to implement additional security enhancements” but did not specify what those may entail.

Related: [The best robot vacuums]

## Home owners are grappling with the privacy cost of smart homes

The DJI security concerns come amid a period of growing unease generally about the surveillance capabilities of smart home technology. Earlier this month, Ring camera ownersflooded social mediaafter acontroversial advertisementfor the company’s pet-finding “search party” feature was interpreted by some as a Trojan horse for broader monitoring. Around the same time, reports that Google was able toretrieve video footage from a Nest Doorbell camerato assist in an abduction investigation (despite earlier indications that the footage had been deleted) reignited debate over how much control consumers truly have over their sensitive data.

On top of that, lawmakers from both political parties in the US have spent years warning that DJI and otherChinese tech manufacturers pose a unique security threat. The evidence for those claims are murky, it’s nonetheless helpedjustify the banning of certain Chinese-made products.

The irony of many robot vacuums and other smart home devices is that, as a category, they have a long history of questionable security practices, despite the fact that they operate in some of our most private spaces. All signs suggest that the average person will soon welcome more cameras and microphones into their homes, not fewer. As of 2020, market research firm Parks Associatesestimatesthat 54 million U.S. households had at least one smart home device installed. Othersurveysshow that those who already have one often want more.

The specific types of devices entering homes are also becoming more sophisticated. Though still early,Tesla,Figure, and other companies are racing to build human-like autonomous robots that canlive in a home and perform chores. A company called 1X is already retailing one of these humanoids, claiming it canclean dishes and crack walnuts—albeit often with some help from a human. Eventually though, for any of these at-home robot servants to function effectively, they will need unprecedented access to the intimate details of their owners’ homes. For a stalker or hacker, that represents a potential goldmine.

True to his word though, Azdoufal found himself wrapped up in this mess even though all he wanted to do was drive his robot around with a joystick. On that front,mission accomplished.

				Controlling DJI Romo vacuum with a ps5 controller

 



### 2025 PopSci Best of What’s New

The 50 most important innovations of the year

	See it
