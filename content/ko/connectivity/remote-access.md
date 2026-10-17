# 원격 액세스 {#remote-access}

!!! info "사전 요구 사항"
    이 섹션은 [Amazon VPC](../foundation/vpc.md) 및 [AWS Organizations](../foundation/organizations.md)에 대한 이해를 전제로 합니다. AWS 네트워킹 기초가 처음이라면 해당 항목을 먼저 검토하세요.

인가된 사용자와 디바이스에게 내부 AWS 애플리케이션 액세스를 제공하는 것은 인프라 연결과는 별개의 아키텍처 과제입니다. AWS는 서로 반대 방향에서 이 문제를 해결하는 두 가지 서비스를 제공합니다. [AWS Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/what-is.html)은 사용자를 네트워크에 배치하여 IP로 애플리케이션에 접근할 수 있게 하고, [AWS Verified Access](https://docs.aws.amazon.com/verified-access/latest/ug/what-is-verified-access.html)는 애플리케이션을 제로 트러스트 정책 엔진 뒤에 배치하여 ID와 디바이스 포스처(device posture)를 기반으로 모든 요청을 인증하고 인가합니다. 웹 애플리케이션에는 VPN 클라이언트가 필요 없으며(비 HTTP 앱은 경량 연결 클라이언트를 사용), 두 서비스 모두 하이브리드 연결 여부와 무관하게 동작합니다. Direct Connect 회선이 없는 순수 클라우드 조직도 하이브리드 환경과 마찬가지로 원격 액세스가 필요합니다.

새로운 애플리케이션 액세스 사용 사례에는 AWS Verified Access가 권장 옵션입니다. 제로 트러스트 애플리케이션 액세스는 다수의 애플리케이션과 사용자에 걸쳐 더 잘 확장되고, VPN 클라이언트 및 엔드포인트 인증서 유지 관리에 따른 운영 부담을 없애며, 네트워크 계층에서 복제하기 어려운 요청별 정책을 적용합니다.

## AWS Client VPN {#aws-client-vpn}

AWS Client VPN은 최종 사용자에게 VPC로의 네트워크 수준 연결을 제공하는 관리형 OpenVPN 호환 서비스입니다. 연결된 각 클라이언트는 사용자가 구성한 클라이언트 CIDR에서 IP 주소를 할당받으며, 연결된 VPC의 리소스(및 전송 경로를 통해 다른 VPC와 온프레미스 네트워크)에 접근할 수 있습니다. 인증은 Active Directory, AWS IAM Identity Center와 같은 ID 공급자와의 SAML 기반 페더레이션, 그리고 인증서 기반 상호 인증을 지원합니다.

Client VPN은 사용자에게 네트워크 계층 도달성이 실제로 필요한 경우에 적합합니다. 예를 들어 서브넷 내 여러 호스트와 포트에 임시로 액세스해야 하는 관리자(단일 관리형 애플리케이션이 아닌 경우), 직접 IP 연결이나 비 TCP 프로토콜이 필요한 도구, 또는 IP 주소로 클라이언트를 인증하는 레거시 애플리케이션이 해당됩니다. 또한 사용자가 이미 VPN 클라이언트에 익숙하고 애플리케이션이 ID 인식 액세스 방식으로 리팩터링되지 않은 기존 워크플로에도 적합합니다.

### AWS Client VPN 모범 사례 {#aws-client-vpn-best-practices}

#### 기본적으로 스플릿 터널 사용 {#use-split-tunnel-by-default}

특정 컴플라이언스 요구 사항으로 인해 풀 터널이 필요한 경우가 아니라면, 스플릿 터널을 사용하여 AWS로 향하는 트래픽만 Client VPN을 통과하고 일반 인터넷 트래픽은 클라이언트의 로컬 네트워크를 통해 직접 나가도록 하세요. 풀 터널은 이그레스 비용을 증가시키고 VPN 엔드포인트에 부하를 집중시킵니다. 스플릿 터널은 사용자 경험도 향상시킵니다. 지연 시간에 민감한 트래픽(화상 통화, 스트리밍)은 로컬 인터넷 경로를 유지합니다.

#### 라우팅만이 아닌 인가 규칙 정의 {#define-authorization-rules-not-just-routes}

Client VPN 인가 규칙은 어떤 사용자가 어떤 대상에 접근할 수 있는지를 제어합니다. 라우팅 테이블만으로는 트래픽이 흐를 수 있지만, 일치하는 인가 규칙이 없으면 사용자는 자신의 역할이 접근해서는 안 되는 대상에도 여전히 접근할 수 있습니다. 직무 기능을 기준으로 인가 규칙을 설계하세요. 관리자는 관리 서브넷에 대한 SSH/RDP 액세스를, 개발자는 애플리케이션 VPC에 대한 액세스를, 일반 사용자는 자신에게 필요한 특정 애플리케이션에 대한 액세스만 부여합니다.

#### 충돌을 피하도록 클라이언트 CIDR 계획 {#plan-the-client-cidr-to-avoid-conflicts}

클라이언트 CIDR(연결된 VPN 클라이언트에 할당되는 IP 범위)은 VPC CIDR, 피어링된 VPC, 온프레미스 네트워크, 또는 다른 VPN 클라이언트 풀과 겹치지 않아야 합니다. IPAM 계획에서 전용 범위를 사용하세요. VPC와 온프레미스에 일반적으로 사용되는 `10.0.0.0/8` 공간과의 충돌을 피하기 위해 `172.16.0.0/12` 공간에서 `/16`을 사용하는 것이 일반적인 선택입니다.

#### 가용 영역뿐만 아니라 엔드포인트 수로 확장 계획 {#scale-by-endpoint-count-not-just-availability-zone}

Client VPN 엔드포인트는 많은 동시 연결을 지원하지만, 크기 조정 시 안정 상태뿐만 아니라 최대 동시 사용자 수를 고려해야 합니다. CloudWatch에서 `ActiveConnectionsCount`와 `CrlDaysToExpiry`를 모니터링하세요. 수천 명의 동시 사용자가 있는 조직의 경우, 사용자 집단 또는 애플리케이션 그룹별로 세분화된 여러 엔드포인트를 고려하세요.

#### ID와 디바이스 포스처 결합 {#combine-identity-with-device-posture}

사용자만 인증하면 그들이 사용하는 디바이스를 신뢰하게 됩니다. ID와 디바이스 포스처를 결합하여 액세스가 디바이스의 보안 상태(컴플라이언스 상태, 디스크 암호화, 방화벽)에도 의존하도록 하세요. 이를 통해 포스처에 민감한 사용자 집단에 대해 "신뢰할 수 있는 사용자"에서 "정상 디바이스를 사용하는 신뢰할 수 있는 사용자"로 기준을 높일 수 있습니다. 포스처는 지속적으로 적용됩니다. 디바이스가 연결될 때 확인되고 세션 기간 동안 재평가되므로, 컴플라이언스를 벗어난 디바이스는 다음 재연결 시까지 신뢰되는 것이 아니라 연결이 끊깁니다. 이는 Client VPN 인가 규칙 위에 추가되는 별도의 정책이며 대체가 아니므로, 두 가지를 모두 유지해야 합니다.

디바이스를 확인할 수 있는 신호와 정책 정의 방법은 [AWS Client VPN의 디바이스 포스처](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/device-posture.html)를 참조하세요.

#### 포스처 적용 전 클라이언트 및 공급자 지원 범위 확인 {#confirm-client-and-provider-coverage-before-enforcing-posture}

포스처 게이팅은 연결 가능한 대상을 좁히므로, 먼저 자신의 플릿을 대상으로 검증하세요. AWS 제공 클라이언트가 필요하므로 서드파티 OpenVPN 클라이언트는 포스처 게이팅된 엔드포인트에 접근할 수 없습니다. 포스처는 지원되는 디바이스 신뢰 공급자에서도 제공되며, 공급자 및 OS 지원 범위는 다양합니다. 적용 전에 플릿이 지원되는지 확인하고, 현재 목록은 [지원되는 디바이스 신뢰 공급자](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/device-posture-providers.html) 페이지를 확인하세요. 그런 다음 섀도 모드로 정책을 실행하세요. 섀도 모드는 아무도 차단하지 않고 결정 내용을 로깅하므로, 실제 적용 전에 차단될 디바이스를 미리 파악할 수 있습니다.

## AWS Verified Access {#aws-verified-access}

AWS Verified Access는 VPN 클라이언트 없이 기업 애플리케이션에 대한 제로 트러스트 액세스를 제공합니다. 사용자는 브라우저 또는 애플리케이션별 클라이언트를 통해 애플리케이션에 접근하며, Verified Access는 ID(AWS IAM Identity Center 또는 서드파티 ID 공급자)와 디바이스 포스처(CrowdStrike 또는 모바일 디바이스 관리 벤더와 같은 통합 디바이스 신뢰 공급자)를 결합한 정책에 따라 모든 요청을 평가합니다. 정책을 충족하지 못하는 요청은 거부되고, 충족하는 요청은 애플리케이션으로 전달됩니다.

Verified Access는 웹 기반 애플리케이션(HTTP/HTTPS)과 TCP, SSH, RDP를 통해 접근하는 비 웹 애플리케이션을 모두 지원합니다. 웹 애플리케이션은 클라이언트 설치 없이 표준 브라우저를 통해 접근하며, 비 HTTP(S) 엔드포인트는 사용자 디바이스에 [Verified Access 연결 클라이언트](https://docs.aws.amazon.com/verified-access/latest/ug/connectivity-client.html)가 필요합니다. 정책은 AWS에서 중앙 집중식으로 관리되며, Cedar 정책 언어로 표현되고, ID, 디바이스 포스처, 요청 컨텍스트를 기반으로 요청별로 평가됩니다. 따라서 모든 개별 요청은 네트워크 연결의 지속적인 도달성을 상속받는 것이 아니라 자체적으로 인가됩니다.

### AWS Verified Access 모범 사례 {#aws-verified-access-best-practices}

#### 모든 새로운 애플리케이션 액세스 사용 사례에 Verified Access 우선 적용 {#start-with-verified-access-for-every-new-application-access-use-case}

새로운 애플리케이션 액세스 사용 사례에는 AWS Verified Access가 권장 옵션입니다. 그 이유는 다음과 같습니다.

* **엔드포인트에 배포, 배포, 유지 관리할 VPN 클라이언트가 없습니다.** 사용자는 이미 사용 중인 표준 클라이언트(브라우저 또는 프로토콜별 클라이언트)를 통해 애플리케이션에 접근합니다.
* **요청별 정책 평가** — ID와 디바이스 포스처를 기반으로 하며, VPN 연결이 포스처 통과 후 부여하는 지속적인 네트워크 도달성 대신 모든 요청을 평가합니다.
* **모든 액세스 시도(허용 및 거부)에 대한 포괄적인 로깅** — 이유, 사용자, 디바이스 컨텍스트를 포함합니다. VPN 연결 로그와 애플리케이션 로그를 별도로 재구성하는 것보다 훨씬 용이합니다.
* **규모에 따른 간소화된 운영 모델** — 새 애플리케이션 온보딩 시 VPN 인가 규칙 확장 및 경로 재전파 대신 Verified Access 엔드포인트와 정책만 추가하면 됩니다.

#### 처음부터 디바이스 신뢰 통합 {#integrate-device-trust-from-day-one}

Verified Access 정책은 ID *와* 디바이스 포스처를 결합할 때 가장 효과적입니다. 나중에 추가하는 것이 아니라 배포 시점에 디바이스 신뢰 공급자(CrowdStrike, Jamf 또는 다른 MDM/EDR 벤더)를 연결하세요. ID만 확인하는 정책은 기존 SSO 확인과 크게 다르지 않습니다. 디바이스 포스처(OS 패치 수준, 디스크 암호화, EDR/컴플라이언스 상태 등 디바이스 신뢰 공급자가 보고하는 신호)를 추가하는 것이 Verified Access를 진정한 제로 트러스트로 만드는 핵심입니다.

#### 세분화되고 감사 가능한 액세스 제어를 위한 Cedar 정책 사용 {#use-cedar-policies-for-fine-grained-auditable-access-control}

Verified Access가 사용하는 정책 언어인 Cedar는 사용자 속성, 그룹 멤버십, 디바이스 포스처 신호, 요청 속성(IP, 시간, 애플리케이션)에 대한 조건을 지원합니다. "인증된 모든 사용자 허용"과 같은 광범위한 규칙 대신 애플리케이션별로 명시적인 정책을 작성하세요. 세분화된 정책은 감사하기 쉽고, 컴플라이언스 팀에 설명하기 쉬우며, 자격 증명이 침해되었을 때의 장애 반경을 줄입니다.

#### Client VPN에서 점진적으로 마이그레이션 {#migrate-from-client-vpn-incrementally}

Verified Access가 현재 적합하지 않은 경우 Client VPN을 계속 사용할 수 있으며, 마이그레이션 중에 두 서비스를 함께 운영할 수 있습니다. 권장 패턴은 다음과 같습니다.

1. 처음부터 새 애플리케이션에 Verified Access 배포
2. 기존 애플리케이션은 라이프사이클이 허용하는 시점(일반적으로 다음 주요 업데이트 또는 보안 검토 시)에 Verified Access로 마이그레이션
3. 네트워크 계층 도달성이 실제로 필요한 경우(VPC 내 라우팅 가능한 IP, 임의의 호스트 및 포트, 비 TCP 프로토콜)로 Client VPN 범위를 점진적으로 축소
4. 애플리케이션 포트폴리오가 현대화됨에 따라 시간이 지나면서 Verified Access로 통합

[Client VPN과 Verified Access 상호 운용성 패턴](https://aws.amazon.com/blogs/networking-and-content-delivery/aws-client-vpn-and-aws-verified-access-migration-and-interoperability-patterns/)에서 이러한 마이그레이션 경로를 자세히 다룹니다.

## 각 서비스의 사용 시기 {#when-to-use-each-service}

**AWS Verified Access**가 적합한 경우:

* 사용자가 웹 애플리케이션(HTTP/HTTPS) 또는 TCP/SSH/RDP 서비스에 액세스해야 하는 경우
* 지속적인 네트워크 연결의 주기적 재평가 대신 요청별 인가(모든 요청에 대해 ID, 디바이스 포스처, 요청 컨텍스트 평가)가 필요한 경우
* VPN 클라이언트 배포 및 유지 관리를 없애고 싶은 경우
* 새 애플리케이션을 원격 액세스에 온보딩하는 경우

**AWS Client VPN**이 적합한 경우:

* 애플리케이션이 완전한 네트워크 계층 IP 도달성(애플리케이션 수준 액세스가 아닌)을 필요로 하는 경우
* 사용자가 특정 애플리케이션이 아닌 광범위한 네트워크 범위에 액세스해야 하는 경우
* 레거시 프로토콜이나 워크플로가 사용자의 VPC 내 라우팅 가능한 IP에 의존하는 경우
* 아직 마이그레이션되지 않은 VPN 기반 워크플로가 조직에 확립되어 있는 경우

AWS Client VPN은 애플리케이션 액세스를 위한 **장기적인 해답이 아닙니다**. 새로운 애플리케이션에는 Verified Access를 우선 적용하고, 실제 네트워크 계층이 필요한 경우에만 Client VPN을 사용하세요.

## 문서 {#documentation}

<div class="grid cards" markdown>

*   :material-file-document: **AWS Client VPN 문서**

    ---

    엔드포인트, 인증 방법, 인가 규칙, 스플릿 터널 구성을 다루는 전체 서비스 문서입니다.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/what-is.html)

*   :material-file-document-outline: **AWS Verified Access 문서**

    ---

    엔드포인트, Cedar 정책, ID 및 디바이스 신뢰 공급자, 지원되는 애플리케이션 유형을 다루는 전체 서비스 문서입니다.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/verified-access/latest/ug/what-is-verified-access.html)

*   :material-post: **AWS Client VPN과 Verified Access 상호 운용성 패턴**

    ---

    전환 기간 동안 Client VPN과 Verified Access를 함께 운영하기 위한 네 가지 마이그레이션 및 상호 운용성 패턴입니다.

    [:octicons-arrow-right-24: 블로그 게시물](https://aws.amazon.com/blogs/networking-and-content-delivery/aws-client-vpn-and-aws-verified-access-migration-and-interoperability-patterns/)

*   :material-currency-usd: **AWS Verified Access 요금**

    ---

    Verified Access 엔드포인트의 애플리케이션 시간당 및 GB당 데이터 처리 요금입니다.

    [:octicons-arrow-right-24: 요금](https://aws.amazon.com/verified-access/pricing/)

</div>

## 관련 페이지 {#related-pages}

**다른 연결 주제와의 관계:**

* **[하이브리드 및 멀티 클라우드 연결](hybrid-multicloud.md)** — 하이브리드 연결은 온프레미스와 AWS 간의 인프라 수준 경로를 제공합니다. 원격 액세스는 애플리케이션에 대한 사용자 수준 경로를 제공합니다. 두 가지는 독립적입니다. Verified Access와 Client VPN은 하이브리드 연결 없이도 동작합니다.

**보안 주제와의 관계:**

* **[네트워크 세분화](../security/segmentation.md)** — Verified Access 인가 정책은 애플리케이션 경계에서 ID 기반 세분화를 제공합니다. Client VPN 인가 규칙은 VPN 사용자에 대한 네트워크 수준 세분화를 제공합니다.
