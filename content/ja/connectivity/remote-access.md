# リモートアクセス {#remote-access}

!!! info "前提条件"
    このセクションは、[Amazon VPC](../foundation/vpc.md) と [AWS Organizations](../foundation/organizations.md) に精通していることを前提としています。AWS ネットワーキングの基礎を初めて学ぶ方は、先にそれらのトピックを確認してください。

承認されたユーザーとデバイスに内部 AWS アプリケーションへのアクセスを提供することは、インフラストラクチャ接続とは異なるアーキテクチャ上の課題です。AWS はこの課題に対して、対照的なアプローチを取る 2 つのサービスを提供しています。[AWS Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/what-is.html) はユーザーをネットワークに配置して IP でアプリケーションに到達できるようにし、[AWS Verified Access](https://docs.aws.amazon.com/verified-access/latest/ug/what-is-verified-access.html) はアプリケーションをゼロトラストポリシーエンジンの背後に置き、VPN クライアントを使わずにアイデンティティとデバイスポスチャに基づいてすべてのリクエストを認証・認可します。どちらのサービスも、環境にハイブリッド接続があるかどうかに関わらず動作します。Direct Connect 回線を持つ組織と同様に、クラウドのみの組織にもリモートアクセスは必要です。

新しいアプリケーションアクセスのユースケースには、AWS Verified Access が推奨されます。ゼロトラストアプリケーションアクセスは、多数のアプリケーションとユーザーに対してより優れたスケーラビリティを発揮し、VPN クライアントやエンドポイント証明書の維持管理という運用負荷を排除し、ネットワーク層では実現が難しいリクエスト単位のポリシーを適用します。

## AWS Client VPN {#aws-client-vpn}

AWS Client VPN は、エンドユーザーに VPC へのネットワークレベルの接続を提供する、マネージド型の OpenVPN 互換サービスです。接続された各クライアントは、設定したクライアント CIDR から IP アドレスを受け取り、関連付けられた VPC 内のリソース(およびトランジットパスを通じて他の VPC やオンプレミスネットワーク)に到達できます。認証は、Active Directory、AWS IAM Identity Center などのアイデンティティプロバイダーを使用した SAML ベースのフェデレーション、および証明書ベースの相互認証をサポートしています。

Client VPN は、アプリケーションがネットワーク層の到達性を真に必要とする場合に適しています。たとえば、EC2 インスタンスへの SSH や RDP を使用する管理者、直接 IP 接続を必要とするツールを使用する開発者、または IP アドレスでクライアントを認証するレガシーアプリケーションなどです。また、ユーザーがすでに VPN クライアントに慣れており、アプリケーションがアイデンティティ対応アクセスに向けてリファクタリングされていない既存のワークフローにも適しています。

### AWS Client VPN のベストプラクティス {#aws-client-vpn-best-practices}

#### デフォルトでスプリットトンネルを使用する {#use-split-tunnel-by-default}

特定のコンプライアンス要件によってフルトンネルが正当化される場合を除き、スプリットトンネルを使用してください。これにより、AWS 宛てのトラフィックのみが Client VPN を経由し、一般的なインターネットトラフィックはクライアントのローカルネットワークから直接送出されます。フルトンネルはエグレスコストを増大させ、VPN エンドポイントに負荷を集中させます。スプリットトンネルはユーザーエクスペリエンスも向上させます。レイテンシーに敏感なトラフィック(ビデオ通話、ストリーミング)はローカルインターネットパスを維持できます。

#### ルートだけでなく認可ルールを定義する {#define-authorization-rules-not-just-routes}

Client VPN の認可ルールは、どのユーザーがどの宛先に到達できるかを制御します。ルートテーブルだけではトラフィックの流れを許可するに過ぎず、対応する認可ルールがなければ、ユーザーは本来アクセスすべきでない宛先にも到達できてしまいます。認可ルールは職務機能に基づいて設計してください。管理者には管理サブネットへの SSH/RDP アクセスを、開発者にはアプリケーション VPC へのアクセスを、一般ユーザーには必要な特定のアプリケーションへのアクセスのみを付与します。

#### 競合を避けるためにクライアント CIDR を計画する {#plan-the-client-cidr-to-avoid-conflicts}

クライアント CIDR(接続された VPN クライアントに割り当てられる IP 範囲)は、VPC CIDR、ピアリングされた VPC、オンプレミスネットワーク、または他の VPN クライアントプールと重複してはなりません。IPAM 計画から専用の範囲を使用してください。`172.16.0.0/12` 空間からの `/16` は、VPC やオンプレミスで一般的に使用される `10.0.0.0/8` 空間との競合を避けるための一般的な選択肢です。

#### アベイラビリティーゾーンだけでなくエンドポイント数でスケールする {#scale-by-endpoint-count-not-just-availability-zone}

Client VPN エンドポイントは多数の同時接続をサポートしますが、サイジングは定常状態だけでなく、ピーク時の同時ユーザー数を考慮する必要があります。CloudWatch で `ActiveConnectionsCount` と `CrlDaysToExpiry` を監視してください。数千の同時ユーザーを抱える組織では、ユーザー集団またはアプリケーショングループごとにセグメント化した複数のエンドポイントを検討してください。

## AWS Verified Access {#aws-verified-access}

AWS Verified Access は、VPN クライアントなしで企業アプリケーションへのゼロトラストアクセスを提供します。ユーザーはブラウザまたはアプリケーション固有のクライアントを通じてアプリケーションに到達し、Verified Access はアイデンティティ(AWS IAM Identity Center またはサードパーティのアイデンティティプロバイダーから)とデバイスポスチャ(CrowdStrike やモバイルデバイス管理ベンダーなどの統合デバイストラストプロバイダーから)を組み合わせたポリシーに対してすべてのリクエストを評価します。ポリシーを満たさないリクエストは拒否され、満たすリクエストはアプリケーションに転送されます。

Verified Access は、Web ベースのアプリケーション(HTTP/HTTPS)と TCP、SSH、または RDP 経由で到達する非 Web アプリケーションの両方をサポートしているため、以前は Client VPN が必要だったほとんどのユースケースをカバーします。ポリシーは AWS で一元管理され、Cedar ポリシー言語で表現され、リクエストごとに評価されます。これにより、ネットワーク層のアクセスでは提供できないきめ細かい制御が可能になります(たとえば、ユーザーが認証されていても、デバイスのポスチャチェックが失敗した場合にアクセスをブロックするなど)。

### AWS Verified Access のベストプラクティス {#aws-verified-access-best-practices}

#### すべての新しいアプリケーションアクセスのユースケースに Verified Access から始める {#start-with-verified-access-for-every-new-application-access-use-case}

新しいアプリケーションアクセスのユースケースには、AWS Verified Access が推奨されます。その理由は以下のとおりです。

* **エンドポイントへの VPN クライアントのデプロイ、配布、維持管理が不要。** ユーザーはすでに使用している標準クライアント(ブラウザまたはプロトコル固有のクライアント)を通じてアプリケーションに到達します。
* **アイデンティティとデバイスポスチャによるリクエスト単位のポリシー評価**。ネットワーク接続の全か無かのトラストモデルとは異なります。
* **すべてのアクセス試行(許可と拒否)の包括的なログ記録**。理由、ユーザー、デバイスのコンテキストを含みます。VPN 接続ログとアプリケーションログを別々に組み合わせて再構成するよりも容易です。
* **スケールにおけるシンプルな運用モデル。** 新しいアプリケーションのオンボーディングは、VPN 認可ルールの拡張とルートの再伝播ではなく、Verified Access エンドポイントとポリシーの追加を意味します。

#### 最初からデバイストラストを統合する {#integrate-device-trust-from-day-one}

Verified Access のポリシーは、アイデンティティ*と*デバイスポスチャを組み合わせたときに最も価値を発揮します。デバイストラストプロバイダー(CrowdStrike、Jamf、またはその他の MDM/EDR ベンダー)は、後から追加する機能としてではなく、デプロイ時に接続してください。アイデンティティのみをチェックするポリシーは、従来の SSO チェックとほとんど変わりません。デバイスポスチャ(OS にパッチが適用されているか？ディスク暗号化が有効か？EDR エージェントが実行中か？)を追加することが、Verified Access を真のゼロトラストにします。

#### きめ細かく監査可能なアクセス制御に Cedar ポリシーを使用する {#use-cedar-policies-for-fine-grained-auditable-access-control}

Verified Access が使用するポリシー言語である Cedar は、ユーザー属性、グループメンバーシップ、デバイスポスチャシグナル、およびリクエスト属性(IP、時刻、アプリケーション)に対する条件をサポートしています。「認証済みユーザー全員を許可する」という広範なルールではなく、アプリケーションごとに明示的なポリシーを記述してください。きめ細かいポリシーは監査が容易で、コンプライアンスチームへの説明も簡単になり、認証情報が侵害された場合の影響範囲を縮小します。

#### Client VPN から段階的に移行する {#migrate-from-client-vpn-incrementally}

Verified Access が現時点で適合しない場合、Client VPN は引き続き利用可能であり、移行中は両者を共存させることができます。推奨されるパターンは以下のとおりです。

1. 最初から新しいアプリケーションに Verified Access をデプロイする
2. ライフサイクルが許す限り(通常は次のメジャーアップデートまたはセキュリティレビュー時に)既存のアプリケーションを Verified Access に移行する
3. Client VPN のスコープを、ネットワーク層のアクセスが真に必要なケース(SSH、RDP、レガシープロトコル)に徐々に縮小する
4. アプリケーションポートフォリオのモダナイゼーションが進むにつれて、Verified Access に統合していく

[Client VPN と Verified Access の相互運用パターン](https://aws.amazon.com/blogs/networking-and-content-delivery/aws-client-vpn-and-aws-verified-access-migration-and-interoperability-patterns/)では、これらの移行パスについて詳しく説明しています。

## 各サービスの使い分け {#when-to-use-each-service}

**AWS Verified Access** が適切な選択肢となる場合:

* ユーザーが Web アプリケーション(HTTP/HTTPS)または TCP/SSH/RDP サービスへのアクセスを必要とする場合
* リクエスト単位のアイデンティティとデバイスポスチャの評価が必要な場合
* VPN クライアントのデプロイと維持管理を排除したい場合
* 新しいアプリケーションをリモートアクセスにオンボーディングする場合

**AWS Client VPN** が適切な選択肢となる場合:

* アプリケーションが完全なネットワーク層の IP 到達性を必要とする場合(アプリケーションレベルのアクセスだけでは不十分な場合)
* ユーザーが特定のアプリケーションではなく広範なネットワーク範囲へのアクセスを必要とする場合
* レガシープロトコルやワークフローが、ユーザーが VPC 内でルーティング可能な IP を持つことに依存している場合
* 組織がまだ移行していない VPN ベースのワークフローを確立している場合

AWS Client VPN はアプリケーションアクセスの**長期的な解決策ではありません**。新しいアプリケーションには Verified Access から始め、真にネットワーク層が必要なケースにのみ Client VPN を使用してください。

## ドキュメント {#documentation}

<div class="grid cards" markdown>

*   :material-file-document: **AWS Client VPN ドキュメント**

    ---

    エンドポイント、認証方法、認可ルール、スプリットトンネル設定を網羅した完全なサービスドキュメント。

    [:octicons-arrow-right-24: ドキュメント](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/what-is.html)

*   :material-file-document-outline: **AWS Verified Access ドキュメント**

    ---

    エンドポイント、Cedar によるポリシー、アイデンティティとデバイストラストプロバイダー、サポートされるアプリケーションタイプを網羅した完全なサービスドキュメント。

    [:octicons-arrow-right-24: ドキュメント](https://docs.aws.amazon.com/verified-access/latest/ug/what-is-verified-access.html)

*   :material-post: **AWS Client VPN と Verified Access の相互運用パターン**

    ---

    移行中に Client VPN と Verified Access を並行して運用するための 4 つの移行・相互運用パターン。

    [:octicons-arrow-right-24: ブログ記事](https://aws.amazon.com/blogs/networking-and-content-delivery/aws-client-vpn-and-aws-verified-access-migration-and-interoperability-patterns/)

*   :material-currency-usd: **AWS Verified Access 料金**

    ---

    Verified Access エンドポイントのアプリケーション時間単位およびデータ処理 GB 単位の料金。

    [:octicons-arrow-right-24: 料金](https://aws.amazon.com/verified-access/pricing/)

</div>

## 関連ページ {#related-pages}

**他の接続トピックとの関係:**

* **[ハイブリッド & マルチクラウド接続](hybrid-multicloud.md)** — ハイブリッド接続はオンプレミスと AWS 間のインフラストラクチャレベルのパスを提供します。リモートアクセスはアプリケーションへのユーザーレベルのパスを提供します。両者は独立しています。Verified Access と Client VPN は、ハイブリッド接続がなくても動作します。

**セキュリティトピックとの関係:**

* **[ネットワークセグメンテーション](../security/segmentation.md)** — Verified Access の認証ポリシーはアプリケーション境界でアイデンティティベースのセグメンテーションを提供します。Client VPN の認可ルールは VPN ユーザーに対してネットワークレベルのセグメンテーションを提供します。
