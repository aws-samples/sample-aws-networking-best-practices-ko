# 네트워킹 의사결정 맵 {#networking-decision-map}

이 페이지는 일반적인 AWS 네트워킹 질문을 적합한 서비스, 패턴, 그리고 이 가이드의 해당 페이지로 연결해 줍니다. 달성하려는 목표는 알고 있지만 어떤 AWS 서비스나 아키텍처 패턴이 적합한지 확실하지 않을 때 활용하세요.

## VPC 및 계정 연결 {#connecting-vpcs-and-accounts}

| 목표 | 권장 서비스 | 주요 트레이드오프 | 자세히 알아보기 |
| --- | --- | --- | --- |
| 중앙 집중식 정책으로 여러 리전에 걸쳐 다수의 VPC 연결 | **AWS Cloud WAN** — 선언적 네트워크 정책, 자동화된 연결 수락, 세그먼트 기반 격리, 글로벌 동적 라우팅 | TGW 대비 연결당 비용이 높지만, 정책 기반 관리로 리전별 수동 구성 불필요 | [AWS 내부 연결](connectivity/within-aws.md) |
| 단일 리전 내 VPC를 허브를 통해 연결 | **AWS Transit Gateway** — 수천 개의 연결을 지원하는 리전 허브, 라우팅 테이블 세분화 | 단일 리전에서는 Cloud WAN보다 단순하지만, 여러 리전에 걸쳐 관리하면 복잡해짐 | [AWS 내부 연결](connectivity/within-aws.md) |
| 두 VPC 간 고처리량 연결 및 동일 AZ 데이터 처리/전송 비용 없음 | **VPC 피어링** — 최저 지연 시간, 대역폭 제한 없음, 동일 AZ 트래픽에 GB당 요금 없음, 비전이적 | 소수의 쌍을 넘어서면 확장 어려움; CIDR 중복 불가 | [AWS 내부 연결](connectivity/within-aws.md) |
| HTTP/gRPC 서비스를 다른 VPC 및 계정에 노출 | **VPC Lattice 서비스** — 피어링이나 TGW 없이 VPC 간 연결, IAM 인증 정책, 가중치 기반 라우팅, CIDR 중복 허용 | L7 전용(HTTP/HTTPS/gRPC)으로만 동작 | [AWS 내부 연결](connectivity/within-aws.md) |
| 다른 계정에 데이터베이스 또는 온프레미스 엔드포인트에 대한 프라이빗 TCP 액세스 제공 | **VPC Lattice VPC 리소스** — NLB 없이 사용자 지정 도메인 이름 및 DNS를 대상으로 하는 리소스 구성, CIDR 중복 허용, 포트 범위 노출 | 단방향(소비자 → 리소스 방향만); TCP 전용 | [AWS 내부 연결](connectivity/within-aws.md) |
| NLB 뒤의 TCP 서비스를 소비자 VPC에 노출 | **AWS PrivateLink 엔드포인트 서비스** — NLB 기반, 소비자별 인터페이스 엔드포인트, ENI 기반 | 소비자 수에 비례하여 선형 확장(소비자 VPC당 엔드포인트 하나); 인증 정책 없음 | [AWS 내부 연결](connectivity/within-aws.md) |

## 인터넷 연결 {#reaching-the-internet}

| 목표 | 권장 패턴 | 주요 트레이드오프 | 자세히 알아보기 |
| --- | --- | --- | --- |
| 프라이빗 IPv4 리소스의 인터넷 액세스 허용 | **NAT 게이트웨이** — 가용 영역 또는 리전 단위, 탄력적이며 자동 확장 | 중앙 집중화하지 않으면 데이터 처리 및 시간당 비용 발생 | [인터넷 연결](connectivity/internet.md) |
| 프라이빗 IPv6 리소스의 인터넷 액세스 허용 | **이그레스 전용 인터넷 게이트웨이** — 데이터 처리 비용 없음(데이터 전송 비용은 적용), VPC별, 아웃바운드 전용 | 중앙 집중화 불가; NAT66/NPTv6 미지원 | [인터넷 연결](connectivity/internet.md) |
| HTTP/HTTPS 애플리케이션을 인터넷에 노출 | **CloudFront + AWS WAF + ALB** (분산형 인그레스) — 엣지 캐싱, L7 보호, 프라이빗 백엔드를 위한 VPC Origins | 공유 VPC를 통한 중앙 집중식 인그레스는 로드 밸런서 체이닝과 장애 반경을 증가시킴; 컴플라이언스 요구 사항이 없는 한 지양 | [인터넷 연결](connectivity/internet.md) |
| TCP/UDP 서비스를 인터넷에 노출 | **NLB** 인터넷 대면, VPC별, 클라이언트 IP 보존 가능 | 추가 보안을 위해 보안 그룹 또는 차세대 방화벽과 함께 사용 | [인터넷 연결](connectivity/internet.md) |
| AWS 서비스 트래픽에 대한 NAT 게이트웨이 비용 절감 | **VPC 엔드포인트** — S3/DynamoDB용 게이트웨이 엔드포인트(무료), 기타 서비스용 인터페이스 엔드포인트 | 인터페이스 엔드포인트는 시간당 및 데이터 처리 요금 발생 | [인터넷 연결](connectivity/internet.md) |

## 온프레미스 및 다른 클라우드 연결 {#connecting-to-on-premises-and-other-clouds}

| 목표 | 권장 서비스 | 주요 트레이드오프 | 자세히 알아보기 |
| --- | --- | --- | --- |
| 온프레미스와의 프라이빗하고 예측 가능한 대역폭 연결 | **AWS Direct Connect** — 1/10/100/400 Gbps 전용 회선, 파트너 호스팅 회선 50Mbps~10Gbps; 인터넷 대비 낮은 이그레스 요금 | 전용 포트는 최대 72시간 내 준비되지만 프로비저닝에 크로스 커넥트 또는 공급자/파트너 조율 필요; 최대 복원력 설계 권장(연결 2개 이상, 위치 2개 이상) | [하이브리드 및 멀티 클라우드](connectivity/hybrid-multicloud.md) |
| 대기 없이 빠르게 구축하는 온프레미스 암호화 연결 | **AWS Site-to-Site VPN** — 인터넷을 통한 IPsec, 수 분 내 구성, Large 터널당 최대 5 Gbps | 인터넷 기반: 지연 시간 및 처리량 예측 불가. 프로덕션 하이브리드 환경에서 Direct Connect 대체 불가 | [하이브리드 및 멀티 클라우드](connectivity/hybrid-multicloud.md) |
| AWS와 Google Cloud 간 프라이빗 연결 | **AWS Interconnect** — 관리형 직접 클라우드 간 연결, MACsec 암호화, 수 분 내 프로비저닝 | 현재 AWS ↔ Google Cloud만 지원; 확장 중. 미지원 쌍에는 파트너 기반 Direct Connect 사용 | [하이브리드 및 멀티 클라우드](connectivity/hybrid-multicloud.md) |
| 기존 SD-WAN을 AWS와 통합 | **Transit Gateway Connect 또는 Cloud WAN 터널리스 Connect** — BGP를 사용하는 GRE/터널리스 연결 | 트랜짓 VPC에 SD-WAN 가상 어플라이언스 필요(또는 TGW Connect의 경우 DX 언더레이를 사용하는 온프레미스) | [하이브리드 및 멀티 클라우드](connectivity/hybrid-multicloud.md) |
| 원격 사용자에게 애플리케이션 액세스 제공 | **AWS Verified Access** (권장) — 제로 트러스트, 요청별 ID + 디바이스 상태 확인, VPN 클라이언트 불필요 | 애플리케이션이 네트워크 계층 IP 연결(SSH, RDP, 레거시 프로토콜)을 실제로 필요로 하는 경우에만 Client VPN 사용 | [원격 액세스](connectivity/remote-access.md) |

## 네트워크 트래픽 보안 {#securing-network-traffic}

| 목표 | 권장 서비스 | 주요 트레이드오프 | 자세히 알아보기 |
| --- | --- | --- | --- |
| 네트워크 계층에서 리소스 간 통신 제어 | **보안 그룹** — 스테이트풀, ENI별, 참조 기반 규칙. 모든 워크로드의 기본 액세스 제어 | 거부 불가(허용 전용); 서브넷 수준의 명시적 거부에는 NACL 사용 | [경계 제어](security/perimeter-inbound.md) |
| L7 공격으로부터 웹 애플리케이션 보호 | CloudFront 또는 ALB의 **AWS WAF** — 관리형 규칙 그룹, 속도 제한, 봇 제어, 지역 차단 | AWS WAF는 HTTP 전용; 비HTTP 검사에는 Network Firewall 사용 | [경계 제어](security/perimeter-inbound.md) |
| 인터넷 이그레스 또는 VPC 간 트래픽을 포함한 VPC 경계 트래픽 검사(L3-L7) | **AWS Network Firewall** — 관리형 스테이트풀/스테이트리스 검사, Suricata IPS 규칙, 도메인 필터링 | 비용 고려 필요 — 엔드포인트 시간당 + GB당 처리 요금 | [경계 제어](security/perimeter-inbound.md) |
| 서드파티 방화벽 어플라이언스 삽입 | **Gateway Load Balancer** — GENEVE 캡슐화를 사용하여 서드파티 방화벽 어플라이언스로의 세션 고정 유지, 투명한 삽입, 원본 헤더 보존 | 어플라이언스 플릿(패치, 확장, 라이선스) 직접 관리 필요; Network Firewall보다 운영 비용 높음. 일부 벤더는 완전 관리형 GWLB 기반 솔루션 제공 | [경계 제어](security/perimeter-inbound.md) |
| 워크로드가 승인되지 않은 도메인에 액세스하는 것을 차단 | **Route 53 DNS Firewall** — DNS 확인 시점의 도메인 기반 필터링, 백만 쿼리당 수 센트 수준의 비용 | 하드코딩된 IP 또는 DNS-over-HTTPS로 우회 가능; 완전한 보호를 위해 Network Firewall과 함께 사용 | [아웃바운드 제어](security/outbound.md) |
| 승인되지 않은 S3 버킷으로의 데이터 유출 방지 | S3 게이트웨이 엔드포인트의 **VPC 엔드포인트 정책** — 조직의 버킷으로만 제한 | 엔드포인트를 통한 S3 트래픽만 적용; 다른 유출 경로는 차단하지 않음 | [아웃바운드 제어](security/outbound.md) |
| 가장 강력한 수준의 워크로드 격리 | **별도의 AWS 계정** — 독립적인 IAM, 네트워크, 청구 경계. 무료, 네트워킹 구성 불필요 | 계정 간 연결에는 명시적 연결 수단 필요(Transit Gateway, Cloud WAN, VPC Lattice) | [네트워크 세분화](security/segmentation.md) |
| 마이크로서비스 간 ID 기반 액세스 제어 적용 | **VPC Lattice 인증 정책** — IAM SigV4 서명, 요청별 평가, 네트워크 위치와 무관 | 소비자가 SigV4로 요청에 서명해야 함; 서명 도입 전 VPC/경로 기반 조건으로 시작 가능 | [네트워크 세분화](security/segmentation.md) |

## 모니터링 및 문제 해결 {#monitoring-and-troubleshooting}

| 목표 | 권장 서비스 | 주요 트레이드오프 | 자세히 알아보기 |
| --- | --- | --- | --- |
| VPC 내 트래픽 흐름 확인 | **VPC Flow Logs** — VPC 수준에서 활성화, 40개 이상의 필드를 포함한 사용자 지정 형식, 비용 효율적인 Athena 쿼리를 위해 S3로 전송 | S3 전송: 가장 비용 효율적. CloudWatch Logs: 비용이 높지만 실시간 알림 가능 | [내부 트래픽](observability/internal-traffic.md) |
| 조직 내 모든 VPC 간 트래픽 확인 | **Transit Gateway Flow Logs** — 네트워킹 계정의 단일 구성으로 모든 VPC 간 트래픽 포괄 | TGW를 통과하는 트래픽만 캡처; VPC 내부 트래픽은 VPC별 Flow Logs 필요 | [내부 트래픽](observability/internal-traffic.md) |
| 로드 밸런서 상태 및 성능 모니터링 | **CloudWatch 지표** — HealthyHostCount, TargetResponseTime, HTTPCode_ELB_5XX, RejectedConnectionCount | 지표는 집계됨; 요청별 조사에는 ALB/NLB 액세스 로그 사용 | [AWS 서비스 모니터링](observability/service-monitoring.md) |
| VPN 터널 또는 DX 연결 다운 시 알림 수신 | 상태 변경 이벤트에 대한 **EventBridge 규칙** + TunnelState/ConnectionState에 대한 **CloudWatch 알람** | 두 터널 모두 다운(장애)이 아닌 단일 터널 다운(이중화 손실) 시 알람 설정 | [알림](observability/notifications.md) |
| 이그레스 비용 및 목적지 파악 | **AWS Cost and Usage Reports**(리소스별 데이터 전송 항목) + **CloudWatch 지표**(BytesOutToDestination, ActiveConnectionCount) + **VPC Flow Logs**(목적지 IP, 흐름별 바이트) | CUR은 비용 귀속 정보를 제공하지만 시차가 있음; Flow Logs는 실시간 목적지 상세 정보를 제공하지만 비용 데이터 없음 — 전체 파악을 위해 두 가지 모두 활용 | [외부 트래픽](observability/external-traffic.md) |
| EC2 인스턴스와 AWS 서비스 간 실시간 패킷 손실 및 지연 시간 측정 | **Network Flow Monitor** — 인스턴스의 경량 에이전트가 TCP 성능 통계 보고; 대시보드에서 흐름별 패킷 손실, 지연 시간, 귀속 정보 표시 | 각 인스턴스에 에이전트 설치 필요; TCP 기반 흐름만 지원 | [AWS 서비스 모니터링](observability/service-monitoring.md) |
| 인터넷 대면 애플리케이션의 인터넷 성능 및 가용성 모니터링 | **Internet Monitor** — AWS 글로벌 네트워크 데이터를 사용하여 성능 기준선 설정; 상태 이벤트 표시 및 CloudFront 또는 대체 리전을 통한 라우팅 개선 제안 | AWS가 관찰 가능한 트래픽 경로로만 가시성 제한; 온프레미스 미지원 | [AWS 서비스 모니터링](observability/service-monitoring.md) |
| 온프레미스 목적지까지의 하이브리드 연결 지연 시간 및 패킷 손실 추적 | **Network Synthetic Monitor** — AWS 리소스에서 온프레미스 IP로의 완전 관리형 프로브; 에이전트 설치 불필요; 구성 가능한 임계값으로 상태 이벤트 알림 | AWS에서 온프레미스 방향만 측정; 목적지 IP가 프로브 소스에서 도달 가능해야 함 | [AWS 서비스 모니터링](observability/service-monitoring.md) |

## 로드 밸런서 선택 {#choosing-a-load-balancer}

| 트래픽 유형 | 사용할 것 | 사용하지 않을 것 | 이유 |
| --- | --- | --- | --- |
| HTTP, HTTPS, gRPC | **ALB** | NLB(처리는 가능하지만 앱 계층 가시성 없음) | ALB는 콘텐츠 기반 라우팅, TLS 종료, AWS WAF 통합, mTLS, 자동 대상 가중치 제공 |
| TCP, UDP, TLS, QUIC(비HTTP) | **NLB** | ALB | NLB는 HTTP 디코딩 없이 전달; 클라이언트 IP 보존; 가용 영역별 정적 IP 제공 |
| 정적 IP와 HTTP 라우팅 모두 필요 | **ALB를 대상으로 하는 NLB** | ALB 단독 | NLB가 정적 IP 제공; ALB가 그 뒤에서 L7 라우팅 처리 |
| 서드파티 방화벽 삽입 | **GWLB** | Network Firewall | GWLB는 자체 어플라이언스 플릿용; Network Firewall은 AWS 관리형 대안 |
| VPC 간 서비스 간 통신 | **VPC Lattice** | ALB + PrivateLink | VPC Lattice는 로드 밸런서 관리 없이 VPC 간 연결, 인증, 가중치 기반 라우팅, 액세스 로그를 번들로 제공 |
