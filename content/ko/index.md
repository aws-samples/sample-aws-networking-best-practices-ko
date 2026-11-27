---
title: AWS 네트워킹 베스트 프랙티스
hide:
  - navigation
  - toc
---

# 소개 {#introduction}

AWS 네트워킹 모범 사례를 위한 참조 아키텍처입니다.

엔터프라이즈 AWS 네트워크는 다섯 가지 상호 연결된 기반 위에 구축됩니다.

* **기반** - AWS Organizations, Amazon VPC, 서브넷, Amazon VPC IP Address Manager를 사용하여 구축된 핵심 인프라로, 다른 모든 요소가 의존하는 토대
* **연결** - 인터넷 게이트웨이, AWS Transit Gateway, AWS Direct Connect, VPN 서비스를 통한 통신
* **애플리케이션 네트워킹** - Elastic Load Balancing을 통한 트래픽 분산, Amazon VPC Lattice를 통한 서비스 간 통신, 컨테이너 네트워킹
* **보안** - AWS Network Firewall, AWS PrivateLink, Amazon Route 53 Resolver DNS Firewall을 통한 보호 및 네트워크 격리
* **관측성** - 모든 서비스에 걸친 모니터링 및 문제 해결 기능

![AWS 네트워크 참조 아키텍처](assets/introduction/AWS-Network-Reference-Architecture.png)
/// caption
AWS 네트워크 참조 아키텍처
///

## 시작하기 {#getting-started}

달성하려는 목표가 명확하다면 **[의사결정 맵](decisions.md)**에서 시작하세요. 일반적인 AWS 네트워킹 질문을 권장 서비스, 패턴, 트레이드오프에 직접 연결해 줍니다.

어떤 결정이 되돌리기 어렵고 설계가 언제 맞지 않게 되는지 알고 싶다면 **[의사결정 프레임워크](decision-framework.md)**를 읽어보세요. 네트워킹 결정을 단방향 또는 양방향 문으로 분류하고, 이를 다시 열게 되는 변곡점을 명시합니다.

또는 기반부터 시작하여 기초를 이해한 다음, 특정 네트워킹 요구 사항에 따라 각 기반 영역을 탐색하세요.

<div class="grid cards" markdown>

*   :material-network: **기반**

    ---

    VPC, 서브넷, 라우팅, 핵심 인프라 구성 요소를 포함한 필수 AWS 네트워킹 개념을 다룹니다.

    ---

    [:octicons-arrow-right-24: 기반](foundation/)

*   :material-lan-connect: **연결**

    ---

    인터넷 액세스, AWS 내부 연결, 하이브리드 및 멀티 클라우드 네트워킹 솔루션을 다룹니다.

    ---

    [:octicons-arrow-right-24: 연결](connectivity/)

*   :material-application: **애플리케이션 네트워킹**

    ---

    현대적인 애플리케이션을 위한 로드 밸런싱, 서비스 간 통신, 컨테이너 메시 네트워킹을 다룹니다.

    ---

    [:octicons-arrow-right-24: 애플리케이션 네트워킹](application-networking/)

*   :material-lock-outline: **보안**

    ---

    심층 방어 전략, 액세스 제어, 위협 방지를 통해 AWS 네트워크를 보호합니다.

    ---

    [:octicons-arrow-right-24: 보안](security/)

*   :material-monitor-eye: **관측성**

    ---

    네트워크 성능을 모니터링하고, 연결 문제를 해결하며, AWS 네트워크에 대한 가시성을 확보합니다.

    ---

    [:octicons-arrow-right-24: 관측성](observability/)

</div>

## 기여하기 {#contribute}

[이슈 보고](community/report-a-correction.md), [새로운 모범 사례 제안](community/new-best-practice.md), [콘텐츠 기여](community/making-a-pull-request.md)를 통해 이 가이드를 개선하는 데 도움을 주세요. 모든 사람을 위한 포괄적인 AWS 네트워킹 리소스를 만들기 위한 커뮤니티 주도 활동에 함께해 주세요.
