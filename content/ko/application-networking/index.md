# 애플리케이션 네트워킹 {#application-networking}

이 섹션에서는 애플리케이션 트래픽이 분산되는 방식, 서비스가 서로를 검색하고 통신하는 방식, 그리고 컨테이너 워크로드가 서비스 간 연결을 관리하는 방식을 다룹니다. 애플리케이션 네트워킹은 연결 계층 위에서 동작하며, 그 아래의 기반 인프라(VPC, 서브넷, IP 주소 지정)를 활용합니다.

여기서 다루는 애플리케이션 네트워킹 서비스는 "VPC 간 라우팅이 가능하다"와 "애플리케이션 코드가 호출을 수행한다" 사이에 위치하는 문제들을 처리합니다. 즉, 서비스 간 통신에서의 트래픽 분산, 서비스 검색, 인증, 트래픽 관리, 그리고 관측성(observability)이 이에 해당합니다.

## 1. 로드 밸런싱 {#1-load-balancing}

**Elastic Load Balancing**은 여러 대상에 트래픽을 분산하여 애플리케이션의 가용성을 유지하고, 수평 확장을 지원하며, 개별 대상의 장애를 흡수합니다. AWS는 세 가지 관리형 로드 밸런서를 제공하며, 이들은 서로 대체 가능하지 않습니다. 각각은 서로 다른 트래픽 유형과 아키텍처 내 역할을 위해 설계되었습니다.

**주요 서비스:**

*   **Application Load Balancer (ALB)** — 콘텐츠 기반 라우팅, TLS 종료, 상호 TLS, AWS WAF 통합을 지원하는 HTTP, HTTPS, gRPC용 L7 로드 밸런싱
*   **Network Load Balancer (NLB)** — 초고처리량, 클라이언트 IP 보존, 가용 영역별 고정 IP를 지원하는 TCP, UDP, TLS, QUIC용 L4 로드 밸런싱
*   **Gateway Load Balancer (GWLB)** — 서드파티 네트워크 어플라이언스(방화벽, IDS/IPS)를 데이터 경로에 투명하게 삽입하며, ALB 및 NLB와 구조적으로 다름

***핵심 인사이트:*** *ALB와 NLB는 대상에 애플리케이션 트래픽을 분산합니다. GWLB는 근본적으로 다른 역할을 수행합니다. 서드파티 어플라이언스 플릿을 데이터 경로에 투명하게 삽입하는 것입니다. GWLB를 ALB나 NLB와 동등한 위치로 취급하는 것이 가장 흔한 혼동의 원인입니다.*

## 2. 서비스 간 통신 {#2-service-to-service}

**서비스 간 통신(Service-to-service communication)**은 어느 정도 규모가 있는 애플리케이션이라면 그 연결 조직입니다. 흥미로운 질문이 "ALB냐 NLB냐?"인 경우는 드뭅니다. 오히려 "소비자는 공급자를 어떻게 찾는가?", "서비스는 서로를 어떻게 인증하는가?", "대상이 실패하면 어떻게 되는가?", "새 버전을 안전하게 배포하려면 어떻게 해야 하는가?"입니다.

**주요 패턴:**

*   **서비스 검색** — Route 53 프라이빗 호스팅 영역, AWS Cloud Map, Amazon VPC Lattice DNS
*   **인증 및 권한 부여** — SigV4를 사용하는 Amazon VPC Lattice 인증 정책, 보안 그룹, 상호 TLS
*   **트래픽 관리** — Amazon VPC Lattice 가중치 기반 라우팅, ALB 가중치 기반 대상 그룹, Route 53 가중치 기반 레코드
*   **크로스 VPC 및 크로스 계정 액세스** — Amazon VPC Lattice 서비스 네트워크, AWS PrivateLink 엔드포인트 서비스, 기존 연결을 통한 내부 로드 밸런서
*   **비동기 패턴** — 프라이빗 API에 직접 연결하는 Amazon EventBridge 및 AWS Step Functions

***핵심 인사이트:*** *각 패턴은 팀이 통합을 직접 담당하는 개별 빌딩 블록(Route 53, PrivateLink, ALB, IAM)으로 구성하거나, 검색·인증·크로스 VPC 도달성·트래픽 관리·관측성을 단일 관리형 계층으로 통합하는 Amazon VPC Lattice를 통해 처리할 수 있습니다.*

## 3. 컨테이너 메시 {#3-container-mesh}

**컨테이너 메시(Container mesh)**는 컨테이너화된 워크로드가 서비스 간 통신을 처리하는 방식을 다룹니다. 클러스터 내 기본 요소부터 클러스터 간 연결, 완전한 서비스 메시 배포까지 포괄합니다. 핵심 질문은 "어떤 특정 기능이 필요하며, 각 기능은 어디에 위치해야 하는가?"입니다.

**주요 패턴:**

*   **클러스터 내 컨테이너 네트워킹** — Amazon VPC CNI, Pod Identity, 파드용 보안 그룹, Amazon ECS Service Connect, awsvpc 네트워크 모드
*   **메시의 대안으로서의 Amazon VPC Lattice** — 메시 컨트롤 플레인 없이 AWS Gateway API Controller를 통한 클러스터 간, VPC 간, 계정 간 서비스 통신
*   **자체 관리형 서비스 메시** — 사이드카 메시 기능이 실제로 필요한 경우, Amazon VPC Lattice 또는 기존 AWS 연결 위에서 Istio, Cilium, Linkerd 실행

***핵심 인사이트:*** *사람들이 서비스 메시를 도입하는 이유가 되는 대부분의 기능은 이미 AWS 관리형 서비스로 기본 제공됩니다. 특정 사이드카 메시 기능(메시 관리형 mTLS 수명 주기, 메시 CRD, 요청별 복원력 정책)이 실제 요구 사항인 경우에만 자체 관리형 메시를 도입하세요.*

---

## 애플리케이션 네트워킹 주제 탐색 {#explore-application-networking-topics}

<div class="grid cards" markdown>

*   :material-scale-balance: **로드 밸런싱**

    ---

    ALB, NLB, GWLB: 각각의 사용 시기, 모범 사례, 헬스 체크, 가용 영역 복원력, 그리고 조합 방법.

    [:octicons-arrow-right-24: 로드 밸런싱](load-balancing.md)

*   :material-swap-horizontal: **서비스 간 통신**

    ---

    서비스 검색, 인증, 트래픽 관리, 관측성, 크로스 VPC 액세스, 비동기 패턴.

    [:octicons-arrow-right-24: 서비스 간 통신](service-to-service.md)

*   :material-hexagon-multiple: **컨테이너 메시**

    ---

    클러스터 내 네트워킹, 컨테이너를 위한 Amazon VPC Lattice, AWS 위의 자체 관리형 메시.

    [:octicons-arrow-right-24: 컨테이너 메시](container-mesh.md)

</div>
