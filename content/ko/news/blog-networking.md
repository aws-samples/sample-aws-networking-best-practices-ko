---
hide:
  - toc
---
# AWS Networking & Content Delivery 블로그 (한국어 요약)

[AWS Networking & Content Delivery Blog](https://aws.amazon.com/blogs/networking-and-content-delivery/)(영문)의 글을 **매주 금요일** 최근 올라온 신규 글 위주로 한국어 요약합니다. 원문은 각 항목의 링크에서 확인하세요. 최신 항목이 맨 위에 표시됩니다.

<!-- NEWS:INSERT -->

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
