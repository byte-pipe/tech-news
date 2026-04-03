---
title: Building a new Flash - by Bill
url: https://bill.newgrounds.com/news/post/1607118
site_name: hackernews_api
content_file: hackernews_api-building-a-new-flash-by-bill
fetched_at: '2026-03-06T06:00:13.656001'
original_url: https://bill.newgrounds.com/news/post/1607118
author: TechPlasma
date: '2026-03-05'
description: 'I don''t know where to start with this but yeah I''m making flash if flash was built in 2026. I''m making it compatible with Linux,Mac, and PC. If you''d like to support this project I''ve started a patreon I''ll still post updates here on Newgrounds though :) It’s a full 2D animation authoring tool — timeline, drawing tools, symbol library, tweening, scripting, the works — built from the ground up in C# with Avalonia and SkiaSharp. This isn’t a proof of concept or a weekend project. It’s a real authoring environment. Here’s where things stand: Drawing engine — I built a vector engine based on a DCEL (doubly-connected edge list) data structure. If you’ve ever used Flash’s merge drawing mode where shapes eat into each other, that’s what this replicates — and it supports all five of Flash’s original paint modes. Paint Normal, Paint Behind, Paint Fills, Paint Selection, Paint Inside. The whole set. Timeline — Keyframes, frame-by-frame, onion skinning. It works the way you expect
  it to if you’ve spent any time in Flash. Shape tweening — Actual shape tweening with contour correspondence. Not just morphing a bounding box. Symbol library — Graphic symbols, movie clips, the whole organizational structure Flash users rely on. .fla / XFL import — This is the one I’m most proud of. You can open your old Flash files. As far as I know, this is the only open-source tool that functions as a full authoring environment and can actually import .fla files. Not just play them back — edit them. Scripting — I’m building a dual-surface scripting system using Roslyn (the C# compiler). One surface for authoring-time scripts (think JSFL but way more powerful), one for runtime frame scripts (think ActionScript but in C#). I’m also planning an ActionScript-to-C# transpiler so imported .fla scripts aren’t just dead code. Sound editor — Embedded, built on SkiaSharp waveform rendering. This is a brief run down of everything there''s so much already and I''m constantly adding more. If you''d
  like to support this project I''ve started a patreon it''d be awesome to build a dedicated team to making this even better.'
tags:
- hackernews
- trending
---

00:00
	

		00:00
	

Newgrounds

Login

 /
 
Sign Up

						Bill					

 FOLLOW

 

 Bill Premo 

@Bill

Age 34

Game Developer

American Academy of Art

Las Vegas

Joined on 7/15/03

* YouTube
* Twitter

 

Level:
 
23

Exp Points:
 
5,874 / 5,880

Exp Rank:

													9,047											

Vote Power:
 
6.52 votes

Art Scouts

5

Rank:

Private

Global Rank:

													3,700											

Blams:

1,356

Saves:

1,171

B/P Bonus:

18%

Whistle:
 
Bronze

Trophies:
 
60
 
Medals:
 
514
 
Supporter:
 
10y 9m 18d
 
Gear:
 
3

 

## Building a new Flash

Posted byBill- 1 day ago

I don't know where to start with this but yeah I'm making flash if flash was built in 2026. I'm making it compatible with Linux,Mac, and PC. If you'd like to support this project I've started apatreonI'll still post updates here on Newgrounds though :)

It’s a full 2D animation authoring tool — timeline, drawing tools, symbol library, tweening, scripting, the works — built from the ground up in C# with Avalonia and SkiaSharp.

This isn’t a proof of concept or a weekend project. It’s a real authoring environment. Here’s where things stand:

Drawing engine — I built a vector engine based on a DCEL (doubly-connected edge list) data structure. If you’ve ever used Flash’s merge drawing mode where shapes eat into each other, that’s what this replicates — and it supports all five of Flash’s original paint modes. Paint Normal, Paint Behind, Paint Fills, Paint Selection, Paint Inside. The whole set.

Timeline — Keyframes, frame-by-frame, onion skinning. It works the way you expect it to if you’ve spent any time in Flash.

Shape tweening — Actual shape tweening with contour correspondence. Not just morphing a bounding box.

Symbol library — Graphic symbols, movie clips, the whole organizational structure Flash users rely on.

.fla / XFL import — This is the one I’m most proud of. You can open your old Flash files. As far as I know, this is the only open-source tool that functions as a full authoring environment and can actually import .fla files. Not just play them back — edit them.

Scripting — I’m building a dual-surface scripting system using Roslyn (the C# compiler). One surface for authoring-time scripts (think JSFL but way more powerful), one for runtime frame scripts (think ActionScript but in C#). I’m also planning an ActionScript-to-C# transpiler so imported .fla scripts aren’t just dead code.

Sound editor — Embedded, built on SkiaSharp waveform rendering.

This is a brief run down of everything there's so much already and I'm constantly adding more. If you'd like to support this project I've started apatreonit'd be awesome to build a dedicated team to making this even better.

## Core

1. Multi-document tabs— Open multiple projects simultaneously in docked or floating windows.
2. Auto-save— Periodically saves project progress automatically.
3. Project serialization— Save/load as folder-based or compressed .anim files using JSON + SkiaSharp.
4. Scene management— Supports multiple scenes per document.
5. Stage configuration— Customizable canvas dimensions, background color, and frame rate.

## Drawing Tools (17)

1. Selection Tool— Move, transform, and merge-on-drop objects.
2. Subselection Tool— Edit individual bezier control points and path endpoints.
3. Brush Tool— Freehand drawing with pressure sensitivity, smoothing, and five paint modes (Normal, Fills, Behind, Selection, Inside).
4. Pencil Tool— Precise pen-like stroke drawing.
5. Line Tool— Draw straight lines with optional angle-lock increments.
6. Rectangle Tool— Create rectangles with optional corner radius.
7. Circle Tool— Draw circles and ellipses.
8. Arc Tool— Create arcs with customizable start angle, end angle, and radius.
9. Eraser Tool— Erase content with adjustable brush size.
10. Free Transform Tool— Move, scale, rotate, and skew objects with interactive handles.
11. Paint Bucket Tool— Fill regions with color and sample via Alt+click.
12. Eyedropper Tool— Sample colors from any drawn element.
13. Text Tool— Create and edit text objects with live preview.
14. Hand Tool— Pan the canvas by dragging.
15. Zoom Tool— Click to zoom in or drag-to-rect zoom.
16. Lasso Tool— Free-form selection of multiple objects.
17. Camera Tool— Control a virtual camera with pan, zoom, and rotation per frame.

## Object Types

1. Shape Objects— Vector shapes with fill/stroke properties composed of VectorPath segments.
2. Text Objects— Editable text with font, size, color, and alignment options.
3. Rich Text Objects— Text rendered as glyph outlines with per-character gradient/pattern fills.
4. Bitmap Objects— Imported raster images with transform support.
5. Symbol Instances— Reusable instances of library symbols with independent transforms.

## Symbol System

1. Graphic Symbols— Reusable symbols whose timelines sync to the parent timeline.
2. MovieClip Symbols— Self-contained symbols with independently playing timelines.
3. Button Symbols— Interactive buttons with Up, Over, Down, and Hit states.
4. RichText Symbols— Specialized symbols for rich text rendering with animation.
5. Symbol Library— Centralized repository of all reusable project assets.
6. Convert to Symbol— Dialog to turn selected objects into new reusable symbols.

## Timeline & Animation

1. Multi-layer timeline— Layer organization with visibility toggling and locking.
2. Layer types— Normal, Guide, Mask, Folder, Camera, and Sound layers.
3. Layer folders— Parent-child hierarchy with expand/collapse.
4. Keyframe system— Multiple keyframes per layer at arbitrary frames.
5. Classic Tween— Smooth property interpolation between keyframes.
6. Motion Tween— Path-based animation with optional rotation alignment to path.
7. Shape Tween— Morphing between shapes using mesh/SDF-based interpolation.
8. Easing functions— Linear, Quad, Cubic, Sine, Expo, Back, Bounce, Elastic (In/Out/InOut).
9. Custom easing— Cubic-bezier control points (CSS-style).
10. Frame-by-frame animation— Individual frame labeling and navigation.
11. Motion path editing— Visualize and edit motion tween paths with bezier handles.
12. Camera animation— Animate zoom, pan, and rotation across frames on a camera layer.
13. Sound layers— Attach audio with sync modes (Event, Start, Stop, Stream) and repeat counting.
14. Sound playback— Frame-accurate audio synchronization during animation preview.
15. Guide layers— Reference content that doesn't appear in final output.
16. Mask layers— Mask content on layers below.

## Styling

1. Fill styles— Solid colors, linear gradients, radial gradients, and pattern fills.
2. Stroke styles— Configurable width, color, line cap, line join, and miter limit.
3. Alpha transparency— Per-object opacity values.
4. Color picker— HSV wheel with saturation/value square.

## Filters & Effects

1. Blur filter— Separate X/Y blur with quality settings.
2. Drop Shadow— Configurable color, angle, distance, blur, and strength.
3. Glow filter— Color and blur intensity for glow effects.
4. Bevel filter— 3D embossed effects.
5. Adjust Color— Hue, saturation, brightness, and contrast adjustments.
6. Filter chaining— Compose multiple filters per object.

## Selection & Transformation

1. Marquee selection— Rectangle selection with add/remove/intersect modes.
2. Lasso selection— Free-form multi-object selection.
3. Object transform— Move, scale, rotate, and skew individual objects.
4. Group transform— Batch transformation of selected objects.
5. Path bending— Curve manipulation on selected paths.
6. Endpoint snapping— Connected endpoint snapping when dragging path endpoints.

## Alignment & Distribution

1. Alignment— Align left, center, right, top, middle, bottom.
2. Distribution— Distribute spacing horizontally and vertically.
3. Align reference— Align to stage or to current selection.

## Undo/Redo

1. Undo/Redo— Full history with up to 100 undo steps.
2. Mergeable commands— Group similar operations (e.g., continuous dragging) into one undo step.
3. Batch commands— Group multiple operations into a single undo entry.

## Import/Export

1. XFL import— Parse and load Adobe Flash .fla files (ZIP with XML).
2. Flash edge/style mapping— Convert Flash shapes to FlashSuccessor's internal format.
3. SWF export— Compile project to Flash SWF binary format.
4. HTML5/Canvas export— Export to self-contained HTML5 with JavaScript Canvas 2D playback.
5. Shape compiler— Convert vector paths to SWF shape records.
6. Tween baking— Pre-compute animation frames at export time.
7. Bezier conversion— Cubic-to-quadratic bezier conversion for SWF compatibility.

## Scripting & Automation

1. C# scripting engine— Author scripts (JSFL-equivalent) compiled with Roslyn.
2. Frame scripts— C# code executed when the playhead enters a keyframe.
3. Document API— Script access to document properties, scenes, and library.
4. Timeline API— Script control of playback, frame navigation, and keyframe manipulation.
5. Layer API— Script access to layer properties and organization.
6. Selection API— Programmatic object selection and manipulation.
7. Element API— Script creation and property modification of display objects.
8. Graphics API— Vector drawing commands from script.
9. Library API— Script access to symbols and assets.
10. Frame API— Frame labeling and navigation from script.
11. AS3 to C# transpiler— Convert ActionScript 3 code to C# for backward compatibility.
12. AS3 lexer/parser— Full ActionScript 3 syntax analysis.
13. Script playback engine— Runtime globals for animation testing during playback.
14. Input API— Detect keyboard and mouse input during playback.
15. Output panel— Script logging and debug message display.

## Audio

1. Sound editor panel— Waveform display with zoom and selection.
2. Audio buffer editing— Cut/copy/paste with undo/redo.
3. Audio playback preview— Timeline-synced audio controls.
4. Waveform rendering— Visual waveform feedback.
5. NAudio integration— Audio I/O and playback via NAudio library.

## Rich Text & Formatting

1. Text field properties— Font family, size, color, bold, italic.
2. Text alignment— Left, center, right, justify.
3. Character properties— Letter spacing and auto-kerning.
4. Paragraph properties— Line spacing, paragraph spacing, and margins.
5. Block layout engine— Text wrapping and multi-line rendering.
6. Glyph path rendering— Convert text to vector outlines for animation.

## UI/UX

1. Docking panel system— VS-style docking with left, right, and bottom zones.
2. Floating windows— Detach any panel into a separate window.
3. Auto-hide strips— Quick-access panel strips that slide out on hover.
4. Tabbed documents— Manage multiple open projects via tabs.
5. Properties panel— View and edit selected object properties.
6. Library panel— Manage symbols and assets visually.
7. Tools panel— Tool selection and per-tool options.
8. Timeline panel— Visual keyframe scrubbing and frame navigation.
9. Zoom dropdown— Preset zoom levels including fit-to-stage and 100%.
10. Color picker panel— Integrated color selection UI control.
11. Width profile editor— Edit stroke centerline width curves visually.
 

Tags:

* flash

	575 
 

## Log in to Comment

 

IvanAlmighty2026-03-03 21:28:57

you aight white boy

 

 

Bill2026-03-03 21:28:57

best first comment

 

 

squidly2026-03-03 21:42:21

WOW this is incredible

 

 

Bill2026-03-03 21:42:21

thanks squidly!

 

 

LeviRamirez2026-03-03 21:46:45

very cool looking mr. premo!

 

 

Bill2026-03-03 21:46:45

:) thanks levi!

 

 

nicolistheguy2026-03-03 21:55:25

Lookin fresh

 

 

OatmealPecheneg2026-03-03 21:58:17

Good luck with it.In reality there is Krita and Blender can easy replace flash(paid option is ToonBoom), but they all have a confusing interface. (Even Krita, try to do 2d rig and some custom easing on keyframes to understand the pain and limitations). If you will able to do it user friendly it might be the goal.

 

 

Emizip2026-03-03 22:38:35

this is what we love to see fuck yea bill

 

 

Ceejaythe630th2026-03-03 22:47:35

I don't know what compelled me to read this entire thing, but honestly I'm pretty glad I did. At first I was thinking this was probably another thing akin to Ruffle, and thinking how futile it would be to finishing this project when that exists, but after reading through it more and really understand that this is going to be an improved Flash replication, my hopes for this project did a complete U-Turn and became really high after finishing this post.

Considering what Adobe did earlier with them trying to shut down Animate, I sincerely hope that THIS could be the Adobe killer we need, assuming everything you described here comes to fruition. I might even use this myself when this gets completed because I used to have .fla files I made before I got blocked out by Creative Cloud. You also have my utmost respect for making this compatible for the three main OSs (Windows, Mac and Linux), since that's something you don't usually see very often. With both this and Ruffle, the future for Flash is starting to look better every day.

 

 

Wriizzy2026-03-03 23:00:12

Woah, this rocks

 

 

CatMonTri2026-03-03 23:08:31

Looks and sounds really cool, Bill!I hope it works out for getting a team and making it even better.

 

 

atlaslovesedm87042026-03-03 23:25:26

SQUIDWAAARD!!! FLASH HAD A BABY!!!

 

 

midgetsausage2026-03-03 23:29:14

bill i am gonna give u a big ol kiss. compatibility with .flas is all i need

 

 

KingCrowned2026-03-03 23:29:53

Very interesting 🐛

 

 

GlitchyPSI2026-03-03 23:37:13

yo. yo? holy shit, this looks wonderful

 

 

GlitchyPSI2026-03-03 23:43:22

really intrigued by the open source part, wonder if I could help with something

 

 

NBS-Toons2026-03-04 00:02:49

That’s looks fantastic, and also it’s will having ActionScript 1.0 and ActionScript 2.0 too?

 

 

noodelz12026-03-04 00:02:49

This is really cool! I'm also trying to write an swf writer in c but it only supports a few basic tags right now.

 

 

MaxIsJoe2026-03-04 00:17:46

Excited for Linux support

 

 

KingMB-XJ2026-03-04 00:28:59

If this is free and open source, my life is legally yours.

 

 

GamerJamesey232026-03-04 00:32:00

Holy shit, thanks bill :D

 

 

JamesLee2026-03-04 00:32:22

Dope as!

 

More Results

 

			©Copyright 1995-2026 Newgrounds, Inc. All rights reserved.
			
Privacy Policy

			|
			
Terms of Use