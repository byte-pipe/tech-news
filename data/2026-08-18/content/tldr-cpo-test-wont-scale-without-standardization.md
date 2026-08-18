---
title: CPO Test Won't Scale Without Standardization
url: https://semiengineering.com/cpo-test-wont-scale-without-standardization/
site_name: tldr
content_file: tldr-cpo-test-wont-scale-without-standardization
fetched_at: '2026-08-18T11:23:11.333238'
original_url: https://semiengineering.com/cpo-test-wont-scale-without-standardization/
author: Anne Meixner
date: '2026-08-18'
published_date: '2026-08-11T07:01:56+00:00'
description: CPO Test Won't Scale Without Standardization (4 minute read)
tags:
- tldr
---

Submit

Home
 >
 
Test, Measurement & Analytics
 >
 CPO Test Won’t Scale Without Standardization 

Test, Measurement & Analytics

# CPO Test Won’t Scale Without Standardization

Across the CPO ecosystem, profitability will not happen until standardization occurs.

								August 11th, 2026 - 

								By: 
Anne Meixner

Key Takeaways:

* A smaller set of fiber connectors that meet manufacturing test high insertion count will ease the cost burden for all.
* Test specifications and associated standardized test formats will facilitate data analytics and lower test cell costs.
* Traceability across the multiple suppliers will bridge the data silos, which greatly improve yield learning.

Co-packaged optics (CPO) is taking off as AI data centers leverage every possible option for improving performance and reducing power, but moving from lab instrumentation to production ATEs on a factory floor is struggling to keep pace with demand.

CPO checks all the boxes for next-gen computing — higher bandwidth, lower power, and reduced latency. But there are so many options for heterogeneous integration, thermal management, serviceability, and manufacturing test — that it’s slowing the rollout of this technology.

Nearly every aspect of the physical test cell poses a challenge, from the test specifications to data management. This is made worse by the fact that there are no standards for connectors, product specifications, or test data formats, so every CPO design requires a custom solution. The result is longer time to market, higher cost, and limited reuse of equipment and software.

“Traditionally, optics have been done with pluggables, but they typically tend to have very poor bandwidth density and power consumption relative to the kinds of bandwidths you need,” said Vishal Chandrasekar, director of product management atAyar Labs. “Plus, you need to get the optics closer and closer to the GPU, and you need to do it at low power. For scale-up applications, that’s really becoming very bandwidth-sensitive. Scale-up has about 10X the bandwidth requirement of scale-out, and so traditional pluggables don’t work. So then people are saying we need to put those two together.”

The industry is taking a stepwise approach to optics integration with electronics. “The first step would be an NPO (near package optics), which brings the optical into the board, which is not in volume production yet. I expect that to get into volume production in 12 to 18 months’ time. Phase two would be the CPO, which would be on the substrate, and that I expect to get to volume in 18 to 24 months time, at least for the scale-up applications or scale-out,” said Chandrasekar. “Nvidia and Broadcom have introduced those solutions, and they are heavily ramping this into volume right now. [For CPO], we have to let the proof-of-concept phase run, and we are in the process of reducing the assembly time. In addition, the test equipment is being developed alongside the product with our partners.”

But as with everything related to AI data centers, each new technology has spawned an industry-wide scramble. There are multiple CPO designs and approaches available. The problem is choosing which ones to use. Today, these are predominantly custom test cell solutions, which include everything from ATE instrumentation to robotic handling and software code. This is where standards are sorely needed to reduce the number of test-cell architectures, which in turn would reduce the cost of goods and alleviate the engineering team’s burden.

“Standards can help the industry by reducing unnecessary variation in how co-packaged optics are accessed, stimulated, measured, and reported during test,” said Abram Detofsky, manufacturing test architect atIntel Foundry. “Today, many optical test solutions are highly customized because package formats, optical interfaces, calibration methods, handling schemes, and data definitions can vary significantly. Standardization can create common expectations around test access, reference conditions, terminology, calibration practices, and result reporting. This helps equipment suppliers, OSATs, foundries, and customers build interoperable solutions instead of one-off engineering setups.”

Others agree. “Standards are expected to play a vital role in helping all the customers, suppliers, and OSATs converge,” explained Vineet Pancholi, manufacturing test technologist atAmkor. “Suppliers will converge toward production test simplification by designing test equipment that services a specific functionality and performance envelope. Customers will begin defining and architecting products that meet a certain specific standard — data rate(s), failure rate specifications, test limits, guard-bands, etc. OSATs will be able to help define the production test cell definitions with pre-defined success criteria and the overall production test workflow.”

Fig. 1: Components of co-packaged optics, split between electronic chiplets, photonic chiplets, and an external laser. Source: Amkor

However, the chip industry has yet to settle on a data model for optical test content. “The hardware challenges get most of the attention, but the least-appreciated one is a data problem,” said Dieter Rathei, CEO of DR Yield. “STDF was built for electrical parametric and functional results. It was never designed to carry a wavelength sweep or a polarization-dependent loss curve as a first-class object. So optical measurements end up flattened into scalar limits or parked in vendor-specific files, and the richness needed for real yield learning is lost before analysis even starts.”

StandardsStandards begin with device design, which is used to create a common understanding from that point all the way to test measurements. In a March press release [1], Lightmatter announced a partnership with other Open Compute Project members to develop an open reference design at the rack level. The reference design and the associated specifications and standardization will enable the ecosystem to scale up to 10 million units/year, and test specifications will be included.

Multiple industry experts highlighted the large variance in test specifications, test data formats, and fiber connectors. Those need to be addressed because standardizing manufacturing tests, along with key components, will drive down the cost in a number of ways. For example, limiting the number of fiber connector types in a test cell would greatly benefit test equipment suppliers.

“Today, CPO packages vary widely from test program to test program,” said Matt Griffin, senior product manager for the silicon photonics test group atTeradyne. “Current designs integrate anywhere from 4 to 36 optical engines across two to four sides of a compute die, and the industry still lacks a common approach to fiber connectors, alignment schemes, and laser delivery. This lack of connector standardization complicates automation, requiring test systems to support a variety of connector types, and practically means every new customer design can require a custom implementation.”

When to implement standards has always included an element of guesswork. Because CPO is closely tied to AI data center build-up and build-out, it is being rolled out rapidly. Consequently, it may be up to the marketplace to reduce the number of optical connector choices because the technology is moving so quickly.

“The challenge is that the CPO market is evolving faster than traditional standards bodies can typically respond,” said Ira Leventhal, vice president of research and venture atAdvantest America. “As a result, industry leaders are increasingly driving de facto standards through their own market adoption, industry consortia, and multi-source agreements (MSAs). In some areas, such as optical connectivity, the market is already beginning to converge based on the evaluation and deployment decisions of leading customers and system providers as opposed to formal industry standards.”

Nevertheless, a handful of assertions is needed over the connector’s lifecycle. For manufacturing, there may be tens of thousands of insertions. If the connector design cannot survive that gauntlet, it can’t be used in a production environment.

Many of the priorities here are shared with mainstream semiconductor assembly. “You have to maintain the thermals, you have to maintain the manufacturability, yields, and have field replaceability,” said Ayar Labs’ Chandrasekar. “These are all the different tradeoffs that people make. For instance, one example of CPO is to have external lasers because the laser is the high-risk part from a reliability perspective.”

However, there is a rather surprising lack of standardization across the wide range of test methods and their associated specifications, which are often customized for each design. Reducing the variety of manufacturing test methods enables cost-effective and efficient test solutions. This can be approached by understanding the primary defect mechanisms.

“A comprehensive list of fabrication defect types in Si-optical structures is being identified from a half-dozen fab houses. This data is expected to drive the test priority and test limits,” said Amkor’s Pancholi. “For instance, customers have optical engines and optical switches that operate in the O-band and the C-band. Their performance attributes can vary widely. The OSATs will be successful when the deployed test equipment can cater to a larger range of products being fabricated. This will allow for maximum CapEx re-use.”

Most of the standardization efforts so far have focused on physical and electrical interfaces. “But there’s a parallel gap that gets far less attention — test-data standardization,” said DR Yield’s Rathei. “Interoperable modules aren’t enough if every supplier reports optical parameters in a different schema, because cross-vendor yield learning then becomes a manual reconciliation exercise. The industry would benefit enormously from a common way to represent optical test content and unit genealogy so that data from a foundry, an OSAT, and a system integrator can be correlated without custom glue each time. That’s the layer we work at, and it’s where standardization would most directly reduce cost of test.”

Others also point to the need for test data format standardization. “STDF was never really designed with optical measurements in mind — wavelength sweeps, far-field profiles, OSA traces, LIV curves — so every vendor invents something,” said Aftkhar Aslam, CEO of yieldWerx. “If we got an STDF extension (or a parallel format with the same discipline) that handled the optical side cleanly, downstream analytics would move much faster.”

Lack of standardization affects analyticsIn discussing the need for standardization for cost-effective and efficient test solutions, many industry experts pointed to data formats, device identifiers, and breaking down the silos between the different test insertions to support a robust data analytic platform. For purely electrical devices, such platforms have become an essential tool for yield learning, process optimization, and quality management. For CPO to reach desired production volumes, engineering teams will need this type of platform.

Fig. 2: Test insertions for silicon photonics from wafer to system-level test. Source: Teradyne

But currently the lack of standards/standardization impedes most aspects of setting up and maintaining a robust data analytics solution. Meg O’Brien, director of product engineering at Lightmatter, highlighted three areas that need attention:

* Universal Optical Test Formats: Optical testing currently lacks the standardized output common in electrical testing across ATE providers. Implementing consistent formats would remove the heavy engineering burden of developing bespoke data integrations, creating a plug-and-play testing environment.
* Uniform Identifier Protocols: Creating industry standards for die identification among PIC and EIC vendors, and defining how OSATs manage these IDs, is essential for seamless end-to-end traceability and streamlined quality assurance.
* Standardized Test Metadata: Aligning fields for environmental conditions, recipe versions, and hardware status would enable analytics platforms to operate across various suppliers without the need for manual data mapping, dramatically speeding up time-to-market.

TraceabilityAnalytics starts with device traceability. Engineers need two components for traceability. The first component is a readable physical ID, or a virtual ID (a.k.a. digital binding), for any component used in the CPO’s final assembly. This encompasses EICs, PICs, lasers, fiber connectors, splitters, combiners, substrates, and heatsinks.

The second component is a data platform that stitches together the data available via these IDs, which necessitates sharing the IDs across the platform. But IDs are easily dropped during the transfer from one factory to the next. “This isn’t a technology problem,” said Aslam. “It’s a contract problem. Anyone serious about CPO yield learning needs to write ID-propagation requirements directly into their OSAT statements of work and check them at incoming. From our side, we’ll take whatever the factory gives us and make every linked ID a join key. But we can’t manufacture data that nobody captured.”

That data needs to be analyzed, as well. “As CPO manufacturing matures and moves toward high-volume production, data analytics will play an increasingly important role in correlating results across the entire test flow, said Advantest’s Leventhal. “The ability to trace failures, identify process excursions, optimize test coverage, and predict yield impacts across multiple insertions will be essential for improving product quality while controlling manufacturing and test costs.”

Implementing such a solution requires due diligence across all factories, and it often falls to the manufacturer to implement the tracking of physical IDs to feed into their data management and analytics system. Many point to challenges that make it so, including narrowing down data analytics methodologies across CPO customers, mature physical IDs for optical components, and auditing the links between factories.

“Supporting traceability in a CPO environment is primarily a challenge of data modeling, said Lightmatter’s O’Brien. “The lifecycle of a single module involves tracking EIC and PIC dies, laser components, the final assembly, every test insertion, and potential rework cycles. Our centralized data platform facilitates this by stitching together identifiers across the entire value chain. By maintaining auditable links from raw data through to the integrated layers, we ensure that every component remains traceable back to its origin without compromising the intellectual property of individual suppliers.”

Others agree that with traceability comes the acknowledgment that suppliers’ IP needs to be protected while supporting the common good of CPO yield learning. “The goal is not to expose proprietary process details, but to preserve enough structured context (identity, lot history, test conditions, calibration state, and performance results) to support yield learning and quality management across both the advanced assembly flow and the supply chain,” said Intel Foundry’s Detofsky.

Yield learning and moreWith an effective data management solution in place, engineering teams can decipher the relationships and measurements that can identify the source of a yield issue and propose a solution. That, in turn, enables them to apply adaptive test algorithms that improve product quality and use data-feedforward methods to assist with test optimization.

It starts with a robust data platform that checks all the boxes related to big data management — volume, velocity, variety, and veracity.

“Improving yield for co-packaged photonics necessitates expertise spanning EIC and PIC fabrication, assembly, and both optical and system-level testing—a breadth of knowledge rarely found in a single engineering discipline,” O’Brien said. “To bridge these silos, we utilize a centralized hardware data platform to manage complex operational and analytical requirements. Key attributes of this infrastructure include a seamless data pipeline, unified truth, comprehensive genealogy, scalable architecture, and access and IP control.”

With such a system in place, product engineering teams can merge data between electrical and photonic test measurements and ask salient yield learning questions.

“CPO test is where data analytics stops being optional,” Rathei said. “The core problem is that electrical and optical results live in different worlds — parametric bins and functional pass/fail on one side, spectral sweeps, insertion loss, return loss, wavelength and polarization data on the other. Yield learning only happens when you can correlate across both on the same unit. We built our platform around cross-flow correlation for exactly this reason — pulling assembly, unit-level and system-level data into one model so an engineer can ask, ‘Does this optical margin loss track a specific bond process, a specific EIC lot, or a specific test site without exporting three datasets and reconciling them by hand?’ The teams moving fastest on CPO are the ones treating multi-domain correlation as a first-class capability rather than a post-mortem activity.”

Others observe that their customers see similar value in merging data across test insertions.

“We’ve worked with photonic manufacturers running flows that look a lot like what CPO is becoming — bar test, tile test, far-field, SPC, inline inspection — and the analytics value lands in three pretty consistent places. The biggest one is just getting the streams onto one canvas,” said yieldWerx’s Aslam. “If you can correlate bar-test electricals with far-field optical metrics in a single analysis, you start spotting things like, ‘Units with marginal threshold current are the ones losing far-field power two insertions later.’ Second is the basic unit-level commonality and outlier work, such as PAT and MV-PAT, which catches systematic problems an engineer scanning a spreadsheet won’t see in time. Third is having executives, process owners, and the test team all looking at the same Power BI report so the discussions actually start from the same numbers. The hard part is almost never the math. It’s getting the data merged in the first place.”

ConclusionWhile test challenges in CPO are understood well enough, the need to standardize is only now gaining attention. To scale to 10 million units per year, standardization is essential. Without it, the entire ecosystem is left struggling with the heavy engineering burden of supporting manufacturing test.

All industry experts point to the need for test-related standards, both formal (e.g. extending STDF for optical measurements) and informal (e.g. data management agreements). However, several of them also noted that equipment vendors and OSATs often follow their lead customers.

“CPO test will not scale if every product, supplier, package, optical interface, and test cell is treated as a custom engineering project. The industry must move toward a shared manufacturing framework — common optical test-access concepts, repeatable package-level mechanical interfaces, standardized traceability practices, consistent data structures, and DFT features that make optical engines observable and controllable across the test flow and across multiple suppliers,” noted Intel Foundry’s Detofsky. “This does not mean every company has to expose proprietary design or process details. The goal is to standardize the optical, mechanical, test methods, calibration, and data boundaries that allow foundries, OSATs, equipment suppliers, component suppliers, and system companies to be interoperable and make consistent quality decisions. Interoperability at boundaries is key.”

References:

1. https://lightmatter.co/press-release/lightmatter-announces-reference-architecture-initiative-with-industry-leaders-in-the-open-compute-project-for-co-packaged-optics/

Related Articles

Co-Packaged Optics Testing Faces Steep Data Center RampScaling to tens of millions of CPO units per year requires the industry to first settle on automated, cost-effective methods for electrical and optical testing.

Transforming Test For Co-packaged OpticsProfound changes are underway to ensure the reliability of co-packaged opto-electronic systems.

Co-Packaged Optics Reaches Power Efficiency Tipping PointBut blazing fast data speeds come with significant manufacturing challenges.

 

 Tags:
 
Advantest
 
Amkor
 
ATE
 
Ayar Labs
 
chiplets
 
co-packaged optics
 
CPO
 
data analytics
 
data management
 
DR Yield
 
EIC
 
Intel Foundry
 
Lightmatter
 
OCP
 
Open Compute Project
 
optical fiber connectors
 
photonics
 
PIC
 
standards
 
Teradyne
 
yield learning
 
yieldWerx

### Anne Meixner

  
(all posts)

							Anne Meixner is a contributing editor at Semiconductor Engineering. She has 30+ years in the semiconductor industry. She became fascinated by defects in the semiconductor manufacturing process as a young engineer at IBM. Over that period, she has focused on test methodology with emphasis on mixed-signal and analog DFT and test. As a technical communicator she takes complex ideas and explains them in consumable understandable pieces. Meixner has worked at IBM, Carnegie Mellon University and Intel. She holds three U.S. patents and her peers have recognized her work with two best papers at IEEE International Test Conference. She founded The Engineers’ Daughter in 2015 to consult on semiconductor testing and to coach engineers.
						

### Leave a ReplyCancel reply

Comment*

Name*(Note: This name will be displayed publicly)

Email*(This will not be displayed publicly)

Notify me of follow-up comments by email.

Notify me of new posts by email.

 

Δ

 

### Technical Papers

* Controlling Voltage Droop In 2.5D PIM Chiplet Architectures (Washington St., UW-Madison)August 17, 2026by Technical Paper Link
* Self-Supervised Layout Generation To Fix Advanced-Node DRVs (Nvidia, Duke)August 12, 2026by Technical Paper Link
* 2D GAA CFETs Need Contact And Parasitic Co-Optimization At A2 Node (imec)August 12, 2026by Technical Paper Link
* Defect Prediction in Optical Lithography, EUVL, and NIL (National Taiwan University)August 12, 2026by Technical Paper Link
* Failure Analysis HW Enables System-Level Debug For 3D ICs (Google, TU Delft)August 10, 2026by Technical Paper Link
 

## Knowledge CentersEntities, people and technologies explored

Learn More

## Related Articles

### Self-Driving Cars Have An Aging Problem

								AI workloads are pushing automotive sensors harder, forcing engineers to rethink how long safety-critical systems can be trusted.
							

by 
Brendan Heffernan

### TSMC Tech Symposium 2026, By The Numbers

								Foundry rolls out aggressive new roadmap, focusing on area, power, and latency.
							

by 
Barry Pangrle

### The Sub-2nm Paradox

								Reducing variation in manufacturing, monitoring behavior over time, and targeting specific workloads can have a big impact on power, performance, and area/cost.
							

by 
Ed Sperling

### When Semiconductor Materials Misbehave

								The gap between lab performance and fab reality is growing wider as packages grow more complex.
							

by 
Gregory Haley

### TSV Complexity Leads To Manufacturing Bottleneck

								Creating through-silicon vias is a necessary but daunting challenge.
							

by 
Laura Peters

### Flash Getting Stacked High-Bandwidth Version

								Inspired by HBM, HBF could improve AI efficiency in 3D flash memory.
							

by 
Bryon Moyer

### HBM Shifts Testing Left To Preserve AI Chip Yield

								Testing sooner and more often can improve quality and reduce scrap, but it's also more costly.
							

by 
Anne Meixner

### Creating Agentic EDA Methodologies

								Current approaches involve multiple tools, vendors, designs, data formats, and abstractions. Can agents really use them all?
							

by 
Brian Bailey

 

Chip Industry Technical Paper Ro...
 
Linda Christensen
Semiconductor Earnings Roundup: ...
 
Linda Christensen

 
 

### About

* About us
* Contact us
* Advertising on SemiEng
* Newsletter SignUp

### Navigation

* Homepage
* Special Reports
* Systems & Design
* Low Power-High Perf
* Manufacturing, Packaging & Materials
* Test, Measurement & Analytics
* Auto, Security & Edge AI

* Videos
* Jobs
* Technical Papers
* Events
* Webinars
* Knowledge Centers
* Industry Research
* Business & Startups
* Newsletters
* Store

### Connect With Us

* Facebook
* Twitter@semiEngineering
* LinkedIn
* YouTube

Copyright ©2013-2026 SMG   |  
Terms of Service
  |  
Privacy Policy

This site uses cookies. By continuing to use our website, you consent to our 
Cookies Policy
ACCEPT
 
Manage consent

Close

#### Privacy Overview

 

This website uses cookies to improve your experience while you navigate through the website. The cookies that are categorized as necessary are stored on your browser as they are essential for the working of basic functionalities of the website. We also use third-party cookies that help us analyze and understand how you use this website. We do not sell any personal information.


By continuing to use our website, you consent to our Privacy Policy. If you access other websites using the links provided, please be aware they may have their own privacy policies, and we do not accept any responsibility or liability for these policies or for any personal data which may be collected through these sites. Please check these policies before you submit any personal information to these sites.

 

								Necessary							

Necessary

Always Enabled

									Necessary cookies are absolutely essential for the website to function properly. This category only includes cookies that ensures basic functionalities and security features of the website. These cookies do not store any personal information.								

								Non-necessary							

Non-necessary

									Any cookies that may not be particularly necessary for the website to function and is used specifically to collect user personal data via analytics, ads, other embedded contents are termed as non-necessary cookies. It is mandatory to procure user consent prior to running these cookies on your website.								

SAVE & ACCEPT