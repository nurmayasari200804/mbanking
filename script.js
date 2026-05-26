// JavaScript untuk interaktivitas tambahan

// Fungsi untuk menampilkan toast notification
function showToast(message, type = 'success') {
    // Cek apakah toast container sudah ada
    let toast = document.querySelector('.toast-notification');
    
    if (!toast) {
        toast = document.createElement('div');
        toast.className = 'toast-notification';
        document.body.appendChild(toast);
    }
    
    const icon = type === 'success' ? '✅' : '❌';
    toast.innerHTML = `<span class="toast-icon">${icon}</span><span>${message}</span>`;
    toast.classList.add('show');
    
    setTimeout(() => {
        toast.classList.remove('show');
    }, 2000);
}

// Fungsi untuk copy ke clipboard
async function copyToClipboard(text, methodName) {
    try {
        await navigator.clipboard.writeText(text);
        showToast(`Nomor ${methodName} berhasil disalin!`, 'success');
        
        // Trigger event untuk logging
        const event = new CustomEvent('copy-success', {
            detail: { method: methodName, number: text }
        });
        document.dispatchEvent(event);
        
        return true;
    } catch (err) {
        console.error('Gagal menyalin:', err);
        showToast('Gagal menyalin, silakan copy manual', 'error');
        return false;
    }
}

// Event listener untuk semua tombol copy di HTML
document.querySelectorAll('.copy-button').forEach(button => {
    button.addEventListener('click', async function(e) {
        e.preventDefault();
        e.stopPropagation();
        
        const method = this.getAttribute('data-method');
        const number = this.getAttribute('data-number');
        
        // Animasi tombol
        const originalHTML = this.innerHTML;
        this.innerHTML = '<span class="copy-icon">✅</span> Tersalin!';
        this.style.background = '#34c759';
        
        await copyToClipboard(number, method);
        
        setTimeout(() => {
            this.innerHTML = originalHTML;
            this.style.background = '#0052cc';
        }, 1500);
    });
});

// Klik di card juga bisa copy
document.querySelectorAll('.payment-card').forEach(card => {
    card.addEventListener('click', (e) => {
        // Jangan trigger jika klik tombol
        if (e.target.closest('.copy-button')) return;
        
        const copyBtn = card.querySelector('.copy-button');
        if (copyBtn) {
            copyBtn.click();
        }
    });
});

// Animasi hover pada card
document.querySelectorAll('.payment-card').forEach(card => {
    card.addEventListener('mouseenter', () => {
        card.style.transform = 'translateY(-2px)';
    });
    
    card.addEventListener('mouseleave', () => {
        card.style.transform = 'translateY(0)';
    });
});

// Log ke console
console.log('%c✨ Payment Methods Loaded! ✨', 'color: #0052cc; font-size: 14px; font-weight: bold;');
console.log('%c📋 Data pembayaran Nurmayasari Usman siap digunakan', 'color: #34c759; font-size: 12px;');

// Tampilkan timestamp
const now = new Date();
console.log(`📅 Loaded at: ${now.toLocaleString('id-ID')}`);

// Page view tracking (opsional)
document.addEventListener('DOMContentLoaded', () => {
    console.log('📄 Page loaded completely');
    
    // Event listener untuk copy success
    document.addEventListener('copy-success', (e) => {
        console.log(`📋 Copy event: ${e.detail.method} - ${e.detail.number}`);
    });
});