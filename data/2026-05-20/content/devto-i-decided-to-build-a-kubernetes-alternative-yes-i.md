---
title: I decided to build a Kubernetes alternative. Yes, I know I'm crazy - DEV Community
url: https://dev.to/denerfernandes/i-decided-to-build-a-kubernetes-alternative-yes-i-know-im-crazy-21b5
site_name: devto
content_file: devto-i-decided-to-build-a-kubernetes-alternative-yes-i
fetched_at: '2026-05-20T19:46:44.815750'
original_url: https://dev.to/denerfernandes/i-decided-to-build-a-kubernetes-alternative-yes-i-know-im-crazy-21b5
author: Dener Fernandes
date: '2026-05-20'
description: Using Kubernetes is a love-hate relationship. Love, because before it, deploying to production was... Tagged with opensource, kubernetes, devops, infrastructure.
tags: '#opensource, #kubernetes, #devops, #infrastructure'
---

The 15-abstraction hurdle for small teams

Using Kubernetes is a love-hate relationship.

Love, because before it, deploying to production was something dark and uncertain. Many tools tried to solve this problem — Mesos, Fleet, Nomad — but only Kubernetes meaningfully solved container orchestration at scale. It's not without merit that today over 96% of organizations using containers run Kubernetes, according to the 2023 CNCF report.

But as nothing is perfect, a piece of software built by Google engineers fell short on design — not UI design, but how things actually work. Engineers think like engineers: it works, but Kubernetes complexity is something you'll likely need a dedicated course to truly understand. On one side it created entire careers — the CKA certification became a market commodity — on the other, small companies that can't afford a certified DevOps engineer find themselves at a crossroads: they feel the need for Kubernetes but can't manage it.

The concrete problem: a minimal Kubernetes cluster requires understanding at least 15 different abstractions — Pods, Deployments, Services, Ingress, ConfigMaps, Secrets, RBAC, PVCs, StorageClasses, NetworkPolicies, and so on. And incredibly, with each release that number grows. Kubernetes 1.29 introduced over 60 API changes. In 2024, more than 10 APIs that projects depended on were deprecated.Several projects tried to reduce this complexity. Rancher added a solid UI layer on top of Kubernetes. Dokploy, which doesn't use Kubernetes but Docker Swarm instead, achieved something remarkable: the first time I used it, I had a project running in production in minutes, no course needed, no major concerns. Their UX is genuinely good.

But I have one problem with Dokploy: it uses Docker Swarm. And while Swarm is still technically maintained by Docker Inc., development has slowed dramatically in favor of Kubernetes-based solutions, the ecosystem stopped investing in it, and adoption has shrunk. It's a functionally stagnant project — which for critical infrastructure is a real risk.

HashiCorp's Nomad tried a different path — simpler than Kubernetes, single binary, without all the ceremony. But in my opinion it made the mistake of being too tightly coupled to the HashiCorp ecosystem: Consul for service discovery, Vault for secrets, Terraform for infrastructure. It works great if you adopt everything. If you don't, it's limiting. And now, after HashiCorp was acquired by IBM in 2024 and changed its license from MPL to BSL, that dependency became even riskier for anyone building on top of it.

Something about me you should know: I love studying anything related to IT. Beyond being my profession, it's a hobby. And I like giving meaning to what I study.

With that said, I recently started a personal project. I have three VPS instances, started analyzing what I'd need, and realized I didn't need the full complexity of the Kubernetes stack. I went with Dokploy — it works fine for an MVP. But the question remained: what happens when it grows?

So one day, in the shower, reflecting on all of this, I thought: I can use Dokploy while it's an MVP, I can take a Kubernetes course and hope the AI configures everything correctly, or I can build a real alternative. I went with the obvious choice: build the alternative.

You might think I'm crazy. But Kubernetes itself was born from Google engineers who thought they could do better than Borg. Docker was born from someone who thought LXC could be simpler. Real projects emerge when people decide to think differently about known problems.

My goal isn't fame or money. The project will be 100% open source, Apache 2 license, no paid tiers. What I want is to solve a real problem: unnecessary complexity in container orchestration. I'm not promising I'll succeed — but it's worth trying.

I've been working on this for a few weeks now. The repository is still private, but soon, once I have a more stable version, I'll make it public. In the next posts I'll detail the architecture decisions and the reasoning behind them — including why I built my own orchestrator instead of layering on top of Kubernetes.

If you also feel that Kubernetes complexity is out of proportion with the problem it solves, follow along. I'll probably make a lot of mistakes — but I'll document everything.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse