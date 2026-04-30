---
title: 'GitHub - GliaX/Stethoscope: A research-validated stethoscope whose plans are available Freely and openly. The cost of the entire stethoscope is between $2.5 to $5 to produce · GitHub'
url: https://github.com/GliaX/Stethoscope
site_name: hnrss
content_file: hnrss-github-gliaxstethoscope-a-research-validated-steth
fetched_at: '2026-04-30T12:14:54.599849'
original_url: https://github.com/GliaX/Stethoscope
date: '2026-04-29'
description: A research-validated stethoscope whose plans are available Freely and openly. The cost of the entire stethoscope is between $2.5 to $5 to produce - GliaX/Stethoscope
tags:
- hackernews
- hnrss
---

GliaX

 

/

Stethoscope

Public

* NotificationsYou must be signed in to change notification settings
* Fork106
* Star932

 
 
 
 
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

191 Commits
191 Commits
manual
manual
 
 
publication
publication
 
 
source_files
source_files
 
 
testing
testing
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
ring_x16.3mf
ring_x16.3mf
 
 
stethoscope_x1.3mf
stethoscope_x1.3mf
 
 
stethoscope_x3.3mf
stethoscope_x3.3mf
 
 
stethoscope_x4.3mf
stethoscope_x4.3mf
 
 
View all files

## Repository files navigation

# Stethoscope

This project aims to create a research-validated stethoscope whose plans are
available freely and openly. The goal is for the bell to cost ~USD$1-2 to produce,
and the rest of the stethoscope to cost approximately the same. You can see the peer-reviewed publication relating to this stethoscope's validation here:

http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0193087

Currently, the stethoscope resulting from this project functions as well as the
market gold standard, the Littmann Cardiology III.

# Bill of Materials

Printed parts:

* 1 stethoscope head (head.stl)
* 2 ear tubes (eartube.stl)
* 1 Y-piece (y_piece.stl)
* 1 Spring (spring.stl)
* 1 Ring (ring.stl)

Other hardware:Some vendors are suggested.

Translucent Silicone Rubber Tubing in US

* 50cm length of Silicone tube - 8mm ID, 13mm OD, 50 durometer8MM ID X 13MM OD (0.315" ID x 0.512" OD)
* 8MM ID X 13MM OD (0.315" ID x 0.512" OD)
* 20cm length of silicone tube (cut into 10cm pieces) - 4mm ID, 8mm OD, 50 durometer4mm ID x 8mm OD (0.157" ID x 0.314" OD)
* 4mm ID x 8mm OD (0.157" ID x 0.314" OD)

Diaphragm: 40mm diameter cut from a report cover with approx 0.35mm plastic sheet

* In Business Report Covers(USD$8.99)
* You can cut the diaphragm by hand or with a stamp likethis one

Earbuds / Eartips: Any large-sized standard earbuds will do

* Silicone Earbuds 7 Pairs - Large size

# Print Instructions

INFILL MUST BE 100%INFILL MUST BE 100%INFILL MUST BE 100%INFILL MUST BE 100%

* Use PETG or ABS
* Layer height: 0.2mm
* Use PrusaSlicer 2.0 or above to import 3MF file
* Modify filament and printer settings as needed.
* DO NOT MODIFY PRINT SETTINGS
* Export and print

# Troubleshooting

* If the spring and eartubes do not fit well, go ahead and scale the spring as needed
* If the head and ring do not fit well, use caution as you may be modifying the acoustics. You can scale the head a little.

# Notes

* We do not use PLA due to deformation in heat and poor plastic quality in the spring causing early failure. PLA may be used, but the lifetime of the stethoscope will decrease significantly.
* We do not use brims, but you may print the eartubes and Y-pieces with a brim of 2mm to ensure that none of the parts lift off.

INFILL MUST BE 100% Otherwise, the stethoscope will not produce a correct sound!

# Assembly Instructions

Seethis instructional videofor assembly instructions.

* Attach the diaphragm (40mm) to the stethoscope head.
* Attach the stethoscope head to the silicone tube.
* Attach the silicone tube to the Y-Piece.
* Attach spring to ear tubes.
* Attach the Y-piece to the ear tubes.
* Attach the ear tubes to the eartips / earbuds.
* Test the stethoscope as per the validation instructions.

# Printing the inserts

The inserts are included in themanualdirectory. Using 8.5 x 11 (Legal) paper,
they can be printed at 8.25" page width with 95% scale for the top print and
90% scale for the bottom print using GIMP.

The top insert is cut at 14.5cm and again at 1cm creating two labels of 13.5cm height.
These inserts are printed on adhesive material.

The bottom insert is cut at a width of 20cm with a height cuts at 25cm, 15cm,
13.5cm and 3.5cm creating 10cm x 20cm inserts.

# Changing and creating SCAD files

CrystalSCADandOpenSCADwere used to create all STL files. To recreate the stethoscope head, simply do:

gem install crystalscad
ruby source_files/stethoscope_head/stethoscope_head.rb

The SCAD files output from CrystalSCAD are found insource_files/stethoscope_head/outputand are named as follows:

* PrintableStethoscopeHead1Assembly_output.scad - The head

# Mass Manufacturing

We generally print 4 stethoscopes per plate to ensure that each stethoscope is created out of the same material.

Our serial numbering system consists of two parts. The last number part is the total number of unique stethoscopes created since day 1. All numbers before that dash are spool identifiers involved in that stethoscope. For example:

001-010 would be the tenth stethoscope made with the first spool in our inventory. If the first spool makes a total of 15 stethoscopes, then the first stethoscope of the second spool would be 002-016. If the twentieth stethoscope uses plastic from spool 002 and spool 003, it would be 002-003-020.

# Other stethoscopes

Others have made 3D printed stethoscopes too. See:

* https://www.youmagine.com/designs/stethoscope-chestpiece

# Licensing notes

As per our understanding, hardware is not covered by copyright. However, we present
our work under the TAPR OHL license insofar as it applies.

## About

A research-validated stethoscope whose plans are available Freely and openly. The cost of the entire stethoscope is between $2.5 to $5 to produce

### Topics

 open-source

 medicine

 open-hardware

 free-software

 stethoscope

 glia

### Resources

 Readme

 

### License

 View license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

932

 stars
 

### Watchers

91

 watching
 

### Forks

106

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Ruby57.4%
* OpenSCAD37.1%
* MATLAB5.5%