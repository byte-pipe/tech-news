---
title: GitHub - 0x0mer/CasNum · GitHub
url: https://github.com/0x0mer/CasNum
site_name: hackernews_api
content_file: hackernews_api-github-0x0mercasnum-github
fetched_at: '2026-03-08T11:07:37.873810'
original_url: https://github.com/0x0mer/CasNum
author: aebtebeten
date: '2026-03-07'
description: Contribute to 0x0mer/CasNum development by creating an account on GitHub.
tags:
- hackernews
- trending
---

0x0mer

 

/

CasNum

Public

* NotificationsYou must be signed in to change notification settings
* Fork5
* Star172

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

8 Commits
8 Commits
casnum
casnum
 
 
examples
examples
 
 
screenshots
screenshots
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
requirements.txt
requirements.txt
 
 
View all files

## Repository files navigation

# CasNum

CasNum (Compass and straightedge Number) is a library that implements
arbitrary precision arithmetic usingcompass and straightedgeconstructions.
Arbitrary precision arithmetic, now with 100% more Euclid. Featuring a functional
modified Game Boy emulator where every ALU opcode is implemented entirely through
geometric constructions.

# Table of Contents

1. Introduction To Compass And Straightedge Constructions
2. Possible UsesIntegration inside a Gameboy Emulator
3. Integration inside a Gameboy Emulator
4. Examples and how to run
5. Philosophy
6. Performance
7. Dependencies
8. F.A.Q
9. License and Third-Party Credits

## Introduction To Compass And Straightedge Constructions

This project began with a simple compass-and-straightedge 'engine', which can be found under the directorycas/.
In compass-and-straightedge constructions, one start with just two points:
The origin, and a unit. Exactly as God intended. The engine then allows us to do what the ancients did:

* Construct the line through two points
* Construct the circle that contains one point and has a center at another point
* Construct the point at the intersection of two (non-parallel) lines
* Construct the one or two points in the intersection of a line and a circle (if they intersect)
* Construct the one point or two points in the intersection of two circles (if they intersect) (Which, by the way turns out to be a nasty 4th degree equation. Check out the formula incircle.py, over 3600 characters, yikes. Good thing we have WolframAlpha).

These five constructions are considered the basic compass and straightedge constructions. Think of these as your ISA.

On top of the compass-and-straightedge engine, we have theCasNumclass.
InCasNum, a numberxis represented as the point(x,0)in the plane.
Now, the fun part: implementing all arithmetic and logical operations.
We can construct the addition of two points by finding the midpoint between them
and doubling it, which are both standard compass-and-straightedge constructions.
Then, we can build the product and quotient of numbers using triangle similarity.
The logical operations (AND, OR, XOR) are a little uglier, since they are not a "clean algebraic operation" in the relevant sense, but, hey, it works right?

What I thought was pretty neat is that implementing all this from scratch leaves a lot of room for optimization. For example, multiplication by 2 can be implemented much more efficiently than the generic algorithm for multiplication using triangle similarity. Then, implementing modulo by first removing the highest power of two times the modulus from the dividend yielded much better results than the naive implementation.

## Possible Uses

* Simple RSA program
* Integrate into the ALU of a Game Boy emulator, thus obtaining a Game Boy that arithmetically and logically runs solely on compass and straightedge constructions
* More? idk

The first two examples were actually implemented and can be found under theexamples/directory.
So apparently one cannotsquare the circleusing a compass and a straightedge, but at least one can run Pokémon Red.
Man, I'm sure the ancient Greeks would have loved to see this.

### Integration inside a Game Boy Emulator

Thanks to the great code written byPyBoy,
integratingCasNumwithin it was pretty seamless.
The only file I needed to edit wasopcodes_gen.py, and the edit was pretty
minimal.

## Examples and how to run

As always, please save any important work before running anything I ever write.

To clone the repo, and install requirements:

git clone --recursive git@github.com:0x0mer/CasNum.git

cd
 CasNum
pip install -r requirements.txt

You can run the rsa and basic examples from the repo's root directory like so:

python3 -m examples.basic
python3 -m examples.rsa

The library comes with a viewer (casnum/cas/viewer.py) that shows the compass
and straightedge constructions. It has an automatic zoom that kinda works, but it
goes crazy in the rsa example, so you may want to use manual zoom there.

In order to run PyBoy, first you need a ROM. In order to avoid copyright
infringement, I included the ROM for2048,
free to distribute under the zlib license. But if, for example, the ROM you have
is 'Pokemon.gb', then you can place it in examples/Pyboy and run:

cd
 examples/PyBoy
pip install -r requirements.txt
PYTHONPATH=../.. python

Then, once in python, run:

from
 
pyboy
 
import
 
PyBoy

from
 
casnum
 
import
 
viewer

viewer
.
start
()

pyboy
 
=
 
PyBoy
(
'2048.gb'
) 
# Or whatever ROM you have

while
 
pyboy
.
tick
():
 
pass

pyboy
.
stop
()

theviewer.start()just displays the compass-and-straightedge constructions, it is not
strictly needed, but it is fun.

Notice however that the first run of Pokemon on the Game Boy emulator takes approximately 15
minutes to boot, so playing it may require somewhat increased patience. You see, Euclid wouldn't have optimized the Game Boy boot screen.
He would have spent those 15 minutes in silent appreciation, thinking, "Yeah.
That’s about how long that should take."

After running it once, most calculations should already be cached if you run it
from the same python interpreter instance, so on the second run you should be able
to get a decent 0.5~1 FPS, which is totally almost playable.

## Philosophy

Most modern developers are content witha + b. They don't want to work for it.
They don't want to see the midpoint being birthed from the intersection of two circles.CasNumis for the developer who believes that if you didn't have to solve a
4th-degree polynomial just to increment a loop counter,
you didn't really increment it.

## Performance

Python'slru_cacheis used to cache almost any calculation done in the library,
as everything is so expensive. Memory usage may blow up, run at your own risk.

* Time Complexity: Yes
* Space Complexity: Also yes

## Dependencies

* sympy
* pyglet (optional but highly recommended. Only needed if you want to display the
compass-and-straightedge constructions)
* pytest-lazy-fixtures (Only needed in order to run the tests)
* pycryptodome (Only needed if you want to run the rsa example)
* Euclid Postulate V (optional)

## F.A.Q

1. Q: buT cAN iT rUn dOOm?A: It can't really "run" anything, its a number.
2. Q: Is it fast?A: Define "fast". If you mean "faster than copying Euclid by hand", then yes, dramatically.
3. Q: Why did you make this?A: I wanted arbitrary precision arithmetic, but I also wanted tofeel something.

## License and Third-Party Credits

The code in the root of this repository is licensed under theMIT License.

### Third-Party Components

This project incorporates the following third-party materials:

* PyBoy (Modified): Located in./examples/PyBoy/. Distributed under theGNU Lesser General Public License (LGPL) v3.0.Notice of Modification: This version of PyBoy has been modified from the original source code to use the CasNum library instead of Python's int.The original, unmodified source code for PyBoy can be found at:https://github.com/Baekalfen/PyBoy.The full LGPL license text is available in./examples/PyBoy/License.md.
* Notice of Modification: This version of PyBoy has been modified from the original source code to use the CasNum library instead of Python's int.
* The original, unmodified source code for PyBoy can be found at:https://github.com/Baekalfen/PyBoy.
* The full LGPL license text is available in./examples/PyBoy/License.md.
* 2048.gb: This Game Boy ROM binary is distributed under thezlib License.Disclaimer: This software is provided 'as-is', without any express or implied warranty. In no event will the authors be held liable for any damages arising from the use of this software.
* Disclaimer: This software is provided 'as-is', without any express or implied warranty. In no event will the authors be held liable for any damages arising from the use of this software.

## About

 No description, website, or topics provided.
 

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

172

 stars
 

### Watchers

0

 watching
 

### Forks

5

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors1

* 0x0merOmer

## Languages

* Python100.0%