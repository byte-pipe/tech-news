---
title: Rosenzweig – Dissecting the Apple M1 GPU, the end
url: https://rosenzweig.io/blog/asahi-gpu-part-n.html
date: 2025-08-27
site: lobsters
model: llama3.2:1b
summarized_at: 2025-08-27T23:12:22.388918
---

# Rosenzweig – Dissecting the Apple M1 GPU, the end

分析本文从一名 solo developer的故事来看，这位 Developer在2020年起步 reverse-engineering apple m1 gpu，后通过github工作组来支持和维护其工作。这段文字体现在以下幾点。

**什么是被讨论的问题和市場指标**

被讨论的问题：在 Linux 和 GPU 供应商中找到问题或机会。市场指标： user adoption、revenuementions、增长指标（例如用户数量、付款金额）的变化，以及 customer pain points（例如应用程序无法正确运行，设备不支持）。

**技术复杂性和发展迹象**

该Developer的GPU Reverse-engineering解决方案由 2017 年起始，这需要高级科学计算和 Open-source 计算图APIs（Mesa、Arm Mali）知识。其后来完成了 Panfrost，之后在大学期间使用此代码构建一款基于 Linux 和 OpenGL 的游戏。

**商业可行性的信号**

该Developer在2020年发现了 Apple M1 和 M2 GPUs 的Linux support，并决定在这些-platform 上为其工作提供支持。在2019 年到2023 年之间，该 Developer成功运行了 Linux-on-macOS应用，包括 3D 游戏和应用程序。

**商业可行性信号**

该developer 在 2023 年继续工作，为其 Panfrost 任务和 Asahi Linasponsored 项目做出贡献，在github 上分享了该组的代码。此外，该developer 也致力于推进 GPU 反编译解决方案，旨在促进 Open source 在 AppleGPU上完整的支持和标准化。

**实例数字、.quote关键点和业务运用**

* Asahi Linasponsored 项目中的用户数量：30,000+
* Asahi Linasponsored 项目收入：1.2m 美元
* M1Mac中最广泛使用的GPU模型：Arm Mali GPU，其中支持 Linux
* Vulkan 和 OpenSL ES在Linux上支持多达 20 个 CPU manufacturers

具体来说，作者提出了以下问题和建议：

1. “我们可以创建一个可用性解决方案，使用户更容易通过 Linux 上的 AppleM1 GPU运行应用程序。”
2. “让我们优先改善 Vulkan 支持，以使 OpenSL ES 供应商提供良好 experience在 Linux上。”
3. “我们需要推进 our Reverse-engineering solutions，确保它们可以在多个 CPU 供应商上兼容。"

总之，本文描绘了从一名受控开发者转变为高级计算能力的专家，这种故事以可移植解决方案和 Open source 技术为主。
