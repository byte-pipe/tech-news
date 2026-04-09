---
title: Algorithms for making interesting organic simulations
url: https://bleuje.com/physarum-explanation/
site_name: lobsters
fetched_at: '2025-07-14T23:07:17.208833'
original_url: https://bleuje.com/physarum-explanation/
date: '2025-07-14'
description: Article explaining simulation algorithms that produce complex organic behaviours, starting with the classic physarum algorithm from Jeff Jones.
tags: graphics, visualization
---

## Algorithms for making interesting organic simulations

The purpose of this article is to explain techiques that enabled me to make simulations like the one
 below, along with a lot of other organic looking things. We will focus on algorithmic techniques for
 artistic purpose
 rather than scientific meaning.

## 1. Physarum algorithm from Jeff Jones (2010)

Jeff Jones presented a simulation algorithm that reproduces the behavior of organisms such
 asPhysarum polycephalum.
 It is explained inthis
 paper.

Results typically look like this:(source: screenshots from implementation by Amanda
 Ghassaei)

### General principle

The basic idea is that particles (also called agents) move around, leaving a trail behind them and trying
 to follow the trails
 they detect.

Below is an interactive explanation of a single agent,without representing the trail update.Please don't mind the glitch after slider change :)

#### Detailed description of the algorithm

A large number of agents move in a 2D space.

At each iteration of the algorithm, agents deposit trail on an
 image called atrail map, just by adding a value to a pixel of the image. In the above
 illustration, each cell represents a pixel of the trail map image.

Agent attributes:2D position(x,y)orientation: ananglecalledheadingHere are the different steps for an iteration of the algorithm:1. Sensing:Each agent "looks" at three places: straight ahead, slightly right, and slightly
 left.sometimes not so slightlyThe distance from the agent to the 3 sensor places is defined by the parameterSensor
 Distance(SD).The side angle is a parameter calledSensor Angle(SA).The agent detects the trail intensity at those three positions/pixels.2. Rotation and movement:If the highest value is to the left or right, the agent turns in that direction.The turn angle is controlled by the parameterRotation Angle(RA).If the highest value is straight ahead, the agent doesn't rotate.Actually in the case where straight ahead is the lowest value, the agent makes a random choice
 between left and right.After potentially turning, the agent moves forward by a distance calledMove Distance(MD).3. Deposit:the agents add a value to the trail map at their new position.4. Trail diffusion and decay:At each iteration, after deposit of all agents, the trail is slightly diffused (a sort of blur effect on
 the image), and multiplied by adecay factor(for example0.75) to
 keep things stable. A more precise
 explanation will be given later.Although the trail is a 2D
 image,
 artistically it's often better not to display it directly, and instead only show the
 particles.By modifying the four main parameters (SD, SA, RA, MD), various simulated behaviors can be observed.

 The algorithm from Jeff Jones can have more complex features than this but I'm giving a simple version
 that's used for what is described next in this article.### Real interactive implementation with few agents.The simulation below implements the algorithm, there are just too few particles and too few pixels for
 cool
 structures to appear!You can check outthis
 very nice webpageby Amanda Ghassaei, to see the simulation with a lot of particles and with
 controllable sliders.Another explanation/review of this algorithm from Jeff Jones can be foundhere. It has a pretty drawing to sum up
 the algorithm.Show explanation image by Sage Jenson## 2.36 Pointsby Sage Jenson (2019-2022)A more complex version of the previous algorithm can be found in the work36 Pointsby Sage Jenson, which
 displays amazing varied behaviours. Press letters or digits of your keyboard to
 change the Point.26 letters + 10 digits = 36It uses a single algorithm and each Point represents different parameters, which result
 in different behaviours.

 A Point corresponds to a behaviour obtained with 20 parameters (so mathematically this project shows 36
 points of ℝ²⁰).The above images show 6 Points.(found there)### Main ideaLooking at the code we can understand some clever ideas. The most important one is to make the parameters
 of the classic algorithm different depending on the value\( x \)of the trail map at
 the particle's position.The formulas below are used:$$
 \begin{eqnarray}
 \text{sensor distance} &=& p_1 + p_2 \cdot x^{p_3} \nonumber \\
 \text{sensor angle} &=& p_4 + p_5 \cdot x^{p_6} \nonumber \\
 \text{rotation angle} &=& p_7 + p_8 \cdot x^{p_9} \nonumber \\
 \text{move distance} &=& p_{10} + p_{11} \cdot x^{p_{12}}
 \end{eqnarray}
 $$For each iteration, we first get the value\( x \)of the trail map at the particle's
 position,
 and then with the previous formulas we just do the same as the previous classic algorithm. That gives us
 12
 parameters to play with instead of 4.Below is an update of the animated explanation with a single agent. This is using fixed parameters.I think adding interactive sliders to control the 12 parameters wouldn't add much value for the
 explanation.### Other ideaThere are 2 other parameters that are important to use: two offsets to rather get\( x
 \)near the particle position.The first one is an absolute vertical offset\( p_{13} \)("absolute" meaning the
 heading of the particle
 doesn't matter). The second one,\( p_{14} \), is an offset relatively to the
 particle's heading (getting \( x \) ahead of the particle),A piece of code for that part can look like this:### RespawnAnother thing in36 Pointsis that in addition to position and heading attributes, there is a
 progress
 attribute so that a particle periodically respawns at a random position.### Other commentsSimply by using variations of these 14 parameters, very different and interesting behaviours can be
 obtained. At this point maybe we should not call the results "physarum simulations", but rather
 "speculative biology" as Sage seems to state.I haven't used the 6 other parameters from36 Points: for example the decay factor is one of
 them (I use a fixed value to 0.75).Sage's piece of code(link)that
 implements the particle update with these techniques
 has the followinglicense:License Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License## 3. Bleuje implementationYou can find my implementation of the previous algorithm on github:physarum-36pAlthough I use the techniques described in the previous part that come from36 Points, my
 implementation is different, and because of that I added a 15th parameter to make some points of36
 Pointswork. It's simply some rescaling factor for the sensed \( x \). A lot of points from36 Pointsdon't work at all with my implementation, and those that work mostly give different
 behaviours. I also added new points.Below is a video showing what this implementation produces for 22 different Points (each one having 15
 parameters).Below is a description of what the code is doing.### Real-time setupIn order to have real-time fast computation, we can use shaders to compute the algorithm on the GPU. I'm
 using compute shaders and openFrameworks to manage them and the interface. The particles updates are
 done in parallel, same for the trail map updates in other shaders. It can run smoothly with millions of
 particles.There are 4 shaders:A shader that just resets counters to zero.Particle update/move, incrementing counter on new pixel postion.Trail deposit from counter, and pretty image production.Diffusion + decay on trail map.### Diffusion and decay algorithmThe diffusion is using a 3x3 cells kernel, as explained in the code below.Show code for diffusion and decay stepThe implementation is actually a bit different because we "loop" the image at the borders.(link
 to actual code)### Deposit on trail mapThere is a counter of particles on each pixel of the trail map. The counters are set to 0 at the
 beginning ot
 each iteration of the algorithm. After they move, the particles increment the counter at their position,
 which can be done in parallel thanks to the atomicAdd function in glsl.To update the trail map, we add \( \sqrt{k} \times f \) to the trail map image, where \( k \) is the
 particles count at the pixel and \( f \) some constant deposit factor. This part is a personal idea, I
 find that
 it works quite well. I also limit the count to a maximum value.Here is simplified code for that part.(link
 to actual code)Show GLSL code piece for particle deposit step### Difference compared to36 PointsThe trail map in36 Pointsworks differently compared to what I described. If I understand
 correctly, in36 Pointsparticles are like transparent dots that are added on the trail map
 image. It results that the
 trail map doesn't have values larger than the opaque value 1.In my implementation there is no such limit on trail map values, so when getting the value \( x \) we
 clamp
 it to avoid a value larger than 1: \( x = \min(x,1) \).### Move shaderWith the previous explanations we can give simplified code for the particle move and update.Show GLSL code piece for particle update/move (the most important code)(link
 to actual code)### Displayed imageTo get the image to display, the particles count on a pixel can be mapped to brightness in [0,1], non
 linearly. The deposit shader does it at the same time as doing the deposit on trail map.Some screenshots to end this section:## 4. Color experimentsA natural thing to do to obtain more colorful simulations is to map the counter of particles on a pixel
 to a color gradient, typically from black to white with various colors in between.I experimented with something more complex. The trail map image has two channels: one is the classic
 trail map, the other one is the trail map with a delay. When determining the color of a pixel, we check
 for the difference between trail map and delayed trail map at this pixel. The absolute value of the
 difference interpolates the previous color (with a gradient) towards white or another gradient. With
 that technique, areas where there is more change can have different colors. The interpolation amount can
 also be different with distance from the center.Link
 to an implementation## 5. Weird velocity effect experimentAt some point I wanted to experiment with adding velocity attributes to particles, so that they have some
 kind of inertia.I don't remember how, but with my experiments I arrived at a technique that can produce smooth and
 intricate results. It's described in the code below.Show GLSL code piece for weird effectIn the videos below, after 3 seconds the effect is activated.## 6. Playful interaction ideas, points mixingI've been making a playful version of these algorithms. The main idea is that there is a cursor that the
 user controls, through mouse or joystick, and different Points are spatially mixed.At the
 center of the cursor the simulation parameters use the first Point and far from cursor it's the second
 one. In the area in between, interpolation is done to get parameters. The interpolation parameter is
 defined with a gaussian function, and the size of the cursor is a standard deviation \( \sigma \). Let's
 call \( \mathbf{P} \) the particle position, and \( \mathbf{C} \) the cursor position. I also use the
 word pen instead of
 cursor.$$t = \exp\left( -\frac{\|\mathbf{P} - \mathbf{C}\|^2}{\sigma^2} \right)$$
 $$\text{param} = (1-t) \times \text{BackgroundPoint.param} + t \times \text{CursorPoint.param} $$We do this for all Point parameters of the simulation.The user can control pen size and navigate through Point choices.### Spawning actionThe user can spawn particles at some positions: the desired spawn position is given as uniform to the
 move
 shader, and each particle has a small probability of going to that location. So the spawning
 doesn't actually add new particles.### My big interactive physarum projectI open sourced the project where all of this and more features are implemented, it can be used as
 playful artistic installation with one or two players using gamepads. Link:Interactive physarum repository## 7. Other experimentsThe algorithm has enough elements to allow for a lot of room for experimentation.### Example 1Here is an example where the heading of the particle is used to interpolate parameters between two
 Points.$$t = 0.5 + 0.5 \times \sin(\text{heading} + f(x,y,\text{time}))$$
 $$\text{param} = (1-t) \times \text{Point1.param} + t \times \text{Point2.param} $$\( f(x,y,\text{time}) \) is a scalar field to play with. Mostly with that technique the simulation below
 with
 obtained.Another thing that was used is that particle random respawn has different probability depending on the
 sensed value at particle position.### Example 2For the simulations below, the main technique was using negative effect amount with the technique that
 was described earlier in the
 velocity effect section (see "effectAmount" variable):### Example 3In the velocity effect code given earlier, we can force adding some velocity.With that technique and higher respawn probability when further from center, the simulation below was
 obtained:## 8. Additional resourcesInteractive explanation for the
 classic
 physarum simulation, by Deniz BicerA go implementation with nice results, by
 Michael FoglemanPresentation video by Sebastian LagueReal-time
 web implementationwith parameters control, by Amanda GhassaeiReminder:Sage's explanation and comments
 about physarum simulation## 9. Last remarksIf you followed well this article you can understand that I would not have achieved these results without
 borrowing ideas and parameters from36 Points.
 The content of this page uses the same license as its key piece of code(License Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported
 License).Some of my experiments seem to force the behaviour and structure, rather than letting them emerge
 naturally from uniform rules. Sometimes I don't feel proud about that aspect! It loses the speculative
 biology quality.I hope this article can inspire people to build their own experiments.Thanks for reading!Contact: etin.jacob (at) gmail.comby Etienne Jacob, article underCC BY-NC-SA 3.0
