// Navigation interactions
const navLinks = document.querySelectorAll('nav a');
navLinks.forEach(link => {
    link.addEventListener('click', function() {
        navLinks.forEach(nav => nav.classList.remove('active'));
        this.classList.add('active');
    });
});

// Form validation
const form = document.getElementById('analysis-form');
form.addEventListener('submit', function(event) {
    const textArea = document.getElementById('text');
    if (textArea.value.trim() === '') {
        alert('Please enter some text for analysis.');
        event.preventDefault();
    }
});

// Smooth scrolling
const smoothScroll = function(targetEl, duration) {
    const target = document.querySelector(targetEl);
    const targetPosition = target.getBoundingClientRect().top;
    const startPosition = window.pageYOffset;
    const startTime = null;

    const ease = function(t, b, c, d) {
        t /= d / 2;
        if (t < 1) return c / 2 * t * t + b;
        t--;
        return -c / 2 * (t * (t - 2) - 1) + b;
    };

    const animation = function(currentTime) {
        if (startTime === null) startTime = currentTime;
        const timeElapsed = currentTime - startTime;
        const run = ease(timeElapsed, startPosition, targetPosition, duration);
        window.scrollTo(0, run);
        if (timeElapsed < duration) requestAnimationFrame(animation);
    };
    requestAnimationFrame(animation);
};

const scrollTo = document.querySelectorAll('.scroll-to');
scrollTo.forEach(each => {
    each.addEventListener('click', function() {
        const currentTarget = this.getAttribute('href');
        smoothScroll(currentTarget, 1000);
    });
});