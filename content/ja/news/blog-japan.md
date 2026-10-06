---
hide:
  - toc
---
# AWS Japan ブログ — ネットワーキング

[AWS Japan ブログ](https://aws.amazon.com/jp/blogs/news/) のネットワーキング関連記事を毎週金曜日に、最近の投稿を中心に要約します。原文は各項目のリンクをご確認ください。最新の項目が上部に表示されます。

<!-- NEWS:INSERT -->

## 2026-10-06 · 週次まとめ

- **[週刊 AWS – 2026/9/28 週](https://aws.amazon.com/jp/blogs/news/aws-weekly-20260928/)** — Amazon Route 53 Resolver DNS Firewall での Palo Alto Networks Advanced DNS Security の GA や、AWS Backup の論理的エアギャップボールトによる Amazon FSx for NetApp ONTAP 対応、Aurora PostgreSQL からの Apache Iceberg/Parquet 直接クエリなど、幅広いアップデートが発表されました。ネットワーキング観点では、DNS セキュリティの強化と AWS IAM Identity Center のマルチリージョンサポート拡大が注目ポイントです。

## 2026-09-25 · 週次まとめ

- **[週刊 AWS – 2026/9/14 週](https://aws.amazon.com/jp/blogs/news/aws-weekly-20260914/)** — 今週は AWS Direct Connect 専用接続の定額料金導入、AWS PrivateLink Tunnel Endpoint のリリース、AWS Transfer Family における Network Load Balancer 配下での送信元 IP 保持サポートなど、ネットワーキング関連の重要なアップデートが複数発表されました。その他にも Amazon Bedrock AgentCore の新しい AgentCore Runtime、Amazon ECS の Amazon S3 Files サポート拡張、Amazon Connect の新機能など幅広いサービスアップデートが含まれています。

## 2026-09-24 · 週次まとめ

- **[Amazon CloudFront で SAP S/4HANA に mTLS 認証を実装する](https://aws.amazon.com/jp/blogs/news/implement-mtls-authentication-with-amazon-cloudfront-for-sap-s-4hana/)** — Amazon CloudFront の mTLS verify モードを使用してエッジでクライアント証明書を検証し、ALB パススルーと SAP ICM の X.509 認証を組み合わせることで、パスワードレスな SSO を実現するアーキテクチャを解説します。社内テストでは TLS ハンドシェイクの遅延時間を削減し、初回ログイン時間を約 40〜50% 短縮できることが確認されました。

## 2026-09-19 · 週次まとめ

- **[SAP Commerce Cloud と AWS 上の SAP Cloud ERP Private の統合 – 実践的で実証済みのアプローチ](https://aws.amazon.com/jp/blogs/news/integrating-sap-commerce-cloud-with-sap-cloud-erp-private-on-aws-a-practical-and-proven-approach/)** — SAP Commerce (SAP Hybris) 2205 のメインストリームメンテナンス終了を前に、SAP Commerce Cloud SaaS と AWS 上の SAP Cloud ERP Private を統合するモダナイゼーションアーキテクチャを紹介します。リージョン選択、Amazon CloudFront・AWS Global Accelerator・Amazon Route 53 を活用した遅延時間の最適化、セキュリティの 4 つの観点からベストプラクティスを解説し、Buy with Prime および Amazon MCF との連携による e コマース拡張についても説明しています。

## 2026-09-15 · 週次まとめ

- **[はじめての自動推論](https://aws.amazon.com/jp/blogs/news/a-gentle-introduction-to-automated-reasoning/)** — C と Python のコード例を用いて自動推論の概念をわかりやすく解説し、網羅的テストで 1,300 年以上かかる検証をミリ秒で行える理由や、停止性問題に起因する「Don't know」応答の必然性を説明しています。IAM Access Analyzer や VPC Reachability Analyzer など AWS サービスにおける活用事例も紹介しています。

## 2026-09-13 · 週次まとめ

- **[Amazon MWAA と Airflow 3.0 によるイベント駆動のパイプラインオーケストレーション](https://aws.amazon.com/jp/blogs/news/event-driven-pipeline-orchestration-with-amazon-mwaa-and-airflow-3-0/)** — Apache Airflow 3.0 の Asset Watcher と Amazon SQS を組み合わせることで、複数の Amazon MWAA 環境やアカウント間にまたがるイベント駆動のオーケストレーションを実現する方法を解説しています。ポーリングベースのセンサーをイベント駆動トリガーに置き換えることで環境間の遅延時間を数分から数秒に短縮でき、クロスアカウント IAM および Amazon VPC ネットワークの設定に関するモ범사례も紹介しています。

## 2026-08-29 · 週次まとめ

- **[Amazon CloudWatch Logs で Application Load Balancer のログを分析する](https://aws.amazon.com/jp/blogs/news/analyze-application-load-balancer-logs-with-amazon-cloudwatch-logs/)** — Amazon CloudWatch Logs が ALB のアクセスログ・接続ログ・ヘルスチェックログを Vended Logs として構造化 JSON で直接配信できるようになりました。これにより、リクエスト・接続・ターゲット単位の詳細な観測性が実現し、ダッシュボードや Log Analytics、Contributor Insights を活用した障害切り分けやアラーム設定が可能になります。

## 2026-08-25 · 週次まとめ

- **[週刊 AWS – 2026/8/17 週](https://aws.amazon.com/jp/blogs/news/aws-weekly-20260817/)** — AWS Direct Connect がインバウンドプレフィックス制御と VIF あたり最大 1,000 経路への拡張を発表するなど、ネットワーキング面での重要なアップデートが含まれています。その他にも AWS CloudShell へのビジュアルファイルエディタ追加、Amazon ECR のレプリケーションルール上限引き上げ、AWS Glue 6.0 の GA と 30% 値下げなど、幅広いサービス改善が行われました。

## 2026-08-21 · 週次まとめ

- **[Oracle Database 26ai での自然言語クエリ: Amazon Bedrock を使った Amazon RDS for Oracle での Select AI 入門](https://aws.amazon.com/jp/blogs/news/natural-language-queries-on-oracle-database-26ai-getting-started-with-select-ai-on-amazon-rds-for-oracle-with-amazon-bedrock/)** — Amazon RDS for Oracle で Oracle Database 26ai がサポートされ、Amazon Bedrock の基盤モデルを通じて自然言語でリレーショナルデータを照会できる Select AI が利用可能になりました。VPC インターフェイスエンドポイントや IAM 認証情報の設定から DBMS_CLOUD_AI プロファイルの作成・自然言語クエリの実行まで、一連の構成手順を解説しています。
