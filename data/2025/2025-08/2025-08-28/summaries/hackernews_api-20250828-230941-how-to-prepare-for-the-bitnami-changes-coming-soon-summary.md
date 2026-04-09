---
title: How to prepare for the Bitnami Changes coming soon
url: https://community.broadcom.com/tanzu/blogs/beltran-rueda-borrego/2025/08/18/how-to-prepare-for-the-bitnami-changes-coming-soon
date: 2025-08-28
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-08-28T23:09:41.397052
---

# How to prepare for the Bitnami Changes coming soon

**Analysis:**

The article discusses the upcoming changes to Bitnami's public catalog (docker.io/bitnami) and how solo developers can prepare. The authors are providing a 10-day notice before the catalog deletion, followed by brownouts to raise awareness.

**Market indicators:**
- User adoption is not mentioned
- Revenue mentions are not provided
- Growth metrics are mentioned as "community feedback", which indicates a growing community that needs updates and support.
- Customer pain points appear to be about finding suitable alternatives for deprecated images in a rapidly changing environment, such as transitioning from older Bitnami content to new Bitnami Secure Images.

**Technical feasibility for a solo developer:**
- Complexity is moderate to high due to the need to update pipelines, internal mirrors, and Kubernetes clusters.
- Required skills may include experience with containerization, Helm charts, and security practices.
- Time investment required appears to be significant, possibly several weeks or months depending on individual's workflow.

**Business viability signals:**
- Willingness to pay is demonstrated by the 10-day notice before catalog deletion, indicating customers are not eager for alternatives like Bitnami Legacy Registry.
- Existing competition may not appear as a direct threat since most alternatives offer deprecated content; however, it cannot be ruled out that future competitors will provide suitable alternatives.
- Distribution channels like GitHub and Bitnami's official website provide existing communication channels for discussing changes and alternatives.

**Actionable insights:**
1. **Upskill:** Solo developers should focus on acquiring skills in creating secured images (BSI), Helm charts, and containerization to handle the transition smoothly.
2. **Prepare pipelines and mirrors:** Update internal mirrors and Kubernetes clusters before the brownouts begin, ensuring they can serve temporary versions of deprecated content.
3. **Diversify offerings:** Consider providing an alternative solution with a paid plan that offers more secure images for customers willing to invest in upgrading their ecosystem.

**Additional Insights:**

- The article does not provide information on the new Bitnami registry available after February 28, but it mentions how users can obtain existing Docker Hub container images from July to September as temporary solutions before adopting Bitnami's Secure Images (BSI).

Specific numbers mentioned include:

* No user adoption metrics provided
* Revenue mention implies a need for more information on how revenue is generated and who is potentially losing business due to these changes.
