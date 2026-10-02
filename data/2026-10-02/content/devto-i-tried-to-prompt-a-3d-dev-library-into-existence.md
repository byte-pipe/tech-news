---
title: I Tried to Prompt a 3D DEV Library Into Existence. Then I Had to Build My Own Level Editor. - DEV Community
url: https://dev.to/mikachu/i-tried-to-prompt-a-3d-dev-library-into-existence-then-i-had-to-build-my-own-level-editor-37gf
site_name: devto
content_file: devto-i-tried-to-prompt-a-3d-dev-library-into-existence
fetched_at: '2026-10-02T22:50:50.558926'
original_url: https://dev.to/mikachu/i-tried-to-prompt-a-3d-dev-library-into-existence-then-i-had-to-build-my-own-level-editor-37gf
author: Mika Flowers
date: '2026-09-27'
description: 'This is a submission for the Sanity Challenge, Path Two: Vibe-Code Something Strange. I started... Tagged with devchallenge, sanitychallenge, ai, sanity.'
tags: '#devchallenge, #sanitychallenge, #ai, #sanity'
---

Sanity Challenge Path Two Submission

This is a submission for theSanity Challenge, Path Two: Vibe-Code Something Strange.

I started this hackathon building a dream journal.

A few days later, I was walking through a giant library filled with real DEV articles, debugging floating bookshelves, building spatial authoring tools, and learning how to teach Sanity to remember which shelves were alive.

That escalation probably tells you most of what you need to know about how this project went.

The result isOniria: The Living DEV Library.

Instead of browsing DEV as a feed, grid, or search page, Oniria turns it into a place.

* You walk through rooms.
* Articles become books.
* Topics occupy shelves.
* Search physically restocks part of the library.
* Parts of the archive can evolve over time based on activity.
* Sanity remembers what previously occupied that physical space.

The question behind the project eventually became:

## What if information had geography?

## 🔗 Project Links

Repository:github.com/miflow13/OniriaAgent sessions:Public Oniria development transcriptsSanity project:Oniria Archive Control

Live project:TBADemo video:TBA

# What I Built

Oniria is a walkable 3D library built from live DEV content.

The current library is organized into six rooms:

Room

Purpose

Featured

Popular and curated writing

New Arrivals

Recently published DEV articles

Topics

Tag-driven collections

Creators

Authors and their writing

Search

A physical card catalogue

Archive

Deeper exploration and long-tail content

DEV provides the live content.

Sanity provides the memory and structure of the world.

Three.js turns both into a place you can walk through.

### The data flow

I didn't want to copy DEV articles into a CMS and call that an integration.

Instead, DEV remains the source of the content itself.

DEV API
 │
 │ articles / creators / tags / search
 ▼
Oniria
 │
 ├──────────────► Three.js
 │ architecture
 │ books
 │ navigation
 │ interactions
 │
 ▼
Sanity
world configuration
room definitions
layout markers
curator picks
guided journeys
living shelf state
history / lifecycle

Enter fullscreen mode

Exit fullscreen mode

DEV tells Oniria what currently exists.

Sanity tells Oniria what the world means, where things belong, and what happened there before.

That distinction became the foundation of the whole project.

# 🎮 Demo

A first visit is intentionally simple:

1. Enter the libraryand explore Featured or New Arrivals.
2. Approach a shelfand target a book.
3. Open the real DEV articlerepresented by that book.
4. Return to the libraryand land back at the same physical location.
5. Visit Search, query DEV, and watch that room restock around the query.
6. Explore Topics, Creators, and the deeper Archive.

The goal was to make the underlying technology complicated while keeping the mental model simple.

The visitor shouldn't need to understand data graphs, procedural systems, lifecycle state, or spatial indexes.

They should just understand:

## This is a library.

## 📸 Inside Oniria

### The Main Hall

### Browsing the Shelves

### Reading a Real DEV Article

### Sanity as the World Backend

### Using the In-World Authoring Tool

# 💻 Code

Repository:github.com/miflow13/Oniria

The main stack is:

* Next.js 16
* React 19
* TypeScript
* Three.js
* Sanity
* next-sanity
* DEV / Forem API
* Vercel
* GLB environment and architectural assets

The building itself is assembled through code, configuration, reusable assets, and structured world data rather than a traditional 3D level editor.

That last part became one of the most important parts of the project.

# 🛠️ Building Oniria

This is the part of Oniria I'm most interested in.

The project didnotcome from one perfect prompt.

It changed direction repeatedly because actually walking through what the agents produced exposed problems that were impossible to understand from code alone.

## 1. It Started as a Dream Journal

The original Oniria was much smaller.

I built a Sanity-backed dream journal where dreams referenced recurring symbols, mood, and other structured information.

Those relationships became a visual map.

Then the map became 3D.

Then I wanted to move through it.

Dreams became environments.

I added first-person movement.

Then portals between related memories.

At some point I had to ask myself:

Have I accidentally started building a video game?

Probably.

But something useful had emerged underneath all of that experimentation.

The idea was no longer specifically about dreams.

I was interested in whether structured information could have:

* space
* distance
* landmarks
* relationships
* physical context
* geography

I briefly experimented with using that same structure to explore files and codebases.

Then I looked at DEV.

Articles already have natural relationships:

* tags
* authors
* recency
* popularity
* search
* recommendations

And suddenly the metaphor was obvious.

A library.

## 2. From a Graph to a Building

The first DEV version was much more abstract.

Articles and profiles existed as objects in an explorable spatial web.

Technically, it worked.

Experientially, it didn't.

Everything competed for attention.

There wasn't enough hierarchy.

So I simplified it into six obvious destinations:

Featured
New Arrivals
Topics
Creators
Search
Archive

Enter fullscreen mode

Exit fullscreen mode

That was the first major course correction.

Instead of explaining a graph, I could put a door in front of someone.

Instead of explaining an article node, I could put a book on a shelf.

The complexity stayed underneath.

The visitor saw a library.

## 3. The AI Was Useful — and Confidently Wrong

I used Codex heavily during development, with ChatGPT helping me think through architecture, UX, debugging, and the direction of the project.

The agents were incredibly useful.

They were also very capable of producing something technically valid that was visually wrong.

One of the clearest examples involved the library walls.

I provided actual wall assets and asked the agent to construct the environment with them.

The result looked wrong.

It had generated procedural wall geometry instead.

There were technically walls.

They were just not the walls I gave it.

Eventually my prompt became:

## “DO NOT GENERATE YOUR OWN ASSET FOR THE WALL.”

Use the assets provided to you.

The next implementation removed the generated visible walls and made the authored GLB assets the source of truth.

Primitive geometry remained useful for things like invisible collision and structural helpers.

That experience taught me something important:

A model can satisfy the semantic meaning of a request while completely missing the visual intention.

## 4. A Convincing Wrong Diagnosis

Another example was lighting.

At one point, the library became almost completely washed out.

The first explanation focused on overlapping lights and bright materials.

That was plausible.

Some of it was even correct.

But it didn't fully explain what I was seeing.

Continued testing eventually exposed the bigger issue:

UnrealBloomPass.

The bloom threshold was allowing too much of the scene to contribute, making the entire environment glow.

That debugging process was valuable because the first answer sounded reasonable.

The important thing was continuing to test the actual experience instead of accepting the first explanation simply because it sounded technical.

## 5. The Problem a Better Prompt Couldn't Solve

The biggest limitation appeared when I started placing shelves and architecture precisely.

I wasn't using a traditional 3D editor.

The environment was being built through:

* Three.js code
* coordinates
* configuration
* screenshots
* prompts

That worked surprisingly well until the task became:

Put this shelf against that wall, slightly left of the pavilion, rotated toward the center of the room.

I could see exactly where I wanted it.

The coding model could see coordinates and occasional screenshots.

Those are not equivalent.

We spent multiple iterations nudging architecture through prompts.

Eventually I realized:

## The solution wasn't a better prompt.

## It was a better tool.

## 6. So I Built a Level Editor Inside Oniria

Oniria gained a development-only spatial authoring workflow.

While walking through the running Three.js environment, I can place markers exactly where objects or zones should exist.

A marker looks like this:

{

 
"label"
:
 
"R1-P04"
,

 
"roomSlot"
:
 
1
,

 
"districtId"
:
 
"latest"
,

 
"x"
:
 
13.687
,

 
"y"
:
 
0
,

 
"z"
:
 
11.998
,

 
"yaw"
:
 
0
,

 
"width"
:
 
4.5
,

 
"depth"
:
 
0.72

}

Enter fullscreen mode

Exit fullscreen mode

Those markers are stored in Sanity aslibraryLayoutMarkerdocuments.

The workflow became:

walk through world
 ↓
stand where something belongs
 ↓
place marker
 ↓
Sanity persists spatial data
 ↓
renderer consumes authored layout

Enter fullscreen mode

Exit fullscreen mode

That was the moment Sanity stopped feeling like just a CMS in this project.

It became part of my3D authoring environment.

A structured document didn't have to represent a blog post.

It could represent a physical location.

## 7. Sanity Became the Memory of the World

The current Studio is organized asOniria Archive Control.

Sanity manages several layers of the environment.

### Library Control

Global configuration such as:

* welcome copy
* movement defaults
* atmosphere
* haze
* live DEV updates
* archive behavior

### Library Districts

Each room has structured configuration including:

* title
* room code
* ordering
* DEV tags
* accent
* atmosphere
* audio profile
* landmark
* content source
* enabled state

### Layout Pins

These store authored spatial positions created from the development tool.

### Curator Picks

Specific DEV articles can be intentionally featured without duplicating ownership of the original content.

### Guided Journeys

Ordered destinations can define intentional paths through the archive.

And then there are the part of the data model that became my favorite:

Living Shelf Slots.

# 🌱 The Living Library

A physical location can exist independently from whatever currently occupies it.

That became the foundation of the Living Shelf system.

A shelf slot has a stable identity.

Sanity stores information including:

slotKey
district
physical slot
occupant
topic
lifecycle
vitality
signal score
article count
timestamps
history

Enter fullscreen mode

Exit fullscreen mode

Its lifecycle can move through:

DORMANT
 ↓
FORMING
 ↓
ACTIVE
 ↓
COOLING
 ↓
DORMANT

Enter fullscreen mode

Exit fullscreen mode

A scheduled process samples recent DEV activity and evaluates topic signals.

If a topic begins gaining momentum, a dormant location can materialize around it.

It becomes active.

Later, if activity fades, it can cool down and eventually return to latent space.

But Sanity still remembers what happened there.

The position persists.

The occupant changes.

The history remains.

That's whereLiving DEV Librarystopped being just a name.

## Search Became Physical Too

Search originally behaved like normal application UI.

Type something.

Get a result list.

But that pulled the user out of the spatial metaphor.

So the Search room became a physical catalogue.

Searching DEV can restock shelves in the environment with matching content.

The architecture remains familiar while the information changes.

Again, the idea became:

Place and content do not have to be the same thing.

## Performance Changed the Architecture

Making the library feel enormous caused predictable performance problems.

Some early versions attempted very large shelf fields with hundreds of individual books and remote cover textures.

That created:

* cover-image flicker
* unnecessary texture work
* excessive geometry
* worse GPU performance
* visual clutter
* harder navigation

Instead of treating performance only as an optimization problem, I started treating it as a design constraint.

Nearby books get more detail:

* covers
* readable metadata
* individual interaction
* pull-forward behavior

Mid-distance shelves simplify.

Far-away structures can become architectural mass rather than hundreds of fully interactive objects.

The rule became:

## Full fidelity only where interaction matters.

That made the experience faster and clearer at the same time.

# 🤖 What I Learned About Vibe Coding

One of the most interesting parts of this project was learning when to follow an agent's implementation and when to challenge it.

Sometimes the agent correctly ignored my implementation request.

During work on the Living Shelves system, I requested a larger architectural refactor.

Codex audited the existing implementation first.

It discovered that the architecture I wanted was already reusable.

The real problem was a prototype capacity restriction that prevented the system from expanding correctly.

Instead of blindly performing the requested refactor, it fixed the actual bottleneck.

That was one of my favorite agent interactions from the project because it represented the kind of AI-assisted engineering I want.

Not:

“The user asked for a refactor, so refactor.”

But:

“What problem are we actually trying to solve?”

## A Lot of Oniria Was Thrown Away

There are many abandoned versions of this project.

At various points it contained:

* a dream journal
* a relationship constellation
* Dream Dive environments
* portals
* an Observatory
* an experimental project/codebase explorer
* a floating DEV WebSurf graph
* giant cyber-library structures
* enormous procedural shelf fields
* multi-level archives
* an outdoor library
* multiple architecture styles
* fake infinite corridors
* several ambience systems

Some were bad.

Some were cool but wrong for the final product.

Most taught me something that survived.

The commit history is basically an archaeological site.

I decided not to hide that because Path Two is specifically about the build process.

The interesting thing about vibe coding wasn't that AI magically created the right application.

It was how cheaply I could explore an idea, discover that it was wrong, and throw it away.

## Where AI Helped — and Where It Didn't

AI was particularly good at:

* rapidly implementing architectural ideas
* repetitive Three.js construction
* refactoring
* tracing state through large systems
* generating implementation alternatives
* debugging TypeScript and integration problems
* making experiments cheap enough to discard

It was weaker at:

* understanding exact spatial intent
* judging visual scale from screenshots
* knowing whether a world actuallyfelt good
* resisting technically-correct-but-visually-wrong solutions
* recognizing when the requested implementation wasn't the real problem

My workflow increasingly became:

observe
 ↓
decide what feels wrong
 ↓
describe the underlying problem
 ↓
agent implements
 ↓
run it
 ↓
walk through it
 ↓
correct assumptions
 ↓
repeat

Enter fullscreen mode

Exit fullscreen mode

The fastest workflow wasn't maximizing agent autonomy.

It was creating a tighter feedback loop betweenhuman perception and machine implementation.

The spatial authoring system exists because of that realization.

# 🤖 Public Agent Sessions

Because this is theVibe-Code Something Strangetrack, I wanted the development process itself to be inspectable.

👉Browse the sanitized Oniria agent sessions

I exported and curated the Codex rollout sessions used while building Oniria.

The Codex task pages themselves are private, so the public versions preserve the development trail without exposing private/internal material.

They keep the parts that matter:

* prompts
* implementation updates
* mistakes
* course corrections
* verification
* commits
* failed assumptions

### Session Highlights

#### Core Library Loop Alpha

Implemented physical article targeting, Search →Take Me There, reader state, exact return-to-shelf state, and interaction analytics.

The live loop was verified with a real DEV search result before the final polish pass.

Repository milestone:c6a09c0

#### Living Shelf Capacity

Codex audited the existing shared shelf pipeline and found that the architecture was already reusable.

The real problem was a prototype capacity limit.

That restriction was removed so qualified topics can fill authored Sanity slots without creating a parallel renderer or fake content.

Repository milestone:40552c6

#### Authored Architecture and Visual Debugging

Corrected the workflow so supplied wall assets became the source of truth, then later traced the library's whiteout regression toUnrealBloomPassand disabled it only for the DEV Library.

Repository milestone:5cc55e1

#### Spatial Shelf Authoring and Library Scale

Built physical double-sided stacks, bounded cover atlases, dense instanced book massing, and level-of-detail behavior for the larger library.

* Shelf geometry —45537db
* Cover atlases —c74f07e
* Shelf LOD —fcfeba5

#### Wayfinding and Floor Identity

Added root-aware breadcrumbs, threshold-onlyAHEADcues, environmental floor differentiation, and matte-to-satin floor material treatment.

* Breadcrumbs —9473c3f
* Wayfinding cue —5c4c367
* Floor identity —1f56966
* Floor material —f6ed0b6

The public session export removes:

* private/internal reasoning
* system/developer instructions
* security/guardian telemetry
* repetitive shell output
* unrelated project sessions

The repository milestones are the public companion to those sanitized transcripts.

Some of my favorite parts of the sessions aren't where Codex got everything right immediately.

They're the moments where the workflow became genuinely collaborative because I had to challenge what it produced.

Including, of course:

## “DO NOT GENERATE YOUR OWN ASSET FOR THE WALL.”

That is probably a more accurate description of vibe coding than anything else I could write.

# ⚙️ Sanity Project Details

Technical project details, schemas, API, and commands

### Sanity

Sanity project:Oniria Archive ControlSanity Project ID:z5fp07epDataset:productionSanity Studio:/studioon the deployed application, orhttp://localhost:3000/studiowhen running locallySanity project console:Manage projectz5fp07epPublic dataset API:https://z5fp07ep.apicdn.sanity.io/v2026-09-27/data/query/production

The public API URL above is the Content Lake endpoint for theproductiondataset. It requires a GROQ query parameter to return documents; the project ID and dataset are included in the URL so the Sanity integration can be identified directly.

Project repository:github.com/miflow13/OniriaStable project reference:Oniria — The Living DEV LibraryAuthor:Mika Flowers (GitHub)

### Project Architecture

Oniria is a Next.js 16 / React 19 / TypeScript application that uses Three.js to render a walkable six-room library built from live DEV / Forem content.

Vercel hosts the application and runs the living-library evolution route every 30 minutes.

The six Sanity-backed rooms are:

* R-01— Featured
* R-02— New Arrivals
* R-03— Topics
* R-04— Creators
* R-05— Search
* R-06— Archive

Sanity is used as the persistent world-configuration and authoring layer.

The embedded Studio is titledOniria Archive Controland is mounted at/studio.

The application uses Sanity for:

* authored room definitions
* in-world layout pins
* curator picks
* guided journeys
* living shelf state
* lifecycle history
* global library configuration

DEV remains the source of live:

* articles
* authors
* tags
* popularity
* recency
* search data

### Project Commands

npm run dev
npm run typecheck
npm run build
npm run start
npm run sanity
npm run seed:library

Enter fullscreen mode

Exit fullscreen mode

Theseed:librarycommand creates or updates the main library configuration, the six room documents, and the default guided journey.

The scheduled/api/library-evolutionroute samples recent DEV activity, evaluates topic signals and physical shelf slots, updates lifecycle state, and persists the shared result to Sanity.

### Primary Sanity Schemas

* libraryConfig
* libraryDistrict
* libraryLayoutMarker
* librarySlotState
* curatedArticle
* archiveJourney

The repository also still contains the original:

* dream
* symbol

schemas from the project's first iteration.

I kept those as part of Oniria's development history rather than deleting where the project started.

# Final Thoughts

Oniria started as a project about dreams.

It ended up becoming a project about information.

Feeds are useful because they remove geography.

Everything is immediately reachable.

But removing geography also removes:

* distance
* landmarks
* wandering
* memory of place
* discovery
* physical context

Oniria is an experiment in putting some of those things back.

I don't think every website should become a 3D environment.

## Please do not make me walk across a room to change my password.

But I do think there are kinds of information whereexploration itself can be meaningful.

And if nothing else, this project taught me that when an AI repeatedly puts the bookshelf in the wrong place, the right answer might be to stop arguing with it...

and build yourself a level editor.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments have been hidden by the post's author -find out more

For further actions, you may consider blocking this person and/orreporting abuse