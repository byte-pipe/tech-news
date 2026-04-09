---
title: "From Permanent Access to Just-in-Time: A Startup's IAM Journey Part 1 - DEV Community"
url: https://dev.to/ccscaesar/from-permanent-access-to-just-in-time-a-startups-iam-journey-part-1-4lbn
date: 2025-10-10
site: devto
model: llama3.2:1b
summarized_at: 2025-10-12T11:11:41.063549
screenshot: devto-from-permanent-access-to-just-in-time-a-startup-s.png
---

# From Permanent Access to Just-in-Time: A Startup's IAM Journey Part 1 - DEV Community

**Implementing Just-In-Time (JIT) IAM inAWS**
=====================================

This post delves into the challenges of managing cloud access and security in rapidly growing FinTech startups. A journey to revamp the IAM strategy was undertaken to address perceived risk factors, including:

* Security issues such as single-factor authentication with limited MFA enforcement, permanent "always-on" access paths, overly permissive roles, lack of separation of duties, and no just-in-time (JIT) access management.

A modern approach to identifying and addressing these concerns involves the use of tools specifically designed for cloud-native environments. This includes AWS IAM Identity Center, AWS IAM Access Analyzer, Entra ID Privileged Identity Management (PIM), and Entra ID Conditional Access.

In this second part of a 3-part series, the focus shifts from defining the problem and implementing the foundational steps to detailing the implementation phase in more detail. Here is an outline for how the "Just-in-Time" IAM strategy was implemented:

### Implementation Phase Overview

The key stages involved are:
- Setting clear end goals
- Enacting risk-based multi-factor authentication (MFA)
- Implementing a principle of least privilege for all IAM roles
- Establishing a strict separation of duties between users and teams.

**Detailed Steps**

### Prioritization and Planning

*   Conduct thorough assessments to identify the scope of risk from single-factor MFA, permanent access paths, and lack of role granularity.
*   Clearly define the security requirements in line with industry standards and compliance.

### Security Architecture Updates

A modern IAM architecture was implemented using AWS IAM Identity Center for multi-factor authentication. Additionally, roles and trust policies were analyzed to ensure they meet the desired criteria.

AWS IAM Access Analyzer is utilized to identify weaknesses in access policies and provide recommendations for improvement. PIM tool helps enforce role based MFA, ensuring compliance with regulatory standards.

Lastly, Entra ID Conditional Access is invoked for all tasks requiring privileged identities, further enhancing security postures.

### Review and Remediation

-   Regularly review IAM configuration and ensure it reflects the defined security architecture.
-   Address concerns about potential access to sensitive resources, implement fine-grained access controls in accordance with role-based access control (RBAC).

With a focus on Just-In-Time (JIT) IAM strategy implemented, FinTech companies can minimize exposure risks and protect their cloud environments. By carefully defining the security requirements for risk management and continuously monitoring compliance posture, organizations can ensure protection of financial data.

In subsequent parts, a more detailed walkthrough of how IAM is managed through this approach will be provided, emphasizing steps such as continuous auditing and threat management.

## Additional Support
Additional support for FinTech businesses looking to enhance their cloud infrastructure security includes:
-   Professional guidance from experts across various cloud-based services.
-   Customizable solutions that cater to diverse security requirements and industry standards.
