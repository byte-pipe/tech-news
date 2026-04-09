---
title: Release v2.0.0 · syncthing/syncthing · GitHub
url: https://github.com/syncthing/syncthing/releases/tag/v2.0.0
site_name: lobsters
fetched_at: '2025-08-12T23:07:11.767896'
original_url: https://github.com/syncthing/syncthing/releases/tag/v2.0.0
date: '2025-08-12'
description: Open Source Continuous File Synchronization. Contribute to syncthing/syncthing development by creating an account on GitHub.
tags: distributed, release
---

syncthing



/

syncthing

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork4.7k
* Star74.5k



# v2.0.0

Latest

Latest


Compare


Loading

st-release

 released this



 12 Aug 06:13


 ·


 3 commits


 to main
 since this release


 v2.0.0


5d80333


## ⚠️First 2.0 release⚠️

This is the first release of the new 2.0 series. Expect some rough edges and keep a sense of adventure! 🙏

## Major changes in 2.0

* Database backend switched from LevelDB to SQLite. There is a migration onfirst launch which can be lengthy for larger setups. The new database iseasier to understand and maintain and, hopefully, less buggy.
* The logging format has changed to use structured log entries (a messageplus several key-value pairs). Additionally, we can now control the loglevel per package, and a new log level WARNING has been inserted betweenINFO and ERROR (which was previously known as WARNING...). The INFO levelhas become more verbose, indicating the sync actions taken by Syncthing. Anew command line flag--log-levelsets the default log level for allpackages, and theSTTRACEenvironment variable and GUI has been updatedto set log levels per package. The--verboseand--logflagscommandline options have been removed and will be ignored if given.
* Deleted items are no longer kept forever in the database, instead they areforgotten after six months. If your use case require deletes to takeeffect after more than a six month delay, set the--db-delete-retention-intervalcommand line option or correspondingenvironment variable to zero, or a longer time interval of your choosing.
* Modernised command line options parsing. Old single-dash long options areno longer supported, e.g.-homemust be given as--home. Some optionshave been renamed, others have become subcommands. All serve options arenow also accepted as environment variables. Seesyncthing --helpandsyncthing serve --helpfor details.
* Rolling hash detection of shifted data is no longer supported as thiseffectively never helped. Instead, scanning and syncing is faster and moreefficient without it.
* A "default folder" is no longer created on first startup.
* Multiple connections are now used by default between v2 devices. The newdefault value is to use three connections: one for index metadata and twofor data exchange.
* The following platforms unfortunately no longer get prebuilt binaries fordownload at syncthing.net and on GitHub, due to complexities related tocross compilation with SQLite:dragonfly/amd64illumos/amd64 and solaris/amd64linux/ppc64netbsd/*openbsd/386 and openbsd/armwindows/arm
* dragonfly/amd64
* illumos/amd64 and solaris/amd64
* linux/ppc64
* netbsd/*
* openbsd/386 and openbsd/arm
* windows/arm
* The handling of conflict resolution involving deleted files has changed. Adelete can now be the winning outcome of conflict resolution, resulting inthe deleted file being moved to a conflict copy.

This release is also available as:

* APT repository:https://apt.syncthing.net/
* Docker image:docker.io/syncthing/syncthing:2.0.0orghcr.io/syncthing/syncthing:2.0.0({docker,ghcr}.io/syncthing/syncthing:2to follow just the major version)

## What's Changed

### Fixes

* fix(db): handle large numbers of blocks in update by@calmhin#10025
* fix(syncthing): make directory flags global for all commands by@calmhin#10028
* fix(sqlite): apply options by@pixelsparkin#10049
* fix(db): version vector serialisation :( by@calmhin#10050
* fix(model): loop-break regression while block copying in puller by@imsodinin#10069
* fix(model): close fd immediately in copier by@imsodinin#10079
* fix(model): use same folder first in copier by@imsodinin#10093
* fix(model): correct bufferpool handling; simplify by@calmhin#10113
* fix(protocol): avoid deadlock with concurrent connection start and close by@calmhin#10140
* fix(syncthing): avoid writing panic log to nil fd by@ardevdin#10154
* fix(fs): check for unsupported error on modern Windows (fixes#10164) by@rasain#10165
* fix(gui): don't show dial errors for paused devices (fixes#10166) by@marbens-archin#10167
* fix: track invalid files in LocalFlags to fix global count by@imsodinin#10170
* fix(watchaggregator): properly handle sub-second watch durations (fixes#9927) by@imsodinin#10179
* fix(db): remove invalid member from FileMetadata by@imsodinin#10180
* fix(model): avoid flashing "Sync Waiting" unnecessarily by@calmhin#10181
* fix(protocol): slightly loosen/correct ownership comparison criteria (fixes#9879) by@yparitcherin#10176
* fix(model): don't clobber local flags when receiving index by@calmhin#10190
* fix(beacon, osutil, upnp): fix local discovery send and intf detection on Android by@Catfriend1in#10196
* fix(pmp, netutil): workaround native code denied to discover gateway ipv4 addr on Android 14+ by@Catfriend1in#10204
* fix: allow deleted files to win conflict resolution by@calmhin#10207
* fix(gui): show revert buttons only when folder is idle (fixes#10191) by@tomasz1986in#10212
* fix(gui): fix identicon generation by@aionescuin#10228
* fix(model): properly set folder state "syncing" when copying data by@calmhin#10227
* fix(slogutil): quote values with parentheses in them by@calmhin#10229
* fix(test): remove lib/logger from testmocks target by@rasain#10231
* fix: correct logging of our ID after startup & generate by@calmhin#10234

### Features

* feat: addsyncthing debug database-statisticscommand by@calmhin#10117
* feat(config): enable multiple connections by default by@calmhin#10151
* feat(config): expose folder and device info as metrics (fixes#9519) by@calmhin#10148
* feat: use Ed25519 keys for sync connections by@calmhin#10162
* feat(gui): add option to limit bandwidth in LAN to Settings (ref#10046) by@tomasz1986in#10182
* feat(connections, nat): add UDP portmapping/pinhole for QUIC (fixes#7403) by@marbens-archin#10171
* feat: add debug commands for folder counts and files by@calmhin#10206
* feat(ignore): add .stignore escaping on Windows by@rasain#10205
* feat: switch logging framework by@calmhin#10220

### Other

* chore: remove abandoned next-gen-gui experiment by@calmhin#10004
* chore: remove weak hashing which does not pull its weight by@calmhin#10005
* chore: switch database engine to sqlite (fixes#9954) by@calmhin#9965
* chore: harmonise command line flags by@calmhin#10007
* chore(db): increase journal limit to 64MiB by@bt90in#10022
* chore: forget deleted files older than six months (fixes#6284) by@calmhin#10023
* chore(db): use shorter read transactions and periodic checkpoint for smaller WAL by@calmhin#10027
* chore: configurable delete retention interval by@calmhin#10030
* chore(db): fix debug logging by@bt90in#10033
* chore(db): buffer pulled files for smaller WAL by@calmhin#10036
* chore(db): use one SQLite database per folder by@calmhin#10042
* chore(model): delay starting a pull while there are incoming index updates by@calmhin#10041
* chore(syncthing): remove "default" folder concept by@calmhin#10068
* chore(syncthing): ensure migrated database is closed before exiting by@xjtdy888in#10076
* chore(db, model): simplify per hash DB lookup in copier by@imsodinin#10080
* chore(model): refactor copier for more flatness by@imsodinin#10094
* build: upgrade setup-zig action by@calmhin#10134
* build: properly propagate build tags to Debian build by@calmhin#10144
* chore(protocol): don't start connection routines a second time by@imsodinin#10146
* chore(protocol): only allow enc. password changes on cluster config by@imsodinin#10145
* chore: various linter fixes by@calmhin#10157
* build: streamline gathering of facts, checkouts by@calmhin#10158
* build: build both Debian armel and armhf (though they are the same for us) by@calmhin#10159
* build: explicitly trigger build after pushing release tag by@calmhin#10160
* chore(syncthing): ensure response body is closed in upgrade request by@ardevdin#10169
* refactor(syncthing): use named constant for SIGHUP by@ardevdin#10168
* chore(model): remove redundant removal of internal fields in indexsender by@imsodinin#10173
* chore: add migration for remote invalid local flag by@imsodinin#10174
* chore(config): increase max concurrent writes default by@imsodinin#10200
* chore(gui): added spacing between folder name and error message by@ardevdin#10201
* build: unset build ID in generated binaries by@Catfriend1in#10203
* chore(protocol): minor cleanup of ClusterConfig messages; remove DisableTempIndexes option by@calmhin#10202
* refactor(beacon, osutil, upnp, netutil): only use anet on Android by@marbens-archin#10211
* chore(gui): fix "Shut Down" spelling in Actions by@tomasz1986in#10213
* chore(gui): update fancytree from 2.38.0 to 2.38.5 (ref#10051, ref#10155) by@tomasz1986in#10214
* chore(config): remove fallback STUN servers that are CNAMEs to stun.counterpath.com by@marbens-archin#10219
* chore(scanner): reduce memory pressure by using pools inside hasher by@danogin#10222
* chore(fs): slightly reduce memory usage of IsParent by@danogin#10223
* refactor(scanner): use recommended pattern for slice pool by@danogin#10225
* chore(slogutil): ensure quoting of empty and confusing log values by@calmhin#10236
* chore: remove GUI "debugging" toggle, debug HTTP metrics by@calmhin#10235
* chore(gui): remove redundant "authenticated" conditions from Actions menu (#10235) by@tomasz1986in#10237

## New Contributors

* @ardevdmade their first contribution in#10154
* @yparitchermade their first contribution in#10176
* @danogmade their first contribution in#10222

Full Changelog:v1.30.0...v2.0.0



### Contributors

 calmh, pixelspark, and 11 other contributors




Assets

35




Loading

### Uh oh!

There was an error while loading.Please reload this page.






👍

69


239, hawcgn, BrammyS, guguss-31, mannp, itsutsu, meain, 7thgenerationdesign, mamgodev, xfzv, and 59 more reacted with thumbs up emoji


😄

11


hawcgn, guguss-31, itsutsu, meain, boxden, liuquanzhong, dot-Justin, WrobotGames, egeesin, g105b, and TzurSoffer reacted with laugh emoji


🎉

104


kkoyung, liigo, andrewbrereton, rubenbe, rahilarious, tomasz-c, Tonybxf, Dannecron, freshleafmedia, 239, and 94 more reacted with hooray emoji


❤️

36


GiorgioMendieta, liigo, Turhvjbufv, indaco, 239, hawcgn, robbymilo, guguss-31, 0xfeeddeadbeef, itsutsu, and 26 more reacted with heart emoji


🚀

34


GiorgioMendieta, liigo, andrewbrereton, davidetogni, GithubUser5462, tomasz-c, freshleafmedia, 239, hawcgn, guguss-31, and 24 more reacted with rocket emoji


👀

9


hawcgn, guguss-31, itsutsu, andruhov, boxden, liuquanzhong, dot-Justin, egeesin, and TzurSoffer reacted with eyes emoji



All reactions


164 people reacted
