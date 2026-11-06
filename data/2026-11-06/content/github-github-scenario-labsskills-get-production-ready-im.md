---
title: 'GitHub - scenario-labs/skills: Get production-ready images, video, audio, and 3D from any AI agent: skills that pick the right model, price before spending, and keep characters and brands consistent through the Scenario MCP, plus expert teams that drive Blender, Maya, ZBrush, Unreal, and Unity. · GitHub'
url: https://github.com/scenario-labs/skills
site_name: github
content_file: github-github-scenario-labsskills-get-production-ready-im
fetched_at: '2026-11-06T12:28:16.469076'
original_url: https://github.com/scenario-labs/skills
author: scenario-labs
description: 'Get production-ready images, video, audio, and 3D from any AI agent: skills that pick the right model, price before spending, and keep characters and brands consistent through the Scenario MCP, plus expert teams that drive Blender, Maya, ZBrush, Unreal, and Unity. - scenario-labs/skills'
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

304 Commits
304 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents/
skills
.agents/
skills
 
 
.claude-plugin
.claude-plugin
 
 
.claude
.claude
 
 
.codex
.codex
 
 
.cursor
.cursor
 
 
.github
.github
 
 
.husky
.husky
 
 
.vscode
.vscode
 
 
docs
docs
 
 
resources
resources
 
 
scripts
scripts
 
 
skills
skills
 
 
tests
tests
 
 
.coveragerc
.coveragerc
 
 
.editorconfig
.editorconfig
 
 
.git-blame-ignore-revs
.git-blame-ignore-revs
 
 
.gitignore
.gitignore
 
 
.nvmrc
.nvmrc
 
 
.prettierignore
.prettierignore
 
 
.prettierrc.json
.prettierrc.json
 
 
.release-please-manifest.json
.release-please-manifest.json
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
INSTALL.md
INSTALL.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
REVIEW.md
REVIEW.md
 
 
SECURITY.md
SECURITY.md
 
 
SUPPORT.md
SUPPORT.md
 
 
commitlint.config.js
commitlint.config.js
 
 
cspell.json
cspell.json
 
 
lychee.toml
lychee.toml
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
project-words.txt
project-words.txt
 
 
release-please-config.json
release-please-config.json
 
 
ruff.toml
ruff.toml
 
 
skills-lock.json
skills-lock.json
 
 
skills.sh.json
skills.sh.json
 
 
version.txt
version.txt
 
 
View all files

## Repository files navigation

# Scenario Agent Skills

Agent Skills that teach AI coding agents (Claude Code, Cursor, Codex, Copilot, and 70+ others) how
to create production-ready content withScenariothrough theScenario MCP server: images, video, audio, textures, skyboxes, 3D
assets, and custom-trained models, for games, entertainment, and any creative vertical.

The expert tools at the bottom of the list work differently: teams of skills that drive DCC (digital
content creation) software and game engines installed on your machine (ZBrush, Blender, Maya, Unreal
Engine, Unity, Godot, Roblox Studio), distilled from expert tutorials, conference talks, and
official documentation. They need the application, not the Scenario MCP server, and each family
folder's README records how it was built and how far it was verified.

Skills follow theAgent Skillsformat.

## Install

Everything for Scenario.Every Scenario skill, without the expert tools: the default for working
through the Scenario MCP.

#
 Every Scenario skill, without the expert tools

npx skills add scenario-labs/skills --skill scenario scenario-inspiration scenario-image scenario-multi-reference scenario-product-shots scenario-brand-kit scenario-image-editing scenario-text-overlay scenario-storyboards scenario-game-assets scenario-sprite-animation scenario-side-view-game-kit scenario-blender-2d-animation scenario-textures scenario-skyboxes scenario-3d scenario-video-to-motion scenario-blender scenario-patina-retexture scenario-orbit-views scenario-walkable-room scenario-video scenario-video-editing scenario-video-color-grade scenario-seedance-music-video scenario-kinetic-music-video scenario-chatgpt-pet-create scenario-chatgpt-pet-update scenario-seedance-storyboard scenario-seedance-drafts scenario-video-ads scenario-ugc scenario-fan-cam scenario-reel-recast scenario-audio scenario-video-assembly scenario-motion-loops scenario-caption-studio scenario-consistency scenario-identity-library scenario-model-training scenario-asset-analysis scenario-quality-gate scenario-refine-loop scenario-model-comparison scenario-formats scenario-workflows scenario-workflow-authoring scenario-moderation scenario-report scenario-team-admin scenario-admin-analytics scenario-gpt-image scenario-mai-image scenario-seedream scenario-gemini-image scenario-reve scenario-ideogram scenario-grok-imagine-image scenario-luma-image scenario-minimax-video scenario-gemini-omni scenario-grok-imagine-video scenario-veo scenario-seedance scenario-kling scenario-vidu scenario-wan scenario-runway scenario-luma-video scenario-minimax-music scenario-elevenlabs scenario-ace-step scenario-sonilo scenario-meshy scenario-rodin scenario-sparc3d scenario-3d-worlds scenario-ad-variants scenario-thumbnails

By role or goal.INSTALL.mdgroups the skills by job, from 2D artist to producer,
and by outcome, from game art to ChatGPT pets, with one command each.

Expert tools.A family installs as one set, since its specialists import the lead skill's
scripts: select its "Expert tools" group in the installer menu, or run the command in its family
README (ZBrush,Blender,Maya,Unreal Engine,Unity,Godot,Roblox Studio).

Pick, or install one skill.

#
 Pick from the installer menu, grouped by topic (it opens with nothing preselected: select before pressing enter)

npx skills add scenario-labs/skills

#
 A single skill

npx skills add scenario-labs/skills --skill scenario

Pin a reviewed release.The commands above fetch the latest copy of each skill frommain. To
install a reviewed state instead, pin both the installer and the commit, taken from a release's tag.
Run it again with a newer commit to move.

npx skills@1.7.4 add scenario-labs/skills#
<
commit
>
 --skill 
<
name
>

The menu's topic groups cannot be selected from the command line: the CLI matches--skillagainst
exact skill names only, and a group flag is an open request upstream
(vercel-labs/skills#992). From a script or CI,
run the default command above or a role command from INSTALL.md with-y, which skips every prompt.

The Scenario skills need the Scenario MCP server connected:

claude mcp add --transport http scenario https://mcp.scenario.com/mcp

Or addhttps://mcp.scenario.com/mcpto any MCP client and sign in with a Scenario account (OAuth),
or use anAPI key. Full setup lives in thescenarioskill.

## Staying up to date

Releases are how changes become visible: every feature, fix, and documentation change merged tomainlands in the next release, staged by release-please as an open release PR. Merging that PR
tags a version, updatesCHANGELOG.mdin this repository, publishes aGitHub release, and posts the notes to theScenario changelog.

* To learn that a skill changed, watch this repository's releases (Watch, then Custom, then Releases
on GitHub) or check any of the changelog pages above. An entry scoped to a single skill carries
that skill's name; changes spanning several skills appear under broader scopes such asskills.
* To pull the changes, runnpx skills updatewhere you installed, or re-run your originalnpx skills addcommand.
* To stay on a reviewed state, pin the install (seeInstall).

## Skills

### Getting started

Connect the Scenario MCP server and learn the core generation loop every other skill builds on.

Skill

Use it for

scenario

Connecting to the Scenario MCP and the core generation loop: discover, schema, run, wait, display, download

### Finding a direction

Turn a blank brief into references, options someone can choose between, and a moodboard the next
batch runs from.

Skill

Use it for

scenario-inspiration

Finding a direction before generating: serendipity, reference hunting, A/B/C/D concept options, moodboard collections

### Images

Generate and edit images: model choice, sizing, references, masked edits, post-processing tools, and
letter-perfect text overlay cards.

Skill

Use it for

scenario-image

Text-to-image and image editing: model choice, sizing fields, prompt limits, reference images, masked inpainting

scenario-multi-reference

One image composed from several references, each with one job (subject, place, pose, style, palette), leaks checked

scenario-product-shots

Product photography from a real photo: packshots, lifestyle scenes, relighting, label-fidelity gates

scenario-brand-kit

Visual identities: SVG logos and wordmarks, palette and type specs, gated variants and applications, the filed kit

scenario-image-editing

Tool-model image edits: 3D LUT grades, effects, expand and reframe, resize, slicing, layers, background removal

scenario-text-overlay

Letter-perfect text overlays: templated transparent PNG cards (taglines, CTAs, legal supers, rich cards) to composite

scenario-storyboards

Comic pages, storybooks, and pre-viz storyboards: script first, one run per panel, a locked cast, lettering in post

scenario-thumbnails

Finished video covers with character fidelity, exact copy and small-preview readability

### Game art and 3D

Sprites, icons, tilesets, textures, skyboxes, 3D models, and walkable spaces for games, the web, and
interactive scenes.

Skill

Use it for

scenario-game-assets

Sprites, icons, props, tilesets, pixel art, concept art, transparent backgrounds, style-consistent batches

scenario-sprite-animation

Walk cycles, idle loops, VFX sprites, and animation sheets from one prompt: GIF vs sprite sheet output, frame slicing, pixel cleanup

scenario-side-view-game-kit

Side-scroller and platformer art: side-view pixel sprite strips for a hero and enemies (run, walk, attack, hurt, poses), parallax layers, seamless wall texture, platform strip, props

scenario-blender-2d-animation

A side-scroller shot animated in Blender from Scenario pictures: a concept frame that locks the look, parallax layers, props and a hero run cycle on its reference, flat image cards with an orthographic camera, keyed jumps and rigid-body props, and a whole new look by swapping the pictures

scenario-textures

Seamless and tileable textures, PBR materials, tiling-safe upscaling, engine-ready sizing

scenario-skyboxes

360 equirectangular panoramas and skyboxes, seam-safe upscaling, engine export

scenario-3d

Text or image to 3D meshes, multi-view reconstruction, retexture and remesh, inline 3D preview, GLB/FBX download

scenario-video-to-motion

Motion capture from a reference or generated video: an uploaded character auto-rigged and animated, or motion alone on a Mixamo or MetaHuman skeleton, with in-place, looping, and engine-ready exports

scenario-blender

Drive an open Blender scene through the Scenario for Blender extension's local MCP server: read the scene, quote and run generations, capture viewport references, place results, plan camera paths

scenario-patina-retexture

PATINA PBR retexture of a finished mesh: material families, one map set per family, Blender apply with geometry untouched, matched before/after comparison film

scenario-orbit-views

New camera angles of one picture through a 3D intermediary: clay layouts in a grounded panorama, repaint per camera, matched transparent set

scenario-walkable-room

A room from one interior photo to walk into: clean plate, splat world, PBR props with impact sounds, splat-based calibration, physics viewer with grab and throw

### Video and audio

Video generation, editing, and color grading, seamless motion loops, music, sound effects, voice,
and speech.

Skill

Use it for

scenario-video

Text-to-video and image-to-video, motion prompting, lipsync, video editing, upscaling, cut/split/concat utilities

scenario-video-editing

Tool-model footage edits: LUT grades and effects, trim, split, resize, reverse, frames, masks, layers

scenario-video-color-grade

Code-written grades on existing footage: looks, relight, log to Rec.709, reference match, one kept color with masks, .cube LUTs, a showreel

scenario-seedance-music-video

Turning a song into a music video: beat-aligned shots, lyric transcription, shot sound under the master, assembly

scenario-seedance-storyboard

Movement that holds across cuts: timecoded shot scripts, character sheets and boards, pose-chained shots that play as one performance

scenario-seedance-drafts

Cheap 480p Seedance takes reviewed and ranked, only the picks finalized to 1080p, with the draft-versus-final cost math

scenario-video-ads

Producing a video ad from a product shot: brief, storyboard, cinematic grammar, fidelity gates, budget, delivery

scenario-ad-variants

Ordered independent campaign edits from existing footage, preserving original gameplay and audio

scenario-audio

Music, sound effects, voice and speech generation, video scoring, audio utilities

scenario-video-assembly

Assembling clips into a finished video: timeline composition, concat with transitions, overlays, music, captions

scenario-motion-loops

Seamless brand-color motion loops in code (backgrounds, bumpers, shape animations) rendered to MP4, with a Scenario cut-out over them

scenario-caption-studio

Captioning a finished video per destination: styled burn-in or SRT, transcription hints, translation, per-platform placement

### Socials

Made for social feeds and chat apps: UGC-style creator videos, fan-cam reactions from a photo, trend
reels recast with your own character, kinetic-typography lyric videos, and animated ChatGPT and
Codex pets, new or updated.

Skill

Use it for

scenario-ugc

UGC-style creator video: talking-head and avatar ads, demos, faceless voiceover, spoken-register scripts, claim safety

scenario-fan-cam

Personalized fan-cam clips: identity edit into a broadcast still, reaction beats to video, graphics composited in post

scenario-reel-recast

A trending reel performed again by your character: same moves, camera and song, outfit swaps, a redecorated room

scenario-kinetic-music-video

Kinetic-typography music video, landscape or 9:16: style frames and footage from Scenario, a JavaScript engine for lyric type on sung onsets, mattes, per-section agents

scenario-chatgpt-pet-create

ChatGPT or Codex pet from an idea or photos: a v2 sprite sheet with sixteen look directions, a v1 copy for web upload, pixel-perfect mode, GIFs, a Codex package

scenario-chatgpt-pet-update

Change an existing pet sheet: fix or redo a row, add look directions to a v1 sheet, a new outfit or color, a rename, a check and GIF preview

### Consistency and custom models

Hold one character, product, or style across a whole set, and train custom models on your own art.

Skill

Use it for

scenario-consistency

Holding one character, product, or style across a set: baseline-plus-delta prompts, reference images, control maps

scenario-identity-library

Creating named characters and props as reusable identities: interview to brief, gated collections, Grid Maker sheets, reuse

scenario-model-training

Training custom models for style, character, or product consistency, and generating with them

### Reviewing and organizing output

Read finished assets back: caption them, extract a style or a control map, check a batch against a
brief or the Quality Gate, compare candidate models on one brief, and file the keepers.

Skill

Use it for

scenario-asset-analysis

Reading assets back: captions, style descriptions, batch review against a brief, control maps, collections, tags

scenario-quality-gate

Pass/warn/fail image verdicts from the Quality Gate: free stored reads, dry-run pricing, feeding suggestions back into the next run

scenario-refine-loop

Iterating until output matches the brief: rubric first, batched critique verdicts, cheapest targeted fix, round caps

scenario-model-comparison

Bake-offs between candidate models on one brief: normalized inputs, a dry-run cost matrix, billed cost and latency, contact sheets, pre-registered criteria

### Formats and placements

Ship one approved master, image or video, to every placement: ratios, safe zones, and platform specs
from social feeds to shops, storefronts, and print.

Skill

Use it for

scenario-formats

Deriving every placement from one master, image or video: crop vs resize vs expand vs reframe, platform specs and safe areas

### Workflows and apps

Discover, run, build, and publish Scenario workflows (apps), and migrate graphs from Weavy, ComfyUI,
or other node editors.

Skill

Use it for

scenario-workflows

Running saved workflows (apps): building the run inputs, dry-run pricing, unsticking approval gates

scenario-workflow-authoring

Creating and editing workflow graphs: editor_info grammar, node wiring, publishing apps, and migrating graphs from Weavy, ComfyUI, or other node editors

### Troubleshooting

Get past a blocked generation, and turn a stuck session into a reproducible public issue.

Skill

Use it for

scenario-moderation

Recovering a blocked generation: provider-side filters, model switching, proportional wording, look-alike errors

scenario-report

Reporting a bug or change request as a reproducible, redacted issue on this repository's public tracker

### Team administration

Govern a team from the agent: which models it can run, who is on it and in which projects,
per-member spend caps, API key roles, and who spent what.

Skill

Use it for

scenario-team-admin

Model access control, team and project membership, per-member Creative Unit caps, API key roles, and spend attribution

scenario-admin-analytics

Cached MCP usage analytics, model and user rankings, CSV exports, adoption PDFs, and a local dashboard

### Image model families

The top image families in depth: generation and editing modes, reference rules, and the caps that
differ per member.

Skill

Use it for

scenario-gpt-image

GPT Image 2.5 Flare and Sunburst, GPT Image 2 and 1.5: member routing, the quality tiers up to max and their price ladder, alpha masks, transparent cutouts, in-image text, pixel sizing

scenario-mai-image

MAI Image: in-image typography, quoted copy prompts, instruction editing (preserve first, one change), per-editor source input shapes, edit cost split

scenario-seedream

Seedream images: member selection (Pro, Lite, 4.5, Layerize), per-member sizing contracts, in-image text, sequence sets, layer splits, cost

scenario-gemini-image

Gemini image (Nano Banana): member choice (Flash, Pro, Lite), instruction editing, reference roles, video stills, Search grounding, cost

scenario-reve

Reve image: v2.1 vs Remix selection, frame-tag reference wiring, maskless instruction edits, per-member caps and cost

scenario-ideogram

Ideogram images: member selection (4.5 typography and edits, Precise Edit, native transparency, layerize text, character, remove background), the 4.5 quality price ladder and sizes, edits that keep the exact canvas, expansion off for exact copy

scenario-grok-imagine-image

Grok Imagine images: text-to-image and instruction editing, exact in-image typography, quoted copy rules, aspect ratio traps, quality and cost tiers

scenario-luma-image

Luma Uni-1 images: create vs edit mode, role-labeled references, web search grounding, rendered text, cost

### Video model families

The top video families in depth: conditioning modes, native audio, editing and extension, and
per-member caps and costs.

Skill

Use it for

scenario-minimax-video

MiniMax Hailuo video: H3 keyframe vs reference modes, bracketed camera commands, native audio prompting, 2.3 duration coupling, cost

scenario-gemini-omni

Gemini Omni video: member selection (first frame, references, edit, extend), prompted native audio, identity from references, motion-locked restyles

scenario-grok-imagine-video

Grok Imagine video: one member per mode (first frame, @image references, edit, extend), prompted audio and dialogue, resolution and preprocessing caps

scenario-veo

Veo video: mode selection (first frame, transitions, references, extend), asset or style references, prompt-directed native audio, tier costs

scenario-seedance

Seedance video: mode selection (first frame, references, edit, extend), conditioning traps, native sound, cost

scenario-kling

Kling video: picking a member across V3, O1, and 2.6 (multi-shot, elements, editing, motion control, lipsync, avatar), audio exclusivity, tier cost

scenario-vidu

Vidu video: tier and mode selection (text, image, start/end frames, references), per-tier caps, two prompt shapes, music toggle traps

scenario-wan

Wan video: member-per-job selection (T2V, I2V, edit, Animate, reframe, outpainting), parameter drift across generations, multi-shot prompts, audio sources

scenario-runway

Runway video: Gen4.5 generation (text, first frame), Aleph 2 footage edits (swap, remove, restyle), keyframe pinning, aspect ratio traps, cost

scenario-luma-video

Luma Ray video: member routing (generate, edit, reframe, modify), option vetoes (10s, loop, HDR, anchors), twin editor ladders, cost

### Audio model families

The top audio families in depth: music, covers and stems, sound effects, speech, dubbing, and video
scoring.

Skill

Use it for

scenario-minimax-music

MiniMax music: vocal songs from a tagged lyric sheet, auto lyrics, instrumental mode, melody-keeping covers, character-count cost

scenario-elevenlabs

ElevenLabs audio: picking the member (TTS, music, SFX, dubbing, re-voicing, isolation), voice and tag rules, song section grammar, cost

scenario-ace-step

ACE-Step music: one member per mode, Turbo vs Quality lanes, lyric sheet tags, cover strength, repaint windows, stem edits

scenario-sonilo

Sonilo audio: SFX and music from text or video, standalone track vs muxed clip, segment prompts, keep-speech scoring, cost

### 3D model families

The top 3D families in depth: mesh generation, retexture and rigging toolchains, portraits, and
explorable worlds and splats.

Skill

Use it for

scenario-meshy

Meshy 3D: generate from image, multi-view, or text, then retexture, remesh, UV unwrap, rig, or animate; texture precedence, Ultra mode, polycount traps

scenario-rodin

Rodin 3D: member selection (image-to-3D, text-to-3D, Fast lanes, Bang! mesh splitting), full versus Fast parameter dialects, topology and tier traps, cost

scenario-sparc3d

Sparc3D image-to-3D: ordered multi-view input, mesh vs textured output, per-member resolution spellings, face budgets, long-job waits

scenario-3d-worlds

3D worlds and splats: member choice by input (text, image, pano, multi-view, video, object), Marble draft-then-upgrade seed reuse, HY World skybox-to-splat pipeline, long-job patience

### Expert tools: ZBrush

DCC software. A lead and eight specialists that drive Maxon ZBrush 2026 through its agent bridge:
sculpting, characters and creatures, stylized work, hard surface, polypaint and renders, posing and
3D print, retopology and export, automation. The bridge was proven live; full live tests of every
skill are still pending.

Skill

Use it for

scenario-zbrush-expert

ZBrush lead: the agent bridge (launch, scripted strokes, dialog-free export), ZBrush Python and ZScript, review renders, 2026 traps, handoffs to the specialists

scenario-zbrush-automation

ZBrush automation: batch jobs over OBJ or ZTL folders, ZBrush Python and ZScript, macros, UV Master, Decimation Master, Multi Map Exporter, GoZ round trips

scenario-zbrush-character-creature

Realistic heads, bodies, and creatures in ZBrush: anatomy and landmarks, skin, pores, wrinkles and scales, subdivision and HD Geometry planning

scenario-zbrush-hard-surface

Hard surface in ZBrush: ZModeler, Dynamic Subdivision and creasing, Live Boolean, Knife and Slice curves, IMM, ArrayMesh, NanoMesh, Panel Loops

scenario-zbrush-paint-render

Polypaint and renders in ZBrush: color zones, cavity and AO passes, Spotlight, baking to texture or vertex color, BPR or Redshift, turntables

scenario-zbrush-pose-print

Posing and 3D print in ZBrush: Transpose Master, Gizmo posing with masks, ZSphere rigs, print scale, hollowing, wall thickness, drain holes

scenario-zbrush-retopology-export

Sculpt, scan, or AI mesh to production topology and files in ZBrush: ZRemesher and guides, Retopo brush, Project All, UVs, normal and displacement maps, export

scenario-zbrush-sculpting

Organic sculpting in ZBrush: primary and secondary forms, DynaMesh, Sculptris Pro or subdivision levels, core brushes, masks and polygroups

scenario-zbrush-stylized

Stylized characters, collectibles, and toys in ZBrush: shape language, deliberate exaggeration, crisp planes through subdivision, silhouette reads

### Expert tools: Blender

DCC software. A lead and fourteen specialists that drive Blender 5.2 through Python, headless or in
a live session: sculpting, retopology, UVs and baking, shading, hair, rigging, animation, previs,
blockouts for render-to-real video, Geometry Nodes, lighting, Grease Pencil, hard surface, export to
game engines. Twelve test suites pass headless on Blender 5.2.1.

Skill

Use it for

scenario-blender-expert

Blender lead: Python headless or through a live MCP bridge, the expert review loop, the shared review and mesh-audit toolkit, Blender 5.2 API traps

scenario-blender-animation

Blender animation: cycles, jumps, acting and lip sync, stepped blocking to spline and polish, timing and spacing, graph editor, slotted actions and NLA

scenario-blender-blockout

Blockouts that guide render-to-real video: color-coded proxies at metric scale, cameras locked to the timeline, framing audits, playblast and hand-off sheet

scenario-blender-export

Exports for game engines: FBX, GLB, USDZ and STL presets for Unity, Unreal, Godot, Roblox, three.js, round-trip checks, LODs, collision, batch

scenario-blender-geometry-nodes

Geometry Nodes: procedural modeling, scattering, curves and loops, simulation zones, 5.2 physics, closures and bundles, node-group assets

scenario-blender-grease-pencil

Grease Pencil in Blender 5.x: 2D and 2.5D illustration, frame-by-frame and cutout animation, fills, interpolation, Line Art, strokes on meshes

scenario-blender-hair

Hair and fur with hair curves: hairstyles, animal fur, Essentials hair nodes, density masks and partings, hair cards and mesh hair for games

scenario-blender-hard-surface

Hard surface in Blender: booleans and cutters, bevels, weighted normals, support loops and creases, fixing smeared or pinched shading

scenario-blender-lighting-rendering

Blender lighting and rendering: motivated and three-point setups, HDRI and sun, EEVEE vs Cycles, noise and leaks, AgX color management, passes and compositing

scenario-blender-previs-storyboard

Script to previs in Blender: beats to shot list, cameras and lenses, staging and screen direction, cuts and camera moves, storyboards and animatics

scenario-blender-retopology

Retopology in Blender: dense sculpt, scan, or AI mesh to clean topology for animation, subdivision, or a game low poly, loop and pole placement

scenario-blender-rigging

Rigging in Blender: Rigify metarigs, automatic weights and weight fixes, IK/FK, foot roll, twist bones, drivers and custom properties

scenario-blender-sculpting

Sculpting heads and characters in Blender: blockout from primitives, planes and landmarks, stylized and realistic faces, remesh or multires resolution

scenario-blender-texturing-shading

Texturing and shading in Blender: PBR from texture sets, procedural materials, wear and grime, triplanar mapping, skin and eyes, stylized looks

scenario-blender-uv-baking

UVs and baking in Blender: seams, packing, texel density, UDIMs, normal, AO, curvature, and ID bakes from high poly or Multires, fixing bad bakes

### Expert tools: Maya

DCC software. A lead and ten specialists that drive Autodesk Maya 2027 through Python, batch or
live: modeling, retopology and UVs, rigging, skinning, animation, groom, FX, look dev, Arnold
lighting and rendering, pipeline scripting.

Skill

Use it for

scenario-maya-expert

Maya lead: maya.cmds and OpenMaya 2.0, mayapy batch jobs, a commandPort or MCP bridge into a live Maya, scene validation, Maya 2027 traps

scenario-maya-animation

Maya animation: cycles, jumps, heavy lifts, acting and lip sync, stepped blocking to spline and polish, Graph Editor, layers, mocap cleanup, game clips

scenario-maya-deformation

Skinning in Maya: binding and weight painting, Skin Tools or ngSkinTools layers, fixing pinching and volume loss, weights for Unreal or Unity

scenario-maya-fx

Maya FX: nCloth and Nucleus, nParticles, Bifrost smoke, fire, liquids, and MPM, MASH scattering

scenario-maya-groom

Grooming with XGen: scalp hair, brows, lashes, and fur, guides, clumps, and density maps, aiStandardHair, hair that moves

scenario-maya-lighting-rendering

Maya lighting and rendering with Arnold: hero, character, and sequence lighting, noise and fireflies, AOVs and light groups, denoising, color management

scenario-maya-lookdev

Look dev in Maya with Arnold: OpenPBR or aiStandardSurface, Substance and UDIM texture sets, color spaces, normal and displacement fixes, skin, metal, glass

scenario-maya-modeling

Maya modeling: hard-surface props and vehicles, game-ready or SubD models, base meshes, support loops vs bevels vs creases, scene cleanup

scenario-maya-pipeline-scripting

Maya pipeline code: mayapy batch jobs, scene validation and fixes, FBX for Unreal or Unity, Alembic, USD, references, PySide6 tools

scenario-maya-retopology-uv

Retopology and UVs in Maya: sculpt, scan, or AI mesh to animation-ready or game-ready topology, Quad Draw, deformation tests, UV layout

scenario-maya-rigging

Rigging in Maya: joint placement and orientation, IK/FK switching and matching, space switching, foot roll, spline spines, matrix rigging, controls

### Expert tools: Unreal Engine

Game engine. A lead and nine specialists that drive Unreal Engine 5.8 on macOS through Editor
Python, headless jobs, and Epic's Unreal MCP server: world building, materials, lighting and
rendering, gameplay, animation, cinematics, VFX, pipeline automation, performance.

Skill

Use it for

scenario-unreal-expert

Unreal lead: Editor Python, headless UnrealEditor-Cmd jobs, Epic's Unreal MCP server, the Remote Control API, console commands, 5.8 traps

scenario-unreal-animation

Unreal animation: skeletal import, IK Rig and Retargeter, Motion Matching and Pose Search, root motion, foot IK, Control Rig

scenario-unreal-cinematics

Unreal cinematics with Sequencer: shot lists, master and shot sequences, cameras and lenses, per-shot lighting, Movie Render Graph output

scenario-unreal-gameplay

Unreal gameplay: characters and abilities, enemy AI, HUD, Blueprint vs C++, GAS, StateTree vs Behavior Tree, Enhanced Input, replication

scenario-unreal-lighting-rendering

Unreal lighting and rendering: physical units and exposure, Lumen, MegaLights, virtual shadow maps, sky and fog, post process, path tracer

scenario-unreal-materials

Unreal materials: master materials and instances, Substrate, glass and emissives, decals, landscape layers and RVT, toon shading, shader permutations

scenario-unreal-performance

Unreal performance: frame budgets, CPU vs GPU bound, hitches and PSO stutter, GC spikes, Lumen, Nanite, VSM, and Niagara cost, profiling

scenario-unreal-pipeline-automation

Unreal pipeline: bulk FBX, USD, OBJ, or glTF import from Maya, ZBrush, or Blender, Editor Python tools, Interchange, naming and validation, cook and package

scenario-unreal-vfx

Unreal VFX: Niagara systems (fireballs, trails, impacts, smoke, sparks), Niagara fluids, scalability and pooling, Chaos destruction

scenario-unreal-world-building

Unreal levels and open worlds: World Partition, Data Layers, Level Instances, HLOD, landscape, foliage, PCG scatter, Nanite

### Expert tools: Unity

Game engine. A lead and thirteen specialists that drive Unity 6.3 LTS on macOS through batch mode, a
live editor, and command-line builds: architecture, gameplay, 2D, animation, UI, VFX, shaders,
rendering and lighting, world building, performance, mobile, Web, pipeline automation. Every
procedure was run live in Unity 6.3.

Skill

Use it for

scenario-unity-expert

Unity lead: batch mode and -executeMethod jobs, a live editor over the Unity CLI, MCP servers, the Test Framework, command-line builds, proof by capture

scenario-unity-2d

Unity 2D in URP: sprite import and PPU, atlases, Tilemaps and Rule Tiles, 2D lights, 2D animation, platformer and top-down controllers

scenario-unity-animation

Unity animation and cameras: humanoid import and retargeting, Animator Controllers and blend trees, root motion, Animation Rigging, Timeline, Cinemachine 3

scenario-unity-architecture

Unity C# architecture: ScriptableObject data, events and services, inventory, health, save and load, Input System, Awaitable, assembly definitions, Git and LFS

scenario-unity-gameplay

Unity gameplay: enemy AI, NavMesh and agents, state machines and behavior trees, projectile physics, collision layers, CharacterController vs Rigidbody

scenario-unity-mobile

Unity on Android and iOS: frame and thermal budgets, texture compression, touch controls and safe areas, startup time, AAB and signing

scenario-unity-performance

Unity performance: frame spikes and hitches, GC, draw and SetPass calls, CPU vs GPU bound, Profiler, Memory Profiler, Frame Debugger, GPU Resident Drawer

scenario-unity-pipeline-automation

Unity content pipeline: AssetPostprocessor import rules, prefab and scene generation from script, Addressables, content-validation tests, CI builds

scenario-unity-rendering-lighting

Unity rendering and lighting: URP setup and quality tiers, sun and sky, lightmaps and Adaptive Probe Volumes, reflection probes, shadow and bake fixes

scenario-unity-shaders

Unity shaders in URP: HLSL, Shader Graph water, toon, dissolve, and outline, renderer features on Render Graph, compute shaders, variants and stripping

scenario-unity-ui

Unity game UI: menus, settings, HUD and health bars, uGUI vs UI Toolkit, scaling from phone to 4K, layout groups, UXML and USS

scenario-unity-vfx

Unity VFX: explosions, projectiles, spells, and smoke with the Particle System or VFX Graph, overdraw and mobile cost

scenario-unity-web

Unity on the Web: WebGL and Web build settings, compression and server headers, build size and load time, portal limits, Addressables on the Web

scenario-unity-world-building

Unity levels and open worlds: terrain from code or heightmaps, procedural islands, foliage rules, ProBuilder graybox, modular kits, landmarks, spline roads

### Expert tools: Godot

Game engine. A lead and thirteen specialists that drive Godot 4.7 on macOS through headless jobs,
windowed captures, GUT and gdUnit4 tests, and command-line exports: architecture, gameplay, 2D, 3D
worlds, animation, UI, VFX, shaders, rendering and lighting, audio, multiplayer, performance and
export, pipeline automation. Every procedure was run live in Godot 4.7.2.

Skill

Use it for

scenario-godot-expert

Godot lead: headless --script jobs, --import and --check-only, windowed captures, GUT tests, command-line exports, MCP into an editor, proof by capture

scenario-godot-2d

Godot 2D: platformer and top-down controllers, TileMapLayer and terrains, pixel-perfect stretch and cameras, 2D lights, y-sort, parallax, AI-generated sprites

scenario-godot-3d-world

Godot 3D levels: third-person and FPS controllers, CSG blockout, GridMap, terrain, MultiMesh scatter, streaming, Jolt physics, GLB imports

scenario-godot-animation

Godot animation: AnimationPlayer and RESET, AnimationTree state machines and blend spaces in code, Mixamo retargeting, root motion, IK, cutscenes

scenario-godot-architecture

Godot code structure: scenes and nodes, signals and event bus autoloads, custom Resources, components, save and load, InputMap rebinding, typed GDScript

scenario-godot-audio

Godot audio: buses and effects, volume sliders, combat with hundreds of enemies, 3D sound and reverb zones, adaptive and interactive music, SFX variation

scenario-godot-gameplay

Godot gameplay: enemy AI that patrols, chases, and attacks, state machines, behavior trees, NavigationAgent3D, hitbox combat, dialogue, procedural dungeons

scenario-godot-multiplayer

Godot multiplayer: ENet and WebSocket host and join, RPCs, MultiplayerSpawner and Synchronizer, authority, lag, lobbies, dedicated servers

scenario-godot-performance-export

Godot performance and shipping: profiling and monitors, CPU vs GPU bound, hitches, phones overheating, macOS, Web, Android, and iOS exports

scenario-godot-pipeline-automation

Godot pipeline: batch GLB import and naming rules, import presets and post-import scripts, editor plugins, @tool, gdUnit4 and GitHub Actions CI

scenario-godot-rendering-lighting

Godot rendering: Forward+, Mobile, or Compatibility, SDFGI, VoxelGI, and lightmaps, environment and fog, shadows, light leaks, quality tiers

scenario-godot-shaders

Godot shaders: .gdshader spatial, canvas_item, particles, and sky code, VisualShader in code, toon water, dissolve, outlines, stencil, post-processing

scenario-godot-ui

Godot game UI: main menu, settings, HUD and health bars, Control layout, containers and anchors, themes, scaling to any screen, gamepad focus, localization

scenario-godot-vfx

Godot VFX and game feel: GPUParticles explosions, fireballs with trails, impacts, sparks and smoke, hit stop, screen shake, particle cost on phones

### Expert tools: Roblox Studio

Game engine. A lead and thirteen specialists that drive Roblox Studio on macOS through its built-in
MCP server, playtests driven by code, offline Luau checks, and Rojo builds: architecture, Luau,
networking and security, data, tooling, environment, VFX and audio, UI, animation, gameplay, assets
and avatar items, performance, monetization. Procedures were run live in Roblox Studio 0.743.

Skill

Use it for

scenario-roblox-expert

Roblox lead: Studio's built-in MCP server, Luau run in Edit and in playtests, simulated input and captures, two-solver type checks, Rojo, RunScript, Open Cloud

scenario-roblox-animation

Roblox animation: priorities and blending, events and markers, Blender and FBX imports, custom and creature rigs, IKControl, FaceControls, Animate replacements, NPC animators

scenario-roblox-architecture

Roblox code structure: where scripts go, RunContext, module loaders, services and controllers, signals and attributes, CollectionService tags, cleanup, Rojo layout

scenario-roblox-assets

Roblox 3D assets and avatar items: Blender, GLB, and FBX imports, AI-generated meshes, scale in studs, triangle and texture budgets, PBR SurfaceAppearance, UGC validation

scenario-roblox-data

Roblox player data: DataStores and UpdateAsync, session locking with ProfileStore, schema migration, receipts granted once, trading, leaderboards, MemoryStore, teleports

scenario-roblox-environment

Roblox maps and lighting: graybox, terrain, parts vs unions, collision fidelity, MaterialVariants, Lighting and Atmosphere moods, foliage scatter, streaming, level of detail

scenario-roblox-gameplay

Roblox gameplay: NPC AI and pathfinding, hundreds of enemies, hitboxes and melee combos, raycasts and projectiles, knockback, physics movers, vehicles, round loops

scenario-roblox-luau

Roblox Luau: task library and deferred events, --!strict and the new type solver, typed classes, memory leaks, Parallel Luau with Actors, --!native, buffers

scenario-roblox-monetization

Roblox monetization and live ops: Developer Products and passes, subscriptions, receipts granted once, loot odds and PolicyService, rewarded video, analytics funnels, A/B tests

scenario-roblox-networking

Roblox networking and security: remote design and server validation, rate limits, speed, fly, and hitbox exploits, network ownership, Server Authority, bandwidth

scenario-roblox-performance

Roblox performance: mobile FPS and frame spikes, server heartbeat, physics and network load, memory leaks, MicroProfiler and Script Profiler, streaming, budgets, releases and rollbacks

scenario-roblox-tooling

Roblox team tooling: Rojo and Script Sync, Wally, Rokit, luau-lsp, Selene, StyLua, Lune and in-engine tests, GitHub Actions CI, Open Cloud publishing and Luau Execution

scenario-roblox-ui

Roblox game UI and input: HUD, menus, shop grids, scaling from phone to TV, safe areas, layouts and StyleSheets, gamepad navigation, the Input Action System, localization

scenario-roblox-vfx-audio

Roblox VFX and audio: particles, beams, trails, flipbooks, hit and explosion effects, the Audio API with wires and emitters, 3D sound, music and ducking, footsteps

## Example prompts

Once the skills are installed and the MCP server is connected, ask your agent things like:

* "Generate four style-matched potion icons with transparent backgrounds for my RPG inventory"
* "Make a seamless brick texture, then upscale it to 2048 without breaking the tiling"
* "Turn this concept sketch into a 3D prop and let me preview it before I export the GLB"

## What is an Agent Skill?

A skill is aSKILL.mdfile with procedural knowledge an agent loads on demand, defined by the openAgent Skills specification. TheskillsCLI installs these
files into 70+ agents, and the ecosystem directory lives atskills.sh.

## Contributing

SeeCONTRIBUTING.mdfor the contribution workflow, andAGENTS.mdfor
the authoring contract, the public-content policy, validation, and the application-testing bar.
One-time setup after cloning: install theprerequisites, uv included, then
runpnpm install(installs commitlint, cspell, prettier, and the husky git hooks).pnpm run validateruns the same content checks CI runs; commit messages and the PR title are
linted separately with commitlint. PRs welcome; PR titles follow Conventional Commits since they
become the squash commit header onmain.

Every script shipped with a core skill has a test suite intests/<name>/; expert tools have one
suite per family instead.pnpm testruns them all (CI does too). Suites need Python 3.11+, plus
ffmpeg on PATH where a suite uses it. With uv installed,pnpm testgives each suite the
dependencies in itstests/<name>/requirements.txt; without uv, install them intopython3first.
Python suites use stdlibunittest, TypeScript suites use vitest.

## License

MIT