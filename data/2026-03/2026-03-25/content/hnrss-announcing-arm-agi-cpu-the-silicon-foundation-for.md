---
title: 'Announcing Arm AGI CPU: The silicon foundation for the agentic AI cloud era - Arm Newsroom'
url: https://newsroom.arm.com/blog/introducing-arm-agi-cpu
site_name: hnrss
content_file: hnrss-announcing-arm-agi-cpu-the-silicon-foundation-for
fetched_at: '2026-03-25T11:19:57.545865'
original_url: https://newsroom.arm.com/blog/introducing-arm-agi-cpu
author: Mohamed Awad
date: '2026-03-24'
published_date: '2026-03-24T16:55:00+00:00'
description: Arm introduces the Arm AGI CPU to power agentic AI infrastructure with rack-scale performance, efficiency and scalable compute for next-generation data centers.
tags:
- hackernews
- hnrss
---

Arm Newsroom

 Blog



Today,Arm is announcing the Arm AGI CPU, a new class of production-ready silicon built on theArm Neoverseplatform and designed to power the next generation of AI infrastructure.

For the first time in ourmore than 35-year history, Arm is delivering its own silicon products – extending the Arm Neoverse platform beyond IP and Arm Compute Subsystems (CSS) to give customers greater choice in how they deploy Arm compute – from building custom silicon to integrating platform-level solutions or deploying Arm-designed processors. It reflects both the rapid evolution of AI infrastructure and growing demand from the ecosystem for production-ready Arm platforms that can be deployed at pace and scale.

## The rise of the agentic AI infrastructure

AI systems are increasingly operating continuously at global scale. Historically, the human was the bottleneck in computing – the pace at which people could interact with systems defined how quickly work could move through them. In the era of agentic AI, that constraint disappears as software agents coordinate tasks, interact with multiple models and make decisions in real time.

As AI systems run continuously and workloads grow in complexity, theCPU becomes the pacing element of modern infrastructure– responsible for keeping distributed AI systems operating efficiently at scale. In a modern-day AI data center, the CPU manages thousands of distributed tasks – orchestrating accelerators, managing memory and storage, scheduling workloads and moving data across systems – and now, with agentic AI, coordinating fan-out across large numbers of agents.

This shift places new demands on the CPU and that requires an evolution of the processor.

Arm Neoverse already underpins many of today’s leading hyperscale and AI platforms, includingAWS Graviton,Google Axion,Microsoft Azure CobaltandNVIDIA Vera. As AI infrastructure scales globally, partners across the ecosystem are asking Arm to do more. The Arm AGI CPU was created to address this shift.

## Arm AGI CPU: Built for rack-scale agentic efficiency

Agentic AI workloads demand sustained performance at massive scale. TheArm AGI CPUis designed to deliver high per-task performance at sustained load across thousands of cores in parallel – all within the power and cooling limits of modern data centers.

Every element of the Arm AGI CPU – from operating frequency to memory and I/O architecture – has been designed to support massively parallel, high-performance agentic workloads in a densely populated rack deployment.

Arm’s reference server configuration is a 1OU, 2-node design – packing in two chips with dedicated memory and I/O for a total of 272 cores per blade. These blades are designed to fully populate a standard air-cooled 36kW rack – 30 blades delivering a total of 8160 cores. Arm has additionally partnered with Supermicro on a liquid-cooled 200kW design capable of housing 336 Arm AGI CPUs for over 45,000 cores.

In this configuration, the Arm AGI CPU is capable of delivering more than 2x the performance per rack compared to the latest x86 systems*, achieved through the fundamental advantages of the Arm architecture and careful matching of system resources to compute:

* Arm AGI CPU’s class-leading memory bandwidth means more effective threads of execution per rack; x86 CPUs degrade as cores contend under sustained load.
* High performance, efficient, single-threadedArm Neoverse V3 CPUcores outperform legacy architectures; every Arm thread does more work.
* More usable threads and more work-per-thread compounds to massive performance gains per rack.

## Early momentum across the AI ecosystem

The Arm AGI CPU is already seeing strong commercial momentum with partners at the forefront of scaling agentic AI infrastructure. Planned deployments span accelerator management, agentic orchestration and the densification of services, applications and tools needed for agentic task scale-out — as well as increased networking and data plane compute to support the AI data center.

Meta is our lead partner and customer, co-developing the Arm AGI CPU to optimize gigawatt-scale infrastructure for its Meta family of apps and to work alongside Meta’s own custom MTIA accelerators. Other launch partners include Cerebras, Cloudflare, F5, OpenAI, Positron, Rebellions, SAP, and SK Telecom – each working with Arm on the deployment of the Arm AGI CPU to accelerate AI-driven services across cloud, networking and enterprise environments. Commercial systems are now available for order from ASRockRack, Lenovo and Supermicro.

To accelerate adoption further, Arm is introducing theArm AGI CPU 1OU Dual Node Reference Server, an Open Compute Project (OCP) DC-MHS standard form factor server. Arm plans to contribute this reference server design and supporting firmware, along with further contributions including system architecture specifications, debug frameworks and diagnostic and verification tooling applicable to all Arm-based systems. Further details will come at the upcomingOCP EMEA Summit.

## A new chapter for Arm infrastructure

The launch of Arm AGI CPU represents a new chapter in Arm’s data center journey and continued leadership in computing innovation. As AI reshapes the industry, Arm remains committed to enabling progress across the ecosystem – meeting customers where they are, from hyperscale cloud providers to AI startups.

The Arm AGI CPU is the first offering of Arm’s new data center silicon product line and is available to order now. Follow-on products are committed, targeting best-in-class performance, scale and efficiency. This continues in parallel with theArm Neoverse CSSproduct roadmap so that all Arm data center customers move forward together on platform architecture and software compatibility.

Entering this new chapter, our mission remains unchanged: to provide the compute foundation that enables innovation across industries. And the ecosystem is fully behind us:More than 50 leading companiesacross hyperscale, cloud, silicon, memory, networking, software, system design and manufacturing are supporting the expansion of the Arm compute platform into silicon. With Arm AGI CPU, we are not only defining the architecture of the AI-native data center, we are building it.

Hear more from our Arm AGI CPU deployment partners:

### Cerebras

“At Cerebras we build AI infrastructure designed for ultra-fast, large-scale inference, and as this becomes the dominant workload in AI, composable, high-performance systems matter more than ever – these systems need purpose-built AI acceleration alongside efficient, scalable CPUs orchestrating data movement, networking, and coordination at scale. Extending the Arm compute platform into AGI-class infrastructure is a positive step for the ecosystem and for customers deploying AI at global scale.” –Andrew Feldman, CEO, Cerebras

### Cloudflare

“To continue our mission of helping build a better Internet, Cloudflare needs infrastructure that scales efficiently across our global network. The Arm AGI CPU provides high-performance, energy-efficient compute designed for the next generation of workloads.” –Stephanie Cohen, Chief Strategy Officer, Cloudflare

### Meta

“Delivering AI experiences at global scale demands a robust and adaptable portfolio of custom silicon solutions, purpose-built to accelerate AI workloads and optimize performance across Meta’s platforms. We worked alongside Arm to develop the Arm AGI CPU to deploy an efficient compute platform that significantly improves our data center performance density and supports a multi-generation roadmap for our evolving AI systems.” –Santosh Janardhan, Head of Infrastructure, Meta

### OpenAI

“OpenAI runs AI systems at massive scale. Hundreds of millions use ChatGPT every day, businesses build on our API, and developers rely on tools like Codex. The Arm AGI CPU will play an important role in our infrastructure as we scale, strengthening the orchestration layer that coordinates large scale AI workloads and improving efficiency, performance, and bandwidth across the system.” –Sachin Katti, Head of Industrial Compute at OpenAI

### Positron

“At Positron, we are focused on purpose-built inference accelerators that delivers breakthrough token generation efficiency using commodity memory. Arm has consistently delivered the industry’s most power-efficient compute platforms, which makes the Arm AGI CPU a natural foundation for next-generation AI infrastructure. By combining Positron’s inference acceleration technology with the energy-efficient Arm AGI CPU platform, we see a powerful opportunity to help data center operators deploy frontier AI models at scale with greater performance per watt and per dollar.” –Mitesh Agrawal, CEO, Positron AI

### Rebellions

“High-performance AI systems require tight coordination between general-purpose compute and accelerator architectures. By combining the Arm AGI CPU with Rebellions’ NPUs in new high-density server configurations — we’re delivering a scalable, energy efficient platform that is optimized for AI inference workloads at scale.” –Marshall Choy, Chief Business Officer, Rebellions

### SAP

“SAP’s successful deployment of SAP HANA on Arm-based AWS Graviton underscores the maturity and performance of the Arm ecosystem for enterprise workloads. The Arm AGI CPU extends that opportunity, providing scalable, efficient compute designed to support the next generation of AI-powered business solutions.” –Stefan Bäuerle, Senior Vice President, Head of HANA & Persistency, SAP

### SK Telecom

“SK Telecom is expanding into large-scale, full-stack AI inference data center infrastructure, which includes Arm AGI CPU and Rebellions AI accelerator chip. By bringing together our sovereign A.X foundation model with inference-optimized AI servers, we are ready to deliver it to world while elevating our AIDC competitiveness.” –Suk-geun (SG) Chung, CTO and Head of AI CIC, SK Telecom

## Forward-looking statements

This blog post contains forward-looking statements regarding Arm’s product roadmap, future performance, planned contributions and partner deployments. These statements are based on current expectations and are subject to risks and uncertainties that could cause actual results to differ materially. For a discussion of factors that could affect Arm’s results, please refer to Arm’s filings with the U.S. Securities and Exchange Commission.

Performance claims are based on Arm internal estimates comparing a fully populated rack of Arm AGI CPU-based servers against comparable x86-based server configurations using industry-standard workloads. Actual results may vary based on system configuration, workload, and other factors.

All product and company names are trademarks or registered trademarks of their respective holders.

*Based on estimates

By
Mohamed Awad
,
Executive Vice President, Cloud AI Business Unit,
Arm

Share



 Article Text

 Copy Text

Any re-use permitted for informational and non-commercial or personal use only.

## Editorial Contact

Arm Global PR Team

 Global-PRteam@arm.com

 Stay informed with Arm's top stories, insights, and conversations.

## Media Information



### Company Overview & History

Arm is defining the future of computing

Learn More

→



### Arm Corporate Guidelines

Information on how to use the Arm corporate logo

Learn More

→



### Media Contacts

Get the latest Media contact information

Learn More

→



## Latest on X

;


Arm

@Arm

·

19h
 2036225253639082122



Agentic AI rises ⬆️AI infrastructure shifts 🔀Agentic AI calls for infrastructure designed for real-world inference and scale, elevating the CPU’s role at the center of AI systems to drive efficiency and unlock performance - and Arm is built for it.

In the Age of Agentic AI, CPUs Matter More Than Ever

In the Age of Agentic AI, CPUs Matter More Arm and Bloomberg Media Studios

okt.to


Reply on Twitter 2036225253639082122


Retweet on Twitter 2036225253639082122

8


Like on Twitter 2036225253639082122

38

Twitter

2036225253639082122

;


Arm

@Arm

·

21 Mar
 2035503001897410834



A defining moment for AI compute begins at #ArmEverywhere.Arm CEO Rene Haas shares his vision for the next era of intelligence—and the ecosystem driving innovation at scale.Be part of it. Join us on March 24: https://okt.to/1uwUz2



Twitter feed image.



Reply on Twitter 2035503001897410834


Retweet on Twitter 2035503001897410834

14


Like on Twitter 2035503001897410834

54

Twitter

2035503001897410834

;


Arm

@Arm

·

20 Mar
 2035114277342744939



Missed a call? Your AI agent can handle it. 📱With Arm Scalable Matrix Extension 2 (SME2), agentic AI call handling runs entirely on device, sending follow-ups, suggesting callback times and managing scheduling with low latency and enhanced privacy.This is what accelerated,



Twitter feed video.



Reply on Twitter 2035114277342744939


Retweet on Twitter 2035114277342744939

12


Like on Twitter 2035114277342744939

32

Twitter

2035114277342744939

;


Arm

@Arm

·

20 Mar
 2035071187852673440



When robots visit the office 🤖AGIBOT joined us in Cambridge with its humanoids and a quadruped showcasing a variety of tasks from painting and dancing to human interactions and dynamic movement.Behind every action is the Arm compute platform, spanning sensor-level processing



Twitter feed video.



Reply on Twitter 2035071187852673440


Retweet on Twitter 2035071187852673440

15


Like on Twitter 2035071187852673440

52

Twitter

2035071187852673440

;


Arm

@Arm

·

20 Mar
 2034979077325550061



AI is moving into the physical world. 🤖🚗Vehicles, robots and industrial systems are becoming intelligent machines that can sense, reason and act in real time, driving the rise of physical AI.Learn how it’s shaping the next platform shift. https://okt.to/s7UWhi



Twitter feed video.



Reply on Twitter 2034979077325550061


Retweet on Twitter 2034979077325550061

11


Like on Twitter 2034979077325550061

26

Twitter

2034979077325550061

;


Arm

@Arm

·

19 Mar
 2034774452781658566



5 days to go.A defining moment for AI compute is coming.Join our CEO Rene Haas live on March 24 for #ArmEverywhere: https://okt.to/2vhEiM10am PDT | live on X



Twitter feed image.



Reply on Twitter 2034774452781658566


Retweet on Twitter 2034774452781658566

9


Like on Twitter 2034774452781658566

47

Twitter

2034774452781658566

;


Arm

@Arm

·

19 Mar
 2034704801062171015



🌍 Innovation built for the real world.In partnership with @Simprints and @gavi, we’re supporting biometric digital ID solutions that let health workers identify infants on a smartphone and give them the care they need.Hear from Dr. Toby Norman as he shares how this



Twitter feed video.



Reply on Twitter 2034704801062171015


Retweet on Twitter 2034704801062171015

7


Like on Twitter 2034704801062171015

29

Twitter

2034704801062171015
