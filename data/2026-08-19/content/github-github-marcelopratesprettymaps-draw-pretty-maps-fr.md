---
title: 'GitHub - marceloprates/prettymaps: Draw pretty maps from OpenStreetMap data! Built with osmnx +matplotlib + shapely · GitHub'
url: https://github.com/marceloprates/prettymaps
site_name: github
content_file: github-github-marcelopratesprettymaps-draw-pretty-maps-fr
fetched_at: '2026-08-19T19:22:59.573549'
original_url: https://github.com/marceloprates/prettymaps
author: marceloprates
description: Draw pretty maps from OpenStreetMap data! Built with osmnx +matplotlib + shapely - marceloprates/prettymaps
---

marceloprates

 

/

prettymaps

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork651
* Star13k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

283 Commits
283 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
docs
docs
 
 
notebooks
notebooks
 
 
pictures
pictures
 
 
prettymaps
prettymaps
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
MANIFEST.in
MANIFEST.in
 
 
README.md
README.md
 
 
app.py
app.py
 
 
mkdocs.yml
mkdocs.yml
 
 
packages.txt
packages.txt
 
 
requirements.txt
requirements.txt
 
 
setup.py
setup.py
 
 
setup.sh
setup.sh
 
 
View all files

## Repository files navigation

# prettymaps

A minimal Python library to draw customized maps fromOpenStreetMapcreated using theosmnx,matplotlib,shapelyandvsketchpackages.

 
 
 

This work islicensedunder a GNU Affero General Public License v3.0 (you can make commercial use, distribute and modify this project, but mustdisclosethe source code with the license and copyright notice)

## Note about crediting and NFTs:

* Please keep the printed message on the figures crediting my repository and OpenStreetMap (mandatory by their license).
* I am personallyagainstNFTs for theirenvironmental impact, the fact that they're agiant money-laundering pyramid schemeand the structural incentives they create fortheftin the open source and generative art communities.
* I do not authorize in any way this project to be used for selling NFTs, although I cannot legally enforce it.Respect the creator.
* TheAeternaCivitasandgeoartnftprojects have used this work to sell NFTs and refused to credit it. See how they reacted after being exposed:AeternaCivitas,geoartnft.
* I have closed my other generative art projects on Github and won't be sharing new ones as open source to protect me from the NFT community.

## As seen onHacker News:

## prettymaps subreddit

## Tutorial(marimo) ·Google Colaboratory Demo

# Installation

### Install locally:

Install prettymaps with:

pip install prettymaps

### Install on Google Colaboratory:

Install prettymaps with:

!pip install -e "git+https://github.com/marceloprates/prettymaps#egg=prettymaps"

Thenrestart the runtime(Runtime -> Restart Runtime) before importing prettymaps

# Run front-end

After prettymaps is installed, you can run the front-end (streamlit) application from the prettymaps repository using:

streamlit run app.py

# Tutorial

The full tutorial is atdocs/tutorial.md— a markdown walkthrough with rendered images, the[Plot]dataclass fields, thelayers/styleparameters, presets, multiplot, hillshade, and keypoints.

Quick start:

import
 
prettymaps

plot
 
=
 
prettymaps
.
plot
(
'Stad van de Zon, Heerhugowaard, Netherlands'
)

Resource

Where to find it

Full tutorial (markdown + images)

docs/tutorial.md

Interactive marimo notebook (runnable)

notebooks/tutorial.py

Open in Google Colab

Open in Colab

Streamlit front-end

streamlit run app.py

### Run the tutorial locally (marimo)

#
 Install marimo (already in requirements.txt)

pip install marimo

#
 Open the notebook in your browser

marimo edit notebooks/tutorial.py

### Customizing parameters

The most importantprettymaps.plot()parameters are:

* layers— dict of OpenStreetMap layers to fetch.
* style— dict of matplotlib style parameters per layer.
* preset— load a JSON preset (e.g.'default','minimal','macao','tijuca').
* circle/radius/dilate— boundary shape.

plotis a dataclass withgeodataframes(per-layer GeoDataFrames),fig, andax.

plot
 
=
 
prettymaps
.
plot
(
 
'Praça Ferreira do Amaral, Macau'
,
 
circle
=
True
,
 
radius
=
1100
,
 
layers
=
{
 
"water"
: {
"tags"
: {
"natural"
: [
"water"
, 
"bay"
]}},
 
"building"
: {
"tags"
: {
"building"
: 
True
}},
 },
 
style
=
{
 
"water"
: {
"fc"
: 
"#a1e3ff"
, 
"ec"
: 
"#2F3737"
},
 
"building"
: {
"palette"
: [
"#FFC857"
, 
"#E9724C"
, 
"#C5283D"
]},
 },
)

Seedocs/tutorial.mdfor the full set of examples (Macau, Bom Fim, mosaic, Barcelona plotter, Tijuca, multiplot, hillshade, Garopaba keypoints).