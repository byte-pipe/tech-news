---
title: GitHub - roboflow/rf-detr: RF-DETR is a real-time object detection and segmentation model architecture developed by Roboflow, SOTA on COCO, designed f...
url: https://github.com/roboflow/rf-detr
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-09-08T00:31:38.827687
---

# GitHub - roboflow/rf-detr: RF-DETR is a real-time object detection and segmentation model architecture developed by Roboflow, SOTA on COCO, designed f...

# RF‑DETR Repository Overview

## Project Summary
- RF‑DETR is a real‑time transformer model for object detection, instance segmentation, and (preview) keypoint detection, developed by Roboflow.  
- Built on a DINOv2 vision‑transformer backbone, it offers state‑of‑the‑art accuracy‑latency trade‑offs on Microsoft COCO and RF100‑VL datasets.  
- The open‑source `rfdetr` package and Apache‑licensed models are released under Apache 2.0; the Plus components (RF‑DETR‑XL/2XL) use the PML 1.0 license.  
- Model sizes were discovered via neural architecture search (NAS); the same NAS tool is available on the Roboflow platform for custom dataset optimization.

## Installation
- Standard installation (Python ≥ 3.10):  
  ```bash
  pip install rfdetr
  ```
- Install the latest development version from source:  
  ```bash
  pip install https://github.com/roboflow/rf-detr/archive/refs/heads/develop.zip
  ```

## Benchmarks  

### Detection (COCO / RF100‑VL)
| Model | COCO AP<sub>50</sub> | COCO AP<sub>50:95</sub> | RF100‑VL AP<sub>50</sub> | RF100‑VL AP<sub>50:95</sub> | Latency (ms) | Params (M) | Resolution |
|-------|---------------------|------------------------|--------------------------|----------------------------|--------------|------------|------------|
| RF‑DETR‑N | 67.6 | 48.4 | 85.0 | 57.7 | 2.3 | 30.5 | 384×384 |
| RF‑DETR‑S | 72.1 | 53.0 | 86.7 | 60.2 | 3.5 | 32.1 | 512×512 |
| RF‑DETR‑M | 73.6 | 54.7 | 87.4 | 61.2 | 4.4 | 33.7 | 576×576 |
| RF‑DETR‑L | 75.1 | 56.5 | 88.2 | 62.2 | 6.8 | 33.9 | 704×704 |
| RF‑DETR‑XL* | 77.4 | 58.6 | 88.5 | 62.9 | 11.5 | 126.4 | 700×700 |
| RF‑DETR‑2XL* | 78.5 | 60.1 | 89.0 | 63.2 | 17.2 | 126.9 | 880×880 |

\* Plus models (PML 1.0 license).  
- All latency numbers measured on an NVIDIA T4 with TensorRT (FP16, batch 1).  
- RF‑DETR consistently outperforms YOLO 11, YOLO 26, LW‑DETR, and D‑FINE families at comparable latency.

### Segmentation (COCO)
| Model | COCO AP<sub>50</sub> | COCO AP<sub>50:95</sub> | Latency (ms) | Params (M) | Resolution |
|-------|---------------------|------------------------|--------------|------------|------------|
| RF‑DETR‑Seg‑N | 63.0 | 40.3 | 3.4 | 33.6 | 312×312 |
| RF‑DETR‑Seg‑S | 66.2 | 43.1 | 4.4 | 33.7 | 384×384 |
| RF‑DETR‑Seg‑M | 68.4 | 45.3 | 5.9 | 35.7 | 432×432 |
| RF‑DETR‑Seg‑L | 70.5 | 47.1 | 8.8 | 36.2 | 504×504 |
| RF‑DETR‑Seg‑XL | 72.2 | 48.8 | 13.5 | 38.1 | 624×624 |
| RF‑DETR‑Seg‑2XL | 73.1 | 49.9 | 21.8 | 38.6 | 768×768 |

- RF‑DETR segmentation models surpass YOLOv8 and YOLOv11 segmentation variants across the board.

### Keypoint Detection (Preview)
| Model | COCO AP<sub>50:95</sub> | Latency (ms) | Params (M) |
|-------|------------------------|--------------|------------|
| RF‑DETR Keypoint (preview) | 71.8 | 9.7 | 40.7 |
| YOLO11‑pose N | 48.9 | 3.2 | 2.9 |
| YOLO11‑pose X | 68.6 | 10.6 | 58.8 |
| YOLO26‑pose X | 71.0 | 9.8 | 57.6 |

- The preview keypoint model already matches or exceeds the best YOLO 26 pose model while remaining real‑time.

## Licensing
- Core `rfdetr` package and models: **Apache 2.0**.  
- Plus components (RF‑DETR‑XL/2XL): **PML 1.0**.  

## Neural Architecture Search (NAS)
- The NAS method used to create the published model sizes is now exposed on the Roboflow platform.  
- Users can run NAS on their own datasets to discover optimal RF‑DETR architectures tailored to specific tasks and hardware constraints.  

## Additional Resources
- Documentation, changelog, and contribution guidelines are located in the `docs/` and root `README.md`.  
- Benchmarking methodology and reproducibility details are provided in the `roboflow/sab` repository.