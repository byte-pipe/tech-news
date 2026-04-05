---
title: 'GitHub - roboflow/supervision: We write your reusable computer vision tools. 💜 · GitHub'
url: https://github.com/roboflow/supervision
site_name: github
content_file: github-github-roboflowsupervision-we-write-your-reusable
fetched_at: '2026-04-05T11:12:28.535963'
original_url: https://github.com/roboflow/supervision
author: roboflow
description: We write your reusable computer vision tools. 💜. Contribute to roboflow/supervision development by creating an account on GitHub.
---

roboflow

 

/

supervision

Public

* NotificationsYou must be signed in to change notification settings
* Fork3.3k
* Star37.7k

 
 
 
 
develop
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

4,792 Commits
4,792 Commits
.github
.github
 
 
docs
docs
 
 
examples
examples
 
 
src/
supervision
src/
supervision
 
 
tests
tests
 
 
.codecov.yml
.codecov.yml
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
AGENTS.md
AGENTS.md
 
 
CITATION.cff
CITATION.cff
 
 
CLAUDE.md
CLAUDE.md
 
 
LICENSE.md
LICENSE.md
 
 
README.md
README.md
 
 
demo.ipynb
demo.ipynb
 
 
mkdocs.yml
mkdocs.yml
 
 
pyproject.toml
pyproject.toml
 
 
release_process.md
release_process.md
 
 
tox.ini
tox.ini
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

notebooks|inference|autodistill|maestro

## 👋 hello

We write your reusable computer vision tools.Whether you need to load your dataset from your hard drive, draw detections on an image or video, or count how many detections are in a zone. You can count on us! 🤝

## 💻 install

Pip install the supervision package in aPython>=3.9environment.

pip install supervision

Read more about conda, mamba, and installing from source in ourguide.

## 🔥 quickstart

### models

Supervision was designed to be model agnostic. Just plug in any classification, detection, or segmentation model. For your convenience, we have createdconnectorsfor the most popular libraries like Ultralytics, Transformers, MMDetection, or Inference. Other integrations, likerfdetr, already returnsv.Detectionsdirectly.

Install the optional dependencies for this example withpip install pillow rfdetr.

import
 
supervision
 
as
 
sv

from
 
PIL
 
import
 
Image

from
 
rfdetr
 
import
 
RFDETRSmall

image
 
=
 
Image
.
open
(...)

model
 
=
 
RFDETRSmall
()

detections
 
=
 
model
.
predict
(
image
, 
threshold
=
0.5
)

len
(
detections
)

# 5

👉 more model connectors

* inferenceRunning withInferencerequires aRoboflow API KEY.importsupervisionassvfromPILimportImagefrominferenceimportget_modelimage=Image.open(...)model=get_model(model_id="rfdetr-small",api_key="ROBOFLOW_API_KEY")result=model.infer(image)[0]detections=sv.Detections.from_inference(result)len(detections)# 5

### annotators

Supervision offers a wide range of highly customizableannotators, allowing you to compose the perfect visualization for your use case.

import
 
cv2

import
 
supervision
 
as
 
sv

image
 
=
 
cv2
.
imread
(...)

detections
 
=
 
sv
.
Detections
(...)

box_annotator
 
=
 
sv
.
BoxAnnotator
()

annotated_frame
 
=
 
box_annotator
.
annotate
(
scene
=
image
.
copy
(), 
detections
=
detections
)

supervision-0.16.0-annotators.mp4

### datasets

Supervision provides a set ofutilsthat allow you to load, split, merge, and save datasets in one of the supported formats.

import
 
supervision
 
as
 
sv

from
 
roboflow
 
import
 
Roboflow

project
 
=
 
Roboflow
().
workspace
(
"WORKSPACE_ID"
).
project
(
"PROJECT_ID"
)

dataset
 
=
 
project
.
version
(
"PROJECT_VERSION"
).
download
(
"coco"
)

ds
 
=
 
sv
.
DetectionDataset
.
from_coco
(
 
images_directory_path
=
f"
{
dataset
.
location
}
/train"
,
 
annotations_path
=
f"
{
dataset
.
location
}
/train/_annotations.coco.json"
,
)

path
, 
image
, 
annotation
 
=
 
ds
[
0
]

# loads image on demand

for
 
path
, 
image
, 
annotation
 
in
 
ds
:
 
# loads image on demand

 
pass

👉 more dataset utils

* loaddataset=sv.DetectionDataset.from_yolo(images_directory_path=...,annotations_directory_path=...,data_yaml_path=...,
)dataset=sv.DetectionDataset.from_pascal_voc(images_directory_path=...,annotations_directory_path=...,
)dataset=sv.DetectionDataset.from_coco(images_directory_path=...,annotations_path=...,
)
* splittrain_dataset,test_dataset=dataset.split(split_ratio=0.7)test_dataset,valid_dataset=test_dataset.split(split_ratio=0.5)len(train_dataset),len(test_dataset),len(valid_dataset)# (700, 150, 150)
* mergeds_1=sv.DetectionDataset(...)len(ds_1)# 100ds_1.classes# ['dog', 'person']ds_2=sv.DetectionDataset(...)len(ds_2)# 200ds_2.classes# ['cat']ds_merged=sv.DetectionDataset.merge([ds_1,ds_2])len(ds_merged)# 300ds_merged.classes# ['cat', 'dog', 'person']
* savedataset.as_yolo(images_directory_path=...,annotations_directory_path=...,data_yaml_path=...,
)dataset.as_pascal_voc(images_directory_path=...,annotations_directory_path=...,
)dataset.as_coco(images_directory_path=...,annotations_path=...,
)
* convertsv.DetectionDataset.from_yolo(images_directory_path=...,annotations_directory_path=...,data_yaml_path=...,
).as_pascal_voc(images_directory_path=...,annotations_directory_path=...,
)

## 🎬 tutorials

Want to learn how to use Supervision? Explore ourhow-to guides,end-to-end examples,cheatsheet, andcookbooks!

Dwell Time Analysis with Computer Vision | Real-Time Stream Processing

Created: 5 Apr 2024

Learn how to use computer vision to analyze wait times and optimize processes. This tutorial covers object detection, tracking, and calculating time spent in designated zones. Use these techniques to improve customer experience in retail, traffic management, or other scenarios.

Speed Estimation & Vehicle Tracking | Computer Vision | Open Source

Created: 11 Jan 2024

Learn how to track and estimate the speed of vehicles using YOLO, ByteTrack, and Roboflow Inference. This comprehensive tutorial covers object detection, multi-object tracking, filtering detections, perspective transformation, speed estimation, visualization improvements, and more.

## 💜 built with supervision

Did you build something cool using supervision?Let us know!

football-players-tracking-25.mp4

traffic_analysis_result.mov

vehicles-step-7-new.mp4

## 📚 documentation

Visit ourdocumentationpage to learn how supervision can help you build computer vision applications faster and more reliably.

## 🏆 contribution

We love your input! Please see ourcontributing guideto get started. Thank you 🙏 to all our contributors!

## About

We write your reusable computer vision tools. 💜

supervision.roboflow.com

### Topics

 python

 tracking

 machine-learning

 computer-vision

 deep-learning

 metrics

 tensorflow

 image-processing

 pytorch

 video-processing

 yolo

 classification

 coco

 object-detection

 hacktoberfest

 pascal-voc

 low-code

 instance-segmentation

 oriented-bounding-box

### Resources

 Readme

 

### License

 MIT license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

37.7k

 stars
 

### Watchers

228

 watching
 

### Forks

3.3k

 forks
 

 Report repository

 

## Releases35

supervision-0.27.0.post

 Latest

 

Mar 14, 2026

 

+ 34 releases

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python100.0%

 Generated from 
roboflow/template-python