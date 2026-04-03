---
title: 'Metal Birds Watch: Copilot CLI Helped Me Watch Planes Without Looking Up - DEV Community'
url: https://dev.to/georgekobaidze/metal-birds-watch-copilot-cli-helped-me-watch-planes-without-looking-up-4ha0
site_name: devto
content_file: devto-metal-birds-watch-copilot-cli-helped-me-watch-plan
fetched_at: '2026-02-17T11:20:06.116937'
original_url: https://dev.to/georgekobaidze/metal-birds-watch-copilot-cli-helped-me-watch-planes-without-looking-up-4ha0
author: Giorgi Kobaidze
date: '2026-02-13'
description: This is a submission for the GitHub Copilot CLI Challenge Table of Contents Demo What I... Tagged with devchallenge, githubchallenge, cli, githubcopilot.
tags: '#devchallenge, #githubchallenge, #cli, #githubcopilot'
---

GitHub Copilot CLI Challenge Submission

This is a submission for theGitHub Copilot CLI Challenge

## Table of Contents

* Demo
* What I BuiltThe IdeaSo, What Does It Do?Turns Out, It Wasn't That SimpleThe SolutionA Few Words About the Tech Stack
* The Idea
* So, What Does It Do?
* Turns Out, It Wasn't That Simple
* The Solution
* A Few Words About the Tech Stack
* My Experience with GitHub Copilot CLISo Here's the Conclusion:And One Last Thing
* So Here's the Conclusion:
* And One Last Thing
* Credits
* Useful Links

## Demo

In this video, I not only present the demo, but also walk through the core purpose and motivation behind the project. I dive into the architecture and design decisions in detail, explaining how everything fits together and why certain approaches were chosen.

You can check out the video chapters if you'd like to jump to a specific part, but I highly recommend watching the full video to get the complete picture and fully understand how everything connects.

## What I Built

### The Idea

I love airplanes, traveling, airports, the sound of engines, everything related to aviation. For a long time, I've wanted to build something connected to that world. I just needed the right excuse.

Then this challenge appeared. This was my though process:

Okay, this challenge looks fun. I need to use Copilot CLI.Alright, but what do I build? It has to be authentic. Cool. Creative and actually useful...

Copilot CLI...Copilot...Pilot...Airplanes...

And suddenly it clicked.

That was the momentMetal Birds Watchwas born.

What started as a word association turned into a real-time aircraft tracking app that notifies you when planes fly over you. Sometimes ideas don't come from complex brainstorming sessions, sometimes they come from connecting a few dots and letting your curiosity do the rest.

This challenge didn't just give me a prompt, it gave me the push I needed to finally build something I'd been thinking about for years. And I'm insanely proud of how it turned out.

### So, What Does It Do?

As a regular aircraft nerd, I instinctively look up at the sky every time I hear an engine overhead. I try to guess the make and model, the airline, maybe even where it took off from or where it's heading. It's like a little game (I'm not the best at it though, my brother and mom absolutely destroy me at this game, they make me look like I've never seen a plane in my life).

But there's one problem.

I can't just stand outside all day watching planes. Most of the time I'm working - coding, building things, solving problems. I'm a busy guy, too busy.

Sure, there are plenty of websites where you can track airplanes from all around the world in real time. But that still requires actively watching a screen. And again... I'm way too busy for that.

So I decided to build something that would "watch the sky" for me.

I use quotation marks because it doesn't literally watch the sky, it taps into real-time public flight data and detects when aircraft enter my area. When that happens, it sends me a notification. And if I miss it, the plane is still logged in my browser so I can check later and see what flew over my head.

Instead of me watching planes, the app watches them for me. Hence the nameMetal Birds Watch.

Try it out yourself using the following link:https://metalbirdswatch.pilotronica.com/

### Turns Out, It Wasn't That Simple

The whole concept sounds pretty straightforward right?

Fetch plane data periodically → filter by your area → trigger a notification. Easy!

Well, nuh-uh! The architecture and implementation turned out to be way more complex than the idea itself.

When you rely on a third-party public service, there are always limitations and rightfully so. Free APIs need rate limits. Without them, they'd be abused and become unusable for everyone.

The API I used for this challenge is no exception. It has strict request limits, and I have to respect the limits. If I exceed them, my app runs out of credits and simply stops working.

Usually when you're constrained by request limits or data quotas, the obvious solution is caching. Smart caching reduces the number of calls you make to the API provider. Great!

But then comes the real question:

How do you cache this kind of data?

There are tens of thousands of aircraft in the sky at any given moment, scattered across the globe. I needed to keep a fine balance between caching too aggressively (which could overload my storage and keep irrelevant data) and not caching enough (which would burn through API credits in minutes).

And that's where things started to get interesting.

On top of that, I made a deliberate decision to keep the system simple.

No persistent storage.

And more importantly, no sensitive data stored anywhere.

This is a privacy-first application. That means I don't store the user's location, IP address, or any personally identifiable information, not in a database, not in logs, not even in cache and any readable storage. Nor should it be retrievable via any endpoint.

By now, you can probably tell there are already quite a few moving parts in this system.

And we haven't even started talking about the actual solution yet.

### The Solution

#### A Note Before You Dive In

Disclaimer: This is one way to solve this problem, not the only way. There are many strategies and approaches you could take, and I'd love to hear your ideas or suggestions. Here's how I tackled it:

#### Caching by "Grid Cells"

I decided to cache plane data based on what I call grid cells - basically, areas where multiple airplanes might be present. Instead of tracking every user individually, I group users by coordinates, rounding them to the nearest grid cell.

Each grid cell is roughly0.2° latitude × 0.2° longitude, about22 km × 22 km. That's484 km².

For reference, San Francisco is121 km², so each grid cell is about four times larger.

Users are grouped by rounding their coordinates to nearest0.2°

Example:

User Aat(48.856, 2.352)→ grid cell48.8_2.4(cache key)

User Bat(48.772, 2.421)→ same grid cell48.8_2.4(same cache key)

Both users can get plane data for the area without storing their exact locations anywhere.

As you can see, User B falls within the same grid cell initialized by User A, so both users share the same cache entry48.8_2.4. Any user in this area will use the same entry.

#### Detection Radius

After the plane data is retrieved, each user only sees aircraft within a 12 km detection radius centered on their location. This filtering happens on the client side to minimize backend resource usage and keep the system flexible.

But there's an important edge case

If a user is near the edge of a grid cell, they might miss planes flying just outside the grid. Corner users could see only a quarter of the surrounding sky. See the diagram below for a better visualization:

The green planes (Plane A and Plane C) are cached and fall within the detection radii of their respective users so notifications will be triggered. ✅

The yellow plane (Plane B) is inside the grid cell, so it's cached as well. Users will see it on the page, but no notification will be sent until it enters one of the detection circles. ❌

The white planes (Plane E, Plane D, and Plane F), however, are outside the grid cell and therefore won't be cached, nor will they be shown on the map, even though Plane D is technically within the detection radius of User C. ❌

Now, this is a significant drawback, because it means some users might not receive fully accurate information about nearby planes.

And this is exactly where theBounding Boxstrategy saves the day.

#### Bounding Box

Fetching a slightly larger rectangle ensures everyone gets the full "all-around" view.

The backend actually fetches a 50 km × 50 km rectangle around the grid cell center, slightly larger than the grid itself, to ensure full coverage of the area.

See the diagram below for a clearer view:

As you can see, Plane D has just turned green, which means User C will now receive a notification about it.

Keep in mind: the bounding box serves a completely different purpose than the grid cell. If a new user appears within the bounding box but outside the existing grid cell, a new grid cell and consequently a new bounding box will be created for them. The bounding box's only job is to ensure that no planes are missed near the edges.

Looking at the diagram, you can see that the bounding box doesn't need to be this large, which is fine for now. In future versions of the app, users will be able to adjust their detection radius and making it bigger (or smaller).

#### Smart Polling

Clients don't poll the server at fixed intervals. Instead, the server tells each client when to request new data, based on cache freshness. This approach:

* Reduces unnecessary polling
* Saves bandwidth

#### Haversine Distance for Accuracy

To calculate the exact distance between a plane and a user, I use the Haversine formula, which measures distance on a sphere. This ensures accurate notifications, even for users near the edge of a grid cell.

This setup allows my app to provide real-time, privacy-first plane tracking, efficiently handling thousands of planes and users simultaneously.

#### Math Reference

### Constants

KM_PER_DEGREE_LAT = 111 km (constant everywhere)
KM_PER_DEGREE_LON = 111 × cos(latitude) km (varies by latitude)

Enter fullscreen mode

Exit fullscreen mode

### Why Longitude Varies

Earth is a sphere. Longitude lines converge at poles.

At equator (0°): 1° longitude = 111 km
At Paris (48.8°): 1° longitude = 111 × cos(48.8°) = 73 km
At Oslo (60°): 1° longitude = 111 × cos(60°) = 55.5 km
At poles (90°): 1° longitude = 0 km

Enter fullscreen mode

Exit fullscreen mode

### Converting km to Degrees

Δlat = distance_km / 111
Δlon = distance_km / (111 × cos(latitude))

Enter fullscreen mode

Exit fullscreen mode

### Bounding Box Calculation

Given center (φ, λ) and radius r km:

lat_min = φ - (r / 111)
lat_max = φ + (r / 111)
lon_min = λ - (r / (111 × cos(φ)))
lon_max = λ + (r / (111 × cos(φ)))

Enter fullscreen mode

Exit fullscreen mode

Example: 25km around Paris (48.8°, 2.4°)

Δlat = 25 / 111 = 0.225°
Δlon = 25 / (111 × cos(48.8°)) = 25 / 73 = 0.342°

lat_min = 48.8 - 0.225 = 48.575
lat_max = 48.8 + 0.225 = 49.025
lon_min = 2.4 - 0.342 = 2.058
lon_max = 2.4 + 0.342 = 2.742

Enter fullscreen mode

Exit fullscreen mode

### Grid Rounding

grid_lat = round(lat / 0.2) × 0.2
grid_lon = round(lon / 0.2) × 0.2
cache_key = "{grid_lat}_{grid_lon}"

Enter fullscreen mode

Exit fullscreen mode

Example:

User location: (48.8712, 2.3891)

grid_lat = round(48.8712 / 0.2) × 0.2 = round(244.356) × 0.2 = 244 × 0.2 = 48.8
grid_lon = round(2.3891 / 0.2) × 0.2 = round(11.9455) × 0.2 = 12 × 0.2 = 2.4

cache_key = "48.8_2.4"

Enter fullscreen mode

Exit fullscreen mode

### A Few Words About the Tech Stack

Even though I'm most proficient in .NET, I wanted to make this challenge more interesting by building it on something different, for a few reasons:

1. I wanted to learn a technology I had less experience with.
2. I'd get to interact more with Copilot CLI and explore its capabilities.
3. I needed a stack that's popular and widely used, making it easier for others to contribute in the future.

That's how I landed on Node.js. It's completely different from .NET, but that's exactly the point! I wanted to step outside my comfort zone, explore a relatively unexplored area, and see how it felt. Spoiler: it felt just right!

For the front-end, I kept things simple with plain HTML, CSS, and JavaScript. In the future, I plan to upgrade it with something more advanced, but for this challenge, simplicity was key.

## My Experience with GitHub Copilot CLI

I'm a huge fan of the CLI tools in general. To me, it's the single most efficient and authentic tool a software engineer can use. After all, every GUI tool is built on top of it. I often find myself struggling to understand GUI tools, which might make me look a bit weird to developers who can't live without their shiny interfaces, but I guess I'll never be able to understand that point of view.

As amazing as Copilot is, it always lacked one feature I had been waiting for - the CLI tool. Now that it's finally here, there's no way I'm not going to use it.

This was actually my first time using Copilot in CLI mode, and I was instantly amazed at how good of a communicator it is. The variety of model options is fantastic too, and I really appreciate the token system, each model consumes a specific number of tokens, allowing you to choose based on the complexity of your task.

Copilot CLI didn't just help me create beautiful visuals and make the front-end fully responsive, it also helped me refine all the ideas I had sketched out before even starting to code. It improved my calculations to handle edge cases I hadn't considered, like normalizing longitude values.

Here's how the conversation went like:

Me: Can you explain the purpose of this normalization function?Copilot CLI:This function ensures longitude values stay within the valid range of-180° to +180°.Why it's needed:- Longitude wraps around the Earth (180° and -180°are the same line - the International Date Line)- If a user pans the map far right, Leaflet might report longitude as370°instead of10°- API calls and distance calculations need standard-180 to 180rangeHow it works:1.lon % 360- Wraps values into-360 to 360range2.If > 180→ subtract 360 (e.g.,270° → -90°)3.If < -180→ add 360 (e.g.,-270° → 90°)

Example: User pans to longitude540° → 540 % 360 = 180→ returns180°✓

This is one of the highlights and a perfect example of how Copilot CLI can save you from overlooking subtle details. It really feels like having a fellow engineer by your side, pointing out mistakes, suggesting better alternatives, and even helping you implement them.

Additionally, it was incredibly easy and convenient to create issues on my GitHub project board directly from the CLI. Based on the strategy and implementation details I provided, Copilot generated a neatly organized list of tasks for me. I didn't have to create them manually, which is a process that can be repetitive and time-consuming.

### So, Here's the Conclusion

Would I be able to create this project only by myself? - Yes, absolutely.Would I be able to create the same exact project only by myselfin less than 2 weeks? - Probably not - the Copilot CLI really boosted my performance.

I didn't encounter any issues or bugs while using Copilot CLI, which is impressive for a brand-new tool, especially since you'd normally expect at least some minor hiccups.

Overall, I'm absolutely satisfied with Copilot CLI and I think it'll always have room in my toolbox from now on.

### And One Last Thing

This app has great potential. I've already planned many features that will be added in the future, and I'd love to see contributions from other software engineers as well.

Check out the high-level roadmap in the screenshot on the website:

Building this app wasn't just a coding challenge, it was a way to bring a piece of my passion for aviation into reality. Every line of code, every architecture decision, and every optimization I made was about connecting people to the thrill of watching planes even if they're stuck at a desk or on the go.

It's amazing how technology can bridge the gap between curiosity and reality. With just a few carefully crafted algorithms, users can feel the sky above them, catch glimpses of planes flying overhead, and experience the small joys I've loved for years.

This project reminded me that the best ideas aren't just about what you create, they're about the feeling they leave behind. For me, it's that little spark of excitement when a plane passes by, and now, thanks to this app, I can share that spark with anyone, anywhere. Working on this app reminded me that nothing makes me feel more alive than building and creating things that I'm passionate about.

## Credits

Special thanks to the following projects and services that made this application possible:

OpenSky Network API- An incredible public service providing real-time aviation data that powers this application ✈️

Leaflet- For delivering lightweight and powerful interactive maps

OpenStreetMap- For providing the open-source map data and tiles

## Useful Links

GitHub Repository

Demo

Video Explanation

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (12 comments)


For further actions, you may consider blocking this person and/orreporting abuse
