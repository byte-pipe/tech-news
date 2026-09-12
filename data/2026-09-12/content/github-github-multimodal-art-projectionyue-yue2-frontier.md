---
title: 'GitHub - multimodal-art-projection/YuE: YuE2: frontier music generation with symbolic planning, zero-shot covers, and agentic music editing. · GitHub'
url: https://github.com/multimodal-art-projection/YuE
site_name: github
content_file: github-github-multimodal-art-projectionyue-yue2-frontier
fetched_at: '2026-09-12T13:52:44.104053'
original_url: https://github.com/multimodal-art-projection/YuE
author: multimodal-art-projection
description: 'YuE2: frontier music generation with symbolic planning, zero-shot covers, and agentic music editing. - multimodal-art-projection/YuE'
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 multimodal-art-projection

 

/

YuE

Public

* NotificationsYou must be signed in to change notification settings
* Fork810
* Star7.1k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

156 Commits
156 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github/
workflows
.github/
workflows
 
 
assets
assets
 
 
docs
docs
 
 
examples
examples
 
 
licenses
licenses
 
 
skills/
yue2-music
skills/
yue2-music
 
 
src/
yue2
src/
yue2
 
 
tests
tests
 
 
tools
tools
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
MANIFEST.in
MANIFEST.in
 
 
MODEL_LICENSE
MODEL_LICENSE
 
 
README.md
README.md
 
 
THIRD_PARTY_NOTICES.md
THIRD_PARTY_NOTICES.md
 
 
pyproject.toml
pyproject.toml
 
 
View all files

## Repository files navigation

Looking for the original YuE? Its code, documentation, and license are preserved on theYuE-v1 branch.

# YuE2: Unifying Symbolic and Audio Music Generation at Frontier Quality

Compose in symbols. Create in sound.

🎧 Demos·🤗 YuE2·🚀 Quick start·🤖 Agent skill·📊 Benchmarks·🤗 MERT2·🤗 SheetSage2·🤗 WSB·📦 Release·

YuE2 brings frontier song quality to music generation with an editable composition.Give it lyrics and a style prompt: it writes a melody-and-chord plan, then realizes that plan as a complete song with vocals and accompaniment.

* Frontier quality.YuE2 is competitive with Suno v5/v6 on WildSongBench. YuE2 (best-of-8) achieves6.9632 SongBench Avg, the highest observed mean among all evaluated settings.
* White-box music generation through symbolic planning.Read, play, and change the composition before rendering it. Melody and chords become explicit controls that a person or an agent can inspect and edit.
* Zero-shot covers and agentic editing.Reimagine a transcribed song in a new style, or refine a song through a conversation about its score, arrangement, and lyrics—all with the same generation checkpoint.

192 WildSongBench prompts. Both YuE2 settings use symbolic planning. Bo8 = best-of-8. The axes are normalized comparison indices; bubble area represents AudioBox production quality.Scores and evaluation protocol.Vector PDF·SVG.

## Hear what you can make

Create

Cover

Edit with an agent

Lyrics + style → score → full song

Source recording → melody score → a new interpretation

Musical feedback → score, style, or lyric revisions → a new recording

Listen and inspect the score

Hear zero-shot covers

Follow an editing conversation

The agentic demo followsThe Last Train through 9 steps and 14 versions, from Mandarin pop to English jazz with new harmony and a saxophone solo. Listen to each version and inspect its conversation, score, prompt, and lyrics.

## How it works

OneAR–NAR Mixture-of-Transformersbackbone predicts the score and semantic tokens autoregressively, then generates acoustic latents with flow matching. A VAE decodes those latents into stereo audio. Creation, covering, and editing differ in where the score comes from: YuE2, a transcribed recording, or an edited composition.

The staged Python API exposesplan()→generate_semantic()→synthesize()→decode(). See thegeneration guidefor exact-plan reuse and decoder selection.

## Quick start

Linux · Python 3.12 · NVIDIA GPU with BF16 support and 24 GB VRAM.YuE2 produces 48 kHz stereo audio without quantization. Model files download from Hugging Face on first use.

git clone https://github.com/multimodal-art-projection/YuE.git

cd
 YuE
python3.12 -m venv .venv

source
 .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install 
.

python examples/generate.py --output outputs/first-song

Openoutputs/first-song/audio.flac. The output directory also retains the score, semantic tokens, acoustic latents, generation settings, and model identities.

The Python interface is equally short:

import
 
json

from
 
pathlib
 
import
 
Path

from
 
yue2
 
import
 
YuE2Pipeline

request
 
=
 
json
.
loads
(
Path
(
"examples/song.json"
).
read_text
(
encoding
=
"utf-8"
))

with
 
YuE2Pipeline
.
from_pretrained
(
"m-a-p/YuE2-3B"
, 
device
=
"cuda"
) 
as
 
pipe
:
 
song
 
=
 
pipe
(
**
request
)
 
song
.
save_artifacts
(
"outputs/my-song"
)
 
print
(
song
.
truncated
)

Setting

Behavior

cot="full"

Generate an editable melody-and-chord plan; the default for new songs

cot="melody"

Use a melody plan with free accompaniment; recommended for covers

cot="off"

Generate directly from lyrics and style

abc=...

Supply your own score in 
full
 or 
melody
 mode

Generation guide·Original example inputs·v0.1.6 wheel archive

## Cover a song

Transcribe a source recording with🤗 SheetSage2, review its melody ABC, and provide new lyrics or a target style. For covers, usecot="melody"and a score without chord symbolsso the accompaniment can adapt to the new style.

from
 
pathlib
 
import
 
Path

from
 
yue2
 
import
 
YuE2Pipeline

with
 
YuE2Pipeline
.
from_pretrained
(
"m-a-p/YuE2-3B"
, 
device
=
"cuda"
) 
as
 
pipe
:
 
cover
 
=
 
pipe
(
 
style
=
"English, jazz-funk, warm lead vocal, Rhodes, bass and drums"
,
 
lyrics
=
Path
(
"cover-lyrics.txt"
).
read_text
(
encoding
=
"utf-8"
),
 
abc
=
Path
(
"cover-score/score.abc"
).
read_text
(
encoding
=
"utf-8"
),
 
cot
=
"melody"
,
 
seed
=
42
,
 )
 
cover
.
save_artifacts
(
"outputs/cover"
)

SheetSage2 runs in a separate environment and loads its MERT2 encoder automatically. Thecover guidegives the complete transcription and generation commands. An includedoriginal melody examplealso lets you try score-conditioned generation immediately.

## Edit a composition

Export a plan, revise the musical details, and render the edited score:

import
 
json

from
 
pathlib
 
import
 
Path

from
 
yue2
 
import
 
YuE2Pipeline

request
 
=
 
json
.
loads
(
Path
(
"examples/song.json"
).
read_text
(
encoding
=
"utf-8"
))

with
 
YuE2Pipeline
.
from_pretrained
(
"m-a-p/YuE2-3B"
, 
device
=
"cuda"
) 
as
 
pipe
:
 
plan
 
=
 
pipe
.
plan
(
**
request
)
 
plan
.
save
(
"outputs/plan"
)

Copyoutputs/plan/score.abctoedited.abc, then ask an agent to change its harmony, melody, tempo, or form. Supply the edited file as a new score:

python examples/generate.py --request examples/song.json \
 --abc-file edited.abc --cot full --output outputs/edited

The editable score is the white-box interface: you can inspect the intended composition and intervene on it. Editing generates a new complete recording; it does not preserve the original waveform outside an edit.Editing guide and a reproducible harmony example.

## Agent skill

Theyue2-music skillteaches an agent how to generate songs, transcribe and cover recordings, edit ABC scores, check musical invariants, and organize listening comparisons. It includes portable helpers and references to the released model interfaces.

Useskills/yue2-music/from this repositorywith an agent that supportsSKILL.mdpackages. Install it using your agent's skill-directory or import mechanism; the Python runtime is installed separately withpip install .. The earlierv0.1.6 skill ZIPremains available under its bundled license.

Try a concrete request:

Use the yue2-music skill to create an English piano-pop song. Keep the original audio and score. Make a second version with jazz harmony, preserve the vocal melody and lyric order, and give me both versions to compare.

## Benchmarks

WildSongBench: 192 prompts, automatic evaluation, September 12, 2026.

System / setting

SongBench Avg ↑

AudioBox PQ ↑

MuLan ↑

PER ↓

YuE2 (best-of-8)
 †

6.9632

8.2714

0.5051

9.79%

Mureka 9

6.9377

8.0226

0.4394

11.69%

Suno v5

6.8721

8.1698

0.5428

8.10%

YuE2
 †

6.7316

8.2598

0.5068

8.44%

Suno v5.5

6.7150

8.1955

0.5089

5.96%

Suno v4.5

6.6995

8.2541

0.5022

5.80%

Suno v6

6.5562

8.1296

0.4916

7.58%

Suno v6 Wild

6.4195

8.1785

0.4999

7.45%

LeVo 2 †

6.3247

8.3966

0.3542

26.12%

MiniMax Music 2.6

6.3222

8.1711

0.4251

24.55%

MiniMax Music 3 †

6.2830

8.2825

0.3928

6.27%

HeartMuLa †

6.2483

8.2933

0.3823

10.71%

Muse †

6.0349

8.0517

0.3937

33.42%

ACE-Step 1.5 †

6.0118

8.0518

0.4372

7.46%

DiffRhythm 2 †

5.2428

7.9782

0.3782

18.41%

YuE 1 †

4.9165

7.8683

0.2623

36.38%

SongBloom †

4.2350

8.1539

0.2697

19.19%

† Publicly available model weights. All 17 evaluated settings are shown, sorted by SongBench Avg; bold values mark the best result in each column.

Both YuE2 settings use symbolic planning and the benchmark decoder,YuE2-Vae-legacy. Standard YuE2 selects from two candidates; best-of-8 selects from eight. Rankings vary by metric; the small gap between the highest means does not establish statistical significance.Full results and selection protocols.

Zero-shot covers.On 948 works, full-score YuE2 reaches0.647 CLEWS mAP, compared with0.006 without a score, while using the general generator without cover-specific fine-tuning. Source-identity preservation and target-style quality are measured separately; melody-only covers offer more freedom to change the arrangement.Cover evaluation.

### Reproduce the benchmarks

To reproduce the reported benchmark scores, follow the instructions on🤗 WildSongBench (WSB).

## MERT2

State-of-the-art music understanding:SOTA on14 of 15 MARBLE metrics, with91.72% genre accuracy on GTZAN.

Demo and results·🤗 MERT2-30s·🤗 MERT2-FS

## SheetSage2

State-of-the-art audio-to-score transcription:SOTA on10 of 13 benchmark metrics, with82.51% vocal melody pitch-class F1 on RWC-Pop.

Demo and results·🤗 Model and inference

## Models and resources

Resource

Purpose

🤗 YuE2-3B

Song generation, symbolic planning, covering, and editing

🤗 YuE2-Vae

Default generation and listening decoder

🤗 YuE2-Vae-legacy

Decoder for the reported benchmark protocol

🤗 SheetSage2

Audio-to-score transcription for covers and editing

🤗 MERT-v2-FullSong

Full-song music representations; SheetSage2's encoder

🤗 MERT-v2-30s

Music representations for short recordings

🤗 WildSongBench

Evaluation prompts and benchmark resources

MERT2 feature extraction is optional for generation. YuE2's pipeline does not require a separate MERT2 model download.Demos and interactive results·Release downloads.

## License

YuE2's first-party code, agent skill, and documentation are licensed underApache 2.0. Copyright (c) 2026 the YuE2 authors.

Model weights are separately licensed underCC BY-NC 4.0. Third-party components retain theiroriginal licenses. The archivedYuE-v1 branchretains its original license.

Apache 2.0 applies to the current repository source; the earlieryue2-v0.1.6download archives retain their bundled licenses.

## Citation

The YuE2 technical report is coming soon. For now, please citeMERTandYuE:

@article
{
li2023mert
,
 
title
 = 
{
{MERT}: Acoustic Music Understanding Model with Large-Scale Self-supervised Training
}
,
 
author
 = 
{
Li, Yizhi and Yuan, Ruibin and Zhang, Ge and Ma, Yinghao and Chen, Xingran and Yin, Hanzhi and Xiao, Chenghao and Lin, Chenghua and Ragni, Anton and Benetos, Emmanouil and Gyenge, Norbert and Dannenberg, Roger and Liu, Ruibo and Chen, Wenhu and Xia, Gus and Shi, Yemin and Huang, Wenhao and Wang, Zili and Guo, Yike and Fu, Jie
}
,
 
journal
 = 
{
arXiv preprint arXiv:2306.00107
}
,
 
year
 = 
{
2023
}
,
 
eprint
 = 
{
2306.00107
}
,
 
archivePrefix
 = 
{
arXiv
}
,
 
url
 = 
{
https://arxiv.org/abs/2306.00107
}

}

@article
{
yuan2025yue
,
 
title
 = 
{
{YuE}: Scaling Open Foundation Models for Long-Form Music Generation
}
,
 
author
 = 
{
Yuan, Ruibin and Lin, Hanfeng and Guo, Shuyue and Zhang, Ge and Pan, Jiahao and Zang, Yongyi and Liu, Haohe and Liang, Yiming and Ma, Wenye and Du, Xingjian and Du, Xinrun and Ye, Zhen and Zheng, Tianyu and Jiang, Zhengxuan and Ma, Yinghao and Liu, Minghao and Tian, Zeyue and Zhou, Ziya and Xue, Liumeng and Qu, Xingwei and Li, Yizhi and Wu, Shangda and Shen, Tianhao and Ma, Ziyang and Zhan, Jun and Wang, Chunhui and Wang, Yatian and Chi, Xiaowei and Zhang, Xinyue and Yang, Zhenzhu and Wang, Xiangzhou and Liu, Shansong and Mei, Lingrui and Li, Peng and Wang, Junjie and Yu, Jianwei and Pang, Guojian and Li, Xu and Wang, Zihao and Zhou, Xiaohuan and Yu, Lijun and Benetos, Emmanouil and Chen, Yong and Lin, Chenghua and Chen, Xie and Xia, Gus and Zhang, Zhaoxiang and Zhang, Chao and Chen, Wenhu and Zhou, Xinyu and Qiu, Xipeng and Dannenberg, Roger and Liu, Jiaheng and Yang, Jian and Huang, Wenhao and Xue, Wei and Tan, Xu and Guo, Yike
}
,
 
journal
 = 
{
arXiv preprint arXiv:2503.08638
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
2503.08638
}
,
 
archivePrefix
 = 
{
arXiv
}
,
 
url
 = 
{
https://arxiv.org/abs/2503.08638
}

}

## Contact

For collaborations, licensing, and data partnerships, please contactgezhang@umich.edu.