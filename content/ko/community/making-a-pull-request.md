# 풀 리퀘스트 {#pull-requests}

AWS 네트워킹 모범 사례 가이드에 콘텐츠를 기여할 준비가 되셨나요? 이 페이지에서는 첫 번째 변경 사항 작성부터 메인 저장소에 병합되기까지, 풀 리퀘스트를 생성하는 전체 과정을 안내합니다.

## 빠른 시작 {#quick-start}

**풀 리퀘스트가 처음이신가요?** 핵심 프로세스는 다음과 같습니다:

1. GitHub에서 저장소를 **[포크(Fork)](#1-fork-the-repository-on-github)**합니다

2. 변경 사항을 위한 **[브랜치를 생성](#2-create-a-branch-for-your-changes)**합니다

3. **[편집 후 커밋](#3-make-your-edits-and-commit-them)**합니다

4. 명확한 설명과 함께 **[풀 리퀘스트를 제출](#4-submit-a-pull-request-with-a-clear-description)**합니다

5. **[리뷰 프로세스](#5-review-process)**를 진행합니다

**더 자세한 내용이 필요하신가요?** 전체 워크플로우는 아래 내용을 계속 읽어보세요.

## 제출 전 확인 사항 {#before-you-submit}

!!! tip "체크리스트"
    * [ ] 변경 사항이 [컨벤션](conventions.md)을 따르는지 확인

    * [ ] 모든 링크가 올바르게 작동하는지 확인

    * [ ] 커밋 메시지가 명확하게 작성되었는지 확인

    * [ ] PR 설명에 관련 이슈가 참조되었는지 확인

    * [ ] 오류 없이 문서가 빌드되는지 테스트

## 단계별 프로세스 {#step-by-step-process}

### 1. GitHub에서 저장소 포크 {#1-fork-the-repository-on-github}

* GitHub에서 [aws-networking-best-practices] 저장소를 포크합니다 ([GitHub Docs: 저장소 포크하기][fork-docs]{:target="_blank"})

* 포크한 저장소를 로컬 머신에 클론합니다 ([GitHub Docs: 저장소 클론하기][clone-docs]{:target="_blank"})

* 새 브랜치를 생성합니다: `git checkout -b your-feature-name` ([GitHub Docs: Git 브랜치][branch-docs]{:target="_blank"})

[aws-networking-best-practices]: https://github.com/aws/aws-networking-best-practices
[fork-docs]: https://docs.github.com/en/get-started/quickstart/fork-a-repo
[clone-docs]: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository
[branch-docs]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches

### 2. 변경 사항을 위한 브랜치 생성 {#2-create-a-branch-for-your-changes}

* 새 브랜치를 생성합니다: `git checkout -b your-feature-name` ([GitHub Docs: Git 브랜치][branch-docs]{:target="_blank"})

* 브랜치 이름은 내용을 잘 설명하도록 작성합니다: `add-transit-gateway-best-practices` 또는 `fix-vpc-peering-link`

[branch-docs]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches

### 3. 편집 후 커밋 {#3-make-your-edits-and-commit-them}

* 문서 파일을 편집합니다

* 명확한 메시지와 함께 논리적인 단위로 변경 사항을 커밋합니다 ([GitHub Docs: 커밋에 대하여][commit-docs]{:target="_blank"})

* 정기적으로 포크에 푸시합니다: `git push origin your-feature-name` ([GitHub Docs: 변경 사항 푸시하기][push-docs]{:target="_blank"})

[commit-docs]: https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/about-commits
[push-docs]: https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository

### 4. 명확한 설명과 함께 풀 리퀘스트 제출 {#4-submit-a-pull-request-with-a-clear-description}

* 포크에서 업스트림 저장소로 풀 리퀘스트를 엽니다 ([GitHub Docs: 포크에서 PR 생성하기][create-pr-fork-docs]{:target="_blank"})

* 변경 사항에 대한 명확한 설명을 포함합니다

* 관련 이슈나 토론을 참조합니다 ([GitHub Docs: 이슈 연결하기][linking-issues]{:target="_blank"})

* 피드백을 위해 초기에 Draft 풀 리퀘스트를 여는 것을 고려해 보세요 ([GitHub Docs: Draft PR][draft-pr-docs]{:target="_blank"})

[create-pr-fork-docs]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork
[draft-pr-docs]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests#draft-pull-requests
[linking-issues]: https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue

### 5. 리뷰 프로세스 {#5-review-process}

* 리뷰어 피드백에 신속하게 응답합니다 ([GitHub Docs: PR 리뷰][pr-review-docs]{:target="_blank"})

* 요청된 변경 사항을 반영하고 업데이트를 푸시합니다

* 승인되면 PR이 병합됩니다

[pr-review-docs]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews

!!! example "좋은 커밋 메시지 예시"
    * ✅ "Add Transit Gateway best practices for multi-account setups"

    * ✅ "Fix broken link in VPC peering documentation"

    * ❌ "Update docs"

    * ❌ "Various fixes"

## 다음 단계는? {#what-happens-next}

풀 리퀘스트가 병합된 후:

* 변경 사항이 라이브 문서에 반영됩니다

* 피처 브랜치를 삭제할 수 있습니다

* 지속적인 기여를 고려해 주세요 - 꾸준히 기여해 주시는 분들을 환영합니다!

커뮤니티를 위한 AWS 네트워킹 가이드 개선에 기여해 주셔서 감사합니다.

## 환경 설정 {#environment-setup}

먼저 저장소를 클론합니다.

```bash
git clone https://github.com/YOUR-USERNAME/aws-networking-best-practices
cd aws-networking-best-practices
```

그런 다음 설정 스크립트를 소스하여 Python 가상 환경을 생성하고 모든 의존성을 설치합니다:

```bash
source ./scripts/setup.sh
```

이것으로 완료됩니다. 스크립트는 `venv` 디렉터리(이미 `.gitignore`에 포함됨)를 생성하고, `requirements.txt`에서 모든 패키지를 설치하며, 현재 셸에서 가상 환경을 활성화합니다.

!!! note "pip가 항상 가상 환경에서 실행되도록 설정"

    환경 변수 `PIP_REQUIRE_VIRTUALENV`를 `true`로 설정하면,
    `pip`는 가상 환경 외부에서의 패키지 설치를 거부합니다.
    `venv` 활성화를 잊으면 시간이 지남에 따라 가상 환경 외부에
    온갖 패키지가 설치되어 추가적인 오류가 발생할 수 있으므로
    매우 불편해질 수 있습니다. 따라서 `.bashrc` 또는 `.zshrc`에
    다음을 추가하고 셸을 재시작하는 것을 권장합니다:

```bash
export PIP_REQUIRE_VIRTUALENV=true
```

  [venv]: https://docs.python.org/3/library/venv.html
  [venv-activate]: https://docs.python.org/3/library/venv.html#how-venvs-work

### 라이브 미리보기 {#live-preview}

다음 명령으로 라이브 미리보기 서버를 시작합니다:

```
mkdocs serve
```

브라우저에서 [localhost:8000][live preview]으로 접속하면 이 문서를 바로 확인할 수 있습니다.

!!! warning "자동 생성 파일"

    `material` 디렉터리의 내용은 `src` 디렉터리에서 자동으로 생성되며
    테마 빌드 시 덮어쓰이므로, 해당 디렉터리에서는 절대 변경을 하지 마세요.

  [live preview]: http://localhost:8000

## 로컬 유효성 검사 {#local-validation}

풀 리퀘스트를 제출하기 전에 유효성 검사 스크립트를 실행하여 문제를 조기에 발견하세요:

```bash
./scripts/validate-pr.sh
```

이 스크립트는 자동화된 PR 유효성 검사와 동일한 검사를 실행하며, 다음 항목을 포함합니다:

* Markdown 린팅
* MkDocs 빌드 테스트
* 링크 검사
* 맞춤법 검사
* YAML 유효성 검사
* 파일 명명 규칙
* 이미지 최적화 검사
* 내비게이션 구조 유효성 검사
* IP 주소 유효성 검사

### 필수 의존성 {#required-dependencies}

설정 스크립트가 모든 Python 패키지를 처리합니다. 전체 유효성 검사를 위해 다음 Node.js 도구도 필요합니다:

```bash
npm install -g markdownlint-cli2 markdown-link-check cspell
```

!!! tip "누락된 도구 건너뛰기"
    스크립트는 누락된 도구에 대해 경고를 표시하지만 사용 가능한 검사는 계속 진행합니다.

## 권장 사항 및 주의 사항 {#dos-and-donts}

1. 변경 사항에 대한 설명 없이 풀 리퀘스트를 생성하지 **마세요**.

2. 코드를 작성하거나 수정하기 전에 변경 의도를 토론에서 사람들과 논의하여

   변경 사항의 근거가 명확하게 전달되도록 **하세요**.

3. 풀 리퀘스트의 맥락을 제공하기 위해 토론이나 관련 이슈를 링크로 연결

   **하세요**.

4. 불확실한 사항이 있으면 질문을 **하세요**.

5. 진행하려는 작업이 더 넓은 커뮤니티에 도움이 되고 AWS 네트워킹 모범 사례

   가이드를 더 나은 리소스로 만드는지 스스로에게 **물어보세요**.

6. 변경 사항을 만드는 데 드는 비용이 가져올 이점과 적절한 균형을 이루는지

   스스로에게 **물어보세요**. 그렇지 않으면 합리적으로 보이는 변경 사항도 상대적으로
   작은 이득을 위해 복잡성을 추가하거나, 기존 동작을 깨뜨리거나, 다른 변경이
   필요할 때 취약해질 수 있습니다.

7. 해결하기 어려운 충돌을 최소화하기 위해 동시 변경 사항을 자주 병합

   **하세요**.

## 일반적인 문제 {#common-issues}

**빌드 오류가 발생하나요?** 모든 Markdown 구문이 올바르고 링크가 유효한지 확인하세요.

**병합 충돌이 발생하나요?** 포크를 메인 저장소와 동기화하세요:

```bash
git remote add upstream https://github.com/aws/aws-networking-best-practices.git
git fetch upstream
git merge upstream/main
```

## 풀 리퀘스트에 대해 알아보기 {#learning-about-pull-requests}

풀 리퀘스트는 Git 호스팅 서비스가 Git 위에 추가한 개념입니다.
풀 리퀘스트를 만들기 전에 현재 사용 중인 서비스인 GitHub의 문서를 숙지하는 것이 좋습니다. 다음 문서들이 특히 중요합니다:

1. [저장소 포크하기]{:target="_blank"}
2. [포크에서 풀 리퀘스트 생성하기]{:target="_blank"}
3. [풀 리퀘스트 생성하기]{:target="_blank"}

GitHub은 다양한 운영 체제와 GitHub과 상호작용하는 다양한 방법에 맞춘 문서를 제공합니다. 이 문서에서는 AWS 네트워킹 모범 사례 가이드에 적용되는 프로세스를 최대한 설명하려 하지만, 모든 도구와 방법의 조합을 다룰 수는 없습니다. 계속 진행하기 전에 풀 리퀘스트의 개념을 일반적으로 이해하는 것도 중요합니다.

[저장소 포크하기]: https://docs.github.com/en/get-started/quickstart/fork-a-repo
[포크에서 풀 리퀘스트 생성하기]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork
[풀 리퀘스트 생성하기]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request
