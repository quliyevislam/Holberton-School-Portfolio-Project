document.addEventListener('DOMContentLoaded', function () {
    // Set current year in footer
    document.getElementById('currentYear').textContent = new Date().getFullYear();

    // Mobile menu toggle
    const menuToggle = document.getElementById('menuToggle');
    const mobileMenu = document.getElementById('mobileMenu');

    if (menuToggle && mobileMenu) {
        menuToggle.addEventListener('click', function () {
            mobileMenu.classList.toggle('open');
        });
    }

    // Password visibility toggle
    const togglePassword = document.getElementById('togglePassword');
    const password = document.getElementById('password');
    const toggleConfirmPassword = document.getElementById('toggleConfirmPassword');
    const confirmPassword = document.getElementById('confirmPassword');

    if (togglePassword && password) {
        togglePassword.addEventListener('click', function () {
            const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
            password.setAttribute('type', type);

            // Toggle the eye icon
            const icon = this.querySelector('i');
            if (type === 'password') {
                icon.classList.remove('fa-eye');
                icon.classList.add('fa-eye-slash');
            } else {
                icon.classList.remove('fa-eye-slash');
                icon.classList.add('fa-eye');
            }
        });
    }

    if (toggleConfirmPassword && confirmPassword) {
        toggleConfirmPassword.addEventListener('click', function () {
            const type = confirmPassword.getAttribute('type') === 'password' ? 'text' : 'password';
            confirmPassword.setAttribute('type', type);

            // Toggle the eye icon
            const icon = this.querySelector('i');
            if (type === 'password') {
                icon.classList.remove('fa-eye');
                icon.classList.add('fa-eye-slash');
            } else {
                icon.classList.remove('fa-eye-slash');
                icon.classList.add('fa-eye');
            }
        });
    }

    // Password strength meter
    if (password) {
        password.addEventListener('input', function () {
            const value = this.value;
            const strengthSegments = document.querySelectorAll('.strength-segment');
            const strengthText = document.getElementById('strengthText');

            // Reset all segments
            strengthSegments.forEach(segment => {
                segment.classList.remove('active');
            });

            // Check password strength
            let strength = 0;

            if (value.length >= 8) strength++;
            if (/[A-Z]/.test(value)) strength++;
            if (/[0-9]/.test(value)) strength++;
            if (/[^A-Za-z0-9]/.test(value)) strength++;

            // Update strength meter
            for (let i = 0; i < strength; i++) {
                if (strengthSegments[i]) {
                    strengthSegments[i].classList.add('active');
                }
            }

            // Update strength text
            let strengthLabel = 'Weak';
            if (strength === 2) strengthLabel = 'Fair';
            if (strength === 3) strengthLabel = 'Good';
            if (strength === 4) strengthLabel = 'Strong';

            if (strengthText) {
                strengthText.textContent = strengthLabel;
            }
        });
    }

    // Signup form submission
    const signupForm = document.getElementById('signupForm');
    if (signupForm) {
        signupForm.addEventListener('submit', function (e) {
            // Get form values
            const firstName = document.getElementById('firstName').value.trim();
            const lastName = document.getElementById('lastName').value.trim();
            const email = document.getElementById('email').value.trim();
            const password = document.getElementById('password').value;
            const confirmPassword = document.getElementById('confirmPassword').value;
            const agreeTerms = document.getElementById('agreeTerms').checked;

            // Validate inputs
            if (!firstName || !lastName || !email || !password || !confirmPassword) {
                alert('Please fill in all required fields.');
                e.preventDefault(); // Prevent submission only if validation fails
                return;
            }

            if (password !== confirmPassword) {
                alert('Passwords do not match!');
                e.preventDefault(); // Prevent submission only if validation fails
                return;
            }

            if (!agreeTerms) {
                alert('You must agree to the Terms of Service and Privacy Policy.');
                e.preventDefault(); // Prevent submission only if validation fails
                return;
            }

            // Allow the form to submit naturally to the backend
        });
    }

    // Back to top button
    const backToTopButton = document.getElementById('backToTop');

    if (backToTopButton) {
        window.addEventListener('scroll', function () {
            if (window.pageYOffset > 300) {
                backToTopButton.classList.add('visible');
            } else {
                backToTopButton.classList.remove('visible');
            }
        });

        backToTopButton.addEventListener('click', function () {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
});