// ملف JavaScript الرئيسي لموقع شركة الصانع

document.addEventListener('DOMContentLoaded', function() {
    // التحقق من وجود نموذج الاتصال وإضافة تنسيق Bootstrap للحقول
    const contactForm = document.querySelector('form');
    if (contactForm) {
        const formInputs = contactForm.querySelectorAll('input, textarea, select');
        formInputs.forEach(input => {
            if (!input.classList.contains('form-control') && input.type !== 'hidden' && input.type !== 'submit') {
                input.classList.add('form-control');
            }
        });
    }

    // تحريك البطاقات عند التمرير
    const scrollAnimations = () => {
        const cards = document.querySelectorAll('.card');
        cards.forEach(card => {
            const cardPosition = card.getBoundingClientRect().top;
            const screenPosition = window.innerHeight / 1.3;
            
            if (cardPosition < screenPosition) {
                card.classList.add('animated');
            }
        });
    };

    // التمرير السلس للروابط الداخلية
    const smoothScroll = () => {
        const internalLinks = document.querySelectorAll('a[href^="#"]');
        internalLinks.forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const targetId = this.getAttribute('href');
                if (targetId === '#') return;
                
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop - 70,
                        behavior: 'smooth'
                    });
                }
            });
        });
    };

    // إضافة سلوك التثبيت للقائمة عند التمرير
    const stickyHeader = () => {
        const header = document.querySelector('header');
        const sticky = header.offsetTop;
        
        window.onscroll = function() {
            if (window.pageYOffset > sticky) {
                header.classList.add('sticky');
            } else {
                header.classList.remove('sticky');
            }
            
            // تفعيل تأثيرات التمرير
            scrollAnimations();
        };
    };

    // تهيئة العناصر التفاعلية من Bootstrap
    const initBootstrapComponents = () => {
        // تهيئة tooltips
        const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
        
        // تهيئة popovers
        const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
        popoverTriggerList.map(function (popoverTriggerEl) {
            return new bootstrap.Popover(popoverTriggerEl);
        });
    };

    // تهيئة الوظائف
    smoothScroll();
    stickyHeader();
    scrollAnimations();
    
    // التحقق من وجود Bootstrap قبل تهيئة المكونات
    if (typeof bootstrap !== 'undefined') {
        initBootstrapComponents();
    }

    // عداد تنازلي للعروض المحدودة (إذا وجدت)
    const countdownElement = document.getElementById('countdown');
    if (countdownElement) {
        const countDownDate = new Date(countdownElement.getAttribute('data-end-date')).getTime();
        
        const countdown = setInterval(function() {
            const now = new Date().getTime();
            const distance = countDownDate - now;
            
            if (distance < 0) {
                clearInterval(countdown);
                countdownElement.innerHTML = "انتهى العرض";
                return;
            }
            
            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);
            
            countdownElement.innerHTML = `${days} يوم ${hours} ساعة ${minutes} دقيقة ${seconds} ثانية`;
        }, 1000);
    }
}); 