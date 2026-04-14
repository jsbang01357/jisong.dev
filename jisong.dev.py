import streamlit as st
from apps import APPS, LINKS, CLOUD


def main():
    st.set_page_config(
        page_title="jisong.dev",
        page_icon="🔗",
        layout="wide",
    )

    # --- CSS ---
    st.markdown("""
        <style>
        /* 전체 배경 */
        [data-testid="stAppViewContainer"] {
            background-color: var(--background-color);
        }

        /* 앱 카드 */
        .app-card {
            background-color: var(--secondary-background-color);
            border: 1px solid rgba(128, 128, 128, 0.2);
            border-radius: 12px;
            padding: 1.2rem 1.4rem;
            margin-bottom: 1rem;
            height: 100%;
            box-sizing: border-box;
        }
        .app-card .app-icon {
            font-size: 1.6rem;
            margin-bottom: 0.4rem;
        }
        .app-card .app-name {
            font-size: 1.05rem;
            font-weight: 600;
            margin: 0 0 0.2rem 0;
        }
        .app-card .app-desc {
            font-size: 0.82rem;
            color: gray;
            margin: 0;
        }

        /* 링크 카드 */
        .link-card {
            background-color: var(--secondary-background-color);
            border: 1px solid rgba(128, 128, 128, 0.2);
            border-radius: 12px;
            padding: 1rem 1.2rem;
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }
        .link-card .link-icon {
            font-size: 1.2rem;
        }
        .link-card .link-name {
            font-size: 0.95rem;
            font-weight: 500;
            margin: 0;
        }
        .link-card .link-desc {
            font-size: 0.78rem;
            color: gray;
            margin: 0;
        }

        /* 섹션 레이블 */
        .section-label {
            font-size: 0.75rem;
            font-weight: 600;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: gray;
            margin: 0 0 0.8rem 0;
        }

        /* 버튼 간격 */
        [data-testid="stLinkButton"] {
            margin-top: 0.4rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- 헤더 ---
    st.markdown("## jisong.dev")
    st.caption("지송의 프로젝트 허브")
    st.divider()

    # --- Cloud 섹션 ---
    st.markdown('<p class="section-label">Cloud</p>', unsafe_allow_html=True)

    cloud_cols = st.columns(3, gap="medium")
    with cloud_cols[0]:
        st.markdown(f"""
            <div class="app-card">
                <div class="app-icon">{CLOUD['icon']}</div>
                <p class="app-name">{CLOUD['name']}</p>
                <p class="app-desc">{CLOUD['desc']}</p>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("열기 →", CLOUD["url"], use_container_width=True)

    st.divider()

    # --- Apps 섹션 ---
    st.markdown('<p class="section-label">Apps</p>', unsafe_allow_html=True)

    cols = st.columns(3, gap="medium")
    for i, app in enumerate(APPS):
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
