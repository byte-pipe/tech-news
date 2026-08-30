---
title: 'Sopro V2: private, fast, on-device text-to-speech · Halo Research'
url: https://research.haloneuro.ai/posts/sopro-v2
site_name: tldr
content_file: tldr-sopro-v2-private-fast-on-device-text-to-speech-hal
fetched_at: '2026-08-30T21:52:52.777141'
original_url: https://research.haloneuro.ai/posts/sopro-v2
date: '2026-08-30'
description: 'A new family of state-of-the-art (SOTA) voice-cloning TTS models, and sopro-v2-turbo: a 120M-parameter open multilingual model that streams, runs on-device, and natively supports European Portuguese.'
tags:
- tldr
---

## Sopro V2 Turbo

Today we are presenting a new family of TTS models called Sopro V2, and open-sourcing our fastest one:sopro-v2-turbo. Sopro V2 Turbo is a 120M-parameter voice-cloning text-to-speech model that streams, runs comfortably on a laptop CPU or in the browser, and is multilingual: English, German, French, and, more importantly to us, it is to our knowledge the first open TTS model natively targetingEuropeanPortuguese.

It is also genuinely fast. On an Apple M3 CPU, sopro-v2-turbo generates offline at 0.24 real-time factor (RTF, generation time divided by audio duration) and streams with a time-to-first-audio of about 300 ms at 0.21 RTF. On a single H100 it reaches 0.07 RTF offline and about 200 ms to first audio when streaming. All numbers are single-stream PyTorch with the default settings, no batching.

Sopro aims to be as simple as possible to use. One command spins up a local demo:

uvx --from sopro soprotts serve

There is also a fully in-browserONNX demothat runs without any server; note that on mobile the model is quantized, so results can be slightly below the demo above, and devices with low memory may crash.

For everything else, therepositoryREADME has the details.

We want people to communicate as fast as they used to.

## A bit of backstory

Sopro started as a personal project in December 2025, built over two weeks of vacation from the startup I co-founded —Halo NeuroAI. Halo is a software and hardware company whose main goal is to give a voice back to people who lost theirs, to conditions like ALS or post-stroke aphasia. We offered (and still offer) several voice-cloning providers: OpenAI, Cartesia, ElevenLabs. The recurring problem was that European Portuguese didn't sound right on any of them, mostly due to Brazilian Portuguese data bias, and the workarounds we built to compensate increased latency substantially, especially on our best-quality provider at the time, OpenAI, where generating a sentence took 4 to 6 seconds. For us that is a deal breaker: we want people to communicate as fast as they used to. ElevenLabs has improved since, and Cartesia is the fastest of the three because streaming cuts time-to-first-audio substantially, but its European Portuguese pronunciation still isn't there. And that is before we even talk about privacy or price.

So I had an itch to explore existing models and train my own in my free time. Budget constraints more or less forced me into a very small model, which in retrospect was a good thing: it made me realize there was a gap, one that has been closing since, for good, local, fast TTS. Sopro V1 made some headlines and reached #2 on Hacker News, and a few influential people got in touch. But V1 had real problems: it was unstable, cloning quality was inconsistent across voices, and it was not built with rigorous ablations and evaluations; it was trained for $250, after all. It was also English-only, so it didn't even address the problem that started all of this. It was, however, enough to gather attention and eventually compute. We are still pre-funding, so compute is not something we could buy. Our partners atFCCN-FCTstepped in promptly, first on Portugal's supercomputerDeucalion, and later onMareNostrum 5. We are very thankful to them: they made the research and the results below possible.

## The model

Sopro V2 evolved organically from the ablations we ran over time. The starting point was Sopro V1, whose architecture was close to Sesame'sCSMat the time:Mimias the codec, an autoregressive convolutional model predicting semantic codes (Mimi's codebook 0), and a non-autoregressive head predicting the remaining acoustic codebooks in stages, with cross-attention to the reference codes and FiLM-injected speaker features. Over V2's development, every one of those components was replaced or improved.

Overview of the Sopro V2 architecture

### Text tokenizer

The first component we replaced was the Llama text tokenizer and its 128k-entry vocabulary. At a 384-dimensional embedding table, 128k entries are ~49M parameters, so Sopro V1 was really an ~85M-parameter model, not the headline number. For V2 we trained an 8,192-tokenSentencePieceunigram tokenizer: we keep some compression without paying for a huge vocabulary.

### AR model

The second change was replacing the convolutional base model with a transformer decoder. The conv model was too myopic and led to repetitions, and at the sentence lengths we work with, attention is cheap with a KV cache. We kept it simple: a decoder with RoPE, RMSNorm, and grouped-query attention.

Unlike CosyVoice-style models, we don't require a transcription of the reference audio: the prompt to the semantic LM is just the reference's semantic tokens plus some style tokens. That removes an ASR dependency at inference, which matters on the edge, with no audible difference in pronunciation or similarity.

### Acoustic flow-matching head

The third change was the acoustic head, where we explored several directions. If you tried Sopro V1 you may have noticed speech often came out clean but failed to carry the things that make a voice sound like itself: microphone character, room tone, and so on. Part of that (not all: recent models likeQwen3-TTSshow discrete heads can work) comes from the discrete nature of acoustic codebooks. Recent work has been moving to continuous acoustic heads (F5-TTS,CosyVoice,PocketTTS), so we did too. We first tried keeping Mimi's semantic branch and swapping the acoustic branch for a continuous VAE, similar toCALMand PocketTTS. It partly worked, but it was hard to keep the latent space well-behaved enough for downstream modeling, even with KL regularization, and equally hard to guarantee a clean semantic/acoustic separation between branches. In the end we adopted the F5/CosyVoice approach and use mel spectrograms as the acoustic frontend, which is inherently well-structured. Differently from those models, we add a conditioning mask so the model knows which region is the prompt, and we mean/std-normalize theflow-matchingmels.

### Semantic speech tokenizer

The last change was the speech tokenizer itself. We originally kept Mimi's encoder and itsWavLM-distilled semantic branch, but an intermediate model trained on it was unstable and had poor intelligibility, around 7% WER on LibriSpeech test-clean and 14% on Seed-TTS test-en. WavLM features inherently carry more than semantics and don't guarantee alignment with text. So we trained an ASR-aligned tokenizer for English, French, German, and Portuguese by warm-starting from theWhisperlarge-v3 encoder and inserting anFSQbottleneck. This massively improved intelligibility. We then distilled that tokenizer into an equivalent 20M-parameter one. It runs at 23.4375 Hz instead of Mimi's 12.5 Hz, so one token corresponds to exactly 4 mel frames of our 93.75 Hz vocoder frontend and less upsampling is needed.

### Vocoder

We fine-tuned a slightly deeperVocoson our data for the offline path, and fine-tuned that further into a causal variant with 3 frames of lookahead for streaming.

## Training

We trained Sopro V2 on a mix of open-source and publicly available data,Emilia YODASandFalARamong them, with the main focus on English and European Portuguese, while keeping French and German supported. Training was split into four stages: pre-training, preference tuning, distillation, and reflow.

We first pre-trained a 0.5B base model with CFG-aware dropout; at inference the base model runs with CFG 3.0 and 32 acoustic solver steps. It trained for 400k steps at an effective batch size of 72 across 4 H100s. To support both offline and streaming generation, half the samples trained with full acoustic attention context and the other half sampled a future chunk size uniformly from 32, 64, 128, and 256 frames. That buys versatility at inference: batch offline generation when a GPU is available, or streaming with a smaller chunk for lower time-to-first-audio (at some real-time-factor cost) and a larger chunk for the reverse trade. Training segments are capped at 30 seconds, but generation length is not: longer inputs are split into segments, and each segment is generated with the previous generation as context to the semantic LM, so the model can speak indefinitely.

We then experimented with GRPO using WER, similarity, and duration rewards, but found it destabilized the model.DPOover the same kinds of preference pairs worked much better: it improved the failure tail while keeping the base model stable. We ran three rounds of it on the teacher.

Next we distilled the 0.5B teacher into a 120M model, mixing the ground-truth data the teacher saw with curated teacher rollouts. The student ended up even more stable than the teacher, trailing only slightly in similarity.

The final stage cut solver steps from 32 to 2, a 16× speedup of the acoustic head, via self-distillation withreflow, reaching near-parity with the 32-step model with no measurable loss in quality, similarity, or intelligibility. That model is sopro-v2-turbo.

The four training stages

## Evaluation

We evaluate on three benchmarks:Seed-TTS-evaltest-en, LibriSpeech test-clean under the F5-TTS protocol, and theMiniMax multilingual test set. Throughout: WER is computed with Whisper large-v3 and similarity with a WavLM speaker-verification model, following each benchmark's official harness. Baseline numbers come from the papers cited in each table, and bold marks the best value in each column (reference rows excluded).

### Seed-TTS test-en

On Seed-TTS test-en, Sopro V2 Turbo reaches SOTA-level intelligibility and competitive similarity against models 3-14× larger, some running 16× more solver steps. We could probably squeeze further with more post-training, but as the table shows we are already below ground-truth WER and close to resynthesized ground-truth similarity; past this point we would mostly be feeding Goodhart's law. We use the official evaluation harness, which applies only light text normalization: if Whisper transcribes "fifty" as "50", WER is taxed aggressively, and optimizing that away means optimizing the model's enunciation for Whisper rather than for people.

Seed-TTS-eval test-en
System
Params
WER ↓
SIM ↑
Ground truth
—
2.14
0.734
Ground truth (our vocoder resynthesis)
—
2.14
0.701
Seed-TTS
—
2.25
0.762
CosyVoice 2
0.5B
2.57
0.652
CosyVoice 3
0.5B
2.02
0.718
F5-TTS (32 steps)
336M
1.83
0.67
Spark-TTS
0.5B
1.98
0.584
VibeVoice-1.5B
1.5B
3.04
0.689
MaskGCT
1.0B
2.62
0.717
Qwen3-TTS (12 Hz base)
1.7B
1.24
—
Sopro V2 (32 steps)
0.5B
1.77
0.685
Sopro V2 Turbo (2 steps)
120M
1.65
0.651
Sopro V2 Turbo (streaming)
120M
1.51
0.644

Baselines as reported by their authors (CosyVoice 2/3, Spark-TTS, VibeVoice, F5-TTS papers; Seed-TTS and MaskGCT as quoted in the CosyVoice 2 and F5-TTS papers; Qwen3-TTS from its technical report, which reports WER only on this benchmark). The ground-truth row follows the CosyVoice 2 paper; the resynthesis row is measured with our vocoder on the official harness.

Seed-TTS test-en · reference vs. Sopro V2 Turbo

English

“It is also used as an initial ingredient in homeopathic remedies.”

Reference
Sopro

English

“As such, symbols and customs of Mexico grew up in New Mexico as well.”

Reference
Sopro

English

“Changes to diet and nutritional supplements may help some patients.”

Reference
Sopro

### LibriSpeech test-clean (F5 protocol)

We use the F5-TTS cross-sentence protocol (1,127 samples from LibriSpeech-PC test-clean). Baseline rows come from the F5-TTS paper.

LibriSpeech-PC test-clean · F5-TTS protocol
System
Params
WER ↓
SIM ↑
Ground truth
—
2.23
0.69
Ground truth (our vocoder resynthesis)
—
2.72
0.664
F5-TTS (32 steps)
336M
2.42
0.66
E2-TTS (32 steps)
333M
2.95
0.69
CosyVoice
300M
3.59
0.66
FireRedTTS
580M
2.69
0.47
PocketTTS
100M
1.84
—
Sopro V2 (32 steps)
0.5B
2.05
0.667
Sopro V2 Turbo (2 steps)
120M
1.85
0.645
Sopro V2 Turbo (streaming)
120M
1.88
0.635

Baselines from the F5-TTS paper, Table 1 (E2-TTS is the F5 authors' reproduction); PocketTTS as reported in itsblog postand theCALMpaper, which do not report a comparable WavLM similarity. The ground-truth row is as reported in the F5-TTS paper; the resynthesis row is measured with our vocoder.

### MiniMax multilingual eval

On theMiniMax-Speechmultilingual test set, Sopro V2 Turbo holds up well against closed systems across English, French, German, and Portuguese. On Portuguese the comparison is not entirely fair to us: the reference speakers in the benchmark's Portuguese portion are Brazilian, while Sopro's Portuguese targets the European variant. European pronunciation itself also inflates WER: unstressed vowels get reduced, so words like "telefone", "esperança", or "desenvolvimento" come out clipped compared to their Brazilian reading, and the ASR is more likely to mis-transcribe them even when the European pronunciation is correct.

MiniMax multilingual test set · WER ↓ / SIM ↑ per language
System
en
fr
de
pt
MiniMax-Speech
2.16 / 0.756
4.10
 / 0.628
1.91 / 0.733
1.88 / 
0.805
ElevenLabs Multilingual v2
2.34 / 0.613
5.22 / 0.535
0.57
 / 0.614
1.33
 / 0.711
Sopro V2 (32 steps)
2.18 / 
0.782
4.29 / 
0.729
0.71 / 
0.774
3.45 / 0.722
Sopro V2 Turbo (2 steps)
1.90
 / 0.721
5.06 / 0.684
0.62 / 0.741
2.66 / 0.681
Sopro V2 Turbo (streaming)
2.12 / 0.706
4.73 / 0.676
0.73 / 0.735
2.71 / 0.686

Each cell is WER / SIM. MiniMax-Speech and ElevenLabs rows as reported in the MiniMax-Speech paper (Table 2, Whisper large-v3 WER).

MiniMax multilingual · reference vs. Sopro V2 Turbo

English

“I guess it comes down a simple choice. Get busy living or get busy dying.”

Reference
Sopro

English

“As the spacecraft broke through the atmosphere of the alien planet, the crew held their breath, unsure of what new life forms they might encounter.”

Reference
Sopro

Português

“Neste episódio, nossos ouvintes conhecerão os segredos da fabricação artesanal do queijo da Serra da Estrela, considerado um dos melhores queijos de Portugal.”

Reference
Sopro

Português

“Os buracos negros são regiões do espaço onde a gravidade é tão intensa que nem mesmo a luz consegue escapar, o que os torna invisíveis aos telescópios convencionais.”

Reference
Sopro

Português

“Não posso adiar este abraço que é uma arma de dois gumes, amor e ódio.”

Reference
Sopro

Deutsch

“Der Wetterdienst hat eine Warnung vor starken Stürmen herausgegeben, die in den nächsten drei Tagen die Küstengebiete treffen werden.”

Reference
Sopro

Deutsch

“Die Stadtverwaltung hat die Einführung eines neuen öffentlichen Verkehrssystems angekündigt, das verspricht, die Wartezeiten zu verkürzen und die Servicequalität zu verbessern.”

Reference
Sopro

Français

“Les américains ont bien insisté là-dessus, il faut être nickel à cheval.”

Reference
Sopro

Français

“Un séisme de magnitude 6,2 a frappé la côte nord du pays ce matin, mais aucune victime ni dégât majeur n'a été signalé pour le moment.”

Reference
Sopro

### European Portuguese

European Portuguese is the reason Sopro exists, so here are a few voices from our internal EP test set, built from European Portuguese Common Voice speakers.

European Portuguese · reference vs. Sopro V2 Turbo

Português europeu

“Você quer jogar um jogo quinta-feira?”

Reference
Sopro

Português europeu

“Oceano Índico, Pacífico e Atlântico”

Reference
Sopro

Português europeu

“agroquímicos, agroplásticos, películas, estufas, mudas, polímeros, polietileno, linear, densidade”

Reference
Sopro

## Limitations and disclaimers

We did not add watermarking: with an open-source inference pipeline it would be trivial to remove, so it would only provide a false sense of safety. Please use the model for good: do not impersonate people.

We deliberately keep the text frontend minimal, so some abbreviations, numbers, and symbols may not be pronounced correctly. Prefer words:1 + 2should be writtenone plus two. That said, Sopro generally reads common abbreviations like "CPU" or "TTS" fine, and you can put a language-specific normalizer in front of it.

Mixed-language text is another weak spot: words from one language inside a sentence of another (an English product name in a Portuguese sentence, for example) can be mispronounced.

We are not planning to release the training code in the near future due to its complexity.

Compute for this project was funded by FCCN-FCT and Fábrica de IA / Barcelona Supercomputing Center, under project reference eporaif07.

## Conclusion

Once again, thank you to FCCN-FCT for the compute, and to the open-source community whose work was a constant inspiration for Sopro V2.

Sopro V2 delivers SOTA-level text-to-speech that is local and fast, and it is the foundation for the models coming next from Halo Research. We are excited to add more languages, emotion control, and to keep improving from here.

If you want to partner with us, or you are an investor, don't hesitate to reach out at[email protected].