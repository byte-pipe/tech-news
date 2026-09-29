---
title: Tcl/Tk 9.1
url: https://www.tcl-lang.org/software/tcltk/9.1.html
site_name: hackernews_api
content_file: hackernews_api-tcltk-91
fetched_at: '2026-09-29T22:52:19.631395'
original_url: https://www.tcl-lang.org/software/tcltk/9.1.html
author: dmux
date: '2026-09-29'
description: Tcl/Tk 9.1
tags:
- hackernews
- trending
---

Hosted by

* HOME
* ABOUT TCL/TK
* SOFTWARE
* CORE DEVELOPMENT
* COMMUNITY
* DOCUMENTATION

Tcl/Tk 9.1

Latest Release: Tcl/Tk 9.1.0 (Sep 29, 2026)Tcl/Tk 9.1.0 is the current development work on Tcl and Tk,
aiming toward stable releases in September 2026. They add new features
and interfaces to the foundation of Tcl/Tk 9.0.Download Tcl/Tk 9.1.0 Source Releases### Highlights of Tcl 9.1New commandunicode: Unicode normalizationNew C routinesTcl_UtfToNormalized*: Unicode normalizationNew commandtimer: monotonic clock; microsecond resolutionNew commandlfilter: select items from listNew commandinterp set: variable access in child interpreterNewsubstoptions:-backslashes,-commands,-variables.Newswitchoptions:-integer.Many C99 math routines now available asexprfunctions.Applications now required to call an initialization routine,
 eitherTcl_FindExecutableorTclZipfs_AppHook.New C routineTcl_IsEmpty.New C routineTcl_GetEncodingNameForUser.New C routineTcl_AttemptCreateHashEntry.New C routinesTcl_ListObjRange,Tcl_ListObjRepeat,Tcl_ListObjReverse.New C time API usinglong longin place ofTcl_TimeCase-insensitive filesystem paths on macOS.auto_execokandexecsearch reform on Windows.Revised searches for script library and encodings.Improved list internals for memory efficiency of large lists.Extended support for 64-bit sizes.### Highlights of Tk 9.1Accessibility screen reader support.Initial support for bidirectional text / RTL languages.New widgetttk::toggleswitch.New commandtk attribtable.sendcommand revised and improved on Aqua.Handling of negative screen distances.Extended states inttk::treeviewandttk::notebookImprovements toTk_CanvasTextInfoRotated text on labelsLimit message box and dialogs to physical screen width.Improved listbox selection colors.Removed obsolete support for Windows XP appearances.This is the main Tcl Developer Xchange site,
		 www.tcl-lang.org .About this Site|[email protected]Home|About Tcl/Tk|Software|Core Development|Community|Documentation