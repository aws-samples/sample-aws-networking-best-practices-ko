---
hide:
  - toc
---
# AWS What's New — Networking

Networking-related items from [AWS What's New](https://aws.amazon.com/new/), automatically summarized every weekday morning. Follow each link for the original announcement. Most recent items appear first.

<!-- NEWS:INSERT -->

## 2026-07-03 · Daily update

- **[AWS Config Now Supports 8 New Resource Types](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-config-new-resource-types)** — AWS Config expands its coverage with 8 additional resource types across Amazon API Gateway, Amazon EC2, and Amazon S3 Vectors, enabling broader discovery, assessment, auditing, and remediation. Environments with all-resource-type recording enabled will automatically track these new additions, which are also available in Config rules and Config aggregators.

## 2026-07-02 · Daily update

- **[ECS Service Connect Now Supports Zone-Aware Routing](https://aws.amazon.com/about-aws/whats-new/2026/07/ecs-service-connect-zone-aware/)** — Amazon ECS Service Connect now supports zone-aware routing, automatically prioritizing service-to-service traffic within the same AZ to reduce cross-AZ data transfer costs and latency. Traffic weights are dynamically adjusted as endpoints scale to maintain balanced load across target services.
- **[Amazon ECS Express Mode Now Supports Custom Task Definitions](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ecs-express-mode-custom-task-def/)** — Amazon ECS Express Mode now supports custom task definitions, allowing teams to reuse existing task definitions from CI/CD pipelines and IaC workflows within Express Mode's simplified deployment experience. This enables organizations to retain established operational practices while benefiting from Express Mode's streamlined infrastructure automation.
- **[AWS Network Firewall Now Supports Container Attribute-Based Inspection for Amazon EKS and Amazon ECS](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-network-firewall-container-attributes-referencing)** — AWS Network Firewall now supports container attribute-based rules, enabling firewall policies to be written using native constructs such as Namespace, Cluster Name, and Labels for Amazon EKS, and Cluster Name and Container Instance Attributes for Amazon ECS. This eliminates the need to manage complex IP-based rules that break when pods scale or restart, simplifying security for containerized workloads.
- **[AWS Announces AWS Interconnect - Last Mile New Partner with AT&T in Gated Preview](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-announces-AWS-interconnect-last-mile-ATT-gated-preview/)** — AWS has launched AWS Interconnect - last mile in gated preview with AT&T, a fully managed connectivity offering that lets customers connect branch offices, data centers, and remote locations to AWS with just a few clicks. Customers can instantly establish private, high-speed connections by selecting their preferred AWS Region, bandwidth, and Direct Connect Gateway, eliminating the complexity of traditional network setup.

## 2026-07-01 · Daily update

- **[AWS CloudFormation and CDK Express Mode Speeds Up Infrastructure Deployments by Up to 4x](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-cloudformation-cdk/)** — AWS CloudFormation and CDK express mode cuts deployment time by up to 4x by completing stack operations as soon as resource configuration is applied, skipping extended stabilization checks such as traffic readiness and region propagation. This enables faster iteration cycles for developers and AI agents building infrastructure in development environments.
- **[AWS Parallel Computing Service Supports In-Place Slurm Major Version Upgrades](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-parallel-computing-service-upgrade/)** — AWS Parallel Computing Service (PCS) now supports managed in-place Slurm major version upgrades, allowing clusters to advance up to three major versions without disrupting running jobs. PCS handles the upgrade of all managed Slurm components—controller, accounting database, and REST API—while queued jobs resume automatically once the operation completes.
- **[Announcing Capability Insights for AWS, an Open-Source Solution for Regional Capabilities](https://aws.amazon.com/about-aws/whats-new/2026/06/capability-insights-aws/)** — AWS has launched Capability Insights, an open-source self-hosted dashboard that lets organizations deploy regional capabilities data inside their own Amazon VPC. The solution is designed for teams with data residency requirements, compliance reporting needs, or multi-Region expansion and recovery planning.
- **[AWS Security Hub CSPM Launches AI Security Best Practices Standard with 31 Automated Controls](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-security-hub-cspm-ai-security/)** — AWS Security Hub CSPM has introduced the AI Security Best Practices standard, comprising 31 automated controls that continuously evaluate Amazon Bedrock, Amazon Bedrock AgentCore, and Amazon SageMaker workloads against recommended security configurations. The standard covers critical domains including network isolation and encryption, eliminating the need for manual assessments or custom rule authoring.

## 2026-06-30 · Daily update

- **[Amazon MWAA Serverless Now Supports Shared VPC Configurations](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-mwaa-serverless-vpc/)** — Amazon MWAA Serverless now supports VPC subnets shared via AWS RAM, resolving a validation error that previously blocked workflow creation in shared VPC setups. This enables organizations using centralized networking in multi-account landing zone architectures to deploy MWAA Serverless workflows on shared subnets, consistent with MWAA Provisioned environments.

## 2026-06-23 · Daily update

- **[AWS Network Firewall updates default drop action for improved connection reliability](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-network-firewall-updates-default-drop-action)** — The default stateful action for new AWS Network Firewall policies changed from "Application drop established" in both directions to server-direction only. This resolves the previous default's behavior of automatically blocking legitimate server-to-client TCP traffic, improving connection reliability.
