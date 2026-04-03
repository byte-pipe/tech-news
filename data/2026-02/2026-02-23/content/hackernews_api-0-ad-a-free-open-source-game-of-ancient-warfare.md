---
title: 0 A.D. | A free, open-source game of ancient warfare
url: https://play0ad.com/new-release-0-a-d-release-28-boiorix/
site_name: hackernews_api
content_file: hackernews_api-0-ad-a-free-open-source-game-of-ancient-warfare
fetched_at: '2026-02-23T20:14:29.019348'
original_url: https://play0ad.com/new-release-0-a-d-release-28-boiorix/
author: jonbaer
date: '2026-02-19'
description: 0 A.D. is a free, open-source, historical Real Time Strategy (RTS) game currently under development by Wildfire Games, a global group of volunteer game developers.
tags:
- hackernews
- trending
---

Wildfire Games, an international group of volunteer game developers, proudly announces the release of 0 A.D. Release 28: “Boiorix”, the twenty-eighth version of 0 A.D., a free, open-source real-time strategy game of ancient warfare. The release is named after the king of the Cimbri Germanic tribeBoiorix.

## Easy download and install

Download and installation instructions are available for Windows, Linux, and macOS. 0 A.D. is free software. This means you can download, redistribute, modify andcontributeto the application under the same licenses: GNU Public Licence version 2 (GPL v2) for code and Creative Commons Attribution Share-Alike 3.0 (CC-BY-SA 3.0) for artwork. Although you might find some people selling copies of 0 A.D., either over the internet or on physical media, you will always have the option todownload 0 A.D.completely gratis, directly from the developers. No “freemium” model, no in-game advertising, no catch.





Don’t forget to deactivate every mod before updating the game to avoid any risk of conflict. If you’re a mod creator, please look atthis pageon how to port your mod to the new version. As always, feel free to reach out to us for assistance.

## Now is the time to contribute!

The Release 28 is our first release without the Alpha label: our development process has matured, our releases are more frequent, and our commitment to quality has never been higher.Now is the time to join us and place 0 A.D. in the spotlight. We need your help to make the game flourish and to bring new features to life.

As you can see, this release unfortunately comes without a video trailer. It is difficult for the current team to spread the word about our beloved game. We are in sore need of contributors in the following areas:

* Video Editing
* Social Media Management
* Website Design

Of course, we are also always looking for, and providing a welcoming contribution environment, for:

* Testers and Quality Assurance enthusiasts
* Translators (get started right away onTransifex)
* and of course, Developers and Artists – the team will gladly welcome contributions in all areas.

You can also support us by simply donating. This allows us to pay the server hosting fees for our multiplayer, websites, and development environments.

## A new faction: the Germans

Terror Germanicus, the fear of the Germanic tribes migrating south, from the Jutland region, towards the Roman Republic, is coming to 0 A.D. in Release 28.

The Cimbri were a large group of Germanic peoples originally from the north of modern-day Denmark. In the late 2nd century BC, their migration south into Italy and France would spark the decade-long Cimbrian War against the Roman Republic. Accompanied by powerful armies and seeresses, Germanic convoys, in long trains of wagons, brought livestock, shelter and goods. The Cimbri placed great importance on animals for religious sacrifices.

In 0 A.D., we represent the nomadic coalition formed between the Cimbri, the Teutones, the Ambrones, and other Celto-German tribes simply as the "Germans". The Germans are a semi-nomadic civilization with a flexible economy owing to Supply Wagons and Wagon Encampments, which can be fortified. The unique technologies "Wagon Trains" and "Migratory Resettlement" lean into this flexibility, reducing dependence on territorial boundaries. The Germans also feature an aggressive lineup of siege units, with a crush-dealing unit available in each phase. Between their economic flexibility and unique military units, Cimbrian raiders, Log Rams, and Seeresses, the Germans are a mysterious force to be reckoned with.

Play with this new faction, against their historical Roman foes, or turn history around by making them battle the 14 other factions of the game. Many other novelties await you in the new release of 0 A.D.!

## Top new features of Release 28

* Gendered Civilians
* Direct Font Rendering
* Support for JavaScript Modules
* New Game-Setup Options
* Lobby improvements
* Engine upgrades and updated platform support
* New quotes and tips
* Various balancing improvements
* … and much more!

## Gendered Civilians

In an effort to improve historical consistency, we have replaced the visual appearance of civilian units. Previously described as a "female citizen", the basic economic unit is now called the "civilian" and has male and female models.

This enhancement was made possible by incremental improvements of the engine, which now allows a unit to have variants not only in its appearance, but also in its voice and in other gendered characteristics.

In the civilizations displayed in the game, women did not usually hold citizenship, which was a prized social status. The "female citizen" was a misnomer. It was also incorrect to display all men as soldiers, and most women as servants. Instead, we want to describe the armies of 0 A.D. as followed by a group of minions of lower social status, able to support the soldiers in the army camp, but not on the battlefield. Those are the new Civilians. Citizens, on the other hand, were soldiers, able to wage war as well as working, which we have always been accurately describing in the game with the citizen-soldier concept. The ambiguity of the term "citizen" is removed: this word now only describes citizen soldiers.

This change does not touch the balance of the game at all.The so-called "female citizens" keep all their statistics, only their appearance and name have changed. The citizen soldiers are not touched at all.

## Direct Font Rendering

In order to display text, we used to pre-render fonts and load them into memory when starting the game. In order to display scripts such as Chinese, we needed to load a large atlas of thousands of characters into memory, which could overwhelm the players' RAM. As a consequence, we were forced to provide East Asian languages as mods, which was an accessibility issue for non-English speaking users of these languages.

On top of memory management improvements, we now use the Freetype library in the engine to render fonts on the fly when the game runs. Modding the fonts also becomes far easier with this new feature.

This new rendering system also improves the text display with GUI scaling, for users with Hi-DPI screens or who simply wish to use a larger interface.

In the future, we hope to also use this feature to render ancient scripts, such as hieroglyphs and cuneiform.

## New Game-Setup Options

New personalization options are available in the game setup screen.

You can remove some players entirely (removing all of the initial buildings and units in their starting zone) in Skirmish and Scenario games.

It is also possible to set the population limit per team:

Lastly, some code refactoring allowed us to fix outstanding bugs in the game setup. For instance, in Alpha 27, a recurring issue would create an unwanted flood event in games where the user had previously played a flood game. This issue has been fixed.

## Lobby improvements

The multiplayer lobby received some quality of life improvements. Verifying TLS certificates is now enabled by default when connecting to the multiplayer lobby, reducing the risk of man-in-the-middle attacks. A secure connection to the lobby will become mandatory in future releases, so please check that TLS encryption and certificate verification are not disabled in your settings, and report any issue you may encounter.

It is also more straightforward now to host matches, as there is no need to decide whether to use STUN or not; and a bug causing freezes when joining a match got fixed.

We have decided to rename the main menu entry for playing with friends over LAN or by direct IP: now calledMultiplayer > Connect by IP, it is still the same system for direct matchmaking without using the lobby.

## Engine upgrades and updated platform support

In Release 28, we have upgraded the SpiderMonkey JavaScript engine to version 128. This upgrade drops support for Windows 7 and 8.1, and for macOS below 10.15. Windows 10 and 11 are now the only supported Windows versions, and we will try our best to keep supporting Windows 10 as long as possible.

Still on Windows, we now provide a long-awaited 64-bit build, which should address infrequent out-of-memory errors. The 64-bit version will become the default one for the next release, and the 32-bit build will eventually be deprecated in the future.

On Linux distributions, special care is always given to release bundles for package maintainers, but we also walked the extra mile to provide an AppImage in official releases, starting with Release 28. We are also working close together with maintainers of theSnapandFlatpakversions, so that you can enjoy the latest release as soon as we get it out.

## New quotes and tips

Our contributor manowar has brought gifts for the history nerds among you with a dozen new quotes in the game load screen, and, together with Vantha, they have added new tips for both beginners and seasoned players.

## Balancing improvements

### General

#### Capturing

* Structure, Civil Center, and Fortress default (ungarrisoned) capture resistance increased from 0.5, 5, 10, to 5, 30, and 45, respectively.
* Civilians (formerly Women) given a capture attack of 1.0.

#### Naval Warfare

* Naval technology tree simplified.
* Scout ships made available in Village phase.
* Ship balancing: Ram ships, scout ships nerfed; Fire ships, arrow ships buffed.Scout shipsrange 37 (from 45).Fire ships175 wood, 50 food, 50 metal -> 100 wood, 0 food, 50 metal.Arrow ships120 wood, 100 metal -> 100 wood, 100 metal, acceleration increased by 25%.Ram ships350 hack, 70 crush damage -> 320 hack, 50 crush damage.

#### Group Movement

* Units' destinations are distributed around the endpoint, allowing groups to move cohesively without colliding and forming long lines.

#### Champion Cavalry

* Melee Champion Cavalry HP decreased from 300 to 260.
* Cataphract Champion Cavalry +2 Hack and Pierce armor, but speed decreased from 17.1 to 14.4.

#### Miscellaneous

* 3 traders are no longer required for researching Diaspora.
* Fortress accuracy increased from 2.0 to 1.25.
* Elephants +1 pierce armor, +0.5m splash range.
* Longsword champions +2 splash hack damage damage, but -2 direct hack damage.

### Faction-specific

#### Carthage

* New civilization bonus: Stone gathering storehouse technologies are free and instant with each phase.
* Mercenary refactoring and differentiation. TheCeltic embassytrains sword cavalry and infantry.TheIberian embassytrains unique ranged infantry mercenaries. TheItalic embassytrains spear cavalry and infantry.
* New civilization bonus: Numidian cavalry +10% movement speed.

#### Han – Minister rework

* Minister attack removed.
* Minister garrison aura and ministry garrison aura removed.
* Minister economy and building auras increased from 2% to 10%, but ranged reduced from 40 meters to 20 meters. This is no longer stackable.
* Minister health and armor reduced to 50 HP, 2 hack, 2 pierce armor.
* Ministers and Ministry available in village phase instead of town phase.
* Ministry cost reduced from 200 stone, 200 metal to 50 wood, 200 stone, 50 metal.
* Reduced cost of ministry technologies.
* Ministry resource trickle removed.

#### Mauryas

* Mauryan maiden archers and swordsmen differentiation.
* Maiden archers increased movement speed, decreased range, decreased damage, increased poison damage, cost reduced to 100 wood 90 metal.
* Maiden guard increased movement speed, decreased health, decreased pierce armor, increased hack armor, cost reduced to 100 food 90 metal.

## Full list of changes

The full list of changes can be found atthe changelog page of the wiki.

## Team Changes

After numerous contributions in many areas of the game, especially the user interface and the game simulation,Vanthahas joined the team at the beginning of the preparation of Release 28. We are extremely happy to welcome him!

## Reporting issues

If you experience a technical problem with the game, please report it at gitea.wildfiregames.com. This is also the first address to visit when you wish to dedicate some of your time to help patch the code. Got any further questions or suggestions? Discuss them with other players and developers at the forum or talk with us directly in the IRC chat rooms: #0ad and #0ad-dev on QuakeNet.

## Subscribe

See ourLinkTree. For press/media inquiries, please DM play0ad@mastodon.social on Mastodon, or email webmaster at wildfiregames dot com.
