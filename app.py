import streamlit as st

st.set_page_config(page_title="Nomor Pembayaran", page_icon="💳")

# DATA PEMBAYARAN
payment_data = {
    "Bank BRI": "1234567890",
    "SeaBank": "0987654321",
    "ShopeePay": "081234567890",
    "DANA": "081234567890",
    "GoPay": "081234567890"
}

# JUDUL
st.title("Ini No Rekening Saya")
st.write("Silakan gunakan salah satu metode pembayaran di bawah ini")

st.divider()

# CARD STYLE SIMPLE
for name, number in payment_data.items():
    st.subheader(name)
    st.code(number)

    if st.button(f"Salin {name}"):
        st.write("Nomor disalin:", number)

st.divider()

# FOOTER
st.markdown("### Terima kasih 🙏")
st.write("Silakan konfirmasi ulang ke saya untuk memastikan transaksi Anda berhasil.")
