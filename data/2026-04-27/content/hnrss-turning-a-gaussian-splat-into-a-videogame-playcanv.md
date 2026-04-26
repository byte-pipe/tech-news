---
title: Turning a Gaussian Splat Into a Videogame | PlayCanvas Blog
url: https://blog.playcanvas.com/turning-a-gaussian-splat-into-a-videogame/
site_name: hnrss
content_file: hnrss-turning-a-gaussian-splat-into-a-videogame-playcanv
fetched_at: '2026-04-27T06:00:34.763407'
original_url: https://blog.playcanvas.com/turning-a-gaussian-splat-into-a-videogame/
date: '2026-04-23'
published_date: '2026-04-22T00:00:00.000Z'
description: How I turned a photogrammetric 3D Gaussian Splat scene into a playable browser FPS - with collision, pre-baked lighting, navmesh-driven NPCs and behavior-tree AI, all in PlayCanvas.
tags:
- hackernews
- hnrss
---

Gaussian Splatting gives youphotorealisticenvironments for free. The catch: a splat is just a cloud of oriented blobs - no triangles, no colliders, no navmesh, no lights. Drop a character in and they'll float through walls looking like they belong in a different universe.

This post walks through the demo I built to fix all of that:

* 👉Play it in your browser- WASD, mouse to aim, left-click to fire.
* 👉Check the project- the full PlayCanvas project is public. Every script mentioned in this post lives inside it, ready to read, fork, or remix.

The scene is a gorgeous indoor scan of a real abandoned place byChristoph Schindelar. Christoph is one the best artists working with Gaussian Splats out there, so when he proposed to scan a real place for me, I jumped at the opportunity. On top of that splat I bolted a physics collider, a grid of baked lighting probes, a Recast navmesh, eight personality-driven NPCs and a classic FPS loop. Everything runs in a browser tab.

## 🏗️ The Build​

Here's how I built it, step by step.

### 📥 Step 1: Download a Splat from SuperSplat​

Before any code, you need a scene. Any splat onSuperSplattaggedDownloadablehas been published under Creative Commons by its author - grab the.plyor.sogand drop it straight into your own PlayCanvas project. The lighting, clutter and scale of the scan I picked were already cinematic, so I didn't have to art-direct anything.

Try it now

Jump straight to thepre-filtered downloadable viewand pick one.

### 📡 Step 2: Convert the Splat to Streamed SOG Format​

The Swiss Army knife for everything that follows issplat-transform- PlayCanvas's open-source CLI for converting splats. We'll lean on it for streamed LOD here and for a collision mesh in the next step.

My scene is a few million Gaussians - big enough that shipping it as a single.sogasset would punish anyone on a phone or a slow connection. The fix isStreamed LOD: instead of one monolithic file, SuperSplat (andsplat-transform) write out afolder of SOG chunksplus a manifest. The runtime loads chunks on demand based on the camera's viewpoint and the device's capability - high-end desktop pulls full detail around the player, a phone pulls a lighter subset, and neither of them stalls waiting for the whole file.

Scripts/streaming-lod.mjshooks into the camera and asks the runtime to keep the chunks around the player fully loaded before the game starts - so you never see pop-in mid-firefight.

Try it now

If your splat is over a few million Gaussians, export it as streamed LOD (the easiest way is from SuperSplat's export dialog - see theStreamed LOD docs) and let the viewer stream it. Your mobile players will thank you.npm install -g @playcanvas/splat-transform

### 🧱 Step 3: Generate a Collision Mesh​

This used to be the hard part. A splat has no surfaces, so physics is blind to it. You can't walk on it, shoot through it, or path around it. That's wheresplat-transformearns its keep again - the flag you want is-K/--collision-mesh. It voxelizes the splat, flood-fills the navigable interior from a seed position, and writes out a watertight.collision.glbthat you can import straight into PlayCanvas as ameshcollider.

splat-transform scene.ply \
 --seed-pos 0,1,0 \
 --voxel-params 0.05,0.1 \
 --voxel-carve 1.6,0.2 \
 -K \
 scene.sog

That one command gives me two outputs:

* scene.sog- a single-file compressed splat for quick iteration; the shipped build uses the streamed folder from Step 2.
* scene.collision.glb- a voxel-derived mesh that hugs the real geometry.

I dropped both into the PlayCanvas project and attached the GLB to an invisible entity with aCollisioncomponent (mesh) and aRigid Bodycomponent (static). Suddenly the player has a floor, the bullets can collide with walls, and the NPCs have something to walk on. No modelling, no clean-up.

Try it now

One command turns a pretty splat into a playable one - runsplat-transform scene.ply -K scene.sogand drop the resulting.collision.glbinto your project as a static mesh rigidbody.

### 💡 Step 4: Bake a Lightness Grid from the Splat​

Splats carry their lighting baked into every Gaussian. That means the scene looksamazingand unchanging. But my player's weapon model, the NPC soldiers and the pickups are ordinary lit PBR meshes - they'd stand out like cardboard cutouts under gym lighting unless they somehow inherited the splat's lighting.

I didn't want to re-light the splat. I wanted a cheap way to ask "how bright is it here?" at any point in the map, at runtime, for my regular meshes.

HowScripts/probes.jsworks:

1. Grab the AABB of a designated floor entity and build a1-metre grid of probe positions1 metre above the ground.
2. Create a tiny 16×16 offscreenRenderTargetand a 90° FOV camera that renders only theWorldlayer (i.e. the splat - no characters, no HUD, no viewmodel).
3. For each probe, render6 facesof a cube (+X, -X, +Y, -Y, +Z, -Z),readPixelsthe 16×16 RGBA output, and compute luminance using the standard Rec. 601 weights:this._faceLuminance+=0.299*r+0.587*g+0.114*b;// ... after all 6 faces:varlightness=this._faceLuminance/1536;// 6 faces * 256 pixels
4. Stash the value in agridDepth × gridWidth2D array and spawn a tiny debug sphere at the probe position withemissive = lightnessso you canseethe light field floating in the scene.
5. When all probes are done,console.log(JSON.stringify(this.probeJSON)). I copy that out once, save it aslightness.json, attach it as a JSON asset, and delete the probes entity.

Here's the bake in action - each debug sphere pops in as its cube of faces is rendered and its luminance is averaged. Bright spheres mark a well-lit spot on the floor; dim ones sit in corners and under cover. By the end you can read the scene's lighting as a dotted heatmap before a single byte of JSON is written.

At runtime, every dynamic character script (weapon, NPC, pickup) loadslightness.json, bilinearly samples the grid at its world position, remaps it to a sensible exposure range and callsmeshInstance.setParameter('exposure', value). Step from a bright atrium into a dim corridor and your hands darken smoothly. Fire your weapon and the pulsating omni-light bounces off the splat around you.

─── Probes: baking 392 probes (28 x 14) ───
Probe 1/392 lightness: 0.4821
Probe 2/392 lightness: 0.4733
...

The whole bake takes ~15 seconds once, then the JSON is ~40 KB. No expensive runtime probes, no deferred relighting, just a lookup table.

### 🛠️ Step 5: Vibe Code with the PlayCanvas VS Code Extension​

I didn't write any of this in the PlayCanvas web editor's code panel. I used thePlayCanvas extension for VS Code- which also works insideCursor, so I could pair-program with Claude while editing.

Save the file → the editor picks up the change → reload the launch tab → test. That round-trip is measured in seconds.

Most of the gameplay logic in this demo -character-controller.js,anim-states.js,npc-ai.js,probes.js- was iterated on entirely from Cursor.

Try it now

Install thePlayCanvas VS Code extension. If you live in VS Code or Cursor, it turns PlayCanvas into a normal dev environment.

### 🔄 Step 6: Version Your Project with PlayCanvas + GitHub​

"What did I change yesterday, and how do I roll back?" PlayCanvas ships a first-partyversion controlthat answers exactly that. You can also use GitHub at the root of your locally synced PlayCanvas project (via the VS Code extension). Don't forget to add a.pcignoreso the.gitfolder isn't synced to the cloud.

Combined with the VS Code extension, this is about as close to "I'm working in a normal repo" as I've ever had in a browser-first engine. If I break the NPC AI, I'm onegit revertaway from last night's working build.

Try it now

Link a GitHub repo to your PlayCanvas project before you start. You'll thank yourself the first time an AI coding agent commits a bad refactor at 1 AM.

### 🧭 Step 7: Generate a Navmesh from the Collision Mesh​

NPCs can't path on a splat either - they need a navmesh. For the runtime, I userecast-navigation, loaded straight fromesm.shwith dynamic import - zero bundler, just:

const
 recast 
=
 
await
 
import
(
'https://esm.sh/recast-navigation'
)
;
await
 recast
.
init
(
)
;
const
 imported 
=
 recast
.
importNavMesh
(
new
 
Uint8Array
(
navmeshBuffer
)
)
;

Toproducethenavmesh.binbinary, I feed the samescene.collision.glbfrom Step 3 into a small offline Recast-based generator. The collision mesh already represents "solid floor you can walk on", so Recast just has to rasterize it, filter walkable spans and build the nav polygons - takes a few seconds.

I'm cleaning up the generator into a standalone library and will publish it on GitHub shortly - drop-in collision-GLB-to-navmesh-binary for any PlayCanvas project. Follow myX accountif you want the drop.

Want to see the navmesh in-game? PressNin the demo to toggle the debug overlay - the walkable polygons, agent positions and current paths all light up on top of the splat.

Coming soon

Once the library is live, it'll be a one-liner:npx glb-to-navmesh scene.collision.glb navmesh.bin

### 🧠 Step 8: Give NPCs a Brain with Behavior Trees and Personalities​

The NPCs are the part I had the most fun with. Every soldier in the demo is driven by a classicbehavior tree- the same abstraction Halo 2 popularised two decades ago and that's still the default for AAA AI in 2026.

Scripts/npc-ai.jsexposes four primitives:

sequence
(
...
children
)
 
// all must succeed
selector
(
...
children
)
 
// first non-failure wins
condition
(
pred
)
 
// leaf: true/false
action
(
fn
)
 
// leaf: 'success' | 'failure' | 'running'

…and then every NPC's brain is built by composing those, parameterised by apersonality:

return
 
selector
(
 
sequence
(
isDead
,
 autoRespawn
)
,
 
sequence
(
 isAlive
,
 
selector
(
 
sequence
(
isReloading
,
 stopShooting
)
,
 
sequence
(
ammoEmpty
,
 doReload
)
,
 
...
(
traits
.
healPriority
 
>
 
0.4
 
?
 
[
sequence
(
hpBelow
(
retreat
)
,
 hasPickupsNearby
,
 goToPickup
)
]
 
:
 
[
]
)
,
 
...
(
traits
.
lootPriority
 
>
 
0.7
 
?
 
[
sequence
(
hasPickupsNearby
,
 goToPickup
)
]
 
:
 
[
]
)
,
 
...
(
traits
.
retreatThreshold
 
>
 
0.3
 
?
 
[
sequence
(
hpBelow
(
retreat
)
,
 retreat
)
]
 
:
 
[
]
)
,
 
...
(
traits
.
aggression
 
>
 
0.2
 
?
 
[
sequence
(
hasEnemiesInRange
(
range
)
,
 engageEnemy
)
]
 
:
 
[
]
)
,
 guard
 
)
 
)
)
;

Spawn eight NPCs with eight different personalities -Sgt. Havoc(aggressive, pushes),Ghost(cautious, heals),Captain Valor(heroic),Strategist(tactical),Chaos(randomness 0.8, impossible to read),Loot Goblin(greedy, will run across the map for a pickup),Chicken(cowardly, retreats at 80% HP),Grumps(grumpy) - and they already feel distinct, because thesametree collapses to wildly different priority orders based on traits.

Each agent'sposition,aimAngle,animBitsis updated every tick. The PlayCanvas side -npc-controller.js- is just a dumb bridge that reads those fields, sets the entity transform, picks an anim state, fires a muzzle-flash ray, triggers sounds. The AI itself haszero PlayCanvas dependenciesexceptpc.Vec3; it could be lifted into Three.js, Babylon, a headless sim, whatever.

Try it now

If you've been nervous about behavior trees, readChris Simpson's primerand then copy my four-function implementation. It's 20 lines of code and it unlocks production-grade AI.

## 🎮 What You Need to Build One of These​

To recap the full stack:

* 📥Environment- any downloadable splat fromSuperSplat, or your own capture.
* 📡Streaming- convert withsplat-transformto a streamed SOG folder so phones and slow connections don't stall.
* 🧱Collider-splat-transform -K→.collision.glb, dropped into PlayCanvas as a static mesh rigidbody.
* 💡Lighting- bake alightness.jsongrid withprobes.js, sample it per-mesh-instance at runtime.
* 🛠️Authoring-PlayCanvas VS Code extensionfor a normal save-and-reload dev loop.
* 🔄Versioning-PlayCanvas version controland/or GitHub via the VS Code extension.
* 🧭Pathfinding-recast-navigationfromesm.sh, fed a pre-bakednavmesh.bin(generator library coming soon).
* 🧠AI-behavior trees+ personality-driven traits.

Every one of those pieces is free and open source. The whole thing ships as static files to a CDN. My build is 68 MB (splats environment streamed separately from AWS S3) and cold-loads in a few seconds.

## 💚 Free and Open Source​

SuperSplat,splat-transform, recast-navigation and the PlayCanvas Engine are all open source. And so isthis demo- the whole PlayCanvas project is public. Sign up for a free PlayCanvas account, fork the project, and every script mentioned above (probes.js,npc-ai.js,npc-controller.js, the navmesh wrapper, and the rest) is yours to read or remix. If you take them somewhere cool, I want to see it.

## 👂 Try It, Break It, Tell Me​

Play the demo. Stand in a bright room and watch an NPC walk into the shadow. Fire your weapon next to a wall and watch the splat flash. Crouch into a corner and notice the footsteps go quiet.

Then go build your own. If you have questions, find me and the rest of the splat-creator community on thePlayCanvas Discord- that's where all the interesting splats-into-games conversations are happening right now.

See you in there.