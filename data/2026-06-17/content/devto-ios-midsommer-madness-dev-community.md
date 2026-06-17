---
title: IOS Midsommer Madness - DEV Community
url: https://dev.to/gde/ios-midsommer-madness-5h4
site_name: devto
content_file: devto-ios-midsommer-madness-dev-community
fetched_at: '2026-06-17T12:27:18.767069'
original_url: https://dev.to/gde/ios-midsommer-madness-5h4
author: xbill
date: '2026-06-12'
description: This is a submission for the June Solstice Game Jam Your Iphone can now celebrate the Solstace! When... Tagged with antigravitycli, devchallenge, gamechallenge, gamedev.
tags: '#antigravitycli, #devchallenge, #gamechallenge, #gamedev'
---

June Solstice Game Jam Submission

This is a submission for theJune Solstice Game Jam

Your Iphone can now celebrate the Solstace! When you have a hammer- everything is a nail! This installment brings a Flutter build running on IOS!

A complete IOS App is built using Flutter with Xcode and some Joystick bugs are fixed!

### What I Built

When it comes to Summar Solstace — the place to be is Sweden. It is one of the highlights of the calendar.

This project aimed to recreate some of the mystique around the event- just in time for some fresh surestromming!

Now you can get it on the GO!

In a previous article, the web app was refactored to be Flutter compatible. This installment adds an IOS build from the Flutter code base and deploys it to an Iphone.

### Code

GitHub repo is here:

GitHub - xbill9/midsommer-flutter: Midsommer Madness game in Flutter / Web view

### Midsommer Madness game in Flutter / Web view

The first version of the article built the app out as a web based game:

Midsommer Madness

Then, the app was converted to Android:

Android Midsommer Madness

And finally to Flutter:

Flutter Midsommer Madnesss

#### Game Play

The key levels include:

1. IKEA Warehouse:Battle crowded, flatpack-carrying shoppers who throw box projectiles at you.
2. Systembolaget:The state-owned liquor shop crowded with drunk Swedes stumbling and lobbing green beer bottles.
3. Lördagsgodis:Sugar rush Saturday! Dodge hyperactive, strung-out Swedish kids throwing sweet candy projectiles.
4. The Swedish Pub:Sing along with Frank Zappa fans singing “Bobby Brown” (shouting and firing glowing letters B, O, B, B, Y).
5. Volvo Highway:A survival lane-crossing level where…

### My Lingonberries are ripening- get to work!

How do you deploy this?

To build for IOS- you need a recent Mac system with Xcode tools installed along with Flutter. You can use standard Mac installs for Xcode and Flutter is available directly or via Homebrew.

The build environment will look similar to this:

The Makefile included with the project has IOS targets:

m3:midsommer-flutter xbill$
 
make 
help

========================================================================
🇸🇪 Midsommer Madness Flutter Build & Development Controls 🇸🇪
========================================================================
Available commands:
 make dev - Start the local web server for browser play (from assets/)
 make build-apk - Compile the Flutter App and build Debug APK
 make build-ios - Compile the Flutter App and build iOS app (no codesign)
 make install-apk - Install the compiled debug APK on a connected device/emulator
 make clean - Clean Flutter build outputs and temporary caches
 make logcat - Monitor application logs using Flutter logger
========================================================================

m3:midsommer-flutter xbill$
 
pwd

/Users/xbill/midsommer-flutter

m3:midsommer-flutter xbill$
 

Enter fullscreen mode

Exit fullscreen mode

OK. Tell me more!

> how do I build the IOS version of this?

● ListDir(/Users/xbill/midsommer-flutter)
● Read(/Users/xbill/midsommer-flutter/Makefile)
● Read(/Users/xbill/midsommer-flutter/README.md) (ctrl+o to expand)

 To build the iOS version of this project, you can use the following
 methods:

 ### 1. Build via CLI (Without Code Signing)

 If you want to compile the iOS version quickly without setting up
 provisioning profiles or code signing, you can run the command defined in
 the Makefile:

 make build-ios 

 Alternatively, you can run the underlying Flutter command directly:

 flutter build ios --no-codesign 

 ──────
 ### 2. Build for the iOS Simulator

 If you want to build and run the application specifically for testing
 inside the macOS iOS Simulator:

 flutter build ios --simulator 

 And then run it using:

 flutter run 

 ──────
 ### 3. Build & Run via Xcode (For Physical Devices / App Store)

 To configure signing certificates, team provisioning profiles, and run on a
 physical iOS device:

 1.
 Open the iOS project workspace in Xcode:
 open ios/Runner.xcworkspace 

 2.
 In Xcode, select the Runner project in the left sidebar.

 3.
 Under the Signing & Capabilities tab, select your developer Team and
 bundle identifier to resolve code signing.

 4.
 Select your connected target device or simulator at the top, and click
 the Play button to build and run.

Enter fullscreen mode

Exit fullscreen mode

#### OK — Lets get this Party Started

Switch to the Flutter repo and run the Makefile:

>
 make build-ios

○ Bash
(
make build-ios
)
 
(
ctrl+o to 
expand
)

 I have started the make build-ios 
command 
in 
the background. Please
 approve the 
command 
execution 
in 
your terminal/UI 
if 
prompted. I will
 notify you as soon as the build completes or 
if 
any errors occur.

Enter fullscreen mode

Exit fullscreen mode

Once Xcode has been configured — you can deploy the app to a local Iphone:

>
 flutter build ios

● Bash
(
flutter build ios
)
 
(
ctrl+o to 
expand
)

 I have started the flutter build ios 
command 
in 
the background to build
 the signed app bundle.

 Please approve the execution 
if 
prompted. I will 
let 
you know as soon as
 it completes.

 The signed iOS app bundle has been built successfully!

 • Output File: build/ios/iphoneos/Runner.app 

 You can now deploy it to your connected device:

 ios-deploy 
--bundle
 build/ios/iphoneos/Runner.app

Enter fullscreen mode

Exit fullscreen mode

and send it to an Iphone:

● Bash
(
ios-deploy 
--bundle
 build/ios/iphoneos/Runner.app
)
 
(
ctrl+o to 
expand
)

 The signed application has been successfully deployed to your connected
 iOS device!

 
[
95%] GeneratingApplicationMap 
 
[
100%] InstallComplete 
 
[
100%] Installed package build/ios/iphoneos/Runner.app 

 The game should now be visible on your device
's home screen.

Enter fullscreen mode

Exit fullscreen mode

#### Screenshots or It didn’t Happen!

Once the full Flutter App has been built — you can transfer it to an Iphone for testing:

#### This is Fun! How do I add my own levels?

The levels can be directly added with Antigravity CLI:

>
 
add
 
a
 
godis
 
level
 
where
 
strung
 
out
 
kids
 
throw
 
lordagsgodis
 

▸
 
Thought
 
for
 
2
s
,
 
525
 
tokens
 
Considering
 
Level
 
Placement
 

I
 
will
 
search
 
for
 
level
 
ID
 
checks
 
referencing
 
level
 
9
 
in
 
game
.
js
 
to
 
prepare
 
for
 
adding
 
a
 
10
th
 
level
.
 
●
 
Search
(
Search
 
for
 
lvl
.
id
 
===
 
9
 
checks
)
 
(
ctrl
+
o
 
to
 
expand
)
 
I
 
will
 
view
 
lines
 
495
 
to
 
585
 
in
 
game
.
js
 
to
 
inspect
 
the
 
current
 
level
 
configurations
.
 
●
 
Read
(
/home/
xbill
/
midsommer
-
madness
/
game
.
js
)
 
(
ctrl
+
o
 
to
 
expand
)
 
▸
 
Thought
 
for
 
2
s
,
 
1.8
k
 
tokens
 
Sequencing
 
the
 
Levels
 
I
 
will
 
view
 
the
 
setLevelAudioMode
 
method
 
in
 
game
.
js
 
to
 
prepare
 
for
 
adding
 
Level
 
3
 
"
Lördagsgodis
"
.
 
●
 
Read
(
/home/
xbill
/
midsommer
-
madness
/
game
.
js
)
 
(
ctrl
+
o
 
to
 
expand
)
 
I
 
will
 
update
 
the
 
setLevelAudioMode
 
method
 
in
 
game
.
js
 
to
 
map
 
the
 
scales
 
and
 
tempos
 
for
 
the
 
10
-
level
 
layout
.
 
●
 
Edit
(
/home/
xbill
/
midsommer
-
madness
/
game
.
js
)
 
(
ctrl
+
o
 
to
 
expand
)
 
I
 
will
 
view
 
the
 
current
 
level
 
checks
 
in
 
tickSequencer
 
inside
 
game
.
js
 
to
 
prepare
 
the
 
next
 
set
 
of
 
replacements
.
 
●
 
Read
(
/home/
xbill
/
midsommer
-
madness
/
game
.
js
)
 
(
ctrl
+
o
 
to
 
expand
)
 
I
 
will
 
shift
 
the
 
level
 
conditionals
 
in
 
the
 
music
 
sequencer
 
tickSequencer
 
method
 
to
 
accommodate
 
the
 
10
-
level
 
progression
.
 
●
 
Edit
(
/home/
xbill
/
midsommer
-
madness
/
game
.
js
)
 
(
ctrl
+
o
 
to
 
expand
)
 
I
 
will
 
view
 
lines
 
920
 
to
 
935
 
of
 
game
.
js
 
to
 
locate
 
the
 
exact
 
Maypole
 
check
 
in
 
initLevel
 
.
 
●
 
Read
(
/home/
xbill
/
midsommer
-
madness
/
game
.
js
)
 
(
ctrl
+
o
 
to
 
expand
)
 
I
 
will
 
view
 
lines
 
1060
 
to
 
1070
 
of
 
game
.
js
.
 
●
 
Read
(
/home/
xbill
/
midsommer
-
madness
/
game
.
js
)
 
(
ctrl
+
o
 
to
 
expand
)
 
I
 
will
 
view
 
lines
 
1290
 
to
 
1300
 
of
 
game
.
js
.
 
●
 
Read
(
/home/
xbill
/
midsommer
-
madness
/
game
.
js
)
 
(
ctrl
+
o
 
to
 
expand
)
 
I
 
will
 
view
 
lines
 
1360
 
to
 
1375
 
of
 
game
.
js
.
 
●
 
Read
(
/home/
xbill
/
midsommer
-
madness
/
game
.
js
)
 
(
ctrl
+
o
 
to
 
expand
)
 
I
 
will
 
view
 
lines
 
1370
 
to
 
1385
 
of
 
game
.
js
.
 
●
 
Read
(
/home/
xbill
/
midsommer
-
madness
/
game
.
js
)
 
(
ctrl
+
o
 
to
 
expand
)
 
I
 
will
 
view
 
lines
 
1460
 
to
 
1475
 
of
 
game
.
js
.
 
●
 
Read
(
/home/
xbill
/
midsommer
-
madness
/
game
.
js
)
 
(
ctrl
+
o
 
to
 
expand
)
 
I
 
will
 
update
 
the
 
level
 
ID
 
checks
 
for
 
the
 
final
 
Maypole
 
level
 
from
 
9
 
to
 
10
 
and
 
register
 
the
 
candy
-
throwing
 
kids
 
target
 
name
 
in
 
the
 
HUD
.
 
●
 
Edit
(
/home/
xbill
/
midsommer
-
madness
/
game
.
js
)
 
(
ctrl
+
o
 
to
 
expand
)
 
I
 
will
 
view
 
the
 
start
 
of
 
the
 
levels
 
array
 
in
 
game
.
js
 
to
 
prepare
 
the
 
level
 
insertion
 
edit
.
 
●
 
Read
(
/home/
xbill
/
midsommer
-
madness
/
game
.
js
)
 
(
ctrl
+
o
 
to
 
expand
)
 
I
 
will
 
view
 
lines
 
545
 
to
 
585
 
of
 
game
.
js
.
 
●
 
Read
(
/home/
xbill
/
midsommer
-
madness
/
game
.
js
)
 
(
ctrl
+
o
 
to
 
expand
)
 
▸
 
Thought
 
for
 
3
s
,
 
1.2
k
 
tokens
 
Refining
 
The
 
Level
 
Design
 
I
 
will
 
update
 
the
 
levels
 
array
 
in
 
game
.
js
 
to
 
insert
 
Lördagsgodis
 
as
 
Level
 
3
,
 
shift
 
subsequent
 
level
 
IDs
,
 
and
 
re
-
calculate
 
scores
.
 
●
 
Edit
(
/home/
xbill
/
midsommer
-
madness
/
game
.
js
)
 
(
ctrl
+
o
 
to
 
expand
)
 
I
 
will
 
view
 
lines
 
950
 
to
 
985
 
of
 
game
.
js
 
to
 
locate
 
the
 
spawnEnemy
 
switch
 
statement
.
 
●
 
Read
(
/home/
xbill
/
midsommer
-
madness
/
game
.
js
)
 
(
ctrl
+
o
 
to
 
expand
)
 
I
 
will
 
view
 
lines
 
985
 
to
 
1010
 
of
 
game
.
js
.
 
●
 
Read
(
/home/
xbill
/
midsommer
-
madness
/
game
.
js
)
 
(
ctrl
+
o
 
to
 
expand
)
 
I
 
will
 
add
 
the
 
"
kid
"
 
case
 
to
 
the
 
spawnEnemy
 
switch
 
block
.
 
●
 
Edit
(
/home/
xbill
/
midsommer
-
madness
/
game
.
js
)
 
(
ctrl
+
o
 
to
 
expand
)
 
▸
 
Thought
 
for
 
3
s
,
 
2.1
k
 
tokens
 
Considering
 
Projectile
 
Design
 
I
 
will
 
search
 
for
 
class
 
ZappaFan
 
in
 
game
.
js
 
to
 
locate
 
a
 
suitable
 
place
 
to
 
insert
 
CandyKid
 
and
 
Lordagsgodis
 
.
 
●
 
Search
(
Search
 
for
 
ZappaFan
 
in
 
game
.
js
)
 
(
ctrl
+
o
 
to
 
expand
)
 
I
 
will
 
view
 
lines
 
2120
 
to
 
2145
 
in
 
game
.
js
.
 
●
 
Read
(
/home/
xbill
/
midsommer
-
madness
/
game
.
js
)
 
(
ctrl
+
o
 
to
 
expand
)
 
I
 
will
 
insert
 
the
 
CandyKid
 
and
 
Lordagsgodis
 
class
 
definitions
 
in
 
game
.
js
 
right
 
after
 
the
 
Drunkard
 
class
.
 
●
 
Edit
(
/home/
xbill
/
midsommer
-
madness
/
game
.
js
)
 
(
ctrl
+
o
 
to
 
expand
)
 
I
 
will
 
view
 
lines
 
275
 
to
 
325
 
of
 
index
.
html
.
 
●
 
Read
(
/home/
xbill
/
midsommer
-
madness
/
index
.
html
)
 
(
ctrl
+
o
 
to
 
expand
)
 
I
 
will
 
update
 
index
.
html
 
to
 
add
 
Level
 
3
 
Lördagsgodis
 
to
 
the
 
sidebar
 
levels
 
tracker
 
and
 
update
 
levels
 
4
 
through
 
10
.
 
●
 
Edit
(
/home/
xbill
/
midsommer
-
madness
/
index
.
html
)
 
(
ctrl
+
o
 
to
 
expand
)
 
I
 
will
 
run
 
a
 
syntax
 
check
 
on
 
game
.
js
 
using
 
node
 
to
 
ensure
 
the
 
new
 
classes
 
and
 
level
 
configurations
 
are
 
syntax
-
error
 
free
.
 
●
 
Bash
(
node
 
-
c
 
game
.
js
)
 
(
ctrl
+
o
 
to
 
expand
)
 
I
 
will
 
view
 
lines
 
20
 
to
 
45
 
of
 
game_overview
.
md
 
to
 
inspect
 
the
 
levels
 
sequence
 
list
.
 
●
 
Read
(
/home/
xbill
/
.
gemini
/
antigravity
-
cli
/
brain
/
a
...
2
ba
-
4622
-
b252
-
003672
e1b73f
/
game_overview
.
md
)
 
(
ctrl
+
o
 
to
 
expand
)
 
I
 
will
 
update
 
game_overview
.
md
 
to
 
describe
 
the
 
10
-
level
 
layout
 
including
 
Lördagsgodis
.
 
●
 
Edit
(
/home/
xbill
/
.
gemini
/
antigravity
-
cli
/
brain
/
a
...
2
ba
-
4622
-
b252
-
003672
e1b73f
/
game_overview
.
md
)
 
(
ctrl
+
o
 
to
 
expand
)
 
I
 
have
 
successfully
 
added
 
the
 
Lördagsgodis
 
level
 
to
 
Midsommer
 
Madness
,
 
featuring
 
hyperactive
,
 

sugar
-
rushed
 
children
 
throwing
 
Saturday
 
candy
 
at
 
Sven
!

###
 
Summary
 
of
 
Changes

Level
 
Setup 
(
 
game
.
js
 
):
 
*
 
Inserted
 
Lördagsgodis
 
as
 
game
.
js
 
in
 
the
 
levels
 
array
,
 
shifting
 
following
 
levels
 
up
 
to
 
Level
 
10
 
(
ABBA
 
Disco
).
 
*
 
Updated
 
all
 
final
-
level
 
check
 
logic
 
throughout
 
game
.
js
 
from
 
Level
 
9
 
to
 
Level
 
10
.

Added
 
CandyKid
 
&
 
Lordagsgodis
 
Classes 
(
 
game
.
js
 
):

 
*
 
Defined
 
game
.
js
 
and
 
game
.
js
 
right
 
after
 
the
 
Drunkard
 
class
.

 
*
 
Behavior
:

 
*
 
CandyKid
 
has
 
high
 
speed 
(
1.8
),
 
low
 
health 
(
35
),
 
and
 
throws
 
sweets
 
rapidly
.

 
*
 
Kids
 
shiver
/
vibrate
 
rapidly
 
on
 
screen
 
to
 
depict
 
their
 
extreme
 
sugar
 
rush
.

 
*
 
Lordagsgodis
 
are
 
fast
-
moving
 
candy
 
projectiles 
(
round
 
jelly
 
drops
,
 
square
 
sweet
 
gel
 
blocks
,
 
and
 
candy

 
star
 
crosses
)
 
that
 
rotate
 
in
 
flight
 
and
 
come
 
in
 
a
 
variety
 
of
 
bright
 
colors
.

Music
 
&
 
Audio
:

 
*
 
Modified
 
game
.
js
 
to
 
include
 
a
 
happy
,
 
hyperactive
 
150
 
BPM
 
C
 
Major
 
chiptune
 
track
 
for
 
Level
 
3

 
(
Lördagsgodis
).

 
*
 
Shifted
 
level
 
conditions
 
in
 
game
.
js
 
to
 
map
 
Levels
 
8
,
 
9
,
 
and
 
10
 
to
 
their
 
respective
 
custom
 
chiptune

 
hooks
.

UI
 
&
 
Documentation
:

 
*
 
renumerated
 
the
 
sidebar
 
tracker
 
list
 
in
 
index
.
html
 
to
 
show
 
the
 
10
-
level
 
layout
.

 
*
 
Updated
 
the
 
level
 
progression
 
descriptions
 
in
 
game_overview
.
md
.

Enter fullscreen mode

Exit fullscreen mode

#### Summary- How did we get here?

In the first article, a Node.JS browser based webapp was built.

Then this app was converted to a Native Android APK. From there- the codebase was refactored to be Flutter compatible and deployed as a Flutter Android APK. Finally- this Flutter codebase was used along with Xcode to produce an IOS compatible version from a Mac Laptop.

This IOS version was downloaded to an Iphone and was fully playable.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse