---
title: Installing every* Firefox extension
url: https://jack.cab/blog/every-firefox-extension
site_name: hackernews_api
content_file: hackernews_api-installing-every-firefox-extension
fetched_at: '2026-04-11T11:12:39.432500'
original_url: https://jack.cab/blog/every-firefox-extension
author: RohanAdwankar
date: '2026-04-10'
description: Oh, you use Firefox? Name every extension.
tags:
- hackernews
- trending
---

# Installing every* Firefox extension

 

Oh, you use Firefox? Name every extension.

 

Published

 4/9/2026 
 
 
 
 

*All but 8 we didn’t scrape (or got deleted between me checking the website and me scraping) and 42 missing from extensions.json.1Technically we only installed 99.94% of the extensions.

It turns out there’s only84 thousandFirefox extensions.
That soundsfeasiblysmall. That even sounds like it’s less than 50 gigabytes. Let’s install them all!

## Scraping every Firefox extension

There’s apublic APIfor the add-ons store.
No authentication required, and seemingly no rate limits. This should be easy.

Thesearch endpointcan take an empty query. Let’s read every page:

1
let
 url 
=
2
 
"https://addons.mozilla.org/api/v5/addons/search/?page_size=50&type=extension&app=firefox&appversion=150.0"
3

4
let
 extensions 
=
 []
5
let
 page 
=
 
1
6

7
while
 (
true
) {
8
 
let
 res 
=
 
await
 
fetch
(url)
9
 
let
 data 
=
 
await
 res.
json
()
10
 
console.
log
(
`PAGE ${
page
++
}: ${
data
.
results
.
length
} EXTENSIONS`
)
11
 
extensions.
push
(
...
data.results)
12
 
url 
=
 data.next
13
 
if
 (
!
data.next) 
break
14
}
15

16
Bun.
write
(
"extensions-default.json"
, 
JSON
.
stringify
(extensions))

The search API only gives me 600 pages, meaning I can only see 30 thousand extensions, less than half of them.

A solution I found is to use different sorts. The default sort issort=recommended,users: first recommended extensions, then sorted by users, descending. Changing to justsort=createdgave me some of the long tail:

1
let
 url 
=
2
 
"https://addons.mozilla.org/api/v5/addons/search/?page_size=50&type=extension&app=firefox&appversion=150.0"
3
 
"https://addons.mozilla.org/api/v5/addons/search/?page_size=50&type=extension&app=firefox&appversion=150.0&sort=created"

16
Bun.
write
(
"extensions-default.json"
, 
JSON
.
stringify
(extensions))
17
Bun.
write
(
"extensions-newest.json"
, 
JSON
.
stringify
(extensions))

count.ts
1
import
 extensions_default 
from
 
"../extensions-default.json"
2
import
 extensions_newest 
from
 
"../extensions-newest.json"
3

4
let
 extensions 
=
 {}
5

6
// Yes, somehow I got the same slug twice
7
for
 (
const
 
ext
 
of
 extensions_default) {
8
 
extensions[ext.slug] 
=
 ext
9
}
10

11
for
 (
const
 
ext
 
of
 extensions_newest) {
12
 
extensions[ext.slug] 
=
 ext
13
}
14

15
console.
log
(
`TOTAL UNIQUE EXTENSIONS: ${
Object
.
keys
(
extensions
).
length
}`
)

Terminal window
~/Developer/every-addon> bun count
TOTAL UNIQUE EXTENSIONS: 54218

I’m still missing 30,0252extensions, so I addedratingandhotnesstoo.

Terminal window
~/Developer/every-addon> bun count
TOTAL UNIQUE EXTENSIONS: 67458

That’s still 16,7852missing. Addingupdated…

Terminal window
~/Developer/every-addon> bun count
TOTAL UNIQUE EXTENSIONS: 67945

Starting to hit diminishing returns. While I was waiting 7 minutes for that last list to get scraped because my code didn’t fetch in parallel, I had an epiphany: useexclude_addons. I can just fetch page 600 and exclude all its addons to get page 601.

1
let
 url 
=
2
 
"https://addons.mozilla.org/api/v5/addons/search/?page_size=50&page=600&type=extension&app=firefox&appversion=150.0&sort=updated"
3
const
 
page_600
 
=
 
await
 
fetch
(url).
then
(
res
 
=>
 res.
json
())
4
const
 
page_601
 
=
 
await
 
fetch
(
5
 
`${
url
}&exclude_addons=${
page_600
.
results
.
map
(
ext
 
=>
 
ext
.
id
).
join
(
","
)
}`
,
6
).
then
(
res
 
=>
 res.
json
())

It works! There is a URL length limit, sadly, so I can only fetch an extra 20 pages.

1
let
 url 
=
2
 
"https://addons.mozilla.org/api/v5/addons/search/?page_size=50&page=600&type=extension&app=firefox&appversion=150.0&sort=created&exclude_addons="
3

4
let
 extensions 
=
 []
5
let
 page 
=
 
600
6
try
 {
7
 
while
 (
true
) {
8
 
let
 res 
=
 
await
 
fetch
(url)
9
 
let
 data 
=
 
await
 res.
json
()
10
 
console.
log
(
`PAGE ${
page
++
}: ${
data
.
results
.
length
} EXTENSIONS`
)
11
 
if
 (data.results.
at
(
-
1
).id 
===
 extensions.
at
(
-
1
)?.id) 
break
 
// IDK
12
 
extensions.
push
(
...
data.results)
13
 
url 
+=
 data.results.
map
(
ext
 
=>
 ext.id).
join
(
","
)
14
 
}
15
} 
catch
 {}
16

17
Bun.
write
(
"created-2.json"
, 
JSON
.
stringify
(extensions))

TAke a look, y’all:

Terminal window
~/Developer/every-addon> bun count
TOTAL UNIQUE EXTENSIONS: 68035

A lot less than I expected, especially considering what happens when I add thedownloadssort:

Terminal window
~/Developer/every-addon> bun count
TOTAL UNIQUE EXTENSIONS: 68901

Reading the docs again, I notice I can filter by category as well.
I’m tired of waiting 7 minutes so I’ll just fetch every page in parallel.

1
function
 
get
(
url
:
 
string
, 
path
:
 
string
) {
2
 
return
 
Promise
.
all
(
3
 
Array.
from
({ length: 
600
 }, (
_
, 
i
) 
=>
 
fetch
(
`${
url
}&page=${
i
 
+
 
1
}`
).
then
(
res
 
=>
 res.
json
())),
4
 
).
then
(
pages
 
=>
 {
5
 
let
 extensions 
=
 pages.
flatMap
(
page
 
=>
 page.results)
6
 
Bun.
write
(path, 
JSON
.
stringify
(extensions))
7
 
})
8
}
9

10
const
 
categories
 
=
 
await
 
fetch
(
"https://addons.mozilla.org/api/v5/addons/categories/"
).
then
(
res
 
=>
11
 
res.
json
(),
12
)
13

14
await
 
Promise
.
all
(
15
 
categories
16
 
.
filter
(
category
 
=>
 category.type 
===
 
"extension"
)
17
 
.
map
(
category
 
=>
 {
18
 
return
 
get
(
19
 
`https://addons.mozilla.org/api/v5/addons/search/?page_size=50&type=extension&app=firefox&sort=created&category=${
category
.
slug
}&appversion=150.0`
,
20
 
`./newest-${
category
.
slug
}.json`
,
21
 
)
22
 
}),
23
)

I got basically all the extensions with this, making everything I did before this look really stupid.

Terminal window
~/Developer/every-addon> bun analyze
Found 84235 unique extensions
That would be 49.3 GB, an average of 584.9 kB per extension

That’s 8 less extensions than what it says on the website.
When I ran this in September 2025, it found 21moreextensions than what was mentioned on the website, so I think this is enough.

So that nobody has to do this again, I’ve uploaded this dataset toHugging Face.

 

Alternatively,addons-serverhas CORS enabled, so click this funny button to get
		your very ownall_extensions.json:

 
Download all_extensions.json
 
This requires JavaScript!
 
 
 

### April 11 update

The search API supports date filters:created__gteandcreated__lte.
The API also returns the full number of extensions that match your search.

You can start with a filter that includes all extensions, then keep splitting the ranges in half until it is less than 30 thousand, then
fetch all of them.

I’ve updated the downloader: it is faster, wastes fewer requests, and seems to scrape exactly all the extensions, too.

This won’t work if over 30 thousand extensions get created in a single second, which I can’t imagine will ever happen.

## Analyzing every Firefox extension

I have a copy of Bun andall_extensions.json, so I will torment you with my unmatched script power.

### Biggest extensions

The biggest Firefox extension isdmitlichessat 196.3 MB, which contains 2000+ audio files.

Here’s the rest of the top ten:

* (Unoffical) ReactBot Web, 184.9 MB: An entire Unity application. “This add-on is larger than most add-ons” is an understatement.
* Eric’s Thumbnail Seasoning!, 146.6 MB: Someone’s personal fork of YouTube MrBeastify. Contains 900 .pngs.
* Animal Forest:PG BGM, 137.4 MB: Evil version ofhttps://tane.us/ac.
* YouTube OCR, 128.3 MB:Tesseract.js.
* Image to Text for ChatGPT, 128.3 MB: AlsoTesseract.js.
* qwip AI Detection BETA, 126.0 MB: Two deepfake detection models.
* Kumo Study, 117.0 MB: 50 royalty free lo-fi study beats.
* YouTube Jakkify, 114.0 MB: Another YouTube MrBeastify fork. 500 soyjaks.
* True Paper, 111.6 MB: Like qwip, this also embeds an AI model and the ONNX runtime.

The first time I ran this analysis, in September, “Cute doggy - Dog puppies” was the 10th largest extension. I’m still mentioning it here, because I was so fucking confused:

 

The smallest extension istheTabs-saver, which is 7518 bytes and has no code.

### Worst extension

Subjectively it’s Cute doggy - Dog puppies, but objectively:

1
import
 extensions 
from
 
"../all_extensions.json"
2
console.
log
(
3
 
extensions
4
 
.
filter
(
ext
 
=>
 ext.ratings.count 
>
 
10
)
5
 
.
sort
((
a
, 
b
) 
=>
 a.ratings.bayesian_average 
-
 b.ratings.bayesian_average)[
0
],
6
)

it’sTab Stack for Firefox, by lolicon (?!?!?!?!?!).

### First extension

Web Developer.

### Most screenshots

RDS Barhas 54.

### The “Middle Finger Emoji Sticker” Award

FalscheLaden, with no users, requests 3,695 permissions.
The author has posteda writeup.

Second place isGoogle Dark Theme, which requests 2,675 permissions but has 1,687 users.

### Most prolific developer

1
import
 extensions 
from
 
"../all_extensions.json"
2

3
console.
log
(
4
 
Object.
values
(
5
 
Object.
groupBy
(
6
 
extensions.
flatMap
(
e
 
=>
 e.authors),
7
 
author
 
=>
 author.id,
8
 
),
9
 
).
sort
((
a
, 
b
) 
=>
 b.
length
 
-
 a.
length
)[
0
][
0
],
10
)

Dr. Bis the king of slop, with 84 extensions published, all of them vibe coded.

How do I know? Most of their extensions have a README.md in them describing their process of getting these through addon review, and mention Grok 3.
Also, not a single one of them have icons or screenshots.

Personally, I’m shocked this number is this low. I expected to see some developers with hundreds!

### Phishing

I reviewed the source of a couple homoglyph attacks on crypto wallets discovered in the dataset
and was disappointed to find out they just pop up a form asking for your seed phrase and send it off to their server.
It’s an extension!!! You can steal theircoinbase.comtoken! You can monitor the clipboard and swap out their address for yours!
You cancrash their browser and claim your real malware is the fix!

Why would you make a fake MetaMask extension and bot 1-star reviews?

 

Is this the doing of their cybercrime competitors, who bot 4-star reviews on extensions of their own?

 

Either way, these extensions are clearly phishing. I reported some to Mozilla, and the next day they were all gone, even the ones I was too lazy to report. I forgot to archive them, so I guess they live on in May’s VM!

In terms of implementation, the most interesting one is “Іron Wаllеt” (the I, a, and e are Cyrillic).
Three seconds after install, it fetches the phishing page’s URL from the first record of a NocoDB spreadsheet and opens it:

static/background/index.js
58
var
 r 
=
 
e
(
"./lib/noco"
)
59
chrome.runtime.onInstalled.
addListener
(
async
 () 
=>
 {
60
 
try
 {
61
 
await
 
new
 
Promise
(
e
 
=>
 
setTimeout
(e, 
3e3
))
62
 
let
 e 
=
 
await
 (
0
, r.fetchUrlFromNocoRest)()
63
 
e
64
 
?
 
await
 chrome.tabs.
create
({
65
 
url: e,
66
 
})
67
 
:
 console.
warn
(
"No valid URL from NocoDB."
)
68
 
} 
catch
 (e) {
69
 
console.
error
(
"Install flow failed:"
, e)
70
 
}
71
})

I think the extension’s “no accounts or remote code” description is really funny, like putting “no copyright infringement intended” in your video’s description in case YouTube is watching.
The API key had write access, so I wiped the spreadsheet.

### SEO spam

You get a “Homepage” link in your extension’s page and your own page.It’s beennofollowfor two years,
but that hasn’t stopped grifters from trying anyway.

OnAttempt 1, I encounteredTypo SniperandTab Fortune Teller,
AI generated extensions with casinos in their author’s Homepage links.

In the dataset, there’smany “Code Injector” extensions, which are all virtually identical
and also have random websites in their author’s Homepage link.

All of these extensions are from 2025. Is there an ancient SEO guide circulating?
Is there some evil AMO frontend they’re still getting a backlink from?
I have no idea what’s happening here.

### PUAs

Do you notice a pattern?

* Maps Assist & Custom Web Search: 138,082 users
* Package Tracking Tab & Custom Web Search: 83,506 users
* Converter Suite & Custom Web Search: 82,502 users
* Manuals Explorer & Custom Web Search: 66,835 users
* Ezy Photo Tab & Custom Web Search: 54,347 users
* Easy Games Tab & Custom Web Search: 34,918 users
* Task Manager Tab & Custom Web Search: 34,585 users
* Turbo Converter & Custom Web Search: 32,236 users
* Quick Live News & Custom Web Search: 31,542 users
* Ezy Speed Test & Custom Web Search: 30,853 users
* Quick Recipe Hub & Custom Web Search: 29,556 users
* Flight Tab Pro & Custom Web Search: 28,633 users
* Weather Authority & Custom Web Search: 13,658 users
* Video Converter World & Custom Web Search: 13,191 users
* Daily Top Coupons & Custom Web Search: 9,385 users
* Password Generator Pro & Custom Web Search: 5,289 users
* Calculator Whiz & Custom Web Search: 4,563 users
* Calendar Planner & Custom Web Search: 4,223 users
* Ezy Alarm Clock & Custom Web Search: 4,051 users
* Zip-Unzip Files & Custom Web Search: 3,298 users
* Latest Wallpapers & Custom Web Search: 2,648 users
* Ezy Screenshot & Custom Web Search: 2,231 users
* Precious Bible & Custom Web Search: 1,946 users
* Grammar Wise & Custom Web Search: 1,115 users
* Stream Live Radio & Custom Web Search: 725 users
* Astrology Craft & Custom Web Search: 185 users
* AI Chat Pro & Custom Web Search: 1 poor user

Over 700 thousand users in total.

All of these extensions are their author’s only uploads and they have their own domains. Most of them are on both Chrome and Firefox, their websites look the same, and they all have a terms of service referencing “Innover Online Group Ltd”, which is a .png for some reason.

Because I scraped every Firefox extension twice, I can see what got removed in between the runs.
Three of Innover Group’s extensions—Earth View 360°, View Manuals, and View Recipes, totaling 115 thousand users—have been disabled by Mozilla.

Innover Group runsGoogle adsfor their extensions, a lot of themsimply saying “Continue”.

The “Custom Web Search” is Yahoo but with their affilate code.
That code beingsafeplexsearch, which has a website of its own which of course mentions Innover Online Group Ltd, and links toan addonwith 3,892 users, which is actually a Firefox exclusive.
Actually, “Custom Web Search” is a Firefox exclusive on all of these extensions. Why did they even make a Chrome version, to sell them to the NSA??

One user claimed Ezy Speed Test “disables Ublock [sic] Origin once installed”, which I did not find in its code.

There’s a million companies like this, though.
I just went to Download.com with my ad-blocker off and discovered the company Atom Apps in an ad,
whichalsouploads extensions for both Chrome and Firefox,
with a new account for each extension,
only includes Yahoo in the Firefox version,
with names that end in either “and Search” or ”& Search”,
and has their company name as a .png in their terms of service.
They have 220 thousand daily users total across 12 extensions, and none of theirs have been disabled.

### Some percentages

* 34.3% of extensions have no daily users25.1% of extensions have more than 10 daily users10.6% of extensions have more than 100 daily users3.2% of extensions have more than 1000 daily users0.7% of extensions have more than 10000 daily users
* 25.1% of extensions have more than 10 daily users
* 10.6% of extensions have more than 100 daily users
* 3.2% of extensions have more than 1000 daily users
* 0.7% of extensions have more than 10000 daily users
* 76.7% of extensions are open source (SPDX license that isn’t All Rights Reserved)
* 23% of extensions were created after I started writing this article19% of extensions have no users, no reviews, no screenshots, no downloads, and no icon
* 19% of extensions have no users, no reviews, no screenshots, no downloads, and no icon
* 2.4% of extensions require payment38.1% of those are open source???
* 38.1% of those are open source???

## Installing every Firefox extension

Obviously I’m not going toopen each of these in a new tabandgo through those prompts. Not for lack of trying:

 

Each extension has thecurrent_version.file.urlproperty which is a direct download for the extension.
I download them to my profile’s extensions folder with theguidproperty as the base name and the .xpi file extension, becauseanything else will not be installed.

Then, I delete theaddonStartup.json.lz4andextensions.jsonfiles.
When I reopen Firefox, each extension is disabled. Tampering withextensions.jsonis common enough that you can ask any chatbot to do it for you:

enable.js
1
const
 
fs
 
=
 
require
(
"fs"
) 
// WHY IS THIS COMMONJS
2
const
 
path
 
=
 
require
(
"path"
)
3

4
// Path to extensions.json (adjust this to your Firefox profile directory)
5
// WHY IS THIS IN CAMELCASE
6
const
 
extensionsJsonPath
 
=
7
 
"/Users/user/Library/Application Support/Firefox/Profiles/1avegyqd.default-release/extensions.json"
8

9
try
 {
10
 
// Read the extensions.json file
11
 
const
 
data
 
=
 fs.
readFileSync
(extensionsJsonPath, 
"utf-8"
) 
// WHY IS THIS NOT NODE:FS/PROMISES
12
 
const
 
extensionsData
 
=
 
JSON
.
parse
(data)
13

14
 
// Modify extensions
15
 
if
 (Array.
isArray
(extensionsData.addons)) {
16
 
extensionsData.addons.
forEach
(
addon
 
=>
 {
17
 
addon.userDisabled 
=
 
false
18
 
addon.active 
=
 
true
19
 
addon.seen 
=
 
true
20
 
})
21
 
// WHY IS THIS NOT A GUARD
22
 
} 
else
 {
23
 
console.
error
(
"Unexpected format: addons property is missing or not an array."
)
24
 
process.
exit
(
1
)
25
 
}
26

27
 
// Write the updated data back to extensions.json
28
 
fs.
writeFileSync
(extensionsJsonPath, 
JSON
.
stringify
(extensionsData, 
null
, 
2
))
29

30
 
console.
log
(
"All extensions enabled successfully!"
)
31
} 
catch
 (error) {
32
 
console.
error
(
"Error processing extensions.json:"
, error)
33
}

### Attempt 0: 65,335

My first attempt was in atiny11 coreVM on my desktop.

At first, instead of downloading all of them with a script, I tried using enterprise policies, but this copies all the extensions into the folder.
I quickly ran out of memory, and the pagefile took up the rest of the storage allocated to the VM.
I had also expected Firefox to open immediately and the extensions to install themselves as the browser is being used, but that also did not happen: it just froze.

 

### Attempt 1: ~1,000

After that, I tried downloading them myself.

download.ts
1
import
 extensions 
from
 
"./all_extensions.json"
2
import
 { exists } 
from
 
"node:fs/promises"
3
let
 progress 
=
 
0
4
let
 count 
=
 extensions.
length
5

6
const
 
PATH_TO_EXTENSIONS_FOLDER
 
=
7
 
"C:
\\
Users
\\
user
\\
AppData
\\
Local
\\
Mozilla
\\
Firefox
\\
Profiles
\\
mkrso47f.default-release
\\
"
8

9
await
 
Promise
.
all
(
10
 
extensions.
map
(
async
 
ext
 
=>
 {
11
 
if
 (
await
 
exists
(
PATH_TO_EXTENSIONS_FOLDER
 
+
 ext.guid 
+
 
".xpi"
)) {
12
 
progress
++
13
 
} 
else
 {
14
 
console.
log
(
"Downloading"
, ext.current_version.file.url)
15
 
const
 
file
 
=
 
await
 
fetch
(ext.current_version.file.url)
16
 
await
 Bun.
write
(
PATH_TO_EXTENSIONS_FOLDER
 
+
 ext.guid 
+
 
".xpi"
, file)
17
 
console.
log
(
"Downloaded"
, ext.slug, 
`${
(
++
progress
 
/
 
count
) 
*
 
100
}% done`
)
18
 
}
19
 
}),
20
)

 

To make sure I was installing extensions correctly, I moved the extensions folder elsewhere and then moved about a thousand extensions back in. It worked.

 

There were multiple extensions that changed all text to a certain string.bruh-ifierlost toSe ni važn.
Goku is in the background.

My context menu is so long thatI’m showing it sideways:

 

I had installed lots of protection extensions. Oneblocks traffic to .zip and .mov domains, presumably because they are file extensions.
This is.caberasure!
Then, I realized that there were likely multiple people viewing my browsing history, so I went to send them a message.

 

That “⚠️ SCAM WARNING!” popup is fromAnti-Phishing Alert. As you may have inferred, it seems to only exists for its Homepage link. How does it work?

phishing_detector.js
1
function
 
isPhishingURL
(
url
) {
2
 
const
 
suspiciousPatterns
 
=
 [
3
 
/
[
\.\-
]
login
[
\.\-
]
/
i
,
4
 
/
[
\.\-
]
secure
[
\.\-
]
/
i
,
5
 
/
[
\.\-
]
account
[
\.\-
]
/
i
,
6
 
/
[
\.\-
]
verify
[
\.\-
]
/
i
,
7
 
/
[a-z0-9
\-
]
{1,}
\.
com
\.
xyz/
i
,
8
 
/https
?
:
\/\/
(?!www
\.
)
[a-z0-9
\-
]
+
\.
(
[a-z]
{2,}
)
{2,}
/
i
,
9
 
]
10

11
 
return
 suspiciousPatterns.
some
(
pattern
 
=>
 pattern.
test
(url))
12
}

Vasavi Fraudulent Detectoralso has a popup for when a site is safe:

modal.js
23
$.
sweetModal
({
24
 
title: 
"Vasavi Fraudulent Detector"
,
25
 
content: 
"Safe Webpage !!"
,
26
 
icon: $.sweetModal.
ICON_SUCCESS
,
27

28
 
buttons: [
29
 
{
30
 
label: 
"Continue"
,
31
 
classes: 
"greenB"
,
32
 
},
33
 
],
34
})

### Attempt 2: 65,335

Only the addons from Attempt 1 were actually loaded, because I didn’t know I needed to deleteaddonStartup.json.lz4yet.
I scrolled through the addons page, then I opened DevTools to verify it was the full 65,335, at which point Firefox froze and I was unable to reopen it.

### Attempt 3: 65,335 (Mac edition)

After that,I made a new (non-admin) user on my Macto
try again on a more powerful device.

Every time I glanced at my script downloading extensions one at a time for six hours, I kept recognizing names.
Oops, I’m the AMO subject-matter expert now!
Parallelizing was making itslowerby the last 4000 extensions, which didn’t happen on my Windows VM.

When that finished, I found out my hardware couldn’t run 65,335 extensions at once, sadly.
The windowdoes openafter some time I didn’t measure, but the windownever starts responding.
I don’t have the balls to run my laptop overnight.3

Firefoxdidmakeover 400 GB of disk writes.
Because I forgot swap existed, I checked the profile trying to find the culprit, which is when I learned I needed to deleteaddonStartup.json.lz4and modifyextensions.json.
Theextensions.jsonwas 144 MB. For comparison, my PC’sextensions.jsonis 336 KB.

### Attempts 4-10: 1000-6000

My solution: add 1000 extensions at a time until Firefox took too long to open. I got to 6000.

3000 extensions was the last point where I was at least able to load webpages.

 

After 4000 or more extensions, the experience is basically identical. Here’s a video of mine (epilepsy warning):

5000 was the same as 4000 but every website was blocked by some extension I know starts with an S and ends with Blocker and has a logo with CJK characters.
At 6000 extensions, the only page that I could load wasabout:addons.

### Attempt 11: 84,194 (six months later)

My desktop has 16 GB of RAM, and my laptop has 24 GB of unified memory.
You might notice that 49.3 GB is more than twice that.

I asked a friend to help.

What you’re about to see was recorded inMay’svirtual machine.
Do not try this on your main profile.

#### Downloading

My download script started in parallel, then we switched it to serial when it slowed down.
In total, downloading took about 1 hour and 43 minutes.

I was on a call the entire time, and we spotted a lot of strange extensions in the logs.
What kind of chud would use “KiwiFarms Math Renderer”?
Are they drafting the theory of soytivity?

Turning on Mullvad VPN and routing to Tel Aviv appeared tospeed up the process.
This was not because of Big Yahu, but because May restarted the script, so she repeated that a couple times.
Whether that’s a Bun bug, I don’t know and I don’t care.
May joked about a “version 2” that I dread thinking about.

Defender marked one extension,HackTools, as malware.
May excluded the folder after that, so it may not be the only one.

 

#### Launch 1

Firefox took its sweet time remaking extensions.json, and it kept climbing.
About 39 minutes of Firefox displaying a skeleton (hence “it has yet to render a second frame”) later, it was 189 MB large: a new record! May killed Firefox and ranenable.js.

 

I did some research to find why this took so long.13 years ago, extensions.json used to be extensions.sqlite.
Nowadays, extensions.jsonisserialized and rewritten in full on every write debounced to 20 ms, which works fine for 15 extensions but not 84,194.

#### Launch 2

Finally, we see the browser.
The onboarding tabs trickled in, never loading.

 

3 minutes later, Firefox crashed.

#### Launch 3

May reopened it, took a shower, and came back to this:

 

IT STABLIZED. YOU CAN (barely) RUN FIREFOX WITH ALL 84 THOUSAND EXTENSIONS.

 

Well, we were pretty sure it had 84 thousand extensions.
It hadTab Counter, at least, and the scrollbar in the extensions panel was absolutely massive.

## Using every Firefox extension

It works.

 

### about:addons

#### Addon page

She loaded the configure pages of two extensions. The options iframe never loaded.

 

#### Index page

I realized we need to disable auto update before Firefox sends another 84 thousand requests. This one took a while to load.

The list loaded but with no icons and stopped responding, and6 hours laterit had loaded fully.

 

We recorded the entire process; the memory usage fluctuated between 27 and 37 GiB the entire time.

We did have basically every extension, including May’s ownmt-rpc.

 

Istillhave no idea whyabout:addonstook 6 hours to load.

I tested my first theory, the extension icons notloading lazily—ironically, sending another 84 thousand requests—with
aone-line patch to Firefoxand installed 3 thousand (disabled) extensions on my Mac.
To compile Firefox, I had to delete the extensions from Attempt 3 to free up storage.

 

I don’t think it reduced the amount of time Firefox was frozen for.
To be fair, I tested with 28 times less extensions than Attempt 11, so perhaps the issue only manifests at that scale.

### about:support

Wow, that’s a lot of extensions. You can’t be sure, though.

I asked May to open DevTools and check$$("#addons-tbody tr").lengthso we could be sure what we thought was 84,205 extensions were running.

 

Readingabout:supportcloser, I realized my fear was correct, but not for the reason I expected: that 84,205 included the built-in addons like Web Compatibility Interventions.
Excluding those, it was a total of 84,194 extensions we had installed.

Previously, I had written that DevTools had loaded no extensions because it was anabout:page, but I just installed webhint and went toabout:supportand sure enough it’s there, so I don’t know what caused that.

### about:preferences

We wanted to see how many New Tab options we can choose from.

 

We turned on crash reporting on the way.

### New Tab

Which extension wins? The answer is none of them.
The New Tab page never loaded, no matter which extension we selected for it, except for Firefox Home which opened instantly.

### moz-extension

A page from thebuyPal(1 user) extension opened without action on our end and replaced the other tabs open at the time. It loaded: the only non-about:page to do so.

 

Then Firefox crashed again.

### example.com

This is the first page where content scripts can run.

Like in Attempt 9, there had to have been multiple extensions that block every website.
They didn’t matter, though, because we kept the tab open for24 hoursand it never loaded.

### about:telemetry

It loaded, then she clicked on Environment Data and the browser crashed.

 

## Is this usable?

No.

## Further potential explorations

* Find out whyabout:addonstook 6 hours to load and whyexample.comnever loaded.
* Firefox isn’t the only browser that supports.xpis: so doKagi OrionandGNOME Web, both WebKit. Orion doesn’t have bulk install, so I didn’t try it, and Web is slow enough with 0 extensions.
* We intentionally installed everyextension, not every addon. It’s pretty obvious what happens when you install a lot of themes, and there’s 500 thousand of them, well beyond what we can reasonably test or even scrape.
* Install every user script and user style? There isn’t really a central database for these.
Additionally, Stylus has ahardcoded 1 GB limit for backups,
and after patching this out,
I gota new, stranger error.
* Install every Chrome extension? No, just kidding, there’s too many to do that, and no easy way to scrape them all.

## Footnotes

1. Here’s the addons that were in all_extensions.json but not extensions.json. Strikethrough = deleted from AMO.ExtensionGUIDFacebook Bulk Image Downloaderfacebook-downloader@daniel.extensionsRestart Web Browser / Shutdown OS After Download@restart_web_browserToolship: Toolkit for DEV & QAtoolship@shridharClickArmorclickarmor@clickarmor.dev当图-高级二维码生成器{af68df6c-3dc8-4986-ade3-633c34a0b16a}Auto Link Openmosa.allbedre0@gmail.comNitter Redirect Reloaded{f885cff8-968c-462b-817f-8060be9b1635}VirusTotal URL Scannervirustotal-scanner@jaffacakes118.devAiStuffaistore@example.comBraveFox Enhancerenhancer@goldenfox.comSecNote Messages encryption{07d7c62a-d3c3-484f-99d3-47641e13b24c}WIXTABcs.dorgpio.23@gmail.comNyx Controlnyx@alsania-ioOutlook Support Extensionoutlook-extension@kitamura.jf7Mistral Text Assistantmistral-text-assistant@addonsBase WaIlet Extensoin{e07663c2-b159-4f18-b382-2b44d615f5ed}(WIP) LHS - 8248 New Tabcustom-new-tab@8248.localProduct Image Scrapertechpriest@gurglorium.comBitculatorid@bitculator.comPixel emojisemoji-replacer@nadz.devMonitorizomonitorizo@monitorizo.netAzninjazninj@azninj.comAnime Streamingextension@anime-streaming.euTSS+tss_plus@mozilla.orgTruSearchtrusearchnewtab@gmail.comClass Link Check for Google Classroom™{9b887266-8284-4069-8f12-c9bd326979c2}History Overrid{f9d43888-0f36-4b8c-b5f2-f5f595547ddf}History Overrides{41e67140-ef2b-42a4-a9b3-758b4e9df8da}OnPageSeoCheck{9c3f49f3-9346-40d5-ba97-0b1872526a41}tnt-signuature{493830f0-1fff-4f9a-aa1e-444bafbc7312}CheharaTime{fc1f9366-1a9c-4aac-8113-d91e9ecb7a74}Social Networks Automationsocial-networks-automation@mozilla.orgHistory Override{c09a4ed2-c611-41af-b3e4-79a810216f93}Facebook Always Active (DCS)DCS-FB-AA@mozilla.orgFont Finder Lm{ee6a863e-c039-4f97-af7c-dd4f65e7af95}Classroom Meeting Link Checker{fb6bc162-d129-45d1-8da9-7a132342b667}ZimRim Search Extensionzimrim-extension@mozilla.orgZimRim Extension{ccd4a5ce-0a3b-449e-b3f8-43a90ec7aaa9}HipDashdev@hipdash.comLANeros - Galería De Imagenescarlos.gaviria.gallego1@outlook.comPriberam dictionary searchpriberam_dictionary_search_@voila.techSite Annonceextension@classified-media.com↩
2. This article was published in April 2026, but the first version, including the scraping scripts, were written in September 2025. I reran the final script and asked Claude to update the numbers. It worked backwards using my intermediate files instead of rescraping (rescraping would be inaccurate since the data had changed by then), and I think the numbers are accurate enough. I updated the missing extension counts myself because it assumed the final count was 84,000 (like I had written) and not 84,243.↩↩2
3. Foreshadowing is a literary device that writers utilize as a means to indicate or hint to readers something that is to follow or appear later in a story↩