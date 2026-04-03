---
title: 'Zed for Windows: What''s Taking So Long?! — Zed''s Blog'
url: https://zed.dev/blog/windows-progress-report
site_name: lobsters
fetched_at: '2025-08-20T23:06:47.095006'
original_url: https://zed.dev/blog/windows-progress-report
date: '2025-08-20'
published_date: 08/19/2025
description: 'From the Zed Blog: An update on what the Zed for Windows team has been doing in July and August.'
tags: editors, windows
---

← Back to Blog

# Zed for Windows: What's Taking So Long?!

Lots of people have beenasking uswhen we're releasing Zed on Windows.
The Windows port started as aone-personproject, but for the past 6 weeks, we've had a group of four engineers focused on Windows full-time.
We're excited about the progress we're making and want to share an update about the work we're doing.

## Adding A Rendering Backend

When we first got Zed running on Windows, we used the same rendering backend we use on Linux, which is based on Vulkan graphics API. It was useful to be able to reuse code between platforms, but we gotreportsfromusersthat Zed didn't run on their machines due to the Vulkan dependency.

To solve this problem, wecreated a new rendering backendfor Zed based on DirectX 11. DirectX 11 is guaranteed to be available on Windows 7 or later, including Windows VMs, so now Zed should run for the vast majority of Windows users. The new backend also significantly reduces Zed's memory footprint.

Previously, we had two implementations of our GPU shaders: one MSL implementation for macOS, and one WGSL implementation for Vulkan. To use DirectX 11, we had to create a third implementation inHLSL. The process of debugging the new rendering pipeline and shaders led us down an interesting rabbit hole of its own: glyph rasterization.

## Reimplementing Glyph Rasterization in the Name of Debuggability

When developing Zed's original macOS renderer, we had relied heavily on Xcode’s Metal debugger. It lets you capture a frame in your app, step through every draw call that happened in that frame, and inspect every vertex in the scene's geometry, and every pixel in the rendered image.

On Windows, the best comparable tool for graphics debugging isRenderDoc. Unfortunately, Zed crashed on startup when run under RenderDoc, because we were relying on the Direct2D API for text rendering, and RenderDocdoes not supportapplications that use Direct2D. To work around this limitation, we decided to stop using Direct2D andswitch to rasterizing glyphs using DirectWrite instead. In the process, we fixed bugs where glyphs' boundaries were not calculated correctly, which had been causing incorrect clipping for certain characters and font sizes.

Inspecting Zed's rendering using RenderDoc. Here we're viewing the glyph atlas—a GPU texture that contains one copy of every glyph in the frame

## Flattening VRAM Usage

As more of the Zed team began to use Zed on Windows as our daily driver, some people experienced crashes due to GPU memory allocation failures. Zed seemed to be using GPU memory inefficiently in certain situations. We hadn't noticed this on macOS because recent Macs have unified memory. But on most computers running Windows and Linux, GPUs have separate memory that is more limited.

Luckily, we got help on this problem from the team behindLongbridge, who use Zed's UI framework for their own desktop app. Theydiscoveredan inefficiency in our approach to renderingpaths- combinations of lines and curves that you can use to draw arbitrary shapes. We use paths in Zed for rendering selections and text highlights.

To create smooth edges for paths, we use multi-sample antialiasing (MSAA)—we draw paths to an intermediate texture with multiple color samples per pixel, and then we copy the averaged pixel values to the final render target. Previously, we were arranging paths in our MSAA textures similarly to how we arrange glyphs in ourtexture atlas—we allocated enough space in the textures to place each visible pathwithout overlap. This sometimes resulted in us allocating a lot of very large textures.

The Longbridge folks landed aninitial fixfor this problem that removed the intermediate textures entirely, and enabled MSAA for our entire scene. Unfortunately, this ended up tanking performance on Intel GPUs, which have less efficient implementations of MSAA. But we foundanother approachto MSAA that avoided the high VRAM usage: we now draw all paths to a single color MSAA texture that's the same size as our render target, allowing the paths to overlap as they do in the final scene. We then copy directly from this texture to the render target. This change fixed the high VRAM usage, and also improved Zed's rendering performance on all platforms, even macOS.

Using RenderDoc to inspect the draw call where paths are copied from an intermediate MSAA texture into the final scene

## Updating our Auto-Updater

Graphics isn't the only thing that's different on Windows; there are also unique restrictions on file system operations. In particular, you can't overwrite an.exefile while it's running. This meant we needed a new strategy for performing auto-updates. On macOS and Linux, we simply copy the new application bundle into place, overwriting the old one, after downloading an update. But on Windows, we must perform this step whenZed.exeis not running.

Afterafewiterations, we've settled on an approach where we use a dedicated "auto update helper" binary that gets invoked on quitting or restarting Zed. The auto update helper finishes moving executables into place, and then restarts Zed if needed.

## Crash Reporting

Even crashing is different on Windows! We had to rework our crash reporting infrastructure, because on Windows, symbolicating stack traces requires a.pdbfile that is too large to ship to users as part of the installer. For users whoallow it, we now collectminidump filesto help us track and debug the crashes that users are experiencing, and symbolicate these crashes server-side after they are uploaded.

## Next Steps

There are still problems to solve before we declare Zed on Windows ready for general use. Here are the areas we're focused on in the coming weeks:

* Key bindings- Windows users have different expectations about how key bindings are displayed, and what kinds of keyboard shortcuts will be bound, depending on their keyboard layout.
* SSH Remoting- When editing files on a remote Linux machine from a Windows client, there are currently bugs related to different file-system path conventions. Also, SSH itself works differently on Windows.
* WSL- Though it's currently possible to edit files in the Linux subsystem using a local SSH connection, we're adding first-class support for WSL.
* Extensions- Zed extensions are cross-platform WASM binaries, and have access to standard file system APIs via theWebAssembly System Interface. On Windows, there are some mismatches in path conventions between the extension and host, which we need to account for.
* Performance- We'll be keeping an eye on the performance of our new graphics backend, and any other OS-specific code paths, to ensure that the Windows app is as snappy as our macOS version.

## Get Involved

* If you're interested in Zed for Windows, join our beta-testing group:zed.dev/windows.
* If you want to help out with the port, fork Zed on GitHub:github.com/zed-industries/zed.
* We're hiring!zed.dev/jobs

### Looking for a better editor?

You can try Zed today on macOS or Linux.Download now!

### We are hiring!

If you're passionate about the topics we cover on our blog, please considerjoining our teamto help us ship the future of software development.
