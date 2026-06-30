"""번역 용어집 — 단일 소스(Single Source of Truth).

translate.py(번역 프롬프트)와 sync.py(번역 후 정규화)가 모두 이 파일을 사용한다.
용어를 바꾸려면 여기만 수정하면 된다.

- PROMPT_GLOSSARY : 번역 시점에 Bedrock에 주입되는 사람이 읽는 표준 용어집
- NORMALIZE       : 번역 후 content md에 적용하는 안전 치환(문맥 무관·고확신만)
- NAV_LABEL_FIX   : 자동번역된 nav 라벨 사후 보정
- HOME_NAV_LABEL  : 홈(index.md) nav 라벨
"""
from __future__ import annotations

# ── 표준 용어집(번역 프롬프트 주입용) ─────────────────────────────────────────
PROMPT_GLOSSARY = """\
[필수 용어집 — 아래 용어는 반드시 이 한국어로 통일한다]
- Foundation(기둥/핵심 영역) → 기반   ※ "기초" 금지 (단, fundamentals/basics 의미는 "기초" 유지)
- Connectivity → 연결 / Security → 보안 / Observability → 관측성   ※ "관찰 가능성"·"옵저버빌리티"·"가시성" 금지
- Application Networking → 애플리케이션 네트워킹
- segmentation → 세분화, micro-segmentation → 마이크로 세분화   ※ "세그멘테이션"·"분리" 금지
- consumer → 소비자, provider → 공급자, producer → 프로듀서   ※ "컨슈머"·"프로바이더" 금지
  (단 Kinesis consumer, Terraform provider 등 별개 제품 개념은 영문/관례 유지)
- access(명사) → 액세스 (remote access → 원격 액세스, access control → 액세스 제어)
  ※ 동사 "접근하다"(to access)는 자연스러우므로 유지
- stateful → 스테이트풀, stateless → 스테이트리스
- attachment → 어태치먼트, connection → 연결 (둘을 구분)
- blast radius → 장애 반경 / tier → 계층 / metric → 지표 / latency → 지연 시간
- route table → 라우팅 테이블, route summarization → 경로 요약
- maintainer → 메인테이너 / best practice → 모범 사례 / fundamentals → 기초
- service discovery → 서비스 디스커버리 / identity → ID, identity-aware → ID 인식
- private hosted zone → 프라이빗 호스팅 영역 / alias record → 별칭 레코드
- Local Zone → 로컬 존 / Wavelength Zone → Wavelength 존
- cross-account → 계정 간, cross-VPC → VPC 간, cross-Region → 리전 간, cross-AZ → AZ 간
  ※ 단 cross-zone load balancing은 "교차 영역 로드 밸런싱"
- device → 디바이스 / branch office → 지사 / resiliency → 복원력
- centralized → 중앙 집중식, distributed → 분산형 / reference architecture → 참조 아키텍처
- Pull Request → 풀 리퀘스트 / Conventions → 컨벤션
- Flow Logs, ECS Service Connect, Direct Connect Gateway 등 AWS 기능/제품명 → 영문 유지"""

# ── 번역 후 안전 치환(문맥 무관·고확신만; 동사/일반어는 제외) ──────────────────
NORMALIZE = {
    # 용어 표준화
    "관찰 가능성": "관측성",
    "옵저버빌리티": "관측성",
    "세그멘테이션": "세분화",
    "세그먼테이션": "세분화",
    "접근 제어": "액세스 제어",
    "접근 권한": "액세스 권한",
    "중앙집중형": "중앙 집중식",
    "중앙 집중형": "중앙 집중식",
    "분산식": "분산형",
    # 치환 부작용 조사 오류 보정(받침 없는 명사 뒤)
    "액세스으로": "액세스로",
    "액세스을": "액세스를",
    "액세스이 ": "액세스가 ",
    "액세스은": "액세스는",
    "세분화을": "세분화를",
    "세분화이 ": "세분화가 ",
    "디스커버리은": "디스커버리는",
    "디스커버리이나": "디스커버리나",
    "디스커버리을": "디스커버리를",
}

# ── nav 라벨 ──────────────────────────────────────────────────────────────────
NAV_LABEL_FIX = {"기초": "기반"}
HOME_NAV_LABEL = "HOME"
