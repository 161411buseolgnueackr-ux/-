import streamlit as st
import streamlit.components.v1 as components
import os

# Set page layout to wide and remove default margins for full-screen feel
st.set_page_config(
    page_title="Apex 2D Aim Trainer",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default UI elements (header, footer, padding)
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
    }
    iframe {
        border: none;
        width: 100vw;
        height: 100vh;
    }
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Path to the HTML file inside the repository
html_file_path = os.path.join("htmls", "index.html")

# Read and render the HTML file
if os.path.exists(html_file_path):
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # Render full-width HTML using st.components.v1.html
    components.html(html_content, height=950, scrolling=False)
else:
    st.error(f"❌ '{html_file_path}' 파일을 찾을 수 없습니다. GitHub 저장소 내 폴더 구조(htmls/index.html)를 확인해주세요.")
