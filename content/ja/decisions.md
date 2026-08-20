# ネットワーキング決定マップ {#networking-decision-map}

このページでは、一般的な AWS ネットワーキングに関する疑問を、適切なサービス・パターン・本ガイドのページへと対応付けています。達成したいことは明確だが、どの AWS サービスやアーキテクチャパターンが適切かわからない場合にご活用ください。

## VPC とアカウントの接続 {#connecting-vpcs-and-accounts}

| やりたいこと | 推奨サービス | 主なトレードオフ | 詳細 |
| --- | --- | --- | --- |
| 複数リージョンにまたがる多数の VPC を集中ポリシーで接続する | **AWS Cloud WAN** — 宣言型ネットワークポリシー、アタッチメントの自動受け入れ、セグメントベースの分離、グローバルダイナミックルーティング | TGW よりアタッチメントあたりのコストは高いが、ポリシー駆動の管理によりリージョンごとの手動設定が不要 | [AWS 内の接続性](connectivity/within-aws.md) |
| 単一リージョン内の VPC をハブ経由で接続する | **AWS Transit Gateway** — 数千のアタッチメントに対応するリージョンハブ、ルートテーブルによるセグメンテーション | 単一リージョンでは Cloud WAN より簡単だが、複数リージョンにまたがると管理が複雑になる | [AWS 内の接続性](connectivity/within-aws.md) |
| 2 つの VPC を高スループット・同一 AZ のデータ処理/転送コストゼロで接続する | **VPC Peering** — 最低レイテンシー、帯域制限なし、同一 AZ トラフィックの GB あたり課金なし、非推移的 | 少数のペアを超えるとスケールしない。CIDR の重複不可 | [AWS 内の接続性](connectivity/within-aws.md) |
| HTTP/gRPC サービスを他の VPC やアカウントに公開する | **VPC Lattice Services** — ピアリングや TGW 不要のクロス VPC 接続、IAM 認証ポリシー、重み付きルーティング、CIDR 重複対応 | L7 のみ対応 (HTTP/HTTPS/gRPC) | [AWS 内の接続性](connectivity/within-aws.md) |
| 別アカウントにデータベースやオンプレミスエンドポイントへのプライベート TCP アクセスを提供する | **VPC Lattice VPC Resources** — カスタムドメイン名と DNS をターゲットとするリソース設定 (NLB 不要)、CIDR 重複対応、ポート範囲の公開 | 単方向のみ (コンシューマー → リソース)。TCP のみ | [AWS 内の接続性](connectivity/within-aws.md) |
| NLB の背後にある TCP サービスをコンシューマー VPC に公開する | **AWS PrivateLink エンドポイントサービス** — NLB バックエンド、コンシューマーごとのインターフェイスエンドポイント、ENI ベース | コンシューマー数に比例してスケール (コンシューマー VPC ごとに 1 エンドポイント)。認証ポリシーなし | [AWS 内の接続性](connectivity/within-aws.md) |

## インターネットへの接続 {#reaching-the-internet}

| やりたいこと | 推奨パターン | 主なトレードオフ | 詳細 |
| --- | --- | --- | --- |
| プライベート IPv4 リソースからインターネットへの通信を許可する | **NAT ゲートウェイ** — ゾーンまたはリージョン単位、高可用性で自動スケール | 集約しない場合はデータ処理コストと時間単位のコストが発生 | [インターネット接続性](connectivity/internet.md) |
| プライベート IPv6 リソースからインターネットへの通信を許可する | **Egress-only インターネットゲートウェイ** — データ処理コストなし (データ転送コストは適用)、VPC ごと、アウトバウンドのみ | 集約不可。NAT66/NPTv6 非対応 | [インターネット接続性](connectivity/internet.md) |
| HTTP/HTTPS アプリケーションをインターネットに公開する | **CloudFront + AWS WAF + ALB** (分散型イングレス) — エッジキャッシング、L7 保護、プライベートバックエンド向け VPC Origins | 共有 VPC を経由した集中型イングレスはロードバランサーの連鎖と影響範囲の拡大を招く。コンプライアンス要件がない限り避けること | [インターネット接続性](connectivity/internet.md) |
| TCP/UDP サービスをインターネットに公開する | **NLB** インターネット向け、VPC ごと、クライアント IP の保持が可能 | セキュリティグループや次世代ファイアウォールと組み合わせて追加のセキュリティを確保 | [インターネット接続性](connectivity/internet.md) |
| AWS サービスへのトラフィックにかかる NAT ゲートウェイのコストを削減する | **VPC エンドポイント** — S3/DynamoDB 向けゲートウェイエンドポイント (無料)、その他サービス向けインターフェイスエンドポイント | インターフェイスエンドポイントには時間単位とデータ処理の料金が発生 | [インターネット接続性](connectivity/internet.md) |

## オンプレミスおよび他クラウドへの接続 {#connecting-to-on-premises-and-other-clouds}

| やりたいこと | 推奨サービス | 主なトレードオフ | 詳細 |
| --- | --- | --- | --- |
| オンプレミスへのプライベートで予測可能な帯域幅を確保する | **AWS Direct Connect** — 1/10/100/400 Gbps の専用回線、パートナーホスト型回線 50 Mbps〜10 Gbps。インターネットより低い送信料金 | 専用ポートは最大 72 時間で準備完了だが、プロビジョニングにはクロスコネクトまたはプロバイダー/パートナーとの調整が必要。最大限の冗長性を設計すること (2 接続以上、2 拠点以上) | [ハイブリッド & マルチクラウド](connectivity/hybrid-multicloud.md) |
| 待ち時間なしでオンプレミスへの暗号化接続を確立する | **AWS Site-to-Site VPN** — インターネット経由の IPsec、数分で起動、Large トンネルあたり最大 5 Gbps | インターネットベースのためレイテンシーとスループットが不安定。本番ハイブリッド環境での Direct Connect の代替にはならない | [ハイブリッド & マルチクラウド](connectivity/hybrid-multicloud.md) |
| AWS と Google Cloud をプライベートに接続する | **AWS Interconnect** — マネージドなクラウド間直接接続、MACsec 暗号化、数分でプロビジョニング | 現在は AWS ↔ Google Cloud のみ対応。拡張予定。未対応の組み合わせにはパートナーベースの Direct Connect を使用 | [ハイブリッド & マルチクラウド](connectivity/hybrid-multicloud.md) |
| 既存の SD-WAN を AWS と統合する | **Transit Gateway Connect または Cloud WAN Tunnel-less Connect** — BGP を使用した GRE/Tunnel-less アタッチメント | トランジット VPC 内 (または TGW Connect 向けに DX アンダーレイを使用したオンプレミス) に SD-WAN 仮想アプライアンスが必要 | [ハイブリッド & マルチクラウド](connectivity/hybrid-multicloud.md) |
| リモートユーザーにアプリケーションへのアクセスを提供する | **AWS Verified Access** (推奨) — ゼロトラスト、リクエストごとの ID + デバイスポスチャー評価、VPN クライアント不要 | アプリケーションがネットワーク層の IP 到達性 (SSH、RDP、レガシープロトコル) を真に必要とする場合のみ Client VPN を使用 | [リモートアクセス](connectivity/remote-access.md) |

## ネットワークトラフィックのセキュリティ確保 {#securing-network-traffic}

| やりたいこと | 推奨サービス | 主なトレードオフ | 詳細 |
| --- | --- | --- | --- |
| ネットワーク層でどのリソースが通信できるかを制御する | **セキュリティグループ** — ステートフル、ENI ごと、参照ベースのルール。すべてのワークロードの主要なアクセス制御 | 拒否不可 (許可のみ)。サブネットレベルでの明示的な拒否には NACL を使用 | [境界コントロール](security/perimeter-inbound.md) |
| L7 攻撃から Web アプリケーションを保護する | CloudFront または ALB 上の **AWS WAF** — マネージドルールグループ、レート制限、ボット制御、ジオブロッキング | AWS WAF は HTTP のみ。HTTP 以外のインスペクションには Network Firewall を使用 | [境界コントロール](security/perimeter-inbound.md) |
| インターネットエグレスや VPC 間を含む VPC 境界でのトラフィックを検査する (L3〜L7) | **AWS Network Firewall** — マネージドなステートフル/ステートレスインスペクション、Suricata IPS ルール、ドメインフィルタリング | コストに注意 — エンドポイント時間単位 + GB あたりの処理料金 | [境界コントロール](security/perimeter-inbound.md) |
| サードパーティのファイアウォールアプライアンスを挿入する | **Gateway Load Balancer** — GENEVE カプセル化を使用したサードパーティファイアウォールアプライアンスへのセッションアフィニティ維持、透過的な挿入、元のヘッダーを保持 | アプライアンスフリート (パッチ適用、スケーリング、ライセンス) は自己管理。Network Firewall より運用コストが高い。一部ベンダーは完全マネージドな GWLB ベースのソリューションを提供 | [境界コントロール](security/perimeter-inbound.md) |
| ワークロードが未承認ドメインに到達するのをブロックする | **Route 53 DNS Firewall** — DNS 解決時のドメインベースフィルタリング、100 万クエリあたり数セント以下 | ハードコードされた IP や DNS-over-HTTPS では回避される。完全なカバレッジには Network Firewall と組み合わせること | [アウトバウンドコントロール](security/outbound.md) |
| 未承認の S3 バケットへのデータ流出を防ぐ | S3 ゲートウェイエンドポイントの **VPC エンドポイントポリシー** — 自組織のバケットのみに制限 | エンドポイント経由の S3 トラフィックのみ対象。他の流出経路はカバーしない | [アウトバウンドコントロール](security/outbound.md) |
| 最強レベルでワークロードを分離する | **AWS アカウントの分離** — 独立した IAM、ネットワーク、請求の境界。無料、ネットワーク設定不要 | アカウント間の接続には明示的な接続設定が必要 (Transit Gateway、Cloud WAN、VPC Lattice) | [ネットワークセグメンテーション](security/segmentation.md) |
| マイクロサービス間に ID ベースのアクセスを適用する | **VPC Lattice 認証ポリシー** — IAM SigV4 署名、リクエストごとの評価、ネットワーク位置に依存しない | コンシューマーは SigV4 でリクエストに署名する必要がある。署名の導入中は VPC/パスベースの条件から始めることも可能 | [ネットワークセグメンテーション](security/segmentation.md) |

## モニタリングとトラブルシューティング {#monitoring-and-troubleshooting}

| やりたいこと | 推奨サービス | 主なトレードオフ | 詳細 |
| --- | --- | --- | --- |
| VPC 内のトラフィックフローを確認する | **VPC Flow Logs** — VPC レベルで有効化、40 以上のフィールドを持つカスタム形式、コスト効率の高い Athena クエリのために S3 に配信 | S3 配信: 最もコスト効率が高い。CloudWatch Logs: より高コストだがリアルタイムアラートが可能 | [内部トラフィック](observability/internal-traffic.md) |
| 組織内のすべてのクロス VPC トラフィックを確認する | **Transit Gateway Flow Logs** — ネットワークアカウントでの単一設定ですべてのクロス VPC トラフィックをカバー | TGW を通過するトラフィックのみキャプチャ。VPC 内トラフィックには VPC ごとの Flow Logs が必要 | [内部トラフィック](observability/internal-traffic.md) |
| ロードバランサーの健全性とパフォーマンスを監視する | **CloudWatch メトリクス** — HealthyHostCount、TargetResponseTime、HTTPCode_ELB_5XX、RejectedConnectionCount | メトリクスは集計値。リクエストごとの調査には ALB/NLB アクセスログを使用 | [AWS サービスのモニタリング](observability/service-monitoring.md) |
| VPN トンネルや DX 接続がダウンした際にアラートを受け取る | 状態変化イベント向けの **EventBridge ルール** + TunnelState/ConnectionState の **CloudWatch アラーム** | 両方のトンネルダウン (障害) だけでなく、単一トンネルダウン (冗長性喪失) でもアラームを設定すること | [通知](observability/notifications.md) |
| エグレスコストと宛先を把握する | **AWS Cost and Usage Reports** (リソースごとのデータ転送明細) + **CloudWatch メトリクス** (BytesOutToDestination、ActiveConnectionCount) + **VPC Flow Logs** (宛先 IP、フローごとのバイト数) | CUR はコスト帰属を示すが遅延がある。Flow Logs はリアルタイムの宛先詳細を提供するがコストデータはない — 全体像の把握には両方を組み合わせること | [外部トラフィック](observability/external-traffic.md) |
| EC2 インスタンスと AWS サービス間のリアルタイムのパケットロスとレイテンシーを測定する | **Network Flow Monitor** — インスタンス上の軽量エージェントが TCP パフォーマンス統計を報告。ダッシュボードにフローごとのパケットロス、レイテンシー、帰属情報を表示 | 各インスタンスへのエージェントインストールが必要。TCP ベースのフローのみ対応 | [AWS サービスのモニタリング](observability/service-monitoring.md) |
| インターネット向けアプリケーションのインターネットパフォーマンスと可用性を監視する | **Internet Monitor** — AWS グローバルネットワークデータを使用してパフォーマンスをベースライン化。ヘルスイベントを表示し、CloudFront や代替リージョン経由のルーティング改善を提案 | AWS が観測可能なトラフィックパスに限定。オンプレミスはカバーしない | [AWS サービスのモニタリング](observability/service-monitoring.md) |
| オンプレミス宛先へのハイブリッド接続のレイテンシーとパケットロスを追跡する | **Network Synthetic Monitor** — AWS リソースからオンプレミス IP への完全マネージドプローブ。エージェントインストール不要。設定可能なしきい値によるヘルスイベントアラート | AWS からオンプレミス方向のみ測定。宛先 IP がプローブソースから到達可能である必要がある | [AWS サービスのモニタリング](observability/service-monitoring.md) |

## ロードバランサーの選択 {#choosing-a-load-balancer}

| トラフィックタイプ | 使用するもの | 使用しないもの | 理由 |
| --- | --- | --- | --- |
| HTTP、HTTPS、gRPC | **ALB** | NLB (処理は可能だがアプリ層の可視性がない) | ALB はコンテンツベースルーティング、TLS 終端、AWS WAF 統合、mTLS、Automatic Target Weights を提供 |
| TCP、UDP、TLS、QUIC (非 HTTP) | **NLB** | ALB | NLB は HTTP デコードなしで転送。クライアント IP を保持。アベイラビリティーゾーンごとに静的 IP を提供 |
| 静的 IP と HTTP ルーティングの両方が必要 | **NLB + ALB をターゲットとして使用** | ALB 単独 | NLB が静的 IP を提供し、その背後で ALB が L7 ルーティングを担当 |
| サードパーティのファイアウォール挿入 | **GWLB** | Network Firewall | GWLB は自己管理のアプライアンスフリート向け。Network Firewall は AWS マネージドの代替 |
| VPC をまたいだサービス間通信 | **VPC Lattice** | ALB + PrivateLink | VPC Lattice はロードバランサーを管理することなく、クロス VPC 到達性、認証、重み付きルーティング、アクセスログをバンドルで提供 |
