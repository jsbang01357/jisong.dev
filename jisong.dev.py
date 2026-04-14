import streamlit as st
from apps import APPS, LINKS


def main():
    st.set_page_config(
        page_title="jisong.dev",
        page_icon="🔗",
        layout="wide",
    )

    @st.cache_data(ttl=3600*12)
    def get_sun_times():
        import urllib.request
        import json
        from datetime import datetime, timezone, timedelta
        try:
            url = "https://api.sunrise-sunset.org/json?lat=37.5665&lng=126.9780&formatted=0"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=3) as response:
                data = json.loads(response.read().decode())
            sunrise = datetime.fromisoformat(data['results']['sunrise'].replace('Z', '+00:00'))
            sunset = datetime.fromisoformat(data['results']['sunset'].replace('Z', '+00:00'))
            return sunrise, sunset
        except Exception:
            kst = timezone(timedelta(hours=9))
            n = datetime.now(kst)
            return n.replace(hour=6, minute=0, second=0).astimezone(timezone.utc), n.replace(hour=18, minute=0, second=0).astimezone(timezone.utc)

    # 초기 상태 설정 (가장 먼저 수행)
    if 'dark_mode' not in st.session_state:
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        sunrise, sunset = get_sun_times()
        st.session_state.dark_mode = not (sunrise <= now < sunset)

    # UI 상단 레이아웃
    col1, col2 = st.columns([10, 1])
    with col2:
        # 고정된 레이블을 사용하거나, key 만으로 상태를 관리하도록 단순화합니다.
        # 레이블이 바뀌면 Streamlit이 위젯을 새로 생성하여 '두 번 클릭' 현상이 발생할 수 있습니다.
        st.toggle("🌙", key="dark_mode")

    if st.session_state.dark_mode:
        bg_color = "#111827"
        card_bg = "#1f2937"
        text_color = "#f3f4f6"
        border_color = "rgba(255, 255, 255, 0.2)" # 조금 더 선명하게 변경
        desc_color = "#9ca3af"
        btn_hover_bg = "rgba(99, 102, 241, 0.15)"
    else:
        bg_color = "#f9fafb"
        card_bg = "#ffffff"
        text_color = "#111827"
        border_color = "rgba(0, 0, 0, 0.15)"
        desc_color = "#6b7280"
        btn_hover_bg = "rgba(99, 102, 241, 0.1)"

    # --- CSS ---
    st.markdown(f"""
        <style>
        @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');

        /* 폰트 및 글로벌 텍스트 */
        html, body, [class*="css"] {{
            font-family: 'Pretendard', sans-serif !important;
        }}

        [data-testid="stAppViewContainer"] {{
            background-color: {bg_color} !important;
        }}
        .stMarkdown, p, h1, h2, h3, h4, h5, h6, span {{
            color: {text_color} !important;
        }}

        /* 타이틀 배경 그라데이션 포인트 */
        .gradient-header {{
            background: linear-gradient(135deg, #6366f1 0%, #06b6d4 100%);
            padding: 2.5rem;
            border-radius: 20px;
            margin-bottom: 2rem;
            box-shadow: 0 10px 30px rgba(99, 102, 241, 0.2);
            display: flex;
            align-items: center;
            gap: 1.5rem;
        }}
        .gradient-header img {{
            width: 80px;
            height: 80px;
            border-radius: 50%;
            object-fit: contain;
            flex-shrink: 0;
            background-color: rgba(255, 255, 255, 0.2);
            padding: 5px;
        }}
        .gradient-header-texts {{
            display: flex;
            flex-direction: column;
        }}
        .gradient-header h2 {{
            color: white !important;
            margin: 0;
            font-size: 2.4rem;
            font-weight: 800;
            letter-spacing: -0.02em;
        }}
        .gradient-header p {{
            color: rgba(255, 255, 255, 0.9) !important;
            margin: 0;
            margin-top: 0.5rem;
            font-size: 1.1rem;
        }}

        /* 앱 카드 */
        .app-card {{
            background-color: {card_bg};
            border: 1px solid {border_color};
            border-radius: 16px;
            padding: 1.4rem 1.6rem;
            margin-bottom: 1rem;
            height: 100%;
            box-sizing: border-box;
            transition: all 0.3s ease;
        }}
        .app-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
        }}
        
        .app-card .app-icon {{ font-size: 1.8rem; margin-bottom: 0.5rem; }}
        .app-card .app-name {{ font-size: 1.1rem; font-weight: 700; margin: 0 0 0.3rem 0; color: {text_color} !important; }}
        .app-card .app-desc {{ font-size: 0.85rem; color: {desc_color} !important; margin: 0; }}

        /* 링크 카드 */
        .link-card {{
            background-color: {card_bg};
            border: 1px solid {border_color};
            border-radius: 16px;
            padding: 1.2rem 1.4rem;
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
            gap: 0.8rem;
            transition: all 0.3s ease;
        }}
        .link-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
        }}
        .link-card .link-icon {{ font-size: 1.4rem; }}
        .link-card .link-name {{ font-size: 1rem; font-weight: 600; margin: 0; color: {text_color} !important; }}
        .link-card .link-desc {{ font-size: 0.8rem; color: {desc_color} !important; margin: 0; }}

        /* 섹션 레이블 */
        .section-label {{
            font-size: 0.8rem;
            font-weight: 700;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            color: {desc_color} !important;
            margin: 0 0 1rem 0;
        }}

        /* 버튼 스타일 전면 수정 */
        div[data-testid="stLinkButton"] a {{
            background-color: transparent !important;
            border: 1px solid {border_color} !important;
            color: {text_color} !important;
            transition: all 0.2s ease !important;
            border-radius: 10px !important;
            text-decoration: none !important;
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            padding: 0.5rem 1rem !important;
        }}
        /* 모든 하위 텍스트 요소 색상 강제 지정 */
        div[data-testid="stLinkButton"] a *, 
        div[data-testid="stLinkButton"] button * {{
            color: {text_color} !important;
        }}
        
        div[data-testid="stLinkButton"] a:hover {{
            border-color: #6366f1 !important;
            background-color: {btn_hover_bg} !important;
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.2) !important;
        }}
        div[data-testid="stLinkButton"] a:hover * {{
            color: #6366f1 !important;
        }}
        </style>
    """, unsafe_allow_html=True)

    import base64
    import os
    try:
        img_path = os.path.join(os.path.dirname(__file__), 'choonsik.png')
        with open(img_path, "rb") as f:
            img_b64 = base64.b64encode(f.read()).decode()
            img_html = f'<img src="data:image/png;base64,{img_b64}" alt="춘식이">'
    except Exception:
        img_html = ""

    # --- 헤더 ---
    st.markdown(f"""
        <div class="gradient-header">
            {img_html}
            <div class="gradient-header-texts">
                <h2>jisong.dev</h2>
                <p>지송의 프로젝트 허브</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    def render_app_cards(apps_list):
        cols = st.columns(3, gap="medium")
        for i, app in enumerate(apps_list):
            with cols[i % 3]:
                st.markdown(f"""
                    <div class="app-card">
                        <div class="app-icon">{app['icon']}</div>
                        <p class="app-name">{app['name']}</p>
                        <p class="app-desc">{app['desc']}</p>
                    </div>
                """, unsafe_allow_html=True)
                btn_col1, btn_col2 = st.columns(2)
                with btn_col1:
                    st.link_button("열기 →", app["url"], use_container_width=True)
                with btn_col2:
                    st.link_button("GitHub", app["github"], use_container_width=True)

    # --- Frame Series 섹션 ---
    st.markdown('<p class="section-label">Frame Series</p>', unsafe_allow_html=True)
    frame_apps = [app for app in APPS if "frame" in app["name"].lower()]
    render_app_cards(frame_apps)

    st.divider()

    # --- Other Projects 섹션 ---
    st.markdown('<p class="section-label">Other Projects</p>', unsafe_allow_html=True)
    other_apps = [app for app in APPS if "frame" not in app["name"].lower()]
    render_app_cards(other_apps)

    st.divider()

    # --- More 섹션 ---
    st.markdown('<p class="section-label">More</p>', unsafe_allow_html=True)

    link_cols = st.columns(len(LINKS), gap="medium")
    for i, link in enumerate(LINKS):
        with link_cols[i]:
            st.markdown(f"""
                <div class="link-card">
                    <span class="link-icon">{link['icon']}</span>
                    <div>
                        <p class="link-name">{link['name']}</p>
                        <p class="link-desc">{link['desc']}</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button(f"{link['name']} 바로가기", link["url"], use_container_width=True)

    # --- 푸터 ---
    st.markdown("""
        <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            padding: 0.6rem 1.5rem;
            font-size: 0.72rem;
            color: gray;
            opacity: 0.6;
            text-align: right;
        }
        </style>
        <div class="footer">@ Jisong Bang 2026</div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
