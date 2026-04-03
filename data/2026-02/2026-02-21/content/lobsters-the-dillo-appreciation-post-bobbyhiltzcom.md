---
title: The Dillo Appreciation Post | BobbyHiltz.com
url: https://bobbyhiltz.com/posts/2026/02/dillo-appreciation/
site_name: lobsters
content_file: lobsters-the-dillo-appreciation-post-bobbyhiltzcom
fetched_at: '2026-02-21T06:00:39.102107'
original_url: https://bobbyhiltz.com/posts/2026/02/dillo-appreciation/
author: Bobby Hiltz
date: '2026-02-21'
description: An appreciation post regarding the Dillo Browser and how I use it to browse the web, including YouTube, Wallabag, and others
tags: browsers
---

## The Dillo Appreciation Post

Putting the little browser to work

About a year ago Imentionedthat I had rediscovered the Dillo Web Browser. Unlike some of my other hobbies, endeavours, and interests, my appreciation for Dillo has not wavered.

I only have a moment to gush today, so I’ll cut right to it. Dillo has been plugging along nicely (see the Git forge.) and adding little features. Features that even I, a guy with a blog, can put to use. Here are a few of my favourites.

## Page Actions

### Webmentions

Mybookmarkspage isn’t just a copy-pasted list. There is a little more to it. If you look at the source you’ll see that the list entries have some markup. That markup is used when I send webmentions, and it also makes the page into anh-feed(see). To save time, I made a few quick page actions to include in thedillorcfile:

page_action="Copy Like:~/.dillo/actions/dillo-like.sh"
page_action="Copy Bookmark:~/.dillo/actions/dillo-bookmark.sh"

The page actions call little Bash scripts that just copy the URL and title to the clipboard for me. It saves me a little time. This is what the scripts look like.

#!/usr/bin/env bash

url
=
$(
dilloc

url
)

pagetitle
=
$(
dilloc

dump

|

grep

-P

-o

"(?<=\<title\>).*(?=\<\/title\>)"
)

set

-x

echo

"* <div class=\"h-entry\"><a href=\"/\" class=\"u-author\">Bobby Hiltz</a> liked: <span class=\"u-like-of h-cite\"><a href=\""
$url
"\" class=\"u-url\">
$pagetitle
</a></span> <time class=\"dt-published\" datetime=\"
$(
date

'+%Y-%m-%dT%H:%M:%S%:z'
)
\">(
$(
date

'+%d %B %Y'
)
)</time></div>"

|

xclip

-selection

clipboard

#!/usr/bin/env bash

url
=
$(
dilloc

url
)

pagetitle
=
$(
dilloc

dump

|

grep

-P

-o

"(?<=\<title\>).*(?=\<\/title\>)"
)

set

-x

echo

"* <div class=\"h-entry\"><a href=\"/\" class=\"u-author\">Bobby Hiltz</a> bookmarked: <span class=\"p-name\"><span class=\"u-bookmark-of h-cite\"><a href=\""
$url
"\" class=\"u-url\">
$pagetitle
</a></span></span> <time class=\"dt-published\" datetime=\"
$(
date

'+%Y-%m-%dT%H:%M:%S%:z'
)
\">(
$(
date

'+%d %B %Y'
)
)</time></div>"

|

xclip

-selection

clipboard

They both use thedilloccommand to dump the page andgrepthe part of the page I want.

I am positive that there are better ways to do this, but this hasn’t failed me yet.

### Sharing to other services

page_action="Send to Wallabag:wallabag add $url"
page_action="Send to linkhut:dilloc open https://ln.ht/_/add?url=$url&title={dilloc dump | grep -P -o "(?<=\<title\>).*(?=\<\/title\>)"}"

Two other actions that I use are for sharing pages to Wallabag (usingwallabag-client) andlinkhut.Wallabagis a read-it-later service, andlinkhutis a social bookmarking site that works with Dillo.

The action for linkhut opens the submission page with the URL and title prefilled.

## Browsing YouTube and Wallabag

### YouTube (dillPype? Pype-Dillo?)

On my personal computer, I hardly ever open the actual YouTube page. The main ways to see content from that website are using alternative frontends, likeInvidiousor by subscribing to the RSS feed of the channel inNewsboatand viewing the content usingmpv.

Both of those are fine.

There are times, however, when I am using Dillo that I want to just have a list of my videos to watch. For that, I made a quick Python script usingfeedparser, having been inspired byPhilip Wattamore’sRSS feeds page, and called itdillPypebecause it needed a better name thanyt-rss-to-html-thingy.

It takes a list of feeds in a text file (on feed per line), grabsNentries, sorts them by date, and outputs an HTML file.

#!/usr/bin/env python3

import

feedparser

import

os

import

datetime

# Settings

input_file

=

"/home/USER/.dillo/scripts/feeds.txt"

output_file

=

"/home/USER/.dillo/dillpype.html"

video_count

=

3

# number of videos to fetch for each feed

homepage

=

open
(
output_file
,

"w"
)

# Gets feeds from txt file input

print
(
"Opening input..."
,

input_file
)

with

open
(
input_file
,

"r"
)

as

f
:


feedlist

=

f
.
read
()
.
splitlines
()

# Creates a list of dictionaries containing video entries

print
(
"Making list of videos..."
)

video_list

=

[]

for

channel

in

feedlist
:


parsed_channel

=

feedparser
.
parse
(
channel
)


# print(parsed_channel)


vid

=

0


while

vid

<

video_count
:


author

=

f
"
{
parsed_channel
[
'entries'
][
0
][
'authors'
][
0
][
'name'
]
}
"


link

=

f
"
{
parsed_channel
[
'entries'
][
0
][
'link'
]
}
"


date

=

f
"
{
parsed_channel
[
'entries'
][
vid
][
'published_parsed'
][
0
]
}
-
{
parsed_channel
[
'entries'
][
vid
][
'published_parsed'
][
1
]
:
02d
}
-
{
parsed_channel
[
'entries'
][
vid
][
'published_parsed'
][
2
]
:
02d
}
"


video_title

=

f
"
{
parsed_channel
[
'entries'
][
vid
][
'title'
]
}
"


video_entry

=

{


"date"
:

date
,


"author"
:

author
,


"videotitle"
:

video_title
,


"link"
:

link
,


}


video_list
.
append
(
video_entry
)


vid

+=

1

# Sorts the list of videos

sorted_video_list

=

sorted
(
video_list
,

key
=
lambda

x
:

x
[
"date"
],

reverse
=
True
)

# Takes videos from list and prints them as <li> entries

def

feedprinter
():


homepage
.
write
(
"<ul>
\n
"
)


for

e
,

entry

in

enumerate
(
sorted_video_list
):


# print(entry['date'], entry['videotitle'])


homepage
.
write
(


f
"<li>
{
entry
[
'date'
]
}
 &dash; <a href=
\"
{
entry
[
'link'
]
}
\"
>
{
entry
[
'author'
]
}
 &dash;
{
entry
[
'videotitle'
]
}
</a></li>
\n
"


)


homepage
.
write
(
"</ul>
\n
"
)

# header templates

html_header_1

=

"""<!DOCTYPE html>

<html lang="en">

<head>

<style>

 body {

 background: white;

 line-height: 1.5;

 margin: 0;

 }

 main {

 margin: 10px;

 }

 header {

 color: white;

 background: red;

 padding: 1rem;

 text-align: center;

 }

</style>

<title>dillPype</title>

</head>

<body>

<header>

<h1>dillPype</h1>

"""

html_header_2

=

"""</header>

<main>

"""

# footer template

html_footer

=

"""</main>

<footer><a href="dpi:/bm/">all bookmarks</a></footer>

</body>

</html>

"""

# writes html file

print
(
"Preparing homepage..."
)

# writes header to html

print
(
"Writing header..."
)

homepage
.
write
(
html_header_1
)

t

=

datetime
.
datetime
.
now
()

lastup

=

f
"
{
t
.
year
}
-
{
t
.
month
:
02d
}
-
{
t
.
day
:
02d
}
 at
{
t
.
hour
}
:
{
t
.
minute
:
02d
}
"

print
(
lastup
)

homepage
.
write
(
lastup
)

homepage
.
write
(
html_header_2
)

# writes feeds to html

print
(
"Writing feed..."
)

feedprinter
()

# writes footer to html

print
(
"Writing footer..."
)

homepage
.
write
(
html_footer
)

homepage
.
close
()

print
(
"Done"
)

Here is the result:

I just right-click and use a link action to open the video in mpv. Easy. Of course, I do need to run the script sometimes to get new videos, but that isn’t such a problem.

Special thanks to this post from MacKenzie:No Shorts Please! Hidden YouTube RSS Feed URLs

Be sure to check that out if you subscribe to YouTube RSS feeds.

## Wallabag (dillBag? Bag-o-Dillo?)

Same this as above. Wallabag doesn’t work in Dillo, but if you use Wallabag, you can subscribe to your own feed. When I am out and about, I can save pages for later on my phone and then access the links from Dillo (I generally open the articles in using ardrviewlink action).

The script looks like this:

#!/usr/bin/env python3

import

feedparser

import

os

import

datetime

import

re

# Settings

output_file

=

"/home/USER/.dillo/wallabag.html"

article_count

=

20

# number of videos to fetch for each feed

homepage

=

open
(
output_file
,

"w"
)

wallabag

=

feedparser
.
parse
(
"https://app.wallabag.it/feed/USER/qsdqsdqsd/unread"
)

# Loop to add entries to dictionary

art

=

0

article_list

=

[]

while

art

<

article_count
:


title

=

f
"
{
wallabag
[
'entries'
][
art
][
'title'
]
}
"


link

=

f
"
{
wallabag
[
'entries'
][
art
][
'links'
][
0
][
'href'
]
}
"


content

=

f
"
{
wallabag
[
'entries'
][
art
][
'content'
][
0
][
'value'
]
}
"


time_search

=

re
.
search
(
r
"(\d*) min"
,

content
)


print
(
time_search
)


try
:


article_entry

=

{


"title"
:

title
,


"link"
:

link
,


"readingtime"
:

time_search
.
group
(
1
),


}


except
:


article_entry

=

{
"title"
:

title
,

"link"
:

link
,

"readingtime"
:

"0"
}


article_list
.
append
(
article_entry
)


art

+=

1

# takes entries from dictionary and prints them

def

feedprinter
():


homepage
.
write
(
"<ul>
\n
"
)


for

e
,

entry

in

enumerate
(
article_list
):


# print(entry['date'], entry['videotitle'])


homepage
.
write
(


f
"<li><a href=
\"
{
entry
[
'link'
]
}
\"
>
{
entry
[
'title'
]
}
</a> <span class=
\"
readingtime
\"
>(
{
entry
[
'readingtime'
]
}
 min.)</span></li>
\n
"


)


homepage
.
write
(
"</ul>
\n
"
)

print
(
"Preparing homepage..."
)

# header template

html_header_1

=

"""<!DOCTYPE html>

<html lang="en">

<head>

<style>

 body {

 background: white;

 line-height: 1.5;

 margin: 0;

 }

 main {

 margin: 10px;

 }

 header {

 color: white;

 background: blue;

 padding: 1rem;

 text-align: center;

 }

 .readingtime {

 font-size: small;

 }

</style>

<title>dillbag</title>

</head>

<body>

<header>

<h1>dillbag</h1>

"""

html_header_2

=

"""</header>

<main>

"""

# footer template

html_footer

=

"""</main>

<footer><a href="dpi:/bm/">all bookmarks</a></footer>

</body>

</html>

"""

# writes header

homepage
.
write
(
html_header_1
)

t

=

datetime
.
datetime
.
now
()

lastup

=

f
"
{
t
.
year
}
-
{
t
.
month
:
02d
}
-
{
t
.
day
:
02d
}
 at
{
t
.
hour
}
:
{
t
.
minute
:
02d
}
"

print
(
lastup
)

homepage
.
write
(
lastup
)

homepage
.
write
(
html_header_2
)

# prints feed

feedprinter
()

# writes footer

homepage
.
write
(
html_footer
)

homepage
.
close
()

print
(
"done"
)

And the output looks like this:

## Just Browsing

Not every site works perfectly on Dillo. Here are a few sites thatdolook fine:

* Alterslash
* CBC Lite
* CNN Lite
* NPR (text)
* Skinny Guardian
* The Brutalist Report
* wrttr.in

Obviously, nearly all the blogs inmy blogrolllook great too.

Overall, Dillo handles the job of navigating today’s totally messed up web quite nicely, despite the many sites that are just overly-complicated for what they are (there are workarounds forsomeof the more bloated pages). I encourage you to grab the latest version from the Git (unless your distropackagesan up-to-date version) and go surfing.

## dotfiles

You can see the scripts and config filesherein my dotfiles repo.
