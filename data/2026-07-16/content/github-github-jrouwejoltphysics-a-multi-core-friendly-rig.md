---
title: 'GitHub - jrouwe/JoltPhysics: A multi core friendly rigid body physics and collision detection library. Written in C++. Suitable for games and VR applications. Used by Horizon Forbidden West and Death Stranding 2. · GitHub'
url: https://github.com/jrouwe/JoltPhysics
site_name: github
content_file: github-github-jrouwejoltphysics-a-multi-core-friendly-rig
fetched_at: '2026-07-16T11:34:50.867076'
original_url: https://github.com/jrouwe/JoltPhysics
author: jrouwe
description: A multi core friendly rigid body physics and collision detection library. Written in C++. Suitable for games and VR applications. Used by Horizon Forbidden West and Death Stranding 2. - jrouwe/JoltPhysics
---

jrouwe

 

/

JoltPhysics

Public

* NotificationsYou must be signed in to change notification settings
* Fork910
* Star11k

 
 
 
 
master
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

1,700 Commits
1,700 Commits
.github
.github
 
 
Assets
Assets
 
 
Build
Build
 
 
Docs
Docs
 
 
HelloWorld
HelloWorld
 
 
Jolt
Jolt
 
 
JoltViewer
JoltViewer
 
 
PerformanceTest
PerformanceTest
 
 
Samples
Samples
 
 
TestFramework
TestFramework
 
 
UnitTests
UnitTests
 
 
.clang-format
.clang-format
 
 
.editorconfig
.editorconfig
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
ContributorAgreement.md
ContributorAgreement.md
 
 
Doxyfile
Doxyfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
doxygen-awesome.css
doxygen-awesome.css
 
 
run_doxygen.bat
run_doxygen.bat
 
 
sonar-project.properties
sonar-project.properties
 
 
View all files

## Repository files navigation

# Jolt Physics

A multi core friendly rigid body physics and collision detection library. Suitable for games and VR applications. Used by Horizon Forbidden West and Death Stranding 2: On the Beach.

A YouTube video showing a ragdoll pile simulated with Jolt Physics.

For more demos andvideosgo to theSamplessection.

## Design considerations

Why create yet another physics engine? Firstly, it has been a personal learning project. Secondly, I wanted to address some issues that I had with existing physics engines:

* Games do more than simulating physics. These things happen across multiple threads. We emphasize on concurrently accessing physics data outside of the main simulation update:Sections of the simulation can be loaded / unloaded in the background. We prepare a batch of physics bodies on a background thread without locking or affecting the simulation. We insert the batch into the simulation with a minimal impact on performance.Collision queries can run parallel to adding / removing or updating a body. If a change to a body happened on the same thread, the change will be immediately visible. If the change happened on another thread, the query will see a consistent before or after state. An alternative would be to have a read and write version of the world. This prevents changes from being visible immediately, so we avoid this.Collision queries can run parallel to the main physics simulation. We do a coarse check (broad phase query) before the simulation step and do fine checks (narrow phase query) in the background. This way, long running processes (like navigation mesh generation) can be spread out across multiple frames.
* Sections of the simulation can be loaded / unloaded in the background. We prepare a batch of physics bodies on a background thread without locking or affecting the simulation. We insert the batch into the simulation with a minimal impact on performance.
* Collision queries can run parallel to adding / removing or updating a body. If a change to a body happened on the same thread, the change will be immediately visible. If the change happened on another thread, the query will see a consistent before or after state. An alternative would be to have a read and write version of the world. This prevents changes from being visible immediately, so we avoid this.
* Collision queries can run parallel to the main physics simulation. We do a coarse check (broad phase query) before the simulation step and do fine checks (narrow phase query) in the background. This way, long running processes (like navigation mesh generation) can be spread out across multiple frames.
* Accidental wake up of bodies cause performance problems when loading / unloading content. Therefore, bodies will not automatically wake up when created. Neighboring bodies will not be woken up when bodies are removed. This can be triggered manually if desired.
* The simulation runs deterministically. You can replicate a simulation to a remote client by merely replicating the inputs to the simulation. Read theDeterministic Simulationsection to understand the limits.
* We try to simulate behavior of rigid bodies in the real world but make approximations. Therefore, this library should mainly be used for games or VR simulations.

## Features

* Simulation of rigid bodies of various shapes using continuous collision detection:SphereBoxCapsuleTapered-capsuleCylinderTapered-cylinderConvex hullPlaneCompoundMesh (triangle)Terrain (height field)
* Sphere
* Box
* Capsule
* Tapered-capsule
* Cylinder
* Tapered-cylinder
* Convex hull
* Plane
* Compound
* Mesh (triangle)
* Terrain (height field)
* Simulation of constraints between bodies:FixedPointDistance (including springs)HingeSlider (also called prismatic)ConeRack and pinionGearPulleySmooth spline pathsSwing-twist (for humanoid shoulders)6 DOF
* Fixed
* Point
* Distance (including springs)
* Hinge
* Slider (also called prismatic)
* Cone
* Rack and pinion
* Gear
* Pulley
* Smooth spline paths
* Swing-twist (for humanoid shoulders)
* 6 DOF
* Motors to drive the constraints.
* Collision detection:Casting rays.Testing shapes vs shapes.Casting a shape vs another shape.Broadphase only tests to quickly determine which objects may intersect.
* Casting rays.
* Testing shapes vs shapes.
* Casting a shape vs another shape.
* Broadphase only tests to quickly determine which objects may intersect.
* Sensors (trigger volumes).
* Animated ragdolls:Hard keying (kinematic only rigid bodies).Soft keying (setting velocities on dynamic rigid bodies).Driving constraint motors to an animated pose.Mapping a high detail (animation) skeleton onto a low detail (ragdoll) skeleton and vice versa.
* Hard keying (kinematic only rigid bodies).
* Soft keying (setting velocities on dynamic rigid bodies).
* Driving constraint motors to an animated pose.
* Mapping a high detail (animation) skeleton onto a low detail (ragdoll) skeleton and vice versa.
* Game character simulation (capsule)Rigid body character. Moves during the physics simulation. Cheapest option and most accurate collision response between character and dynamic bodies.Virtual character. Does not have a rigid body in the simulation but simulates one using collision checks. Updated outside of the physics update for more control. Less accurate interaction with dynamic bodies.
* Rigid body character. Moves during the physics simulation. Cheapest option and most accurate collision response between character and dynamic bodies.
* Virtual character. Does not have a rigid body in the simulation but simulates one using collision checks. Updated outside of the physics update for more control. Less accurate interaction with dynamic bodies.
* VehiclesWheeled vehicles.Tracked vehicles.Motorcycles.
* Wheeled vehicles.
* Tracked vehicles.
* Motorcycles.
* Soft body simulation (e.g. a soft ball or piece of cloth).Edge constraints.Dihedral bend constraints.Cosserat rod constraints (an edge with an orientation that can be used to orient geometry, e.g. a plant leaf).Tetrahedron volume constraints.Long range attachment constraints (also called tethers).Limiting the simulation to stay within a certain range of a skinned vertex.Internal pressure.Collision with simulated rigid bodies.Collision tests against soft bodies.
* Edge constraints.
* Dihedral bend constraints.
* Cosserat rod constraints (an edge with an orientation that can be used to orient geometry, e.g. a plant leaf).
* Tetrahedron volume constraints.
* Long range attachment constraints (also called tethers).
* Limiting the simulation to stay within a certain range of a skinned vertex.
* Internal pressure.
* Collision with simulated rigid bodies.
* Collision tests against soft bodies.
* A strand based hair simulation running on GPUSystem is based on Cosserad rods.Can use long range attachment constraints to limit the stretch of hairs.Supports simulation (guide) and render (follow) hairs.Hair vs hair collision is handled by accumulating the average velocity in a grid and using those velocities to drive hairs.Supports collision with the environment, although it only supports ConvexHull and CompoundShapes at the moment.The roots of the hairs can be skinned to the scalp mesh.
* System is based on Cosserad rods.
* Can use long range attachment constraints to limit the stretch of hairs.
* Supports simulation (guide) and render (follow) hairs.
* Hair vs hair collision is handled by accumulating the average velocity in a grid and using those velocities to drive hairs.
* Supports collision with the environment, although it only supports ConvexHull and CompoundShapes at the moment.
* The roots of the hairs can be skinned to the scalp mesh.
* Water buoyancy calculations.
* An optional double precision mode that allows large worlds.

## Supported platforms

* Windows x86/x64/ARM64
* Linux (tested on Ubuntu) x86/x64/ARM32/ARM64/RISC-V64/LoongArch64/PowerPC64LE
* FreeBSD
* Android x86/x64/ARM32/ARM64
* Platform Blue (a popular game console) x64
* macOS x64/ARM64
* iOS x64/ARM64
* MSYS2 MinGW64
* WebAssembly, seethisseparate project.

## Required CPU features

* On x86/x64 the minimal requirements are SSE2. The library can be compiled using SSE4.1, SSE4.2, AVX, AVX2, or AVX512.
* On ARM64 the library uses NEON and FP16. On ARM32 it can be compiled without any special CPU instructions.

## Documentation

To get started, look at theHelloWorldexample. AHelloWorld example using CMake FetchContentis also available to show how you can integrate Jolt Physics in a CMake project.

Every feature in Jolt has its own sample.Running the Samples applicationand browsing through thecodeis a great way to learn about the library!

To learn more about Jolt go to the latestArchitecture and API documentation. Documentation fora specific release is also available.

Some algorithms used by Jolt are described in detail in my GDC 2022 talk: Architecting Jolt Physics for 'Horizon Forbidden West' (slides,slides with speaker notes,video).

## Compiling

* Compiles with Visual Studio 2022+, Clang 16+ or GCC 12+.
* Uses C++ 17.
* Depends only on the standard template library.
* Doesn't use RTTI.
* Doesn't use exceptions.

If you want to run on Platform Blue you'll need to provide your own build environment and PlatformBlue.h due to NDA requirements. This file is available on the Platform Blue developer forum.

For build instructions go to theBuildsection. When upgrading from an older version of the library go to theRelease NotesorAPI Changessections.

## Performance

If you're interested in how Jolt scales with multiple CPUs and compares to other physics engines, take a look atthis document.

## Folder structure

* Assets - This folder contains assets used by the TestFramework, Samples and JoltViewer.
* Build - Contains everything needed to build the library, see theBuildsection.
* Docs - Contains documentation for the library.
* HelloWorld - A simple application demonstrating how to use the Jolt Physics library.
* Jolt - All source code for the library is in this folder.
* JoltViewer - It is possible to record the output of the physics engine using the DebugRendererRecorder class (a .jor file), this folder contains the source code to an application that can visualize a recording. This is useful for e.g. visualizing the output of the PerformanceTest from different platforms. Currently available on Windows, macOS and Linux.
* PerformanceTest - Contains a simple application that runs aperformance testand collects timing information.
* Samples - This contains the sample application, see theSamplessection. Currently available on Windows, macOS and Linux.
* TestFramework - A rendering framework to visualize the results of the physics engine. Used by Samples and JoltViewer. Currently available on Windows, macOS and Linux.
* UnitTests - A set of unit tests to validate the behavior of the physics engine.

## Bindings for other languages

* Chere,hereandhere
* C#
* Java or Kotlinhereandhere
* JavaScript
* Rust
* Python
* Zig

## Integrations in other engines

* Godot
* Source Engine
* Unreal Pluginhereandhere

Seea list of projects that use Jolt Physics here.

## License

The project is distributed under theMIT license.

## Contributions

All contributions are welcome! If you intend to make larger changes, please discuss first in the GitHub Discussion section. For non-trivial changes, we require that you agree to aContributor Agreement. When you create a PR,CLA assistantwill prompt you to sign it.

Note that all PRs will be squashed before merging, so there's no need to force-push to git to keep the history clean.

## About

A multi core friendly rigid body physics and collision detection library. Written in C++. Suitable for games and VR applications. Used by Horizon Forbidden West and Death Stranding 2.

### Topics

 c-plus-plus

 game-engine

 cpp

 simulation

 physics

 vr

 game-development

 physics-engine

 physics-simulation

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

11k

 stars
 

### Watchers

199

 watching
 

### Forks

910

 forks
 

 Report repository

 

## Releases16

5.6.0

 Latest

 

Jul 11, 2026

 

+ 15 releases

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* C++94.0%
* C1.5%
* CMake1.5%
* CSS1.2%
* Objective-C++0.7%
* HLSL0.6%
* Other0.5%