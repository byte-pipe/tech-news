---
title: 'v3.0.0 · immich-app/immich · Discussion #29439 · GitHub'
url: https://github.com/immich-app/immich/discussions/29439
site_name: hnrss
content_file: hnrss-v300-immich-appimmich-discussion-29439-github
fetched_at: '2026-07-03T11:50:09.872345'
original_url: https://github.com/immich-app/immich/discussions/29439
date: '2026-07-02'
description: v3.0.0
tags:
- hackernews
- hnrss
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 immich-app

 

/

immich

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork6k
* Star105k

# v3.0.0#29439

 alextran1502
 

 
 announced in
 
Announcements

 v3.0.0
 

#29439

 alextran1502
 

Jul 2, 2026

·

 19 comments
 
·

 23 replies
 

Return to top

 

Discussion options

 

Quote reply

 

edited

## alextran1502Jul 2, 2026Maintainer

 

-

# v3.0.0

Welcome to Immichv3.0.0!

After months of hard work from the team and our amazing contributors, we're thrilled to announce the next major version of Immich:v3.0.0! 🎉

## Breaking changes

This release includes several breaking changes; read the full migration guidehere.It's worth mentioning that many of the breaking changes are updates to API endpoints and affect onlythird-party toolsthat integrate with Immich's API. For the vast majority of users, updating works exactly as it always has.

## How to update

Warning

v3.0.0drops support for pgvecto.rs. If you run Immich beforev1.133.0and haven't done the migration step yet, see the migration guide here.https://docs.immich.app/install/upgrading/#migrating-to-vectorchord

First, update theIMMICH_VERSIONin your.envfile tov3:

-
 IMMICH_VERSION=v2

+
 IMMICH_VERSION=v3

Then run the usual update commands:

docker compose pull 
&&
 docker compose up -d

## Release candidates

If you missed it,v3.0.0was the first time we used release candidates, also known as prereleases. Release candidates are tested but not yet official releases of Immich, and they allow us to find and fix any outstanding bugs before a final release. If you would like to be notified about release candidates directly through Immich, you can change the release channel from "Stable" to "Release candidate" in theAdmin settings > Version checkoptions (here).

## New Merch

As part of this release, we're happy to announce we also have some new swag for you!

* Kids clothing: For those who are likely the reason for your Immich library's size
* Colored embroidery: We now have clothes with a full color embroidered Immich logo

Check it out now athttps://immich.store!

## Highlights

Now, let's get right into all the new features in this release:

* Mobile non-destructive editing
* Workflows (preview)
* Background backup improvement
* Recently added page
* Integrity checks
* Slideshow on mobile app
* HLS and real-time video transcoding (preview)
* New video player for web
* Open photo in Immich as gallery on Android
* OCR on mobile app
* Upload asset directly to album on the mobile app
* Option to select image size when sharing on the mobile app
* Timeline performance improvement for browsing a large amount of assets in a single month

### Mobile non-destructive editing

This is a follow-up to Image Editing on the web, which was released inv2.5.0. This feature allows you to make non-destructive edits to your photos inside of Immich. Until now, the mobile editor used a completely different system that created new assets instead of editing the photo in place.

With this update, we bring a new, easier-to-use editor to mobile devices that has the same features as the web version. You can now edit photos directly in the mobile app, including cropping, rotating, and adjusting your images without ever touching the original file. Similar to the web, edits are non-destructive, so you can revisit or revert them at any time. You can even make edits on mobile and then adjust them on the web later!

Some features from the previous mobile editing implementation have been removed including:

* Recoloring photos
* Editing live photos
* Editing local assets

We have plans to bring some of these capabilities back in future releases.

### Workflows (preview)

The first preview of Workflows is here! Workflows let you automate actions in your library by chaining triggers, filters, and actions together with a drag-and-drop builder. This is the foundation for many exciting automations to come, and we'd love your feedback as we continue building on it.

You can access the feature fromUtilities > Workflowson the web.

From there, you can either create a new blank workflow or browse the premade templates to get a basic understanding of how workflows can be used.

#### Workflows editor

In the workflows editor, you can switch between the Visual or JSON editor. The visual editor is nice for building out the workflow; the JSON editor is nice for sharing and receiving workflow content from others.

In each workflow, there is atriggerand a sequence ofsteps.

* Trigger: this is the entry point of each workflow; when the trigger occurs, the steps are evaluated.
* Steps: they include Filters (conditions) and Actions (effects); they can be combined to produce the desired effect of the use case you aim for.

#### Sharing a workflow

You can share the workflow you made with others in two ways: text and JSON. Text is nice for sharing on a forum or for show-and-tell content. JSON is nice for others to make an exact copy of your workflow's configuration.

You can copy the text in the workflows summary panel on the lower right of the screen

You can share the JSON content from the copy workflows button in the app bar, switch to the JSON editor, or use theShow schemabutton in the context menu in the workflows list

Note

Please use thisdiscussion threadto propose new ideas of triggers and actions. We are looking for extensive feedback and suggestions from you all.

### Background backup improvements

Background backup on Android is now significantly more reliable. Previously, the background backup on Android was limited to newly taken photos. Now, the app uses a new periodic task scheduler, which allows you to upload your entire library in the background, and it plays nicer with Android's background execution limits, properly cleans up tasks, and warns you when battery optimization and notification settings might interfere with backups.

On iOS, the background refresh task now runs its sync and upload work in parallel, so uploads actually start within the short time window iOS allows.

### Recently added page

A new "Recently Added" page on the web and mobile lets you browse your library sorted by when assets were added to Immich, rather than when they were taken. This makes it easier to find what's new when browsing a new batch of imports. You can find the new page in the "Explore" tab on the web and in the "Search" tab on mobile.

### Integrity checks

The maintenance page has gotten a new addition: integrity reports! Immich will scan its directories on your file system, and compare it to what it has stored in its database. If there are deviations, they will be surfaced as

* untracked, if there is a file in Immich's directories that Immich does not know of
* missing, if Immich references a file in its database that does not exist in that place (anymore)
* a checksum mismatch, if the checksum of the file on disk does not match the checksum Immich has stored for that file. Typically, this would happen through file corruption but could also be the result of a bad rename.

You can configure when and how long the job runs each night.

### Slideshow (mobile)

The slideshow experience comes to mobile! You can now sit back and let your photos and videos play across the screen, just like on the web.

### HLS and Real-Time Video transcoding (preview)

Immich can now transcode videos on-the-fly without needing to generate offline transcodes. This has been a long-requested feature with many benefits:

* Quality switching (both manual and automatic)
* Transcoding to the best codecs supported by the client
* Lower storage overhead when offline transcoding is disabled
* HDR for compatible clients (not implemented yet)
* Remuxing rather than transcoding the original when bandwidth allows it (not implemented yet)

Please note that this feature is still experimental and can change behavior from version to version. It's currently only implemented in the web app, with the mobile app implementation in progress.

To enable real-time transcoding, go to thevideo transcoding settings(scroll down). Offline transcoding isn't directly affected by enabling it, so if you'd like to disable offline transcoding, you should also adjust the transcode policy.

Note

For assets imported prior to v3, you will also need to re-run Metadata Extraction in the job panel for them to be re-processed.

Keep in mind that your server needs to be powerful enough to transcode in real-time for this feature to work well. Hardware acceleration is recommended, but not required, when using this feature.

### New video player for web

A new custom video player on the web app ensures all your devices share the same controls and layout, matching the Immich design. Some basic functions, like changing the playback rate, are available. This should also fix a lot of the problems on iOS, where the OS's controls are hidden behind the Immich navbar.

### Open photos in Immich as a gallery on Android

Immich can now act as a gallery/image viewer app on Android. Tap a photo or video in another app, choose Immich, and it opens directly in the asset viewer with options to share the file or upload it to your library.

This is the first iteration of the feature, and refinements to how Immich recognizes files that are already in your library are on the way

### OCR on the mobile app

The asset viewer now has a toggle that highlights recognized text in a photo, and you can select and copy it directly from the image.

### Upload assets directly to an album on mobile

You can now upload local photos directly to an album in the mobile app, including from the asset bottom sheet, instead of uploading first and organizing later. A small change that removes a lot of friction from the backup-and-organize flow.

### Select image size when sharing on mobile

When sharing photos from the mobile app, you can now choose the image size before sending; it is handy for keeping shared files small for messaging apps while preserving the option to share at full quality when needed.

You can change the default behavior in theApp Settings > Preferences

You can also pick the option when sharing on-the-fly by long pressing theSharebutton

### Timeline performance Improvements

Browsing months with a large number of assets is now dramatically smoother and prevents the browser tab from locking up when your instance encounters that scenario.

## Support Immich

If you find the project helpful, you can support Immich by purchasing a product key athttps://buy.immich.appor our merchandise athttps://immich.store

## What's Changed

### 🚨 Breaking Changes

* refactor!: migrate class-validator to zod by@timonriegerinrefactor!: migrate class-validator to zod#26597
* refactor!: remove replace asset by@jrasm91inrefactor!: remove replace asset#27022
* refactor!: remove my shared link dto by@jrasm91inrefactor!: remove my shared link dto#27023
* chore!: remove deprecated env variables by@jrasm91inchore!: remove deprecated env variables#27802
* chore!: remove getRandom api endpoint by@bweesinchore!: remove getRandom api endpoint#27780
* chore!: remove unused token response param by@jrasm91inchore!: remove unused token response param#27805
* refactor: yeet old timeline by@shenlong-tanweninrefactor: yeet old timeline#27666
* chore!: remove old timeline sync endpoints by@jrasm91inchore!: remove old timeline sync endpoints#27804
* chore!: remove deviceId and deviceAssetId by@danieldietzlerinchore!: remove deviceId and deviceAssetId#27818
* chore!: rename API key schemas by@jrasm91inchore!: rename API key schemas#27828
* chore!: remove without assets by@jrasm91inchore!: remove without assets#27835
* fix: oauth issuerUrl validation by@bo0tzzinfix: oauth issuerUrl validation#27848
* fix!: do not allow insecure oauth requests by default by@bo0tzzinfix!: do not allow insecure oauth requests by default#27844
* fix!: set duration to null when not present by@meesfrenselinfix!: set duration to null when not present#26982
* chore!: remove /api/server/theme endpoint by@jrasm91inchore!: remove /api/server/theme endpoint#27880
* chore!: migrate album owner to album_user by@danieldietzlerinchore!: migrate album owner to album_user#27467
* refactor!: change number to integer types by@timonriegerinrefactor!: change number to integer types#27912
* refactor(server)!: move correlationId to X-Correlation-ID response header by@timonriegerinrefactor(server)!: move correlationId to X-Correlation-ID response header#28139
* refactor(server)!: remove redundant error and statusCode fields from error responses by@timonriegerinrefactor(server)!: remove redundant error and statusCode fields from error responses#28140
* chore(server)!: drop pgvecto.rs support by@mertalevinchore(server)!: drop pgvecto.rs support#28159
* chore!: duration in milliseconds by@mertalevinchore!: duration in milliseconds#28003
* refactor(server)!: sanitize error messages to avoid leaking resource details by@timonriegerinrefactor(server)!: sanitize error messages to avoid leaking resource details#28154
* refactor(server)!: structured validation error responses by@timonriegerinrefactor(server)!: structured validation error responses#28204
* feat(server)!: add isOwned filter to albums API by@timonriegerinfeat(server)!: add isOwned filter to albums API#28213
* chore(ml)!: require numpy 2.4 by@mertalevinchore(ml)!: require numpy 2.4#28158
* fix(deps): update dependency nestjs-otel to v8 by@renovate[bot] infix(deps): update dependency nestjs-otel to v8#27863
* chore(ml)!: remove deprecated envs by@mertalevinchore(ml)!: remove deprecated envs#28326
* chore(server)!: remove libopus enum by@mertalevinchore(server)!: remove libopus enum#28325
* refactor!: remove asset faces from AssetResponseDto by@bweesinrefactor!: remove asset faces from AssetResponseDto#27779
* refactor(server)!: drop empty string to null conversion by@timonriegerinrefactor(server)!: drop empty string to null conversion#28808
* refactor(server)!: remove changeExpiryTime by@timonriegerinrefactor(server)!: remove changeExpiryTime#28816
* refactor!: disallow star rating < 1 by@meesfrenselinrefactor!: disallow star rating < 1#27896
* fix!: search endpoints visibility can be omitted by@danieldietzlerinfix!: search endpoints visibility can be omitted#29385

### 🫥 Deprecated Changes

* refactor(server): deprecate PUT routes in favor of PATCH by@timonriegerinrefactor(server): deprecate PUT routes in favor of PATCH#28859

### 🔒 Security

* fix: run profile picture through thumbnail pipeline by@bo0tzzinfix: run profile picture through thumbnail pipeline#27890

### 🚀 Features

* feat: mobile editing by@bweesinfeat: mobile editing#25397
* feat: album map markers endpoint by@jrasm91infeat: album map markers endpoint#27830
* feat(server): added backchannel logout api endpoint by@santanoceinfeat(server): added backchannel logout api endpoint#26235
* feat(server): add OIDC logout URL override option by@LJspiceinfeat(server): add OIDC logout URL override option#27389
* feat: android periodic work manager task by@shenlong-tanweninfeat: android periodic work manager task#23563
* feat(web): custom video player controls by@meesfrenselinfeat(web): custom video player controls#26183
* feat(web): add full-path search mode to UI by@mws-weekend-projectsinfeat(web): add full-path search mode to UI#26758
* feat: recently added assets page by@benbeckfordinfeat: recently added assets page#28272
* feat(mobile): slideshow view by@benbeckfordinfeat(mobile): slideshow view#28421
* feat(mobile): "Add Tags" asset multiselect option by@benjamonnguyeninfeat(mobile): "Add Tags" asset multiselect option#26269
* feat: workflows & plugins by@jrasm91infeat: workflows & plugins#26727
* feat(server): hls with real-time transcoding by@mertalevinfeat(server): hls with real-time transcoding#28230
* feat(web): hls player by@mertalevinfeat(web): hls player#28312
* feat(mobile): Android. Immich as a gallery / image viewer app by@PeterOmbodiinfeat(mobile): Android. Immich as a gallery / image viewer app#26109
* feat: user upload heatmap by@bondeabhijeetinfeat: user upload heatmap#28593
* feat(mobile): ocr support by@YarosMallorcainfeat(mobile): ocr support#26523
* feat: geolocation workflow filter by@benbeckfordinfeat: geolocation workflow filter#28961
* feat: image quality option in sharing by@alextran1502infeat: image quality option in sharing#28918
* feat: integrity check jobs (missing files, untracked files, checksums) by@insertishinfeat: integrity check jobs (missing files, untracked files, checksums)#24205
* feat: new feature message by@alextran1502infeat: new feature message#29388

### 🌟 Enhancements

* feat(web): persist state of file path information in details panel by@cratooinfeat(web): persist state of file path information in details panel#27770
* feat: commands by@jrasm91infeat: commands#27546
* feat: upgrade immich/ui by@jrasm91infeat: upgrade immich/ui#27792
* feat: filter users on share by@OdinOxininfeat: filter users on share#27732
* fix(server): render storage template date/time tokens in UTC (Storage Template dates/times not adjusted for timezone#24350) by@migpovrapinfix(server): render storage template date/time tokens in UTC (#24350)#26917
* feat(web): lazy load library and server statistics by@etnoyinfeat(web): lazy load library and server statistics#26406
* feat: sort users alphabetically when adding to album by@OdinOxininfeat: sort users alphabetically when adding to album#27731
* feat: auth logout page by@jrasm91infeat: auth logout page#27831
* chore: improve randomness of /search/random endpoint by@StevenMassaroinchore: improve randomness of /search/random endpoint#27531
* feat: dynamic languages by@jrasm91infeat: dynamic languages#27869
* feat: cache shared link by@danieldietzlerinfeat: cache shared link#27889
* feat(server): add configurable OAuth prompt parameter by@sparsh985infeat(server): add configurable OAuth prompt parameter#26755
* feat(server): add MPO file type support by@git-akihakuneinfeat(server): add MPO file type support#27963
* feat(mobile): action bottom sheet on map timeline by@YarosMallorcainfeat(mobile): action bottom sheet on map timeline#27515
* feat(server): track video metadata by@mertalevinfeat(server): track video metadata#28023
* feat(enhancement): Navigate stack with up and down arrow keys by@cratooinfeat(enhancement): Navigate stack with up and down arrow keys#27854
* fix(web): migrate people management component to page, enabling tooltips by@SkyDev125infix(web): migrate people management component to page, enabling tooltips#26971
* chore(mobile): add box shadow to asset details by@uhthomasinchore(mobile): add box shadow to asset details#27510
* feat: hide hidden person from memories by@sakshamchawlainfeat: hide hidden person from memories#20877
* feat(mobile): increased tap area on video player overlay by@YarosMallorcainfeat(mobile): increased tap area on video player overlay#27269
* feat(web): Add metadata overlay to slideshow by@timonriegerinfeat(web): Add metadata overlay to slideshow#24627
* feat(web): add individual filter removal from search result chips by@timonriegerinfeat(web): add individual filter removal from search result chips#28166
* feat(mobile): trash/restore all by@YarosMallorcainfeat(mobile): trash/restore all#28116
* feat: display more info in asset viewer by@alextran1502infeat: display more info in asset viewer#24630
* feat(server): allow subpaths for machine learning URL by@gnojusinfeat(server): allow subpaths for machine learning URL#28427
* feat(ui): Shared URL input configuration by@Lauritz-Tiesteinfeat(ui): Shared URL input configuration#27105
* refactor: enhance shared link UI and functionality by@Lauritz-Tiesteinrefactor: enhance shared link UI and functionality#26464
* feat: upload and add local asset directly to album by@alextran1502infeat: upload and add local asset directly to album#28123
* feat: Selectable metadata in duplicates utility with diffing by@ollioddiinfeat: Selectable metadata in duplicates utility with diffing#26328
* fix: improve form control focus visibility by@Caltsicinfix: improve form control focus visibility#28512
* feat: command for user pages by@alextran1502infeat: command for user pages#28554
* refactor: use ControlBar UI Library component by@bweesinrefactor: use ControlBar UI Library component#28567
* feat: workflow template by@alextran1502infeat: workflow template#28553
* feat(mobile): improve downloading algorithm for sharing by@YarosMallorcainfeat(mobile): improve downloading algorithm for sharing#27312
* feat: search by album name and id by@jrasm91infeat: search by album name and id#28672
* feat: upload local assets to album from bottom sheet by@alextran1502infeat: upload local assets to album from bottom sheet#28531
* feat: places in context search by@timonriegerinfeat: places in context search#28768
* feat: minimum face count per user by@timjonezinfeat: minimum face count per user#27452
* feat: show notification and battery optimization warning by@shenlong-tanweninfeat: show notification and battery optimization warning#26610
* feat: workflows drag and drop enhancements by@danieldietzlerinfeat: workflows drag and drop enhancements#28764
* feat(mobile): min face count per-user by@YarosMallorcainfeat(mobile): min face count per-user#28805
* refactor(server): allow -1 rating again by@timonriegerinrefactor(server): allow -1 rating again#28886
* feat(web): warn before overwriting existing locations in geolocation utility by@yoshovskiinfeat(web): warn before overwriting existing locations in geolocation utility#28840
* feat: warn if microservices worker is missing by@bo0tzzinfeat: warn if microservices worker is missing#28869
* fix(web): show album names in duplicate review by@meesfrenselinfix(web): show album names in duplicate review#29080
* feat: keyboard seeking for new video player by@danieldietzlerinfeat: keyboard seeking for new video player#29208
* feat(web): Add text-white-shadow to elements and increase the shadows effect by@Vogeluffinfeat(web): Add text-white-shadow to elements and increase the shadows effect#29165
* feat: webhook workflow action by@benbeckfordinfeat: webhook workflow action#29258
* feat: integrity checks admin settings by@danieldietzlerinfeat: integrity checks admin settings#29406

### 🐛 Bug fixes

* fix(web): center images in RTL layouts (Bug: Image not centered in RTL layout (Hebrew)#27678) by@Nicolas-micuda-beckerinfix(web): center images in RTL layouts (#27678)#27753
* fix(mobile): add keys for person tiles in search by@YarosMallorcainfix(mobile): add keys for person tiles in search#27689
* fix(web): selection clearing on preview by@YarosMallorcainfix(web): selection clearing on preview#27702
* fix: asset multi select download shortcut by@danieldietzlerinfix: asset multi select download shortcut#27784
* fix(web): add partner photo to album from multiselect by@YarosMallorcainfix(web): add partner photo to album from multiselect#27767
* fix: redirect original by@danieldietzlerinfix: redirect original#27759
* fix: make web build stage deterministic by@bo0tzzinfix: make web build stage deterministic#27823
* fix(web): svelte regression - cancel video preview fetch when bind:this is cleared early by@midzelisinfix(web): svelte regression - cancel video preview fetch when bind:this is cleared early#27713
* fix(web): stale adaptive image when original overlays preview by@midzelisinfix(web): stale adaptive image when original overlays preview#27621
* fix(mobile): readonly redirect when not logged in by@YarosMallorcainfix(mobile): readonly redirect when not logged in#27728
* fix(web): close edit faces panel on Escape key press by@midzelisinfix(web): close edit faces panel on Escape key press#27519
* fix(oauth): normalize email claim to lowercase and trim before account lookup and registration by@timdobrasinfix(oauth): normalize email claim to lowercase and trim before account lookup and registration#26841
* fix(web): use event for zooming out after opening face editor by@meesfrenselinfix(web): use event for zooming out after opening face editor#27789
* fix: sanitize filenames before adding to zip by@bo0tzzinfix: sanitize filenames before adding to zip#27893
* fix(server): require at least one field to be set when updating memory by@fredfloyddinfix(server): require at least one field to be set when updating memory#27842
* fix(web): compute hashes for uploads in chunks by@fredfloyddinfix(web): compute hashes for uploads in chunks#27878
* fix(web): fix stale album page load by@fredfloyddinfix(web): fix stale album page load#27825
* fix(web): prevent interaction with detail panel behind person side panel by@midzelisinfix(web): prevent interaction with detail panel behind person side panel#27309
* fix: show neon light by@alextran1502infix: show neon light#27994
* fix(mobile): zero exposure by@YarosMallorcainfix(mobile): zero exposure#28017
* fix(mobile): clear local data on forced logout by@LeLunZinfix(mobile): clear local data on forced logout#27957
* fix(mobile): enable autoplay for motion photos in video viewer by@LeLunZinfix(mobile): enable autoplay for motion photos in video viewer#27961
* fix(mobile): thumbnail transition to asset viewer by@LeLunZinfix(mobile): thumbnail transition to asset viewer#27850
* fix: jump to timeline on new auto_router update by@alextran1502infix: jump to timeline on new auto_router update#28022
* fix(mobile): delete assets on trash empty, Android by@PeterOmbodiinfix(mobile): delete assets on trash empty, Android#26070
* fix(ml): handle empty/corrupt images in face detection by@yositinfix(ml): handle empty/corrupt images in face detection#27391
* fix(web): refresh memories hourly by@meesfrenselinfix(web): refresh memories hourly#28114
* fix(web): large files: better handling of asset deletions by@meesfrenselinfix(web): large files: better handling of asset deletions#28117
* fix(web): double video playback on map timeline by@YarosMallorcainfix(web): double video playback on map timeline#28090
* fix(mobile): suppress asset stack UI in trash timeline by@PeterOmbodiinfix(mobile): suppress asset stack UI in trash timeline#26536
* fix(web): timeline scroll when pressing back from stacked asset by@Snowknight26infix(web): timeline scroll when pressing back from stacked asset#28163
* fix(server): selectively apply metadata bitstream filter for video thumbnails by@pinhaoinfix(server): selectively apply metadata bitstream filter for video thumbnails#28162
* fix(web): fix shared link /s/photos.* navigation after password login by@meesfrenselinfix(web): fix shared link /s/photos.* navigation after password login#27788
* fix(ml): respect time zone for logs in cuda container by@AyaanMAGinfix(ml): respect time zone for logs in cuda container#28155
* fix: librknnrt permissions in machine-learning by@DavidTheFighterinfix: librknnrt permissions in machine-learning#28216
* fix(server): validate duplicate group ownership before dismissal by@timonriegerinfix(server): validate duplicate group ownership before dismissal#28221
* fix(web): correct timeline yesterday label across month boundaries by@michelheusscheninfix(web): correct timeline yesterday label across month boundaries#28183
* fix(mobile): show lens info without lens name by@benbeckfordinfix(mobile): show lens info without lens name#28234
* fix: stale person name after merge by@danieldietzlerinfix: stale person name after merge#28222
* fix(web): shared album avatars opening modal by@meesfrenselinfix(web): shared album avatars opening modal#26719
* fix(mobile): prevent asset loading issues when changing page or when closing memories by@LeLunZinfix(mobile): prevent asset loading issues when changing page or when closing memories#27596
* fix(mobile): correct filter default and UI desync in similar photos search by@TheBestX11infix(mobile): correct filter default and UI desync in similar photos search#27516
* fix(server): hide isFavorite from partner asset sync stream by@timonriegerinfix(server): hide isFavorite from partner asset sync stream#28035
* fix(mobile): restore notification plugin init by@santoshakilinfix(mobile): restore notification plugin init#28284
* fix(mobile): mounted check before setState in album sync action by@santoshakilinfix(mobile): mounted check before setState in album sync action#28300
* fix(mobile): avoid duplicate assets in album view by@stfn42infix(mobile): avoid duplicate assets in album view#28152
* fix(mobile): Deduplicate assets in person view timeline by @thowdev infix(mobile): Deduplicate assets in person view timeline#26723
* fix(deployment): remove unneeded volume by @mmomjian infix(deployment): remove unneeded volume#28307
* fix: mobile upload duration type by@alextran1502infix: mobile upload duration type#28362
* fix: deep link for assets when asset viewer already open by@bweesinfix: deep link for assets when asset viewer already open#27971
* fix: kekab icon colors in light mode by@shenlong-tanweninfix: kekab icon colors in light mode#28366
* fix: indexes on remote_asset_entity by@shenlong-tanweninfix: indexes on remote_asset_entity#28264
* fix(mobile): clear linkedRemoteAlbumId in reset() so FK refs dont dangle by@santoshakilinfix(mobile): clear linkedRemoteAlbumId in reset() so FK refs dont dangle#28382
* fix: ignore icc profile make and model by@jrasm91infix: ignore icc profile make and model#28412
* fix(mobile): don't block app open on slow validateAccessToken by@santoshakilinfix(mobile): don't block app open on slow validateAccessToken#28405
* fix(mobile): add restore option to trashed assets by @inesiscosta infix(mobile): add restore option to trashed assets#27442
* fix(mobile): use correct delete action by @ByteSizedMarius infix(mobile): use correct delete action#26575
* fix(server): dedupe database backup jobs by @rdeaton infix(server): dedupe database backup jobs#28341
* fix(mobile): cronet buffer overflow on compressed thumbnails by@santoshakilinfix(mobile): cronet buffer overflow on compressed thumbnails#28439
* fix(mobile): cronet thumbnail buffer overflow regression fromfix(mobile): cronet buffer overflow on compressed thumbnails#28439by@santoshakilinfix(mobile): cronet thumbnail buffer overflow regression from #28439#28450
* fix(mobile): mounted check in ThumbnailTile hero flight listener by@santoshakilinfix(mobile): mounted check in ThumbnailTile hero flight listener#28451
* fix(mobile): don't force-unwrap nil localizedTitle in ios getAlbums by@santoshakilinfix(mobile): don't force-unwrap nil localizedTitle in ios getAlbums#28452
* fix(web): work around Chrome HDR image seam lines during zoom by@midzelisinfix(web): work around Chrome HDR image seam lines during zoom#27715
* fix(ios): respect status bar scroll to top in timeline views by @agg23 infix(ios): respect status bar scroll to top in timeline views#28469
* fix(mobile): asset viewer stuck on spinner after rotation by@LeLunZinfix(mobile): asset viewer stuck on spinner after rotation#28019
* fix(web): timeline stuttering with many assets in 1 day by@benbeckfordinfix(web): timeline stuttering with many assets in 1 day#28509
* fix(mobile): preserve zoom level during image loading and live photo playback by@LeLunZinfix(mobile): preserve zoom level during image loading and live photo playback#27960
* fix(ml): stabilize MIGraphX inference by @fabianwimberger infix(ml): stabilize MIGraphX inference#28444
* fix: await sync asset v2 by@bweesinfix: await sync asset v2#28569
* fix: strip metadata from timeline responses for shared links without exif sharing by@danieldietzlerinfix: strip metadata from timeline responses for shared links without exif sharing#28644
* fix: Refresh local album overview page after asset deletion by@Lauritz-Tiesteinfix: Refresh local album overview page after asset deletion#28586
* fix(server): prevent locked assets from leaking to partners by@timonriegerinfix(server): prevent locked assets from leaking to partners#28652
* refactor(web): replace per-asset viewport proximity with day-tier active indices by@midzelisinrefactor(web): replace per-asset viewport proximity with day-tier active indices#28597
* fix: timeline scroll flicker by@alextran1502infix: timeline scroll flicker#28653
* fix: api repositories using stale endpoint by@shenlong-tanweninfix: api repositories using stale endpoint#28667
* fix: disallow cross origin/non http protocols for continueUrl on login by@bweesinfix: disallow cross origin/non http protocols for continueUrl on login#28706
* fix(web): skip thumbhash fade for offscreen thumbnails by@midzelisinfix(web): skip thumbhash fade for offscreen thumbnails#27335
* fix(web): prevent partner assets from being selected in geolocation utility by @okxint infix(web): prevent partner assets from being selected in geolocation utility#28737
* fix(mobile): invisible ink splashes in asset sheet by@timonriegerinfix(mobile): invisible ink splashes in asset sheet#28756
* fix!: unauthorized face creation by@shenlong-tanweninfix!: unauthorized face creation#28561
* fix(mobile): proper background task cleanup by@mertalevinfix(mobile): proper background task cleanup#28694
* fix(cli): prevent out-of-memory on file upload due to undici storing the request body by @moversity infix(cli): prevent out-of-memory on file upload due to undici storing the request body#28723
* fix: error log on aborted uploads by@jrasm91infix: error log on aborted uploads#28806
* fix(server): respect timezone in iso date string encoding by@timonriegerinfix(server): respect timezone in iso date string encoding#28810
* test: fix tests when OpenVINO provider is available by @nekowinston intest: fix tests when OpenVINO provider is available#28802
* fix(mobile): run iOS bg task phases in parallel by@santoshakilinfix(mobile): run iOS bg task phases in parallel#28293
* fix: error handling by@jrasm91infix: error handling#28843
* fix: cross isolate drift watchers by@shenlong-tanweninfix: cross isolate drift watchers#28862
* fix: reload timeline on group by setting change by@shenlong-tanweninfix: reload timeline on group by setting change#28864
* fix(web): use irot/imir tags for HEIF Orientation by @joojoooo infix(web): use irot/imir tags for HEIF Orientation#27820
* fix: detail panel faces reactivity issues by@danieldietzlerinfix: detail panel faces reactivity issues#28910
* fix(server): hide isFavorite from album asset sync stream by@timonriegerinfix(server): hide isFavorite from album asset sync stream#28923
* fix(mobile): show memory and folder dates in local time by@santoshakilinfix(mobile): show memory and folder dates in local time#28941
* fix(mobile): show error when creating an album fails by@santoshakilinfix(mobile): show error when creating an album fails#28942
* fix(mobile): add album picker to archive bottom sheet by@santoshakilinfix(mobile): add album picker to archive bottom sheet#28953
* fix: normalize diacritics in person name search in Web & Mobile by @pedrovieira infix: normalize diacritics in person name search in Web & Mobile#28887
* fix(web): Prevent face editor from closing when dismissing tag confirmation by @pedrovieira infix(web): Prevent face editor from closing when dismissing tag confirmation#28900
* fix(mobile): map timeline layout crash by@YarosMallorcainfix(mobile): map timeline layout crash#28878
* fix(mobile): deduplicate people in asset details panel by@santoshakilinfix(mobile): deduplicate people in asset details panel#28972
* fix(mobile): keep timezone when editing asset date time by@santoshakilinfix(mobile): keep timezone when editing asset date time#28978
* fix(mobile): stale details after editing asset date by@santoshakilinfix(mobile): stale details after editing asset date#28977
* fix(mobile): show albums whose assets are all trashed by@santoshakilinfix(mobile): show albums whose assets are all trashed#28985
* fix(mobile): give android notification channels proper names by@santoshakilinfix(mobile): give android notification channels proper names#28986
* fix: Improving scroll behavior on image stacks that overflow the screen by @BlankCanvasStudio infix: Improving scroll behavior on image stacks that overflow the screen#28885
* fix(web): focus on scrollable element on load by@timonriegerinfix(web): focus on scrollable element on load#29004
* fix(mobile): show like and comment options on album photo deep links by@santoshakilinfix(mobile): show like and comment options on album photo deep links#29020
* fix(web): correctly handle person search with more than 100 results by @maxinegardenas infix(web): correctly handle person search with more than 100 results#29002
* fix(web): prevent upload status panel from overlapping album action bar by @okxint infix(web): prevent upload status panel from overlapping album action bar#29044
* fix(web): error loading image state by@bweesinfix(web): error loading image state#29058
* fix(web): show asset arrows by@timonriegerinfix(web): show asset arrows#29010
* fix(server): hide partner archived asset locations from map by@timonriegerinfix(server): hide partner archived asset locations from map#29028
* fix: lock transcoding options by@timonriegerinfix: lock transcoding options#29076
* fix(server): do not merge metadata when multiple duplicates are kept by@timonriegerinfix(server): do not merge metadata when multiple duplicates are kept#29035
* fix: integrity report checksum query by@danieldietzlerinfix: integrity report checksum query#29136
* fix: map settings by@danieldietzlerinfix: map settings#29134
* fix: too strict cron expression validation by@danieldietzlerinfix: too strict cron expression validation#29138
* fix(web): respect local timezone when building date range for search by @okxint infix(web): respect local timezone when building date range for search#29128
* fix(web): language selector by@meesfrenselinfix(web): language selector#29065
* fix: update datetimeRelative description to minutes instead of seconds by@meesfrenselinfix: update datetimeRelative description to minutes instead of seconds#29137
* fix: video thumbnail quality sharing by@bweesinfix: video thumbnail quality sharing#29104
* fix(mobile): stop sync albums crashing on the main isolate by@santoshakilinfix(mobile): stop sync albums crashing on the main isolate#29133
* fix(mobile): show memories with no showAt/hideAt in the timeline lane by@santoshakilinfix(mobile): show memories with no showAt/hideAt in the timeline lane#29158
* fix(mobile): keep toasts off the dynamic island when keyboard is open by@santoshakilinfix(mobile): keep toasts off the dynamic island when keyboard is open#29159
* fix(server): skip existing users when sharing albums by @jeevan6996 infix(server): skip existing users when sharing albums#28884
* fix: web i18n by@danieldietzlerinfix: web i18n#29175
* fix(web): shift+click on GPS asset extends range selection in geolocation utility by@timonriegerinfix(web): shift+click on GPS asset extends range selection in geolocation utility#29022
* fix(server): allow non-utc datetime offsets by@timonriegerinfix(server): allow non-utc datetime offsets#29186
* fix: remove local-only step ids from workflow json by@danieldietzlerinfix: remove local-only step ids from workflow json#29188
* fix: asset type filter by@danieldietzlerinfix: asset type filter#29190
* fix(mobile): prevent duplicate login pages for unauthenticated share intent warm start by @olildu infix(mobile): prevent duplicate login pages for unauthenticated share intent warm start#29054
* fix(mobile): refresh memories on resume and day change by@santoshakilinfix(mobile): refresh memories on resume and day change#28983
* fix(mobile): re-lock locked folder when the app is backgrounded by@santoshakilinfix(mobile): re-lock locked folder when the app is backgrounded#29089
* fix(mobile): endless spinner on album selection when device has no albums by@santoshakilinfix(mobile): endless spinner on album selection when device has no albums#28994
* fix: rc version check by@danieldietzlerinfix: rc version check#29194
* fix: detail panel people reactivity and iterator consumption by@danieldietzlerinfix: detail panel people reactivity and iterator consumption#29250
* fix(server): use VBR for QSV so the max bitrate is respected by @aclerici38 infix(server): use VBR for QSV so the max bitrate is respected#29240
* fix: ignore external libraries for integrity report checksum check by@danieldietzlerinfix: ignore external libraries for integrity report checksum check#29248
* fix(web): remove map's fullscreen button by@meesfrenselinfix(web): remove map's fullscreen button#29192
* refactor: use SemVer classes for version compatability message by@bweesinrefactor: use SemVer classes for version compatability message#29056
* fix: sync backfill by@jrasm91infix: sync backfill#29267
* fix(mobile): force AssetViewerPage recreation on repeated view intents by @okxint infix(mobile): force AssetViewerPage recreation on repeated view intents#29235
* fix(mobile): blank notifications page after enabling notifications by@santoshakilinfix(mobile): blank notifications page after enabling notifications#29232
* fix(mobile): app doesn't exit full-screen mode by@YarosMallorcainfix(mobile): app doesn't exit full-screen mode#29301
* fix(mobile): only toggle backup from the switch, not the whole row by@santoshakilinfix(mobile): only toggle backup from the switch, not the whole row#29236
* fix(mobile): hide video thumbnail when video is ready by@santoshakilinfix(mobile): hide video thumbnail when video is ready#29012
* fix(mobile): apply exif orientation to android raw photos by@santoshakilinfix(mobile): apply exif orientation to android raw photos#29337
* fix(server): face region coordinates parsing by @djbravo06 infix(server): face region coordinates parsing#29333
* feat: honor album access permissions in search endpoints by@danieldietzlerinfeat: honor album access permissions in search endpoints#29352
* fix: version compatability check by@bweesinfix: version compatability check#29405

### 📚 Documentation

* fix(docs): instructions on how to use local immich ui by@YarosMallorcainfix(docs): instructions on how to use local immich ui#27813
* fix(docs): helmet file affected containers by @mmomjian infix(docs): helmet file affected containers#27939
* fix(docs): Update Tailscale free tier user and device limits by @Hakuin123 infix(docs): Update Tailscale free tier user and device limits#28151
* docs: update rocm installation instructions by @aigarius indocs: update rocm installation instructions#25434
* fix(docs): documentupgrade-insecure-requestsdefault by@meesfrenselinfix(docs): documentupgrade-insecure-requestsdefault#28279
* fix(docs): missing colon in config file doc by @SuperSandro2000 infix(docs): missing colon in config file doc#28313
* fix: update server-commands subcommand list by@bo0tzzinfix: update server-commands subcommand list#28402
* feat(docs): add fixed subnet guide for Synology to prevent firewall issues by @racehd infeat(docs): add fixed subnet guide for Synology to prevent firewall issues#26554
* chore(docs): update FAQ with profile picture change instructions by @tvangemert inchore(docs): update FAQ with profile picture change instructions#28634
* chore: update documentation to use mise commands by@timonriegerinchore: update documentation to use mise commands#28515
* fix(docs): v3 bumps by @mmomjian infix(docs): v3 bumps#29007
* docs(server): clarify AssetBulkUploadCheckItem.id is a correlation token by@timonriegerindocs(server): clarify AssetBulkUploadCheckItem.id is a correlation token#29141
* docs(mobile-app): add Play App Signing certificate hash by @tlvince indocs(mobile-app): add Play App Signing certificate hash#29168
* docs(mobile): point users towards shared setup docs by @agg23 indocs(mobile): point users towards shared setup docs#29078
* docs: clarify duplicate exif merging intent by@timonriegerindocs: clarify duplicate exif merging intent#29203
* fix(docsc): v3 bump by @mmomjian infix(docsc): v3 bump#29246
* docs: MS smtp guide by @jameskimmel indocs: MS smtp guide#29289

### 🌐 Translations

* feat: latest language requests by@danieldietzlerinfeat: latest language requests#28858
* chore: update translations by @weblate inchore: update translations#27764
* feat: languages by@danieldietzlerinfeat: languages#29088
* chore(web): update translations by @weblate inchore(web): update translations#29036
* chore(web): update translations by @weblate inchore(web): update translations#29162
* fix: turkish readme translation by @MuySup infix: turkish readme translation#29234
* chore(web): update translations by @weblate inchore(web): update translations#29204
* chore(web): update translations by @weblate inchore(web): update translations#29290
* chore(web): update translations by @weblate inchore(web): update translations#29347

## New Contributors

* @OdinOxinmade their first contribution infeat: filter users on share#27732
* @migpovrapmade their first contribution infix(server): render storage template date/time tokens in UTC (#24350)#26917
* @StevenMassaromade their first contribution inchore: improve randomness of /search/random endpoint#27531
* @timdobrasmade their first contribution infix(oauth): normalize email claim to lowercase and trim before account lookup and registration#26841
* @santanocemade their first contribution infeat(server): added backchannel logout api endpoint#26235
* @fredfloyddmade their first contribution infix(server): require at least one field to be set when updating memory#27842
* @sparsh985made their first contribution infeat(server): add configurable OAuth prompt parameter#26755
* @LJspicemade their first contribution infeat(server): add OIDC logout URL override option#27389
* @git-akihakunemade their first contribution infeat(server): add MPO file type support#27963
* @shaun0927 made their first contribution infix(web): normalize underscore locale codes in dynamic language selection#27900
* @yositmade their first contribution infix(ml): handle empty/corrupt images in face detection#27391
* @Hakuin123 made their first contribution infix(docs): Update Tailscale free tier user and device limits#28151
* @pinhaomade their first contribution infix(server): selectively apply metadata bitstream filter for video thumbnails#28162
* @AyaanMAGmade their first contribution infix(ml): respect time zone for logs in cuda container#28155
* @DavidTheFightermade their first contribution infix: librknnrt permissions in machine-learning#28216
* @benbeckfordmade their first contribution infix(mobile): show lens info without lens name#28234
* @bhugh made their first contribution inchore: enhance documentation on wildcard and exclusion patterns#27884
* @SkyDev125made their first contribution infix(web): migrate people management component to page, enabling tooltips#26971
* @aigarius made their first contribution indocs: update rocm installation instructions#25434
* @mws-weekend-projectsmade their first contribution infeat(web): add full-path search mode to UI#26758
* @TheBestX11made their first contribution infix(mobile): correct filter default and UI desync in similar photos search#27516
* @sakshamchawlamade their first contribution infeat: hide hidden person from memories#20877
* @santoshakilmade their first contribution infix(mobile): restore notification plugin init#28284
* @stfn42made their first contribution infix(mobile): avoid duplicate assets in album view#28152
* @thowdev made their first contribution infix(mobile): Deduplicate assets in person view timeline#26723
* @SuperSandro2000 made their first contribution infix(docs): missing colon in config file doc#28313
* @racehd made their first contribution infeat(docs): add fixed subnet guide for Synology to prevent firewall issues#26554
* @inesiscosta made their first contribution infix(mobile): add restore option to trashed assets#27442
* @gnojusmade their first contribution infeat(server): allow subpaths for machine learning URL#28427
* @rdeaton made their first contribution infix(server): dedupe database backup jobs#28341
* @agg23 made their first contribution infix(ios): respect status bar scroll to top in timeline views#28469
* @ollioddimade their first contribution infeat: Selectable metadata in duplicates utility with diffing#26328
* @Caltsicmade their first contribution infix: improve form control focus visibility#28512
* @fabianwimberger made their first contribution infix(ml): stabilize MIGraphX inference#28444
* @tvangemert made their first contribution inchore(docs): update FAQ with profile picture change instructions#28634
* @BlankCanvasStudio made their first contribution infix: dev container properly builds @immich/plugin-sdk for import#28620
* @pneuly made their first contribution infix(ml): pass model_root_dir to OcrOptions for RapidOCR compatibility#28610
* @timjonezmade their first contribution infeat: minimum face count per user#27452
* @moversity made their first contribution infix(cli): prevent out-of-memory on file upload due to undici storing the request body#28723
* @nekowinston made their first contribution intest: fix tests when OpenVINO provider is available#28802
* @bondeabhijeetmade their first contribution infeat: user upload heatmap#28593
* @joojoooo made their first contribution infix(web): use irot/imir tags for HEIF Orientation#27820
* @pedrovieira made their first contribution infix: normalize diacritics in person name search in Web & Mobile#28887
* @yoshovskimade their first contribution infeat(web): warn before overwriting existing locations in geolocation utility#28840
* @maxinegardenas made their first contribution infix(web): correctly handle person search with more than 100 results#29002
* @jeevan6996 made their first contribution infix(server): skip existing users when sharing albums#28884
* @rizwanpatel-gif made their first contribution infix(web): use deterministic version name in svelte config#29172
* @olildu made their first contribution infix(mobile): prevent duplicate login pages for unauthenticated share intent warm start#29054
* @MuySup made their first contribution infix: turkish readme translation#29234
* @aclerici38 made their first contribution infix(server): use VBR for QSV so the max bitrate is respected#29240
* @jullanggit made their first contribution infix: small typo in openapi-spec#29308
* @jameskimmel made their first contribution indocs: MS smtp guide#29289
* @djbravo06 made their first contribution infix(server): face region coordinates parsing#29333

Full Changelog:v2.7.5...v3.0.0

This discussion was created from the release 
v3.0.0
.

BetaWas this translation helpful?Give feedback.

 

51

 
You must be logged in to vote

 
👍

79

 
 
😄

21

 
 
🎉

112

 
 
❤️

64

 
 
🚀

41

 
 
👀

9

 

 

All reactions

## Replies:19 comments·23 replies

 

Comment options

 

Quote reply

### AspiandJul 2, 2026

 

-

Great work!

BetaWas this translation helpful?Give feedback.

 

6

 
You must be logged in to vote

 

All reactions

 0 replies
 

 

Comment options

 

Quote reply

### dll94-videodeckJul 2, 2026

 

-

is there a tutorial anywhere on how to jump to 3.0 from older [v2.0.1] ?

BetaWas this translation helpful?Give feedback.

 

2

 
You must be logged in to vote

 

All reactions

 2 replies
 

 

Comment options

 

Quote reply

#### jrasm91Jul 2, 2026Maintainer

 

-

I don't think there are any special instructions for any versions between 2.0.1 and 3.0.0, so you should be able to follow the instructions in the release notes.

BetaWas this translation helpful?Give feedback.

 
👍

1

 
 
❤️

1

 

 

All reactions

 

Comment options

 

Quote reply

#### theraspb3rryJul 3, 2026

 

-

https://immich.app/blog/v3-migration

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

### MedPlex98Jul 2, 2026

 

-

I love you all <3

BetaWas this translation helpful?Give feedback.

 

1

 
You must be logged in to vote

 

All reactions

 0 replies
 

 

Comment options

 

Quote reply

### PouzorJul 2, 2026

 

-

Nice !!

BetaWas this translation helpful?Give feedback.

 

1

 
You must be logged in to vote

 

All reactions

 0 replies
 

 

Comment options

 

Quote reply

### SandiyosDevJul 2, 2026

 

-

YEAH, we're finally here!

BetaWas this translation helpful?Give feedback.

 

1

 
You must be logged in to vote

 

All reactions

 0 replies
 

 

Comment options

 

Quote reply

 

edited

### jcbeck37Jul 2, 2026

 

-

Very excited!! What is the best way to handle this:

* on mobile (updated in Play Store to latest), albums are not appearing, just says "No albums found matching your search"

Should I chat in Discord, open a GitHub issue?

EDIT: Fixed by Clearing File Cache in mobile app, under Settings -> Sync Status -> Clear File Cache

BetaWas this translation helpful?Give feedback.

 

2

 
You must be logged in to vote

 

All reactions

 1 reply
 

 

Comment options

 

Quote reply

#### jrasm91Jul 2, 2026Maintainer

 

-

Looks like there was a bug with a migration on the mobile side. Logging out and back it should fix it. Updating to v3 server after updating mobile would also fix it.

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

### tiiinsJul 2, 2026

 

-

New version, new fun, I'm already looking forward to it 🎉🎉

BetaWas this translation helpful?Give feedback.

 

1

 
You must be logged in to vote

 

All reactions

 0 replies
 

 

Comment options

 

Quote reply

### thinkhJul 2, 2026

 

-

Great work and looking forward to all the new features! I updated my Immich instance from v2.7.5 to v3.0.0 by following theHow to updatesection. After the server restarted, I only see the photos and videos until October 2025. All more recent photos are gone(?) or not shown. Also the license key and additional users, I entered in the past months are gone. The last backup listed in the app is also from October, even though I'm sure there were more recent backups. What could be the problem here and how can I get back to the previous state?

BetaWas this translation helpful?Give feedback.

 

1

 
You must be logged in to vote

 

All reactions

 3 replies
 

 

Comment options

 

Quote reply

#### alextran1502Jul 2, 2026MaintainerAuthor

 

-

Can you open a GitHub issue and post the logs from the server and provide your setup info?

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

#### thinkhJul 2, 2026

 

-

@alextran1502Here you go:#29445. Thanks for looking into it.

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

#### thinkhJul 2, 2026

 

-

Resolved. It wasn't an immich but a RAId/mount issue. ✅

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

### binnichtaktivJul 2, 2026

 

-

I have a question:I had to restore my iPhone from an one moth old backup. I uploaded all photos and videos to Immich so they are not lost.I want to have them back in my photos app on my phone locally but in the immich app I can’t find a way to download and save them to my phone. The „photos“ page in the immich app only shows the photos that are locally in my phone. I didn’t find a way to download the uploaded photos that are missing on my phone.Is it just not possible or did I miss something? When I go to immich in my browser I see all photos

BetaWas this translation helpful?Give feedback.

 

1

 
You must be logged in to vote

 

All reactions

 5 replies
 

 

Comment options

 

Quote reply

#### alextran1502Jul 2, 2026MaintainerAuthor

 

-

you can download individual photos, we don't have bulk download option on the mobile app yet

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

 

edited

#### binnichtaktivJul 2, 2026

 

-

you can download individual photos, we don't have bulk download option on the mobile app yet

Okay that’s fine thanks. But where can I find the individual photos tho? I don’t see them in the „photos“ page

Another question I have:Every photo in image shows that the image isn’t uploaded yet (cloud with a line trough it). But I did upload them all. I just had to restore my phone so immich probably doesn’t know that I already uploaded them. Is there a way to refresh this?

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

#### binnichtaktivJul 2, 2026

 

-

@alextran1502pls help me if you have time 🥲

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

#### bondeabhijeetJul 3, 2026

 

-

So for your first question, you'll have to use the web to get those assets or you can get them from the location that the assets are stored on the server side.

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

 

edited

#### bondeabhijeetJul 3, 2026

 

-

For your second question (if i understood your situation correctly) , that icon probably means the Immich app’s local backup state got reset when the phone was restored that does not mean that the photos aren’t on the server. First check Immich Web to confirm the photos are there. Then in the mobile app, reselect the backup albums and let backup run again Immich should scan/check the files and skip ones that already are present on the server (it will automaticallyskip duplicates. If the icons still don’t update, try logging out/in or reinstalling the app so that it rebuilds its local index.

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

### julessandozJul 2, 2026

 

-

Thank you all for the hard work! Excited to try it out!

BetaWas this translation helpful?Give feedback.

 

1

 
You must be logged in to vote

 

All reactions

 0 replies
 

 

Comment options

 

Quote reply

### IoSonoAndreaZJul 2, 2026

 

-

I want to try the new real-time transcoding and I enabled it, but I suppose I should delete all the transcoded videos already done, am I right? how?

BetaWas this translation helpful?Give feedback.

 

1

 
You must be logged in to vote

 

All reactions

 4 replies
 

 

Comment options

 

Quote reply

#### alextran1502Jul 2, 2026MaintainerAuthor

 

-

Please note that this feature is still experimental and can change behavior from version to version. It's currently only implemented in the web app, with the mobile app implementation in progress.

To enable real-time transcoding, go to thevideo transcoding settings(scroll down). Offline transcoding isn't directly affected by enabling it, so if you'd like to disable offline transcoding, you should also adjust the transcode policy.

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

#### IoSonoAndreaZJul 2, 2026

 

-

Please note that this feature is still experimental and can change behavior from version to version. It's currently only implemented in the web app, with the mobile app implementation in progress.

To enable real-time transcoding, go to thevideo transcoding settings(scroll down). Offline transcoding isn't directly affected by enabling it, so if you'd like to disable offline transcoding, you should also adjust the transcode policy.

ok, but still remains the question: how to delete all transcoded videos and free up space? should I manually delete the files or there is a better way?

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

#### alextran1502Jul 2, 2026MaintainerAuthor

 

-

You still need transcoded videos to use with the mobile app since real-time transcoding is not supported on the mobile app yet.

To answer your questions, manually delete is the only way right now but I advise against it

BetaWas this translation helpful?Give feedback.

 
👍

1

 

 

All reactions

 

Comment options

 

Quote reply

#### jrasm91Jul 2, 2026Maintainer

 

-

There is a plan to have the system automatically delete transcoded videos once the feature is done, so I'd just wait for that to be finished and then it'll happen automatically.

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

### vipotaenko02Jul 2, 2026

 

-

Thanks for making transcoding videos on the fly! I have a question, would it be possible to make HEIC photos convert to JPG on the fly too? That would be extremely useful on PCs that can’t view HEIC images in browsers.

BetaWas this translation helpful?Give feedback.

 

3

 
You must be logged in to vote

 

All reactions

 1 reply
 

 

Comment options

 

Quote reply

#### alextran1502Jul 2, 2026MaintainerAuthor

 

-

we don't have plan for that. Generated thumbnail we have at the moment is compatible with all browsers and client (JPEG/WEBP)

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

### isaacolsen94Jul 2, 2026

 

-

First, thank you all for your hard work! It's so nice to have a polished alternative for photos!

Second, does the new android backup improvements help with large images/photos over 100mb? I know it's cloudflare's limit, but didn't know if these improvements would help.

BetaWas this translation helpful?Give feedback.

 

1

 
You must be logged in to vote

 

All reactions

 1 reply
 

 

Comment options

 

Quote reply

#### alextran1502Jul 2, 2026MaintainerAuthor

 

-

No, the improvement is for the background job to run periodically in the background more often

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

### MrCyberSentinelJul 2, 2026

 

-

Just Love The Project💖💖💖

BetaWas this translation helpful?Give feedback.

 

2

 
You must be logged in to vote

 

All reactions

 0 replies
 

 

Comment options

 

Quote reply

### yann117Jul 2, 2026

 

-

More questions onReal-time Transcoding

1. First, I see it is using/applying theHardware Accelerationsettings, but on the opposite it doesn't seems to applyEncoding Optionsat all? WhateverVideo CodecI choose (in my case I would choose either x264 or x265), it seems to force encoding toAV1-> I see this flag in the log-c:v av1_qsv
2. Then, on my Intel Raptor Lake (gen12 I think), using hardware acceleration with either VAAPI or Quick Sync is crashing, possibly because RPL doesn't support hardware encoding for AV1

BetaWas this translation helpful?Give feedback.

 

1

 
You must be logged in to vote

 

All reactions

 4 replies
 

 

Comment options

 

Quote reply

#### mertalevJul 2, 2026Maintainer

 

-

1. The client chooses the codec, not the server. Clients with AV1 decode will gravitate toward it since the server advertises AV1 variants.
2. Yes, we'll add configuration so you can choose which codecs and resolutions the server advertises, so the client only sees options that the server can actually handle.

BetaWas this translation helpful?Give feedback.

 
👍

1

 

 

All reactions

 

Comment options

 

Quote reply

#### kingp0ddJul 2, 2026

 

-

Really looking forward to RTT for mobile. I think that's where it's really used by people.

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

#### yann117Jul 3, 2026

 

-

Yes, I tried the cast on web as a preview/test, but indeed that is not the real scenario I'm waiting for too.My ultimate wish/dream is:

* Realtime Transcoding
* RT applied in mobile casting

The reason is that all my videos are reencoded in AV1 (way better quality/size) but unfortunately many TVs / devices don't support it. So when trying to show my stuff to friends it always fails for video.

Chromecast + realtime transcoding would finally solve that issue.

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

#### etnoyJul 3, 2026Maintainer

 

-

Yes, I tried the cast on web as a preview/test, but indeed that is not the real scenario I'm waiting for too. My ultimate wish/dream is:

* Realtime Transcoding
* RT applied in mobile casting

The reason is that all my videos are reencoded in AV1 (way better quality/size) but unfortunately many TVs / devices don't support it. So when trying to show my stuff to friends it always fails for video.

Chromecast + realtime transcoding would finally solve that issue.

Better casting is already on my todo list! We need to rewrite cast entirely and also add RTT :)

BetaWas this translation helpful?Give feedback.

 
❤️

1

 

 

All reactions

 

Comment options

 

Quote reply

### compblJul 2, 2026

 

-

Getting this error after upgrading. Looks like the server cant start the microservices service (?)

�Starting microservices worker2026-07-02 23:50:31���Error: No vector extension found. Available extensions: vchord, vector2026-07-02 23:50:31at getVectorExtension (/usr/src/app/server/dist/repositories/database.repository.js:51:15)2026-07-02 23:50:31at process.processTicksAndRejections (node:internal/process/task_queues:104:5)2026-07-02 23:50:31at async /usr/src/app/server/dist/services/database.service.js:62:312026-07-02 23:50:31at async /usr/src/app/server/dist/repositories/database.repository.js:376:272026-07-02 23:50:31at async /usr/src/app/server/node_modules/.pnpm/kysely@0.28.17/node_modules/kysely/dist/cjs/kysel2026-07-02T23:50:31.786Z y.js:541:202026-07-02 23:50:31at async DefaultConnectionProvider.provideConnection (/usr/src/app/server/node_modules/.pnpm/kysely@0.28.17/node_modules/kysely/dist/cjs/driver/default-connection-provider.js:12:20)2026-07-02 23:50:31at async /usr/src/app/server/dist/repositories/database.repository.js:373:132026-07-02 23:50:31��zmicroservices worker error: Error: No vector extension found. Available extensions: vchord, vector, stack: Error: No vector extension found. Available extensions: vchord, vector2026-07-02 23:50:31at getVectorExtension (/usr/src/app/server/dist/repositories/database.repository.js:51:15)2026-07-02 23:50:31at process.processTicksAndRejections (node:internal/process/task_queues:104:5)2026-07-02 23:50:31at async /usr/src/app/server/dist/services/database.service.js:62:312026-07-02 23:50:31at async /usr/src/app/server/dist/repositories/database.repository.js:32026-07-02T23:50:31.795Z 76:272026-07-02 23:50:31at async /usr/src/app/server/node_modules/.pnpm/kysely@0.28.17/node_modules/kysely/dist/cjs/kysely.js:541:202026-07-02 23:50:31at async DefaultConnectionProvider.provideConnection (/usr/src/app/server/node_modules/.pnpm/kysely@0.28.17/node_modules/kysely/dist/cjs/driver/default-connection-provider.js:12:20)2026-07-02 23:50:31at async /usr/src/app/server/dist/repositories/database.repository.js:373:132026-07-02 23:50:31�<microservices worker exited with code 12026-07-02 23:50:31Killing api process

BetaWas this translation helpful?Give feedback.

 

1

 
You must be logged in to vote

 

All reactions

 2 replies
 

 

Comment options

 

Quote reply

#### bondeabhijeetJul 3, 2026

 

-

what is in your docker-compose.yml file?

BetaWas this translation helpful?Give feedback.

 

All reactions

 

Comment options

 

Quote reply

#### compblJul 3, 2026

 

-

Got it fixed... All good

BetaWas this translation helpful?Give feedback.

 
👍

1

 

 

All reactions

 

Comment options

 

Quote reply

### X-lemJul 3, 2026

 

-

O wow! Huge release. tbh I'm most excited for

Upload asset directly to album on the mobile app

BetaWas this translation helpful?Give feedback.

 

1

 
You must be logged in to vote

 

All reactions

 0 replies
 

 

Comment options

 

Quote reply

 

edited

### waclaw66Jul 3, 2026

 

-

A remark to the new checksum mismatch check. In the past I've edited already uploaded images to Immich outside Immich, thefore there are hunderts of images with checksum mismatch. It would be helpful to have a function that resolves that mismatch by a new checksum recalculation. Thanks.Delete all function for missing files doesn't work at all. They are deleted from the list, but reappears after return. Single file delete works fine.Running recheck was probably blocking Delete all. It's not visible that the task is running in the background.

BetaWas this translation helpful?Give feedback.

 

1

 
You must be logged in to vote

 

All reactions

 0 replies
 

 

Comment options

 

Quote reply

### kosukesandoJul 3, 2026

 

-

In regards to the VectorChord migration, I think there should be a warning for people from prior to thev1.102 releasewhere it first mentions anopt-inforDB_DATA_LOCATION. I don't recall ever seeing this becoming the default as opposed to an opt-in, so some users like me haven't had the chance to change over to this setup. A simple backup and restore of the database does the trick, but a little reminder wouldn't hurt.

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