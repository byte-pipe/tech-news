---
title: Rosenzweig – Hilariously Fast Volume Computation with the Divergence Theorem
url: https://alyssarosenzweig.ca/blog/hilariously-fast-volume-computation-with-the-divergence-theorem.html
site_name: hnrss
content_file: hnrss-rosenzweig-hilariously-fast-volume-computation-wit
fetched_at: '2026-08-28T21:21:32.750510'
original_url: https://alyssarosenzweig.ca/blog/hilariously-fast-volume-computation-with-the-divergence-theorem.html
date: '2026-08-28'
description: Hilariously fast volume computation with the divergence theorem (2018)
tags:
- hackernews
- hnrss
---

(No,
there won’t be jokes.)

The following presents a fast algorithm for volume computation of a
simple, closed, triangulated 3D mesh. This assumption is a consequence
of the divergence theorem. Further extensions may generalise to other
meshes as well, although that is presently out of scope.

We begin with the definition of volume as the triple integral over a
region of the constant one:

V=∭R1dVV = \iiint_R 1 \mathrm{d}V

Let𝐅\mathbf{F}be a function inℝ3\mathbb{R}^3such that its divergence is equal to one. For the purposes of this
paper, we choose:

𝐅(x,y,z)=<x,0,0>\mathbf{F}(x, y, z) = <x, 0, 0>

It can easily be verified that

div𝐅=∂F∂x+∂F∂y+∂F∂z=1+0+0=1\mathrm{div} \mathbf{F} = \frac{\partial F}{\partial x} + \frac{\partial F}{\partial y} + \frac{\partial F}{\partial z} = 1 + 0 + 0 = 1

Therefore,

V=∭R1dV=∭Rdiv𝐅(x,y,z)dVV = \iiint_R 1 dV = \iiint_R \mathrm{div} \mathbf{F}(x, y, z) \mathrm{d}V

By the Divergence Theorem, this is equal to the surface integral:

V=∬S𝐅(x,y,z)d𝐒V = \iint_S \mathbf{F}(x, y, z) \mathrm{d}\mathbf{S}

This surface integral, defined over the surface S of the 3D mesh, is
equal to the sum of its piecewise triangle parts. LetTiT_idenote the surface of theii’th
triangle in the mesh. Then,

V=∑i=0∬Ti𝐅(x,y,z)d𝐒V = \sum_{i = 0} \iint_{T_i} \mathbf{F}(x, y, z) \mathrm{d}\mathbf{S}

LetTinT_{in}represent thenn’th
vertex of theii’th
triangle. LetΔ1\Delta_1equal the vector difference betweenTi1T_{i1}andTi0T_{i0},
andΔ2\Delta_2likewise equal toTi2−Ti0T_{i2} - T{i0}.
Each individual triangleTiT_imay thus be parametrised as:

𝐫(u,v)=Ti0+uΔ1+vΔ2\mathbf{r}(u, v) = T_{i0} + u\Delta_1 + v\Delta_2

Then, simple differentiation yields:

𝐫u=Δ1\mathbf{r}_u = \Delta_1𝐫v=Δ2\mathbf{r}_v = \Delta_2

Therefore,

𝐫u×𝐫v=Δ1×Δ2\mathbf{r}_u \times \mathbf{r}_v = \Delta_1 \times \Delta_2

Thus, the surface integral can be rewritten in terms of this
parametrisation, substituting in the definition of𝐅\mathbf{F}as needed:

V=∑i=0∬Ti𝐅(x,y,z)(𝐫u×𝐫v)dAV = \sum_{i = 0} \iint_{T_i} \mathbf{F}(x, y, z) (\mathbf{r}_u \times \mathbf{r}_v) dA=∑i=0∬Ti𝐅(x,y,z)(̇Δi1×Δi2)dA= \sum_{i = 0} \iint_{T_i} \mathbf{F}(x, y, z) \dot (\Delta_{i1} \times \Delta_{i2}) dA=∑i=0∬Ti<x,0,0>(̇Δi1×Δi2)dA= \sum_{i = 0} \iint_{T_i} <x, 0, 0> \dot (\Delta_{i1} \times \Delta_{i2}) dA

This cross product is constant throughout the triangle and easy to
calculate from the vertex data. Only the X component of the cross
product should be calculated; the others are equal to zero due to the
dot product with the zero components of𝐅\mathbf{F}.VVcan be thus be rewritten as:

V=∑i=0(Δi1×Δi2)x∬TixdAV = \sum_{i = 0} (\Delta_{i1} \times \Delta_{i2})_x \iint_{T_i} x dA

We now focus on the surface integral∬TixdA\iint_{T_i} x dA.
Expanding with the parametrisation yields:

∬TixdA=∫01∫0uxdvdu=∫01∫0u(Ti0x+uΔi1x+vΔi2x)dvdu\iint_{T_i} x dA = \int_{0}^{1} \int_{0}^{u} x dv du = \int_{0}^{1} \int_{0}^{u} (T_{i0x} + u \Delta_{i1x} + v \Delta_{i2x}) dv du

This integral can be directly evaluated, treating vertex data as
constants:

∫01∫01−u(Ti0x+uΔi1x+vΔi2x)dvdu\int_{0}^{1} \int_{0}^{1-u} (T_{i0x} + u \Delta_{i1x} + v \Delta_{i2x}) dv du=Ti0x∫01∫01−udvdu+Δi1x∫01∫01−uudvdu+Δi2x)∫01∫01−uvdvdu= T_{i0x} \int_{0}^{1} \int_{0}^{1-u} dv du + \Delta_{i1x} \int_{0}^{1} \int_{0}^{1-u} u dv du + \Delta_{i2x}) \int_{0}^{1} \int_{0}^{1-u} v dv du=Ti0x(12)+Δi1x(16)+Δi2x(16)= T_{i0x} (\frac{1}{2}) + \Delta_{i1x} (\frac{1}{6}) + \Delta_{i2x} (\frac{1}{6})=Ti0x(12)+(Ti1x−Ti0x)(16)+(Ti2x−Ti0x)(16)= T_{i0x} (\frac{1}{2}) + (T_{i1x} - T_{i0x})(\frac{1}{6}) + (T_{i2x} - T_{i0x})(\frac{1}{6})=Ti0x(16)+(Ti1x)(16)+(Ti2x)(16)= T_{i0x} (\frac{1}{6}) + (T_{i1x})(\frac{1}{6}) + (T_{i2x})(\frac{1}{6})=16(Ti0x+Ti1x+Ti2x)= \frac{1}{6}(T_{i0x} + T_{i1x} + T_{i2x})

Substituting into the original sum and pulling out a constant factor
of16\frac{1}{6}to avoid the inner loop division, this yields the following compact
formula for the volume:

V=16∑i=0(Δi1×Δi2)x(Ti0x+Ti1x+Ti2x)V = \frac{1}{6} \sum_{i = 0} (\Delta_{i1} \times \Delta_{i2})_x (T_{i0x} + T_{i1x} + T_{i2x})

## Performance analysis

The final algorithm contains no numerical integration nor
differentiation. In contrast to common naive algorithms for volume,
which are equivalent to rendering the mesh and then sampling the render,
an expensive operation, there is only a single loop in this algorithm,
over the triangles. Thus, this algorithm for volume computation is O(n)
to the number of the triangles. Furthermore, the per-triangle
calculation is similarly efficient: given the natural expansion of the
cross product, the inner part contains seven additions and three
multiplications. On the outside of the loop is only a single
multiplication. Thus, for a mesh ofnntriangles, the algorithm requires8n−18n - 1additions and3n+13n + 1multiplications, or11n11nfloating point operations. This isveryfast.

For a ballpark number, if volume needs to be calculated every frame
in a high-performance 60 frames per second application, without the aid
of a GPU, only using the CPU capabilities of a$35
Raspberry Pi, around 30 million triangles could be measured every
frame.

## Motivation

The vector calculus exam is soon, and I need to study. Plus, who
doesn’t love 3D graphics?!

I would be (pleasantly) surprised if the algorithm is
novel.Further researchafterposting reveals the paperEfficient
Feature Extraction for 2D/3D Objects in Mesh Representationby Cha
Zheng and Tsuhan Chen, which appears to describe the same algorithm,
although the derivation is different. It was fun while it lasted!

Retourner à l’accueil