---
title: Shoggoth Mini
url: https://www.matthieulc.com/posts/shoggoth-mini
site_name: hackernews
fetched_at: '2025-07-16T07:04:18.317156'
original_url: https://www.matthieulc.com/posts/shoggoth-mini
author: cataPhil
date: '2025-07-16'
description: Matthieu Le Cauchois's website
---

Over the past year, robotics has been catching up with the LLM era. Pi’s π0.5can clean unseen homes. Tesla’s Optimus can follownatural language cooking instructions. These systems are extremely impressive, but they feel stuck in a utilitarian mindset of robotic appliances. For these future robots to live with us, they must be expressive. Expressiveness communicates internal state such as intent, attention, and confidence. Beyond its functional utility as a communication channel, expressiveness makes interactions feel natural. Without it, you get the textbookuncanny valleyeffect.

Earlier this year, I came across Apple’sELEGNTpaper, which frames this idea rigorously through a Pixar-like lamp to show how posture and timing alone can convey intention. Around the same time, I discoveredSpiRobs, a soft tentacle robot that feels oddly alive with just simple movements. One system was carefully designed to express intent while the other just moved, yet somehow felt like it had intent. That difference was interesting. I started building Shoggoth Mini as a way to explore it more directly. Not with a clear goal, but to see what would happen if I pushed embodiment into stranger territory. This post retraces that process, the happy accidents, and what I learned about building robots.

ELEGNT
SpiRobs

SpiRobs demo

# Hardware

The first challenge was creating a testbed to explore the control of SpiRobs. I started very simple: a plate to hold three motors, and a dome to lift the tentacle above them. This setup wasn’t meant to be the final design, only a platform for quick experimentation. However, halfway through 3D printing, I ran out of black filament and had to finish the dome in grey. This made it look like the dome had a mouth. When my flatmate saw it sitting on my desk, he grabbed a marker and drew some eyes. It looked good: cute, weird, slightly unsettling. I used ChatGPT to explore renders, and decided that this accident would become the form factor.

Later, I mounted stereo cameras on the dome to track the tentacle. Robot eyes are eerie. You keep expecting movement, but nothing ever happens. That prediction errorfocuses attention even more.

The original open-spool design relied on constant cable tension, but any slight perturbation (such as testing a buggy new policy) would make the cables leave the spool and tangle around the motor shafts. The process to fix it required untying the knot at the tip holding the cables together, and dismantling the whole robot. Adding simple spool covers eliminated most tangles and made iteration dramatically faster.

Another key step was adding a calibration script and pre-rolling extra wire length. This made it possible to:

* Unroll and reroll the cables to open the robot without having to untie the tip knot, speeding up iteration dramatically
* Calibrate cable tension precisely and as often as needed
* Give control policies slack to work with during motion

Rolling the cables back after working on Shoggoth Mini's insides

Finally, as you can see in the video, the standard 3-cable SpiRobs design sags under its own weight. This makes consistent behavior hard to reproduce. I had to thicken the spine just enough to prevent sag, but not so much that it would deform permanently under high load.

You can explore the current CAD assembly here, with all STL files for 3D printing included in therepo.

This is an interactive 3D model - click and drag to rotate, scroll to zoom

# Manual control

With the hardware ready, the next step was to feel how the tentacle moved. To simplify control, I reduced the tentacle’s three tendon lengths (a 3D space) down to two intuitive dimensions you can manipulate with a trackpad.

Concretely, each of the three tendons has a principal pulling direction in the 2D plane, forming a triangular basis that sums to zero. By projecting the 2D cursor control vector onto each tendon’s principal axis, you compute how much each tendon should shorten or lengthen to align with the desired direction.

This projection is linear:

$$
s_i = \mathbf{v}_i^\top \mathbf{c}
$$

where:

* $\mathbf{c}$ is the 2D cursor vector,
* $\mathbf{v}_i$ is the principal axis of tendon $i$.

Positive $s_i$ means shortening the tendon; negative means lengthening it. In practice, the cursor input is normalized to keep the motor commands in a reasonable range.

While this 2D mapping doesn’t expose the tentacle’s full configuration space (there are internal shapes it cannot reach), it is intuitive. Anyone can immediately move the tentacle by dragging on a trackpad, seeing the tip follow the cursor in the same direction.

Unexpectedly, this simple 2D-to-3D mapping became the backbone of the entire system. Later, all automated control policies, from hardcoded primitives to reinforcement learning, reused the same projection layer to output actions.

Trackpad control

# System design

The system has two control layers. Low-level control uses both open-loop primitives (like “<yes>” or “<shake>”) and closed-loop RL policies (like finger-tracking). The latter depends on a specialized stereo vision pipeline, which tracks the tentacle tip and user hand positions. Initially, I considered embedding internal optical sensors for proprioception, but this proved impractical without adding bulk, so I stuck with external stereo vision instead. While this works, it limits the usable field of view. To address this, I implemented a somewhat natural-looking homing behavior if the tip goes out of frame, and restricted the RL observation space to ensure it remains visible.

High-level control leverages GPT-4o’s real-time API, which streams audio and text (vision isn’t exposed yet). GPT-4o continuously listens to speech through the audio stream, while stereo vision is processed locally to detect high-level visual events—like hand waves or proximity triggers—which are sent to GPT-4o as text cues ("<user waving>" or “<finger near>”). GPT-4o then decides, zero-shot, which low-level API calls to make. This follows the approach shown in DeepMind’sGemini Roboticspaper, where a vision-language-action (VLA) model zero-shots control of ALOHA 2 by generating Python control code without robot-specific fine-tuning. In practice, GPT-4o tends to overcall or undercall actions (the question of time calibration of LLMs is tricky), so prompt engineering was essential.

I initially considered training a single end-to-end VLA model. Projects like Hugging Face’sLeRobotlean hard on imitation learning. That works for rigid arms because the end-effector pose maps cleanly to joint angles, so a replayed trajectory usually does what you expect. A cable-driven soft robot is different: the same tip position can correspond to many cable length combinations. This unpredictability makes demonstration-based approaches difficult to scale.

Instead, I went with a cascaded design: specialized vision feeding lightweight controllers, leaving room to expand into more advanced learned behaviors later.

One thing I noticed was that the tentacle would look slightly lifeless during pauses between API calls. To address this, I added a breathing idle mode with small, noisy oscillations that shift between principal directions, keeping it feeling alive even when not actively responding.

I don't know about you but I find idle mode sooo weird - Turn sound on for full vibes

# Perception

Perception required two components: hand tracking and tentacle tip tracking. For hands, MediaPipe worked reasonably well out of the box, though it struggles with occlusions.

For the tentacle, I collected a dataset across varied lighting, positions, and backgrounds, using k-means clustering to filter for diverse, non-redundant samples.Roboflow’s auto-labeling and active learning sped up annotation, and I augmented the dataset synthetically by extracting tentacle tips via theSegment Anything demo.

Once the data was ready, training a YOLO model withUltralyticswas straightforward. The final calibration step used aDeepLabCut notebookto compute camera intrinsics and extrinsics, enabling 3D triangulation of the tentacle tip and hand positions.

Triangulation procedure

Real-time 3D triangulation of hand and tentacle

# Low-level control API

Programming open-loop behaviors for soft robots is uniquely hard. Unlike rigid systems where inverse kinematics can give you precise joint angles for a desired trajectory, soft bodies deform unpredictably. To simplify, I reused the2D control projection from manual control. Instead of thinking in raw 3D cable lengths, I could design behaviors in an intuitive 2D space and let the projection handle the rest. Having a thicker spine that prevents sag also helped ensure consistent behavior reproduction across different sessions.

Experimenting with object interactions made me appreciate how robust SpiRobs can be. The grabbing primitive, for example, simply pulls the front cable while adding slack to the others, yet it reliably grips objects of varying shapes and weights. Given that high-frequency dexterous manipulation remains challenging1, this mechanical robustness is a non-trivial design opportunity.

## Reinforcement Learning

For closed-loop control, I turned to reinforcement learning, starting with a policy that would follow a user’s finger. This came from an old idea I’ve always wanted to make: a robotic wooden owl that follows you with its big eyes. It was also simple enough to validate the entire sim-to-real stack end-to-end before moving to more complex policies.

I recreated SpiRobs in MuJoCo and set up a target-following environment with smooth, randomized trajectories. I used PPO with a simple MLP and frame stacking to provide temporal context. To improve sim-to-real transfer, I added dynamics randomization, perturbing mass, damping, and friction during training.

Manual control in MuJoCo

My first approach used direct tendon lengths as the action space. The policy quickly found reward-hacking strategies, pulling cables to extremes to achieve perfect tracking in simulation. In reality, these chaotic configurations would never transfer.

Reward hacking

A fix I found was to constrain the action space to the same2D projectionused everywhere else. This representation blocked unrealistic behaviors while keeping the system expressive enough. Note that you could use curriculum learning to gradually transition from this 2D constraint to full 3D control by starting with the simplified representation and progressively expanding the action space as the policy becomes more stable.

Another issue was that the policy exhibited jittery behavior from rapid action changes between timesteps. I added control penalties to the reward function that penalized large consecutive action differences, encouraging smooth movements over erratic corrections.

Jittery policy before adding control penalties

Once the policy stabilized in simulation, transfer to hardware was surprisingly smooth.

Simulation

Not simulation

One last issue: even with a stationary target, the policy would sometimes jitter and oscillate unpredictably as it overcorrected. Applying an exponential moving average to the actions added enough damping to let the tentacle settle quietly without sacrificing responsiveness too much.

Raw predicted action

With action smoothing

# Conclusion

One thing I noticed toward the end is that, even though the robot remained expressive, it started feeling less alive. Early on, its motions surprised me: I had to interpret them, infer intent. But as I internalized how it worked, the prediction error faded.

Expressiveness is about communicating internal state. But perceived aliveness depends on something else: unpredictability, a certain opacity. This makes sense: living systems track a messy, high-dimensional world. Shoggoth Mini doesn’t.

This raises a question: do we actually want to build robots that feel alive? Or is there a threshold, somewhere past expressiveness, where the system becomes too agentic, too unpredictable to stay comfortable around humans?

Looking forward, I see several short-term paths worth exploring:

* Giving it a voice (but as non-human as possible!)
* Ditching the constrained 2D control space
* Expanding the expression repertoire, both open and closed-loop, potentially through RLHF
* Adding more tentacles and teaching it to crawl
* Using direct drive motors to reduce noise

Fork therepo, build your own, or get in touch if you’d like to discuss robotics, RL, or LLMs!

# Citation

@misc
{
lecauchois2025shoggothmini
,


author

=

{Le Cauchois, Matthieu B.}
,


title

=

{Shoggoth Mini: Expressive and Functional Control of a Soft Tentacle Robot}
,


howpublished

=

"\url{https://github.com/mlecauchois/shoggoth-mini}"
,


year

=

{2025}

}

1. Although we are witnessing impressive progress like withGeneralist AIdemonstrating end-to-end neural control with precise force modulation and cross-embodiment generalization.↩︎
