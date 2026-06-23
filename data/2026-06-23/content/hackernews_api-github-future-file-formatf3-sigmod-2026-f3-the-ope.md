---
title: 'GitHub - future-file-format/F3: [SIGMOD 2026] F3: The Open-Source Data File Format for the Future · GitHub'
url: https://github.com/future-file-format/f3
site_name: hackernews_api
content_file: hackernews_api-github-future-file-formatf3-sigmod-2026-f3-the-ope
fetched_at: '2026-06-23T19:38:31.533138'
original_url: https://github.com/future-file-format/f3
author: tosh
date: '2026-06-23'
description: '[SIGMOD 2026] F3: The Open-Source Data File Format for the Future - future-file-format/F3'
tags:
- hackernews
- trending
---

future-file-format

 

/

F3

Public

* NotificationsYou must be signed in to change notification settings
* Fork22
* Star573

 
 
 
 
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

4 Commits
4 Commits
.cargo
.cargo
 
 
.github/
workflows
.github/
workflows
 
 
deprecated_code
deprecated_code
 
 
doc
doc
 
 
exp_scripts
exp_scripts
 
 
fff-bench
fff-bench
 
 
fff-core
fff-core
 
 
fff-encoding
fff-encoding
 
 
fff-format
fff-format
 
 
fff-poc
fff-poc
 
 
fff-test-util
fff-test-util
 
 
fff-ude-wasm
fff-ude-wasm
 
 
fff-ude
fff-ude
 
 
format
format
 
 
results
results
 
 
scripts
scripts
 
 
third_party
third_party
 
 
wasm-libs
wasm-libs
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
View all files

## Repository files navigation

 
 

# F3: The Open-Source Data File Format for the Future

F3 is a data file format that is designed with efficiency, interoperability, and extensibility in mind. It provides a data organization that rectifies the layout shortcomings of the last-generation formats like Parquet, while at the same time maintaining good interoperability and extensibility (a.k.a future-proof) via embedded Wasm decoders.

⚠️This project is a research prototype verifying the ideas in the paper. You should not use it in production.

## Build instructions

We only tested on an Intel machine with Debian 12.

git submodule update --init --recursive
./scripts/setup_debian.sh

#
 build the PoC package of F3

cargo build -p fff-poc

#
 run unit test for F3

cargo 
test
 -p fff-poc

## Important directories

format: FlatBuffer definition of the file format.

fff-poc: The main code of the F3 format. It references other subdirs like fff-core, fff-encoding, fff-format, and fff-ude-wasm.

fff-bench: Benchmarks and experiments appeared in the paper. Specifically,fff-bench/examplesshould contain most experiments, both micro and e2e.

fff-ude*: ude stand for User-Defined-Encoding and code in those directories relates to the Wasm decoding implementation.

scriptsandexp_scripts: scripts related to run the experiments.

## Reproduction steps for the experiment results in the paper

Please refer todoc/paper_reproduction.mdfor the detailed steps.

## License

This project is licensed under the MIT License. SeeLICENSEfor details.

## Citation

If you find this project useful, please consider citing:

@article
{
zeng2025f3
,

author
 = 
{
Zeng, Xinyu and Meng, Ruijun and Prammer, Martin and McKinney, Wes and Patel, Jignesh M. and Pavlo, Andrew and Zhang, Huanchen
}
,

title
 = 
{
F3: The Open-Source Data File Format for the Future
}
,

year
 = 
{
2025
}
,

issue_date
 = 
{
September 2025
}
,

publisher
 = 
{
Association for Computing Machinery
}
,

address
 = 
{
New York, NY, USA
}
,

volume
 = 
{
3
}
,

number
 = 
{
4
}
,

url
 = 
{
https://doi.org/10.1145/3749163
}
,

doi
 = 
{
10.1145/3749163
}
,
abstract = {Columnar storage formats are the foundation for modern data analytics systems. The proliferation of open-source file formats (i.e., Parquet, ORC) allows seamless data sharing across disparate platforms. However, these formats were created over a decade ago for hardware and workload environments that are much different from today. Although these formats have incorporated some updates to their specification to adapt to these changes, not all deployments support those modifications, and too often systems cannot overcome the formats' deficiencies and limitations without a rewrite.In this paper, we present the Future-proof File Format (F3) project. It is a next-generation open-source file format with interoperability, extensibility, and efficiency as its core design principles. F3 obviates the need to create a new format every time a shift occurs in data processing and computing by providing a data organization structure and a general-purpose API to allow developers to add new encoding schemes easily. Each self-describing F3 file includes both the data and meta-data, as well as WebAssembly (Wasm) binaries to decode the data. Embedding the decoders in each file requires minimal storage (kilobytes) and ensures compatibility on any platform in case native decoders are unavailable. To evaluate F3, we compared it against legacy and state-of-the-art open-source file formats. Our evaluations demonstrate the efficacy of F3's storage layout and the benefits of Wasm-driven decoding.},

journal
 = 
{
Proc. ACM Manag. Data
}
,

month
 = sep,

articleno
 = 
{
245
}
,

numpages
 = 
{
27
}
,

keywords
 = 
{
columnar storage, compression, extensibility, file format
}

}

## About

[SIGMOD 2026] F3: The Open-Source Data File Format for the Future

dl.acm.org/doi/10.1145/3749163

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

573

 stars
 

### Watchers

6

 watching
 

### Forks

22

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

* Rust67.5%
* WebAssembly25.3%
* C++4.2%
* Shell1.7%
* Python1.3%