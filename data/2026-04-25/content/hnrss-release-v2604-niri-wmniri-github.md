---
title: Release v26.04 · niri-wm/niri · GitHub
url: https://github.com/niri-wm/niri/releases/tag/v26.04
site_name: hnrss
content_file: hnrss-release-v2604-niri-wmniri-github
fetched_at: '2026-04-25T19:42:40.475889'
original_url: https://github.com/niri-wm/niri/releases/tag/v26.04
date: '2026-04-25'
description: A scrollable-tiling Wayland compositor. Contribute to niri-wm/niri development by creating an account on GitHub.
tags:
- hackernews
- hnrss
---

niri-wm

 

/

niri

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork841
* Star23.1k

 

# v26.04

Latest

Latest

 

Compare

# Choose a tag to compare

 

## Sorry, something went wrong.

 

 Filter

 
Loading

 

## Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

## No results found

 

 
 

View all tags

 

YaLTeR

 released this

 

 25 Apr 13:50
 

 v26.04
 

8ed0da4

Niri is a scrollable-tiling Wayland compositor. Windows are arranged in columns on an infinite strip going to the right. Opening a new window never causes existing windows to resize.

As you may have noticed, niri now lives in aGitHub orgrather than my (@YaLTeR) personal account.

The primary reason was the ability to give out issue triage permissions: I'd like to give amassive thanksto@Sempyosfor triagingallof our issues and pull requests, answering many, many questions, and helping people diagnose their problems with niri.

We've also moved a few niri-adjacent projects to the GitHub org, like theawesome-nirilist of related projects maintained by@Vortrizand a newartworkrepo by@bluelindenand@HumpityDumpityDumber—two of the creators of our project logo. In the artwork repo, you can find a badge and severalwallpapers, including two stunning 3D works created by@Duncan-Rosein Blender:

pool

cut

The main niri repo also flew past 20,000 stars in February! 🌟 Thanks everyone for support.

Note

Packagers:

* our minimum supported Rust version is now 1.85.
* niri.serviceno longer hardcodes/usr/bin/in the niri binary path (thanks@Axlefublr).
* @markK24restructured the dinit service files:3bfa4a7

Now with introductions out of the way, here are the improvements from the last release.

## Blur

It's here. The most requested niri feature by far. Our highest upvoted issue on GitHub. After tireless fork maintenance by@visualglitch91and@Naxdy, blur is in mainline niri for everyone to use!

Windows and layer-shell components can request blur through theext-background-effectWayland protocol with no extra niri configuration. Many already do:

* Dank Material Shellv1.4.5: enable background blurin settings
* Noctaliashell: enable in settings andsee docs
* Vicinaelauncher
* footterminal v1.26: setblur=truein colors config
* kittyterminal v0.46.2: setbackground_blur 1
* Ghosttyterminal: will have support in v1.4

Toolkits:

* Quickshell: will have support in v0.3
* winit: will have support in v0.31

For apps that don't supportext-background-effectyet, you can enable blur through the niri config:

// Enable blur behind the Alacritty terminal.

window-rule
 {

 match
 
app-id=
"^Alacritty$"

 background-effect
 {

 blur
 
true

 }
}

// Enable blur behind the fuzzel launcher.

layer-rule
 {

 match
 
namespace=
"^launcher$"

 background-effect
 {

 blur
 
true

 }
}

Keep in mind that niri-configured blur needs the rightgeometry-corner-radius, and it won't work with complex surface shapes. See theWindow Effectswiki page for details.

Have I seen this screenshot before?..

We have both normal blur and xray blur that always shows the wallpaper. Xray blur is the default because it's much more efficient: niri computes the blurred wallpaper once, and then reuses it as a static image, which is extremely cheap. Only if the wallpaper changes, the blur is recomputed (so an animated background will shrink the efficiency gains).

If you prefer non-xray (normal) blur, you can enable it with a window/layer rule. For example, you can set it on top and overlay layers (that usually overlap other content), via the newlayermatcher:

// Make top and overlay layers use the regular blur (if enabled),

// while bottom and background layers keep using the efficient xray blur.

layer-rule
 {

 match
 
layer=
"top"

 match
 
layer=
"overlay"

 background-effect
 {

 xray
 
false

 }
}

So, if blur is so good, where's blur 2? Err, I mean, why did it take so long to add?

In short, background blur turned out to be a massive undertaking. Not because of the blur algorithm itself (by the way, if you want to learn about different blurs, including the widely used Dual Kawase, I highly recommendthis blog post), but because window background effects in general required a lot of thinking and additions to the code, especially to make them as efficient as possible. This is one of the most complex niri features thus far.

Xray and non-xray effects are also pretty much twoentirely separateand very different beasts, code-wise. Non-xray reads back the just-rendered pixels in the middle of a frame, blurs them, then continues drawing the frame. This required extensive refactors of Smithay's rendering architecture (big thanks to@Drakulix!). Xray on the other hand requires threading the window positions all throughout the rendering code to draw the right cut-out of the background.

But it gets worse: we have ourOverview. It was quite a challenge figuring out how to support xray blur in the overview, while maintaining the property that it is never re-rendered.

niri-xray-blur-offscreens.mp4

I also had to get both of them working with all other niri features, likeblocking out from screencasts. When the window itself is blocked out that's easy, but what if somethingin the background layer, inside the blur, is blocked out? An unusual case for sure, but hardly a good exclude if your sensitive data gets accidentally leaked.

niri-xray-blur-blocked-out.mp4

By the way, I made it so xray can be used on its own, without the blur. As well as the noise and saturation effects (normally for reducing blur color banding and bumping the vividness). For example:

window-rule
 {

 match
 
app-id=
"Alacritty"

 
// Xray without the blur!

 background-effect
 {

 xray
 
true

 }
}

One more thing you can do starting from this release is to configure niri to apply transparency and background effects to pop-up menus, using the newpopupsblock inwindoworlayerrules.

// Blur the background behind pop-up menus in Loupe.

window-rule
 {

 match
 
app-id=
"Loupe"

 popups
 {
 
// Matches the default libadwaita pop-up corner radius.

 geometry-corner-radius
 
15

 
// Note: it'll look better to set background opacity

 
// through your GTK theme CSS and not here.

 
// This is just an example that makes it look obvious.

 opacity
 
0.5

 background-effect
 {

 blur
 
true

 }
 }
}

Keep in mind that pop-up rules tend to bump even more into problems with application behavior and surface shapes. For example, web apps or Electron don't use Wayland pop-ups at all; they're entirely emulated inside the client—niri cannot do anything with them.

Shape-wise, in GTK 4, pop-ups withhas-arrow=truewon't look right because they aren't rounded rectangles. Thankfully, clients implementingext-background-effectcan shape their blurin any sort of elaborate pattern.

Well, enough about blur, we've got more interesting things to cover!

Credit: Houl Floof

## Optional includes

Pretty much right after I addedconfig includeslast release (before I merged them even), people started requesting optional includes—that can be absent without failing config loading. Some use-cases are being able to change parts of an immutable niri config on NixOS, or having local/private overrides for parts of the config.

I pushed back for a time because I think some of those problems should be solved elsewhere, rather than requiring every program with includes to support optional. However, the added code complexity was rather low, so I eventually went ahead and accepted@johnrichardrinehart's implementation.

Starting from this release, you can make an include optional by settingoptional=true:

// Won't fail if this file doesn't exist.

include
 
optional=
true
 
"optional-config.kdl"

// Regular include, will fail if the file doesn't exist.

include
 
"required-config.kdl"

When an optional include file is missing, niri will emit a warning in the logs on every config reload. This reminds you that the file is missing while still loading the config successfully.

The optional file is still watched for changes, so if you create it later, the config will automatically reload and apply the new settings. Finally,optional=trueonly affects whether a missing file causes an error, so if the file exists but contains invalid syntax or other errors, those errors will still cause a parsing failure.

While we're talking about includes: they now expand paths starting with~to the home directory, so~/file.kdlwill expand to/home/user/file.kdl. Thanks to@HigherOrderLogicand@BennyDeeDevfor prototype implementations of this feature.

## Pointer warping while scrolling

Last release, I made dragging windows horizontally by their titlebars scroll the view left and right. This made mouse-only navigation much more convenient, but I still felt that something was missing.

This release makes the pointer warp from one side of the screen to the other during view scrolling gestures, similarly to Blender. It makes scrolling through several windows natural and convenient, even when you start right next to the monitor edge.

niri-pointer-warp.mp4

## Screencasting features

Earlier in the release cycle, I spent some time improving various aspects of our screencasting support. In niri, you can screencast through xdg-desktop-portal-gnome via PipeWire (the recommended approach), or throughwlr-screencopy(mainly intended for tools such aswf-recorder). Both of these have seen improvements.

### Pointer in window screencasts

When sharing the screen, you generally want to include the cursor in the video stream. In PipeWire, you can either do the simple thing and just draw the cursor directly inside the video frames, or you can attach it as a separate framemetadata. In this mode, the video stream itself doesn't contain the cursor, instead, the compositor sends a separate buffer with the cursor icon and coordinates. The consuming application itself (such asOBS, or your browser in a video meeting) then has to draw the cursor on top.

This allows the consuming application to control the cursor visibility. You might have seen this toggle in OBS; it can work thanks to the metadata cursor mode:

Ever since I implemented PipeWire screencasting in niriabout a month into development, it's been using the embedded cursor mode for simplicity. I rendered the cursor for monitor streams and hid it for window streams, and this mostly did what you wanted (and the cursor toggle in OBS didn't work).

Doing it properly has always been in the back of my mind though. I was most missing cursor in window streams because I pretty much always use the window target when screensharing in meetings.

Well, in the summer of last year,@abmantistook up the task. The road was quite bumpy though: they hit and managed to debug amemory corruption issue in PipeWire(that other compositors haven't hit due to more eagerly overriding unchanged data every frame). The bug was thankfully promptly fixed by a PipeWire developer.

It took me several more months to get to the PR (busy with uni and other things as usual), then some heavy refactoring to make it work correctly and iron out all the edge cases, and now niri does screencasting with cursor metadata!

The implementation is quite comprehensive. It works in both monitor and window capture modes and draws the cursor along with its drag-and-drop icon (if any). In window capture mode, the cursor is shownonlywhen it's targeting the window or any of its pop-ups. So, for example, if you cast a window fully covered by another window, and move your mouse on top of that, the screencast of the window belowwill notshow the cursor.

niri-cursor-cast-metadata.mp4

Metadata cursor is also intended to support an optimization where if you move your mouse over an otherwise unchanging screen, the compositor can skip sending these stationary video frames and only update the cursor position. Unfortunately, the OBS PipeWire code doesn't quite allow for this code path yet, so I couldn't do this for the time being.

While working on this, I also found several disagreements between the intended meaning in PipeWire (indicated through comments in header files) and what the code was doing in consumers such aslibwebrtc(used in all browsers). This is unfortunate since compositors have to not only work around these problems, but also keep the workarounds forever, as they can't tell how old is the library on the other side of the PipeWire stream. It would be good to have high-quality PipeWire producer and consumer examples for these more complex scenarios, that get all the small details right.

Anyhow! Metadata cursor is here and works with everything I tested. As a bonus, I added pointer capture to windowscreenshotswith a new flag on the action:screenshot-window show-pointer=true.

### Delayed start for dynamic cast target

Dynamic cast targetis a niri feature that lets you instantly switch what you're screencasting with a keybind. I personally use it all the time because it's very convenient to toggle screencasting between different windows without going through some video conferencing screen sharing UI or having to cast the entire monitor.

You start a dynamic cast by selecting a special "niri Dynamic Cast Target" in the window picker. The dynamic cast always starts as a blank video stream to avoid sharing something sensitive by mistake.

Before this release, the dynamic cast literally started as a 1×1 black pixel video stream. This worked just fine in every app... except, apparently, everyone's favoriteMicrosoft Teams. So, in this release I changed the dynamic cast to delay starting the video stream until the first dynamic target is selected. As far as the screen sharing programs are concerned, you're just taking a bit longer to pick what to screen share. No more slightly odd brief 1×1 video.

### Cast IPC

It can be useful to know if there's an ongoing screencast. For example, desktop bars may want to show a screen recording indicator to alert you of any unintended screen capture.

For PipeWire, a bar could enumerate all ongoing video streams and try to figure out which ones are screencasts, but it's error prone, and for wlr-screencopy there's no way at all to tell from outside the compositor.

So in this release, I added screencast IPC to niri. You can see currently active screencasts withniri msg casts. Desktop components can subscribe to the nirievent streamand listen for the newcast events.

TheCastobject provides various bits of information: kind (PipeWire or wlr-screencopy), current target (output, window), whether the cast is active. PipeWire screencasts provide their node ID which you can use to find out the consumer, while wlr-screencopy screencasts provide the client process ID for the same purpose.

DankMaterialShellalready shows a screencasting indicator using the niri IPC:

And if you need more, it's easy to make a plugin that shows all exposed information.

While working on this, I found that I had a bunch of duplicate screencast sources in OBS.

Keep in mind that for wlr-screencopy, there's no robust way to tell apart different screencasts and screenshots, so I had to come up with some heuristics. Notably, xdg-desktop-portal-wlr always uses and keeps alive a single wlr-screencopy manager object, so there's no way to tell when a screencast has stopped short of using a timeout for when the last frame was requested.

All of these wlr-screencopy problems are fixed in the newext-image-copy-captureprotocol, but we don't have it in niri just yet (and some clients will remain legacy anyway).

Also, with cast IPC providing IDs for screencasts, we can add actions to manipulate them. The newniri msg action stop-cast --session-id <ID>will force-stop a PipeWire screencast (wlr-screencopy ones cannot currently be stopped through IPC).

niri-stop-cast.mp4

### Miscellaneous fixes

Some more random things I fixed in this release:

* Copying with damage would always include the cursor even if the wlr-screencopy client said not to; now this is honored.
* Fixed behavior when a wlr-screencopy client requests multiple frame copies with damage at once. I don't know of any client that does this but now it should work.
* Fixed the niri wlr-screencopy data never getting freed in some cases, like when the client was killed.
* Reduced the default PipeWire screencast buffer count from 16 to 8.
* @kriiveworked around a use-after-free bug in pipewire-rs by reordering some struct fields in niri.
* Fixed wrong rendering z-order that could appear for one frame when switching the dynamic cast target to a window.

## Animation improvements

In winter, I felt like doing a bit of an "animation detox" and spent several weeks with some niri animations disabled. (If you're curious, I turn off window open, close, resize and movement animations, and leave horizontal view movement since it helps with spatial awareness.) While doing this, I noticed some jank in the unfullscreen/unmaximize animation.

You canconfigure individual animationsdifferently in niri. However, in several cases, two animations are meant to run together and match exactly. In those cases, niri willsynchronizethe animations—for example, it can run some animation that is otherwise disabled.

In particular, a window resize animation is synchronized with the horizontal view movement animation that it causes. This way, resizing a window next to the right edge of the monitor will "grow" it to the left instead of an awkward combination of growing to the right and moving back in-view.

The problem that I found is that while fullscreen/maximize correctly synchronized the view movement, unfullscreen/unmaximize didn't. So the window would unmaximize instantly (window-resize is off) but slowly scroll back into position.

This is now fixed:

synchronized.unmaximize.anim.mp4

Another animation issue that's been bugging me for a while was fairly specific. When you "drag out" a maximized window, it will automatically unmaximize. If it was floating before you maximized it, it will also automatically return to floating. And when you did this specific action—drag a window to unmaximize into floating—it would skip the horizontal view movement animation of other tiled windows on the same workspace.

unmaximize.view.scroll.anim.mp4

This was a tricky issue to find because it was at an intersection with another feature: left-right workspace scrolling if you drag-and-drop near a monitor edge. If this drag-and-drop scrolled the view, the view needs to resnap to a window edge, but if it never scrolled the view, then the view should remain exactly as it was, no resnapping. It turned out that this drag-and-drop finalization code ran right after the horizontal view animation was started, and since no scrolling had occurred, it immediately skipped the animation.

Thefixwas to take a possibly running animation into account explicitly (and add a test of course).

Finally, there was always some weirdness when "dragging out" the leftmost column on a workspace, specifically when it wasn't focused. (You can easily hit this when moving windows from the overview.)

"Dragging out" in this case preserves the view position, which is intended: the focused window (not the one we're dragging out) always remains fixed in the view, regardless of what's happening around it. But dropping the window back would awkwardly put it on the right side instead of where it previously was.

drag.leftmost.column.mp4

After carefully reading through the relevant code (which is among the earliest code I wrote in niri since this is a fundamental windowing operation, but also changed shape many times over development), I noticed that some operation ordering wasn't quite logical when inserting the leftmost column into a workspace, and was able to refactor things a bit to make it work right.

And the last small animation fix was to prevent the slowdown/speedup setting affecting the duration the config error notification is visible on screen.

## IME in pop-ups

We fixed (or rather worked around) one long-standing annoying problem: GTK 4 pop-ups with input fields didn't work if you were running an IME like Fcitx5. Effectively, you couldn't open any pop-up with a text entry.

The underlying issue is that Smithay's abstractions don't allow for multiple input grabs at once. Pop-ups generally take a pointer and keyboard grab (notice how when a pop-up is open, moving the mouse over other windows doesn't trigger any hover effects in them), but an IME also works through a keyboard grab in order to handle key events. These two conflicted with each other in niri, so it dropped the pop-up grab, which closed the pop-up immediately upon opening it.

A proper fix would be rearchitecting this part of Smithay, but until then, I loosened some checks, allowing this grab sequence to work. Finally, IME users are able to rename files in Nautilus.

## Escape to cancel drag-and-drop

PressingEscapeduring drag-and-drop will now cancel the operation. I wanted to add this for a while since it's a common gesture, so I did as soon as Smithay recently merged the necessary code.

## Input device improvements

We've had an assortment of improvements to input devices:

* Fixed compounding slowdown over time when using a high Hz mouse with cursorhide-after-inactive-msor an idle monitoring daemon.
* If you have libwayland-server v1.23 or later, niri will increase its Wayland buffer size, so moving a high Hz mouse over non-responsive windows will no longer quickly crash them.
* @qqwaadded themap-to-focused-outputtablet optionthat makes the tablet target the currently focused output rather than some single configured output.
* @skrmcfixed an issue where putting the cursor at the topmost pixels on a workspace wouldn't always target a maximized window under the cursor.
* Fixed Alt-Tab reacting to mouse input before it's visible.
* @ArijanJmade trackball (on-button-down) scrolling work in the overview.
* @mgabor3141made the Num Lock state preserve acrossloading a custom .xkb file keymap.
* @Atan-D-RP4fixed niri being unable to use any input devices when starting from a different TTY via tmux.
* Enabled the loading oflibinput plugins.

## GPU profiling

One of my main blockers for blur in niri has always been the lack of GPU profiling integration in Smithay. Blur is a heavy operation, and I wanted to see its performance behavior to make good decisions about the code architecture.

In Smithay and niri we useTracy, a highly capable frame profiler. It supports showing GPU zones, however collecting timestamps from the GPU requires a fair bit of integration work: you need to submit timestamp queries along with your GPU work, then keep a queue of in-flight queries, periodically collect the values of completed queries and upload them to Tracy. At the end of 2025, I sat down anddid the necessary workin Smithay which enables both profiling GPU operations done by Smithay itself, and for compositors to annotate their own GPU operations.

Here's an example Tracy recording with GPU zones shown in red at the top, and CPU zones in teal below.

On this recording niri draws a single frame, first to the DRM buffer (goes to the monitor), then, separately, to a buffer for an ongoing PipeWire screencast. You can see the screencast rendering on the GPU in parallel with some CPU work, then as soon as it's done, the CPU is notified, and sends the finished frame over PipeWire to the screencast consumer.

On multi-GPU systems (common on laptops if you have an integrated + discrete GPU), Tracy will show multiple GPU tracks:

On this frame profile, I have a laptop with the main screen (connected to the iGPU) and an external screen (connected to the dGPU). You can see the main GPU rendering both screens (niri renders everything on the main GPU), then the external screen contents are copied over to the dGPU where they are rendered in a single texture draw.

This profiling integration allowed me to verify that blur isn't slower than expected (actually it turned out to run faster than I thought it would). Also, it's now much easier to diagnose dropped frames caused by GPU rendering stalls.

## Rendering optimizations

In Smithay and, by extension, niri, rendering works by first constructing arender list, aVecof render elements that describe exactly how the final scene is laid out on screen. This render list is then processed by the damage tracker to cut out all invisible and unchanged regions, and then, only if anything needs to be redrawn, the damage tracker hands the elements over to the GPU—just the ones that changed. Compositors try hard to minimize unnecessary redrawing and waking up the GPU to conserve battery.

When designing the rendering architecture in niri, I implemented everything through iterators. Functions likeWorkspace::render()would return a type like-> impl Iterator<Item = SomeRenderElement>, aggregating and processing render elements from their constituent parts (like individual windows on a workspace). At the top level,Niri::render()would collect from such an iterator into aVecof render elements.

Generally, this code structure avoids intermediate allocations (returning an iterator like this compiles down to a state machine that creates all items on-demand as they are pulled by the caller). It also avoids doing unnecessary work since the caller can cut the iterator short at any time if it doesn't need some of the items.

However, as you may know if you have dealt with complex iterators in Rust, there's a whole range of annoyances that come with this kind of structure. For a start, it's hard to write any logic, like conditionals, around returning iterators. Since this-> impl Iteratormust be a single type, you cannot just write:

if
 condition 
{

 
return
 one_iterator
;

}
 
else
 
{

 
return
 another_iterator
;

}

It won't compile as these are two different types. You have to come up with workarounds.

Then, in many cases in niri, the returned iterator would borrow from&self, leading to complex lifetimes. I actually designed for this from the start, withrender()functions intentionally borrowing a shared&self, preceded by a separateupdate(&mut self)step. However, rendering also needs an exclusive&mut Renderer, and this thing did cause annoying borrowing issues every now and then.

In several cases, the borrowing is not practical to work around, so I had to fall back to returning aVecfrom intermediate functions, which is a short-lived temporary allocation that's immediately freed. Especially unfortunate is that the iterator approach doesn't really work across crate boundaries, so Smithay's surface rendering function returns aVec—and niri calls itper Wayland window and pop-up, causing many temporary allocations during rendering.

For a few months, thoughts brewed in my head on how to rearchitect this. Finally, in December, I felt like I had a solid, working idea, and attempted the refactor.

The idea was to replace pull-based functions with push-based ones. Instead of returning-> impl Iterator<Element>, all rendering functions would accept apush: &mut dyn FnMut(Element)closure, and call it to push their render elements to the list. At the top level, push would simplyfinal_vec.push(element), and intermediate rendering functions would forward this push function down. (This design is not unlike howrender tree constructionworks in GTK 4.)

The refactor honestly succeeded beyond my expectations. It solved pretty much all problems I've had. Conditionals become trivial and just work. No complex iterator chains. Functions can still do their logic by wrapping the parent'spushin their own closure. There's no borrowing. All temporaryVecs gone. As for cutting iterators short, we didn't actually need it in niri.

It also sped up the render list construction by 2-3× on my main machines (I didn't expect that):

And, wildly enough, by 8× on my ancient Eee PC! Render list construction does not include the rendering time, which still dominates the frame duration. But it happens much more frequently, even when no actual rendering is needed afterwards, so the improvement is very welcome.

I measured performance and memory use with Tracy. Here's an example profile showing old and new render list construction side-by-side:

The orange line at the bottom tracks the allocated memory. You can see that the previous rendering allocates and drops many times, while the only allocations in the new rendering are pretty much growing the output vector (the steps are the vector capacity increasing as more elements are added—it should be possible to reuse the same vector to get rid of even those, but I haven't got around to it yet).

If you're curious for a more detailed motivation and want to see the diff,which somehow turned out to be negative, seethe pull request.

## Old laptop support

There's been a long-standing niri issue where screenshots (both built-in and through wlr-screencopy tools) didn't work on old Intel laptops with a weird error. Last week,@xdagizfinally dug in andfigured it out: a wrong OpenGL enum value in Smithay.

Also, I did some small optimizations to the niri shaders and managed to fit our resize and clip into the (extremely limited) GPU of an ancient ASUS Eee PC that I have lying around, meaning that window resize animations and compositor-rounded corners now work there (can't say they are particularly smooth though).

Both things combine to show you the following image:

## Other improvements in this release

* @cmeisslfixed a VRAM leak that occurred on some systems after closing certain apps.
* @sodibooand@HigherOrderLogicimplemented theext-foreign-toplevel-listprotocol which will help Quickshell and other shells associate Wayland window objects with niri IPC window IDs.
* @Ind-Emade it so the error message for a duplicate bind in the config also shows the first definition of the same bind.
* Mod+LMB window dragging is now indicated with a grabbing cursor (thanks@kchibisov).
* @zimwardadded the--pathargument toniri msg action load-config-filewhich lets you switch to a different niri config at runtime.
* @Fingeladded DMA-BUF support to nested niri, which makes hardware acceleration work there again, now that Mesa's wl_drm is deprecated and phased out.
* Removed padding that niri added to layer-shell pop-ups near monitor edges, as it was more confusing than helpful.
* Thedefault confignow binds Mod+M tomaximize-window-to-edgesand Mod+Shift+R toswitch-preset-column-width-back.
* Added theforce-disable-connectors-on-resumedebug flag to force a screen blank on TTY switch into niri or waking up from suspend, which can help on some rare hardware configurations.
* Putting a window into windowed fullscreen now correctly squares the corners.
* Fixed constant screen repainting while the overview is open.
* Slightly corrected therelative-to=workspace-viewgradient border rendering for interactively dragged windows.
* @jakobhellermannprettified diaeresis shortcut rendering in the Important Hotkeys dialog.
* Fixed the description ofexpel-window-from-columninniri msg actionto say that it expels the bottom window (this has been the behavior for a few niri releases already).
* Fixed several panics possible if a client tries to use a recently removed output.
* Fixed broken rendering whenclip-to-geometryis applied to a client that attachesy_invertbuffers.
* @tobhefixed building on OpenBSD.
* @titaniumtravelermade nested niri set its windowapp-id.
* @DuskyElfchanged niri to re-evaluate theignore-drm-devicedebug settings when a new GPU is plugged in, allowing to use/dev/dri/by-path/symlinks there.
* Updated Smithay:Improved automatic GPU selection on some devices such as ARM Macs. Asahi and Pinephone should now run niri out of the box with no manualrender-drm-deviceconfiguration necessary.Improved the behavior of some layer-shell clients likewl_shimejiby not considering subsurfaces for layer surface positioning.Improved support for docks that cause monitor EDID to be loaded late.Made screenshots and screencasts work on older Intel systems.Fixed stale outputs being left behind when some USB-C docks are disconnected while the computer is suspended.Fixed azxdg_exporter_v2panic with some clients.Fixed a memory leak when clients using the clipboard protocols don't destroy them explicitly.Fixed a panic when the client tries to set unrecognized text-input content hint and purpose (this started to happen in the GTK 4.23 development release).Various fixes to drag-and-drop, IME text input and multi-GPU, as well as various performance improvements.
* Improved automatic GPU selection on some devices such as ARM Macs. Asahi and Pinephone should now run niri out of the box with no manualrender-drm-deviceconfiguration necessary.
* Improved the behavior of some layer-shell clients likewl_shimejiby not considering subsurfaces for layer surface positioning.
* Improved support for docks that cause monitor EDID to be loaded late.
* Made screenshots and screencasts work on older Intel systems.
* Fixed stale outputs being left behind when some USB-C docks are disconnected while the computer is suspended.
* Fixed azxdg_exporter_v2panic with some clients.
* Fixed a memory leak when clients using the clipboard protocols don't destroy them explicitly.
* Fixed a panic when the client tries to set unrecognized text-input content hint and purpose (this started to happen in the GTK 4.23 development release).
* Various fixes to drag-and-drop, IME text input and multi-GPU, as well as various performance improvements.

## Funding

I work on niri in the spare time that I have from my university studies. If you like what I do, you can support my work onGitHub Sponsors. Big thanks to all current and past sponsors!

 

### Contributors

 abmantis, YaLTeR, and 30 other contributors
 

 

Assets

3

 

 
Loading

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
👍

104

 
Atemo-C, Fingel, Giftzwerg02, ClixTW, nicthegarden, Creator54, Eurekaimer, bjamex, MintyDoggo, Noticxs, and 94 more reacted with thumbs up emoji

 
😄

17

 
Atemo-C, Giftzwerg02, Creator54, Kasui92, jialuo999, SOV710, bdsqqq, neverlink, Tal0na, primalmotion, and 7 more reacted with laugh emoji

 
🎉

155

 
Kotujin, anatolij1923, avesst, ajtribick, VolodymyrVorona, pgils, a-piece-of-snake, nfoert, rockneurotiko, yjydist, and 145 more reacted with hooray emoji

 
❤️

85

 
Diddy42, omasanori, cppHusky, Vortriz, markstos, epic9491, Atemo-C, Giftzwerg02, njkevlani, Yaasosu, and 75 more reacted with heart emoji

 
🚀

33

 
James-Kni, Atemo-C, NahojPh, Giftzwerg02, jialuo999, gavlig, SOV710, bdsqqq, felipeadeildo, anwar, and 23 more reacted with rocket emoji

 
👀

9

 
Atemo-C, Giftzwerg02, jialuo999, neverlink, primalmotion, Tal0na, thenil3sh, 1Step621, and TeddyHuang-00 reacted with eyes emoji

 

All reactions

 
243 people reacted

 8
 

 

Join discussion