---
title: 5.2 LTS — Blender
url: https://www.blender.org/download/releases/5-2/
site_name: hackernews_api
content_file: hackernews_api-52-lts-blender
fetched_at: '2026-07-19T19:27:41.441588'
original_url: https://www.blender.org/download/releases/5-2/
author: Blender Foundation
date: '2026-07-14'
description: Node-powered physics, online asset libraries, and fierce new features throughout with 2 years of LTS updates.
tags:
- hackernews
- trending
---

# Showcase Reel

Blender 5.2 LTS showcase reel featuring work by the Blender community.

# Watch theRecapVideo

New features overview by Jonathan Lampel and Wayne Dixon from 
CGCookie
, 
Cartesian Caramel
, 
Paul Caggegi

Blender 5.2 LTS splash artwork by Joanna Kobierska, featuring the now-extinct 
Panthera spelaea

Released July 14th, 2026

##### GEOMETRY NODES

# Music to yourNodes

Imagine driving your nodes with imported audio files, how does that sound?

TheSample Sound Frequenciesnode, coupled with the new Sound socket, brings audio-reactive animations and simulations to Geometry Nodes.

Sound files can be loaded directly into the node tree. To hear them during playback, add them to the Video Sequencer as well, and set Playback Sync to“Sync to Audio”.

Read Manual

Sample Sound Frequencies node.

Warning: contains sound. Audio-reactive animation by 
Cartesian Caramel
.

Download Demo File

##### GEOMETRY NODES

## Beveland be well

A new node enters the chat:Mesh Bevel.

The long awaited power of detailed procedural control over the edges or vertices.

Read Manual

# Cloth Dynamics

Quickly add a cloth-like behaviour to any mesh with a new node-based modifier (and a node group as well). Comes with a list of built-in controls for pinning, tearing, controlling stretch and bendiness.

# Hair Dynamics

Hair physics work similarly to cloth: the only extra requirement is having a surface object to attach hair to. The set up itself can be automated with the updated Empty hair operator.

Effectors

New node-based dynamics come with a bunch of built-in effectors for effortless gravity and/or surface collision application. In 5.2. LTS, three types of customisable effectors are available:

# Colliders

Apply a Collider modifier to transform any closed mesh into a collision object. Or go further in a fully procedural set up and use the collider effector bundle and pass into the dynamics node.

# Forces

Built-in gravity setup is available, as well as endless possibilities to build your own custom forces.

# Custom effectors

Inject fully custom behaviour into simulations using Closure and Custom Effector nodes.

Tag&Filter

Tag-based filtering system for effectors is also here to easily determine which geometries they affect. Each simulated geometry can have multiple tags for the effector to specify which tags it should affect.

## Physics:Solved

Reimagined, node based: Blender 5.2. LTS introduces a brand new procedural approach to physics for hair and cloth simulations.

The power behind experimental node-based physics lies within the new built-in XPBD Solver node.

While built-in assets contain use-case specific declarative systems around it, advanced users can customize the simulations further. Adapt existing node groups by editing constraints as needed or create a new simulation system from scratch.

Read Manual

What the community is creating with node-based physics

Vegetation interaction test render with the new#blender5.2 Alpha Cloth Dynamics node in#geometrynodesand rendered with#b3dCyclesAnimated hippo 3D model from Sketchfabpic.twitter.com/bBAeHrSO63

— Kevin Lim Wanasili (@_cgman_) 
May 20, 2026

Testing a bit more of the new cloth simulation in#geometrynodeson Blender 5.2, really cool, optimized, and above all very customizable!#b3d#clothsimpic.twitter.com/lDMtM09m4d

— Wender Silva (@wendervfx) 
June 29, 2026

Cloth sim experiment#b3d#geometrynodespic.twitter.com/p8B6fM90x9

— Cartesian Caramel (@Cartesian_C) 
June 17, 2026

all done :) i learned a lot about the new cloth solver nodes. these are exciting times!pic.twitter.com/WKuqbgl1IH

— ashlee! COMMS OPEN (@ashlee3dee) 
May 18, 2026

#GeometryNodes on Bluesky

on mstdn.social

on X

# Bundle Up

Blender 5.0 introduced the concept ofbundles, which can now be attached to geometry to carry arbitrary data across modifier and object boundaries.

Use newGet Geometry BundleandSet Geometry bundlenodes to unlock new workflows and possibilities.

Set and Get Geometry Bundle nodes.

# More Geometry Nodes

Lists

* New core data type that allows storing a sequence of arbitrary length (e.g. numbers or strings). Lots of new nodes were added to provide control.
* Create lists throughField to ListandClosure to Listnodes.
* Access lists withList LengthandGet List Itemnodes.
* Modify lists with classic Math nodes as well as newFilter ListandSort Listnodes.

Attributes

* The Capture Attribute node now supports selection.
* The newRename Attributenode renames attributes with a specific prefix.
* TheGet Attribute Namesnode outputs a list of the names of attributes in a geometry, optionally filtered by domain and data type.
* The newTransfer Attributesnode can transfer an arbitrary number of attributes from one geometry to another.
* Attributes can now be stored as 4D float vectors (note that Geometry Nodes currently only operate on 3D vectors).

Strings

* Geometry Nodes now support String fields.
* The Find in String node can now find the first occurrence from the end.
* Remove specific characters at the start or end of a string with the newTrim Stringnode.
* Reverse the character order in a string with the newReverse String.
* Switch between upper and lower case through the newSet String Case.
* StringandString to ValueBaseinput.
* Split text into a list based on a delimiter with newSplit Stringnode.

Empty Objects

* Geometry nodes modifiers can be now applied to empties. Recommended use: custom effectors for simulations, procedural effects that don’t require original geometry.

Curves

* You can now access built-in attributes to control the computation of the final curve with the newSet NURBS OrderandSet NURBS Weightnodes.

Node Tools

* Node tools inputs are remembered between operator invocations.
* Node tool inputs can now be assigned in Python.

Performance

* Internal fields pre-evaluation deduplication.
* Face corner evaluation is now avoided in some sampling nodes.
* Preferences: configure a new call stack depth limit for Geometry Nodes.

Other

* New in:Collection Childrennode for accessing all the Child Objects and Collections of a Collection as a list.
* New in:Principal Component Analysisnodes.
* 3 new building block nodes associated with Merge by Distance for expanded control over merging.
* Node group inputs: new Scene Frame default input type.
* Object sockets can now have Self Object as a default input mode.
* Access the internal attribute which tells instances what geometry to instance with the newInstance Referencenode.
* Extract a single component of a geometry or edit it in a new simpler way with theGet Geometry Componentnode.
* Closures can now be called recursively.
* Display data-block name in Viewer Node.
* Data-blocks sockets can now be compared to each other and toNone.
* Bone Info: New “Exists” output.

##### CYCLES

## CachedIn

On scenes with many image textures, the newTexture Cachesignificantly reduces memory usage and startup time by automatically generating smaller, optimized texture files that load only the tiles and resolutions needed for rendering.

* Texture Cache Off
* Texture Cache On

* Attic
* Bistro
* Junkshop

* 0
* 1000
* 2000
* 3000
* 4000
* 5000
* 6000

* Memory usage
* Unit: MB

##### CYCLES

## EasySavings

One toggle, loads of memory savings.

UnderPerformance → Texture Cache, enableAuto Generateor clickGenerate. A corresponding.txfile will be generated for each image and automatically updated whenever the image file is modified.

Memory savings and performance improvements are highly scene-dependent. Using Texture Cache comes at the cost of a small rendering performance impact and increased disk space usage.

Read Blog Post

##### CYCLES & EEVEE

# Paper-thin wall

Render physically accurate thin materials such as paper, leaves, and window sheets with the newThin Wallmode in thePrincipled BSDFnode.

When Thin Wall is enabled, the surface is treated as a slab with its layers mirrored around the base, and the thickness is assumed to be zero.

Thin Wall OFF

Thin Wall ON

Render byChristopher 3D.

This new mode provides a more accurate approximation of thin transparent and translucent materials, combining reflection and transmission for thin glass surfaces, and diffuse and translucent scattering for thin subsurface materials.

Read Manual

Thin Wall OFF

Thin Wall ON

Render byChristopher 3D.

##### COLOR MANAGEMENT

## Awesome inSpace

Organized color spaces intomenus, adding new input color spaces forApple, ARRI, Blackmagic Design, Canon, and Sonycameras, as well as support forAdobe RGB, common gamma values, and wide gamut textures.

# More Cycles & Rendering

Cycles

* Added: negative anisotropy support for Subsurface BSDF and Principled BSDF’s Subsurface component.
* The Random Walk radius scaling and anisotropy to albedo mapping adjustments for matching other renderers better.
* Added: Cast Shadows options for World.
* Geometry memory usage optimization and improved sync performance.
* Raycast Node: Access to custom attributes at intersection point.

Rendering

* New: disable option for render output saving.
* New: easy copy to selection for light/shadow linking.
* Shader nodes: newTime Node, behaves similar to its Geometry Nodes version.

##### EEVEE

# Eevolved

Blender 5.2 LTS is a major release for EEVEE, addressing long-standing usability issues from the transition to the EEVEE Next project architecture.

# What’sNew

* 2x speed-upin instance-heavy scenes
* Reduced bandingusing dithering
* Removed limit of 8 attributesper material
* Support forNormal Map Base
* AddedRaycast visibilitytoggle
* Added 1.5GB and 2GBShadow Poolsizes
* AddedCamera visibility for lights
* Plane Light Probes now support Blended materials and Shader to RGB
* Improved consistencyrendering across platforms
* AddedAnisotropic Filtering

## Behind theScreen

The newBackfaceoption underScreen Tracingcontrols how rays that intersect the back faces of visible geometry are handled.

When enabled, intersections with back faces are treated as valid hits instead of misses.

This can reduce light leaking when using screen-space global illumination, and lets you fine-tune the appearance of global illumination. It affects bothScreen Space GIandFast GI Approximation.

Read Manual

* Double Sided
* Single Sided
* Disabled (Compatibility Mode)

Both front and back faces contribute to global illumination (slider at 1.0)

Only front faces affect global illumination (slider at 0.0)

Use it for compatibility with old renders.

# WhatGot Better

* Screen Space Raytracing overhaul
* Principled BSDF sheen accounts for Coat normal
* Critical Fast GI issues fixed
* Shadow visibility fixes
* Depth of Field bokeh fixes
* Shadow artifacts fixes
* Faster and less noisy Fast GI
* Fixdd light culling at shallow FoV angles
* Light render passes consistency with Cycles
* Motion blur fixes
* Volume shader compilation fixes
* Improved Refraction BSDF light evaluation
* Improved Vector Transform normals on non-uniform scale objects
* Mix node consistency with Cycles
* Subsurface Scattering indirect lighting fixes
* See all changes in EEVEE & Viewport

##### ASSETS ♥ ONLINE

## EssentialsOn Demand

Dozens of new parametric materials, compositing effects, HDR world backgrounds, Geometry Nodes setups, and many more assets have been added to the Essentials library.

The best part? Blender isn’t any larger. These new assets are hosted online, ready for download whenever you need them.

## Make ThemYours

Watch this demo on customizing online assets by Simon fromBlender Studio

## HostYour Own

Need more? Host your own or add your favorite creator’s online asset libraries.

Smart indexing makes browsing thousands of assets a breeze.

Keep your assets up to date with a single click.

Read Manual

Add your own online repository in the new 
Asset Libraries
 preferences section.

## More inAssets

* New Asset Libraries tab in Preferences
* Per-asset Import Method
* Added “All Libraries” and “Essentials” to the Asset Libraries list in Preferences
* Organized built-in catalogs
* Better handle deleted libraries in asset shelves

##### COMPOSITOR

## New nodes,unlimitedpossibilities.

Do more in the Compositor with six new socket types supported:Matrix,Rotation,String,Object,Font, andInteger Vector.

Plus35 new nodesall-around, from string manipulation to , many of which will already be familiar to Geometry Nodes users.

See All Compositing Nodes

## Instant Looks

Whether you’re after a realisticfilmicfinish or a hand-paintedwatercolororoil paintingstyle, the new compositing assets provide a quick starting point for a wide range of looks.

Additionally, you’ll find new utility node groups that can be used as building blocks or incorporated into your own setups.

* 3D to Screen Space:transform 3D coordinates from world to normalized camera space. The inverse is available asScreen to 3D Space. Use it, for example, to drive the Sun Beams position with a 3D object.
* Transform and Project:lower level generalised variation of 3D to Screen Space that inputs from Transform and Projection to compute coordinates.
* Project with Depth:transforms 2D coordinates with their corresponding depth into a 3D vector.

## GizmosGo Further

Compositor gizmos now supportauto keying.

Transforming a gizmo will automatically insert keyframes, providing a direct way to animate compositing setups from the backdrop or theImage Editor, which nowsupports gizmostoo!

As for theviewer gizmo, it now follows the image display offset, so handles stay aligned with the backdrop as you pan and zoom.

# MORE IN COMPOSITOR

Performance & Quality

* Muchmore responsiveinteractive compositor.
* Switch nodes with a fixed condition (unconnected or directly connected to Group Input) now uselazy evaluation, saving execution time.
* TheDistance Thresholdmode of theDilate/Erodenode is now faster for relatively large sizes, with execution time independent of the size or inset inputs.
* TheGroup Outputnode now displays the total execution time of the node tree.
* Anisotropicsampling now works withTransformnodes and can be used for higher quality scaling down. Previously, it silently used Bi-Cubic sampling.

Changes

* The mask rasterizer now uses “Delaunay” tessellator by default providing robust support for overlapping regions.
* The interactive compositor now supports animation playback.
* The interactive compositor runs only when needed: fewer redundant executions, correct updates for referenced scene data, and no blocking from unrelated undo.

Additions

* File Extensioncheckbox in File Output node independent of scene render settings ‘File Extension’ checkbox.
* EEVEE only: the depth of Grease Pencil objects reflection in the viewport compositor depth pass.
* Blank Imagenode that returns a new image of a given size and constant color.
* Integer Vectorsockets are now supported and used by default where possible.
* NewFrameinput in theStabilize 2Dnode.
* Levels node gotMinimumandMaximumoutputs.
* Support forObjectsockets andActive Camera,Camera Info,Input Object,Object Infonodes from Geometry nodes.
* Objects can be now dragged and dropped from the outliner to the node editor.
* The Node Editor now displays a render region when the backdrop is enabled.
* Socket value inspection support.
* Sockets representing pixel values now show pixel units.
* New masks can now be directly created from the Mask node.
* Support forDefault Input Types.

## It’s a keeper.

TheLTSin Blender 5.2 LTS stands for “long-term support”, meaning it will get fixes for up to two years, until July 2028.

Learn More

##### GREASE PENCIL

## FillGood Ink.

Welcome the new Grease PencilDelaunay fillalgorithm. It creates exact geometry from boundary strokes, with automatic gap detection, inverse filling, zoom-independent results, and much faster performance.

Read Manual

## Ready. Set.Go Random.

Dots and Squares line materials now feature Placement settings to control the distribution of shapes along a stroke.

Strokes are now generated at render time instead of as extra geometry, significantly improving performance compared to subdividing strokes with the modifier.

## MoreOnline

Don’t forget to enable the Online Essentials Asset library: which includes 19 new Grease Pencil brushes by Blender Studio artists and Daniel Martínez Lara.

Bundled brush assets got refreshed thumbnails as well as new material controls forDots, plus settings updates forAirbrush,Ink Pen RoughandPencil soft brushes.

## Even moreGrease Pencil

* Move to Layeroperator now shows layers groups matching the layer tree structure
* Vertex Brushgot blend modes support
* UI updates (icons) for Vertex Paint mode’s toolbar
* Shift + Lnow deselects strokes that are completely selected
* NewDraw Toolsettings for picking a curve type
* Erasernow uses the last activated eraser brush
* NewFill Strokesoption lets generated strokes to carry fill material
* NewScene Unitstoggle in theSVG importerfor scale the import in the scene units
* PDF and SVG exporters now support corner types export

##### ANIMATION

## LoopMood

Introducing Playback Loop modes!

* Infinite
* Stop at End Frame
* Stop at Start Frame
* Restore Frame
* Bounce

Read Manual

## MOREANIMATION & RIGGING

Graph Editor

* Improved UI feedback when using Smooth and Cycles F-Curves modifiers
* Batch delete F-Curve modifiers (All, First, by Type)
* Ctrl+Clickon the channel visibility setting in Graph Editor now isolates that channel
* Local View to isolate selected F-Curves.
* Normalize button click in the Graph Editor now performs a normalization even if Auto Normalization is disabled

Playback

* New:Allow Prerolloption in the Playback popover for playing back frames that are before the defined playback start frame.
* New:screen.animation_pauseoperator that always pauses playback.

Pose Library

* Blender auto corrects rotation mode mismatches when a pose is applied. Closest Euler for quaternion poses, XYZ assumed for Euler-to-quaternion, unchanged when modes already match.

Workflow & Rigging

* In-Between tools now available in Object mode.
* Copy Constraintsadded to Link/Transfer Data menu (Ctrl+L).
* Auto IK reverse behaviour now works with non-connected parent bones.
* New in Dope Sheet: an operator to select keys by type (Select→Select by Type)
* New operator in Armature Edit mode: useDuplicate and Renameto duplicate selected bones and perform a search/replace on the name.
* Only Insert Availableuser preference is on by default.
* Motion paths no longer update on the current frame during auto-keyed transforms.
* NewHead/Tailslider for adjusting position along a bone when using Bone parenting.
* AdditionalSpace,Align,Length, andDeformoptions in the redo panel for adding bones.
* New operator for selecting markers left or right of the playhead with[and]hotkeys.

Fixes

* In Pose Mode, parent/child bone selection with hotkeys now works on all selected bones instead of just the active.
* Mirror bones no longer ignore transform lock settings.
* The In-Between tools now work with X-mirror in Pose Mode.
* Correct motion paths display when “Bake to Active Camera” is used with animated camera properties like Focal Length.

EXPANDYOUR BLENDER

TheBlender Extensions platformkeeps growing, with over 1100 free add-ons and themes to customize your workflows.

You can also share your own add-ons and themes!

Browse Extensions

Share Your Extensions

Three operators from the LoopTools add-on now built-in Blender 5.2 LTS.

##### MODELING

## Stay In TheLoop

To Circle,Space Edge Loops EvenlyandFlattenoperators from the popularLoop Toolsadd-on are now available as native operators.

Rewritten from scratch in C++ for improved performance, while also fixing several corner-case issues.

## MORE INMODELING

* Support forsnapping to Latticeobject
* Interpolate custom vertex datawhen merging
* Select through back-faceculled faces
* Improvedrotationalignment option inArraymodifier
* 3D Text:Fixed placementon marks (e.g. accents) over their base characters

## MORE INUVEDITING

* AddedBase Snapsupport
* Delimitseam, sharp in material inSelect Linked
* Axis options inCopy Mirrored UV coordinates
* NewSelect by Windingoperator
* Islandsupport for selectoverlap
* NewOriginal bounding box unwrapping option

# Get theartwork

Blender splash artwork source files are available for you to play with!

 Download Blend File (141 MB)

See All Demo Files

Splash artwork by 
Joanna Kobierska
, based on a model by 
Ken Barthelmey.

##### SCULPT

## Not SoPrimitive

Sculpt mode expands its toolkit: drop primitives straight into sculpts with theAdd Primitivetool.

Insert Cubes, Cones, Cylinders, UV and Icon Spheres while in Sculpt mode.

Read Manual

##### SCULPT

## Scene!Project!

Wrap surfaces onto nearby geometry with the newScene Project brush, and keep painted color intact through repeated voxel remeshing with a smoother color workflow along the way.

Read Manual

See the newScene Project brushin action in this live demo by Daniel Bystedt.

## Remesh, don’t wreck.

The voxel remesher now interpolates vertex and corner attributes, instead of taking the value of the nearest point in the original mesh.

This update provides better preservation of vertex painted meshes after repeated remeshing.

5.1

5.2 LTS

Vertex Colors preservation comparison between 5.1 and 5.2 LTS

## EVEN MORESCULPT & PAINT

Sculpt

* The Color Filter tool in Fill Mode now uses the scene “unified” colors for its operations.
* Extra user confirmation for entering Dyntopo is now removed.

Paint

* Vertex and Weight Paint received 3D brush cursor support.
* Autosave is now extended to Texture Paint.

##### VIDEO SEQUENCER

STACK, STYLE, SCOPE

The Video Sequencer mastering kit gets real in 5.2 LTS: share compositor effects as modifierassets, style titles and toggle modifiers per preview or render. All of that and more plus grading withHDRscopes.

## COMPOSITOR+ VSE

A new Compositor effect strip runs compositor node treesdirectly on the timelinewith zero, one, or two inputs, plus an effect fader on the input group.

Strip modifiers now expose inputs in the panel, driven by the node group interface like Geometry Nodes. Save compositor node trees as Strip Modifier assets to add them from the Add Modifier menu later. In the modifier extras menu, you can hide the node group selector so shared assets feel like built-in modifiers.

Last but not least: modifiers and effects can now run on the GPU, a real solution needed for heavier graphs and large blurs.

## Write inStyle

Text strips now support style presets.

Font, outline, shadows, layout, all settings in the Style panel are stored.

Three presets come built-in:

* Subtitle: classic movie subtitles.
* Main Title: big, centered text.
* Corner Title: smaller titles in the bottom-left corner.

## MakeSpace

Line Spacingcan now be adjusted in text strips relative to the font height, or inabsolute pixels.

* Subtitle
* Main Title
* Corner Title

## Now you see me, now you don’t.

Strip modifiers now have a preview visibility toggle just like object modifiers, so you can cut heavy processing from playback without touching the final export.

This also means that cached frames are kept in memory after rendering, making the next preview faster with the same result.

# PERFORMANCEBOOSTS

* Footage and compositor results now convert to sequencer color spaceon demand.
* Compositor modifiersdetect fully opaqueresults and use a faster render path instead of always assuming transparency.
* Maskinputs render faster, especially in compositor strip modifiers.

# THERE’S EVEN MORESEQUENCER

Timeline & Scene

* Stepping back a few frames while editing now feels much faster as Prefetch now loads five frames before the playhead.
* Timeline Strip thumbnails at start/end of strip are visible by default and also can be shown across the whole strip.
* Scene strips have a view layer selector, initially set to the scene’s default view layer.
* New override workbench world settings for tweaking background color for all scene strips at once.
* The Add menu shows “No other scenes” under Scene Strip when only the Edit scene exists in the file.

Strip Modifiers

* Extras menu on strip modifiers similar to object modifiers: duplicate, copy to selected strips, move to first/last in the stack.
* Linear Modifiers strip option was removed.

Python API

* New collection strip property.connectionsreturns all strips connected to a given strip.
* strips.new_movieandstrips.new_soundaccept an optionalstreamparameter to pick the video/audio stream index.
* Removed strip property.use_linear_modifiers.

## PLUS THESE

* Scopes now support HDR and wide gamut colour spaces.
* Optional scrubbing region on playback footer.
* Import adds all audio and video streams from video files.
* Render Audio operator now shows a real-time progress bar that can be cancelled.
* New: composition guides in VSE preview.
* Color strip size can now be set in raw pixels from the Strip Properties > Transform menu.
* More snap options for strip image origins (e.g. preview center).
* Unused mask inputs in compositor strip modifiers are now black and opaque instead of transparent.
* Sequencer colorspace transforms with semitransparent images now match the compositor Convert Colorspace node behavior.
* Proxy builds no longer create*.blen_tc, as timecode files functionality was removed.

##### USER INTERFACE

DETAILSMATTER

Long-term support comes with a long list of small UI improvements that make a huge difference for those who blend on daily basis.

## Do aQuick Flip!

Need portrait instead of landscape? Right-click Resolution X or Resolution Y and use newSwap Dimensionsoperator to quickly flip render dimensions.

##### OUTLINER

## ActiveFocus

Turn onScroll to Activein the Outliner to keep focus on the active object.

Elements inside collapsed Collections, and children of collapsed parents, are ignored in order to keep your Outliner tidy.

## CozySidebar

Fit more on your sidebar!

Compactmode turns the sidebar tabs into squares fitting the first two letters of the name, first two letters of each word, or even an icon.

Similar tobl_categoryfor the panel name, definebl_iconand the ID of your icon.

Additionally, you can now click-drag to switch the active tab, and the sidebar is always visible even with a single tab.

## PLUS ALL THESEUSER INTERFACEIMPROVEMENTS

General

* New Preference:Save Modified Imagesprompt
* With right-click selection, File and Asset Browsers still open a context menu when right-clicking files/assets.
* When resizing areas, aligned edges no longer move together by default: holdShiftto move them as a group.
* When Developer Extras is enabled, the property’s icon ID is shown in the tooltip.
* Circle/Lasso Select order is consistent across editors.
* Frame the active element with Mouse Button 4 by default (alongside Numpad dot/comma).

Tree View

* Auto-scroll the list when the mouse is near the edges during drag-and-drop.
* Invert sorting for root and nested list items.
* Invert the search filter to show items that don’t match.
* Navigate Tree View and Asset Shelf grid view with arrow keys.
* Numpad periodbrings the active item into view (tree and grid).

Widgets and Icons

* New text-box widget for multi-line text input.
* New “link” widget type allows to style buttons as links (blue, underline, or custom via theme)
* Pan menus and popovers with the middle mouse button, just like in other Blender areas.
* Color widgets now allow direct paste of hex values.
* Sub-panels inside popovers can be collapsed.
* Number widgets: the unit is no longer part of the selected text, a unit hint appears after the value instead.
* New icons: FILTER_FILLED, DOWNLOAD, DOWNLOAD_DONE, PACKAGE_INDIRECT.
* Set Parent Tomenu shows icons for data/object type

Node Editor

* Make Group operator avoids type conversion on multi-connected inputs and duplicate output sockets.
* Ungroup operator adds proxy input and converter nodes so behavior stays the same after ungrouping.
* NewImplicit Conversionnodes for fixed data-type conversion.
* New constant input nodes for Menu sockets and Font data-blocks in all node editors.
* Shader Editor welcomed Boolean, Integer, and Vector input nodes.
* Vector input nodes support 2D and 4D vectors.
* HoldAltto affect all selected tree interface items.
* Multiple nodes can be now resized at once.
* More renaming directly inside nodes.
* Add dynamic sockets directly on nodes.
* String input nodes update evaluation on text edit.
* Float, Integer, Vector, and Integer Vector sockets now support Pixel subtype.
* Node Wrangler merge supports Integer Math nodes.
* Linked node groups moved to a submenu in the Add menu; indirectly linked groups hidden.
* Image drop into the World shading editor now creates an Environment Texture node instead of a regular Texture node.
* Searchable AOVs in the AOV Output node.

Other Editors

* 3D Viewport: cameras now have gizmo for orthographic scale adjustment.
* 3D Viewport: Brush popover Advanced section is transformed into collapsible sub-panel.
* Image Editor: UV Grid overlay options are now visible in all modes.
* Outliner: individual shape keys display.
* Outliner: filter panel is reorganized with sub-panels (the icon is removed).
* Animation: improved readability ofMirrormenu for keys.

Preferences and Platforms

* Theme Editor: color, text style, and UI panels reorganization.
* After disablingAllow Online Access, choose to continue offline or allow internet access again.
* Linux (Wayland): key shortcuts work with non-Latin layouts when a Latin fallback layout (A–Z) is available.
* macOS 26+: new Liquid Glass application icon.

##### VIRTUAL REALITY

## GreatScout

Jump straight into your 3D scene withLocation Scouting!

Block camera vantage points and assess camera properties in VR with full 3D environment immersion.

## FullControl

The VR Controller default bindings deadzone threshold was adjusted to provide a smoother user experience.

Read Manual

# I/O

Alembic

* Import support for object visibility from Alembic archives, including animated visibility as F-Curves.
* Animated camera data now imports as F-Curves.
* Subdivision meshes keep their original coordinates on import.
* Subdivision meshes rebuild correctly when Alembic changes their structure between frames.

OpenUSD

* Color space support: import converts colors to the .blend working space; export tags prims and image textures with their color space.
* New export option to control how often USD data is flushed to disk andreduce peak memory usage on large exports.

Images

* OpenEXR: Faster writing of half-precision (FP16) EXRs.

Video & Audio Output

* Stereoscopic metadata is written to exported video for correct playback in video players.
* Panoramic camera metadata export support for full equirectangular cameras.

STL

* New option to decide which evaluation (Viewport/Render) will be used in export.

glTF: New in Import/Export

* Point Cloud support.
* Meshopt compression viaEXT_meshopt_compressionandKHR_meshopt_compression.
* Iridescence and dispersion materials viaKHR_materials_iridescenceandKHR_materials_dispersion.
* KHR primitive attributes for the official glTF primitive attribute set.
* Errors raised by glTF Hooks now stop the export.
* Performance: inline material is used when possible.
* Performance: animation export enhancement by viewport disabling.
* Nodes are now sorted by name.
* Fixed: retrieve sockets by index instead of names when they are named the same.
* Fixed: scripts reloading crash.
* Fixed: Vertex Color export for a subset of materials only use case.
* UI filter for glTF Collections.
* Fixed: crash on import multiple custom attributes.
* Animation Pointer fixes.

# BUT WAIT,THERE’SMORE

Theme

* Viewport: Added axis brightness setting.

Core

* Autosave: Programmatic triggering via new operator.
* Autosave & recovery: Unsaved image edits are now kept in backup files.
* Outliner: Remove override rules directly from the Library Overrides menu.
* Library Overrides: Geometry Nodes packed bakes are now supported on modifier stacks.

Motion Tracking

* New:“Move to Layer”operator for masks in the Movie Clip Editor (M).
* Mute footage shortcut moved toCtrl+H.
* Faster high-resolution footage playback in the Movie Clip Editor on OpenGL.
* Proxy building no longer creates *.blen_tc timecode index files.

Python API

* Geometry Nodes: modifier inputs and outputs are nowRNA propertiesinstead of custommodifier["..."]keys. Scripts that set Geometry Nodes values the old wayrequire updates.
* Expanded image-buffer API: conversion between file formats, direct pixel access, and grey-scale/RGB/RGBA support.
* Newbpy.data.all_idsiterator to loop over all data-blocks at once.
* New options forbpy.data.file_path_foreachto expand UDIM tiles, image/volume sequences, and cache files (including Cycles texture cache).
* New:gpu.init()to use the GPU in background mode (--background).
* Sculpt Mode automasking settings moved toMeshAutomaskingSettingsonPaintandBrush.
* mathutilstypes (Vector, Matrix, Color, Euler) now support slice step (e.g.vector[begin:end:step]).
* New functions to add, edit, and remove annotation strokes and points.
* bpy.data.libraries.load()now exposes linked library blend-file paths.
* New:Window.screenshotmethod to access screenshot pixel data without saving to disk.
* New:UILayout.linkandUILayout.textboxfor styled link buttons and multi-line text in panels.
* Blender reports are now exposed as a read-only list onWindowManager, with session-wide unique IDs.
* Grease Pencil: new functionslayer.layer_masks.addandlayer.layer_masks.removeto add/remove layer masks.
* Grease Pencil: newfill_idandhide_strokeproperties to strokes in the high-level python API.
* See all API changes.

Plus hundreds of bug fixes, code cleanups and refactors.See thefull list of changes.

## CREDITS

Blender is a community project.Learn more on how you cancontribute to Blender.

List of developerswho contributed to Blender 5.2 LTS and all-time contributors.

Splash artwork:Joanna Kobierska,based on a model byKen Barthelmey.Thin Wall renders byChristopher 3D. VR Location Scouting image byDaniel Bystedt.

Huge thanks to everyone involved! 🧡

The Blender team. July 14th, 2026