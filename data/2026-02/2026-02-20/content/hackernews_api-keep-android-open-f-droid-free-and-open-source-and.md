---
title: Keep Android Open | F-Droid - Free and Open Source Android App Repository
url: https://f-droid.org/2026/02/20/twif.html
site_name: hackernews_api
content_file: hackernews_api-keep-android-open-f-droid-free-and-open-source-and
fetched_at: '2026-02-20T19:19:25.440193'
original_url: https://f-droid.org/2026/02/20/twif.html
author: LorenDB
date: '2026-02-20'
description: This Week in F-Droid TWIF curated on Friday, 20 Feb 2026, Week 8 F-Droid core During out talks with F-Droid users at FOSDEM26 we were baffled to learn most w...
tags:
- hackernews
- trending
---

### This Week in F-Droid

### TWIF curated on Friday, 20 Feb 2026, Week 8

#### F-Droid core

During out talks with F-Droid users atFOSDEM26we were baffled to learn most were relieved that Google has canceled their plans to lock-down Android.

Why baffled?Because no such thing actually happened, the plans announced last August are still scheduled to take place. We see a battle of PR campaigns and whomever has the last post out remains in the media memory as the truth, and having journalists just copy/paste Google posts serves no one.

But Google said…Said what? That there’s a magical “advanced flow”? Did you see it? Did anyone experience it? When is it scheduled to be released? Was it part of Android 16 QPR2 in December? Of 16 QPR3 Beta 2.1 last week? Of Android 17 Beta 1? No? That’s the issue… As time marches on people were left with the impression that everything was done, fixed, Google “wasn’t evil” after all, this time, yay!

While we all have bad memories of “banners” as the dreaded ad delivery medium of the Internet, after FOSDEM we decided that we have to raise the issue back and have everyone, who cares about Android as an open platform, informed that we are running out of time until Google becomes the gate-keeper of all users devices.

Hence, thewebsiteand starting today our clients, with the updates ofF-DroidandF-Droid Basic, feature a banner that reminds everyone how little time we have and how to voice their concerns to whatever local authority is able to understand the dangers of this path Android is led to.

We are not alone in our fight,IzzyOnDroidadded a banner too, more F-Droid clients will add the warning banner soon and other app downloaders, likeObtainium, already have an in-app warning dialogue.

RegardingF-Droid Basicrewrite, development continues with a new release2.0-alpha3:

* Updated Translations
* Export installed apps list as CSV
* Add install history feature
* Add mirror chooser setting
* Add prevent screenshots setting
* Show tool-tips for all app bar buttons
* Create 3-dot overflow menu for My Apps for less frequently used actions
* Persist sort order of My Apps
* Adapt strings according to Material Design 3 guidelines
* Apply string suggestions (Thanks Lucas)
* Fix missing icon bug in pre-approval dialog

Note that if you are already using F-Droid Basic version1.23.x, you won’t receive this update automatically. You need to navigate to the app inside F-Droid and toggle “Allow beta updates” in top right three dot menu.

In apps news, we’re slowly getting back on track with post Debian upgrade fixes(if your app still uses Java 17 is there a chance you can upgrade to 21?)and post FOSDEM delays. Every app is important to us, yet actions like the Google one above waste the time we could have put to better use in Gitlab.

#### Community News

Buseswas updated to1.10after a two year hiatus.

ConversationsandQuicksywere updated to2.19.10+freeimproving on cleaning up after banned users, a better QR workflow and better tablet rotation support. These are nice, but another change raises our interest,“Play Store flavor: Stop using Google library and interface directly with Google Play Service via IPC”. Sounds interesting for your app too? Is this a path to having one single version for both F-Droid and Play that is fully FLOSS? We don’t know yet, but we salute any trick that removes another proprietary dependency from the code. If curious feel free to take a look atthe commit.

Dolphin Emulatorwas updated to2512. We missed one version in between so the changelogs are huge, luckily the devs publish highly detailed posts about updates. So we’ll start with“Release 2509”(about 40 mins to read), we side-track with“Starlight Spotlight: A Hospital Wii in a New Light”(for about 50 mins), we continue to the current release in“Release 2512”(40 more minutes)and we finish with“Rise of the Triforce”delving in history for more than one hour.

Image Toolboxwas updated to3.6.1adding many fixes and…some AI tools.Were you expecting such helpers? Will you use them?

Luantiwas updated to5.15.1addingsome welcomed fixes.If your game world started flickering after the last update make sure to update.

Nextcloud apps are getting an update almost every week, likeNextcloudwas updated to33.0.0,Nextcloud Cookbookto0.27.0,Nextcloud Devto20260219,Nextcloud Notesto33.0.0andNextcloud Talkwas updated to23.0.0.

But are you following the server side too?Nextcloud Hub 26 Winterwas just released adding a plethora of features. If you want to read about them, see the 30 minutes posthereor watch the one hour long video presentation from the teamhere.

ProtonVPN - Secure and Free VPNwas updated to5.15.70.0adding more control to auto-connects, countries and cities. Also all connections are handled now by WireGuard and Stealth protocols as the older OpenVPN was removed making the app almost 40% smaller.

Offiwas updated to14.0with a bit of code polish. Unfortunately for Android 7 users, the app now needs Android 8 or later.

QUIK SMSwas updated to4.3.4withmany fixes. ButVishalpraised the duplicate remover, the default auto de-duplication function and found that the bug that made deleted messages reappear is fixed.

SimpleEmailwas updated to1.5.4after a 2 year pause. It’s just a fixes release, updating translations and making the app compatible with Android 12 and later versions.

#### Removed Apps

##### 5 apps were removed

* Chord Shift: Shift plain text notes
* OpenAthena™ for Android: OpenAthena™ lets common drones spot precise locations
* Tibetan Keyboard: Keyboard for Tibetan script
* Tibetan Pad: Read Tibetan script
* Tomdroid: Note taker

#### Newly Added Apps

##### 1 app was newly added

* NeoDB You: A native Android app for NeoDB designed with Material 3/You

#### Updated Apps

##### 287 more apps were updated

 (expand for the full list)

* AAAAXYwas updated to1.7.12+20260209.3971.fc2186af
* Activity Managerwas updated to5.4.17
* addy.iowas updated tov5.9.2
* Alarmetricswas updated to2.4.0
* AliasVaultwas updated to0.26.4
* Amberwas updated to4.1.2
* AndroidCryptwas updated to2.0.2
* AndroidMicwas updated to2.2.5
* ANeko Rebornwas updated to1.6.1
* Anx Readerwas updated to1.12.0
* Arcticonswas updated to14.3.3
* Arcticons Blackwas updated to14.3.3
* Arcticons Day & Nightwas updated to14.3.3
* Arcticons Material Youwas updated to14.3.3
* Aurora Storewas updated to4.8.1
* AVNCwas updated to3.2.0
* Bangle.js Gadgetbridgewas updated to0.89.1-banglejs
* baresipwas updated to77.1.1
* baresip+was updated to65.1.1
* BeeCount Knitting Counterwas updated to2.7.5
* Binary Eyewas updated to1.68.0
* Birthday Adapterwas updated to3.11.4
* Blue Line Consolewas updated to1.2.24
* Bold Bitcoin Walletwas updated to2.1.15
* Booming Musicwas updated to1.2.1
* Breakout 71was updated to29519142
* Breezy Weatherwas updated to6.1.3_freenet
* Butterflywas updated to2.4.4
* CalcYouwas updated to4.0
* Calisthenics Memorywas updated to1.19.0
* CAPod - Companion for AirPodswas updated to3.0.5-rc0
* Capy Readerwas updated to2026.02.1195
* Carburoidwas updated to1.4.1
* Cartes IGNwas updated to3.4.7
* Cavitywas updated to1.11.0
* ccgtwas updated to1.53
* CClauncherwas updated tov10.6.2
* Celestiawas updated to1.9.9
* Chesswas updated to10.0.7
* CineLogwas updated to3.0.0
* Cirruswas updated to4.5
* Clash Meta For Androidwas updated to2.11.22.Meta
* CleanSlatewas updated to1.0.43
* Com-Phone Story Makerwas updated to1.8.2
* CoMaps - Hike, Bike, Drive Offline with Privacywas updated to2026.02.09-4-FDroid
* Commonswas updated to6.3.0
* Copy SMS Code - OTP Helperwas updated to1.20.4
* Critical Mapswas updated to3.1.0
* Crosswordwas updated to1.26
* CuteMusicwas updated to3.1.6
* DanXiwas updated to1.5.0
* DAVx⁵was updated to4.4.11
* Deeprwas updated to1.0.26
* Delta Icon Packwas updated to2.12.0
* DigiAgriAppwas updated to0.5.0
* DobbyVPNwas updated to1.1.15
* DoliDroidwas updated to3.0.69
* Droid Padwas updated to3.12.0
* DSub2000was updated to5.7.2
* DuckDuckGo Privacy Browserwas updated to5.266.0
* Dungeon Crawl Stone Soupwas updated to0.34.0
* DuressKeyboardwas updated to4.7
* Element Classicwas updated to1.6.50
* Element X - Secure Chat & Callwas updated to26.02.0
* Encointer Walletwas updated to1.18.11
* EnigmaDroidwas updated to1.7.2
* Ente Photos - Encrypted photo storagewas updated to1.3.13
* Escapepod - Podcast Playerwas updated to1.6.4
* Exclavewas updated to0.17.14
* F-Droid Build Statuswas updated to5.14.0
* FairEmailwas updated to1.2312
* FairScan – PDF Scannerwas updated to1.14.0
* Fedilabwas updated to3.36.1
* Feederwas updated to2.17.0
* Feeder (Play version)was updated to2.17.0
* FeedFlow - RSS Readerwas updated to1.10.0
* Fitness Calendarwas updated to2026.02.1
* Flarewas updated to1.2.1
* Flexifywas updated to2.1.50
* Fluffywas updated to4.1.2
* Fluxwas updated to3.0
* Food You - Calorie Tracker & Food Diarywas updated to3.4.3
* Forkgramwas updated to12.4.2.0
* Forkyzwas updated to78
* Fossify Calendarwas updated to1.10.3
* Fossify File Managerwas updated to1.6.1
* Fossify Gallerywas updated to1.13.1
* Fossify Launcher Betawas updated to1.10.0
* Fossify Music Playerwas updated to1.8.1
* Fossify Voice Recorder Betawas updated to1.7.1
* FossWalletwas updated to0.39.0
* FreeOTPwas updated to2.0.6
* Fucks Givenwas updated to1.1.0
* Fulguris Web Browserwas updated to2.0.9
* Gadgetbridgewas updated to0.89.1
* Gallery for PhotoPrismwas updated to1.42.1
* Game Counterwas updated to2.6.0
* Gauguinwas updated to0.48.3
* GCompriswas updated to26.0
* GDF HEMA Timerwas updated to1.1.2
* Geo Sharewas updated to5.16.0
* GeoWeatherwas updated to1.2.4
* Goals Tracker 24/7 - timeto.mewas updated to2026.02.15
* GPTMobilewas updated to0.7.2
* Grazer Linuxtagewas updated to1.8.27-glt-Edition
* Hammerwas updated to2.1.4
* Harpwas updated to1.5.0
* Hate It Or Rate Itwas updated to1.5.1
* HFUT-Schedulewas updated to4.19.3.5
* Home Medkitwas updated to1.9.3
* HTTP Request Shortcutswas updated to4.2.0
* Immichwas updated to2.5.6
* Immich Uploaderwas updated to2.1.0
* Inbox Pagerwas updated to8.0
* Infomaniak kDrivewas updated to5.12.3
* Infomaniak Mailwas updated to1.24.4
* Inter Profile Sharingwas updated to1.1
* Inure App Manager (Trial)was updated tobuild106.5.1
* IR Blaster Remotewas updated to2.0.14
* Jamiwas updated to20260214-01
* Jerboa for Lemmywas updated to0.0.85-gplay
* Jigsawwas updated to1.3.0
* K-9 Mailwas updated to16.1
* Kahonwas updated to0.19.6
* Kaiwas updated to1.7.0
* KashCalwas updated to23.0.0
* Kazumiwas updated to2.0.2
* KDE Connectwas updated to1.35.3
* Keep it upwas updated to1.10.0
* KeePassVaultwas updated to1.16.0
* kitshn (for Tandoor)was updated to2.0.4
* Knock on Portswas updated to2.1.0
* Launch - Minimalist Launcherwas updated to5.8
* Launch Chatwas updated to1.6.0
* LCTermwas updated to1.4.2
* Les Pas - Photo Album for Nextcloudwas updated to2.11.0
* LinkHubwas updated to2.0.7
* Linux Command Librarywas updated to3.5.11
* Linwood Butterfly Nightlywas updated to2.4.4
* Lissen: Audiobookshelf clientwas updated to1.8.10
* Little Relaywas updated to1.5.0
* Loggerwas updated to3.4.2
* LRC Editorwas updated to3.2.7
* Lux Alarmwas updated to2.1.0
* MakeACopywas updated to3.2.0
* MateDroidwas updated to1.0.0
* Mattermost Betawas updated to2.37.0
* MediLog (Non-reproducible build)was updated to3.6.3
* MediLog (Reproducible build)was updated to3.6.3
* MedTimerwas updated to1.22.4
* Mental Mathwas updated to20
* Middorwas updated to0.1.7
* Millwas updated to7.2.5
* Mindustrywas updated to8-fdroid-155.4
* monocles chatwas updated to2.1.2
* MOROway Appwas updated to10.3.12
* Musifywas updated to9.8.1
* My Quran - قرآنيwas updated to1.4.4
* Myne: Download & Read eBookswas updated to4.7.2
* NATINFo+was updated to1.1.2
* Navitwas updated tov0.5.7
* NeoStumblerwas updated to2.3.1
* neutriNote CEwas updated to4.6.0e
* NewPipewas updated to0.28.3
* NFC Radiowas updated to0.17.0-fdroid
* nospeakwas updated tov0.11.1
* NotallyX - Quick Notes/Taskswas updated to7.7.0
* NotiFilterwas updated to4.4.0
* Oinkoinwas updated to1.4.2
* Olauncherwas updated tov6.2.18
* Open Passkey Authenticatorwas updated to2.0.2
* OpenBiblewas updated to3.0.3
* OpenContactswas updated to32.0
* openHABwas updated to3.19.4
* openHAB Betawas updated to3.19.3-beta
* OpenMoneyBoxwas updated to3.5.1.8
* OpenTracks (Non-reproducible)was updated tov4.26.0irreproducible
* OpenTracks (Reproducible build)was updated tov4.26.0
* Organic Maps・Offline Map & GPSwas updated to2026.02.18-5-FDroid
* Orgrowas updated to2.0.16
* OSMTrackerwas updated to2026.02
* oxproxionwas updated to2.1.35
* P.CASH Crypto Walletwas updated to0.51.14
* Paganwas updated to1.8.1
* PAIesquewas updated to36
* Parcelwas updated to1.5.0
* PariDroidwas updated to2.17.3.2.5
* PassVaultwas updated to1.9.0-beta1
* Passy - cross-platform password managerwas updated to1.10.0
* PCAPdroidwas updated to1.9.0
* PennyWise AIwas updated to2.15.46
* Phonograph Pluswas updated to1.11.5
* Pie Launcherwas updated to1.24.2
* PlainApp: File & Web Accesswas updated to2.2.0
* plees-trackerwas updated to26.2
* PocketCheckwas updated to1.5.3
* Podcini.X - Podcast instrumentwas updated to10.9.3
* Pomodorotwas updated to0.13.3
* Power Ampache 2was updated to1.01-87-fdroid
* Prayer modewas updated to1.6
* Proton Authenticatorwas updated to1.3.6
* Proton Pass: Password Managerwas updated to1.37.2
* QuickTile Settingswas updated to1.2.0
* QuickWeatherwas updated to2.8.7
* Quillpadwas updated to1.5.11
* Quotes.appwas updated to4.2
* Railway station photoswas updated to16.4.0
* Rank-My-Favswas updated to0.6.19
* Ringdroid - Ringtone editorwas updated to2.9.4
* RSAFwas updated to3.33
* Rufflewas updated to0.260216
* RunnerUpwas updated to2.10.0.3
* Running Services Monitorwas updated to1.0.22
* Saberwas updated to1.31.1
* Sapiowas updated to1.13.0
* Screenshot Tile (NoRoot)was updated to2.17.0
* Sensor Spotwas updated to1.16.0
* Session F-Droidwas updated to1.31.2
* SFTP-SAFwas updated to0.2.13
* Shadowsockswas updated to5.3.5-nightly
* Shadowsocks TVwas updated to5.3.5-nightly
* Share to folderwas updated to0.1.4
* Shattered Pixel Dungeonwas updated to3.3.6
* ShockAlarmwas updated to0.4.3
* SicMu Neowas updated to2.4.5
* Simple Notes Syncwas updated to1.8.2
* Simple Searchwas updated to2.6.0
* SimpleXraywas updated to1.10.16
* Simply Scoredwas updated to0.1.8
* sing-boxwas updated to1.12.22
* Siteswap Generatorwas updated to1.7.0
* SiYuanwas updated to3.5.7
* SnapSafewas updated to4.1.2
* SpamBlocker (Call & SMS)was updated to5.4
* Status Bar Speedometerwas updated to3.15.1
* Stay Put - Unplug Alertwas updated to0.8.8
* Stocks Widgetwas updated to4.0.048
* Sudaku - Pattern-driven sudokuwas updated to0.1.1
* Suntimeswas updated to0.16.13
* Super Productivitywas updated to17.1.8
* SwatchItwas updated to0.7.0
* Syncthing-Forkwas updated to2.0.14.2
* Table Habitwas updated to1.23.8
* TacticMasterwas updated to1.0.28
* Taler Point-of-Sale Terminalwas updated to1.3.2
* Tasks.org: Open-source To-Do Lists & Reminderswas updated to14.12
* tazwas updated to2.0.5
* The One Appwas updated to5.1.4
* Thumb-Keywas updated to5.1.3
* Thunderbird: Free Your Inboxwas updated to16.1
* ToLoSharewas updated to1.0.13
* Torrents Diggerwas updated to1.2.0
* Trackbook - Movement Recorderwas updated to2.2.8
* Traffic Lightwas updated to2.10
* Trail Sensewas updated to7.6.0
* Trailencewas updated to1.4.1
* Tranquil Stopwatchwas updated to1.12.1
* Transistor - Simple Radio Appwas updated to4.3.6
* Translate Youwas updated to17.2
* Triggerwas updated to4.0.8
* Trudidowas updated to1.3.1
* Träwelldroidwas updated to2.22.3
* Tubularwas updated to0.28.2
* Tuskywas updated to32.1
* Tuta Calendarwas updated to327.260210.0
* Tuta Mailwas updated to327.260210.0
* Tutto Counterwas updated to0.8.1
* Twili Recipeswas updated to0.2.10
* Uncivwas updated to4.19.13
* Unitto — calculator and unit converterwas updated toTitanium yellow
* Unstoppable Crypto Walletwas updated to0.47.1
* Urik Keyboardwas updated to0.17.3-beta
* Vacation Dayswas updated to17.2
* Varengold activeTANwas updated to1.2.0
* VerveDowas updated to3.0.1
* Vespucci - an OSM Editorwas updated to21.2.3.0
* Wall Youwas updated to14.1
* Wave Lines Live Wallpaperwas updated to1.13.7
* WebLibre: The Privacy-Focused Browserwas updated to0.9.32
* Whisper+was updated to1.6
* WHPH • Work Hard Play Hardwas updated to0.21.0
* Xed-Editorwas updated to3.2.7
* Xraywas updated to12.1.1
* Yagni Launcherwas updated to0.4.4-alpha
* Yiviwas updated to7.13.2
* Your local weatherwas updated to6.2.1
* Zimly S3 Backupwas updated to3.4.1
* 天使动漫was updated to1.15.0

Thank you for reading this week’s TWIF 🙂

Please subscribe to theRSS feedin your favourite RSS application to be updated of new TWIFs when they come up.

You are welcome to join theTWIF forum thread. If you have any news from the community, post it there, maybe it will be featured next week 😉

To help support F-Droid, please check out thedonation pageand contribute what you can.
