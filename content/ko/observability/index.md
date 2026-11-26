# 관측성 {#observability}

이 섹션에서는 AWS 네트워크에 대한 가시성을 확보하는 방법을 다룹니다. 어떤 트래픽이 흐르고 있는지, 해당 트래픽을 처리하는 서비스가 정상 상태인지, 엔드포인트 간 네트워크 경로의 성능은 어떠한지, 성능 저하의 원인이 어디에 있는지, 그리고 문제가 발생했을 때 어떻게 알림을 받을 수 있는지를 설명합니다. 네트워크 관측성은 단일 대시보드가 아닙니다. 각 데이터 소스가 서로 다른 질문에 답하고, 이를 조합하여 전체 상황을 파악하는 계층적 접근 방식입니다.

관측성은 연결, 애플리케이션 네트워킹, 보안 계층 위에서 동작합니다. 이러한 계층에서 생성되는 로그, 지표, 이벤트를 수집하여 실행 가능한 인사이트로 전환합니다. 관측성이 없으면 아무것도 보이지 않는 상태로 운영하는 것과 같습니다. 연결 장애를 트러블슈팅할 수 없고, 보안 인시던트를 탐지할 수 없으며, 비용을 귀속시킬 수 없고, 아키텍처가 설계대로 동작하는지 검증할 수도 없습니다.

## 1. 내부 트래픽 모니터링 {#1-internal-traffic-monitoring}

**내부 트래픽 모니터링**은 AWS 환경 내 리소스 간 트래픽 흐름에 대한 가시성을 제공합니다. VPC 간, 서브넷 간, ENI 간 트래픽이 이에 해당합니다. 이는 네트워크 보안 분석, 비용 귀속, 연결 트러블슈팅의 기반이 됩니다.

**주요 데이터 소스:**

*   **VPC Flow Logs** — VPC, 서브넷, ENI 수준에서 40개 이상의 커스텀 형식 필드를 포함한 패킷 수준 메타데이터
*   **Transit Gateway Flow Logs** — 단일 구성으로 VPC 간 및 계정 간 트래픽을 중앙 집중식으로 파악
*   **AWS Cloud WAN Flow Logs** — 코어 네트워크 소유자 계정에서 세그먼트, 검사, 드롭 이유 상세 정보를 포함한 코어 네트워크 트래픽
*   **VPC Lattice Access Logs** — ID, 지연 시간, 인증 결정 정보를 포함한 서비스 간 요청별 상세 정보
*   **Network Firewall Logs** — 규칙 귀속 정보와 함께 스테이트풀 검사 결정(허용, 거부, 경고)
*   **Amazon Athena** — 대규모 분석을 위해 S3에 저장된 Flow Logs를 SQL로 쿼리

***핵심 인사이트:*** *VPC Flow Logs는 프로덕션 환경에서 선택 사항이 아닙니다. 애플리케이션 로깅에 해당하는 네트워크 수준의 기록입니다. 이 로그 없이는 보안 인시던트를 조사하거나, 연결 문제를 트러블슈팅하거나, 실제 트래픽 패턴을 파악할 수 없습니다.*

## 2. 외부 트래픽 모니터링 {#2-external-traffic-monitoring}

**외부 트래픽 모니터링**은 AWS 환경과 공용 인터넷 간의 경계를 넘나드는 트래픽에 대한 가시성을 제공합니다. 클라이언트로부터의 인그레스 트래픽과 외부 서비스로의 이그레스 트래픽이 모두 포함됩니다. 각 계층은 다른 계층에서 볼 수 없는 정보를 캡처합니다.

**주요 데이터 소스:**

*   **CloudFront 액세스 로그 / 실시간 로그** — 엣지 수준의 클라이언트 경험(지연 시간, 캐시 상태, 프로토콜, 지리적 분포)
*   **ALB / NLB 액세스 로그** — 요청별 또는 연결별 상세 정보(대상 지연 시간, 응답 코드, TLS 메타데이터)
*   **AWS WAF 로그** — 보안 평가 결과(규칙 매칭, 허용/차단 결정, 요청 속성)
*   **NAT 게이트웨이 CloudWatch 지표** — 이그레스 볼륨, 연결 수, 포트 고갈, 패킷 드롭
*   **Route 53 쿼리 로그** — 퍼블릭 호스팅 영역의 DNS 쿼리 패턴

***핵심 인사이트:*** *ALB 액세스 로그는 생성 비용이 무료이고 저장 비용도 매우 저렴하며, 인시던트 조사 시 대체 불가능한 자료입니다. 프로덕션 ALB에서 이 로그를 비활성화할 타당한 이유는 없습니다.*

## 3. AWS 서비스 모니터링 {#3-aws-services-monitoring}

**AWS 서비스 모니터링**은 네트워킹 서비스 자체의 운영 상태에 초점을 맞춥니다. 서비스를 통해 흐르는 트래픽이 아니라, 해당 트래픽을 전달하는 인프라가 정상 상태인지를 확인합니다. 블랙홀 드롭이 발생하는 Transit Gateway, 포트 할당이 고갈되는 NAT 게이트웨이, 또는 연결이 불안정한 Direct Connect는 트래픽 모니터링만으로는 감지할 수 없는 서비스 수준의 장애입니다.

**주요 패턴:**

*   **서비스별 핵심 지표** — Transit Gateway, NAT 게이트웨이, Direct Connect, VPN, ALB, NLB, Network Firewall, VPC Lattice의 실제 운영 문제를 나타내는 특정 CloudWatch 지표
*   **복합 알람** — 여러 신호를 결합하여 실제 문제를 확인한 후 알림 발송(알람 피로 감소)
*   **이상 탐지** — 수동 임계값 조정 없이 트래픽 패턴에 적응하는 ML 기반 알림
*   **할당량 모니터링** — 서비스 한도에 도달하기 전에 80% 사용률에서 알람 설정
*   **중앙 집중식 대시보드** — 네트워킹 팀을 위한 계정 간, 리전 간 가시성

***핵심 인사이트:*** *CloudWatch 지표는 서비스가 정상임을 알려줍니다. 합성 상태 확인은 경로가 엔드투엔드로 정상 동작하는지 알려줍니다. 둘 다 필요합니다. 서비스가 정상이더라도 라우팅이 잘못되면 장애가 발생합니다.*

## 4. 네트워크 성능 모니터링 {#4-network-performance-monitoring}

**네트워크 성능 모니터링**은 네트워크 경로의 성능을 측정하고, 성능 저하가 AWS 네트워크에서 비롯된 것인지 자체 세그먼트에서 비롯된 것인지를 파악합니다. Flow Logs는 네트워크를 통과한 트래픽을 보여주고, 서비스 지표는 서비스의 정상 여부를 보여주지만, 어느 것도 경로의 AWS 제어 구간에 장애가 있는지는 보여주지 않습니다. Amazon CloudWatch Network Monitoring은 이를 위해 각기 다른 관점을 제공하는 3가지 제품을 제공합니다.

**주요 제품:**

*   **Network Synthetic Monitor** — 에이전트 없이 관리형 프로브를 사용합니다. AWS Direct Connect 경로 및 AWS Transit Gateway 피어링을 포함한 리전 간 경로에 대한 왕복 시간, 패킷 손실, 네트워크 상태 지표(NHI)를 제공합니다.
*   **Network Flow Monitor** — Amazon EC2 인스턴스 및 Amazon EKS 노드의 에이전트가 실제 워크로드 흐름에 대한 TCP 성능을 보고하며, 모니터당 NHI를 제공합니다.
*   **Internet Monitor** — 인터넷 연결 애플리케이션에 대한 도시 네트워크 및 ASN 상태 이벤트를 AWS 또는 ISP 귀속 정보와 함께 제공합니다.
*   **네트워크 상태 지표** — 이진 귀속 신호입니다. NHI 100은 AWS 측 성능 저하가 관찰되었음을 의미합니다. NHI 0은 전체 경로가 정상임을 의미하지 않습니다.

***핵심 인사이트:*** *NHI와 패킷 손실 및 왕복 시간을 함께 활용하세요. NHI는 AWS가 관련되어 있는지를 알려주고, 성능 지표는 실제로 영향을 받는 대상이 있는지를 알려줍니다.*

## 5. 알림 {#5-notifications}

**알림**은 문제를 감지하는 것과 적절한 담당자가 조치를 취하는 것 사이의 간극을 연결합니다. 모니터링에서 가장 흔한 운영 실패는 알람 피로입니다. 너무 많은 오탐이나 낮은 우선순위의 노이즈로 인해 팀이 알람을 무시하게 되는 현상입니다.

**주요 서비스:**

*   **CloudWatch Alarms** — 임계값, 이상 탐지, 복합 알람을 활용한 지표 기반 알림
*   **Amazon EventBridge** — 상태 변경에 대한 이벤트 기반 알림(VPN 터널 다운, Direct Connect 불안정, BGP 세션 손실)
*   **Amazon SNS** — 이메일, PagerDuty, Lambda, SQS로의 팬아웃 전달
*   **AWS Health Dashboard** — 내 리소스에 영향을 미치는 AWS 서비스 이벤트에 대한 사전 인지
*   **AWS Chatbot** — 인터랙티브 액션과 함께 Slack 및 Microsoft Teams로 알람 전달

***핵심 인사이트:*** *팀이 알람을 습관적으로 무시한다면, 모니터링 문제가 아니라 알람 설계 문제입니다. 모든 알람에는 명확한 담당자와 정의된 대응 조치가 있어야 합니다.*

---

## 관측성 주제 살펴보기 {#explore-observability-topics}

<div class="grid cards" markdown>

*   :material-lan: **내부 트래픽 모니터링**

    ---

    VPC Flow Logs, Transit Gateway 및 Cloud WAN Flow Logs, VPC Lattice 액세스 로그, Athena 통합, 비용 효율적인 로그 분석.

    [:octicons-arrow-right-24: 내부 트래픽 모니터링](internal-traffic.md)

*   :material-web-check: **외부 트래픽 모니터링**

    ---

    CloudFront 로그, ALB/NLB 액세스 로그, AWS WAF 로그, NAT 게이트웨이 지표, 클라이언트 경험 모니터링.

    [:octicons-arrow-right-24: 외부 트래픽 모니터링](external-traffic.md)

*   :material-monitor-dashboard: **AWS 서비스 모니터링**

    ---

    서비스별 핵심 지표, 복합 알람, 이상 탐지, 중앙 집중식 대시보드, 자동화된 복구.

    [:octicons-arrow-right-24: AWS 서비스 모니터링](service-monitoring.md)

*   :material-speedometer: **네트워크 성능 모니터링**

    ---

    Network Synthetic Monitor, Network Flow Monitor, Internet Monitor, 그리고 경로 성능 저하를 AWS 네트워크에 귀속시키기 위한 네트워크 상태 지표.

    [:octicons-arrow-right-24: 네트워크 성능 모니터링](network-performance.md)

*   :material-bell-alert: **알림**

    ---

    알람 설계, 심각도 계층, 복합 알람, EventBridge 상태 변경 라우팅, 계정 간 이벤트 전달.

    [:octicons-arrow-right-24: 알림](notifications.md)

</div>
