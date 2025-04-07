document.addEventListener('DOMContentLoaded', function () {
    // Set current year in footer
    document.getElementById('currentYear').textContent = new Date().getFullYear();

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

    // Mobile menu toggle
    const menuToggle = document.getElementById('menuToggle');
    const mobileMenu = document.getElementById('mobileMenu');

    if (menuToggle && mobileMenu) {
      menuToggle.addEventListener('click', function () {
        mobileMenu.classList.toggle('open');
      });
    }

    // Function to check if there are any community posts/events and load them
    function loadCommunityData() {
      // This function would check for data in localStorage or from an API
      // and populate the appropriate sections if data exists

      // Example of how you might check for posts:
      const posts = JSON.parse(localStorage.getItem('communityPosts') || '[]');
      const feedTab = document.getElementById('feed');

      if (posts.length > 0) {
        // If there are posts, replace the empty state with actual posts
        let postsHTML = '';

        posts.forEach(post => {
          // Create HTML for each post
          postsHTML += `
            <div class="post-card">
              <!-- Post content would go here -->
            </div>
          `;
        });

        // Replace empty state with posts
        feedTab.innerHTML = `
          <div class="create-post">
            <div class="create-post-header">
              <div class="create-post-avatar">
                <i class="fas fa-user"></i>
              </div>
              <input type="text" class="create-post-input" placeholder="Share something with the community...">
            </div>
            <div class="create-post-actions">
              <div class="post-type-buttons">
                <button class="post-type-button">
                  <i class="fas fa-image"></i> Photo
                </button>
                <button class="post-type-button">
                  <i class="fas fa-file-alt"></i> Article
                </button>
              </div>
              <button class="primary-button">
                <i class="fas fa-paper-plane"></i> Post
              </button>
            </div>
          </div>
          ${postsHTML}
        `;
      }

      // Similar checks could be done for events, discussions, etc.
    }

    // Load community data when the page loads
    loadCommunityData();
  });

  document.addEventListener('DOMContentLoaded', function () {
    const menuToggle = document.getElementById('menuToggle');
    const mobileMenu = document.getElementById('mobileMenu');

    if (menuToggle && mobileMenu) {
      menuToggle.addEventListener('click', function () {
        mobileMenu.classList.toggle('open');
      });
    }
  });