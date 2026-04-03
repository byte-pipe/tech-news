---
title: postmarketOS // FOSDEM 2026 + Hackathon
url: https://postmarketos.org/blog/2026/02/10/fosdem-and-hackathon/
site_name: lobsters
content_file: lobsters-postmarketos-fosdem-2026-hackathon
fetched_at: '2026-02-12T06:00:27.451211'
original_url: https://postmarketos.org/blog/2026/02/10/fosdem-and-hackathon/
date: '2026-02-12'
description: Aiming for a 10 year life-cycle for smartphones
tags: event, linux, mobile
---

# FOSDEM 2026 + Hackathon

February 10, 2026
13 min. read

Another FOSDEM and Hackathon are in the rear-view mirror, and it is hard to find words to describe how amazingly productive and fun the experience was! We met so many people at the postmarketOS stand, in the FOSS on Mobile devroom and at dinners in the evening. As always it is fun to put faces to nicknames and to talk about the Linux Mobile ecosystem, and figure out how to improve it in person.

## FOSDEM 2026

* Stand:Besides a good selection of phones (+ external screen) and stickers, version v0.3 of ourphone-harnessPCB hadarrivedjust in time to show it at the stand this year and people were quite excited about it! This year we also had proper phone stands for the first time, as well asshirts(we gave 26 of them away to people who donated), namecards, and a QR code that goes to the donation page. There were too many great interactions to recount here, but to quote just one fromMat'sfedi post:"Most memorable #FOSDEM moment for me has to be at the #postmarketOS booth, where I asked for help updating my phone, handed it over and ended up withBhushanalmost(I think) getting the mic working on it. Had to leave to catch a talk, but hey I did get my phone updated 😄️"

Luca,Bart,HugoandAelinare ready for curious FOSDEM visitors after preparing the stand together withFederico.

The other side of the stand, where one can see the PCB that the phone on the right was connected to. Federico, who created it together withNicola, was there in person and happily talked to the many people interested in our hardware CI setup.

* Talks:TheFOSS on Mobile devroomhad far better ventilation than last year, and was pretty much full all the time. We had plenty of postmarketOS related talks, and recordings for all of them are available:postmarketOS: Reliability in 2026byOliverMainline kernel for Fairphones - 2026 updateby LucaPhosh: What's new and where are we going?byEvangelosSnapdragon 8 Gen 3 Mainline: From Day-1 Patches to Product RealitybyNeilRunning mainline Linux on the Unisoc-based Jolla C2byAffeThe Linux Phone App Ecosystem (2026)byPeterPhotos and Video Recording on Mobile PhonesbyPavel M.UnifiedPush - Push notifications. Decentralized and Open SourcebyDaniel G.andS1mCollabora Office Can Finally Run on Mobile LinuxbySkyler
* postmarketOS: Reliability in 2026byOliver
* Mainline kernel for Fairphones - 2026 updateby Luca
* Phosh: What's new and where are we going?byEvangelos
* Snapdragon 8 Gen 3 Mainline: From Day-1 Patches to Product RealitybyNeil
* Running mainline Linux on the Unisoc-based Jolla C2byAffe
* The Linux Phone App Ecosystem (2026)byPeter
* Photos and Video Recording on Mobile PhonesbyPavel M.
* UnifiedPush - Push notifications. Decentralized and Open SourcebyDaniel G.andS1m
* Collabora Office Can Finally Run on Mobile LinuxbySkyler

Evangelos presents"Phosh: What's new and where are we going?"

* Podcast:On Sunday we did the traditional podcast recording, this time on the parking lot where we found several tables and benches next to each other, and with several special guests from other projects. Editing will take a bit, consider adding thepostmarketOS podcastto your player if you haven't already.

## Hackathon

For the hackathon we had two floors. The top floor was mostly just beds, the one below had one living room that we used for discussions and hacking during the day. This room featured a TV (that quickly had HDMI cables hanging out for plugging devices), a table in front of that, and around it a ring of comfortable chairs and two somewhat broken but still comfortable couches. On the other side we had a bigger table that was used for parallel sessions as well as having dinner.

Lunch break on Monday at the Hackathon. The schedule in the background is not planned out for Tuesday and Wednesday yet.

On Monday after FOSDEM, we began making the schedule with a stack of post-its. We quickly found that behind the TV actually was a good spot to put them, wrote the three days on the X axis and timeslots on the Y axis and assigned initial topics for day 1 and some on the side to be used later. Each session was planned for one hour, in total we got 8 slots each day, some with two sessions in parallel, plus time for lunch. We were able to mostly stick to the time schedule (even better than previous years), usually trying about ~40 min into the session to figure out if we can conclude it or how, or make another part of the same session.

The final schedule at the end of Wednesday.

In the evening we had a fun activity each day, and we used additional time around the planned schedule mostly for additional discussions around postmarketOS, and improving things.

### Monday

* Reliability:in total we talked three hours about the new requirements for themaincategory (PMCR 0009). It will include hardware CI, and it became apparent that we do not only want to have the new main category indicate that a specific feature set is working, but also that the postmarketOS teamendorsesdevices that made it in this category and will try to keep them there for quite some time. This means the hurdles to getting a device in main will be high, and we will need a team of people for each device in main to ensure we can keep it there. The PMCR will be reworked based on these discussions soon and we will present a plan to get the first reference devices into main based on these discussions.
* AI policy:our currentAI policydoes not state that we forbid the use of generative AI in postmarketOS, so far this document just lists why we think it is a bad idea and misaligned with the project values. We discussed this and will soon change it (via merge request) to clearly state that we don't want generative AI to be used in the project. It was also noted that currently the policy is too long, it would make sense to split it into the actual policy and still keep, but separate the reasoning from it.
* HW-CI PCB workshop:Federico did a wonderful job explaining how thePCBhe designed with Nicola works. Afterwards we spent a lot of time getting CI-tron running and hooking up devices to the PCB.

Federico presented the functionality of the HW-CI PCB and the journey to get there so well that we recommended he does a standalone talk on this topic at a conference.

* Financial review & budget approval:we have approved a new budget. There will be a separate blog post about this, similar tolast year.
* Security:in parallel,Ariadnefrom Alpine Linux presented how the vulnerability monitoring works in Alpine (seesecurity.alpinelinux.org, knowing exactly which vulnerabilities are open is essential for fixing them quickly!) and we discussed how postmarketOS could join this effort in the future.
* PipeWire for audio:various discussions to move theSwitch to PipeWiremilestone forward.

For hackathon movie night we followed the theme of movies with UI names, previously "The Gnome-Mobile" (1967) and "For the Plasma" (2014), and this time "COSMIC Journey" (1936 !!!). Find our reviews of the movie onfedi.

### Tuesday

* Push notification blockers:the author of this blog post was in the parallel session, but looked over to Bhushan et al. several times who appeared to be quite busy with unblocking these blockers.
* Legal entity:Pablopresented#1and the research that went into this topic since, and that he andRobare looking into an AISBL with an e.V. as backup plan. We discussed the topic and concluded that this makes sense, and that they should proceed.
* Power delegation and teams: in over two hours we discussed how to move forward withPMCR 0008to organize ourselves better, and how it fits with soon having a legal entity. We figured that we need to rename"The Board"(which is currently for financial oversight) to"Financial Team", as we will soon have a new board for the legal entity. In the end our idea was to have the new board refer to an "assembly" for all important decisions, and this "assembly" would just be all Trusted Contributors in postmarketOS. The Core Contributors team would be dissolved in favor of having several topic-specific teams (a lot of which we already have, such as the infra team). This way we would have a very flat decision structure. The PMCR will be updated soon and discussed further there.Caseyalso askedon fedifor further feedback and got a lot of input.
* FP5 Call Audio:Bhushan and Luca worked on getting speaker audio in calls with the Fairphone 5. This feature was not working yet, and a good target since recently speaker audio was recently brought up for this device. They were successful and made ashort video illustrating the featuretogether with Bart and Oliver, under whichAchillcommented"such a banger video, of course was without scripting and 5 retries".

Bhushan gets a mysteryious call.We totally didn't record this in the kitchen next to the living room, as that wouldn't have made sense for the plot in the video.

* BPO redesign:we discussed finding a successor tobuild.postmarketos.org, our packages and images building service. Find the results of this discussion in#157.
* Patch for upstream review service:Henrikhad the idea of offering a service for pre-reviewing patches from the postmarketOS community before they get sent to the kernel mailing list to help with fixing some common mistakes, given that the kernel ML is not intuitive for newcomers. We concluded the discussion with that it makes sense to just use a sourcehut list for test-sending mails, doing actual reviewing upstream on the ML, and to update thesubmitting patchesguide to be more step-by-step (all still TBD).
* Alpine TSC process:we looked into"Define election/appointment of TSC & Council"(#698) and will present Alpine a proposal to move this forward.
* Installer / first boot setup:we discussed#5, and most importantly concluded that we don't want to do the first boot setup in the initramfs but rather in the UI. This is already possible by plasma-setup and similar first-boot programs in most UIs. Most importantly, a step to re-encrypt LUKS volumes is missing in these first boot UIs, and we want to add it there. With this, we will be able to have encrypted images, for which the password and encryption key are changed on first boot, and the device gets re-encrypted with the new encryption key right after. See also#4076.
* Requiring DCO:we discussed whether we want to require contributors to sign off on theDeveloper Certificate of Originfor their contributions and decided to require this for all projects except pmaports (unclear license with aports right now) in the near future. We will probably write a separate blog post about this.
* (More hw-ci and reliability sessions, see Monday)

As fun evening activity,Clayton, Bart and Oliver went to a local bouldering gym. We were surprised to see how many are in the area and had some good fun there.

### Wednesday

* Dogfooding reboot:Federico is daily driving a Pixel 3a, and asked all others at the hackathon to consider using postmarketOS on their phones more, not just on laptops. He convinced some to do this, we discussed the topic quite a lot, and will likely make a blog post about this afterwards.
* pmOS + OEMs/ resellers:we discussed reaching out to OEMs/resellers for selling phones with postmarketOS pre-installed. We currently have such a relationship in place withSendero Linuxand discussed that this is a good, small scope for now (compared to e.g. PINE64), and will allow us to have more experience when we will likely want to do something like this on a bigger scale, more geared towards end-users instead of enthusiast-only as it is the case now, etc. We don't want to reach out to more vendors right now.
* HW-CI + Documentation with Martin:we had a video call withMartin R.from CI-tron, who showed us how to bring up new CI-tron hosts among other things. Afterwards we discussed where to put the documentation, and decided to put anoverview in docs.postmarketos.organd in-depth docs in pmaports (!7881) and thephone-harnessrepository (docs.postmarketos.org/phone-harness). The plan is, that everything is accessible through the docs.postmarketos.org website, no matter the repository location (as we already have it for some other repos).

Pablo got Casey's original OP6T with the PCB and a local CI-tron instance running on a Raspberry Pi connected to our GitLab. The CI job shows the kernel logs while the device is booting.Watch the full video here.

* The future of events (stands, hackathon) and retrospective:this was a session from Luca about what worked for the stands and hackathons and what could be improved.
* Package repo consistency:Casey had the idea to make snapshots of Alpine's repositories whenmainandcommunityare consistent, so we can always build consistent installs on top of that, and so we can easily go back in time and bisect issues with previous packages. We had another short meeting about this since the hackathon and created#136to follow up. Get in touch there if this interests you!
* Async decision making:brainstorming on how we can make decisions between team meetings instead of making them in the team meetings. This has the advantage that TCs who can't attend the meetings due to timezone differences could be more involved in decisions.
* pmbootstrap:We discussed whether to move forward with!2523(yes) and later discussed some bigger ideas that we had started but were not finished, such as not requiring sudo to run pmbootstrap. Given that we have several of them and integrating them into the current code base is very hard as they change so much, we considered making a design document for writing a new pmbootstrap-like toolfrom scratchthat has all these improvements, lists what features to keep and remove, has proper abstraction layers, library first and a CLI interface around that. The pmbootstrap maintainers will work on this spec until they like it, and if it makes sense, would start work on such a new tool. So the next step here is drafting such a spec and posting it publicly.
* (More on power delegation, see Tuesday)
* Podcast:given that we now have two (!) new podcast editors who don't have any other responsibilities in postmarketOS, we decided to record another podcast towards the end of the hackathon :>

### Other

* Outside of the above sessions, Federico, Aelin, Casey, and Pablo put a lot of work in to the hardware CI. As a result, we were able to test the firmware that Martin R. had written in more scenarios, which in turn lead to uncovering multiple bugs that were then fixed. We also made some modifications to make it work with devices with other voltages. In the end, we were able to get a gateway working withtwophone harnesses and devices connected, a OnePlus 6T and Casey'soriginal OnePlus 6, which worked like charm.

Cooking and shopping for so many people is a challenge. Thanks to Luca and Federico who cooked delicious meals once again that kept all hackers going!

### Thank you

Having this hackathon was only possible thanks toyourdonations! Just like last year, it was incredibly productive to have everybody in the same place, for planning, discussing goals and for just getting things done quickly without delay.

If you appreciate the work we're doing with postmarketOS and want to support us,consider contributing financially via OpenCollective.

 This blog post was written by Oliver. Header image by Federico.
