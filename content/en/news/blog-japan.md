---
hide:
  - toc
---
# AWS Japan Tech Blog — Networking

Networking-related posts from the [AWS Japan Tech Blog](https://aws.amazon.com/jp/blogs/news/) (Japanese), summarized weekly (every Friday) with a focus on recent articles. Follow each link for the original article. Most recent items appear first.

<!-- NEWS:INSERT -->

## 2026-10-29 · Weekly summary

- **[Securing MCP Endpoints at the Edge with Amazon CloudFront and AWS WAF](https://aws.amazon.com/jp/blogs/news/protect-mcp-endpoints-at-the-edge-with-amazon-cloudfront-and-aws-waf/)** — With MCP redesigned as a stateless HTTP request/response protocol, Layer 7 inspection, transformation, and optimization via AWS WAF can now be applied to MCP endpoints deployed behind Amazon CloudFront or an ALB—without any server-side code changes. This post walks through nine practical security and observability use cases enabled by the updated MCP specification.

## 2026-10-27 · Weekly summary

- **[Achieve Predictable Costs with AWS Direct Connect Flat-Rate Pricing](https://aws.amazon.com/jp/blogs/news/powering-predictable-costs-with-aws-direct-connect-flat-rate-pricing/)** — AWS Direct Connect now offers a flat-rate pricing option, allowing customers to use dedicated network connections at a fixed cost regardless of data transfer volume. This makes networking costs more predictable for workloads with variable traffic patterns.

## 2026-10-20 · Weekly summary

- **[Threat Breakdown: How Subdomain Takeover Works and How to Defend Against It](https://aws.amazon.com/jp/blogs/news/threat-tactic-spotlight-subdomain-takeover/)** — This post explains how attackers exploit dangling DNS records to redirect traffic to attacker-controlled resources, covering targets such as S3, CloudFront, and Elastic Beanstalk. It introduces proactive detection via AWS Config custom rules, a standard procedure to delete DNS records first, and notification and remediation using Security Hub and SNS.
- **[Real-Time Malware Defense: Leveraging AWS Network Firewall Active Threat Defense](https://aws.amazon.com/jp/blogs/news/real-time-malware-defense-leveraging-aws-network-firewall-active-threat-defense/)** — AWS Network Firewall's Active Threat Defense uses threat intelligence from Amazon's MadPot honeypot network to automatically deploy protection rules within 30 minutes. It blocks attacks across DNS, HTTP, TLS SNI, and IP layers using a layered defense model, and integrates with Amazon GuardDuty—including a real-world case blocking a CVE-2025-48703 exploit deploying the Mythic C2 framework.
- **[Preventing Data Exfiltration: Egress Controls for Cloud Workloads on AWS](https://aws.amazon.com/jp/blogs/news/prevent-data-exfiltration-aws-egress-controls-for-cloud-workloads/)** — To prevent data exfiltration via outbound traffic, this post demonstrates a layered egress control approach built on a hub-and-spoke architecture, combining AWS Network Firewall and Amazon Route 53 Resolver DNS Firewall for preventive controls. It also covers data perimeters using SCPs, RCPs, and VPC endpoint policies, detective controls via Amazon GuardDuty and AWS Security Hub, and applicability to agentic AI workloads.
- **[Secure Network Architecture for Generative AI Applications Built with AWS Services](https://aws.amazon.com/jp/blogs/news/build-secure-network-architectures-for-generative-ai-applications-using-aws-services/)** — This post presents a defense-in-depth reference architecture for generative AI applications, combining private connectivity to Amazon Bedrock via AWS PrivateLink, edge protection with AWS WAF and AWS Shield, perimeter defense using AWS Network Firewall, and monitoring through Amazon GuardDuty to address threats such as DDoS attacks, SQL injection, and malicious bots.

## 2026-10-19 · Weekly summary

- **[Implementing Least-Privilege Access in Amazon Bedrock](https://aws.amazon.com/jp/blogs/news/implementing-least-privilege-access-for-amazon-bedrock/)** — This article explains how to apply the principle of least privilege across the model selection, adaptation, testing, and production phases of generative AI applications built on Amazon Bedrock. It covers policy examples using SCPs, VPC endpoint policies, KMS key policies, Amazon Bedrock Guardrails, and Amazon Bedrock Agents, along with periodic permission reviews via IAM Access Analyzer.

## 2026-10-17 · Weekly summary

- **[Detecting Multi-Stage Attacks on AWS: A Guide to Cross-Service Signal Correlation](https://aws.amazon.com/jp/blogs/news/detecting-multi-stage-attacks-on-aws-a-guide-to-cross-service-signal-correlation/)** — This guide explains how to layer business context—such as data classification, access patterns, and resource ownership—on top of Amazon GuardDuty's enhanced threat detection to reveal the full picture of multi-stage attacks. It covers four correlation patterns using CloudTrail, VPC Flow Logs, and Route 53 Resolver query logs in CloudWatch Logs Insights, along with automation via Lambda, Amazon SNS, and EventBridge Scheduler.
- **[Accelerating SAP Network Troubleshooting from Hours to Minutes: An Agentic AI Approach](https://aws.amazon.com/jp/blogs/news/accelerate-sap-network-troubleshooting-from-hours-to-minutes-agentic-ai-approach/)** — This post demonstrates how combining Kiro-CLI with AWS MCP Servers enables an agentic AI approach that reduces complex SAP network troubleshooting from hours to minutes. Five real-world scenarios—including cross-AZ latency analysis, 504 error root-cause analysis, security group drift detection, and capacity forecasting—are covered using VPC Flow Logs, security groups, and Transit Gateway diagnostics via natural-language prompts.

## 2026-10-16 · Weekly summary

- **[Extending Data Perimeters to the AWS Management Console with Private Access](https://aws.amazon.com/jp/blogs/news/extend-your-data-perimeter-to-the-aws-management-console-with-private-access/)** — AWS Management Console private access is now generally available, supporting VPCs without internet connectivity by routing all console traffic—including authentication flows, static assets, and console-specific APIs—through AWS PrivateLink VPC endpoints. Combining VPC endpoint policies with Resource Control Policies (RCPs) enables organizations to enforce a stronger data perimeter.

## 2026-10-15 · Weekly summary

- **[AWS STS Session Token Size Limit Simplified with Monitoring Support](https://aws.amazon.com/jp/blogs/news/aws-sts-simplifies-session-token-size-limits-and-adds-session-token-size-monitoring/)** — AWS STS session token size limits have been consolidated into a single 4,096-byte limit, expanding the capacity available for session policies and session tags. Token sizes are now reported via API responses, Amazon CloudWatch metrics, and AWS CloudTrail events, and the MinimumSessionTokenSize parameter can be used to validate the maximum token size that infrastructure components such as load balancers and databases can handle.

## 2026-10-14 · Weekly summary

- **[Amazon GuardDuty Extended Threat Detection Adds Five New Indicators to Enhance Attack Sequence Detection](https://aws.amazon.com/jp/blogs/news/guardduty-extended-threat-detection-has-added-five-new-indicators-to-surface-attack-sequences/)** — Amazon GuardDuty's extended threat detection now includes five new indicators sourced from Amazon Inspector, Amazon VPC Reachability Analyzer, Amazon Macie, and AWS Security Hub, correlating vulnerability, reachability, misconfiguration, and sensitive data signals with weak runtime findings. This consolidates low-level noise into CRITICAL-severity, actionable attack sequence findings to streamline incident response.

## 2026-10-06 · Weekly summary

- **[Weekly AWS – Week of September 28, 2026](https://aws.amazon.com/jp/blogs/news/aws-weekly-20260928/)** — This week's AWS updates include the GA of Palo Alto Networks Advanced DNS Security in Amazon Route 53 Resolver DNS Firewall, logical air-gap vault support for Amazon FSx for NetApp ONTAP in AWS Backup, and direct Apache Iceberg/Parquet querying from Aurora PostgreSQL. From a networking perspective, the enhanced DNS security integration and expanded multi-Region support for AWS IAM Identity Center are particularly noteworthy.

## 2026-09-25 · Weekly summary

- **[Weekly AWS – Week of September 14, 2026](https://aws.amazon.com/jp/blogs/news/aws-weekly-20260914/)** — This week's AWS updates include AWS Direct Connect flat-rate pricing for dedicated connections, the launch of AWS PrivateLink Tunnel Endpoint, and source IP preservation support for SFTP servers behind a Network Load Balancer in AWS Transfer Family. Additional highlights cover a new AgentCore Runtime in Amazon Bedrock AgentCore, expanded Amazon S3 Files support for Amazon ECS on EC2, and several Amazon Connect enhancements.

## 2026-09-24 · Weekly summary

- **[Implementing mTLS Authentication for SAP S/4HANA with Amazon CloudFront](https://aws.amazon.com/jp/blogs/news/implement-mtls-authentication-with-amazon-cloudfront-for-sap-s-4hana/)** — This post explains an architecture that uses Amazon CloudFront's mTLS verify mode to validate client certificates at the edge, combined with ALB passthrough and SAP ICM X.509 authentication to achieve passwordless SSO. Internal testing showed the approach reduces initial login time by approximately 40–50% by minimizing global TLS handshake latency.

## 2026-09-19 · Weekly summary

- **[Integrating SAP Commerce Cloud with SAP Cloud ERP Private on AWS – A Practical, Proven Approach](https://aws.amazon.com/jp/blogs/news/integrating-sap-commerce-cloud-with-sap-cloud-erp-private-on-aws-a-practical-and-proven-approach/)** — With the end of mainstream maintenance for SAP Commerce (SAP Hybris) 2205 approaching, this post outlines proven architectural best practices for integrating SAP Commerce Cloud SaaS with SAP Cloud ERP Private on AWS. It covers four key areas—Region selection, latency optimization using Amazon CloudFront, AWS Global Accelerator, and Amazon Route 53, and security—along with e-commerce expansion through Buy with Prime and Amazon MCF integration.

## 2026-09-15 · Weekly summary

- **[Introduction to Automated Reasoning](https://aws.amazon.com/jp/blogs/news/a-gentle-introduction-to-automated-reasoning/)** — This article explains automated reasoning in an accessible way using simple C and Python examples, covering why it can verify in milliseconds what exhaustive testing would take over 1,300 years, and why a 'Don't know' answer is unavoidable due to the halting problem. It also highlights AWS use cases such as IAM Access Analyzer and VPC Reachability Analyzer.

## 2026-09-13 · Weekly summary

- **[Event-Driven Pipeline Orchestration with Amazon MWAA and Airflow 3.0](https://aws.amazon.com/jp/blogs/news/event-driven-pipeline-orchestration-with-amazon-mwaa-and-airflow-3-0/)** — This post explains how to combine Apache Airflow 3.0's Asset Watcher with Amazon SQS to achieve event-driven orchestration across multiple Amazon MWAA environments and AWS accounts. Replacing polling-based sensors with event-driven triggers reduces inter-environment orchestration latency from minutes to seconds, with best practices covering cross-account IAM and Amazon VPC networking.

## 2026-08-29 · Weekly summary

- **[Analyzing Application Load Balancer Logs with Amazon CloudWatch Logs](https://aws.amazon.com/jp/blogs/news/analyze-application-load-balancer-logs-with-amazon-cloudwatch-logs/)** — Amazon CloudWatch Logs now supports ALB access logs, connection logs, and health check logs as Vended Logs, delivering them directly as structured JSON. This enables per-request, per-connection, and per-target observability with dashboards, Log Analytics, alarms, and Contributor Insights for streamlined troubleshooting.

## 2026-08-25 · Weekly summary

- **[Weekly AWS – Week of August 17, 2026](https://aws.amazon.com/jp/blogs/news/aws-weekly-20260817/)** — AWS Direct Connect announced inbound prefix control and expansion to up to 1,000 routes per VIF, marking a notable networking update this week, alongside broader improvements such as a visual file editor in AWS CloudShell, increased Amazon ECR replication rule limits, and AWS Glue 6.0 GA with a 30% price reduction.

## 2026-08-21 · Weekly summary

- **[Natural Language Queries with Oracle Database 26ai: Getting Started with Select AI on Amazon RDS for Oracle Using Amazon Bedrock](https://aws.amazon.com/jp/blogs/news/natural-language-queries-on-oracle-database-26ai-getting-started-with-select-ai-on-amazon-rds-for-oracle-with-amazon-bedrock/)** — Oracle Database 26ai is now available on Amazon RDS for Oracle, enabling Select AI to query relational data using natural language via Amazon Bedrock foundation models. The post covers the end-to-end setup, from configuring VPC interface endpoints and IAM credentials to creating DBMS_CLOUD_AI profiles and running natural language queries.
