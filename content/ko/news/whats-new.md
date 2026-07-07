---
hide:
  - toc
---
# AWS What's New — 네트워킹 (한국어 요약)

[AWS What's New](https://aws.amazon.com/new/)의 신규 발표 중 **네트워킹 관련 항목**만 추려 매일(평일) 오전 자동 요약합니다. 원문은 각 항목의 링크에서 확인하세요. 최신 항목이 맨 위에 표시됩니다.

<!-- NEWS:INSERT -->

## 2026-07-07 · 전일 업데이트

- **[Amazon EVS, VCF 9.0 및 9.1 지원 발표](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-evs-vcf9)** — Amazon Elastic VMware Service(EVS)가 VMware Cloud Foundation(VCF) 9.0 및 9.1을 지원합니다. Amazon VPC 내 EC2 베어메탈 인스턴스에서 최신 VCF 버전을 직접 실행하고, 기존 데이터센터와 동일한 도구·프로세스로 관리할 수 있습니다.

## 2026-07-03 · 전일 업데이트

- **[AWS Config, 8개의 새로운 리소스 유형 지원 추가](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-config-new-resource-types)** — AWS Config가 Amazon API Gateway, Amazon EC2, Amazon S3 Vectors 등 주요 서비스에 걸쳐 8개의 새로운 리소스 유형을 추가로 지원합니다. 이를 통해 더 넓은 범위의 리소스에 대한 검색, 평가, 감사 및 교정이 가능해지며, 전체 리소스 유형 기록이 활성화된 경우 자동으로 추적됩니다.

## 2026-07-02 · 전일 업데이트

- **[ECS Service Connect, 영역 인식 라우팅 지원 시작](https://aws.amazon.com/about-aws/whats-new/2026/07/ecs-service-connect-zone-aware/)** — Amazon ECS의 ECS Service Connect가 영역 인식 라우팅을 지원하여, 동일 AZ 내 서비스 간 트래픽을 우선 라우팅함으로써 AZ 간 데이터 전송 비용과 지연 시간을 줄일 수 있습니다. 엔드포인트 수가 변동되더라도 트래픽 가중치를 동적으로 조정해 대상 서비스 전반의 부하 균형을 유지합니다.
- **[Amazon ECS Express Mode, 사용자 정의 태스크 정의 지원 추가](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ecs-express-mode-custom-task-def/)** — Amazon ECS Express Mode가 사용자 정의 태스크 정의를 지원하여, 기존 CI/CD 파이프라인 및 IaC 워크플로에서 사용하던 태스크 정의를 Express Mode의 간소화된 배포 환경에서 그대로 재사용할 수 있습니다. 이를 통해 기존 운영 방식을 유지하면서도 Express Mode의 인프라 자동화 이점을 함께 활용할 수 있습니다.
- **[AWS Network Firewall, Amazon EKS 및 Amazon ECS 컨테이너 속성 기반 검사 지원](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-network-firewall-container-attributes-referencing)** — AWS Network Firewall이 컨테이너 속성 기반 규칙을 지원하여, Amazon EKS의 네임스페이스·클러스터 이름·레이블, Amazon ECS의 클러스터 이름·컨테이너 인스턴스 속성 등 네이티브 컨테이너 구성 요소로 방화벽 정책을 작성할 수 있습니다. 파드 스케일링이나 재시작 시마다 IP 기반 규칙을 갱신해야 하는 복잡성이 해소되어 컨테이너화된 워크로드 보안 관리가 간소화됩니다.
- **[AWS Interconnect - last mile, AT&T와의 신규 파트너십 게이티드 프리뷰 발표](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-announces-AWS-interconnect-last-mile-ATT-gated-preview/)** — AWS가 지사, 데이터 센터, 원격 거점을 AWS에 간편하게 연결할 수 있는 완전 관리형 연결 서비스인 AWS Interconnect - last mile을 AT&T와의 파트너십으로 게이티드 프리뷰에서 제공합니다. 고객은 선호하는 AWS 리전, 대역폭, Direct Connect Gateway를 선택하는 것만으로 프라이빗 고속 연결을 즉시 구성할 수 있어 네트워크 설정의 복잡성이 크게 줄어듭니다.

## 2026-07-01 · 전일 업데이트

- **[AWS CloudFormation 및 CDK 익스프레스 모드로 인프라 배포 속도 최대 4배 향상](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-cloudformation-cdk/)** — AWS CloudFormation과 CDK의 익스프레스 모드는 트래픽 준비 상태 확인·리전 전파 등 확장된 안정화 대기 과정을 생략하고 리소스 구성 적용 시점에 스택 작업을 완료하여 배포 시간을 최대 4배 단축합니다. 개발 환경에서 빠른 반복 주기가 필요한 개발자와 AI 에이전트의 인프라 구축 속도를 크게 개선합니다.
- **[AWS Parallel Computing Service, Slurm 메이저 버전 인플레이스 업그레이드 지원](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-parallel-computing-service-upgrade/)** — AWS Parallel Computing Service(PCS)가 기존 클러스터에 대한 관리형 인플레이스 Slurm 메이저 버전 업그레이드를 지원합니다. 실행 중인 작업을 중단하지 않고 최대 3개의 Slurm 메이저 버전을 한 번에 올릴 수 있으며, 컨트롤러·회계 데이터베이스·REST API 등 모든 관리형 Slurm 구성 요소의 업그레이드를 PCS가 처리합니다.
- **[AWS 리전 역량 데이터를 위한 오픈소스 솔루션 Capability Insights 출시](https://aws.amazon.com/about-aws/whats-new/2026/06/capability-insights-aws/)** — AWS가 리전별 역량 데이터를 사용자 소유의 Amazon VPC 내에 직접 배포할 수 있는 오픈소스 셀프 호스팅 대시보드 솔루션 Capability Insights를 출시했습니다. 데이터 레지던시 요구사항이 있는 조직이나 멀티 리전 아키텍처를 계획하는 팀이 자체 네트워크와 거버넌스 하에서 리전 역량 데이터를 관리할 수 있도록 설계되었습니다.
- **[AWS Security Hub CSPM, 31개 자동화 제어 항목을 포함한 AI 보안 모범 사례 표준 출시](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-security-hub-cspm-ai-security/)** — AWS Security Hub CSPM이 Amazon Bedrock, Amazon Bedrock AgentCore, Amazon SageMaker 워크로드를 대상으로 네트워크 격리·암호화 등 주요 보안 영역을 자동 평가하는 31개 제어 항목으로 구성된 AI 보안 모범 사례 표준을 발표했습니다. 수동 평가나 커스텀 규칙 작성 없이 배포된 AI 리소스의 보안 구성을 지속적으로 검사할 수 있습니다.

## 2026-06-30 · 전일 업데이트

- **[Amazon MWAA Serverless, 공유 VPC 구성 지원 추가](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-mwaa-serverless-vpc/)** — Amazon MWAA Serverless가 AWS RAM을 통해 공유된 VPC 서브넷을 이제 지원합니다. 이로써 멀티 계정 랜딩 존 아키텍처에서 중앙 집중식으로 네트워킹을 관리하는 조직도 MWAA Serverless 워크플로를 공유 서브넷 위에서 오류 없이 생성할 수 있게 되었습니다.

## 2026-06-23 · 전일 업데이트

- **[AWS Network Firewall, 연결 안정성 향상을 위한 기본 드롭 액션 업데이트](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-network-firewall-updates-default-drop-action)** — AWS Network Firewall의 신규 방화벽 정책 기본 상태 저장 액션이 '양방향 Application drop established'에서 '서버 방향 전용 Application drop established'로 변경되었습니다. 이로써 기존 기본값이 정상적인 서버→클라이언트 TCP 트래픽을 자동 차단하던 문제가 해소되어 연결 안정성이 개선됩니다.
