# 연결(Connectivity) {#connectivity}

이 섹션에서는 AWS 리소스가 인터넷, 다른 리소스, 그리고 AWS 외부 네트워크와 통신하는 방법을 다룹니다. 연결은 기반 인프라(VPC, 서브넷, IP 주소 지정)와 그 위에서 실행되는 애플리케이션 네트워킹 서비스 사이의 계층입니다.

선택하는 연결 패턴은 전체 AWS 환경의 비용, 지연 시간, 보안 경계, 운영 책임에 영향을 미칩니다. 대부분의 조직은 여러 연결 서비스를 동시에 사용하며, 각 서비스는 가장 큰 가치를 제공하는 계층에서 동작합니다.

**각 페이지의 관계:** 인터넷 연결은 외부 경계(트래픽이 AWS에 들어오고 나가는 방식)를 다룹니다. AWS 내부 연결은 VPC와 계정 간의 내부 라우팅 및 서비스 통신을 다룹니다. 하이브리드 및 멀티 클라우드 연결은 AWS 외부 네트워크(온프레미스 데이터 센터 및 다른 클라우드 공급자)와의 연결을 다룹니다. 원격 액세스는 인가된 사용자와 디바이스가 내부 애플리케이션에 액세스하는 방법을 다룹니다. 대부분의 아키텍처는 네 페이지 모두에 걸쳐 있습니다. 공개 워크로드에는 인터넷 연결, 워크로드 간 백본에는 AWS 내부 연결, 온프레미스 및 멀티 클라우드 구간에는 하이브리드 연결, 임직원 접속에는 원격 액세스를 활용합니다.

!!! tip "VPC Lattice 다루는 범위"
    Amazon VPC Lattice는 의도적으로 두 곳에서 다룹니다. [AWS 내부 연결](within-aws.md) 페이지에서는 연결 및 네트워크 팀 관점에서 VPC Lattice를 다룹니다. 서비스 네트워크, 연결 모델, 그리고 VPC Lattice가 연결 스택에서 차지하는 위치를 설명합니다. [애플리케이션 네트워킹 → 서비스 간 통신](../application-networking/service-to-service.md) 페이지에서는 애플리케이션 팀 관점에서 VPC Lattice를 다룹니다. 서비스 검색, 인증 정책, 트래픽 관리, 배포 패턴을 설명합니다.

## 1. 인터넷 연결 {#1-internet-connectivity}

**인터넷 연결**은 두 가지 관심사를 다룹니다. **인그레스(ingress)**(외부 클라이언트가 AWS에서 호스팅되는 애플리케이션에 액세스하는 방법)와 **이그레스(egress)**(AWS 리소스가 인터넷의 외부 서비스에 액세스하는 방법)입니다. 각각에 적합한 패턴은 서로 다른 기준에 따라 결정되며, 한쪽에서 내린 결정이 다른 쪽에 그대로 적용되는 경우는 드뭅니다.

**주요 결정 사항:**

*   **인그레스: 분산형 vs 중앙 집중식** — 분산형(각 VPC가 자체 인그레스를 소유)이 권장 기본값이며, 중앙 집중식(공유 인그레스 VPC)은 특정 컴플라이언스 요건이 있는 경우에만 사용합니다.
*   **이그레스: IPv6 vs IPv4** — IPv6 이그레스는 설계상 분산형(VPC별 이그레스 전용 인터넷 게이트웨이)이며, IPv4 이그레스는 분산형과 중앙 집중식 패턴 사이에서 실질적인 트레이드오프가 존재합니다.
*   **엣지 서비스** — Amazon CloudFront, AWS Global Accelerator, AWS WAF는 인그레스 패턴에 관계없이 중앙에서 관리되는 보호 기능을 제공합니다.

***핵심 인사이트:*** *인그레스의 경우, AWS 엣지(CloudFront, AWS WAF, VPC별 방화벽 엔드포인트)가 사실상 중앙에서 관리되는 글로벌 분산 경계가 됩니다. 이로 인해 모든 트래픽을 공유 리전 인그레스 VPC를 통해 라우팅해야 했던 기존의 이유가 사라집니다.*

## 2. AWS 내부 연결 {#2-connectivity-within-aws}

**AWS 내부 연결**은 VPC, 계정, 리전이 서로 통신하는 방법을 다룹니다. 관련 서비스는 두 가지 상호 보완적인 계층에서 동작합니다. 네트워크 수준 연결(VPC가 트래픽을 라우팅하는 방법)과 애플리케이션 수준 연결(서비스가 서로를 검색하고 통신하는 방법)입니다.

**주요 서비스:**

*   **AWS Cloud WAN** — 선언적 세분화를 통한 정책 기반 글로벌 네트워크 관리
*   **Amazon VPC Lattice** — IAM 기반 인증을 갖춘 애플리케이션 계층 서비스 간 통신
*   **VPC Lattice VPC Resources** — 데이터베이스, 온프레미스 엔드포인트, 서드파티 서비스에 대한 프라이빗 TCP 액세스
*   **AWS Transit Gateway** — VPC, VPN, Direct Connect를 위한 리전 허브 앤 스포크 라우팅
*   **AWS PrivateLink** — AWS 서비스에 대한 프라이빗 액세스 및 다른 계정에 자체 서비스 노출
*   **VPC Peering** — 특정하고 정당한 이유가 있는 VPC 쌍을 위한 직접 지점 간 연결

***핵심 인사이트:*** *이 서비스들은 서로 경쟁하는 대안이 아니라 상호 보완적인 계층입니다. 각 서비스가 가장 큰 가치를 제공하는 계층에서 동작하도록 연결 스택을 구성하세요.*

## 3. 하이브리드 및 멀티 클라우드 연결 {#3-hybrid-and-multi-cloud-connectivity}

**하이브리드 및 멀티 클라우드 연결**은 두 가지 관심사를 다룹니다. 온프레미스 데이터 센터와 지사를 AWS에 연결하는 것(하이브리드)과 AWS를 다른 퍼블릭 클라우드에 연결하는 것(멀티 클라우드)입니다.

**주요 서비스:**

*   **AWS Direct Connect** — 예측 가능한 대역폭과 지연 시간을 위한 전용 프라이빗 회선. 대부분의 프로덕션 하이브리드 배포의 기반
*   **AWS Site-to-Site VPN** — 인터넷을 통한 암호화된 IPsec 연결. 하이브리드 연결을 가장 빠르게 구축하는 방법
*   **SD-WAN 통합** — 기존 SD-WAN 오버레이를 위한 Transit Gateway Connect 또는 AWS Cloud WAN Connect 연결
*   **AWS Interconnect** — 관리형 직접 클라우드 간 연결(현재 AWS ↔ Google Cloud 지원, 확장 예정)

***핵심 인사이트:*** *대부분의 조직은 이 서비스들을 동시에 둘 이상 사용합니다. 기본 프라이빗 경로에는 Direct Connect, 빠른 시작 또는 암호화 오버레이에는 VPN, 기존 지사 오버레이에는 SD-WAN Connect를 활용합니다.*

## 4. 원격 액세스 {#4-remote-access}

**원격 액세스**는 인가된 사용자와 디바이스가 내부 AWS 애플리케이션에 액세스하는 방법을 다룹니다. 이는 인프라 연결과는 별개의 결정 영역으로, 네트워크 엔지니어링이 아닌 ID 및 보안 팀을 위한 것이며, 환경에 하이브리드 연결이 있는지 여부와 무관하게 동작합니다.

**주요 서비스:**

*   **AWS Verified Access** — 요청별 ID 및 디바이스 보안 상태 평가를 통한 제로 트러스트 애플리케이션 수준 액세스. 새로운 사용 사례에 권장되는 옵션
*   **AWS Client VPN** — VPC 내에서 라우팅 가능한 IP가 실제로 필요한 경우를 위한 네트워크 수준 사용자 액세스

***핵심 인사이트:*** *모든 새로운 애플리케이션 액세스 사용 사례에는 AWS Verified Access를 먼저 검토하세요. 애플리케이션이 사용자에게 VPC 내부의 라우팅 가능한 IP가 실제로 필요한 경우에만 Client VPN을 사용하세요.*

---

## 연결 주제 살펴보기 {#explore-connectivity-topics}

<div class="grid cards" markdown>

*   :material-web: **인터넷 연결**

    ---

    인그레스 및 이그레스 패턴, 분산형 vs 중앙 집중식 아키텍처, 엣지 서비스, NAT 게이트웨이, 이그레스 필터링.

    [:octicons-arrow-right-24: 인터넷 연결](internet.md)

*   :material-aws: **AWS 내부 연결**

    ---

    AWS Cloud WAN, Amazon VPC Lattice, Transit Gateway, PrivateLink, VPC Peering, 그리고 이를 조합하는 방법.

    [:octicons-arrow-right-24: AWS 내부 연결](within-aws.md)

*   :material-cloud-sync: **하이브리드 및 멀티 클라우드 연결**

    ---

    온프레미스 및 멀티 클라우드 인프라 연결을 위한 Direct Connect, Site-to-Site VPN, SD-WAN, AWS Interconnect.

    [:octicons-arrow-right-24: 하이브리드 및 멀티 클라우드 연결](hybrid-multicloud.md)

*   :material-account-lock: **원격 액세스**

    ---

    제로 트러스트 애플리케이션 액세스를 위한 AWS Verified Access와 네트워크 수준 사용자 연결을 위한 AWS Client VPN.

    [:octicons-arrow-right-24: 원격 액세스](remote-access.md)

</div>
