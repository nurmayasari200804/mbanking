import streamlit as st

def show_header():
    """Menampilkan header halaman"""
    st.markdown("""
    <div class="custom-header">
        <h1>💳 Metode Pembayaran</h1>
        <p>Klik tombol Salin untuk copy nomor</p>
    </div>
    """, unsafe_allow_html=True)