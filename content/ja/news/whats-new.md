---
hide:
  - toc
---
# AWS What's New — ネットワーキング

[AWS What's New](https://aws.amazon.com/new/) の新着発表からネットワーキング関連の項目を抽出し、平日の毎朝、自動で要約します。原文は各項目のリンクをご確認ください。最新の項目が上部に表示されます。

<!-- NEWS:INSERT -->

## 2026-11-26 · 前日のアップデート

- **[Amazon EC2 M8g インスタンスがイスラエル（テルアビブ）リージョンで利用可能に](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-ec2-m8g-instances-telaviv-region/)** — AWS Graviton4 プロセッサを搭載した Amazon EC2 M8g インスタンスが、イスラエル（テルアビブ）リージョンで利用可能になりました。Graviton3 ベースのインスタンスと比較して最大 30% の性能向上を実現し、アプリケーションサーバーやマイクロサービスなどの汎用ワークロードに適しています。
- **[AWS IoT Core の HTTP ルールアクションが専用 IPv6 アドレス範囲を使用するように](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-iot-core-dedicated-ipv6-ranges/)** — AWS IoT Core の HTTP ルールアクションが、専用の公開済み IPv6 アドレス範囲を使用して HTTPS エンドポイントにトラフィックを送信できるようになりました。これにより、HTTPS エンドポイントが AWS IoT Core からのリクエストのみを受け入れるよう設定でき、パブリックインターネットへの露出を低減できます。

## 2026-11-25 · 前日のアップデート

- **[Amazon API Gateway、API Portal の提供を発表](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-api-gateway-announces-api-portal/)** — Amazon API Gateway は、AWS 組織全体の API および AI エンドポイントを自動的に検出・管理・ドキュメント化する新機能 API Portal をリリースしました。インストールやログ転送、トラフィックの再ルーティングなしに、AWS 側のトラフィックログとサービス設定レコードを活用して継続的に最新のインベントリを維持します。

## 2026-11-24 · 前日のアップデート

- **[AWS WAF、Amazon Bedrock Guardrails を使用した LLM・MCP・A2A エンドポイントの自動検出と保護機能を発表](https://aws.amazon.com/about-aws/whats-new/2026/11/waf-ai-endpoint-discovery-protection/)** — AWS WAF が、Amazon API Gateway、Application Load Balancer、Amazon CloudFront の背後にある LLM、MCP、A2A エンドポイントを自動検出し、Amazon Bedrock Guardrails で保護する機能を一般提供開始しました。エージェントのデプロイやログ転送なしに、トラフィックログとサービス設定レコードから AI エンドポイントを自動識別し、AWS Organization 全体に保護を適用できます。
- **[Amazon CloudFront が AWS European Sovereign Cloud で利用可能に](https://aws.amazon.com/about-aws/whats-new/2026/11/cloudfront-european-sovereign-cloud)** — Amazon CloudFront が AWS European Sovereign Cloud で正式に利用可能となり、EU データ主権要件を持つ組織がコンテンツ配信、TLS 終端、ログおよび設定を EU 境界内に保ちながら CloudFront のパフォーマンスと保護を活用できるようになりました。これまでは EU 内にトラフィックを留めるために独自の配信・TLS 終端インフラを構築する必要がありました。
- **[Amazon CloudFront、オリジンへの接続で HTTP/2 サポートを発表](https://aws.amazon.com/about-aws/whats-new/2026/01/amazon-cloudfront-http2-origins/)** — Amazon CloudFront がカスタムオリジンおよび VPC オリジンへの HTTP/2 接続をサポートし、より少ない接続と TLS ハンドシェイクで多数のリクエストを処理できるようになりました。AI エージェントによる MCP サーバーへの同時ツール呼び出しなど、トラフィックが急増するエージェント型ワークロードでのオリジン負荷を大幅に軽減します。
- **[AWS Global Accelerator、TLS リスナーを持つ NLB に対するクライアント IP 保持をサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/global-accelerator-client-ip-nlb-tls/)** — AWS Global Accelerator が TLS リスナーを使用する Network Load Balancer エンドポイントへのトラフィックに対してクライアント IP アドレスの保持をサポートし、NLB で TLS を終端しながらもアプリケーションで実際のクライアント IP を確認できるようになりました。これにより、セキュリティグループ、ジオブロッキング、レート制限、監査ログなどの保護制御を実際のクライアント IP に基づいて適用できます。
- **[Amazon EC2 G7 インスタンスの metal サイズの提供開始を発表](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-g7-metal-size/)** — AWS が NVIDIA RTX PRO 4500 Blackwell Server Edition GPU を搭載した Amazon EC2 G7 インスタンスの metal サイズを一般提供開始しました。G6 比で最大 4.6 倍の AI 推論性能を提供し、ベアメタルインフラへの直接アクセスが必要な物理 AI シミュレーション、AI エージェントサンドボックス、グラフィクスワークロードに活用できます。
- **[Amazon Aurora Serverless for MySQL、最大 384 ACU をサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/aurora-serverless-mysql-supports-384-acu/)** — Amazon Aurora Serverless が Aurora MySQL 互換エディションで最大 384 ACU (Aurora Capacity Units) をサポートし、従来の最大値 256 ACU から 50% 増加しました。単一データベースが最大 768 GiB のメモリまでスケールアップでき、活動の急増と長いアイドル期間が繰り返されるエージェント型 AI アプリケーションに特に適しています。
- **[AWS WAF を活用した API セキュリティの自動化機能が一般提供開始](https://aws.amazon.com/about-aws/whats-new/2026/11/api-security-with-waf/)** — AWS Organization 全体で Amazon API Gateway、Application Load Balancer、Amazon CloudFront の背後にあるすべての API を自動検出し、AWS WAF で保護する機能が一般提供開始されました。新しい API Gateway API Portal はトラフィックログとサービス設定レコードから API を自動識別し、ゾンビ API やシャドウ API を検出して各 API のセキュリティ状態を評価します。
- **[Amazon SageMaker HyperPod、Amazon EKS オーケストレーションクラスター作成のためのコンソール体験を刷新](https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-hyperpod-console-eks/)** — Amazon SageMaker HyperPod が Amazon EKS オーケストレーションクラスターを作成するための AWS Management Console 体験を刷新し、ネットワーキング、インスタンスグループ、ストレージ、権限、復元力、観測性などをガイド付きワークフローで設定できるようになりました。必須設定とオプション設定を分離し、スマートデフォルトとワークロードプロファイルを提供することで、ML インフラ管理者のクラスター設定の負担を軽減します。

## 2026-11-21 · 前日のアップデート

- **[AWS Network Firewall、自動化されたインターネットファイアウォールをパブリックプレビューで発表](https://aws.amazon.com/about-aws/whats-new/2026/11/network-firewall-automated-internet/)** — AWS Network Firewall が、インターネットゲートウェイに直接アタッチする自動化されたインターネットファイアウォール機能をパブリックプレビューで公開しました。ルーティングやアーキテクチャの変更なしに、すべての VPC のインバウンド・アウトバウンドトラフィックにセキュリティルールを中央集中式で適用でき、ネイティブ NAT 機能も提供されます。
- **[AWS CloudFormation Service-Managed StackSets、ネストされたスタックをサポートするカスタム実行ロールを追加](https://aws.amazon.com/about-aws/whats-new/2026/11/stacksets-custom-execution-roles/)** — AWS CloudFormation StackSets が、サービス管理型スタックセットでカスタム実行ロールをサポートし、各ターゲットアカウントで使用する権限の範囲を細かく制御できるようになりました。これにより、ネストされたスタックやマクロ、トランスフォームを活用した再利用可能なテンプレートを、組織全体のアカウントおよびリージョンに一括デプロイできます。
- **[Amazon ECS Action Logs、タスク・コンテナインスタンス・キャパシティプロバイダーまでカバー範囲を拡張](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-ecs-action-logs-expanded-troubleshooting)** — Amazon ECS の Action Logs が、サービスデプロイに加えてタスク、コンテナインスタンス、クラスター、キャパシティプロバイダーまでカバー範囲を拡張しました。タイムスタンプ付きの詳細な記録により、タスクの失敗やスケーリングの問題を AWS サポートに問い合わせることなく自己診断・解決できます。
- **[Amazon Route 53、アベイラビリティーゾーン (AZ) アフィニティルーティングをサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/route-53-affinity-routing/)** — Amazon Route 53 が AZ アフィニティルーティングをサポートし、VPC 内のクライアントからの DNS クエリを同じ AZ 内のリソースへ優先的に応答するようになりました。これにより、AZ 間トラフィックを削減して遅延時間を短縮し、アプリケーションのパフォーマンスを向上させることができます。
- **[Amazon VPC IPAM ポリシー、自動化されたインターネットファイアウォールおよび AWS Lambda Web Functions・MicroVM をサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/vpc-ipam-policies-firewall-lambda/)** — Amazon VPC IPAM ポリシーが AWS Network Firewall の自動化されたインターネットファイアウォールと AWS Lambda Web Functions・MicroVM をサポートし、BYOIP や Amazon 提供の連続 IPv4 ブロックなど特定の IPAM プールからパブリック IPv4 アドレスを中央集中式に割り当てられるようになりました。これにより、セキュリティ態勢の強化、ネットワーク運用の簡素化、および BYOIP 使用時のパブリック IPv4 コスト削減が期待できます。
- **[コロンビア・ボゴタの新しい AWS Local Zone が一般提供開始](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-local-zone-bogota-colombia/)** — AWS がコロンビアのボゴタに新しい Local Zone を一般提供開始し、リアルタイムゲームやライブ動画ストリーミング、医療画像処理、金融取引処理など、一桁ミリ秒の遅延時間を必要とするワークロードに対応します。AWS リージョンと同じ API およびツールを使用しながら、コンピューティング・ストレージ・ネットワーキングのインフラをボゴタ近郊のエンドユーザーに近い場所で提供します。
- **[Amazon Route 53 プライベートホスティングゾーン、パブリック DNS フォールバックをサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/route-53-public-dns-fallback/)** — Amazon Route 53 のプライベートホスティングゾーンがパブリック DNS フォールバックをサポートし、ゾーン内に一致するレコードがないクエリに対して NXDOMAIN ではなくパブリック DNS の応答を返すようになりました。この機能は Advanced Hosted Zones の一部として提供され、パブリックゾーンのすべてのレコードをプライベートゾーンに複製する運用負担を軽減します。
- **[Amazon VPC Lattice、VPC リソース向け CloudWatch メトリクスをサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/vpc-lattice-cloudwatch-metrics/)** — Amazon VPC Lattice が VPC リソース向けの Amazon CloudWatch メトリクスの公開をサポートし、リソースの公급者と消費者の両方がデータベース・クラスター・オンプレミスエンドポイントへの TCP トラフィックをリアルタイムで確認できるようになりました。これまでは追加処理が必要なリソースアクセスログに依存していましたが、CloudWatch メトリクスによってより簡単に観測性を確保できます。
- **[Amazon Route 53、Advanced Hosted Zones を提供開始](https://aws.amazon.com/about-aws/whats-new/2026/11/route-53-offers-advanced-hosted-zones/)** — Amazon Route 53 が、変更ガードレール、レコードレベルの変更履歴、プライベートホスティングゾーンのパブリック DNS フォールバックなどの追加保護機能と観測性を提供する新しいホスティングゾーン階層「Advanced Hosted Zones」を発表しました。誤ったレコード削除や委任の削除によるドメイン障害を防ぎ、DNS 運用の復元力を高めます。

## 2026-11-20 · 前日のアップデート

- **[Amazon CloudFront の SaaS Manager に IP ベースルーティングと接続ログを追加](https://aws.amazon.com/about-aws/whats-new/2026/11/cloudfront-ip-based-routing-connection-logging)** — Amazon CloudFront SaaS Manager が IP アドレスベースのルーティングをサポートし、同一ワイルドカードドメイン配下で顧客の計層ごとに異なる設定を提供できるようになりました。また、接続ログにより視聴者接続の観測性も確保できます。
- **[Amazon CloudFront SaaS Manager のドメイン移行とオンボーディングを簡素化](https://aws.amazon.com/about-aws/whats-new/2026/11/cloudfront-domain-moves-distribution-tenants)** — Amazon CloudFront がダウンタイムなしに単一リクエストで顧客ドメインをプラットフォームへ移行できる機能を追加し、TLS 証明書の設定中もリクエストを処理できるようになりました。既存の AWS 顧客をトラフィックへの影響なくマルチテナント配布へ移行できます。
- **[Amazon Route 53 がプライベートエンドポイントのヘルスチェックをサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/route-53-private-endpoint-health-checks/)** — Amazon Route 53 がプライベートエンドポイントのヘルスチェックをサポートし、パブリックインターネットに公開されない内部 API やデータベースなどに対してネイティブのヘルス監視と自動 DNS フェイルオーバーが利用できるようになりました。プライベートホスティングゾーンの DNS レコードと関連付けることで、正常なエンドポイントのみにトラフィックをルーティングできます。
- **[AWS WAF がリアルタイム調査向けセキュリティ分析ダッシュボードを提供開始](https://aws.amazon.com/about-aws/whats-new/2026/02/aws-waf-security-analytics-dashboard/)** — AWS WAF が、アカウント内のすべての Web ACL のトラフィックを単一ビューに統合する新しいセキュリティ分析ダッシュボードを提供開始しました。ロギングパイプラインを構築せずにコンソールから直接リクエストログを検索でき、21 日分のフルフィデリティリクエストデータを追加料金なしで利用できます。
- **[エクスプレス設定で作成した Aurora PostgreSQL が Amazon VPC をサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/aurora-postgresql-express-vpc/)** — エクスプレス設定で作成した Aurora PostgreSQL データベースを、単一の API 呼び出しまたは Amazon RDS コンソールの変更操作で Amazon VPC 内に移行できるようになりました。データ移行なしに AI 構築のプロトタイプを本番環境へ移行しながら、セキュリティおよびコンプライアンス要件を満たすことができます。
- **[Amazon Aurora が異なる VPC へのクラスター移行をサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/aurora-move-clusters-to-different-vpc/)** — Aurora PostgreSQL および Aurora MySQL クラスターを、データ移行なしに単一の API 呼び出しで別の Amazon VPC へ移行できるようになりました。IP アドレス空間の拡張や非重複 CIDR 範囲の適用、ネットワークアーキテクチャの統合など、さまざまなネットワーキング要件に対応できます。
- **[AWS Continuum for Penetration Testing が一時停止と再開をサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/continuum-pentest-pause-resume/)** — AWS Continuum for Penetration Testing が、実行中のペネトレーションテストジョブを一時停止し、最後に保存されたチェックポイントから再開できる機能を追加しました。クライアント設定エラーでジョブが失敗しても、既存の検出結果と完了済み作業を保持したまま続行できます。
- **[AWS Site-to-Site VPN がポスト量子鍵交換をサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/site-to-site-vpn-post-quantum/)** — AWS Site-to-Site VPN が NIST ガイドラインに基づくポスト量子暗号への移行をサポートするため、ポスト量子鍵交換方式を追加しました。CreateVpnConnection および ModifyVpnTunnelOptions API を通じて VPN トンネルオプションに設定でき、追加料金はかかりません。
- **[Amazon VPC Flow Logs が Amazon EKS メタデータをサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-vpc-flow-logs-amazon-eks-metadata/)** — Amazon VPC Flow Logs がフローログレコードに Amazon EKS メタデータを追加し、トラフィックを送受信した Pod とそのクラスター、ネームスペース、ラベルを識別できるようになりました。ノードに監視ソフトウェアをインストールすることなく、EKS クラスターのセキュリティイベント調査やネットワークトラブルシューティングを迅速化できます。
- **[AWS Network Firewall が明示的プロキシ機能と NAT Gateway の関連付けを提供開始](https://aws.amazon.com/about-aws/whats-new/2026/11/network-firewall-proxy-nat-gateway/)** — AWS Network Firewall が NAT Gateway との関連付けをサポートし、明示的プロキシと透過型ファイアウォールの両方として動作しながらネイティブのネットワークアドレス変換を提供できるようになりました。アプリケーショントラフィックのフィルタリング、データ流出防止、マルウェア注入のブロックを統合的に設定できます。
- **[Amazon Inspector Code Security が GitHub Enterprise Server とプライベート接続をサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/inspector-code-ghes-private-network/)** — Amazon Inspector Code Security が GitHub Enterprise Server (GHES) の統合と、GHES および GitLab Self-Managed 向けのプライベートネットワーク接続をサポートしました。Amazon VPC 設定または AWS CodeConnections を通じて、ファイアウォールを AWS の全 IP 範囲に開放することなくプライベートネットワーク内のリポジトリをスキャンできます。
- **[Amazon Bedrock AgentCore Identity がプライベート認証局をサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/bedrock-agentcore-identity-private-ca/)** — Amazon Bedrock AgentCore Identity がカスタム OAuth 2.0 クレデンシャルプロバイダー向けにプライベート認証局 (CA) をサポートしました。VPC 内にホストされた ID プロバイダー (IdP) との接続で、AWS Private CA、エンタープライズ CA、自己署名ルート CA が発行した証明書を信頼するよう設定できます。
- **[AWS Network Load Balancer が相互 TLS 認証をサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/network-load-balancer-mtls/)** — AWS Network Load Balancer (NLB) が X.509 証明書を提示するクライアントに対する相互 TLS (mTLS) 認証をサポートしました。NLB の TLS リスナーでクライアント証明書を検証するため、バックエンドアプリケーションに証明書ロジックを追加することなく、信頼されたクライアントのみがターゲットにアクセスできるよう制限できます。
- **[AWS CloudFormation StackSets が大規模デプロイの進捗可視化機能を追加](https://aws.amazon.com/about-aws/whats-new/2026/11/cloudformation-stacksets-progress/)** — AWS CloudFormation StackSets が、数十から数千のアカウントおよび AWS リージョンにまたがるデプロイのステージごとの進捗状況を表示する機能を追加しました。デプロイの完了を待たずにリアルタイムで状況を確認し、必要に応じてすぐに対処できるため、ネットワーキングやセキュリティ設定の大規模なロールアウト管理が容易になります。
- **[Amazon CloudWatch が Amazon VPC のネットワークパフォーマンス監視を簡素化](https://aws.amazon.com/about-aws/whats-new/2026/11/cloudwatch-network-path-monitoring/)** — Amazon CloudWatch Network Monitoring がパフォーマンスモニターを通じて、ソフトウェアのインストールなしに VPC ワークロードが使用する AWS ネットワークパスの状態をほぼリアルタイムで監視できるようになりました。監視する VPC を選択するだけで、パスごとの遅延時間、ネットワーク影響スコア、トラフィックボリュームなどの指標を数分以内に確認できます。

## 2026-11-19 · 前日のアップデート

- **[Amazon CloudFront の標準ログが CMCD および追加ログフィールドをサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/cloudfront-standard-logging-cmcd-fields)** — Amazon CloudFront の標準ログが、これまでリアルタイムログでのみ利用可能だった CloudFront サーバー IP、配信識別子、メディア品質信頼スコア、CMCD などのフィールドに対応しました。別途リアルタイムログストリームを設定することなく、Amazon S3・Amazon CloudWatch Logs・Amazon Data Firehose へ配信できます。
- **[Amazon CloudFront が WebSocket および gRPC のオリジン相互 TLS をサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-cloudfront-origin-mtls-websockets-grpc/)** — Amazon CloudFront のオリジン相互 TLS (mTLS) 認証が WebSocket および gRPC トラフィックに対応しました。チャットプラットフォームやリアルタイムダッシュボードなど、持続的・双方向接続を必要とするアプリケーションを未認証リクエストから保護できます。
- **[Amazon CloudFront Functions がネットワーク呼び出しをサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/cloudfront-functions-network-calls/)** — Amazon CloudFront Functions が新しい cf.fetch() メソッドにより、エッジから外部 API を直接呼び出してレスポンスに基づいたリクエスト処理が可能になりました。これまで外部データを必要とするロジックは Lambda@Edge やオリジンに移す必要がありましたが、エッジでリアルタイムにパーソナライズ・認証・ルーティングを実行できます。
- **[Amazon SageMaker HyperPod が EKS オーケストレーションクラスターでより高い Pod 密度をサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-hyperpod-higher-pod-density/)** — Amazon SageMaker HyperPod が EKS オーケストレーションクラスターでノードあたりの Pod 密度向上をサポートし、Pod 増加に応じて Amazon VPC CNI がネットワーク容量を自動的に拡張します。Karpenter によるオートスケーリングも高い Pod 容量に対応し、より少ないインスタンスで同等のワークロードを処理できます。
- **[Cost Optimization Hub がアイドル状態の Amazon EC2 インスタンスの停止をサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/cost-hub-stop-idle-ec2/)** — AWS Cost Optimization Hub の「節約の機会」ページから、アイドル状態の Amazon EC2 インスタンスをコンソールを離れることなく直接停止できるようになりました。これまでは EC2 コンソールに移動してインスタンスを特定する必要がありましたが、推奨事項から即座に対応できます。
- **[Amazon SageMaker HyperPod Inference が分散・マルチノード推論向けに NVIDIA Dynamo をサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-hyperpod-nvidia-dynamo/)** — Amazon SageMaker HyperPod Inference が NVIDIA Dynamo に対応し、単一インスタンスの GPU メモリを超える大規模モデルのマルチノード推論や、プリフィルとデコードステージの分離による高速なトークン生成が可能になりました。Inference Operator アドオンを通じて HyperPod が Dynamo を管理するため、分散サービングインフラを自前で構築・運用する必要はありません。
- **[AWS Transform が AWS Outposts へのマイグレーションをサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-transform-outposts-migration/)** — AWS Transform が AWS Outposts をマイグレーション先としてサポートし、オンプレミス環境や別の Outpost、異なるアベイラビリティーゾーン・リージョンから Outposts へのワークロード移行が可能になりました。低レイテンシー要件で Outposts を運用するお客様も、AI エージェントによる自動化されたマイグレーションワークフローを活用できます。
- **[AWS Transform が Well-Architected Agent レビューを提供](https://aws.amazon.com/about-aws/whats-new/2026/11/transform-well-architected-agent/)** — AWS Transform のマイグレーションサービスが、インフラを AWS へ移行する過程でターゲットネットワークの Well-Architected レビューを自動的に提供するようになりました。セキュリティ・信頼性・コスト最適化の各原則に基づく推奨事項がデプロイ前にネットワーク設計へ直接適用されるため、デプロイ後の修正コストを削減できます。
- **[AWS Transit Gateway が Gateway Load Balancer とのネイティブ統合をサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/transit-gateway-gwlb-integration/)** — AWS Transit Gateway が Gateway Load Balancer タイプのネットワーク機能アタッチメントをサポートし、複雑な VPC 設定なしにファイアウォールなどのセキュリティアプライアンスを Transit Gateway に接続できるようになりました。選択したアベイラビリティーゾーンへの Gateway Load Balancer エンドポイントの作成・管理は Transit Gateway が自動的に行うため、専用のエンドポイントサブネットやルーティングテーブルが不要になります。
- **[AWS WAF が Bot Control ターゲット保護のオンボーディングを簡素化](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-waf-bot-control-onboarding/)** — AWS WAF が Bot Control のターゲット検査レベルに対して簡素化されたコンソール操作を提供し、単一の設定で Amazon CloudFront ディストリビューションに AWS 推奨のターゲットボット保護を適用できるようになりました。ボット信頼度レベル（高・中・低）と最新の検出を自動維持する LATEST バージョンが追加され、高度な AI 駆動ボットへの対策が強化されています。

## 2026-11-18 · 前日のアップデート

- **[Amazon EC2 C8gn インスタンスが AWS イスラエル (テルアビブ) リージョンで利用可能に](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-ec2-c8gn/)** — AWS Graviton4 プロセッサを搭載した Amazon EC2 C8gn インスタンスが、AWS イスラエル (テルアビブ) リージョンで利用可能になりました。最大 600 Gbps のネットワーク帯域幅を提供し、前世代の C7gn と比較してコンピューティング性能が最大 30% 向上しています。
- **[Amazon EC2 C8ine インスタンスが AWS ヨーロッパ (アイルランド) リージョンで利用可能に](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-ec2-c8ine)** — AWS 専用の第 6 世代 Intel Xeon Scalable プロセッサを搭載した Amazon EC2 C8ine インスタンスが、AWS ヨーロッパ (アイルランド) リージョンで利用可能になりました。前世代の C6in と比較して最大 43% 高いパフォーマンスと、vCPU あたり最大 2.5 倍のパケット処理性能を提供します。
- **[Amazon EVS が r7i.metal インスタンス、外部プリンシパルストレージ、Agent Skill をサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-evs-r7i-agent-skill-support/)** — Amazon Elastic VMware Service (Amazon EVS) が、VMware Cloud Foundation 9.x 向けに r7i.metal-24xl および r7i.metal-48xl EC2 ベアメタルインスタンスをサポートしました。ローカル NVMe ディスクを持たないこれらのインスタンスで、Amazon FSx for NetApp ONTAP などの外部ストレージソリューションを主ストレージとして利用できます。
- **[Amazon VPC、AWS Transit Gateway、AWS Cloud WAN がリージョン間トラフィックに 99.999% 可用性 SLA を提供](https://aws.amazon.com/about-aws/whats-new/2026/11/vpc-tgw-cloudwan-99999-sla/)** — AWS は Multipath Resilience 機能を導入し、Amazon VPC リージョン間ピアリング、AWS Transit Gateway、AWS Cloud WAN のリージョン間トラフィックに対して 99.999% の可用性 SLA を提供します。物理的に多様なファイバーパスを活用して経路障害時に自動的にトラフィックを切り替え、決済処理や金融取引などのミッションクリティカルなアプリケーションの復元力を高めます。
- **[Amazon S3 が追加エンドポイントにポスト量子 TLS キー交換サポートを拡張](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-s3-post-quantum-tls-key-exchange-support/)** — Amazon S3 が S3 Vectors および AWS PrivateLink for Amazon S3 インターフェースエンドポイントに、ポスト量子 TLS (PQ-TLS) キー交換サポートを追加しました。NIST 標準アルゴリズムである ML-KEM を使用し、量子コンピューティングの脅威に対する暗号化保護の範囲がさらに拡大されます。
- **[Amazon S3 が AWS CloudTrail でポスト量子 TLS の観測性を提供](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-s3-post-quantum-tls-aws-cloudtrail/)** — Amazon S3 が AWS CloudTrail に TLS キー交換アルゴリズム情報を記録するようになり、どのリクエストやクライアントがポスト量子 TLS (PQ-TLS) を使用しているかを確認できます。これにより、従来のキー交換を使用しているアプリケーションや IAM プリンシパルを特定し、アップグレード計画を立てることが容易になります。
- **[Amazon Route 53 Resolver DNS Firewall が Infoblox Threat Defense をサポート (プレビュー)](https://aws.amazon.com/about-aws/whats-new/2026/11/route53-dns-firewall-infoblox-preview/)** — Amazon Route 53 Resolver DNS Firewall が Infoblox Threat Defense と統合され (プレビュー)、AWS Marketplace から購読した Infoblox の脅威インテリジェンスを DNS Firewall ルールに直接適用できるようになりました。これにより、Amazon VPC 内のアプリケーションを DNS レイヤーで悪意のあるドメインから事前に保護できます。
- **[Amazon Route 53 Resolver DNS Firewall が許可リストの自動生成をサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/route-53-dns-firewall-auto-allowlists/)** — Amazon Route 53 Resolver DNS Firewall が VPC の DNS クエリトラフィックを分析してドメイン許可リストを自動生成する機能をサポートしました。セキュリティチームが手動でログを分析することなく、最小権限の DNS アクセスポリシーを迅速に適用し、DNS ベースのデータ漏洩リスクを低減できます。
- **[AWS Transit Gateway がセグメンテーションポリシーのためにリソースコンテキストをファイアウォールと共有](https://aws.amazon.com/about-aws/whats-new/2026/11/transit-gateway-firewall-context-sharing/)** — AWS Transit Gateway が接続されたファイアウォールなどのセキュリティサービスとリソースコンテキストを共有する機能をサポートしました。IP アドレスの代わりに Amazon VPC、VPC サブネット、VPC セキュリティグループ、Transit Gateway アタッチメントに基づいてセグメンテーションポリシーを適用でき、新しいワークロードが追加されても手動でルールを更新する必要がなくなります。
- **[Amazon Route 53 Global Resolver がハイブリッドネットワーク向けに AWS Cloud WAN をサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/route-53-global-resolver-cloud-wan/)** — Amazon Route 53 Global Resolver が AWS Cloud WAN で管理されるプライベート接続に対してエニーキャスト DNS 解決をサポートしました。AWS Direct Connect または AWS VPN を通じてパブリックおよびプライベートドメインの DNS クエリを処理でき、リージョン間の自動フェイルオーバーによりハイブリッドネットワーク環境での高可用性を実現します。
- **[AWS Network Firewall が AWS Transit Gateway アタッチ環境でコンテキスト認識ルールをサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/network-firewall-context-aware-rules/)** — AWS Transit Gateway に接続された AWS Network Firewall がコンテキスト認識ルールをサポートし、IP アドレスの代わりに VPC リソースコンテキストを参照してファイアウォールポリシーを記述できるようになりました。新しいワークロードが追加されても既存のルールが自動的に適用されるため、一貫したセキュリティ制御を容易に維持できます。
- **[AWS Security Hub Network Scanning が Amazon RDS データベースインスタンスのスキャンをサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/security-hub-network-scanning-rds/)** — AWS Security Hub Network Scanning が Amazon RDS DB インスタンスを自動的に検出・スキャンし、インターネットから到達可能なインスタンスを識別するようになりました。パブリックアクセスが設定された RDS インスタンスの到達可能なポートを検出してファインディングを生成し、データベースの露出リスクに対する観測性を向上させます。

## 2026-11-17 · 前日のアップデート

- **[Amazon EBS スナップショットへの追加 KMS キー関連付けをサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/ebs-snapshots-associate-kms-keys/)** — Amazon EBS スナップショットに追加の AWS KMS キーを関連付けられるようになり、再暗号化なしにアカウント間で暗号化済みスナップショットを共有・コピーできるようになりました。これにより、ディザスタリカバリやバックアップのワークフローが簡素化されます。
- **[IAM Identity Center が VPC エンドポイントとネットワークアクセス制御をサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/iam-identity-center-vpc-endpoints/)** — AWS IAM Identity Center が AWS PrivateLink を利用したインターフェイス VPC エンドポイントとネットワークアクセス制御をサポートし、サインインおよび API トラフィックを AWS プライベートネットワーク経由でルーティングできるようになりました。これにより、IAM Identity Center へのトラフィックをプライベートに保ち、アクセス可能なネットワークを制限することが可能です。
- **[Amazon VPC 向けネットワーキング柔軟コスト配分 (FCA) を発表](https://aws.amazon.com/about-aws/whats-new/2026/11/networking-flexible-cost-allocation/)** — Amazon VPC にネットワーキング柔軟コスト配分 (FCA) 機能が追加され、NAT ゲートウェイのデータ処理やデータ転送などの共有ネットワーキングコストを、実際に発生させたリソースごとに分割して把握できるようになりました。これまで AWS Cost and Usage Report では単一の明細として表示されていたため、チームごとの費用配分にカスタムスクリプトや手作業が必要でしたが、今後はリソース単位での正確なコスト把握が可能です。

## 2026-11-14 · 前日のアップデート

- **[Amazon Route 53 がレコードセット保護をサポート開始](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-route-53-record-set-protection/)** — Amazon Route 53 で、ホストゾーン内の重要な DNS レコードへの誤変更を防ぐレコードセット保護機能が追加されました。保護されたレコードへの変更は権限を持つユーザーが保護を解除するまでブロックされるため、従来のように IAM ポリシーにレコードレベルの条件を個別に記述する手間が不要になります。

## 2026-11-13 · 前日のアップデート

- **[Amazon Aurora および RDS が Graviton5 ベースの R9g データベースインスタンスをサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-aurora-rds-postgresql-mysql-mariadb-r9g-instances/)** — AWS Graviton5 ベースの R9g データベースインスタンスが、Amazon Aurora (PostgreSQL・MySQL 互換) および Amazon RDS for PostgreSQL・MySQL・MariaDB で一般提供開始されました。Graviton4 ベースの同等インスタンスと比較して最大 30% の性能向上と最大 22% の価格対性能比の改善を実現し、large から 48xlarge まで 9 つのサイズで利用できます。
- **[Amazon Route 53 Domains が期限切れ・削除済みドメインのセルフサービス復元をサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/route-53-domains-self-service-restore/)** — Amazon Route 53 Domains で、期限切れまたは最近削除されたドメインを AWS Support に依頼することなく、コンソール・AWS CLI・AWS SDK から直接復元できるようになりました。更新忘れや決済手段の期限切れ、誤削除によって失ったドメインと、それに依存するウェブサイト・メール・アプリケーションを迅速に復旧できます。
- **[AWS Cloud WAN が Direct Connect アタッチメントでのルーティングポリシー向け BGP コミュニティをサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/cloud-wan-bgp-community-directconnect/)** — AWS Cloud WAN が Direct Connect アタッチメントでの BGP コミュニティをサポートし、オンプレミスでルーティングの意図をタグ付けして Cloud WAN 内でフィルタリングやパス優先ルールを適用し、コミュニティをオンプレミスルーターに伝播できるようになりました。これにより、以前は Site-to-Site VPN および Connect アタッチメントのみで利用可能だった BGP コミュニティベースのルーティングポリシーが Direct Connect にも拡張され、ハイブリッドネットワークのオーケストレーションが簡素化されます。

## 2026-11-12 · 前日のアップデート

- **[AWS Network Security Manager が AWS European Sovereign Cloud および追加の新リージョンで利用可能に](https://aws.amazon.com/about-aws/whats-new/2026/11/network-security-mgr-eu-sovereign-cloud/)** — AWS Network Security Manager が AWS European Sovereign Cloud リージョンを含む 31 の新しいリージョンで一般提供開始されました。AWS WAF および AWS Shield と連携し、大規模なネットワークセキュリティポリシーの展開と適用を簡素化します。
- **[AWS Cloud WAN が Flow Logs をサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-cloud-wan-flow-logs/)** — AWS Cloud WAN が Flow Logs をサポートし、グローバルネットワーク全体の IP トラフィックを単一の AWS Cloud WAN アカウントから一元的に確認できるようになりました。これにより、複数の VPC・アカウント・リージョンにまたがる VPC Flow Logs を個別に収集する必要がなくなります。
- **[Amazon EKS Auto Mode が Pod のセキュリティグループをサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eks-auto-mode-security-groups-for-pods/)** — Amazon EKS Auto Mode が Pod レベルのセキュリティグループをサポートし、同一ノード上の異なるワークロードに個別の Amazon EC2 セキュリティグループルールを適用できるようになりました。別のノードプールを作成することなく Pod 単位のネットワークレベルのセグメンテーションが可能となり、Amazon RDS や Amazon ElastiCache などセキュリティグループベースのアクセス制御を使用するリソースへ Pod から直接接続できます。

## 2026-11-11 · 前日のアップデート

- **[Amazon EC2 G7 インスタンス、追加リージョンで提供開始](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-g7-additional-regions/)** — Amazon EC2 G7 インスタンスが、欧州 (ロンドン)、アジアパシフィック (ムンバイ、シドニー)、南米 (サンパウロ) リージョンで新たに利用可能になりました。NVIDIA RTX PRO 4500 Blackwell GPU を搭載し、G6 インスタンスと比較して AI 推論性能が最大 4.6 倍、グラフィックス性能が最大 2.1 倍向上しています。
- **[AWS Network Firewall、次世代ファイアウォールポリシーを提供開始](https://aws.amazon.com/about-aws/whats-new/2026/11/network-firewall-launches-ngfw-policy/)** — AWS Network Firewall が新たな次世代ファイアウォール (NGFW) ポリシーモデルを発表し、よりシンプルなポリシー構造と拡張されたルール容量を提供します。ファイアウォール保護と IPS 保護を組み合わせるのではなく階層化することで、セキュリティ態勢を強化しつつポリシー管理を簡素化します。

## 2026-11-10 · 前日のアップデート

- **[Amazon Bedrock AgentCore が Web Search API を提供開始](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-bedrock-agentcore-web-search-api/)** — AWS は Amazon Bedrock AgentCore において、単一の API 呼び出しで Web 検索を実行できる InvokeWebSearch API の一般提供を開始しました。追加リソースの作成不要で、テキスト抜粋・URL・公開日時を含む検索結果をドメインフィルタリングとともに取得できます。
- **[Amazon Route 53 Profiles が VPC あたり複数プロファイルの関連付けをサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/route-53-profiles-multiple-per-vpc/)** — Amazon Route 53 Profiles が 1 つの VPC に複数のプロファイルを関連付ける機能をサポートしました。セキュリティチームの DNS Firewall ルールグループとネットワーク管理チームのプライベートホスティングゾーン・Resolver ルールをそれぞれ独立したプロファイルで管理しながら、同一 VPC に適用できるようになります。
- **[Amazon EKS・ECS・EC2 向けにハードウェア分離された AWS Nitro Sandboxes を提供開始](https://aws.amazon.com/about-aws/whats-new/2026/11/nitro-sandboxes-eks-ecs-ec2/)** — AWS Nitro Sandboxes が Nitro Hypervisor で管理される軽量 VM として利用可能になり、Amazon EKS ポッド・Amazon ECS タスク・スタンドアロン VM にハードウェアレベルの分離境界を提供します。単一の EC2 インスタンス上でネイティブに近いパフォーマンスを維持しながら、信頼できないマルチテナントや規制対象ワークロードを安全に実行できます。

## 2026-11-07 · 前日のアップデート

- **[Amazon MSK Replicator が AWS GovCloud (US-East, US-West) リージョンで利用可能に](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-msk-replicator-additional-aws-regions)** — Amazon MSK Replicator が AWS GovCloud (US-East, US-West) リージョンで利用可能になりました。Amazon MSK クラスター間、またはオンプレミスや他のクラウドプロバイダーの外部 Apache Kafka クラスターから Amazon MSK Provisioned クラスターへのストリーミングデータの自動レプリケーションが可能となり、カスタムレプリケーションインフラを管理することなく、復元力の高いストリーミングアプリケーションを構築できます。

## 2026-11-06 · 前日のアップデート

- **[AWS Interconnect - last mile、米国 Northern Virginia に新メトロを追加](https://aws.amazon.com/about-aws/whats-new/2026/11/interconnect-last-mile-northern-virginia/)** — AWS Interconnect - last mile が米国 Northern Virginia に新しいメトロを追加し、New York に続く 2 番目の提供拠点となりました。各接続はデフォルトで物理的に分離された 2 拠点と 4 つの冗長リンクでプロビジョニングされ、Direct Connect ポイントまで 99.99% の可用性 SLA が提供されます。
- **[AWS Network Load Balancer が AWS Phoenix ローカルゾーンで利用可能に](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-nlb-available-phx-local-zone/)** — AWS Network Load Balancer が Phoenix ローカルゾーン (us-west-2-phx-2a) で直接作成できるようになりました。これまでは親リージョンのアベイラビリティーゾーンにロードバランサーを配置する必要がありましたが、今回の提供開始によりトラフィックをローカルゾーン内で処理でき、地延時間の短縮とネットワークパスの簡素化が実現します。
- **[AWS Security Hub ネットワークスキャニングが AWS GovCloud (US) で利用可能に](https://aws.amazon.com/about-aws/whats-new/2026/11/security-hub-network-scanning-govcloud/)** — AWS Security Hub のネットワークスキャニング機能が AWS GovCloud (US) でサポートされました。セキュリティグループルールやルーティングテーブルに基づく理論的な到達可能性ではなく、インターネットから実際にアクセス可能なパブリック IP、仮想マシン、ロードバランサー、オープンポートを直接検出し、より正確な攻撃対象領域の把握が可能になります。
- **[AWS WAF AI トラフィックマネタイゼーションが Stripe による法定通貨払い出しをサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-waf-stripe-fiat-payouts/)** — AWS WAF の AI トラフィックマネタイゼーション機能が Stripe と統合され、パブリッシャーや API プロバイダーが AI ボット・エージェントからのステーブルコイン決済を現地通貨で Stripe 残高に直接受け取れるようになりました。暗号資産ウォレットを管理することなくエージェントアクセスをマネタイズでき、既存の料金ポリシーやエージェントポリシーはそのまま利用できます。

## 2026-11-05 · 前日のアップデート

- **[AWS Interconnect - Last Mile、Equinix とのプレビューを発表](https://aws.amazon.com/about-aws/whats-new/2026/11/interconnect-last-mile-preview-equinix/)** — AWS Interconnect - Last Mile が Equinix との連携でプレビュー公開され、Equinix のグローバル 282 拠点のインフラを数クリックで AWS に接続できるようになりました。クロスコネクトの発注やルーター設定が不要な管理型プライベート接続を提供し、AWS Management Console で リージョン・帯域幅・Direct Connect Gateway・Equinix Fabric One プロジェクト ID を選択するだけでセットアップが完了します。
- **[Amazon EC2 および VPC コンソール、全リソースタイプの関連リソース表示に対応](https://aws.amazon.com/about-aws/whats-new/2026/11/ec2-vpc-related-resources-all-types/)** — Amazon EC2、Amazon VPC、AWS Global View のコンソールが、EC2 インスタンス・Amazon EBS ボリューム・起動テンプレート・Auto Scaling グループ・サブネット・ラウティングテーブルなど、すべてのリソースタイプで関連リソースを表示できるようになりました。従来はセキュリティグループのみに限定されていた機能が全リソースタイプに拡張され、関連リソースタブがコンソールツールバーに移動してアクセスしやすくなっています。

## 2026-11-03 · 前日のアップデート

- **[Amazon CloudFront が AWS Service Quotas によるセルフサービスの上限引き上げをサポート](https://aws.amazon.com/about-aws/whats-new/2026/11/cloudfront-self-service-quotas/)** — Amazon CloudFront が AWS Service Quotas と統合され、ディストリビューションやキャッシュポリシー、オリジン、代替ドメイン名など 28 個のクォータをコンソールまたは API から直接確認・モニタリング・増加申請できるようになりました。AWS Business Support 以上のお客様は、公開されたしきい値内のクォータ引き上げリクエストが自動承認されるため、サポートケースを開く必要がなくなります。

## 2026-10-31 · 前日のアップデート

- **[Amazon CloudFront がビューワー ISP およびポスト量子 TLS 詳細情報の提供を開始](https://aws.amazon.com/about-aws/whats-new/2026/10/cloudfront-viewer-isp-post-quantum-visbility/)** — Amazon CloudFront が 2 つの新しいオプションヘッダーをオリジンに転送できるようになりました。CloudFront-Viewer-ISP ヘッダーでリクエスト元の ISP を把握でき、CloudFront-Viewer-TLS-Details ヘッダーでポスト量子暗号 (PQC) の使用有無を含む TLS 接続の暗号化方式を確認できます。
- **[AWS WAF が Amazon CloudFront ディストリビューション向け自動 SDK 統合を発表](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-waf-automatic-sdk-integration-amazon-cloudfront/)** — AWS WAF が Amazon CloudFront ディストリビューション向けに、アプリケーションコードやビルドプロセスを変更することなく AWS WAF JavaScript SDK のスクリプトタグを自動挿入する機能を発表しました。これにより、Bot Control・アカウント乗っ取り防止 (ATP)・アカウント作成不正防止 (ACFP) の 3 つのマネージドルールグループに必要なクライアント側シグナルを手動での対応なしに提供できます。

## 2026-10-30 · 前日のアップデート

- **[Amazon ElastiCache Serverless のパブリックエンドポイントが AWS GovCloud (US) で利用可能に](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-elasticache-serverless-public-endpoints-govcloud/)** — Amazon ElastiCache Serverless for Valkey が AWS GovCloud (US) リージョンでパブリックエンドポイントをサポートしました。VPN やバスチョンホスト、SSH トンネルなしで VPC 外部のアプリケーションからキャッシュに直接接続でき、すべての接続は TLS 1.3 による IAM 認証で保護されます。

## 2026-10-29 · 前日のアップデート

- **[Amazon EKS Auto Mode が Kubernetes Gateway API をサポート開始](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-eks-auto-mode-kubernetes-gateway-api/)** — Amazon EKS Auto Mode が Kubernetes Gateway API をサポートし、別途コントローラーをインストールすることなく Gateway および HTTPRoute リソースでアプリケーションロードバランシングを設定できるようになりました。HTTP・gRPC ルーティングやマルチチーム環境向けの名前空間をまたいだトラフィックルーティングなど、次世代の Kubernetes トラフィック管理標準を EKS Auto Mode が AWS インフラを自動プロビジョニングしながらサポートします。

## 2026-10-28 · 前日のアップデート

- **[Amazon Aurora Serverless が最大 384 ACU をサポート](https://aws.amazon.com/about-aws/whats-new/2026/10/aurora-serverless-supports-384-acu/)** — Amazon Aurora Serverless の Aurora PostgreSQL 互換エディションで、最大 384 ACU (Aurora Capacity Unit) がサポートされ、従来の 256 ACU から 50% 増加しました。単一データベースで最大 768 GiB のメモリまでスケールアップできるため、バースト的なトラフィックと長いアイドル時間を持つエージェンティック AI アプリケーションに特に適しています。

## 2026-10-24 · 前日のアップデート

- **[AWS Transit Gateway および AWS Cloud WAN が 1:1 NAT をサポート](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-transit-gateway-cloud-wan-1-1-nat/)** — AWS Transit Gateway と AWS Cloud WAN が、Regional Private NAT Gateway との統合により、アタッチメント上で直接マネージド 1:1 NAT をサポートするようになりました。これにより、同一の IP アドレス範囲を持つプライベートネットワーク間で、IP の再割り当てや NAT アプライアンスの導入なしに通信が可能となり、M&A やパートナーネットワーク接続時の CIDR 重複問題を解消できます。

## 2026-10-23 · 前日のアップデート

- **[AWS Direct Connect、インド・バンガロールで 100G 拡張を発表](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-direct-connect-100g-bangalore/)** — インド・バンガロール近郊の Netmagic DC2 データセンターにある既存の AWS Direct Connect ロケーションで、100 Gbps 専用接続がサポートされました。これにより、中国を除くすべてのパブリック AWS リージョン、AWS GovCloud リージョン、および AWS Local Zones へのプライベート直接接続が可能になります。
- **[AWS、Megaport との AWS Interconnect ラストマイルプレビューを発表](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-announces-AWS-interconnect-last-mile-megaport-preview/)** — AWS と Megaport が共同で、支社・データセンター・リモートロケーションを数クリックで AWS に接続できる完全マネージド型の接続サービス「AWS Interconnect - last mile」のプレビューを開始しました。31 か国 1,200 以上のデータセンターをカバーする Megaport の SDN と AWS マネジメントコンソールを組み合わせることで、ネットワーク設定の複雑さを大幅に軽減できます。
- **[AWS Transform、新規ネットワーク構築とセキュリティグループの最新化に対応](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-transform-new-networks/)** — AWS Transform が、既存ネットワークの移行・最新化に加え、新規ネットワークをゼロから構築する機能と、オンプレミスのアクセスルールを最適化されたセキュリティグループに変換して既存 VPC へデプロイする機能をサポートしました。いずれの方法でも、AWS のモ범事例に沿った安全でスケーラブルなネットワーク基盤を実現できます。

## 2026-10-22 · 前日のアップデート

- **[AWS Direct Connect、英国マンチェスターで 100G 拡張を発表](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-direct-connect-100g-manchester/)** — AWS は、英国マンチェスター近郊の Equinix MA3 データセンターにある既存の AWS Direct Connect ロケーションで、MACsec 暗号化に対応した 10 Gbps および 100 Gbps 専用接続を拡張しました。これにより、英国で 100 Gbps MACsec をサポートする Direct Connect ロケーションは 3 か所となり、中国を除くすべてのパブリック AWS リージョン、AWS GovCloud リージョン、および AWS Local Zones へのプライベート接続が可能になります。
- **[AWS Network Firewall が Route 53 Resolved IP Validation をサポート](https://aws.amazon.com/about-aws/whats-new/2026/10/network-firewall-route-53-ip-validation/)** — AWS Network Firewall が Route 53 Resolved IP Validation をサポートし、ドメインベースのフィルタリングを HTTP/HTTPS だけでなく SFTP や SSH などのプロトコルにも拡張しました。接続先 IP アドレスが VPC の Amazon Route 53 VPC Resolver を通じて解決されたものかを検証することで、ドメインルールの回避や SNI スプーフィングによるセキュリティギャップを解消します。
- **[Amazon WorkSpaces、AI エージェントのエンタープライズクラウドデスクトップへのセキュアなアクセスをインフラ管理負荷を軽減しながら簡素化](https://aws.amazon.com/about-aws/whats-new/2026/10/workspaces-ai-agents-oauth-connection-management)** — Amazon WorkSpaces は、管理型 Model Context Protocol (MCP) サービスの一部として AI エージェントの認証とデスクトップ接続を自動処理するようになり、カスタムコードなしでエージェントをガバナンス済みクラウドデスクトップに接続できます。既存の AWS 認証情報と OAuth 2.0 を使用してセッションを作成でき、ストリーミング URL の生成・ローテーションもサービスが担うため、運用負荷が大幅に軽減されます。

## 2026-10-21 · 前日のアップデート

- **[Amazon ECS Gateway 発表 — ECS サービス向けマネージドイングレスソリューション](https://aws.amazon.com/about-aws/whats-new/2026/10/announcing-amazon-ecs-gateway/)** — AWS は、コンテナ化されたアプリケーションのイングレスネットワーキングを簡素化する Amazon ECS Gateway を発表しました。プラットフォームチームがゲートウェイに組織のネットワーキング標準を一度定義すると、Application Load Balancer (ALB) および関連リソースが自動的にプロビジョニングされ、アプリケーションチームはネットワーキングの専門知識なしにその標準を継承して中央集中式にトラフィックを管理できます。

## 2026-10-17 · 前日のアップデート

- **[Oracle Database@AWS、ODB ピアリングで集約ルートおよびデフォルトルートをサポート](https://aws.amazon.com/about-aws/whats-new/2026/10/oracle-database-aws-aggregate-routes-odb/)** — Oracle Database@AWS (ODB) は、ODB ピアリング設定時に集約ルートおよびデフォルトルート (0.0.0.0/0) のアドバタイズをサポートするようになりました。これにより、新しい Amazon VPC やオンプレミスネットワークを ODB ネットワークに接続する際、CIDR を個別に追加する必要がなくなり、ネットワーク運用が簡素化されます。

## 2026-10-16 · 前日のアップデート

- **[AWS HealthOmics が共有 VPC をサポート開始](https://aws.amazon.com/about-aws/whats-new/2026/10/omics-workflows-shared-vpcs/)** — AWS HealthOmics が AWS Resource Access Manager (RAM) を通じて他の AWS アカウントが管理する Amazon VPC を共有できるようになりました。これにより、組織内の複数アカウントにまたがるサブネットとセキュリティグループを単一の VPC で中央集中式に管理できます。
- **[Amazon CloudFront が VPC オリジンのデュアルスタックサポートを発表](https://aws.amazon.com/about-aws/whats-new/2026/10/cloudfront-vpc-origin-dualstack/)** — Amazon CloudFront が VPC オリジンに対するデュアルスタックサポートを追加し、プライベートサブネット内の ALB・NLB・EC2 インスタンスへ IPv6 トラフィックをエンドツーエンドで配信できるようになりました。オリジンをインターネットに公開することなく、IPv6 アーキテクチャおよびコンプライアンス要件を満たすことが可能です。

## 2026-10-15 · 前日のアップデート

- **[ノードブートストラッピングのための AWS Blockchain Snapshots の発表](https://aws.amazon.com/about-aws/whats-new/2026/10/blockchain-snapshots-node-bootstrapping/)** — AWS は、Ethereum および Solana のブロックチェーンノード運用者向けに、事前同期済みのチェーンデータを Amazon S3 にパブリックスナップショットとして提供する Blockchain Snapshots on AWS を発表しました。P2P ネットワーク同期の代わりにスナップショットからノードをブートストラップできるため、AWS 上でノードを運用する際の遅延時間短縮とデータ転送の最適化が期待できます。

## 2026-10-14 · 前日のアップデート

- **[Amazon Route 53 がプレミアムドメインの登録・移管・更新をサポート](https://aws.amazon.com/about-aws/whats-new/2026/10/route-53-premium-domains/)** — Amazon Route 53 Domains が、プレミアムドメイン名の検索・登録・移管・更新・復元を直接サポートするようになりました。これにより、短くて覚えやすい高需要のプレミアムドメインを他のレジストラを使わずに Route 53 だけで一元管理できます。

## 2026-10-13 · 前日のアップデート

- **[Amazon CloudFront が AWS Lambda Web Functions をオリジンとしてサポート](https://aws.amazon.com/about-aws/whats-new/2026/10/cloudfront-lambda-web-functions-origin/)** — Amazon CloudFront が AWS Lambda Web Functions をオリジンとしてサポートし、エッジでの TLS 終端・キャッシュ・カスタムドメインを活用した低遅延の Web アプリケーション配信が可能になりました。CloudFront Origin Access Control (OAC) により、Lambda Web Function への直接アクセスを遮断し、セキュリティを強化できます。
- **[Amazon EC2 G7 インスタンスがヨーロッパ（フランクフルト）およびヨーロッパ（ストックホルム）リージョンで提供開始](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-g7-european-regions/)** — NVIDIA RTX PRO 4500 Blackwell Server Edition GPU を搭載した Amazon EC2 G7 インスタンスが、ヨーロッパ（フランクフルト）およびヨーロッパ（ストックホルム）リージョンで利用可能になりました。G7 インスタンスは G6 と比較して AI 推論性能が最大 4.6 倍、グラフィックス性能が最大 2.1 倍向上しており、AI モデルのデプロイや GPU アクセラレーションワークロードに活用できます。
- **[AWS Lambda が Lambda Web Functions を発表](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-web-functions/)** — AWS Lambda は、コードがポートをリッスンして HTTP リクエストを直接処理する新しいサーバーレスコンピューティングプリミティブ、Lambda Web Functions を発表しました。Express や Hono などの既存フレームワークをアダプターなしでそのまま利用でき、AI 推論エンドポイントや SSR Web アプリ、ストリーミング API などのワークロードをサポートし、アイドル CPU 時間ではなくアクティブ CPU 時間に基づいて課金されます。

## 2026-10-10 · 前日のアップデート

- **[Amazon EC2 R8gd インスタンスが追加リージョンで利用可能に](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-ec2-r8gd-thf/)** — Amazon EC2 R8gd インスタンスが AWS European Sovereign Cloud (ドイツ) リージョンで新たに利用可能になりました。 AWS Graviton4 プロセッサを搭載し、最大 11.4 TB の NVMe SSD ローカルストレージと最大 50 Gbps のネットワーク帯域幅を提供し、高速・低レイテンシのローカルストレージを必要とするアプリケーションに最適です。
- **[Amazon EC2 R8g インスタンスが追加リージョンで利用可能に](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-ec2-r8g-instances-thf/)** — Amazon EC2 R8g インスタンスが AWS European Sovereign Cloud (ドイツ) リージョンで利用可能になりました。 AWS Graviton4 プロセッサを搭載し、Graviton3 ベースのインスタンスと比較して最大 30% 優れたパフォーマンスを発揮し、データベースやインメモリキャッシュ、リアルタイムビッグデータ分析などのメモリ集約型ワークロードに適しています。
- **[Amazon SageMaker Unified Studio がカスタム Tooling ブループリントをサポート](https://aws.amazon.com/about-aws/whats-new/2026/10/sagemaker-custom-tooling-blueprints/)** — Amazon SageMaker Unified Studio がカスタム Tooling ブループリントをサポートし、ドメイン管理者が独自の AWS CloudFormation テンプレートを使用してプロジェクト環境の基盤を定義できるようになりました。 IAM ロール名の命名規則やカスタム権限境界など、組織固有の要件に合わせた環境構成が可能です。

## 2026-10-09 · 前日のアップデート

- **[AWS Network Firewall がコンテナ属性フィルターにワイルドカードサポートを追加](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-network-firewall-container-attributes-wildcard)** — AWS Network Firewall が Amazon EKS および Amazon ECS のコンテナ属性ベースの検査フィルターでワイルドカードマッチングをサポートしました。app=payments-* のようなパターン 1 つで複数のコンテナワークロードのバリアントを単一ルールでカバーでき、ルール管理が簡素化されます。
- **[Amazon EC2 C8gb インスタンスが追加リージョンで一般提供開始](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-ec2-c8gb/)** — AWS Graviton4 プロセッサーを搭載した Amazon EC2 C8gb インスタンスが、米国東部 (オハイオ)、米国西部 (北カリフォルニア)、EU (フランクフルト、アイルランド、パリ、ストックホルム)、アフリカ (ケープタウン) の各リージョンで新たに利用可能になりました。最大 300 Gbps の EBS 帯域幅と 160 万 IOPS を提供し、同サイズの Graviton4 ベースインスタンスと比較して高いブロックストレージ性能を実現しています。

## 2026-10-08 · 前日のアップデート

- **[AWS Config が 77 個の新しいリソースタイプをサポート](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-config-new-resource-types)** — AWS Config が Amazon EC2、Amazon S3 Files、Amazon Q Business などの主要サービスにわたる 77 個の新しいリソースタイプのサポートを追加しました。全リソースタイプの記録を有効にしている場合は自動的に追跡され、Config ルールおよび Config アグリゲーターでも利用できるため、AWS 環境の監査とコンプライアンスのカバレッジがさらに拡大します。

## 2026-10-07 · 前日のアップデート

- **[AWS Certificate Manager が AWS PrivateLink 経由の ACME 証明書発行をサポート](https://aws.amazon.com/about-aws/whats-new/2026/10/AWS-Certificate-Manager-ACME-Privatelink)** — AWS Certificate Manager (ACM) が AWS PrivateLink を介した ACME パブリック証明書の発行をサポートし、TLS 証明書のリクエストと更新を AWS ネットワーク内のプライベートパスで処理できるようになりました。VPC インターフェイスエンドポイントを作成するだけで、既存の ACME クライアントへの変更は不要です。

## 2026-10-06 · 前日のアップデート

- **[AWS IAM Identity Center が Identity Store のネットワークアクセス制御をサポート](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-identity-store-network-controls/)** — AWS IAM Identity Center が、ユーザーとグループを管理する Identity Store に対するネットワークアクセス制御をサポートしました。リクエストの送信元ネットワークに基づいて Identity Store API および SCIM API へのアクセスを制限でき、ユーザープロビジョニングや外部 ID プロバイダー連携のセキュリティを強化できます。
- **[AWS Client VPN がデバイスポスチャ評価をサポート](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-client-vpn-device-posture/)** — AWS Client VPN がデバイスポスチャ評価をサポートし、接続するユーザーのデバイスがセキュリティおよびコンプライアンス要件を満たしているかを確認してからネットワークアクセスを許可できるようになりました。CrowdStrike、Jamf、JumpCloud との統合により、デバイスのセキュリティシグナルを自動評価し、信頼済みのデバイスのみが AWS リソースにアクセスできるよう制御できます。

## 2026-10-03 · 前日のアップデート

- **[Amazon ECS が Amazon VPC Lattice を使用したブルー/グリーン・線形・カナリアデプロイをサポート](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-ecs-vpc-lattice-blue-green-deployments)** — Amazon ECS が Amazon VPC Lattice を使用するサービスに対して、ブルー/グリーン・線形・カナリアのデプロイ戦略をネイティブサポートしました。VPC 間およびアカウント間のサービス通信に VPC Lattice を活用するアプリケーションで、ECS から直接トラフィックシフトを制御しながら安全にアップデートを展開できます。
- **[AgentCore Gateway が VPC エンドポイント向けプライベート TLS 証明書をサポート](https://aws.amazon.com/about-aws/whats-new/2026/10/agentcore-gateway-private-tls-vpc/)** — Amazon Bedrock AgentCore Gateway が、MCP・OpenAPI・HTTP プロキシターゲットに対してプライベート CA (認証局) が署名した TLS 証明書をサポートしました。中間の Application Load Balancer を必要とせず、Amazon VPC Lattice を利用したプライベートエンドポイントへ直接セキュアに接続できるため、VPC 内のプライベート接続構成が簡素化されます。

## 2026-10-02 · 前日のアップデート

- **[Amazon Redshift がデータレイクへのリージョン間クエリをサポート](https://aws.amazon.com/about-aws/whats-new/2026/10/redshift-cross-Region-queries-for-data-lake)** — Amazon Redshift が別の AWS リージョンにある Amazon S3 データレイクテーブルへのクエリをサポートしました。Enhanced VPC ルーティングにより、S3 と Redshift 間のクエリトラフィックは VPC 内に留まり、グローバルに分散したデータを扱う企業やセキュリティ要件の厳しいお客様に適しています。
- **[Route 53 Global Resolver および DNS Firewall の DNS 分析とインサイト機能を発表](https://aws.amazon.com/about-aws/whats-new/2026/10/route-53-dns-analytics-insights/)** — Route 53 Global Resolver と DNS Firewall が Amazon CloudWatch のネイティブ統合を通じて DNS 分析とインサイト機能を提供するようになりました。ネットワーク管理者やセキュリティチームは DNS クエリパターンの完全な観測性を得られ、DNS Firewall ルールの効果監視や異常検知、パフォーマンス最適化が可能になります。
- **[Amazon Kinesis Video Streams が AWS PrivateLink による VPC エンドポイントをサポート](https://aws.amazon.com/about-aws/whats-new/2026/09/kinesis-video-streams-vpc-privatelink/)** — Amazon Kinesis Video Streams が AWS PrivateLink を利用したインターフェイス VPC エンドポイントをサポートし、コントロールプレーンおよびビデオ取り込み・再生のデータプレーン全体でトラフィックが AWS ネットワーク内に留まるようになりました。厳格なセキュリティ・コンプライアンス・ネットワーク分離要件を持つお客様は、インターネットゲートウェイや NAT デバイス、パブリック IP アドレスなしにビデオの取り込み・保存・再生が可能です。

## 2026-10-01 · 前日のアップデート

- **[AWS CLI が Agent Toolkit for AWS の一括スキル更新とバージョン確認をサポート](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-cli-agent-toolkit-update-skill/)** — AWS CLI に Agent Toolkit for AWS 向けの 2 つの新しいコマンドが追加され、インストール済みスキルのバージョンをレジストリと比較したり、単一コマンドで一括更新したりできるようになりました。これにより、15,000 以上の AWS API に対応するエージェントスキルを効率的に最新状態に保つことができます。
- **[AWS Parallel Computing Service がスケーリングログをサポート](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-pcs-scaling-logs/)** — AWS Parallel Computing Service (AWS PCS) がスケーリングログをサポートし、クラスター内のコンピュートノードグループのスケーリング状態変化を記録できるようになりました。インスタンスの起動、ノード登録、スケールダウン、起動失敗の原因などを追跡でき、スケーリング問題のトラブルシューティングが容易になります。
- **[AWS Transfer Family が SFTP コネクタのクォータ増加を最大 1,000 件まで自動承認](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-transfer-family-sftp-connector-quota-1000/)** — AWS Transfer Family が SFTP コネクタのクォータ増加リクエストを AWS アカウントおよびリージョンごとに最大 1,000 件まで自動承認するようになり、手動承認を待たずにファイル転送規模を拡張できるようになりました。自動承認はサービス管理型および Amazon VPC Lattice エグレスを使用するコネクタの両方に適用されます。

## 2026-09-30 · 前日のアップデート

- **[AWS DataSync が共有 VPC をサポート開始](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-datasync-shared-vpcs/)** — AWS DataSync が AWS Resource Access Manager (RAM) を通じて共有 VPC をサポートし、中央アカウントで管理された共有サブネットと VPC エンドポイントを使ったプライベートなデータ転送が可能になりました。これにより、アカウントごとに個別の DataSync VPC エンドポイントを作成する必要がなくなり、運用負荷が軽減されます。
- **[Amazon ElastiCache Serverless for Valkey がパブリックエンドポイントをサポート](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-elasticache-serverless-public-endpoints/)** — Amazon ElastiCache Serverless for Valkey がパブリックエンドポイントをサポートし、VPN やバスティオンホスト、SSH トンネルなしにインターネット経由でキャッシュへ直接接続できるようになりました。VPC の設定やインフラのプロビジョニングが不要で、1 分以内に作成できるため、迅速なプロトタイピングや AWS 外のワークロードへのキャッシュ追加に適しています。
- **[Amazon Route 53 Resolver DNS Firewall の Palo Alto Networks Advanced DNS Security サポートが一般提供 (GA) 開始](https://aws.amazon.com/about-aws/whats-new/2026/09/route-53-dns-firewall-panw-dns-security-generally-available)** — Amazon Route 53 Resolver DNS Firewall が Palo Alto Networks (PANW) Advanced DNS Security との統合を 32 の AWS リージョンで一般提供開始し、別途ファイアウォールを導入したり VPC 設定を変更したりすることなく、VPC 内から直接悪意のある DNS トラフィックを検出・ブロックできるようになりました。C&C、マルウェア、フィッシング、新規登録ドメインなどの DNS 脅威保護を Route 53 DNS Firewall を通じてネイティブに適用できます。

## 2026-09-26 · 前日のアップデート

- **[AWS IAM アウトバウンド ID フェデレーション、OIDC ディスカバリー向けインターフェイス VPC エンドポイントをサポート](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-sts-vpc-oidc/)** — AWS IAM アウトバウンド ID フェデレーションが AWS PrivateLink を介したインターフェイス VPC エンドポイントをサポートし、OIDC ディスカバリーメタデータおよび JWKS 検証キーエンドポイントへパブリックインターネットを経由せずに VPC 内からアクセスできるようになりました。これにより、外部サービスにアクセスする AWS ワークロードが短期 JWT をより安全に取得できます。

## 2026-09-25 · 前日のアップデート

- **[AWS Network Security Manager が米国東部 (バージニア北部) リージョンで一般提供開始](https://aws.amazon.com/about-aws/whats-new/2026/09/network-security-manager-us-east-va/)** — AWS Network Security Manager が正式リリースされ、AWS WAF および AWS Shield Advanced のファイアウォール・DDoS 保護ポリシーを AWS 組織全体に一貫して適用できるようになりました。常時稼働のセキュリティ自動化機能により大規模なポリシー管理が簡素化され、今後は AWS Network Firewall のサポートも追加される予定です。
- **[スケーラブルな LLM 推論のための Amazon SageMaker HyperPod Inference Gateway](https://aws.amazon.com/about-aws/whats-new/2026/09/sagemaker-hyperpod-inference-gateway/)** — Amazon SageMaker HyperPod Inference Gateway は Kubernetes ネイティブの GPU 対応ルーティングシステムで、ラウンドロビン型ロードバランシングをリアルタイムの推論シグナル駆動ルーティングに置き換え、初回トークンの遅延時間を最大 82%、p99 TTFT を最大 97〜98% 削減します。既存の SageMaker HyperPod インフラに EKS マネージドアドオンとして追加でき、アプリケーションの変更は不要です。
- **[Amazon GameLift Servers が 5 つの新リージョンと 8 つの Local Zone で利用可能に](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-gamelift-servers-region-expansion-2026)** — Amazon GameLift Servers が 5 つの新しい AWS リージョンと 8 つの AWS Local Zone に拡張され、ラテンアメリカ・東南アジア・ヨーロッパ・中東・南アジアのプレイヤー近くにゲームサーバーフリートを展開できるようになりました。地理的距離による遅延時間の課題を軽減し、マルチプレイヤーゲームの体験向上に貢献します。

## 2026-09-24 · 前日のアップデート

- **[Amazon EMR on EKS が IPv6 Amazon EKS クラスターをサポート開始](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-emr-eks-ipv6-support)** — Amazon EMR on EKS が IPv6 Amazon EKS クラスター上でのワークロード実行をサポートしました。大規模な Apache Spark および Apache Flink ワークロードを IPv6 の広大なアドレス空間を活用して実行できるようになり、IP アドレス枯渇の問題を解消できます。

## 2026-09-23 · 前日のアップデート

- **[Amazon Route 53 Resolver が第 2 世代 AWS Outposts ラックで一般提供開始](https://aws.amazon.com/about-aws/whats-new/2026/09/route-53-resolver-gen2-outposts/)** — Amazon Route 53 Resolver が第 2 世代 AWS Outposts で一般提供開始となり、Outpost 上のワークロードからの DNS クエリをローカルで直接解決することで、遅延時間の短縮と Service Link への依存排除を実現します。また、Service Link の切断中もキャッシュされた DNS レコードを保持し、継続的な DNS 解決を保証します。

## 2026-09-22 · 前日のアップデート

- **[Amazon EVS が FedRAMP Class C の対象範囲に追加](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-evs-fedramp-class-c/)** — Amazon Elastic VMware Service (EVS) が、米国の全リージョンで FedRAMP Class C（旧 Moderate ベースライン）の対象範囲に追加されました。これにより、米国政府機関および関連顧客は、Amazon VPC 内の EC2 ベアメタルインスタンス上で VMware Cloud Foundation (VCF) を実行する際に、標準化されたセキュリティ認証要件を満たすことができます。

## 2026-09-19 · 前日のアップデート

- **[Amazon ECS Express Mode が AWS Graviton (ARM64) ワークロードをサポート](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-ecs-express-mode-arm-architecture/)** — Amazon ECS Express Mode が ARM64 CPU アーキテクチャをサポートし、AWS Graviton ベースのコンピューティングに ARM コンテナイメージを簡単にデプロイできるようになりました。x86 インスタンスと比較して最大 40% 優れた価格性能比を実現でき、ネットワーキングやロードバランシングなどのインフラ設定は ECS Express Mode が自動的に処理します。
- **[AWS RTB Fabric が設定可能な Availability Zone アフィニティをサポート](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-rtb-fabric-configurable-availability-zone-affinity/)** — AWS RTB Fabric がレスポンダーゲートウェイに対して設定可能な Availability Zone (AZ) アフィニティをサポートし、パートナーが自身の AZ またはゲートウェイがまたがる任意の AZ に接続するかを選択できるようになりました。これにより、DSP や SSP などの AdTech 企業は追加費用なしで複数 AZ にわたる入札システムのインフラ効率を向上させることができます。
- **[AWS PrivateLink がネットワークセグメントにアクセスするためのトンネルエンドポイントを発表](https://aws.amazon.com/about-aws/whats-new/2026/9/privatelink-tunnel-endpoint/)** — AWS PrivateLink が新しいタイプの VPC エンドポイントである「トンネル」エンドポイントを導入し、別の VPC やアカウントのネットワークセグメントにプライベートかつ安全にアクセスできるようになりました。これにより、外部ベンダーなどとリソースを共有する際にリソースごとに個別設定する必要がなくなり、アカウント間の接続構成が大幅に簡素化されます。

## 2026-09-18 · 前日のアップデート

- **[AWS Transfer Family、NLB の背後にある SFTP サーバーでソース IP 保存をサポート](https://aws.amazon.com/about-aws/whats-new/2026/09/transfer-family-sftp-source-ip-nlb/)** — AWS Transfer Family は、VPC ホスト型エンドポイントの SFTP サーバー前段に NLB を配置する際、Proxy Protocol v2 (PPv2) を使用してクライアントのソース IP アドレスを保持できるようになりました。これにより、従来 NLB のプライベート IP に置き換えられていた問題が解消され、IP ベースの監査やアクセス制御、コンプライアンス要件を満たすことが可能です。

## 2026-09-17 · 前日のアップデート

- **[AWS Client VPN が MacOS 27 Golden Gate をサポート](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-client-vpn-macos-golden-gate/)** — AWS Client VPN はクライアントバージョン 6.0 以降で MacOS 27 Golden Gate をサポートするようになりました。既存の MacOS 13.0〜26.0、Windows、Ubuntu-Linux に加え、最新の MacOS でもリモートアクセスが利用可能です。
- **[AWS Step Functions が新しい AWS サービス統合を自動追加 — AWS Lambda MicroVMs を皮切りに](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-step-functions-integrations/)** — AWS Step Functions は、新しい AWS サービスのリリース後数週間以内に AWS SDK 統合を自動的に追加するようになりました。第一弾として AWS Lambda MicroVMs および AWS Lambda Core が対象となり、カスタムコードなしでエージェントワークフローをオーケストレーションできます。

## 2026-09-16 · 前日のアップデート

- **[AWS Direct Connect、専用接続のフラットレート料金を発表](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-direct-connect-announces-flat-rate-pricing/)** — AWS Direct Connect が 10G および 100G 専用接続向けにフラットレート料金オプションを導入しました。大量かつ継続的なデータ転送アウト (DTO) を行うワークロードにおいて、月額コストの予測が容易になります。
- **[Amazon Q Console で自然言語を使って CloudTrail イベントを分析](https://aws.amazon.com/about-aws/whats-new/2026/09/cloudtrail-amazon-q-console/)** — AWS CloudTrail が Amazon Q Console と統合され、自然言語の質問だけで CloudTrail の設定確認、セキュリティ調査、運用トラブルシューティングが行えるようになりました。クエリの記述やログファイルの手動解析が不要になり、セキュリティ監査やコンプライアンス対応が簡素化されます。

## 2026-09-11 · 前日のアップデート

- **[第 2 世代シングルラック AWS Outposts の発表](https://aws.amazon.com/about-aws/whats-new/2026/09/single-rack-aws-outposts/)** — AWS は、第 2 世代シングルラック AWS Outposts の一般提供を発表しました。この 42U の自己完結型ラックは、最大 2,688 vCPU と 100 TB の Amazon EBS ストレージを提供し、スペースおよび電力が制約された環境での低レイテンシーなローカルデータ処理ワークロード向けに、コンピューティング・ストレージ・ネットワーキングを 1 つのユニットに統合しています。
- **[Amazon CloudWatch、合成モニターを使用した TGW リージョン間ピアリングのネットワーク健全性インジケーターをサポート](https://aws.amazon.com/about-aws/whats-new/2026/09/cloudwatch-network-monitoring-tgw-support/)** — Amazon CloudWatch Network Monitoring の合成モニターが、AWS Transit Gateway のリージョン間ピアリング接続を経由するパスに対してネットワーク健全性インジケーター (NHI) をサポートするようになりました。これにより、ネットワーク運用者はパフォーマンス低下の原因が AWS ネットワーク側にあるかどうかを迅速に特定でき、障害の切り分け時間を短縮できます。
- **[AWS Elemental MediaLive が A/B フォレンジックウォーターマーキングをサポート](https://aws.amazon.com/about-aws/whats-new/2026/09/medialive-ab-forensic-watermarking/)** — AWS Elemental MediaLive が A/B フォレンジックウォーターマーキングをサポートし、1 つのチャンネルから視覚的に透明な異なるウォーターマークを持つ 2 つの同期出力バリアントを生成できるようになりました。ダウンストリームのパッケージングおよび CDN インフラがこれらをセッションごとの固有シーケンスに組み合わせ、流出コンテンツの発生源を特定できます。
- **[AWS Storage Gateway が Amazon S3 File Gateway の FIPS 準拠プライベート接続をサポート](https://aws.amazon.com/about-aws/whats-new/2026/09/storage-gateway-fips-privatelink-s3/)** — AWS Storage Gateway が、Amazon S3 File Gateway 向けに AWS PrivateLink 経由の FIPS 140-3 検証済みエンドポイントをサポートするようになりました。これにより、FIPS 準拠のトラフィックをパブリックインターネットを経由せずプライベート AWS ネットワーク内で処理できるため、規制対象ワークロードでの利用が容易になります。
- **[Amazon EVS が追加リージョンで利用可能に](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-evs-available-in-additional-regions/)** — Amazon Elastic VMware Service (Amazon EVS) が、アジアパシフィック (大阪)、アジアパシフィック (台北)、ヨーロッパ (スペイン)、イスラエル (テルアビブ) の各リージョンで新たに利用可能になりました。Amazon EVS は、AWS Nitro を搭載した EC2 ベアメタルインスタンス上で Amazon VPC 内に VMware Cloud Foundation (VCF) 環境を直接実行でき、VMware ワークロードの迅速な AWS への移行を支援します。

## 2026-09-10 · 前日のアップデート

- **[AWS Lambda、Lambda Managed Instances で Graviton5 搭載 EC2 インスタンスをサポート](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-lambda-graviton5-ec2/)** — AWS Lambda の Lambda Managed Instances で、Graviton5 搭載の C9g、C9gd、M9g、M9gd インスタンスがサポートされました。Graviton4 比で最大 25% の性能向上を実現しつつ、インフラ管理不要で EC2 の料金メリットを活用できます。
- **[Amazon EBS Volume Clones、アカウント間のボリュームコピーをサポート](https://aws.amazon.com/about-aws/whats-new/2026/09/ebs-volume-clones-cross-account-copy/)** — Amazon EBS Volume Clones が、アカウント間での EBS ボリュームのコピーと再暗号化をサポートしました。コピー先アカウントの AWS KMS キーで再暗号化しながらボリュームを転送できるため、本番環境と開発環境を別アカウントで管理する組織でも安全にデータを共有できます。
- **[Amazon CloudFront 向け Dynamic Image Transformation に 4 つの新機能を追加](https://aws.amazon.com/about-aws/whats-new/2026/08/dynamic-image-transformation-adds-new-features/)** — Amazon CloudFront 向け Dynamic Image Transformation (DIT) に、カスタムラベル検出を活用したスマートクロップや高度なコンポジション制御、ブラウザ・デバイス別の自動画像最適化など 4 つの新機能が追加されました。スマートフォンからスマート TV まで、あらゆるデバイスに適切なサイズの画像を効率的に配信できます。

## 2026-09-09 · 前日のアップデート

- **[Amazon CloudFront 向け Dynamic Image Transformation に 4 つの新機能を追加](https://aws.amazon.com/about-aws/whats-new/2026/08/dynamic-image-transfromation-adds-new-features/)** — AWS は Amazon CloudFront 向け Dynamic Image Transformation (DIT) に、カスタムラベル検出を活用したスマートクロップ、高度なコンポジション制御、CloudFront のマルチ階層デバイス検出を利用した自動画像最適化など 4 つの新機能を追加しました。スマートフォンからスマート TV まで幅広いデバイスに最適化された画像を配信できるようになり、コンテンツ配信の効率が向上します。

## 2026-09-05 · 前日のアップデート

- **[Amazon EC2 C8g インスタンスが追加リージョンで利用可能に](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-ec2-c8g-instances-additional-regions/)** — Amazon EC2 C8g インスタンスが、AWS アジアパシフィック（台北、ニュージーランド）および AWS GovCloud (US-East) リージョンで新たに利用可能になりました。AWS Graviton4 プロセッサを搭載し、Graviton3 ベースのインスタンスと比較して最大 30% 高いパフォーマンスを発揮し、HPC やバッチ処理、ゲーム、動画エンコードなどのコンピューティング集約型ワークロードに適しています。

## 2026-09-04 · 前日のアップデート

- **[Amazon EC2 P6-B200 インスタンスが AWS アジアパシフィック（ハイデラバード）リージョンで利用可能に](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-ec2-p6-b200-instances-available-asia-pacific-hyderabad)** — NVIDIA Blackwell GPU を搭載した Amazon EC2 P6-B200 インスタンスが、AWS アジアパシフィック（ハイデラバード）リージョンで利用可能になりました。P5en インスタンスと比較して最大 2 倍の AI 学習・推論性能と、最大 3.2 Tbps の EFAv4 ネットワーキングを提供します。
- **[Amazon EC2 P6-B300 インスタンスが AWS アジアパシフィック（ジャカルタ）リージョンで利用可能に](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-ec2-p6-b300-instances-available-asia-pacific-jakarta)** — NVIDIA Blackwell Ultra GPU を 8 基搭載し、6.4 Tbps の EFA ネットワーキングを備えた Amazon EC2 P6-B300 インスタンスが、AWS アジアパシフィック（ジャカルタ）リージョンで利用可能になりました。P6-B200 と比較してネットワーキング帯域幅が 2 倍、GPU メモリが 1.5 倍となり、大規模な基盤モデルの学習・デプロイに適しています。
- **[Amazon CloudFront、定額料金プランの API サポートを発表](https://aws.amazon.com/about-aws/whats-new/2026/09/cloudfront-flat-rate-pricing-plans-api/)** — Amazon CloudFront の定額料金プランが、AWS CLI、SDK、CloudFormation、CDK、または PricingPlanManager API を通じてプログラムで管理できるようになりました。これにより、IaC ワークフローにおいてコンソールでの手動操作なしに定額プランを自動化できます。
- **[AWS Gateway Load Balancer、高速な障害復旧のための TCP Reset をサポート](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-gateway-load-balancer-tcp-reset/)** — AWS Gateway Load Balancer (GWLB) が、ターゲットの異常検知・登録解除時やアイドルタイムアウト時に TCP Reset (RST) パケットを送信する機能をサポートしました。これにより、障害検知と復旧にかかる時間を数分から数秒に短縮できます。
- **[Amazon S3、FIPS エンドポイントへの PrivateLink サポートを開始](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-s3-privatelink-fips-endpoints)** — Amazon S3 が FIPS 140-3 検証済みエンドポイントに対して AWS PrivateLink をサポートしました。セキュリティおよびコンプライアンス要件を持つお客様は、トラフィックを VPC 内に保ちながら FIPS 検証済み暗号化モジュールを使用して S3 に接続できます。
- **[Amazon MemoryDB が AWS GovCloud（米国）リージョンで AWS PrivateLink をサポート](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-memorydb-privatelink/)** — Amazon MemoryDB が AWS GovCloud (US-West) および AWS GovCloud (US-East) リージョンで AWS PrivateLink をサポートしました。インターフェイス VPC エンドポイントを作成することで、パブリックインターネットにトラフィックを公開せずに VPC から MemoryDB へプライベートに接続できます。

## 2026-09-01 · 前日のアップデート

- **[Amazon Redshift が Enhanced VPC Routing 環境で AWS IAM Identity Center 認証をサポート](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-redshift-supports-idc-evr)** — Amazon Redshift が Enhanced VPC Routing (EVR) を設定したプロビジョニングクラスターおよびサーバーレスワークグループで AWS IAM Identity Center 認証をサポートしました。企業の認証情報による SSO アクセスが可能になり、すべてのトラフィックが Amazon VPC を経由して AWS ネットワーク内に留まるため、データ所在地やネットワーク分離の要件を満たすことができます。
- **[Amazon Cognito がユーザープールドメインなしでマシン間認証をサポート](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cognito-get-client-token/)** — Amazon Cognito に新しい GetClientToken API オペレーションが追加され、ユーザープールドメインを設定せずに AWS SDK、CLI、または API から直接マシン間 (M2M) アクセストークンを取得できるようになりました。マイクロサービスや自動化ワークロードにおけるサービス間通信の認証経路が追加され、ネットワーク構成の複雑さを軽減できます。

## 2026-08-29 · 前日のアップデート

- **[Amazon EC2 C8gn インスタンスが AWS ヨーロッパ（パリ）リージョンで利用可能に](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-c8gn-europe-paris/)** — AWS Graviton4 プロセッサを搭載した Amazon EC2 C8gn インスタンスが、AWS ヨーロッパ（パリ）リージョンで利用可能になりました。ネットワーク最適化 EC2 インスタンスの中で最大となる 600 Gbps のネットワーク帯域幅を提供し、C7gn インスタンスと比較して最大 30% のコンピューティング性能向上を実現しています。
- **[Amazon EC2 P6-B300 インスタンスが追加の AWS リージョンで利用可能に](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-p6-b300-instances-available-additional-regions)** — Amazon EC2 P6-B300 インスタンスが、アジアパシフィック（ハイデラバード）および南米（サンパウロ）リージョンで新たに利用可能になりました。6.4 Tbps の EFA ネットワーキングと 300 Gbps の専用 ENA スループットを備え、P6-B200 インスタンスと比較して 2 倍のネットワーキング帯域幅を提供するため、大規模な基盤モデルのトレーニングやデプロイに適しています。

## 2026-08-27 · 前日のアップデート

- **[Amazon EC2 R8id インスタンスが追加の AWS リージョンで利用可能に](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-r8id/)** — Amazon EC2 R8id インスタンスが、アジアパシフィック（ムンバイ、マレーシア、シドニー）、カナダ（中部）、ヨーロッパ（アイルランド、ストックホルム）の各リージョンで利用可能になりました。最大 22.8 TB の NVMe SSD ローカルストレージを備え、R6id と比較して最大 43% 高いパフォーマンスを発揮し、インメモリデータベースやリアルタイムビッグデータ分析などのメモリ集約型ワークロードに適しています。
- **[Amazon EC2 C8id および M8id インスタンスが追加の AWS リージョンで利用可能に](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-c8id-m8id-aws-regions/)** — Amazon EC2 C8id インスタンスはアジアパシフィック（シドニー）とカナダ（中部）、M8id インスタンスはアジアパシフィック（ムンバイ）とカナダ（中部）で新たに利用可能になりました。両インスタンスとも最大 22.8 TB のローカル NVMe SSD ストレージを備え、前世代の第 6 世代インスタンスと比較して最大 43% 高いコンピューティングパフォーマンスと 3.3 倍のメモリ帯域幅を提供します。

## 2026-08-26 · 前日のアップデート

- **[AWS Batch が Amazon ECS Managed Instances をサポート開始](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-batch-on-ecs-managed-instances/)** — AWS Batch が新しいコンピューティングオプションとして Amazon ECS Managed Instances (ECS MI) をサポートし、GPU アクセラレーテッドおよびコンピューティング集約型のバッチワークロードを AWS マネージドインフラで実行できるようになりました。AMI の更新、セキュリティパッチ適用、インスタンスのライフサイクル管理を AWS が自動的に処理するため、お客様による Amazon EC2 インフラの運用負担が軽減されます。
- **[AWS Lambda MicroVMs が AWS PrivateLink をサポート開始](https://aws.amazon.com/about-aws/whats-new/2026/08/lambda-microvms-supports-privatelink)** — AWS Lambda MicroVMs が AWS PrivateLink をサポートし、Amazon VPC リソースからパブリックインターネットを経由せずに Lambda MicroVMs へプライベート接続できるようになりました。金融、医療、政府機関など規制の厳しい業界のワークロードが、厳格なネットワーク分離要件を満たすことが可能になります。

## 2026-08-22 · 前日のアップデート

- **[Amazon EC2 C8gd、M8gd、R8gd インスタンスが追加の AWS リージョンで利用可能に](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-c8gd-m8gd/)** — Amazon EC2 C8gd、M8gd、R8gd インスタンスが、アジアパシフィック（シンガポール）、メキシコ（中部）、アジアパシフィック（メルボルン）、ヨーロッパ（チューリッヒ）などの追加リージョンで利用可能になりました。 AWS Graviton4 プロセッサを搭載し、最大 11.4 TB のローカル NVMe SSD ストレージを備え、Graviton3 ベースのインスタンスと比較して最大 30% 高いパフォーマンスを提供します。

## 2026-08-21 · 前日のアップデート

- **[ラスベガス（ネバダ州）に新しい AWS Local Zone が一般提供開始](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-local-zones-las-vegas-nevada/)** — AWS は米国ネバダ州ラスベガスに新しい AWS Local Zone を一般提供開始しました。この Local Zone は Amazon EC2 C7i/M7i/R7i/C8gn インスタンス、Amazon EBS、Amazon ECS、Amazon EKS、Application Load Balancer、AWS Direct Connect をサポートし、大都市圏のユーザーに低レイテンシーのコンピューティングおよびネットワーキングサービスを提供します。
- **[Amazon EC2 P6-B300 インスタンスがアジアパシフィック（ソウル）リージョンで利用可能に](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-p6-b300/)** — Amazon EC2 P6-B300 インスタンスがアジアパシフィック（ソウル）リージョンで利用可能になりました。6.4 Tbps の EFA ネットワーキングと 300 Gbps の専用 ENA スループットを備え、P6-B200 比で 2 倍のネットワーキング帯域幅を提供するため、大規模な基盤モデルや LLM のトレーニング・推論ワークロードに適しています。
- **[Amazon CloudFront が Amazon S3 Multi-Region Access Points の Origin Access Control（OAC）をサポート](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cloudfront-oac-s3-mrap)** — Amazon CloudFront が Amazon S3 Multi-Region Access Points（MRAP）に対する Origin Access Control（OAC）をサポートしました。これにより、顧客は SigV4a 署名を手動で処理することなく、指定した CloudFront ディストリビューションからのみ MRAP オリジンへのアクセスを制限でき、グローバル分散コンテンツ配信のセキュリティと運用性が向上します。
- **[AWS Direct Connect がインバウンドプレフィックス制御と大規模プレフィックススケールをサポート](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-direct-connect-new-prefix-controls)** — AWS Direct Connect にインバウンドプレフィックス制御機能が追加され、プライベートおよびトランジット仮想インターフェース（VIF）で IPv4・IPv6 それぞれ最大 1,000 個のルートプレフィックスを許可できるようになりました。従来の上限 100 個による経路要約などの回避策が不要となり、大規模なオンプレミスネットワーク環境での運用が大幅に簡素化されます。

## 2026-06-30 · 日次アップデート

- **[Amazon MWAA Serverless が共有 VPC 構成をサポート](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-mwaa-serverless-vpc/)** — Amazon MWAA Serverless が AWS RAM 経由で共有された VPC サブネットをサポートするようになりました。これにより、共有 VPC 環境でのワークフロー作成をブロックしていたバリデーションエラーが解消されます。マルチアカウントのランディングゾーンアーキテクチャで集中型ネットワーキングを採用している組織が、MWAA Provisioned 環境と同様に、共有サブネット上に MWAA Serverless ワークフローをデプロイできるようになります。

## 2026-06-23 · 日次アップデート

- **[AWS Network Firewall がデフォルトのドロップアクションを更新し、接続信頼性を向上](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-network-firewall-updates-default-drop-action)** — 新しい AWS Network Firewall ポリシーのデフォルトステートフルアクションが、双方向の「Application drop established」からサーバー方向のみに変更されました。これにより、以前のデフォルト設定が正当なサーバーからクライアントへの TCP トラフィックを自動的にブロックしていた問題が解消され、接続の信頼性が向上します。
