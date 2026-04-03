---
title: SHARP
url: https://apple.github.io/ml-sharp/
site_name: hackernews
fetched_at: '2025-12-16T11:07:58.289926'
original_url: https://apple.github.io/ml-sharp/
author: dvrp
date: '2025-12-16'
---

# Sharp Monocular View Synthesis in Less Than a Second

Lars Mescheder, Wei Dong, Shiwei Li, Xuyang Bai, Marcel Santos, Peiyun Hu, Bruno Lecouat, Mingmin Zhen,

Amaël Delaunoy, Tian Fang, Yanghai Tsin, Stephan R. Richter, Vladlen Koltun

Apple

 Paper (arXiv)


 Code (GitHub)


## Abstract

We present SHARP, an approach to photorealistic view synthesis from a single image. Given a single photograph, SHARP regresses the parameters of a 3D Gaussian representation of the depicted scene. This is done in less than a second on a standard GPU via a single feedforward pass through a neural network. The 3D Gaussian representation produced by SHARP can then be rendered in real time, yielding high-resolution photorealistic images for nearby views. The representation is metric, with absolute scale, supporting metric camera movements. Experimental results demonstrate that SHARP delivers robust zero-shot generalization across datasets. It sets a new state of the art on multiple datasets, reducing LPIPS by 25–34% and DISTS by 21–43% versus the best prior model, while lowering the synthesis time by three orders of magnitude.

Input

Views synthesized by SHARP

SHARP synthesizes a photorealistic 3D representation from a single photograph in less
than a second. The synthesized representation supports high-resolution rendering of nearby views,
with sharp details and fine structures, at more than 100 frames per second on a standard GPU. We
illustrate on photographs fromUnsplash.

## Video Comparisons

* Unsplash
* ETH3D
* Middlebury
* ScanNet++
* TanksAndTemples
* Booster
* WildRGBD

Gen3C

ViewCrafter

TMPI

Flash3D

LVSM

SVC

Select a video to compare

Gen3C

ViewCrafter

TMPI

Flash3D

LVSM

SVC

Select a video to compare

Gen3C

ViewCrafter

TMPI

Flash3D

LVSM

SVC

Select a video to compare

Gen3C

ViewCrafter

TMPI

Flash3D

LVSM

SVC

Select a video to compare

Gen3C

ViewCrafter

TMPI

Flash3D

LVSM

SVC

Select a video to compare

Gen3C

ViewCrafter

TMPI

Flash3D

LVSM

SVC

Select a video to compare

Gen3C

ViewCrafter

TMPI

Flash3D

LVSM

SVC

Select a video to compare

## Citation

@inproceedings{Sharp2025:arxiv,
 title = {Sharp Monocular View Synthesis in Less Than a Second},
 author = {Lars Mescheder and Wei Dong and Shiwei Li and Xuyang Bai and Marcel Santos and Peiyun Hu and Bruno Lecouat and Mingmin Zhen and Ama\"{e}l Delaunoyand Tian Fang and Yanghai Tsin and Stephan R. Richter and Vladlen Koltun},
 journal = {arXiv preprint arXiv:2512.10685},
 year = {2025},
 url = {https://arxiv.org/abs/2512.10685},
}
