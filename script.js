function copyText() {
    const text = `
BRI
SeaBank
DANA / GOPAY
ShopeePay
    `;

    navigator.clipboard.writeText(text);
    alert("Info pembayaran berhasil disalin!");
}
