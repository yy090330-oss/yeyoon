import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="나의 웹사이트",
    layout="wide"
)

html = Path("index.html").read_text(
    encoding="utf-8"
)

st.components.v1.html(
    html,
    height=800,
    scrolling=True
)
