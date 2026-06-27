---
title: Run isolated sandboxes with full lifecycle control: AWS Lambda introduces MicroVMs | AWS News Blog
url: https://aws.amazon.com/blogs/aws/run-isolated-sandboxes-with-full-lifecycle-control-aws-lambda-introduces-microvms/
date: 2026-06-23
site: hnrss
model: llama3.2:1b
summarized_at: 2026-06-27T11:37:37.714162
---

# Run isolated sandboxes with full lifecycle control: AWS Lambda introduces MicroVMs | AWS News Blog

## AWS Lambda MicroVMs: A New Serverless Compute Primitive

AWS Lambda MicroVMs are a new serverless compute primitive introduced by AWS lambda, offering isolated execution environments with full lifecycle control at the virtual machine level.

### Key Features and Benefits

*   **Stateful Execution Environments**: Isolated, stateful execution environments can be created for users or applications.
*   **Near-instant Launch and Resume**: Code generated from users or AI can be launched quickly and resumes seamlessly.
*   **Direct Control over Environment Lifecycle and State**: Full lifecycle control is provided without managing infrastructure or complex virtualization technologies.
*   **Firecracker-based Virtualization Technology**

### Use Cases and Applicability

Lambda MicroVMs are designed for multi-tenant applications that require dedicated execution environments, such as:

*   AI coding assistants
*   Interactive code environments
*   Data analytics platforms
*   Vulnerability scanners
*   Game servers running user-supplied scripts

Building capability today involves making tradeoffs between performance and isolation or investing time and resources in custom virtualization infrastructure.

### Integration with AWS Lambda Functions

Lambda MicroVMs inherit the operational maturity of existing AWS lambda functions, leveraging Firecracker technology for seamless execution environments.