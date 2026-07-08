---
title: China’s cybersecurity standard on AI agent deployment
url: https://www.geopolitechs.org/p/chinas-cybersecurity-standard-on
site_name: tldr
content_file: tldr-chinas-cybersecurity-standard-on-ai-agent-deployme
fetched_at: '2026-07-08T11:37:56.113385'
original_url: https://www.geopolitechs.org/p/chinas-cybersecurity-standard-on
author: Geopolitechs
date: '2026-07-08'
description: the TC260’s Cybersecurity Standards Practice Guide – Security Guidelines for the Deployment and Use of AI Agents
tags:
- tldr
---

# China’s cybersecurity standard on AI agent deployment

### the TC260’s Cybersecurity Standards Practice Guide – Security Guidelines for the Deployment and Use of AI Agents

Geopolitechs
Jul 04, 2026
8
4
Share

China’s National Information Security Standardization Technical Committee (TC260) has officially released theCybersecurity Standards Practice Guide – Security Guidelines for the Deployment and Use of AI Agents.

The document follows a clear lifecycle-based security framework. It requires AI agents to undergo security assessments before they are put into use, complete security hardening prior to deployment, operate under strict permission controls throughout their lifecycle, and ensure that all data is securely erased when they are decommissioned.

Across every stage of this lifecycle, the guidelines repeatedly emphasize six practical security requirements: ensuring the integrity and trustworthiness of software and model sources; enforcing the principle of least privilege; minimizing network exposure; maintaining comprehensive audit logs of agent activities; implementing controls over high-risk operations; and applying enhanced safeguards to sensitive data and long-term memory.

The guidance suggests that China no longer regards AI agents merely as lightweight application-layer components built on top of large language models. Instead, regulators increasingly view them as integrated systems that combine memory, tool use, autonomous decision-making, and operational privileges—systems that introduce an entirely new category of security risks requiring dedicated governance.

Separately, the Cyberspace Administration of China, together with four other government agencies, has issued theInterim Measures for the Administration of Anthropomorphic AI Interaction Services, which will take effect on15 July 2026.

In early July, both Doubao and Tongyi Qianwen notified users that certain AI agent features would be discontinued during the same period. According to multiple media reports, these adjustments form part of a broader compliance campaign aimed at bringing anthropomorphic AI services and user-created AI agents into line with the new regulatory framework. Importantly, this should not be interpreted as China seeking to restrict AI agent technology as such. Rather, it reflects a shift toward more granular regulation, with authorities requiring major platforms to remove or modify product features with ambiguous regulatory boundaries before the new rules formally come into force.

Below is the full translation of the standard:

TC260-PG-20266A

Cybersecurity Standard Practice Guide— Security Guidance for Agent Deployment and Use

(v1.0-202607)

Secretariat of the National Technical Committee 260 on Cybersecurity of Standardization Administration of China

July 2026

This document is available at:www.tc260.org.cn/

Foreword

The Cybersecurity Standard Practice Guide (hereinafter referred to as the “Practice Guide”) is a standards-related technical document organized, developed, and issued by the Secretariat of the National Technical Committee 260 on Cybersecurity of Standardization Administration of China (hereinafter referred to as the “TC260 Secretariat”). It is intended to promote cybersecurity-related standards and knowledge and provide standardized practice guidance around topics such as cybersecurity laws, regulations and policies, standards, and cybersecurity hotspots and incidents.

This document was drafted by the China Electronics Standardization Institute, National Computer Network Emergency Response Technical Team/Coordination Center of China, Tsinghua University, Pujiang National Laboratory, Beijing Zhongguancun Laboratory, Data and Technology Support Center of the Cyberspace Administration of China, Zhejiang University, Alibaba Cloud Computing Co., Ltd., Huawei Cloud Computing Technologies Co., Ltd., Beijing Volcano Engine Technology Co., Ltd., Beihang University, China Mobile Communications Group Co., Ltd., The Fifth Electronics Research Institute of the Ministry of Industry and Information Technology, Beijing University of Posts and Telecommunications, Beijing Shengxin Network Technology Co., Ltd., Tencent Cloud Computing Co., Ltd., Hangzhou Anheng Information Technology Co., Ltd., Fangcun Yueqian (Xiong'an) Technology Co., Ltd., Hangzhou Turing Zhiyue Technology Co., Ltd., Beijing NSFOCUS Technologies Group Co., Ltd., and Beijing Qihoo Technology Co., Ltd.

The principal drafters of this document are Yao Xiangzhen, Bo Zhaoyi, Ren Kui, Xu Wei, Zhou Ruikang, Wang Bo, Wang Yingchun, Cui Yong, Li Qi, Hao Chunliang, Wang Zhiwei, Liu Xianglong, Qin Zhan, Guan Zhenyu, Zhang Lei, Zhang Yanting, Xu Yang, Li Ziwei, Meng Lingyu, Zhao Yuhang, Cui Dong, Chu Zhixuan, Shi Guixin, Peng Juntao, Geng Tao, Shao Meng, Guo Jianling, Yuan Kaiguo, Li Xiaojian, Wang Jiakai, Zhao Bin, Fan Chunpeng, Zou Quanchen, Su Ruisheng, Sun Lipeng, Xiao Na, Chen Xing, Ye Xiaohu, Zheng Yanting, Yu Xionghui, Hu Hao, Chen Yanxu, Zhong Yucheng, Yang Shaobo, and Peng Xiaojun.

Statement

The copyright of this Practice Guide belongs to the TC260 Secretariat. No part of the Practice Guide may be copied or translated in any manner without the written authorization of the Secretariat.

When reproducing or citing the views or data in this Practice Guide, please indicate the source as: “Secretariat of the National Technical Committee 260 on Cybersecurity of Standardization Administration of China”.

1 Scope

This document provides security guidance for the deployment and use of agents, covering the stages of assessment, preparation, deployment, use, and decommissioning.

This document applies to the prevention of security risks in the deployment and use of agents, and may also serve as a reference for selecting and using commercial agent services.

2 Normative References

The contents of the following documents constitute indispensable provisions of this document through normative reference in this text. For dated references, only the version corresponding to that date applies to this document. For undated references, the latest version, including all amendments, applies to this document.

GB/T 25069 Information Security Technology Vocabulary

3 Terms and Definitions

The terms and definitions defined in GB/T 25069 and the following apply to this document.

3.1 agent

An intelligent system with capabilities for autonomous perception, memory, decision-making, interaction, and execution.

Note: In this document, “agent” specifically refers to an AI agent based on large models, oriented to personal-assistant scenarios, and requiring the user to grant relatively high privileges. It is generally a software system.

3.2 tools

Standardized interfaces that enable agents to invoke external capabilities, defining the name, input parameters, and return results of an atomic operation.

3.3 skills

A standardized instruction set for specific tasks, encapsulating best practices, operating procedures, and domain knowledge for completing a certain type of task.

4 Abbreviations

API: Application Programming Interface

IP: Internet Protocol

5 Overview

During the deployment and use of agents, users should carry out security protection in accordance with the security guidance in Chapters 6 to 10 of this document, and perform security checks with reference to Appendix A. If security issues are identified during the security check or in the course of use, users should promptly strengthen security according to the relevant chapters of this document. Users shall carry out agent deployment and use activities in compliance with the regulations of the state and of their organizations. To address various security risks that may arise from internal personnel deploying and using agents, relevant organizations should establish corresponding security management systems and supporting security capabilities in accordance with the security management guidance in Appendix B.

6 Assessment Stage

This stage mainly involves assessments prior to agent deployment and use, including the necessity of using agents, the applicability of open-source agents and commercial agents, and whether the proposed agent to be selected meets the baseline security feature requirements.

a) The purpose of use, business scenario, and work task should be clearly defined, and the necessity and reasonableness of using an agent to complete the relevant tasks should be assessed.

b) The user should understand in advance the technical characteristics, capability boundaries, and security risks of agents, as well as the principal differences between open-source agents and commercial agents.

c) Based on the needs analysis in a) and the knowledge preparation in b), the agent to be deployed and used should be selected prudently. Priority should be given to complete solutions in which the provider offers both the agent and supporting security protection capabilities. Open-source projects lacking security protection measures should be selected with caution.

Note: When selecting a commercial agent, the user should carefully read the security precautions issued by the provider and verify its security features against the subsequent chapters of this document. If the requirements are met, it is unnecessary to repeat the subsequent security measures. When selecting an open-source agent for which security protection must be implemented independently, security protection should be strengthened in accordance with the subsequent chapters of this document.

d) The maintenance status of the proposed agent project should be checked. An agent project shall not be selected if any of the following conditions exists:

1. There has been no maintenance record for more than one month, and unresolved security issues exist.

2. Publicly disclosed security issues have gone unanswered for a long period.

3. Unpatched high-severity vulnerabilities exist.

4. The provider has explicitly ceased maintenance.

e) Priority should be given to agents that integrate mechanisms such as secure sandboxes, high-risk operation control, emergency stop control, and traceable file systems. Agents lacking basic security mechanisms such as log auditing and permission management shall not be selected.

f) The proposed agent to be deployed and used should be checked for major security risks such as automatically opening public network interfaces or forcibly returning runtime data.

7 Preparation Stage

This stage mainly concerns preparation for the installation and deployment of the agent, including installation materials, deployment environment, large models, and security protection.

a) When selecting installation materials for the agent:

1. Agent installation files, container images, and other installation materials should be obtained from channels with clearly identified responsible entities and release mechanisms, such as the provider’s official website or application stores. Modified versions, redistributed versions, cracked versions, or other installation materials of unknown origin from network drives, forums, instant-messaging groups, and similar channels shall not be used.

2. Before installing the agent, the authenticity and integrity of installation materials should be verified through the digital signatures, hash values, checksums, or similar methods provided by the releasing entity, in order to prevent poisoned or tampered installation materials.

b) Corresponding security protection measures should be taken according to the installation and deployment method of the agent:

1. Where deployment is to be carried out directly in a local environment, a dedicated device should be chosen for installing the agent, and it should not be mixed with devices used for daily life, work, office work, and similar purposes. Before deployment, the existing files on the device should be backed up. If the device contains sensitive data or private files, such data or files should be cleaned up or migrated in advance.

2. Where deployment is to be carried out in a virtualized environment such as a virtual machine or container, strict isolation should be implemented through configurations such as prohibiting the virtual machine from accessing files on the host machine, so as to prevent security issues from spreading to the host.

3. Where deployment is to be carried out in a cloud environment, a cloud platform with capabilities such as agent identity management, access control, log auditing, and security alerting should be selected. Before deployment, the cloud service provider should be consulted to confirm whether the security capabilities it provides meet the relevant requirements of this document.

c) When selecting the large model required for agent operation:

1. A large model that has completed the filing required for generative AI services should be selected.

2. Where there are relevant requirements for data security and privacy protection, and the necessary computing conditions and technical foundations are available, a locally deployed large model should be given priority.

3. Where an external large-model service is invoked, the official interface of the large-model service provider shall be used. A large model shall not be invoked through relay services of unknown origin or unauthorized agents.

4. A large model whose context window, capability boundaries, and security level meet the requirements should be selected according to the complexity of the agent task and the security needs, so as to avoid agent misoperation caused by insufficient context window length or inadequate security capabilities.

d) According to security needs, a gap analysis should be conducted on the existing security mechanisms of the selected agent and large model. Where the following security capabilities are insufficient, they should be strengthened by deploying security tools, connecting security services, or similar means:

1. Security protection for input and output content.

2. Agent behavior control, such as runtime behavior monitoring and anomaly circuit breaking.

3. Security management of agent identities and credentials.

4. Security inspection of the agent supply chain, such as skills and tools.

5. Interception and management of high-risk operations.

6. Environment isolation based on technologies such as sandboxes.

7. Resource consumption and cost control.

8 Deployment Stage

This chapter sets out security guidance for the deployment stage of the agent, including deployment methods, plugin installation, runtime accounts, permission configuration, network exposure control, log auditing, and management of high-risk operations.

a) Deployment should be carried out according to the official documentation of the agent provider or deployment scripts that have been verified. Convenience scripts such as one-click deployment scripts from unknown sources shall not be used.

b) Where plugins need to be installed additionally, the reliability of the plugin source should be checked before installation. Plugins from unknown sources, with unpatched high-severity vulnerabilities, with abnormal permission requirements, or unrelated to the intended task shall not be installed.

c) The agent shall not be run with operating-system administrator privileges. Only the minimum permissions necessary for the agent to complete the intended task should be granted, so as to reduce the impact range of agent overreach or abuse.

d) The range of directories accessible to the agent should be restricted. The agent shall not be granted default access to important locations such as the user’s home directory or system directories. A dedicated working directory should be established for the agent, and only the files necessary for the task should be placed in that directory.

e) The agent and its related services should be configured to be accessible only from the local machine and not exposed to external networks, in order to prevent unauthorized remote invocation. Where access to the agent through the internet is genuinely required, encrypted access shall be configured and access sources shall be restricted.

f) The logging function of the agent should be enabled. Full logs should be kept for actions such as file operations, instruction execution, network activities, and skill invocation. The logging granularity should be set to the finest level supported.

g) A list of high-risk operations should be established in advance and managed through the agent’s security mechanisms. Operations on the list should be subject to secondary confirmation or direct blocking. High-risk operations include, but are not limited to, stopping or disabling system services, terminating processes, formatting or overwriting disks, bulk deletion, permission modification, key changes, opening ports, modifying firewall rules, modifying system settings, and accessing password managers. According to the purpose of agent use, operations involving transfers, payments, and other acts affecting personal property security should be included in the list of high-risk operations.

9 Use Stage

This chapter sets out security guidance for the use stage of the agent, including security re-check, skill security, sensitive information protection, network access security, long-term memory management, emergency response, and updates.

a) The installation and configuration of the agent should be reviewed, including but not limited to the following:

1. Whether the user can effectively understand the execution status of the agent.

2. Whether the user can carry out security management over the operations executed by the agent, for example by configuring blacklists and whitelists.

3. Whether the user can conveniently trigger emergency stop control of the agent.

b) Security protection for the use of skills should be strengthened, including but not limited to the following:

1. Skills from reliable sources shall be used.

2. Comprehensive security testing of skills should be carried out. Where skills that have not undergone security testing are used, risk precautions should be prepared in advance.

c) When using an agent connected to the internet, attention shall be paid to protecting the security of sensitive data, including but not limited to the following:

1. When providing personal information to the agent, the principle of minimum necessity shall be followed. Sensitive information involving biometric characteristics, family privacy, and the like should be provided with caution.

2. Without third-party authorization, the personal information and sensitive data of third parties shall not be provided to the agent.

3. Business data for which the user has not obtained permission, and content involving intellectual property, shall not be provided to the agent.

d) Where the agent is accessed through the internet, the necessity and security of its public network interfaces should be checked regularly, and non-essential exposed interfaces should be closed in a timely manner.

e) Where the agent is used to obtain online information services or participate in online social-media discussions, the relevant cybersecurity laws and regulations shall be complied with.

f) Valuable data in the environment in which the agent operates should be backed up regularly for disaster recovery.

g) The contents recorded in long-term memory files should be reviewed manually on a regular basis. Personal information, private data, and internal information that should not be stored should be handled in a timely manner, and the long-term memory configuration strategy should be adjusted accordingly.

h) Sensitive permissions should be revoked in a timely manner, unused skills and sensitive conversation records should be cleaned up regularly, and multi-factor authentication should be enabled to protect account security.

i) Alert information from deployed security tools and security services shall be checked and handled in a timely manner. Based on other obtained security threat information, risk alerts, and similar information, the deployment and use of the agent shall be reviewed for security, and security risks shall be removed in a timely manner.

j) Security notices issued by the agent operator and by security companies shall be followed continuously. When a security incident affecting a specific version occurs, corresponding measures such as upgrade, downgrade, or version pinning shall be taken according to the security notice, in order to avoid long-term use of versions with known vulnerabilities or versions that have ceased to be maintained.

10 Decommissioning Stage

This chapter sets out security guidance for the decommissioning stage of the agent, including safely terminating operation, cleaning up data and permissions, and completing environment reclamation.

a) The main program of the agent, as well as all related services and background processes, shall be stopped, and it shall be confirmed that the agent has completely exited its running state.

b) Before cleaning up the environment, conversation records, configuration files, knowledge-base files, logs, and other data that still need to be retained shall be backed up for disaster recovery.

c) After completing the necessary data backup, corresponding environment-cleanup operations shall be performed according to the deployment environment:

1. Where deployed in a local environment, if the agent provider provides an official uninstaller, the official uninstaller should be used for removal, and after removal the relevant processes, ports, network connections, and other conditions should be checked to confirm that no residue remains. If there is no official uninstaller, the operating system should be reset.

2. Where deployed in a cloud environment, public access entry points related to the agent shall be closed, unused working files and data such as the agent’s knowledge bases, logs, long-term memory, plugins, and skill configurations shall be deleted, and related credentials and permissions such as API keys, service-account credentials, and third-party application authorizations shall be revoked at the same time.

3. Where deployed in a virtualized environment, the virtualized environment itself should be decommissioned directly if possible. If that virtualized environment cannot be decommissioned, environment cleanup should be carried out with reference to the relevant guidance in 1).

4. After decommissioning the agent, related services should be confirmed as terminated in a timely manner, subscriptions and auto-renewal should be canceled, and attention should be paid to whether the large-model interface is generating abnormal charges.

Appendix A (Informative) Security Checklist

Table 1 Security Checklist for Deployment and Use

Appendix B (Informative) Security Management Guidance

Where agents are used within an organization, it is recommended that management work be carried out around the following aspects.

a) Establish an internal management regime for agent use, and manage activities such as the deployment, use, and change of agents. The management regime shall include at least the following:

1. Requirements on prohibited behaviors. Specific behaviors prohibited during agent use should be clearly defined, for example, not connecting internal organizational data or system interfaces to agents that have not passed approval.

2. Requirements on usage boundaries. In accordance with the principle of minimum authorization, the scope of use, permission boundaries, and data-processing boundaries of agents should be clearly defined.

3. Requirements on approval procedures. The processes for application, assessment, approval, and filing before agent deployment should be clearly defined. The submitted application content should include the purpose of use, usage boundaries, skills to be configured, tools to be connected, security protection measures, and similar matters.

b) Establish an asset register for agents, carry out unified registration of approved agents, and update the register when changes occur. The asset register shall record at least the following information:

1. Agent information, including the agent name, purpose, and business ownership.

2. Deployment-location information, including host physical location, IP address, container name, or another uniquely identifiable agent identifier.

3. Developer information, including the deployer, deployment time, and responsible person.

4. Model information, including the name, version, and access method of the large model in use.

5. Tool and component information, including the list of installed skills, plugins, and other external tools.

6. Access-control information, including the accessible internal systems, interfaces, and data scope.

7. Authorization information, including permission configuration status.

8. Review-record information, including the time and result of the most recent security review.

c) Manage the activities of approved agents:

1. Keep logs of key activities, including execution of high-privilege commands, access to sensitive data, access to internal systems, transmission of external data, permission changes, tool calls, and abnormal operations.

2. Use artificial intelligence, rule analysis, or other technical means to conduct risk analysis of agent behavior patterns.

3. Conduct periodic analysis and review of logs to identify and handle security issues in a timely manner, and form records.

d) The ability to discover unapproved agents should be established through the following means, so that further handling such as network isolation, permission downgrading, and process blocking can be carried out:

1. Regularly scan typical agent service ports within the organizational intranet.

2. Analyze network-traffic logs to identify abnormal agent communication behavior.

3. Identify internal hosts communicating with known large-model API endpoints.

4. Search endpoints for processes related to the installation or operation of agents.

e) Conduct security education for employees within the organization to improve their awareness of agent security risks and secure use. Security education shall cover prompt-injection attacks, supply-chain security, credential leakage, data leakage, unauthorized access, liability for improper use, and similar topics.

8
4
Share
Previous