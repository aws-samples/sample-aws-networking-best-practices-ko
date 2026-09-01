---
hide:
  - toc
---
# AWS Networking & Content Delivery ブログ

[AWS Networking & Content Delivery Blog](https://aws.amazon.com/blogs/networking-and-content-delivery/)（英語）の記事を毎週金曜日に、最近の投稿を中心に要約します。原文は各項目のリンクをご確認ください。最新の項目が上部に表示されます。

<!-- NEWS:INSERT -->

## 2026-09-01 · 週次まとめ

- **[VPC Encryption Controls を使った接続パターン全体での転送中暗号化の実装](https://aws.amazon.com/blogs/networking-and-content-delivery/implementing-encryption-in-transit-across-connectivity-patterns-with-vpc-encryption-controls/)** — VPC Encryption Controls を活用して、Amazon EC2 インスタンスを含む多様なネットワークパスで転送中の暗号化を一貫して適用する方法を紹介します。セキュリティおよびコンプライアンスチームは、任意の 2 ノード間で暗号化されていないトラフィックをポリシーでブロックでき、ネットワークセキュリティガバナンスを強化できます。
- **[AWS と Microsoft Azure がマルチクラウドネットワーキングの拡張に向けて協力](https://aws.amazon.com/blogs/networking-and-content-delivery/aws-and-microsoft-azure-collaborate-to-expand-multicloud-networking/)** — AWS と Microsoft Azure が協力し、両クラウド間の高パフォーマンスなプライベート接続を簡素化するマルチクラウドネットワーキングソリューションの提供を開始しました。これにより、複数の接続プロバイダーや物理インフラを経由して数週間から数か月かかっていたプロビジョニング作業を大幅に短縮できます。

## 2026-08-27 · 週次まとめ

- **[CloudFront VPC Origins と高度なルーティングを活用したマルチリージョン アクティブ-アクティブ アーキテクチャの構築](https://aws.amazon.com/blogs/networking-and-content-delivery/building-multi-region-active-active-architectures-with-cloudfront-vpc-origins-and-advanced-routing/)** — 2024 年 11 月にリリースされた Amazon CloudFront VPC Origins を活用し、マルチリージョン アクティブ-アクティブ アーキテクチャを構築する方法を紹介しています。トラフィック ルーティング、セッション一貫性、自動フェイルオーバーによる可用性維持の手法を解説しています。

## 2026-08-25 · 週次まとめ

- **[CloudFront Functions の統合ロギング](https://aws.amazon.com/blogs/networking-and-content-delivery/cloudfront-functions-unified-logging/)** — CloudFront Functions のログを Amazon CloudWatch Logs に統合して送信できるようになり、トークン検証結果やヘッダー情報などの関数実行履歴を一か所で確認できるようになりました。これまで CloudFront Realtime Logs など複数の経路から分散収集する必要があった観測性の課題が改善されます。
- **[Amazon Route 53 Global Resolver を使ったマルチアカウント環境向け共有 DNS ビュー](https://aws.amazon.com/blogs/networking-and-content-delivery/shared-dns-views-for-multi-account-environments-with-amazon-route-53-global-resolver/)** — Amazon Route 53 Global Resolver の DNS ビュー機能により、ネットワーキングチームは共有名前解決を中央集中式で制御しながら、アプリケーションチームはマルチアカウント構成でも独自の DNS レコードを自律的に管理できるようになります。これにより、複雑な DNS 環境における中央ガバナンスとチームの自律性のバランスを保つことが可能です。

## 2026-08-22 · 週次まとめ

- **[NEL でクライアント側のネットワーク障害を可視化する](https://aws.amazon.com/blogs/networking-and-content-delivery/gain-visibility-into-client-side-network-failures-with-nel/)** — NEL (Network Error Logging) を活用することで、サーバーログには残らない DNS 解決失敗や TCP タイムアウトなどのクライアント側ネットワーク障害を収集・分析できます。CDN などの共有インフラ上で特定のオリジンに起因する接続問題を把握するうえで、ネットワーク観測性の観点から実践的な手段となります。

## 2026-06-30 · 週次サマリー

- **[AWS Cloud WAN Routing Policy: Real-World Global Network Scenarios – Part 2](https://aws.amazon.com/blogs/networking-and-content-delivery/aws-cloud-wan-routing-policy-real-world-global-network-scenarios-part-2/)** — Part 1 で紹介した AWS Cloud WAN ルーティングポリシーの基礎を踏まえ、マッチ条件・アクション・ルート集約という 3 つのコアコンポーネントを活用して、ルート伝播とパス選択を細かく制御する実際のグローバルネットワークシナリオを探求する第 2 弾です。複数リージョンにまたがる複雑なネットワーク環境でルーティングポリシーを適用するための実践的なガイダンスを提供します。
- **[Extending NLB Health Checks for RADIUS Using an Amazon ECS Witness](https://aws.amazon.com/blogs/networking-and-content-delivery/extending-nlb-health-checks-for-radius-using-an-amazon-ecs-witness/)** — 標準的な Network Load Balancer のヘルスチェックは RADIUS サーバーへの到達性のみを確認するため、実際の認証機能は検証されません。そのため、ID ストアに障害が発生したサーバーにもトラフィックが送られ続けるという問題があります。本記事では、単一の Amazon ECS ウィットネスを使用してアプリケーション層の RADIUS プローブを実行し、NLB ターゲットグループのメンバーシップを直接調整するオープンソースのリファレンスソリューションを紹介します。

## 2026-06-23 · 週次サマリー

- **[VPC Resource Gateways: Implementation Patterns and Use Cases](https://aws.amazon.com/blogs/networking-and-content-delivery/vpc-resource-gateways-implementation-patterns-and-use-cases/)** — AWS PrivateLink のプロバイダー/コンシューマーモデルに適合しない環境や、IP アドレス空間が重複している環境で VPC 間のサービス接続が必要な場合に向けた、VPC リソースゲートウェイの実装パターンとユースケースを紹介します。VPC ピアリングや AWS Transit Gateway 単独では解決できない複雑なネットワーク課題への対処方法を解説します。
- **[Extending SD-WAN segmentation into AWS Cloud WAN – Part 2](https://aws.amazon.com/blogs/networking-and-content-delivery/extending-sd-wan-segmentation-into-aws-cloud-wan-part-2/)** — SD-WAN セグメンテーションを AWS Cloud WAN に拡張する 2 部構成シリーズの第 2 部です。Part 1 で構築した GRE ベースの Connect アタッチメントを基盤として、マルチテナントおよび規制対象環境における厳格なネットワークセグメンテーションの維持方法を解説します。セキュリティおよびコンプライアンス要件を満たしながら SD-WAN を AWS クラウドネットワークと統合することに焦点を当てています。
- **[Extending SD-WAN segmentation into AWS Cloud WAN – Part 1](https://aws.amazon.com/blogs/networking-and-content-delivery/extending-sd-wan-segmentation-into-aws-cloud-wan-part-1/)** — マルチテナントや規制対象の環境、または複数のビジネスユニットを運営する組織が、SD-WAN 仮想アプライアンスをデプロイして AWS Cloud WAN を通じてネットワークセグメンテーションを拡張する方法を示す 2 部構成シリーズの第 1 部です。セグメント化された環境を単一のスケーラブルなグローバルネットワークに統合するアーキテクチャを解説します。
- **[Best practices for securing your IPv6 infrastructure on AWS using VPC Block Public Access](https://aws.amazon.com/blogs/networking-and-content-delivery/best-practices-for-securing-your-ipv6-infrastructure-on-aws-using-vpc-block-public-access/)** — 接続モデルの柔軟性を維持しながら、AWS 上のプライベート IPv6 リソースを保護するためのベストプラクティスと考慮事項を解説します。VPC Block Public Access を使用して IPv6 ネットワークおよびアプリケーションインフラストラクチャを安全に構成する方法を説明します。
- **[Securing zero trust access with AWS Verified Access and AWS Network Firewall](https://aws.amazon.com/blogs/networking-and-content-delivery/securing-zero-trust-access-with-aws-verified-access-and-aws-network-firewall/)** — 従来の VPN が付与する過剰なネットワークアクセスという課題に対処するため、AWS Verified Access と AWS Network Firewall を組み合わせて ID ベースのアクセス制御ときめ細かなトラフィックインスペクションを実現するゼロトラストソリューションを紹介します。内部アプリケーションへのアクセスを意図したスコープに限定し、セキュリティを強化する方法を解説します。
- **[Deploying internal DNS zones for internet-facing load balancers](https://aws.amazon.com/blogs/networking-and-content-delivery/deploying-internal-dns-zones-for-internet-facing-load-balancers/)** — インターネット向け Elastic Load Balancing に対してプライベートホストゾーンを使用した内部 DNS を構成する方法を解説します。Network Load Balancer、Application Load Balancer、Gateway Load Balancer など、さまざまな ELB タイプに適した DNS デプロイパターンを説明します。
- **[Extending AWS DevOps Agent network investigations with S3 logs and custom MCP on Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/networking-and-content-delivery/extending-aws-devops-agent-network-investigations-with-s3-logs-and-custom-mcp-on-amazon-bedrock-agentcore/)** — AWS Application Load Balancer で 502 エラーが発生した際に、Amazon S3 に保存されたログとカスタム MCP を Amazon Bedrock AgentCore に接続することで、API レベルの調査を超えて根本原因を分析する方法を示します。ネットワークインシデント対応において AI ベースのエージェントを活用して調査範囲を拡張する実践的なアプローチを紹介します。
