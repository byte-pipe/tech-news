---
title: How Microsoft Vaporized a Trillion Dollars
url: https://isolveproblems.substack.com/p/how-microsoft-vaporized-a-trillion
site_name: hackernews_api
content_file: hackernews_api-how-microsoft-vaporized-a-trillion-dollars
fetched_at: '2026-04-04T01:01:11.728166'
original_url: https://isolveproblems.substack.com/p/how-microsoft-vaporized-a-trillion
author: Axel Rietschin
date: '2026-04-03'
description: Inside the complacency and decisions that eroded trust in Azure—from a former Azure Core engineer.
tags:
- hackernews
- trending
---

# How Microsoft Vaporized a Trillion Dollars

### Inside the complacency and decisions that eroded trust in Azure—from a former Azure Core engineer.

Axel Rietschin
Mar 29, 2026
39
2
Share

This is the first of a series of articles in which you will learn about what may be one of the silliest, most preventable, and most costly mishaps of the 21st century, where Microsoft all but lost OpenAI, its largest customer, and the trust of the US government.

I joined Azure Core on the dull Monday morning of May 1st, 2023, as a senior member of the Overlake R&D team, the folks behind the Azure Boost offload card and network accelerator.

I wasn’t new to Azure, having run what is likely the longest-running production subscription of this cloud service, which launched in February 2010 as Windows Azure.

I wasn’t new to Microsoft either, having been part of the Windows team since 1/1/2013 and later helped migrate SharePoint Online to Azure, before joining the Core OS team as a kernel engineer, where I notably helped improve the kernel and helped invent and deliver the Container platform that supports Docker, Azure Kubernetes, Azure Container Instances, Azure App Services, and Windows Sandbox, all shipping technologies that resulted in multiple granted patents.

Furthermore, I contributed to brainstorming the early Overlake cards in 2020-2021, drafting a proposal for a Host OS <-> Accelerator Card communication protocol and network stack, when all we had was a debugger’s serial connection. I also served as a Core OS specialist, helping Azure Core engineers diagnose deep OS issues.

I rejoined in 2023 as an Azureexperton day one, having contributed to the development of some of the technologies on which Azure relies and having used the platform for more than a decade, both outside and inside Microsoft at a global scale.

As a returning employee, I skipped the New Employee Orientation and had my Global Security invite for 12 noon to pick up my badge, but my future manager asked if I could come in earlier, as the team had their monthly planning meeting that morning.

I, of course, agreed and arrived a few minutes before 10 am at the entrance of the Studio X building, not far from The Commons on the West Campus in Redmond. A man showed up in the lobby and opened the door for me. I followed him to a meeting room through a labyrinth of corridors.

The room was chock-full, with more people on a live conference call. The dev manager, the leads, the architects, the principal and senior engineers shared the space with what appeared to be new hires and junior personnel.

The screen projected a slide where I recognized a number of familiar acronyms, like COM, WMI, perf counters, VHDX, NTFS, ETW, and a dozen others, mixed with new Azure-related ones, in an imbroglio of boxes linked by arrows.

I sat quietly at the back while a man was walking the room through a big porting plan of their current stack to the Overlake accelerator. As I listened, it was not immediately clear what that series of boxes with Windows user-mode and kernel components had to do with that plan.

After a few minutes, I risked a question: Are you planning toportthose Windows features to Overlake? The answer was yes, or at least they were looking into it. The dev manager showed some doubt, and the man replied that they could at least “ask a couple of junior devs to look into it.”

The room remained silent for an instant. I had seen the hardware specs for the SoC on the Overlake card in my previous tenure: the RAM capacity and the power budget, which was just a tiny fraction of the TDP you can expect from a regular server CPU.

The hardware folks I had spoken with told me they could only spare 4KB of dual-ported memory on the FPGA for my doorbell shared-memory communication protocol.

Everything was nimble, efficient, and power-savvy, and the team I had joined 10 minutes earlier wasseriouslyconsidering porting half of Windows to that tiny, fanless, Linux-running chip the size of a fingernail.

That felt like Elon talking about colonizing Mars: just nuke the poles then grow an atmosphere! Easier said than done, uh?

That entire 122-strong org was knee-deep in impossible ruminations involving porting Windows to Linux to support their existing VM management agents.

The man was a Principal Group Engineering Manager overseeing a chunk of the software running on each Azure node; his boss, a Partner Engineering Manager, was in the room with us, and theyreallycontemplated porting Windows to Linux to support their current software.

At first, I questioned my understanding. Was that serious? The rest of the talk left no doubt: the plan was outlined, and the dev leads were tasked with contributing people to the effort. It was immediately clear to me that this plan would never succeed and that the org neededa lotof help.

That first hour in the new role left me with a mix of strange feelings, stupefaction, and incredulity.

The stack was hitting its scaling limits on a 400 Watt Xeon at just a few dozen VMs per node, I later learned, a far cry from the 1,024 VMs limit I knew the hypervisor was capable of, and was a noisy neighbor consuming so many resources that it was causing jitter observable from the customer VMs.

There is no dimension in the universe where this stack would fit on a tiny ARM SoC and scale up by many factors. It was not going to happen.

I have seen a lot in my decades of industry (and Microsoft) experience, but I had never seen an organization so far from reality. My day-one problem was therefore not to ramp up on new technology, but rather to convince an entire org, up to my skip-skip-level, that they were on a death march.

Somewhere, I knew it was going to be a fierce uphill battle. As you can imagine, it didn’t go well, as you will later learn.

I spent the next few days reading more about the plans, studying the current systems, and visiting old friends in Core OS, my alma mater. I was lost away from home in a bizarre territory where people made plans that didn’t make sense with the aplomb of a drunk LLM.

I notably spent more than 90 minutes chatting in person with the head of the Linux System Group, a solid scholar with a PhD from INRIA, who was among the folks who hired me on the kernel team years earlier.

His org is responsible for delivering Mariner Linux (now Azure Linux) and the trimmed-down distro running on the Overlake / Azure Boost card. He kindly answered all my questions, and I learned that they had identified 173 agents (one hundred seventy-three) as candidates for porting to Overlake.

I later researched this further and found that no one at Microsoft, not a single soul, could articulate why up to 173 agents were needed to manage an Azure node, what they all did, how they interacted with one another, what their feature set was, or even why they existed in the first place.

Azure sells VMs, networking, and storage at the core. Add observability and servicing, and you should be good. Everything else, SQL, K8s, AI workloads, and whatnot all build on VMs with xPU, networking, and storage, and the heavy lifting to make the magic happen is done by the good Core OS folks and the hypervisor.

How the Azure folks came up with 173 agents will probably remain a mystery, but it takes a serious amount of misunderstanding to get there, and this is also how disasters are built.

Now, fathom for a second that this pile of uncontrolled “stuff” is orchestrating the VMs running Anthropic’s Claude, what’s left of OpenAI’s APIs on Azure, SharePoint Online, the government clouds and other mission-critical infrastructure, and you’ll be close to understanding how a grain of sand in that fragile pileup can cause a global collapse, with serious National Security implications as well as potential business-ending consequences for Microsoft.

We are still far from the vaporized trillion in market cap, my letters to the CEO, to the Microsoft Board of Directors, and to the Cloud + AI EVP and their total silence, the quasi-loss of OpenAI, the breach of trust with the US government as publicly stated by the Secretary of Defense, the wasted engineering efforts, the Rust mandate, my stint on the OpenAI bare-metal team in Azure Core, the escort sessions from China and elsewhere, and the delayed features publicly implied as shipping since 2023, before the work even began.

If you’re running production workloads on Azure or relying on it for mission-critical systems, this story matters more than you think.

Click for Part 2.

39
2
Share