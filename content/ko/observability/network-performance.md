# 네트워크 성능 모니터링 {#network-performance-monitoring}

!!! info "사전 요구 사항"
    이 섹션은 [AWS 서비스 모니터링](service-monitoring.md), [AWS 내 연결](../connectivity/within-aws.md), [하이브리드 및 멀티 클라우드](../connectivity/hybrid-multicloud.md)에 대한 이해를 전제로 합니다. AWS 네트워킹 기초가 처음이라면 해당 항목을 먼저 검토하세요.

Amazon CloudWatch 네트워크 모니터링은 세 가지 제품으로 네트워크 경로 성능을 측정합니다. Amazon CloudWatch Network Synthetic Monitor(관리형 프로브), Network Flow Monitor(워크로드의 에이전트), Internet Monitor(AWS 글로벌 네트워크 데이터)가 그것입니다. 각 제품은 서로 다른 관점에서 네트워크를 관측하며, 이 세 제품이 함께 답하는 질문은 Flow Logs와 서비스 지표만으로는 알 수 없는 것입니다. 즉, 이 경로의 성능 저하가 AWS 네트워크 내부에서 발생한 것인지, 아니면 사용자가 소유한 구간에서 발생한 것인지를 파악할 수 있습니다.

[Flow Logs](internal-traffic.md)는 네트워크를 통과한 트래픽을 기록하고, [서비스 지표](service-monitoring.md)는 네트워킹 서비스의 정상 여부를 보고합니다. 그러나 두 가지 모두 두 엔드포인트 사이 경로에서 AWS가 제어하는 구간의 성능이 저하되고 있는지는 알려주지 않습니다. Network Synthetic Monitor와 Network Flow Monitor는 이를 위해 네트워크 상태 지표(NHI, Network Health Indicator)를 게시합니다. NHI는 AWS 네트워크 성능 저하가 관측되었는지를 나타내는 이진 값입니다. Internet Monitor는 인터넷 대상 트래픽에 대해 동일한 방식으로 원인을 규명하며, AWS 네트워크 또는 특정 인터넷 서비스 공급자(ISP) 네트워크를 지목합니다. Network Synthetic Monitor는 AWS Direct Connect 경로와 네 가지 리전 간 경로 유형(AWS Transit Gateway 리전 간 피어링, 리전 간 VPC 피어링, AWS PrivateLink, Amazon EC2 퍼블릭 IP 경로)에 대한 NHI를 게시합니다.

이 페이지는 관측 모델을 기준으로 구성되어 있습니다. 먼저 세 가지 제품 중 어떤 것을 선택할지에 대한 기준을 설명하고, NHI를 올바르게 해석하는 방법(포함되지 않는 항목 포함)을 다룬 후, 모든 제품에 공통으로 적용되는 설계 결정 사항을 설명합니다. 여기에는 멀티 계정 조직에서 모니터를 배포할 위치, IPv6 처리 방법, 노이즈 없이 알람을 설정하는 방법, 비용을 결정하는 요소 등이 포함됩니다.

![네트워크 성능 모니터링 제품 — Network Synthetic Monitor(VPC 서브넷에서 Direct Connect 및 리전 간 경로로의 관리형 프로브), Network Flow Monitor(TCP 플로우를 관측하는 EC2 인스턴스 및 EKS 노드의 에이전트), Internet Monitor(VPC, CloudFront 배포 또는 WorkSpaces 디렉터리에 접근하는 도시 및 네트워크별 최종 사용자와 ASN)가 각각 Amazon CloudWatch에 신호를 게시하는 모습](../assets/observability/network-performance-products.png)
/// caption
네트워크 성능 모니터링 제품 — [Drawio 소스](../assets/observability/network-performance-products.drawio)
///

## 주요 기능 {#key-capabilities}

<div class="grid cards" markdown>

*   :material-radar: **Network Synthetic Monitor**

    ---

    에이전트 설치 없이 VPC 서브넷에서 대상 IP 주소로 관리형 ICMP 또는 TCP 프로브를 실행합니다. AWS Direct Connect 경로 및 리전 간 경로에 대한 왕복 시간, 패킷 손실, NHI를 게시합니다. IPv4 및 IPv6 대상을 지원합니다.

*   :material-chart-timeline-variant: **Network Flow Monitor**

    ---

    Amazon EC2 인스턴스 및 Amazon EKS 노드에 설치된 경량 에이전트가 실제 워크로드 플로우에 대한 TCP 왕복 시간, 재전송, 재전송 타임아웃, 전송 바이트를 보고합니다. 각 모니터는 NHI를 게시합니다.

*   :material-web-check: **Internet Monitor**

    ---

    AWS 글로벌 네트워크의 연결 데이터를 활용하여 최종 사용자와 VPC, Network Load Balancer, Amazon CloudFront 배포 또는 Amazon WorkSpaces 디렉터리 간의 인터넷 성능 및 가용성 기준선을 설정합니다. 하나의 모니터에서 VPC와 CloudFront 배포를 함께 구성할 수 있으며, NLB와 WorkSpaces 디렉터리는 각각 별도의 모니터가 필요합니다. 이벤트 원인을 특정할 수 있는 경우 AWS 네트워크 또는 특정 ASN을 명시합니다.

*   :material-stethoscope: **네트워크 상태 지표(NHI)**

    ---

    AWS 네트워크 성능 저하가 감지되었는지 여부를 보고하는 이진 신호입니다. 장애 원인이 AWS 측인지 사용자 측인지를 구분합니다. 왕복 시간이나 패킷 손실은 보고하지 않습니다.

*   :material-bell-alert: **CloudWatch 통합**

    ---

    세 가지 제품 모두 CloudWatch에 데이터를 게시하므로, 알람, 복합 알람, 대시보드를 다른 네트워킹 지표와 동일한 방식으로 활용할 수 있습니다. Internet Monitor는 Amazon EventBridge에도 상태 이벤트를 게시합니다.

*   :material-account-multiple: **멀티 계정 범위**

    ---

    Network Synthetic Monitor는 모니터링 대상 서브넷을 소유한 계정에서 실행됩니다. Network Flow Monitor는 AWS Organizations를 통해 여러 계정에 걸쳐 운영할 수 있습니다. 중앙 집중식 가시성은 CloudWatch 계정 간 관측성을 통해 제공됩니다.

</div>

## 제품 선택 {#choosing-a-product}

3가지 제품은 서로 대체할 수 없습니다. 관측 대상(합성 프로브, 실제 플로우, 최종 사용자 트래픽), 배포 방식, 커버리지 범위가 각각 다릅니다. 필요한 질문에 맞게 선택하세요.

| 항목 | Network Synthetic Monitor | Network Flow Monitor | Internet Monitor |
| --- | --- | --- | --- |
| 관측 모델 | AWS가 생성하는 능동 프로브(ICMP 또는 TCP) | 인스턴스의 에이전트에서 수집하는 수동 TCP 통계 | AWS 글로벌 네트워크 데이터 기반의 수동 베이스라인 |
| 배포 대상 | 소스 서브넷과 대상 IP 주소를 지정한 모니터 | 커버하려는 각 EC2 인스턴스 또는 EKS 노드에 에이전트 | VPC와 Amazon CloudFront 배포, 또는 NLB만, 또는 Amazon WorkSpaces 디렉터리만 나열하는 모니터 |
| 측정 트래픽 | 구성한 경로를 따라 생성되는 합성 프로브 트래픽 | 실제 워크로드 플로우 | 최종 사용자의 인터넷 트래픽 |
| 경로 커버리지 | Direct Connect에서 온프레미스까지, 그리고 리전 간 경로 | 서브넷, 가용 영역, VPC, AWS 서비스, 다른 리전 엣지까지의 플로우 | 최종 사용자와 AWS 애플리케이션 간의 인터넷 경로 |
| 귀인 신호 | NHI | 모니터별 NHI | AWS 네트워크 또는 ASN을 명시하는 상태 이벤트 |
| 게시 지표 | 왕복 시간, 패킷 손실, NHI | TCP 왕복 시간, 재전송, 재전송 타임아웃, 바이트, NHI | 가용성 및 성능 지표, 상태 이벤트 |
| 주요 한계 | 워크로드가 아닌 프로브 관점의 측정 | Linux 컴퓨팅 전용, TCP 전용 | 온프레미스 또는 프라이빗 경로 커버리지 없음 |

| 질문 | 사용 제품 | 이유 |
| --- | --- | --- |
| "Direct Connect 경로의 지연 시간 또는 손실이 AWS 측 문제인가?" | Network Synthetic Monitor | 에이전트 없이 프로브가 지속적으로 실행되며, NHI가 Direct Connect 위치까지의 경로에서 AWS 측 성능 저하를 보고함 |
| "두 리전 간 성능 저하가 AWS 네트워크 문제인가?" | Network Synthetic Monitor | NHI는 Transit Gateway 리전 간 피어링, 리전 간 VPC 피어링, PrivateLink, EC2 퍼블릭 IP 경로를 커버함 |
| "애플리케이션의 실제 TCP 연결에서 재전송이 발생하고 있으며, AWS가 원인인가?" | Network Flow Monitor | 에이전트가 실제 플로우를 측정하고 주요 원인을 순위별로 제공하며, 모니터 NHI가 AWS 측 장애를 보고함 |
| "재전송률이 가장 높은 가용 영역 쌍 또는 AWS 서비스는 어디인가?" | Network Flow Monitor | 지표가 서브넷, 가용 영역, VPC, AWS 서비스별로 집계됨 |
| "특정 국가 또는 ISP 사용자가 불량한 경험을 겪고 있는가?" | Internet Monitor | 상태 이벤트가 도시-네트워크 및 ASN 단위로 범위가 지정되며, AWS 또는 ISP 귀인 정보 제공 |
| "네트워크를 통과한 트래픽이 무엇이며, 허용되었는가?" | 이 페이지가 아닌 Flow Logs | 이 제품들은 패킷이나 허용/거부 결정을 기록하지 않습니다. [내부 트래픽 모니터링](internal-traffic.md) 참조 |

***핵심 인사이트:*** *관측 가능한 대상과 엔드포인트를 제어하는 주체에 따라 제품을 선택하세요. 프로브는 직접 제어하거나 도달 가능한 대상 IP 주소가 필요합니다. 에이전트는 직접 관리하는 컴퓨팅 리소스가 필요합니다. Internet Monitor는 애플리케이션 리소스만 있으면 됩니다.*

## 네트워크 상태 지표 {#network-health-indicator}

NHI는 이진 값입니다. 값이 100이면 AWS가 제어하는 경로 구간에서 성능 저하가 관찰된 것이고, 값이 0이면 AWS 측 성능 저하가 관찰되지 않은 것입니다. Network Synthetic Monitor의 경우, AWS는 AWS 샘플 데이터셋 전반에 걸친 이상 탐지 및 통계적 상관 분석과 모니터 자체의 패킷 손실 및 왕복 시간(round-trip time) 측정값을 결합하여 NHI를 산출합니다. 따라서 이는 확률적 귀인(probabilistic attribution)이며 보장이 아닙니다. 콘솔에서 Network Flow Monitor 값은 정상(Healthy) 또는 저하(Degraded)로 표시됩니다.

Network Synthetic Monitor는 경로 유형별로 NHI 범위를 다르게 정의합니다. 이 범위는 잘못된 가정의 가장 흔한 원인입니다. "NHI가 정상"이라는 것은 결코 "전체 경로가 정상"을 의미하지 않기 때문입니다.

| 경로 유형 | NHI가 포함하는 범위 | NHI가 포함하지 않는 범위 |
| --- | --- | --- |
| AWS Direct Connect | 모니터링 대상 리소스에서 Direct Connect 위치까지 AWS가 제어하는 경로 | AWS Direct Connect 엔드포인트 이후의 모든 구간(예: 고객 라우터 및 온프레미스 네트워크) |
| AWS Transit Gateway 리전 간 피어링 | Transit Gateway 피어링 연결까지의 AWS 네트워크 경로 | 원격 리전의 어태치먼트, VPC 및 워크로드. 두 Transit Gateway 사이의 경로를 NHI가 어떻게 처리하는지 문서에 명시되어 있지 않으므로, 범위 포함 여부를 가정하지 마십시오 |
| 리전 간 VPC 피어링 | 모니터링 대상 서브넷에서 대상 리전까지의 AWS 네트워크 경로 | 대상 VPC 내부의 모든 구간. 동일 리전 내 피어링은 리전 간 경로가 아닙니다 |
| 다른 리전의 엔드포인트 서비스에 대한 AWS PrivateLink | 모니터링 대상 서브넷에서 대상 리전까지의 AWS 네트워크 경로 | 엔드포인트 서비스 자체 |
| 인터넷 게이트웨이를 통한 다른 리전의 Amazon EC2 퍼블릭 IP 주소 | 모니터링 대상 서브넷에서 대상 리전까지의 AWS 네트워크 경로 | 대상 인스턴스 및 해당 보안 제어 |

NHI에 대한 알람을 구성하는 방식에 영향을 미치는 네 가지 동작이 있습니다.

* **워밍업 지연.** 모니터를 생성하거나, 프로브를 추가하거나, 프로브를 재활성화한 후 AWS가 이상 탐지를 위한 데이터를 수집하는 동안 NHI는 몇 시간 동안 지연됩니다. 이 기간 중 NHI 값이 0이더라도 경로가 정상임을 의미하지 않습니다.
* **Cloud WAN 중간 라우팅.** AWS Cloud WAN을 통한 중간 라우팅을 사용하는 Direct Connect 어태치먼트의 경우 NHI가 정확하지 않습니다. Cloud WAN을 포함하는 하이브리드 네트워크에서는 해당 경로의 성능 문제 지표로 NHI를 사용하지 마십시오.
* **Network Flow Monitor의 모니터 수준 집계.** 저하(Degraded) 값은 선택한 기간 동안 모니터가 추적하는 플로우 중 하나 이상에서 AWS 네트워크 문제가 발생했음을 의미합니다. 단일 워크로드 또는 단일 플로우 그룹으로 각 모니터의 범위를 지정하십시오. 그렇지 않으면 하나의 장애 플로우만으로도 전체 모니터가 저하(Degraded)로 표시됩니다.
* **자동 장애 조치 없음.** Network Synthetic Monitor는 문제를 탐지하고 귀인하지만 트래픽을 재라우팅하지는 않습니다. 복구 방안은 사용자가 직접 설계해야 합니다.

***핵심 인사이트:*** *NHI 100은 "AWS가 관여되어 있음"을 나타냅니다. 왕복 시간이나 패킷 손실이 증가하는 상황에서 NHI 0은 "자체 구간을 확인하라"는 의미입니다. 두 신호를 항상 함께 해석하고, NHI만 단독으로 판단하지 마십시오.*

## 모범 사례 {#best-practices}

### 제품 선택 {#product-selection}

#### 하이브리드 및 리전 간 경로에는 Network Synthetic Monitor 사용 {#use-network-synthetic-monitor-for-hybrid-and-inter-region-paths}

Network Synthetic Monitor는 AWS가 관리하며 모니터링 대상 리소스에 에이전트를 설치할 필요가 없습니다. 따라서 소프트웨어를 설치할 수 없거나 설치하지 않으려는 경로, 즉 온프레미스 대상으로의 Direct Connect 링크나 다른 리전으로의 경로를 커버할 수 있습니다. VPC 서브넷과 대상 IP 주소만 제공하면 됩니다. 이 제품은 3가지 제품 중 애플리케이션 트래픽이 없을 때도 경로를 능동적으로 점검하는 유일한 제품으로, 트래픽이 거의 없는 백업 Direct Connect 연결이나 재해 복구 리전과 같은 대기 경로에 적합한 선택입니다.

애플리케이션 동작을 측정하는 용도로는 사용하지 마십시오. 프로브는 프로브가 보는 것만 측정하며, 특정 애플리케이션 플로우에 문제가 발생하더라도 경로는 ICMP 또는 TCP SYN 프로브에 정상적으로 응답할 수 있습니다.

#### 실제 워크로드 플로우에는 Network Flow Monitor 사용 {#use-network-flow-monitor-for-real-workload-flows}

Network Flow Monitor는 애플리케이션이 실제로 생성하는 트래픽을 보고하므로, 합성 프로브에는 영향을 주지 않지만 실제 TCP 연결에 영향을 미치는 문제를 감지합니다. 커버하려는 모든 Amazon EC2 인스턴스 또는 Amazon EKS 노드에 에이전트를 설치해야 합니다. TCP만 관측하며, 왕복 시간(round-trip time) 데이터는 항상 계산되지 않으므로 희소할 수 있고, 원격 리전은 해당 리전의 엣지까지만 측정되며 리전 내 특정 엔드포인트까지는 측정되지 않습니다.

워크로드 인사이트 뷰를 사용하여 재전송 또는 재전송 타임아웃이 가장 많은 플로우를 찾은 다음, 해당 워크로드에 대한 모니터를 생성하십시오. 모든 것에 대한 모니터부터 시작하면 아무도 조치를 취할 수 없는 단일 Degraded 신호만 생성됩니다.

#### 사용자 대면 엣지에는 Internet Monitor 사용 {#use-internet-monitor-for-the-user-facing-edge}

Internet Monitor는 다른 두 제품과 다른 질문에 답합니다. 특정 도시-네트워크의 사용자가 영향을 받는지, 그리고 AWS 네트워크 또는 ASN이 원인인지를 파악합니다. 프라이빗 경로, Direct Connect, 또는 온프레미스 대상에 대한 가시성은 없습니다. 액세스 로그의 대체재가 아닌, 각 요청의 경험을 캡처하는 [외부 트래픽 모니터링](external-traffic.md)과 함께 사용하십시오.

***핵심 인사이트:*** *중요한 경로에서는 두 제품을 함께 실행하십시오. Network Synthetic Monitor는 유휴 상태일 때 경로가 정상인지 보여주고, Network Flow Monitor는 실제 플로우에 문제가 있는지 보여줍니다. 두 제품 간의 불일치는 네트워크가 아닌 애플리케이션 또는 호스트를 가리킵니다.*

### Transit Gateway를 통한 리전 간 경로 {#inter-region-paths-over-transit-gateway}

#### 중요 트래픽이 발생하는 모든 리전에 모니터 배치 {#place-a-monitor-in-every-region-that-originates-critical-traffic}

Network Synthetic Monitor 프로브는 소스 서브넷에서 피어링된 리전의 대상을 향해 실행됩니다. Transit Gateway 피어링의 경우, NHI(네트워크 상태 표시기)는 해당 소스에서 피어링 연결까지의 로컬 리전 AWS 경로만 커버합니다. 따라서 단일 모니터는 트래픽 패턴에 관계없이 경로의 원격 리전 절반에 대한 AWS 측 귀속을 제공하지 않습니다. 각 리전에 모니터를 배포하고 상대 리전의 대상을 프로브 타겟으로 설정하여, 경로의 각 절반이 자체 NHI를 갖도록 하십시오. 모니터는 자체 소스 서브넷에서 대상을 향해서만 측정합니다.

여러 가용 영역에 걸친 워크로드에는 가용 영역당 하나의 소스 서브넷을 사용하십시오. Network Synthetic Monitor는 각 프라이빗 서브넷의 경로를 모니터링할 수 있으며, 경로는 가용 영역마다 다를 수 있으므로 한 가용 영역의 서브넷이 반드시 다른 가용 영역을 대표하지는 않습니다. 비용은 서브넷 수와 대상 수에 따라 증가하므로, 모든 서브넷이 아닌 대표적인 서브넷과 대상을 선택하십시오.

#### NHI와 Transit Gateway 지표 및 플로우 로그 연계 {#pair-the-nhi-with-transit-gateway-metrics-and-flow-logs}

NHI는 피어링 연결에서 멈춥니다. NHI가 0이고 경로가 저하된 경우, 원인은 NHI가 커버하지 않는 세그먼트에 있습니다. 즉, 어느 한쪽 Transit Gateway의 블랙홀 또는 누락된 경로, 원격 측의 어태치먼트, 또는 대상 자체가 원인일 수 있습니다. [AWS 서비스 모니터링](service-monitoring.md)의 Transit Gateway 패킷 드롭 지표와 [Transit Gateway 플로우 로그](internal-traffic.md#enable-transit-gateway-flow-logs-for-organization-wide-traffic-visibility)의 리전 간 트래픽을 확인하십시오. NHI를 사용하여 AWS 관련 여부를 판단하고, 해당 소스를 사용하여 원인을 찾으십시오.

#### 안정적으로 응답하는 프로브 대상 선택 {#choose-probe-destinations-that-respond-reliably}

보안 그룹, 네트워크 ACL, 또는 방화벽이 프로브를 차단하여 실패하는 경우, 네트워크 문제처럼 보이는 패킷 손실이 발생합니다. 직접 제어하고 항상 프로브 프로토콜에 응답하는 안정적인 대상 IP 주소를 선택하십시오. TCP 프로브 사용 시 프로브가 순환하는 전체 TCP 소스 포트 범위를 허용하십시오. 링크-로컬 주소(인스턴스 메타데이터 주소 포함)나 10.0.0.2와 같은 예약된 주소 또는 AWS 내부 주소를 대상으로 사용하지 마십시오. 프로브 트래픽이 AWS 데이터 센터를 벗어나지 않으므로 왕복 시간이 인위적으로 낮게 측정됩니다.

리전 간 경로의 프로브는 추가 네트워크 경로를 커버하기 위해 다른 경로의 프로브보다 더 많은 트래픽을 전송하므로, 피어링 연결과 대상 호스트에 대한 지속적인 백그라운드 부하로 취급하십시오. 프로브는 또한 모니터링되는 서브넷에서 관리형 탄력적 네트워크 인터페이스를 사용합니다. [서브넷 IP 계획](../foundation/subnets.md)과 서브넷을 관리하는 규칙에 이를 포함하십시오.

***핵심 인사이트:*** *Transit Gateway 리전 간 경로의 NHI는 "내 서브넷과 피어링 연결 사이의 AWS 네트워크가 손상되었는가?"에 답합니다. "두 워크로드 사이의 모든 것이 정상인가?"에는 답하지 않습니다.*

### 귀속에 대한 알람 설정 {#alarming-on-attribution}

#### NHI와 패킷 손실 및 왕복 시간 결합 {#combine-the-nhi-with-packet-loss-and-round-trip-time}

NHI 알람만으로는 AWS가 관련되어 있을 수 있다는 것은 알 수 있지만 사용자가 영향을 받는지는 알 수 없습니다. 패킷 손실 또는 왕복 시간 알람만으로는 문제의 책임 소재를 알 수 없습니다. 두 조건을 모두 요구하는 [복합 알람](service-monitoring.md#use-composite-alarms-to-reduce-noise)을 사용하고, 두 가지 결과를 다르게 라우팅하십시오.

| 패킷 손실 또는 왕복 시간 | NHI | 해석 | 대응 |
| --- | --- | --- | --- |
| 저하됨 | 100 | 경로에 영향을 미치는 AWS 네트워크 장애 | 중복 경로가 있는 경우 런북에 따라 장애 조치 여부를 결정한 후, 모니터 증거와 함께 AWS Support 케이스 오픈 |
| 저하됨 | 0 | AWS 제어 세그먼트 외부의 장애 | 라우터, 온프레미스 네트워크, 원격 리전 또는 애플리케이션 조사 |
| 정상 | 100 | 아직 측정 가능한 영향은 없지만 AWS 이벤트 가능성 있음 | 낮은 심각도로 알림을 보내고 추세를 모니터링. 두 신호를 모두 요구하는 복합 알람은 이 상태에서 발생할 수 없으므로, 이 행은 NHI만을 대상으로 하는 별도의 알람이 필요 |
| 정상 | 0 | 정상 | 조치 불필요 |

이는 알람 피로도도 줄여줍니다. 측정 가능한 영향 없이 모든 일시적인 AWS 측 이상에 대해 페이지를 보내는 NHI 알람은 팀이 이를 무시하도록 훈련시킵니다. 심각도 계층 및 라우팅에 대해서는 [알림](notifications.md)을 참조하십시오.

이러한 알람의 누락 데이터 처리를 명시적으로 설정하십시오. NHI는 모니터를 생성하거나 프로브를 추가 또는 재활성화한 후 워밍업 기간 동안 데이터가 없습니다. `missing` 처리를 사용하면 알람이 INSUFFICIENT_DATA로 이동하는데, 이는 아직 아무도 측정하지 않은 경로에 대한 정확한 상태입니다. `notBreaching`을 사용하면 알람이 OK를 보고하여 정상으로 읽힙니다. `missing`을 사용하고, 모니터 변경 후 INSUFFICIENT_DATA를 대시보드에서 페이지가 아닌 "워밍업 중"으로 표시하십시오.

#### NHI를 자동 장애 조치의 트리거가 아닌 증거로 취급 {#treat-the-nhi-as-evidence-not-as-a-trigger-for-automatic-failover}

NHI는 통계적 귀속입니다. 이를 자동으로 처리하면 오탐 발생 시 정상 경로에서 트래픽을 전환할 수 있으며, 백업 경로로 부하를 이동하면 피하려던 혼잡이 발생할 수 있습니다. NHI를 알림과 런북 결정을 유도하는 데 사용하십시오. Network Synthetic Monitor는 장애 조치를 수행하지 않으며, 라우팅 프로토콜이 이미 경로를 결정하는 경우 NHI나 프로브 지표를 기반으로 장애 조치를 구축해서는 안 됩니다. Direct Connect의 경우, BGP가 장애 조치를 수행하며, 빠른 감지를 위한 BFD와 AS_PATH 및 로컬 선호도 설계가 트래픽 이동 위치를 결정합니다. 모니터링은 런북에 정보를 제공하고 라우팅이 장애 조치를 수행합니다. 프로브 지표 기반의 Lambda 구동 장애 조치는 라우팅 프로토콜과 경쟁하여 플랩을 유발할 수 있기 때문입니다. 장애 조치 설계에 대해서는 [하이브리드 및 멀티 클라우드](../connectivity/hybrid-multicloud.md)를 참조하십시오.

### 멀티 계정 배포 {#multi-account-deployment}

#### 모니터링되는 서브넷을 소유한 계정에 모니터 배포 {#deploy-monitors-in-the-account-that-owns-the-monitored-subnet}

Network Synthetic Monitor는 모니터링되는 서브넷을 소유한 계정과 동일한 계정에 생성해야 합니다. 공유 VPC 모델에서 서브넷 소유자는 참여자가 아닌 VPC 소유자 계정입니다. 모니터가 중앙 네트워킹 계정에만 있는 것이 아니라 워크로드 계정 또는 공유 VPC를 소유한 계정에 위치하도록 계획하십시오.

인프라를 코드로 모니터를 배포하여 모든 계정과 리전이 동일한 프로브 세트를 갖도록 하고, [CloudWatch 계정 간 관측성](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html)을 사용하여 NHI, 패킷 손실, 왕복 시간 지표를 [AWS 서비스 모니터링](service-monitoring.md#deploy-a-centralized-monitoring-account)에 설명된 모니터링 계정으로 집계하십시오. Network Flow Monitor는 AWS Organizations로 구성하면 계정 간 범위를 지정할 수 있으므로, 하나의 뷰로 워크로드 계정을 커버할 수 있습니다.

#### 경로를 소유한 팀이 알람 소유권 유지 {#keep-ownership-of-alarms-with-the-team-that-owns-the-path}

Transit Gateway 또는 Direct Connect 경로 소유자는 워크로드 팀이 아닌 NHI 및 경로 손실 알람을 수신해야 합니다. 모니터가 워크로드 계정 또는 공유 VPC를 소유한 계정에 있으므로, 경로 소유자는 기본적으로 자신의 지표를 볼 수 없습니다. CloudWatch 계정 간 관측성을 통해 소스 계정의 NHI, 패킷 손실, 왕복 시간 지표를 모니터링 계정으로 공유하고, 해당 모니터링 계정에서 경로 소유자의 알람을 정의하십시오. 워크로드 팀은 자체 계정에서 자신의 플로우에 대한 Network Flow Monitor 알람을 정의합니다. 두 팀이 대화할 때 귀속이 보이도록 두 알람을 동일한 인시던트 채널로 전송하십시오.

### IPv6 고려 사항 {#ipv6-considerations}

#### IPv4와 IPv6 경로를 별도로 모니터링 {#monitor-ipv4-and-ipv6-paths-separately}

IPv4 경로가 정상이라고 해서 IPv6 경로도 정상임을 의미하지는 않습니다. 보안 그룹, 네트워크 ACL, 경로, BGP 광고는 주소 패밀리마다 다릅니다. Network Synthetic Monitor는 듀얼 스택 VPC에서 IPv4 및 IPv6 대상을 지원하지만, 단일 모니터는 두 주소 패밀리를 혼합할 수 없으므로 각 중요 경로에 대해 패밀리별로 하나의 모니터를 생성하십시오. IPv6 커버리지 누락을 격차로 취급하십시오. 듀얼 스택 워크로드는 IPv4 지표가 정상인 동안 IPv6 경로에서 실패할 수 있습니다.

### 비용 최적화 {#cost-optimization}

#### 각 제품의 과금 항목 이해 {#understand-what-each-product-charges-for}

가격은 리전마다 다르고 변경될 수 있으므로, 아래 항목과 [CloudWatch 가격 페이지](https://aws.amazon.com/cloudwatch/pricing/)에서 현재 값을 확인하십시오.

| 제품 | 가격 항목 | 비용 유발 요인 |
| --- | --- | --- |
| Network Synthetic Monitor | 시간당 모니터링 리소스(소스 서브넷 및 각 서브넷에서 모니터링되는 대상), 각 프로브에 대한 CloudWatch 지표. 리전 간 프로브의 경우 프로브 트래픽에 대한 데이터 요금: Transit Gateway 데이터 처리 및 리전 간 데이터 전송 | 서브넷 수 × 대상 IP 주소 수, 리전 간 경로의 경우 지속적인 프로브 트래픽 |
| Network Flow Monitor | 시간당 모니터링 리소스(인스턴스 또는 노드의 각 에이전트), CloudWatch 지표 | 에이전트를 실행하는 인스턴스 또는 노드 수 |
| Internet Monitor | 시간당 모니터링 리소스, 시간당 모니터링 도시-네트워크, 진단 로그에 대한 CloudWatch Logs | 모니터링되는 도시-네트워크 수(사용자 기반에 따라 증가하며, 트래픽 비율과 도시-네트워크 최대값으로 제한 가능) |

리전 간 경로의 프로브는 지속적으로 실행되며 다른 경로의 프로브보다 더 많은 트래픽을 전송하므로, 해당 트래픽에는 Transit Gateway 데이터 처리 및 리전 간 데이터 전송([Transit Gateway 가격](https://aws.amazon.com/transit-gateway/pricing/) 참조)과 같이 워크로드 트래픽과 동일한 데이터 요금이 부과됩니다. 프로브를 추가할 때마다 워크로드가 실행되지 않을 때도 해당 기준 비용이 증가합니다.

CloudWatch 알람, 대시보드, 지표 요금은 3가지 모두에 추가로 적용됩니다. 동일한 [지표 수식 및 복합 알람 기법](service-monitoring.md#use-metric-math-to-reduce-alarm-count)을 사용하여 알람 수를 제한하십시오.

#### 중요 경로로 커버리지 범위 제한 {#scope-coverage-to-critical-paths}

모든 서브넷을 모든 대상에 대해 프로빙하면 신호 추가 없이 비용만 증가합니다. 각 비즈니스 크리티컬 경로에서 가용 영역당 하나의 서브넷으로 시작하십시오. Network Flow Monitor의 경우, 워크로드 인사이트 뷰의 상위에 나타나는 워크로드에 먼저 에이전트를 설치하고 그 다음으로 확장하십시오. Internet Monitor의 경우, 트래픽 비율과 도시-네트워크 최대값이라는 두 가지 커버리지 제어를 사용하십시오. 비율은 모니터링되는 도시-네트워크 수를 결정하고, 최대값은 해당 수를 제한하며 비율보다 우선하여 비용을 예측 가능하게 만듭니다. 두 가지 모두 격차를 만듭니다. 모니터링하지 않는 트래픽에 대해서는 Internet Monitor가 상태 이벤트를 발생시키지 않으므로, 해당 사용자에게 영향을 미치는 이벤트는 보이지 않습니다. 목표 커버리지에 필요한 도시-네트워크에서 최대값을 선택하고, 가치가 낮은 트래픽에 대한 격차는 의도적으로 수용하십시오.

***핵심 인사이트:*** *비용은 관측 지점 수에 따라 증가합니다. 리전 간 경로의 Network Synthetic Monitor의 경우, 워크로드 트래픽처럼 과금되는 경로를 통과하는 프로브 트래픽에 따라서도 증가합니다. 각 중요 경로에서 AWS와 자체 네트워크를 구분할 수 있는 최소한의 관측 지점 세트를 선택하십시오.*

## 각 제품의 사용 시기 {#when-to-use-each-product}

**Network Synthetic Monitor**가 적합한 경우:

* Direct Connect 또는 리전 간 경로의 성능 저하가 AWS 네트워크 내부에서 발생하는지 확인해야 할 때
* 대기 중인 Direct Connect 연결이나 재해 복구 리전처럼 경로에 실제 트래픽이 거의 없거나 전혀 없을 때
* 엔드포인트에 에이전트를 설치할 수 없거나 목적지가 AWS 외부에 있을 때

Network Synthetic Monitor가 적합하지 **않은** 경우:

* 실제 애플리케이션 플로우를 측정해야 할 때 (Network Flow Monitor 사용)
* 보안 제어에 의해 전송되거나 허용된 내용을 확인해야 할 때 ([플로우 로그](internal-traffic.md) 사용)
* 인터넷 사용자 경험을 측정해야 할 때 (Internet Monitor 사용)
* 경로가 Cloud WAN 코어 네트워크를 통과하거나, Cloud WAN 중간 라우팅을 사용하는 Direct Connect 어태치먼트인 경우. Cloud WAN 코어 네트워크 경로는 NHI 경로 유형이 아니며, 해당 Direct Connect 사례에서는 NHI가 정확하지 않으므로 귀속 판단에 NHI를 사용하지 마세요

**Network Flow Monitor**가 적합한 경우:

* Linux 컴퓨팅 환경에 에이전트를 설치할 수 있고, 실제 TCP 플로우를 측정해야 할 때
* 재전송 횟수를 기준으로 플로우를 순위화하여 가장 큰 문제 원인을 찾아야 할 때
* 워크로드별로 범위를 지정하여 애플리케이션이 의존하는 플로우에 대한 귀속 정보가 필요할 때

Network Flow Monitor가 적합하지 **않은** 경우:

* 에이전트를 설치할 수 없는 컴퓨팅 환경에서 워크로드가 실행될 때 (Network Synthetic Monitor 사용)
* 트래픽이 TCP가 아닐 때
* 다른 리전 내의 특정 엔드포인트를 검사해야 할 때 (측정이 리전 경계에서 중단되기 때문)

**Internet Monitor**가 적합한 경우:

* 애플리케이션이 인터넷 사용자를 대상으로 하며, 어떤 도시와 ISP가 영향을 받는지 파악해야 할 때
* AWS 네트워크와 ISP 네트워크 간의 귀속 정보가 필요할 때

Internet Monitor가 적합하지 **않은** 경우:

* Direct Connect, VPN, Transit Gateway 등 프라이빗 경로를 사용할 때 (Network Synthetic Monitor 또는 Network Flow Monitor 사용)
* 요청별 세부 정보가 필요할 때 ([CloudFront 및 로드 밸런서 액세스 로그](external-traffic.md) 사용)

## 네트워크 성능 모니터링과 다른 서비스의 결합 {#combining-network-performance-monitoring-with-other-services}

| 조합 | 네트워크 성능 모니터링이 제공하는 것 | 다른 서비스가 제공하는 것 |
| --- | --- | --- |
| **Network Synthetic Monitor + Transit Gateway 지표** | 피어링 연결까지의 AWS 측 귀인(attribution) 및 왕복 시간과 패킷 손실 | NHI가 다루지 않는 구간에서 원인을 파악하는 드롭 카운터 및 어태치먼트 상태 |
| **Network Synthetic Monitor + Direct Connect 지표** | 엔드투엔드 경로 측정 및 Direct Connect 위치까지의 AWS 측 귀인 | 물리 계층 및 라우팅 계층에 대한 연결 상태, BGP 세션 상태, 광 레벨 |
| **Network Flow Monitor + VPC Flow Logs** | 플로우 그룹별 재전송 및 왕복 시간 통계와 AWS 귀인 | 소스, 대상, 허용/거부 결정에 대한 플로우별 레코드 |
| **Internet Monitor + CloudFront 및 로드 밸런서 로그** | AWS 또는 ISP 귀인이 포함된 도시 네트워크 및 ASN 상태 이벤트 | 요청별 지연 시간, 상태 코드, 클라이언트 세부 정보 |
| **NHI + CloudWatch 복합 알람** | 귀인 신호 | 알림 발송 전 측정 가능한 영향을 요구하는 불리언 논리 |
| **네트워크 성능 모니터링 + AWS Health Dashboard** | 서브넷에서 측정된 특정 경로에 대한 영향. Internet Monitor가 전반적인 문제의 원인이 AWS 네트워크임을 파악하면, AWS가 취하는 완화 조치와 함께 AWS Health Dashboard 알림도 전송 | AWS가 선언한 서비스 이벤트 및 유지 관리 공지 |
| **네트워크 성능 모니터링 + 알림** | 장애를 나타내는 지표 및 상태 이벤트 | 라우팅, 심각도 계층, 에스컬레이션(자세한 내용은 [알림](notifications.md) 참조) |

## 도입 지침 {#adoption-guidance}

**신규 환경.** 첫 번째 프로덕션 워크로드가 사용하기 전에 모든 Direct Connect 및 리전 간 경로에 Network Synthetic Monitor 프로브를 배포하여, 첫 번째 인시던트 발생 시 기준선(baseline)을 확보하세요. 랜딩 존에서 모니터의 계정 및 서브넷 배치를 계획하고, 서브넷 크기 산정 시 관리형 네트워크 인터페이스를 포함하세요. AZ 간 또는 리전 간 트래픽에 의존하는 워크로드의 기본 이미지에 Network Flow Monitor 에이전트를 추가하세요. 인터넷 연결 애플리케이션은 출시 시점에 Internet Monitor 모니터를 생성하세요.

**기존 환경.** 원인을 알 수 없는 인시던트가 발생했던 경로부터 시작하세요. 중요한 하이브리드 또는 리전 간 경로마다 Network Synthetic Monitor를 하나씩 추가하되, 가용 영역(Availability Zone)당 소스 서브넷을 하나씩 구성하고, NHI와 패킷 손실을 연계하는 복합 알람을 생성하세요. 워크로드 인사이트 상위에 표시되는 워크로드에 Network Flow Monitor 에이전트를 추가하세요. 각 제품을 배포할 리전이 지원되는지 설계 전에 반드시 확인하세요.

## 문서 {#documentation}

<div class="grid cards" markdown>

*   :material-file-document: **Network Synthetic Monitor**

    ---

    프로브, 모니터, 요구 사항, 그리고 Direct Connect 및 리전 간 경로 유형에 대한 네트워크 상태 지표 작동 방식을 설명합니다.

    [:octicons-arrow-right-24: 작동 방식](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-how-it-works.html)

*   :material-file-document: **Network Flow Monitor**

    ---

    Amazon EC2 및 Amazon EKS의 TCP 플로우에 대한 에이전트, 범위, 워크로드 인사이트, 모니터 및 네트워크 상태 지표를 설명합니다.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor.html)

*   :material-file-document: **Internet Monitor**

    ---

    Internet Monitor가 인터넷 성능 기준선을 설정하고 상태 이벤트를 AWS 네트워크 또는 ASN에 귀속시키는 방식을 설명합니다.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html)

*   :material-earth: **Network Synthetic Monitor 리전**

    ---

    Network Synthetic Monitor의 현재 리전 가용성입니다. 배포를 설계하기 전에 확인하세요.

    [:octicons-arrow-right-24: 지원 리전](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-regions.html)

*   :material-file-document: **Transit Gateway 피어링 어태치먼트**

    ---

    Transit Gateway 리전 간 피어링 작동 방식을 설명합니다. 이는 NHI가 지원하는 리전 간 경로 유형 중 하나입니다.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-peering.html)

*   :material-currency-usd: **CloudWatch 요금**

    ---

    CloudWatch 네트워크 모니터링의 플로우 모니터링, 인터넷 모니터링, 합성 모니터링에 대한 요금 체계를 설명합니다.

    [:octicons-arrow-right-24: 요금](https://aws.amazon.com/cloudwatch/pricing/)

</div>

## 관련 관측성 페이지 {#related-observability-pages}

* **[내부 트래픽 모니터링](internal-traffic.md)** — Flow Logs는 네트워크를 통과한 트래픽을 보여줍니다. 네트워크 성능 모니터링은 경로상의 성능 저하가 AWS 네트워크에서 비롯된 것인지 여부를 확인합니다.
* **[외부 트래픽 모니터링](external-traffic.md)** — 액세스 로그는 각 요청을 캡처합니다. Internet Monitor는 동일한 사용자에 대한 도시 네트워크 및 ASN 상태 이벤트를 추가합니다.
* **[AWS 서비스 모니터링](service-monitoring.md)** — 서비스 지표는 리소스 상태를 보고하며, Transit Gateway 및 Direct Connect의 지표와 알람은 NHI가 다른 원인을 가리킬 때 근본 원인을 파악하는 데 도움을 줍니다.
* **[알림](notifications.md)** — NHI, 패킷 손실, 상태 이벤트 알람을 대응 담당 팀에 전달합니다.

**기반과의 관계:**

* **[서브넷](../foundation/subnets.md)**: Network Synthetic Monitor 프로브는 모니터링 대상 서브넷의 관리형 네트워크 인터페이스를 사용하므로, 서브넷 크기 조정 및 규칙에서 이를 반드시 고려해야 합니다.
* **[AWS Organizations](../foundation/organizations.md)**: 계정 구조에 따라 모니터가 실행되는 위치와 Network Flow Monitor 범위 및 계정 간 관측성 구성 방식이 결정됩니다.

**연결과의 관계:**

* **[AWS 내 연결](../connectivity/within-aws.md)**: Transit Gateway 피어링 및 Cloud WAN을 다룹니다. NHI는 Transit Gateway 리전 간 피어링 경로를 포함하지만, Cloud WAN 코어 네트워크 경로는 NHI의 경로 유형에 해당하지 않습니다.
* **[하이브리드 및 멀티 클라우드](../connectivity/hybrid-multicloud.md)**: NHI 기반 런북이 의존하는 장애 상태 용량 및 이중화를 포함한 Direct Connect 설계를 다룹니다.
