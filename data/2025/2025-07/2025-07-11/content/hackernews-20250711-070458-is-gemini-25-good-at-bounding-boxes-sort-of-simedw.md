---
title: Is Gemini 2.5 good at bounding boxes? Sort of... - SimEdw's Blog
url: https://simedw.com/2025/07/10/gemini-bounding-boxes/
site_name: hackernews
fetched_at: '2025-07-11T07:04:58.127856'
original_url: https://simedw.com/2025/07/10/gemini-bounding-boxes/
author: Simon Edwardsson
date: '2025-07-11'
published_date: '2025-07-10'
description: Can Gemini 2.5 replace CNN for object detection?
---

# Is Gemini 2.5 good at bounding boxes? Sort of...

July 10, 2025

TL;DR Gemini 2.5 Pro is a decent object detector, matching Yolo V3 from 2018 on MS-COCO val.

Multimodal Large Language Models keep getting better, but are they ready to dethrone CNNs in computer vision tasks like object detection? The allure of skipping dataset collection, annotation, and training is too enticing not to waste a few evenings testing.

I decided to write a small benchmark and check Gemini 2.5 on MS-COCO, focusing on object detection. You can find the code and more resultshere.

Hover or tap to switch between ground truth (green) and Gemini predictions (blue) bounding boxes

## Dataset

MS-COCOis a classic in the object detection world, sure it's a bit dated and the masks/bounding boxes aren't super tight, still, it has a long history and it should be easy to place Gemini among the historical results.

There are 80 classes, frompersontotoothbrush. Object boundaries can sometimes be ambiguous, but this tends to even out across the dataset.

The validation set, which you are not supposed to train on, contains 5000 images. However there are no guarantees that Gemini didn't vacuum it up during its training.

COCO sees four cakes, Gemini sees only one

## Prompt

I've embedded the list of valid classes from MS-COCO into the prompt, and asked it to follow my JSON output schema. I deliberately avoided explicitly mentioning COCO by name in case Gemini had seen it during training.

Full prompt

Look carefully at this image and detect ALL visible objects, including small ones.

IMPORTANT: Focus on finding as many objects as possible, even if they are small, distant, or partially visible.
Make sure that the bounding box is as tight as possible.
Valid object classes: {class_list}

For each detected object, provide:

-
 "label": exact class name from the list above

-
 "confidence": how certain you are (0.0 to 1.0)

-
 "box_2d": bounding box [ymin, xmin, ymax, xmax] normalized 0-1000

-
 "mask": binary mask of the object in the image, as a base64 encoded string

Detect everything you can see that matches the valid classes. Don't be conservative - include objects even if you're only moderately confident.

Return as JSON array:
[
 {
 "label": "person",
 "confidence": 0.95,
 "box_2d": [100, 200, 300, 400],
 "mask": "..."
 },
 {
 "label": "kite",
 "confidence": 0.80,
 "box_2d": [50, 150, 250, 350],
 "mask": "..."
 }
]

Confidence is important for calculating the Average Precision (see Measure section), however, from experience and some sampling the output only partially correlates with better matches.

I ran this prompt with and without structured output, and to burn a bit more credits I also tried both with and without a thinking budget (1024 tokens). For Pro, a thinking budget of *128 tokens is the minimum, I also tried with 2048 tokens. The Gemini documentation recommends to turn it off, and looking at the result that seems like sound advice.

Initially, I wrote 1024 tokens, but it was pointed out that the minimum is in fact 128. I have updated the results table, but it didn't change the overall outcome.

## Measure

In object detection, mAP (mean Average Precision) is essentially the average precision of the model's predictions across multiple overlap thresholds (Intersection over Union - IoU), typically ranging from 0.5 to 0.95. Higher values are better. The goal here is to collapse a graph showing how precision changes as recall changes into a single number, since it's much easier to benchmark with a single number.

Here is some pseudo code, not sure if it makes things any clearer, there are also a lot of guides floating around for mAP with nice illustrations:

def

iou
(
box_a
,

box_b
):


return

intersection_area
(
box_a
,

box_b
)

/

union_area
(
box_a
,

box_b
)

def

calculate_ap
(
threshold
):


# Mark predictions as True or False positives based on IoU threshold


for

prediction

in

predictions
:


prediction
.
true_positive

=

iou
(
prediction
,

ground_truth
)

>

threshold


# Sort predictions by confidence (important for the curve!)


predictions

=

sorted
(
predictions
,

key
=
lambda

x
:

x
.
confidence
,

reverse
=
True
)


true_positives

=

0


false_positives

=

0


precision_values

=

[]


recall_values

=

[]


total_ground_truth

=

len
(
ground_truth_objects
)


for

prediction

in

predictions
:


if

prediction
.
true_positive
:


true_positives

+=

1


else
:


false_positives

+=

1


precision

=

true_positives

/

(
true_positives

+

false_positives
)


recall

=

true_positives

/

total_ground_truth


precision_values
.
append
(
precision
)


recall_values
.
append
(
recall
)


# Calculate area under precision-recall curve


return

area_under_curve
(
precision_values
,

recall_values
)

# Finally average over multiple thresholds

mAP

=

sum
(
calculate_ap
(
threshold
)

for

threshold

in

[
0.50
,

0.55
,

...
,

0.95
])

/

10

## Results

The results are fairly clear:

* Pro is better than Flash, which is better than Flash-Lite.
* Adding a thinking budget reduces the performance significantly.
* Unstructured output was better for Flash and Flash-Lite but worse for Pro.
* Pro is much better at not returning invalid outputs.

Model

Think Tokens

Mode

mAP

[email protected]

Errors (# invalid outputs)

Avg Time

flash

0

structured

0.224

0.381

47/5000

0.18s

flash

0

unstructured

0.261

0.417

57/5000

0.20s

flash

1024

structured

0.160

0.311

23/5000

0.27s

flash

1024

unstructured

0.161

0.319

19/5000

0.28s

pro

128

structured

0.332

0.495

5/5000

0.20s

pro

1024

structured

0.340

0.517

6/5000

0.46s

pro

2048

structured

0.325

0.506

5/5000

0.30s

pro

1024

unstructured

0.288

0.438

25/5000

0.47s

pro

2048

unstructured

0.277

0.434

26/5000

0.54s

flash-lite

0

structured

0.156

0.279

335/5000

0.37s

flash-lite

0

unstructured

0.211

0.338

216/5000

0.23s

flash-lite

1024

structured

0.140

0.273

168/5000

0.27s

flash-lite

1024

unstructured

0.215

0.364

114/5000

0.24s

This means Gemini Pro 2.5 structured (~0.34 mAP) is roughly on par withYolo v3(2018, ~0.33 mAP). State-of-the-art models likeCo-DETRreach ~0.60 mAP.

I also wanted to add amaskoutput (base64 RLE encoded) as I thought it might increase the bounding box performance. Unfortunately, including themaskfield caused the model to spiral into infinite loops, spewing out meaningless tokens, and burning my budget (maybe 5% of the time, but enough that I didn't complete the testing).

Sometimes Gemini is better than the ground truth

## Conclusion

This benchmark isn't entirely fair, since CNNs are explicitly trained on these 80 classes. Even so, Gemini 2.5 Pro held its own surprisingly well. Loose bounding boxes can easily be refined by segmentation models like SAM. CNNs remain faster, cheaper, and easier to reason about, especially with good training data, but Gemini's versatility across open-set tasks feels almost magical. I'll definitely be using it in my side projects going forward.

## Related work

Simon Willisoncovered this earlier this year, I recommend checking out his visualiser, and most of his blog posts for that matter.

The paperHow Well Does GPT-4o Understand Vision? Evaluating Multimodal Foundation Models on Standard Computer Vision Taskscompares various large models on vision tasks, but they don't just prompt for bounding box coordinates, instead they do "recursive zooming", essentially dividing the image into a grid of cells and ask the model if part of objects are present in each grid. And then do this recursively on grids with objects.
This is different from my benchmark which is just asking for all the objects at once.
