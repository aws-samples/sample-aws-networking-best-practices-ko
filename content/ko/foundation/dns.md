# DNS 아키텍처 {#dns-architecture}

!!! info "사전 요구 사항"
    이 섹션은 [Amazon VPC](vpc.md), [AWS Organizations](organizations.md), [CIDR 계획](cidr.md)에 대한 이해를 전제로 합니다. AWS 네트워킹 기초가 처음이라면 해당 페이지를 먼저 검토하세요.

Amazon Route 53 Resolver는 VPC 내부에서 발생하는 모든 DNS 쿼리를 처리합니다. 프라이빗 호스팅 영역에 대한 쿼리 응답, 하이브리드 연결을 통한 온프레미스 도메인 쿼리 전달, 공용 인터넷 이름 확인 등을 별도의 DNS 인프라 배포 없이 수행합니다. 멀티 계정 AWS 환경에서 DNS 설계 결정은 서비스 디스커버리, 하이브리드 연결, 보안 태세 전반에 연쇄적인 영향을 미칩니다. 잘못 구성된 전달 규칙은 계정 전체의 이름 확인을 조용히 중단시키고, 공유되지 않은 프라이빗 호스팅 영역은 다른 VPC의 소비자에게 서비스를 보이지 않게 만들며, DNS Firewall이 없으면 모든 워크로드가 인터넷상의 임의 도메인을 확인(따라서 접근)할 수 있게 됩니다.

AWS의 DNS는 함께 설계해야 하는 세 가지 계층에서 동작합니다. **확인(resolution)**(쿼리 응답 방식), **공유(sharing)**(DNS 구성을 모든 계정에 전달하는 방식), **보안(security)**(아웃바운드 트래픽의 제어 지점으로 DNS를 활용하는 방식)입니다. Route 53 Resolver는 확인 엔진 역할을 하고, Route 53 Profiles는 대규모로 구성을 배포하며, Route 53 Resolver DNS Firewall은 DNS 계층에서 도메인 기반 필터링을 적용합니다.

## 주요 기능 {#key-capabilities}

<div class="grid cards" markdown>

*   :material-dns: **Route 53 Resolver**

    ---

    모든 VPC에 기본으로 제공되는 재귀 리졸버입니다. 프라이빗 호스팅 영역에 대한 쿼리에 응답하고, Resolver 엔드포인트를 통해 온프레미스 도메인 쿼리를 전달하며, 퍼블릭 DNS를 자동으로 확인합니다.

*   :material-share-variant: **Route 53 Profiles**

    ---

    OU 수준에서 계정 전반에 걸쳐 프라이빗 호스팅 영역 연결, Resolver 전달 규칙, DNS Firewall 규칙 그룹을 배포합니다. 신규 계정은 DNS 구성을 자동으로 상속받습니다.

*   :material-lock: **프라이빗 호스팅 영역**

    ---

    연결된 VPC에서만 볼 수 있는 DNS 네임스페이스입니다. 내부 서비스 이름, 스플릿 호라이즌 DNS(내부 쿼리와 외부 쿼리에 대해 서로 다른 응답 제공), VPC Lattice 및 PrivateLink 엔드포인트의 사용자 지정 도메인 이름에 활용됩니다.

*   :material-arrow-right-bold: **Resolver 엔드포인트**

    ---

    인바운드 엔드포인트를 통해 온프레미스 DNS 서버가 AWS 프라이빗 호스팅 영역을 확인할 수 있습니다. 아웃바운드 엔드포인트를 통해 VPC 워크로드가 온프레미스 DNS 서버로 쿼리를 전달하여 온프레미스 도메인을 확인할 수 있습니다.

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

모든 VPC는 VPC+2 주소에 Route 53 Resolver를 자동으로 제공받습니다. VPC 워크로드의 기본 리졸버로 커스텀 DNS 서버(BIND, Active Directory DNS, Kubernetes 외부의 CoreDNS)를 배포하지 마십시오. 커스텀 리졸버는 운영 부담(패치, 확장, 모니터링)을 가중시키고, Route 53 Resolver에는 없는 단일 장애 지점을 만들며, Route 53 기능(DNS Firewall, 쿼리 로깅, Resolver 규칙)을 우회합니다. 유일하게 정당화되는 예외는 도메인 조인 해석을 위해 AD DNS가 필요한 Active Directory 조인 Windows 워크로드이며, 이 경우에도 AD 외 쿼리는 Route 53 Resolver로 다시 전달해야 합니다.

#### 하이브리드 DNS 해석을 위한 전달 규칙 설계 {#design-forwarding-rules-for-hybrid-dns-resolution}

AWS의 워크로드가 온프레미스 도메인 이름(예: `corp.example.com`)을 해석해야 하는 경우, Resolver 아웃바운드 엔드포인트와 전달 규칙을 생성하여 해당 쿼리를 Direct Connect 또는 VPN을 통해 온프레미스 DNS 서버로 전송합니다. 반대로, 온프레미스 워크로드가 AWS 프라이빗 호스팅 영역 이름을 해석해야 하는 경우, 온프레미스 DNS 서버가 전달할 Resolver 인바운드 엔드포인트를 생성합니다.

전달 규칙은 가능한 한 구체적으로 설계하십시오. `corp.example.com`을 온프레미스로 전달하되, `.`(루트)는 전달하지 마십시오. 와일드카드 전달 규칙은 모든 DNS 트래픽을 온프레미스로 전송하므로 모든 쿼리에 지연 시간이 추가되고, 모든 DNS 해석이 하이브리드 연결에 의존하게 되며, 전달된 쿼리에 대해 DNS Firewall이 우회됩니다.

#### 여러 가용 영역에 걸쳐 Resolver 엔드포인트 배포 {#deploy-resolver-endpoints-across-multiple-availability-zones}

Resolver 인바운드 및 아웃바운드 엔드포인트는 지정한 서브넷에 ENI를 생성합니다. 각 엔드포인트에 대해 두 개의 가용 영역에 걸쳐 최소 두 개의 ENI를 배포하십시오. 단일 AZ 엔드포인트는 해당 엔드포인트에 의존하는 모든 DNS 해석의 단일 장애 지점이 됩니다. 하이브리드 환경에서는 해당 가용 영역에 문제가 발생하면 모든 경계 간 이름 해석이 실패합니다.

***핵심 인사이트:*** *DNS는 모든 네트워크에서 장애에 가장 민감한 의존성입니다. 30초간의 DNS 해석 실패는 아웃바운드 호출을 수행하는 모든 서비스에 걸쳐 연쇄적인 타임아웃을 유발합니다. 가장 중요한 워크로드와 동일한 가용성 기준으로 DNS 인프라를 설계하십시오.*

### 멀티 계정 DNS 공유 {#multi-account-dns-sharing}

#### 멀티 계정 DNS 배포에 Route 53 Profiles 사용 {#use-route-53-profiles-for-multi-account-dns-distribution}

Route 53 Profiles를 사용하면 프라이빗 호스팅 영역 연결, Resolver 전달 규칙, DNS Firewall 규칙 그룹을 단일 프로파일로 묶어 OU 수준에서 AWS RAM을 통해 공유할 수 있습니다. OU에 추가된 새 계정은 커스텀 자동화, 계정 간 Lambda 함수, 수동 연결 단계 없이 전체 DNS 구성을 자동으로 상속합니다.

Profiles 없이 계정 간 DNS 구성을 공유하려면 계정별 프라이빗 호스팅 영역 연결(호스팅 영역당 VPC당 API 호출 1회), 계정별 전달 규칙 공유, 계정별 DNS Firewall 연결이 필요합니다. 이러한 자동화는 취약하고 감사하기 어렵습니다. Profiles는 이를 일급 작업으로 대체합니다.

#### 네트워킹 계정에서 프라이빗 호스팅 영역 소유권 중앙 집중화 {#centralize-private-hosted-zone-ownership-in-the-networking-account}

중앙 집중식 네트워킹 계정에서 프라이빗 호스팅 영역을 생성하고 관리하십시오. Route 53 Profiles를 통해 소비 계정에 공유합니다. 이를 통해 네트워킹 팀이 권한 있는 DNS 네임스페이스를 제어하면서, 애플리케이션 팀이 적절한 경우 위임된 하위 영역에서 레코드를 생성할 수 있습니다.

대안인 각 계정이 자체 프라이빗 호스팅 영역을 생성하는 방식은 네임스페이스를 분산시키고, 영역이 겹칠 때 해석 충돌을 일으키며, DNS Firewall과 쿼리 로깅을 일관되게 구현하기 어렵게 만듭니다.

#### 내부 네임스페이스 계층 구조를 의도적으로 설계 {#design-your-internal-namespace-hierarchy-deliberately}

단일 내부 도메인(예: `internal.example.com`)을 선택하고 환경, 리전 또는 서비스 도메인별로 하위 영역을 생성하십시오. 잘 설계된 계층 구조는 DNS 레코드를 자체 문서화하고 경로 기반 해석 정책을 가능하게 합니다:

```
internal.example.com           (root, networking account)
├── prod.internal.example.com  (production services)
├── dev.internal.example.com   (development services)
└── hybrid.internal.example.com (on-premises forwarding)
```

수백 개의 레코드가 단일 영역에 쌓이는 플랫 네임스페이스는 피하십시오. 길고 읽기 어려운 FQDN을 만드는 지나치게 깊은 계층 구조도 피하십시오. 루트 아래 2~3단계가 적절합니다.

### DNS 보안 {#dns-security}

#### 모든 VPC에 DNS Firewall 배포 {#deploy-dns-firewall-in-every-vpc}

Route 53 Resolver DNS Firewall은 AWS에서 가장 저렴하고 광범위한 이그레스 제어 수단입니다. VPC에서 수행되는 모든 DNS 쿼리를 도메인 목록(AWS의 관리형 위협 인텔리전스 목록 또는 사용자 지정 목록)과 비교하여 차단, 허용 또는 경고할 수 있습니다. 사실상 모든 아웃바운드 연결은 DNS 조회로 시작되므로, 악성 도메인의 해석을 차단하면 연결 시도 자체를 방지할 수 있습니다.

Route 53 Profiles를 통해 DNS Firewall 규칙 그룹을 배포하여 조직의 모든 VPC가 동일한 기본 보호를 받도록 하십시오. DNS를 우회하는 트래픽(하드코딩된 IP, DNS-over-HTTPS)에 대해서는 Network Firewall 또는 서드파티 검사와 계층화하십시오.

자세한 DNS Firewall 모범 사례 및 다른 이그레스 제어와의 통합에 대해서는 [아웃바운드 제어](../security/outbound.md)를 참조하십시오.

#### 가시성 및 포렌식을 위한 Resolver 쿼리 로깅 활성화 {#enable-resolver-query-logging-for-visibility-and-forensics}

Resolver 쿼리 로깅은 연결된 VPC에서 수행되는 모든 DNS 쿼리(쿼리 이름, 유형, 응답 코드, 소스 IP, 타임스탬프)를 캡처합니다. 비용 효율적인 보존 및 Athena 쿼리를 위해 S3로 로그를 전달하거나, 의심스러운 해석 패턴(알려진 C2 도메인 쿼리, 고빈도 NXDOMAIN 응답, 단일 소스의 비정상적인 쿼리 볼륨)에 대한 실시간 알림을 위해 CloudWatch Logs로 전달하십시오.

쿼리 로깅은 VPC Flow Logs의 DNS 버전으로, 워크로드가 이름으로 접근하려 한 대상의 완전한 기록을 제공합니다. 이 없이는 DNS 관련 인시던트(DNS 터널링을 통한 데이터 유출, C2 콜백, 잘못 구성된 전달)를 조사할 때 추측에 의존해야 합니다.

#### DNS 쿼리 로그와 DNS Firewall 활동을 지표 및 알람으로 전환 {#turn-dns-query-logs-and-dns-firewall-activity-into-metrics-and-alarms}

DNS 활동을 단순히 보존하는 것이 아니라 알림을 받으려면 Resolver 쿼리 로그를 CloudWatch Logs로 전달하십시오. 지표 필터, Contributor Insights, Logs Insights는 포렌식용으로 보관하는 S3 복사본이 아닌 로그 그룹에서 실행됩니다. DNS Firewall도 몇 분마다 VPC별 및 규칙 그룹별 쿼리 볼륨 지표를 CloudWatch에 게시하므로, 로그를 파싱하지 않고도 직접 알람을 설정할 수 있습니다.

고정된 수치가 아닌 설정한 기준선을 기반으로 알람을 설정하십시오. 쿼리 로그는 고유한 쿼리만 기록하므로 캐시에서 응답된 조회는 로깅되지 않아 수치가 낮게 나타납니다. 이를 예방이 아닌 탐지 수단으로 취급하십시오. 리졸버에 도달하는 것만 볼 수 있으므로 DNS-over-HTTPS 및 하드코딩된 IP 트래픽은 우회됩니다. 이러한 트래픽에는 Network Firewall 또는 다른 검사 수단을 유지하십시오.

### 중요 레코드 보호 {#protecting-critical-records}

#### 중요 레코드를 실수로 인한 변경으로부터 보호 {#protect-critical-records-from-accidental-change}

Route 53 레코드 세트 보호는 퍼블릭 및 프라이빗 호스팅 영역에서 보호된 이름과 유형의 레코드를 생성, 업데이트 또는 삭제하는 모든 `ChangeResourceRecordSets` 요청을 거부합니다. 이 보호는 전체 Route 53 권한을 가진 주체를 포함한 모든 주체에 적용되므로 직접 변경이 차단되고 의도적인 추가 단계가 강제됩니다. 이는 실수를 방지하며 보안 경계는 아닙니다. `route53:*`와 같이 광범위한 권한을 가진 주체는 보호를 삭제한 후 레코드를 변경할 수 있습니다(아래 권한 지침 참조). 실수로 변경될 경우 장애가 발생하고 거의 변경되지 않는 레코드(프로덕션 도메인의 apex 레코드, MX 레코드, 중요 엔드포인트로 트래픽을 라우팅하는 레코드 등)에 사용하십시오. 실수 비용이 큰 소수의 레코드만 보호하십시오. 각 보호는 일상적인 변경을 권한이 필요한 2단계 변경으로 전환하며, 호스팅 영역당 보호 수는 [할당량](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html#limits-api-entities-records)으로 제한되므로 광범위하게 보호하면 일상적인 변경이 느려지고 할당량이 소진될 수 있습니다.

의존하기 전에 동작 방식을 파악하십시오:

* **범위는 이름과 유형입니다.** 하나의 보호는 세트 식별자에 관계없이 해당 이름과 유형을 가진 모든 레코드를 포함합니다. 가중치 레코드 세트의 일부만 보호할 수 없습니다. 유형은 범위의 일부입니다. `A`에 대한 보호는 동일한 이름의 `AAAA`를 포함하지 않으므로, 듀얼 스택 이름은 각각에 대해 하나씩 보호가 필요합니다. `A`만 보호된 경우 누군가 `AAAA` 레코드를 변경하거나 삭제할 수 있으며, IPv6 클라이언트는 실패하고 IPv4 클라이언트는 계속 작동하는 발견하기 어려운 부분 장애가 발생합니다.
* **거부는 전체 배치에 적용됩니다.** 요청의 변경 사항 중 하나라도 보호된 이름과 유형을 건드리면 Route 53는 `InvalidChangeBatch`로 전체 요청을 거부하고 아무것도 적용하지 않습니다. 보호된 레코드를 건드리는 변경은 AWS CLI, AWS SDK, AWS CloudFormation에서 실패합니다. [Route 53 설명서](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/rrset-protection.html#rrset-protection-blocked-changes)와 [CloudFormation 참조](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-recordsetprotection.html#aws-resource-route53-recordsetprotection--remarks)는 오류를 다르게 명명(`InvalidChangeBatch`와 `ResourceConflict`)하므로, 런북이나 알람을 하나의 오류 이름에 연결하지 마십시오.
* **CloudFormation 업데이트는 순서가 있습니다.** CloudFormation은 레코드를 변경한 후 정리 단계에서만 제거된 보호를 삭제하므로, 보호된 레코드를 변경하고 보호를 제거하는 스택 업데이트는 실패합니다. 하나의 업데이트에서 보호를 추가하고 동일한 레코드를 변경하면 스택이 롤백 실패 상태가 될 수 있으며, 보호의 주석을 변경하면 교체되므로 교체 중에 레코드가 보호되지 않습니다. 뒤에 남겨진 보호(예: `DeletionPolicy: Retain`)는 레코드 삭제를 차단하고 해체를 실패시킵니다. 레코드 변경과 보호 변경을 별도의 스택 업데이트 또는 파이프라인 단계로 배포하고, 하나의 파이프라인이 남겨진 보호 제거를 담당하도록 하십시오. CloudFormation 참조에 절차가 설명되어 있습니다.
* **보호는 이름을 예약할 수 있습니다.** 아직 레코드가 없는 이름과 유형에 대해 보호를 생성할 수 있으며, 이는 누구도 해당 레코드를 생성하지 못하도록 합니다.
* **유용한 주석을 작성하십시오.** 선택적 주석(최대 256자)은 변경이 거부될 때 오류에 표시됩니다. 레코드가 보호된 이유와 연락처를 명시하십시오.

보호된 레코드 변경은 의도적입니다. 보호를 삭제하고, 변경을 수행한 후, 보호를 다시 생성하십시오. 보호는 편집할 수 없으므로 주석을 변경하려면 삭제 후 재생성해야 합니다. 이를 변경 프로세스와 런북에 계획하십시오. 보호가 재생성될 때까지 변경 권한이 있는 모든 주체가 레코드를 변경할 수 있으며, 변경 단계가 실패하고 보호가 재생성되지 않으면 레코드는 신호 없이 보호되지 않은 상태로 유지됩니다. 자동화가 삭제, 변경, 재생성을 실패 시 보호를 복원하는 하나의 단위로 처리하도록 하고, `DeleteResourceRecordSetProtections` 호출에 대한 알림을 설정하십시오. [AWS CloudTrail](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/logging-using-cloudtrail.html)은 보호 생성, 삭제, 목록 조회 요청을 로깅합니다.

보호의 강도는 제거할 수 있는 주체에 달려 있습니다. 호스팅 영역에 대해 `route53:DeleteResourceRecordSetProtections` 권한을 가진 모든 주체는 해당 영역의 모든 보호를 삭제할 수 있으며, 세 가지 레코드 세트 보호 작업(생성, 삭제, 목록 조회)은 호스팅 영역 리소스만 지원하고 서비스별 조건 키가 없습니다. 해당 권한을 소수의 관리자에게만 부여하고 다른 모든 사람에게는 거부하는 것을 고려하십시오. 네트워킹 계정이 호스팅 영역을 소유하는 AWS Organizations 환경에서는 호스팅 영역을 소유한 계정이 포함된 OU에 [서비스 제어 정책](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)(SCP) 거부를 적용하고 중앙 DNS 또는 네트워킹 관리자 역할을 면제하십시오. SCP는 관리 계정에 적용되지 않으며, 작업에 조건 키가 없으므로 동일한 영역에서 일부 보호 제거는 허용하고 다른 것은 거부할 수 없습니다. 보호의 강도는 가장 광범위한 삭제 권한 부여에 달려 있습니다.

레코드가 없는 이름에 대한 보호를 포함하여 보호가 있는 호스팅 영역은 삭제할 수 없습니다. 해체 자동화에 먼저 보호를 목록 조회하고 삭제하는 단계를 추가하십시오.

보호는 Route 53가 DNS 쿼리에 응답하는 방식을 변경하지 않습니다. 레코드 변경만 제어합니다.

***핵심 인사이트:*** *레코드 세트 보호는 실수를 방지하며, 의도적인 변경은 방지하지 않습니다. 보호의 강도는 보호를 삭제할 수 있는 주체에 대한 제어에 달려 있습니다.*

콘솔 및 CLI 단계는 [변경으로부터 레코드 보호](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/rrset-protection.html)를 참조하십시오. 보호 제거를 거부하는 예시 정책은 [예시 5: 레코드 세트 보호 제거 거부](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/access-control-managing-permissions.html#access-policy-example-deny-delete-rrset-protections)를 참조하십시오.

### IPv6 고려 사항 {#ipv6-considerations}

#### 처음부터 듀얼 스택 Resolver 엔드포인트 구성 {#configure-dual-stack-resolver-endpoints-from-the-start}

Resolver 인바운드 및 아웃바운드 엔드포인트는 IPv6 ENI 주소를 지원합니다. VPC가 듀얼 스택인 경우, IPv6 전용 워크로드가 NAT64 없이 전달 및 해석할 수 있도록 Resolver 엔드포인트를 IPv4 및 IPv6 주소 모두로 구성하십시오. AWS 인바운드 엔드포인트로 전달하는 온프레미스 DNS 서버는 온프레미스 네트워크도 듀얼 스택인 경우 엔드포인트의 IPv6 주소에 대한 연결이 필요합니다.

#### 프라이빗 호스팅 영역에서 A 레코드와 함께 AAAA 레코드 포함 {#include-aaaa-records-alongside-a-records-in-private-hosted-zones}

듀얼 스택 인프라에서 실행되는 모든 내부 서비스에 대해 프라이빗 호스팅 영역에 A 레코드와 AAAA 레코드를 모두 게시하십시오. IPv6를 선호하거나 IPv6 전용으로 실행되는 애플리케이션은 AAAA 레코드를 사용하고, IPv4 전용 소비자는 A 레코드를 사용합니다. 이는 듀얼 스택 VPC 설계와 동일한 원칙입니다. 나중에 개조하는 것보다 처음부터 IPv6를 포함하십시오.

## Route 53 Resolver 기능 사용 시기 {#when-to-use-route-53-resolver-features}

Route 53 Resolver는 항상 사용 중입니다. 모든 VPC의 기본 리졸버로 동작하며, 어떤 추가 기능을 활성화할지 결정하는 것이 핵심입니다.

**프라이빗 호스팅 영역**은 다음 경우에 적합합니다.

* 공개 인터넷에서 확인할 수 없어야 하는 서비스, 데이터베이스 또는 엔드포인트에 내부 DNS 이름이 필요한 경우
* 스플릿 호라이즌 DNS(쿼리가 AWS 내부에서 오는지 외부에서 오는지에 따라 동일한 도메인에 대해 다른 응답을 반환)가 필요한 경우

**Resolver 엔드포인트 및 전달 규칙**은 다음 경우에 적합합니다.

* 온프레미스 워크로드가 AWS 프라이빗 호스팅 영역 이름을 확인해야 하는 경우(인바운드 엔드포인트)
* AWS 워크로드가 온프레미스 도메인 이름을 확인해야 하는 경우(아웃바운드 엔드포인트 + 전달 규칙)
* AWS 경계를 넘는 DNS 의존성이 있는 하이브리드 환경에서 운영하는 경우

**Route 53 Profiles**는 다음 경우에 적합합니다.

* 여러 계정을 운영하며 모든 계정에 걸쳐 일관된 DNS 구성이 필요한 경우
* 새 계정이 별도의 자동화 없이 DNS 구성을 자동으로 상속받기를 원하는 경우

**DNS Firewall**은 모든 VPC에 적합합니다. AWS 관리형 위협 도메인 목록을 최소한으로라도 배포하지 않아도 되는 시나리오는 존재하지 않습니다.

## 문서 {#documentation}

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

*   :material-file-document: **레코드 변경 방지**

    ---

    레코드 세트 보호 작동 방식, 보호할 레코드, 거부된 변경 및 영역 삭제 동작, 제거를 제어하는 권한에 대한 설명입니다.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/rrset-protection.html)

*   :material-file-document: **AWS::Route53::RecordSetProtection**

    ---

    업데이트 순서, 롤백 동작, 기존 보호 가져오기를 포함한 보호 관리를 위한 CloudFormation 리소스입니다.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-recordsetprotection.html)

*   :material-post: **Route 53 블로그 게시물**

    ---

    AWS Networking and Content Delivery 블로그의 아키텍처 패턴, 기능 발표 및 구현 가이드입니다.

    [:octicons-arrow-right-24: 블로그 게시물](https://aws.amazon.com/blogs/networking-and-content-delivery/category/networking-content-delivery/amazon-route-53/)

</div>

## 관련 페이지 {#related-pages}

**다른 기반 주제와의 관계:**

* **[Amazon VPC](vpc.md)**: 모든 VPC에는 Route 53 Resolver가 자동으로 포함됩니다. VPC 설계(VPC 수, 계정 배치)에 따라 필요한 프라이빗 호스팅 영역 연결 수와 Resolver 엔드포인트 수가 결정됩니다.
* **[AWS Organizations](organizations.md)**: Route 53 Profiles는 OU 수준에서 DNS 구성을 공유하며, OU의 SCP는 레코드 세트 보호를 제거할 수 있는 주체를 제한합니다. OU 구조에 따라 DNS 구성이 배포되는 방식과 해당 제어가 적용되는 위치가 결정됩니다.

**연결 주제와의 관계:**

* **[하이브리드 및 멀티 클라우드 연결](../connectivity/hybrid-multicloud.md)**: Resolver 엔드포인트와 전달 규칙은 Direct Connect 및 VPN의 DNS 보완 요소입니다. 연결 계층이 네트워크 수준에서 제공하는 하이브리드 경계를 넘어 이름 확인을 가능하게 합니다.

**보안 주제와의 관계:**

* **[아웃바운드 제어](../security/outbound.md)**: DNS Firewall은 아웃바운드 제어 페이지에서 이그레스 방어의 첫 번째 계층으로 심층적으로 다룹니다. 이 페이지에서는 DNS Firewall을 아키텍처 및 배포 관점에서 다루고, 아웃바운드 제어 페이지에서는 보안 정책 관점에서 다룹니다.

**애플리케이션 네트워킹 주제와의 관계:**

* **[서비스 간 통신](../application-networking/service-to-service.md)**: 프라이빗 호스팅 영역과 Route 53 별칭 레코드는 해당 페이지에서 다루는 주요 서비스 디스커버리 메커니즘입니다. DNS 아키텍처 결정은 서비스가 서로를 찾는 방식에 직접적인 영향을 미칩니다.

**관측성 주제와의 관계:**

* **[AWS 서비스 모니터링](../observability/service-monitoring.md)**: 이 페이지의 DNS 지표 및 알람 가이던스가 기반으로 하는 기존 Route 53 Resolver 및 DNS Firewall CloudWatch 지표(`FirewallRuleGroupQueryVolume` 포함)와 대시보드를 다룹니다.
* **[내부 트래픽 모니터링](../observability/internal-traffic.md)**: DNS 쿼리 로깅과 DNS Firewall 지표를 VPC, Transit Gateway, Cloud WAN Flow Logs와 함께 DNS 계층 신호로 위치시킵니다.
