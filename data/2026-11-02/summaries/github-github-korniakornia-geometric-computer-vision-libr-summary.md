---
title: GitHub - kornia/kornia: 🐍 Geometric Computer Vision Library for Spatial AI · GitHub
url: https://github.com/kornia/kornia
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-11-02T08:49:03.222436
---

# GitHub - kornia/kornia: 🐍 Geometric Computer Vision Library for Spatial AI · GitHub

# Kornia – Differentiable Computer Vision Library for PyTorch  

## Overview  
- Kornia is an open‑source library that adds a large collection of differentiable image processing and geometric vision algorithms to PyTorch.  
- It integrates directly into AI pipelines, supporting batch processing, automatic differentiation, and GPU acceleration.  
- The project aims to become the reference implementation and executable specification for differentiable computer vision within the PyTorch ecosystem, with explicit conventions, conformance tests, and benchmarks.  

## When to Use Kornia  
- When hand‑written implementations become long, fragile, or inefficient on the GPU.  
- For tasks that require per‑sample parameters in a single batched call (e.g., per‑image blur kernels, rotation angles, affine matrices).  
- When you need batched minimal solvers, robust estimation (RANSAC), or differentiable geometry (depth‑to‑3D, camera models, Lie groups).  
- For GPU‑accelerated local feature pipelines (SIFT, HardNet, DISK, LoFTR, LightGlue, etc.).  
- When you want annotated augmentations that keep image, mask, box, and keypoint transformations consistent.  

## Key Components  

### Differentiable Image Processing  
- Filters: Gaussian, Sobel, Median, Box blur, etc.  
- Transformations: Affine, Homography, Perspective, warp operations.  
- Enhancements: Histogram equalization, CLAHE, gamma correction, brightness/contrast adjustments.  
- Edge detection: Canny, Laplacian, Sobel.  

### Advanced Augmentations  
- Pipelines: `AugmentationSequential`, `PatchSequential`, `VideoSequential`.  
- Automatic policies: AutoAugment, RandAugment, TrivialAugment.  
- Supports synchronized augmentation of images, masks, bounding boxes, and keypoints, with GPU‑resident parameter sampling.  

### Pre‑trained AI Models  
- Face detection: YuNet.  
- Feature matching: LoFTR, LightGlue.  
- Feature descriptors: DISK, DeDoDe, SOLD2.  
- Segmentation: SAM.  
- Classification: MobileViT, Vision Transformer.  

## Supported Operation Categories (selected)  

- **Image Processing** – color space conversions, geometric transforms, filtering, edge detection, morphological ops.  
- **Augmentation** – random cropping/erasing, geometric transforms (affine, flip, fisheye, perspective, TPS, elastic), noise injections, color jitter, MixUp, CutMix, Mosaic, etc.  
- **Feature Detection & Description** – detectors (Harris, GFTT, DoG, KeyNet, DISK, DeDoDe), descriptors (SIFT, HardNet, TFeat, SOSNet, LAFDescriptor), matchers (nearest‑neighbor, mutual NN, AdaLAM, LightGlue, LoFTR).  
- **Geometry** – camera models and calibration, stereo/epipolar geometry, homography and essential matrix estimation, depth from disparity, 3D transformations.  
- **Deep Learning Layers** – custom convolution layers, recurrent vision layers, loss functions for image tasks.  

## Performance Highlights  
- Batched operations run on the input device without NumPy round‑trips and are mostly differentiable.  
- On RTX 4090 with batch size 32, many filters, warps, and matching steps are 10×–70× faster in eager mode than CPU‑based OpenCV or scikit‑image; compiled graphs can exceed 100× speed‑ups.  
- Compared to torchvision on the same GPU, eager Kornia is slower for simple ops, but compiled Kornia outperforms for hue, color jitter, and Gaussian blur.  
- All operator configurations are tested with `torch.compile` and exported to ONNX (≈1,000 operators supported).  

## Resources  
- Documentation, tutorials, examples, and a performance page are available in the repository.  
- Contribution guidelines, code of conduct, and roadmap are provided in the repo’s markdown files.