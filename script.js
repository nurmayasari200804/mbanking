// Copy to clipboard functionality
function copyToClipboard(text) {
    // Create temporary input element
    const tempInput = document.createElement('input');
    tempInput.value = text;
    document.body.appendChild(tempInput);
    
    // Select and copy
    tempInput.select();
    tempInput.setSelectionRange(0, 99999);
    
    try {
        document.execCommand('copy');
        showNotification(`Copied: ${text}`);
    } catch (err) {
        console.error('Failed to copy: ', err);
        showNotification('Failed to copy. Please manually copy.');
    }
    
    // Clean up
    document.body.removeChild(tempInput);
}

// Show notification/toast
function showNotification(message) {
    // Remove existing notification
    const existingNotif = document.querySelector('.toast-notification');
    if (existingNotif) {
        existingNotif.remove();
    }
    
    // Create notification element
    const notif = document.createElement('div');
    notif.className = 'toast-notification';
    notif.innerHTML = `
        <div style="display: flex; align-items: center; gap: 10px;">
            <span>✅</span>
            <span>${message}</span>
        </div>
    `;
    
    document.body.appendChild(notif);
    
    // Auto remove after 2 seconds
    setTimeout(() => {
        if (notif && notif.remove) {
            notif.remove();
        }
    }, 2000);
}

// Add keyboard shortcuts (Ctrl/Cmd + C on account numbers)
document.addEventListener('keydown', function(e) {
    if ((e.ctrlKey || e.metaKey) && e.key === 'c') {
        const activeElement = document.activeElement;
        if (activeElement && activeElement.classList && activeElement.classList.contains('account-number')) {
            e.preventDefault();
            const text = activeElement.innerText.split('Copy')[0].trim();
            copyToClipboard(text);
        }
    }
});

// Add hover effect for all account numbers
document.addEventListener('DOMContentLoaded', function() {
    const accountNumbers = document.querySelectorAll('.account-number');
    accountNumbers.forEach(elem => {
        elem.addEventListener('click', function(e) {
            if (!e.target.classList.contains('copy-btn')) {
                const text = this.innerText.split('Copy')[0].trim();
                copyToClipboard(text);
            }
        });
        elem.style.cursor = 'pointer';
    });
});