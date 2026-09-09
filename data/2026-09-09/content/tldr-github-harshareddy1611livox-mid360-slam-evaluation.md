---
title: 'GitHub - harshareddy1611/livox-mid360-slam-evaluation: Benchmarking KISS-ICP, DLIO, FAST-LIO2 and GLIM on Livox Mid360 datasets using ROS2 Humble and EVO trajectory evaluation against ground-truth data. · GitHub'
url: https://github.com/harshareddy1611/livox-mid360-slam-evaluation
site_name: tldr
content_file: tldr-github-harshareddy1611livox-mid360-slam-evaluation
fetched_at: '2026-09-09T21:30:56.711703'
original_url: https://github.com/harshareddy1611/livox-mid360-slam-evaluation
date: '2026-09-09'
description: Benchmarking KISS-ICP, DLIO, FAST-LIO2 and GLIM on Livox Mid360 datasets using ROS2 Humble and EVO trajectory evaluation against ground-truth data. - harshareddy1611/livox-mid360-slam-evaluation
tags:
- tldr
---

harshareddy1611

 

/

livox-mid360-slam-evaluation

Public

* NotificationsYou must be signed in to change notification settings
* Fork0
* Star6

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

22 Commits
22 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
configs
configs
 
 
data
data
 
 
docs
docs
 
 
recovered
recovered
 
 
results
results
 
 
scripts
scripts
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
TIERS_DATASET.md
TIERS_DATASET.md
 
 
View all files

## Repository files navigation

# Live Drone Dataset (Livox Mid-360 + Pixhawk)

In addition to the offline TIERS benchmark (seeTIERS_DATASET.md), this
repo evaluates the same four methods onlive recordings from an actual UAV
platform: a Livox Mid-360 mounted alongside a Pixhawk flight controller,
flown inside a VICON-tracked indoor arena. Unlike the TIERS runs, all four
methods here, includingGLIM in GPU mode, run directly on the Jetson
Orin NX, the platform's actual target hardware.

## Results

APE RMSE (translation, meters) across 7 clean sequences:

Method

batch1_00

batch1_07

batch2_01

batch2_02

batch2_03

batch2_04

batch2_05

Average

KISS-ICP

0.046

0.426

0.086

0.067

0.043

0.094

0.098

0.123

DLIO

0.089

0.110

0.086

0.100

0.096

0.090

0.104

0.096

FAST-LIO2

0.084

0.180

0.095

0.085

0.078

0.134

0.127

0.112

GLIM (GPU)

0.038

0.035

0.059

0.043

0.024

0.035

0.046

0.040

Ground truth: Pixhawk EKF pose (/mavros/local_position/pose, VICON-fused).
SE(3) Umeyama alignment viaevo.

## Key findings

* GLIM (GPU) wins decisively on every sequence, averaging 0.040m vs 0.096-0.123m
for the other three methods, driven by loop closure against the small, revisitable
VICON arena, and holding up consistently across the full flight duration.
* KISS-ICP is the most volatile: best-in-class on some sequences (0.043-0.098m)
but spikes to 0.426m on batch1_07, LiDAR-only ICP has no inertial backstop against
faster/more aggressive drone motion.
* DLIO and FAST-LIO2 perform similarly(0.096m vs 0.112m average), both far more
consistent than KISS-ICP across sequences.

## Dataset

Two recording sessions, 7 sequences total, flown in the same indoor
VICON-tracked arena:

Sequence

Duration

batch1_00

78.0 s

batch1_07

64.5 s

batch2_01

72.3 s

batch2_02

76.0 s

batch2_03

62.2 s

batch2_04

41.8 s

batch2_05

59.5 s

All sequences publish/livox/lidar(10 Hz, same per-point timestamp fields
as the Mid-360 TIERS data) and/livox/imu(200 Hz nominal).

Ground truth:/mavros/local_position/pose, the Pixhawk EKF's fusion of
VICON pose with onboard IMU/barometer, ~30 Hz. An alternative topic,/vicon/drone/drone/pose, gives pure unfused VICON at ~120 Hz for
cross-checking.

Startup trim: the drone sat stationary on the ground for the first ~3.5s
of every recording before takeoff. This period is trimmed from ground truth
and every method's output before evaluation viascripts/trim_startup.py,
a plain time-based trim, distinct fromtrim_dlio.py's zero-position
calibration-artifact trim used for the TIERS dataset.

## Environment

Indoor VICON-tracked arena with an obstacle course (rope-frame gates, cones,
a wooden pallet, stacked boxes), ceiling-mounted VICON cameras visible on
the truss.

## Map reconstruction

For each sequence: the APE error map (trajectory colored by per-pose error
against ground truth, same style as the TIERS benchmark above) followed by
the reconstructed point-cloud map, built by reprojecting every raw/livox/lidarscan into world frame using that method's own estimated
trajectory, then voxel-downsampling. Same technique regardless of method,
so results are directly comparable. Click any thumbnail to open the
full-resolution image.

batch1_00

KISS-ICP

FAST-LIO2

DLIO

GLIM

batch2_02

KISS-ICP

FAST-LIO2

DLIO

GLIM

batch2_05

KISS-ICP

FAST-LIO2

DLIO

GLIM

Compare against the environment photos above, the rectangular hall outline
and internal obstacle panels are recognizable in every method's reconstruction.

Note: the Ericsii FAST-LIO2 ROS2 port has its per-scan PCD-accumulation code
commented out upstream, sopcd_save_ennever writes a file, hence the
trajectory-reprojection approach above rather than a native map export.

## Reproducing

#
 batch run: all 7 clean sequences x all 4 methods, with GT extraction,

#
 startup trimming, and evo evaluation

bash scripts/run_drone_batch.sh

Or per-method, with the drone dataset's topics/configs:

python3 scripts/extract_gt.py 
<
bag
>
 --topic /mavros/local_position/pose --out gt_raw.tum
python3 scripts/trim_startup.py gt_raw.tum --out gt.tum --trim 3.5

bash scripts/run_kiss_icp.sh 
<
bag
>
 /livox/lidar
bash scripts/run_fastlio2.sh 
<
bag
>
 drone.yaml
bash scripts/run_dlio.sh 
<
bag
>
 /livox/lidar /livox/imu
bash scripts/run_glim.sh 
<
bag
>
 configs/glim/config_drone

## Platform

Jetson Orin NX (JetPack 6.2, CUDA 12.6), Ubuntu 22.04, ROS 2 Humble,
Livox Mid-360 + Pixhawk, GLIM runs in GPU mode.

## Author

Harsha Reddy