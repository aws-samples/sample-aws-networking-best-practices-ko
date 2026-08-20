# プルリクエスト {#pull-requests}

AWS ネットワーキングベストプラクティスガイドへのコンテンツ貢献をご検討いただきありがとうございます。このページでは、最初の変更を加えてからメインリポジトリにマージされるまでの、プルリクエストの作成手順を説明します。

## クイックスタート {#quick-start}

**プルリクエストが初めての方へ** 基本的な手順は以下のとおりです。

1. GitHub でリポジトリを **[フォーク](#1-fork-the-repository-on-github)** する

2. 変更用の **[ブランチを作成](#2-create-a-branch-for-your-changes)** する

3. **[編集してコミット](#3-make-your-edits-and-commit-them)** する

4. 明確な説明を添えて **[プルリクエストを提出](#4-submit-a-pull-request-with-a-clear-description)** する

5. **[レビュープロセス](#5-review-process)** に従って対応する

**詳細を確認したい方は** 引き続き完全なワークフローをお読みください。

## 提出前の確認 {#before-you-submit}

!!! tip "チェックリスト"
    * [ ] 変更が [規約](conventions.md) に従っている

    * [ ] すべてのリンクが正しく機能している

    * [ ] コミットメッセージが説明的である

    * [ ] PR の説明に関連する Issue を参照している

    * [ ] ドキュメントがエラーなくビルドされることを確認した

## ステップバイステップの手順 {#step-by-step-process}

### 1. Fork the repository on GitHub {#1-fork-the-repository-on-github}

* GitHub で [aws-networking-best-practices] リポジトリをフォークする ([GitHub Docs: リポジトリのフォーク][fork-docs]{:target="_blank"})

* フォークをローカルマシンにクローンする ([GitHub Docs: リポジトリのクローン][clone-docs]{:target="_blank"})

* 新しいブランチを作成する: `git checkout -b your-feature-name` ([GitHub Docs: Git ブランチ][branch-docs]{:target="_blank"})

[aws-networking-best-practices]: https://github.com/aws/aws-networking-best-practices
[fork-docs]: https://docs.github.com/en/get-started/quickstart/fork-a-repo
[clone-docs]: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository
[branch-docs]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches

### 2. Create a branch for your changes {#2-create-a-branch-for-your-changes}

* 新しいブランチを作成する: `git checkout -b your-feature-name` ([GitHub Docs: Git ブランチ][branch-docs]{:target="_blank"})

* ブランチ名はわかりやすく付ける: `add-transit-gateway-best-practices` や `fix-vpc-peering-link` など

[branch-docs]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches

### 3. Make your edits and commit them {#3-make-your-edits-and-commit-them}

* ドキュメントファイルを編集する

* 明確なメッセージを添えて、論理的な単位でコミットする ([GitHub Docs: コミットについて][commit-docs]{:target="_blank"})

* 定期的にフォークへプッシュする: `git push origin your-feature-name` ([GitHub Docs: 変更のプッシュ][push-docs]{:target="_blank"})

[commit-docs]: https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/about-commits
[push-docs]: https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository

### 4. Submit a pull request with a clear description {#4-submit-a-pull-request-with-a-clear-description}

* フォークからアップストリームリポジトリへプルリクエストを開く ([GitHub Docs: フォークから PR を作成する][create-pr-fork-docs]{:target="_blank"})

* 変更内容を明確に説明する

* 関連する Issue やディスカッションを参照する ([GitHub Docs: Issue のリンク][linking-issues]{:target="_blank"})

* 早めにドラフトプルリクエストを開いてフィードバックを得ることを検討する ([GitHub Docs: ドラフト PR][draft-pr-docs]{:target="_blank"})

[create-pr-fork-docs]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork
[draft-pr-docs]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests#draft-pull-requests
[linking-issues]: https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue

### 5. Review Process {#5-review-process}

* レビュアーのフィードバックに迅速に対応する ([GitHub Docs: PR レビュー][pr-review-docs]{:target="_blank"})

* 要求された変更を加えてプッシュする

* 承認されると PR がマージされる

[pr-review-docs]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews

!!! example "良いコミットメッセージの例"
    * ✅ "Add Transit Gateway best practices for multi-account setups"

    * ✅ "Fix broken link in VPC peering documentation"

    * ❌ "Update docs"

    * ❌ "Various fixes"

## マージ後の流れ {#what-happens-next}

プルリクエストがマージされると:

* 変更が公開ドキュメントに反映される

* フィーチャーブランチを削除できる

* ぜひ継続的に貢献してください — 継続的なコントリビューターを歓迎します！

コミュニティのために AWS ネットワーキングガイドの改善にご協力いただきありがとうございます。

## 環境のセットアップ {#environment-setup}

まず、リポジトリをクローンします。

```bash
git clone https://github.com/YOUR-USERNAME/aws-networking-best-practices
cd aws-networking-best-practices
```

次に、セットアップスクリプトをソースして Python 仮想環境を作成し、すべての依存関係をインストールします。

```bash
source ./scripts/setup.sh
```

以上です。スクリプトは `venv` ディレクトリ(すでに `.gitignore` に含まれています)を作成し、`requirements.txt` からすべてをインストールして、現在のシェルで仮想環境を有効化します。

!!! note "pip を常に仮想環境内で実行する"

    環境変数 `PIP_REQUIRE_VIRTUALENV` を `true` に設定すると、`pip` は仮想環境の外へのインストールを拒否します。`venv` のアクティベートを忘れると、時間の経過とともに仮想環境の外にさまざまなパッケージがインストールされ、さらなるエラーの原因になることがあります。そのため、`.bashrc` または `.zshrc` に以下を追加してシェルを再起動することをお勧めします。

```bash
export PIP_REQUIRE_VIRTUALENV=true
```

  [venv]: https://docs.python.org/3/library/venv.html
  [venv-activate]: https://docs.python.org/3/library/venv.html#how-venvs-work

### ライブプレビュー {#live-preview}

以下のコマンドでライブプレビューサーバーを起動します。

```
mkdocs serve
```

ブラウザで [localhost:8000][live preview] を開くと、このドキュメントが表示されます。

!!! warning "自動生成されるファイル"

    `material` ディレクトリ内のファイルは `src` ディレクトリから自動生成されるため、テーマのビルド時に上書きされます。このディレクトリ内のファイルは絶対に変更しないでください。

  [live preview]: http://localhost:8000

## ローカルでの検証 {#local-validation}

プルリクエストを提出する前に、検証スクリプトを実行して問題を早期に発見してください。

```bash
./scripts/validate-pr.sh
```

このスクリプトは、自動化された PR 検証と同じチェックを実行します。チェック内容は以下のとおりです。

* Markdown のリント
* MkDocs のビルドテスト
* リンクチェック
* スペルチェック
* YAML の検証
* ファイル命名規則
* 画像最適化チェック
* ナビゲーション構造の検証
* IP アドレスの検証

### 必要な依存関係 {#required-dependencies}

Python パッケージはセットアップスクリプトが処理します。完全な検証には以下の Node.js ツールも必要です。

```bash
npm install -g markdownlint-cli2 markdown-link-check cspell
```

!!! tip "不足しているツールのスキップ"
    ツールが見つからない場合はスクリプトが警告を表示しますが、利用可能なチェックは続行されます。

## すべきこと・すべきでないこと {#dos-and-donts}

1. **すべきでないこと**: 説明のない変更だけのプルリクエストを作成する。

2. **すべきこと**: 変更を加える前に、ディスカッションで意図を共有し、変更の根拠を明確にする。

3. **すべきこと**: プルリクエストにディスカッションや Issue へのリンクを添えてコンテキストを提供する。

4. **すべきこと**: 不明な点があれば積極的に質問する。

5. **すべきこと**: 自分の変更がより広いコミュニティに利益をもたらし、AWS ネットワーキングベストプラクティスガイドをより良いリソースにするかどうかを自問する。

6. **すべきこと**: 変更のコストが得られるメリットに見合っているかを自問する。一見合理的な変更でも、比較的小さなメリットのために複雑さを増したり、既存の動作を壊したり、他の変更が必要になったときに脆弱になる場合がある。

7. **すべきこと**: 競合が難しくなる可能性のある変更の衝突を最小限に抑えるため、並行する変更を頻繁にマージする。

## よくある問題 {#common-issues}

**ビルドエラーが発生する場合** Markdown の構文が正しいこと、リンクが有効であることを確認してください。

**マージコンフリクトが発生する場合** フォークをメインリポジトリと同期してください。

```bash
git remote add upstream https://github.com/aws/aws-networking-best-practices.git
git fetch upstream
git merge upstream/main
```

## プルリクエストについて学ぶ {#learning-about-pull-requests}

プルリクエストは、Git ホスティングサービスが Git の上に追加した概念です。プルリクエストを作成する前に、使用しているサービスである GitHub のドキュメントをよく理解しておく必要があります。特に以下の記事が重要です。

1. [リポジトリのフォーク]{:target="_blank"}
2. [フォークからプルリクエストを作成する]{:target="_blank"}
3. [プルリクエストを作成する]{:target="_blank"}

GitHub では、異なる OS や GitHub との操作方法に応じたドキュメントが提供されています。このドキュメントでは AWS ネットワーキングベストプラクティスガイドに適用されるプロセスをできる限り説明していますが、すべてのツールや操作方法の組み合わせを網羅することはできません。また、続きを読む前に、プルリクエストの概念全般を理解しておくことが重要です。

[リポジトリのフォーク]: https://docs.github.com/en/get-started/quickstart/fork-a-repo
[フォークからプルリクエストを作成する]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork
[プルリクエストを作成する]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request
