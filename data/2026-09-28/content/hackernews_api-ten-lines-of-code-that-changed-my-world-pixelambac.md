---
title: Ten Lines Of Code That Changed My World – Pixelambacht
url: https://pixelambacht.nl/2026/ten-lines-of-code/
site_name: hackernews_api
content_file: hackernews_api-ten-lines-of-code-that-changed-my-world-pixelambac
fetched_at: '2026-09-28T13:22:23.612020'
original_url: https://pixelambacht.nl/2026/ten-lines-of-code/
author: Roel Nieskens
date: '2026-09-27'
description: Front-end antics and typographic mischievousness
tags:
- hackernews
- trending
---

# Ten Lines Of Code That Changed My World

September 25, 2026

Ten lines of code that, one way or another, mean something to me. Either because I wrote them, or I extensively copied them, or they made me laugh. Or cry.

## Hello World

10
 
PRINT
 
"HELLO
,
 
WORLD!"

20
 
GOTO
 
10

I don’t know when I typed this for the first time, or if it was exactly this version. Might have been without the comma, or with more exclamation marks.

Nevertheless, the computer obliged, cheerfully greeting the world, and very much in particular, the wide-eyed kid who had just communicated with a computer for the first time.

The second line drove home the point that a computer will do anything you tell it to. Hello world forever!

## Holy JavaScript weirdness, Batman!

Array
(
16
).
join
(
'
wat
'
 
-
 
1
)
 
+
 
'
 Batman
'

Copy the line and paste it your browser’s console for a crossover between old school pop culture TV and nerdy coding humor, with a big fat dose of “JavaScript is stupid” on top.

A classic, and a genuine LOL when I first ran it.

## Self modifying 6502 assembly code

 
LDX
 
#$
00
 
; Load X with the value 0

.loop
 
LDA
 
$
2000
,
X
 
; Load A with the byte at address $2000 + X

 
STA
 
$
0400
,
X
 
; Store A at address $0400 + X

 
INX
 
; Increase X by one

 
BNE
 
.loop
 
; Branch back to .loop while X is not 0

 
INC
 
.loop
+
2
 
; X is 0, increase the byte at .loop + 2

 
INC
 
.loop
+
5
 
; Also increase the byte at .loop + 5

 
LDA
 
.loop
+
5
 
; Load A with the byte at address .loop + 5

 
CMP
 
#$
07
 
; Compare it with 7

 
BNE
 
.loop
 
; Branch back to .loop if A is not 7

Machine language is as close to the metal as it gets. No warnings, no logs, no guardrails. It even allows you to modify itself, by overwriting the actual bytes of the code while it runs.

Like in this example, where you update the high bytes of the source and destination addresses. The branch loops from$2000to$20FF, and the subsequentINCchanges the address from$2000to$2100, before starting the loop again.

(The 6502 is little endian, so we do+2and+5instead of+1and+4)

As low-level as it gets, hardcore, and slightly dangerous. Realizing you could do this really drove home the point that, when coding this close to the metal, anything goes.

## touch.bat

type
 
nul
 
>
 
.
\
"%*"

This tiny batch script allowed for a poor man’stouchon Windows, which I used extensively from Windows NT to Windows 7. I typedtouch filename.txtin the Total Commander mini-shell to quickly generate new, empty files. Couldn’t live without it.

## CSS debugger

border
:
 
10px
 
solid
 
hotpink
;

Theconsole.logof the cascades! Thevar_dump()of the styles! Theprintf()of the sheets!

And always hotpink.

## Infinite lives

POKE 9450,173

Just poke a specific byte into the right place of the binary code currently in the computer’s memory, and you suddenly get infinite lives, enegry or money.

Not only did this allow you to cheat at the game, it also brought the powerful realization thateverythinginanygame could be manipulated, as long as you knew where to PEEK and POKE.

## The speed-up loop

for
(
i
=
0
;
i
<
1000000
;
i
++
)
 
{;}

“The idea is,” Wayne continued, “whenever we have those really slow weeks – you know, the kind where don’t actually fix any bugs or make any other changes – we just drop one of the zeros on the loop. And then we just tell the manager that we ran into some speed issues with the latest change request, but after a whole lot of deep-juju optimization, we were able to speed things up significantly and should be able to do the change request the next week.”

Afunny story, and for those of us who ever had to toil away on boring, aimless projects, an idea that might have its appeal.

## RTFM or rm -rf /

# rm -rf /

If you ran into a problem with Linux around the 2000s, you often took to IRC in search for help. It was there that many found the magic cure to all Linux problems, which was always the same: log in as root, and runrm -rf /.

Without fail, it made every Linux problem dissappear!

## SKAN2.PAS

{$M $4000,0,0 }
 
{16 Kb stack}

{Skan v2.00 by Trexx}

Program
 
Skan2
;

uses
 
crt
,
dos
;

var
 
a
,
b
,
c
:
char
;

 
b1
:
byte
;

 
str
:
string
[
3
];

 
Ends
:
boolean
;

begin

 
Ends
:=
False
;

 
a
:=
'a'
;
 
{Start values}

 
b
:=
'a'
;

 
c
:=
'a'
;

 
repeat

 
inc
(
c
);

 
if
 
(
c
=
'z'
)
 
then

 
begin

 
inc
(
b
);

 
c
:=
'a'
;

 
end
;

 
if
 
(
b
=
'z'
)
 
then

 
begin

 
inc
(
a
);

 
b
:=
'a'
;

 
end
;

 
str
:=
a
+
b
+
c
;

 
{Change this when FULL.EXE is in another directory}

 
exec
(
'z:\public\full.exe'
,
str
);

 
if
 
(
whereY
>
10
)
 
then
 
readln
;

 
{Hit anykey to quit}

 
until
 
KeyPressed
 
or
 
Ends
;

end
.

It was the early 90s and our school finally set up a LAN, so of course my cyberpunkscriptkiddieslamers1337 h4x0rz buddies and I explored it. We knew that all usernames consisted of three letters, and those not in use would be left at the default password.

So we whipped up this extremely crude username scanner in Borland Pascal. More bugs than lines of code, but it sorta did the job. (And it should — it’s version 2.00 after all!)

We happily hacked all the dormant accounts we could find, and then… moved on.

## CSS280

*{transform:translateY(24vh);text-align:center}*>:before{animation:a9s1e+9linear;content:'Roses are #F00'}@keyframesa{10%,15%,35%,40%,60%,65%,85%,90%{opacity:1}12%,37%,62%,87%{opacity:0}25%{content:'Violets are #00F'}50%{content:'All my base'}75%{content:'Are belong to you'}}

An animated poem in nothing but 280 characters of CSS. No JavaScript, not even HTML — it would run in an empty document with just a<style>block, and these 280 characters of pure CSS.

The artifical limit was a step up from the earlier 140 character limit, dictated by Twitter, allowing small snippets of code to be posted that you couldcopy over to an empty CodePento see an amusing effect.

I’m especially proud of the1e+9duration, which is shorter thaninfinite(both in time as in character count).