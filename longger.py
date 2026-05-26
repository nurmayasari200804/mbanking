import streamlit as st
import json
import os
from datetime import datetime

def init_logger():
    """Inisialisasi session state untuk logging"""
    if 'copy_logs' not in st.session_state:
        # Coba load dari file jika ada
        logs = []
        if os.path.exists('logs.json'):
            try:
                with open('logs.json', 'r') as f:
                    logs = json.load(f)
            except:
                logs = []
        st.session_state.copy_logs = logs

def save_log(method_name, account_number):
    """
    Menyimpan log copy ke session state dan file
    
    Args:
        method_name: Nama metode pembayaran
        account_number: Nomor rekening/ewallet
    """
    log_entry = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'method': method_name,
        'number': account_number
    }
    
    # Simpan ke session state
    st.session_state.copy_logs.append(log_entry)