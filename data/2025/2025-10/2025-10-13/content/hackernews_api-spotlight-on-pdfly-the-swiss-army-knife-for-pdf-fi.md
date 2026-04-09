---
title: Spotlight on pdfly, the Swiss Army knife for PDF files
url: https://chezsoi.org/lucas/blog/spotlight-on-pdfly.html
site_name: hackernews_api
fetched_at: '2025-10-13T19:07:37.329593'
original_url: https://chezsoi.org/lucas/blog/spotlight-on-pdfly.html
author: Lucas Cimon
date: '2025-10-13'
description: 'Project documentation: pdfly.readthedocs.io pdfly is the youngest project of the py-pdf organization. It has been created by Martin Thoma in 2022. It''s simply a CLI tool to manipulate PDF files, written in Python and based on the fpdf2 & pypdf libraries. I''m a maintainer of the project 🙂 What can …'
tags:
- hackernews
- trending
---

# Spotlight on pdfly, the Swiss Army knife for PDF files

Mon 13 October 2025🔗Lucas Cimon

Project documentation: pdfly.readthedocs.io pdfly is the youngest project of the py-pdf organization. It has been created by Martin Thoma in 2022. It's simply a CLI tool to manipulate PDF files, written in Python and based on the fpdf2 & pypdf libraries. I'm a maintainer of the project 🙂 What can …

Project documentation:pdfly.readthedocs.io

pdflyis the youngest project of thepy-pdforganization.
It has been created byMartin Thomain 2022.

It's simplya CLI tool to manipulate PDF files, written in Python and based on thefpdf2&pypdflibraries.

I'm a maintainer of the project 🙂

## What can it do?

It has meany features, including:

* display PDF metadatausingpdfly metaandpdfly pagemetacommands.
Example:

$

pdfly

meta

minimal-document.pdf


Operating

System

Data
┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃

Attribute

┃

Value

┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│

File

Name

│

/tmp/minimal-document.pdf

│
│

File

Permissions

│

-rw-r--r--

│
│

File

Size

│

16
,978

bytes

│
│

Creation

Time

│

2025
-10-13

09
:44:32

│
│

Modification

Time

│

2025
-10-13

09
:44:32

│
│

Access

Time

│

2025
-10-13

09
:44:46

│
└───────────────────┴───────────────────────────┘


PDF

Data
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃

Attribute

┃

Value

┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│

CreationDate

│

2022
-04-03

18
:05:42+02:00

│
│

Creator

│

TeX

│
│

Producer

│

pdfTeX-1.40.23

│
│

Pages

│

1

│
│

Encrypted

│

None

│
│

PDF

File

Version

│

%PDF-1.5

│
│

Page

Layout

│

│
│

Page

Mode

│

│
│

PDF

ID

│

ID1
=
b
'q\x96\xc3\xe3U\xc1|\x9fS\xba\x9a\r\xcap\xcd\xd0'

│
│

│

ID2
=
b
'q\x96\xc3\xe3U\xc1|\x9fS\xba\x9a\r\xcap\xcd\xd0'

│
│

Fonts

(
embedded
)

│

│
│

Fonts

(
embedded
)

│

/KNEUFH+CMR10

│
│

Attachments

│

[]

│
│

Images

│

0

images

(
0

bytes
)

│
└────────────────────┴──────────────────────────────────────────────────────────┘

* pdflycan also combine files into new PDF documents: it canextract specific pages & merge documents(pdfly cat); selectivelyremove pages(pdfly rm);convert images to PDF documents(pdfly x2pdf); and evencompress documents(pdfly compress) orbuild booklets(pdfly 2-up&pdfly booklet).
* pdflyincludes some commands topull out specific content from PDF files:pdfly extract-images&pdfly extract-annotated-text.
* sometimes you want to edit a PDF file manually, in a text editor.
But when you do so, you break itsxreftable, that is an index of byte offsets in the document.pdfly update-offsetsis there to save the day,fixing manually-edited PDF documents, so that they can be opened in a PDF viewer again!

## Release 0.5.0 & new features

Today we released a new version:pdfly release 0.5.0.

Thanks to several contributors, including developers taking part inHacktoberfest, new exciting features have been added:

* pdfly signallows you toeasily sign PDF documents, whilepdfly check-signmakes it easy to check a PDF document signature. Thanks to@moormasterfor implementing this in PRs#165&#166👍🙏.
* pdfly extract-annotated-pagesextract only annotated pagesfrom a PDF, hence helping to review or rework pages from a large document iteratively. Thanks toHal Wine (@hwine)for implementing this in PR#128👍🙏.
* pdfly rotaterotate specific pagesof a document. Thanks toSubhajit Sahu (@wolfram77)for implementing this in PR#98👍🙏.

## What's next?

We have a bunch of feature ideas:up-for-grabsissues, including somegood first issuesaimed specially atnew contributors, that are willing to help but new to open-source.

Personally, I think thepdfly sign&check-signcould become handy to many end-users, and I think we should continue to extend those commands usage options, as described inissue #71.

We would also be happy to get your feedbacks, bug reports & feature suggestions! 🙂

* lang:en
* libre-software
* open-source
* python
* library
* release
* pdf
* pdfly
* hacktoberfest
* pypi
* prog



Lucas Cimon

Saint-Mathurin-sur-Loire
France

Software engineer. Tabletop RPG writer. Love libre software, and especially Python 🐍. Currently working for oui.sncf @Nantes



* Pages
* Bienvenue
* Projets en cours
* Créations de jeux de rôle
* Mes jeux de rôle favoris
* Images sous licences libres
* Je soutiens
* Open-Source
* Slides
* Net-Art
* Mentions légales
* Découvertes vidéoludiques
* Gopher access (beta)

## Ubiquity

### Syndication

 ATOM

 Shaarli

## En ce moment je lis

### 🤣

## Avatars

### Blogroll

* Justin Mason's Weblog
* Neal Krawetz Hacker Factor Blog
* Shaarli de sebsauvage
* Hugin & Munin
* Radio Rôliste
* C'est pas du jeu de rôle
* Trop Long ; Pas Lu !
* Le blog de Gulix
* Le blog de JeePee
* Pitche - Scénarios et aides pour divers JDR et JDRA
* Le Fix di6dent
* ptgptb
* Derrière le paravent de Greg Pogorzelski
* Oglaf
* Blog BD de Boulet
* Warpdoor
* AlphaBetaGamer
* Free Game Planet
* OuJeViPo
* Du papier et des jeux
* Blog de David Larlet
* No Limit Secu
* LinuxFR
* Framablog
* Reflets.info
* Tristan Nitot
* Blog de Victor Stinner
* Rhizome.org
* Du Monde Dans l'Objectif
* Galerie d'Elliot Jolivet aka Tenseï
* Galerie d'Elodie Olivier
* Antre Deletre - Peinture sur figurines
* Renard'eau
* L'instant Présent
* Atelier COALA
* boka.l - Laure Coignard
