---
hide:
  - toc
---
# AWS What's New — 네트워킹 (한국어 요약)

[AWS What's New](https://aws.amazon.com/new/)의 신규 발표 중 **네트워킹 관련 항목**만 추려 매일(평일) 오전 자동 요약합니다. 원문은 각 항목의 링크에서 확인하세요. 최신 항목이 맨 위에 표시됩니다.

<!-- NEWS:INSERT -->

## 2026-09-05 · 전일 업데이트

- **[Amazon EC2 C8g 인스턴스, 추가 리전에서 제공 시작](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-ec2-c8g-instances-additional-regions/)** — Amazon EC2 C8g 인스턴스가 AWS 아시아 태평양(타이베이, 뉴질랜드) 및 AWS GovCloud(US-East) 리전에서 새롭게 제공됩니다. AWS Graviton4 프로세서 기반으로 Graviton3 대비 최대 30% 향상된 성능을 제공하며, HPC·배치 처리·게임·비디오 인코딩 등 컴퓨팅 집약적 워크로드에 적합합니다.

## 2026-09-04 · 전일 업데이트

- **[Amazon EC2 P6-B200 인스턴스, AWS 아시아 태평양(하이데라바드) 리전 출시](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-ec2-p6-b200-instances-available-asia-pacific-hyderabad)** — NVIDIA Blackwell GPU 기반의 Amazon EC2 P6-B200 인스턴스가 AWS 아시아 태평양(하이데라바드) 리전에서 제공됩니다. P5en 대비 최대 2배의 AI 학습·추론 성능과 최대 3.2Tbps의 EFAv4 네트워킹을 지원합니다.
- **[Amazon EC2 P6-B300 인스턴스, AWS 아시아 태평양(자카르타) 리전 출시](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-ec2-p6-b300-instances-available-asia-pacific-jakarta)** — NVIDIA Blackwell Ultra GPU 8개와 6.4Tbps EFA 네트워킹을 갖춘 Amazon EC2 P6-B300 인스턴스가 AWS 아시아 태평양(자카르타) 리전에서 출시되었습니다. P6-B200 대비 2배의 네트워킹 대역폭과 1.5배의 GPU 메모리를 제공하여 대규모 파운데이션 모델 학습 및 배포에 적합합니다.
- **[Amazon CloudFront, 정액제 요금제 API 지원 발표](https://aws.amazon.com/about-aws/whats-new/2026/09/cloudfront-flat-rate-pricing-plans-api/)** — Amazon CloudFront의 정액제 요금제를 이제 AWS CLI, SDK, CloudFormation, CDK 또는 PricingPlanManager API를 통해 프로그래밍 방식으로 구독 및 관리할 수 있습니다. 이를 통해 IaC 워크플로에서 콘솔 수동 작업 없이 콘텐츠 전송, WAF, DDoS, DNS 등을 포함한 정액 요금제를 자동화할 수 있습니다.
- **[AWS Gateway Load Balancer, 빠른 장애 복구를 위한 TCP Reset 지원](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-gateway-load-balancer-tcp-reset/)** — AWS Gateway Load Balancer(GWLB)가 대상 인스턴스가 비정상 상태가 되거나 등록 해제될 때, 또는 유휴 타임아웃 만료 시 TCP Reset(RST) 패킷을 전송하는 기능을 지원합니다. 이를 통해 장애 감지 및 복구 시간을 기존 수 분에서 수 초로 단축할 수 있습니다.
- **[Amazon S3, FIPS 엔드포인트에 대한 PrivateLink 지원](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-s3-privatelink-fips-endpoints)** — Amazon S3가 FIPS 140-3 검증 엔드포인트에 대해 AWS PrivateLink를 지원하기 시작했습니다. 이를 통해 보안 및 규정 준수 요건이 있는 고객은 트래픽을 VPC 내부에 유지하면서 FIPS 검증 암호화 모듈을 사용해 S3에 연결할 수 있습니다.
- **[Amazon MemoryDB, AWS GovCloud(미국) 리전에서 AWS PrivateLink 지원](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-memorydb-privatelink/)** — Amazon MemoryDB가 AWS GovCloud(US-West) 및 AWS GovCloud(US-East) 리전에서 AWS PrivateLink를 통한 프라이빗 액세스를 지원합니다. 인터페이스 VPC 엔드포인트를 생성하면 퍼블릭 인터넷에 트래픽을 노출하지 않고 VPC에서 MemoryDB에 안전하게 연결할 수 있습니다.

## 2026-09-01 · 전일 업데이트

- **[Amazon Redshift, Enhanced VPC Routing 환경에서 AWS IAM Identity Center 인증 지원](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-redshift-supports-idc-evr)** — Amazon Redshift가 Enhanced VPC Routing(EVR)이 구성된 프로비저닝 클러스터 및 서버리스 워크그룹에서 AWS IAM Identity Center 인증을 지원합니다. 이를 통해 기업 자격 증명으로 SSO 액세스가 가능하며, 모든 트래픽이 Amazon VPC를 통해 AWS 네트워크 내에서만 이동하므로 데이터 상주 및 네트워크 격리 요건을 충족할 수 있습니다.
- **[Amazon Cognito, 사용자 풀 도메인 없이 머신 간 인증 지원](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cognito-get-client-token/)** — Amazon Cognito가 새로운 GetClientToken API 작업을 통해 사용자 풀 도메인 구성 없이 AWS SDK, CLI, 또는 API로 직접 머신 간(M2M) 액세스 토큰을 발급받을 수 있게 되었습니다. 이를 통해 마이크로서비스 및 자동화 워크로드의 서비스 간 통신 인증 경로가 추가되어 네트워크 구성 복잡도를 줄일 수 있습니다.

## 2026-08-29 · 전일 업데이트

- **[Amazon EC2 C8gn 인스턴스, AWS 유럽(파리) 리전에서 출시](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-c8gn-europe-paris/)** — AWS Graviton4 프로세서 기반의 Amazon EC2 C8gn 인스턴스가 유럽(파리) 리전에서 제공됩니다. 최대 600 Gbps 네트워크 대역폭을 지원하며, 네트워크 최적화 EC2 인스턴스 중 가장 높은 네트워크 대역폭을 제공합니다.
- **[Amazon EC2 P6-B300 인스턴스, 추가 AWS 리전에서 출시](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-p6-b300-instances-available-additional-regions)** — Amazon EC2 P6-B300 인스턴스가 아시아 태평양(하이데라바드) 및 남미(상파울루) 리전으로 확대 제공됩니다. 6.4 Tbps EFA 네트워킹과 300 Gbps 전용 ENA 처리량을 갖추고 있으며, P6-B200 대비 2배의 네트워킹 대역폭을 제공해 대규모 파운데이션 모델 학습 및 배포에 적합합니다.

## 2026-08-27 · 전일 업데이트

- **[Amazon EC2 R8id 인스턴스, 추가 AWS 리전에서 제공 시작](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-r8id/)** — Amazon EC2 R8id 인스턴스가 아시아 태평양(뭄바이, 말레이시아, 시드니), 캐나다(중부), 유럽(아일랜드, 스톡홀름) 리전으로 확대 제공됩니다. R8id 인스턴스는 최대 22.8TB NVMe SSD 로컬 스토리지와 R6id 대비 최대 43% 높은 성능을 제공하여 인메모리 데이터베이스 및 실시간 빅데이터 분석 등 메모리 집약적 워크로드에 적합합니다.
- **[Amazon EC2 C8id 및 M8id 인스턴스, 추가 AWS 리전에서 제공 시작](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-c8id-m8id-aws-regions/)** — Amazon EC2 C8id 인스턴스는 아시아 태평양(시드니)과 캐나다(중부), M8id 인스턴스는 아시아 태평양(뭄바이)과 캐나다(중부) 리전으로 확대 제공됩니다. 두 인스턴스 모두 최대 22.8TB의 로컬 NVMe SSD 스토리지를 제공하며, 이전 6세대 인스턴스 대비 최대 43% 높은 컴퓨팅 성능과 3.3배 더 많은 메모리 대역폭을 지원합니다.

## 2026-08-26 · 전일 업데이트

- **[AWS Batch, Amazon ECS Managed Instances 지원 시작](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-batch-on-ecs-managed-instances/)** — AWS Batch가 Amazon ECS Managed Instances(ECS MI)를 새로운 컴퓨팅 옵션으로 지원하여, GPU 가속 및 컴퓨팅 집약적 배치 워크로드를 AWS 관리형 인프라에서 실행할 수 있게 되었습니다. AMI 업데이트, 보안 패치, 인스턴스 수명 주기를 AWS가 자동으로 처리하므로 고객이 직접 Amazon EC2 인프라를 관리하는 운영 부담이 줄어듭니다.
- **[AWS Lambda MicroVMs, AWS PrivateLink 지원 추가](https://aws.amazon.com/about-aws/whats-new/2026/08/lambda-microvms-supports-privatelink)** — AWS Lambda MicroVMs가 AWS PrivateLink를 지원하여 Amazon VPC 리소스에서 퍼블릭 인터넷을 거치지 않고 Lambda MicroVMs에 직접 프라이빗 연결이 가능해졌습니다. 이를 통해 금융, 의료, 공공 분야 등 규제 산업의 엄격한 네트워크 격리 요건을 충족할 수 있습니다.

## 2026-08-22 · 전일 업데이트

- **[Amazon EC2 C8gd, M8gd, R8gd 인스턴스, 추가 AWS 리전에서 제공 시작](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-c8gd-m8gd/)** — Amazon EC2 C8gd, M8gd, R8gd 인스턴스가 싱가포르, 멕시코(중부), 멜버른, 취리히 등 추가 리전으로 확대 제공됩니다. AWS Graviton4 프로세서 기반으로 최대 11.4TB의 로컬 NVMe SSD 스토리지를 탑재하며, Graviton3 대비 최대 30% 향상된 성능을 제공합니다.

## 2026-08-21 · 전일 업데이트

- **[라스베이거스, 네바다주 신규 AWS Local Zone 일반 출시 발표](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-local-zones-las-vegas-nevada/)** — AWS가 미국 라스베이거스, 네바다주에 새로운 AWS Local Zone을 일반 출시했습니다. 이 로컬 존은 Amazon EC2 C7i/M7i/R7i/C8gn 인스턴스, Amazon EBS, Amazon ECS, Amazon EKS, Application Load Balancer, AWS Direct Connect를 지원하여 해당 대도시권 사용자에게 낮은 지연 시간의 컴퓨팅·네트워킹 서비스를 제공합니다.
- **[Amazon EC2 P6-B300 인스턴스, 아시아 태평양(서울) 리전에서 출시](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-p6-b300/)** — Amazon EC2 P6-B300 인스턴스가 아시아 태평양(서울) 리전에서 사용 가능해졌습니다. 이 인스턴스는 6.4 Tbps EFA 네트워킹과 300 Gbps 전용 ENA 처리량을 제공하며, P6-B200 대비 2배의 네트워킹 대역폭을 갖춰 대규모 파운데이션 모델 학습 및 추론 워크로드에 적합합니다.
- **[Amazon CloudFront, Amazon S3 Multi-Region Access Points에 대한 Origin Access Control(OAC) 지원](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cloudfront-oac-s3-mrap)** — Amazon CloudFront가 Amazon S3 Multi-Region Access Points(MRAP)에 대해 Origin Access Control(OAC)을 지원하기 시작했습니다. 이를 통해 고객은 별도의 SigV4a 서명 처리 없이 지정된 CloudFront 배포에서만 MRAP 오리진에 액세스하도록 제한할 수 있어, 글로벌 분산 콘텐츠 제공의 보안과 운영 편의성이 향상됩니다.
- **[AWS Direct Connect, 인바운드 프리픽스 제어 및 더 높은 프리픽스 규모 지원 도입](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-direct-connect-new-prefix-controls)** — AWS Direct Connect가 인바운드 프리픽스 제어 기능을 도입하여 프라이빗 및 트랜짓 가상 인터페이스(VIF)에서 IPv4·IPv6 각각 최대 1,000개의 경로 프리픽스를 허용합니다. 기존 최대 100개 제한으로 인해 경로 요약 등의 우회 설계가 필요했던 대규모 온프레미스 네트워크 환경에서 운영 복잡성이 크게 줄어들 것으로 기대됩니다.

## 2026-08-20 · 전일 업데이트

- **[AWS Marketplace, Amazon Lightsail 지원 시작](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-marketplace-launch-ami-amazon-lightsail)** — AWS Marketplace에서 선택된 AMI를 Amazon Lightsail에 바로 배포할 수 있게 되었습니다. 고정 월정액으로 컴퓨팅·스토리지·데이터 전송을 제공하는 Lightsail의 간편한 인스턴스 생성 경험과 Marketplace AMI를 결합해 애플리케이션 배포가 더욱 쉬워졌습니다.
- **[AWS Storage Gateway, Tape 및 Volume Gateway에 FIPS 준수 프라이빗 연결 지원 추가](https://aws.amazon.com/about-aws/whats-new/2026/08/storage-gateway-fips-privatelink/)** — AWS Storage Gateway의 Tape Gateway와 Volume Gateway가 AWS PrivateLink를 통해 FIPS 140-3 검증 엔드포인트를 지원하게 되었습니다. 이제 FIPS 준수 트래픽을 퍼블릭 인터넷 대신 VPC 내 인터페이스 VPC 엔드포인트를 통해 프라이빗 AWS 네트워크로 유지할 수 있어 규제 대상 워크로드에서의 활용이 용이해졌습니다.

## 2026-08-18 · 전일 업데이트

- **[Amazon EC2 Auto Scaling, 인스턴스 일괄 종료 지원](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-auto-scaling-batch-termination)** — Amazon EC2 Auto Scaling이 단일 API 호출로 최대 100개의 인스턴스를 일괄 종료하는 기능을 지원합니다. AI/ML 학습 작업이나 이벤트 기반 아키텍처처럼 대규모 플릿을 빠르게 축소해야 하는 워크로드에서 API 호출 횟수를 줄이고 스케일 다운 속도를 높일 수 있습니다.
- **[Amazon MSK, Provisioned 클러스터에 대한 사용자 지정 도메인 이름 구성 지원](https://aws.amazon.com/about-aws/whats-new/2026/17/amazon-msk-custom-domain-names/)** — Amazon MSK Provisioned 클러스터에서 ZooKeeper 및 KRaft 모드 모두 클러스터 수준의 사용자 지정 도메인 이름을 손쉽게 설정할 수 있게 되었습니다. 이를 통해 클러스터 마이그레이션, 재해 복구 페일오버, 스케일링 시 클라이언트 애플리케이션의 연결 엔드포인트를 재구성 없이 유지할 수 있습니다.
- **[AWS Network Firewall, 스테이트풀 규칙 적중 횟수 지원](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-network-firewall-stateful-rule-hit-counts/)** — AWS Network Firewall이 스테이트풀 규칙별 적중 횟수를 제공하여 각 규칙이 네트워크 트래픽과 얼마나 자주 매칭되는지 파악할 수 있게 되었습니다. 이를 통해 인시던트 대응 가속화, 중복·미사용 규칙 식별, 정책 변경 검증 등 방화벽 정책 관리를 개선할 수 있습니다.
- **[Amazon OpenSearch Service, VPC 도메인에 대한 자동 시맨틱 강화 지원](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-opensearch-service-vpc/)** — Amazon OpenSearch Service가 VPC 도메인에서도 자동 시맨틱 강화 기능을 지원하여, 프라이빗 네트워크 환경의 고객이 도메인을 퍼블릭 인터넷에 노출하지 않고도 AI 기반 시맨틱 검색을 활용할 수 있게 되었습니다. 이 기능은 쿼리의 의미를 이해해 키워드 일치 없이도 관련 결과를 반환하는 컨텍스트 인식 검색을 가능하게 합니다.

## 2026-08-14 · 전일 업데이트

- **[AWS Client VPN, CLI 지원·관리 제어·빠른 연결 기능 추가](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-client-vpn-cli/)** — AWS VPN Client v6.0.x가 출시되어 CLI 지원, 기업용 관리 제어, 빠른 연결 수립 기능이 추가되었습니다. CLI를 통해 VPN 연결을 자동화 워크플로 및 IaC 배포에 통합할 수 있으며, 기존에는 서드파티 도구가 필요했던 작업을 기본 기능으로 처리할 수 있습니다.
- **[Spot Placement Score, 로컬 존 지원 추가](https://aws.amazon.com/about-aws/whats-new/2026/08/spot-placement-score-local-zones/)** — AWS Spot Placement Score가 이제 로컬 존을 포함한 점수를 제공하여 Spot 용량 요청 성공 가능성이 높은 위치를 더 넓은 범위에서 파악할 수 있습니다. 기존에는 로컬 존 용량 정보가 지역 및 영역 점수에서 제외되었으나, 이제 선택적으로 포함할 수 있습니다.
- **[AWS Certificate Manager, 이메일에서 DNS 검증 방식으로 전환 지원](https://aws.amazon.com/about-aws/whats-new/2026/08/AWS-Certificate-Manager-Email-DNS-Switch)** — AWS Certificate Manager(ACM)가 기존 공개 TLS 인증서의 도메인 검증 방식을 인증서 재발급이나 ARN 변경 없이 이메일에서 DNS로 전환할 수 있도록 지원합니다. CA/B Forum의 이메일 기반 도메인 검증 폐지 방침에 따라 ACM은 2027년부터 이메일 검증 인증서 발급을 단계적으로 중단할 예정입니다.

## 2026-08-13 · 전일 업데이트

- **[AWS Global View, AWS 리전 및 AWS 로컬 존을 위한 인터랙티브 맵 뷰 제공](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-global-view-map-view/)** — AWS Management Console의 AWS Global View에 인터랙티브 맵 뷰가 추가되어, 기존 목록 방식 대신 지도에서 AWS 리전과 로컬 존의 위치를 시각적으로 확인할 수 있게 되었습니다. 이를 통해 고객은 글로벌 AWS 인프라 풋프린트를 보다 직관적으로 파악하고 인프라 배치 결정을 내릴 수 있습니다.

## 2026-08-11 · 전일 업데이트

- **[Amazon EC2, 애플리케이션 상태 확인 기능 도입](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-application-status-checks)** — Amazon EC2가 인스턴스 내 애플리케이션 수준의 문제를 감지하고 대응할 수 있는 새로운 상태 확인 기능을 출시했습니다. 웹 서버 중단, Docker 데몬 미실행, 잘못된 네트워킹 구성, 트래픽 전달 불가 네트워크 인터페이스 등 애플리케이션 계층 장애를 자동으로 탐지할 수 있어 기존 시스템 수준 상태 확인을 보완합니다.

## 2026-08-09 · 전일 업데이트

- **[Amazon VPC IPAM, BYOIP 접두사에 대한 BGP 경로 보호 모니터링 및 위임된 RPKI 지원](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-vpc-ipam-bgp-rpki-byoip/)** — Amazon VPC IPAM이 BYOIP 접두사에 대해 BGP 경로 보호 모니터링과 위임된 RPKI 관리를 지원합니다. 네트워크 관리자는 단일 대시보드에서 RPKI 유효성 상태, ROA 강도, 경로 중복 감지를 중앙 집중식으로 확인하고 계정 및 리전 전반의 ROA 관리를 자동화할 수 있습니다.

## 2026-08-08 · 전일 업데이트

- **[Amazon OpenSearch UI, 네트워크 액세스 제어 지원 추가](https://aws.amazon.com/about-aws/whats-new/2026/08/opensearch-ui-network-access-control)** — Amazon OpenSearch Service의 OpenSearch UI 애플리케이션에 네트워크 액세스 제어 기능이 추가되어, aws:SourceVpce·aws:SourceVpc·aws:SourceIp 등 IAM 조건 키를 활용해 승인된 네트워크로만 액세스를 제한할 수 있습니다. ID 기반·리소스 기반·서비스 제어 정책 등 세 가지 수준에서 네트워크 제한을 적용해 일관된 데이터 경계를 구성할 수 있습니다.

## 2026-08-07 · 전일 업데이트

- **[Amazon EC2 G7 인스턴스, AWS 유럽(스페인) 리전에서 출시](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-g7-available-spain)** — NVIDIA RTX PRO 4500 Blackwell GPU를 탑재한 Amazon EC2 G7 인스턴스가 유럽(스페인) 리전에서 제공됩니다. G6 대비 AI 추론 성능 최대 4.6배, 그래픽 성능 최대 2.1배 향상되어 언어 번역·영상 분석·음성 인식 등 GPU 가속 워크로드에 활용할 수 있습니다.
- **[Amazon EC2 M8g 인스턴스, 추가 리전으로 확대 제공](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-m8g-instances-additional-regions/)** — AWS Graviton4 프로세서 기반의 Amazon EC2 M8g 인스턴스가 AWS 아시아 태평양(타이베이) 및 AWS 멕시코(중부) 리전에서 새롭게 제공됩니다. Graviton3 기반 인스턴스 대비 최대 30% 향상된 성능을 제공하며, 애플리케이션 서버·마이크로서비스·게임 서버 등 범용 워크로드에 적합합니다.

## 2026-08-06 · 전일 업데이트

- **[AWS Lambda, VPC 외부 함수에 최대 3,000 Mbps 확장형 네트워크 대역폭 지원 발표](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-lambda-network-bandwidth/)** — AWS Lambda가 VPC 외부에서 실행되는 함수에 대해 메모리 크기에 비례하는 확장형 네트워크 대역폭을 지원합니다. 메모리 2 GB에서 625 Mbps, 10 GB에서 최대 3,000 Mbps까지 제공되어 대용량 데이터를 처리하는 지연 시간에 민감한 워크로드의 데이터 전송 성능이 크게 향상됩니다.

## 2026-08-05 · 전일 업데이트

- **[[미리 보기 발표] AWS Network Firewall 기능으로 포워드 프록시 재도입](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-network-firewall-forward-proxy-preview/)** — AWS Network Firewall이 기존의 모든 필터링 기능을 유지하면서 명시적 포워드 프록시로도 동작할 수 있게 되었습니다. 이전에 별도 제품으로 분리되어 있던 프록시 기능이 Network Firewall에 통합되어, 단일 보안 정책으로 데이터 유출 및 악성코드 주입에 대한 중앙 집중식 보안 제어가 가능해집니다.
- **[Amazon EC2 C8g 인스턴스, 추가 리전에서 제공 시작](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-c8g-instances-additional-regions/)** — Amazon EC2 C8g 인스턴스가 유럽(파리), 아프리카(케이프타운), 이스라엘(텔아비브), 캐나다 서부(캘거리) 리전에서 새롭게 제공됩니다. AWS Graviton4 프로세서 기반으로 Graviton3 대비 최대 30% 향상된 성능을 제공하며, HPC·배치 처리·게임·비디오 인코딩 등 컴퓨팅 집약적 워크로드에 적합합니다.
- **[AWS Application Load Balancer 및 Network Load Balancer, RFC 9151 준수 보안 정책 지원](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-application-network/)** — AWS ALB와 NLB가 미국 NSA의 CNSA 1.0 요건을 정의한 RFC 9151을 준수하는 새로운 TLS 기반 보안 정책을 지원합니다. TLS 1.2 및 TLS 1.3 프로토콜에서 CNSA 1.0 TLS 보안 요건을 충족해야 하는 고객은 이제 ALB·NLB에서 해당 정책을 직접 적용할 수 있습니다.
- **[Amazon EC2 I8g 인스턴스, AWS 유럽(파리) 및 아시아 태평양(자카르타) 리전 출시](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-i8g-instances-aws-paris-jakarta-regions/)** — AWS Graviton4 프로세서 기반의 스토리지 최적화 Amazon EC2 I8g 인스턴스가 유럽(파리)과 아시아 태평양(자카르타) 리전에서 정식 출시되었습니다. 3세대 AWS Nitro SSD를 탑재하여 I4g 대비 TB당 실시간 스토리지 성능이 최대 65% 향상되고, 스토리지 I/O 지연 시간은 최대 50% 단축됩니다.

## 2026-08-01 · 전일 업데이트

- **[Amazon CloudWatch, 관리형 Prometheus 수집기 발표](https://aws.amazon.com/about-aws/whats-new/2026/07/cloudwatch-managed-collectors/)** — Amazon CloudWatch가 에이전트 배포 없이 Prometheus 지표를 수집할 수 있는 완전 관리형 수집기를 출시했습니다. 기존에는 자체 관리형 OpenTelemetry Collector를 직접 배포·운영해야 했으나, 이제 스크레이프 설정과 리소스 연결만 제공하면 CloudWatch가 프로비저닝과 스케일링을 자동으로 처리합니다.

## 2026-07-31 · 전일 업데이트

- **[AWS Direct Connect, Virtual Interface에서 BGP 경로 가시성 지원](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-direct-connect-bgp-visibility/)** — AWS Direct Connect가 프라이빗·트랜짓·퍼블릭 Virtual Interface에서 BGP 경로 가시성을 제공하여, AWS가 수락하거나 광고하는 경로를 AS 경로 및 BGP 커뮤니티 값과 함께 확인할 수 있게 되었습니다. 이를 통해 네트워크 관리자는 하이브리드 네트워크의 라우팅 문제 해결 및 경로 전파 검증을 보다 효율적으로 수행할 수 있습니다.
- **[AWS Transit Gateway, 정책 기반 라우팅(PBR) 정식 출시 발표](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-transit-gateway-policy-based-routing/)** — AWS Transit Gateway가 정책 기반 라우팅(PBR)을 정식 지원하여, 목적지 IP 주소만이 아닌 출발지·목적지 IP, 포트, 프로토콜 등 복합 패킷 속성을 기반으로 트래픽 전달 방향을 세밀하게 제어할 수 있게 되었습니다. 이로써 트래픽 스티어링이나 워크로드 격리를 위해 다중 VPC 아키텍처를 구성하던 복잡성과 운영 부담을 줄일 수 있습니다.

## 2026-07-30 · 전일 업데이트

- **[AWS Glue REST API 커넥터, VPC 지원·필터 푸시다운·파티션 지원 추가](https://aws.amazon.com/about-aws/whats-new/2026/07/aws-glue-rest-connector-filtering-partitioning-vpc)** — AWS Glue의 REST API 커넥터가 VPC 연결, 필터 푸시다운, 파티션 지원을 새롭게 제공합니다. 이를 통해 프라이빗 엔드포인트에 안전하게 연결하고, 필요한 데이터만 전송하며, 병렬 읽기로 수집 속도를 높이는 ETL 파이프라인을 커스텀 코드 없이 구성할 수 있습니다.

## 2026-07-29 · 전일 업데이트

- **[Amazon EKS, 클러스터 OIDC 엔드포인트에 AWS PrivateLink 지원 추가](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-eks-oidc-endpoint-privatelink)** — Amazon EKS 클러스터의 OIDC 디스커버리 및 JWKS 엔드포인트를 AWS PrivateLink를 통해 VPC 내부에서 인터넷 없이 비공개로 접근할 수 있게 되었습니다. 이를 통해 eksctl, Terraform, 커스텀 토큰 검증기 등 VPC 내 도구들이 인터페이스 VPC 엔드포인트를 생성하여 IRSA 관련 OIDC 문서와 JWKS를 안전하게 조회할 수 있습니다.

## 2026-07-28 · 전일 업데이트

- **[Amazon Neptune, IAM 태그 기반 액세스 제어 지원](https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-neptune-tbac/)** — Amazon Neptune Database가 IAM을 위한 태그 기반 액세스 제어(TBAC)를 지원하여, AWS 리소스 태그와 IAM 주체 태그를 IAM 정책 및 서비스 제어 정책(SCP)의 조건으로 활용해 데이터 플레인 작업에 대한 액세스를 제어할 수 있게 되었습니다. 이를 통해 대규모 다중 클러스터 환경에서 클러스터별 ARN을 일일이 열거하지 않고도 속성 기반으로 조직의 액세스 경계를 동적으로 적용할 수 있습니다.

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
