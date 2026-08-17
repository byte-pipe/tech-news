---
title: Development Update, August 2026 - GIMP
url: https://www.gimp.org/news/2026/08/16/dev-update-august-2026/
site_name: hnrss
content_file: hnrss-development-update-august-2026-gimp
fetched_at: '2026-08-17T11:22:24.791933'
original_url: https://www.gimp.org/news/2026/08/16/dev-update-august-2026/
date: '2026-08-17'
published_date: '2026-08-16T00:00:00+02:00'
description: Development Update, August 2026
tags:
- hackernews
- hnrss
---

## Development Update, August 2026

Previous Post

 2026-08-16
 

 by 
GIMP Team
 

For the past few months, we’ve been developing all kinds of features for
the futureGIMP3.4 release. We noticed recently that ourchangelogwas getting quite long - a good problem to have!

While there’s been a lot going on internally, it’s been a while since we made a
public progress report. So we want to share details on some of the new features
andUXimprovements that’ll be available in the first development release,GIMP3.3.2. This won’t be an exhaustive list (we have to save at least some
news for the release itself!) but hopefully it will give you some insight into
the current direction and progress ofGIMP’s development.

* New Project File Format
* MyPaint Brush: Spectral Blending
* Non-Destructive Editing
* PSDSupport Improvements
* Native File Chooser Dialogs
* User Experience and Interface Updates
* Assorted Changes and Fixes
* What’s Next

# New Project File Format¶

The big focus for maintainerJehanrecently has been developing a new project file format
forGIMP.

XCFhas beenGIMP’s primary project
format since1997, and it has served many users well. Over time however, we’ve observed
more and more limitations of the binaryXCFformat.
Among other issues, it does not easily support very large or complex projects, such as
the multi-page and animation features currently planned forGIMP3.6.

The new project file format will follow a more common “zippedXML” structure. While
the technical details are still being designed and implemented, this change will allow for
faster saving since we’ll only need to update parts of the file instead of the whole
thing each time. It will also set the stage for much desired features such as auto-saving,
which will now be much more feasible.

That said,XCFis not going away! Backwards compatibility is important to us,
and we will continue to support loading XCFs in all future versions ofGIMP.
(For instance, we’re quite proud that aXCFfile made by a small companyfor their logo in 1998 still renders the same way in the latest version ofGIMP)

However, going forward we will only add support for saving/loading new features
in the new project file format once it is finalized.

# MyPaint Brush: Spectral Blending¶

DuringGIMP3.2’s development, weupgraded to a newer versionof the MyPaint brush engine. While this brought new brushes and canvas interactions to theMyPaint Brush Tool,
one feature that was left out wasSpectral Blending.

Spectral Blending simulates the effects of blending physical pigments in digital art. For example,
blending yellow and blue will produce a green color instead of darker yellow, and blending red and
yellow will create an orange mix.

Fortunately, new contributorCassidie Groganpicked up the slack and implemented this feature.
There is now aSpectral Blendingcheckbox in the MyPaint Brush Tool Options. If checked, the new
blending method is used. You can control the strength of the blending with thePigmentslider.

Demonstration of MyPaint Spectral Blending

In addition, maintainerMichael Nattererimproved the MyPaint Brush preview code to display at their
full size instead of 48x48 pixels. This fixes an issue where the previews appeared blurry on larger screens.

# Non-Destructive Editing¶

Alx Sahas continued making updates to our non-destructive filter code. To list a few:

You can now apply filters non-destructively toLayer masks! To go along with this,
the filter popover has been redesigned byRejuto show the active filters
for both the layer and its mask, so you can interact with both on the same screen.

TheGradient Toolcan now be
used non-destructively! If you checkEditable Gradientin the Tool Options, the
gradient you create will be added to the filter stack like any other effect. You can
toggle its visibility, rearrange its position in the filter stack and delete it. You
can also edit the gradient, which will switch back to the Gradient Tool to let you
make further changes.

User interface with a live Gradient filter on the layer, and a live filter on the layer mask

Filters without dialogs (such as Invert) can now be applied non-destructively on non-raster
layers such as layer groups and link, text, and vector layers.

# PSDSupport Improvements¶

Normally we list all file format updates in a combined section, but there
has been so much work done onPSDsupport (and by so many people) that
we wanted to highlight it in more detail.

First, new contributorFrank Teklotehas been busy improving our compatibility
with PSDs. His big project for this release was creating aPSDmetadata export procedure
for TIFFs and JPEGs. This complements our existingPSDmetadata import procedure,
meaning that if you import aJPEGwith paths or aTIFFwith layers (or create one inGIMP),
that information can now be retained in the exported image.

Another great thing about Frank’s work is that as we continue to improve ourPSDcompatibility, theTIFFandJPEGexport features will automatically get those updates too!

Related to that,Jacob Boeremahas implementedPSDDescriptor import support.
Most of our currentPSDsupport has been based on the publicAdobe specification.
This document was last updated in 2019 however, and modern PSDs use a relatively undocumented
text format called Descriptors to store many features.

Now thatGIMPcan read descriptors, we’ve begun drastically improving ourPSDimport support.
To list just a few updates: text layers are now editable, a number of adjustment layers and modern
layer styles appear as theirGEGLequivalents, and solid color shapes are imported as vector layers.
This is an active area of development, including by two of our GSoC studentsAkascapeandWaris Maqbool. We hope this work will make it easier forGIMPusers to interact with existingPSDprojects!

Editable 
PSD
 text layers in 
GIMP

# Native File Chooser Dialogs¶

We have always used thefile chooser dialogprovided by theGTKGUIlibrary for people to find, load, and save files inGIMP.
While the file chooser does the job, it often works differently than the “native”
file chooser on non-GNOMEplatforms like Windows, macOS, andKDE. Additionally
there have been some changes to theUIof this dialog inGTK3, which has inspired
somestrongfeedback in our issue tracker!

Therefore,Alx Sahas begun portingGIMP’s file choosers to the “native” option provided
inGTK3. This means that when you open or save a file, you will see your platform’s
standard file chooser dialog instead of theGTKdialog (unless your platform uses
that already, in which case there will be no change!)

Example of native file chooser on macOS, by Bruno Lopes

Many of the simple dialogs have already been converted. Those with more complex additional
features will require some workflow redesigns, which we’re still developing.

# User Experience and Interface Updates¶

A lot of new and existing contributors have submitted improvements toGIMP’s user interface
and its user experience. We wanted to highlight their efforts, and encourage you all
to continue sharing your feedback on ourdesign issue tracker.

DesignerDenis Rangelovhas been hard at work updatingGIMP’sUIicons. He recreated our
layer lock icons to create a more consistent look.

He also took on the monumental task of converting all78of our cursor icons toSVG,
which will allow us to scale them for higher resolution displays without losing quality!

Original Raster Cursor

Denis’s Vector Cursor

Example of original and vector cursors

There have been reported performance issues when drawing or zooming into the canvas when the
canvas view was rotated. New contributorwoot000diagnosed the problem and created a fix.
Now the “checkerboard” transparency pattern no longer rotates when the canvas does, which significantly
boosts performance when painting or editing. They also fixed a related issue where the checkerboard
pattern would disappear when zooming into the canvas past a certain point.

Gabriele Barberoimplemented a redesign of the Search ActionUIwhich was designed byDenis Rangelov. The new layout makes the associated shortcut key more visible, and is more
consistent with the menu layouts.

Bruno Lopeshas been working to fix issues with pop-up dialog displays on macOS. Since traditionally
we have fewer macOS developers compared to other platforms, we’re really happy to see improvements for
these users!

New contributorAndreas Vukmanimproved our Pattern dock display. Now smaller patterns tile to fill
the available space, creating a consistent preview for all patterns instead of having some patterns
display with odd amounts of padding. We think it makes the dock look much nicer!

Richard Gitschlaghas updated the on-canvas text editor to allow selections when youShift+Click
in the text. It should now work similar to what you can do in a word processor like LibreOffice.

In previous versions ofGIMP, you imported or exported metadata from the Metadata Editor by selecting an option
in a dropdown.Ahmed E. Yassinhas made this process more intuitive (and more consistent with the rest ofGIMP’sUI)
by replacing the dropdown with two buttons instead.

Ondřej Míchalreviewed several portions ofGIMP’sUIand replaced many instances of theSpin Entrywidget withSpin Scale. TheSpin Entrywidget is difficult to use when the width is shrunk, so this change improves usability
in many areas of theUI.

# Assorted Changes and Fixes¶

Our four GSoC interns have been continuing their work since themidpoint update. Recently,Waris Maqbool‘s
Sharpen filter was merged intoGEGL, so it’ll be available in the nextGEGLrelease.

New contributorDimitriy Ryazantcevhas submitted several patches for improving our WindowsICO/CUR/ANIsupport.
They’ve already fixed the rendering for certain 32bitICOformats and made our loading and preview algorithms better
match the Windows specification.

Esteckahas fixed a rendering issue when applyingNDEfilters on passthrough layer groups, which made the image
look different depending on whether the group had child layers or not.

New contributorPetr Vorelfixed a bug where pressingAlt+0did not open the tenth most recent
image in your history.

Lloyd Konneker, our main Script-fu contributor, fixed a regression in third party scripts where the number range
for certain parameters wasn’t shown in theGUI.

Jacob BoeremaandAlx Sahave responded to and patched a number of security reports about potential flaws in
some of our image plug-ins.

# What’s Next¶

There’s more in-progress work that we look forward to sharing with you all soon!

There is not an official 3.3.2 development release yet, as severalroadmap itemsare still in-progress.
If you’re feelingreallyadventurous and just can’t wait, you can try our “nightly” builds. Instructions
are under theAutomatic Development Buildsheader.

In the meantime, we are planning to releaseGIMP3.2.6in the coming weeks. It is a stable release so it won’t
include many of the new features described here. However, it will have a number of important bug fixes and small
improvements. We’ll discuss these more in the 3.2.6 release news post!

Previous Post

Share this on:Mastodon|twitter|Facebook

Your Mastodon instance: