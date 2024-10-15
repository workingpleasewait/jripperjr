document.addEventListener('DOMContentLoaded', function() {
    // Newsletter form submission
    const newsletterForm = document.getElementById('newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const email = this.querySelector('input[type="email"]').value;
            subscribeToNewsletter(email)
                .then(message => {
                    alert(message);
                    this.reset();
                })
                .catch(handleError);
        });
    }

    // Contact form submission
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            sendContactForm(this)
                .then(message => {
                    alert(message);
                    this.reset();
                })
                .catch(handleError);
        });
    }
});

function subscribeToNewsletter(email) {
    return fetch('/subscribe', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `email=${encodeURIComponent(email)}`
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if (data.success) {
            return data.message;
        } else {
            throw new Error(data.message);
        }
    });
}

function sendContactForm(form) {
    const formData = new FormData(form);
    return fetch('/contact', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if (data.success) {
            return data.message;
        } else {
            throw new Error(data.message);
        }
    });
}

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const targetId = this.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetId);
        if (targetElement) {
            targetElement.scrollIntoView({
                behavior: 'smooth'
            });
        } else {
            console.warn(`Element with id "${targetId}" not found`);
        }
    });
});

// Lazy loading for images
if ('loading' in HTMLImageElement.prototype) {
    const images = document.querySelectorAll('img[loading="lazy"]');
    images.forEach(img => {
        img.src = img.dataset.src;
    });
} else {
    // Fallback for browsers that don't support lazy loading
    loadLazyLoadingScript().catch(handleError);
}

function loadLazyLoadingScript() {
    return new Promise((resolve, reject) => {
        const script = document.createElement('script');
        script.src = 'https://cdnjs.cloudflare.com/ajax/libs/lazysizes/5.3.2/lazysizes.min.js';
        script.onload = resolve;
        script.onerror = reject;
        document.body.appendChild(script);
    });
}

// Updated error handler
function handleError(error) {
    console.error('An error occurred:', error);
    if (error.code === 4001) {
        console.log('User cancelled the operation. This is likely due to a browser extension or security setting.');
    } else if (error instanceof TypeError) {
        console.log('A type error occurred. This might be due to unexpected data formats.');
    } else if (error instanceof NetworkError) {
        console.log('A network error occurred. Please check your internet connection.');
    } else {
        alert('An unexpected error occurred. Please try again later.');
    }
}

// Global unhandled rejection handler
window.addEventListener('unhandledrejection', function(event) {
    event.preventDefault();
    handleError(event.reason);
});
