---
title: Medium
url: https://blog.argoproj.io/argo-cd-2026-user-survey-results-dcffc9a8e48e
site_name: tldr
content_file: tldr-medium
fetched_at: '2026-07-15T19:31:02.276904'
original_url: https://blog.argoproj.io/argo-cd-2026-user-survey-results-dcffc9a8e48e
author: Nikita 'Kit' Dergilev
date: '2026-07-15'
published_date: '2026-07-09T14:23:45.355Z'
description: Argo CD 2026 User Survey Results We’re happy to share the results of the 2026 Argo CD user survey! We have never had this many people engage with Argo CD surveys; this year, we broke a record with …
tags:
- tldr
---

# Argo CD 2026 User Survey Results

Nikita 'Kit' Dergilev
12 min read
·
6 days ago

--

Listen

Share

Press enter or click to view image in full size

We’re happy to share the results of the 2026 Argo CD user survey! We have never had this many people engage with Argo CD surveys; this year, we broke a record with 269 responses.

Last year, we added a new section to capture the community’s insights onenvironment promotions. This year, we asked the same questions to learn what has changed over the last 12 months (and a few things have changed rapidly; see the section onenvironment promotionsbelow). We also added a new section to learn about AI/ML and Argo CD.

So, what did we learn?

## TL;DR

Argo CD has been and remains the standard for GitOps deployments. It’s well established and loved by the community.

Implementations of Argo CD are becoming more mature; compared to last year, fewer companies use manual promotions or struggle with traceability across environments. However, modeling environments remain the second-most-common challenge for Argo CD users.

What’s the first one? Its performance when a single Argo CD instance manages many Applications and/or clusters. To give an idea of the scale of organizations that use Argo CD, 42% of respondents report managing 500+ Applications. 25% of respondents are running more than 10 instances.

Argo CD is widely used for AI/ML workloads: 80% of organizations that deploy or manage them use it for deployments, and 60% use it in production.

A few extra insights:

* The popularity of ApplicationSets continues to grow; 79% of respondents use them this year.
* Significantly more organizations are using the Argo CD Operator for installations than in 2025.
* More organizations are adopting dedicated tools forenvironment promotionsand moving from manual manifest updates. The top promotion challenges shifted with them: traceability dropped from first place, while release gates and standardized pipelines are now the leading pain points.

## What does the community think of Argo CD?

Every year, we ask respondents whether they are likely to recommend Argo CD to others. This year, over 75% of respondents recommended the tool, which is consistent with last year’s findings. This gives a Net Promoter Score (NPS) of 73.4, well above the NPS of most tools in this space. The community support is strong.

Press enter or click to view image in full size

A few quotes from the community:

“Thank you all for your hard work! I’ve been running ArgoCD for nearly five years, and it’s been a pleasure to use and work with.”

“Keep going, you’re great.”

“Keep doing God’s work like you have done so far!”

“You all rock!”

“Argo CD is great, keep it up.”

## Who uses Argo CD?

As in most of our surveys, the majority of respondents are Platform Engineers, with DevOps Engineers as the second-largest group. This year, though, we noticed a new trend: the number of SREs is noticeably higher than in 2025.

The number of responders in this role isn’t large enough to draw conclusions about an industry shift underway; however, it’s worth noting that the same role might have different names across organizations. That said, there is a slight dip in DevOps Engineer representation, which could suggest some overlap or a gradual transition. It’s an interesting trend to watch.

Press enter or click to view image in full size

The survey findings are heavily weighted towards the experiences of small to mid-sized companies, with a large portion of respondents (44%) from companies with fewer than 100 engineers, and 32% of respondents are from companies with between 100 and 500 engineers.

## What does Argo CD adoption look like in 2026?

The adoption numbers haven’t changed much since 2025. With 66% of respondents using Argo CD in production for more than two years, a clear sign of a maturing community that has graduated from early adoption to established everyday infrastructure.

Press enter or click to view image in full size

Among the more seasoned adopters in this community, almost 60% run three-quarters of their production applications on Kubernetes, and 66% manage more than three-quarters of these applications with Argo CD. The combination of Kubernetes adoptionandArgo CD makes it the tool of choice for many Kubernetes users.

At the same time, and it shouldn’t be a surprise, there is a strong correlation between the size of the organization and the percentage of applications running on Kubernetes. For example, among organizations with 500 to 2000 engineers, only 39% have more than a quarter of their applications on Kubernetes. This means that these organizations have heterogeneous infrastructure, which explains some of the challenges we’ll cover in the following sections.

Press enter or click to view image in full size

The community still mostly uses Argo CD for business applications (87%), cluster bootstrapping (65%), and infrastructure management (64%). As last year, almost a third of Argo CD users manage databases with it. What’s new this year is that 22% of respondents use Argo CD to manage AI/ML workloads.

Most organizations use Argo CD for multiple use cases; it’s typical to use Argo CD for two of three scenarios, like infrastructure management and business application deployments. However, around 12% of respondents use it solely for platform needs, without deploying business applications.

Press enter or click to view image in full size

The main installation method for Argo CD hasn’t changed since 2025. Most organizations still prefer Helm, and Kustomize is the second most common response. The only significant change is the growing popularity of Argo CD Operator. Last year, less than 1% of respondents used it; this year, it has grown to 8%, a significant increase.

Press enter or click to view image in full size

Another point worth noting is the persistent popularity of cluster-wide installations over namespace-scoped installations. Most likely, many organizations install Argo CD on the clusters where they also run Applications and/or don’t consider risks associated with cluster-wide installations significant.

## What is the scale of Argo CD implementations?

When looking into the scale of Argo CD implementation, the 2026 numbers show an interesting trend: the number of organizations running between 500 and 2000 Applications is shrinking (from 28% in 2025 to 17% in 2026). At the same time, the share of organizations running under 50 or more than 2000 Applications is growing.

This could be explained by broader industry patterns in which organizations are reacting to the “cost of tool sprawl” from years of over-enthusiastic tool adoption, leading to consolidation(https://www.techzine.eu/blogs/applications/136174/the-state-of-cloud-native-computing-in-2025/). On the other end of the spectrum, organizations may be successfully maturing into large-scale enterprises by investing in Platform Engineering and standardized guardrails (https://www.veeam.com/blog/kubernetes-2025-enterprise-trends.html).

At the same time, the number of clusters per Argo CD instance didn’t change much since 2025. The only noticeable shift is the dropping number of respondents having one cluster per instance. This aligns with “scale” being one of the top challenges, as organizations connect more clusters to fewer instances, the pressure on each instance grows.

Press enter or click to view image in full size

What patterns and sub-projects do the community use the most?

This year, we added more options to the questions about sub-projects and patterns. However, it didn’t change the overall picture. The two most popular patterns are still App-of-Apps and ApplicationsSets. And ApplicationSets are growing in popularity (from 66% in 2025 to 76% in 2026). This is a clear signal of the community’s growing maturity and a strong indication that it follows best practices, thereby extracting maximum value from the tool.

Press enter or click to view image in full size

A few extra noticeable observations:

* Sync waves and hooks are used by more than half of the respondents (54%). This might indicate that organizations are solving the deployment automation problem in-house without dedicated tools.
* The adoption of source hydrator has increased over the last year, but the absolute numbers are still low. It’s a good sign from the community. There might be changes needed to simplify adoption or better explain the tool’s value.

For the sub-project options, we explicitly added Argo Rollouts, Argo Workflows, and Argo Events to the list. Last year, we ran separate surveys for them. The adoption numbers for these projects are impressive, 63% of respondents use Argo Rollouts, 43% use Argo Workflows, and 26% use Argo Events.

Press enter or click to view image in full size

Use of other projects decreased in 2026 compared to 2025. New survey options might explain the drop in the numbers. At the same time, some of the drop can be explained by the growing adoption of dedicated CD tools.

## GetNikita 'Kit' Dergilev’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe
Subscribe

Remember me for faster sign in

The only project growing in 2026 compared to 2025 is the Argo CD Agent. The total number is still significantly lower than the number of respondents connecting multiple clusters to a single Argo CD instance. It’s interesting to see whether adoption of the Agent increases over time and whether it addresses scalability and performance challenges.

## Environment promotion

We first explored theenvironment promotiontopic last year. We repeated the questions this year to spot any trends and added an extra question about the promotion mechanics.

One thing that hasn’t changed since 2025 is the number of environments. Half of the respondents still have 1–3 environments, and only 13% run more than 8.

The promotion methods shifted significantly during the last 12 months. The most noticeable change is the drop in manual promotions. The reasons aren’t clear; however, tools like GitOps Promoter and Kargo have had time to gain traction, and organizations using Argo CD are moving towards fully automated pipelines.

Press enter or click to view image in full size

At the same time, the larger the organization, the more likely it is to use custom scripts, in-house solutions, or manual manifest updates. The survey results don’t explain the reason. We can assume that large companies that have already implemented sophisticated in-house solutions would be slow to adopt new solutions, as they might require significant rework on their end. Another potential reason is that large organizations often use multiple Argo CD instances and need centralized solutions to manage promotions across them.

Press enter or click to view image in full size

At the same time, there is a correlation between theenvironment promotion-related challenges and organization size. We also see a significant shift in responses for this question. Traceability across environments (38%), the main challenge in 2025, is now in third place. It’s still a major pain point, but release gates (50%) and standardized pipelines (44%) are more significant for respondents in 2026.

Press enter or click to view image in full size

The growing popularity of automation tools might explain these changes. These tools usually provide a good overview of the Application status and let cross-environment traceability. At the same time, they don’t solve the more advanced CD needs like gates and standardized pipelines as easily. These results suggest a clear path for current tools to develop or for the community to seek more advanced solutions.

Finally, this year, we learned what mechanisms the community use to roll out new Application versions. Two methods stand out clearly from the rest: Helm values and plain YAML manifest updates.

Press enter or click to view image in full size

Looking more closely into what methods are usually used together, we found that teams updating Helm values also often use Helm umbrella chart and almost as often update the Helm chart version in Application specification or via ApplicationSet generators (actually, if a team uses ApplicationSet generators, they will use Helm values in 81% of cases).

Press enter or click to view image in full size

These insights can help the community focus on scenarios that are more relevant to organizations using Argo CD.

## AI/ML workloads

For the first time this year, we explored AI/ML workloads more deeply. Most respondents don’t deploy or manage such workloads; however, 80% of those who do already use Argo CD (60% in production).

Press enter or click to view image in full size

AI/ML is already a genuine Argo CD use case. More than half of the respondents use Argo CD to deploy model inference/serving endpoints. Interestingly, only 27% use Argo CD for AI agents or multi-model orchestration.

Model inference and LLM serving, not training, are the most common preferences here, which makes sense: these are long-running, declarative deployments that GitOps suits well.

Press enter or click to view image in full size

The biggest AI/ML-related deployment challenges (we asked this question for all tools involved in the deployment, not just Argo CD) are GPU resource allocation, managing model images, lack of visibility, and deployments across GPU and non-GPU nodes.

Press enter or click to view image in full size

These results point to real opportunities to further develop Argo CD and other Argo projects. It’s worth noting that ~20% of respondents also flagenvironment promotionsand progressive rollouts as needs, which are challenges that are not AI/ML-specific but remain relevant.

## What challenges are teams facing?

One of the most interesting questions in the survey is about the challenges teams face with Argo CD. Based on last year’s feedback, we added scaling and performance as options, and respondents reported them as the main challenge straight away.

Press enter or click to view image in full size

The other common challenges are “troubleshooting”, “environment modeling promotions”, “RBAC and multi-tenancy”. Compared to last year, “insufficient automation” dropped from 22% to 13%. This change might be caused by other challenges taking priority.

Some challenges correlate with the respondent’s role. For example, Platform Engineers focus on “scaling and performance” more than others.

Press enter or click to view image in full size

Looking more closely at the “scaling and performance” data, we found that this is more common for companies managing more Applications or having more engineers, which is somewhat expected. What’s less expected is how significant the problem is for companies managing more than 2000 Applications. Half of the respondents named this challenge among their top 3 challenges with Argo CD. This indicates that this problem is worth solving, especially as the overall number of Applications is growing; therefore, more organizations will experience it.

Press enter or click to view image in full size

We also asked respondents about missing features that would remove pain points for their teams.

Press enter or click to view image in full size

The top themes identified are

* Environment promotion and pipelines (25%):Teams want built-in workflows for approvals and verifications. They’re looking to move past simple autosync and want better ways to manage promotions across multiple clusters.
* UI features and performance (23%):Users want faster, more responsive dashboards, especially for large applications. Top requests include easier management of application sets and clearer error messages.
* RBAC and security (9%):Teams are looking for easier security setup, including better support for Kubernetes groups and improved audit logs for compliance.
* Observability (8%):Teams need a way to check if a specific commit is healthy before their pipeline continues, bridging a key gap between CI and CD.
* Dependency management (7%):For complex deployments, current “sync waves” aren’t enough. Users are requesting more advanced dependency control to manage deployment order across apps.

Overall, these findings are positive: the results show that the community is satisfied with Argo CD’s core deployment functionality, with users requesting better tooling to manage everything around them. These missing features indicate that users are moving beyond basic deployments and are now focused on optimizing the operational layer surrounding them.

## What Argo CD features are most useful for users?

Rounding out the survey, we explored which Argo CD features respondents find most useful in practice. Three capabilities stood out most here as the backbone for Argo CD users.

Press enter or click to view image in full size
1. ApplicationSets and App-of-apps (25%):These are important for managing multiple clusters and rolling out standard components at scale. They make centralized sync management easy, and users value the PR generator for creating temporary (ephemeral) environments.
2. Autosync self-healing (22%):This is the key “safety net” for Argo CD. Respondents trust it to maintain their infrastructure consistency without manual intervention.
3. The UI (20%):This allows users to inspect live resources and manage their platform from a single central place, serving as “Kubernetes for developers”.

## Final words

The 2026 survey brought a considerably larger and growing Argo CD-engaged community and delved deeper into deployment challenges, the patterns behindenvironment promotions, and the state of AI/ML deployments. These findings will inform the project’s further development.

We really appreciate the time and effort of everyone who participated in the survey. Your insights are critically important for the community. Many thanks!

This survey wouldn’t be possible without Charlotte Fleming, Carolyn King, Adriana Naula, and Katie Lamkin-Fulsher. Great work, team.