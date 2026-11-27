# Per-game facts. Verified against each game's repository on 2026-11-27 unless marked PLANNED.
MODIFIED = (2026, 11, 27)

GT = "&gt;"


def ol(items):
    return "<ol>\n" + "\n".join(f"<li>{i}</li>" for i in items) + "\n</ol>"


ANALYTICS_CAT = {
    "title": "Firebase Analytics, Crashlytics",
    "names_ko": "Google Firebase Analytics와 Crashlytics",
    "names_en": "Google Firebase Analytics and Crashlytics",
    "body_ko": """<p>앱은 게임을 개선하고 오류를 고치기 위해 Google Firebase의 Analytics와 Crashlytics를 사용합니다. 수집되는 정보는 다음과 같습니다.</p>
<ul>
<li><b>이용 통계(Analytics)</b>: 스테이지 시작·클리어·실패, 소요 시간, 힌트 사용 횟수, 획득한 별 개수, 보상형 광고 시청 여부, 튜토리얼 완료 여부, 앱 언어 설정, 앱 실행·사용 시간</li>
<li><b>오류 정보(Crashlytics)</b>: 앱이 비정상 종료되거나 오류가 발생했을 때의 오류 내용, 기기 모델과 운영체제 버전, 앱 버전, 오류 당시의 스테이지 번호</li>
<li><b>기기 단위 식별자</b>: 앱 설치별로 만들어지는 임의의 식별자(Firebase 설치 ID, 앱 인스턴스 ID)와 광고 ID</li>
</ul>
<p>이 정보는 이용자의 이름, 이메일 등과 연결되지 않으며, 게임 개선, 오류 수정, 서비스 안정성 확인 목적으로만 사용합니다. 광고 개인화나 제3자 판매에 사용하지 않습니다.</p>""",
    "body_en": """<p>To improve the game and fix errors, the App uses Google Firebase Analytics and Crashlytics. The information collected is:</p>
<ul>
<li><b>Usage statistics (Analytics)</b>: stage starts, clears and failures, time taken, number of hints used, stars earned, whether a rewarded ad was watched, whether the tutorial was completed, the app language setting, app launches and usage time</li>
<li><b>Error information (Crashlytics)</b>: the error details when the App crashes or an error occurs, device model and OS version, app version, and the stage being played at the time</li>
<li><b>Device-level identifiers</b>: random identifiers created per app installation (Firebase installation ID, app instance ID) and the advertising ID</li>
</ul>
<p>This information is not linked to your name or email. It is used only to improve the game, fix errors and check service stability. We do not use it for ad personalization or sell it to third parties.</p>""",
}


def time_extra(hosts_ko, hosts_en):
    return {
        "ko": ("시간 확인을 위한 외부 요청", f"<p>앱은 게임 내 시간 경과를 정확히 계산하기 위해 외부 서버({hosts_ko})에 현재 시각을 요청합니다. 이 요청에는 계정 정보나 게임 기록이 포함되지 않지만, 통신 과정에서 이용자의 IP 주소가 해당 서버에 전달됩니다.</p>"),
        "en": ("External requests to check the time", f"<p>To calculate elapsed in-game time accurately, the App requests the current time from external servers ({hosts_en}). These requests do not include account information or game records, but your IP address is transmitted to those servers as part of the connection.</p>"),
    }


def time_row(hosts):
    return {"ko": (hosts, "IP 주소(통신 과정에서 전달)", "현재 시각 확인"), "en": (hosts, "IP address (transmitted as part of the connection)", "Checking the current time")}


LOCAL_DEL_KO = "앱 삭제 또는 기기의 앱 데이터 삭제로 제거 (클라우드 삭제와는 별개)"
LOCAL_DEL_EN = "Removed by uninstalling the App or clearing its data on your device (separate from cloud deletion)"

GAMES = [
    {   # ads only. Verified.
        "dir": "inky-bakery", "ko": "먹물 탐정의 베이커리 클리커", "en": "Bakery Clicker", "icon": "inky-icon-s",
        "effective": (2026, 11, 1), "ads": ["rewarded"], "iap": False, "ump": True, "perms": ["net", "adid"],
        "login": {"fields": ["email", "name", "uid"], "save": "both",
                  "save_ko": "로그인한 상태에서는 진행 상황이 약 1분마다 자동으로 저장되며, 설정에서 직접 저장하거나 불러올 수도 있습니다.",
                  "save_en": "While you are signed in, your progress is saved automatically about once a minute, and you can also save or load it yourself in Settings."},
        "del_ko": f"설정 {GT} 계정 (구글) {GT} 계정·클라우드 데이터 삭제", "del_en": f"Settings {GT} Account (Google) {GT} Delete account &amp; cloud data",
        "del_steps_ko": ol(["앱 아래쪽의 <b>설정</b> 탭을 엽니다.", "<b>계정 (구글)</b> 항목에서 <b>계정·클라우드 데이터 삭제</b>를 누릅니다.", "확인 창에서 <b>삭제</b>를 누르면 클라우드에 저장된 진행 상황과 구글 연결 계정 정보가 삭제됩니다. 삭제 후에는 되돌릴 수 없으며, 이 기기에 저장된 게임 데이터는 그대로 남습니다."]),
        "del_steps_en": ol(["Open the <b>Settings</b> tab in the App.", "In the <b>Account (Google)</b> card, tap <b>Delete account &amp; cloud data</b>.", "Tap <b>Delete</b> in the confirmation dialog. Your progress saved in the cloud and your Google connection information are deleted. This cannot be undone. Game data stored on this device is kept."]),
        "local_ko": ["게임 진행 기록(코인, 단계·레벨, 레시피·설비·직원 현황, 출석·퀘스트 기록, 수집·업적, 광고 시청 횟수 등)", "설정 값(언어, 배경음악·효과음 음량)"],
        "local_en": ["Game progress (coins, stage and level, recipes, equipment and staff, attendance and quest records, collections and achievements, ad view counts, etc.)", "Settings (language, music and sound effect volume)"],
        "local_del_ko": LOCAL_DEL_KO, "local_del_en": LOCAL_DEL_EN,
    },
    {   # ads only (rewarded + interstitial), Analytics + Crashlytics. Verified.
        "dir": "cat-detective", "ko": "먹물 탐정의 숨은그림찾기", "en": "Mukmul the Black Cat: Hidden Objects", "icon": "cat-icon",
        "effective": (2026, 11, 25), "ads": ["interstitial", "rewarded"], "iap": False, "ump": True, "perms": ["net", "vibrate", "adid"],
        "analytics": ANALYTICS_CAT,
        "login": {"fields": ["email", "name", "uid"], "save": "both",
                  "save_ko": "로그인한 상태에서는 진행 상황이 바뀔 때와 앱을 내릴 때 자동으로 저장되며, 설정에서 직접 저장하거나 불러올 수도 있습니다.",
                  "save_en": "While you are signed in, your progress is saved automatically when it changes and when the App goes to the background, and you can also save or load it yourself in Settings."},
        "del_ko": f"설정 {GT} 계정과 클라우드 데이터 {GT} 삭제", "del_en": f"Settings {GT} Account &amp; cloud data {GT} Delete",
        "del_steps_ko": ol(["앱의 <b>설정</b>을 엽니다.", "<b>계정과 클라우드 데이터</b> 항목의 <b>삭제</b>를 누릅니다. 이 항목은 구글 계정으로 로그인한 상태에서만 보입니다.", "확인 창에서 삭제를 확인하면 클라우드에 저장된 진행 상황과 구글 연결 계정 정보가 삭제됩니다. 이어서 이 기기의 진행 상황도 함께 지울지 선택할 수 있습니다. 삭제 후에는 되돌릴 수 없습니다."]),
        "del_steps_en": ol(["Open <b>Settings</b> in the App.", "Tap <b>Delete</b> in the <b>Account &amp; cloud data</b> row. This row is shown only while you are signed in with a Google account.", "Confirm the deletion. Your progress saved in the cloud and your Google connection information are deleted. You are then asked whether to also erase the progress on this device. This cannot be undone."]),
        "local_ko": ["게임 진행 기록(클리어한 스테이지, 별 개수, 최단 기록)", "보유한 아이템과 받은 보상 기록", "설정 값(언어, 효과음, 배경음악, 진동)"],
        "local_en": ["Game progress (cleared stages, stars, best times)", "Items you own and rewards you have received", "Settings (language, sound effects, music, vibration)"],
        "local_del_ko": "계정 삭제 과정에서 함께 지우도록 선택하거나, 앱 삭제 또는 기기의 앱 데이터 삭제로 제거", "local_del_en": "Erased if you choose so during account deletion, or removed by uninstalling the App or clearing its data on your device",
    },
    {   # ads + IAP. Verified.
        "dir": "catapult-idle", "ko": "투석기 키우기", "en": "Catapult Idle: Siege", "icon": "catapult-icon-s",
        "effective": (2026, 11, 4), "ads": ["rewarded"], "iap": True, "iap_ko": "광고 제거, 유료 투석기", "iap_en": "ad removal and premium catapults", "noads": "skip",
        "ump": True, "perms": ["net", "adid", "billing"],
        "login": {"fields": ["email", "uid"], "save": "both",
                  "save_ko": "로그인한 상태에서는 스테이지를 클리어할 때, 상품을 구매할 때, 앱을 내릴 때 등 진행 상황이 바뀌면 자동으로 저장되며, 설정의 동기화 버튼으로 직접 저장할 수도 있습니다.",
                  "save_en": "While you are signed in, your progress is saved automatically when it changes, for example when you clear a stage, make a purchase or send the App to the background, and you can also save it yourself with the Sync button in Settings."},
        "del_ko": f"설정 {GT} 계정 · 클라우드 {GT} 계정 삭제", "del_en": f"Settings {GT} Account &amp; Cloud {GT} Delete account",
        "del_steps_ko": ol(["앱을 열고 오른쪽 위의 <b>설정</b>(톱니바퀴)을 엽니다.", "<b>계정 · 클라우드</b> 항목에서 <b>계정 삭제</b>를 누릅니다.", "확인 창에서 <b>확인</b>을 누르면 클라우드에 저장된 진행 상황과 구글 연결 계정 정보가 삭제됩니다. 삭제 후에는 되돌릴 수 없습니다."]),
        "del_steps_en": ol(["Open the App and tap <b>Settings</b> (the gear icon) at the top right.", "In the <b>Account &amp; Cloud</b> section, tap <b>Delete account</b>.", "Tap <b>OK</b> in the confirmation dialog. Your progress saved in the cloud and your Google connection information are deleted. This cannot be undone."]),
        "local_ko": ["게임 진행 기록(스테이지 진행, 코인, 업그레이드 레벨, 투석기·탄 보유 현황, 별 평가, 출석·일일 미션 기록, 광고 시청 횟수, 구매한 유료 상품의 보유 여부 등)", "설정 값(언어, 효과음 음량)"],
        "local_en": ["Game progress (stage progress, coins, upgrade levels, catapults and ammo you own, star ratings, attendance and daily mission records, ad view counts, whether you own purchased items, etc.)", "Settings (language, sound effect volume)"],
        "local_del_ko": LOCAL_DEL_KO, "local_del_en": LOCAL_DEL_EN,
    },
    {   # ads + IAP. Verified.
        "dir": "drone-storm-defense", "ko": "드론 스톰 디펜스", "en": "Drone Storm Defense", "icon": "mukmul-icon",
        "effective": (2026, 11, 8), "ads": ["rewarded"], "iap": True, "iap_ko": "광고 제거, 크리스탈 묶음", "iap_en": "ad removal and crystal packs",
        "ump": True, "perms": ["net", "adid", "billing"],
        "login": {"fields": ["email", "uid"], "save": "auto",
                  "save_ko": "로그인한 상태에서는 진행 상황이 바뀌면 자동으로 저장됩니다.",
                  "save_en": "While you are signed in, your progress is saved automatically when it changes."},
        "del_ko": f"설정 {GT} 계정 {GT} 클라우드 데이터·계정 삭제", "del_en": f"Settings {GT} Account {GT} Delete Cloud Data &amp; Account",
        "del_steps_ko": ol(["앱 아래쪽의 <b>설정</b> 탭을 엽니다.", "<b>계정</b> 항목에서 <b>클라우드 데이터·계정 삭제</b>를 누릅니다.", "확인 창에서 <b>확인</b>을 누르면 클라우드에 저장된 진행 상황과 구글 연결 계정 정보가 삭제됩니다. 삭제 후에는 되돌릴 수 없으며, 이 기기에 저장된 게임 데이터는 그대로 남습니다."]),
        "del_steps_en": ol(["Open the <b>Settings</b> tab at the bottom of the App.", "In the <b>Account</b> section, tap <b>Delete Cloud Data &amp; Account</b>.", "Tap <b>OK</b> in the confirmation dialog. Your progress saved in the cloud and your Google connection information are deleted. This cannot be undone. Game data stored on this device is kept."]),
        "local_ko": ["게임 진행 기록(스테이지 진행, 재화, 영웅·포탑·장비·룬 보유 현황, 미션·출석 기록, 도감·업적, 우편, 광고 시청 횟수, 구매한 유료 상품의 보유 여부 등)", "설정 값(언어, 음량)"],
        "local_en": ["Game progress (stage progress, currencies, heroes, turrets, equipment and runes you own, mission and attendance records, codex and achievements, mail, ad view counts, whether you own purchased items, etc.)", "Settings (language, volume)"],
        "local_del_ko": "설정의 <b>데이터 초기화</b>, 또는 앱 삭제나 기기의 앱 데이터 삭제로 제거 (클라우드 삭제와는 별개)", "local_del_en": "Removed with <b>Reset Data</b> in Settings, or by uninstalling the App or clearing its data on your device (separate from cloud deletion)",
    },
    {   # ads + IAP. Verified.
        "dir": "drone-idle", "ko": "드론 키우기", "en": "The Age of Drone Ops", "icon": "drone-idle-icon-s",
        "effective": (2026, 11, 25), "ads": ["rewarded"], "iap": True, "iap_ko": "유료 드론, 광고 제거", "iap_en": "premium drones and ad removal", "noads": "skip",
        "ump": "settings", "perms": ["net", "netstate", "adid", "billing"], "backup": True,
        "login": {"fields": ["email", "name", "uid"], "save": "manual",
                  "save_ko": "클라우드 저장과 불러오기는 이용자가 직접 누를 때만 실행됩니다.",
                  "save_en": "Cloud save and load run only when you tap them yourself."},
        "del_ko": f"설정 {GT} 계정 {GT} 계정 삭제", "del_en": f"Settings {GT} Account {GT} Delete Account",
        "del_steps_ko": ol(["로비에서 <b>설정</b>을 열고 <b>계정</b> 탭을 고릅니다.", "<b>계정 삭제</b> 항목의 <b>삭제</b>를 누릅니다.", "확인 창에서 <b>정말 삭제</b>를 누르면 클라우드에 저장된 진행 상황과 로그인 계정이 삭제되고 구글 계정 연결이 해제됩니다. 삭제 후에는 되돌릴 수 없으며, 이 기기에 저장된 게임 데이터는 그대로 남습니다."]),
        "del_steps_en": ol(["From the lobby, open <b>Settings</b> and choose the <b>Account</b> tab.", "Tap <b>Delete</b> in the <b>Delete Account</b> row.", "Tap <b>Delete now</b> in the confirmation dialog. Your progress saved in the cloud and your sign-in account are deleted and the connection to your Google account is revoked. This cannot be undone. Game data stored on this device is kept."]),
        "local_ko": ["게임 진행 기록(크레딧, 연구 포인트, 보유 드론·무기·장비와 레벨, 임무·연구 진행, 출석 기록, 도감·칭호, 광고 시청 횟수, 구매한 유료 상품의 보유 여부 등)", "설정 값(언어, 효과음·배경음악, 화질)"],
        "local_en": ["Game progress (credits, research points, drones, weapons and gear you own and their levels, mission and research progress, attendance records, codex and titles, ad view counts, whether you own purchased items, etc.)", "Settings (language, sound effects and music, graphics quality)"],
        "local_del_ko": f"설정 {GT} 데이터 {GT} <b>데이터 초기화</b>, 또는 앱 삭제나 기기의 앱 데이터 삭제로 제거 (클라우드 삭제와는 별개)", "local_del_en": f"Removed with Settings {GT} Data {GT} <b>Reset data</b>, or by uninstalling the App or clearing its data on your device (separate from cloud deletion)",
    },
    {   # ads + IAP (remove_ads). Verified. Korean-only UI.
        "dir": "fireworks-idle", "ko": "폭죽 키우기", "en": "Fireworks Idle", "icon": "fireworks-icon-s", "age": 14,
        "effective": (2026, 11, 26), "ads": ["rewarded"], "iap": True, "iap_ko": "광고 제거", "iap_en": "ad removal",
        "ump": True, "perms": ["net", "adid", "billing"], "backup": True, "also_delete_as": ["delete-account.html"],
        "login": {"fields": ["email", "name", "uid"], "save": "manual",
                  "save_ko": "클라우드 저장과 불러오기는 이용자가 직접 누를 때만 실행됩니다.",
                  "save_en": "Cloud save and load run only when you tap them yourself."},
        "del_ko": f"설정 {GT} 계정 삭제", "del_en": f"Settings (설정) {GT} Delete account (계정 삭제)",
        "del_steps_ko": ol(["앱 아래쪽의 <b>설정</b>을 엽니다.", "<b>계정 삭제</b> 항목의 <b>삭제</b>를 누릅니다. 구글 계정으로 로그인한 상태에서만 누를 수 있습니다.", "확인 창에서 <b>삭제</b>를 누르면 클라우드에 저장된 진행 상황과 로그인 계정이 삭제됩니다. 삭제 후에는 되돌릴 수 없으며, 이 기기에 저장된 게임 데이터는 그대로 남습니다."]),
        "del_steps_en": ol(["Open <b>Settings</b> (설정) at the bottom of the App. The App's menus are in Korean.", "Tap <b>삭제</b> (Delete) in the <b>계정 삭제</b> (Delete account) row. It is available only while you are signed in with a Google account.", "Tap <b>삭제</b> (Delete) in the confirmation dialog. Your progress saved in the cloud and your sign-in account are deleted. This cannot be undone. Game data stored on this device is kept."]),
        "local_ko": ["게임 진행 기록(자금, 불씨, 재료, 폭죽 모양, 주문·미션, 연구, 업적, 광고 시청 횟수, 광고 제거 구매 여부 등)", "이용자가 입력한 가게 이름", "설정 값(자동 발사, 효과음·음량)"],
        "local_en": ["Game progress (money, embers, materials, firework shapes, orders and missions, research, achievements, ad view counts, whether you purchased ad removal, etc.)", "The shop name you enter", "Settings (auto-launch, sound effects and volume)"],
        "local_del_ko": f"설정 {GT} <b>데이터 초기화</b>, 또는 앱 삭제나 기기의 앱 데이터 삭제로 제거 (클라우드 삭제와는 별개)", "local_del_en": f"Removed with Settings {GT} <b>데이터 초기화</b> (Reset data), or by uninstalling the App or clearing its data on your device (separate from cloud deletion)",
    },
    {   # ads only. Verified. Korean-only UI.
        "dir": "mars-escape", "ko": "화성 탈출기", "en": "Mars Escape", "icon": "mars-icon-s", "age": 14,
        "effective": (2026, 11, 25), "ads": ["rewarded"], "iap": False, "ump": True, "perms": ["net", "adid"],
        "extra": [time_extra("worldtimeapi.org", "worldtimeapi.org")], "rows": [time_row("worldtimeapi.org")],
        "login": {"fields": ["email", "name", "uid"], "save": "both",
                  "save_ko": "로그인한 상태에서는 약 5분마다, 그리고 앱을 내릴 때 자동으로 저장되며, 설정에서 직접 저장하거나 불러올 수도 있습니다.",
                  "save_en": "While you are signed in, your progress is saved automatically about every 5 minutes and when the App goes to the background, and you can also save or load it yourself in Settings."},
        "del_ko": f"설정 {GT} 구글 계정 {GT} 계정·데이터 삭제", "del_en": f"Settings (설정) {GT} Google account (구글 계정) {GT} Delete account and data (계정·데이터 삭제)",
        "del_steps_ko": ol(["화면 오른쪽 위의 <b>설정</b>(톱니바퀴)을 누르고, 열린 메뉴에서 <b>설정</b> 탭을 고릅니다.", "<b>구글 계정</b> 항목에서 <b>계정·데이터 삭제</b>를 누릅니다.", "확인 창에서 <b>확인</b>을 누르면 클라우드에 저장된 진행 상황과 로그인 계정이 삭제됩니다. 삭제 후에는 되돌릴 수 없으며, 이 기기에 저장된 게임 데이터는 그대로 남습니다."]),
        "del_steps_en": ol(["Tap the gear icon (<b>설정</b>, Settings) at the top right, then choose the <b>설정</b> (Settings) tab in the menu. The App's menus are in Korean.", "In the <b>구글 계정</b> (Google account) row, tap <b>계정·데이터 삭제</b> (Delete account and data).", "Tap <b>확인</b> (OK) in the confirmation dialog. Your progress saved in the cloud and your sign-in account are deleted. This cannot be undone. Game data stored on this device is kept."]),
        "local_ko": ["게임을 시작할 때 이용자가 입력한 이름(최대 10자)", "게임 진행 기록(레벨, 작물·식량, 배터리, 기지 상태, 일지·수신함, 기술, 구조 일정, 광고 시청 횟수 등)", "설정 값(효과음·배경음악 음량, 그래픽 품질)"],
        "local_en": ["The name you enter when starting the game (up to 10 characters)", "Game progress (level, crops and food, battery, base status, diary and inbox, tech, rescue schedule, ad view counts, etc.)", "Settings (sound effect and music volume, graphics quality)"],
        "local_del_ko": f"설정 {GT} <b>데이터 초기화</b>, 또는 앱 삭제나 기기의 앱 데이터 삭제로 제거 (클라우드 삭제와는 별개)", "local_del_en": f"Removed with Settings {GT} <b>데이터 초기화</b> (Reset data), or by uninstalling the App or clearing its data on your device (separate from cloud deletion)",
    },
    {   # ads + IAP. PLANNED: IAP, Google login and consent form are not live in code yet. Korean-only UI.
        "dir": "silver-route", "ko": "은빛 항로", "en": "The Silver Route", "icon": "silver-route-icon-s",
        "effective": (2026, 11, 25), "ads": ["rewarded"], "iap": True, "iap_ko": "광고 제거, 능력치 초기화, 묶음 상품", "iap_en": "ad removal, a stat reset and item packs",
        "ump": True, "perms": ["net", "adid", "billing", "notify", "alarm", "vibrate"],
        "extra": [time_extra("google.com, cloudflare.com", "google.com, cloudflare.com"),
                  {"ko": ("알림", "<p>앱은 항해 도착 등을 알리기 위해 기기 안에서 예약되는 알림을 사용합니다. 알림은 이용자가 허용한 경우에만 표시되고, 알림을 위해 개발자의 서버로 정보가 전송되지 않습니다. 알림은 앱의 설정이나 기기의 설정에서 끌 수 있습니다.</p>"),
                   "en": ("Notifications", "<p>The App uses notifications scheduled on your device, for example to tell you that a voyage has arrived. Notifications are shown only if you allow them, and no information is sent to the Developer's servers for them. You can turn them off in the App's settings or in your device settings.</p>")}],
        "rows": [time_row("google.com, cloudflare.com")],
        "login": {"fields": ["email", "name", "uid"], "save": "manual",
                  "save_ko": "클라우드 저장은 이용자가 직접 누를 때만 실행됩니다.",
                  "save_en": "Cloud save runs only when you tap it yourself."},
        "del_ko": f"설정 {GT} 계정 {GT} 계정 삭제", "del_en": f"Settings (설정) {GT} Account (계정) {GT} Delete account (계정 삭제)",
        "del_steps_ko": ol(["화면 오른쪽 위의 <b>설정</b>을 엽니다.", "<b>계정</b> 항목에서 <b>계정 삭제</b>를 누릅니다. 구글 계정으로 로그인한 상태에서만 보입니다.", "확인 창에서 <b>확인</b>을 누르면 클라우드에 저장된 진행 상황과 로그인 계정이 삭제됩니다. 삭제 후에는 되돌릴 수 없으며, 이 기기에 저장된 게임 데이터는 그대로 남습니다."]),
        "del_steps_en": ol(["Open <b>설정</b> (Settings) at the top right of the screen. The App's menus are in Korean.", "In the <b>계정</b> (Account) section, tap <b>계정 삭제</b> (Delete account). It is shown only while you are signed in with a Google account.", "Tap <b>확인</b> (OK) in the confirmation dialog. Your progress saved in the cloud and your sign-in account are deleted. This cannot be undone. Game data stored on this device is kept."]),
        "local_ko": ["게임 진행 기록(자동 저장된 진행 상황과 저장 슬롯: 재화, 선박·선원·화물, 명성, 임무·출석 기록, 광고 시청 횟수, 구매한 유료 상품의 보유 여부 등)", "설정 값(알림, 진동, 배경음악·효과음 음량)"],
        "local_en": ["Game progress (the auto-saved game and save slots: currencies, ships, crew and cargo, fame, mission and attendance records, ad view counts, whether you own purchased items, etc.)", "Settings (notifications, vibration, music and sound effect volume)"],
        "local_del_ko": f"설정 {GT} 데이터 {GT} <b>데이터 초기화</b>로 현재 진행 상황을 지울 수 있고, 저장 슬롯을 포함한 전체 데이터는 앱 삭제나 기기의 앱 데이터 삭제로 제거 (클라우드 삭제와는 별개)", "local_del_en": f"The current game can be erased with Settings {GT} Data {GT} <b>데이터 초기화</b> (Reset data); all data including save slots is removed by uninstalling the App or clearing its data on your device (separate from cloud deletion)",
    },
    {   # ads + IAP. PLANNED: IAP and Google login are stubs in code; consent form not implemented. Korean-only UI.
        "dir": "storm-arrow", "ko": "스톰 애로우", "en": "Storm Arrow", "icon": "storm-arrow-icon-s",
        "effective": (2026, 11, 25), "ads": ["rewarded"], "iap": True, "iap_ko": "코어 묶음, 스타터 팩, 광고 제거", "iap_en": "core packs, a starter pack and ad removal",
        "ump": True, "perms": ["net", "adid", "billing", "vibrate"],
        "login": {"fields": ["email", "uid"], "save": "manual",
                  "save_ko": "클라우드 저장과 불러오기는 이용자가 직접 누를 때만 실행됩니다.",
                  "save_en": "Cloud save and load run only when you tap them yourself."},
        "del_ko": f"설정 {GT} 클라우드 {GT} 삭제", "del_en": f"Settings (설정) {GT} Cloud (클라우드) {GT} Delete (삭제)",
        "del_steps_ko": ol(["로비의 메뉴에서 <b>설정</b>을 엽니다.", "<b>클라우드</b> 항목의 <b>삭제</b>를 누릅니다.", "확인 창에서 <b>확인</b>을 누르면 클라우드에 저장된 진행 상황과 로그인 계정 정보가 삭제됩니다. 삭제 후에는 되돌릴 수 없으며, 이 기기에 저장된 게임 데이터는 그대로 남습니다."]),
        "del_steps_en": ol(["Open <b>설정</b> (Settings) from the lobby menu. The App's menus are in Korean.", "Tap <b>삭제</b> (Delete) in the <b>클라우드</b> (Cloud) row.", "Tap <b>확인</b> (OK) in the confirmation dialog. Your progress saved in the cloud and your sign-in account information are deleted. This cannot be undone. Game data stored on this device is kept."]),
        "local_ko": ["게임 진행 기록(스테이지 진행, 재화, 영웅·무기 보유 현황, 미션·출석 기록, 광고 시청 횟수, 구매한 유료 상품의 보유 여부 등)", "설정 값(배경음악, 효과음, 진동)"],
        "local_en": ["Game progress (stage progress, currencies, heroes and weapons you own, mission and attendance records, ad view counts, whether you own purchased items, etc.)", "Settings (music, sound effects, vibration)"],
        "local_del_ko": f"설정 {GT} 데이터 {GT} <b>데이터 초기화</b>, 또는 앱 삭제나 기기의 앱 데이터 삭제로 제거 (클라우드 삭제와는 별개)", "local_del_en": f"Removed with Settings {GT} Data {GT} <b>데이터 초기화</b> (Reset data), or by uninstalling the App or clearing its data on your device (separate from cloud deletion)",
    },
    {   # ads + IAP. PLANNED: no ad SDK, billing or login in code yet (placeholders only).
        "dir": "mukmul-match", "ko": "먹물 사천성", "en": "Mukmul Match", "icon": "match-icon-s",
        "effective": (2026, 11, 25), "ads": ["rewarded"], "iap": True, "iap_ko": "광고 제거", "iap_en": "ad removal",
        "ump": True, "perms": ["net", "adid", "billing", "vibrate"],
        "login": {"fields": ["email", "uid"], "save": "auto", "save_ko": "", "save_en": ""},
        "del_ko": f"설정 {GT} 데이터 {GT} 계정 데이터 삭제", "del_en": f"Settings {GT} Data {GT} Delete account data",
        "del_steps_ko": ol(["앱의 <b>설정</b>을 엽니다.", "<b>데이터</b> 항목에서 <b>계정 데이터 삭제</b>를 누릅니다.", "확인 창에서 <b>확인</b>을 누르면 클라우드에 저장된 진행 상황과 구글 연결 계정 정보가 삭제됩니다. 삭제 후에는 되돌릴 수 없습니다."]),
        "del_steps_en": ol(["Open <b>Settings</b> in the App.", "In the <b>Data</b> section, tap <b>Delete account data</b>.", "Tap <b>OK</b> in the confirmation dialog. Your progress saved in the cloud and your Google connection information are deleted. This cannot be undone."]),
        "local_ko": ["게임 진행 기록(챕터·스테이지 진행, 별, 찾은 이웃 도감, 아이템, 골드, 출석·일일 도전·미션 기록, 광고 제거 구매 여부 등)", "설정 값(언어, 효과음·배경음악 음량, 진동)"],
        "local_en": ["Game progress (chapter and stage progress, stars, neighbors you have found, items, gold, attendance, daily challenge and mission records, whether you purchased ad removal, etc.)", "Settings (language, sound effect and music volume, vibration)"],
        "local_del_ko": f"설정 {GT} 데이터 {GT} <b>데이터 초기화</b>, 또는 앱 삭제나 기기의 앱 데이터 삭제로 제거", "local_del_en": f"Removed with Settings {GT} Data {GT} <b>Reset data</b>, or by uninstalling the App or clearing its data on your device",
    },
    {   # ads + IAP. PLANNED: the game has no ads, billing, login or settings in code yet (design docs only).
        "dir": "fantasy-arena", "ko": "판타지 아레나", "en": "Fantasy Arena", "icon": "mukmul-icon",
        "effective": (2026, 11, 25), "ads": ["rewarded"], "iap": True, "iap_ko": "광고 제거, 크리스탈 묶음", "iap_en": "ad removal and crystal packs",
        "ump": True, "perms": ["net", "adid", "billing"],
        "login": {"fields": ["email", "uid"], "save": "auto", "save_ko": "", "save_en": ""},
        "del_ko": "설정의 계정 삭제", "del_en": "Settings, using the account deletion option",
        "del_steps_ko": ol(["앱의 <b>설정</b>을 엽니다.", "계정 항목에서 <b>계정 삭제</b>를 누릅니다.", "확인 창에서 삭제를 확인하면 클라우드에 저장된 진행 상황과 구글 연결 계정 정보가 삭제됩니다. 삭제 후에는 되돌릴 수 없습니다."]),
        "del_steps_en": ol(["Open <b>Settings</b> in the App.", "In the account section, tap the <b>account deletion</b> option.", "Confirm the deletion. Your progress saved in the cloud and your Google connection information are deleted. This cannot be undone."]),
        "local_ko": ["게임 진행 기록(스테이지 진행, 재화, 영웅·카드 보유 현황, 광고 시청 횟수, 구매한 유료 상품의 보유 여부 등)", "설정 값(소리 등)"],
        "local_en": ["Game progress (stage progress, currencies, heroes and cards you own, ad view counts, whether you own purchased items, etc.)", "Settings (such as sound)"],
        "local_del_ko": "앱 삭제 또는 기기의 앱 데이터 삭제로 제거", "local_del_en": "Removed by uninstalling the App or clearing its data on your device",
    },
]
