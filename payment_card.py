import streamlit as st

def show_payment_cards(accounts, save_log_func):
    """
    Menampilkan semua payment cards
    
    Args:
        accounts: List of account dictionaries
        save_log_func: Function to save copy log
    """
    for account in accounts:
        with st.container():
            # Card HTML
            card_html = f"""
            <div class="payment-card">
                <div class="card-header">
                    <span class="{account['icon_class']}" style="font-size: 24px;">{account['icon']}</span>
                    <h3>{account['name']}</h3>
                </div>
                <div class="card-body">
                    <div class="label">{account['label']}</div>
                    <div class="account-number" id="{account['id']}-number">{account['number']}</div>
                    <div class="account-name" id="{account['id']}-name">{account['owner']}</div>
                </div>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)
            
            # Tombol copy
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button(f"📋 Salin", key=f"btn_{account['id']}", use_container_width=True):
                    # JavaScript untuk copy ke clipboard
                    copy_js = f"""
                    <script>
                        navigator.clipboard.writeText('{account['number']}');
                        parent.document.dispatchEvent(new Event('copy-success'));
                    </script>
                    """
                    st.components.v1.html(copy_js, height=0)
                    
                    # Simpan log
                    save_log_func(account['name'], account['number'])
                    
                    # Tampilkan pesan sukses
                    st.success(f"✅ Nomor {account['name']} berhasil disalin!", icon="✅")
                    st.balloons()
            
            st.markdown("<br>", unsafe_allow_html=True)