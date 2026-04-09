---
title: SHARP
url: https://apple.github.io/ml-sharp/
date: 2025-12-16
site: hackernews
model: llama3.2:1b
summarized_at: 2025-12-16T11:15:39.912308
screenshot: hackernews-sharp.png
---

# SHARP

## Sharp Monocular View Synthesis in Less Than a Second

SHARP is an approach to photorealistic view synthesis from a single image, achieving faster rendering times than prior methods.

### Main Idea
The SHARP system consists of a single feedforward neural network that regresses the parameters of a 3D Gaussian representation for a given scene. This representation can be rendered in real-time to produce high-resolution images, which are then metric and support camera movements.

### Key Points

* SHARP synthesizes views from a photograph in under a second.
* Supports high resolution rendering with sharp details and fine structures at over 100 frames per second on standard GPUs.
* Compared to prior methods on multiple datasets, achieving a reduction of up to 34% in LPIPS (Lipschitz Polynomial Image Gradient) and DISTS (Data Statistics Transform).
* Demonstrates robust zero-shot generalization across various datasets.

### Summary

The SHARP approach uses a neural network to predict the parameters of a 3D Gaussian representation for a given scene, which can be rendered quickly in real-time. This results in high-quality photorealistic images that support camera movements and are metric with absolute scale. The system achieves significant improvements over prior methods on multiple datasets, showcasing its potential as an efficient solution for view synthesis tasks.

### Supported Datasets

* Unsplash
* ETH3D
* Middlebury
* ScanNet++
* TankstAndTemples
* Booster
* WildRGBD
