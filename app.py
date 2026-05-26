import streamlit as st
from components.header import show_header
from components.payment_card import show_payment_cards
from components.sidebar import show_sidebar
from data.accounts import ACCOUNTS
from utils.logger import init_logger, save_log

# Konfigurasi halaman
st.set_page_config(
    page_title="Metode Pembayaran - Nurmayasari Usman",
    page_icon="💳",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Load custom CSS
def load_css():
    with open('static/style.css', 'r') as f:
        css = f.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Inisialisasi logger
init_logger()

# Load CSS
load_css()

# Tampilkan header
show_header()

# Tampilkan payment cards
show_payment_cards(ACCOUNTS, save_log)

# Tampilkan sidebar
show_sidebar()