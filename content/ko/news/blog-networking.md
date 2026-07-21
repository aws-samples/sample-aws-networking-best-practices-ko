---
hide:
  - toc
---
# AWS Networking & Content Delivery 블로그 (한국어 요약)

[AWS Networking & Content Delivery Blog](https://aws.amazon.com/blogs/networking-and-content-delivery/)(영문)의 글을 **매주 금요일** 최근 올라온 신규 글 위주로 한국어 요약합니다. 원문은 각 항목의 링크에서 확인하세요. 최신 항목이 맨 위에 표시됩니다.

<!-- NEWS:INSERT -->

## 2026-07-21 · 주간 요약

- **[LBC Ingress에서 Gateway API로 마이그레이션하는 툴킷 소개](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-the-lbc-ingress-to-gateway-api-migration-toolkit/)** — AWS Load Balancer Controller(LBC)의 Ingress 리소스를 Gateway API로 수동 전환할 때 발생하는 어노테이션·경로 규칙·TLS 설정 재작성 오류를 방지하기 위해, 검증된 가이드 방식의 마이그레이션 툴킷이 출시되었습니다. 이 툴킷은 프로덕션 트래픽 중단 위험을 줄이면서 안전하게 Gateway API로 전환할 수 있는 경로를 제공합니다.

## 2026-07-18 · 주간 요약

- **[AWS에서 엑스트라넷 구축: 안전하고 확장 가능한 파트너 연결](https://aws.amazon.com/blogs/networking-and-content-delivery/building-extranet-on-aws-secure-scalable-partner-connectivity/)** — 외부 파트너와 AWS 인프라 간 엑스트라넷 연결 시 발생하는 IP 주소 중복, 비용 증가, 커뮤니케이션 불일치 문제를 해결하는 안전하고 확장 가능한 복원력 있는 아키텍처 패턴을 소개합니다. 이 참조 아키텍처는 일반적인 설계에서 흔히 나타나는 문제를 최소화하는 데 초점을 맞춥니다.

## 2026-07-17 · 주간 요약

- **[AWS Client VPN의 Client VPN Route Enforcement로 VPN 트래픽 누출 방지](https://aws.amazon.com/blogs/networking-and-content-delivery/prevent-vpn-traffic-leaks-with-client-vpn-route-enforcement-in-aws-client-vpn/)** — AWS Client VPN에 Client VPN Route Enforcement 기능이 추가되어, 관리자가 정의한 라우팅 규칙이 클라이언트 디바이스에서 임의로 변경되는 것을 방지할 수 있게 되었습니다. 이를 통해 원격 액세스 환경에서 의도치 않은 트래픽 누출 위험을 줄이고 VPN 터널의 라우팅 무결성을 유지할 수 있습니다.

## 2026-07-16 · 주간 요약

- **[Amazon EC2에서 Layer 2 네트워킹 설정하기](https://aws.amazon.com/blogs/networking-and-content-delivery/setting-up-layer-2-networking-on-amazon-ec2/)** — Amazon VPC가 기본적으로 지원하지 않는 Layer 2 네트워크 통신이 필요한 워크로드(산업 제어 시스템 등)를 Amazon EC2에서 실행하는 방법을 소개합니다. 적절한 접근 방식을 통해 L2 의존성을 가진 워크로드를 AWS 환경으로 마이그레이션할 수 있습니다.
- **[IAM 조건 키를 활용한 세분화된 Amazon Route 53 액세스 제어 (3부)](https://aws.amazon.com/blogs/networking-and-content-delivery/fine-grained-amazon-route-53-access-with-iam-condition-keys-part-3/)** — 공유 환경에서 페더레이션 사용자에게 DNS 레코드 액세스를 부여할 때 발생하는 과도한 권한 문제를 해결하기 위해, IAM 조건 키를 활용한 세분화된 Amazon Route 53 액세스 제어 방법을 시리즈 3부에서 이어서 설명합니다. 이를 통해 운영 부담을 줄이고 최소 권한 원칙을 유지할 수 있습니다.
- **[CloudFront VPC Origins와 차세대 OpenSearch Serverless를 활용한 WebSocket 스트리밍 프라이빗 AI 에이전트](https://aws.amazon.com/blogs/networking-and-content-delivery/private-ai-agent-with-websocket-streaming-over-cloudfront-vpc-origins-and-the-next-generation-of-opensearch-serverless-for-knowledge-retrieval/)** — 파트너 계약서 검토를 자동화하기 위해 CloudFront VPC Origins를 통한 WebSocket 스트리밍과 차세대 OpenSearch Serverless 기반 지식 검색을 결합한 프라이빗 AI 에이전트 구축 방법을 소개합니다. 이 아키텍처는 민감한 문서를 외부에 노출하지 않고 안전하게 AI 추론을 수행할 수 있는 네트워킹 설계를 제시합니다.

## 2026-07-14 · 주간 요약

- **[CIDR 자동 확장: IP 고갈로 인한 다운타임 줄이기](https://aws.amazon.com/blogs/networking-and-content-delivery/automating-cidr-expansion-reducing-ip-exhaustion-downtime/)** — Amazon VPC의 IP 사용률을 모니터링하고 고갈 위험 감지 시 보조 CIDR과 새 서브넷을 자동으로 추가하는 서버리스 자동화 솔루션을 소개합니다. AWS Lambda, Step Functions, IPAM을 활용하며 IPAM 완전 관리·서브넷 전용·미사용 등 세 가지 운영 모드를 지원하고, SAM 명령 하나로 배포할 수 있습니다.

## 2026-07-09 · 주간 요약

- **[United Airlines가 Private NAT Gateway로 IP 고갈 문제를 해결한 방법](https://aws.amazon.com/blogs/networking-and-content-delivery/how-united-airlines-solved-ip-exhaustion-with-private-nat-gateway/)** — United Airlines는 수백 개의 AWS VPC 운영 중 IP 주소 고갈 문제에 직면했으며, Private NAT Gateway를 도입해 중복 CIDR 환경에서도 VPC 간 통신을 가능하게 하고 확장성을 확보했습니다.

## 2026-07-08 · 주간 요약

- **[AWS Lambda@Edge와 Amazon DynamoDB를 활용한 지능형 페일오버](https://aws.amazon.com/blogs/networking-and-content-delivery/intelligent-failover-using-aws-lambdaedge-and-amazon-dynamodb/)** — 리전 장애 발생 시 사용자를 동적으로 다른 엔드포인트로 전환하는 지능형 페일오버 솔루션을 소개합니다. Lambda@Edge와 DynamoDB를 결합해 사용자-엔드포인트 간 지속적 관계를 유지하면서 고가용성을 확보하는 참조 아키텍처를 제시합니다.

## 2026-07-07 · 주간 요약

- **[IAG가 Amazon VPC Lattice로 서비스 간 통신을 가속화한 방법](https://aws.amazon.com/blogs/networking-and-content-delivery/how-iag-accelerated-service-to-service-communication-with-amazon-vpc-lattice/)** — 호주·뉴질랜드 최대 손해보험사인 IAG가 서버리스 기반 디지털 엔지니어링 플랫폼에서 마이크로서비스 간 통신을 개선하기 위해 Amazon VPC Lattice를 도입한 사례를 소개합니다. VPC Lattice를 활용해 통합된 패턴과 일관된 거버넌스를 유지하면서 서비스 간 연결을 단순화하고 가속화했습니다.

## 2026-07-01 · 주간 요약

- **[Terraform과 Network MCP Server를 활용한 AWS Transit Gateway에서 AWS Cloud WAN으로의 단계적 마이그레이션](https://aws.amazon.com/blogs/networking-and-content-delivery/phased-aws-transit-gateway-to-aws-cloud-wan-migration-with-terraform-and-network-mcp-server/)** — 6단계 Terraform 접근 방식과 AWS Network MCP Server 검증을 통해 여러 리전에 걸쳐 AWS Transit Gateway에서 AWS Cloud WAN으로 단계적으로 마이그레이션하는 방법을 소개합니다. 이를 통해 복잡한 멀티 리전 네트워크 전환 작업을 체계적으로 수행하고 운영 위험을 줄일 수 있습니다.
- **[지능형 VPN 관측성: AWS Site-to-Site VPN 로그 분석](https://aws.amazon.com/blogs/networking-and-content-delivery/intelligent-vpn-observability-decoding-aws-site-to-site-vpn-logs/)** — AWS Site-to-Site VPN 연결 장애 시 수백 개의 로그 항목을 수동으로 분석하던 작업을 개선하기 위해, BGP 상태 전환과 IKE 단계 변경을 자동으로 연관 분석하여 프리픽스 할당량 위반, AS 경로 루프, 홀드 타이머 만료 등의 원인을 신속하게 파악하는 방법을 다룹니다. 이를 통해 반복적인 수동 작업을 줄이고 복구 시간을 단축할 수 있습니다.

## 2026-06-30 · 주간 요약

- **[AWS Cloud WAN 라우팅 정책: 실제 글로벌 네트워크 시나리오 – 2부](https://aws.amazon.com/blogs/networking-and-content-delivery/aws-cloud-wan-routing-policy-real-world-global-network-scenarios-part-2/)** — AWS Cloud WAN 라우팅 정책의 세 가지 핵심 구성 요소(매칭 조건, 액션, 경로 요약)를 활용해 글로벌 네트워크에서 경로 전파와 경로 선택을 세밀하게 제어하는 실제 시나리오를 다룬 2부 시리즈입니다. 1부에서 소개한 개념을 바탕으로 복잡한 멀티 리전 네트워크 환경에서의 라우팅 정책 적용 방법을 구체적으로 설명합니다.
- **[Amazon ECS 위트니스를 활용한 RADIUS용 NLB 헬스 체크 확장](https://aws.amazon.com/blogs/networking-and-content-delivery/extending-nlb-health-checks-for-radius-using-an-amazon-ecs-witness/)** — Network Load Balancer의 기본 헬스 체크는 RADIUS 서버의 도달 가능성만 확인할 뿐 실제 인증 가능 여부는 검증하지 못하는 한계가 있습니다. 이 게시물은 단일 Amazon ECS 위트니스가 애플리케이션 계층 RADIUS 프로브를 실행하고 NLB 대상 그룹 멤버십을 직접 조정하는 오픈 소스 참조 솔루션을 통해 이 문제를 해결하는 방법을 소개합니다.

## 2026-06-23 · 주간 요약

- **[VPC 리소스 게이트웨이: 구현 패턴과 활용 사례](https://aws.amazon.com/blogs/networking-and-content-delivery/vpc-resource-gateways-implementation-patterns-and-use-cases/)** — 기존 AWS PrivateLink 공급자-소비자 모델에 맞지 않거나 IP 주소 공간이 겹치는 환경에서 VPC 간 서비스 연결이 필요할 때 VPC 리소스 게이트웨이를 활용하는 구현 패턴과 사례를 소개합니다. VPC 피어링이나 AWS Transit Gateway만으로는 해결하기 어려운 복잡한 네트워킹 문제를 해소하는 방법을 다룹니다.
- **[SD-WAN 세분화를 AWS Cloud WAN으로 확장하기 – 2부](https://aws.amazon.com/blogs/networking-and-content-delivery/extending-sd-wan-segmentation-into-aws-cloud-wan-part-2/)** — SD-WAN 세분화를 AWS Cloud WAN으로 확장하는 두 편 시리즈의 2부로, 1부에서 다룬 GRE 기반 Connect 어태치먼트에 이어 멀티테넌트·규제 환경에서 엄격한 네트워크 세분화를 유지하는 구성 방법을 설명합니다. 보안·컴플라이언스 요건을 충족하면서 SD-WAN과 AWS 클라우드 네트워크를 통합하는 방법에 초점을 맞춥니다.
- **[SD-WAN 세분화를 AWS Cloud WAN으로 확장하기 – 1부](https://aws.amazon.com/blogs/networking-and-content-delivery/extending-sd-wan-segmentation-into-aws-cloud-wan-part-1/)** — 멀티테넌트·규제 환경 또는 여러 사업부를 운영하는 조직이 SD-WAN 가상 어플라이언스를 배포하고 AWS Cloud WAN을 통해 네트워크 세분화를 확장하는 방법을 소개하는 두 편 시리즈의 1부입니다. 단일하고 확장 가능한 글로벌 네트워크 아래 세분화된 환경을 통합하는 아키텍처를 다룹니다.
- **[VPC Block Public Access를 활용한 AWS IPv6 인프라 보안 모범 사례](https://aws.amazon.com/blogs/networking-and-content-delivery/best-practices-for-securing-your-ipv6-infrastructure-on-aws-using-vpc-block-public-access/)** — AWS에서 프라이빗 IPv6 리소스를 보호하면서 연결 모델의 유연성을 유지하는 모범 사례와 고려 사항을 다룹니다. VPC Block Public Access를 활용해 IPv6 네트워크 및 애플리케이션 인프라를 안전하게 구성하는 방법을 설명합니다.
- **[AWS Verified Access와 AWS Network Firewall을 활용한 제로 트러스트 액세스 보안](https://aws.amazon.com/blogs/networking-and-content-delivery/securing-zero-trust-access-with-aws-verified-access-and-aws-network-firewall/)** — 기존 VPN의 과도한 네트워크 액세스 허용 문제를 해결하기 위해 AWS Verified Access와 AWS Network Firewall을 결합해 ID 기반 액세스 제어와 세밀한 트래픽 검사를 제공하는 제로 트러스트 솔루션을 소개합니다. 내부 애플리케이션에 대한 액세스를 의도된 범위로 제한하고 보안을 강화하는 구성 방법을 설명합니다.
- **[인터넷 연결 로드 밸런서를 위한 내부 DNS 영역 배포](https://aws.amazon.com/blogs/networking-and-content-delivery/deploying-internal-dns-zones-for-internet-facing-load-balancers/)** — 인터넷 연결 Elastic Load Balancing에 프라이빗 호스팅 영역을 활용해 내부 DNS를 구성하는 방법을 다룹니다. Network Load Balancer, Application Load Balancer, Gateway Load Balancer 등 다양한 ELB 유형에 맞는 DNS 배포 패턴을 설명합니다.
- **[S3 로그와 커스텀 MCP로 AWS DevOps Agent 네트워크 조사 기능 확장 (Amazon Bedrock AgentCore 활용)](https://aws.amazon.com/blogs/networking-and-content-delivery/extending-aws-devops-agent-network-investigations-with-s3-logs-and-custom-mcp-on-amazon-bedrock-agentcore/)** — AWS Application Load Balancer에서 502 오류가 발생했을 때 API 수준 조사를 넘어 Amazon S3에 저장된 로그와 커스텀 MCP를 Amazon Bedrock AgentCore에 연결해 근본 원인을 분석하는 방법을 소개합니다. 네트워킹 장애 대응 시 AI 기반 에이전트로 조사 범위를 확장하는 실용적인 접근법을 제시합니다.
