---
hide:
  - toc
---
# AWS What's New — Networking

Networking-related items from [AWS What's New](https://aws.amazon.com/new/), automatically summarized every weekday morning. Follow each link for the original announcement. Most recent items appear first.

<!-- NEWS:INSERT -->

## 2026-07-01 · Daily update

- **[AWS CloudFormation and CDK Express Mode Speeds Up Infrastructure Deployments by Up to 4x](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-cloudformation-cdk/)** — AWS CloudFormation and CDK express mode cuts deployment time by up to 4x by completing stack operations as soon as resource configuration is applied, skipping extended stabilization checks such as traffic readiness and region propagation. This enables faster iteration cycles for developers and AI agents building infrastructure in development environments.
- **[AWS Parallel Computing Service Supports In-Place Slurm Major Version Upgrades](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-parallel-computing-service-upgrade/)** — AWS Parallel Computing Service (PCS) now supports managed in-place Slurm major version upgrades, allowing clusters to advance up to three major versions without disrupting running jobs. PCS handles the upgrade of all managed Slurm components—controller, accounting database, and REST API—while queued jobs resume automatically once the operation completes.
- **[Announcing Capability Insights for AWS, an Open-Source Solution for Regional Capabilities](https://aws.amazon.com/about-aws/whats-new/2026/06/capability-insights-aws/)** — AWS has launched Capability Insights, an open-source self-hosted dashboard that lets organizations deploy regional capabilities data inside their own Amazon VPC. The solution is designed for teams with data residency requirements, compliance reporting needs, or multi-Region expansion and recovery planning.
- **[AWS Security Hub CSPM Launches AI Security Best Practices Standard with 31 Automated Controls](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-security-hub-cspm-ai-security/)** — AWS Security Hub CSPM has introduced the AI Security Best Practices standard, comprising 31 automated controls that continuously evaluate Amazon Bedrock, Amazon Bedrock AgentCore, and Amazon SageMaker workloads against recommended security configurations. The standard covers critical domains including network isolation and encryption, eliminating the need for manual assessments or custom rule authoring.

## 2026-06-30 · Daily update

- **[Amazon MWAA Serverless Now Supports Shared VPC Configurations](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-mwaa-serverless-vpc/)** — Amazon MWAA Serverless now supports VPC subnets shared via AWS RAM, resolving a validation error that previously blocked workflow creation in shared VPC setups. This enables organizations using centralized networking in multi-account landing zone architectures to deploy MWAA Serverless workflows on shared subnets, consistent with MWAA Provisioned environments.

## 2026-06-23 · Daily update

- **[AWS Network Firewall updates default drop action for improved connection reliability](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-network-firewall-updates-default-drop-action)** — The default stateful action for new AWS Network Firewall policies changed from "Application drop established" in both directions to server-direction only. This resolves the previous default's behavior of automatically blocking legitimate server-to-client TCP traffic, improving connection reliability.
