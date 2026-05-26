import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Payment Information - NURMAYASARI USMAN",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
with open('styles.css', 'r') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load JavaScript
with open('script.js', 'r') as f:
    js_code = f.read()

# Title Section
st.markdown("""
<div class="header-container">
    <h1>💳 Payment Information</h1>
    <p>NURMAYASARI USMAN</p>
</div>
""", unsafe_allow_html=True)

# Payment data
payment_data = [
    {
        "bank": "BRI",
        "icon": "🏦",
        "account_number": "025901087762503",
        "account_name": "NURMAYASARI USMAN",
        "color": "#0055A4"
    },
    {
        "bank": "SEABANK",
        "icon": "🌊",
        "account_number": "901641785010",
        "account_name": "NURMAYASARI USMAN",
        "color": "#00A86B"
    },
    {
        "bank": "DANA",
        "icon": "📱",
        "account_number": "082246038126",
        "account_name": "NURMAYASARI USMAN",
        "color": "#1E90FF"
    },
    {
        "bank": "GOPAY",
        "icon": "🟢",
        "account_number": "082246038126",
        "account_name": "NURMAYASARI USMAN",
        "color": "#00AA5E"
    },
    {
        "bank": "SHOPEEPAY",
        "icon": "🛍️",
        "account_number": "082246038126",
        "account_name": "nmayaaaa",
        "color": "#EE4D2D"
    }
]

# Create columns for responsive grid
cols = st.columns(2)

for idx, payment in enumerate(payment_data):
    with cols[idx % 2]:
        st.markdown(f"""
        <div class="payment-card" style="border-left: 4px solid {payment['color']};">
            <div class="card-header">
                <span class="bank-icon">{payment['icon']}</span>
                <h2 class="bank-name">{payment['bank']}</h2>
            </div>
            <div class="card-body">
                <div class="account-field">
                    <label>Account Number</label>
                    <div class="account-number">
                        {payment['account_number']}
                        <button class="copy-btn" onclick="copyToClipboard('{payment['account_number']}')">
                            📋 Copy
                        </button>
                    </div>
                </div>
                <div class="account-field">
                    <label>Account Name</label>
                    <div class="account-name">{payment['account_name']}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# QR Code Section (if you want to add QR codes later)
st.markdown("""
<div class="info-section">
    <h3>📌 Quick Actions</h3>
    <p>Click the copy button next to any account number to copy it to clipboard.</p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown(f"""
<div class="footer">
    <p>Last updated: {datetime.now().strftime('%B %d, %Y')}</p>
    <p>© NURMAYASARI USMAN - All payment methods verified</p>
</div>
""", unsafe_allow_html=True)

# Inject JavaScript
components.html(f"""
<script>{js_code}</script>
""", height=0)

# Sidebar with additional info
with st.sidebar:
    st.markdown("## ℹ️ Information")
    st.markdown("---")
    st.markdown("### Supported Payment Methods")
    for pay in payment_data:
        st.markdown(f"- {pay['icon']} **{pay['bank']}**")
    st.markdown("---")
    st.markdown("### 💡 Tips")
    st.markdown("""
    - Double-check the account number before transferring
    - Save this page for quick access
    - Contact me if you need confirmation
    """)