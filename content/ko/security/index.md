# 보안 {#security}

이 섹션에서는 AWS 네트워크를 모든 계층에서 보호하는 방법을 다룹니다. 글로벌 엣지부터 개별 리소스까지, 인바운드 트래픽부터 아웃바운드 연결까지, 그리고 네트워크 수준의 격리부터 자격 증명 기반 액세스 제어까지 아우릅니다. AWS의 네트워크 보안은 경계에 단일 방화벽을 두는 방식이 아닙니다. 각 계층이 다른 계층에서 놓친 위협을 잡아내는, 중첩된 제어 체계로 구성됩니다.

여기서 다루는 보안 제어는 연결성 및 애플리케이션 네트워킹 계층 위에서 동작합니다. VPC 구조, 서브넷 티어, 연결 패턴을 이미 설계했다고 가정합니다. 보안은 완성된 아키텍처에 사후에 적용하는 것이 아닙니다 — 보안은 처음부터 아키텍처를 형성하며, 서브넷 설계(전용 방화벽 티어), 라우팅 테이블 구성(검사를 통한 트래픽 유도), 계정 구조(가장 강력한 경계로서의 격리)에 영향을 미칩니다.

## 1. 경계 제어 {#1-perimeter-controls}

**경계 제어(Perimeter Controls)**는 무단 인바운드 액세스로부터 네트워크 경계를 보호합니다. AWS에서 경계는 단일 방화벽이 아닙니다 — 글로벌 엣지 네트워크부터 개별 ENI까지, 스택의 여러 수준에서 동작하는 계층형 제어입니다.

**주요 서비스:**

*   **보안 그룹** — 스테이트풀(Stateful), ENI별 액세스 제어; 모든 워크로드의 기본 메커니즘
*   **Network ACLs** — 심층 방어를 위한 스테이트리스(Stateless), 서브넷 수준의 거부 규칙
*   **AWS WAF** — CloudFront, ALB, API Gateway에서의 L7 요청 검사
*   **AWS Shield** — DDoS 보호 (Standard는 자동 적용, Advanced는 고급 티어 제공)
*   **AWS Network Firewall** — VPC 경계에서의 관리형 스테이트풀/스테이트리스 검사
*   **Gateway Load Balancer** — 서드파티 방화벽 어플라이언스의 투명한 삽입
*   **AWS Firewall Manager** — 모든 계정에 걸친 중앙 집중식 정책 관리

***핵심 인사이트:*** *보안 그룹이 기본 액세스 제어 수단입니다 — NACL도, Network Firewall도 아닙니다. 보안 그룹 설계를 올바르게 하면, 나머지 계층은 보완 제어가 아닌 안전망 역할을 하게 됩니다.*

## 2. 아웃바운드 제어 {#2-outbound-controls}

**아웃바운드 제어(Outbound Controls)**는 워크로드가 인터넷에서 접근할 수 있는 대상과, 트래픽이 환경을 떠나기 전에 필터링되는 방식을 결정합니다. 핵심 원칙은 아웃바운드 기본 거부, 예외적 허용입니다.

**주요 서비스:**

*   **보안 그룹 (아웃바운드 규칙)** — ENI 수준에서의 포트 및 프로토콜 제한
*   **Route 53 DNS Firewall** — DNS 확인 계층에서의 도메인 기반 필터링; 가장 저렴하고 빠른 이그레스 제어
*   **AWS Network Firewall (이그레스 규칙)** — 스테이트풀 검사, IPS 시그니처, SNI 기반 도메인 필터링
*   **VPC Endpoints** — AWS 서비스 트래픽(S3, DynamoDB 등)의 이그레스를 완전히 제거
*   **AWS Network Firewall Proxy (미리 보기)** — 아웃바운드 웹 트래픽을 위한 관리형 명시적 포워드 프록시

***핵심 인사이트:*** *DNS Firewall은 모든 VPC에 가장 먼저 배포해야 할 이그레스 제어입니다 — 가장 낮은 비용으로 가장 넓은 위협 표면을 커버하며, 이그레스가 중앙 집중식이든 분산형이든 관계없이 동작합니다.*

## 3. 네트워크 세분화 {#3-network-segmentation}

**네트워크 세분화(Network Segmentation)**는 네트워크를 여러 계층에서 격리된 세그먼트로 분할하여 장애 반경(blast radius)을 제한합니다. AWS는 계정 수준 격리(가장 강력한 경계)부터 요청별 자격 증명 기반 액세스 제어(가장 세분화된 수준)까지 세분화를 제공합니다.

**주요 메커니즘:**

*   **AWS Accounts** — 가장 강력한 격리: IAM, 네트워크, 청구 경계를 완전히 분리
*   **VPCs** — 암묵적인 크로스-VPC 라우팅이 없는 네트워크 수준 격리
*   **Cloud WAN Segments / Transit Gateway Route Tables** — 정책 기반 라우팅 도메인 세분화
*   **보안 그룹** — 참조 기반 규칙을 활용한 마이크로 세분화
*   **VPC Lattice Auth Policies** — 네트워크 위치와 무관한 자격 증명 기반 세분화
*   **Service Insertion** — Cloud WAN 또는 Transit Gateway 라우팅을 통한 세그먼트 간 Network Firewall 검사

***핵심 인사이트:*** *가장 저렴한 세분화가 가장 강력합니다: 계정 및 VPC 격리는 비용이 들지 않습니다. 먼저 올바른 계정 구조에 투자하고, 세그먼트 간 연결이 필요한 경우에만 라우팅 계층 세분화를 추가하세요.*

---

## 보안 주제 살펴보기 {#explore-security-topics}

<div class="grid cards" markdown>

*   :material-shield: **경계 제어**

    ---

    인바운드 보호를 위한 보안 그룹, NACL, AWS WAF, Shield, Network Firewall, GWLB, Firewall Manager.

    [:octicons-arrow-right-24: 경계 제어](perimeter-inbound.md)

*   :octicons-sign-out-16: **아웃바운드 제어**

    ---

    DNS Firewall, Network Firewall 이그레스 규칙, VPC 엔드포인트, 데이터 유출 방지 패턴.

    [:octicons-arrow-right-24: 아웃바운드 제어](outbound.md)

*   :material-chart-pie: **네트워크 세분화**

    ---

    계정 격리, Cloud WAN 세그먼트, 보안 그룹 마이크로 세분화, VPC Lattice를 활용한 제로 트러스트 패턴.

    [:octicons-arrow-right-24: 네트워크 세분화](segmentation.md)

</div>
