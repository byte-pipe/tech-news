---
title: Microsoft's New CLI Text Editor Works Great on Ubuntu - OMG! Ubuntu
url: https://www.omgubuntu.co.uk/2025/06/microsoft-edit-text-editor-ubuntu
site_name: hackernews
fetched_at: '2025-06-22T10:21:28.559621'
original_url: https://www.omgubuntu.co.uk/2025/06/microsoft-edit-text-editor-ubuntu
author: Joey Sneddon
date: '2025-06-22'
published_date: '2025-06-17T22:15:00+00:00'
description: Edit is a new open source command line text editor from Microsoft that supports Windows, macOS and Linux. Learn what it can do, and how to try it on Ubuntu.
---

If you spend a lot time in a terminal on Linux you’ll have preferred command-line text editor, but Microsoft’s recently announced open-source offering, simply calledEdit, might be worth checking out — if only so you know you’re not missing out.

Editis a remake/reboot of the oldMS-DOS Editor, updated to suit current sensibilities. Built using Rust, it aims to deliver a user experience that, per its GitHub page, provides“modern interface and input controls similar to VS Code.”

Microsoft says it madeEdit“to provide an accessible editor that even users largely unfamiliar with terminals can easily use”on Windows if/when needed, out-of-the-box (as recent versions of Windows do not include a CLI text editor in recent versions).

The arrival ofEditwill mean Windows devs aren’t forced to fire up notepad.exe to make a simple shell script edit, but is there any benefit to running the app on Linux?

Note:When I spotlight apps, tools and utilities on this blog, it’snotbecause I think you (or anyone) “MUST” use them. I simply showcase choices. Whether you choose to use them is up to you.

## Why would Linux users useEdit?

As straightforward to use as it seems

Windows is the primary target forEditsince it lacks a built-in CLI text editor natively so the fact you can useEditon Linux (and macOS) is more of bonus than purpose.

But if you use Linux andVSCodeyour muscle memory might like the factEditshares many of the latter’s keybindings. This could make it easier to slot in to your workflow compared tovimornano(though I stress it’s not a replacement for either of those).

Not that only avowed VSCode fans will see the appeal.

The simplicity of the text-driven UI (TUI) makes it less complex to learn, while the speed ofEdit, even when seeking across lines in giant 1GB+ files, is impressive — both USPs are by design.

Working with multiple files is easy enough too

Eager to avoid “how to exit vim” memes, Microsoft designedEditas a modeless text editor (as opposed to a multi-mode one like Vim, where you need to learn how to activate different modes and switch between them as needed).

You canuse a mouse or a keyboardto access menus, select lines or regions of text, position the caret, etc which makes using it feel more intuitive in use than the either/or approach of (admittedly more capable) alternatives.

Editoffers up a modest, lightweight set of features (and an equally modest footprint: a mere 250kB out of the box, and fast file opening) including:

* Find and Replace(supportsMatch Case&Regular Expression)
* Word wrapon resize(optional)
* Set tab/space indentation
* Set/change file encoding
* Line Feed (LF) or Carriage Return + Line Feed ( CRLF)
* Open multiple files

There’s pretty much all there is right now.Edithas no syntax highlighting, no range of colour schemes, no command prompt, and few creature comforts common in other command line text editors.

Editis designed to edit text, rather than handle complex task better suited to IDEs.

More features are planned, including colour schemes and a settings TUI, so the list of features will grow in time, but as Microsoft’s aim is speed and simplicity, don’t expect too many bells and whistles.

Editis open source so anyone can modify, contribute, package or fork it.

## How to RunEditon Ubuntu

Editis free, open source software that works on Windows, Linux and macOS (so no, you don’t need to using Windows to make use of it).

Right now there is no official “installer” for Linux, and no unofficial DEB of PPA, thoughthere is a snap. A couple of Linux distributions now packageEdit, including Arch Linux, and Manjaro, so if you use one of those, you can install it properly.

To runEditon Ubuntu you can download the latest binary from theproject GitHub releases page(be sure to select the correct one for your architecture), extract the package,cdinto the extracted folder, then launch the binary each time you want to use it:

1. Download the latest release(link above)
2. Extract the archive(right-click inNautilus>Extract)
3. Open a terminal app(such as the newPytxisin Ubuntu 25.10)
4. Navigate to the extracted folder:cd /path/to/
5. RunEditdirectly:./edit

To install the unofficial snap build useApp Center(search ‘msedit’) or runsudo snap install mseditfrom the command line, and usemseditto launch it. On my laptop, the snap takes ~5 seconds to open. The official binary is instantaneous. YMMV.

From there, the interface is easy enough to figure out.

Give it a try and let me know what you think!

 CLI Tools

 Edit

 Microsoft

 Text Editor
