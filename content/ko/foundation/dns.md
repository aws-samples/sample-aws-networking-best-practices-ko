# DNS 아키텍처 {#dns-architecture}

!!! info "사전 요구 사항"
    이 섹션은 [Amazon VPC](vpc.md), [AWS Organizations](organizations.md), [CIDR 계획](cidr.md)에 대한 기본 지식을 전제로 합니다. AWS 네트워킹 기초가 처음이라면 해당 페이지를 먼저 검토하세요.

Amazon Route 53 Resolver는 VPC 내부에서 발생하는 모든 DNS 쿼리를 처리합니다. 프라이빗 호스팅 영역에 대한 쿼리 응답, 하이브리드 연결을 통한 온프레미스 도메인 쿼리 전달, 공용 인터넷 이름 확인 등을 별도의 DNS 인프라 배포 없이 수행합니다. 멀티 계정 AWS 환경에서 DNS 설계 결정은 서비스 디스커버리, 하이브리드 연결, 보안 태세 전반에 연쇄적인 영향을 미칩니다. 잘못 구성된 전달 규칙은 계정 전체의 이름 확인을 조용히 중단시키고, 공유되지 않은 프라이빗 호스팅 영역은 다른 VPC의 소비자에게 서비스를 보이지 않게 만들며, DNS Firewall이 없으면 모든 워크로드가 인터넷상의 임의 도메인을 확인(따라서 접근)할 수 있게 됩니다.

AWS의 DNS는 함께 설계해야 하는 세 가지 계층에서 동작합니다. **확인(resolution)**(쿼리 응답 방식), **공유(sharing)**(DNS 구성을 모든 계정에 전달하는 방식), **보안(security)**(아웃바운드 트래픽의 제어 지점으로 DNS를 활용하는 방식)이 그것입니다. Route 53 Resolver는 확인 엔진 역할을 하고, Route 53 Profiles는 대규모로 구성을 배포하며, Route 53 Resolver DNS Firewall은 DNS 계층에서 도메인 기반 필터링을 적용합니다.

## 주요 기능 {#key-capabilities}

<div class="grid cards" markdown>

*   :material-dns: **Route 53 Resolver**

    ---

    모든 VPC에 기본으로 제공되는 재귀 리졸버입니다. 프라이빗 호스팅 영역에 대한 쿼리에 응답하고, Resolver 엔드포인트를 통해 온프레미스 도메인 쿼리를 전달하며, 퍼블릭 DNS를 자동으로 확인합니다.

*   :material-share-variant: **Route 53 Profiles**

    ---

    프라이빗 호스팅 영역 연결, Resolver 전달 규칙, DNS Firewall 규칙 그룹을 OU 수준에서 계정 전체에 배포합니다. 새 계정은 DNS 구성을 자동으로 상속합니다.

*   :material-lock: **프라이빗 호스팅 영역**

    ---

    연결된 VPC에서만 표시되는 DNS 네임스페이스입니다. 내부 서비스 이름, 스플릿 호라이즌 DNS(내부 쿼리와 외부 쿼리에 대해 서로 다른 응답 제공), VPC Lattice 및 PrivateLink 엔드포인트의 사용자 지정 도메인 이름에 활용됩니다.

*   :material-arrow-right-bold: **Resolver 엔드포인트**

    ---

    인바운드 엔드포인트를 사용하면 온프레미스 DNS 서버가 AWS 프라이빗 호스팅 영역을 확인할 수 있습니다. 아웃바운드 엔드포인트를 사용하면 VPC 워크로드가 온프레미스 DNS 서버로 쿼리를 전달하여 온프레미스 도메인을 확인할 수 있습니다.

*   :material-earth: **Route 53 Global Resolver**

    ---

    지사, 온프레미스 사이트, 원격 사용자 등 VPC 외부 클라이언트를 위한 관리형 DNS 리졸버입니다. 선택한 리전의 애니캐스트 주소에서 퍼블릭 도메인과 프라이빗 호스팅 영역을 확인하며, 인터넷 또는 AWS Cloud WAN을 통해 DNS 필터링을 지원합니다.

*   :material-shield-lock: **DNS Firewall**

    ---

    DNS 확인 계층에서 도메인 기반 필터링을 수행합니다. 워크로드가 연결되기 전에 특정 도메인에 대한 쿼리를 차단, 허용 또는 알림 처리할 수 있습니다. 가장 저렴하고 광범위한 이그레스 제어 수단입니다.

*   :material-ip-network: **듀얼 스택 지원**

    ---

    Resolver 엔드포인트, 전달 규칙, DNS Firewall 모두 IPv4와 IPv6를 지원합니다. 프라이빗 호스팅 영역의 AAAA 레코드는 듀얼 스택 워크로드를 위해 A 레코드와 함께 동작합니다.

</div>

## 모범 사례 {#best-practices}

### 해석 아키텍처 {#resolution-architecture}

#### 모든 VPC의 유일한 DNS 리졸버로 Route 53 Resolver 사용 {#use-route-53-resolver-as-the-sole-dns-resolver-for-all-vpcs}

모든 VPC는 VPC+2 주소에 Route 53 Resolver를 자동으로 제공받습니다. VPC 워크로드의 기본 리졸버로 커스텀 DNS 서버(BIND, Active Directory DNS, Kubernetes 외부의 CoreDNS)를 배포하지 마십시오. 커스텀 리졸버는 운영 부담(패치, 확장, 모니터링)을 가중시키고, Route 53 Resolver에는 없는 단일 장애 지점을 만들며, Route 53 기능(DNS Firewall, 쿼리 로깅, Resolver 규칙)을 우회합니다. 유일하게 정당한 예외는 도메인 가입 해석을 위해 AD DNS가 필요한 Active Directory 가입 Windows 워크로드이며, 이 경우에도 AD 외 쿼리는 Route 53 Resolver로 다시 전달해야 합니다.

#### 하이브리드 DNS 해석을 위한 전달 규칙 설계 {#design-forwarding-rules-for-hybrid-dns-resolution}

AWS의 워크로드가 온프레미스 도메인 이름(예: `corp.example.com`)을 해석해야 할 경우, Resolver 아웃바운드 엔드포인트와 전달 규칙을 생성하여 해당 쿼리를 Direct Connect 또는 VPN을 통해 온프레미스 DNS 서버로 전송하십시오. 반대로, 온프레미스 워크로드가 AWS 프라이빗 호스팅 영역 이름을 해석해야 할 경우, 온프레미스 DNS 서버가 전달할 Resolver 인바운드 엔드포인트를 생성하십시오. 하나의 멀티 리전 애니캐스트 주소 세트로 서비스하려는 지사, 온프레미스 사이트, 원격 사용자에게는 [Route 53 Global Resolver](#global-resolver-for-clients-outside-vpcs)가 리전별 인바운드 엔드포인트의 대안입니다. 온프레미스 도메인을 해석하는 VPC 워크로드에는 아웃바운드 엔드포인트가 여전히 필요합니다.

전달 규칙은 가능한 한 구체적으로 설계하십시오. `.`(루트)가 아닌 `corp.example.com`을 온프레미스로 전달하십시오. 와일드카드 전달 규칙은 모든 DNS 트래픽을 온프레미스로 보내므로 모든 쿼리에 지연 시간이 추가되고, 모든 DNS 해석이 하이브리드 연결에 의존하게 되며, 전달된 쿼리에 대해 DNS Firewall을 우회합니다.

#### 여러 가용 영역에 Resolver 엔드포인트 배포 {#deploy-resolver-endpoints-across-multiple-availability-zones}

Resolver 인바운드 및 아웃바운드 엔드포인트는 지정한 서브넷에 ENI를 생성합니다. 각 엔드포인트에 대해 두 개의 가용 영역에 걸쳐 최소 두 개의 ENI를 배포하십시오. 단일 AZ 엔드포인트는 해당 엔드포인트에 의존하는 모든 DNS 해석의 단일 장애 지점이 됩니다. 하이브리드 환경에서는 해당 가용 영역에 문제가 발생하면 모든 경계 간 이름 해석이 실패합니다.

***핵심 인사이트:*** *DNS는 모든 네트워크에서 장애에 가장 민감한 의존성입니다. 30초간의 DNS 해석 실패는 아웃바운드 호출을 수행하는 모든 서비스에 걸쳐 연쇄적인 타임아웃을 유발합니다. 가장 중요한 워크로드와 동일한 가용성 기준으로 DNS 인프라를 설계하십시오.*

### VPC 외부 클라이언트를 위한 Global Resolver {#global-resolver-for-clients-outside-vpcs}

#### 지사, 온프레미스 사이트, 원격 사용자에게 Route 53 Global Resolver 사용 {#use-route-53-global-resolver-for-branch-offices-on-premises-sites-and-remote-users}

Route 53 Global Resolver는 VPC 외부의 인가된 클라이언트의 DNS 쿼리에 응답합니다. 퍼블릭 도메인과 DNS 뷰에 연결한 프라이빗 호스팅 영역을 해석하며, 클라이언트는 선택한 두 개 이상의 리전 중 가장 가까운 리전으로 각 쿼리를 라우팅하는 애니캐스트 IP 주소로 접근합니다. 리전이 사용 불가능해지면 쿼리는 다음으로 가까운 리전으로 장애 조치됩니다([작동 방식](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-how-it-works.html)). 클라이언트는 리전별 전달 규칙 대신 하나의 주소 세트를 사용하며, DNS 필터링이 뷰를 통해 이 클라이언트에 적용됩니다.

클라이언트의 위치와 기존 환경에 따라 Global Resolver와 Resolver 인바운드 엔드포인트 중 선택하십시오:

* VPC에 없는 클라이언트에 대해 멀티 리전 애니캐스트, 리전별 전달 없음, DNS 필터링이 필요한 경우 Global Resolver를 선택하십시오.
* 해석이 특정 VPC 내에 머물러야 하거나, 교체하지 않을 기존 리졸버 환경을 운영 중인 경우 인바운드 엔드포인트를 유지하십시오.

위에서 설명한 대로 VPC 워크로드는 VPC Resolver를 사용하십시오. VPC Resolver는 내장되어 있고, Route 53 Profiles, VPC별 DNS Firewall, Resolver 쿼리 로깅과 함께 작동하며, 관리할 액세스 소스 인가가 없습니다. 이는 권장 사항이지 제한이 아닙니다. [AWS 블로그](https://aws.amazon.com/blogs/networking-and-content-delivery/hybrid-dns-with-amazon-route-53-global-resolver-for-private-connections-on-aws-cloud-wan/)에서는 VPC 인스턴스가 Cloud WAN을 통해 Global Resolver를 쿼리하는 방법을 보여줍니다. VPC 워크로드를 Global Resolver로 보내는 경우, 두 번째 인가 모델과 필터링 및 로깅을 적용할 두 번째 위치를 관리해야 하며, VPC별 제어를 포기하게 됩니다. 아웃바운드 엔드포인트와 전달 규칙은 여전히 VPC 워크로드가 온프레미스 도메인에 접근하는 방법입니다.

리전 수를 선택하기 전에 비용을 계획하십시오. [Route 53 요금 페이지](https://aws.amazon.com/route53/pricing/)에서는 리전당 시간당 요금과 쿼리당 요금을 청구하며, 인터넷 액세스와 프라이빗(Cloud WAN) 액세스를 별도로 청구합니다.

처음부터 IPv6를 계획하십시오. 리졸버 주소 유형은 기본적으로 IPv4이며, 듀얼 스택은 IPv6 애니캐스트 주소를 추가합니다([CreateGlobalResolver](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_CreateGlobalResolver.html)). 클라이언트나 사이트가 듀얼 스택 또는 IPv6를 사용하는 경우 듀얼 스택을 선택하고, IPv6 액세스 소스를 IPv4 액세스 소스와 별도로 [할당량 페이지](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-load-balancer-limits.html)의 독립적인 차원으로 취급하십시오.

#### 액세스 경로 선택 및 인가 범위 최소화 {#choose-the-access-path-and-keep-authorization-narrow}

Global Resolver는 인터넷, AWS Cloud WAN, 또는 둘 다를 통해 접근할 수 있습니다. 인터넷을 통해서는 [액세스 제어 관리](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-managing-access-controls.html)에 설명된 대로 액세스 소스(CIDR 범위, DNS over port 53(Do53), DNS over TLS(DoT), DNS over HTTPS(DoH)용) 또는 액세스 토큰(DoT 및 DoH 전용)으로 클라이언트를 인가하십시오. 예측 가능한 주소를 가진 사무실과 VPN 이그레스에는 액세스 소스를, 주소가 변경되는 모바일 또는 원격 사용자에게는 토큰을 사용하십시오. 액세스 소스는 소스 IP 주소 신뢰에 의존하므로, 클라이언트가 허용하는 한 범위를 최대한 좁게 유지하십시오.

모든 클라이언트가 프라이빗 네트워크에 있는 경우, 퍼블릭 IP 연결을 비활성화하여 리졸버가 연결된 코어 네트워크에서만 접근 가능하도록 하십시오. 이를 위한 두 가지 방법이 있습니다([CreateGlobalResolver](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_CreateGlobalResolver.html)). 애니캐스트 주소를 예약한 채로 비활성화하면 나중에 동일한 주소로 퍼블릭 액세스를 다시 활성화할 수 있습니다. 주소를 해제하며 비활성화하면 주소가 해제되므로, 해당 주소로 구성된 클라이언트는 작동을 멈추고 리졸버는 동일한 주소를 다시 얻을 수 없습니다. 해당 주소가 더 이상 필요하지 않다고 확신하지 않는 한 예약을 사용하십시오.

#### Cloud WAN 연결을 신중하게 계획 {#plan-the-cloud-wan-connection-deliberately}

코어 네트워크 엔드포인트를 연결하면 리졸버가 실행되는 모든 리전에서 코어 네트워크의 세그먼트를 액세스 소스로 사용할 수 있게 되므로, DNS 소스로 신뢰하는 코어 네트워크만 연결하십시오. 엔드포인트를 생성하기 전에 다음을 계획하십시오([코어 네트워크 엔드포인트](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-core-network-endpoints.html), [AWS 블로그](https://aws.amazon.com/blogs/networking-and-content-delivery/hybrid-dns-with-amazon-route-53-global-resolver-for-private-connections-on-aws-cloud-wan/)):

* 하나의 Global Resolver는 하나의 코어 네트워크 엔드포인트를 통해 하나의 코어 네트워크에 연결됩니다.
* 엔드포인트는 리졸버의 리전에서 가져온 최소 두 개의 리전이 필요합니다. 엔드포인트당 프라이빗 IP 주소 수는 제한되어 있으므로 [할당량 페이지](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-load-balancer-limits.html)를 확인하십시오. 각 IP 주소는 서로 다른 리전 하위 집합과 연결할 수 있어 클라이언트를 다른 리전으로 유도하고 이중화를 위한 두 번째 IP를 제공합니다. 장애 조치가 가능하도록 각 IP 주소를 두 개 이상의 리전과 연결하십시오.
* 리졸버 IP 주소가 네트워크의 CIDR 블록이나 코어 네트워크의 내부 CIDR 블록과 충돌하지 않도록 하고, 퍼블릭 IP 주소를 외부로 라우팅하지 마십시오. 겹치는 경우 리졸버 주소로의 트래픽이 잘못된 경로를 따를 수 있습니다.
* 리전 세트를 신중하게 정렬하십시오. Global Resolver와 코어 네트워크 모두에 속한 리전만 해석을 제공할 수 있으므로, 둘 중 하나에만 있는 리전은 클라이언트에게 해석 경로를 제공하지 않습니다.
* 쿼리가 가장 가까운 리전으로 라우팅되도록 코어 네트워크 정책 버전 2026.10 이상을 사용하십시오. 해당 버전에서 Cloud WAN은 동등한 리전 간 경로 간의 타이를 기본 Multi-Exit Discriminator(MED)로 해소합니다. 라우팅 기본 설정을 지정하지 않은 경우, 동등한 경로가 여러 개인 목적지로의 트래픽은 업데이트가 적용될 때 한 번 다른 리전으로 이동할 수 있습니다. 업데이트 전에 엣지 위치 라우팅 정책으로 기본 설정을 지정하여 트래픽이 의도한 경로를 유지하도록 하십시오. [정책 버전](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policies-json.html#cloudwan-version-json)을 참조하십시오.
* DNS 뷰를 세그먼트에 의도적으로 매핑하십시오. 세그먼트의 클라이언트는 해당 세그먼트를 참조하는 액세스 소스가 있는 뷰를 통해 인가됩니다.
* 리졸버가 Direct Connect 인터페이스의 리전에서 실행되지 않는 경우, 쿼리는 가장 가까운 리전으로 가는 대신 동일 대륙의 모든 리졸버 리전에 ECMP됩니다. Direct Connect 인터페이스가 종료되는 리전에서 리졸버를 실행하는 것을 고려하십시오.
* Transit Gateway와 Direct Connect 게이트웨이 토폴로지도 Transit Gateway에서 Cloud WAN 네트워크로의 경로가 있는 한 리졸버에 대한 프라이빗 연결을 사용할 수 있습니다.

#### DNS 뷰를 사용하여 클라이언트 그룹 분리 {#use-dns-views-to-separate-client-groups}

DNS 뷰에는 자체 액세스 소스, 토큰, 방화벽 규칙, 프라이빗 호스팅 영역 연결이 있습니다([DNS 뷰 관리](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-manage-dns-views.html)). 보안 요구 사항, 위치, 또는 디바이스 유형이 다른 그룹에 대해 별도의 뷰를 생성하고, 각 뷰에 필요한 영역과 액세스만 부여하십시오. 세 가지 뷰 설정은 신중한 선택이 필요합니다:

* **DNSSEC 유효성 검사**는 퍼블릭 도메인에만 적용됩니다. 유효하지 않은 서명은 `SERVFAIL`을 반환합니다.
* **EDNS Client Subnet**은 부분 클라이언트 주소(IPv4의 경우 최대 /24, IPv6의 경우 최대 /48)를 권한 있는 서버로 전송합니다. CDN 라우팅을 개선할 수 있으며, 프라이버시 트레이드오프가 있습니다.
* **방화벽 페일 오픈**은 기본적으로 비활성화되어 있으므로, 방화벽 규칙을 평가할 수 없을 때 쿼리가 차단됩니다. 필터링보다 가용성이 더 중요한 경우에만 활성화하십시오.

네 가지 할당량 차원이 뷰 레이아웃을 결정하며, [할당량 페이지](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-load-balancer-limits.html)에 현재 값이 있습니다:

* **리졸버당 DNS 뷰**는 클라이언트 그룹을 얼마나 세밀하게 분할할 수 있는지를 제한합니다. 각 사무실마다 뷰를 만들기보다는 동일한 보안 요구 사항을 가진 그룹을 병합하십시오.
* **뷰당 방화벽 규칙**은 하나의 클라이언트 그룹이 가질 수 있는 필터링 정책의 양을 제한합니다. 도메인 목록을 사용하여 규칙 수를 낮게 유지하십시오.
* **리졸버당 액세스 소스**는 인가할 수 있는 별도 범위의 수를 제한합니다. 클라이언트가 허용하는 경우 범위를 요약하십시오.
* **리졸버당 총 액세스 소스 CIDR 크기**는 늘릴 수 없습니다. 넓은 범위는 이 예산을 소비하고 쿼리할 수 있는 대상도 넓히므로, 클라이언트를 포함하는 가장 좁은 범위를 인가하십시오.

#### 이 클라이언트에도 DNS 필터링 및 로깅 적용 {#apply-dns-filtering-and-logging-to-these-clients-too}

뷰의 DNS Firewall 규칙은 커스텀 또는 AWS 관리형 도메인 목록을 사용하여 쿼리를 허용, 경고, 또는 차단할 수 있으며, 도메인 생성 알고리즘 및 DNS 터널링에 대한 고급 보호 기능도 제공합니다. 이는 VPC의 Route 53 Resolver DNS Firewall을 보완하며 대체하지 않습니다. 리졸버를 생성할 때 관측성 리전을 설정하지 않으면 쿼리 로깅이 비활성화됩니다([CreateGlobalResolver](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_CreateGlobalResolver.html)). 로깅 없이는 이 클라이언트가 해석한 내용에 대한 DNS 기록이 없어, 이 모범 사례가 설명하는 포렌식 및 탐지 가치가 사라집니다. 로그는 선택한 단일 대상 리전으로 전송되므로([사용 사례](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-cloud-resolver-use-cases.html)), 감사 및 보존 요구 사항을 고려하여 해당 리전을 선택하십시오. Amazon CloudWatch Logs, Amazon Data Firehose, 또는 Amazon S3로 전달하십시오.

***핵심 인사이트:*** *액세스 및 인가 모델, 즉 누가 어떤 뷰를 통해 쿼리할 수 있는지가 다른 모든 Global Resolver 결정을 이끕니다. 리전, 주소, 로깅보다 먼저 결정하십시오.*

### 멀티 계정 DNS 공유 {#multi-account-dns-sharing}

#### 멀티 계정 DNS 배포에 Route 53 Profiles 사용 {#use-route-53-profiles-for-multi-account-dns-distribution}

Route 53 Profiles를 사용하면 프라이빗 호스팅 영역 연결, Resolver 전달 규칙, DNS Firewall 규칙 그룹을 단일 프로파일로 묶어 OU 수준에서 AWS RAM을 통해 공유할 수 있습니다. OU에 추가된 새 계정은 커스텀 자동화, 계정 간 Lambda 함수, 수동 연결 단계 없이 전체 DNS 구성을 자동으로 상속합니다.

Profiles 없이 계정 간에 DNS 구성을 공유하려면 계정별 프라이빗 호스팅 영역 연결(호스팅 영역당 VPC당 API 호출 1회), 계정별 전달 규칙 공유, 계정별 DNS Firewall 연결이 필요합니다. 이러한 자동화는 취약하고 감사하기 어렵습니다. Profiles는 이를 일급 작업으로 대체합니다.

#### AWS RAM을 통해 DNS 뷰 공유(Route 53 Profiles 아님) {#share-dns-views-through-aws-ram-not-route-53-profiles}

Global Resolver에는 자체 공유 모델이 있습니다. DNS 뷰는 AWS RAM을 통해 공유할 수 있으므로, 다른 계정이 영역이나 뷰의 소유권을 이전하지 않고도 자체 프라이빗 호스팅 영역을 연결할 수 있습니다([DNS 뷰 공유](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-sharing-dns-views.html)). 이는 VPC를 다루는 Route 53 Profiles와 별개입니다. 거버넌스를 위해 네 가지 사항이 중요합니다:

* **기본적으로 연결 전용 권한 부여.** 기본 AWS RAM 관리형 권한을 사용하면 소비자가 공유 뷰를 보고 자체 호스팅 영역을 연결할 수 있습니다. 다른 관리형 권한은 소비자가 공유 뷰를 업데이트, 활성화, 또는 비활성화할 수 있게 하며, 뷰 변경은 모든 리전의 해당 뷰의 모든 클라이언트에 영향을 미칩니다. 연결 이상의 권한 부여는 편의가 아닌 거버넌스 위험입니다.
* **기본적으로 영역 연결의 중앙 소유권.** 공유 뷰는 소비자가 뷰의 모든 클라이언트에 대해 해석되는 이름을 게시할 수 있게 합니다. 네트워킹 계정이 영역을 연결하고, 위임된 하위 영역에만 소비자 소유 연결을 사용하십시오. 계정별 영역은 아래에서 설명하는 것처럼 네임스페이스를 분산시킵니다.
* **데이터 상주.** 소비자의 호스팅 영역 ID와 도메인 이름은 소비자가 활성화하지 않은 옵트인 리전을 포함하여 소유자의 리졸버가 실행되는 모든 리전에 복사되므로, 신뢰하는 계정과만 뷰를 공유하고 데이터 상주 요구 사항을 확인하십시오.
* **공유 중지는 제거가 아닙니다.** 공유를 중지해도 기존 연결이 제거되지 않습니다. 소유자나 소비자가 제거할 때까지 계속 해석됩니다.

#### 네트워킹 계정에서 프라이빗 호스팅 영역 소유권 중앙화 {#centralize-private-hosted-zone-ownership-in-the-networking-account}

중앙 집중식 네트워킹 계정에서 프라이빗 호스팅 영역을 생성하고 관리하십시오. Route 53 Profiles를 통해 소비 계정에 공유하십시오. 이를 통해 네트워킹 팀이 권한 있는 DNS 네임스페이스를 제어하면서 애플리케이션 팀이 적절한 경우 위임된 하위 영역에 레코드를 생성할 수 있습니다.

대안인 각 계정이 자체 프라이빗 호스팅 영역을 생성하도록 허용하면 네임스페이스가 분산되고, 영역이 겹칠 때 해석 충돌이 발생하며, DNS Firewall과 쿼리 로깅을 일관되게 구현하기 어려워집니다.

이는 VPC Lattice 리소스 구성에도 적용됩니다. 소비자 VPC에 VPC Lattice가 관리할 커스텀 도메인 이름과 동일한 도메인에 대한 프라이빗 호스팅 영역이 있는 경우, VPC Lattice는 `PrivateDnsAlreadyExists`를 보고하고 영역을 변경하지 않습니다. 겹침을 해결하는 방법은 [안정적인 소비자 계약을 위한 커스텀 도메인 이름 사용](../connectivity/within-aws.md#use-custom-domain-names-for-stable-consumer-contracts)을 참조하십시오. AWS 문서에서는 Route 53 Profile을 통해 전달된 영역이 이를 트리거하는지 여부를 명시하지 않으므로, 어느 결과에도 의존하기 전에 레이아웃을 테스트하십시오.

#### 내부 네임스페이스 계층 구조를 신중하게 설계 {#design-your-internal-namespace-hierarchy-deliberately}

단일 내부 도메인(예: `internal.example.com`)을 선택하고 환경, 리전, 또는 서비스 도메인별로 하위 영역을 생성하십시오. 잘 설계된 계층 구조는 DNS 레코드를 자체 문서화하고 경로 기반 해석 정책을 가능하게 합니다:

```
internal.example.com           (root, networking account)
├── prod.internal.example.com  (production services)
├── dev.internal.example.com   (development services)
└── hybrid.internal.example.com (on-premises forwarding)
```

수백 개의 레코드가 단일 영역에 쌓이는 플랫 네임스페이스를 피하십시오. 길고 읽기 어려운 FQDN을 만드는 지나치게 깊은 계층 구조도 피하십시오. 루트 아래 2~3 수준이 적절합니다.

### 프라이빗 및 하이브리드 엔드포인트의 DNS 장애 조치 {#dns-failover-for-private-and-hybrid-endpoints}

#### 프라이빗 및 하이브리드 엔드포인트의 DNS 장애 조치를 위한 프라이빗 엔드포인트 상태 확인 사용 {#use-private-endpoint-health-checks-for-dns-failover-of-private-and-hybrid-endpoints}

Amazon Route 53 프라이빗 엔드포인트 상태 확인은 선택한 VPC에 Route 53이 배치하는 네트워크 인터페이스인 상태 확인 소스에서 HTTP, HTTPS, 또는 TCP를 통해 프라이빗 IP 주소나 도메인 이름을 프로브합니다. 대상이 실패하면 Route 53은 프라이빗 호스팅 영역의 레코드를 비정상으로 표시하고, 라우팅 정책은 정상 엔드포인트로 응답합니다. 대상에 퍼블릭 IP 주소 없이 내부 API, 데이터베이스, 내부 로드 밸런서 뒤의 대상, AWS Direct Connect 또는 AWS Site-to-Site VPN을 통한 온프레미스 엔드포인트의 액티브-패시브 장애 조치에 사용하십시오. CloudWatch 경보와 Route 53 API를 통해 레코드를 업데이트하는 Lambda 함수의 커스텀 루프를 대체하며, 이는 장애 조치에 몇 분이 걸리고 유지 관리해야 하는 코드입니다.

탐지와 레코드 변경은 몇 초 내에 이루어지도록 설계되었지만, 클라이언트는 캐시된 응답이 만료될 때만 이동합니다. 레코드 TTL과 리졸버 캐싱이 클라이언트가 경험하는 장애 조치 시간을 결정하므로, 장애 조치 레코드의 TTL을 짧게 유지하십시오.

프라이빗 엔드포인트 상태 확인이 **적합하지 않은** 경우:

* **대상에 퍼블릭 엔드포인트가 있는 경우.** 퍼블릭 상태 확인을 사용하십시오.
* **상태가 여러 확인을 결합하는 경우.** 계산된 상태 확인은 현재 프라이빗 엔드포인트 상태 확인을 참조할 수 없습니다([출시 시 가용성](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-private-endpoints.html#health-checks-private-endpoints-scope)). 오류율이나 큐 깊이와 같이 프로브가 측정할 수 없는 신호에는 CloudWatch 경보 기반 상태 확인을 사용하십시오.
* **클라이언트가 Route 53을 통해 해석하지 않는 경우.** 온프레미스 클라이언트는 Resolver 인바운드 엔드포인트나 Route 53 Global Resolver를 통해 Route 53을 통해 해석하는 경우에만 장애 조치를 따릅니다. 온프레미스 DNS가 해당 이름에 대해 권한이 있는 경우, 장애 조치를 볼 수 없습니다.

구성에 대해서는 [프라이빗 엔드포인트 상태 확인](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-private-endpoints.html) 및 [상태 확인 소스](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-check-sources.html)를 참조하십시오.

#### 레코드를 소유한 계정에 상태 확인 소스 배치 {#place-the-health-check-source-in-the-account-that-owns-the-records}

프라이빗 엔드포인트 상태 확인, 상태 확인 소스, 연결된 레코드는 동일한 계정에 있어야 합니다. 계정 간 연결은 지원되지 않으므로, 각 호스팅 영역을 소유한 계정이 확인과 소스의 위치를 결정합니다:

* **네트워킹 계정의 레코드.** [중앙 집중식 모델](#centralize-private-hosted-zone-ownership-in-the-networking-account)에서 네트워킹 계정이 소유한 영역의 레코드는 네트워킹 계정에 확인과 소스가 필요합니다. [AWS Transit Gateway 또는 AWS Cloud WAN을 통해 모든 대상에 접근하는](https://aws.amazon.com/blogs/networking-and-content-delivery/fast-failover-with-amazon-route-53-private-endpoint-health-checks/) 해당 계정의 공유 서비스 VPC를 사용하십시오. 워크로드 계정에서 생성된 확인은 해당 레코드와 연결할 수 없습니다.
* **위임된 하위 영역의 레코드.** 애플리케이션 계정이 하위 영역을 소유하는 경우, 해당 레코드는 대상에 대한 자체 접근 경로가 있는 VPC의 해당 애플리케이션 계정에 확인과 소스가 필요합니다.
* **할당량이 한 계정에 집중됩니다.** 중앙화하면 모든 팀의 확인이 네트워킹 계정의 계정당 상태 확인 및 계정당 상태 확인 소스 할당량에 집중되며, 각 소스에는 이를 사용하는 확인에 대한 자체 상한이 있습니다. 할당량에 도달하면 새 장애 조치 레코드에 확인을 추가할 수 없습니다. 팀 전체의 총합을 계획하고 현재 [상태 확인 할당량](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html#limits-api-entities-health-checks)을 확인하십시오.
* **접근 경로가 세분화를 가로지릅니다.** 모든 대상에 접근하는 소스는 대상을 보유한 모든 Transit Gateway 라우팅 테이블이나 Cloud WAN 세그먼트로의 경로가 필요합니다. 소스 VPC에 대상 네트워크에 접근하되 서로 연결하지 않는 자체 라우팅 테이블이나 세그먼트를 부여하고, 대상의 보안 그룹과 네트워크 ACL을 제어 지점으로 삼아 상태 확인 포트에서 소스의 서브넷만 허용하십시오.

#### 모니터링하는 장애 도메인 외부에 상태 확인 소스 배치 {#place-health-check-sources-outside-the-failure-domain-they-monitor}

프라이빗 엔드포인트 상태 확인은 소스의 리전에서만 실행되며, 상태, CloudWatch 지표, 경보는 해당 리전에 있습니다. 각 확인은 하나의 소스를 사용하고, 계산된 상태 확인은 프라이빗 확인을 결합할 수 없으므로, 레코드는 여러 소스가 아닌 하나의 확인 소스가 실행되는 위치의 복원력을 갖습니다. 해당 리전의 서비스 이벤트는 해당 리전에서 엔드포인트를 상태 확인하는 능력에 영향을 줄 수 있으며, 개발자 가이드는 그러한 이벤트 중 개별 확인의 동작을 설명하지 않습니다.

하나의 리전 이벤트가 대상과 이를 감시하는 확인 모두에 영향을 줄 수 없도록 소스를 배치하십시오:

* **여러 리전에 소스 분산.** 두 개 이상의 리전에 소스를 생성하여 한 리전의 이벤트가 해당 리전의 소스를 사용하는 확인에만 영향을 미치도록 하십시오([리전 고려 사항](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-private-endpoints.html#health-checks-private-endpoints-regional)).
* **다른 리전에 연결된 소스 VPC 사용.** VPC 피어링이나 Transit Gateway를 통해 한 리전의 소스가 다른 리전의 대상을 확인할 수 있으므로, 확인이 대상의 리전에서 실행될 필요가 없습니다.
* **기본 리전 외부에서 기본 확인.** 리전 간 재해 복구의 경우, 기본을 확인하는 소스를 해당 연결을 통해 DR 리전에서 실행하여 기본을 실패시키는 이벤트가 확인도 손상시키지 않도록 하십시오. 이는 개발자 가이드의 리전 지침에서 따릅니다. 가이드는 이를 재해 복구에 대한 권장 사항으로 명시하지 않습니다.
* **소스의 리전에서 경보 설정**, 확인의 상태와 지표가 있는 곳에서.

소스는 고정된 가용 영역 세트를 커버합니다. VPC가 하나의 소스가 커버하는 것보다 더 많은 가용 영역에 걸쳐 있는 경우, 나머지 가용 영역의 대상에는 추가 소스가 필요합니다.

#### 소스에서의 네트워크 경로를 확인의 일부로 취급 {#treat-the-network-path-from-the-source-as-part-of-the-check}

프라이빗 엔드포인트 상태 확인은 클라이언트가 아닌 소스에서의 도달 가능성을 측정합니다. 경로상에서 실패하거나 트래픽을 삭제하는 모든 것은 실패한 대상처럼 보입니다:

* **네트워크 액세스.** 보안 그룹과 네트워크 ACL은 소스에서 대상으로의 트래픽을 허용해야 하며, 소스의 보안 그룹은 양방향 트래픽을 허용해야 합니다([출시 블로그](https://aws.amazon.com/blogs/networking-and-content-delivery/fast-failover-with-amazon-route-53-private-endpoint-health-checks/)). 온프레미스 대상의 경우, Direct Connect 또는 VPN 경로의 방화벽이 동일한 역할을 하지만, AWS 문서는 보안 그룹과 네트워크 ACL만 언급합니다. 이 중 하나라도 상태 확인 트래픽을 삭제하면, 확인은 정상 대상을 비정상으로 보고하고 레코드를 장애 조치합니다.
* **하이브리드 경로 실패.** 소스와 온프레미스 대상 사이의 Direct Connect 또는 VPN 실패는 인바운드 엔드포인트를 통해 해석하는 온프레미스 클라이언트와 같이 여전히 접근할 수 있는 클라이언트가 있더라도 대상을 비정상으로 표시합니다. 대상과 동일한 이중화 기준으로 하이브리드 경로를 구축하십시오.
* **FQDN 해석.** 도메인 이름으로 확인되는 대상의 경우, Route 53은 DHCP 옵션 세트의 커스텀 DNS 서버가 아닌 VPC의 Route 53 Resolver를 통해서만 이름을 해석합니다. VPC에는 DNS 해석이 활성화되어 있고 프라이빗 범위의 기본 IPv4 CIDR 블록이 있어야 합니다. 온프레미스 DNS만 해석하는 이름에는 Resolver 전달 규칙, 프라이빗 호스팅 영역 연결, 또는 IP 주소에 대한 확인이 필요하며, 그렇지 않으면 확인이 실패합니다.
* **IPv6.** 도메인 이름으로 확인하는 경우 이름의 A 레코드를 조회하고 해당 IPv4 주소만 프로브합니다. 듀얼 스택 대상의 IPv6 경로가 끊어지면 확인은 정상 상태를 유지하고 Route 53은 AAAA 레코드를 계속 반환하므로 IPv6 클라이언트가 실패합니다. 이름에 A 레코드가 없으면 확인은 "DNS resolution failed"로 실패합니다. AAAA 레코드에 대상의 IPv6 주소에 대한 자체 확인을 부여하고, 대상의 보안 그룹과 네트워크 ACL에서 소스의 IPv6 범위를 허용하십시오. 듀얼 스택 VPC의 소스는 IPv6 대상을 프로브할 수 있습니다. AWS 문서는 소스가 IPv6 전용 서브넷을 지원하는지 여부를 명시하지 않으므로, 이에 의존하기 전에 검증하십시오.

#### 소스 구성을 사전에 결정 {#decide-the-sources-configuration-up-front}

상태 확인 소스를 생성한 후에는 VPC, 서브넷, 보안 그룹을 변경할 수 없으므로, 첫 번째 확인이 소스에 의존하기 전에 결정하십시오. 소스를 생성하기 전에:

* **코드로 관리.** 소스와 확인을 인프라 코드로 정의하여 소스 교체가 수동 마이그레이션이 아닌 제어된 변경이 되도록 하십시오.
* **서비스 연결 역할 권한 유지.** 소스를 생성하거나 삭제하는 모든 요청은 역할이 이미 존재하더라도 `AWSServiceRoleForRoute53PrivateHealthChecks`에 대해 `iam:CreateServiceLinkedRole`을 호출합니다. SCP, 권한 경계, 또는 파이프라인 역할이 이를 차단하면 요청이 실패합니다.
* **비용 제어를 위한 소스 공유.** 소스는 확인 사용 여부에 관계없이 존재하는 동안 가용 영역 연결당 시간당 요금이 청구되므로, 요금은 소스 수와 커버하는 가용 영역에 따라 확장됩니다. 각 확인은 월별 요금과 HTTPS, 문자열 매칭, 빠른 요청 간격과 같은 각 선택적 기능에 대한 요금이 청구됩니다([Route 53 요금](https://aws.amazon.com/route53/pricing/)). 팀당 하나보다 리전당 몇 개의 공유 소스가 비용이 적게 들며, 교체 중에는 두 소스 모두에 대한 요금이 발생합니다.

***핵심 인사이트:*** *프라이빗 엔드포인트 상태 확인은 소스가 접근할 수 있는 것만 보고합니다. 소스를 레코드를 소유한 계정에, 대상의 장애 도메인 외부에, 대상이 실패할 때만 실패하는 경로에 배치하십시오.*

### DNS 보안 {#dns-security}

#### 모든 VPC에 DNS Firewall 배포 {#deploy-dns-firewall-in-every-vpc}

Route 53 Resolver DNS Firewall은 AWS에서 가장 저렴하고 광범위한 이그레스 제어입니다. VPC에서 이루어지는 모든 DNS 쿼리를 도메인 목록(AWS의 관리형 위협 인텔리전스 목록 또는 커스텀 목록)에 대해 평가하고 차단, 허용, 또는 경고할 수 있습니다. 사실상 모든 아웃바운드 연결은 DNS 조회로 시작하므로, 악성 도메인의 해석을 차단하면 연결 시도 자체를 방지합니다.

Route 53 Profiles를 통해 DNS Firewall 규칙 그룹을 배포하여 조직의 모든 VPC가 동일한 기본 보호를 받도록 하십시오. DNS를 우회하는 트래픽(하드코딩된 IP, DNS-over-HTTPS)에 대해서는 Network Firewall이나 서드파티 검사와 계층화하십시오.

관리형 위협 목록 외에도, 워크로드에 필요한 모든 도메인을 알지 못할 때 허용 목록 모드(승인된 도메인만 허용하고 나머지는 차단)의 실용적인 경로는 [자동화된 허용 목록 규칙](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/firewall-advanced-automated-allowlists.html)입니다. DNS Firewall은 조회 기간 동안 VPC가 쿼리한 도메인을 나열하며, 처음부터 목록을 작성하는 대신 검토하고 승인합니다. 이 규칙은 DNS Firewall Advanced 계층이 필요하며, 그 뒤에 전체 차단 규칙을 추가할 때까지 아무것도 적용하지 않습니다. 이전의 전체 차단 규칙은 합법적인 트래픽을 차단하므로, 목록을 검토한 후에만 추가하십시오. 규칙 순서와 차단 전 확인 사항은 아웃바운드 제어의 [자동화된 허용 목록 규칙으로 허용 목록 구축](../security/outbound.md#build-the-allow-list-with-an-automated-allowlist-rule)을 참조하십시오.

자세한 DNS Firewall 모범 사례와 다른 이그레스 제어와의 통합에 대해서는 [아웃바운드 제어](../security/outbound.md)를 참조하십시오.

#### 가시성 및 포렌식을 위한 Resolver 쿼리 로깅 활성화 {#enable-resolver-query-logging-for-visibility-and-forensics}

Resolver 쿼리 로깅은 연결된 VPC에서 이루어지는 모든 DNS 쿼리(쿼리 이름, 유형, 응답 코드, 소스 IP, 타임스탬프)를 캡처합니다. 비용 효율적인 보존 및 Athena 쿼리를 위해 S3로, 또는 의심스러운 해석 패턴(알려진 C2 도메인에 대한 쿼리, 고빈도 NXDOMAIN 응답, 단일 소스의 비정상적인 쿼리 볼륨)에 대한 실시간 경보를 위해 CloudWatch Logs로 로그를 전달하십시오.

쿼리 로깅은 VPC Flow Logs의 DNS 버전입니다. 워크로드가 이름으로 접근하려 한 것의 완전한 기록을 제공합니다. 이 없이는 DNS 관련 인시던트(DNS 터널링을 통한 데이터 유출, C2 콜백, 잘못 구성된 전달)를 조사하는 데 추측에 의존해야 합니다.

#### DNS 쿼리 로그와 DNS Firewall 활동을 지표와 경보로 전환 {#turn-dns-query-logs-and-dns-firewall-activity-into-metrics-and-alarms}

DNS 활동을 단순히 보존하는 것이 아니라 경보를 발생시키려면, Resolver 쿼리 로그를 CloudWatch Logs로 전달하십시오. 지표 필터, Contributor Insights, Logs Insights는 포렌식용으로 보관하는 S3 복사본이 아닌 로그 그룹에서 실행됩니다. DNS Firewall은 또한 VPC별 및 규칙 그룹별 쿼리 볼륨 지표를 몇 분마다 CloudWatch에 게시하며, 로그를 파싱하지 않고도 직접 경보를 설정할 수 있습니다.

고정 횟수가 아닌 설정한 기준선에 대해 경보를 설정하십시오. 쿼리 로그는 고유한 쿼리만 기록하므로 캐시에서 응답된 조회는 로깅되지 않아 횟수가 낮게 나타납니다. 이를 예방이 아닌 탐지로 취급하십시오. 리졸버에 도달하는 것만 볼 수 있으므로, DNS-over-HTTPS 및 하드코딩된 IP 트래픽은 우회합니다. 이러한 트래픽에는 Network Firewall이나 다른 검사를 유지하십시오.

### 중요 레코드 보호 {#protecting-critical-records}

#### 중요 레코드를 실수로 변경되지 않도록 보호 {#protect-critical-records-from-accidental-change}

Route 53 레코드 세트 보호는 퍼블릭 및 프라이빗 호스팅 영역에서 보호된 이름과 유형의 레코드를 생성, 업데이트, 또는 삭제하는 모든 `ChangeResourceRecordSets` 요청을 거부합니다. 보호는 전체 Route 53 권한을 가진 주체를 포함한 모든 주체에 적용되므로, 직접 변경이 차단되고 의도적인 추가 단계가 강제됩니다. 실수를 방지하며 보안 경계는 아닙니다. `route53:*`와 같은 광범위한 권한을 가진 주체는 보호를 삭제한 다음 레코드를 변경할 수도 있습니다(아래 권한 지침 참조). 실수로 변경되면 중단이 발생하는 레코드, 예를 들어 프로덕션 도메인의 apex 레코드, MX 레코드, 중요 엔드포인트로 트래픽을 라우팅하는 레코드에 사용하십시오. 실수가 비용이 많이 드는 몇 가지 레코드만 보호하십시오. 각 보호는 일상적인 변경을 권한 있는 두 단계 변경으로 전환하며, 호스팅 영역당 보호 수는 [할당량](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html#limits-api-entities-records)으로 제한되므로, 광범위하게 보호하면 일상적인 변경이 느려지고 해당 할당량을 소진할 수 있습니다.

의존하기 전에 동작을 파악하십시오:

* **범위는 이름과 유형입니다.** 하나의 보호는 세트 식별자에 관계없이 해당 이름과 유형의 모든 레코드를 커버합니다. 가중치 레코드 세트의 일부만 보호할 수 없습니다. 유형은 범위의 일부입니다. `A`에 대한 보호는 동일한 이름의 `AAAA`를 커버하지 않으므로, 듀얼 스택 이름에는 각각에 대한 보호가 필요합니다. `A`만 보호된 경우, 누군가 `AAAA` 레코드를 변경하거나 삭제할 수 있으며, IPv4 클라이언트는 계속 작동하는 동안 IPv6 클라이언트가 실패하는 발견하기 어려운 부분 중단이 발생합니다.
* **거부는 전체 배치입니다.** 요청의 변경 사항 중 하나라도 보호된 이름과 유형에 접촉하면, Route 53은 `InvalidChangeBatch`로 전체 요청을 거부하고 아무것도 적용하지 않습니다. 보호된 레코드에 접촉하는 변경은 AWS CLI, AWS SDK, AWS CloudFormation에서 실패합니다. [Route 53 문서](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/rrset-protection.html#rrset-protection-blocked-changes)와 [CloudFormation 참조](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-recordsetprotection.html#aws-resource-route53-recordsetprotection--remarks)는 오류를 다르게 명명하므로(`InvalidChangeBatch`와 `ResourceConflict`), 런북이나 경보를 하나의 오류 이름에 연결하지 마십시오.
* **CloudFormation 업데이트는 순서가 있습니다.** CloudFormation은 레코드를 변경한 후 정리 단계에서만 제거된 보호를 삭제하므로, 보호된 레코드를 변경하고 보호를 제거하는 스택 업데이트가 실패합니다. 하나의 업데이트에서 보호를 추가하고 동일한 레코드를 변경하면 스택이 실패한 롤백 상태가 될 수 있으며, 보호의 주석을 변경하면 교체되므로 교체 중에 레코드가 보호되지 않습니다. 예를 들어 `DeletionPolicy: Retain`으로 남겨진 보호는 레코드 삭제를 차단하고 해체를 실패시킵니다. 레코드 변경과 보호 변경을 별도의 스택 업데이트나 파이프라인 단계로 제공하고, 하나의 파이프라인이 남겨진 보호 제거를 소유하도록 하십시오. CloudFormation 참조에 절차가 설명되어 있습니다.
* **보호는 이름을 예약할 수 있습니다.** 아직 레코드가 없는 이름과 유형에 대해 보호를 생성할 수 있으며, 이는 누구도 해당 레코드를 생성하지 못하도록 합니다.
* **유용한 주석 작성.** 선택적 주석(최대 256자)은 변경이 거부될 때 오류에 표시됩니다. 레코드가 보호된 이유와 연락할 사람을 명시하십시오.

보호된 레코드 변경은 의도적입니다. 보호를 삭제하고, 변경하고, 보호를 다시 생성하십시오. 보호는 편집할 수 없으므로, 주석을 변경하는 것도 삭제하고 다시 생성하는 것을 의미합니다. 이를 변경 프로세스와 런북에 계획하십시오. 보호가 다시 생성될 때까지 변경 권한이 있는 모든 주체가 레코드를 변경할 수 있으며, 변경 단계가 실패하고 보호를 다시 생성하지 않으면 레코드는 신호 없이 보호되지 않은 상태로 남습니다. 자동화가 삭제, 변경, 재생성을 실패 시 보호를 복원하는 하나의 단위로 취급하도록 하고, `DeleteResourceRecordSetProtections` 호출에 대해 경보를 설정하십시오. [AWS CloudTrail](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/logging-using-cloudtrail.html)은 보호 생성, 삭제, 목록 요청을 로깅합니다.

보호는 제거할 수 있는 사람만큼만 강력합니다. 호스팅 영역에 대해 `route53:DeleteResourceRecordSetProtections`를 가진 모든 주체는 해당 영역의 모든 보호를 삭제할 수 있으며, 세 가지 레코드 세트 보호 작업(생성, 삭제, 목록)은 호스팅 영역 리소스만 지원하고 서비스별 조건 키가 없습니다. 해당 권한을 소수의 관리자에게만 부여하고 다른 모든 사람에게는 거부하는 것을 고려하십시오. 네트워킹 계정이 호스팅 영역을 소유하는 AWS Organizations 환경에서는 호스팅 영역을 소유한 계정이 포함된 OU에 [서비스 제어 정책](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)(SCP) 거부를 적용하고, 중앙 DNS 또는 네트워킹 관리자 역할을 면제하십시오. SCP는 관리 계정에 적용되지 않으며, 작업에 조건 키가 없으므로 동일한 영역에서 일부 보호 제거를 허용하고 다른 것을 거부할 수 없습니다. 보호는 가장 광범위한 삭제 권한만큼만 강력합니다.

레코드가 없는 이름에 대한 보호를 포함하여 보호가 있는 호스팅 영역은 삭제할 수 없습니다. 먼저 보호를 나열하고 삭제하는 단계를 해체 자동화에 추가하십시오.

보호는 Route 53이 DNS 쿼리에 응답하는 방식을 변경하지 않습니다. 레코드 변경만 제어합니다.

***핵심 인사이트:*** *레코드 세트 보호는 실수를 방지하며, 의도적인 변경은 방지하지 않습니다. 보호를 삭제할 수 있는 사람에 대한 제어만큼만 강력합니다.*

콘솔 및 CLI 단계는 [변경으로부터 레코드 보호](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/rrset-protection.html)를 참조하십시오. 보호 제거를 거부하는 예시 정책은 [예시 5: 레코드 세트 보호 제거 거부](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/access-control-managing-permissions.html#access-policy-example-deny-delete-rrset-protections)를 참조하십시오.

#### 리졸버가 따르는 경우에만 위임 NS 레코드 보호 {#protect-delegation-ns-records-only-where-a-resolver-follows-them}

상위 영역의 위임 NS 레코드는 리졸버가 이를 따라 하위 영역의 네임 서버에 도달할 때만 중요합니다. 해당 경우에 보호하고 그 외에는 건너뛰십시오.

**퍼블릭 위임: 레코드 보호.** 인터넷 리졸버는 상위 영역의 NS 레코드에서 퍼블릭 하위 영역의 네임 서버를 학습합니다. 누군가 해당 레코드를 변경하거나 삭제하면, 자체 레코드는 그대로인데도 전체 하위 영역의 해석이 중단됩니다. 상위 영역의 계정이 하위 도메인을 애플리케이션 계정의 영역에 위임할 때, 상위 영역의 보호는 일상적인 자동화와 애플리케이션 계정의 역할이 위임을 변경하지 못하도록 합니다. 하위 영역을 다시 생성하면 재사용 가능한 위임 세트를 사용하지 않는 한 새로운 네임 서버 세트가 생성됩니다. 네임 서버가 변경되면 상위 레코드를 업데이트하려면 먼저 보호를 제거해야 하며, 이것이 보호가 강제하는 의도적인 단계입니다. 하위 영역이 DNSSEC로 서명된 경우, 상위 영역의 DS 레코드도 보호하십시오. 보호는 하나의 레코드 유형을 커버하므로, `NS`를 보호하면 `DS`가 열려 있으며, 누락되거나 잘못된 DS 레코드는 전체 하위 영역에 대해 유효성 검사 리졸버를 실패시킵니다. 서명된 하위 영역을 다시 생성하면 새로운 키 서명 키도 생성되며 상위에 새 DS 레코드가 필요합니다. 위임 작동 방식은 [하위 도메인에 대한 트래픽 라우팅](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-routing-traffic-for-subdomains.html)을, DS 레코드는 [DNSSEC 서명 활성화 및 신뢰 체인 구축](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec-enable-signing.html)을 참조하십시오.

**AWS에서 호스팅되는 프라이빗 영역: 레코드에 의존하지 마십시오.** Route 53 Resolver는 이름과 일치하고 VPC와 연결된 가장 구체적인 프라이빗 호스팅 영역에서 쿼리에 응답하므로, 프라이빗 하위 영역은 상위 영역의 NS 레코드가 아닌 VPC 연결을 통해 해석됩니다. 해당 NS 레코드를 삭제해도 하위 영역을 해석 불가능하게 만들지 않습니다. 하위 영역의 VPC 연결을 제거하면 됩니다. 따라서 NS 레코드를 보호하는 것은 이 페이지 앞에서 설명한 중앙 상위 영역과 하위 영역 패턴에 아무것도 추가하지 않습니다. VPC 연결에 대한 레코드 보호는 없으므로, 대신 IAM으로 제어하십시오. 중앙 DNS 관리자 역할을 제외한 모든 사람에게 `route53:DisassociateVPCFromHostedZone`을, Route 53 Profiles가 영역을 배포하는 경우 `route53profiles:DisassociateResourceFromProfile`과 `route53profiles:DisassociateProfile`을 거부하십시오. 이러한 호출이 이루어지는 계정을 커버하는 SCP로 거부를 적용하십시오. Profile 작업은 일반적으로 VPC를 소유한 계정에서 실행되며, 이는 호스팅 영역을 보유한 OU와 다를 수 있습니다. 거부는 애플리케이션 팀이 Profile이나 연결을 직접 분리하는 것도 막으므로, VPC 해체를 포함한 해당 요청을 중앙 DNS 관리자 역할을 통해 라우팅하십시오. 매칭 규칙은 [프라이빗 호스팅 영역 작업 시 고려 사항](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-considerations.html)을 참조하십시오.

**외부 네임 서버에 위임된 프라이빗 영역: 레코드 보호.** 프라이빗 호스팅 영역이 Resolver 위임 규칙을 통해 하위 도메인을 온프레미스 또는 퍼블릭 네임 서버에 위임하는 경우, NS 레코드가 Route 53 Resolver가 따르는 것입니다. 퍼블릭 위임처럼 취급하십시오. 위임이 프라이빗 호스팅 영역의 글루 레코드를 사용하는 경우, 해당 `A` 및 `AAAA` 레코드도 보호하십시오. 이는 네임 서버의 주소를 보유하며, NS 레코드에 대한 보호는 이를 커버하지 않으므로, 변경된 글루 레코드는 Resolver를 잘못된 IP 주소로 보냅니다. [Resolver 위임 규칙](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/outbound-delegation-tutorial.html)을 참조하십시오.

보호는 상위 영역의 레코드만 커버합니다. 하위 영역 소유자가 하위 영역의 레코드를 변경하거나 삭제하는 것을 막지 않으며, 이는 더 이상 응답하지 않는 네임 서버를 가리키는 위임을 남깁니다. 하위 영역 자체를 보호하려면 하위 영역의 apex `NS` 및 `SOA` 레코드를 보호하십시오. Route 53은 여전히 관리하는 apex 레코드를 업데이트하며, 보호가 있는 호스팅 영역은 삭제할 수 없으므로 하위 영역 삭제에도 동일한 의도적인 추가 단계가 필요합니다. 이는 실수를 방지하며 의도적인 변경은 방지하지 않습니다. 하위 영역에서 보호를 삭제할 수 있는 사람은 누구나 제거할 수 있기 때문입니다.

***핵심 인사이트:*** *리졸버가 따르는 경우에만 위임 NS 레코드를 보호하십시오. 퍼블릭 위임과 외부 네임 서버에 대한 위임이 해당됩니다. AWS에서 호스팅되는 프라이빗 하위 영역은 상위의 NS 레코드가 아닌 VPC 연결을 통해 해석됩니다.*

### IPv6 고려 사항 {#ipv6-considerations}

#### 처음부터 듀얼 스택 Resolver 엔드포인트 구성 {#configure-dual-stack-resolver-endpoints-from-the-start}

Resolver 인바운드 및 아웃바운드 엔드포인트는 IPv6 ENI 주소를 지원합니다. VPC가 듀얼 스택인 경우, IPv6 전용 워크로드가 NAT64 없이 전달하고 해석할 수 있도록 IPv4와 IPv6 주소 모두로 Resolver 엔드포인트를 구성하십시오. AWS 인바운드 엔드포인트로 전달하는 온프레미스 DNS 서버는 온프레미스 네트워크도 듀얼 스택인 경우 엔드포인트의 IPv6 주소에 대한 도달 가능성이 필요합니다.

#### Global Resolver 생성 시 듀얼 스택 선택 {#choose-dual-stack-when-you-create-a-global-resolver}

Global Resolver는 기본적으로 IPv4 애니캐스트 주소를 사용하며, 듀얼 스택은 IPv6 애니캐스트 주소를 추가합니다. 지사, 온프레미스, 또는 원격 클라이언트가 IPv6를 사용하는 경우, IPv4 경로에 의존하지 않고 IPv6를 통해 리졸버에 접근할 수 있도록 듀얼 스택을 선택하십시오. IPv6 액세스 소스는 자체 차원으로 제한되므로 IPv4 액세스 소스와 별도로 계획하십시오. [VPC 외부 클라이언트를 위한 Global Resolver](#global-resolver-for-clients-outside-vpcs)를 참조하십시오.

#### 프라이빗 호스팅 영역에서 A 레코드와 함께 AAAA 레코드 포함 {#include-aaaa-records-alongside-a-records-in-private-hosted-zones}

듀얼 스택 인프라에서 실행되는 모든 내부 서비스에 대해 프라이빗 호스팅 영역에 A 레코드와 AAAA 레코드를 모두 게시하십시오. IPv6를 선호하거나 IPv6 전용으로 실행되는 애플리케이션은 AAAA 레코드를 사용하고, IPv4 전용 소비자는 A 레코드를 사용합니다. 이는 듀얼 스택 VPC 설계와 동일한 원칙입니다. 나중에 개조하는 것보다 처음부터 IPv6를 포함하십시오.

## Route 53 Resolver 기능 사용 시기 {#when-to-use-route-53-resolver-features}

Route 53 Resolver는 항상 사용 중입니다. 모든 VPC의 기본 리졸버이기 때문입니다. 결정해야 할 사항은 어떤 추가 기능을 활성화할지입니다.

**프라이빗 호스팅 영역**은 다음과 같은 경우에 적합합니다.

* 공용 인터넷에서 확인할 수 없어야 하는 서비스, 데이터베이스 또는 엔드포인트에 내부 DNS 이름이 필요한 경우
* 스플릿 호라이즌 DNS(쿼리가 AWS 내부에서 오는지 외부에서 오는지에 따라 동일한 도메인에 대해 다른 응답을 반환)가 필요한 경우

**리졸버 엔드포인트 및 전달 규칙**은 다음과 같은 경우에 적합합니다.

* 온프레미스 워크로드가 AWS 프라이빗 호스팅 영역 이름을 확인해야 하는 경우(인바운드 엔드포인트)
* AWS 워크로드가 온프레미스 도메인 이름을 확인해야 하는 경우(아웃바운드 엔드포인트 + 전달 규칙)
* AWS 경계를 넘는 DNS 의존성이 있는 하이브리드 환경에서 운영하는 경우

**Route 53 Global Resolver**는 다음과 같은 경우에 적합합니다.

* 지사, 온프레미스 사이트 또는 원격 사용자가 모든 리전에 리졸버 엔드포인트 없이 프라이빗 호스팅 영역 이름을 확인해야 하는 경우
* 멀티 리전 장애 조치 및 VPC 외부 클라이언트를 위한 DNS 필터링이 포함된 단일 애니캐스트 주소 세트를 원하는 경우
* AWS Cloud WAN을 통해 해당 클라이언트를 연결하고 프라이빗 전용 DNS 확인을 원하는 경우

Global Resolver는 다음과 같은 경우에는 **적합하지 않습니다**.

* 클라이언트가 VPC 워크로드인 경우(VPC Resolver 사용)
* 사이트에 기존 리졸버 환경에 대한 조건부 전달이 필요하고 Cloud WAN 또는 애니캐스트 요구 사항이 없는 경우(리졸버 인바운드 엔드포인트 사용)
* 클라이언트를 소스 주소, 세그먼트 또는 토큰으로 인증할 수 없는 경우(기존 리졸버 유지)

**프라이빗 엔드포인트 상태 확인**은 다음과 같은 경우에 적합합니다.

* 프라이빗 호스팅 영역의 레코드가 프라이빗 엔드포인트 간, 리전 간 또는 Direct Connect나 Site-to-Site VPN을 통한 온프레미스 엔드포인트로의 DNS 장애 조치가 필요한 경우
* 프라이빗 대상의 레코드를 업데이트하기 위해 사용자 지정 CloudWatch 경보 및 Lambda 루프를 실행하는 경우

프라이빗 엔드포인트 상태 확인은 다음과 같은 경우에는 **적합하지 않습니다**.

* 대상에 퍼블릭 엔드포인트가 있는 경우(표준 퍼블릭 상태 확인 사용)
* 장애 조치가 여러 확인에 걸친 복합 상태에 의존하는 경우(계산된 상태 확인은 현재 프라이빗 확인을 참조할 수 없으므로 CloudWatch 경보 기반 상태 확인 사용)
* 클라이언트가 Route 53이 응답하지 않는 DNS 서버를 통해 이름을 확인하는 경우(장애 조치 레코드는 해당 클라이언트에 효과가 없음)

**Route 53 Profiles**는 다음과 같은 경우에 적합합니다.

* 여러 계정을 운영하며 모든 계정에 걸쳐 일관된 DNS 구성이 필요한 경우
* 사용자 지정 자동화 없이 새 계정이 DNS 구성을 자동으로 상속받기를 원하는 경우

**DNS Firewall**은 모든 VPC에 적합합니다. AWS 관리형 위협 도메인 목록을 최소한으로라도 배포하지 않아야 할 시나리오는 없습니다.

## 문서 {#documentation}

### Resolver, Profiles, 및 Global Resolver {#resolver-profiles-and-global-resolver}

<div class="grid cards" markdown>

*   :material-file-document: **Route 53 Resolver 문서**

    ---

    Resolver 엔드포인트, 전달 규칙, 쿼리 로깅, DNSSEC 검증에 대한 전체 문서입니다.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html)

*   :material-file-document: **Route 53 Profiles 문서**

    ---

    다중 계정 DNS 구성 배포를 위한 Profiles 생성, 공유 및 관리 방법입니다.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profiles.html)

*   :material-file-document: **Route 53 Resolver DNS Firewall**

    ---

    도메인 기반 필터링 구성, 관리형 도메인 목록, Firewall Manager와의 통합입니다.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall.html)

*   :material-file-document: **Route 53 Global Resolver 문서**

    ---

    Global Resolver의 개념, DNS 뷰, 액세스 제어, 코어 네트워크 엔드포인트, 공유 및 할당량입니다.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-what-is-global-resolver.html)

</div>

### 레코드 보호 및 상태 확인 {#record-protection-and-health-checks}

<div class="grid cards" markdown>

*   :material-file-document: **변경으로부터 레코드 보호**

    ---

    레코드 세트 보호의 작동 방식, 보호할 레코드, 거부된 변경 및 영역 삭제 동작, 제거를 제어하는 권한에 대한 설명입니다.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/rrset-protection.html)

*   :material-file-document: **AWS::Route53::RecordSetProtection**

    ---

    업데이트 순서, 롤백 동작, 기존 보호 가져오기를 포함한 보호 관리를 위한 CloudFormation 리소스입니다.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-recordsetprotection.html)

*   :material-file-document: **프라이빗 엔드포인트 상태 확인**

    ---

    프라이빗 엔드포인트 상태 확인 및 상태 확인 소스의 작동 방식, 리전 및 계정 범위, 설정 고려 사항, 현재 지원되는 항목입니다.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-private-endpoints.html)

*   :material-file-document: **상태 확인 소스**

    ---

    프라이빗 엔드포인트 상태 확인이 실행되는 소스에 대한 네트워크 구성, 가용 영역 커버리지, 불변성, 서비스 연결 역할 권한입니다.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-check-sources.html)

</div>

### 블로그 게시물 및 요금 {#blog-posts-and-pricing}

* [Route 53 블로그 게시물](https://aws.amazon.com/blogs/networking-and-content-delivery/category/networking-content-delivery/amazon-route-53/): AWS 네트워킹 및 콘텐츠 전송 블로그의 아키텍처 패턴, 기능 발표 및 구현 가이드입니다.
* [Route 53 요금](https://aws.amazon.com/route53/pricing/): 호스팅 영역, 쿼리, 상태 확인, 상태 확인 소스에 대한 요금 항목입니다.

## 관련 페이지 {#related-pages}

**다른 기반 주제와의 관계:**

* **[Amazon VPC](vpc.md)**: 모든 VPC에는 Route 53 Resolver가 자동으로 제공됩니다. VPC 설계(VPC 수, 계정 배치)에 따라 필요한 프라이빗 호스팅 영역 연결 수와 Resolver 엔드포인트 수가 결정됩니다.
* **[AWS Organizations](organizations.md)**: Route 53 Profiles는 OU 수준에서 DNS 구성을 공유하며, OU의 SCP는 레코드 세트 보호를 제거할 수 있는 주체를 제한합니다. OU 구조에 따라 DNS 구성이 배포되는 방식과 해당 제어가 적용되는 위치가 결정됩니다.

**연결 주제와의 관계:**

* **[하이브리드 및 멀티 클라우드 연결](../connectivity/hybrid-multicloud.md)**: Resolver 엔드포인트와 전달 규칙은 Direct Connect 및 VPN을 보완하는 DNS 구성 요소입니다. 연결 계층이 네트워크 수준에서 제공하는 하이브리드 경계를 넘어 이름 확인을 가능하게 합니다. 프라이빗 엔드포인트 상태 확인은 해당 경계를 넘는 DNS 장애 조치를 추가합니다. 동일한 경로를 통해 온프레미스 엔드포인트를 확인하므로, 하이브리드 경로 장애가 발생하면 상태 확인도 실패합니다.

**보안 주제와의 관계:**

* **[아웃바운드 제어](../security/outbound.md)**: DNS Firewall은 아웃바운드 제어 페이지에서 이그레스 방어의 첫 번째 계층으로 심층적으로 다룹니다. 이 페이지에서는 아키텍처 및 배포 관점에서 DNS Firewall을 다루고, 아웃바운드 제어 페이지에서는 보안 정책 관점에서 다룹니다.

**애플리케이션 네트워킹 주제와의 관계:**

* **[서비스 간 통신](../application-networking/service-to-service.md)**: 프라이빗 호스팅 영역과 Route 53 별칭 레코드는 해당 페이지에서 다루는 주요 서비스 디스커버리 메커니즘입니다. DNS 아키텍처 결정은 서비스가 서로를 찾는 방식에 직접적인 영향을 미칩니다.

**관측성 주제와의 관계:**

* **[AWS 서비스 모니터링](../observability/service-monitoring.md)**: 이 페이지의 DNS 지표 및 알람 가이던스가 기반으로 하는 기존 Route 53 Resolver 및 DNS Firewall CloudWatch 지표(`FirewallRuleGroupQueryVolume` 포함)와 대시보드를 다룹니다.
* **[내부 트래픽 모니터링](../observability/internal-traffic.md)**: DNS 쿼리 로깅과 DNS Firewall 지표를 VPC, Transit Gateway, Cloud WAN Flow Logs와 함께 DNS 계층 신호로 위치시킵니다.
