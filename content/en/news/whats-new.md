---
hide:
  - toc
---
# AWS What's New — Networking

Networking-related items from [AWS What's New](https://aws.amazon.com/new/), automatically summarized every weekday morning. Follow each link for the original announcement. Most recent items appear first.

<!-- NEWS:INSERT -->

## 2026-06-30 · Daily update

- **[Amazon MWAA Serverless Now Supports Shared VPC Configurations](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-mwaa-serverless-vpc/)** — Amazon MWAA Serverless now supports VPC subnets shared via AWS RAM, resolving a validation error that previously blocked workflow creation in shared VPC setups. This enables organizations using centralized networking in multi-account landing zone architectures to deploy MWAA Serverless workflows on shared subnets, consistent with MWAA Provisioned environments.

## 2026-06-23 · Daily update

- **[AWS Network Firewall updates default drop action for improved connection reliability](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-network-firewall-updates-default-drop-action)** — The default stateful action for new AWS Network Firewall policies changed from "Application drop established" in both directions to server-direction only. This resolves the previous default's behavior of automatically blocking legitimate server-to-client TCP traffic, improving connection reliability.
