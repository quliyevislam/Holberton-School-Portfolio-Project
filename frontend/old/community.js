document.addEventListener('DOMContentLoaded', function () {
  // Set current year in footer
  document.getElementById('currentYear').textContent = new Date().getFullYear();

  // Tab functionality
  const tabButtons = document.querySelectorAll('.tab-button');
  const tabContents = document.querySelectorAll('.tab-content');

  tabButtons.forEach(button => {
    button.addEventListener('click', function () {
      tabButtons.forEach(btn => btn.classList.remove('active'));
      tabContents.forEach(content => content.classList.remove('active'));
      this.classList.add('active');
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
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // Load community data
  function loadCommunityData() {
    const posts = JSON.parse(localStorage.getItem('communityPosts') || '[]');
    const feedTab = document.getElementById('feed');

    if (posts.length > 0) {
      let postsHTML = '';
      posts.forEach(post => {
        postsHTML += `
          <div class="post-card">
            <!-- Post content would go here -->
          </div>
        `;
      });

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
  }
  loadCommunityData();

  // Feed post and photo handlers
  const createPostInput = document.querySelector('#feed .create-post-input');
  const postButton = document.querySelector('#feed .primary-button');
  const photoButton = document.querySelector('#feed .post-type-button');

  const photoInput = document.createElement('input');
  photoInput.type = 'file';
  photoInput.accept = 'image/*';
  photoInput.style.display = 'none';
  document.body.appendChild(photoInput);

  let selectedImageURL = null;

  photoButton?.addEventListener('click', function () {
    photoInput.click();
  });

  photoInput.addEventListener('change', function () {
    const file = this.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function (e) {
        selectedImageURL = e.target.result;
      };
      reader.readAsDataURL(file);
    }
  });

  postButton?.addEventListener('click', function () {
    const postText = createPostInput.value.trim();
    if (!postText && !selectedImageURL) {
      alert("Please enter some text or choose a photo.");
      return;
    }

    const postContainer = document.createElement('div');
    postContainer.classList.add('post');

    let imageHTML = '';
    if (selectedImageURL) {
      imageHTML = `
        <div class="post-image">
          <img src="${selectedImageURL}" alt="Posted image">
        </div>
      `;
    }

    postContainer.innerHTML = `
      <div class="post-header">
        <div class="post-avatar">
          <img src="./assets/images/pfp.png" alt="User avatar">
        </div>
        <div class="post-meta">
          <div class="post-author">You</div>
          <div class="post-time">Just now</div>
        </div>
      </div>
      <div class="post-content">
        <p class="post-text">${postText}</p>
        ${imageHTML}
      </div>
      <div class="post-actions">
        <div class="post-action">
          <i class="far fa-heart"></i>
          <span>0 Likes</span>
        </div>
        <div class="post-action">
          <i class="far fa-comment"></i>
          <span>0 Comments</span>
        </div>
        <div class="post-action">
          <i class="far fa-share-square"></i>
          <span>Share</span>
        </div>
      </div>
    `;

    const feedContainer = document.getElementById('feed');
    feedContainer.insertBefore(postContainer, feedContainer.children[1]);
    createPostInput.value = '';
    selectedImageURL = null;
    photoInput.value = null;
  });

  // Discussion handlers
  const discussionSection = document.querySelector('#discussions .create-post');
  const discussionInput = discussionSection?.querySelector('.create-post-input');
  const addTopicButton = discussionSection?.querySelector('.post-type-button');
  const createDiscussionButton = discussionSection?.querySelector('.primary-button');
  let selectedTopic = '';

  addTopicButton?.addEventListener('click', function () {
    const topic = prompt("Enter discussion topic:");
    if (topic) {
      selectedTopic = topic;
      addTopicButton.innerHTML = `<i class="fas fa-tag"></i> ${topic}`;
    }
  });

  createDiscussionButton?.addEventListener('click', function () {
    const discussionText = discussionInput.value.trim();
    if (!discussionText) {
      alert("Please enter discussion text.");
      return;
    }

    const discussionItem = document.createElement('div');
    discussionItem.classList.add('discussion-item');
    discussionItem.innerHTML = `
      <div class="discussion-header">
        <h3 class="discussion-title">${discussionText}</h3>
        <span class="discussion-category">${selectedTopic || "General"}</span>
      </div>
      <div class="discussion-meta">
        <div class="discussion-meta-item">
          <i class="far fa-user"></i>
          <span>Started by You</span>
        </div>
        <div class="discussion-meta-item">
          <i class="far fa-comment"></i>
          <span>0 replies</span>
        </div>
        <div class="discussion-meta-item">
          <i class="far fa-clock"></i>
          <span>Just now</span>
        </div>
      </div>
    `;

    const discussionList = document.querySelector('#discussions .discussion-list');
    discussionList.insertBefore(discussionItem, discussionList.firstChild);
    discussionInput.value = '';
    selectedTopic = '';
    addTopicButton.innerHTML = `<i class="fas fa-tag"></i> Add Topic`;
  });

  // Like toggle
  document.addEventListener('click', function (event) {
    const action = event.target.closest('.post-action');
    if (!action) return;

    const heartIcon = action.querySelector('i');
    if (heartIcon && heartIcon.classList.contains('fa-heart')) {
      const span = action.querySelector('span');
      let count = parseInt(span.textContent) || 0;

      if (action.classList.contains('liked')) {
        action.classList.remove('liked');
        count = Math.max(count - 1, 0);
      } else {
        action.classList.add('liked');
        count++;
      }
      span.textContent = `${count} Likes`;
    }
  });

});