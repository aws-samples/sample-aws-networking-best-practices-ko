---
hide:
  - toc
---
# AWS Japan 기술 블로그 — 네트워킹

[AWS Japan 기술 블로그](https://aws.amazon.com/jp/blogs/news/)(일본어)의 네트워킹 관련 글을 **매주 금요일** 최근 올라온 신규 글 위주로 요약합니다. 원문은 각 항목의 링크에서 확인하세요. 최신 항목이 맨 위에 표시됩니다.

<!-- NEWS:INSERT -->

## 2026-10-29 · 주간 요약

- **[Amazon CloudFront와 AWS WAF로 엣지에서 MCP 엔드포인트 보호하기](https://aws.amazon.com/jp/blogs/news/protect-mcp-endpoints-at-the-edge-with-amazon-cloudfront-and-aws-waf/)** — MCP가 스테이트리스 HTTP 요청/응답 프로토콜로 재설계됨에 따라, Amazon CloudFront 또는 ALB 뒤에 배포된 MCP 엔드포인트에 AWS WAF의 레이어 7 검사·변환·최적화를 서버 코드 변경 없이 적용할 수 있게 되었습니다. 본 글에서는 새 MCP 사양을 활용한 9가지 보안 및 관측성 유스케이스를 소개합니다.

## 2026-10-27 · 주간 요약

- **[AWS Direct Connect 정액 요금으로 예측 가능한 비용 실현](https://aws.amazon.com/jp/blogs/news/powering-predictable-costs-with-aws-direct-connect-flat-rate-pricing/)** — AWS Direct Connect에 정액 요금 옵션이 도입되어, 데이터 전송량에 관계없이 고정 비용으로 전용 네트워크 연결을 사용할 수 있게 되었습니다. 이를 통해 트래픽 변동이 큰 워크로드에서도 네트워킹 비용을 예측 가능하게 관리할 수 있습니다.

## 2026-10-20 · 주간 요약

- **[위협 수법 해설: 서브도메인 탈취의 작동 원리와 대응 방법](https://aws.amazon.com/jp/blogs/news/threat-tactic-spotlight-subdomain-takeover/)** — 댕글링 DNS 레코드를 악용한 서브도메인 탈취 공격의 원리를 설명하고, S3·CloudFront·Elastic Beanstalk 등 탈취 대상이 될 수 있는 리소스를 정리합니다. AWS Config 커스텀 규칙을 통한 사전 탐지, DNS 레코드 선삭제 표준 절차, Security Hub 및 SNS를 활용한 알림·수정 방법을 소개합니다.
- **[실시간 멀웨어 방어: AWS Network Firewall의 능동적 위협 방어 활용](https://aws.amazon.com/jp/blogs/news/real-time-malware-defense-leveraging-aws-network-firewall-active-threat-defense/)** — AWS Network Firewall의 능동적 위협 방어 기능은 Amazon의 허니팟 네트워크 MadPot의 위협 인텔리전스를 활용해 30분 이내에 보호 규칙을 자동 배포합니다. DNS·HTTP·TLS SNI·IP 계층에 걸친 다층 방어로 공격 킬체인 각 단계를 차단하며, Amazon GuardDuty 연동 및 실제 CVE-2025-48703 공격 차단 사례도 소개합니다.
- **[데이터 유출 방지: AWS로 구현하는 클라우드 워크로드의 이그레스 제어](https://aws.amazon.com/jp/blogs/news/prevent-data-exfiltration-aws-egress-controls-for-cloud-workloads/)** — 아웃바운드 트래픽을 악용한 데이터 유출을 막기 위해 허브 앤 스포크 아키텍처를 기반으로 AWS Network Firewall과 Amazon Route 53 Resolver DNS Firewall을 조합한 다층적 이그레스 제어 구현 방법을 소개합니다. SCP·RCP·VPC 엔드포인트 정책을 통한 데이터 경계 설정과 Amazon GuardDuty·AWS Security Hub를 활용한 탐지 제어를 결합하며, 에이전틱 AI 워크로드에도 적용 가능함을 설명합니다.
- **[AWS 서비스로 구축하는 생성형 AI 애플리케이션의 보안 네트워크 아키텍처](https://aws.amazon.com/jp/blogs/news/build-secure-network-architectures-for-generative-ai-applications-using-aws-services/)** — 생성형 AI 애플리케이션을 DDoS 공격·SQL 인젝션·악성 봇 등 외부 위협으로부터 보호하기 위해, AWS PrivateLink를 통한 Amazon Bedrock 프라이빗 연결, AWS WAF·AWS Shield의 엣지 보호, AWS Network Firewall의 경계 방어, Amazon GuardDuty 모니터링을 결합한 다층 방어 참조 아키텍처를 소개합니다.

## 2026-10-19 · 주간 요약

- **[Amazon Bedrock에서 최소 권한 액세스 구현](https://aws.amazon.com/jp/blogs/news/implementing-least-privilege-access-for-amazon-bedrock/)** — 생성형 AI 애플리케이션에서 Amazon Bedrock의 모델 선택·적응·테스트·운영 각 단계에 최소 권한 원칙을 적용하는 방법을 소개합니다. SCP, VPC 엔드포인트 정책, KMS 키 정책, Amazon Bedrock Guardrails, Amazon Bedrock Agents를 활용한 정책 예시와 함께 IAM Access Analyzer를 통한 권한 정기 검토 방법도 다룹니다.

## 2026-10-17 · 주간 요약

- **[AWS에서 다단계 공격 탐지: 서비스 간 시그널 상관 분석 가이드](https://aws.amazon.com/jp/blogs/news/detecting-multi-stage-attacks-on-aws-a-guide-to-cross-service-signal-correlation/)** — Amazon GuardDuty 확장 위협 탐지에 데이터 분류, 액세스 패턴, 리소스 소유 관계 등 비즈니스 컨텍스트를 결합하여 다단계 공격의 전체 흐름을 파악하는 방법을 소개합니다. CloudTrail, VPC Flow Logs, Route 53 Resolver 쿼리 로그를 CloudWatch Logs Insights로 상관 분석하는 4가지 패턴과 Lambda·Amazon SNS·EventBridge Scheduler를 활용한 자동화 방법도 함께 설명합니다.
- **[SAP 네트워크 트러블슈팅을 수 시간에서 수 분으로 단축: 에이전트형 AI 접근법](https://aws.amazon.com/jp/blogs/news/accelerate-sap-network-troubleshooting-from-hours-to-minutes-agentic-ai-approach/)** — Kiro-CLI와 AWS MCP Servers를 결합한 에이전트형 AI를 활용해 복잡한 SAP 환경의 네트워크 트러블슈팅 시간을 수 시간에서 수 분으로 줄이는 방법을 소개합니다. VPC Flow Logs, 보안 그룹, Transit Gateway 등을 자연어 프롬프트로 진단하며, AZ 간 지연 시간 분석·보안 그룹 드리프트 탐지·용량 예측 등 5가지 실제 사례를 통해 운영 효율화 방안을 설명합니다.

## 2026-10-16 · 주간 요약

- **[프라이빗 액세스로 데이터 경계를 AWS Management Console까지 확장](https://aws.amazon.com/jp/blogs/news/extend-your-data-perimeter-to-the-aws-management-console-with-private-access/)** — AWS Management Console 프라이빗 액세스가 인터넷 연결 없는 VPC를 지원하며 일반 공개되었습니다. VPC 엔드포인트 정책과 리소스 제어 정책(RCP)을 결합해 인증 흐름·정적 자산·콘솔 전용 API 트래픽을 AWS PrivateLink를 통해 라우팅함으로써 데이터 경계를 강화할 수 있습니다.

## 2026-10-15 · 주간 요약

- **[AWS STS 세션 토큰 크기 제한 단순화 및 크기 모니터링 지원](https://aws.amazon.com/jp/blogs/news/aws-sts-simplifies-session-token-size-limits-and-adds-session-token-size-monitoring/)** — AWS STS 세션 토큰 크기 제한이 4,096바이트 단일 제한으로 단순화되어 세션 정책 및 세션 태그에 사용할 수 있는 용량이 확대되었습니다. 토큰 크기는 API 응답, Amazon CloudWatch 지표, AWS CloudTrail 이벤트를 통해 확인할 수 있으며, 로드 밸런서·데이터베이스 등 토큰을 처리하는 시스템에서는 MinimumSessionTokenSize 파라미터로 최대 토큰 크기를 검증하는 것이 권장됩니다.

## 2026-10-14 · 주간 요약

- **[Amazon GuardDuty 확장 위협 탐지에 5가지 새로운 지표 추가: 공격 시퀀스 탐지 강화](https://aws.amazon.com/jp/blogs/news/guardduty-extended-threat-detection-has-added-five-new-indicators-to-surface-attack-sequences/)** — Amazon GuardDuty 확장 위협 탐지의 공격 시퀀스 탐지 결과에 Amazon Inspector, Amazon VPC Reachability Analyzer, Amazon Macie, AWS Security Hub에서 수집한 취약점·도달 가능성·설정 오류·민감 데이터 정보를 포함한 5가지 새로운 지표가 추가되었습니다. 이를 통해 낮은 수준의 런타임 신호를 CRITICAL 심각도의 실행 가능한 탐지 결과로 통합하여 인시던트 대응 효율을 높입니다.

## 2026-10-06 · 주간 요약

- **[주간 AWS – 2026년 9월 28일 주](https://aws.amazon.com/jp/blogs/news/aws-weekly-20260928/)** — Amazon Route 53 Resolver DNS Firewall에서 Palo Alto Networks Advanced DNS Security GA, AWS Backup 논리적 에어갭 볼트의 Amazon FSx for NetApp ONTAP 지원, Aurora PostgreSQL에서 Apache Iceberg/Parquet 직접 쿼리 등 다양한 네트워킹·스토리지·데이터베이스 업데이트가 발표되었습니다. 네트워킹 관점에서는 DNS 보안 강화와 AWS IAM Identity Center 멀티 리전 지원 확대가 주목할 만합니다.

## 2026-09-25 · 주간 요약

- **[주간 AWS – 2026년 9월 14일 주](https://aws.amazon.com/jp/blogs/news/aws-weekly-20260914/)** — AWS Direct Connect 전용 연결 정액 요금 도입, AWS PrivateLink Tunnel Endpoint 출시, AWS Transfer Family의 Network Load Balancer 환경에서 송신 IP 보존 지원 등 네트워킹 관련 업데이트가 다수 포함되었습니다. 그 외 Amazon Bedrock AgentCore 신규 런타임, Amazon ECS의 Amazon S3 Files 지원 확장, Amazon Connect 신규 기능 등 다양한 서비스 업데이트가 발표되었습니다.

## 2026-09-24 · 주간 요약

- **[Amazon CloudFront로 SAP S/4HANA에 mTLS 인증 구현하기](https://aws.amazon.com/jp/blogs/news/implement-mtls-authentication-with-amazon-cloudfront-for-sap-s-4hana/)** — Amazon CloudFront의 mTLS verify 모드를 활용해 엣지에서 클라이언트 인증서를 검증하고, ALB 패스스루와 SAP ICM의 X.509 인증을 결합하여 패스워드 없는 SSO를 구현하는 아키텍처를 소개합니다. 이 구성은 글로벌 TLS 핸드셰이크 지연 시간을 줄이고 초기 로그인 시간을 약 40~50% 단축하는 효과를 내부 테스트에서 확인했습니다.

## 2026-09-19 · 주간 요약

- **[SAP Commerce Cloud와 AWS 기반 SAP Cloud ERP Private 통합 – 실증된 실용적 접근법](https://aws.amazon.com/jp/blogs/news/integrating-sap-commerce-cloud-with-sap-cloud-erp-private-on-aws-a-practical-and-proven-approach/)** — SAP Commerce(SAP Hybris) 2205 메인스트림 유지보수 종료를 앞두고, SAP Commerce Cloud SaaS와 AWS 기반 SAP Cloud ERP Private를 통합하는 모더나이제이션 아키텍처를 소개합니다. 리전 선택, Amazon CloudFront·AWS Global Accelerator·Amazon Route 53를 활용한 지연 시간 최적화, 보안 등 네 가지 관점에서 모범 사례를 제시하며, Buy with Prime 및 Amazon MCF와의 연동을 통한 e커머스 확장 방안도 다룹니다.

## 2026-09-15 · 주간 요약

- **[자동 추론 입문](https://aws.amazon.com/jp/blogs/news/a-gentle-introduction-to-automated-reasoning/)** — 자동 추론(Automated Reasoning)의 개념을 C·Python 코드 예제와 함께 쉽게 설명하며, 1,300년 이상 걸리는 망라적 테스트를 밀리초 만에 검증할 수 있는 원리와 한계(정지 문제로 인한 'Don't know' 응답)를 다룹니다. IAM Access Analyzer, VPC Reachability Analyzer 등 AWS 서비스에서의 실제 활용 사례도 소개합니다.

## 2026-09-13 · 주간 요약

- **[Amazon MWAA와 Airflow 3.0을 활용한 이벤트 기반 파이프라인 오케스트레이션](https://aws.amazon.com/jp/blogs/news/event-driven-pipeline-orchestration-with-amazon-mwaa-and-airflow-3-0/)** — Apache Airflow 3.0의 Asset Watcher와 Amazon SQS를 결합해 여러 Amazon MWAA 환경 및 계정 간 이벤트 기반 오케스트레이션을 구현하는 방법을 설명합니다. 폴링 방식 센서를 이벤트 기반 트리거로 교체함으로써 환경 간 오케스트레이션 지연 시간을 수 분에서 수 초로 단축할 수 있으며, 계정 간 IAM 및 Amazon VPC 네트워크 구성 모범 사례도 함께 소개합니다.

## 2026-08-29 · 주간 요약

- **[Amazon CloudWatch Logs로 Application Load Balancer 로그 분석하기](https://aws.amazon.com/jp/blogs/news/analyze-application-load-balancer-logs-with-amazon-cloudwatch-logs/)** — Amazon CloudWatch Logs가 ALB의 액세스 로그, 연결 로그, 헬스체크 로그를 Vended Logs로 구조화된 JSON 형태로 직접 수집하는 기능을 지원합니다. 이를 통해 요청·연결·대상 단위의 세밀한 관측성을 확보하고, 대시보드·Log Analytics·Contributor Insights를 활용한 장애 분석 및 알람 설정이 가능해집니다.

## 2026-08-25 · 주간 요약

- **[주간 AWS – 2026년 8월 17일 주](https://aws.amazon.com/jp/blogs/news/aws-weekly-20260817/)** — AWS Direct Connect가 인바운드 프리픽스 제어 및 VIF당 최대 1,000개 경로 확장을 발표하는 등 네트워킹 관련 업데이트가 포함되었으며, AWS CloudShell 비주얼 파일 편집기 추가·Amazon ECR 복제 규칙 상한 25개 상향 등 다양한 서비스 개선이 이루어졌습니다.

## 2026-08-21 · 주간 요약

- **[Oracle Database 26ai의 자연어 쿼리: Amazon RDS for Oracle에서 Amazon Bedrock을 활용한 Select AI 입문](https://aws.amazon.com/jp/blogs/news/natural-language-queries-on-oracle-database-26ai-getting-started-with-select-ai-on-amazon-rds-for-oracle-with-amazon-bedrock/)** — Amazon RDS for Oracle에서 Oracle Database 26ai가 지원되면서, Amazon Bedrock 기반 모델을 통해 자연어로 관계형 데이터를 조회하는 Select AI 기능을 사용할 수 있게 되었습니다. VPC 인터페이스 엔드포인트와 IAM 자격 증명 설정부터 DBMS_CLOUD_AI 프로필 생성 및 자연어 쿼리 실행까지의 구성 방법을 소개합니다.
