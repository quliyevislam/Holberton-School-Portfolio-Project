document.addEventListener('DOMContentLoaded', function() {
    // Set current year in footer
    document.getElementById('currentYear').textContent = new Date().getFullYear();
    
    // Mobile menu toggle
    const menuToggle = document.getElementById('menuToggle');
    const mobileMenu = document.getElementById('mobileMenu');
    
    if (menuToggle && mobileMenu) {
      menuToggle.addEventListener('click', function() {
        mobileMenu.classList.toggle('open');
      });
    }
    
    // Set today's date as default for date field
    const dateField = document.getElementById('dateFound');
    if (dateField) {
      const today = new Date();
      const year = today.getFullYear();
      let month = today.getMonth() + 1;
      let day = today.getDate();
      
      month = month < 10 ? '0' + month : month;
      day = day < 10 ? '0' + day : day;
      
      dateField.value = `${year}-${month}-${day}`;
    }
    
    // Set current time as default for time field
    const timeField = document.getElementById('timeFound');
    if (timeField) {
      const now = new Date();
      let hours = now.getHours();
      let minutes = now.getMinutes();
      
      hours = hours < 10 ? '0' + hours : hours;
      minutes = minutes < 10 ? '0' + minutes : minutes;
      
      timeField.value = `${hours}:${minutes}`;
    }
    
    // File upload handling
    const uploadArea = document.getElementById('uploadArea');
    const fileInput = document.getElementById('photo');
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
            reader.onloadend = function() {
              previewImg.src = reader.result;
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
    const form = document.getElementById('animalReportForm');
    if (form) {
      form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Collect form data
        const formData = {
          name: document.getElementById('name').value,
          contact: document.getElementById('contact').value,
          animalType: document.getElementById('animalType').value,
          otherAnimalType: document.getElementById('otherAnimalType').value,
          colorMarkings: document.getElementById('colorMarkings').value,
          age: document.getElementById('age').value,
          healthStatus: document.getElementById('healthStatus').value,
          behavior: document.getElementById('behavior').value,
          injuries: document.getElementById('injuries').value,
          location: document.getElementById('location').value,
          dateFound: document.getElementById('dateFound').value,
          timeFound: document.getElementById('timeFound').value,
          notes: document.getElementById('notes').value
        };
        
        // Here you would typically send the data to your backend
        console.log('Form data:', formData);
        
        // For demo purposes, store in localStorage
        const reports = JSON.parse(localStorage.getItem('animalReports') || '[]');
        reports.push({
          ...formData,
          id: Date.now(),
          reportedAt: new Date().toISOString(),
          status: 'pending'
        });
        localStorage.setItem('animalReports', JSON.stringify(reports));
        
        alert('Thank you for your report! Animal rescue teams have been notified.');
        

        form.reset();
        uploadPrompt.style.display = 'block';
        imagePreview.style.display = 'none';
        

        if (dateField) {
          const today = new Date();
          const year = today.getFullYear();
          let month = today.getMonth() + 1;
          let day = today.getDate();
          
          month = month < 10 ? '0' + month : month;
          day = day < 10 ? '0' + day : day;
          
          dateField.value = `${year}-${month}-${day}`;
        }
        
        if (timeField) {
          const now = new Date();
          let hours = now.getHours();
          let minutes = now.getMinutes();
          
          hours = hours < 10 ? '0' + hours : hours;
          minutes = minutes < 10 ? '0' + minutes : minutes;
          
          timeField.value = `${hours}:${minutes}`;
        }
      });
    }
  });