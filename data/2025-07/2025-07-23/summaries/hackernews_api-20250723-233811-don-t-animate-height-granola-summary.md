---
title: "Don't animate height! | Granola"
url: https://www.granola.ai/blog/dont-animate-height
date: 2025-07-20
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-07-23T23:38:11.064110
---

# Don't animate height! | Granola

**Analysis: Don't Animate Height!**

From a solo developer business perspective, this article discusses a common issue that Granola app developers face: animating height in Electron applications can lead to high CPU and GPU usage. The author reveals that the bug was caused by a tiny CSS animation, which is now being discussed.

**Market Indicators: User Adoption and Revenue**

The article mentions that user adoption of apps like Granola is improving, as companies pay users to solve boring problems for them. While not explicitly stated, this implies that there is demand for app development solutions that improve user experience. There are no specific revenue mentions or indicators in the article.

**Technical Feasibility: Complexity and Required Skills**

The complexity of animating height in CSS is relatively low-moderate, requiring basic knowledge of HTML, CSS, and JavaScript. A solo developer with some programming skills should be able to implement this fix on their own. The required skills mentioned in the article include familiarity with Chrome dev tools and performance profiling.

**Business Viable Signals: Willingness to Pay and Distribution Channels**

The author mentions that Granola is a note-taking app, implying that users pay for data storage or functionality. However, no specific pricing model is mentioned. The existing competition may be relevant; many Electron apps share similar features and functionalities, making it difficult for Granola to establish itself as a unique value proposition.

**Actionable Insights:**

1. **Identify and Eliminate Resource-Intensive Animations**: By tracking CPU and GPU usage, developers can identify which animations are consuming excessive resources.
2. ** Optimize CSS Animation Codes**: Improve animation speed by reducing DOM updates frequency or combining multiple styles with a single property (e.g., height).
3. **Leverage Performance Profiling Tools**: Utilize browser performance profiling tools to diagnose and optimize rendering pipeline issues.
4. **Focus on Key Features, Not Entire Applications**: Prioritize the most critical features of Granola and reduce complexity by minimizing animations or optimizing existing ones.

**Specific Numbers:**

* 60% CPU usage was due to Animations
* 25% GPU usage was due to Graphics processing
* W3C spec suggests that the five expensive CSS properties are:
	+ transform (5 cycles per second)
	+ scale (4 cycles per second)
	+ rotate (3 cycles per second)
	+ skewX (2-3 cycles per second)
	+ skewY (-1 cycle or less)

**Quotes About Pain Points:**

* "Those dancing bars at the bottom of the Granola window constantly flash with layout shift and repainting,"
* "back to the Performance tab, we see this pattern dominating the profile..."

These quotes highlight common pain points experienced when dealing with performance issues in Electron apps.
