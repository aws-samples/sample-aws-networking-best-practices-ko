# DNS アーキテクチャ {#dns-architecture}

!!! info "前提条件"
    このセクションは、[Amazon VPC](vpc.md)、[AWS Organizations](organizations.md)、および [CIDR 計画](cidr.md)に関する知識を前提としています。AWS ネットワーキングの基礎を初めて学ぶ方は、先にそれらのページをご確認ください。

Amazon Route 53 Resolver は、VPC 内から発生するすべての DNS クエリを処理します。プライベートホストゾーンへのクエリへの応答、ハイブリッド接続を経由したオンプレミスドメインへのクエリの転送、パブリックインターネット名の解決を、DNS インフラストラクチャを一切デプロイすることなく実現します。マルチアカウントの AWS 環境では、DNS の設計判断がサービスディスカバリ、ハイブリッド接続、セキュリティ体制に連鎖的な影響を与えます。転送ルールの設定ミスはアカウント全体の名前解決をサイレントに破壊し、共有されていないプライベートホストゾーンは他の VPC のコンシューマーからサービスを不可視にし、DNS Firewall が存在しなければすべてのワークロードがインターネット上の任意のドメインを解決(そして到達)できる状態になります。

AWS における DNS は、一体として設計しなければならない 3 つのレイヤーで動作します。**解決(Resolution)**(クエリへの応答方法)、**共有(Sharing)**(DNS 設定をすべてのアカウントに届ける方法)、**セキュリティ(Security)**(DNS をアウトバウンドトラフィックの制御点として活用する方法)です。Route 53 Resolver が解決エンジンとして機能し、Route 53 Profiles が設定をスケールで配布し、Route 53 Resolver DNS Firewall が DNS レイヤーでドメインベースのフィルタリングを適用します。

## 主要機能 {#key-capabilities}

<div class="grid cards" markdown>

*   :material-dns: **Route 53 Resolver**

    ---

    すべての VPC に標準搭載されている再帰リゾルバーです。プライベートホストゾーンへのクエリへの応答、Resolver エンドポイントを経由したオンプレミスドメインへのクエリの転送、パブリック DNS の解決をすべて自動的に行います。

*   :material-share-variant: **Route 53 Profiles**

    ---

    プライベートホストゾーンの関連付け、Resolver 転送ルール、DNS Firewall ルールグループを OU レベルでアカウント全体に配布します。新しいアカウントは DNS 設定を自動的に継承します。

*   :material-lock: **プライベートホストゾーン**

    ---

    関連付けられた VPC にのみ表示される DNS 名前空間です。内部サービス名、スプリットホライズン DNS(内部クエリと外部クエリで異なる応答を返す仕組み)、VPC Lattice および PrivateLink エンドポイントのカスタムドメイン名に使用します。

*   :material-arrow-right-bold: **Resolver エンドポイント**

    ---

    インバウンドエンドポイントにより、オンプレミスの DNS サーバーが AWS のプライベートホストゾーンを解決できます。アウトバウンドエンドポイントにより、VPC のワークロードがオンプレミスの DNS サーバーへ転送することでオンプレミスドメインを解決できます。

*   :material-shield-lock: **DNS Firewall**

    ---

    DNS 解決レイヤーでのドメインベースフィルタリングです。ワークロードが接続を試みる前に、特定ドメインへのクエリをブロック、許可、またはアラートとして処理します。利用可能なエグレス制御の中で最もコストが低く、最も広範な制御手段です。

*   :material-ip-network: **デュアルスタックサポート**

    ---

    Resolver エンドポイント、転送ルール、DNS Firewall はすべて IPv4 と IPv6 の両方をサポートします。プライベートホストゾーンの AAAA レコードは、デュアルスタックワークロード向けに A レコードと並行して機能します。

</div>

## ベストプラクティス {#best-practices}

### 解決アーキテクチャ {#resolution-architecture}

#### すべての VPC の唯一の DNS リゾルバーとして Route 53 Resolver を使用する {#use-route-53-resolver-as-the-sole-dns-resolver-for-all-vpcs}

すべての VPC には、VPC+2 アドレスに Route 53 Resolver が自動的に配置されます。VPC ワークロードのプライマリリゾルバーとして、カスタム DNS サーバー(BIND、Active Directory DNS、Kubernetes 外の CoreDNS)をデプロイしないでください。カスタムリゾルバーは運用負荷(パッチ適用、スケーリング、モニタリング)を増加させ、Route 53 Resolver には存在しない単一障害点を生み出し、Route 53 の機能(DNS Firewall、クエリログ、Resolver ルール)を迂回させます。唯一正当な例外は、ドメイン参加の解決に AD DNS を必要とする Active Directory 参加済みの Windows ワークロードです。それでも、AD 以外のクエリは Route 53 Resolver に転送すべきです。

#### ハイブリッド DNS 解決のための転送ルールを設計する {#design-forwarding-rules-for-hybrid-dns-resolution}

AWS 内のワークロードがオンプレミスのドメイン名(例: `corp.example.com`)を解決する必要がある場合、Resolver アウトバウンドエンドポイントと転送ルールを作成し、Direct Connect または VPN 経由でオンプレミスの DNS サーバーにクエリを送信します。逆に、オンプレミスのワークロードが AWS プライベートホストゾーン名を解決する必要がある場合は、オンプレミスの DNS サーバーが転送先として使用できる Resolver インバウンドエンドポイントを作成します。

転送ルールはできる限り具体的に設計してください。ルート(`.`)ではなく、`corp.example.com` をオンプレミスに転送します。ワイルドカードの転送ルールはすべての DNS トラフィックをオンプレミスに送信するため、すべてのクエリにレイテンシーが加わり、すべての DNS 解決がハイブリッド接続に依存することになり、転送されたクエリに対して DNS Firewall が迂回されます。

#### 複数のアベイラビリティーゾーンに Resolver エンドポイントをデプロイする {#deploy-resolver-endpoints-across-multiple-availability-zones}

Resolver のインバウンドおよびアウトバウンドエンドポイントは、指定したサブネットに ENI を作成します。各エンドポイントに対して、少なくとも 2 つのアベイラビリティーゾーンにまたがる 2 つ以上の ENI をデプロイしてください。単一 AZ のエンドポイントは、それに依存するすべての DNS 解決の単一障害点となります。ハイブリッド環境では、そのアベイラビリティーゾーンに問題が発生した場合、すべてのクロスバウンダリーの名前解決が失敗することを意味します。

***重要なポイント:*** *DNS はあらゆるネットワークにおいて最も障害に敏感な依存関係です。30 秒間の DNS 解決の失敗は、アウトバウンド呼び出しを行うすべてのサービスにわたってカスケードタイムアウトを引き起こします。DNS インフラストラクチャは、最も重要なワークロードと同等の可用性基準で設計してください。*

### マルチアカウント DNS 共有 {#multi-account-dns-sharing}

#### マルチアカウントの DNS 配布には Route 53 Profiles を使用する {#use-route-53-profiles-for-multi-account-dns-distribution}

Route 53 Profiles を使用すると、プライベートホストゾーンの関連付け、Resolver 転送ルール、DNS Firewall ルールグループを 1 つのプロファイルにまとめ、AWS RAM を通じて OU レベルで共有できます。OU に追加された新しいアカウントは、カスタムオートメーション、クロスアカウントの Lambda 関数、手動の関連付け手順なしに、完全な DNS 設定を自動的に継承します。

Profiles を使用しない場合、アカウント間で DNS 設定を共有するには、アカウントごとのプライベートホストゾーン関連付け(ホストゾーンごと・VPC ごとに 1 回の API 呼び出し)、アカウントごとの転送ルール共有、アカウントごとの DNS Firewall 関連付けが必要です。そのようなオートメーションは脆弱で監査が困難です。Profiles はそれをファーストクラスの操作に置き換えます。

#### プライベートホストゾーンの所有権をネットワーキングアカウントに集約する {#centralize-private-hosted-zone-ownership-in-the-networking-account}

プライベートホストゾーンは、集中管理されたネットワーキングアカウントで作成・管理してください。Route 53 Profiles を通じてコンシューマーアカウントに共有します。これにより、ネットワーキングチームが権威ある DNS 名前空間を管理しながら、アプリケーションチームが適切な場合に委任されたサブゾーンにレコードを作成できます。

代替案として各アカウントが独自のプライベートホストゾーンを作成する方法は、名前空間を断片化し、ゾーンが重複した際に解決の競合を生み出し、DNS Firewall とクエリログを一貫して実装することを困難にします。

#### 内部名前空間の階層を意図的に設計する {#design-your-internal-namespace-hierarchy-deliberately}

単一の内部ドメイン(例: `internal.example.com`)を選択し、環境、リージョン、またはサービスドメインごとにサブゾーンを作成します。適切に設計された階層は DNS レコードを自己文書化し、ルートベースの解決ポリシーを可能にします。

```
internal.example.com           (root, networking account)
├── prod.internal.example.com  (production services)
├── dev.internal.example.com   (development services)
└── hybrid.internal.example.com (on-premises forwarding)
```

数百のレコードが単一ゾーンに集中するフラットな名前空間は避けてください。長くて読みにくい FQDN を生み出す過度に深い階層も避けてください。ルートから 2〜3 レベルが最適です。

### DNS セキュリティ {#dns-security}

#### すべての VPC に DNS Firewall をデプロイする {#deploy-dns-firewall-in-every-vpc}

Route 53 Resolver DNS Firewall は、AWS で利用可能なエグレス制御の中で最もコストが低く、最も広範な手段です。VPC から発生するすべての DNS クエリをドメインリスト(AWS が提供するマネージド脅威インテリジェンスリスト、または独自のカスタムリスト)と照合して評価し、ブロック、許可、またはアラートを実行できます。実質的にすべてのアウトバウンド接続は DNS ルックアップから始まるため、悪意のあるドメインの解決をブロックすることで、接続の試みそのものを防止できます。

Route 53 Profiles を通じて DNS Firewall ルールグループをデプロイし、組織内のすべての VPC が同じベースライン保護を受けられるようにしてください。DNS を迂回するトラフィック(ハードコードされた IP、DNS-over-HTTPS)に対しては、Network Firewall またはサードパーティの検査と組み合わせてください。

DNS Firewall のベストプラクティスと他のエグレス制御との統合については、[アウトバウンド制御](../security/outbound.md)を参照してください。

#### 可視性とフォレンジックのために Resolver クエリログを有効にする {#enable-resolver-query-logging-for-visibility-and-forensics}

Resolver クエリログは、関連付けられた VPC から発生するすべての DNS クエリ(クエリ名、タイプ、レスポンスコード、送信元 IP、タイムスタンプ)を記録します。コスト効率の高い保存と Athena クエリのために S3 に配信するか、不審な解決パターン(既知の C2 ドメインへのクエリ、高頻度の NXDOMAIN レスポンス、単一送信元からの異常なクエリ量)のリアルタイムアラートのために CloudWatch Logs に配信してください。

クエリログは VPC フローログの DNS 版です。ワークロードが名前で到達しようとした対象の完全な記録を提供します。これがなければ、DNS 関連のインシデント(DNS トンネリングによるデータ漏洩、C2 コールバック、転送の設定ミス)の調査は推測に頼ることになります。

### IPv6 に関する考慮事項 {#ipv6-considerations}

#### 最初からデュアルスタックの Resolver エンドポイントを設定する {#configure-dual-stack-resolver-endpoints-from-the-start}

Resolver のインバウンドおよびアウトバウンドエンドポイントは IPv6 ENI アドレスをサポートします。VPC がデュアルスタックの場合、Resolver エンドポイントに IPv4 と IPv6 の両方のアドレスを設定し、IPv6 のみのワークロードが NAT64 なしで転送・解決できるようにしてください。AWS インバウンドエンドポイントに転送するオンプレミスの DNS サーバーは、オンプレミスネットワークもデュアルスタックの場合、エンドポイントの IPv6 アドレスへの到達性が必要です。

#### プライベートホストゾーンの A レコードと並行して AAAA レコードを含める {#include-aaaa-records-alongside-a-records-in-private-hosted-zones}

デュアルスタックインフラストラクチャで動作するすべての内部サービスについて、プライベートホストゾーンに A レコードと AAAA レコードの両方を公開してください。IPv6 を優先する(または IPv6 のみで動作する)アプリケーションは AAAA レコードを使用し、IPv4 のみのコンシューマーは A レコードを使用します。これはデュアルスタック VPC 設計と同じ原則です。後から追加するのではなく、最初から IPv6 を含めてください。

## Route 53 Resolver 機能の使い分け {#when-to-use-route-53-resolver-features}

Route 53 Resolver は常に使用されています。すべての VPC のデフォルトリゾルバーです。判断が必要なのは、どの追加機能を有効にするかです。

**プライベートホストゾーン**が適切な選択肢となるのは以下の場合です。

* パブリックインターネットから解決できないようにすべきサービス、データベース、またはエンドポイントに内部 DNS 名が必要な場合
* スプリットホライズン DNS が必要な場合(クエリが AWS 内外どちらから来るかによって同じドメインに異なる応答を返す)

**Resolver エンドポイントと転送ルール**が適切な選択肢となるのは以下の場合です。

* オンプレミスのワークロードが AWS プライベートホストゾーン名を解決する必要がある場合(インバウンドエンドポイント)
* AWS のワークロードがオンプレミスのドメイン名を解決する必要がある場合(アウトバウンドエンドポイント + 転送ルール)
* AWS 境界をまたぐ DNS 依存関係を持つハイブリッド環境で運用している場合

**Route 53 Profiles** が適切な選択肢となるのは以下の場合です。

* 少数以上のアカウントを運用しており、すべてのアカウントで一貫した DNS 設定が必要な場合
* カスタムオートメーションなしに新しいアカウントが DNS 設定を自動的に継承するようにしたい場合

**DNS Firewall** はすべての VPC で適切な選択肢です。少なくとも AWS マネージド脅威ドメインリストをデプロイしない理由はありません。

## ドキュメント {#documentation}

<div class="grid cards" markdown>

*   :material-file-document: **Route 53 Resolver ドキュメント**

    ---

    Resolver エンドポイント、転送ルール、クエリログ、DNSSEC 検証に関する完全なドキュメントです。

    [:octicons-arrow-right-24: ドキュメント](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html)

*   :material-file-document: **Route 53 Profiles ドキュメント**

    ---

    マルチアカウントの DNS 設定配布のためのプロファイルの作成、共有、管理方法です。

    [:octicons-arrow-right-24: ドキュメント](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profiles.html)

*   :material-file-document: **Route 53 Resolver DNS Firewall**

    ---

    ドメインベースフィルタリングの設定、マネージドドメインリスト、Firewall Manager との統合です。

    [:octicons-arrow-right-24: ドキュメント](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall.html)

*   :material-post: **Route 53 ブログ記事**

    ---

    AWS Networking and Content Delivery ブログのアーキテクチャパターン、機能発表、実装ガイドです。

    [:octicons-arrow-right-24: ブログ記事](https://aws.amazon.com/blogs/networking-and-content-delivery/category/networking-content-delivery/amazon-route-53/)

</div>

## 関連ページ {#related-pages}

**他の基盤トピックとの関係:**

* **[Amazon VPC](vpc.md)**: すべての VPC には Route 53 Resolver が自動的に配置されます。VPC の設計(VPC の数、アカウントの配置)によって、必要なプライベートホストゾーンの関連付けと Resolver エンドポイントの数が決まります。
* **[AWS Organizations](organizations.md)**: Route 53 Profiles は OU レベルで DNS 設定を共有します。OU 構造によって DNS 設定の配布方法が決まります。

**接続性トピックとの関係:**

* **[ハイブリッド & マルチクラウド接続](../connectivity/hybrid-multicloud.md)**: Resolver エンドポイントと転送ルールは、Direct Connect および VPN の DNS 補完機能です。接続レイヤーがネットワークレベルで提供するハイブリッド境界をまたいだ名前解決を可能にします。

**セキュリティトピックとの関係:**

* **[アウトバウンド制御](../security/outbound.md)**: DNS Firewall はアウトバウンド制御ページでエグレス防御の第一層として詳しく説明されています。このページでは DNS Firewall をアーキテクチャとデプロイの観点から説明し、アウトバウンド制御ではセキュリティポリシーの観点から説明しています。

**アプリケーションネットワーキングトピックとの関係:**

* **[サービス間通信](../application-networking/service-to-service.md)**: プライベートホストゾーンと Route 53 エイリアスレコードは、そのページで説明されているプライマリのサービスディスカバリメカニズムです。DNS アーキテクチャの設計判断は、サービスが互いを見つける方法に直接影響します。
