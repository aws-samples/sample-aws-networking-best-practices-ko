---
hide:
  - toc
---
# AWS What's New — 네트워킹 (한국어 요약)

[AWS What's New](https://aws.amazon.com/new/)의 신규 발표 중 **네트워킹 관련 항목**만 추려 매일(평일) 오전 자동 요약합니다. 원문은 각 항목의 링크에서 확인하세요. 최신 항목이 맨 위에 표시됩니다.

<!-- NEWS:INSERT -->

## 2026-07-24 · 전일 업데이트

- **[Amazon CloudWatch Logs, Application Load Balancer 로그 지원 추가](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-cloudwatch-logs/)** — Amazon CloudWatch Logs가 ALB 로그를 벤디드 로그로 지원하여 액세스·연결·헬스 체크 로그를 CloudWatch에서 직접 분석할 수 있게 되었습니다. CloudWatch 텔레메트리 활성화 규칙을 통해 기존 및 신규 ALB 리소스의 로깅을 자동 구성할 수 있어 네트워크 트래픽 문제 진단이 간소화됩니다.
- **[Amazon EVS, 추가 리전으로 서비스 확대](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-evs-available-in-additional-regions/)** — Amazon Elastic VMware Service(Amazon EVS)가 아시아 태평양(서울), 유럽(취리히), 유럽(스톡홀름) 리전에서 새롭게 제공됩니다. AWS Nitro 기반 EC2 베어메탈 인스턴스 위에서 Amazon VPC 내에 VMware Cloud Foundation 환경을 직접 구성할 수 있어, 더 많은 지역에서 VMware 워크로드를 AWS로 신속하게 마이그레이션할 수 있습니다.
- **[SageMaker AI 추론에서 G7e 인스턴스 제공 리전 확대](https://aws.amazon.com/about-aws/whats-new/2026/07/g7e-sagemaker-ai/)** — Amazon EC2 G7e 인스턴스가 아시아 태평양(서울·도쿄) 및 유럽(런던) 리전의 Amazon SageMaker AI 추론에서 사용 가능해졌습니다. G7e 인스턴스는 최대 1,600 Gbps의 Elastic Fabric Adapter 네트워킹 대역폭을 제공하며, 이전 세대 G6e 대비 최대 2.3배 향상된 추론 성능으로 아시아·유럽 최종 사용자에게 더 가까운 위치에서 엔드포인트를 배포할 수 있습니다.
- **[Amazon SageMaker AI 추론, G7 인스턴스 지원 추가](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-sagemaker-ai-g7/)** — Amazon SageMaker AI 추론이 NVIDIA RTX PRO 4500 Blackwell GPU 기반 G7 인스턴스를 지원하며, 이전 세대 G6 대비 최대 4.6배 향상된 AI 추론 성능을 제공합니다. GPU당 32GB 메모리를 갖춰 중대형 생성형 AI 모델을 과도한 프로비저닝이나 모델 양자화 없이 비용 효율적으로 서빙할 수 있습니다.

## 2026-07-23 · 전일 업데이트

- **[AWS Network Load Balancer, 맞춤형 트래픽 라우팅을 위한 리스너 규칙 지원](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-network-load-balancer-supports-listener-rules/)** — Network Load Balancer(NLB)가 리스너 규칙을 지원하여 소스 IP 주소 유형에 따라 트래픽을 서로 다른 대상 그룹으로 라우팅할 수 있게 되었습니다. 이를 통해 단일 듀얼 스택 NLB에서 IPv6 클라이언트 트래픽은 IPv6 대상으로, IPv4 클라이언트 트래픽은 IPv4 대상으로 각각 전달하면서 양쪽 모두 원본 클라이언트 IP 주소를 종단 간 보존할 수 있습니다.
- **[Amazon EKS Auto Mode 및 Karpenter에서 EFA 및 배치 그룹 지원](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-eks-efa-placement-groups/)** — Amazon EKS가 EKS Auto Mode와 오픈소스 Karpenter 프로젝트의 노드 풀에서 Amazon EC2 배치 그룹과 Elastic Fabric Adapter(EFA) 네트워크 디바이스 구성을 지원합니다. 이를 통해 분산 학습 및 추론 워크로드에 최적화된 네트워크 인터페이스 구성과 EC2 인스턴스의 물리적 배치를 세밀하게 제어할 수 있습니다.
- **[AWS Direct Connect, 페루 리마에서 100G 확장 발표](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-direct-connect-100g-lima/)** — AWS가 페루 리마의 Cirion 데이터센터 내 기존 AWS Direct Connect 위치에서 100Gbps 전용 연결을 확장한다고 발표했습니다. 이번 확장은 페루 최초로 MACsec 암호화를 지원하는 100Gbps Direct Connect 연결을 제공하며, 중국을 제외한 모든 퍼블릭 AWS 리전, AWS GovCloud 리전, AWS 로컬 존에 대한 프라이빗 네트워크 액세스가 가능합니다.

## 2026-07-22 · 전일 업데이트

- **[Amazon EC2 R6in 및 R6idn 인스턴스, 추가 리전에서 제공 시작](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ec2-r6in-r6idn/)** — Amazon EC2 R6in 및 R6idn 인스턴스가 유럽(파리)과 캐나다(중부) 리전에서 새롭게 제공됩니다. 이 6세대 네트워크 최적화 인스턴스는 최대 200Gbps 네트워크 대역폭을 지원하며, 5세대 대비 2배 높은 네트워크 대역폭과 패킷 처리 성능을 제공합니다.
- **[Amazon EC2 C6in 인스턴스, 아시아 태평양(타이베이) 리전에서 제공 시작](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ec2-c6in/)** — Amazon EC2 C6in 인스턴스가 아시아 태평양(타이베이) 리전에서 새롭게 제공됩니다. 최대 200Gbps 네트워크 대역폭을 지원하는 이 6세대 네트워크 최적화 인스턴스는 네트워크 가상 어플라이언스, 텔코 5G UPF, 데이터 분석 등 고성능 네트워크 집약적 워크로드에 활용할 수 있습니다.
- **[Amazon EC2 M6in 및 M6idn 인스턴스, 추가 리전에서 제공 시작](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ec2-m6in-m6idn/)** — Amazon EC2 M6in 및 M6idn 인스턴스가 아시아 태평양(하이데라바드)과 남미(상파울루) 리전에서 새롭게 제공됩니다. 최대 200Gbps 네트워크 대역폭을 갖춘 이 6세대 네트워크 최적화 인스턴스는 고성능 파일 시스템, 분산형 웹 서비스 등 네트워크 집약적 워크로드의 성능과 처리량 향상에 활용할 수 있습니다.
- **[Amazon ECS 고급 배포 전략, AWS 유럽 소버린 클라우드에서 지원 시작](https://aws.amazon.com/about-aws/whats-new/2026/07/ecs-adv-deployments-eu-sovereign-cloud/)** — Amazon ECS의 블루/그린, 선형, 카나리 배포 전략이 AWS 유럽 소버린 클라우드에서 새롭게 지원됩니다. 별도의 커스텀 배포 툴링 없이 배포 라이프사이클 훅, 베이크 타임, 빠른 롤백 등 프로덕션 수준의 제어 기능을 활용해 컨테이너화된 애플리케이션을 더 안전하게 업데이트할 수 있습니다.

## 2026-07-21 · 전일 업데이트

- **[AWS CloudTrail에서 ID 기반으로 네트워크 활동 이벤트를 선택적으로 로깅](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-cloudtrail-filter-useridentity-advance-selectors/)** — AWS CloudTrail의 VPC 엔드포인트 네트워크 활동 이벤트에 대해 IAM 사용자 ID 기반 필터링이 추가되었습니다. 이를 통해 신뢰할 수 없는 ID의 액세스 거부 이벤트만 선택적으로 기록하는 등 로깅 비용과 노이즈를 줄이면서 무단 액세스 시도를 효과적으로 포착할 수 있습니다.
- **[그리스 아테네 AWS 로컬 존 정식 출시 발표](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-local-zone-athens-greece/)** — AWS가 그리스 아테네에 새로운 로컬 존을 정식 출시했으며, 이는 EMEA 지역에서 Amazon S3 및 Amazon EBS 로컬 스냅샷을 지원하는 두 번째 로컬 존입니다. 그리스 내 데이터 레지던시 요구 사항 충족을 위해 Amazon EC2(C7i·M7i·R7i 인스턴스), Amazon S3, Amazon EBS 등 주요 서비스를 현지에서 이용할 수 있습니다.
- **[KNFSD File Cache 프리뷰 출시 발표](https://aws.amazon.com/about-aws/whats-new/2026/07/knfsd-file-cache/)** — AWS가 오픈소스 기반의 확장 가능한 NFS 캐시 솔루션인 KNFSD File Cache를 프리뷰로 공개했습니다. 온프레미스 파일러, 다른 AWS 가용 영역·리전의 파일 시스템, 또는 AWS Interconnect를 통한 멀티클라우드 환경의 NFS 서버를 마운트하여 AWS 내 NFS 클라이언트에 재공유함으로써 네트워크 파일 액세스 성능을 향상시킬 수 있습니다.

## 2026-07-17 · 전일 업데이트

- **[Amazon CloudWatch Logs Insights, 25개의 새로운 쿼리 명령 및 함수 추가](https://aws.amazon.com/about-aws/whats-new/2026/7/amazon-cloudwatch-logs-insights-ql/)** — Amazon CloudWatch Logs Insights 쿼리 언어에 타입 변환·인코딩 함수(hexToAscii, decToHex 등), 날짜/시간 함수(parseDate, formatDate 등), 통계 집계, 결측값 처리, 시간 창 비교, 이상값 탐지, 룩업 데이터 보강 등 25개의 새로운 명령과 함수가 추가되었습니다. 이를 통해 복잡한 로그 분석 및 상관 관계 파악이 더욱 용이해져 네트워킹 운영 관측성이 향상됩니다.

## 2026-07-16 · 전일 업데이트

- **[Amazon EC2 G7e 인스턴스, 추가 리전에서 제공 시작](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-g7e-additional-regions/)** — Amazon EC2 G7e 인스턴스가 유럽(프랑크푸르트, 스톡홀름) 및 아시아 태평양(뭄바이) 리전에서 새롭게 제공됩니다. NVIDIA RTX PRO 6000 Blackwell GPU 기반으로 G6e 대비 최대 2.3배 추론 성능을 제공하며, LLM·생성형 AI·공간 컴퓨팅 워크로드에 활용할 수 있습니다.
- **[Amazon RDS 및 Aurora, 추가 AWS 리전에서 R8g·M8g 데이터베이스 인스턴스 지원](https://aws.amazon.com/about-aws/whats-new/2026/7/amazon-rds-aurora-r8g-m8g-regions/)** — AWS Graviton4 기반 R8g 및 M8g 데이터베이스 인스턴스가 Amazon Aurora(MySQL·PostgreSQL 호환)와 Amazon RDS의 여러 추가 리전에서 정식 제공됩니다. 이를 통해 더 많은 리전의 고객이 Graviton4의 향상된 성능과 비용 효율성을 데이터베이스 워크로드에 활용할 수 있습니다.
- **[AWS Elastic Disaster Recovery, AWS 간 워크로드 복구 시간 단축](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-drs-fast-recovery/)** — AWS Elastic Disaster Recovery(AWS DRS)가 Amazon EC2에서 실행 중인 소스 서버에 대해 불필요한 준비 단계를 건너뛰어 Windows는 최대 65%, Linux는 최대 40% 복구 시간을 단축합니다. AWS 기반 워크로드는 이미 호환 드라이버와 구성을 갖추고 있어 더 적은 단계로 빠르게 애플리케이션을 복구할 수 있습니다.
- **[Amazon CloudWatch, 로그 보강을 위한 룩업 프로세서 발표](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-cloudwatch-lookup-processor/)** — Amazon CloudWatch가 CloudWatch Pipeline 내에서 CSV 파일 기반 룩업 테이블을 활용해 로그 이벤트에 추가 컨텍스트를 자동으로 보강하는 룩업 프로세서를 지원합니다. 예를 들어 IP 주소와 애플리케이션 팀을 매핑한 CSV를 업로드하면 VPC Flow Logs 수집 시 팀 소유 정보를 자동으로 태깅할 수 있어 네트워크 로그 분석이 용이해집니다.
- **[Amazon EC2 M8in, M8idn, M8ib, M8idb 인스턴스, 추가 리전에서 제공 시작](https://aws.amazon.com/about-aws/whats-new/2026/07/m8in-m8idn-m8ib-m8idb-new-regions)** — 네트워크 최적화 인스턴스인 Amazon EC2 M8in·M8idn과 EBS 최적화 인스턴스인 M8ib·M8idb가 미국 동부(오하이오), 유럽(아일랜드), 아시아 태평양(도쿄) 리전에서 추가로 제공됩니다. M8in·M8idn은 최대 600Gbps 네트워크 대역폭을 제공하며, 최신 6세대 AWS Nitro 카드를 탑재해 이전 세대 대비 최대 43% 높은 성능을 발휘합니다.

## 2026-07-15 · 전일 업데이트

- **[Amazon Managed Service for Apache Flink, Flink 애플리케이션 구축·운영을 위한 AI Agent Skills 제공](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-managed-service-flink-agent-skills/)** — Amazon Managed Service for Apache Flink가 AI 코딩 어시스턴트에 전문 가이던스를 제공하는 AI Agent Skills를 출시했습니다. 애플리케이션 생성, 트러블슈팅, 스케일링, 모니터링, 네트워킹 구성, 비용 최적화 등의 작업을 지원하며 Flink 2.2 등 최신 버전으로의 업그레이드도 간소화합니다.
- **[Amazon CloudFront Functions, CloudFront 액세스 로그로의 직접 로깅 지원](https://aws.amazon.com/about-aws/whats-new/2026/07/cloudfront-functions-access-logs/)** — Amazon CloudFront Functions에서 새로운 헬퍼 메서드 cf.logCustomData()를 사용해 커스텀 데이터를 CloudFront 액세스 로그에 직접 기록할 수 있게 되었습니다. 기존에는 함수 로그가 Amazon CloudWatch Logs에 별도로 저장되어 액세스 로그와 상호 연계가 필요했으나, 이번 업데이트로 단일 로그 시스템에서 엣지 함수 동작과 요청 정보를 통합 분석할 수 있습니다.

## 2026-07-11 · 전일 업데이트

- **[Amazon EC2 네트워크/EBS 인스턴스, 추가 리전에서 제공 시작](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ec2-r8in-r8ib-r8idn-r8idb)** — Amazon EC2 R8in, R8ib, R8idn, R8idb 인스턴스가 아시아 태평양(도쿄) 및 유럽(프랑크푸르트, 아일랜드) 리전에서 새롭게 제공됩니다. 특히 R8in·R8idn 인스턴스는 600 Gbps 네트워크 대역폭을 지원하며, 이는 향상된 네트워킹 EC2 인스턴스 중 최고 수준입니다.
- **[Amazon EC2 G7 인스턴스, AWS 미국 동부(버지니아 북부) 리전에서 제공 시작](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ec2-g7-available-North-Virginia)** — NVIDIA RTX PRO 4500 Blackwell Server Edition GPU 기반의 Amazon EC2 G7 인스턴스가 미국 동부(버지니아 북부) 리전에서 출시되었습니다. G6 인스턴스 대비 AI 추론 성능은 최대 4.6배, 그래픽 성능은 최대 2.1배 향상되어 AI 모델 배포 및 GPU 가속 워크로드에 활용할 수 있습니다.
- **[AWS DMS Schema Conversion, 오프라인 SQL Server 변환 지원](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-dms-schema-conversion-offline-source/)** — AWS Database Migration Service(DMS) Schema Conversion이 Microsoft SQL Server의 오프라인 소스 변환을 지원하여, 소스 데이터베이스에 직접 연결하지 않고도 스키마 변환이 가능해졌습니다. 이를 통해 보안 검토, 방화벽 변경, VPN 설정 없이 마이그레이션을 진행할 수 있어 엄격한 보안 정책을 가진 조직에 특히 유용합니다.
- **[Amazon EC2 I8g 인스턴스, AWS GovCloud(미국) 리전에서 제공 시작](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ec2-i8g-instances-aws-govcloud-us-regions/)** — 스토리지 최적화 Amazon EC2 I8g 인스턴스가 AWS GovCloud(미국 동부, 미국 서부) 리전에서 정식 출시되었습니다. AWS Graviton4 프로세서와 3세대 AWS Nitro SSD를 탑재하여 이전 세대 I4g 대비 컴퓨팅 성능은 최대 60%, 스토리지 I/O 지연 시간은 최대 50% 개선되었습니다.

## 2026-07-10 · 전일 업데이트

- **[AWS Client VPN, 4개 추가 AWS 리전으로 가용 범위 확대](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-client-vpn-four-additional-regions/)** — AWS Client VPN이 캐나다 서부(캘거리), 멕시코(중부), 아시아 태평양(뉴질랜드·타이베이) 등 4개 신규 리전에서 제공됩니다. 이 완전 관리형 서비스를 통해 원격 인력이 AWS 및 온프레미스 네트워크 리소스에 안전하게 연결할 수 있으며, 별도의 하드웨어 VPN 어플라이언스 없이 단일 콘솔에서 관리할 수 있습니다.
- **[AWS Config, 191개 추가 관리형 규칙 지원](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-config-additional-managed-rules)** — AWS Config가 Amazon Bedrock, Amazon SageMaker, Amazon ECS, Amazon EKS, Amazon RDS 등 주요 서비스를 대상으로 191개의 관리형 규칙을 새롭게 지원합니다. 신규 규칙은 암호화, 로깅, 퍼블릭 액세스, 네트워크 보안, 데이터 보호 등의 구성 평가를 포함하며, AI 워크로드와 핵심 클라우드 인프라 전반의 거버넌스 적용 범위가 확대됩니다.

## 2026-07-09 · 전일 업데이트

- **[AWS Security Hub, 공개적으로 접근 가능한 리소스를 식별하는 Network Scanning 기능 출시](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-security-hub-network-scanning/)** — AWS Security Hub에 Network Scanning 기능이 추가되어 실제 인터넷에서 접근 가능한 리소스를 탐지할 수 있게 되었습니다. 보안 그룹 규칙이나 라우팅 테이블 기반의 이론적 분석이 아닌 실제 프로빙 방식으로 AWS 및 Azure 환경의 공개 IP, 가상 머신, 로드 밸런서의 열린 포트와 실행 중인 서비스를 식별합니다.

## 2026-07-08 · 전일 업데이트

- **[Amazon EC2 C8ine 인스턴스, AWS 유럽(프랑크푸르트) 리전에서 제공 시작](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ec2-c8ine-aws-frankfurt/)** — Amazon EC2 C8ine 인스턴스가 AWS 유럽(프랑크푸르트) 리전에서 사용 가능해졌습니다. 6세대 AWS Nitro 카드를 탑재해 이전 세대 C6in 대비 최대 43% 높은 성능과 vCPU당 최대 2.5배 향상된 패킷 처리 성능을 제공하며, 인터넷 게이트웨이를 통한 트래픽에서 최대 2배 높은 네트워크 처리량을 지원합니다.
- **[AWS, VPC Encryption Controls에 선언적 제어 기능 도입](https://aws.amazon.com/about-aws/whats-new/2026/07/vpc-encryption-controls-declarative-controls/)** — 이제 선언적 정책(declarative policies)을 사용해 환경 내 모든 VPC에 VPC Encryption Controls를 모니터링 또는 강제 적용 모드로 중앙 집중식 관리할 수 있습니다. 계정, 조직 또는 특정 조직 단위 수준에서 VPC 내·간 전송 중 암호화를 감사·적용하고 HIPAA, FedRAMP, PCI 등 규정 준수를 입증하는 데 활용할 수 있습니다.

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
