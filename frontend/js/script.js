// Mobile menu toggle
document.addEventListener('DOMContentLoaded', function() {
    // Set current year in footer
    document.querySelectorAll('#currentYear').forEach(function(element) {
      element.textContent = new Date().getFullYear();
    });
  
    // Mobile menu toggle
    const menuToggle = document.getElementById('menuToggle');
    const mobileMenu = document.getElementById('mobileMenu');
  
    if (menuToggle && mobileMenu) {
      menuToggle.addEventListener('click', function() {
        mobileMenu.classList.toggle('open');
      });
    }
  
    // File upload functionality
    const uploadArea = document.getElementById('uploadArea');
    const fileInput = document.getElementById('fileInput');
    const uploadPrompt = document.getElementById('uploadPrompt');
    const imagePreview = document.getElementById('imagePreview');
    const previewImg = document.getElementById('previewImg');
    const dragFileElement = document.getElementById('dragFileElement');
  
    if (uploadArea && fileInput) {
      // Click to upload
      uploadArea.addEventListener('click', function() {
        fileInput.click();
      });
  
      // File input change
      fileInput.addEventListener('change', function() {
        handleFile(this.files[0]);
      });
  
      // Drag and drop events
      ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        uploadArea.addEventListener(eventName, preventDefaults, false);
      });
  
      function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
      }
  
      ['dragenter', 'dragover'].forEach(eventName => {
        uploadArea.addEventListener(eventName, highlight, false);
      });
  
      ['dragleave', 'drop'].forEach(eventName => {
        uploadArea.addEventListener(eventName, unhighlight, false);
      });
  
      function highlight() {
        uploadArea.classList.add('drag-active');
        dragFileElement.style.display = 'flex';
      }
  
      function unhighlight() {
        uploadArea.classList.remove('drag-active');
        dragFileElement.style.display = 'none';
      }
  
      uploadArea.addEventListener('drop', handleDrop, false);
  
      function handleDrop(e) {
        const dt = e.dataTransfer;
        const file = dt.files[0];
        handleFile(file);
      }
  
      function handleFile(file) {
        if (file && file.type.startsWith('image/')) {
          if (file.size <= 5 * 1024 * 1024) { // 5MB max
            const reader = new FileReader();
            reader.onload = function(e) {
              previewImg.src = e.target.result;
              uploadPrompt.style.display = 'none';
              imagePreview.style.display = 'block';
            };
            reader.readAsDataURL(file);
          } else {
            alert('File size should be less than 5MB');
          }
        } else {
          alert('Please upload an image file');
        }
      }
    }
  
    // Form submission
    const animalForm = document.getElementById('animalForm');
    if (animalForm) {
      animalForm.addEventListener('submit', function(e) {
        e.preventDefault();
        alert('Form submitted successfully!');
        // Here you would typically send the form data to a server
      });
    }
  });