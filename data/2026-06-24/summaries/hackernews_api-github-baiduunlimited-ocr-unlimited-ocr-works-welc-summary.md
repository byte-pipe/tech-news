---
title: GitHub - baidu/Unlimited-OCR: Unlimited OCR Works: Welcome the Era of One-shot Long-horizon Parsing. · GitHub
url: https://github.com/baidu/Unlimited-OCR
date: 2026-06-23
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-24T01:02:37.892200
---

# GitHub - baidu/Unlimited-OCR: Unlimited OCR Works: Welcome the Era of One-shot Long-horizon Parsing. · GitHub

# Unlimited OCR Works

## Overview
- Introduces Unlimited-OCR, a model designed for one‑shot long‑horizon document parsing.
- Aims to extend the capabilities of Deepseek‑OCR by handling unlimited text length.
- Provides both transformer‑based and SGLang‑based inference pipelines.

## Release
- **2026/06/23** – Paper released on arXiv and model published on ModelScope.
- **2026/06/22** – Unlimited‑OCR announced as the next step after Deepseek‑OCR.

## Inference

### Transformers
- Runs on NVIDIA GPUs with Python 3.12.3 and CUDA 12.9.
- Required packages: `torch==2.10.0`, `torchvision==0.25.0`, `transformers==4.57.1`, `Pillow==12.1.1`, `matplotlib==3.10.8`, `einops==0.8.2`, `addict==2.4.0`, `easydict==1.13`, `pymupdf==1.27.2.2`, `psutil==7.2.2`.
- Model loading example:
  ```python
  from transformers import AutoModel, AutoTokenizer
  import torch, os

  model_name = 'baidu/Unlimited-OCR'
  tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
  model = AutoModel.from_pretrained(
      model_name,
      trust_remote_code=True,
      use_safetensors=True,
      torch_dtype=torch.bfloat16,
  ).eval().cuda()
  ```
- Two single‑image configurations:
  - **gundam** – `base_size=1024`, `image_size=640`, `crop_mode=True`.
  - **base** – `base_size=1024`, `image_size=1024`, `crop_mode=False`.
- Multi‑page/PDF parsing uses the **base** configuration (`image_size=1024`).

### SGLang
- Environment setup with `uv` virtualenv (Python 3.12) and installation of the local SGLang wheel, `kernels==0.11.7`, and `pymupdf`.
- Launch server command (example):
  ```bash
  python -m sglang.launch_server \
    --model baidu/Unlimited-OCR \
    --served-model-name Unlimited-OCR \
    --attention-backend fa3 \
    --page-size 1 \
    --mem-fraction-static 0.8 \
    --context-length 32768 \
    --enable-custom-logit-processor \
    --disable-overlap-schedule \
    --skip-server-warmup \
    --host 0.0.0.0 \
    --port 10000
  ```
- Provides an OpenAI‑compatible streaming API for image or PDF inputs.
- Supports custom logit processor `DeepseekOCRNoRepeatNGramLogitProcessor` to enforce no‑repeat‑ngram constraints.

## Usage Examples

### Single Image
```python
model.infer(
    tokenizer,
    prompt='<image>document parsing.',
    image_file='your_image.jpg',
    output_path='your/output/dir',
    base_size=1024,
    image_size=640,
    crop_mode=True,
    max_length=32768,
    no_repeat_ngram_size=35,
    ngram_window=128,
    save_results=True,
)
```

### Multi‑Page / PDF (base configuration)
```python
model.infer_multi(
    tokenizer,
    prompt='<image>Multi page parsing.',
    image_files=['page1.png', 'page2.png', 'page3.png'],
    output_path='your/output/dir',
    image_size=1024,
    max_length=32768,
    no_repeat_ngram_size=35,
    ngram_window=1024,
    save_results=True,
)
```
- PDF handling is performed by converting pages to images with PyMuPDF (`fitz`) and then calling `infer_multi`.

### Batch Inference with SGLang
```bash
python infer.py --image_dir ./examples/images --output_dir ./outputs --concurrency 8 --image_mode gundam
python infer.py --pdf ./examples/document.pdf --output_dir ./outputs --concurrency 8 --image_mode gundam
```
- Options include `--model_dir`, `--gpu`, and `--server_log`.

## Visualization
- The repository includes tools to visualize OCR results; refer to the `visualization` scripts in the codebase.

## Acknowledgement
- Thanks to the developers of Deepseek‑OCR, Deepseek‑OCR‑2, and PaddleOCR for their foundational models and ideas.

## Citation
```bibtex
@misc{yin2026unlimitedocrworks,
  title={Unlimited OCR Works},
  author={Yin et al.},
  year={2026},
  note={arXiv preprint}
}
```