---
title: 'Writing a Rust GPU kernel driver: a brief introduction on how GPU drivers work'
url: https://www.collabora.com/news-and-blog/blog/2025/08/06/writing-a-rust-gpu-kernel-driver-a-brief-introduction-on-how-gpu-drivers-work/
site_name: hackernews
fetched_at: '2025-08-07T10:21:09.863404'
original_url: https://www.collabora.com/news-and-blog/blog/2025/08/06/writing-a-rust-gpu-kernel-driver-a-brief-introduction-on-how-gpu-drivers-work/
author: losgehts
date: '2025-08-07'
---

* AboutWho we areOur expertiseOur workOpen SourceOur ecosystem
* Who we are
* Our expertise
* Our work
* Open Source
* Our ecosystem
* ServicesGuideTrainBuildIntegrateOptimizeMaintain
* Guide
* Train
* Build
* Integrate
* Optimize
* Maintain
* IndustriesAutomotiveDigital TVSiliconOEMVR/AR
* Automotive
* Digital TV
* Silicon
* OEM
* VR/AR
* News & Blog
* Careers
* Contact

* About
* Services
* Industries
* News & Blog
* Careers
* Contact

* +44 (0)1223 362967
* +1 514 667 2499
* contact@collabora.com

* Home
* News & Blog
* Blog

## Writing a Rust GPU kernel driver: a brief introduction on how GPU drivers work

Daniel AlmeidaAugust 06, 2025

Share this post:

Reading time:

This post is the second iteration of a series of posts that provide an in-depth look at the development of Tyr, a state-of-the-art Rust GPU driver for the Linux Kernel, supporting Arm Mali CSF-based GPUs.

As promised in the first iteration, we will now explore how GPU drivers work in more detail by exploring an application known asVkCube. As the program name implies, this application uses the Vulkan API to render a rotating cube on the screen. Its simplicity makes it a prime candidate to be used as a learning aid in our journey through GPU drivers.

This article will first introduce the concept of User Mode Drivers (UMDs) and Kernel Mode Drivers (KMDs), breaking down the steps needed to actually describeVkCube's workload to the GPU. This will be done in a more compact way for brevity as it's a rather extensive topic that has been detailed in several books.

We will wrap up with an overview of the actual API offered by Tyr. As previously stated, this is the same API offered by Panthor, which is the C driver for the same hardware.

### A quick introduction to GPU drivers

It is easier to introduce this topic by considering a simple 3D application like drawing a single triangle, or VkCube, a program that will render a rotating cube on the screen. Throughout this brief introduction, I will be using the terms UMD (usermode driver) to refer to the non-privileged part of the driver. For us this ispanvk, a Vulkan driver that is part of Mesa. The term KMD, on the other hand, refers to the privileged part of the driver. That is represented by Tyr, a kernel driver that aims to be part of the Linux kernel.

The starting point is to understand that a kernel-mode GPU driver connects a much larger UMD (user-mode driver) to the actual GPU. The UMD will actually implement APIs like Vulkan, OpenGL, OpenCL, and others. These APIs, in turn, will be used by actual programs to describe their workload to the GPU. This includes allocating and using not only the geometry and textures, but also the shaders being used to process said data into the final result. This means that a key aspect of GPU drivers is actually allocating GPU memory to house data related to the current scene being drawn so that it can actually be operated on by the hardware.

Shaders are full-blown programs running on the GPU. They are extremely powerful and can be used in a lot of ways, but for VkCube their main purpose is to place the cube in the scene, color its sides, and continuously rotate it. Notice that even a very trivial shader needs to have access to some external data to actually work. The shaders for VkCube need, at least, the geometry and color data, as well as the matrix data describing the rotation about an axis in 3D space.

With the data describing the model and the machine code describing the shaders, the UMD must ask the KMD to place this in GPU memory prior to execution. It must also tell the GPU that it wants to carry out a draw call and set any state needed to make this happen, which it does by means of building VkCommandBuffers, which are structures containing instructions to be carried out by the GPU in order to make the workload happen. It also needs to set up a way to be notified when the workload is done and then allocate the memory to place the results in.

This is quite intense at first, but neatly summarizes the interface that our GPU driver must offer. One of the main jobs of the kernel driver is allocating and mapping memory, preferably in a way that promotes isolation through some sort of context that is private to the application. Other key responsibilities include submitting work to a hardware queue where it can be considered for execution, as well as notifying the user when said work has been carried out.

The last part is key as we are dealing with massively parallel hardware where things may (and will) complete asynchronously and out of order. There must be a way to encode a job's dependencies and it is up to the kernel driver to make sure that these dependencies are actually followed if we are to extract anything meaningful from the result.

Therefore, deciding what to execute when (also known as scheduling) is a major part of a kernel mode driver.

Finally, it is up to the KMD to actually initialize the device and make sure that it is operational for all clients. This means powering on any clocks and voltage regulators and running any startup code to bring the device to life, at which point the KMD must make sure that the device is fairly shared among all clients by rotating the access to the hardware among the different applications using it.

### A key takeaway

One thing to be understood from the previous section is that the majority of the complexity tends to reside at theUMDlevel. This component is in charge of translating the higher-level API commands into lower-level commands that the GPU can understand. Nevertheless theKMDis responsible for providing key operations such that its user-mode driver is actually implementable, and it must do so in a way that fairly shares the underlying GPU hardware among multiple tasks in the system.

### Our driver interface

Given the previous introduction on how a modern GPU driver works, we are now in a position to formally define the interface that will be exposed by ourKMD:

	/** @DRM_PANTHOR_DEV_QUERY: Query device information. */
	DRM_PANTHOR_DEV_QUERY = 0,

	/** @DRM_PANTHOR_VM_CREATE: Create a VM. */
	DRM_PANTHOR_VM_CREATE,

	/** @DRM_PANTHOR_VM_DESTROY: Destroy a VM. */
	DRM_PANTHOR_VM_DESTROY,

	/** @DRM_PANTHOR_VM_BIND: Bind/unbind memory to a VM. */
	DRM_PANTHOR_VM_BIND,

	/** @DRM_PANTHOR_VM_GET_STATE: Get VM state. */
	DRM_PANTHOR_VM_GET_STATE,

	/** @DRM_PANTHOR_BO_CREATE: Create a buffer object. */
	DRM_PANTHOR_BO_CREATE,

	/**
	 * @DRM_PANTHOR_BO_MMAP_OFFSET: Get the file offset to pass to
	 * mmap to map a GEM object.
	 */
	DRM_PANTHOR_BO_MMAP_OFFSET,

	/** @DRM_PANTHOR_GROUP_CREATE: Create a scheduling group. */
	DRM_PANTHOR_GROUP_CREATE,

	/** @DRM_PANTHOR_GROUP_DESTROY: Destroy a scheduling group. */
	DRM_PANTHOR_GROUP_DESTROY,

	/**
	 * @DRM_PANTHOR_GROUP_SUBMIT: Submit jobs to queues belonging
	 * to a specific scheduling group.
	 */
	DRM_PANTHOR_GROUP_SUBMIT,

	/** @DRM_PANTHOR_GROUP_GET_STATE: Get the state of a scheduling group. */
	DRM_PANTHOR_GROUP_GET_STATE,

	/** @DRM_PANTHOR_TILER_HEAP_CREATE: Create a tiler heap. */
	DRM_PANTHOR_TILER_HEAP_CREATE,

	/** @DRM_PANTHOR_TILER_HEAP_DESTROY: Destroy a tiler heap. */
	DRM_PANTHOR_TILER_HEAP_DESTROY,

Note this is a rather compact API, and very far removed from our initial task of drawing a rotating cube. This fits nicely into our model where theUMDis in charge of handling all the drawing commands, and uses theKMDas a means to access the underlying GPU hardware.

We can break the API above into a few distinct groups:

1. Device information: This is represented here by theDEV_QUERYioctl. Needless to say, theUMDneeds to know some information from the underlying GPU hardware in order to work. This is usually implemented by simply reading someROM(read-only memory) area in the GPU.

2. Memory allocation and isolation: This is represented byVM_CREATE,VM_BIND,VM_DESTROY,VM_GET_STATE,BO_CREATE, andBO_MMAP_OFFSET. We will see how this is implemented at the kernel level later.

3. Group creation and management:GROUP_CREATE,GROUP_DESTROY, andGROUP_GET_STATE. We will go into great detail on what groups are in a later installment in this series.

4. Job submission: This is implemented solely byGROUP_SUBMIT. Note that this call is extremely important, as it's how we submit our device-specific command buffers that describe what operations are to be carried out by the GPU hardware.

5. Tiler heap management: This is represented byTILER_HEAP_CREATEandTILER_HEAP_DESTROY. Explaining howtiling GPUswork is so far beyond the scope of this series, but for the time being, it is enough to assume that they need a variable amount of internal memory in order to draw the geometry. This pool of memory is managed by theUMDthrough the interface presented here.

### What's next

This article introduced some key concepts about how GPU drivers work. We will use these concepts in subsequent parts of this series as we delve further into Arm's CSF hardware.

The next section will explore the CSF architecture, introducing components like the Micro Controller Unit (i.e.:MCU) that underpins the design, as well as the steps needed to get it to boot.

### Related Posts

##### Introducing Tyr, a new Rust DRM driver

##### Matt Godbolt sold me on Rust (by showing me C++)

##### PanVK now supports Vulkan 1.4

### Related Posts

##### Introducing Tyr, a new Rust DRM driver

##### Matt Godbolt sold me on Rust (by showing me C++)

##### PanVK now supports Vulkan 1.4

## Search the newsroom

Search

## Latest Blog Posts

### Writing a Rust GPU kernel driver: a brief introduction on how GPU drivers work

06/08/2025

This second post in the Tyr series dives deeper into GPU driver internals by using the Vulkan-based VkCube application to explain how User…

### A practical debugging guide for media driver developers

22/07/2025

Getting into kernel development can be daunting. There are layers upon layers of knowledge to master, but no clear roadmap, especially when…

### Quick notes from the GStreamer Spring Hackfest 2025

15/07/2025

This past May, we met with the community at the GStreamer Spring Hackfest in Nice, France, and were able to make great strides, including…

### PipeWire workshop 2025: Updates on video transport, Rust efforts, TSN networking, and Bluetooth support

03/07/2025

As part of the activities Embedded Recipes in Nice, France, Collabora hosted a PipeWire workshop/hackfest, an opportunity for attendees…

### Coccinelle for Rust progress report

25/06/2025

In collaboration with Inria, the French Institute for Research in Computer Science and Automation, Tathagata Roy shares the progress made…

### Linux Media Summit 2025 recap

23/06/2025

Last month in Nice, active media developers came together for the annual Linux Media Summit to exchange insights and tackle ongoing challenges…

#### About Collabora

Whether writing a line of code or shaping a longer-term strategic software development plan, we'll help you navigate the ever-evolving world of Open Source.

한국어 버전의 Collabora.com 보기

Acesse Collabora.com em Português

#### Learn more

* Who we are
* Services
* Our expertise
* Industries
* Our work
* Careers
* Open Source

Collabora on LinkedIn

Collabora on YouTube

Collabora on Mastodon

Collabora on Bluesky

Collabora on Facebook

Collabora RSS Feed

+44 1223 362967

+1 514 667 2499

contact@collabora.com

Our website only uses a strictly necessary session cookie provided by our CMS system. To find out more pleasefollow this link.

Collabora Limited © 2005-2025. All rights reserved.Privacy Notice.Sitemap.

To ensure the Collabora website works as designed, please enable JavaScript. Thanks
