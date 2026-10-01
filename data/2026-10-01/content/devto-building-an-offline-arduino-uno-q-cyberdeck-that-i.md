---
title: Building an Offline Arduino UNO Q Cyberdeck That Identifies Birdsong and Draws Vintage Field Notes - DEV Community
url: https://dev.to/cloudinary/building-an-offline-arduino-uno-q-cyberdeck-that-identifies-birdsong-and-draws-vintage-field-notes-1cjg
site_name: devto
content_file: devto-building-an-offline-arduino-uno-q-cyberdeck-that-i
fetched_at: '2026-10-01T17:18:15.906441'
original_url: https://dev.to/cloudinary/building-an-offline-arduino-uno-q-cyberdeck-that-identifies-birdsong-and-draws-vintage-field-notes-1cjg
author: Jen Looper
date: '2026-09-30'
description: In this post, I walk through B.L.O.O.M. (Bridging Local Observations, Openly Mapped), an offline... Tagged with arduino, iot, cloudinary, ai.
tags: '#arduino, #iot, #cloudinary, #ai'
---

In this post, I walk throughB.L.O.O.M.(Bridging Local Observations, Openly Mapped), an offline cyberdeck built on theArduino UNO Qthat helps naturalists capture field notes, identify birdsong withEdge Impulse, and generate vintage field sketches withCloudinary's image generation API. It stores everything locally and syncs to a community site only when you choose.

## What you'll learn

* How to wire an Arduino UNO Q cyberdeck with a USB hub, camera, mic and HDMI screen
* How to run a local Gemma LLM and an audio classifier with Arduino App Lab bricks
* How to retrain an Edge Impulse birdsong model with balanced data
* How to sync SQLite entries to GitHub pull requests from a Netlify Function
* How to generate style-matched images with Cloudinary's image_to_image API with reference images

Cyberdecks are back. The 80s sci-fi dream of a portable, hackable computer rig has been picked back up, especially by nature-loving corners of the internet that want tech that works offline, respects privacy, and looks cool doing it. The one I built for this project lives in a $10 vintage makeup train case and createsGrinnell style field notesas you tiptoe through the tulips.

This post covers thehardware-to-cloud pipeline, with the most detail on the part where Cloudinary comes in. The full build (wiring, enclosure, every step) is onHackster.

The architecture at a glance

┌──────────── In the field (offline) ────────────┐ ┌────────────── Back online ──────────────┐
│ │ │ │
│ Mic ─► Edge Impulse birdsong model │ │ Netlify Function │
│ Camera ─► photo │ POST │ ├─► Cloudinary image_to_image │
│ Keyboard/mouse ─► sketch + notes ─► SQLite ├───────►│ │ (Nano Banana → field sketch) │
│ Gemma LLM ─► AI note │ │ └─► Octokit: open PR on GitHub │
│ │ │ │ │
│ Arduino UNO Q (App Lab, Chromium kiosk) │ │ merge ─► Astro rebuild ─► live site │
└────────────────────────────────────────────────┘ └──────────────────────────────────────────┘

Enter fullscreen mode

Exit fullscreen mode

Nothing leaves the device unless you press Sync to Cloud. That was a hard requirement, as this project is affiliated as well with the nonprofit I founded,Her AI Studio, where we talk a lot about data governance, security, and privacy, working primarily with local AI on device.

Here's the full schematic:

The core of the cloud side is a single POST to Cloudinary:

{

 
"prompt"
:
 
"Create a field sketch illustration in the style of the reference image [1]..."
,

 
"reference_images"
:
 
[{
 
"source_type"
:
 
"url"
,
 
"url"
:
 
"<your reference sketch>"
 
}],

 
"model"
:
 
{
 
"family"
:
 
"nano-banana"
,
 
"tier"
:
 
"premium"
 
},

 
"target"
:
 
{
 
"target_type"
:
 
"managed_asset"
,
 
"public_id"
:
 
"field-notes/<slug>-ai"
 
}

}

Enter fullscreen mode

Exit fullscreen mode

The full function is below.

## Hardware: the Arduino UNO Q parts list

* Arduino UNO Q (4 GB)
* 5" HDMI screen + 6" HDMI cable
* USB 5-in-1 hub
* USB camera
* USB microphone
* Power bank + USB-A to Micro-USB cable
* Bluetooth keyboard with built-in mouse pad
* Vintage train case (or the enclosure you like best! This is the fun part)

TheArduino UNO Qruns everything. The 4 GB variant can run a small language model and an audio classifier fully offline, which is what makes the device useful on a forest trail with no signal...and to explore offline, local AI models on hardware!

Because it's a cyberdeck, there are peripherals, and those are all connected to the USB hub: screen, mic, camera and power go into the hub, and the hub's USB-C plug goes into the UNO Q. Pair the keyboard and mouse over Bluetooth in Debian and you get those USB ports back.

AtHer AI Studio, students will get access to this AI Kit.

## Running Gemma and birdsong detection on the UNO Q with App Lab

The app is built in Arduino App Lab from three "bricks", which are modular code available pre-built for the Arduino Uno Q:

* Web UI for the interface with camera and sketching interface
* LLM brick running Gemma, downloaded locally to the board
* Audio Classification brick for birdsong

The Web UI brick helps you build a tidy interface with a little JS and HTML that runs on your local board via Arduino App Lab. This is how you write your field notes. The LLM brick creates a little space to chat with an LLM and learn more about the flora and fauna photos that you take with the build-in camera.

Side Quest: Fixing Chromium popups on Debian with a kiosk brickOn Debian, the stock Web UI brick opened Chromium popups behind other windows. It worked fine on desktop but not on the device. I fixed it with a small custom brick that waits for the local server and then launches Chromium in kiosk mode:

def
 
build_kiosk_command
(
url
:
 
str
):

 
if
 
system
 
==
 
"
Linux
"
:

 
return
 
[
"
chromium-browser
"
,
 
"
--kiosk
"
,
 
"
--noerrdialogs
"
,

 
"
--disable-infobars
"
,
 
f
"
--app={url}
"
]

def
 
launch_kiosk
(
url
:
 
str
,
 
ready_timeout
:
 
float
 
=
 
15.0
):

 
if
 
not
 
wait_for_server
(
url
,
 
timeout
=
ready_timeout
):

 
logger
.
error
(
f
"
Server never became reachable at {url}
"
)

 
return
 
None

 
cmd
 
=
 
build_kiosk_command
(
url
)

 
logger
.
info
(
f
"
Launching: {' '.join(cmd)}
"
)

 
return
 
subprocess
.
Popen
(
cmd
)

Enter fullscreen mode

Exit fullscreen mode

The interface is presented full-screen without desktop chrome, so the screen is just the field notebook, like this:

## Listening for birds

I wanted to give my cyberdeck some "ears", so I turned to a platform that works well to add local, custom-trained models to Arduino via App Lab: Edge Impulse.

I started from a birdsong classifier in the Edge Impulse community gallery. It had class imbalance and too few samples, so I:

* Duplicated the project and removed unusable clips
* Pulled at least 20 recordings each of Blue Jay, Mourning Dove and Northern Cardinal fromxeno-canto, a birdsong database
* Converted everything to WAV, labeled it, and uploaded it
* Rebalanced the train/test split and retrained
* Dropped the new model into the App Lab project

When your USB microphone picks up a bird singing, you tap a button, the model classifies the audio, and the result is saved into a field note. The model ispublic and cloneableif you want to add your local species.

## Syncing: from SQLite to a pull request

Every observation is stored in a local SQLite database, but maybe you want to showcase your field notes to our public repository. When you choose to share, the device posts the entry to a Netlify Function. Photos and sketches are base64-encoded so the whole entry travels as one JSON payload:

def
 
sync_entry
(
entry_id
):

 
with
 
_db_lock
:

 
conn
 
=
 
sqlite3
.
connect
(
DB_PATH
)

 
row
 
=
 
conn
.
execute
(

 
"
SELECT id, timestamp, photo, sketch, ai_note, locality, weather, habitat 
"

 
"
FROM entries WHERE id = ?
"
,

 
(
entry_id
,)

 
).
fetchone
()

 
conn
.
close
()

 
eid
,
 
timestamp
,
 
photo
,
 
sketch
,
 
ai_note
,
 
locality
,
 
weather
,
 
habitat
 
=
 
row

 
payload
 
=
 
{

 
"
id
"
:
 
eid
,

 
"
catalog_no
"
:
 
catalog_number
(
eid
),

 
"
timestamp
"
:
 
timestamp
,

 
"
note
"
:
 
ai_note
 
or
 
""
,

 
"
locality
"
:
 
locality
 
or
 
""
,

 
"
weather
"
:
 
weather
 
or
 
""
,

 
"
habitat
"
:
 
habitat
 
or
 
""
,

 
"
photo
"
:
 
base64
.
b64encode
(
photo
).
decode
(
"
utf-8
"
)
 
if
 
photo
 
else
 
None
,

 
"
sketch
"
:
 
base64
.
b64encode
(
sketch
).
decode
(
"
utf-8
"
)
 
if
 
sketch
 
else
 
None
,

 
}

 
response
 
=
 
requests
.
post
(
CLOUD_SYNC_URL
,
 
json
=
payload
,
 
timeout
=
CLOUD_SYNC_TIMEOUT
)

The
 
function
 
does
 
not
 
write
 
to
 
a
 
database
.
 
It
 
opens
 
a
 
pull
 
request
 
against
 
the
 
field
-
notes
 
repo
 
with
 
Octokit
:

const
 
{
 
data
:
 
pr
 
}
 
=
 
await
 
octokit
.
pulls
.
create
({

 
owner
:
 
OWNER
,

 
repo
:
 
REPO
,

 
title
:
 
`New field note: ${catalog_no}`
,

 
head
:
 
branchName
,

 
base
:
 
BASE_BRANCH
,

 
body
:
 
[

 
"
Submitted automatically from a Bloom device.
"
,

 
""
,

 
`**Locality:** ${locality || "—"}`
,

 
`**Weather:** ${weather || "—"}`
,

 
`**Habitat:** ${habitat || "—"}`
,

 
aiSketchPath
 
?
 
"
\n
_AI-generated sketch included._
"
 
:
 
null
,

 
].
filter
((
line
)
 
=>
 
line
 
!==
 
null
).
join
(
"
\n
"
),

 
labels
:
 
[
"
device-submission
"
],

});

Enter fullscreen mode

Exit fullscreen mode

This process makes it easier for the community site to get human moderation: a maintainer reviews the PR, merges it, and Netlify rebuilds the Astro site. You can see the results atcommunity-field-notes.netlify.app.

Generating AI field sketches with Cloudinary's image_to_image APINaturalists in the Grinnell tradition paired written notes with drawings. I wanted every synced note to come with an illustration in that vintage style, even if the person who wrote it can't draw.

Before the PR is opened, the Netlify Function sends the note text to Cloudinary's image generation API using the image_to_image endpoint and the Nano Banana model. I also pass a reference image, an old-style field sketch already stored in my Cloudinary account, so every output matches the same look:

async
 
function
 
generateAiSketch
(
noteText
,
 
slug
)
 
{

 
const
 
prompt
 
=
 
[

 
"
Create a field sketch illustration in the style of the reference image [1].
"
,

 
"
The sketch should depict:
"
,

 
noteText
 
||
 
"
A natural world observation
"
,

 
"
Use a vintage field journal aesthetic with earthy tones, hand-drawn quality, and scientific illustration style.
"
,

 
].
join
(
"
 
"
);

 
const
 
auth
 
=
 
Buffer
.
from
(

 
`
${
CLOUDINARY_API_KEY
}
:
${
CLOUDINARY_API_SECRET
}
`

 
).
toString
(
"
base64
"
);

 
const
 
response
 
=
 
await
 
fetch
(

 
`https://api.cloudinary.com/v2/generate/
${
CLOUDINARY_CLOUD_NAME
}
/image_to_image`
,

 
{

 
method
:
 
"
POST
"
,

 
headers
:
 
{

 
"
Content-Type
"
:
 
"
application/json
"
,

 
Authorization
:
 
`Basic 
${
auth
}
`
,

 
},

 
body
:
 
JSON
.
stringify
({

 
prompt
,

 
reference_images
:
 
[

 
{
 
source_type
:
 
"
url
"
,
 
url
:
 
REFERENCE_IMAGE_URL
 
},

 
],

 
model
:
 
{
 
family
:
 
"
nano-banana
"
,
 
tier
:
 
"
premium
"
 
},

 
target
:
 
{

 
target_type
:
 
"
managed_asset
"
,

 
public_id
:
 
`field-notes/
${
slug
}
-ai`
,

 
},

 
}),

 
}

 
);

 
// ...handle response, return the asset path for the PR

}

Enter fullscreen mode

Exit fullscreen mode

### A few things I like about this setup:

* The use of the reference image keeps the style consistent, and you can either choose the model, or keep it set to 'auto' - so that the model is chosen for you based on your use case.
* The prompt describes what to draw, and the reference image sets how it should look. Swap the reference and every future note gets a new visual identity.
The target_type: "managed_asset" saves the output straight into my Cloudinary media library under a predictable public_id (field-notes/-ai). I don't have to download and re-upload anything, and the image is ready for delivery to my community field notes app.
* After that it's a normal Cloudinary asset, so the site can deliver it with the usual transformations: f_auto,q_auto, resizing for cards and thumbnails, and so on.
* It's one fetch call. No SDK and no extra infrastructure, which suits a serverless function.

### Setup tips

* Keep CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY and CLOUDINARY_API_SECRET in Netlify environment variables. Never put them on the device.
* Upload your reference sketch to Cloudinary first and use its delivery URL as REFERENCE_IMAGE_URL.
* The Image Generation API has a free monthly allowance, which covers a community project like this. If you don't have an account yet, sign up for free.

## The enclosure: no 3D printer needed

Instead of printing a case, I reused one (preferable for cyberdecks!): a vintage Lancôme makeup train case, costing about $10 on eBay. Here's what I did to fit everything in the case:

* Cut a small hole in the side for the camera lens
* Build shelves from recycled foam and fabric
* Zip-tie the USB hub in place
* Made a cardboard backing for the screen, with room for cables
* Gave the UNO Q its own spot, with airflow in mind (foam and fabric trap heat, so watch temperatures or use an open weave like rattan - I've even used a sushi rolling mat for this type of shelf)

The tall case also leaves room for a magnifier, pressed flowers, a small watercolor set, or a leaf guide.

the author enjoying a Fall day of field notes

## Go touch grass: using B.L.O.O.M. in the field

Power it on, head outside, and record what you find: birdsong, photos, sketches, questions for the LLM, locality, weather and habitat. When you're back on Wi-Fi, press sync to send the note to GitHub, get a Cloudinary-generated sketch, and add it to a shared natural-history record.

Discover new fauna

## Resources

📖 Full build on Hackster:B.L.O.O.M.: A Community Cyberdeck for your Field Notes

💻 Device code:

## Her-AI-Studio/BLOOM-code

### This is the codebase for use in Arduino App Lab, for the Arduino Uno Q in a cyberdeck

# B.L.O.O.M — an offline field journal

Bridging Local Observations, Openly Mapped

B.L.O.O.Mturns an Arduino® UNO Q into a self-powered, offline field-journal cyberdeck: point it at a plant, an animal, or anything worth noticing on a hike, capture a photo, sketch on top of it, and talk through what you're observing with a fully local AI model. Every entry — photo, sketch, and note — is saved to the board itself and stays there unless you deliberately choose to sync it to a companion website. No connectivity is required to use it in the field.

Built for Her AI Studio's curriculum and submitted for hackathons including theInvent the Future with Arduino UNO Q and App Labcontest, Best Social Impact category — the pitch is a countermeasure to phone-and-camera culture: a single-purpose device that makes you stop, point, and wait for a note instead of snapping and swiping past.

…

View on GitHub

🌐Community web app (Astro + Netlify)

## Her-AI-Studio/field-notes

### This is the core code of the offline, locally-powered cyberdeck for use when hiking

# Field Notes

A digital field journal — a collection of natural history observations, surveys, and records from the field.

Built withAstroand Markdown content collections.

## Project Structure

/
├── public/
│ └── favicon.svg
├── src/
│ ├── content/
│ │ ├── config.ts
│ │ └── notes/
│ │ ├── observation-of-the-red-shouldered-hawk.md
│ │ ├── botanical-survey-of-coastal-dune-ecology.md
│ │ ├── geological-observations-along-the-appalachian-trail.md
│ │ └── nocturnal-insect-survey-june.md
│ ├── layouts/
│ │ └── Layout.astro
│ ├── pages/
│ │ ├── index.astro
│ │ └── notes/
│ │ └── [...slug].astro
│ └── styles/
│ └── global.css
└── package.json

## Adding a New Note

Create a new.mdfile insrc/content/notes/with frontmatter:

---

title
: 
"
Your Note Title
"

date
: 
2026-07-21

location
: 
"
Location, State
"

excerpt
: 
"
A brief summary of the observation.
"

image
: 
"
/images/your-image.jpg
"

tags
: 
["tag1", "tag2"]

---

Enter fullscreen mode

Exit fullscreen mode

The note will automatically appear on the…

View on GitHub

🐦Edge Impulse birdsong model

If you build a nature-loving cyberdeck like this, contribute a note to the website, or retrain the model for birds near you, share it in the comments. I'd like to see what other people's field notes look like and what you're looking at in your region. 🌿

Cloudinary ❤️ developers

Ready to level up your media workflow? Start using Cloudinary for free and build better visual experiences today.

👉 
Create your free account

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse