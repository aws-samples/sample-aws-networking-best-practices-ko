---
hide:
  - toc
---
# AWS What's New — ネットワーキング

[AWS What's New](https://aws.amazon.com/new/) の新着発表からネットワーキング関連の項目を抽出し、平日の毎朝、自動で要約します。原文は各項目のリンクをご確認ください。最新の項目が上部に表示されます。

<!-- NEWS:INSERT -->

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
