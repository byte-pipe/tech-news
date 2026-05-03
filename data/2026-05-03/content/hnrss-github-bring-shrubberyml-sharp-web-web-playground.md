---
title: 'GitHub - bring-shrubbery/ml-sharp-web: Web playground to create Gaussian Splats using Apple''s ml-sharp model. · GitHub'
url: https://github.com/bring-shrubbery/ml-sharp-web
site_name: hnrss
content_file: hnrss-github-bring-shrubberyml-sharp-web-web-playground
fetched_at: '2026-05-03T19:54:59.590793'
original_url: https://github.com/bring-shrubbery/ml-sharp-web
date: '2026-05-03'
description: Web playground to create Gaussian Splats using Apple's ml-sharp model. - bring-shrubbery/ml-sharp-web
tags:
- hackernews
- hnrss
---

bring-shrubbery

 

/

ml-sharp-web

Public

* NotificationsYou must be signed in to change notification settings
* Fork4
* Star142

 
 
 
 
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

28 Commits
28 Commits
docs
docs
 
 
packages
packages
 
 
public
public
 
 
scripts
scripts
 
 
src
src
 
 
.gitignore
.gitignore
 
 
.vercelignore
.vercelignore
 
 
README.md
README.md
 
 
bun.lock
bun.lock
 
 
eslint.config.js
eslint.config.js
 
 
index.html
index.html
 
 
package.json
package.json
 
 
tsconfig.app.json
tsconfig.app.json
 
 
tsconfig.json
tsconfig.json
 
 
tsconfig.node.json
tsconfig.node.json
 
 
vercel.json
vercel.json
 
 
vite.config.ts
vite.config.ts
 
 
View all files

## Repository files navigation

# ml-sharp-web

A browser-based Gaussian splat generator built on top ofApple SHARP. ✨

This project lets you:

* upload one image
* generate Gaussian splats in the browser
* preview the result
* download a.plyfile

## Links

* Project repo:bring-shrubbery/ml-sharp-web
* Follow the author on X:@bringshrubberyy
* Upstream SHARP repo (Apple):apple/ml-sharp
* SHARP project page:apple.github.io/ml-sharp
* SHARP paper:arXiv:2512.10685

## Before you start (important license note)

Apple's SHARP repository has separate licenses for code and model weights.

* SHARP code license:LICENSE
* SHARP model license:LICENSE_MODEL

If you use Apple's released SHARP checkpoint/weights, you must followLICENSE_MODEL(research-use restrictions apply).

## What you need

* Buninstalled
* A modern desktop browser (Chrome or Edge recommended)
* Enough disk space and RAM for the SHARP model (the exported ONNX sidecar is large, ~2.4 GB)

## Quick start (run the app) 🚀

### 1. Star this repo 🤩

If this project helps you, please star it:

* bring-shrubbery/ml-sharp-web

### 2. Install dependencies

bun install

This also copies ONNX Runtime Web WASM assets intopublic/ort/automatically.

### 3. Start the app

bun dev

Open the URL shown by Vite (usuallyhttp://localhost:5173).

### 4. Use the app

1. Upload an image.
2. ClickGenerate Splat.
3. Preview the result and download the.plyfile.

## Important model file note (.onnx+.onnx.data)

SHARP exports usually producetwo files:

* sharp_web_predictor.onnx
* sharp_web_predictor.onnx.data

Both files must be served together from the same folder (for examplepublic/models/).

Why this matters:

* The.onnxfile is only the graph and metadata.
* The.onnx.datafile contains most of the model weights.

For that reason, the app uses the hosted model by default.
Uploading only the.onnxfile directly in the browser usually will not work because the.onnx.datasidecar is separate.

## Export the SHARP model to ONNX (beginner-friendly steps)

Everything runs in the browser, but you still need an exported SHARP ONNX model.

### 1. Clone Apple's SHARP repo (reference code)

git clone https://github.com/apple/ml-sharp /tmp/ml-sharp-upstream

### 2. Prepare a Python environment for export

You need Python + SHARP dependencies + ONNX export dependencies.

The easiest route is to follow the upstream SHARP setup first, then run this exporter script from this repo.

### 3. Export the browser predictor ONNX

From this repo:

python3 scripts/export_sharp_onnx.py \
 --sharp-repo /tmp/ml-sharp-upstream \
 --output public/models/sharp_web_predictor.onnx

If the model is large (it is), the script will also write:

public/models/sharp_web_predictor.onnx.data

### Optional export flags

* --checkpoint /path/to/sharp_2572gikvuh.ptto use a manually downloaded checkpoint
* --device cudato export on GPU (if your environment supports it)
* --opset 20to change ONNX opset (default is20)

## Static build (optional)

If you want a static build instead of runningbun dev:

bun run build
bun run preview

Notes:

* bun run buildcopiespublic/intodist/, including the model files.
* Ifsharp_web_predictor.onnx.datais present, the build output will be very large.

## How it works (high level)

* React + TypeScript UI (src/)
* ONNX Runtime Web worker for inference (src/workers/sharpWorker.ts)
* Browser-side SHARP postprocessing (NDC -> metric gaussian conversion)
* Browser-side PLY writer
* In-page preview with@mkkellogg/gaussian-splats-3d

## Troubleshooting 🛠️

### "expected magic word ... found 3c 21 64 6f" (WASM error)

This means a WASM file request returned HTML instead.

Try:

* run the app withbun dev(notfile://...)
* restart the dev server afterbun install
* verify these load in your browser:/ort/ort-wasm-simd-threaded.asyncify.mjs/ort/ort-wasm-simd-threaded.asyncify.wasm
* /ort/ort-wasm-simd-threaded.asyncify.mjs
* /ort/ort-wasm-simd-threaded.asyncify.wasm

### "Failed to load external data file ... sharp_web_predictor.onnx.data"

This means the ONNX sidecar file is missing or not served correctly.

Check:

* public/models/sharp_web_predictor.onnx
* public/models/sharp_web_predictor.onnx.data
* The app can reach the hosted model files in your deployment/browser environment

### The app runs, but generation is very slow or crashes

SHARP is large and browser inference is heavy.

Try:

* Chrome or Edge (desktop)
* smallerMax gaussiansin the UI
* closing other memory-heavy tabs/apps
* waiting longer on first run (model + runtime initialization can take time)

## Tech stack

* Bun
* React
* TypeScript
* Vite
* ONNX Runtime Web
* GaussianSplats3D viewer

## Project status

Working prototype / experimental. 🧪

The app runs end-to-end in the browser, but performance and compatibility depend heavily on browser WebGPU/WASM support and your machine's available memory.

## About

Web playground to create Gaussian Splats using Apple's ml-sharp model.

ml-sharp-web.vercel.app/

### Resources

 Readme

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

142

 stars
 

### Watchers

0

 watching
 

### Forks

4

 forks
 

 Report repository

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript59.0%
* JavaScript28.1%
* CSS8.7%
* Python4.0%
* HTML0.2%