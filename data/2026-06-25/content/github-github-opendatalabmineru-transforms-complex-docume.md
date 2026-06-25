---
title: 'GitHub - opendatalab/MinerU: Transforms complex documents like PDFs and Office docs into LLM-ready markdown/JSON for your Agentic workflows. · GitHub'
url: https://github.com/opendatalab/MinerU
site_name: github
content_file: github-github-opendatalabmineru-transforms-complex-docume
fetched_at: '2026-06-25T11:55:59.638574'
original_url: https://github.com/opendatalab/MinerU
author: opendatalab
description: Transforms complex documents like PDFs and Office docs into LLM-ready markdown/JSON for your Agentic workflows. - opendatalab/MinerU
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 opendatalab

 

/

MinerU

Public

* NotificationsYou must be signed in to change notification settings
* Fork5.8k
* Star69.1k

 
 
 
 
master
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

5,687 Commits
5,687 Commits
.github
.github
 
 
demo
demo
 
 
docker
docker
 
 
docs
docs
 
 
mineru
mineru
 
 
projects
projects
 
 
tests
tests
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
LICENSE.md
LICENSE.md
 
 
MinerU_CLA.md
MinerU_CLA.md
 
 
README.md
README.md
 
 
README_zh-CN.md
README_zh-CN.md
 
 
SECURITY.md
SECURITY.md
 
 
mineru.template.json
mineru.template.json
 
 
mkdocs.yml
mkdocs.yml
 
 
pyproject.toml
pyproject.toml
 
 
update_version.py
update_version.py
 
 
View all files

## Repository files navigation

English|简体中文

🚀Access MinerU Now→✅ Zero-Install Web Version ✅ Full-Featured Desktop Client ✅ Instant API Access; Skip deployment headaches – get all product formats in one click. Developers, dive in!

👋 join us onDiscordandWeChat

MinerU — High-accuracy document parsing engine for LLM · RAG · Agent workflows

Converts PDF · DOCX · PPTX · XLSX · Images · Web pages into structured Markdown / JSON · VLM+OCR dual engine · 109 languages 

MCP Server · LangChain / Dify / FastGPT native integration · 10+ domestic AI chip support

🔍 Core Parsing Capabilities

* Native support forDOCX,PPTX, andXLSXparsing
* Formulas → LaTeX · Tables → HTML, accurate layout reconstruction
* Supports scanned docs, handwriting, multi-column layouts, cross-page table merging
* Output follows human reading order with automatic header/footer removal
* VLM + OCR dual engine, 109-language OCR recognition

🔌 Integration

Use Case

Solution

AI Coding Tools

MCP Server — Cursor · Claude Desktop · Windsurf

RAG Frameworks

LangChain · LlamaIndex · RAGFlow · RAG-Anything · Flowise · Dify · FastGPT

Development

Python / Go / TypeScript SDK · CLI · REST API · Docker

No-Code

mineru.net online · Gradio WebUI · Desktop client

🖥️ Deployment (Private · Fully Offline)

Inference Backend

Best For

pipeline

Fast & stable, no hallucination, runs on CPU or GPU

vlm-engine

High accuracy, supports vLLM / LMDeploy / mlx ecosystem

hybrid-engine

High accuracy, native text extraction, low hallucination

Domestic AI chips: Ascend · Cambricon · Enflame · MetaX · Moore Threads · Kunlunxin · Iluvatar · Hygon · Biren · T-Head

# Changelog

* 2026/06/18 3.4 ReleasedThis release focuses onOCR capability upgrades for the pipeline backend,OCR processing pipeline optimization, andmodel download experience improvements. The main updates include:OCR model upgrade and processing accelerationThe OCR model for thepipelinebackend has been upgraded toPP-OCRv6, improving OCR accuracy by about11%on OmniDocBench v1.6.Removed Japanese, Traditional Chinese, English, and Latin options from OCR language selection. These scenarios are now routed to thechOCR model, simplifying model configuration and language selection.Optimized the OCR inference and processing pipeline, increasing OCR processing speed by about100%and significantly improving parsing efficiency for batch documents and OCR-intensive documents.Model download logic optimizationAdded automatic model source selection, allowing first-time installations to choose a better model source based on the current network environment.Before downloading models, MinerU now prioritizes checking locally downloaded model cache files. Cache hits can be reused directly, reducing repeated downloads and unnecessary remote requests.For more details about model source configuration, automatic source selection, and local model usage, see theModel Source Documentation.With the 3.4 release, MinerU further improves the parsing accuracy and processing efficiency of thepipelinebackend in OCR scenarios. It also optimizes model downloads, cache reuse, and local configuration write-back, making first-time installation, model updates, and multi-environment deployment more stable and automated.
* OCR model upgrade and processing accelerationThe OCR model for thepipelinebackend has been upgraded toPP-OCRv6, improving OCR accuracy by about11%on OmniDocBench v1.6.Removed Japanese, Traditional Chinese, English, and Latin options from OCR language selection. These scenarios are now routed to thechOCR model, simplifying model configuration and language selection.Optimized the OCR inference and processing pipeline, increasing OCR processing speed by about100%and significantly improving parsing efficiency for batch documents and OCR-intensive documents.
* The OCR model for thepipelinebackend has been upgraded toPP-OCRv6, improving OCR accuracy by about11%on OmniDocBench v1.6.
* Removed Japanese, Traditional Chinese, English, and Latin options from OCR language selection. These scenarios are now routed to thechOCR model, simplifying model configuration and language selection.
* Optimized the OCR inference and processing pipeline, increasing OCR processing speed by about100%and significantly improving parsing efficiency for batch documents and OCR-intensive documents.
* Model download logic optimizationAdded automatic model source selection, allowing first-time installations to choose a better model source based on the current network environment.Before downloading models, MinerU now prioritizes checking locally downloaded model cache files. Cache hits can be reused directly, reducing repeated downloads and unnecessary remote requests.For more details about model source configuration, automatic source selection, and local model usage, see theModel Source Documentation.
* Added automatic model source selection, allowing first-time installations to choose a better model source based on the current network environment.
* Before downloading models, MinerU now prioritizes checking locally downloaded model cache files. Cache hits can be reused directly, reducing repeated downloads and unnecessary remote requests.
* For more details about model source configuration, automatic source selection, and local model usage, see theModel Source Documentation.
* 2026/06/11 3.3 ReleasedThis release focuses onHybrid parsing performance optimizationandVLM model capability upgrades. The main updates include:Neweffortparsing-strength parameter for the Hybrid backendAdded two parsing-strength levels,mediumandhigh, allowing users to balance parsing speed, parsing accuracy, and feature requirements.On OmniDocBench v1.6,mediumreduces overall accuracy by only0.13points compared withhigh, while delivering35%~220%parsing speed improvements across different devices and scenarios:Linux: about80%faster for text PDF scenarios and about35%faster for OCR scenariosWindows: about90%faster for text PDF scenarios and about45%faster for OCR scenariosmacOS: about220%faster for text PDF scenarios and about50%faster for OCR scenariosThe default Hybrid backend now useseffort=medium, significantly improving overall parsing efficiency while maintaining high parsing accuracy.Themediumlevel does not supportimage analysis; for maximum parsing accuracy orimage analysissupport, switch to the high-strength parsing mode witheffort=high, which may have an impact on parsing speed.VLM model upgraded toMinerU2.5-Pro-2605-1.2BFixed multiple model issues found in the2604version, further improving parsing stability on complex documents.Added native multilingual OCR support, reducing the need for extra language-parameter configuration and improving out-of-the-box usability for multilingual documents.With the 3.3 release, MinerU further improves Hybrid backend efficiency across platforms and scenarios while maintaining high-accuracy parsing. The defaultmediumeffort level is better suited for most day-to-day document processing tasks, whilehighis designed for scenarios that require maximum parsing accuracy orimage analysiscapabilities.
* Neweffortparsing-strength parameter for the Hybrid backendAdded two parsing-strength levels,mediumandhigh, allowing users to balance parsing speed, parsing accuracy, and feature requirements.On OmniDocBench v1.6,mediumreduces overall accuracy by only0.13points compared withhigh, while delivering35%~220%parsing speed improvements across different devices and scenarios:Linux: about80%faster for text PDF scenarios and about35%faster for OCR scenariosWindows: about90%faster for text PDF scenarios and about45%faster for OCR scenariosmacOS: about220%faster for text PDF scenarios and about50%faster for OCR scenariosThe default Hybrid backend now useseffort=medium, significantly improving overall parsing efficiency while maintaining high parsing accuracy.Themediumlevel does not supportimage analysis; for maximum parsing accuracy orimage analysissupport, switch to the high-strength parsing mode witheffort=high, which may have an impact on parsing speed.
* Added two parsing-strength levels,mediumandhigh, allowing users to balance parsing speed, parsing accuracy, and feature requirements.
* On OmniDocBench v1.6,mediumreduces overall accuracy by only0.13points compared withhigh, while delivering35%~220%parsing speed improvements across different devices and scenarios:Linux: about80%faster for text PDF scenarios and about35%faster for OCR scenariosWindows: about90%faster for text PDF scenarios and about45%faster for OCR scenariosmacOS: about220%faster for text PDF scenarios and about50%faster for OCR scenarios
* Linux: about80%faster for text PDF scenarios and about35%faster for OCR scenarios
* Windows: about90%faster for text PDF scenarios and about45%faster for OCR scenarios
* macOS: about220%faster for text PDF scenarios and about50%faster for OCR scenarios
* The default Hybrid backend now useseffort=medium, significantly improving overall parsing efficiency while maintaining high parsing accuracy.
* Themediumlevel does not supportimage analysis; for maximum parsing accuracy orimage analysissupport, switch to the high-strength parsing mode witheffort=high, which may have an impact on parsing speed.
* VLM model upgraded toMinerU2.5-Pro-2605-1.2BFixed multiple model issues found in the2604version, further improving parsing stability on complex documents.Added native multilingual OCR support, reducing the need for extra language-parameter configuration and improving out-of-the-box usability for multilingual documents.
* Fixed multiple model issues found in the2604version, further improving parsing stability on complex documents.
* Added native multilingual OCR support, reducing the need for extra language-parameter configuration and improving out-of-the-box usability for multilingual documents.
* 2026/04/18 3.1.0 ReleasedThis release focuses onlicensing openness, parsing accuracy, and full-format native support. The main updates include:License upgradeMinerU has officially moved fromAGPLv3to theMinerU Open Source License, a custom license based onApache 2.0.This change significantly reduces adoption friction for both community users and commercial deployments, making MinerU easier to integrate into real-world workflows.VLM main model upgradeThe primary VLM model has been upgraded toMinerU2.5-Pro-2604-1.2B, bringing overall parsing accuracy to a state-of-the-art level.The new model now supports image and chart parsing, truncated paragraph merging, cross-page table merging, and image recognition inside tables, further strengthening performance on complex document layouts.Full-format native parsing supportNative parsing support has now been extended toPPTXandXLSX.MinerU now fully supports parsing across images,PDF,DOCX,PPTX, andXLSX, providing a more complete multi-format document understanding workflow.With the 3.1.0 release, MinerU becomes more open, more accurate, and easier to adopt in production. The new license lowers the barrier for both community and commercial use,MinerU2.5-Pro-2604-1.2Bimproves parsing quality on complex content, and nativePPTX/XLSXsupport completes end-to-end coverage of mainstream document formats.
* License upgradeMinerU has officially moved fromAGPLv3to theMinerU Open Source License, a custom license based onApache 2.0.This change significantly reduces adoption friction for both community users and commercial deployments, making MinerU easier to integrate into real-world workflows.
* MinerU has officially moved fromAGPLv3to theMinerU Open Source License, a custom license based onApache 2.0.
* This change significantly reduces adoption friction for both community users and commercial deployments, making MinerU easier to integrate into real-world workflows.
* VLM main model upgradeThe primary VLM model has been upgraded toMinerU2.5-Pro-2604-1.2B, bringing overall parsing accuracy to a state-of-the-art level.The new model now supports image and chart parsing, truncated paragraph merging, cross-page table merging, and image recognition inside tables, further strengthening performance on complex document layouts.
* The primary VLM model has been upgraded toMinerU2.5-Pro-2604-1.2B, bringing overall parsing accuracy to a state-of-the-art level.
* The new model now supports image and chart parsing, truncated paragraph merging, cross-page table merging, and image recognition inside tables, further strengthening performance on complex document layouts.
* Full-format native parsing supportNative parsing support has now been extended toPPTXandXLSX.MinerU now fully supports parsing across images,PDF,DOCX,PPTX, andXLSX, providing a more complete multi-format document understanding workflow.
* Native parsing support has now been extended toPPTXandXLSX.
* MinerU now fully supports parsing across images,PDF,DOCX,PPTX, andXLSX, providing a more complete multi-format document understanding workflow.
* 2026/03/29 3.0.0 ReleasedThis release delivers a systematic upgrade centered onparsing capability, system architecture, and engineering usability. The main updates include:NativeDOCXparsingOfficial support for nativeDOCXparsing, delivering high-precision results without hallucinations.Compared with the traditional workflow of first convertingDOCXtoPDFand then parsing it, end-to-end speed is improved by tens of times, making it better suited for scenarios with high requirements for both accuracy and throughput.pipelinebackend upgradeThepipelinebackend achieves a score of86.2on OmniDocBench (v1.5), surpassing the accuracy of the previous-generation mainstream VLMMinerU2.0-2505-0.9B.Added support for parsing images/formulas inside tables, seal text recognition, vertical text support, and interline formula numbering recognition, continuously improving parsing quality for complex document scenarios.While maintaining high accuracy, it keeps resource usage extremely low and continues to support inference in pure CPU environments.API / CLI / Routerorchestration upgrademinerunow runs as an orchestration client based onmineru-api; when--api-urlis not provided, it will automatically start a local temporary service.mineru-apiadds a new asynchronous task endpointPOST /tasks, supporting task submission, status querying, and result retrieval; meanwhile, it retains the synchronous parsing endpointPOST /file_parsefor compatibility with legacy plugins.Addedmineru-router, designed for unified entry deployment and task routing across multiple services and multiple GPUs; its interfaces are fully compatible withmineru-apiand support automatic task load balancing.Deployment and usability improvementsResolved compatibility issues withtorch >= 2.8; the base image has been upgraded tovllm0.11.2 + torch2.9.0, unifying installation paths across different Compute Capabilities.Optimized the parsing pipeline with a sliding-window mechanism, significantly reducing peak memory usage in long-document scenarios, so documents with tens of thousands of pages no longer need to be split manually.Batch inference inpipelinenow supports streaming writes to disk, allowing completed parsing results to be written out in time and further improving the experience for long-running tasks.Completed thread-safety optimization and now fully supports multi-threaded concurrent inference; together withmineru-router, this enables one-click multi-GPU deployment and makes it easy to build high-concurrency, high-throughput parsing systems.Completely removed the use of two AGPLv3 models (doclayoutyoloandmfd_yolov8) and one CC-BY-NC-SA 4.0 model (layoutreader).This update is not just a set of feature enhancements, but a key leap forward in MinerU's overall system capabilities. We specifically addressed the peak memory usage issue in long-document parsing. Through optimizations such as sliding windows and streaming writes to disk, ultra-long document parsing has moved from “requiring manual splitting and careful handling” to being “stable, scalable, and ready for production workloads.” At the same time, we completed thread-safety optimization and fully enabled multi-threaded concurrent inference, further improving single-machine resource utilization and runtime stability under high-concurrency workloads. On top of this, withmineru-routerand the newAPI / CLIorchestration framework, MinerU now supports one-click multi-GPU deployment, unified access across multiple services, and automatic task load balancing, significantly reducing the difficulty of large-scale deployment. As a result, MinerU is evolving from a standalone data production tool into a large-scale document parsing foundation for high-concurrency and high-throughput scenarios, providing enterprise-grade document data processing with infrastructure that is more stable, more efficient, and easier to scale.
* NativeDOCXparsingOfficial support for nativeDOCXparsing, delivering high-precision results without hallucinations.Compared with the traditional workflow of first convertingDOCXtoPDFand then parsing it, end-to-end speed is improved by tens of times, making it better suited for scenarios with high requirements for both accuracy and throughput.
* Official support for nativeDOCXparsing, delivering high-precision results without hallucinations.
* Compared with the traditional workflow of first convertingDOCXtoPDFand then parsing it, end-to-end speed is improved by tens of times, making it better suited for scenarios with high requirements for both accuracy and throughput.
* pipelinebackend upgradeThepipelinebackend achieves a score of86.2on OmniDocBench (v1.5), surpassing the accuracy of the previous-generation mainstream VLMMinerU2.0-2505-0.9B.Added support for parsing images/formulas inside tables, seal text recognition, vertical text support, and interline formula numbering recognition, continuously improving parsing quality for complex document scenarios.While maintaining high accuracy, it keeps resource usage extremely low and continues to support inference in pure CPU environments.
* Thepipelinebackend achieves a score of86.2on OmniDocBench (v1.5), surpassing the accuracy of the previous-generation mainstream VLMMinerU2.0-2505-0.9B.
* Added support for parsing images/formulas inside tables, seal text recognition, vertical text support, and interline formula numbering recognition, continuously improving parsing quality for complex document scenarios.
* While maintaining high accuracy, it keeps resource usage extremely low and continues to support inference in pure CPU environments.
* API / CLI / Routerorchestration upgrademinerunow runs as an orchestration client based onmineru-api; when--api-urlis not provided, it will automatically start a local temporary service.mineru-apiadds a new asynchronous task endpointPOST /tasks, supporting task submission, status querying, and result retrieval; meanwhile, it retains the synchronous parsing endpointPOST /file_parsefor compatibility with legacy plugins.Addedmineru-router, designed for unified entry deployment and task routing across multiple services and multiple GPUs; its interfaces are fully compatible withmineru-apiand support automatic task load balancing.
* minerunow runs as an orchestration client based onmineru-api; when--api-urlis not provided, it will automatically start a local temporary service.
* mineru-apiadds a new asynchronous task endpointPOST /tasks, supporting task submission, status querying, and result retrieval; meanwhile, it retains the synchronous parsing endpointPOST /file_parsefor compatibility with legacy plugins.
* Addedmineru-router, designed for unified entry deployment and task routing across multiple services and multiple GPUs; its interfaces are fully compatible withmineru-apiand support automatic task load balancing.
* Deployment and usability improvementsResolved compatibility issues withtorch >= 2.8; the base image has been upgraded tovllm0.11.2 + torch2.9.0, unifying installation paths across different Compute Capabilities.Optimized the parsing pipeline with a sliding-window mechanism, significantly reducing peak memory usage in long-document scenarios, so documents with tens of thousands of pages no longer need to be split manually.Batch inference inpipelinenow supports streaming writes to disk, allowing completed parsing results to be written out in time and further improving the experience for long-running tasks.Completed thread-safety optimization and now fully supports multi-threaded concurrent inference; together withmineru-router, this enables one-click multi-GPU deployment and makes it easy to build high-concurrency, high-throughput parsing systems.Completely removed the use of two AGPLv3 models (doclayoutyoloandmfd_yolov8) and one CC-BY-NC-SA 4.0 model (layoutreader).
* Resolved compatibility issues withtorch >= 2.8; the base image has been upgraded tovllm0.11.2 + torch2.9.0, unifying installation paths across different Compute Capabilities.
* Optimized the parsing pipeline with a sliding-window mechanism, significantly reducing peak memory usage in long-document scenarios, so documents with tens of thousands of pages no longer need to be split manually.
* Batch inference inpipelinenow supports streaming writes to disk, allowing completed parsing results to be written out in time and further improving the experience for long-running tasks.
* Completed thread-safety optimization and now fully supports multi-threaded concurrent inference; together withmineru-router, this enables one-click multi-GPU deployment and makes it easy to build high-concurrency, high-throughput parsing systems.
* Completely removed the use of two AGPLv3 models (doclayoutyoloandmfd_yolov8) and one CC-BY-NC-SA 4.0 model (layoutreader).

📝 View the completeChangelogfor more historical version information

# MinerU

## Project Introduction

MinerU is a document parsing tool that convertsPDF, image,DOCX,PPTX, andXLSXinputs into machine-readable formats such as Markdown and JSON for downstream retrieval, extraction, and processing.
MinerU was born during the pre-training process ofInternLM. We focus on solving symbol conversion issues in scientific literature and hope to contribute to technological development in the era of large models.
Compared to well-known commercial products, MinerU is still young. If you encounter any issues or if the results are not as expected, please submit an issue onissueandattach the relevant document or sample file.

pdf_zh_cn.mp4

## Key Features

* SupportPDF, image,DOCX,PPTX, andXLSXinputs.
* Remove headers, footers, footnotes, page numbers, etc., to ensure semantic coherence.
* Output text in human-readable order, suitable for single-column, multi-column, and complex layouts.
* Preserve the structure of the original document, including headings, paragraphs, lists, etc.
* Extract images, image descriptions, tables, table titles, and footnotes.
* Automatically recognize and convert formulas in the document to LaTeX format.
* Automatically recognize and convert tables in the document to HTML format.
* Automatically detect scanned PDFs and garbled PDFs and enable OCR functionality.
* OCR supports detection and recognition of 109 languages.
* Supports multiple output formats, such as multimodal and NLP Markdown, JSON sorted by reading order, and rich intermediate formats.
* Supports various visualization results, including layout visualization and span visualization, for efficient confirmation of output quality.
* Built-in CLI, FastAPI, Gradio WebUI, for local orchestration and multi-service deployment.
* Supports running in a pure CPU environment, and also supports GPU/MPS acceleration
* Compatible with Windows, Linux, and Mac platforms.

# Quick Start

Document parsing is a difficult and complex task. In scenarios such as complex layouts, scanned pages, and handwritten content, the parsing results may fall short of expectations. We recommend trying the online demo first to evaluate MinerU's parsing quality and suitability before choosing an appropriate deployment method based on your actual needs.
If you havedocumentsamples with unsatisfactory parsing results, feel free to share them in anissue. We will continue improving the parsing capabilities.
If you encounter any installation issues, please first consult theFAQ.

## Online Experience

### Official online web application

The official online version has the same functionality as the client, with a beautiful interface and rich features, requires login to use

### Gradio-based online demo

A WebUI developed based on Gradio, with a simple interface and only core parsing functionality, no login required

## Local Deployment

Warning

Pre-installation Notice—Hardware and Software Environment Support

To ensure the stability and reliability of the project, we only optimize and test for specific hardware and software environments during development. This ensures that users deploying and running the project on recommended system configurations will get the best performance with the fewest compatibility issues.

By focusing resources on the mainline environment, our team can more efficiently resolve potential bugs and develop new features.

In non-mainline environments, due to the diversity of hardware and software configurations, as well as third-party dependency compatibility issues, we cannot guarantee 100% project availability. Therefore, for users who wish to use this project in non-recommended environments, we suggest carefully reading the documentation and FAQ first. Most issues already have corresponding solutions in the FAQ. We also encourage community feedback to help us gradually expand support.

Parsing Backend

pipeline

*-engine

*-http-client

hybrid

vlm

hybrid

vlm

Backend Features

Good Compatibility

High Hardware Requirements

For OpenAI Compatible Servers
2

Accuracy
1

86.47

95.39 (high)
95.26 (medium)

95.30

95.39 (high)
95.26 (medium)

95.30

Operating System

Linux
3
 / Windows
4
 / macOS
5

Pure CPU Support

✅

❌

✅

GPU Acceleration

Volta and later architecture GPUs or Apple Silicon

Not Required

Min VRAM

4GB

8GB

2GB

RAM

Min 16GB, Recommended 32GB or more

Min 16GB

Disk Space

Min 20GB, SSD Recommended

Min 2GB

Python Version

3.10-3.13

1Accuracy metrics are the End-to-End Evaluation Overall scores from OmniDocBench (v1.6), based on the latest version ofMinerU.2Servers compatible with OpenAI API, such as local model servers or remote model services deployed via inference frameworks likevLLM/SGLang/LMDeploy.3Linux only supports distributions from 2019 and later.4Since the key dependencyraydoes not support Python 3.13 on Windows, only versions 3.10~3.12 are supported.5macOS requires version 14.0 or later.

### Install MinerU

#### Install MinerU using pip or uv

pip install --upgrade pip
pip install uv
uv pip install -U 
"
mineru[all]
"

#### Install MinerU from source code

git clone https://github.com/opendatalab/MinerU.git

cd
 MinerU
uv pip install -e .[all]

Tip

* mineru[all]includes all core features, compatible with Windows / Linux / macOS systems, suitable for most users.
* If CUDA acceleration is unavailable after installing on Windows, see theWindows CUDA acceleration FAQ.
* If you need to specify the inference framework for the VLM model, or only intend to install a lightweight client on an edge device, please refer to the documentationExtension Modules Installation Guide.

#### Deploy MinerU using Docker

MinerU provides a convenient Docker deployment method, which helps quickly set up the environment and solve some tricky environment compatibility issues.

Tip

* Docker deployment is only supported on Linux and Windows environments with WSL2 support;
* macOS users should refer to the two installation methods above for installation instead of using Docker deployment.

You can get theDocker Deployment Instructionsin the documentation.

### Using MinerU

If your device meets the GPU acceleration requirements in the table above, you can use a simple command line for document parsing:

mineru -p 
<
input_path
>
 -o 
<
output_path
>

If your device does not meet the GPU acceleration requirements, you can specify the backend aspipelineto run in a pure CPU environment:

mineru -p 
<
input_path
>
 -o 
<
output_path
>
 -b pipeline

minerucurrently supports localPDF, image,DOCX,PPTX, andXLSXfile or directory inputs, and can be used for document parsing through the CLI, API, WebUI, andmineru-router. For detailed instructions, please refer to theUsage Guide.

# FAQ

* If you encounter any issues during usage, you can first check theFAQfor solutions.
* If your issue remains unresolved, you may also useDeepWikito interact with an AI assistant, which can address most common problems.
* If you still cannot resolve the issue, you are welcome to join our community viaDiscordorWeChatto discuss with other users and developers.

# All Thanks To Our Contributors

# License Information

This repository is licensed under theMinerU Open Source License, based on Apache 2.0 with additional conditions.

# Acknowledgments

* UniMERNet
* TableStructureRec
* PaddleOCR
* PaddleOCR2Pytorch
* fast-langdetect
* pypdfium2
* pdftext
* pypdf
* magika
* vLLM
* LMDeploy

# Citation

@article
{
wang2026mineru2
,
 
title
=
{
MinerU2. 5-Pro: Pushing the Limits of Data-Centric Document Parsing at Scale
}
,
 
author
=
{
Wang, Bin and He, Tianyao and Ouyang, Linke and Wu, Fan and Zhao, Zhiyuan and Chu, Tao and Qu, Yuan and Jin, Zhenjiang and Zeng, Weijun and Miao, Ziyang and others
}
,
 
journal
=
{
arXiv preprint arXiv:2604.04771
}
,
 
year
=
{
2026
}

}

@article
{
dong2026minerudiffusion
,
 
title
=
{
MinerU-Diffusion: Rethinking Document OCR as Inverse Rendering via Diffusion Decoding
}
,
 
author
=
{
Dong, Hejun and Niu, Junbo and Wang, Bin and Zeng, Weijun and Zhang, Wentao and He, Conghui
}
,
 
journal
=
{
arXiv preprint arXiv:2603.22458
}
,
 
year
=
{
2026
}

}

@article
{
niu2025mineru2
,
 
title
=
{
Mineru2. 5: A decoupled vision-language model for efficient high-resolution document parsing
}
,
 
author
=
{
Niu, Junbo and Liu, Zheng and Gu, Zhuangcheng and Wang, Bin and Ouyang, Linke and Zhao, Zhiyuan and Chu, Tao and He, Tianyao and Wu, Fan and Zhang, Qintong and others
}
,
 
journal
=
{
arXiv preprint arXiv:2509.22186
}
,
 
year
=
{
2025
}

}

@article
{
wang2024mineru
,
 
title
=
{
Mineru: An open-source solution for precise document content extraction
}
,
 
author
=
{
Wang, Bin and Xu, Chao and Zhao, Xiaomeng and Ouyang, Linke and Wu, Fan and Zhao, Zhiyuan and Xu, Rui and Liu, Kaiwen and Qu, Yuan and Shang, Fukai and others
}
,
 
journal
=
{
arXiv preprint arXiv:2409.18839
}
,
 
year
=
{
2024
}

}

@article
{
he2024opendatalab
,
 
title
=
{
Opendatalab: Empowering general artificial intelligence with open datasets
}
,
 
author
=
{
He, Conghui and Li, Wei and Jin, Zhenjiang and Xu, Chao and Wang, Bin and Lin, Dahua
}
,
 
journal
=
{
arXiv preprint arXiv:2407.13773
}
,
 
year
=
{
2024
}

}

# Star History

# Links

* MinerU-Diffusion: Rethinking Document OCR as Inverse Rendering via Diffusion Decoding
* Easy Data Preparation with latest LLMs-based Operators and Pipelines
* Vis3 (OSS browser based on s3)
* LabelU (A Lightweight Multi-modal Data Annotation Tool)
* LabelLLM (An Open-source LLM Dialogue Annotation Platform)
* PDF-Extract-Kit (A Comprehensive Toolkit for High-Quality PDF Content Extraction)
* OmniDocBench (A Comprehensive Benchmark for Document Parsing and Evaluation)
* Magic-HTML (Mixed web page extraction tool)
* Magic-Doc (Fast speed ppt/pptx/doc/docx/pdf extraction tool)
* Dingo: A Comprehensive AI Data Quality Evaluation Tool

## About

Transforms complex documents like PDFs and Office docs into LLM-ready markdown/JSON for your Agentic workflows.

opendatalab.github.io/MinerU/

### Topics

 python

 pdf

 parser

 ocr

 xlsx

 pdf-converter

 docx

 pptx

 extract-data

 document-analysis

 pdf-parser

 layout-analysis

 ai4science

 pdf-extractor-rag

 pdf-extractor-llm

 pdf-extractor-pretrain

### Resources

 Readme

 

### License

 View license
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

69.1k

 stars
 

### Watchers

252

 watching
 

### Forks

5.8k

 forks
 

 Report repository

 

## Releases175

mineru-3.4.0-released

 Latest

 

Jun 18, 2026

 

+ 174 releases

## Used by154

 + 146
 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python99.3%
* Dockerfile0.7%