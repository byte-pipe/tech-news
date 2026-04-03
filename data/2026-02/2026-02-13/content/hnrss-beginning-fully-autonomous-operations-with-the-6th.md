---
title: Beginning fully autonomous operations with the 6th-generation Waymo Driver
url: https://waymo.com/blog/2026/02/ro-on-6th-gen-waymo-driver
site_name: hnrss
content_file: hnrss-beginning-fully-autonomous-operations-with-the-6th
fetched_at: '2026-02-13T11:15:58.689909'
original_url: https://waymo.com/blog/2026/02/ro-on-6th-gen-waymo-driver
date: '2026-02-12'
description: Waymo will begin fully autonomous operations with its 6th-generation Driver —an important step in bringing our technology to more riders in more cities. This latest system serves as the primary engine for our next era of expansion, with a streamlined configuration that drives down costs while maintaining our uncompromising safety standards. Designed for long-term growth across multiple vehicle platforms, this system’s expanded capabilities allow us to safely broaden our footprint into more diverse environments, including those with extreme winter weather, at an even greater scale.
tags:
- hackernews
- hnrss
---

Waymo will begin fully autonomous operations with its 6th-generation Driver —an important step in bringing our technology to more riders in more cities. This latest system serves as the primary engine for our next era of expansion, with a streamlined configuration that drives down costs while maintaining our uncompromising safety standards. Designed for long-term growth across multiple vehicle platforms, this system’s expanded capabilities allow us to safely broaden our footprint into more diverse environments, including those with extreme winter weather, at an even greater scale.

The 6th-generation Waymo Driver is the product of seven years ofsafety-proven serviceamassed from driving nearly 200 million fully autonomous miles across the densest cores of 10+ major cities and an expanding network of freeways. Our experience as the only company operating a fully autonomous service at this scale has reinforced a fundamental truth:demonstrably safe AIrequires equally resilient inputs. This deep understanding of real-world requirements is why the Waymo Driver utilizes a custom, multi-modal sensing suite where high-resolution cameras, advanced imaging radar, and lidar work as a unified system. Using these diverse inputs, the Waymo Driver can confidently navigate the "long tail" of one-in-a-million events we regularly encounter when driving millions of miles a week, leaving nothing to the imagination of a single lens.

By leveraging breakthroughs in AI and validating the system through our rigorous safety framework, we can now accelerate our journey to the road with unprecedented velocity and confidence. Today, we're lifting the lid on our 6th-generation Waymo Driver's sophisticated sensing technology delivering expanded capabilities at a lower cost.

Vision System

The Waymo Driver’s vision system goes far beyond the capabilities of human sight or standard automotive cameras. While it interprets the same semantic details we do, such as traffic light colors and road signs, it operates with a level of awareness no person can match. Our vision system can see everywhere at once and possesses a dynamic range that allows it to pull critical details out of deep shadows while being hit with the direct glare of high-beams or emergency vehicle lights.

Your web browser does not support this video.

Compared to a traditional automotive camera (right), the 6th-generation Waymo Driver camera (left) delivers significantly higher resolution at cost parity, allowing the system to make better-informed driving decisions.

At the core of this system is our next-gen 17 megapixel imager, a breakthrough in automotive vision technology. This high-resolution sensor captures millions of data points for incredibly sharp images while offering exceptional thermal stability across automotive conditions. These imagers allow the Waymo Driver to see around the vehicle with fewer cameras than if we used 5 or 8-megapixel sensors. The result is a system a generation ahead of other automotive cameras in terms of resolution, dynamic range, and low-light sensitivity.

A vision system that is reliable in inclement weather needs to keep itself clear. While cameras on conventional cars can struggle with raindrops, road grime, and ice, our system features  integrated cleaning systems  to maintain visibility. In conditions where a camera’s view may be limited, our lidar and radar provide the necessary redundancy to maintain the Waymo Driver’s perception.

This focus on high-performance sensing extends throughout our hardware system. We've pushed more processing complexity into Waymo’s custom silicon chips rather than relying on multiple hardware components. This approach delivers superior results with remarkable efficiency—our new cameras outperform the highly capable system on our 5th-generation vehicles, even as we continue to reduce costs by using less than half the number of cameras.

Lidar

Unlike cameras that rely on light reflected from the environment to see, lidar lights up its own way by using laser beams to paint a 3D picture, also known as a point cloud image, of the world around it. If you drive in the rain or snow on dark freeways, you know how hard it is to see with vision alone.

Waymo’s lidar sees the world in exceptional detail, distinguishing smaller objects like pedestrians near larger ones like vehicles, day and night.

Our 6th-generation lidar leverages the significant cost reductions the industry has seen over the last five years, especially as affordable lidar increasingly appears in consumer vehicles. By harnessing these market efficiencies alongside our custom-designed chips and optical designs—with core components designed and built in California—we have developed a system that sees at greater distances with better fidelity and higher robustness, all at a cost profile optimized for expansion.

Strategically placed short-range lidars provide redundant coverage to our cameras, enabling the Waymo Driver to associate accurate distance measurements with camera imagery. This is critical when navigating alongside vulnerable road users,  opening car doors, and other urban situations where centimeter-scale range accuracy matters. Beyond physical placement, we have reengineered how our lidar illuminates a scene and processes data internally. These upgrades help the lidar penetrate weather and avoid point cloud distortion near highly reflective signs, expanding the Waymo Driver's ability to see through heavy roadspray on freeways and other complex edge cases.

Radar

Waymo’s imaging radar creates dense, temporal maps that instantly track the distance, velocity, and size of objects in all lighting and weather conditions. By leveraging radar chipsets that have become more sensitive and affordable, we benefit from industry-wide cost reductions while continuing to expand our own capabilities.

Waymo’s imaging radar can operate in a range of severe weather conditions, providing our system more time to discern an object and inform our next move.

Our next-generation radar builds on the foundation of the 5th-generation Waymo Driver, using new in-house algorithms to deliver improved performance in rain or snow. This 6th-generation system maximizes the benefit of sensor fusion by leveraging lightweight, powerful machine-learned models to extract maximum information from each sensor and dynamically optimize the performance of every sensing component.

External Audio Receivers (EARs)

To complement our visual sensors, the Waymo Driver has long utilized several external audio receivers, or EARs, that help the Driver detect important sounds on the road, such as approaching emergency vehicles and railroad crossings, and respond accordingly. The Driver’s EARs are strategically placed around the central perception dome to optimize its ability to hear sirens and localize where the sounds are coming from while reducing the amount of wind noise it is susceptible to, especially at high speeds. Thanks to its EARs, the Waymo Driver can often hear and identify which direction a siren is traveling before it can even see it.

One driver, different vehicle platforms

The Waymo Driver can be applied to different platforms and use cases.

Because we are focused on building a Driver and not a vehicle, we’ve designed a versatile, integrated autonomous driving system that can be adapted to various platforms and use cases over time. Our versatile hardware approach allows us to reconfigure our sensors  and generalize our AI to meet each platform's unique needs—whether it is the Ojai or the Hyundai IONIQ 5—providing the Waymo Driver an optimal view of its surroundings while streamlining for efficiency. This 6th-generation system marks a major shift at ourautonomous vehicle factoryin Metro Phoenix, where we are beginning to meaningfully  scale toward a capacity of tens of thousands of units per year.  By collaborating with OEM partners to ensure base vehicles are Waymo Driver ready, we have engineered a system built for high-volume production, allowing us to unlock greater economies of scale as we bring our technology to more people.

As we transition to fully autonomous operations with the 6th-generation Waymo Driver on the Ojai, we'll continue providing our employees and their guests trips as we refine the rider experience. We can’t wait to open our doors to the public soon.

We’re looking for innovators and visionaries tojoin us to buildthe next generation of sensing technology and custom compute. From the silicon up, we’re designing the hardware that allows the Waymo Driver to see, think, and scale globally.
