---
title: 'MolmoAct 2: An open foundation for robots that work in the real world | Ai2'
url: https://allenai.org/blog/molmoact2
site_name: tldr
content_file: tldr-molmoact-2-an-open-foundation-for-robots-that-work
fetched_at: '2026-05-06T20:20:54.686849'
original_url: https://allenai.org/blog/molmoact2
date: '2026-05-06'
description: MolmoAct 2 is a fully open robotics foundation model that brings faster, stronger 3D action reasoning to real-world robot tasks, alongside a major new bimanual manipulation dataset for researchers to study, reproduce, and build on.
tags:
- tldr
---

# MolmoAct 2: An open foundation for robots that work in the real world

May 5, 2026

Ai2

Share
Models
Tech Report
Data
Code

AI writes our emails, debugs our code, and books flights for us. In the physical world, though, it still struggles. Getting a robot to reliably load a dishwasher or prep test tube samples in a lab is still far beyond what most systems can dependably do for hours on end. Yet these are the places where capable machines would matter most—handling the repetitive work that's toughest to staff and accelerating scientific discovery.

The past year has brought real progress in robotics foundation models, moving us closer to fully autonomous robots. But the underlying recipes remain largely closed. Some teams release weights, fewer release data, and almost none publish enough for researchers to closely study or meaningfully improve on the work.

Last August, we launchedMolmoAct, the first Action Reasoning Model (ARM)—a new class of models that reason about their environment in 3D before they act. Today we're releasingMolmoAct 2, a substantial upgrade that outperforms capable proprietary robotics models on industry benchmarks, handles various real-world tasks out of the box without per-task fine-tuning, and runs up to 37x faster than its predecessor—vastly expanding the types of work it can do. Alongside MolmoAct 2, we're releasing theMolmoAct 2-Bimanual YAM dataset, the largest open-source bimanual tabletop manipulation robotics dataset ever published, with over 720 hours of training demonstrations.

MolmoAct 2, the MolmoAct 2-Bimanual YAM dataset, and our updated VLA pipeline with a novel adapter architecture are available for researchers to study and build on—including the model weights, datasets, and our adaptive reasoning approach that helps MolmoAct 2 reason more deeply in 3D to boost performance and interpretability.

### Rethinking MolmoAct for reasoning, from architecture to data

MolmoAct was trained on 22 hours of curated in-house data generated over a period of 3 months – about 10.6K trajectories, each a successful recording of a robot arm completing a manipulation task across kitchens, bathrooms, bedrooms, living rooms, and tabletop setups – plus a filtered subset of Open X-Embodiment, a community-aggregated dataset pooled from dozens of robotics labs. While MolmoAct served to prove that an open, reasoning-based architecture could beat much larger closed models on industry-standard benchmarks, MolmoAct 2 is built to deploy in real-world environments.

To create MolmoAct 2, we reimagined the architecture. MolmoAct 2 isn’t simply initialized from Molmo 2, butMolmo 2-ER, a specialized embodied-reasoning variant of Molmo 2. We trained Molmo 2-ER by further training Molmo 2 on an additional ~3M embodied-reasoning examples covering image-based pointing, object detection, abstract spatial reasoning, multi-image reasoning, and image- and video-based spatial question answering.

That stronger reasoning backbone shows up directly in evaluation. Across 13 embodied-reasoning benchmarks covering pointing, multi-image reasoning, ego-exo correspondence, and video spatial reasoning, Molmo 2-ER scores an average of 63.8 out of 100—ahead of systems including GPT-5, Gemini 2.5 Pro, Qwen3-VL-8B, and GR-ER 1.5.

MolmoAct 2 pairs Molmo 2-ER with a dedicated action expert that generates robot actions through flow matching, connected to the VLM through a KV-cache bridge. MolmoAct 2 also has an open action tokenizer; Physical Intelligence's FAST tokenizer is one of the field's most useful recent contributions, but the data used to train it hasn’t been openly released. We've builtMolmoAct 2-FAST Tokenizer, a fully open-source reimplementation trained on our data, and published it with MolmoAct 2.

As a result of these and other improvements, MolmoAct 2's inference is dramatically faster. A single action call takes about 180 ms in the base model and 790 ms in MolmoAct 2 with adaptive depth reasoning, versus 6,700 ms in MolmoAct (running in the LIBERO benchmark environment with 1 NVIDIA H100)—the difference between a robot that pauses visibly between movements and one that responds to its environment in near-real time.

We also introduceMolmoAct 2-Think, which augments MolmoAct 2 with depth perception tokens for tasks that benefit from explicit 3D reasoning. To avoid unnecessary computation, our adaptive-depth mechanism routes depth prediction only when it’s expected to improve task performance. This enables MolmoAct 2 to reason more deeply about 3D spatial structure while maintaining efficient inference. Instead of predicting depth tokens for all image patches, the model focuses depth prediction on regions with dynamic scene changes, reducing the latency of dense depth-token prediction and achieving a 17% speedup compared to full depth-token prediction.

To train MolmoAct 2, we created the MolmoAct 2-Bimanual YAM dataset, a 700-hour collection of robot demonstrations involving two machine arms working together, covering coordinated tasks such as folding a towel, scanning groceries, charging a smartphone, and table bussing. MolmoAct 2-Bimanual YAM dataset is the largest open-source bimanual robotics dataset ever released, and contains over 30x the robot data used for MolmoAct. We curated MolmoAct 2-Bimanual YAM dataset with support fromCortex AI.

MolmoAct was capable of bimanual manipulation via per-task fine-tuning; MolmoAct 2 has bimanual capabilities baked into the base model, so users get it out of the box.

We supplemented MolmoAct 2-Bimanual YAM dataset with a broader mix of robot datasets that expose MolmoAct 2 to different arms, camera setups, control schemes, and task styles. That includes large-scale SO-100/SO-101 datasets from low-cost open-source robot arms; filtered DROID Franka data for real-world single-arm manipulation across varied scenes; Google Robot BC-Z and Fractal data from Open X-Embodiment, which add many examples of instruction-conditioned robot manipulation; Bridge WidowX data, which broadens coverage to another commonly used robot setup; and MolmoAct’s original training data, preserving the household and tabletop manipulation skills that grounded the first model.

We also improved the language side of the robot data. Many robotics datasets reuse repetitive task labels or contain low-quality annotations such as test-run strings. To make instructions more accurate and diverse, we re-annotated robot demonstrations with an open VLM, increasing the number of unique labels from ~71K to ~146K across the dataset mixture.

### Evaluating across simulation, adaptation, and real-world robot tasks

We put MolmoAct 2 through one of our most rigorous robotics evaluations to date, covering simulation, zero-shot deployment, and post-training adaptation to new robot settings.

MolmoAct 2 performs strongly in simulation. On MolmoBot, our household manipulation benchmark, it averages a 20.6% success rate across all tasks—roughly double the score of Physical Intelligence’s π0.5 (10.3%). (MolmoBot is intended to be difficult; many baselines score in the single digits.) On RoboEval, a bimanual manipulation benchmark designed to capture more than simple pass/fail outcomes, MolmoAct 2 scores 0.443 versus 0.405 for π0.5 (higher is better).

In real-world zero-shot tests on a Franka arm, MolmoAct 2 outperforms both π0.5 and our prior MolmoBot model across every task we evaluated, from straightforward pick-and-place tasks like moving an apple onto a plate to more precise tasks like putting a pipette into a tray, placing a small red cube into the center of a tape roll, or putting a knife into a box. Across 15 trials per task, MolmoAct 2 reaches 100% success on apple-on-plate, 86.7% on pipette-in-tray, 93.3% on red-cube-in-tape-roll, 93.3% on knife-in-box, and 62% on the longer-horizon task of moving several objects into a bowl. Overall, MolmoAct 2 averages 87.1% success, compared with 48.4% for MolmoBot and 45.2% for π0.5.

We also evaluated MolmoAct 2 after post-training on single-arm and bimanual tasks such as setting, bussing, and wiping a table; putting a bowl in a sink; lifting a tray; and folding a towel. MolmoAct 2 performs especially well on towel folding, bowl placement, table wiping, and tray lifting, showing how the model can be adapted to practical manipulation behaviors via post-training.

And on LIBERO, a benchmark measuring how well a model can acquire and retain many skills over time, MolmoAct 2 reaches a 97.2% average success rate after post-training while MolmoAct 2-Think reaches 98.1%. That improves over MolmoAct by roughly 10.6 and 11.5 points, respectively.

Some of the in-lab evaluations described here were conducted on YAM arms donated by I2RT Robotics. I2RT had no role in the development of MolmoAct 2, the design of the evaluations, or the reporting of these results. We’re grateful for their contributions.

To validate MolmoAct 2 beyond our own lab evaluations, we retained Cortex AI, a robotics data and evaluation company, to conduct a third-party benchmark of MolmoAct 2’s real-world fine-tuning performance. Cortex AI evaluated five robotics policies including MolmoAct 2 across multiple bimanual tasks using a systematic many-trial setup.

MolmoAct 2 achieved the highest average score at 0.51, ahead of OpenVLA-OFT at 0.36, π0.5 at 0.32, Cosmos Policy at 0.16, and X-VLA at 0.05. It also had the strongest task-level showing, ranking first on 7 of 8 tasks, including returning a test tube to a tray, storing candy, putting tools away, putting toys away, storing cups, preparing the pipette tip, and making popcorn.

### Deploying in the real world

The real test for any robotics model is whether it works outside controlled environments, where instructions vary and small mistakes can compound over time. MolmoAct 2 is designed to be easier to guide in those settings without retraining the whole model. It can respond to natural-language instructions and use visual traces that show the path a user wants the robot to take, making MolmoAct 2’s behavior easier to interpret and fine-tune.

To lower the barrier to deployment, we've also published a reference robot hardware setup for MolmoAct 2 that pairs two YAM arms with an overhead Intel RealSense D435 camera, two D405 cameras for close-up views, an extendable mount, and a simple tabletop workspace—giving researchers a simple starting point for tabletop and bimanual manipulation work.

We’ve been piloting MolmoAct 2 with research partners since early this year, including researchers from theCong Labat Stanford School of Medicine, led by Professor Le Cong. The lab is working toward a self-driving wetlab that can accelerate genome engineering, making it a useful stress test for robotics models: the environment is unstructured, the tasks require repeated precision, and small errors can accumulate over the course of an experiment.

In these workflows, a MolmoAct 2-driven arm handles routine manipulation steps in CRISPR gene-editing experiments, such as moving samples between stations and operating benchtop equipment. After testing a range of generalist robotics models fine-tuned to their workflow, the Stanford team found that MolmoAct 2 shows strong potential to streamline key parts of wetlab operations and, in turn, accelerate scientific discovery.

Separately, we’ve also tested internally how MolmoAct 2 handles changes that mirror real deployment: rephrased instructions, shifted object positions, distractor objects in the scene, and object substitutions. These stress tests probe whether the model can follow the intent of an instruction even when the exact scene differs from training.

Together, these pilots and evaluations help us understand not just whether MolmoAct 2 can complete a task in a controlled setting, but how well it holds up when the environment changes frequently around it.

### Built to be studied and extended

MolmoAct 2 is a highly capable model, but it still has limitations. Like other robot systems, it can struggle when its own gripper blocks the camera’s view, when the model can’t respond as quickly as the robot’s control system, or when a task requires especially fine-grained manipulation. And its visual-trace steering capability is still early—2D traces from human operators can introduce depth-axis errors.

These are exactly the kinds of challenges that shared foundations can help the field tackle—models researchers can inspect, datasets they can build on, and (coming soon) training code they can adapt to new machines and situations. MolmoAct 2 is meant to help set that standard, building on the groundwork we laid last year with MolmoAct and translating our earlier research into tangible impact.

Taking actions in the physical world is one of AI’s hardest frontiers, and we think the open path is the best way forward. Download thetechnical artifactsand let us know what you build with them—and where we can improve.

## Subscribe to receive monthly updates about the latest Ai2 news.

First Name
Last Name
Email
Sign up