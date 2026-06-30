#!/usr/bin/env python3
"""
upstream(aws/aws-networking-best-practices)를 추적해 한국어 사이트를 최신화한다.

흐름:
  1. upstream 레포 clone/pull
  2. manifest.json(파일별 원문 해시)과 비교해 변경/신규 .md만 선별
  3. 변경분을 Bedrock(Claude)로 번역해 content/ , includes/ 에 기록
  4. 이미지 등 비-md 에셋은 그대로 복사
  5. upstream mkdocs.yml의 nav 라벨을 번역(캐시)해 한글 mkdocs.yml 생성

옵션:
  --all        manifest 무시하고 전체 재번역
  --no-pull    upstream pull 생략(이미 받은 상태에서 재번역)
  --only PATH  특정 content 상대경로만 번역 (반복 지정 가능)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from translate import (  # noqa: E402
    translate_markdown,
    translate_label as _tl,
    preserve_anchors,
)
from glossary import NORMALIZE as TERM_NORMALIZE, NAV_LABEL_FIX, HOME_NAV_LABEL  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
UPSTREAM = ROOT / "upstream"
UPSTREAM_REPO = "https://github.com/aws/aws-networking-best-practices.git"
CONTENT_SRC = UPSTREAM / "content"
INCLUDES_SRC = UPSTREAM / "includes"
CONTENT_ROOT = ROOT / "content"  # docs_dir (언어 폴더 ko/·en/ 의 상위)
CONTENT_DST = CONTENT_ROOT / "ko"  # 한국어 번역본 출력
CONTENT_EN = CONTENT_ROOT / "en"  # 영어 원문(upstream verbatim)
INCLUDES_DST = ROOT / "includes"
MANIFEST = ROOT / "scripts" / "manifest.json"
MKDOCS_OUT = ROOT / "mkdocs.yml"

SITE_NAME = "AWS 네트워킹 베스트 프랙티스"
SITE_DESC = "AWS 네트워킹 아키텍처 가이드와 베스트 프랙티스 — 한국어 번역본"
SITE_NAME_EN = "AWS Networking Best Practices"
SITE_DESC_EN = (
    "AWS Networking Architecture guidance and best practices "
    "(community Korean-translation mirror)"
)
KO_COPYRIGHT = (
    '본 사이트는 <a href="https://github.com/aws/aws-networking-best-practices" '
    'target="_blank">AWS Networking Best Practices</a>의 한국어 번역본입니다. '
    "원문 저작권 &copy; Amazon Web Services, Inc."
)
EN_COPYRIGHT = (
    'Community mirror of <a href="https://github.com/aws/aws-networking-best-practices" '
    'target="_blank">AWS Networking Best Practices</a>. '
    "&copy; Amazon Web Services, Inc."
)
# HOME_NAV_LABEL, NAV_LABEL_FIX, TERM_NORMALIZE는 glossary.py에서 import (단일 소스)


class PyName:
    """mkdocs.yml의 `!!python/name:...` YAML 태그를 정확히 출력하기 위한 래퍼."""

    def __init__(self, dotted: str):
        self.dotted = dotted


def _represent_pyname(dumper: yaml.Dumper, data: "PyName"):
    return dumper.represent_scalar(f"tag:yaml.org,2002:python/name:{data.dotted}", "")


yaml.add_representer(PyName, _represent_pyname)


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_manifest() -> dict:
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text())
    return {"files": {}, "nav_labels": {}}


def save_manifest(m: dict) -> None:
    MANIFEST.write_text(json.dumps(m, ensure_ascii=False, indent=2))


def pull_upstream() -> None:
    # 인자가 모두 하드코딩 상수(셸 미사용·리스트 형식) → 외부 입력 주입 경로 없음
    if (UPSTREAM / ".git").exists():
        print("• upstream pull ...")
        subprocess.run(["git", "-C", str(UPSTREAM), "pull", "--depth", "1"], check=True)  # nosec B603
    else:
        print("• upstream clone ...")
        subprocess.run(
            ["git", "clone", "--depth", "1", UPSTREAM_REPO, str(UPSTREAM)], check=True  # nosec B603
        )


def copy_assets() -> None:
    """upstream content/ 내 비-md 파일(이미지/도면)을 한국어 폴더(content/ko)로 복사.

    이미지는 언어 무관이지만, ko 마크다운의 상대 경로(assets/…)가 그대로
    동작하려면 ko 폴더 안에도 사본이 필요하다. 스타일시트는 merge_theme_css가
    루트(content/stylesheets)에 별도 병합하므로 여기서 제외한다."""
    n = 0
    for src in CONTENT_SRC.rglob("*"):
        if src.is_dir() or src.suffix == ".md":
            continue
        rel = src.relative_to(CONTENT_SRC)
        if rel.parts and rel.parts[0] == "stylesheets":
            continue
        dst = CONTENT_DST / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        n += 1
    print(f"• 에셋 {n}개 복사 완료 (content/ko)")


def copy_english() -> None:
    """upstream content/ 전체(마크다운+에셋)를 영어 폴더(content/en)로 그대로 복사.

    영어는 번역하지 않고 원문을 그대로 서빙한다. 스타일시트는 루트에서
    공유(merge_theme_css)하므로 제외한다. 매 실행 덮어쓰기(idempotent)."""
    n = 0
    for src in CONTENT_SRC.rglob("*"):
        if src.is_dir():
            continue
        rel = src.relative_to(CONTENT_SRC)
        if rel.parts and rel.parts[0] == "stylesheets":
            continue
        dst = CONTENT_EN / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        n += 1
    print(f"• 영어 원문 {n}개 복사 완료 (content/en)")


THEME_CSS_SRC = ROOT / "stylesheets" / "extra.css"
CONTENT_CSS = CONTENT_ROOT / "stylesheets" / "extra.css"  # 언어 무관 공유(docs_dir 루트)
CSS_MARKER = "/* === KO custom theme (scripts/sync.py가 병합) === */"


def merge_theme_css() -> None:
    """upstream의 extra.css 뒤에 우리 커스텀 CSS를 병합(매 실행 덮어쓰기, idempotent)."""
    upstream_css = ""
    up_file = CONTENT_SRC / "stylesheets" / "extra.css"
    if up_file.exists():
        upstream_css = up_file.read_text(encoding="utf-8")
    mine = THEME_CSS_SRC.read_text(encoding="utf-8") if THEME_CSS_SRC.exists() else ""
    CONTENT_CSS.parent.mkdir(parents=True, exist_ok=True)
    CONTENT_CSS.write_text(
        upstream_css.rstrip() + "\n\n" + CSS_MARKER + "\n" + mine,
        encoding="utf-8",
    )
    print("• 커스텀 CSS 병합 완료 (content/stylesheets/extra.css)")


def md_sources() -> list[Path]:
    files = sorted(CONTENT_SRC.rglob("*.md"))
    if INCLUDES_SRC.exists():
        files += sorted(INCLUDES_SRC.rglob("*.md"))
    return files


def dst_for(src: Path) -> Path:
    if INCLUDES_SRC.exists() and INCLUDES_SRC in src.parents:
        return INCLUDES_DST / src.relative_to(INCLUDES_SRC)
    return CONTENT_DST / src.relative_to(CONTENT_SRC)


MAX_WORKERS = 6


def translate_changed(manifest: dict, force_all: bool, only: list[str]) -> int:
    files = md_sources()
    todo = []
    for src in files:
        rel = str(src.relative_to(UPSTREAM))
        text = src.read_text(encoding="utf-8")
        h = sha(text)
        dst = dst_for(src)
        only_match = (not only) or any(o in rel for o in only)
        needs = force_all or manifest["files"].get(rel) != h or not dst.exists()
        if needs and only_match:
            todo.append((rel, src, dst, text, h))

    if not todo:
        print("• 번역할 변경분 없음")
        return 0

    print(f"• 번역 대상 {len(todo)}개 — 워커 {MAX_WORKERS}개로 병렬 처리")

    def _work(item):
        rel, src, dst, text, h = item
        ko = translate_markdown(text)
        ko = preserve_anchors(text, ko)  # 번역 헤딩에 원문 앵커 보존
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(ko, encoding="utf-8")
        return rel, h

    changed = 0
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(_work, it): it[0] for it in todo}
        for fut in as_completed(futures):
            rel = futures[fut]
            try:
                rel_done, h = fut.result()
                manifest["files"][rel_done] = h  # GIL로 dict 갱신 안전
                changed += 1
                print(f"  ✓ ({changed}/{len(todo)}) {rel_done}")
            except Exception as e:  # noqa: BLE001
                print(f"  ✗ 실패: {rel} — {e}")
    print(f"• 번역된 파일: {changed}개")
    return changed


# ---- nav 번역/생성 ----------------------------------------------------------

def translate_label(label: str, cache: dict) -> str:
    if label in cache:
        return cache[label]
    ko = _tl(label)
    cache[label] = ko
    return ko


def translate_nav(nav, cache: dict):
    """upstream nav 구조를 순회하며 라벨만 한국어로 치환."""
    if isinstance(nav, list):
        return [translate_nav(item, cache) for item in nav]
    if isinstance(nav, dict):
        out = {}
        for key, val in nav.items():
            new_key = translate_label(key, cache)
            out[new_key] = translate_nav(val, cache)
        return out
    return nav  # 문자열 경로(예: foundation/vpc.md)는 그대로


def build_mkdocs(manifest: dict) -> None:
    up_cfg_text = (UPSTREAM / "mkdocs.yml").read_text(encoding="utf-8")
    # upstream은 !!python/... 태그를 사용하므로 안전 로딩 불가 → nav만 정규식 없이 추출
    # _TolerantLoader는 SafeLoader 기반(임의 객체 생성 불가) → 안전
    up_cfg = yaml.load(up_cfg_text, Loader=_TolerantLoader)  # nosec B506
    nav_en = up_cfg.get("nav", [])  # 영어(기본 언어) nav — upstream 원본 라벨 그대로

    cache = manifest.setdefault("nav_labels", {})
    nav_ko = translate_nav(nav_en, cache)

    # 홈(index.md) 최상위 nav 라벨을 "HOME"으로, 그 외 보정 라벨 적용(한국어 한정)
    for itm in nav_ko:
        if isinstance(itm, dict):
            for k, v in list(itm.items()):
                if v == "index.md":
                    itm[HOME_NAV_LABEL] = itm.pop(k)
                elif k in NAV_LABEL_FIX:
                    itm[NAV_LABEL_FIX[k]] = itm.pop(k)

    # "소식" 섹션 — 영/한 각각 자체 콘텐츠(content/{ko,en}/news).
    # i18n folder 모드에서 nav 경로는 언어 폴더 접두사 없이 작성한다.
    if (CONTENT_DST / "news" / "whats-new.md").exists():
        nav_ko.append({
            "소식": [
                {"AWS What's New": "news/whats-new.md"},
                {"Networking 블로그 (영문)": "news/blog-networking.md"},
                {"AWS 한국 기술 블로그": "news/blog-korea.md"},
            ]
        })
    if (CONTENT_EN / "news" / "whats-new.md").exists():
        nav_en.append({
            "News": [
                {"AWS What's New": "news/whats-new.md"},
                {"Networking Blog": "news/blog-networking.md"},
                {"AWS Korea Tech Blog": "news/blog-korea.md"},
            ]
        })

    cfg = _base_config()
    cfg["nav"] = nav_ko  # 최상위 nav = 기본 언어(한국어)
    # i18n 플러그인: 한국어(루트 /) 기본, 영어(/en/). 헤더 언어 선택기 자동 생성.
    cfg["plugins"] = [
        "search",
        {
            "i18n": {
                "docs_structure": "folder",
                "reconfigure_material": True,
                "reconfigure_search": True,
                "fallback_to_default": True,
                "languages": [
                    {
                        "locale": "ko",
                        "name": "한국어",
                        "default": True,
                        "build": True,
                    },
                    {
                        "locale": "en",
                        "name": "English",
                        "build": True,
                        "site_name": SITE_NAME_EN,
                        "site_description": SITE_DESC_EN,
                        "copyright": EN_COPYRIGHT,
                        "nav": nav_en,
                    },
                ],
            }
        },
    ]
    dumped = yaml.dump(cfg, allow_unicode=True, sort_keys=False, default_flow_style=False)
    # `!!python/name:foo ''` → `!!python/name:foo` (빈 스칼라 꼬리 제거)
    dumped = re.sub(r"(!!python/name:[\w.]+) ?''", r"\1", dumped)
    MKDOCS_OUT.write_text(
        "# 이 파일은 scripts/sync.py가 생성합니다. 직접 수정하지 마세요.\n" + dumped,
        encoding="utf-8",
    )
    print("• mkdocs.yml 생성 완료 (영/한 i18n nav)")


class _TolerantLoader(yaml.SafeLoader):
    pass


# upstream mkdocs.yml의 !!python/name 태그를 무시하고 로드
def _ignore_unknown(loader, suffix, node):  # noqa: ANN001
    return None


_TolerantLoader.add_multi_constructor("tag:yaml.org,2002:python/name:", _ignore_unknown)
_TolerantLoader.add_multi_constructor("!!python/name:", _ignore_unknown)


def _base_config() -> dict:
    """한글판 MkDocs Material 설정(테마/디자인/플러그인)."""
    # 최상위는 기본 언어(한국어) 기준. 영어 값은 i18n languages.en 에서 오버라이드.
    return {
        "site_name": SITE_NAME,
        "site_description": SITE_DESC,
        "site_url": "https://aws-samples.github.io/sample-aws-networking-best-practices-ko/",
        "repo_name": "GitHub",
        "repo_url": "https://github.com/aws/aws-networking-best-practices/",
        "edit_uri": "",
        "docs_dir": "content",
        "copyright": KO_COPYRIGHT,
        "theme": {
            "name": "material",
            "language": "ko",
            "custom_dir": "overrides",
            "font": {"text": "Noto Sans KR", "code": "JetBrains Mono"},
            "palette": [
                {
                    "media": "(prefers-color-scheme: light)",
                    "scheme": "default",
                    "primary": "custom",
                    "accent": "custom",
                    "toggle": {
                        "icon": "material/weather-night",
                        "name": "다크 모드로 전환",
                    },
                },
                {
                    "media": "(prefers-color-scheme: dark)",
                    "scheme": "slate",
                    "primary": "custom",
                    "accent": "custom",
                    "toggle": {
                        "icon": "material/weather-sunny",
                        "name": "라이트 모드로 전환",
                    },
                },
            ],
            "icon": {
                "logo": "fontawesome/brands/aws",
                "repo": "fontawesome/brands/github",
            },
            "features": [
                "navigation.tracking",
                "navigation.tabs",
                "navigation.tabs.sticky",
                "navigation.top",
                "navigation.indexes",
                "navigation.footer",
                "navigation.sections",
                "toc.follow",
                "content.code.copy",
                "content.code.annotate",
                "search.suggest",
                "search.highlight",
                "search.share",
            ],
        },
        "extra": {
            "social": [
                {
                    "icon": "fontawesome/brands/github",
                    "link": "https://github.com/aws/aws-networking-best-practices",
                    "name": "원본 레포지토리",
                }
            ],
            "generator": False,
        },
        "markdown_extensions": [
            {"toc": {"permalink": True, "toc_depth": 3}},
            "admonition",
            "abbr",
            "attr_list",
            "md_in_html",
            "tables",
            "def_list",
            "footnotes",
            "pymdownx.details",
            "pymdownx.caret",
            "pymdownx.mark",
            "pymdownx.tilde",
            {"pymdownx.highlight": {"anchor_linenums": True, "line_spans": "__span"}},
            "pymdownx.inlinehilite",
            {"pymdownx.snippets": {"auto_append": ["includes/abbreviations.md"]}},
            {"pymdownx.tabbed": {"alternate_style": True}},
            {"pymdownx.tasklist": {"custom_checkbox": True}},
            {
                "pymdownx.emoji": {
                    "emoji_index": PyName("material.extensions.emoji.twemoji"),
                    "emoji_generator": PyName("material.extensions.emoji.to_svg"),
                }
            },
            {
                "pymdownx.superfences": {
                    "custom_fences": [
                        {
                            "name": "mermaid",
                            "class": "mermaid",
                            "format": PyName("pymdownx.superfences.fence_code_format"),
                        }
                    ]
                }
            },
            "pymdownx.blocks.caption",
        ],
        "extra_css": ["stylesheets/extra.css"],
        "plugins": ["search"],
    }


# title은 헤더 스크롤 시 로고 옆 타이틀/문서 제목용. 홈은 커스텀 포털(히어로)을
# 렌더하므로 nav/toc를 숨긴다. 본문은 템플릿이 대체하므로 표시되지 않는다.
def _home_frontmatter(title: str) -> str:
    return f"---\ntitle: {title}\nhide:\n  - navigation\n  - toc\n---\n\n"


def _inject_home_meta(home_md: Path, title: str) -> None:
    if not home_md.exists():
        return
    text = home_md.read_text(encoding="utf-8")
    # 기존 선두 front matter 블록 제거 후 표준 블록을 다시 입힘(멱등)
    m = re.match(r"^\s*---\n.*?\n---\n+", text, re.S)
    if m:
        text = text[m.end():]
    home_md.write_text(_home_frontmatter(title) + text, encoding="utf-8")


def apply_home_meta() -> None:
    """양 언어 홈(index.md)에 풀폭 포털 front matter를 주입한다.

    번역본·영어 원문 모두 매 sync마다 덮어써지므로 항상 적용한다."""
    _inject_home_meta(CONTENT_DST / "index.md", SITE_NAME)
    _inject_home_meta(CONTENT_EN / "index.md", SITE_NAME_EN)
    print("• 홈 포털 front matter 주입 완료 (content/ko, content/en)")


def normalize_terms() -> int:
    """전 content md에서 표준 용어로 치환(코드/URL에 없는 안전 용어만)."""
    n = 0
    for md in CONTENT_DST.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        new = text
        for src, dst in TERM_NORMALIZE.items():
            new = new.replace(src, dst)
        if new != text:
            md.write_text(new, encoding="utf-8")
            n += 1
    print(f"• 용어 정규화: {n}개 파일")
    return n


def fix_anchors() -> int:
    """재번역 없이 기존 번역물 헤딩에 원문 영어 앵커를 다시 입힌다."""
    n = 0
    for src in md_sources():
        dst = dst_for(src)
        if not dst.exists():
            continue
        src_text = src.read_text(encoding="utf-8")
        ko = dst.read_text(encoding="utf-8")
        fixed = preserve_anchors(src_text, ko)
        if fixed != ko:
            dst.write_text(fixed, encoding="utf-8")
            n += 1
    print(f"• 앵커 보정: {n}개 파일")
    return n


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="전체 재번역")
    ap.add_argument("--fix-anchors", action="store_true", help="재번역 없이 앵커만 보정")
    ap.add_argument("--no-pull", action="store_true", help="upstream pull 생략")
    ap.add_argument("--only", action="append", default=[], help="특정 경로만 번역")
    ap.add_argument("--skip-nav", action="store_true", help="nav 번역 생략")
    args = ap.parse_args()

    if args.fix_anchors:
        fix_anchors()
        return

    if not args.no_pull:
        pull_upstream()

    CONTENT_DST.mkdir(parents=True, exist_ok=True)
    CONTENT_EN.mkdir(parents=True, exist_ok=True)
    INCLUDES_DST.mkdir(exist_ok=True)

    manifest = load_manifest()
    copy_assets()
    copy_english()
    merge_theme_css()
    translate_changed(manifest, args.all, args.only)
    normalize_terms()
    apply_home_meta()
    if not args.skip_nav:
        build_mkdocs(manifest)
    save_manifest(manifest)
    print("✓ 동기화 완료")


if __name__ == "__main__":
    main()
