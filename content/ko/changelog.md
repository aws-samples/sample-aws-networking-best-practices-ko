# 변경 이력 {#changelog}

결정에 영향을 미치는 콘텐츠 변경 사항은 여기에 기록되며, 최신 항목이 먼저 표시되고 풀 리퀘스트가 병합된 월별로 그룹화됩니다. 첫 번째 항목은 2026년 7월부터 시작합니다. 오타 수정, 깨진 링크 수정, 서식, CI, 사이트 메타데이터 변경 사항은 목록에 포함되지 않습니다. 해당 내용은 [커밋 기록](https://github.com/aws/aws-networking-best-practices/commits/main)에서 확인할 수 있습니다. 이 페이지를 통해 마지막으로 읽은 이후 권장 사항이 변경되었는지, 또는 이전 학습 데이터를 기반으로 답변하는 AI 모델이 현재 지침을 반영하는지 확인하세요.

**포함 기준:** 이전 버전의 페이지를 적용한 독자가 이제 다른 결정을 내릴 수 있는 경우 해당 항목을 여기에 기록합니다.

| 아이콘 | 유형 | 사용 시점 |
| --- | --- | --- |
| 🆕 | 새로운 지침 | 새로운 모범 사례, 섹션 또는 서비스 기능이 문서화된 경우 |
| 🔄 | 변경된 권장 사항 | 이전과 다른 조언 또는 기본 선택이 제시된 경우 |
| 🔧 | 수정 | 독자의 행동에 영향을 미치는 방식으로 사실적, 기술적 또는 다이어그램 오류가 수정된 경우 |
| 🗑️ | 제거됨 | 지침, 권장 사항 또는 섹션이 폐기된 경우 |

## 2026년 10월 {#october-2026}

* 🆕 **새로운 지침** — [경계 제어](security/perimeter-inbound.md#choose-between-centralized-and-per-vpc-inspection-deliberately): AWS Cloud WAN 서비스 삽입은 중앙 집중식 검사 VPC로 트래픽을 라우팅하는 두 번째 방법으로, AWS Transit Gateway를 통해 공유 검사 VPC로 라우팅하는 방법과 함께 사용할 수 있습니다. AWS Firewall Manager는 중앙 집중식 검사에서 선택 사항입니다. Firewall Manager를 통한 VPC별 검사는 VPC가 많은 환경의 기본값으로 유지됩니다. ([#166](https://github.com/aws/aws-networking-best-practices/pull/166))
* 🔧 **수정** — [경계 제어](security/perimeter-inbound.md#use-stateless-rules-for-high-volume-simple-filtering-and-stateful-rules-for-protocol-aware-inspection): 이전에는 스테이트리스 및 스테이트풀 규칙 분리가 비용 조절 수단으로 제시되었습니다. 이제 페이지에서는 AWS Network Firewall이 어떤 규칙 엔진이 트래픽을 평가하든 관계없이 엔드포인트 시간 및 처리된 기가바이트에 대해 요금을 부과하므로, 규칙 분리는 처리 비용을 줄이는 방법이 아닌 규칙 설계 선택임을 명시합니다. ([#166](https://github.com/aws/aws-networking-best-practices/pull/166))
* 🆕 **새로운 지침** — [로드 밸런싱](application-networking/load-balancing.md#manage-flow-lifetime-and-failure-recovery): Gateway Load Balancer는 대상이 비정상 상태가 되거나, 등록 해제되거나, 플로우가 유휴 상태로 만료될 때 TCP 리셋을 전송할 수 있으므로, 발신자는 TCP 재시도가 만료될 때까지 기다리는 대신 새 플로우를 열 수 있습니다. 세 가지 설정 모두 기존 로드 밸런서를 포함하여 기본적으로 비활성화되어 있으며, 5-튜플 플로우 고정성이 필요합니다. TCP 유휴 타임아웃을 350초 이상으로 높이는 경우, 대상의 연결 추적 유휴 타임아웃을 Gateway Load Balancer 값 이상으로 유지하세요. ([#167](https://github.com/aws/aws-networking-best-practices/pull/167))
* 🆕 **새로운 지침** — [DNS 아키텍처](foundation/dns.md#turn-dns-query-logs-and-dns-firewall-activity-into-metrics-and-alarms): Amazon Route 53 Resolver 쿼리 로그를 Amazon CloudWatch Logs로 전달하여 지표 필터와 알람을 구성하고, DNS Firewall 쿼리 볼륨 지표에 직접 알람을 설정하세요. 쿼리 로그는 캐시된 조회, DNS-over-HTTPS, 하드코딩된 IP 트래픽을 누락하므로, 이를 예방이 아닌 탐지 수단으로 활용하세요. ([#175](https://github.com/aws/aws-networking-best-practices/pull/175))
* 🆕 **새로운 지침** — [아웃바운드 제어](security/outbound.md#scope-egress-rules-to-container-workloads): Network Firewall 컨테이너 연결은 Amazon ECS 태스크와 Amazon EKS 파드를 동적 소스 IP 집합으로 추적하므로, 동일한 VPC를 공유하는 워크로드에 서로 다른 이그레스 규칙을 적용할 수 있습니다. Amazon EKS VPC CNI에서 소스 NAT가 활성화된 상태로 남아 있는 등 충족되지 않은 제약 조건이 있으면 규칙이 자동으로 일치하지 않을 수 있습니다. ([#176](https://github.com/aws/aws-networking-best-practices/pull/176))
* 🆕 **새로운 지침** — [AWS 내 연결](connectivity/within-aws.md#account-for-the-tunnel-endpoint-when-planning-a-cidr-range-configuration): Amazon VPC Lattice VPC 리소스는 GENEVE 캡슐화를 사용하는 터널 엔드포인트를 통해 도달하는 CIDR 범위를 나타낼 수 있으며, 이는 호스트가 사전에 알려지지 않은 세그먼트에 적합합니다. CIDR 범위 구성은 NAT를 수행하지 않고, 서비스 네트워크에 참여할 수 없으며, 사용자 지정 도메인 이름이 없으므로, 겹치는 CIDR의 이점은 단일, 그룹 및 ARN 구성에만 적용됩니다. ([#174](https://github.com/aws/aws-networking-best-practices/pull/174))
* 🔄 **변경된 권장 사항** — [원격 액세스](connectivity/remote-access.md#aws-client-vpn): 이전에는 SSH 및 RDP 액세스가 AWS Client VPN을 선택하는 이유로 나열되었으며, AWS Verified Access는 VPN 클라이언트가 필요 없는 것으로 설명되었습니다. 이제 특정 애플리케이션에 대한 TCP, SSH, RDP 액세스는 Verified Access에 적합하며(비 HTTP(S) 엔드포인트에는 Connectivity Client가 필요), Client VPN은 다수의 호스트 및 포트에 대한 임시 액세스, 비 TCP 프로토콜, IP 기반 레거시 애플리케이션에 적합합니다. ([#173](https://github.com/aws/aws-networking-best-practices/pull/173))
* 🆕 **새로운 지침** — [원격 액세스](connectivity/remote-access.md#combine-identity-with-device-posture): Client VPN은 사용자 ID 외에 디바이스 포스처를 요구할 수 있으며, 연결 시점에 확인되고 세션 유지 기간 동안 재평가됩니다. 포스처 게이팅 엔드포인트는 AWS 제공 클라이언트만 허용하므로, 적용하기 전에 디바이스 신뢰 공급자 적용 범위를 확인하고 섀도우 모드에서 정책을 실행하세요. ([#173](https://github.com/aws/aws-networking-best-practices/pull/173))

## 2026년 8월 {#august-2026}

* 🆕 **새로운 지침** — [로드 밸런싱](application-networking/load-balancing.md#plan-ipv6-as-a-first-class-option_1): 새로운 배포에는 기본적으로 듀얼 스택 Network Load Balancer를 사용하고, 각 주소 패밀리를 자체 대상 그룹으로 전송하는 리스너 규칙을 구성하여 클라이언트 IP가 엔드투엔드로 보존되도록 하세요. 대상 보안 그룹은 두 주소 패밀리 모두에서 상태 확인을 허용해야 하며, UDP 리스너는 패밀리별로 트래픽을 분리하기 전에 IPv6 대상 그룹이 필요합니다. ([#161](https://github.com/aws/aws-networking-best-practices/pull/161))
* 🔧 **수정** — [하이브리드 및 멀티 클라우드 연결](connectivity/hybrid-multicloud.md#use-bgp-attributes-for-traffic-engineering-across-multiple-direct-connect-paths): 이전에는 모든 가상 인터페이스에 대해 하나의 BGP 속성 목록이 제공되었으며, Local Preference 커뮤니티는 AWS에서 오는 경로에 적용되는 것으로 설명되었습니다. 이제 속성은 AWS에 광고하는 경로에 설정되고, Local Preference와 MED는 프라이빗 및 트랜짓 가상 인터페이스에 적용되며, 범위 커뮤니티는 AWS가 퍼블릭 가상 인터페이스의 프리픽스를 전파하는 범위를 제어합니다. ([#160](https://github.com/aws/aws-networking-best-practices/pull/160))
* 🆕 **새로운 지침** — [하이브리드 및 멀티 클라우드 연결](connectivity/hybrid-multicloud.md#monitor-bgp-and-vif-metrics-and-verify-the-routes-themselves): AWS Direct Connect BGP 경로 가시성은 AS 경로 및 커뮤니티 값과 함께 각 가상 인터페이스에서 수락 및 광고된 경로를 나열합니다. BGP 세션 및 프리픽스 수 지표에 알람을 설정한 후, 경로 목록을 읽어 변경된 프리픽스를 확인하세요. ([#160](https://github.com/aws/aws-networking-best-practices/pull/160))
* 🆕 **새로운 지침** — [AWS 내 연결](connectivity/within-aws.md#order-policy-rules-from-specific-to-broad-and-always-end-with-a-catch-all): Transit Gateway 정책 기반 라우팅은 소스 및 대상 CIDR, 포트, 프로토콜을 기준으로 플로우별 라우팅 테이블을 선택하며, 추가 요금이 없습니다. 어떤 규칙과도 일치하지 않는 트래픽은 삭제되므로, 모든 정책 테이블의 마지막에는 반드시 캐치올 규칙을 추가하세요. IPv4 전용 규칙은 IPv6 트래픽과 일치하지 않으며, 해당 트래픽은 캐치올 규칙으로 넘어갑니다. ([#158](https://github.com/aws/aws-networking-best-practices/pull/158))

## 2026년 7월 {#july-2026}

* 🔧 **수정** — [경계 제어](security/perimeter-inbound.md): 이전에는 경계 제어 계층 다이어그램에서 네트워크 ACL이 VPC 경계의 Network Firewall과 함께 그룹화되고 보안 그룹이 서브넷 계층에 표시되었습니다. 이제 네트워크 ACL은 서브넷 경계에, 보안 그룹은 리소스 네트워크 인터페이스에 위치하며, AWS Global Accelerator는 경계 제어가 아닌 라우팅 도구이므로 제거되었습니다. ([#157](https://github.com/aws/aws-networking-best-practices/pull/157))
* 🔄 **변경된 권장 사항** — [하이브리드 및 멀티 클라우드 연결](connectivity/hybrid-multicloud.md#no-supported-pair-for-the-regions-you-need): 이전에는 아직 지원되지 않는 AWS Interconnect 리전 페어에 대해 파트너 기반 AWS Direct Connect 또는 VPN을 사용하도록 안내했습니다. 이제 지원되는 페어에 연결한 후 나머지 구간은 각 클라우드 내부에서 처리하고, Interconnect가 지원하지 않는 클라우드이거나 기존 코로케이션 인프라가 더 저렴한 경우에만 파트너 기반 옵션을 유지하세요. ([#155](https://github.com/aws/aws-networking-best-practices/pull/155))
* 🆕 **새로운 지침** — [하이브리드 및 멀티 클라우드 연결](connectivity/hybrid-multicloud.md#treat-a-single-interconnect-as-the-resilient-unit): 단일 Interconnect는 내부에 이중화가 포함되어 있으므로 월 99.99% 가동 시간 SLA를 제공합니다. 동일한 리전 페어에 두 번째 Interconnect를 추가하면 비용이 두 배가 되지만 해당 약정은 높아지지 않으며, SLA 자격을 얻으려면 엔드포인트가 둘 이상의 가용 영역에 걸쳐 있어야 합니다. ([#155](https://github.com/aws/aws-networking-best-practices/pull/155))
* 🔧 **수정** — [하이브리드 및 멀티 클라우드 연결](connectivity/hybrid-multicloud.md#watch-the-pricing-tier-as-the-interconnects-reach-grows): 이전에는 Interconnect 요금이 대역폭 계층별 시간당 요금과 데이터 전송 요금으로 설명되었습니다. 이제 프로비저닝된 대역폭과 GB당 요금 없이 거리 기반 요금 계층으로 설정된 시간당 요금이며, 원거리 Cloud WAN Core Network Edge를 추가하면 계층이 높아질 수 있습니다. ([#155](https://github.com/aws/aws-networking-best-practices/pull/155))
