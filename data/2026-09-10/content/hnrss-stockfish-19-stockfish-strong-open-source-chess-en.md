---
title: Stockfish 19 - Stockfish - Strong open-source chess engine
url: https://stockfishchess.org/blog/2026/stockfish-19/
site_name: hnrss
content_file: hnrss-stockfish-19-stockfish-strong-open-source-chess-en
fetched_at: '2026-09-10T14:50:09.095571'
original_url: https://stockfishchess.org/blog/2026/stockfish-19/
date: '2026-09-07'
description: Stronger, smaller, and easier to run, thanks to an upgraded network architecture, universal binaries, and more!
tags:
- hackernews
- hnrss
---

Today, we have the pleasure of announcingStockfish 19, a new major release. As always, you can freely download it atstockfishchess.org/downloadand use it as a drop-in replacement in theGUI of your choiceto benefit from stronger play and more accurate analysis.

Whether you can spare hours or days of CPU time, your help matters for the ongoing development of Stockfish. Find out how you can contribute atstockfishchess.org/get-involved. Join ourDiscord serverto get in touch with the community of developers and users of the project!

## Quality of Chess Play

In tests against Stockfish 18, this new release brings an Elo gain ofup to 44 points, and winsmore than three times as many game pairsas it loses.

Stockfish continues to set the standard for engine strength. Against the strongest competition, it consistently secures the top spot in engine championships, continuing todominate the field.

## Update Highlights

### Universal Binaries

We have transitioned to universal binaries for our releases, simplifying the download process. These universal binaries automatically detect the features of your CPU and run the optimal code, eliminating the need to manually choose between AVX2, AVX-512, etc.

### Upgraded NNUE Architecture and Training

This release introduces the SFNNv16 network architecture, reducing binary size by removing redundant threat features while increasing strength by introducing new pawn-pair features. The secondary neural network, introduced in Stockfish 16.1, has been retired, enhancing strength in positions where the small net previously underperformed.

The training process has been further improved with the introduction of new techniques, such as Quantization-Aware Training (QAT), and further parameter tweaks. These techniques have been applied to hundreds of billions of training positions, all of which have been consistently rescored using a strongLeelanet.

### Expanded Platform Support

We have added native support for RISC-V (RVV) and LoongArch (LSX/LASX), 1GB Linux huge pages, as well as WebAssembly targets. The shared-memory implementation for Linux, macOS, and BSD was also overhauled.

### Strict Position Validation

We have implemented stricter validation for board positions, FEN strings, and UCI commands. The engine will now output aninfo string CRITICAL ERRORfollowed by the exact command and the reason it failed, and then immediately terminate the process. A good GUI will ensure you never encounter these errors.

## Thank You

The Stockfish project builds on a thriving community of enthusiasts (thanks to everybody!) who contribute their expertise, time, and resources to build a free and open-source chess engine that is robust, widely available, and very strong.

We would like to express our gratitude for the 16.4k stars that light up our GitHub project. Thank you for your support and encouragement – your recognition means a lot to us. Programmers can contribute to the project either directly toStockfish(C++), toFishtest(HTML, CSS, JavaScript, and Python), to our trainernnue-pytorch(C++ and Python), or to ourwebsite(HTML, CSS/SCSS, and JavaScript).

The Stockfish team