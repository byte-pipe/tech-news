---
title: Vāgdhenu — A Vṛtta-Aware Śloka-to-Chant TTS for Sanskrit
url: https://prathosh.in/vagdhenu/
site_name: hnrss
content_file: hnrss-vāgdhenu-a-vṛtta-aware-śloka-to-chant-tts-for-sans
fetched_at: '2026-07-18T11:24:55.546335'
original_url: https://prathosh.in/vagdhenu/
date: '2026-07-13'
description: 'Vāgdhenu: a meter-aware Sanskrit śloka-to-chant text-to-speech system. Prof. Prathosh A P, Indian Institute of Science, Bengaluru.'
tags:
- hackernews
- hnrss
---

## Try it

Paste a Sanskrit verse in any Indian script — the meter is detected automatically.

First chant takes ~10–60s while the model warms up. If the demo doesn't load,
 use thebackup demo ↗.

## Listen — sample chants

Six vṛttas rendered by this system — including verses from the shipped deployments.

vasantatilakā

Mahābhārata Tātparya Nirṇaya · 1.1

नारायणाय परिपूर्णगुणार्णवाय विश्वोदयस्थितिलयोन्नियतिप्रदाय ।ज्ञानप्रदाय विबुधासुरसौख्यदुःखसत्कारणाय वितताय नमोनमस्ते

śārdūlavikrīḍita

Śrīmad Bhāgavatam · 1.1.2

जन्माद्यस्य यतोऽन्वयादितरतश्‍चार्थेष्वभिज्ञः स्वराट् तेने ब्रह्म हृदा य आदिकवये मुह्यन्ति यं सूरयः। तेजोवारिमृदां यथा विनिमयो यत्र त्रिसर्गो मृषा धाम्ना स्वेन सदा निरस्तकुहकं सत्यं परं धीमहि

anuṣṭubh

Śrīmad Bhāgavatam · 1.1.5

नैमिषेऽनिमिषक्षेत्रे ऋषयः शौनकादयः। सत्रं स्वर्गाय लोकाय सहस्रसममासत

vaṃśastha

Śrīmad Bhāgavatam · 1.3.5

पश्यन्त्यदो रूपमदभ्रचक्षुषः सहस्रपादोरुभुजाननाद्भुतम्। सहस्रमूर्धश्रवणाक्षिनासिकं सहस्रमौल्यम्बरकुण्डलोल्‍लसत्

drutavilambita

Śrīmad Bhāgavatam · 1.1.4

निगमकल्पतरोर्गलितं फलं शुकमुखादमृतद्रवसंयुतम्। पिबत भागवतं रसमालयं मुहुरहो रसिका भुवि भावुकाः

mālinī

Narasiṃha stuti · retroflex tongue-twister

हठलुठ दल घिष्टोत्कण्ठदष्टोष्ठ विद्युत् सटशठ कठिनोरः पीठभित्सुष्ठुनिष्ठाम् ।पठतिनुतव कण्ठाधिष्ठ घोरान्त्रमाला दह दह नरसिंहासह्यवीर्याहितं मे ॥

## Get the app

These recitations power a free app for the complete Śrīmad Bhāgavatam.

॥ भागवतवाणी ॥

### Bhāgavata-VāNi

The complete Śrīmad Bhāgavatam — all 12 skandhas — with synced audio recitation and
 line-by-line karaoke highlighting, in 10 Indian scripts. Search any verse in any script, traditional
 indices, works fully offline. Free, no ads.

Open web app ↗

Google Play ↗

App Store ↗

## Practise with it

Vāgdhenu's chants power a companion tool that listens toyou.

॥ वाग्बोधिनी ॥

### Vāgbodhinī

A Sanskrit chant tutor. Paste any śloka (or prose) in any script, hear its
 metre-aware reference chant rendered by Vāgdhenu, then chant along — a Sanskrit speech model
 scoresevery syllableand shows you what to fix. For classical (laukika) Sanskrit.

Open Vāgbodhinī ↗

GitHub ↗

ASR model ↗

## About

Vāgdhenu maps a metrical verse to its chantedpārāyaṇarecitation. Its voice is a
 flow-matching TTS backboneretrained on a purpose-recorded, carefully designed
 single-speaker Sanskrit chant corpus(~5 hours), with a further voice-steering retrain;
 the neural vocoder is likewise fine-tuned for the chant register. Around the trained model sits
 the machinery a faithful Sanskrit chant pipeline needs: a script-aware frontend that routes
 Sanskrit through Kannada orthography (avoiding the Hindi schwa-deletion that Devanagari triggers);
 visarga sandhi with the jihvāmūlīya and upadhmānīya allophones; the aspiration contrast; the three
 sibilants and the full retroflex series kept distinct; homorganic anusvāra and vocalic ṝ; and a
 vṛtta-aware mechanism that detects the meter and selects a matched reference under thehalf-reference rule. The retrained model reaches an expert MOS of about4.6,
 and dense conjuncts — including retroflex aspirates — render correctly, the class earlier
 architectures could not crack.

## Deployments

This system produced two corpora at scale.

●Mahābhārata Tātparya Nirṇaya— 32 chapters, 5,183 verses (~17.5h) ·video series ↗

●Śrīmad Bhāgavatam— ~18,000 verses across 12 books ·karaoke-video series ↗