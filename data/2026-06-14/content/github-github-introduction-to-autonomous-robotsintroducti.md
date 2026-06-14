---
title: 'GitHub - Introduction-to-Autonomous-Robots/Introduction-to-Autonomous-Robots: Introduction to Autonomous Robots · GitHub'
url: https://github.com/Introduction-to-Autonomous-Robots/Introduction-to-Autonomous-Robots
site_name: github
content_file: github-github-introduction-to-autonomous-robotsintroducti
fetched_at: '2026-06-14T19:34:05.480213'
original_url: https://github.com/Introduction-to-Autonomous-Robots/Introduction-to-Autonomous-Robots
author: Introduction-to-Autonomous-Robots
description: Introduction to Autonomous Robots. Contribute to Introduction-to-Autonomous-Robots/Introduction-to-Autonomous-Robots development by creating an account on GitHub.
---

Introduction-to-Autonomous-Robots

 

/

Introduction-to-Autonomous-Robots

Public

* NotificationsYou must be signed in to change notification settings
* Fork602
* Star2.6k

 
 
 
 
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

626 Commits
626 Commits
chapters
chapters
 
 
figs
figs
 
 
homework
homework
 
 
hooks
hooks
 
 
mathematica
mathematica
 
 
matlab
matlab
 
 
templates
templates
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
book.tex
book.tex
 
 
robotics.bib
robotics.bib
 
 
solutions.tex
solutions.tex
 
 
View all files

## Repository files navigation

# Introduction-to-Autonomous-Robots

An open textbook focusing on computational principles of autonomous robots. The source-code is released under Creative Commons 4.0 (CC-BY-NC-ND), whereas the print version is copyrighted by MIT Press. You are therefore permitted to use images and content from the book for non-commercial purposes (including teaching) with proper attribution, but you cannot post compiled versions of the book online.

The book is available on AmazonIntroduction to Autonomous Robots, you can also review it and/or rate it there.

## How to compile

Due to copyright issues, we are not allowed to have a freely available PDF version of this book online.
However, you can create one yourself if you so choose!
In order to compile a PDF of this book yourself, you either need a working implementation of Latex on your computer or use the online Latex editor overleaf.com.

### Overleaf compilation

On overleaf, you can either upload a zip file of the source code ("download ZIP" option underneath the green "Code" button on this page), or fork the project into your Github account and import it directly into Overleaf from there.

### Latex Compilation

#### Prerequisites

* LaTeX installation withpdflatexandbibtex
* ImageMagick (for converting missing figures)

#### Compilation Steps

pdflatex -interaction=nonstopmode book.tex
bibtex book
pdflatex -interaction=nonstopmode book.tex
pdflatex -interaction=nonstopmode book.tex

The final PDF will be generated asbook.pdf.

#### Notes

* The-interaction=nonstopmodeflag allows compilation to continue past non-fatal errors
* Multiple pdflatex runs are needed to resolve cross-references and citations
* Some warnings about overfull boxes are normal and don't affect the final output

## Citation

This book can be cited as follows:

Nikolaus Correll, Bradley Hayes, Christoffer Heckman and Alessandro Roncone. Introduction to Autonomous Robots: Mechanisms, Sensors, Actuators, and Algorithms, MIT Press, 2022 (forthcoming).

@book{correll2022introduction,
 title={ Introduction to Autonomous Robots: Mechanisms, Sensors, Actuators, and Algorithms},
 author={Correll, Nikolaus and Hayes, Bradley, and Heckman, Christoffer, and Roncone, Alessandro},
 year={2022},
 edition={1st},
 publisher={MIT Press, Cambridge, MA}
}

## About

Introduction to Autonomous Robots

introduction-to-autonomous-robots.github.io/

### Topics

 robotics

 book

 cu

 boulder

### Resources

 Readme

 

### License

 View license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

2.6k

 stars
 

### Watchers

86

 watching
 

### Forks

602

 forks
 

 Report repository

 

## Releases14

Major overhaul and revision of the whole book

 Latest

 

Dec 1, 2021

 

+ 13 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TeX52.0%
* Wolfram Language46.7%
* MATLAB1.2%
* Other0.1%