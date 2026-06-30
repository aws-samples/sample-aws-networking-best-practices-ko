# 컨테이너 메시(Container Mesh) {#container-mesh}

!!! info "사전 요구 사항"
    이 섹션은 [Amazon VPC](../foundation/vpc.md), [서브넷](../foundation/subnets.md), [AWS 내부 연결](../connectivity/within-aws.md) 페이지의 연결 패턴(특히 Amazon VPC Lattice), [서비스 간 통신](service-to-service.md) 페이지, 그리고 [로드 밸런싱](load-balancing.md) 페이지에 대한 이해를 전제로 합니다. 컨테이너 메시 패턴은 이러한 모든 기본 요소를 재사용하며, 이 페이지에서는 그 위에 구축되는 컨테이너 특화 메커니즘을 다룹니다.

## 서비스 메시란 무엇이며, 필요한지 여부 {#what-a-service-mesh-is-and-whether-you-need-one}

서비스 메시는 [CNCF 용어집의 정의](https://glossary.cncf.io/service-mesh/)에 따르면, 애플리케이션 코드 변경 없이 마이크로서비스 간 트래픽을 관리하고 신뢰성, 관측성, 보안을 일관되게 제공하는 전용 인프라 레이어입니다. 전통적인 구현 방식은 컨트롤 플레인이 구성하는 파드별 사이드카 프록시(데이터 플레인)이며, 사이드카 없는 변형 방식은 eBPF를 통해 동일한 로직을 커널에 구현합니다. 이 용어는 광범위하게 사용됩니다. 각 메시 프로젝트마다 경계를 조금씩 다르게 정의하기 때문에, "서비스 메시가 필요한가?"라는 질문은 실질적으로 "어떤 특정 기능이 필요하며, 각 기능은 어디에 위치해야 하는가?"라는 질문과 같습니다.

클라우드 네이티브 AWS 환경에서는 서비스 메시 도입의 주된 이유가 되는 대부분의 기능이 이미 AWS 관리형 서비스로 기본 제공됩니다. 아래 표는 메시가 제공하는 기능을 세부 항목으로 분류하고, 각 항목이 어디에 해당하는지 보여줍니다.

| 기능 | 설명 | AWS 기본 제공 | 메시 고유 영역 |
| --- | --- | --- | --- |
| **서비스 디스커버리** | 안정적인 서비스 이름을 현재 대상으로 확인 | Amazon Route 53, AWS Cloud Map | 일반적인 워크로드에서는 없음. |
| **서비스 간 인증** | 호출자별 암호화 ID를 서비스 수준에서 평가 | IAM + AWS SigV4(Amazon VPC Lattice 인증 정책), Amazon API Gateway IAM 인증자는 공유 시크릿 없이 엔드투엔드 ID 기반 인증을 제공. | AWS 네이티브 호출자에 대해서는 없음. |
| **상호 TLS(mTLS)** | 핸드셰이크 시 양측이 인증서를 제시 | ALB mTLS 및 Amazon VPC Lattice TLS 패스스루(사이드카 또는 백엔드에서 mTLS 종료)가 리스너 측을 담당. | 메시 관리형 mTLS 수명 주기(파드별 자동 발급, 자동 교체, 자동 폐기)는 사이드카 메시 영역. |
| **트래픽 관리** | 가중치 기반 라우팅, 블루/그린, 카나리 배포 | Amazon VPC Lattice 가중치 기반 라우팅, ALB 가중치 기반 대상 그룹 | 메시 네이티브 CRD(`VirtualService`, `DestinationRule`, `ServiceProfile`) 및 요청별 장애 주입은 사이드카 메시 전용. |
| **복원력 정책** | 요청별 재시도, 타임아웃, 이상값 감지, 서킷 브레이킹 | 애플리케이션 수준 또는 AWS SDK 재시도; Amazon VPC Lattice 및 로드 밸런서 상태 확인. | 데이터 플레인 구성으로서 사이드카가 적용하는 **요청별** 정책은 사이드카 메시 전용. |
| **관측성** | 요청별 액세스 로그 및 분산 추적 | Amazon VPC Lattice 액세스 로그(ID 인식), ALB 액세스 로그, AWS X-Ray, Amazon CloudWatch Application Signals. | 애플리케이션 변경 없이 사이드카가 내보내는 골든 시그널 메트릭은 사이드카 메시 전용. |
| **네트워크 정책** | 어떤 워크로드가 어떤 워크로드에 접근할 수 있는지 | 보안 그룹(태스크별, 파드별), Amazon VPC CNI를 통한 Kubernetes NetworkPolicy, Amazon VPC Lattice 인증 정책. | 메시 CRD 기반 정책은 사이드카 메시 전용. |
| **멀티 클러스터 서비스 연결** | 클러스터 A의 서비스를 클러스터 B에서 로컬 서비스처럼 접근 가능하게 하며, 팀 및 클러스터 소유권을 분리 | Amazon VPC Lattice는 독립적인 팀 경계를 유지하면서 멀티 클러스터, 멀티 계정 접근을 제공. | 멀티 클러스터 연결이 메시 내부에 위치해야 하는 경우의 메시 네이티브 클러스터 메시 컨트롤 플레인(Istio multi-primary, Cilium Cluster Mesh). |

클라우드 네이티브 AWS 환경에서는 **디스커버리, ID 기반 인증, 트래픽 관리, 관측성, 네트워크 정책, 멀티 클러스터 연결이 이미 관리형 서비스로 제공됩니다**. 사이드카 메시에 남은 영역은 메시 관리형 mTLS 수명 주기, 메시 CRD 기반 트래픽 및 복원력 정책, 그리고 특정 클러스터 메시 컨트롤 플레인 패턴입니다. 이 중 어느 것도 메시를 도입하는 나쁜 이유가 아닙니다. 일부 워크로드에서는 실제로 필요한 요구사항이지만, 기본 출발점이 아니라 **명시적으로 합의된 요구사항**이어야 합니다.

멀티 클러스터 항목은 가장 신중하게 검토할 필요가 있습니다. 팀들은 독립적인 팀이 각자의 클러스터를 운영하면서도 서비스를 상호 노출할 수 있도록 클러스터 메시 패턴을 선택합니다. Amazon VPC Lattice는 네트워크 레이어에서 동일한 확장 문제를 해결합니다. 각 팀은 자체 클러스터를 소유하고, 서비스를 공유 서비스 네트워크에 내보내며, 다른 클러스터의 소비자는 Lattice 서비스를 기반으로 하는 Route 53 별칭을 통해 해당 서비스에 접근합니다. 메시 컨트롤 플레인 없이도 팀 경계가 유지됩니다.

워크로드에 메시 고유 영역의 항목이 하나 이상 실제로 필요하다면, 자체 관리형 메시가 올바른 선택입니다. 이 페이지의 나머지 부분에서는 AWS에서 컨테이너 서비스 간 아키텍처가 취하는 세 가지 형태를 다룹니다. 클러스터 내 기본 요소, 메시의 대안으로서의 Amazon VPC Lattice, 그리고 AWS 네트워킹 위에 구축하는 자체 관리형 메시입니다.

![세 가지 패턴을 보여주는 컨테이너 메시 형태: 클러스터 내 컨테이너 네트워킹(EKS, ECS), 메시의 대안으로서의 Amazon VPC Lattice, AWS 네트워킹 위의 자체 관리형 메시](../assets/application-networking/container-mesh-shapes.png)
/// caption
컨테이너 메시 형태 — [Drawio 소스](../assets/application-networking/container-mesh-shapes.drawio)
///

## 클러스터 내 컨테이너 네트워킹 {#in-cluster-container-networking}

첫 번째 형태는 사실 "메시"가 아닙니다. Amazon ECS와 Amazon EKS가 이미 제공하는 클러스터 내 기본 요소들입니다. 이를 잘 활용하면 메시를 별도로 운영하지 않고도 "단일 클러스터 내 메시가 필요하다"는 요구사항 대부분을 충족할 수 있습니다.

### Amazon EKS 클러스터 내 네트워킹 {#amazon-eks-in-cluster-networking}

Amazon EKS 파드는 기본적으로 [Amazon VPC CNI](https://docs.aws.amazon.com/eks/latest/userguide/pod-networking.html)를 사용합니다. 각 파드는 클러스터 서브넷에서 라우팅 가능한 VPC IP를 할당받고, 노드에는 IP 용량을 확보하기 위해 보조 ENI가 연결되며, 파드 간 트래픽은 오버레이 없이 VPC 내부에서 직접 흐릅니다. 필요한 경우 프리픽스 위임(Prefix Delegation)으로 노드당 IP 밀도를 높일 수 있으며, IPv6 모드(클러스터에서 `enableIPv6: true` 설정)를 사용하면 모든 파드에 IPv6 주소가 부여되어 신규 클러스터에서 IPv4 고갈 문제를 완전히 해소할 수 있습니다. Cilium, Calico 같은 대체 CNI도 더 풍부한 정책 시맨틱이나 eBPF 기반 데이터 플레인이 필요한 경우 유효한 선택지이지만, Amazon VPC CNI는 AWS가 공식 지원하는 기본값이며 **파드용 보안 그룹**을 일급(first-class)으로 지원하는 유일한 CNI입니다.

클러스터 내 서비스 디스커버리는 Kubernetes Services와 CoreDNS를 통해 이루어집니다. 안정적인 가상 IP를 위한 ClusterIP, 파드 IP 직접 DNS를 위한 헤드리스 서비스, 서비스 이름 별칭을 위한 ExternalName이 제공됩니다. `kube-proxy`(`iptables` 또는 `IPVS` 모드)나 이를 대체하는 Cilium이 ClusterIP에서 파드 IP로의 로드 밸런싱을 처리합니다. 이 중 어느 것도 메시를 필요로 하지 않습니다.

파드의 ID는 메시 없이 서비스 간 인증을 가능하게 하는 핵심 요소입니다.

* **[Amazon EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html)**는 신규 클러스터에 권장되는 패턴입니다. 파드 ID 에이전트가 DaemonSet으로 실행되어 AWS SDK 자격 증명 조회를 가로채고, 파드의 IAM 역할에 대한 단기 자격 증명을 반환합니다. 설정은 연결(association)당 단일 API 호출로 완료되며, 역할별 OIDC 신뢰 관계가 필요하지 않습니다.
* **[IAM Roles for Service Accounts (IRSA)](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html)**는 이전 패턴으로, 현재도 완전히 지원됩니다. OIDC 기반 신뢰 모델에 이미 의존하는 기존 클러스터에서 사용하고, 신규 클러스터는 Pod Identity를 기본으로 사용하세요.

AWS 레이어의 네트워크 정책은 **[파드용 보안 그룹](https://docs.aws.amazon.com/eks/latest/userguide/security-groups-for-pods.html)**(파드별 VPC 보안 그룹 식별자, 다른 ENI에 사용하는 것과 동일한 SG)을 통해 제공됩니다. 레이블 기반 클러스터 내 네트워크 정책을 위해 **[VPC CNI 네트워크 정책](https://docs.aws.amazon.com/eks/latest/userguide/cni-network-policy.html)**(또는 도입한 경우 Cilium/Calico)을 그 위에 계층화하세요. 두 레이어는 상호 보완적입니다. SG는 AWS 측 접근을 제어하고, NetworkPolicy는 클러스터 측 접근을 제어합니다.

#### Amazon EKS 클러스터 내 네트워킹 모범 사례 {#amazon-eks-in-cluster-best-practices}

* **신규 클러스터에는 Amazon VPC CNI를 기본으로 사용하세요**. VPC CNI가 충족하지 못하는 구체적인 요구사항(eBPF 데이터 플레인, 더 풍부한 NetworkPolicy 시맨틱, kube-proxy 대체)이 있을 때만 Cilium이나 Calico를 선택하세요.
* **신규 클러스터에는 Amazon EKS Pod Identity를 사용하고, 기존 클러스터는 IRSA를 유지하세요**.
* **파드용 보안 그룹과 Kubernetes NetworkPolicy를 계층화하세요**. SG는 "어떤 AWS 소스가 이 파드에 접근할 수 있는가"를 답하고, NetworkPolicy는 "어떤 워크로드 레이블이 이 파드에 접근할 수 있는가"를 답합니다.
* **신규 클러스터에는 IPv6 모드를 도입하세요**. IPv4 고갈 문제가 사라지고, 프리픽스 위임 튜닝 없이 라우팅 가능한 v6 주소 체계를 클러스터에 적용할 수 있습니다.

#### Amazon EKS 클러스터 내 네트워킹 문서 {#amazon-eks-in-cluster-documentation}

<div class="grid cards" markdown>

*   :material-file-document: **Amazon VPC CNI**

    ---

    VPC 라우팅 가능한 파드 IP, 프리픽스 위임, IPv6 지원을 갖춘 Amazon EKS 기본 파드 네트워킹.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/eks/latest/userguide/pod-networking.html)

*   :material-file-document: **Amazon EKS Pod Identity**

    ---

    신규 클러스터에서 파드에 IAM 역할을 할당하는 권장 패턴. 역할별 OIDC 신뢰 관계가 필요 없습니다.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html)

*   :material-file-document: **IAM Roles for Service Accounts (IRSA)**

    ---

    기존 환경을 위해 유지되는, 파드에 IAM 역할을 할당하는 OIDC 기반 패턴.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html)

*   :material-file-document: **파드용 보안 그룹**

    ---

    AWS 레이어에서 ID 기반 네트워크 정책을 위한 파드별 VPC 보안 그룹.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/eks/latest/userguide/security-groups-for-pods.html)

*   :material-file-document: **Amazon VPC CNI 네트워크 정책**

    ---

    클러스터 내 레이블 기반 트래픽 제어를 위한 AWS 네이티브 Kubernetes NetworkPolicy 구현.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/eks/latest/userguide/cni-network-policy.html)

</div>

### Amazon ECS 클러스터 내 네트워킹 {#amazon-ecs-in-cluster-networking}

**[awsvpc 네트워크 모드](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking-awsvpc.html)**의 Amazon ECS 태스크는 각각 고유한 ENI, VPC IP, 보안 그룹을 갖습니다. 이를 통해 AWS 레이어에서 태스크별 ID를 무료로 얻을 수 있으며, ENI에 적용되는 것과 동일한 보안 그룹 기반 네트워크 정책이 태스크에도 적용됩니다. `awsvpc`는 Fargate의 기본값이며 EC2 기반 태스크에도 권장되는 모드입니다.

단일 Amazon ECS 클러스터 내에서 AWS가 제공하는 관리형 메시에 가장 가까운 것은 **[Amazon ECS Service Connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html)**입니다. Amazon ECS가 주입하는 AWS 관리형 Envoy 사이드카, AWS Cloud Map을 통한 네임스페이스 기반 서비스 주소 지정, 태스크별 자동 서비스 디스커버리, 내장 트래픽 메트릭을 제공합니다. 메시 컨트롤 플레인을 직접 운영할 필요가 없으며, 애플리케이션은 친숙한 네임스페이스 이름으로 다른 서비스를 확인합니다. 단일 ECS 클러스터 내 신규 컨테이너 간 트래픽에는 이것이 AWS 네이티브 패턴입니다. [AWS Cloud Map을 통한 Amazon ECS 서비스 디스커버리](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html)은 이전 패턴입니다. 속성 필터 기반 디스커버리(소비자가 필터링하는 커스텀 속성을 노출하는 ECS 태스크 인스턴스)이나 Service Connect를 사용하지 않는 워크로드에는 여전히 유용하지만, 신규 클러스터 내 서비스 간 트래픽에는 Service Connect가 권장 경로입니다.

태스크의 ID는 **[Amazon ECS 태스크 역할](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html)**을 통해 관리됩니다. 각 태스크 정의는 AWS SDK가 요청 서명에 사용하는 IAM 역할을 참조합니다.

#### Amazon ECS 클러스터 내 네트워킹 모범 사례 {#amazon-ecs-in-cluster-best-practices}

* **Amazon ECS 태스크에는 `awsvpc` 네트워크 모드를 기본으로 사용하세요**. 태스크별 ENI를 통해 태스크별 SG ID, IP, 관측성을 무료로 얻을 수 있습니다.
* **클러스터 내 컨테이너 간 트래픽에는 Amazon ECS Service Connect를 사용하세요**. 네임스페이스 추상화, AWS 관리형 Envoy 사이드카, 트래픽 메트릭은 대부분의 팀이 메시를 통해 얻으려는 것을 대체합니다.
* **AWS Cloud Map 서비스 디스커버리는 속성 필터가 필요한 경우에만 사용하세요**. 단순한 경우는 Service Connect가 더 깔끔하게 처리합니다.
* **AWS API 접근을 위해 태스크별 IAM 역할을 할당하세요**. 태스크별 ID가 있어야 감사 및 액세스 로그 신호를 활용할 수 있습니다.

#### Amazon ECS 클러스터 내 네트워킹 문서 {#amazon-ecs-in-cluster-documentation}

<div class="grid cards" markdown>

*   :material-file-document: **Amazon ECS `awsvpc` 네트워크 모드**

    ---

    태스크별 ENI, 태스크별 IP, 태스크별 보안 그룹을 제공하는 Amazon ECS 권장 네트워크 모드.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking-awsvpc.html)

*   :material-file-document: **Amazon ECS Service Connect**

    ---

    클러스터 내 서비스 간 통신을 위한 AWS 관리형 Envoy 사이드카: 네임스페이스 주소 지정, 서비스 디스커버리, 트래픽 메트릭 제공.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html)

*   :material-file-document: **AWS Cloud Map을 통한 Amazon ECS 서비스 디스커버리**

    ---

    특정 워크로드에서 Service Connect를 보완하는 Amazon ECS 속성 필터 기반 서비스 디스커버리.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html)

*   :material-file-document: **Amazon ECS 태스크 IAM 역할**

    ---

    AWS SDK가 SigV4로 요청을 서명하는 데 사용하는 태스크별 IAM 역할.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html)

</div>

## 메시의 대안으로서의 Amazon VPC Lattice {#amazon-vpc-lattice-as-the-alternative-to-a-mesh}

[Amazon VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html)는 트래픽이 단일 클러스터를 벗어날 때 발생하는 메시 사용 사례의 일부를 흡수합니다. 구체적으로는 서비스 미러(service-mirror)나 클러스터 메시(cluster-mesh) 컨트롤 플레인 없이 클러스터 간 디스커버리, 서비스 또는 서비스 네트워크 수준의 IAM 기반 인증, 가중치 기반 라우팅, ID 인식 액세스 로그, 그리고 L3/L4 연결(피어링, AWS Transit Gateway, AWS Cloud WAN 불필요)을 제공합니다. 전체 서비스 처리에 대한 내용은 [Within AWS](../connectivity/within-aws.md) 페이지(연결 측면)와 [Service to Service](service-to-service.md) 페이지(애플리케이션 팀 측면)에서 다루며, 이 섹션에서는 컨테이너 특화 메커니즘을 설명합니다.

네이티브 Kubernetes 통합은 **[AWS Gateway API Controller](https://www.gateway-api-controller.eks.aws.dev/)**입니다. 이 컨트롤러는 클러스터 내의 Kubernetes Gateway API 리소스(`Gateway`, `HTTPRoute`, `GRPCRoute`, `TLSRoute`, `ServiceImport`, `ServiceExport`)를 감시하고, 이에 대응하는 Amazon VPC Lattice 서비스 네트워크 연결, 서비스, 대상 그룹, 리스너 규칙을 생성합니다. 애플리케이션 팀은 표준 방식인 Gateway API 리소스로 라우팅을 정의하고, 컨트롤러가 VPC Lattice 프로비저닝을 처리합니다.

Amazon ECS는 [Amazon VPC Lattice with Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/vpc-lattice.html) 통합을 통해 VPC Lattice에 연결됩니다. ECS 서비스 정의는 태스크를 VPC Lattice 대상 그룹 대상으로 직접 등록합니다. `awsvpc`의 태스크별 보안 그룹 모델이 그대로 적용됩니다.

멀티 클러스터 및 크로스 계정 환경에서는 AWS RAM을 통해 조직 전체에 Amazon VPC Lattice 서비스 네트워크를 공유합니다([Within AWS](../connectivity/within-aws.md) 페이지 참조). 각 클러스터는 해당 네트워크에 서비스를 내보내고, 다른 클러스터의 소비자는 Kubernetes `ServiceImport`(Amazon EKS)로 가져오거나, VPC Lattice 서비스 DNS 이름이 지원하는 Route 53 별칭을 호출합니다(Amazon ECS, 일반 클라이언트, 하이브리드 연결을 통해 접근하는 온프레미스 워크로드). 연결은 서비스에 번들로 포함되므로, 소비자 클러스터별로 피어링이나 AWS Transit Gateway 연결이 필요하지 않습니다.

솔직한 평가: **Amazon VPC Lattice가 도입된 이후에도 사이드카 메시가 여전히 필요한가?** Amazon VPC Lattice는 L7(HTTP 및 HTTPS)과 L4(SNI 기반 TLS 패스스루)에서 동작합니다. 메시 컨트롤 플레인이 관리하는 파드별 mTLS 라이프사이클, 메시 네이티브 트래픽 관리 CRD(`VirtualService`, `DestinationRule`, `ServiceProfile`), 또는 이상값 감지(outlier detection)나 서킷 브레이커(circuit-breaker) 정책과 같은 풍부한 클라이언트 측 로드 밸런싱 시맨틱을 데이터 플레인 구성으로 제공하지는 않습니다. 대부분의 워크로드에는 이러한 기능이 필요하지 않으며, 필요한 경우에는 아래의 자체 관리형 서비스 메시 방식이 적합한 답입니다.

### Amazon VPC Lattice 모범 사례 {#amazon-vpc-lattice-best-practices}

* **Amazon EKS에서 VPC Lattice를 위한 클러스터 내 계약으로 AWS Gateway API Controller를 사용하세요**. 애플리케이션 팀은 Kubernetes 표준인 `Gateway`와 `HTTPRoute`를 통해 라우팅을 정의하고, 컨트롤러가 내부적으로 Lattice 서비스 네트워크와 서비스 프로비저닝을 처리합니다.
* **VPC Lattice 서비스 앞에는 VPC Lattice 관리형 DNS 이름 대신 Route 53 별칭을 사용하세요**. 이 간접 계층이 향후 구현 변경 사항을 소비자에게 투명하게 만들어 줍니다.
* **Amazon ECS 전용 환경에서는 클러스터 간, VPC 간, 계정 간 연결에 VPC Lattice를 사용하고, 각 클러스터 내부에는 Service Connect를 사용하세요**. 두 가지는 깔끔하게 공존합니다. 로컬 컨테이너 간 통신에는 Service Connect를, 클러스터·VPC·계정 경계를 넘는 모든 통신에는 VPC Lattice를 사용합니다.
* **서비스 네트워크 공유 모델을 계정 구조에 맞게 설정하세요**. 조직 전체에 하나의 서비스 네트워크를 사용하는 것이 가장 단순하며, 워크로드 경계와 일치한다면 OU별 또는 환경별 네트워크로 장애 반경(blast radius)을 줄일 수 있습니다.
* **특정 사이드카 메시 기능이 실제로 필요한 경우에만 자체 관리형 서비스 메시를 선택하세요**. "모두가 메시를 사용한다"는 이유만으로는 충분하지 않습니다. 메시 CRD, 파드 내 mTLS 라이프사이클, 메시 네이티브 트래픽 관리 시맨틱이 실제 요구 사항이어야 합니다.

### Amazon VPC Lattice 문서 {#amazon-vpc-lattice-documentation}

<div class="grid cards" markdown>

*   :material-file-document: **Amazon VPC Lattice with Amazon EKS**

    ---

    Amazon VPC Lattice와 AWS Gateway API Controller를 통한 Amazon EKS 워크로드의 클러스터 간 연결.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/eks/latest/userguide/integration-vpc-lattice.html)

*   :material-file-document: **AWS Gateway API Controller**

    ---

    Amazon VPC Lattice 서비스 네트워크, 서비스, 대상 그룹, 규칙을 프로비저닝하는 Kubernetes Gateway API 구현체.

    [:octicons-arrow-right-24: 문서](https://www.gateway-api-controller.eks.aws.dev/)

*   :material-file-document: **Amazon VPC Lattice with Amazon ECS**

    ---

    Amazon ECS 서비스를 Amazon VPC Lattice 대상 그룹 대상으로 네이티브 연결.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/vpc-lattice.html)

*   :material-file-document: **Amazon VPC Lattice 서비스 네트워크와 AWS RAM 공유**

    ---

    멀티 계정, 멀티 클러스터 서비스 간 통신을 위한 서비스 네트워크의 크로스 계정 공유.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html)

*   :material-file-document: **Kubernetes Gateway API**

    ---

    Amazon VPC Lattice 및 AWS 로드 밸런서를 위해 AWS Gateway API Controller가 구현하는 Kubernetes 명세.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/eks/latest/best-practices/gateway-api-controller.html)

</div>

## AWS 네트워킹 위에서 실행되는 자체 관리형 서비스 메시 {#self-managed-service-mesh-on-top-of-aws-networking}

워크로드에 AWS가 제공하지 않는 사이드카 메시 기능(메시 관리형 mTLS 라이프사이클, 트래픽 정책을 위한 메시 CRD, 이미 프로덕션에서 운영 중인 멀티 클러스터 메시 패턴)이 실제로 필요한 경우, 메시는 AWS 네트워킹 위에서 실행됩니다. 운영 비용을 결정하는 핵심은 **메시 하단에서 클러스터 간 및 VPC 간 트래픽을 전달하는 AWS 서비스가 무엇인가**입니다. 메시의 프로토콜 집합이 호환되는 경우 Amazon VPC Lattice가 상당한 부하를 처리할 수 있으며, 호환되지 않는 경우에는 VPC 피어링, AWS Transit Gateway, AWS Cloud WAN이 대안이 됩니다.

### Amazon VPC Lattice 위에서 메시 실행 {#running-the-mesh-on-top-of-amazon-vpc-lattice}

메시 컨트롤 플레인과 데이터 플레인 사이드카는 클러스터 내부에서 실행되고, 클러스터 간 및 VPC 간 트래픽은 Amazon VPC Lattice를 통해 흐릅니다. 메시는 친숙한 DNS 이름(VPC Lattice 서비스 또는 리소스 구성 커스텀 도메인 이름에 대한 Route 53 별칭)을 인식하고 다른 클러스터를 업스트림으로 처리합니다. **이를 통해 절감되는 것**: 피어링, AWS Transit Gateway, AWS Cloud WAN, CIDR 조율, 크로스 VPC 보안 그룹 인가, 운영해야 할 공유 연결 구성 요소가 모두 불필요합니다.

동일한 VPC Lattice 네트워크는 서로 다른 VPC Lattice 구성 요소를 통해 다양한 메시 트래픽 형태를 처리합니다.

| 메시 트래픽 형태 | VPC Lattice 구성 요소 | 비고 |
| --- | --- | --- |
| HTTP / HTTPS / gRPC 애플리케이션 트래픽 | HTTPS 리스너가 있는 서비스 | VPC Lattice가 TLS를 종료하며, 메시 사이드카는 평문을 수신하거나 재암호화합니다. |
| 사이드카 간 mTLS | TLS 패스스루 리스너가 있는 서비스 | SNI 기반으로 라우팅하며, 사이드카가 mTLS를 종료합니다. 10분 연결 제한이 적용되므로 이 경로를 통한 장기 gRPC 컨트롤 플레인 스트림은 모니터링이 필요합니다. |
| TCP 전용 메시 트래픽 (xDS, ID, 클러스터 메시 컨트롤 플레인) | 리소스 게이트웨이를 통한 [리소스 구성](https://docs.aws.amazon.com/vpc-lattice/latest/ug/resource-configuration.html) | TCP, 구성 가능한 포트 범위, 커스텀 도메인 이름 지원. 10분 리스너 제한 및 리스너 수준 인증 정책 제한이 적용되지 않습니다. |
| UDP, 멀티 프로토콜, 근본적으로 비TCP 트래픽 | 피어링 / AWS Transit Gateway / AWS Cloud WAN으로 폴백 | 위 세 가지를 배치한 후 남은 잔여 트래픽입니다. 혼합 라우팅은 유효한 패턴입니다. |

### 다른 AWS 네트워킹 서비스 위에서 메시 실행 {#running-the-mesh-on-top-of-other-aws-networking-services}

Amazon VPC Lattice의 모델이 적합하지 않은 경우, 클러스터 간 트래픽은 **VPC 피어링, AWS Transit Gateway, 또는 AWS Cloud WAN**을 통해 흐릅니다. 이는 [Within AWS](../connectivity/within-aws.md) 페이지에서 다루는 연결 기본 요소이며, 메시는 다른 클러스터를 IP 도달 가능한 서브넷으로 처리하고 나머지를 담당합니다.

이 구성의 비용은 실질적입니다. 운영해야 할 완전한 L3 연결, 모든 참여 VPC에 걸친 CIDR 계획, 메시 트래픽 패턴을 위한 보안 그룹 및 라우팅 테이블, 그리고 연결 구성 요소 자체(피어링은 N개 클러스터로 확장이 어렵고, AWS Transit Gateway와 AWS Cloud WAN은 확장되지만 VPC당, 리전당 어태치먼트가 추가됨)가 필요합니다. 메시 팀과 네트워크 팀은 새 클러스터마다 조율해야 합니다.

CIDR 중복 문제는 Kubernetes 환경에서 가장 큰 어려움입니다. IPv4 모드의 Amazon VPC CNI는 클러스터의 VPC CIDR에서 파드 IP를 할당하므로, 멀티 클러스터 환경에서는 클러스터 간 파드 범위가 겹치는 경우가 많습니다. VPC 피어링, AWS Transit Gateway, AWS Cloud WAN은 모두 연결된 양측 간에 겹치지 않는 CIDR을 요구합니다. 표준 해결책은 각 클러스터의 파드 범위를 크로스 클러스터 경로에서만 사용되는 겹치지 않는 범위로 변환하는 **[프라이빗 NAT 게이트웨이](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#private-nat-gateway-overview)**입니다. 이 방법은 동작하지만, 프라이빗 NAT 게이트웨이당 시간당 + GB당 비용, 분산 추적 및 감사 로그에 영향을 주는 IP 재작성, 그리고 네트워크 팀이 운영해야 할 추가 구성 요소가 발생합니다. **Amazon VPC Lattice는 이 문제를 완전히 회피합니다**: 소비자 측에서 연결을 종료하고 제공자 측에서 재개시하므로 CIDR 중복이 보이지 않습니다. 신규 클러스터에 **Amazon VPC CNI의 IPv6 모드**를 채택하면 근본적으로 문제를 제거할 수 있습니다(모든 파드가 전역적으로 고유한 IPv6 주소를 갖게 됨).

자체 관리형 서비스 메시 형태의 두 가지 변형 모두에서 AWS로부터 여전히 제공받는 것:

* **클러스터 외부에서 메시로의 인그레스**는 AWS Load Balancer Controller가 생성하는 ALB 또는 NLB를 통해 실행됩니다([로드 밸런싱](load-balancing.md) 페이지에서 다룸). 로드 밸런서는 메시 인그레스 게이트웨이(Istio Gateway, Linkerd 인그레스 등)에 도달하며, 메시가 그 이후의 라우팅을 처리합니다.
* **AWS 서비스로의 이그레스**는 [VPC 엔드포인트](https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html)(인터페이스 및 게이트웨이)를 통해 실행됩니다. 메시 이그레스 게이트웨이 또는 파드가 직접 엔드포인트를 통해 Amazon S3, Amazon DynamoDB, Amazon SQS, Amazon Kinesis 및 기타 AWS 서비스에 접근합니다.
* **메시의 텔레메트리**는 [AWS Distro for OpenTelemetry](https://aws-otel.github.io/)를 통해 Amazon CloudWatch Application Signals, AWS X-Ray, Amazon Managed Service for Prometheus / Amazon Managed Grafana로 흐르며, AWS 관리 경계에서의 Amazon VPC Lattice 액세스 로그 및 ALB 액세스 로그와 함께 수집됩니다.

멀티 클러스터 메시 패턴(Istio 멀티 프라이머리, Cilium Cluster Mesh 등)은 메시 컨트롤 플레인 내부에 존재하며, AWS 네트워킹 관점에서는 위의 두 가지 변형 중 하나로 전달되어야 하는 추가적인 클러스터 간 트래픽일 뿐입니다.

### 자체 관리형 메시 모범 사례 {#self-managed-mesh-best-practices}

* **자체 관리형 메시를 실행하기로 결정했다면, 기본적으로 Amazon VPC Lattice 위에서 실행하세요**. 각 메시 트래픽 형태를 적절한 VPC Lattice 구성 요소에 매핑하세요(위 표 참조): HTTP / HTTPS / gRPC 애플리케이션 트래픽에는 HTTPS 리스너, 사이드카 mTLS에는 TLS 패스스루, TCP 전용 메시 트래픽에는 리소스 구성. 장기 gRPC 컨트롤 플레인 스트림에 대한 TLS 패스스루 리스너의 10분 연결 제한을 모니터링하세요. 리소스 구성에는 이 제한이 없습니다.
* **피어링, AWS Transit Gateway, 또는 AWS Cloud WAN을 메시 하단에 사용하는 것은** VPC Lattice가 커버하지 않는 잔여 트래픽(UDP, 멀티 프로토콜)이나 기존 연결 구성 요소가 이미 워크로드를 지원하는 경우에만 폴백으로 사용하세요.
* **메시로의 인그레스에는 AWS Load Balancer Controller를 사용하세요**. AWS 관리형 로드 밸런서를 사용할 수 있는 경우 메시 CRD에서 인그레스를 재구현하지 마세요.
* **AWS 서비스로의 메시 이그레스에는 VPC 엔드포인트를 사용하세요**. 공용 인터넷이 아닌 인터페이스 또는 게이트웨이 엔드포인트를 통해 Amazon S3, Amazon DynamoDB, Amazon SQS 등에 접근하세요.
* **AWS API 접근을 위한 IAM은 Pod Identity, IRSA, 또는 태스크 역할에 유지하세요**. 메시 발급 인증서에 의존하지 마세요. 메시는 클러스터 내 서비스 ID를 처리하고, AWS는 AWS 서비스 ID를 처리합니다.

### 자체 관리형 메시 문서 {#self-managed-mesh-documentation}

<div class="grid cards" markdown>

*   :material-file-document: **AWS Load Balancer Controller**

    ---

    ALB 및 NLB를 프로비저닝하는 Kubernetes 컨트롤러로, 메시 인그레스 게이트웨이로의 AWS 네이티브 인그레스입니다.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html)

*   :material-file-document: **AWS PrivateLink 및 VPC 엔드포인트**

    ---

    공용 인터넷을 경유하지 않고 클러스터 워크로드에서 AWS 서비스로의 메시 이그레스를 위한 프라이빗 연결입니다.

    [:octicons-arrow-right-24: 문서](https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html)

*   :material-file-document: **AWS Distro for OpenTelemetry**

    ---

    메시 텔레메트리를 Amazon CloudWatch, AWS X-Ray, Amazon Managed Service for Prometheus로 전송하기 위한 AWS 지원 OpenTelemetry 배포판입니다.

    [:octicons-arrow-right-24: 문서](https://aws-otel.github.io/)

</div>

## 컨테이너 메시 스택 구성 {#building-your-container-mesh-stack}

컨테이너 메시 아키텍처는 연결성([Within AWS](../connectivity/within-aws.md) 페이지에서 다룸)과 워크로드의 애플리케이션 로직 사이에 위치하는 계층입니다. 위에서 설명한 세 가지 형태는 상호 배타적이지 않습니다. 대부분의 환경에서는 각 클러스터 내부에 인클러스터(in-cluster) 컨테이너 네트워킹을 적용하고, 클러스터 간에는 Amazon VPC Lattice를 활용하며, 사이드카 메시가 실제로 필요한 워크로드에 한해서만 자체 관리형 서비스 메시를 도입합니다.

![세 계층으로 구성된 컨테이너 메시 스택: 인클러스터(EKS 및 ECS 기본 요소), VPC Lattice를 통한 크로스 클러스터(서비스 네트워크, Gateway API Controller, Route 53), 자체 관리형 메시(Lattice 리스너, 리소스 구성, 연결 폴백)](../assets/application-networking/container-mesh-stack.png)
/// caption
컨테이너 메시 스택 — [Drawio 소스](../assets/application-networking/container-mesh-stack.drawio)
///

### 신규 환경 {#new-environments}

컨테이너 서비스 간 통신을 처음부터 구축하는 조직은 첫날부터 일관된 스택으로 시작할 수 있습니다.

1. **각 클러스터 내부에서는 AWS 네이티브 기본 요소를 활용하세요**. EKS 측에서는 Amazon VPC CNI(신규 클러스터에는 IPv6 모드를 사용하면 IPv4 고갈 및 CIDR 중복 문제를 근본적으로 해결할 수 있음), Amazon EKS Pod Identity, 파드용 보안 그룹, Kubernetes NetworkPolicy를 사용합니다. ECS 측에서는 `awsvpc` 모드, Amazon ECS Service Connect, 태스크별 IAM 역할을 사용합니다. 이 인클러스터 컨테이너 네트워킹 형태는 단일 클러스터 내에서 팀이 메시를 통해 얻고자 하는 대부분의 요구사항을 충족합니다.
2. **클러스터, VPC, 계정 경계를 넘는 모든 통신에는 Amazon VPC Lattice를 사용하세요**. Amazon EKS에서는 AWS Gateway API Controller를, Amazon ECS에서는 네이티브 Lattice 연결을 활용합니다. AWS RAM을 통해 OU 수준에서 공유되는 단일 서비스 네트워크를 구성하면 새로운 클러스터와 계정이 자동으로 연결 범위를 상속받습니다. 이를 통해 크로스 클러스터 연결 문제를 메시 결정에서 분리할 수 있습니다.
3. **Amazon Route 53 Profiles로 배포되는 Route 53 별칭으로 Lattice 서비스를 앞단에 배치하세요**. [서비스 간 통신](service-to-service.md) 페이지와 동일한 패턴으로, 구현 방식이 변경되더라도 소비자가 바라보는 이름은 안정적으로 유지됩니다.
4. **특정 사이드카 메시 요구사항이 비용을 정당화할 때만 자체 관리형 메시를 도입하세요**. 그 시점이 오면 위의 프로토콜 적합성 표(HTTPS 리스너 / TLS 패스스루 / 리소스 구성)를 참고하여 VPC Lattice 위에서 메시를 운영하는 것을 기본으로 삼고, 나머지 잔여 트래픽에 한해 피어링 / AWS Transit Gateway / AWS Cloud WAN을 예비로 활용하세요.
5. **첫날부터 관측성을 중앙화하세요**: AWS 관리형 경계에서는 Amazon VPC Lattice 액세스 로그(ID 인식), 로드 밸런서가 경로에 있는 경우 ALB 및 NLB 액세스 로그를 수집하고, AWS Distro for OpenTelemetry를 통해 메시 및 애플리케이션 텔레메트리를 Amazon CloudWatch Application Signals, AWS X-Ray, Amazon Managed Service for Prometheus로 전송합니다.

### 기존 환경 {#existing-environments}

기존 컨테이너 서비스 간 통신 패턴을 운영 중인 조직은 모든 것을 한꺼번에 변경할 필요가 없습니다.

1. **기존 인클러스터 패턴은 그대로 유지하세요**. AWS Cloud Map을 통한 Amazon ECS 서비스 디스커버리, Amazon EKS의 IRSA, 현재 운영 중인 인클러스터 메시는 계속 동작합니다. 고정된 일정이 아닌, 호출 코드를 수정하는 시점에 워크로드별로 마이그레이션하세요.
2. **새로운 크로스 클러스터 요구사항에는 먼저 Amazon VPC Lattice를 추가하세요**. 클러스터, VPC, 계정 경계를 넘는 새로운 서비스 간 트래픽은 기존 피어링이나 AWS Transit Gateway 기반 메시를 확장하는 대신, AWS Gateway API Controller(EKS) 또는 Amazon ECS와 함께 Amazon VPC Lattice를 사용해야 합니다. L3 경로에서 발생하는 CIDR 중복 문제와 프라이빗 NAT 게이트웨이 비용 부담이 사라집니다.
3. **기존 자체 관리형 메시의 경우, 기회가 될 때마다 Amazon VPC Lattice를 하위 계층에 추가하세요**. 메시를 업그레이드하거나, 새 클러스터가 합류하거나, 연결 계층을 재설계할 때 클러스터 간 애플리케이션 트래픽을 VPC Lattice 리스너로, TCP 컨트롤 플레인 트래픽을 리소스 구성으로 이전하세요. 잔여 트래픽(UDP, 멀티 프로토콜)만 피어링 / AWS Transit Gateway / AWS Cloud WAN에 남겨두세요. 모든 것을 한꺼번에 마이그레이션하기 위해 정상 동작하는 메시를 제거하지 마세요.
4. **기존 내부 로드 밸런서는 수정하는 시점에 Route 53 별칭으로 앞단을 구성하세요**. 애플리케이션 코드에 하드코딩된 ALB / NLB DNS 이름과 직접 사용하는 Lattice 관리형 DNS 이름은 모두 소비자를 공급자의 특정 인스턴스에 종속시킵니다. Route 53 별칭 간접 참조를 통해 향후 구현 변경 사항을 소비자에게 투명하게 처리할 수 있습니다.
