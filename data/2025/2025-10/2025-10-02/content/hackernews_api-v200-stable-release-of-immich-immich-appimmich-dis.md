---
title: 'v2.0.0 - Stable Release of Immich · immich-app/immich · Discussion #22546 · GitHub'
url: https://github.com/immich-app/immich/discussions/22546
site_name: hackernews_api
fetched_at: '2025-10-02T19:07:46.845459'
original_url: https://github.com/immich-app/immich/discussions/22546
author: Alexvb
date: '2025-10-02'
description: v2.0.0 - Stable Release of Immich
tags:
- hackernews
- trending
---

immich-app



/

immich

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork4.1k
* Star78.8k

# v2.0.0 - Stable Release of Immich#22546

 alextran1502



 announced in

Announcements

 v2.0.0 - Stable Release of Immich


#22546

 alextran1502


Oct 1, 2025

·

 133 comments

·

 36 replies


Return to top



Discussion options



Quote reply



edited by jrasm91

## alextran1502Oct 1, 2025Maintainer



-

# v2.0.0 - Stable Release of Immich

Watch the video

## Welcome

Hello everyone,

After:

* ~1,337 days,
* 271 releases,
* 78,000 stars on GitHub,
* 1,558 contributors,
* 31,500 members on Discord,
* 36,000 members on Reddit,
* 68 languages on Weblate,
* Surviving the controversial announcement about joining FUTO,
* Having overwhelming success and support from the community with the product keys model,
* Launching the Merch store,
* Attending our first FOSDEM,
* ...andbeforethe release of GTA VI

We are thrilled to announce thestable release of Immich!🎉

This has been a journey long in the making. So much has changed since the first commit on the project, all the way back in February, 2022. The project and team continue to grow, and today we’re proud to announcev2.0.0, our stable release. Stable signifies that we have now resolved a significant amount of technical debt. It also means we will be prioritizing compatibility and less effort will be required to keep Immich up-to-date. Finally, it means that the warning banner on the website has been removed! Along with this, we’re happy to announce a new version of thehttps://immich.app/website.

For more specifics about the stable release, see ourFAQsbelow.

## Merch and DVD

To celebrate this release, we want to capture this moment in a nostalgic form, reminiscent of how software was distributed in our childhood - on a CD (or DVD, in this “case”). Introducing Immich Stable in physical form! You can find the link to the diskhere

The disk comes with a fully bootable Immich instance, featuring a selection of curated photos chosen by the team. You can purchase the disk from our merch store, along with a client or server product key, to support and celebrate this milestone with us.

The merch store is also updated with retro-styled Immich designs, check it out inhttps://immich.store

## Future plans

Now that Immich is stable, here are some of the things that we will be focusing on:

* Roadmap— There are still a few items on our roadmap that we want to complete before the year ends such as auto-stacking, and achieving feature parity between the web and mobile app. We also have plans to start work on improved stack support, better sharing, group management, and ownership improvements, as well as many other enhancements.
* Usage data— The team wants to understand how the software is used, so that we can make better, informed decisions as we design and build Immich. We want to collect that information in a non-invasive and transparent way. We plan to discuss it with the community and gather feedback from everyone to come up with the best solution.
* Backup services— We aim to introduce additional paid services (not paywalled features, as we will never implement paywalled features), which will help support the project and that enhance self-hosting, making it easier and more reliable. First among the many services already planned is an end-to-end encrypted, off-site backup and restore feature, built directly into Immich. This will enable a buddy backup feature as well.

## Thank you

We cannot thank you enough for the support over the past three years. Community participation, from the first comments on theoriginal reddit post, to the feedback when we joined FUTO, have contributed to the awesome product Immich is today. Thank you for joining us and believing in our mission to regain control over your most precious data. Here’s to many more years!

We'll also be hosting a Q&A livestream tomorrow,October 2nd, 2025 at 6 PM UTC. You can submit your questionshereand subscribe for notifications when the livestream startshere.

Cheers,

The Immich Team

# FAQs

## Will there be a live stream?

Yes. We'll be hosting a Q&A livestream tomorrow,October 2nd, 2025 at 6 PM UTC. You can submit your questionshereand subscribe for notifications when the livestream startshere.

## Do I still need backups?

Yes! A 3-2-1 backup strategy is still crucial. The team has the responsibility to ensure that the application doesn’t cause loss of your precious memories; however, we cannot guarantee that hard drives will not fail, or an electrical event causes unexpected shutdown of your server/system, leading to data loss. Therefore, we still encourage users to follow best practices when safeguarding their data. Keep multiple copies of your most precious data: at least two local copies and one copy offsite in cold storage. Additionally, we are starting to work on a cloud backup service to make backups easier.

## When willv2.0.0be available?

The Docker images forv2.0.0will be pushed out a few hours after this post is released.

## How can I update tov2.0.0?

You can follow the upgrade documentation,here.

## What versioning strategy will Immich use?

Starting withv2.0.0, we will now followsemantic versioning.

## What mobile app versions will work withv2.0.0?

Anyv2.x.xversion of the mobile app will work with any2.x.xversion of the server. For example, a mobile app on versionv2.9.0will continue to work with server versions:v2.0.0,v2.1.0,v2.3.1, etc.

## Will new features continue to be released?

Yes. Immich will continue to build, develop, and release new features.

BetaWas this translation helpful?Give feedback.



320


You must be logged in to vote


👍

404



😄

86



🎉

525



❤️

410



🚀

232



👀

30





All reactions

## Replies:133 comments·36 replies



Comment options



Quote reply



edited

### mirkohubtvOct 1, 2025



-

Huge congratulations to the Immich team! Excited to see v2.0.0 reach stable release — an amazing milestone for open-source and self-hosting

BetaWas this translation helpful?Give feedback.



39


You must be logged in to vote


🎉

17





All reactions

 0 replies




Comment options



Quote reply

### felinusfishOct 1, 2025



-

congratulations to the team at Immich (and by extension, FUTO)!! a well deserved victory for the open source community!!

BetaWas this translation helpful?Give feedback.



20


You must be logged in to vote


🎉

6





All reactions

 0 replies




Comment options



Quote reply

### SomeRandomCpuOct 1, 2025



-

Is the performance better than previous versions, because it used to be a resource hog

BetaWas this translation helpful?Give feedback.



5


You must be logged in to vote


👎

41



😕

2





All reactions

 2 replies




Comment options



Quote reply

#### schuhbaccaOct 1, 2025Collaborator



-

Which part? Ingesting large batches of photos can be very intensive, but day-to-day it's pretty minimal.

BetaWas this translation helpful?Give feedback.


👍

13





All reactions



Comment options



Quote reply

#### coltenkrauterOct 1, 2025



-

Just so you know, this thread is a celebratory milestone. 😉 🥳

Performance has improved a lot compared to early versions. The team has been cutting down memory use with theSync v2 overhaul, optimizingthumbnail pipelines and scalability, and fixing long-standingresource issues.

Recent releases also highlight this:

* v1.133.0introducedVectorChord(replacingpgvecto.rs), described as faster, more stable, and using less RAM. It also improved the web timeline and fixed thumbnail caching issues on mobile.
* v1.132.0removed TypeORM on the server side and moved to a new schema tool + SQLite on mobile, reducing startup lag and improving performance on large libraries.
* v1.143.0enabledconcurrent hashingon mobile for higher throughput and reduced bottlenecks. It also fixed a SQLite concurrency crash that caused freezes.
* Ya,there is more...

I run it on my own server and I have no complaints... It’s fast, responsive, and seemingly efficient.

BetaWas this translation helpful?Give feedback.


👍

29





All reactions



Comment options



Quote reply

### chadneuOct 1, 2025



-

About time. It's been so long without an update that I thought immich was abandoned.

(im not serious)

BetaWas this translation helpful?Give feedback.



20


You must be logged in to vote


👍

2



😄

28





All reactions

 0 replies




Comment options



Quote reply

### TASelwynOct 1, 2025



-

Stable 🥳

BetaWas this translation helpful?Give feedback.



5


You must be logged in to vote


🎉

3





All reactions

 0 replies




Comment options



Quote reply

### simonbuehlerOct 1, 2025



-

this is the legit successor of the AOL CDRom

BetaWas this translation helpful?Give feedback.



10


You must be logged in to vote


😄

4





All reactions

 0 replies




Comment options



Quote reply

### kaysondOct 1, 2025



-

Are the warning messages on the docs supposed to go away too?

BetaWas this translation helpful?Give feedback.



5


You must be logged in to vote



All reactions

 2 replies




Comment options



Quote reply

#### JPar99Oct 1, 2025



-

No because its self hosted! Every self hosted project comes with warnings

BetaWas this translation helpful?Give feedback.


👎

28





All reactions



Comment options



Quote reply

#### ireunOct 1, 2025



-

Select at 'next' not 'latest' in the dropdown at top, it'll be gone ;)

BetaWas this translation helpful?Give feedback.


🎉

9





All reactions



Comment options



Quote reply

### Wh1rrOct 1, 2025



-

Congrats!!!🥳

BetaWas this translation helpful?Give feedback.



4


You must be logged in to vote


🎉

1





All reactions

 0 replies




Comment options



Quote reply

### hitech95Oct 1, 2025



-

Since last few updates (1.14X) the app get stuck when opening I have to force close it and open it again.

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote


👎

5





All reactions

 1 reply




Comment options



Quote reply



edited

#### schuhbaccaOct 1, 2025Collaborator



-

Please make a help support thread in the discord 🙂

BetaWas this translation helpful?Give feedback.



All reactions



Comment options



Quote reply

### RestartBOct 1, 2025



-

Nice - congrats! 🥳🎉

BetaWas this translation helpful?Give feedback.



4


You must be logged in to vote


🎉

2





All reactions

 0 replies




Comment options



Quote reply

### wispdevonOct 1, 2025



-

Amazing news!!!

BetaWas this translation helpful?Give feedback.



4


You must be logged in to vote


🎉

2





All reactions

 0 replies




Comment options



Quote reply

### JPar99Oct 1, 2025



-

Congrats guys! What an achievement!

BetaWas this translation helpful?Give feedback.



4


You must be logged in to vote


🎉

2





All reactions

 0 replies




Comment options



Quote reply

### trevordavies095Oct 1, 2025



-

This is great news!! Congrats to everyone

BetaWas this translation helpful?Give feedback.



3


You must be logged in to vote


🎉

1





All reactions

 0 replies




Comment options



Quote reply

### tantalusblankOct 1, 2025



-

Congrats to the team! 🎉🎉 Been eagerly awaiting this one

BetaWas this translation helpful?Give feedback.



4


You must be logged in to vote


🎉

1





All reactions

 0 replies




Comment options



Quote reply

### sr20kschmitzOct 1, 2025



-

Congrats!

BetaWas this translation helpful?Give feedback.



3


You must be logged in to vote



All reactions

 0 replies


 103 hidden items


 Load more…




Comment options



Quote reply

### AFumi39Oct 2, 2025



-

Great!!!Finally, the first stable version!!! 🎉Thank you for all the hard work! 🎊

There're just 3 little things that I think should be mandatory for a stable version of Immich:

* Image rotation on web: a really basic web image editor that let you change the orientation of the image should be present
* Auto include new albums on Android: as now, Android app let you select all the local albums to sync, and that's good. Bu if you add a new local album, you have to open Immich App, go to the backup settings and select the new albums to be synced. That's not good, a flag that automatically include every new album that is created, is a thing that can't be missed
* Default TZ: as now, the TZ for the images is present only if the "DateTaken" EXIF tag is present, or if the GPS coordinates are present. So all the WhatsApp (for example) images are stored with UTC time. A default TZ per user (or per server) should be used if "DateTaken" and "GPS" EXIF tags are missing

I think that with these 3 things the release can really be considered a stable version 😊

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote


👎

1





All reactions

 1 reply




Comment options



Quote reply

#### coltenkrauterOct 2, 2025



-

Great!!! Finally, the first stable version!!! 🎉 Thank you for all the hard work! 🎊

There're just 3 little things that I think should be mandatory for a stable version of Immich:

* Image rotation on web: a really basic web image editor that let you change the orientation of the image should be present

* Auto include new albums on Android: as now, Android app let you select all the local albums to sync, and that's good. Bu if you add a new local album, you have to open Immich App, go to the backup settings and select the new albums to be synced. That's not good, a flag that automatically include every new album that is created, is a thing that can't be missed

* Default TZ: as now, the TZ for the images is present only if the "DateTaken" EXIF tag is present, or if the GPS coordinates are present. So all the WhatsApp (for example) images are stored with UTC time. A default TZ per user (or per server) should be used if "DateTaken" and "GPS" EXIF tags are missing

I think that with these 3 things the release can really be considered a stable version 😊

Glad you framed this in a positive tone. That said, a release announcement is hardly the place to add new stability requirements. If you’d like these ideas to get traction, I would suggest opening afeature request discussion.

BetaWas this translation helpful?Give feedback.



All reactions



Comment options



Quote reply

### DrSlump74Oct 2, 2025



-

Hi, great news, congratulations!I have a question about the update. My docker-compose has this database image:ghcr.io/immich-app/postgres:14-vectorchord0.3.0-pgvectors0.2.0While you recommend using this one:ghcr.io/immich-app/postgres:14-vectorchord0.4.3-pgvectors0.2.0Should I just follow your instructions without hesitation, or do I need to perform some other steps before modifying the database image?Thanks

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote



All reactions

 1 reply




Comment options



Quote reply

#### coltenkrauterOct 2, 2025



-

Hi@DrSlump74,

I am not a maintainer...

You should be totally fine upgrading without extra steps beyond the usual precautions (backup first). TheImmich docssay,

“Make sure the installed version of VectorChord is compatible with your version of Immich. The current accepted range for VectorChord is >= 0.3.0, < 0.5.0.”

Also: VectorChord is thesuccessor to pgvecto.rs(built by the same team) and maintains backward-compatible behavior in that version window. Because that change is “minor” (a version bump within the same major range), you shouldn’t see breakage from VectorChord itself.They followSemVer.

BetaWas this translation helpful?Give feedback.


👍

1





All reactions



Comment options



Quote reply

### thegabriele97Oct 2, 2025



-

Finally! Waiting now for editor and, most important at least for me,#165

BetaWas this translation helpful?Give feedback.



4


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### Altharion1Oct 2, 2025



-

Congratulations !! I've been using Immich for 2 months now and it already seemed very stable, so I didn't understand why it wasn't :)

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote


👍

1





All reactions

 0 replies




Comment options



Quote reply

### rommOct 2, 2025



-

Congratulations on this awesome milestone! 🥳

Can't wait to see what you'll bring in the future!

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote


👍

1





All reactions

 0 replies




Comment options



Quote reply

### kondi06Oct 2, 2025



-

Great, I hope there will finally be an option to disable albums from the timeline view, which will make the timeline contain only what is needed.

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote


👍

2





All reactions

 0 replies




Comment options



Quote reply



edited

### HELPY4Oct 2, 2025



-

OOOO LET'S GOOOO FOLKS

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote


👍

1





All reactions

 0 replies




Comment options



Quote reply

### aksdbOct 2, 2025



-

~1,337 days

Hehe. Nice.

Congrats and thanks for the ride so far! For an "unstable" product, it was quite well-working and flawless already.

BetaWas this translation helpful?Give feedback.



2


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### elkemperOct 2, 2025



-

Congrats 🎉Thanks for pointing out that in the future you want to gather telemetry, and will discuss this with the community. Please, emphasize this more in the nearest communications, so there will be less reddit posts "THeY StEAlInG oUr DaTa" and less pressure on the team

BetaWas this translation helpful?Give feedback.



2


You must be logged in to vote


😄

1





All reactions

 0 replies




Comment options



Quote reply

### neforceOct 2, 2025



-

Impressive. Previous versions was a bit buggy on mobile (lag, slow, heating up the device), but now, a breeze! 100k images, no issue!

BetaWas this translation helpful?Give feedback.



2


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### greenloglesOct 2, 2025



-

Thanks for the great project!

I like the idea of adding paid features , especially if your team can offer saas services.I'd love to see encrypted backup solutions to store another copy of my photos and videos elsewhere.

BetaWas this translation helpful?Give feedback.



2


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### jpwspeedOct 2, 2025



-

Congrats to the team!

As someone who has used Immich since late 2022 and has seen many projects spin up and die off in that time, I can't tell you how much I appreciate the work that has been put into the project.

Can't wait to see what the (stable) future holds!

BetaWas this translation helpful?Give feedback.



3


You must be logged in to vote


🎉

2





All reactions

 0 replies




Comment options



Quote reply

### Dawo9889Oct 2, 2025



-

Congrats for all of the team and also for other contributors!You've changed my life with helping me to secure my private data in my home

BetaWas this translation helpful?Give feedback.



2


You must be logged in to vote


🎉

2





All reactions

 0 replies




Comment options



Quote reply

### wall03Oct 2, 2025



-

ironically waiting until v2.0.1 for them to iron out the bugs. May just be me being used to the unstable versions! Good job guys

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote


😄

1





All reactions

 3 replies




Comment options



Quote reply

#### coltenkrauterOct 2, 2025



-

Haha, yep, waiting for the first patch release is a safe bet with basically all software.

BetaWas this translation helpful?Give feedback.



All reactions



Comment options



Quote reply

#### athornfam2Oct 2, 2025



-

Yeah, I actually just updated from 1.42.1 to 1.44.1 myself. Waiting until the initial bugs get cooked.

BetaWas this translation helpful?Give feedback.



All reactions



Comment options



Quote reply

#### bo0tzzOct 2, 2025Maintainer



-

There's no point in waiting, 1.144.1 -> 2.0.0 had basically no changes and so won't have introduced any new bugs to be fixed in a patch release.

BetaWas this translation helpful?Give feedback.



All reactions



Comment options



Quote reply

### rodneyosodoOct 2, 2025



-

Congrats to the Immich team on the stable release 🎉Can’t believe I hung in there for this long — totally worth it 🙌

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote



All reactions

 0 replies


Sign up for free

to join this conversation on GitHub
.
 Already have an account?

Sign in to comment
