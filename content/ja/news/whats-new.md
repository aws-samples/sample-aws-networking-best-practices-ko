---
hide:
  - toc
---
# AWS What's New — ネットワーキング

[AWS What's New](https://aws.amazon.com/new/) の新着発表からネットワーキング関連の項目を抽出し、平日の毎朝、自動で要約します。原文は各項目のリンクをご確認ください。最新の項目が上部に表示されます。

<!-- NEWS:INSERT -->

## 2026-06-30 · 日次アップデート

- **[Amazon MWAA Serverless が共有 VPC 構成をサポート](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-mwaa-serverless-vpc/)** — Amazon MWAA Serverless が AWS RAM 経由で共有された VPC サブネットをサポートするようになりました。これにより、共有 VPC 環境でのワークフロー作成をブロックしていたバリデーションエラーが解消されます。マルチアカウントのランディングゾーンアーキテクチャで集中型ネットワーキングを採用している組織が、MWAA Provisioned 環境と同様に、共有サブネット上に MWAA Serverless ワークフローをデプロイできるようになります。

## 2026-06-23 · 日次アップデート

- **[AWS Network Firewall がデフォルトのドロップアクションを更新し、接続信頼性を向上](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-network-firewall-updates-default-drop-action)** — 新しい AWS Network Firewall ポリシーのデフォルトステートフルアクションが、双方向の「Application drop established」からサーバー方向のみに変更されました。これにより、以前のデフォルト設定が正当なサーバーからクライアントへの TCP トラフィックを自動的にブロックしていた問題が解消され、接続の信頼性が向上します。
