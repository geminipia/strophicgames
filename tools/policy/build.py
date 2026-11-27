#!/usr/bin/env python3
"""Generate bilingual (ko/en) privacy.html and delete-data.html for every game.
Usage: build.py <site_root>   (games config is read from games.py next to this file)
"""
import os, sys, html
from games import GAMES, MODIFIED

EMAIL = "strophicgames@gmail.com"
MAIL = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
G_PARTNER = "https://policies.google.com/technologies/partner-sites"
G_PRIVACY = "https://policies.google.com/privacy"
PLAY_TOS = "https://play.google.com/about/play-terms/"

MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


def d_ko(d):
    y, m, dd = d
    return f"{y}년 {m}월 {dd}일"


def d_en(d):
    y, m, dd = d
    return f"{MONTHS[m - 1]} {dd}, {y}"


def ul(items):
    return "<ul>\n" + "\n".join(f"<li>{i}</li>" for i in items if i) + "\n</ul>"


def join_ko(xs):
    return ", ".join(xs)


def join_en(xs):
    xs = list(xs)
    if len(xs) <= 1:
        return "".join(xs)
    if len(xs) == 2:
        return " and ".join(xs)
    return ", ".join(xs[:-1]) + " and " + xs[-1]


AD_KO = {"rewarded": "보상형 광고", "interstitial": "전면 광고", "banner": "배너 광고", "appopen": "앱 오프닝 광고"}
AD_EN = {"rewarded": "rewarded ads", "interstitial": "interstitial ads", "banner": "banner ads", "appopen": "app open ads"}
FIELD_KO = {"email": "이메일 주소", "name": "이름(구글 프로필 이름)", "uid": "계정 고유 ID", "photo": "프로필 사진 주소"}
FIELD_EN = {"email": "email address", "name": "name (Google profile name)", "uid": "unique account ID", "photo": "profile photo URL"}


PERM_KO = {"net": "인터넷 연결", "netstate": "네트워크 상태 확인", "adid": "광고 제공용 광고 ID", "billing": "Google Play 결제", "notify": "알림 표시", "alarm": "정확한 시각 알림 예약", "vibrate": "진동"}
PERM_EN = {"net": "internet access", "netstate": "network state", "adid": "the advertising ID used for ads", "billing": "Google Play billing", "notify": "showing notifications", "alarm": "scheduling exact-time alerts", "vibrate": "vibration"}


def perms_ko(g):
    return f'앱이 사용하는 권한은 {join_ko(PERM_KO[p] for p in g["perms"])}뿐입니다. 위치, 연락처, 사진, 카메라, 마이크 권한은 요청하지 않습니다.'


def perms_en(g):
    return f'The only permissions the App uses are {join_en(PERM_EN[p] for p in g["perms"])}. It does not request location, contacts, photos, camera or microphone permissions.'


class Doc:
    """Collects numbered sections for one language."""

    def __init__(self):
        self.parts = []
        self.n = 0

    def h(self, title):
        self.n += 1
        self.parts.append(f"<h2>{self.n}. {title}</h2>")
        return self.n

    def sub(self, title):
        self.parts.append(f"<h3>{title}</h3>")

    def add(self, *chunks):
        self.parts.extend(c for c in chunks if c)

    def out(self):
        return "\n".join(self.parts)


def privacy_ko(g):
    name = g["ko"]
    full = f'{name}(영문명 {g["en"]}, 이하 "앱")'
    ads = g["ads"]
    login = g.get("login")
    iap = g.get("iap")
    an = g.get("analytics")
    ads_only_rewarded = ads == ["rewarded"]
    A = g.get("age", 13)
    D = Doc()
    D.add(f'<h1>개인정보처리방침 — {name}</h1>',
          f'<p class="meta">시행일: {d_ko(g["effective"])} · 최종 수정일: {d_ko(MODIFIED)}</p>',
          f'<p>strophicgames(이하 "개발자")는 모바일 게임 {full}을 제공하며, 이용자의 개인정보를 소중히 다룹니다. 이 방침은 앱이 어떤 정보를 어떻게 다루는지 설명합니다.</p>')

    # 1 summary
    D.h("요약")
    s = []
    if login:
        fields = join_ko(FIELD_KO[f] for f in login["fields"])
        s.append("앱은 로그인 없이도 플레이할 수 있습니다. 이용자가 원할 때만 구글 계정을 연결해 게임 진행 상황을 클라우드에 백업할 수 있습니다.")
        s.append("구글 계정을 연결하지 않으면 게임 진행 상황은 이용자의 기기 안에만 저장됩니다.")
        when = '이용자가 클라우드 저장을 직접 누를 때 ' if login["save"] == "manual" else ""
        s.append(f"구글 계정을 연결하면 {fields}가 로그인 확인에 사용되고, {when}게임 진행 상황이 Google Firebase에 저장됩니다. 앱에서 언제든 계정과 클라우드 데이터를 삭제할 수 있습니다.")
    else:
        s.append("앱은 회원 가입이나 로그인 없이 플레이합니다. 게임 진행 상황은 이용자의 기기 안에만 저장되며 개발자의 서버로 전송되지 않습니다.")
    if ads_only_rewarded:
        s.append("앱에는 이용자가 선택해서 보는 보상형 광고(Google AdMob)가 포함되어 있습니다. 광고는 게임 내 보상을 받기 위해 이용자가 직접 누를 때만 표시됩니다.")
    else:
        s.append(f"앱에는 Google AdMob의 {join_ko(AD_KO[a] for a in ads)}가 포함되어 있습니다.")
    if iap:
        s.append(f'앱에는 {g["iap_ko"]} 등 유료 상품(인앱결제)이 있습니다. 결제는 Google Play 결제 시스템으로 처리되며, 개발자는 카드 번호 등 결제 수단 정보를 받거나 저장하지 않습니다.')
    else:
        s.append("앱에는 유료 상품(인앱결제)이 없습니다.")
    if an:
        s.append(f'앱은 게임 개선과 오류 수정을 위해 {an["names_ko"]}로 이용 통계와 오류 정보를 수집합니다. 이름, 이메일 등 이용자를 직접 식별하는 정보는 포함되지 않습니다.')
    s.append(perms_ko(g))
    s.append(f"앱은 만 {A}세 이상을 대상으로 합니다.")
    D.add(ul(s))

    # 2 device
    n = D.h("기기에 저장되는 정보")
    tail = "구글 계정을 연결하지 않으면 이 정보는 개발자에게 전송되지 않습니다." if login else "이 정보는 개발자에게 전송되지 않습니다."
    D.add(f"<p>앱은 다음 정보를 이용자의 기기에 저장합니다. {tail}</p>", ul(g["local_ko"]),
          "<p>이 정보는 앱을 삭제하거나 앱 데이터를 지우면 기기에서 함께 삭제됩니다." + (" 기기에서 Android 백업 기능을 켜 둔 경우, 이 정보는 이용자 본인의 Google 계정 백업에 포함될 수 있습니다." if g.get("backup") else "") + "</p>")
    if login:
        fields = join_ko(FIELD_KO[f] for f in login["fields"])
        D.sub(f"{n}-1. 구글 계정 연결과 클라우드 저장 (선택)")
        saved = '이용자가 클라우드 저장을 눌렀을 때 올라가는 게임 진행 기록' if login["save"] == "manual" else f"위 {n}번의 게임 진행 기록"
        D.add("<p>이용자가 앱에서 구글 로그인을 선택하면 Google 로그인(Firebase Authentication)을 사용합니다. 이때 다음 정보가 처리됩니다.</p>",
              ul([f"구글 계정의 {fields}(로그인 확인과 데이터 구분 목적)",
                  f"{saved}(기기 변경·재설치 시 복원 목적)",
                  "로그인·저장 요청을 처리하는 과정에서 Google Firebase가 자동으로 처리하는 기술 정보(IP 주소, 앱·기기 정보 등)"]),
              f'<p>이 정보는 Google이 제공하는 Firebase(Cloud Firestore)에 저장되며, 보안 규칙으로 계정 본인만 읽고 쓸 수 있도록 접근이 제한됩니다. {login["save_ko"]} 광고나 분석 목적으로 사용하거나 제3자에게 판매하지 않습니다. 이용자는 앱의 <b>{g["del_ko"]}</b>에서 계정 연결과 저장된 데이터를 직접 삭제할 수 있습니다.</p>')

    # 3 ads
    D.h("광고 (Google AdMob)")
    if ads_only_rewarded:
        lead = "앱은 이용자가 선택해 시청하고 게임 내 보상을 받는 보상형 광고를 표시하기 위해 Google AdMob을 사용합니다."
    else:
        lead = f"앱은 {join_ko(AD_KO[a] for a in ads)}를 표시하기 위해 Google AdMob을 사용합니다."
    D.add(f"<p>{lead} 광고가 표시되면 AdMob은 광고 제공, 성과 측정, 부정 사용 방지를 위해 다음과 같은 정보를 자동으로 수집할 수 있습니다.</p>",
          ul(["광고 식별자(Android 광고 ID)", "IP 주소와 대략적인 위치", "기기 및 운영체제 정보, 앱 사용 및 광고 상호작용 정보"]),
          f'<p>Google의 정보 처리 방식은 <a href="{G_PARTNER}">Google 정책 안내</a>와 <a href="{G_PRIVACY}">Google 개인정보처리방침</a>에서 확인할 수 있습니다.</p>')
    if iap and g.get("noads"):
        D.add("<p>광고 제거 상품을 구매하면 광고를 보지 않고도 보상을 받을 수 있습니다.</p>" if g["noads"] == "skip" else "")

    # 4 iap
    if iap:
        D.h("앱 내 결제 (Google Play 결제)")
        stored = "구매한 상품의 보유 여부는 기기에 저장되며, 구글 계정을 연결한 경우 클라우드 저장 데이터에도 포함됩니다." if login and g.get("iap_cloud", True) else "구매한 상품의 보유 여부는 기기에 저장됩니다."
        D.add(f'<p>앱은 {g["iap_ko"]} 등 유료 상품을 판매하며, 결제는 Google Play 결제 시스템으로 처리됩니다.</p>',
              ul(["카드 번호 등 결제 수단 정보와 청구 정보는 Google이 처리하며, 개발자에게 전달되거나 저장되지 않습니다.",
                  "개발자는 구매를 확인하고 상품을 지급하기 위해 Google Play로부터 구매 정보(상품 종류, 구매 여부, 주문 번호, 구매 토큰, 구매 시각)를 전달받아 처리합니다.",
                  stored,
                  "광고 제거처럼 한 번 구매하면 계속 보유하는 상품은, 앱을 다시 설치했을 때 Google Play 계정의 구매 내역을 확인해 복원합니다.",
                  "구매 내역 확인, 결제 취소와 환불은 Google Play의 정책과 절차를 따릅니다."]),
              f'<p>Google Play의 결제 정보 처리 방식은 <a href="{G_PRIVACY}">Google 개인정보처리방침</a>과 <a href="{PLAY_TOS}">Google Play 서비스 약관</a>에서 확인할 수 있습니다.</p>')

    # analytics
    if an:
        D.h(f'이용 통계와 오류 정보 ({an["title"]})')
        D.add(an["body_ko"])

    for x in g.get("extra", []):
        D.h(x["ko"][0])
        D.add(x["ko"][1])

    # processors
    D.h("제3자 서비스와 국외 이전")
    rows = [("Google LLC (AdMob)", "광고 식별자, IP 주소, 기기·앱 사용 정보", "광고 제공과 성과 측정")]
    if iap:
        rows.append(("Google LLC (Google Play 결제)", "구매 정보(결제 수단 정보는 Google만 처리)", "유료 상품 결제와 구매 확인"))
    if login:
        rows.append(("Google LLC (Firebase Authentication, Cloud Firestore)", f'{join_ko(FIELD_KO[f] for f in login["fields"])}, 게임 진행 기록', "로그인 처리와 클라우드 저장 (이용자가 구글 계정을 연결한 경우에만)"))
    if an:
        rows.append((f'Google LLC ({an["title"]})', "이용 통계, 오류 정보, 설치 단위 식별자", "게임 개선과 오류 수정"))
    rows += [r["ko"] for r in g.get("rows", [])]
    D.add("<p>앱은 아래 서비스를 이용하며, 해당 정보는 Google이 운영하는 미국 등 국외의 서버에서 처리될 수 있습니다. 개발자는 이 밖에 개인정보를 제3자에게 제공하거나 판매하지 않습니다.</p>",
          "<table><tr><th>서비스 제공자</th><th>항목</th><th>목적</th></tr>" + "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in rows) + "</table>")

    # choices
    D.h("동의 및 선택권")
    c = ["유럽경제지역(EEA), 영국 등 법령이 요구하는 지역에서는 앱이 처음 실행될 때 광고 관련 동의 창이 표시될 수 있습니다." + (" 이후 앱의 설정에서 선택을 변경할 수 있습니다." if g.get("ump") == "settings" else ""),
         "이용자는 기기의 설정 &gt; Google &gt; 광고에서 광고 ID를 재설정하거나 삭제하고, 광고 개인화를 해제할 수 있습니다."]
    if an:
        c.append("이용 통계와 오류 정보 수집을 원하지 않으면 앱을 삭제하거나 아래 문의처로 연락해 주세요.")
    D.add(ul(c))

    D.h("아동의 개인정보")
    D.add(f"<p>앱은 만 {A}세 미만을 대상으로 하지 않으며, 만 {A}세 미만 아동의 개인정보를 의도적으로 수집하지 않습니다. 만 {A}세 미만 아동의 정보가 수집된 사실을 알게 되면 해당 정보를 삭제하기 위해 조치하겠습니다.</p>")

    D.h("보관 및 삭제")
    if login:
        t = f'구글 계정을 연결하지 않은 이용자의 게임 기록은 개발자의 서버에 보관되지 않습니다. 기기에 저장된 정보는 앱 삭제 또는 앱 데이터 삭제로 제거할 수 있습니다. 구글 계정을 연결한 경우 클라우드 데이터는 앱의 <b>{g["del_ko"]}</b> 기능으로 삭제할 수 있고, 앱을 설치하지 않은 상태에서의 삭제 요청은 <a href="delete-data.html#ko">계정·데이터 삭제 안내</a>와 아래 문의처로 보낼 수 있습니다.'
    else:
        t = '개발자는 이용자의 게임 기록을 서버에 보관하지 않습니다. 기기에 저장된 정보는 앱 삭제 또는 앱 데이터 삭제로 제거할 수 있습니다. 자세한 내용은 <a href="delete-data.html#ko">계정·데이터 삭제 안내</a>를 참고해 주세요.'
    t += " 광고 관련 정보의 보관과 삭제는 Google의 정책을 따릅니다."
    if iap:
        t += " 구매 기록은 Google Play 계정에 보관되며 Google의 정책에 따라 관리됩니다."
    D.add(f"<p>{t}</p>")

    D.h("보안")
    if login:
        D.add("<p>앱은 필요한 최소한의 정보만 다룹니다. 클라우드 데이터는 Google Firebase의 보안 규칙으로 본인 계정에서만 접근할 수 있고, 전송 구간은 암호화됩니다. 개발자가 별도의 서버를 운영하지 않습니다.</p>")
    else:
        D.add("<p>앱은 필요한 최소한의 정보만 다룹니다. 게임 기록은 이용자의 기기에만 저장되며, 개발자가 별도의 서버를 운영하지 않습니다.</p>")

    D.h("방침의 변경")
    D.add("<p>이 방침은 앱의 기능이나 법령이 바뀌면 수정될 수 있으며, 수정 시 이 페이지에 최종 수정일과 함께 게시합니다.</p>")
    D.h("문의")
    D.add(f"<p>개인정보와 관련한 문의는 아래로 연락해 주세요.<br>{MAIL}</p>")
    return D.out()


def privacy_en(g):
    name = g["en"]
    ads = g["ads"]
    login = g.get("login")
    iap = g.get("iap")
    an = g.get("analytics")
    ads_only_rewarded = ads == ["rewarded"]
    A = g.get("age", 13)
    D = Doc()
    D.add(f'<h1>Privacy Policy — {name}</h1>',
          f'<p class="meta">Effective: {d_en(g["effective"])} · Last updated: {d_en(MODIFIED)}</p>',
          f'<p>strophicgames ("Developer") provides the mobile game {name} (Korean name: {g["ko"]}, the "App") and takes your privacy seriously. This policy explains what information the App handles and how.</p>')

    D.h("Summary")
    s = []
    if login:
        fields = join_en(FIELD_EN[f] for f in login["fields"])
        s.append("You can play without signing in. You may connect a Google account only if you want to back up your progress to the cloud.")
        s.append("If you do not connect a Google account, your game progress stays on your device only.")
        when = ' when you choose to save to the cloud' if login["save"] == "manual" else ""
        s.append(f"If you connect a Google account, your {fields} are used to verify your sign-in, and your game progress is stored in Google Firebase{when}. You can delete your account and cloud data at any time in the App.")
    else:
        s.append("You play without creating an account or signing in. Your game progress is stored only on your device and is not sent to the Developer's servers.")
    if ads_only_rewarded:
        s.append("The App contains rewarded ads from Google AdMob. Ads are shown only when you choose to watch one in exchange for an in-game reward.")
    else:
        s.append(f"The App contains ads from Google AdMob ({join_en(AD_EN[a] for a in ads)}).")
    if iap:
        s.append(f'The App offers paid items (in-app purchases) such as {g["iap_en"]}. Payments are processed by the Google Play billing system; the Developer does not receive or store your card number or other payment method details.')
    else:
        s.append("The App does not offer paid items (in-app purchases).")
    if an:
        s.append(f'To improve the game and fix errors, the App uses {an["names_en"]} to collect usage statistics and error information. This does not include information that directly identifies you, such as your name or email.')
    s.append(perms_en(g))
    s.append(f"The App is intended for users aged {A} and over.")
    D.add(ul(s))

    n = D.h("Information stored on your device")
    tail = "If you do not connect a Google account, this information is not sent to the Developer." if login else "This information is not sent to the Developer."
    D.add(f"<p>The App stores the following on your device. {tail}</p>", ul(g["local_en"]),
          "<p>This information is removed together with the App when you uninstall it or clear its data." + (" If Android backup is turned on for your device, this information may be included in the backup of your own Google account." if g.get("backup") else "") + "</p>")
    if login:
        fields = join_en(FIELD_EN[f] for f in login["fields"])
        D.sub(f"{n}-1. Connecting a Google account and cloud save (optional)")
        saved = 'The game progress uploaded when you choose to save to the cloud' if login["save"] == "manual" else f"The game progress described in section {n}"
        D.add("<p>If you choose to sign in with Google in the App, the App uses Google Sign-In (Firebase Authentication). The following is processed:</p>",
              ul([f"Your Google account {fields} (to verify sign-in and keep your data separate)",
                  f"{saved} (to restore it on a new device or after reinstalling)",
                  "Technical information that Google Firebase processes automatically while handling sign-in and save requests (IP address, app and device information)"]),
              f'<p>This information is stored in Firebase (Cloud Firestore) provided by Google, and access is restricted by security rules so that only the account owner can read and write it. {login["save_en"]} We do not use it for advertising or analytics, or sell it to third parties. You can disconnect your account and delete the saved data yourself in the App under <b>{g["del_en"]}</b>.</p>')

    D.h("Advertising (Google AdMob)")
    if ads_only_rewarded:
        lead = "The App uses Google AdMob to show rewarded ads, which you choose to watch in exchange for in-game rewards."
    else:
        lead = f"The App uses Google AdMob to show {join_en(AD_EN[a] for a in ads)}."
    D.add(f"<p>{lead} When an ad is shown, AdMob may automatically collect the following to serve ads, measure performance and prevent abuse:</p>",
          ul(["Advertising identifier (Android advertising ID)", "IP address and approximate location", "Device and operating system information, app usage and ad interaction information"]),
          f'<p>You can learn how Google handles this information at <a href="{G_PARTNER}">How Google uses information from sites or apps that use our services</a> and in the <a href="{G_PRIVACY}">Google Privacy Policy</a>.</p>')
    if iap and g.get("noads") == "skip":
        D.add("<p>If you purchase the ad removal item, you receive the rewards without watching ads.</p>")

    if iap:
        D.h("In-app purchases (Google Play billing)")
        stored = "Whether you own a purchased item is stored on your device and, if you connected a Google account, is included in your cloud save data." if login and g.get("iap_cloud", True) else "Whether you own a purchased item is stored on your device."
        D.add(f'<p>The App sells paid items such as {g["iap_en"]}. Payments are processed by the Google Play billing system.</p>',
              ul(["Your card number and other payment method and billing details are handled by Google and are not sent to or stored by the Developer.",
                  "To confirm a purchase and deliver the item, the Developer receives purchase information from Google Play (product type, purchase status, order number, purchase token and purchase time).",
                  stored,
                  "Items that you keep once purchased, such as ad removal, are restored by checking the purchase history of your Google Play account when you reinstall the App.",
                  "Purchase history, cancellations and refunds follow Google Play's policies and procedures."]),
              f'<p>You can learn how Google Play handles payment information in the <a href="{G_PRIVACY}">Google Privacy Policy</a> and the <a href="{PLAY_TOS}">Google Play Terms of Service</a>.</p>')

    if an:
        D.h(f'Usage statistics and error information ({an["title"]})')
        D.add(an["body_en"])

    for x in g.get("extra", []):
        D.h(x["en"][0])
        D.add(x["en"][1])

    D.h("Third-party services and international transfer")
    rows = [("Google LLC (AdMob)", "Advertising ID, IP address, device and app usage information", "Serving ads and measuring performance")]
    if iap:
        rows.append(("Google LLC (Google Play billing)", "Purchase information (payment method details are handled by Google only)", "Processing payments and confirming purchases"))
    if login:
        rows.append(("Google LLC (Firebase Authentication, Cloud Firestore)", f'Your {join_en(FIELD_EN[f] for f in login["fields"])}, game progress', "Sign-in and cloud save (only if you connect a Google account)"))
    if an:
        rows.append((f'Google LLC ({an["title"]})', "Usage statistics, error information, per-installation identifiers", "Improving the game and fixing errors"))
    rows += [r["en"] for r in g.get("rows", [])]
    D.add("<p>The App uses the services below, and the information may be processed on servers operated by Google in the United States and other countries. The Developer does not otherwise share or sell personal information to third parties.</p>",
          "<table><tr><th>Provider</th><th>Information</th><th>Purpose</th></tr>" + "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in rows) + "</table>")

    D.h("Your choices")
    c = ["In the European Economic Area (EEA), the United Kingdom and other regions where required by law, an ad-related consent form may be shown when you first launch the App." + (" You can change your choice later in the App's settings." if g.get("ump") == "settings" else ""),
         "You can reset or delete your advertising ID, or turn off ad personalization, in your device settings under Settings &gt; Google &gt; Ads."]
    if an:
        c.append("If you do not want usage statistics and error information to be collected, uninstall the App or contact us below.")
    D.add(ul(c))

    D.h("Children's privacy")
    D.add(f"<p>The App is not directed to children under {A} and we do not knowingly collect personal information from children under {A}. If we learn that information from a child under {A} has been collected, we will take steps to delete it.</p>")

    D.h("Retention and deletion")
    if login:
        t = f'Game records of users who have not connected a Google account are not stored on the Developer\'s servers. Information on your device can be removed by uninstalling the App or clearing its data. If you connected a Google account, you can delete your cloud data in the App under <b>{g["del_en"]}</b>. If the App is no longer installed, you can send a deletion request as described in <a href="delete-data.html#en">Account and data deletion</a> or to the contact below.'
    else:
        t = 'The Developer does not store your game records on any server. Information on your device can be removed by uninstalling the App or clearing its data. See <a href="delete-data.html#en">Account and data deletion</a> for details.'
    t += " Retention and deletion of advertising information follow Google's policies."
    if iap:
        t += " Purchase records are kept in your Google Play account and managed under Google's policies."
    D.add(f"<p>{t}</p>")

    D.h("Security")
    if login:
        D.add("<p>The App handles only the minimum information necessary. Cloud data can be accessed only by your own account through Google Firebase security rules, and data in transit is encrypted. The Developer does not operate any separate server.</p>")
    else:
        D.add("<p>The App handles only the minimum information necessary. Game records are stored only on your device, and the Developer does not operate any separate server.</p>")

    D.h("Changes to this policy")
    D.add("<p>This policy may be updated when the App's features or applicable laws change. Updates will be posted on this page together with the last updated date.</p>")
    D.h("Contact")
    D.add(f"<p>For questions about privacy, please contact:<br>{MAIL}</p>")
    return D.out()


def delete_ko(g):
    name = g["ko"]
    login = g.get("login")
    iap = g.get("iap")
    an = g.get("analytics")
    p = [f"<h1>계정·데이터 삭제 안내 — {name}</h1>"]
    if login:
        p.append(f"<p>{name}({g['en']})에서 구글 계정을 연결해 클라우드에 저장한 경우, 아래 방법으로 계정 정보와 저장 데이터를 삭제할 수 있습니다.</p>")
        p.append("<h2>방법 1. 앱에서 직접 삭제 (가장 빠름)</h2>")
        p.append(g["del_steps_ko"])
        p.append("<h2>방법 2. 이메일로 요청 (앱을 지웠거나 기기가 없는 경우)</h2>")
        p.append(f"<p>{MAIL}으로 <b>구글 계정 이메일 주소</b>와 앱 이름({name})을 적어 보내 주세요. 본인 확인 후 영업일 기준 7일 이내에 삭제하고 회신합니다.</p>")
    else:
        p.append(f"<p>{name}({g['en']})은 회원 가입이나 로그인 기능이 없으며, 개발자의 서버에 계정이나 게임 기록을 저장하지 않습니다. 따라서 개발자가 삭제할 계정 정보는 없고, 게임 데이터는 아래 방법으로 이용자가 직접 삭제할 수 있습니다.</p>")
        p.append("<h2>기기에 저장된 게임 데이터 삭제</h2>")
        p.append(g["del_steps_ko"])
        p.append("<h2>문의</h2>")
        p.append(f"<p>삭제와 관련해 도움이 필요하면 {MAIL}으로 앱 이름({name})을 적어 보내 주세요. 영업일 기준 7일 이내에 회신합니다.</p>")
    p.append("<h2>삭제되는 정보</h2>")
    rows = []
    if login:
        rows.append((f'구글 계정 {join_ko(FIELD_KO[f] for f in login["fields"])} (Firebase Authentication)', "삭제"))
        rows.append(("클라우드에 저장된 게임 진행 기록 (Cloud Firestore)", "삭제"))
    rows.append(("이 기기에 저장된 게임 데이터", g["local_del_ko"]))
    if iap:
        rows.append(("구매 내역 (Google Play 결제)", "Google Play 계정에 보관되며 Google의 정책에 따라 관리됩니다. 개발자는 결제 수단 정보를 보관하지 않습니다. 클라우드 데이터를 삭제해도 결제가 환불되지는 않으며, 환불은 Google Play의 정책을 따릅니다." if login else "Google Play 계정에 보관되며 Google의 정책에 따라 관리됩니다. 개발자는 결제 수단 정보를 보관하지 않습니다. 환불은 Google Play의 정책을 따릅니다."))
    if an:
        rows.append((f'이용 통계와 오류 정보 ({an["title"]})', "이름·이메일과 연결되지 않는 기기 단위 정보입니다. 앱을 삭제하면 더 이상 수집되지 않으며, 삭제를 원하면 이메일로 요청해 주세요."))
    rows.append(("광고 관련 정보 (Google AdMob)", f'Google이 관리합니다. 기기의 설정 &gt; Google &gt; 광고에서 광고 ID를 재설정하거나 삭제할 수 있습니다. (<a href="{G_PRIVACY}">Google 개인정보처리방침</a>)'))
    p.append("<table><tr><th>정보</th><th>처리</th></tr>" + "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in rows) + "</table>")
    if login and iap:
        p.append("<p>계정과 클라우드 데이터를 삭제하면 클라우드에 저장된 진행 상황과 구매한 상품의 보유 기록도 함께 삭제되며 되돌릴 수 없습니다.</p>")
    p.append('<p><a href="privacy.html#ko">개인정보처리방침 보기</a></p>')
    return "\n".join(x for x in p if x)


def delete_en(g):
    name = g["en"]
    login = g.get("login")
    iap = g.get("iap")
    an = g.get("analytics")
    p = [f"<h1>Account and Data Deletion — {name}</h1>"]
    if login:
        p.append(f"<p>If you connected a Google account in {name} ({g['ko']}) and saved your progress to the cloud, you can delete your account information and saved data in either of these ways.</p>")
        p.append("<h2>Method 1. Delete in the App (fastest)</h2>")
        p.append(g["del_steps_en"])
        p.append("<h2>Method 2. Request by email (if you uninstalled the App or no longer have the device)</h2>")
        p.append(f"<p>Email {MAIL} with your <b>Google account email address</b> and the app name ({name}). After verifying your identity, we will delete your data and reply within 7 business days.</p>")
    else:
        p.append(f"<p>{name} ({g['ko']}) has no account or sign-in feature, and the Developer does not store any account or game records on a server. There is therefore no account information for the Developer to delete, and you can delete the game data yourself as described below.</p>")
        p.append("<h2>Deleting game data stored on your device</h2>")
        p.append(g["del_steps_en"])
        p.append("<h2>Contact</h2>")
        p.append(f"<p>If you need help with deletion, email {MAIL} with the app name ({name}). We will reply within 7 business days.</p>")
    p.append("<h2>What is deleted</h2>")
    rows = []
    if login:
        rows.append((f'Google account {join_en(FIELD_EN[f] for f in login["fields"])} (Firebase Authentication)', "Deleted"))
        rows.append(("Game progress saved in the cloud (Cloud Firestore)", "Deleted"))
    rows.append(("Game data stored on this device", g["local_del_en"]))
    if iap:
        rows.append(("Purchase history (Google Play billing)", "Kept in your Google Play account and managed under Google's policies. The Developer does not keep payment method details. " + ("Deleting your cloud data does not refund purchases; refunds follow Google Play's policies." if login else "Refunds follow Google Play's policies.")))
    if an:
        rows.append((f'Usage statistics and error information ({an["title"]})', "Device-level information that is not linked to your name or email. No further data is collected after you uninstall the App. Email us if you would like it deleted."))
    rows.append(("Advertising information (Google AdMob)", f'Managed by Google. You can reset or delete your advertising ID in your device settings under Settings &gt; Google &gt; Ads. (<a href="{G_PRIVACY}">Google Privacy Policy</a>)'))
    p.append("<table><tr><th>Information</th><th>Handling</th></tr>" + "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in rows) + "</table>")
    if login and iap:
        p.append("<p>Deleting your account and cloud data also deletes the progress and the record of purchased items saved in the cloud. This cannot be undone.</p>")
    p.append('<p><a href="privacy.html#en">View the Privacy Policy</a></p>')
    return "\n".join(x for x in p if x)


SCRIPT = """<script>
(function(){
  var hash=location.hash==='#en'?'en':(location.hash==='#ko'?'ko':'');
  var q=(location.search.match(/[?&]lang=(ko|en)/)||[])[1];
  var lang=q||hash||((navigator.language||'').toLowerCase().indexOf('ko')===0?'ko':'en');
  function apply(l){document.documentElement.classList.add('js');document.querySelectorAll('.lang-block').forEach(function(b){b.hidden=b.id!==l;});
    document.querySelectorAll('.lang-switch a').forEach(function(a){a.classList.toggle('on',a.dataset.l===l);if(a.dataset.l===l)a.setAttribute('aria-current','true');else a.removeAttribute('aria-current');});
    document.querySelectorAll('[data-ko]').forEach(function(e){if(e.tagName!=='TITLE')e.textContent=e.getAttribute('data-'+l);});
    var t=document.querySelector('title[data-ko]');if(t)document.title=t.getAttribute('data-'+l);
    document.documentElement.lang=l;}
  document.querySelectorAll('.lang-switch a').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();apply(a.dataset.l);history.replaceState(null,'','#'+a.dataset.l);});});
  window.addEventListener('hashchange',function(){if(location.hash==='#en'||location.hash==='#ko')apply(location.hash.slice(1));});
  apply(lang);
})();
</script>"""


def page(g, kind):
    if kind == "privacy":
        tko, ten = f"개인정보처리방침 — {g['ko']}", f"Privacy Policy — {g['en']}"
        ko, en = privacy_ko(g), privacy_en(g)
    else:
        tko, ten = f"계정·데이터 삭제 안내 — {g['ko']}", f"Account and Data Deletion — {g['en']}"
        ko, en = delete_ko(g), delete_en(g)
    e = html.escape
    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title data-ko="{e(tko)}" data-en="{e(ten)}">{e(tko)} · {e(ten)}</title>
<meta name="description" content="strophicgames — {e(g['ko'])} ({e(g['en'])}) {'개인정보처리방침 · Privacy Policy' if kind == 'privacy' else '계정·데이터 삭제 안내 · Account and Data Deletion'}">
<link rel="icon" href="../images/{g['icon']}.webp">
<link rel="stylesheet" href="../site.css">
</head>
<body>
<div class="top"><div class="in">
  <a class="brand" href="../"><img src="../images/mukmul-icon.webp" alt="">strophicgames</a>
  <nav><a href="../#games" data-ko="게임" data-en="Games">게임</a><a href="../#about" data-ko="소개" data-en="About">소개</a><a href="mailto:{EMAIL}" data-ko="문의" data-en="Contact">문의</a></nav>
</div></div>
<main class="doc"><p class="crumb"><a href="../" data-ko="홈" data-en="Home">홈</a> › <span data-ko="{e(g['ko'])}" data-en="{e(g['en'])}">{e(g['ko'])}</span></p><div class="card">
<div class="lang-switch"><a href="#ko" data-l="ko" lang="ko">한국어</a><a href="#en" data-l="en" lang="en">English</a></div>
<section class="lang-block" id="ko" lang="ko">
{ko}
</section>
<section class="lang-block" id="en" lang="en">
{en}
</section>
</div></main>
<footer class="site"><span>© strophicgames</span><span><span data-ko="문의" data-en="Contact">문의</span> {MAIL}</span></footer>
{SCRIPT}
</body>
</html>
"""


def main():
    root = sys.argv[1]
    for g in GAMES:
        d = os.path.join(root, g["dir"])
        os.makedirs(d, exist_ok=True)
        for kind, fn in (("privacy", "privacy.html"), ("delete", "delete-data.html")):
            with open(os.path.join(d, fn), "w", encoding="utf-8") as f:
                f.write(page(g, kind))
        for extra in g.get("also_delete_as", []):
            with open(os.path.join(d, extra), "w", encoding="utf-8") as f:
                f.write(page(g, "delete"))
        print("built", g["dir"])
    legacy_root(root)


def legacy_root(root):
    g = next(x for x in GAMES if x["dir"] == "cat-detective")
    p = page(g, "privacy").replace('"../', '"').replace('href=""', 'href="./"').replace('href="#games"', 'href="./#games"').replace('href="#about"', 'href="./#about"')
    p = p.replace('href="delete-data.html#', 'href="cat-detective/delete-data.html#')
    with open(os.path.join(root, "privacy.html"), "w", encoding="utf-8") as f:
        f.write(p)


if __name__ == "__main__":
    main()
