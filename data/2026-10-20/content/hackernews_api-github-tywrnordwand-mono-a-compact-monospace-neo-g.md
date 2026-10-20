---
title: 'GitHub - tywr/Nordwand-Mono: A compact monospace neo-grotesque font designed for developers (and adventurers). · GitHub'
url: https://github.com/tywr/Nordwand-Mono
site_name: hackernews_api
content_file: hackernews_api-github-tywrnordwand-mono-a-compact-monospace-neo-g
fetched_at: '2026-10-20T15:34:57.370558'
original_url: https://github.com/tywr/Nordwand-Mono
author: noriax86
date: '2026-10-18'
description: A compact monospace neo-grotesque font designed for developers (and adventurers). - tywr/Nordwand-Mono
tags:
- hackernews
- trending
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

586 Commits
586 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github/
workflows
.github/
workflows
 
 
assets
assets
 
 
doc
doc
 
 
specimens
specimens
 
 
src
src
 
 
.gitignore
.gitignore
 
 
ATTRIBUTIONS.md
ATTRIBUTIONS.md
 
 
LICENSE-FONT.txt
LICENSE-FONT.txt
 
 
LICENSE.txt
LICENSE.txt
 
 
README.md
README.md
 
 
config.example.yml
config.example.yml
 
 
makefile
makefile
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

A compact neo-grotesk font designed for coding.

## Philosophy

I'm very passionate about the font I am using for my terminal and overall neovim experience, and I couldn't find the "perfect" font. So I decided to design one from scratch using python. This font aims to bring some elements from the all time classic "Univers" font into the proportions of the "JetBrains Mono" font. The name "Nordwand" is a reference to switzerland and its iconic typography – bringing it into the stiff and cold atmosphere of the swiss north faces.

Amongst the inspirations for the design, you might identify:

* Univers from Adrian Frutiger
* SF Pro & SF Mono from Apple
* Alpes Mono from Sharp Type
* Ubuntu Mono from Dalton Maag

## Alternative characters

Some alternative character designs are available to tweak the vibe of the font to your liking. See thealternative characters documentfor a visual comparison and the corresponding OpenType feature tags.

## Ligatures

Only two minimal ligatures are exposed with "->" and "=>". I might add a full set of ligatures later on, but I personally won't be using them.

## Compile your own custom version

This font is generated with python. Each glyph is drawn from a python glyph class, in which you can inject a drawing context object. You can for example modify some metrics like the x-height, the capital height etc.

To do so, override the config.example.yml with the values of your liking. Be sure to visualize the individual glyphs withpython -m visualize --config config.yml <glyph_id>. Then you can geneate the full font withpython -m generate_font --config config.yml. The font files will be generated inside./custom-fonts.

Warning

There are no guarantees that the font might look good with different metrics, and some glyphs might require some tweaking if the metrics are altered !

## Characters

## Weights

## Samples

### Python

### C++

### Haskell

## Alternative Alphabets

### Cyrillic