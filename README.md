# strophicgames 사이트 (정적 페이지)

GitHub Pages 로 올리는 정적 사이트입니다. 빌드 과정이 없습니다.

| 주소 | 내용 |
|---|---|
| `/` | 게임 목록 (카드 11개) |
| `/inky-bakery/privacy.html` | 먹물 탐정의 베이커리 클리커 개인정보처리방침 |
| `/inky-bakery/delete-data.html` | 먹물 탐정의 베이커리 클리커 계정·데이터 삭제 안내 (Play Console 의 "데이터 삭제 URL") |
| `/cat-detective/privacy.html`, `/cat-detective/delete-data.html` | 먹물 탐정의 숨은그림찾기 (Mukmul the Black Cat: Hidden Objects) |
| `/catapult-idle/privacy.html`, `/catapult-idle/delete-data.html` | 투석기 키우기 (Catapult Idle: Siege) (Play Console 의 개인정보처리방침 URL / 데이터 삭제 URL) |
| `/drone-storm-defense/privacy.html`, `/drone-storm-defense/delete-data.html` | 드론 스톰 디펜스 (Play Console 의 개인정보처리방침 URL / 데이터 삭제 URL) |
| `/silver-route/privacy.html`, `/silver-route/delete-data.html` | 은빛 항로 (The Silver Route) — 투석기 키우기 방침을 복사한 초안 |
| `/mukmul-match/privacy.html`, `/mukmul-match/delete-data.html` | 먹물 사천성 (Mukmul Match) — 투석기 키우기 방침을 복사한 초안 |
| `/storm-arrow/privacy.html`, `/storm-arrow/delete-data.html` | 스톰 애로우 (Storm Arrow) — 투석기 키우기 방침을 복사한 초안 |
| `/drone-idle/privacy.html`, `/drone-idle/delete-data.html` | 드론 키우기 (The Age of Drone Ops) — 투석기 키우기 방침을 복사한 초안 |
| `/mars-escape/privacy.html`, `/mars-escape/delete-data.html` | 화성 탈출기 (Mars Escape) — 투석기 키우기 방침을 복사한 초안 |
| `/fireworks-idle/privacy.html`, `/fireworks-idle/delete-data.html` | 폭죽 키우기 (Fireworks Idle) — 투석기 키우기 방침을 복사한 초안 |
| `/fantasy-arena/privacy.html`, `/fantasy-arena/delete-data.html` | 판타지 아레나 (Fantasy Arena) — 투석기 키우기 방침을 복사한 초안 |
| `/privacy.html` | 예전 주소 유지용(먹물 탐정의 숨은그림찾기 (Mukmul the Black Cat: Hidden Objects) 방침과 같은 내용) |

## 올리는 방법
기존 사이트 저장소(`cat-detective-site`)의 루트에 이 폴더 안의 파일을 그대로 복사해 커밋·푸시합니다. `.nojekyll` 파일도 같이 복사하세요.

## 디자인 파일
- `site.css` : 모든 페이지 공통 스타일(밝은/어두운 모드 자동). 기존 사이트의 `style.css`와 이름이 달라 서로 덮어쓰지 않습니다.
- `images/` : 앱 아이콘과 장면 그림. 먹물 탐정의 숨은그림찾기 (Mukmul the Black Cat: Hidden Objects) 카드는 그림이 오면 `images/` 에 넣고 `index.html` 의 `.pic.cat` 을 이미지로 바꾸면 됩니다.
