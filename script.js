// Data akun pembayaran (bisa disesuaikan)
const paymentAccounts = {
    bri: {
        number: "1234-5678-9012-3456",
        name: "MUHAMMAD ANDIKA"
    },
    seabank: {
        number: "9012-3456-7890-1234",
        name: "ANDIKA SETIAWAN"
    },
    shopeepay: {
        number: "0812-3456-7890",
        name: "@andikaofficial"
    },
    dana: {
        number: "0852-1234-5678",
        name: "Andika Pratama"
    },
    gopay: {
        number: "0895-1234-5678",
        name: "Andika Nugraha"
    }
};

// Fungsi untuk menampilkan toast notification
function showToast(message = "Nomor berhasil disalin!") {
    const toast = document.getElementById('toast');
    const toastSpan = toast.querySelector('span');
    
    toastSpan.textContent = message;
    toast.classList.add('show');
    
    setTimeout(() => {
        toast.classList.remove('show');
    }, 2000);
}

// Fungsi untuk menyalin teks ke clipboard
async function copyToClipboard(text, methodName) {
    try {
        await navigator.clipboard.writeText(text);
        showToast(`${methodName} berhasil disalin!`);
        
        // Animasi tambahan pada card
        const activeCard = document.querySelector(`.payment-card[data-method="${methodName.toLowerCase()}"]`);
        if (activeCard) {
            activeCard.style.transform = 'scale(0.98)';
            setTimeout(() => {
                activeCard.style.transform = '';
            }, 200);
        }
    } catch (err) {
        console.error('Gagal menyalin: ', err);
        showToast('Gagal menyalin, coba manual ya!');
    }
}

// Event listener untuk semua tombol copy
document.querySelectorAll('.copy-btn').forEach(button => {
    button.addEventListener('click', (e) => {
        e.stopPropagation();
        
        const accountId = button.getAttribute('data-account');
        const accountElement = document.getElementById(accountId);
        
        if (accountElement) {
            const textToCopy = accountElement.textContent.trim();
            let methodName = '';
            
            // Menentukan metode pembayaran
            if (accountId.includes('bri')) methodName = 'BRI';
            else if (accountId.includes('seabank')) methodName = 'SeaBank';
            else if (accountId.includes('shopeepay')) methodName = 'ShopeePay';
            else if (accountId.includes('dana')) methodName = 'DANA';
            else if (accountId.includes('gopay')) methodName = 'GoPay';
            
            copyToClipboard(textToCopy, methodName);
        }
    });
});

// Animasi hover dan efek klik pada card
document.querySelectorAll('.payment-card').forEach(card => {
    card.addEventListener('click', (e) => {
        // Jangan trigger jika klik tombol copy
        if (e.target.closest('.copy-btn')) return;
        
        // Animasi ripple effect
        const ripple = document.createElement('div');
        ripple.classList.add('ripple');
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        ripple.style.left = `${x}px`;
        ripple.style.top = `${y}px`;
        card.style.position = 'relative';
        card.style.overflow = 'hidden';
        card.appendChild(ripple);
        
        setTimeout(() => {
            ripple.remove();
        }, 600);
        
        // Auto copy saat card diklik (opsional)
        const accountNumber = card.querySelector('.account-number');
        if (accountNumber) {
            const methodName = card.querySelector('h3').textContent;
            copyToClipboard(accountNumber.textContent.trim(), methodName);
        }
    });
});

// Tambahan CSS untuk ripple effect
const style = document.createElement('style');
style.textContent = `
    .ripple {
        position: absolute;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.6);
        transform: scale(0);
        animation: ripple-animation 0.6s linear;
        pointer-events: none;
        width: 100px;
        height: 100px;
        margin-left: -50px;
        margin-top: -50px;
    }
    
    @keyframes ripple-animation {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Menampilkan pesan selamat datang di console
console.log('%c✨ Payment Methods Loaded! ✨', 'color: #667eea; font-size: 16px; font-weight: bold;');
console.log('Silakan gunakan tombol copy untuk menyalin nomor pembayaran.');

// Optional: Menambahkan timestamp terakhir diupdate
const lastUpdate = new Date().toLocaleString('id-ID');
console.log(`📅 Last update: ${lastUpdate}`);