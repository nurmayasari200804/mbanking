import streamlit as st
import pandas as pd

def show_sidebar():
    """Menampilkan sidebar dengan statistik dan riwayat"""
    with st.sidebar:
        st.markdown("### 📊 Statistik Copy")
        st.markdown(f"**Total copy:** {len(st.session_state.copy_logs)} kali")
        
        if st.session_state.copy_logs:
            st.markdown("### 📋 Riwayat Copy")
            logs_df = pd.DataFrame(st.session_state.copy_logs)
            
            # Tampilkan dataframe
            st.dataframe(logs_df, use_container_width=True, height=300)
            
            # Tombol hapus riwayat
            if st.button("🗑️ Hapus Riwayat", use_container_width=True):
                st.session_state.copy_logs = []
                st.rerun()
            
            # Tombol export
            if st.button("📥 Export CSV", use_container_width=True):
                csv = logs_df.to_csv(index=False)
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name="copy_logs.csv",
                    mime="text/csv"
                )
        else:
            st.info("Belum ada yang copy nomor")
        
        st.markdown("---")
        st.markdown("### ℹ️ Info")
        st.caption("© Nurmayasari Usman")