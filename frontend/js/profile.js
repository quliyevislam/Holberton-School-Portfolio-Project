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

    // Tab functionality
    const tabButtons = document.querySelectorAll('.tab-button');
    const tabContents = document.querySelectorAll('.tab-content');

    tabButtons.forEach(button => {
        button.addEventListener('click', function () {
            // Remove active class from all buttons and contents
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));

            // Add active class to clicked button
            this.classList.add('active');

            // Show corresponding content
            const tabId = this.getAttribute('data-tab');
            document.getElementById(tabId).classList.add('active');
        });
    });

    // Profile picture upload
    const changePictureBtn = document.getElementById('changePictureBtn');
    const pictureUpload = document.getElementById('pictureUpload');
    const profilePicture = document.getElementById('profilePicture');

    if (changePictureBtn && pictureUpload) {
        changePictureBtn.addEventListener('click', function () {
            pictureUpload.click();
        });

        pictureUpload.addEventListener('change', function () {
            const file = this.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function (e) {
                    profilePicture.src = e.target.result;
                };
                reader.readAsDataURL(file);
            }
        });
    }

    // Edit profile modal
    const editProfileBtn = document.getElementById('editProfileBtn');
    const editProfileModal = document.getElementById('editProfileModal');
    const closeModalBtn = document.getElementById('closeModalBtn');
    const cancelEditBtn = document.getElementById('cancelEditBtn');
    const editProfileForm = document.getElementById('editProfileForm');

    if (editProfileBtn && editProfileModal && closeModalBtn && cancelEditBtn) {
        // Open modal
        editProfileBtn.addEventListener('click', function () {
            editProfileModal.style.display = 'flex';
        });

        // Close modal functions
        function closeModal() {
            editProfileModal.style.display = 'none';
        }

        closeModalBtn.addEventListener('click', closeModal);
        cancelEditBtn.addEventListener('click', closeModal);

        // Close when clicking outside the modal
        window.addEventListener('click', function (event) {
            if (event.target === editProfileModal) {
                closeModal();
            }
        });
    }

    // Form submission
    if (editProfileForm) {
        editProfileForm.addEventListener('submit', function (e) {
            e.preventDefault();

            // Get form values
            const fullName = document.getElementById('fullName').value;
            const email = document.getElementById('email').value;
            const phone = document.getElementById('phone').value;
            const currentPassword = document.getElementById('currentPassword').value;
            const newPassword = document.getElementById('newPassword').value;
            const confirmPassword = document.getElementById('confirmPassword').value;

            // Validate form
            if (!fullName || !email || !currentPassword) {
                alert('Please fill in all required fields.');
                return;
            }

            if (newPassword && newPassword !== confirmPassword) {
                alert('New passwords do not match.');
                return;
            }

            // Here you would typically send the data to your backend
            console.log('Profile update data:', {
                fullName,
                email,
                phone,
                newPassword: newPassword ? '(password changed)' : '(unchanged)'
            });

            // Update profile info in the UI
            document.querySelector('.profile-name').textContent = fullName;
            const contactInfo = document.querySelector('.profile-contact');
            contactInfo.innerHTML = `<p>${email}</p><p>${phone}</p>`;

            // Show success message and close modal
            alert('Profile updated successfully!');
            closeModal();
        });
    }

    // Function to check for reports and render them
    function checkForReports() {
        const reports = JSON.parse(localStorage.getItem('animalReports') || '[]');
        const reportsTab = document.getElementById('reports');

        if (reports.length > 0) {
            // If there are reports, clear the empty state and render them
            reportsTab.innerHTML = '';

            reports.forEach(report => {
                // Create and append report cards here
                // This would be populated with actual user data when available
            });
        }
    }

    // Function to check for posts and render them
    function checkForPosts() {
        const posts = JSON.parse(localStorage.getItem('userPosts') || '[]');
        const postsTab = document.getElementById('posts');

        if (posts.length > 0) {
            // If there are posts, clear the empty state and render them
            postsTab.innerHTML = '';

            posts.forEach(post => {
                // Create and append post cards here
                // This would be populated with actual user data when available
            });
        }
    }

    // Function to check for comments and render them
    function checkForComments() {
        const comments = JSON.parse(localStorage.getItem('userComments') || '[]');
        const commentsTab = document.getElementById('comments');

        if (comments.length > 0) {
            // If there are comments, clear the empty state and render them
            commentsTab.innerHTML = '';

            comments.forEach(comment => {
                // Create and append comment cards here
                // This would be populated with actual user data when available
            });
        }
    }

    // Check for user data
    checkForReports();
    checkForPosts();
    checkForComments();

      // Back to top button
  const backToTopButton = document.getElementById('backToTop');
  
  if (backToTopButton) {
    window.addEventListener('scroll', function() {
      if (window.pageYOffset > 300) {
        backToTopButton.classList.add('visible');
      } else {
        backToTopButton.classList.remove('visible');
      }
    });
    
    backToTopButton.addEventListener('click', function() {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }
});