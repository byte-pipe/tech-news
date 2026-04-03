---
title: 'GitHub - microsoft/BitNet: Official inference framework for 1-bit LLMs · GitHub'
url: https://github.com/microsoft/BitNet
site_name: hnrss
content_file: hnrss-github-microsoftbitnet-official-inference-framewor
fetched_at: '2026-03-12T03:14:07.359314'
original_url: https://github.com/microsoft/BitNet
date: '2026-03-11'
description: Official inference framework for 1-bit LLMs. Contribute to microsoft/BitNet development by creating an account on GitHub.
tags:
- hackernews
- hnrss
---

microsoft

 

/

BitNet

Public

* NotificationsYou must be signed in to change notification settings
* Fork2.5k
* Star29.5k

 
 
 
 
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

96 Commits
96 Commits
3rdparty
3rdparty
 
 
assets
assets
 
 
docs
docs
 
 
gpu
gpu
 
 
include
include
 
 
media
media
 
 
preset_kernels
preset_kernels
 
 
src
src
 
 
utils
utils
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
CMakeLists.txt
CMakeLists.txt
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
requirements.txt
requirements.txt
 
 
run_inference.py
run_inference.py
 
 
run_inference_server.py
run_inference_server.py
 
 
setup_env.py
setup_env.py
 
 
View all files

## Repository files navigation

# bitnet.cpp

Try it out via thisdemo, or build and run it on your ownCPUorGPU.

bitnet.cpp is the official inference framework for 1-bit LLMs (e.g., BitNet b1.58). It offers a suite of optimized kernels, that supportfastandlosslessinference of 1.58-bit models on CPU and GPU (NPU support will coming next).

The first release of bitnet.cpp is to support inference on CPUs. bitnet.cpp achieves speedups of1.37xto5.07xon ARM CPUs, with larger models experiencing greater performance gains. Additionally, it reduces energy consumption by55.4%to70.0%, further boosting overall efficiency. On x86 CPUs, speedups range from2.37xto6.17xwith energy reductions between71.9%to82.2%. Furthermore, bitnet.cpp can run a 100B BitNet b1.58 model on a single CPU, achieving speeds comparable to human reading (5-7 tokens per second), significantly enhancing the potential for running LLMs on local devices. Please refer to thetechnical reportfor more details.

Latest optimizationintroduces parallel kernel implementations with configurable tiling and embedding quantization support, achieving1.15x to 2.1xadditional speedup over the original implementation across different hardware platforms and workloads. For detailed technical information, see theoptimization guide.

## Demo

A demo of bitnet.cpp running a BitNet b1.58 3B model on Apple M2:

demo.mp4

## What's New:

* 01/15/2026BitNet CPU Inference Optimization
* 05/20/2025BitNet Official GPU inference kernel
* 04/14/2025BitNet Official 2B Parameter Model on Hugging Face
* 02/18/2025Bitnet.cpp: Efficient Edge Inference for Ternary LLMs
* 11/08/2024BitNet a4.8: 4-bit Activations for 1-bit LLMs
* 10/21/20241-bit AI Infra: Part 1.1, Fast and Lossless BitNet b1.58 Inference on CPUs
* 10/17/2024 bitnet.cpp 1.0 released.
* 03/21/2024The-Era-of-1-bit-LLMs__Training_Tips_Code_FAQ
* 02/27/2024The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits
* 10/17/2023BitNet: Scaling 1-bit Transformers for Large Language Models

## Acknowledgements

This project is based on thellama.cppframework. We would like to thank all the authors for their contributions to the open-source community. Also, bitnet.cpp's kernels are built on top of the Lookup Table methodologies pioneered inT-MAC. For inference of general low-bit LLMs beyond ternary models, we recommend using T-MAC.

## Official Models

Model

Parameters

CPU

Kernel

I2_S

TL1

TL2

BitNet-b1.58-2B-4T

2.4B

x86

✅

❌

✅

ARM

✅

✅

❌

## Supported Models

❗️We use existing 1-bit LLMs available onHugging Faceto demonstrate the inference capabilities of bitnet.cpp. We hope the release of bitnet.cpp will inspire the development of 1-bit LLMs in large-scale settings in terms of model size and training tokens.

Model

Parameters

CPU

Kernel

I2_S

TL1

TL2

bitnet_b1_58-large

0.7B

x86

✅

❌

✅

ARM

✅

✅

❌

bitnet_b1_58-3B

3.3B

x86

❌

❌

✅

ARM

❌

✅

❌

Llama3-8B-1.58-100B-tokens

8.0B

x86

✅

❌

✅

ARM

✅

✅

❌

Falcon3 Family

1B-10B

x86

✅

❌

✅

ARM

✅

✅

❌

Falcon-E Family

1B-3B

x86

✅

❌

✅

ARM

✅

✅

❌

## Installation

### Requirements

* python>=3.9
* cmake>=3.22
* clang>=18For Windows users, installVisual Studio 2022. In the installer, toggle on at least the following options(this also automatically installs the required additional tools like CMake):Desktop-development with C++C++-CMake Tools for WindowsGit for WindowsC++-Clang Compiler for WindowsMS-Build Support for LLVM-Toolset (clang)For Debian/Ubuntu users, you can download withAutomatic installation scriptbash -c "$(wget -O - https://apt.llvm.org/llvm.sh)"
* For Windows users, installVisual Studio 2022. In the installer, toggle on at least the following options(this also automatically installs the required additional tools like CMake):Desktop-development with C++C++-CMake Tools for WindowsGit for WindowsC++-Clang Compiler for WindowsMS-Build Support for LLVM-Toolset (clang)
* Desktop-development with C++
* C++-CMake Tools for Windows
* Git for Windows
* C++-Clang Compiler for Windows
* MS-Build Support for LLVM-Toolset (clang)
* For Debian/Ubuntu users, you can download withAutomatic installation scriptbash -c "$(wget -O - https://apt.llvm.org/llvm.sh)"
* conda (highly recommend)

### Build from source

Important

If you are using Windows, please remember to always use a Developer Command Prompt / PowerShell for VS2022 for the following commands. Please refer to the FAQs below if you see any issues.

1. Clone the repo

git clone --recursive https://github.com/microsoft/BitNet.git

cd
 BitNet

1. Install the dependencies

#
 (Recommended) Create a new conda environment

conda create -n bitnet-cpp python=3.9
conda activate bitnet-cpp

pip install -r requirements.txt

1. Build the project

#
 Manually download the model and run with local path

huggingface-cli download microsoft/BitNet-b1.58-2B-4T-gguf --local-dir models/BitNet-b1.58-2B-4T
python setup_env.py -md models/BitNet-b1.58-2B-4T -q i2_s

usage: setup_env.py [-h] [--hf-repo {1bitLLM/bitnet_b1_58-large,1bitLLM/bitnet_b1_58-3B,HF1BitLLM/Llama3-8B-1.58-100B-tokens,tiiuae/Falcon3-1B-Instruct-1.58bit,tiiuae/Falcon3-3B-Instruct-1.58bit,tiiuae/Falcon3-7B-Instruct-1.58bit,tiiuae/Falcon3-10B-Instruct-1.58bit}] [--model-dir MODEL_DIR] [--log-dir LOG_DIR] [--quant-type {i2_s,tl1}] [--quant-embd]
 [--use-pretuned]

Setup the environment for running inference

optional arguments:
 -h, --help show this help message and exit
 --hf-repo {1bitLLM/bitnet_b1_58-large,1bitLLM/bitnet_b1_58-3B,HF1BitLLM/Llama3-8B-1.58-100B-tokens,tiiuae/Falcon3-1B-Instruct-1.58bit,tiiuae/Falcon3-3B-Instruct-1.58bit,tiiuae/Falcon3-7B-Instruct-1.58bit,tiiuae/Falcon3-10B-Instruct-1.58bit}, -hr {1bitLLM/bitnet_b1_58-large,1bitLLM/bitnet_b1_58-3B,HF1BitLLM/Llama3-8B-1.58-100B-tokens,tiiuae/Falcon3-1B-Instruct-1.58bit,tiiuae/Falcon3-3B-Instruct-1.58bit,tiiuae/Falcon3-7B-Instruct-1.58bit,tiiuae/Falcon3-10B-Instruct-1.58bit}
 Model used for inference
 --model-dir MODEL_DIR, -md MODEL_DIR
 Directory to save/load the model
 --log-dir LOG_DIR, -ld LOG_DIR
 Directory to save the logging info
 --quant-type {i2_s,tl1}, -q {i2_s,tl1}
 Quantization type
 --quant-embd Quantize the embeddings to f16
 --use-pretuned, -p Use the pretuned kernel parameters

## Usage

### Basic usage

#
 Run inference with the quantized model

python run_inference.py -m models/BitNet-b1.58-2B-4T/ggml-model-i2_s.gguf -p 
"
You are a helpful assistant
"
 -cnv

usage: run_inference.py [-h] [-m MODEL] [-n N_PREDICT] -p PROMPT [-t THREADS] [-c CTX_SIZE] [-temp TEMPERATURE] [-cnv]

Run inference

optional arguments:
 -h, --help show this help message and exit
 -m MODEL, --model MODEL
 Path to model file
 -n N_PREDICT, --n-predict N_PREDICT
 Number of tokens to predict when generating text
 -p PROMPT, --prompt PROMPT
 Prompt to generate text from
 -t THREADS, --threads THREADS
 Number of threads to use
 -c CTX_SIZE, --ctx-size CTX_SIZE
 Size of the prompt context
 -temp TEMPERATURE, --temperature TEMPERATURE
 Temperature, a hyperparameter that controls the randomness of the generated text
 -cnv, --conversation Whether to enable chat mode or not (for instruct models.)
 (When this option is turned on, the prompt specified by -p will be used as the system prompt.)

### Benchmark

We provide scripts to run the inference benchmark providing a model.

usage: e2e_benchmark.py -m MODEL [-n N_TOKEN] [-p N_PROMPT] [-t THREADS] 
 
Setup the environment for running the inference 
 
required arguments: 
 -m MODEL, --model MODEL 
 Path to the model file. 
 
optional arguments: 
 -h, --help 
 Show this help message and exit. 
 -n N_TOKEN, --n-token N_TOKEN 
 Number of generated tokens. 
 -p N_PROMPT, --n-prompt N_PROMPT 
 Prompt to generate text from. 
 -t THREADS, --threads THREADS 
 Number of threads to use. 

Here's a brief explanation of each argument:

* -m,--model: The path to the model file. This is a required argument that must be provided when running the script.
* -n,--n-token: The number of tokens to generate during the inference. It is an optional argument with a default value of 128.
* -p,--n-prompt: The number of prompt tokens to use for generating text. This is an optional argument with a default value of 512.
* -t,--threads: The number of threads to use for running the inference. It is an optional argument with a default value of 2.
* -h,--help: Show the help message and exit. Use this argument to display usage information.

For example:

python utils/e2e_benchmark.py -m /path/to/model -n 200 -p 256 -t 4 

This command would run the inference benchmark using the model located at/path/to/model, generating 200 tokens from a 256 token prompt, utilizing 4 threads.

For the model layout that do not supported by any public model, we provide scripts to generate a dummy model with the given model layout, and run the benchmark on your machine:

python utils/generate-dummy-bitnet-model.py models/bitnet_b1_58-large --outfile models/dummy-bitnet-125m.tl1.gguf --outtype tl1 --model-size 125M

#
 Run benchmark with the generated model, use -m to specify the model path, -p to specify the prompt processed, -n to specify the number of token to generate

python utils/e2e_benchmark.py -m models/dummy-bitnet-125m.tl1.gguf -p 512 -n 128

### Convert from.safetensorsCheckpoints

#
 Prepare the .safetensors model file

huggingface-cli download microsoft/bitnet-b1.58-2B-4T-bf16 --local-dir ./models/bitnet-b1.58-2B-4T-bf16

#
 Convert to gguf model

python ./utils/convert-helper-bitnet.py ./models/bitnet-b1.58-2B-4T-bf16

### FAQ (Frequently Asked Questions)📌

#### Q1: The build dies with errors building llama.cpp due to issues with std::chrono in log.cpp?

A:This is an issue introduced in recent version of llama.cpp. Please refer to thiscommitin thediscussionto fix this issue.

#### Q2: How to build with clang in conda environment on windows?

A:Before building the project, verify your clang installation and access to Visual Studio tools by running:

clang -v

This command checks that you are using the correct version of clang and that the Visual Studio tools are available. If you see an error message such as:

'clang' is not recognized as an internal or external command, operable program or batch file.

It indicates that your command line window is not properly initialized for Visual Studio tools.

• If you are using Command Prompt, run:

"C:\Program Files\Microsoft Visual Studio\2022\Professional\Common7\Tools\VsDevCmd.bat" -startdir=none -arch=x64 -host_arch=x64

• If you are using Windows PowerShell, run the following commands:

Import-Module "C:\Program Files\Microsoft Visual Studio\2022\Professional\Common7\Tools\Microsoft.VisualStudio.DevShell.dll" Enter-VsDevShell 3f0e31ad -SkipAutomaticLocation -DevCmdArguments "-arch=x64 -host_arch=x64"

These steps will initialize your environment and allow you to use the correct Visual Studio tools.

## About

Official inference framework for 1-bit LLMs

### Resources

 Readme

 

### License

 MIT license
 

### Code of conduct

 Code of conduct
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

29.5k

 stars
 

### Watchers

266

 watching
 

### Forks

2.5k

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors16

+ 2 contributors

## Languages

* Python50.2%
* C++45.9%
* Shell2.9%
* Other1.0%