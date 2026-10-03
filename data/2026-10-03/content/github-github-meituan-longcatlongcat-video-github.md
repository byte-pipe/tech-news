---
title: GitHub - meituan-longcat/LongCat-Video · GitHub
url: https://github.com/meituan-longcat/LongCat-Video
site_name: github
content_file: github-github-meituan-longcatlongcat-video-github
fetched_at: '2026-10-03T15:04:10.025510'
original_url: https://github.com/meituan-longcat/LongCat-Video
author: meituan-longcat
description: Contribute to meituan-longcat/LongCat-Video development by creating an account on GitHub.
---

meituan-longcat

 

/

LongCat-Video

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.5k
* Star8.6k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

63 Commits
63 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
assets
assets
 
 
longcat_video
longcat_video
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
requirements.txt
requirements.txt
 
 
requirements_avatar.txt
requirements_avatar.txt
 
 
run_demo_avatar_multi_audio_to_video.py
run_demo_avatar_multi_audio_to_video.py
 
 
run_demo_avatar_single_audio_to_video.py
run_demo_avatar_single_audio_to_video.py
 
 
run_demo_image_to_video.py
run_demo_image_to_video.py
 
 
run_demo_interactive_video.py
run_demo_interactive_video.py
 
 
run_demo_long_video.py
run_demo_long_video.py
 
 
run_demo_text_to_video.py
run_demo_text_to_video.py
 
 
run_demo_video_continuation.py
run_demo_video_continuation.py
 
 
run_streamlit.py
run_streamlit.py
 
 
View all files

## Repository files navigation

# LongCat-Video

## Model Introduction

We introduce LongCat-Video, a foundational video generation model with 13.6B parameters, delivering strong performance acrossText-to-Video,Image-to-Video, andVideo-Continuationgeneration tasks. It particularly excels in efficient and high-quality long video generation, representing our first step toward world models.

### Key Features

* 🌟Unified architecture for multiple tasks: LongCat-Video unifiesText-to-Video,Image-to-Video, andVideo-Continuationtasks within a single video generation framework. It natively supports all these tasks with a single model and consistently delivers strong performance across each individual task.
* 🌟Long video generation: LongCat-Video is natively pretrained onVideo-Continuationtasks, enabling it to produce minutes-long videos without color drifting or quality degradation.
* 🌟Efficient inference: LongCat-Video generates$720p$,$30fps$videos within minutes by employing a coarse-to-fine generation strategy along both the temporal and spatial axes. Block Sparse Attention further enhances efficiency, particularly at high resolutions
* 🌟Strong performance with multi-reward RLHF: Powered by multi-reward Group Relative Policy Optimization (GRPO), comprehensive evaluations on both internal and public benchmarks demonstrate that LongCat-Video achieves performance comparable to leading open-source video generation models as well as the latest commercial solutions.

For more detail, please refer to the comprehensiveLongCat-Video Technical Report.

## 🎥 Teaser Video

teaser_video_1min_0p5size.mp4

## 🔥 Latest News!!

* May 21, 2026: 🚀 We releaseLongCat-Video-Avatar-1.5, an upgraded open-source framework for audio-driven human video generation. v1.5 replaces Wav2Vec2 with Whisper-Large for more accurate lip synchronization, achieves production-ready physical rationality and temporal stability with robust long-video generation, generalizes to stylized domains (anime, animals, complex real-world conditions), supports both single-stream and multi-stream audio inputs, and accelerates inference to 8 steps via step distillation. [code| 🤗weights|project page]
* Dec 16, 2025: 🚀 We are excited to announce the release ofLongCat-Video-Avatar, a unified model that delivers expressive and highly dynamic audio-driven character animation, supporting native tasks includingAudio-Text-to-Video,Audio-Text-Image-to-Video, andVideo Continuationwith seamless compatibility for bothsingle-streamandmulti-streamaudio inputs. The release includes ourTechnical Report,inference code, 🤗model weights, andproject page.
* Oct 25, 2025: 🚀 We've released LongCat-Video, a foundational video generation model. Tech report and models are available atLongCat-Video Technical Reportand 🤗Huggingface!

## Quick Start

### Installation

Clone the repo:

git clone --single-branch --branch main https://github.com/meituan-longcat/LongCat-Video

cd
 LongCat-Video

Install dependencies:

#
 create conda environment

conda create -n longcat-video python=3.10
conda activate longcat-video

#
 install torch (configure according to your CUDA version)

pip install torch==2.6.0+cu124 torchvision==0.21.0+cu124 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu124

#
 install flash-attn-2

pip install ninja 
pip install psutil 
pip install packaging 
pip install flash_attn==2.7.4.post1

#
 install other requirements

pip install -r requirements.txt

#
 install longcat-video-avatar requirements

conda install -c conda-forge librosa
conda install -c conda-forge ffmpeg
pip install -r requirements_avatar.txt

FlashAttention-2 is enabled in the model config by default; you can also change the model config ("./weights/LongCat-Video/dit/config.json") to use FlashAttention-3 or xformers once installed.

### Model Download

Models

Description

Download Link

LongCat-Video

foundational video generation

🤗 
Huggingface

LongCat-Video-Avatar

single- and multi-character audio-driven video generation (wav2vec2)

🤗 
Huggingface

LongCat-Video-Avatar-1.5

upgraded avatar model with Whisper-large-v3 audio encoder, distillation-based fast inference

🤗 
Huggingface

Download models using huggingface-cli:

pip install 
"
huggingface_hub[cli]
"

huggingface-cli download meituan-longcat/LongCat-Video --local-dir ./weights/LongCat-Video
huggingface-cli download meituan-longcat/LongCat-Video-Avatar --local-dir ./weights/LongCat-Video-Avatar
huggingface-cli download meituan-longcat/LongCat-Video-Avatar-1.5 --local-dir ./weights/LongCat-Video-Avatar-1.5

### Run Text-to-Video

#
 Single-GPU inference

torchrun run_demo_text_to_video.py --checkpoint_dir=./weights/LongCat-Video --enable_compile

#
 Multi-GPU inference

torchrun --nproc_per_node=2 run_demo_text_to_video.py --context_parallel_size=2 --checkpoint_dir=./weights/LongCat-Video --enable_compile

### Run Image-to-Video

#
 Single-GPU inference

torchrun run_demo_image_to_video.py --checkpoint_dir=./weights/LongCat-Video --enable_compile

#
 Multi-GPU inference

torchrun --nproc_per_node=2 run_demo_image_to_video.py --context_parallel_size=2 --checkpoint_dir=./weights/LongCat-Video --enable_compile

### Run Video-Continuation

#
 Single-GPU inference

torchrun run_demo_video_continuation.py --checkpoint_dir=./weights/LongCat-Video --enable_compile

#
 Multi-GPU inference

torchrun --nproc_per_node=2 run_demo_video_continuation.py --context_parallel_size=2 --checkpoint_dir=./weights/LongCat-Video --enable_compile

### Run Long-Video Generation

#
 Single-GPU inference

torchrun run_demo_long_video.py --checkpoint_dir=./weights/LongCat-Video --enable_compile

#
 Multi-GPU inference

torchrun --nproc_per_node=2 run_demo_long_video.py --context_parallel_size=2 --checkpoint_dir=./weights/LongCat-Video --enable_compile

### Run Interactive Video Generation

#
 Single-GPU inference

torchrun run_demo_interactive_video.py --checkpoint_dir=./weights/LongCat-Video --enable_compile

#
 Multi-GPU inference

torchrun --nproc_per_node=2 run_demo_interactive_video.py --context_parallel_size=2 --checkpoint_dir=./weights/LongCat-Video --enable_compile

### Run LongCat-Video-Avatar

💡 User tips for 1.5

* Lip synchronization accuracy:Audio CFG works optimally between 3–5. Increase the audio CFG value for better synchronization.
* Prompt Enhancement:Longer, more descriptive prompts yield better consistency and naturalness than short ones. We recommend including rich details such as character appearance, actions, and scene context (e.g.,"A young woman with long black hair is speaking and smiling, wearing a white blouse, sitting in a bright café") for best results.
* Mitigate repeated actions:Setting the reference image index（--ref_img_index, default to 10） between 0 and 24 ensures better consistency; setting it to 30 helps reduce repeated actions. Additionally, increasing the mask frame range (--mask_frame_range, default to 3) can further help mitigate repeated actions, but excessively large values may introduce artifacts.
* Super resolution:Our model is compatible with both 480P and 720P, which can be controlled via --resolution.
* Dual-Audio Modes:Merge mode (set audio_type to para) requires two audio clips of equal length, and the resulting audio is obtained by summing the two clips; Concatenation mode (set audio_type to add) does not require equal-length inputs, and the resulting audio is formed by sequentially concatenating the two clips with silence padding for any gaps, where by default person1 speaks first and person2 speaks afterward.
* Model versions:--model_type avatar-v1.0uses wav2vec2 audio encoder (default);--model_type avatar-v1.5uses Whisper-large-v3 audio encoder for better lip sync quality.
* Distillation mode:Add--use_distillto enable distillation sampling (fewer steps, faster inference). This isrequiredwhen using--model_type avatar-v1.5.
* INT8 quantization:Add--use_int8to load the INT8 quantized DiT model for reduced VRAM usage. Only supported with--model_type avatar-v1.5.

💡 User tips for 1.0

* Lip synchronization accuracy:​​ Audio CFG works optimally between 3–5. Increase the audio CFG value for better synchronization.
* Prompt Enhancement: Include clear verbal-action cues (e.g., talking, speaking) in the prompt to achieve more natural lip movements.
* Mitigate repeated actions: Setting the reference image index（--ref_img_index, default to 10） between 0 and 24 ensures better consistency, while selecting other ranges (e.g., -10 or 30) helps reduce repeated actions. Additionally, increasing the mask frame range (--mask_frame_range, default to 3) can further help mitigate repeated actions, but excessively large values may introduce artifacts.
* Super resolution: Our model is compatible with both 480P and 720P, which can be controlled via --resolution.
* Dual-Audio Modes: Merge mode (set audio_type to para) requires two audio clips of equal length, and the resulting audio is obtained by summing the two clips; Concatenation mode (set audio_type to add) does not require equal-length inputs, and the resulting audio is formed by sequentially concatenating the two clips with silence padding for any gaps, where by default person1 speaks first and person2 speaks afterward.

#### LongCat-Video-Avatar-1.5

* Single-Audio-to-Video Generation

#
 Audio-Text-to-Video

torchrun --nproc_per_node=2 run_demo_avatar_single_audio_to_video.py --context_parallel_size=2 --checkpoint_dir=./weights/LongCat-Video-Avatar-1.5 --stage_1=at2v --input_json=assets/avatar/single_example_1.json --use_distill --model_type avatar-v1.5 --use_int8

#
 Audio-Image-to-Video

torchrun --nproc_per_node=2 run_demo_avatar_single_audio_to_video.py --context_parallel_size=2 --checkpoint_dir=./weights/LongCat-Video-Avatar-1.5 --stage_1=ai2v --input_json=assets/avatar/single_example_1.json --use_distill --model_type avatar-v1.5 --use_int8

#
 Audio-Text-to-Video and Video-Continuation

torchrun --nproc_per_node=2 run_demo_avatar_single_audio_to_video.py --context_parallel_size=2 --checkpoint_dir=./weights/LongCat-Video-Avatar-1.5 --stage_1=at2v --input_json=assets/avatar/single_example_1.json --num_segments=5 --ref_img_index=10 --mask_frame_range=3 --use_distill --model_type avatar-v1.5 --use_int8

#
 Audio-Image-to-Video and Video-Continuation

torchrun --nproc_per_node=2 run_demo_avatar_single_audio_to_video.py --context_parallel_size=2 --checkpoint_dir=./weights/LongCat-Video-Avatar-1.5 --stage_1=ai2v --input_json=assets/avatar/single_example_1.json --num_segments=5 --ref_img_index=10 --mask_frame_range=3 --use_distill --model_type avatar-v1.5 --use_int8

* Multi-Audio-to-Video Generation

#
 Audio-Image-to-Video

torchrun --nproc_per_node=2 run_demo_avatar_multi_audio_to_video.py --context_parallel_size=2 --checkpoint_dir=./weights/LongCat-Video-Avatar-1.5 --input_json=assets/avatar/multi_example_1.json --use_distill --model_type avatar-v1.5 --use_int8

#
 Audio-Image-to-Video and Video-Continuation

torchrun --nproc_per_node=2 run_demo_avatar_multi_audio_to_video.py --context_parallel_size=2 --checkpoint_dir=./weights/LongCat-Video-Avatar-1.5 --input_json=assets/avatar/multi_example_1.json --num_segments=5 --ref_img_index=10 --mask_frame_range=3 --use_distill --model_type avatar-v1.5 --use_int8

### Run Streamlit

#
 Single-GPU inference

streamlit run ./run_streamlit.py --server.fileWatcherType none --server.headless=false

## Evaluation Results

### Text-to-Video

TheText-to-VideoMOS evaluation results on our internal benchmark.

MOS score

Veo3

PixVerse-V5

Wan 2.2-T2V-A14B

LongCat-Video

Accessibility

Proprietary

Proprietary

Open Source

Open Source

Architecture

-

-

MoE

Dense

# Total Params

-

-

28B

13.6B

# Activated Params

-

-

14B

13.6B

Text-Alignment↑

3.99

3.81

3.70

3.76

Visual Quality↑

3.23

3.13

3.26

3.25

Motion Quality↑

3.86

3.81

3.78

3.74

Overall Quality↑

3.48

3.36

3.35

3.38

### Image-to-Video

TheImage-to-VideoMOS evaluation results on our internal benchmark.

MOS score

Seedance 1.0

Hailuo-02

Wan 2.2-I2V-A14B

LongCat-Video

Accessibility

Proprietary

Proprietary

Open Source

Open Source

Architecture

-

-

MoE

Dense

# Total Params

-

-

28B

13.6B

# Activated Params

-

-

14B

13.6B

Image-Alignment↑

4.12

4.18

4.18

4.04

Text-Alignment↑

3.70

3.85

3.33

3.49

Visual Quality↑

3.22

3.18

3.23

3.27

Motion Quality↑

3.77

3.80

3.79

3.59

Overall Quality↑

3.35

3.27

3.26

3.17

## Community Works

Community works are welcome! Please PR or inform us in Issue to add your work.

* CacheDiToffers Fully Cache Acceleration support for LongCat-Video with DBCache and TaylorSeer, achieved nearly 1.7x speedup without obvious loss of precision. Visit theirexamplefor more details.

## License Agreement

Themodel weightsare released under theMIT License.

Any contributions to this repository are licensed under the MIT License, unless otherwise stated. This license does not grant any rights to use Meituan trademarks or patents.

See theLICENSEfile for the full license text.

## Usage Considerations

This model has not been specifically designed or comprehensively evaluated for every possible downstream application.

Developers should take into account the known limitations of large language models, including performance variations across different languages, and carefully assess accuracy, safety, and fairness before deploying the model in sensitive or high-risk scenarios.
It is the responsibility of developers and downstream users to understand and comply with all applicable laws and regulations relevant to their use case, including but not limited to data protection, privacy, and content safety requirements.

Nothing in this Model Card should be interpreted as altering or restricting the terms of the MIT License under which the model is released.

## Citation

We kindly encourage citation of our work if you find it useful.

@misc{meituanlongcatteam2025longcatvideotechnicalreport,
 title={LongCat-Video Technical Report}, 
 author={Meituan LongCat Team and Xunliang Cai and Qilong Huang and Zhuoliang Kang and Hongyu Li and Shijun Liang and Liya Ma and Siyu Ren and Xiaoming Wei and Rixu Xie and Tong Zhang},
 year={2025},
 eprint={2510.22200},
 archivePrefix={arXiv},
 primaryClass={cs.CV},
 url={https://arxiv.org/abs/2510.22200}, 
}

@misc{meituanlongcatteam2026longcatvideoavatar15technicalreport,
 title={LongCat-Video-Avatar 1.5 Technical Report}, 
 author={Meituan LongCat Team and Xunliang Cai and Meng Cheng and Feng Gao and Zhe Kong and Jiamu Li and Le Li and Weiheng Li and Hongyu Liu and Shuai Tan and Xiaoming Wei and Tianyu Yang and Yong Zhang},
 year={2026},
 eprint={2605.26486},
 archivePrefix={arXiv},
 primaryClass={cs.CV},
 url={https://arxiv.org/abs/2605.26486}, 
}

@misc{meituanlongcatteam2025longcatvideoavatartechnicalreport,
 title={LongCat-Video-Avatar Technical Report}, 
 author={Meituan LongCat Team},
 year={2025},
 eprint={},
 archivePrefix={arXiv},
 primaryClass={cs.CV},
 url={}, 
}

## Acknowledgements

We would like to thank the contributors to theWan,UMT5-XXL,DiffusersandHuggingFacerepositories, for their open research.

## Contact

Please contact us atlongcat-team@meituan.comor scan the QR code to join our WeChat Group if you have any questions.