---
hide:
  - toc
---
# AWS What's New — ネットワーキング

[AWS What's New](https://aws.amazon.com/new/) の新着発表からネットワーキング関連の項目を抽出し、平日の毎朝、自動で要約します。原文は各項目のリンクをご確認ください。最新の項目が上部に表示されます。

<!-- NEWS:INSERT -->

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
