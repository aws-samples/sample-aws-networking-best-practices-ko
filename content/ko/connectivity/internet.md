# 인터넷 연결 {#internet-connectivity}

!!! info "사전 요구 사항"
    이 섹션은 [Amazon VPC](../foundation/vpc.md), [서브넷](../foundation/subnets.md), 그리고 [AWS 내부 연결](within-aws.md) 서비스(특히 AWS Transit Gateway 및 AWS Cloud WAN)에 대한 이해를 전제로 합니다. AWS 네트워킹 기초가 처음이라면 해당 주제를 먼저 검토하세요.

인터넷 연결은 두 가지 서로 다른 관심사를 다루며, 각각에 적합한 패턴은 서로 다른 기준에 따라 결정됩니다. **인그레스 연결(Ingress connectivity)**은 외부 클라이언트를 AWS에서 호스팅하는 애플리케이션으로 연결합니다 — Amazon CloudFront의 450개 이상의 엣지 로케이션, 관리형 규칙 그룹에 따라 요청을 평가하는 AWS WAF, 그리고 자동으로 확장되는 VPC별 로드 밸런서를 통해 이루어집니다. **이그레스 연결(Egress connectivity)**은 AWS 리소스가 외부 서비스에 접근할 수 있도록 합니다 — 게이트웨이당 최대 100Gbps로 IPv4 트래픽을 처리하며 GB당 처리 요금이 부과되는 NAT 게이트웨이([NAT 게이트웨이 요금](https://aws.amazon.com/vpc/pricing/) 참조), 또는 무료로 무제한 IPv6 아웃바운드 액세스를 제공하는 이그레스 전용 인터넷 게이트웨이를 통해 이루어집니다. 한 방향에서 내린 결정이 다른 방향에 그대로 적용되는 경우는 드물기 때문에, 이 페이지에서는 두 가지를 별도로 다룹니다.

양방향 모두에 걸친 핵심 선택은 **중앙 집중식 vs. 분산형**입니다. 인그레스 또는 이그레스를 공유 VPC와 네트워크 팀을 통해 집중시킬 것인지, 아니면 각 애플리케이션을 소유한 팀에게 워크로드별로 분산시킬 것인지의 문제입니다. 올바른 답은 방향에 따라 다릅니다. 인그레스의 경우 분산형이 권장 기본값이며, 중앙 집중식은 특정 사례에 한해 사용합니다. 이그레스의 경우 비용, 운영 소유권, 검사 지점의 위치에 걸쳐 진정한 트레이드오프가 존재하며, 단일한 정답은 없습니다. 이러한 패턴을 결합한 권장 아키텍처는 이 페이지 하단의 [인터넷 연결 스택 구성](#building-your-internet-connectivity-stack)을 참조하세요.

![인그레스(분산형 권장, 중앙 집중식 옵션, 엣지 서비스)와 이그레스(IPv6 분산형, IPv4 패턴 선택, 필터링)를 보여주는 인터넷 인그레스 및 이그레스 개요](../assets/connectivity/internet-ingress-egress.png)
/// caption
인터넷 인그레스 및 이그레스 — [Drawio 소스](../assets/connectivity/internet-ingress-egress.drawio)
///

인그레스의 경우, 분산형 패턴은 각 애플리케이션의 인터넷 진입점을 워크로드를 소유한 VPC 및 계정 내에 유지합니다. 애플리케이션 팀은 자체 로드 밸런서, 인증서, 확장 결정을 직접 관리하며, 한 팀의 인그레스 장애가 다른 팀에 영향을 미치지 않습니다. 중앙 집중식 보호는 CloudFront, AWS WAF, 그리고 VPC별 레이어 3/4 검사(AWS Network Firewall 또는 서드파티 방화벽 어플라이언스를 사용하는 [Gateway Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html))를 통해 균일하게 적용되며, 이 모두는 [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html)를 통해 중앙에서 관리됩니다. AWS 엣지는 사실상 중앙에서 관리되는 전 세계적으로 분산된 경계가 되어, 모든 트래픽을 공유 리전 인그레스 VPC를 통해 라우팅해야 했던 기존의 이유를 없애줍니다. 공유 VPC를 통한 중앙 집중식 인그레스도 여전히 옵션으로 남아 있지만, 로드 밸런서 체이닝, 추가 트래픽 처리 비용, 공유 VPC의 장애 반경(blast radius)이 추가되는 반면, 클라우드 네이티브 분산형 패턴이 이미 제공하지 않는 보호 기능을 추가로 제공하지는 않습니다.

이그레스의 경우 선택이 더 복잡하며 IP 버전에 따라 나뉩니다. **IPv6 이그레스는 설계상 분산형**입니다. 각 VPC는 자체 이그레스 전용 인터넷 게이트웨이를 통해 인터넷에 접근하며, 이를 중앙화할 수 있는 관리형 NAT66은 존재하지 않습니다. **IPv4 이그레스**는 진정한 50-50 선택입니다. IPv4를 중앙화하면 VPC별 [NAT 게이트웨이](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)와 검사 엔드포인트를 하나의 공유 이그레스 VPC로 통합할 수 있지만, 모든 트래픽에 Transit Gateway 또는 AWS Cloud WAN 데이터 처리 요금이 추가되고 운영 소유권이 중앙 팀에 집중됩니다. IPv4를 분산화하면 각 VPC가 트랜짓 네트워크 요금 없이 독립적으로 운영되지만, 각 VPC가 자체 NAT 게이트웨이 비용을 부담하고 필요한 경우 VPC별 검사 비용도 지불해야 합니다. 균일한 정책은 두 패턴 모두에서 달성 가능합니다.

## 인그레스 연결 {#ingress-connectivity}

인그레스(Ingress)는 외부 클라이언트가 AWS에서 호스팅하는 애플리케이션에 접근하는 방식입니다. 두 가지 아키텍처 패턴이 있습니다. **분산형(decentralized)**은 각 애플리케이션이 자체 인터넷 진입점을 소유하는 방식이고, **중앙 집중식(centralized)**은 공유 인그레스 VPC가 여러 애플리케이션 앞단에 위치하는 방식입니다. 대부분의 환경에서는 분산형이 올바른 기본 선택입니다. 중앙 집중식 인그레스는 일반적인 모범 사례가 아니라 특정 상황에서만 정당화됩니다.

두 패턴은 프로토콜과 대체로 무관하지만, 각 패턴을 구현하는 서비스는 트래픽 유형에 따라 달라집니다. **L7 트래픽**(HTTP, HTTPS, gRPC 웹 애플리케이션, REST API 및 기타 애플리케이션 계층 워크로드)과 **L4 트래픽**(로드 밸런서가 HTTP 인식 디코딩 없이 전달해야 하는 TCP 및 UDP 서비스로, 게임, 금융 거래, 커스텀 프로토콜, 클라이언트 IP를 종단 간 보존해야 하는 서비스 포함)에 따라 사용하는 서비스가 다릅니다. 이어지는 각 하위 섹션에서 두 트래픽 유형에 해당하는 서비스를 설명합니다.

!!! note "기본 DDoS 보호"
    [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html) Standard는 분산형 또는 중앙 집중식 인그레스 패턴 채택 여부와 관계없이, 모든 공개 AWS 엔드포인트(CloudFront 배포, Global Accelerator, ALB, NLB, Route 53, AWS API 엔드포인트)에 자동으로 무료 적용됩니다. 아래 패턴은 애플리케이션 계층 보호 및 트래픽 셰이핑에 초점을 맞추며, 기본 볼류메트릭 DDoS 방어는 이미 적용되어 있습니다.

### 분산형 인그레스 (권장) {#decentralized-ingress-preferred}

분산형 모델에서는 인터넷 연결 애플리케이션을 호스팅하는 각 VPC가 자체 인그레스를 소유합니다. 애플리케이션 팀은 워크로드에 맞는 로드 밸런서 또는 API 엔드포인트를 선택하고, AWS Certificate Manager를 통해 자체 TLS 인증서를 관리하며, 다른 워크로드와 독립적으로 인그레스를 확장합니다. 인그레스 잘못 구성으로 인한 장애 반경(blast radius)은 해당 애플리케이션으로 한정됩니다.

분산형 인그레스에 대한 일반적인 우려 중 하나는 팀별 소유권이 보안 공백을 만드는지 여부입니다. 그렇지 않습니다. 중앙의 균일한 보호는 모든 워크로드 앞단에 여전히 적용되지만, 공유 인그레스 VPC가 아닌 AWS 엣지에서 이루어집니다.

* L7 트래픽의 경우, [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)와 [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html)가 모든 배포에 일관된 규칙 기준을 적용합니다.
* L4 트래픽의 경우, 각 워크로드 VPC의 **VPC별 방화벽 엔드포인트**가 인터넷 게이트웨이와 워크로드 진입점 사이에서 인그레스 트래픽을 검사합니다. 두 가지 옵션은 AWS 관리형 방화벽인 [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html)과 서드파티 방화벽 어플라이언스 플릿 앞단의 Gateway Load Balancer입니다. 어느 경우든 규칙 세트는 중앙에서 정의됩니다.

두 경우 모두 보호 정책은 중앙에서 정의하고 관리하며, 분산되는 것은 데이터 플레인입니다. AWS 엣지와 VPC별 방화벽 엔드포인트는 함께 완전히 분산된 중앙 관리형 경계(전통적인 네트워크에서 DMZ가 수행하는 역할)를 형성하며, 공유 리전 VPC를 통해 모든 흐름을 라우팅하는 운영 비용 없이 이를 달성합니다.

**분산형이 권장되는 이유**:

<div class="grid cards" markdown>

*   :material-shield-check: **제한된 장애 도메인**

    ---

    잘못 구성된 리스너, 소진된 대상 그룹, 또는 만료된 인증서는 조직의 모든 인터넷 연결 워크로드가 아닌 하나의 애플리케이션에만 영향을 미칩니다.

*   :material-account-group: **팀 자율성과 소유권**

    ---

    워크로드를 구축하는 애플리케이션 팀이 인그레스도 운영하므로, 일상적인 변경을 조율하기 위한 팀 간 의존성이 없습니다.

*   :material-trending-up: **독립적인 확장**

    ---

    각 애플리케이션의 인그레스는 자체 트래픽 프로파일에 맞게 확장되며, 한 팀의 트래픽 급증이 다른 팀에 영향을 주지 않습니다.

*   :material-tune: **워크로드별 튜닝, 중앙 보호**

    ---

    인증서, 리스너 정책, 대상 그룹은 애플리케이션별로 튜닝되는 반면, CloudFront, AWS WAF, VPC별 방화벽 검사는 조직 전체에 일관된 엣지 및 VPC 보호를 제공합니다.

*   :material-routes: **단순한 라우팅**

    ---

    클라이언트는 CloudFront를 통하거나 DNS를 통해 직접 애플리케이션에 접근합니다. 트랜짓 홉, 공유 VPC 의존성, 디버깅해야 할 트래픽 흐름 복잡성이 없습니다.

</div>

#### L7 트래픽: 각 오리진 앞단의 CloudFront와 AWS WAF {#l7-traffic-cloudfront-and-aws-waf-in-front-of-each-origin}

L7 트래픽의 경우, 권장 패턴은 **각 오리진 앞단에 Amazon CloudFront와 AWS WAF를 배치**하는 것입니다. 각 애플리케이션 팀이 자체 오리진을 소유하며, CloudFront는 세 가지 오리진 유형을 지원합니다. 정적 콘텐츠를 위한 Amazon S3 버킷, 워크로드 VPC 내부의 프라이빗(인터넷 비연결) [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)(ALB), [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html)(NLB), 또는 EC2 인스턴스를 가리키는 **VPC 오리진**, 그리고 모든 HTTP/HTTPS 공개 엔드포인트를 위한 **커스텀 오리진**입니다. CloudFront와 AWS WAF는 중앙에서 관리되고 모든 배포에 균일하게 적용됩니다. CloudFront는 엣지에서 TLS를 종료하고 사용자 가까이에서 보호(AWS WAF, HTTP/3, 엣지 TLS)를 집중시키며, AWS WAF는 트래픽이 오리진 VPC에 도달하기 전에 관리형 규칙 그룹, 커스텀 규칙, 속도 제한에 따라 각 요청을 평가합니다.

**L7 인그레스 모범 사례**:

* **VPC 호스팅 워크로드의 기본값으로 [CloudFront VPC Origins](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-vpc-origins.html)를 사용하세요**. VPC Origins를 사용하면 CloudFront가 퍼블릭 IP 없이, 퍼블릭 서브넷 호스팅 없이 프라이빗 ALB, NLB, 또는 EC2 인스턴스에 연결할 수 있으며, CloudFront가 유일한 진입 경로가 됩니다. 크로스 계정 VPC 오리진은 AWS Resource Access Manager(RAM)를 통해 지원됩니다. CloudFront를 앞단에 둔 모든 새로운 VPC 호스팅 L7 워크로드에 이를 사용하고, 기존 퍼블릭 오리진의 마이그레이션을 고려하세요.
* **TLS는 CloudFront와 오리진 로드 밸런서에서 종료하고**, 애플리케이션에서 종료하지 마세요. ACM 발급 인증서는 무료이고, 자동 갱신되며, 중앙에서 감사 가능합니다. 워크로드의 컴플라이언스 기준이 종단 간 TLS를 요구하는 경우에만 CloudFront-오리진 간 재암호화를 적용하세요.
* **AWS Firewall Manager로 AWS WAF를 중앙에서 관리하세요**. 단일 Firewall Manager 정책이 조직 내 모든 CloudFront 배포와 ALB에 일관된 기준을 적용하는 동시에, 애플리케이션 팀은 그 위에 워크로드별 규칙을 추가할 수 있습니다.
* **워크로드에 맞는 백엔드 서비스를 선택하세요**. ALB는 대부분의 HTTP/HTTPS 웹 애플리케이션, REST API, gRPC 서비스에 적합하고, [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)는 인그레스 계층에 요청 검증, 스로틀링, 인증이 내장된 API 우선 워크로드에 적합합니다.

#### L4 트래픽: 엣지 또는 VPC 내 보호를 갖춘 VPC별 진입점 {#l4-traffic-per-vpc-entry-points-with-edge-or-in-vpc-protection}

일부 워크로드는 HTTP 인식 인그레스를 사용할 수 없으며, 클라이언트의 소스 IP와 프로토콜을 그대로 보존하는 레이어 4 진입점이 필요합니다. 여기에는 HTTP 계층 추가 시 지연 시간이 증가하거나 프로토콜이 손상되는 실시간 게임, 음성, 영상, 거래 워크로드, 소스 IP로 클라이언트를 종단 간 인증하는 워크로드, HTTP/HTTPS 이외의 프로토콜(커스텀 바이너리 프로토콜, MQTT, SMTP, 인가된 클라이언트에 노출된 데이터베이스 프로토콜)을 사용하는 서비스, 그리고 프로토콜 디코딩 없이 전달해야 하는 고처리량 TCP 또는 UDP가 포함됩니다.

기본 구성 요소는 기본적으로 클라이언트 소스 IP를 보존하면서 매우 높은 처리량으로 레이어 4 TCP, UDP, TLS 종료를 제공하는 NLB와, 대륙 전반에 분산된 클라이언트를 위해 애니캐스트 정적 IP와 AWS 글로벌 엣지 네트워크의 이점을 활용하는 TCP 및 UDP 워크로드를 위한 [AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)입니다.

L7과 동일한 목표(중앙 보호를 갖춘 워크로드별 소유권)가 적용되지만, 보안 메커니즘은 앞단에 있는 진입점에 따라 달라집니다.

* **인터넷 연결 NLB(트래픽이 인터넷 게이트웨이를 통해 VPC로 진입)**: 전용 방화벽 서브넷에 VPC별 방화벽 엔드포인트를 배포하고, VPC 인그레스 라우팅을 통해 인터넷 게이트웨이와 NLB 사이에 삽입합니다. IGW 엣지 라우트 테이블은 수신 트래픽을 먼저 방화벽 엔드포인트로 보낸 다음 NLB 및 워크로드 서브넷으로 전달합니다. 방화벽 계층은 AWS Network Firewall이거나 서드파티 방화벽 어플라이언스 플릿 앞단의 Gateway Load Balancer이며, 규칙 세트는 중앙에서 관리됩니다.
* **내부 NLB, ALB, 또는 EC2 엔드포인트 앞단의 AWS Global Accelerator**: Global Accelerator의 트래픽은 고객의 인터넷 게이트웨이가 아닌 AWS 내부 네트워크를 통해 엔드포인트로 전달되므로, 위의 IGW + 인그레스 라우팅 패턴이 적용되지 않습니다. 적용되는 보호는 AWS Shield Standard(Global Accelerator에 내장), 클라이언트 IP 보존(NLB 또는 EC2 엔드포인트에서 실제 클라이언트 IP를 사용한 보안 그룹 규칙 작성 가능), NLB의 보안 그룹, 그리고 엔드포인트가 ALB인 경우 AWS WAF입니다. 더 깊은 상태 저장 검사가 필요한 경우, IGW가 아닌 VPC 내부의 로드 밸런서 서브넷과 워크로드 서브넷 사이에 서브넷 수준 라우팅을 통해 검사 계층을 배치하세요.

두 경우 모두 중앙화되는 것은 정책이고 분산되는 것은 데이터 플레인입니다.

**L4 인그레스 모범 사례**:

* **여러 가용 영역에 NLB를 배포하고** 크로스 존 로드 밸런싱을 활성화하세요(NLB의 기본값은 비활성화). 크로스 존은 클라이언트 분포가 영역 간에 고르지 않을 때 부하를 균등하게 분산합니다.
* **워크로드가 TCP 수준 TLS를 실제로 필요로 하는 경우에만 NLB에서 TLS 리스너를 사용하세요**. HTTPS 워크로드의 경우, (일반적으로 CloudFront 뒤에 위치한) ALB의 HTTP 인식 종료가 운영상 더 간단합니다.
* **소스 IP 보존에 대해 신중하게 결정하세요**. NLB는 기본적으로 클라이언트 IP를 보존하므로, 백엔드 보안 그룹은 로드 밸런서 주소가 아닌 클라이언트 IP 범위를 허용해야 합니다. 애플리케이션이 필요로 하는 것에 맞는 로드 밸런서를 선택하세요.
* **글로벌 L4 대상을 위해 NLB 앞단에 Global Accelerator를 배치하세요**. Global Accelerator의 애니캐스트 IP는 CloudFront가 L7 트래픽에 하는 것과 같은 방식으로, 원거리 클라이언트의 인터넷 경로 변동성 영향을 줄입니다. Global Accelerator를 사용할 때는 엔드포인트에서 클라이언트 IP 보존을 활성화하여 보안 그룹이 실제 클라이언트 IP를 사용한 IP 기반 규칙을 적용할 수 있도록 하세요.
* **검사 패턴을 진입점에 맞추세요**. VPC별 AWS Network Firewall 또는 서드파티 방화벽을 갖춘 GWLB 엔드포인트는 트래픽이 인터넷 게이트웨이를 통해 진입할 때(NLB 직접 인그레스) 작동합니다. Global Accelerator가 진입점인 경우, 엣지 보호(Shield Standard, 클라이언트 IP 보존, 보안 그룹, ALB 엔드포인트의 AWS WAF)에 의존하고, 더 깊은 검사는 VPC 내부의 로드 밸런서와 워크로드 서브넷 사이에 배치하세요.

### 중앙 집중식 인그레스 {#centralized-ingress}

중앙 집중식 인그레스는 외부 트래픽을 먼저 공유 인그레스 VPC로 보내고, 그곳에서 검사 또는 공유 TLS 종료를 거친 후 내부 네트워크(Transit Gateway 또는 AWS Cloud WAN)를 통해 올바른 애플리케이션 VPC로 전달합니다. 두 가지 일반적인 구현 방식은 워크로드 VPC에 백엔드 대상을 두는 인그레스 VPC의 공유 ALB 또는 NLB, 또는 해당 공유 로드 밸런서 앞단에 서드파티 방화벽을 갖춘 Gateway Load Balancer입니다.

!!! danger "AWS에서는 거의 올바른 패턴이 아닙니다"
    중앙 집중식 인그레스는 온프레미스 사고 방식(모든 인바운드 트래픽이 반드시 통과해야 하는 경계 DMZ)을 클라우드 환경에 적용한 것으로, 동일한 보안 목표는 위에서 설명한 분산형 + CloudFront + AWS WAF + VPC Origins 패턴으로 더 잘 달성할 수 있습니다. Firewall Manager를 통해 중앙에서 관리되는 VPC별 방화벽 엔드포인트(AWS Network Firewall 또는 서드파티 방화벽 어플라이언스를 갖춘 Gateway Load Balancer)는 L4에서 동일한 결과를 달성합니다. 두 경우 모두 보호는 중앙에서 정의하고 관리하며, 분산되는 것은 데이터 플레인입니다. 이것이 바로 클라우드 네이티브 패턴이 작동하는 이유입니다.

AWS에서 중앙 집중식 인그레스의 트레이드오프는 실질적입니다.

<div class="grid cards" markdown>

*   :material-link-variant: **로드 밸런서 체이닝**

    ---

    크로스 VPC ELB 대상 그룹은 **IP 대상 전용**입니다(인스턴스 및 ALB 대상 유형은 동일 VPC 내에서만 사용 가능). 공유 인그레스 VPC에서 동적 워크로드 백엔드로 트래픽을 전달하려면, 각 워크로드 VPC는 일반적으로 공유 LB에 안정적인 IP 대상을 제공하기 위해 자체 내부 NLB(L7 트래픽의 경우 ALB도)를 실행해야 합니다. 트래픽 경로는 클라이언트 → 엣지 → 인그레스 VPC ALB/NLB → Transit Gateway 또는 AWS Cloud WAN을 통한 IP 대상 → 워크로드 VPC NLB → ALB(L7인 경우) → 워크로드 컴퓨팅이 됩니다. 각 홉은 크기를 조정해야 할 또 다른 구성 요소, 디버깅해야 할 또 다른 장애 모드, 그리고 대상 그룹, 리스너 규칙, 인증서를 동기화해야 할 또 다른 지점입니다.

*   :material-cash-multiple: **추가 트래픽 처리 비용**

    ---

    트래픽은 인그레스 로드 밸런서, 검사 계층, 그리고 워크로드 측 로드 밸런서 외에 Transit Gateway 또는 AWS Cloud WAN 데이터 처리에 의해 처리됩니다. 분산형 패턴은 동일한 흐름을 CloudFront에서 한 번, 오리진에서 한 번만 처리합니다.

*   :material-bullseye-arrow: **공유 VPC 장애 반경**

    ---

    인그레스 VPC의 변경은 모든 소비 애플리케이션에 영향을 미칩니다. 유지 관리 창, 변경 관리, 롤백 절차가 모두 팀별이 아닌 조직 전체 수준이 됩니다.

*   :material-account-cog: **운영 소유권 집중**

    ---

    인그레스 VPC를 운영하는 네트워크 팀이 인터넷에 무언가를 노출하려는 모든 애플리케이션의 조율 병목이 되어, 애플리케이션 팀의 속도를 저해합니다.

</div>

이러한 트레이드오프는 이론적인 것이 아닙니다. 중앙 집중식 인그레스 배포가 결국 다시 분산되는 가장 일반적인 이유입니다.

!!! info "중앙 집중식 인그레스가 정당화되는 경우"
    채택하기 전에, 다음 특정 요인 중 하나가 실제로 적용되는지, 그리고 분산형 패턴이 이를 충족하지 못하는지 확인하세요.

    * **특정 컴플라이언스 기준이 CloudFront 앞단에서 기본적으로 사용할 수 없는 특정 프록시 계층을 요구**하거나, VPC별 방화벽 아키텍처를 허용하지 않는 경우.
    * **프라이빗 CA를 사용한 중앙 집중식 TLS 종료**가 모든 인터넷 연결 서비스에 요구되며, 애플리케이션별 인증서 재발급이 허용되지 않는 경우.
    * **단일하고 감사된 인터넷 노출 표면**이 기술적 보안 결과와 무관하게 정책적 선택으로 요구되는 경우.

    이 중 어느 것도 해당되지 않는다면, 분산형 인그레스가 올바른 선택입니다. 분산형 인그레스는 중앙 집중식 패턴을 선택하게 만드는 중앙 보호를 공유 인그레스 VPC의 운영 비용 없이 제공합니다.

!!! tip "중앙 집중식 인그레스를 채택하는 경우"

    * **검사는 중앙 집중식 계층에서 적용하고, 다운스트림에서 다시 적용하지 마세요**. 공유 ALB의 AWS WAF, 또는 인터넷 게이트웨이와 공유 NLB 사이의 방화벽 삽입(AWS Network Firewall 또는 서드파티 방화벽 어플라이언스를 갖춘 Gateway Load Balancer)이 중앙 집중식 패턴을 선택하게 만드는 중앙 보호를 제공합니다. 트래픽이 Transit Gateway 또는 AWS Cloud WAN을 통해 워크로드 VPC로 진입할 때 두 번째로 검사하는 것은 실질적인 보안을 추가하지 않으며(트래픽은 이미 검사됨), 모든 흐름에 대해 또 다른 검사 계층의 비용과 운영 부담을 추가합니다.
    * **공유 계층에서 ALB 및 NLB 할당량을 모니터링하세요**. 로드 밸런서 자체는 자동으로 확장되지만, LB별 할당량은 이제 인그레스를 공유하는 모든 애플리케이션이 소비하며, 단일 애플리케이션 온보딩이 공유 LB를 한도 초과로 밀어낼 수 있습니다. CloudWatch에서 인그레스 LB별 할당량 사용량을 추적하고, 워크로드 온보딩이 실패하는 순간이 아닌 사전에 한도 증가를 요청하세요.
    * **인그레스 VPC 변경은 엄격한 변경 관리로 처리하세요**. 인그레스 VPC는 이제 많은 애플리케이션의 단일 인터넷 진입점이므로, 라우팅, 리스너 규칙, 인증서, 또는 검사 정책에 영향을 미치는 모든 변경은 조직 전체에 영향을 미칩니다. 피어 리뷰, 단계적 릴리스(하위 환경 인그레스 먼저, 프로덕션 마지막), 인그레스 LB가 허용하는 경우 카나리 또는 가중치 기반 대상 배포, 그리고 자동화된 롤백 경로를 사용하세요. 목표는 중앙 집중식 계층이 일상적인 온보딩에 충분히 동적으로 유지되면서도 단일 변경이 다중 애플리케이션 인시던트가 되는 것을 방지하는 것입니다.

## 이그레스 연결 {#egress-connectivity}

이그레스(Egress)는 AWS 리소스가 인터넷의 외부 서비스에 접근하는 방식입니다. 이그레스 결정의 형태는 워크로드가 사용하는 IP 버전에 따라 달라지는데, IPv4와 IPv6는 AWS에서 근본적으로 다른 이그레스 경로를 가지기 때문입니다.

* **IPv6의 경우, 이그레스는 본질적으로 분산형입니다**. 각 VPC는 자체 [이그레스 전용 인터넷 게이트웨이](https://docs.aws.amazon.com/vpc/latest/userguide/egress-only-internet-gateway.html)를 통해 인터넷에 접근합니다. 이는 IPv6에서 "프라이빗 서브넷 + NAT"에 해당하는 방식으로, 아웃바운드 전용이며 기가바이트당 요금이 없고 데이터 경로에 NAT가 없습니다. AWS에서 관리하는 IPv6용 NAT는 존재하지 않으며, 이그레스 전용 인터넷 게이트웨이는 해당 VPC에 로컬로 존재합니다(VPC A의 워크로드는 VPC B의 이그레스 전용 인터넷 게이트웨이를 통해 IPv6 트래픽을 라우팅할 수 없습니다). 이후에 다루는 분산형 대 중앙 집중식 논의는 거의 전적으로 IPv4에 해당합니다.
* **IPv4의 경우, 이그레스에는 NAT가 필요하며**, 이로 인해 실질적인 아키텍처 선택이 생깁니다. 각 워크로드 VPC에서 NAT 게이트웨이를 실행하는 방식(분산형)과, Transit Gateway 또는 AWS Cloud WAN을 통해 공유 이그레스 VPC로 IPv4 이그레스를 전송하는 방식(중앙 집중식) 중 하나를 선택해야 합니다. 이는 세 가지 차원에서 진정한 50-50 트레이드오프이며, 모든 조직에 적합한 단일 정답은 없습니다.

IPv4 트레이드오프:

* **비용**: 모든 플로우에는 비용 구조가 있습니다. 분산형 모델에서는 각 워크로드 VPC가 자체 NAT 게이트웨이와 (사용하는 경우) 자체 AWS Network Firewall 또는 Gateway Load Balancer 엔드포인트를 운영하므로, VPC별 시간당 요금과 처리 요금이 누적됩니다. 중앙집중화하면 이를 단일 이그레스 VPC로 통합할 수 있지만, 이제 모든 플로우가 해당 VPC로 향하는 과정에서 Transit Gateway 또는 AWS Cloud WAN 데이터 처리 요금도 발생합니다. 어떤 패턴이 더 저렴한지는 운영하는 VPC 수와 이그레스 트래픽 양에 따라 달라집니다.
* **운영 소유권**: NAT 게이트웨이를 누가 운영하고, 비용을 누가 부담하며, 이그레스 장애 발생 시 티켓을 누가 처리하는지의 문제입니다. 중앙집중화하면 이를 네트워크 또는 플랫폼 팀에 집중시키고, 분산화하면 각 애플리케이션 팀에 위임합니다.
* **검사 지점의 위치**: 분산형 데이터 플레인도 여러 AWS Network Firewall 또는 Gateway Load Balancer 엔드포인트(단일 방화벽 플릿)와 Route 53 DNS Firewall(아웃바운드 도메인 규칙용)을 활용하여 하나의 통일된 정책을 적용할 수 있습니다. 중앙집중화하면 하나의 VPC에 단일 물리적 검사 레이어로 통합됩니다. 두 방식 모두 일관된 정책을 제공하지만, 검사 지점이 논리적(VPC 전반에 분산된 하나의 관리형 규칙 세트)인지 물리적(모든 플로우가 통과하는 하나의 공유 어플라이언스 플릿)인지에서 차이가 납니다.

올바른 선택은 조직에서 이 세 가지 차원 중 어느 것이 가장 중요한지에 따라 달라집니다. 이어지는 하위 섹션에서 각 패턴과 그에 따른 설계 선택 사항을 자세히 살펴봅니다.

IP 버전이나 패턴에 관계없이 모든 이그레스 전략에서 첫 번째 결정은 **NAT 위치를 결정하기 전에 이그레스 트래픽 양을 줄이는 것**입니다. NAT 게이트웨이를 통해 퍼블릭 AWS 엔드포인트에 도달하는 AWS API 트래픽은 가장 흔하게 발생하는 불필요한 비용입니다. Amazon S3 및 Amazon DynamoDB용 게이트웨이 [VPC 엔드포인트(AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html)는 무료이며, 워크로드에서 가장 많이 사용하는 AWS 서비스(STS, KMS, ECR, Systems Manager, CloudWatch Logs 등)용 인터페이스 VPC 엔드포인트는 해당 트래픽을 프라이빗하게 유지합니다. 이는 중앙 집중식 또는 분산형 이그레스 중 어느 것을 선택하든 적용되며, 이그레스 경로에서 트래픽을 완전히 제거합니다.

### 리전형 NAT 게이트웨이와 가용 영역형 NAT 게이트웨이 선택 (IPv4) {#choose-between-regional-and-zonal-nat-gateway-ipv4}

IPv4 이그레스에서 분산형 대 중앙 집중식을 선택하기 전에, 사용할 NAT 게이트웨이 가용성 모드를 결정해야 합니다. AWS NAT 게이트웨이에는 두 가지 모드가 있습니다. **가용 영역형(zonal)** 모드(퍼블릭 서브넷에 가용 영역당 하나의 NAT 게이트웨이를 배치하고, 라우팅 테이블 항목으로 각 가용 영역의 프라이빗 서브넷이 로컬 NAT 게이트웨이를 통하도록 설정)와, 신규 **리전형(regional)** 모드(워크로드 존재 여부에 따라 가용 영역 전반에 걸쳐 자동으로 확장 및 축소되는 단일 NAT 게이트웨이 ID로, 퍼블릭 서브넷이 필요 없으며 가용 영역당 더 높은 IP 및 포트 한도를 제공)입니다.

권장 사항은 명확합니다.

* **그린필드 배포의 경우, 기본적으로 리전형 NAT 게이트웨이를 사용하세요**. 모든 가용 영역에 걸친 단일 NAT 게이트웨이 ID는 라우팅 테이블 설계를 단순화하고, 가용 영역별 퍼블릭 서브넷 유지 요건을 제거하며(이는 우발적 노출 위험의 한 유형을 제거합니다), 수동 재프로비저닝 없이 가용 영역별 IP 할당을 확장합니다. 리전형 NAT 게이트웨이는 새 VPC에 권장되는 옵션입니다.
* **가용 영역형 NAT 게이트웨이를 운영 중인 기존 배포의 경우, 마이그레이션할 이유가 없습니다**. 가용 영역형 NAT 게이트웨이는 계속 완전히 지원되며, 이미 라우팅과 퍼블릭 서브넷이 구성된 환경에서 전환하는 운영상의 이점은 미미합니다. 새 VPC를 생성할 때 리전형 NAT 게이트웨이를 적용하고 기존 것은 그대로 운영하세요.
* **프라이빗 NAT(하이브리드 사용 사례를 위해 프라이빗 서브넷에 배치하는 NAT 게이트웨이)의 경우, 가용 영역형 모드를 계속 사용하세요**. 리전형 NAT 게이트웨이는 일반 이그레스에 권장되며, 프라이빗 연결 시나리오는 여전히 가용 영역형 모델에 의존합니다.

이 선택은 IPv4 이그레스를 분산형으로 운영하는지 중앙 집중식으로 운영하는지와 무관합니다. 이는 두 패턴 모두에 적용되는 NAT 게이트웨이 가용성 모드 결정입니다.

### 분산형 IPv4 이그레스 {#decentralized-ipv4-egress}

분산형 IPv4 모델에서는 인터넷 이그레스가 필요한 각 VPC가 자체 NAT 게이트웨이와 자체 이그레스 정책을 운영합니다. 프라이빗 서브넷의 트래픽은 트랜짓 홉이나 공유 의존성 없이 해당 VPC의 인터넷 게이트웨이를 통해 직접 퍼블릭 인터넷에 도달합니다. 이는 IPv6 경로(VPC별 이그레스, 트랜짓 네트워크 처리 없음)와 동일한 형태이므로, 듀얼 스택 워크로드는 두 IP 버전 모두에 단일 VPC 로컬 패턴을 사용할 수 있습니다.

모범 사례:

* **가용 영역 이중화 NAT 용량을 배포하세요**. 리전형 NAT 게이트웨이를 사용하면 자동으로 처리됩니다. 가용 영역형 NAT 게이트웨이를 사용하는 경우, 가용 영역당 하나씩 배포하고 각 가용 영역의 프라이빗 서브넷이 로컬 NAT 게이트웨이를 통하도록 라우팅하세요. 단일 가용 영역형 NAT 게이트웨이는 해당 VPC의 이그레스에 대한 단일 장애 지점이 됩니다. 가용 영역 인식 설계를 적용하면 이 위험을 제거하고 가용 영역 간 데이터 전송을 최소화할 수 있습니다.
* **VPC 엔드포인트를 사용하여 NAT 게이트웨이 트래픽을 줄이세요**. S3 및 DynamoDB용 게이트웨이 엔드포인트는 무료이며 해당 트래픽을 NAT 경로에서 완전히 제거합니다. 트래픽이 많은 AWS 서비스용 인터페이스 엔드포인트는 NAT 처리 비용 절감으로 비용을 충당하는 경우가 많습니다.
* **VPC 레이어에서 이그레스 정책을 적용하세요**. 워크로드의 보안 그룹, 필요한 CIDR만 NAT 경로로 향하도록 하는 라우팅 테이블, 그리고 거친 두 번째 레이어로서의 NACL을 활용하세요. 목적지 기반 필터링(특정 도메인 또는 IP)의 경우, Route 53 DNS Firewall, AWS Network Firewall, 또는 워크로드 VPC 내 서드파티 방화벽이 포함된 Gateway Load Balancer를 사용하고, 규칙 세트는 AWS Firewall Manager를 통해 중앙에서 관리하세요.

### 중앙 집중식 IPv4 이그레스 {#centralized-ipv4-egress}

중앙 집중식 IPv4 모델에서는 공유 이그레스 VPC가 여러 워크로드 VPC의 인터넷 이그레스를 담당합니다. 워크로드 VPC의 IPv4 트래픽은 Transit Gateway 또는 AWS Cloud WAN을 통해 이그레스 VPC로 라우팅된 후, NAT 게이트웨이를 통해 인터넷으로 나갑니다. 이그레스 VPC는 일반적으로 공유 필터링(AWS Network Firewall, 서드파티 방화벽이 포함된 Gateway Load Balancer)도 호스팅하여 모든 워크로드에 단일 이그레스 정책이 적용되도록 합니다. 이 패턴은 IPv4에만 적용됩니다. IPv6 이그레스는 이그레스 전용 인터넷 게이트웨이가 VPC별로 존재하고 AWS가 관리형 NAT66 대안을 제공하지 않으므로, 모든 소비 VPC에서 분산형으로 유지됩니다.

모범 사례:

* **이그레스 VPC를 네트워크 또는 플랫폼 팀이 소유하는 공유 서비스로 운영하세요**. 애플리케이션 팀은 이그레스 VPC를 수정하지 않고 Transit Gateway 또는 AWS Cloud WAN 어태치먼트를 통해 소비합니다.
* **최소한 AWS 리전당 하나의 이그레스 VPC를 사용하세요**. 단일 글로벌 이그레스 VPC를 위해 리전 간 이그레스를 라우팅하는 것은 비용과 지연 시간 측면에서 거의 가치가 없습니다. AWS Cloud WAN을 사용하면 리전별 이그레스 VPC도 단일 네트워크 정책으로 관리할 수 있습니다.
* **이그레스 경로에서 NAT 이전에 검사 레이어를 배치하세요**. 일반적인 레이아웃은 다음과 같습니다. 워크로드 VPC → Transit Gateway 또는 AWS Cloud WAN → 이그레스 VPC 내 AWS Network Firewall 또는 서드파티 방화벽이 포함된 Gateway Load Balancer → NAT 게이트웨이 → 인터넷 게이트웨이. NAT 이전에 검사하면 원본 VPC 소스 IP가 보존되어 VPC별 정책 적용 및 포렌식 분석에 중요합니다.
* **공유 검사 레이어를 가용 영역 이중화로 배포하세요**. AWS Network Firewall과 GWLB 기반 서드파티 방화벽 플릿 모두 다중 가용 영역 배포를 지원합니다. 단일 가용 영역 검사 레이어는 이그레스 VPC를 소비하는 모든 워크로드에 대한 단일 장애 지점이 됩니다.
* **처리량 외에도 검사 레이어의 드롭 및 패스 카운트에 대한 알람을 설정하세요**. 드롭 급증은 소비 워크로드의 이그레스 프로파일이 변경되었다는 신호인 경우가 많으며, 이를 빠르게 감지하면 잘못 구성된 정책을 바로 고칠 수 있지만, 놓치면 혼란에 빠진 애플리케이션 팀을 뒤쫓게 됩니다.
* **운영 소유권 경계를 문서화하세요**. 애플리케이션 팀은 자신이 소유하는 이그레스 운영(워크로드의 아웃바운드 트래픽 프로파일, 요청하는 허용 목록)과 중앙 팀이 소유하는 것(검사 규칙, 정책 적용)을 명확히 알아야 합니다.

### 분산형 대 중앙 집중식 IPv4 이그레스 비교 {#comparing-decentralized-vs-centralized-ipv4-egress}

분산형이 거의 항상 정답인 인그레스와 달리, IPv4 이그레스는 기술적 요소만큼이나 조직적 요소에 의해 결정되는 진정한 50-50 결정입니다. 아래 표는 일반적으로 선택을 결정하는 차원에서 각 패턴이 어떻게 처리되는지 요약합니다. 이 결정은 IPv4에만 해당하며, IPv6 이그레스는 어느 경우에도 분산형임을 기억하세요.

| 차원 | 분산형 IPv4 이그레스 | 중앙 집중식 IPv4 이그레스 |
| --- | --- | --- |
| **VPC별 비용 오버헤드** | 각 VPC는 자체 NAT 게이트웨이와 (사용하는 경우) 자체 AWS Network Firewall 또는 Gateway Load Balancer 엔드포인트 비용을 부담합니다. 직접 IGW 출구는 트랜짓 네트워크 데이터 처리 요금이 없습니다 | 하나의 공유 이그레스 VPC가 소비하는 워크로드 수에 관계없이 NAT 및 검사 엔드포인트 비용을 흡수하지만, 이제 모든 플로우가 이그레스 VPC로 향하는 과정에서 Transit Gateway 또는 AWS Cloud WAN 데이터 처리 요금도 발생합니다 |
| **운영 소유권** | 각 애플리케이션 팀이 자체 이그레스 경로, 허용 목록, 비용을 소유합니다 | 네트워크 또는 플랫폼 팀이 이그레스 VPC를 소유하고, 애플리케이션 팀은 공유 서비스로 소비합니다 |
| **검사 지점 배치** | 관리 플레인에서는 중앙 집중식, 데이터 플레인에서는 분산형: AWS Network Firewall 및 Gateway Load Balancer 규칙 세트는 중앙에서 관리되고, [Route 53 DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall.html)은 모든 VPC에 단일 도메인 규칙 세트를 적용합니다. 모든 플로우를 하나의 이그레스 VPC로 강제하지 않고도 동일한 통일된 정책을 적용할 수 있습니다 | 두 플레인 모두 중앙 집중식: 하나의 이그레스 VPC에 있는 하나의 검사 레이어가 모든 플로우를 처리합니다. 보안 기준이 논리적 검사 지점이 아닌 단일 물리적 검사 지점을 요구할 때 유용합니다 |
| **장애 도메인** | 이그레스 문제는 하나의 VPC에만 영향을 미칩니다 | 공유 이그레스 VPC의 이그레스 문제나 변경은 모든 소비 워크로드에 영향을 미칩니다 |
| **검사 커버리지** | VPC별 AWS Network Firewall 또는 서드파티 방화벽이 포함된 Gateway Load Balancer로, 워크로드가 필요한 곳에만 적용됩니다 | 이그레스 VPC의 하나의 공유 검사 레이어가 모든 플로우에 균일하게 적용됩니다 |
| **듀얼 스택 일관성** | IPv4와 IPv6 모두 VPC별로 출구를 사용하므로, 두 프로토콜의 이그레스 형태가 동일하고 워크로드 VPC가 두 경로를 모두 소유합니다 | IPv4는 Transit Gateway 또는 AWS Cloud WAN을 통해 공유 이그레스 VPC로 이동하고, IPv6는 여전히 이그레스 전용 인터넷 게이트웨이를 통해 VPC별로 출구를 사용합니다. 운영자는 듀얼 스택 워크로드에 대해 두 가지 다른 이그레스 패턴을 동시에 운영합니다 |
| **지연 시간 오버헤드** | 직접 IGW 출구, 트랜짓 홉 없음 | 모든 IPv4 플로우에 Transit Gateway 또는 AWS Cloud WAN 홉과 검사 처리가 추가됩니다 |
| **최적 적합** | 소규모 환경, 팀 자율성 조직, 지연 시간 또는 처리량에 민감한 워크로드, 단일 이그레스 형태가 선호되는 IPv6 우선 또는 듀얼 스택 워크로드, 서로 근본적으로 다른 이그레스 정책이 필요한 애플리케이션 | IPv4 트래픽에 대한 대규모 비용 압박(수십 또는 수백 개의 VPC), IPv4에 대한 필수 단일 물리적 검사 지점, 중앙 보안 소유권, IPv4 이그레스를 공유 플랫폼 서비스로 운영하는 조직 |

### 향후 전망: AWS Network Firewall Proxy (퍼블릭 프리뷰) {#looking-ahead-aws-network-firewall-proxy-public-preview}

[AWS Network Firewall Proxy](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-network-firewall-proxy-preview/)는 아웃바운드 웹 트래픽을 위한 관리형 **명시적 포워드 프록시**로, 현재 퍼블릭 프리뷰 중입니다. AWS Network Firewall이나 서드파티 방화벽이 포함된 Gateway Load Balancer는 데이터 경로에 투명하게 위치하지만, 이 프록시는 그러한 옵션의 동등한 대안이 아니며 다른 추상화 수준에서 동작합니다. 이 프록시는 인터넷 또는 온프레미스 목적지로의 HTTP CONNECT 요청을 명시적으로 프록시하고, 각 요청의 세 단계(PreDNS, PreRequest, PostResponse)에서 규칙을 평가하여 각 워크로드가 접근할 수 있는 대상에 대한 세밀한 요청 수준 제어를 제공합니다.

이 패턴이 대체하는 것은 **자체 호스팅 포워드 프록시 플릿**(명시적 이그레스 필터링을 위해 조직이 역사적으로 운영해 온 EC2의 Squid 클러스터 또는 컨테이너 기반 프록시 플릿)입니다. AWS Network Firewall과 GWLB+서드파티 방화벽이 이그레스 경로에서 패킷 수준 검사를 제공하는 반면, 이 프록시는 요청 수준 규칙을 통한 애플리케이션 인식 프록시를 제공합니다.

서비스가 퍼블릭 프리뷰 중이므로, 이 글을 작성하는 시점에서 기능, 지원되는 구성 및 리전 가용성이 제한적입니다. 명시적 포워드 프록시 시맨틱이 조직의 요구 사항인 경우, 서비스가 일반 공급(GA)에 도달했을 때 더 광범위하게 채택할 것을 염두에 두고 지금부터 AWS Network Firewall Proxy를 평가하기 시작하는 패턴으로 취급하세요.

### 인그레스와 이그레스 패턴 결합 {#combining-ingress-and-egress-patterns}

인그레스와 이그레스는 독립적인 결정입니다. 워크로드는 분산형 인그레스와 중앙 집중식 이그레스를 함께 사용하거나, 그 반대로 사용할 수 있습니다. 가장 자주 등장하는 조합은 다음과 같습니다.

* **분산형 인그레스 + 분산형 이그레스**는 가장 단순한 패턴으로, 소규모 환경과 완전한 소유권을 원하는 애플리케이션 팀의 일반적인 기본값입니다.
* **분산형 인그레스 + 중앙 집중식 이그레스**는 대규모 조직에서 흔합니다. 각 애플리케이션이 자체 퍼블릭 진입점을 소유하지만, IPv4 이그레스는 VPC별 NAT 및 검사 비용을 하나의 공유 이그레스 VPC로 통합합니다.
* **중앙 집중식 인그레스 + 중앙 집중식 이그레스**는 경계 검사와 아웃바운드 트래픽에 대한 단일 물리적 검사 지점이 모두 요구되는 컴플라이언스 중심 환경에서 나타납니다. 두 방향 모두 동일한 운영 의존성과 소유권 모델을 공유합니다.
* **중앙 집중식 인그레스 + 분산형 이그레스**는 드뭅니다. 인바운드 트래픽에 대한 경계 검사가 중앙집중화를 정당화한다면, 일반적으로 동일한 요인이 아웃바운드 트래픽에도 적용됩니다. 순수한 비대칭은 이례적입니다.

## 문서 {#documentation}

이 페이지에서 참조하는 서비스를 등장 위치별로 분류하면 다음과 같습니다.

| 서비스 | 이 페이지에서의 역할 | 문서 |
| --- | --- | --- |
| Amazon CloudFront | 인그레스: 모든 워크로드를 위한 L7 엣지 | [문서](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) |
| CloudFront VPC Origins | 인그레스: CloudFront 뒤에 위치한 프라이빗 ALB, NLB 또는 EC2 오리진 | [문서](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-vpc-origins.html) |
| AWS WAF | 인그레스: CloudFront, ALB, API Gateway에 대한 관리형 L7 보호 | [문서](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) |
| Application Load Balancer | 인그레스: 워크로드 VPC의 L7 진입점 | [문서](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) |
| Network Load Balancer | 인그레스: 워크로드 VPC의 L4 진입점 | [문서](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) |
| Amazon API Gateway | 인그레스: API 중심 워크로드를 위한 관리형 L7 인그레스 | [문서](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) |
| AWS Global Accelerator | 인그레스: 글로벌 클라이언트를 위한 L4 워크로드용 애니캐스트 정적 IP | [문서](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html) |
| NAT gateway | 이그레스(IPv4): 리전 또는 가용 영역 모드의 관리형 NAT | [문서](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) |
| Egress-only internet gateway | 이그레스(IPv6): VPC별 아웃바운드 IPv6 경로 | [문서](https://docs.aws.amazon.com/vpc/latest/userguide/egress-only-internet-gateway.html) |
| Route 53 DNS Firewall | 이그레스: VPC 전반에 걸친 도메인 기반 아웃바운드 필터링 | [문서](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall.html) |
| AWS Network Firewall Proxy *(미리 보기)* | 이그레스: 관리형 명시적 포워드 프록시 | [공지](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-network-firewall-proxy-preview/) |
| VPC endpoints (AWS PrivateLink) | 이그레스: AWS 서비스 트래픽을 이그레스 경로에서 분리 | [문서](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) |
| AWS Network Firewall | 인그레스 + 이그레스: 관리형 스테이트풀 방화벽 | [문서](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html) |
| Gateway Load Balancer | 인그레스 + 이그레스: 서드파티 방화벽을 위한 투명한 삽입 지점 | [문서](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html) |
| AWS Firewall Manager | 인그레스 + 이그레스: AWS WAF, Network Firewall, GWLB에 대한 중앙 집중식 규칙 세트 관리 | [문서](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html) |
| AWS Shield | 기본 보호: Shield Standard는 모든 퍼블릭 AWS 엔드포인트에 자동 적용되며, Shield Advanced는 고급 DDoS 보호 제공 | [문서](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html) |

## 인터넷 연결 스택 구성하기 {#building-your-internet-connectivity-stack}

실제 인터넷 연결 전략은 두 가지 독립적인 차원에서의 선택을 결합합니다. 인그레스(분산형 vs 중앙 집중식, 워크로드별)와 이그레스(IPv6는 분산형 유지, IPv4는 트레이드오프에 따라 분산형 vs 중앙 집중식)가 그것입니다. 각 결정은 독립적인 기준으로 내려집니다.

![인터넷 연결 스택의 세 계층: 인그레스(엣지 레이어, VPC별 진입점, VPC별 L4 검사), 이그레스(IPv6 분산형, IPv4 패턴 선택, 트래픽 감소), 필터링 레이어(중앙 관리, 데이터 플레인 옵션)](../assets/connectivity/internet-stack.png)
/// caption
인터넷 연결 스택 — [Drawio 소스](../assets/connectivity/internet-stack.drawio)
///

### 신규 환경 {#new-environments}

처음부터 인터넷 연결을 구성하는 조직은 확장성이 있고 클라우드 네이티브 모델에 충실한 패턴으로 시작할 수 있습니다.

1. **기본값으로 분산형 인그레스 채택**. 각 애플리케이션 팀이 자체 퍼블릭 진입점을 소유합니다. L7 워크로드 앞에는 Amazon CloudFront와 AWS WAF를 사용하고(VPC 호스팅 백엔드에는 CloudFront VPC Origins 활용), L4 워크로드 앞에는 NLB 또는 AWS Global Accelerator를 사용합니다. L4 검사가 필요한 경우 VPC별로 AWS Network Firewall 또는 GWLB와 서드파티 방화벽 엔드포인트를 적용하되, 규칙 세트는 AWS Firewall Manager를 통해 중앙에서 관리합니다.
2. **워크로드가 지원하는 경우 IPv6 우선 이그레스 적용**. 각 VPC는 자체 이그레스 전용 인터넷 게이트웨이를 통해 인터넷에 연결됩니다. 관리형 NAT66이 없으므로 IPv6 이그레스는 모든 곳에서 분산형으로 운영되도록 계획하고, 이 단순함을 IPv6 도입 결정의 동력으로 삼으세요.
3. **모든 신규 VPC에 IPv4 이그레스용 리전 NAT 게이트웨이 적용**. VPC당 단일 NAT 게이트웨이 ID, 퍼블릭 서브넷 불필요, 더 간단한 라우팅을 제공합니다.
4. **처음부터 IPv4 이그레스 트래픽 감소**. 모든 VPC에 S3 및 DynamoDB용 게이트웨이 VPC 엔드포인트를 무료로 적용합니다. 워크로드가 가장 많이 호출하는 AWS 서비스에는 인터페이스 VPC 엔드포인트를 사용합니다.
5. **조직 적합성에 따라 IPv4 이그레스 패턴 선택**. 팀 자율성, 듀얼 스택 대칭성, 또는 지연 시간 민감도가 중요하다면 분산형을 선택합니다. 대규모 비용 절감이나 단일 물리적 검사 지점이 필요하다면 중앙 집중식을 선택합니다. 두 방식 모두 균일한 정책을 제공합니다. 분산형의 경우 AWS Firewall Manager와 Route 53 DNS Firewall을 통해, 중앙 집중식의 경우 공유 검사 레이어를 통해 정책을 적용합니다.

### 기존 환경 {#existing-environments}

기존 인터넷 연결을 운영 중인 조직은 교체할 필요 없이 현재 패턴을 유지할 수 있습니다.

1. **기존 분산형 인그레스**는 변경 없이 계속 작동합니다. CloudFront + AWS WAF + AWS Firewall Manager 패턴은 모든 계정 토폴로지에 적합합니다. 새로 생성하는 VPC 호스팅 L7 워크로드에는 CloudFront VPC Origins를 도입하고, 운영 가능한 시간대에 기존 퍼블릭 오리진을 CloudFront 뒤로 마이그레이션하는 것을 검토하세요.
2. **공유 VPC를 통한 기존 중앙 집중식 인그레스**는 특정 컴플라이언스 요건으로 도입된 경우 계속 운영할 수 있습니다. 신규 워크로드는 기본적으로 분산형을 사용하고, 중앙 집중식은 원래 요구했던 워크로드에 한해 유지합니다.
3. **기존 가용 영역별 NAT 게이트웨이**는 완전히 지원되며 리전 모드로 마이그레이션할 필요가 없습니다. 새로 생성하는 VPC에는 리전 NAT 게이트웨이를 기본값으로 채택하고, 기존 가용 영역별 배포는 그대로 운영합니다.
4. **기존 중앙 집중식 IPv4 이그레스 VPC**는 역할을 유지합니다. 소비 VPC 전반에 Route 53 DNS Firewall과 AWS Firewall Manager 관리 규칙 세트를 추가하여, 중앙 집중식 검사 레이어를 통과할 필요가 없는 트래픽(DNS 기반 필터링, 워크로드별 규칙)에도 균일한 정책 적용을 확장합니다.
5. **IPv6 도입을 신중하게 계획**. IPv6 이그레스는 설계상 분산형이며, 자체 호스팅 NAT66 없이는 중앙 집중식 모델로 전환할 수 없습니다. 각 애플리케이션이 듀얼 스택을 시작하는 시기와 방법을 결정할 때 이 점을 고려하세요.
