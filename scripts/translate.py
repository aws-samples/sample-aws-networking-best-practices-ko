"""
Bedrock(Claude) 기반 EN→KO 마크다운 번역기.

MkDocs Material 문법(admonition, grid cards, 아이콘 단축코드, /// caption,
abbreviations, frontmatter)과 코드/mermaid/링크를 보존하면서 산문만 번역한다.
큰 파일은 코드펜스를 인지하는 H2 단위 청크로 나눠 번역해 출력 truncation을 방지한다.
"""
from __future__ import annotations

import re
import time
import boto3
from botocore.config import Config

from glossary import PROMPT_GLOSSARY

REGION = "us-east-1"
MODEL_ID = "us.anthropic.claude-sonnet-4-6"

# H2 단위 청킹 임계값(문자). 이보다 크면 섹션 단위로 분할 번역.
CHUNK_THRESHOLD = 14000
MAX_TOKENS = 32000

_client = boto3.client(
    "bedrock-runtime",
    region_name=REGION,
    config=Config(read_timeout=900, retries={"max_attempts": 4, "mode": "adaptive"}),
)

SYSTEM_PROMPT = """\
당신은 AWS 네트워킹 기술 문서를 영어에서 한국어로 번역하는 전문 번역가입니다.
입력은 MkDocs Material로 렌더링되는 Markdown입니다. 다음 규칙을 **엄격히** 지키세요.

[번역 대상 — 한국어로 자연스럽게 번역]
- 본문 산문, 제목(heading) 텍스트, 목록 항목 텍스트
- admonition 제목 따옴표 안 텍스트:  `!!! note "여기"` 의 "여기"
- grid cards / 표(table)의 사람이 읽는 텍스트
- `/// caption` 블록 안의 캡션 문장
- 이미지 대체텍스트 `![여기](경로)` 의 여기
- 링크의 표시 텍스트 `[여기](경로)` 의 여기 (단, 경로는 절대 변경 금지)

[절대 보존 — 원문 그대로 유지]
- YAML frontmatter(--- ... ---) 의 키와 구조
- 코드 블록(``` ```), 인라인 코드(`code`) 안의 내용
- mermaid 다이어그램 블록 내부의 코드/노드 ID/라벨 구문(라벨 안 영어 텍스트도 그대로 둔다)
- 모든 URL, 파일 경로, 앵커(.md, #anchor, ../assets/...) — 한 글자도 바꾸지 않는다
- Material 아이콘/이모지 단축코드: `:material-...:`, `:octicons-...:`, `:fontawesome-...:`
- HTML 태그와 그 속성/class (예: `<div class="grid cards" markdown>`)
- admonition 타입 키워드(note, info, tip, warning, danger, example 등)는 영어 그대로
- `/// ... ///`, `--8<--` 스니펫, `*[ABBR]:` 약어 정의의 약어 키
- Markdown 구조 문자(#, *, -, >, |, 들여쓰기, 줄바꿈, 빈 줄)를 원문과 동일하게 유지

[번역 스타일]
- AWS 서비스/제품 고유명사는 영어 원문 유지: Amazon VPC, AWS Transit Gateway, Elastic Load Balancing, PrivateLink 등
- 기술 용어는 한국어 IT 업계 관례를 따른다. 처음 등장하는 핵심 용어는 "한국어(English)" 병기 가능
- 정중하고 간결한 기술 문서체("~합니다"체). 직역투를 피하고 자연스러운 한국어로
- 약어 정의 `*[VPC]: Virtual Private Cloud` 는 키([VPC])는 유지하고 설명을 한국어로: `*[VPC]: 가상 프라이빗 클라우드(Virtual Private Cloud)`

""" + PROMPT_GLOSSARY + """

출력은 번역된 Markdown **본문만** 출력합니다. 설명, 머리말, 코드펜스 감싸기 없이 변환된 내용 그 자체만 반환하세요."""


def _converse(text: str) -> str:
    last_err = None
    for attempt in range(4):
        try:
            resp = _client.converse(
                modelId=MODEL_ID,
                system=[{"text": SYSTEM_PROMPT}],
                messages=[{"role": "user", "content": [{"text": text}]}],
                inferenceConfig={"maxTokens": MAX_TOKENS, "temperature": 0},
            )
            return resp["output"]["message"]["content"][0]["text"]
        except Exception as e:  # noqa: BLE001
            last_err = e
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"Bedrock converse failed: {last_err}")


def _split_h2_fence_aware(md: str) -> list[str]:
    """코드펜스 밖에 있는 '## ' 헤더 기준으로 분할. 펜스 내부는 무시."""
    lines = md.splitlines(keepends=True)
    chunks: list[str] = []
    cur: list[str] = []
    in_fence = False
    fence_re = re.compile(r"^\s*(```|~~~)")
    for line in lines:
        if fence_re.match(line):
            in_fence = not in_fence
        is_h2 = (not in_fence) and line.startswith("## ")
        if is_h2 and cur:
            chunks.append("".join(cur))
            cur = [line]
        else:
            cur.append(line)
    if cur:
        chunks.append("".join(cur))
    return chunks


def translate_markdown(md: str) -> str:
    """마크다운 문자열을 한국어로 번역해 반환."""
    if not md.strip():
        return md
    if len(md) <= CHUNK_THRESHOLD:
        return _converse(md).rstrip("\n") + "\n"

    parts = _split_h2_fence_aware(md)
    out: list[str] = []
    for part in parts:
        if not part.strip():
            out.append(part)
            continue
        out.append(_converse(part).rstrip("\n"))
    return "\n\n".join(out).rstrip("\n") + "\n"


import unicodedata

_FENCE_RE = re.compile(r"^\s*(```|~~~)")
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
# `{#id}` 와 `{ #id }`(중괄호 안 공백) 모두 매칭 — 후자를 못 잡으면 앵커가 중복 생성됨
_EXPLICIT_ID_RE = re.compile(r"\{\s*#([^}]+?)\s*\}\s*$")


def _slugify(text: str) -> str:
    """python-markdown toc 기본 slugify와 동일 규칙으로 영어 앵커 생성."""
    text = re.sub(r"\{[^}]*\}", "", text)            # 기존 {#id}/{ #id } 속성 블록 제거
    # 인라인 마크다운 제거: 아이콘, 코드, 링크 표시, 강조
    text = re.sub(r":[\w-]+:", "", text)            # :material-...:
    text = re.sub(r"`([^`]*)`", r"\1", text)         # `code`
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)  # [t](u)
    text = re.sub(r"[*_~]", "", text)
    value = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^\w\s-]", "", value).strip().lower()
    return re.sub(r"[-\s]+", "-", value)


def _headings(md: str) -> list[tuple[int, str]]:
    """(줄 인덱스, 헤딩 텍스트) 목록 — 코드펜스 밖만."""
    out = []
    in_fence = False
    for i, line in enumerate(md.splitlines()):
        if _FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = _HEADING_RE.match(line)
        if m:
            out.append((i, m.group(2)))
    return out


def preserve_anchors(src_md: str, ko_md: str) -> str:
    """번역으로 바뀐 헤딩에 원문 영어 앵커를 {#slug}로 부여해 내부 링크를 보존.

    원문/번역 헤딩 개수가 같을 때만 위치 매핑으로 적용한다(불일치 시 원본 유지).
    """
    src_h = _headings(src_md)
    if not src_h:
        return ko_md
    ko_lines = ko_md.splitlines()
    ko_h = _headings(ko_md)
    if len(src_h) != len(ko_h):
        return ko_md  # 안전: 구조 불일치 시 손대지 않음

    for (_, src_text), (ko_idx, ko_text) in zip(src_h, ko_h):
        # 번역 헤딩에 이미 명시적 id가 있으면 그대로 둔다
        if _EXPLICIT_ID_RE.search(ko_text):
            continue
        # 원문에 명시적 id가 있으면 그것을, 없으면 원문 텍스트의 slug를 사용
        m = _EXPLICIT_ID_RE.search(src_text)
        anchor = m.group(1) if m else _slugify(src_text)
        if not anchor:
            continue
        line = ko_lines[ko_idx]
        ko_lines[ko_idx] = f"{line.rstrip()} {{#{anchor}}}"
    return "\n".join(ko_lines) + ("\n" if ko_md.endswith("\n") else "")


_LABEL_SYSTEM = """\
당신은 AWS 기술 문서 사이트의 내비게이션 메뉴 라벨을 영어에서 한국어로 번역합니다.
입력은 메뉴에 표시되는 **짧은 라벨 한 개**입니다.

규칙:
- 출력은 번역된 라벨 텍스트 **한 줄만**. 설명·문장·마침표·따옴표를 절대 추가하지 마세요.
- 절대 내용을 지어내거나 확장하지 마세요. 입력에 없는 정보를 추가하면 안 됩니다.
- AWS 서비스/제품 고유명사는 영어 원문 유지: AWS Organizations, Amazon VPC, CIDR, IPAM, DNS 등
- 일반 단어는 자연스러운 한국어로: Introduction→소개, Connectivity→연결, Security→보안,
  Observability→관측성, Decision Map→의사결정 맵, Foundation→기반

예시:
입력: Introduction → 출력: 소개
입력: Amazon VPC → 출력: Amazon VPC
입력: CIDR Planning → 출력: CIDR 계획"""


def translate_label(label: str) -> str:
    """내비게이션 라벨 한 개를 한국어로 번역(환각 방지용 엄격 프롬프트)."""
    label = label.strip()
    if not label:
        return label
    for attempt in range(4):
        try:
            resp = _client.converse(
                modelId=MODEL_ID,
                system=[{"text": _LABEL_SYSTEM}],
                messages=[{"role": "user", "content": [{"text": label}]}],
                inferenceConfig={"maxTokens": 200, "temperature": 0},
            )
            out = resp["output"]["message"]["content"][0]["text"].strip()
            # 안전장치: 모델이 여러 줄을 뱉으면 첫 줄만, 비정상적으로 길면 원문 유지
            out = out.splitlines()[0].strip() if out else label
            if len(out) > max(60, len(label) * 4):
                return label
            return out or label
        except Exception:  # noqa: BLE001
            time.sleep(2 * (attempt + 1))
    return label


if __name__ == "__main__":
    import sys
    print(translate_markdown(sys.stdin.read()))
