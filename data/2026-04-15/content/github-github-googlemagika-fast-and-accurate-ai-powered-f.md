---
title: 'GitHub - google/magika: Fast and accurate AI powered file content types detection · GitHub'
url: https://github.com/google/magika
site_name: github
content_file: github-github-googlemagika-fast-and-accurate-ai-powered-f
fetched_at: '2026-04-15T11:55:48.996703'
original_url: https://github.com/google/magika
author: google
description: 'Fast and accurate AI powered file content types detection - GitHub - google/magika: Fast and accurate AI powered file content types detection'
---

google



/

magika

Public

* NotificationsYou must be signed in to change notification settings
* Fork697
* Star13.4k




 
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

1,726 Commits
1,726 Commits
.cargo
.cargo
 
 
.gemini
.gemini
 
 
.github
.github
 
 
assets
assets
 
 
docs
docs
 
 
go
go
 
 
js
js
 
 
python
python
 
 
rust
rust
 
 
tests_data
tests_data
 
 
website-ng
website-ng
 
 
website
website
 
 
.dockerignore
.dockerignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
CITATION.cff
CITATION.cff
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
dist-workspace.toml
dist-workspace.toml
 
 
View all files

## Repository files navigation

# Magika

Magika is a novel AI-powered file type detection tool that relies on the recent advance of deep learning to provide accurate detection. Under the hood, Magika employs a custom, highly optimized model that only weighs about a few MBs, and enables precise file identification within milliseconds, even when running on a single CPU. Magika has been trained and evaluated on a dataset of ~100M samples across 200+ content types (covering both binary and textual file formats), and it achieves an average ~99% accuracy on our test set.

Here is an example of what Magika command line output looks like:

Magika is used at scale to help improve Google users' safety by routing Gmail, Drive, and Safe Browsing files to the proper security and content policy scanners, processing hundreds billions samples on a weekly basis. Magika has also been integrated withVirusTotal(example) andabuse.ch(example).

For more context you can read our initialannouncement post on Google's OSS blog, you can consultMagika's website, and you can read more in ourresearch paper, published at the IEEE/ACM International Conference on Software Engineering (ICSE) 2025.

You can try Magika without installing anything by using ourweb demo, which runs locally in your browser!

# Highlights

* Available as a command line tool written in Rust, a Python API, and additional bindings for Rust, JavaScript/TypeScript (with an experimental npm package, which powers ourweb demo), and GoLang (WIP).
* Trained and evaluated on a dataset of ~100M files across200+ content types.
* On our test set, Magika achieves ~99% average precision and recall, outperforming existing approaches -- especially on textual content types.
* After the model is loaded (which is a one-off overhead), the inference time is about 5ms per file, even when run on a single CPU.
* You can invoke Magika with even thousands of files at the same time. You can also use-rfor recursively scanning a directory.
* Near-constant inference time, independently from the file size; Magika only uses a limited subset of the file's content.
* Magika uses a per-content-type threshold system that determines whether to "trust" the prediction for the model, or whether to return a generic label, such as "Generic text document" or "Unknown binary data".
* The tolerance to errors can be controlled via different prediction modes, such ashigh-confidence,medium-confidence, andbest-guess.
* The client and the bindings are already open source, and more is coming soon!

# Table of Contents

1. Getting StartedInstallationQuick Start
2. Installation
3. Quick Start
4. Documentation
5. Security Vulnerabilities
6. License
7. Disclaimer

# Getting Started

## Installation

### Command Line Tool

Magika ships a CLI written in Rust, and can be installed in several ways.

Viamagikapython package:

pipx install magika

Via brew (macOS / Linux)

brew install magika

Via installer script:

curl -LsSf https://securityresearch.google/magika/install.sh
|
 sh

or:

powershell -ExecutionPolicy Bypass -c
"
irm https://securityresearch.google/magika/install.ps1 | iex
"

Viamagika-cliRust package:

cargo install --locked magika-cli

### Python package

pip install magika

### JavaScript package

npm install magika

## Quick Start

Here you can find a number of quick examples just to get you started.

To learn about Magika's inner workings, see theCore Conceptssection of Magika's website.

### Command Line Tool Examples

%
cd
 tests_data/basic
&&
 magika -r
*

|
 head
asm/code.asm: Assembly (code)
batch/simple.bat: DOS batch file (code)
c/code.c: C
source
 (code)
css/code.css: CSS
source
 (code)
csv/magika_test.csv: CSV document (code)
dockerfile/Dockerfile: Dockerfile (code)
docx/doc.docx: Microsoft Word 2007+ document (document)
docx/magika_test.docx: Microsoft Word 2007+ document (document)
eml/sample.eml: RFC 822 mail (text)
empty/empty_file: Empty file (inode)

% magika ./tests_data/basic/python/code.py --json
[
 {

"
path
"
:
"
./tests_data/basic/python/code.py
"
,

"
result
"
: {

"
status
"
:
"
ok
"
,

"
value
"
: {

"
dl
"
: {

"
description
"
:
"
Python source
"
,

"
extensions
"
: [

"
py
"
,

"
pyi
"

 ],

"
group
"
:
"
code
"
,

"
is_text
"
: true,

"
label
"
:
"
python
"
,

"
mime_type
"
:
"
text/x-python
"

 },

"
output
"
: {

"
description
"
:
"
Python source
"
,

"
extensions
"
: [

"
py
"
,

"
pyi
"

 ],

"
group
"
:
"
code
"
,

"
is_text
"
: true,

"
label
"
:
"
python
"
,

"
mime_type
"
:
"
text/x-python
"

 },

"
score
"
: 0.996999979019165
 }
 }
 }
]

% cat tests_data/basic/ini/doc.ini
|
 magika -
-: INI configuration file (text)

% magika --help
Determines file content types using AI

Usage: magika [OPTIONS] [PATH]...

Arguments:
 [PATH]...
 List of paths to the files to analyze.

 Use a dash (-) to
read
 from standard input (can only be used once).

Options:
 -r, --recursive
 Identifies files within directories instead of identifying the directory itself

 --no-dereference
 Identifies symbolic links as is instead of identifying their content by following them

 --colors
 Prints with colors regardless of terminal support

 --no-colors
 Prints without colors regardless of terminal support

 -s, --output-score
 Prints the prediction score
in
 addition to the content
type

 -i, --mime-type
 Prints the MIME
type
 instead of the content
type
 description

 -l, --label
 Prints a simple label instead of the content
type
 description

 --json
 Prints
in
 JSON format

 --jsonl
 Prints
in
 JSONL format

 --format
<
CUSTOM
>

 Prints using a custom format (use --help
for
 details).

 The following placeholders are supported:

 %p The file path
 %l The unique label identifying the content
type

 %d The description of the content
type

 %g The group of the content
type

 %m The MIME
type
 of the content
type

 %e Possible file extensions
for
 the content
type

 %s The score of the content
type

for
 the file
 %S The score of the content
type

for

the file

in
 percent
 %b The model output
if
 overruled (empty otherwise)
 %% A literal %

 -h, --help
 Print
help
 (see a summary with
'
-h
'
)

 -V, --version
 Print version

For more examples and documentation about the CLI, seehttps://crates.io/crates/magika-cli.

### Python Examples

>
>>

from

magika

import

Magika

>
>>

m

=

Magika
()

>
>>

res

=

m
.
identify_bytes
(
b'function log(msg) {console.log(msg);}'
)

>
>>

print
(
res
.
output
.
label
)

javascript

>
>>

from

magika

import

Magika

>
>>

m

=

Magika
()

>
>>

res

=

m
.
identify_path
(
'./tests_data/basic/ini/doc.ini'
)

>
>>

print
(
res
.
output
.
label
)

ini

>
>>

from

magika

import

Magika

>
>>

m

=

Magika
()

>
>>

with

open
(
'./tests_data/basic/ini/doc.ini'
,
'rb'
)
as

f
:

>
>>

res

=

m
.
identify_stream
(
f
)

>
>>

print
(
res
.
output
.
label
)

ini

For more examples and documentation about the Python module, see thePythonMagikamodulesection.

# Documentation

Please consultMagika's websitefor detailed documentation about:

* Core ConceptsHow Magika worksModels & content typesPrediction modesUnderstanding the output
* How Magika works
* Models & content types
* Prediction modes
* Understanding the output
* CLI & Bindings (Python module, JavaScript module, ...)
* Contributing
* FAQ
* ...

# Security Vulnerabilities

Please contact us directly atmagika-dev@google.com.

# License

Apache 2.0; seeLICENSEfor details.

# Disclaimer

This project is not an official Google project. It is not supported by
Google and Google specifically disclaims all warranties as to its quality,
merchantability, or fitness for a particular purpose.

## About

Fast and accurate AI powered file content types detection

securityresearch.google/magika/

### Topics

 ai

 deep-learning

 filetype

 mime-types

 keras-models

 keras-classification-models

 onnx

### Resources

 Readme



### License

 Apache-2.0 license


### Code of conduct

 Code of conduct


### Contributing

 Contributing


### Security policy

 Security policy


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

13.4k

 stars


### Watchers

50

 watching


### Forks

697

 forks


 Report repository



## Releases14

python-v1.0.2

 Latest



Feb 27, 2026



+ 13 releases

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* Python33.2%
* Rust26.1%
* TypeScript18.4%
* Rich Text Format5.6%
* Svelte4.9%
* Go3.9%
* Other7.9%
