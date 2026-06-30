# 배포 가이드

이 사이트는 `mkdocs build`가 만드는 `site/` 정적 디렉터리를 어디에 올리든 동일하게 동작합니다.
기본 호스팅은 **GitHub Pages**이며, 자동화 수준에 따라 두 가지 방식이 있습니다.

---

## 방식 2 — 로컬 생성 + Pages 자동 배포 (기본·권장)

번역/소식은 **로컬에서** 생성해 커밋하고, GitHub Actions는 **AWS 없이** 빌드·배포만 합니다.
조직(aws-samples) repo의 Secret/OIDC 제약을 우회할 수 있어 가장 빠르게 시작됩니다.

1. **GitHub Pages 활성화**: repo Settings → Pages → Source = **GitHub Actions**
2. **콘텐츠 생성(로컬, AWS 자격증명 필요)**
   ```bash
   pip install -r requirements.txt boto3
   python scripts/sync.py                      # upstream 변경분 재번역(EN→KO)
   python scripts/news.py --source whats-new   # 소식 수집·요약(EN/KO)
   python scripts/news.py --source blog-networking
   python scripts/news.py --source blog-korea
   ```
3. **커밋·푸시** → `.github/workflows/deploy-pages.yml`가 자동으로 빌드 후 Pages에 배포
   ```bash
   git add -A && git commit -m "chore: update translations & news" && git push
   ```

> `deploy-pages.yml`는 시크릿이 필요 없습니다. `push`(main) 또는 수동 실행 시 동작합니다.

---

## 방식 1 — 풀 CI 자동화 (OIDC, 선택)

GitHub Actions가 직접 Amazon Bedrock을 호출해 매일 무인으로 재번역·소식·배포합니다.
`sync-and-deploy.yml`·`news.yml`은 현재 **수동(workflow_dispatch) 전용**으로 두었습니다. 자동화하려면:

1. **AWS OIDC 역할 생성** (키 없이 GitHub Actions가 AWS 접근)
   - IAM → Identity providers → `token.actions.githubusercontent.com` 추가
   - 역할 신뢰 정책을 이 repo의 main 브랜치로 제한(최소 권한):
     ```json
     "Condition": {
       "StringEquals": { "token.actions.githubusercontent.com:aud": "sts.amazonaws.com" },
       "StringLike":   { "token.actions.githubusercontent.com:sub": "repo:aws-samples/sample-aws-networking-best-practices-ko:ref:refs/heads/main" }
     }
     ```
   - 권한: `bedrock:InvokeModel`(모델 `us.anthropic.claude-sonnet-4-6`)만 부여
2. **repo Secret**: `AWS_ROLE_ARN` = 위 역할 ARN
3. `sync-and-deploy.yml`·`news.yml`의 `on:`에 `schedule:` 트리거를 다시 추가
4. (sync 워크플로에 `aws s3 sync --delete`를 쓸 경우) 빌드 산출물·버킷명 가드를 먼저 추가하고,
   역할 권한을 해당 버킷/배포 ARN으로 한정 — 파괴적 명령 방지

> ⚠️ aws-samples는 **조직 repo**입니다. repo Secret 추가, Actions 허용 정책, Pages 사용이
> 조직 설정에 의해 제한될 수 있으니 먼저 권한을 확인하세요.

---

## 원본

이 프로젝트는 [aws/aws-networking-best-practices](https://github.com/aws/aws-networking-best-practices)의
한국어 번역/파생본이며 영어 원문 미러를 함께 제공합니다. 라이선스: MIT-0 (원본과 동일).
