---
title: SCREAM CIPHER (“ǠĂȦẶAẦ ĂǍÄẴẶȦ”) — Seth Larson
url: https://sethmlarson.dev/scream-cipher
site_name: hackernews
fetched_at: '2025-09-21T11:05:36.131756'
original_url: https://sethmlarson.dev/scream-cipher
author: Seth Michael Larson
date: '2025-09-21'
description: Python, open source, and the internet
---

Blog
 :

About
 :

Links
 :

RSS
 :

Mastodon
 :

Email

# SCREAM CIPHER (“ǠĂȦẶAẦ ĂǍÄẴẶȦ”)

Seth Larson @ 2025-09-13

You've probably heard ofstream ciphers, but what about ascream cipher😱?
Today I learned there are more “Latin capital letter A”
Unicode characters than there are letters in the English alphabet. You know what that means, it's time to scream:

CIPHER

=

{

"A"
:
"A"
,

# Round-trip!

"B"
:
"Á"
,
"G"
:
"Ẳ"
,
"L"
:
"Ậ"
,
"Q"
:
"Ǟ"
,
"V"
:
"À"
,

"C"
:
"Ă"
,
"H"
:
"Ẵ"
,
"M"
:
"Ầ"
,
"R"
:
"Ȧ"
,
"W"
:
"Ả"
,

"D"
:
"Ắ"
,
"I"
:
"Ǎ"
,
"N"
:
"Ẩ"
,
"S"
:
"Ǡ"
,
"X"
:
"Ȃ"
,

"E"
:
"Ặ"
,
"J"
:
"Â"
,
"O"
:
"Ẫ"
,
"T"
:
"Ạ"
,
"Y"
:
"Ā"
,

"F"
:
"Ằ"
,
"K"
:
"Ấ"
,
"P"
:
"Ä"
,
"U"
:
"Ȁ"
,
"Z"
:
"Ą"
,

}

CIPHER
.
update
({
map
(
str
.
lower
,

kv
)

for

kv

in

CIPHER
.
items
()})

UNCIPHER

=

{
v
:

k

for

k
,

v

in

CIPHER
.
items
()}

def

SCREAM
(
text
:

str
)

->

str
:


return

""
.
join
(
CIPHER
.
get
(
ch
,

ch
)

for

ch

in

text
)

def

unscream
(
scream
:

str
)

->

str
:


return

""
.
join
(
UNCIPHER
.
get
(
ch
,

ch
)

for

ch

in

scream
)

print
(
s

:=

SCREAM
(
"SCREAM CIPHER"
))

# ǠĂȦẶAẦ ĂǍÄẴẶȦ

print
(
unscream
(
s
))

# SCREAM CIPHER

Wow, you made it to the end!...and you're thinking, what now?Share your thoughts onMastodon,email, orBluesky.Follow this blog onRSSor theemail newsletter.Browse thisblog’s archiveof 137 entries.Check out thislist of cool stuffI found on the internet.Go outside (best option)
