#!/usr/bin/env python3
"""AWS 네트워킹 소식 수집기.

AWS What's New / AWS 한국 기술 블로그 RSS에서 **네트워킹 관련 항목만** 필터링한 뒤
Amazon Bedrock(Claude)으로 한국어로 요약해 content/news/*.md에 최신순으로 누적한다.

  python scripts/news.py --source whats-new        # 매일 오전: 전일 발표 요약
  python scripts/news.py --source blog-networking  # 매주 금: 영문 네트워킹 블로그 신규 글
  python scripts/news.py --source blog-korea       # 매주 금: 한국 블로그 네트워킹 신규 글

윈도(window_days)는 '얼마나 거슬러 올라가 볼지'이며, 중복은 manifest로 막으므로
넉넉히 잡아도(블로그 14일) 같은 글이 두 번 실리지 않는다.

이미 수록한 항목은 scripts/news-manifest.json으로 추적해 중복 추가하지 않는다.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

import boto3
import feedparser
from botocore.config import Config

from glossary import PROMPT_GLOSSARY

ROOT = Path(__file__).resolve().parent.parent
NEWS_KO = ROOT / "content" / "ko" / "news"  # 한국어 소식
NEWS_EN = ROOT / "content" / "en" / "news"  # 영어 소식
MANIFEST = ROOT / "scripts" / "news-manifest.json"
INSERT_MARKER = "<!-- NEWS:INSERT -->"
KST = timezone(timedelta(hours=9))

REGION = "us-east-1"
MODEL_ID = "us.anthropic.claude-sonnet-4-6"

FEEDS = {
    "whats-new": {
        "url": "https://aws.amazon.com/about-aws/whats-new/recent/feed/",
        "md_ko": NEWS_KO / "whats-new.md",
        "md_en": NEWS_EN / "whats-new.md",
        "window_days": 2,
        "section_kind": "daily",
        "filter": True,   # 전 서비스 발표 → 네트워킹 키워드로 필터
    },
    "blog-networking": {
        "url": "https://aws.amazon.com/blogs/networking-and-content-delivery/feed/",
        "md_ko": NEWS_KO / "blog-networking.md",
        "md_en": NEWS_EN / "blog-networking.md",
        "window_days": 14,
        "section_kind": "weekly",
        "filter": False,  # 네트워킹 전용 블로그 → 전 글 포함(필터 불필요)
    },
    "blog-korea": {
        "url": "https://aws.amazon.com/ko/blogs/korea/feed/",
        "md_ko": NEWS_KO / "blog-korea.md",
        "md_en": NEWS_EN / "blog-korea.md",
        "window_days": 14,
        "section_kind": "weekly",
        "filter": True,   # 전 주제 블로그 → 네트워킹 키워드로 필터
    },
}

# 네트워킹 관련 판별 키워드(소문자). 정밀도 우선 — 모호한 "network"/"네트워크"는 제외.
NET_KEYWORDS = [
    "vpc", "transit gateway", "direct connect", "cloudfront", "route 53", "route53",
    "network firewall", "load balanc", "elastic load", "application load balancer",
    "network load balancer", "gateway load balancer", "global accelerator",
    "vpc lattice", "privatelink", "private link", "nat gateway", "site-to-site vpn",
    "client vpn", "cloud wan", "ipam", "app mesh", "ecs service connect",
    "verified access", "internet gateway", "prefix list", "security group",
    "vpc peering", "wavelength", "local zone", "dns firewall", "elastic ip",
    "subnet", "cidr", "networking", "cloud map", "network access scope",
    "네트워킹", "로드 밸런", "로드밸런", "트랜짓 게이트웨이", "다이렉트 커넥트",
]

_client = boto3.client(
    "bedrock-runtime",
    region_name=REGION,
    config=Config(read_timeout=600, retries={"max_attempts": 4, "mode": "adaptive"}),
)

SUMMARY_SYSTEM = """\
당신은 AWS 네트워킹 소식을 한국어와 영어로 간결하게 요약하는 기술 편집자입니다.
입력은 RSS 항목 목록(JSON 배열)이며 각 원소는 {"i": 번호, "title": 제목, "desc": 본문요약}입니다.
각 항목에 대해 다음 네 필드를 생성하세요.
- ko_title: 제목을 자연스러운 한국어로. AWS 서비스/제품 고유명사는 영문 유지(Amazon VPC, AWS Transit Gateway 등).
- summary: 1~2문장의 한국어 요약. 무엇이 새로워졌는지와 네트워킹 관점의 의미를 담되 과장 없이 사실 위주로.
- en_title: 자연스러운 영어 제목. 원문 제목이 이미 영어면 그대로(고유명사 보존), 한국어면 영어로 번역.
- summary_en: 1~2문장의 영어 요약. ko summary와 동일한 사실을 담되 자연스러운 영어로.

출력은 입력과 동일한 순서·개수의 JSON 배열만 반환하세요.
각 원소는 {"i": 번호, "ko_title": "...", "summary": "...", "en_title": "...", "summary_en": "..."}.
설명·머리말·코드펜스 없이 JSON 그 자체만 출력하세요.

""" + PROMPT_GLOSSARY


def load_manifest() -> dict:
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text(encoding="utf-8"))
    return {}


def save_manifest(m: dict) -> None:
    MANIFEST.write_text(json.dumps(m, ensure_ascii=False, indent=2), encoding="utf-8")


def is_networking(*texts: str) -> bool:
    blob = " ".join(t for t in texts if t).lower()
    return any(k in blob for k in NET_KEYWORDS)


def clean_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text or "")
    text = re.sub(r"&[a-z]+;", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def entry_dt(entry) -> datetime | None:
    t = getattr(entry, "published_parsed", None) or getattr(entry, "updated_parsed", None)
    if not t:
        return None
    return datetime(*t[:6], tzinfo=timezone.utc)


def fetch_items(feed: dict, seen: set[str]) -> list[dict]:
    parsed = feedparser.parse(feed["url"])
    cutoff = datetime.now(timezone.utc) - timedelta(days=feed["window_days"])
    items = []
    for e in parsed.entries:
        link = (getattr(e, "link", "") or "").split("?")[0]
        title = getattr(e, "title", "") or ""
        desc = clean_html(getattr(e, "summary", "") or getattr(e, "description", ""))
        dt = entry_dt(e)
        if not link or link in seen:
            continue
        if dt and dt < cutoff:
            continue
        if feed.get("filter", True) and not is_networking(title, desc):
            continue
        items.append({"link": link, "title": title, "desc": desc[:600], "dt": dt})
    return items


def summarize(items: list[dict]) -> list[dict]:
    payload = [{"i": i, "title": it["title"], "desc": it["desc"]} for i, it in enumerate(items)]
    user = json.dumps(payload, ensure_ascii=False)
    last_err = None
    for attempt in range(4):
        try:
            resp = _client.converse(
                modelId=MODEL_ID,
                system=[{"text": SUMMARY_SYSTEM}],
                messages=[{"role": "user", "content": [{"text": user}]}],
                inferenceConfig={"maxTokens": 8000, "temperature": 0},
            )
            txt = resp["output"]["message"]["content"][0]["text"].strip()
            txt = re.sub(r"^```(?:json)?\s*|\s*```$", "", txt).strip()
            arr = json.loads(txt)
            by_i = {int(o["i"]): o for o in arr}
            out = []
            for i, it in enumerate(items):
                o = by_i.get(i, {})
                out.append({
                    **it,
                    "ko_title": (o.get("ko_title") or it["title"]).strip(),
                    "summary": (o.get("summary") or "").strip(),
                    "en_title": (o.get("en_title") or it["title"]).strip(),
                    "summary_en": (o.get("summary_en") or "").strip(),
                })
            return out
        except Exception as e:  # noqa: BLE001
            last_err = e
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"Bedrock summarize 실패: {last_err}")


def section_heading(kind: str, now_kst: datetime, lang: str) -> str:
    if lang == "en":
        label = "Weekly summary" if kind == "weekly" else "Daily update"
    else:
        label = "주간 요약" if kind == "weekly" else "전일 업데이트"
    return f"## {now_kst:%Y-%m-%d} · {label}"


def render_section(items: list[dict], kind: str, now_kst: datetime, lang: str) -> str:
    """lang('ko'|'en')에 맞는 제목/요약 필드로 섹션을 렌더링."""
    title_key = "en_title" if lang == "en" else "ko_title"
    summary_key = "summary_en" if lang == "en" else "summary"
    lines = [section_heading(kind, now_kst, lang), ""]
    for it in sorted(items, key=lambda x: x["dt"] or now_kst, reverse=True):
        s = it.get(summary_key, "")
        lines.append(f"- **[{it[title_key]}]({it['link']})**" + (f" — {s}" if s else ""))
    return "\n".join(lines) + "\n"


def prepend_section(md_path: Path, section: str) -> None:
    text = md_path.read_text(encoding="utf-8")
    if INSERT_MARKER not in text:
        raise RuntimeError(f"삽입 마커 없음: {md_path} ({INSERT_MARKER})")
    head, tail = text.split(INSERT_MARKER, 1)
    body = tail.lstrip("\n")
    block = section.rstrip("\n")
    if body:  # 새 섹션과 기존 본문 사이에 빈 줄 보장(헤딩 파싱 안전)
        block += "\n\n" + body
    if not block.endswith("\n"):
        block += "\n"
    md_path.write_text(head + INSERT_MARKER + "\n\n" + block, encoding="utf-8")


def run(source: str) -> int:
    feed = FEEDS[source]
    manifest = load_manifest()
    seen = set(manifest.get(source, []))
    items = fetch_items(feed, seen)
    if not items:
        print(f"• [{source}] 새 네트워킹 항목 없음")
        return 0
    print(f"• [{source}] 새 네트워킹 항목 {len(items)}개 → Bedrock 요약(영/한)")
    items = summarize(items)
    now_kst = datetime.now(KST)
    # 한국어·영어 섹션을 각 언어 파일에 삽입
    prepend_section(feed["md_ko"], render_section(items, feed["section_kind"], now_kst, "ko"))
    prepend_section(feed["md_en"], render_section(items, feed["section_kind"], now_kst, "en"))
    # manifest 갱신(최근 500개만 유지)
    manifest[source] = ([it["link"] for it in items] + list(seen))[:500]
    save_manifest(manifest)
    print(f"• [{source}] {len(items)}개 추가 → {feed['md_ko'].relative_to(ROOT)} · {feed['md_en'].relative_to(ROOT)}")
    return len(items)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", choices=list(FEEDS), required=True)
    args = ap.parse_args()
    run(args.source)


if __name__ == "__main__":
    main()
