// Fungsi untuk menampilkan toast notification
function showToast(message) {
    const toast = document.getElementById('toast');
    const toastMessage = document.getElementById('toast-message');
    
    toastMessage.textContent = message;
    toast.classList.add('show');
    
    setTimeout(() => {
        toast.classList.remove('show');
    }, 2000);
}

// Fungsi untuk menyalin teks ke clipboard
async function copyToClipboard(text, methodName) {
    try {
        await navigator.clipboard.writeText(text);
        showToast(`Nomor ${methodName} berhasil disalin!`);
    } catch (err) {
        console.error('Gagal menyalin: ', err);
        showToast('Gagal menyalin, silakan copy manual');
    }
}

// Event listener untuk semua tombol copy
document.querySelectorAll('.copy-btn').forEach(button => {
    button.addEventListener('click', async function(e) {
        e.preventDefault();
        e.stopPropagation();
        
        const targetId = this.getAttribute('data-target');
        const methodName = this.getAttribute('data-name');
        const accountElement = document.getElementById(targetId);
        
        if (accountElement) {
            const textToCopy = accountElement.textContent.trim();
            await copyToClipboard(textToCopy, methodName);
            
            // Animasi feedback pada tombol
            const originalHTML = this.innerHTML;
            this.innerHTML = '<i class="fas fa-check"></i> Tersalin!';
            this.style.background = '#34c759';
            
            setTimeout(() => {
                this.innerHTML = originalHTML;
                this.style.background = '#0052cc';
            }, 1500);
        }
    });
});

// Optional: Klik di card juga bisa copy (kecuali tombol)
document.querySelectorAll('.payment-card').forEach(card => {
    card.addEventListener('click', (e) => {
        // Jangan trigger jika yang diklik adalah tombol atau di dalam tombol
        if (e.target.closest('.copy-btn')) return;
        
        // Cari tombol copy di dalam card yang sama
        const copyBtn = card.querySelector('.copy-btn');
        if (copyBtn) {
            copyBtn.click();
        }
    });
});

console.log('✅ Payment Methods Loaded!');
console.log('📋 Data pembayaran Nurmayasari Usman siap digunakan');