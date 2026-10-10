---
title: 'Eye of Sauron: Long-Range Hidden Spy Camera Detection and Positioning with Inbuilt Memory EM Radiation | USENIX'
url: https://www.usenix.org/conference/usenixsecurity24/presentation/zhang-qibo
site_name: hnrss
content_file: hnrss-eye-of-sauron-long-range-hidden-spy-camera-detecti
fetched_at: '2026-10-10T16:08:04.917766'
original_url: https://www.usenix.org/conference/usenixsecurity24/presentation/zhang-qibo
date: '2026-10-07'
description: 'Eye of Sauron: Long-Range Hidden Spy Camera Detection (2024)'
tags:
- hackernews
- hnrss
---

# Eye of Sauron: Long-Range Hidden Spy Camera Detection and Positioning with Inbuilt Memory EM Radiation

Qibo Zhang and Daibo Liu,Hunan University;Xinyu Zhang,University of California San Diego;Zhichao Cao,Michigan State University;Fanzi Zeng, Hongbo Jiang, and Wenqiang Jin,Hunan University

In this paper, we present ESauron — the first proof-of-concept system that can detect diverse forms of spy cameras (i.e., wireless, wired and offline devices) and quickly pinpoint their locations. The key observation is that, for all spy cameras, the captured raw images must be first digested (e.g., encoding and compression) in the video-capture devices before transferring to target receiver or storage medium. This digestion process takes place in an inbuilt read-write memory whose operations cause electromagnetic radiation (EMR). Specifically, the memory clock drives a variable number of switching voltage regulator activities depending on the workloads, causing fluctuating currents injected into memory units, thus emitting EMR signals at the clock frequency. Whenever the visual scene changes, bursts of video data processing (e.g., video encoding) suddenly aggravate the memory workload, bringing responsive EMR patterns. ESauron can detect spy cameras by intentionally stimulating scene changes and then sensing the surge of EMRs even from a considerable distance. We implemented a proof-of-concept prototype of the ESauron by carefully designing techniques to sense and differentiate memory EMRs, assert the existence of spy cameras, and pinpoint their locations. Experiments with 50 camera products show that ESauron can detect all spy cameras with an accuracy of 100% after only 4 stimuli, the detection range can exceed 20 meters even in the presence of blockages, and all spy cameras can be accurately located.

## Open Access Media

USENIX is committed to Open Access to the research presented at our events. Papers and proceedings are freely available to everyone once the event begins. Any video, audio, and/or slides that are posted after the event are also free and open to everyone.Support USENIXand our commitment to Open Access.

BibTeX
@inproceedings {298164,

	author = {Qibo Zhang and Daibo Liu and Xinyu Zhang and Zhichao Cao and Fanzi Zeng and Hongbo Jiang and Wenqiang Jin},

	title = {Eye of Sauron: {Long-Range} Hidden Spy Camera Detection and Positioning with Inbuilt Memory {EM} Radiation},

	booktitle = {33rd USENIX Security Symposium (USENIX Security 24)},

	year = {2024},

	isbn = {978-1-939133-44-1},

	address = {Philadelphia, PA},

	pages = {109--126},

	url = {https://www.usenix.org/conference/usenixsecurity24/presentation/zhang-qibo},

	publisher = {USENIX Association},

	month = aug

}

Download
 
Zhang PDF
 
Zhang Paper (Prepublication) PDF

## Presentation Video