---
title: Strange Attractors | Shashank Tomar
url: https://blog.shashanktomar.com/posts/strange-attractors
site_name: hackernews_api
fetched_at: '2025-11-02T11:08:14.705461'
original_url: https://blog.shashanktomar.com/posts/strange-attractors
author: Shashank Tomar
date: '2025-10-31'
published_date: '2025-09-05'
description: A visualisation of Strange Attractors using a Threejs particle system. In this post, I will try to explain the basics of dynamical systems, chaos theory, attractors and the butterfly effect.
tags:
- hackernews
- trending
---

A few months back, while playing around withThree.js, I came across something that completely derailed my plans. Strange attractors - fancy math that creates beautiful patterns. At first I thought I'd just render one and move on, but then soon I realized that this is too much fun. When complexity emerges from three simple equations, when you see something chaotic emerge into beautiful, it's hard not to waste some time. I've spent countless hours, maybe more than I'd care to admit, watching these patterns form. I realized there's something deeply satisfying about seeing order emerge from randomness. Let me show you what kept me hooked.

## The Basics: Dynamical Systems and Chaos Theory

Dynamical Systems are a mathematical way to understand how thingschange over time. Imagine you have a system, which
could be anything from the movement of planets to the growth of a population. In this system, there are rules that
determine how it evolves from one moment to the next. These rules tell you what will happen next based on what is
happening now. Some examples are, a pendulum, the weather patterns, a flock of birds, the spread of a virus in a
population (we are all too familiar with this one), and stock market.

There are two primary things to understand about this system:

* Phase Space: This is like a big collection of all the possible states the system can be in. Each state is like a
snapshot of the system at a specific time. This is also called thestate spaceor theworld state.
* Dynamics: These are the rules that takes one state of the system and moves it to the next state. It can be
represented as a function that transforms the system from now to later.

Figure 1 - Phase Space in Dynamical Systems

For instance, when studying population growth, a phase-space (world-state) might consist of the current population size
and the rate of growth or decline at a specific time. The dynamics would then be derived from models of population
dynamics, which, considering factors like birth rates, death rates, and carrying capacity of the environment, dictate
the changes in population size over time.

Another way of saying this is that the dynamical systems describe how things change over time, in a space of
possibilities, governed by a set of rules. Numerous fields such as biology, physics, economics, and applied mathematics,
study systems like these, focusing on the specific rules that dictate their evolution. These rules are grounded in
relevant theories, such as Newtonian mechanics, fluid dynamics, and mathematics of economics, among others.

### Chaos Theory

There are different ways of classifying dynamical systems, and one of the most interesting is the classification into
chaotic and non-chaotic systems. The change over time in non-chaotic systems is more deterministic as compared to
chaotic systems which exhibit randomness and unpredictability.

Chaos Theoryis the sub branch of dynamical systems that studies chaotic systems and challenges the traditional
deterministic views of causality. Most of the natural systems we observe are chaotic in nature, like the weather, a drop
of ink dissolving in water, social and economic behaviours etc. In contrast, systems like the movement of planets,
pendulums, and simple harmonic oscillators are extremely predictable and non-chaotic.

Chaos Theory deals with systems that exhibit irregular and unpredictable behavior over time, even though they follow
deterministic rules. Having a set of rules that govern the system, and yet exhibit randomness and unpredictability,
might seem a bit contradictory, but it is because the rules do not always represent the whole system. In fact, most of
the time, these rules are an approximation of the system and that is what leads to the unpredictability. In complex
systems, we do not have enough information to come up with a perfect set of rules. And by using incomplete information
to make predictions, we introduce uncertainty, which amplifies over time, leading to the chaotic behaviour.

Figure 2 - Unpredictability in Chaos Theory

Chaotic systems generally have many non-linear interacting components, which we partially understand (or can partially
observe) and which are very sensitive to small changes. A small change in the initial conditions can lead to a
completely different outcome, a phenomenon known as thebutterfly effect. In this post, we will try to see the
butterfly effect in action but before that, let's talk aboutStrange Attractors.

## Strange Attractors

To understand Strange Attractors, let's first understand what an attractor is. As discussed earlier, dynamical systems
are all aboutchange over time. During this change, the system moves through different possible states (remember the
phase space jargon?). An attractor is a set of states towards which a system tends to settle over time, or you can say,
towards which it isattracted. It's like a magnet that pulls the system towards it.

For example, think of a pendulum. When you release it, it swings back and forth, but eventually, it comes to rest at the
bottom. The bottom is the attractor in this case. It's the state towards which the pendulum is attracted.

This happens due to the system's inherent dynamics, which govern how states in the phase space change. Here are some of
the reasons why different states get attracted towards attractors:

* Stability: Attractors are stable states of the system, meaning that once the system reaches them, it tends to stay
there. This stability arises from the system's dynamics, which push it towards the attractor and keep it there.
* Dissipation: Many dynamical systems have dissipative forces, which cause the system to lose energy over time. This
loss of energy leads the system to settle into a lower-energy state, which often corresponds to an attractor. This is
what happens in the case of the pendulum.
* Contraction: In some regions of the phase space, the system's dynamics cause trajectories to converge. This
contraction effect means that nearby states will tend to come closer together over time, eventually being drawn
towards the attractor.

Figure 3 - Attractor state in a simple pendulum

Some attractors have complex governing equations that can create unpredictable trajectories or behaviours. These
nonlinear interactions can result in multiple stable states or periodic orbits, towards which the system evolves. These
complex attractors are categorised asstrange attractors. They are called "strange" due to their unique
characteristics.

1. Fractal Structure: Strange attractors often have a fractal-like structure, meaning they display intricate
patterns that repeat at different scales. This complexity sets them apart from simpler, regular attractors.
2. Sensitive Dependence on Initial Conditions: Systems with strange attractors are highly sensitive to their initial
conditions. Small changes in the starting point can lead to vastly different long-term behaviors, a phenomenon known
as the "butterfly effect".
3. Unpredictable Trajectories: The trajectories on a strange attractor never repeat themselves, exhibiting
non-periodic motion. The system's behavior appears random and unpredictable, even though it is governed by
deterministic rules.
4. Emergent Order from Chaos: Despite their chaotic nature, strange attractors exhibit a form of underlying order.
Patterns and structures emerge from the seemingly random behavior, revealing the complex dynamics at play.

You can observe most of these characteristics in the visualisation. The one which is most fascinating to observe is the
butterfly effect.

### The Butterfly Effect

A butterfly can flutter its wings over a flower in China and cause a hurricane in the Caribbean.

One of the defining features of strange attractors is their sensitivity to initial conditions. This means that small
changes in the starting state of the system can lead to vastly different long-term behaviors, a phenomenon known as thebutterfly effect. In chaotic systems, tiny variations in the initial conditions can amplify over time, leading to
drastically different outcomes.

Figure 3 - A Simplification of The Bufferfly Effect

In our visualisation, let's observe this behavior on Thomas Attractor. It is governed by the following equations:

### Thomas Attractor Equation

1
float
 a
=

0.19
;
2

3
dx
=

(
-
a
*
x
+

sin
(
y
)
)

*
 dt
;
4
dy
=

(
-
a
*
y
+

sin
(
z
)
)

*
 dt
;
5
dz
=

(
-
a
*
z
+

sin
(
x
)
)

*
 dt
;
1
float
 a
=

0.19
;
2

3
dx
=

(
-
a
*
x
+

sin
(
y
)
)

*
 dt
;
4
dy
=

(
-
a
*
y
+

sin
(
z
)
)

*
 dt
;
5
dz
=

(
-
a
*
z
+

sin
(
x
)
)

*
 dt
;

A small change in the parameteracan lead to vastly different particle trajectories and the overall shape of the
attractor. Change this value in the control panel and observe the butterfly effect in action.

a = 0.19
a = 0.21
a = 0.13
a = 0.10

There is another way of observing the butterfly effect in this visualisation. Change theInitial Statefromcubetosphere surfacein the control panel and observe how the particles move differently in the two cases. The particles
eventually get attracted to the same states but have different trajectories.

## Implementation Details

This visualization required rendering a large number of particles using Three.js. To achieve this efficiently, we used a
technique calledping-pong rendering2. This method handles iterative updates of particle systems directly on the GPU,
minimizing data transfers between the CPU and GPU. It utilizes two frame buffer objects (FBOs) that alternate roles: One
stores the current state of particles and render them on the screen, while the other calculates the next state.

### Implementation Workflow

1. Setting Up Frame Buffer Objects (FBOs):We start by creating two FBOs,pingandpong, to hold the current and
next state of particles. These buffers store data such as particle positions in RGBA channels, making efficient use
of GPU resources.typescript1constping=newTHREE.WebGLRenderTarget(size,size,{2minFilter:THREE.NearestFilter,3magFilter:THREE.NearestFilter,4format:THREE.RGBAFormat,5stencilBuffer:false,6type:THREE.FloatType,7});89constpong=newTHREE.WebGLRenderTarget(size,size,{10minFilter:THREE.NearestFilter,11magFilter:THREE.NearestFilter,12format:THREE.RGBAFormat,13stencilBuffer:false,14type:THREE.FloatType,15});1constping=newTHREE.WebGLRenderTarget(size,size,{2minFilter:THREE.NearestFilter,3magFilter:THREE.NearestFilter,4format:THREE.RGBAFormat,5stencilBuffer:false,6type:THREE.FloatType,7});89constpong=newTHREE.WebGLRenderTarget(size,size,{10minFilter:THREE.NearestFilter,11magFilter:THREE.NearestFilter,12format:THREE.RGBAFormat,13stencilBuffer:false,14type:THREE.FloatType,15});
2. Shader Programs for Particle Dynamics:The shader programs execute on the GPU and apply attractor dynamics to
each particle. Following is the attractor function which update the particle positions based on the attractor equation.glsl1vec3attractor(vec3pos){2floata=0.16;3floatx=pos.x,y=pos.y,z=pos.z;4floatdt=0.015;56floatdx,dy,dz;7dx=(-a*x+sin(y))*dt;8dy=(-a*y+sin(z))*dt;9dz=(-a*z+sin(x))*dt;10returnvec3(dx,dy,dz);11}1vec3attractor(vec3pos){2floata=0.16;3floatx=pos.x,y=pos.y,z=pos.z;4floatdt=0.015;56floatdx,dy,dz;7dx=(-a*x+sin(y))*dt;8dy=(-a*y+sin(z))*dt;9dz=(-a*z+sin(x))*dt;10returnvec3(dx,dy,dz);11}
3. Rendering and Buffer Swapping:In each frame, the shader computes the new positions based on the attractor's
equations and stores them in the inactive buffer. After updating, the roles of the FBOs are swapped: The previously
inactive buffer becomes active, and vice versa.typescript1constcurrentTarget=flip?ping:pong;2constnextTarget=flip?pong:ping;34// Use current positions for calculations in shader5uniforms.positions.value=currentTarget.texture;67// Render the other on the screen8gl.setRenderTarget(nextTarget);9gl.clear();10gl.render(scene,camera);11gl.setRenderTarget(null);1213flip=!flip;1constcurrentTarget=flip?ping:pong;2constnextTarget=flip?pong:ping;34// Use current positions for calculations in shader5uniforms.positions.value=currentTarget.texture;67// Render the other on the screen8gl.setRenderTarget(nextTarget);9gl.clear();10gl.render(scene,camera);11gl.setRenderTarget(null);1213flip=!flip;

This combination of efficient shader calculations and the ping-pong technique allows us to render the particle system.

If you have any comments, please leave them onthis GitHub discussions topic. Sooner or later, I will integrate it with the blog. Thehacker newsdiscussion can be foundhere.

#### Footnotes

1. When the Butterfly Effect Took
Flight[↩]
2. WebGLFundamentals: Ping Pong Rendering[↩]

#### References

* Inspired by the work of Maxim
* Wikipedia: Attractor
* Wikipedia: List Of Chaotic Maps
* Dynamical Systems Theory: What in the World is it?

#### Related Links

* https://fusefactory.github.io/openfuse/strange%20attractors/particle%20system/Strange-Attractors-GPU/
* https://chaoticatmospheres.com/mathrules-strange-attractors
* https://www.dynamicmath.xyz/strange-attractors/
* https://www.reddit.com/r/math/comments/z0dmms/visualization_of_3d_strange_attractors
* https://www.clicktorelease.com/code/codevember-2016/3
* https://discourse.mcneel.com/t/strange-attractors/120053
* https://www.reddit.com/r/generative/comments/191fkkv/genuary_day_8_chaotic_system/
