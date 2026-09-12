---
title: Inverse Kinematics and Foot Locking
url: https://theorangeduck.com/page/inverse-kinematics-foot-locking
date: 2026-09-07
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-09-13T02:06:42.759137
---

# Inverse Kinematics and Foot Locking

# Inverse Kinematics and Foot Locking – Summary

## Solving a Leg Chain  
- Goal: adjust local joint rotations so the toe reaches a target while preserving the original pose.  
- Steps:  
  1. Compute the heel target by adding the original heel‑to‑toe offset to the desired toe position.  
  2. Apply a two‑bone IK solver to position the hip and knee for the heel target.  
  3. Rotate the heel joint to point the toe toward the toe target.  
  4. Optionally rotate the toe end to resolve ground collisions.  
- IK implementation highlights:  
  - Uses a softened clamp (`maxExtension` + `softening`) to avoid hyper‑extension; the target is exponentially eased as it approaches the maximum length.  
  - Determines a stable rotation axis from the knee’s side vector, eliminating the need for an explicit pole‑vector.  
  - Rotations are built from quaternion exponentials (`QuaternionFromScaledAngleAxis`) and applied in world space before converting back to local space.

## Foot Locking  
- Problem: keep the toe stationary during contact while the rest of the body moves.  
- Solution: employ **inertialization** (smooth blending of rotation/position over a short time) to transition the toe from IK‑driven motion to a locked state and back.  
- Runtime workflow:  
  1. Detect contact (e.g., foot‑ground collision).  
  2. Capture the current toe transform as the lock pose.  
  3. Blend the toe’s transform toward the lock pose using an exponential decay curve.  
  4. When contact ends, blend back to the IK‑driven pose.  
- This approach yields a natural “foot‑sticking” effect without abrupt jumps.

## Contact Times  
- Automatic annotation of foot‑ground contacts in animation data:  
  - Sample the foot’s world‑space trajectory.  
  - Detect intervals where the foot’s vertical velocity crosses zero and its height is within a tolerance of the ground.  
  - Mark these intervals as contact phases, storing start/end frames for later use.  
- Benefits: removes the need for manual key‑frame tagging and enables consistent foot‑locking across varied animations.

## Offline Foot Locking  
- When the full animation clip is available, foot sliding can be corrected post‑process:  
  1. Identify contact intervals using the method above.  
  2. For each interval, compute the average foot position and enforce it as a constant (or smoothly interpolated) trajectory.  
  3. Re‑apply the IK solver to the remaining frames, preserving the locked foot pose during contacts.  
  4. Optionally smooth the transition between locked and free phases to avoid visual pops.  
- This technique is useful for polishing pre‑recorded animations or generating clean motion‑capture data.

## Conclusion & Philosophical Thoughts  
- Foot sliding is a pervasive issue; solutions blend mathematics (IK, quaternion algebra) with artistic judgment (how much slip is acceptable).  
- No single “best” method exists; the presented recipes serve as practical starting points that can be adapted per project.  
- Emphasizes iterative experimentation: adjust parameters like `maxExtension`, `softening`, and inertialization decay to match the desired visual style.  
- Encourages developers to treat foot locking as part of a broader animation pipeline rather than an isolated fix.