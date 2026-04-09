---
title: 'Preserving code that shaped generations: Zork I, II, and III go Open Source'
url: https://opensource.microsoft.com/blog/2025/11/20/preserving-code-that-shaped-generations-zork-i-ii-and-iii-go-open-source
site_name: hackernews_api
fetched_at: '2025-11-21T11:06:58.640733'
original_url: https://opensource.microsoft.com/blog/2025/11/20/preserving-code-that-shaped-generations-zork-i-ii-and-iii-go-open-source
author: stacey haffner, scott hanselman
date: '2025-11-20'
description: Microsoft’s Open Source Programs Office (OSPO), Team Xbox, and Activision are making Zork I, Zork II, and Zork III available under the MIT License.
tags:
- hackernews
- trending
---

## Preserving code that shaped generations: Zork I, II, and III go Open Source

pageName

Blog home

pageLink

/en-us/opensource/blog

share-modal-id

modal

theme

night

* A game that changed how we think about play
* Preserving a piece of history
* Running Zork I-III today
* Continuing the journey

Search the blog

Share

share-modal-id

modal-1

/en-us/opensource/blog/fragments/modal-dialog

READ TIME

6 min

WRITTEN BY

/en-us/opensource/blog/author/stacey-haffner

/en-us/opensource/blog/author/scott-hanselman

Today, we’re preserving a cornerstone of gaming history that is near and dear to our hearts. Together, Microsoft’s Open Source Programs Office (OSPO), Team Xbox, and Activision are making
Zork I
,
Zork II
, and
Zork III
 available under the MIT License. Our goal is simple: to place historically important code in the hands of students, teachers, and developers so they can study it, learn from it, and, perhaps most importantly, play it.

Find Zork 1 GitHub repository here

New Tab

appearance

button--primary

shape

circle

### A game that changed how we think about play

WhenZorkarrived, it didn’t just ask players to win; it asked them to imagine. There were no graphics, no joystick, and no soundtrack, only words on a screen and the player’s curiosity. Yet those words built worlds more vivid than most games of their time. What made that possible wasn’t just clever writing, it was clever engineering.

Beneath that world of words was something quietly revolutionary: the Z-Machine, a custom-built engine. Z-Machine is a specification of a virtual machine, and now there are many Z-Machine interpreters that we used today that are software implementations of that VM. The original mainframe version ofZorkwas too large for early home computers to handle, so the team at Infocom made a practical choice. They split it into three games titledZork I,Zork II, andZork III, all powered by the same underlying system. This also meant that instead of rebuilding the game for each platform, they could use the Z-Machine to interpret the same story files on any computer. That design madeZorkone of the first games to be truly cross-platform, appearing on Apple IIs, IBM PCs, and more.

media-modal-id

modal-2

### Preserving a piece of history

Game preservation takes many forms, and it’s important to consider research as well as play. The Zork source code deserves to be preserved and studied. Rather than creating new repositories, we’re contributing directly to history. In collaboration with Jason Scott, the well-known digital archivist ofInternet Archivefame, we have officially submitted upstream pull requests to the historical source repositories ofZork I,Zork II, andZork III. Those pull requests add a clear MIT LICENSE and formally document the open-source grant.

Each repository includes:

* Source code forZork I,Zork II, andZork III.
* Accompanying documentation where available, such as build notes, comments, and historically relevant files.
* Clear licensing and attribution, via MIT LICENSE.txt and repository-level metadata.

This release focuses purely on the code itself. It does not include commercial packaging or marketing materials, and it does not grant rights to any trademarks or brands, which remain with their respective owners. All assets outside the scope of these titles’ source code are intentionally excluded to preserve historical accuracy.

### Running Zork I-III today

More than forty years later,Zorkis still alive and easier than ever to play. The games remain commercially available viaThe Zork Anthologyon Good Old Games. For those who enjoy a more hands on approach, the games can be compiled and run locally usingZILF, the modern Z-Machine interpreter created by Tara McGrew. ZILF compiles ZIL files into Z3s that can be run withTara’s own ZLRwhich is a sentence I never thought I’d write, much less say out loud! There are a huge number of wonderful Z-machine runners across all platforms for you to explore.

Here's how to get started running Zork locally with ZILF. From the command line, compile and assembly the zork1.zil into a runnable z3 file.

"%ZILF_PATH%\zilf.exe" zork1.zil

"%ZILF_PATH%\zapf.exe" zork1.zap zork1-ignite.z3

Then run your Z3 file in a Zmachine runner. I’m usingWindows Frotzfrom David Kinder based on Stefan Jokisch’s Frotz core:

media-modal-id

modal-4

Or, if you’re of a certain age as I am, you can apply a CRT filter to your Terminal and use a CLI implementation of a Zmachine like Matthew Darby’s “Fic” written in Python:

media-modal-id

modal-5

### Continuing the journey

We will use the existing historical repositories as the canonical home forZork’s source. Once the initial pull requests land under the MIT License, contributions are welcome. We chose MIT for its simplicity and openness because it makes the code easy to study, teach, and build upon. File issues, share insights, or submit small, well-documented improvements that help others learn from the original design. The goal is not to modernizeZorkbut to preserve it as a space for exploration and education.

Zorkhas always been more than a game. It is a reminder that imagination and engineering can outlast generations of hardware and players. Bringing this code into the open is both a celebration and a thank you to the original Infocom creators for inventing a universe we are still exploring, to Jason Scott and the Internet Archive for decades of stewardship and partnership, and to colleagues across Microsoft OSPO, Xbox, and Activision who helped make open source possible.

section-id

section-1

/en-us/opensource/blog/author/stacey-haffner

/en-us/opensource/blog/author/scott-hanselman

section-id

section-2

Related posts

section-id

section-3

/en-us/opensource/blog/fragments/global-cta-banner

section-id

section-4

/en-us/opensource/blog/fragments/social-footer
