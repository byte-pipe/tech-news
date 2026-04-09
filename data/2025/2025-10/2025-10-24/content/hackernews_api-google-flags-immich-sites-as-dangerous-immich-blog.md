---
title: Google flags Immich sites as dangerous | Immich Blog
url: https://immich.app/blog/google-flags-immich-as-dangerous
site_name: hackernews_api
fetched_at: '2025-10-24T11:33:04.588762'
original_url: https://immich.app/blog/google-flags-immich-as-dangerous
author: janpio
date: '2025-10-22'
description: How Google actively breaks Immich deployments, an open-source Google Photos alternative
tags:
- hackernews
- trending
---

* Blog
* Google flags Immich sites as dangerous


# Google flags Immich sites as dangerous



October 20, 2025



— Jason Rasmussen



Earlier this month all of our*.immich.cloudwebsites were marked as dangerous and users started being shown the dreaded "red-screen-of-death" page.




No one on the team really understood how this browser feature worked, but it's now, unfortunately, been added to our list ofCursed Knowledge.



## Background



Google offers a service calledSafe Browsing, which aims to determine if a site is running malware, unwanted software, or performs some form of social engineering. The service is free, and many browsers, including Chrome & Firefox, directly integrate the service into their products, although it is still a bit unclear how itactuallydetermines if something is "dangerous".



So, what happens if your site is marked as dangerous? Well, since most browsers seem to use this service, your site essentially becomes unavailable for all users, except the few that might realize it's a false positive, click theDetailsbutton, and then see and click the tiny, underlined "visit this safe site" link. So basically it becomes unavailable for your entire audience with little apparent recourse.



## Being flagged



At some point earlier this month, we realized that a bunch of sites on theimmich.clouddomain had recently started showing up as "dangerous". At the same time, a few users started complaining about their own Immich deployments being flagged. We also noticed that all our own internal sites had the same warning, including our preview environments. It got oldreal fastto have to go through the tedious effort to "view this safe site" whenever we wanted to view anything.



## Search Console



After a few days we realized this warning was not going to go away on its own, and that theGoogle Search Consolewas apparently the official way to manage these types of issues. It seems a bit crazy that the only way to make our site available again was to create a Google account, and use the Google Search Console to request a review of the affected site. The service did at least provide a few more details aboutwhat exactlywas flagged, although it made the whole thing a bit more comical. Per the service:



Google has detected harmful content on some of your site’s pages. We recommend that you remove it as soon as possible. Until then, browsers such as Google Chrome will display a warning when users visit or download certain files from your site.



and



These pages attempt to trick users into doing something dangerous, such as installing unwanted software or revealing personal information.



Below these warnings was a list of affected URLs:






https://main.preview.internal.immich.cloud/
https://main.preview.internal.immich.cloud/auth/login
https://pr-22838.preview.internal.immich.cloud/
https://pr-22838.preview.internal.immich.cloud/auth/login
...


It was super useful to learn that the affected URLs were for ourpreview environments. Maybe the thought was that these Immich environments were imitating ourdemo website? The most alarming thing was realizing that a single flagged subdomain would apparently invalidate theentire domain.



## Impact



This issue affects all of our preview environments and other internal services such as zitadel, outline, grafana, victoria metrics, etc. This also impacts our production tile server, which is deployed attiles.immich.cloud. Luckily, the requests to the tile server are made via JavaScript, and since those are not user facing they seem to still be working as expected.



## "Fixing" the issue



The Google Search Console has aRequest Reviewbutton, where you can explain how you have resolved the issues. It does warn that:



Requesting a review of issues that weren't fixed will result in longer review cycles






Since, nothing isactuallywrong we decided to respond with the following:



Immich is a self-hosted application, and the Immich team (https://immich.app/) owns and operates theimmich.clouddomain and subdomains. The flagged sites are our own deployments of our own products and are not impersonating anything or anyone else.



A day or two later, the resolution was accepted and the domain was clean again! 🎉



Wethoughtwe were home free, but unfortunately that was not the case.



## Minimizing the issue



An Immich preview environment can be requested by adding thepreviewlabel to a pull request on GitHub. When the environment is created, a comment is posted on the pull request with the preview url, which follows the following format:






https://pr-<num>.preview.internal.immich.cloud/


As soon as we created a new preview environment, theimmich.clouddomain wasonce againflagged as a dangerous site. The best we can tell, Google crawls GitHub, sees the new URL, crawls the site, marks it as deceptive, and the whole process begins anew.



Our current plan is to attempt to minimize the impact of this issue by moving the preview environments to their own, dedicated domain —immich.build.



## A wider issue



Google Safe Browsing looks to be have been built without consideration for open-source or self-hosted software. Many popular projects have run into similar issues, such as:


* Jellyfin
* YunoHost
* n8n
* NextCloud
* other Immich deployments
* etc.


Unfortunately, Google seems to have the ability to arbitrarily flag any domain and make it immediately unaccessible to users. I'm not sure what, if anything, can be done when this happens, except constantly request another review from the all mighty Google.



Cheers,The Immich Team




Download



Android



iOS



Server



Company



FUTO



Purchase



Merch



Sites



Documentation



My Immich



Immich API



Miscellaneous



Roadmap



Cursed Knowledge



Privacy Policy
