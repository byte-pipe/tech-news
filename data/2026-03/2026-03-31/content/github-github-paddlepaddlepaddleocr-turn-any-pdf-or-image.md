---
title: 'GitHub - PaddlePaddle/PaddleOCR: Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages. · GitHub'
url: https://github.com/PaddlePaddle/PaddleOCR
site_name: github
content_file: github-github-paddlepaddlepaddleocr-turn-any-pdf-or-image
fetched_at: '2026-03-31T11:22:16.407208'
original_url: https://github.com/PaddlePaddle/PaddleOCR
author: PaddlePaddle
description: Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages. - PaddlePaddle/PaddleOCR
---

PaddlePaddle



/

PaddleOCR

Public

* NotificationsYou must be signed in to change notification settings
* Fork10.1k
* Star73.8k




 
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

6,861 Commits
6,861 Commits
.github
.github
 
 
applications
applications
 
 
benchmark
benchmark
 
 
configs
configs
 
 
deploy
deploy
 
 
doc/
fonts
doc/
fonts
 
 
docs
docs
 
 
langchain-paddleocr
langchain-paddleocr
 
 
mcp_server
mcp_server
 
 
overrides
overrides
 
 
paddleocr
paddleocr
 
 
ppocr
ppocr
 
 
ppstructure
ppstructure
 
 
readme
readme
 
 
skills
skills
 
 
test_tipc
test_tipc
 
 
tests
tests
 
 
tools
tools
 
 
.clang_format.hook
.clang_format.hook
 
 
.gitignore
.gitignore
 
 
.lycheeignore
.lycheeignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.style.yapf
.style.yapf
 
 
CNAME
CNAME
 
 
LICENSE
LICENSE
 
 
MANIFEST.in
MANIFEST.in
 
 
README.md
README.md
 
 
awesome_projects.md
awesome_projects.md
 
 
mkdocs-ci.yml
mkdocs-ci.yml
 
 
mkdocs.yml
mkdocs.yml
 
 
pyproject.toml
pyproject.toml
 
 
requirements.txt
requirements.txt
 
 
setup.py
setup.py
 
 
train.sh
train.sh
 
 
View all files

## Repository files navigation

### Global Leading OCR Toolkit & Document AI Engine

English |简体中文|繁體中文|日本語|한국어|Français|Русский|Español|العربية

PaddleOCR converts PDF documents and images into structured, LLM-ready data (JSON/Markdown) with industry-leading accuracy. With 70k+ Stars and trusted by top-tier projects like Dify, RAGFlow, and Cherry Studio, PaddleOCR is the bedrock for building intelligent RAG and Agentic applications.

## 🚀 Key Features

### 📄 Intelligent Document Parsing (LLM-Ready)

Transforming messy visuals into structured data for the LLM era.

* SOTA Document VLM: FeaturingPaddleOCR-VL-1.5 (0.9B), the industry's leading lightweight vision-language model for document parsing. It excels in parsing complex documents across 5 major "Real-World" challenges:Warping, Scanning, Screen Photography, Illumination, and Skewed documents, with structured outputs inMarkdownandJSONformats.
* Structure-Aware Conversion: Powered byPP-StructureV3, seamlessly convert complex PDFs and images intoMarkdownorJSON. Unlike the PaddleOCR-VL series models, it provides more fine-grained coordinate information, including table cell coordinates, text coordinates, and more.
* Production-Ready Efficiency: Achieve commercial-grade accuracy with an ultra-small footprint. Outperforms numerous closed-source solutions in public benchmarks while remaining resource-efficient for edge/cloud deployment.

### 🔍 Universal Text Recognition (Scene OCR)

The global gold standard for high-speed, multilingual text spotting.

* 100+ Languages Supported: Native recognition for a vast global library. OurPP-OCRv5single-model solution elegantly handles multilingual mixed documents (Chinese, English, Japanese, Pinyin, etc.).
* Complex Element Mastery: Beyond standard text recognition, we supportnatural scene text spottingacross a wide range of environments, including IDs, street views, books, and industrial components
* Performance Leap: PP-OCRv5 delivers a13% accuracy boostover previous versions, maintaining the "Extreme Efficiency" that PaddleOCR is famous for.

### 🛠️ Developer-Centric Ecosystem

* Seamless Integration: The premier choice for the AI Agent ecosystem—deeply integrated withDify, RAGFlow, Pathway, and Cherry Studio.
* LLM Data Flywheel: A complete pipeline to build high-quality datasets, providing a sustainable "Data Engine" for fine-tuning Large Language Models.
* One-Click Deployment: Supports various hardware backends (NVIDIA GPU, Intel CPU, Kunlunxin XPU, and diverse AI Accelerators).

## 📣 Recent updates

### 🔥 [2026.01.29] PaddleOCR v3.4.0 Released: The Era of Irregular Document Parsing

* PaddleOCR-VL-1.5 (SOTA 0.9B VLM): Our latest flagship model for document parsing is now live!94.5% Accuracy on OmniDocBench: Surpassing top-tier general large models and specialized document parsers.Real-World Robustness: First to introduce thePP-DocLayoutV3algorithm for irregular shape positioning, mastering 5 tough scenarios:Skew, Warping, Scanning, Illumination, and Screen Photography.Capability Expansion: Now supportsSeal Recognition,Text Spotting, and expands to111 languages(including China’s Tibetan script and Bengali).Long Document Mastery: Supports automatic cross-page table merging and hierarchical heading identification.Try it now: Available onHuggingFaceor ourOfficial Website.
* 94.5% Accuracy on OmniDocBench: Surpassing top-tier general large models and specialized document parsers.
* Real-World Robustness: First to introduce thePP-DocLayoutV3algorithm for irregular shape positioning, mastering 5 tough scenarios:Skew, Warping, Scanning, Illumination, and Screen Photography.
* Capability Expansion: Now supportsSeal Recognition,Text Spotting, and expands to111 languages(including China’s Tibetan script and Bengali).
* Long Document Mastery: Supports automatic cross-page table merging and hierarchical heading identification.
* Try it now: Available onHuggingFaceor ourOfficial Website.

2025.10.16: Release of PaddleOCR 3.3.0

* Released PaddleOCR-VL:Model Introduction:PaddleOCR-VLis a SOTA and resource-efficient model tailored for document parsing. Its core component is PaddleOCR-VL-0.9B, a compact yet powerful vision-language model (VLM) that integrates a NaViT-style dynamic resolution visual encoder with the ERNIE-4.5-0.3B language model to enable accurate element recognition.This innovative model efficiently supports 109 languages and excels in recognizing complex elements (e.g., text, tables, formulas, and charts), while maintaining minimal resource consumption. Through comprehensive evaluations on widely used public benchmarks and in-house benchmarks, PaddleOCR-VL achieves SOTA performance in both page-level document parsing and element-level recognition. It significantly outperforms existing solutions, exhibits strong competitiveness against top-tier VLMs, and delivers fast inference speeds. These strengths make it highly suitable for practical deployment in real-world scenarios. The model has been released onHuggingFace. Everyone is welcome to download and use it! More introduction infomation can be found inPaddleOCR-VL.Core Features:Compact yet Powerful VLM Architecture: We present a novel vision-language model that is specifically designed for resource-efficient inference, achieving outstanding performance in element recognition. By integrating a NaViT-style dynamic high-resolution visual encoder with the lightweight ERNIE-4.5-0.3B language model, we significantly enhance the model’s recognition capabilities and decoding efficiency. This integration maintains high accuracy while reducing computational demands, making it well-suited for efficient and practical document processing applications.SOTA Performance on Document Parsing: PaddleOCR-VL achieves state-of-the-art performance in both page-level document parsing and element-level recognition. It significantly outperforms existing pipeline-based solutions and exhibiting strong competitiveness against leading vision-language models (VLMs) in document parsing. Moreover, it excels in recognizing complex document elements, such as text, tables, formulas, and charts, making it suitable for a wide range of challenging content types, including handwritten text and historical documents. This makes it highly versatile and suitable for a wide range of document types and scenarios.Multilingual Support: PaddleOCR-VL Supports 109 languages, covering major global languages, including but not limited to Chinese, English, Japanese, Latin, and Korean, as well as languages with different scripts and structures, such as Russian (Cyrillic script), Arabic, Hindi (Devanagari script), and Thai. This broad language coverage substantially enhances the applicability of our system to multilingual and globalized document processing scenarios.
* Model Introduction:PaddleOCR-VLis a SOTA and resource-efficient model tailored for document parsing. Its core component is PaddleOCR-VL-0.9B, a compact yet powerful vision-language model (VLM) that integrates a NaViT-style dynamic resolution visual encoder with the ERNIE-4.5-0.3B language model to enable accurate element recognition.This innovative model efficiently supports 109 languages and excels in recognizing complex elements (e.g., text, tables, formulas, and charts), while maintaining minimal resource consumption. Through comprehensive evaluations on widely used public benchmarks and in-house benchmarks, PaddleOCR-VL achieves SOTA performance in both page-level document parsing and element-level recognition. It significantly outperforms existing solutions, exhibits strong competitiveness against top-tier VLMs, and delivers fast inference speeds. These strengths make it highly suitable for practical deployment in real-world scenarios. The model has been released onHuggingFace. Everyone is welcome to download and use it! More introduction infomation can be found inPaddleOCR-VL.
* PaddleOCR-VLis a SOTA and resource-efficient model tailored for document parsing. Its core component is PaddleOCR-VL-0.9B, a compact yet powerful vision-language model (VLM) that integrates a NaViT-style dynamic resolution visual encoder with the ERNIE-4.5-0.3B language model to enable accurate element recognition.This innovative model efficiently supports 109 languages and excels in recognizing complex elements (e.g., text, tables, formulas, and charts), while maintaining minimal resource consumption. Through comprehensive evaluations on widely used public benchmarks and in-house benchmarks, PaddleOCR-VL achieves SOTA performance in both page-level document parsing and element-level recognition. It significantly outperforms existing solutions, exhibits strong competitiveness against top-tier VLMs, and delivers fast inference speeds. These strengths make it highly suitable for practical deployment in real-world scenarios. The model has been released onHuggingFace. Everyone is welcome to download and use it! More introduction infomation can be found inPaddleOCR-VL.
* Core Features:Compact yet Powerful VLM Architecture: We present a novel vision-language model that is specifically designed for resource-efficient inference, achieving outstanding performance in element recognition. By integrating a NaViT-style dynamic high-resolution visual encoder with the lightweight ERNIE-4.5-0.3B language model, we significantly enhance the model’s recognition capabilities and decoding efficiency. This integration maintains high accuracy while reducing computational demands, making it well-suited for efficient and practical document processing applications.SOTA Performance on Document Parsing: PaddleOCR-VL achieves state-of-the-art performance in both page-level document parsing and element-level recognition. It significantly outperforms existing pipeline-based solutions and exhibiting strong competitiveness against leading vision-language models (VLMs) in document parsing. Moreover, it excels in recognizing complex document elements, such as text, tables, formulas, and charts, making it suitable for a wide range of challenging content types, including handwritten text and historical documents. This makes it highly versatile and suitable for a wide range of document types and scenarios.Multilingual Support: PaddleOCR-VL Supports 109 languages, covering major global languages, including but not limited to Chinese, English, Japanese, Latin, and Korean, as well as languages with different scripts and structures, such as Russian (Cyrillic script), Arabic, Hindi (Devanagari script), and Thai. This broad language coverage substantially enhances the applicability of our system to multilingual and globalized document processing scenarios.
* Compact yet Powerful VLM Architecture: We present a novel vision-language model that is specifically designed for resource-efficient inference, achieving outstanding performance in element recognition. By integrating a NaViT-style dynamic high-resolution visual encoder with the lightweight ERNIE-4.5-0.3B language model, we significantly enhance the model’s recognition capabilities and decoding efficiency. This integration maintains high accuracy while reducing computational demands, making it well-suited for efficient and practical document processing applications.
* SOTA Performance on Document Parsing: PaddleOCR-VL achieves state-of-the-art performance in both page-level document parsing and element-level recognition. It significantly outperforms existing pipeline-based solutions and exhibiting strong competitiveness against leading vision-language models (VLMs) in document parsing. Moreover, it excels in recognizing complex document elements, such as text, tables, formulas, and charts, making it suitable for a wide range of challenging content types, including handwritten text and historical documents. This makes it highly versatile and suitable for a wide range of document types and scenarios.
* Multilingual Support: PaddleOCR-VL Supports 109 languages, covering major global languages, including but not limited to Chinese, English, Japanese, Latin, and Korean, as well as languages with different scripts and structures, such as Russian (Cyrillic script), Arabic, Hindi (Devanagari script), and Thai. This broad language coverage substantially enhances the applicability of our system to multilingual and globalized document processing scenarios.
* Released PP-OCRv5 Multilingual Recognition Model:Improved the accuracy and coverage of Latin script recognition; added support for Cyrillic, Arabic, Devanagari, Telugu, Tamil, and other language systems, covering recognition of 109 languages. The model has only 2M parameters, and the accuracy of some models has increased by over 40% compared to the previous generation.
* Improved the accuracy and coverage of Latin script recognition; added support for Cyrillic, Arabic, Devanagari, Telugu, Tamil, and other language systems, covering recognition of 109 languages. The model has only 2M parameters, and the accuracy of some models has increased by over 40% compared to the previous generation.

2025.08.21: Release of PaddleOCR 3.2.0

* Significant Model Additions:Introduced training, inference, and deployment for PP-OCRv5 recognition models in English, Thai, and Greek.The PP-OCRv5 English model delivers an 11% improvement in English scenarios compared to the main PP-OCRv5 model, with the Thai and Greek recognition models achieving accuracies of 82.68% and 89.28%, respectively.
* Introduced training, inference, and deployment for PP-OCRv5 recognition models in English, Thai, and Greek.The PP-OCRv5 English model delivers an 11% improvement in English scenarios compared to the main PP-OCRv5 model, with the Thai and Greek recognition models achieving accuracies of 82.68% and 89.28%, respectively.
* Deployment Capability Upgrades:Full support for PaddlePaddle framework versions 3.1.0 and 3.1.1.Comprehensive upgrade of the PP-OCRv5 C++ local deployment solution, now supporting both Linux and Windows, with feature parity and identical accuracy to the Python implementation.High-performance inference now supports CUDA 12, and inference can be performed using either the Paddle Inference or ONNX Runtime backends.The high-stability service-oriented deployment solution is now fully open-sourced, allowing users to customize Docker images and SDKs as required.The high-stability service-oriented deployment solution also supports invocation via manually constructed HTTP requests, enabling client-side code development in any programming language.
* Full support for PaddlePaddle framework versions 3.1.0 and 3.1.1.
* Comprehensive upgrade of the PP-OCRv5 C++ local deployment solution, now supporting both Linux and Windows, with feature parity and identical accuracy to the Python implementation.
* High-performance inference now supports CUDA 12, and inference can be performed using either the Paddle Inference or ONNX Runtime backends.
* The high-stability service-oriented deployment solution is now fully open-sourced, allowing users to customize Docker images and SDKs as required.
* The high-stability service-oriented deployment solution also supports invocation via manually constructed HTTP requests, enabling client-side code development in any programming language.
* Benchmark Support:All production lines now support fine-grained benchmarking, enabling measurement of end-to-end inference time as well as per-layer and per-module latency data to assist with performance analysis.Here'show to set up and use the benchmark feature.Documentation has been updated to include key metrics for commonly used configurations on mainstream hardware, such as inference latency and memory usage, providing deployment references for users.
* All production lines now support fine-grained benchmarking, enabling measurement of end-to-end inference time as well as per-layer and per-module latency data to assist with performance analysis.Here'show to set up and use the benchmark feature.
* Documentation has been updated to include key metrics for commonly used configurations on mainstream hardware, such as inference latency and memory usage, providing deployment references for users.
* Bug Fixes:Resolved the issue of failed log saving during model training.Upgraded the data augmentation component for formula models for compatibility with newer versions of the albumentations dependency, and fixed deadlock warnings when using the tokenizers package in multi-process scenarios.Fixed inconsistencies in switch behaviors (e.g.,use_chart_parsing) in the PP-StructureV3 configuration files compared to other pipelines.
* Resolved the issue of failed log saving during model training.
* Upgraded the data augmentation component for formula models for compatibility with newer versions of the albumentations dependency, and fixed deadlock warnings when using the tokenizers package in multi-process scenarios.
* Fixed inconsistencies in switch behaviors (e.g.,use_chart_parsing) in the PP-StructureV3 configuration files compared to other pipelines.
* Other Enhancements:Separated core and optional dependencies. Only minimal core dependencies are required for basic text recognition; additional dependencies for document parsing and information extraction can be installed as needed.Enabled support for NVIDIA RTX 50 series graphics cards on Windows; users can refer to theinstallation guidefor the corresponding PaddlePaddle framework versions.PP-OCR series models now support returning single-character coordinates.Added AIStudio, ModelScope, and other model download sources, allowing users to specify the source for model downloads.Added support for chart-to-table conversion via the PP-Chart2Table module.Optimized documentation descriptions to improve usability.
* Separated core and optional dependencies. Only minimal core dependencies are required for basic text recognition; additional dependencies for document parsing and information extraction can be installed as needed.
* Enabled support for NVIDIA RTX 50 series graphics cards on Windows; users can refer to theinstallation guidefor the corresponding PaddlePaddle framework versions.
* PP-OCR series models now support returning single-character coordinates.
* Added AIStudio, ModelScope, and other model download sources, allowing users to specify the source for model downloads.
* Added support for chart-to-table conversion via the PP-Chart2Table module.
* Optimized documentation descriptions to improve usability.

History Log

## 🚀 Quick Start

### Step 1: Try Online

PaddleOCR official website provides interactiveExperience CenterandAPIs—no setup required, just one click to experience.

👉Visit Official Website

### Step 2: Local Deployment

For local usage, please refer to the following documentation based on your needs:

* PP-OCR Series: SeePP-OCR Documentation
* PaddleOCR-VL Series: SeePaddleOCR-VL Documentation
* PP-StructureV3: SeePP-StructureV3 Documentation
* More Capabilities: SeeMore Capabilities Documentation

## 🧩 More Features

* Convert models to ONNX format:Obtaining ONNX Models.
* Accelerate inference using engines like OpenVINO, ONNX Runtime, TensorRT, or perform inference using ONNX format models:High-Performance Inference.
* Accelerate inference using multi-GPU and multi-process:Parallel Inference for Pipelines.
* Integrate PaddleOCR into applications written in C++, C#, Java, etc.:Serving.

## 🔄 Quick Overview of Execution Results

### PP-OCRv5

### PP-StructureV3

### PaddleOCR-VL

## ✨ Stay Tuned

⭐Star this repository to keep up with exciting updates and new releases, including powerful OCR and document parsing capabilities!⭐

## 👩‍👩‍👧‍👦 Community

PaddlePaddle WeChat official account

Join the tech discussion group

## 😃 Awesome Projects Leveraging PaddleOCR

PaddleOCR wouldn't be where it is today without its incredible community! 💗 A massive thank you to all our longtime partners, new collaborators, and everyone who's poured their passion into PaddleOCR — whether we've named you or not. Your support fuels our fire!

Project Name

Description

Dify


Production-ready platform for agentic workflow development.

RAGFlow


RAG engine based on deep document understanding.

pathway


Python ETL framework for stream processing, real-time analytics, LLM pipelines, and RAG.

MinerU


Multi-type Document to Markdown Conversion Tool

Umi-OCR


Free, Open-source, Batch Offline OCR Software.

cherry-studio


A desktop client that supports for multiple LLM providers.

haystack

AI orchestration framework to build customizable, production-ready LLM applications.

OmniParser

OmniParser: Screen Parsing tool for Pure Vision Based GUI Agent.

QAnything

Question and Answer based on Anything.

Learn more projects

More projects based on PaddleOCR

## 👩‍👩‍👧‍👦 Contributors

## 🌟 Star

## 📄 License

This project is released under theApache 2.0 license.

## 🎓 Citation

@misc
{
cui2025paddleocr30technicalreport
,

title
=
{
PaddleOCR 3.0 Technical Report
}
,

author
=
{
Cheng Cui and Ting Sun and Manhui Lin and Tingquan Gao and Yubo Zhang and Jiaxuan Liu and Xueqing Wang and Zelun Zhang and Changda Zhou and Hongen Liu and Yue Zhang and Wenyu Lv and Kui Huang and Yichao Zhang and Jing Zhang and Jun Zhang and Yi Liu and Dianhai Yu and Yanjun Ma
}
,

year
=
{
2025
}
,

eprint
=
{
2507.05595
}
,

archivePrefix
=
{
arXiv
}
,

primaryClass
=
{
cs.CV
}
,

url
=
{
https://arxiv.org/abs/2507.05595
}
,
}

@misc
{
cui2025paddleocrvlboostingmultilingualdocument
,

title
=
{
PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model
}
,

author
=
{
Cheng Cui and Ting Sun and Suyin Liang and Tingquan Gao and Zelun Zhang and Jiaxuan Liu and Xueqing Wang and Changda Zhou and Hongen Liu and Manhui Lin and Yue Zhang and Yubo Zhang and Handong Zheng and Jing Zhang and Jun Zhang and Yi Liu and Dianhai Yu and Yanjun Ma
}
,

year
=
{
2025
}
,

eprint
=
{
2510.14528
}
,

archivePrefix
=
{
arXiv
}
,

primaryClass
=
{
cs.CV
}
,

url
=
{
https://arxiv.org/abs/2510.14528
}
,
}

@misc
{
cui2026paddleocrvl15multitask09bvlm
,

title
=
{
PaddleOCR-VL-1.5: Towards a Multi-Task 0.9B VLM for Robust In-the-Wild Document Parsing
}
,

author
=
{
Cheng Cui and Ting Sun and Suyin Liang and Tingquan Gao and Zelun Zhang and Jiaxuan Liu and Xueqing Wang and Changda Zhou and Hongen Liu and Manhui Lin and Yue Zhang and Yubo Zhang and Yi Liu and Dianhai Yu and Yanjun Ma
}
,

year
=
{
2026
}
,

eprint
=
{
2601.21957
}
,

archivePrefix
=
{
arXiv
}
,

primaryClass
=
{
cs.CV
}
,

url
=
{
https://arxiv.org/abs/2601.21957
}
,
}

## About

Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages.

www.paddleocr.com

### Topics

 ocr

 pdf-parser

 kie

 document-translation

 rag

 chineseocr

 ai4science

 pp-ocr

 document-parsing

 pp-structure

 pdf-extractor-rag

 pdf2markdown

 paddleocr-vl

### Resources

 Readme



### License

 Apache-2.0 license


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

73.8k

 stars


### Watchers

531

 watching


### Forks

10.1k

 forks


 Report repository



## Releases29

v3.4.0

 Latest



Jan 29, 2026



+ 28 releases

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* Python76.8%
* C++14.1%
* Shell5.4%
* Java1.2%
* Dockerfile0.8%
* CMake0.4%
* Other1.3%
