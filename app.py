import streamlit as st
import pandas as pd
from datetime import datetime
import json
import os

# Konfigurasi halaman
st.set_page_config(
    page_title="Metode Pembayaran - Nurmayasari Usman",
    page_icon="💳",
    layout="centered"
)

# Data rekening
ACCOUNTS = [
    {"name": "Bank BRI", "number": "025901087762503", "owner": "Nurmayasari Usman", "label": "Nomor Rekening", "icon": "🏦"},
    {"name": "SeaBank", "number": "901641785010", "owner": "Nurmayasari Usman", "label": "Nomor Rekening", "icon": "🌊"},
    {"name": "DANA", "number": "082246038126", "owner": "Nurmayasari Usman", "label": "Nomor DANA", "icon": "🕊️"},
    {"name": "GoPay", "number": "082246038126", "owner": "Nurmayasari Usman", "label": "Nomor GoPay", "icon": "🍃"},
    {"name": "ShopeePay", "number": "082246038126", "owner": "nmayaaaa", "label": "Nomor ShopeePay", "icon": "🛍️"},
]

# Custom CSS
st.markdown("""
<style>
    .payment-card {
        background: white;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 16px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border: 1px solid #eee;
    }
    .card-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 16px;
        padding-bottom: 12px;
        border-bottom: 1px solid #eee;
    }
    .card-icon {
        font-size: 28px;
    }
    .card-title {
        font-size: 18px;
        font-weight: bold;
        margin: 0;
    }
    .field-label {
        font-size: 12px;
        color: #666;
        margin-bottom: 5px;
    }
    .account-number {
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .account-name {
        font-size: 14px;
        color: #666;
        margin-bottom: 16px;
    }
    .stButton button {
        width: 100%;
        background: #0052cc;
        color: white;
        border-radius: 12px;
        padding: 10px;
    }
    .stButton button:hover {
        background: #0041a8;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("💳 Metode Pembayaran")
st.caption("Klik tombol Salin untuk copy nomor")

# Tampilkan cards
for account in ACCOUNTS:
    with st.container():
        st.markdown(f"""
        <div class="payment-card">
            <div class="card-header">
                <div class="card-icon">{account['icon']}</div>
                <div class="card-title">{account['name']}</div>
            </div>
            <div class="field-label">{account['label']}</div>
            <div class="account-number">{account['number']}</div>
            <div class="account-name">{account['owner']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button(f"📋 Salin", key=account['name']):
                st.success(f"✅ Nomor {account['name']} berhasil disalin!", icon="✅")
                st.code(account['number'], language="text")
                st.balloons()

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #666;'>© 2024 - Nurmayasari Usman</p>", unsafe_allow_html=True)
