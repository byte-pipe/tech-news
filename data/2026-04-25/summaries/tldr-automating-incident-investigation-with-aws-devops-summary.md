---
title: Automating Incident Investigation with AWS DevOps Agent and Salesforce MCP Server | AWS DevOps & Developer Productivity Blog
url: https://aws.amazon.com/blogs/devops/automating-incident-investigation-with-aws-devops-agent-and-salesforce-mcp-server/
date: 2026-04-25
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-04-25T08:22:18.271204
---

# Automating Incident Investigation with AWS DevOps Agent and Salesforce MCP Server | AWS DevOps & Developer Productivity Blog

# Automating Incident Investigation with AWS DevOps Agent and Salesforce MCP Server

## Overview
- AWS DevOps Agent automates incident investigation, cutting mean time to resolution (MTTR) from hours to minutes.  
- Integration with Salesforce Hosted MCP Server links support cases directly to infrastructure diagnostics, providing rapid, consistent resolution.

## The Challenge: Manual Incident Investigation
- Customer reports (e.g., “website is slow”) trigger lengthy investigations across fragmented telemetry and multiple teams.  
- Problems caused by manual handoffs:
  - Increased mean time to detect (MTTD) as issues wait for the right expert.  
  - Extended MTTR due to manual checks in CloudWatch, CloudTrail, logs, and deployment history.  
  - Loss of context between support tickets and technical analysis.  
  - Reactive focus on symptoms rather than prevention.

## Automated Workflow – From Complaint to Diagnosis
1. **Case Creation** – Customer submits a case in Agentforce Service.  
2. **Trigger** – Salesforce Flow detects the new case and calls the AWS DevOps Agent via API/webhook.  
3. **Autonomous Investigation** – Agent queries AWS observability services, third‑party tools (Splunk, Datadog), code repositories, and CI/CD pipelines; builds a dynamic topology graph of resources.  
4. **Case Enrichment** – Findings are posted back to the Salesforce case, giving support staff technical context and root‑cause analysis.  
5. **Preventative Recommendations** – Agent suggests architectural improvements to avoid recurrence.

## Real‑World Example: Single Instance Outage
- **Incident**: Customer reports an unavailable application via Agentforce Service.  
- **Investigation Steps**:
  - Retrieve case details using Salesforce SOQL query.  
  - Discover topology and map all application components.  
  - Analyze CloudWatch metrics; detect request count dropping to zero.  
  - Examine CloudTrail events; identify administrative actions leading to downtime.  
  - Correlate actions with metrics to determine that an EC2 instance termination caused the outage.  
  - Update the Salesforce case with a detailed root‑cause analysis and timeline.  
- **Result**: Case contains comprehensive diagnostics, affected resources, and contributing factors.  
- **Mitigation Plan**: Agent generates actionable steps and architectural recommendations to prevent future occurrences.

## Technical Implementation

### Prerequisites
- Agentforce Service with Salesforce Hosted MCP Server enabled.  
- AWS DevOps Agent Space configured in the AWS account.  
- Amazon CloudWatch and AWS CloudTrail enabled.  
- (Optional) Infrastructure resources tagged for topology mapping.  
- Familiarity with Salesforce Flow Builder.

### Setup Overview
1. **Create Agent Space** – Define AWS accounts, integrations, and IAM permissions; add a skill that instructs the agent to update Salesforce cases.  
2. **Integrate Observability Tools** – Connect Splunk, Datadog, New Relic, etc., to supply telemetry data.  
3. **Connect Code Repositories** – Link GitHub, GitLab, or AWS CodeCommit for deployment correlation.  
4. **Build Topology Mapping** – Tag resources to focus the agent on relevant components.  
5. **Add Skills** – Configure investigation instructions, including case updates.

### Salesforce Hosted MCP Server Configuration
- Enable External MCP Service in the Salesforce org.  
- Register AWS DevOps Agent as an OAuth client with the callback URL `https://api.prod.cp.aidevops.us-east-1.api.aws/v1/register/mcpserver/callback`.  
- Enable required OAuth scopes.  
- Add the MCP endpoint (e.g., sandbox URL `https://api.salesforce.com/platform/mcp/v1-beta.2/sandbox/sobject-all`) to the Agent Space in the AWS console.  

## Benefits
- Eliminates manual handoffs between support and DevOps teams.  
- Reduces MTTD and MTTR dramatically.  
- Preserves context by automatically enriching support cases with technical findings.  
- Provides proactive recommendations to improve system resilience.