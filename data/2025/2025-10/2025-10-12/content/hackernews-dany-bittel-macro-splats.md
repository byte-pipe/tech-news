---
title: Dany Bittel, Macro Splats
url: https://danybittel.ch/macro.html
site_name: hackernews
fetched_at: '2025-10-12T19:09:02.642188'
original_url: https://danybittel.ch/macro.html
author: danybittel
date: '2025-10-12'
---

# Macro Splats 2025

A Gaussian splat is essentially a bunch of blurry ellipsoids. Each one has a view-dependent color, using a process similar to training an AI model, you can optimize until it converges to the photos you feed in. The result is a sort of 3D photograph that can be viewed freely from any angle.Captivated by this possibility, I wanted to create splats of macro subjects. The hairy, fuzzy textures and complex structures of insects make them a perfect fit for this technique.In theory, creating a splat is as simple as filming the object from all sides. Unfortunately, the extremely shallow depth of field in macro photography completely throws this process off. If you feed unsharp photos into it, the resulting model will contain unsharp areas as well.Thankfully, there’s a common technique in macro photography called focus stacking, where multiple images taken from the same angle but with slightly different focal points are combined into one fully sharp photo. A single stack usually contains anywhere from 50 to 500 images. Since I needed to photograph the subject from many angles, I optimized the process to use as few photos per stack as possible and settled on 16. I shot at a small aperture of f/18 to maximize depth of field. The diffraction introduced by this setup can be minimized later in post.To capture the specimen from all angles, covering a bit more than half a hemisphere, I mounted the insect on a rotary disk and tilted the camera up and down on a boom arm. A script rotated the disk by fixed increments, and each focus stack was captured using a WeMacro automated focus rail. The vertical angle was adjusted manually (only eight times), so it wasn’t a big issue. In total, I captured 111 perspectives. A full session of 1776 photos took about four hours. The main bottleneck is my Nikon D810, which isn’t built for such continuous shooting, it slows down to one frame every one or two seconds once the buffer fills up. I used a Tamron 90mm lens with a 20mm extension and shot in DX (cropped sensor) mode. Shorter lenses would change the perspective too much between focus areas, making image alignment impossible.After batch focus-stacking all the photos, I ended up with 111 fully sharp images. The camera positions could then be reconstructed inCOLMAP. I performed some color correction and background masking before feeding the data into training withPostshot. Out comes the splat, requiring only minimal retouching to remove the mounting.

# See it in 3D

You can view all the insects on mysuperspl.atpage.I’m also releasing the cluster fly model for free under a CC BY license:Download here. You’re free to use this model for both commercial and non-commercial purposes, as long as you provide credit.

© 2025, Dany Bittel
