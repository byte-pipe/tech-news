---
title: 'GitHub - rxi/microui: A tiny immediate-mode UI library · GitHub'
url: https://github.com/rxi/microui
site_name: hackernews_api
content_file: hackernews_api-github-rximicroui-a-tiny-immediate-mode-ui-library
fetched_at: '2026-06-19T01:17:32.899108'
original_url: https://github.com/rxi/microui
author: peter_d_sherman
date: '2026-06-17'
description: A tiny immediate-mode UI library. Contribute to rxi/microui development by creating an account on GitHub.
tags:
- hackernews
- trending
---

rxi

 

/

microui

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork384
* Star6.3k

 
 
 
 
master
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

51 Commits
51 Commits
.github
.github
 
 
demo
demo
 
 
doc
doc
 
 
src
src
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

Atiny, portable, immediate-mode UI library written in ANSI C

## Features

* Tiny: around1100 slocof ANSI C
* Works within a fixed-sized memory region: no additional memory is allocated
* Built-in controls: window, scrollable panel, button, slider, textbox, label,
checkbox, wordwrapped text
* Works with any rendering system that can draw rectangles and text
* Designed to allow the user to easily add custom controls
* Simple layout system

## Example

if
 (
mu_begin_window
(
ctx
, 
"My Window"
, 
mu_rect
(
10
, 
10
, 
140
, 
86
))) {
 
mu_layout_row
(
ctx
, 
2
, (
int
[]) { 
60
, 
-1
 }, 
0
);

 
mu_label
(
ctx
, 
"First:"
);
 
if
 (
mu_button
(
ctx
, 
"Button1"
)) {
 
printf
(
"Button1 pressed\n"
);
 }

 
mu_label
(
ctx
, 
"Second:"
);
 
if
 (
mu_button
(
ctx
, 
"Button2"
)) {
 
mu_open_popup
(
ctx
, 
"My Popup"
);
 }

 
if
 (
mu_begin_popup
(
ctx
, 
"My Popup"
)) {
 
mu_label
(
ctx
, 
"Hello world!"
);
 
mu_end_popup
(
ctx
);
 }

 
mu_end_window
(
ctx
);
}

## Screenshot

Browser Demo

## Usage

* Seedoc/usage.mdfor usage instructions
* See thedemodirectory for a usage example

## Notes

The library expects the user to provide input and handle the resultant drawing
commands, it does not do any drawing itself.

## Contributing

The library is designed to be lightweight, providing a foundation to which you
can easily add custom controls and UI elements; pull requests adding additional
features will likely not be merged. Bug reports are welcome.

## License

This library is free software; you can redistribute it and/or modify it under
the terms of the MIT license. SeeLICENSEfor details.

## About

A tiny immediate-mode UI library

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

6.3k

 stars
 

### Watchers

87

 watching
 

### Forks

384

 forks
 

 Report repository

 

## Releases

No releases published

## Sponsor this project

 

 

 Sponsor

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

Learn more about GitHub Sponsors

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* C100.0%