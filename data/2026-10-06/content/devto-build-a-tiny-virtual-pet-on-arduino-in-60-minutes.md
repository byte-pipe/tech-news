---
title: Build a Tiny Virtual Pet on Arduino in 60 Minutes 🐾 - DEV Community
url: https://dev.to/heraistudio/build-a-tiny-virtual-pet-on-arduino-in-60-minutes-2cf
site_name: devto
content_file: devto-build-a-tiny-virtual-pet-on-arduino-in-60-minutes
fetched_at: '2026-10-06T17:04:39.594175'
original_url: https://dev.to/heraistudio/build-a-tiny-virtual-pet-on-arduino-in-60-minutes-2cf
author: Jen Looper
date: '2026-10-06'
description: Turn an Arduino Uno Q into Kiku, a Tamagotchi-style virtual pet with an animated LED face, moods, and keyboard controls. Tagged with arduino, beginners, programming, hacktoberfest.
tags: '#arduino, #beginners, #programming, #hacktoberfest'
---

Hacktoberfest: Maintainer Spotlight

What if your first hardware project wasn't another blinking LED, but a tiny pet that gets hungry, plays with you, falls asleep, and reacts to what you type?

MeetKiku. 🌸

Kiku is the mascot and in-house pet ofHer AI Studio, a community program helping the next generation of women learn and build with AI.

In this mini workshop, we're shrinking Kiku down until the entire pet can live on anArduino Uno Q.

Full tutorial is available in theHer AI Studio curriculum

What you need:

* an Arduino Uno Q
* a USB cable
* your laptop
* Arduino App Lab
* about 60 minutes

Tip! To celebrate Hacktoberfest 2026, swag packs from Major League Hacking are shipping with these Arduinos, so use this workshop for your Hack Day as an introduction to hardware hacking.

Shhh, Kiku is sleeping

By the end, you'll have a tiny Tamagotchi-style pet whose face lives on the board's LED matrix. You'll be able tofeed it, play with it, and put it to sleep from your keyboard. More importantly, you'll see how a surprisingly small amount of code can produce behavior that feels alive.

## What you'll learn

This project brings together several useful embedded-programming concepts:

* flashing code onto physical hardware
* communicating with a microcontroller over Serial
* drawing graphics on an LED matrix
* tracking application state
* responding to user input
* creating simple animations
* building a tiny state machine

If you've mostly written software that stays inside your laptop, there's something especially satisfying about seeing your code suddenly appear on physical hardware.

## Part 1: Make sure the board is alive

Before building a virtual pet, start with the embedded developer's version of"Hello, world!":Blink an LED.

Connect your Uno Q to your laptop over USB and open Arduino App Lab which you've downloaded. Login to your board.

Create a new app, and take a look at the scaffolded code. Opensketch.ino, and write a basic blink sketch:

void
 
setup
()
 
{

 
pinMode
(
LED_BUILTIN
,
 
OUTPUT
);

}

void
 
loop
()
 
{

 
digitalWrite
(
LED_BUILTIN
,
 
LOW
);

 
delay
(
1000
);

 
digitalWrite
(
LED_BUILTIN
,
 
HIGH
);

 
delay
(
1000
);

}

Enter fullscreen mode

Exit fullscreen mode

Pressrunin App Lab.

If the built-in LED turns on and off every second,it's aliiiiive!

If the board isn't detected, check your USB cable. Some USB cables provide power but don't carry data.

## Part 2: Give your Arduino a way to listen

Now we need Kiku to hear us. We could add buttons or sensors (and we do, in our full workshop with our full AI Kit), but there's a much simpler interface already available:Serial communication.

The same USB connection used to upload your program can carry messages between your laptop and your Arduino while the program is running. In App Lab, it looks like this:

Start Serial communication insetup():

void
 
setup
()
 
{

 
Serial
.
begin
(
9600
);

}

Enter fullscreen mode

Exit fullscreen mode

Then check for incoming characters:

void
 
loop
()
 
{

 
if
 
(
Serial
.
available
()
 
>
 
0
)
 
{

 
char
 
typed
 
=
 
Serial
.
read
();

 
if
 
(
typed
 
==
 
'f'
)
 
{

 
// feed Kiku

 
}

 
if
 
(
typed
 
==
 
'p'
)
 
{

 
// play with Kiku

 
}

 
if
 
(
typed
 
==
 
's'
)
 
{

 
// sleep or wake up

 
}

 
}

}

Enter fullscreen mode

Exit fullscreen mode

Your keyboard has effectively become the controller for a physical device.

To interact with Kiku, we'll use 3 keystrokes:

f → feed
p → play
s → sleep / wake

Enter fullscreen mode

Exit fullscreen mode

## Part 3: Give Kiku some feelings

A virtual pet needs more than commands. It needsstate. Kiku tracks three simple stats:

int
 
hunger
 
=
 
3
;

int
 
joy
 
=
 
6
;

int
 
energy
 
=
 
8
;

bool
 
asleep
 
=
 
false
;

Enter fullscreen mode

Exit fullscreen mode

We'll treat each stat as a value from0to10. Now actions can change the pet by incrementing or decrementing these values. Feeding Kiku, for example, reduces hunger (but don't overfeed!):

hunger
 
=
 
max
(
0
,
 
hunger
 
-
 
3
);

joy
 
=
 
min
(
10
,
 
joy
 
+
 
1
);

Enter fullscreen mode

Exit fullscreen mode

Playing might make Kiku happier while consuming energy:

joy
 
=
 
min
(
10
,
 
joy
 
+
 
3
);

energy
 
=
 
max
(
0
,
 
energy
 
-
 
2
);

hunger
 
=
 
min
(
10
,
 
hunger
 
+
 
1
);

Enter fullscreen mode

Exit fullscreen mode

## Make time matter

If Kiku's stats only changed when we typed something, the pet wouldn't feel particularly alive.

So we introduce time! Every few seconds, atick()function updates Kiku's state, like this:

void
 
tick
()
 
{

 
if
 
(
asleep
)
 
{

 
// regain energy

 
}
 
else
 
{

 
// lose energy

 
// gradually lose joy

 
}

 
// gradually become hungry

}

Enter fullscreen mode

Exit fullscreen mode

In your code, use a short interval so changes are easy to observe (and change this later when you want your pet to chill out):

const
 
unsigned
 
long
 
TICK_MS
 
=
 
10000
;

Enter fullscreen mode

Exit fullscreen mode

That's one update every ten seconds. Walk away from Kiku and come back later, and its state will definitely be different - they can get cranky when left alone!

## Give the state a face

Kiku turns its internal state into facial expressions on the Uno Q's LED matrix. We can define its eyes:

enum
 
Eyes
 
{

 
EYES_OPEN
,

 
EYES_CLOSED
,

 
EYES_HAPPY
,

 
EYES_PEEK

};

Enter fullscreen mode

Exit fullscreen mode

And mouth poses:

enum
 
Mouth
 
{

 
MOUTH_FLAT
,

 
MOUTH_SMILE
,

 
MOUTH_FROWN
,

 
MOUTH_OPEN
,

 
MOUTH_DOT

};

Enter fullscreen mode

Exit fullscreen mode

Now our program can translate state into emotion:

Mouth
 
moodMouth
()
 
{

 
if
 
(
hunger
 
>=
 
7
 
||
 
joy
 
<=
 
3
)

 
return
 
MOUTH_FROWN
;

 
if
 
(
joy
 
>=
 
7
)

 
return
 
MOUTH_SMILE
;

 
return
 
MOUTH_FLAT
;

}

Enter fullscreen mode

Exit fullscreen mode

Kiku isn't actually experiencing happiness or hunger, of course, but a handful of variables and conditionals suddenly starts to look like personality.

## Connect actions to behavior

Now the pieces come together. Your main loop has three jobs:

1. Listen for commands.
2. Update Kiku's state over time.
3. Draw the appropriate expression.

In simplified form:

void
 
loop
()
 
{

 
if
 
(
Serial
.
available
()
 
>
 
0
)
 
{

 
char
 
typed
 
=
 
Serial
.
read
();

 
if
 
(
typed
 
==
 
'f'
)
 
feed
();

 
if
 
(
typed
 
==
 
'p'
)
 
play
();

 
if
 
(
typed
 
==
 
's'
)
 
toggleSleep
();

 
}

 
// update stats when enough time has passed

 
// calculate blinking

 
// redraw Kiku

}

Enter fullscreen mode

Exit fullscreen mode

That's the core architecture of your Kiku. Try it with your own device!

Open the Serial Monitor in App Lab and type:

f

Enter fullscreen mode

Exit fullscreen mode

Kiku eats.

Then:

p

Enter fullscreen mode

Exit fullscreen mode

Kiku plays.

And:

s

Enter fullscreen mode

Exit fullscreen mode

Kiku goes to sleep.

## What's next?

Try to make some changes that alters Kiku's personality.

### 1. Change time

ModifyTICK_MS.

### 2. Invent an expression

Make Kiku wink, act surprised, or act sad.

### 3. Add another command

Maybe:

c → clean

Enter fullscreen mode

Exit fullscreen mode

## What did we actually build?

On the surface, we built a cute virtual pet. Underneath, we explored several concepts that appear in much larger systems:

Input handling: Serial commands become events.

State management: Variables remember what's happening between iterations of the loop.

State transitions: Actions modify that state.

Time-based behavior: The system changes even without direct input.

Rendering: Internal state becomes visible through the LED matrix.

Human-computer interaction: Animation and timing make simple logic feel expressive.

If you build your own Kiku for Hacktoberfest, we'd love to see what personality you give it.🌸

This article is presented as a gift to Hacktoberfest hackers byHer AI Studio, a community program for the next generation of women in AI.

The complete Kiku workshop, including the full Arduino sketch, exercises, knowledge checks, and additional resources, is available in theHer AI Studio curriculum.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse