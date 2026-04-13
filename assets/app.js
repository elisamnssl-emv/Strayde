// ==========================================
// 1. GESTION DES ACCORDÉONS (Desktop & FAQ)
// ==========================================
function toggleAccordion(btn) {
    const item = btn.closest('.accordion-item');
    const content = item.querySelector('.accordion-content');
    const isOpen = item.classList.contains('open');

    // Ferme les autres accordéons ouverts
    document.querySelectorAll('.accordion-item.open').forEach(el => {
        el.classList.remove('open');
        if (el.querySelector('.accordion-content')) {
            el.querySelector('.accordion-content').classList.remove('open');
        }
    });

    // Ouvre celui cliqué
    if (!isOpen) {
        item.classList.add('open');
        content.classList.add('open');
    }
}

function toggleFaq(btn) {
    const content = btn.querySelector('.faq-answer') || btn.nextElementSibling;
    const icon = btn.querySelector('.faq-icon');

    if (content.style.display === 'block') {
        content.style.display = 'none';
        if (icon) icon.style.transform = 'rotate(0deg)';
    } else {
        content.style.display = 'block';
        if (icon) icon.style.transform = 'rotate(45deg)';
    }
}

// ==========================================
// 2. GESTION DES MENUS MOBILES
// ==========================================
function toggleMobAccordion(id, btn) {
    var body = document.getElementById(id);
    var chevron = btn.querySelector('[data-lucide="chevron-down"]');
    if (body.classList.contains('hidden')) {
        body.classList.remove('hidden');
        if (chevron) chevron.style.transform = 'rotate(180deg)';
    } else {
        body.classList.add('hidden');
        if (chevron) chevron.style.transform = '';
    }
    // Rafraîchir les icônes Lucide si nécessaire
    if (window.lucide) lucide.createIcons();
}

// ==========================================
// 3. CARROUSEL DES AVIS / LOGOS
// ==========================================
document.addEventListener('DOMContentLoaded', function () {
    var rc = document.getElementById('reviews-carousel') || document.getElementById('race-carousel');
    if (!rc) return;

    var isDown = false, startX, scrollLeft, paused = false, speed = 0.6;

    rc.addEventListener('mousedown', function (e) {
        isDown = true; paused = true;
        rc.style.scrollBehavior = 'auto';
        rc.style.scrollSnapType = 'none';
        rc.classList.add('active');
        startX = e.pageX - rc.offsetLeft;
        scrollLeft = rc.scrollLeft;
    });

    rc.addEventListener('mouseleave', function () {
        if (isDown) {
            isDown = false;
            rc.style.scrollSnapType = 'x mandatory';
            rc.style.scrollBehavior = 'smooth';
        }
        paused = false;
    });

    rc.addEventListener('mouseup', function () {
        isDown = false;
        rc.style.scrollSnapType = 'x mandatory';
        rc.style.scrollBehavior = 'smooth';
        setTimeout(function () { paused = false; }, 1200);
    });

    rc.addEventListener('mousemove', function (e) {
        if (!isDown) return;
        e.preventDefault();
        rc.scrollLeft = scrollLeft - (e.pageX - rc.offsetLeft - startX);
    });

    rc.addEventListener('mouseenter', function () { if (!isDown) paused = true; });
    rc.addEventListener('touchstart', function () { paused = true; }, { passive: true });
    rc.addEventListener('touchend', function () { setTimeout(function () { paused = false; }, 1500); }, { passive: true });

    function tick() {
        if (!paused && !isDown) {
            rc.scrollLeft += speed;
            if (rc.scrollLeft >= rc.scrollWidth - rc.clientWidth - 1) rc.scrollLeft = 0;
        }
        requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
});