---
title: GitHub - Friedrich-M/UniMate: [SIGGRAPH Asia 2026] UniMate: One Unified Model to Animate Diverse Skeletons · GitHub
url: https://github.com/Friedrich-M/UniMate
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-10-01T17:25:39.838229
---

# GitHub - Friedrich-M/UniMate: [SIGGRAPH Asia 2026] UniMate: One Unified Model to Animate Diverse Skeletons · GitHub

Here is a concise and informative summary of the article:

### Overview

UniMate is a unified model for animating diverse skeletons, a crucial aspect of many computer graphics, animation, and robotics applications. It combines various styles to create diverse animations.

### Key Features

* UniMate is written in Go and has a unified architecture
* It can animate bipedal, quadrupedal, avian, marine, insectoid, serpentine, and articulated rigid objects
* The dataset, UniML3D, contains 13,006 motion sequences with diverse skeletal topologies
* The raw source assets are available on the Hugging Face Hub
* A full data processing pipeline for converting raw assets into UniML3D can be viewed in README.md

### Training

UniMate is trained on the canonicalized clips in the dataset using a JSON configuration file, allowing for various input combinations of data and models.

### Software Components

* UniMate and UniML3D are implemented in Go
* Requirements.txt defines the necessary dependencies, including conda and pip
* The pipeline is built using the UniML3D dataset and data-processing files

### Future Enhancements

A new preprocessing pipeline for new rigging datasets will be released by this week.