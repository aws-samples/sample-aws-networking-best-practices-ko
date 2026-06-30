# DNS 아키텍처 {#dns-architecture}

!!! info "사전 요구 사항"
    이 섹션은 [Amazon VPC](vpc.md), [AWS Organizations](organizations.md), [CIDR 계획](cidr.md)에 대한 기본 지식을 전제로 합니다. AWS 네트워킹 기반이 처음이라면 해당 페이지를 먼저 검토하세요.

Amazon Route 53 Resolver는 VPC 내에서 발생하는 모든 DNS 쿼리를 처리합니다. 프라이빗 호스팅 영역에 대한 쿼리 응답, 하이브리드 연결을 통한 온프레미스 도메인 쿼리 전달, 공용 인터넷 이름 확인 등을 별도의 DNS 인프라 배포 없이 모두 수행합니다. 멀티 계정 AWS 환경에서 DNS 설계 결정은 서비스 검색, 하이브리드 연결, 보안 태세 전반에 연쇄적인 영향을 미칩니다. 잘못 구성된 전달 규칙은 계정 전체의 이름 확인을 조용히 중단시키고, 공유되지 않은 프라이빗 호스팅 영역은 다른 VPC의 소비자에게 서비스를 보이지 않게 만들며, DNS Firewall이 없으면 모든 워크로드가 인터넷의 임의 도메인을 확인하고 나아가 접근까지 할 수 있게 됩니다.

AWS의 DNS는 함께 설계해야 하는 세 가지 계층에서 동작합니다. **확인(resolution)**(쿼리 응답 방식), **공유(sharing)**(DNS 구성이 모든 계정에 전달되는 방식), **보안(security)**(DNS를 아웃바운드 트래픽의 제어 지점으로 활용하는 방식)입니다. Route 53 Resolver는 확인 엔진이고, Route 53 Profiles는 대규모로 구성을 배포하며, Route 53 Resolver DNS Firewall은 DNS 계층에서 도메인 기반 필터링을 적용합니다.

## 주요 기능 {#key-capabilities}

<div class="grid cards" markdown>

*   :material-dns: **Route 53 Resolver**

    ---

    모든 VPC에 기본으로 탑재된 재귀 확인자입니다. 프라이빗 호스팅 영역에 대한 쿼리 응답, Resolver 엔드포인트를 통한 온프레미스 도메인 쿼리 전달, 공용 DNS 확인을 모두 자동으로 처리합니다.

*   :material-share-variant: **Route 53 Profiles**

    ---

    프라이빗 호스팅 영역 연결, Resolver 전달 규칙, DNS Firewall 규칙 그룹을 OU 수준에서 계정 전반에 배포합니다. 새 계정은 DNS 구성을 자동으로 상속합니다.

*   :material-lock: **프라이빗 호스팅 영역**

    ---

    연결된 VPC에서만 볼 수 있는 DNS 네임스페이스입니다. 내부 서비스 이름, 스플릿 호라이즌 DNS(내부와 외부 쿼리에 대해 다른 응답 제공), VPC Lattice 및 PrivateLink 엔드포인트의 사용자 지정 도메인 이름에 활용됩니다.

*   :material-arrow-right-bold: **Resolver 엔드포인트**

    ---

    인바운드 엔드포인트는 온프레미스 DNS 서버가 AWS 프라이빗 호스팅 영역을 확인할 수 있게 합니다. 아웃바운드 엔드포인트는 VPC 워크로드가 온프레미스 DNS 서버로 쿼리를 전달하여 온프레미스 도메인을 확인할 수 있게 합니다.

*   :material-shield-lock: **DNS Firewall**

    ---

    DNS 확인 계층에서의 도메인 기반 필터링입니다. 워크로드가 실제로 연결을 시도하기 전에 특정 도메인에 대한 쿼리를 차단, 허용, 또는 경고할 수 있습니다. 가장 저렴하고 광범위한 이그레스 제어 수단입니다.

*   :material-ip-network: **듀얼 스택 지원**

    ---

    Resolver 엔드포인트, 전달 규칙, DNS Firewall 모두 IPv4와 IPv6를 지원합니다. 프라이빗 호스팅 영역의 AAAA 레코드는 듀얼 스택 워크로드를 위해 A 레코드와 함께 동작합니다.

</div>

## 모범 사례 {#best-practices}

### 확인 아키텍처 {#resolution-architecture}

#### 모든 VPC의 유일한 DNS 확인자로 Route 53 Resolver 사용 {#use-route-53-resolver-as-the-sole-dns-resolver-for-all-vpcs}

모든 VPC에는 VPC+2 주소에 Route 53 Resolver가 자동으로 제공됩니다. VPC 워크로드의 기본 확인자로 사용자 지정 DNS 서버(BIND, Active Directory DNS, Kubernetes 외부의 CoreDNS)를 배포하지 마세요. 사용자 지정 확인자는 운영 부담(패치, 확장, 모니터링)을 가중시키고, Route 53 Resolver에는 없는 단일 장애 지점을 만들며, Route 53 기능(DNS Firewall, 쿼리 로깅, Resolver 규칙)을 우회하게 됩니다. 유일하게 정당화되는 예외는 도메인 가입 확인을 위해 AD DNS가 필요한 Active Directory 가입 Windows 워크로드이며, 이 경우에도 AD 외 쿼리는 Route 53 Resolver로 다시 전달해야 합니다.

#### 하이브리드 DNS 확인을 위한 전달 규칙 설계 {#design-forwarding-rules-for-hybrid-dns-resolution}

AWS의 워크로드가 온프레미스 도메인 이름(예: `corp.example.com`)을 확인해야 하는 경우, Resolver 아웃바운드 엔드포인트와 전달 규칙을 생성하여 Direct Connect 또는 VPN을 통해 해당 쿼리를 온프레미스 DNS 서버로 전송합니다. 반대로 온프레미스 워크로드가 AWS 프라이빗 호스팅 영역 이름을 확인해야 하는 경우, 온프레미스 DNS 서버가 전달할 Resolver 인바운드 엔드포인트를 생성합니다.

전달 규칙은 가능한 한 구체적으로 설계하세요. `.`(루트)가 아닌 `corp.example.com`을 온프레미스로 전달하세요. 와일드카드 전달 규칙은 모든 DNS 트래픽을 온프레미스로 보내므로 모든 쿼리에 지연 시간이 추가되고, 모든 DNS 확인이 하이브리드 연결에 의존하게 되며, 전달된 쿼리에 대해 DNS Firewall이 우회됩니다.

#### 여러 가용 영역에 걸쳐 Resolver 엔드포인트 배포 {#deploy-resolver-endpoints-across-multiple-availability-zones}

Resolver 인바운드 및 아웃바운드 엔드포인트는 지정한 서브넷에 ENI를 생성합니다. 각 엔드포인트에 대해 두 개 이상의 가용 영역에 걸쳐 최소 두 개의 ENI를 배포하세요. 단일 AZ 엔드포인트는 해당 엔드포인트에 의존하는 모든 DNS 확인의 단일 장애 지점이 됩니다. 하이브리드 환경에서는 해당 가용 영역에 문제가 발생하면 모든 경계 간 이름 확인이 실패합니다.

***핵심 인사이트:*** *DNS는 모든 네트워크에서 장애에 가장 민감한 의존성입니다. 30초간의 DNS 확인 실패는 아웃바운드 호출을 수행하는 모든 서비스에 걸쳐 연쇄적인 타임아웃을 유발합니다. 가장 중요한 워크로드와 동일한 가용성 기준으로 DNS 인프라를 설계하세요.*

### 멀티 계정 DNS 공유 {#multi-account-dns-sharing}

#### 멀티 계정 DNS 배포에 Route 53 Profiles 사용 {#use-route-53-profiles-for-multi-account-dns-distribution}

Route 53 Profiles를 사용하면 프라이빗 호스팅 영역 연결, Resolver 전달 규칙, DNS Firewall 규칙 그룹을 단일 프로파일로 묶어 OU 수준에서 AWS RAM을 통해 공유할 수 있습니다. OU에 추가된 새 계정은 별도의 자동화, 계정 간 Lambda 함수, 수동 연결 단계 없이 전체 DNS 구성을 자동으로 상속합니다.

Profiles 없이 계정 전반에 DNS 구성을 공유하려면 계정별 프라이빗 호스팅 영역 연결(호스팅 영역당 VPC당 API 호출 1회), 계정별 전달 규칙 공유, 계정별 DNS Firewall 연결이 필요합니다. 이러한 자동화는 취약하고 감사하기 어렵습니다. Profiles는 이를 정식 기능으로 대체합니다.

#### 네트워킹 계정에서 프라이빗 호스팅 영역 소유권 중앙화 {#centralize-private-hosted-zone-ownership-in-the-networking-account}

중앙화된 네트워킹 계정에서 프라이빗 호스팅 영역을 생성하고 관리하세요. Route 53 Profiles를 통해 소비 계정에 공유합니다. 이를 통해 네트워킹 팀이 권한 있는 DNS 네임스페이스를 제어하면서도, 적절한 경우 애플리케이션 팀이 위임된 하위 영역에 레코드를 생성할 수 있습니다.

대안인 각 계정이 자체 프라이빗 호스팅 영역을 생성하는 방식은 네임스페이스를 분산시키고, 영역이 겹칠 때 확인 충돌을 일으키며, DNS Firewall과 쿼리 로깅을 일관되게 구현하기 어렵게 만듭니다.

#### 내부 네임스페이스 계층 구조를 의도적으로 설계 {#design-your-internal-namespace-hierarchy-deliberately}

단일 내부 도메인(예: `internal.example.com`)을 선택하고 환경, 리전, 또는 서비스 도메인별로 하위 영역을 생성하세요. 잘 설계된 계층 구조는 DNS 레코드를 자체 문서화하고 경로 기반 확인 정책을 가능하게 합니다.

```
internal.example.com           (루트, 네트워킹 계정)
├── prod.internal.example.com  (프로덕션 서비스)
├── dev.internal.example.com   (개발 서비스)
└── hybrid.internal.example.com (온프레미스 전달)
```

수백 개의 레코드가 단일 영역에 쌓이는 플랫 네임스페이스는 피하세요. 길고 읽기 어려운 FQDN을 만드는 지나치게 깊은 계층 구조도 피하세요. 루트 아래 2~3단계가 적절합니다.

### DNS 보안 {#dns-security}

#### 모든 VPC에 DNS Firewall 배포 {#deploy-dns-firewall-in-every-vpc}

Route 53 Resolver DNS Firewall은 AWS에서 가장 저렴하고 광범위한 이그레스 제어 수단입니다. VPC에서 발생하는 모든 DNS 쿼리를 도메인 목록(AWS의 관리형 위협 인텔리전스 목록 또는 사용자 지정 목록)과 비교하여 차단, 허용, 또는 경고할 수 있습니다. 사실상 모든 아웃바운드 연결은 DNS 조회로 시작되므로, 악성 도메인의 확인을 차단하면 연결 시도 자체를 방지할 수 있습니다.

Route 53 Profiles를 통해 DNS Firewall 규칙 그룹을 배포하여 조직의 모든 VPC가 동일한 기본 보호를 받도록 하세요. DNS를 우회하는 트래픽(하드코딩된 IP, DNS-over-HTTPS)에 대해서는 Network Firewall 또는 서드파티 검사와 계층화하세요.

DNS Firewall 모범 사례 및 다른 이그레스 제어와의 통합에 대한 자세한 내용은 [아웃바운드 제어](../security/outbound.md)를 참조하세요.

#### 가시성 및 포렌식을 위한 Resolver 쿼리 로깅 활성화 {#enable-resolver-query-logging-for-visibility-and-forensics}

Resolver 쿼리 로깅은 연결된 VPC에서 발생하는 모든 DNS 쿼리(쿼리 이름, 유형, 응답 코드, 소스 IP, 타임스탬프)를 캡처합니다. 비용 효율적인 보존 및 Athena 쿼리를 위해 S3로 로그를 전달하거나, 의심스러운 확인 패턴(알려진 C2 도메인 쿼리, 높은 빈도의 NXDOMAIN 응답, 단일 소스의 비정상적인 쿼리 볼륨)에 대한 실시간 경고를 위해 CloudWatch Logs로 전달하세요.

쿼리 로깅은 VPC Flow Logs의 DNS 버전입니다. 워크로드가 이름으로 접근하려 한 대상의 완전한 기록을 제공합니다. 이 기능 없이는 DNS 관련 인시던트(DNS 터널링을 통한 데이터 유출, C2 콜백, 잘못 구성된 전달)를 조사할 때 추측에 의존해야 합니다.

### IPv6 고려 사항 {#ipv6-considerations}

#### 처음부터 듀얼 스택 Resolver 엔드포인트 구성 {#configure-dual-stack-resolver-endpoints-from-the-start}

Resolver 인바운드 및 아웃바운드 엔드포인트는 IPv6 ENI 주소를 지원합니다. VPC가 듀얼 스택인 경우, IPv6 전용 워크로드가 NAT64 없이 전달 및 확인할 수 있도록 Resolver 엔드포인트를 IPv4와 IPv6 주소 모두로 구성하세요. AWS 인바운드 엔드포인트로 전달하는 온프레미스 DNS 서버는 온프레미스 네트워크도 듀얼 스택인 경우 엔드포인트의 IPv6 주소에 대한 도달 가능성이 필요합니다.

#### 프라이빗 호스팅 영역에서 A 레코드와 함께 AAAA 레코드 포함 {#include-aaaa-records-alongside-a-records-in-private-hosted-zones}

듀얼 스택 인프라에서 실행되는 모든 내부 서비스에 대해 프라이빗 호스팅 영역에 A 레코드와 AAAA 레코드를 모두 게시하세요. IPv6를 선호하거나 IPv6 전용으로 실행되는 애플리케이션은 AAAA 레코드를 사용하고, IPv4 전용 소비자는 A 레코드를 사용합니다. 이는 듀얼 스택 VPC 설계와 동일한 원칙입니다. 나중에 개선하는 것보다 처음부터 IPv6를 포함하세요.

## Route 53 Resolver 기능 사용 시점 {#when-to-use-route-53-resolver-features}

Route 53 Resolver는 항상 사용 중입니다. 모든 VPC의 기본 확인자이기 때문입니다. 결정해야 할 것은 어떤 추가 기능을 활성화할지입니다.

**프라이빗 호스팅 영역**이 적합한 경우:

* 공용 인터넷에서 확인할 수 없어야 하는 서비스, 데이터베이스, 엔드포인트에 대한 내부 DNS 이름이 필요한 경우
* 스플릿 호라이즌 DNS가 필요한 경우(쿼리가 AWS 내부에서 오는지 외부에서 오는지에 따라 동일한 도메인에 대해 다른 응답 제공)

**Resolver 엔드포인트 및 전달 규칙**이 적합한 경우:

* 온프레미스 워크로드가 AWS 프라이빗 호스팅 영역 이름을 확인해야 하는 경우(인바운드 엔드포인트)
* AWS 워크로드가 온프레미스 도메인 이름을 확인해야 하는 경우(아웃바운드 엔드포인트 + 전달 규칙)
* AWS 경계를 넘는 DNS 의존성이 있는 하이브리드 환경에서 운영하는 경우

**Route 53 Profiles**가 적합한 경우:

* 소수 이상의 계정을 운영하며 모든 계정에 걸쳐 일관된 DNS 구성이 필요한 경우
* 사용자 지정 자동화 없이 새 계정이 DNS 구성을 자동으로 상속하기를 원하는 경우

**DNS Firewall**은 모든 VPC에 적합합니다. AWS 관리형 위협 도메인 목록을 최소한으로라도 배포하지 않아야 할 시나리오는 없습니다.

## 문서 {#documentation}

<div class="grid cards" markdown>

*   :material-file-document: **Route 53 Resolver 문서**

    ---

    Resolver 엔드포인트, 전달 규칙, 쿼리 로깅, DNSSEC 검증에 대한 전체 문서입니다.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html)

*   :material-file-document: **Route 53 Profiles 문서**

    ---

    멀티 계정 DNS 구성 배포를 위한 Profiles 생성, 공유, 관리 방법입니다.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profiles.html)

*   :material-file-document: **Route 53 Resolver DNS Firewall**

    ---

    도메인 기반 필터링 구성, 관리형 도메인 목록, Firewall Manager와의 통합입니다.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall.html)

*   :material-post: **Route 53 블로그 게시물**

    ---

    AWS Networking and Content Delivery 블로그의 아키텍처 패턴, 기능 발표, 구현 가이드입니다.

    [:octicons-arrow-right-24: 블로그 게시물](https://aws.amazon.com/blogs/networking-and-content-delivery/category/networking-content-delivery/amazon-route-53/)

</div>

## 관련 페이지 {#related-pages}

**다른 기반 주제와의 관계:**

* **[Amazon VPC](vpc.md)**: 모든 VPC에는 Route 53 Resolver가 자동으로 제공됩니다. VPC 설계(VPC 수, 계정 배치)에 따라 필요한 프라이빗 호스팅 영역 연결 및 Resolver 엔드포인트 수가 결정됩니다.
* **[AWS Organizations](organizations.md)**: Route 53 Profiles는 OU 수준에서 DNS 구성을 공유합니다. OU 구조에 따라 DNS 구성이 배포되는 방식이 결정됩니다.

**연결 주제와의 관계:**

* **[하이브리드 및 멀티 클라우드 연결](../connectivity/hybrid-multicloud.md)**: Resolver 엔드포인트와 전달 규칙은 Direct Connect 및 VPN의 DNS 보완 요소입니다. 연결 계층이 네트워크 수준에서 제공하는 하이브리드 경계를 넘는 이름 확인을 가능하게 합니다.

**보안 주제와의 관계:**

* **[아웃바운드 제어](../security/outbound.md)**: DNS Firewall은 아웃바운드 제어 페이지에서 이그레스 방어의 첫 번째 계층으로 심층적으로 다룹니다. 이 페이지는 아키텍처 및 배포 관점에서 DNS Firewall을 다루고, 아웃바운드 제어 페이지는 보안 정책 관점에서 다룹니다.

**애플리케이션 네트워킹 주제와의 관계:**

* **[서비스 간 통신](../application-networking/service-to-service.md)**: 프라이빗 호스팅 영역과 Route 53 별칭 레코드는 해당 페이지에서 다루는 기본 서비스 검색 메커니즘입니다. DNS 아키텍처 결정은 서비스가 서로를 찾는 방식에 직접적인 영향을 미칩니다.
