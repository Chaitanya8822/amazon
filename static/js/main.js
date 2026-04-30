/* =============================================
   Amazon Clone – Main JavaScript
   ============================================= */

document.addEventListener('DOMContentLoaded', function () {

    // ---- Auto-dismiss alerts after 4 seconds ----
    const alerts = document.querySelectorAll('.alert.alert-dismissible');
    alerts.forEach(function (alert) {
        setTimeout(function () {
            const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
            if (bsAlert) bsAlert.close();
        }, 4000);
    });


    // ---- Quantity input: enforce min=1, max=stock ----
    const qtySelects = document.querySelectorAll('select[name="quantity"]');
    qtySelects.forEach(function (sel) {
        sel.addEventListener('change', function () {
            const val = parseInt(sel.value);
            if (isNaN(val) || val < 1) sel.value = 1;
        });
    });


    // ---- Add to Cart button feedback ----
    const cartForms = document.querySelectorAll('form[action*="/cart/add/"]');
    cartForms.forEach(function (form) {
        form.addEventListener('submit', function (e) {
            const btn = form.querySelector('button[type="submit"]');
            if (btn) {
                btn.disabled = true;
                btn.innerHTML = '<span class="spinner-border spinner-border-sm me-1"></span>Adding…';
            }
        });
    });


    // ---- Cart quantity auto-submit on change (desktop) ----
    const cartUpdateForms = document.querySelectorAll('form[action*="/cart/update/"]');
    cartUpdateForms.forEach(function (form) {
        const sel = form.querySelector('select[name="quantity"]');
        if (sel) {
            sel.addEventListener('change', function () {
                form.submit();
            });
        }
    });


    // ---- Sticky navbar shadow on scroll ----
    const navbar = document.querySelector('.amazon-navbar');
    if (navbar) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 10) {
                navbar.classList.add('shadow-lg');
            } else {
                navbar.classList.remove('shadow-lg');
            }
        });
    }


    // ---- Back to Top button ----
    const backToTopBtn = document.createElement('button');
    backToTopBtn.innerHTML = '<i class="bi bi-arrow-up"></i>';
    backToTopBtn.className = 'btn btn-warning btn-sm position-fixed bottom-0 end-0 m-4 rounded-circle back-to-top';
    backToTopBtn.style.cssText = 'width:44px;height:44px;display:none;z-index:1050;box-shadow:0 2px 8px rgba(0,0,0,0.3);';
    backToTopBtn.title = 'Back to top';
    document.body.appendChild(backToTopBtn);

    window.addEventListener('scroll', function () {
        backToTopBtn.style.display = window.scrollY > 300 ? 'block' : 'none';
    });

    backToTopBtn.addEventListener('click', function () {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });


    // ---- Tooltip initialization ----
    const tooltipEls = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    tooltipEls.forEach(function (el) {
        new bootstrap.Tooltip(el);
    });


    // ---- Product image zoom on hover (detail page) ----
    const detailImg = document.querySelector('.product-detail-img');
    if (detailImg) {
        detailImg.addEventListener('mouseenter', function () {
            detailImg.style.transform = 'scale(1.04)';
            detailImg.style.transition = 'transform 0.3s ease';
        });
        detailImg.addEventListener('mouseleave', function () {
            detailImg.style.transform = 'scale(1)';
        });
    }

});