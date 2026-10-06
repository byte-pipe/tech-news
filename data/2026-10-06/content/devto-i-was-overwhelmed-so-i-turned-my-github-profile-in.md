---
title: I Was Overwhelmed, So I Turned My GitHub Profile Into a Roguelike Dungeon - DEV Community
url: https://dev.to/g00ds0ul/i-was-overwhelmed-so-i-turned-my-github-profile-into-a-roguelike-dungeon-17a8
site_name: devto
content_file: devto-i-was-overwhelmed-so-i-turned-my-github-profile-in
fetched_at: '2026-10-06T22:54:12.336014'
original_url: https://dev.to/g00ds0ul/i-was-overwhelmed-so-i-turned-my-github-profile-into-a-roguelike-dungeon-17a8
author: Iseoluwa Olowogoke
date: '2026-10-03'
description: It was a late afternoon. I came in tired and a bit down, with a long list of tasks and a pile of... Tagged with csharp, gamedev, github, showdev.
tags: '#showdev, #csharp, #gamedev, #github'
---

Includes a complete C# build log and live link

It was a late afternoon. I came in tired and a bit down, with a long list of tasks and a pile of issues waiting for me. I didn't know where to start, so I did what a lot of us do when we're stuck: I opened DEV and started scrolling.

Then I found this post byGeorge Kobaidze:

Bypassing GitHub's strict sandbox via SVGs

 Giorgi Kobaidze
 

 Giorgi Kobaidze
 

Giorgi Kobaidze

 Follow
 

Oct 1

## I Turned My GitHub Profile Into a Cyberpunk Console With a City Built From My Contributions

#
showdev

#
python

#
github

#
design

237
 reactions

Picked as gem

Picked as gem by you

Comments

 136
 comments

 15 min read
 

He turned his GitHub profile into a cyberpunk console, with a city built from his contributions. I was hooked straight away. I didn't just want to look at it. I wanted tobuild one of my own.

I'm a C#/.NET game developer, so a city didn't feel likeme. Adungeondid. That rush of excitement did something my to-do list couldn't: it got me moving. I picked up my tools and started building, and the momentum carried over into the tasks I'd been putting off.

This post is my build log: what I made, how it works and what I learned along the way.

🙏 Credit where it's due:the core idea (a README made of stacked SVG "slices" that look like one console, redrawn daily by a GitHub Action) comes from George's post. Go read it. Everything below is my own take: a roguelike theme, a C#/.NET generator and the features I wanted for my profile.

## 🗺️ What I built

👉Live:github.com/G00dS0ul

My profile is now one retro terminal, split into numbered sections. Here's the tour.

### 01 · Boot screen

The console "boots up" with a typing animation:> ./G00dS0ul.exe --boot, loading the engine core, mounting the renderer and spawning the player.

### 02 · The dungeon

My last 365 days of contributions as dungeon tiles: stone walls, glowing floors, treasure chests, torches and a tiny hero walking my current streak. A night sky sits on top, with stars, a moon, a castle and the dungeon entrance.

### Explore mode 🔍

Images on GitHub can't react to your mouse, so clicking the dungeon (or the glowingCLICK TO EXPLOREbutton) opens an interactive version on GitHub Pages. Hover over any tile to see that day's contributions.

### 03 · Inventory

A "backpack" of the languages I use (weighted by my commits this year) and a character stats panel: stars, repos, PRs, issues, guilds and followers.

### 04 · Quest log

My pinned repos as quest cards, each with a status:ACTIVE,IN PROGRESSorON HOLD. For open source projects I contribute to, the card gets a goldCONTRIBUTORbadge, my role and how many of my PRs were merged. Every card links to its repo.

### 05 · Character sheet

Who I am, in RPG form: a character sheet, "active effects" (what I'm learning and looking for) and my equipped gear and skills.

### 06 · Party

Key-cap style buttons to reach me: Email, LinkedIn, X and the dungeon page.

## 🧠 The approach

### 1. A README can't run code, but an SVG can animate

GitHub strips JavaScript and most CSS from READMEs. But an SVG loaded through an<img>tag can still useCSS animations inside the SVG itself. So every blinking cursor, pulsing button, flickering rail and walking hero is plain SVG + CSS keyframes.

### 2. One console, many images

The trick from George's post that I built on: the "console" is reallya stack of separate imagesthat line up perfectly.

<p
 
align=
"center"
>

 
<img
 
src=
"./assets/header.svg"
 
width=
"100%"
 
align=
"top"
>

 
<a
 
href=
"https://g00ds0ul.github.io/G00dS0ul/"
>

 
<img
 
src=
"./assets/dungeon.svg"
 
width=
"100%"
 
align=
"top"
>

 
</a>

 
<img
 
src=
"./assets/inventory.svg"
 
width=
"100%"
 
align=
"top"
>

 
<!-- quest cards: 2 per row, 50% width each -->

 
<!-- connect buttons: 4 per row, 25% width each -->

 
<img
 
src=
"./assets/footer.svg"
 
width=
"100%"
 
align=
"top"
>

</p>

Enter fullscreen mode

Exit fullscreen mode

For the slices to read as one window, I set a few rules:

* Everything is 960px wide, and every slice height is amultiple of 40, so the background grid continues across slice edges.
* Every slice draws the same side railsat the same x position. Half-width quest cards only draw the rail on their outer side, so two cards side by side still look like one frame.
* Quest cards and buttons are separate imagesbecause a README image can only linkas a whole. Six clickable quest cards means six images.

### 3. A C# generator instead of a script

I wanted to write this in my own language, so the generator is a small.NET 10 console appintools/DungeonGen:

Program.cs -> entry point & args
GitHub.cs -> GraphQL + contribution calendar
DungeonRenderer.cs -> the dungeon map
NightSky.cs -> stars, moon, castle, airship
InventoryRenderer.cs -> languages + stats
QuestRenderer.cs -> pinned repo cards
AboutRenderer.cs -> character sheet (from about.json)
ConnectRenderer.cs -> link buttons
ReadmeUpdater.cs -> rewrites the README blocks + cache-busting

Enter fullscreen mode

Exit fullscreen mode

Each renderer is just C# string building that produces SVG. No libraries, no magic.

### 4. Turning contributions into a dungeon

Each day becomes a 14px tile:

* 0 contributions:a stone wall
* More contributions:brighter floor tiles
* My busiest days:treasure chests 💰
* My best day:a glowing gold frame
* The hero:walks along my current streak, ending on today

On top, I added a night sky strip (stars, a crescent moon, a shooting star, a castle and the dungeon entrance) so it feels like a real place.

### 5. Making it update itself

A GitHub Action runs the generator every day and commits only if something changed:

on
:

 
schedule
:

 
-
 
cron
:
 
"
17
 
6
 
*
 
*
 
*"
 
# daily

 
workflow_dispatch
:
 
# manual "Run workflow" button

 
push
:

 
paths
:
 
[
"
tools/DungeonGen/**"
]

# ...

-
 
run
:
 
>

 
dotnet run --project tools/DungeonGen -c Release --

 
${{ github.repository_owner }}

 
--assets assets --html docs/index.html --readme README.md

 
env
:

 
PROFILE_TOKEN
:
 
${{ secrets.PROFILE_TOKEN || github.token }}

Enter fullscreen mode

Exit fullscreen mode

## 📜 Progress log

Step 1: Boot screen.I started small: a header with a typing animation, built by animating aclipPathwidth one character at a time. Seeing it type my name was the moment I knew I'd finish this.

Step 2: The dungeon.I mapped the contribution calendar to tiles, then added torches, chests, the hero and the stat boxes (XP, STREAK, BEST DAY, TODAY).

Step 3: Hover doesn't work in a README, so I added a page.I generate a second, interactive version intodocs/index.htmland serve it with GitHub Pages. The dungeon image links to it.

Step 4: Inventory & quests.Languages, stats and pinned repos as quest cards.

Step 5: Character sheet & party buttons.All the text lives in anabout.jsonfile, so I can update my bio or links without touching any code.

Step 6: Night sky & final polish.I added the sky, then went back and gave every section a numbered divider and room to breathe. At first, everything was stacked so tightly it felt cramped.

## 🐛 Bugs that taught me things

My numbers didn't match my profile.The GraphQL API only counts private contributions if your token can see them. GitHub's own profile graph already includes them (when "private contributions" is turned on). So the generator now reads the same calendar the profile page shows, with the API as a fallback.

My languages were wrong.Ranking languages bybytes of codemade a single big repo dominate everything. I switched tolanguages weighted by my commits this year(fromcommitContributionsByRepository), which reflects what I actually work in.

My open source work was invisible.I'm a core contributor toGS-SystemAnalyzer/coreand I work on the C# loader inmetacall/core, but those repos aren't mine. So for pinned repos I don't own, the generator runs one aliased GraphQLsearchto countmy PRs and how many got merged, and shows them on the card with a CONTRIBUTOR badge.

One org blocked my token, and the whole run crashed.GraphQL can returnpartialdata with anerrorsarray. Now the generator logs those as warnings and keeps going with what it got.

My side rails disappeared.I drew them as<line>elements with a glow filter. A perfectly vertical line has azero-width bounding box, so the filter region was empty and the line vanished. Drawing them as 3px<rect>elements fixed it.

"It's not updating!"It was, but GitHub caches README images aggressively. The generator now adds a hash of each SVG to its URL (dungeon.svg?v=1a2b3c4d), so a changed image gets a new URL. (And Ctrl+Shift+R is your friend.)

## 💡 What I took away

I started that afternoon overwhelmed and unmotivated. I ended it with a working project and, more importantly,momentum. Once I'd shipped the first slice, the tasks I'd been dreading didn't feel so heavy anymore.

Sometimes the best way to get unstuck is to build something just because it excites you.

Thanks again toGeorge Kobaidzefor the spark. If his post inspired me, maybe mine will inspire you. If you build your own, drop a link in the comments. I'd love to see it! 🗡️

Source:github.com/G00dS0ul/G00dS0ul(the generator is intools/DungeonGen)

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (12 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse