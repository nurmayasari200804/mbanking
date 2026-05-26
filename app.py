import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Info Pembayaran", layout="centered")

# Load HTML
html_file = Path("templates/index.html").read_text(encoding="utf-8")

st.markdown(html_file, unsafe_allow_html=True)
