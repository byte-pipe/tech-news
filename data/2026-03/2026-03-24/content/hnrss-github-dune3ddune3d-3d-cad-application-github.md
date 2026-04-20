---
title: 'GitHub - dune3d/dune3d: 3D CAD application · GitHub'
url: https://github.com/dune3d/dune3d
site_name: hnrss
content_file: hnrss-github-dune3ddune3d-3d-cad-application-github
fetched_at: '2026-03-24T11:21:58.750312'
original_url: https://github.com/dune3d/dune3d
date: '2026-03-22'
description: 3D CAD application. Contribute to dune3d/dune3d development by creating an account on GitHub.
tags:
- hackernews
- hnrss
---

dune3d



/

dune3d

Public

* NotificationsYou must be signed in to change notification settings
* Fork74
* Star1.8k




 
main
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

825 Commits
825 Commits
.github/
workflows
.github/
workflows
 
 
3rd_party
3rd_party
 
 
scripts
scripts
 
 
src
src
 
 
wix
wix
 
 
.cirrus.yml
.cirrus.yml
 
 
.clang-format
.clang-format
 
 
.gitignore
.gitignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Info.plist
Info.plist
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
check_dll.sh
check_dll.sh
 
 
check_version.py
check_version.py
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
macos-launcher.sh
macos-launcher.sh
 
 
make_bindist.sh
make_bindist.sh
 
 
make_color_presets.py
make_color_presets.py
 
 
make_icon_texture_atlas.py
make_icon_texture_atlas.py
 
 
make_rc.py
make_rc.py
 
 
make_version.py
make_version.py
 
 
meson.build
meson.build
 
 
org.dune3d.dune3d.desktop
org.dune3d.dune3d.desktop
 
 
org.dune3d.dune3d.metainfo.xml
org.dune3d.dune3d.metainfo.xml
 
 
screenshot.png
screenshot.png
 
 
version.py
version.py
 
 
View all files

## Repository files navigation

# Dune 3D

Dune 3D is a parametric 3D CAD application that supports STEP import/export, fillets and chamfers.

## Motivation

So why another open-source 3D CAD application when FreeCAD and Solvespace exist?
My primary use case for 3D CAD is designing 3D-printed enclosures for my electronics projects. I often found myself procrastinating designing the enclosure and attributed that to my dissatisfaction with the available open source 3D CAD applications.

While FreeCAD technically does everything I need, the way it's implemented isn't quite to my liking. My biggest pain points with it are the modal sketcher that only works in 2D, no constraints in 3D for extrusions and the perils of referencing things in the design.

Solvespace on the other hand gets the workflow part right, but falls short by not importing STEP and the geometry kernel not supporting chamfers and fillets.

Having solved the similar problem for PCB CAD by developing Horizon EDA, I began pondering whether I could pull off the same thing for 3D CAD. After all, what does it take to make a 3D CAD?

* Geometry kernel to do extrusions, intersections, chamfers, etc.: While it's not a nice library to work with, Open CASCADE is the only viable choice if we want to have STEP import/export and fillets/chamfers. Fortunately, I have some experience with it from dealing with STEP files in Horizon EDA.
* 3D viewport: Obviously, we need a way to put 3D geometry on screen, zoom/pan and select things. The 3D preview in Horizon EDA already does all of this, so I have a well-understood codebase I can reuse.
* Constraint solver: Unlike with Horizon EDA where things just stay where you last moved them, in 3D CAD, it's commonplace to specify where things go by means of constraints that need to be solved. Turns out that Solvespace's solver is available as a library1, so that part's also covered.
* Editor infrastructure: Last but not least, we need code that takes care of the tools, undo/redo and all of the other bits and pieces that make up an interactive editor. While there'll be some differences, I felt confident that I could reuse and adapt the interactive manipulator from Horizon EDA.

With all of the building blocks available, I set out to glue them together to form a 3D CAD application. About three months later, it's somewhat presentable.

## How to build

See thebuild instructions.

## How to use

Similar to Horizon EDA, all tools and actions are available from the spacebar menu.

Use the "set workplane" tool to set a group's workplane.

Also check out thedocumentation.

## Where to go with questions

The project's discussion platforms are amatrix roomandGitHub Discussions.

## Anticipated questions

### Where do I find sample files?

See thesamplesrepository.

### Does it run on Windows?

See thebuild instructionsfor how to build on Windows.

### Does it run on macOS?

See thebuild instructionsfor how to build on macOS.

### Why not integrate it into Horizon EDA?

There's no place in Horizon EDA where a 3D CAD would make sense to implement. Also, I wanted to do some things differently and give Gtk 4 a try.

### Why not improve Solvespace or FreeCAD?

Making FreeCAD parametric in 3D or putting Open CASCADE into Solvespace seemed to be too big a change to pull off as an outside contributor to either project. I also really like writing CAD software, so here we are.

## Footnotes

1. I ended up directly using solvespace's solver instead of the suggestedwrapper codesince it didn't expose all of the features I needed.
I also had to patch the solver to make it sufficiently fast for the kinds of equations I was generating by symbolically solving equations where applicable.↩

## About

3D CAD application

dune3d.org

### Topics

 cad

 parametric

 3d-printing

 3d

 opencascade

### Resources

 Readme



### License

 GPL-3.0 license


### Contributing

 Contributing


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

1.8k

 stars


### Watchers

27

 watching


### Forks

74

 forks


 Report repository



## Releases5

Dune 3D Version 1.4.0 "Einstein"

 Latest



Jan 28, 2026



+ 4 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* C84.3%
* C++15.0%
* GLSL0.2%
* Meson0.2%
* Python0.2%
* Shell0.1%
