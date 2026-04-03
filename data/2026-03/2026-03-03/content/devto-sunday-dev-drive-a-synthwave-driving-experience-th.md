---
title: 'Sunday DEV Drive: A Synthwave Driving Experience Through Your DEV Community Articles'
url: https://dev.to/georgekobaidze/sunday-dev-drive-a-synthwave-driving-experience-through-your-dev-community-articles-5032
site_name: devto
content_file: devto-sunday-dev-drive-a-synthwave-driving-experience-th
fetched_at: '2026-03-03T06:00:50.976294'
original_url: https://dev.to/georgekobaidze/sunday-dev-drive-a-synthwave-driving-experience-through-your-dev-community-articles-5032
author: Giorgi Kobaidze
date: '2026-03-01'
description: 'This is a submission for the DEV Weekend Challenge: Community The Community ... Tagged with devchallenge, weekendchallenge, showdev.'
tags: '#showdev, #devchallenge, #weekendchallenge'
---

DEV Weekend Challenge: Community

This is a submission for theDEV Weekend Challenge: Community

## The Community

### Let's Start from the Very Beginning

I love weekends. Not because I want to escape coding, quite the opposite. As a full-time principal engineer, my weekdays belong to meetings, architecture decisions, reviews, and production responsibilities. Evenings are short. Energy is limited. But weekends? Weekends are different. Weekends are pure.

They're the only time I can dedicate an entire day to building something just for the joy of it. Writing. Experimenting. Creating.

Recently, I started participating in DEV challenges and it's been one of the best decisions I've made in a long time. There's something powerful about building in public. Shipping something playful and sharing it with your community.

This challenge, in particular, just felt right -the weekend challenge.

### To the Community I Call Home

The DEV community has been my home since 2017, since the very beginning of myprofessionalsoftware engineering journey.

More often than not, I found comfort here when things weren't going well. Especially in those early years. When imposter syndrome was loud. When mistakes felt heavier. When growth felt slow.

Reading other developers' stories helped. Seeing their struggles. Their wins. Their lessons. It all reminded me that we're all just figuring it out.

Now, years later, I wanted to give something back.

I wanted to build something that would:

* Make fellow members smile.
* Help them feel proud of their work.
* Turn their articles into something interactive.
* Encourage passive members to write.
* Maybe even inspire non-members to join.

Something actually different... something actually fun...

## What I Built

### So I Built Sunday DEV Drive

Sunday DEV Drive is a game, but not in the traditional sense.

There are no bosses to defeat, no side quests, no objectives, no timers.

It's intentionally different.

It's a browser-based synthwave driving game where your DEV Community articles become neon billboards along an endless procedural road. You type in a username, and within seconds you're cruising through a retro-futuristic cityscape with your article titles, cover images, and actual quotes from your writing towering above the highway.

And as you drive, billboards around the city display articles - yours or someone else's, pulled dynamically using theDEV API.

Imagine cruising through a digital city and suddenly seeing your own words glowing above you.

Or discovering another developer's article while driving past a virtual skyline.

It's not about winning, it's about reflecting, it's all about feeling proud and transforming written content into a spatial experience.

### It Works in Three Modes

* Your articles: Enter any DEV username. The game fetches their posts via the DEV API, extracts real quotes from article bodies, and renders them onto billboard textures in real-time.
* Motivational mode: If a user has an account but no articles yet, every billboard becomes an encouraging message with "Click here to start writing!" - each one linking directly todev.to/new.
* Test drive: No DEV account? No problem. Take a demo spin and let the game convince you to join the community, every billboard becomes an invitation.

Every billboard is clickable. See a post you want to read? Click it, and it opens in a new tab.

Beyond billboards, green road signs display your profile stats as you drive: total articles, lifetime reactions, reading time, your top post, favorite tags, and the date you joined DEV.

But wait, there's more.

You can even switch to first-person mode and drive straight from the cabin for full immersion.

### The Idea Behind It

We usually consume articles passively, scrolling on a feed. But what if your writing became part of a world? What if your thoughts lived on digital billboards? What if discovering developers felt like exploring a city instead of browsing a list?

Sunday DEV Drive turns articles into scenery. It makes community content feel tangible.

### More Than Just a Game

At its core, this project is a thank-you letter.

To the platform.To the writers.To the readers.To the beginners who are still doubting themselves.

If you've ever published even one article, you deserve to see it shining in neon.

If you've been thinking about writing, maybe this is your sign. WHAT ARE YOU WAITING FOR? START NOW. A year from now, you'll wish you'd started today. Regret is avoidable by taking action.

Welcome to Sunday DEV Drive!🚗✨

## Demo

Try it yourself: 🔗sundaydevdrive.pilotronica.com

Try it with your own DEV username, or just hit "Take a test drive" to jump right in.

GAME CONTROLLER SUPPORT INCLUDEDPlug in a controller and enjoy the experience.

## Code

The entire codebase is public, dive into the repository and take a look:

## georgekobaidze/sunday-dev-drive

### A synthwave driving experience through your DEV Community articles

# Sunday DEV Drive

A synthwave driving experience through your DEV Community articles

Live Demo•Features•Controls•How It Works

## Live Demo

🔗sundaydevdrive.pilotronica.com

## About

Enter yourDEV Communityusername, hitStart Driving, and cruise through a neon-lit synthwave world where your articles appear as roadside billboards. Each billboard shows a title, cover image, and a snippet from the article body. Click any to open the full post.

Built for theDEV Weekend Challenge: Build for Your Community.

## Features

### Your Articles as Billboards

Roadside and overhead signs generated from your real DEV posts, complete with cover images, snippets, and reaction counts.

### Stat Signs Along the Road

Green road signs display your profile stats: total articles, reactions, reading time, top post, favorite tags, and join date.

### Keyboard & gamepad support

Drive with arrow keys or plug in a controller. Full analog steering, throttle, and a right-stick orbit…

View on GitHub

Don't judge the JavaScript too harshly, I come from the land of APIs and databases - I'm a back-end developer through and through.

## How I Built It

### The Stack

* Three.js(r170) - 3D rendering, loaded via ES module import maps from CDN
* Vanilla JavaScript- 12 ES modules, zero build step, zero bundler, zero npm dependencies
* Canvas API- Every billboard and road sign texture is drawn programmatically
* DEV API- Public endpoints, no API key, no backend

No React. No Vite. No webpack. Openindex.htmlwith any static file server and drive.

### The Architecture

The entire project is 12 ES modules with a clean dependency graph and zero circular imports:

scene.js ← road.js ← buildings.js
 ← car.js ← camera.js
 ← input.js
 ← billboards.js ← stats.js ← api.js
main.js imports everything

Enter fullscreen mode

Exit fullscreen mode

Each module owns its domain:road.jsgenerates the path,car.jsbuilds the car,billboards.jshandles the article-to-texture pipeline. Themain.jsentry point wires them together and runs the animation loop.

### Procedural Road Generation: Stochastic Steering

The road is infinitely generated as you drive. There's no predefined track, it grows segment by segment using a stochastic steering algorithm:

export
 
function
 
growPath
(
count
)
 
{

 
for 
(
let
 
i
 
=
 
0
;
 
i
 
<
 
count
;
 
i
++
)
 
{

 
if 
(
--
pathTurnCountdown
 
<=
 
0
)
 
{

 
pathTurnRate
 
=
 
(
Math
.
random
()
 
-
 
0.5
)
 
*
 
0.042
;

 
pathTurnCountdown
 
=
 
4
 
+
 
Math
.
floor
(
Math
.
random
()
 
*
 
6
);

 
}

 
pathHead
.
angle
 
+=
 
pathTurnRate
;

 
pathData
.
push
({
 
pos
:
 
pathHead
.
pos
.
clone
(),
 
angle
:
 
pathHead
.
angle
 
});

 
pathHead
.
pos
 
=
 
new
 
THREE
.
Vector3
(

 
pathHead
.
pos
.
x
 
+
 
Math
.
sin
(
pathHead
.
angle
)
 
*
 
SEGMENT_LEN
,

 
0
,

 
pathHead
.
pos
.
z
 
-
 
Math
.
cos
(
pathHead
.
angle
)
 
*
 
SEGMENT_LEN

 
);

 
}

}

Enter fullscreen mode

Exit fullscreen mode

Every few segments, a new random turn rate and duration are chosen. Because the turn rateaccumulatesover multiple segments rather than being applied instantly, the road produces smooth, organic curves, gentle sweeps, not jarring zigzags. Randomizing both the magnitude (0.042range) and the duration (4–10 segments) creates surprising variation from very simple math.

The road surface itself is a ribbon mesh: a sliding window of 200 segments rebuilt from rawBufferGeometry. For each segment, perpendicular edge points are computed using the path angle:

const
 
rx
 
=
 
Math
.
cos
(
pd
.
angle
);

const
 
rz
 
=
 
Math
.
sin
(
pd
.
angle
);

const
 
lx
 
=
 
pd
.
pos
.
x
 
-
 
rx
 
*
 
ROAD_WIDTH
 
/
 
2
;
 
// Left edge

const
 
hx
 
=
 
pd
.
pos
.
x
 
+
 
rx
 
*
 
ROAD_WIDTH
 
/
 
2
;
 
// Right edge

Enter fullscreen mode

Exit fullscreen mode

The ribbon follows the car. When you've driven far enough, the mesh is rebuilt centered around your position. The road is always beneath you, and always extends into the horizon.

### Canvas-Rendered Billboard Textures

This is where the DEV API meets the Canvas API. Every billboard texture is a512×768canvas (roadside) or1024×512canvas (overhead), painted section by section:

1. Header bar- neon-bordered strip with author and reaction count
2. Cover image- letterboxed from the article'scover_imageURL, loaded asynchronously
3. Snippet- an actual quote extracted from the article body
4. Footer- reading time and tag display

The tricky part: cover images loadafterthe texture is already applied to the 3D mesh. Three.js handles this beautifully withtex.needsUpdate = true:

if 
(
article
.
cover_image
)
 
{

 
const
 
img
 
=
 
new
 
window
.
Image
();

 
img
.
crossOrigin
 
=
 
'
anonymous
'
;

 
img
.
onload
 
=
 
()
 
=>
 
{

 
drawImageLetterbox
(
img
,
 
cx
,
 
cy
,
 
cw
,
 
ch
);

 
tex
.
needsUpdate
 
=
 
true
;
 
// GPU re-uploads on next frame

 
};

 
img
.
src
 
=
 
article
.
cover_image
;

}

Enter fullscreen mode

Exit fullscreen mode

For articles without cover images, the cover area becomes a playful "404 / cover_image: null / (the author was too busy)" message, complete with a retro grid background. In motivational mode, it reads "Click here to start writing!" instead.

### Snippet Extraction: Turning Markdown Into Billboard Quotes

Simply showing article titles on billboards wouldn't be enough. I wanted actualquotesfrom people's writing. But the DEV API returns raw Markdown, not clean prose. The extraction pipeline strips away code blocks, images, links, and headers, then picks paragraphs in a sweet spot - long enough to be meaningful, short enough to fit a billboard.

The 60-400 character filter is crucial. Too short and you get orphaned sentences. Too long and the text overflows the billboard canvas. The result: clean, readable quotes that actually represent what someone wrote.

### Car Physics: The Struggle Effect When Both Pedals Are Pressed

The driving model is simple but has one detail I'm proud of. When a player presses both throttle and brake simultaneously (a common thing with gamepads), instead of canceling out, the car settles into a "struggle" state, which is basically low speed, high engine strain:

if 
(
throttle
 
>
 
0
 
&&
 
brake
 
>
 
0
)
 
{

 
const
 
struggle
 
=
 
CAR
.
maxSpeed
 
*
 
0.08
;

 
carState
.
speed
 
+=
 
(
struggle
 
-
 
carState
.
speed
)
 
*
 
0.04
;

}

Enter fullscreen mode

Exit fullscreen mode

The speed converges to 8% of max through lerp smoothing. It simulates the feeling of fighting the brakes, the car doesn't stop, doesn't accelerate, just vibrates with restrained energy. It's a small detail but it makes the physics feelalive.

Acceleration also uses diminishing returns, the faster you're going, the harder it is to go faster:

const
 
speedRatio
 
=
 
carState
.
speed
 
/
 
CAR
.
maxSpeed
;

const
 
effectiveAccel
 
=
 
CAR
.
acceleration
 
*
 
throttle
 
*
 
(
1
 
-
 
speedRatio
 
*
 
0.85
);

Enter fullscreen mode

Exit fullscreen mode

This single line replaces what would otherwise be a complex drag model. At zero speed, you get 100% acceleration. At top speed, you get 15%. The curve in between is completely smooth.

### The 25-Article Shuffle

The DEV API has a quirk: the list endpoint returns titles and metadata, but not the full article body. To get actual text for snippet extraction, you need a separate request per article. For a user with hundreds of posts, that's hundreds of requests - too slow and too aggressive.

And I'm not planning to brutally overload our favorite creators' platform. I'll be easy on it. So Jess, Ben, Peter, if you're reading this, don't worry, I got you.😄

The solution: shuffle the full article list and deep-fetch only 25 random articles. The rest get theirdescriptionfield as a fallback snippet:

const
 
shuffled
 
=
 
[...
list
].
sort
(()
 
=>
 
Math
.
random
()
 
-
 
0.5
);

const
 
toFetch
 
=
 
shuffled
.
slice
(
0
,
 
25
);

for 
(
const
 
art
 
of
 
toFetch
)
 
{

 
const
 
r
 
=
 
await
 
fetch
(
`https://dev.to/api/articles/
${
art
.
id
}
`
);

 
if 
(
r
.
status
 
===
 
429
)
 
{
 
art
.
_snippets
 
=
 
[
art
.
description
 
||
 
''
];
 
continue
;
 
}

 
const
 
full
 
=
 
await
 
r
.
json
();

 
art
.
_snippets
 
=
 
extractSnippets
(
full
.
body_markdown
 
||
 
''
);

 
await
 
new
 
Promise
(
res
 
=>
 
setTimeout
(
res
,
 
350
));

}

Enter fullscreen mode

Exit fullscreen mode

Each request has a 350ms delay to respect rate limits. If the API returns 429 (Too Many Requests), it gracefully falls back to the description instead of failing. The player never notices, they just see billboards with quotes. Whether those quotes came from a full article parse or a description fallback is invisible.

### Billboard Click Detection via Raycasting

Clicking a 3D billboard to open an article isn't trivial in a 3D scene. The solution is Three.js raycasting, converting a 2D mouse position into a 3D ray, then testing intersection against billboard geometry.

Each billboard stores its article URL inuserData. The raycast checks both front and back panels, so billboards work no matter which direction you're looking at them from. Theorbit.activeguard prevents accidental clicks during camera rotation.

### Building a Car from 46 Boxes

When I was a kid, I'd grab random little wooden scraps nobody seemed to need (or at least I thought nobody needed), hammer them together into a rough car shape, and nail four bottle caps on as wheels. Perfect toy car. Good times.

Who would've thought that, more than 20 years later, the same "stack-and-nail" approach would actually come in handy... in code.

There are no 3D models in this project. Every part of the car like body, cabin, hood, trunk, wheels, rims, windows, dashboard, headlights, tail/brake/reverse lights, steering wheel, interior screens, is built entirely from BoxGeometry and CylinderGeometry primitives, carefully stacked and positioned by hand.

And boy did I spend a lot of time on that! Totally worth it.

Lower body → Mid body → Hood → Trunk → Cabin
→ 4× Wheels (cylinder + torus rim)
→ 4× Windows (transparent glass material)
→ Dashboard with neon trim + dual screens
→ Steering wheel (torus + cylinder spokes)
→ Headlights (emissive mesh + PointLight)
→ Tail/brake/reverse lights

Enter fullscreen mode

Exit fullscreen mode

The steering wheel actually rotates when you turn:

const
 
sw
 
=
 
car
.
userData
.
steeringWheel
;

if 
(
sw
)
 
sw
.
rotation
.
z
 
=
 
-
carState
.
steer
 
*
 
0.5
;

Enter fullscreen mode

Exit fullscreen mode

Visible only in interior camera mode, but it's there. These kinds of details don't matter until they do.

### So Much More to Talk About

This project was a blast to build. Every component of the game required a ton of thought, and I learned so much along the way. What I've shared here are just the most exciting parts, there are plenty of other fascinating details. If I included everything, I'd probably end up writing a book. Maybe that's a story for another day.

### What I Learned This Weekend

Building a 3D game with zero dependencies and zero build tools in a weekend taught me a few things:

1. The Canvas API is absurdly powerful for textures.Every billboard, every road sign, the sun, the skyline, all drawn withfillRect,fillText, anddrawImage. No texture files needed.
2. ES modules are production-ready.Import maps + CDN +type="module"gives you a complete module system with zero tooling. Twelve modules, clean dependency graph, no bundler.
3. Simple physics beat complex physics.A one-line diminishing-returns formula (1 - speedRatio * 0.85) gives more "feel" than a proper friction simulation would. Games aren't simulations, they're about how things feel.
4. The DEV API is a goldmine.Public, no auth, generous rate limits, full Markdown body access. Buildingforthe community with the community's own API felt right.

This project was built in a weekend with coffee, a gamepad, and a deep appreciation for the DEV Community. Every article you've written deserves to be a neon billboard on an endless synthwave highway.

Now it's your turn. Take your car for a spin, share your journey in the comments, grab screenshots and show it off to your friends, colleagues... anyone! I'd love to hear everyone's reaction. Let's show everyone that we're by far the best community.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (20 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse