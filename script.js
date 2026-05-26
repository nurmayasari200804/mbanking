function copyText(id) {
    const text = document.getElementById(id).innerText;

    navigator.clipboard.writeText(text);

    alert("Nomor berhasil disalin: " + text);
}