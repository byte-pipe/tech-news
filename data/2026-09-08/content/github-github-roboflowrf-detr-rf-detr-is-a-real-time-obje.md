---
title: 'GitHub - roboflow/rf-detr: RF-DETR is a real-time object detection and segmentation model architecture developed by Roboflow, SOTA on COCO, designed for fine-tuning. [ICLR 2026] · GitHub'
url: https://github.com/roboflow/rf-detr
site_name: github
content_file: github-github-roboflowrf-detr-rf-detr-is-a-real-time-obje
fetched_at: '2026-09-08T00:30:53.499287'
original_url: https://github.com/roboflow/rf-detr
author: roboflow
description: 'RF-DETR is a real-time object detection and segmentation model architecture developed by Roboflow, SOTA on COCO, designed for fine-tuning. [ICLR 2026] - GitHub - roboflow/rf-detr: RF-DETR is a real-time object detection and segmentation model architecture developed by Roboflow, SOTA on COCO, designed for fine-tuning. [ICLR 2026]'
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 roboflow

 

/

rf-detr

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.2k
* Star9.3k

 
 
 
develop
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

1,121 Commits
1,121 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
configs
configs
 
 
docs
docs
 
 
src/
rfdetr
src/
rfdetr
 
 
tests
tests
 
 
.codecov.yml
.codecov.yml
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CITATION.cff
CITATION.cff
 
 
CLAUDE.md
CLAUDE.md
 
 
CNAME
CNAME
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
mkdocs.yaml
mkdocs.yaml
 
 
pyproject.toml
pyproject.toml
 
 
View all files

## Repository files navigation

# RF-DETR: Real-Time SOTA Object Detection, Instance Segmentation, and Keypoint Detection

 
 
 
 

 
 
 
 

RF-DETR is a real-time transformer architecture for object detection, instance segmentation, and keypoint detection (preview) developed by Roboflow. Built on a DINOv2 vision transformer backbone, RF-DETR delivers state-of-the-art accuracy and latency trade-offs onMicrosoft COCOandRF100-VL.

RF-DETR uses a DINOv2 vision transformer backbone and supports object detection, instance segmentation, and keypoint detection (preview) in a single, consistent API. The open-sourcerfdetrpackage and Apache-designated models are released under Apache 2.0, while Plus components (rfdetr_plus, including RF-DETR-XL/2XL detection models) are licensed under PML 1.0.

The published RF-DETR sizes were created with neural architecture search (NAS) — and the same NAS method is now available on theRoboflow platform, so you can discover the best architecture for your own dataset. Learn more in theNAS docs.

rf-detr-segmentation-promo.mp4

## Install

To install RF-DETR, install therfdetrpackage in aPython>=3.10environment withpip.

pip install rfdetr

Install from source

By installing RF-DETR from source, you can explore the most recent features and enhancements that have not yet been officially released.Please note that these updates are still in development and may not be as stable as the latest published release.

pip install https://github.com/roboflow/rf-detr/archive/refs/heads/develop.zip

## Benchmarks

RF-DETR achieves state-of-the-art results in both object detection and instance segmentation, with benchmarks reported on Microsoft COCO and RF100-VL (RF100-VL for detection only). The charts and tables below compare RF-DETR against other top real-time models across accuracy and latency for detection and segmentation. All COCO accuracy numbers are measured in-house for every model shown, computed with pycocotools in SAB over the full 5,000-imageval2017split, so every row is directly comparable and may differ from vendor-reported figures. The sole exception is rows marked †, which are quoted from the original authors' paper and were not measured in SAB. All latency numbers were measured on an NVIDIA T4 using TensorRT, FP16, and batch size 1. Parameter counts are deployment (fused)nn.Moduleparameter counts (model.parameters(), not the raw tensor count of the saved checkpoint), except rows marked †, which are the authors' reported counts. For full benchmarking methodology and reproducibility details, seeroboflow/sab.

### Detection

See object detection benchmark numbers

Architecture

COCO AP
50

COCO AP
50:95

RF100VL AP
50

RF100VL AP
50:95

Latency (ms)

Params (M)

Resolution

License

RF-DETR-N

67.6

48.4

85.0

57.7

2.3

30.5

384x384

Apache 2.0

RF-DETR-S

72.1

53.0

86.7

60.2

3.5

32.1

512x512

Apache 2.0

RF-DETR-M

73.6

54.7

87.4

61.2

4.4

33.7

576x576

Apache 2.0

RF-DETR-L

75.1

56.5

88.2

62.2

6.8

33.9

704x704

Apache 2.0

RF-DETR-XL △

77.4

58.6

88.5

62.9

11.5

126.4

700x700

PML 1.0

RF-DETR-2XL △

78.5

60.1

89.0

63.2

17.2

126.9

880x880

PML 1.0

YOLO11-N

52.0

37.4

81.4

55.3

2.5

2.6

640x640

AGPL-3.0

YOLO11-S

59.7

44.4

82.3

56.2

3.2

9.4

640x640

AGPL-3.0

YOLO11-M

64.1

48.6

82.5

56.5

5.1

20.1

640x640

AGPL-3.0

YOLO11-L

64.9

49.9

82.2

56.5

6.5

25.3

640x640

AGPL-3.0

YOLO11-X

66.1

50.9

81.7

56.2

10.5

56.9

640x640

AGPL-3.0

YOLO26-N

55.8

40.3

76.7

52.0

1.7

2.6

640x640

AGPL-3.0

YOLO26-S

64.3

47.7

82.7

57.0

2.6

9.4

640x640

AGPL-3.0

YOLO26-M

69.7

52.5

84.4

58.7

4.4

20.1

640x640

AGPL-3.0

YOLO26-L

71.1

54.1

85.0

59.3

5.7

25.3

640x640

AGPL-3.0

YOLO26-X

74.0

56.9

85.6

60.0

9.6

56.9

640x640

AGPL-3.0

LW-DETR-T

60.7

42.9

84.7

57.1

1.9

12.1

640x640

Apache 2.0

LW-DETR-S

66.8

48.0

85.0

57.4

2.6

14.6

640x640

Apache 2.0

LW-DETR-M

72.0

52.6

86.8

59.8

4.4

28.2

640x640

Apache 2.0

LW-DETR-L

74.6

56.1

87.4

61.5

6.9

46.8

640x640

Apache 2.0

LW-DETR-X

76.9

58.3

87.9

62.1

13.0

118.0

640x640

Apache 2.0

D-FINE-N

60.2

42.7

84.4

58.2

2.1

3.8

640x640

Apache 2.0

D-FINE-S

67.6

50.6

85.3

60.3

3.5

10.2

640x640

Apache 2.0

D-FINE-M

72.6

55.0

85.5

60.6

5.4

19.2

640x640

Apache 2.0

D-FINE-L

74.9

57.2

86.4

61.6

7.5

31.0

640x640

Apache 2.0

D-FINE-X

76.8

59.3

86.9

62.2

11.5

62.0

640x640

Apache 2.0

SAM 3 †

—

—

—

61.6

—

~850

1008x1008

N/A

† Reported by the SAM 3 authors (arXiv:2511.16719, Table 36),notmeasured by us in SAB. The value is SAM 3 fine-tuned on the full RF100-VL training set, which is the same setting as the RF100VL columns above — SAM 3's paper reports LW-DETR-m at 59.8 on this benchmark, matching our own measurement, so the numbers line up. Dashes mark results SAM 3 does not report under this protocol. Parameter count is the paper's stated ~850 M (~450 M vision + ~300 M text encoders + ~100 M detector/tracker).

### Segmentation

See instance segmentation benchmark numbers

Architecture

COCO AP
50

COCO AP
50:95

Latency (ms)

Params (M)

Resolution

License

RF-DETR-Seg-N

63.0

40.3

3.4

33.6

312x312

Apache 2.0

RF-DETR-Seg-S

66.2

43.1

4.4

33.7

384x384

Apache 2.0

RF-DETR-Seg-M

68.4

45.3

5.9

35.7

432x432

Apache 2.0

RF-DETR-Seg-L

70.5

47.1

8.8

36.2

504x504

Apache 2.0

RF-DETR-Seg-XL

72.2

48.8

13.5

38.1

624x624

Apache 2.0

RF-DETR-Seg-2XL

73.1

49.9

21.8

38.6

768x768

Apache 2.0

YOLOv8-N-Seg

45.6

28.3

3.5

3.4

640x640

AGPL-3.0

YOLOv8-S-Seg

53.8

34.0

4.2

11.8

640x640

AGPL-3.0

YOLOv8-M-Seg

58.2

37.3

7.0

27.3

640x640

AGPL-3.0

YOLOv8-L-Seg

60.5

39.0

9.7

46.0

640x640

AGPL-3.0

YOLOv8-XL-Seg

61.3

39.5

14.0

71.8

640x640

AGPL-3.0

YOLOv11-N-Seg

47.8

30.0

3.6

2.9

640x640

AGPL-3.0

YOLOv11-S-Seg

55.4

35.0

4.6

10.1

640x640

AGPL-3.0

YOLOv11-M-Seg

60.0

38.5

6.9

22.4

640x640

AGPL-3.0

YOLOv11-L-Seg

61.5

39.5

8.3

27.6

640x640

AGPL-3.0

YOLOv11-XL-Seg

62.4

40.1

13.7

62.1

640x640

AGPL-3.0

YOLO26-N-Seg

54.3

34.7

2.31

2.7

640x640

AGPL-3.0

YOLO26-S-Seg

62.4

40.2

3.47

10.4

640x640

AGPL-3.0

YOLO26-M-Seg

67.8

44.0

6.32

23.6

640x640

AGPL-3.0

YOLO26-L-Seg

69.8

45.5

7.58

28.0

640x640

AGPL-3.0

YOLO26-X-Seg

71.6

46.8

12.92

62.8

640x640

AGPL-3.0

### Keypoints

See keypoint detection benchmark numbers

Architecture

COCO AP
50:95

Latency (ms)

Params (M)

License

RF-DETR Keypoint (Preview)

71.8

9.7

40.7

Apache 2.0

YOLO11-pose N

48.9

3.2

2.9

AGPL-3.0

YOLO11-pose S

57.5

3.4

9.9

AGPL-3.0

YOLO11-pose M

64.2

5.2

20.9

AGPL-3.0

YOLO11-pose L

65.2

6.6

26.2

AGPL-3.0

YOLO11-pose X

68.6

10.6

58.8

AGPL-3.0

YOLO26-pose N

55.9

1.9

2.9

AGPL-3.0

YOLO26-pose S

62.0

2.7

10.4

AGPL-3.0

YOLO26-pose M

68.0

4.6

21.5

AGPL-3.0

YOLO26-pose L

69.2

5.9

25.9

AGPL-3.0

YOLO26-pose X

71.0

9.8

57.6

AGPL-3.0

Keypoint benchmarks report AP50:95(OKS-based); this is the standard COCO keypoint comparison metric.

### NAS on the Roboflow Platform

Since the paper release, we have improved RF-DETR NAS training on the Roboflow platform even further. A single training run gives you every model size, with results that beat not only the open-source checkpoints but also our own paper NAS results.Try it now!

## Run Models

### Detection

RF-DETR provides multiple model sizes, ranging from Nano to 2XLarge. To use a different model size, replace the class name in the code snippet below with another class from the table.

import
 
supervision
 
as
 
sv

from
 
rfdetr
 
import
 
RFDETRMedium

from
 
rfdetr
.
assets
.
coco_classes
 
import
 
COCO_CLASSES

model
 
=
 
RFDETRMedium
()

detections
 
=
 
model
.
predict
(
"https://media.roboflow.com/dog.jpg"
, 
threshold
=
0.5
)

labels
 
=
 [
f"
{
COCO_CLASSES
[
class_id
]
}
"
 
for
 
class_id
 
in
 
detections
.
class_id
]

annotated_image
 
=
 
sv
.
BoxAnnotator
().
annotate
(
detections
.
metadata
[
"source_image"
], 
detections
)

annotated_image
 
=
 
sv
.
LabelAnnotator
().
annotate
(
annotated_image
, 
detections
, 
labels
)

Note:COCO_CLASSESworks for COCO-pretrained models. For fine-tuned models, usedetections.data["class_name"]instead — it resolves class names from the checkpoint and works for both COCO and custom datasets.

Run RF-DETR with Inference

You can also run RF-DETR models using the Inference library. To switch model size, select the appropriate inference package alias from the table below.

import
 
requests

import
 
supervision
 
as
 
sv

from
 
PIL
 
import
 
Image

from
 
inference
 
import
 
get_model

model
 
=
 
get_model
(
"rfdetr-medium"
)

image
 
=
 
Image
.
open
(
requests
.
get
(
"https://media.roboflow.com/dog.jpg"
, 
stream
=
True
).
raw
)

predictions
 
=
 
model
.
infer
(
image
, 
confidence
=
0.5
)[
0
]

detections
 
=
 
sv
.
Detections
.
from_inference
(
predictions
)

annotated_image
 
=
 
sv
.
BoxAnnotator
().
annotate
(
image
, 
detections
)

annotated_image
 
=
 
sv
.
LabelAnnotator
().
annotate
(
annotated_image
, 
detections
)

Size

RF-DETR package class

Inference package alias

COCO AP
50

COCO AP
50:95

Latency (ms)

Params (M)

Resolution

License

N

RFDETRNano

rfdetr-nano

67.6

48.4

2.3

30.5

384x384

Apache 2.0

S

RFDETRSmall

rfdetr-small

72.1

53.0

3.5

32.1

512x512

Apache 2.0

M

RFDETRMedium

rfdetr-medium

73.6

54.7

4.4

33.7

576x576

Apache 2.0

L

RFDETRLarge

rfdetr-large

75.1

56.5

6.8

33.9

704x704

Apache 2.0

XL

RFDETRXLarge
 △

rfdetr-xlarge

77.4

58.6

11.5

126.4

700x700

PML 1.0

2XL

RFDETR2XLarge
 △

rfdetr-2xlarge

78.5

60.1

17.2

126.9

880x880

PML 1.0

△ Requires therfdetr_plusextension:pip install rfdetr[plus]. SeeLicensefor details.

### Segmentation

RF-DETR supports instance segmentation with model sizes from Nano to 2XLarge. To use a different model size, replace the class name in the code snippet below with another class from the table.

import
 
supervision
 
as
 
sv

from
 
rfdetr
 
import
 
RFDETRSegMedium

from
 
rfdetr
.
assets
.
coco_classes
 
import
 
COCO_CLASSES

model
 
=
 
RFDETRSegMedium
()

detections
 
=
 
model
.
predict
(
"https://media.roboflow.com/dog.jpg"
, 
threshold
=
0.5
)

labels
 
=
 [
f"
{
COCO_CLASSES
[
class_id
]
}
"
 
for
 
class_id
 
in
 
detections
.
class_id
]

annotated_image
 
=
 
sv
.
MaskAnnotator
().
annotate
(
detections
.
metadata
[
"source_image"
], 
detections
)

annotated_image
 
=
 
sv
.
LabelAnnotator
().
annotate
(
annotated_image
, 
detections
, 
labels
)

Run RF-DETR-Seg with Inference

You can also run RF-DETR-Seg models using the Inference library. To switch model size, select the appropriate inference package alias from the table below.

import
 
requests

import
 
supervision
 
as
 
sv

from
 
PIL
 
import
 
Image

from
 
inference
 
import
 
get_model

model
 
=
 
get_model
(
"rfdetr-seg-medium"
)

image
 
=
 
Image
.
open
(
requests
.
get
(
"https://media.roboflow.com/dog.jpg"
, 
stream
=
True
).
raw
)

predictions
 
=
 
model
.
infer
(
image
, 
confidence
=
0.5
)[
0
]

detections
 
=
 
sv
.
Detections
.
from_inference
(
predictions
)

annotated_image
 
=
 
sv
.
MaskAnnotator
().
annotate
(
image
, 
detections
)

annotated_image
 
=
 
sv
.
LabelAnnotator
().
annotate
(
annotated_image
, 
detections
)

Size

RF-DETR package class

Inference package alias

COCO AP
50

COCO AP
50:95

Latency (ms)

Params (M)

Resolution

License

N

RFDETRSegNano

rfdetr-seg-nano

63.0

40.3

3.4

33.6

312x312

Apache 2.0

S

RFDETRSegSmall

rfdetr-seg-small

66.2

43.1

4.4

33.7

384x384

Apache 2.0

M

RFDETRSegMedium

rfdetr-seg-medium

68.4

45.3

5.9

35.7

432x432

Apache 2.0

L

RFDETRSegLarge

rfdetr-seg-large

70.5

47.1

8.8

36.2

504x504

Apache 2.0

XL

RFDETRSegXLarge

rfdetr-seg-xlarge

72.2

48.8

13.5

38.1

624x624

Apache 2.0

2XL

RFDETRSeg2XLarge

rfdetr-seg-2xlarge

73.1

49.9

21.8

38.6

768x768

Apache 2.0

### Keypoints

RF-DETR supports keypoint detection (preview) withRFDETRKeypointPreview, pretrained on COCO person keypoints.

from
 
rfdetr
 
import
 
RFDETRKeypointPreview

model
 
=
 
RFDETRKeypointPreview
()

key_points
 
=
 
model
.
predict
(
"image.jpg"
, 
threshold
=
0.5
)

Size

RF-DETR package class

COCO AP
50:95

Latency (ms)

Params (M)

Resolution

License

Keypoint (Preview)

RFDETRKeypointPreview

71.8

9.7

40.7

576x576

Apache 2.0

### Train Models

RF-DETR supports training for object detection, instance segmentation, and keypoint detection (preview). You can train models inGoogle Colabor directly on the Roboflow platform. Below you will find a step-by-step video fine-tuning tutorial.

## Documentation

Visit ourdocumentation websiteto learn more about how to use RF-DETR.

## License

Licensing is split by component:

* The open-sourcerfdetrpackage and Apache-designated model weights are licensed under Apache License 2.0. SeeLICENSE.
* Plus components, including therfdetr_plusextension and RF-DETR-XL / RF-DETR-2XL detection models, are licensed under PML 1.0.

## Acknowledgements

Our work is built uponLW-DETR,DINOv2, andDeformable DETR. Thanks to their authors for their excellent work!

## Citation

If you find our work helpful for your research, please consider citing the following BibTeX entry.

@inproceedings
{
robinson2026rfdetr
,
 
title
 = 
{
RF-DETR: Real-Time Detection Transformer
}
,
 
author
 = 
{
Robinson, Isaac and Robicheaux, Peter and Popov, Matvei and Ramanan, Deva and Peri, Neehar
}
,
 
booktitle
 = 
{
International Conference on Learning Representations (ICLR)
}
,
 
year
 = 
{
2026
}
,
 
url
 = 
{
https://arxiv.org/abs/2511.09554
}

}

## Contribute

We welcome and appreciate all contributions! If you notice any issues or bugs, have questions, or would like to suggest new features, pleaseopen an issueor pull request. By sharing your ideas and improvements, you help make RF-DETR better for everyone.